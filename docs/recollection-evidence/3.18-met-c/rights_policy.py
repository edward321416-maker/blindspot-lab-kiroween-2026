"""Fail-closed rights decisions for sanitized Met research output."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

Decision = Literal[
    "RIGHTS_REVIEW_HOLD",
    "METADATA_ONLY_ALLOWED",
    "AUTHORED_TEXT_ALLOWED",
    "IMAGE_REUSE_APPROVED",
]


@dataclass(frozen=True)
class RightsSignals:
    """Independent source signals and explicit reuse approvals for one object."""

    api_public_domain: bool
    page_public_domain: bool | None
    primary_image_present: bool
    image_download_available: bool | None
    metadata_reviewed: bool
    authored_text_approved: bool
    image_display_approved: bool
    third_party_fallback_requested: bool = False
    simulated_rights_change: str | None = None


def evaluate_rights(signals: RightsSignals) -> dict[str, dict[str, object]]:
    """Evaluate metadata, authored text, and image output independently."""
    # Runtime types matter: a string such as "false" is truthy in Python.
    # Reject invalid data at this exact approval boundary, even if constructed
    # through a dataclass with type hints or decoded from external JSON.
    required_bools = (
        "api_public_domain",
        "primary_image_present",
        "metadata_reviewed",
        "authored_text_approved",
        "image_display_approved",
        "third_party_fallback_requested",
    )
    valid = isinstance(signals, RightsSignals) and all(
        type(getattr(signals, field)) is bool for field in required_bools
    )
    if valid:
        valid = (
            (signals.page_public_domain is None or type(signals.page_public_domain) is bool)
            and (signals.image_download_available is None or type(signals.image_download_available) is bool)
            and (signals.simulated_rights_change is None or type(signals.simulated_rights_change) is str)
        )
    if not valid:
        return {
            slot: {"decision": "RIGHTS_REVIEW_HOLD", "reasons": ["INVALID_SIGNAL_TYPE"]}
            for slot in ("METADATA", "AUTHORED_TEXT", "IMAGE")
        }

    conflict = (
        signals.page_public_domain is not None
        and signals.api_public_domain != signals.page_public_domain
    )
    simulated = signals.simulated_rights_change is not None

    metadata_decision: Decision = (
        "METADATA_ONLY_ALLOWED" if signals.metadata_reviewed else "RIGHTS_REVIEW_HOLD"
    )
    authored_decision: Decision = (
        "AUTHORED_TEXT_ALLOWED"
        if signals.authored_text_approved and not simulated
        else "RIGHTS_REVIEW_HOLD"
    )
    image_allowed = all(
        (
            signals.api_public_domain,
            signals.page_public_domain is True,
            signals.primary_image_present,
            signals.image_download_available is True,
            signals.image_display_approved,
            not signals.third_party_fallback_requested,
            not simulated,
            not conflict,
        )
    )
    image_decision: Decision = (
        "IMAGE_REUSE_APPROVED" if image_allowed else "RIGHTS_REVIEW_HOLD"
    )

    image_reasons: list[str] = []
    if conflict:
        image_reasons.append("API_AND_ITEM_PAGE_RIGHTS_CONFLICT")
    if not signals.primary_image_present:
        image_reasons.append("PRIMARY_IMAGE_ABSENT")
    if signals.image_download_available is not True:
        image_reasons.append("DOWNLOAD_NOT_CONFIRMED")
    if not signals.api_public_domain:
        image_reasons.append("API_NOT_PUBLIC_DOMAIN")
    if signals.page_public_domain is not True:
        image_reasons.append("ITEM_PAGE_PUBLIC_DOMAIN_NOT_CONFIRMED")
    if not signals.image_display_approved:
        image_reasons.append("DISPLAY_NOT_APPROVED")
    if signals.third_party_fallback_requested:
        image_reasons.append("THIRD_PARTY_FALLBACK_FORBIDDEN")
    if simulated:
        image_reasons.append("SIMULATED_RIGHTS_CHANGE_NOT_REAL_EVIDENCE")

    return {
        "METADATA": {
            "decision": metadata_decision,
            "reasons": [] if signals.metadata_reviewed else ["METADATA_REVIEW_REQUIRED"],
        },
        "AUTHORED_TEXT": {
            "decision": authored_decision,
            "reasons": []
            if authored_decision == "AUTHORED_TEXT_ALLOWED"
            else ["AUTHORED_TEXT_APPROVAL_REQUIRED"],
        },
        "IMAGE": {
            "decision": image_decision,
            "reasons": image_reasons,
        },
    }

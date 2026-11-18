"""Eight synthetic rights and visitor-output safety tests."""

from __future__ import annotations

import unittest

from rights_policy import RightsSignals, evaluate_rights


def signals(
    *,
    api_public_domain: bool = True,
    page_public_domain: bool | None = True,
    primary_image_present: bool = True,
    image_download_available: bool | None = True,
    metadata_reviewed: bool = True,
    authored_text_approved: bool = True,
    image_display_approved: bool = True,
    third_party_fallback_requested: bool = False,
    simulated_rights_change: str | None = None,
) -> RightsSignals:
    """Build a synthetic state for one safety scenario."""
    return RightsSignals(
        api_public_domain=api_public_domain,
        page_public_domain=page_public_domain,
        primary_image_present=primary_image_present,
        image_download_available=image_download_available,
        metadata_reviewed=metadata_reviewed,
        authored_text_approved=authored_text_approved,
        image_display_approved=image_display_approved,
        third_party_fallback_requested=third_party_fallback_requested,
        simulated_rights_change=simulated_rights_change,
    )


class TestRightsPolicy(unittest.TestCase):
    """Exercise the preregistered R01-R08 fail-closed cases."""

    def test_r01_api_page_conflict_is_held(self) -> None:
        result = evaluate_rights(signals(api_public_domain=False))
        self.assertEqual(result["IMAGE"]["decision"], "RIGHTS_REVIEW_HOLD")
        self.assertIn("API_AND_ITEM_PAGE_RIGHTS_CONFLICT", result["IMAGE"]["reasons"])

    def test_r02_absent_primary_image_is_held(self) -> None:
        result = evaluate_rights(signals(primary_image_present=False))
        self.assertEqual(result["IMAGE"]["decision"], "RIGHTS_REVIEW_HOLD")
        self.assertIn("PRIMARY_IMAGE_ABSENT", result["IMAGE"]["reasons"])

    def test_r03_non_public_domain_with_url_is_held(self) -> None:
        result = evaluate_rights(
            signals(api_public_domain=False, page_public_domain=False)
        )
        self.assertEqual(result["IMAGE"]["decision"], "RIGHTS_REVIEW_HOLD")
        self.assertIn("API_NOT_PUBLIC_DOMAIN", result["IMAGE"]["reasons"])

    def test_r04_public_domain_url_without_display_approval_is_held(self) -> None:
        result = evaluate_rights(signals(image_display_approved=False))
        self.assertEqual(result["IMAGE"]["decision"], "RIGHTS_REVIEW_HOLD")
        self.assertIn("DISPLAY_NOT_APPROVED", result["IMAGE"]["reasons"])

    def test_r05_third_party_image_fallback_is_forbidden(self) -> None:
        result = evaluate_rights(signals(third_party_fallback_requested=True))
        self.assertEqual(result["IMAGE"]["decision"], "RIGHTS_REVIEW_HOLD")
        self.assertIn("THIRD_PARTY_FALLBACK_FORBIDDEN", result["IMAGE"]["reasons"])

    def test_r06_simulated_revocation_or_reapproval_never_grants_real_use(self) -> None:
        for event in ("SIMULATED_REVOKED", "SIMULATED_REAPPROVED"):
            with self.subTest(event=event):
                result = evaluate_rights(signals(simulated_rights_change=event))
                self.assertEqual(result["IMAGE"]["decision"], "RIGHTS_REVIEW_HOLD")
                self.assertIn(
                    "SIMULATED_RIGHTS_CHANGE_NOT_REAL_EVIDENCE",
                    result["IMAGE"]["reasons"],
                )

    def test_r07_authored_description_needs_independent_approval(self) -> None:
        result = evaluate_rights(signals(authored_text_approved=False))
        self.assertEqual(result["AUTHORED_TEXT"]["decision"], "RIGHTS_REVIEW_HOLD")
        self.assertEqual(result["IMAGE"]["decision"], "IMAGE_REUSE_APPROVED")

    def test_r08_reviewed_metadata_only_fallback_is_allowed(self) -> None:
        result = evaluate_rights(
            signals(
                api_public_domain=False,
                page_public_domain=None,
                primary_image_present=False,
                image_download_available=False,
                authored_text_approved=False,
                image_display_approved=False,
            )
        )
        self.assertEqual(result["METADATA"]["decision"], "METADATA_ONLY_ALLOWED")
        self.assertEqual(result["AUTHORED_TEXT"]["decision"], "RIGHTS_REVIEW_HOLD")
        self.assertEqual(result["IMAGE"]["decision"], "RIGHTS_REVIEW_HOLD")


if __name__ == "__main__":
    unittest.main(verbosity=2)

"""
Automated tests for the proposed ID card replacement workflow.
Tests 1-5 are the five synthetic cases required by the assignment.
All student references (STU-A, STU-B, ...) are made up.

Run:  py -m unittest test_idcard_workflow -v
"""
import unittest

from idcard_workflow import (
    IdCardDesk, WorkflowError,
    STUDENT, ID_DESK, ADMIN_OFFICER, ADMIN_HEAD,
    NEEDS_INFO, SUBMITTED, ESCALATED, APPROVED, PRINT_FAILED, READY, COLLECTED, REJECTED,
)


def full_form(ref, reason="lost"):
    form = {"student_ref": ref, "reason": reason, "photo_attached": True,
            "declaration_signed": True, "charge_cleared": True}
    if reason in ("damaged", "details_change"):
        form["old_card_returned"] = True
    return form


class FiveRequiredCases(unittest.TestCase):

    def test_1_normal(self):
        """Complete request goes all the way to COLLECTED."""
        desk = IdCardDesk()
        r = desk.submit("STU-A", full_form("STU-A"))
        self.assertEqual(r.status, SUBMITTED)
        desk.verify(ID_DESK, r.request_id)
        desk.approve(ADMIN_OFFICER, r.request_id)
        desk.print_card(ID_DESK, r.request_id)
        self.assertEqual(r.status, READY)
        desk.hand_over(ID_DESK, r.request_id, "STU-A")
        self.assertEqual(r.status, COLLECTED)

    def test_2_missing_information(self):
        """No photo and no declaration -> NEEDS_INFO; recovers after the student adds them."""
        desk = IdCardDesk()
        form = full_form("STU-B")
        form["photo_attached"] = False
        form["declaration_signed"] = False
        r = desk.submit("STU-B", form)
        self.assertEqual(r.status, NEEDS_INFO)
        self.assertEqual(sorted(r.missing), ["declaration_signed", "photo_attached"])
        with self.assertRaises(WorkflowError):          # staff cannot verify an incomplete request
            desk.verify(ID_DESK, r.request_id)
        desk.provide_info("STU-B", r.request_id, photo_attached=True, declaration_signed=True)
        self.assertEqual(r.status, SUBMITTED)            # recovery: back in the normal flow

    def test_3_duplicate(self):
        """A second request while one is still open is rejected and linked to the first."""
        desk = IdCardDesk()
        first = desk.submit("STU-C", full_form("STU-C"))
        second = desk.submit("STU-C", full_form("STU-C"))
        self.assertEqual(second.status, REJECTED)
        self.assertIn(first.request_id, second.history[-1][1])
        self.assertEqual(first.status, SUBMITTED)        # the original request is untouched

    def test_4_unauthorized_request(self):
        """Someone else cannot request or collect another student's card; all three attempts are logged."""
        desk = IdCardDesk()
        with self.assertRaises(WorkflowError):
            desk.submit("STU-X", full_form("STU-D"))
        r = desk.submit("STU-D", full_form("STU-D"))
        with self.assertRaises(WorkflowError):          # a student cannot approve
            desk.approve(STUDENT, r.request_id)
        desk.verify(ID_DESK, r.request_id)
        desk.approve(ADMIN_OFFICER, r.request_id)
        desk.print_card(ID_DESK, r.request_id)
        with self.assertRaises(WorkflowError):
            desk.hand_over(ID_DESK, r.request_id, "STU-X")
        self.assertEqual(r.status, READY)                # card stays safely at the desk
        kinds = [entry[0] for entry in desk.security_log]
        self.assertEqual(kinds, ["UNAUTHORIZED_SUBMIT", "UNAUTHORIZED_ACTION", "UNAUTHORIZED_COLLECT"])

    def test_5_failed_step(self):
        """Printer fails -> temporary pass + retry; fails again -> manual card fallback."""
        desk = IdCardDesk()
        r = desk.submit("STU-E", full_form("STU-E"))
        desk.verify(ID_DESK, r.request_id)
        desk.approve(ADMIN_OFFICER, r.request_id)
        desk.print_card(ID_DESK, r.request_id, printer_ok=False)
        self.assertEqual(r.status, PRINT_FAILED)
        self.assertTrue(r.temporary_pass)
        desk.print_card(ID_DESK, r.request_id, printer_ok=False)
        self.assertEqual(r.status, READY)
        self.assertTrue(r.manual_card)
        desk.hand_over(ID_DESK, r.request_id, "STU-E")
        self.assertEqual(r.status, COLLECTED)


class ApprovalBoundary(unittest.TestCase):

    def test_officer_can_approve_within_limit(self):
        desk = IdCardDesk(replacements_last_12_months={"STU-F": 1})
        r = desk.submit("STU-F", full_form("STU-F", "damaged"))
        desk.verify(ID_DESK, r.request_id)
        desk.approve(ADMIN_OFFICER, r.request_id)
        self.assertEqual(r.status, APPROVED)

    def test_third_replacement_needs_admin_head(self):
        desk = IdCardDesk(replacements_last_12_months={"STU-G": 2})
        r = desk.submit("STU-G", full_form("STU-G"))
        desk.verify(ID_DESK, r.request_id)
        desk.approve(ADMIN_OFFICER, r.request_id)
        self.assertEqual(r.status, ESCALATED)
        desk.approve(ADMIN_HEAD, r.request_id)
        self.assertEqual(r.status, APPROVED)

    def test_invalid_reason_is_missing_information(self):
        desk = IdCardDesk()
        r = desk.submit("STU-H", full_form("STU-H", "want_new_photo"))
        self.assertEqual(r.status, NEEDS_INFO)
        desk.provide_info("STU-H", r.request_id, reason="also_wrong")
        self.assertEqual(r.status, NEEDS_INFO)
        desk.provide_info("STU-H", r.request_id, reason="details_change")
        self.assertEqual(r.missing, ["old_card_returned"])   # new reason -> new proof needed
        desk.provide_info("STU-H", r.request_id, old_card_returned=True)
        self.assertEqual(r.status, SUBMITTED)


class ProofRules(unittest.TestCase):
    """Proof depends on the reason (benchmarks: Thapar, NIT Calicut; see evidence/benchmarks.md)."""

    def test_damaged_card_must_be_handed_in(self):
        desk = IdCardDesk()
        form = full_form("STU-J", "damaged")
        del form["old_card_returned"]
        r = desk.submit("STU-J", form)
        self.assertEqual((r.status, r.missing), (NEEDS_INFO, ["old_card_returned"]))

    def test_fir_only_required_when_setting_is_on(self):
        self.assertEqual(IdCardDesk().submit("STU-K", full_form("STU-K")).status, SUBMITTED)
        strict = IdCardDesk(require_fir_for_lost=True)
        r = strict.submit("STU-K", full_form("STU-K"))
        self.assertEqual((r.status, r.missing), (NEEDS_INFO, ["fir_copy_attached"]))

    def test_student_cannot_change_whose_card_it_is(self):
        desk = IdCardDesk()
        form = full_form("STU-L")
        form["photo_attached"] = False
        r = desk.submit("STU-L", form)
        desk.provide_info("STU-L", r.request_id, photo_attached=True, student_ref="STU-Z")
        self.assertEqual(r.form["student_ref"], "STU-L")

    def test_cannot_skip_steps(self):
        desk = IdCardDesk()
        r = desk.submit("STU-I", full_form("STU-I"))
        with self.assertRaises(WorkflowError):
            desk.print_card(ID_DESK, r.request_id)       # not approved yet


if __name__ == "__main__":
    unittest.main(verbosity=2)

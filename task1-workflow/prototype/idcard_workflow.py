"""
Prototype of the PROPOSED student ID card replacement workflow (Task 1).

This is a design prototype with synthetic data only. It is not connected to any
college system, and the rules marked ILLUSTRATIVE are design choices that must be
checked against the real process (see ../evidence/what-to-verify.md).

Run the demo:   py idcard_workflow.py
Run the tests:  py -m unittest test_idcard_workflow -v
"""
from dataclasses import dataclass, field

# ---- Statuses -------------------------------------------------------------
SUBMITTED = "SUBMITTED"          # request received, not yet checked
NEEDS_INFO = "NEEDS_INFO"        # something required is missing
VERIFIED = "VERIFIED"            # details checked against the student record
ESCALATED = "ESCALATED"          # outside the officer's approval boundary
APPROVED = "APPROVED"            # ready to print
PRINT_FAILED = "PRINT_FAILED"    # printer/system failure; temporary pass issued
READY = "READY"                  # card printed, waiting for collection
COLLECTED = "COLLECTED"          # handed to the student; old card deactivated
REJECTED = "REJECTED"            # closed without a card (duplicate, unauthorized, ...)

OPEN_STATUSES = {SUBMITTED, NEEDS_INFO, VERIFIED, ESCALATED, APPROVED, PRINT_FAILED, READY}

# ---- Roles ----------------------------------------------------------------
STUDENT = "student"
ID_DESK = "id_desk"              # front desk: checks details, prints, hands over
ADMIN_OFFICER = "admin_officer"  # accountable owner: approves standard cases
ADMIN_HEAD = "admin_head"        # approves cases outside the officer's boundary

REASONS = {"lost", "damaged", "details_change"}
REQUIRED_FIELDS = ("student_ref", "reason", "photo_attached", "declaration_signed", "charge_cleared")

# ILLUSTRATIVE approval boundary: an officer may approve a student's 1st or 2nd
# replacement in 12 months; a 3rd or later goes to the admin head.
OFFICER_LIMIT_PER_YEAR = 2
# ILLUSTRATIVE fallback: after this many print failures, issue a manual card.
MAX_PRINT_ATTEMPTS = 2
# Proof depends on the reason. Benchmarks (evidence/benchmarks.md): Thapar asks for an
# FIR copy for a lost card and the old card for a damaged one. Whether IFHE needs an
# FIR is unknown (check V9), so it is a setting, off by default.
REQUIRE_FIR_FOR_LOST = False


class WorkflowError(Exception):
    """Raised when an action is not allowed in the current state or for this role."""


@dataclass
class Request:
    request_id: str
    student_ref: str
    reason: str
    status: str = SUBMITTED
    missing: list = field(default_factory=list)
    print_attempts: int = 0
    temporary_pass: bool = False
    manual_card: bool = False
    form: dict = field(default_factory=dict)
    history: list = field(default_factory=list)

    def log(self, actor, event):
        self.history.append((actor, event, self.status))


class IdCardDesk:
    """Holds all requests and enforces the rules of the proposed process."""

    def __init__(self, replacements_last_12_months=None, require_fir_for_lost=REQUIRE_FIR_FOR_LOST):
        self.require_fir_for_lost = require_fir_for_lost
        self.requests = {}
        self.security_log = []
        # synthetic history: student_ref -> number of replacements already issued this year
        self.past = dict(replacements_last_12_months or {})
        self._next = 1

    # -- Student actions -----------------------------------------------------
    def submit(self, requester_ref, form):
        """A student submits a replacement request for their own card."""
        student_ref = form.get("student_ref")
        if requester_ref != student_ref:
            self.security_log.append(("UNAUTHORIZED_SUBMIT", requester_ref, student_ref))
            raise WorkflowError(f"{requester_ref} cannot request a card for {student_ref}")

        open_req = self.open_request_for(student_ref)
        if open_req:
            dup = self._new(student_ref, form.get("reason", ""))
            dup.status = REJECTED
            dup.log(requester_ref, f"duplicate of {open_req.request_id}")
            return dup

        req = self._new(student_ref, form.get("reason", ""))
        req.form = dict(form)
        self._check_complete(req)
        req.log(requester_ref, "submitted" + (f", missing: {req.missing}" if req.missing else ""))
        return req

    def provide_info(self, requester_ref, request_id, **fields):
        """The student adds or corrects fields; the whole form is re-checked."""
        req = self._get(request_id)
        self._require(req.student_ref == requester_ref, "only the requesting student can add information")
        self._require(req.status == NEEDS_INFO, f"request is {req.status}, not NEEDS_INFO")
        fields.pop("student_ref", None)  # the student reference cannot be changed
        req.form.update(fields)
        req.reason = req.form.get("reason", "")
        self._check_complete(req)
        req.log(requester_ref, f"provided {sorted(fields)}")
        return req

    # -- Staff actions -------------------------------------------------------
    def verify(self, actor_role, request_id):
        req = self._get(request_id)
        self._role(actor_role, {ID_DESK}, req, "verify")
        self._require(req.status == SUBMITTED, f"request is {req.status}, not SUBMITTED")
        req.status = VERIFIED
        req.log(actor_role, "details checked")
        return req

    def approve(self, actor_role, request_id):
        req = self._get(request_id)
        self._role(actor_role, {ADMIN_OFFICER, ADMIN_HEAD}, req, "approve")
        self._require(req.status in (VERIFIED, ESCALATED), f"request is {req.status}, cannot approve")
        within_officer_limit = self.past.get(req.student_ref, 0) < OFFICER_LIMIT_PER_YEAR
        if actor_role == ADMIN_OFFICER and not within_officer_limit:
            req.status = ESCALATED
            req.log(actor_role, "outside officer boundary -> escalated to admin head")
            return req
        if req.status == ESCALATED and actor_role != ADMIN_HEAD:
            raise WorkflowError("escalated requests need the admin head")
        req.status = APPROVED
        req.log(actor_role, "approved")
        return req

    def print_card(self, actor_role, request_id, printer_ok=True):
        req = self._get(request_id)
        self._role(actor_role, {ID_DESK}, req, "print")
        self._require(req.status in (APPROVED, PRINT_FAILED), f"request is {req.status}, cannot print")
        req.print_attempts += 1
        if printer_ok:
            req.status = READY
            req.log(actor_role, f"printed (attempt {req.print_attempts})")
        elif req.print_attempts >= MAX_PRINT_ATTEMPTS:
            req.manual_card = True
            req.status = READY
            req.log(actor_role, "printer failed again -> manual card issued (fallback)")
        else:
            req.status = PRINT_FAILED
            req.temporary_pass = True
            req.log(actor_role, "printer failed -> temporary pass issued, retry later")
        return req

    def hand_over(self, actor_role, request_id, collector_ref):
        req = self._get(request_id)
        self._role(actor_role, {ID_DESK}, req, "hand over")
        self._require(req.status == READY, f"request is {req.status}, not READY")
        if collector_ref != req.student_ref:
            self.security_log.append(("UNAUTHORIZED_COLLECT", collector_ref, req.student_ref))
            raise WorkflowError(f"{collector_ref} cannot collect the card of {req.student_ref}")
        req.status = COLLECTED
        self.past[req.student_ref] = self.past.get(req.student_ref, 0) + 1
        req.log(actor_role, "collected; old card deactivated")
        return req

    # -- Helpers -------------------------------------------------------------
    def _check_complete(self, req):
        form = req.form
        req.missing = [f for f in REQUIRED_FIELDS if not form.get(f)]
        if form.get("reason") and form.get("reason") not in REASONS:
            req.missing.append("reason (must be lost, damaged or details_change)")
        req.missing += self._proof_missing(form)
        req.status = NEEDS_INFO if req.missing else SUBMITTED

    def _proof_missing(self, form):
        """Damaged/details change: old card must be handed in. Lost: FIR copy if required."""
        reason = form.get("reason")
        if reason in ("damaged", "details_change") and not form.get("old_card_returned"):
            return ["old_card_returned"]
        if reason == "lost" and self.require_fir_for_lost and not form.get("fir_copy_attached"):
            return ["fir_copy_attached"]
        return []

    def open_request_for(self, student_ref):
        return next((r for r in self.requests.values()
                     if r.student_ref == student_ref and r.status in OPEN_STATUSES), None)

    def _new(self, student_ref, reason):
        req = Request(f"REQ-{self._next:03d}", student_ref, reason)
        self._next += 1
        self.requests[req.request_id] = req
        return req

    def _get(self, request_id):
        if request_id not in self.requests:
            raise WorkflowError(f"unknown request {request_id}")
        return self.requests[request_id]

    def _role(self, actor_role, allowed, req, action):
        if actor_role not in allowed:
            self.security_log.append(("UNAUTHORIZED_ACTION", actor_role, action, req.request_id))
            raise WorkflowError(f"role {actor_role} cannot {action}")

    @staticmethod
    def _require(condition, message):
        if not condition:
            raise WorkflowError(message)


def demo():
    """Walk one synthetic request through the whole process and print each step."""
    desk = IdCardDesk()
    form = {"student_ref": "STU-A", "reason": "lost", "photo_attached": True,
            "declaration_signed": True, "charge_cleared": True}
    r = desk.submit("STU-A", form)
    desk.verify(ID_DESK, r.request_id)
    desk.approve(ADMIN_OFFICER, r.request_id)
    desk.print_card(ID_DESK, r.request_id, printer_ok=False)
    desk.print_card(ID_DESK, r.request_id)
    desk.hand_over(ID_DESK, r.request_id, "STU-A")
    for actor, event, status in r.history:
        print(f"{status:<13} {actor:<14} {event}")


if __name__ == "__main__":
    demo()

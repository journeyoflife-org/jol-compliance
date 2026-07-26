#!/usr/bin/env python3
"""
JOL GDPR Data Subject Rights (DSR) Tracker
=============================================
Tracks and manages GDPR data subject rights requests (Art. 15–22),
ensuring compliance with response timelines and escalation procedures.

Document ID: JOL-SCRIPT-DSR-001
Owner: DPO
Version: 1.0
Classification: RESTRICTED

Usage:
    python scripts/gdpr_dsr_tracker.py --add --type access --requester "john@example.com"
    python scripts/gdpr_dsr_tracker.py --list
    python scripts/gdpr_dsr_tracker.py --overdue
    python scripts/gdpr_dsr_tracker.py --metrics
    python scripts/gdpr_dsr_tracker.py --status 1 --update in-progress
"""

import argparse
import json
import sys
from datetime import UTC, datetime, timedelta
from pathlib import Path

# ── Configuration ──────────────────────────────────────────────────────────

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "dsr_requests.json"

# GDPR Art. 12(3): Response within 1 month (extendable by 2 months for complex requests)
STANDARD_RESPONSE_DAYS = 30
EXTENSION_DAYS = 60
ESCALATION_THRESHOLD_DAYS = 20  # Internal early warning

DSR_TYPES: dict[str, dict] = {
    "access": {
        "article": "Art. 15",
        "name": "Right of Access",
        "description": "Data subject requests copy of personal data",
    },
    "rectification": {
        "article": "Art. 16",
        "name": "Right to Rectification",
        "description": "Correction of inaccurate personal data",
    },
    "erasure": {
        "article": "Art. 17",
        "name": "Right to Erasure (Right to be Forgotten)",
        "description": "Deletion of personal data",
    },
    "restriction": {
        "article": "Art. 18",
        "name": "Right to Restriction of Processing",
        "description": "Limit processing of personal data",
    },
    "portability": {
        "article": "Art. 20",
        "name": "Right to Data Portability",
        "description": "Receive personal data in structured, machine-readable format",
    },
    "objection": {
        "article": "Art. 21",
        "name": "Right to Object",
        "description": "Object to processing based on legitimate interest or direct marketing",
    },
    "automated-decision": {
        "article": "Art. 22",
        "name": "Automated Decision-Making",
        "description": "Right not to be subject to solely automated decisions with legal effect",
    },
}

STATUSES = ["new", "identity-verified", "in-progress", "awaiting-info", "completed", "rejected", "withdrawn"]


# ── Data Management ────────────────────────────────────────────────────────


def load_requests() -> list[dict]:
    """Load DSR requests from data file."""
    if DATA_FILE.exists():
        with open(DATA_FILE, encoding="utf-8") as f:
            return json.load(f)
    return []


def save_requests(requests: list[dict]) -> None:
    """Save DSR requests to data file."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(requests, f, indent=2, ensure_ascii=False)


def generate_id(requests: list[dict]) -> str:
    """Generate a unique DSR request ID."""
    now = datetime.now(tz=UTC)
    year = now.strftime("%Y")
    seq = len([r for r in requests if r["id"].startswith(f"DSR-{year}")]) + 1
    return f"DSR-{year}-{seq:04d}"


# ── Core Functions ─────────────────────────────────────────────────────────


def add_request(
    dsr_type: str,
    requester: str,
    country: str = "LT",
    notes: str = "",
    complex_request: bool = False,
) -> dict:
    """Add a new DSR request."""
    if dsr_type not in DSR_TYPES:
        print(f"Error: Unknown DSR type '{dsr_type}'. Valid types: {', '.join(DSR_TYPES.keys())}")
        sys.exit(1)

    requests = load_requests()
    now = datetime.now(tz=UTC)
    response_deadline = now + timedelta(days=STANDARD_RESPONSE_DAYS)

    if complex_request:
        response_deadline = now + timedelta(days=STANDARD_RESPONSE_DAYS + EXTENSION_DAYS)

    new_request = {
        "id": generate_id(requests),
        "type": dsr_type,
        "article": DSR_TYPES[dsr_type]["article"],
        "type_name": DSR_TYPES[dsr_type]["name"],
        "requester_email": requester,
        "country": country,
        "received_date": now.isoformat(),
        "response_deadline": response_deadline.isoformat(),
        "extended": complex_request,
        "status": "new",
        "assigned_to": "",
        "notes": notes,
        "history": [
            {
                "timestamp": now.isoformat(),
                "action": "created",
                "by": "system",
                "note": "DSR request registered",
            }
        ],
    }

    requests.append(new_request)
    save_requests(requests)
    return new_request


def update_status(request_id: str, new_status: str, note: str = "") -> dict | None:
    """Update the status of a DSR request."""
    if new_status not in STATUSES:
        print(f"Error: Invalid status '{new_status}'. Valid: {', '.join(STATUSES)}")
        return None

    requests = load_requests()
    now = datetime.now(tz=UTC)

    for req in requests:
        if req["id"] == request_id:
            old_status = req["status"]
            req["status"] = new_status
            req["history"].append({
                "timestamp": now.isoformat(),
                "action": f"status: {old_status} → {new_status}",
                "by": "user",
                "note": note,
            })
            save_requests(requests)
            return req

    print(f"Error: Request '{request_id}' not found")
    return None


def list_requests(status_filter: str | None = None) -> list[dict]:
    """List all DSR requests, optionally filtered by status."""
    requests = load_requests()
    if status_filter:
        requests = [r for r in requests if r["status"] == status_filter]
    return requests


def get_overdue_requests() -> list[dict]:
    """Get requests that are overdue or approaching deadline."""
    requests = load_requests()
    now = datetime.now(tz=UTC)
    overdue = []

    for req in requests:
        if req["status"] in ("completed", "rejected", "withdrawn"):
            continue

        deadline = datetime.fromisoformat(req["response_deadline"])
        days_remaining = (deadline - now).days

        if days_remaining < 0:
            req["urgency"] = "OVERDUE"
            req["days_remaining"] = days_remaining
            overdue.append(req)
        elif days_remaining <= ESCALATION_THRESHOLD_DAYS:
            req["urgency"] = "AT RISK"
            req["days_remaining"] = days_remaining
            overdue.append(req)

    overdue.sort(key=lambda r: r["days_remaining"])
    return overdue


def calculate_metrics() -> dict:
    """Calculate DSR processing metrics."""
    requests = load_requests()
    now = datetime.now(tz=UTC)

    total = len(requests)
    by_type: dict[str, int] = {}
    by_status: dict[str, int] = {}
    completed_on_time = 0
    completed_late = 0
    avg_resolution_days = 0.0
    resolution_times = []

    for req in requests:
        # Count by type
        dsr_type = req.get("type_name", "Unknown")
        by_type[dsr_type] = by_type.get(dsr_type, 0) + 1

        # Count by status
        status = req["status"]
        by_status[status] = by_status.get(status, 0) + 1

        # Resolution metrics
        if status == "completed":
            received = datetime.fromisoformat(req["received_date"])
            deadline = datetime.fromisoformat(req["response_deadline"])
            # Estimate completion as now if no completion timestamp
            completed_time = received + timedelta(days=15)  # Placeholder

            for event in reversed(req.get("history", [])):
                if "completed" in event.get("action", ""):
                    completed_time = datetime.fromisoformat(event["timestamp"])
                    break

            days_to_complete = (completed_time - received).days
            resolution_times.append(days_to_complete)

            if completed_time <= deadline:
                completed_on_time += 1
            else:
                completed_late += 1

    if resolution_times:
        avg_resolution_days = sum(resolution_times) / len(resolution_times)

    total_completed = completed_on_time + completed_late
    on_time_pct = round(completed_on_time / max(total_completed, 1) * 100, 1)

    # Active requests
    active = [r for r in requests if r["status"] not in ("completed", "rejected", "withdrawn")]

    return {
        "total_requests": total,
        "active_requests": len(active),
        "completed_on_time": completed_on_time,
        "completed_late": completed_late,
        "on_time_percentage": on_time_pct,
        "avg_resolution_days": round(avg_resolution_days, 1),
        "by_type": by_type,
        "by_status": by_status,
        "generated_at": now.isoformat(),
    }


# ── Display Functions ──────────────────────────────────────────────────────


def print_request(req: dict, show_history: bool = False) -> None:
    """Print a formatted DSR request."""
    now = datetime.now(tz=UTC)
    deadline = datetime.fromisoformat(req["response_deadline"])
    days_remaining = (deadline - now).days

    urgency = ""
    if req["status"] not in ("completed", "rejected", "withdrawn"):
        if days_remaining < 0:
            urgency = " [OVERDUE]"
        elif days_remaining <= ESCALATION_THRESHOLD_DAYS:
            urgency = " [AT RISK]"

    print(f"\n  {'─' * 56}")
    print(f"  ID:             {req['id']}")
    print(f"  Type:           {req['type_name']} ({req['article']})")
    print(f"  Requester:      {req['requester_email']}")
    print(f"  Country:        {req.get('country', 'N/A')}")
    print(f"  Received:       {req['received_date'][:10]}")
    print(f"  Deadline:       {req['response_deadline'][:10]} ({days_remaining} days{urgency})")
    print(f"  Status:         {req['status'].upper()}")
    print(f"  Extended:       {'Yes (+60 days)' if req.get('extended') else 'No'}")
    print(f"  Assigned To:    {req.get('assigned_to', 'Unassigned')}")
    if req.get("notes"):
        print(f"  Notes:          {req['notes']}")

    if show_history and req.get("history"):
        print("\n  HISTORY:")
        for event in req["history"]:
            ts = event["timestamp"][:16].replace("T", " ")
            print(f"    [{ts}] {event['action']}")
            if event.get("note"):
                print(f"             {event['note']}")


def print_list(requests: list[dict]) -> None:
    """Print a table of DSR requests."""
    if not requests:
        print("\n  No DSR requests found.\n")
        return

    print(f"\n{'=' * 90}")
    print("  JOL GDPR DATA SUBJECT RIGHTS REQUESTS")
    print(f"{'=' * 90}")
    print(f"  {'ID':<18s} {'Type':<20s} {'Requester':<25s} {'Status':<12s} {'Days Left':>9s}")
    print(f"  {'-' * 86}")

    now = datetime.now(tz=UTC)
    for req in sorted(requests, key=lambda r: r["received_date"]):
        deadline = datetime.fromisoformat(req["response_deadline"])
        days_left = (deadline - now).days
        status = req["status"].upper()

        if req["status"] not in ("completed", "rejected", "withdrawn"):
            if days_left < 0:
                days_str = f"{days_left:+d} OVERDUE"
            elif days_left <= ESCALATION_THRESHOLD_DAYS:
                days_str = f"{days_left}d AT RISK"
            else:
                days_str = f"{days_left}d"
        else:
            days_str = "—"

        print(f"  {req['id']:<18s} {req['type_name']:<20s} {req['requester_email']:<25s} {status:<12s} {days_str:>9s}")

    print(f"\n  Total: {len(requests)} request(s)")
    print(f"{'=' * 90}\n")


def print_metrics(metrics: dict) -> None:
    """Print DSR processing metrics."""
    print(f"\n{'=' * 60}")
    print("  JOL DSR PROCESSING METRICS")
    print(f"  Generated: {metrics['generated_at'][:19]}")
    print(f"{'=' * 60}")

    print("\n  OVERVIEW:")
    print(f"    Total Requests:     {metrics['total_requests']}")
    print(f"    Active:             {metrics['active_requests']}")
    print(f"    On-Time Completion: {metrics['completed_on_time']} ({metrics['on_time_percentage']}%)")
    print(f"    Late Completion:    {metrics['completed_late']}")
    print(f"    Avg Resolution:     {metrics['avg_resolution_days']} days")

    if metrics["by_type"]:
        print("\n  BY TYPE:")
        for dsr_type, count in sorted(metrics["by_type"].items()):
            print(f"    {dsr_type:<35s} {count:>4d}")

    if metrics["by_status"]:
        print("\n  BY STATUS:")
        for status, count in sorted(metrics["by_status"].items()):
            print(f"    {status:<35s} {count:>4d}")

    # SLA compliance
    sla_target = 95.0
    compliance = "PASS" if metrics["on_time_percentage"] >= sla_target else "BELOW TARGET"
    print("\n  SLA COMPLIANCE:")
    print(f"    Target:             {sla_target}% on-time")
    print(f"    Actual:             {metrics['on_time_percentage']}%")
    print(f"    Status:             {compliance}")

    print(f"\n{'=' * 60}\n")


# ── Main ───────────────────────────────────────────────────────────────────


def main() -> int:
    parser = argparse.ArgumentParser(
        description="JOL GDPR Data Subject Rights Tracker",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument("--add", action="store_true", help="Add a new DSR request")
    parser.add_argument("--type", choices=list(DSR_TYPES.keys()), help="DSR type (for --add)")
    parser.add_argument("--requester", help="Requester email (for --add)")
    parser.add_argument("--country", choices=["LT", "LV", "EE"], default="LT", help="Requester country")
    parser.add_argument("--complex", action="store_true", help="Mark as complex request (+60 day extension)")
    parser.add_argument("--notes", default="", help="Additional notes")

    parser.add_argument("--list", action="store_true", help="List all requests")
    parser.add_argument("--status-filter", choices=STATUSES, help="Filter by status")

    parser.add_argument("--status", help="Update status of request ID")
    parser.add_argument("--update", choices=STATUSES, help="New status (for --status)")
    parser.add_argument("--update-note", default="", help="Note for status update")

    parser.add_argument("--overdue", action="store_true", help="Show overdue and at-risk requests")
    parser.add_argument("--metrics", action="store_true", help="Show DSR processing metrics")
    parser.add_argument("--detail", help="Show detailed view of request ID")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.add:
        if not args.type or not args.requester:
            parser.error("--type and --requester are required for --add")
        req = add_request(args.type, args.requester, args.country, args.notes, args.complex)
        print(f"\n  DSR request created: {req['id']}")
        print(f"  Deadline: {req['response_deadline'][:10]}")
        print_request(req)
        return 0

    if args.status:
        if not args.update:
            parser.error("--update is required with --status")
        req = update_status(args.status, args.update, args.update_note)
        if req:
            print(f"\n  Status updated: {req['id']} → {req['status'].upper()}")
        return 0 if req else 1

    if args.overdue:
        overdue = get_overdue_requests()
        if args.json:
            print(json.dumps(overdue, indent=2, ensure_ascii=False))
        else:
            if not overdue:
                print("\n  No overdue or at-risk requests.\n")
            else:
                print(f"\n  OVERDUE / AT-RISK REQUESTS ({len(overdue)} found):")
                for req in overdue:
                    print_request(req)
        return 0

    if args.metrics:
        metrics = calculate_metrics()
        if args.json:
            print(json.dumps(metrics, indent=2, ensure_ascii=False))
        else:
            print_metrics(metrics)
        return 0

    if args.detail:
        requests = load_requests()
        for req in requests:
            if req["id"] == args.detail:
                print_request(req, show_history=True)
                return 0
        print(f"Error: Request '{args.detail}' not found")
        return 1

    if args.list:
        requests = list_requests(args.status_filter)
        if args.json:
            print(json.dumps(requests, indent=2, ensure_ascii=False))
        else:
            print_list(requests)
        return 0

    # Default: show list
    requests = list_requests()
    print_list(requests)
    return 0


if __name__ == "__main__":
    sys.exit(main())

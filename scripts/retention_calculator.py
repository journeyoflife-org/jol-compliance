#!/usr/bin/env python3
"""
JOL Data Retention Calculator
===============================
Calculates retention periods and disposal dates for personal data
based on JOL's data retention policy and applicable legal requirements.

Document ID: JOL-SCRIPT-RC-001
Owner: DPO
Version: 1.0
Classification: RESTRICTED

Usage:
    python scripts/retention_calculator.py --category employee --collected 2024-01-15
    python scripts/retention_calculator.py --category financial --collected 2023-06-01 --country LT
    python scripts/retention_calculator.py --list-categories
    python scripts/retention_calculator.py --audit
"""

import argparse
import json
import sys
from datetime import datetime, timedelta, timezone
from typing import Optional


# ── Retention Schedule ─────────────────────────────────────────────────────
# Based on gdpr/retention-policies/data-retention-policy.md
# and country-specific legal requirements

RETENTION_SCHEDULES: dict[str, dict] = {
    # ── HR / Employee Data ──
    "employee-active": {
        "description": "Active employee personnel records",
        "legal_basis": "GDPR Art. 6(1)(b) — Contract performance",
        "retention_years": 0,
        "retention_note": "Duration of employment + review period",
        "disposal_action": "Review at employment end",
    },
    "employee-former": {
        "description": "Former employee personnel records",
        "legal_basis": "GDPR Art. 6(1)(c) — Legal obligation (LT Darbo kodeksas Art. 264)",
        "retention_years": 3,
        "retention_note": "3 years after termination (LT); check country-specific",
        "disposal_action": "Secure deletion (NIST 800-88 Clear)",
        "country_overrides": {
            "LT": {"years": 3, "law": "Darbo kodeksas Art. 264"},
            "LV": {"years": 3, "law": "Darba likums 44. pants"},
            "EE": {"years": 3, "law": "Töölepingu seadus § 28"},
        },
    },
    "employee-health": {
        "description": "Employee health and safety records",
        "legal_basis": "GDPR Art. 9(2)(h) — Occupational health",
        "retention_years": 10,
        "retention_note": "10 years after last medical examination",
        "disposal_action": "Secure deletion + destruction of physical copies (DIN 66399 P4)",
    },
    # ── Financial Data ──
    "financial-accounting": {
        "description": "Accounting records, invoices, receipts",
        "legal_basis": "GDPR Art. 6(1)(c) — Legal obligation",
        "retention_years": 10,
        "retention_note": "Varies by country — use --country flag",
        "disposal_action": "Secure deletion after retention period",
        "country_overrides": {
            "LT": {"years": 10, "law": "Mokesčių administravimo įstatymas Art. 40"},
            "LV": {"years": 5, "law": "Grāmatvedības likums 10. pants"},
            "EE": {"years": 7, "law": "Raamatupidamise seadus § 12"},
        },
    },
    "financial-payroll": {
        "description": "Payroll processing records",
        "legal_basis": "GDPR Art. 6(1)(c) — Legal obligation (tax/social security)",
        "retention_years": 10,
        "retention_note": "Varies by country — use --country flag",
        "disposal_action": "Secure deletion",
        "country_overrides": {
            "LT": {"years": 10, "law": "Mokesčių administravimo įstatymas Art. 40"},
            "LV": {"years": 5, "law": "Par valsts sociālo apdrošināšanu 27. pants"},
            "EE": {"years": 7, "law": "Maksukorralduse seadus § 94"},
        },
    },
    "financial-tax": {
        "description": "Tax declarations and supporting documents",
        "legal_basis": "GDPR Art. 6(1)(c) — Legal obligation",
        "retention_years": 5,
        "retention_note": "Minimum 5 years from filing date",
        "disposal_action": "Secure deletion",
        "country_overrides": {
            "LT": {"years": 5, "law": "Mokesčių administravimo įstatymas Art. 40"},
            "LV": {"years": 5, "law": "Par nodokļiem un nodevām 23. pants"},
            "EE": {"years": 5, "law": "Maksukorralduse seadus § 94"},
        },
    },
    # ── Customer / User Data ──
    "customer-active": {
        "description": "Active customer account data",
        "legal_basis": "GDPR Art. 6(1)(b) — Contract performance",
        "retention_years": 0,
        "retention_note": "Duration of service + 30 days for data export",
        "disposal_action": "Automated deletion after grace period",
    },
    "customer-former": {
        "description": "Former customer account data (post-deletion request)",
        "legal_basis": "GDPR Art. 17 — Right to erasure",
        "retention_years": 0,
        "retention_note": "Deleted within 30 days of request (Art. 17); billing data retained per financial schedule",
        "disposal_action": "Automated secure deletion (NIST 800-88 Clear)",
    },
    "customer-consent": {
        "description": "Consent records (marketing, analytics cookies)",
        "legal_basis": "GDPR Art. 7(1) — Demonstrate consent",
        "retention_years": 5,
        "retention_note": "5 years from consent withdrawal or last interaction",
        "disposal_action": "Automated deletion",
    },
    # ── Security Data ──
    "security-logs": {
        "description": "Security event logs, audit trails",
        "legal_basis": "GDPR Art. 6(1)(f) — Legitimate interest (security)",
        "retention_years": 2,
        "retention_note": "2 years; P1 incidents retained 7 years",
        "disposal_action": "Automated log rotation",
    },
    "security-incident": {
        "description": "Security incident records",
        "legal_basis": "GDPR Art. 33(5) — Breach documentation; ISO 27001 A.5.26",
        "retention_years": 7,
        "retention_note": "7 years for P1/P2; 3 years for P3/P4",
        "disposal_action": "Archive then secure deletion",
    },
    "security-cctv": {
        "description": "CCTV / physical access control recordings",
        "legal_basis": "GDPR Art. 6(1)(f) — Legitimate interest (physical security)",
        "retention_years": 0,
        "retention_note": "90 days maximum; longer if incident-related",
        "disposal_action": "Automated overwrite",
        "retention_days": 90,
    },
    # ── Business / Communication ──
    "email-business": {
        "description": "Business email correspondence",
        "legal_basis": "GDPR Art. 6(1)(f) — Legitimate interest",
        "retention_years": 3,
        "retention_note": "3 years from last communication",
        "disposal_action": "Automated archival then deletion",
    },
    "email-marketing": {
        "description": "Marketing email lists and campaign data",
        "legal_basis": "GDPR Art. 6(1)(a) — Consent; ePrivacy Directive Art. 13",
        "retention_years": 2,
        "retention_note": "2 years from last engagement or consent withdrawal",
        "disposal_action": "Automated deletion",
    },
    "vendor-contracts": {
        "description": "Vendor contracts, DPAs, and compliance records",
        "legal_basis": "GDPR Art. 28; Art. 6(1)(b)",
        "retention_years": 7,
        "retention_note": "7 years after contract termination",
        "disposal_action": "Secure deletion",
    },
    # ── Special Categories ──
    "health-parishioner": {
        "description": "Parishioner pastoral care / sacramental records with health data",
        "legal_basis": "GDPR Art. 9(2)(d) — Religious body processing",
        "retention_years": 75,
        "retention_note": "75 years (sacramental records); canon law requirements",
        "disposal_action": "Archival transfer; physical records preserved per canon law",
    },
    "religious-membership": {
        "description": "Religious membership / baptism / sacramental records",
        "legal_basis": "GDPR Art. 9(2)(d) — Religious body legitimate activities",
        "retention_years": 100,
        "retention_note": "Permanent archival (canon law + cultural heritage)",
        "disposal_action": "Transfer to diocesan archive; no deletion",
    },
}


# ── Helper Functions ───────────────────────────────────────────────────────


def calculate_disposal_date(
    collected_date: datetime,
    category: str,
    country: Optional[str] = None,
) -> dict:
    """Calculate the disposal date for a given data category."""
    schedule = RETENTION_SCHEDULES.get(category)
    if not schedule:
        return {"error": f"Unknown category: {category}"}

    # Check country override
    years = schedule["retention_years"]
    law = schedule.get("legal_basis", "")

    if country and "country_overrides" in schedule:
        override = schedule["country_overrides"].get(country)
        if override:
            years = override["years"]
            law = f"{law}; {override['law']}"

    # Check for day-based retention
    if "retention_days" in schedule and years == 0:
        disposal_date = collected_date + timedelta(days=schedule["retention_days"])
    elif years > 0:
        disposal_date = collected_date.replace(year=collected_date.year + years)
    else:
        disposal_date = None

    now = datetime.now(tz=timezone.utc)
    days_remaining = None
    status = "N/A"

    if disposal_date:
        disposal_aware = disposal_date.replace(
            hour=0, minute=0, second=0, microsecond=0, tzinfo=timezone.utc
        )
        days_remaining = (disposal_aware - now).days
        if days_remaining <= 0:
            status = "OVERDUE — dispose immediately"
        elif days_remaining <= 30:
            status = "DUE SOON — schedule disposal"
        else:
            status = "ACTIVE — within retention period"

    return {
        "category": category,
        "description": schedule["description"],
        "collected_date": collected_date.strftime("%Y-%m-%d"),
        "retention_years": years,
        "retention_note": schedule.get("retention_note", ""),
        "disposal_date": disposal_date.strftime("%Y-%m-%d") if disposal_date else "EVENT-BASED (see note)",
        "days_remaining": days_remaining,
        "status": status,
        "legal_basis": law,
        "disposal_action": schedule.get("disposal_action", "Secure deletion"),
        "country": country or "DEFAULT",
    }


def list_categories() -> None:
    """Print all available retention categories."""
    print("\n" + "=" * 80)
    print("  JOL DATA RETENTION CATEGORIES")
    print("=" * 80)

    current_group = ""
    for key, schedule in RETENTION_SCHEDULES.items():
        group = key.split("-")[0]
        if group != current_group:
            current_group = group
            print(f"\n  ── {group.upper()} ──")

        overrides = ""
        if "country_overrides" in schedule:
            countries = ", ".join(schedule["country_overrides"].keys())
            overrides = f" [varies: {countries}]"

        years = schedule["retention_years"]
        if "retention_days" in schedule and years == 0:
            period = f"{schedule['retention_days']} days"
        elif years > 0:
            period = f"{years} years"
        else:
            period = "Event-based"

        print(f"  {key:35s}  {period:15s}{overrides}")
        print(f"    {schedule['description']}")

    print("\n" + "=" * 80)
    print(f"  Total categories: {len(RETENTION_SCHEDULES)}")
    print("  Use --category <name> --collected <YYYY-MM-DD> to calculate disposal date")
    print("=" * 80 + "\n")


def audit_retention() -> None:
    """Audit all retention schedules for consistency."""
    print("\n" + "=" * 80)
    print("  RETENTION SCHEDULE AUDIT")
    print("=" * 80)

    warnings = []
    info_count = 0

    for key, schedule in RETENTION_SCHEDULES.items():
        info_count += 1

        # Check for missing legal basis
        if not schedule.get("legal_basis"):
            warnings.append(f"[WARN] {key}: No legal basis specified")

        # Check for missing disposal action
        if not schedule.get("disposal_action"):
            warnings.append(f"[WARN] {key}: No disposal action specified")

        # Check for country overrides
        if "country_overrides" in schedule:
            for country, override in schedule["country_overrides"].items():
                if not override.get("law"):
                    warnings.append(f"[WARN] {key} ({country}): Override missing law reference")
                info_count += 1

        # Check for very long retention
        if schedule.get("retention_years", 0) > 50:
            warnings.append(
                f"[INFO] {key}: Retention > 50 years — verify legal necessity"
            )

        # Check for zero retention without event-based note
        if schedule.get("retention_years", 0) == 0 and not schedule.get("retention_days"):
            if "event" not in schedule.get("retention_note", "").lower():
                info_count += 1

    print(f"\n  Categories audited: {len(RETENTION_SCHEDULES)}")
    print(f"  Checks run:         {info_count + len(warnings)}")
    print(f"  Warnings:           {len(warnings)}")

    if warnings:
        print("\n  FINDINGS:")
        for w in warnings:
            print(f"    {w}")
    else:
        print("\n  STATUS: All retention schedules are consistent")

    print("\n" + "=" * 80 + "\n")


# ── Main ───────────────────────────────────────────────────────────────────


def main() -> int:
    parser = argparse.ArgumentParser(
        description="JOL Data Retention Calculator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--category",
        help="Data category (e.g., employee-former, financial-accounting)",
    )
    parser.add_argument(
        "--collected",
        help="Date data was collected (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--country",
        choices=["LT", "LV", "EE"],
        help="Country for country-specific retention overrides",
    )
    parser.add_argument(
        "--list-categories",
        action="store_true",
        help="List all available retention categories",
    )
    parser.add_argument(
        "--audit",
        action="store_true",
        help="Audit all retention schedules for consistency",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output result as JSON",
    )

    args = parser.parse_args()

    if args.list_categories:
        list_categories()
        return 0

    if args.audit:
        audit_retention()
        return 0

    if not args.category or not args.collected:
        parser.error("--category and --collected are required for calculation")

    try:
        collected_date = datetime.strptime(args.collected, "%Y-%m-%d")
    except ValueError:
        print(f"Error: Invalid date format '{args.collected}'. Use YYYY-MM-DD.")
        return 1

    result = calculate_disposal_date(collected_date, args.category, args.country)

    if "error" in result:
        print(f"Error: {result['error']}")
        print(f"Available categories: {', '.join(RETENTION_SCHEDULES.keys())}")
        return 1

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("\n" + "=" * 60)
        print("  JOL DATA RETENTION CALCULATION")
        print("=" * 60)
        print(f"  Category:        {result['category']}")
        print(f"  Description:     {result['description']}")
        print(f"  Collected:       {result['collected_date']}")
        print(f"  Retention:       {result['retention_years']} years")
        print(f"  Country:         {result['country']}")
        print(f"  Disposal Date:   {result['disposal_date']}")
        print(f"  Days Remaining:  {result['days_remaining']}")
        print(f"  Status:          {result['status']}")
        print(f"  Legal Basis:     {result['legal_basis']}")
        print(f"  Disposal Action: {result['disposal_action']}")
        print(f"  Note:            {result['retention_note']}")
        print("=" * 60 + "\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())

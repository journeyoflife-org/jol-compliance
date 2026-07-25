#!/usr/bin/env python3
"""
JOL Vendor Risk Calculator
=============================
Assesses and scores third-party vendor risk based on data access,
service criticality, compliance certifications, and geographic location.

Document ID: JOL-SCRIPT-VR-001
Owner: CISO
Version: 1.0
Classification: RESTRICTED

Usage:
    python scripts/vendor_risk_calculator.py --vendor "AWS" --data-access personal --criticality high
    python scripts/vendor_risk_calculator.py --assess-all
    python scripts/vendor_risk_calculator.py --report
"""

import argparse
import json
import sys
from datetime import UTC, datetime

# ── Risk Scoring Weights ──────────────────────────────────────────────────

DATA_ACCESS_WEIGHTS: dict[str, int] = {
    "none": 0,
    "metadata": 10,
    "pseudonymised": 20,
    "personal": 40,
    "special-category": 60,  # GDPR Art. 9
}

SERVICE_CRITICALITY_WEIGHTS: dict[str, int] = {
    "low": 5,
    "medium": 15,
    "high": 30,
    "critical": 50,
}

COMPLIANCE_CERT_WEIGHTS: dict[str, int] = {
    "iso27001": -10,
    "soc2-type2": -15,
    "iso27701": -10,
    "gdpr-dpa": -5,
    "none": 15,
}

GEO_RISK_WEIGHTS: dict[str, int] = {
    "eu-eea": 0,
    "adequacy-decision": 5,
    "sccs-required": 15,
    "high-risk-third-country": 30,
}

SUBPROCESSOR_WEIGHTS: dict[str, int] = {
    "none": 0,
    "documented": 5,
    "undocumented": 25,
}

# Risk level thresholds
RISK_THRESHOLDS = {
    "LOW": (0, 25),
    "MEDIUM": (26, 50),
    "HIGH": (51, 75),
    "CRITICAL": (76, 100),
}

# ── Sample Vendor Registry ─────────────────────────────────────────────────
# In production, this would read from vendor-register/vendor-register-master.md

SAMPLE_VENDORS: list[dict] = [
    {
        "name": "Amazon Web Services (AWS)",
        "service": "Cloud infrastructure hosting",
        "data_access": "personal",
        "criticality": "critical",
        "certifications": ["iso27001", "soc2-type2", "gdpr-dpa"],
        "geo_risk": "eu-eea",
        "subprocessors": "documented",
        "dpa_signed": True,
        "review_date": "2025-12-01",
        "notes": "Primary infrastructure provider; EU region (Frankfurt/Ireland)",
    },
    {
        "name": "GitHub (Microsoft)",
        "service": "Source code repository, CI/CD",
        "data_access": "metadata",
        "criticality": "high",
        "certifications": ["iso27001", "soc2-type2"],
        "geo_risk": "sccs-required",
        "subprocessors": "documented",
        "dpa_signed": True,
        "review_date": "2025-11-15",
        "notes": "US-based; SCCs in place via DPA; code may contain metadata",
    },
    {
        "name": "[PAYMENT PROVIDER]",
        "service": "Payment processing",
        "data_access": "personal",
        "criticality": "critical",
        "certifications": ["iso27001", "soc2-type2", "iso27701"],
        "geo_risk": "eu-eea",
        "subprocessors": "documented",
        "dpa_signed": True,
        "review_date": "2025-10-01",
        "notes": "PCI DSS Level 1 compliant; processes payment personal data",
    },
    {
        "name": "[EMAIL SERVICE]",
        "service": "Transactional email delivery",
        "data_access": "personal",
        "criticality": "high",
        "certifications": ["soc2-type2", "gdpr-dpa"],
        "geo_risk": "adequacy-decision",
        "subprocessors": "documented",
        "dpa_signed": True,
        "review_date": "2026-01-15",
        "notes": "EU data residency option available; adequacy country",
    },
    {
        "name": "[ANALYTICS PROVIDER]",
        "service": "Product analytics and user behaviour",
        "data_access": "pseudonymised",
        "criticality": "medium",
        "certifications": ["soc2-type2"],
        "geo_risk": "sccs-required",
        "subprocessors": "documented",
        "dpa_signed": True,
        "review_date": "2026-03-01",
        "notes": "Pseudonymised data only; US-based with SCCs",
    },
]


# ── Risk Assessment Functions ──────────────────────────────────────────────


def calculate_vendor_risk(vendor: dict) -> dict:
    """Calculate risk score and level for a vendor."""
    score = 0
    factors = []

    # Data access risk
    da = vendor.get("data_access", "none")
    da_score = DATA_ACCESS_WEIGHTS.get(da, 0)
    score += da_score
    factors.append({"factor": "Data Access", "value": da, "score": da_score})

    # Service criticality
    crit = vendor.get("criticality", "low")
    crit_score = SERVICE_CRITICALITY_WEIGHTS.get(crit, 0)
    score += crit_score
    factors.append({"factor": "Service Criticality", "value": crit, "score": crit_score})

    # Compliance certifications
    certs = vendor.get("certifications", [])
    cert_score = 0
    if not certs or certs == ["none"]:
        cert_score = COMPLIANCE_CERT_WEIGHTS["none"]
        factors.append({"factor": "Certifications", "value": "None", "score": cert_score})
    else:
        for cert in certs:
            w = COMPLIANCE_CERT_WEIGHTS.get(cert, 0)
            cert_score += w
            factors.append({"factor": f"Cert: {cert}", "value": cert, "score": w})
    score += cert_score

    # Geographic risk
    geo = vendor.get("geo_risk", "eu-eea")
    geo_score = GEO_RISK_WEIGHTS.get(geo, 0)
    score += geo_score
    factors.append({"factor": "Geographic Risk", "value": geo, "score": geo_score})

    # Subprocessor risk
    sub = vendor.get("subprocessors", "none")
    sub_score = SUBPROCESSOR_WEIGHTS.get(sub, 0)
    score += sub_score
    factors.append({"factor": "Subprocessors", "value": sub, "score": sub_score})

    # DPA status bonus/penalty
    if not vendor.get("dpa_signed", False):
        score += 20
        factors.append({"factor": "DPA Status", "value": "NOT SIGNED", "score": 20})
    else:
        factors.append({"factor": "DPA Status", "value": "Signed", "score": -5})
        score -= 5

    # Clamp score to 0-100
    score = max(0, min(100, score))

    # Determine risk level
    risk_level = "LOW"
    for level, (low, high) in RISK_THRESHOLDS.items():
        if low <= score <= high:
            risk_level = level
            break

    # Determine review frequency based on risk level
    review_frequency = {
        "LOW": "Annual",
        "MEDIUM": "Semi-annual",
        "HIGH": "Quarterly",
        "CRITICAL": "Monthly",
    }

    return {
        "vendor_name": vendor.get("name", "Unknown"),
        "service": vendor.get("service", "Unknown"),
        "risk_score": score,
        "risk_level": risk_level,
        "factors": factors,
        "review_frequency": review_frequency[risk_level],
        "dpa_signed": vendor.get("dpa_signed", False),
        "notes": vendor.get("notes", ""),
        "assessed_at": datetime.now(tz=UTC).isoformat(),
    }


def assess_all_vendors(vendors: list[dict]) -> list[dict]:
    """Assess all vendors and return sorted results."""
    results = [calculate_vendor_risk(v) for v in vendors]
    results.sort(key=lambda r: r["risk_score"], reverse=True)
    return results


def print_assessment(result: dict) -> None:
    """Print a single vendor risk assessment."""
    print(f"\n{'=' * 60}")
    print(f"  VENDOR RISK ASSESSMENT: {result['vendor_name']}")
    print(f"{'=' * 60}")
    print(f"  Service:          {result['service']}")
    print(f"  Risk Score:       {result['risk_score']}/100")
    print(f"  Risk Level:       {result['risk_level']}")
    print(f"  DPA Signed:       {'Yes' if result['dpa_signed'] else 'NO — ACTION REQUIRED'}")
    print(f"  Review Frequency: {result['review_frequency']}")

    print("\n  RISK FACTORS:")
    print(f"  {'Factor':<30s} {'Value':<20s} {'Score':>6s}")
    print(f"  {'-' * 58}")
    for f in result["factors"]:
        print(f"  {f['factor']:<30s} {f['value']:<20s} {f['score']:>+6d}")

    if result["notes"]:
        print(f"\n  Notes: {result['notes']}")

    # Recommendations
    print("\n  RECOMMENDATIONS:")
    if result["risk_level"] == "CRITICAL":
        print("    [!] Immediate CISO review required")
        print("    [!] Verify DPA and SCCs are current")
        print("    [!] Conduct enhanced due diligence")
    if result["risk_level"] in ("HIGH", "CRITICAL"):
        print("    [*] Schedule enhanced monitoring")
        print("    [*] Verify data residency and transfer mechanisms")
    if not result["dpa_signed"]:
        print("    [!] Execute DPA before any data sharing")
    if result["risk_level"] == "LOW":
        print("    [✓] Standard monitoring — annual review sufficient")

    print(f"\n  Assessed: {result['assessed_at']}")


def print_report(results: list[dict]) -> None:
    """Print a summary risk report for all vendors."""
    now = datetime.now(tz=UTC)

    print(f"\n{'=' * 72}")
    print("  JOL VENDOR RISK REPORT")
    print(f"  Generated: {now.strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"{'=' * 72}")

    # Summary counts
    levels = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0}
    unsigned_dpa = 0
    for r in results:
        levels[r["risk_level"]] += 1
        if not r["dpa_signed"]:
            unsigned_dpa += 1

    print(f"\n  Total Vendors:    {len(results)}")
    print(f"  Critical Risk:    {levels['CRITICAL']}")
    print(f"  High Risk:        {levels['HIGH']}")
    print(f"  Medium Risk:      {levels['MEDIUM']}")
    print(f"  Low Risk:         {levels['LOW']}")
    print(f"  DPA Unsigned:     {unsigned_dpa}")

    print(f"\n  {'Vendor':<35s} {'Score':>6s} {'Level':<10s} {'DPA':<5s} {'Review':<12s}")
    print(f"  {'-' * 70}")

    for r in results:
        dpa = "Yes" if r["dpa_signed"] else "NO"
        print(
            f"  {r['vendor_name']:<35s} {r['risk_score']:>6d} "
            f"{r['risk_level']:<10s} {dpa:<5s} {r['review_frequency']:<12s}"
        )

    # Action items
    action_items = []
    for r in results:
        if not r["dpa_signed"]:
            action_items.append(f"Execute DPA with {r['vendor_name']}")
        if r["risk_level"] == "CRITICAL":
            action_items.append(f"Urgent review of {r['vendor_name']}")
        if r["risk_level"] == "HIGH":
            action_items.append(f"Enhanced due diligence for {r['vendor_name']}")

    if action_items:
        print("\n  ACTION ITEMS:")
        for i, item in enumerate(action_items, 1):
            print(f"    {i}. {item}")

    print(f"\n{'=' * 72}\n")


# ── Interactive Assessment ─────────────────────────────────────────────────


def interactive_assessment() -> dict:
    """Run an interactive vendor risk assessment."""
    print("\n  JOL Vendor Risk Assessment — Interactive Mode")
    print("  " + "-" * 45)

    name = input("  Vendor name: ").strip() or "Unknown Vendor"
    service = input("  Service description: ").strip() or "Unknown"

    print(f"\n  Data access level: {', '.join(DATA_ACCESS_WEIGHTS.keys())}")
    data_access = input("  Data access [personal]: ").strip() or "personal"
    if data_access not in DATA_ACCESS_WEIGHTS:
        data_access = "personal"

    print(f"  Service criticality: {', '.join(SERVICE_CRITICALITY_WEIGHTS.keys())}")
    criticality = input("  Criticality [high]: ").strip() or "high"
    if criticality not in SERVICE_CRITICALITY_WEIGHTS:
        criticality = "high"

    print(f"  Geographic risk: {', '.join(GEO_RISK_WEIGHTS.keys())}")
    geo_risk = input("  Geographic risk [eu-eea]: ").strip() or "eu-eea"
    if geo_risk not in GEO_RISK_WEIGHTS:
        geo_risk = "eu-eea"

    certs_input = input("  Certifications (comma-separated) [iso27001,soc2-type2]: ").strip()
    certs = [c.strip() for c in certs_input.split(",")] if certs_input else ["iso27001", "soc2-type2"]

    dpa = input("  DPA signed? [y/N]: ").strip().lower() in ("y", "yes")

    vendor = {
        "name": name,
        "service": service,
        "data_access": data_access,
        "criticality": criticality,
        "certifications": certs,
        "geo_risk": geo_risk,
        "subprocessors": "documented",
        "dpa_signed": dpa,
        "review_date": "",
        "notes": "",
    }

    return calculate_vendor_risk(vendor)


# ── Main ───────────────────────────────────────────────────────────────────


def main() -> int:
    parser = argparse.ArgumentParser(
        description="JOL Vendor Risk Calculator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--vendor", help="Vendor name for individual assessment")
    parser.add_argument("--data-access", choices=list(DATA_ACCESS_WEIGHTS.keys()), default="personal")
    parser.add_argument("--criticality", choices=list(SERVICE_CRITICALITY_WEIGHTS.keys()), default="high")
    parser.add_argument("--geo-risk", choices=list(GEO_RISK_WEIGHTS.keys()), default="eu-eea")
    parser.add_argument("--assess-all", action="store_true", help="Assess all sample vendors")
    parser.add_argument("--report", action="store_true", help="Print vendor risk summary report")
    parser.add_argument("--interactive", action="store_true", help="Interactive vendor assessment")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.interactive:
        result = interactive_assessment()
        print_assessment(result)
        return 0

    if args.assess_all or args.report:
        results = assess_all_vendors(SAMPLE_VENDORS)
        if args.json:
            print(json.dumps(results, indent=2, ensure_ascii=False))
        else:
            print_report(results)
        return 0

    if args.vendor:
        vendor = {
            "name": args.vendor,
            "service": "Custom assessment",
            "data_access": args.data_access,
            "criticality": args.criticality,
            "certifications": [],
            "geo_risk": args.geo_risk,
            "subprocessors": "documented",
            "dpa_signed": False,
            "notes": "",
        }
        result = calculate_vendor_risk(vendor)
        if args.json:
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print_assessment(result)
        return 0

    # Default: print report
    results = assess_all_vendors(SAMPLE_VENDORS)
    print_report(results)
    return 0


if __name__ == "__main__":
    sys.exit(main())

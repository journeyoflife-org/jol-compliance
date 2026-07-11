#!/usr/bin/env python3
"""
JOL Compliance Evidence Collector
==================================
Automated collection and organisation of audit evidence for
ISO 27001:2022, SOC 2 Type II, and GDPR compliance audits.

Document ID: JOL-SCRIPT-EC-001
Owner: DevOps Lead
Version: 1.0
Classification: RESTRICTED

Usage:
    python scripts/evidence_collector.py --framework all --output ./evidence-export
    python scripts/evidence_collector.py --framework iso27001 --output ./iso-evidence
    python scripts/evidence_collector.py --framework soc2 --output ./soc2-evidence
    python scripts/evidence_collector.py --framework gdpr --output ./gdpr-evidence
"""

import argparse
import hashlib
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


# ── Configuration ──────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT = REPO_ROOT / "evidence-export"

EVIDENCE_SOURCES: dict[str, list[dict]] = {
    "iso27001": [
        {
            "name": "Information Security Policy",
            "source": "iso27001/policies/information-security-policy.md",
            "clause": "5.2",
            "control": "A.5.1",
            "description": "ISMS information security policy",
        },
        {
            "name": "Risk Register",
            "source": "iso27001/risk-register/risk-register-2026.md",
            "clause": "6.1.2",
            "control": "A.5.9",
            "description": "Current risk register with assessments",
        },
        {
            "name": "Statement of Applicability",
            "source": "iso27001/soa/statement-of-applicability.md",
            "clause": "6.1.3",
            "control": "N/A",
            "description": "SoA covering all 93 Annex A controls",
        },
        {
            "name": "Asset Register",
            "source": "iso27001/asset-register/asset-register.md",
            "clause": "6.1.2",
            "control": "A.5.9",
            "description": "Information asset inventory",
        },
        {
            "name": "Internal Audit Template",
            "source": "iso27001/internal-audits/internal-audit-template.md",
            "clause": "9.2",
            "control": "N/A",
            "description": "Internal audit programme and findings template",
        },
        {
            "name": "Management Review Template",
            "source": "iso27001/management-reviews/management-review-template.md",
            "clause": "9.3",
            "control": "N/A",
            "description": "Management review meeting template",
        },
        {
            "name": "Access Control Procedure",
            "source": "iso27001/procedures/access-control-procedure.md",
            "clause": "6.1.2",
            "control": "A.5.15",
            "description": "Access control implementation procedure",
        },
    ],
    "soc2": [
        {
            "name": "Trust Services Criteria Mapping",
            "source": "soc2/trust-services-criteria/tsc-control-mapping.md",
            "clause": "N/A",
            "control": "CC1-CC9",
            "description": "SOC 2 TSC to internal control mapping",
        },
        {
            "name": "Access Control Evidence",
            "source": "soc2/evidence/cc6/access-control-evidence.md",
            "clause": "N/A",
            "control": "CC6",
            "description": "Logical access control evidence collection guide",
        },
        {
            "name": "System Operations Evidence",
            "source": "soc2/evidence/cc7/system-operations-evidence.md",
            "clause": "N/A",
            "control": "CC7",
            "description": "System operations monitoring evidence",
        },
        {
            "name": "Change Management Evidence",
            "source": "soc2/evidence/cc8/change-management-evidence.md",
            "clause": "N/A",
            "control": "CC8",
            "description": "Change management evidence collection guide",
        },
        {
            "name": "Availability Evidence",
            "source": "soc2/evidence/a1/availability-evidence.md",
            "clause": "N/A",
            "control": "A1",
            "description": "Availability SLA and uptime evidence",
        },
        {
            "name": "Quarterly Access Review",
            "source": "soc2/access-reviews/quarterly-access-review-template.md",
            "clause": "N/A",
            "control": "CC6.1",
            "description": "Quarterly user access review template",
        },
        {
            "name": "Vendor Compliance Review",
            "source": "soc2/vendor-reviews/vendor-compliance-review-template.md",
            "clause": "N/A",
            "control": "CC9.2",
            "description": "Vendor compliance review template",
        },
    ],
    "gdpr": [
        {
            "name": "Privacy Policy (Lithuania)",
            "source": "gdpr/privacy-policies/lt/privacy-policy-lt.md",
            "clause": "Art. 13-14",
            "control": "N/A",
            "description": "Data subject privacy notice — Lithuania",
        },
        {
            "name": "Privacy Policy (Latvia)",
            "source": "gdpr/privacy-policies/lv/privacy-policy-lv.md",
            "clause": "Art. 13-14",
            "control": "N/A",
            "description": "Data subject privacy notice — Latvia",
        },
        {
            "name": "Privacy Policy (Estonia)",
            "source": "gdpr/privacy-policies/ee/privacy-policy-ee.md",
            "clause": "Art. 13-14",
            "control": "N/A",
            "description": "Data subject privacy notice — Estonia",
        },
        {
            "name": "ROPA Template",
            "source": "gdpr/ropa/ropa-template.md",
            "clause": "Art. 30",
            "control": "N/A",
            "description": "Records of Processing Activities template",
        },
        {
            "name": "DPIA Template",
            "source": "gdpr/dpias/dpia-template.md",
            "clause": "Art. 35",
            "control": "N/A",
            "description": "Data Protection Impact Assessment template",
        },
        {
            "name": "Data Retention Policy",
            "source": "gdpr/retention-policies/data-retention-policy.md",
            "clause": "Art. 5(1)(e)",
            "control": "N/A",
            "description": "Data retention and disposal policy",
        },
        {
            "name": "Cookie Policy",
            "source": "gdpr/cookie-policies/cookie-policy.md",
            "clause": "Art. 5(3) ePrivacy",
            "control": "N/A",
            "description": "Cookie consent and management policy",
        },
        {
            "name": "Data Subject Rights Procedure",
            "source": "gdpr/dsr-procedures/data-subject-rights-procedure.md",
            "clause": "Art. 15-22",
            "control": "N/A",
            "description": "DSR handling procedure",
        },
    ],
    "security-policies": [
        {
            "name": "Acceptable Use Policy",
            "source": "security-policies/acceptable-use-policy.md",
            "clause": "N/A",
            "control": "A.5.10",
            "description": "Acceptable use of information assets",
        },
        {
            "name": "Password Policy",
            "source": "security-policies/password-policy.md",
            "clause": "N/A",
            "control": "A.5.17",
            "description": "Authentication credential management",
        },
        {
            "name": "Incident Response Policy",
            "source": "security-policies/incident-response-policy.md",
            "clause": "N/A",
            "control": "A.5.24",
            "description": "Information security incident management",
        },
        {
            "name": "Data Classification Policy",
            "source": "security-policies/data-classification-policy.md",
            "clause": "N/A",
            "control": "A.5.12",
            "description": "Information classification scheme",
        },
        {
            "name": "Encryption Policy",
            "source": "security-policies/encryption-policy.md",
            "clause": "N/A",
            "control": "A.8.24",
            "description": "Use of cryptography",
        },
        {
            "name": "Backup and Recovery Policy",
            "source": "security-policies/backup-and-recovery-policy.md",
            "clause": "N/A",
            "control": "A.8.13",
            "description": "Information backup",
        },
        {
            "name": "Remote Work Security Policy",
            "source": "security-policies/remote-work-security-policy.md",
            "clause": "N/A",
            "control": "A.6.7",
            "description": "Remote working security controls",
        },
    ],
}


# ── Helper Functions ───────────────────────────────────────────────────────


def compute_sha256(file_path: Path) -> str:
    """Compute SHA-256 hash of a file for integrity verification."""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return "FILE_NOT_FOUND"


def get_file_metadata(file_path: Path) -> dict:
    """Extract metadata from a file."""
    if not file_path.exists():
        return {"exists": False, "size": 0, "hash": "N/A", "modified": "N/A"}

    stat = file_path.stat()
    return {
        "exists": True,
        "size_bytes": stat.st_size,
        "hash_sha256": compute_sha256(file_path),
        "modified": datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(),
        "path": str(file_path.relative_to(REPO_ROOT)),
    }


def collect_evidence(
    framework: str,
    output_dir: Path,
    dry_run: bool = False,
) -> list[dict]:
    """Collect evidence files for a specific framework."""
    sources = EVIDENCE_SOURCES.get(framework, [])
    results = []

    framework_dir = output_dir / framework
    if not dry_run:
        framework_dir.mkdir(parents=True, exist_ok=True)

    for item in sources:
        source_path = REPO_ROOT / item["source"]
        metadata = get_file_metadata(source_path)

        record = {
            "name": item["name"],
            "framework": framework,
            "clause": item["clause"],
            "control": item["control"],
            "description": item["description"],
            "source": item["source"],
            "status": "COLLECTED" if metadata["exists"] else "MISSING",
            "metadata": metadata,
        }

        if metadata["exists"] and not dry_run:
            dest = framework_dir / source_path.name
            shutil.copy2(source_path, dest)
            record["collected_to"] = str(dest.relative_to(output_dir))

        results.append(record)

    return results


def generate_manifest(
    all_results: list[dict],
    output_dir: Path,
    dry_run: bool = False,
) -> dict:
    """Generate an evidence collection manifest (JSON)."""
    now = datetime.now(tz=timezone.utc)

    collected = [r for r in all_results if r["status"] == "COLLECTED"]
    missing = [r for r in all_results if r["status"] == "MISSING"]

    manifest = {
        "manifest_id": f"EVM-{now.strftime('%Y%m%d-%H%M%S')}",
        "generated_at": now.isoformat(),
        "generated_by": "jol-evidence-collector-v1.0",
        "repository": "jol-compliance",
        "summary": {
            "total_items": len(all_results),
            "collected": len(collected),
            "missing": len(missing),
            "completeness_pct": round(
                len(collected) / max(len(all_results), 1) * 100, 1
            ),
        },
        "frameworks": {},
        "items": all_results,
    }

    # Group by framework
    for framework in EVIDENCE_SOURCES:
        fw_items = [r for r in all_results if r["framework"] == framework]
        fw_collected = [r for r in fw_items if r["status"] == "COLLECTED"]
        manifest["frameworks"][framework] = {
            "total": len(fw_items),
            "collected": len(fw_collected),
            "missing": len(fw_items) - len(fw_collected),
        }

    if not dry_run:
        manifest_path = output_dir / "evidence-manifest.json"
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
        print(f"  Manifest written to: {manifest_path}")

    return manifest


def print_report(manifest: dict) -> None:
    """Print a human-readable evidence collection report."""
    print("\n" + "=" * 72)
    print("  EVIDENCE COLLECTION REPORT")
    print(f"  Manifest ID: {manifest['manifest_id']}")
    print(f"  Generated:   {manifest['generated_at']}")
    print("=" * 72)

    summary = manifest["summary"]
    print(f"\n  Total items:    {summary['total_items']}")
    print(f"  Collected:      {summary['collected']}")
    print(f"  Missing:        {summary['missing']}")
    print(f"  Completeness:   {summary['completeness_pct']}%")

    print("\n" + "-" * 72)
    print("  FRAMEWORK BREAKDOWN")
    print("-" * 72)

    for fw, stats in manifest["frameworks"].items():
        status = "OK" if stats["missing"] == 0 else "GAPS"
        print(f"  [{status:4s}] {fw:25s}  {stats['collected']}/{stats['total']} collected")

    missing_items = [
        r for r in manifest["items"] if r["status"] == "MISSING"
    ]
    if missing_items:
        print("\n" + "-" * 72)
        print("  MISSING EVIDENCE")
        print("-" * 72)
        for item in missing_items:
            print(f"  [MISS] {item['framework']}/{item['name']}")
            print(f"         Source: {item['source']}")

    print("\n" + "=" * 72)
    completeness = summary["completeness_pct"]
    if completeness == 100.0:
        print("  STATUS: ALL EVIDENCE COLLECTED SUCCESSFULLY")
    elif completeness >= 80.0:
        print(f"  STATUS: MOSTLY COMPLETE — {summary['missing']} item(s) missing")
    else:
        print(f"  STATUS: SIGNIFICANT GAPS — {summary['missing']} item(s) missing")
    print("=" * 72 + "\n")


# ── Main ───────────────────────────────────────────────────────────────────


def main() -> int:
    parser = argparse.ArgumentParser(
        description="JOL Compliance Evidence Collector",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--framework",
        choices=["all", "iso27001", "soc2", "gdpr", "security-policies"],
        default="all",
        help="Framework to collect evidence for (default: all)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Output directory (default: {DEFAULT_OUTPUT})",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Check evidence availability without copying files",
    )

    args = parser.parse_args()

    frameworks = (
        list(EVIDENCE_SOURCES.keys())
        if args.framework == "all"
        else [args.framework]
    )

    print(f"JOL Evidence Collector v1.0")
    print(f"Repository: {REPO_ROOT}")
    print(f"Frameworks: {', '.join(frameworks)}")
    print(f"Output:     {args.output}")
    if args.dry_run:
        print("Mode:       DRY RUN (no files will be copied)")
    print()

    if not args.dry_run:
        args.output.mkdir(parents=True, exist_ok=True)

    all_results: list[dict] = []
    for fw in frameworks:
        print(f"  Collecting evidence for: {fw}")
        results = collect_evidence(fw, args.output, dry_run=args.dry_run)
        all_results.extend(results)
        collected = sum(1 for r in results if r["status"] == "COLLECTED")
        print(f"    {collected}/{len(results)} items collected")

    manifest = generate_manifest(all_results, args.output, dry_run=args.dry_run)
    print_report(manifest)

    return 0 if manifest["summary"]["missing"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

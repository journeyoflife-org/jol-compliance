"""
Compliance Repository Validator

Validates the structure, completeness, and content of the jol-compliance
repository against GDPR, ISO 27001:2022, and SOC 2 Type II requirements.

Usage:
    python compliance_validator.py [--strict] [--json] [--quiet]
"""

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent


class Severity(Enum):
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"


@dataclass
class Finding:
    severity: Severity
    category: str
    message: str
    path: str | None = None

    def __init__(
        self,
        severity: Severity,
        category: str,
        message: str,
        path: str | None = None,
    ) -> None:
        self.severity = severity
        self.category = category
        self.message = message
        self.path = path

    def to_dict(self) -> dict:
        return {
            "severity": self.severity.value,
            "category": self.category,
            "message": self.message,
            "path": self.path,
        }


@dataclass
class ValidationReport:
    findings: list = field(default_factory=list)
    checks_run: int = 0
    checks_passed: int = 0

    def __init__(
        self,
        findings: list = None,
        checks_run: int = 0,
        checks_passed: int = 0,
    ) -> None:
        self.findings = findings if findings is not None else []
        self.checks_run = checks_run
        self.checks_passed = checks_passed

    def add(self, finding: Finding) -> None:
        self.findings.append(finding)

    def ok(self, category: str, message: str) -> None:
        self.checks_run += 1
        self.checks_passed += 1
        self.findings.append(Finding(Severity.INFO, category, message))

    def warn(self, category: str, message: str, path: str = None) -> None:
        self.checks_run += 1
        self.findings.append(Finding(Severity.WARNING, category, message, path))

    def fail(self, category: str, message: str, path: str = None) -> None:
        self.checks_run += 1
        self.findings.append(Finding(Severity.ERROR, category, message, path))

    @property
    def error_count(self) -> int:
        return sum(1 for f in self.findings if f.severity == Severity.ERROR)

    @property
    def warning_count(self) -> int:
        return sum(1 for f in self.findings if f.severity == Severity.WARNING)

    def to_dict(self) -> dict:
        return {
            "checks_run": self.checks_run,
            "checks_passed": self.checks_passed,
            "errors": self.error_count,
            "warnings": self.warning_count,
            "findings": [f.to_dict() for f in self.findings],
        }


# ---------------------------------------------------------------------------
# Required structure
# ---------------------------------------------------------------------------

REQUIRED_DIRECTORIES = [
    # GDPR
    "gdpr",
    "gdpr/ropa",
    "gdpr/dpias",
    "gdpr/privacy-policies",
    "gdpr/privacy-policies/lt",
    "gdpr/privacy-policies/lv",
    "gdpr/privacy-policies/ee",
    "gdpr/retention-policies",
    "gdpr/cookie-policies",
    "gdpr/dsr-procedures",
    # ISO 27001
    "iso27001",
    "iso27001/risk-register",
    "iso27001/asset-register",
    "iso27001/soa",
    "iso27001/policies",
    "iso27001/procedures",
    "iso27001/internal-audits",
    "iso27001/management-reviews",
    # SOC 2
    "soc2",
    "soc2/trust-services-criteria",
    "soc2/evidence",
    "soc2/evidence/cc6",
    "soc2/evidence/cc7",
    "soc2/evidence/cc8",
    "soc2/evidence/a1",
    "soc2/access-reviews",
    "soc2/vendor-reviews",
    # Other
    "security-policies",
    "vendor-register",
    "audit-evidence",
    "audit-evidence/github",
    "audit-evidence/infrastructure",
    "audit-evidence/penetration-tests",
    "audit-evidence/vulnerability-scans",
    "country",
    "country/lt",
    "country/lv",
    "country/ee",
    "docs",
]

REQUIRED_FILES = [
    ".gitignore",
    "gdpr/ropa/ropa-template.md",
    "gdpr/dpias/dpia-template.md",
    "iso27001/risk-register/risk-register-template.md",
    "iso27001/soa/soa-template.md",
    "soc2/evidence/cc6/access-control-evidence-template.md",
    "security-policies/information-security-policy.md",
    "docs/compliance-checklist.md",
]

# Templates that must contain specific GDPR article references
GDPR_CONTENT_CHECKS = {
    "gdpr/ropa/ropa-template.md": {
        "required_strings": [
            "Article 30",
            "Art. 9",
            "Art. 6",
            "Legal Basis",
            "Data Subject",
            "Retention",
        ],
        "required_placeholders": ["Company Name", "DPO"],
        "label": "ROPA",
    },
    "gdpr/dpias/dpia-template.md": {
        "required_strings": [
            "Article 35",
            "Likelihood",
            "Severity",
            "Risk",
            "Mitigation",
            "Supervisory Authority",
        ],
        "required_placeholders": ["Company Name", "DPO"],
        "label": "DPIA",
    },
}

# ISO 27001 template checks
ISO27001_CONTENT_CHECKS = {
    "iso27001/risk-register/risk-register-template.md": {
        "required_strings": [
            "ISO/IEC 27001",
            "Risk",
            "Likelihood",
            "Impact",
            "CIA",
            "Treatment",
        ],
        "required_placeholders": ["Company Name"],
        "label": "Risk Register",
    },
    "iso27001/soa/soa-template.md": {
        "required_strings": [
            "Statement of Applicability",
            "A.5",
            "A.6",
            "A.7",
            "A.8",
            "Annex A",
        ],
        "required_placeholders": ["Company Name"],
        "label": "SoA",
    },
}

# SOC 2 template checks
SOC2_CONTENT_CHECKS = {
    "soc2/evidence/cc6/access-control-evidence-template.md": {
        "required_strings": [
            "CC6",
            "SOC 2",
            "Access Control",
            "Authentication",
            "MFA",
        ],
        "required_placeholders": ["Company Name"],
        "label": "CC6 Evidence",
    },
}

# Master policy and checklist checks
POLICY_CONTENT_CHECKS = {
    "security-policies/information-security-policy.md": {
        "required_strings": [
            "ISO/IEC 27001",
            "GDPR",
            "SOC 2",
            "Access Control",
            "Encryption",
            "Incident",
            "Business Continuity",
        ],
        "required_placeholders": ["Company Name", "CISO"],
        "label": "InfoSec Policy",
    },
    "docs/compliance-checklist.md": {
        "required_strings": [
            "GDPR",
            "ISO 27001",
            "SOC 2",
            "DPIA",
            "ROPA",
            "Breach",
        ],
        "required_placeholders": ["Company Name"],
        "label": "Compliance Checklist",
    },
}

ALL_CONTENT_CHECKS = {
    **GDPR_CONTENT_CHECKS,
    **ISO27001_CONTENT_CHECKS,
    **SOC2_CONTENT_CHECKS,
    **POLICY_CONTENT_CHECKS,
}


# ---------------------------------------------------------------------------
# Validators
# ---------------------------------------------------------------------------

def validate_directory_structure(report: ValidationReport) -> None:
    """Check that all required directories exist."""
    for dir_path in REQUIRED_DIRECTORIES:
        full_path = REPO_ROOT / dir_path
        if full_path.is_dir():
            report.ok("structure", f"Directory exists: {dir_path}")
        else:
            report.fail("structure", f"Missing directory: {dir_path}", dir_path)


def validate_required_files(report: ValidationReport) -> None:
    """Check that all required template files exist."""
    for file_path in REQUIRED_FILES:
        full_path = REPO_ROOT / file_path
        if full_path.is_file():
            report.ok("files", f"Required file exists: {file_path}")
        else:
            report.fail("files", f"Missing required file: {file_path}", file_path)


def validate_gitignore(report: ValidationReport) -> None:
    """Check that .gitignore excludes expected patterns."""
    gitignore_path = REPO_ROOT / ".gitignore"
    if not gitignore_path.is_file():
        report.fail("gitignore", ".gitignore not found")
        return

    content = gitignore_path.read_text(encoding="utf-8")
    required_patterns = [".venv/", ".idea/", "__pycache__/", "*.save"]

    for pattern in required_patterns:
        if pattern in content:
            report.ok("gitignore", f".gitignore excludes: {pattern}")
        else:
            report.warn("gitignore", f".gitignore missing pattern: {pattern}", ".gitignore")


def validate_template_content(report: ValidationReport) -> None:
    """Validate that templates contain required sections and placeholders."""
    for file_path, checks in ALL_CONTENT_CHECKS.items():
        full_path = REPO_ROOT / file_path
        label = checks["label"]

        if not full_path.is_file():
            report.fail("content", f"[{label}] File not found: {file_path}", file_path)
            continue

        content = full_path.read_text(encoding="utf-8")

        # Check required strings
        for required_str in checks["required_strings"]:
            if required_str.lower() in content.lower():
                report.ok("content", f"[{label}] Contains required section: '{required_str}'")
            else:
                report.fail(
                    "content",
                    f"[{label}] Missing required content: '{required_str}'",
                    file_path,
                )

        # Check required placeholders
        for placeholder in checks["required_placeholders"]:
            pattern = rf"\[{re.escape(placeholder)}[^\]]*\]"
            if re.search(pattern, content):
                report.ok("content", f"[{label}] Contains placeholder: [{placeholder}...]")
            else:
                report.warn(
                    "content",
                    f"[{label}] Missing placeholder: [{placeholder}...]",
                    file_path,
                )


def validate_privacy_policies(report: ValidationReport) -> None:
    """Check that country-specific privacy policy directories have content."""
    countries = ["lt", "lv", "ee"]
    for country in countries:
        policy_dir = REPO_ROOT / "gdpr" / "privacy-policies" / country
        if not policy_dir.is_dir():
            report.fail("privacy", f"Missing privacy policy directory: gdpr/privacy-policies/{country}")
            continue

        md_files = list(policy_dir.glob("*.md"))
        if md_files:
            report.ok("privacy", f"Privacy policy exists for {country.upper()}: {md_files[0].name}")
        else:
            report.warn(
                "privacy",
                f"No privacy policy (.md) found for {country.upper()}",
                f"gdpr/privacy-policies/{country}/",
            )


def validate_country_compliance(report: ValidationReport) -> None:
    """Check that country-specific compliance directories have content."""
    countries = ["lt", "lv", "ee"]
    for country in countries:
        country_dir = REPO_ROOT / "country" / country
        if not country_dir.is_dir():
            report.fail("country", f"Missing country directory: country/{country}")
            continue

        # Check for any non-gitkeep files
        real_files = [f for f in country_dir.iterdir() if f.name != ".gitkeep"]
        if real_files:
            report.ok("country", f"Country {country.upper()} has compliance content: {[f.name for f in real_files]}")
        else:
            report.warn(
                "country",
                f"Country {country.upper()} directory exists but has no compliance documents yet",
                f"country/{country}/",
            )


def validate_soc2_evidence_coverage(report: ValidationReport) -> None:
    """Check that SOC 2 evidence directories have template or evidence files."""
    evidence_dirs = ["cc6", "cc7", "cc8", "a1"]
    for sub_dir in evidence_dirs:
        ev_path = REPO_ROOT / "soc2" / "evidence" / sub_dir
        if not ev_path.is_dir():
            report.fail("soc2", f"Missing SOC 2 evidence directory: soc2/evidence/{sub_dir}")
            continue

        md_files = list(ev_path.glob("*.md"))
        if md_files:
            report.ok("soc2", f"SOC 2 evidence template exists for {sub_dir.upper()}")
        else:
            report.warn(
                "soc2",
                f"No evidence template (.md) in soc2/evidence/{sub_dir}",
                f"soc2/evidence/{sub_dir}/",
            )


def validate_empty_directories(report: ValidationReport) -> None:
    """Identify directories that are still empty (only .gitkeep or nothing)."""
    skip_prefixes = [".git", ".venv", ".idea", "node_modules"]

    for dir_path, _, files in os.walk(REPO_ROOT):
        rel = os.path.relpath(dir_path, REPO_ROOT)
        if any(rel.startswith(p) for p in skip_prefixes):
            continue

        real_files = [f for f in files if f != ".gitkeep"]
        if not real_files and not files:
            report.warn("completeness", f"Empty directory: {rel}", rel)


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

ANSI_COLORS = {
    Severity.ERROR: "\033[91m",   # Red
    Severity.WARNING: "\033[93m", # Yellow
    Severity.INFO: "\033[36m",    # Cyan
}
ANSI_RESET = "\033[0m"
ANSI_BOLD = "\033[1m"


def print_report(report: ValidationReport, quiet: bool = False) -> None:
    """Print human-readable validation report."""
    if not quiet:
        print(f"\n{ANSI_BOLD}{'='*70}")
        print("  jol-compliance Repository Validator")
        print(f"{'='*70}{ANSI_RESET}\n")

    errors = [f for f in report.findings if f.severity == Severity.ERROR]
    warnings = [f for f in report.findings if f.severity == Severity.WARNING]
    infos = [f for f in report.findings if f.severity == Severity.INFO]

    if not quiet:
        # Print errors first
        for finding in errors:
            color = ANSI_COLORS[finding.severity]
            path_str = f" ({finding.path})" if finding.path else ""
            print(f"  {color}[{finding.severity.value}]{ANSI_RESET} [{finding.category}] {finding.message}{path_str}")

        for finding in warnings:
            color = ANSI_COLORS[finding.severity]
            path_str = f" ({finding.path})" if finding.path else ""
            print(f"  {color}[{finding.severity.value}]{ANSI_RESET} [{finding.category}] {finding.message}{path_str}")

        if not errors and not warnings:
            for finding in infos:
                color = ANSI_COLORS[finding.severity]
                print(f"  {color}[{finding.severity.value}]{ANSI_RESET} [{finding.category}] {finding.message}")

        # Summary
        print(f"\n{ANSI_BOLD}{'─'*70}{ANSI_RESET}")
        print(f"  Checks run: {report.checks_run}")
        print(f"  Checks passed: {report.checks_passed}")
        print(f"  Errors: {ANSI_COLORS[Severity.ERROR]}{report.error_count}{ANSI_RESET}")
        print(f"  Warnings: {ANSI_COLORS[Severity.WARNING]}{report.warning_count}{ANSI_RESET}")
        print(f"  Info: {len(infos)}")

        if report.error_count == 0 and report.warning_count == 0:
            print(f"\n  {ANSI_BOLD}\033[92m✓ Repository is fully compliant.{ANSI_RESET}")
        elif report.error_count == 0:
            print(f"\n  {ANSI_BOLD}\033[93m⚠ Repository has warnings but no errors.{ANSI_RESET}")
        else:
            msg = f"\u2717 Repository has {report.error_count} error(s) requiring attention."
            print(f"\n  {ANSI_BOLD}\033[91m{msg}{ANSI_RESET}")

        print(f"\n{ANSI_BOLD}{'='*70}{ANSI_RESET}\n")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def run_validation() -> ValidationReport:
    """Run all validators and return the report."""
    report = ValidationReport()

    validate_directory_structure(report)
    validate_required_files(report)
    validate_gitignore(report)
    validate_template_content(report)
    validate_privacy_policies(report)
    validate_country_compliance(report)
    validate_soc2_evidence_coverage(report)
    validate_empty_directories(report)

    return report


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate the jol-compliance repository structure and content."
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors (exit code 1 on warnings)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as JSON",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress info-level findings; only show errors and warnings",
    )

    args = parser.parse_args()
    report = run_validation()

    if args.json:
        print(json.dumps(report.to_dict(), indent=2))
    else:
        print_report(report, quiet=args.quiet)

    if report.error_count > 0:
        return 1
    if args.strict and report.warning_count > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

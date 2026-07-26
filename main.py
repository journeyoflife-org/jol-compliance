#!/usr/bin/env python3
"""
jol-compliance — CLI Entry Point
===================================
Unified command-line interface for the jol-compliance repository tools.

Usage:
    python main.py validate [--strict] [--json] [--quiet]
    python main.py evidence [--framework all] [--output DIR] [--dry-run]
    python main.py dsr [--list | --overdue | --metrics]
    python main.py retention [--list-categories | --audit | --category CAT --collected DATE]
    python main.py vendor-risk [--report | --assess-all | --vendor NAME]
"""

import sys
from pathlib import Path

# Ensure the repository root is on sys.path so sibling imports resolve
# when this script is executed from any working directory.
REPO_ROOT = Path(__file__).resolve().parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


def _print_usage() -> None:
    """Print top-level usage banner."""
    print(__doc__)
    print("Available commands:")
    print("  validate      Run the compliance repository validator")
    print("  evidence      Collect and report on audit evidence")
    print("  dsr           GDPR Data Subject Rights tracker")
    print("  retention     Data retention period calculator")
    print("  vendor-risk   Third-party vendor risk calculator")
    print()
    print("Run 'python main.py <command> --help' for command-specific options.")


def _dispatch_validate(argv: list[str]) -> int:
    """Dispatch to compliance_validator.main()."""
    from compliance_validator import main as validator_main

    sys.argv = ["compliance_validator"] + argv
    return validator_main()


def _dispatch_evidence(argv: list[str]) -> int:
    """Dispatch to scripts/evidence_collector.main()."""
    from scripts.evidence_collector import main as evidence_main

    sys.argv = ["evidence_collector"] + argv
    return evidence_main()


def _dispatch_dsr(argv: list[str]) -> int:
    """Dispatch to scripts/gdpr_dsr_tracker.main()."""
    from scripts.gdpr_dsr_tracker import main as dsr_main

    sys.argv = ["gdpr_dsr_tracker"] + argv
    return dsr_main()


def _dispatch_retention(argv: list[str]) -> int:
    """Dispatch to scripts/retention_calculator.main()."""
    from scripts.retention_calculator import main as retention_main

    sys.argv = ["retention_calculator"] + argv
    return retention_main()


def _dispatch_vendor_risk(argv: list[str]) -> int:
    """Dispatch to scripts/vendor_risk_calculator.main()."""
    from scripts.vendor_risk_calculator import main as vendor_main

    sys.argv = ["vendor_risk_calculator"] + argv
    return vendor_main()


COMMANDS = {
    "validate": _dispatch_validate,
    "evidence": _dispatch_evidence,
    "dsr": _dispatch_dsr,
    "retention": _dispatch_retention,
    "vendor-risk": _dispatch_vendor_risk,
}


def main() -> int:
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        _print_usage()
        return 0

    command = sys.argv[1]
    if command not in COMMANDS:
        print(f"Error: Unknown command '{command}'")
        print(f"Available commands: {', '.join(COMMANDS.keys())}")
        return 1

    return COMMANDS[command](sys.argv[2:])


if __name__ == "__main__":
    sys.exit(main())

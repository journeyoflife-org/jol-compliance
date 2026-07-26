#!/usr/bin/env bash
# =============================================================================
# run-compliance-lint.sh
#
# Runs compliance linting checks for the jol-compliance repository.
# Called by the compliance-lint.yml GitHub Actions workflow.
#
# CHECKS PERFORMED:
#   1. Ruff lint check (code style + pyflakes + isort + bugbear)
#   2. Bandit security scan (vulnerability detection)
#   3. compliance_validator.py (repository structure validation)
#
# COMPLIANCE CONTROLS:
#   SOC 2 CC8.1  — Change Management: Validates code quality before merge
#   ISO 27001 A.8.9 — Change Management: Automated validation gate
#   GDPR Art. 32  — Security: Security scanning of compliance tooling
#
# USAGE:
#   ./run-compliance-lint.sh             # Run checks, exit 1 on failure
#   ./run-compliance-lint.sh --dry-run   # Run checks, always exit 0
#
# IDEMPOTENT: Safe to run multiple times. Produces fresh report each run.
# Refs: SOC 2 CC8.1, ISO 27001 A.8.9, GDPR Art. 32
# =============================================================================

set -euo pipefail

# ---------------------------------------------------------------------------
# Argument Parsing
# ---------------------------------------------------------------------------
DRY_RUN=false
for arg in "$@"; do
    case "$arg" in
        --dry-run) DRY_RUN=true ;;
        --help|-h)
            echo "Usage: $0 [--dry-run]"
            echo ""
            echo "  --dry-run   Report issues without failing the build (exit 0)"
            echo "  --help      Show this help message"
            exit 0
            ;;
        *)
            echo "Unknown argument: $arg" >&2
            exit 1
            ;;
    esac
done

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
# Colors for output (suppressed when not a TTY)
if [ -t 1 ]; then
    RED='\033[0;31m'
    GREEN='\033[0;32m'
    YELLOW='\033[0;33m'
    BLUE='\033[0;34m'
    NC='\033[0m'
else
    RED=''
    GREEN=''
    YELLOW=''
    BLUE=''
    NC=''
fi

# Files to lint
LINT_TARGETS="compliance_validator.py main.py scripts/"

# Temporary files for output capture
TMPDIR=$(mktemp -d /tmp/compliance-lint-XXXXXX)
trap 'rm -rf "$TMPDIR"' EXIT

# Counters
ERRORS=0
PASSED=0
TOTAL_CHECKS=3

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
echo -e "${BLUE}======================================================================${NC}"
echo -e "${BLUE}  COMPLIANCE LINT CHECK${NC}"
echo -e "${BLUE}  Mode: $(if $DRY_RUN; then echo 'DRY-RUN (report only)'; else echo 'ENFORCED'; fi)${NC}"
echo -e "${BLUE}  Date: $(date -u +"%Y-%m-%dT%H:%M:%SZ")${NC}"
echo -e "${BLUE}  Refs: SOC 2 CC8.1, ISO 27001 A.8.9, GDPR Art. 32${NC}"
echo -e "${BLUE}======================================================================${NC}"
echo ""

# ---------------------------------------------------------------------------
# Check 1: Ruff Lint
# SOC 2 CC8.1: Code quality standards enforced before merge.
# ISO 27001 A.8.9: Change management requires linting gate.
# ---------------------------------------------------------------------------
echo -e "${BLUE}[1/${TOTAL_CHECKS}] Ruff Lint Check${NC}"
echo "  Target: $LINT_TARGETS"
echo "  Config: pyproject.toml [tool.ruff]"

if ruff check $LINT_TARGETS > "$TMPDIR/ruff-output.txt" 2>&1; then
    echo -e "  ${GREEN}PASS${NC} — No linting errors found"
    ((PASSED++)) || true
else
    RUFF_EXIT=$?
    RUFF_LINES=$(wc -l < "$TMPDIR/ruff-output.txt" || echo "0")
    echo -e "  ${RED}FAIL${NC} — $RUFF_LINES line(s) of output (exit code: $RUFF_EXIT)"
    # Show first 20 lines of output
    head -20 "$TMPDIR/ruff-output.txt" | sed 's/^/    /'
    if [ "$RUFF_LINES" -gt 20 ]; then
        echo "    ... ($((RUFF_LINES - 20)) more lines)"
    fi
    ((ERRORS++)) || true
fi
echo ""

# ---------------------------------------------------------------------------
# Check 2: Bandit Security Scan
# GDPR Art. 32: Security scanning of code handling personal data.
# ISO 27001 A.8.9: Vulnerability detection in compliance tooling.
# SOC 2 CC6.1: Code must not introduce security vulnerabilities.
# ---------------------------------------------------------------------------
echo -e "${BLUE}[2/${TOTAL_CHECKS}] Bandit Security Scan${NC}"
echo "  Target: $LINT_TARGETS"
echo "  Config: pyproject.toml [tool.bandit]"

if bandit -r $LINT_TARGETS -q > "$TMPDIR/bandit-output.txt" 2>&1; then
    echo -e "  ${GREEN}PASS${NC} — No security issues found"
    ((PASSED++)) || true
else
    BANDIT_EXIT=$?
    # Bandit exits with non-zero if issues found
    BANDIT_ISSUES=$(grep -c "Issue:" "$TMPDIR/bandit-output.txt" 2>/dev/null || echo "0")
    if [ "$BANDIT_ISSUES" -eq 0 ]; then
        # Might be a config error, not a security finding
        BANDIT_ISSUES=$(wc -l < "$TMPDIR/bandit-output.txt" || echo "0")
    fi
    echo -e "  ${RED}FAIL${NC} — $BANDIT_ISSUES issue(s) found (exit code: $BANDIT_EXIT)"
    head -20 "$TMPDIR/bandit-output.txt" | sed 's/^/    /'
    # Save bandit report for artifact upload
    cp "$TMPDIR/bandit-output.txt" bandit-report.txt 2>/dev/null || true
    ((ERRORS++)) || true
fi
echo ""

# ---------------------------------------------------------------------------
# Check 3: Compliance Validator (Repository Structure)
# SOC 2 CC8.1: Repository structure must meet compliance requirements.
# ISO 27001 A.8.9: Documentation completeness validation.
# ---------------------------------------------------------------------------
echo -e "${BLUE}[3/${TOTAL_CHECKS}] Repository Structure Validation${NC}"
echo "  Target: compliance_validator.py"
echo "  Validates: Required directories, files, and content checks"

if python compliance_validator.py > "$TMPDIR/validator-output.txt" 2>&1; then
    echo -e "  ${GREEN}PASS${NC} — Repository structure is compliant"
    ((PASSED++)) || true
else
    VALIDATOR_EXIT=$?
    VALIDATOR_ERRORS=$(grep -c "ERROR" "$TMPDIR/validator-output.txt" 2>/dev/null || echo "0")
    VALIDATOR_WARNINGS=$(grep -c "WARNING" "$TMPDIR/validator-output.txt" 2>/dev/null || echo "0")
    echo -e "  ${RED}FAIL${NC} — $VALIDATOR_ERRORS error(s), $VALIDATOR_WARNINGS warning(s) (exit: $VALIDATOR_EXIT)"
    # Show last 20 lines (validator outputs summary at the end)
    tail -20 "$TMPDIR/validator-output.txt" | sed 's/^/    /'
    ((ERRORS++)) || true
fi
echo ""

# ---------------------------------------------------------------------------
# Generate Report File (for artifact upload)
# SOC 2 CC8.1: Audit evidence must be retained.
# ---------------------------------------------------------------------------
{
    echo "Compliance Lint Report"
    echo "======================"
    echo "Date: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
    echo "Mode: $(if $DRY_RUN; then echo 'DRY-RUN'; else echo 'ENFORCED'; fi)"
    echo "Refs: SOC 2 CC8.1, ISO 27001 A.8.9, GDPR Art. 32"
    echo ""
    echo "--- Ruff Lint ---"
    cat "$TMPDIR/ruff-output.txt" 2>/dev/null || echo "(no output)"
    echo ""
    echo "--- Bandit Security Scan ---"
    cat "$TMPDIR/bandit-output.txt" 2>/dev/null || echo "(no output)"
    echo ""
    echo "--- Structure Validator ---"
    cat "$TMPDIR/validator-output.txt" 2>/dev/null || echo "(no output)"
} > compliance-lint-report.txt 2>/dev/null || true

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
echo -e "${BLUE}======================================================================${NC}"
echo -e "${BLUE}  SUMMARY${NC}"
echo -e "${BLUE}======================================================================${NC}"
echo "  Checks passed:  $PASSED/$TOTAL_CHECKS"
echo "  Checks failed:  $ERRORS/$TOTAL_CHECKS"
echo "  Mode:           $(if $DRY_RUN; then echo 'DRY-RUN'; else echo 'ENFORCED'; fi)"
echo "  Report:         compliance-lint-report.txt"
echo ""

# ---------------------------------------------------------------------------
# Exit Logic
# ---------------------------------------------------------------------------
if $DRY_RUN; then
    # SOC 2 CC8.1: Dry-run mode reports without blocking merges
    echo -e "${YELLOW}DRY-RUN: Reporting issues without failing the build.${NC}"
    if [ "$ERRORS" -gt 0 ]; then
        echo -e "${YELLOW}  $ERRORS check(s) would have failed in enforced mode.${NC}"
    else
        echo -e "${GREEN}  All checks would pass in enforced mode.${NC}"
    fi
    exit 0
else
    if [ "$ERRORS" -gt 0 ]; then
        echo -e "${RED}FAILED: $ERRORS compliance check(s) failed.${NC}"
        echo -e "${RED}  Review the output above and fix the issues.${NC}"
        echo -e "${RED}  Re-run with --dry-run for a non-blocking report.${NC}"
        exit 1
    else
        echo -e "${GREEN}PASSED: All $TOTAL_CHECKS compliance checks passed.${NC}"
        exit 0
    fi
fi

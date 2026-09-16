# Changelog

All notable changes to the JOL Compliance Repository are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to a compliance-document versioning scheme aligned with ISO 27001 Clause 7.5 (Documented Information).

---

## [Unreleased]

### Fixed — CI Workflow Repairs (R1 2026-09-16)
- `.github/workflows/compliance-validation.yml` — Removed `cache: 'pip'` from 3 jobs (`structure-validation`, `document-format`, `script-validation`) that don't run `pip install`. The `setup-python@v5` cache post-step fails fatally when no pip cache directory exists. Kept cache in `lint-and-security` which does `pip install -r requirements-dev.txt`.
- `.github/workflows/qodana.yml` — Disabled push/PR triggers (changed to `workflow_dispatch` only). `QODANA_TOKEN` declined by Qodana Cloud server (expired/revoked). Re-enable after token rotation. `compliance-lint.yml` (ruff + bandit) covers CI lint in the meantime.

### Planned
- Expansion of country-specific compliance documents to additional EU member states
- Integration of automated DSR tracking with production systems
- Board-approved compliance dashboard
- PCI DSS compliance documentation (if payment processing is brought in-house)

---

## [1.0.0] — [DATE]

### Added — GDPR Compliance Documents
- `gdpr/privacy-policies/lt/privacy-policy-lt.md` — Lithuania privacy policy (Art. 13–14)
- `gdpr/privacy-policies/lv/privacy-policy-lv.md` — Latvia privacy policy (Art. 13–14)
- `gdpr/privacy-policies/ee/privacy-policy-ee.md` — Estonia privacy policy (Art. 13–14)
- `gdpr/retention-policies/data-retention-policy.md` — Data retention and disposal policy (Art. 5(1)(e))
- `gdpr/cookie-policies/cookie-policy.md` — Cookie consent and management (ePrivacy Directive Art. 5(3))
- `gdpr/dsr-procedures/data-subject-rights-procedure.md` — Data subject rights procedure (Art. 15–22)
- `gdpr/ropa/ropa-template.md` — Records of Processing Activities template (Art. 30)
- `gdpr/dpias/dpia-template.md` — Data Protection Impact Assessment template (Art. 35)

### Added — ISO 27001:2022 ISMS Documents
- `iso27001/policies/information-security-policy.md` — ISMS information security policy (Clause 5.2)
- `iso27001/procedures/access-control-procedure.md` — Access control procedure (A.5.15)
- `iso27001/risk-register/risk-register-2026.md` — Risk register with 10 assessed risks (Clause 6.1.2)
- `iso27001/risk-register/risk-register-template.md` — Risk register template
- `iso27001/asset-register/asset-register.md` — Information asset inventory (A.5.9)
- `iso27001/soa/statement-of-applicability.md` — SoA covering all 93 Annex A controls (Clause 6.1.3 d)
- `iso27001/soa/soa-template.md` — Statement of Applicability template
- `iso27001/internal-audits/internal-audit-template.md` — Internal audit template (Clause 9.2)
- `iso27001/management-reviews/management-review-template.md` — Management review template (Clause 9.3)

### Added — SOC 2 Type II Documents
- `soc2/trust-services-criteria/tsc-control-mapping.md` — TSC to internal control mapping (CC1–CC9, A1, C1, P1)
- `soc2/evidence/cc6/access-control-evidence.md` — CC6 logical access evidence collection
- `soc2/evidence/cc6/access-control-evidence-template.md` — CC6 evidence template
- `soc2/evidence/cc7/system-operations-evidence.md` — CC7 system operations evidence
- `soc2/evidence/cc8/change-management-evidence.md` — CC8 change management evidence
- `soc2/evidence/a1/availability-evidence.md` — A1 availability evidence collection
- `soc2/access-reviews/quarterly-access-review-template.md` — Quarterly access review template
- `soc2/vendor-reviews/vendor-compliance-review-template.md` — Vendor compliance review template

### Added — Security Policies
- `security-policies/information-security-policy.md` — Organisational information security policy
- `security-policies/acceptable-use-policy.md` — Acceptable use of information assets (A.5.10)
- `security-policies/password-policy.md` — Password and authentication management (A.5.17)
- `security-policies/remote-work-security-policy.md` — Remote working security controls (A.6.7)
- `security-policies/incident-response-policy.md` — Incident response management (A.5.24)
- `security-policies/data-classification-policy.md` — Information classification scheme (A.5.12)
- `security-policies/encryption-policy.md` — Cryptography use policy (A.8.24)
- `security-policies/backup-and-recovery-policy.md` — Backup and disaster recovery (A.8.13)

### Added — Vendor Management
- `vendor-register/vendor-register-master.md` — Master vendor register with risk ratings
- `vendor-register/dpa-template.md` — Data Processing Agreement template (GDPR Art. 28)

### Added — Audit Evidence
- `audit-evidence/github/github-evidence-collection.md` — GitHub audit evidence guide
- `audit-evidence/infrastructure/infrastructure-evidence.md` — Infrastructure evidence collection
- `audit-evidence/penetration-tests/pen-test-report-template.md` — Penetration test report template
- `audit-evidence/vulnerability-scans/vulnerability-scan-template.md` — Vulnerability scan report template

### Added — Country-Specific Compliance
- `country/lt/lithuania-compliance-requirements.md` — Lithuania national compliance requirements
- `country/lv/latvia-compliance-requirements.md` — Latvia national compliance requirements
- `country/ee/estonia-compliance-requirements.md` — Estonia national compliance requirements

### Added — Guidance and Documentation
- `docs/compliance-checklist.md` — Comprehensive compliance checklist
- `docs/new-employee-compliance-guide.md` — New employee onboarding compliance guide
- `docs/audit-preparation-guide.md` — Audit preparation guide (ISO 27001, SOC 2, GDPR)
- `docs/incident-response-playbook.md` — Incident response playbook with specific playbooks

### Added — Automation Scripts
- `compliance_validator.py` — Repository structure and completeness validator (120 checks)
- `scripts/evidence_collector.py` — Automated evidence collection tool with manifest generation
- `scripts/retention_calculator.py` — Data retention period calculator with country overrides
- `scripts/vendor_risk_calculator.py` — Third-party vendor risk scoring and assessment
- `scripts/gdpr_dsr_tracker.py` — GDPR data subject rights request tracker

### Added — CI/CD Workflows
- `.github/workflows/compliance-validation.yml` — Automated compliance validation on push/PR
- `.github/workflows/evidence-collection.yml` — Monthly automated evidence collection
- `.github/workflows/vendor-review-reminder.yml` — Vendor review schedule reminders
- `.github/workflows/policy-review-scheduler.yml` — Policy review cycle tracking

### Added — Root Documents
- `COMPLIANCE_MATRIX.md` — Cross-framework compliance status matrix
- `CHANGELOG.md` — This file
- `GLOSSARY.md` — Compliance terminology glossary

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 1.0.0 | [DATE] | Initial compliance repository — GDPR, ISO 27001, SOC 2 frameworks |
| — | 2026-09-16 | R1: CI workflow repairs — fix pip cache failures in compliance-validation, disable broken qodana.yml |

---

## Document Control

- **Owner**: Chief Compliance Officer
- **Review Frequency**: Updated with every release; reviewed quarterly
- **Related**: `COMPLIANCE_MATRIX.md`, `docs/compliance-checklist.md`

---

*This document is the property of Journey Of Life UAB. It is classified as RESTRICTED. All changes to compliance documents must be recorded in this changelog per ISO 27001 Clause 7.5.*

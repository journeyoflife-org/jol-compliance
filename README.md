# jol-compliance

> **Classification:** RESTRICTED — Internal Use Only  
> **Owner:** Gintaras Kazlauskas · Journey Of Life UAB  
> **Repository:** `github.com/journeyoflife-org/jol-compliance` (Private)  
> **Visibility:** Private · No exceptions · Zero public exposure

[
[
[
[

***

## Purpose

This repository is the **single authoritative source** for all compliance, legal, privacy, and security governance documentation for the **Journey Of Life (JOL)** platform — a multi-tenant, multi-country digital platform serving ~400,000 religious institutions across 28 EU countries.

All documents in this repository are:

- **Version-controlled** — every change is tracked with a signed commit and a meaningful commit message
- **Auditable** — git history constitutes the change log for SOC 2, ISO 27001, and GDPR audit purposes
- **Separated from code** — legal and compliance documents must never be mixed with executable code repositories
- **GPG-signed** — all commits to `main` must be GPG or SSH signed

***

## ⚠️ Critical Rules

```
1. NEVER commit secrets, API keys, passwords, or credentials to this repository
2. NEVER make this repository public — not even temporarily
3. NEVER delete files — archive with an _ARCHIVED suffix and a dated commit
4. EVERY document update requires a signed commit with a clear message
5. EVERY DPIA must be reviewed before the related processing activity begins
6. EVERY third-party vendor handling PII must have a signed DPA before go-live
```

***

## Repository Structure

```
jol-compliance/
├── gdpr/                          GDPR compliance documentation
│   ├── ropa/                      Article 30 Records of Processing Activities
│   ├── dpias/                     Data Protection Impact Assessments (Art. 35)
│   ├── privacy-policies/          Privacy notices per country (LT/LV/EE/...)
│   │   ├── lt/                    Lithuanian privacy policy
│   │   ├── lv/                    Latvian privacy policy
│   └── └── ee/                    Estonian privacy policy
│   ├── retention-policies/        Data retention schedules per data category
│   ├── cookie-policies/           Cookie consent and ePrivacy policies
│   └── dsr-procedures/            Data Subject Rights request procedures
│
├── iso27001/                      ISO 27001:2022 ISMS documentation
│   ├── risk-register/             Information security risk register
│   ├── asset-register/            Information asset register
│   ├── soa/                       Statement of Applicability (Annex A)
│   ├── policies/                  ISMS policies
│   ├── procedures/                ISMS procedures
│   ├── internal-audits/           Internal audit records and findings
│   └── management-reviews/        Management review meeting minutes
│
├── soc2/                          SOC 2 Type II evidence and controls
│   ├── trust-services-criteria/   TSC control mapping
│   ├── evidence/                  Quarterly evidence artifacts
│   │   ├── cc6/                   Logical and physical access controls
│   │   ├── cc7/                   System operations evidence
│   │   ├── cc8/                   Change management evidence
│   │   └── a1/                    Availability evidence
│   ├── access-reviews/            Quarterly access review records
│   └── vendor-reviews/            Vendor compliance review records
│
├── security-policies/             All information security policies
│
├── vendor-register/               Third-party vendor and DPA register
│
├── audit-evidence/                Timestamped audit artifacts
│   ├── github/                    GitHub org screenshots, access lists
│   ├── infrastructure/            Infrastructure config snapshots
│   ├── penetration-tests/         Penetration test reports
│   └── vulnerability-scans/       Vulnerability scan results
│
├── country/                       Country-specific compliance
│   ├── lt/                        Lithuania: ADTA, LT-specific requirements
│   ├── lv/                        Latvia: DVI, LV-specific requirements
│   └── ee/                        Estonia: AKI, EE-specific requirements
│
└── docs/                          Guidance, checklists, and how-to documents
```

***

## Compliance Frameworks

| Framework | Status | Lead | Next Review |
|-----------|--------|------|-------------|
| GDPR (EU) 2016/679 | 🟡 In Progress | Gintaras Kazlauskas | 2026-10-01 |
| ISO 27001:2022 | 🟡 In Progress | Gintaras Kazlauskas | 2026-10-01 |
| SOC 2 Type II | 🟡 In Progress | Gintaras Kazlauskas | 2027-01-01 |
| ePrivacy Directive | 🟡 In Progress | Gintaras Kazlauskas | 2026-10-01 |
| NIS2 Directive | 🔴 Not Started | TBD | TBD |
| EU AI Act | 🔴 Not Started | TBD | TBD |
| PCI-DSS (payments) | 🔴 Not Started | TBD | TBD |

***

## Country Supervisory Authorities

| Country | Authority | Contact | Breach Notification |
|---------|-----------|---------|---------------------|
| Lithuania 🇱🇹 | ADTA (Valstybinė duomenų apsaugos inspekcija) | ada@ada.lt | 72 hours |
| Latvia 🇱🇻 | DVI (Datu valsts inspekcija) | info@dvi.gov.lv | 72 hours |
| Estonia 🇪🇪 | AKI (Andmekaitse Inspektsioon) | info@aki.ee | 72 hours |

***

## Key Contacts

| Role | Responsibility | Contact |
|------|---------------|---------|
| Controller / DPO | GDPR accountability, DPIA sign-off | journey4oflife@gmail.com |
| Platform Owner | Technical security controls | Gintaras Kazlauskas |
| Legal Counsel | Contract review, DPAs | [To be appointed] |
| External DPO (if appointed) | Independent oversight | [To be appointed] |

***

## Document Lifecycle

Every document in this repository follows this lifecycle:

```
DRAFT → REVIEW → APPROVED → ACTIVE → UNDER_REVIEW → REVISED or ARCHIVED
```

Commit message convention for compliance documents:

```
docs(gdpr): update LT privacy policy for cookie consent — v1.2
docs(iso27001): add risk R-042 to risk register — Q3 2026
docs(soc2): add CC6.1 quarterly access review evidence — 2026-Q3
feat(vendor): add DPA for Bitrix24 — effective 2026-07-09
fix(dpia): update jol-analytics-ai DPIA after scope change
```

***

## Branch Protection

| Branch | Policy |
|--------|--------|
| `main` | Protected — requires PR + review + signed commit |
| `develop` | Protected — integration branch |
| `review/*` | For documents under external review |

***

## Incident Response Quick Reference

| Event | Immediate Action | Deadline |
|-------|-----------------|----------|
| Personal data breach | Notify DPO → assess scope → notify supervisory authority | 72 hours from discovery |
| Security incident | Activate incident response plan in `security-policies/` | Immediate |
| DSR received | Log in `gdpr/dsr-procedures/` → assign → begin processing | Acknowledge within 48h; respond within 30 days |
| New vendor with PII access | Block deployment → execute DPA process | Before any PII data flows |

***

## Setup (First Clone)

```bash
# Clone
git clone git@github.com:journeyoflife-org/jol-compliance.git /opt/jol/repos/jol-compliance
cd /opt/jol/repos/jol-compliance

# Configure GPG signing (required for all commits)
git config commit.gpgsign true
git config tag.gpgsign true

# Verify
git config --list | grep gpg
```

***

*This repository is a controlled compliance artifact. Every commit is evidence. Treat every change as if an auditor is watching — because they will be.*

**Classification:** RESTRICTED · **Version:** 1.0.0 · **Created:** 2026-07-09 · **Owner:** journeyoflife-org

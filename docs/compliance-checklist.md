# Master Compliance Checklist

**Compliance Readiness Checklist for [Company Name] — Multi-Tenant SaaS Platform**

| Field | Value |
|-------|-------|
| **Organisation** | [Company Name] |
| **Platform** | [Platform Name] |
| **Checklist Owner** | [Compliance Officer / CISO Name] |
| **Version** | [Version Number] |
| **Effective Date** | [YYYY-MM-DD] |
| **Last Reviewed** | [YYYY-MM-DD] |
| **Review Frequency** | Quarterly |
| **Classification** | Internal — Confidential |

---

## How to Use This Checklist

- **Status:** ☐ Not started | ◐ In progress | ☑ Complete | N/A Not applicable
- **Evidence:** Link to the artefact or document that proves completion
- **Owner:** The role or person accountable for this item
- **Notes:** Any context, blockers, or exceptions

---

## 1. GDPR Compliance

### 1.1 Lawfulness, Fairness, and Transparency

| # | Requirement | Status | Evidence | Owner | Notes |
|---|------------|--------|----------|-------|-------|
| 1.1.1 | Record of Processing Activities (ROPA) maintained and current | ☐ | `gdpr/ropa/` | DPO | Updated per processing activity change |
| 1.1.2 | Privacy notices published for each country (LT, LV, EE, ...) | ☐ | `gdpr/privacy-policies/` | DPO / Legal | Localised per member state |
| 1.1.3 | Legal basis documented for each processing activity | ☐ | `gdpr/ropa/ropa-template.md` §1.2 | DPO | |
| 1.1.4 | Legitimate Interest Assessments (LIAs) completed where applicable | ☐ | [LIA documents] | DPO | |
| 1.1.5 | Consent mechanisms implemented and auditable | ☐ | [Consent management platform] | Engineering | |

### 1.2 Data Subject Rights

| # | Requirement | Status | Evidence | Owner | Notes |
|---|------------|--------|----------|-------|-------|
| 1.2.1 | Data Subject Rights (DSR) request procedure documented | ☐ | `gdpr/dsr-procedures/` | DPO | |
| 1.2.2 | DSR requests handled within 30-day SLA | ☐ | [DSR tracking system] | Operations | |
| 1.2.3 | Right to access (Art. 15) — self-service or manual process | ☐ | [Export mechanism] | Engineering | |
| 1.2.4 | Right to rectification (Art. 16) — editable profiles | ☐ | [User profile system] | Engineering | |
| 1.2.5 | Right to erasure (Art. 17) — deletion workflow | ☐ | [Deletion process] | Engineering | |
| 1.2.6 | Right to data portability (Art. 20) — export in machine-readable format | ☐ | [JSON/CSV export] | Engineering | |
| 1.2.7 | Right to restriction (Art. 18) and objection (Art. 21) | ☐ | [Flagging mechanism] | Engineering | |
| 1.2.8 | Automated decision-making safeguards (Art. 22) | ☐ | [Human review process] | DPO | |

### 1.3 Data Protection by Design and Default

| # | Requirement | Status | Evidence | Owner | Notes |
|---|------------|--------|----------|-------|-------|
| 1.3.1 | Data Protection Impact Assessment (DPIA) completed for high-risk processing | ☐ | `gdpr/dpias/` | DPO | |
| 1.3.2 | DPIA re-assessment triggered on material change | ☐ | [DPIA review log] | DPO | |
| 1.3.3 | Data minimisation applied — only necessary data collected | ☐ | ROPA data categories | DPO / Engineering | |
| 1.3.4 | Pseudonymisation/anonymisation applied where feasible | ☐ | [Technical documentation] | Engineering | |
| 1.3.5 | Children's data (Art. 8) — parental consent mechanisms | ☐ | [Consent flow] | Engineering / Legal | |

### 1.4 Data Transfers and Processors

| # | Requirement | Status | Evidence | Owner | Notes |
|---|------------|--------|----------|-------|-------|
| 1.4.1 | Data Processing Agreements (DPAs) in place with all processors (Art. 28) | ☐ | `vendor-register/` | Legal / DPO | |
| 1.4.2 | Sub-processor register maintained and communicated to controllers | ☐ | `vendor-register/` | DPO | 30-day notice for changes |
| 1.4.3 | International transfer safeguards (SCCs, BCRs, adequacy) | ☐ | ROPA §6 | DPO / Legal | |
| 1.4.4 | Transfer Impact Assessments (TIAs) completed for third countries | ☐ | [TIA documents] | DPO | Post-Schrems II |

### 1.5 Breach Notification and Accountability

| # | Requirement | Status | Evidence | Owner | Notes |
|---|------------|--------|----------|-------|-------|
| 1.5.1 | Data breach notification procedure (72-hour SLA to SA) | ☐ | `iso27001/procedures/incident-response.md` | DPO / CISO | |
| 1.5.2 | Breach register maintained (all breaches, regardless of notification) | ☐ | [Breach register] | DPO | |
| 1.5.3 | DPO appointed and contact details published (Art. 37–39) | ☐ | [DPO appointment letter] | Board | |
| 1.5.4 | EU representative appointed if required (Art. 27) | ☐ | [Representative agreement] | Legal | |

### 1.6 Retention and Disposal

| # | Requirement | Status | Evidence | Owner | Notes |
|---|------------|--------|----------|-------|-------|
| 1.6.1 | Data retention schedule documented per data category | ☐ | `gdpr/retention-policies/` | DPO | |
| 1.6.2 | Automated retention enforcement implemented | ☐ | [Retention automation] | Engineering | |
| 1.6.3 | Secure data disposal procedures (NIST 800-88) | ☐ | [Disposal procedure] | Operations | |

---

## 2. ISO 27001:2022 ISMS

### 2.1 ISMS Framework (Clauses 4–10)

| # | Requirement | Status | Evidence | Owner | Notes |
|---|------------|--------|----------|-------|-------|
| 2.1.1 | ISMS scope defined and documented | ☐ | ISMS scope document | ISMS Manager | |
| 2.1.2 | Information security policy approved by management | ☐ | `security-policies/information-security-policy.md` | CISO | |
| 2.1.3 | ISMS roles and responsibilities assigned | ☐ | [Role assignment matrix] | CISO | |
| 2.1.4 | Risk assessment methodology documented | ☐ | `iso27001/policies/risk-methodology.md` | ISMS Manager | |
| 2.1.5 | Risk register maintained and current | ☐ | `iso27001/risk-register/` | ISMS Manager | |
| 2.1.6 | Risk treatment plan defined for all unacceptable risks | ☐ | Risk register §3 | Risk owners | |
| 2.1.7 | Statement of Applicability (SoA) completed | ☐ | `iso27001/soa/` | ISMS Manager | All 93 controls assessed |
| 2.1.8 | Information security objectives defined and measurable | ☐ | ISP §3 | CISO | |
| 2.1.9 | Competence and training records maintained | ☐ | [Training records] | HR / ISMS Manager | |
| 2.1.10 | Internal audit programme defined and executed | ☐ | `iso27001/internal-audits/` | ISMS Manager | Annual minimum |
| 2.1.11 | Management review conducted at least annually | ☐ | `iso27001/management-reviews/` | Board / CISO | |
| 2.1.12 | Nonconformities and corrective actions tracked | ☐ | [Corrective action register] | ISMS Manager | |

### 2.2 Annex A Controls (Selected Key Controls)

| # | Control | Status | Evidence | Owner | Notes |
|---|---------|--------|----------|-------|-------|
| 2.2.1 | A.5.1 — Information security policies | ☐ | `security-policies/` | CISO | |
| 2.2.2 | A.5.9 — Asset inventory | ☐ | `iso27001/asset-register/` | System owners | |
| 2.2.3 | A.5.15 — Access control | ☐ | `soc2/evidence/cc6/` | CISO | |
| 2.2.4 | A.5.23 — Cloud services security | ☐ | [Cloud security config] | Engineering | |
| 2.2.5 | A.5.24–A.5.28 — Incident management | ☐ | `iso27001/procedures/` | CISO | |
| 2.2.6 | A.5.34 — Privacy and PII protection | ☐ | `gdpr/` | DPO | |
| 2.2.7 | A.7.1–A.7.14 — Physical security | ☐ | [Provider SOC 2 report] | Operations | Via hosting provider |
| 2.2.8 | A.8.13 — Information backup | ☐ | `soc2/evidence/cc7/` | Engineering | |
| 2.2.9 | A.8.15–A.8.16 — Logging and monitoring | ☐ | [Monitoring dashboard] | Security Operations | |
| 2.2.10 | A.8.24 — Cryptography | ☐ | [Encryption config] | Engineering | |
| 2.2.11 | A.8.25–A.8.30 — Secure development | ☐ | `soc2/evidence/cc8/` | Engineering | |
| 2.2.12 | A.8.32 — Change management | ☐ | `soc2/evidence/cc8/` | Engineering | |

---

## 3. SOC 2 Type II

### 3.1 Trust Services Criteria — Common Criteria

| # | Criterion | Status | Evidence | Owner | Notes |
|---|----------|--------|----------|-------|-------|
| 3.1.1 | CC1 — Control Environment (governance, ethics, HR) | ☐ | `security-policies/`, HR records | CISO / HR | |
| 3.1.2 | CC2 — Communication and Information (data quality, flows) | ☐ | Architecture docs, data flow diagrams | Engineering | |
| 3.1.3 | CC3 — Risk Assessment (fraud risk, change risk) | ☐ | `iso27001/risk-register/` | CISO | |
| 3.1.4 | CC4 — Monitoring Activities (ongoing and separate evaluations) | ☐ | Internal audit records, monitoring dashboards | ISMS Manager | |
| 3.1.5 | CC5 — Control Activities (selection, development, deployment) | ☐ | Policies, procedures, SoA | CISO | |
| 3.1.6 | CC6 — Logical and Physical Access Controls | ☐ | `soc2/evidence/cc6/` | CISO | See §4 below |
| 3.1.7 | CC7 — System Operations (monitoring, incident response) | ☐ | `soc2/evidence/cc7/` | Security Operations | |
| 3.1.8 | CC8 — Change Management | ☐ | `soc2/evidence/cc8/` | Engineering | |
| 3.1.9 | CC9 — Risk Mitigation (outsourcing, business continuity) | ☐ | `vendor-register/`, BCP/DR plans | CISO | |

### 3.2 Additional TSC (If Applicable)

| # | Criterion | Status | Evidence | Owner | Notes |
|---|----------|--------|----------|-------|-------|
| 3.2.1 | A1 — Availability (uptime, DR, capacity) | ☐ | `soc2/evidence/a1/` | Engineering / Ops | |
| 3.2.2 | C1 — Confidentiality (data classification, encryption) | ☐ | ISP §7, encryption configs | CISO | |
| 3.2.3 | P1 — Privacy (notice, consent, DSR, retention) | ☐ | `gdpr/` | DPO | |

### 3.3 SOC 2 Audit Readiness

| # | Requirement | Status | Evidence | Owner | Notes |
|---|------------|--------|----------|-------|-------|
| 3.3.1 | System description documented | ☐ | [System description doc] | Engineering | |
| 3.3.2 | Evidence collected for full audit period | ☐ | `soc2/evidence/` | Compliance | Quarterly collection |
| 3.3.3 | Access reviews completed quarterly | ☐ | `soc2/access-reviews/` | CISO | |
| 3.3.4 | Vendor reviews completed annually | ☐ | `soc2/vendor-reviews/` | Compliance | |
| 3.3.5 | Prior audit findings remediated | ☐ | [Remediation evidence] | CISO | |
| 3.3.6 | Management assertion letter prepared | ☐ | [Assertion letter] | CISO / CFO | |

---

## 4. Multi-Tenant Platform Specific

| # | Requirement | Status | Evidence | Owner | Notes |
|---|------------|--------|----------|-------|-------|
| 4.1 | Tenant data isolation verified (penetration test + architecture review) | ☐ | `audit-evidence/penetration-tests/` | Engineering / CISO | |
| 4.2 | Tenant admin access controls (per-institution RBAC) | ☐ | [RBAC configuration] | Engineering | |
| 4.3 | Tenant data export and deletion capabilities | ☐ | [Export/delete mechanism] | Engineering | |
| 4.4 | Tenant-specific privacy notice support | ☐ | `gdpr/privacy-policies/` | DPO | Per-country templates |
| 4.5 | Tenant controller-processor agreements (DPAs) | ☐ | `vendor-register/` | Legal | |
| 4.6 | Scalability validated for 400,000 institutions | ☐ | [Load test reports] | Engineering | |

---

## 5. Country-Specific Compliance

### 5.1 Lithuania (LT)

| # | Requirement | Status | Evidence | Owner | Notes |
|---|------------|--------|----------|-------|-------|
| 5.1.1 | Registered with Valstybinė duomenų apsaugos inspekcija (VDAI) | ☐ | [Registration confirmation] | Legal | |
| 5.1.2 | LT-specific privacy notice published | ☐ | `gdpr/privacy-policies/lt/` | DPO | |
| 5.1.3 | ADTA (Lithuanian data protection law) requirements met | ☐ | `country/lt/` | Legal | |

### 5.2 Latvia (LV)

| # | Requirement | Status | Evidence | Owner | Notes |
|---|------------|--------|----------|-------|-------|
| 5.2.1 | Registered with Datu valsts inspekcija (DVI) | ☐ | [Registration confirmation] | Legal | |
| 5.2.2 | LV-specific privacy notice published | ☐ | `gdpr/privacy-policies/lv/` | DPO | |
| 5.2.3 | LV-specific requirements documented | ☐ | `country/lv/` | Legal | |

### 5.3 Estonia (EE)

| # | Requirement | Status | Evidence | Owner | Notes |
|---|------------|--------|----------|-------|-------|
| 5.3.1 | Registered with Andmekaitse Inspektsioon (AKI) | ☐ | [Registration confirmation] | Legal | |
| 5.3.2 | EE-specific privacy notice published | ☐ | `gdpr/privacy-policies/ee/` | DPO | |
| 5.3.3 | EE-specific requirements documented | ☐ | `country/ee/` | Legal | |

### 5.4 Other EU Member States

| # | Requirement | Status | Evidence | Owner | Notes |
|---|------------|--------|----------|-------|-------|
| 5.4.1 | Supervisory authority mapping for all 28 EU countries | ☐ | [SA contact register] | DPO / Legal | |
| 5.4.2 | Privacy notices localised per active country | ☐ | `gdpr/privacy-policies/` | DPO | |
| 5.4.3 | Country-specific legal requirements documented | ☐ | `country/` | Legal | |

---

## 6. Audit Evidence and Artefacts

| # | Requirement | Status | Evidence | Owner | Notes |
|---|------------|--------|----------|-------|-------|
| 6.1 | GitHub org access lists and screenshots current | ☐ | `audit-evidence/github/` | Security Operations | Quarterly |
| 6.2 | Infrastructure config snapshots retained | ☐ | `audit-evidence/infrastructure/` | Engineering | Quarterly |
| 6.3 | Penetration test reports on file (annual external) | ☐ | `audit-evidence/penetration-tests/` | CISO | Annual |
| 6.4 | Vulnerability scan results retained | ☐ | `audit-evidence/vulnerability-scans/` | Security Operations | Weekly |
| 6.5 | All audit artefacts timestamped and version-controlled | ☐ | Git commit history | All | |

---

## 7. Governance and Review Cadence

| Activity | Frequency | Last Completed | Next Due | Owner |
|----------|-----------|---------------|----------|-------|
| ROPA review | Per change | [Date] | [Date] | DPO |
| DPIA review | Annual + per change | [Date] | [Date] | DPO |
| Risk assessment | Annual + per change | [Date] | [Date] | ISMS Manager |
| Access review | Quarterly | [Date] | [Date] | CISO |
| Vendor review | Annual | [Date] | [Date] | Compliance |
| Internal audit | Annual | [Date] | [Date] | ISMS Manager |
| Management review | Annual | [Date] | [Date] | Board / CISO |
| Penetration test | Annual | [Date] | [Date] | CISO |
| Security training | Annual | [Date] | [Date] | HR / ISMS Manager |
| Compliance checklist review | Quarterly | [Date] | [Date] | Compliance Officer |
| Privacy notice update | Per change | [Date] | [Date] | DPO |
| Incident response test | Biannual | [Date] | [Date] | CISO |

---

## 8. Compliance Scorecard

| Domain | Total Items | Complete | In Progress | Not Started | N/A | Completion % |
|--------|------------|----------|-------------|-------------|-----|-------------|
| GDPR | [N] | [N] | [N] | [N] | [N] | [X%] |
| ISO 27001 | [N] | [N] | [N] | [N] | [N] | [X%] |
| SOC 2 | [N] | [N] | [N] | [N] | [N] | [X%] |
| Multi-Tenant | [N] | [N] | [N] | [N] | [N] | [X%] |
| Country-Specific | [N] | [N] | [N] | [N] | [N] | [X%] |
| Audit Evidence | [N] | [N] | [N] | [N] | [N] | [X%] |
| **Overall** | **[N]** | **[N]** | **[N]** | **[N]** | **[N]** | **[X%]** |

---

*This checklist provides a comprehensive view of compliance readiness for a multi-tenant SaaS platform serving religious institutions across 28 EU member states. It should be reviewed quarterly and updated to reflect regulatory changes, audit findings, and organisational changes. All checklist items should be supported by referenced evidence artefacts stored in the corresponding repository directories.*

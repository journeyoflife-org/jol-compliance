# Data Protection Impact Assessment (DPIA)

**GDPR Article 35 — Data Protection Impact Assessment**

| Field | Value |
|-------|-------|
| **Organisation** | [Company Name] |
| **Project / System Name** | [Project Name] |
| **DPIA Reference** | DPIA-[YYYY]-[NNN] |
| **Data Protection Officer** | [DPO Name] — [DPO Email] |
| **DPIA Lead** | [Assessor Name] — [Assessor Role] |
| **Document Owner** | [Document Owner Name/Role] |
| **Version** | [Version Number] |
| **Initiated Date** | [YYYY-MM-DD] |
| **Completed Date** | [YYYY-MM-DD] |
| **Status** | ☐ Draft ☐ Under Review ☐ Approved ☐ Re-assessment |
| **Classification** | Internal — Confidential |

---

## 1. Screening: Is a DPIA Required?

Answer each question. If **any** answer is "Yes," a full DPIA is mandatory.

| # | Screening Question | Yes | No | Notes |
|---|-------------------|-----|-----|-------|
| 1 | Does the processing involve special category data (Art. 9) — e.g., religious affiliation, health, children's data? | ☐ | ☐ | |
| 2 | Is the processing carried out on a large scale (≥400,000 data subjects)? | ☐ | ☐ | |
| 3 | Does it involve systematic monitoring of publicly accessible areas? | ☐ | ☐ | |
| 4 | Does it involve automated decision-making with legal or similarly significant effects? | ☐ | ☐ | |
| 5 | Does it involve processing of vulnerable data subjects (children, elderly, congregants in pastoral care)? | ☐ | ☐ | |
| 6 | Does it involve new technologies or innovative use of existing technologies (AI/ML, biometrics)? | ☐ | ☐ | |
| 7 | Does it involve matching or combining datasets from multiple sources? | ☐ | ☐ | |
| 8 | Does it involve systematic evaluation or scoring of individuals? | ☐ | ☐ | |
| 9 | Does it involve transfers of personal data outside the EU? | ☐ | ☐ | |
| 10 | Does the supervisory authority's "must-DPIA" list require one for this type of processing? | ☐ | ☐ | |

**Screening Result:** ☐ DPIA Required ☐ DPIA Not Required (document justification below)

**Justification if not required:** [Provide reasoning]

---

## 2. Description of Processing

### 2.1 Nature of Processing

| Aspect | Description |
|--------|-------------|
| **Processing Operations** | [e.g. Collection, storage, analysis, sharing, deletion of member data] |
| **Technologies Used** | [e.g. Multi-tenant SaaS platform, PostgreSQL, AWS EU-West] |
| **Data Flow** | [Describe end-to-end data lifecycle from collection to deletion] |

### 2.2 Scope of Processing

| Aspect | Description |
|--------|-------------|
| **Geographic Scope** | [e.g. 28 EU member states — LT, LV, EE, PL, DE, FR, ...] |
| **Data Subject Volume** | [e.g. ~400,000 institutions × avg. N members per institution] |
| **Data Categories** | [Reference ROPA data category codes DC-01 through DC-XX] |
| **Processing Frequency** | [e.g. Continuous / batch / one-time] |

### 2.3 Context of Processing

| Aspect | Description |
|--------|-------------|
| **Data Subject Relationship** | [e.g. Members of religious institutions using the platform voluntarily] |
| **Data Subject Expectations** | [e.g. Expect confidential handling of parish membership and pastoral data] |
| **Vulnerable Populations** | [e.g. Children in religious education, elderly congregants] |

### 2.4 Purpose of Processing

| Purpose | Description | Legal Basis |
|---------|-------------|-------------|
| [e.g. Member directory] | [e.g. Enable institutions to manage their congregation records] | [Art. 6(1)(b)] |
| | | |

---

## 3. Necessity and Proportionality Assessment

### 3.1 Lawfulness, Fairness, and Transparency

| Criterion | Assessment | Compliant |
|-----------|-----------|-----------|
| **Legal basis identified for each purpose** | [Describe basis per processing activity] | ☐ Yes ☐ Partial ☐ No |
| **Privacy notice provided** | [Reference privacy notice document/link] | ☐ Yes ☐ Partial ☐ No |
| **Purpose limitation respected** | [Confirm data is not repurposed beyond stated purposes] | ☐ Yes ☐ Partial ☐ No |

### 3.2 Data Minimisation

| Criterion | Assessment | Compliant |
|-----------|-----------|-----------|
| **Only necessary data collected** | [Justify each data category is essential for the stated purpose] | ☐ Yes ☐ Partial ☐ No |
| **Retention periods defined** | [Reference retention schedule] | ☐ Yes ☐ Partial ☐ No |
| **Anonymisation/pseudonymisation considered** | [Describe if applicable] | ☐ Yes ☐ Partial ☐ No |

### 3.3 Data Subject Rights

| Right | Mechanism | SLA | Compliant |
|-------|-----------|-----|-----------|
| Access (Art. 15) | [e.g. Self-service portal + DPO email] | 30 days | ☐ Yes |
| Rectification (Art. 16) | [e.g. User profile edit + support ticket] | 30 days | ☐ Yes |
| Erasure (Art. 17) | [e.g. Account deletion workflow] | 30 days | ☐ Yes |
| Restriction (Art. 18) | [e.g. Data flagging mechanism] | 30 days | ☐ Yes |
| Portability (Art. 20) | [e.g. JSON/CSV export] | 30 days | ☐ Yes |
| Objection (Art. 21) | [e.g. Opt-out mechanism for marketing] | 30 days | ☐ Yes |
| Automated decisions (Art. 22) | [e.g. Human review process] | 30 days | ☐ Yes |

> **Cross-reference:** See `gdpr/dsr-procedures/` for full Data Subject Rights handling procedures.

---

## 4. Risk Assessment

### 4.1 Risk Identification

For each identified risk, assess **likelihood** and **severity** on a 1–5 scale.

**Likelihood Scale:** 1 = Very Low | 2 = Low | 3 = Medium | 4 = High | 5 = Very High
**Severity Scale:** 1 = Negligible | 2 = Minor | 3 = Moderate | 4 = Significant | 5 = Severe

| Risk ID | Risk Description | Source / Threat | Data Categories Affected | Likelihood (1–5) | Severity (1–5) | Risk Score (L×S) | Risk Level |
|---------|-----------------|-----------------|-------------------------|-------------------|-----------------|-------------------|------------|
| R-001 | [e.g. Unauthorised access to religious affiliation data] | [e.g. Credential theft, insider threat] | DC-04, DC-06 | | | | ☐ Low ☐ Med ☐ High ☐ Critical |
| R-002 | [e.g. Data breach exposing children's records] | [e.g. SQL injection, misconfiguration] | DC-07 | | | | |
| R-003 | [e.g. Cross-tenant data leakage] | [e.g. Multi-tenancy isolation failure] | All | | | | |
| R-004 | [e.g. Unlawful international transfer] | [e.g. Sub-processor in non-adequate country] | All | | | | |
| R-005 | | | | | | | |

**Risk Level Matrix:**

| | Severity 1 | Severity 2 | Severity 3 | Severity 4 | Severity 5 |
|--|-----------|-----------|-----------|-----------|-----------|
| **Likelihood 5** | Medium | Medium | High | High | Critical |
| **Likelihood 4** | Medium | Medium | High | High | Critical |
| **Likelihood 3** | Low | Medium | Medium | High | High |
| **Likelihood 2** | Low | Low | Medium | Medium | High |
| **Likelihood 1** | Low | Low | Low | Medium | Medium |

### 4.2 Risk Treatment Plan

| Risk ID | Risk Level | Treatment | Mitigation Measure | Residual Likelihood | Residual Severity | Residual Risk | Owner | Target Date |
|---------|-----------|-----------|-------------------|--------------------|--------------------|---------------|-------|-------------|
| R-001 | | ☐ Mitigate ☐ Transfer ☐ Accept ☐ Avoid | [e.g. Encrypt DC-04/DC-06 at field level, enforce MFA] | | | | [Role] | [Date] |
| R-002 | | | [e.g. WAF, input validation, penetration testing] | | | | | |
| R-003 | | | [e.g. Tenant isolation via schema-level separation, row-level security] | | | | | |
| R-004 | | | [e.g. SCCs, EU-only data residency, transfer impact assessment] | | | | | |

---

## 5. Measures Envisaged

### 5.1 Technical Measures

| Measure | Description | Addresses Risk | Status |
|---------|-------------|----------------|--------|
| Encryption at rest | AES-256 encryption for all stored personal data | R-001, R-002 | ☐ Implemented ☐ Planned |
| Encryption in transit | TLS 1.3 for all API and web traffic | R-001 | |
| Field-level encryption | Application-level encryption for special category data | R-001 | |
| Tenant isolation | Schema-level or row-level security in multi-tenant DB | R-003 | |
| Access controls | RBAC with least-privilege; MFA enforced | R-001 | |
| Audit logging | Immutable audit trail for all data access | R-001, R-003 | |
| Vulnerability scanning | Weekly automated scans + quarterly penetration tests | R-002 | |
| Backup & DR | Encrypted backups, tested recovery procedures | R-002 | |

### 5.2 Organisational Measures

| Measure | Description | Addresses Risk | Status |
|---------|-------------|----------------|--------|
| DPO oversight | DPO reviews all new processing activities | All | ☐ Implemented ☐ Planned |
| Staff training | Annual GDPR + security awareness training | R-001 | |
| DPA with processors | Art. 28-compliant DPAs with all sub-processors | R-004 | |
| Incident response plan | Documented and tested within 72-hour notification SLA | R-001, R-002 | |
| Privacy by design | Privacy review gate in SDLC | All | |
| Vendor due diligence | Annual security assessment of all sub-processors | R-004 | |

---

## 6. Consultation with Supervisory Authority

**Is prior consultation required (Art. 36)?**

- [ ] **No** — Residual risk after mitigation is acceptable (document rationale below)
- [ ] **Yes** — High residual risk remains; prior consultation with [Supervisory Authority Name] required

**Rationale:** [Explain why residual risk is or is not acceptable]

**If consultation is required:**

| Field | Value |
|-------|-------|
| Authority consulted | [e.g. VDAI (LT), DVI (LV), AKI (EE)] |
| Date of consultation | [YYYY-MM-DD] |
| Reference number | [Authority reference] |
| Authority response | [Summary of guidance received] |
| Actions taken | [Describe how guidance was implemented] |

---

## 7. DPO Opinion

| Field | Value |
|-------|-------|
| **DPO Name** | [DPO Name] |
| **Date** | [YYYY-MM-DD] |
| **Opinion** | ☐ Approve ☐ Approve with conditions ☐ Do not proceed |
| **Conditions (if any)** | [List any conditions for approval] |
| **Signature** | _________________________ |

---

## 8. Approval & Sign-Off

| Role | Name | Date | Signature |
|------|------|------|-----------|
| DPIA Lead | [Name] | [Date] | _________________ |
| Data Protection Officer | [DPO Name] | [Date] | _________________ |
| Chief Information Security Officer | [CISO Name] | [Date] | _________________ |
| Executive Sponsor | [Name] | [Date] | _________________ |

---

## 9. Review Schedule

| Review # | Date | Trigger | Reviewer | Outcome | Next Review |
|----------|------|---------|----------|---------|-------------|
| 1 | [YYYY-MM-DD] | [e.g. Annual review / material change / incident] | [Name] | [Summary] | [YYYY-MM-DD] |
| 2 | | | | | |

---

## Appendix A: DPIA Process Flow

1. **Screening** → Determine if DPIA is required (Section 1)
2. **Description** → Document the processing activity (Section 2)
3. **Necessity** → Assess lawfulness, minimisation, and rights (Section 3)
4. **Risk Assessment** → Identify and score risks (Section 4.1)
5. **Risk Treatment** → Define and implement mitigations (Section 4.2)
6. **Measures** → Document technical and organisational measures (Section 5)
7. **Consultation** → Determine if supervisory authority consultation is needed (Section 6)
8. **Approval** → Obtain DPO opinion and executive sign-off (Sections 7–8)
9. **Monitor** → Review on schedule or upon material change (Section 9)

---

*This DPIA template is designed for a multi-tenant SaaS platform processing personal data — including special category data — of approximately 400,000 religious institutions across 28 EU member states. Legal review is recommended before adoption.*

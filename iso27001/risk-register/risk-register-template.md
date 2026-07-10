# Information Security Risk Register

**ISO/IEC 27001:2022 — Clause 6.1.2 Information Security Risk Assessment**

| Field | Value |
|-------|-------|
| **Organisation** | [Company Name] |
| **ISMS Scope** | [Define ISMS scope — e.g. "Multi-tenant SaaS platform serving religious institutions across 28 EU member states"] |
| **Risk Register Owner** | [CISO / Risk Manager Name] |
| **Methodology Reference** | [Reference to risk methodology document — e.g. "ISMS-RM-001"] |
| **Version** | [Version Number] |
| **Effective Date** | [YYYY-MM-DD] |
| **Last Reviewed** | [YYYY-MM-DD] |
| **Next Review Due** | [YYYY-MM-DD] |
| **Classification** | Internal — Confidential |

---

## 1. Risk Assessment Methodology

### 1.1 Risk Criteria

**Risk Acceptance Criteria:** Risks scored ≤ [X] after treatment are acceptable. All risks above this threshold require a documented treatment plan.

**Risk Assessment Scale:**

| Score | Likelihood | Impact (CIA) |
|-------|-----------|--------------|
| 1 | Rare (once in 10+ years) | Negligible — no material effect |
| 2 | Unlikely (once in 5 years) | Minor — limited operational disruption |
| 3 | Possible (once per year) | Moderate — significant disruption, limited financial loss |
| 4 | Likely (quarterly) | Major — prolonged disruption, regulatory action, financial loss |
| 5 | Almost certain (monthly or more) | Severe — existential threat, major regulatory penalty, data breach |

**Risk Score Calculation:** Risk Score = Likelihood × Impact

**Risk Level Matrix:**

| | Impact 1 | Impact 2 | Impact 3 | Impact 4 | Impact 5 |
|--|---------|---------|---------|---------|---------|
| **Likelihood 5** | Medium (5) | Medium (10) | High (15) | High (20) | Critical (25) |
| **Likelihood 4** | Medium (4) | Medium (8) | High (12) | High (16) | Critical (20) |
| **Likelihood 3** | Low (3) | Medium (6) | Medium (9) | High (12) | High (15) |
| **Likelihood 2** | Low (2) | Low (4) | Medium (6) | Medium (8) | High (10) |
| **Likelihood 1** | Low (1) | Low (2) | Low (3) | Medium (4) | Medium (5) |

| Risk Level | Score Range | Action Required |
|-----------|------------|-----------------|
| Low | 1–4 | Monitor; accept or treat at next review |
| Medium | 5–9 | Treatment plan required within 90 days |
| High | 10–15 | Treatment plan required within 30 days |
| Critical | 16–25 | Immediate treatment; escalate to management |

### 1.2 CIA Impact Assessment

For each risk, assess impact across three dimensions:

| Dimension | Description |
|-----------|-------------|
| **Confidentiality** | Unauthorised disclosure of information |
| **Integrity** | Unauthorised modification or destruction of information |
| **Availability** | Loss of access to information or information systems |

---

## 2. Risk Register

### 2.1 Identified Risks

| Risk ID | Category | Asset | Threat | Vulnerability | Existing Controls | L | I | Score | Level | CIA Impact | Risk Owner |
|---------|----------|-------|--------|---------------|-------------------|---|---|-------|-------|-----------|------------|
| IR-001 | Access Control | [e.g. Tenant database] | [e.g. Unauthorised access] | [e.g. Weak authentication] | [e.g. MFA, RBAC] | | | | | C: ☐ I: ☐ A: ☐ | [Role] |
| IR-002 | Data Protection | [e.g. Special category data] | [e.g. Data breach] | [e.g. Insufficient encryption] | [e.g. AES-256, TLS 1.3] | | | | | | |
| IR-003 | Multi-Tenancy | [e.g. Shared infrastructure] | [e.g. Cross-tenant data leakage] | [e.g. Isolation failure] | [e.g. Schema separation, row-level security] | | | | | | |
| IR-004 | Supply Chain | [e.g. Sub-processor services] | [e.g. Vendor compromise] | [e.g. Insufficient vendor oversight] | [e.g. Vendor reviews, DPAs] | | | | | | |
| IR-005 | Availability | [e.g. Platform uptime] | [e.g. DDoS attack] | [e.g. Single point of failure] | [e.g. CDN, auto-scaling, DR plan] | | | | | | |
| IR-006 | Compliance | [e.g. GDPR obligations] | [e.g. Regulatory fine] | [e.g. Incomplete ROPA] | [e.g. DPO oversight, DPIA process] | | | | | | |
| IR-007 | Personnel | [e.g. Privileged accounts] | [e.g. Insider threat] | [e.g. Excessive privileges] | [e.g. Least-privilege, SoD, access reviews] | | | | | | |
| IR-008 | Change Mgmt | [e.g. Production systems] | [e.g. Unauthorised change] | [e.g. Insufficient change control] | [e.g. Change approval, CI/CD gates] | | | | | | |
| IR-009 | Physical | [e.g. Data centre] | [e.g. Physical intrusion] | [e.g. Inadequate physical security] | [e.g. SOC 2 certified facilities] | | | | | | |
| IR-010 | Incident Mgmt | [e.g. Security incidents] | [e.g. Delayed breach notification] | [e.g. No incident response plan] | [e.g. IR plan, 72h notification SLA] | | | | | | |

---

## 3. Risk Treatment Plan

### 3.1 Treatment Options

| Option | Description |
|--------|-------------|
| **Mitigate** | Implement controls to reduce likelihood or impact |
| **Transfer** | Share risk with a third party (e.g. insurance, outsourcing) |
| **Accept** | Acknowledge and accept the risk (requires risk owner approval) |
| **Avoid** | Discontinue the activity that gives rise to the risk |

### 3.2 Treatment Register

| Risk ID | Residual Score | Treatment Option | Treatment Action | ISO 27001 Annex A Control | Implementation Owner | Target Date | Status | Post-Treatment Score | Accepted By |
|---------|---------------|-----------------|-----------------|--------------------------|--------------------|-------------|--------|---------------------|-------------|
| IR-001 | | ☐ Mitigate ☐ Transfer ☐ Accept ☐ Avoid | [e.g. Implement MFA for all admin access] | [e.g. A.5.15 Access control] | [Role] | [Date] | ☐ Planned ☐ In Progress ☐ Complete | | [Name/Role] |
| IR-002 | | | [e.g. Deploy field-level encryption for Art. 9 data] | [e.g. A.8.24 Use of cryptography] | | | | | |
| IR-003 | | | [e.g. Implement tenant isolation testing] | [e.g. A.8.13 Information backup — A.5.35 Independent review] | | | | | |
| IR-004 | | | [e.g. Annual vendor security assessments] | [e.g. A.5.19–A.5.22 Supplier relationships] | | | | | |
| IR-005 | | | [e.g. Deploy DDoS mitigation service] | [e.g. A.8.14 Redundancy of information processing] | | | | | |

---

## 4. Risk Acceptance Register

| Risk ID | Residual Score | Justification for Acceptance | Accepted By | Date | Review Date |
|---------|---------------|----------------------------|-------------|------|-------------|
| | | [Document why the residual risk is acceptable] | [Name/Role] | [Date] | [Date] |
| | | | | | |

---

## 5. Emerging Risks & Watch List

| Risk ID | Description | Category | Monitoring Approach | Next Assessment |
|---------|------------|----------|--------------------|----------------|
| EM-001 | [e.g. AI-generated phishing targeting clergy] | Social Engineering | [e.g. Monitor threat intel feeds] | [Date] |
| EM-002 | [e.g. Quantum computing impact on encryption] | Cryptography | [e.g. Track NIST PQC standardisation] | [Date] |
| EM-003 | [e.g. New EU member state data localisation laws] | Regulatory | [e.g. Monitor regulatory updates] | [Date] |

---

## 6. Risk Review Log

| Review # | Date | Reviewer | Trigger | Risks Added | Risks Closed | Score Changes | Actions |
|----------|------|----------|---------|-------------|-------------|---------------|---------|
| 1 | [YYYY-MM-DD] | [Name] | ☐ Scheduled ☐ Incident ☐ Change ☐ Audit | [Count] | [Count] | [Summary] | [Summary] |
| 2 | | | | | | | |

---

## 7. Risk Dashboard Summary

| Metric | Value |
|--------|-------|
| Total identified risks | [N] |
| Critical risks | [N] |
| High risks | [N] |
| Medium risks | [N] |
| Low risks | [N] |
| Risks with overdue treatment | [N] |
| Risks accepted | [N] |
| Average residual risk score | [X.X] |
| Risk trend (vs. last quarter) | ☐ Improving ☐ Stable ☐ Deteriorating |

---

## 8. Approval & Governance

| Role | Name | Responsibility |
|------|------|---------------|
| Risk Owner (CISO) | [Name] | Overall risk management and treatment decisions |
| ISMS Manager | [Name] | Risk assessment execution and register maintenance |
| DPO | [DPO Name] | GDPR-related risk consultation and DPIA coordination |
| Management Review Board | [Names] | Risk acceptance approval for High/Critical risks |

---

## 9. Cross-References

| Document | Location | Description |
|----------|----------|-------------|
| Risk Methodology | `iso27001/policies/risk-methodology.md` | Detailed risk assessment methodology |
| Statement of Applicability | `iso27001/soa/soa-template.md` | Annex A control applicability mapping |
| ISMS Policies | `iso27001/policies/` | Information security policies |
| GDPR DPIA | `gdpr/dpias/dpia-template.md` | Data Protection Impact Assessments |
| SOC 2 Evidence | `soc2/evidence/` | Control evidence for SOC 2 Type II |

---

*This risk register template aligns with ISO/IEC 27001:2022 Clause 6.1.2 and is tailored for a multi-tenant SaaS platform serving ~400,000 religious institutions across 28 EU member states. Review and customise the risk criteria, scoring, and acceptance thresholds to match your organisation's risk appetite.*

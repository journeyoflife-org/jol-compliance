# Audit Preparation Guide

## Document Information

| Field | Value |
|-------|-------|
| Document ID | JOL-DOC-AUDIT-PREP-001 |
| Owner | Chief Compliance Officer |
| Version | 1.0 |
| Classification | RESTRICTED |
| Effective Date | [DATE] |
| Next Review | [DATE + 12 MONTHS] |
| Approved By | [APPROVER NAME] |

---

## 1. Purpose

This guide provides a structured approach to preparing for ISO 27001:2022, SOC 2 Type II, and GDPR compliance audits at Journey Of Life UAB. It consolidates preparation activities, evidence requirements, and common pitfalls across all three frameworks.

---

## 2. Audit Scope Overview

### 2.1 Framework Summary

| Framework | Standard | Audit Type | Frequency | Typical Duration |
|-----------|----------|------------|-----------|-----------------|
| ISO 27001 | ISO/IEC 27001:2022 | Certification / Surveillance | Annual (certification triennial) | 3–5 days (Stage 2) |
| SOC 2 | AICPA TSC 2017 | Type II Examination | Annual | 4–8 weeks observation period |
| GDPR | Regulation (EU) 2016/679 | Supervisory Authority / Internal | Ongoing / As required | 1–3 days |

### 2.2 Audit Triggers

- **Scheduled**: Annual certification cycle, contractually required SOC 2 report
- **Triggered**: Data breach (GDPR Art. 33), significant system change, customer request
- **Random**: VDAI supervisory audit (Lithuania), cross-border investigation

---

## 3. Pre-Audit Timeline

### 3.1 Twelve Weeks Before Audit

| # | Activity | Responsible | Reference |
|---|----------|-------------|-----------|
| 1 | Confirm audit scope and objectives with external auditor | CCO | — |
| 2 | Review previous audit findings and remediation status | CCO | Prior audit report |
| 3 | Verify ISMS scope document is current (ISO 27001 Clause 4.3) | CISO | `iso27001/policies/information-security-policy.md` |
| 4 | Ensure risk assessment has been performed within last 12 months | CISO | `iso27001/risk-register/risk-register-2026.md` |
| 5 | Confirm Statement of Applicability reflects current controls | CISO | `iso27001/soa/statement-of-applicability.md` |
| 6 | Validate all policies have been reviewed within policy-defined frequency | Policy Owners | `security-policies/` |
| 7 | Update ROPA entries for any new processing activities | DPO | `gdpr/ropa/ropa-template.md` |
| 8 | Verify all DPIAs are complete for high-risk processing | DPO | `gdpr/dpias/dpia-template.md` |

### 3.2 Eight Weeks Before Audit

| # | Activity | Responsible | Reference |
|---|----------|-------------|-----------|
| 9 | Collect access review evidence for observation period | IT Security | `soc2/access-reviews/quarterly-access-review-template.md` |
| 10 | Compile change management evidence (last 12 months) | DevOps Lead | `soc2/evidence/cc8/change-management-evidence.md` |
| 11 | Gather incident response records and post-incident reviews | CISO | `security-policies/incident-response-policy.md` |
| 12 | Verify vendor register is current; all DPAs signed | Procurement / DPO | `vendor-register/vendor-register-master.md` |
| 13 | Confirm penetration test completed within last 12 months | IT Security | `audit-evidence/penetration-tests/pen-test-report-template.md` |
| 14 | Review vulnerability scan results; remediate Critical/High findings | IT Security | `audit-evidence/vulnerability-scans/vulnerability-scan-template.md` |
| 15 | Validate backup restoration test results | IT Operations | `security-policies/backup-and-recovery-policy.md` |

### 3.3 Four Weeks Before Audit

| # | Activity | Responsible | Reference |
|---|----------|-------------|-----------|
| 16 | Conduct internal audit dry run | Internal Audit Lead | `iso27001/internal-audits/internal-audit-template.md` |
| 17 | Perform management review meeting | Senior Management | `iso27001/management-reviews/management-review-template.md` |
| 18 | Prepare evidence folder structure for auditor access | CCO | Audit evidence repository |
| 19 | Brief all interview candidates on audit expectations | Department Heads | — |
| 20 | Verify all employee training records are current | HR / CISO | Training management system |
| 21 | Confirm physical security controls (office access, CCTV) | Facilities | A.7 Physical controls |
| 22 | Test evidence collection scripts | DevOps | `scripts/evidence_collector.py` |

### 3.4 One Week Before Audit

| # | Activity | Responsible |
|---|----------|-------------|
| 23 | Final evidence completeness check using compliance validator | CCO |
| 24 | Prepare auditor welcome pack (scope, org chart, system overview) | CCO |
| 25 | Confirm interview schedule with all departments | CCO |
| 26 | Verify NDA/audit engagement letter signed | Legal |
| 27 | Prepare demo environment if required | Engineering |
| 28 | Brief reception/front desk on auditor arrival procedures | Facilities |

---

## 4. Evidence Requirements by Framework

### 4.1 ISO 27001:2022 Evidence Checklist

| Clause | Requirement | Evidence Location | Status |
|--------|-------------|-------------------|--------|
| 4.1 | Understanding the organisation and its context | ISMS scope document | [ ] |
| 4.2 | Understanding needs and expectations of interested parties | Stakeholder analysis | [ ] |
| 4.3 | Determining the scope of the ISMS | Scope statement | [ ] |
| 5.2 | Information security policy | `iso27001/policies/information-security-policy.md` | [ ] |
| 5.3 | Organisational roles, responsibilities and authorities | RACI matrix | [ ] |
| 6.1.2 | Information security risk assessment | `iso27001/risk-register/risk-register-2026.md` | [ ] |
| 6.1.3 | Information security risk treatment | Risk treatment plan | [ ] |
| 6.1.3 d | Statement of Applicability | `iso27001/soa/statement-of-applicability.md` | [ ] |
| 7.2 | Competence | Training records, certifications | [ ] |
| 7.3 | Awareness | Awareness training completion records | [ ] |
| 7.5 | Documented information | Document control log | [ ] |
| 8.2 | Information security risk assessment (operational) | Risk assessment records | [ ] |
| 8.3 | Information security risk treatment (operational) | Treatment plan status | [ ] |
| 9.1 | Monitoring, measurement, analysis and evaluation | KPI dashboards, metrics | [ ] |
| 9.2 | Internal audit | `iso27001/internal-audits/internal-audit-template.md` | [ ] |
| 9.3 | Management review | `iso27001/management-reviews/management-review-template.md` | [ ] |
| 10.1 | Nonconformity and corrective action | CAPA register | [ ] |
| 10.2 | Continual improvement | Improvement register | [ ] |

### 4.2 SOC 2 Type II Evidence Checklist

| TSC Category | Evidence Required | Evidence Location | Status |
|-------------|-------------------|-------------------|--------|
| CC1 – Control Environment | Code of conduct, org structure, HR policies | HR system | [ ] |
| CC2 – Communication and Information | Security awareness records, policy acknowledgements | LMS | [ ] |
| CC3 – Risk Assessment | Risk register, threat modelling records | `iso27001/risk-register/` | [ ] |
| CC4 – Monitoring Activities | Internal audit results, management reviews | `iso27001/internal-audits/` | [ ] |
| CC5 – Control Activities | Policies and procedures documentation | `security-policies/` | [ ] |
| CC6 – Logical and Physical Access | Access reviews, joiner/mover/leaver records | `soc2/evidence/cc6/` | [ ] |
| CC7 – System Operations | Incident logs, monitoring alerts, vulnerability scans | `soc2/evidence/cc7/` | [ ] |
| CC8 – Change Management | Change tickets, code review logs, deployment approvals | `soc2/evidence/cc8/` | [ ] |
| CC9 – Risk Mitigation | Vendor reviews, BCP test results | `soc2/vendor-reviews/` | [ ] |
| A1 – Availability | Uptime reports, SLA compliance, DR test results | `soc2/evidence/a1/` | [ ] |
| C1 – Confidentiality | Data classification, encryption evidence, NDAs | `security-policies/` | [ ] |
| P1 – Privacy | Privacy notices, DSR logs, consent records | `gdpr/` | [ ] |

### 4.3 GDPR Audit Evidence Checklist

| Article | Requirement | Evidence | Status |
|---------|-------------|----------|--------|
| Art. 6 | Lawfulness of processing | Consent records, legitimate interest assessments | [ ] |
| Art. 13–14 | Information to data subjects | Privacy policies for LT/LV/EE | [ ] |
| Art. 15–22 | Data subject rights | DSR procedure and request log | [ ] |
| Art. 28 | Processor contracts | Signed DPAs in vendor register | [ ] |
| Art. 30 | Records of processing activities | ROPA | [ ] |
| Art. 32 | Security of processing | Technical measures documentation | [ ] |
| Art. 33–34 | Breach notification | Incident response records | [ ] |
| Art. 35 | Data protection impact assessment | DPIA records | [ ] |
| Art. 37–39 | Data protection officer | DPO appointment letter, contact details | [ ] |
| Art. 44–49 | International transfers | SCCs, TIA records | [ ] |

---

## 5. Interview Preparation

### 5.1 Common Auditor Questions by Role

**CISO / IT Security Lead:**
- How do you identify and classify information assets?
- Walk me through your risk assessment methodology
- How are security incidents detected, escalated, and resolved?
- What is your vulnerability management process?

**DPO:**
- How do you maintain records of processing activities?
- Describe the data subject rights fulfilment process
- How are cross-border data transfers managed?
- What triggers a DPIA and how is it conducted?

**Engineering / DevOps Lead:**
- How are changes to production systems authorised and tracked?
- Describe your CI/CD pipeline security controls
- How are secrets managed in your development lifecycle?
- What is your backup and disaster recovery strategy?

**HR:**
- How is security awareness training delivered and tracked?
- What is the employee onboarding/offboarding security process?
- How are disciplinary actions for policy violations handled?

### 5.2 Interview Best Practices

1. **Answer only what is asked** — do not volunteer additional information
2. **Refer to documented evidence** — "Let me show you the procedure" rather than verbal explanation
3. **If unsure, defer** — "I'll confirm that and get back to you by [timeframe]"
4. **Be honest about gaps** — auditors value transparency and documented remediation plans
5. **Have evidence ready** — pre-stage documents for quick retrieval

---

## 6. Common Findings and Prevention

### 6.1 Frequent ISO 27001 Non-Conformities

| Finding | Prevention |
|---------|-----------|
| Risk assessment not updated after significant changes | Schedule quarterly risk review triggers |
| Internal audit scope does not cover all ISMS requirements | Use annual audit programme covering 3-year cycle |
| Management review missing required inputs (Clause 9.3) | Use `iso27001/management-reviews/management-review-template.md` checklist |
| Documented information not controlled (version, approval) | Implement document control metadata on all documents |
| Corrective actions not tracked to closure | Maintain CAPA register with status and due dates |

### 6.2 Frequent SOC 2 Exceptions

| Finding | Prevention |
|---------|-----------|
| Access not removed within SLA after termination | Automate offboarding with HR system integration |
| Changes deployed without approval evidence | Enforce PR approval requirements in GitHub branch protection |
| Vulnerability remediation exceeding policy timelines | Track with `scripts/vendor_risk_calculator.py` and escalate overdue items |
| Incomplete evidence for observation period gaps | Continuous evidence collection via `scripts/evidence_collector.py` |

### 6.3 Frequent GDPR Findings

| Finding | Prevention |
|---------|-----------|
| DSR response exceeding 30-day deadline | Track with `scripts/gdpr_dsr_tracker.py`, escalate at day 20 |
| ROPA missing new processing activities | Quarterly ROPA review aligned with product release cycle |
| Data retention not enforced | Automated retention schedules in `scripts/retention_calculator.py` |
| DPA not in place before data sharing | Vendor onboarding checklist requires DPA execution |

---

## 7. Audit Day Logistics

### 7.1 Audit Room Setup

- Secure meeting room with controlled access
- Projector/screen for evidence presentation
- Wi-Fi guest access (isolated VLAN) for auditor
- Printer access for evidence copies
- Water, coffee, and refreshments

### 7.2 Audit Support Team

| Role | Person | Responsibility |
|------|--------|---------------|
| Audit Coordinator | [NAME] | Primary point of contact, schedule management |
| Evidence Runner | [NAME] | Retrieve additional evidence as requested |
| Technical Lead | [NAME] | System demonstrations, technical clarifications |
| Legal Advisor | [NAME] | On-call for legal privilege questions |
| Note Taker | [NAME] | Document auditor questions, findings, commitments |

### 7.3 Daily Audit Routine

| Time | Activity |
|------|----------|
| 08:30 | Team briefing — review day's schedule, prepare evidence |
| 09:00 | Audit session begins |
| 12:00 | Lunch break (team debrief on morning session) |
| 13:00 | Audit session resumes |
| 16:30 | End-of-day wrap-up with auditor — clarify open items |
| 17:00 | Team debrief — prepare for next day, address open items |

---

## 8. Post-Audit Activities

### 8.1 Within 48 Hours

1. Send thank-you communication to audit team and internal staff
2. Compile all auditor questions and preliminary findings
3. Begin drafting management responses for any findings

### 8.2 Within Two Weeks

1. Receive formal audit report
2. Conduct management review of findings
3. Develop Corrective Action Plans (CAPs) for all non-conformities/exceptions
4. Assign owners and deadlines for each CAP
5. Update risk register with identified risks

### 8.3 Within 90 Days

1. Complete all corrective actions
2. Gather evidence of remediation
3. Conduct follow-up internal audit to verify closure
4. Report remediation status to senior management
5. Update compliance matrix: `COMPLIANCE_MATRIX.md`

---

## 9. Continuous Compliance Calendar

| Month | Activity |
|-------|----------|
| January | Annual risk assessment review, update risk register |
| February | Internal audit programme planning |
| March | Q1 access review, vendor register review |
| April | Policy review cycle (security policies) |
| May | Management review meeting |
| June | Q2 access review, vulnerability assessment |
| July | Mid-year internal audit |
| August | Policy review cycle (GDPR documents) |
| September | Q3 access review, DR test |
| October | Pre-audit preparation (if annual audit in Q4) |
| November | External audit / surveillance audit |
| December | Q4 access review, annual compliance report |

---

## 10. Related Documents

| Document | Location |
|----------|----------|
| Compliance Checklist | `docs/compliance-checklist.md` |
| New Employee Compliance Guide | `docs/new-employee-compliance-guide.md` |
| Incident Response Playbook | `docs/incident-response-playbook.md` |
| Compliance Validator Script | `compliance_validator.py` |
| Evidence Collector Script | `scripts/evidence_collector.py` |
| Compliance Matrix | `COMPLIANCE_MATRIX.md` |

---

## Document History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [DATE] | [AUTHOR] | Initial release |

## Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Chief Compliance Officer | [NAME] | [SIGNATURE] | [DATE] |
| CISO | [NAME] | [SIGNATURE] | [DATE] |
| DPO | [NAME] | [SIGNATURE] | [DATE] |

---

*This document is the property of Journey Of Life UAB. It is classified as RESTRICTED and must not be distributed without authorisation from the document owner. Legal review is recommended before use in audit engagements.*

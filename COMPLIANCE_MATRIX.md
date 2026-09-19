# JOL Compliance Matrix


> **TEMPLATE DOCUMENT** — This compliance matrix contains placeholders that must be completed by the compliance team with actual audit results, metrics data, and responsible party information. Placeholders are marked explicitly:
> - `[STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed]`
> - `[DATE — fill: YYYY-MM-DD]`
> - `[X — fill: actual metric value]`
> - `[NAME/SIGNATURE — fill: responsible party]`
>
> **Completion owner**: Chief Compliance Officer + DPO + CISO  
> **Target**: Complete all placeholders before ISO 27001 Stage 2 audit

## Document Information

| Field | Value |
|-------|-------|
| Document ID | JOL-DOC-CM-001 |
| Owner | Chief Compliance Officer |
| Version | 1.0 |
| Classification | RESTRICTED |
| Effective Date | [DATE — fill: YYYY-MM-DD] |
| Next Review | [DATE + 12 MONTHS] |

---

## Purpose

The Compliance Matrix provides a single-page view of Journey Of Life UAB's compliance posture across GDPR, ISO 27001:2022, and SOC 2 Type II frameworks. It maps each requirement to the implementing document and current status.

---

## 1. Overall Compliance Status

| Framework | Status | Last Audit | Next Audit | Certificate / Report |
|-----------|--------|-----------|------------|---------------------|
| GDPR | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] | [DATE — fill: YYYY-MM-DD] | [DATE — fill: YYYY-MM-DD] | N/A (regulatory) |
| ISO 27001:2022 | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] | [DATE — fill: YYYY-MM-DD] | [DATE — fill: YYYY-MM-DD] | [CERT NUMBER — fill: ISO certificate number] |
| SOC 2 Type II | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] | [DATE — fill: YYYY-MM-DD] | [DATE — fill: YYYY-MM-DD] | [REPORT REF — fill: SOC 2 report reference] |

**Status Key**: Compliant | Partially Compliant | Non-Compliant | Not Yet Assessed

---

## 2. GDPR Compliance Matrix

| # | Requirement | Article | Implementing Document | Status | Evidence |
|---|-------------|---------|----------------------|--------|----------|
| 1 | Lawfulness of processing | Art. 6 | Privacy policies, consent management | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] | `gdpr/privacy-policies/` |
| 2 | Special category processing | Art. 9 | Legitimate activities of religious body | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] | Privacy policies Art. 9(2)(d) basis |
| 3 | Transparency — privacy notices | Art. 13–14 | Country-specific privacy policies (LT/LV/EE) | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] | `gdpr/privacy-policies/{lt,lv,ee}/` |
| 4 | Right of access | Art. 15 | DSR procedure | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] | `gdpr/dsr-procedures/` |
| 5 | Right to rectification | Art. 16 | DSR procedure | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] | `gdpr/dsr-procedures/` |
| 6 | Right to erasure | Art. 17 | DSR procedure + retention policy | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] | `gdpr/dsr-procedures/` |
| 7 | Right to restriction | Art. 18 | DSR procedure | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] | `gdpr/dsr-procedures/` |
| 8 | Right to portability | Art. 20 | DSR procedure | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] | `gdpr/dsr-procedures/` |
| 9 | Right to object | Art. 21 | DSR procedure | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] | `gdpr/dsr-procedures/` |
| 10 | Automated decision-making | Art. 22 | DSR procedure | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] | `gdpr/dsr-procedures/` |
| 11 | Processor contracts (DPA) | Art. 28 | DPA template | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] | `vendor-register/dpa-template.md` |
| 12 | Records of processing | Art. 30 | ROPA template | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] | `gdpr/ropa/ropa-template.md` |
| 13 | Security of processing | Art. 32 | Security policies + technical measures | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] | `security-policies/` |
| 14 | Breach notification — authority | Art. 33 | Incident response playbook | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] | `docs/incident-response-playbook.md` |
| 15 | Breach notification — subjects | Art. 34 | Incident response playbook | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] | `docs/incident-response-playbook.md` |
| 16 | Data protection impact assessment | Art. 35 | DPIA template | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] | `gdpr/dpias/dpia-template.md` |
| 17 | Prior consultation | Art. 36 | DPIA procedure | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] | `gdpr/dpias/dpia-template.md` |
| 18 | DPO designation | Art. 37 | DPO appointment letter | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] | HR records |
| 19 | DPO tasks | Art. 39 | DPO role description | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] | Org chart + job description |
| 20 | International transfers | Art. 44–49 | DPA template + SCCs + TIA | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] | `vendor-register/dpa-template.md` |
| 21 | Data retention | Art. 5(1)(e) | Data retention policy | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] | `gdpr/retention-policies/` |
| 22 | Cookie consent | ePrivacy Art. 5(3) | Cookie policy | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] | `gdpr/cookie-policies/` |

---

## 3. ISO 27001:2022 Compliance Matrix

### 3.1 Management System Clauses (4–10)

| Clause | Requirement | Implementing Document | Status |
|--------|-------------|----------------------|--------|
| 4.1 | Understanding the organisation and its context | ISMS scope (information security policy) | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| 4.2 | Needs and expectations of interested parties | Stakeholder analysis in ISMS scope | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| 4.3 | Determining the scope of the ISMS | `iso27001/policies/information-security-policy.md` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| 4.4 | Information security management system | Full ISMS documentation suite | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| 5.1 | Leadership and commitment | Management review records | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| 5.2 | Information security policy | `iso27001/policies/information-security-policy.md` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| 5.3 | Organisational roles, responsibilities and authorities | RACI matrix + job descriptions | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| 6.1.2 | Information security risk assessment | `iso27001/risk-register/risk-register-2026.md` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| 6.1.3 | Information security risk treatment | Risk treatment plan | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| 6.1.3 d | Statement of Applicability | `iso27001/soa/statement-of-applicability.md` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| 6.2 | Information security objectives | Objectives in ISMS policy | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| 7.1 | Resources | Budget records, resource allocation | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| 7.2 | Competence | Training records, certifications | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| 7.3 | Awareness | Security awareness training records | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| 7.4 | Communication | Communication plan | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| 7.5 | Documented information | Document control process | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| 8.1 | Operational planning and control | Procedures documentation | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| 8.2 | Information security risk assessment (operational) | Risk assessment records | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| 8.3 | Information security risk treatment (operational) | Risk treatment records | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| 9.1 | Monitoring, measurement, analysis and evaluation | KPI dashboards, metrics | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| 9.2 | Internal audit | `iso27001/internal-audits/internal-audit-template.md` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| 9.3 | Management review | `iso27001/management-reviews/management-review-template.md` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| 10.1 | Nonconformity and corrective action | CAPA register | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| 10.2 | Continual improvement | Improvement register | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |

### 3.2 Annex A Controls (Key Controls)

| Control | Title | Implementing Document | Status |
|---------|-------|----------------------|--------|
| A.5.1 | Policies for information security | `iso27001/policies/information-security-policy.md` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| A.5.9 | Inventory of information and other associated assets | `iso27001/asset-register/asset-register.md` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| A.5.10 | Acceptable use of information and other associated assets | `security-policies/acceptable-use-policy.md` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| A.5.12 | Classification of information | `security-policies/data-classification-policy.md` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| A.5.15 | Access control | `iso27001/procedures/access-control-procedure.md` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| A.5.17 | Authentication information | `security-policies/password-policy.md` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| A.5.24 | Information security incident management planning and preparation | `security-policies/incident-response-policy.md` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| A.5.25 | Assessment and decision on information security events | `docs/incident-response-playbook.md` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| A.5.26 | Response to information security incidents | `docs/incident-response-playbook.md` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| A.5.27 | Learning from information security incidents | Post-incident reviews | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| A.5.35 | Independent review of information security | Internal/external audit results | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| A.6.7 | Remote working | `security-policies/remote-work-security-policy.md` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| A.7.4 | Physical security monitoring | CCTV, access control systems | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| A.8.9 | Configuration management | Infrastructure-as-code, CMDB | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| A.8.13 | Information backup | `security-policies/backup-and-recovery-policy.md` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| A.8.24 | Use of cryptography | `security-policies/encryption-policy.md` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| A.8.29 | Security testing in development and acceptance | Penetration testing, vulnerability scans | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |

*Full 93 controls detailed in `iso27001/soa/statement-of-applicability.md`*

---

## 4. SOC 2 Type II Compliance Matrix

| TSC | Title | Key Controls | Evidence Location | Status |
|-----|-------|-------------|-------------------|--------|
| CC1 | Control Environment | Code of conduct, HR policies, org structure | HR system | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| CC2 | Communication and Information | Security awareness, policy distribution | LMS, `docs/` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| CC3 | Risk Assessment | Risk register, threat modelling | `iso27001/risk-register/` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| CC4 | Monitoring Activities | Internal audit, management review | `iso27001/internal-audits/` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| CC5 | Control Activities | Policies, procedures, segregation of duties | `security-policies/` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| CC6.1 | Logical Access — Authorisation | Access control procedure | `iso27001/procedures/` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| CC6.2 | Logical Access — Registration | JML (joiner/mover/leaver) process | HR + IT | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| CC6.3 | Logical Access — Removal | Offboarding procedure | HR + IT | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| CC6.6 | Logical Access — MFA | Password policy + MFA enforcement | `security-policies/password-policy.md` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| CC6.7 | Logical Access — Restrict Transmission | Encryption policy | `security-policies/encryption-policy.md` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| CC7.1 | System Operations — Monitoring | SIEM, alerting | `soc2/evidence/cc7/` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| CC7.2 | System Operations — Anomaly Detection | IDS/IPS, EDR | `soc2/evidence/cc7/` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| CC7.3 | System Operations — Incident Response | Incident response playbook | `docs/incident-response-playbook.md` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| CC7.4 | System Operations — Vulnerability Management | Vulnerability scan programme | `audit-evidence/vulnerability-scans/` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| CC8.1 | Change Management — Authorisation | PR approval, change advisory board | `soc2/evidence/cc8/` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| CC8.2 | Change Management — Testing | CI/CD pipeline, test requirements | `soc2/evidence/cc8/` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| CC9.1 | Risk Mitigation — Business Continuity | BCP/DR plan, testing records | `security-policies/backup-and-recovery-policy.md` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| CC9.2 | Risk Mitigation — Vendor Management | Vendor register, DPA reviews | `vendor-register/` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| A1.1 | Availability — Capacity Management | Capacity planning, monitoring | `soc2/evidence/a1/` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| A1.2 | Availability — Incident Response | Incident response for availability events | `soc2/evidence/a1/` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| A1.3 | Availability — Recovery | DR testing, RTO/RPO compliance | `soc2/evidence/a1/` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| C1.1 | Confidentiality — Classification | Data classification policy | `security-policies/data-classification-policy.md` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| C1.2 | Confidentiality — Encryption | Encryption policy | `security-policies/encryption-policy.md` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| P1.1 | Privacy — Notice | Privacy policies | `gdpr/privacy-policies/` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| P1.2 | Privacy — Choice and Consent | Consent management, cookie policy | `gdpr/cookie-policies/` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| P1.3 | Privacy — Collection and Use | ROPA, purpose limitation | `gdpr/ropa/` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| P1.4 | Privacy — Access and Correction | DSR procedures | `gdpr/dsr-procedures/` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| P1.5 | Privacy — Disclosure to Third Parties | DPA, vendor register | `vendor-register/` | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |

*Full mapping in `soc2/trust-services-criteria/tsc-control-mapping.md`*

---

## 5. Country-Specific Compliance

| Country | Supervisory Authority | Key Legislation | Documents | Status | Phase |
|---------|----------------------|-----------------|-----------|--------|-------|
| Lithuania (LT) | VDAI | ADTAĮ, Mokesčių administravimo įstatymas, Darbo kodeksas | `country/lt/`, `gdpr/privacy-policies/lt/` | 🟡 Pilot — placeholders pending | Pilot (immediate) |
| Latvia (LV) | DVI | Personas datu apstrādes likums, Grāmatvedības likums, Darba likums | `country/lv/`, `gdpr/privacy-policies/lv/` | 🟡 Pre-positioned — not yet invoked | Pilot (pre-positioned) |
| Estonia (EE) | AKI | Isikuandmete kaitse seadus, Raamatupidamise seadus, TLS | `country/ee/`, `gdpr/privacy-policies/ee/` | 🟡 Pre-positioned — not yet invoked | Pilot (pre-positioned) |
| Poland (PL) | UODO | UODO regulations, Kodeks pracy | — | 🔴 Required before Phase 2 | Phase 2 (+6 months) |
| Germany (DE) | BfDI + Landesbehörden | BDSG, BGB | — | 🔴 Required before Phase 2 | Phase 2 (+6 months) |
| Italy (IT) | Garante | Codice Privacy, D.Lgs. 196/2003 | — | 🔴 Required before Phase 2 | Phase 2 (+6 months) |
| 21 other EU states | Various | National implementations | — | ⚪ Planned | Industrialization |

> **Scope decision**: See `gdpr/privacy-policies/scope-decision-c1-baltic-pilot.md` (JOL-SD-C1-001).

---

## 6. Compliance Metrics Dashboard

| Metric | Target | Current | Trend | Status |
|--------|--------|---------|-------|--------|
| Policy review completion | 100% within cycle | [X — fill: actual metric value]% | [TREND — fill: ↑ improving / → stable / ↓ declining] | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| DSR on-time response (≤30 days) | ≥95% | [X — fill: actual metric value]% | [TREND — fill: ↑ improving / → stable / ↓ declining] | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| Security awareness training completion | ≥98% | [X — fill: actual metric value]% | [TREND — fill: ↑ improving / → stable / ↓ declining] | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| Vulnerability remediation — Critical (≤7 days) | 100% | [X — fill: actual metric value]% | [TREND — fill: ↑ improving / → stable / ↓ declining] | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| Vulnerability remediation — High (≤30 days) | ≥95% | [X — fill: actual metric value]% | [TREND — fill: ↑ improving / → stable / ↓ declining] | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| Access review completion (quarterly) | 100% | [X — fill: actual metric value]% | [TREND — fill: ↑ improving / → stable / ↓ declining] | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| Vendor DPA coverage | 100% | [X — fill: actual metric value]% | [TREND — fill: ↑ improving / → stable / ↓ declining] | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| Incident response — MTTD (P1) | < 15 min | [X] min | [TREND — fill: ↑ improving / → stable / ↓ declining] | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| Incident response — MTTR (P1) | < 24 hours | [X] hours | [TREND — fill: ↑ improving / → stable / ↓ declining] | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| Uptime / availability SLA | ≥99.9% | [X — fill: actual metric value]% | [TREND — fill: ↑ improving / → stable / ↓ declining] | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| Penetration test — Critical findings remediated | 100% within 30 days | [X — fill: actual metric value]% | [TREND — fill: ↑ improving / → stable / ↓ declining] | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| Internal audit findings closed on time | ≥90% | [X — fill: actual metric value]% | [TREND — fill: ↑ improving / → stable / ↓ declining] | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |

---

## 7. Improvement Roadmap

| # | Initiative | Owner | Target Date | Status |
|---|-----------|-------|-------------|--------|
| 1 | Complete all placeholder dates in documents | All owners | [DATE — fill: YYYY-MM-DD] | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| 2 | Implement automated DSR tracking | DevOps + DPO | [DATE — fill: YYYY-MM-DD] | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| 3 | Deploy continuous compliance monitoring | DevOps | [DATE — fill: YYYY-MM-DD] | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| 4 | Complete ISO 27001 Stage 2 audit | CISO | [DATE — fill: YYYY-MM-DD] | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| 5 | Obtain SOC 2 Type II report | CISO + Auditor | [DATE — fill: YYYY-MM-DD] | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| 6 | Expand country-specific compliance: PL/DE/IT (Phase 2) → remaining 21 EU states (industrialization) | DPO | Phase 2: +6 months from pilot | 🟡 Planned |
| 7 | Implement automated evidence collection pipeline | DevOps | [DATE — fill: YYYY-MM-DD] | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |
| 8 | Conduct GDPR Art. 35 DPIA for all high-risk processing | DPO | [DATE — fill: YYYY-MM-DD] | [STATUS — fill: Compliant / Partially Compliant / Non-Compliant / Not Yet Assessed] |

---

## Related Documents

| Document | Location |
|----------|----------|
| Compliance Checklist | `docs/compliance-checklist.md` |
| Audit Preparation Guide | `docs/audit-preparation-guide.md` |
| Compliance Validator Script | `compliance_validator.py` |
| Changelog | `CHANGELOG.md` |
| Glossary | `GLOSSARY.md` |

---

## Document History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [DATE — fill: YYYY-MM-DD] | [AUTHOR — fill: document author] | Initial compliance matrix |

## Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Chief Compliance Officer | [NAME — fill: responsible party] | [SIGNATURE — fill: digital/physical signature] | [DATE — fill: YYYY-MM-DD] |
| CISO | [NAME — fill: responsible party] | [SIGNATURE — fill: digital/physical signature] | [DATE — fill: YYYY-MM-DD] |
| DPO | [NAME — fill: responsible party] | [SIGNATURE — fill: digital/physical signature] | [DATE — fill: YYYY-MM-DD] |
| CEO | [NAME — fill: responsible party] | [SIGNATURE — fill: digital/physical signature] | [DATE — fill: YYYY-MM-DD] |

---

*This document is the property of Journey Of Life UAB. It is classified as RESTRICTED. Update this matrix after every audit, management review, or significant compliance event.*

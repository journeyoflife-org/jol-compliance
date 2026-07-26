# Risk Register — 2026

**Journey Of Life UAB — ISMS Risk Register (ISO 27001 Clause 6.1.2)**

| Field | Value |
|-------|-------|
| **Document ID** | JOL-ISMS-RR-2026 |
| **Organisation** | Journey Of Life UAB |
| **Assessment Period** | 1 January 2026 – 31 December 2026 |
| **Register Owner** | [CISO Name] |
| **Methodology** | ISO 27005-based qualitative risk assessment |
| **Last Updated** | [YYYY-MM-DD] |
| **Next Review** | [YYYY-MM-DD] |
| **Risk Acceptance Threshold** | Score ≤ [X] acceptable without treatment plan |
| **Classification** | Internal — Confidential |

---

## 1. Risk Assessment Methodology

### 1.1 Likelihood Scale

| Score | Rating | Description |
|-------|--------|-------------|
| 1 | Rare | Not expected to occur (< once in 5 years) |
| 2 | Unlikely | May occur occasionally (once in 3–5 years) |
| 3 | Possible | May occur within 12–36 months |
| 4 | Likely | Expected to occur within 12 months |
| 5 | Almost certain | Expected to occur within 3 months |

### 1.2 Impact Scale

| Score | Rating | Financial | Operational | Reputational | Legal/Regulatory |
|-------|--------|-----------|-------------|-------------|-----------------|
| 1 | Negligible | <€5,000 | Minimal disruption | No media attention | No enforcement |
| 2 | Minor | €5K–€25K | <4 hours disruption | Local media | Warning letter |
| 3 | Moderate | €25K–€100K | 4–24 hours disruption | National media | Investigation |
| 4 | Major | €100K–€500K | 1–7 days disruption | International media | Enforcement action |
| 5 | Severe | >€500K | >7 days / business-threatening | Existential reputation | Major fine / criminal |

### 1.3 Risk Score Matrix

| | **1** | **2** | **3** | **4** | **5** |
|---|---|---|---|---|---|
| **5** | 5 | 10 | 15 | 20 | 25 |
| **4** | 4 | 8 | 12 | 16 | 20 |
| **3** | 3 | 6 | 9 | 12 | 15 |
| **2** | 2 | 4 | 6 | 8 | 10 |
| **1** | 1 | 2 | 3 | 4 | 5 |

### 1.4 Treatment Thresholds

| Score Range | Risk Level | Action Required |
|------------|-----------|----------------|
| 1–4 | **Low** | Accept — monitor at annual review |
| 5–9 | **Medium** | Mitigate if cost-effective — review quarterly |
| 10–15 | **High** | Treat immediately — monthly review by CISO |
| 16–25 | **Critical** | Escalate to Board — treatment plan within 48 hours |

---

## 2. Risk Register Entries

### R-2026-001: Unauthorised Cross-Tenant Data Access

| Field | Detail |
|-------|--------|
| **Risk ID** | R-2026-001 |
| **Category** | Multi-tenancy / Data Isolation |
| **Description** | A vulnerability or misconfiguration in tenant isolation controls allows one tenant to access another tenant's personal data, including special category data (Art. 9) |
| **Affected Assets** | Tenant databases, API layer, application platform |
| **Threat Agent** | Malicious tenant, insider, external attacker |
| **Likelihood** | 2 (Unlikely) |
| **Impact** | 5 (Severe) — GDPR Art. 33 breach affecting multiple institutions |
| **Inherent Risk Score** | 10 (High) |
| **Current Controls** | Row-level security / schema separation, tenant_id enforcement, automated isolation tests, penetration testing, WAF, input validation |
| **Residual Risk Score** | 4 (Low) |
| **Treatment** | Maintain existing controls; add quarterly tenant isolation penetration test |
| **Risk Owner** | CISO |
| **Status** | Monitored |

### R-2026-002: Personal Data Breach via Sub-Processor

| Field | Detail |
|-------|--------|
| **Risk ID** | R-2026-002 |
| **Category** | Supply Chain / Third-Party |
| **Description** | A sub-processor experiences a security incident resulting in exposure of personal data processed on behalf of Journey Of Life or its tenant institutions |
| **Affected Assets** | Sub-processor systems, data shared with processors |
| **Threat Agent** | External attacker targeting sub-processor |
| **Likelihood** | 3 (Possible) |
| **Impact** | 4 (Major) — GDPR liability, reputational damage |
| **Inherent Risk Score** | 12 (High) |
| **Current Controls** | Art. 28 DPAs with all processors, annual vendor security assessments, SOC 2 / ISO 27001 certification requirements, incident notification clauses |
| **Residual Risk Score** | 6 (Medium) |
| **Treatment** | Enhance monitoring; require sub-processor breach notification within 24 hours; maintain cyber insurance |
| **Risk Owner** | DPO |
| **Status** | Treatment in progress |

### R-2026-003: Ransomware Attack on Platform Infrastructure

| Field | Detail |
|-------|--------|
| **Risk ID** | R-2026-003 |
| **Category** | Cyber Threat |
| **Description** | Ransomware attack encrypts platform databases or infrastructure, causing service disruption and potential data loss for all tenants |
| **Affected Assets** | Production servers, databases, storage systems |
| **Threat Agent** | External attacker (organised crime) |
| **Likelihood** | 3 (Possible) |
| **Impact** | 5 (Severe) — Platform-wide disruption affecting ~400,000 institutions |
| **Inherent Risk Score** | 15 (High) |
| **Current Controls** | Encrypted immutable backups (daily), network segmentation, endpoint protection, phishing awareness training, incident response plan, offline backup copies |
| **Residual Risk Score** | 8 (Medium) |
| **Treatment** | Test backup restore quarterly; conduct tabletop ransomware exercise annually; maintain offline backup copies |
| **Risk Owner** | CISO |
| **Status** | Monitored |

### R-2026-004: GDPR Non-Compliance — Children's Data

| Field | Detail |
|-------|--------|
| **Risk ID** | R-2026-004 |
| **Category** | Regulatory Compliance |
| **Description** | Platform processes children's data (under 16) without adequate parental consent mechanisms, violating GDPR Art. 8 |
| **Affected Assets** | Children's personal data, consent management system |
| **Threat Agent** | N/A (compliance failure) |
| **Likelihood** | 2 (Unlikely) |
| **Impact** | 5 (Severe) — Art. 83(5) fine up to €20M or 4% global turnover |
| **Inherent Risk Score** | 10 (High) |
| **Current Controls** | Age verification gates, parental consent workflow, children's data flagging, enhanced protection controls, DPO oversight, DPIA completed |
| **Residual Risk Score** | 4 (Low) |
| **Treatment** | Annual audit of consent workflows; legal review of age verification mechanisms per member state |
| **Risk Owner** | DPO |
| **Status** | Monitored |

### R-2026-005: Insider Threat — Unauthorised Data Exfiltration

| Field | Detail |
|-------|--------|
| **Risk ID** | R-2026-005 |
| **Category** | Insider Threat |
| **Description** | Employee or contractor with privileged access extracts and exfiltrates tenant personal data for financial gain or malicious purposes |
| **Affected Assets** | All personal data accessible to privileged users |
| **Threat Agent** | Insider (employee, contractor) |
| **Likelihood** | 2 (Unlikely) |
| **Impact** | 5 (Severe) — Mass data breach, regulatory action |
| **Inherent Risk Score** | 10 (High) |
| **Current Controls** | Background screening, least privilege, PAM with session recording, DLP, segregation of duties, quarterly access reviews, SIEM monitoring |
| **Residual Risk Score** | 5 (Medium) |
| **Treatment** | Implement data loss prevention (DLP) rules; enhance privileged session monitoring; maintain insider threat programme |
| **Risk Owner** | CISO |
| **Status** | Treatment in progress |

### R-2026-006: Loss of ISO 27001 Certification

| Field | Detail |
|-------|--------|
| **Risk ID** | R-2026-006 |
| **Category** | Compliance |
| **Description** | Failure to maintain ISMS conformance results in suspension or withdrawal of ISO 27001 certification |
| **Affected Assets** | ISMS documentation, certification status |
| **Threat Agent** | N/A |
| **Likelihood** | 1 (Rare) |
| **Impact** | 4 (Major) — Loss of customer trust, contractual breach |
| **Inherent Risk Score** | 4 (Low) |
| **Current Controls** | Annual internal audits, management reviews, continuous improvement process, dedicated ISMS Manager role |
| **Residual Risk Score** | 2 (Low) |
| **Treatment** | Accept — maintain audit programme and management review cadence |
| **Risk Owner** | ISMS Manager |
| **Status** | Accepted |

### R-2026-007: DDoS Attack on Platform

| Field | Detail |
|-------|--------|
| **Risk ID** | R-2026-007 |
| **Category** | Cyber Threat / Availability |
| **Description** | Distributed denial of service attack renders the platform unavailable to tenants |
| **Affected Assets** | Platform web servers, API gateway, DNS |
| **Threat Agent** | External attacker, hacktivists |
| **Likelihood** | 4 (Likely) |
| **Impact** | 3 (Moderate) — Temporary disruption, SLA breaches |
| **Inherent Risk Score** | 12 (High) |
| **Current Controls** | DDoS mitigation service, CDN, auto-scaling, rate limiting, WAF, multi-region failover |
| **Residual Risk Score** | 6 (Medium) |
| **Treatment** | Maintain DDoS mitigation; test failover annually; review SLA impact thresholds |
| **Risk Owner** | Head of Operations |
| **Status** | Monitored |

### R-2026-008: Failure to Notify Supervisory Authority Within 72 Hours

| Field | Detail |
|-------|--------|
| **Risk ID** | R-2026-008 |
| **Category** | Regulatory Compliance |
| **Description** | A personal data breach occurs but the incident response team fails to identify the breach and/or notify the supervisory authority within GDPR Art. 33's 72-hour window |
| **Affected Assets** | Incident response processes, breach notification procedures |
| **Threat Agent** | N/A (process failure) |
| **Likelihood** | 2 (Unlikely) |
| **Impact** | 4 (Major) — Aggravated enforcement |
| **Inherent Risk Score** | 8 (Medium) |
| **Current Controls** | Incident response plan, 24/7 on-call rotation, breach notification playbook, SIEM alerting, annual tabletop exercises |
| **Residual Risk Score** | 4 (Low) |
| **Treatment** | Conduct bi-annual breach notification tabletop exercise; automate breach assessment checklist |
| **Risk Owner** | DPO |
| **Status** | Monitored |

### R-2026-009: Supply Chain Compromise via CI/CD Pipeline

| Field | Detail |
|-------|--------|
| **Risk ID** | R-2026-009 |
| **Category** | Supply Chain / Software Security |
| **Description** | Compromised dependency, container image, or CI/CD pipeline component introduces malicious code into the platform |
| **Affected Assets** | Source code, CI/CD pipeline, container registry, third-party libraries |
| **Threat Agent** | External attacker, compromised open-source project |
| **Likelihood** | 3 (Possible) |
| **Impact** | 5 (Severe) — Platform compromise, data breach |
| **Inherent Risk Score** | 15 (High) |
| **Current Controls** | SCA scanning, signed commits, code review, container scanning, dependency pinning, SBOM, immutable infrastructure |
| **Residual Risk Score** | 8 (Medium) |
| **Treatment** | Implement software signing verification; add supply chain attestation; enhance dependency monitoring |
| **Risk Owner** | Head of Engineering |
| **Status** | Treatment in progress |

### R-2026-010: Encryption Key Compromise

| Field | Detail |
|-------|--------|
| **Risk ID** | R-2026-010 |
| **Category** | Cryptographic Security |
| **Description** | Encryption keys (at-rest or field-level) are compromised, enabling unauthorised decryption of personal data |
| **Affected Assets** | Key management service, encrypted databases, field-level encryption |
| **Threat Agent** | Insider, external attacker |
| **Likelihood** | 1 (Rare) |
| **Impact** | 5 (Severe) — Exposure of all encrypted personal data |
| **Inherent Risk Score** | 5 (Medium) |
| **Current Controls** | Dedicated KMS, key separation, annual key rotation, HSM-backed storage, keys stored separately from data |
| **Residual Risk Score** | 2 (Low) |
| **Treatment** | Accept — maintain KMS controls and rotation schedule |
| **Risk Owner** | CISO |
| **Status** | Accepted |

---

## 3. Risk Summary Dashboard

| Level | Count | Risk IDs |
|-------|-------|---------|
| **Critical (16–25)** | 0 | — |
| **High (10–15)** | 3 | R-002, R-003, R-007, R-009 (inherent) |
| **Medium (5–9)** | 4 | R-002, R-003, R-005, R-007, R-009 (residual) |
| **Low (1–4)** | 6 | R-001, R-004, R-006, R-008, R-010 (residual) |

---

## 4. Risk Treatment Plan Tracker

| Risk ID | Treatment Action | Owner | Target Date | Status |
|---------|----------------|-------|------------|--------|
| R-2026-002 | Enhance sub-processor breach notification SLA to 24 hours | DPO | [Date] | In Progress |
| R-2026-005 | Deploy DLP rules for privileged users | CISO | [Date] | In Progress |
| R-2026-009 | Implement supply chain attestation | Head of Engineering | [Date] | In Progress |

---

## 5. Risk Acceptance Decisions

| Risk ID | Risk Level | Justification | Approved By | Date |
|---------|-----------|---------------|------------|------|
| R-2026-006 | Low (2) | Comprehensive ISMS programme with annual audits | CISO | [Date] |
| R-2026-010 | Low (2) | Robust KMS with separation and rotation | CISO | [Date] |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [YYYY-MM-DD] | [CISO Name] | Initial 2026 risk register |

---

*This Risk Register covers the information security risks to the Journey Of Life multi-tenant SaaS platform as assessed under ISO/IEC 27001:2022 Clause 6.1.2. It is reviewed quarterly and updated whenever significant changes to the threat landscape, organisational context, or risk profile occur. Risk acceptance decisions are approved by the risk owner and reported to the management review.*

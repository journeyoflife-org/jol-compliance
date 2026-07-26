# Information Security Management System (ISMS) Policy

**ISO/IEC 27001:2022 — Master ISMS Policy for Journey Of Life UAB**

| Field | Value |
|-------|-------|
| **Document ID** | JOL-ISMS-001 |
| **Organisation** | Journey Of Life UAB |
| **ISMS Scope** | Design, development, operation, and support of the Journey Of Life multi-tenant SaaS platform |
| **Policy Owner** | [CISO Name] |
| **Version** | 1.0 |
| **Effective Date** | [YYYY-MM-DD] |
| **Last Reviewed** | [YYYY-MM-DD] |
| **Next Review Due** | [YYYY-MM-DD] |
| **Certification Body** | [Certification Body Name] |
| **Certificate Number** | [Certificate Number] |
| **Certificate Expiry** | [YYYY-MM-DD] |
| **Classification** | Internal — All Staff |

---

## 1. Policy Statement (ISO 27001 Clause 5.2)

Journey Of Life UAB is committed to protecting the confidentiality, integrity, and availability of all information assets processed, stored, or transmitted in the delivery of its multi-tenant SaaS platform serving religious institutions across 28 EU member states.

The ISMS is established, implemented, maintained, and continually improved in accordance with ISO/IEC 27001:2022 and supports compliance with GDPR, SOC 2 Type II, and applicable national data protection laws.

**Information security objectives:**
- Protect tenant data confidentiality with zero cross-tenant data leakage
- Maintain platform availability ≥99.9% (excluding planned maintenance)
- Ensure data integrity with zero unauthorised modification incidents
- Achieve zero GDPR enforcement actions and zero SOC 2 exceptions
- Respond to security incidents within 1 hour (triage) and notify breaches within 72 hours
- Maintain 100% staff completion of annual security awareness training

---

## 2. Scope (ISO 27001 Clause 4.3)

### 2.1 In Scope

- All information assets owned, processed, or managed by Journey Of Life UAB
- The Journey Of Life multi-tenant SaaS platform and all associated infrastructure
- All employees, contractors, consultants, and temporary staff
- All third parties and sub-processors with access to Company information assets
- All processing of personal data on behalf of religious institution tenants (controllers)
- Cloud infrastructure in EU regions (primary: EU-West; secondary: EU-Central)
- All office locations and remote working environments

### 2.2 Out of Scope

- Tenant-managed systems and data outside the Platform
- Third-party systems accessed via Platform integrations (governed by respective DPAs)

### 2.3 Interested Parties

| Party | Requirements |
|-------|-------------|
| Religious institution tenants (controllers) | Data protection, tenant isolation, DPA compliance |
| Data subjects (clergy, members, children) | GDPR rights, privacy, data security |
| Supervisory authorities (VDAI, DVI, AKI) | GDPR compliance, breach notification, ROPA |
| Certification body | ISO 27001 conformance, audit access |
| SOC 2 auditors | Trust Services Criteria evidence, system description |
| Employees and contractors | Security policies, training, incident reporting |
| Shareholders / Board | Risk management, business continuity, reputation |

---

## 3. Leadership and Commitment (ISO 27001 Clause 5)

### 3.1 Roles and Responsibilities

| Role | ISMS Responsibility |
|------|-------------------|
| **Board of Directors** | Ultimate accountability; approve ISMS scope, policy, and resources |
| **CISO** | ISMS establishment, implementation, and maintenance; risk treatment decisions |
| **ISMS Manager** | Day-to-day ISMS operation, documentation, audit coordination |
| **DPO** | GDPR compliance oversight, DPIA coordination, supervisory authority liaison |
| **System Owners** | Security of assigned systems; access control decisions |
| **All Personnel** | Policy compliance; incident reporting; security awareness |

### 3.2 Segregation of Duties (A.5.3)

- Development, testing, and production environments are segregated
- No individual may develop, approve, and deploy production changes without independent review
- Security monitoring is independent of operational management

---

## 4. Risk Assessment and Treatment (ISO 27001 Clause 6.1)

### 4.1 Risk Assessment Methodology

Risk assessments follow the documented methodology in `iso27001/policies/risk-methodology.md` and align with ISO/IEC 27005.

- **Likelihood scale:** 1 (Rare) to 5 (Almost certain)
- **Impact scale:** 1 (Negligible) to 5 (Severe)
- **Risk score:** Likelihood × Impact (1–25)
- **Risk acceptance threshold:** Risks ≤ [X] are acceptable; above requires treatment plan

### 4.2 Risk Treatment

| Option | Description |
|--------|-------------|
| Mitigate | Implement controls to reduce likelihood or impact |
| Transfer | Share risk with third party (insurance, outsourcing) |
| Accept | Acknowledge and accept (requires risk owner approval) |
| Avoid | Discontinue the risk-generating activity |

### 4.3 Statement of Applicability (SoA)

The SoA (`iso27001/soa/`) covers all 93 Annex A controls with justification for applicability and implementation status.

---

## 5. Asset Management (ISO 27001 A.5.9–A.5.14)

### 5.1 Asset Inventory

All information assets are inventoried in the Asset Register (`iso27001/asset-register/`) with:
- Asset owner, classification, location, and criticality

### 5.2 Information Classification

| Level | Description | Handling |
|-------|------------|---------|
| **Public** | Approved for public disclosure | No restrictions |
| **Internal** | General internal use | Not for external distribution |
| **Confidential** | Sensitive business or personal data | Encrypted; need-to-know access |
| **Restricted** | Highly sensitive (Art. 9 data, credentials, financial) | Field-level encryption; MFA access |

### 5.3 Acceptable Use (A.5.10)

Information assets are used only for legitimate business purposes and in accordance with classification. See `security-policies/acceptable-use-policy.md`.

---

## 6. Access Control (ISO 27001 A.5.15–A.5.18)

### 6.1 Principles

- **Least privilege:** Minimum access required for job function
- **Need-to-know:** Confidential/Restricted data requires documented justification
- **Default deny:** All access denied unless explicitly granted
- **Segregation of duties:** Critical operations require multiple authorised individuals

### 6.2 User Access Lifecycle

| Phase | Process |
|-------|---------|
| **Provisioning** | Access request → manager approval → system owner approval → provisioning |
| **Modification** | Role change → access review → updated provisioning |
| **Deprovisioning** | Termination notification → access removal within 24 hours |
| **Review** | Quarterly access review; recertification or revocation |

### 6.3 Authentication

- MFA mandatory for all production and administrative systems
- Passwords: ≥12 characters, complexity enforced
- Service accounts: certificate-based or key-based authentication with rotation

### 6.4 Multi-Tenant Isolation

- Logical isolation via [schema separation / row-level security]
- Cross-tenant access technically prevented and logged as security event
- Tenant administrators access only their own tenant's data

See `iso27001/procedures/access-control-procedure.md` for detailed procedures.

---

## 7. Cryptography (ISO 27001 A.8.24)

| Requirement | Standard |
|------------|---------|
| Data at rest | AES-256 for all stored personal data |
| Data in transit | TLS 1.2 minimum (TLS 1.3 preferred) |
| Field-level encryption | Application-level for Art. 9 special category data |
| Key management | Dedicated KMS; annual rotation; separate from encrypted data |
| Approved algorithms | AES-256, RSA-2048+, ECDSA P-256+, SHA-256+ |

See `security-policies/encryption-policy.md` for full encryption policy.

---

## 8. Physical Security (ISO 27001 A.7.1–A.7.14)

- Physical access to data centres managed by hosting provider under SOC 2 Type II certification
- Office premises secured with badge access and visitor logging
- Remote workers: full-disk encryption, screen locks, secure device handling
- Equipment disposal: NIST 800-88 compliant secure wiping

---

## 9. Operations Security (ISO 27001 A.8.1–A.8.34)

### 9.1 Change Management (A.8.32)

All production changes follow: request → impact assessment → approval → CI/CD implementation → post-implementation review.

### 9.2 Vulnerability Management (A.8.8)

| Activity | Frequency | Patching SLA |
|----------|-----------|-------------|
| Automated vulnerability scanning | Weekly | — |
| Penetration testing (external) | Annual | — |
| Critical vulnerability patching | — | ≤24 hours |
| High vulnerability patching | — | ≤7 days |
| Medium vulnerability patching | — | ≤30 days |

### 9.3 Logging and Monitoring (A.8.15–A.8.16)

- All production access logged with immutable audit trails
- 12-month log retention minimum
- Real-time security event monitoring and alerting
- Clock synchronisation (A.8.17) via NTP

### 9.4 Backup and Recovery (A.8.13)

- Daily automated encrypted backups
- Quarterly restore testing
- RPO: [4 hours] | RTO: [24 hours]

See `security-policies/backup-and-recovery-policy.md` for full backup policy.

---

## 10. Supplier Relationships (ISO 27001 A.5.19–A.5.23)

- Security due diligence for all suppliers with data access
- GDPR Art. 28-compliant DPAs with all processors
- Annual supplier security review (see `vendor-register/`)
- Sub-processor changes communicated to controllers with ≥30 days' notice
- Cloud services governed by security requirements (A.5.23)

---

## 11. Incident Management (ISO 27001 A.5.24–A.5.28)

### 11.1 Response Process

1. **Detection** — Identify and classify the security event
2. **Containment** — Limit scope and impact
3. **Eradication** — Remove root cause
4. **Recovery** — Restore affected systems
5. **Lessons learned** — Document and improve controls

### 11.2 Notification Requirements

| Scenario | Target | SLA |
|----------|--------|-----|
| Personal data breach (GDPR) | Supervisory authority | ≤72 hours |
| Personal data breach — high risk | Affected data subjects | Without undue delay |
| Tenant data breach | Affected tenant (controller) | ≤24 hours |
| SOC 2 relevant incident | Audit firm, affected customers | Per contractual terms |

See `security-policies/incident-response-policy.md` for full incident response policy.

---

## 12. Business Continuity (ISO 27001 A.5.29–A.5.30)

- BCP and DR Plan maintained and tested annually
- Maximum tolerable downtime: [X hours]
- Redundancy architecture in primary and secondary EU regions
- ICT readiness assessed against business requirements

---

## 13. Compliance (ISO 27001 Clause 9)

### 13.1 Internal Audit (Clause 9.2)

- Annual internal audit programme covering all ISMS clauses and Annex A controls
- Audits conducted by qualified, independent personnel
- Findings tracked, remediated, and reported to management

### 13.2 Management Review (Clause 9.3)

Annual management review considering:
- Audit results and compliance status
- Security incidents and trends
- Risk assessment outcomes and treatment effectiveness
- Feedback from interested parties
- Resource adequacy
- Improvement opportunities

### 13.3 Nonconformity and Corrective Action (Clause 10.1)

- All nonconformities documented with root cause analysis
- Corrective actions tracked to completion
- Effectiveness of corrective actions verified

---

## 14. Competence and Awareness (ISO 27001 Clause 7.2–7.3)

- Background screening appropriate to role (A.6.1)
- Security awareness training within 30 days of onboarding and annually thereafter (A.6.3)
- Role-specific security training for privileged access roles
- Written acknowledgment of security responsibilities

---

## 15. Document Control

| Requirement | Implementation |
|------------|---------------|
| Version control | Git-based; all changes tracked with commit history |
| Review cycle | Annual minimum; triggered by material change |
| Approval | CISO + relevant stakeholders before publication |
| Distribution | Internal repository; classified per information classification |
| Retention | Superseded versions retained 5 years for audit trail |

---

## 16. Related Documents

| Document | Location |
|----------|----------|
| Master InfoSec Policy | `security-policies/information-security-policy.md` |
| Access Control Procedure | `iso27001/procedures/access-control-procedure.md` |
| Risk Register | `iso27001/risk-register/` |
| Statement of Applicability | `iso27001/soa/` |
| Asset Register | `iso27001/asset-register/` |
| Internal Audit Template | `iso27001/internal-audits/` |
| Management Review Template | `iso27001/management-reviews/` |
| All Security Policies | `security-policies/` |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [YYYY-MM-DD] | [CISO Name] | Initial ISMS policy creation |

---

## Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| CISO | [Name] | [Date] | _________________ |
| ISMS Manager | [Name] | [Date] | _________________ |
| Board Representative | [Name] | [Date] | _________________ |

---

*This ISMS Policy establishes the information security management framework for Journey Of Life UAB in accordance with ISO/IEC 27001:2022. It is reviewed annually and updated to reflect changes in the threat landscape, regulatory environment, and organisational structure. All personnel are required to comply with this policy and all referenced subordinate policies and procedures.*

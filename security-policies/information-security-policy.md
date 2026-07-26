# Information Security Policy

**Master Information Security Policy for [Company Name]**

| Field | Value |
|-------|-------|
| **Organisation** | [Company Name] |
| **Policy Number** | ISP-001 |
| **Version** | [Version Number] |
| **Effective Date** | [YYYY-MM-DD] |
| **Last Reviewed** | [YYYY-MM-DD] |
| **Next Review Due** | [YYYY-MM-DD] |
| **Policy Owner** | [CISO Name] |
| **Approved By** | [Executive Sponsor / Board] |
| **Classification** | Internal — All Staff |

---

## 1. Purpose

This Information Security Policy establishes the framework for protecting the confidentiality, integrity, and availability of information assets processed, stored, and transmitted by [Company Name] in the delivery of its multi-tenant SaaS platform serving religious institutions across 28 EU member states.

This policy supports the organisation's compliance with:

- **ISO/IEC 27001:2022** — Information Security Management System (ISMS)
- **GDPR (Regulation (EU) 2016/679)** — General Data Protection Regulation
- **SOC 2 Type II** — Trust Services Criteria (Security, Availability, Confidentiality)
- **ePrivacy Directive (2002/58/EC)** — Electronic communications privacy
- **National data protection laws** of EU member states (LT, LV, EE, and 25 others)

---

## 2. Scope

This policy applies to:

- All employees, contractors, consultants, and temporary staff of [Company Name]
- All information assets owned, processed, or managed by [Company Name]
- All systems, networks, applications, and infrastructure within the ISMS scope
- All third parties and sub-processors with access to [Company Name] information assets
- All processing of personal data on behalf of religious institution tenants (controllers)

**ISMS Scope Statement:** The ISMS covers the design, development, operation, and support of the [Platform Name] multi-tenant SaaS platform, including all associated infrastructure, personnel, and third-party services.

---

## 3. Information Security Objectives

| Objective | Target | Measurement |
|-----------|--------|-------------|
| Protect tenant data confidentiality | Zero cross-tenant data leakage incidents | Quarterly isolation testing |
| Ensure platform availability | ≥ 99.9% uptime (excluding planned maintenance) | Monthly uptime reports |
| Maintain data integrity | Zero unauthorised data modification incidents | Audit log monitoring |
| Achieve regulatory compliance | Zero GDPR enforcement actions; zero SOC 2 exceptions | Annual audit results |
| Respond to incidents promptly | 100% of incidents triaged within 1 hour; breaches notified within 72 hours | Incident metrics |
| Maintain staff security awareness | 100% staff completion of annual security training | Training completion rates |

---

## 4. Governance and Organisation

### 4.1 Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| **Board / Executive Management** | Ultimate accountability for information security; approve ISMS scope and objectives |
| **CISO** | Overall management of the ISMS; risk assessment and treatment decisions |
| **ISMS Manager** | Day-to-day ISMS operation, policy maintenance, and audit coordination |
| **Data Protection Officer (DPO)** | GDPR compliance oversight, DPIA coordination, supervisory authority liaison |
| **System Owners** | Security of assigned systems; access control decisions |
| **All Personnel** | Comply with this policy; report security incidents and concerns |

### 4.2 Segregation of Duties

- Development, testing, and production environments shall be segregated
- No individual shall have the ability to develop, approve, and deploy changes to production without independent review
- Security monitoring functions shall be independent of operational management

---

## 5. Asset Management

### 5.1 Information Asset Register

All information assets shall be inventoried in the Asset Register (`iso27001/asset-register/`) and classified according to sensitivity.

### 5.2 Information Classification

| Classification | Description | Handling Requirements |
|---------------|-------------|----------------------|
| **Public** | Information approved for public disclosure | No restrictions |
| **Internal** | Information for general internal use | Not for external distribution |
| **Confidential** | Sensitive business or personal data | Encrypted; need-to-know access |
| **Restricted** | Highly sensitive — special category data, credentials, financial | Encrypted at rest and in transit; field-level protection; MFA access |

### 5.3 Acceptable Use

All personnel shall comply with the Acceptable Use Policy. Information assets shall be used only for legitimate business purposes and in accordance with their classification.

---

## 6. Access Control

### 6.1 Access Control Principles

- **Least privilege:** Access granted only to the minimum required for job function
- **Need-to-know:** Access to confidential/restricted data requires documented business justification
- **Segregation of duties:** Critical operations require multiple authorised individuals
- **Default deny:** All access is denied unless explicitly granted

### 6.2 User Access Management

- All access requests shall be approved by the user's manager and the system owner
- Privileged access requires additional approval from the CISO or ISMS Manager
- Access shall be reviewed quarterly and revoked for inactive accounts (>90 days)
- Access shall be removed within 24 hours of employment termination

### 6.3 Authentication

- Multi-factor authentication (MFA) is mandatory for all production and administrative systems
- Passwords shall meet minimum requirements: ≥12 characters, complexity enforced
- Service accounts shall use certificate-based or key-based authentication with regular rotation

### 6.4 Multi-Tenant Access Isolation

- Each tenant's data shall be logically isolated using [schema separation / row-level security / tenant ID enforcement]
- Cross-tenant access shall be technically prevented and logged as a security event if attempted
- Tenant administrators shall only access their own tenant's data and configuration

---

## 7. Cryptography and Data Protection

### 7.1 Encryption Requirements

| Data State | Requirement |
|-----------|-------------|
| **In transit** | TLS 1.2 minimum (TLS 1.3 preferred) for all data in transit |
| **At rest** | AES-256 encryption for all stored personal data and confidential information |
| **Field-level** | Application-level encryption for special category data (GDPR Art. 9) |
| **Backups** | Encrypted using AES-256; keys managed separately from encrypted data |

### 7.2 Key Management

- Cryptographic keys shall be generated, stored, and rotated in accordance with the Key Management Procedure
- Keys shall be stored in a dedicated key management service (e.g. AWS KMS, HashiCorp Vault)
- Key rotation shall occur at least annually or upon compromise suspicion

---

## 8. Physical Security

- Physical access to data centres shall be managed by the hosting provider under SOC 2 Type II certified controls
- Office premises shall be secured with badge access and visitor logging
- Remote workers shall secure devices with full-disk encryption and lock screens when unattended
- Equipment containing data shall be securely wiped (NIST 800-88) before disposal or re-use

---

## 9. Operations Security

### 9.1 Change Management

All changes to production systems shall follow the documented change management process:

1. Change request submitted and documented
2. Impact assessment completed (security, availability, data protection)
3. Approved by change advisory board or designated approver
4. Implemented through CI/CD pipeline with automated testing
5. Post-implementation review for significant changes

### 9.2 Vulnerability Management

| Activity | Frequency | SLA |
|----------|-----------|-----|
| Automated vulnerability scanning | Weekly | — |
| Penetration testing (external) | Annually | — |
| Critical vulnerability patching | As needed | ≤ 24 hours |
| High vulnerability patching | As needed | ≤ 7 days |
| Medium vulnerability patching | As needed | ≤ 30 days |

### 9.3 Logging and Monitoring

- All access to production systems shall be logged with immutable audit trails
- Logs shall be retained for a minimum of 12 months (or longer per regulatory requirement)
- Security events shall be monitored and alerted in real-time
- Log integrity shall be protected; tampering shall trigger an immediate alert

### 9.4 Backup and Recovery

- Automated daily backups of all production data
- Backups tested for restore integrity quarterly
- Recovery Point Objective (RPO): [e.g. 1 hour]
- Recovery Time Objective (RTO): [e.g. 4 hours]

---

## 10. Incident Management

### 10.1 Incident Response

All security incidents shall be managed in accordance with the Incident Response Plan:

1. **Detection** — Identify and classify the security event
2. **Containment** — Limit the scope and impact
3. **Eradication** — Remove the root cause
4. **Recovery** — Restore affected systems
5. **Lessons learned** — Document and improve controls

### 10.2 Notification Requirements

| Scenario | Notification Target | SLA |
|----------|-------------------|-----|
| Personal data breach (GDPR) | Supervisory authority (e.g. VDAI, DVI, AKI) | ≤ 72 hours |
| Personal data breach — high risk | Affected data subjects | Without undue delay |
| SOC 2 relevant incident | Audit firm, affected customers | Per contractual terms |
| Tenant data breach | Affected tenant (controller) | ≤ 24 hours |

---

## 11. Supplier and Third-Party Security

- All suppliers with access to [Company Name] data shall be subject to security due diligence
- Data Processing Agreements (DPAs) compliant with GDPR Art. 28 shall be executed with all processors
- Supplier security shall be reviewed annually (see `vendor-register/`)
- Sub-processor changes shall be communicated to controllers with ≥30 days' notice

---

## 12. Business Continuity

- A Business Continuity Plan (BCP) and Disaster Recovery (DR) Plan shall be maintained
- DR plans shall be tested at least annually
- ICT readiness for business continuity shall be assessed against maximum tolerable downtime

---

## 13. Compliance

### 13.1 Regulatory Compliance

| Regulation | Key Obligations | Responsible |
|-----------|----------------|-------------|
| GDPR | ROPA, DPIA, DSR handling, breach notification, DPO appointment | DPO |
| ISO 27001:2022 | ISMS maintenance, risk assessment, SoA, internal audit | ISMS Manager |
| SOC 2 Type II | Control operation evidence, annual audit | CISO |
| ePrivacy Directive | Cookie consent, electronic marketing | DPO / Legal |
| National laws (LT/LV/EE) | Country-specific data protection requirements | Country compliance leads |

### 13.2 Internal Audit

- Internal audits shall be conducted at least annually covering all ISMS clauses and Annex A controls
- Audit findings shall be tracked, remediated, and reported to management
- Nonconformities shall be addressed through the corrective action process

### 13.3 Management Review

Management shall review the ISMS at least annually, considering:

- Audit results and compliance status
- Security incidents and trends
- Risk assessment outcomes
- Feedback from interested parties
- Opportunities for improvement

---

## 14. Personnel Security

- All personnel shall undergo background screening appropriate to their role
- Security awareness training shall be completed within 30 days of onboarding and annually thereafter
- Personnel shall acknowledge their security responsibilities in writing
- Disciplinary action may be taken against personnel who violate this policy

---

## 15. Policy Enforcement

- Violations of this policy may result in disciplinary action, up to and including termination of employment or contract
- Exceptions must be documented, risk-assessed, and approved by the CISO
- The CISO has the authority to suspend access immediately in case of suspected policy violation

---

## 16. Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| [1.0] | [YYYY-MM-DD] | [Name] | Initial policy creation |
| | | | |

---

## 17. Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| CISO / Policy Owner | [Name] | [Date] | _________________ |
| Data Protection Officer | [DPO Name] | [Date] | _________________ |
| Executive Sponsor | [Name] | [Date] | _________________ |

---

## 18. Related Documents

| Document | Location |
|----------|----------|
| Acceptable Use Policy | `iso27001/policies/acceptable-use-policy.md` |
| Access Control Policy | `iso27001/policies/access-control-policy.md` |
| Incident Response Plan | `iso27001/procedures/incident-response.md` |
| Risk Register | `iso27001/risk-register/risk-register-template.md` |
| Statement of Applicability | `iso27001/soa/soa-template.md` |
| GDPR ROPA | `gdpr/ropa/ropa-template.md` |
| GDPR DPIA | `gdpr/dpias/dpia-template.md` |
| SOC 2 CC6 Evidence | `soc2/evidence/cc6/access-control-evidence-template.md` |
| Vendor Register | `vendor-register/` |
| Compliance Checklist | `docs/compliance-checklist.md` |

---

*This Information Security Policy is the governing document for the ISMS at [Company Name]. It is reviewed at least annually and updated to reflect changes in the threat landscape, regulatory environment, and organisational structure. All personnel are required to read, understand, and comply with this policy.*

# SOC 2 Type II — Trust Services Criteria Control Mapping

**Journey Of Life UAB — TSC to Control Cross-Reference**

| Field | Value |
|-------|-------|
| **Document ID** | JOL-SOC2-TSC-2026 |
| **Organisation** | Journey Of Life UAB |
| **Standard** | AICPA Trust Services Criteria (2017, updated 2022) |
| **Audit Period** | [Start Date] to [End Date] |
| **Mapping Owner** | [CISO Name] |
| **Version** | 1.0 |
| **Classification** | Internal — Confidential |

---

## 1. Common Criteria (CC1–CC9)

### CC1: Control Environment

| TSC Point of Focus | Control Description | Policy/Procedure | Evidence |
|-------------------|-------------------|-----------------|---------|
| CC1.1 Integrity and ethical values | Code of conduct communicated and enforced | HR Handbook | Signed acknowledgments |
| CC1.2 Board independence and oversight | Board reviews ISMS performance quarterly | ISMS Management Review | Board minutes |
| CC1.3 Management commitment to attract and retain competent individuals | Hiring, screening, and training processes | HR Policy | Background check records, training completion |
| CC1.4 Accountability | Security responsibilities in job descriptions and performance reviews | HR Policy | Job descriptions, performance reviews |

### CC2: Communication and Information

| TSC Point of Focus | Control Description | Policy/Procedure | Evidence |
|-------------------|-------------------|-----------------|---------|
| CC2.1 Information quality | Data quality controls and validation | Data Classification Policy | Data quality reports |
| CC2.2 Internal communication | Security policies communicated to all personnel | InfoSec Policy | Communication records |
| CC2.3 External communication | Security commitments communicated to customers | DPA, Privacy Policies | Published policies |

### CC3: Risk Assessment

| TSC Point of Focus | Control Description | Policy/Procedure | Evidence |
|-------------------|-------------------|-----------------|---------|
| CC3.1 Risk identification | Annual risk assessment covering ISMS scope | Risk Register | `iso27001/risk-register/` |
| CC3.2 Fraud risk assessment | Risk register includes fraud-related risks | Risk Register | Risk entries |
| CC3.3 Risk response | Risk treatment plans with owners and deadlines | Risk Register | Treatment tracker |
| CC3.4 Change risk assessment | Change impact assessments for significant changes | Change Management | Change records |

### CC4: Monitoring Activities

| TSC Point of Focus | Control Description | Policy/Procedure | Evidence |
|-------------------|-------------------|-----------------|---------|
| CC4.1 Ongoing monitoring | SIEM, automated alerts, KPI dashboards | ISMS Policy Section 9 | SIEM dashboards |
| CC4.2 Separate evaluations | Internal and external audits | Internal Audit Template | Audit reports |

### CC5: Control Activities

| TSC Point of Focus | Control Description | Policy/Procedure | Evidence |
|-------------------|-------------------|-----------------|---------|
| CC5.1 Selection of control activities | Controls selected based on risk assessment | SoA, Risk Register | SoA document |
| CC5.2 Technology controls | Automated controls in CI/CD, access management | Access Control Procedure | System configurations |
| CC5.3 Policies and procedures | Documented policies for all control areas | Policy documents | Compliance repository |

### CC6: Logical and Physical Access Controls

| TSC Point of Focus | Control Description | Policy/Procedure | Evidence |
|-------------------|-------------------|-----------------|---------|
| CC6.1 Access infrastructure | Authentication and authorisation infrastructure | Access Control Procedure | `soc2/evidence/cc6/` |
| CC6.2 User registration | Identity proofing and account provisioning | Access Control Procedure | Provisioning records |
| CC6.3 Unique identification | Unique IDs for all users; no shared accounts | Access Control Procedure | User directory |
| CC6.4 Credential management | Password policy, MFA enforcement | Password Policy | MFA logs |
| CC6.5 Access provisioning | RBAC, least privilege, approval workflow | Access Control Procedure | Access request logs |
| CC6.6 Access modification | Role changes trigger access review | Access Control Procedure | Modification records |
| CC6.7 Access removal | Automated deprovisioning within 24 hours | Access Control Procedure | Deprovisioning logs |
| CC6.8 Physical access | Badge access, visitor management | ISMS Policy Section 8 | Access logs |

### CC7: System Operations

| TSC Point of Focus | Control Description | Policy/Procedure | Evidence |
|-------------------|-------------------|-----------------|---------|
| CC7.1 Infrastructure management | Managed infrastructure with monitoring | ISMS Policy Section 9 | `soc2/evidence/cc7/` |
| CC7.2 Vulnerability management | Scanning, patching, and remediation | Vulnerability Management | Scan reports |
| CC7.3 Incident detection | SIEM alerting and correlation | Incident Response Policy | SIEM alerts |
| CC7.4 Incident response | Defined IR process with SLAs | Incident Response Playbook | Incident records |
| CC7.5 Incident recovery | Backup restore, system recovery procedures | Backup & Recovery Policy | Restore test results |

### CC8: Change Management

| TSC Point of Focus | Control Description | Policy/Procedure | Evidence |
|-------------------|-------------------|-----------------|---------|
| CC8.1 Change authorisation | Code review, approval gates in CI/CD | Change Management | PR approvals |
| CC8.2 Change documentation | Changes tracked in version control | Change Management | Git commit history |
| CC8.3 Change testing | Automated tests in CI/CD pipeline | SDLC | Test results |
| CC8.4 Change approval | Production deployments require approval | Change Management | Deployment approvals |

### CC9: Risk Mitigation

| TSC Point of Focus | Control Description | Policy/Procedure | Evidence |
|-------------------|-------------------|-----------------|---------|
| CC9.1 Risk mitigation activities | Risk treatment plans per risk register | Risk Register | Treatment tracker |
| CC9.2 Vendor management | Supplier security assessments and DPAs | Vendor Register | `vendor-register/` |

---

## 2. Additional Criteria

### A1: Availability

| TSC Point of Focus | Control Description | Policy/Procedure | Evidence |
|-------------------|-------------------|-----------------|---------|
| A1.1 Availability commitment | SLA with ≥99.9% uptime target | SLA Agreements | Availability reports |
| A1.2 Capacity management | Monitoring, auto-scaling, capacity planning | ISMS Policy Section 9 | Capacity reports |
| A1.3 Incident response for availability | Availability incidents in IR process | Incident Response Policy | Incident records |
| A1.4 Recovery procedures | BCP, DR plan, annual testing | Backup & Recovery Policy | DR test results |
| A1.5 Redundancy | Multi-region failover architecture | ISMS Policy Section 8 | Architecture diagrams |

### C1: Confidentiality

| TSC Point of Focus | Control Description | Policy/Procedure | Evidence |
|-------------------|-------------------|-----------------|---------|
| C1.1 Confidentiality requirements | Data classification with Confidential level | Data Classification Policy | Classification records |
| C1.2 Confidentiality protections | Encryption at rest and in transit | Encryption Policy | Encryption configs |
| C1.3 Confidentiality destruction | Secure deletion per retention policy | Data Retention Policy | Deletion logs |

### P1: Privacy

| TSC Point of Focus | Control Description | Policy/Procedure | Evidence |
|-------------------|-------------------|-----------------|---------|
| P1.1 Privacy notice | Privacy policies for each jurisdiction | Privacy Policies (LT/LV/EE) | `gdpr/privacy-policies/` |
| P1.2 Choice and consent | Consent management and preference centre | Cookie Policy | Consent records |
| P1.3 Data collection | Lawful basis for all processing | ROPA | `gdpr/ropa/` |
| P1.4 Use and retention | Retention schedules per data type | Data Retention Policy | `gdpr/retention-policies/` |
| P1.5 Access | Data subject access requests | DSR Procedure | `gdpr/dsr-procedures/` |
| P1.6 Disclosure to third parties | DPAs with all processors | Vendor Register | Signed DPAs |
| P1.7 Data quality | Accuracy controls for personal data | DSR Procedure (rectification) | Rectification records |
| P1.8 Monitoring and enforcement | DPO oversight, compliance monitoring | DPO Reports | Monitoring records |

---

## 3. Control Coverage Summary

| Criteria | Points of Focus | Controls Mapped | Coverage |
|----------|----------------|----------------|---------|
| CC1–CC9 (Common) | [X] | [X] | 100% |
| A1 (Availability) | 5 | 5 | 100% |
| C1 (Confidentiality) | 3 | 3 | 100% |
| P1 (Privacy) | 8 | 8 | 100% |
| **Total** | **[X]** | **[X]** | **100%** |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [YYYY-MM-DD] | [CISO Name] | Initial TSC mapping |

---

*This document maps the AICPA Trust Services Criteria (2017, updated 2022) to the controls implemented by Journey Of Life UAB for SOC 2 Type II audit purposes. It is updated annually or when significant changes to the control environment occur.*

# Statement of Applicability (SoA)

**ISO/IEC 27001:2022 — Statement of Applicability for Journey Of Life UAB**

| Field | Value |
|-------|-------|
| **Document ID** | JOL-ISMS-SOA-2026 |
| **Organisation** | Journey Of Life UAB |
| **ISMS Reference** | Clause 6.1.3(d) |
| **SoA Owner** | [CISO Name] |
| **Version** | 1.0 |
| **Effective Date** | [YYYY-MM-DD] |
| **Last Reviewed** | [YYYY-MM-DD] |
| **Next Review Due** | [YYYY-MM-DD] |
| **Classification** | Internal — Confidential |

---

## 1. Introduction

This Statement of Applicability identifies which of the 93 Annex A controls from ISO/IEC 27001:2022 are applicable to the Journey Of Life ISMS scope, provides justification for inclusion/exclusion, and describes the implementation status of each applicable control.

**Total Annex A controls:** 93 across 4 themes  
**Applicable:** [X]  
**Not applicable:** [X]

**Legend:** A = Applicable, N/A = Not applicable, Implemented (I), Partially implemented (P), Planned (PL)

---

## 2. A.5 Organisational Controls (37 controls)

| Ref | Control | Applicable | Justification | Status | Evidence |
|-----|---------|-----------|--------------|--------|---------|
| A.5.1 | Policies for information security | A | Core ISMS requirement | I | `iso27001/policies/` |
| A.5.2 | Information security roles and responsibilities | A | Defined in ISMS policy | I | ISMS policy Section 3 |
| A.5.3 | Segregation of duties | A | Dev/test/prod segregation | I | Access control procedure |
| A.5.4 | Management responsibilities | A | Board and management oversight | I | Management review minutes |
| A.5.5 | Contact with authorities | A | Supervisory authority contacts defined | I | DSR procedure, incident response |
| A.5.6 | Contact with special interest groups | A | ISACA, ENISA memberships | I | Membership records |
| A.5.7 | Threat intelligence | A | Industry threat feeds and advisories | I | Threat intel subscription records |
| A.5.8 | Information security in project management | A | Security requirements in SDLC | I | SDLC documentation |
| A.5.9 | Inventory of information and other associated assets | A | Asset register maintained | I | `iso27001/asset-register/` |
| A.5.10 | Acceptable use of information and other associated assets | A | Acceptable use policy in place | I | `security-policies/acceptable-use-policy.md` |
| A.5.11 | Return of assets | A | Defined in HR offboarding | I | Asset register Section 6 |
| A.5.12 | Classification of information | A | 4-level classification scheme | I | `security-policies/data-classification-policy.md` |
| A.5.13 | Labelling of information | A | Classification labels applied | I | Data classification policy |
| A.5.14 | Information transfer | A | Encryption in transit; secure transfer rules | I | Encryption policy |
| A.5.15 | Access control | A | RBAC, least privilege | I | Access control procedure |
| A.5.16 | Identity management | A | Unique IDs, SSO | I | Access control procedure |
| A.5.17 | Authentication information | A | MFA, password policy | I | Password policy |
| A.5.18 | Access rights | A | Lifecycle management, quarterly review | I | Access control procedure |
| A.5.19 | Information security in supplier relationships | A | Vendor security assessment | I | Vendor register |
| A.5.20 | Addressing information security within supplier agreements | A | Art. 28 DPAs, security clauses | I | DPA template |
| A.5.21 | Managing information security in the ICT supply chain | A | Supply chain risk assessment | P | Risk register R-2026-009 |
| A.5.22 | Monitoring, review, and change management of supplier services | A | Annual vendor reviews | I | Vendor review template |
| A.5.23 | Information security for use of cloud services | A | Cloud security requirements defined | I | Cloud provider assessment |
| A.5.24 | Information security incident management planning and preparation | A | Incident response plan | I | Incident response policy |
| A.5.25 | Assessment and decision on information security events | A | Event classification and assessment | I | Incident response playbook |
| A.5.26 | Response to information security incidents | A | Defined response procedures | I | Incident response playbook |
| A.5.27 | Learning from information security incidents | A | Post-incident reviews | I | Incident records |
| A.5.28 | Collection of evidence | A | Forensic evidence procedures | I | Incident response playbook |
| A.5.29 | Information security during disruption | A | BCP and DR plan | I | Business continuity plan |
| A.5.30 | ICT readiness for business continuity | A | Redundancy and failover architecture | I | DR plan |
| A.5.31 | Legal, statutory, regulatory and contractual requirements | A | Compliance matrix maintained | I | Country-specific docs |
| A.5.32 | Intellectual property rights | A | License compliance, open-source policy | I | SBOM, license records |
| A.5.33 | Protection of records | A | Immutable audit logs | I | Audit log configuration |
| A.5.34 | Privacy and protection of personally identifiable information | A | GDPR compliance programme | I | `gdpr/` directory |
| A.5.35 | Independent review of information security | A | Annual external penetration test | I | Pen test reports |
| A.5.36 | Compliance with policies, rules and standards for information security | A | Compliance validation tool | I | `compliance_validator.py` |
| A.5.37 | Documented operating procedures | A | Procedures documented and maintained | I | Procedures directory |

---

## 3. A.6 People Controls (8 controls)

| Ref | Control | Applicable | Justification | Status | Evidence |
|-----|---------|-----------|--------------|--------|---------|
| A.6.1 | Screening | A | Background checks for all employees | I | HR records |
| A.6.2 | Terms and conditions of employment | A | Security clauses in contracts | I | Employment contract templates |
| A.6.3 | Information security awareness, education and training | A | Onboarding + annual training | I | LMS records |
| A.6.4 | Disciplinary process | A | Policy violation procedures defined | I | HR handbook |
| A.6.5 | Responsibilities after termination or change of employment | A | Offboarding checklist | I | HR offboarding procedure |
| A.6.6 | Confidentiality or non-disclosure agreements | A | NDAs for all staff and contractors | I | Signed NDA records |
| A.6.7 | Remote working | A | Remote work security policy | I | `security-policies/remote-work-security-policy.md` |
| A.6.8 | Information security event reporting | A | Reporting channels defined | I | Incident response policy |

---

## 4. A.7 Physical Controls (14 controls)

| Ref | Control | Applicable | Justification | Status | Evidence |
|-----|---------|-----------|--------------|--------|---------|
| A.7.1 | Physical security perimeters | A | Office access controls | I | Facilities records |
| A.7.2 | Physical entry | A | Badge access, visitor log | I | Access control logs |
| A.7.3 | Securing offices and facilities | A | Locked cabinets, clean desk policy | I | Acceptable use policy |
| A.7.4 | Physical security monitoring | A | CCTV in office areas | I | CCTV records |
| A.7.5 | Protecting against physical and environmental threats | A | Fire suppression, climate control | I | Facilities records |
| A.7.6 | Working in secure areas | A | Restricted area access rules | I | Access control procedure |
| A.7.7 | Clear desk and clear screen | A | Clear desk policy in acceptable use | I | Acceptable use policy |
| A.7.8 | Equipment siting | A | Screen positioning guidelines | I | Remote work policy |
| A.7.9 | Security of assets off-premises | A | Remote device security requirements | I | Remote work policy |
| A.7.10 | Storage media | A | Encrypted portable media | I | Encryption policy |
| A.7.11 | Supporting utilities | A | UPS and generator for office | I | Facilities records |
| A.7.12 | Cabling security | A | Cable management standards | I | Facilities records |
| A.7.13 | Equipment maintenance | A | Maintenance contracts and logs | I | Maintenance records |
| A.7.14 | Secure disposal or re-use of equipment | A | NIST 800-88 compliant disposal | I | Disposal certificates |

---

## 5. A.8 Technological Controls (34 controls)

| Ref | Control | Applicable | Justification | Status | Evidence |
|-----|---------|-----------|--------------|--------|---------|
| A.8.1 | User endpoint devices | A | Endpoint management and protection | I | Endpoint protection records |
| A.8.2 | Privileged access rights | A | PAM with session recording | I | PAM logs |
| A.8.3 | Restriction of information access | A | Need-to-know enforcement | I | Access control procedure |
| A.8.4 | Access to source code | A | Repository access control | I | GitHub access controls |
| A.8.5 | Secure authentication | A | MFA for all critical systems | I | MFA configuration |
| A.8.6 | Capacity management | A | Monitoring and auto-scaling | I | Capacity reports |
| A.8.7 | Protection against malware | A | Endpoint protection and server AV | I | AV deployment records |
| A.8.8 | Management of technical vulnerabilities | A | Vulnerability scanning + patching | I | Vulnerability scan reports |
| A.8.9 | Configuration management | A | IaC and baseline configurations | I | Configuration repository |
| A.8.10 | Information deletion | A | Secure deletion procedures | I | Data retention policy |
| A.8.11 | Data masking | A | PII masking in non-production | I | Environment provisioning docs |
| A.8.12 | Data leakage prevention | A | DLP for privileged users | P | DLP deployment records |
| A.8.13 | Information backup | A | Automated encrypted backups | I | Backup logs |
| A.8.14 | Redundancy of information processing facilities | A | Multi-region failover | I | DR test results |
| A.8.15 | Logging | A | Comprehensive logging | I | Log management platform |
| A.8.16 | Monitoring activities | A | SIEM with alerting | I | SIEM configuration |
| A.8.17 | Clock synchronisation | A | NTP for all systems | I | NTP configuration |
| A.8.18 | Use of privileged utility software | A | Restricted admin tools | I | Access control records |
| A.8.19 | Installation of software on operational systems | A | Change management required | I | Change management records |
| A.8.20 | Networks security | A | Network segmentation, firewalls | I | Network diagrams, firewall rules |
| A.8.21 | Security of network services | A | TLS, VPN, network access control | I | Network configuration |
| A.8.22 | Segregation of networks | A | Dev/test/prod network isolation | I | Network architecture |
| A.8.23 | Web filtering | A | Outbound web filtering | I | Web filter configuration |
| A.8.24 | Use of cryptography | A | AES-256, TLS 1.2+, field-level encryption | I | Encryption policy |
| A.8.25 | Secure development life cycle | A | Secure SDLC with security gates | I | SDLC documentation |
| A.8.26 | Application security requirements | A | OWASP requirements, threat modelling | I | Security requirements doc |
| A.8.27 | Secure system architecture and engineering principles | A | Defence in depth, zero trust | I | Architecture documentation |
| A.8.28 | Secure coding | A | Code review, SAST, secure coding standards | I | Code review records |
| A.8.29 | Security testing in development and acceptance | A | SAST, DAST, penetration testing | I | Test results |
| A.8.30 | Outsourced development | A | Security requirements for contractors | I | Contractor agreements |
| A.8.31 | Separation of development, test and production environments | A | Environment segregation | I | Environment access controls |
| A.8.32 | Change management | A | CI/CD with approval gates | I | Change management records |
| A.8.33 | Test information | A | Masked test data | I | Test data management |
| A.8.34 | Protection of information systems during audit testing | A | Read-only audit access | I | Audit access procedures |

---

## 6. Controls Not Applicable

| Ref | Control | Reason for Exclusion |
|-----|---------|---------------------|
| — | — | All 93 controls are considered applicable for the Journey Of Life ISMS scope |

*Note: The organisation has determined that all 93 Annex A controls are applicable given the scope of the ISMS covering a multi-tenant SaaS platform processing personal data and special category data for ~400,000 religious institutions.*

---

## 7. SoA Summary

| Theme | Total Controls | Applicable | Implemented | Partially | Planned |
|-------|--------------|-----------|------------|----------|---------|
| A.5 Organisational | 37 | 37 | [X] | [X] | 0 |
| A.6 People | 8 | 8 | [X] | 0 | 0 |
| A.7 Physical | 14 | 14 | [X] | 0 | 0 |
| A.8 Technological | 34 | 34 | [X] | [X] | 0 |
| **Total** | **93** | **93** | **[X]** | **[X]** | **0** |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [YYYY-MM-DD] | [CISO Name] | Initial SoA for ISO 27001:2022 certification |

---

## Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| CISO | [Name] | [Date] | _________________ |
| ISMS Manager | [Name] | [Date] | _________________ |

---

*This Statement of Applicability covers all 93 controls in ISO/IEC 27001:2022 Annex A as applied to the Journey Of Life UAB ISMS. It is reviewed annually and updated to reflect changes in the ISMS scope, risk assessment results, or organisational context.*

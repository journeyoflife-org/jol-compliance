# Vendor Register — Master

**Journey Of Life UAB — Sub-Processor and Vendor Register (GDPR Art. 28)**

| Field | Value |
|-------|-------|
| **Document ID** | JOL-VR-001 |
| **Organisation** | Journey Of Life UAB |
| **Register Owner** | [DPO Name] — duomenu.apsauga@jol-hub.com |
| **Version** | 1.0 |
| **Last Updated** | [YYYY-MM-DD] |
| **Next Review** | [YYYY-MM-DD] |
| **Classification** | Internal — Confidential |

---

## 1. Sub-Processor Register (GDPR Art. 28)

### 1.1 Infrastructure and Hosting

| # | Vendor | Service | Data Processed | Processing Location | Transfer Mechanism | DPA Signed | SOC 2 / ISO 27001 | Risk Level |
|---|--------|---------|---------------|-------------------|------------------|-----------|------------------|-----------|
| 1 | [Cloud Provider] | Cloud hosting, compute, storage | Tenant data, platform data | EU-West | N/A (EU) | ☐ | [Certification] | High |
| 2 | [CDN Provider] | Content delivery, DDoS protection | Public content, IP addresses | EU PoPs | N/A (EU) | ☐ | [Certification] | Medium |
| 3 | [Backup Provider] | Off-site backup storage | Encrypted backups | EU-Central | N/A (EU) | ☐ | [Certification] | High |

### 1.2 SaaS and Productivity

| # | Vendor | Service | Data Processed | Processing Location | Transfer Mechanism | DPA Signed | SOC 2 / ISO 27001 | Risk Level |
|---|--------|---------|---------------|-------------------|------------------|-----------|------------------|-----------|
| 4 | [Email Provider] | Corporate email | Employee email | EU | N/A | ☐ | [Certification] | Medium |
| 5 | [Collaboration Tool] | Messaging, video | Employee communications | EU/US | EU-US DPF | ☐ | [Certification] | Medium |
| 6 | [HR System] | Employee records | Employee personal data | EU | N/A | ☐ | [Certification] | High |

### 1.3 Development and Security

| # | Vendor | Service | Data Processed | Processing Location | Transfer Mechanism | DPA Signed | SOC 2 / ISO 27001 | Risk Level |
|---|--------|---------|---------------|-------------------|------------------|-----------|------------------|-----------|
| 7 | GitHub | Code hosting, CI/CD | Source code, configurations | US | EU-US DPF / SCCs | ☐ | SOC 2 Type II | Medium |
| 8 | [Monitoring Provider] | Infrastructure monitoring | System metrics, logs | EU | N/A | ☐ | [Certification] | Medium |
| 9 | [SIEM Provider] | Security monitoring | Security events | EU | N/A | ☐ | [Certification] | High |
| 10 | [Pen Test Firm] | Penetration testing | Test environment data | EU | N/A | ☐ | [Certification] | Low |

### 1.4 Analytics and Marketing

| # | Vendor | Service | Data Processed | Processing Location | Transfer Mechanism | DPA Signed | Risk Level |
|---|--------|---------|---------------|-------------------|------------------|-----------|-----------|
| 11 | Google Analytics | Web analytics | Anonymised usage data | US | EU-US DPF | ☐ | Low |
| 12 | [Payment Processor] | Payment processing | Payment data | EU | N/A | ☐ | High |

---

## 2. DPA Compliance Tracker

| Vendor # | DPA Status | DPA Date | Sub-processor Clause | Breach Notification | Audit Rights | Data Return/Deletion |
|----------|-----------|---------|---------------------|-------------------|-------------|-------------------|
| 1 | ☐ Signed ☐ Pending | [Date] | ☐ | ☐ ≤48h | ☐ | ☐ |
| 2 | | | | | | |

---

## 3. Vendor Onboarding Checklist

- [ ] Security questionnaire completed
- [ ] DPA reviewed and signed (GDPR Art. 28)
- [ ] Data processing locations confirmed (EU only preferred)
- [ ] International transfer mechanism identified (if non-EU)
- [ ] SOC 2 / ISO 27001 certification verified
- [ ] Sub-processor notification clause included
- [ ] Data breach notification SLA agreed (≤48 hours)
- [ ] Data return/deletion clause included
- [ ] Risk assessment completed (see `scripts/vendor_risk_calculator.py`)
- [ ] Added to vendor register
- [ ] Controller notification (if sub-processor): 30-day advance notice

---

## 4. Annual Review Schedule

| Quarter | Vendors to Review | Review Focus |
|---------|-----------------|-------------|
| Q1 (Jan) | Infrastructure and hosting vendors | Certification renewal, audit findings |
| Q2 (Apr) | SaaS and productivity vendors | DPA compliance, data handling |
| Q3 (Jul) | Development and security vendors | Access review, security posture |
| Q4 (Oct) | Analytics and marketing vendors | Cookie consent, data minimisation |

Review template: `soc2/vendor-reviews/vendor-compliance-review-template.md`

---

## 5. Sub-Processor Change Notification

When adding or changing sub-processors, Journey Of Life will:
1. Notify all tenant controllers at least **30 days** before the change takes effect
2. Provide details of the new sub-processor, service, and data processed
3. Allow controllers to object within the notification period
4. If a controller objects: negotiate alternatives or allow contract termination
5. Update this register and publish the change

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [YYYY-MM-DD] | [DPO Name] | Initial vendor register |

---

*This Vendor Register maintains the list of all sub-processors and vendors with access to Journey Of Life data, in compliance with GDPR Art. 28 and ISO 27001 A.5.19–A.5.22. It is reviewed annually and updated whenever vendor relationships change.*

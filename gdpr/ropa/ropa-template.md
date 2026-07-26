# Record of Processing Activities (ROPA)

**GDPR Article 30 — Record of Processing Activities**

| Field | Value |
|-------|-------|
| **Organisation** | [Company Name] |
| **Registration Number** | [Company Registration Number] |
| **Registered Address** | [Company Address] |
| **Data Protection Officer** | [DPO Name] — [DPO Email] |
| **EU Representative (if applicable)** | [EU Representative Name] — [EU Representative Address] |
| **Document Owner** | [Document Owner Name/Role] |
| **Version** | [Version Number] |
| **Effective Date** | [YYYY-MM-DD] |
| **Last Reviewed** | [YYYY-MM-DD] |
| **Next Review Due** | [YYYY-MM-DD] |
| **Classification** | Internal — Confidential |

---

## 1. Controller Processing Activities

### 1.1 Processing Activity Register

| Ref. | Activity Name | Purpose of Processing | Legal Basis (Art. 6) | Special Category Basis (Art. 9) | Data Categories | Data Subject Categories | Recipient Categories | Third-Country Transfers | Retention Period | Technical & Organisational Measures |
|------|--------------|----------------------|---------------------|-------------------------------|----------------|------------------------|---------------------|------------------------|-----------------|-------------------------------------|
| PA-001 | [e.g. User Account Management] | [e.g. Provision of platform access] | [e.g. Art. 6(1)(b) — Contract performance] | [N/A or Art. 9(2)(a)/(d)] | [e.g. Name, email, role, credentials] | [e.g. Platform administrators, clergy members] | [e.g. Cloud hosting provider, payment processor] | [N/A or specify country + safeguard] | [e.g. Account lifetime + 24 months] | [e.g. Encryption at rest, RBAC, MFA] |
| PA-002 | | | | | | | | | | |
| PA-003 | | | | | | | | | | |

### 1.2 Legal Basis Mapping

| Processing Activity | Primary Legal Basis | Condition Met | Justification |
|--------------------|---------------------|---------------|---------------|
| PA-001 | Art. 6(1)(b) — Contract | ☐ Consent ☐ Contract ☐ Legal obligation ☐ Vital interests ☐ Public interest ☐ Legitimate interests | [Brief justification] |
| PA-002 | | | |
| PA-003 | | | |

---

## 2. Processor Processing Activities

*(Complete this section if [Company Name] acts as a data processor on behalf of controllers — e.g., parish dioceses, religious organisations.)*

| Ref. | Controller Name & Contact | Processing Activity | Data Categories | Data Subject Categories | Sub-Processors | Third-Country Transfers | Technical & Organisational Measures |
|------|--------------------------|---------------------|----------------|------------------------|----------------|------------------------|-------------------------------------|
| PR-001 | [e.g. Diocese of X] | [e.g. Member management] | | | [e.g. AWS EU-West, Stripe] | | |
| PR-002 | | | | | | | |

---

## 3. Data Categories Reference

| Code | Category | Description | Sensitivity |
|------|----------|-------------|-------------|
| DC-01 | Identity Data | Full name, date of birth, national ID | Standard |
| DC-02 | Contact Data | Email, phone, postal address | Standard |
| DC-03 | Authentication Data | Password hashes, MFA tokens | Standard |
| DC-04 | Religious Affiliation | Denomination, parish membership, clergy status | **Special Category (Art. 9)** |
| DC-05 | Financial Data | Donation records, payment details, tax IDs | Standard (heightened risk) |
| DC-06 | Communication Data | Messages, prayer requests, counselling notes | **Special Category (Art. 9)** |
| DC-07 | Children's Data | Sunday school records, youth group participation | **Heightened protection required** |
| DC-08 | Technical Data | IP addresses, device identifiers, access logs | Standard |
| DC-09 | | | |
| DC-10 | | | |

---

## 4. Data Subject Categories

| Code | Category | Description |
|------|----------|-------------|
| DS-01 | Clergy | Priests, pastors, ministers, imams, rabbis |
| DS-02 | Lay Administrators | Parish staff, diocesan employees |
| DS-03 | Congregation Members | Registered parishioners and community members |
| DS-04 | Children & Minors | Under-18 participants in religious education |
| DS-05 | Donors | Financial contributors |
| DS-06 | Third-Party Contacts | Vendors, external partners |
| DS-07 | | |

---

## 5. Recipient & Third-Party Disclosures

| Recipient | Category | Data Shared | Legal Basis | DPA in Place | Location |
|-----------|----------|-------------|-------------|-------------|----------|
| [e.g. AWS EMEA] | Cloud hosting provider | All platform data | Art. 28 Processor | ☐ Yes ☐ No | EU-West |
| [e.g. Stripe] | Payment processor | Financial data | Art. 28 Processor | ☐ Yes ☐ No | EU |
| [e.g. SendGrid] | Email service | Contact data | Art. 28 Processor | ☐ Yes ☐ No | EU (with SCCs) |
| | | | | | |

---

## 6. International Data Transfers

| Destination Country | Recipient | Data Categories | Transfer Mechanism | Safeguards | Adequacy Decision |
|-------------------|-----------|----------------|--------------------|------------|--------------------|
| [e.g. United States] | [Provider name] | [Categories] | ☐ SCCs ☐ BCRs ☐ Adequacy ☐ Derogation | [e.g. EU-US DPF certification] | ☐ Yes ☐ No |
| | | | | | |

---

## 7. Retention Schedule Reference

> **Cross-reference:** See `gdpr/retention-policies/` for full retention schedule per data category.

| Data Category | Retention Period | Justification | Disposal Method |
|--------------|-----------------|---------------|-----------------|
| [e.g. Account data] | [e.g. Active + 24 months] | [e.g. Statute of limitations] | [e.g. Secure deletion] |
| | | | |

---

## 8. Technical and Organisational Measures (Art. 32)

| Measure Category | Description | Implementation Status |
|-----------------|-------------|----------------------|
| Encryption | Data encrypted at rest (AES-256) and in transit (TLS 1.3) | ☐ Implemented ☐ Planned ☐ N/A |
| Access Control | Role-based access control (RBAC) with least-privilege principle | |
| Authentication | Multi-factor authentication (MFA) for all administrative access | |
| Backup & Recovery | Automated daily backups, tested quarterly | |
| Logging & Monitoring | Centralised audit logging with 12-month retention | |
| Incident Response | Documented IR plan, tested biannually | |
| Staff Training | Annual GDPR and security awareness training | |
| Physical Security | SOC 2 Type II certified data centres | |

---

## 9. Review & Approval History

| Date | Reviewer | Role | Changes Made | Approved |
|------|----------|------|--------------|----------|
| [YYYY-MM-DD] | [Name] | [Role] | Initial creation | ☐ Yes |
| | | | | |

---

## Appendix A: ROPA Completion Guidance

1. **Scope:** Every processing activity involving personal data must be recorded, regardless of volume or sensitivity.
2. **Legal Basis:** Must be determined *before* processing begins. Document the specific article and condition relied upon.
3. **Special Categories (Art. 9):** Religious affiliation, health data, children's data, and biometric data require an explicit Art. 9(2) condition in addition to an Art. 6 basis.
4. **Updates:** This register must be updated whenever a new processing activity is introduced, or an existing activity materially changes.
5. **Availability:** This document must be made available to the supervisory authority upon request (Art. 30(4)).
6. **Multi-Tenant Consideration:** Each tenant (religious institution) may act as an independent controller. Confirm controller/processor roles in the Data Processing Agreement.

---

*This template aligns with GDPR Article 30 requirements and is designed for a multi-tenant SaaS platform serving religious institutions across EU member states. Legal review is recommended before adoption.*

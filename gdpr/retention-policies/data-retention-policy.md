# Data Retention Policy

**Journey Of Life UAB — Data Retention and Secure Disposal Policy**

| Field | Value |
|-------|-------|
| **Document ID** | JOL-DRP-001 |
| **Organisation** | Journey Of Life UAB |
| **Policy Owner** | [DPO Name] — duomenu.apsauga@jol-hub.com |
| **Version** | 1.0 |
| **Effective Date** | [YYYY-MM-DD] |
| **Last Reviewed** | [YYYY-MM-DD] |
| **Next Review Due** | [YYYY-MM-DD] |
| **Approved By** | [CISO / Board] |
| **Classification** | Internal — Confidential |

---

## 1. Purpose and Scope

This Data Retention Policy establishes the framework for retaining, archiving, and securely disposing of personal data and business records processed by Journey Of Life UAB (the "Company") through the Journey Of Life multi-tenant platform serving religious institutions across 28 EU member states.

This policy ensures compliance with:
- **GDPR Article 5(1)(e)** — Storage limitation principle
- **GDPR Article 17** — Right to erasure
- **ISO/IEC 27001:2022 Annex A 5.33** — Protection of records
- **National retention laws** of Lithuania, Latvia, and Estonia
- **SOC 2 CC6.7** — Data transmission and storage controls

### 1.1 Scope

This policy applies to:
- All personal data processed by the Company as controller or processor
- All business records, regardless of format (electronic, paper, audio, video)
- All data stored in production systems, backups, archives, and third-party processors
- All employees, contractors, and third parties with access to Company data

---

## 2. Retention Principles

| Principle | Description |
|-----------|-------------|
| **Storage limitation** | Personal data shall be kept no longer than necessary for the purposes for which it is processed (GDPR Art. 5(1)(e)) |
| **Legal compliance** | Retention periods shall satisfy the longest applicable legal requirement |
| **Data minimisation** | Only data categories with a documented purpose and legal basis shall be retained |
| **Secure disposal** | All data shall be destroyed using methods that prevent reconstruction |
| **Auditability** | All retention and disposal decisions shall be logged and auditable |
| **Country variation** | Where member states impose different requirements, the longest period applies |

---

## 3. Retention Schedule — Personal Data

### 3.1 User Account Data

| Data Category | Retention Period | Legal Basis | Start Trigger | Disposal Method |
|--------------|-----------------|-------------|--------------|-----------------|
| Account registration data | Account lifetime + 24 months | GDPR Art. 6(1)(b); national limitation periods | Account deactivation/deletion | Secure deletion (NIST 800-88 Purge) |
| Authentication credentials | Account lifetime | GDPR Art. 6(1)(b) | Account deactivation/deletion | Immediate cryptographic erasure |
| Profile preferences | Account lifetime | GDPR Art. 6(1)(a) — consent | Consent withdrawal | Secure deletion within 30 days |
| Session data / tokens | 30 days | GDPR Art. 6(1)(f) — legitimate interest | Session end | Automatic expiry |
| MFA enrollment data | Account lifetime + 24 months | GDPR Art. 6(1)(b) | Account deletion | Secure deletion |

### 3.2 Financial and Transaction Data

| Data Category | Retention Period | Legal Basis | Start Trigger | Disposal Method |
|--------------|-----------------|-------------|--------------|-----------------|
| Donation records | 10 years (LT), 7 years (LV, EE) | LT: Mokesčių administravimo įstatymas Art. 40; LV: Grāmatvedības likums; EE: Raamatupidamise seadus §12 | Transaction date | Secure deletion after period |
| Payment processing records | 10 years (LT), 7 years (LV, EE) | Tax and accounting legislation | Transaction date | Secure deletion after period |
| Invoices and receipts | 10 years (LT), 7 years (LV, EE) | Tax legislation | Invoice date | Secure deletion after period |
| Bank account details | Account lifetime + retention period above | Contract + legal obligation | Account deletion | Secure deletion |
| Grant and funding records | 10 years | Grant agreement + audit requirements | Grant closure | Secure deletion |

### 3.3 Communication Data

| Data Category | Retention Period | Legal Basis | Start Trigger | Disposal Method |
|--------------|-----------------|-------------|--------------|-----------------|
| Platform messages (inter-user) | 24 months | GDPR Art. 6(1)(b) — contract | Last message date | Secure deletion |
| Prayer requests | 12 months (or per user request) | GDPR Art. 6(1)(a) — consent | Submission date | Secure deletion or upon request |
| Pastoral counselling notes | 5 years (or per pastoral policy) | GDPR Art. 9(2)(a) — explicit consent + professional duty | Counselling closure | Secure deletion |
| Email correspondence (operational) | 36 months | GDPR Art. 6(1)(f) — legitimate interest | Last correspondence | Secure deletion |
| Notification / alert logs | 12 months | GDPR Art. 6(1)(f) | Generation date | Automatic purge |
| Newsletter subscriptions | Until unsubscribe + 36 months | GDPR Art. 6(1)(a) — consent | Unsubscribe date | Secure deletion |

### 3.4 Special Category Data (GDPR Article 9)

| Data Category | Retention Period | Legal Basis | Start Trigger | Disposal Method |
|--------------|-----------------|-------------|--------------|-----------------|
| Religious affiliation | Account lifetime | GDPR Art. 9(2)(d) — legitimate activities of religious body | Account deletion | Secure deletion within 30 days |
| Membership records (parish) | Account lifetime + 10 years | Religious body activities + legal claims | Account deletion | Secure deletion |
| Baptism / sacrament records | Indefinite (per canon law) | GDPR Art. 9(2)(d) + religious institution mandate | N/A | Archival preservation (encrypted) |
| Health data (pastoral care) | 5 years after last contact | GDPR Art. 9(2)(h) — health/social care + professional obligation | Last contact | Secure deletion |
| Children's data | Until age 18 + 5 years | Parental consent + limitation period | Birth/registration date | Secure deletion at age 23 |

### 3.5 Children and Minors

| Data Category | Retention Period | Legal Basis | Start Trigger | Disposal Method |
|--------------|-----------------|-------------|--------------|-----------------|
| Sunday school attendance | Until age 18 + 5 years | Parental consent (Art. 8) + limitation period | Registration | Secure deletion at age 23 |
| Youth group participation | Until age 18 + 5 years | Parental consent + limitation period | Registration | Secure deletion at age 23 |
| Parental consent records | Until age 18 + 5 years | GDPR Art. 8 | Consent date | Secure deletion at age 23 |
| Photographs / media of minors | Until withdrawal of consent | GDPR Art. 6(1)(a) | Consent withdrawal | Immediate deletion within 72 hours |

---

## 4. Retention Schedule — System and Technical Data

### 4.1 System Logs

| Data Category | Retention Period | Legal Basis | Start Trigger | Disposal Method |
|--------------|-----------------|-------------|--------------|-----------------|
| Access / audit logs | 12 months (online) + 24 months (archive) | GDPR Art. 6(1)(f) — security; ISO 27001 A.8.15 | Event date | Automatic purge after archive period |
| Application error logs | 90 days | GDPR Art. 6(1)(f) — operations | Event date | Automatic rotation |
| Web server access logs | 12 months | GDPR Art. 6(1)(f) — security monitoring | Request timestamp | Automatic purge |
| Firewall / IDS logs | 12 months | GDPR Art. 6(1)(f) — security | Event date | Automatic purge |
| DNS query logs | 30 days | GDPR Art. 6(1)(f) | Query date | Automatic purge |
| Authentication logs | 24 months | GDPR Art. 6(1)(f) — security; SOC 2 evidence | Event date | Automatic purge |

### 4.2 Infrastructure Data

| Data Category | Retention Period | Legal Basis | Start Trigger | Disposal Method |
|--------------|-----------------|-------------|--------------|-----------------|
| Cloud configuration snapshots | 12 months | ISO 27001 A.8.9 — configuration management | Snapshot date | Overwritten by next snapshot |
| Penetration test reports | 5 years | ISO 27001 A.8.8; SOC 2 audit trail | Report date | Secure deletion |
| Vulnerability scan results | 3 years | ISO 27001 A.8.8 | Scan date | Secure deletion |
| SSL/TLS certificates | Until expiry + 1 year | Operational | Certificate expiry | Removal from key store |
| Encryption keys (inactive) | Per Key Management Policy | ISO 27001 A.8.24 | Key rotation | Cryptographic destruction |

### 4.3 Backup and Archive Data

| Data Category | Retention Period | Legal Basis | Start Trigger | Disposal Method |
|--------------|-----------------|-------------|--------------|-----------------|
| Daily incremental backups | 30 days (rolling) | ISO 27001 A.8.13 — backup | Backup date | Automatic overwrite |
| Weekly full backups | 12 weeks (rolling) | ISO 27001 A.8.13 | Backup date | Automatic overwrite |
| Monthly archive backups | 1 year | Business continuity + audit | Archive date | Secure deletion after 1 year |
| Annual archive backups | 7 years (LT/LV/EE financial) or 10 years (LT tax) | Tax and legal obligations | Archive date | Secure deletion |
| Disaster recovery snapshots | 72 hours | Business continuity | Snapshot date | Automatic overwrite |

> **Note:** Backup retention does not extend the retention period of the underlying data. When source data is eligible for deletion, the next backup cycle will exclude it. For individual deletion requests, data is purged from active backups within the next rotation cycle.

---

## 5. Retention Schedule — Business Records

| Record Category | Retention Period | Legal Basis | Start Trigger | Disposal Method |
|----------------|-----------------|-------------|--------------|-----------------|
| Contracts (tenant agreements) | Contract term + 10 years (LT), 7 years (LV/EE) | Limitation periods | Contract expiry/termination | Secure deletion |
| Data Processing Agreements | Contract term + 10 years | GDPR Art. 28 | DPA expiry | Secure deletion |
| Employee records | Employment + 5 years (LT), 3 years (LV/EE) | Labour law + limitation period | Employment termination | Secure deletion |
| Board meeting minutes | Permanent | Company law | Meeting date | Permanent archive |
| Policy and procedure documents | Superseded + 5 years | ISO 27001 A.5.33 — protection of records | Supersession date | Secure deletion |
| Audit reports (internal) | 5 years | ISO 27001 Clause 9.2 | Audit completion | Secure deletion |
| Audit reports (external) | 7 years | SOC 2, ISO 27001 certification | Audit completion | Secure deletion |
| Incident reports | 5 years | GDPR Art. 33-34; ISO 27001 A.5.27 | Incident closure | Secure deletion |
| Training records | Employment + 3 years | ISO 27001 A.6.3 | Training completion | Secure deletion on departure + 3y |

---

## 6. Country-Specific Variations

### 6.1 Lithuania (LT)

| Requirement | Detail | Legal Reference |
|------------|--------|----------------|
| Financial records | 10 years | Mokesčių administravimo įstatymas Art. 40 |
| Employee records | 5 years post-employment | Darbo kodeksas Art. 44 |
| Accounting documents | 10 years | Buhalterinės apskaitos įstatymas Art. 19 |
| CCTV footage | 60 days (general), 6 months (incident-related) | VDAI guidelines |
| Consent records | Duration of consent + 5 years | ADTAĮ |

### 6.2 Latvia (LV)

| Requirement | Detail | Legal Reference |
|------------|--------|----------------|
| Financial records | 7 years | Grāmatvedības likums Art. 14 |
| Employee records | 3 years post-employment | Darba likums |
| Accounting documents | 7 years | Par grāmatvedību |
| CCTV footage | 30 days (general) | DVI guidelines |
| Consent records | Duration of consent + 3 years | Personas datu apstrādes likums |

### 6.3 Estonia (EE)

| Requirement | Detail | Legal Reference |
|------------|--------|----------------|
| Financial records | 7 years | Raamatupidamise seadus §12 |
| Employee records | 3 years post-employment | Töölepingu seadus |
| Accounting documents | 7 years | Raamatupidamise seadus §12 |
| CCTV footage | 30 days (general) | AKI guidelines |
| E-residency data | Per e-residency programme rules | E-identiteedi seadus |
| Consent records | Duration of consent + 3 years | Isikuandmete kaitse seadus |

### 6.4 Application Rule

Where a data subject is located in a member state with a longer retention requirement, the **longer period** applies. The platform enforces retention per the data subject's country of registration.

---

## 7. Secure Disposal Procedures

### 7.1 Disposal Methods by Data Classification

| Classification | Electronic Disposal | Physical Disposal |
|---------------|--------------------|--------------------|
| **Public** | Standard deletion | Recycling |
| **Internal** | Overwrite (minimum 1 pass) | Cross-cut shredding (DIN 66399 Level P-4) |
| **Confidential** | Cryptographic erasure or overwrite (3 passes, NIST 800-88 Clear) | Cross-cut shredding (DIN 66399 Level P-5) |
| **Restricted** | Cryptographic erasure + overwrite (NIST 800-88 Purge) | Incineration or micro-cut shredding (DIN 66399 Level P-7) |

### 7.2 Disposal Workflow

1. **Identification** — Automated retention scheduler flags records past retention date
2. **Verification** — System owner verifies no legal hold or active litigation applies
3. **Approval** — DPO or designated approver authorises disposal
4. **Execution** — Data is destroyed using the appropriate method
5. **Logging** — Disposal is logged with: record ID, category, disposal date, method, approver
6. **Verification** — Quarterly audit confirms disposal was completed

### 7.3 Legal Hold Procedure

When litigation, investigation, or regulatory inquiry is anticipated or in progress:

- A **legal hold notice** is issued by the DPO or Legal Counsel
- All disposal of relevant records is **immediately suspended**
- Hold notices are tracked in the Legal Hold Register
- Hold is lifted only by written notice from the issuing authority
- Records under hold are **excluded** from automated disposal regardless of retention period

---

## 8. Backup and Archive Management

### 8.1 Backup Retention Hierarchy

| Tier | Type | Frequency | Retention | Location | Encryption |
|------|------|-----------|-----------|----------|-----------|
| 1 | Incremental | Daily | 30 days rolling | Primary region (EU-West) | AES-256 |
| 2 | Full | Weekly | 12 weeks rolling | Primary region (EU-West) | AES-256 |
| 3 | Archive | Monthly | 1 year | Secondary region (EU-Central) | AES-256 |
| 4 | Long-term archive | Annually | 7–10 years (per legal req.) | Secondary region (EU-Central) | AES-256 + key separation |

### 8.2 Backup Integrity

- Backup integrity is verified weekly through automated checksums
- Quarterly restore tests validate recoverability
- Backup encryption keys are managed separately from encrypted data
- Backup access is restricted to authorised operations personnel with MFA

### 8.3 Individual Deletion from Backups

When a data subject exercises the right to erasure (GDPR Art. 17):

1. Data is deleted from the **active production database** within 30 days
2. Data is **flagged for exclusion** in the next backup cycle
3. Data is **permanently removed** from all backups within the next rotation cycle (maximum 30 days for daily, 90 days for weekly)
4. Long-term archives are purged during the next scheduled archive maintenance (maximum 12 months)
5. **Cryptographic erasure** is available for immediate effect: destroying the encryption key renders archived copies irrecoverable

---

## 9. Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| **DPO** | Policy ownership, retention schedule approval, legal hold authorisation |
| **CISO** | Technical implementation of retention controls, disposal method approval |
| **System Owners** | Ensuring their systems comply with retention schedules, verifying disposal |
| **Engineering** | Implementing automated retention and disposal mechanisms |
| **Operations** | Backup management, archive maintenance, restore testing |
| **Legal Counsel** | Advising on legal retention requirements, issuing legal holds |
| **All Personnel** | Not retaining data beyond approved periods, reporting retention concerns |

---

## 10. Monitoring and Compliance

### 10.1 Retention Metrics

| Metric | Target | Frequency |
|--------|--------|-----------|
| Records past retention date (unresolved) | 0 | Monthly |
| Disposal requests completed within SLA | 100% | Quarterly |
| Backup restore tests passed | 100% | Quarterly |
| Legal holds active and tracked | 100% | Ongoing |
| Retention policy training completion | 100% | Annual |

### 10.2 Audit and Review

- Retention compliance is audited annually as part of the ISMS internal audit (`iso27001/internal-audits/`)
- Disposal logs are reviewed quarterly by the DPO
- Retention schedules are reviewed annually or upon regulatory change
- This policy is reviewed at least annually by the DPO and CISO

---

## 11. Exceptions

Exceptions to this policy require:

1. Written justification from the requesting party
2. Risk assessment by the DPO
3. Approval by the CISO
4. Documentation in the Exception Register with review date

| Exception ID | Data Category | Standard Period | Requested Period | Justification | Approved By | Review Date |
|-------------|--------------|----------------|-----------------|---------------|-------------|-------------|
| EXC-001 | [e.g. Litigation hold] | [e.g. 24 months] | [e.g. Indefinite] | [e.g. Active court case] | [Name] | [Date] |

---

## 12. Cross-References

| Document | Location |
|----------|----------|
| ROPA | `gdpr/ropa/ropa-template.md` |
| Privacy Policies (LT/LV/EE) | `gdpr/privacy-policies/` |
| Cookie Policy | `gdpr/cookie-policies/cookie-policy.md` |
| DSR Procedures | `gdpr/dsr-procedures/data-subject-rights-procedure.md` |
| Backup Policy | `security-policies/backup-and-recovery-policy.md` |
| Encryption Policy | `security-policies/encryption-policy.md` |
| Data Classification | `security-policies/data-classification-policy.md` |
| Information Security Policy | `security-policies/information-security-policy.md` |
| Asset Register | `iso27001/asset-register/asset-register.md` |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [YYYY-MM-DD] | [DPO Name] | Initial policy creation |
| | | | |

---

## Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| DPO / Policy Owner | [Name] | [Date] | _________________ |
| CISO | [Name] | [Date] | _________________ |
| Legal Counsel | [Name] | [Date] | _________________ |

---

*This Data Retention Policy ensures that Journey Of Life UAB retains personal data and business records only as long as necessary and in compliance with GDPR, ISO 27001:2022, SOC 2 Type II, and the national laws of Lithuania, Latvia, and Estonia. All retention periods are enforced through automated scheduling with human oversight for exceptions and legal holds.*

# Data Classification Policy

**Journey Of Life UAB — Information Classification Scheme (ISO 27001 A.5.12–A.5.13)**

| Field | Value |
|-------|-------|
| **Document ID** | JOL-SEC-DC-001 |
| **Policy Owner** | [CISO Name] |
| **Version** | 1.0 |
| **Effective Date** | [YYYY-MM-DD] |
| **Classification** | Internal — All Staff |

---

## 1. Classification Levels

| Level | Label | Description | Examples |
|-------|-------|------------|---------|
| **C1** | Public | Approved for unrestricted disclosure | Marketing materials, published privacy policies |
| **C2** | Internal | General internal use; not for external distribution | Meeting notes, internal announcements, training materials |
| **C3** | Confidential | Sensitive; need-to-know access; encrypted at rest | Employee records, tenant data, financial reports, source code |
| **C4** | Restricted | Highly sensitive; named individuals only; field-level encryption | Art. 9 special category data, encryption keys, credentials, children's data |

## 2. Classification Criteria

| Factor | C1 Public | C2 Internal | C3 Confidential | C4 Restricted |
|--------|----------|------------|---------------|-------------|
| Disclosure impact | None | Minor disruption | Significant damage | Severe damage / regulatory action |
| Legal requirement | None | None | GDPR Art. 32, contractual | GDPR Art. 9, children's data |
| Access control | Open | All employees | Role-based + approval | Named individuals + CISO approval |
| Encryption at rest | Optional | Optional | Mandatory (AES-256) | Mandatory (field-level AES-256) |
| Encryption in transit | HTTPS | HTTPS | TLS 1.2+ | TLS 1.3 preferred |

## 3. Handling Requirements

### 3.1 Storage

| Classification | Approved Storage | Prohibited Storage |
|---------------|----------------|------------------|
| C1 | Any Company storage | — |
| C2 | Company storage, internal collaboration tools | Personal cloud, unencrypted USB |
| C3 | Encrypted Company storage, approved SaaS | Personal devices, unencrypted media |
| C4 | Encrypted partitions with field-level encryption | Local storage, email attachments |

### 3.2 Transfer

| Classification | Approved Transfer Methods |
|---------------|-------------------------|
| C1 | Email, file sharing, web publication |
| C2 | Company email, internal file sharing |
| C3 | Encrypted email, secure file transfer, SFTP |
| C4 | Encrypted channel + out-of-band key delivery; never via email |

### 3.3 Disposal

| Classification | Disposal Method | Standard |
|---------------|----------------|---------|
| C1 | Standard deletion | — |
| C2 | Secure deletion | NIST 800-88 Clear |
| C3 | Secure deletion + verification | NIST 800-88 Clear |
| C4 | Cryptographic erasure + media destruction | NIST 800-88 Purge; DIN 66399 Level P-5 |

## 4. Labelling Requirements

| Medium | Labelling Method |
|--------|----------------|
| Digital documents | Header/footer with classification label |
| Email | Subject line prefix: [CONFIDENTIAL] or [RESTRICTED] |
| Databases | Column-level classification metadata |
| Physical documents | Stamp or watermark on every page |
| Storage media | Label on exterior |
| Cloud storage | Folder-level classification tags |

## 5. Classification Responsibilities

| Role | Responsibility |
|------|---------------|
| **Information owner** | Classify data upon creation; review annually |
| **System owner** | Ensure systems enforce classification controls |
| **All personnel** | Handle data according to its classification |
| **CISO** | Oversee classification scheme; resolve disputes |

## 6. Reclassification

- Data may be reclassified when sensitivity changes (e.g., after publication, upon retention expiry)
- Reclassification requires owner approval
- Downgrade from C4 requires CISO approval
- Log all reclassification decisions

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [YYYY-MM-DD] | [CISO Name] | Initial policy creation |

---

*This Data Classification Policy establishes the classification scheme for all Journey Of Life information assets. It supports ISO 27001 A.5.12–A.5.13 and GDPR Art. 32 security requirements.*

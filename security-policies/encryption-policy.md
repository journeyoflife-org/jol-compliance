# Encryption Policy

**Journey Of Life UAB — Cryptographic Controls (ISO 27001 A.8.24)**

| Field | Value |
|-------|-------|
| **Document ID** | JOL-SEC-ENC-001 |
| **Policy Owner** | [CISO Name] |
| **Version** | 1.0 |
| **Effective Date** | [YYYY-MM-DD] |
| **Classification** | Internal — Confidential |

---

## 1. Encryption Standards

| Use Case | Algorithm | Key Length | Mode |
|----------|----------|-----------|------|
| Data at rest (database) | AES | 256-bit | GCM |
| Data at rest (field-level) | AES | 256-bit | GCM (application-layer) |
| Data in transit | TLS | 1.2 minimum (1.3 preferred) | — |
| Asymmetric (signing) | ECDSA | P-256 or P-384 | — |
| Asymmetric (key exchange) | RSA | 2048+ or X25519 | — |
| Hashing | SHA | 256 or 384 | — |
| Password hashing | Argon2id / bcrypt | — | — |

**Prohibited:** DES, 3DES, RC4, MD5, SHA-1, SSL, TLS 1.0/1.1

## 2. Data at Rest Encryption

| Data Type | Encryption Level | Implementation |
|-----------|----------------|---------------|
| All production databases | Volume-level encryption | Cloud provider managed KMS |
| Personal data (C3) | Database-level encryption | Application-managed keys |
| Special category data (C4) | Field-level encryption | Application-layer encryption per field |
| Backups | Backup-level encryption | AES-256, separate key from source |
| Portable media | Full-disk encryption | BitLocker / FileVault |

## 3. Data in Transit Encryption

| Connection Type | Minimum Protocol |
|----------------|-----------------|
| Client → Platform | TLS 1.2 (TLS 1.3 preferred) |
| API → API (internal) | mTLS |
| VPN | IPsec or WireGuard |
| Email (external) | Opportunistic TLS; S/MIME for Confidential |
| Database connections | TLS 1.2 with certificate verification |

## 4. Key Management

| Requirement | Implementation |
|------------|---------------|
| Key generation | Cryptographically secure RNG; HSM-backed where possible |
| Key storage | Dedicated KMS; separate from encrypted data |
| Key rotation | Annual rotation for data-at-rest keys; per-incident rotation if compromise suspected |
| Key access | Separation of duties; dual control for key ceremonies |
| Key destruction | Cryptographic erasure when data retention expires |
| Key escrow | No key escrow; recovery via backup key with dual control |
| Multi-tenant keys | Tenant-specific encryption keys for data at rest |

## 5. Certificate Management

| Requirement | Implementation |
|------------|---------------|
| Certificate authority | Trusted public CA or internal CA |
| Certificate monitoring | Automated expiry monitoring (30-day alert) |
| Certificate pinning | Not used (rely on PKI trust chain) |
| Wildcard certificates | Avoided; use specific domain certificates |

## 6. Compliance Monitoring

| Activity | Frequency | Owner |
|----------|-----------|-------|
| TLS configuration scan | Monthly | Security |
| Key rotation verification | Annual | CISO |
| Encryption coverage audit | Annual | CISO |
| Deprecated algorithm scan | Quarterly | Security |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [YYYY-MM-DD] | [CISO Name] | Initial policy creation |

---

*This Encryption Policy defines cryptographic standards for all Journey Of Life systems. It supports ISO 27001 A.8.24, SOC 2 C1.2, and GDPR Art. 32(1)(a) pseudonymisation and encryption requirements.*

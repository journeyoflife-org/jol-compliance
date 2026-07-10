# Password Policy

**Journey Of Life UAB — Authentication and Credential Management (ISO 27001 A.5.17)**

| Field | Value |
|-------|-------|
| **Document ID** | JOL-SEC-PWD-001 |
| **Policy Owner** | [CISO Name] |
| **Version** | 1.0 |
| **Effective Date** | [YYYY-MM-DD] |
| **Classification** | Internal — All Staff |

---

## 1. Password Requirements

| Parameter | Employees / Contractors | Tenant Admins | Tenant Users | Service Accounts |
|-----------|------------------------|--------------|-------------|-----------------|
| Minimum length | 12 characters | 12 characters | 10 characters | 32 characters |
| Complexity | Upper + lower + digit + symbol | Upper + lower + digit + symbol | Upper + lower + digit | Random generated |
| Maximum age | No forced rotation* | No forced rotation* | No forced rotation* | 90 days (rotation) |
| History | Last 12 passwords | Last 12 passwords | Last 5 passwords | Last 12 |
| Lockout threshold | 5 failed attempts | 5 failed attempts | 5 failed attempts | 10 failed attempts |
| Lockout duration | 30 minutes | 30 minutes | 30 minutes | 30 minutes |

*NIST SP 800-63B recommends no forced rotation unless compromise is suspected.

## 2. Multi-Factor Authentication

| System | MFA Mandatory | Methods Accepted |
|--------|-------------|-----------------|
| SSO / Identity Provider | Yes | TOTP, hardware key (FIDO2), push notification |
| Production infrastructure | Yes | Hardware key (FIDO2), TOTP |
| Code repositories (GitHub) | Yes | Hardware key, TOTP, passkey |
| VPN | Yes | Hardware key, TOTP |
| Tenant admin portal | Yes | TOTP, push notification |
| Tenant user portal | Configurable per tenant | TOTP, push, email OTP |

## 3. Password Storage and Transmission

- Passwords stored using bcrypt/scrypt/Argon2 with per-user salt
- Passwords never stored in plaintext or reversible encryption
- Passwords never transmitted via email or unencrypted channels
- Password reset requires identity verification (Section 4)
- Breach detection: passwords checked against known breach databases (e.g., HaveIBeenPwned) at creation

## 4. Password Reset Procedures

| Scenario | Verification Method | Reset Method |
|----------|-------------------|-------------|
| Self-service (SSO) | Current password + MFA | Self-service portal |
| Forgotten password | Email to registered address + MFA | Self-service portal |
| Account lockout | MFA challenge + manager confirmation | IT service desk |
| Privileged account | CISO approval + hardware key | IT service desk |

## 5. Service Account Credentials

- Generated randomly (≥32 characters) or certificate/key-based
- Stored in secrets manager — never in code, configuration files, or documentation
- Rotated every 90 days (automated where possible)
- Access logged and audited quarterly

## 6. Prohibited Practices

- Sharing passwords with any person (including colleagues and managers)
- Writing passwords on paper, sticky notes, or unsecured digital files
- Reusing passwords across personal and Company accounts
- Using default vendor passwords on any production system
- Embedding credentials in source code or CI/CD configurations

## 7. Compliance Monitoring

| Activity | Frequency | Owner |
|----------|-----------|-------|
| MFA enrollment audit | Quarterly | CISO |
| Password policy configuration review | Quarterly | IT Security |
| Service account credential rotation audit | Quarterly | DevOps |
| Breach database check for compromised credentials | Monthly | IT Security |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [YYYY-MM-DD] | [CISO Name] | Initial policy creation |

---

*This Password Policy governs authentication for all Journey Of Life systems. It aligns with NIST SP 800-63B, ISO 27001 A.5.17, and SOC 2 CC6.4.*

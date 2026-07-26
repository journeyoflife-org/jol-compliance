# Access Control Procedure

**ISO/IEC 27001:2022 — Access Control Procedures for Journey Of Life UAB**

| Field | Value |
|-------|-------|
| **Document ID** | JOL-ISMS-PROC-001 |
| **Organisation** | Journey Of Life UAB |
| **ISMS Reference** | ISO 27001 Annex A.5.15–A.5.18 (Identity, Authentication, Access rights) |
| **Procedure Owner** | [CISO Name] |
| **Version** | 1.0 |
| **Effective Date** | [YYYY-MM-DD] |
| **Last Reviewed** | [YYYY-MM-DD] |
| **Next Review Due** | [YYYY-MM-DD] |
| **Classification** | Internal — Confidential |

---

## 1. Purpose

This procedure defines the operational controls for user identity management, authentication, authorisation, and access rights throughout the user lifecycle for the Journey Of Life multi-tenant SaaS platform.

**Applicable standards:**
- ISO/IEC 27001:2022 — A.5.15 (Access control), A.5.16 (Identity management), A.5.17 (Authentication information), A.5.18 (Access rights)
- SOC 2 — CC6.1–CC6.8 (Logical and Physical Access Controls)
- GDPR Art. 32 — Security of processing (access control measures)

---

## 2. Identity Management (A.5.16)

### 2.1 User Account Types

| Account Type | Description | Authentication Method | Review Frequency |
|-------------|-------------|----------------------|-----------------|
| **Employee** | Full-time and part-time staff | SSO + MFA | Quarterly |
| **Contractor** | External consultants and developers | SSO + MFA + client certificate | Quarterly |
| **Tenant Admin** | Institution administrators | Email/password + MFA | Quarterly |
| **Tenant User** | Institution members (clergy, staff) | Email/password + MFA | Annual |
| **Service Account** | Applications and automated processes | API keys / certificates | Quarterly |
| **Guest / Auditor** | Temporary read-only access | SSO + MFA + time-limited | Per engagement |

### 2.2 Unique Identification

- Every individual user receives a unique user identifier (UUID)
- Shared accounts are **prohibited** in all environments
- Each user account maps to exactly one individual

### 2.3 Identity Proofing

| User Type | Identity Verification |
|-----------|----------------------|
| Employee | Government-issued ID + background check |
| Contractor | Government-issued ID + company verification + NDA |
| Tenant Admin | Email verification + institution affiliation confirmation |
| Tenant User | Email verification + tenant admin approval |

---

## 3. Authentication Controls (A.5.17)

### 3.1 Multi-Factor Authentication (MFA)

| System | MFA Requirement | MFA Methods |
|--------|----------------|-------------|
| **Production infrastructure** | Mandatory — all users | TOTP, hardware key (YubiKey), push notification |
| **Administrative panels** | Mandatory — all users | TOTP, hardware key (YubiKey) |
| **Code repositories (GitHub)** | Mandatory — all users | TOTP, hardware key, passkey |
| **Tenant admin portal** | Mandatory — all admins | TOTP, push notification |
| **Tenant user portal** | Configurable per tenant | TOTP, push notification, email OTP |
| **VPN** | Mandatory — all users | TOTP, hardware key |
| **Office Wi-Fi** | Recommended | Certificate-based |

### 3.2 Password Requirements

| Parameter | Employee/Contractor | Tenant Users |
|-----------|--------------------|-------------|
| Minimum length | 12 characters | 10 characters |
| Complexity | Upper + lower + digit + symbol | Upper + lower + digit |
| Maximum age | 90 days (recommended) | No forced rotation |
| History | Last 12 passwords | Last 5 passwords |
| Lockout | 5 failed attempts → 30 min lockout | 5 failed attempts → 30 min lockout |
| Breach check | Mandatory (HaveIBeenPwned) | Recommended |

### 3.3 Single Sign-On (SSO)

- SAML 2.0 / OIDC-based SSO for employee and contractor accounts
- Identity provider: [IdP Name]
- Session timeout: 8 hours (configurable), forced re-authentication for sensitive operations

---

## 4. Authorisation Controls (A.5.15)

### 4.1 Role-Based Access Control (RBAC)

| Role | Description | Key Permissions |
|------|------------|----------------|
| **Platform Super Admin** | Platform-wide administration | All admin functions (break-glass only) |
| **Operations Engineer** | Infrastructure management | Deploy, monitor, infrastructure access |
| **Developer** | Code development and deployment | Code repo, CI/CD, staging environments |
| **Support Agent** | Tenant user support | Read-only tenant data (with consent), ticket system |
| **DPO / Privacy** | Data protection oversight | ROPA, DSR, audit logs (read-only) |
| **Tenant Admin** | Institution administration | Own tenant data, user management, settings |
| **Tenant Manager** | Institution management | Own tenant content, reporting, limited settings |
| **Tenant Member** | Standard institution user | Own data, assigned features |
| **Auditor** | External audit access | Read-only compliance evidence |

### 4.2 Privileged Access Management (PAM)

| Control | Implementation |
|---------|---------------|
| Privileged access request | Justification → manager approval → CISO approval → time-limited grant |
| Session recording | All privileged sessions recorded and retained 12 months |
| Just-in-time access | Elevated privileges granted for specific time windows |
| Break-glass accounts | Emergency accounts with enhanced monitoring; used only with CISO approval |
| Privileged access review | Monthly review of all privileged access grants |

### 4.3 Multi-Tenant Isolation

| Control | Implementation |
|---------|---------------|
| Data isolation | [Schema separation / row-level security] with tenant_id enforcement |
| API isolation | All API requests validated against authenticated tenant context |
| Storage isolation | Tenant-specific encryption keys for data at rest |
| Logging | Cross-tenant access attempts logged as security events |
| Testing | Automated tenant isolation regression tests in CI/CD pipeline |

### 4.4 Access Rights by Data Classification

| Classification | Default Access | Additional Controls |
|---------------|---------------|-------------------|
| **Public** | All authenticated users | None |
| **Internal** | All employees and contractors | None |
| **Confidential** | Role-based, need-to-know | Manager approval + logged access |
| **Restricted** | Named individuals only | CISO approval + MFA re-authentication + session logging |

---

## 5. Access Lifecycle Management

### 5.1 Provisioning (Joiner)

| Step | Action | Owner | SLA |
|------|--------|-------|-----|
| 1 | HR creates employee record (or contractor agreement signed) | HR / Procurement | Day 0 |
| 2 | Manager submits access request with role assignment | Manager | Day 0 |
| 3 | IT validates identity and creates account | IT / Identity Team | Day 1 |
| 4 | Base access provisioned (email, SSO, standard tools) | Identity Team | Day 1 |
| 5 | Role-specific access provisioned per approved request | System Owner | Day 1–3 |
| 6 | User acknowledges security responsibilities | User | Day 1 |

### 5.2 Modification (Mover)

| Step | Action | Owner | SLA |
|------|--------|-------|-----|
| 1 | HR notifies role change | HR | Within 24 hours |
| 2 | Current access reviewed against new role | System Owner | Day 1–3 |
| 3 | Previous role-specific access revoked | Identity Team | Day 1–3 |
| 4 | New role-specific access provisioned | Identity Team | Day 1–5 |
| 5 | Access change logged | Identity System | Automatic |

### 5.3 Deprovisioning (Leaver)

| Step | Action | Owner | SLA |
|------|--------|-------|-----|
| 1 | HR notifies termination (or resignation accepted) | HR | Same day |
| 2 | All system access revoked | Identity Team (automated) | **Within 24 hours** |
| 3 | Email account disabled | IT | Within 24 hours |
| 4 | Company devices collected | IT / Security | Within 48 hours |
| 5 | Data transferred or archived per retention policy | System Owner | Within 7 days |
| 6 | Access removal confirmed in audit log | Identity System | Automatic |

**Emergency termination:** All access revoked immediately upon HR notification.

### 5.4 Quarterly Access Review

| Activity | Frequency | Owner | Evidence |
|----------|-----------|-------|----------|
| Review all active user accounts | Quarterly | System Owner | Access review report |
| Review privileged access grants | Monthly | CISO | PAM review log |
| Identify dormant accounts (>90 days) | Quarterly | Identity Team | Dormant account report |
| Recertify or revoke access | Quarterly | Manager + System Owner | Recertification record |
| Review service account usage | Quarterly | Engineering | Service account inventory |

See `soc2/access-reviews/quarterly-access-review-template.md` for the review template.

---

## 6. Monitoring and Enforcement

| Activity | Tool/Method | Frequency |
|----------|------------|-----------|
| Failed login monitoring | SIEM alerting | Real-time |
| Privilege escalation detection | SIEM correlation | Real-time |
| Cross-tenant access attempt detection | Application logging + SIEM | Real-time |
| Account lockout notification | Automated alert to user + IT | Real-time |
| Anomalous access pattern detection | Behavioural analytics | Real-time |
| Access review compliance | Dashboard | Weekly |

---

## 7. Cross-References

| Document | Location |
|----------|----------|
| ISMS Policy | `iso27001/policies/information-security-policy.md` |
| Master InfoSec Policy | `security-policies/information-security-policy.md` |
| Password Policy | `security-policies/password-policy.md` |
| Acceptable Use Policy | `security-policies/acceptable-use-policy.md` |
| Quarterly Access Review | `soc2/access-reviews/quarterly-access-review-template.md` |
| Access Control Evidence (SOC 2) | `soc2/evidence/cc6/access-control-evidence.md` |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [YYYY-MM-DD] | [CISO Name] | Initial procedure creation |

---

*This Access Control Procedure governs identity management, authentication, and authorisation for all users of the Journey Of Life platform in compliance with ISO 27001:2022 Annex A.5.15–A.5.18, SOC 2 CC6, and GDPR Art. 32.*

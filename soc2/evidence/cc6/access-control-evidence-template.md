# SOC 2 — CC6 Logical and Physical Access Controls Evidence

**Trust Services Criteria — CC6: Common Criteria (Logical & Physical Access Controls)**

| Field | Value |
|-------|-------|
| **Organisation** | [Company Name] |
| **Service Organisation** | [Company Name] — [Platform Name] |
| **Report Type** | SOC 2 Type II |
| **Audit Period** | [Start Date] to [End Date] |
| **Evidence Reference** | CC6-EVD-[YYYY]-[NNN] |
| **Evidence Collected By** | [Name / Role] |
| **Evidence Date** | [YYYY-MM-DD] |
| **Auditor** | [Audit Firm Name] |
| **Classification** | Internal — Confidential |

---

## 1. CC6 Criteria Overview

| Criterion | Title | Description |
|-----------|-------|-------------|
| **CC6.1** | Logical and Physical Access Controls | The entity implements logical access security software, infrastructure, and architectures over protected information assets to protect them from security events. |
| **CC6.2** | Registration and Authorisation | Prior to issuing system credentials and granting system authorisations, the entity registers and authorises new internal and external users. |
| **CC6.3** | Removal of Access | The entity removes access to protected information assets when appropriate. |
| **CC6.4** | Access Changes | The entity designs and develops or configures security settings in a manner that restricts access based on the entity's defined access control policy. |
| **CC6.5** | Authentication Mechanisms | The entity restricts access to protected information assets through the use of authentication mechanisms. |
| **CC6.6** | Access to Data | The entity restricts physical access to facilities and protected information assets. |
| **CC6.7** | Transmission and Storage | The entity restricts the transmission, processing, and storage of protected information assets to authorised destinations. |
| **CC6.8** | Malicious Software Prevention | The entity implements controls to prevent or detect and act upon the introduction of unauthorised or malicious software. |

---

## 2. CC6.1 — Logical Access Security

### 2.1 Access Control Architecture

| Evidence Item | Description | Screenshot/Reference | Date Collected |
|--------------|-------------|---------------------|----------------|
| Access control policy | Documented access control policy defining roles, permissions, and least-privilege principles | [Reference/link to policy document] | [Date] |
| Network architecture diagram | Diagram showing network segmentation, firewalls, and access boundaries | [Reference/link to architecture diagram] | [Date] |
| RBAC matrix | Role-based access control matrix mapping roles to permissions per system | [Reference/link to RBAC configuration] | [Date] |
| Tenant isolation design | Documentation of multi-tenant data isolation mechanisms (schema separation, row-level security) | [Reference/link] | [Date] |

### 2.2 Logical Access Controls — System Inventory

| System / Application | Access Control Mechanism | Authentication Method | MFA Enforced | Access Review Frequency |
|---------------------|-------------------------|----------------------|-------------|------------------------|
| [e.g. AWS Console] | IAM policies, RBAC | SSO + MFA | ☐ Yes ☐ No | Quarterly |
| [e.g. Production Database] | Database roles, row-level security | Service account / IAM | ☐ Yes ☐ No | Quarterly |
| [e.g. CI/CD Pipeline] | Branch protection, approval gates | SSO + MFA | ☐ Yes ☐ No | Quarterly |
| [e.g. Admin Panel] | Application-level RBAC | SSO + MFA | ☐ Yes ☐ No | Quarterly |
| [e.g. Monitoring (Datadog/Grafana)] | Team-based access | SSO + MFA | ☐ Yes ☐ No | Quarterly |

---

## 3. CC6.2 — User Registration and Authorisation

### 3.1 New User Provisioning

| Evidence Item | Description | Screenshot/Reference | Date Collected |
|--------------|-------------|---------------------|----------------|
| User provisioning workflow | Documented process for requesting, approving, and granting access | [Reference/link] | [Date] |
| Sample new user request | Example of a completed access request with manager approval | [Screenshot — redacted] | [Date] |
| Access approval record | Evidence of approval chain for new access grants | [Screenshot — redacted] | [Date] |
| Background check policy | Policy requiring screening for privileged access roles | [Reference/link] | [Date] |

### 3.2 Provisioning Audit Sample

| Sample # | User (redacted) | Role | System | Requested By | Approved By | Date Granted | Compliant |
|----------|----------------|------|--------|-------------|-------------|-------------|-----------|
| 1 | User-A*** | [e.g. Developer] | [e.g. AWS] | [Manager] | [Team Lead] | [Date] | ☐ Yes ☐ No |
| 2 | User-B*** | | | | | | |
| 3 | User-C*** | | | | | | |
| 4 | User-D*** | | | | | | |
| 5 | User-E*** | | | | | | |

---

## 4. CC6.3 — Access Removal

### 4.1 Deprovisioning Process

| Evidence Item | Description | Screenshot/Reference | Date Collected |
|--------------|-------------|---------------------|----------------|
| Deprovisioning policy | Documented process for removing access upon termination or role change | [Reference/link] | [Date] |
| Automated deprovisioning | Evidence of automated access removal triggered by HR system | [Screenshot] | [Date] |
| Termination checklist | Checklist completed for departing employees | [Sample — redacted] | [Date] |

### 4.2 Deprovisioning Audit Sample

| Sample # | User (redacted) | Termination Date | Systems Disabled | Disabled Date | Time to Disable | Compliant (≤24h) |
|----------|----------------|-----------------|-----------------|--------------|----------------|-------------------|
| 1 | User-F*** | [Date] | [e.g. AWS, Slack, email, admin panel] | [Date] | [Hours] | ☐ Yes ☐ No |
| 2 | User-G*** | | | | | |
| 3 | User-H*** | | | | | |

---

## 5. CC6.4 — Access Changes

### 5.1 Access Modification Controls

| Evidence Item | Description | Screenshot/Reference | Date Collected |
|--------------|-------------|---------------------|----------------|
| Access change workflow | Process for requesting and approving access modifications | [Reference/link] | [Date] |
| Access review schedule | Quarterly access review calendar and completion records | [Reference/link] | [Date] |
| Access review sample | Completed access review with recertification decisions | [Screenshot — redacted] | [Date] |

### 5.2 Quarterly Access Review Evidence

| Review Period | Reviewer | Systems Reviewed | Total Accounts | Accounts Revoked | Completion Date | Sign-Off |
|--------------|----------|-----------------|---------------|-----------------|----------------|----------|
| Q[1-4] [YYYY] | [Name/Role] | [List systems] | [N] | [N] | [Date] | ☐ Signed |
| Q[1-4] [YYYY] | | | | | | |
| Q[1-4] [YYYY] | | | | | | |
| Q[1-4] [YYYY] | | | | | | |

---

## 6. CC6.5 — Authentication Mechanisms

### 6.1 Authentication Configuration

| Evidence Item | Description | Screenshot/Reference | Date Collected |
|--------------|-------------|---------------------|----------------|
| Password policy | Documented password complexity, length, and rotation requirements | [Reference/link] | [Date] |
| MFA enforcement config | Screenshot showing MFA is enforced for all users | [Screenshot] | [Date] |
| SSO configuration | Identity provider configuration (e.g. SAML/OIDC settings) | [Screenshot — redacted] | [Date] |
| Service account controls | Controls for non-interactive accounts (rotation, scoping) | [Reference/link] | [Date] |

### 6.2 Password Policy Parameters

| Parameter | Requirement | Enforced | Evidence |
|-----------|------------|----------|----------|
| Minimum length | ≥ 12 characters | ☐ Yes | [Config screenshot] |
| Complexity | Mixed case, numbers, symbols | ☐ Yes | |
| History | Last [N] passwords remembered | ☐ Yes | |
| Maximum age | [N] days (if applicable) | ☐ Yes | |
| Lockout threshold | [N] failed attempts | ☐ Yes | |
| Lockout duration | [N] minutes | ☐ Yes | |

---

## 7. CC6.6 — Physical Access Controls

### 7.1 Facility Access

| Evidence Item | Description | Screenshot/Reference | Date Collected |
|--------------|-------------|---------------------|----------------|
| Data centre SOC 2 report | Current SOC 2 Type II report from hosting provider | [Reference — restricted distribution] | [Date] |
| Visitor access log | Sample visitor access log with sign-in/out records | [Screenshot — redacted] | [Date] |
| Badge access records | Sample badge access logs for restricted areas | [Screenshot — redacted] | [Date] |
| CCTV retention policy | Policy defining camera coverage and footage retention | [Reference/link] | [Date] |

### 7.2 Office / Remote Access

| Evidence Item | Description | Screenshot/Reference | Date Collected |
|--------------|-------------|---------------------|----------------|
| Remote access policy | VPN and remote access security requirements | [Reference/link] | [Date] |
| VPN configuration | VPN settings showing encryption and MFA requirements | [Screenshot] | [Date] |
| Endpoint security policy | Requirements for endpoint device security | [Reference/link] | [Date] |

---

## 8. CC6.7 — Data Transmission and Storage

| Evidence Item | Description | Screenshot/Reference | Date Collected |
|--------------|-------------|---------------------|----------------|
| TLS configuration | TLS 1.2+ enforcement on all endpoints | [Screenshot / SSL Labs report] | [Date] |
| Encryption at rest | Database and storage encryption configuration | [Screenshot] | [Date] |
| Data residency controls | Evidence that data resides in approved regions (EU) | [Screenshot — AWS region config] | [Date] |
| Transfer controls | Controls preventing unauthorised data exfiltration | [Reference/link] | [Date] |

---

## 9. CC6.8 — Malicious Software Prevention

| Evidence Item | Description | Screenshot/Reference | Date Collected |
|--------------|-------------|---------------------|----------------|
| Anti-malware solution | Endpoint protection platform deployed across all devices | [Screenshot — dashboard] | [Date] |
| Email filtering | Email security gateway with spam/phishing detection | [Screenshot — dashboard] | [Date] |
| Web application firewall | WAF rules and configuration | [Screenshot] | [Date] |
| Vulnerability scanning | Automated scanning schedule and latest report | [Reference/link] | [Date] |
| Patch management | Patch deployment SLA and compliance dashboard | [Screenshot] | [Date] |

---

## 10. Exception Log

| Exception # | Criterion | Description | Risk Rating | Mitigation | Remediation Owner | Target Date | Status |
|-------------|-----------|-------------|-------------|-----------|--------------------|-------------|--------|
| EXC-001 | [e.g. CC6.5] | [e.g. 2 service accounts without MFA] | [Low/Med/High] | [e.g. Service accounts scoped to read-only; certificate-based auth] | [Name] | [Date] | ☐ Open ☐ Closed |
| | | | | | | | |

---

## 11. Auditor Assessment

| Criterion | Control Design | Operating Effectiveness | Evidence Sufficiency | Auditor Notes |
|-----------|---------------|------------------------|---------------------|---------------|
| CC6.1 | ☐ Effective ☐ Deficiency ☐ Material weakness | ☐ Effective ☐ Deficiency ☐ Material weakness | ☐ Sufficient ☐ Insufficient | |
| CC6.2 | | | | |
| CC6.3 | | | | |
| CC6.4 | | | | |
| CC6.5 | | | | |
| CC6.6 | | | | |
| CC6.7 | | | | |
| CC6.8 | | | | |

---

## 12. Evidence Retention

| Requirement | Period |
|------------|--------|
| SOC 2 evidence retention | Minimum 5 years or per contractual requirement |
| Storage location | [e.g. `audit-evidence/` in jol-compliance repository] |
| Access restrictions | Restricted to audit team, CISO, and compliance officers |
| Integrity controls | Version-controlled (git); tamper-evident via commit hashes |

---

*This evidence template maps to SOC 2 Type II Trust Services Criteria CC6.1–CC6.8 and is designed for a multi-tenant SaaS platform serving ~400,000 religious institutions. Evidence should be collected quarterly and retained for the full audit period. All screenshots containing sensitive data must be redacted before inclusion.*

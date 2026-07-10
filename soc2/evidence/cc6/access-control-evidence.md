# SOC 2 CC6 — Access Control Evidence

**Journey Of Life UAB — Evidence Collection for CC6 (Logical and Physical Access Controls)**

| Field | Value |
|-------|-------|
| **Document ID** | JOL-SOC2-EV-CC6-2026 |
| **Audit Period** | [Start Date] to [End Date] |
| **Evidence Owner** | [CISO Name] |
| **Version** | 1.0 |
| **Classification** | Internal — Confidential |

---

## 1. CC6.1 — Access Infrastructure

| Evidence Item | Description | Collection Method | Frequency | Location |
|--------------|-------------|------------------|-----------|---------|
| EV-CC6-001 | Access control policy | Document review | Annual | `iso27001/procedures/access-control-procedure.md` |
| EV-CC6-002 | RBAC role definitions | Configuration export | Quarterly | Access control procedure Section 4.1 |
| EV-CC6-003 | MFA configuration screenshots | System configuration | Quarterly | [Screenshot evidence] |
| EV-CC6-004 | Authentication failure logs | SIEM export | Monthly | SIEM platform |
| EV-CC6-005 | Password policy configuration | System configuration | Quarterly | Password policy document |

## 2. CC6.2 — User Registration and De-registration

| Evidence Item | Description | Collection Method | Frequency | Location |
|--------------|-------------|------------------|-----------|---------|
| EV-CC6-010 | New hire onboarding tickets | HR system export | Quarterly (sample) | [Ticket system] |
| EV-CC6-011 | Employee termination tickets | HR system export | Quarterly (sample) | [Ticket system] |
| EV-CC6-012 | Identity verification records | HR records | Quarterly (sample) | [HR system] |
| EV-CC6-013 | Background check completion | HR records | Annual | [HR system] |

## 3. CC6.3 — Unique Identification

| Evidence Item | Description | Collection Method | Frequency | Location |
|--------------|-------------|------------------|-----------|---------|
| EV-CC6-020 | User directory listing | Identity system export | Quarterly | [Identity system] |
| EV-CC6-021 | Shared account scan (zero expected) | Automated scan | Monthly | [Scan results] |
| EV-CC6-022 | Service account inventory | Engineering export | Quarterly | Asset register |

## 4. CC6.4 — Credential Management

| Evidence Item | Description | Collection Method | Frequency | Location |
|--------------|-------------|------------------|-----------|---------|
| EV-CC6-030 | MFA enrollment report | IdP export | Quarterly | [IdP report] |
| EV-CC6-031 | Password complexity configuration | System configuration | Quarterly | Password policy |
| EV-CC6-032 | Account lockout events | SIEM export | Quarterly | SIEM platform |
| EV-CC6-033 | Credential rotation logs (service accounts) | Secrets manager export | Quarterly | [Secrets manager] |

## 5. CC6.5 — Access Provisioning

| Evidence Item | Description | Collection Method | Frequency | Location |
|--------------|-------------|------------------|-----------|---------|
| EV-CC6-040 | Access request approvals (sample) | Ticket system export | Quarterly (sample 25) | [Ticket system] |
| EV-CC6-041 | Privileged access requests | PAM system export | Quarterly | PAM logs |
| EV-CC6-042 | New user access configuration | IdP export | Quarterly (sample) | [IdP] |

## 6. CC6.6 — Access Modification

| Evidence Item | Description | Collection Method | Frequency | Location |
|--------------|-------------|------------------|-----------|---------|
| EV-CC6-050 | Role change tickets (sample) | Ticket system export | Quarterly (sample 25) | [Ticket system] |
| EV-CC6-051 | Access modification audit log | Identity system | Quarterly | [Audit log] |

## 7. CC6.7 — Access Removal

| Evidence Item | Description | Collection Method | Frequency | Location |
|--------------|-------------|------------------|-----------|---------|
| EV-CC6-060 | Termination access removal (sample) | Identity system + HR | Quarterly (sample 25) | [Cross-reference] |
| EV-CC6-061 | Time from termination to access removal | Automated report | Quarterly | [Report] |
| EV-CC6-062 | Dormant account report (>90 days) | Identity system | Quarterly | [Report] |
| EV-CC6-063 | Access review recertification records | Access review | Quarterly | `soc2/access-reviews/` |

## 8. CC6.8 — Physical Access Controls

| Evidence Item | Description | Collection Method | Frequency | Location |
|--------------|-------------|------------------|-----------|---------|
| EV-CC6-070 | Physical access log (sample) | Badge system export | Quarterly | [Badge system] |
| EV-CC6-071 | Visitor log (sample) | Facilities records | Quarterly | [Visitor log] |
| EV-CC6-072 | Data centre SOC 2 report | Hosting provider | Annual | [Provider report] |

---

## 9. Evidence Collection Schedule

| Month | Activities |
|-------|-----------|
| January | Q4 evidence collection, annual policy review |
| April | Q1 evidence collection, access review |
| July | Q2 evidence collection, mid-year review |
| October | Q3 evidence collection, pre-audit preparation |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [YYYY-MM-DD] | [CISO Name] | Initial evidence register |

---

*This evidence register supports SOC 2 Type II audit for CC6 (Logical and Physical Access Controls). Evidence is collected quarterly and retained for the audit period plus 1 year.*

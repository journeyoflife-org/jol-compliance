# Quarterly Access Review Template

**SOC 2 Type II — CC6.7 User Access Recertification**

| Field | Value |
|-------|-------|
| **Document ID** | JOL-SOC2-AR-[YYYY]-Q[N] |
| **Organisation** | Journey Of Life UAB |
| **Review Period** | Q[N] [YYYY] ([Start] – [End]) |
| **Review Owner** | [CISO Name] |
| **Completion Date** | [YYYY-MM-DD] |
| **Classification** | Internal — Confidential |

---

## 1. Review Scope

| System / Application | Owner | Users Reviewed |
|---------------------|-------|---------------|
| Journey Of Life Platform (production) | CTO | [X] |
| GitHub (code repositories) | Head of Engineering | [X] |
| Infrastructure (cloud console) | Head of Ops | [X] |
| Identity Provider (SSO) | CISO | [X] |
| Email system | IT | [X] |
| Collaboration tools | IT | [X] |
| SIEM / monitoring | CISO | [X] |
| CI/CD pipeline | DevOps | [X] |

## 2. Reviewer Assignment

| Role | Reviewer | Systems |
|------|---------|---------|
| CISO | [Name] | Infrastructure, IdP, SIEM |
| Head of Engineering | [Name] | GitHub, CI/CD |
| Head of Operations | [Name] | Platform production |
| IT Manager | [Name] | Email, collaboration tools |

## 3. User Access Review

### 3.1 Active User Inventory

| # | User ID | Name | Role | Department | Last Login | MFA Enabled | Action |
|---|--------|------|------|-----------|-----------|------------|--------|
| 1 | | | | | | ☐ Yes | ☐ Retain ☐ Modify ☐ Revoke |

### 3.2 Privileged Access Review

| # | User ID | Name | System | Privilege Level | Justification | Action |
|---|--------|------|--------|---------------|--------------|--------|
| 1 | | | | | | ☐ Retain ☐ Modify ☐ Revoke |

### 3.3 Service Account Review

| # | Service Account | System | Purpose | Owner | Last Used | Action |
|---|----------------|--------|---------|-------|----------|--------|
| 1 | | | | | | ☐ Retain ☐ Revoke |

### 3.4 Dormant Accounts (>90 days inactive)

| # | User ID | Name | System | Last Login | Action |
|---|--------|------|--------|-----------|--------|
| 1 | | | | | ☐ Disable ☐ Investigate |

## 4. Review Actions Summary

| Action | Count | Percentage |
|--------|-------|-----------|
| Retained (access confirmed) | [X] | [X]% |
| Modified (access reduced) | [X] | [X]% |
| Revoked (access removed) | [X] | [X]% |
| Dormant accounts disabled | [X] | — |
| **Total reviewed** | **[X]** | **100%** |

## 5. Findings and Issues

| # | Finding | Severity | Action Required | Owner | Target Date |
|---|---------|---------|----------------|-------|------------|
| 1 | | ☐ High ☐ Medium ☐ Low | | | |

## 6. Sign-Off

| Reviewer | Date | Signature |
|----------|------|-----------|
| [CISO Name] | [Date] | _________________ |
| [Head of Engineering] | [Date] | _________________ |
| [Head of Operations] | [Date] | _________________ |
| [IT Manager] | [Date] | _________________ |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [YYYY-MM-DD] | [CISO Name] | Initial template |

---

*This template is used for quarterly access reviews as required by SOC 2 CC6.7 and ISO 27001 A.5.18. Reviews must be completed within 10 business days of quarter-end. All access modifications must be actioned within 5 business days of the review sign-off.*

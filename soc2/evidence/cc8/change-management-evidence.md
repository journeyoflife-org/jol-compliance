# SOC 2 CC8 — Change Management Evidence

**Journey Of Life UAB — Evidence Collection for CC8 (Change Management)**

| Field | Value |
|-------|-------|
| **Document ID** | JOL-SOC2-EV-CC8-2026 |
| **Audit Period** | [Start Date] to [End Date] |
| **Evidence Owner** | [Head of Engineering] |
| **Version** | 1.0 |
| **Classification** | Internal — Confidential |

---

## 1. CC8.1 — Change Authorisation

| Evidence Item | Description | Collection Method | Frequency |
|--------------|-------------|------------------|-----------|
| EV-CC8-001 | Change management policy | Document review | Annual |
| EV-CC8-002 | Pull request approval records (sample) | GitHub export | Quarterly (sample 25) |
| EV-CC8-003 | Code review statistics | GitHub metrics | Quarterly |
| EV-CC8-004 | Emergency change approvals | Change log | Per event |
| EV-CC8-005 | Branch protection rules | GitHub configuration | Quarterly |

### PR Approval Sample Template

| PR # | Title | Author | Reviewers | Approved Date | Merged Date | Status |
|------|-------|--------|----------|--------------|------------|--------|
| | | | | | | ☐ Compliant |

## 2. CC8.2 — Change Documentation

| Evidence Item | Description | Collection Method | Frequency |
|--------------|-------------|------------------|-----------|
| EV-CC8-010 | Git commit log (sample) | Git export | Quarterly |
| EV-CC8-011 | Signed commits verification | GitHub export | Quarterly |
| EV-CC8-012 | Release notes / changelog | Release system | Per release |
| EV-CC8-013 | Deployment records | CI/CD pipeline | Quarterly |

## 3. CC8.3 — Change Testing

| Evidence Item | Description | Collection Method | Frequency |
|--------------|-------------|------------------|-----------|
| EV-CC8-020 | CI/CD pipeline test results (sample) | CI/CD export | Quarterly (sample 25) |
| EV-CC8-021 | Test coverage reports | CI/CD export | Quarterly |
| EV-CC8-022 | SAST scan results (sample) | Security scanner | Quarterly (sample 25) |
| EV-CC8-023 | DAST scan results | Security scanner | Quarterly |
| EV-CC8-024 | Security gate pass/fail records | CI/CD pipeline | Quarterly |

## 4. CC8.4 — Change Approval and Deployment

| Evidence Item | Description | Collection Method | Frequency |
|--------------|-------------|------------------|-----------|
| EV-CC8-030 | Production deployment approvals (sample) | CI/CD export | Quarterly (sample 25) |
| EV-CC8-031 | Deployment success/failure records | CI/CD pipeline | Quarterly |
| EV-CC8-032 | Rollback records (if any) | CI/CD pipeline | Per event |
| EV-CC8-033 | Environment segregation verification | Configuration review | Quarterly |
| EV-CC8-034 | Separation of duties (dev ≠ deploy approver) | Access review | Quarterly |

### Deployment Compliance Summary

| Quarter | Total Deployments | With Approval | With Tests | Compliant | Rate |
|---------|-----------------|--------------|-----------|----------|------|
| Q1 | [X] | [X] | [X] | [X] | [X]% |
| Q2 | [X] | [X] | [X] | [X] | [X]% |
| Q3 | [X] | [X] | [X] | [X] | [X]% |
| Q4 | [X] | [X] | [X] | [X] | [X]% |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [YYYY-MM-DD] | [Head of Engineering] | Initial evidence register |

---

*This evidence register supports SOC 2 Type II audit for CC8 (Change Management). Evidence is collected quarterly and retained for the audit period plus 1 year.*

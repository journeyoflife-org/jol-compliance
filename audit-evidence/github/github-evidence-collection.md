# GitHub Evidence Collection Guide

**Audit Evidence — Code Repository and CI/CD Security Controls**

| Field | Value |
|-------|-------|
| **Document ID** | JOL-AE-GH-001 |
| **Organisation** | Journey Of Life UAB |
| **Evidence Owner** | [Head of Engineering] |
| **Version** | 1.0 |
| **Classification** | Internal — Confidential |

---

## 1. Repository Security Configuration

| Evidence Item | Description | Collection Method |
|--------------|-------------|------------------|
| AE-GH-001 | Branch protection rules (main/release) | GitHub Settings screenshot |
| AE-GH-002 | Required reviewers configuration | GitHub Settings screenshot |
| AE-GH-003 | Signed commits enforcement | GitHub Settings + GPG key list |
| AE-GH-004 | Repository access control (teams) | GitHub Teams export |
| AE-GH-005 | Two-factor authentication enforcement | GitHub Org settings |
| AE-GH-006 | Secret scanning configuration | GitHub Settings screenshot |
| AE-GH-007 | Dependabot configuration | dependabot.yml file |

## 2. CI/CD Security Evidence

| Evidence Item | Description | Collection Method |
|--------------|-------------|------------------|
| AE-GH-010 | Workflow files (.github/workflows/) | File listing |
| AE-GH-011 | SAST scan results (sample) | CI/CD pipeline export |
| AE-GH-012 | Dependency scan results (SCA) | CI/CD pipeline export |
| AE-GH-013 | Container image scan results | CI/CD pipeline export |
| AE-GH-014 | Deployment approval records (sample 25) | GitHub Actions log |
| AE-GH-015 | Environment protection rules | GitHub Settings |
| AE-GH-016 | Secrets management (no hardcoded secrets) | Repository scan report |

## 3. Access Control Evidence

| Evidence Item | Description | Collection Method |
|--------------|-------------|------------------|
| AE-GH-020 | Organisation member list | GitHub API export |
| AE-GH-021 | Team membership and permissions | GitHub API export |
| AE-GH-022 | Outside collaborator access | GitHub API export |
| AE-GH-023 | Personal access token inventory | GitHub Settings |
| AE-GH-024 | SSH key inventory | GitHub Settings |
| AE-GH-025 | Audit log (90-day sample) | GitHub audit log export |

## 4. Collection Schedule

| Frequency | Items |
|-----------|-------|
| Quarterly | AE-GH-001–007, AE-GH-010–016 |
| Monthly | AE-GH-020–025 |
| Per audit | Full collection |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [YYYY-MM-DD] | [Head of Engineering] | Initial guide |

---

*This guide supports evidence collection for GitHub repository and CI/CD security controls. Evidence is collected quarterly for SOC 2 CC8 and ISO 27001 A.8.25–A.8.32 compliance.*

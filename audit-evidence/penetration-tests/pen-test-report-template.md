# Penetration Test Report Template

**Audit Evidence — External Penetration Testing**

| Field | Value |
|-------|-------|
| **Document ID** | JOL-AE-PT-[YYYY]-[NNN] |
| **Test Period** | [Start] to [End] |
| **Testing Firm** | [Firm Name] |
| **Scope** | Platform web application, API, infrastructure |
| **Methodology** | OWASP Testing Guide v4.2, PTES |
| **Classification** | Restricted |

---

## 1. Executive Summary

[Summary of findings, overall risk rating, key recommendations]

| Severity | Count |
|----------|-------|
| Critical | [X] |
| High | [X] |
| Medium | [X] |
| Low | [X] |
| Informational | [X] |

## 2. Scope and Methodology

### 2.1 In-Scope Targets

| Target | Type | Method |
|--------|------|--------|
| [URL] | Web application | Black-box / Grey-box |
| [API endpoint] | REST API | Grey-box |
| [IP range] | Infrastructure | External |
| [Mobile app] | Mobile | Grey-box |

### 2.2 Out of Scope

- Tenant data and production databases
- Third-party integrations
- Social engineering
- Physical security

### 2.3 Methodology

- OWASP Testing Guide v4.2
- Penetration Testing Execution Standard (PTES)
- Manual testing + automated scanning
- Tenant isolation testing (cross-tenant access attempts)

## 3. Findings

### Finding Template

| Field | Detail |
|-------|--------|
| **Finding ID** | PT-[YYYY]-F[NNN] |
| **Title** | |
| **Severity** | ☐ Critical ☐ High ☐ Medium ☐ Low ☐ Info |
| **CVSS Score** | |
| **Affected Component** | |
| **Description** | |
| **Reproduction Steps** | |
| **Evidence** | [Screenshots, HTTP requests/responses] |
| **Impact** | |
| **Recommendation** | |
| **Remediation Effort** | ☐ Low ☐ Medium ☐ High |

## 4. Tenant Isolation Testing

| Test | Result | Details |
|------|--------|---------|
| Cross-tenant API access | ☐ Pass ☐ Fail | |
| Tenant ID manipulation | ☐ Pass ☐ Fail | |
| Cross-tenant data in search | ☐ Pass ☐ Fail | |
| Shared resource isolation | ☐ Pass ☐ Fail | |

## 5. Remediation Tracker

| Finding ID | Severity | Status | Owner | Target Date | Verified |
|-----------|---------|--------|-------|------------|---------|
| | | ☐ Open ☐ Fixed ☐ Accepted | | | ☐ |

## 6. Re-Test Results

| Finding ID | Re-Test Date | Result | Tester |
|-----------|-------------|--------|--------|
| | | ☐ Fixed ☐ Partially Fixed ☐ Not Fixed | |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [YYYY-MM-DD] | [Testing Firm] | Initial report |

---

*Penetration tests are conducted annually by an independent third-party firm. Reports are classified as Restricted and shared only with authorised personnel and auditors.*

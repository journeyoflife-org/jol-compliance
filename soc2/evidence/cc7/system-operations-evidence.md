# SOC 2 CC7 — System Operations Evidence

**Journey Of Life UAB — Evidence Collection for CC7 (System Operations)**

| Field | Value |
|-------|-------|
| **Document ID** | JOL-SOC2-EV-CC7-2026 |
| **Audit Period** | [Start Date] to [End Date] |
| **Evidence Owner** | [CISO Name] |
| **Version** | 1.0 |
| **Classification** | Internal — Confidential |

---

## 1. CC7.1 — Infrastructure Management

| Evidence Item | Description | Collection Method | Frequency |
|--------------|-------------|------------------|-----------|
| EV-CC7-001 | Infrastructure architecture diagrams | Engineering export | Annual |
| EV-CC7-002 | Server hardening baseline | Configuration export | Quarterly |
| EV-CC7-003 | Patch management compliance report | System export | Monthly |
| EV-CC7-004 | Infrastructure monitoring dashboard | Monitoring platform | Quarterly (screenshot) |
| EV-CC7-005 | Anti-malware deployment report | Endpoint protection | Monthly |

## 2. CC7.2 — Vulnerability Management

| Evidence Item | Description | Collection Method | Frequency |
|--------------|-------------|------------------|-----------|
| EV-CC7-010 | Vulnerability scan reports (internal) | Scanner export | Weekly |
| EV-CC7-011 | Vulnerability scan reports (external) | Scanner export | Weekly |
| EV-CC7-012 | Penetration test report | External firm | Annual |
| EV-CC7-013 | Vulnerability remediation tracking | Ticket system | Monthly |
| EV-CC7-014 | Critical vulnerability patching SLA compliance | Automated report | Monthly |
| EV-CC7-015 | Container image scan results | CI/CD pipeline | Per build |
| EV-CC7-016 | Dependency vulnerability scan (SCA) | CI/CD pipeline | Per build |

### Patching SLA Compliance Report Template

| Severity | SLA | Vulnerabilities Found | Patched Within SLA | Compliance Rate |
|----------|-----|----------------------|-------------------|----------------|
| Critical | ≤24 hours | [X] | [X] | [X]% |
| High | ≤7 days | [X] | [X] | [X]% |
| Medium | ≤30 days | [X] | [X] | [X]% |
| Low | ≤90 days | [X] | [X] | [X]% |

## 3. CC7.3 — Incident Detection

| Evidence Item | Description | Collection Method | Frequency |
|--------------|-------------|------------------|-----------|
| EV-CC7-020 | SIEM alert summary | SIEM export | Quarterly |
| EV-CC7-021 | SIEM rule configuration | SIEM configuration | Annual |
| EV-CC7-022 | Threat intelligence feed subscriptions | Vendor records | Annual |
| EV-CC7-023 | Security event log retention proof | Log management | Quarterly |
| EV-CC7-024 | Anomaly detection alerts (sample) | SIEM export | Quarterly (sample) |

## 4. CC7.4 — Incident Response

| Evidence Item | Description | Collection Method | Frequency |
|--------------|-------------|------------------|-----------|
| EV-CC7-030 | Incident response policy | Document review | Annual |
| EV-CC7-031 | Incident response playbook | Document review | Annual |
| EV-CC7-032 | Incident records (if any during period) | Incident management system | Per incident |
| EV-CC7-033 | Tabletop exercise report | Exercise records | Annual |
| EV-CC7-034 | On-call rotation schedule | Scheduling system | Quarterly |
| EV-CC7-035 | Incident response time metrics | Automated report | Quarterly |

### Incident Response Metrics

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Mean time to detect (MTTD) | ≤[X] minutes | [X] min | ☐ Met |
| Mean time to respond (MTTR) | ≤[X] minutes | [X] min | ☐ Met |
| Mean time to contain | ≤[X] hours | [X] hours | ☐ Met |
| Total incidents (period) | — | [X] | — |
| Major incidents (P1/P2) | — | [X] | — |

## 5. CC7.5 — Incident Recovery

| Evidence Item | Description | Collection Method | Frequency |
|--------------|-------------|------------------|-----------|
| EV-CC7-040 | Backup success rate report | Backup system | Weekly |
| EV-CC7-041 | Backup restore test results | DR test records | Quarterly |
| EV-CC7-042 | DR plan test report | Exercise records | Annual |
| EV-CC7-043 | Business continuity plan | Document review | Annual |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [YYYY-MM-DD] | [CISO Name] | Initial evidence register |

---

*This evidence register supports SOC 2 Type II audit for CC7 (System Operations). Evidence is collected per the defined frequency and retained for the audit period plus 1 year.*

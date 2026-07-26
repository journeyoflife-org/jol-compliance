# SOC 2 A1 — Availability Evidence

**Journey Of Life UAB — Evidence Collection for A1 (Availability)**

| Field | Value |
|-------|-------|
| **Document ID** | JOL-SOC2-EV-A1-2026 |
| **Audit Period** | [Start Date] to [End Date] |
| **Evidence Owner** | [Head of Operations] |
| **Version** | 1.0 |
| **Classification** | Internal — Confidential |

---

## 1. A1.1 — Availability Commitments

| Evidence Item | Description | Collection Method | Frequency |
|--------------|-------------|------------------|-----------|
| EV-A1-001 | SLA agreements with tenants | Contract management | Annual |
| EV-A1-002 | Uptime monitoring report | Monitoring platform | Monthly |
| EV-A1-003 | SLA breach notifications (if any) | Incident records | Per event |
| EV-A1-004 | Service status page history | Status page | Quarterly |

### Uptime Report Template

| Month | Target Uptime | Actual Uptime | Incidents | Breach |
|-------|-------------|--------------|----------|--------|
| January | 99.9% | [X]% | [X] | ☐ Yes ☐ No |
| February | 99.9% | [X]% | [X] | ☐ Yes ☐ No |
| ... | | | | |

## 2. A1.2 — Capacity Management

| Evidence Item | Description | Collection Method | Frequency |
|--------------|-------------|------------------|-----------|
| EV-A1-010 | Capacity planning report | Engineering | Quarterly |
| EV-A1-011 | Resource utilisation metrics | Monitoring platform | Monthly |
| EV-A1-012 | Auto-scaling event log | Infrastructure | Monthly |
| EV-A1-013 | Load testing results | Engineering | Annual |
| EV-A1-014 | Database performance metrics | DBA | Monthly |

## 3. A1.3 — Availability Incident Response

| Evidence Item | Description | Collection Method | Frequency |
|--------------|-------------|------------------|-----------|
| EV-A1-020 | Availability incident records | Incident management | Per event |
| EV-A1-021 | Availability alerting rules | Monitoring platform | Annual |
| EV-A1-022 | On-call schedule for operations | Scheduling system | Quarterly |

## 4. A1.4 — Recovery Procedures

| Evidence Item | Description | Collection Method | Frequency |
|--------------|-------------|------------------|-----------|
| EV-A1-030 | Backup and recovery policy | Document review | Annual |
| EV-A1-031 | Backup success rate (monthly) | Backup system | Monthly |
| EV-A1-032 | Backup restore test results | DR testing | Quarterly |
| EV-A1-033 | RPO/RTO achievement metrics | Operations | Quarterly |
| EV-A1-034 | Disaster recovery plan test report | Annual exercise | Annual |

### Backup Success Rate

| Month | Backups Attempted | Successful | Failed | Success Rate |
|-------|------------------|-----------|--------|-------------|
| | [X] | [X] | [X] | [X]% |

### RPO/RTO Achievement

| Quarter | RPO Target | RPO Actual | RTO Target | RTO Actual |
|---------|-----------|-----------|-----------|-----------|
| Q1 | [X] hours | [X] hours | [X] hours | [X] hours |
| Q2 | | | | |
| Q3 | | | | |
| Q4 | | | | |

## 5. A1.5 — Redundancy

| Evidence Item | Description | Collection Method | Frequency |
|--------------|-------------|------------------|-----------|
| EV-A1-040 | Architecture diagram (showing redundancy) | Engineering | Annual |
| EV-A1-041 | Failover test results | DR testing | Annual |
| EV-A1-042 | Multi-region deployment verification | Infrastructure | Quarterly |
| EV-A1-043 | CDN and DDoS protection configuration | Operations | Quarterly |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [YYYY-MM-DD] | [Head of Operations] | Initial evidence register |

---

*This evidence register supports SOC 2 Type II audit for A1 (Availability). Evidence is collected per the defined frequency and retained for the audit period plus 1 year.*

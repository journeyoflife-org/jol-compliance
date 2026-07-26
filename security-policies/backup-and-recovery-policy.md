# Backup and Recovery Policy

**Journey Of Life UAB — Information Backup and Disaster Recovery (ISO 27001 A.8.13–A.8.14)**

| Field | Value |
|-------|-------|
| **Document ID** | JOL-SEC-BKP-001 |
| **Policy Owner** | [Head of Operations] |
| **Version** | 1.0 |
| **Effective Date** | [YYYY-MM-DD] |
| **Classification** | Internal — Confidential |

---

## 1. Recovery Objectives

| Metric | Target | Scope |
|--------|--------|-------|
| **Recovery Point Objective (RPO)** | 4 hours | Maximum acceptable data loss |
| **Recovery Time Objective (RTO)** | 24 hours | Maximum acceptable downtime |
| **Backup Success Rate** | ≥99.5% | Monthly aggregate |

## 2. Backup Schedule

| Backup Type | Frequency | Retention | Encryption | Storage Location |
|------------|-----------|----------|-----------|-----------------|
| Full database backup | Daily (02:00 UTC) | 30 days (daily), 12 weeks (weekly), 1 year (monthly) | AES-256 | Primary region + secondary region |
| Incremental backup | Every 4 hours | 7 days | AES-256 | Primary region |
| Transaction log backup | Continuous | 7 days | AES-256 | Primary region |
| Configuration backup | Daily | 90 days | AES-256 | Primary + secondary region |
| File system backup | Daily | 30 days | AES-256 | Primary region |
| Infrastructure as Code | Per commit (Git) | Indefinite | N/A (Git) | GitHub |

## 3. Backup Requirements

| Requirement | Implementation |
|------------|---------------|
| Encryption | AES-256 encryption for all backup data |
| Key separation | Backup encryption keys stored separately from backup data |
| Immutability | Write-once storage for backup retention period |
| Integrity verification | Automated checksum verification after each backup |
| Access control | Restricted to Operations team; MFA required |
| Off-site storage | Secondary region backup (EU-Central) |
| Offline copies | Monthly offline backup copies stored in secure facility |

## 4. Restore Testing

| Test Type | Frequency | Scope | Pass Criteria |
|-----------|-----------|-------|-------------|
| Full restore test | Quarterly | Complete database restore | Restore within RTO; data integrity verified |
| Point-in-time restore | Quarterly | Restore to specific timestamp | Data matches expected state |
| File-level restore | Monthly | Individual file/document restore | File integrity verified |
| DR failover test | Annual | Full infrastructure failover | All services operational within RTO |

## 5. Disaster Recovery Plan

### 5.1 Activation Criteria

| Scenario | DR Activation |
|----------|-------------|
| Primary region total outage | Automatic failover |
| Database corruption (unrecoverable) | Manual activation by Head of Ops |
| Ransomware / data destruction | Manual activation by CISO |
| Natural disaster affecting primary data centre | Automatic failover |

### 5.2 Failover Process

| Step | Action | Owner | SLA |
|------|--------|-------|-----|
| 1 | Detect failure / receive alert | Monitoring (automated) | Immediate |
| 2 | Assess severity and scope | On-call engineer | 15 minutes |
| 3 | Activate DR plan | Head of Ops / CISO | 30 minutes |
| 4 | Initiate failover to secondary region | Operations team | 2 hours |
| 5 | Verify service restoration | Operations + Engineering | 4 hours |
| 6 | Notify tenants and stakeholders | Communications Lead | 4 hours |
| 7 | Begin primary region recovery | Operations team | 24 hours |

### 5.3 Return to Primary

- Primary region fully restored and verified before switching back
- Data synchronisation validated before failback
- Failback during maintenance window where possible

## 6. Backup Monitoring and Alerting

| Alert | Condition | Notification |
|-------|-----------|-------------|
| Backup failure | Any backup job fails | Immediate: Operations + Head of Ops |
| Backup size anomaly | >50% deviation from baseline | Warning: Operations |
| Restore test failure | Quarterly test fails to meet RTO | Escalation: Head of Ops + CISO |
| Storage capacity | >80% backup storage utilisation | Warning: Operations |

## 7. Compliance Monitoring

| Activity | Frequency | Owner |
|----------|-----------|-------|
| Backup job review | Daily (automated) | Operations |
| Backup success rate report | Monthly | Head of Ops |
| Restore test execution and report | Quarterly | Operations |
| DR plan review and update | Annual | Head of Ops |
| Backup encryption audit | Annual | CISO |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [YYYY-MM-DD] | [Head of Operations] | Initial policy creation |

---

*This Backup and Recovery Policy governs data protection and disaster recovery for the Journey Of Life platform. It supports ISO 27001 A.8.13–A.8.14, SOC 2 A1.4–A1.5, and GDPR Art. 32(1)(c) ability to restore availability.*

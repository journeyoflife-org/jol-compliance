# Incident Response Playbook

## Document Information

| Field | Value |
|-------|-------|
| Document ID | JOL-DOC-IR-PLAY-001 |
| Owner | CISO |
| Version | 1.0 |
| Classification | RESTRICTED |
| Effective Date | [DATE] |
| Next Review | [DATE + 6 MONTHS] |
| Approved By | [APPROVER NAME] |

---

## 1. Purpose

This playbook provides step-by-step procedures for Journey Of Life UAB's incident response team (CSIRT) to detect, analyse, contain, eradicate, and recover from security incidents. It aligns with ISO 27001:2022 Annex A.5.24–A.5.28 (Incident management) and SOC 2 CC7 (System Operations), and supports GDPR Art. 33–34 breach notification obligations.

---

## 2. Incident Response Team (CSIRT)

| Role | Primary | Backup | Contact |
|------|---------|--------|---------|
| Incident Commander | CISO | Deputy CISO | [PHONE / EMAIL] |
| Technical Lead | Senior Security Engineer | DevOps Lead | [PHONE / EMAIL] |
| DPO (Privacy Breach) | duomenu.apsauga@jol-hub.com | Deputy DPO | [PHONE / EMAIL] |
| Legal Counsel | [NAME] | External Counsel | [PHONE / EMAIL] |
| Communications Lead | Head of Communications | [BACKUP] | [PHONE / EMAIL] |
| HR Representative | HR Director | [BACKUP] | [PHONE / EMAIL] |

### 2.1 Escalation Matrix

| Severity | Response Time | Notification | Authority |
|----------|--------------|--------------|-----------|
| P1 – Critical (data breach, ransomware, full outage) | 15 minutes | CEO, Board, Legal, DPO | Incident Commander |
| P2 – High (partial breach, malware, privilege escalation) | 30 minutes | CISO, Legal, DPO | Incident Commander |
| P3 – Medium (phishing, unauthorised access attempt) | 2 hours | CISO, IT Security | Technical Lead |
| P4 – Low (policy violation, minor anomaly) | 8 hours | IT Security | Security Engineer |

---

## 3. Incident Lifecycle (NIST SP 800-61r2)

```
┌──────────┐    ┌──────────────┐    ┌──────────────┐    ┌───────────────┐    ┌──────────────┐
│Detection │───▶│ Analysis &   │───▶│ Containment, │───▶│ Post-Incident │───▶│ Lessons      │
│& Triage  │    │ Escalation   │    │ Eradication, │    │ Activity      │    │ Learned      │
│          │    │              │    │ Recovery     │    │               │    │              │
└──────────┘    └──────────────┘    └──────────────┘    └───────────────┘    └──────────────┘
```

---

## 4. Phase 1 — Detection and Triage

### 4.1 Detection Sources

| Source | Examples | Monitoring Tool |
|--------|----------|-----------------|
| SIEM Alerts | Failed logins, anomalous data access, privilege escalation | [SIEM PLATFORM] |
| Endpoint Detection | Malware, suspicious processes, file integrity changes | [EDR PLATFORM] |
| Network Monitoring | DDoS, unusual outbound traffic, port scans | [IDS/IPS] |
| User Reports | Phishing emails, suspicious behaviour, lost devices | Ticketing system |
| Third-Party Reports | Vendor notifications, security researcher reports | Email: security@jol-hub.com |
| Vulnerability Scans | Critical CVEs in production systems | `audit-evidence/vulnerability-scans/` |
| Penetration Tests | Exploitable findings | `audit-evidence/penetration-tests/` |

### 4.2 Triage Checklist

```markdown
- [ ] **INCIDENT ID**: IR-[YYYY]-[NNNN]
- [ ] **Date/Time Detected**: [DATETIME UTC]
- [ ] **Detected By**: [NAME / SYSTEM]
- [ ] **Source**: [DETECTION SOURCE]
- [ ] **Affected Systems**: [LIST SYSTEMS]
- [ ] **Affected Data Types**: [PERSONAL DATA / FINANCIAL / CREDENTIALS / IP / NONE]
- [ ] **Estimated Scope**: [NUMBER OF USERS / RECORDS / SYSTEMS]
- [ ] **Initial Severity**: P1 / P2 / P3 / P4
- [ ] **Personal Data Involved?**: YES / NO → If YES, notify DPO immediately
- [ ] **Initial Description**: [BRIEF DESCRIPTION]
```

### 4.3 Triage Decision Tree

```
Is personal data involved or likely involved?
├── YES → Classify as potential GDPR breach → Notify DPO → Proceed to Phase 2
│         within 1 hour (GDPR Art. 33 clock starts at awareness)
└── NO  → Continue triage

Is there active unauthorised access or data exfiltration?
├── YES → Classify P1 or P2 → Immediate containment → Phase 2
└── NO  → Continue assessment

Is a production service degraded or unavailable?
├── YES → Classify based on SLA impact → Phase 2
└── NO  → Classify P3 or P4 → Standard investigation
```

---

## 5. Phase 2 — Analysis and Escalation

### 5.1 Analysis Actions

| # | Action | Tool / Method | Document Evidence |
|---|--------|---------------|-------------------|
| 1 | Capture volatile memory and disk images | [FORENSIC TOOL] | Forensic image hash |
| 2 | Analyse system and application logs | [LOG ANALYSIS TOOL] | Log export |
| 3 | Identify attack vector and timeline | Correlation analysis | Timeline document |
| 4 | Determine data accessed/exfiltrated | Database audit logs, DLP | Data inventory impact |
| 5 | Identify threat actor (if applicable) | Threat intelligence feeds | Threat assessment |
| 6 | Assess business impact | Impact matrix | Business impact assessment |
| 7 | Update severity classification | Escalation matrix | Updated incident record |

### 5.2 GDPR Breach Assessment (Art. 33–34)

If personal data is involved, the DPO must assess within **1 hour**:

| Question | Assessment |
|----------|-----------|
| Is there a risk to the rights and freedoms of data subjects? | [YES / NO] |
| Is there a **high** risk to the rights and freedoms of data subjects? | [YES / NO] |
| Can the breach be contained to prevent further data loss? | [YES / NO] |
| Is notification to the supervisory authority (VDAI) required within 72 hours? | [YES / NO] |
| Is notification to affected data subjects required without undue delay? | [YES / NO] |

**GDPR Notification Timeline:**
- **Art. 33 (Supervisory Authority)**: Notify VDAI within **72 hours** of becoming aware, unless the breach is unlikely to result in a risk to rights and freedoms
- **Art. 34 (Data Subjects)**: Notify without undue delay if the breach is likely to result in a **high risk**

### 5.3 Breach Notification Template (VDAI — Art. 33)

```markdown
**To**: Valstybinė duomenų apsaugos inspekcija (VDAI)
**From**: Journey Of Life UAB, DPO — duomenu.apsauga@jol-hub.com
**Subject**: Personal Data Breach Notification — IR-[YYYY]-[NNNN]

1. Nature of the breach: [DESCRIPTION]
2. Categories and approximate number of data subjects concerned: [NUMBER]
3. Categories and approximate number of personal data records concerned: [NUMBER]
4. Name and contact details of the DPO: duomenu.apsauga@jol-hub.com
5. Likely consequences of the breach: [ASSESSMENT]
6. Measures taken or proposed to address the breach: [MEASURES]
7. Date and time of the breach: [DATETIME UTC]
8. Date and time of awareness: [DATETIME UTC]
```

---

## 6. Phase 3 — Containment, Eradication, and Recovery

### 6.1 Containment Strategies

| Scenario | Immediate Containment | Evidence Preservation |
|----------|----------------------|----------------------|
| **Ransomware** | Isolate affected systems from network; do NOT power off | Memory dump before isolation |
| **Data Exfiltration** | Block egress IPs, revoke compromised credentials | Network capture, log export |
| **Compromised Account** | Disable account, revoke all sessions, reset passwords | Session logs, authentication logs |
| **Vulnerable Service** | Apply WAF rules, disable service, or firewall block | Service logs, vulnerability scan |
| **Insider Threat** | Revoke access, preserve workstation | Forensic image, HR involvement |
| **Phishing Campaign** | Block sender domain, remove emails from mailboxes | Email headers, click tracking |
| **DDoS Attack** | Activate DDoS mitigation service, engage ISP | Traffic analysis, ISP reports |

### 6.2 Eradication Steps

1. **Identify root cause** — patch vulnerability, fix misconfiguration, or remove malware
2. **Remove threat artifacts** — delete malicious files, remove backdoors, reset compromised credentials
3. **Strengthen controls** — apply additional hardening, update firewall rules, increase monitoring
4. **Verify eradication** — re-scan affected systems, review logs for residual indicators of compromise

### 6.3 Recovery Procedures

| Step | Action | Validation |
|------|--------|-----------|
| 1 | Restore systems from clean backups (verified pre-incident) | Backup integrity check |
| 2 | Rebuild compromised systems from golden images | Configuration verification |
| 3 | Apply all security patches and hardening | Vulnerability scan (clean) |
| 4 | Restore data from verified clean backups | Data integrity verification |
| 5 | Re-enable network connectivity with enhanced monitoring | Traffic baseline comparison |
| 6 | Monitor restored systems for 72 hours with heightened alerting | No anomalous activity |
| 7 | Declare recovery complete and notify stakeholders | Incident Commander sign-off |

---

## 7. Phase 4 — Post-Incident Activity

### 7.1 Post-Incident Review (Within 10 Business Days)

**Attendees**: CSIRT, affected business units, DPO (if personal data involved)

**Agenda:**
1. Incident timeline reconstruction
2. Response effectiveness evaluation
3. What went well
4. What needs improvement
5. Corrective actions and owners
6. Policy/procedure updates required

### 7.2 Post-Incident Report Template

```markdown
# Post-Incident Report — IR-[YYYY]-[NNNN]

## Summary
- **Incident Type**: [TYPE]
- **Severity**: P1 / P2 / P3 / P4
- **Duration**: [DETECTION] to [RESOLUTION] ([HOURS/DAYS])
- **Impact**: [SUMMARY OF IMPACT]

## Timeline
| Date/Time (UTC) | Event | Actor |
|-----------------|-------|-------|
| [TIMESTAMP] | [EVENT] | [ACTOR] |

## Root Cause
[ROOT CAUSE ANALYSIS]

## Impact Assessment
- **Systems Affected**: [LIST]
- **Data Compromised**: [YES/NO — if yes, describe]
- **Business Impact**: [REVENUE / REPUTATION / OPERATIONAL]
- **Regulatory Impact**: [NOTIFICATION REQUIRED — YES/NO]

## Response Effectiveness
| Metric | Target | Actual | Met? |
|--------|--------|--------|------|
| Detection to triage | 15 min (P1) | [TIME] | [YES/NO] |
| Triage to containment | 1 hour (P1) | [TIME] | [YES/NO] |
| Containment to eradication | 4 hours (P1) | [TIME] | [YES/NO] |
| Total resolution time | 24 hours (P1) | [TIME] | [YES/NO] |

## Corrective Actions
| # | Action | Owner | Due Date | Status |
|---|--------|-------|----------|--------|
| 1 | [ACTION] | [OWNER] | [DATE] | [OPEN/CLOSED] |

## Lessons Learned
[KEY FINDINGS AND IMPROVEMENTS]
```

### 7.3 Metrics and KPIs

| KPI | Target | Measurement |
|-----|--------|-------------|
| Mean Time to Detect (MTTD) | < 15 minutes for P1 | Time from incident start to detection |
| Mean Time to Triage (MTTT) | < 15 minutes for P1 | Time from detection to classification |
| Mean Time to Contain (MTTC) | < 1 hour for P1 | Time from triage to containment |
| Mean Time to Resolve (MTTR) | < 24 hours for P1 | Time from detection to resolution |
| GDPR notification compliance | 100% within 72 hours | Notifications sent within deadline |
| Post-incident review completion | 100% within 10 business days | Reviews completed on time |

---

## 8. Specific Incident Playbooks

### 8.1 Playbook: Ransomware Attack

| Step | Action | Time | Owner |
|------|--------|------|-------|
| 1 | Isolate infected endpoints from network (pull cable / disable Wi-Fi) | Immediate | IT Security |
| 2 | Do NOT pay ransom or communicate with attackers | Immediate | Incident Commander |
| 3 | Capture forensic images of affected systems | +30 min | Forensics |
| 4 | Identify ransomware variant and attack vector | +2 hours | IT Security |
| 5 | Assess scope of encryption across estate | +4 hours | IT Operations |
| 6 | Check backup integrity (ensure backups not encrypted) | +4 hours | IT Operations |
| 7 | Notify DPO if personal data is affected | +1 hour | Incident Commander |
| 8 | Begin restoration from clean offline backups | +8 hours | IT Operations |
| 9 | Rebuild affected systems from golden images | +24 hours | IT Operations |
| 10 | Conduct full malware scan on restored environment | +36 hours | IT Security |
| 11 | File report with Lithuanian Police (if criminal activity) | +24 hours | Legal |

### 8.2 Playbook: Data Breach (Personal Data)

| Step | Action | Time | Owner |
|------|--------|------|-------|
| 1 | Identify scope: which data subjects, records, categories | +1 hour | DPO + IT Security |
| 2 | Contain the breach (revoke access, block exfiltration) | +1 hour | IT Security |
| 3 | Assess risk to data subjects (likelihood × severity) | +2 hours | DPO |
| 4 | If risk exists: prepare Art. 33 notification to VDAI | +4 hours | DPO |
| 5 | Submit Art. 33 notification within 72 hours | ≤72 hours | DPO |
| 6 | If high risk: prepare Art. 34 notification to data subjects | +24 hours | DPO + Comms |
| 7 | Notify affected third-country supervisory authorities if applicable | +72 hours | DPO |
| 8 | Update ROPA with breach record (Art. 33(5)) | +48 hours | DPO |
| 9 | Conduct post-incident review | +10 days | CSIRT |

### 8.3 Playbook: Compromised Employee Account

| Step | Action | Time | Owner |
|------|--------|------|-------|
| 1 | Disable compromised account immediately | Immediate | IT Operations |
| 2 | Revoke all active sessions (SSO, VPN, applications) | Immediate | IT Operations |
| 3 | Reset passwords for all linked accounts | +15 min | IT Security |
| 4 | Review authentication logs for lateral movement | +2 hours | IT Security |
| 5 | Check for data access/exfiltration during compromise | +4 hours | IT Security |
| 6 | Scan endpoint for malware/keyloggers | +2 hours | IT Security |
| 7 | Interview employee (social engineering assessment) | +4 hours | HR + IT Security |
| 8 | Re-enable account with MFA reset and monitoring | +8 hours | IT Operations |
| 9 | Mandatory security awareness re-training | +48 hours | HR + CISO |

### 8.4 Playbook: DDoS Attack

| Step | Action | Time | Owner |
|------|--------|------|-------|
| 1 | Confirm DDoS (vs. legitimate traffic spike) | +15 min | IT Operations |
| 2 | Activate DDoS mitigation service ([PROVIDER]) | +15 min | IT Operations |
| 3 | Notify ISP and request upstream filtering | +30 min | IT Operations |
| 4 | Implement rate limiting and geo-blocking if applicable | +30 min | DevOps |
| 5 | Monitor service availability and adjust thresholds | Ongoing | IT Operations |
| 6 | Assess impact on SLA and notify affected customers if required | +4 hours | Communications |
| 7 | Post-attack traffic analysis and playbook update | +5 days | IT Security |

---

## 9. Evidence Preservation

### 9.1 Chain of Custody

All evidence must be handled with a documented chain of custody:

| Field | Value |
|-------|-------|
| Evidence ID | [UNIQUE ID] |
| Description | [DESCRIPTION] |
| Date/Time Collected | [DATETIME UTC] |
| Collected By | [NAME] |
| Hash (SHA-256) | [HASH VALUE] |
| Storage Location | [SECURE LOCATION] |
| Transferred To | [NAME] on [DATE] |
| Transfer Reason | [REASON] |

### 9.2 Evidence Retention

| Incident Severity | Retention Period |
|-------------------|-----------------|
| P1 – Critical | 7 years |
| P2 – High | 5 years |
| P3 – Medium | 3 years |
| P4 – Low | 1 year |

Evidence involving personal data must comply with the data retention policy (`gdpr/retention-policies/data-retention-policy.md`).

---

## 10. Communication Templates

### 10.1 Internal Notification (All Staff — P1/P2)

```
Subject: [SECURITY INCIDENT — ACTION REQUIRED / FOR AWARENESS]

Team,

We are currently responding to a security incident affecting [SYSTEMS/SERVICES].

What we know:
- [BRIEF DESCRIPTION — do not include sensitive technical details]

What you need to do:
- [SPECIFIC ACTIONS, e.g., "Do not access System X", "Change your password", "Report any suspicious emails to security@jol-hub.com"]

What we are doing:
- [SUMMARY OF RESPONSE ACTIVITIES]

Next update: [TIMEFRAME]

CSIRT
```

### 10.2 Customer Notification (If Required Under GDPR Art. 34)

```
Subject: Important Notice Regarding Your Personal Data

Dear [NAME],

We are writing to inform you about a security incident that may affect your personal data.

What happened:
[PLAIN-LANGUAGE DESCRIPTION]

What data was affected:
[CATEGORIES OF PERSONAL DATA]

What we are doing:
[MEASURES TAKEN AND PLANNED]

What you can do:
[RECOMMENDED STEPS FOR THE INDIVIDUAL]

Contact us:
If you have questions, please contact our DPO at duomenu.apsauga@jol-hub.com or call [PHONE].

We sincerely regret the concern this may cause and are committed to protecting your data.

Sincerely,
Data Protection Officer
Journey Of Life UAB
```

---

## 11. Related Documents

| Document | Location |
|----------|----------|
| Incident Response Policy | `security-policies/incident-response-policy.md` |
| Data Breach Notification Procedure | `gdpr/dsr-procedures/data-subject-rights-procedure.md` |
| Data Retention Policy | `gdpr/retention-policies/data-retention-policy.md` |
| ISO 27001 ISMS Policy (A.5.24–A.5.28) | `iso27001/policies/information-security-policy.md` |
| SOC 2 System Operations Evidence | `soc2/evidence/cc7/system-operations-evidence.md` |
| Audit Preparation Guide | `docs/audit-preparation-guide.md` |

---

## Document History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [DATE] | [AUTHOR] | Initial release |

## Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| CISO | [NAME] | [SIGNATURE] | [DATE] |
| DPO | [NAME] | [SIGNATURE] | [DATE] |
| CEO | [NAME] | [SIGNATURE] | [DATE] |

---

*This document is the property of Journey Of Life UAB. It is classified as RESTRICTED and must not be distributed without authorisation. Test this playbook at least annually through tabletop exercises. Legal review is recommended before use in live incident response.*

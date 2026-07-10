# Incident Response Policy

**Journey Of Life UAB — Security Incident Management (ISO 27001 A.5.24–A.5.28, GDPR Art. 33–34)**

| Field | Value |
|-------|-------|
| **Document ID** | JOL-SEC-IR-001 |
| **Policy Owner** | [CISO Name] |
| **Version** | 1.0 |
| **Effective Date** | [YYYY-MM-DD] |
| **Classification** | Internal — All Staff |

---

## 1. Purpose

Establishes the framework for detecting, reporting, assessing, responding to, and learning from information security incidents, supporting ISO 27001 A.5.24–A.5.28, SOC 2 CC7.3–CC7.4, and GDPR Art. 33–34.

## 2. Definitions

- **Security event:** Observable occurrence relevant to security (e.g., failed login, firewall block)
- **Security incident:** Security event that indicates a probable compromise of confidentiality, integrity, or availability
- **Personal data breach:** Incident resulting in accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to personal data (GDPR Art. 4(12))

## 3. Severity Classification

| Severity | Description | Response SLA | Escalation |
|----------|------------|-------------|-----------|
| **P1 — Critical** | Active data breach, platform-wide compromise, significant data loss | Triage: 15 min | CISO + CEO immediately |
| **P2 — High** | Targeted attack, privileged access compromise, data exfiltration attempt | Triage: 1 hour | CISO within 1 hour |
| **P3 — Medium** | Successful phishing, malware infection (contained), single-account compromise | Triage: 4 hours | CISO within 4 hours |
| **P4 — Low** | Policy violation, unsuccessful attack attempt, minor security event | Triage: 24 hours | IT Security |

## 4. Incident Response Team

| Role | Responsibility | Availability |
|------|---------------|-------------|
| **Incident Commander** (CISO) | Overall incident management, escalation decisions | 24/7 on-call rotation |
| **Technical Lead** | Investigation, containment, eradication | 24/7 on-call rotation |
| **DPO** | GDPR breach assessment, supervisory authority notification | 24/7 on-call rotation |
| **Communications Lead** | Internal/external communications, tenant notifications | Business hours + on-call |
| **Legal Counsel** | Legal obligations, regulatory notifications, evidence preservation | As needed |

## 5. Response Process

### Phase 1: Detection and Reporting

- All personnel must report suspected incidents to **security@jol-hub.com** or the incident hotline
- Automated detection via SIEM, endpoint protection, and monitoring
- Anonymous reporting channel available

### Phase 2: Triage and Classification

- Incident Commander assesses and classifies severity within SLA
- Determine if incident involves personal data (triggers GDPR notification)
- Activate full IR team based on severity

### Phase 3: Containment

- **Short-term:** Isolate affected systems, block attacker access, preserve evidence
- **Long-term:** Apply patches, change credentials, update firewall rules
- Do not destroy evidence — preserve forensic artefacts

### Phase 4: Eradication

- Remove root cause (patch vulnerability, remove malware, revoke compromised credentials)
- Verify eradication through scanning and testing

### Phase 5: Recovery

- Restore affected systems from clean backups
- Verify system integrity before returning to production
- Monitor restored systems for signs of re-compromise

### Phase 6: Lessons Learned

- Post-incident review within **5 business days** of closure
- Document root cause, timeline, impact, and improvements
- Update risk register and controls as needed
- Share lessons (sanitised) with relevant teams

## 6. GDPR Breach Notification (Art. 33–34)

| Notification | Recipient | Deadline | Trigger |
|-------------|----------|----------|---------|
| Supervisory authority | VDAI / DVI / AKI (as applicable) | **≤72 hours** from awareness | Personal data breach (unless unlikely to result in risk) |
| Data subjects | Affected individuals | **Without undue delay** | Personal data breach likely to result in **high risk** |
| Tenant (controller) | Institution administrator | **≤24 hours** from awareness | Breach affecting tenant's data |
| Sub-processor | Journey Of Life (as controller's processor) | **≤24 hours** from awareness | Breach in sub-processor's systems |

## 7. Evidence Collection

| Requirement | Standard |
|------------|---------|
| Chain of custody | Documented for all evidence |
| Forensic imaging | Bit-for-bit copies of affected systems |
| Log preservation | Minimum 12-month retention; extended during incidents |
| Timestamp accuracy | NTP-synchronised clocks (ISO 27001 A.8.17) |
| Admissibility | Collection methods compatible with legal proceedings |

## 8. Communication Plan

| Audience | Method | Owner | Timing |
|----------|--------|-------|--------|
| Internal staff | Email / all-hands | Communications Lead | As needed |
| Affected tenants | Direct email + phone | Account Manager + DPO | ≤24 hours |
| Supervisory authority | Official notification form | DPO | ≤72 hours |
| Media (if applicable) | Press release (approved by CEO) | Communications Lead | As directed |
| Law enforcement | Direct contact | Legal Counsel + CISO | As needed |

## 9. Testing and Training

- **Tabletop exercises:** Bi-annual (covering data breach, ransomware, insider threat scenarios)
- **IR team training:** Annual refresher; new member orientation within 30 days
- **All-staff awareness:** Annual training on incident identification and reporting

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [YYYY-MM-DD] | [CISO Name] | Initial policy creation |

---

*This Incident Response Policy governs all security incident management activities for Journey Of Life UAB. It is tested bi-annually and reviewed annually. See `docs/incident-response-playbook.md` for detailed response procedures.*

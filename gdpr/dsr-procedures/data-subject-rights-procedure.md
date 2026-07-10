# Data Subject Rights (DSR) Procedure

**Journey Of Life UAB — Procedure for Handling Data Subject Rights Requests**

| Field | Value |
|-------|-------|
| **Document ID** | JOL-DSR-001 |
| **Organisation** | Journey Of Life UAB |
| **Procedure Owner** | [DPO Name] — duomenu.apsauga@jol-hub.com |
| **Version** | 1.0 |
| **Effective Date** | [YYYY-MM-DD] |
| **Last Reviewed** | [YYYY-MM-DD] |
| **Next Review Due** | [YYYY-MM-DD] |
| **Classification** | Internal — Confidential |

---

## 1. Purpose and Scope

This procedure establishes the operational workflow for receiving, verifying, processing, and responding to Data Subject Rights (DSR) requests under GDPR Articles 15–22.

### 1.1 Applicable Rights

| Right | GDPR Article | Description | Platform Mechanism |
|-------|-------------|-------------|-------------------|
| **Access** | Art. 15 | Confirm processing and provide copy of data | Self-service export + manual |
| **Rectification** | Art. 16 | Correct inaccurate or incomplete data | Self-service profile edit + manual |
| **Erasure** | Art. 17 | Delete personal data ("right to be forgotten") | Account deletion workflow |
| **Restriction** | Art. 18 | Temporarily halt processing | Data flagging mechanism |
| **Portability** | Art. 20 | Receive data in machine-readable format | Self-service JSON/CSV export |
| **Objection** | Art. 21 | Object to processing (e.g., direct marketing) | Opt-out mechanism |
| **Automated decisions** | Art. 22 | Not be subject to solely automated decisions | Human review process |
| **Withdraw consent** | Art. 7(3) | Withdraw previously given consent | Preference centre |

### 1.2 Scope

This procedure applies to:
- All personal data processed by Journey Of Life UAB as controller or processor
- Requests from any data subject regardless of EU member state
- Requests received via any channel: Platform, email, post, telephone, supervisory authority

---

## 2. Request Intake

### 2.1 Channels

| Channel | Method | Routing |
|---------|--------|---------|
| **Platform self-service** | Settings → Privacy → Data Requests | Automated ticket creation |
| **Email** | duomenu.apsauga@jol-hub.com | DPO inbox → ticket system |
| **Postal mail** | [Company Address] | Scanned → DPO inbox → ticket system |
| **Telephone** | [Phone Number] | Logged by support → ticket system |
| **Supervisory authority** | Via VDAI/DVI/AKI | Escalated to DPO immediately |
| **Tenant administrator** | Via institution admin panel | Forwarded to DPO |

### 2.2 Intake Checklist

Upon receipt, the DSR handler shall:

1. [ ] Log the request in the DSR Tracker (`scripts/gdpr_dsr_tracker.py`)
2. [ ] Assign a unique reference number: `DSR-[YYYY]-[NNNN]`
3. [ ] Record: date received, channel, data subject identifier, right(s) requested
4. [ ] Calculate the response deadline: **30 calendar days** from receipt
5. [ ] Send acknowledgment to the data subject within **48 hours**
6. [ ] Assess if the request is complex (may require extension)

---

## 3. Identity Verification

### 3.1 Verification Methods

| Channel | Primary Method | Fallback Method |
|---------|---------------|----------------|
| **Platform (authenticated)** | Active session — identity pre-verified | N/A |
| **Email (from registered address)** | Match to registered email on file | Request additional ID |
| **Email (from unregistered address)** | Government-issued ID copy + registered email confirmation | Video call verification |
| **Postal mail** | Government-issued ID copy (redacted to minimum necessary) + signature match | N/A |
| **Telephone** | Pre-agreed security questions (minimum 3) | Callback to registered number |
| **Authorised representative** | Written power of attorney + representative ID + data subject ID | N/A |

### 3.2 Verification Rules

- Identity verification must be completed within **7 calendar days** of receipt
- If verification fails after 2 attempts, the request may be refused (document justification)
- ID copies are used **solely for verification** and destroyed within **72 hours** of verification
- For children's data: verify **parental/guardian authority** in addition to identity
- Verification efforts and outcomes are logged in the DSR Tracker

### 3.3 Manifestly Unfounded or Excessive Requests

A request may be refused or charged for if:
- The same data has been provided within the last 6 months (without material change)
- The request is clearly aimed at causing disruption
- The volume of requests from the same individual is disproportionate

**Before refusing:** Consult with the DPO. Document the refusal rationale. Inform the data subject of their right to lodge a complaint with the supervisory authority.

---

## 4. Processing Workflows

### 4.1 Right of Access (Art. 15)

| Step | Action | Owner | SLA |
|------|--------|-------|-----|
| 1 | Verify identity (Section 3) | DSR Handler | Day 0–7 |
| 2 | Identify all systems holding the data subject's data | DSR Handler + Engineering | Day 7–10 |
| 3 | Extract data from all identified systems | Engineering | Day 10–17 |
| 4 | Redact third-party data (if applicable) | DSR Handler | Day 17–20 |
| 5 | Compile response in concise, intelligible format | DSR Handler | Day 20–25 |
| 6 | DPO quality review | DPO | Day 25–27 |
| 7 | Deliver response to data subject | DSR Handler | Day 27–30 |

**Response format:** Secure download link (time-limited, encrypted) or encrypted email attachment.

**Information to provide:**
- Purposes of processing
- Categories of personal data
- Recipients or categories of recipients
- Retention periods
- Existence of DSR rights
- Right to lodge a complaint with supervisory authority
- Source of data (if not collected directly)
- Existence of automated decision-making (Art. 22)

### 4.2 Right to Rectification (Art. 16)

| Step | Action | Owner | SLA |
|------|--------|-------|-----|
| 1 | Verify identity | DSR Handler | Day 0–7 |
| 2 | Review accuracy claim | DSR Handler + System Owner | Day 7–14 |
| 3 | If valid: correct data in all systems | Engineering | Day 14–21 |
| 4 | If disputed: flag data as "disputed" pending resolution | Engineering | Day 14–21 |
| 5 | Notify data subject of correction or refusal | DSR Handler | Day 21–28 |
| 6 | Notify recipients of corrected data (if applicable) | DSR Handler | Day 28–30 |

### 4.3 Right to Erasure (Art. 17)

| Step | Action | Owner | SLA |
|------|--------|-------|-----|
| 1 | Verify identity | DSR Handler | Day 0–7 |
| 2 | Assess erasure grounds (Art. 17(1) conditions) | DPO | Day 7–10 |
| 3 | Check for exceptions (Art. 17(3): legal obligation, public interest, legal claims) | DPO + Legal | Day 10–14 |
| 4 | If valid: execute deletion across all systems | Engineering | Day 14–21 |
| 5 | Flag data for exclusion from next backup cycle | Operations | Day 21–22 |
| 6 | Notify sub-processors of deletion requirement | DSR Handler | Day 22–25 |
| 7 | Confirm deletion to data subject | DSR Handler | Day 25–30 |

**Deletion exceptions (Art. 17(3)):**
- Exercise of freedom of expression and information
- Compliance with a legal obligation (e.g., tax records)
- Public interest in public health
- Archiving purposes in the public interest
- Establishment, exercise, or defence of legal claims

### 4.4 Right to Restriction (Art. 18)

| Step | Action | Owner | SLA |
|------|--------|-------|-----|
| 1 | Verify identity | DSR Handler | Day 0–7 |
| 2 | Apply "restricted" flag to data subject's records | Engineering | Day 7–10 |
| 3 | Ensure restricted data is excluded from processing (except storage) | Engineering | Day 10–14 |
| 4 | Confirm restriction to data subject | DSR Handler | Day 14–21 |
| 5 | Before lifting restriction: notify data subject | DSR Handler | Prior to lifting |

### 4.5 Right to Data Portability (Art. 20)

| Step | Action | Owner | SLA |
|------|--------|-------|-----|
| 1 | Verify identity | DSR Handler | Day 0–7 |
| 2 | Identify data within scope (data provided by the subject, processed by consent or contract) | DSR Handler | Day 7–10 |
| 3 | Generate export in JSON and/or CSV format | Engineering | Day 10–20 |
| 4 | DPO review for third-party data exclusion | DPO | Day 20–25 |
| 5 | Deliver via secure download or transmit to specified controller | DSR Handler | Day 25–30 |

**Supported formats:** JSON, CSV. Direct transfer to another controller upon request where technically feasible.

### 4.6 Right to Object (Art. 21)

| Step | Action | Owner | SLA |
|------|--------|-------|-----|
| 1 | Verify identity | DSR Handler | Day 0–7 |
| 2 | Identify processing activities the objection relates to | DSR Handler | Day 7–10 |
| 3 | Assess compelling legitimate grounds (if processing is based on Art. 6(1)(f)) | DPO + Legal | Day 10–17 |
| 4 | If no overriding grounds: cease processing | Engineering | Day 17–21 |
| 5 | If direct marketing: cease **immediately** (no assessment needed) | Engineering | Within 24 hours |
| 6 | Notify data subject | DSR Handler | Day 25–30 |

---

## 5. Response Timelines

| Scenario | Standard | Extension | Total Maximum |
|----------|---------|-----------|---------------|
| Standard request | 30 calendar days | N/A | 30 days |
| Complex request | 30 calendar days | +60 days (Art. 12(3)) | 90 days |
| Extension triggered | Inform data subject within 30 days of receipt | — | — |

**Complexity criteria:** Multiple requests, large volume of data, need to consult third parties, technically complex extraction.

---

## 6. Fees

| Scenario | Fee |
|----------|-----|
| First access request | **Free** |
| Manifestly unfounded or excessive requests | Reasonable fee based on administrative costs |
| Additional copies of previously provided data | Reasonable fee |

Fee decisions require DPO approval and must be communicated to the data subject before processing.

---

## 7. Escalation Matrix

| Trigger | Escalation Path | Response Time |
|---------|----------------|---------------|
| Request approaching Day 25 without resolution | Alert to DPO | Immediate |
| Request approaching Day 28 without resolution | Escalation to CISO | Immediate |
| Supervisory authority forwarded request | DPO direct handling | Within 24 hours |
| Request involving children's data | DPO mandatory review | Within 48 hours |
| Request involving special category data (Art. 9) | DPO mandatory review | Within 48 hours |
| Disputed identity verification | DPO + Legal | Within 72 hours |
| Potential litigation hold conflict | Legal Counsel | Within 24 hours |

---

## 8. Record Keeping

### 8.1 DSR Log Fields

| Field | Description |
|-------|-------------|
| Reference Number | DSR-[YYYY]-[NNNN] |
| Data Subject | Identifier (not name in log) |
| Right(s) Requested | Art. 15/16/17/18/20/21/22 |
| Date Received | [YYYY-MM-DD] |
| Channel | Platform / Email / Post / SA |
| Identity Verified | Yes / No / Pending |
| Response Deadline | [YYYY-MM-DD] |
| Extension Applied | Yes / No + justification |
| Outcome | Fulfilled / Partially fulfilled / Refused |
| Refusal Reason | [If applicable — Art. reference] |
| Date Responded | [YYYY-MM-DD] |
| Handler | [Name] |
| DPO Review | [Name + Date] |

### 8.2 Retention

DSR records are retained for **5 years** from resolution for audit and legal defence purposes, then securely deleted.

---

## 9. Template Response Letters

### 9.1 Acknowledgment (within 48 hours)

> **Subject:** Your Data Request — Reference DSR-[YYYY]-[NNNN]
>
> Dear [Data Subject],
>
> Thank you for your request regarding your personal data, received on [Date].
>
> We have logged your request under reference number **DSR-[YYYY]-[NNNN]** and will respond within **30 calendar days** (by [Deadline Date]).
>
> If we require additional information to verify your identity, we will contact you promptly.
>
> Kind regards,
> Data Protection Team
> Journey Of Life UAB
> duomenu.apsauga@jol-hub.com

### 9.2 Fulfilment — Access Request

> **Subject:** Your Data Access Request — DSR-[YYYY]-[NNNN]
>
> Dear [Data Subject],
>
> In response to your access request (ref: DSR-[YYYY]-[NNNN]), please find enclosed a copy of your personal data as processed by Journey Of Life.
>
> The enclosed document includes:
> - The categories of personal data we process
> - The purposes of processing
> - Recipients of your data
> - Retention periods
> - Your rights regarding this data
>
> The download link is valid for 7 days and is password-protected.
>
> If you have any questions, please contact us at duomenu.apsauga@jol-hub.com.
>
> Kind regards,
> Data Protection Team

### 9.3 Refusal

> **Subject:** Your Data Request — DSR-[YYYY]-[NNNN] — Partial Refusal
>
> Dear [Data Subject],
>
> Thank you for your request (ref: DSR-[YYYY]-[NNNN]).
>
> After careful review, we are unable to fully comply with your request for the following reason:
>
> [Specific legal basis for refusal — e.g., Art. 17(3)(b): compliance with legal obligation under Lithuanian Tax Administration Law Art. 40]
>
> You have the right to:
> - Lodge a complaint with the [relevant supervisory authority]
> - Seek a judicial remedy
>
> If you believe this refusal is incorrect, please contact us at duomenu.apsauga@jol-hub.com.
>
> Kind regards,
> Data Protection Team

---

## 10. Cross-References

| Document | Location |
|----------|----------|
| ROPA | `gdpr/ropa/ropa-template.md` |
| Privacy Policies | `gdpr/privacy-policies/` |
| Data Retention Policy | `gdpr/retention-policies/data-retention-policy.md` |
| DSR Tracker Script | `scripts/gdpr_dsr_tracker.py` |
| Incident Response Policy | `security-policies/incident-response-policy.md` |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [YYYY-MM-DD] | [DPO Name] | Initial procedure creation |

---

*This procedure governs the handling of Data Subject Rights requests for Journey Of Life UAB's multi-tenant platform in compliance with GDPR Articles 12, 15–22. It applies to all ~400,000 religious institutions and their members across 28 EU member states. Legal review is recommended before adoption.*

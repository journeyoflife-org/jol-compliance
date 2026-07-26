# Glossary of Compliance Terms

## Document Information

| Field | Value |
|-------|-------|
| Document ID | JOL-DOC-GLOS-001 |
| Owner | Chief Compliance Officer |
| Version | 1.0 |
| Classification | INTERNAL |
| Effective Date | [DATE] |
| Next Review | [DATE + 12 MONTHS] |

---

## A

**Access Control** — The practice of restricting access to information systems and data based on identity, role, and need-to-know. *See: `iso27001/procedures/access-control-procedure.md`*

**Adequacy Decision** — A European Commission determination that a non-EU country provides an adequate level of data protection, enabling unrestricted data transfers. *Reference: GDPR Art. 45*

**Annex A** — The appendix to ISO/IEC 27001:2022 containing 93 information security controls organised into four themes: Organisational (A.5), People (A.6), Physical (A.7), and Technological (A.8). *See: `iso27001/soa/statement-of-applicability.md`*

**Art. 28 (GDPR)** — Article requiring contracts between controllers and processors to specify subject-matter, duration, nature, purpose, data types, and obligations. *See: `vendor-register/dpa-template.md`*

**Asset Register** — A documented inventory of information assets, including their classification, owner, and location. *See: `iso27001/asset-register/asset-register.md`*

**Audit Trail** — Chronological record of system activities sufficient to enable reconstruction, review, and examination of events.

**Availability** — The property of being accessible and usable upon demand by an authorised entity. One of the SOC 2 Trust Services Criteria (A1).

---

## B

**Breach Notification** — The obligation under GDPR Art. 33–34 to notify the supervisory authority within 72 hours and affected data subjects without undue delay when a personal data breach is likely to result in risk. *See: `docs/incident-response-playbook.md`*

**Business Continuity Plan (BCP)** — A documented plan for maintaining or restoring business operations during and after a disruption.

---

## C

**CAPA (Corrective Action and Preventive Action)** — A systematic approach to investigate, identify root cause, correct, and prevent non-conformities. Required by ISO 27001 Clause 10.1.

**CC (Common Criteria)** — SOC 2 Trust Services Criteria categories CC1–CC9 covering control environment, communication, risk assessment, monitoring, control activities, access, operations, change management, and risk mitigation. *See: `soc2/trust-services-criteria/tsc-control-mapping.md`*

**CIA Triad** — The three fundamental principles of information security: Confidentiality, Integrity, and Availability.

**Classification (Data)** — The categorisation of data based on sensitivity and impact if compromised. *See: `security-policies/data-classification-policy.md`*

**Confidentiality** — The property that information is not made available or disclosed to unauthorised individuals, entities, or processes.

**Controller** — Under GDPR Art. 4(7), the natural or legal person determining the purposes and means of processing personal data. Journey Of Life UAB acts as a controller for its platform users' data.

**Cookie** — A small piece of data stored on a user's device by a web browser, used for session management, preferences, and tracking. Regulated by the ePrivacy Directive (2002/58/EC) Art. 5(3). *See: `gdpr/cookie-policies/cookie-policy.md`*

**CSIRT (Computer Security Incident Response Team)** — The team responsible for managing security incidents within the organisation.

---

## D

**DIN 66399** — German standard for media destruction specifying security levels (P1–P7 for paper, H1–H9 for hard drives, etc.).

**DPA (Data Processing Agreement)** — A contract between a data controller and data processor specifying processing obligations under GDPR Art. 28. *See: `vendor-register/dpa-template.md`*

**DPIA (Data Protection Impact Assessment)** — An assessment required under GDPR Art. 35 when processing is likely to result in high risk to data subjects' rights and freedoms. *See: `gdpr/dpias/dpia-template.md`*

**DPO (Data Protection Officer)** — The person designated under GDPR Art. 37–39 responsible for overseeing data protection compliance. Contact: duomenu.apsauga@jol-hub.com

**DSR (Data Subject Rights)** — Rights granted to individuals under GDPR Art. 15–22, including access, rectification, erasure, restriction, portability, and objection. *See: `gdpr/dsr-procedures/data-subject-rights-procedure.md`*

---

## E

**ePrivacy Directive** — Directive 2002/58/EC concerning the processing of personal data and the protection of privacy in electronic communications. Supplements the GDPR for electronic communications.

**Encryption** — The process of encoding data so that only authorised parties can access it. *See: `security-policies/encryption-policy.md`*

**Evidence (Audit)** — Documented information, records, or data used to demonstrate compliance with audit criteria. *See: `audit-evidence/` directory*

---

## G

**GDPR (General Data Protection Regulation)** — Regulation (EU) 2016/679 on the protection of natural persons with regard to the processing of personal data and on the free movement of such data. Effective 25 May 2018.

**Golden Image** — A standardised, security-hardened system image used as a baseline for deploying servers or workstations.

---

## H

**High Risk (GDPR)** — A threshold under GDPR requiring DPIA (Art. 35) and/or data subject notification (Art. 34). Factors include: systematic monitoring, large-scale processing, special category data, automated decision-making, and vulnerable data subjects.

---

## I

**Incident** — An unplanned interruption or reduction in quality of an IT service, or an event that has not yet impacted service but could. *See: `security-policies/incident-response-policy.md`*

**Integrity** — The property of safeguarding the accuracy and completeness of data and systems.

**ISMS (Information Security Management System)** — The systematic framework of policies, processes, and controls for managing information security risk, as required by ISO 27001. *See: `iso27001/policies/information-security-policy.md`*

**ISO/IEC 27001:2022** — International standard specifying requirements for establishing, implementing, maintaining, and continually improving an ISMS.

---

## J

**JML (Joiner, Mover, Leaver)** — The HR/IT process for managing employee access through their lifecycle: provisioning on hire, adjusting on role change, and revoking on departure.

---

## L

**Lawful Basis** — The six legal grounds for processing personal data under GDPR Art. 6(1): consent (a), contract (b), legal obligation (c), vital interests (d), public task (e), legitimate interests (f).

**Legitimate Interest Assessment (LIA)** — A documented balancing test required when relying on Art. 6(1)(f) as the lawful basis for processing.

---

## M

**MTTD (Mean Time to Detect)** — Average time from when a security incident begins to when it is detected.

**MTTR (Mean Time to Resolve)** — Average time from detection of a security incident to its resolution.

**Management Review** — A periodic review by top management of the ISMS's continuing suitability, adequacy, and effectiveness, as required by ISO 27001 Clause 9.3. *See: `iso27001/management-reviews/management-review-template.md`*

**Multi-Factor Authentication (MFA)** — An authentication method requiring two or more verification factors: something you know, something you have, or something you are.

---

## N

**NIST SP 800-61** — NIST Computer Security Incident Handling Guide providing a framework for incident response lifecycle.

**NIST 800-88** — NIST Guidelines for Media Sanitization defining three levels: Clear (overwrite), Purge (cryptographic erasure or degauss), and Destroy (physical destruction).

**Non-Conformity** — Non-fulfilment of a requirement. In ISO 27001 context, failure to meet ISMS requirements must be addressed through corrective action (Clause 10.1).

---

## P

**Penetration Test** — A simulated attack on a system to identify exploitable vulnerabilities. *See: `audit-evidence/penetration-tests/pen-test-report-template.md`*

**Personal Data** — Under GDPR Art. 4(1), any information relating to an identified or identifiable natural person ('data subject').

**Privacy by Design** — The principle (GDPR Art. 25) that data protection measures should be integrated into the design of systems and processes from the outset.

**Processor** — Under GDPR Art. 4(8), a natural or legal person processing personal data on behalf of the controller.

---

## R

**Risk Assessment** — The process of identifying, analysing, and evaluating information security risks. *See: `iso27001/risk-register/risk-register-2026.md`*

**Risk Register** — A documented record of identified risks, their assessment, treatment decisions, and residual risk acceptance. *See: `iso27001/risk-register/risk-register-2026.md`*

**Risk Treatment** — The process of selecting and implementing measures to modify risk, as required by ISO 27001 Clause 6.1.3.

**ROPA (Records of Processing Activities)** — The register of all personal data processing activities maintained under GDPR Art. 30. *See: `gdpr/ropa/ropa-template.md`*

**RPO (Recovery Point Objective)** — The maximum acceptable amount of data loss measured in time.

**RTO (Recovery Time Objective)** — The maximum acceptable time to restore a service after a disruption.

---

## S

**SCCs (Standard Contractual Clauses)** — EU-approved contractual clauses for international data transfers under GDPR Art. 46(2)(c). Required when transferring data to countries without an adequacy decision.

**SIEM (Security Information and Event Management)** — A system that aggregates, correlates, and analyses security event data from multiple sources.

**SLA (Service Level Agreement)** — A commitment between a service provider and customer defining expected service levels, typically measured as uptime percentages.

**SOC 2 (System and Organization Controls 2)** — AICPA's auditing standard for examining controls relevant to security, availability, processing integrity, confidentiality, and privacy. *See: `soc2/` directory*

**SoA (Statement of Applicability)** — A document required by ISO 27001 Clause 6.1.3(d) stating which Annex A controls are applicable and how they are implemented. *See: `iso27001/soa/statement-of-applicability.md`*

**Special Category Data** — Under GDPR Art. 9, personal data revealing racial/ethnic origin, political opinions, religious/philosophical beliefs, trade union membership, genetic data, biometric data, health data, or data concerning sex life/sexual orientation. Processing is prohibited unless an exception under Art. 9(2) applies.

**Supervisory Authority** — An independent public authority established by an EU member state to supervise GDPR compliance. JOL's lead authority is VDAI (Lithuania).

---

## T

**TIA (Transfer Impact Assessment)** — An assessment of the data protection laws and practices of a third country, required by the Schrems II judgment when relying on SCCs for international transfers.

**TSC (Trust Services Criteria)** — The criteria used in SOC 2 examinations: CC1–CC9 (common criteria), plus optional A1 (availability), C1 (confidentiality), PI (processing integrity), and P1 (privacy). *See: `soc2/trust-services-criteria/tsc-control-mapping.md`*

---

## V

**VDAI (Valstybinė duomenų apsaugos inspekcija)** — Lithuanian State Data Protection Inspectorate, the supervisory authority for GDPR in Lithuania.

**Vendor Register** — A documented list of all third-party vendors with access to organisational data, including risk assessment and DPA status. *See: `vendor-register/vendor-register-master.md`*

**Vulnerability Scan** — An automated assessment of systems to identify known security vulnerabilities. *See: `audit-evidence/vulnerability-scans/vulnerability-scan-template.md`*

---

## Document History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | [DATE] | [AUTHOR] | Initial glossary |

---

*This document is the property of Journey Of Life UAB. Classified as INTERNAL. Update this glossary as new compliance terms are introduced. Cross-reference with `COMPLIANCE_MATRIX.md` for framework mappings.*

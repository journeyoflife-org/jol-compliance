# Information Asset Register

**ISO/IEC 27001:2022 — Asset Inventory for Journey Of Life UAB**

| Field | Value |
|-------|-------|
| **Document ID** | JOL-ISMS-AR-2026 |
| **Organisation** | Journey Of Life UAB |
| **ISMS Reference** | A.5.9 (Inventory of information and other associated assets) |
| **Register Owner** | [CISO Name] |
| **Version** | 1.0 |
| **Last Updated** | [YYYY-MM-DD] |
| **Next Review** | [YYYY-MM-DD] |
| **Classification** | Internal — Confidential |

---

## 1. Classification Legend

| Level | Label | Description |
|-------|-------|-------------|
| C1 | Public | Approved for external disclosure |
| C2 | Internal | General internal use |
| C3 | Confidential | Sensitive; need-to-know; encrypted at rest |
| C4 | Restricted | Highly sensitive (Art. 9 data, credentials, keys); field-level encryption; MFA access |

---

## 2. Information Assets

### 2.1 Tenant Data

| Asset ID | Asset Name | Description | Classification | Owner | Location | Retention |
|----------|-----------|-------------|---------------|-------|---------|-----------|
| IA-001 | Tenant User Database | Personal data of institution members | C3 | CTO | Primary DB cluster (EU-West) | Per data retention policy |
| IA-002 | Special Category Data Store | Religious affiliation, health data (Art. 9) | C4 | DPO | Encrypted partition | Per data retention policy |
| IA-003 | Children's Data Store | Data of minors (<16 years) | C4 | DPO | Encrypted partition with enhanced controls | Per data retention policy |
| IA-004 | Tenant Configuration | Institution settings, preferences | C3 | CTO | Application database | Account lifetime + 30 days |
| IA-005 | Communication Records | Messages, notifications within platform | C3 | CTO | Application database | 24 months |
| IA-006 | Financial Transaction Data | Donations, payment records | C3 | CFO | Payment database | Per country retention (7–10 years) |

### 2.2 Platform Infrastructure

| Asset ID | Asset Name | Description | Classification | Owner | Location |
|----------|-----------|-------------|---------------|-------|---------|
| IA-010 | Production Web Servers | Application frontend servers | C3 | Head of Ops | EU-West cloud |
| IA-011 | Production API Servers | Backend API layer | C3 | Head of Ops | EU-West cloud |
| IA-012 | Production Database Cluster | Primary PostgreSQL cluster | C4 | DBA | EU-West cloud |
| IA-013 | Staging Environment | Pre-production testing | C2 | Head of Engineering | EU-West cloud |
| IA-014 | Development Environment | Development and testing | C2 | Head of Engineering | EU-West cloud |
| IA-015 | CI/CD Pipeline | Build and deployment infrastructure | C3 | DevOps | GitHub Actions |
| IA-016 | Container Registry | Docker image storage | C3 | DevOps | [Registry provider] |
| IA-017 | CDN / Load Balancer | Content delivery and traffic routing | C2 | Head of Ops | Global (EU PoPs) |

### 2.3 Security and Monitoring Assets

| Asset ID | Asset Name | Description | Classification | Owner | Location |
|----------|-----------|-------------|---------------|-------|---------|
| IA-020 | SIEM Platform | Security event monitoring and alerting | C3 | CISO | EU cloud |
| IA-021 | Vulnerability Scanner | Automated vulnerability scanning | C3 | Security | EU cloud |
| IA-022 | Key Management Service | Encryption key storage and management | C4 | CISO | EU cloud (dedicated) |
| IA-023 | Audit Log Store | Immutable audit trail | C3 | CISO | EU cloud (append-only) |
| IA-024 | Backup System | Automated backup infrastructure | C4 | Head of Ops | EU-West + EU-Central |

### 2.4 Identity and Access

| Asset ID | Asset Name | Description | Classification | Owner | Location |
|----------|-----------|-------------|---------------|-------|---------|
| IA-030 | Identity Provider (IdP) | SSO and identity management | C3 | CISO | EU cloud |
| IA-031 | User Directory | Employee and contractor identity records | C3 | HR | IdP / HR system |
| IA-032 | MFA Token Database | TOTP secrets and hardware key registrations | C4 | CISO | Encrypted store |
| IA-033 | API Key Management | Service account keys and certificates | C4 | DevOps | Secrets manager |

### 2.5 Business and Compliance Records

| Asset ID | Asset Name | Description | Classification | Owner | Location |
|----------|-----------|-------------|---------------|-------|---------|
| IA-040 | ROPA (Record of Processing) | GDPR Art. 30 register | C3 | DPO | Compliance repo |
| IA-041 | DPIA Reports | Data Protection Impact Assessments | C3 | DPO | Compliance repo |
| IA-042 | Risk Register | ISO 27001 risk assessments | C3 | CISO | Compliance repo |
| IA-043 | Audit Evidence | SOC 2 and ISO audit evidence | C3 | CISO | Audit evidence repo |
| IA-044 | Vendor Register | Supplier register and DPAs | C3 | DPO | Compliance repo |
| IA-045 | Incident Records | Security incident documentation | C3 | CISO | Incident management system |
| IA-046 | Training Records | Security awareness completion records | C2 | HR | LMS |
| IA-047 | Policy Documents | ISMS policies and procedures | C2 | CISO | Compliance repo |

### 2.6 Corporate and Communication

| Asset ID | Asset Name | Description | Classification | Owner | Location |
|----------|-----------|-------------|---------------|-------|---------|
| IA-050 | Email System | Corporate email | C3 | IT | [Provider] |
| IA-051 | Collaboration Platform | Internal communication (Slack/Teams) | C2 | IT | [Provider] |
| IA-052 | Document Management | Shared document repository | C2 | IT | [Provider] |
| IA-053 | Code Repositories | Source code (GitHub) | C3 | Head of Engineering | GitHub |
| IA-054 | Knowledge Base | Internal documentation (Confluence/Notion) | C2 | IT | [Provider] |

---

## 3. Software Assets

| Asset ID | Software Name | Version | Classification | Owner | License Type |
|----------|--------------|---------|---------------|-------|-------------|
| SA-001 | Journey Of Life Platform | [Current] | C3 | CTO | Proprietary |
| SA-002 | PostgreSQL | [Current] | C3 | DBA | Open source |
| SA-003 | Redis | [Current] | C3 | DBA | Open source |
| SA-004 | Nginx | [Current] | C2 | Head of Ops | Open source |
| SA-005 | Docker / Kubernetes | [Current] | C3 | DevOps | Open source |
| SA-006 | GitHub Actions | [Current] | C3 | DevOps | Commercial |
| SA-007 | Monitoring Stack | [Current] | C3 | Head of Ops | [Open source / Commercial] |
| SA-008 | SIEM Solution | [Current] | C3 | CISO | Commercial |
| SA-009 | Endpoint Protection | [Current] | C3 | IT | Commercial |
| SA-010 | Email Security Gateway | [Current] | C3 | IT | Commercial |

---

## 4. Hardware Assets

| Asset ID | Hardware Type | Description | Classification | Owner | Location |
|----------|--------------|-------------|---------------|-------|---------|
| HA-001 | Employee Laptops | Company-issued devices | C3 | IT | Employee locations |
| HA-002 | Hardware Security Keys | YubiKey for MFA | C4 | CISO | Employee possession |
| HA-003 | Office Network Equipment | Routers, switches, APs | C2 | IT | Office premises |
| HA-004 | Mobile Devices | Company phones/tablets | C3 | IT | Employee possession |

---

## 5. Intangible Assets

| Asset ID | Asset Name | Description | Classification | Owner |
|----------|-----------|-------------|---------------|-------|
| INT-001 | Brand Reputation | Trust of religious institution tenants | — | CEO |
| INT-002 | Customer Relationships | Relationships with ~400,000 institutions | — | CCO |
| INT-003 | Intellectual Property | Platform source code and architecture | C3 | CTO |
| INT-004 | Compliance Certifications | ISO 27001, SOC 2 certifications | — | CISO |

---

## 6. Asset Returnable Upon Termination

| Asset Type | Return Procedure | Deadline |
|-----------|----------------|---------|
| Laptop / device | Return to IT on last working day | Day of termination |
| Hardware security key | Return to CISO on last working day | Day of termination |
| Access badges | Return to Security on last working day | Day of termination |
| Company phone | Return to IT within 48 hours | 48 hours post-termination |
| Company credit card | Return to Finance on last working day | Day of termination |

---

## 7. Review Schedule

| Review Type | Frequency | Owner | Method |
|------------|-----------|-------|--------|
| Full inventory review | Annual | CISO | Manual + automated discovery |
| New asset onboarding | Per event | System Owner | Add to register upon deployment |
| Decommissioned asset removal | Per event | System Owner | Update register upon decommission |
| Classification review | Annual | Asset Owner | Review against current classification |
| Service account audit | Quarterly | DevOps | Automated inventory |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [YYYY-MM-DD] | [CISO Name] | Initial asset register |

---

*This Asset Register is maintained in accordance with ISO 27001:2022 Annex A.5.9 and forms part of the ISMS for Journey Of Life UAB. It is reviewed annually and updated whenever assets are added, modified, or decommissioned.*

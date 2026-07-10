# Infrastructure Evidence Collection

**Audit Evidence — Cloud Infrastructure Security Controls**

| Field | Value |
|-------|-------|
| **Document ID** | JOL-AE-INF-001 |
| **Evidence Owner** | [Head of Operations] |
| **Version** | 1.0 |
| **Classification** | Internal — Confidential |

---

## 1. Infrastructure Configuration

| Evidence Item | Description | Collection Method | Frequency |
|--------------|-------------|------------------|-----------|
| AE-INF-001 | Cloud account inventory | Cloud console export | Quarterly |
| AE-INF-002 | Network architecture diagram | Engineering | Annual |
| AE-INF-003 | Firewall rules export | Cloud console | Quarterly |
| AE-INF-004 | Security group / NSG rules | Cloud console | Quarterly |
| AE-INF-005 | VPC / network segmentation configuration | Cloud console | Quarterly |
| AE-INF-006 | Load balancer configuration (TLS settings) | Cloud console | Quarterly |
| AE-INF-007 | DNS configuration | DNS provider | Quarterly |

## 2. Compute and Container Security

| Evidence Item | Description | Collection Method | Frequency |
|--------------|-------------|------------------|-----------|
| AE-INF-010 | Kubernetes cluster configuration | kubectl export | Quarterly |
| AE-INF-011 | Container image scan results | CI/CD pipeline | Per build |
| AE-INF-012 | Pod security policies / admission controllers | Cluster config | Quarterly |
| AE-INF-013 | Server hardening baseline | Configuration files | Annual |
| AE-INF-014 | OS patch level report | System export | Monthly |

## 3. Database Security

| Evidence Item | Description | Collection Method | Frequency |
|--------------|-------------|------------------|-----------|
| AE-INF-020 | Database encryption at rest configuration | DBA export | Quarterly |
| AE-INF-021 | Database access control list | DBA export | Quarterly |
| AE-INF-022 | Database backup configuration | DBA export | Quarterly |
| AE-INF-023 | Database audit log configuration | DBA export | Annual |

## 4. Encryption and Key Management

| Evidence Item | Description | Collection Method | Frequency |
|--------------|-------------|------------------|-----------|
| AE-INF-030 | KMS key inventory | Cloud console | Quarterly |
| AE-INF-031 | Key rotation evidence | KMS export | Annual |
| AE-INF-032 | TLS certificate inventory | Monitoring platform | Quarterly |
| AE-INF-033 | Certificate expiry monitoring | Monitoring platform | Quarterly |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [YYYY-MM-DD] | [Head of Operations] | Initial guide |

---

*Infrastructure evidence supports SOC 2 CC7.1 and ISO 27001 A.8.1–A.8.34 compliance.*

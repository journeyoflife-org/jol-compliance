# C1 Scope Decision — Privacy Policy Coverage for Baltic Pilot & Phase 2 Expansion

**GDPR Article 13–14 — Transparency Obligation: Geographic Scope**

| Field | Value |
|-------|-------|
| **Decision ID** | JOL-SD-C1-001 |
| **Organisation** | Journey Of Life UAB |
| **Decision Owner** | Gintaras Kazlauskas — Platform Owner / DPO |
| **Document Reference** | `gdpr/privacy-policies/` |
| **Version** | 1.0 |
| **Effective Date** | 2026-09-19 |
| **Status** | Approved |
| **Classification** | Internal — Confidential |

---

## 1. Decision Summary

**The Baltic-only privacy policy scope (LT/LV/EE) is correct and sufficient for the Lithuania pilot.** After the 6-month pilot phase, the platform will expand to Poland (PL), Germany (DE), and Italy (IT), requiring 3 additional country-specific privacy policies. Full EU-27 coverage is the long-term industrialization target, not the current operational scope.

---

## 2. Context

### 2.1 Pilot Scope (Ratified 2026-08-24)

The Lithuania pilot targets the Šiauliai Diocese cluster — 23 sites on `*.gyvenimo-kelias.lt` subdomains (Wave 0: 3–5 reference sites, Wave 1: 23 sites, Wave 2: ~100). All pilot data subjects are Lithuanian residents. The supervisory authority is VDAI (Lithuania).

**Source**: `jol-hub/docs/decisions/MASTER-PROMPT-LT-PILOT-FRONTEND.md` §4.

### 2.2 Expansion Timeline (Ratified)

| Phase | Countries | Timeline | Privacy Policy Requirement |
|-------|-----------|----------|---------------------------|
| **Pilot** | Lithuania (LT) | Immediate | JOL-PP-LT-001 (exists) |
| **Pre-positioned** | Latvia (LV), Estonia (EE) | Not yet processing data | JOL-PP-LV-001, JOL-PP-EE-001 (exist, ready) |
| **Phase 2** | Poland (PL), Germany (DE), Italy (IT) | +6 months from pilot | 3 new policies required before go-live |
| **Industrialization** | Remaining 21 EU member states | Post-Phase 2 | 21 additional policies (tracked roadmap) |

### 2.3 Current Coverage

| Country | Privacy Policy | Country Compliance Doc | Status |
|---------|---------------|----------------------|--------|
| Lithuania (LT) | `gdpr/privacy-policies/lt/privacy-policy-lt.md` | `country/lt/lithuania-compliance-requirements.md` | ✅ Complete |
| Latvia (LV) | `gdpr/privacy-policies/lv/privacy-policy-lv.md` | `country/lv/latvia-compliance-requirements.md` | ✅ Complete |
| Estonia (EE) | `gdpr/privacy-policies/ee/privacy-policy-ee.md` | `country/ee/estonia-compliance-requirements.md` | ✅ Complete |
| Poland (PL) | — | — | 🔴 Required before Phase 2 |
| Germany (DE) | — | — | 🔴 Required before Phase 2 |
| Italy (IT) | — | — | 🔴 Required before Phase 2 |
| 21 other EU states | — | — | ⚪ Planned (industrialization phase) |

---

## 3. Decision

### 3.1 What is decided

1. **Baltic-only scope is approved for the pilot.** The 3 existing privacy policies (LT, LV, EE) are sufficient for the current operational phase. No additional policies are required until Phase 2 expansion begins.

2. **Phase 2 (PL/DE/IT) requires 3 additional policies.** Each must be completed, legally reviewed, and approved BEFORE processing begins in the respective country. Target completion: 30 days before Phase 2 go-live.

3. **Full EU-27 coverage is a tracked roadmap item**, not a current gap. The remaining 21 EU member state policies will be produced during the industrialization phase, following the same template and review process.

4. **LV and EE policies are pre-positioned, not yet invoked.** No Latvian or Estonian data subjects exist during the Lithuania-only pilot. These policies are ready for activation when the first LV/EE tenant is onboarded.

### 3.2 Rationale

| Factor | Analysis |
|--------|----------|
| **GDPR Art. 13** | Privacy notices must be provided "at the time when personal data are obtained." No data collection from PL/DE/IT subjects means no current obligation for those policies. |
| **Supervisory authority** | Only VDAI (Lithuania) has jurisdiction during the pilot. PL (UODO), DE (BfDI + Landesbehörden), IT (Garante) become relevant only when processing begins. |
| **Data minimisation** | Preparing 24 additional policies now would create documents referencing unknown processing activities — counter to GDPR Art. 5(1)(b) purpose limitation. |
| **Proportionality** | 3 policies for 3 countries (pilot scope) is proportionate. 27 policies for a hypothetical full-EU rollout is premature when the expansion timeline is phased. |
| **Audit readiness** | An auditor examining the pilot will find 3 complete policies matching the operational scope. The scope decision + expansion roadmap demonstrates planned compliance for future phases. |

---

## 4. Obligations & Deadlines

| Action | Owner | Deadline | Dependency |
|--------|-------|----------|------------|
| Fill all `[*]` placeholders in LT policy (registration number) | DPO | Before pilot go-live | Company registration details |
| Complete PL privacy policy + country compliance doc | DPO + Legal | 30 days before PL go-live | Phase 2 scope confirmation |
| Complete DE privacy policy + country compliance doc | DPO + Legal | 30 days before DE go-live | Phase 2 scope confirmation |
| Complete IT privacy policy + country compliance doc | DPO + Legal | 30 days before IT go-live | Phase 2 scope confirmation |
| Conduct DPIA for Phase 2 expansion | DPO | Before Phase 2 go-live | Country compliance docs complete |
| Update `COMPLIANCE_MATRIX.md` §5 with PL/DE/IT | DPO | When Phase 2 begins | Policies drafted |
| Produce EU-27 remaining policies (21 countries) | DPO | Industrialization phase | Post-Phase 2 |

---

## 5. Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Auditor challenges why only 3 policies exist | Low (pilot is LT-only) | Medium | This scope decision document + expansion roadmap |
| LT policy published with `[*]` placeholders | Medium | **High** (Art. 13 non-compliance) | P0: fill all `[*]` items before pilot launch |
| PL/DE/IT policies not ready at Phase 2 expansion | Medium | High (cannot legally process without notice) | 30-day-before-go-live deadline tracked |
| 21 remaining EU policies treated as a gap | Low | Low | Documented as industrialization roadmap, not a gap |

---

## 6. Review Triggers

This decision must be revisited when:
1. Phase 2 expansion scope changes (additional countries beyond PL/DE/IT).
2. A supervisory authority (VDAI, UODO, BfDI, Garante) issues guidance requiring broader pre-positioning.
3. The industrialization timeline is accelerated.
4. A DPIA finding requires country-specific policy amendments.

---

## 7. Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| DPO / Platform Owner | Gintaras Kazlauskas | 2026-09-19 | _________________ |

---

## Related Documents

| Document | Location |
|----------|----------|
| LT Privacy Policy | `gdpr/privacy-policies/lt/privacy-policy-lt.md` |
| LV Privacy Policy | `gdpr/privacy-policies/lv/privacy-policy-lv.md` |
| EE Privacy Policy | `gdpr/privacy-policies/ee/privacy-policy-ee.md` |
| LT Compliance Requirements | `country/lt/lithuania-compliance-requirements.md` |
| LV Compliance Requirements | `country/lv/latvia-compliance-requirements.md` |
| EE Compliance Requirements | `country/ee/estonia-compliance-requirements.md` |
| Lithuania Pilot Master Prompt | `jol-hub/docs/decisions/MASTER-PROMPT-LT-PILOT-FRONTEND.md` |
| Compliance Matrix | `COMPLIANCE_MATRIX.md` §5 |

---

*This scope decision is made under GDPR Articles 13–14 (transparency obligation) and Article 5(1)(b) (purpose limitation). It records the rationale for limiting privacy policy coverage to the Baltic pilot scope and establishes the expansion plan for Phase 2 countries.*

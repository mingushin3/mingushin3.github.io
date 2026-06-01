# 01_Audit Report v1 — Source Fidelity Audit

**Task type:** PDF 대조 감사, 웹 검색 OFF  
**Inputs:**
- `01_G_1구획 IV PK CL·V·t½(1).pdf` = Gabrielsson & Weiner source excerpt, Ch.2 p.14–32 + Case Study PK1 p.469–475
- `01_T_1구획 IV PK CL·V·t½(1).pdf` = Rowland & Tozer source excerpt, Ch.3 p.53–76
- `01_step1_draft_v0.md` = Step 1 Draft v0
- `S01_phase1_patch memo.md` = audit attention guide only

**Audit mode:** Verification only. No web search. No pedagogical rewriting.  
**Figure inspection:** PDF pages were rendered and visually inspected. T6 inspection method is therefore `VISUAL_INSPECTED` unless otherwise stated.

---

## Executive finding

**판정: CONDITIONAL GO — Source Fidelity patch required before HTML compile.**

Step 1 Draft v0의 중심축인 **`CL`·`V` primary / `K`·`t1/2` secondary / `MRT` bridge**는 원문과 잘 부합한다. Gabrielsson p.17은 `CL`과 `V`를 independent primary parameters로, `K`, `t1/2`, `AUC`를 secondary/derived parameters로 설명하고, R&T p.58도 `half-life`와 `k`가 `CL`과 `V`에 의해 결정된다는 점을 chapter objective와 본문에서 반복한다. Draft의 MUST 카드 5개 구성은 타당하다.

다만 Draft v0에는 **한 개의 명백한 수치/논리 오류**와 여러 개의 **NOT_IN_SOURCE 실무 확장**이 섞여 있다. 가장 중요한 오류는 C1에서 **Subject 1과 Subject 4의 `CL`이 같다고 해석한 부분**이다. 원문 Case Study PK1 Table 1.2는 Subject 1 `CL=0.1 L/min`, Subject 4 `CL=0.2 L/min`이며, 두 피험자는 `K`와 `t1/2`가 유사할 뿐 `CL`은 다르다. 따라서 “동일 주입속도에서 `Css`가 같다”는 결론도 틀리다.

---

## T1: Equation/Numerical Audit

| Item | Draft v0 Expression | PDF Source | Classification | Correction |
|---|---|---|---|---|
| Core hierarchy | `CL` and `V` are primary/independent; `K`, `t1/2`, `AUC` are secondary/derived | G p.17; R&T objectives p.53 and text p.58 | MATCH | None |
| One-compartment IV bolus ODE | `dC/dt = -K·C = -(CL/V)·C` | G Eq.2:1/2:4 p.16–17; R&T Eq.3-9/3-10 p.57–58 | MATCH | None |
| Integrated monoexponential equation | `C = C0·e^(-Kt) = (D/V)·e^{-(CL/V)t}` | G Eq.2:4 p.17; R&T Eq.3-10 p.58 | MATCH | None |
| Semi-log slope | `ln C = ln C0 - K·t`; slope `=-K` | R&T Eq.3-11 p.58; G Fig.2.4/2.6 p.15–17 | MATCH | None |
| `K = CL/V` | `K = CL/V` | G p.17; R&T Eq.3-7 p.56 | MATCH | None |
| `t1/2 = ln2/K = 0.693·V/CL` | as written | G Eq.2:3/2:6 p.17–18; R&T Eq.3-15/3-16 p.58 | MATCH | None |
| `CL` definition | “unit time volume completely cleared”; units `mL/min`, `L/hr` | G p.16; R&T Eq.3-4/3-5 p.56 | MATCH | None |
| `CL = Q·E` | flow × extraction ratio; upper bound `Q` if `E=1` | R&T Eq.3-5 p.56 | MATCH | None |
| `Rate of elimination = CL·C` | as written | R&T Eq.3-4 p.56; G Eq.2:2 p.16 | MATCH | None |
| `CL = Dose/AUC` | `CL = Dose/AUC0-inf` | G Eq.2:12 p.19; R&T Eq.3-22 p.60 | MATCH | None |
| `Css = Rin/CL` | as written | G Eq.2:22 p.23 | MATCH | None |
| “Clearance is the sole parameter determining maintenance dose at steady state” | direct message in Draft | G p.23 | MATCH | None |
| `V = Ab/C` | volume as proportionality factor between body amount and plasma concentration | G Eq.2:14 p.20; R&T Eq.3-26 p.63 | MATCH | None |
| `V = Div/C0` | IV bolus direct volume estimate | G Eq.2:13 p.20; G Fig.2.6 p.17 | MATCH | None |
| `V = CL/K = 1.44·CL·t1/2` | as written | R&T Eq.3-27/3-28 p.63 | MATCH | None |
| `V = Vu·fu` | as written | G Eq.2:15 p.20 | MATCH | None |
| `Kpi = fuB/fuTi` | tissue-to-blood partition relationship | G Eq.2:17 p.21 | MATCH | None |
| `V = VB + VTi·Kpi` approximate form | single-average approximation | G Eq.2:18 p.21 | MATCH | None |
| `Vss = VB + Σ VTi·Kpi·(1-ETi)` | steady-state tissue decomposition with extraction term | G Eq.2:16 p.20 | MATCH | None |
| Quinacrine `V = 40,000 L` | as written | G p.20 | MATCH | None |
| Quinacrine “body보다 600배” | derived approximation | G only gives 40,000 L, not “600×” | RESTORED | Accept only as clearly marked derived calculation; do not present as source quote. |
| Quinacrine “혈장에 0.0017%만 남음” | percentage claim | Not in source; calculation basis unclear and likely not consistent with plasma-volume denominator | ERROR | Remove or mark as unsupported derived inference with calculation shown. |
| Gabrielsson Fig.2.7 numeric example | `D=10,000 µg`, `C0=1000 µg/L`, `V=10 L`, `K≈0.01 min^-1`, `t1/2≈65 min` | G p.18 | MATCH | None |
| Compound A Table values | S1 `K=0.01`, `V=10`, `CL=0.1`, `AUC=98,000`; S2 `0.02`, `9.8`, `0.2`, `49,000`; S3 `0.02`, `10`, `0.2`, `51,000`; S4 `0.01`, `20`, `0.2`, `51,000` | G Tables 1.2/1.3 p.473–474 | MATCH | None |
| C1 Anchor: Subject 1 vs 4 | “`CL`이 같은데 `V`가 다르므로 `K`가 다르고, `t1/2`가 다르다; same `Css`” | G Tables 1.2/1.3 p.473–474 | ERROR | Source: S1 `CL=0.1`, S4 `CL=0.2`; `K` similar (`0.01`), `t1/2` similar (68 vs 71), `Css` at same `Rin` differs because `Css=Rin/CL`. |
| Q5 Subject 1 vs 4 calculation | `Rin=10 µg/min`; S1 `Css=100 µg/L`, S4 `Css=50 µg/L` | G Tables 1.2/1.3 + G Eq.2:22 | MATCH | None. This later section correctly contradicts the earlier C1 anchor. |
| `AUC`, `AUMC`, `MRT=AUMC/AUC` | as written | G Eq.2:10–2:11 p.19 | MATCH | None |
| `MRT=1/K` | 1-cmt IV bolus | R&T Eq.3-25 p.60; derived from G Eq.2:10–2:11 | MATCH | None |
| `MRT = 1.443·t1/2` | 1-cmt IV bolus derived relation | R&T Eq.3-15 and 3-25 | MATCH | Pedagogical derivation; source supports components. |
| Compound A MRT ratios | S1 98/68≈1.44; S2 48/34≈1.41; S3 53/36≈1.47; S4 100/71≈1.41 | G Table 1.3 p.474 | MATCH | None; minor variation is rounding. |
| R&T creatinine/inulin | `CL=4.5 L/hr`; creatinine `V=42 L`, `t1/2=6.5 hr`; inulin `V=16 L`, `t1/2=2.5 hr` | R&T p.58 | MATCH | None |
| R&T midazolam | dose `7.5 mg base`; `AUC=287 µg·hr/L`; `CL=26 L/hr`; `t1/2=3.8 hr`; `V=142 L`; 5-min plasma amount `0.61 mg`; 92% outside plasma | R&T p.61–63 | MATCH | None |
| Midazolam “high-extraction, E≈0.4–0.6” | Draft Q6 | Not stated in provided R&T Ch.3 excerpt | NOT_IN_SOURCE | Tag as external pharmacology or remove from source-bound Step 1. |
| “간경변 midazolam t1/2 증가 mainly CL decrease” | Draft C4/Q6 | Not supported by the provided R&T excerpt; the citation under Fig.3-4 mentions chronic liver disease but this chapter excerpt does not derive that scenario | NOT_IN_SOURCE | Tag as external clinical inference or remove. |
| G Fig.2.8 steady state timing | 1 t1/2=50%, 2=75%, 3=87.5%, 3–4≈90% | G Fig.2.8 p.22 | MATCH | None |
| R&T 6.64 half-lives | 99% lost / 1% remaining | R&T p.59 | MATCH | None |
| R&T Table 3-1 | `k=0.1 hr^-1`; 100 mg → 90, 81, 72.9, 65.6, 59.04 mg; limiting case 60.63% at 5 hr | R&T Table 3-1 p.57 | MATCH | None |
| Gentamicin example | >95% eliminated before distribution equilibrium | R&T Fig.3-7 and text p.66 | MATCH | None |
| `CLR = fe·CL` | as written | R&T Eq.3-34 p.68 | MATCH | None |
| `Renal clearance = Ae∞/AUC` | as written/implicit | R&T Eq.3-32 p.68 | MATCH | None |
| `CL = CLR + CLNR` | Draft context | R&T describes `fe` and complement `1-fe`; not written exactly in excerpt but conceptually supported | RESTORED | Accept as pedagogical simplification; avoid presenting as direct quote. |
| `CL/F` after extravascular dosing | Draft context | G Eq.2:36–2:38 discusses extravascular AUC and bioavailability; text explicitly mentions `V/F` | RESTORED | Keep as context only; source directly anchors `V/F`, while `CL/F` follows from AUC/F relation. |
| `MRTiv = Vss/CL` | Draft C5 limitations / Pair 3 | Not stated in provided page range | NOT_IN_SOURCE | Tag as future-session relation or remove from source-bound card. |
| `MRTpo = MRTiv + MAT` | Draft C5 limitations | Not stated in provided page range | NOT_IN_SOURCE | Tag as future absorption/NCA relation. |
| `MRT/t1/2=1.85 → 2-cmt ADVAN3/TRANS4` | Draft Q8 | Not in source; extrapolates to PopPK workflow | NOT_IN_SOURCE | Keep only as explicitly marked 실무 확장/TRENCH. |
| NONMEM code snippets | `THETA`, `ETA`, `ADVAN1 TRANS1/TRANS2`, `ADVAN3 TRANS4`, GOF/CWRES | Not in PDFs | NOT_IN_SOURCE | Must be tagged as 실무 확장 or removed from source-fidelity content. |
| “Deficiency Letter 30%” | Draft §8C | Draft itself marks `[확인 필요]`; not in PDFs | NOT_IN_SOURCE | Remove from source-bound output unless externally cited later. |
| “patient death”, “FDA IR”, “ICH M14”, “TQT ±0.10” | strong regulatory/clinical claims | Not in PDFs | NOT_IN_SOURCE | Do not present as source-derived. Tag, remove, or move to external commentary layer. |
| “신부전 + 부종 V 30–50% 증가” | numeric clinical claim | Not in PDFs | NOT_IN_SOURCE | Remove or tag as external clinical inference requiring citation. |
| “신생아 체수분 1.5배; gentamicin adult mg/kg → underexposure” | numeric pediatric claim | Not in PDFs | NOT_IN_SOURCE | Remove or tag as external clinical inference requiring citation. |
| RC circuit / gas-law analogies | analogy layer | Not in PDFs | OPTIONAL | Accept if analogy layer is explicitly non-source pedagogy. |

---

## T2: Examples & Data Audit

| Item | Draft v0 Status | PDF Location | Classification | Importance | Action |
|---|---|---|---|---|---|
| G Fig.2.3 activated-charcoal bucket example | Included in V concept | G p.14–15 | INCLUDED_CORRECT | HIGH | Keep; this is the cleanest V intuition source. |
| G Fig.2.7 one-compartment 10 mg example | Included in V/K calculations | G p.18 | INCLUDED_CORRECT | HIGH | Keep. |
| G Case Study PK1 Compound A, 4 volunteers, 10 mg IV bolus | Included as source anchor | G p.469–475 | INCLUDED_ERROR | HIGH | Numeric table is correct, but Subject 1 vs 4 interpretation in C1 anchor is wrong. |
| G Table 1.1 raw concentration-time data | Not included | G p.471 | MISSING | MEDIUM | Optional table-level enrichment; not required in card text if Table 1.2/1.3 are used. |
| G Table 1.2 parameter estimates | Included | G p.473 | INCLUDED_CORRECT | HIGH | Keep. |
| G Table 1.3 secondary parameters | Included | G p.474 | INCLUDED_CORRECT | HIGH | Keep. |
| G Case Study design issue: reduce observations; `1/K` and `1/Ka` optimal sampling time points | Largely absent | G p.475 | MISSING | LOW | Omission acceptable; belongs to experimental design/session planning rather than core CL/V/t1/2. |
| G constant infusion example | Partly included via `Css` and 3–4 half-lives | G p.22–28 | INCLUDED_CORRECT | HIGH | Keep as context; do not let it expand into a full infusion session. |
| G Eq.2:31 infusion-to-bolus back extrapolation | Context bullet only | G p.24–25 | INCLUDED_CORRECT | LOW | Context treatment is enough. |
| G Table 2.1 tissue partition coefficients | Context only | G p.21 | INCLUDED_CORRECT | MEDIUM | Context treatment is enough; full tissue table is out of current scope. |
| G extravascular route rat example | Rejected/omitted | G p.29–30 | MISSING | LOW | Omission justified; absorption session material. |
| G flip-flop example | Rejected/omitted | G p.29–30 | MISSING | LOW | Omission justified; absorption session material. |
| G lag-time/residual method | Rejected/omitted | G p.31–32 | MISSING | LOW | Omission justified; absorption session material. |
| R&T Figs.3-1/3-2 simulated Drugs A–D | Concept reflected, figures not directly used | R&T p.54–55 | MISSING | MEDIUM | SHOULD_FIX: brief inclusion would improve author-message fidelity because these figures motivate CL vs V differences. |
| R&T Fig.3-3 reservoir-extractor model | Included in CL card | R&T p.55–56 | INCLUDED_CORRECT | HIGH | Keep. |
| R&T Table 3-1 k=0.1 hr^-1 reservoir example | Included in K card | R&T p.57 | INCLUDED_CORRECT | MEDIUM | Keep. |
| R&T creatinine/inulin example | Included in t1/2 card | R&T p.58 | INCLUDED_CORRECT | HIGH | Keep; strong source anchor for `t1/2` depends on both `CL` and `V`. |
| R&T midazolam case | Included in C4/Q7 | R&T p.61–64 | INCLUDED_CORRECT | HIGH | Keep; avoid adding unsupported liver-cirrhosis/high-extraction claims. |
| R&T Fig.3-5 midazolam area/elimination by 2 hr | Partly reflected | R&T p.64 | INCLUDED_CORRECT | MEDIUM | Could retain as context; not mandatory. |
| R&T Fig.3-6 distribution vs elimination competing processes | Partly reflected via distribution/terminal phase | R&T p.65 | MISSING | MEDIUM | SHOULD_FIX: add as source anchor for “terminal phase usually elimination, but exceptions exist.” |
| R&T gentamicin Fig.3-7 | Included in C4 limitation | R&T p.66 | INCLUDED_CORRECT | HIGH | Keep; one of the most important exceptions. |
| R&T renal clearance pathway discussion | Context only | R&T p.66–68 | INCLUDED_CORRECT | MEDIUM | Context treatment acceptable for current session; ensure not omitted if chapter objective is retained. |
| R&T Table 3-2 plasma/urine worked dataset | Mostly omitted | R&T p.69 | MISSING | MEDIUM | Omission acceptable if renal clearance stays context; problematic only if `fe/CLR` becomes a card. |
| R&T Fig.3-8/3-9 plasma/urine plots | Omitted | R&T p.70–71 | MISSING | LOW | Omission justified under current scope. |
| R&T precision/computer-use comments | Omitted | R&T p.71–72 | MISSING | LOW | Optional. |
| R&T study problems: valproic acid, diazepam, cocaine, theophylline | Omitted | R&T p.73–76 | MISSING | LOW | Omission justified; study-problem bank, not core source narrative. |
| Draft neonate/gentamicin dosing claim | Included in V card | No source in PDFs | NOT_IN_SOURCE | HIGH | Remove or tag as external clinical inference requiring citation. |
| Draft PopPK/NONMEM/Deficiency Letter/Boss Dilemma examples | Included | No source in PDFs | NOT_IN_SOURCE | HIGH | Move to clearly marked 실무 확장 layer, or remove from source-bound Step 1. |

---

## T3: Author Key Messages

| Message | PDF Location | In Draft v0? | Status |
|---|---|---|---|
| IV bolus captures pure disposition; disposition = distribution + elimination | G p.14; R&T p.53–54 | Yes, partially | MATCH |
| One-compartment model approximates the organism as a single volume; concentration declines monoexponentially | G Fig.2.2–2.4 p.14–15; R&T Eq.3-10 p.58 | Yes | MATCH |
| Semi-log plots linearize monoexponential decline; slope is `-K` | G Fig.2.4/2.6 p.15–17; R&T Eq.3-11 p.58 | Yes | MATCH |
| `CL` is an imaginary/apparent flow-volume term relating elimination rate to concentration | G p.16; R&T p.56 | Yes | MATCH |
| `CL = Q·E`; even perfect extraction cannot exceed flow `Q` | R&T p.56 | Yes | MATCH |
| `CL` and `V` are independent primary determinants; `K` and `t1/2` depend on them, not vice versa | G p.17; R&T p.58 | Yes | MATCH |
| `V` is apparent, not anatomical volume; tissue binding can make `V` extremely large | G p.14–21; R&T p.63–64 | Yes | MATCH |
| `AUC` is governed by `CL`; peak/intercept `C0` is governed by `V` | G Fig.2.6/2.12 p.17, 26–27; R&T p.59–60 | Yes | MATCH |
| Steady-state concentration during infusion is determined by `CL`; time to steady state depends on half-life | G p.22–28 | Yes | MATCH |
| `3–4 t1/2` gives about 90% steady state | G Fig.2.8 p.22 | Yes | MATCH |
| Distribution phase can make early plasma decline non-elimination; terminal phase usually represents elimination but has exceptions | R&T p.61–66 | Yes, but compressed | SHOULD_FIX: anchor more explicitly to Fig.3-6/Fig.3-7. |
| For gentamicin, terminal phase is not the major elimination phase; >95% eliminated before distribution equilibrium | R&T p.66 | Yes | MATCH |
| Renal excretion fraction `fe` quantifies contribution of renal route; `CLR = fe·CL` | R&T p.66–68 | Yes, context | MATCH |
| Data should be plotted graphically even when computers fit models; visual inspection teaches model suitability | R&T p.71–72 | Mostly absent | OPTIONAL |
| Linear PK assumes parameters do not vary with dose/time; nonlinearities are separate later topic | R&T p.72 | Partly in assumptions | MATCH |

---

## T4: Priority Summary (sorted: MUST_FIX → SHOULD_FIX → OPTIONAL → REJECT)

| # | Item | Priority | Rationale |
|---|---|---|---|
| 1 | C1 Subject 1 vs 4 interpretation says same `CL`, different `K/t1/2`, same `Css` | MUST_FIX | Directly contradicts G Tables 1.2/1.3 and Eq.2:22. This is the single clearest source error. |
| 2 | “환자를 죽일 수 있는 추론” phrasing | MUST_FIX | Unsupported severity claim; source says `t1/2` depends on `CL` and `V`, not that this specific clinical outcome follows. |
| 3 | “신부전 + 부종 → V 30–50% 증가” | MUST_FIX | Numeric clinical claim not in PDFs. |
| 4 | “Volume Drift pattern”, CWRES/IPRED diagnostic claims | MUST_FIX | Useful but not source-derived; must be tagged as 실무 추론/TRENCH or removed. |
| 5 | High/low extraction examples with propranolol/warfarin/phenytoin | MUST_FIX | `CL=Q·E` is in source; high/low extraction worked examples are not in this excerpt. Scope creep. |
| 6 | C2 neonate/gentamicin body-water and underdosing claim | MUST_FIX | Not in PDFs; do not present as source-derived. |
| 7 | Quinacrine percentage/body-size quantification | MUST_FIX | 40,000 L is source; exact “600×” and “0.0017%” are not source and percentage appears unsupported. |
| 8 | Q6 midazolam high-extraction/liver-cirrhosis scenario | MUST_FIX | Not in source excerpt; only healthy-adult midazolam PK is worked out here. |
| 9 | Q8 PopPK model decision from `MRT/t1/2=1.85` | MUST_FIX | Not source-derived. May stay only if explicitly marked as practical extension. |
| 10 | Q9 Boss Dilemma with OFV/COV/FDA/ICH claims | MUST_FIX | Entire scenario is invented from source motifs; keep only in a clearly separated 실무 확장 module. |
| 11 | “FDA Deficiency Letter 약 30%” | MUST_FIX | Draft already marks 확인 필요; no PDF support. Remove until sourced. |
| 12 | R&T Fig.3-1/Fig.3-2 A–D examples not explicitly reflected | SHOULD_FIX | These are author’s opening pedagogical devices for separating initial concentration/V and slope/CL. |
| 13 | R&T Fig.3-6 competing distribution/elimination not explicitly anchored | SHOULD_FIX | This is the key bridge to why terminal phase usually but not always represents elimination. |
| 14 | R&T computer/precision message absent | OPTIONAL | Useful metacognitive note but not essential to CL/V/t1/2 card set. |
| 15 | G Case Study design advice about reducing samples and `1/K`/`1/Ka` sampling | OPTIONAL | Useful for experimental design, but out of narrow Step 1 concept anatomy. |
| 16 | Full extravascular absorption equations/cards | REJECT | Scope creep; Draft correctly rejects full Ka/F/tlag/residual-method treatment for this session. |
| 17 | Full tissue partition table as a standalone card | REJECT | Too much for this session; context treatment is enough. |
| 18 | Full renal clearance card | REJECT for this session | R&T covers it, but current session lock is CL·V·K·t1/2 with renal clearance only as context. |

---

## T5: Coverage Audit

| PDF Element | Type | PDF Location | Step 1 Status | Omission Verdict | Required Action |
|---|---|---|---|---|---|
| G §2.2 One-Compartment Models | Heading | G p.14 | INCLUDED_AS_MUST | None | None |
| G §2.2.1 Intravenous bolus administration | Heading | G p.14 | INCLUDED_AS_MUST | None | None |
| G Eq.2:1–2:4: first-order decline and integrated IV bolus equation | Equations | G p.16–17 | INCLUDED_AS_MUST | None | None |
| G Eq.2:5–2:7: slope, half-life, volume example | Equations | G p.18 | INCLUDED_AS_MUST | None | None |
| G Eq.2:8–2:13: AUC, AUMC, MRT, CL, V | Equations | G p.19–20 | INCLUDED_AS_MUST/CONTEXT | None | Keep AUMC derivation compressed. |
| G Eq.2:14–2:18: `V`, `Vu`, `fu`, `Vss`, `Kpi`, approximate V | Equations | G p.20–21 | INCLUDED_AS_CONTEXT | None | Current context treatment acceptable. |
| G Table 2.1 tissue partition coefficients | Table | G p.21 | INCLUDED_AS_CONTEXT | OMITTED_JUSTIFIABLE | Do not expand into full card. |
| G §2.2.2 Constant rate infusion | Heading | G p.22–25 | INCLUDED_AS_CONTEXT | None | Keep `Css` and time-to-SS only. |
| G Eq.2:19–2:26: infusion ODE, `Css`, post-infusion, residual slope | Equations | G p.22–23 | INCLUDED_AS_CONTEXT | OMITTED_JUSTIFIABLE | Only `Css` is MUST; residual slope is optional. |
| G Eq.2:27–2:31: infusion-to-bolus back extrapolation | Equations | G p.24–25 | INCLUDED_AS_CONTEXT | OMITTED_JUSTIFIABLE | Context line enough. |
| G §2.2.3 Integration of clearance and volume | Heading | G p.25–28 | INCLUDED_AS_MUST | None | Keep as core organizing logic. |
| G Fig.2.11–2.14 CL/V effects on bolus/infusion/multiple dosing | Figures | G p.26–28 | INCLUDED_AS_CONTEXT | None | Figure 2.12 is especially useful if HTML later visualizes CL/V changes. |
| G §2.2.4 Extravascular administration | Heading | G p.28–32 | OMITTED_JUSTIFIABLE | None | Keep rejected/context only. |
| G Eq.2:32–2:39 absorption/F/tlag | Equations | G p.30–32 | OMITTED_JUSTIFIABLE | None | Do not promote to MUST. |
| G §2.2.5 Estimation of absorption parameters | Heading | G p.32 | OMITTED_JUSTIFIABLE | None | Separate absorption session. |
| G Eq.2:40 residual method slope | Equation | G p.32 | OMITTED_JUSTIFIABLE | None | Separate absorption session. |
| G Case Study PK1 title/objectives/keywords/problem specification | Case study | G p.469 | INCLUDED_AS_CONTEXT | None | Enough. |
| G Case Study Table 1.1 concentration-time data | Dataset | G p.471 | OMITTED_JUSTIFIABLE | MISSING_EXAMPLE, LOW | Optional raw-data appendix only. |
| G Case Study Fig.1.1/1.2 male/female semilog data | Figures | G p.470 | INCLUDED_AS_CONTEXT | None | Could be used in Phase 4C. |
| G Case Study Eq.1:1–1:8 | Equations | G p.472–473 | INCLUDED_AS_CONTEXT | None | Enough; no need to duplicate all. |
| G Table 1.2 parameter estimates | Table | G p.473 | INCLUDED_AS_MUST | None | Fix Subject 1/4 interpretation. |
| G Table 1.3 secondary parameters | Table | G p.474 | INCLUDED_AS_MUST | None | None |
| G Case Study design issues and Fig.1.4 | Example/figure | G p.474–475 | INCLUDED_AS_CONTEXT | OMITTED_JUSTIFIABLE | Optional; not core. |
| T chapter objectives | Summary/objectives | R&T p.53 | INCLUDED_AS_MUST/CONTEXT | None | Key objectives mostly covered. |
| T Appreciation of Kinetic Concepts | Heading | R&T p.54 | INCLUDED_AS_CONTEXT | MISSING_EXAMPLE, MEDIUM | SHOULD_FIX: make A–D opening examples visible. |
| T Figs.3-1/3-2 | Figures | R&T p.54–55 | OMITTED_PROBLEMATIC | MISSING_EXAMPLE | Add short source anchor or view instruction later. |
| T Volume of Distribution and Clearance | Heading | R&T p.55–56 | INCLUDED_AS_MUST | None | None |
| T Eq.3-1–3-5 | Equations | R&T p.55–56 | INCLUDED_AS_MUST | None | None |
| T First-order Elimination | Heading | R&T p.56–58 | INCLUDED_AS_MUST | None | None |
| T Eq.3-6–3-11 | Equations | R&T p.56–58 | INCLUDED_AS_MUST | None | None |
| T Table 3-1 | Table | R&T p.57 | INCLUDED_AS_MUST | None | None |
| T Half-life | Heading | R&T p.58 | INCLUDED_AS_MUST | None | None |
| T Eq.3-12–3-16 | Equations | R&T p.58 | INCLUDED_AS_MUST | None | None |
| T creatinine/inulin example | Worked example | R&T p.58 | INCLUDED_AS_MUST | None | None |
| T Fraction of Dose Remaining | Heading/equations | R&T p.59 | INCLUDED_AS_MUST | None | None |
| T Eq.3-17–3-19 | Equations | R&T p.59 | INCLUDED_AS_MUST | None | None |
| T Clearance, Area, and Volume of Distribution | Heading/equations | R&T p.59–60 | INCLUDED_AS_MUST | None | None |
| T Eq.3-20–3-23 | Equations | R&T p.59–60 | INCLUDED_AS_MUST | None | None |
| T Mean Residence Time | Heading/equations | R&T p.60 | INCLUDED_AS_MUST | None | None |
| T Eq.3-24–3-25 | Equations | R&T p.60 | INCLUDED_AS_MUST | None | None |
| T A Case Study: midazolam | Heading/case | R&T p.61–64 | INCLUDED_AS_MUST | None | Remove unsupported liver/high-extraction add-ons. |
| T Fig.3-4/3-5 | Figures | R&T p.61, 64 | INCLUDED_AS_CONTEXT | None | Good candidate for learner view instruction. |
| T Distribution Phase / Terminal Phase / Elimination Half-life | Headings | R&T p.62 | INCLUDED_AS_CONTEXT | None | None |
| T Clearance / Volume of Distribution in midazolam | Headings/calculations | R&T p.63 | INCLUDED_AS_MUST | None | None |
| T Distribution and Elimination: Competing Processes | Heading/figure | R&T p.64–66 | INCLUDED_AS_CONTEXT | MISSING_BRIDGE | SHOULD_FIX: anchor to Fig.3-6. |
| T Fig.3-6 competing scenarios | Figure | R&T p.65 | OMITTED_PROBLEMATIC | MISSING_BRIDGE | Add as bridge source or view instruction. |
| T Fig.3-7 gentamicin exception | Figure | R&T p.66 | INCLUDED_AS_CONTEXT | None | None |
| T Pathways of Elimination | Heading | R&T p.66 | INCLUDED_AS_CONTEXT | None | None |
| T Renal Clearance | Heading/equations | R&T p.67–68 | INCLUDED_AS_CONTEXT | OMITTED_JUSTIFIABLE | Context enough. |
| T Eq.3-29–3-34 | Equations | R&T p.67–68 | INCLUDED_AS_CONTEXT | OMITTED_JUSTIFIABLE | Context enough. |
| T Estimation of Pharmacokinetic Parameters / Table 3-2 / Fig.3-8/3-9 | Worked example/table/figures | R&T p.68–71 | OMITTED_JUSTIFIABLE | None | Omit unless renal clearance becomes a card. |
| T A Question of Precision | Author message | R&T p.71 | OMITTED_JUSTIFIABLE | MISSING_AUTHOR_MSG, LOW | Optional. |
| T Measurement Fluid | Author terminology note | R&T p.71 | OMITTED_JUSTIFIABLE | LOW | Optional; can be footnote. |
| T Use of Computers | Author message | R&T p.71–72 | OMITTED_JUSTIFIABLE | MISSING_AUTHOR_MSG, LOW | Optional. |
| T Change in Dose | Author message | R&T p.72 | INCLUDED_AS_CONTEXT | None | Linear PK assumptions covered. |
| T Key Relationships | Box summary | R&T p.72–73 | INCLUDED_AS_MUST/CONTEXT | None | Core equations reflected. |
| T Study Problems 1–10 | Study problems/tables/figures | R&T p.73–76 | OMITTED_JUSTIFIABLE | None | Omission justified. |

---

## T6: Figure Inventory & Learning Value Audit

| Figure/Table | Page | Teaches | Value | View Instruction? | Redraw/New Schematic? | Inspection Method | Rationale |
|---|---:|---|---|---|---|---|---|
| G Fig.2.2 | 14 | One-compartment model and monoexponential decline in linear vs semilog view | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Core mental model for 1-cmt IV bolus. |
| G Fig.2.3 | 15 | Apparent volume via equal buckets and charcoal binding | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Best visual for “V is apparent, not physical.” |
| G Fig.2.4 | 15 | Linear vs semilog decline and half-life/slope | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Directly links `t1/2` and `K`. |
| G Fig.2.5 | 16 | Elimination rate vs concentration; slope = `CL` | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Makes `CL` as proportionality factor visible. |
| G Fig.2.6 | 17 | `V=Div/C0`, `CL=Div/AUC`, `t1/2=ln2/K` on semilog curve | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Compact source map for core parameters. |
| G Fig.2.7 | 18 | Worked one-cmt 10 mg bolus example | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Source anchor for initial estimates. |
| G Table 2.1 | 21 | Tissue-to-blood partition coefficients and `Vss` examples | USEFUL | NO | YES | VISUAL_INSPECTED | Useful for V depth, but too detailed for core session. |
| G Fig.2.8 | 22 | Constant infusion and 3–4 half-lives to ~90% steady state | USEFUL | YES | YES | VISUAL_INSPECTED | Supports `Css` and time-to-SS context. |
| G Fig.2.9 | 24 | Estimating `K` from infusion residual slope | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Too narrow for this session. |
| G Fig.2.10 | 25 | Infusion back-extrapolation to bolus intercept | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Context only. |
| G Fig.2.11 | 26 | Effect of increased `CL` vs increased `V` on bolus curve | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Highly relevant to CL/V separation. |
| G Fig.2.12 | 26–27 | Equal/different CL and V effects on bolus and infusion | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Best visual for primary-parameter independence. |
| G Fig.2.13 | 27 | CL/V effects after repeated IV bolus dosing at steady state | USEFUL | NO | YES | VISUAL_INSPECTED | Useful but moves toward multiple dosing. |
| G Fig.2.14 | 28 | Infusion rate vs clearance changes at steady state | USEFUL | YES | YES | VISUAL_INSPECTED | Good for distinguishing dose-rate vs CL. |
| G Fig.2.15 | 29 | One-compartment gut absorption model | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Absorption session material. |
| G Fig.2.16 | 29 | IV/SC/IP route comparison in rats | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Out of core session. |
| G Fig.2.17 | 30 | Extravascular terminal slope vs flip-flop | USEFUL | NO | YES | VISUAL_INSPECTED | Important later; only context here. |
| G Fig.2.18 | 31 | Lag-time and residual slope | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Absorption parameter session. |
| G Fig.2.19 | 32 | Residual method for absorption rate | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Absorption parameter session. |
| G Fig.1.1 | 470 | Male subjects Compound A: same intercept, different AUC/CL | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Directly demonstrates CL difference with similar V. |
| G Fig.1.2 | 470 | Female subjects Compound A: Subject 4 higher V/lower intercept | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Directly anchors V interpretation. |
| G Table 1.1 | 471 | Raw concentration-time data for four subjects | USEFUL | NO | NO | VISUAL_INSPECTED | Useful for exercise, not needed in card. |
| G Fig.1.3 | 471 | Estimating `V`, `t1/2`, `CL` from semilog plot | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Duplicates Fig.2.6 but source-case specific. |
| G Table 1.2 | 473 | Primary parameter estimates for `K`, `CL`, `V` | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Needed to prevent Subject 1/4 error. |
| G Table 1.3 | 474 | Secondary parameters `AUC`, `AUMC`, `t1/2`, `MRT` | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Needed for MRT/t1/2 ratio anchor. |
| G Fig.1.4 | 475 | Acute dosing vs constant infusion for Subjects 1/2 | USEFUL | YES | YES | VISUAL_INSPECTED | Good for `CL` → `Css`, but not essential if Eq.2:22 retained. |
| R&T Fig.3-1 | 54 | Same initial concentration, different slopes/AUC | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Opening author device for separating CL effect. |
| R&T Fig.3-2 | 55 | Same half-life, different initial concentrations/AUC | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Opening author device for separating V and CL. |
| R&T Fig.3-3 | 55 | Reservoir-extractor model: `Q`, `E`, `CL` | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Structural basis of clearance. |
| R&T Table 3-1 | 57 | Fractional elimination with `k=0.1 hr^-1` | USEFUL | YES | NO | VISUAL_INSPECTED | Strong K intuition but text is sufficient. |
| R&T Fig.3-4 | 61 | Midazolam biphasic profile and distribution phase | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Critical for terminal-phase interpretation. |
| R&T Fig.3-5 | 64 | Midazolam AUC split and fraction eliminated by 2 hr | USEFUL | YES | NO | VISUAL_INSPECTED | Useful for AUC-as-eliminated-amount logic. |
| R&T Fig.3-6 | 65 | Distribution vs elimination as competing processes | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Missing bridge in Draft; should be explicitly anchored. |
| R&T Fig.3-7 | 66 | Gentamicin exception: most elimination before terminal phase | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Prevents overgeneralizing terminal slope. |
| R&T Table 3-2 | 69 | Plasma and urine data for PK parameter estimation | USEFUL | NO | NO | VISUAL_INSPECTED | Useful if renal clearance is expanded. |
| R&T Fig.3-8 | 70 | Regular/semilog plot for Table 3-2 | USEFUL | NO | NO | VISUAL_INSPECTED | Supports distribution-phase diagnosis. |
| R&T Fig.3-9 | 71 | Renal clearance from amount excreted vs AUC interval | USEFUL | NO | NO | VISUAL_INSPECTED | Renal clearance context. |
| R&T Fig.3-10 | 74 | Study problem: concentration and urinary excretion two-point graphs | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Problem exercise only. |
| R&T Table 3-3 | 75 | Cocaine IV plasma concentrations | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Problem exercise only. |
| R&T Fig.3-11 | 75 | Theophylline biexponential profile | USEFUL | NO | NO | VISUAL_INSPECTED | Useful extension, but study-problem level. |

---

## Patch Memo independent classification

| Memo item | Classification | Audit decision |
|---|---|---|
| Big Idea phrase “환자를 죽일 수 있는 추론” too strong | MATCH | Source does not support that severity; must soften or tag as practical inference. |
| “신부전 + 부종 V 30–50%” source check | MATCH | NOT_IN_SOURCE confirmed. |
| High/low extraction scope creep | MATCH | `CL=Q·E` is source, but high/low examples are not in provided excerpt. |
| GOF/NONMEM diagnostic outside source | MATCH | NOT_IN_SOURCE confirmed. |
| MRT multicompartment extension requires boundary tag | MATCH | `MRT=1/K` is source for 1-cmt; ADVAN/model-diagnostic extension is not source. |
| “Phase 1 v0 good but not HTML-ready” | MATCH | Audit supports conditional go with mandatory source-fidelity patch. |

---

## Final audit verdict

**Go condition:** Step 1 Draft v0 can proceed to Phase 4A/HTML only after source-fidelity patching.  
**Do not fully rewrite.** The core architecture is right. The required action is targeted cleanup:

1. Fix the **Subject 1 vs Subject 4** interpretation error.
2. Mark or remove all **NOT_IN_SOURCE clinical/regulatory/NONMEM claims**.
3. Add/restore a small source anchor for **R&T Fig.3-1/Fig.3-2** and **R&T Fig.3-6**, because these are author-designed conceptual bridges.
4. Keep `Ka/F/tlag`, detailed tissue partition, renal clearance, and absorption residual method as context/rejected items, not MUST cards.


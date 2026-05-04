# 15_Audit Report v1 — Source Fidelity Audit

**업무 형태:** 파일 분석 / PDF 대조 감사 / 웹 검색 OFF  
**입력:** `015_G_모델 구축의 기술 초기값·GOF·실험설계(1).pdf` + `15_step1_draft_v0(1).md` + `S15_phase1_patch memo.md`  
**감사 역할:** Source Fidelity Auditor  
**감사 원칙:** 문장 개선·교육적 보강·재작성 금지. PDF에 근거가 있는지와 Draft v0의 출처 충실도만 판정.  
**시각 자료 검증:** PDF 전 페이지를 PNG 렌더링하여 figure/table을 육안 확인함.  

---

## Executive Verdict

**최종 판정: CONDITIONAL PASS / HTML 직행 금지 / Phase 4 전 MUST_FIX 필요**

Draft v0는 Session 15의 중심 골격인 **초기값 → GOF/잔차 → F-test/AIC → 정밀도·상관 → 편미분 설계 → 민감도·toxicokinetic design**을 상당히 잘 포착했다. 특히 Fig.4.16 modeling carousel, Eq.4:16–4:20 초기값 계산, Fig.4.53 `r` 오용, Table 4.8 F-test/AIC 제한, Fig.5.4–5.6 편미분 설계, Fig.5.20 toxicokinetic 혼동은 핵심 소스와 잘 대응한다.

다만 Draft v0에는 다음 문제가 남아 있다.

1. **PDF 외부 규제·실무 표현 혼입:** `NDA/IND Deficiency Letter`, `Major Deficiency`, `6-month review extension`, `NDA Module 5`, `FDA Guidance`, `10M USD`, `시장 가치 수천만 USD` 등은 첨부 PDF 직접 근거가 없다.
2. **현대 PopPK 구현 번역 혼입:** `NONMEM`, `CWRES`, `NPDE`, `Pirana/Xpose`, `SCM`, `ΔOFV > 3.84`, `Bayesian TDM`, `Fisher information matrix`, `D-optimal`, `ED-optimal`, `PFIM`, `PopED`, `Sobol`, `mrgsolve` 등은 대부분 원문 직접 내용이 아니다.
3. **Source range 표기 정밀도 부족:** Ch.5 범위는 실제 PDF에서 p.399–405와 p.412–414로 분리되어 있으며, p.406–411은 업로드에 없다. Draft의 `p.399–414` 연속 표기는 부정확하다.
4. **동적 non-steady-state 초기값 예시 누락:** Eq.4:23–4:33 및 Table 4.3의 두 모델 비교 예시는 Draft에서 거의 빠져 있다. 치명적 누락은 아니지만 A-Critical 모드에서는 SHOULD_FIX이다.
5. **Patch Memo 중 Eq.4:53 및 Eq.4:22 수정 요구는 Source Fidelity 관점에서는 자동 채택하면 안 된다.** 렌더링 PDF 원문 자체가 Draft와 같은 형태를 제시한다. 수학적 관점의 후속 주석은 가능하지만, Source Fidelity ERROR는 아니다.

---

## T1: Equation/Numerical Audit

| Item | Draft v0 Expression | PDF Source | Classification | Correction |
|---|---|---|---|---|
| Source page range, Ch.4 | `p.352-364 / p.368-392` and pp.365-367 missing | PDF contains p.352-364, skips to p.368, then p.368-392 | MATCH | No correction. |
| Source page range, Ch.5 | `p.399-414` | PDF contains p.399-405 and p.412-414; p.406-411 absent | ERROR | Change source range to `p.399-405 / p.412-414`; note p.406-411 not uploaded/out of scope. |
| Modeling carousel | Fig.4.16 six steps: Tentative model → Design → Run experiment → Explore data → Fit model → Analyze output | p.352 Fig.4.16 | MATCH | None. |
| Poor initial estimates | wrong final values, local minima, physiologically impossible values | p.353 text | MATCH | None. |
| `10 mg IV bolus` | Fig.4.17 two subjects after identical 10 mg IV bolus | p.353 Fig.4.17 | MATCH | None. |
| Eq.4:16 | `slope = [ln(800)-ln(400)]/(23-87) = -0.01 min^-1` | p.354 Eq.4:16 | MATCH | None. |
| Eq.4:17 | `t1/2 = ln2/K = 0.693/0.01 ≈ 65 min` | p.354 Eq.4:17 | MATCH | None. |
| Eq.4:18 | `AUC = C0/K = 100,000 µg·L^-1·min` | p.354 Eq.4:18 | MATCH | None. |
| Eq.4:19 | `Cl = 0.1 L·min^-1` | p.354 Eq.4:19 | MATCH | None. |
| Eq.4:20 | `V = 10 L` | p.354 Eq.4:20 | MATCH | None. |
| Eq.4:21 | `C = A·e^-αt + B·e^-βt` | p.354 Eq.4:21 | MATCH | None. |
| Fig.4.18 values | `A=1.0 µg·L^-1`, `B=0.8 µg·L^-1`, `alpha=0.05 min^-1`, `beta=0.003 min^-1` | p.355 Fig.4.18 | MATCH | None. |
| Dynamic equilibrium IC50/Emax graphical estimate | semi-log plot expands below IC50 and aids IC50 estimate | p.355 Fig.4.19, p.356 text | RESTORED | Draft does not give this as a full item; optional context restore if Phase 4 allows. |
| Eq.4:22 warfarin-PCA slope | `slope = [ln(124)-ln(56.77)]/(24-0) = -0.03 h^-1` | p.356 Eq.4:22 | MATCH* | *PDF itself has an internal algebra/sign inconsistency: the displayed fraction is positive by arithmetic, but PDF labels it as `-0.03 h^-1`. This is not a Draft-vs-PDF mismatch. If corrected later, label as `[source-internal arithmetic note]`. |
| Fig.4.21 baseline/kout/kin | baseline `120 sec`, `kout≈0.03 h^-1`, `kin=3.6 sec·h^-1` | p.357 text/Fig.4.21 | MATCH | None. |
| Eq.4:23–4:33 | indirect response models, baseline/steady-state/Emax/n derivations | pp.358-359 | RESTORED | Draft largely omits this worked example. Consider context restoration; not a source error in included text. |
| Table 4.3 | Model 1/Model 4 final estimates, initial estimates, WRSS/AIC `7.3/83` vs `12/102` | p.360 Table 4.3 | RESTORED | Draft mentions Table 4.3 only in Phase 2 handoff, not core content. Consider restoring as model-choice example. |
| Eq.4:34 oral PK input | `Ka=1.1 h^-1`, `K=0.128 h^-1`, `V/F=5.0 L·kg^-1` | pp.361-363 | MATCH | None. |
| Eq.4:36 turnover model | `dR/dt = kin·I(C) - kout·R` | p.361 Eq.4:36 | MATCH | None. |
| Eq.4:41 | `kout≈0.06 h^-1` from repeated-dose anxiolytic example | p.362 Eq.4:41 | MATCH | None. |
| Eq.4:42 | `kin = kout·R0 = 4.8 units` | p.362 Eq.4:42 | MATCH | None. |
| Anxiolytic IC50 | `IC50≈0.25 µg·L^-1` | p.362-363 text/Fig.4.25 | MATCH | None. |
| Predicted adequate dose range | `15-25 mg/day` probably adequate; non-toxic at that range | p.363 | RESTORED | Draft omits this conclusion. Optional; may be too case-specific. |
| Eq.4:43 | bi-exponential model under boundary scaling section | p.364 Eq.4:43 | RESTORED | Draft refers to boundary scaling but does not foreground Eq.4:43; optional. |
| Eq.4:44 | `(IE-LB)/(UB-LB)` scales to `0-1` range | p.364 Eq.4:44 | MATCH | None. |
| Table 4.4 | `A=100 LB=10 UB=1000`; `alpha=0.01 LB=0.001 UB=0.1`; `B=1 LB=0.1 UB=10`; `beta=0.05 LB=0.0005 UB=0.05` | p.364 Table 4.4 | MATCH | None. |
| `0.1·IE to 10·IE` relative range | Draft states general recommendation | p.364 text | MATCH | Table 4.4 beta upper boundary is source-specific and does not follow 10·IE; no Draft correction if table copied. |
| Eq.4:46 | `ε = N(0, σ²)` | p.369 Eq.4:46 | MATCH | None. |
| Residual definition | `residual_i = Cobs,i - Ĉcalc,i` | p.369 Fig.4.41 | MATCH | None. |
| Eq.4:47 | `WRSS = Σ Wi(Ci - Ĉi)^2` | p.371 Eq.4:47 | MATCH | None. |
| Eq.4:48 | `σ = sqrt(WRSS/(Nobs-Npar))` | p.371 Eq.4:48 | MATCH | None. |
| Eq.4:49 | `Weight = C_i^-λz` or `Ĉ_i^-λz` | p.373 Eq.4:49 | MATCH | None. |
| Weighting exponent table | Draft labels `λz values: 0, -1, -2, -n` | p.374 text says weighting to power `0, -1, -2, -n`; Eq.4:49 writes exponent as `-λz` | ERROR | Avoid calling these `λz values` unless sign convention is clarified. Use `weighting power/exponent = 0, -1, -2, -n`. |
| Residual pattern examples | banana/U-shape, fan, lag-time bulge, systematic runs | pp.372-376 Fig.4.43-4.50 | MATCH (pedagogical simplification) | Source shows patterns visually; Draft terms are pedagogical labels. |
| Eq.4:50 | mono-exponential model for in vitro microsome lack-of-fit example | p.377 Eq.4:50 | RESTORED | Draft uses downstream F_LOF values but not Eq.4:50. Optional. |
| Table 4.5 | compound X microsome data, 27 observations | p.377 Table 4.5 | RESTORED | Draft summarizes but does not enumerate table. Acceptable. |
| Table 4.6 | pure error: total df `21`, SS `23.61` | p.378 Table 4.6 | MATCH | None. |
| Table 4.7 | residual SS `92.67`, pure error `23.61`, LOF `69.06`, FLOF `15.35`, Fcrit `2.76` | p.378 Table 4.7 | MATCH | None. |
| Eq.4:51 / F_LOF | `[(92.67-23.61)/(25-21)]/(23.61/21)=15.35` | p.379 Eq.4:51 + p.378 Table 4.7 | MATCH | None. |
| Accuracy/precision definitions | bias=accuracy, CV%=precision implied | pp.379-380 Fig.4.52 and text | MATCH | None. |
| Eq.4:52 | `CV% = SE(p̂)/p̂·100` | p.380 Eq.4:52 | MATCH | None. |
| `CV% >50%` as threshold | Draft implies 50% as decision threshold | p.380 uses `K=0.01±0.005 h^-1, CV=50%` only as example | NOT_IN_SOURCE | Do not present 50% as a PDF-defined threshold. Label as heuristic if retained. |
| Eq.4:53 | Draft `r = 1 - ...` | p.381 Eq.4:53 visually shows `r = 1 - ...` without square-root denominator | MATCH | Do not replace with conventional Pearson formula in Source Fidelity phase. If later corrected mathematically, label as external/statistical correction, not source restoration. |
| Fig.4.53 r values | OLS `r=0.96`; IRLS `r=0.94`; OLS underestimates last three observations | p.382 Fig.4.53 and text | MATCH | None. |
| Parameter correlation matrix | correlation >0.9; high correlations suggest fewer parameters or more data | pp.382-383 Fig.4.54 | MATCH | None. |
| `correlation >0.95` threshold | Draft uses 0.95 as action threshold | Source discusses high correlation, examples near 0.9/ellipsoids; no universal 0.95 cutoff | NOT_IN_SOURCE | Label as heuristic or remove. |
| Fig.4.55–4.57 design A/B | confidence ellipsoids and design influence on Cl/V correlation | pp.383-385 | MATCH | None. |
| WRSS vs `-2·Log Likelihood` | asymptotic convergence to same values; compare with criteria on `-2LL` and WRSS | p.386 §4.7.8 | MATCH | None. |
| NONMEM OFV / ΔOFV / chi-square `3.84` | Draft implementation extension | PDF p.386 mentions `-2LL`, not NONMEM, OFV threshold, FOCE, SCM | NOT_IN_SOURCE | Label `[교과서 외 구현 번역]` or remove. |
| Eq.4:54 | F statistic | p.387 Eq.4:54 | MATCH | None. |
| Eq.4:55 | `df = Nobs - Npar` | p.387 Eq.4:55 | MATCH | None. |
| F-test nested condition | hierarchical/nested; reduced model from full model by fixing parameter | p.387-388 | MATCH | None. |
| Equal weighting condition | F-test requires nested models and equal weighting | p.388 | MATCH | None. |
| Ordinary Emax vs sigmoid Emax | nested; `n=1` reduces sigmoid to ordinary Emax | p.388 | MATCH | None. |
| Ordinary Emax vs linear response | not nested unless `C << EC50`; F-test inappropriate | p.388 | MATCH | None. |
| Hepatic distributed vs parallel tube | full/reduced; F-test could be used | p.388-389 | MATCH | None. |
| Eq.4:56, Eq.4:57 | AIC and SC definitions | p.389 | MATCH if present; RESTORED if only discussed | Draft discusses AIC/SC but does not consistently display exact formulas. Optional restoration. |
| AIC/SC same weighting condition | AIC/SC require equal weighting; no nested requirement | p.389 text/Table 4.8 | MATCH | None. |
| Table 4.8 | MM weighted vs first-order unweighted; cannot use F-test because unnested, cannot use AIC because different weights | p.389 Table 4.8 | MATCH | None. |
| Deficiency Letter / Major Deficiency / 6-month extension | Draft repeatedly states regulatory consequence | No such statement in PDF | NOT_IN_SOURCE | MUST_FIX: delete or explicitly label `[교과서 외 실무 추론]`; remove fabricated reviewer quote. |
| Figure 4.59 outlier A/B | A reduces precision; B has leverage and biases parameter estimates with high precision | p.390 | MATCH | None. |
| Table 4.9 checklist | 5 questions and problem/symptom/solution table | p.391 | MATCH | None. |
| “battery of statistical tools” | residuals/precision/accuracy/correlation superior to F/AIC/SC alone | p.391 | MATCH | None. |
| Eq.5:7 | bi-exponential model | p.399 Eq.5:7 | MATCH | None. |
| Eq.5:8 | partial derivatives wrt A/B | p.399 Eq.5:8 | MATCH | None. |
| Eq.5:9 | derivatives wrt alpha/beta | p.399 Eq.5:9 | MATCH | Draft signs match source conceptually; check notation if recompiling. |
| Eq.5:10 | second derivative set to zero | p.399 Eq.5:10 | MATCH | None. |
| Eq.5:11 | `t=1/alpha`, `t=1/beta` | p.400 Eq.5:11 | MATCH | None. |
| `alpha=0.69 h^-1`, `beta=0.069 h^-1`, sampling `1.4` and `14 h` | p.400 | MATCH | None. |
| Fig.5.4 caption values | alpha/beta information near ~20 and ~300 min in plotted example | p.400 Fig.5.4 | MATCH | None. |
| Eq.5:12 sigmoid Imax model | p.400 Eq.5:12 | MATCH | None. |
| Eq.5:13, Eq.5:14 | partial derivatives wrt Imax and IC50 | pp.400-401 | MATCH | None. |
| IC50 `140 µg·L^-1` | partial derivative wrt IC50 peaks at actual IC50 | p.401 | MATCH | None. |
| `20%` and `80%` effect levels | max information about sigmoidicity factor n | p.401 | MATCH | None. |
| Fig.5.6 five design points | E0, n, EC50, n, Emax | p.402 Fig.5.6 | MATCH | None. |
| Fisher information, D-optimal, PFIM, PopED | Draft theoretical/implementation extension | Not in uploaded PDF pages | NOT_IN_SOURCE | Label `[교과서 외 구현 번역]`; do not present as PDF content. |
| Eq.5:15 | turnover response model | p.402 Eq.5:15 | MATCH | None. |
| Eq.5:16 | inhibition function I(C) using mono-exponential PK | p.403 Eq.5:16 | MATCH | None. |
| Fig.5.8 | `kout` maximal sensitivity at 25 and ~100 h | p.403-404 | MATCH | None. |
| Fig.5.9 | Vmax/Km/Vc/Vt +100%/-50% sensitivity | p.405 | MATCH | None. |
| Fig.5.10 | IC50, kin, kout, tlag sensitivity; +100%/-50% | p.405 | MATCH | None. |
| Sobol/global sensitivity | Draft mentions Sobol total-order index | Not in PDF | NOT_IN_SOURCE | Remove or label as external extension. |
| Toxicokinetic `Cmax only` minimalistic package | Table 5.6; chronic studies normally Cmax QC except exceptions | p.413 | MATCH | None. |
| `AUC0-infinity` not true under nonlinear elimination unless sampling continues to first-order/negligible | p.414 text/Fig.5.19 | MATCH | None. |
| Fig.5.20 capacity + induction can obscure AUC Day 1 vs AUCss interpretation | p.414 Fig.5.20 | MATCH | None. |
| `full profile only PK/DRF` | Table 5.6 shows PK and DRF = Profile; chronic uses Cmax/profile pattern | p.413 Table 5.6 | MATCH | None. |
| `all modeling failures 80%` | Draft claim | No source | NOT_IN_SOURCE | MUST_FIX: delete or relabel as unsupported rhetorical claim. |
| `10M USD`, `수천만 USD`, market delay cost | Draft claim | No source | NOT_IN_SOURCE | MUST_FIX: delete or relabel as external business speculation. |

---

## T2: Examples & Data Audit

| Item | Draft v0 Status | PDF Location | Classification | Importance | Action |
|---|---|---|---|---|---|
| Modeling carousel | Included | p.352 Fig.4.16 | INCLUDED_CORRECT | HIGH | Keep. |
| IV bolus two-subject kinetic example | Included with equations and values | pp.353-354 Fig.4.17, Eq.4:16-4:20 | INCLUDED_CORRECT | HIGH | Keep. |
| Bi-exponential curve stripping example | Included with A/B/alpha/beta | pp.354-355 Fig.4.18, Eq.4:21 | INCLUDED_CORRECT | HIGH | Keep. |
| Dynamic equilibrium antagonistic concentration-response example | Mostly absent | pp.355-356 Fig.4.19 | MISSING | MEDIUM | Restore as 1-2 sentence context for graphical IC50/Emax initial estimates. |
| Warfarin-PCA turnover initial estimate | Included | pp.356-357 Fig.4.20-4.21, Eq.4:22 | INCLUDED_CORRECT | HIGH | Keep; note source-internal sign issue if desired. |
| Two-infusion new compound indirect response example | Mostly absent | pp.357-360 Fig.4.22-4.23, Eq.4:23-4:33, Table 4.3 | MISSING | MEDIUM | Restore minimally; it demonstrates initial estimates leading to model selection. |
| Dynamic repeated-dose anxiolytic example | Included as context | pp.360-363 Fig.4.24-4.25, Eq.4:34-4:42 | INCLUDED_CORRECT | MEDIUM | Keep. |
| Boundary scaling example | Included | p.364 Eq.4:44, Table 4.4 | INCLUDED_CORRECT | MEDIUM | Keep. |
| Residual definition and residual plotting | Included | pp.369-371 Fig.4.41-4.42, Eq.4:46-4:48 | INCLUDED_CORRECT | HIGH | Keep. |
| Residual pattern comparison ordinary vs sigmoid Emax | Included partially | pp.372-374 Fig.4.43-4.46 | INCLUDED_CORRECT | HIGH | Keep; terms are pedagogical simplifications. |
| Bi- vs tri-exponential residual comparison | Included partially | pp.374-376 Fig.4.47-4.49 | INCLUDED_CORRECT | MEDIUM | Keep as context. |
| Common residual plot schematic | Included | p.376 Fig.4.50 | INCLUDED_CORRECT | HIGH | Keep. |
| Pure error vs lack-of-fit microsome compound X | Included with F_LOF | pp.377-378 Table 4.5-4.7, Fig.4.51 | INCLUDED_CORRECT | HIGH | Keep. |
| Accuracy vs precision dartboard | Included context | pp.379-380 Fig.4.52 | INCLUDED_CORRECT | MEDIUM | Keep. |
| Correlation coefficient misuse | Included | pp.381-382 Fig.4.53 | INCLUDED_CORRECT | HIGH | Keep. |
| Parameter correlation matrix/ellipse/design examples | Included | pp.382-385 Fig.4.54-4.57 | INCLUDED_CORRECT | HIGH | Keep. |
| Parameter perturbation figure | Included lightly | p.386 Fig.4.58 | INCLUDED_CORRECT | LOW | Optional. |
| Model discrimination examples | Included | pp.387-389 Emax vs sigmoid, Emax vs linear, hepatic models, Table 4.8 | INCLUDED_CORRECT | HIGH | Keep. |
| Outlier A/B | Included | p.390 Fig.4.59 | INCLUDED_CORRECT | HIGH | Keep. |
| GOF checklist | Included | p.391 Table 4.9 | INCLUDED_CORRECT | HIGH | Keep. |
| Partial derivative bi-exponential design | Included | pp.399-400 Fig.5.4, Eq.5:7-5:11 | INCLUDED_CORRECT | HIGH | Keep. |
| Sigmoid Imax design points | Included | pp.400-402 Fig.5.5-5.6, Eq.5:12-5:14 | INCLUDED_CORRECT | HIGH | Keep. |
| Turnover model partial derivative design | Included | pp.402-403 Fig.5.7-5.8, Eq.5:15-5:16 | INCLUDED_CORRECT | HIGH | Keep. |
| Sensitivity analysis PK18 and PD4 | Included | pp.404-405 Fig.5.9-5.10 | INCLUDED_CORRECT | HIGH | Keep. |
| Nortriptyline induction design | Mostly absent except high-level statement | p.412 Fig.5.17 | MISSING | LOW | Optional; context only. |
| Exposure metrics and minimalistic toxicokinetic package | Included | p.413 Fig.5.18, Table 5.6 | INCLUDED_CORRECT | MEDIUM | Keep. |
| Incorrect half-life/AUC extrapolation under nonlinear elimination | Included | p.414 Fig.5.19 | INCLUDED_CORRECT | HIGH | Keep. |
| Simultaneous capacity/time-dependent kinetics | Included | p.414 Fig.5.20 | INCLUDED_CORRECT | HIGH | Keep. |
| NDA/IND/Deficiency scenario | Included but unsupported | No PDF location | NOT_IN_SOURCE | HIGH | Remove or label external. |
| NONMEM/FOCE/CWRES/NPDE/SCM/Bayesian/PFIM/PopED/Sobol/mrgsolve examples | Included but unsupported | No PDF location except broad `-2LL` p.386 | NOT_IN_SOURCE | MEDIUM | Label external implementation bridge. |

---

## T3: Author Key Messages

| Message | PDF Location | In Draft v0? | Status |
|---|---|---|---|
| Initial estimates deserve time investment; poor estimates can converge to wrong values/local minima. | p.353 | Yes | PRESENT_CORRECT |
| There is no golden rule for initial estimates; use available information. | p.353 | Yes, partially | PRESENT_PARTIAL |
| Build a knowledge base around the compound early and define regression objectives; modeling can be endless without a goal. | p.353 | Weakly present | SHOULD_FIX: author message underemphasized. |
| Graphical methods, linear regression, and NCA assist initial parameter estimates. | p.353 | Yes | PRESENT_CORRECT |
| Visual inspection of observed/predicted curves is necessary but can mislead; residual plots are strongly recommended. | pp.368-370 | Yes | PRESENT_CORRECT |
| Residuals should be randomly scattered; non-random residuals imply model or weighting problem. | pp.369-370, p.391 | Yes | PRESENT_CORRECT |
| Goodness-of-fit should not be judged by one statistic; use a battery of tools. | pp.389, 391 | Yes | PRESENT_CORRECT |
| F-test only applies to hierarchical/nested models, and equal weighting is required. | pp.387-388 | Yes | PRESENT_CORRECT |
| AIC/SC do not require nested models but require equal weighting; smallest AIC may still be inadequate. | p.389 | Yes | PRESENT_CORRECT |
| Correlation coefficient `r` is one of the most misused GOF criteria; high `r` does not imply good fit. | pp.381-382 | Yes | PRESENT_CORRECT |
| Parameter precision and correlation depend strongly on sampling design. | pp.380-385 | Yes | PRESENT_CORRECT |
| The importance of graphical presentation of outliers cannot be overemphasized. | p.390 | Yes | PRESENT_CORRECT |
| Extract the most out of available data and use that information to design the next experiment. | p.392 | Yes, partially | PRESENT_PARTIAL |
| Partial derivatives show times/regions of maximal parameter sensitivity and guide future sampling. | pp.399-403 | Yes | PRESENT_CORRECT |
| Robust design is needed because true parameters and between-subject variability are uncertain. | p.402 | Yes, partially | PRESENT_PARTIAL |
| Sensitivity plots help identify regions where additional samples increase parameter precision. | pp.404-405 | Yes | PRESENT_CORRECT |
| In ordinary toxicokinetic studies, detailed kinetic assessment is often less important than establishing exposure. | p.413 | Yes | PRESENT_CORRECT |
| Nonlinear elimination prevents true extrapolated AUC to infinity unless sampling continues until first-order/negligible concentrations. | p.414 | Yes | PRESENT_CORRECT |
| Simultaneous capacity and time dependence can obscure Day 1 vs steady-state AUC comparison. | p.414 | Yes | PRESENT_CORRECT |
| Regulatory Deficiency Letter / review extension consequences. | Not in PDF | Yes | MUST_FIX: absent from source. |

---

## T4: Priority Summary (sorted: MUST_FIX → SHOULD_FIX → OPTIONAL → REJECT)

| # | Item | Priority | Rationale |
|---|---|---|---|
| 1 | Deficiency Letter / Major Deficiency / 6-month review extension / NDA Module 5/FDA reviewer quotation | MUST_FIX | PDF supports statistical validity rules, not regulatory letters, review delays, or fabricated reviewer language. |
| 2 | `all modeling failures 80%` | MUST_FIX | No source. Numeric claim must be deleted or relabeled unsupported. |
| 3 | Business cost claims: `10M USD`, `수천만 USD`, market delay | MUST_FIX | No source in textbook PDF. |
| 4 | NONMEM/CWRES/NPDE/SCM/Bayesian/Fisher/D-optimal/PFIM/PopED/Sobol/mrgsolve claims treated as source content | MUST_FIX | Mostly external implementation translation. Keep only if explicitly tagged `[교과서 외 구현 번역]`. |
| 5 | Ch.5 page range `p.399-414` | MUST_FIX | Actual uploaded pages are p.399-405 and p.412-414; p.406-411 are absent. |
| 6 | Weighting exponent sign convention | MUST_FIX | Draft table says `λz=-1/-2`; source text describes weighting powers 0, -1, -2 while Eq.4:49 writes exponent as `-λz`. Needs sign convention clarity. |
| 7 | `CV% >50%` and `correlation >0.95` as hard thresholds | SHOULD_FIX | PDF gives examples and qualitative warning, not universal thresholds. |
| 8 | Eq.4:23-4:33 and Table 4.3 omission | SHOULD_FIX | This is a worked example connecting initial estimates, model choice, WRSS/AIC. Omission reduces learning completeness. |
| 9 | Dynamic equilibrium Fig.4.19 omission | SHOULD_FIX | Author explicitly uses it to show IC50/Emax graphical estimates. One-line context enough. |
| 10 | Author message “define regression objective; modeling can be endless” underemphasized | SHOULD_FIX | Important author warning on p.353. |
| 11 | Toxicokinetic p412 Fig.5.17 nortriptyline design underrepresented | OPTIONAL | Useful but not central to the six-card structure. |
| 12 | Eq.4:43 exact boundary model | OPTIONAL | Draft covers boundary scaling; exact Eq.4:43 restoration is optional. |
| 13 | Patch Memo: change Eq.4:53 to conventional Pearson formula | REJECT | Source PDF visually shows Draft-like `r = 1 - ...`; do not alter during Source Fidelity audit. If later mathematically corrected, label external correction. |
| 14 | Patch Memo: classify Eq.4:22 slope sign as Draft ERROR | REJECT/OPTIONAL NOTE | Draft matches PDF. The PDF itself is algebraically inconsistent. Add optional source-internal note; do not mark Draft source mismatch. |
| 15 | Patch Memo: flag regulatory extensions | MATCH | Memo correctly identifies these as non-source-supported. |
| 16 | Patch Memo: label NONMEM/CWRES/NPDE/SCM/Bayesian/Fisher/Sobol as external | MATCH | Memo correctly identifies scope/source boundary issue. |
| 17 | Patch Memo: monitor pp.365-367 missing section | MATCH | Draft handles pp.365-367, but also needs p406-411 range precision. |

---

## T5: Coverage Audit

### T5-A. Section Headings

| PDF Element | Type | PDF Location | Step 1 Status | Omission Verdict | Required Action |
|---|---|---|---|---|---|
| §4.4 Obtaining Initial Estimates | H2 | p.352 | INCLUDED_AS_MUST | - | Keep. |
| §4.4.1 Graphical methods and linear regression | H3 | p.353 | INCLUDED_AS_MUST | - | Keep. |
| §4.4.1.1 Kinetic data | H4 | p.353-355 | INCLUDED_AS_MUST | - | Keep. |
| §4.4.1.2 Dynamic equilibrium data | H4 | p.355-356 | OMITTED_PROBLEMATIC | MISSING_BRIDGE | Restore 1-2 sentence context. |
| §4.4.1.3 Dynamic non-steady state data | H4 | p.356-360 | INCLUDED_AS_MUST | Partial omission of Eq.4:23-4:33/Table 4.3 | Restore example summary. |
| §4.4.1.4 Dynamic repeated dose data | H4 | p.360-363 | INCLUDED_AS_CONTEXT | - | Keep. |
| §4.4.2 When all else fails | H3 | p.363-364 | INCLUDED_AS_CONTEXT | - | Keep. |
| §4.7 Assessing the Goodness-of-Fit | H2 | p.368 | INCLUDED_AS_MUST | - | Keep. |
| §4.7.1 Analyzing the residuals | H3 | p.369-371 | INCLUDED_AS_MUST | - | Keep. |
| §4.7.2 Graphical presentation of residuals | H3 | p.371-376 | INCLUDED_AS_MUST | - | Keep. |
| §4.7.3 Pure error versus lack of fit | H3 | p.377-379 | INCLUDED_AS_CONTEXT | - | Keep. |
| §4.7.4 Parameter estimates - Accuracy | H3 | p.379-380 | INCLUDED_AS_CONTEXT | - | Keep. |
| §4.7.5 Parameter estimates - Precision | H3 | p.380-381 | INCLUDED_AS_MUST | - | Keep. |
| §4.7.6 Correlation between observed and predicted values | H3 | p.381-382 | INCLUDED_AS_CONTEXT/CONFUSION | - | Keep. |
| §4.7.7 Correlation between parameters | H3 | p.382-385 | INCLUDED_AS_MUST | - | Keep. |
| §4.7.8 WRSS versus -2·Log Likelihood | H3 | p.386 | INCLUDED_AS_CONTEXT | - | Keep but avoid NONMEM overextension. |
| §4.8 Discrimination Between Rival Models | H2 | p.386 | INCLUDED_AS_MUST | - | Keep. |
| §4.8.1 F test | H3 | p.387-389 | INCLUDED_AS_MUST | - | Keep. |
| §4.8.1.1 Background | H4 | p.387 | INCLUDED_AS_MUST | - | Keep. |
| §4.8.1.2 Ordinary Emax vs sigmoid Emax | H4 | p.388 | INCLUDED_AS_CONTEXT | - | Keep. |
| §4.8.1.3 Ordinary Emax vs linear response | H4 | p.388 | INCLUDED_AS_MUST | - | Keep. |
| §4.8.1.4 Hepatic distributed vs parallel tube model | H4 | p.388-389 | INCLUDED_AS_CONTEXT | - | Keep. |
| §4.8.2 Akaike and Schwarz criteria | H3 | p.389 | INCLUDED_AS_MUST | - | Keep. |
| §4.9 Outliers | H2 | p.390 | INCLUDED_AS_CONTEXT/CONFUSION | - | Keep. |
| §4.10 Checklist for Assessing Goodness-of-Fit | H2 | p.391-392 | INCLUDED_AS_CONTEXT | - | Keep. |
| §5.2.3 Partial derivatives | H3 | p.399-403 | INCLUDED_AS_MUST | - | Keep. |
| §5.2.4 Sensitivity analysis | H3 | p.404-405 | INCLUDED_AS_MUST | - | Keep. |
| §5.3.3 Design of toxicokinetic studies | H3 | p.412-414 | INCLUDED_AS_CONTEXT | - | Keep. |
| pp.365-367 §4.5-4.6 | Missing in upload | Not uploaded | OMITTED_JUSTIFIABLE | - | Keep `[확인 필요]` flags. |
| pp.406-411 | Missing in upload | Not uploaded | OMITTED_JUSTIFIABLE | - | Add missing-range note in header if using `p.399-414`. |

### T5-B. Numbered Equations / Formula Elements

| PDF Element | Type | PDF Location | Step 1 Status | Omission Verdict | Required Action |
|---|---|---|---|---|---|
| Eq.4:13-4:15 | Equations from preceding section | p.352 | OMITTED_JUSTIFIABLE | Out of session scope | None. |
| Eq.4:16-4:21 | Initial kinetic estimates and bi-exponential model | p.354 | INCLUDED_AS_MUST | - | Keep. |
| Eq.4:22 | Warfarin-PCA `kout` slope | p.356 | INCLUDED_AS_MUST | - | Keep; optional source-internal note. |
| Eq.4:23-4:33 | Non-steady-state indirect response derivation | pp.358-359 | OMITTED_PROBLEMATIC | MISSING_EXAMPLE | Restore compressed context. |
| Eq.4:34-4:42 | Repeated-dose anxiolytic PK/PD initial estimates | pp.361-362 | INCLUDED_AS_CONTEXT | - | Keep. |
| Eq.4:43-4:44 | Boundary scaling | p.364 | INCLUDED_AS_CONTEXT | - | Keep. |
| Eq.4:46-4:49 | Residual assumptions, WRSS, sigma, weighting | pp.369-373 | INCLUDED_AS_MUST | - | Keep; clarify weighting exponent sign. |
| Eq.4:50-4:51 | Pure error/LOF model and F_LOF | pp.377-379 | INCLUDED_AS_CONTEXT | - | Keep. |
| Eq.4:52 | CV% | p.380 | INCLUDED_AS_MUST | - | Keep. |
| Eq.4:53 | Correlation coefficient | p.381 | INCLUDED_AS_CONTEXT/CONFUSION | - | Keep source form; do not apply patch memo correction in this phase. |
| Eq.4:54-4:55 | F-test and df | p.387 | INCLUDED_AS_MUST | - | Keep. |
| Eq.4:56-4:57 | AIC/SC | p.389 | INCLUDED_AS_CONTEXT | MISSING_BRIDGE | Consider restoring exact formulas if A-Critical. |
| Eq.5:7-5:11 | Partial derivative design for bi-exponential model | pp.399-400 | INCLUDED_AS_MUST | - | Keep. |
| Eq.5:12-5:14 | Sigmoid Imax partial derivatives | pp.400-401 | INCLUDED_AS_MUST | - | Keep. |
| Eq.5:15-5:16 | Turnover partial derivative model | pp.402-403 | INCLUDED_AS_MUST | - | Keep. |

### T5-C. Repeated Author Messages

| PDF Element | Type | PDF Location | Step 1 Status | Omission Verdict | Required Action |
|---|---|---|---|---|---|
| Visual inspection is essential but must be paired with residual/diagnostic plots. | Repeated message | pp.368-370, 391 | INCLUDED_AS_MUST | - | Keep. |
| Random residual scatter is a core adequacy criterion. | Repeated message | pp.369-370, 391 | INCLUDED_AS_MUST | - | Keep. |
| Use a battery of tools, not one statistic. | Repeated message | pp.389, 391 | INCLUDED_AS_MUST | - | Keep. |
| Initial estimates and design are part of a repeated modeling cycle. | Repeated message | pp.352, 392 | INCLUDED_AS_MUST | - | Keep. |
| Poor estimates/poor design can make parameter estimates practically useless. | Repeated message | pp.353, 380-385, 391 | INCLUDED_AS_MUST | - | Keep. |
| Nonlinear/toxicokinetic interpretation can be confounded by capacity and time dependence. | Repeated message | pp.412-414 | INCLUDED_AS_CONTEXT | - | Keep. |

### T5-D. Worked Examples, Case Studies, and Experimental Datasets

| PDF Element | Type | PDF Location | Step 1 Status | Omission Verdict | Required Action |
|---|---|---|---|---|---|
| Two-subject 10 mg IV bolus kinetic example | Worked example | pp.353-354 | INCLUDED_AS_MUST | - | Keep. |
| Bi-exponential curve-stripping example | Worked example | pp.354-355 | INCLUDED_AS_MUST | - | Keep. |
| Antagonistic concentration-response IC50 example | Worked example | pp.355-356 | OMITTED_PROBLEMATIC | MISSING_BRIDGE | Restore short context. |
| Warfarin-PCA initial `kout/kin` example | Worked example | pp.356-357 | INCLUDED_AS_MUST | - | Keep. |
| Two-infusion indirect response model comparison | Worked example | pp.357-360 | OMITTED_PROBLEMATIC | MISSING_EXAMPLE | Restore compressed example. |
| Four-day anxiolytic repeated-dose PK/PD example | Worked example | pp.360-363 | INCLUDED_AS_CONTEXT | - | Keep. |
| Boundary scaling Table 4.4 | Worked example | p.364 | INCLUDED_AS_CONTEXT | - | Keep. |
| Residual diagnostics examples | Worked examples | pp.369-376 | INCLUDED_AS_MUST | - | Keep. |
| In vitro microsome compound X LOF example | Dataset | pp.377-379 | INCLUDED_AS_CONTEXT | - | Keep. |
| Outlier A/B example | Worked example | p.390 | INCLUDED_AS_CONTEXT | - | Keep. |
| Partial derivative design examples | Worked examples | pp.399-403 | INCLUDED_AS_MUST | - | Keep. |
| Sensitivity analysis PK18/PD4 | Worked examples | pp.404-405 | INCLUDED_AS_MUST | - | Keep. |
| Toxicokinetic minimal package | Design example | pp.412-414 | INCLUDED_AS_CONTEXT | - | Keep. |

### T5-E. Chapter Summary / Box / Closing Messages

| PDF Element | Type | PDF Location | Step 1 Status | Omission Verdict | Required Action |
|---|---|---|---|---|---|
| Ch.4 closing message: extract maximum from available data and use it for next experiment | Closing message | p.392 | INCLUDED_AS_CONTEXT | MISSING_AUTHOR_MSG if underemphasized | Strengthen citation/placement if Phase 4. |
| Table 4.9 common problems/symptoms/solutions | Checklist/box summary | p.391 | INCLUDED_AS_CONTEXT | - | Keep. |
| Ch.5 toxicokinetic concluding warning on nonlinear AUC extrapolation and simultaneous capacity/time dependence | Closing concept | p.414 | INCLUDED_AS_CONTEXT | - | Keep. |

---

## T6: Figure Inventory & Learning Value Audit

| Figure/Table | Page | Teaches | Value | View Instruction? | Redraw/New Schematic? | Inspection Method | Rationale |
|---|---:|---|---|---|---|---|---|
| Fig.4.16 | 352 | Modeling carousel and EDA position. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | This is the organizing spine of the session. |
| Fig.4.17 | 353 | Semi-log IV bolus data for initial K, Cl, V estimates. | USEFUL | YES | NO | VISUAL_INSPECTED | Text equations carry the concept, figure anchors it. |
| Fig.4.18 | 355 | Bi-exponential curve stripping and intercept/slope separation. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Structural understanding of curve stripping depends on the visual separation. |
| Fig.4.19 | 355 | IC50 estimation from lin-lin vs semi-log response-concentration plots. | USEFUL | YES | NO | VISUAL_INSPECTED | Useful bridge to dynamic equilibrium initial estimates. |
| Fig.4.20 | 356 | Turnover model and semi-log downswing slope as `-kout`. | USEFUL | YES | NO | VISUAL_INSPECTED | Visualizes why slope gives kout. |
| Fig.4.21 | 357 | Warfarin-PCA data and calculation of kout/kin from intercept/slope. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Needed for worked example logic. |
| Fig.4.22 | 357 | Two consecutive IV infusion concentration-time profile. | USEFUL | NO | NO | VISUAL_INSPECTED | Useful input visualization but not central if example is compressed. |
| Fig.4.23 | 359 | Response-time and response-concentration fits for two indirect response models. | USEFUL | YES | YES | VISUAL_INSPECTED | Helpful for omitted Table 4.3/model choice example. |
| Table 4.3 | 360 | Initial vs final estimates and model comparison by WRSS/AIC. | USEFUL | YES | NO | VISUAL_INSPECTED | Important worked example summary; currently underused. |
| Fig.4.24 | 361 | Repeated oral anxiolytic response downswing and kout slope. | USEFUL | YES | NO | VISUAL_INSPECTED | Supports repeated-dose initial estimate method. |
| Fig.4.25 | 363 | Translating 50% response to IC50 using response/concentration time courses. | USEFUL | YES | NO | VISUAL_INSPECTED | Useful for IC50 context. |
| Table 4.4 | 364 | Initial estimates and parameter boundaries. | USEFUL | YES | NO | VISUAL_INSPECTED | Supports boundary scaling. |
| Fig.4.40 | 368 | Analyze output as last step in modeling carousel. | USEFUL | NO | NO | VISUAL_INSPECTED | Redundant with Fig.4.16 but reinforces GOF position. |
| Fig.4.41 | 369 | Residual as vertical distance between observed and predicted curve. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Core residual definition is visual. |
| Fig.4.42 | 370 | Weighted residual patterns under absolute vs relative error. | USEFUL | YES | NO | VISUAL_INSPECTED | Supports variance model intuition. |
| Fig.4.43 | 372 | Relative residuals over time; systematic vs random residual patterns. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Learner must see pattern-to-diagnosis logic. |
| Fig.4.44 | 373 | Ordinary vs sigmoid Emax model fit, systematic deviation vs no deviation. | USEFUL | YES | NO | VISUAL_INSPECTED | Example for structural model inadequacy. |
| Fig.4.45 | 373 | Residual plots for ordinary vs sigmoid Emax. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Shows why residual plots reveal model inadequacy. |
| Fig.4.46 | 374 | Constant absolute vs relative error distributions on log/linear scales. | USEFUL | YES | YES | VISUAL_INSPECTED | Useful for weighting decisions. |
| Fig.4.47 | 374 | Bi- vs tri-exponential fits and residuals. | USEFUL | YES | NO | VISUAL_INSPECTED | Demonstrates residual amplitude/randomness. |
| Fig.4.48 | 375 | Residual plots for mono/bi/tri-exponential models. | USEFUL | YES | NO | VISUAL_INSPECTED | Complements Fig.4.47. |
| Fig.4.49 | 376 | Predicted curve mimicking trends in oral drug concentration data. | USEFUL | YES | NO | VISUAL_INSPECTED | Supports “fit trend, not only points” message. |
| Fig.4.50 | 376 | Schematic common residual plots and likely model/weighting fixes. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Highly valuable diagnostic map. |
| Table 4.5 | 377 | In vitro compound X time-concentration replicate data. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Raw data table is less important than LOF summary. |
| Fig.4.51 | 378 | Lack-of-fit visualized against replicate means. | USEFUL | YES | NO | VISUAL_INSPECTED | Supports pure error vs LOF interpretation. |
| Table 4.6 | 378 | Pure error calculation by time point. | USEFUL | NO | NO | VISUAL_INSPECTED | Numerical support for F_LOF. |
| Table 4.7 | 378 | Residual/pure/LOF SS and F_LOF. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Central numerical anchor for LOF test. |
| Fig.4.52 | 379 | Accuracy vs precision dartboard. | USEFUL | YES | NO | VISUAL_INSPECTED | Useful visual distinction. |
| Fig.4.53 | 382 | High r does not guarantee good fit; OLS r=0.96 vs IRLS r=0.94. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Essential for confusion pair. |
| Fig.4.54 | 382 | Correlation matrix graphical representation. | USEFUL | YES | YES | VISUAL_INSPECTED | Helps interpret parameter correlation. |
| Fig.4.55 | 383-384 | Confidence ellipsoids for highly correlated parameters. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Central to parameter identifiability. |
| Fig.4.56 | 384 | Different degrees of parameter correlation. | USEFUL | YES | YES | VISUAL_INSPECTED | Reinforces correlation geometry. |
| Fig.4.57 | 385 | Design A/B and resulting Cl/V correlation plots. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Shows design determines parameter correlation. |
| Fig.4.58 | 386 | Parameter perturbations and response surface/fit inspection. | USEFUL | NO | NO | VISUAL_INSPECTED | Useful but not core. |
| Table 4.8 | 389 | When F-test and AIC are inappropriate. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Apex condition table; must be viewed. |
| Fig.4.59 | 390 | Outlier A vs B and leverage/precision/accuracy consequences. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Core outlier confusion pair. |
| Table 4.9 | 391 | GOF problems, symptoms, and solutions. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Closing checklist for GOF. |
| Fig.5.4 | 400 | Partial derivatives show sampling times for A/B/alpha/beta. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Core design concept. |
| Fig.5.5 | 401 | Partial derivatives wrt n and IC50 in sigmoid Imax model. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Links derivatives to information regions. |
| Fig.5.6 | 402 | Five design points for sigmoid Emax/Imax. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Should be explicitly viewed. |
| Fig.5.7 | 402 | Turnover model with inhibition of kin. | USEFUL | YES | NO | VISUAL_INSPECTED | Supports Eq.5:15. |
| Fig.5.8 | 403 | Partial derivatives of turnover response wrt kout, IC50, n. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Directly guides sampling regions. |
| Fig.5.9 | 405 | Sensitivity analysis for Vmax, Km, Vc, Vt in MM model. | USEFUL | YES | YES | VISUAL_INSPECTED | Useful example of parameter perturbation. |
| Fig.5.10 | 405 | Sensitivity analysis for IC50, kin, kout, tlag in warfarin-PCA model. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Central to sensitivity card. |
| Fig.5.17 | 412 | Nortriptyline induction design points. | USEFUL | NO | NO | VISUAL_INSPECTED | Context for time-dependent design. |
| Fig.5.18 | 413 | Exposure metrics: Css, Cmax, AUC, time-above-target area. | USEFUL | YES | YES | VISUAL_INSPECTED | Helpful for toxicokinetic exposure design. |
| Table 5.6 | 413 | Minimalistic toxicokinetic package by study type/day. | USEFUL | YES | NO | VISUAL_INSPECTED | Supports toxicokinetic design summary. |
| Fig.5.19 | 414 | Incorrect half-life/AUC assessment under nonlinear elimination. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Important warning for nonlinear toxicokinetics. |
| Fig.5.20 | 414 | Simultaneous capacity and induction can mask exposure interpretation. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Key conceptual trap in §5.3.3. |

---

## Patch Memo Independent Classification

| Patch Memo Item | Classification Against PDF | Audit Decision |
|---|---|---|
| Phase 1 재실행 불필요 / Phase 2 필수 / HTML 직행 금지 | MATCH | Supported by audit findings. |
| Six MUST-card curation is broadly valid | MATCH | Source structure supports this spine. |
| F-test Apex choice is appropriate | MATCH | PDF strongly supports nested/equal weighting condition. |
| Regulatory Deficiency Letter / 6-month extension unsupported | MATCH | Must be fixed. |
| Eq.4:53 `r = 1 - ...` is Draft transcription error | REJECT | Visual PDF shows the same `r = 1 - ...` structure. Source fidelity does not support changing it to conventional Pearson form. |
| Eq.4:22 slope sign is Draft error | REJECT as source mismatch; OPTIONAL as math note | Draft matches PDF. PDF itself has arithmetic sign inconsistency. |
| NONMEM/CWRES/NPDE/SCM/Bayesian/Fisher/Sobol should be tagged external | MATCH | Most are not in uploaded source. |
| “80% modeling failure” unsupported | MATCH | Must delete/label unsupported. |
| pp.365-367 missing handling is correct | MATCH | Draft handled this correctly. Add p406-411 note. |
| Table 4.5-4.7, Fig.4.53, Table 4.8, §5.2.3, §5.2.4 values need audit | MATCH | Completed above. |

---

## Final Audit Conclusion

**Draft v0 is source-aligned at the conceptual spine level, but not yet source-clean.**

**Proceed:** Phase 2 완료 → Phase 3/4로 이동 가능.  
**Block:** HTML compile / final learner-facing version.  
**Mandatory before HTML:**

1. Remove or label all regulatory/business-cost claims not present in the PDF.
2. Label modern implementation bridges as external, especially NONMEM/CWRES/NPDE/SCM/Bayesian/Fisher/D-optimal/Sobol/mrgsolve.
3. Correct source range to `p.399-405 / p.412-414` and note missing p.406-411 if needed.
4. Clarify weighting exponent sign convention for Eq.4:49.
5. Restore compressed context for Fig.4.19 and Eq.4:23-4:33/Table 4.3 if A-Critical completeness is desired.
6. Do **not** apply Patch Memo’s Eq.4:53 “Pearson correction” as a source-fidelity correction; it is not supported by the rendered PDF.
7. Treat Eq.4:22 as **source-internal arithmetic inconsistency**, not Draft source mismatch.

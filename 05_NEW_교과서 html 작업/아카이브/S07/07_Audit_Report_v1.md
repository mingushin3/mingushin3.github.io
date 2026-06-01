# 07_Audit Report v1 — Source Fidelity Audit

**대상 세션**: Session 07 — 치료역·항정상태·다중투여·축적  
**업무 형태**: 파일 분석 / PDF 대조 감사 / 웹 검색 OFF  
**입력**: Original textbook PDFs + Step 1 Draft v0 + S07 Phase 1 Patch Memo  
**출력**: Audit Report v1  
**감사 역할**: Source Fidelity Auditor — 검증 전용  

---

## 0. Executive Verdict

**판정: CONDITIONAL GO to Phase 2 / NO-GO to HTML.**

Draft v0는 Session 07의 큰 축, 즉 `therapeutic window → constant-rate input → multiple-dose accumulation → loading/maintenance → TW-driven regimen design`을 넓게 포착했다. 그러나 Source Fidelity 관점에서는 다음 항목들이 HTML 전환 전에 반드시 잠겨야 한다.

1. **M4 상단 Curation Map의 차원 오류**: `C_ss,avg = ... = 1.443·F·Dose·t1/2/τ`는 source상 `A_av,ss` 식이며, concentration 식과 직접 등치하면 오류.
2. **교과서에 없는 실무·규제 단정**: `NDA 표준`, `FDA Clinical Pharmacology Section`, `deficiency letter`, `NDA 거부`, `30–40%`, `AUC 30–80%` 등은 source PDF에 없음.
3. **Daptomycin Study A 요약 오류**: `25 mg/kg q24h vs 25 mg/kg q8h`를 “same daily dose”로 표현한 부분은 오류. 같은 daily dose 비교는 `75 mg/kg q24h` vs `25 mg/kg q8h`이다.
4. **Phenobarbital R=5.8 표기 불안정**: `A_av,ss/Dose ≈ 5.76`으로는 맞지만, `R_ac = 1/(1-e^{-kτ})` 의미의 accumulation index라면 source 값은 약 6.3이다.
5. **Utility function formalization**: `U(C)=Σw_iP_i(C)` 및 `TW={C:U(C)≥threshold}`는 R&T의 therapeutic utility 개념을 수학화한 것이나, 해당 식 자체는 PDF에 없다.
6. **PK13 anchor 약화**: Source-of-Record에는 포함되어 있으나 실제 개념 카드·scenario anchor로는 충분히 사용되지 않았다.

---

## T1: Equation/Numerical Audit

중복·반복 식은 동일 source-equivalence class로 묶었다. `Classification`은 PDF source 기준이다.

| Item | Draft v0 Expression | PDF Source | Classification | Correction |
|---|---|---|---|---|
| T1-01 | `dC/dt = Rin/V - (Cl/V)·C` | G §2.2.2 p.23 Eq.2:20; R&T Ch.10 p.288 Eq.10-1/10-2 대응 | MATCH | 없음 |
| T1-02 | `C(t)=Rin/Cl[1-exp(-(Cl/V)t)]` | G p.23 Eq.2:21; R&T p.292 Eq.10-11 대응 | MATCH | 없음 |
| T1-03 | `Css = Rin/Cl` | G p.23 Eq.2:22; R&T p.288 Eq.10-4 | MATCH | 없음 |
| T1-04 | “Clearance is sole parameter determining maintenance dose / Css target” | G p.23; R&T p.288 | MATCH | 없음 |
| T1-05 | `Cpost = (Rin/Cl)(1-exp(-Cl/V·Tinf)) exp(-Cl/V·t')` | G p.23 Eq.2:23 | MATCH | 없음 |
| T1-06 | `ln[(Css-C)/Css] = -Kt` | G p.23 Eq.2:26; Fig.2.9 | MATCH | 없음 |
| T1-07 | Infusion-to-bolus intercept relation `CI ↔ C0`, Eq.2:27–2:31 | G p.24–25 | MATCH / RESTORED | Draft가 세부식을 일부만 사용. 필수 오류는 아님. |
| T1-08 | 1 half-life → 50%; 2 → 75%; 3 → 87.5/88%; 3–4 t1/2 → ~90% | G p.22 Fig.2.8; R&T p.291 Table 10-4 | MATCH | 없음 |
| T1-09 | `3.32 half-lives = 90%` | R&T p.291 Table 10-4: 3.3 half-lives = 90%; `log2(10)=3.32` | MATCH | 없음 |
| T1-10 | `5 half-lives ≈ 97%`, `6 ≈ 98%`, `7 ≈ 99%` | R&T p.291 Table 10-4 | MATCH | 없음 |
| T1-11 | `MRT = Ass/Rinf = 1/k = 1.443·t1/2 = V/CL` | R&T Ch.10 p.289 Eq.10-5~10-8 | MATCH | 없음 |
| T1-12 | Eptifibatide example: `Css 1 mg/L`, `CL 4 L/hr`, `V 14.3 L`, `k 0.28 hr^-1`, `t1/2 2.5 hr`, `Rinf 4 mg/hr` | R&T Ch.10 p.288–291 | MATCH | 없음 |
| T1-13 | t-PA half-life `5 min`, plateau in `17 min` | R&T p.291 | MATCH | 없음 |
| T1-14 | `R = Cmax,ss/Cmax,1 = 1/(1-e^{-Kτ})` | G p.44 Eq.2:75–2:78; R&T Appendix I p.795–796; R&T Ch.11 p.325 Eq.11-10 | MATCH | 없음 |
| T1-15 | `R = 1/(1-2^{-τ/t1/2})` | G p.44–45 Eq.2:77–2:78 | MATCH | 없음 |
| T1-16 | “R depends on half-life and dosing interval; independent of dose” | G p.45; R&T Ch.11 p.324–325 | MATCH | 없음 |
| T1-17 | `Cav,ss = F·Dose/(CL·τ)` | G p.45 Eq.2:79; R&T Ch.11 p.324 Eq.11-8; Table 11-6 | MATCH | 없음 |
| T1-18 | **Curation Map**: `Css,avg = F·Dose/(τ·CL) = AUC/τ = 1.443·F·Dose·t1/2/τ` | R&T p.324 Eq.11-7/11-8 and p.337 Table 11-6 separate amount vs concentration | **ERROR** | `Cav,ss = F·Dose/(CL·τ)`; `Aav,ss = 1.44·F·Dose·t1/2/τ`; only 1-compartment with known V gives `Cav,ss=Aav,ss/V`. |
| T1-19 | `Aav,ss = 1.443·F·Dose·t1/2/τ` | R&T Ch.11 p.324 Eq.11-7; Table 11-6 | MATCH | 없음 |
| T1-20 | `AUC0-τ,ss = F·Dose/CL`, `Cav,ss = AUC0-τ,ss/τ` | G p.45 Eq.2:79; R&T p.336–337 Eq.11-22 and Table 11-6 | MATCH | 없음 |
| T1-21 | `ka < k ⇒ terminal slope = ka` flip-flop | G p.45 Fig.2.29 and text | MATCH | 없음 |
| T1-22 | Oral one-site equation `C(t)=kaFD/[V(ka-k)](e^{-kt}-e^{-ka t})` | G earlier Eq.2:35 referenced on p.45; exact equation not fully in attached visible range | RESTORED [확인 필요] | PDF p.45 explicitly references Eq.2:35 and Fig.2.29; exact equation should be checked against full chapter if needed. |
| T1-23 | Two-site absorption `Frct`, `ka,rapid`, `ka,delayed` | G §2.2.11 p.46 Fig.2.31 | MATCH | 없음 |
| T1-24 | `Amax,N`, `Amin,N`, `Amax,ss`, `Amin,ss`, Eq.11-1~11-4 | R&T Ch.11 p.322–323; Appendix I p.795–796 | MATCH | 없음 |
| T1-25 | `Amax,N/Amax,ss = Amin,N/Amin,ss = 1-e^{-kNτ}` | R&T Ch.11 p.325 Eq.11-9 | MATCH | 없음 |
| T1-26 | `Amax,ss - Amin,ss = Dose` for IV bolus at plateau | R&T Ch.11 p.322–323 example and equations | MATCH | 없음 |
| T1-27 | Table 11-1 values: 200 mg q24h x 5 days; 49h total 14.4, 73h 14.87, 97h 15.04 | R&T Ch.11 p.320 Table 11-1 | MATCH | 없음 |
| T1-28 | Table 11-1 derived `t1/2=16.7 hr`, `V=20 L`, `Cmax,ss=15.82 mg/L`, `Cmin,ss=5.82 mg/L` | R&T Ch.11 p.323 | MATCH | 없음 |
| T1-29 | Phenobarbital: `t1/2=4 days`, `100 mg q24h`, 4d=50%, 8d=75%, 24d=98% | R&T Ch.11 p.324 Table 11-2 | MATCH | 없음 |
| T1-30 | Phenobarbital: `R=5.8` | R&T p.324–325: `Aav,ss≈576 mg`, `Amax,ss=630 mg`, `Amin,ss=530 mg`; Eq.11-10 gives `Rac≈6.3` | **ERROR / AMBIGUOUS** | If meaning average accumulation, write `Aav,ss/Dose≈5.76`; if meaning `Rac`, correct to `≈6.3`. |
| T1-31 | `DM = DL(1-e^{-kτ})`, `DL = DM/(1-e^{-kτ}) = Rac·DM` | R&T Ch.11 p.326–327 Eq.11-11, 11-12 | MATCH | 없음 |
| T1-32 | Doxycycline: `t1/2=24 hr`, `DL=200 mg`, `DM=100 mg/day`, `Rac=2` | R&T Ch.11 p.327 Fig.11-4 and text | MATCH | 없음 |
| T1-33 | Sirolimus: `t1/2=2.5 days`, `DL=6 mg`, `DM=2 mg/day`; draft says theoretical `R=4.13`, theoretical DL `8.3 mg` | R&T Ch.11 p.326–327 text supports clinical DL/DM; theoretical value follows Eq.11-12 | MATCH for values; RESTORED for “under-loading” interpretation | “under-loading/toxicity avoidance” is interpretation, not explicit source wording. |
| T1-34 | Table 11-3 TI × t1/2 matrix values | R&T Ch.11 p.328 Table 11-3 | MATCH | 없음, but simplify later if not all rows used. |
| T1-35 | `τmax = ln(Cupper/Clower)/k = 1.44·t1/2·ln(Cupper/Clower)` | R&T Ch.11 p.334 Eq.11-15, 11-16 | MATCH | 없음 |
| T1-36 | `DM,max = (V/F)(Cupper-Clower)` | R&T Ch.11 p.334 Eq.11-17 | MATCH | 없음 |
| T1-37 | `Css,av = (Cupper-Clower)/ln(Cupper/Clower)` | R&T Ch.11 p.334 Eq.11-19 | MATCH | 없음 |
| T1-38 | `DM = (DM,max/τmax)τ`, `DL=DM/(1-e^{-kτ})` | R&T Ch.11 p.335 Eq.11-20, 11-21 | MATCH | 없음 |
| T1-39 | Fig.11-10 example: TW 5–10 mg/L, V=20 L, t1/2=46 hr, k=0.015 hr^-1, τmax=46 hr, DMmax=100 mg, 2.17 mg/hr, τ=24h, DM≈50 mg, DL=165 mg | R&T Ch.11 p.335 Fig.11-10 text | MATCH | 없음 |
| T1-40 | Self-test example: TW 4–12, V=50, F=0.8, t1/2=12 → τmax≈19h, DMmax=500 mg, τ=12h, DM≈316→300 mg, DL=600 mg | Calculated from R&T Eq.11-15~11-21; scenario itself not in PDF | RESTORED / NOT_IN_SOURCE for scenario | Formula application is correct; fictional parameters should be labelled as exercise, not source fact. |
| T1-41 | `U(C)=Σw_iP_i(C)`, sample weights `+0.4`, `-0.2`, `-1.0`, `Uthreshold=0.10` | R&T Ch.9 discusses therapeutic utility curves qualitatively; no such explicit formula/weights | NOT_IN_SOURCE | Label as pedagogical formalization or delete from source-fidelity layer. |
| T1-42 | Phenytoin 10–20 mg/L; gentamicin peak 5–8/trough 1–2 | R&T Ch.9 p.276 Table 9-1 | MATCH | 없음 |
| T1-43 | Phenytoin toxicity levels: nystagmus ~20+, ataxia ~30, mental changes 40+ mg/L | R&T Ch.9 p.275 Fig.9-6 | MATCH | 없음 |
| T1-44 | Atorvastatin `t1/2=14 hr`, PD max 3–4 weeks | R&T Ch.11 p.343 Fig.11-16/text | MATCH | 없음 |
| T1-45 | Erythropoietin `t1/2=9 hr`, hematocrit plateau ~70 days | R&T Ch.11 p.344 Fig.11-17/text | MATCH | 없음 |
| T1-46 | Acquired resistance = mutation/cell population; tolerance = PD adaptation; tachyphylaxis acute tolerance; tolerance never complete | R&T Ch.11 p.346 | MATCH | 없음 |
| T1-47 | `AUC/MIC >101`: 9% resistant; `<100`: only 50% susceptible after 5 days | R&T Ch.11 p.348 Fig.11-20 | MATCH | Draft’s shorthand “resistance avoidance” is acceptable but should preserve quantitative nuance if used. |
| T1-48 | `AUC/MIC target 35` for fluoroquinolone/Pseudomonas respiratory infection | R&T Ch.11 p.348 text | MATCH | 없음 |
| T1-49 | Daptomycin Study A: 25 mg/kg q24h vs 25 mg/kg q8h “same daily dose” | R&T Ch.11 p.351–353: groups are saline q8h, 25 q24h, 75 q24h, 25 q8h | **ERROR** | Same daily dose comparison is `75 mg/kg q24h` vs `25 mg/kg q8h`; `25 q24h` vs `25 q8h` is same dose per administration, not same daily dose. |
| T1-50 | Daptomycin Study A CPK: 25 q24h 994 U/L; 75 q24h 991; 25 q8h 3996 | R&T Ch.11 p.353 Table 11-7 | MATCH | 없음 |
| T1-51 | Daptomycin Study B: same Cmax 58 µg/mL; AUC 180 vs 412; CPK 157 vs 483 | R&T Ch.11 p.352–353 Table 11-7 | MATCH | 없음 |
| T1-52 | “q24h CPK no change, q12h CPK increase in healthy volunteers; FDA-approved once-daily label; 4–6 mg/kg IV q24h” | Not in attached PDF pages | NOT_IN_SOURCE | Remove or mark as external regulatory/label information requiring separate source. |
| T1-53 | Trench Tip: pump/catheter issue probability `30–40%` | Not in attached PDFs | NOT_IN_SOURCE | Delete number or label as unsupported field heuristic. |
| T1-54 | SS=1 misuse → `AUC 30–80%` overprediction → Phase 3 SAE → NDA refusal | Not in attached PDFs | NOT_IN_SOURCE | Delete numerical/causal chain or label as external risk scenario. |
| T1-55 | `FDA Clinical Pharmacology Section`, `NDA 표준`, `Deficiency Letter` | Not in attached PDFs | NOT_IN_SOURCE | Use only as explicitly labelled external regulatory framing; not as source-derived claim. |
| T1-56 | Cardarone-X fictional case: t1/2=4h, V=100L, F=0.6, TW[1,4], q6h vs q8h redesign | No such drug/case in PDFs | NOT_IN_SOURCE | Keep only as fictional exercise; do not imply source anchor. |

---

## T2: Examples & Data Audit

| Item | Draft v0 Status | PDF Location | Classification | Importance | Action |
|---|---|---|---|---|---|
| G constant infusion, Fig.2.8 | Included in M1/M2 | G p.22 | INCLUDED_CORRECT | HIGH | 유지 |
| G steady-state definition and deconvolution statement | Partly included | G p.25 | INCLUDED_CORRECT | MEDIUM | `steady state ≠ thermodynamic equilibrium` nuance can remain CONTEXT |
| G input functions: bolus, zero-order, first-order, multiple zero-/first-order, log+zero-order | Included as C5 | G p.43 Fig.2.27 | INCLUDED_CORRECT | MEDIUM | 유지, 1–2문장 압축 가능 |
| G multiple dosing accumulation, Fig.2.28 | Included | G p.43–44 | INCLUDED_CORRECT | HIGH | 유지 |
| G accumulation factor Eq.2:75–2:78 | Included M3 | G p.44–45 | INCLUDED_CORRECT | HIGH | 유지 |
| G flip-flop Fig.2.29 | Included M5 | G p.45 | INCLUDED_CORRECT | HIGH | 유지 |
| G repeated dosing Fig.2.30, drug half-life 7h → 21–28h | Partly included | G p.45–46 | INCLUDED_CORRECT | MEDIUM | 유지 |
| G multiple absorption sites Fig.2.31 | Included as context | G p.46 | INCLUDED_CORRECT | MEDIUM | 유지 |
| G PK11 two-compartment repeated oral dosing | Source listed, weakly integrated | G p.528–531 | MISSING/UNDERUSED | MEDIUM | Phase 4 simulator/scenario anchor에 명시 배치 |
| G PK13 bolus + constant infusion | Source listed, weakly integrated | G p.537–539 | MISSING/UNDERUSED | HIGH | `400 µg/kg bolus + 800 µg/kg over 26 min; Vc=2 L/kg; CL=1 L/min/kg; Cld=1; Vt=5` anchor 반영 |
| R&T Ch.9 dosage regimen determinants, Fig.9-1 | Included M6 roadmap | R&T p.267–268 | INCLUDED_CORRECT | HIGH | 유지 |
| R&T Fig.9-2 dose-response cohort example placebo/10/20/40 mg | Mostly omitted | R&T p.269–270 | MISSING | MEDIUM | M6에서 TW 형성 예시로 1문장 가능 |
| R&T Fig.9-3 therapeutic effectiveness/utility curves | Partly abstracted | R&T p.272 | INCLUDED_ERROR/PARTIAL | HIGH | `U(C)` 수식은 source 식이 아님. Qualitative curve로 낮추기 |
| R&T Fig.9-4 poor dose-response due to PK variability | Partly included | R&T p.273 | INCLUDED_CORRECT | MEDIUM | 유지 |
| R&T Fig.9-5 poor systemic exposure-response cases | Partly included | R&T p.274 | INCLUDED_CORRECT | MEDIUM | 유지 |
| R&T Fig.9-6 phenytoin escalation | Included | R&T p.275 | INCLUDED_CORRECT | HIGH | 유지 |
| R&T Table 9-1 selected concentration ranges | Included | R&T p.276 | INCLUDED_CORRECT | HIGH | 유지 |
| R&T Fig.9-7 mutant selection window | Partly included through AUC/MIC/resistance | R&T p.277 | INCLUDED_CORRECT | MEDIUM | Fig.9-7 자체는 CONTEXT 가능 |
| R&T Table 9-2 probabilities | Omitted | R&T p.281 | MISSING | LOW | Study problem; omission justified |
| R&T Appendix I telescoping derivation/table I-1/I-2 | Included M3 | R&T p.795–797 | INCLUDED_CORRECT | HIGH | 유지 |
| R&T Ch.10 IV infusion drug examples Table 10-1 | Included as input mapping | R&T p.284 | INCLUDED_CORRECT | MEDIUM | 유지 |
| R&T Ch.10 devices Tables 10-2/10-3 | Included as input mapping | R&T p.285–286 | INCLUDED_CORRECT | MEDIUM | 유지 |
| R&T Ch.10 eptifibatide example | Included M1/M2/M7 | R&T p.288–292 | INCLUDED_CORRECT | HIGH | 유지 |
| R&T Ch.10 t-PA Fig.10-6 | Included as source anchor | R&T p.293 | INCLUDED_CORRECT | MEDIUM | 유지 |
| R&T Ch.10 furosemide Fig.10-11 | Mentioned as response delay? | R&T p.298 | INCLUDED_CORRECT/PARTIAL | MEDIUM | If retained, clarify as PD/time-course, not accumulation equation anchor |
| R&T Ch.10 turnover examples Table 10-5, Fig.10-12~10-18 | Partly included C15 | R&T p.299–307 | INCLUDED_CORRECT | MEDIUM | Keep as CONTEXT only |
| R&T Ch.10 PK/PD indices Fig.10-20/10-21/10-22 | Included M6 | R&T p.307–312 | INCLUDED_CORRECT | HIGH | 유지 |
| R&T Ch.10 physiologic changes Table 10-6/Fig.10-19 | Mentioned | R&T p.309–310 | INCLUDED_CORRECT | MEDIUM | Maintain but do not over-expand |
| R&T Ch.10 nifedipine/droperidol/rolipram study problems | Omitted | R&T p.313–317 | MISSING | LOW | Study problem; omission justified |
| R&T Ch.11 superposition Table 11-1/Fig.11-1 | Included M4 | R&T p.320–321 | INCLUDED_CORRECT | HIGH | 유지 |
| R&T Ch.11 IV bolus accumulation Fig.11-2 | Included M3 | R&T p.322 | INCLUDED_CORRECT | HIGH | 유지 |
| R&T Ch.11 phenobarbital Table 11-2 | Included but R label unstable | R&T p.324–325 | INCLUDED_ERROR | HIGH | `R=5.8` 의미 수정 필요 |
| R&T Ch.11 Fig.11-3 frequency independence | Included M3 | R&T p.325 | INCLUDED_CORRECT | HIGH | 유지 |
| R&T Ch.11 doxycycline Fig.11-4 | Included M7 | R&T p.327 | INCLUDED_CORRECT | HIGH | 유지 |
| R&T Ch.11 Table 11-3 TI × t1/2 | Included M6 | R&T p.328 | INCLUDED_CORRECT | HIGH | 유지 |
| R&T Ch.11 amoxicillin/naproxen/piroxicam Tables 11-4/11-5; Figs 11-5~11-7 | Included M4 | R&T p.330–332 | INCLUDED_CORRECT | HIGH | 유지 |
| R&T Ch.11 extravascular Figs 11-8/11-9 | Lightly included | R&T p.333 | INCLUDED_CORRECT | MEDIUM | Keep as CONTEXT |
| R&T Ch.11 TW algorithm Fig.11-10/Eq.11-14~11-22 | Included M8 | R&T p.334–337 | INCLUDED_CORRECT | HIGH | 유지 |
| R&T Ch.11 clobazam Fig.11-12 | Underused | R&T p.336 | MISSING | MEDIUM | Single-dose AUC → plateau validation example로 1문장 추가 가능 |
| R&T Ch.11 modified release morphine Fig.11-13 | Included | R&T p.337–338 | INCLUDED_CORRECT | MEDIUM | 유지 |
| R&T Ch.11 evaluation Fig.11-14/Eq.11-23~25 | Included in source list; lightly used | R&T p.339–341 | INCLUDED_CORRECT/PARTIAL | MEDIUM | If Phase 4 scope allows, CONTEXT로 압축 |
| R&T Ch.11 PD-driven dosing Fig.11-15; atenolol/morphine | Included | R&T p.341–342 | INCLUDED_CORRECT | HIGH | 유지 |
| R&T Ch.11 atorvastatin Fig.11-16 | Included | R&T p.343 | INCLUDED_CORRECT | HIGH | 유지 |
| R&T Ch.11 erythropoietin Fig.11-17 | Included | R&T p.344 | INCLUDED_CORRECT | HIGH | 유지 |
| R&T Ch.11 onset/duration/intensity Fig.11-18 | Lightly included | R&T p.345 | INCLUDED_CORRECT/PARTIAL | MEDIUM | CONTEXT 가능 |
| R&T Ch.11 acquired resistance/tolerance | Included | R&T p.346 | INCLUDED_CORRECT | HIGH | 유지 |
| R&T Ch.11 Fig.11-19 ceftazidime/gentamicin | Included | R&T p.347 | INCLUDED_CORRECT | HIGH | 유지 |
| R&T Ch.11 Fig.11-20 AUC/MIC resistance | Included | R&T p.348 | INCLUDED_CORRECT | HIGH | 유지 |
| R&T Ch.11 altered absorption/disposition Figs.11-22/11-23 | Included | R&T p.350–351 | INCLUDED_CORRECT | MEDIUM | 유지 |
| R&T Ch.11 daptomycin Fig.11-24/Table11-7 | Included, one comparison error | R&T p.351–353 | INCLUDED_ERROR | HIGH | Same daily dose comparison correction required |
| R&T Ch.11 study problems Tables 11-8~11-12 | Mostly omitted | R&T p.354–358 | MISSING | LOW | Study problem material; omission justified unless §7 self-test uses them |

---

## T3: Author Key Messages

| Message | PDF Location | In Draft v0? | Status |
|---|---|---|---|
| Constant infusion concentration rises to plateau; 1 t1/2=50%, 3–4 t1/2≈90%. | G p.22; R&T p.291 | Yes | INCLUDED |
| `Css = Rin/Cl`; clearance controls maintenance dosing to keep target Css. | G p.23; R&T p.288 | Yes | INCLUDED |
| Steady state means rate in equals rate out; for discrete dosing, equivalent profiles recur over intervals. | G p.25; R&T p.322 | Yes | INCLUDED |
| Steady state is not thermodynamic equilibrium, although the book uses the terms interchangeably. | G p.25 | Partly | SHOULD_FIX as CONTEXT nuance |
| Accumulation factor depends on half-life and dosing interval, not dose. | G p.44–45 | Yes | INCLUDED |
| Time to 90% steady state depends only on half-life; average steady-state concentration depends on dosing rate and clearance. | G p.45 | Yes | INCLUDED |
| Flip-flop: when absorption is rate-limiting, terminal slope reflects absorption. | G p.45 | Yes | INCLUDED |
| Multiple peaks after extravascular dosing do not necessarily mean enterohepatic recirculation. | G p.46 | Yes/Context | INCLUDED |
| Dosage regimens optimize therapy by balancing harm risk and achievable benefit. | R&T Ch.9 p.267–268 | Yes | INCLUDED |
| Exposure-response data are often limited; therapeutic window may be defined clinically by dose rather than concentration in large trials. | R&T Ch.9 p.269 | Partly | SHOULD_FIX |
| Poor systemic exposure-response relationships can occur and must be diagnosed. | R&T Ch.9 p.273–274 | Partly | INCLUDED_PARTIAL |
| All substances produce harm if given high enough amounts. | R&T p.267 | No | OPTIONAL |
| Constant-rate IV input is precise and can be stopped instantly; institutional limitation exists. | R&T Ch.10 p.283 | Partly | OPTIONAL/CONTEXT |
| Plateau amount depends on infusion rate and k; plateau concentration depends on infusion rate and clearance. | R&T Ch.10 p.288 | Yes | INCLUDED |
| Approach to a new plateau, higher or lower, depends only on half-life. | R&T Ch.10 p.292 | Yes | INCLUDED |
| After stopping infusion, concentration falls by half each half-life; some transdermal systems decline slower due to continued input. | R&T Ch.10 p.291 | Partly | SHOULD_FIX as CONTEXT |
| Multiple-dose concentration profile can be predicted by superposition of the single-dose profile without PK parameters, if same regimen and linearity hold. | R&T Ch.11 p.320–321 | Yes | INCLUDED |
| Plateau during discrete dosing is not constant within interval; values at the same time in the interval repeat. | R&T Ch.11 p.322 | Yes | INCLUDED |
| Extent of accumulation is frequency relative to half-life; accumulation itself is not an intrinsic label of a drug. | R&T Ch.11 p.324 | Yes | INCLUDED |
| Same average dosing rate gives same approach time to plateau; dosing interval changes fluctuation. | R&T Ch.11 p.325 Fig.11-3 | Yes | INCLUDED |
| Loading dose rationale: immediate plateau; for some drugs loading is omitted/divided to avoid acute toxicity. | R&T Ch.11 p.326–329 | Yes | INCLUDED |
| Design of regimen can be based on `Cupper`, `Clower`, `t1/2`, `V`, `F`; choose practical interval/dose strengths. | R&T Ch.11 p.334–335 | Yes | INCLUDED |
| PD can govern time to plateau effect more than PK; statins and erythropoietin are examples. | R&T Ch.11 p.342–344 | Yes | INCLUDED |
| Acquired resistance and tolerance are distinct mechanisms of declining effectiveness. | R&T Ch.11 p.346 | Yes | INCLUDED |
| Daptomycin toxicity depends on dose fractionation/recovery time, not simply Cmax or AUC24. | R&T Ch.11 p.351–353 | Yes, with one error | INCLUDED_ERROR |
| Patients vary; next section covers individualization. | R&T Ch.11 p.353 | No | OPTIONAL |

---

## T4: Priority Summary (sorted: MUST_FIX → SHOULD_FIX → OPTIONAL → REJECT)

| # | Item | Priority | Rationale |
|---|---|---|---|
| 1 | M4 Curation Map: concentration equation equated to amount equation | MUST_FIX | Dimensionally wrong; R&T Eq.11-7 and 11-8 explicitly separate `Aav,ss` and `Cav,ss`. |
| 2 | Daptomycin Study A “same daily dose” comparison | MUST_FIX | Source comparison is 75 q24h vs 25 q8h for same total daily dose; current wording is factual error. |
| 3 | Phenobarbital `R=5.8` as accumulation index | MUST_FIX | If `Rac`, source/formula gives ~6.3; 5.8 is only close to average amount/dose. |
| 4 | Unsupported numerical/regulatory chains: `30–40%`, `AUC 30–80%`, `SAE`, `NDA refusal`, `Deficiency Letter` | MUST_FIX | Not present in source PDFs; violates source-fidelity mode. |
| 5 | `FDA Clinical Pharmacology Section`, `NDA standard language` as if source-derived | MUST_FIX | No attached PDF source; must be labelled external or removed. |
| 6 | `U(C)` weighted utility formula and sample weights | SHOULD_FIX | R&T supports qualitative utility curves but not this equation/weights. Keep only as labelled formalization. |
| 7 | PK13 source anchor underused | SHOULD_FIX | Source-of-Record includes PK13; current draft does not sufficiently use its numerical anchor. |
| 8 | G p.25 steady state vs equilibrium nuance | SHOULD_FIX | Author explicitly states distinction; valuable for rigorous understanding. |
| 9 | R&T Ch.11 clobazam Fig.11-12 underused | SHOULD_FIX | Strong example for single-dose AUC predicting average plateau concentration. |
| 10 | Overdense M6/M7/M8 repeated regulatory phrasing | SHOULD_FIX | Not a source error, but increases risk of unsourced claims and obscures hierarchy. |
| 11 | Study problems and peripheral tables not integrated | OPTIONAL | Most are exercises, not essential source concepts. |
| 12 | Extra fictional Cardarone-X case | OPTIONAL / REJECT if unlabeled | Safe only as fictional exercise; reject if presented as source-derived. |
| 13 | Patch memo’s “Phase 1 redo 불필요 / Phase 2로 진행” | OPTIONAL | Process judgment, not a PDF claim; reasonable but outside source-fidelity audit. |

### Patch Memo independent classification

| Patch memo item | Classification vs PDF | Audit decision |
|---|---|---|
| “M4 amount vs concentration 혼합” | MATCH | MUST_FIX confirmed. |
| “30–40%, AUC 30–80%, NDA 거부 등 unsupported” | MATCH | MUST_FIX confirmed. |
| “Scope Lock 병존” | OPTIONAL | Process issue, not source-fidelity claim; still useful workflow hygiene. |
| “PK13 anchor 약함” | MATCH | SHOULD_FIX confirmed. |
| “압축 필요” | OPTIONAL | Content-lock issue, not direct PDF fidelity. |
| “Phenobarbital R=5.8 육안 확인 필요” | MATCH → ERROR clarified | R_ac라면 ~6.3; average amount/dose라면 ~5.76. |

---

## T5: Coverage Audit

### T5-A. Section headings and structural coverage

| PDF Element | Type | PDF Location | Step 1 Status | Omission Verdict | Required Action |
|---|---|---|---|---|---|
| G §2.2.2 Constant rate infusion | H2 | G p.22–25 | INCLUDED_AS_MUST | — | M1/M2 유지 |
| G §2.2.3 Integration of clearance and volume | H2 | G p.25 onward, partially included by PDF range | OMITTED_JUSTIFIABLE | Out of current core range except transition | 없음 |
| G §2.2.9 How does input to the plasma compartment vary? | H2 | G p.43 | INCLUDED_AS_CONTEXT | — | C5 유지 |
| G §2.2.10 Multiple dosing | H2 | G p.43–45 | INCLUDED_AS_MUST | — | M3/M4/M5 유지 |
| G §2.2.11 Absorption from multiple sites | H2 | G p.46 | INCLUDED_AS_CONTEXT | — | CONTEXT 유지 |
| G Case Study PK11 — Two-compartment repeated oral dosing | Case study | G p.528–531 | INCLUDED_AS_CONTEXT/PARTIAL | OMITTED_PROBLEMATIC: MISSING_EXAMPLE | Simulator/scenario anchor 보강 |
| G Case Study PK13 — Bolus plus constant infusion | Case study | G p.537–539 | INCLUDED_AS_CONTEXT/PARTIAL | OMITTED_PROBLEMATIC: MISSING_EXAMPLE | Numerical anchor 보강 |
| R&T Ch.9 Objectives | Chapter opening | R&T p.267 | INCLUDED_AS_CONTEXT | — | 없음 |
| R&T Ch.9 Dosage Regimens | H2 | R&T p.267–269 | INCLUDED_AS_MUST | — | M6 유지 |
| R&T Ch.9 Therapeutic Exposure | H2 | R&T p.269–277 | INCLUDED_AS_MUST | — | M6 유지; utility formula source labeling 필요 |
| R&T Ch.9 Therapeutic Index | H2 | R&T p.278 | INCLUDED_AS_CONTEXT | — | §5-쌍5 유지 |
| R&T Ch.9 Additional Considerations | H2 | R&T p.279 | INCLUDED_AS_CONTEXT/PARTIAL | OMITTED_JUSTIFIABLE | Multiple active species 등 필요 시 압축 |
| R&T Ch.9 Achieving Therapeutic Goals | H2 | R&T p.280 | INCLUDED_AS_CONTEXT | — | M6 결론에 반영 가능 |
| R&T Ch.9 Study Problems | H2 | R&T p.280–281 | OMITTED_JUSTIFIABLE | Exercises | 없음 |
| R&T Appendix I Accumulation | Appendix | R&T p.795–797 | INCLUDED_AS_MUST | — | M3 유지 |
| R&T Ch.10 Objectives/opening | Chapter opening | R&T p.283 | INCLUDED_AS_CONTEXT | — | 없음 |
| R&T Ch.10 constant-rate devices/tables | H2 content | R&T p.284–286 | INCLUDED_AS_CONTEXT | — | C5 유지 |
| R&T Ch.10 Exposure-time relationships | H2 | R&T p.287–292 | INCLUDED_AS_MUST | — | M1/M2 유지 |
| R&T Ch.10 The Plateau Value | H3 | R&T p.288 | INCLUDED_AS_MUST | — | M1 유지 |
| R&T Ch.10 Mean Residence Time | H3 | R&T p.289 | INCLUDED_AS_CONTEXT | — | M4/MRT nuance 유지 |
| R&T Ch.10 Time to Reach Plateau | H3 | R&T p.290–292 | INCLUDED_AS_MUST | — | M2 유지 |
| R&T Ch.10 Postinfusion | H3 | R&T p.291 | INCLUDED_AS_CONTEXT/PARTIAL | OMITTED_PROBLEMATIC: MISSING_BRIDGE | Transdermal continued input nuance optional context |
| R&T Ch.10 Bolus plus Infusion | H2 | R&T p.293–295 | INCLUDED_AS_MUST | — | M7 유지 |
| R&T Ch.10 Pharmacodynamics | H2 | R&T p.296–298 | INCLUDED_AS_CONTEXT | — | M6 context 유지 |
| R&T Ch.10 Turnover of Affected Systems | H2 | R&T p.299–304 | INCLUDED_AS_CONTEXT | — | C15 유지, 과확장 금지 |
| R&T Ch.10 Influences on Kinetics and Pharmacodynamics | H2 | R&T p.305–312 | INCLUDED_AS_CONTEXT | — | C12/C13 유지 |
| R&T Ch.10 Study Problems | H2 | R&T p.312–318 | OMITTED_JUSTIFIABLE | Exercises | 없음 |
| R&T Ch.11 Objectives/opening | Chapter opening | R&T p.319 | INCLUDED_AS_CONTEXT | — | 없음 |
| R&T Ch.11 Principles of Drug Accumulation | H2 | R&T p.320–326 | INCLUDED_AS_MUST | — | M3/M4 유지 |
| R&T Ch.11 Maxima and Minima on Accumulation to Plateau | H3 | R&T p.321–323 | INCLUDED_AS_MUST | — | M3 유지 |
| R&T Ch.11 Average Level at Plateau | H3 | R&T p.323–324 | INCLUDED_AS_MUST | — | M4 유지, dimension fix 필요 |
| R&T Ch.11 Rate of Accumulation to Plateau | H3 | R&T p.324–325 | INCLUDED_AS_MUST | — | M2/M3 유지 |
| R&T Ch.11 Accumulation Index | H3 | R&T p.325–326 | INCLUDED_AS_MUST | — | phenobarbital R fix 필요 |
| R&T Ch.11 Relationship Between Initial and Maintenance Doses | H2 | R&T p.326–328 | INCLUDED_AS_MUST | — | M7 유지 |
| R&T Ch.11 Maintenance of Drug in Therapeutic Range | H2 | R&T p.328–329 | INCLUDED_AS_MUST | — | M6 유지 |
| R&T Ch.11 Reinforcing the Principles | H2 | R&T p.330–332 | INCLUDED_AS_MUST | — | M4 examples 유지 |
| R&T Ch.11 Extravascular Considerations | H2 | R&T p.332–334 | INCLUDED_AS_CONTEXT | — | Context 유지 |
| R&T Ch.11 Design of Dosage Regimens Using Plasma Concentration | H2 | R&T p.334–337 | INCLUDED_AS_MUST | — | M8 유지 |
| R&T Ch.11 Modified-Release Products | H2 | R&T p.337–338 | INCLUDED_AS_CONTEXT | — | Context 유지 |
| R&T Ch.11 Evaluation of a Multiple-Dose Regimen | H2 | R&T p.339–341 | INCLUDED_AS_CONTEXT/PARTIAL | OMITTED_PROBLEMATIC: MISSING_BRIDGE | Eq.11-23~25는 context로 명확화 |
| R&T Ch.11 Pharmacodynamic Considerations | H2 | R&T p.341–348 | INCLUDED_AS_MUST | — | M6 유지 |
| R&T Ch.11 When Absorption or Disposition is Altered | H2 | R&T p.348–353 | INCLUDED_AS_CONTEXT/MUST for daptomycin | — | daptomycin 오류 수정 |
| R&T Ch.11 Other Situations and closing transition to individualization | Closing | R&T p.353 | OMITTED_JUSTIFIABLE | Low priority closing | Optional note only |
| R&T Ch.11 Study Problems | H2 | R&T p.353–358 | OMITTED_JUSTIFIABLE | Exercises | 없음 |

### T5-B. Numbered formulas/equation groups

| PDF Element | Type | PDF Location | Step 1 Status | Omission Verdict | Required Action |
|---|---|---|---|---|---|
| G Eq.2:19–2:23 | Equations | G p.22–23 | INCLUDED_AS_MUST | — | 유지 |
| G Eq.2:24–2:26 | Equations | G p.23 | INCLUDED_AS_CONTEXT | — | 유지 |
| G Eq.2:27–2:31 | Equations | G p.24–25 | INCLUDED_AS_CONTEXT/PARTIAL | OMITTED_JUSTIFIABLE | PK13/Vss context 외 독립 카드 불필요 |
| G Eq.2:75–2:78 | Equations | G p.44–45 | INCLUDED_AS_MUST | — | 유지 |
| G Eq.2:79 | Equation | G p.45 | INCLUDED_AS_MUST | — | 유지 |
| R&T Eq.10-1–10-4 | Equations | R&T p.288 | INCLUDED_AS_MUST | — | 유지 |
| R&T Eq.10-5–10-8 | Equations | R&T p.289 | INCLUDED_AS_CONTEXT | — | MRT context 유지 |
| R&T Eq.10-9–10-11 | Equations | R&T p.290–292 | INCLUDED_AS_MUST | — | M2/M7 유지 |
| R&T Eq.10-12~10-16 turnover equations | Equations | R&T p.299–304 | INCLUDED_AS_CONTEXT | — | 독립 확장 금지 |
| R&T Eq.11-1–11-4 | Equations | R&T p.322–323 | INCLUDED_AS_MUST | — | 유지 |
| R&T Eq.11-5–11-8 | Equations | R&T p.323–324 | INCLUDED_AS_MUST | — | M4 dimension fix |
| R&T Eq.11-9–11-10 | Equations | R&T p.325–326 | INCLUDED_AS_MUST | — | 유지 |
| R&T Eq.11-11–11-13 | Equations | R&T p.326–333 | INCLUDED_AS_MUST/CONTEXT | — | 유지 |
| R&T Eq.11-14–11-22 | Equations | R&T p.334–337 | INCLUDED_AS_MUST | — | M8 유지 |
| R&T Eq.11-23–11-25 | Equations | R&T p.341 | INCLUDED_AS_CONTEXT/PARTIAL | OMITTED_PROBLEMATIC: MISSING_BRIDGE | Evaluation context로 1–2문장 보강 |
| Appendix I Eq.I-1~I-10 | Equations | R&T p.795–797 | INCLUDED_AS_MUST | — | 유지 |

### T5-C. Repeated author messages

| Repeated message | PDF Location | Step 1 Status | Omission Verdict | Required Action |
|---|---|---|---|---|
| Time to approach plateau depends only on half-life | G p.22/45; R&T Ch.10 p.291–292; Ch.11 p.324–325 | INCLUDED_AS_MUST | — | 유지 |
| Plateau level/concentration is determined by input rate and CL/k, not by half-life alone | G p.23/45; R&T p.288 | INCLUDED_AS_MUST | — | 유지 |
| Average rate determines average plateau; dosing interval controls fluctuation | R&T Ch.11 p.325 Fig.11-3; p.337 Table 11-6 | INCLUDED_AS_MUST | — | 유지 |
| Single-dose profile can predict repeated-dose profile by superposition | R&T Ch.11 p.320–321; p.336–337 | INCLUDED_AS_MUST | — | 유지 |
| PD response may not follow PK plateau time | R&T Ch.10 p.296–307; Ch.11 p.341–345 | INCLUDED_AS_MUST | — | 유지 |

---

## T6: Figure Inventory & Learning Value Audit

All pages were rendered to images and inspected as contact sheets plus targeted page renders where numerical/figure content was important. `VISUAL_INSPECTED` therefore means the rendered page containing the figure/table was visually inspected; small-font numerical extraction still relies on accompanying text when needed.

| Figure/Table | Page | Teaches | Value | View Instruction? | Redraw/New Schematic? | Inspection Method | Rationale |
|---|---:|---|---|---|---|---|---|
| G Fig.2.8 | G p.22 | Constant infusion rises asymptotically to steady state by half-lives. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M1/M2의 핵심 그래프. |
| G Fig.2.9 | G p.24 | `ln(R)` residual slope during infusion estimates K. | USEFUL | NO | NO | VISUAL_INSPECTED | 식만으로 충분하나 보강 가치 있음. |
| G Fig.2.10 | G p.25 | Infusion intercept `CI` depends on infusion length relative to bolus `C0`. | USEFUL | NO | NO | VISUAL_INSPECTED | PK13/Vss 연결에 유용. |
| G Fig.2.27 | G p.43 | Input functions and corresponding responses. | USEFUL | YES | YES | VISUAL_INSPECTED | 입력 함수 분류를 한눈에 보여줌. |
| G Fig.2.28 | G p.44 | Repeated dosing accumulates toward same time-to-SS independent of dose. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M3의 dose-independent time-to-SS 핵심. |
| G Fig.2.29 | G p.45 | Flip-flop vs ordinary terminal slope identity. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M5 이해에 필수. |
| G Fig.2.30 | G p.46 | Repeated dose AUC within interval corresponds to amount eliminated. | USEFUL | YES | YES | VISUAL_INSPECTED | M4 평균농도/steady-state AUC 연결에 도움. |
| G Fig.2.31 | G p.46 | Two-site absorption can create two peaks. | USEFUL | NO | NO | VISUAL_INSPECTED | Context 수준. |
| G PK11 Fig.11.1 | G p.528–529 | Two-compartment repeated oral dose concentration-time data and model. | USEFUL | YES | NO | VISUAL_INSPECTED | Simulator anchor로 유용. |
| G PK11 Fig.11.2 | G p.529–530 | Observed concentration-effect relationship in PK11. | USEFUL | NO | NO | VISUAL_INSPECTED | PD 연결 보강. |
| G PK13 Fig.13.1 | G p.537–539 | Bolus plus constant infusion two-compartment data. | USEFUL | YES | NO | VISUAL_INSPECTED | Source-of-Record인데 draft 반영 약함. |
| R&T Fig.9-1 | p.268 | Dosage regimen is determined by PK, PD, clinical factors. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M6 roadmap의 구조 그림. |
| R&T Fig.9-2 | p.270 | Dose-response cohorts show benefit/adverse categories across placebo/10/20/40 mg. | USEFUL | YES | YES | VISUAL_INSPECTED | TW 형성 예시. |
| R&T Fig.9-3 | p.272 | Therapeutic effectiveness and utility curves. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Draft의 utility formalization을 원문 그래프로 되돌릴 필요. |
| R&T Fig.9-4 | p.273 | PK variability can obscure dose-response while exposure-response remains clearer. | USEFUL | YES | YES | VISUAL_INSPECTED | Exposure-response reasoning에 중요. |
| R&T Fig.9-5 | p.274 | Poor systemic exposure-response scenarios. | USEFUL | YES | YES | VISUAL_INSPECTED | M6 limitation에 유용. |
| R&T Fig.9-6 | p.275 | Phenytoin therapeutic window/toxicity escalation. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Strong clinical anchor. |
| R&T Table 9-1 | p.276 | Selected drugs and usual therapeutic plasma concentration ranges. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | TDM/TW anchor. |
| R&T Fig.9-7 | p.277 | Mutant selection window above MIC. | USEFUL | YES | YES | VISUAL_INSPECTED | Resistance bridge. |
| R&T Table 9-2 | p.281 | Study problem probabilities for response/adverse events. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Exercise material. |
| R&T Table I-1 | p.795 | Drug remaining after successive equal doses. | USEFUL | YES | NO | VISUAL_INSPECTED | Telescoping derivation support. |
| R&T Table I-2 | p.797 | Diazepam successive-dose exercise table. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Exercise. |
| R&T Table 10-1 | p.284 | Examples of drugs given by IV infusion. | USEFUL | NO | NO | VISUAL_INSPECTED | Context mapping. |
| R&T Table 10-2 | p.285–286 | Constant-rate devices/systems. | USEFUL | NO | NO | VISUAL_INSPECTED | Input route context. |
| R&T Table 10-3 | p.286 | Transdermal systems. | USEFUL | NO | NO | VISUAL_INSPECTED | Input route context. |
| R&T Fig.10-1 | p.287 | Plasma concentration around infusion start/stop. | USEFUL | YES | YES | VISUAL_INSPECTED | Dynamic intuition. |
| R&T Fig.10-2 | p.287 | Constant-rate input reservoir model. | USEFUL | YES | YES | VISUAL_INSPECTED | M1 derivation visual. |
| R&T Fig.10-3 | p.288 | Amount time course depends on input and elimination. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | `Rinf`, `kA`, `CL·C` core. |
| R&T Fig.10-4 | p.290 | Approach to plateau and bolus-from-plateau idea. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M2/M7 bridge. |
| R&T Table 10-4 | p.291 | Percentage of plateau at half-life multiples. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | 3.3 half-life rule source. |
| R&T Fig.10-5 | p.292 | New plateau up/down depends only on half-life. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Author repeated message. |
| R&T Fig.10-6 | p.293 | t-PA concentration on changing infusion rate. | USEFUL | NO | NO | VISUAL_INSPECTED | Empirical support. |
| R&T Fig.10-7 | p.294 | Plateau depends on infusion rate, not initial bolus. | USEFUL | YES | YES | VISUAL_INSPECTED | M7 loading caveat. |
| R&T Fig.10-8 | p.295 | Plateau plasma concentration depends on t1/2 and CL changes. | USEFUL | NO | YES | VISUAL_INSPECTED | Conceptually useful but not central. |
| R&T Fig.10-9 | p.296 | Bolus + infusion can maintain concentration. | USEFUL | YES | YES | VISUAL_INSPECTED | M7 visual. |
| R&T Fig.10-10 | p.297 | Onset/offset of effect after infusion can differ from concentration. | USEFUL | YES | YES | VISUAL_INSPECTED | PD bridge. |
| R&T Fig.10-11 | p.298 | Furosemide sodium excretion response over time. | USEFUL | NO | NO | VISUAL_INSPECTED | Response delay example. |
| R&T Table 10-5 | p.299 | Examples of altered turnover. | USEFUL | NO | NO | VISUAL_INSPECTED | Turnover context. |
| R&T Fig.10-12 | p.300 | Pool size after blocked elimination/input. | USEFUL | NO | YES | VISUAL_INSPECTED | Turnover analogy. |
| R&T Fig.10-13 | p.302 | Increased/decreased turnover rate effects. | USEFUL | NO | YES | VISUAL_INSPECTED | Context. |
| R&T Fig.10-14 | p.303 | Pool size and fractional turnover changes. | USEFUL | NO | YES | VISUAL_INSPECTED | Context. |
| R&T Fig.10-15 | p.304 | Pool size decreases to new value after turnover change. | USEFUL | NO | YES | VISUAL_INSPECTED | Context. |
| R&T Fig.10-16 | p.305 | Erythropoietin/hematocrit delayed response. | USEFUL | YES | NO | VISUAL_INSPECTED | Later Ch.11 EPO bridge. |
| R&T Fig.10-17 | p.306 | Pharmacodynamic tolerance relationship. | USEFUL | NO | NO | VISUAL_INSPECTED | Tolerance context. |
| R&T Fig.10-18 | p.307 | Nicotine tolerance/tachyphylaxis. | USEFUL | NO | NO | VISUAL_INSPECTED | Tolerance context. |
| R&T Table 10-6 | p.309 | PK parameter changes with physiologic variables. | USEFUL | NO | NO | VISUAL_INSPECTED | Advanced context. |
| R&T Fig.10-19 | p.310 | Concentration-time profiles under physiologic changes. | USEFUL | NO | YES | VISUAL_INSPECTED | Context only. |
| R&T Fig.10-20 | p.311 | PK/PD indices: peak/MIC, AUC/MIC, time above MIC. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M6 antimicrobial PK/PD. |
| R&T Fig.10-21 | p.312 | Mouse thigh infection PK/PD index determination. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Strong empirical anchor. |
| R&T Fig.10-22 | p.313 | Infusion vs bolus antibiotic dosing comparison. | USEFUL | NO | YES | VISUAL_INSPECTED | Context. |
| R&T Fig.10-23 | p.314 | Study problem time course. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Exercise. |
| R&T Table 10-7 | p.315 | Nifedipine rectal infusion kinetics. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Study problem. |
| R&T Table 10-8 | p.316 | Droperidol IV bolus + infusion concentrations. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Study problem. |
| R&T Table 10-9 | p.316 | Rolipram dermal concentration table. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Study problem. |
| R&T Fig.10-24 | p.317 | Rolipram dermal infusion profile. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Study problem. |
| R&T Table 11-1 | p.320 | Superposition table for 200 mg q24h x 5 days. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | M4 source anchor. |
| R&T Fig.11-1 | p.321 | Sawtooth accumulation by superposition. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M3/M4 visual. |
| R&T Fig.11-2 | p.322 | Dosing frequency controls accumulation. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M3 core. |
| R&T Table 11-2 | p.324 | Phenobarbital approach to plateau. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | M3/M2 numeric anchor. |
| R&T Fig.11-3 | p.325 | Same average dose rate gives same approach time, different fluctuation. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Apex reinforcement. |
| R&T Fig.11-4 | p.327 | Loading + maintenance with doxycycline. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M7 core. |
| R&T Table 11-3 | p.328 | TI × half-life dosage regimen matrix. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | M6/M7 decision table. |
| R&T Table 11-4 | p.330 | Regimens and half-lives for amoxicillin/naproxen/piroxicam. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | 3-drug reinforcement. |
| R&T Table 11-5 | p.330 | Amount in body under regimens in Table 11-4. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Quantitative comparison. |
| R&T Fig.11-5 | p.331 | Naproxen amount-time course. | USEFUL | YES | NO | VISUAL_INSPECTED | Reinforcement. |
| R&T Fig.11-6 | p.331 | Amoxicillin amount-time course. | USEFUL | YES | NO | VISUAL_INSPECTED | Reinforcement. |
| R&T Fig.11-7 | p.332 | Piroxicam amount-time course. | USEFUL | YES | NO | VISUAL_INSPECTED | Reinforcement. |
| R&T Fig.11-8 | p.333 | Oral vs IV amount/concentration behavior. | USEFUL | NO | YES | VISUAL_INSPECTED | Extravascular context. |
| R&T Fig.11-9 | p.333 | Slow absorption effect on fluctuation. | USEFUL | NO | YES | VISUAL_INSPECTED | Extravascular context. |
| R&T Fig.11-10 | p.335 | TW-driven regimen design with loading and maintenance doses. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M8 core figure. |
| R&T Fig.11-11 | p.336 | IV vs oral profiles: same average concentration when F=1. | USEFUL | YES | YES | VISUAL_INSPECTED | Cav/AUC concept. |
| R&T Fig.11-12 | p.336 | Clobazam single-dose AUC predicts average plateau. | USEFUL | YES | NO | VISUAL_INSPECTED | Underused source anchor. |
| R&T Table 11-6 | p.337 | Relationship applicability matrix for dosing regimens. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | M4/M8 equation reliability. |
| R&T Fig.11-13 | p.338 | Morphine IR q4h vs MR q24h. | USEFUL | YES | NO | VISUAL_INSPECTED | Modified-release context. |
| R&T Fig.11-14 | p.340 | Multiple-dose regimen evaluation: AUCss, accumulation, fluctuation. | USEFUL | YES | YES | VISUAL_INSPECTED | Eq.11-23~25 bridge. |
| R&T Fig.11-15 | p.342 | PD position on Emax curve changes dosing interval acceptability. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M6 PD-driven dosing. |
| R&T Fig.11-16 | p.343 | Atorvastatin lipid response delayed weeks vs PK half-life. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | PD plateau example. |
| R&T Fig.11-17 | p.344 | Erythropoietin reticulocyte/hematocrit delay. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | PD plateau example. |
| R&T Fig.11-18 | p.345 | Onset/duration/intensity dependence. | USEFUL | NO | YES | VISUAL_INSPECTED | Context. |
| R&T Fig.11-19 | p.347 | Ceftazidime vs gentamicin dosing interval effect. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Antimicrobial PK/PD. |
| R&T Fig.11-20 | p.348 | AUC/MIC and organism resistance. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Resistance anchor. |
| R&T Fig.11-21 | p.349 | Multiple IV dose model for altered absorption/disposition. | USEFUL | NO | YES | VISUAL_INSPECTED | Context. |
| R&T Fig.11-22 | p.350 | Low extraction inhibition increases Css and t1/2. | USEFUL | YES | YES | VISUAL_INSPECTED | Altered disposition context. |
| R&T Fig.11-23 | p.351 | High extraction induction reduces F/Css without changing t1/2 materially. | USEFUL | YES | YES | VISUAL_INSPECTED | Altered disposition context. |
| R&T Fig.11-24 | p.352 | Daptomycin concentration profiles under q24h/q8h dose fractionation. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Daptomycin conclusion depends on figure/table. |
| R&T Table 11-7 | p.353 | Daptomycin PK and myopathy findings. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Draft has one comparison error. |
| R&T Tables 11-8~11-12 | p.354–358 | Study problem dosing tables. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Exercise material, not core Step 1. |

---

## Final Audit Lock

**Go/No-Go**

```text
GO: Phase 2 Source Fidelity Audit continuation and Phase 4 patching.
NO-GO: Direct HTML conversion.
NO NEED: Full Phase 1 redo.
```

**MUST_FIX before Phase 4 content lock**

```text
1. M4 Curation Map amount/concentration dimension error.
2. Daptomycin Study A same-daily-dose comparison.
3. Phenobarbital R=5.8 labeling.
4. Unsupported numbers/regulatory claims.
5. U(C) utility formula source labeling.
```

**SHOULD_FIX before final compile**

```text
1. PK13 anchor placement.
2. Clobazam Fig.11-12 context.
3. G p.25 steady-state/equilibrium nuance.
4. Evaluation-of-multiple-dose-regimen context: Eq.11-23~11-25.
5. Compression of repeated NDA/FDA language.
```

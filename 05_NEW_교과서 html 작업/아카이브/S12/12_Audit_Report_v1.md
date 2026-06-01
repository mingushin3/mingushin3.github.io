# 12_Audit Report v1 — Source Fidelity Audit

**업무 형태:** 파일 분석 / PDF 대조 감사 / 웹 검색 OFF  
**대상 세션:** Session 12 — Effect Compartment · Tolerance/Rebound · Transduction  
**입력:** `012_G_Effect Compartment 내성·Transduction(1).pdf` + `012_T_Effect Compartment 내성·Transduction(1).pdf` + `12_step1_draft_v0.md` + `S12_phase1_patch memo.md`  
**산출:** Source Fidelity Audit Report v1  
**감사 역할:** Verification only. 문장 개선/교육 강화/재작성은 수행하지 않고, Draft v0의 사실·수식·수치·예시가 PDF source에 대응되는지 판정함.

---

## Executive Verdict

**최종 판정: Conditional Go — Phase 4A 패치 필수 / HTML 직행 금지 / Phase 1 재작성 불필요**

Draft v0의 큰 구조, 즉 **C1 Effect Compartment & ke0 → C2 Hysteresis 방향 판별 → C3 Tolerance/Rebound via Moderator M → C4 Transduction chain**의 4-card 구성은 source scope와 대체로 부합한다. G&W는 §3.9 effect compartment의 ODE·동일 `tmax` 성질·Table 3.10 pitfall, §3.11 tolerance/rebound의 negative feedback 구조, §3.13 transduction chain 및 PD13/PD20/PD21/PD35 case anchors를 제공하고, R&T는 time delay/hysteresis, effect compartment collapse, systems-in-flux, rate-limiting response 및 succinylcholine duration logic을 제공한다.

그러나 Draft v0에는 **case label 오류**, **식별가능성 가정의 과잉 물리화**, **drug/example 수치 혼합**, **규제·NONMEM·공학 비유의 source 밖 확장**이 섞여 있다. 특히 다음 항목은 mandatory correction이다.

1. **G&W §3.9.7 Table 3.10 link-model pitfall을 “PD13”이라고 부른 오류**: Table 3.10은 turnover-generated data를 effect compartment model로 잘못 fit한 pitfall 예시이며, Figure 3.59는 Case Study PD12 data라고 명시된다. PD13은 repeated IV infusion tolerance/rebound case study이다.
2. **`k1e = ke0` 설명 오류**: G&W는 identifiability 문제 때문에 `k1e = ke0` 가정을 둔다고 설명한다. Draft의 “물리적 질량보존/정합성 때문에 강제”라는 표현은 source보다 강하다.
3. **succinylcholine과 d-tubocurarine 수치 혼합**: G&W Table 3.9의 `t1/2,ke0 = 4 min`은 d-tubocurarine/vecuronium muscle paralysis 예시이고, R&T의 succinylcholine 예시는 `0.5 mg/kg IV`, `T50 ≈ 6 min`, `k≈0.2 min^-1`, half-life about 4 min, response decline about `22%/min`이다.
4. **hysteresis 방향 = 모델 선택 결정**: 방향은 강력한 diagnostic clue이나, 단독 결정 규칙은 아니다. 최종 모델 선택은 `tmax` dose invariance/peak shift, repeated-dose pattern, rising-falling limb data, metabolite/target information, model comparison을 함께 보아야 한다.
5. **NDA Deficiency Letter, FDA reviewer, ICH E9(R1), NONMEM bootstrap/SIR/SAEM, BIC/AIC/ΔOFV 등**: 교과서 직접 내용이 아니라 실무 해석/구현 번역이다. 유지하려면 `[교과서 외 실무 해석]`, `[구현 번역]`으로 분리해야 한다.
6. **Transduction의 Erlang/gamma PDF/Bode plot/tanks-in-series/RC delay line/do-loop 비유**: 학습적으로 유용할 수 있으나 원문 직접 내용은 아니다. G&W는 chain of events/compartments, `1/t = kout`, transit time, number of transduction steps 및 PD35 WRSS 비교를 제시한다.

---

## T1: Equation/Numerical Audit

| Item | Draft v0 Expression | PDF Source | Classification | Correction |
|---|---|---|---|---|
| Source scope | G&W §3.9, §3.11, §3.13 + PD13/PD20/PD21/PD35; R&T Ch.8 | G&W p.261–272, 284–302, 323–325, 805–809, 836–848, 910–914; R&T p.233–264 | MATCH | 유지. Draft가 §3.10, §3.12, §3.14를 제외한 것은 scope control 측면에서 적절. |
| Effect compartment definition | Plasma C와 biophase Ce를 first-order constant `ke0`로 연결하는 hypothetical link model | G&W p.262–263, Fig.3.52–3.53 | MATCH | 유지. |
| `Ce` not directly measured | `Ce`는 직접 측정되지 않고 response-time course에서 간접 유도 | G&W p.263 | MATCH | 유지. |
| Need rising/falling response-time data | steady-state dynamics alone insufficient; rise/fall response over time 필요 | G&W p.263 | MATCH | 유지. |
| `ke0` + `Emax, EC50, n` estimated | Link model estimates `ke0` and PD parameters | G&W p.263, p.268 Eq.3:141 | MATCH | 유지. |
| Same `tmax` with increasing doses | Linear PK에서 effect compartment model predicts same `tmax` for increasing doses | G&W p.264 | MATCH | 유지. 단 “정당성을 결정한다”는 표현은 “useful discriminatory tool”로 낮출 것. |
| One-compartment plasma profile | `Ap = D·e^{-Kt}` | G&W p.264 Eq.3:126 | MATCH | 유지. |
| Effect compartment amount ODE | `dAe/dt = k1e·Ap - ke0·Ae` | G&W p.264 Eq.3:127 | MATCH | 유지. |
| Integrated `Ae` | `Ae = k1e·D/(ke0-K)[e^{-Kt}-e^{-ke0t}]` | G&W p.264 Eq.3:128 | MATCH | 유지. |
| `Ce` expression before simplification | `Ce = k1e·D/[Ve(ke0-K)] [e^{-Kt}-e^{-ke0t}]` | G&W p.264 Eq.3:129 | MATCH | 유지. |
| Equilibrium rates | `k1e·C·Vc = ke0·Ce·Ve` | G&W p.265 Eq.3:131 | MATCH | 유지. |
| `Kp = Ce/C` and `Ve` rearrangement | `Ve = k1e·Vc/(ke0·Kp)` | G&W p.265 Eq.3:132 | MATCH | 유지. |
| `k1e = ke0` assumption | Draft: “identifiability 때문이 아니라 물리적 정합성/질량보존 때문에 강제” | G&W p.263, p.265: due to identifiability problems, all rate constants are assumed equal; partitioning may make `Ce` different from C at steady state | ERROR | 반드시 수정: `k1e = ke0`는 식별가능성과 모델 단순화를 위한 표준 가정. 모든 생리학적 상황에서 물리적으로 강제되는 등식이 아님. |
| Simplified bolus `Ce` | `Ce = ke0·D/[Vc(ke0-K)] [e^{-Kt}-e^{-ke0t}]` | G&W p.265 Eq.3:134 | MATCH | 유지. 단 `Kp=1`/no partitioning 가정 명시. |
| Constant Cp simulation | Larger `ke0` → shorter time to equilibrium; `Ce=Cp` at steady state if `Kp=1` | G&W p.266 Fig.3.54 | MATCH | 유지. |
| Two-compartment formulas | Eq.3:135–3:140 included conceptually | G&W p.266–267 | MATCH_AS_CONTEXT | Draft가 세부식을 모두 카드화하지 않은 것은 정당. |
| Hill integration | `E = Emax·Ce^n/(EC50^n+Ce^n)` after substituting `Ce` | G&W p.268 Eq.3:141 | MATCH | 유지. |
| Convolution form | `E = ke0*C*e^{-ke0t}` and `dCe/dt = ke0(C-Ce)` style | G&W p.268–269 Eq.3:142–3:143 | MATCH | 유지. 단 notation은 원문과 일치하도록 `Ce` ODE로 표기. |
| ODE works for nonlinear/table plasma kinetics | `C` in Eq.3:143 can be linear, nonlinear, or table function | G&W p.269 | MATCH | 유지. |
| `t1/2,ke0 = ln(2)/ke0` | Effect compartment equilibration half-life | G&W p.269 §3.9.6 | MATCH | 유지. |
| Table 3.9 values | Terbutaline FEV-1 7.5 min; theophylline 11; d-tubocurarine 4; fentanyl 6.4; quinidine 8 etc. | G&W p.269 Table 3.9 | MATCH | 유지. |
| “분 단위가 일반적” | Distribution-rate-limited response equilibration half-lives generally order of minutes | G&W p.269 | MATCH | 유지. |
| Succinylcholine `t1/2,ke0 = 4 min` | Draft associates 4 min `t1/2,ke0` with succinylcholine | G&W Table 3.9; R&T p.249, p.255–256 | ERROR | 4 min `t1/2,ke0` in Table 3.9 is d-tubocurarine/vecuronium muscle paralysis. Succinylcholine R&T example: 0.5 mg/kg IV, T50≈6 min, k≈0.2 min^-1, half-life about 4 min, 80–20% decline about 22%/min. |
| Simulation parameters Fig.3.56–3.58 | K=0.693 h^-1, infusion 1 h, k0=20, V=1; varied `ke0`, `n`, `EC50`, `Emax` | G&W p.270–271 Fig.3.56–3.58, Eq.3:145–3:147 | MATCH_AS_CONTEXT | 유지 가능. Draft에서 세부 수치를 모두 넣지 않아도 됨. |
| Link pitfall EC50 values | Draft: “PD13 Table 3.10 EC50 0.681, 4.85, 0.941” | G&W p.271 Table 3.10; §3.9.7; Fig.3.59 says Case Study PD12 data | ERROR | `PD13` label 삭제. `G&W §3.9.7 Table 3.10 link-model pitfall`로 수정. |
| Table 3.10 values | Simultaneous `ke0=0.0075`, `Emax=55.8`, `EC50=0.206`, `n=0.91`; Dose 1 `EC50=0.681`; Dose 10 `EC50=4.85`; Dose 100 `EC50=0.941`; Original Trn `kout=0.024`, `Emax=0.532`, `EC50=0.164`, `n=1.47` | G&W p.271 Table 3.10 | MATCH | 수치 자체는 일치. 단 case label만 수정. |
| “EC50가 7배 분기” | `4.85/0.681 ≈ 7.1` | 계산상 source-derived | MATCH_AS_DERIVED | 유지 가능. 단 source-derived 계산으로 표시. |
| “NDA Deficiency Letter 직결” | Draft critical blow/regulatory narrative | G&W: biologically implausible situation; no regulatory letter | NOT_IN_SOURCE | `[교과서 외 실무 해석]`으로 분리 또는 삭제. |
| Tolerance definition | Progressive reduction in response over extended exposure; desensitization/tachyphylaxis/tolerance | G&W p.284–286 | MATCH | 유지. |
| Nitroglycerin hat TDS | Weekend rebound/angina-like symptoms; hat sweatbands with nitroglycerine | G&W p.285 Fig.3.71 | MATCH | 유지. 단 “심근경색” 등 임상 재난 서사는 source 밖. |
| Tolerance mechanisms | receptor down-regulation, internalization, transduction changes, cofactor depletion, mRNA, antibodies, enzyme induction | G&W p.285–286 Fig.3.72 | MATCH | 유지. |
| Table 3.12 approaches | systems analysis, attenuation, tolerance compartment, hypothetical metabolite antagonist, counteracting mechanisms, feedback/rebound, indirect response | G&W p.287 Table 3.12 | MATCH | 유지. |
| Colburn-Eldon time attenuation | `EC50(t)` or `Emax(t)` attenuation; acute dosing, no rebound/mechanistic base | G&W p.291–292 Fig.3.74; Table 3.12 | MATCH_AS_CONTEXT | 유지 가능. |
| Antagonistic metabolite | Hypothetical metabolite antagonist; no rebound; empirical | G&W p.292–293 Fig.3.76; Table 3.12 | MATCH_AS_CONTEXT | 유지. |
| Tolerance compartment | Mechanism compartment alters potency; can handle various tolerance patterns | G&W p.293–294 Fig.3.77 | MATCH_AS_CONTEXT | 유지. |
| Counteracting mechanisms | Models for counteracting effect, nicotine example | G&W p.294–295 Fig.3.78 | MATCH_AS_CONTEXT | 유지. |
| Feedback/rebound | Overshoot, shoulder, rebound; AUCE and AUCR asymmetric | G&W p.297–298 Fig.3.82 | MATCH | 유지. |
| Simple negative feedback | Eq.3:187–3:192; set point feedback; no overshoot/rebound unlike moderator model | G&W p.296–297 | MATCH_AS_CONTEXT | 유지. |
| Moderator ODE | `dR/dt = kin·S(C) - kout·M`; `dM/dt = ktol·R - ktol·M` | G&W p.299 Eq.3:193–3:194 | MATCH | 유지. |
| Moderator steady state | `R0 = kin/kout`; `Rss = kin/kout·S(C)`; `Rmax = kin/kout[1+Emax]` | G&W p.299–300 Eq.3:198–3:202 | MATCH | 유지. |
| `ktol` governs both production/loss of M | Draft says PD13 simplification | G&W p.299 | MATCH | 유지 with caveat: may not always be the case. |
| Moderator + level of response | Second-order polynomial form Eq.3:205–3:218 | G&W p.301–302 | MATCH | 유지. |
| “2차 다항식 정상상태” | Eq.3:212–3:216 | MATCH | 유지. |
| PD13 objectives | Apply turnover model to multiple IV infusion response data, different tolerance structures, discriminate models | G&W p.805 | MATCH | 유지. |
| PD13 Model I equation | Draft sometimes writes Model I loss term with `M` | G&W p.806 Eq.13:1: ordinary turnover stimulation of kout/no feedback; variable notation in OCR may appear as M/R, but concept is no feedback | RESTORED / CHECK | If Draft uses `M` as loss driver in Model I, revise to ordinary turnover/no feedback to avoid confusing with Moderator M. |
| PD13 Model II | Negative feedback model; `dR/dt=kin·S(C)-kout·M`, `dM/dt=ktol·R-ktol·M` | G&W p.806 Eq.13:3–13:4 | MATCH | 유지. |
| PD13 Model III | Pool/precursor equations | G&W p.807 Eq.13:5–13:7 | MATCH | 유지. |
| PD13 Table 13.1 | Model I AIC −39.0 WRSS 0.33; Model II AIC −97.5 WRSS 0.083; Model III AIC −43.5 WRSS 0.28; `ktol=4.2`, `kout=2.9` for Model II | G&W p.808 Table 13.1 | MATCH | 유지. |
| PD13 “Model II 압도” | Negative feedback model successfully fit; ktol > kout allows observing tolerance | G&W p.808 | MATCH | 유지. |
| PD13 second trough differs | trough value not same during second infusion; slight rebound | G&W p.808 | MATCH | 유지. |
| PD13 “complete inhibition possible” | Almost complete inhibition of response seen | G&W p.809 | MATCH | 유지. |
| Transduction chain | Chain of events/compartments between receptor-ligand coupling and observed response | G&W p.323 Fig.3.98 | MATCH | 유지. |
| `1/t = kout` | rate constant in catenary model approximated to `1/t = kout`; `kout=1/τ` | G&W p.323 Fig.3.98; p.912 | MATCH | 유지. |
| PD35 15–20 h onset delay | ordinary indirect response cannot mimic 15–20 h delay | G&W p.323 Fig.3.99 | MATCH | 유지. |
| Transduction ODEs | Eq.3:257–3:260 and PD35 Eq.35:5–35:6 | G&W p.324–325, p.911–912 | MATCH | 유지. |
| “single indirect response 절대 불가” | Source: ordinary indirect response would not capture that delay; “cannot be mimicked” in Fig.3.99 caption | MATCH with tone caveat | “절대”는 원문 강도와 대체로 부합하나, 모델링 문맥에서는 “ordinary indirect response alone cannot capture the observed 15–20 h onset delay”로 표현 권장. |
| Gamma/Erlang/PFR/Bode/RC analogies | Draft structural analogies | Not in G&W/R&T | NOT_IN_SOURCE | `[교과서 외 구조적 비유]`로 분리. |
| PD35 C0/K values | `C0=1.05 nmol/L`, `K=0.0228 h^-1`, `t1/2 about 30 h`; intermediate 4x, high 16x | G&W p.911 Eq.35:1–35:3 | MATCH | 유지. |
| PD35 initial EC50 | `16·1.05·e^{-0.0228·216} ≈ 0.12` | G&W p.912 Eq.35:7 | MATCH | 유지. |
| PD35 Emax initial | Baseline 20, peak 110, Δ=90, `Emax≈4.5` | G&W p.912 Eq.35:8 | MATCH | 유지. |
| PD35 slope/kin/tau | slope `(88-39)/(48-24)≈2`, `kin≈0.4`, τ≈4 h for 3 compartments, `kout=0.25 h^-1` | G&W p.912 Eq.35:9 | MATCH | 유지. |
| PD35 Table 35.1 WRSS | n=1 1319; n=2 789; n=3 642; n=4 632; n=5 682 | G&W p.914 Table 35.1 | MATCH | 유지. |
| PD35 “n=3 practical/parsimony” | Source: original 3-step model; 4 steps improves slightly; 5 steps worsens | G&W p.913–914 | MATCH_AS_INTERPRETATION | 유지 가능. 정확히는 “four transduction compartment model including receptor/three transduction steps would suffice”; n=4 step model WRSS slightly lower but added step. |
| PD20 values | IV bolus 45 µg/kg; C0=45.0; V=1 L/kg; K=0.50 h^-1; response 80 h; initial Emax 3 or 4–5; EC50 1.5 µg/L; ke0 0.1 h^-1 | G&W p.837–838 | MATCH | 유지. |
| PD20 simulated doses | 5, 45, 225 µg/kg; same tmax; linear decline below EC50/IC50 | G&W p.839 Fig.20.2 | MATCH | 유지. |
| PD21 values | rabbit oral 1 and 2 µmol/kg; ke0 0.025, kout 0.031, koff 0.018 min^-1; half-lives 28, 22, 39 min; potencies 42, 40, 48 nM | G&W p.840–845, Table 21.1 | MATCH | 유지 if included. |
| Hysteresis direction quote attributed to R&T p.296/G&W | Draft quotes clockwise/anti-clockwise text | G&W p.295 around Fig.3.80 more likely; not R&T p.296 (R&T page numbering differs) | ERROR_CITATION | Correct source attribution: G&W §3.11.7/Fig.3.80 region, not R&T Ch.8 p.296. R&T supports time-delay/hysteresis diagnosis with digoxin/naproxen. |
| R&T Chapter objective | Time always needs to be considered | R&T p.233 | MATCH | 유지. |
| Digoxin | 1 mg IV; left ventricular ejection-time index rises while plasma falls first 4 h; wait ~6 h | R&T p.234 Fig.8-1 | MATCH | 유지. |
| Naproxen | 500 mg oral; dental pain; counterclockwise hysteresis; response follows fall after ~5 h | R&T p.234–235 Fig.8-2 | MATCH | 유지. |
| R&T effect compartment collapse | Effect compartment links plasma with response; varying distribution rate constant removes hysteresis in naproxen | R&T p.245–246 Fig.8-13–8-14 | MATCH | 유지. |
| R&T indirect response four cases | Increase/decrease formation or elimination of biomarker | R&T p.241 | MATCH | 유지. |
| Ibuprofen | 6 mg/kg oral in febrile children; large hysteresis; heat-control mechanism | R&T p.241 Fig.8-9 | MATCH | 유지. |
| Warfarin | 1.5 mg/kg oral sodium warfarin; prothrombin complex turnover; response delayed 1–2 days | R&T p.242, p.247 Fig.8-10, 8-15 | MATCH | 유지. |
| Eq.8-7 synthesis estimate | `Rsyn = (A2-A1)/Δt + kt·(A1+A2)/2` | R&T p.247 Eq.8-7 | MATCH | 유지 if used. |
| Succinylcholine decline | 0.5 mg/kg IV; onset delay ~1 min; elimination half-life 3.5 min; decline 22%/min between 80–20%; T50 dose-duration k=0.2 min^-1, half-life about 4 min | R&T p.249–256 Fig.8-18, 8-24 | MATCH | Use for duration/rate-limiting example, not as G&W Table 3.9 `ke0`. |
| NONMEM/FOCE/SAEM/bootstrap/SIR | Draft boss dilemma | Not in PDFs | NOT_IN_SOURCE | `[실무 구현 번역]` or remove from source-fidelity content. |
| Reviewer/FDA/ICH E9/R1 | Draft regulatory blow | Not in PDFs | NOT_IN_SOURCE | `[교과서 외 규제 해석]`; do not present as textbook fact. |

---

## T2: Examples & Data Audit

| Item | Draft v0 Status | PDF Location | Classification | Importance | Action |
|---|---|---|---|---|---|
| G&W Fig.3.51 direct vs delayed response hysteresis | Included in C1/C2 | G&W p.261–262 | INCLUDED_CORRECT | HIGH | 유지. |
| G&W Fig.3.52 link model PK→biophase→response | Included | G&W p.262 | INCLUDED_CORRECT | HIGH | 유지. |
| G&W Fig.3.53 effect compartment schematic | Included | G&W p.263 | INCLUDED_CORRECT | HIGH | 유지; `Ce` indirect and rise/fall data requirement 강조. |
| G&W Table 3.8 one-compartment link equations | Mostly context | G&W p.265 | INCLUDED_AS_CONTEXT | MEDIUM | 세부식 전체는 카드에 과도하므로 context 충분. |
| G&W Fig.3.54 ke0 simulation | Included | G&W p.266 | INCLUDED_CORRECT | HIGH | 유지. |
| G&W Table 3.9 t1/2ke0 values | Included but one misuse | G&W p.269 | INCLUDED_ERROR_PARTIAL | HIGH | d-tubocurarine/vecuronium 4 min과 succinylcholine 분리. |
| G&W Fig.3.56–3.58 simulations | Partly included | G&W p.270–271 | INCLUDED_AS_CONTEXT | MEDIUM | ke0/n/EC50/Emax sensitivity simulation으로 1–2문장 유지. |
| G&W §3.9.7 Table 3.10 pitfall | Included but mislabeled PD13 | G&W p.271 | INCLUDED_ERROR | HIGH | `PD13` label 제거, `§3.9.7 Table 3.10 / PD12 data`로 수정. |
| G&W §3.10 | Explicitly excluded | G&W p.272–284 | OMITTED_JUSTIFIABLE | LOW | Scope 밖. |
| G&W Fig.3.71 nitroglycerine tolerance/rebound, hat TDS | Included | G&W p.285 | INCLUDED_CORRECT | HIGH | 유지. |
| G&W Fig.3.72 tolerance mechanisms | Included | G&W p.286 | INCLUDED_CORRECT | MEDIUM | 유지. |
| G&W Table 3.12 tolerance approaches | Included | G&W p.287 | INCLUDED_CORRECT | HIGH | 유지. |
| Systems analysis Fig.3.73 | Context | G&W p.288 | INCLUDED_AS_CONTEXT | LOW | 충분. |
| Time-dependent attenuation Fig.3.74–3.75 | Context | G&W p.291–292 | INCLUDED_AS_CONTEXT | MEDIUM | 유지; source밖 수식이면 확인. |
| Antagonistic metabolite Fig.3.76 | Context | G&W p.292–293 | INCLUDED_AS_CONTEXT | MEDIUM | 유지. |
| Tolerance compartment Fig.3.77 | Context | G&W p.293–294 | INCLUDED_AS_CONTEXT | MEDIUM | 유지. |
| Counteracting mechanisms Fig.3.78 | Context | G&W p.294–295 | INCLUDED_AS_CONTEXT | MEDIUM | 유지. |
| Feedback/rebound Fig.3.79–3.82 | Included | G&W p.295–298 | INCLUDED_CORRECT | HIGH | 유지. |
| Biomarker Y/test compound X Fig.3.83 | Mostly omitted | G&W p.298 | OMITTED_JUSTIFIABLE | LOW | PD14로 넘어가는 사례이므로 필수 아님. |
| Negative feedback via moderator Eq.3:193–3:204 | Included | G&W p.299–300 | INCLUDED_CORRECT | HIGH | 유지. |
| Negative feedback + level of response Eq.3:205–3:218 | Included | G&W p.301–302 | INCLUDED_CORRECT | MEDIUM | 유지; 2차 다항식 anchor로 좋음. |
| Fig.3.84 simulations | Mostly omitted | G&W p.302+ | OMITTED_JUSTIFIABLE | MEDIUM | Scope page가 시작만 포함. Phase 4에서 필요 시 context. |
| G&W §3.13 Fig.3.98–3.101 transduction | Included | G&W p.323–325 | INCLUDED_CORRECT | HIGH | 유지. |
| PD13 repeated IV infusion | Included | G&W p.805–809 | INCLUDED_CORRECT | HIGH | 유지 as tolerance/rebound case. |
| PD13 Table 13.1 | Included | G&W p.808 | INCLUDED_CORRECT | HIGH | 유지. |
| PD20 analgesic IV bolus | Included | G&W p.836–839 | INCLUDED_CORRECT | MEDIUM | 유지. |
| PD21 rabbit antagonist X | Included | G&W p.840–845 | INCLUDED_CORRECT | MEDIUM | 유지 as ke0/kout/koff comparison; 너무 길면 context. |
| PD35 human transduction data | Included | G&W p.910–914 | INCLUDED_CORRECT | HIGH | 유지. |
| PD35 Table 35.1 | Included | G&W p.914 | INCLUDED_CORRECT | HIGH | 유지. |
| R&T objectives | Partly reflected | R&T p.233 | INCLUDED_AS_CONTEXT | MEDIUM | “time always matters” author message 보강. |
| Digoxin | Included | R&T p.234 Fig.8-1 | INCLUDED_CORRECT | HIGH | 유지. |
| Naproxen | Included | R&T p.234–235 Fig.8-2 | INCLUDED_CORRECT | HIGH | 유지. |
| R&T Fig.8-3 downstream compartments | Included in C2/C4 logic | R&T p.236–237 | INCLUDED_CORRECT | MEDIUM | 유지. |
| R&T Fig.8-13–8-14 effect compartment | Included | R&T p.245–246 | INCLUDED_CORRECT | HIGH | 유지. |
| Ibuprofen fever | Included | R&T p.241 Fig.8-9 | INCLUDED_CORRECT | MEDIUM | 유지. |
| Warfarin/prothrombin | Included as indirect response | R&T p.242, p.247 | INCLUDED_CORRECT | MEDIUM | 유지. |
| Succinylcholine | Included but mixed with d-tubocurarine | R&T p.249, p.255–256 | INCLUDED_ERROR_PARTIAL | HIGH | 수치 anchor 분리. |
| Acenocoumarol/phenprocoumon | Mentioned in completion block | R&T p.243–244 Fig.8-11 | INCLUDED_CORRECT_IF_USED | LOW | Session 12 핵심은 아님. |
| Aspirin/omeprazole/paclitaxel | Possibly carried from previous Session 10 | R&T p.251–253 | OPTIONAL | LOW | Session 12에서는 과도하면 삭제 가능. |
| Study problems / Tables 8-1, 8-2 | Mostly omitted | R&T p.260–264 | OMITTED_JUSTIFIABLE | LOW | 세션 핵심 아님. |

---

## T3: Author Key Messages

| Message | PDF Location | In Draft v0? | Status |
|---|---|---|---|
| Time delay between effect and plasma concentration produces hysteresis in response-vs-concentration plots. | G&W p.261–262; R&T p.234–235 | Present | MATCH |
| Effect compartment model covers distributional delays where transport between plasma and biophase is first-order rate-limiting. | G&W p.262 | Present | MATCH |
| `Ce` cannot be directly measured; non-steady-state rise/fall response-time data and a plasma kinetic model are required. | G&W p.263 | Present but could be stronger | SHOULD_FIX |
| Due to identifiability problems, additional rate constants are assumed equal (`k1e = ke0`); partitioning may violate `Ce=C` at steady state. | G&W p.263 | Partly contradicted | MUST_FIX |
| Linear PK effect compartment predicts same `tmax` with increasing doses; this helps discriminate link vs turnover response models. | G&W p.264 | Present | MATCH with tone reduction |
| Distribution-rate-limited response equilibration half-lives are generally minutes. | G&W p.269 Table 3.9 | Present | MATCH with correction for succinylcholine |
| Effect compartment model has severe limitations when applied to turnover processes; dose-dependent EC50/Emax/n is biologically implausible. | G&W p.271–272 | Present but mislabeled | MUST_FIX |
| Tolerance/rebound can arise from endogenous counter-regulation; causes are diverse and often not fully understood. | G&W p.284–286 | Present | MATCH |
| Negative feedback via moderator can generate overshoot, shoulder, rebound, and asymmetric AUCE/AUCR. | G&W p.297–300 | Present | MATCH |
| PD13 demonstrates a recommended modeling sequence: ordinary turnover model first, then tolerance models; Model II fits best. | G&W p.805–809 | Present | MATCH |
| Transduction models represent chains of events/compartments between receptor-ligand coupling and observed response. | G&W p.323–325 | Present | MATCH |
| PD35 shows ordinary indirect response cannot mimic the 15–20 h onset delay; transit chain is needed. | G&W p.323, p.910–914 | Present | MATCH |
| In practice, time always needs to be considered when integrating exposure and response. | R&T p.233 | Present | MATCH |
| Hysteresis is a useful diagnostic of temporal features, not proof of a single mechanism. | R&T p.234–235; G&W p.262 | Present but over-stated as deterministic | MUST_FIX |
| Response can be PK-rate-limited or PD-rate-limited; the slower process governs decline/duration. | R&T p.237–256 | Present | MATCH |
| Duration can be proportional to log dose under assumptions; succinylcholine illustrates dose-duration relation. | R&T p.254–256 | Present | MATCH with drug/example separation |

---

## T4: Priority Summary (sorted)

| # | Item | Priority | Rationale |
|---|---|---|---|
| 1 | Table 3.10 link-model pitfall을 “PD13”이라고 지칭 | MUST_FIX | G&W §3.9.7 Table 3.10의 pitfall이며 Figure 3.59는 PD12 data. PD13은 tolerance/rebound repeated infusion case. |
| 2 | `k1e = ke0`를 물리적 필연/질량보존 강제라고 설명 | MUST_FIX | 원문은 identifiability problem 때문에 rate constants를 같게 둔다고 설명. Partitioning이 있으면 `Ce`와 C가 steady state에서도 다를 수 있음. |
| 3 | succinylcholine과 d-tubocurarine/vecuronium 수치 혼합 | MUST_FIX | G&W Table 3.9의 4 min `t1/2,ke0`는 d-tubocurarine/vecuronium. R&T succinylcholine은 별도 dose-duration example. |
| 4 | Hysteresis 방향이 모델 선택을 “결정”한다고 표현 | MUST_FIX | 방향은 diagnostic clue. 최종 선택은 `tmax`, peak shift, repeated-dose, metabolite/target data, model comparison 필요. |
| 5 | NDA Deficiency Letter/FDA/ICH E9(R1)/reviewer/6개월 지연 서사 | MUST_FIX | PDF 직접 근거 없음. `[교과서 외 실무 해석]`으로 분리해야 함. |
| 6 | NONMEM, FOCE/SAEM, bootstrap/SIR, OMEGA/MU-referencing 구현 지시 | MUST_FIX | 교재 source 밖 구현 번역. HTML 본문에서 교과서 사실처럼 배치 금지. |
| 7 | Erlang/gamma/Bode/tanks-in-series/RC delay line 등 transduction 비유 | SHOULD_FIX | 유용하나 NOT_IN_SOURCE. `[구조적 비유 — 교과서 외 확장]` 라벨 필요. |
| 8 | “Link 모델은 분포 지연을 포착하는 유일한 도구” | SHOULD_FIX | G&W는 effect compartment model을 distributional delay model로 설명하지만, 원인에는 active metabolites, arteriovenous differences, receptor upregulation, slow on/off 등도 포함. “유일한”은 과강. |
| 9 | “단일 ODE로는 rebound 후 baseline 회귀를 만들 수 없다” | SHOULD_FIX | Moderator M의 필요성을 설명하는 해석으로 가능하지만, 원문 직접 문장보다 강함. 모델 가족 제한 하의 statement로 낮출 것. |
| 10 | PD35 “n=3 최적” 표현 | SHOULD_FIX | Table 35.1에서는 n=4 WRSS가 더 낮으나, original 3-step model이 practical sufficiency. “n=3 practical/parsimony; n=4 slight improvement”로 표현. |
| 11 | PD21 `ke0/kout/koff` 수치적 근접성 → TMDD 혼동 서사 | SHOULD_FIX | 수치는 source-supported이나 TMDD 결론은 외부 확장. |
| 12 | R&T/G&W citation attribution for clockwise/anti-clockwise quote | SHOULD_FIX | Draft의 “R&T p.296의 G&W 인용”은 source attribution 혼동. G&W §3.11/Fig.3.80 근처로 바로잡기. |
| 13 | PD20 single-dose low EC50 precision | OPTIONAL | Source-supported; effect compartment card의 limitation으로 유용. |
| 14 | Table 3.8/3.9 full equation inventory | OPTIONAL | Phase 4에서 너무 과도하면 축약 가능. |
| 15 | R&T study problems | OPTIONAL | Step 1 concept cards에서는 생략 정당. |
| 16 | §3.10, §3.12, §3.14를 이번 세션에 새로 삽입 | REJECT | Scope creep. Draft의 제외 처리 유지. |

---

## T5: Coverage Audit

### T5-A. G&W Structural Elements

| PDF Element | Type | PDF Location | Step 1 Status | Omission Verdict | Required Action |
|---|---|---|---|---|---|
| MIC carryover Eq.3:123–3:125 | Preceding section tail | p.261 | OMITTED_JUSTIFIABLE | Out of scope | No action. |
| 3.9 Effect Compartment (Link) Models | H1 | p.261–272 | INCLUDED_AS_MUST | — | Keep. |
| 3.9.1 Background | H2 | p.261–264 | INCLUDED_AS_MUST | — | Keep. |
| Fig.3.51 direct vs delayed response/hysteresis | Figure | p.262 | INCLUDED_AS_MUST | — | View recommended. |
| Fig.3.52 PK-link-PD schematic | Figure | p.262 | INCLUDED_AS_MUST | — | View recommended. |
| Fig.3.53 effect compartment schematic | Figure | p.263 | INCLUDED_AS_MUST | — | View recommended. |
| Identifiability and `k1e=ke0` statement | Author key message | p.263 | INCLUDED_WITH_ERROR | MISSING_AUTHOR_MSG if not fixed | Must correct from physical necessity to identifiability assumption. |
| Same `tmax` with increasing doses | Author key message | p.264 | INCLUDED_AS_MUST | — | Keep, with toned wording. |
| 3.9.2 One-compartment models Eq.3:126–3:134 | Equations | p.264–265 | INCLUDED_AS_MUST | — | Keep core equations only. |
| Table 3.8 one-compartment link equations | Table | p.265 | INCLUDED_AS_CONTEXT | — | Optional full table. |
| Fig.3.54 effect of ke0 | Figure | p.266 | INCLUDED_AS_MUST | — | View recommended. |
| 3.9.3 Two-compartment models Eq.3:135–3:140 | Equations | p.266–267 | INCLUDED_AS_CONTEXT | OMITTED_JUSTIFIABLE | Context only sufficient. |
| 3.9.4 Integration into Hill Eq.3:141 | H2/equation | p.268 | INCLUDED_AS_MUST | — | Keep. |
| Fig.3.55 observed/predicted response | Figure | p.268 | INCLUDED_AS_CONTEXT | — | Useful. |
| 3.9.5 Alternative parameterizations Eq.3:142–3:144 | H2/equations | p.268–269 | INCLUDED_AS_MUST | — | Keep ODE form. |
| 3.9.6 Literature examples and simulations | H2 | p.269–271 | INCLUDED_AS_CONTEXT | — | Keep Table 3.9 and key simulations. |
| Table 3.9 response equilibration half-lives | Table | p.269 | INCLUDED_AS_MUST_WITH_ERROR | MISSING_EXAMPLE if uncorrected | Drug-specific correction required. |
| Fig.3.56–3.58 simulations | Figures | p.270–271 | INCLUDED_AS_CONTEXT | — | Optional. |
| 3.9.7 Problems and pitfalls | H2 | p.271–272 | INCLUDED_AS_MUST_WITH_ERROR | MISSING_EXAMPLE if uncorrected | Correct Table 3.10 label. |
| Fig.3.59 turnover vs link fit | Figure | p.271 | INCLUDED_AS_MUST | — | View recommended. |
| Table 3.10 implausible parameter estimates | Table | p.271 | INCLUDED_AS_MUST_WITH_ERROR | MISSING_EXAMPLE if uncorrected | Rename as §3.9.7/Table 3.10 pitfall, not PD13. |
| 3.10 Dose-Response-Time Models | H1 | p.272–284 | OMITTED_JUSTIFIABLE | Scope excluded | Do not add. |
| 3.11 Tolerance and Rebound Models | H1 | p.284–302 | INCLUDED_AS_MUST | — | Keep. |
| 3.11.1 Background | H2 | p.284–287 | INCLUDED_AS_MUST | — | Keep. |
| Fig.3.71 nitroglycerine exposure/rebound | Figure | p.285 | INCLUDED_AS_MUST | — | View useful. |
| Fig.3.72 mechanisms of tolerance | Figure | p.286 | INCLUDED_AS_CONTEXT | — | Useful. |
| Table 3.12 approaches to modeling tolerance/rebound | Table | p.287 | INCLUDED_AS_CONTEXT | — | Keep as map. |
| 3.11.2 Systems analysis Fig.3.73 | H2/figure | p.288 | INCLUDED_AS_CONTEXT | — | Sufficient. |
| 3.11.3 Time-dependent attenuation Eq.3:170–3:173 Fig.3.74–3.75 | H2/equations/figures | p.291–292 | INCLUDED_AS_CONTEXT | — | Sufficient. |
| 3.11.4 Antagonistic metabolite model Eq.3:174–3:178 Fig.3.76 | H2/equations/figure | p.292–293 | INCLUDED_AS_CONTEXT | — | Sufficient. |
| 3.11.5 Tolerance compartment Eq.3:179–3:181 Fig.3.77 | H2/equations/figure | p.293–294 | INCLUDED_AS_CONTEXT | — | Sufficient. |
| 3.11.6 Counteracting mechanisms Eq.3:182–3:186 Fig.3.78 | H2/equations/figure | p.294–295 | INCLUDED_AS_CONTEXT | — | Sufficient. |
| 3.11.7 Feedback and rebound Fig.3.79–3.81 | H2/figures | p.295–296 | INCLUDED_AS_MUST | — | Keep. |
| 3.11.8 Simple negative feedback Eq.3:187–3:192 | H2/equations | p.296–297 | INCLUDED_AS_CONTEXT | — | Sufficient. |
| 3.11.9 Negative feedback via moderator Eq.3:193–3:204 | H2/equations | p.297–300 | INCLUDED_AS_MUST | — | Keep. |
| Fig.3.82 response/rebound asymmetry | Figure | p.298 | INCLUDED_AS_MUST | — | View useful. |
| Fig.3.83 biomarker Y/test compound X | Figure | p.298 | OMITTED_JUSTIFIABLE | Low priority | No action unless Phase 4 wants another example. |
| 3.11.10 Moderator + level of response Eq.3:205–3:218 | H2/equations | p.301–302 | INCLUDED_AS_MUST | — | Keep in compact form. |
| 3.11.11 Simulation of negative feedback | H2 | p.302 onward | INCLUDED_AS_CONTEXT/OMITTED_PARTIAL | Low/medium | Source pages truncated shortly after heading; optional. |
| 3.13 Transduction Models | H1 | p.323–325 | INCLUDED_AS_MUST | — | Keep. |
| Fig.3.98 receptor transduction model | Figure | p.323 | INCLUDED_AS_MUST | — | View recommended. |
| Fig.3.99 15–20 h onset delay | Figure | p.323 | INCLUDED_AS_MUST | — | View recommended. |
| Eq.3:257–3:260 | Equations | p.324–325 | INCLUDED_AS_MUST | — | Keep. |
| Fig.3.100 onset/build-up patterns | Figure | p.325 | INCLUDED_AS_CONTEXT | — | Useful. |
| Fig.3.101 model schematic | Figure | p.325 | INCLUDED_AS_CONTEXT | — | Useful. |
| PD13 Tolerance I | Case study | p.805–809 | INCLUDED_AS_MUST | — | Keep as tolerance/rebound case only. |
| Fig.13.1 observed/model II response-time | Figure | p.806 | INCLUDED_AS_MUST | — | View useful. |
| Fig.13.2 response vs time/concentration | Figure | p.807 | INCLUDED_AS_CONTEXT | — | Useful. |
| Table 13.1 model comparison | Table | p.808 | INCLUDED_AS_MUST | — | Keep. |
| Fig.13.3 simulated single infusion/rebound | Figure | p.808 | INCLUDED_AS_CONTEXT | — | Useful. |
| PD20 Effect compartment I | Case study | p.836–839 | INCLUDED_AS_CONTEXT | — | Keep as numeric anchor. |
| Fig.20.1 observed response-time | Figure | p.836 | INCLUDED_AS_CONTEXT | — | Useful. |
| Fig.20.2 simulated doses same tmax | Figure | p.839 | INCLUDED_AS_CONTEXT | — | Useful. |
| PD21 link/turnover/receptor models | Case study | p.840–845 | INCLUDED_AS_CONTEXT | — | Keep as ke0/kout/koff comparison only. |
| Table 21.1 | Table | p.845 | INCLUDED_AS_CONTEXT | — | Optional. |
| PD35 Transduction | Case study | p.910–914 | INCLUDED_AS_MUST | — | Keep. |
| Fig.35.1 observed data | Figure | p.910 | INCLUDED_AS_MUST | — | View useful. |
| Fig.35.2 model schematic | Figure | p.912 | INCLUDED_AS_CONTEXT | — | Useful. |
| Fig.35.3 observed/predicted response | Figure | p.913 | INCLUDED_AS_CONTEXT | — | Useful. |
| Fig.35.4 predicted response-time | Figure | p.913–914 | INCLUDED_AS_CONTEXT | — | Useful. |
| Table 35.1 transduction steps | Table | p.914 | INCLUDED_AS_MUST | — | Keep. |

### T5-B. R&T Structural Elements

| PDF Element | Type | PDF Location | Step 1 Status | Omission Verdict | Required Action |
|---|---|---|---|---|---|
| Chapter 8 objectives | Objectives | p.233 | INCLUDED_AS_CONTEXT | — | Keep “time always matters” message. |
| Time delays between concentration and response | Heading | p.234 | INCLUDED_AS_MUST | — | Keep. |
| Fig.8-1 digoxin | Figure/example | p.234 | INCLUDED_AS_MUST | — | Keep. |
| Fig.8-2 naproxen counterclockwise hysteresis | Figure/example | p.235 | INCLUDED_AS_MUST | — | Keep. |
| Causes: tissue distribution | Heading/message | p.235–236 | INCLUDED_AS_MUST | — | Keep. |
| Causes: pharmacodynamics/downstream systems | Heading/message | p.236–237 | INCLUDED_AS_MUST | — | Keep. |
| Fig.8-3 downstream compartments | Figure | p.236 | INCLUDED_AS_CONTEXT | — | Useful. |
| Fig.8-4 tight binding slow dissociation | Figure | p.238 | INCLUDED_AS_CONTEXT | — | Useful if discussing slow binding. |
| Fig.8-5 downstream response peak delay | Figure | p.238 | INCLUDED_AS_CONTEXT | — | Useful. |
| Fig.8-6 midazolam direct link | Figure | p.239 | OMITTED_JUSTIFIABLE | Low | Optional. |
| Eq.8-1–8-3 log-linear response decline | Equations | p.239 | INCLUDED_AS_CONTEXT | — | Keep if used. |
| Fig.8-7 locomotor activity | Figure | p.240 | OMITTED_JUSTIFIABLE | Low | No action. |
| Fig.8-8 ranitidine/gastric pH | Figure | p.240 | OMITTED_JUSTIFIABLE | Low | No action. |
| Systems in flux / indirect response four cases | Heading/message | p.241 | INCLUDED_AS_MUST | — | Keep. |
| Fig.8-9 ibuprofen fever | Figure/example | p.241 | INCLUDED_AS_CONTEXT | — | Useful. |
| Fig.8-10 warfarin/prothrombin | Figure/example | p.242 | INCLUDED_AS_CONTEXT | — | Useful. |
| Fig.8-11 PK- vs PD-rate-limited response | Figure | p.243–244 | INCLUDED_AS_CONTEXT | — | Optional. |
| Revealing concentration-response relationship | Heading | p.245 | INCLUDED_AS_MUST | — | Keep. |
| Fig.8-13 effect compartment concept | Figure | p.245 | INCLUDED_AS_MUST | — | View recommended. |
| Fig.8-14 naproxen effect compartment collapse | Figure | p.246 | INCLUDED_AS_MUST | — | View recommended. |
| Warfarin Eq.8-6–8-8 / Fig.8-15–8-16 | Equations/figures | p.247–248 | INCLUDED_AS_CONTEXT | — | Sufficient. |
| Decline of response with time | Heading | p.248 | INCLUDED_AS_CONTEXT | — | Keep as rate-limiting background. |
| Fig.8-17 response decline regions | Figure | p.249 | INCLUDED_AS_CONTEXT | — | Useful. |
| Fig.8-18 succinylcholine paralysis | Figure/example | p.249–250 | INCLUDED_WITH_ERROR | MISSING_EXAMPLE if uncorrected | Correct with d-tubocurarine separation. |
| Fig.8-19 minoxidil | Figure | p.250 | OMITTED_JUSTIFIABLE | Low | No action. |
| Fig.8-20 aspirin | Figure/example | p.251 | OPTIONAL | Low for Session 12 | Include only if rate-limiting contrast needed. |
| Fig.8-21 omeprazole | Figure/example | p.252 | OPTIONAL | Low for Session 12 | Include only if slow dissociation contrast needed. |
| Fig.8-22 paclitaxel | Figure/example | p.253 | OPTIONAL | Low for Session 12 | Optional. |
| Onset and duration / Eq.8-10–8-12 | Heading/equations | p.254–255 | INCLUDED_AS_CONTEXT | — | Keep for succinylcholine duration. |
| Fig.8-23 log-dose duration | Figure | p.255 | INCLUDED_AS_CONTEXT | — | Useful. |
| Fig.8-24 succinylcholine T50 vs dose | Figure | p.256 | INCLUDED_WITH_ERROR | MISSING_EXAMPLE if uncorrected | Correct numerical attribution. |
| Fig.8-25–8-29 methylpred/rosuvastatin | Figures | p.257–259 | OMITTED_JUSTIFIABLE | Low | Not needed for Session 12 core. |
| Key relationships | Summary | p.260 | PARTLY_INCLUDED | MISSING_AUTHOR_MSG minor | Not necessary unless making R&T summary box. |
| Study problems / Fig.8-30–8-33 / Tables 8-1–8-2 | Exercises | p.260–264 | OMITTED_JUSTIFIABLE | Low | No action. |

---

## T6: Figure Inventory & Learning Value Audit

**Inspection note:** PDF pages were rendered to PNG and key pages were visually inspected through rendered contact sheets. For figures not directly inspected in the contact sheets, ratings use caption + surrounding context conservatively.

### T6-A. G&W Figures/Tables

| Figure/Table | Page | Teaches | Value | View Instruction? | Redraw/New Schematic? | Inspection Method | Rationale |
|---|---:|---|---|---|---|---|---|
| Fig.3.51 | 262 | Direct vs delayed response and hysteresis loop | ESSENTIAL | YES | YES | VISUAL_INSPECTED | This is the visual definition of delayed response and link-model motivation. |
| Fig.3.52 | 262 | PK→link/effect compartment→PD response chain | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Core architecture of this session. |
| Fig.3.53 | 263 | Plasma C, Ce, response-vs-Ce, response-time sequence | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Explains why Ce is inferred and how ke0 enters. |
| Table 3.8 | 265 | One-compartment link equations for bolus/first-order/zero-order input | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Dense formula table; text/card summary is enough. |
| Fig.3.54 | 266 | Larger ke0 gives faster Ce-Cp equilibration | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Key intuition for `t1/2,ke0`. |
| Fig.3.55 | 268 | Effect-time fit using effect compartment + Emax | USEFUL | YES | NO | VISUAL_INSPECTED | Good anchor, but not structurally indispensable if Fig.3.53 is used. |
| Table 3.9 | 269 | Literature `t1/2,ke0` examples | ESSENTIAL | YES | NO | CAPTION_AND_CONTEXT | Prevents drug/example confusion; must be used correctly. |
| Fig.3.56 | 270 | Simulation with different ke0/n/EC50/Emax | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Useful for sensitivity intuition. |
| Fig.3.57 | 270 | Simulation showing response dependence on ke0/Emax | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Redundant with Fig.3.56/3.58. |
| Fig.3.58 | 271 | Simulation of extreme sigmoid/EC50 settings | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Useful but not mandatory. |
| Fig.3.59 | 271 | Turnover vs link misfit | ESSENTIAL | YES | YES | CAPTION_AND_CONTEXT | Core pitfall figure; should not be mislabeled PD13. |
| Table 3.10 | 271 | Implausible dose-dependent EC50/Emax/n under link misapplication | ESSENTIAL | YES | NO | CAPTION_AND_CONTEXT | Mandatory numeric anchor for C1 pitfall. |
| Fig.3.71 | 285 | Nitroglycerine tolerance/rebound and Hat TDS | USEFUL | YES | NO | CAPTION_AND_CONTEXT | Memorable but not sufficient as model proof. |
| Fig.3.72 | 286 | Mechanistic routes to tolerance | USEFUL | NO | YES | CAPTION_AND_CONTEXT | Could be redrawn as a cleaner mechanism map. |
| Table 3.12 | 287 | Taxonomy of tolerance/rebound modeling approaches | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Governs C3 context hierarchy. |
| Fig.3.73 | 288 | Systems analysis approach | SKIPPABLE | NO | NO | CAPTION_AND_CONTEXT | Context only. |
| Fig.3.74 | 291 | Time-dependent attenuation of parameters | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Context limitation example. |
| Fig.3.75 | 292 | Decline of buprenorphine response after injection | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Supports attenuation model; not core. |
| Fig.3.76 | 293 | Antagonistic metabolite model | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Context alternative. |
| Fig.3.77 | 294 | Tolerance compartment model | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Context alternative. |
| Fig.3.78 | 295 | Counteracting mechanisms | USEFUL | NO | YES | CAPTION_AND_CONTEXT | Mechanistically useful but visually dense. |
| Fig.3.79 | 295 | Feedback/rebound response pattern | USEFUL | YES | NO | CAPTION_AND_CONTEXT | Good visual for rebound. |
| Fig.3.80 | 296 | Instantaneous/indirect/tolerant systems and hysteresis direction | ESSENTIAL | YES | YES | CAPTION_AND_CONTEXT | Important for clockwise/counterclockwise nuance. |
| Fig.3.81 | 296 | Negative feedback by R or moderator M | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Core bridge to moderator ODE. |
| Fig.3.82 | 298 | Overshoot/shoulder/rebound and AUCE/AUCR asymmetry | ESSENTIAL | YES | NO | CAPTION_AND_CONTEXT | Core for C3 model behavior. |
| Fig.3.83 | 298 | Biomarker Y drift/overshoot/shoulder without rebound | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Optional example. |
| Fig.3.84 | 302+ | Simulations of response/modulator M | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Useful if page range fully available. |
| Fig.3.98 | 323 | Receptor-transduction chain | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Core diagram for C4. |
| Fig.3.99 | 323 | 15–20 h onset delay not captured by ordinary turnover | ESSENTIAL | YES | NO | CAPTION_AND_CONTEXT | Core data shape for transduction. |
| Fig.3.100 | 325 | Few/slow vs many/rapid compartments | USEFUL | YES | YES | CAPTION_AND_CONTEXT | Good candidate for simplified schematic. |
| Fig.3.101 | 325 | Alternative transduction model structure | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Context. |
| Fig.13.1 | 806 | PD13 repeated infusion, tolerance/rebound | ESSENTIAL | YES | NO | CAPTION_AND_CONTEXT | Core PD13 data anchor. |
| Fig.13.2 | 807 | Response-vs-time and response-vs-concentration with event labels | USEFUL | YES | NO | CAPTION_AND_CONTEXT | Useful for initial estimate discussion. |
| Table 13.1 | 808 | Model I/II/III comparison; Model II best | ESSENTIAL | YES | NO | CAPTION_AND_CONTEXT | Mandatory tolerance anchor. |
| Fig.13.3 | 808 | Single infusion simulation and slight rebound | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Supports Model II interpretation. |
| Fig.20.1 | 836 | PD20 effect-time data after IV bolus | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Numeric example. |
| Fig.20.2 | 839 | Simulated 5/45/225 µg/kg doses same tmax | USEFUL | YES | NO | CAPTION_AND_CONTEXT | Good visual support for same `tmax`. |
| Fig.21.1–21.6 | 840–845 | Link/turnover/receptor model comparison for antagonist X | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Useful context; too much for core card. |
| Table 21.1 | 845 | ke0/kout/koff and potency comparison | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Useful for ke0/kout/koff distinction. |
| Fig.35.1 | 910 | PD35 concentration/response data for three doses | ESSENTIAL | YES | NO | CAPTION_AND_CONTEXT | Core transduction data. |
| Fig.35.2 | 912 | PD35 receptor-transduction schematic | USEFUL | YES | NO | CAPTION_AND_CONTEXT | Good support for chain ODE. |
| Fig.35.3 | 913 | Observed/model-predicted response-time data | USEFUL | YES | NO | VISUAL_INSPECTED | Supports initial estimates and fit. |
| Fig.35.4 | 913–914 | Predicted response-time data for model | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Optional. |
| Table 35.1 | 914 | Transduction step comparison WRSS | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Mandatory numeric anchor. |

### T6-B. R&T Figures/Tables

| Figure/Table | Page | Teaches | Value | View Instruction? | Redraw/New Schematic? | Inspection Method | Rationale |
|---|---:|---|---|---|---|---|---|
| Fig.8-1 | 234 | Digoxin effect rises while plasma concentration falls | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Canonical delay example. |
| Fig.8-2 | 235 | Naproxen counterclockwise hysteresis | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Core hysteresis visual. |
| Fig.8-3 | 236 | Site of action vs downstream measured response | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Important for mechanism classification. |
| Fig.8-4 | 238 | Slow dissociation from target site | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Useful for slow binding context. |
| Fig.8-5 | 238 | More distant downstream response peaks later | USEFUL | NO | YES | CAPTION_AND_CONTEXT | Helpful but can be redrawn simply. |
| Fig.8-6 | 239 | Direct link PK-PD example | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Useful contrast. |
| Fig.8-7 | 240 | Locomotor CNS response decline | SKIPPABLE | NO | NO | CAPTION_AND_CONTEXT | Not central. |
| Fig.8-8 | 240 | Ranitidine concentration and gastric pH | SKIPPABLE | NO | NO | CAPTION_AND_CONTEXT | Not central. |
| Fig.8-9 | 241 | Ibuprofen fever indirect response hysteresis | USEFUL | YES | NO | VISUAL_INSPECTED | Supports systems-in-flux example. |
| Fig.8-10 | 242 | Warfarin sluggish prothrombin response | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Context for turnover. |
| Fig.8-11 | 243–244 | PK vs PD rate-limited decline | USEFUL | NO | YES | CAPTION_AND_CONTEXT | Useful distinction. |
| Fig.8-12 | 244 | Endogenous system turnover | USEFUL | NO | YES | CAPTION_AND_CONTEXT | Supports indirect response. |
| Fig.8-13 | 245 | Effect compartment links concentration with response | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Core R&T effect compartment diagram. |
| Fig.8-14 | 246 | Naproxen hysteresis removed by effect compartment | ESSENTIAL | YES | NO | CAPTION_AND_CONTEXT | Core model-diagnostic visual. |
| Fig.8-15 | 247 | Warfarin synthesis inhibition over time | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Context. |
| Fig.8-16 | 248 | Concentration-inhibition relationship after heptabarbital pretreatment | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Context. |
| Fig.8-17 | 249 | Response decline regions and linear decline in 20–80% region | USEFUL | YES | NO | CAPTION_AND_CONTEXT | Supports response decline math. |
| Fig.8-18 | 250 | Succinylcholine paralysis response-time profile | ESSENTIAL | YES | NO | CAPTION_AND_CONTEXT | Must be used with correct numerical interpretation. |
| Fig.8-19 | 250 | Minoxidil response decline | SKIPPABLE | NO | NO | CAPTION_AND_CONTEXT | Peripheral. |
| Fig.8-20 | 251 | Aspirin antiplatelet response vs plasma | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Useful rate-limited contrast, not core. |
| Fig.8-21 | 252 | Omeprazole persistent acid suppression | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Useful slow target recovery contrast. |
| Fig.8-22 | 253 | Paclitaxel leukocyte response over weeks | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Peripheral. |
| Fig.8-23 | 255 | Duration proportional to log dose | USEFUL | YES | NO | CAPTION_AND_CONTEXT | Supports succinylcholine duration logic. |
| Fig.8-24 | 256 | Succinylcholine T50 vs dose | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Corrects mixed attribution. |
| Fig.8-25–8-29 | 257–259 | Methylprednisolone/rosuvastatin exposure-response examples | SKIPPABLE | NO | NO | CAPTION_AND_CONTEXT | Outside Session 12 core. |
| Fig.8-30–8-33 / Tables 8-1–8-2 | 260–264 | Study problems | SKIPPABLE | NO | NO | CAPTION_AND_CONTEXT | Not needed for Step 1 cards. |

---

## Patch Memo Independent Classification

| Patch Memo Item | Classification | Audit Decision |
|---|---|---|
| Phase 1 재실행 불필요 / Phase 2 필수 / HTML 직행 금지 | MATCH | 본 감사도 동일 판정. |
| Scope Lock 큰 구조 반영 양호 | MATCH | Draft의 4-card structure는 적절. |
| Effect compartment 핵심 메시지 양호 | MATCH | `Ce` indirect, `ke0`, same `tmax` 구조 반영. |
| PD35 anchor 양호 | MATCH | Table 35.1 수치와 practical/parsimony 해석 대체로 타당. |
| Table 3.10 pitfall을 PD13이라고 부른 오류 | MATCH | MUST_FIX 1순위. |
| `k1e=ke0` 물리적 정합성 강제 설명 과도 | MATCH | MUST_FIX. |
| succinylcholine/d-tubocurarine 수치 혼합 | MATCH | MUST_FIX. |
| hysteresis 방향 = 모델 결정 과강 | MATCH | MUST_FIX/SHOULD_FIX. |
| NDA Deficiency Letter는 교과서 밖 실무 해석 | MATCH | MUST_FIX 라벨링 필요. |
| Transduction engineering analogies are NOT_IN_SOURCE | MATCH | 삭제가 아니라 라벨링 권장. |
| PD20/PD21/PD35 수치 전수 대조 필요 | MATCH | 본 감사에서 주요 수치 MATCH 확인. |

---

## Final Go/No-Go Recommendation

**Go 조건부 유지.** Draft v0는 concept selection과 source split이 좋고, Phase 1을 다시 돌릴 필요는 없다. 다만 아래 6개 패치가 완료되기 전에는 Content Lock 또는 HTML 변환으로 넘어가면 안 된다.

### Mandatory Phase 4A Patch List

1. `PD13 Table 3.10` / `PD13 EC50 분기` → **`G&W §3.9.7 Table 3.10 link-model pitfall / PD12 data`**로 전면 수정.
2. `PD13`은 **repeated IV infusion tolerance/rebound Model I/II/III comparison**으로만 사용.
3. `k1e = ke0`는 **identifiability-based simplifying assumption**으로 수정. “물리적 질량보존 때문에 강제” 삭제.
4. `succinylcholine 4 min ke0` 삭제. **d-tubocurarine/vecuronium Table 3.9 4 min**과 **succinylcholine R&T dose-duration example** 분리.
5. “hysteresis 방향이 모델 선택을 결정” → “hysteresis 방향은 첫 번째 진단 단서”로 낮춤.
6. NDA/FDA/ICH/NONMEM/SAEM/bootstrap/BIC/Erlang/Bode/tanks-in-series/do-loop 계열은 `[교과서 외 실무 해석]`, `[구현 번역]`, `[구조적 비유]` 라벨 부착 또는 본문에서 분리.

### Post-patch Expected Status

위 6개가 반영되면 Session 12 Draft는 **Content Lock 후보**로 충분하다. 특히 다음 anchor는 유지할 가치가 높다.

- G&W §3.9.1–3.9.7: `Ce` indirect estimation, `same tmax`, Table 3.9, Table 3.10 pitfall.
- G&W §3.11.9–3.11.11 + PD13: Moderator M, `ktol > kout`, Model II AIC/WRSS superiority.
- G&W §3.13 + PD35: 15–20 h onset delay, transit chain, Table 35.1 WRSS comparison.
- R&T Ch.8: digoxin/naproxen hysteresis, effect compartment collapse, systems-in-flux, succinylcholine duration logic.


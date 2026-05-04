# 03_Audit Report v1 — Source Fidelity Audit

**업무 형태:** 파일 분석 / PDF 대조 감사 / 웹 검색 OFF  
**입력:** `03_G_경구 PK F·Ka·Tmax·흡수(1).pdf`, `03_T_경구 PK F·Ka·Tmax·흡수(1).pdf`, `03_step1_draft_v0.md`, `S03_phase1_patch memo.md`, audit prompt  
**산출:** Audit Report v1  
**역할:** Source Fidelity Auditor — 검증 전용. 재작성, 문장 개선, 새 비유·설명 생성은 수행하지 않음.  

---

## Executive Verdict

**판정:** `CONDITIONAL PASS — Phase 1 Draft v0는 구조적으로 우수하나, Phase 4A/HTML 직행 전 MUST_FIX 패치 필요.`

Draft v0의 5개 MUST 카드 구성은 대체로 타당하다. 특히 `C(t) Master Equation`, `tmax/Cmax`, `F`, `V/F 식별불가능성 + flip-flop`, `ka,app vs ka,true`를 핵심 spine으로 잡은 것은 PDF 원문과 잘 맞는다. 그러나 다음 오류·과잉 확장·source-header 불일치는 반드시 패치해야 한다.

### MUST_FIX 핵심 8건

1. **T source header 누락:** Draft header에는 Rowland & Tozer Ch.7이 빠져 있으나, 본문은 Ch.7의 BCS, gastric emptying, F = FF·FG·FH를 사용한다.
2. **T Eq.6-3 오표기:** Draft의 Curation Map은 Master Equation을 `T Eq.6-3`로 연결하지만, T Eq.6-3은 integrated solution이 아니라 mass-balance ODE다. Integrated solution은 Appendix F Eq.F-1이다.
3. **Flip-flop 직관 문장 오류:** `ka ≪ kel이면 천천히 올라갔다가 빠르게 내려와야`는 관찰 terminal decline의 의미를 잘못 전달한다.
4. **“IV 없이는 V·F·ka·kel 어느 것도 진짜 값이 아니다” 과강함:** V/F 분리 불가와 terminal slope label 불확정은 맞지만, 모든 parameter를 일괄 “진짜가 아님”으로 단정하면 과도하다.
5. **F는 “오직 IV 비교로만” 표현 보완 필요:** Plasma AUC 기반 절대 F에는 IV reference가 필요하지만, T Ch.6은 urine data 기반 bioavailability/relative bioavailability도 다룬다.
6. **PK2 V 계산 충돌:** Source는 `V/F = 32 L`, `F = 82%`, `true V = 20 L`이라고 쓰지만 산술상 26 L이다. Draft는 26 L을 정답처럼 사용하므로 source fidelity상 위험하다.
7. **Self-test Q5/Q8 내부 반감기 논리 오류:** `ka < kel`인 oral model에서 관찰 terminal slope는 작은 rate constant를 따라야 하므로, `terminal t½ = ln2/kel`처럼 제시한 부분은 수학적으로 불일치한다.
8. **Regulatory/deficiency/ICH/FDA 문장:** BE 기준은 source 기반이나, NDA deficiency letter, ICH M9/FDA Population PK guidance 문장은 PDF source에 없고 일부는 부정확할 가능성이 있어 `[실무 추론]` 또는 삭제/분리 필요.

---

# T1: Equation/Numerical Audit

| Item | Draft v0 Expression / Claim | PDF Source | Classification | Correction / Required Action |
|---|---|---|---|---|
| Source scope | Source B = `R&T Ch.6 + Appendix F` | T PDF also includes Ch.7 pp.197–220; Draft uses Ch.7 content | **ERROR** | Header and §1 source line must include `Ch.7 context only` if Ch.7-derived claims remain. |
| Curation Map source | `Master Equation = G Eq.2:35; T Eq.6-3` | T Eq.6-3 = `dA/dt = Rate of absorption − k·A`; Appendix F Eq.F-1 = integrated solution | **ERROR** | Replace with `T Eq.6-3 = mass-balance ODE; Appendix F Eq.F-1 = integrated first-order absorption solution`. |
| dAg/dt | `dA_g/dt = −ka·A_g` | G Eq.2:33 uses loss from gut; T Eq.6-2 uses rate proportional to amount remaining | **MATCH** | Simplified notation acceptable. |
| dC/dt / oral ODE | `dC/dt = ka·F·Dpo·e−ka t/V − kel·C` | G Eq.2:32–2:34 | **MATCH** | Symbol conversion K→kel acceptable. |
| Master Equation | `C(t)=ka·F·Dpo/[V(ka−kel)]·[e−kel t−e−ka t]` | G Eq.2:35; T Appendix F Eq.F-1 | **MATCH** | Keep. |
| Lag-time equation | `t → t−tlag; C=0 if t<tlag` | G Eq.2:39; G note `C=0 when t<tlag` | **MATCH** | Keep. |
| Zero-order input equation | `C=Rin/(V·kel)[1−e−kel·Tabs]e−kel·t′` | G Eq.2:66/2:67 | **MATCH** | Add condition only if later rewriting: during absorption `Tabs=t`, after cessation `Tabs` constant and `t′` is time after absorption. |
| ka = kel limit | `C=(k′·F·Dpo/V)·t·e−k′t` | G Eq.2:58 | **MATCH** | Keep. |
| dC/dt for tmax | Draft derivative Eq.2:49 | G Eq.2:49 | **MATCH** | Keep. |
| tmax derivation | `tmax = ln(ka/kel)/(ka−kel)` | G Eq.2:52; T Appendix F Eq.F-6 | **MATCH** | Keep. |
| Cmax | `Cmax ≈ F·Dpo/V·e−kel·tmax` under `ka ≫ kel` | G Eq.2:53 | **MATCH** | Keep; approximation condition must remain. |
| Lag-time tmax/Cmax | `tmax → tmax+tlag`; Cmax uses `(tmax−tlag)` | G Eq.2:54–2:55 | **MATCH** | Keep. |
| F absolute | `F=(AUCpo/AUCiv)(Div/Dpo)` | G Eq.2:74; T Eq.6-11 | **MATCH** | Keep, but do not imply this is the only possible data type for all F estimation. |
| Relative F | `Frel=(AUCB/AUCA)(DA/DB)` | T Eq.6-15 | **MATCH** | Keep. |
| Urine-based F | Draft underemphasizes urine data | T Eq.6-18–6-21; Ch.6 objectives/key relationships | **MISSING** | Add a context sentence: plasma AUC method needs IV for absolute F; urine excretion data can estimate F/relative F if assumptions such as constant `fe` hold. |
| F mechanistic product | `F = FF·FG·FH` | T Ch.7 absorption/first-pass section | **MATCH**, but source header inconsistent | Keep only if Ch.7 is listed as source/context. |
| V/F identifiability | Oral-only data estimate `V/F`; F and V cannot be uniquely separated without IV | G p.32; T p.185 says oral-only parameters difficult | **MATCH** | Keep. |
| Overstatement | `IV 비교 없이는 V·F·ka·kel 어느 것도 진짜 값이 아니다` | G/T support V/F and flip-flop ambiguity, not blanket invalidation of all values | **ERROR** | Change to: oral-only data cannot separate V and F, and terminal slope cannot always be assigned to kel vs ka without IV or route/formulation comparison. |
| Flip-flop algebra | Swapping ka and kel preserves C(t) shape after sign reversal | Implied by Eq.2:35; supported by G Fig.2.17/PK2 Solution III | **MATCH** | Keep with source-context caveat. |
| Flip-flop intuition | `ka ≪ kel이면 천천히 올라갔다가 빠르게 내려와야` | T Case C: observed decline corresponds to absorption half-life; G Fig.2.17 terminal slope reflects absorption | **ERROR** | Must correct conceptual direction. Observed terminal decline can be slow because residual absorption is rate-limiting. |
| PK2 Solution II | `Ka=0.043 min⁻¹; K=0.0088 min⁻¹; V/F=32 L; tlag=16 min` | G PK2 p.480 | **MATCH** | Keep. |
| PK2 Solution I CV claim | Draft links `CV% 3400%` to PK2 Solution I | G PK2 says high standard errors/correlation; `CV% 3400%` belongs to PK3 Table 3.1 first-order model | **ERROR** | Do not attach `3400%` to PK2. Use “high standard errors/correlation” for PK2; reserve 3400% for PK3. |
| PK2 deconvolution lag/F | `15 min lag-time`, `about 60%`, `NCA 64%`, `F=82%` | G PK2 p.480 | **RESTORED [확인 필요]** | Source itself appears internally inconsistent. Preserve source wording and flag; do not resolve silently. |
| PK2 true V | Draft answer `V=32×0.82≈26 L`; source states `true V=20 L` | G PK2 p.480 | **ERROR / RESTORED** | Do not present 26 L as source-confirmed. Mark as arithmetic check vs source inconsistency. |
| PK2 Solution III | `initial Ka/K reversed 0.01/0.1; final Ka=0.0088, K=0.043, V/F=6.54 L, tlag=16 min` | G PK2 Solution III | **MATCH with unit caution** | Source text/OCR shows `0.043 h⁻¹`; context suggests min⁻¹. Flag unit as [확인 필요]. |
| `6배 변동` | Draft says `V/F 32 L → 6.54 L` is `6배` | Arithmetic: 32/6.54≈4.9; source says 6.54 vs 30 L | **ERROR** | Use `약 5배` or source phrase without ratio. |
| PK3 zero-order model | First-order `Ka=0.42, Ke=0.43, V/F=99, CV%=3400`; zero-order `Tabs=4.54, Ke=0.47, V/F=96`, CV 5/14/11 | G Table 3.1 | **MATCH** | Keep. |
| PK3 AIC | `AIC 85.2 vs 76.2` | G PK3 p.486 | **MATCH** | Keep. |
| PK3 interpretation | Better zero-order fit does not prove true zero-order absorption; need multiple doses, dose range, IV | G PK3 conclusion | **MATCH** | Keep. |
| ka,app equation | `ka,app = ka,true + kd` | G Fig.2.24 / p.40–41 | **MATCH** | Keep with source wording “apparent loss from GI tract”. |
| F from ka,true/kd | `F=ka,true/(ka,true+kd)` | G Eq.2:70 | **MATCH** | Keep. |
| Rate input/loss with ka,true/kd | Input/loss formulas explicitly written in Draft | Derived from G Eq.2:68–2:70 and figures | **RESTORED** | Accept as derivation, but mark as derived rather than directly quoted source equation. |
| Multiple absorption sites | Eq.2:80–2:82, buccal + GI model | G §2.2.11 | **MATCH** | Context inclusion acceptable. |
| Accumulation R | `R=1/(1−e−kel·τ)` | G Eq.2:78 | **MATCH** | As context/dependency only. |
| BE criterion | `90% CI 0.80–1.25` | T Fig.6-13 and surrounding BE text | **MATCH** | Keep. |
| `tmax not 90% CI target` | Draft states BE tmax is not 90% CI target | T says AUC, Cmax, tmax are common measures; notes tmax is noisy/flat near peak; Fig.6-13 focuses CI declarations | **RESTORED [확인 필요]** | The flat-peak limitation is supported; exact “not 90% CI target” is not directly established by the provided pages. Mark as regulatory-context, not direct source. |
| Fluticasone example | `500 µg inhaled; median tmax 90 min; Cmax 30–90 min; absorption t½ 3.8–4 h; 10 min wrong if flip-flop ignored` | T Fig.6-7 / p.177 | **MATCH** | Keep. |
| Theophylline example | Food/water alter absorption kinetics but not terminal half-life; terminal half-life 6.3 h | T Fig.6-8 | **MISSING** | Add as optional/should context for route/formulation discrimination. |
| Penicillin G example | Sparingly soluble i.m. formulation can make absorption rate-limiting | T Fig.6-9 | **MISSING** | Add as should-fix example if flip-flop teaching is expanded. |
| Q5 hypothetical | `ka=0.05 hr⁻¹, kel=0.5 hr⁻¹, terminal t½=1.4 h` | Not in source; internally inconsistent for observed oral terminal slope | **ERROR / NOT_IN_SOURCE** | If retained as hypothetical, terminal/kel half-life distinction must be corrected. With ka<kel, terminal decline should be associated with ka unless independently assigned. |
| Q8 boss dilemma | `ka=0.18, kel=0.69, terminal t½≈1.0 h` with flip-flop discussion | Not in source; internally inconsistent | **ERROR / NOT_IN_SOURCE** | Recalculate terminal interpretation. `ln2/0.18≈3.85 h`, `ln2/0.69≈1.0 h`; do not call the latter observed terminal half-life under ka<kel oral-only setup. |
| ICH M9 / FDA PopPK sentence | Draft cites external guidance in Q8 answer | Not in PDF source; web search OFF; ICH M9 mention is not sourced here | **NOT_IN_SOURCE / REJECT** | Remove, or tag explicitly as external regulatory inference requiring separate source verification. |
| Deficiency letter phrase | “standard deficiency letter” phrasing | Not in PDF source | **NOT_IN_SOURCE / REJECT** | Remove or mark as fictionalized regulatory teaching scenario, not source-backed claim. |
| `AUC = F·D/(CL/F)·F = D/CL_true` | Draft causal chain in Phantom Volume Drift | Source relation is `AUC = F·Dose/CL = Dose/(CL/F)` | **ERROR** | Correct algebra. `Dose/(CL/F)` equals `F·Dose/CL`, not `D/CL_true` unless F=1. |

---

# T2: Examples & Data Audit

| Item | Draft v0 Status | PDF Location | Classification | Importance | Action |
|---|---|---|---|---|---|
| G Fig.2.16 route comparison in rats | Not materially used | G p.29 | **MISSING** | LOW | Optional; useful only as variability/route anchor. |
| G Fig.2.17 flip-flop iv/po parallel vs non-parallel | Included | G p.30 | **INCLUDED_CORRECT** | HIGH | Keep. |
| G Method of residuals graphical example | Included as algorithm | G pp.31–33, Figs.2.18–2.20 | **INCLUDED_CORRECT** | HIGH | Keep; add figure view instruction later in Phase 4C. |
| G Table 2.2 initial estimates | Partially included | G p.34 | **INCLUDED_CORRECT but UNDERUSED** | MEDIUM | Could cite as source for initial estimates instead of only prose. |
| G Pidgeon-Pitlick / Vaughan | Explicitly omitted | G p.36 | **MISSING but justified** | LOW | Omission acceptable for B-Standard. |
| G zero/mixed-order input schematic | Included conceptually | G Fig.2.23 pp.38–39 | **INCLUDED_CORRECT** | MEDIUM | Keep. |
| G apparent vs true absorption constant | Included | G Figs.2.24–2.25 pp.40–41 | **INCLUDED_CORRECT** | HIGH | Keep; source header/caption caveat okay. |
| G bioavailability sequential IV+oral | Included | G Fig.2.26 / Eq.2:71–2:74 pp.41–42 | **INCLUDED_CORRECT** | HIGH | Keep. |
| G multiple dosing/accumulation | Context only | G pp.43–45 | **INCLUDED_CORRECT** | LOW | Good as dependency only. |
| G multiple absorption sites | Context only | G Fig.2.31 / Eq.2:80–2:82 pp.46–47 | **INCLUDED_CORRECT** | MEDIUM | Accept as context. |
| G conclusion Figure 2.32 | Not explicitly used as visual anchor | G p.47 | **MISSING** | MEDIUM | Should add figure view instruction in Phase 4C; it summarizes oral curve determinants. |
| G PK2 100 µg oral drug A | Included | G pp.476–482 | **INCLUDED_ERROR in V calculation; otherwise correct** | HIGH | Correct V/F/F/V inconsistency handling. |
| G PK2 Solution I no lag | Included | G p.480 | **INCLUDED_ERROR** | MEDIUM | Remove `CV% 3400` from PK2; use high SE/correlation only. |
| G PK2 Solution II lag-time model | Included | G p.480 | **INCLUDED_CORRECT** | HIGH | Keep. |
| G PK2 Solution III flip-flop | Included | G pp.481–482 | **INCLUDED_CORRECT with ratio/unit caution** | HIGH | Correct 6-fold claim and unit caveat. |
| G PK3 20 mg highly polar drug | Included | G pp.483–486 | **INCLUDED_CORRECT** | HIGH | Keep. |
| G PK3 first vs zero-order AIC/CV | Included | G Table 3.1 p.486 | **INCLUDED_CORRECT** | HIGH | Keep. |
| T aspirin 650 mg IV vs oral solution | Omitted | T Fig.6-3 p.172 | **MISSING** | MEDIUM | Useful for “absorption delays/lower peak” author message. |
| T bucket analogy / first-order absorption | Mostly replaced by other explanation | T Fig.6-1 p.171 | **MISSING** | LOW–MEDIUM | Optional; not required if draft uses G model spine. |
| T zero vs first-order remaining-to-be-absorbed plot | Partially included | T Fig.6-2 p.171 | **MISSING/UNDERUSED** | MEDIUM | Should include if zero-order distinction remains a confusion pair. |
| T dose change plot | Not explicitly included | T Fig.6-5 p.174 | **MISSING** | MEDIUM | Add to prevent the misleading `Cmax not dose proportional` impression. |
| T absorption kinetics Case A/B/C | Included conceptually | T Fig.6-6 pp.175–176 | **INCLUDED_CORRECT** | HIGH | Keep and fix flip-flop wording. |
| T fluticasone propionate | Included | T Fig.6-7 p.177 | **INCLUDED_CORRECT** | HIGH | Keep. |
| T theophylline food/water | Omitted | T Fig.6-8 p.178 | **MISSING** | MEDIUM | Should include as route/formulation discrimination example. |
| T penicillin G formulation/route | Omitted | T Fig.6-9 p.178 | **MISSING** | MEDIUM | Should include as absorption-limited example. |
| T changing disposition kinetics | Mostly absent | T Figs.6-10–6-11 pp.179–180 | **MISSING** | MEDIUM | Add as context if discussing CL/V effects on Cmax/tmax/AUC. |
| T product performance / BE | Included | T pp.181–183, Figs.6-12–6-13 | **INCLUDED_CORRECT with tmax caveat** | HIGH | Keep BE criterion; soften tmax regulatory specificity. |
| T Table 6-1 500 mg i.m./oral | Omitted | T Fig.6-14/Table 6-1 p.184 | **MISSING** | HIGH | Should add as concrete F/plasma/urine parameter-estimation anchor. |
| T urine data alone | Mostly omitted | T pp.187–188 | **MISSING** | HIGH | Add context sentence/table note for F and renal clearance from urine data. |
| T local bioequivalence/topical microdialysis | Omitted | T pp.188–189, Figs.6-16–6-18 | **MISSING justified** | LOW | Scope creep for this session unless BE/local topical is later needed. |
| T study problems/procainamide | Omitted | T pp.190–195, Tables 6-2–6-7 | **MISSING justified** | LOW | Study problems are not needed in Phase 1 core. |
| T Ch.7 BCS/gastric emptying/first-pass | Included in one sentence and F product | T pp.197–220 | **INCLUDED_CONTEXT but source header missing** | MEDIUM | Fix source header; keep compressed. |
| T Appendix F Table F-1/Fig.F-1 | Included conceptually | T pp.781–783 | **INCLUDED_CORRECT** | HIGH | Keep as Method of Residuals support. |

---

# T3: Author Key Messages

| Message | PDF Location | In Draft v0? | Status |
|---|---|---|---|
| Extravascular dosing introduces an absorption step; rate of change reflects absorption and elimination. | G p.28; T p.169–170 | Yes | INCLUDED |
| First-order systemic absorption is proportional to amount remaining to be absorbed. | T p.171; Eq.6-2 | Yes, via ODE | INCLUDED |
| Zero-order absorption differs from first-order; constant-rate input concepts apply. | T p.171–172; G p.38 | Yes | INCLUDED |
| Absorption delays and lowers peak vs equal IV bolus. | T Fig.6-3 p.172 | Weakly | SHOULD_FIX |
| At tmax, rate of absorption equals rate of elimination. | T p.173; G Eq.2:49–2:52; Appendix F | Yes | INCLUDED |
| Rising/declining limbs should not automatically be called absorption/elimination phases in flip-flop. | G p.29–30; T p.175 | Yes | INCLUDED, but wording patch needed |
| In flip-flop, decline phase can reflect absorption half-life, not elimination half-life. | G Fig.2.17; T Case C | Yes | INCLUDED, but one misleading sentence MUST_FIX |
| Early tmax does not prove rapid absorption. | T Fig.6-7 fluticasone p.177 | Yes | INCLUDED |
| Changing dose or F changes Cmax/AUC proportionally but not tmax, if other factors constant. | T Fig.6-5 p.174 | Partly absent; one draft phrase conflicts | SHOULD_FIX |
| Changing ka alters tmax/Cmax shape; AUC unchanged if F and CL unchanged. | T Fig.6-6 p.176 | Yes | INCLUDED |
| Changing CL changes AUC and can change tmax/Cmax; changing V changes Cmax and tmax in distinct ways. | T Figs.6-10–6-11 pp.179–180 | Weak/absent | SHOULD_FIX |
| No PK parameter can be determined confidently from a single oral dose alone: AUC can be calculated but CL cannot; decay half-life cannot be assigned without knowing rate limitation; V cannot be calculated. | T p.185 | Partly | SHOULD_FIX; aligns strongly with Draft apex |
| Bioavailability can be estimated from plasma data with IV reference; relative F can be estimated without IV. | T pp.183–185 | Yes | INCLUDED |
| Urinary excretion data can estimate bioavailability/relative bioavailability/renal clearance under assumptions. | T pp.187–188 | Mostly absent | MUST/SHOULD_FIX depending target depth |
| Apparent absorption constant from oral fitting is GI loss, not necessarily appearance in plasma. | G p.40–41 | Yes | INCLUDED |
| Lag-time, multiple peaks, and zero-order absorption confound extravascular interpretation. | G conclusion p.47 | Yes | INCLUDED |
| Figure 2.32 summarizes determinants of oral concentration-time curve. | G p.47 | Not as figure | SHOULD_FIX in Phase 4C view instruction |
| Chapter 7: physiologic/physicochemical factors influence absorption; BCS anticipates BA/BE problem products. | T Ch.7 pp.197–220 | Compressed | INCLUDED_CONTEXT, but source header missing |

---

# T4: Priority Summary

| # | Item | Priority | Rationale |
|---|---|---|---|
| 1 | Add R&T Ch.7 to Source B / pages if Ch.7 claims remain | MUST_FIX | Draft uses Ch.7-derived claims; header omits source. |
| 2 | Correct T Eq.6-3 as mass-balance ODE, not Master Equation | MUST_FIX | Direct source mis-citation. |
| 3 | Fix flip-flop “ka≪kel” intuitive sentence | MUST_FIX | Misleads terminal slope interpretation. |
| 4 | Soften `V·F·ka·kel none true` | MUST_FIX | Source supports apparent V/F and slope ambiguity, not blanket invalidation. |
| 5 | Add urine-data caveat to F section | MUST_FIX/SHOULD_FIX | T objectives/key relationships explicitly include urine-based estimation. |
| 6 | Correct PK2 V = 26 vs source V = 20 handling | MUST_FIX | Draft currently uses arithmetic result as answer despite source contradiction. |
| 7 | Remove `CV% 3400` from PK2 Solution I discussion | MUST_FIX | 3400% belongs to PK3 Table 3.1. |
| 8 | Correct `6배 변동` for V/F 32→6.54 | MUST_FIX | Arithmetic error; source says 6.54 vs 30 L, not sixfold. |
| 9 | Correct Self-test Q5 half-life logic | MUST_FIX | Internal mathematical inconsistency. |
| 10 | Correct Self-test Q8 half-life/flip-flop logic | MUST_FIX | Internal mathematical inconsistency. |
| 11 | Remove/tag ICH M9/FDA/deficiency letter statements | MUST_FIX | Not in source and external verification forbidden by task. |
| 12 | Correct `AUC = ... = D/CL_true` algebra | MUST_FIX | Incorrect relation; source relation is `AUC = F·Dose/CL = Dose/(CL/F)`. |
| 13 | Add T Table 6-1 parameter-estimation example | SHOULD_FIX | High-yield author example for plasma/urine/absolute F. |
| 14 | Add T Fig.6-5 dose proportionality message | SHOULD_FIX | Prevents misleading Cmax-dose interpretation. |
| 15 | Add T Figs.6-8/6-9 examples | SHOULD_FIX | Strong route/formulation examples for distinguishing absorption vs disposition limitation. |
| 16 | Add G Fig.2.32 view instruction in Phase 4C | SHOULD_FIX | Author’s summary visual for determinants of oral curve. |
| 17 | Keep Vaughan/Pidgeon-Pitlick omitted | OPTIONAL | Scope-limiting omission acceptable under B-Standard. |
| 18 | Keep local BE/topical microdialysis omitted | OPTIONAL/REJECT for core | Scope creep relative to F·ka·tmax core. |
| 19 | Keep Ch7 BCS as 1–2 sentence context only | OPTIONAL | Appropriate compression; avoid expanding into full Ch7 absorption physiology. |

---

# T5: Coverage Audit

## T5-A. Section Headings / Structural Elements

| PDF Element | Type | PDF Location | Step 1 Status | Omission Verdict | Required Action |
|---|---|---|---|---|---|
| G §2.2.4 Extravascular administration | H2 | G pp.28–32 | INCLUDED_AS_MUST | — | Keep. |
| G §2.2.5 Estimation from first-order input | H2 | G pp.32–35 | INCLUDED_AS_CONTEXT/MUST | — | Keep; Figure 2.19/2.20 view later. |
| G Alternative methods: Pidgeon-Pitlick, Vaughan | Subsection/content | G p.36 | OMITTED_JUSTIFIABLE | Low depth for B-Standard | No action unless advanced appendix. |
| G ka=K limiting case | Content | G pp.37–38 | INCLUDED_AS_CONTEXT | — | Keep. |
| G §2.2.6 Zero-order input | H2 | G pp.38–39 | INCLUDED_AS_CONTEXT | — | Keep; preserve non-proof caveat. |
| G §2.2.7 Apparent absorption rate constant | H2 | G pp.40–41 | INCLUDED_AS_MUST | — | Keep. |
| G §2.2.8 Estimation of bioavailability | H2 | G pp.41–42 | INCLUDED_AS_MUST | — | Keep. |
| G §2.2.9 How input varies | H2 | G p.43 | INCLUDED_AS_CONTEXT | — | No expansion required. |
| G §2.2.10 Multiple dosing | H2 | G pp.43–45 | INCLUDED_AS_CONTEXT | — | Good as dependency only. |
| G §2.2.11 Absorption from multiple sites | H2 | G pp.46–47 | INCLUDED_AS_CONTEXT | — | Keep as one-sentence context. |
| G §2.2.12 Conclusions | H2 | G p.47 | PARTIAL | MISSING_AUTHOR_MSG | Add G conclusion / Fig.2.32 view instruction. |
| G PK2 Case Study | Worked case | G pp.476–482 | INCLUDED_AS_MUST | — with errors | Fix V/F/F/V and 3400% issue. |
| G PK3 Case Study | Worked case | G pp.483–486 | INCLUDED_AS_CONTEXT/MUST | — | Keep. |
| T Ch.6 Objectives | Chapter opening | T p.169 | PARTIAL | MISSING_AUTHOR_MSG | Add urine-data and parameter-estimation objectives if final deck needs completeness. |
| T Routes of extravascular administration | H2 | T pp.169–170 | INCLUDED_AS_CONTEXT | — | Keep compressed. |
| T Kinetics of absorption | H2 | T pp.170–172 | INCLUDED_AS_MUST | — | Keep. |
| T Exposure-time and exposure-dose relationships | H2 | T pp.172–174 | PARTIAL | MISSING_BRIDGE | Add absorption delays/lower peak and dose proportionality. |
| T Changes in dose/absorption kinetics | H2 | T pp.174–178 | INCLUDED_AS_MUST/PARTIAL | MISSING_EXAMPLE | Add Fig.6-5, 6-8, 6-9 examples if possible. |
| T Changing disposition kinetics | H2 | T pp.177–180 | WEAK | MISSING_BRIDGE | Add brief CL/V effect context if discussing tmax/Cmax/AUC. |
| T Assessment of product performance | H2 | T pp.181–183 | INCLUDED_AS_CONTEXT | — with tmax caveat | Keep BE criterion; soften tmax claim. |
| T Assessment of PK parameters | H2 | T pp.183–188 | PARTIAL | MISSING_CRITICAL | Add Table 6-1 and urine-data caveat. |
| T Key Relationships | Box summary | T p.189 | PARTIAL | MISSING_AUTHOR_MSG | Ensure F, Frel, urine equations represented or acknowledged. |
| T Study Problems | Exercises | T pp.190–195 | OMITTED_JUSTIFIABLE | Low relevance | No action. |
| T Ch.7 Absorption | Chapter | T pp.197–220 | INCLUDED_AS_CONTEXT | — but source header error | Add source header; keep compressed. |
| T Appendix F Method of Residuals | Appendix | T pp.781–784 | INCLUDED_AS_CONTEXT | — | Keep. |

## T5-B. Numbered Formula Inventory

| PDF Element | Type | PDF Location | Step 1 Status | Omission Verdict | Required Action |
|---|---|---|---|---|---|
| G Eq.2:32–2:35 | ODE + integrated first-order oral model | G p.30 | INCLUDED_AS_MUST | — | Keep. |
| G Eq.2:36–2:38 | AUC derivation from Eq.2:35 | G p.31 | PARTIAL | MISSING_BRIDGE | Optional: cite if AUC/F bridge feels abrupt. |
| G Eq.2:39 | Lag-time model | G p.32 | INCLUDED_AS_CONTEXT/MUST | — | Keep. |
| G Eq.2:40–2:42 | Residual method / tlag | G pp.32–33 | INCLUDED_AS_CONTEXT | — | Keep. |
| G Eq.2:43–2:46 | Fraction eliminated examples | G p.34 | OMITTED_JUSTIFIABLE | Low relevance | No action. |
| G Eq.2:47–2:55 | tmax/Cmax derivation | G pp.34–35 | INCLUDED_AS_MUST | — | Keep. |
| G Eq.2:56–2:57 | Pidgeon-Pitlick/Vaughan | G p.36 | OMITTED_JUSTIFIABLE | Low relevance | No action. |
| G Eq.2:58–2:65 | ka=K limiting case | G pp.37–38 | INCLUDED_AS_CONTEXT | — | Keep compressed. |
| G Eq.2:66–2:67 | Zero-order input | G p.38 | INCLUDED_AS_CONTEXT | — | Keep. |
| G Eq.2:68–2:70 | apparent vs true ka / F | G pp.40–41 | INCLUDED_AS_MUST | — | Keep. |
| G Eq.2:71–2:74 | IV+oral fitting / F | G pp.42 | INCLUDED_AS_MUST | — | Keep. |
| G Eq.2:75–2:79 | multiple dosing / accumulation | G pp.44–45 | INCLUDED_AS_CONTEXT | — | No expansion required. |
| G Eq.2:80–2:82 | multiple absorption sites | G pp.46–47 | INCLUDED_AS_CONTEXT | — | Keep one-sentence context. |
| G PK2 Eq.2:1–2:4 | case-specific oral lag/residual formulas | G pp.477–479 | PARTIAL | MISSING_EXAMPLE | Only needed for case detail; current coverage sufficient. |
| G PK3 Eq.3:1–3:3 | case-specific first/zero-order fitting and CL0 | G pp.484–485 | PARTIAL | MISSING_EXAMPLE | Sufficient for Phase 1 if PK3 table retained. |
| T Eq.6-1–6-2 | absorption t½ and rate | T pp.170–171 | INCLUDED_AS_CONTEXT | — | Keep/optional. |
| T Eq.6-3–6-8 | mass balance and rate-limitation/flip-flop | T pp.172–175 | INCLUDED_AS_MUST | — | Correct Eq.6-3 citation. |
| T Eq.6-9–6-17 | plasma F/Frel and parameter estimation | T pp.183–186 | PARTIAL | MISSING_CRITICAL | Add Table 6-1 / oral-only parameter caveat. |
| T Eq.6-18–6-21 | urine data, F, CLr | T pp.187–188 | OMITTED_PROBLEMATIC | MISSING_CRITICAL | Add at least one caveat sentence. |
| T Ch.7 Eq.7-1 etc. | first-pass/mechanistic F | T Ch.7 | INCLUDED_AS_CONTEXT | — source header issue | Fix header. |
| T Appendix F Eq.F-1–F-6 | residual method and tmax | T pp.782–783 | INCLUDED_AS_CONTEXT/MUST | — | Use as correct T integrated-solution source. |

---

# T6: Figure Inventory & Learning Value Audit

**Inspection note:** PDF page renders and embedded figure images were reviewed where available. Value ratings are conservative. `ESSENTIAL` is used only where the figure materially prevents conceptual misunderstanding.

## T6-A. Gabrielsson & Weiner Figures/Tables

| Figure/Table | Page | Teaches | Value | View Instruction? | Redraw/New Schematic? | Inspection Method | Rationale |
|---|---:|---|---|---|---|---|---|
| Fig.2.14 | G p.28 | Infusion rate vs clearance effects on steady state and time to steady state | USEFUL | NO | NO | VISUAL_INSPECTED | Pre-extravascular carryover; useful but not core. |
| Fig.2.15 | G p.29 | Gut compartment first-order input into plasma with elimination | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Core model structure for Card 1. |
| Fig.2.16 | G p.29 | Same compound/dose by IV/SC/IP routes in rats; route variability | USEFUL | NO | NO | VISUAL_INSPECTED | Good empirical anchor, not required for equations. |
| Fig.2.17 | G p.30 | Parallel vs non-parallel IV/PO terminal slopes; flip-flop | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Central to Card 4. |
| Fig.2.18 | G p.31 | Lag-time intersection of residual and terminal slopes | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Required for lag-time visual understanding. |
| Fig.2.19 | G p.33 | Method of residuals for absorption rate constant | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Required for residual method. |
| Fig.2.20 | G p.33 | Graphical estimation of tlag | USEFUL | YES | NO | VISUAL_INSPECTED | Reinforces Fig.2.18/2.19. |
| Table 2.2 | G p.34 | Initial estimates for K, Ka, V/F, tlag | USEFUL | YES | NO | VISUAL_INSPECTED | Practical estimation table. |
| Fig.2.21 | G p.36 | Pidgeon-Pitlick method | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Scope-deep alternative method. |
| Fig.2.22 | G p.36 | Vaughan method | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Scope-deep alternative method. |
| Fig.2.23 | G p.39 | First-, zero-, mixed-order input by dose/solubility | USEFUL | YES | YES | VISUAL_INSPECTED | Helps distinguish zero-order vs first-order. |
| Fig.2.24 | G p.40 | Ka,app vs Ka,true and gut loss/degradation | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Core for Card 5. |
| Fig.2.25 | G p.41 | F and Ka effects on gut loss/input profile | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Shows F changes input rate relative to gut loss. |
| Fig.2.26 | G p.42 | Sequential IV/PO dosing for F estimation and nonstationarity risk | USEFUL | YES | NO | VISUAL_INSPECTED | Supports F estimation assumptions. |
| Fig.2.27 | G p.43 | Typical input rates and plasma profiles | USEFUL | NO | NO | VISUAL_INSPECTED | Helpful but broad. |
| Fig.2.28 | G p.44 | Repeated dosing and approach to steady state | USEFUL | NO | NO | VISUAL_INSPECTED | Dependency for next session. |
| Fig.2.29 | G p.45 | Flip-flop under repeated dosing / clearance contrasts | USEFUL | YES | YES | VISUAL_INSPECTED | Useful if multiple-dose flip-flop risk retained. |
| Fig.2.30 | G p.46 | AUC over dosing interval at steady state | USEFUL | NO | NO | VISUAL_INSPECTED | Next-session bridge. |
| Fig.2.31 | G p.46 | Two-site absorption and double peak | USEFUL | YES | YES | VISUAL_INSPECTED | Good for multiple peak caution. |
| Fig.2.32 | G p.47 | Determinants of oral concentration-time curve | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Author’s conclusion summary; should be used in Phase 4C. |
| PK2 Fig.2.1 | G p.476 | Oral data for drug A | USEFUL | YES | NO | VISUAL_INSPECTED | Case anchor. |
| PK2 Table 2.1 | G p.478 | Oral/IV data, input rate, cumulative input | USEFUL | YES | NO | VISUAL_INSPECTED | Supports deconvolution/F inconsistency. |
| PK2 Fig.2.2 | G p.478–479 | Residual/terminal slope for case | USEFUL | YES | NO | VISUAL_INSPECTED | Supports initial estimates. |
| PK2 Table 2.2 | G p.479 | Initial estimates for case | USEFUL | YES | NO | VISUAL_INSPECTED | Practical anchor. |
| PK2 Fig.2.3 | G p.480 | Lag-time vs no-lag model fit | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Shows why lag-time improves fit. |
| PK2 Fig.2.4 | G p.481 | Input function/cumulative input from deconvolution | USEFUL | YES | NO | VISUAL_INSPECTED | Supports F discrepancy audit. |
| PK3 Fig.3.1 | G p.483–485 | First- vs zero-order model fit | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Supports model comparison. |
| PK3 Table 3.1 | G p.486 | Parameter estimates/CV% for first vs zero-order | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Source for CV/AIC interpretation. |

## T6-B. Rowland & Tozer Figures/Tables

| Figure/Table | Page | Teaches | Value | View Instruction? | Redraw/New Schematic? | Inspection Method | Rationale |
|---|---:|---|---|---|---|---|---|
| Fig.6-1 | T p.171 | First-order absorption as bucket emptying | USEFUL | NO | NO | VISUAL_INSPECTED | Good intuition but not essential given G model. |
| Fig.6-2 | T p.171 | Zero- vs first-order absorption in linear/semilog plots | USEFUL | YES | YES | VISUAL_INSPECTED | Supports confusion pair 4. |
| Fig.6-3 | T p.172 | Aspirin IV vs oral; oral delay/lower peak | USEFUL | YES | NO | VISUAL_INSPECTED | Missing author example. |
| Fig.6-4 | T p.173 | Integrated absorption-elimination reservoir model | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Strong conceptual bridge to tmax condition. |
| Fig.6-5 | T p.174 | Dose changes Cmax/AUC proportionally; tmax unchanged | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Needed to prevent dose-proportionality confusion. |
| Fig.6-6 | T p.176 | Absorption half-life cases A/B/C and flip-flop | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Core flip-flop figure. |
| Fig.6-7 | T p.177 | Fluticasone early tmax but slow absorption half-life | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Core example already included. |
| Fig.6-8 | T p.178 | Theophylline food/water changes absorption, not terminal half-life | USEFUL | YES | NO | VISUAL_INSPECTED | Should-fix example for discrimination. |
| Fig.6-9 | T p.178 | Penicillin G absorption rate-limited by formulation/route | USEFUL | YES | NO | VISUAL_INSPECTED | Should-fix example for absorption-limited case. |
| Fig.6-10 | T p.179 | Clearance effect on profile when absorption constant | USEFUL | YES | YES | VISUAL_INSPECTED | Helpful for CL/V effects. |
| Fig.6-11 | T p.180 | Volume effect on profile when absorption/CL constant | USEFUL | YES | YES | VISUAL_INSPECTED | Helpful for V effects. |
| Fig.6-12 | T p.181 | Bioequivalence/product performance profile comparison | USEFUL | YES | NO | VISUAL_INSPECTED | Supports BE discussion. |
| Fig.6-13 | T p.183 | BE vs BA confidence-interval declarations | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Source for 90% CI/0.80–1.25 criterion. |
| Fig.6-14 | T p.184 | IM/oral 500 mg plasma curves | USEFUL | YES | NO | VISUAL_INSPECTED | Missing parameter-estimation anchor. |
| Table 6-1 | T p.184 | Plasma/urine data and PK parameters after IM/oral/IV | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Critical for F/urine/CL examples. |
| Fig.6-15 | T p.186 | AUC up to/beyond tmax and fraction eliminated/remaining | USEFUL | YES | YES | VISUAL_INSPECTED | Helpful but not mandatory. |
| Fig.6-16 | T p.188 | Local exposure after topical products | SKIPPABLE | NO | NO | VISUAL_INSPECTED | BE scope extension. |
| Fig.6-17 | T p.189 | Dermal open-flow microperfusion | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Local BE scope extension. |
| Fig.6-18 | T p.190 | Microdialysis probe calibration | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Local BE scope extension. |
| Fig.6-19 | T p.191 | Study problem curves for F/ka/CL/V alterations | USEFUL | NO | YES | VISUAL_INSPECTED | Exercise; could be useful but not core. |
| Tables 6-2–6-7 | T pp.191–195 | Study-problem datasets | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Exercises; omit justified. |
| Fig.6-20 | T p.194 | Study problem concentration-time curves | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Exercise figure. |
| Fig.7-1 | T p.199 | pH partition/absorption of weak acids/bases | USEFUL | NO | NO | VISUAL_INSPECTED | Ch.7 context only. |
| Table 7-1 | T pp.200–202 | Extent of absorption for drugs | USEFUL | NO | NO | VISUAL_INSPECTED | Context only. |
| Fig.7-2 | T p.201 | Intestinal absorption/permeability | USEFUL | NO | NO | VISUAL_INSPECTED | Context only. |
| Fig.7-3 | T p.202 | Fraction absorbed vs permeability/region | USEFUL | NO | YES | VISUAL_INSPECTED | Context only; could support BCS if expanded. |
| Fig.7-4 | T p.203 | Griseofulvin/particle size or absorption illustration | USEFUL | NO | NO | VISUAL_INSPECTED | Context only. |
| Fig.7-5 | T p.204 | Grapefruit juice/simvastatin interaction | USEFUL | NO | NO | VISUAL_INSPECTED | Context only for first-pass/DDI. |
| Tables 7-2–7-4 | T pp.204–209 | First-pass/food-DDI data | USEFUL | NO | NO | VISUAL_INSPECTED | Context only. |
| Fig.7-6 | T p.208 | Hepatic extraction / first-pass schematic | USEFUL | NO | YES | VISUAL_INSPECTED | Supports F_H if expanded. |
| Fig.7-7 | T p.209 | Intestinal metabolism + efflux transporters | USEFUL | NO | YES | VISUAL_INSPECTED | Context only; not core Phase 1. |
| Tables 7-5–7-7 | T pp.211–214 | IM/SC and solid dosage/formulation factors | USEFUL | NO | NO | VISUAL_INSPECTED | Context only. |
| Fig.7-8 | T p.213 | Solid dosage form dissolution/absorption chain | USEFUL | NO | YES | VISUAL_INSPECTED | Could be one schematic if formulation context retained. |
| Fig.7-9 | T p.215 | Gastric emptying influence | USEFUL | NO | NO | VISUAL_INSPECTED | Context only. |
| Fig.7-10 | T p.216 | Gastric emptying/food effect example | USEFUL | NO | NO | VISUAL_INSPECTED | Context only. |
| Fig.7-11 | T p.218 | Gastroretentive system / gastric emptying | USEFUL | NO | NO | VISUAL_INSPECTED | Context only. |
| Fig.7-12 | T p.218 | Absorption window/gastroretentive design | USEFUL | NO | NO | VISUAL_INSPECTED | Context only. |
| Table 7-8 | T p.219 | BCS 2×2 matrix | USEFUL | YES | NO | VISUAL_INSPECTED | Best single Ch.7 context figure/table for BCS. |
| Table 7-9 | T p.220 | BCS Class I examples | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Detail not required. |
| Table F-1 | T p.781 | Residual method calculation table | USEFUL | YES | NO | VISUAL_INSPECTED | Supports Appendix F method. |
| Fig.F-1 | T p.782 | Residual line and lag-time | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Strong method-of-residuals visual. |
| Table F-2 | T p.783 | Study problem plasma concentrations | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Exercise dataset. |

---

# Patch Memo Independent Classification

| Patch memo item | Audit classification | Decision |
|---|---|---|
| MUST 5 cards appropriate | MATCH | Accept. |
| Apex = V/F + flip-flop | MATCH | Accept. |
| Need Phase 2 before HTML | MATCH | Accept. |
| Source B should include Ch.7 | ERROR in Draft | Accept patch. |
| T Eq.6-3 misidentified | ERROR in Draft | Accept patch. |
| Flip-flop intuitive sentence risky | ERROR in Draft | Accept patch. |
| “IV 없이는 V·F·ka·kel 전부 진짜 아님” too strong | ERROR/overstatement | Accept patch. |
| F estimation should mention urine data | MATCH | Accept patch. |
| Regulatory/NDA expressions should be tagged | NOT_IN_SOURCE | Accept patch; some should be rejected unless separately sourced. |
| Zero-order better fit ≠ true zero-order proof | MATCH | Already handled well; keep. |

---

# Final Audit Decision

**Go to Phase 4A only after MUST_FIX patch. Do not proceed directly to HTML.**

Draft v0 is not a rewrite failure. It is a strong Phase 1 conceptual draft with source-backed core spine. However, source fidelity is not clean enough for final HTML because several statements would cause false learning: especially T Eq.6-3 citation, flip-flop terminal half-life logic, PK2 V/F arithmetic/source conflict, and unsupported regulatory assertions.

**Recommended next operation:** `Phase 4A Integration & Compression Patch`, using this audit as the mandatory correction list. Phase 4C figure handling should explicitly instruct learners to inspect G Fig.2.17, G Fig.2.24/2.25, G Fig.2.32, T Fig.6-5, T Fig.6-6, T Fig.6-7, T Fig.6-13, and T Fig.F-1.

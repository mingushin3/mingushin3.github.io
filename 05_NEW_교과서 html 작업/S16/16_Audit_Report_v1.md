# 16_Audit Report v1 — Source Fidelity Audit

**업무 형태**: 파일 분석 / 웹 검색 OFF / PDF 대조 감사  
**입력**: `016_G_임상 통합·패턴인식 TDM·질환·캡스톤(1).pdf` + `016_T_임상 통합·패턴인식 TDM·질환·캡스톤_01(1).pdf` + `016_T_임상 통합·패턴인식 TDM·질환·캡스톤_02(1).pdf` + `16_step1_draft_v0(1).md` + `S16_phase1_patch memo.md`  
**산출**: `16_Audit Report v1`  
**감사 역할**: Source Fidelity Auditor — 문장 개선·비유 추가·교육적 재작성 금지, 원문 근거 대조만 수행  
**Figure inspection**: PDF rendered contact sheets visually inspected. Figure/Table entries below use `VISUAL_INSPECTED` unless explicitly marked otherwise.

## Executive Audit Verdict

**판정: CONDITIONAL GO to Phase 3/4A after MUST_FIX patch. HTML 직행은 금지.**

Draft v0는 Gabrielsson Ch.6의 pattern-recognition 기반 model-class narrowing, PK35의 Bayesian individual parameter estimation, PK15의 toxicokinetic exposure reporting, Rowland & Tozer Ch.15의 disease/renal impairment/dialysis adjustment, Ch.18의 initiating/managing therapy와 target concentration strategy를 하나의 clinical capstone spine으로 통합한 점은 대체로 성공적이다.

다만 다음 항목은 Source Fidelity 기준에서 반드시 수정해야 한다.

1. **Peak-shift deterministic overclaim**: `좌/우 방향이 곧 모델 클래스`는 원문보다 강함. 원문은 potential models를 평가하는 pattern-recognition framework이다.
2. **TCS 필수 적용 과장**: phenytoin/digoxin/vancomycin/cyclosporine 등을 “필수”처럼 단정하면 원문보다 강함. Ch.18은 criteria가 충족될 때 유용한 adjunct strategy로 설명한다.
3. **Loading-dose 예측 정확도 수치**: `V 5–10%`, `CL 30–40%`는 Fig.18-5의 qualitative variability partition에서 직접 산출되는 수치가 아님. Draft 방식의 “정확도” 표현은 NOT_IN_SOURCE 또는 RESTORED[확인 필요].
4. **Q8 digoxin 처방 권고**: PK35는 CL/V/t½ Bayesian estimation 사례이며, `loading 0.4 mg`, `maintenance 0.1–0.125 mg/day`, `NDA Briefing Document` 문구는 원문 직접 처방 권고가 아님.
5. **TDM 환자 80% claim**: “임상 TDM 80% 처리”는 첨부 PDF에서 직접 확인되지 않음.
6. **NONMEM/BestDose/ID-ODS/Pmetrics/NDA/IND/RMP**: 원문 직접 근거가 아니라 현대 구현·규제 번역. 유지하려면 `[교과서 외 구현/규제 번역]` 라벨 필요.
7. **Ch.6 Fig.6.12 omission**: Figure 6.12 guidance flow-chart는 pattern-recognition workflow의 통합 figure인데 Draft에서는 충분히 반영되지 않음. SHOULD_FIX.
8. **MUST 12개 과밀**: Source 오류는 아니지만 `MUST` test를 원문 기준으로 재적용하면 Rd/Cockcroft/Hemodialysis는 하나의 disease-adjusted dosing card로 통합 가능. Content Lock 단계에서 압축 필요.

---

## T1: Equation/Numerical Audit

| Item | Draft v0 Expression | PDF Source | Classification | Correction |
|---|---|---|---|---|
| Pattern-recognition 4축 | baseline / time-delay / peak-shift / saturation-slope 중심 | G p.423, Fig.6.1 | MATCH | 수정 불필요. 다만 Fig.6.12 workflow도 함께 반영 필요. |
| `60초 내 모델 클래스 좁히기` | 학습 목표: 4축 패턴 인식으로 60초 내 모델 클래스 좁히기 | G Ch.6 | NOT_IN_SOURCE | 교육용 시간 제한 수치. 유지 시 `[교육용 운영 목표]`로 라벨. |
| Peak-shift directionality | `좌/우 방향이 곧 모델 클래스` | G p.424–428, Fig.6.2–6.3 | ERROR / OVERCLAIM | 원문은 left/right shift로 competing models를 평가한다. `곧 모델 클래스`가 아니라 `모델 후보를 좁히는 1차 진단 신호`로 낮출 것. |
| Case A plasma peak timing | plasma peak occurs at about 1/3 of time of Rmin | G p.424, Fig.6.2 | MATCH | 수정 불필요. |
| Case B leftward shift | higher dose trough shifted left | G p.424–425, Fig.6.2–6.3 | MATCH | 단, model selection 확정 규칙처럼 쓰지 말 것. |
| Case C rightward shift + flat portion | highest dose trough shifted right; flat portion indicates saturation | G p.424–425, Fig.6.2–6.3 | MATCH | 수정 불필요. |
| Turnover inhibition of input | `dR/dt = kin·I(C) − kout·R` | G p.425, Eq.6:1 | MATCH | 수정 불필요. |
| I(C) variants | nonlinear/linear inhibitory mechanism functions | G p.425, Eq.6:2 | MATCH | 수정 불필요. |
| Stimulation of loss | `dR/dt = kin − kout·R·S(C)` style | G p.425–426, Eq.6:3–6:4 | MATCH | 수정 불필요. |
| Effect compartment/link model | `dCe/dt = ke0·(C − Ce)` style, inhibitory Emax with E0 | G p.426, Eq.6:5–6:6 | MATCH | 수정 불필요. |
| Receptor on/off model | second-order binding / koff loss logic | G p.426–427, Eq.6:7–6:8 | MATCH | 수정 불필요. |
| Antagonistic metabolite | alternative instantaneous model | G p.427, Eq.6:9 | MATCH if included as context | 전용 MUST로 올릴 필요는 낮음. |
| Fig.6.4 Case A–I | individual response-time signatures | G p.429–437, Fig.6.4 | MATCH / OVERDENSE | 개별 case equations는 CONTEXT로 충분. |
| Fig.6.5 Case A–I | concentration-response / response-time pattern cases | G p.437–442, Fig.6.5 | MATCH / OVERDENSE | 본문 과밀 시 representative cases만 남겨도 됨. |
| Fig.6.6 Case A–I | route/absorption/delay/tolerance pattern examples | G p.442–447, Fig.6.6 | MATCH / OVERDENSE | 개별 equations를 전수 설명하면 Step 1 과밀. |
| Fig.6.12 workflow | guidance flow-chart: plot C/R vs time, C-R plot, direct/indirect/rebound/tolerance 등 분기 | G p.465–466, Fig.6.12 | MISSING / SHOULD_FIX | Draft의 4축 decision algorithm에 Fig.6.12가 구조적으로 더 직접적이다. |
| PK15 toxicokinetic doses | 10 / 56 / 320 µmol·day⁻¹·kg⁻¹ | G PK15 p.546–548, Fig.15.1–15.3 | MATCH | 수정 불필요. |
| PK15 Cmax anchor | `Cmax ~50 µM` | G PK15 p.546–548 | MATCH if source context retained | 자료 내 high-dose exposure anchor로 유지 가능. |
| PK15 therapeutic concentration | `0.05–0.1 µM`; `>100배 안전역` | G PK15 p.546–548 | MATCH with caveat | 원문 toxicokinetic interpretation 맥락에서만 사용. `NDA 규제 언어`는 source 밖. |
| PK35 Bayesian objective function | population prior + concentration likelihood form | G PK35 p.641–643, Eq.35:1–35:4 | MATCH | 수정 불필요. |
| PK35 no concentration / no prior / full Bayesian extremes | three cases in Bayesian interpretation | G PK35 p.641–643 | MATCH | 수정 불필요. |
| PK35 digoxin demographics | 55-year-old, 60 kg male CHF patient | G PK35 p.641–643 | MATCH | 수정 불필요. |
| PK35 Lanoxicap dose | 0.2 mg | G PK35 p.641–643 | MATCH | 수정 불필요. |
| PK35 digoxin concentrations | 2.5 µg/L at 458 h; 0.9 µg/L at 479 h | G PK35 p.641–643 | MATCH | 수정 불필요. |
| PK35 population estimates | CLpop 1.8 L/h, Vpop 500 L | G PK35 p.641–643 | MATCH | 수정 불필요. |
| PK35 final estimates | CL 5.7 L/h, V 119.6 L, t½ 14.5 h | G PK35 p.641–643 | MATCH | 수정 불필요. |
| PK35 clinical prescription | loading dose 0.4 mg divided; maintenance 0.1–0.125 mg/day | G PK35 + T Ch.18 principles | NOT_IN_SOURCE as direct claim | 원문 직접 처방 권고 아님. `[교과서 외 통합 추론 예시]`로 라벨. |
| Rd framework | `Rd = RF·fe + 1 − fe` | T15 p.453, Eq.15-8 | MATCH | 수정 불필요. |
| Full Rd with age/weight | `Rd = RF·fe(t) + [1−fe(t)]·((140−Age)·Wt^0.75/1936)` | T15 p.452–453, Eq.15-7 | MATCH if full version included | 간단형은 “typical에서 크게 벗어나지 않는 환자” caveat 필요. |
| fe definition | fraction of i.v. dose recovered unchanged in urine | T15 p.453, Eq.15-9 | MATCH | 수정 불필요. |
| 30% renal adjustment rule | “30% 규칙으로 신부전 조정 대상 약물 분류” | T15 renal adjustment discussion; Fig.15-9 | RESTORED [확인 필요] | R&T는 Rd/fe/RF로 판단한다. `30% rule`은 명시적 문구가 아니면 heuristic으로 라벨. |
| Cockcroft-Gault adult equation | age, weight, sex, Scr 기반 | T15 p.457, Table 15-5 | MATCH | 수정 불필요. 비만/근감소 caveat 유지. |
| MDRD exclusion | MDRD not core; Cockcroft-Gault standard 유지 | T15 p.455–457, Table 15-4–15-5 | MATCH as curation | Draft의 의도적 제외는 정당. |
| Hemodialysis ineffective conditions | `Vu > 120 L`; if `CLu` much greater than `CLuD`, dialysis less effective; 400 mL/min threshold | T15 p.471–472, Fig.15-18 | MATCH with wording caveat | Draft의 `Vu<120 L AND CLu<CLuD`는 simplified gate. 원문은 continuous relation이며 hard AND rule이 아님. |
| Dialysis fraction equations | Eq.15-27–15-30 | T15 p.470–471 | MATCH if summarized | 수식 상세를 생략하면 CONTEXT로 충분. |
| Dialysis half-life equations | `t1/2(during)=0.693·Vu/(CLu+CLuD)`, `t1/2=0.693·Vu/CLu` | T15 p.472, Eq.15-31–15-32 | MATCH | 수정 불필요. |
| Supplemental dose | `Supplemental dose = V·C(0)·(e^{-kT} − e^{-kD T})` | T15 p.472, Eq.15-34 | MATCH | 수정 불필요. |
| Phenobarbital dialysis example | Vu=77 L, CLu=0.4 L/h, k=0.005 h⁻¹, t½=137 h, CLuD=150 mL/min=9 L/h, t½ during dialysis=5.7 h, dialysis accounts for 96% elimination but removes 29% in 3 h | T15 p.472 | MATCH if included | 유지 가능. |
| Gentamicin supplement | 40 mg initial, 12 mg every other day, 12 mg post-dialysis supplement | T15 p.473–474, Fig.15-20 | MATCH if included | 유지 가능. |
| Disease hepatic examples | cefetamet, meptazinol, verapamil Table 15-1 | T15 p.445–446, Table 15-1 | MATCH | 수정 불필요. |
| Meptazinol 400+% bioavailability | Draft: meptazinol 400+% increase | T15 p.446, Table 15-1 discussion | MATCH | 수정 불필요. |
| TCS criteria count | `5 criteria` | T18 p.594–597 | MATCH | 수정 불필요. |
| TCS “all/most criteria” | Draft: all 5 criteria / 필수 적용 | T18 p.594: “Most of them must be met” | ERROR / OVERCLAIM | “대부분 충족되어야 routine effective”로 수정. |
| Warfarin TCS non-applicability | Warfarin monitored by INR rather than plasma concentration | T18 p.594–596 discussion | MATCH | 수정 불필요. |
| Phenytoin TCS candidate | phenytoin monitoring useful, weekly in DDI context; Table 18-5 | T18 p.596–597, Table 18-5 | MATCH | `필수`가 아니라 `clinically helpful/useful candidate`. |
| Digoxin/vancomycin TCS examples | used throughout concentration monitoring examples | T18 p.597–599, Table 18-7 | MATCH | 수정 불필요. |
| TCS representative drugs | cyclosporine, sirolimus, phenytoin etc. | T18 p.595–596, Table 18-5 | MATCH | “필수 적용” 단정은 수정. |
| Loading dose equation | `D_L = V·Ctarget/F` | T18 p.584–586 principles | MATCH as standard PK approximation | 원문은 amount at plateau/bioavailability/target window framing. 식 자체는 적절하나 직접 equation numbering 없음. |
| LD depends on V | V/bioavailability drives loading dose; body weight important | T18 p.584–586 | MATCH | 수정 불필요. |
| Maintenance depends on CL | dosing rate/maintenance tied to clearance | T18 Ch.18 + prior chapters | MATCH | 수정 불필요. |
| V 5–10% / CL 30–40% “accuracy” | Draft claims LD estimation 5–10%, maintenance 30–40% | T18 Fig.18-5 is qualitative variability partition | NOT_IN_SOURCE / RESTORED [확인 필요] | 직접 수치로 잠그지 말 것. If retained, cite as Draft inference not PDF fact. |
| Fig.18-5 V/CL component percentages | V variability components and hepatic clearance unexplained components | T18 p.582, Fig.18-5 | MATCH if percentages visually read | “accuracy”로 변환하지 말 것. |
| Esmolol half-life | t½ about 9 min; LD needed in emergency | T18 p.584 | MATCH | 수정 불필요. |
| Mefloquine loading dose | 1250 mg (five 250-mg tablets); divided dose strategy | T18 p.584–585 | MATCH | 수정 불필요. |
| Amiodarone loading | 1000 mg initially, 500 mg 6–8 h later, 500 mg each day; t½ about 40 days | T18 p.585 | MATCH | 수정 불필요. |
| Flecainide titration | 50 mg q12h, increase 50 mg every 4 days | T18 p.585 | MATCH | 수정 불필요. |
| Valproic acid titration | 10–15 mg/kg/day; increase 5–10 mg/kg/week; usually <60 mg/kg/day | T18 p.585 | MATCH | 수정 불필요. |
| Terazosin titration | 1 mg bedtime; 2/5/10 mg stepwise; t½ about 12 h | T18 p.585 | MATCH | 수정 불필요. |
| Missed-dose Eq.18-1 | one missed dose subtraction from expected steady-state | T18 p.601, Eq.18-1 | MATCH | 수정 불필요. |
| Two missed doses Eq.18-2 | expected concentration after two consecutive missed doses | T18 p.601–602, Eq.18-2 | MATCH | 수정 불필요. |
| Digoxin missed-dose example | 60 y, 70 kg, CLcr=75 mL/min, F=0.8, V=441 L, CL=91 mL/min=5.46 L/h, k=0.0123 h⁻¹=0.3 day⁻¹, result 0.39 µg/L, therapeutic 0.8–2.0 µg/L | T18 p.602 | MATCH | 수정 불필요. |
| 9-13-17-21 Eq.18-3 | regular 24-h cycle with unequal intervals | T18 p.602–603, Eq.18-3 | MATCH | 수정 불필요. |
| Vancomycin pediatric 9-13-17-21 | 20 kg, 5-year-old, CLcr 55 mL/min, F=1.0, V=14 L, CL=3.3 L/h, k=0.24 h⁻¹, 250 mg regimen; 8:00 concentration 2.03 mg/L, therapeutic 5–15 mg/L | T18 p.602–603, Fig.18-12 | MATCH | 수정 불필요. |
| Erratic dosing Eq.18-4 | sum remaining from prior doses; disregard >4 patient half-lives | T18 p.604, Eq.18-4 | MATCH | 수정 불필요. |
| Vancomycin erratic example | 68 kg, 60-year-old male, SCr 2.2 mg/dL, CLcr 34 mL/min=2.06 L/h, V=42.2 L, k=0.049 h⁻¹, observed 34 mg/L vs predicted 33.7 mg/L | T18 p.604–605 | MATCH | 수정 불필요. |
| Confidence in estimates | early sample mainly V, late/plateau mainly CL; Fig.18-13 | T18 p.605–606, Fig.18-13 | MATCH | 수정 불필요. |
| `TDM 환자 80%` | Draft: “임상 TDM 80% 처리” | T18 missed/erratic dosing section | NOT_IN_SOURCE | 삭제하거나 “흔하다”로 낮출 것. |
| NONMEM $DES | 후속 영역 / model implementation | Attached PDFs | NOT_IN_SOURCE | `[교과서 외 구현 번역]` 라벨. |
| BestDose/ID-ODS/Pmetrics | Bayesian TDM software examples | Attached PDFs | NOT_IN_SOURCE | `[교과서 외 구현 번역]` 라벨. |
| NDA/IND/RMP wording | 규제 언어/보고 | Attached PDFs | NOT_IN_SOURCE | `[교과서 외 규제 번역]` 라벨. |
| Dose strengths warfarin 1/2/2.5/5/7.5/10 mg | Draft context | T18 Ch.18 text not clearly in provided excerpts | RESTORED [확인 필요] | 출처 직접 확인 전에는 source-locked claim 금지. |
| “PD 작업말 70%” | Turnover model card reason | Attached PDFs | NOT_IN_SOURCE | 교육용 강조 수치. 삭제 또는 `[교육용 추정]`. |

---

## T2: Examples & Data Audit

| Item | Draft v0 Status | PDF Location | Classification | Importance | Action |
|---|---|---|---|---|---|
| Gabrielsson Fig.6.1 general points | Included conceptually as 4축 | G p.423, Fig.6.1 | INCLUDED_CORRECT | HIGH | 유지. |
| Gabrielsson Fig.6.12 guidance flow-chart | Under-reflected | G p.465–466, Fig.6.12 | MISSING | HIGH | Pattern-recognition decision algorithm의 flow-chart source로 명시 필요. |
| Case A–C response-time profiles | Included | G p.424–428, Fig.6.2–6.3 | INCLUDED_CORRECT with caveat | HIGH | Directionality를 후보 축소 신호로 표현. |
| Case A effect compartment / turnover / receptor alternatives | Included | G p.425–427 | INCLUDED_CORRECT | HIGH | 유지. |
| Case B leftward peak-shift | Included | G p.428 | INCLUDED_CORRECT | HIGH | 유지하되 deterministic phrasing 수정. |
| Case C rightward peak-shift + saturation | Included | G p.428 | INCLUDED_CORRECT | HIGH | 유지. |
| Fig.6.4–6.6 Case A–I banks | Included as broad context | G p.429–447 | INCLUDED_CORRECT but overdense | MEDIUM | Full equation exposition는 Phase 4에서 압축. |
| PK15 toxicokinetics | Included as data anchor / deferred §6 | G p.546–548, Fig.15.1–15.3 | INCLUDED_CORRECT | MEDIUM | §6 또는 §8 closing bridge에 최소 anchor 유지. |
| PK15 NCA/safety margin | Included | G p.546–548 | INCLUDED_CORRECT with caveat | MEDIUM | `NDA 규제 언어` claim은 분리. |
| PK35 digoxin Bayesian model | Included | G p.641–643 | INCLUDED_CORRECT | HIGH | 유지. |
| PK35 direct prescription recommendation | Included in Q8-like integrated clinical recommendation | G PK35 + T Ch.18 principles | NOT_IN_SOURCE | HIGH | 원문 직접 권고가 아닌 통합 추론 예시로 라벨. |
| Hepatic disease — propranolol/cirrhosis | Included as disease contrast | T15 p.445, Fig.15-1 | INCLUDED_CORRECT | MEDIUM | 유지. |
| Cefetamet/meptazinol/verapamil table | Included | T15 p.445–446, Table 15-1 | INCLUDED_CORRECT | HIGH | 유지. |
| Child-Pugh score/amprenavir | Included as context | T15 p.447, Table 15-2/Fig.15-2 | INCLUDED_CORRECT | MEDIUM | 유지 가능. |
| CHF/lidocaine correlation | Included lightly or omitted | T15 p.449, Fig.15-4 | MISSING / OPTIONAL | LOW | Cardiovascular disease context에서 1문장 가능. |
| Cefepime renal impairment | Included lightly or omitted | T15 p.450, Fig.15-5 | MISSING / OPTIONAL | LOW | Rd framework의 clinical example로 optional. |
| Ceftazidime linear CL-CrCL | Included conceptually | T15 p.451, Fig.15-7 | INCLUDED_AS_CONTEXT | MEDIUM | 유지. |
| Amikacin renal impairment sketch | Included conceptually | T15 p.451, Fig.15-6 | INCLUDED_AS_CONTEXT | MEDIUM | 유지. |
| Rd/Fig.15-8–15-9 | Included as MUST | T15 p.452–454, Fig.15-8–15-9 | INCLUDED_CORRECT | HIGH | 유지. |
| Cockcroft-Gault | Included | T15 p.457, Table 15-5 | INCLUDED_CORRECT | HIGH | 유지. |
| Creatinine acute renal failure / delayed plateau | Included lightly or omitted | T15 p.458–461, Fig.15-10–15-13, Table 15-6 | MISSING / SHOULD_FIX | MEDIUM | Creatinine-based RF의 lag limitation으로 1–2문장 필요. |
| Digoxin CHF conditional prior | Included | T15 p.464, Table 15-7 | INCLUDED_CORRECT | HIGH | 유지. |
| Hemodialysis Fig.15-18 | Included | T15 p.471–472, Fig.15-18 | INCLUDED_CORRECT with caveat | HIGH | Hard AND gate로 표현하지 말 것. |
| Phenobarbital dialysis paradox | Included or implied | T15 p.472 | INCLUDED_CORRECT if present | HIGH | half-life shortened ≠ much removed message 유지. |
| Gentamicin supplement dose | Included or implied | T15 p.473–474, Fig.15-19–15-20 | INCLUDED_CORRECT if present | HIGH | Eq.15-34 worked example로 유지. |
| CAPD cefsulodin/teicoplanin | Included as context | T15 p.475–477, Fig.15-21–15-22 | INCLUDED_CORRECT | LOW | CONTEXT 유지. |
| Disease-on-PD Fig.15-23–15-25 | Included as moat/context | T15 p.480–481 | INCLUDED_CORRECT | LOW | §8 context로 충분. |
| Ch.18 Strategy 1 vs 2 | Included conceptually | T18 p.577–578, Fig.18-1 | INCLUDED_CORRECT | HIGH | 유지. |
| Pharmacodynamic variability/HER2/HLA examples | Included as context | T18 p.579, Fig.18-2 | INCLUDED_CORRECT | MEDIUM | 유지. |
| PK variability Table 18-1 | Included conceptually | T18 p.580 | INCLUDED_CORRECT | MEDIUM | 유지. |
| Fig.18-5 variability partition | Included with quantitative inference | T18 p.582, Fig.18-5 | INCLUDED_ERROR in inference | HIGH | component percentages only; `accuracy` claim 삭제/라벨. |
| Trimipramine CYP2D6 | Included | T18 p.583, Fig.18-6 | INCLUDED_CORRECT | MEDIUM | genotype-based prior example 유지. |
| Loading examples: esmolol, mefloquine, amiodarone | Included | T18 p.584–585 | INCLUDED_CORRECT | HIGH | 유지. |
| Titration examples: flecainide, valproic acid, terazosin | Included or available | T18 p.585 | INCLUDED_CORRECT if present | MEDIUM | LD vs titration contrast에 유용. |
| Table 18-2 monitoring matrix | Included conceptually | T18 p.587 | INCLUDED_CORRECT | HIGH | TCS logic에 반영. |
| Phenytoin stable concentration | Included or implied | T18 p.588, Fig.18-8 | INCLUDED_CORRECT if present | MEDIUM | TCS candidate example로 유지. |
| Table 18-3 monitoring by effects/tests | Included lightly | T18 p.589–590 | INCLUDED_CORRECT | MEDIUM | TCS와 response monitoring 대조에 유지. |
| Table 18-4 nonadherence | Included | T18 p.591 | INCLUDED_CORRECT | HIGH | 유지. |
| Fig.18-9 missed/makeup dose | Included conceptually | T18 p.592 | INCLUDED_CORRECT | HIGH | 유지. |
| Fig.18-10 doubling-up doses | Included | T18 p.593 | INCLUDED_CORRECT | MEDIUM | 유지. |
| Table 18-5 TCS drug information | Included | T18 p.595–596 | INCLUDED_CORRECT | HIGH | `필수` 단정 금지. |
| Table 18-6 data collection | Included or implied | T18 p.597 | MISSING / SHOULD_FIX | MEDIUM | TCS는 dose/time/adherence/sampling history mandatory. |
| Table 18-7 digoxin/vancomycin PK | Included | T18 p.598–599 | INCLUDED_CORRECT | HIGH | 유지. |
| Digoxin missed dose 0.39 µg/L | Included | T18 p.602 | INCLUDED_CORRECT | HIGH | 유지. |
| Vancomycin 9-13-17-21 2.03 mg/L | Included | T18 p.603 | INCLUDED_CORRECT | HIGH | 유지. |
| Vancomycin erratic dosing 33.7 vs 34 mg/L | Included | T18 p.604–605 | INCLUDED_CORRECT | HIGH | 유지. |
| Fig.18-13 confidence in estimates | Included | T18 p.605–606 | INCLUDED_CORRECT | HIGH | 유지. |
| Ch.18 study problems | Intentionally excluded | T18 p.606–610 | OMITTED_JUSTIFIABLE | LOW | §7 design 참고로만 충분. |

---

## T3: Author Key Messages

| Message | PDF Location | In Draft v0? | Status |
|---|---|---|---|
| Pattern recognition is pivotal for modeling kinetic/dynamic data; rigorous strategy is needed to dissect determinants of concentration/response-time courses. | G Ch.6 opening, p.423 | Yes | INCLUDED_CORRECT |
| Baseline, time delay, peak shift, saturation, slopes are general points to consider in response-time profiles. | G p.423, Fig.6.1 | Yes | INCLUDED_CORRECT |
| Ch.6 sections aim to interpret concentration-time, response-time, and concentration-response profiles and assess potential models. | G p.424 | Partly | SHOULD_FIX: “potential models” phrasing should soften deterministic model-class claims. |
| Alternative model solutions may explain the same pattern. | G Ch.6 throughout, esp. Case A alternatives | Partly | SHOULD_FIX: model selection should not be reduced to a single visual rule. |
| Fig.6.12 provides practical guidance: plot concentration/response vs time, combine in C-R plot, assess directness, delay, rebound, tolerance, etc. | G p.465–466 | Weak/absent | SHOULD_FIX: include as decision-algorithm source. |
| PK15 demonstrates NCA/toxicokinetic exposure evaluation with dose, AUC, Cmax patterns. | G PK15 p.546–548 | Yes as deferred anchor | INCLUDED_CORRECT |
| PK35 shows Bayesian estimation combines prior/population values and individual concentrations. | G PK35 p.641–643 | Yes | INCLUDED_CORRECT |
| Disease is a major source of variability in drug response, from PK and PD differences; therapy may need tailoring to disease severity and individual needs. | T15 p.444 | Yes | INCLUDED_CORRECT |
| Hepatic diseases are heterogeneous; half-life prolongation must not be equated directly with diminished hepatic metabolism because half-life depends on CL and V. | T15 p.444 | Partly | SHOULD_FIX if not explicit. |
| Renal disease dosage adjustment is most quantitative; fe and RF determine clearance reduction. | T15 p.444, p.452–454 | Yes | INCLUDED_CORRECT |
| Unbound clearance/concentration should be emphasized in renal disease because fu may vary. | T15 p.452 | Partly | SHOULD_FIX if total concentration language dominates. |
| Creatinine-based renal function estimates have assumptions and lags; acute renal failure/steady-state delay matter. | T15 p.457–461 | Weak | SHOULD_FIX as caveat. |
| Hemodialysis can alter drug removal; half-life reduction during dialysis is not equivalent to large fraction removed. | T15 p.471–472 | Yes | INCLUDED_CORRECT |
| Ch.18 therapy can be initiated by individualized usual regimen or low-dose titration strategy. | T18 p.577–578, Fig.18-1 | Yes | INCLUDED_CORRECT |
| Choosing dose/loading/dosing rate is best when sources of variability and patient-specific correlates are understood. | T18 p.579 | Yes | INCLUDED_CORRECT |
| Loading dose may be needed for long half-life drugs needing rapid effect, but may be omitted or divided because of adverse reactions and PD time course. | T18 p.584–585 | Yes | INCLUDED_CORRECT |
| Plasma concentration monitoring is useful only under criteria; most criteria must be met for routine effectiveness. | T18 p.594–597 | Yes but too strong in places | MUST_FIX: “필수” and “all criteria” wording must be softened. |
| Target concentration should be chosen based on greatest probability of therapeutic success and adjusted for severity/protein binding where relevant. | T18 p.596–597 | Partly | SHOULD_FIX if absent. |
| Dose history and sampling time are mandatory for interpreting measured concentrations. | T18 p.596–597, Table 18-6 | Partly | SHOULD_FIX. |
| Missed doses can be handled by subtracting the contribution from the missed dose, based on additivity/superposition. | T18 p.601–602 | Yes | INCLUDED_CORRECT |
| Unequal/erratic dosing can be interpreted by summing residual contributions from previous doses. | T18 p.604 | Yes | INCLUDED_CORRECT |
| Confidence in parameter estimates depends on sampling time; early concentration informs V, later/plateau informs CL. | T18 p.605–606, Fig.18-13 | Yes | INCLUDED_CORRECT |

---

## Patch Memo Cross-check

| Memo Item | Audit Classification | Rationale | Priority |
|---|---|---|---|
| MUST 12개는 HTML 학습문서로 과밀 | OPTIONAL / SHOULD_FIX | Source-fidelity error는 아니지만 원문상 MUST 모두가 독립 full card여야 하는 것은 아님. | SHOULD_FIX |
| Peak-shift 방향 = 모델 클래스 과장 | MATCH | G Ch.6는 potential models 평가 프레임. Draft의 “곧 모델 클래스”는 과장. | MUST_FIX |
| TCS 5 criteria 모두 충족 → 필수 적용 낮추기 | MATCH | T18 p.594는 “Most of them must be met” 및 adjunct strategy로 설명. | MUST_FIX |
| Loading dose V 5–10%, CL 30–40% 확인 | MATCH | Fig.18-5에서 직접 `accuracy`로 제시된 수치가 아님. | MUST_FIX |
| Q8 digoxin 처방 권고는 통합 추론 예시 | MATCH | PK35는 CL/V/t½ 추정 사례. 처방 권고는 교과서 직접 claim 아님. | MUST_FIX |
| TDM 환자 80% 삭제 | MATCH | 원문 직접 수치 없음. | MUST_FIX |
| NONMEM/BestDose/ID-ODS/Pmetrics/NDA/IND/RMP 분리 | MATCH | 첨부 교과서 직접 근거 아님. | MUST_FIX |
| PK15 최소 anchor 명확화 | MATCH | Source 오류는 아니지만 capstone closing bridge로 필요. | SHOULD_FIX |
| Phase 1 재실행 불필요 / Phase 2 필수 / HTML 직행 금지 | MATCH | Core coverage는 충분하나 source-unsupported claims 존재. | MUST_FIX before HTML |

---

## T4: Priority Summary (sorted: MUST_FIX → SHOULD_FIX → OPTIONAL → REJECT)

| # | Item | Priority | Rationale |
|---:|---|---|---|
| 1 | Peak-shift “방향이 곧 모델 클래스” | MUST_FIX | 원문은 potential models 평가. 결정론적 표현은 source overclaim. |
| 2 | TCS “필수 적용”/“all criteria” | MUST_FIX | 원문은 adjunct strategy이며 most criteria must be met. 약물명만으로 자동 적용 아님. |
| 3 | `V 5–10%`, `CL 30–40%` accuracy claim | MUST_FIX | Fig.18-5에서 직접 확인되는 것은 variability components이지 처방 정확도 수치가 아님. |
| 4 | PK35 digoxin loading/maintenance dose recommendation | MUST_FIX | 원문은 Bayesian CL/V/t½ estimation; 직접 처방 권고 아님. |
| 5 | `TDM 환자 80%` | MUST_FIX | 출처 직접 수치 없음. |
| 6 | NONMEM/BestDose/ID-ODS/Pmetrics/NDA/IND/RMP | MUST_FIX | 교과서 외 구현·규제 번역으로 라벨링 필요. |
| 7 | `NDA Exposure-Response wrong mechanism`, `NDA 규제 언어` | MUST_FIX | 원문 직접 표현 아님. 유지 시 `[교과서 외 실무/규제 해석]`. |
| 8 | Hemodialysis `Vu<120 AND CLu<CLuD` hard rule | MUST_FIX | 원문은 continuous relation과 illustrative threshold. Hard AND gate로 과도 단순화하면 오류. |
| 9 | Fig.6.12 guidance flow-chart underuse | SHOULD_FIX | Pattern-recognition algorithm의 직접 source. 누락은 학습 구조 약화. |
| 10 | Creatinine/RF lag and assumptions | SHOULD_FIX | Cockcroft-Gault 사용 전제와 acute renal failure delay caveat가 중요. |
| 11 | Table 18-6 data collection | SHOULD_FIX | TCS와 concentration interpretation의 mandatory input. |
| 12 | PK15 capstone closing bridge | SHOULD_FIX | 노출 보고로 세션을 닫는 구조가 약해질 수 있음. |
| 13 | MUST 12개 압축 | SHOULD_FIX | Source 오류는 아니나 Step 1 learner-facing Content Lock에 과밀. |
| 14 | Ch.6 Case A–I individual equations | SHOULD_FIX | Coverage는 좋지만 full-card exposition보다 representative context가 적합. |
| 15 | `PD 작업말 70%` | SHOULD_FIX | 출처 없는 비율. 삭제 또는 교육용 추정 라벨. |
| 16 | Dose strengths warfarin specific list | RESTORED [확인 필요] / SHOULD_FIX | 직접 source 확인 전에는 exact source claim 금지. |
| 17 | Ch.15 Study Problems | OPTIONAL | 핵심 source coverage에는 불필요. §7 디자인 참고 가능. |
| 18 | Ch.18 Study Problems | OPTIONAL | 핵심 source coverage에는 불필요. §7 디자인 참고 가능. |
| 19 | Direct textbook figure reproduction | REJECT | Image rights = None. Phase 4C는 독자적 schematic만 허용. |
| 20 | FDA/NDA wording as textbook message | REJECT | 첨부 source의 author message가 아니므로 source-fidelity 본문으로 잠그면 안 됨. |

---

## T5: Coverage Audit

| PDF Element | Type | PDF Location | Step 1 Status | Omission Verdict | Required Action |
|---|---|---|---|---|---|
| G Ch.6 Pattern recognition | H1 | G p.423 | INCLUDED_AS_MUST | OK | 유지. |
| G §6.1 Background | H2 | G p.423 | INCLUDED_AS_MUST | OK | “pattern recognition is pivotal” message 유지. |
| G Fig.6.1 general points | Figure | G p.423 | INCLUDED_AS_MUST | OK | View instruction YES. |
| G §6.1 Single and multiple response-time profiles I | H2 | G p.424 | INCLUDED_AS_MUST | OK | 유지. |
| G Fig.6.2 Case A–C | Figure | G p.424 | INCLUDED_AS_MUST | OK | View instruction YES. |
| G Eq.6:1–6:9 | Equations | G p.425–427 | INCLUDED_AS_MUST/CONTEXT | OK | 대표 수식 유지. |
| G Fig.6.3 model alternatives | Figure | G p.428 | INCLUDED_AS_MUST | OK | View instruction YES. |
| G §6.3 Single and multiple response-time profiles II | H2 | G p.429 | INCLUDED_AS_CONTEXT | OK | Case bank는 context. |
| G Fig.6.4 Case A–I | Figure | G p.429–437 | INCLUDED_AS_CONTEXT | OK | 과밀 방지. |
| G §6.4 / Fig.6.5 Case A–I | H2/Figure | G p.437–442 | INCLUDED_AS_CONTEXT | OK | 대표 사례만 유지 가능. |
| G §6.5 / Fig.6.6 Case A–I | H2/Figure | G p.442–447 | INCLUDED_AS_CONTEXT | OK | 대표 사례만 유지 가능. |
| G §6.6 / §6.9 beyond extracted pattern subsections | H2 | G p.447–465 subset | OMITTED_JUSTIFIABLE | Out of session core | Draft 의도적 제외 가능. |
| G Fig.6.12 guidance flow-chart | Figure | G p.465–466 | OMITTED_PROBLEMATIC | MISSING_BRIDGE | Decision algorithm source로 반영 필요. |
| G PK15 Toxicokinetics objectives | Case/Application | G p.546 | INCLUDED_AS_CONTEXT | OK | §6/§8 bridge로 유지. |
| G Fig.15.1 toxicokinetic C-t plots | Figure | G p.546–547 | INCLUDED_AS_CONTEXT | OK | View optional. |
| G Fig.15.2 dose-AUC | Figure | G p.548 | INCLUDED_AS_CONTEXT | OK | safety/exposure reporting. |
| G Fig.15.3 dose-Cmax | Figure | G p.548 | INCLUDED_AS_CONTEXT | OK | safety/exposure reporting. |
| G PK35 Bayesian model Digoxin | Case/Application | G p.641–643 | INCLUDED_AS_MUST | OK | 유지. |
| G Fig.35.1 variability impact | Figure | G p.641–642 | INCLUDED_AS_MUST | OK | Bayesian card view instruction useful. |
| G Eq.35:1–35:4 objective function | Equations | G p.641–643 | INCLUDED_AS_MUST | OK | 유지. |
| T15 Ch.15 Disease objectives | Objectives | T15 p.443 | INCLUDED_AS_CONTEXT | OK | session roadmap 반영. |
| T15 opening: disease as major variability source | Author message | T15 p.444 | INCLUDED_AS_MUST | OK | 유지. |
| T15 Impact of Disease on Pharmacokinetics | H1/H2 | T15 p.444 | INCLUDED_AS_MUST | OK | 유지. |
| T15 Hepatic Diseases | H2 | T15 p.444–449 | INCLUDED_AS_CONTEXT | OK | cirrhosis examples 유지. |
| T15 Fig.15-1 propranolol/cirrhosis | Figure | T15 p.445 | INCLUDED_AS_CONTEXT | OK | useful. |
| T15 Table 15-1 cefetamet/meptazinol/verapamil | Table | T15 p.446 | INCLUDED_AS_CONTEXT | OK | useful/high. |
| T15 Table 15-2 Child-Pugh | Table | T15 p.447 | INCLUDED_AS_CONTEXT | OK | optional. |
| T15 Fig.15-2 amprenavir/Child-Pugh | Figure | T15 p.447 | INCLUDED_AS_CONTEXT | OK | optional. |
| T15 Fig.15-3 conjugating enzymes | Figure | T15 p.448 | OMITTED_JUSTIFIABLE | LOW | hepatic disease detail. |
| T15 Cardiovascular Diseases | H2 | T15 p.449 | INCLUDED_AS_CONTEXT | OK | Sheiner/digoxin prior 연결. |
| T15 Fig.15-4 lidocaine/ICG clearance CHF | Figure | T15 p.449 | OMITTED_JUSTIFIABLE | LOW | optional. |
| T15 Renal Diseases | H2 | T15 p.450–466 | INCLUDED_AS_MUST | OK | 유지. |
| T15 Fig.15-5 cefepime renal function | Figure | T15 p.450 | INCLUDED_AS_CONTEXT | OK | optional/useful. |
| T15 Fig.15-6 amikacin renal impairment sketch | Figure | T15 p.451 | INCLUDED_AS_CONTEXT | OK | useful. |
| T15 Fig.15-7 ceftazidime CL-CrCL | Figure | T15 p.451 | INCLUDED_AS_CONTEXT | OK | useful. |
| T15 Eq.15-1–15-10 Rd derivation | Equations | T15 p.452–453 | INCLUDED_AS_MUST | OK | 유지. |
| T15 Fig.15-8, Fig.15-9 | Figures | T15 p.453–454 | INCLUDED_AS_MUST | OK | View instruction YES. |
| T15 CKD staging/MDRD/Cockcroft | Tables | T15 p.455–457, Table 15-3–15-5 | INCLUDED_AS_MUST/CONTEXT | OK | CG 유지; MDRD optional. |
| T15 Fig.15-10–15-13 creatinine kinetics | Figures/Table | T15 p.458–461 | OMITTED_PROBLEMATIC | MISSING_BRIDGE | RF estimation caveat로 1–2문장 필요. |
| T15 Fig.15-14 loading in renal disease | Figure | T15 p.462 | INCLUDED_AS_CONTEXT | OK | LD connection useful. |
| T15 Table 15-7 digoxin CHF | Table | T15 p.464 | INCLUDED_AS_CONTEXT | OK | PK35 prior connection. |
| T15 Table 15-8 renal/nonrenal CL | Table | T15 p.464–466 | INCLUDED_AS_CONTEXT | OK | optional. |
| T15 Hemodialysis | H1 | T15 p.466–475 | INCLUDED_AS_MUST | OK | 유지. |
| T15 Fig.15-16 hemodialysis system | Figure | T15 p.467 | INCLUDED_AS_CONTEXT | OK | useful. |
| T15 Eq.15-19–15-24 dialysis clearance | Equations | T15 p.467–469 | INCLUDED_AS_CONTEXT | OK | 상세는 optional. |
| T15 Fig.15-17 dialysis clearance variability | Figure | T15 p.470 | INCLUDED_AS_CONTEXT | OK | useful. |
| T15 Eq.15-27–15-34; Fig.15-18–15-20 | Equations/Figures | T15 p.470–474 | INCLUDED_AS_MUST | OK with caveat | Hard threshold 표현 수정. |
| T15 Peritoneal Dialysis | H1 | T15 p.475–477 | INCLUDED_AS_CONTEXT | OK | 1문장 context. |
| T15 Fig.15-21–15-22 | Figures | T15 p.475–477 | INCLUDED_AS_CONTEXT | OK | optional. |
| T15 Dialysis in Drug Overdose | H1 | T15 p.478–479 | OMITTED_JUSTIFIABLE | LOW | capstone core 아님. |
| T15 Impact of Disease on Pharmacodynamics | H1 | T15 p.480–481 | INCLUDED_AS_CONTEXT | OK | WHIG/biomarker moat. |
| T15 Fig.15-23–15-25 | Figures | T15 p.480–481 | INCLUDED_AS_CONTEXT | OK | optional. |
| T15 Key Relationships | Summary | T15 p.482 | INCLUDED_AS_CONTEXT | OK | source summary could be used. |
| T15 Study Problems / Tables 15-9–15-17 | Study problems | T15 p.483–489 | OMITTED_JUSTIFIABLE | LOW | §7 design 참고만. |
| T18 Ch.18 objectives | Objectives | T18 p.577 | INCLUDED_AS_CONTEXT | OK | roadmap 반영. |
| T18 Fig.18-1 two therapy strategies | Figure | T18 p.578 | INCLUDED_AS_MUST | OK | View instruction useful. |
| T18 Anticipating Sources of Variability | H1 | T18 p.579–583 | INCLUDED_AS_MUST/CONTEXT | OK | 유지. |
| T18 Fig.18-2 PD variability | Figure | T18 p.579 | INCLUDED_AS_CONTEXT | OK | useful. |
| T18 Table 18-1 PK variability | Table | T18 p.580 | INCLUDED_AS_CONTEXT | OK | useful. |
| T18 Fig.18-3–18-5 variability/covariate explanation | Figures | T18 p.581–582 | INCLUDED_AS_CONTEXT | OK but inference error | `accuracy` 변환 금지. |
| T18 Fig.18-6 trimipramine/CYP2D6 | Figure | T18 p.583 | INCLUDED_AS_CONTEXT | OK | 유지. |
| T18 Initiating Therapy | H1 | T18 p.584–586 | INCLUDED_AS_MUST | OK | LD/titration 유지. |
| T18 Loading Dose discussion | Section | T18 p.584–586 | INCLUDED_AS_MUST | OK | 유지. |
| T18 Dose titration examples | Section | T18 p.585 | INCLUDED_AS_CONTEXT | OK | LD vs titration contrast. |
| T18 Managing Therapy | H1 | T18 p.586–594 | INCLUDED_AS_MUST/CONTEXT | OK | 유지. |
| T18 Table 18-2 monitoring matrix | Table | T18 p.587 | INCLUDED_AS_MUST | OK | TCS logic. |
| T18 Fig.18-8 phenytoin | Figure | T18 p.588 | INCLUDED_AS_CONTEXT | OK | useful. |
| T18 Table 18-3 monitoring by effects/tests | Table | T18 p.589–590 | INCLUDED_AS_CONTEXT | OK | useful. |
| T18 Table 18-4 nonadherence | Table | T18 p.591 | INCLUDED_AS_CONTEXT | OK | 유지. |
| T18 Fig.18-9–18-10 nonadherence | Figures | T18 p.592–593 | INCLUDED_AS_CONTEXT | OK | useful. |
| T18 Discontinuing Therapy | H1 | T18 p.593–594 | INCLUDED_AS_CONTEXT | OK | tapering context. |
| T18 Target Concentration Strategy | H1 | T18 p.594–606 | INCLUDED_AS_MUST | OK with caveat | TCS 필수 표현 수정. |
| T18 Criteria for Monitoring Plasma Drug Concentrations | H2 | T18 p.594–597 | INCLUDED_AS_MUST | OK | 유지. |
| T18 Table 18-5 selected drug monitoring information | Table | T18 p.595–596 | INCLUDED_AS_MUST | OK | `clinically helpful`로 표현. |
| T18 Table 18-6 data collection | Table | T18 p.597 | OMITTED_PROBLEMATIC | MISSING_BRIDGE | dose/sampling history mandatory로 반영. |
| T18 Table 18-7 digoxin/vancomycin parameters | Table | T18 p.598–599 | INCLUDED_AS_MUST | OK | 유지. |
| T18 Eq.18-1–18-4 | Equations | T18 p.601–604 | INCLUDED_AS_MUST | OK | 유지. |
| T18 Fig.18-11–18-12 | Figures | T18 p.601–603 | INCLUDED_AS_MUST | OK | view instruction useful. |
| T18 Fig.18-13 confidence in estimates | Figure | T18 p.605–606 | INCLUDED_AS_MUST | OK | View instruction YES. |
| T18 Study Problems / Fig.18-14–18-16 | Study problems | T18 p.606–610 | OMITTED_JUSTIFIABLE | LOW | §7 design 참고 가능. |

---

## T6: Figure Inventory & Learning Value Audit

| Figure/Table | Page | Teaches | Value | View Instruction? | Redraw/New Schematic? | Inspection Method | Rationale |
|---|---:|---|---|---|---|---|---|
| G Fig.6.1 | 423 | Pattern-recognition checklist: baseline, time delay, peak shift, saturation, slopes. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Session 016 decision algorithm의 원천 figure. |
| G Fig.6.2 | 424 | Case A–C response-time patterns and dose-stage evolution. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Peak-shift directionality 판단의 핵심. |
| G Fig.6.3 | 428 | Competing model options for Case A–C. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | “하나의 pattern에 여러 model 후보” 메시지를 시각적으로 보여줌. |
| G Fig.6.4 | 429–437 | Nine response-time signature cases. | USEFUL | YES | YES | VISUAL_INSPECTED | 학습 확장에는 유용하나 전수 암기는 과밀. |
| G Fig.6.5 | 437–442 | Concentration-response/time-pattern cases. | USEFUL | YES | YES | VISUAL_INSPECTED | representative cases만 사용 권장. |
| G Fig.6.6 | 442–447 | absorption/route/delay/tolerance pattern cases. | USEFUL | YES | YES | VISUAL_INSPECTED | 여러 alternative patterns를 보여줌. |
| G Fig.6.12 | 465–466 | Practical analysis flow-chart for biological patterns. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Draft decision algorithm에 직접 반영되어야 하는 missing bridge. |
| G Fig.15.1 | 546–547 | Toxicokinetic concentration-time profiles by dose, sex, week. | USEFUL | NO | YES | VISUAL_INSPECTED | PK15 closing bridge에는 유용하나 core card는 아님. |
| G Fig.15.2 | 548 | Dose-AUC relationship in toxicokinetics. | USEFUL | NO | YES | VISUAL_INSPECTED | exposure proportionality anchor. |
| G Fig.15.3 | 548 | Dose-Cmax relationship in toxicokinetics. | USEFUL | NO | YES | VISUAL_INSPECTED | safety margin reporting anchor. |
| G Fig.35.1 | 641–642 | Variability in clearance affects concentration-time curves; Bayesian estimation context. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | PK35 Bayesian card에 구조적으로 필요. |
| T15 Fig.15-1 | 445 | Cirrhosis increases oral propranolol bioavailability. | USEFUL | NO | YES | VISUAL_INSPECTED | hepatic high-extraction contrast. |
| T15 Table 15-1 | 446 | Cefetamet/meptazinol/verapamil changes in cirrhosis. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | hepatic disease heterogeneity를 수치로 보여줌. |
| T15 Table 15-2 | 447 | Child-Pugh scoring. | USEFUL | NO | NO | VISUAL_INSPECTED | context. |
| T15 Fig.15-2 | 447 | Amprenavir AUC vs Child-Pugh score. | USEFUL | NO | YES | VISUAL_INSPECTED | disease severity-PK relation example. |
| T15 Fig.15-3 | 448 | Conjugating enzyme activities in normal/abnormal livers. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | 세션 core에서는 세부. |
| T15 Fig.15-4 | 449 | Lidocaine and ICG clearance correlation in CHF. | USEFUL | NO | YES | VISUAL_INSPECTED | cardiovascular disease context. |
| T15 Fig.15-5 | 450 | Cefepime profiles by renal function. | USEFUL | NO | YES | VISUAL_INSPECTED | renal function impact illustration. |
| T15 Fig.15-6 | 451 | Amikacin amount-time in normal vs reduced renal function. | USEFUL | YES | YES | VISUAL_INSPECTED | dose adjustment intuition. |
| T15 Fig.15-7 | 451 | Ceftazidime clearance vs creatinine clearance. | USEFUL | YES | YES | VISUAL_INSPECTED | CL-CrCL linear relation. |
| T15 Fig.15-8 | 453 | Renal/nonrenal/total unbound clearance vs RF for fe=0.8. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Rd framework를 시각적으로 가르침. |
| T15 Fig.15-9 | 454 | Rd and half-life dependence on RF and fe. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | fe/RF interaction의 핵심 figure. |
| T15 Table 15-3 | 455–456 | CKD staging/action plan. | USEFUL | NO | NO | VISUAL_INSPECTED | clinical context. |
| T15 Table 15-4 | 455–456 | MDRD equations. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Draft scope에서 의도적 제외 가능. |
| T15 Table 15-5 | 457 | Cockcroft-Gault and Schwartz methods. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Cockcroft-Gault card의 primary source. |
| T15 Fig.15-10 | 458 | Serum creatinine by age/sex. | USEFUL | NO | YES | VISUAL_INSPECTED | creatinine caveat. |
| T15 Fig.15-11 | 459 | Acute renal failure and creatinine rise. | USEFUL | YES | YES | VISUAL_INSPECTED | Scr lag warning. |
| T15 Fig.15-12 | 459 | approach to new steady state after turnover-rate decrease. | USEFUL | YES | YES | VISUAL_INSPECTED | RF estimation lag. |
| T15 Table 15-6 | 460 | Creatinine turnover/half-life as RF decreases. | USEFUL | YES | NO | VISUAL_INSPECTED | Scr lag quantification. |
| T15 Fig.15-13 | 461 | Time to plateau with reduced renal function. | USEFUL | NO | YES | VISUAL_INSPECTED | renal impairment accumulation context. |
| T15 Fig.15-14 | 462 | Amikacin renal impairment with/without loading dose. | USEFUL | YES | YES | VISUAL_INSPECTED | LD vs maintenance in renal disease. |
| T15 Table 15-7 | 464 | Digoxin CL/V in mild vs severe CHF. | USEFUL | YES | NO | VISUAL_INSPECTED | conditional prior bridge. |
| T15 Table 15-8 | 464–466 | CL and half-life in normal vs severe chronic renal disease. | USEFUL | NO | NO | VISUAL_INSPECTED | examples. |
| T15 Fig.15-16 | 467 | Hemodialysis system schematic. | USEFUL | NO | YES | VISUAL_INSPECTED | dialysis mechanism. |
| T15 Fig.15-17 | 470 | dialysis clearance variability across drugs. | USEFUL | NO | YES | VISUAL_INSPECTED | clearance variability. |
| T15 Fig.15-18 | 471 | fraction removed by dialysis vs Vu/CLu. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | dialysis supplement decision core. |
| T15 Fig.15-19 | 473 | gentamicin dose replacement principle. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Eq.15-34 operational meaning. |
| T15 Fig.15-20 | 474 | gentamicin regimen with/without dialysis and supplement. | USEFUL | YES | YES | VISUAL_INSPECTED | worked dialysis example. |
| T15 Fig.15-21 | 475 | cefsulodin i.v./i.p. CAPD profiles. | USEFUL | NO | YES | VISUAL_INSPECTED | CAPD context. |
| T15 Fig.15-22 | 477 | teicoplanin bioavailability vs dwell time. | USEFUL | NO | YES | VISUAL_INSPECTED | CAPD context. |
| T15 Fig.15-23 | 480 | disease status models with temporary/symptomatic/disease-independent treatment. | USEFUL | NO | YES | VISUAL_INSPECTED | disease-on-PD expansion. |
| T15 Fig.15-24 | 480 | cascading PK/PD biomarker model. | USEFUL | NO | YES | VISUAL_INSPECTED | biomarker cascade context. |
| T15 Fig.15-25 | 481 | WHIG model. | USEFUL | NO | YES | VISUAL_INSPECTED | advanced disease-PD context. |
| T15 Tables 15-9–15-17 | 483–489 | Study-problem datasets. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | core teaching에 필수 아님. |
| T18 Fig.18-1 | 578 | two therapy-initiation strategies. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Ch.18 clinical decision frame. |
| T18 Fig.18-2 | 579 | hypothetical PD variability sources. | USEFUL | NO | YES | VISUAL_INSPECTED | variability context. |
| T18 Table 18-1 | 580 | variability degree in oral absorption/disposition. | USEFUL | NO | NO | VISUAL_INSPECTED | covariate/prior context. |
| T18 Fig.18-3 | 581 | clearance subpopulation distributions. | USEFUL | NO | YES | VISUAL_INSPECTED | conditional prior intuition. |
| T18 Fig.18-4 | 581 | ganciclovir apparent CL vs creatinine clearance. | USEFUL | NO | YES | VISUAL_INSPECTED | renal covariate example. |
| T18 Fig.18-5 | 582 | variability partition for PK parameters. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | LD vs maintenance confidence logic but not accuracy claim. |
| T18 Fig.18-6 | 583 | trimipramine dose by CYP2D6 genotype. | USEFUL | NO | YES | VISUAL_INSPECTED | pharmacogenomic prior example. |
| T18 Fig.18-7 | 585 | alendronate BMD time course. | USEFUL | NO | YES | VISUAL_INSPECTED | long-term PD/titration context. |
| T18 Table 18-2 | 587 | monitoring need by PK/PD variability. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | TCS criterion logic. |
| T18 Fig.18-8 | 588 | phenytoin steady plasma concentrations. | USEFUL | YES | YES | VISUAL_INSPECTED | monitoring example. |
| T18 Table 18-3 | 589–590 | monitoring drug therapy by effects or alternative tests. | USEFUL | YES | NO | VISUAL_INSPECTED | response monitoring vs concentration monitoring. |
| T18 Table 18-4 | 591 | nonadherence patterns. | USEFUL | YES | NO | VISUAL_INSPECTED | missed/erratic dosing context. |
| T18 Fig.18-9 | 592 | missed doses and makeup doses. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | nonadherence pharmacokinetics. |
| T18 Fig.18-10 | 593 | doubling-up dose consequence. | USEFUL | YES | YES | VISUAL_INSPECTED | adverse risk after makeup dose. |
| T18 Table 18-5 | 595–596 | plasma concentration monitoring information for selected drugs. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | TCS drug examples. |
| T18 Table 18-6 | 597 | information needed for evaluating measured concentration. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | TCS interpretation gate; under-reflected in Draft. |
| T18 Table 18-7 | 598–599 | digoxin and vancomycin PK/dosing parameters. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | worked examples rely on it. |
| T18 Fig.18-11 | 601 | missed dose subtraction principle. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Eq.18-1/18-2 visual support. |
| T18 Fig.18-12 | 603 | 9-13-17-21 regimen vancomycin fluctuation. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Eq.18-3 worked example. |
| T18 Fig.18-13 | 605–606 | sampling time confidence in V vs CL estimates. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Bayesian/TDM decision confidence. |
| T18 Fig.18-14 | 607 | meloxicam study problem graph. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | study problem. |
| T18 Fig.18-15 | 608 | piroxicam drug holiday problem. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | study problem. |
| T18 Fig.18-16 | 609 | naproxen missed-dose study problem. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | study problem. |

---

## Final Source-Fidelity Decision

```text
GO: Phase 3/4A after MUST_FIX patch
NO-GO: direct HTML compile
REDO Phase 1: not required
```

Draft v0의 핵심 source coverage는 강하다. 그러나 현재 상태로 HTML에 들어가면 **source-backed textbook content**와 **교육용 실무/규제/소프트웨어 번역**이 섞여 고정될 위험이 크다. Phase 4A Content Lock 전에는 다음 7개를 우선 패치해야 한다.

```text
MUST_FIX PATCH LIST
1. Peak-shift directionality: 결정 규칙 → 1차 진단 신호.
2. TCS: 필수 적용 → criteria 충족 시 유용한 adjunct strategy.
3. Loading-dose 정확도 수치: V 5–10%, CL 30–40% source claim 삭제/라벨.
4. PK35 digoxin 처방 권고: 원문 직접 권고가 아니라 통합 추론 예시로 라벨.
5. TDM 80% claim 삭제.
6. NONMEM/BestDose/ID-ODS/Pmetrics/NDA/IND/RMP 라벨링.
7. Fig.6.12와 Table 18-6를 decision workflow에 보강.
```

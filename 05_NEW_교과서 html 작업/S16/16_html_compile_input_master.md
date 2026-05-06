# 16_HTML Compile Input Master

## Phase 4D Certification

| Certificate | Status | Basis |
|---|---|---|
| Learner-Standalone Certificate | PASS | PART A contains a learner navigation aid, the complete exact-spliced canonical body, approved figure markers, and bounded adjacent mastery notes. |
| Zero-Omission Certificate | PASS | Scope-required concepts, Audit MUST_FIX/SHOULD_FIX items, Phase 4C KEEP markers, and adopted Crucible logic are present or intentionally bounded. |
| Mastery-Uplift Certificate | PASS | Ten short adjacent augmentations are labeled by epistemic status and do not broaden the canonical scientific body. |
| Source-Boundary Certificate | PASS | Augmentations do not add new page tags, new unsupported numerical values, or new named examples; expert interpretation is labeled. |
| HTML-Readiness Certificate | PASS | PART B contains the Phase 5 rendering contract, figure/page-tag rules, audit/crucible guardrails, splice verification, coverage matrix, and logs. |


## Assembly Mode

PATCH MODE — `16_Content Lock v2.1(1).md` is a Figure Marker Patch, not a full restatement. The canonical learner body was constructed from `16_Content Lock v2(5).md` by exact-splicing seven approved Phase 4C marker blocks into unique anchors.


## Input Manifest

| File | Role | Authority level | Used for | Notes |
|---|---|---:|---|---|
| `16_scope_lock(3).md` | scope boundary | A0 | Source range, learner, image rights, hard rules, data anchors | Image rights = None; direct textbook figure embedding prohibited. |
| `016_G_임상 통합·패턴인식 TDM·질환·캡스톤(4).pdf` | PDF verification source | A1 | G&W Ch.6, PK15, PK35 page/figure/source verification | Used only for high-impact source verification and page/figure identity. |
| `016_T_임상 통합·패턴인식 TDM·질환·캡스톤_01(4).pdf` | PDF verification source | A1 | R&T Ch.15 disease/renal/dialysis verification | Used only for high-impact source verification and page/figure identity. |
| `016_T_임상 통합·패턴인식 TDM·질환·캡스톤_02(4).pdf` | PDF verification source | A1 | R&T Ch.18 therapy/TCS/dosing verification | Used only for high-impact source verification and page/figure identity. |
| `16_Audit_Report_v1(4).md` | audit guardrail | A2 | MUST_FIX/SHOULD_FIX, forbidden restoration, T5/T6/T7 checks | Controls source-fidelity regression prevention. |
| `16_Content Lock v2(5).md` | canonical body | A3 | Base text-final body | Used from `# Session 016 — Content Lock v2` onward; editorial pass ledger excluded from learner body. |
| `16_Content Lock v2.1(1).md` | figure insertion source | A4 | PATCH MODE insertion map and marker registry | All seven KEEP markers were exact-spliced. |
| `16_crucible_report_v1(1).md` | crucible guardrail | A5 | Adopted Grade A insight preservation and expert-pattern guardrails | Not used as raw prose source. |
| `S16_phase1_patch memo(2).md` | locked reference / deprecated-stage diagnostic | A6 | Phase 1 risk check and source-expansion caution | Used for regression awareness only. |
| `16_step1_draft_v0(3).md` | deprecated source | A6 | Omission check only | Not copied into learner body. |
| `붙여넣은 마크다운(1)(97).md` | compiler instruction | A7 | Phase 5 HTML rendering contract | Included in PART B as compiler requirements. |
| `붙여넣은 텍스트 (2)(10).txt` | Phase 4D assembly instruction | assembly instruction | Controls current master-file assembly | Not learner-facing. |
| `16_Content Lock v1(3).md` | prior locked reference | lower than v2 | Regression check only | Superseded by Content Lock v2. |


---

# PART A — Learner-Facing Complete Handout

## Learner Navigation Aid

**How to use this handout**  
Read §1 once to lock the capstone chain, then study §2 as the core concept path. Use the figure pointer blocks only as viewing instructions for the original textbook figures; the textbook images are not reproduced. After §2, use §5 to remove common confusions, §7 for active recall, and §8 for the session-level synthesis.

**Learning route**

```text
§1 Roadmap
→ §2.1–§2.3 Pattern recognition and model-candidate narrowing
→ §2.4 Bayesian individual parameter estimation
→ §2.5–§2.7 Disease, renal function, and dialysis adjustment
→ §2.8–§2.10 TCS, loading/maintenance dosing, and irregular dosing
→ §5 Confusion pairs
→ §7 Self-test
→ §8 Meta-frame
```

**Before you start**

- Keep the distinction between diagnostic signal and model proof.
- Keep the distinction between patient property (`RF`) and drug property (`fe`).
- Keep the distinction between V-driven loading and CL-driven maintenance.
- Keep the distinction between measured concentration and interpretable concentration.

**After you finish**

- You should be able to explain why Ch.6 narrows model candidates, Ch.15 explains patient deviation, PK35 estimates posterior parameters, Ch.18 converts the estimate to dosing/monitoring decisions, and PK15 closes the chain through exposure/safety-margin reporting.
- You should be able to state why direct textbook figures are pointer-only in this handout: image rights are locked as None.

---

# Session 016 — Content Lock v2
## 임상 통합 캡스톤: 패턴 인식 · TDM · 질환 · 치료 의사결정

**역할**: Editor-in-Chief — pharmacometrics specialist  
**적용 원칙**: Source Fidelity Audit v1의 MUST_FIX는 기본 채택하고, Crucible Grade A는 PDF 근거가 있을 때 채택한다. Grade B는 문서 길이를 늘리지 않는 cross-link로만 반영하며, Grade C는 제외한다.  
**분량 판정**: 본 Content Lock v2는 Content Lock v1의 의미·구조·page tag를 유지하면서 문장 가독성과 최소 주석만 반영한 text-final 산출물이다.  
**Figure 처리**: Audit T6 Figure Inventory는 본 단계에서 판정하지 않고 Phase 4C로 이월한다.

---

## Updated Curation Map

### MUST tier — §2 핵심 카드 10개

| # | Card | Source tag | Lock decision |
|---:|---|---|---|
| 2.1 | Pattern-recognition decision workflow | G&W Ch.6 [pp.423–424, pp.465–466] | 4축 + Fig.6.12 workflow를 통합. “모델 확정”이 아니라 “후보 축소”로 고정. |
| 2.2 | Peak-shift + saturation | G&W Ch.6 [pp.424–428] | 좌/우 방향은 1차 진단 신호. deterministic model-class rule 금지. |
| 2.3 | Effect compartment / turnover / receptor on-off | G&W Ch.6 [pp.425–427] | 대표 ODE만 유지. Case A–I 전수 설명은 CONTEXT로 압축. |
| 2.4 | Bayesian objective function | G&W PK35 [pp.641–643]; R&T Ch.18 [pp.605–606] | PK35 수치 유지, 처방 권고는 source-locked claim에서 제외. |
| 2.5 | Disease/RF/Rd framework | R&T Ch.15 [pp.450–464] | fe와 RF 분리. LD/MD 분기와 digoxin uremia 예외만 남김. |
| 2.6 | Cockcroft-Gault + creatinine lag | R&T Ch.15 [pp.457–461] | CG 식 + SCr turnover lag를 반드시 결합. |
| 2.7 | Hemodialysis coordinate plane | R&T Ch.15 [pp.466–474] | `Vu<120 AND CLu<CLuD` hard gate 삭제. Vu·CLu 평면으로 재서술. |
| 2.8 | Target concentration strategy criteria | R&T Ch.18 [pp.594–597] | “필수 적용” 삭제. criteria 충족 시 유용한 adjunct strategy로 고정. |
| 2.9 | Loading vs maintenance dose | R&T Ch.18 [pp.584–586]; Fig.18-5 [p.582] | V/CL “정확도” 수치 삭제. Fig.18-5 variability partition로 정정. |
| 2.10 | Missed / unequal / erratic dosing | R&T Ch.18 [pp.600–605] | TDM 80% 삭제. Eq.18-1–18-4와 worked examples만 유지. |

### CONTEXT tier — 1–2문장으로만 유지

| Context item | Lock position | Treatment |
|---|---|---|
| Ch.6 Case A–I banks | §2.1–§2.3 | representative prototypes only; individual equations not expanded. |
| Hysteresis, tolerance, rebound, adaptation | §2.1–§2.3 | model-selection clues only. |
| PK15 toxicokinetics | §1, §7, §8 | NCA exposure reporting and safety margin bridge; no separate §2 card. |
| Hepatic disease examples | §2.5, §5.4 | high-extraction vs renal-excreted contrast. |
| CAPD | §2.7 | hemodialysis contrast in one sentence. |
| Disease-on-PD / WHIG | §8 | future extension only. |
| Pharmacogenomic variability | §2.8 | prior selection example only. |
| Dose strengths | §2.9 | practical rounding issue retained as `[p.확인 필요]`; exact warfarin strength list not source-locked. |
| NONMEM, BestDose, ID-ODS, Pmetrics, NDA/IND/RMP | §1, §8 | `[교과서 외 구현/규제 번역]` label required. |

### Excluded / compressed

- Direct textbook figure reproduction: **excluded**; Phase 4C may use independent schematic only.
- Ch.15 and Ch.18 study problems: §7 design reference only, not source-locked core content.
- PMDA/EMA/FDA reviewer workflow claims, RMP templates, software-specific workflows: excluded unless labeled `[교과서 외 구현/규제 번역]`.
- “PD 작업말 70%”, “TDM 환자 80%”, “60초 내 모델 확정”: deleted or downgraded to unlabeled learning operation; no source-locked claim.

---

## Phase 4A Adjudication Summary

Phase 4A의 상세 adjudication table은 v1에서 완료되었으며, v2에서는 readability/annotation pass의 산출만 남긴다. Source-fidelity verdict 자체는 변경하지 않았다.

---

# §1 — Session Header & Roadmap

**Session ID**: 016 — 임상 통합 캡스톤: pattern recognition, TDM(← 농도 측정으로 용량 판단을 보정하는 전략), disease, therapeutic decision-making
<!-- ANNOTATION -->

**Source universe**

- Gabrielsson & Weiner 5e: Ch.6 Pattern Recognition [pp.423–466], PK15 Toxicokinetics [pp.546–548], PK35 Bayesian model — Digoxin [pp.641–643]
- Rowland & Tozer 5e: Ch.15 Disease [pp.443–489], Ch.18 Initiating and Managing Therapy [pp.577–610]

<!-- MASTER LENS -->
**Big Idea**  
데이터의 *shape*는 그 데이터를 만든 kinetic/dynamic mechanism(← 농도 변화와 약효 변화의 발생 원리)의 흔적이다.
<!-- ANNOTATION -->
질환은 그 mechanism의 parameters를 population에서 벗어나게 만들고, Bayesian TDM은 그 환자별 deviation을 추정한다. Ch.18의 치료 의사결정은 그 추정을 dose, sampling, monitoring decision으로 바꾼다.

<!-- ANCHOR -->
**Capstone spine**

```text
[Ch.6 Pattern Recognition]
  → 어떤 PD 구조가 가능한가?
[Ch.15 Disease]
  → 환자 parameter가 population에서 왜 벗어났는가?
[PK35 Bayesian TDM]
  → 관측 농도와 prior를 어떻게 결합할 것인가?
[Ch.18 Initiating/Managing Therapy]
  → loading, maintenance, TCS, missed dose를 어떻게 판단할 것인가?
[PK15 Toxicokinetics]
  → 선택된 용량의 exposure와 safety margin을 어떻게 보고할 것인가?
```

**후속 구현 영역 — source-locked 본문이 아님**  
NONMEM `$DES`, Bayesian TDM software, NDA/IND/RMP style writing은 이 세션에서 자연스럽게 이어지는 실무 영역이다. 그러나 교과서 본문 직접 claim은 아니므로 이하에서는 `[교과서 외 구현/규제 번역]`으로만 취급한다.

**Data anchors retained**

- PK35 digoxin: 55-year-old, 60 kg male with CHF; Lanoxicap 0.2 mg daily; concentrations 2.5 µg/L at 458 h and 0.9 µg/L at 479 h; CLpop 1.8 L/h, Vpop 500 L; final estimates CL 5.7 L/h, V 119.6 L, t½ 14.5 h [G&W pp.641–643].
- PK15 toxicokinetics: 10/56/320 µmol·day⁻¹·kg⁻¹ dose levels, Cmax/AUC exposure reporting, therapeutic concentration 0.05–0.1 µM, high-dose Cmax approximately 50 µM, safety margin >100-fold in the toxicokinetic interpretation context [G&W pp.546–548].
- Ch.18 concentration interpretation: Table 18-6 data collection, Eq.18-1–18-4 dosing irregularity equations, and Fig.18-13 sampling-dependent confidence in V vs CL [R&T pp.597, 601–605].

<!-- RECAP -->
**§1 recap**: 이 세션은 “모델 선택 → 질환 보정 → 개인 추정 → 처방·monitoring → exposure reporting”의 단일 clinical pharmacometrics chain을 잠근다.

<!-- FIGURE_SCHEMATIC -->
Title: Session 016 Capstone Spine — from data shape to exposure report
Mode: N
Visual objective: 5초 안에 각 챕터가 다음 챕터에 넘기는 decision object를 보이게 한다.
Core message: Ch.6은 model candidate를, Ch.15는 patient deviation을, PK35는 posterior parameter를, Ch.18은 dose/monitoring decision을, PK15는 exposure/safety-margin report를 만든다.
Elements to include: Five horizontal blocks: Ch.6 Pattern Recognition → Ch.15 Disease/RF/Rd → PK35 Bayesian TDM → Ch.18 Dosing/Monitoring → PK15 Toxicokinetics; under each block, output label only: model candidate, patient deviation, posterior parameter, dose decision, exposure report; one small caution strip: implementation/regulatory translation requires label.
Elements to exclude: Drug examples, numeric anchors, source page tags, software names beyond the caution label, any regulatory workflow diagram.
Suggested rendering: Mermaid
Caption: Session 016은 독립 개념 묶음이 아니라, data shape에서 clinical exposure reporting으로 이어지는 단일 decision chain이다.
Alt text: Five-step left-to-right pipeline connecting pattern recognition, disease adjustment, Bayesian estimation, therapeutic decision-making, and toxicokinetic reporting.
Source relation: Newly designed
<!-- /FIGURE_SCHEMATIC -->

---

# §2 — Concept Anatomy Cards

## §2.1 — Pattern-recognition decision workflow [G&W pp.423–424, pp.465–466]

<!-- MASTER LENS -->
**핵심**: response-time, concentration-time, concentration-response plot은 먼저 baseline, time-delay, peak-shift, saturation/slope를 따라 읽는다. 그 다음 Fig.6.12식 workflow처럼 C/R vs time, C-R plot(← 농도-반응 관계를 시간과 분리해 보는 그림), hysteresis(← 시간 지연으로 C-R 관계가 고리처럼 보이는 현상), rebound, tolerance 여부를 순서대로 확인한다.
<!-- ANNOTATION -->

**Locked formulation**

```text
1. Baseline: stable? drifting? disease progression/adaptation?
2. Time-delay: concentration peak와 response maximum/minimum이 분리되는가?
3. Peak-shift: dose 증가에 따라 response extremum이 좌/우로 이동하는가?
4. Saturation/slope: high dose에서 flat portion 또는 nonlinear rise/fall이 보이는가?
5. C-R plot: direct, indirect, rebound, tolerance, hysteresis 중 어느 후보가 남는가?
```

**Editorial correction**: “60초 내 모델 확정”은 source claim이 아니다. 본 문서에서는 “빠른 후보 축소를 위한 교육용 operation”으로만 둔다.

<!-- TRENCH -->
**Trench-Level Tip**: 단일 dose response-time curve 하나만으로 mechanism을 확정하지 말라. 중요한 것은 dose escalation에서 shape가 어떻게 바뀌는지이다. 그 변화가 model-class narrowing의 핵심이다.

<!-- ANCHOR -->
§2.1은 plot-reading grammar이고, §2.2–§2.3은 그 grammar가 실제 ODE 후보로 내려가는 첫 번째 mechanistic bridge이다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner Ch.6, Fig.6.1 [p.423] and Fig.6.12 [pp.465–466]
Why this matters: Fig.6.1 shows the initial visual grammar — baseline, time-delay, peak-shift, saturation, slopes. Fig.6.12 converts that grammar into a practical analysis workflow.
When to look: after reading this card, before moving to §2.2
Learner instruction: Inspect Fig.6.1 first as the checklist, then Fig.6.12 as the decision workflow. Do not treat the checklist items as independent facts; follow how each observation narrows the next model question.
<!-- /FIGURE_POINTER -->

> **Mastery Note — TEXTBOOK_DERIVED**  
> 이 카드는 “정답 모델”을 즉시 고르는 법이 아니라, 관찰 순서를 고정해 후보 모델을 줄이는 법을 가르친다. 먼저 shape vocabulary를 만들고, 그 다음 남는 mechanistic question을 줄이는 방식으로 읽는다.


---

## §2.2 — Peak-shift + saturation: diagnostic signal, not deterministic rule [G&W pp.424–428]

<!-- MASTER LENS -->
**핵심**: peak-shift 방향은 “모델 클래스 그 자체”가 아니다. 이는 competing model candidates를 좁히는 1차 진단 신호이다.

| Observed pattern | Locked interpretation |
|---|---|
| Case A: plasma peak occurs at about one-third of the time to Rmin | delayed response is present; direct-effect model alone is unlikely. |
| Case B: higher-dose trough shifts left | turnover loss stimulation or receptor on/off may be plausible candidates; not an automatic conclusion. |
| Case C: highest-dose trough shifts right + flat portion | input inhibition with saturation is a strong candidate signal. |

**Corrected sentence**  
“좌/우 방향이 곧 모델 클래스”가 아니다. 더 정확히는, 좌/우 방향과 saturation 유무가 turnover, effect compartment, receptor on/off 등 후보군을 좁히는 1차 진단 신호이다.

<!-- TRENCH -->
**Trench-Level Tip**: Case B left-shift를 “kon이 큰 약물”로 외우지 말라. receptor on/off에서는 finite receptor pool 때문에 nadir가 빨라질 수 있고, turnover model에서도 loss stimulation이 유사한 pattern을 만들 수 있다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner Ch.6, Fig.6.2 [p.424] and Fig.6.3 [p.428]
Why this matters: Fig.6.2 makes the leftward vs rightward response-time movement visible. Fig.6.3 prevents the common error of mapping one pattern to one model by showing competing alternatives.
When to look: immediately after reading this card
Learner instruction: Compare Case A, B, and C by looking only at timing of the trough and high-dose flattening. Then check Fig.6.3 to ask which competing models remain rather than choosing one model prematurely.
<!-- /FIGURE_POINTER -->

> **Failure Mode — AUDIT_DERIVED**  
> Peak-shift를 단일 모델명으로 번역하는 순간 source-fidelity가 무너진다. 좌/우 이동은 후보군을 줄이는 신호이지, 모델 확정 판결이 아니다.


---

## §2.3 — Effect compartment / turnover / receptor on-off prototypes [G&W pp.425–427]

<!-- MASTER LENS -->
**핵심**: Ch.6의 많은 Case A–I equations는 모두 외울 목록이 아니다. 이들은 세 prototype(← 반복적으로 재사용되는 대표 구조)을 구분하기 위한 pattern library이다.
<!-- ANNOTATION -->

### Prototype 1 — Effect compartment

Time-delay가 있으나 dose 증가에 따른 clear peak-shift가 약하면 link model을 먼저 의심한다.

```math
\frac{dC_e}{dt}=k_{e0}(C-C_e)
```

Response model은 `C`가 아니라 `Ce`에 연결된다. Counter-clockwise hysteresis는 effect-site equilibration delay의 전형적 신호이다 [G&W p.426].

### Prototype 2 — Turnover model

Response variable `R`은 생성과 소실의 동적 평형 위에 놓일 수 있다. 이때 drug은 input 또는 loss process를 억제하거나 자극한다.

```math
\frac{dR}{dt}=k_{in}\cdot I(C)-k_{out}R
```

```math
\frac{dR}{dt}=k_{in}-k_{out}R\cdot S(C)
```

Baseline `R0 = kin/kout`는 정적 ratio가 아니라 dynamic equilibrium이다. 새로운 평형으로 이동하는 속도는 주로 `kout`이 지배한다.

### Prototype 3 — Receptor on/off

Receptor binding이 finite pool을 가진다면 response extremum의 timing은 `kon·C·(RT−RC)`와 `koff·RC`의 경쟁으로 결정된다.

```math
\frac{dRC}{dt}=k_{on}C(R_T-RC)-k_{off}RC
```

<!-- TRENCH -->
**Trench-Level Tip**: Case A–I의 모든 수식을 전수 암기하지 말고, direct delay, turnover delay, finite-pool binding 중 어느 failure mode가 현재 plot을 설명하는지 먼저 판단한다.

<!-- RECAP -->
**§2.1–§2.3 recap**: Ch.6의 목적은 shape에서 model candidate를 줄이는 것이다. Pattern은 proof가 아니라 triage signal이다.

> **Practice Lens — EXPERT_INFERENCE**  
> 세 prototype은 “delay가 어디에서 생겼는가”를 묻는 세 가지 문법이다. effect-site equilibration, response turnover, finite receptor binding 중 어느 병목이 plot의 모양을 만들었는지 먼저 분리한다.


---

## §2.4 — Bayesian objective function for individual TDM [G&W pp.641–643; R&T pp.605–606]

<!-- MASTER LENS -->
**핵심**: Bayesian TDM은 observed concentrations만 믿지 않는다. population average만 믿지도 않는다. concentration likelihood와 population prior의 상대적 variance를 함께 고려해 개인 parameter를 추정한다.
<!-- ANNOTATION -->
앞선 §2.1–§2.3이 “어떤 구조가 가능한가”를 줄였다면, §2.4는 그 구조 안에서 “이 환자의 parameter가 어디에 있는가”를 추정한다.

**Conceptual objective**

```math
OBJ_{Bayes}\approx
\sum_i\frac{(C_{obs,i}-\hat C_i)^2}{var(\hat C_i)}
+
\sum_j\frac{(P_{pop,j}-\hat P_j)^2}{var(\hat P_j)}
```

- 농도 없음: population average가 사실상 estimate가 된다.
- prior 없음: maximum-likelihood concentration fitting에 가까워진다.
- 농도 + prior 있음: complete Bayesian method가 된다.

**PK35 digoxin anchor**  
55세, 60 kg, CHF 남성; Lanoxicap 0.2 mg daily; 2.5 µg/L at 458 h와 0.9 µg/L at 479 h; CLpop 1.8 L/h, Vpop 500 L; 추정 CL 5.7 L/h, V 119.6 L, t½ 14.5 h [G&W pp.641–643].

**Sampling identifiability anchor**  
R&T Fig.18-13은 early sample이 V에 더 민감하고, late/plateau sample이 CL에 더 민감함을 보여준다. 따라서 1×t½ 근처 sampling만으로는 CL 1/3 변화와 V 3배 변화를 구분하기 어렵다. 4×t½ 또는 steady-state 정보가 CL 추정에 더 유리하다 [R&T pp.605–606].

<!-- TRENCH -->
**Trench-Level Tip**: Bayesian posterior(← 관측 후 갱신된 개인 추정값)가 이상한 V를 내면 “환자가 이상하다”고 먼저 결론내지 말라. sampling time, dosing history, prior variance, assay error, adherence를 먼저 점검한다.
<!-- ANNOTATION -->

**Boundary**  
PK35 digoxin 사례는 CL/V/t½ 추정 사례이다. Loading dose 0.4 mg, maintenance 0.1–0.125 mg/day 같은 처방 문장은 교과서 직접 권고가 아니라 `[교과서 외 통합 추론 예시]`로만 다룬다. Sheiner 1977을 NONMEM의 직접 조상으로 단정하는 표현은 `[확인 필요]`이다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner PK35, Fig.35.1 [pp.641–642]; Rowland & Tozer Ch.18, Fig.18-13 [pp.605–606]
Why this matters: Fig.35.1 links patient-specific clearance variability to concentration-time behavior. Fig.18-13 shows why sampling time changes confidence in V vs CL estimates.
When to look: after the Sampling identifiability anchor paragraph in this card
Learner instruction: First inspect how CL variability changes predicted concentration-time curves. Then inspect Fig.18-13 and ask whether the available sample is V-informative, CL-informative, or ambiguous.
<!-- /FIGURE_POINTER -->

> **Mastery Note — CRUCIBLE_DERIVED**  
> Bayesian TDM의 핵심은 농도값 자체보다 그 농도가 어떤 parameter를 식별할 수 있는 시점에서 얻어졌는지이다. 같은 concentration이라도 timing이 다르면 posterior가 지지하는 V/CL 조합이 달라진다.


---

## §2.5 — Disease/RF/Rd framework: fe와 patient renal function을 분리하라 [R&T pp.450–464]

<!-- MASTER LENS -->
**핵심**: renal impairment dosing은 “신장 나쁘니 줄인다”가 아니다. drug property `fe`와 patient property `RF`를 분리한 뒤, 그 조합으로 maintenance requirement를 줄이는 작업이다.

```math
R_d = RF\cdot f_e + (1-f_e)
```

- `fe`: fraction excreted unchanged; drug-specific.
- `RF`: renal function relative to typical; patient-specific.
- maintenance dose 또는 dosing rate는 `Rd`에 비례하여 조정한다.

**Clinical triage**

- `fe ≤ 0.30`이면 renal function 감소가 maintenance exposure에 미치는 영향이 작을 수 있다.
- `RF ≥ 0.70`이면 많은 경우 major regimen change가 필요하지 않을 수 있다.
- Loading dose는 CL이 아니라 V에 의존하므로, renal function만으로 자동 감량하지 않는다. 단, digoxin처럼 uremia에서 tissue distribution이 감소하여 V가 줄 수 있는 예외는 별도로 본다 [R&T p.464].

**Hepatic contrast**  
Cirrhosis에서는 high-extraction oral drug의 first-pass loss 감소와 portal bypass로 F가 증가할 수 있다. 반대로 low-extraction albumin-bound drug에서는 fu 증가가 total CL을 증가시킬 수 있으나, unbound CL(← 단백결합 안 된 약물 기준 청소율)은 크게 변하지 않을 수 있다 [R&T pp.444–446].
<!-- ANNOTATION -->

<!-- TRENCH -->
**Trench-Level Tip**: phenytoin처럼 albumin-bound low-extraction drug에서는 fu↑가 total concentration 해석을 망친다. total target을 그대로 쓰면 같은 unbound exposure를 과소평가할 수 있다.

<!-- FIGURE_SCHEMATIC -->
Title: Rd Framework — drug property fe × patient property RF
Mode: R
Visual objective: 5초 안에 renal dose adjustment가 renal impairment label이 아니라 fe와 RF의 interaction임을 보이게 한다.
Core message: Maintenance adjustment becomes large only when the drug depends substantially on renal excretion and the patient’s renal function is meaningfully reduced.
Elements to include: X-axis: RF from normal to severe impairment; Y-axis or layered bands: fe low, moderate, high; output zone: Rd close to 1 vs reduced; annotation: fe = drug property, RF = patient property, Rd = maintenance requirement; small callout: LD is separate unless V changes.
Elements to exclude: Exact reproduction of textbook curves, multiple drug examples, Cockcroft-Gault equation details.
Suggested rendering: SVG
Caption: Rd는 신기능 저하 자체가 아니라 drug-specific fe와 patient-specific RF의 조합으로 maintenance requirement를 줄인다.
Alt text: A two-axis conceptual surface showing renal function on one axis, fraction excreted unchanged on another, and maintenance dose requirement decreasing most when both renal dependence and impairment are high.
Source relation: Redrawn from textbook concept
<!-- /FIGURE_SCHEMATIC -->

> **Practice Lens — TEXTBOOK_DERIVED**  
> Rd framework는 “환자 라벨”과 “약물 라벨”을 분리하는 계산 문법이다. 같은 renal impairment라도 fe가 낮은 약물과 높은 약물의 maintenance decision은 달라져야 한다.


---

## §2.6 — Cockcroft-Gault + creatinine lag [R&T pp.457–461]

<!-- MASTER LENS -->
**핵심**: Cockcroft-Gault는 RF의 입력값을 만든다. 그러나 SCr는 실시간 renal function의 거울이 아니다. creatinine turnover가 반영된 지연 지표이다.

```math
CL_{cr}\;(mL/min)=\frac{(140-age)\cdot WT}{72\cdot SCr}
```

여성에서는 일반적으로 0.85를 곱한다. 식은 adult, stable renal function, body size interpretation이 전제이다 [R&T p.457].

**AKI caveat**  
Acute renal failure에서는 SCr 상승이 renal function 감소보다 늦다. R&T Table 15-6은 renal function이 낮아질수록 creatinine turnover time과 half-life가 길어짐을 보여준다 [R&T pp.459–461]. 따라서 오늘 측정한 SCr로 오늘의 RF를 과신하면, 초기 24–48h 독성 축적을 놓칠 수 있다.

<!-- TRENCH -->
**Trench-Level Tip**: C-G는 snapshot 계산이 아니라 trend 해석과 함께 써야 한다. 특히 노인, 근감소, 비만, AKI에서는 체중 선택과 SCr lag가 dose error의 주된 원인이다.

> **Failure Mode — AUDIT_DERIVED**  
> SCr가 아직 새 steady state에 도달하지 않았는데 Cockcroft-Gault 값을 그대로 RF로 쓰면, 계산은 정확해 보여도 임상적으로는 과거 신기능을 반영할 수 있다. 이 카드는 식보다 시간 지연을 함께 기억해야 한다.


---

## §2.7 — Hemodialysis coordinate plane: Vu와 CLu를 함께 보라 [R&T pp.466–474]

<!-- MASTER LENS -->
**핵심**: hemodialysis 보충 용량은 “half-life가 줄었는가”만으로 결정하지 않는다. dialysis session 동안 body amount가 의미 있게 빠졌는지가 핵심이다.

**Locked correction**

```text
삭제: Vu < 120 L AND CLu < CLuD이면 보충 용량 필요.
채택: Vu·CLu 평면에서 dialysis effectiveness를 읽는다.
```

R&T Fig.15-18은 high-flux 3 h dialysis에서 unbound V가 약 120 L보다 크거나, 환자의 own unbound clearance가 dialysis clearance보다 훨씬 크면 dialysis가 제거하는 fraction이 20% 미만으로 작아질 수 있음을 보여준다 [R&T pp.471–472]. 따라서 이는 hard AND gate가 아니라 continuous trade-off이다.

**Key equations, concept level**

- During dialysis: `kD = (CLu + CLuD)/Vu`.
- Fraction lost during dialysis period: `1 − exp(−kD·T)`.
- Dialysis contribution depends on `CLuD/(CLu + CLuD)` and the fraction lost over the session.
- Supplementary dose is considered when the amount after dialysis should be restored to the amount expected without dialysis [R&T pp.471–474].

**CAPD contrast**  
CAPD clearance is generally much lower than hemodialysis clearance for most drugs, so the same “dialysis patient” label cannot be used as a single dosing rule [R&T pp.475–477].

<!-- TRENCH -->
**Trench-Level Tip**: Phenobarbital의 dialysis half-life가 크게 줄어도 single 3 h session에서 body amount가 충분히 빠지지 않을 수 있다. half-life shortening and amount removed are not the same endpoint.

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer Ch.15, Fig.15-18 [p.471] and Fig.15-19 [p.473]
Why this matters: Fig.15-18 shows why dialysis removal is a continuous function of Vu and CLu, not a hard threshold. Fig.15-19 connects removal during dialysis to the replacement-dose concept.
When to look: after the Locked correction block in this card
Learner instruction: Inspect Fig.15-18 before applying any supplement rule. Ask whether the patient-drug pair sits in a region where dialysis removes clinically meaningful body amount during the session.
<!-- /FIGURE_POINTER -->

> **Failure Mode — AUDIT_DERIVED**  
> Dialysis decision에서 half-life shortening은 시각적으로 강한 신호지만, supplement decision의 endpoint는 session 동안 빠진 body amount이다. 그래서 Vu와 CLuD/CLu의 좌표를 함께 읽어야 한다.


---

## §2.8 — Target Concentration Strategy criteria [R&T pp.594–597]

<!-- MASTER LENS -->
**핵심**: TCS는 특정 약물명에 자동 적용되는 필수 전략이 아니다.
<!-- ANNOTATION -->
여기서 핵심은 “농도를 잴 수 있는가”가 아니라, 그 농도가 다음 clinical decision을 바꿀 만큼 제때·정확하게 해석되는가이다. criteria가 대부분 충족될 때 initiating and monitoring therapy에 유용한 adjunct strategy이다.

**Criteria lock**

1. Concentration-response relationship이 충분히 좋아야 한다.
2. Therapeutic failure probability가 높아야 한다: low therapeutic index, large PK variability, genetic/disease/drug-interaction risk, nonadherence/erratic absorption 가능성.
3. Population PK information이 있어야 한다.
4. Reliable assay가 가능해야 한다.
5. Assay turnaround가 다음 therapeutic decision 전에 도착해야 한다.

**Table 18-5 lock**  
Cyclosporine, digoxin, gentamicin, nortriptyline, phenytoin, theophylline 등은 TCS가 clinically helpful했던 대표 후보군이다. 약물명만으로 TCS가 필수라는 뜻은 아니다 [R&T pp.595–596].

**Table 18-6 interpretation gate**  
Measured concentration 하나만으로는 해석이 끝나지 않는다. 해석에는 dosing history, sampling time, previous concentrations, clinical status, renal/hepatic laboratory data, protein binding, concurrent drugs, assay method, usual PK parameters가 필요하다 [R&T p.597].

**Phenytoin lock**  
Phenytoin은 saturable metabolism과 altered protein binding 이슈가 있어 monitoring 정당성이 강하다 [R&T pp.588, 595–596]. 그러나 total concentration target은 uremia, surgery, displacement drugs에서 unbound target을 맞추도록 조정되어야 한다 [R&T p.596].

<!-- TRENCH -->
**Trench-Level Tip**: TCS의 5 criteria는 checklist가 아니라 sequential filter이다. 하나가 실패하면 measured number가 있어도 임상 의사결정에 유용하지 않을 수 있다.

> **Practice Lens — TEXTBOOK_DERIVED**  
> TCS는 “농도를 측정할 수 있음”이 아니라 “측정값이 다음 처방 결정을 바꿀 수 있음”을 요구한다. Table 18-6의 정보가 빠지면 concentration은 숫자일 뿐 decision object가 아니다.


---

## §2.9 — Loading dose vs maintenance dose [R&T pp.582, pp.584–586]

<!-- MASTER LENS -->
**핵심**: loading dose와 maintenance dose는 서로 다른 parameter가 지배한다.
<!-- ANNOTATION -->
따라서 TCS가 target concentration을 정해 주더라도, 어떤 dose component를 바꿀지는 V와 CL을 분리해서 결정해야 한다. loading dose는 V와 target concentration의 문제이고, maintenance dose는 CL과 target average exposure의 문제이다.

```math
D_L = \frac{V\cdot C_{target}}{F}
```

**Corrected Fig.18-5 lock**  
Step 1의 “V 90% 설명” 또는 “V 5–10% 정확도” 표현은 삭제한다. 이 표현들은 Fig.18-5의 의미를 prediction accuracy로 잘못 읽게 만든다. R&T Fig.18-5의 variability partition은 대략 다음을 보여준다: V는 body weight 25% + age 10% + renal function 10%로 약 45% explained, 55% unaccounted; hepatic CL은 약 40% explained, 60% unaccounted; renal CL은 renal function 50% + body weight 15% + age 15%로 약 80% explained; F는 약 5%만 explained [R&T p.582].

**Clinical implication**

- Renal-clearance dominant drug의 maintenance dose는 RF로 비교적 강하게 예측된다.
- Hepatic-clearance dominant drug의 maintenance dose는 demographic covariate만으로 설명되지 않는 IIV가 크다.
- Loading dose는 V-driven이지만 distribution kinetics, administration rate, formulation, available dose strengths `[p.확인 필요]`, toxicity risk 때문에 divided loading이 필요할 수 있다. Chloroquine example처럼 theoretical LD를 한 번에 투여하지 않는 이유가 여기에 있다 [R&T p.585].

<!-- TRENCH -->
**Trench-Level Tip**: “신부전이므로 LD도 줄인다”는 자동 규칙은 틀릴 수 있다. LD는 V 문제이고 MD는 CL 문제이다. 단, digoxin uremia처럼 V 자체가 변하는 예외는 따로 잡는다.

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer Ch.18, Fig.18-5 [p.582]
Why this matters: This figure was central to correcting the mistaken V/CL prediction accuracy reading. It should be inspected as a variability partition, not as a promise of dosing precision.
When to look: immediately after the Corrected Fig.18-5 lock paragraph in this card
Learner instruction: Read the figure by asking what fraction of variability is explained and what remains unaccounted. Then connect that to why renal CL may support stronger maintenance prediction than hepatic CL or F.
<!-- /FIGURE_POINTER -->

> **Mastery Note — AUDIT_DERIVED**  
> Fig.18-5는 “얼마나 정확히 맞출 수 있는가”가 아니라 “어떤 variability가 설명되고 무엇이 남는가”를 보여준다. 따라서 LD/MD 판단에서는 V와 CL의 설명 가능성을 분리해 읽어야 한다.


---

## §2.10 — Missed / unequal / erratic dosing framework [R&T pp.600–605]

<!-- MASTER LENS -->
**핵심**: nonadherence, unequal interval, erratic ICU dosing은 TDM 해석을 망치는 예외가 아니다. superposition(← 각 용량의 남은 농도 기여를 더하는 원리)으로 정량화할 수 있는 일반 상황이다.
<!-- ANNOTATION -->

**Three scenarios**

| Scenario | Equation | Locked use |
|---|---|---|
| One missed dose | Eq.18-1 | expected steady-state concentration minus contribution remaining from missed dose. |
| Two consecutive missed doses | Eq.18-2 | subtract contributions of two missed doses. |
| 9-13-17-21 institutional regimen | Eq.18-3 | 24 h repeating cycle with unequal intra-day intervals. |
| Dose and interval both unequal | Eq.18-4 | sum remaining amounts from prior doses; doses >4 patient half-lives ago may be disregarded. |

**Worked examples retained**

- Digoxin: typical patient missing two 0.25 mg daily doses gives expected concentration 0.39 µg/L, below therapeutic range 0.8–2.0 µg/L [R&T p.602].
- Vancomycin 9-13-17-21: 20 kg, 5-year-old, V 14 L, CL 3.3 L/h, k 0.24 h⁻¹, 250 mg regimen gives 8:00 concentration 2.03 mg/L vs therapeutic 5–15 mg/L [R&T pp.602–603].
- Erratic vancomycin: 68 kg, 60-year-old male, SCr 2.2 mg/dL, CLcr 34 mL/min, V 42.2 L, k 0.049 h⁻¹; observed 34 mg/L vs predicted 33.7 mg/L, indicating kinetics consistent but dose too high [R&T p.604].

**Deleted claim**  
“TDM 환자의 80%” is not source-backed and is removed.

<!-- TRENCH -->
**Trench-Level Tip**: adherence phantom을 IIV로 흡수하지 말라. dosing history와 sampling time은 clerical detail이 아니라 model input이다.

> **Practice Lens — TEXTBOOK_DERIVED**  
> Missed, unequal, erratic dosing은 예외 처리 항목이 아니라 superposition의 일반 적용이다. dose history와 sampling time을 narrative가 아니라 parameter estimation의 입력으로 취급해야 한다.


<!-- RECAP -->
**§2 recap**: Ch.6이 model 후보를 만들고, Ch.15가 patient-specific parameter deviation을 설명하며, PK35가 posterior parameter를 추정하고, Ch.18이 그 추정을 dosing and monitoring decision으로 변환한다.

---

# §5 — Confusion Pair Dissection

## §5.1 — Effect compartment vs turnover

<!-- CONFUSION -->
| Pair | Wrong shortcut | Correct discriminator |
|---|---|---|
| Effect compartment | “delay가 있으면 모두 turnover” | Delay가 있으나 dose-dependent peak-shift가 뚜렷하지 않으면 Ce equilibration이 우선 후보. |
| Turnover | “response가 늦으면 link model” | baseline, rebound, adaptation, dose-dependent shift가 보이면 production/loss process 자체가 변한 것일 수 있다. |

**One-line lock**: Effect compartment는 response site equilibration delay이고, turnover는 response system의 input/output rate가 drug에 의해 변하는 것이다 [G&W pp.425–426].

---

## §5.2 — Left-shift vs right-shift peak movement

<!-- CONFUSION -->
| Pattern | Misread | Locked interpretation |
|---|---|---|
| Leftward trough shift | “무조건 receptor on/off” | turnover loss stimulation과 receptor on/off가 모두 후보가 될 수 있다. |
| Rightward trough shift + flat high-dose portion | “absorption delay” | input inhibition with saturation가 강한 후보가 된다. |

**One-line lock**: 방향은 확정 규칙이 아니라 competing models를 줄이는 sign이다 [G&W pp.424–428].

---

## §5.3 — Bayesian “no concentration” vs “no prior”

<!-- CONFUSION -->
| Condition | Estimate behavior | Risk |
|---|---|---|
| No concentration | population average dominates | patient-specific deviation missed. |
| No prior | concentration fit dominates | sparse or mistimed concentrations can yield physiologically implausible parameters. |
| Prior + concentration | Bayesian compromise | only useful if dosing/sampling/assay history is reliable. |

**One-line lock**: Bayesian TDM의 central skill은 “posterior number를 믿는 것”이 아니라 likelihood와 prior의 relative information weight를 읽는 것이다 [G&W pp.641–643; R&T pp.597, 605–606].

---

## §5.4 — Hepatic high-extraction drug vs renal-excreted drug

<!-- CONFUSION -->
| Drug situation | Primary altered quantity | Dosing implication |
|---|---|---|
| High-extraction oral hepatic drug in cirrhosis | F increases; CL may decrease | oral exposure may rise sharply. |
| Low-extraction albumin-bound drug | fu increases; total CL can increase while unbound CL may not | total concentration target may need reinterpretation. |
| Renal-excreted unchanged drug | RF lowers renal CL component | Rd framework can guide maintenance dose. |

**One-line lock**: hepatic disease is not “liver bad = all CL down”; extraction ratio, F, protein binding, and unbound CL decide direction [R&T pp.444–446].

---

## §5.5 — Loading dose vs maintenance dose

<!-- CONFUSION -->
| Decision | Dominant parameter | Common error | Correct move |
|---|---|---|---|
| Loading dose | V and target concentration | reduce LD only because CLcr is low | check whether V changed; renal impairment alone does not imply LD reduction. |
| Maintenance dose | CL and target average exposure | use V logic for long-term dosing | adjust by CL/RF/Rd and update with TDM if criteria justify. |
| TCS interpretation | concentration, timing, history, assay | use a measured level without Table 18-6 data | reconstruct dosing/sampling history first. |

**Corrected Fig.18-5 statement**: V is about 45% covariate-explained, hepatic CL about 40%, renal CL about 80%, and F about 5% in the schematic variability partition; these are not loading-dose “accuracy” values [R&T p.582].

<!-- RECAP -->
**§5 recap**: 대부분의 오류는 하나의 관찰값을 하나의 원인으로 고정할 때 발생한다. 이 세션의 판단 단위는 단일 수치가 아니다. shape, covariate, dose history, sampling time의 joint interpretation이다.

---

# §7 — Self-Test: Active Recall Module

<!-- SELF-TEST -->
## Q1
Response-time curve에서 baseline, time-delay, peak-shift, saturation/slope를 왜 같은 순서로 읽어야 하는가?

**Answer**: baseline이 drift하거나 adaptation/rebound가 있으면 direct model 해석이 먼저 깨지고, time-delay와 peak-shift는 effect-site delay, turnover, receptor on/off 후보를 나누며, saturation/slope는 high-dose에서 nonlinear process를 드러내기 때문이다 [G&W pp.423–424].

## Q2
Case B leftward peak-shift를 “모델 클래스 확정”으로 쓰면 왜 위험한가?

**Answer**: leftward shift는 turnover loss stimulation이나 receptor on/off 등 복수 후보를 남기는 diagnostic signal이다. 원문은 potential models를 평가하라고 제시하지, 방향만으로 model을 확정하라고 하지 않는다 [G&W pp.424–428].

## Q3
Effect compartment와 turnover model의 가장 짧은 구분법은?

**Answer**: Effect compartment는 concentration이 effect site로 늦게 equilibration되는 delay이고, turnover는 response variable의 production/loss rate 자체가 drug에 의해 변하는 delay이다 [G&W pp.425–426].

## Q4
Bayesian TDM에서 concentration이 없을 때와 prior가 없을 때의 극단은 어떻게 다른가?

**Answer**: concentration이 없으면 population average가 추정값이 되고, prior가 없으면 concentration-only maximum likelihood에 가까워진다. Sparse concentration + weak prior는 physiologically implausible V/CL을 만들 수 있다 [G&W pp.641–643].

## Q5
PK35 digoxin case에서 반드시 보존해야 할 numeric anchors는?

**Answer**: 55세 60 kg CHF 남성, Lanoxicap 0.2 mg daily, 2.5 µg/L at 458 h, 0.9 µg/L at 479 h, CLpop 1.8 L/h, Vpop 500 L, estimated CL 5.7 L/h, V 119.6 L, t½ 14.5 h [G&W pp.641–643].

## Q6
`Rd = RF·fe + (1−fe)`에서 fe와 RF를 분리해야 하는 이유는?

**Answer**: fe는 drug property이고 RF는 patient property이다. 둘을 분리해야 renal impairment가 maintenance exposure에 미치는 영향을 정량화할 수 있다 [R&T pp.450–453].

## Q7
AKI에서 Cockcroft-Gault를 그대로 적용하면 왜 위험한가?

**Answer**: SCr는 renal function의 즉시값이 아니라 creatinine turnover가 반영된 지연값이다. 급성 변화에서는 실제 RF가 SCr 기반 추정보다 더 낮을 수 있다 [R&T pp.459–461].

## Q8
Hemodialysis에서 half-life가 크게 줄면 보충 용량이 항상 필요한가?

**Answer**: 아니다. dialysis session 동안 실제 body amount가 얼마나 제거되었는지가 중요하다. Vu가 크거나 CLu가 CLuD보다 훨씬 크면 single session의 fraction removed는 작을 수 있다 [R&T pp.471–472].

## Q9
TCS 후보 약물이면 항상 concentration monitoring을 해야 하는가?

**Answer**: 아니다. Good concentration-response relationship, high probability of therapeutic failure, population PK information, reliable assay, decision 전에 도착하는 turnaround time이 대부분 충족되어야 routine strategy가 된다 [R&T pp.594–597].

## Q10
Phenytoin에서 total concentration target을 그대로 해석하면 왜 틀릴 수 있는가?

**Answer**: phenytoin은 albumin binding과 saturable metabolism이 중요하다. Uremia, surgery, displacement drugs에서 altered protein binding이 예상되면 same unbound therapeutic concentration을 맞추도록 total target을 조정해야 한다 [R&T pp.588, 595–596].

## Q11
Loading dose와 maintenance dose를 한 문장으로 구분하라.

**Answer**: Loading dose는 V와 target concentration의 문제이고, maintenance dose는 CL과 target average exposure의 문제이다 [R&T pp.584–586].

## Q12
Fig.18-5를 “V는 정확히 예측 가능하다”로 읽으면 왜 틀린가?

**Answer**: Fig.18-5는 variability partition이다. V는 약 45% explained, 55% unaccounted이고, hepatic CL은 약 40%, renal CL은 약 80% explained로 제시된다. 이는 prediction accuracy 값이 아니다 [R&T p.582].

## Q13
Vancomycin 9-13-17-21 regimen 예제가 가르치는 핵심은?

**Answer**: 24 h total daily dose가 같아도 unequal intra-day intervals는 trough를 크게 낮출 수 있다. 예제에서 250 mg 9-13-17-21 regimen은 8:00 concentration 2.03 mg/L로 therapeutic range 5–15 mg/L보다 낮다 [R&T pp.602–603].

## Q14
Q8 digoxin 처방 권고를 source-locked answer로 쓰면 안 되는 이유는?

**Answer**: PK35는 Bayesian CL/V/t½ 추정 사례이지 loading 0.4 mg 또는 maintenance 0.1–0.125 mg/day를 직접 권고하는 처방 문서가 아니다. 그런 답은 `[교과서 외 통합 추론 예시]`로만 제시해야 한다 [G&W pp.641–643].

<!-- RECAP -->
**§7 recap**: self-test의 목적은 계산 정답보다 “어떤 정보가 없으면 해석이 불가능한가”를 즉시 말하게 만드는 것이다.

---

# §8 — Meta-Frame & Big Picture

## A. 이 세션의 위치

이 세션은 pharmacometrics 학습에서 “model building”과 “clinical dosing decision” 사이의 빈틈을 메운다. 즉, 모델을 만든 뒤 실제 환자 용량 판단으로 넘어가는 연결부를 다룬다. Ch.6은 model structure를 좁히는 눈을 만들고, Ch.15는 disease가 parameter를 어떻게 움직이는지 설명하며, PK35는 individual parameter를 posterior estimate로 만들고, Ch.18은 그 estimate를 loading, maintenance, monitoring, missed-dose interpretation으로 바꾼다.

## B. Four meta-patterns

1. **Two-factor product**: Rd는 `fe × RF`, forgiveness는 `t½/τ × therapeutic window`, TCS는 `risk × measurability`처럼 두 축이 함께 움직인다.
2. **Identifiability depends on sampling geometry**: early concentration은 V, later/steady-state concentration은 CL을 더 잘 식별한다.
3. **Continuous reality, discrete communication**: renal impairment stage, TCS candidate list, dialysis thresholds는 communication tools이지 hard biological cutoffs가 아니다.
4. **Anatomy of CL determines dose logic**: renal CL-dominant, hepatic CL-dominant, high-extraction, low-extraction, protein-bound drug은 같은 “CL 감소” 언어로 묶을 수 없다.

## C. Source-locked professional moat

- Plot shape를 보고 ODE 후보를 줄인다.
- fe/RF/Rd로 renal disease maintenance adjustment를 계산한다.
- C-G를 쓰되 SCr lag와 body composition caveat를 같이 판단한다.
- Bayesian output을 prior, concentration, sampling time, dosing history의 산물로 읽는다.
- TCS를 약물명 자동 적용이 아니라 criteria-based adjunct strategy로 운용한다.
- LD와 MD를 V vs CL 문제로 분리한다.
- Missed/erratic dosing을 “자료 오염”이 아니라 superposition problem으로 계산한다.

## D. PK15 closing bridge

PK15는 처방 자체가 아니라 “선택된 용량에서 어떤 exposure와 safety margin을 보고할 것인가”를 담당한다. 10/56/320 µmol·day⁻¹·kg⁻¹ dose levels, Cmax/AUC exposure reporting, therapeutic concentration 0.05–0.1 µM, high-dose Cmax approximately 50 µM, >100-fold safety margin은 clinical dosing chain의 마지막 reporting layer로만 사용한다 [G&W pp.546–548].

## E. Final locked caution list

```text
Do not say:
- peak-shift direction = model class
- TCS candidate drug = mandatory TCS
- V/CL Fig.18-5 percentages = dosing accuracy
- PK35 digoxin case = direct prescription recommendation
- TDM patients are 80% irregular dosing
- hemodialysis decision = simple Vu<120 AND CLu<CLuD rule
- NDA/IND/RMP/software workflow = textbook source claim
```

```text
Say instead:
- peak-shift direction narrows competing models
- TCS is useful as adjunct when criteria are satisfied
- Fig.18-5 is variability partition
- PK35 estimates individual CL/V/t½; prescription is separate inference
- missed/unequal/erratic dosing is common enough to need equations, without source-free percentages
- dialysis effectiveness lies on Vu·CLu·CLuD coordinate plane
- implementation/regulatory extrapolations require [교과서 외 구현/규제 번역]
```

<!-- RECAP -->
**Final recap**: Content Lock v1 keeps the capstone spine but removes deterministic overclaims, unsupported percentages, unlabelled regulatory/software extrapolations, and direct prescription claims not present in the PDF. The locked document is now ready for Phase 4B readability and Phase 4C visual triage.


---

# PART B — Compiler-Only Appendix

This appendix is not learner-facing. It exists only to protect Phase 5 rendering fidelity and prevent regression.

### B1. Compilation Contract

- PART A is the only learner-facing body.
- Phase 5 must render PART A without altering content.
- PART B is instruction/guardrail only.
- Do not restore deprecated material.
- Do not add new scientific content.
- Do not render PART B as learner content unless explicitly requested.

### B2. Figure Rendering Instructions

- Use the approved Phase 4C figure strategy only.
- Preserve Mode P/R/N decisions exactly.
- Image rights = None: do not embed copyrighted textbook images.
- Render `FIGURE_POINTER` as text-only textbook reference callouts.
- Render `FIGURE_SCHEMATIC` only as visually distinct new schematic based on the brief; do not reproduce textbook figures.
- Do not propose additional figures.
- Do not generate Mermaid/SVG in Phase 4D; Phase 5 may render approved schematic briefs only.

#### Approved Phase 4C Figure Strategy / Insertion Map

```markdown
# 16_Content Lock v2.1 — Figure Marker Patch
## 임상 통합 캡스톤: 패턴 인식 · TDM · 질환 · 치료 의사결정

**Output mode declaration**: PATCH MODE

**Mode rationale**: Content Lock v2는 본문 재출력 시 text drift 위험이 있는 장문 문서이므로, v2 본문 전체를 재출력하지 않는다. 본 산출물은 Strategy Table + Briefs + Insertion Map만 제공한다. Phase 5 operator는 아래 marker block을 Content Lock v2 원문에 splice하여 v2.1을 생성한다.

**Telos**: 그림을 만들지 않고, 그림의 필요성·위치·역할만 결정한다. Mermaid/SVG/HTML rendering은 Phase 5로 이월한다.

**Image rights decision**: Scope Lock의 Image rights = None. 따라서 원문 교과서 figure는 삽입하지 않고, 필요한 경우 Pointer(P) 또는 visually distinct schematic brief(R/N)만 사용한다.

---

## 1. Figure Strategy Table — View (A) Reading-order Figure Plan

| # | Reading order | Location (§ + concept card) | Mode | Source figure (if any) | Trigger | Why text alone is insufficient | Expected learning gain | Decision |
|---:|---|---|---|---|---|---|---|---|
| F01 | 1 | §1 — Session Header & Roadmap / Capstone spine | N | None | G3, G4 | Text lists the chain, but the learner may not see that each block hands a specific decision object to the next block. | 전체 세션을 “model candidate → patient deviation → posterior parameter → dose decision → exposure report”의 단방향 clinical pharmacometrics pipeline으로 고정한다. | KEEP |
| F02 | 2 | §2.1 — Pattern-recognition decision workflow | P | G&W Fig.6.1 [p.423]; G&W Fig.6.12 [pp.465–466] | G1, G3, G5 | Baseline/time-delay/peak-shift/saturation checks and the Fig.6.12 workflow are sequential operations; prose alone can make them sound like a flat checklist. | pattern recognition을 “관찰 항목 목록”이 아니라 “후보 모델 축소 절차”로 읽게 한다. | KEEP |
| F03 | 3 | §2.2 — Peak-shift + saturation | P | G&W Fig.6.2 [p.424]; G&W Fig.6.3 [p.428] | G2, G5 | left/right shift, flat portion, and competing model options are spatial pattern differences; text alone invites deterministic over-reading. | “peak-shift direction = model class” 오류를 막고, directionality를 diagnostic signal로 위치시킨다. | KEEP |
| F04 | 4 | §2.4 — Bayesian objective function for individual TDM | P | G&W Fig.35.1 [pp.641–642]; R&T Fig.18-13 [pp.605–606] | G1, G2, G5 | Bayesian prior/likelihood weighting and sampling-time identifiability are difficult to internalize from equations alone. | posterior estimate를 “농도 하나의 산물”이 아니라 prior, concentration, timing geometry의 결합으로 읽게 한다. | KEEP |
| F05 | 5 | §2.5 — Disease/RF/Rd framework | R | R&T Fig.15-8 [p.453]; R&T Fig.15-9 [p.454] | G1, G2, G5 | `fe` and `RF` are two axes; prose makes learners collapse drug property and patient property into one “renal impairment” label. | Rd를 drug-specific `fe`와 patient-specific `RF`의 product decision으로 보는 구조가 고정된다. | KEEP |
| F06 | 6 | §2.7 — Hemodialysis coordinate plane | P | R&T Fig.15-18 [p.471]; R&T Fig.15-19 [p.473] | G1, G2, G5 | dialysis effectiveness is a continuous Vu·CLu·CLuD surface, not a verbal threshold; text alone reverts to hard-rule thinking. | half-life shortening과 amount removed를 분리하고, post-dialysis supplement 판단을 좌표 평면으로 읽게 한다. | KEEP |
| F07 | 7 | §2.9 — Loading dose vs maintenance dose | P | R&T Fig.18-5 [p.582] | G2, G5 | Fig.18-5 was a prior source of misreading as “accuracy”; learners need to inspect it as variability partition. | V, hepatic CL, renal CL, F의 explained/unaccounted variability를 dose-component confidence 문제로 연결한다. | KEEP |
| R01 | — | §2.8 — Target Concentration Strategy criteria | P candidate | R&T Table 18-5 [pp.595–596]; Table 18-6 [p.597] | G2, G5 | Important but table content is already summarized in the card. | Could reinforce interpretation gate, but would exceed pointer budget. | REJECT — budget lower than F02/F03/F04/F06/F07 |
| R02 | — | §2.10 — Missed / unequal / erratic dosing framework | P candidate | R&T Fig.18-11 [p.601]; Fig.18-12 [p.603] | G1, G5 | Superposition is visual, but the card already includes equations and worked examples. | Useful for Phase 5 optional expansion, not essential in v2.1 budget. | REJECT — pointer budget exhausted |
| R03 | — | §8 — PK15 closing bridge | P candidate | G&W Fig.15.1–15.3 [pp.546–548] | G3, weak G5 | PK15 is a closing reporting layer, not a §2 core mechanism card. | Would support safety-margin reporting but not structural understanding of the capstone spine. | REJECT — B-standard bridge; lower ROI |

---

## 2. Figure Strategy Table — View (B) Type-sorted Summary

**Pointers (P)**: F02, F03, F04, F06, F07 → 5 / max 5 for A-Critical budget.

**Schematics (R/N combined)**: F01, F05 → 2 / max 2 for A-Critical budget.

**Images (I)**: none → Image rights = None; no direct image insertion.

**Rejected after budget enforcement**: R01, R02, R03. These are educationally useful but not retained because they either repeat text already locked, exceed pointer budget, or belong to a lower-priority closing bridge.

---

## 3. Figure Briefs — KEEP Items Only

### F01 — New schematic: Capstone decision pipeline

- **Title**: Session 016 Capstone Spine — from data shape to exposure report
- **Mode**: N
- **Visual objective**: 5초 안에 “각 챕터가 다음 챕터에 넘기는 decision object”를 보이게 한다.
- **Core message**: Ch.6은 model candidate를, Ch.15는 patient deviation을, PK35는 posterior parameter를, Ch.18은 dose/monitoring decision을, PK15는 exposure/safety-margin report를 만든다.
- **Elements to include**:
  - Five horizontal blocks: Ch.6 Pattern Recognition → Ch.15 Disease/RF/Rd → PK35 Bayesian TDM → Ch.18 Dosing/Monitoring → PK15 Toxicokinetics
  - Under each block: output label only — model candidate, patient deviation, posterior parameter, dose decision, exposure report
  - One small caution strip: “implementation/regulatory translation requires label”
- **Elements to exclude**:
  - Drug examples, numeric anchors, source page tags, software names beyond the caution label
  - Any regulatory workflow diagram
- **Suggested rendering**: Mermaid flowchart
- **Caption**: Session 016은 독립 개념 묶음이 아니라, data shape에서 clinical exposure reporting으로 이어지는 단일 decision chain이다.
- **Alt text**: Five-step left-to-right pipeline connecting pattern recognition, disease adjustment, Bayesian estimation, therapeutic decision-making, and toxicokinetic reporting.
- **Source relation**: Newly designed

### F02 — Pointer: Pattern-recognition checklist and workflow

- **Source**: Gabrielsson & Weiner Ch.6, Fig.6.1 [p.423] and Fig.6.12 [pp.465–466]
- **Why this figure matters**: Fig.6.1 shows the initial visual grammar — baseline, time-delay, peak-shift, saturation, slopes. Fig.6.12 converts that grammar into a practical analysis workflow.
- **When to look**: After reading §2.1, before moving to §2.2.
- **Learner instruction**: Inspect Fig.6.1 first as the checklist, then Fig.6.12 as the decision workflow. Do not treat the checklist items as independent facts; follow how each observation narrows the next model question.

### F03 — Pointer: Peak-shift and competing model options

- **Source**: Gabrielsson & Weiner Ch.6, Fig.6.2 [p.424] and Fig.6.3 [p.428]
- **Why this figure matters**: Fig.6.2 makes the leftward vs rightward response-time movement visible. Fig.6.3 prevents the common error of mapping one pattern to one model by showing competing alternatives.
- **When to look**: Immediately after reading the table in §2.2.
- **Learner instruction**: Compare Case A, B, and C by looking only at timing of the trough and high-dose flattening. Then check Fig.6.3 to ask which competing models remain rather than choosing one model prematurely.

### F04 — Pointer: Bayesian estimation and sampling-time confidence

- **Source**: Gabrielsson & Weiner PK35, Fig.35.1 [pp.641–642]; Rowland & Tozer Ch.18, Fig.18-13 [pp.605–606]
- **Why this figure matters**: Fig.35.1 links patient-specific clearance variability to concentration-time behavior. Fig.18-13 shows why sampling time changes confidence in V vs CL estimates.
- **When to look**: After the “Sampling identifiability anchor” paragraph in §2.4.
- **Learner instruction**: First inspect how CL variability changes predicted concentration-time curves. Then inspect Fig.18-13 and ask whether the available sample is V-informative, CL-informative, or ambiguous.

### F05 — Redraw: Rd as a two-axis decision surface

- **Title**: Rd Framework — drug property `fe` × patient property `RF`
- **Mode**: R
- **Visual objective**: 5초 안에 renal dose adjustment가 “renal impairment label”이 아니라 `fe`와 `RF`의 interaction임을 보이게 한다.
- **Core message**: Maintenance adjustment becomes large only when the drug depends substantially on renal excretion and the patient’s renal function is meaningfully reduced.
- **Elements to include**:
  - X-axis: `RF` from normal to severe impairment
  - Y-axis or layered bands: `fe` low / moderate / high
  - Output zone: `Rd` close to 1 vs reduced
  - Annotation: `fe = drug property`, `RF = patient property`, `Rd = maintenance requirement`
  - Small callout: “LD is separate unless V changes”
- **Elements to exclude**:
  - Exact reproduction of textbook curves
  - Multiple drug examples
  - Cockcroft-Gault equation details
- **Suggested rendering**: inline SVG
- **Caption**: Rd는 신기능 저하 자체가 아니라 drug-specific `fe`와 patient-specific `RF`의 조합으로 maintenance requirement를 줄인다.
- **Alt text**: A two-axis conceptual surface showing renal function on one axis, fraction excreted unchanged on another, and maintenance dose requirement decreasing most when both renal dependence and impairment are high.
- **Source relation**: Redrawn from textbook concept

### F06 — Pointer: Hemodialysis fraction removed and supplement principle

- **Source**: Rowland & Tozer Ch.15, Fig.15-18 [p.471] and Fig.15-19 [p.473]
- **Why this figure matters**: Fig.15-18 shows why dialysis removal is a continuous function of Vu and CLu, not a hard threshold. Fig.15-19 connects removal during dialysis to the replacement-dose concept.
- **When to look**: After the “Locked correction” block in §2.7.
- **Learner instruction**: Inspect Fig.15-18 before applying any supplement rule. Ask whether the patient-drug pair sits in a region where dialysis removes clinically meaningful body amount during the session.

### F07 — Pointer: Variability partition for PK parameters

- **Source**: Rowland & Tozer Ch.18, Fig.18-5 [p.582]
- **Why this figure matters**: This figure was central to correcting the mistaken “V/CL prediction accuracy” reading. It should be inspected as a variability partition, not as a promise of dosing precision.
- **When to look**: Immediately after the “Corrected Fig.18-5 lock” paragraph in §2.9.
- **Learner instruction**: Read the figure by asking what fraction of variability is explained and what remains unaccounted. Then connect that to why renal CL may support stronger maintenance prediction than hepatic CL or F.

---

## 4. Insertion Map (PATCH MODE)

| # | Reading order | Anchor copied verbatim from Content Lock v2 | Insert position | Marker block ID |
|---:|---|---|---|---|
| F01 | 1 | `**§1 recap**: 이 세션은 “모델 선택 → 질환 보정 → 개인 추정 → 처방·monitoring → exposure reporting”의 단일 clinical pharmacometrics chain을 잠근다.` | after this anchor paragraph | MB-F01 |
| F02 | 2 | `§2.1은 plot-reading grammar이고, §2.2–§2.3은 그 grammar가 실제 ODE 후보로 내려가는 첫 번째 mechanistic bridge이다.` | after this anchor card, before `## §2.2` | MB-F02 |
| F03 | 3 | `**Trench-Level Tip**: Case B left-shift를 “kon이 큰 약물”로 외우지 말라. receptor on/off에서는 finite receptor pool 때문에 nadir가 빨라질 수 있고, turnover model에서도 loss stimulation이 유사한 pattern을 만들 수 있다.` | after this anchor card, before `## §2.3` | MB-F03 |
| F04 | 4 | `PK35 digoxin 사례는 CL/V/t½ 추정 사례이다. Loading dose 0.4 mg, maintenance 0.1–0.125 mg/day 같은 처방 문장은 교과서 직접 권고가 아니라 `[교과서 외 통합 추론 예시]`로만 다룬다. Sheiner 1977을 NONMEM의 직접 조상으로 단정하는 표현은 `[확인 필요]`이다.` | after this anchor card, before `## §2.5` | MB-F04 |
| F05 | 5 | `**Trench-Level Tip**: phenytoin처럼 albumin-bound low-extraction drug에서는 fu↑가 total concentration 해석을 망친다. total target을 그대로 쓰면 같은 unbound exposure를 과소평가할 수 있다.` | after this anchor card, before `## §2.6` | MB-F05 |
| F06 | 6 | `**Trench-Level Tip**: Phenobarbital의 dialysis half-life가 크게 줄어도 single 3 h session에서 body amount가 충분히 빠지지 않을 수 있다. half-life shortening and amount removed are not the same endpoint.` | after this anchor card, before `## §2.8` | MB-F06 |
| F07 | 7 | `**Trench-Level Tip**: “신부전이므로 LD도 줄인다”는 자동 규칙은 틀릴 수 있다. LD는 V 문제이고 MD는 CL 문제이다. 단, digoxin uremia처럼 V 자체가 변하는 예외는 따로 잡는다.` | after this anchor card, before `## §2.10` | MB-F07 |

---

## 5. Marker Block Registry

### MB-F01

```text
<!-- FIGURE_SCHEMATIC -->
Title: Session 016 Capstone Spine — from data shape to exposure report
Mode: N
Visual objective: 5초 안에 각 챕터가 다음 챕터에 넘기는 decision object를 보이게 한다.
Core message: Ch.6은 model candidate를, Ch.15는 patient deviation을, PK35는 posterior parameter를, Ch.18은 dose/monitoring decision을, PK15는 exposure/safety-margin report를 만든다.
Elements to include: Five horizontal blocks: Ch.6 Pattern Recognition → Ch.15 Disease/RF/Rd → PK35 Bayesian TDM → Ch.18 Dosing/Monitoring → PK15 Toxicokinetics; under each block, output label only: model candidate, patient deviation, posterior parameter, dose decision, exposure report; one small caution strip: implementation/regulatory translation requires label.
Elements to exclude: Drug examples, numeric anchors, source page tags, software names beyond the caution label, any regulatory workflow diagram.
Suggested rendering: Mermaid
Caption: Session 016은 독립 개념 묶음이 아니라, data shape에서 clinical exposure reporting으로 이어지는 단일 decision chain이다.
Alt text: Five-step left-to-right pipeline connecting pattern recognition, disease adjustment, Bayesian estimation, therapeutic decision-making, and toxicokinetic reporting.
Source relation: Newly designed
<!-- /FIGURE_SCHEMATIC -->
```

### MB-F02

```text
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner Ch.6, Fig.6.1 [p.423] and Fig.6.12 [pp.465–466]
Why this matters: Fig.6.1 shows the initial visual grammar — baseline, time-delay, peak-shift, saturation, slopes. Fig.6.12 converts that grammar into a practical analysis workflow.
When to look: after reading this card, before moving to §2.2
Learner instruction: Inspect Fig.6.1 first as the checklist, then Fig.6.12 as the decision workflow. Do not treat the checklist items as independent facts; follow how each observation narrows the next model question.
<!-- /FIGURE_POINTER -->
```

### MB-F03

```text
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner Ch.6, Fig.6.2 [p.424] and Fig.6.3 [p.428]
Why this matters: Fig.6.2 makes the leftward vs rightward response-time movement visible. Fig.6.3 prevents the common error of mapping one pattern to one model by showing competing alternatives.
When to look: immediately after reading this card
Learner instruction: Compare Case A, B, and C by looking only at timing of the trough and high-dose flattening. Then check Fig.6.3 to ask which competing models remain rather than choosing one model prematurely.
<!-- /FIGURE_POINTER -->
```

### MB-F04

```text
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner PK35, Fig.35.1 [pp.641–642]; Rowland & Tozer Ch.18, Fig.18-13 [pp.605–606]
Why this matters: Fig.35.1 links patient-specific clearance variability to concentration-time behavior. Fig.18-13 shows why sampling time changes confidence in V vs CL estimates.
When to look: after the Sampling identifiability anchor paragraph in this card
Learner instruction: First inspect how CL variability changes predicted concentration-time curves. Then inspect Fig.18-13 and ask whether the available sample is V-informative, CL-informative, or ambiguous.
<!-- /FIGURE_POINTER -->
```

### MB-F05

```text
<!-- FIGURE_SCHEMATIC -->
Title: Rd Framework — drug property fe × patient property RF
Mode: R
Visual objective: 5초 안에 renal dose adjustment가 renal impairment label이 아니라 fe와 RF의 interaction임을 보이게 한다.
Core message: Maintenance adjustment becomes large only when the drug depends substantially on renal excretion and the patient’s renal function is meaningfully reduced.
Elements to include: X-axis: RF from normal to severe impairment; Y-axis or layered bands: fe low, moderate, high; output zone: Rd close to 1 vs reduced; annotation: fe = drug property, RF = patient property, Rd = maintenance requirement; small callout: LD is separate unless V changes.
Elements to exclude: Exact reproduction of textbook curves, multiple drug examples, Cockcroft-Gault equation details.
Suggested rendering: SVG
Caption: Rd는 신기능 저하 자체가 아니라 drug-specific fe와 patient-specific RF의 조합으로 maintenance requirement를 줄인다.
Alt text: A two-axis conceptual surface showing renal function on one axis, fraction excreted unchanged on another, and maintenance dose requirement decreasing most when both renal dependence and impairment are high.
Source relation: Redrawn from textbook concept
<!-- /FIGURE_SCHEMATIC -->
```

### MB-F06

```text
<!-- FIGURE_POINTER -->
Source: Rowland & Tozer Ch.15, Fig.15-18 [p.471] and Fig.15-19 [p.473]
Why this matters: Fig.15-18 shows why dialysis removal is a continuous function of Vu and CLu, not a hard threshold. Fig.15-19 connects removal during dialysis to the replacement-dose concept.
When to look: after the Locked correction block in this card
Learner instruction: Inspect Fig.15-18 before applying any supplement rule. Ask whether the patient-drug pair sits in a region where dialysis removes clinically meaningful body amount during the session.
<!-- /FIGURE_POINTER -->
```

### MB-F07

```text
<!-- FIGURE_POINTER -->
Source: Rowland & Tozer Ch.18, Fig.18-5 [p.582]
Why this matters: This figure was central to correcting the mistaken V/CL prediction accuracy reading. It should be inspected as a variability partition, not as a promise of dosing precision.
When to look: immediately after the Corrected Fig.18-5 lock paragraph in this card
Learner instruction: Read the figure by asking what fraction of variability is explained and what remains unaccounted. Then connect that to why renal CL may support stronger maintenance prediction than hepatic CL or F.
<!-- /FIGURE_POINTER -->
```

---

## 6. Phase 5 Splicing Notes

1. Apply marker blocks in reading order F01 → F07.
2. Do not modify any Content Lock v2 body text, source page tags, equations, annotations, `[확인 필요]`, or `[p.확인 필요]` items.
3. Mode P markers remain callouts only; no textbook image should be embedded.
4. Mode R/N markers are briefs only. Phase 5 may render them as visually distinct Mermaid/SVG outputs, but must not reproduce copyrighted textbook figures.
```

### B3. Page Tag Rendering Rules

- Preserve all `[p.XX]`, `[pp.XX–YY]`, `[pp.XX, YY]`, and `[p.확인 필요]` tags.
- Render page tags visibly in HTML.
- Do not fabricate, delete, renumber, or relocate page tags.
- `[p.확인 필요]` remains visible unless already resolved by Audit/Content Lock.
- Do not hide source page tags in print mode.

### B4. HTML Compiler Requirements

The following compiler prompt is the controlling Phase 5 rendering contract. It is not learner-facing.

```text
ROLE: Education UX Engineer.
Function: transform Content Lock v2.1 into a production-quality HTML file.
You render content. You do not alter it.

If inputs include a PATCH MODE Insertion Map (instead of a fully-marked v2.1):
  Step 1 (mandatory): Splice each marker block into Content Lock v2 at the specified
                      anchor location, producing a working v2.1 in memory.
                      Do not modify any other text.
  Step 2 (mandatory): Output a Splice Verification Table BEFORE rendering HTML.
                      If any anchor cannot be matched exactly, STOP and report.
  Step 3:             Render HTML as below.

INPUT: Content Lock v2.1 (or Content Lock v2 + Insertion Map)
DESIGN REFERENCE: [attach reference HTML — T.E.A. Loop Playbook or equivalent]

=== PATCH MODE SPLICE VERIFICATION ===

When rendering from PATCH MODE inputs, output the following table BEFORE the HTML:

## Splice Verification Table (PATCH MODE only)

| Marker # | Anchor text (truncated to 60 chars) | Anchor found? | Match count | Inserted? | Final location (§ + card) |
|----------|-------------------------------------|---------------|-------------|-----------|---------------------------|

Rules:
- Anchor found?  : YES if exact substring match found in Content Lock v2; NO otherwise.
- Match count    : number of times the anchor appears (must be exactly 1 — see below).
- Inserted?      : YES only if Anchor found = YES AND Match count = 1.
- Final location : the § and concept card immediately preceding the inserted marker.

HALT CONDITIONS (do NOT proceed to HTML rendering if any apply):
  H1. Any "Anchor found?" = NO.
  H2. Any "Match count" ≠ 1 (zero matches OR multiple matches → ambiguous).
  H3. Any "Inserted?" = NO.

If a HALT condition triggers:
  Stop rendering. Output:
    "PATCH MODE SPLICE FAILED — N markers could not be inserted unambiguously.
     Return to Phase 4C and request anchor revision (verbatim, unique, ≥40 chars,
     extend to ≥60 chars if collision)."
  Do NOT guess insertion location.
  Do NOT proceed to HTML output.

If all markers pass: continue to HTML rendering and include the Splice Verification Table
as a comment block at the top of the HTML file (inside <!-- ... --> for traceability).

=== MARKER → COMPONENT MAPPING (mandatory) ===

| Marker / Pattern                  | HTML Component              | Style specification                                              |
|-----------------------------------|-----------------------------|------------------------------------------------------------------|
| <!-- MASTER LENS -->              | Callout box                 | border-left:4px solid #c9a84c; background:rgba(201,168,76,0.08)  |
| <!-- ANNOTATION -->               | Inline abbr / tooltip       | font-size:0.85em; color:var(--muted); font-style:italic          |
| <!-- ANCHOR -->                   | Bridge sentence             | font-style:italic; color:var(--muted)                            |
| <!-- TRENCH -->                   | Practical tip box           | border-left:4px solid var(--rose); background:rose-tint          |
| <!-- CONFUSION -->                | Side-by-side comparison     | .box.amber class                                                 |
| <!-- SELF-TEST -->                | Click-to-reveal accordion   | Question visible; answer hidden until click                      |
| <!-- RECAP -->                    | Section summary box         | border-left:4px solid var(--blue); background:blue-tint          |
| [확인 필요]                        | Highlighted flag            | <mark> tag                                                       |
| [p.XX] / [pp.XX–YY] / [pp.XX, YY] | Inline source page tag      | <span class="source-page">[p.XX]</span> — see CSS below          |
| [p.확인 필요]                      | Source page uncertainty tag | <span class="source-page source-uncertain">[p.확인 필요]</span>  |
| <!-- FIGURE_POINTER -->           | Textbook reference callout  | border-left:4px solid var(--purple); 📖 icon                     |
| <!-- FIGURE_SCHEMATIC -->         | Inline schematic <figure>   | Render via Mermaid (default) or inline SVG; <figcaption> below   |
| <!-- FIGURE_IMAGE_SLOT -->        | Image figure or placeholder | <figure> with <img> if file provided; styled placeholder if not  |

=== SOURCE PAGE TAG RENDERING RULES (v3.3.3 신설) ===

Source page tags are NOT HTML comment markers — they appear as plain text in
Content Lock v2.1 (e.g., "Concept Anatomy: Hepatic Clearance [p.123]").
The HTML compiler must detect them via pattern matching and wrap them in <span> elements.

Pattern detection (regex-equivalent, applied to body text only):
  - \[p\.(\d+)\]                 → standard single-page tag
  - \[pp\.(\d+)[–-](\d+)\]       → range tag (en-dash or hyphen)
  - \[pp\.(\d+(?:,\s*\d+)+)\]    → multi-page non-contiguous tag
  - \[p\.확인 필요\]              → uncertainty tag

Rendering:
  Standard tags  → <span class="source-page">[p.XX]</span>
  Uncertain tags → <span class="source-page source-uncertain">[p.확인 필요]</span>

Detection scope:
  - APPLY pattern detection to body text inside §2 cards, equation captions, and example headings.
  - DO NOT apply pattern detection inside <pre><code> blocks (preserve verbatim in code).
  - DO NOT apply pattern detection inside <!-- FIGURE_* --> marker blocks (those have their own
    internal "Source:" fields and are not body content tags).

Fabrication prohibition:
  - DO NOT add page tags that are not present in Content Lock v2.1.
  - DO NOT silently remove page tags during rendering.
  - DO NOT alter page numbers (e.g., normalizing en-dash to em-dash is permitted; changing
    page numbers is forbidden).

=== RENDERING REQUIREMENTS ===

Math      : MathJax CDN — inline \(...\), display \[...\]
Code      : <pre><code> dark background, language class attribute
Navigation: sticky left sidebar, anchor jump per § section
Accordion : Self-Test answers hidden by default; revealed on user click
Checklist : sessionStorage state persistence across page reload
Controls  : code block copy button, print/PDF button (window.print())
Responsive: ≤768px single-column + collapsed nav; ≥1024px two-column
Dark/Light: prefers-color-scheme auto-switch
Print     : remove backgrounds, hide navigation, optimize page-break-inside
            Source page tags MUST remain visible in print mode (do not hide via @media print).

=== NAVIGATION ANCHOR INTEGRITY RULES ===

The HTML must include a sticky left sidebar table of contents.

For every sidebar link:
- Use <a href="#..."> links only.
- Every href target must have a matching id in the body.
- Every major section heading (§1, §2, §3...) must receive a stable id.
- Every concept card inside §2 must also receive a stable id when possible.
- The href value and body id must match exactly, including spelling and hyphens.
- Do not create TOC links whose target id does not exist.
- Do not create duplicate ids.
- Enable smooth scrolling with:

html { scroll-behavior: smooth; }

Before finalizing, self-check:
1. Count all sidebar href="#id" values.
2. Confirm each id exists exactly once in the document.
3. Confirm no duplicate id exists in the body.
4. If any mismatch exists, fix before output.

Required implementation:
- The sidebar must be placed on the left side on desktop.
- The sidebar must remain visible while scrolling unless the viewport is mobile-sized.
- Each major section must be reachable by clicking the sidebar entry.
- Each §2 concept card should be reachable by clicking its sidebar sub-entry when concept-card headings are present.
- The active section may be highlighted using IntersectionObserver or equivalent JavaScript.
- On mobile viewports, the sidebar may collapse, but anchor navigation must still work.

=== FIGURE RENDERING RULES ===

GENERAL:
- Every figure marker becomes a proper <figure> block (or pointer callout) with caption and alt text.
- Figures must not interrupt reading flow — place at end of the concept card they belong to.
- Visual style consistent with the design system. No decorative imagery.
- Do not generate or embed figures not present in Content Lock v2.1.

FIGURE_POINTER:
- Render as a compact callout box with class .figure-pointer:
    border-left: 4px solid var(--purple);
    background: rgba(155, 89, 182, 0.06);
    icon: 📖
- Display: Source / Why this matters / When to look / Learner instruction.
- Do NOT generate or embed an image — pointer is text-only.

FIGURE_SCHEMATIC (Mode R or N):
- Default rendering: Mermaid via CDN (https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js).
  Use <div class="mermaid">...</div> inside <figure>.
- Use inline SVG only when the schematic requires curve plotting, precise spatial layout,
  or shapes Mermaid cannot express (e.g., concentration-time curves, radar plots).
- For comparison-style figures (Confusion-pair), CSS side-by-side cards (no SVG) are acceptable
  if the brief's "Suggested rendering" specifies CSS-card.
- Implement the brief faithfully: include only listed elements; exclude listed exclusions.
- Do not reproduce the textbook figure's exact layout, color palette, or label placement
  even when "Redrawn from textbook concept" — visual distinctness is mandatory.
- Caption: render as <figcaption>.
- Alt text: render as alt attribute on SVG container or aria-label on <figure>.
- Mermaid initialization in inline JS:
    mermaid.initialize({ startOnLoad: true, theme: 'neutral',
                         themeVariables: { fontFamily: 'var(--font)' } });

MERMAID SELF-CHECK (생성 직후 self-validate):
After generating each Mermaid block, verify all of the following BEFORE finalizing:
  M1. Block opens with a valid directive: flowchart TD | flowchart LR |
      graph TD | graph LR | sequenceDiagram | classDiagram | stateDiagram-v2 | erDiagram.
  M2. Node IDs contain ONLY [A-Za-z0-9_]. No parentheses, slashes, dots, hyphens,
      Korean characters, spaces, or quotes inside IDs.
  M3. Any label containing parentheses, special characters, or non-ASCII characters
      is wrapped in double quotes:  A["Clearance (CL)"]
  M4. Edge labels with special chars use the |"label"| form:  A -->|"Q × E"| B
  M5. Subgraph titles, when used, are quoted:  subgraph "Hepatic"
  M6. No trailing semicolons inside node definitions.
  M7. If any of M1–M6 cannot be satisfied OR Mermaid expressiveness is insufficient,
      FALLBACK to one of:
        - inline SVG (for spatial/curve figures)
        - CSS side-by-side cards (for comparison figures)
      Do not emit a Mermaid block that is likely to fail rendering.

FIGURE_IMAGE_SLOT:
- If Rights = User-supplied AND image file exists in working directory:
    <figure><img src="..." alt="..." /><figcaption>...</figcaption></figure>
- If Rights = Open-license AND license/attribution provided in marker:
    <figure>
      <img src="..." alt="..." />
      <figcaption>
        [Caption text]
        <span class="figure-attribution">
          Source: [Attribution]. License: [License type].
          [<a href="[Source URL]">link</a>]
        </span>
      </figcaption>
    </figure>
- If Rights = placeholder OR file unavailable:
    Render styled placeholder box with class .figure-placeholder:
    [📖 교과서 원그림 삽입 위치 — Source: Book, p.XX, Fig.Y]
    Do not generate an approximation of the textbook figure.

CAPTION & ALT TEXT (all schematic/image figures):
- Caption mandatory. Alt text mandatory. Both from the brief.

=== CSS DESIGN SYSTEM (inherit from reference) ===

Variables: --bg, --surface, --surface-2, --ink, --muted, --faint,
           --line, --line-strong, --blue, --green, --purple, --amber, --rose,
           --radius, --radius-sm, --shadow, --font, --mono

Add for navigation:
  html {
    scroll-behavior: smooth;
  }
  .sidebar {
    position: sticky;
    top: 0;
    align-self: start;
    height: 100vh;
    overflow-y: auto;
  }
  .sidebar a {
    display: block;
    text-decoration: none;
  }
  .sidebar a.active {
    font-weight: 700;
    border-left: 3px solid var(--purple);
  }
  @media (max-width: 768px) {
    .sidebar {
      position: static;
      height: auto;
      max-height: none;
    }
  }

Add for v3.3 figure components:
  .figure-pointer { border-left: 4px solid var(--purple); ... }
  figure { margin: 1.5em 0; }
  figcaption { color: var(--muted); font-size: 0.9em; margin-top: 0.5em; }
  .figure-attribution { display: block; font-size: 0.8em; margin-top: 0.3em;
                        color: var(--faint); }
  .figure-placeholder { border: 2px dashed var(--line-strong); padding: 2em;
                         text-align: center; color: var(--muted); }

Add for v3.3.3 source page tag components:
  .source-page {
    font-size: 0.78em;
    color: var(--purple);
    background: rgba(155, 89, 182, 0.10);
    padding: 2px 6px;
    border-radius: 6px;
    vertical-align: super;
    white-space: nowrap;
    margin-left: 0.25em;
    font-weight: 500;
    letter-spacing: 0.01em;
  }
  .source-page.source-uncertain {
    color: var(--amber);
    background: rgba(245, 158, 11, 0.12);
    border: 1px dashed var(--amber);
  }
  /* Print: keep tags visible for offline traceability */
  @media print {
    .source-page {
      background: transparent;
      color: #000;
      border: 1px solid #888;
    }
  }
  /* Hover: subtle elevation to confirm interactivity (if linked to PDF in future) */
  .source-page:hover {
    background: rgba(155, 89, 182, 0.18);
  }

=== OUTPUT SPECIFICATION ===

Single HTML file with all custom CSS and custom JS inline.
External runtime dependencies are allowed ONLY for:
  - MathJax CDN
  - Mermaid CDN
  - cdnjs.cloudflare.com library list (e.g., highlight.js for code coloring)
No external local .css / .js / font / image files unless explicitly supplied by the user.
File header comment block: document title | chapter | generation date.
PATCH MODE only: include Splice Verification Table as a comment block in the HTML header.

=== PROHIBITED ===

- <iframe>, <embed>, external .js files (other than permitted CDNs), external local .css
  files, external font files (other than permitted CDNs).
- Any modification to Content Lock v2.1 text content (including page tag text).
- Self-Test answer text visible without user interaction.
- Markers rendered as plain text (every marker must become its mapped component).
- Source page tags rendered as plain bracketed text without <span> wrapping.
- Reproducing copyrighted textbook figures exactly when rendering R/N schematics.
- Embedding textbook images without User-supplied or Open-license rights with attribution.
- Emitting Mermaid blocks that fail M1–M6 self-check.
- Proceeding to HTML rendering when any PATCH MODE Splice Verification HALT condition
  (H1–H3) is triggered.
- Guessing insertion location for unmatched anchors.
- Adding new source page tags or altering existing ones during HTML compilation.
- Hiding source page tags via @media print or display:none under any condition.
- Creating sidebar TOC links whose target ids do not exist.
- Creating duplicate body ids.
- Creating body ids that are not stable or that change across repeated generations for the same heading text.

Output (PATCH MODE):
  1. Splice Verification Table
  2. (only if all markers pass) Complete HTML from <!DOCTYPE html> to </html>

Output (FULL MODE):
  Complete HTML from <!DOCTYPE html> to </html>.
```

### B5. Audit Guardrails

Regression-prevention items:

- Do not restore “peak-shift direction = model class.” Use diagnostic signal / candidate narrowing only.
- Do not state TCS is mandatory for a drug name alone. Use criteria-based adjunct strategy language.
- Do not restore unsupported `V 5–10%`, `CL 30–40%`, or other dosing-accuracy claims.
- Do not present PK35 digoxin loading/maintenance dosing as direct textbook recommendation.
- Do not restore “TDM patient 80%” or similar unsupported prevalence claims.
- Do not treat NONMEM, BestDose, ID-ODS, Pmetrics, NDA/IND/RMP wording as direct textbook source claims without the explicit `[교과서 외 구현/규제 번역]` label.
- Do not restore hemodialysis `Vu<120 AND CLu<CLuD` as a hard gate.
- Do not embed textbook figures because Image rights = None.
- Do not remove `[확인 필요]` or `[p.확인 필요]` flags.
- Do not expand Ch.6 Case A–I equations into a new full-card bank.

### B6. Crucible Guardrails

- Crucible is not a raw content source at this stage.
- Preserve only already-adopted or explicitly allowed Grade A logic.
- Do not reintroduce omitted/rejected Crucible items.
- Do not convert speculative insight into textbook-derived fact.
- Label expert interpretation as `EXPERT_INFERENCE` when it appears in Mastery Augmentation.

### B7. Deprecated and Forbidden Restorations

- Step 1 Draft v0 is deprecated.
- Do not restore rejected overclaims, unsupported numbers, unsupported regulatory claims, source-unsupported examples, unapproved code, or unapproved figures.
- Do not use Step 1 Draft v0 as learner-body source except through the Micro-Patch Gate.
- Do not add new named drugs, new equations, new external regulatory claims, or new page tags.

### B8. PATCH MODE Splice Verification Table

| Marker # | Anchor text | Anchor found? | Match count | Inserted? | Final location (§ + card) |
|---|---|---|---:|---|---|
| F01 | `**§1 recap**: 이 세션은 “모델 선택 → 질환 보정 → 개인 추정 → 처방·monitoring →` | YES | 1 | YES | §1 — Session Header & Roadmap / Capstone spine |
| F02 | `§2.1은 plot-reading grammar이고, §2.2–§2.3은 그 grammar가 실제 ODE 후` | YES | 1 | YES | §2.1 — Pattern-recognition decision workflow |
| F03 | `**Trench-Level Tip**: Case B left-shift를 “kon이 큰 약물”로 외우지 말라` | YES | 1 | YES | §2.2 — Peak-shift + saturation |
| F04 | `PK35 digoxin 사례는 CL/V/t½ 추정 사례이다. Loading dose 0.4 mg, maint` | YES | 1 | YES | §2.4 — Bayesian objective function for individual TDM |
| F05 | `**Trench-Level Tip**: phenytoin처럼 albumin-bound low-extracti` | YES | 1 | YES | §2.5 — Disease/RF/Rd framework |
| F06 | `**Trench-Level Tip**: Phenobarbital의 dialysis half-life가 크게 ` | YES | 1 | YES | §2.7 — Hemodialysis coordinate plane |
| F07 | `**Trench-Level Tip**: “신부전이므로 LD도 줄인다”는 자동 규칙은 틀릴 수 있다. LD는 ` | YES | 1 | YES | §2.9 — Loading dose vs maintenance dose |


### B9. Zero-Omission Coverage Matrix

| Domain | Required coverage | Status | Resolution in master file |
|---|---|---|---|
| C1. Scope Lock concepts | Ch.6 pattern recognition, PK35 Bayesian TDM, PK15 toxicokinetic exposure reporting, R&T Ch.15 disease/RF/Rd/dialysis, R&T Ch.18 TCS/loading/missed dosing | PASS | Present in §1, §2.1–§2.10, §8. |
| C2. Scope data anchors | PK35 digoxin case values; PK15 toxicokinetic dose/exposure/safety-margin anchors; Table 18-6 concentration interpretation inputs | PASS | Retained in §1 Data anchors, §2.4, §2.8, §2.10, §8. |
| C3. Audit MUST_FIX #1 | Peak-shift deterministic overclaim removed | PASS | §2.2 states diagnostic signal, not deterministic model rule. |
| C3. Audit MUST_FIX #2 | TCS “mandatory/all criteria” overstatement softened | PASS | §2.8 states useful adjunct when criteria are mostly met; not drug-name automatic. |
| C3. Audit MUST_FIX #3 | Unsupported LD/V/CL prediction-accuracy numbers removed | PASS | §2.9 recasts Fig.18-5 as variability partition, not accuracy promise. |
| C3. Audit MUST_FIX #4 | PK35 digoxin prescription recommendation not treated as textbook claim | PASS | §2.4 Boundary labels loading/maintenance suggestions as outside direct source. |
| C3. Audit MUST_FIX #5 | “TDM patient 80%” claim removed | PASS | §2.10 has explicit deleted-claim statement. |
| C3. Audit MUST_FIX #6–7 | NONMEM/software/regulatory wording separated from source-locked claims | PASS | §1 labels these as `[교과서 외 구현/규제 번역]`; §8 caution preserved. |
| C3. Audit MUST_FIX #8 | Hemodialysis hard AND gate removed | PASS | §2.7 uses Vu·CLu coordinate plane and continuous trade-off. |
| C4. Audit SHOULD_FIX | Fig.6.12, creatinine lag, Table 18-6, PK15 closing bridge, MUST-card compression | PASS | §2.1/F02, §2.6, §2.8, §8, and ten-card curation reflect these corrections. |
| C5. Figure coverage | Phase 4C KEEP F01–F07 exactly once; no textbook image embedding | PASS | Raw marker blocks are exact-spliced; P markers are pointer-only; R/N are schematic briefs only. |
| C6. Page-tag integrity | Preserve existing page tags and `[확인 필요]`; do not fabricate new tags | PASS | Canonical tags retained; mastery notes add no page tags. |
| C7. Crucible Grade A preservation | Adopted Grade A logic retained without speculative conversion to textbook fact | PASS | V/CL sampling identifiability, variability partition correction, and forgiveness/superposition logic retained in §2.4, §2.9, §2.10. |
| C8. Deprecated source control | Step 1 Draft v0 not restored as raw learner-body source | PASS | Step 1 used only as deprecated omission-check reference. |


### B10. Micro-Patch Log

| # | Location | Action | Rationale | Risk |
|---:|---|---|---|---|
| 1 | Content Lock v2 → v2.1 | Exact-spliced seven approved figure markers from Phase 4C PATCH MODE | Required to produce working v2.1 without rewriting canonical text | Low |
| 2 | PART A adjacent notes | Added ten bounded Mastery/Practice/Failure Mode notes | Required by Phase 4D Mastery-Uplift while preserving canonical body | Low |

No scientific micro-patch was made to canonical wording. No page tag, equation, numerical value, or source claim was altered.


### B11. Mastery Augmentation Log

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
|---|---|---|---|---|---|---|
| MA01 | §2.1 | Mastery Note | YES | TEXTBOOK_DERIVED | Adjacent bounded augmentation; no new numerical/page/source claims. | Low |
| MA02 | §2.2 | Failure Mode | YES | AUDIT_DERIVED | Adjacent bounded augmentation; no new numerical/page/source claims. | Low |
| MA03 | §2.3 | Practice Lens | YES | EXPERT_INFERENCE | Adjacent bounded augmentation; no new numerical/page/source claims. | Low |
| MA04 | §2.4 | Mastery Note | YES | CRUCIBLE_DERIVED | Adjacent bounded augmentation; no new numerical/page/source claims. | Low |
| MA05 | §2.5 | Practice Lens | YES | TEXTBOOK_DERIVED | Adjacent bounded augmentation; no new numerical/page/source claims. | Low |
| MA06 | §2.6 | Failure Mode | YES | AUDIT_DERIVED | Adjacent bounded augmentation; no new numerical/page/source claims. | Low |
| MA07 | §2.7 | Failure Mode | YES | AUDIT_DERIVED | Adjacent bounded augmentation; no new numerical/page/source claims. | Low |
| MA08 | §2.8 | Practice Lens | YES | TEXTBOOK_DERIVED | Adjacent bounded augmentation; no new numerical/page/source claims. | Low |
| MA09 | §2.9 | Mastery Note | YES | AUDIT_DERIVED | Adjacent bounded augmentation; no new numerical/page/source claims. | Low |
| MA10 | §2.10 | Practice Lens | YES | TEXTBOOK_DERIVED | Adjacent bounded augmentation; no new numerical/page/source claims. | Low |

| Rejected candidate | Reason for rejection |
|---|---|
| New drug examples outside the attached PDFs | Would violate source boundary and introduce unsupported examples. |
| New numerical decision thresholds beyond Content Lock v2 | Would risk restoring unsupported precision. |
| Broad rewrite of §2 cards | Would convert Phase 4D into Content Lock v3. |



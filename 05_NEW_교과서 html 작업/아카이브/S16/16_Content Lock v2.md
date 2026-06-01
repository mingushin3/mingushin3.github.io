# 16_Content Lock v2 — Editorial Pass Ledger

## PASS 1 — Edit log table

| Location (§ + card) | Edit type | Before (excerpt) | After (excerpt) |
|---|---|---|---|
| §1 Big Idea | R1/R2 | “데이터의 shape는… decision으로 변환한다” | 3문장으로 분리해 mechanism → deviation → decision의 인과를 명시. |
| §1 후속 구현 영역 | R2 | “이 세션에서 열리는 실무 영역이지만…” | 실무 확장과 source-locked claim의 경계를 2문장으로 분리. |
| §2.1 핵심 | R1 | “plot은 먼저… 이후 Fig.6.12식 workflow…” | plot-reading 1단계와 workflow 2단계를 분리. |
| §2.1 Trench | R3 | “dose escalation에서 shape가…” | “중요한 것은…”을 앞으로 이동해 실무 의미를 강조. |
| §2.2 핵심/정정문 | R1/R2 | “방향은… 1차 진단 신호” | deterministic rule 부정과 diagnostic signal 설명을 분리. |
| §2.3 핵심 | R1 | “모두 외우는 목록이 아니라…” | 암기 목록 부정과 pattern library 기능을 분리. |
| §2.3 turnover | R2 | “R이 생성과 소실의 동적 평형…” | response variable의 평형 상태와 drug action을 순차화. |
| §2.4 Bayesian 핵심 | R1/R2 | “observed concentrations만… population average만…” | 두 극단을 각각 부정한 뒤 posterior estimation으로 연결. |
| §2.4 sampling identifiability | R2 | “1×t½… 어렵고…” | “따라서”를 추가해 sample timing과 CL/V 식별성의 인과를 명시. |
| §2.5 Rd framework | R2 | “신장 나쁘니 줄인다…” | fe/RF 분리 후 maintenance requirement 조정이라는 작업 순서를 명시. |
| §2.5 hepatic contrast | R1 | cirrhosis 문장 | high-extraction과 low-extraction albumin-bound drug 설명을 2문장으로 분리. |
| §2.6 Cockcroft-Gault | R1/R5 | “SCr는 실시간 renal function의 거울이 아니라…” | C-G의 역할과 SCr lag를 별도 문장으로 분리. |
| §2.7 hemodialysis | R2/R3 | “half-life가 줄었는가가 아니라…” | half-life 부정과 body amount endpoint를 분리. |
| §2.8 TCS/Table 18-6 | R2/R3 | “Measured concentration을 해석하려면…” | measured concentration 단독 해석 불가성을 먼저 제시. |
| §2.9 LD/MD | R1/R2 | “loading dose는 V…” | LD와 MD가 서로 다른 parameter 문제임을 먼저 명시. |
| §2.10 erratic dosing | R1/R3 | “예외가 아니라 superposition…” | 예외 부정과 정량화 가능성을 분리. |
| §5 recap / §8 opening | R1/R2 | joint interpretation 및 meta-frame 문장 | 판단 단위와 세션 위치를 짧은 문장으로 재배열. |

## PASS 2 — Annotation candidate table

| Type | Location (§ + card) | Current text (excerpt) | Proposed annotation | Risk |
|---|---|---|---|---|
| A | §1 header | TDM | TDM(← 농도 측정으로 용량 판단을 보정하는 전략) | Low |
| A | §1 Big Idea | kinetic/dynamic mechanism | mechanism(← 농도 변화와 약효 변화의 발생 원리) | Low |
| A | §2.1 workflow | C-R plot, hysteresis | first-use glosses for C-R plot and hysteresis | Low |
| A | §2.3 pattern library | prototype | prototype(← 반복적으로 재사용되는 대표 구조) | Low |
| B | §2.4 Bayesian TDM | transition from Ch.6 to PK35 | model candidate에서 individual parameter estimation으로 넘어가는 bridge | Low |
| A | §2.4 Trench | posterior | posterior(← 관측 후 갱신된 개인 추정값) | Low |
| A | §2.5 hepatic contrast | unbound CL | unbound CL gloss | Low |
| B | §2.8 TCS | criteria discussion | 농도 측정 가능성보다 의사결정 가능성이 핵심이라는 bridge | Low |
| B | §2.9 LD/MD | dose component split | target concentration 이후 V/CL 분리 필요성 bridge | Low |
| A | §2.10 erratic dosing | superposition | superposition gloss | Low |
| C | §2.10 erratic dosing | superposition analogy | “남은 물을 더한다” analogy | Medium–High |

## PASS 2 — Final recommendation list

**Must annotate (Low risk)**: TDM, kinetic/dynamic mechanism, C-R plot, hysteresis, prototype, §2.4 bridge, posterior, unbound CL, §2.8 bridge, §2.9 bridge, superposition.

**Optional (Medium risk, high learning value)**: none selected. Type C analogy was not inserted because it risks oversimplifying exponential decay and compartmental contribution.

**Do not annotate**: source page tags, equations, numeric anchors, `[p.확인 필요]`, `[확인 필요]`, implementation/regulatory labels, and all Figure-related material reserved for Phase 4C.

**Length control**: Content Lock v1 length = 33404 characters. Content Lock v2 body length = 28396 characters after removing the completed Phase 4A adjudication table from the text-final body and adding minimal annotations. Final v2 body remains within the +8% constraint relative to v1.

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

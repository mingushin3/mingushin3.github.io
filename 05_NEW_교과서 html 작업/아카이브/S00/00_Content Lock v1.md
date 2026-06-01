# 00_Content Lock v1 — Pre-Sprint: 모델링 철학·용어

**Source**: Gabrielsson & Weiner 5e Ch.1, p.1–7 + Rowland & Tozer 5e Ch.1–2, p.3–49  
**Mode**: B-Standard  
**Image rights**: None  
**Phase**: 4A — Integration + Compression  
**Output type**: Text lock only; no HTML; no figure markers

---

# Updated Curation Map

이 세션은 두 권의 교과서가 서로 다른 질문에 답하는 진입점이다. Gabrielsson & Weiner는 **어떤 사고 순서로 모델링할 것인가**를 정하고, Rowland & Tozer는 **그 모델링 언어를 임상 용량 결정으로 어떻게 번역할 것인가**를 정한다. 후속 PopPK 세션에서 control stream, GOF, parameter interpretation, TDM 판단을 다루기 전에 반드시 잠가야 할 기반은 네 개다.

## MUST tier

| # | 개념 | Source | Lock 판정 |
|---|---|---|---|
| M1 | Modeling Carousel & 5대 dysfunction | Gabrielsson Ch.1 | 모델링은 fitting이 아니라 질문→설계→실험→EDA→fitting→진단의 순환이라는 사고 순서를 고정한다. |
| M2 | PK/PD Linkage & Therapeutic Window | Rowland & Tozer Ch.1 | dose regimen을 exposure-time profile과 response-time profile로 번역하는 임상 정량화의 출발점이다. |
| M3 | Emax / C50 / Hill γ | Rowland & Tozer Ch.2 | 농도-반응 관계를 Emax, potency, steepness로 분해하는 direct-effect PD 모델의 골격이다. |
| M4 | Turnover | Rowland & Tozer Ch.2 | response delay와 endogenous system의 dynamic equilibrium을 이해하는 indirect-response 모델의 선행 개념이다. |

## CONTEXT tier — 압축 흡수

| CONTEXT 개념 | 흡수 위치 | v1 처리 |
|---|---|---|
| constant / parameter / variable; primary vs secondary parameter | M1 | primary vs secondary parameter만 1문장으로 유지 |
| NCA vs compartmental modeling | M1 | “질문이 단순하면 NCA, 예측·비선형·PK/PD 정량화에는 모델”로 압축 |
| ADME, disposition, first-pass loss, bioavailability, enterohepatic cycling | M2 | PK phase가 exposure를 만드는 physiological chain이라는 1문장으로 압축 |
| route, dosage form, adherence, variability | M2 | therapeutic window를 흔드는 real-world input factors로 압축 |
| plasma/serum/whole blood, unbound concentration | M3 | response를 연결할 때 measurement matrix와 unbound concentration 조건으로 압축 |
| active metabolite / prodrug / stereoisomer | M3 | “측정한 농도 ≠ 활성 분자일 수 있음”으로 압축 |
| disease progression, placebo, biomarker/surrogate | M3/M4 | measured response 해석의 배경으로 압축 |

---

# Adjudication Table Summary

| Source | Item | Verdict | Rationale |
|---|---|---|---|
| Audit T1 | MUST 4개 구성 | ADOPT | Scope Lock과 PDF 핵심 구조에 부합한다. |
| Audit T1 | Modeling Carousel 6단계 | ADOPT | G Fig.1.1의 핵심 흐름이므로 유지한다. |
| Audit T1 | “EDA 누락이 가장 빈번” | PARTIAL_ADOPT | 원문은 “five most common dysfunctions”이지 순위가 아니므로 “5대 dysfunction 중 하나”로 낮춘다. |
| Audit T1 | “반드시 local minimum” | ADOPT correction | “local minimum 위험이 커진다”로 완화한다. |
| Audit T1 | “wrong FIH dose recommendation” | PARTIAL_ADOPT | PDF 직접 문장은 아니므로 삭제하고, 일반적 해석 왜곡 위험만 [실무 추론]으로 남긴다. |
| Audit T1 | G Fig.1.2 A/B/C/E 해석 | ADOPT correction | A/B/C는 possible initial estimates, D/E는 final estimates로 정정한다. |
| Audit T1 | OFV landscape | PARTIAL_ADOPT | PDF source fidelity에서는 WRSS/objective function로 표기하고 NONMEM OFV 확장은 삭제한다. |
| Audit T1 | AUC 30–50%, OFV>5, 4개 initial estimates, COV/Hessian | REJECT | PDF 범위에 없는 정량·진단 기준이므로 삭제한다. |
| Audit T1 | NCA vs model need | ADOPT | G p.4의 “model only when needed” 메시지를 M1에 보강한다. |
| Audit T1/T2 | digoxin/morphine “50배” | ADOPT correction | 원문은 digoxin once daily, morphine up to 6 times/day이므로 “투여량과 빈도가 크게 다르다”로 정정한다. |
| Audit T2/T3 | 5% hospital admissions due to inappropriate drug use | ADOPT | 왜 dosage regimen 원리가 임상적으로 중요한지 보여 주는 anchor로 1문장 반영한다. |
| Audit T2/T5 | Fig.1-1 empirical approach | PARTIAL_ADOPT | M2에서 empirical trial-and-error와 rational PK/PD approach의 대비로 1문장 반영한다. |
| Audit T2/T5 | Fig.1-5 digitalizing dose | ADOPT | loading-like rapid achievement + maintenance logic를 1문장 보강한다. |
| Audit T1/T2 | CYP2C9·VKORC1 | ADOPT correction | PDF 범위에 맞춰 CYP2C9/CYP2C19 polymorphisms와 vitamin K epoxide reductase 기전으로 정정한다. |
| Audit T2/T5 | Table 2-1 PK/PD applications | PARTIAL_ADOPT | drug design, regimen design, individualized therapy의 목적론을 M2에 1문장 반영한다. |
| Audit T1/T2 | Fig.2-1 Cmax=96 µg/L, tmax=3.0 hr | ADOPT | Cmax/tmax/AUC 정의의 concrete anchor로 반영한다. |
| Audit T5 | Fig.2-19 dose-time-response scenarios | ADOPT | Cmax/tmax/AUC 중 무엇이 중요한지는 clinical objective에 따라 달라진다는 bridge로 반영한다. |
| Audit T1 | Therapeutic window set notation | PARTIAL_ADOPT | formal set notation은 삭제하고, 해석 문장은 [해석/교육용 formalization]으로만 유지한다. |
| Audit T1 | opioid anesthetics γ very large | PARTIAL_ADOPT | source가 alfentanil γ를 추정하지 않으므로 quantal response의 steep all-or-none 양상으로 분리한다. |
| Audit T1 | Hb-O2 γ≈2.7 | REJECT | PDF 범위 외 정량값이므로 삭제한다. |
| Audit T1 | Michaelis-Menten/Langmuir structural isomorphism | REJECT | PDF 직접 근거가 없고 Pre-Sprint 범위에서 불필요하다. |
| Audit T1 | NONMEM/nlmixr2 code blocks | REJECT | PDF source fidelity output에서는 제외하고 후속 implementation 세션으로 이연한다. |
| Audit T1 | Turnover ODE | PARTIAL_ADOPT | PDF 공식은 아니므로 ODE template은 삭제하고 질적 bridge만 유지한다. |
| Audit T1 | warfarin clotting factor turnover time 외부 수치 | REJECT | PDF 범위에 없는 정량값이므로 삭제한다. |
| Audit T2 | digital medicine / industrial process | REJECT | 핵심 10분 handout 범위를 벗어나므로 생략한다. |
| Audit T6 | Figure inventory | NOT_ADJUDICATED | 사용자 지시대로 Phase 4C로 unchanged flow-through 처리한다. |
| Audit T7 | Page tag corrections | NOT_AVAILABLE | 첨부 Audit v1에 T7 표가 없으므로 신규 임의 태그는 만들지 않고, PDF/Audit에서 확인된 page만 source tag로 사용한다. |
| Crucible A1 | Carousel을 nonlinear fitting의 algorithmic 필연으로 강화 | ADOPT | G p.5–6의 EDA→initial estimate→local minimum 논리와 직접 연결된다. |
| Crucible A2 | M3 vs M4 entry rule | ADOPT | concentration peak와 effect peak의 분리 여부는 warfarin/paclitaxel 예시와 맞다. |
| Crucible A3 | γ가 titration vs threshold 인지 모드를 분기 | ADOPT | T p.40–43의 γ steepness, propranolol, alfentanil 예시에 근거한다. |
| Crucible A4 | Therapeutic Window formalization tag | ADOPT | PDF 직접 표기가 아닌 해석임을 명시한다. |
| Crucible A5 | 3개 diagnostic signature 이름만 삽입 | PARTIAL_ADOPT | 이름만 [실무 추론]으로 남기고 threshold/detection criteria는 삭제한다. |
| Crucible A6 | Trench tips 1/2/4 | PARTIAL_ADOPT | PDF-grounded logic만 유지하고 RSE/condition number 등 외부 threshold는 삭제한다. |
| Crucible A7 | D1–D13 deletion candidates | ADOPT | Audit MUST_FIX와 compression rule에 부합한다. |
| Crucible B1 | conserved turnover parameter | ADOPT | T p.45–46의 water vs cholesterol/WBC 예시와 연결 가능하다. |
| Crucible B2 | 30-Second Diagnostic Grid | ADOPT | §2 Recap에 1개 compressed grid로 반영한다. |
| Crucible B3/B4/B5 | expert intuitions α/β/γ | PARTIAL_ADOPT | 각각 1문장만 유지하고 실무 확장은 줄인다. |
| Crucible B6 | Critical Blow를 Graded vs Quantal에 추가 | ADOPT | §5 Pair 2에 반영하되 [교육용 가상 시나리오]로 표시한다. |
| Crucible B7/B8 | adherence artifact, KIN/KOUT, unbound concentration 단정 완화 | PARTIAL_ADOPT | ungrounded threshold는 제거하고 qualitative warning만 남긴다. |
| Crucible C1–C5 | CWRES fan-shape, $COV threshold, workflow 상세, detection threshold, 긴 dialogic scenario | REJECT | 후속 GOF/NONMEM/regulatory 세션 범위이며 PDF 범위 밖이다. |

---

# §1 — Session Header & Roadmap

**Session title**: Pre-Sprint — 모델링 철학·용어  
**Core question**: 모델링은 왜, 언제, 어떤 순서로 해야 하며, 그 결과를 어떻게 임상 용량 결정 언어로 번역할 것인가?

<!-- MASTER LENS -->
**Big Idea**: 모델링은 수식 fitting이 아니라 **임상 질문 → 설계 → 실험 → EDA → fitting → 진단**의 순환 사고이며, PK/PD는 그 순환 안에서 **dose regimen을 exposure-time profile과 response-time profile로 번역하는 언어**다.
<!-- /MASTER LENS -->

## Roadmap

```text
M1. Modeling Carousel
    ├─ 왜 fitting부터 시작하면 안 되는가
    ├─ EDA가 initial estimate와 model structure를 만든다
    └─ 5대 dysfunction: EDA 경시, formula slavery, software overtrust,
       improper weighting, lack of holistic view

M2. PK/PD Linkage & Therapeutic Window
    ├─ dose regimen → exposure → desired/adverse effects
    ├─ empirical regimen design vs rational PK/PD approach
    └─ therapeutic window: efficacy와 harm 사이의 operating range

M3. Emax / C50 / Hill γ
    ├─ Emax: maximum response
    ├─ C50: potency
    └─ γ: steepness; titration-friendly vs threshold-like response

M4. Turnover
    ├─ steady state는 static state가 아니라 dynamic equilibrium
    ├─ Rt, Ass, kt, tt
    └─ concentration peak와 effect peak가 분리될 때 indirect response를 의심한다
```

**후속 개방**: M1은 GOF와 model selection, M2는 compartmental PK와 TDM, M3는 direct-effect PD, M4는 indirect-response/disease progression/TMDD downstream 모델로 이어진다.

---

# §2 — Concept Anatomy Cards

---

## Card M1 ⚡ Apex Concept — Modeling Carousel & 5대 Dysfunction [G pp.1–7]

<!-- MASTER LENS -->
### [개념 Big Idea: 거장의 시각]

**왜 결정적인가**: nonlinear model fitting은 parameter initial estimate를 요구한다. EDA 없이 fitting을 시작하면 model structure와 initial estimate가 데이터에서 오지 않고 사용자의 추측이나 software default에서 오게 되며, 이때 local minimum에 수렴할 위험이 커진다. 핵심은 “fitting이 시작점이 아니다”라는 것이다.

**체화해야 할 단 하나의 직관**: Modeling Carousel에서 fitting은 6단계 중 5번째다. 앞의 네 단계 — tentative model, design, experiment, EDA — 가 fitting의 해석 가능성을 만든다.
<!-- /MASTER LENS -->

### A. Formal Definition

**Modeling Carousel**은 성공적 모델링을 위한 순환 workflow다 [G p.4].

1. **Tentative model** — 실험 전 사전 가설과 tentative system model.
2. **Design** — dose, sampling time, response measurement, population, simulation/CATD.
3. **Run experiment** — 데이터 수집.
4. **Explore data (EDA)** — concentration-time, response-time, response-concentration plot으로 구조와 비선형성을 탐색.
5. **Fit model(s)** — 보통 nonlinear regression으로 parameter와 precision을 추정.
6. **Analyze output & model discrimination** — GOF, residual, parameter precision, validation, competing model 비교.

G Ch.1의 simple model은 dose $D$를 constant, $V$와 $Cl$을 primary parameter, $\hat C$와 $t$를 variable로 둔다. $K=Cl/V$, $AUC=D/Cl$, $t_{1/2}=\ln(2)/K$는 primary parameter에서 도출되는 secondary parameter다 [G pp.1–2].

**Equation block — one-compartment prediction / observation error [G pp.1–2]**

$$
\hat C = \frac{D}{V}\exp\left(-\frac{Cl}{V}t\right)
$$

$$
C = \hat C + \varepsilon
$$

### B. Why Model at All?

G Ch.1의 핵심은 “모델링을 많이 하라”가 아니라 **필요할 때만 하라**다. Bioavailability나 total clearance 같은 exposure summary가 질문이면 NCA가 충분할 수 있고, single-dose에서 multiple-dose를 예측하거나 nonlinear kinetics를 다루거나 PK/PD 관계를 정량화해야 할 때 compartmental/PBPK-type model이 필요하다 [G p.4].

<!-- ANCHOR -->
즉, 모델은 지식 과시가 아니라 질문에 맞는 압축 장치다. “가장 복잡한 모델”이 아니라 “질문을 답하는 데 필요한 만큼만 복잡한 모델”이 원칙이다 [G pp.3–4].
<!-- /ANCHOR -->

### C. Structural Necessity

Step 4 EDA는 예쁜 그림을 만드는 단계가 아니라 Step 5 fitting의 입력을 생산하는 단계다. G p.5–6은 EDA가 model structure와 initial estimates를 제안해야 하며, nonlinear fitting algorithm은 initial estimate를 필요로 한다고 설명한다.

G Fig.1.2는 clearance와 volume의 parameter space에서 objective function WRSS가 여러 hollow를 가질 수 있음을 보여 준다. Yellow point는 possible initial estimate이고 red point는 final estimate다. Poor starting value는 local minimum으로, good initial estimate는 global minimum으로 수렴할 수 있다 [G p.6].

<!-- TRENCH -->
**Trench-level tip [실무 추론]**: EDA의 산출물은 plot 자체가 아니라 “initial estimate 후보 1표 + nonlinearity yes/no 1줄”이다. Dose-normalized plot이 nonlinearity를 시사하면, 결론 전에 dataset의 dose/time/event coding 오류 가능성부터 배제한다.
<!-- /TRENCH -->

### D. Assumptions & Boundary Conditions

Modeling Carousel은 rich dataset과 실험 설계를 전제로 한 사고 순서다. Sparse data나 real-world data에서는 EDA의 해상도가 떨어질 수 있으므로, “모델이 설명한다”와 “데이터가 구분해 준다”를 구분해야 한다.

**Five common dysfunctions** [G p.4]

| Dysfunction | 압축 해석 |
|---|---|
| failure to appreciate EDA before fitting | fitting부터 돌리면 model structure와 initial estimate가 빈약해진다. |
| slavery to formulas | 수식을 외워도 biology와 data가 요구하는 구조를 보지 못한다. |
| too much trust in software | 수렴 메시지는 과학적 타당성 보증서가 아니다. |
| improper use of weighting | residual/error model을 잘못 두면 structural 판단도 흐려진다. |
| lack of holistic view | design, assay, biology, response timing을 함께 보지 못한다. |

### E. Limitations

이 장은 NONMEM convergence diagnostics나 covariance step 해석을 가르치는 장이 아니다. 따라서 “몇 개 initial estimate를 써야 하는가”, “OFV 차이가 얼마면 충분한가” 같은 운영 기준은 이 Content Lock에서 제외한다. 원문 수준에서 잠글 메시지는 **different initial estimates로 rerun하여 local minimum 여부를 확인하라**는 원칙이다 [G p.6].

### F. Cognitive Lock

- **Formal**: model은 response variable이 predictor에 어떻게 의존하는지 표현한다.
- **Graphical**: concentration-time, response-time, response-concentration plot이 구조를 먼저 말한다.
- **Algorithmic**: nonlinear fitting은 initial estimate와 objective surface의 basin에 민감하다.
- **Biological**: model은 biology와 collected data가 drive해야 한다.
- **Practical**: fitting 전에 “질문, design, EDA, initial estimate”가 문서화되어야 한다.

**Diagnostic signature [실무 추론]**: **Premature Convergence Mirage** — EDA 없이 fitting부터 시작해 수렴은 했지만, model structure와 initial estimate의 근거가 빈약한 상태.

### G. Zettelkasten Atom

```yaml
aliases: [Modeling Carousel, EDA-first modeling, local minimum]
tags: [pharmacometrics/modeling, EDA, model-selection]
source: Gabrielsson & Weiner 5e Ch.1 pp.1-7
lock: Fitting is Step 5, not Step 1. EDA produces model structure and initial estimates.
```

<!-- RECAP -->
**M1 Recap**: 모델링의 첫 원칙은 software 실행이 아니라 질문과 데이터 구조를 먼저 보는 것이다. EDA를 건너뛴 fitting은 수렴할 수는 있어도, 왜 그 model이어야 하는지 설명하지 못한다.
<!-- /RECAP -->

---

## Card M2 — PK/PD Linkage & Therapeutic Window [T pp.3–17]

<!-- MASTER LENS -->
### [개념 Big Idea: 거장의 시각]

**왜 결정적인가**: 임상 처방 질문은 “얼마나, 얼마나 자주, 얼마나 오래, 어떤 route와 dosage form으로 줄 것인가”다. 이 질문은 dose 자체가 아니라 dose가 만든 exposure-time profile, 그리고 그 exposure가 만든 desired/adverse response-time profile로 답해야 한다 [T p.3].

**체화해야 할 단 하나의 직관**: PK와 PD는 두 개의 독립 과목이 아니라 하나의 causal chain이다. **Dosage regimen → exposure within body → desired/adverse effects**가 연결되어야 regimen을 바꿀 근거가 생긴다.
<!-- /MASTER LENS -->

### A. Formal Definition

**Pharmacokinetics**: dose, dosage form, dosing frequency, route 같은 input이 시간에 따른 concentration/exposure를 어떻게 만드는가.  
**Pharmacodynamics**: concentration이 desired effect와 adverse effect를 시간에 따라 어떻게 만드는가 [T pp.4–5].

T Fig.1-3의 핵심은 conc-vs-time과 conc-vs-effect가 결합되어 effect-vs-time을 만든다는 점이다. PK만 있으면 “몸 안 농도”만 알 수 있고, PD만 있으면 “농도에서 반응”만 알 수 있다. 치료에는 둘의 link가 필요하다 [T p.5].

**PK phase context**: ADME, disposition, first-pass loss, bioavailability, enterohepatic cycling은 dose가 systemic exposure로 바뀌는 physiological chain의 component다 [T pp.26–33].

### B. Therapeutic Window

Therapeutic window는 too low exposure에서 ineffective therapy가, too high exposure에서 adverse effects가 증가한다는 전제 위에 놓인 operating range다 [T p.6].

<!-- ANCHOR -->
[해석/교육용 formalization] 실무적으로는 therapeutic window를 “therapeutic response probability가 충분하고 adverse-event probability가 지나치지 않은 exposure range”로 읽으면 된다. 단, 이 확률 집합 표기는 원문 수식이 아니라 교육용 formalization이다.
<!-- /ANCHOR -->

### C. Structural Necessity

T Ch.1은 empirical trial-and-error regimen design을 rational PK/PD approach와 대비한다. 예전에는 dose와 interval을 조정하며 desired/adverse effects를 관찰해 regimen을 개선했지만, 이 방식만으로는 digoxin과 morphine regimen 차이의 원리를 설명하지 못한다 [T p.4].

Digoxin은 0.125–0.25 mg once daily로 쓰이는 반면, morphine sulfate는 10–50 mg을 하루 최대 6회까지 투여할 수 있다. 두 약물 모두 therapeutic window가 비교적 좁지만, morphine은 빠르게 제거되어 자주 투여가 필요하고, digoxin은 천천히 제거되어 once-daily가 가능하다 [T pp.4, 7].

**Key example — digoxin accumulation/digitalizing dose [T p.7]**  
Digoxin을 낮은 daily dose로 주면 처음에는 ineffective할 수 있고, 높은 rate로 유지하면 나중에 toxic해질 수 있다. 그래서 초기에는 여러 small dose로 빠르게 therapeutic concentration에 도달시키고 이후 small daily dose로 유지하는 digitalizing dose 논리가 나온다.

### D. Why It Matters Clinically

Rowland & Tozer는 inappropriate drug use 때문에 병원 입원 환자의 약 5%가 입원한다는 예를 든다 [T p.4]. 이 숫자의 메시지는 약동학 지식의 장식성이 아니라 **regimen design의 안전성**이다.

PK/PD는 drug design, drug selection, dosage regimen design, protocol design, data interpretation, drug product performance 평가, individualized therapy initiation에도 쓰인다 [T p.20].

### E. Limitations & Real-World Distortions

- **Measured site problem**: site of action 농도는 대개 직접 측정하기 어렵고 plasma가 대리 site로 쓰인다 [T p.6].
- **Adherence problem**: prescribed regimen이 실제 exposure로 그대로 이어지지 않는다. Once-daily antihypertensive cohort에서 1년 말 처방약을 지속한 비율은 약 50%였다 [T p.12].
- **Variability problem**: phenytoin concentration variability, warfarin S-warfarin variability, G6PD/primaquine, debrisoquine/CYP2D6, terfenadine/ketoconazole 예시는 같은 regimen이 같은 exposure/response를 보장하지 않음을 보여 준다 [T pp.10–12].
- **Warfarin genetics correction**: 이 PDF 범위에서는 CYP2C9/CYP2C19 polymorphisms와 vitamin K epoxide reductase 기전이 언급된다. VKORC1 label은 이 범위의 원문 표현이 아니므로 사용하지 않는다 [T p.10].

<!-- TRENCH -->
**Trench-level tip [실무 추론]**: adherence monitoring이 약하면 apparent PK variability가 실제 missed dose의 artifact일 수 있다. 이때 model은 환자 생리 차이가 아니라 input history 오류를 variability로 흡수할 수 있다.
<!-- /TRENCH -->

### F. Zettelkasten Atom

```yaml
aliases: [PK/PD linkage, therapeutic window, input-response phases]
tags: [clinical-pharmacology/dosing, pharmacometrics/pkpd]
source: Rowland & Tozer 5e Ch.1 pp.3-17; Table 2-1 p.20
lock: Dose regimen is useful only after it is translated into exposure-time and response-time profiles.
```

<!-- RECAP -->
**M2 Recap**: PK/PD linkage의 핵심은 “dose가 아니라 concentration at the site of action이 response를 drive한다”는 점이다. Therapeutic window는 이 linkage가 임상적으로 작동해야 하는 안전 범위다.
<!-- /RECAP -->

---

## Card M3 — Emax / C50 / Hill γ [T pp.35–43]

<!-- MASTER LENS -->
### [개념 Big Idea: 거장의 시각]

**왜 결정적인가**: 농도-반응 관계를 말할 때 “효과가 증가한다”만으로는 부족하다. Emax는 ceiling, C50은 potency, γ는 curve steepness를 분리해 준다. 이 세 가지를 분리하지 못하면 dose titration, endpoint selection, safety margin 해석이 흐려진다.

**체화해야 할 단 하나의 직관**: C50이 낮다고 항상 좋은 약이 아니다. 같은 potency라도 Emax가 낮으면 충분한 clinical response에 도달하지 못할 수 있고, γ가 너무 크면 작은 농도 변화가 response threshold를 급격히 넘게 만든다 [T pp.40–43].
<!-- /MASTER LENS -->

### A. Formal Definition

**Graded response**는 concentration이 변할 때 response intensity가 연속적으로 변하는 반응이다. Ketamine 예시에서 S(+)-ketamine은 R(−)-ketamine보다 더 낮은 C50와 더 높은 maximum response를 보인다: S(+) C50 ≈ 0.7 mg/L, R(−) C50 ≈ 1.8 mg/L [T p.40].

**Equation block — Hill/Emax equation [T p.40]**

$$
E = \frac{E_{\max}\,C^{\gamma}}{C_{50}^{\gamma}+C^{\gamma}}
$$

- $E_{\max}$: maximum response.
- $C_{50}$: 50% of $E_{\max}$를 만드는 concentration.
- $\gamma$: steepness factor.

**Exposure-time anchor [T pp.21–22]**: single oral dose profile에서 $C_{\max}$는 maximum systemic exposure, $t_{\max}$는 그 시간, AUC는 total systemic exposure다. Fig.2-1의 예시는 $C_{\max}=96\,\mu g/L$, $t_{\max}=3.0$ hr이다.

### B. What γ Really Changes

T p.40은 $\gamma=1$이면 20%→80% response에 필요한 concentration 범위가 $0.25C_{50}$에서 $4C_{50}$, 즉 16-fold라고 설명한다. $\gamma=2$이면 $0.5C_{50}$에서 $2C_{50}$, 즉 4-fold로 압축된다.

$$
\gamma=1: C_{20}=0.25C_{50},\; C_{80}=4C_{50}
$$

$$
\gamma=2: C_{20}=0.5C_{50},\; C_{80}=2C_{50}
$$

일반적으로 $\gamma$는 1–3 사이에 있지만, 매우 크면 minimal response와 maximal response 사이의 concentration range가 좁아져 all-or-none response처럼 보일 수 있다 [T pp.40–41].

<!-- ANCHOR -->
$\gamma$는 단순한 곡선 모양이 아니라 처방 사고를 바꾼다. $\gamma \approx 1$이면 symptom-based titration이 상대적으로 자연스럽고, steep/threshold-like response이면 작은 concentration shift가 clinical event를 바꿀 수 있다.
<!-- /ANCHOR -->

### C. Real Data Anchors

**Key example — propranolol [T p.42]**  
Exercise-induced tachycardia 감소율과 unbound propranolol concentration의 관계는 Hill equation에 잘 맞고, $\gamma \approx 1$, $E_{\max}\approx 40\%$, $C_{50}=5.3\,\mu g/L$로 제시된다.

**Key example — alfentanil quantal response [T pp.42–43]**  
Alfentanil은 nitrous oxide anesthesia 중 satisfactory response의 cumulative frequency로 평가된다. C50는 breast 0.27 mg/L, lower abdomen 0.31 mg/L, upper abdomen 0.42 mg/L 순으로 증가한다. 이 예시는 γ를 추정한 graded curve가 아니라, quantal endpoint에서 response probability가 concentration과 어떻게 연결되는지 보여 준다.

### D. Measurement & Assay Boundaries

Total plasma/serum concentration에는 bound와 unbound drug가 모두 포함되지만, distribution, elimination, PD response는 unbound concentration에 의존한다. 다만 fraction unbound가 일정하면 total concentration으로도 충분할 수 있고, saturable binding, displacement interaction, renal/hepatic disease, surgery, severe burns, pregnancy 등 binding이 변하는 조건에서는 unbound concentration 측정이 중요해진다 [T p.21].

**Chemical entity boundary**: racemate, stereoisomer, active metabolite, prodrug에서는 “측정한 total parent concentration”이 실제 active moiety를 대표하지 못할 수 있다. Acenocoumarol, methylphenidate, aspirin/salicylic acid 예시는 assay specificity가 PK/PD link를 좌우한다 [T pp.23–25].

<!-- TRENCH -->
**Trench-level tip [실무 추론]**: dose range가 C50 주변에만 몰려 있고 plateau 정보가 없으면 γ를 자유롭게 estimate하기보다 parsimonious assumption을 먼저 검토한다. “γ를 estimate했다”는 사실보다 “데이터가 γ를 식별할 수 있는가”가 먼저다.
<!-- /TRENCH -->

### E. Limitations

Clinical $E_{\max}$는 pharmacological maximum보다 낮을 수 있다. 예를 들어 heart rate를 올리는 약물에서는 cardiovascular system이 먼저 악화되어 pharmacological maximum에 도달하기 전에 안전성 한계가 올 수 있다. 따라서 agonist의 $E_{\max}$는 antagonist보다 임상적으로 정의하기 어렵다 [T p.41].

Fig.2-19의 메시지는 exposure metric 선택에도 적용된다. Chronic therapy에서는 duration above a minimum concentration이 중요할 수 있고, headache relief처럼 빠른 효과가 목적이면 $C_{\max}$와 $t_{\max}$가 더 중요할 수 있으며, 어떤 경우에는 total AUC가 더 관련 있을 수 있다 [T p.44].

### F. Diagnostic Lock

- **Graded response**: concentration 변화가 response intensity의 연속 변화로 이어진다.
- **Quantal response**: individual-level endpoint는 all-or-none이며, population-level cumulative frequency로 concentration-response를 본다.
- **Endpoint trap**: pharmacologic response는 graded인데 clinical endpoint가 threshold로 절단되어 quantal처럼 분석될 수 있다 [T p.43].
- **Diagnostic signature [실무 추론]**: **Hill γ Identifiability Collapse** — data range가 plateau와 low-response region을 충분히 포함하지 못해 γ 추정이 model보다 noise를 따라가는 상태.

### G. Zettelkasten Atom

```yaml
aliases: [Emax, C50, Hill equation, graded response, quantal response]
tags: [pharmacometrics/pd, exposure-response]
source: Rowland & Tozer 5e Ch.2 pp.35-43
lock: Emax is ceiling, C50 is potency, gamma is steepness; endpoint type decides how response should be modeled.
```

<!-- RECAP -->
**M3 Recap**: Hill equation은 농도-반응의 “현재 순간”을 정량화한다. 하지만 measured concentration, active moiety, endpoint type, γ 식별 가능성을 함께 보지 않으면 정확한 수식도 잘못된 dose 해석으로 이어진다.
<!-- /RECAP -->

---

## Card M4 — Turnover: Pool Size · Rate · Fractional Rate · Time [T pp.44–46]

<!-- MASTER LENS -->
### [개념 Big Idea: 거장의 시각]

**왜 결정적인가**: 어떤 response는 drug concentration이 peak를 찍은 뒤 훨씬 늦게 나타난다. 이 지연이 단순 distribution delay인지, endogenous system의 turnover 때문인지를 구분하지 못하면 direct-effect Hill model로 설명할 수 없는 시간을 억지로 fitting하게 된다.

**체화해야 할 단 하나의 직관**: steady state는 움직이지 않는 상태가 아니라 **input rate와 output rate가 같아 pool size가 일정한 dynamic equilibrium**이다 [T p.45]. 약물이 input을 바꾸는지 output을 바꾸는지에 따라 response time course가 달라진다.
<!-- /MASTER LENS -->

### A. Formal Definition

Turnover는 endogenous substance/system이 steady state에 있으면서 계속 renewal되고 elimination되는 현상이다. Oral anticoagulants, antihyperlipidemics, uricosuric agents, epoetin alfa는 모두 endogenous compound/system의 formation 또는 elimination을 바꿔 delayed response를 만들 수 있다 [T p.45].

**Equation block — turnover relationships [T p.45]**

$$
k_t = \frac{R_t}{A_{ss}}
$$

$$
t_t = \frac{A_{ss}}{R_t}
$$

$$
t_t = \frac{1}{k_t}
$$

- $A_{ss}$: pool size at steady state.
- $R_t$: turnover rate.
- $k_t$: fractional turnover rate.
- $t_t$: turnover time.

### B. Key Examples

**Key example — warfarin [T p.8]**  
Warfarin sodium 1.5 mg/kg single oral dose를 5명의 male volunteers에게 투여했을 때, plasma warfarin concentration은 빠르게 올라가지만 prothrombin complex activity response는 느리게 변한다. 이 분리는 concentration-time profile만으로 response-time profile을 설명할 수 없음을 보여 준다.

**Key example — paclitaxel [T pp.8–9]**  
Paclitaxel은 body에서 약 2일 내 제거되지만 leukocyte count 변화는 매우 느리며, nadir는 1주 이후에 나타나고 baseline 회복은 약 3주가 걸릴 수 있다. 이것이 turnover-driven response의 전형적 시그니처다.

**Key example — total body water [T pp.45–46]**  
Total body water는 약 42 L이고, 평균 turnover rate는 2.5 L/day, fractional turnover rate는 0.06 day⁻¹, turnover time은 17 days다. Desert-like condition에서는 pool size가 거의 일정해도 turnover rate가 21 L/day까지 증가할 수 있고, 이때 fractional turnover rate는 0.5 day⁻¹, turnover time은 2 days가 된다.

### C. Structural Necessity

M3는 concentration과 response의 즉시적 또는 quasi-steady relationship을 다루지만, M4는 measured response가 endogenous pool의 변화를 반영할 때 필요하다. Entry rule은 단순하다: **effect peak time이 concentration peak time과 분리되어 있으면 direct-effect Hill만으로 충분한지 의심한다**.

<!-- ANCHOR -->
Turnover modeling에서 더 중요한 질문은 “Rt, kt, tt 중 무엇을 외웠는가”가 아니라 “이 system에서는 pool size가 보존되는가, fractional turnover가 보존되는가, 아니면 turnover rate 자체가 바뀌는가”다. Water 예시는 pool size가 feedback으로 유지될 수 있음을, cholesterol/WBC 예시는 pool size 자체가 변할 수 있음을 보여 준다 [T p.46].
<!-- /ANCHOR -->

### D. Boundaries

이 장은 indirect response ODE coding을 제공하지 않는다. 원문에서 잠글 것은 equation template이 아니라 turnover parameter 간 관계와 delayed response의 원인이다. ODE, KIN/KOUT, baseline parameterization은 후속 PD modeling 세션으로 이연한다.

<!-- TRENCH -->
**Trench-level tip [실무 추론]**: sparse response-time data에서 input과 output을 동시에 자유롭게 추정하면 parameter가 서로 보상할 수 있다. 먼저 baseline, peak timing, recovery timing을 보고 어떤 turnover component가 데이터로 식별 가능한지 판단한다.
<!-- /TRENCH -->

### E. Diagnostic Lock

- **Turnover rate**가 크다고 process가 빠른 것은 아니다. pool size가 크면 fractional turnover는 느릴 수 있다.
- **Fractional turnover rate**와 **turnover time**이 process speed를 더 직접적으로 말한다.
- **Diagnostic signature [실무 추론]**: **Turnover-PD Mis-attribution** — delayed response를 PK distribution delay나 Hill γ 문제로만 설명하려는 상태.

### F. Zettelkasten Atom

```yaml
aliases: [Turnover, pool size, fractional turnover rate, turnover time]
tags: [pharmacometrics/indirect-response, physiology/dynamic-equilibrium]
source: Rowland & Tozer 5e Ch.2 pp.44-46
lock: Steady state is dynamic equilibrium; delayed response often means the measured system is turning over.
```

<!-- RECAP -->
**M4 Recap**: Turnover는 “반응이 늦다”를 수학적으로 다루기 전, 무엇이 천천히 바뀌고 있는지 묻는 생리학적 언어다. Concentration peak와 effect peak가 분리되면 M4 사고가 켜져야 한다.
<!-- /RECAP -->

---

## §2 Recap — 30-Second Diagnostic Grid

<!-- RECAP -->
새 PK/PD dataset을 처음 받은 30초에는 네 개 lens가 동시에 켜져야 한다.

| Lens | 먼저 볼 것 | 즉시 판단할 것 |
|---|---|---|
| M1 | dose levels, sampling density, concentration-time plot | EDA가 model structure와 initial estimate를 줄 수 있는가? |
| M2 | regimen, route, adherence, measurement site | dose→exposure→response chain에서 빠진 link가 있는가? |
| M3 | plateau, C50 주변 coverage, endpoint type | Emax/C50/γ를 식별할 수 있는가, endpoint가 graded인가 quantal인가? |
| M4 | concentration peak vs effect peak timing | direct-effect model로 충분한가, turnover/delay 구조가 필요한가? |

이 grid의 목적은 control stream을 바로 쓰는 것이 아니라, 어떤 모델을 쓸 권리가 데이터에 있는지 먼저 묻는 것이다.
<!-- /RECAP -->

---

# §5 — Confusion Pair Dissection

## Pair 1 — Pharmacokinetics vs Pharmacodynamics

<!-- CONFUSION -->
| 구분 | Pharmacokinetics | Pharmacodynamics |
|---|---|---|
| 질문 | body가 drug에 무엇을 하는가? | drug가 body에 무엇을 하는가? |
| 축 | input → concentration-time | concentration → effect-time |
| 데이터 | plasma/serum/whole blood concentration, AUC, Cmax, tmax | desired/adverse response, biomarker, clinical endpoint |
| 실패 모드 | exposure를 dose와 동일시 | response를 concentration 없이 직접 dose와 연결 |

**Lock**: PK와 PD는 반대말이 아니다. 치료적으로 유용한 것은 둘의 link다 [T p.5].
<!-- /CONFUSION -->

## Pair 2 ⚡ Critical Blow Applied — Graded Response vs Quantal Response

<!-- CONFUSION -->
| 구분 | Graded response | Quantal response |
|---|---|---|
| response 형태 | intensity가 연속적으로 변함 | individual endpoint가 all-or-none |
| 모델 감각 | Hill/Emax로 continuous response를 설명 | cumulative frequency/probability로 event를 설명 |
| 예시 | ketamine response, propranolol heart-rate reduction | alfentanil satisfactory anesthesia response |
| C50 의미 | 50% of Emax를 주는 concentration | population 50%에서 predetermined response가 나타나는 concentration |

**Critical Blow [교육용 가상 시나리오]**: Protocol의 primary endpoint가 “24시간 내 ≥50% pain reduction: Y/N” 같은 quantal endpoint인데, modeler가 continuous VAS score를 graded Hill model로만 분석하면, statistician의 binary endpoint 분석과 modeler의 exposure-response 분석이 서로 다른 dose를 지지할 수 있다. 문제는 Hill equation 자체가 아니라 **endpoint scale과 modeling framework의 불일치**다.
<!-- /CONFUSION -->

## Pair 3 — Turnover Rate vs Fractional Turnover Rate

<!-- CONFUSION -->
| 구분 | Turnover rate $R_t$ | Fractional turnover rate $k_t$ |
|---|---|---|
| 정의 | 단위 시간당 input/output amount | pool size 대비 fractional replacement speed |
| 단위 | amount/time | time⁻¹ |
| 직관 | 얼마나 많이 바뀌는가 | 얼마나 빠르게 바뀌는가 |
| water 예시 | 2.5 L/day는 커 보임 | 0.06 day⁻¹, turnover time 17 days는 느린 process임을 보여 줌 |

**Lock**: $R_t$만 보면 큰 pool의 느린 turnover를 빠른 process로 오해할 수 있다. Speed는 $k_t$와 $t_t$가 더 잘 말한다 [T pp.45–46].
<!-- /CONFUSION -->

---

# §7 — Self-Test: Active Recall Module

<!-- SELF-TEST -->
## Q1. Modeling Carousel에서 fitting은 몇 번째 단계이며, 왜 그 앞 단계가 중요한가?

**Expected answer**: fitting은 Step 5다. Step 4 EDA가 model structure와 initial estimate를 제안하고, nonlinear fitting algorithm은 initial estimate에 민감하기 때문이다 [G pp.5–6].

## Q2. NCA가 충분한 질문과 compartmental model이 필요한 질문을 하나씩 들어라.

**Expected answer**: bioavailability 또는 total clearance summary가 목적이면 NCA가 충분할 수 있다. single-dose data로 multiple-dose 결과를 예측하거나 nonlinear kinetics 또는 PK/PD 관계를 정량화하려면 model이 필요하다 [G p.4].

## Q3. Therapeutic window를 dose가 아니라 exposure 관점에서 설명하라.

**Expected answer**: 너무 낮은 exposure는 ineffective therapy로, 너무 높은 exposure는 adverse effects 증가로 이어지며, 둘 사이에서 therapeutic response를 얻고 undue adverse effect를 피하는 exposure range가 therapeutic window다 [T p.6].

## Q4. Digoxin과 morphine regimen 차이를 “dose frequency 차이”가 아니라 PK/PD 원리로 설명하라.

**Expected answer**: 두 약물 모두 narrow window를 가질 수 있지만 morphine은 빠르게 제거되어 자주 투여가 필요하고, digoxin은 천천히 제거되어 once-daily가 가능하다. Digoxin은 빠른 도달과 유지가 분리되어 digitalizing dose + maintenance dose 논리가 나온다 [T pp.4, 7].

## Q5. $\gamma=1$과 $\gamma=2$에서 20–80% response concentration range는 어떻게 다른가?

**Expected answer**: $\gamma=1$이면 $0.25C_{50}$에서 $4C_{50}$까지 16-fold, $\gamma=2$이면 $0.5C_{50}$에서 $2C_{50}$까지 4-fold다 [T p.40].

## Q6. Propranolol과 alfentanil 예시가 각각 가르치는 것은 무엇인가?

**Expected answer**: Propranolol은 unbound concentration과 graded response가 Hill equation으로 설명되는 예시이며 $\gamma\approx1$, $E_{\max}\approx40\%$, $C_{50}=5.3\,\mu g/L$다. Alfentanil은 quantal response에서 C50가 population event probability의 기준이 됨을 보여 준다 [T pp.42–43].

## Q7. Concentration peak와 effect peak가 분리되어 있을 때, 어떤 사고가 켜져야 하는가?

**Expected answer**: direct-effect Hill만으로 충분한지 의심하고 turnover/delay 구조를 고려해야 한다. Warfarin과 paclitaxel은 concentration-time과 response-time이 분리되는 예시다 [T pp.8–9].

## Q8. $R_t=2.5$ L/day인 total body water turnover가 왜 “빠른 process”라고 단정할 수 없는가?

**Expected answer**: pool size가 42 L이므로 fractional turnover rate는 0.06 day⁻¹이고 turnover time은 17 days다. Amount/time이 커도 pool 대비 fraction이 작으면 process는 느리다 [T pp.45–46].

## Q9. Fig.2-19의 두 scenario가 exposure metric 선택에 주는 메시지는 무엇인가?

**Expected answer**: 같은 Cmax/tmax라도 decline 속도가 다르면 AUC와 duration이 달라질 수 있고, 같은 AUC라도 input 속도가 다르면 Cmax와 tmax가 달라진다. 어떤 metric이 중요한지는 clinical objective와 exposure-response relationship에 따라 달라진다 [T p.44].
<!-- /SELF-TEST -->

---

# §8 — Meta-Frame & Big Picture

## A. Positioning

<!-- MASTER LENS -->
이 세션의 목표는 “PK/PD 용어 암기”가 아니라 **후속 모델링 판단의 언어를 잠그는 것**이다. M1이 사고 순서를 정하고, M2가 임상 목적 함수를 정하며, M3가 농도-반응 형태를 정하고, M4가 시간 지연과 endogenous system을 해석한다.
<!-- /MASTER LENS -->

## B. Dependencies

- M1 없이 후속 GOF/diagnostic 세션으로 가면, software output을 model validity로 오해한다.
- M2 없이 compartmental PK로 가면, concentration-time curve를 임상 response와 분리해서 보게 된다.
- M3 없이 PD modeling으로 가면, potency, ceiling, steepness, endpoint type을 한 덩어리로 오해한다.
- M4 없이 indirect response로 가면, delayed response를 단순 distribution delay나 poor fit으로만 오해한다.

## C. Professional Lock

<!-- RECAP -->
**한 문장 lock**: 좋은 pharmacometrician은 데이터를 받자마자 fitting하지 않는다. 먼저 질문을 정하고, exposure가 어떻게 만들어졌는지 보고, response가 어떤 scale과 timing으로 측정됐는지 확인한 뒤, 그 데이터가 어떤 model complexity를 허락하는지 판단한다.
<!-- /RECAP -->

## D. Compression Compliance Note

Content Lock v1은 Step 1 Draft v0보다 짧게 재작성되었고, 다음 항목은 삭제 또는 압축되었다.

| 삭제/압축 항목 | 처리 |
|---|---|
| local minimum·regulatory overclaim | 위험 수준으로 완화; unsupported 정량 삭제 |
| AUC 30–50%, OFV>5, 4 initial estimates, COV/Hessian | 삭제 |
| CYP2C9·VKORC1 | CYP2C9/CYP2C19 + vitamin K epoxide reductase로 정정 |
| ADME/route/assay/stereoisomer context | 1–2문장으로 압축 |
| Hill code / NONMEM `$DES` template | 삭제; 후속 implementation 세션으로 이연 |
| Hb-O2, Michaelis-Menten/Langmuir, AI/regulatory meta-claims | PDF 범위 외이므로 삭제 |
| self-test의 unsupported hypothetical quantitative claims | 삭제 또는 source-grounded question으로 교체 |

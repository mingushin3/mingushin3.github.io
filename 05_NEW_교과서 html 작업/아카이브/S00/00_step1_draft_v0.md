━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
**STEP 1 DRAFT v0 — Pre-Sprint: 모델링 철학·용어**
Source: Gabrielsson & Weiner 5e Ch.1 (p.1–7) + Rowland & Tozer 5e Ch.1–2 (p.3–49)
Mode: B-Standard | Image rights: None
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Curation Map

이 세션은 두 권의 교과서가 **인식론적 분업**을 이루는 진입점 세션이다. Gabrielsson은 *"어떤 사고 순서로 모델링할 것인가"*를, Rowland & Tozer는 *"PK/PD 언어로 임상 의사결정을 어떻게 정량화할 것인가"*를 담당한다. 두 축이 만나 28세션 PopPK 커리큘럼의 인식론적 골격을 형성한다.

## MUST tier (4개) — 전용 §2 Concept Anatomy Card 작성

| # | 개념 | 담당 소스 | MUST 판정 근거 |
|---|------|----------|---------------|
| **M1** | **Modeling Carousel & 5대 dysfunction (EDA-First 철학)** | G Ch.1 §1.4 | 이 사고 순서를 내면화하지 않으면 후속 모든 NONMEM 세션에서 "fitting부터 돌리는" 습관이 굳어진다. Local minimum 회피, 초기추정치 감각, GOF 진단 로직 전체가 이 사고 순서에서 파생된다. **Apex Concept 후보.** |
| **M2** | **PK/PD Linkage & Therapeutic Window** | T Ch.1 | "PK와 PD를 두 개의 퍼즐 조각으로 분리해서 보지 않는 통합적 시각"이 이 카드의 핵심. Therapeutic Window는 모든 용량 결정·TDM·NDA 라벨링 결정의 출발점이며, PK/PD 통합 모델의 존재 이유 그 자체. |
| **M3** | **Emax / C50 / Hill γ — 농도-반응 정량화 핵심 수식** | T Ch.2 | 후속 PD 모델링 전 영역(direct-effect, indirect-response, biophase, TMDD downstream)에서 이 3-파라미터 체계가 골격으로 재등장. γ의 의미를 체화하지 못하면 quantal vs graded 구분, 임상 안전 마진 해석 모두 흔들린다. |
| **M4** | **Turnover (Pool Size · Turnover Rate · Fractional Turnover Rate · Turnover Time)** | T Ch.2 마지막 섹션 | Indirect response model, 내인성 물질 PK/PD(epoetin, statin, anticoagulant), warfarin·paclitaxel의 지연 반응 해석의 선행 개념. $k_t$, $t_t$, $A_{ss}$ 정의 없이는 이후 모든 turnover-based 모델 도출이 불가능. |

## CONTEXT tier — 가장 적합한 MUST 카드에 1–2문장으로 흡수

| 개념 | 흡수 위치 | 처리 방식 |
|------|----------|----------|
| Constant / Parameter / Variable / Primary vs Secondary Parameter | M1 카드 §A 정의 부분 | 모델링 jargon 정리 1–2문장 |
| ADME, Disposition, First-pass loss, Bioavailability, Enterohepatic cycle | M2 카드 §D Assumptions 부분 | "PK phase가 전제하는 anatomical-physiological 구조" 1–2문장 |
| Intravascular vs Extravascular vs Parenteral 투여 경로 | M2 카드 §E Limitations | "투여 경로가 노출 곡선을 결정" 1문장 |
| Plasma vs Serum vs Whole Blood 측정 부위 차이, Unbound concentration | M3 카드 §D | "반응을 결정하는 것은 unbound 농도" 1–2문장 |
| Active metabolite / Prodrug / Stereoisomer (acenocoumarol, methylphenidate) | M3 카드 §E Limitations | "측정한 농도가 활성 분자가 아닐 수 있다" 1문장 |
| Cmax, tmax, AUC 정의 | M3 카드 §A | 1문장으로 정의 후 진행 |
| NCA vs Compartmental model 선택 | M1 카드 §C-2 (Apex Plausible Fallacy 후보) | "단순한 질문에는 단순한 도구" 1–2문장 |
| Adherence (Vrijens 2008 곡선) | M2 카드 §E | "처방 regimen ≠ 실제 노출" 1문장 |
| Variability sources (genetic, age, drug-drug interaction) | M2 카드 §E | 1–2문장 |
| Graded vs Quantal response | M3 카드 §B 도출 직후 | 1–2문장 |
| Clinical response / Surrogate endpoint / Biomarker / Safety biomarker | M3 카드 §E | "측정 종류의 위계" 1–2문장 |
| Placebo effect, Disease progression (Duchenne 예시) | M4 카드 §E | 1–2문장 |
| Agonist / Antagonist / Partial agonist | M3 카드 §A | 1문장 |

## 구조 결정 사항

- **Apex Concept 지정**: **M1 (Modeling Carousel & 5대 dysfunction)** — Plausible Fallacy ⚡ 적용. 이유: B-Standard 세션이지만, 박사 1년차가 가장 자주 빠지는 함정("EDA 건너뛰고 fitting부터")이 정확히 여기에 있고, 이후 모든 NONMEM 워크플로 세션에서 재인용되는 메타 개념이기 때문.
- **§5 혼동쌍 후보**: 3쌍 식별 — (a) Pharmacokinetics vs Pharmacodynamics, (b) Graded vs Quantal Response, (c) Turnover Rate vs Fractional Turnover Rate. **Critical Blow는 (a)에 적용** — PK/PD 분리 사고가 NDA 제출 시 가장 큰 deficiency 사유가 되기 때문.
- **§7 보스 딜레마**: Modeling Carousel의 Step 4(EDA) vs Step 5(Fitting) — 시간 압박 하에서 어느 쪽을 희생할 것인가.

이제 Curation Map이 완성되었으므로 본문 작성을 시작한다.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# §1 — Session Header & Roadmap

**Source**: Gabrielsson & Weiner 5e — Chapter 1: General Principles (p.1–7)
Rowland & Tozer 5e — Chapter 1: Therapeutic Relevance (p.3–17), Chapter 2: Fundamental Concepts and Terminology (p.19–49)

**Big Idea (한 문장)**:
> 모델링은 *수식 fitting*이 아니라 **임상 질문 → 실험 설계 → 데이터 탐색 → 모델 선택 → 진단**의 순환 사고이며, PK/PD는 그 순환 안에서 *용량을 임상 결과로 번역하는 정량 언어*다.

**개념 항법도**:

```
[G Ch.1 — 사고 방법론 축]                  [T Ch.1–2 — 임상 정량화 축]
                                          
M1. Modeling Carousel (6단계)              M2. PK/PD Linkage
    ├─ Tentative model                        ├─ Therapeutic Window
    ├─ Design                                 ├─ Variability sources
    ├─ Run experiment                         └─ Adherence
    ├─ Explore data (EDA) ← Apex          
    ├─ Fit model(s)                       M3. Emax / C50 / Hill γ
    └─ Analyze output                         ├─ Graded vs Quantal
                                              └─ Stereoisomer / Active metabolite
    + 5대 dysfunction                     
                                          M4. Turnover
                                              ├─ Pool size, Rt, kt, tt
                                              └─ Disease progression
```

**지식 그래프 위치**:
- **선행 지식**: 없음 (커리큘럼 진입점)
- **후속 개방**:
  - M1 → 모든 NONMEM 세션의 워크플로 철학, GOF 진단 로직, $COVARIANCE 디버깅
  - M2 → 1구획·다구획 모델, Clearance·Vd 체계, TDM 임상 적용
  - M3 → Direct-effect PD 모델, biophase model, indirect response model 진입점
  - M4 → Indirect response model, disease progression model, TMDD downstream effects

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# §2 — Concept Anatomy Cards

---

## Card M1 ⚡ Apex Concept — Modeling Carousel & 5대 Dysfunction

<!-- MASTER LENS -->
### [개념 Big Idea: 거장의 시각]

**왜 치명적으로 결정적인가**: Phase 1 FIH 용량 결정 회의실에서, 데이터를 받자마자 NONMEM에 control stream을 던지는 신진 모델러는 *반드시* local minimum에 수렴한 모델을 들고 와서 잘못된 용량을 추천한다 — 그리고 그 용량이 그대로 first-in-human 임상시험에 들어간다. 이 함정을 막는 단 하나의 방어선이 **EDA를 fitting보다 앞에 두는 사고 순서**다.

**체화해야 할 단 하나의 직관**: 모델링은 "fitting이 시작점"이 아니라 "fitting은 6단계 중 5번째이고, 그 앞의 4단계(가설→설계→실험→EDA)가 fitting의 품질을 결정한다." 즉, *fitting의 정확도는 fitting 알고리즘이 아니라 그 앞에 무엇을 했느냐로 정해진다.*

**이 직관을 머릿속에 박고 아래를 읽어라**: 아래의 6단계 순환과 5대 dysfunction은 모두 이 한 가지 통찰의 변주다.
<!-- /MASTER LENS -->

### A. Formal Definition

**Modeling Carousel** (G Fig.1.1): 성공적 모델링을 보장하는 6단계 순환적 워크플로.

1. **Tentative model** — 실험 전 사전 가설 (e.g., "혈압 응답은 Emax 모델로 기술 가능하다")
2. **Design** — 용량, 샘플링 시간, 대상 인구의 사전 결정. CATD(Computer Assisted Trial Design)와 사전 시뮬레이션 포함.
3. **Run experiment** — 실제 데이터 수집
4. **Explore data (EDA)** — 그래프 기반 탐색. *concentration vs time, response vs time, response vs concentration* 3종 플롯 우선.
5. **Fit model(s)** — 비선형 회귀로 파라미터 추정 (NONMEM 등)
6. **Analyze output & model discrimination** — GOF, residual, parameter precision, model validation

**모델링 jargon 정리** *[CONTEXT 흡수]*: G Ch.1.2의 용어 정의 — Dose $D$는 **constant** (값을 알고 회귀 중 변하지 않음); $V$, $CL$은 **parameter** (회귀로 추정); $\hat{C}$, $t$는 **variable**. $V$, $CL$은 **primary parameter**, 이로부터 도출되는 $K = CL/V$, $AUC = D/CL$, $t_{1/2} = \ln(2)/K$는 **secondary parameter** (중요도가 낮은 것이 아니라 *primary로부터 도출되는 것*이라는 의미). 관측치-예측치 관계: $C = \hat{C} + \varepsilon$.

**5대 Dysfunction** (G p.4): 모델링 카이네티스트가 가장 자주 저지르는 5가지 결함.
1. EDA의 가치를 인식하지 못함 (가장 빈번)
2. 수식에 노예화됨 (slavery to formulas)
3. 모델링 소프트웨어를 과신함 (too much trust in modeling software)
4. 부적절한 weighting 사용
5. 전체적('holistic') 시각의 결여

### B. Derivation / Code Structure

[B.1] **Carousel 단계의 논리적 필연성** — 왜 정확히 이 6단계 순서인가?

각 단계는 다음 단계의 입력을 정의한다:

$$
\text{Step 1 (가설)} \xrightarrow{\text{이끌어냄}} \text{Step 2 (설계)} \xrightarrow{\text{생성}} \text{Step 3 (데이터)} \xrightarrow{\text{탐색}} \text{Step 4 (EDA)}
$$
$$
\text{Step 4 (EDA)} \xrightarrow{\text{제공}} \begin{cases} \text{모델 구조} \\ \text{초기추정치 (initial estimates)} \end{cases} \xrightarrow{\text{입력}} \text{Step 5 (Fit)} \xrightarrow{\text{진단}} \text{Step 6 (Analyze)}
$$

**Step 5(Fit)의 알고리즘적 요구사항**: G p.6 명시 — *"algorithms for fitting nonlinear models generally require initial estimates of the parameters. These initial estimates should be provided by the modeler to avoid convergence of the program to a local minimum."* 즉, Step 4(EDA)가 생성한 *graphical initial estimates*가 Step 5의 입력으로 직접 들어간다. **EDA를 건너뛰면 Step 5는 바로 local minimum 위험**으로 진입한다 (G Fig.1.2 — parameter space의 OFV landscape, A·B·C·E 후보 시작점 중 일부는 local minimum, 일부는 global minimum으로 수렴). `[출처: Gabrielsson 5e, Ch.1, p.6]`

[B.2] **EDA에서의 표준 비선형성 진단 절차** (G p.5):
- 여러 dose level의 plasma concentration curve를 **dose-normalize** → 시간 축에 겹쳐 plot
- 또는 $AUC$ vs $dose$ plot
- 비선형성이 있으면 dose-normalized curve가 겹치지 않음 → Michaelis-Menten 등 saturable kinetics 가능성

### C. Structural Necessity

**왜 정확히 6단계인가? 왜 다른 형태로는 안 되는가?**

수학적 필연성 추적:
- **Step 1(Tentative model) 없이 Step 2(Design)만으로는** — 어떤 시간 점에서 샘플링할지, 어떤 용량을 줄지 결정 불가능. 모델 구조에 대한 사전 가설이 sampling design을 결정한다 (D-optimal design 이론의 기초).
- **Step 3(Run) 후 Step 4(EDA) 없이 Step 5(Fit)로 직행하면** — 비선형 회귀가 요구하는 *initial estimates*를 얻을 방법이 없다. 임의 초기값 → local minimum convergence (G Fig.1.2).
- **Step 5(Fit) 없이 Step 6(Analyze)만 하면** — 분석할 추정치가 존재하지 않음.
- **Step 6 후 Step 1로의 순환 (carousel)** — 모델 검증(model validation)은 새로운 데이터셋에 대한 시뮬레이션과 fitting을 통해서만 가능 → Step 2 또는 Step 5로 재진입.

이 순서는 *임의적 관습*이 아니라 *비선형 회귀 알고리즘의 수학적 요구사항*과 *과학적 가설검증의 epistemological 구조*가 결합한 필연이다.

### C-2. ⚡ Plausible Fallacy: "데이터부터 NONMEM에 던지자" 함정

**오류의 구체적 형태**: 박사 1년차가 임상 데이터셋을 받자마자 — Carousel의 Step 1(가설), Step 4(EDA)를 건너뛰고 — control stream을 작성하여 즉시 `$ESTIMATION METHOD=1` 실행. 이유는 그럴싸하다: *"어차피 NONMEM이 잘 fitting해줄 텐데, 굳이 시간 들여 plot 그릴 필요가 있나?"*

**나비효과의 기계론적 추적**:
1. EDA 부재 → 초기추정치는 임의값 또는 default → 파라미터 공간(G Fig.1.2)에서 local minimum hollow에 수렴
2. local minimum의 $V$, $CL$ 추정치는 global minimum 대비 편향됨 → secondary parameter $K = CL/V$, $t_{1/2}$도 편향
3. 이 편향된 모델로 simulation → Phase 2 dose recommendation에서 **AUC를 30~50% 잘못 예측**
4. NONMEM 출력은 외형상 "수렴 성공"으로 보임 — `$COV` step도 통과 가능 (local minimum 주변에서는 Hessian이 양정치)
5. GOF plot도 fit이 *무난해 보임* (잔차가 임의로 흩어져 있어 보임)

**발견 시그니처 — "Local Minimum Mirage"**: `$ESTIMATION`을 *서로 다른 4개 이상의 초기추정치*로 재실행했을 때, OFV가 5 단위 이상 다른 값으로 수렴하면 의심. global minimum으로 수렴한 run은 항상 가장 낮은 OFV를 보임. G p.6 권고: *"rerunning the program with different initial estimates, and possibly using algorithms that employ different approaches to model fitting."*

### D. Assumptions & Boundary Conditions

- **Carousel 적용 가정**: 모델링 목적이 *질문에 답하기 위함*이라는 전제. 단순 노출 측정(bioavailability, total clearance)에는 NCA(Noncompartmental Analysis)로 충분. *"we strongly encourage scientists only to model when they need to"* (G p.4).
- **NCA의 가정 강도**: NCA도 모델링이지만 가정이 덜 제약적. Compartmental model이 필요한 경우: (a) single dose → multiple dose 예측, (b) 비선형 PK 영역, (c) PK-PD 정량 연계.
- **EDA의 그래픽 초기값 산출 가정**: 데이터의 dose level이 충분히 다양하고 sampling이 dense해야 dose-normalization 진단이 의미 있음.

### E. Limitations

- **Carousel은 *언제* 빠져나갈지 알려주지 않는다**: Step 6 이후 Step 1로 돌아가야 하는지(추가 실험), Step 5로 돌아가야 하는지(다른 모델 시도) 결정은 모델러의 *judgment*. 이 부분은 framework가 자동화하지 않는다.
- **6단계 순서는 *필요조건*이지 *충분조건*이 아니다**: 모든 단계를 거쳐도 데이터 자체가 빈약하면(sparse, identifiability 문제) 모델은 실패. *"Multiple dose levels, repeated dosing, and multiple input rates and routes of administration are often needed"* (G p.7).
- **5대 dysfunction은 *동시에* 발생할 수 있다**: 하나만 막아도 충분한 것이 아님. EDA를 했어도 weighting이 잘못되면 결과는 동일하게 편향.

### F. Five Cognitive Layers

| 레이어 | Vol I — 이론 시각 |
|---|---|
| **L1 Formal** | Carousel 6단계가 nonlinear regression의 algorithmic requirement(initial estimates)를 만족시키는 *순서적 필연*임을 인식 |
| **L2 Geometric** | G Fig.1.2 — parameter space를 *bowl* 형태로 시각화. EDA가 좋은 시작점(E 위치)으로 데려다주고, 임의 초기값(A, B 위치)은 local hollow에 빠진다 |
| **L3 Structural Isomorphism** | Carousel ≅ scientific method 일반 (hypothesis → design → experiment → analysis → conclusion → new hypothesis). 또한 ≅ Plan-Do-Check-Act (PDCA) cycle (industrial quality control), ≅ OODA loop (의사결정 이론) |
| **L4 Physiological** | EDA가 드러내는 attribute: time delay (PK→PD), saturation (M-M kinetics), hysteresis (effect site delay), adaptation (tolerance). 모두 underlying biology의 직접 신호 |
| **L5 Practical** | NONMEM `$ESTIMATION` 전에 R/SAS로 NONMEM dataset의 PROC PRINT, plot.xpose, dose-normalized AUC plot을 *반드시* 먼저 생성. 이것이 Step 4의 실무 구현 |

### G. Zettelkasten Atom

```yaml
---
aliases: [Modeling Carousel, EDA-First, Five Dysfunctions]
tags: [pharmacometrics/methodology, nonmem/workflow, modeling/philosophy]
up: "[[PK-PD Mastery MOC]]"
related: ["[[Local Minimum]]", "[[Initial Estimates]]", "[[GOF Diagnostics]]", "[[NCA vs Compartmental]]"]
source: "Gabrielsson & Weiner 5e, Ch.1, p.1-7"
---

Modeling은 fitting이 아니라 6단계 순환(가설→설계→실험→EDA→fit→분석)이며,
EDA가 Step 5의 initial estimates를 제공하기 때문에 EDA를 건너뛰면
local minimum convergence가 algorithmic으로 불가피해진다.
G Fig.1.2의 parameter space bowl이 이 함정의 기하학적 형태다.
5대 dysfunction 중 EDA 누락이 가장 빈번하며, 다른 4개(수식 노예화,
소프트웨어 맹신, 부적절한 weighting, holistic 시각 결여)와 독립적으로
또는 동시에 발생할 수 있다.
```

<!-- ANCHOR -->
Carousel이 *어떻게* 모델링하는지를 정의했다면, 다음 카드 M2는 *왜 그렇게 모델링하는지* — 즉 PK와 PD를 통합해야만 임상 의사결정이 가능하다는 *목적론적 필연*을 정의한다.
<!-- /ANCHOR -->

---

## Card M2 — PK/PD Linkage & Therapeutic Window

<!-- MASTER LENS -->
### [개념 Big Idea: 거장의 시각]

**왜 치명적으로 결정적인가**: Digoxin은 1일 1회 0.125–0.25 mg, Morphine sulfate는 1일 6회 10–50 mg이다. 두 약물 모두 narrow therapeutic window를 갖는데도 dosing frequency가 50배 차이나는 이유 — 이것을 PK 단독으로도, PD 단독으로도 설명할 수 없다. *PK와 PD를 두 개의 퍼즐 조각으로 분리해서 보지 않고 하나로 결합할 때만* 임상 의사결정이 정량화된다.

**체화해야 할 단 하나의 직관**: PK와 PD는 *서로 반대*가 아니라 *서로 맞물리는 입력-출력 chain*이다. PK는 "*body가 약물에 무엇을 하는가*"(ADME), PD는 "*약물이 body에 무엇을 하는가*"(effect). 둘 중 하나만으로는 effect-vs-time을 예측할 수 없다 — 이것이 **PK/PD modeling의 존재 이유** 그 자체.

**이 직관을 머릿속에 박고 아래를 읽어라**: Therapeutic Window는 PK와 PD가 *맞물리는 정확한 지점*에서만 의미를 가진다.
<!-- /MASTER LENS -->

### A. Formal Definition

**Pharmacokinetics (PK)**: 약물 입력(dose, dosage form, route, frequency)과 시간에 따른 농도 사이의 관계. 즉 "concentration vs time."

**Pharmacodynamics (PD)**: 농도와 desired/adverse effect 사이의 시간 의존적 관계. 즉 "concentration vs effect."

**PK/PD Linkage**: 두 phase가 dosage regimen → exposure → response의 인과 chain으로 결합된 통합 모델 (T Fig.1-2, T Fig.1-3).

**Therapeutic Window** (T Fig.1-4): therapeutic response를 충분히 얻으면서 adverse effect 발생 확률은 낮은 *exposure 범위*. Narrow window 약물 예: digoxin, phenytoin, cyclosporine, warfarin.

**ADME 처리 *[CONTEXT 흡수]*** — *Disposition*은 distribution + elimination을 합한 개념. *First-pass loss*는 oral 투여 후 site of measurement(arm vein plasma) 도달 전 GI tract·간에서 발생하는 손실. *Bioavailability*는 systemically absorbed intact fraction (이 책 정의는 *extent*만, rate는 별도). *Enterohepatic cycle*은 distribution의 component (T Fig.2-10).

**투여 경로 *[CONTEXT 흡수]*** — Intravascular(i.v., i.a.)는 absorption step 불필요; Extravascular(oral, i.m., s.c., 등)는 absorption 필요; Parenteral은 *apart from intestines* 의미로 needle 주사 통칭(일반적으로). Regional administration(intra-arterial, intrathecal 등)은 local exposure 극대화 + systemic exposure 최소화 전략.

### B. Derivation / Code Structure

[B.1] **PK Mass Balance** (T Eq.2-1, T p.28):

$$
\text{Dose} = \underbrace{A_{\text{absorption site}}}_{\text{미흡수}} + \underbrace{A_{\text{body}}}_{\text{체내}} + \underbrace{A_{\text{excreted}}}_{\text{배설}} + \underbrace{A_{\text{metabolized}}}_{\text{대사}}
\quad \text{`[출처: Rowland \& Tozer 5e, Ch.2, p.28]`}
$$

미분 형태 (T Eq.2-2):

$$
\frac{dA_{\text{body}}}{dt} = R_{\text{absorption}} - (R_{\text{excretion}} + R_{\text{metabolism}})
$$

이 mass balance는 *모든* PK 모델(NCA, compartmental, PBPK)이 만족해야 하는 보존 법칙. 위반 시 모델 잘못.

[B.2] **PK/PD Chain의 인과 구조** (T Fig.1-2, 보강된 형태 Fig.1-11):

$$
\underbrace{\text{Prescribed Regimen}}_{\text{처방 의도}} \rightarrow \underbrace{\text{Adherence Pattern}}_{\text{실제 복용}} \rightarrow \underbrace{\text{Exposure}}_{\text{PK phase}} \rightarrow \underbrace{\text{Effect}}_{\text{PD phase}}
$$

*Adherence를 무시한 PK/PD 모델은 real-world 효과를 과대추정한다* — Vrijens 2008 (T Fig.1-10): once-daily 항고혈압제 처방 1년 후 persistence는 ~50%까지 감소.

[B.3] **Therapeutic Window의 운용 정의**:

$$
\text{Therapeutic Window} = \{ C \in \mathbb{R}_{\geq 0} \,:\, \Pr(\text{therapeutic effect} \mid C) \geq \theta_{\text{therapeutic}} \,\wedge\, \Pr(\text{adverse effect} \mid C) \leq \theta_{\text{adverse}} \}
$$

여기서 $\theta_{\text{therapeutic}}$, $\theta_{\text{adverse}}$는 임상적 acceptance 기준. Narrow window 약물은 이 집합이 작은 구간이며, drug variability(genetic, age, drug-drug interaction)가 크면 환자 일부가 이 구간 밖으로 나가 부적절 치료 또는 toxicity 경험.

### C. Structural Necessity

**왜 PK와 PD가 분리되었다가 다시 합쳐져야 하는가?**

1. **분리의 이유**: 두 phase는 *서로 다른 mechanism*에 의해 지배됨 — PK는 organ blood flow, transporter, metabolizing enzyme; PD는 receptor, signal transduction, downstream physiology. 분리해야 각각의 mechanism을 독립적으로 modulate 가능 (e.g., PK 변화 없이 PD만 바뀌는 receptor antagonist).

2. **결합의 이유**: T Fig.1-3 — PK plot(conc vs time) + PD plot(conc vs effect)을 따로 그려서는 *effect vs time*을 예측할 수 없다. 환자에게 가는 정보는 항상 *effect-time profile*이며, 이는 두 plot을 *수학적으로 결합*해야만 도출됨.

3. **Time delay의 두 발생원**: (a) PK 분포 지연 (drug → effect site, e.g., digoxin 심장 작용 지연), (b) PD 시스템 지연 (turnover-based, e.g., warfarin 응고인자 합성 억제 → 2–4일 지연; T Fig.1-6 — 1.5 mg/kg sodium warfarin oral, 5 male volunteers). 두 지연을 구분하지 않으면 dose-titration 결정이 잘못됨.

### D. Assumptions & Boundary Conditions

- **Plasma concentration이 site of action 농도의 valid surrogate라는 가정**: 대부분 약물에 대해 성립하나, BBB 통과가 제한적인 약물(중추 작용 약물)에서는 부분적으로 깨짐.
- **Active metabolite·Prodrug 부재 가정**: 위반 시 측정 plasma drug과 effect 사이 관계 왜곡 (M3 카드에서 별도 다룸).
- **Stable PK/PD relationship 가정**: tolerance, sensitization, disease progression이 있으면 시간 가변. Carousel Step 6에서 이 가정을 검증해야.
- **Stereoisomer mixture 무시 가정**: racemate를 단일 entity로 측정하면 PK/PD 관계 왜곡 (acenocoumarol R-(+) vs S-(-): T Fig.2-2A; methylphenidate (+) vs (-): T Fig.2-2B에서 전혀 다른 노출 곡선).

### E. Limitations

- **Variability sources** *[CONTEXT 흡수]*: age, weight, obesity, disease severity, concurrent medication, environmental factors, **genetics** (G6PD deficiency → primaquine hemolysis; CYP2D6 polymorphism → debrisoquine; CYP2C9·VKORC1 → warfarin variability T Fig.1-9, 97 patients on maintenance therapy; phenytoin T Fig.1-8). 이러한 variability 때문에 "one-dose-for-all"은 narrow window 약물에서 작동하지 않음.
- **Adherence 현실** *[CONTEXT 흡수]*: T Fig.1-10 — antihypertensive 1년 후 ~50%만 지속. Real-world effect를 모델로 예측할 때 prescribed regimen이 아닌 *actual adherence pattern*을 입력으로 사용해야.
- **Drug-drug interaction**: terfenadine + ketoconazole → CYP inhibition으로 terfenadine 노출 폭증 → torsade de pointes (시장 철수 사례).
- **모델은 평균에 fit되지만 결정은 개인에 대해 이루어짐**: population mean 효과적이라도 개별 환자가 효과 범위 밖일 수 있음.

### F. Five Cognitive Layers

| 레이어 | 통합 시각 |
|---|---|
| **L1 Formal** | Mass balance (Eq.2-1) + ODE (Eq.2-2)가 PK의 수학적 골격; PK→PD chain의 hierarchical model 구조 |
| **L2 Geometric** | T Fig.1-3의 *세 plot 결합*: conc-time + conc-effect → effect-time. 두 곡선의 *convolution*이 임상 결과 |
| **L3 Structural Isomorphism** | PK/PD chain ≅ control system (input → plant → output), ≅ stimulus-response in classical psychology, ≅ Hill function in enzymology |
| **L4 Physiological** | ADME의 각 단계가 organ 단위 — Absorption(GI), Distribution(blood, tissue), Metabolism(liver, CYP), Excretion(kidney). Therapeutic window는 receptor density × physiological reserve × signal transduction의 함수 |
| **L5 Practical** | NONMEM `$INPUT` column 설계 시 EVID·MDV·DV·DOSE 컬럼이 mass balance를 hardcoding; PD 관측치는 별도 CMT로 추가; drug-drug interaction은 covariate로 모델링 |

### G. Zettelkasten Atom

```yaml
---
aliases: [PK/PD Linkage, Therapeutic Window, Input-Response Phases]
tags: [pharmacometrics/concept, regulatory/therapeutic-window, clinical/dosing]
up: "[[PK-PD Mastery MOC]]"
related: ["[[ADME]]", "[[Bioavailability]]", "[[Adherence]]", "[[Variability Sources]]"]
source: "Rowland & Tozer 5e, Ch.1 (p.3-17), Ch.2 (p.19-49)"
---

PK는 dose→concentration, PD는 concentration→effect를 담당하며,
두 phase는 dosage regimen → adherence → exposure → effect 의 chain으로
결합된다. Effect-vs-time 곡선은 두 phase 모델의 mathematical convolution
없이는 예측 불가능하다. Therapeutic Window는 narrow일수록(digoxin, warfarin,
phenytoin, cyclosporine) variability sources(genetics, drug-drug interaction,
adherence)가 임상 결정의 dominant factor가 된다.
```

<!-- ANCHOR -->
PK/PD chain의 PD 끝단을 *수식으로* 표현하기 위해 다음 카드 M3는 농도-반응 정량화의 핵심 3-파라미터 체계(Emax, C50, γ)를 도입한다.
<!-- /ANCHOR -->

---

## Card M3 — Emax / C50 / Hill γ

<!-- MASTER LENS -->
### [개념 Big Idea: 거장의 시각]

**왜 치명적으로 결정적인가**: 박사 1년차가 PD 데이터 fitting에서 가장 자주 실수하는 지점 — γ를 1로 고정하고 Emax 모델을 돌리는 것. 그러나 propranolol은 γ≈1, ketamine은 sigmoidal(γ>1), opioid 마취제는 γ가 매우 커서 거의 quantal에 가까운 곡선을 보인다. **γ의 값이 임상 안전 마진 자체를 결정**한다 — γ가 크면 작은 농도 변화로 효과가 0→100% 점프하므로 narrow therapeutic window와 등가.

**체화해야 할 단 하나의 직관**: Emax는 *"얼마까지"*, C50는 *"어디서"*, γ는 *"얼마나 가파르게"* — 세 파라미터가 PD 곡선의 *모든 임상적 함의*를 인코딩한다. *Potency(C50가 작음)는 important하지만 maximum effect(Emax)가 부족하면 약은 임상적으로 useless이고, γ가 너무 크면 dose titration이 불가능*.

**이 직관을 머릿속에 박고 아래를 읽어라**: 이 3-파라미터는 후속 PD 모델(direct, indirect, biophase, TMDD)에서 *항상 재등장*하는 골격 어휘다.
<!-- /MASTER LENS -->

### A. Formal Definition

**Hill (Emax) 방정식** (T Eq.2-4):

$$
E = \frac{E_{\max} \cdot C^{\gamma}}{C_{50}^{\gamma} + C^{\gamma}} \quad \text{`[출처: Rowland \& Tozer 5e, Ch.2, p.40]`}
$$

- $E$: response intensity (baseline 대비 변화량 또는 %)
- $E_{\max}$: maximum achievable effect — 약물의 *intrinsic ceiling*
- $C_{50}$: 50% of $E_{\max}$를 내는 농도 — *potency*의 정량 지표
- $\gamma$: Hill factor (steepness factor) — 곡선의 가파름

**Cmax / tmax / AUC 정의 *[CONTEXT 흡수]*** — Cmax는 *peak systemic exposure* (T Fig.2-1), tmax는 그 시점, AUC는 *total systemic exposure* (T p.22, trapezoidal approximation).

**Agonist / Antagonist *[CONTEXT 흡수]*** — Agonist는 receptor functional response 증가, Antagonist는 감소. *Full*은 maximum 가능 effect 도달, *Partial*은 미달. Estrogen은 농도 영역에 따라 agonist↔antagonist 전환 (특이 사례).

**Graded vs Quantal *[CONTEXT 흡수]*** — *Graded*는 individual 내에서 연속적 magnitude (T Fig.2-11, ketamine EEG median frequency). *Quantal*은 all-or-none (e.g., 부정맥 억제 여부, 사망). Quantal response는 cumulative frequency vs concentration plot으로 정량 (T Fig.2-18, alfentanil).

### B. Derivation / Code Structure

[B.1] **Emax 곡선의 점근선 분석**:

$$
\lim_{C \to 0} E = \frac{E_{\max} \cdot C^{\gamma}}{C_{50}^{\gamma}} \approx 0 \quad \text{(linear region)}
$$

$$
\lim_{C \to \infty} E = E_{\max} \quad \text{(saturation)}
$$

$$
E(C = C_{50}) = \frac{E_{\max} \cdot C_{50}^{\gamma}}{C_{50}^{\gamma} + C_{50}^{\gamma}} = \frac{E_{\max}}{2}
$$

[B.2] **γ의 영향 정량화 — 20%·80% 효과 농도의 비율** (T p.40):

20%·80% 효과 농도 비율(=therapeutic latitude의 역수)을 계산하면:

$$
\gamma = 1: \quad \frac{C_{80\%}}{C_{20\%}} = \frac{4 \cdot C_{50}}{0.25 \cdot C_{50}} = 16
$$

$$
\gamma = 2: \quad \frac{C_{80\%}}{C_{20\%}} = \frac{2 \cdot C_{50}}{0.5 \cdot C_{50}} = 4
$$

γ=2일 때 농도 범위가 16배에서 4배로 좁아짐 → narrow margin. γ→∞면 quantal에 점근.

[B.3] **실제 수치 앵커링** (T 텍스트·Fig.2-17):
- **Propranolol**: exercise-induced tachycardia 감소 측정, γ ≈ 1, C50 = 5.3 µg/L (unbound), Emax ≈ 40% decrease. (T Fig.2-17, Lalonde et al. 1987)
- **Ketamine**: EEG median frequency reduction 측정, S(+)-isomer Emax ≈ 90%, C50 ≈ 0.7 mg/L; R(-)-isomer Emax ≈ 42%, C50 ≈ 1.8 mg/L. (T Fig.2-11, Schuttler et al. 1985)
- **Alfentanil**: nitrous oxide anesthesia 보조 quantal response — C50 (50% satisfactory control) — breast 0.27 mg/L < lower abdomen 0.31 mg/L < upper abdomen 0.42 mg/L. (T Fig.2-18, Ausems et al. 1986)

[B.4] **R nlmixr2 / NONMEM coding skeleton**:

```r
# nlmixr2 — Hill model
hill_pd <- function() {
  ini({
    tEmax <- 40      # %
    tC50  <- 5.3     # ug/L (unbound)
    tgamma <- 1
    eta.Emax ~ 0.1
  })
  model({
    Emax <- tEmax * exp(eta.Emax)
    eff  <- Emax * (Cu^tgamma) / (tC50^tgamma + Cu^tgamma)
    eff ~ add(prop.err)
  })
}
```

```fortran
; NONMEM $PRED block — Hill model
$PRED
EMAX  = THETA(1)*EXP(ETA(1))
C50   = THETA(2)
GAMMA = THETA(3)
EFF   = EMAX*(CU**GAMMA)/(C50**GAMMA + CU**GAMMA)
Y     = EFF + EPS(1)
```

### C. Structural Necessity

**왜 정확히 이 3-파라미터 형태인가?**

1. **수용체 결합 화학에서의 mass action 법칙**: drug + receptor ⇌ drug-receptor complex의 saturable binding이 Michaelis-Menten 형태를 강제 → γ=1의 hyperbolic curve (Langmuir isotherm).
2. **γ ≠ 1의 발생 기전**: positive cooperativity (allosteric, multi-site binding) → γ > 1 (sigmoidal); receptor pool heterogeneity 또는 multiple action sites → γ < 1 (shallow).
3. **세 파라미터의 *독립성***: $E_{\max}$는 receptor pool size + intrinsic activity가 결정; $C_{50}$는 binding affinity가 결정; $\gamma$는 cooperativity·heterogeneity가 결정. 셋이 *생물학적으로 분리된 mechanism*에서 나오므로 이 형태로 수식이 정착.

다른 형태(예: linear $E = k \cdot C$, exponential $E = E_{\max}(1 - e^{-kC})$)는 saturation 또는 cooperativity 둘 중 하나를 표현 못 함 → 이 3-파라미터가 *최소 충분 표현*.

### D. Assumptions & Boundary Conditions

- **Reversible binding**: 비가역 결합 약물(alkylating agent: busulfan)은 Emax 모델 적용 불가 — DNA에 covalent binding하므로 농도 감소해도 효과 reverse 안 됨.
- **Direct effect (no time delay)**: plasma concentration이 effect site와 즉시 평형. 위반 시 hysteresis 발생 → biophase model 필요 (warfarin, paclitaxel).
- **Single receptor population**: 다중 receptor 작용 약물(clonidine — 농도에 따라 hypotensive↔hypertensive)은 단일 Hill 모델로 표현 불가.
- **Unbound concentration이 driver** *[CONTEXT 흡수]*: total plasma concentration은 bound + unbound. Site of action에 도달하는 것은 unbound뿐이므로 *fraction unbound가 변하는 상황*(renal/hepatic disease, displacement interaction, pregnancy, severe burns)에서는 unbound 농도로 모델링 필수. Plasma vs serum vs whole blood (T Table 2-2): plasma는 protein binding 포함, serum은 fibrinogen 제거 후 거의 동일, whole blood는 cell fraction 평균.

### E. Limitations

- **Active metabolite·Prodrug** *[CONTEXT 흡수]*: 측정 분자가 활성 분자 아닐 수 있음. Aspirin → salicylic acid (T Fig.2-3, oral 650 mg) — anti-inflammatory 효과는 metabolite에 있음. Sildenafil은 active metabolite가 효과 augment. Prodrug 예: methylprednisolone hemisuccinate, dolasetron mesylate, famciclovir.
- **Stereoisomer 문제** *[CONTEXT 흡수]*: 측정 assay가 enantiomer 구분 못 하면 PK/PD 관계 왜곡. Acenocoumarol R-(+) vs S-(-) (T Fig.2-2A, oral 20 mg racemate); methylphenidate (+) >> (-) (T Fig.2-2B, oral 30 mg racemate); ketamine R(-) vs S(+) (T Fig.2-11). S-naproxen, tamsulosin (R-isomer, Flomax)은 single enantiomer로 시판.
- **Clinical Endpoint vs Surrogate vs Biomarker** *[CONTEXT 흡수]*: T 정의 — *Clinical response*는 환자에게 의미있는 결과 (생존, 통증 감소). *Surrogate endpoint*는 임상 결과로 *validated된* 대용 측정 (혈압 → 심혈관 morbidity). *Biomarker*는 *validated 안 된* 일반 측정 (혈당, EEG, PET binding). *Safety biomarker*는 일반 안전성 모니터링 (LFT, WBC, ESR). 효과 측정의 위계를 혼동하면 임상 의미 과대해석 위험.
- **Maximum response의 임상적 ceiling**: $E_{\max}$가 pharmacological maximum이지만, 환자가 그 농도에 도달하기 전에 다른 toxicity로 사망/중단 가능. Antagonist는 ceiling 정의 명확 (e.g., 100% paralysis), agonist는 불명확.
- **Resistance development**: T Fig.2-15 — moxifloxacin 28일 투여 시 *M. tuberculosis* 초기 감소 후 18일째 resistant subpopulation 출현, 28일에는 100% resistant. PK/PD 관계 자체가 시간에 따라 deteriorate.

### F. Five Cognitive Layers

| 레이어 | 내용 |
|---|---|
| **L1 Formal** | Hill equation 수식 자체 + 점근선 분석 + 20-80% 농도비 도출 |
| **L2 Geometric** | T Fig.2-16 — γ에 따른 곡선 모양 변화. semi-log scale에서 20-80% 구간이 거의 linear하다는 *transformation 직관* |
| **L3 Structural Isomorphism** | Hill equation ≅ Michaelis-Menten enzyme kinetics ($V_{\max}$, $K_m$), ≅ Langmuir adsorption isotherm, ≅ binding equilibrium with cooperativity |
| **L4 Physiological** | $E_{\max}$ ↔ receptor density · intrinsic efficacy; $C_{50}$ ↔ binding affinity ($K_d$); γ ↔ cooperativity (Hb-O2 binding γ≈2.7), receptor heterogeneity |
| **L5 Practical** | NONMEM/R Hill model coding; γ를 1로 fix vs estimate 결정; unbound concentration 사용 의무; stereospecific assay 사용; biomarker vs surrogate 구분하여 regulatory submission 작성 |

### G. Zettelkasten Atom

```yaml
---
aliases: [Hill Equation, Emax Model, Sigmoid Emax, C50, Hill Coefficient]
tags: [pharmacometrics/pd, modeling/sigmoid, regulatory/dose-response]
up: "[[PD Modeling MOC]]"
related: ["[[Direct Effect Model]]", "[[Indirect Response Model]]", "[[Michaelis-Menten]]", "[[Stereoisomer]]"]
source: "Rowland & Tozer 5e, Ch.2, Eq.2-4, p.40"
---

E = Emax * C^γ / (C50^γ + C^γ).
세 파라미터는 receptor pool size·affinity·cooperativity의 분리된
biology를 인코딩하므로 *최소 충분 표현*이다. γ는 임상 dose titration
가능성을 결정 — γ=1이면 20-80% 농도 범위 16배, γ=2면 4배로 압축.
γ→∞는 quantal에 점근 (alfentanil cumulative frequency curve).
실측 anchor: propranolol γ≈1, C50=5.3 µg/L (Lalonde 1987);
ketamine S(+) Emax≈90% C50=0.7 mg/L vs R(-) Emax≈42% C50=1.8 mg/L
(Schuttler 1985); alfentanil C50(quantal) breast 0.27 < lower abd 0.31
< upper abd 0.42 mg/L (Ausems 1986).
```

<!-- ANCHOR -->
Hill 방정식이 *순간적 농도-반응 관계*를 정량화한다면, 다음 카드 M4는 *반응이 시간 지연을 보이는 구조* — 즉 endogenous substance의 turnover 동역학을 도입한다. Warfarin의 2–4일 지연, paclitaxel의 leukocyte 회복 3주는 모두 turnover 개념 없이는 모델링 불가능.
<!-- /ANCHOR -->

---

## Card M4 — Turnover (Pool Size · Rate · Fractional Rate · Time)

<!-- MASTER LENS -->
### [개념 Big Idea: 거장의 시각]

**왜 치명적으로 결정적인가**: Warfarin oral 1.5 mg/kg single dose 후 plasma 농도는 수시간 내 peak이지만 prothrombin activity 효과는 *2일 후에야* peak에 도달한다 (T Fig.1-6, Nagashima et al. 1969). 이 2일 지연을 *PK 분포 지연*으로 잘못 해석하고 dose titration하면 — 1일째 효과 부족하다 판단 → 증량 → 2–3일째 누적 효과로 *internal hemorrhage*. 이 함정은 turnover 개념(*응고인자의 합성-분해 균형*)을 모르면 *반드시* 발생한다.

**체화해야 할 단 하나의 직관**: Steady state는 *static state*가 아니라 *dynamic equilibrium* — 입력률(synthesis)과 출력률(degradation)이 같아 pool size가 일정한 상태. 약물이 *어느 쪽*을 modulate하느냐에 따라 효과 지연 패턴이 결정된다. *Pool size 변화 속도 = fractional turnover rate × 변화량* — 이것이 후속 indirect response model 전체의 골격.

**이 직관을 머릿속에 박고 아래를 읽어라**: 4개 파라미터(pool size, turnover rate, fractional rate, turnover time)는 모두 *동일 동역학의 다른 표현*이지만, 임상적 함의가 다르다.
<!-- /MASTER LENS -->

### A. Formal Definition

**Pool size** $A_{ss}$: steady state에서 endogenous substance의 *총량*. (e.g., total body water 42 L)

**Turnover rate** $R_t$: 단위 시간당 들어오는 (= 나가는) 양 [mass/time]. (e.g., total body water $R_t$ ≈ 2.5 L/day)

**Fractional turnover rate** $k_t$ (T Eq.2-5):

$$
k_t = \frac{R_t}{A_{ss}} \quad [\text{time}^{-1}] \quad \text{`[출처: Rowland \& Tozer 5e, Ch.2, p.45]`}
$$

**Turnover time** $t_t$ (T Eq.2-6):

$$
t_t = \frac{A_{ss}}{R_t} = \frac{1}{k_t} \quad [\text{time}]
$$

**Steady state 가정**: rate of input = rate of elimination. 위반 시(input ≠ output) pool size 변화 진행 중 — turnover 정의 미적용.

**Disease progression *[CONTEXT 흡수]*** (T Fig.2-14): physiological function의 자연 노화 (~1%/year)에 disease가 가속을 부과. 약물 효과는 *symptomatic relief*(증상 일시 완화, 자연 progression 그대로), *stabilization*(자연 rate로 회귀), *cure*(정상 trajectory 복귀)로 분류. Prednisone in Duchenne dystrophy (T Fig.2-13)는 1–3개월 symptomatic improvement 후 자연 progression 복귀 → *symptomatic relief*만.

**Placebo effect *[CONTEXT 흡수]*** (T Eq.2-3): Measured response = drug response + placebo response + baseline. Montelukast 10 mg vs placebo (T Fig.2-12) — placebo 자체가 시간에 따라 increase-decline 패턴 보이며 substantial. Double-blind placebo-controlled trial 필수.

### B. Derivation / Code Structure

[B.1] **표준 ODE 도출** — pool size의 미분방정식:

$$
\frac{dA}{dt} = R_{\text{in}} - k_t \cdot A
$$

Steady state ($\frac{dA}{dt} = 0$):
$$
R_{\text{in}} = k_t \cdot A_{ss} \implies A_{ss} = \frac{R_{\text{in}}}{k_t}
$$

이 ODE는 **모든 indirect response model의 골격** — 약물이 $R_{\text{in}}$ (synthesis rate) 또는 $k_t$ (degradation rate)를 modulate.

[B.2] **Total body water 실제 수치 적용** (T p.46):

| 파라미터 | 정상 환경 | 사막 환경 |
|---|---|---|
| Pool size $A_{ss}$ | 42 L | 42 L (homeostasis 유지) |
| Turnover rate $R_t$ | 2.5 L/day | 21 L/day |
| Fractional turnover rate $k_t$ | 0.06 day⁻¹ (6%/day) | 0.5 day⁻¹ |
| Turnover time $t_t$ | 17 days | 2 days |

`[출처: Rowland & Tozer 5e, Ch.2, p.46]`

**핵심 통찰**: pool size는 같지만 turnover dynamics는 8배 빨라짐. *Turnover rate 단독*으로는 system의 *speed*를 표현 못 함 — fractional rate 또는 turnover time이 필요.

[B.3] **약물에 의한 turnover modulation 분류**:

1. **Synthesis 억제**: 약물이 $R_{\text{in}}$ 감소 → pool size 감소
   - 예: warfarin (응고인자 합성 감소; 응고인자별 t_t = 6h~3일이라 pool 감소에 시간 소요)
   - 예: simvastatin (cholesterol 합성 감소)
2. **Degradation 가속**: 약물이 $k_t$ 증가 → pool size 감소
   - 예: uricosuric agent (uric acid renal clearance 증가)
3. **Synthesis 가속**: 약물이 $R_{\text{in}}$ 증가 → pool size 증가
   - 예: epoetin alfa (RBC 생산 자극), filgrastim (WBC 생산 자극)
4. **Input 차단 (외부 source)**: 약물이 외부 input 감소
   - 예: ezetimibe (cholesterol 흡수 차단)

[B.4] **NONMEM `$DES` indirect response model template**:

```fortran
$MODEL  COMP=(CENT) COMP=(RESPONSE)
$PK
KIN  = THETA(1)         ; baseline synthesis rate
KOUT = THETA(2)         ; degradation rate constant
EC50 = THETA(3)
EMAX = THETA(4)
A_0(2) = KIN/KOUT       ; baseline pool at SS

$DES
CU  = A(1)/V            ; unbound conc proxy
INH = EMAX*CU/(EC50+CU) ; drug inhibition of synthesis
DADT(1) = -CL/V*A(1)
DADT(2) = KIN*(1-INH) - KOUT*A(2)
```

### C. Structural Necessity

**왜 pool size, turnover rate, fractional rate, turnover time *4개 모두* 필요한가?**

각 파라미터는 *서로 다른 임상 질문*에 답한다:

| 파라미터 | 답하는 질문 | 임상 사용 |
|---|---|---|
| $A_{ss}$ | "현재 얼마나 있는가?" | Lab value 해석 (e.g., serum cholesterol 200 mg/dL) |
| $R_t$ | "1일당 얼마나 만들어지는가?" | Replacement therapy dose 계산 (e.g., albumin synthesis 22 g/day) |
| $k_t$ | "얼마나 빠른 system인가?" | 약물 효과 지연 예측, washout 기간 |
| $t_t$ | "변화가 stabilize까지 얼마나?" | TDM 시 sampling 시점 결정 (~3-5 × $t_t$) |

수학적으로는 $R_t = k_t \cdot A_{ss}$, $t_t = 1/k_t$로 redundant하나, 임상 의사결정 *언어*로는 분리해서 사고해야 혼동 없음.

### D. Assumptions & Boundary Conditions

- **Steady state 가정의 시간 척도**: turnover time보다 짧은 시간 척도에서는 SS 가정 깨짐. Albumin t_t = 16일 → 1주일 측정으로 SS 판단 위험.
- **Single pool 가정**: 다구획 turnover (e.g., red blood cell — bone marrow precursor + circulating mature) 시 multi-compartment turnover 모델 필요. Paclitaxel-induced leukopenia (T Fig.1-7): WBC nadir까지 1주, 회복까지 3주 — bone marrow precursor의 turnover 시간 + maturation lag.
- **Linear elimination ($k_t$ 일정)**: 일부 endogenous substance는 saturable elimination → Michaelis-Menten 형태.
- **Pool size constancy**: feedback control 약한 substance는 pool size 변동 가능.

### E. Limitations

- **Disease progression** *[CONTEXT 흡수]*: 약물이 turnover 동역학을 modulate해도 underlying disease가 *natural history*로 진행하면, 약물 효과는 *시간 가변*. Prednisone in Duchenne (T Fig.2-13): 0.3 mg/kg에서 1개월, 0.75 mg/kg에서 3개월 후 자연 declination 복귀.
- **Placebo and baseline confound** *[CONTEXT 흡수]*: turnover-driven response 측정 시, placebo도 시간에 따라 변동(T Fig.2-12 montelukast study) → baseline 자체의 시간 가변성을 분리 불가능한 경우 흔함.
- **Endogenous compound의 PK 보정** *[CONTEXT 흡수]*: insulin, cortisol, thyroxin 등 endogenous compound 외부 투여 시 *baseline 농도 보정* 필수. 단순 plasma 농도 측정은 endogenous + exogenous 합.
- **Resistance / Tolerance / Sensitization**: long-term turnover 변화는 receptor up/down-regulation 동반 가능 → turnover model이 재구성 필요.

### F. Five Cognitive Layers

| 레이어 | 내용 |
|---|---|
| **L1 Formal** | $dA/dt = R_{in} - k_t A$ ODE; SS condition; $t_t = 1/k_t$ 도출 |
| **L2 Geometric** | Pool을 *욕조*로 시각화 — 수도꼭지(R_in) + 배수구(k_t × A). 두 파라미터 변화의 욕조 수위 trajectory |
| **L3 Structural Isomorphism** | Turnover ≅ first-order chemical reaction kinetics, ≅ RC circuit charging/discharging, ≅ economic stock-flow models |
| **L4 Physiological** | 모든 endogenous substance(hormone, plasma protein, blood cell, electrolyte)가 turnover system. Albumin t_t≈16일, RBC t_t≈40일, water t_t≈17일, clotting factor II t_t≈3일 |
| **L5 Practical** | Indirect response model NONMEM `$DES` 구조; baseline parametrization (KIN/KOUT vs Baseline·KOUT); steady state 도달까지 ~5 × t_t; warfarin 2–4일 지연을 K_out으로 모델링 |

### G. Zettelkasten Atom

```yaml
---
aliases: [Turnover, Indirect Response Foundation, kt, tt, Pool Size]
tags: [pharmacometrics/pd, modeling/turnover, indirect-response]
up: "[[PD Modeling MOC]]"
related: ["[[Indirect Response Model]]", "[[Disease Progression]]", "[[Endogenous Compound]]", "[[Steady State]]"]
source: "Rowland & Tozer 5e, Ch.2, Eq.2-5/2-6/2-7, p.45-46"
---

Pool size A_ss, turnover rate R_t, fractional rate k_t = R_t/A_ss,
turnover time t_t = 1/k_t. dA/dt = R_in - k_t·A is the ODE skeleton
of every indirect response model. 약물 modulation은 4가지 형태:
synthesis 억제(warfarin, statin), degradation 가속(uricosuric),
synthesis 가속(epoetin, filgrastim), input 차단(ezetimibe).
실측 anchor (total body water): A_ss=42L, R_t=2.5 L/day,
k_t=0.06 day⁻¹, t_t=17 days. 사막 환경 시 R_t→21 L/day,
k_t→0.5 day⁻¹, t_t→2 days (pool size 동일). 약물 효과 지연
(warfarin 2-4일, paclitaxel leukocyte 3주)은 turnover 개념 없이
설명 불가.
```

<!-- RECAP -->
**§2 Recap**: 4개 MUST 카드는 PK/PD 인식론의 **수직 계층**을 이룬다.
- M1 (Carousel) = *어떻게 모델링하는가* (방법론)
- M2 (PK/PD Linkage) = *왜 모델링하는가* (목적: dose→effect 번역)
- M3 (Hill Emax) = *PD를 수식으로 어떻게 인코딩하는가* (정량 어휘)
- M4 (Turnover) = *시간 지연이 있을 때 어떻게 인코딩하는가* (동역학 어휘)

이 4개 위에 28세션의 모든 NONMEM·PopPK 내용이 쌓인다.
<!-- /RECAP -->

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# §5 — Confusion Pair Dissection

<!-- CONFUSION -->

## Pair 1 ⚡ Critical Blow Applied — Pharmacokinetics vs Pharmacodynamics

| 비교 차원 | Pharmacokinetics (PK) | Pharmacodynamics (PD) |
|---|---|---|
| **표면적 유사성** | 둘 다 "pharmaco-"로 시작, 둘 다 약물 관련 정량 학문 — 신진 모델러는 둘을 *경쟁* 또는 *대립* 관계로 오인 | |
| **수식/코드 형태** | $dA/dt = R_{abs} - (R_{exc}+R_{met})$ ; concentration-time profile | $E = E_{\max} \cdot C^{\gamma} / (C_{50}^{\gamma} + C^{\gamma})$ ; concentration-effect relationship |
| **생리학적/구조적 지시체** | ADME 기관: GI tract, blood, liver, kidney — *body가 약물에 무엇을 하는가* | Receptor, enzyme, signal transduction, downstream physiology — *약물이 body에 무엇을 하는가* |
| **변화 방향** | Hepatic clearance가 감소하면 → AUC 증가, $C_{\max}$ 증가 | Receptor density가 감소하면 → $E_{\max}$ 감소, $C_{50}$ 영향 가능 |
| **임상/모델링 결과** | PK 변화를 PD 변화로 오인하면: 환자 PK variability(CYP2D6 polymorphism)를 receptor 민감도 차이로 잘못 해석 → 잘못된 dose individualization 전략 채택 | |
| **⚡ 기억 고리** | "PK는 *약물의 여행기*, PD는 *약물의 행동기*. 두 책을 합쳐야 *환자의 이야기*가 된다 — T Fig.1-3의 세 plot이 그 *합쳐짐*의 시각화다." | |
| **💀 치명적 타격 (Critical Blow)** | NDA 제출 dossier에서 PK section과 PD section을 별도 팀이 작성하고 통합 검토를 누락했을 때, FDA reviewer는 *exposure-response justification 부재*를 사유로 Deficiency Letter 발행. 이 경우 dose justification이 무너져 라벨에 권고된 dose가 *지지받지 못함* — 최악의 경우 dose recommendation을 변경하라는 요구로 launch 6–12개월 지연. 실제 historical 사례: 다수 약물의 dose-finding label change가 이 카테고리에 속함. | |

<!-- /CONFUSION -->

<!-- CONFUSION -->

## Pair 2 — Graded Response vs Quantal Response

| 비교 차원 | Graded Response | Quantal Response |
|---|---|---|
| **표면적 유사성** | 둘 다 *response*라 불리고, 둘 다 농도와 관계 가짐 — γ가 큰 graded response는 외형상 quantal과 거의 구분 불가 | |
| **수식/코드 형태** | Hill 식 (T Eq.2-4): individual 내 magnitude 연속 변화 | Cumulative frequency curve (T Fig.2-18): population 내 event 발생 *probability* |
| **생리학적/구조적 지시체** | 단일 환자의 EEG median frequency, 혈압, 통증 강도 — *연속 magnitude* | 부정맥 억제 yes/no, 사망 yes/no, 만족스러운 마취 yes/no — *threshold-crossing event* |
| **변화 방향** | 농도 증가 → magnitude 점진 증가 (Emax까지) | 농도 증가 → event 발생 확률 점진 증가 (100%까지) |
| **임상/모델링 결과** | Graded response를 quantal로 오해하여 binary endpoint(예/아니오)로 분석 → 정보 손실, 통계 검정력 감소; 반대로 quantal을 graded로 fitting하면 logistic/probit 대신 linear regression 사용으로 잘못된 confidence interval | |
| **⚡ 기억 고리** | "Graded는 *볼륨 노브*(연속 회전), Quantal은 *스위치*(on/off). γ→∞일 때 노브가 점점 스위치처럼 보일 뿐, 둘은 *측정 대상*의 구조가 다르다 — 환자 *내부*에서 magnitude를 보는가, 환자 *집단*에서 빈도를 보는가." | |

<!-- /CONFUSION -->

<!-- CONFUSION -->

## Pair 3 — Turnover Rate vs Fractional Turnover Rate

| 비교 차원 | Turnover Rate $R_t$ | Fractional Turnover Rate $k_t$ |
|---|---|---|
| **표면적 유사성** | 둘 다 "turnover rate"라 불리며 단위가 헷갈림 — 신진 모델러가 가장 자주 쓰는 표현 "albumin turnover rate" 자체가 모호 | |
| **수식/코드 형태** | $R_t$ [mass/time] (e.g., 2.5 L/day) | $k_t = R_t/A_{ss}$ [time⁻¹] (e.g., 0.06 day⁻¹) |
| **생리학적/구조적 지시체** | 절대량 flux — 단위 시간당 만들어지는 (또는 사라지는) 양 | 시스템의 *내재적 속도* — pool size 대비 흐름의 비율 |
| **변화 방향** | 사막 환경 → water $R_t$ 8배 증가 (2.5 → 21 L/day) | 사막 환경 → water $k_t$ 8배 증가 (0.06 → 0.5 day⁻¹). $A_{ss}$가 일정해서 둘 다 같은 비율로 변하나, 일반적으로는 다르게 변할 수 있음 |
| **임상/모델링 결과** | Replacement therapy dose는 $R_t$로 결정 (e.g., albumin 22 g/day 합성 → IV 보충 시 이 량 기준). $k_t$로 잘못 계산하면 dose가 단위 매칭 안 되어 *수십 배 오차* 가능 | |
| **⚡ 기억 고리** | "$R_t$는 *얼마나 흐르는가*(L/day), $k_t$는 *얼마나 빠른가*(day⁻¹). 강 너비(L/day)와 강 유속(km/h)을 헷갈리면 안 된다 — 너비가 같아도 유속은 다를 수 있고, 그 반대도 가능. *느린 system은 변화에 시간이 걸리고, 빠른 system은 즉각 반응한다*는 통찰은 $k_t$에서 나온다." | |

<!-- /CONFUSION -->

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# §7 — Self-Test: Active Recall Module

<!-- SELF-TEST -->

**Q1 [★★ 회상]**: G Ch.1의 Modeling Carousel 6단계를 순서대로 나열하고, 각 단계가 다음 단계에 *무엇을 입력으로 제공*하는지 1줄로 답하라.

<details>
<summary>정답 공개</summary>

1. Tentative model → Design에 *모델 구조 가설* 제공
2. Design → Run experiment에 *sampling time, dose level, population* 제공
3. Run experiment → Explore data에 *raw observations* 제공
4. Explore data (EDA) → Fit model에 ***initial estimates와 모델 구조 suggestion*** 제공 ← 가장 critical link
5. Fit model → Analyze output에 *parameter estimates와 precision* 제공
6. Analyze output → Tentative model로 (refined hypothesis) 또는 Design으로 (additional study) 또는 Fit으로 (alternative model) 순환

**다음 깊이 질문**: Step 4(EDA)가 Step 5(Fit)에 initial estimates를 제공한다는 사실에서, EDA를 건너뛸 때 발생하는 algorithmic 결과는 무엇인가?
</details>

---

**Q2 [★★ 회상]**: G p.4의 5대 dysfunction을 모두 나열하라.

<details>
<summary>정답 공개</summary>

1. Failure to appreciate the value of exploratory data analysis prior to any fitting (EDA 무시)
2. Slavery to formulas (수식 노예화)
3. Too much trust in modeling software (소프트웨어 맹신)
4. Improper use of weighting (부적절한 weighting)
5. Lack of a 'holistic' view of the process (전체적 시각 결여)

**다음 깊이 질문**: 이 5개 중 가장 빈번한 것은 #1이라고 G가 명시했다. 왜 EDA가 가장 자주 누락되는가?
</details>

---

**Q3 [★ 회상]**: Hill 방정식 $E = E_{\max} \cdot C^{\gamma} / (C_{50}^{\gamma} + C^{\gamma})$에서 γ=1과 γ=2일 때, 효과가 20%에서 80%로 변하는 농도 범위의 비율을 각각 계산하라.

<details>
<summary>정답 공개</summary>

γ=1: $C_{20\%} = 0.25 \cdot C_{50}$, $C_{80\%} = 4 \cdot C_{50}$ → 비율 16배
γ=2: $C_{20\%} = 0.5 \cdot C_{50}$, $C_{80\%} = 2 \cdot C_{50}$ → 비율 4배

도출 (γ=1 경우): $0.2 = C/(C_{50}+C) \Rightarrow C = 0.25 C_{50}$; $0.8 = C/(C_{50}+C) \Rightarrow C = 4 C_{50}$.

**다음 깊이 질문**: γ가 매우 클 때 graded response는 quantal과 어떻게 구별되는가? 또는 사실상 구별 불가능한가?
</details>

---

**Q4 [★★ 적용 — Warfarin 시나리오]**: 환자에게 warfarin 1.5 mg/kg single oral dose 투여 후, 12시간째 측정한 prothrombin activity reduction이 20%에 불과하다. 임상의는 "효과 부족이니 같은 용량을 한 번 더 투여하자"고 제안한다. 당신은 pharmacometrician으로서 이 결정에 어떻게 응답하는가?

<details>
<summary>정답 공개</summary>

**거부해야 한다**. T Fig.1-6 (Nagashima et al. 1969, 5 male volunteers, oral 1.5 mg/kg sodium warfarin) — peak effect는 *2일 후*에 도달하며, 12시간째 20% reduction은 정상적 진행 과정이다. 추가 dose 투여 시 2–3일째에 누적 효과로 *internal hemorrhage* 위험.

근본 이유: warfarin의 효과 지연은 PK 분포 지연이 아닌 ***응고인자의 turnover*** — warfarin이 vitamin K-dependent clotting factor 합성을 억제해도, 기존 pool은 자연 degradation rate ($k_t$)에 따라 점진적 감소. 응고인자별 $t_t$는 6시간~3일.

**임상의에게 권고**: 추가 dose 보류, 2일째 prothrombin time 재측정 후 결정. 만약 2일째에도 부족하면 그때 증량.

**다음 깊이 질문**: 이 시나리오를 NONMEM에서 모델링하려면 어떤 구조가 필요한가? (Direct effect Hill 모델로 충분한가, indirect response model이 필요한가?)
</details>

---

**Q5 [★ 적용 — Local Minimum 시나리오]**: 박사 1년차 학생이 1구획 IV bolus 모델을 NONMEM으로 fitting했다. `$ESTIMATION` 결과 OFV = 1247.3, $COV step 통과, GOF plot 무난. 학생은 "성공"이라 판단한다. 당신이 supervisor로서 이 결과를 검토할 때, 학생에게 *반드시* 시킬 진단 절차는 무엇인가?

<details>
<summary>정답 공개</summary>

**Initial estimate sensitivity test**: $ESTIMATION을 *서로 다른 4개 이상의 initial estimates*로 재실행. 각 run의 OFV를 비교.

- 모두 OFV = 1247.3 ± 1.0 → global minimum 신뢰 (단, EDA 검증 별도 필요)
- OFV가 1247, 1289, 1305 등 *서로 다른 값*으로 수렴 → ***local minimum 의심***. 가장 낮은 OFV가 global minimum 후보지만, 더 다양한 initial estimates 시도 필요.

추가로:
- EDA plot (concentration-time on linear and log scale, dose-normalized) 검토 — exponential decay인지 visual 확인
- Different fitting algorithm 시도 (FOCE → Laplace, ITS, SAEM)
- 가능하면 graphical 또는 NCA 기반 *parameter prior knowledge* 와 비교

**근거**: G p.6 — *"To ensure that a program has not converged to a local minimum, we suggest rerunning the program with different initial estimates"*; G Fig.1.2 parameter space의 multi-hollow OFV landscape. $COV step 통과는 *local* 신뢰성만 보장 (Hessian이 local에서 양정치이면 됨).

**다음 깊이 질문**: $COV step 통과가 global minimum을 보장하지 않는 이유를 mathematical하게 설명하면? (Hessian의 local vs global property)
</details>

---

**Q6 [○ 회상]**: T 정의에 따라 *clinical response*, *surrogate endpoint*, *biomarker*, *safety biomarker*를 구별하라. 각 카테고리의 예시 1개씩.

<details>
<summary>정답 공개</summary>

- **Clinical response**: 환자에게 직접 의미 있는 결과. 예: 5년 생존율, 통증 감소, stroke prevention.
- **Surrogate endpoint**: clinical response를 *예측하는 것으로 validated*된 측정. 예: 혈압 강하 (cardiovascular morbidity 예측, 다수 long-term study로 validated).
- **Biomarker**: 약물 효과의 측정이지만 surrogate로 validated되지 않은 것. 예: tumor size 감소, EEG median frequency, PET receptor binding.
- **Safety biomarker**: 약물 일반 안전성 모니터링용. 예: liver function test (ALT, AST), white blood cell count, ESR, fecal blood loss.

**핵심 위계**: biomarker ⊃ surrogate endpoint (validated subset) ⊃ clinical response와 직접 등가.

**다음 깊이 질문**: Tumor size 감소는 항상 survival benefit으로 이어지는가? 만약 그렇지 않다면 surrogate vs biomarker 구분의 임상적 의미는?
</details>

---

**Q7 [★ 적용 — Turnover 계산]**: Albumin pool size는 350 g, turnover time은 16일이다. 다음을 계산하라:
(a) Daily turnover rate $R_t$
(b) Fractional turnover rate $k_t$
(c) Severe burn 환자에서 $R_t$가 정상의 2배로 증가하면, pool size를 정상 350 g으로 유지하기 위해 필요한 IV albumin replacement dose (단, $k_t$는 변화 없다 가정)

<details>
<summary>정답 공개</summary>

(a) $R_t = A_{ss} / t_t = 350 / 16 ≈ 21.9$ g/day
(b) $k_t = 1/t_t = 1/16 = 0.0625$ day⁻¹ (≈ 6.25%/day)
(c) $R_t^{\text{burn}} = 2 \cdot 21.9 = 43.8$ g/day. Endogenous synthesis가 정상이라면 차액 $43.8 - 21.9 = 21.9$ g/day를 IV로 보충. (단, 실제 burn 환자는 capillary leak으로 albumin 분포도 변하므로 단순 turnover 모델 한계 있음.)

**다음 깊이 질문**: $k_t$ 단독으로 sample timing을 결정한다면 ($\sim 5 t_t$ for SS), albumin replacement dose 변화의 *최종 효과*를 평가하는 데 며칠이 필요한가? 80일 ($5 \times 16$).
</details>

---

**Q8 [★ 적용 — Stereoisomer 시나리오]**: 어떤 신약 X는 racemic mixture로 개발 중이다. R-isomer와 S-isomer가 동일 PD target에 작용하지만, $E_{\max}$가 R: 30%, S: 80%이고, $C_{50}$도 다르다. 임상시험에서 racemate 농도만 측정하는 assay를 사용하여 dose-response를 fitting했더니 γ ≈ 0.6의 shallow curve가 나왔다. 당신은 이 결과를 어떻게 해석하는가?

<details>
<summary>정답 공개</summary>

**γ=0.6 자체가 다중 receptor population 또는 *isomer mixture artifact*의 신호**.

해석: racemate 측정은 R + S 합산 농도. 두 isomer가 *서로 다른 PD parameter*를 가질 때 각각의 sigmoidal curve가 합쳐지면, 외형상 *shallow*해진 단일 curve로 보임 (γ가 1보다 작아짐).

**조치**:
1. **Stereospecific assay 도입** (T p.24, S-naproxen·tamsulosin precedent)
2. R-isomer와 S-isomer 별도 PK/PD modeling
3. 만약 R-isomer가 임상적으로 의미 없는 활성이라면 single enantiomer 개발 검토 (acenocoumarol·methylphenidate precedent)

**Regulatory implication**: 현재 데이터로 dose-response 도출 시 γ=0.6 모델은 *isomer mixture artifact*를 받아들인 것 — true mechanism 반영 안 됨. NDA submission 시 deficiency 사유 가능.

**다음 깊이 질문**: methylphenidate Fig.2-2B에서 (-)-isomer가 (+)-isomer 대비 노출이 미미한 이유는 무엇인가? (T 텍스트 hint: first-pass metabolism으로는 설명 안 됨)
</details>

---

**Q9 [★★ Boss Dilemma — Socratic Dilemma]**: 

**시나리오**: 당신은 새 약물 X의 Phase 2b 데이터를 받았다. PI는 내일 오전 9시에 dose-response 분석 결과를 발표해야 하며, 그 결과를 바탕으로 Phase 3 dose가 결정된다. 시간은 18시간 남았다. 데이터셋은 280명, 4개 dose level, dense PK/PD sampling. 두 가지 워크플로 옵션이 있다:

- **옵션 A (EDA-First)**: G Modeling Carousel 충실 — 먼저 6시간 EDA(dose-normalized concentration plot, individual time profile, exposure-response scatter, hysteresis check), 그 후 NONMEM fitting + GOF + sensitivity analysis. 총 18시간 빠듯하게 소진.

- **옵션 B (Fit-First)**: NONMEM에 곧바로 control stream 던지기 → 2시간 내 첫 fit 결과, 나머지 16시간을 model refinement·sensitivity·simulation에 활용. EDA는 fitting 후 confirmation 용으로 1시간만.

**당신은 어느 쪽을 선택하는가? 그리고 이 결정을 내일 회의에서, 또는 추후 regulatory submission에서 어떻게 *방어*하는가?**

<details>
<summary>수석 모델러의 Trade-off 논리 공개</summary>

**핵심 통찰**: 이 딜레마의 답은 단순한 정답이 아니라 ***두 옵션이 어떤 위험을 trade하는지를 명시하고, 그 trade를 의식적으로 결정한 흔적을 남기는 것***이다.

**옵션 A 선택 시의 방어 논리**:
- *내일 9시에 가져갈 결과는 아마 simpler한 모델이지만, EDA가 검증한 모델이므로 ***local minimum 위험이 통제됨***. Phase 3 dose 결정에 들어갈 약 *수백억 원의 의사결정*이 local minimum에 의해 왜곡되는 위험을 피한다.*
- Regulatory submission 시: *"We followed Carousel methodology with EDA-driven initial estimates, ensuring global minimum convergence"* — FDA/EMA reviewer가 이의 제기 못 함.
- *Risk*: 시간 부족으로 model refinement(예: covariate model, IIV/IOV 분리)가 불충분할 수 있음.

**옵션 B 선택 시의 방어 논리**:
- *Refined model을 가져갈 수 있어 covariate effect, prediction precision 개선. Phase 3 design (subgroup dose adjustment)에 더 informative.*
- Regulatory submission 시: *문제 발생*. EDA 부재가 documentation에서 드러나면 reviewer가 *"How were initial estimates obtained?"*라고 물을 수 있고, 답이 unsatisfactory면 deficiency.
- *Risk*: local minimum convergence 가능성. 보이지 않는 OFV 차이로 Phase 3 dose가 *체계적으로 잘못* 추천될 수 있음 — 발견은 *Phase 3 실패 후*에야.

**수석 모델러의 결정** (B-Standard 회의실 답):
> ***옵션 A를 선택하되, EDA를 6시간이 아닌 3시간으로 압축한다.*** Dose-normalized concentration plot, exposure-AUC plot, response-concentration scatter — 이 세 가지만으로도 initial estimates를 *graphical하게* 추출할 수 있다 (G p.5 권고). 나머지 15시간을 fitting + sensitivity에 사용. 회의 발표에는 EDA plot 1–2장을 *반드시 포함* — *"This is the basis of our model selection"* 한 줄을 추가.
>
> 만약 PI가 옵션 B를 강요한다면, *"옵션 B로 진행하되, fitting 후 *반드시* multi-initial-estimate sensitivity test를 시행하여 local minimum 위험을 사후적으로 검증해야 한다"*고 명시한다. 이것은 G의 권고와도 일치한다 (p.6).

**Regulatory level**: 두 옵션 모두 *합리적*이다. 결정 자체보다 ***결정의 documentation***이 중요. *"We considered both EDA-first and fit-first approaches; we chose [X] because [Y]; we mitigated [risk] by [Z]"* — 이 한 단락이 deficiency letter 방어의 핵심.

**다음 깊이 질문**: Phase 3 dose 결정이 *환자 안전*과 *상업적 timeline* 사이의 trade-off라면, modeler의 윤리적 의무는 어디에 있는가?
</details>

<!-- /SELF-TEST -->

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# §8 — Meta-Frame & Big Picture

## A. Positioning

이 세션은 28세션 PK/PD Mastery 커리큘럼의 ***인식론적 진입점***이다.

- **이전에 온 것**: 없음 (커리큘럼 시작점).
- **바로 다음에 오는 것**: 1구획·다구획 모델 (M2의 Distribution 구체화), Clearance / Vd 체계 (M2의 Elimination + ADME 정량화), Direct-effect PD model (M3 Hill의 PK/PD 통합), Indirect Response model (M4 Turnover의 ODE 구체화).
- **이 기반에 결정적으로 의존하는 고급 도메인**:
  - **PopPK (NONMEM IIV/RUV)**: M1 Carousel의 *EDA-driven covariate identification*이 IIV 모델 선택의 토대.
  - **TMDD (Target-Mediated Drug Disposition)**: M3 Hill + M4 Turnover의 결합 — receptor binding (Hill) + receptor turnover (Indirect Response)의 hybrid.
  - **PBPK (Physiologically-Based PK)**: M2 ADME chain의 organ-level decomposition.
  - **QSP (Quantitative Systems Pharmacology)**: M4 Turnover의 multi-pool network 확장.
  - **Disease progression modeling**: M4 Turnover + 시간 가변 baseline.

## B. Dependencies — 이 세션을 대충 넘겼을 때 발생하는 구체적 실패 모드

**실패 모드 1: PopPK Covariate Modeling 단계에서의 *spurious correlation* 채택**

원인 chain:
- M1 Carousel의 EDA-First 철학 미체화
- → covariate-parameter 관계를 visual screening 없이 stepwise covariate addition만으로 결정
- → small dataset에서 *type I error 누적* (e.g., body weight ~ CL이 sample-specific artifact)
- → 모델이 새 데이터셋에서 fail
- → external validation step에서 발견되면 다행, 아니면 NDA submission까지 잘못된 covariate로 진행
- → FDA가 reviewer analysis로 covariate effect re-test → significance disappear → ***Deficiency Letter***

**실패 모드 2: Indirect Response Model fitting에서의 *kt와 Rt 혼동에 의한 dose 단위 오류*** (실제 박사 1년차 빈번 사례)

원인 chain:
- M4 Turnover의 4-parameter 분리 미체화
- → indirect response NONMEM control stream 작성 시 `KIN`과 `KOUT` parametrization 혼동 — `BASELINE = KIN/KOUT`인데 `KIN`을 fractional rate인 양 estimate
- → THETA initial estimates가 단위 mismatch (KIN을 0.06으로 입력해야 하는데 2.5로 입력 등)
- → `$ESTIMATION` 즉시 발산 또는 nonsensical baseline 추정
- → 학생이 며칠을 디버깅에 소모
- → 또는 더 나쁘게, 우연히 수렴한 모델로 simulation 수행 → dose recommendation이 *physiological scale에서 벗어남*

## C. Professional Moat — 이 세션 내용에 직접 답함

*Vol I 프레임 적용*:

**"NONMEM을 실행하고 GOF 플롯을 생성할 수 있는 주니어 모델러와, 2구획 모델을 데이터에 적합시킬 수 있는 AI가 이미 존재한다. 이 세션의 원리를 — 메커니즘이 아닌 구조적 이해의 수준에서 — 진정으로 내면화한 연구자는 그 둘 중 어느 것도 복제할 수 없는 무엇을 갖고 있는가?"**

답:

이 세션을 체화한 모델러는 ***"왜 이 결과가 의심스러운가"***를 데이터 한 줄을 보고 판단할 수 있다. 구체적으로:

1. **새 dataset 첫 30초**: dose-normalized AUC plot을 머릿속에 즉시 그릴 수 있고, 비선형성 여부를 *fitting 전에* 판단. 주니어와 AI는 이 "30초 EDA"를 *재현 가능한 procedure로* 보유하지 않는다.

2. **NONMEM 출력 첫 5분**: OFV, condition number, $COV step status를 보고 *수렴이 trustworthy한가*를 판단 — 그러나 trustworthy의 기준이 단순한 numerical threshold가 아니라 *Carousel의 어느 지점이 부실한가*에 대한 인과 추적이다. AI는 numerical threshold만 안다.

3. **PI가 "dose 추천을 50% 올리자"고 제안할 때**: 이 추천이 PK variability(M2) 때문인지, PD ceiling 도달(M3 Emax) 때문인지, turnover dynamics(M4)의 시간 미반영 때문인지를 *분리*하여 회의실에서 immediately push back할 수 있다. 주니어는 어느 한 가지 framework로만 사고하고, AI는 이 분리 자체를 수행하지 못한다.

4. **Regulatory submission 작성 시**: deficiency letter를 받지 않을 *defensive documentation*을 — 즉, "어떤 alternative model을 고려했고, 왜 reject했고, 어떤 sensitivity가 robust한지"를 — Carousel 6단계 framework에 정확히 매핑하여 작성. 이 mapping은 AI가 구조적으로 못 한다 (reasoning chain의 길이가 한정적이며, 자기 자신의 model selection을 *epistemological하게 평가*하지 못함).

요약하자면, **이 세션의 4개 MUST는 *비판적 사고의 hook 시스템***이다 — 데이터·모델·결과를 만났을 때 어디에 *의심을 걸어둘 것인가*의 grid. 이 grid가 없는 모델러는 *어떤 모델도* 진정으로 평가할 수 없으며, 어떤 AI도 이 grid 자체를 *autonomously* 갖지 못한다 (학습된 imitation은 grid의 form은 가지나 *epistemological commitment*는 못 가진다).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
---
✦ STEP 1 완료.

다음이 준비되었습니다:
  • §1 세션 헤더 & 로드맵
  • §2 개념 해부 카드 (4개 개념: M1 Modeling Carousel, M2 PK/PD Linkage,
                      M3 Hill Emax, M4 Turnover; Apex: M1 Modeling Carousel)
  • §5 혼동 쌍 해부 (3개 쌍, Critical Blow 적용: PK vs PD)
  • §7 자기 테스트 (9개 질문, 보스 딜레마 포함 — Q9 Phase 2b 18시간 dilemma)
  • §8 메타프레임 & 빅 픽처
  • 감지된 소스 유형: 혼합 (Vol I — Gabrielsson Ch.1 방법론 축 + Rowland & Tozer Ch.1-2 임상정량 축)
  • Data Anchoring 소스: warfarin 1.5 mg/kg oral, 5 male volunteers (Nagashima 1969);
    paclitaxel single i.v. dose, leukocyte recovery 3주 (Minami 1998);
    propranolol γ≈1, C50=5.3 µg/L unbound (Lalonde 1987);
    ketamine S(+) Emax≈90% C50=0.7 mg/L vs R(-) Emax≈42% C50=1.8 mg/L
    (Schuttler 1985); alfentanil quantal C50 breast 0.27/lower abd 0.31/upper abd
    0.42 mg/L (Ausems 1986); total body water A_ss=42L R_t=2.5 L/day k_t=0.06 day⁻¹
    t_t=17 days (T p.46); methylphenidate (+)>>(-) racemate 30 mg oral (Aoyama 1993);
    acenocoumarol R-(+) vs S-(-) 20 mg racemate (Gill 1988); montelukast 10 mg
    placebo-controlled FEV1 (Dockhorn 2000); prednisone 0.3/0.75 mg/kg in
    Duchenne dystrophy (Griggs 1991); moxifloxacin 400 mg M. tuberculosis
    resistance emergence d18 (Heinrichs 2019).

"계속"을 입력하면 Step 2 HTML 컴파일러가 실행됩니다.
Step 2는 위 내용 전체(§1·§2·§5·§7·§8) +
§3(구조적 동형성 지도) + §4(인터랙티브 시뮬레이터 + Assumption Collapse 토글) +
§6(실용 시나리오 & 진단 병리)를 단일 완성 HTML 파일로 통합합니다.

— 다만 본 워크플로우(Unified v3.3.2)에 따르면 다음 단계는 Step 2 직접 진행이 아닌
   Phase 2 (Source Fidelity Audit)이며, 이를 통해 Step 1 Draft v0가 검증된 후
   Phase 3 (Insight Crucible) → Phase 4A/4B/4C → Phase 5 (HTML Compile)로 진행됩니다.
   "계속" 입력 시 즉시 Step 2 HTML 생성을 원하시면 그렇게 하되,
   v3.3.2 워크플로우 충실 진행을 원하시면 이 Draft v0를 Phase 2 Auditor 세션
   (Gemini Pro 등)으로 가져가시면 됩니다.
---
```

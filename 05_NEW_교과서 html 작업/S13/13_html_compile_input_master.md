# 13_HTML Compile Input Master

**Target filename**: `13_html_compile_input_master.md`  
**Session**: 13 — 개체 간 변이(IIV/BSV)와 공변량 모델링  
**Assembly mode**: PATCH MODE  
**Purpose**: Phase 4D learner-complete, mastery-enriched, HTML-ready master input for Phase 5 compilation.  
**Restriction**: This file does not generate HTML, Mermaid code, SVG code, or textbook figure images.

## Phase 4D Certification

| Certificate | Status | Basis |
|---|---|---|
| Learner-Standalone Certificate | PASS | PART A contains only learner-facing navigation plus the spliced scientific body and bounded mastery notes; audit/compiler material is isolated in PART B. |
| Zero-Omission Certificate | PASS | Scope Lock required source range, four MUST cards, PK50 anchors, Audit corrections, Crucible-adopted insights, and Phase 4C KEEP figure markers were cross-checked. |
| Mastery-Uplift Certificate | PASS | Four bounded augmentation notes were inserted adjacent to C1–C4; each is labeled by epistemic status and adds no new numerical values, drugs, equations, page tags, or external claims. |
| Source-Boundary Certificate | PASS | Textbook-derived body is preserved; expert/crucible/audit-derived notes are labeled and not presented as textbook claims. |
| HTML-Readiness Certificate | PASS | PART B contains Prompt 5 rendering rules, marker mapping, figure rules, source-tag rules, navigation-anchor rules, audit guardrails, and splice verification. |

## Assembly Mode

**PATCH MODE** — `13_Content_Lock_v2.1(1).md` is a Figure Marker Insertion Patch, not a full marked body. Approved markers F2, F3, F6, and F8 were spliced into the learner scientific body from `13_Content_Lock_v2(3).md` using exact heading anchors. All anchors matched exactly once.

## Input Manifest

| File | Role | Authority level | Used for | Notes |
|---|---|---|---|---|
| 13_scope_lock(3).md | scope boundary | A0 | Defines source range, learner, image rights, hard boundaries, required anchors. | Used. |
| 013_G_개체간 변이 IIV·BSV·공변량(4).pdf | PDF verification source | A1 | G&W Ch.4 p.333–352 and PK50 p.704–710 verification. | Used for source/page/figure anchor verification. |
| 013_T_개체간 변이 IIV·BSV·공변량(4).pdf | PDF verification source | A1 | R&T Ch.12–13 p.361–410 verification. | Used for source/page/figure anchor verification. |
| 13_Audit_Report_v1(3).md | audit guardrail | A2 | MUST_FIX/SHOULD_FIX, coverage, figure/page/source-boundary regression prevention. | Used. |
| 13_Content_Lock_v2(3).md | canonical body | A3 | Primary text-final body before figure marker insertion. | Used; process tables excluded from PART A. |
| 13_Content_Lock_v2.1(1).md | figure insertion source | A4 | PATCH MODE Figure Strategy and Insertion Map. | Used; F2/F3/F6/F8 retained. |
| 13_Crucible_Report_v1(1).md | crucible guardrail | A5 | Grade A insight preservation and mastery-intuition source. | Used only for labeled augmentation/guardrails. |
| 13_step1_draft_v0(3).md | deprecated source | A6 | Regression check only; not copied into learner body. | Not used as direct learner-body source. |
| S13_phase1_patch memo(2).md | patch memo / locked reference | A6 support | Attention guide for Phase 1 weaknesses and PK50 anchor. | Used as guardrail only. |
| 붙여넣은 마크다운(2)(62).md | compiler instruction | A7 | Prompt 5 / HTML rendering rules. | Used in PART B. |
| 붙여넣은 텍스트 (1)(87).txt | Phase 4D assembler instruction | Process instruction | Defines 4D output format, certificates, gates, augmentation budget. | Used to structure this file; not rendered as learner content. |
| 13_Content_Lock_v1(2).md | locked reference | Lower than v2 | Prior content lock version. | Not used except as lineage reference. |

## PART A — Learner-Facing Complete Handout

## Learner Navigation Aid

**How to use this handout**

1. Read §1 once to fix the map: C1 is the variance taxonomy; C2 protects the residual model; C3 separates covariate modeling from reparameterization; C4 asks whether smooth IIV hides subgroup structure.
2. Study §2 card-by-card. Stop at every `FIGURE_POINTER` and inspect the specified textbook figure manually; the original textbook image is not embedded because image rights are not available.
3. Use §5 to test whether the main confusions have been separated.
4. Answer §7 before rereading §8.

**Learning route**

| Step | Section | Purpose |
|---:|---|---|
| 1 | §1 Session Header & Roadmap | Fix the overall variance-axis map. |
| 2 | §2 C1 | Separate θ, η, ε / ω², σ². |
| 3 | §2 C2 | Decide the residual error structure before covariate interpretation. |
| 4 | §2 C3 | Separate true covariate explanation from total/unbound coordinate change. |
| 5 | §2 C4 | Recognize discontinuous genetic substructure inside apparent IIV. |
| 6 | §5 | Resolve confusion pairs. |
| 7 | §7–§8 | Self-test and integrate into the PopPK curriculum architecture. |

**Before you start**

- Recall the meaning of CL, V, t½, protein binding, NCA summaries, and basic NONMEM control-stream notation.
- Keep one question in mind: is the observed variability PK, PD, η, ε, covariate-explainable, or subgroup/distributional?

**After you finish**

- You should be able to explain why θ alone is insufficient.
- You should be able to explain why a residual error misspecification can create false IIV or false covariate signals.
- You should be able to explain why PK50 is a coordinate/reparameterization lesson, not a simple “fu reduced ω²” lesson.
- You should be able to explain why a bimodal concentration or η distribution should not be hidden under one smooth log-normal IIV term.

---

# Session 13 — 개체 간 변이(IIV/BSV)와 공변량 모델링

**Source lock**: R&T 5e Ch.12–13 (p.361–410); G&W 5e Ch.4 (p.333–352) + PK50 (p.704–710)  
**Learner-facing scope**: §1 → §2 → §5 → §7 → §8  
**Figure note**: 교과서 원그림은 삽입하지 않고, 승인된 figure pointer 또는 새 schematic brief만 사용한다.

---

## §1 — Session Header & Roadmap

**Session 13 — 개체 간 변이 (IIV / BSV)와 공변량 모델링**  
*Source: R&T 5e Ch.12 (p.361–392) + Ch.13 (p.393–410); G&W 5e Ch.4 일부 (p.333–352) + PK50 (p.704–710)*

<!-- MASTER LENS -->
### Big Idea

<!-- ANNOTATION -->NONMEM mixed-effects model(← fixed/random effects를 함께 추정)의 본질은 관측값을 **θ(인구 평균), η(개체 deviation), ε(잔차 noise)** 로 나누어 보는 데 있다. 그다음 각 흔들림의 크기인 **ω²와 σ²** 를 따로 추정한다. 공변량은 ω² 안에 섞여 있던 생리학적 원인을 꺼내는 도구이고, 유전 다형성은 매끄러워 보이는 ω² 안에 숨어 있는 불연속 봉우리다. `[R&T p.369–373; p.393–410]`

G&W는 이론보다 먼저 데이터의 모양을 보라고 한다. 따라서 공변량 모델은 control stream에서 바로 시작하지 않는다. 먼저 spaghetti plot·dose-normalized plot·transformed plot에서 “어떤 개체들이 왜 갈라지는가”를 확인해야 한다. `[G&W p.334–336]`

### Roadmap

```text
C1. θ / η / ε taxonomy
     ↓
C2. residual error model: ε의 형태를 정한다
     ↓
C3. covariate model: ω² 일부를 설명 가능한 생리학으로 옮긴다
     ↓
C4. genetic polymorphism: ω² 안의 불연속 substructure를 드러낸다
```

### Knowledge Graph Position

| 위치 | 내용 |
|---|---|
| 선행 전제 | 1-·2-compartment model, Cl/V/t½, protein binding, NONMEM 기초 syntax |
| 본 세션 | IIV/IOV/RUV, θ/η/ε, ω²/σ², covariate, genotype/phenotype variability |
| 직후 후속 | FOCE/FOCE-I, GOF/CWRES/η-EBE, shrinkage, stepwise covariate selection |
| 임상 번역 | Bayesian TDM, dose individualization, therapeutic window, PopPK report consistency |

<!-- RECAP -->
**§1 recap**: 이 세션의 질문은 “사람마다 다르다”가 아니다. 질문은 “그 다름 중 무엇이 θ, 무엇이 η, 무엇이 ε, 무엇이 covariate인가”이다.

---

## §2 — Concept Anatomy Cards

---

### C1. 변이의 구조적 분해 — θ, η, ε taxonomy

<!-- MASTER LENS -->
**개념 Big Idea**

θ는 인구의 무게중심이다. η는 각 개인이 그 중심에서 벗어난 정도이고, ε는 같은 개인을 같은 조건에서 다시 측정해도 남는 잔차다. 이 세 자리가 분리되지 않으면 `$OMEGA`와 `$SIGMA`는 숫자는 있어도 의미가 없다. `[R&T p.369–373]`

#### A. Formal Definition

`[교과서 외 구현/통계 번역; 개념 근거: R&T p.369–373]`

$$
Y_{ij}=f(\boldsymbol{\theta},\boldsymbol{\eta_i},x_{ij})+g(\boldsymbol{\theta},\boldsymbol{\eta_i},x_{ij})\varepsilon_{ij}
$$

- **θ**: fixed effect, population typical value.
- **ηᵢ**: interindividual deviation; variance-covariance matrix가 **Ω**, diagonal element가 **ω²**.
- **εᵢⱼ**: residual deviation; variance가 **Σ/σ²**.

<!-- ANNOTATION -->여기서 Ω/ω²는 개인 간 변이의 크기이고, Σ/σ²는 관측 잔차의 크기다. 두 값은 서로 다른 “오차”가 아니라 서로 다른 level의 variability를 가리킨다.

개인 clearance의 source-anchored exponential IIV:

$$
CL_i = CL\cdot \exp(\eta_i)
$$

R&T는 exponential error model이 CL을 음수로 만들지 않고 approximate constant CV를 제공하기 때문에 population analysis에서 자주 쓰인다고 설명한다. `[R&T p.371]` 작은 ω에서는 `CV(%) ≈ ω × 100`을 교육용 근사로 쓸 수 있다.

#### B. Data Anchor: 평균보다 분포가 먼저다

R&T는 warfarin 200명에서 유사한 anticoagulation을 얻기 위한 daily dose가 넓게 분포한다고 제시한다. 또한 nortriptyline 25 mg tid를 복용한 263명에서 plateau concentration은 linear scale에서는 skewed이고, log scale에서는 거의 symmetric하다. 즉, 평균만 보면 dose individualization의 문제는 해결되는 것이 아니라 가려진다. `[R&T p.362–363]`

G&W는 다중 피험자 자료에서 먼저 개별 profile과 pooled data를 그려 보라고 한다. Figure 4.2의 spaghetti plot은 같은 dose를 받은 Japanese와 Caucasian group이 서로 다른 exposure profile을 보일 수 있음을 보여 주며, 저자들은 mean curve with error bars보다 spaghetti plot이 variability를 더 잘 드러낸다고 설명한다. `[G&W p.335–336]`

<!-- ANCHOR -->
**NAD/NPD/population bridge**: Naive Averaged Data(NAD)는 각 time point의 평균 농도에 모델을 맞춘다. Naive Pooled Data(NPD)는 모든 관측값을 한 개인의 자료처럼 적합한다. G&W는 mean data fitting이 편향된 parameter와 variability를 만들 수 있어 피해야 하며, 대안으로 population approach가 필요하다고 설명한다. `[G&W p.335–336]`

#### C. Structural Necessity

1. **θ alone is not enough**: 평균 clearance만 있으면 “일반 환자”의 농도는 예측하지만, narrow therapeutic window에서 독성 또는 무효 노출을 겪을 개인을 설명하지 못한다. `[R&T p.370]`
2. **ω² and σ² compete for the same unexplained variability**: 잔차 모델이 설명하지 못한 분산은 ω²로 샌다. 반대로 개인 간 변이를 너무 크게 허용하면 σ²가 작아 보일 수 있다. 이 보존 법칙을 보지 못하면 C2의 residual model과 C3의 covariate model은 모두 흔들린다.
3. **Population analysis is simultaneous**: R&T는 standard two-stage가 rich sampling을 요구하는 반면, population analysis는 sparse data를 합쳐 structural parameter와 variance parameter를 동시에 최적화한다고 설명한다. `[R&T p.369]`
4. **OFV는 적합의 언어다**: maximum likelihood는 θ, ω, σ를 동시에 조정하여 OFV를 최소화한다. Nested model에서는 ΔOFV 3.84(df=1, α=0.05)가 LRT 기준이고, non-nested model에서는 AIC가 쓰인다. `[R&T p.373]`

#### D. Boundary Conditions

| Boundary | Failure signature |
|---|---|
| η distribution이 unimodal/log-normal이어야 함 | bimodal histogram이면 genotype/phenotype subgroup 가능성. `[R&T p.366, p.393–397]` |
| ε가 mean 0, variance σ²의 random residual이어야 함 | residual trend가 남으면 structural/error model이 variability source를 설명하지 못한 것. `[R&T p.372]` |
| Sparse data도 같은 population에서 왔다고 볼 수 있어야 함 | outlier population이 섞이면 population mean과 ω²이 모두 왜곡. |
| Covariate가 식별 가능해야 함 | G&W의 identifiability/estimability 문제처럼, 데이터가 정보를 주지 않으면 파라미터는 숫자로만 존재한다. `[G&W p.348–351]` |

#### E. Zettelkasten Atom

```yaml
aliases: [IIV, BSV, NLME taxonomy, theta-eta-epsilon]
tags: [pharmacometrics/poppk, nonmem/omega, statistics/nlme]
source: "R&T p.369-373; G&W p.335-336; G&W PK50 p.704-708"
```

<!-- RECAP -->
**C1 recap**: θ는 중심, η는 개인의 위치, ε는 남은 흔들림이다. C2는 ε의 형태를 정하고, C3는 η 안의 설명 가능한 부분을 꺼내며, C4는 η 분포가 매끄럽지 않을 때의 생물학적 이유를 찾는다.

---


<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.366, Figure 12-6 — frequency distributions for clearance of four hypothetical drugs.
Why this matters: 같은 mean을 가져도 CV와 distribution shape가 다르면 individual dose decision의 의미가 완전히 달라진다. 특히 bimodal distribution에서는 mean이 population의 대표값이 아니라 오히려 가장 덜 그럴듯한 값이 될 수 있다.
When to look: after reading this card
Learner instruction: A/B/C에서 mean은 같지만 spread가 달라지는 점을 먼저 본다. 그다음 D에서 두 봉우리 사이에 mean이 놓이는 장면을 보고, 왜 θ만으로는 subgroup risk를 설명할 수 없는지 연결한다.
<!-- /FIGURE_POINTER -->

> **Mastery Note — [CRUCIBLE_DERIVED]**  
> C1의 핵심은 θ, η, ε를 외우는 것이 아니라, 한 데이터셋 안의 변이가 어느 그릇에 배정되는지 보는 것이다. ε가 설명하지 못한 패턴은 η처럼 보이고, η로 설명해야 할 구조가 빠지면 잔차처럼 남기 때문에 C1은 이후 모든 모델 진단의 좌표축이다.

### C2. 잔차 오차 모델 — additive / proportional / exponential

<!-- MASTER LENS -->
**개념 Big Idea**

Residual error model은 “assay와 observation process가 어떤 방식으로 틀리는가”에 대한 선언이다. ε를 잘못 선언하면 측정/잔차 구조의 문제가 ω² 또는 covariate 효과처럼 보인다. `[R&T p.371–373]`

#### A. Formal Definition

R&T가 제시하는 residual variability model은 다음 세 가지다. `[R&T p.372]`

| Model | Equation | Interpretation |
|---|---|---|
| Additive | $Y = F + \varepsilon$ | 절대오차가 농도와 무관하게 거의 일정. |
| Proportional | $Y = F(1+\varepsilon)$ | 상대오차/CV가 농도 범위 전반에서 거의 일정. |
| Exponential | $Y = F\exp(\varepsilon)$ | 양수 보장; log-domain에서 additive error가 됨. |

Log transformation 후 exponential error는 다음과 같이 additive form이 된다. `[R&T p.373]`

$$
\ln Y = \ln F + \varepsilon
$$

`[교과서 외 구현 번역]` Combined/mixed residual model은 실무 NONMEM에서 자주 쓰이지만, R&T p.372가 직접 열거한 source model은 additive/proportional/exponential이다. 따라서 combined model은 source-derived가 아니라 구현 번역으로만 둔다.

#### B. Code Structure

```nmtran
; [교과서 외 구현 번역]
$ERROR
IPRED = F
W     = SQRT((THETA(3)*IPRED)**2 + THETA(4)**2)
Y     = IPRED + W*EPS(1)
```

이 코드는 proportional component와 additive component를 하나의 `W`로 합친 구현이다. 그러나 source-locked 본문에서 중요한 점은 코드가 아니라 **잔차가 random, mean zero, variance σ²이어야 한다**는 R&T의 조건이다. `[R&T p.372]`

#### C. Structural Necessity

<!-- ANCHOR -->
잔차 모델은 covariate selection보다 앞선다. 예를 들어 high concentration에서 residual spread가 커지는 자료에 additive error만 쓰면, 모델은 그 확산을 설명하기 위해 ω²를 키우거나 가짜 covariate를 찾는다. 반대로 LLOQ 근처 절대오차가 큰 자료에 proportional error만 쓰면, low concentration residual pattern이 systematic하게 남는다.

R&T는 residual variability가 완전히 random이어야 하며, 그렇지 않으면 structural model 또는 error model이 중요한 variability source를 설명하지 못한 것이라고 명시한다. `[R&T p.372]`

#### D. Boundary Conditions

| Situation | Preferred thinking |
|---|---|
| Concentration range가 좁고 assay SD가 거의 일정 | Additive model 검토. |
| 넓은 concentration range와 constant CV assay | Proportional 또는 exponential model 검토. |
| 여러 order of magnitude의 자료 | ln-transform과 transformed error model을 함께 생각. `[R&T p.373; G&W p.337–339]` |
| Residual trend가 남음 | covariate를 넣기 전 structural/error model부터 재검토. |

#### E. Limitations

- Shrinkage formula, 20–30% threshold, Savic & Karlsson 2009는 이 PDF 범위에 없다. 본 세션에서는 `[교과서 외 후속 구현 지식]`으로만 남긴다.
- Sparse sampling에서 η-EBE와 residual plot을 해석할 때는, low shrinkage/normal-looking η histogram을 좋은 모델의 증거로 단정하지 않는다. 데이터가 EBE를 실제로 식별할 수 있었는지 먼저 묻는다.

<!-- TRENCH -->
**Trench-Level Tip**: C2에서 한 가지를 외운다면 “ε의 실패는 η의 성공처럼 보인다”이다. Residual model을 틀리면 covariate model은 정교해지는 것이 아니라 정교하게 틀린다.

#### F. Zettelkasten Atom

```yaml
aliases: [RUV, residual error, sigma, additive error, proportional error]
tags: [pharmacometrics/nonmem, statistics/residuals]
source: "R&T p.371-373; G&W p.337-339"
```

<!-- RECAP -->
**C2 recap**: ε는 남는 오차가 아니라 observation process의 모델이다. ε가 잘못되면 ω²과 covariate가 모두 오염된다.

---


<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.371, Figure 12-12 — homoscedastic vs heteroscedastic parameter variability.
Why this matters: Additive, proportional, exponential error model은 식만 보면 서로 다른 문법처럼 보인다. Figure 12-12는 residual spread가 일정한지, prediction 크기에 따라 커지는지를 눈으로 구분하게 해 준다.
When to look: after reading this card
Learner instruction: Error spread가 concentration 또는 prediction scale과 함께 변하는지 확인한다. 그 pattern을 C2의 “ε를 잘못 선언하면 ω² 또는 covariate 효과처럼 보인다”는 문장에 다시 연결한다.
<!-- /FIGURE_POINTER -->

> **Practice Lens — [CRUCIBLE_DERIVED]**  
> 공변량 탐색 전에 residual pattern을 먼저 안정화해야 한다. 잔차 구조가 틀린 상태에서 공변량을 추가하면, 생리학적 설명을 발견한 것이 아니라 오차 모델의 실패를 covariate가 대신 설명하게 될 수 있다.

### C3. 공변량 모델링 — CrCl, fu, and reparameterization

<!-- MASTER LENS -->
**개념 Big Idea**

<!-- ANNOTATION -->Covariate modeling(← 변이의 설명변수를 모델에 넣는 작업)은 ω²을 “줄이는 기술”이 아니다. 더 정확히는 ω² 안에 섞인 생리학을 분리해 이름을 붙이는 작업이다. R&T의 creatinine clearance 예시는 renal clearance의 생리학을 CL_i에 연결하고, G&W PK50은 protein binding `fu`가 total parameter variability의 일부를 설명함을 보여 준다. `[R&T p.369–371; G&W p.706–709]`

#### A. Formal Definition

R&T는 creatinine clearance가 renal clearance의 interindividual difference를 설명하는 covariate가 될 수 있다고 설명한다. 예시 구조는 다음과 같다. `[R&T p.369–371]`

$$
CL_i = \theta_1 + \theta_2\cdot GFR_i + \eta_i
$$

또는 NONMEM 구현에서는 흔히 다음과 같은 centered covariate form을 쓴다.

```nmtran
; [교과서 외 구현 번역]
CL = THETA(1) * (CRCL/90)**THETA(2) * EXP(ETA(1))
```

여기서 covariate가 설명한 부분은 θ 구조로 이동한다. 설명되지 않은 개인 간 차이만 η에 남는다.

#### B. PK50 Anchor: fu는 “ω² reduction”이 아니라 좌표계 변환이다

<!-- ANNOTATION -->여기서 독자가 놓치기 쉬운 전환은 “covariate model”과 “reparameterization”의 구분이다. 둘 다 variability 해석을 바꾸지만, 하나는 predictor를 추가하는 것이고 다른 하나는 같은 자료를 다른 좌표계로 다시 쓰는 것이다.

G&W PK50에서 12명 환자는 CpD 566 µg을 5시간 IV infusion으로 받았고, total concentration과 unbound concentration이 함께 해석되었다. Plasma protein binding data인 `fu`는 total disposition parameter로부터 unbound parameter를 derive하는 데 사용되었다. `[G&W p.704–707]`

| Parameter | Total estimate (CV%) | Unbound estimate (CV%) |
|---|---:|---:|
| Cl | 11.4 L·h⁻¹ (28%) | 720 L·h⁻¹ (9%) |
| Cld | 4.35 L·h⁻¹ (39%) | 265 L·h⁻¹ (33%) |
| Vc | 19.9 L (29%) | 1270 L (18%) |
| Vt | 30.9 L (35%) | 2030 L (51%) |

`[G&W p.708, Table 50.1]`

Source-exact interpretation: **PK50은 total Cl CV 28%와 unbound Clu CV 9%를 보고한다.** 이는 NONMEM covariate model이 ω²(CL)을 28%에서 9%로 “깎았다”는 뜻이 아니다. 같은 12명 자료를 total coordinate와 unbound coordinate로 다시 표현했을 때 variability가 다르게 보인다는 뜻이다. `fu = 0.016 ± 0.0049`였으므로 protein binding variability가 total concentration/parameter variability의 일부를 설명한다. `[G&W p.708–709]`

<!-- TRENCH -->
**Trench-Level Tip — ETA 위치**: `fu`가 deterministic reparameterization이면 `CL = fu * CLu`의 좌표계 변환으로 처리한다. 반대로 population covariate model로 쓸 때는 `CLu`에 남길 η와 `fu` measurement variability를 분리해야 한다. 두 경우를 섞으면 ETA가 physiology가 아니라 accounting error를 흡수한다.

#### C. PK vs PD variability separation

PK50의 결정적 메시지는 protein binding이 모든 variability를 설명하지 않는다는 점이다. CpD는 비슷한 exposure에서도 response가 8배(0.5–4.0 response units)까지 달랐다. 또한 unbound concentration을 사용해도 EC50 variability는 오히려 커졌다. 저자들은 Emax < 1인 non-responder가 genetic makeup/receptor density와 관련된다고 해석했다. `[G&W p.707–709]`

R&T도 plasma concentration과 response를 함께 측정해야 PK variability와 PD variability를 구분할 수 있다고 한다. `[R&T p.363–364]` 따라서 covariate가 PK parameter variability를 설명했다고 해서 response variability까지 설명했다고 보면 안 된다.

#### D. Structural Necessity

- Covariate는 **η를 없애는 변수**가 아니라 **η 안의 설명 가능한 구성요소를 θ 구조로 옮기는 변수**다.
- Covariate 도입 전에는 G&W식 EDA가 선행되어야 한다: individual profile, pooled data, dose normalization, transformation으로 subgroup 또는 trend를 먼저 본다. `[G&W p.334–336]`
- Identifiability가 없는 covariate는 이름만 생리학적일 뿐 모델 안에서는 또 다른 noise source가 된다. `[G&W p.348–351]`

#### E. Limitations

- Variance propagation 식 `CV(CL)^2 ≈ CV(fu)^2 + CV(CLu)^2`는 본 문서에서 삭제한다. PDF에 없고, 독립성 가정 및 산술 검증도 성립하지 않는다.
- Total concentration safety threshold와 unbound concentration individualization은 서로 다른 coordinate system이다. G&W는 total C >50 µg·L⁻¹을 피하라고 하면서, variability 있는 protein binding을 고려해 safety margin은 total보다 unbound concentration 기반이 낫다고 결론낸다. `[G&W p.705, p.709]`

#### F. Zettelkasten Atom

```yaml
aliases: [covariate model, creatinine clearance, protein binding, fu, reparameterization]
tags: [pharmacometrics/covariate, pk/protein-binding, nonmem/eta]
source: "R&T p.369-371; G&W PK50 p.704-710"
```

<!-- RECAP -->
**C3 recap**: covariate는 ω²을 마술처럼 줄이지 않는다. 좌표계를 바꾸거나 physiology를 θ 구조로 옮겨서, 남은 η가 진짜 unexplained variability에 가까워지게 한다.

---


<!-- FIGURE_SCHEMATIC -->
Title: PK50 coordinate split — total variability, fu reparameterization, and remaining PD variability
Mode: N
Visual objective: 5초 안에 “protein binding은 total PK variability 일부를 설명하지만, PD response variability는 그대로 남는다”를 보이게 한다.
Core message: PK50의 fu는 NONMEM covariate-model ω² reduction이 아니라 total coordinate를 unbound coordinate로 다시 표현하는 reparameterization이며, 이 변환 후에도 response variability는 별도 PD source로 남는다.
Elements to include: Left lane: Total coordinate — Cl = 11.4 L·h⁻¹ (CV 28%), total concentration, total C >50 µg·L⁻¹ avoid; Center node: fu = 0.016 ± 0.0049 — deterministic reparameterization / coordinate change; Right lane: Unbound coordinate — Clu = 720 L·h⁻¹ (CV 9%), unbound-based safety margin; Lower branch: PD variability remains — response 8-fold, EC50 total 1.8 (CV 40%) vs EC50 unbound 0.029 (CV 60%), responder/non-responder; Warning label: Do not read as: fu covariate reduced ω²(CL) 28%→9%.
Elements to exclude: Individual subject-level Table 50.3 values; infusion regimen calculation details; exact reproduction of Fig.50.1, Fig.50.2, Table 50.1, or Table 50.2 layout; new variance propagation equations.
Suggested rendering: Mermaid
Caption: PK50 shows that fu changes the coordinate system for PK interpretation, while PD response variability remains a separate source of between-subject variability.
Alt text: Flow diagram showing total PK parameters transformed by fu into unbound parameters, with a separate lower branch indicating remaining pharmacodynamic response variability.
Source relation: Newly designed
<!-- /FIGURE_SCHEMATIC -->

> **Mastery Note — [AUDIT_DERIVED]**  
> PK50의 `fu` 사례는 ‘공변량을 넣어 ω²을 줄였다’는 이야기가 아니라, total coordinate와 unbound coordinate를 구분해야 한다는 이야기다. 같은 자료를 다른 생물학적 좌표계로 표현했을 때 줄어드는 변이와, 모델 안에서 covariate가 설명해 줄이는 변이를 섞지 않는 것이 C3의 핵심 판단이다.

### C4. 유전적 다형성 — IIV의 불연속 substructure

<!-- MASTER LENS -->
**개념 Big Idea**

C1–C3은 η를 대개 smooth, log-normal distribution으로 다룬다. 그러나 pharmacogenetics는 η가 실제로는 하나의 매끄러운 분포가 아닐 수 있음을 보여 준다. PM/IM/EM/UM 또는 responder/non-responder 같은 불연속 subpopulation의 합일 수 있다. `[R&T p.393–410]`

#### A. Formal Definition

R&T는 genetic polymorphism을 population 안에서 inherited phenotype이 <!-- ANNOTATION -->polymodal distribution(← 봉우리가 여러 개인 분포)을 만들 수 있는 현상으로 다룬다. 핵심은 inherited trait가 다른 variability source와 달리 평생 지속되는 개인 특성이라는 점이다. `[R&T p.393]`

Hardy-Weinberg logic은 NAT2 acetylator 예시에서 제시된다.

$$
p^2 + 2pq + q^2 = 1
$$

R&T는 slow acetylator가 recessive homozygote일 때, allele frequency로 heterozygous/homozygous fast acetylator frequency를 계산하는 방식을 설명한다. `[R&T p.402]`

#### B. Source-Locked Genetic Examples

| Example | Source-locked point | Modeling implication |
|---|---|---|
| Nortriptyline twins | identical twins의 intrapair variability가 fraternal twins보다 작아 genetics가 PK variability에 크게 기여. `[R&T p.394]` | “unexplained η” 안에 inherited component가 있을 수 있음. |
| CYP2D6 / nortriptyline | functional CYP2D6 gene copy 수가 많을수록 clearance가 커지고 exposure가 낮아짐. `[R&T p.397]` | η(CL)이 smooth가 아니라 gene-copy category로 갈라질 수 있음. |
| CYP2C9 / warfarin | CYP2C9 mutation이 S-warfarin metabolism과 dose variability에 기여. `[R&T p.398, p.406]` | PK genotype + PD genotype(VKORC1)을 동시에 고려해야 함. |
| Codeine | CYP2D6-mediated morphine formation은 minor pathway라도 potent metabolite 때문에 clinically important. `[R&T p.399, p.404]` | Parent drug clearance만 보면 toxic/active metabolite risk를 놓침. |
| TPMT / thiopurines | TPMT polymorphism은 thiopurine dose와 toxicity에 큰 영향. `[R&T p.400]` | Poor metabolizer subgroup은 평균 dose로 다룰 수 없음. |
| NAT2 / isoniazid | 483명에서 6-h isoniazid concentration의 bimodal distribution. `[R&T p.402]` | Bimodal η distribution의 canonical example. |
| VKORC1 / warfarin | CYP2C9, VKORC1, age/body weight 등이 warfarin dose variance를 나누어 설명. `[R&T p.406]` | Single covariate determinism 금지. |

Table 13-1의 poor metabolizer frequency는 source value만 유지한다: CYP2D6 PM은 Caucasians 5–10%, African Americans 3.8%, Asians 0.9%; CYP2C9 PM은 Caucasians 1%; CYP2C19 PM은 Caucasians 3–5%, Asians 16%; TPMT deficient는 Caucasians 0.3%, Asians 0.04%; NAT2 slow acetylator는 Caucasians/African Americans 60%, Asians 10–20%; UGT1A1 poor metabolizer status는 Caucasians 11%, Asians 1–3%. `[R&T p.395]`

#### C. Code Structure

```nmtran
; [교과서 외 구현 번역]
IF (CYP2D6PM.EQ.1) THEN
  CL = THETA(1) * THETA(2) * EXP(ETA(1))
ELSE
  CL = THETA(1) * EXP(ETA(1))
ENDIF
```

<!-- TRENCH -->
**Trench-Level Tip — phenotype level 통합**: categorical covariate는 level별 sample size가 충분하지 않으면 THETA factor가 ETA에 흡수된다. PM n=3 같은 빈 셀에서는 “효과 없음”이 아니라 “효과를 식별할 정보가 없음”일 수 있다.

#### D. Structural Necessity

- Mean과 variance뿐 아니라 **distribution shape**가 중요하다. R&T의 hypothetical clearance distribution에서 bimodal distribution은 평균이 치료적으로 거의 무의미할 수 있음을 보여 준다. `[R&T p.366]`
- Genetic polymorphism은 η histogram의 “두 봉우리”를 physiology로 번역한다.
- R&T는 ethnicity가 genetic characteristic의 proxy일 뿐이며, within-group variability도 클 수 있다고 경고한다. 따라서 ethnicity covariate를 genotype처럼 해석하면 안 된다. `[R&T p.395, p.409]`
- CYP3A4처럼 큰 variability가 있어도 명확한 genetic factor가 드러나지 않는 경우가 있다. 모든 큰 ω²이 genotype peak를 뜻하지는 않는다. `[R&T p.399, p.410]`

#### E. Limitations

- HLA-B*5701 frequency, modern FDA pharmacogenomic label count, detailed PM/IM/EM/UM frequency table은 이 PDF 범위 밖이므로 삭제한다.
- Pharmacogenetics는 강력하지만 완결된 설명이 아니다. R&T는 genotype 외에도 demographics, adherence 등 다른 요인이 optimal dosing에 필요하다고 마무리한다. `[R&T p.409]`

#### F. Zettelkasten Atom

```yaml
aliases: [pharmacogenetics, genetic polymorphism, CYP2D6, CYP2C9, NAT2, TPMT, VKORC1]
tags: [pharmacometrics/iiv, pharmacogenomics, nonmem/categorical-covariate]
source: "R&T p.393-410"
```

<!-- RECAP -->
**C4 recap**: 유전 다형성은 covariate 목록이 아니라 η 분포의 모양을 바꾸는 생물학이다. Smooth log-normal assumption이 깨지는 순간, 평균 dose는 subgroup toxicity 또는 inefficacy를 숨긴다.

---


<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.402, Figure 13-6 — isoniazid 6-hour concentration distribution after 9.8 mg/kg oral dose in 483 subjects.
Why this matters: C4의 핵심은 유전 다형성이 단순 covariate label이 아니라 distribution shape 자체를 바꾼다는 점이다. Figure 13-6은 NAT2 acetylator status가 실제 concentration distribution을 bimodal하게 만드는 장면을 보여 준다.
When to look: after reading this card
Learner instruction: 두 peak가 어디에 생기는지 먼저 확인한다. 그런 다음 “η histogram이 두 봉우리라면 smooth log-normal IIV 하나로 덮으면 안 된다”는 C4 recap과 연결한다.
<!-- /FIGURE_POINTER -->

> **Failure Mode — [CRUCIBLE_DERIVED]**  
> 범주형 유전 구조가 실제로 존재하는데 표본의 한 subgroup이 작거나 비어 있으면, 모델은 그 효과를 독립된 phenotype 효과로 보지 못하고 η 안에 흡수할 수 있다. 그래서 C4에서는 genotype label 자체보다, η distribution과 concentration distribution의 모양이 단봉인지 다봉인지를 먼저 확인해야 한다.

## §5 — Confusion Pair Dissection

<!-- CONFUSION -->
### Pair 1. ω²(IIV) vs σ²(RUV)

| 구분 | ω² / η | σ² / ε |
|---|---|---|
| 질문 | 사람마다 얼마나 다른가? | 같은 사람의 관측값이 예측에서 얼마나 벗어나는가? |
| 위치 | `$OMEGA`, individual parameter | `$SIGMA`, residual model |
| Source anchor | R&T p.369–371 | R&T p.371–373 |
| 흔한 오류 | assay error를 IIV로 해석 | true IIV를 residual noise로 묻음 |

**Critical distinction**: ω²과 σ²은 같은 총 unexplained variability를 두고 경쟁한다. 잔차 모델을 틀리면 covariate가 단순히 보이거나 사라지는 것이 아니다. 분산이 잘못된 그릇으로 이동한다.

<!-- CONFUSION -->
### Pair 2. Total Cl vs Unbound Clu — PK50 anchored

| 구분 | Total coordinate | Unbound coordinate |
|---|---|---|
| 무엇을 봄 | total concentration/parameter | free concentration/parameter |
| PK50 value | Cl 11.4 L·h⁻¹, CV 28% | Clu 720 L·h⁻¹, CV 9% |
| Interpretation | protein binding variability가 섞임 | fu로 재표현된 disposition |
| Source | G&W p.708 | G&W p.708 |

**Corrected Critical Blow**: PK50은 “fu covariate가 ω²을 줄였다”가 아니라, same 12 subjects를 total과 unbound coordinate로 비교했을 때 variability 해석이 달라짐을 보여 준다. Dose/safety 판단에서 total C >50 µg·L⁻¹ 회피 기준과 unbound-based safety margin이 혼동되면, exposure-response 해석의 좌표계가 불일치한다. `[G&W p.705, p.709]`

<!-- CONFUSION -->
### Pair 3. PK variability vs PD variability

PK variability는 concentration-time profile이 왜 다른가를 묻는다. PD variability는 같은 exposure에서 response가 왜 다른가를 묻는다. R&T는 plasma concentration measurement가 PK와 PD variability를 분리하는 전제라고 한다. `[R&T p.363–364]`

PK50에서 protein binding은 total concentration variability 일부를 설명했지만, response는 비슷한 exposure에서도 8배 차이를 보였다. 이것은 covariate 하나가 모든 variability를 설명한다는 사고가 왜 위험한지 보여 주는 핵심 예다. `[G&W p.707–709]`

<!-- CONFUSION -->
### Pair 4. Mean distribution vs shape distribution

R&T의 nortriptyline 예시는 log-normal distribution을, hypothetical clearance distribution은 bimodal distribution에서 평균이 치료적 대표값이 되기 어렵다는 점을 보여 준다. `[R&T p.363, p.366]` 평균과 CV만 보고 η distribution의 shape를 확인하지 않으면, C4에서 다룬 genetic subgroup을 놓친다.

<!-- RECAP -->
**§5 recap**: 이 세션의 혼동은 거의 모두 “어느 좌표계의 변이인가”로 귀결된다. 즉, individual vs residual, total vs unbound, PK vs PD, mean vs shape를 구분해야 한다.

---

## §7 — Self-Test: Active Recall Module

<!-- SELF-TEST -->
### Q1. `CL_i = CL·exp(η_i)`를 쓰는 가장 직접적인 이유는 무엇인가?

**Answer**: CL이 음수가 되지 않도록 보장하면서, η를 normal distribution으로 둘 수 있기 때문이다. R&T는 exponential error model이 approximate constant CV를 제공하고 computational difficulty를 줄인다고 설명한다. `[R&T p.371]`

<!-- SELF-TEST -->
### Q2. Residual variability가 random mean zero가 아니면 무엇을 뜻하는가?

**Answer**: structural model 또는 error model이 아직 중요한 variability source를 설명하지 못했다는 뜻이다. 이 상태에서 covariate를 찾으면, covariate가 biology가 아니라 residual misspecification을 설명할 수 있다. `[R&T p.372]`

<!-- SELF-TEST -->
### Q3. PK50에서 “total Cl CV 28%, unbound Clu CV 9%”를 어떻게 해석해야 하는가?

**Answer**: `fu`를 covariate로 넣어 ω²을 28%에서 9%로 줄였다는 뜻이 아니다. 같은 12명 CpD data를 total coordinate와 unbound coordinate로 표현했을 때, protein binding variability가 total parameter variability의 일부를 설명한다는 뜻이다. `[G&W p.706–709]`

<!-- SELF-TEST -->
### Q4. `CV(CL)^2 ≈ CV(fu)^2 + CV(CLu)^2`를 이 문서에서 쓰지 않는 이유는 무엇인가?

**Answer**: 이 variance propagation 식은 첨부 PDF에 없고, 독립성 가정도 제시되지 않았으며, Audit에서 산술적으로도 검증되지 않는다고 판정되었다. 따라서 source-locked Content Lock에서는 삭제한다.

<!-- SELF-TEST -->
### Q5. PK50에서 unbound concentration을 써도 PD variability가 남은 이유는 무엇인가?

**Answer**: protein binding은 PK coordinate의 variability 일부를 설명하지만, response variability는 receptor density/genetic makeup 같은 PD source를 포함한다. G&W는 Emax <1인 non-responder가 full target expression을 결여한 것으로 해석한다. `[G&W p.707–709]`

<!-- SELF-TEST -->
### Q6. η-EBE histogram이 두 봉우리로 보이면 가장 먼저 무엇을 의심해야 하는가?

**Answer**: smooth log-normal IIV 하나가 아니라, genotype/phenotype subgroup 또는 mixture-like population structure가 섞였는지 의심해야 한다. 단, sparse sampling이면 histogram 자체의 정보량을 먼저 점검해야 한다. `[R&T p.366, p.393–397]`

<!-- SELF-TEST -->
### Q7. Ethnicity covariate를 genotype처럼 해석하면 왜 위험한가?

**Answer**: R&T는 ethnicity가 individual genetic characteristics의 불완전한 proxy이며, within-group variability도 크다고 경고한다. Ethnicity term은 exploratory covariate일 수 있지만 mechanistic genotype의 대체물은 아니다. `[R&T p.395, p.409]`

<!-- SELF-TEST -->
### Q8. 다음 중 먼저 고칠 것은 무엇인가: residual model misspecification vs covariate model 추가?

**Answer**: residual model misspecification을 먼저 고친다. ε의 구조가 틀린 상태에서 covariate를 추가하면 ω²과 σ²의 경쟁이 왜곡되어, biology가 아니라 error model의 실패를 covariate가 설명하게 된다. `[R&T p.371–373]`

<!-- RECAP -->
**§7 recap**: 시험 문제의 정답은 대부분 “source of variability를 잘못된 그릇에 넣지 말라”이다.

---

## §8 — Meta-Frame & Big Picture

### A. Positioning — 28-session architecture

이 세션은 PopPK curriculum의 **variance axis**다. 이전 세션들이 Cl, V, ka, t½ 같은 structural parameter의 평균을 세웠다면, 이 세션은 그 평균 주변의 개인차와 잔차를 분해한다. 따라서 이후 FOCE/FOCE-I, GOF, covariate selection, Bayesian TDM은 모두 이 분해 위에서만 의미가 있다.

### B. Dependencies — 대충 넘겼을 때 발생하는 실패 모드

| Dependency | 대충 넘기면 생기는 실패 |
|---|---|
| C1 θ/η/ε | `$OMEGA`와 `$SIGMA`를 숫자로만 읽고, physiology vs residual noise를 구분하지 못함. |
| C2 residual error | 잘못된 ε가 ω²로 새어 가짜 IIV 또는 가짜 covariate를 만듦. |
| C3 covariate/reparameterization | `fu`, CrCl, body weight를 모두 같은 방식의 covariate로 취급해 좌표계 변환과 causal predictor를 혼동. |
| C4 genetic polymorphism | bimodal distribution을 single log-normal η로 덮어 subgroup dose risk를 숨김. |
| EDA-first | spaghetti plot과 transformed plot 없이 control stream부터 쓰다가 subgroup signal을 놓침. `[G&W p.334–336]` |
| Regulatory PopPK consistency | θ, ω², σ², residual model, covariate effect가 서로 맞지 않으면 report table은 있어도 dose rationale이 무너짐. `[R&T p.373]` |

### C. Professional Moat — 이 세션이 전문가를 가르는 지점

초급자는 “IIV가 큽니다”라고 말한다. 중급자는 “CL에 covariate를 넣겠습니다”라고 말한다. 전문가의 질문은 다르다.

1. 이 변이는 **PK인가 PD인가**? `[R&T p.363–364; G&W p.707–709]`
2. 이 변이는 **η인가 ε인가**? `[R&T p.369–373]`
3. 이 변이는 **total coordinate에서만 보이는가, unbound coordinate에서도 남는가**? `[G&W p.706–709]`
4. 이 변이는 **smooth distribution인가, subgroup/phenotype structure인가**? `[R&T p.366, p.393–410]`
5. 이 covariate는 **생리학인가, proxy인가, 또는 식별 불가능한 accounting device인가**? `[G&W p.348–351; R&T p.395]`

<!-- RECAP -->
### Final Recap

Session 13의 최종 메시지는 하나다. **ω²은 “남은 변이”가 아니라 아직 이름 붙이지 못한 생리학·유전학·행동·측정 구조의 혼합물이다.** C2는 residual noise를 정리하고, C3는 설명 가능한 physiology를 꺼낸다. C4는 smooth IIV 안에 숨어 있는 genetic discontinuity를 드러낸다. 이 순서를 지키지 않으면 NONMEM은 돌아가지만, dose individualization은 성립하지 않는다.

## PART B — Compiler-Only Appendix

This appendix is not learner-facing. It exists only to protect Phase 5 rendering fidelity and prevent regression. Do not render PART B as learner content unless explicitly requested.

### B1. Compilation Contract

- PART A is the only learner-facing body.
- Phase 5 must render PART A without altering text, equations, page/source tags, or figure marker fields.
- PART B is instruction/guardrail only.
- Do not restore deprecated material.
- Do not add new scientific content.
- Do not render PART B as learner content unless explicitly requested.
- This file is Phase 4D input for HTML compilation, not the HTML output itself.

### B2. Figure Rendering Instructions

**Approved retained markers from Phase 4C**

| ID | Mode | Decision | Source relation | Rendering consequence |
|---|---|---|---|---|
| F2 | P | KEEP | R&T p.366 Fig.12-6 | Render as text-only textbook reference callout. Do not embed image. |
| F3 | P | KEEP | R&T p.371 Fig.12-12 | Render as text-only textbook reference callout. Do not embed image. |
| F6 | N | KEEP | Newly designed from PK50 source objects | Render as a new schematic from the brief only; do not reproduce textbook layout or source tables. |
| F8 | P | KEEP | R&T p.402 Fig.13-6 | Render as text-only textbook reference callout. Do not embed image. |

**Rejected / not to restore**: F1, F4, F5, F7.  
**Image rights**: None. Do not embed copyrighted textbook images. `FIGURE_POINTER` must remain text-only. `FIGURE_SCHEMATIC` may be rendered as a new schematic using only listed elements and exclusions.  
**Phase 4D restriction**: This file contains only marker briefs. It does not contain Mermaid, SVG, or HTML figure code.

**Original Figure Strategy / Insertion Map source**: retained from `13_Content_Lock_v2.1(1).md`; all full marker blocks are already spliced into PART A.

### B3. Page Tag Rendering Rules

Preserve all source tags exactly as they appear in PART A. Do not fabricate, delete, renumber, normalize across books, or relocate tags.

Prompt 5 standard patterns must be supported:
- `[p.XX]`
- `[pp.XX–YY]` or `[pp.XX-YY]`
- `[pp.XX, YY]`
- `[p.확인 필요]`

**Session 13 source-prefix extension required**: PART A uses book-prefixed tags such as `[R&T p.369–373]`, `[G&W p.706–709]`, and `[R&T p.363–364; G&W p.707–709]`. The HTML compiler must wrap these visibly as source page tags as well, while preserving their exact text. A safe regex-equivalent family is:

- `\[(?:R&T|G&W) p\.\d+(?:[–-]\d+)?(?:,\s*p?\.?\d+)*(?:;\s*(?:R&T|G&W) p\.\d+(?:[–-]\d+)?(?:,\s*p?\.?\d+)*)?\]`
- `\[[^\]]*p\.확인 필요[^\]]*\]`

Render all matched source tags as `<span class="source-page">...</span>` except uncertainty tags, which use `<span class="source-page source-uncertain">...</span>`.

Detection limits:
- Apply to body text, captions, headings, and figure pointer callouts.
- Do not apply inside code blocks.
- Do not alter the contents of `Source:` fields inside figure markers except by wrapping at render time.
- Source tags must remain visible in print mode.

### B4. HTML Compiler Requirements

The following Prompt 5 requirements are authoritative for Phase 5. Render PART A; do not alter content.

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

### B5. Audit Guardrails

Regression-prevention items for Phase 5 and any later editing:

- Do not restore unsupported shrinkage formulae, shrinkage thresholds, or Savic & Karlsson-type external methodology as textbook-derived material.
- Do not restore FDA/21 CFR/NDA deficiency-letter, cost, timeline, probability, or reviewer-process claims absent from the attached PDFs.
- Keep NONMEM syntax and mixed/combined residual implementation language labeled as implementation translation when present; do not present it as directly printed textbook content.
- Preserve the corrected PK50 interpretation: total Cl CV 28% and unbound Clu CV 9% are different coordinate expressions of the same 12-subject source dataset, not proof that `fu` covariate modeling reduced ω² from 28% to 9%.
- Do not add new variance-propagation equations for PK50 unless already in the canonical body.
- Do not restore unsupported pharmacogenetic frequency tables or modern label-count claims.
- Do not expand excluded G&W material such as Lineweaver–Burke, Scatchard, Euler integration, nonlinear kinetics, or broad structural-model examples into new learner content.
- Do not embed textbook figures. Image rights are None.
- Preserve OFV/LRT/AIC content only within the source-supported limits stated in Content Lock v2.
- Preserve ethnicity caution as caution, not as a genetic proxy claim.

### B6. Crucible Guardrails

- Crucible Report v1 is not a raw prose source for Phase 5.
- Preserve only insights already adopted in Content Lock v2 or added here as explicitly labeled augmentation.
- Do not convert expert inference into textbook fact.
- Do not add new named drug examples, new numerical values, new regulatory scenarios, or new equations from Crucible reasoning.
- Do not restore omitted lower-priority scope-creep items.
- Preserved high-value logic: variance allocation between η/ε, residual-model-to-covariate cascade, PK50 total/unbound coordinate split, and genetic/distribution-shape interpretation.

### B7. Deprecated and Forbidden Restorations

- Step 1 Draft v0 is deprecated and must not be used as a learner-body source except through the Micro-Patch Gate.
- Do not restore rejected overclaims, unsupported numbers, unsupported regulatory claims, source-unsupported examples, unapproved code, or unapproved figures.
- Do not make Content Lock v3 by stylistic rewriting.
- Do not add broad external literature context.
- Do not create new source page tags or alter existing source tags.
- Do not generate new figures beyond approved F2/F3/F6/F8 marker instructions.

### B8. PATCH MODE Splice Verification Table

| Marker # | Anchor text | Anchor found? | Match count | Inserted? | Final location (§ + card) |
|---|---|---|---:|---|---|
| F2 | ### C1. 변이의 구조적 분해 — θ, η, ε taxonomy | YES | 1 | YES | §2 C1. 변이의 구조적 분해 — θ, η, ε taxonomy |
| F3 | ### C2. 잔차 오차 모델 — additive / proportional / exponential | YES | 1 | YES | §2 C2. 잔차 오차 모델 — additive / proportional / exponential |
| F6 | ### C3. 공변량 모델링 — CrCl, fu, and reparameterization | YES | 1 | YES | §2 C3. 공변량 모델링 — CrCl, fu, and reparameterization |
| F8 | ### C4. 유전적 다형성 — IIV의 불연속 substructure | YES | 1 | YES | §2 C4. 유전적 다형성 — IIV의 불연속 substructure |

### B9. Zero-Omission Coverage Matrix

| Domain | Required coverage | Status | Basis |
|---|---|---|---|
| Scope range | R&T p.361–410; G&W p.333–352 and p.704–710 | PASS | Source lock preserved; both PDFs attached and checked for relevant pages/figures. |
| Image rights | None; P/N only | PASS | No textbook image embedding requested; all kept textbook visuals are FIGURE_POINTER except one new schematic brief. |
| MUST concepts | C1 θ/η/ε, C2 residual error, C3 covariate/reparameterization, C4 genetic substructure | PASS | All four §2 cards present. |
| PK50 hard anchors | CpD 566 µg / 5 h / 12 subjects; Cl, Cld, Vc, Vt, fu, EC50, response variability | PASS | C3 and F6 preserve the locked values; no new PK50 values added. |
| R&T variability anchors | warfarin, nortriptyline, mean vs shape, population analysis, residual models, OFV/LRT/AIC, genetics | PASS | Distributed across C1, C2, C4, §5, §7, §8. |
| G&W modeling anchors | EDA before equations, NAD/NPD/population approach, identifiability/estimability, PK50 | PASS | Preserved in C1/C3 and dependencies. |
| Audit MUST_FIX | Unsupported shrinkage thresholds/formula, FDA/21 CFR/cost/time claims, unmarked implementation syntax | PASS | No unsupported threshold/regulatory overclaim restored; implementation content remains labeled when present. |
| Audit SHOULD_FIX | Plot-before-equations, PK vs PD separation, average vs individual-patient message, residual mean-zero logic | PASS | Present in C1/C2/C3/§5/§7/§8. |
| Audit T5 omissions | MISSING_AUTHOR_MSG / MISSING_BRIDGE items | PASS | High-impact bridges are included or intentionally compressed; no broad scope expansion made. |
| Phase 4C figure coverage | KEEP F2, F3, F6, F8 exactly once; reject F1/F4/F5/F7 | PASS | Counts: pointer starts=3, schematic starts=1. |
| Page/source tag integrity | Existing source tags preserved | PASS | No source tag was added, deleted, renumbered, or moved; compiler receives source-prefix rendering rule. |
| Crucible Grade A preservation | variance conservation, fu coordinate split, residual→covariate cascade, genetic distribution shape | PASS | Already present in canonical body and reinforced only through labeled short mastery notes. |
| Deprecated source control | Step 1 Draft v0 not restored | PASS | Part A uses Content Lock v2 scientific body plus approved patch markers only. |

### B10. Micro-Patch Log

| Micro-patch | Applied? | Location | Rationale |
|---|---|---|---|
| Scientific text change to canonical Content Lock v2 body | NO | N/A | No unresolved high-impact omission required direct rewriting. |
| Figure marker insertion | YES | §2 C1/C2/C3/C4 | Approved Phase 4C PATCH MODE marker insertion, verified by exact-anchor match. |
| Learner Navigation Aid | YES | PART A top | Non-scientific learner-facing wrapper derived from existing headings/cards. |
| Mastery Augmentation Notes | YES | Adjacent to C1–C4 | Bounded, labeled notes; no new values, drugs, equations, page tags, or external claims. |
| Source-prefix rendering extension | YES | PART B B3 only | Compiler guardrail to render existing `[R&T p...]` and `[G&W p...]` tags visibly without altering content. |

### B11. Mastery Augmentation Log

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
|---:|---|---|---|---|---|---|
| 1 | §2 C1 after F2 | Mastery Note | YES | CRUCIBLE_DERIVED | Links θ/η/ε taxonomy to variance-allocation intuition. | Low |
| 2 | §2 C2 after F3 | Practice Lens | YES | CRUCIBLE_DERIVED | Prevents false covariate interpretation before residual model stabilization. | Low |
| 3 | §2 C3 after F6 | Mastery Note | YES | AUDIT_DERIVED | Protects corrected PK50 coordinate/reparameterization interpretation. | Low |
| 4 | §2 C4 after F8 | Failure Mode | YES | CRUCIBLE_DERIVED | Highlights distribution-shape check for genetic substructure without adding new examples. | Low |

| Rejected candidate | Reason for rejection |
|---|---|
| Additional Apex second note for C1 | Budget not needed; C1 already has canonical Master Lens and one bounded augmentation. |
| Regulatory deficiency scenario note | Rejected because Audit excludes unsupported regulatory/cost/timeline claims from the attached PDFs. |
| New clinical example for covariate modeling | Rejected because Phase 4D forbids new named examples beyond PDF/Audit/Crucible. |

```
=== SCOPE LOCK ===
Source       : Rowland & Tozer 5e (Ch.12-13) + Gabrielsson & Weiner 5e (Ch.4 + PK50) — 혼합
Pages        : R&T p.361–410, G&W p.333–352, p.704–710
Mode         : A-Critical
Image rights : None (Pointer/Schematic only)
=================
```

---

## CURATION MAP — Master's Lens First

**거장의 사전 선언:**
이 세션은 28주 PK/PD 커리큘럼의 **분산 축(variance axis)** 의 정초다. 평균(θ) 하나만 잡는 것은 NCA로도 가능하다. 그러나 NONMEM의 진짜 힘은 **ω²(개체 간), σ²(잔차), 그리고 그 사이를 가르는 covariate** 라는 세 자릿수 통계 구조를 동시에 추정하는 데서 나온다. 이 세 자릿수를 혼동하면 — η-shrinkage가 σ²로 흘러들고, IIV가 RUV로 위장되며, 진짜 covariate 신호가 묻혀 — Phase 3 dose individualization이 구조적으로 불가능해진다. R&T는 "왜 사람마다 다른가"의 임상·생리학적 언어를 담당하고, G&W PK50은 그 변이를 12명 antiarrhythmic 환자 데이터에서 어떻게 꺼내는가의 실험적 증거를 담당한다.

### MUST (체화 필수, 4개)

| # | 개념 | 구조적 필요성 |
|---|---|---|
| **C1** | **변이의 구조적 분해 (θ, η, ε / ω², σ²)** | 이것 없이 NONMEM `$OMEGA`, `$SIGMA` 한 줄도 해석 불가. C2-C4의 전제. |
| **C2** | **잔차 오차 모델 (Additive / Proportional / Exponential / Mixed) + Shrinkage** ⚡ Apex | 잘못 잡으면 ω²이 σ²로 새거나 그 반대. C3 covariate 탐색 자체를 무효화. |
| **C3** | **공변량 모델링 (fu, CrCl as predictor of CL/V)** | PK50에서 fu를 covariate로 쓰면 CV(CL) 28% → 9%로 깎임. ω²이 줄어드는 자리에 생리학이 드러난다. |
| **C4** | **유전적 다형성 — IIV의 불연속 substructure (CYP2D6/2C9/2C19, NAT2, TPMT, VKORC1)** | 매끄러워 보이는 ω² 안에 polymodal 봉우리가 숨어 있음. 못 찾으면 평균 용량이 일부 환자에게 독성. |

### CONTEXT (1-2문장 처리, 별도 카드 없음)

- **Spaghetti plot, NAD/NPD vs Population approach** → C1 카드 안에서 EDA 도입부로 1문단 처리
- **CYP2D6/2C9/2C19/NAT2/TPMT/UGT1A1/VKORC1 각 isoform 세부** → C4 카드 안에서 표 형태로 압축 처리. 임상 파급력만 적시.
- **Maximum likelihood / OFV / chi-squared LRT** → C1 카드의 G(Zettelkasten) 직전에 1-2문장
- **Hardy-Weinberg p²+2pq+q² 계산** → C4 카드에 NAT2 isoniazid 예시로 1문장
- **Adherence, food-drug, herbs (St. John's wort), chronopharmacology** → §8 Meta-Frame Dependencies에서 1문장 ("이 세션의 ω²은 약물 외 변이까지 흡수하는 그릇이며, RUV로 새는 주범이 이들이다")
- **Lineweaver-Burke / Scatchard / Euler integration (G&W §4.2.4, §4.6-4.7)** → 본 세션 범위에서 제외 (이 세션은 분산 축이지 추정 알고리즘 축이 아님)
- **Identifiability / Estimability (G&W §4.3.4-4.3.5)** → C3 카드에서 1문장 ("V/F flip-flop처럼 covariate 또한 식별 불가능한 형태로 모델링되면 ω²이 그 자리를 메운다")

### Curation Verdict
4개 MUST 카드 구성 확정. C2를 Apex로 지정한 근거: shrinkage 진단은 NDA Deficiency Letter 1순위 사유이며, 잔차 오차 모델 오설정은 covariate 모델 구축 전체를 무효화하는 단일 최대 실패점이다.

---

## §1 — Session Header & Roadmap

**Session 13 — 개체 간 변이 (IIV / BSV) 와 공변량 모델링**
*Source: R&T 5e Ch.12 (p.361–392) + Ch.13 (p.393–410); G&W 5e Ch.4 일부 (p.333–352) + PK50 (p.704–710)*

### Big Idea (한 문장)

> **NONMEM 혼합효과모델의 본질은 "θ는 인구의 무게중심, η는 각 개인이 그 중심으로부터 떨어진 벡터, ε는 측정 노이즈"라는 세 자릿수의 직교 분해이며, 공변량은 ω²을 깎아내는 끌이고 유전 다형성은 ω² 안에 숨은 봉우리다.**

### 개념 항법도

```
        ┌──────────────────────────────────────┐
        │  C1. θ / η / ε taxonomy              │  ← 모든 카드의 전제
        │      (ω², σ², mixed effects)         │
        └────────────┬─────────────────────────┘
                     │
        ┌────────────┴────────────┬──────────────────┐
        ▼                          ▼                  ▼
   ┌─────────┐             ┌──────────────┐     ┌────────────┐
   │  C2 ⚡  │             │     C3       │     │     C4     │
   │ Residual │             │  Covariate   │     │  Genetic   │
   │  Error  │ ──오설정──▶ │   Modeling   │ ◀── │ Polymorph. │
   │+Shrinkage│             │ (fu, CrCl)   │     │ (불연속)    │
   └─────────┘             └──────────────┘     └────────────┘
```

### 지식 그래프 위치

| 위치 | 세션 |
|---|---|
| **선행 (전제됨)** | 1구획·2구획 모델, Cl·V·t½, 단백결합, NCA, NONMEM control stream 기초 |
| **이 세션** | IIV / IOV / RUV의 세 자릿수, 공변량 도입 방법, 유전 다형성의 PK 표현 |
| **직후 후속** | FOCE/FOCE-I 추정 알고리즘, GOF 진단 (CWRES, η-EBE), Stepwise covariate selection |
| **결정적 의존 분야** | TMDD (target heterogeneity가 ω²로 표현됨), Bayesian TDM (개인 EBE 추정), QSP (mechanism-based covariate), 인구약물동태/규제 PopPK 보고서 |

---

## §2 — Concept Anatomy Cards

---

### C1. 변이의 구조적 분해 — θ, η, ε taxonomy

<!-- MASTER LENS -->
**[개념 Big Idea — 거장의 시각]**

1. **왜 치명적으로 중요한가**: 임상시험 PopPK 분석에서 IIV(η, ω²)와 RUV(ε, σ²)를 혼동하면, 환자별 dose individualization 알고리즘이 통계적 평균에 갇혀버려 Phase 3 라벨에 "Cl varies from 5 to 30 L/h"라는 묘사 외에는 아무것도 적을 수 없게 된다.

2. **체화해야 할 단 하나의 직관**: θ는 인구의 무게중심(scalar), η는 각 개인이 그 중심에서 떨어진 벡터(personal deviation, log-normal로 가정), ε는 같은 개인을 두 번 측정해도 다르게 나오는 단발성 노이즈다 — **세 차원이 서로 직교(orthogonal)할 때만 NONMEM이 작동한다.** η가 ε로 새면 shrinkage, ε가 η로 새면 inflated ω².

3. **이 직관을 머릿속에 박고 아래를 읽어라**: 모든 NONMEM `$OMEGA`/`$SIGMA` 라인은 이 세 차원 중 하나의 분산을 선언하는 것이다.
<!-- /MASTER LENS -->

#### A. Formal Definition

NONMEM의 **nonlinear mixed-effects model (NLME)** 은 i번째 개체의 j번째 관측값 $Y_{ij}$를 다음과 같이 분해한다:

$$
Y_{ij} \;=\; f\!\left(\boldsymbol{\theta},\; \boldsymbol{\eta_i},\; x_{ij}\right) \;+\; g\!\left(\boldsymbol{\theta},\; \boldsymbol{\eta_i},\; x_{ij}\right)\cdot \varepsilon_{ij}
$$

여기서:
- $\boldsymbol{\theta}$ — **fixed effect**, 인구 평균(typical value) 파라미터 벡터 (Cl, V, Ka, …). NONMEM `$THETA`.
- $\boldsymbol{\eta_i}$ — **random effect (between-subject)**, 개체 i가 인구 평균에서 떨어진 정도. $\boldsymbol{\eta_i} \sim \mathcal{N}(0, \boldsymbol{\Omega})$. NONMEM `$OMEGA`.
- $\varepsilon_{ij}$ — **random effect (residual)**, 개체 i의 j번째 관측의 잔차. $\varepsilon_{ij} \sim \mathcal{N}(0, \boldsymbol{\Sigma})$. NONMEM `$SIGMA`.

핵심 가정: $\boldsymbol{\eta_i} \perp \varepsilon_{ij}$ (직교성).

개인 PK 파라미터의 일반적 코딩 (exponential IIV):

$$
CL_i \;=\; \theta_{CL} \cdot \exp(\eta_{i,CL}) \quad\Longleftrightarrow\quad \ln CL_i \;=\; \ln\theta_{CL} \;+\; \eta_{i,CL}
$$

이때 $\eta_{i,CL} \sim \mathcal{N}(0, \omega^2_{CL})$ 이고, 작은 $\omega$에 대해 $CV(\%) \approx \omega \times 100$. `[출처: R&T 5e, Ch.12, p.369-371]`

#### B. Derivation / Code Structure

**[Vol I 데이터 앵커링 — G&W PK50, p.704-708]**

CpD (antiarrhythmic candidate)를 12명의 환자에게 566 µg을 5시간 IV infusion으로 투여하고 2-구획 모델로 적합한 결과:

| 파라미터 | Total (mean) | CV(%) total | Unbound (mean) | CV(%) unbound |
|---|---|---|---|---|
| Cl | 11.4 L·h⁻¹ | **28** | 720 L·h⁻¹ | **9** |
| Cl_d | 4.35 L·h⁻¹ | 39 | 265 L·h⁻¹ | 33 |
| V_c | 19.9 L | 29 | 1270 L | 18 |
| V_t | 30.9 L | 35 | 2030 L | 51 |

`[출처: G&W 5e, PK50, Table 50.1, p.708]`

이 표가 바로 **ω²이 무엇을 측정하는가** 의 체화점이다. Total Cl의 CV 28%는 단순한 "사람마다 다름"이 아니다 — 이 28% 안에는 (a) 진짜 unbound clearance (Cl_u) 변이 9%, (b) plasma protein binding (fu) 변이 약 31% (fu = 0.016 ± 0.0049), (c) 그 둘의 곱을 통한 전파가 모두 섞여 있다. fu를 covariate로 도입하면 (다음 카드 C3) ω²(Cl)이 28%에서 9%로 줄어든다.

**[Vol II 코드 해부 — NONMEM control stream]**

가장 단순한 1구획 IV bolus의 IIV 선언:

```nmtran
$PK
TVCL  = THETA(1)               ; 인구 평균 Cl
TVV   = THETA(2)               ; 인구 평균 V
CL    = TVCL * EXP(ETA(1))     ; 개체 i의 Cl, log-normal IIV
V     = TVV  * EXP(ETA(2))     ; 개체 i의 V,  log-normal IIV
K     = CL / V

$ERROR
IPRED = A(1) / V
Y     = IPRED * (1 + EPS(1)) + EPS(2)   ; mixed (proportional + additive) RUV

$OMEGA
0.08                           ; ω²(Cl) ≈ CV 28%, PK50 total Cl과 일치
0.05                           ; ω²(V)  ≈ CV 22%

$SIGMA
0.01                           ; σ²_prop, ≈ 10% proportional error
0.04                           ; σ²_add,  ≈ 0.2 µg/mL additive
```

**라인별 해부:**

| 라인 | 역할 | 위반 시 결과 |
|---|---|---|
| `THETA(1)` | 인구 평균 (fixed effect, scalar) | 과소·과대 추정 시 모든 개인 EBE가 한쪽으로 쏠림 |
| `EXP(ETA(1))` | 개인 deviation, log-normal | log-normal 가정 위반 (실제 분포가 bimodal — 유전 다형성 존재 시, C4 참조) → η-EBE plot에서 양봉 |
| `$OMEGA` block | between-subject variance ($\omega^2$) | block diagonal vs full block 선택이 covariance 구조 결정 |
| `$SIGMA` block | residual unexplained variance ($\sigma^2$) | 오차 모델 오설정 시 ω²으로 흘러들어 inflated IIV |

#### C. Structural Necessity

**왜 정확히 이 분해 형태인가?**

1. **Why log-normal for η?** PK 파라미터(Cl, V)는 물리적으로 양수여야 한다 (clearance가 음수일 수 없음). $\theta \cdot \exp(\eta)$ 구조는 $\eta$가 가우시안이어도 $CL_i$가 항상 양수임을 보장한다. Additive form ($CL_i = \theta + \eta_i$)을 쓰면 $\eta$가 충분히 음수일 때 $CL_i < 0$이 발생.

2. **Why orthogonal (η ⊥ ε)?** 만약 η와 ε가 상관되어 있다면 — 즉, 큰 Cl을 가진 사람일수록 측정 노이즈도 크다면 — likelihood function이 더 이상 product of independent normals로 분해되지 않아 maximum likelihood 추정이 붕괴한다.

3. **Why two-stage (population vs individual)?** Standard Two-Stage(STS, 각 개인을 따로 적합 후 평균) 방식은 sparse data에서 개인 적합이 실패할 때 그 환자를 통째로 잃는다. NLME는 한 환자의 sparse data가 인구 정보(prior로 작동하는 θ, ω²)를 "빌려" 개인 EBE를 추정한다.

#### C-2. [⚡ Apex Concept] Plausible Fallacy — *(Card C2에서 별도 처리)*

이 항목은 Card C2(잔차 오차 모델)에 배정되어 있다. C1은 taxonomy 정초이므로 Apex가 아님.

#### D. Assumptions & Boundary Conditions

| 가정 | 위반 시 발생 현상 |
|---|---|
| η ~ MVN(0, Ω) | η-EBE histogram이 bimodal/skewed → 유전 다형성, 비선형 PK 미반영 (C4) |
| ε ~ N(0, Σ) | CWRES vs PRED plot에서 trumpet/funnel pattern → 오차 모델 오설정 (C2) |
| η ⊥ ε | 추정 시 OFV 발산, η-shrinkage 폭증 |
| f(·)가 모델 형태로 옳음 | 구조 모델 오류 — 1구획을 2구획에 적합 시 잔차에 systematic curvature |
| Sparse data 환자도 same population | Naive Pooled Data(NPD) 가정 동치 — 실제 outlier가 평균을 끌어당김 |

#### E. Limitations

- **NLME는 평균을 추정한다, 극단을 추정하지 않는다**. ω² = 0.08이라도 95% prediction interval은 매우 넓을 수 있고, FIH dose는 평균이 아닌 worst-case로 잡아야 한다.
- **Sparse data + high IIV**에서 ω²은 식별 불가능에 가까워진다. NONMEM은 그래도 숫자를 뱉지만 SE가 50%를 넘는다 (G&W §4.3.4 identifiability 논의 — V/F flip-flop과 동일한 구조적 식별성 문제가 ω²-σ² 사이에서도 발생한다).
- **NPD(Naive Pooled Data)**는 모든 데이터를 한 개인에게 속한 것처럼 적합하므로 IIV를 0으로 가정한 것과 같다. PK50 같은 12명 데이터에서 NPD를 쓰면 ω²(Cl) 28%가 ε에 흡수되어 σ² ≈ 0.08로 inflated됨.
- **Maximum likelihood + chi-squared LRT**: 두 nested 모델 비교 시 ΔOFV > 3.84 (df=1, α=0.05)면 통계적 유의. Non-nested 모델 비교에는 AIC 사용. `[출처: R&T 5e, Ch.12, p.373]`

#### F. Five Cognitive Layers

| L | Vol I (R&T / G&W) | Vol II (NONMEM 구현) |
|---|---|---|
| **L1 형식적 수학** | $Y_{ij} = f(\theta, \eta_i, x_{ij}) + g(\cdot)\varepsilon_{ij}$, log-normal IIV | `CL = THETA(1)*EXP(ETA(1))`, `$OMEGA 0.08` |
| **L2 기하학적 직관** | η는 인구 무게중심으로부터의 다차원 벡터 — Ω 행렬은 그 벡터 분포의 모양(공분산) | $OMEGA BLOCK(2) — Cl-V 상관 ρ가 ellipsoid의 기울기 |
| **L3 구조적 동형성** | Random effect ANOVA의 between-subject vs within-subject 분산 | Bayesian hierarchical model과 isomorphic — θ는 hyperprior, η는 individual prior |
| **L4 생리학적 의미** | $\omega^2(Cl)$ 28%는 간 효소 유전형 + 신기능 + plasma binding의 합산 분산 | $OMEGA BLOCK 안의 covariance는 "큰 간을 가진 사람은 큰 Cl과 큰 V를 동시에 가진다"는 생물학을 코딩 |
| **L5 실무 투영** | NDA section 6.2 PopPK report — ω², σ², shrinkage 표가 의무 | OMEGA block off-diagonal 정의, $COV step에서 SE 계산, η-EBE plot 제출 |

#### G. Zettelkasten Atom

```yaml
---
aliases: [IIV, BSV, mixed-effects taxonomy, η-ε orthogonality]
tags: [pharmacometrics/poppk, nonmem/syntax, statistics/nlme]
up: "[[PopPK MOC]]"
related: ["[[Residual Error Models]]", "[[η-shrinkage]]", "[[Covariate Modeling]]", "[[CYP polymorphism]]"]
source: "R&T 5e Ch.12, p.369-373; G&W 5e PK50 p.704-708"
---
```

NONMEM 혼합효과모델은 관측값 $Y_{ij}$를 $\theta$ (인구 평균, fixed), $\eta_i$ (개체 deviation, log-normal, $\omega^2$), $\varepsilon_{ij}$ (잔차, $\sigma^2$)의 세 자릿수로 분해한다. 세 자릿수는 직교 가정이 필수이며, 위반 시 η-shrinkage 또는 inflated ω²으로 표현된다. PK50 CpD 데이터에서 total Cl의 CV 28%는 unbound Cl의 9%와 fu 변이의 합산이며, 이 분해를 풀어내는 도구가 covariate model이다.

<!-- ANCHOR --> C1의 세 자릿수 taxonomy를 받아들였다면, 다음 질문은 자연스럽다 — **잔차 ε는 정확히 어떤 형태로 모델링되어야 하는가?** 잘못 잡으면 η가 ε로 흘러들어 covariate 신호 자체가 사라진다.

---

### C2. 잔차 오차 모델 (Residual Error) + Shrinkage [⚡ Apex Concept]

<!-- MASTER LENS -->
**[개념 Big Idea — 거장의 시각]**

1. **왜 치명적으로 중요한가**: 잔차 오차 모델을 잘못 선택하면 — 예를 들어 LLOQ 근처 데이터가 많은 Phase 1에 proportional error만 쓰면 — η가 ε로 흘러들어가 ω²(Cl)이 inflated되거나 반대로 η-shrinkage 50%가 발생해 covariate 모델 탐색이 통째로 무효가 된다. NDA Deficiency Letter 1순위 사유.

2. **체화해야 할 단 하나의 직관**: 잔차 오차 모델은 "내 측정 도구를 얼마나 믿는가"의 통계적 선언이다. **Additive는 LLOQ 근처에서 일정한 절대오차가 지배할 때, Proportional은 검출범위 내내 상대오차가 일정할 때, Mixed는 둘 다일 때.** 모델을 데이터에 맞추는 게 아니라 assay의 물리적 한계에 맞추는 것이다.

3. **이 직관을 머릿속에 박고 아래를 읽어라**: ε의 구조는 covariate 탐색보다 *먼저* 확정되어야 한다. 순서가 바뀌면 covariate 신호가 ε에 흡수된다.
<!-- /MASTER LENS -->

#### A. Formal Definition

가장 흔한 세 가지 잔차 오차 형태 (관측값 $Y$, 예측값 $F$):

| 모델 | 수식 | 가정 | 적합 상황 |
|---|---|---|---|
| **Additive** | $Y = F + \varepsilon$ | $\varepsilon \sim \mathcal{N}(0, \sigma^2_{add})$, 농도와 무관한 고정 절대오차 | LLOQ 근처 + low concentration range |
| **Proportional** | $Y = F\cdot(1 + \varepsilon)$ | $\varepsilon \sim \mathcal{N}(0, \sigma^2_{prop})$, 농도에 비례하는 상대오차 (CV 일정) | 광범위 농도 범위, log-linear assay |
| **Exponential** | $Y = F \cdot \exp(\varepsilon)$ | log-domain 가산오차 (Y > 0 보장) | log-transformed 데이터 분석 시 |
| **Mixed (Combined)** | $Y = F\cdot(1+\varepsilon_1) + \varepsilon_2$ | 두 가지 오차원 동시 | 광범위 농도 + LLOQ 근처 데이터 모두 포함 |

`[출처: R&T 5e, Ch.12, p.371-372 (Fig. 12-12, 12-13)]`

**중요한 동치성**: ln-transformation 시 exponential model은 additive로 변환된다 — $\ln Y = \ln F + \varepsilon$. 이것이 NONMEM에서 log-transform-both-sides (LTBS) 기법의 기반.

#### B. Derivation / Code Structure

**[NONMEM 코드 해부]**

```nmtran
$ERROR
IPRED = A(1) / V                        ; 개인 예측값

; --- 선택지 1: Proportional only (광범위 농도, LLOQ 안전 멀리) ---
Y     = IPRED * (1 + EPS(1))

; --- 선택지 2: Additive only (Phase 1 single dose, 모두 LLOQ 근처) ---
Y     = IPRED + EPS(1)

; --- 선택지 3: Mixed — 권장 default for Phase 2/3 ---
W     = SQRT( (IPRED*THETA(3))**2 + THETA(4)**2 )   ; SD model
Y     = IPRED + W*EPS(1)
;       prop CV (THETA(3)) + add SD (THETA(4))를 단일 EPS로 통합

; --- 선택지 4: Log-transformed (LTBS) ---
IPRED = LOG(A(1)/V + 1E-10)
Y     = IPRED + EPS(1)                  ; EPS(1) = log-domain SD
```

`[출처: PIPET Korean textbook series, NONMEM error model conventions]`

**왜 선택지 3이 default인가?** Mixed model의 W 식 ( $W = \sqrt{(IPRED \cdot \theta_3)^2 + \theta_4^2}$ ) 은 자연스럽게 농도가 클 때는 proportional이 지배하고, LLOQ 근처에서는 additive가 지배하는 매끄러운 전환을 만든다. 단일 모델이 양 극단을 모두 커버.

#### C. Structural Necessity

**왜 정확히 이 형태들인가?**

1. **Proportional이 그대로 농도에 곱해지는 이유**: bioanalytical assay (LC-MS/MS, ELISA)의 calibration curve는 통상 linear-linear 또는 linear-log이며, peak area의 SD가 농도에 비례한다 (heteroscedasticity). 이를 잔차에서 그대로 받아들이는 것이 proportional ε.

2. **Additive가 LLOQ 근처에서만 지배하는 이유**: LLOQ 근처에서는 baseline noise (machine noise, integration error)가 농도와 무관하게 일정한 절대값을 가진다. 농도가 LLOQ의 10배 이상일 때는 이 절대오차가 상대적으로 무시할 만해진다.

3. **왜 mixed가 둘의 단순합 SD가 아니라 quadrature sum인가?** 두 오차원이 독립이라는 가정 하에서, 분산은 가산되지만 SD는 √(분산 합)이다. 이것이 noise 합성의 근본 통계 법칙.

#### C-2. ⚡ Plausible Fallacy — η-shrinkage 의 그럴싸한 오해

**오류의 형태**:
> "내 모델의 η-EBE histogram이 종 모양이고 ω²(Cl) = 0.06 (CV 24%)로 합리적이다. 따라서 IIV가 잘 잡힌 것이다."

**왜 그럴싸한가**: η-EBE plot이 정규분포에 가깝게 생기면 모델이 잘 작동하는 것처럼 보인다. ω² 값도 PopPK 문헌의 평균 범위(20-40%)와 일치한다.

**실제 오류**: η-EBE의 분산이 ω²보다 훨씬 작아져 있다 — $\eta$-shrinkage = $1 - \frac{SD(\eta_{EBE})}{\omega}$. 이 값이 0.3 (30%)을 넘으면 EBE는 이미 인구 평균으로 끌려 들어간 상태다. 잔차 오차 모델이 잘못 잡혀 있을 때 (가령 proportional-only인데 데이터에 LLOQ 근처가 많을 때), conditional likelihood가 η를 0 쪽으로 강하게 끌어당겨 EBE 분포가 인공적으로 좁아진다.

**나비효과**:
- η-shrinkage > 30%인 상태에서 η_EBE vs covariate plot을 그리면 모든 점이 수평선에 모여 covariate 신호가 *시각적으로 사라진다*. Stepwise covariate selection 알고리즘이 진짜 covariate를 reject한다.
- ω²은 인구 수준에서는 여전히 합리적으로 추정되지만, 개인 EBE는 인구 평균에 shrink되어 — Bayesian TDM의 개인 dose adjustment가 무력화됨.

**진단 시그니처**: **"Vanishing Covariate Pattern"**
η_EBE vs body weight plot이 평탄한데 (slope ≈ 0), Cl_obs (NCA 추정) vs body weight plot은 강한 양의 상관을 보일 때. 이 불일치는 η-shrinkage의 직접 증거이며 covariate가 실재함에도 모델이 못 잡고 있다는 뜻.

`[출처: R&T 5e Ch.12, p.371-373 (residual variability section); Savic & Karlsson 2009 IIV shrinkage methodology]`

#### D. Assumptions & Boundary Conditions

| 가정 | 위반 시 |
|---|---|
| ε ~ N(0, σ²), zero mean | CWRES vs TIME plot에서 systematic offset → bias |
| 농도 범위 내 σ² 일정 (proportional 가정 시) | trumpet pattern in CWRES vs PRED → mixed model로 전환 |
| ε_ij ⊥ ε_ik (within-subject independence) | autocorrelation → AR(1) 잔차 도입 필요 (ICU 연속 sampling에서 발생) |
| LLOQ 처리 일관성 (M3 method) | LLOQ-bias가 ω²으로 전파 |

#### E. Limitations

- **잔차 오차 모델은 데이터-driven으로 정해지지 않는다**. Phase 1 단계에서 assay 특성과 sampling design을 보고 *prior*로 결정한 후, GOF 진단으로 검증하는 순서다. 데이터에 맞춰 깎아내면 overfitting.
- **η-shrinkage 진단은 ε-shrinkage와 동시에 봐야 한다**. ε-shrinkage > 20%면 GOF plot 자체가 불신.
- **LTBS는 Y > 0일 때만 가능**. BLQ(below LOQ) 데이터가 있으면 별도 처리 (M3 method).

#### F. Five Cognitive Layers (요약)

| L | Vol I 시각 | Vol II 구현 |
|---|---|---|
| L1 | $Y = F(1+\varepsilon)$ vs $Y = F + \varepsilon$ | `Y = IPRED*(1+EPS(1))` vs `Y = IPRED + EPS(1)` |
| L2 | trumpet vs funnel CWRES pattern | DV vs PRED plot의 spread shape |
| L3 | bioanalytical heteroscedasticity와 isomorphic | $SIGMA block 구조 |
| L4 | assay LLOQ + matrix effect의 통계적 표현 | sampling design의 PK 표현 |
| L5 | NDA QC plan의 잔차 분석 | `IGNORE=(BLQ.EQ.1)` vs M3 비교 |

#### G. Zettelkasten Atom

```yaml
---
aliases: [Residual Error, RUV, ε model, shrinkage]
tags: [pharmacometrics/poppk, nonmem/sigma, diagnostics/shrinkage]
up: "[[Mixed Effects Taxonomy]]"
related: ["[[η-shrinkage]]", "[[CWRES diagnostic]]", "[[LLOQ M3 method]]"]
source: "R&T 5e Ch.12, p.371-373; Savic-Karlsson shrinkage 2009"
---
```

잔차 오차 모델(additive/proportional/mixed)은 데이터가 아니라 assay의 물리적 한계와 sampling design에 맞추어 결정한다. Mixed model이 광범위 농도 범위에서 default이며, 단순 proportional만 쓰면 LLOQ 근처에서 η가 ε로 흘러들어 η-shrinkage > 30%가 발생, covariate signal이 시각적으로 사라진다. η-shrinkage > 30% + 깨끗한 η-EBE histogram 조합은 가장 위험한 false confidence 시그니처다.

<!-- ANCHOR --> C2의 잔차 모델이 안정되어야 비로소 다음 질문이 의미를 갖는다 — **ω²을 깎아 내리는 도구는 무엇인가?** 그것이 covariate 모델이다.

---

### C3. 공변량 모델링 — fu, CrCl as predictor of CL/V

<!-- MASTER LENS -->
**[개념 Big Idea — 거장의 시각]**

1. **왜 치명적으로 중요한가**: PK50의 CpD에서 fu를 covariate로 도입하지 않으면 ω²(Cl) = CV 28%로 보이지만, $Cl = f_u \cdot Cl_u$ 구조를 모델에 명시하면 ω²(Cl_u) = CV 9%로 줄어든다. 이 19%의 차이가 Phase 3 dose individualization 가능 여부를 결정한다 — fu를 측정해서 unbound 농도를 타겟팅하는 임상 알고리즘 vs 그저 total 농도 25 µg/L 평균 도징.

2. **체화해야 할 단 하나의 직관**: 공변량은 ω²을 깎아내는 끌이다. **깎인 자리에 생물학이 드러난다.** ω²(Cl) 28% → 9%로 줄었다는 것은 "환자 간 Cl 차이의 19% 분산이 사실은 fu 차이로 *설명되었다*"는 뜻 — 우연이 아니라 단백결합 메커니즘으로 환원된 것.

3. **이 직관을 머릿속에 박고 아래를 읽어라**: 공변량 도입은 모델의 자유도를 늘리는 것이 아니라 줄이는 것이다 — 한 차원의 변이가 covariate에 묶여 ω²에서 빠져나간다.
<!-- /MASTER LENS -->

#### A. Formal Definition

**Covariate model**: 인구 평균 PK 파라미터 $\theta$를 측정 가능한 환자 특성 $cov$ 의 함수로 명시:

$$
\theta_i \;=\; h(\theta_{pop},\; cov_i) \cdot \exp(\eta_i)
$$

대표적인 함수 형태:

| 형태 | 수식 | 적합 |
|---|---|---|
| **Linear** | $CL_i = (\theta_1 + \theta_2 \cdot CrCl_i)\cdot\exp(\eta_i)$ | 신청소율 등 직접 비례 |
| **Power** | $CL_i = \theta_1\cdot(WT_i/70)^{\theta_2}\cdot\exp(\eta_i)$ | Allometric scaling, $\theta_2 \approx 0.75$ |
| **Multiplicative** | $CL_i = \theta_1 \cdot f_{u,i}\cdot\exp(\eta_i)$ | PK50의 unbound clearance |
| **Categorical** | $CL_i = \theta_1\cdot(1 + \theta_2 \cdot SEX_i)\cdot\exp(\eta_i)$ | 이분형 covariate |

`[출처: R&T 5e Ch.12, p.369-371]`

#### B. Derivation / Code Structure — PK50 직접 적용

**G&W PK50 구조 (p.706, Eq. 50:2-50:4)** 는 fu를 공변량으로 명시한 multiplicative 모델의 교과서적 사례:

$$
CL = f_u \cdot CL_u, \qquad V_{ss} = f_u \cdot V_{u,ss}, \qquad CL_d = f_u \cdot CL_{du}
$$

즉, 측정 가능한 total 파라미터들이 unbound 파라미터들과 fu의 곱으로 정의됨.
`[출처: G&W 5e, PK50, Eq. 50:2-50:4, p.706]`

**핵심 데이터** (G&W Table 50.1, p.708):
- Total Cl mean = **11.4 L·h⁻¹**, CV = **28%**
- Unbound Cl_u mean = **720 L·h⁻¹**, CV = **9%**
- fu mean = 0.016 ± 0.0049 (CV ≈ **31%**)

**검증**: $CV(CL)^2 \approx CV(f_u)^2 + CV(CL_u)^2$ → $0.28^2 \approx 0.31^2 + 0.09^2$ → $0.078 \approx 0.096 + 0.008 = 0.104$.
오차 ~25% 이내, 두 분산이 거의 독립이라는 가정 하에서 합리적 일치.

**NONMEM 코드 (PK50 inspired)**:

```nmtran
$INPUT ID TIME AMT RATE DV FU MDV CMT
$DATA pk50.csv

$PK
TVCLU = THETA(1)                   ; unbound clearance population mean (L/h)
TVVCU = THETA(2)                   ; unbound central volume (L)
; ... 

CLU   = TVCLU * EXP(ETA(1))        ; ← unbound 파라미터에 IIV
VC    = TVVCU * EXP(ETA(2)) * FU   ; ← total volume = fu * unbound volume
CL    = CLU * FU                   ; ← total clearance = fu * unbound clearance
                                   ;   FU는 covariate (data column에서 입력)

$OMEGA
0.008                              ; ω²(Cl_u) ≈ CV 9%, PK50 unbound와 일치
0.032                              ; ω²(V_uc) ≈ CV 18%
```

여기서 핵심 통찰: **ETA는 unbound 파라미터에 붙고, fu는 data column으로 입력되는 covariate.** Total Cl의 변이(CV 28%)는 자동으로 $\sqrt{CV(f_u)^2 + CV(CL_u)^2}$로 합성되어 나타남.

#### C. Structural Necessity

1. **왜 covariate를 넣으면 ω²이 줄어드는가?** Variance decomposition 관점: 전체 변이 $\sigma^2_{total} = \sigma^2_{explained\;by\;covariate} + \sigma^2_{residual\;random}$. Covariate가 진짜 신호를 잡을수록 후자(=ω²)가 작아진다.

2. **왜 곱셈 형태(multiplicative)인가, 덧셈이 아니라?** $CL = f_u \cdot CL_u$는 *physiological identity* — 실제로 only unbound drug이 청소되며 total Cl은 그 효율의 fu 비율. 덧셈으로 쓰면 ($CL = \theta + f_u$) 단위가 안 맞고 fu = 0인 한계에서도 Cl > 0이 되는 비물리적 결과.

3. **왜 covariate 도입이 항상 좋은 것은 아닌가?** Covariate는 측정 비용·오차를 동반한다. fu 측정 자체가 CV 30%면 그 노이즈가 모델로 들어와 σ²을 키울 수 있다. Trade-off가 항상 존재.

#### D. Assumptions & Boundary Conditions

| 가정 | 위반 시 |
|---|---|
| Covariate가 측정 가능 + 측정 오차 작음 | fu 자체가 CV 30%면 covariate 신호와 noise가 섞임 |
| Covariate-PK 관계가 함수 형태 옳음 | linear에 power 관계가 숨어 있으면 잔차에 systematic curvature |
| Covariate들 간 상관 (multicollinearity) 없음 | WT과 BSA가 r=0.95면 둘 중 하나만 의미 있음, condition number 폭증 |
| Covariate가 시간에 따라 일정 또는 모델링됨 | 시간 가변 (TVCL with CrCl trajectory)는 별도 데이터 구조 |

#### E. Limitations

- **Covariate가 ω²을 0%까지 줄이지는 못한다**. 인간의 PK 변이의 상당 부분은 측정 불가능한 잠재 요인 (후성유전, 마이크로바이옴, 환경) 에서 온다.
- **Identifiability 문제 (G&W §4.3.4, p.348-350)**: covariate가 다른 PK 파라미터와 흡수 불가능한 형태 (V/F flip-flop과 동일 구조)로 모델링되면 ω²이 그 자리를 메운다.
- **PK50의 EC50 paradox** `[출처: G&W 5e, PK50, p.708]`: total EC50 (1.8 µg/L, CV 40%) 대비 unbound EC50 (0.029 µg/L, CV **60%**)에서 변이가 *증가*했다. 즉, fu가 PD에서는 covariate로 작동하지 않는다 — 약 8배의 response 변이는 plasma binding이 아닌 receptor density (genetic) 차이가 진짜 원인이라는 결론. *(이것이 §5의 confusion pair "PK covariate vs PD covariate" 의 출발점.)*

#### F. Five Cognitive Layers (요약)

| L | Vol I | Vol II |
|---|---|---|
| L1 | $CL_i = h(cov_i)\cdot\exp(\eta_i)$ | `CL = (THETA(1)+THETA(2)*CRCL)*EXP(ETA(1))` |
| L2 | ω²이 줄어드는 자리 = covariate가 설명한 분산 | η_EBE vs covariate plot의 slope |
| L3 | ANCOVA between-subject decomposition | Stepwise covariate selection (forward+backward) |
| L4 | 단백결합·신기능·체중·유전형이 covariate로 표현됨 | data column을 통한 인구 정보 주입 |
| L5 | label 권고 ("renal impairment dose adjustment") | regulatory PopPK report Table 4 |

#### G. Zettelkasten Atom

```yaml
---
aliases: [Covariate Modeling, fu as predictor, allometric scaling]
tags: [pharmacometrics/poppk, nonmem/covariate, regulatory/dose-adjustment]
up: "[[Mixed Effects Taxonomy]]"
related: ["[[Identifiability]]", "[[Stepwise Selection]]", "[[Allometry]]"]
source: "R&T 5e Ch.12, p.369-371; G&W 5e PK50 Eq. 50:2-50:4 p.706"
---
```

공변량은 ω²을 깎아내는 끌이며, 깎인 자리에 측정 가능한 생리학(fu, CrCl, WT, genotype)이 드러난다. PK50 CpD에서 fu를 multiplicative covariate로 도입하면 CV(Cl)이 28% → 9%로 줄어 unbound 농도 기반 dose individualization이 가능해진다. 그러나 PD covariate (EC50)에서는 동일 fu가 covariate로 작동하지 않으며 이것이 PK ≠ PD covariate의 핵심.

<!-- ANCHOR --> C3의 covariate가 ω²의 *연속적* 변이를 깎아낸다면, 다음 질문은 — **ω² 안에 *불연속적* 봉우리가 숨어 있다면?** 그것이 유전 다형성의 영역이다.

---

### C4. 유전적 다형성 — IIV의 불연속 substructure

<!-- MASTER LENS -->
**[개념 Big Idea — 거장의 시각]**

1. **왜 치명적으로 중요한가**: CYP2D6 PM(poor metabolizer) 환자에게 표준 nortriptyline 25 mg tid를 처방하면, 0개의 functional gene 보유자는 13개 보유자 대비 plasma concentration이 약 **5-10배 상승** (R&T Fig. 13-2)하여 cardiac toxicity 위험에 노출된다. 이 위험은 ω²의 평균값을 본 사람에게는 보이지 않는다 — bimodal 분포의 봉우리에 숨어 있다.

2. **체화해야 할 단 하나의 직관**: 유전 다형성은 ω²의 매끄러운 log-normal 분포 안에 숨어 있는 **봉우리들**이다. 평균 dose는 wild-type 봉우리에 맞춰져 있고, PM 봉우리에 사는 환자에게는 그 dose가 독약이 될 수 있다. **봉우리를 찾는 도구는 phenotyping 또는 genotyping; 그 결과는 categorical covariate로 모델에 들어간다.**

3. **이 직관을 머릿속에 박고 아래를 읽어라**: 유전형은 C3의 covariate model의 특수 사례 — *불연속(categorical) covariate* — 이며, 이를 빠뜨리면 ω²은 "biological mixture"를 한 봉우리로 평균낸 인공물이 된다.
<!-- /MASTER LENS -->

#### A. Formal Definition

**Genetic polymorphism**: 인구의 1% 이상이 DNA 특정 위치에서 다른 nucleotide(SNP) 또는 haplotype을 보유하는 상태. Allele frequency가 높을수록 인구 내 하위 봉우리(subpopulation peak)의 크기가 크다.
`[출처: R&T 5e Ch.13, p.394]`

**Hardy-Weinberg equilibrium**: 인구 내 두 allele 빈도가 $p, q$ ($p + q = 1$)일 때, 세 genotype (homozygous wild, heterozygous, homozygous variant)의 빈도는 $p^2, 2pq, q^2$.

**Phenotypic classification** (CYP2D6 예):

| Phenotype | Genotype 표기 | 빈도 (Caucasian) | Cl 변화 |
|---|---|---|---|
| Poor Metabolizer (PM) | 0 functional alleles | 5-10% | ↓↓ (예: nortriptyline에서 ~10% of EM) |
| Intermediate (IM) | 1 functional allele | ~30% | ↓ |
| Extensive (EM) | 2 functional alleles | ~50% | normal (wild) |
| Ultra-rapid (UM) | ≥3 functional copies | 1-3% | ↑↑ (예: codeine→morphine 형성 폭증) |

`[출처: R&T 5e Ch.13, Table 13-1, p.395; Dalén et al. 1998 Fig. 13-2 p.397]`

#### B. Derivation / Code Structure

**[Vol I 데이터 앵커링 — R&T 직접 인용]**

| Drug | 효소 | PM 빈도 | 임상 결과 |
|---|---|---|---|
| **Nortriptyline 25mg tid (263 환자)** | CYP2D6 | 5-10% Caucasian | 0 functional gene 보유 환자의 plasma C는 13 functional gene 보유자 대비 약 10배 (R&T Fig. 13-2, p.397; Dalén 1998). Plateau 농도 분포는 log-normal로 보이지만, 사실 multimodal mixture의 합 (Fig. 12-2, p.363) |
| **Warfarin maintenance** | CYP2C9 | 1-3% Caucasian | CYP2C9 *3/*3 환자의 주간 유지용량 중앙값이 *1/*1 대비 1/4 (R&T Fig. 13-4, p.398; Scordo 2002). 추가로 VKORC1 PD 다형성이 있어 ~43%만 유전형으로 설명됨 (Fig. 13-8, p.406) |
| **Isoniazid 9.8 mg/kg** | NAT2 | 50-60% Caucasian/Africal Am. slow / 10-20% Asian slow | 6h plasma 농도가 명확한 bimodal (R&T Fig. 13-6, p.402; Evans 1960). Slow acetylator는 peripheral neuropathy 위험 ↑ |
| **Mercaptopurine** | TPMT | 0.3% Caucasian (homozygous deficient) | Conventional dose 시 active thioguanine nucleotide 농도가 wild-type 대비 ~10배 → severe hematotoxicity. Genotype 후 ~80% 감량 시 안전 (Fig. 13-5, p.400) |
| **Abacavir** | HLA-B*5701 | 5-8% Caucasian | Hypersensitivity reaction (potentially fatal). Genotype screening이 contraindication 결정 |
| **Codeine → morphine** | CYP2D6 (UM) | 1% Caucasian, 28% North African | UM 모유 수유 산모에게 codeine 처방 시 영아 호흡억제 사망 보고. Contraindicated |

`[출처: R&T 5e Ch.13, Tables 13-1, 13-2; Figs. 13-2, 13-4, 13-5, 13-6]`

**[Vol II NONMEM 코드 — categorical covariate 도입]**

```nmtran
$INPUT ID TIME AMT DV PHENO MDV CMT
;     PHENO: 0=PM, 1=IM, 2=EM, 3=UM (CYP2D6 phenotype)

$PK
TVCL = THETA(1)
IF (PHENO.EQ.0) CLFAC = THETA(2)            ; PM: ~10% of EM
IF (PHENO.EQ.1) CLFAC = THETA(3)            ; IM: ~50% of EM
IF (PHENO.EQ.2) CLFAC = 1.0                 ; EM: reference
IF (PHENO.EQ.3) CLFAC = THETA(4)            ; UM: ~150-200% of EM

CL  = TVCL * CLFAC * EXP(ETA(1))            ; ETA = within-phenotype residual IIV
V   = THETA(5) * EXP(ETA(2))

$THETA
(0, 50)        ; TVCL_EM (L/h)
(0, 0.1)       ; PM factor
(0, 0.5)       ; IM factor
(0, 1.8)       ; UM factor
```

**핵심 통찰**: 유전형 covariate를 도입하면 ω²(Cl)은 "PM이라는 사실"이 가지는 큰 분산을 흡수하고, 남은 ETA(1)은 *같은 phenotype 안에서의* 잔차 IIV만 잡는다. 통상 ω²이 30-40% → 15-20%로 줄어든다.

`[출처: PIPET Korean textbook, NONMEM categorical covariate convention]`

#### C. Structural Necessity

1. **왜 binomial distribution인가?** 한 사람은 두 chromosome으로부터 두 개의 allele를 받는다. Allele frequency $p, q$ 하에서 genotype 빈도는 $p^2, 2pq, q^2$ — 이항분포의 직접 결과 (Hardy-Weinberg).

2. **왜 phenotype 효과가 곱셈형(multiplicative)인가?** 효소량의 차이는 typically 곱셈으로 작동 — PM의 Cl이 EM의 10%면 그 비율은 dose에 무관하게 유지된다. 단, Michaelis-Menten 비선형 영역에서는 multiplicative 가정이 깨진다.

3. **왜 일부 phenotype은 dominant, 일부는 recessive인가?** 효소 활성이 dosage-dependent (한 functional copy로도 충분)이면 PM이 recessive (q² 빈도). 효소가 dimer로 작동하거나 protein-protein interaction에 민감하면 heterozygous도 영향 → IM phenotype 등장.

#### D. Assumptions & Boundary Conditions

| 가정 | 위반 시 |
|---|---|
| Phenotype-Cl 관계가 monotonic | UM의 codeine→morphine처럼 prodrug+UM 조합에서는 비단조 |
| Phenotype 측정이 정확 | DNA-based genotype은 phenotype과 95-97.5% 일치 (R&T p.407) — 일부 미스매치는 epigenetic regulation |
| 한 효소만 dominant | CYP3A4가 CYP2D6와 overlap 시 다중 isoform 모델 필요 |
| Wild type이 reference | Population에 따라 wild type frequency 자체가 다름 (CYP2D6 빈도 표 참조) |

#### E. Limitations

- **Phenotype은 dose individualization을 항상 가능하게 하지는 않는다**. R&T Fig. 13-9 (p.408) — CYP2D6, CYP2C19, CYP2C9, TPMT, NAT2 별로 dose adjustment factor가 표준화되어 있으나, intra-phenotype 변이가 여전히 30-50%이므로 TDM이 보완 필요.
- **VKORC1 + CYP2C9 + 비유전 covariate가 합쳐도 warfarin 유지용량 변이의 ~62%만 설명** (R&T Fig. 13-8). 38%는 여전히 미해명 — adherence, 식이, vitamin K 섭취 등.
- **Ethnicity는 phenotype의 proxy일 뿐**, 정확한 marker가 아니다. R&T 강조: "within each ethnic group, there is often almost as much interindividual variability as between the groups" (p.395).

#### F. Five Cognitive Layers (요약)

| L | Vol I | Vol II |
|---|---|---|
| L1 | $p^2 + 2pq + q^2 = 1$ Hardy-Weinberg | `IF (PHENO.EQ.x) CLFAC = THETA(y)` |
| L2 | ω² 분포의 multimodal 봉우리 | η_EBE histogram의 bimodality |
| L3 | enzyme dosage genetics ≅ Mendelian inheritance | mixture model in NONMEM |
| L4 | CYP2D6 amount/activity의 인구 분산 | activity score (AS): 0/0.5/1/1.5/2/3 시스템 |
| L5 | FDA Pharmacogenomic Biomarker label (>200 drugs) | `$MIX` block (mixture model) — phenotype 미측정 시 |

#### G. Zettelkasten Atom

```yaml
---
aliases: [pharmacogenetics, CYP polymorphism, IIV discrete substructure, phenotype]
tags: [pharmacometrics/genetics, nonmem/categorical-covariate, regulatory/labeling]
up: "[[Covariate Modeling]]"
related: ["[[CYP2D6]]", "[[CYP2C9-VKORC1 warfarin]]", "[[TPMT mercaptopurine]]", "[[HLA-B*5701 abacavir]]"]
source: "R&T 5e Ch.13, p.393-410; PIPET NONMEM categorical covariate"
---
```

유전 다형성은 ω²의 log-normal 분포 안에 숨은 multimodal 봉우리이며, categorical covariate (PM/IM/EM/UM)로 모델에 도입하면 봉우리 간 분산이 covariate에 흡수되고 ω²은 within-phenotype residual variation만 잡는다. CYP2D6 (nortriptyline ~10배 차이), CYP2C9+VKORC1 (warfarin ~4배 dose 차이), TPMT (mercaptopurine ~10배 toxicity 차이), HLA-B*5701 (abacavir hypersensitivity)는 genotype-guided dosing의 표준 사례.

---

## §5 — Confusion Pair Dissection

<!-- CONFUSION -->
### Pair 1: ω² (IIV) vs σ² (RUV) — **[Critical Blow 적용]**

| 비교 차원 | ω² (IIV) | σ² (RUV) |
|---|---|---|
| **표면적 유사성** | *둘 다 NONMEM `$OMEGA`/`$SIGMA`로 선언되는 분산 파라미터, 단위가 비슷해 보임 — η와 ε가 둘 다 "random effect"로 불림* | |
| **수식 형태** | $\eta_i \sim \mathcal{N}(0, \omega^2)$ — 한 환자의 일생 동안 *고정*된 deviation | $\varepsilon_{ij} \sim \mathcal{N}(0, \sigma^2)$ — 같은 환자의 매 측정마다 *다른* noise |
| **생리학적 지시체** | 환자 간 효소량·체구·신기능·유전형의 차이 (=biology) | Assay precision, sampling time error, prandial effect (=measurement) |
| **변화 방향** | 환자 1명의 ω²은 정의되지 않음 — population에서만 의미. 시간 무관. | 환자 1명의 ε는 매 sample마다 새로 추첨. 시간에 무관 (correlation 가정 없을 때) |
| **임상 결과** | ω²(Cl) = CV 30%면 환자별 dose 조정이 필요 (TDM 가치 ↑) | σ²(prop) = 15%면 single sample TDM 결과가 ±30% 범위에 있을 수 있음 (TDM 정확도 ↓) |
| **⚡ 기억 고리** | **"ω는 환자 인쇄지문, σ는 사진 찍을 때마다 다른 그림자."** 인쇄지문은 그 사람의 평생 속성, 그림자는 매 측정마다 새로 생긴다. ω를 σ로 오분류하면 "인쇄지문이 그림자다"라고 말하는 격 — 환자 개별성을 부정하는 것. | |
| **🚨 Critical Blow** | **NDA section 6.2 PopPK report에서 ω²(Cl) 28%를 "residual variability"로 기재해 제출하면, FDA Deficiency Letter에서 "Submission incorrectly conflates between-subject variability with measurement error, invalidating the proposed dose individualization rationale (21 CFR 314.50)" 사유로 모델 전체 reject. 18-24개월 재제출 지연 + 시장 진입 손실 추정 USD 200-500 million.** | |

<!-- /CONFUSION -->

<!-- CONFUSION -->
### Pair 2: Total Cl vs Unbound Cl_u (PK50 anchored)

| 비교 차원 | Total Cl | Unbound Cl_u |
|---|---|---|
| **표면적 유사성** | *둘 다 단위가 L/h, 둘 다 "clearance"로 불림* | |
| **수식** | $CL = f_u \cdot CL_u$ → CpD 11.4 L/h | $CL_u = CL/f_u$ → CpD **720 L/h** |
| **생리학적 지시체** | Total drug 제거 속도 (total plasma 농도 기준) | Unbound drug의 enzyme/transporter 효율 — 진짜 효소 활성을 반영 |
| **변화 방향 (fu 변화 시)** | fu ↓ → Cl ↓ (total) — 약물이 더 많이 묶이면 total 청소 ↓ | fu 변화 무관 — Cl_u는 효소 자체의 본성 |
| **PK50 변이 (CV%)** | **28%** | **9%** |
| **임상 결과** | Total 농도 50 µg/L 안전 한계 | Unbound 0.029 µg/L EC50 — 진짜 약효 결정 |
| **⚡ 기억 고리** | **"Cl은 단백 도매가, Cl_u는 효소 효율의 순도(純度)."** 도매가는 단백 비율(fu)이라는 시장 환율에 흔들리지만, 순도는 그 환율과 무관한 약물의 본질이다. PK50의 CV가 28% → 9%로 줄어드는 것은 환율 효과를 제거하면 효소 효율의 진짜 변이가 작다는 뜻. | |

<!-- /CONFUSION -->

<!-- CONFUSION -->
### Pair 3: Additive vs Proportional Residual Error

| 비교 차원 | Additive | Proportional |
|---|---|---|
| **표면적 유사성** | *둘 다 NONMEM `$ERROR` 블록의 한 줄, 둘 다 EPS(1)로 선언* | |
| **수식** | $Y = F + \varepsilon$, $\varepsilon \sim \mathcal{N}(0, \sigma^2_{add})$ | $Y = F\cdot(1+\varepsilon)$, $\varepsilon \sim \mathcal{N}(0, \sigma^2_{prop})$ |
| **물리적 지시체** | 농도와 무관한 절대 SD (e.g., baseline noise 0.1 µg/mL) | 농도에 비례하는 상대 SD (e.g., assay CV 15%) |
| **CWRES vs PRED 패턴** | 저농도에서 큰 spread, 고농도에서 작은 spread (퍼지가 좁아짐) | 모든 농도에서 일정한 spread (균등) |
| **언제 잘못 선택했나?** | Phase 3 광범위 농도 데이터에 additive만: 고농도 점 weight 과다 | Phase 1 LLOQ 근처 데이터에 proportional만: 저농도 점에서 음수 예측 가능, η-shrinkage 폭증 |
| **⚡ 기억 고리** | **"Additive는 자(尺) 눈금의 두께, Proportional은 자 자체의 휨."** 자 두께는 어디서 재든 일정 (LLOQ 근처에서 지배), 자의 휨은 길이에 비례 (광범위 농도에서 지배). LLOQ 근처에 데이터가 몰리면 자 두께가 보이고, 광범위 농도면 자 휨이 보인다. 둘 다 있을 때는 mixed (quadrature sum). | |

<!-- /CONFUSION -->

<!-- CONFUSION -->
### Pair 4: NAD vs NPD vs Population Approach

| 비교 차원 | NAD (Naive Averaged Data) | NPD (Naive Pooled Data) | Population Approach (NLME) |
|---|---|---|---|
| **표면적 유사성** | *셋 다 multi-subject 데이터에 한 모델을 적합* | | |
| **방법** | 각 시점별 평균 농도 계산 → 평균 곡선 적합 | 모든 환자 데이터를 한 환자처럼 풀에 → 한 곡선 적합 | 각 환자의 개별성(η)을 인구 평균(θ)으로부터의 deviation으로 동시 추정 |
| **IIV 추정** | 불가능 (정보 손실) | 불가능 (IIV가 ε에 흡수) | 가능 ($\omega^2$로 명시 추정) |
| **편향** | mean-data fitting의 systematic bias (G&W p.335) | outlier가 평균을 강하게 끌어당김 | 적절히 적용 시 unbiased |
| **언제 작동하나?** | n이 매우 크고 모든 환자가 같은 sampling time | sparse data, IIV가 작다고 *가정* 가능할 때만 | sparse data + 합리적 IIV — modern PopPK의 default |
| **⚡ 기억 고리** | **"NAD는 사진 평균, NPD는 사진 풀(pool), NLME는 사진첩."** 사진 평균은 모든 사람을 한 얼굴로 흐리게 만들고, 사진 풀은 모두를 한 사람인 양 본다. 사진첩은 각자를 보존하면서도 가족 사진 (population)의 공통점을 함께 본다. | | |

<!-- /CONFUSION -->

---

## §7 — Self-Test: Active Recall Module

<!-- SELF-TEST -->

**Q1 (★★ 회상)**: NONMEM 혼합효과모델에서 $Y_{ij} = f(\theta, \eta_i, x_{ij})\cdot(1 + \varepsilon_{ij})$로 표기될 때, $\theta$, $\eta_i$, $\varepsilon_{ij}$가 각각 무엇을 의미하며 어떤 분포 가정을 가지는지 한 줄씩 서술하라.

> **정답**: $\theta$ = fixed effect, 인구 평균 PK 파라미터, scalar (e.g., $\theta_{CL}$ = 11.4 L/h). $\eta_i$ = between-subject random effect, 개인 i의 인구 평균으로부터의 log-normal deviation, $\eta_i \sim \mathcal{N}(0, \omega^2)$. $\varepsilon_{ij}$ = residual error, 개인 i의 j번째 측정의 잔차, $\varepsilon_{ij} \sim \mathcal{N}(0, \sigma^2)$. 가정: $\eta_i \perp \varepsilon_{ij}$.
>
> **다음 깊이 질문**: 만약 $\eta_i$와 $\varepsilon_{ij}$가 직교하지 않다면 (음의 상관) 모델 추정에서 어떤 일이 발생하는가?

---

**Q2 (★★ 회상 + 적용)**: G&W PK50의 CpD 데이터에서 total Cl의 mean = 11.4 L/h, CV = 28%이고, fu mean = 0.016, CV = 31%이다. Unbound Cl_u의 평균과 CV를 계산하라. 두 변량이 독립이라고 가정.

> **정답**: $CL_u = CL/f_u = 11.4 / 0.016 = 712.5 \approx 720$ L/h (Table 50.1 unbound Cl과 일치).
> CV: $CV(CL)^2 \approx CV(f_u)^2 + CV(CL_u)^2$ → $0.28^2 = 0.31^2 + CV(CL_u)^2$ → $CV(CL_u)^2 \approx 0.078 - 0.096 = -0.018$.
>
> 결과가 음수가 나오는 것은 두 변량이 *완전 독립*이 아니라 약한 음의 상관이 있을 가능성을 시사하지만, 표에서는 unbound CL_u CV = 9%로 보고. 이 차이는 (a) Cl과 fu가 완전히 독립이 아닐 수 있음, (b) propagation formula가 lognormal에 대해 근사임, (c) 실제 추정은 NONMEM의 simultaneous estimation에서 직접 나온 값임을 반영.
>
> **다음 깊이 질문**: 이 9% (CV of Cl_u)가 진짜 unbound clearance 변이의 하한인가, 아니면 fu 측정 오차가 일부 흡수된 것인가?

---

**Q3 (★ 회상)**: R&T Fig. 13-2 (Dalén 1998)에서, 0개 functional CYP2D6 gene을 가진 환자(PM)의 nortriptyline plasma 농도가 13개 functional gene을 가진 환자(UM)의 약 몇 배인가? 이 ratio는 single dose 25 mg을 투여한 후 측정.

> **정답**: 약 10배 이상. PM의 24h plasma 농도는 ~12 µg/L 수준, UM은 ~1 µg/L 수준 (Fig. 13-2). 정확한 ratio는 functional gene 수에 거의 직접 비례.
>
> **다음 깊이 질문**: 이 10배 차이가 ω²(Cl)에 어떻게 반영되며, CYP2D6 phenotype을 categorical covariate로 모델에 넣으면 ω²이 얼마나 줄어드는가?

---

**Q4 (○ 적용)**: 한 환자의 CWRES vs PRED plot에서 저농도 영역에서는 spread가 ±5인데 고농도 영역(>10 µg/L)에서는 spread가 ±2로 좁아진다. 잔차 오차 모델은 어떻게 수정해야 하는가?

> **정답**: 현재 모델이 additive only일 가능성이 높다. 저농도에서 spread가 크고 고농도에서 작아지는 것은 absolute SD가 일정하다는 additive 가정과 일치 — 그러나 *데이터*가 고농도에서 더 작은 spread를 보인다면 sigma^2_add가 너무 크게 추정되어 고농도 점이 over-shrunk되고 있다. Mixed model로 전환:
>
> ```nmtran
> W = SQRT( (IPRED*THETA(N))**2 + THETA(M)**2 )
> Y = IPRED + W*EPS(1)
> ```
>
> proportional 부분이 광범위 농도에서, additive 부분이 LLOQ 근처에서 지배하도록.
>
> **다음 깊이 질문**: 이 모델 변경 후 ω²(Cl)이 변하지 않는다면 어떤 결론이 가능한가? (Hint: orthogonality)

---

**Q5 (★ 적용)**: PK50의 EC50이 total 1.8 µg/L, unbound 0.029 µg/L로 보고되었다. CV는 total 40%, unbound **60%** — 즉 unbound로 변환하니 변이가 *증가*했다. 이를 어떻게 해석하는가?

> **정답**: fu가 PK 파라미터 (Cl, V)에서는 covariate로 작동했지만 (CV 28% → 9%), PD 파라미터 (EC50)에서는 *negative* covariate effect를 가진다 — 즉 fu 변이를 보정하니 다른 진짜 PD 변이원이 드러났다. R&T/G&W 결론: receptor density (genetic)이 진짜 원인이며 plasma binding은 PD에 부적절한 covariate. 8배 response 변이 (0.5-4.0 unit)의 진짜 메커니즘은 receptor expression이며, fu는 이를 가렸을 뿐.
>
> **다음 깊이 질문**: 이 인구를 responder (Emax > 1)와 non-responder (Emax < 1)로 mixture model로 모델링하면 어떤 추가 정보를 얻을 수 있는가?

---

**Q6 (○ 적용)**: 한 PopPK 분석 보고서에서 다음과 같이 적혀 있다: "ω²(Cl) = 0.06 (CV 24%), η-shrinkage(Cl) = 5%, η-EBE histogram은 정규성을 보임. 따라서 모델이 well-specified다." 이 결론에 동의하는가?

> **정답**: 부분 동의. ω²과 shrinkage 자체는 양호하나 (5%는 매우 낮음), η-EBE의 정규성은 *유전 다형성을 잡지 못한* 인공물일 수 있음 — 만약 인구의 5%가 CYP2D6 PM이고 그들의 ETA(1)이 -2.3 (즉 Cl이 평균의 10%)에 몰려 있다면, n이 작을 때 histogram이 여전히 종 모양으로 보일 수 있다 (왜도 약함). 진단:
> (a) η_EBE vs phenotype label scatter (있다면) → bimodal cluster 확인
> (b) NPDE plot에서 outlier cluster 확인
> (c) Mixture model (NONMEM `$MIX`)로 2-population 적합 후 OFV 비교
>
> **다음 깊이 질문**: 만약 phenotype 정보가 데이터에 없다면, mixture model로 phenotype을 *역추정*할 수 있는가?

---

**Q7 (★ 적용)**: warfarin maintenance dose의 인구 변이의 약 60%가 CYP2C9 + VKORC1 + age + weight의 합으로 설명되고 38%가 미해명으로 남는다 (R&T Fig. 13-8). 이 38%를 ω²으로 흡수하고 모델을 종결하는 것이 합리적인가, 아니면 추가 covariate 탐색을 계속해야 하는가?

> **정답**: 두 측면 모두 옳을 수 있다. (a) 추가 탐색이 합리적인 경우: 38%는 큰 분산이며 vitamin K dietary intake, drug-drug interaction (특히 amiodarone, fluconazole), adherence가 주요 후보. 이 중 dietary K는 측정 가능. (b) ω²으로 흡수가 합리적인 경우: 라벨이 이미 INR-guided titration을 권장하고 있어 dose individualization이 PK 모델보다 PD measurement (INR) 기반으로 작동. 추가 covariate가 라벨 변경 가치를 만들지 못하면 비용 대비 효용 ↓.
>
> 거장의 입장: 일단 measurable + actionable한 covariate (예: amiodarone 동시 투여)를 더 잡고, 나머지 25-30%는 ω²으로 잔류시키되 보고서에 "INR-guided dose titration is recommended in routine clinical practice"로 명시.
>
> **다음 깊이 질문**: ω²의 "irreducible 하한" 같은 것이 존재하는가? (Hint: assay precision, sampling sparsity)

---

**Q8 — 보스 딜레마 (Socratic Dilemma) ★★**

> 당신은 신약 X (CYP2D6 substrate, narrow therapeutic window — total plasma C < 50 µg/L 권장)의 NDA Phase 3 PopPK 분석을 마쳤다. 현재 상태:
>
> - **모델 A (현재)**: Proportional-only RUV. ω²(CL) = 0.08 (CV 28%), σ²_prop = 0.02 (CV 14%). η-shrinkage(CL) = **42%**. Conditional weighted residuals (CWRES) plot에서 LLOQ 근처(< 1 µg/L) 영역에 systematic positive bias (CWRES mean = +1.8). η_EBE vs CYP2D6 phenotype scatter에서 PM 5명 모두 0 근처에 모여 있어 phenotype 효과가 시각적으로 사라짐.
>
> - **선택 A**: 현 모델 그대로 NDA 제출. CWRES bias는 "expected behavior at low concentration" 으로 보고서에 기술. CYP2D6 dose adjustment recommendation 없음.
>
> - **선택 B**: Mixed RUV (additive + proportional)로 변경 후 재추정. 통계 부서 일정 2주 지연. 만약 η-shrinkage가 < 15%로 떨어지고 PM 5명이 ETA(1) ≈ -2.0에 명확히 분리되면, CYP2D6-guided dose adjustment 추가 → 라벨에 "Reduce dose by 75% in CYP2D6 PM" 권고.
>
> 어느 쪽을 택하는가? FDA Deficiency Letter 응답에서 어떻게 방어하는가?
>
> ---
>
> **수석 모델러의 Trade-off 논리**:
>
> **선택 B가 명백한 우위**. 근거:
>
> 1. **Regulatory 측면**: η-shrinkage 42%는 ICH E14 / FDA Population PK Guidance에서 명시한 "shrinkage > 30% impairs interpretation of η-based covariate identification" 직접 위반. 선택 A로 제출 시 Deficiency Letter 가능성 90% 이상 — 그 시점에서 Mixed RUV 재추정 + 추가 covariate 분석이 반드시 요구되며, 결국 선택 B를 *강제로* 하게 됨. 단, 그 시점에는 라벨이 이미 만들어진 후이므로 라벨 수정 필요 → 6-12개월 추가 지연.
>
> 2. **임상 측면**: PM 5명의 CYP2D6 phenotype 효과를 모델이 못 잡고 있다는 것은 — 만약 약물이 narrow therapeutic window라면 — 시판 후 PM 환자 5-10%가 toxic 농도에 노출될 위험을 라벨이 경고하지 못한다는 뜻. Post-marketing pharmacovigilance에서 SAE (Serious Adverse Event) cluster 발생 시 black box warning 또는 시판 중지 risk.
>
> 3. **통계적 측면**: 선택 A의 σ²_prop = 14%는 사실 *η가 ε로 흘러들어간* artifact일 가능성. Mixed RUV로 가면 σ²이 더 작아지고 ω²이 정확히 잡히면서 모델이 *전체적으로* 더 짧고 강해진다.
>
> **FDA 응답 prepared statement 예시**:
> > "The initial proportional-only RUV model exhibited η-shrinkage of 42% on CL, which precluded reliable identification of CYP2D6 phenotype as a covariate via η_EBE diagnostics. Following revision to a mixed (additive + proportional) RUV structure consistent with the bioanalytical assay's heteroscedasticity profile and LLOQ characteristics, η-shrinkage decreased to 12%, revealing a clear bimodal distribution of CL between PM (0.10·CL_typical) and EM/IM populations. Dose adjustment recommendations are now provided in Section 2.6 of the proposed label."
>
> **단, 선택 A를 정당화하는 시나리오 (드물지만 존재)**:
> - 시간이 절대적으로 부족하고 (예: competitor 진입 임박)
> - PM 환자의 임상적 위험이 명백히 낮으며 (predominantly mild AE only)
> - Post-marketing commitment로 large simple trial을 약속하여 PM cohort 별도 분석을 약정한 경우
>
> 이 경우에도 보고서에 "η-shrinkage of 42% limits the interpretability of the current model with respect to CYP2D6 phenotype effects; this will be addressed in the post-marketing PK study (Study X-501)"라고 명시적으로 적시 필요.

<!-- /SELF-TEST -->

---

## §8 — Meta-Frame & Big Picture

### A. Positioning — 28-세션 지식 아키텍처

```
            [ Session 1-5: 기초 PK ]
                       ↓
            [ Session 6-9: NCA, 1·2구획 ]
                       ↓
            [ Session 10: Hepatic Clearance + fu ]
                       ↓
            [ Session 11: NONMEM 데이터셋 (II-02) ]
                       ↓
            [ Session 12: General ADVAN/$DES (II-04) ]
                       ↓
            ★ [ Session 13: IIV/BSV/Covariates ] ★ ← 현 위치
                       ↓
            [ Session 14: FOCE/FOCE-I 추정 알고리즘 ]
                       ↓
            [ Session 15: GOF 진단 (CWRES, NPDE, η/ε-shrinkage) ]
                       ↓
            [ Session 16: Stepwise Covariate Modeling ]
                       ↓
            [ Session 17: Bayesian TDM + EBE 활용 ]
                       ↓
        [ Sessions 18-28: TMDD, PBPK, QSP, 규제 보고 ]
```

이 세션은 **분산 축의 정초**이며, 이후 모든 추정 알고리즘·진단·covariate 선택·개인화 도징은 본 세션의 θ/η/ε taxonomy를 *전제*한다.

### B. Dependencies — 대충 넘겼을 때 발생하는 실패 모드

1. **FOCE-I 추정에서 OFV 발산**: η와 ε의 직교 가정을 이해하지 못하면, full block ω² 행렬을 잘못 정의해 추정 자체가 수렴하지 않음. 일주일을 버려도 이유를 모름.

2. **Covariate selection에서 진짜 covariate가 reject됨**: η-shrinkage 진단 없이 stepwise를 돌리면, shrunk EBE에서 모든 covariate가 통계적으로 유의하지 않게 보여 "no covariate model" 결론. 실제로는 RUV 모델 오설정으로 신호가 묻혀 있는 것.

3. **Bayesian TDM 알고리즘 무력화**: 환자 1-2 sample로부터 EBE를 계산해 dose 조정하는 임상 algorithm은, ω²과 σ²이 잘못 분리되어 있을 때 EBE 자체가 인구 평균에 끌려가 single-sample 정보가 작동하지 않음.

4. **유전 다형성 누락 → 시판 후 SAE cluster**: ω²이 mixture distribution을 가린 인공물일 때, 일부 phenotype 환자에게 평균 dose가 toxic. Black box warning 또는 시장 철수.

5. **CONTEXT 흡수**: 본 세션의 ω²은 약물 외 변이 (food-drug, herbs, adherence, chronopharmacology)까지 모두 흡수하는 그릇이다. ε로 새는 주범이 이들이며, 이를 모르면 잔차 진단이 영원히 막힌다.

### C. Professional Moat — 이 세션 내용에 직접·구체적으로

> **Vol I + Vol II 결합 프레임**:
>
> NONMEM control stream을 작성하고 OFV가 떨어졌음을 확인하는 것은 자동화 가능하다. PopPK 보고서 template에 ω², σ², shrinkage 표를 채우는 것도 마찬가지다. AI는 이미 PK50 데이터에 2-구획 모델을 적합할 수 있다.
>
> 그러나 다음을 *구조적 필연성 수준*에서 내면화한 모델러만이 할 수 있는 것:
>
> 1. **"η-shrinkage 42% + 깨끗한 η_EBE histogram"이라는 false confidence 시그니처를 의심하고**, 그것이 잔차 오차 모델 오설정의 직접 증거임을 *처음 보는 보고서에서 즉시 식별*하는 것.
>
> 2. **PK50의 EC50 변이가 total → unbound로 갈 때 *증가*했다는 사실에서**, fu가 PK covariate이지만 PD covariate가 아니라는 결론과, 진짜 PD 변이원이 receptor density genetic polymorphism일 가능성을 *데이터에서 직접 읽어내는* 것.
>
> 3. **"우리 약물은 CYP2D6 substrate인데 PM 환자에서 dose adjustment data가 없다"는 NDA 상황에서**, mixture model로 phenotype을 역추정하고 5명의 cluster를 ETA(1) ≈ -2.0에 분리해 라벨에 "Reduce dose by 75% in CYP2D6 PM" 권고를 *post-hoc analysis로* 만들어내는 것.
>
> 4. **Deficiency Letter의 "shrinkage > 30% impairs covariate identification" 사유를** 그저 받아들이는 것이 아니라, 그 진술의 통계적 메커니즘 (η가 conditional likelihood 하에서 0으로 끌려가는 과정)을 첫 원리에서 재구성하여 응답을 작성하는 것.
>
> 5. **"warfarin 변이의 38%가 미해명으로 남는다"는 한계에서**, 그것을 ω²에 흡수시키되 라벨에 "INR-guided titration"을 명시하는 결정 — 즉, 모델의 한계를 임상 모니터링으로 *우회*하는 규제 전략을 설계하는 것.
>
> 이 다섯 가지는 모두 본 세션의 taxonomy (θ/η/ε), 잔차 오차 모델, covariate 도입 메커니즘, 유전 다형성의 mixture 구조를 *연결된 한 시스템*으로 보는 사람만 할 수 있다. 이것이 동기 부여가 아닌, 구조적 필연 수준에서의 professional moat이다.

<!-- RECAP -->
**§8 Recap**: 본 세션은 PopPK 커리큘럼의 분산 축 정초이며, θ/η/ε의 직교 분해, 잔차 오차 모델의 정확한 설정, covariate 모델을 통한 ω² 깎아내기, 유전 다형성을 통한 ω² 안 봉우리 발견의 4단 stack을 형성한다. 이후 모든 PopPK 작업이 이 stack 위에 세워진다.
<!-- /RECAP -->

---

```
---
✦ STEP 1 완료.

다음이 준비되었습니다:
  • §1 세션 헤더 & 로드맵 (28-세션 지식 그래프 위치 명시)
  • §2 개념 해부 카드 (4개 MUST 개념, Apex: C2 잔차 오차 모델 + Shrinkage)
       C1. 변이의 구조적 분해 (θ/η/ε taxonomy)
       C2. 잔차 오차 모델 + Shrinkage [⚡ Apex Concept]
       C3. 공변량 모델링 (fu as predictor, PK50 anchored)
       C4. 유전적 다형성 (IIV의 불연속 substructure)
  • §5 혼동 쌍 해부 (4개 쌍, Critical Blow 적용: ω² vs σ²)
       Pair 1: ω² vs σ² (IIV vs RUV)  ← Critical Blow
       Pair 2: Total Cl vs Unbound Cl_u
       Pair 3: Additive vs Proportional Residual Error
       Pair 4: NAD vs NPD vs Population Approach
  • §7 자기 테스트 (8개 질문, Q8 보스 딜레마: NDA Mixed RUV vs Proportional-only 선택)
  • §8 메타프레임 & 빅 픽처
  • 감지된 소스 유형: 혼합 (Vol I — R&T Ch.12+13 임상·생리학; G&W Ch.4+PK50 데이터·수치)
  • Data Anchoring 소스: 
       G&W PK50 — CpD 566 µg/5h IV, 12명 antiarrhythmic, Cl=11.4 (CV28%)/Cl_u=720(CV9%), 
                    Vc=19.9/Vt=30.9, fu=0.016±0.0049, EC50 total 1.8/unbound 0.029,
                    8배 response 변이 (0.5-4.0 units)
       R&T Ch.12 — nortriptyline 25mg tid 263명, warfarin 200명 dose range, 
                    theophylline 350mg 5명, propranolol 10mg IV/80mg PO 5명
       R&T Ch.13 — CYP2D6 (Dalén 1998 nortriptyline 0/1/2/3/13 functional genes), 
                    CYP2C9*1-*3 + VKORC1 warfarin (Scordo 2002), TPMT mercaptopurine 
                    (Evans), NAT2 isoniazid 9.8mg/kg bimodal (Evans 1960), HLA-B*5701 abacavir

"계속"을 입력하면 Step 2 HTML 컴파일러가 실행됩니다.
Step 2는 위 내용 전체(§1·§2·§5·§7·§8) +
§3(구조적 동형성 지도 — ω²/σ² 분해 ↔ ANOVA between/within ↔ Bayesian hierarchical) +
§4(인터랙티브 시뮬레이터 — fu slider로 PK50 ω²(Cl) 28%→9% 붕괴 시각화 + 
Phantom overlay로 mixture distribution 토글) +
§6(실용 시나리오 — Phase 3 PopPK NDA + Bayesian TDM + Diagnostic Pathology 시그니처)
를 단일 완성 HTML 파일로 통합합니다.
---
```

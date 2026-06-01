# Step 1 Draft v0 — Phase 1 출력 (Master's Lens Draft)

**Session 15: 모델 구축의 기술 — 초기값 · GOF · 모델 판별 · 실험 설계**

- **Source**: Gabrielsson & Weiner 5e, *Pharmacokinetic and Pharmacodynamic Data Analysis: Concepts and Applications*
- **Chapter**: Ch.4 §4.4 (Obtaining Initial Estimates), §4.7-4.10 (GOF · Model Discrimination · Outliers · Checklist) + Ch.5 §5.2.3-5.2.4 (Partial Derivatives · Sensitivity Analysis), §5.3.3 (Toxicokinetic Design — CONTEXT)
- **Pages**: p.352-364 / p.368-392 / p.399-414 (※ pp.365-367 §4.5-4.6 업로드 PDF 부재 — [확인 필요]로 플래그)
- **Mode**: A-Critical
- **Detected Source Type**: Vol I — 데이터 이론 (Gabrielsson & Weiner)

---

## CURATION MAP — Master's Lens First

### ■ MUST (체화 필수, 6개 §2 카드)

| # | 카드명 | Source 위치 | 비고 |
|---|---|---|---|
| 1 | **초기값 획득의 실전 기술** (Initial Estimate Acquisition) | §4.4.1.1-4.4.1.3, p.353-363 | 그래프 박리 + 곡선 추출 |
| 2 | **잔차 기반 모델 진단** (Residual-Based Diagnostics) | §4.7.1-4.7.2, p.369-376 | 패턴 → 결함 매핑 |
| 3 | **F 검정 적용 조건** (F-Test Validity Conditions) | §4.8.1, p.387-389 | ⚡ **Apex Concept** |
| 4 | **파라미터 정밀도와 상관** (Parameter Precision & Correlation) | §4.7.5, §4.7.7, p.380-385 | 설계 A vs B |
| 5 | **편미분 기반 최적 샘플링** (Partial-Derivative Optimal Sampling) | §5.2.3, p.399-403 | 정보 극대화 시점 |
| 6 | **민감도 분석** (Sensitivity Analysis) | §5.2.4, p.403-405 | Pre-fitting 검증 |

### ■ CONTEXT (1-2문장으로 MUST 카드에 통합, 별도 카드 없음)

| 출처 | 통합 위치 | 통합 방식 |
|---|---|---|
| §4.4.2 (When all else fails, p.363-364) — boundary scaling Eq.4:44 | MUST 1 끝부분 | 1-2문장: 초기값 부재 시 boundary 0.1·IE ~ 10·IE 사용 |
| §4.4.1.4 (anxiolytic 4일 반복투여 예시, p.360-363) | MUST 1 끝 worked example | 1-2문장: Eq.4:34 PK 모델 + 4:35-4:42 turnover 도출 |
| §4.7.3 (Pure error vs LOF, Table 4.5-4.7, F_LOF=15.35, p.377-378) | MUST 2 본문 | 1-2문장: lack-of-fit F 검정 (≠ §4.8.1 모델 비교 F 검정) |
| §4.7.4 (Accuracy vs Precision dartboard, Fig.4.52, p.379-380) | MUST 4 도입부 | 1-2문장: bias = 정확도, CV% = 정밀도 |
| §4.7.8 (WRSS vs -2·LL, p.386) | MUST 3 끝부분 | 1문장: -2·LL 기반 프로그램에서도 동일 적용 조건 |
| §4.10 Checklist (Table 4.9, p.391) | §8 메타프레임 | 5가지 GOF 진단 질문 통합 |
| §5.3.3 Toxicokinetic 설계 (p.412-414) | MUST 6 끝부분 | 1-2문장: capacity vs time-dependent kinetics 구분 |

### ■ §5 혼동쌍 직접 배치 (CONTEXT 본문 처리 대신)

- §4.7.6 (r 값 오용, Fig.4.53 r=0.96 OLS vs r=0.94 IRLS, p.382) → **§5 혼동쌍 #2**
- §4.9 (Outlier A vs B, Fig.4.59, p.390) → **§5 혼동쌍 #4**

### ■ 누락 구간 명시

- **pp.365-367 (§4.5 Minimization, §4.6 Weighting)**: 업로드 PDF에 부재. Phase 1은 해당 구간을 임의 보완하지 않는다. 언급이 필요한 곳마다 `[확인 필요 — pp.365-367 업로드 부재]`로 표시.

---

## §1 — Session Header & Roadmap

### 📌 이 세션의 정확한 위치

본 세션은 *Gabrielsson & Weiner 5e* Ch.4-5의 핵심 골격으로, p.352 Fig.4.16에 명시된 **modeling carousel** 6단계(Tentative model → Design → Run experiment → Explore data → Fit model → Analyze output)의 4번 EDA부터 6번 출력 분석까지, 그리고 그 출력을 다음 사이클의 2번 Design으로 되먹이는 **실행 척추**를 다룬다. 즉, 단일 모델링 라운드의 마무리(§4.7-4.10)와 다음 라운드의 출발점(§5.2.3-5.2.4)을 잇는 구간이다.

### 📌 Big Idea (한 문장)

> 이 범위는 EDA에서 시작해 초기값(§4.4) → GOF(§4.7) → 모델 판별(§4.8) → 이상치(§4.9) → 최적 샘플링(§5.2.3) → 민감도(§5.2.4)로 이어지는 modeling carousel의 한 사이클 전체를 마스터하는 곳이며, **여기서 배운 통계 도구의 적용 조건(특히 F 검정의 nested + 동일 weighting 요건)을 혼동하면 NDA/IND 심사관이 Deficiency Letter의 근거로 인용하는 바로 그 오류**가 발생한다.

### 📌 개념 항법도 (이 세션의 6개 MUST 카드 + 4개 혼동쌍)

```
[§4.4.1] 초기값 획득 ────► [§4.7.1-2] 잔차 진단 ────► [§4.8.1] F 검정 ⚡
   │                            │                          │
   │ (graphical anchor)          │ (pattern recognition)     │ (model selection)
   │                            │                          │
   ▼                            ▼                          ▼
[§5.2.4] 민감도 분석 ◄──── [§5.2.3] 편미분 최적 샘플링 ◄──── [§4.7.5,7] 정밀도·상관
   │                            │                          │
   │ (pre-fit verification)      │ (information maximization)│ (CV%, correlation matrix)
```

위 6개 MUST는 **modeling carousel을 한 바퀴 완주하는 데 필수적인 6개 도구**이며, 어느 하나라도 빠지면 사이클이 닫히지 않는다. <!-- ANCHOR -->

### 📌 지식 그래프 위치

**선행 지식 (전제):**
- 1구획/다구획 모델 ODE 도출 (Ch.2-3)
- 비선형 회귀의 Gauss-Newton 알고리즘 기초 (Ch.4 §4.5 — `[확인 필요 — pp.365-367 업로드 부재]`)
- 가중치 모델 (constant absolute / constant relative) (Ch.4 §4.6 — `[확인 필요 — pp.365-367 업로드 부재]`)
- NCA(noncompartmental analysis)에서 AUC, Cl, Vd 추출 (Ch.2 §2.8)

**후행 지식 (이 기반에 의존):**
- **PopPK FOCE 추정**: 본 세션의 잔차 진단·정밀도 개념이 NLME에서 η-shrinkage·ε-shrinkage 해석으로 확장
- **공변량 모델링**: F 검정과 OFV(=−2·log likelihood) 비교가 SCM(Stepwise Covariate Modeling)의 근간
- **Bayesian TDM**: 사전 분포의 정밀도(prior precision)가 본 세션의 CV% 개념의 직접 확장
- **규제 제출용 모델 검증**: §4.10 checklist가 NDA Module 5 PopPK 보고서의 Goodness-of-Fit 섹션 작성 골격
- **Optimal Design Theory (D-optimal, ED-optimal)**: §5.2.3 편미분 접근의 일반화 — Fisher information matrix 기반

### 📌 거장의 시각으로 본 본 세션의 의의

이 세션이 다른 모든 PopPK/PD 챕터와 다른 점은, **"수학적 도구를 어떻게 쓰는가"가 아니라 "언제 그 도구를 쓰면 안 되는가"를 가르친다는 점**이다. F 검정, AIC, 상관계수 r, AUC 비교 — 이 도구들을 잘못된 맥락에서 적용한 결과가 모든 모델링 실패의 80%를 차지한다. 따라서 본 세션은 **부정적 지식(negative knowledge)의 결정체**다.

---

## §2 — Concept Anatomy Cards

각 카드는 다음 순서로 전개: **Big Idea (Master's Lens)** → A. Formal Definition → B. Derivation → C. Structural Necessity → (Apex만) C-2 Plausible Fallacy → D. Assumptions → E. Limitations → F. Five Cognitive Layers → G. Zettelkasten Atom.

---

### ▣ MUST 1 — 초기값 획득의 실전 기술 (Initial Estimate Acquisition)

<!-- MASTER LENS -->
**[개념 Big Idea: 거장의 시각]**

1. **왜 치명적으로 중요한가**: Hill 방정식을 비롯한 비선형 모델에서 초기값이 부실하면 **wrong final value로 수렴**하거나 **physiologically impossible한 local minimum에 빠진다** (p.353 명시). 이 사실을 우습게 본 모델러는 NONMEM `MINIMIZATION SUCCESSFUL` 메시지를 받고도 잘못된 모델로 IND를 제출한 뒤, 임상 1상에서 예측이 빗나가서야 무엇이 잘못되었는지 깨닫는다.

2. **체화해야 할 단 하나의 직관**: 초기값은 "회귀의 출발점"이 아니라 **"모델러가 데이터로부터 추출한, 회귀 알고리즘에 넘겨주는 사전 정보(prior knowledge)"**다. 그래프에서 직접 읽어낸 slope·intercept·plateau는 알고리즘이 절대 자력으로 도달할 수 없는 도메인 통찰의 결정체다.

3. **이 직관을 머릿속에 박고 아래를 읽어라**: 회귀는 모델러를 대신해 생각해주지 않는다. 회귀는 모델러가 그래프에서 본 것을 수치화할 뿐이다.

---

#### A. Formal Definition

**초기값 획득(initial estimate acquisition)**: 비선형 회귀 알고리즘이 반복(iteration)을 시작하기 위해 필요한 모델 파라미터 $\theta_0$의 추정치를, **회귀 자체를 시행하기 전에** 그래프적·선형회귀적·NCA 기반 방법으로 데이터로부터 직접 도출하는 절차. modeling carousel(p.352, Fig.4.16)의 Step 4 EDA(Exploratory Data Analysis)의 핵심 산출물이다.

#### B. Derivation / Code Structure (Vol I — 그래프 박리 + 선형회귀)

**[B-1] IV bolus 1구획 모델 (§4.4.1.1, Fig.4.17)** — 두 피험자에게 10 mg IV bolus 투여 후 plasma concentration vs time:

Semi-log plot에서 high·low concentration 두 점으로 log-linear regression:

$$\text{slope} = \frac{y_2 - y_1}{t_2 - t_1} = -K = \frac{\ln(800) - \ln(400)}{23 - 87} = -0.01\ \text{min}^{-1}\quad \text{[Eq.4:16]}$$

$[\text{출처: Gabrielsson 5e, Ch.4 §4.4.1.1, p.354}]$

여기서 도출되는 일차 파라미터:

$$t_{1/2} = \frac{\ln 2 \cdot V}{Cl} = \frac{\ln 2}{K} = \frac{0.693}{0.01} \approx 65\ \text{min}\quad \text{[Eq.4:17]}$$

$$AUC_0^\infty = \int_0^\infty C^0 \cdot e^{-Kt}\, dt = \frac{C^0}{K} = \frac{D_{iv}}{K \cdot V} = \frac{10000}{0.01 \cdot 10} = 100{,}000\ \mu g \cdot L^{-1} \cdot \text{min}\quad \text{[Eq.4:18]}$$

$$Cl = \frac{D_{iv}}{AUC_0^\infty} = \frac{10000}{1000/0.01} = 0.1\ L \cdot \text{min}^{-1}\quad \text{[Eq.4:19]}$$

$$V = \frac{D_{iv}}{C^0} = \frac{10000}{1000} = 10\ L\quad \text{[Eq.4:20]}$$

**[B-2] Bi-exponential 모델 — 곡선 박리(curve stripping) (§4.4.1.1, Fig.4.18)**:

$$C = A \cdot e^{-\alpha t} + B \cdot e^{-\beta t}\quad \text{[Eq.4:21]}$$

$[\text{출처: Gabrielsson 5e, Ch.4 §4.4.1.1, p.354}]$

알고리즘:
- (i) terminal phase의 log-linear regression → $-\beta$ = slope, $B$ = Y-intercept of back-extrapolation
- (ii) back-extrapolated terminal line을 초기 phase에서 빼서 residual line 도출
- (iii) residual line에 log-linear regression → $-\alpha$ = slope, $A$ = Y-intercept

Fig.4.18 실제 수치: $A = 1.0\ \mu g \cdot L^{-1}$, $B = 0.8\ \mu g \cdot L^{-1}$, $\alpha = 0.05\ \text{min}^{-1}$, $\beta = 0.003\ \text{min}^{-1}$.

**[B-3] Turnover 모델 (warfarin-PCA, §4.4.1.3, Fig.4.20-4.21)** — warfarin이 prothrombin complex 합성($k_{in}$)을 완전 차단했을 때, response는 first-order로 감소:

$$\text{slope} = \frac{\ln(R_2) - \ln(R_1)}{t_2 - t_1} = -k_{out} = \frac{\ln(124) - \ln(56.77)}{24 - 0} \approx -0.03\ h^{-1}\quad \text{[Eq.4:22]}$$

$[\text{출처: Gabrielsson 5e, Ch.4 §4.4.1.3, p.356}]$

Baseline에서 $P_0 = k_{in}/k_{out}$ → intercept(120 sec)와 slope($-k_{out}$)로부터 $k_{in} = 3.6\ \text{sec} \cdot h^{-1}$ 도출.

**[B-4] Anxiolytic 4일 반복투여 worked example (§4.4.1.4, Fig.4.24-4.25)** — CONTEXT 통합:

PK 모델은 Eq.4:34: $C = \frac{K_a \cdot F \cdot D_{po}}{V \cdot (K_a - K)}\left[e^{-Kt} - e^{-K_a t}\right]$, parameters: $K_a = 1.1\ h^{-1}$, $K = 0.128\ h^{-1}$, $V/F = 5.0\ L \cdot kg^{-1}$. PD turnover (Eq.4:36): $\frac{dR}{dt} = k_{in} \cdot I(C) - k_{out} \cdot R$, 초기값 $k_{out} \approx 0.06\ h^{-1}$ (Eq.4:41), $k_{in} = k_{out} \cdot R_0 = 4.8\ \text{units}$ (Eq.4:42), $IC_{50} \approx 0.25\ \mu g \cdot L^{-1}$.

**[B-5] When all else fails (§4.4.2) CONTEXT 통합** — 초기값 추출 불가 시 boundary scaling으로 알고리즘을 안정화:

$$\frac{IE - LB}{UB - LB} = \text{scales to}\ 0\text{-}1\ \text{range}\quad \text{[Eq.4:44]}$$

상대 범위 $0.1 \cdot IE$ ~ $10 \cdot IE$ 권장. Table 4.4 예시: $A = 100$ (LB=10, UB=1000), $\alpha = 0.01$ (LB=0.001, UB=0.1), $B = 1$ (LB=0.1, UB=10), $\beta = 0.05$ (LB=0.0005, UB=0.05).

#### C. Structural Necessity

**왜 그래프 박리가 이 형태일 수밖에 없는가?** Bi-exponential의 두 phase는 시간 스케일이 분리되어 있다($\alpha \gg \beta$). 따라서 큰 $t$에서는 $A \cdot e^{-\alpha t} \to 0$이 되어 terminal slope가 순수하게 $-\beta$를 추출한다. 이것이 **분리 가능한 시간 스케일(separable timescales)**의 수학적 필연이며, semi-log plot이 이 분리를 시각화한다. 만약 $\alpha \approx \beta$라면 박리는 불가능하다 — 그래서 두 phase가 시각적으로 구별되는 데이터에서만 이 방법을 쓸 수 있다.

#### D. Assumptions & Boundary Conditions

- **Assumption 1**: 데이터가 "wide enough range of X values to define a full curve"를 포함 (p.353). 위반 시 → 초기값이 의미 없는 영역으로 외삽.
- **Assumption 2**: 노이즈가 적어 그래프상 phase가 명확히 구분 가능. 위반 시 → terminal slope 추출에 큰 오차.
- **Assumption 3**: 모델 구조가 데이터 패턴과 일치. 위반 시 → 곡선 박리 자체가 부적절(예: 1구획 모델인데 bi-exp 박리 시도).
- **Assumption 4**: Turnover 모델의 경우, $k_{in}$이 완전 차단된 phase가 데이터에 존재 (warfarin의 경우 high dose).

#### E. Limitations

- **다파라미터 비선형 모델**(예: TMDD, semi-physiological)에서는 그래프 박리가 불가능. → 시뮬레이션 기반 educated guess + boundary 사용 (p.363).
- **희소 데이터(sparse data)**: 개체별 곡선 박리 불가능. → PopPK NLME에서 prior 분포로 대체.
- **Data span이 부족**: low concentration이 LOQ 미만이거나 terminal phase가 짧으면 $\beta$ 추출 불가능.

#### F. Five Cognitive Layers

| 레이어 | 내용 |
|---|---|
| **L1 형식적 수학** | Linear regression on log-transformed data: $\hat{\beta}_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}$. Curve stripping = subtraction of fitted exponentials in original scale. |
| **L2 기하학적 직관** | Semi-log plot에서 phase가 직선으로 펼쳐진다. 시간 스케일 분리 = 두 직선의 시각적 분리. |
| **L3 구조적 동일성** | RC 회로의 fast·slow time constant 분리, 화학반응 kinetics의 stiff system pre-equilibrium approximation, 신호처리의 multi-rate filtering과 동형. |
| **L4 생리학적 의미** | $\alpha$ phase = distribution(혈류 분포), $\beta$ phase = elimination(소실). $A$ = central compartment 초기 농도 기여, $B$ = peripheral redistribution 기여. |
| **L5 실무 투영** | NONMEM `$THETA (LB, IE, UB)` 구문, Phoenix WinNonlin "Initial Estimate" tab, R `nlsLM()`의 `start = list(...)` argument. |

#### G. Zettelkasten Atom

```yaml
---
aliases: [초기값 획득, Initial Estimate Acquisition, Curve Stripping]
tags: [pharmacometrics/regression, modeling/eda, gabrielsson/ch4-4]
up: "[[Modeling Carousel - 6단계]]"
related: ["[[잔차 진단]]", "[[비선형 회귀 수렴]]", "[[Local Minimum 함정]]"]
source: "Gabrielsson & Weiner 5e, Ch.4 §4.4.1, p.353-364"
---
```

비선형 회귀의 초기값은 그래프적 곡선 박리(curve stripping)와 log-linear regression으로 데이터에서 직접 추출한다. Bi-exponential의 경우 terminal slope($-\beta$)·intercept($B$)를 먼저 잡고, residual line에서 $\alpha$·$A$를 박리한다. Hill 방정식 등에서 초기값이 부실하면 wrong final value로 수렴하므로(Gabrielsson, p.353), 초기값 추출은 회귀 알고리즘에 넘겨주는 사전 정보이지 단순 출발점이 아니다. 초기값 부재 시 boundary scaling($0.1 \cdot IE$ ~ $10 \cdot IE$)으로 알고리즘을 안정화한다.

---

### ▣ MUST 2 — 잔차 기반 모델 진단 (Residual-Based Diagnostics)

<!-- MASTER LENS -->
**[개념 Big Idea: 거장의 시각]**

1. **왜 치명적으로 중요한가**: 잔차 플롯은 **"모델이 무엇을 놓쳤는지를 데이터가 직접 말해주는 유일한 채널"**이다. 잔차의 banana shape, fan shape, lag-time bulge — 이 3가지 패턴을 즉각 읽어낼 수 없는 모델러는 NONMEM 결과를 "MINIMIZATION SUCCESSFUL"이라는 글자만 보고 채택한 뒤, 심사관이 "Why was a lag-time not considered for oral absorption?"이라고 묻는 Deficiency Letter를 받게 된다.

2. **체화해야 할 단 하나의 직관**: 잔차는 "오차"가 아니라 **"모델이 설명하지 못한 신호"**다. 신호가 랜덤하면 모델이 다 잡았다는 뜻이고, 신호에 패턴이 있으면 그 패턴이 곧 다음 모델 개선의 청사진이다.

3. **이 직관을 머릿속에 박고 아래를 읽어라**: 잔차 플롯을 보지 않고 GOF를 평가하는 것은 환자를 진찰하지 않고 처방하는 것과 같다.

---

#### A. Formal Definition

**잔차(residual)** $\varepsilon_i$는 관찰된 농도 $C_{obs,i}$와 모델 예측 농도 $\hat{C}_{calc,i}$의 차이:

$$\text{residual}_i = C_{obs,i} - \hat{C}_{calc,i}\quad \text{[Fig.4.41, p.369]}$$

이상적으로 $\varepsilon \sim N(0, \sigma^2)$ — 평균 0, 분산 $\sigma^2$, 정규분포(F 검정의 전제):

$$\varepsilon = N(0, \sigma^2)\quad \text{[Eq.4:46]}$$

$[\text{출처: Gabrielsson 5e, Ch.4 §4.7.1, p.369}]$

#### B. Derivation / Code Structure

**[B-1] WRSS 정의 (§4.7.1, Eq.4:47)**:

$$WRSS = \sum_{i=1}^{n} W_i \cdot (C_i - \hat{C}_i)^2$$

$[\text{출처: Gabrielsson 5e, Ch.4 §4.7.1, p.371}]$

Mean standard deviation:

$$\sigma = \sqrt{\frac{WRSS}{N_{obs} - N_{par}}}\quad \text{[Eq.4:48]}$$

여기서 $N_{obs} - N_{par}$ = degrees of freedom.

**[B-2] Weighting scheme별 잔차 형태 (§4.7.2, Fig.4.42, 4.46)**:

$$\begin{cases} \text{Weight} = C_i^{-\lambda_z} & \text{(observed)} \\ \text{Weight} = \hat{C}_i^{-\lambda_z} & \text{(predicted)} \end{cases}\quad \text{[Eq.4:49]}$$

| $\lambda_z$ 값 | 가중치 모델 | 잔차 패턴 |
|---|---|---|
| 0 | constant absolute (OLS) | absolute residual scale |
| -1 | Poisson error | sqrt-proportional |
| -2 | constant relative (CV) | relative residual scale |
| $-n$ | estimated variance parameter | NLME 방식 |

**[B-3] 잔차 패턴 진단 카탈로그 (§4.7.2, Fig.4.43, 4.50)**:

| 패턴 | 의미 | 처방 |
|---|---|---|
| **Banana shape (U자형)** — 잔차가 양→음→양 | 구조 모델 부족 (mono-exp인데 데이터는 bi-exp) | Exponential term 추가 |
| **Inverted-U (∩자형)** — 음→양→음, 초반에 잔차 응집 | Lag-time 부재 (oral 데이터에서 흔함) | $t_{lag}$ 파라미터 추가 |
| **Linear drift (우상향)** — 잔차가 시간에 따라 단조 증가 | Baseline term 부재 | $E_0$ baseline 또는 linear term 추가 |
| **Fan shape (concentration-residual)** | 변량(variance) 모델 오류 | Constant absolute → Constant relative weighting 전환 |
| **Time-series runs (-+++- - -)** | 자동상관 또는 구조 모델 결함 | Runs test, exponential term 또는 lag-time 추가 |

**[B-4] Pure error vs Lack of fit (§4.7.3) — CONTEXT 통합**:

이 F 검정은 §4.8.1의 "두 모델 비교 F 검정"과 **다른 종류**다. Pure error는 같은 시점의 반복 측정 분산:

$$F_{LOF} = \frac{\frac{|WRSS_1 - WRSS_2|}{df_1 - df_2}}{\frac{WRSS_2}{df_2}}\quad \text{[Eq.4:51]}$$

Table 4.5-4.7 in vitro 실험 예시: residual error WRSS=92.67 (df=25), pure error SS=23.61 (df=21), lack of fit SS=69.06 (df=4). 결과: $F_{LOF} = \frac{|92.67-23.61|/(25-21)}{23.61/21} = \frac{17.27}{1.124} = 15.35 \gg F_{crit} = 2.76$. 따라서 mono-exponential 모델은 통계적으로 부적합 — bi-exponential 등 추가 항 필요.

#### C. Structural Necessity

**왜 잔차 플롯이 진단의 1차 도구인가?** 함수 플롯(observed vs predicted)에서는 "곡선이 데이터를 잘 따라간다"는 시각적 인상이 small residual을 가린다 (p.369: "the visual inspection can be misleading in certain regions"). 잔차 플롯은 **수직 거리만 추출**하므로 systematic deviation을 amplify한다. 이것이 "잔차 플롯 없이 fit을 판단하지 말라"는 원칙의 수학적 근거다.

또한, 정규성·등분산성·독립성 — 비선형 회귀의 모든 통계 추론이 의존하는 3가지 가정 — 은 잔차 플롯에서만 확인 가능하다. 파라미터 추정치 자체에는 이 가정의 위반이 보이지 않는다.

#### D. Assumptions & Boundary Conditions

- **Assumption 1**: $\varepsilon_i$가 독립(independence) — 시계열 자동상관 없음. 위반 시 → runs test 양성.
- **Assumption 2**: $E[\varepsilon] = 0$ (zero mean). 위반 시 → 잔차 플롯에 systematic bias.
- **Assumption 3**: $Var(\varepsilon) = \sigma^2$ (homoscedasticity, 가중 후). 위반 시 → fan/funnel pattern.
- **Assumption 4**: $\varepsilon \sim N(0, \sigma^2)$ — F 검정 시행에 필요. 위반 시 → 비모수적 검정 또는 변환 필요.

#### E. Limitations

- **소표본**(N < 20): runs test의 통계적 검정력 부족. 시각적 판단(judgment call)에 의존 (p.370).
- **Sparse data**: 시점당 1회 관측만 있으면 pure error 분리 불가능 → §4.7.3의 LOF F 검정 시행 불가.
- **잔차가 구조 결함과 변량 결함을 둘 다 반영**: 두 결함이 공존하면 진단 분리 어려움 — 변량 모델을 먼저 점검 후 구조 모델 진단 권장.
- **잔차 진단은 "필요조건"이지 "충분조건"이 아님**: 잔차가 랜덤해도 모델이 옳다는 보장 없음(다른 동일한 설명력 모델 존재 가능).

#### F. Five Cognitive Layers

| 레이어 | 내용 |
|---|---|
| **L1 형식적 수학** | $\varepsilon_i \sim N(0, \sigma^2)$. WRSS = $\sum W_i (C_i - \hat{C}_i)^2$. Standardized residual = $\varepsilon_i / SD(\hat{Y}_i)$. |
| **L2 기하학적 직관** | 잔차 플롯의 fluctuation envelope = $\pm 2\sigma$ band. Pattern 있으면 envelope 형태가 아닌 trend가 보임. |
| **L3 구조적 동일성** | 통계학의 white noise vs colored noise 구분, 신호처리의 detrending residual, 회귀진단의 leverage·influence와 동형. |
| **L4 생리학적 의미** | Banana shape → 두 번째 분포 phase 누락. Lag bulge → 위장관 흡수 지연. Linear drift → endogenous baseline production. |
| **L5 실무 투영** | NONMEM `WRES` (weighted residual), `CWRES` (conditional WRES, FOCE), `NPDE`. R: `nlme::residuals(.., type='pearson')`. Pirana/Xpose의 GOF panel. |

#### G. Zettelkasten Atom

```yaml
---
aliases: [잔차 진단, Residual Diagnostics, GOF Pattern Reading]
tags: [pharmacometrics/diagnostics, gof/residual, gabrielsson/ch4-7]
up: "[[Modeling Carousel - Step 6 Analyze Output]]"
related: ["[[F 검정]]", "[[Weighting Scheme]]", "[[CWRES]]", "[[Pure error vs LOF]]"]
source: "Gabrielsson & Weiner 5e, Ch.4 §4.7.1-4.7.3, p.369-378"
---
```

잔차는 모델이 설명하지 못한 신호이며, 잔차 플롯의 패턴(banana=구조 부족, lag bulge=흡수 지연, fan=변량 모델 오류)이 다음 모델 개선의 청사진을 제공한다. Pure error와 lack-of-fit을 분리하는 F 검정($F_{LOF} = 15.35 \gg F_{crit} = 2.76$, Gabrielsson Table 4.7)은 §4.8.1의 모델 비교 F 검정과 다른 도구이며, 같은 시점 반복 측정이 있을 때만 시행 가능하다.

---

### ▣ MUST 3 — F 검정 적용 조건 ⚡ **Apex Concept** (F-Test Validity Conditions)

> **[⚡ Apex Concept]** 본 세션의 모든 개념 중 임상·규제 파급력이 가장 큰 단 하나의 개념. 이 개념의 Plausible Fallacy(C-2)는 NDA Deficiency Letter의 실제 사유다.

<!-- MASTER LENS -->
**[개념 Big Idea: 거장의 시각]**

1. **왜 치명적으로 중요한가**: F 검정은 두 가지 적용 조건 — (i) **Nested(hierarchical) models**, (ii) **Equal weighting** — 이 동시에 만족될 때만 유효하다. Michaelis-Menten 소실(가중 모델)과 1차 소실(비가중 모델)을 비교하면서 F 검정을 적용하면 **nested 위반 + weighting 위반**의 이중 위반(Table 4.8)이며, 이것이 NDA Module 5에 포함된 PopPK 보고서가 받는 가장 빈번한 Deficiency Letter 사유 중 하나다.

2. **체화해야 할 단 하나의 직관**: F 검정은 "더 복잡한 모델이 더 잘 맞는가?"를 묻는 것이 아니라, **"추가된 파라미터가 통계적으로 0과 구별되는가?"**를 묻는 도구다. 이것은 reduced model을 full model의 특수 케이스(특정 파라미터를 0으로 고정)로 표현할 수 있을 때만 의미 있는 질문이다.

3. **이 직관을 머릿속에 박고 아래를 읽어라**: F 검정의 적용 조건을 무시하면 통계적 권위로 위장된 무의미한 숫자를 얻을 뿐이다. 도구의 적용 영역을 모르는 사용은 도구를 갖지 않은 것보다 위험하다.

---

#### A. Formal Definition

**F 검정(F-test)**: 두 모델이 nested(reduced model을 full model에서 일부 파라미터를 특정 값으로 고정하여 얻을 수 있음) 관계이고, 동일한 weighting scheme(OLS 또는 동일한 WLS) 하에 적합되었을 때, 추가 파라미터가 sum of squares를 통계적으로 유의하게 개선하는지 검정하는 도구. F 통계량:

$$F^* = \frac{\frac{|WRSS_1 - WRSS_2|}{df_1 - df_2}}{\frac{WRSS_2}{df_2}}\quad \text{[Eq.4:54]}$$

$[\text{출처: Gabrielsson 5e, Ch.4 §4.8.1.1, p.387}]$

여기서 subscript 1 = reduced(축소 모델), 2 = full(완전 모델), $df = N_{obs} - N_{par}$ (Eq.4:55).

판정: $F^* > F_{table}(p=0.05, \Delta df = |df_1 - df_2|, df_2)$ → full model이 reduced model보다 통계적으로 우수.

#### B. Derivation / Code Structure

**[B-1] Nested 관계의 4가지 분류 (§4.8.1.2-4.8.1.4)**:

| 비교 | Nested 여부 | F 검정 적용 가능 |
|---|---|---|
| **Mono-exp vs Bi-exp**: $C = A e^{-\alpha t}$ vs $C = A e^{-\alpha t} + B e^{-\beta t}$ ($B = 0$이면 reduced) | ✅ Nested | ✅ Yes |
| **Ordinary $E_{max}$ vs Sigmoid $E_{max}$**: $E = \frac{E_{max} \cdot C}{EC_{50} + C}$ vs $E = \frac{E_{max} \cdot C^n}{EC_{50}^n + C^n}$ ($n=1$이면 reduced) | ✅ Nested | ✅ Yes |
| **Hepatic Distributed vs Parallel-tube**: 분산 $\varepsilon^2$ → 0이면 reduced | ✅ Nested | ✅ Yes |
| **Ordinary $E_{max}$ vs Linear**: $E = sC$는 $E_{max}$ 모델의 특수 케이스가 아님 ($C \ll EC_{50}$ 한정으로만 유사) | ❌ Non-nested | ❌ **No (적용 불가)** |

$[\text{출처: Gabrielsson 5e, Ch.4 §4.8.1.2-4.8.1.4, p.388-389}]$

**[B-2] Sigmoid $E_{max}$ vs Ordinary $E_{max}$ (§4.8.1.2) — 단순 대안**:

$n$의 95% 신뢰구간이 1을 포함하지 않으면 $n \neq 1$ → sigmoid 모델 채택. F 검정과 동등한 결론 (단일 파라미터 검정이라).

**[B-3] WRSS vs -2·log likelihood (§4.7.8) — CONTEXT 통합**:

NONMEM(FOCE 등)은 WRSS 대신 $-2 \cdot LL$로 수렴. 점근적으로 동일한 모델 파라미터로 수렴하나, OFV(Objective Function Value)로 표현. F 검정의 적용 조건(nested + 동일 likelihood 모델)은 동일하게 유지된다 — `[확인 필요]`: NONMEM에서는 실제로 OFV difference의 $\chi^2$ 분포 사용(LRT, likelihood ratio test)이 일반적이며, 이는 F 검정의 -2·LL 형태로 본 교과서에서는 명시되지 않는다.

#### C. Structural Necessity

**왜 nested가 F 검정의 필수 조건인가?** F 분포는 두 $\chi^2$ 변량의 비로 정의되며, $\chi^2$ 분포의 자유도가 well-defined되려면 reduced model이 full model의 특정 파라미터를 0(또는 고정값)으로 제약한 형태여야 한다. 이 제약이 없으면(non-nested), $WRSS_1 - WRSS_2$의 분포가 $\chi^2$ 형태가 아니다. 따라서 비율 자체가 F 분포를 따르지 않으며, $p$-value 계산이 무의미하다.

**왜 동일 weighting이 필수 조건인가?** Weighting scheme이 다르면 $WRSS$의 정의 자체가 다르다. constant absolute($W=1$)와 constant relative($W = 1/\hat{C}^2$)는 단위가 다르므로, 두 WRSS의 차이는 통계적으로 비교 불가능한 양이다. 이것은 단순한 단위 차이가 아니라 **likelihood function 자체의 다른 정의**다.

#### C-2. Plausible Fallacy (그럴싸한 오류) — Apex Concept 전용

**오류의 구체적 형태**:

> "Michaelis-Menten 소실(2 파라미터: $V_{max}$, $K_m$)과 1차 소실(1 파라미터: $K$)이 모두 1구획 IV bolus 모델에서 적합되었으니, 파라미터 수가 다르므로 nested 관계로 보고 F 검정을 적용한다. 게다가 MM 모델은 fan-shape 잔차 때문에 constant relative weighting을 썼고, 1차 모델은 잔차가 균질해서 constant absolute weighting을 썼다. 두 모델의 WRSS를 직접 비교해 작은 쪽을 채택한다."

**왜 그럴싸한가**: 파라미터 수가 다르고 한 모델이 더 복잡해 보이므로 "full vs reduced" 직관을 자극한다.

**왜 틀렸는가 — 이중 위반**:
1. **Nested 위반**: MM 모델 $\frac{V_{max} \cdot C}{K_m + C}$에서 어떤 파라미터를 어떤 값으로 고정해도 1차 모델 $K \cdot C$를 얻지 못한다. $C \ll K_m$ 극한에서만 근사적으로 유사할 뿐, 수학적으로 nested가 아니다(Table 4.8 명시, p.389).
2. **Weighting 위반**: 다른 weighting → 다른 likelihood → WRSS 직접 비교 불가능.

**나비효과 — NONMEM 피팅과 임상 예측에 미치는 결과**:
- F 검정 통과/실패 판정 자체가 무의미. 통과되어 MM 모델 채택 시: 임상 용량 외삽에서 약 100배 bias 가능성(MM의 saturation kinetics가 부적절한 농도 범위에 적용됨).
- 잔차 진단 시그니처: **"Phantom Convergence Pattern"** — 두 모델 모두 `MINIMIZATION SUCCESSFUL`이지만 OFV 비교가 invalid. CWRES 플롯에서는 두 모델이 거의 동일하게 보여 모델러가 차이를 시각적으로 잡을 수 없음.

**해결**: AIC/SC 사용 (단, **동일 weighting 조건은 AIC도 적용** — Table 4.8 `Comparing 1&2: Cannot use AIC because different weights`). 동일 weighting 하에 적합 후 AIC 비교 또는 별도의 Model averaging 기법 사용.

#### D. Assumptions & Boundary Conditions

- **Assumption 1**: 잔차 정규성 $\varepsilon \sim N(0, \sigma^2)$ — F 검정의 통계적 기반.
- **Assumption 2**: Nested model 관계 — reduced = full의 특정 파라미터 고정 형태.
- **Assumption 3**: 동일 weighting scheme — OLS or 동일 WLS.
- **Assumption 4**: 동일 데이터셋 — 다른 표본 크기에는 적용 불가.
- **Assumption 5**: 정확한 자유도 계산 — $df = N_{obs} - N_{par}$.

#### E. Limitations

- **Non-nested 모델 비교 불가** — AIC/SC도 weighting 동일성 제약 받음.
- **Mathematically distinct models**: 메커니즘이 옳은 모델이 적은 파라미터로 데이터를 설명할 수 있고, 그른 모델이 많은 파라미터로 동일 fit을 낼 수 있음 — F 검정은 이를 구별하지 못함 (p.387: "With mathematically distinct models, a function that is mechanistically correct may describe the data with fewer parameters").
- **소표본**: $df$가 작으면 검정력 부족.
- **Boundary problem**: 단일변량 95% 신뢰구간이 unity를 포함하지 않으면 F 검정과 동등한 결론을 단일변량으로 빠르게 얻을 수 있음 (§4.8.1.2 sigmoid 사례).

#### F. Five Cognitive Layers

| 레이어 | 내용 |
|---|---|
| **L1 형식적 수학** | $F^* \sim F(\Delta df, df_2)$ under $H_0$. Likelihood Ratio Test 형태: $-2 \log \frac{L_1}{L_2} \sim \chi^2(\Delta df)$. |
| **L2 기하학적 직관** | OFV(혹은 WRSS) surface에서 reduced model = full model의 lower-dimensional subspace. F 검정 = subspace에 머물러도 충분한가? |
| **L3 구조적 동일성** | ANOVA의 nested vs crossed factor 검정, 회귀의 partial F-test, 시계열의 ARIMA(p,d,q)에서 차수 검정과 동형. |
| **L4 생리학적 의미** | $n=1$ vs $n>1$ 검정 = 수용체 cooperativity 통계적 검정. $B=0$ vs $B>0$ = peripheral compartment 존재 여부 검정. |
| **L5 실무 투영** | NONMEM: $\Delta OFV > 3.84$ ($\chi^2$, df=1, $\alpha=0.05$) → 추가 파라미터 채택. PsN `scm.pl` (Stepwise Covariate Modeling) 알고리즘의 핵심. NDA Module 5 PopPK Section: "Model selection was based on a likelihood ratio test (LRT) with..." |

#### G. Zettelkasten Atom

```yaml
---
aliases: [F 검정, F-test, LRT, Likelihood Ratio Test, Model Discrimination]
tags: [pharmacometrics/inference, statistics/nested, regulatory/lrt, gabrielsson/ch4-8]
up: "[[Model Selection Hierarchy]]"
related: ["[[AIC]]", "[[SC]]", "[[Nested Models]]", "[[Weighting Scheme]]", "[[Plausible Fallacy - MM vs 1st-order]]"]
source: "Gabrielsson & Weiner 5e, Ch.4 §4.8.1, p.387-389"
---
```

F 검정($F^* = \frac{|WRSS_1 - WRSS_2|/(df_1 - df_2)}{WRSS_2/df_2}$, Gabrielsson Eq.4:54)은 nested + 동일 weighting의 두 조건이 동시에 만족될 때만 유효하다. Michaelis-Menten 소실과 1차 소실 비교는 nested가 아니며(고정 파라미터 값으로 변환 불가), 가중치까지 다르면 이중 위반(Table 4.8)이다. 이 오류는 NDA Deficiency Letter의 실제 사유이며, AIC/SC도 동일 weighting 제약을 받는다.

---

### ▣ MUST 4 — 파라미터 정밀도와 상관 (Parameter Precision & Correlation)

<!-- MASTER LENS -->
**[개념 Big Idea: 거장의 시각]**

1. **왜 치명적으로 중요한가**: 파라미터 추정치가 아무리 좋은 fit을 보여도, **CV%가 50% 이상이거나 두 파라미터의 correlation이 0.95 이상**이면 그 추정치는 "값"이 아니라 "그 데이터로는 분리할 수 없는 두 파라미터의 임의 조합"이다. 이를 모르고 추정치를 인용하면 NDA에서 "The reported $V_{max}$ and $K_m$ values are highly correlated (r = -0.95) and cannot be considered independently identified"라는 심사관 코멘트를 받는다 — 그리고 **이것은 모델 오류가 아니라 실험 설계 오류**다.

2. **체화해야 할 단 하나의 직관**: 정밀도는 모델의 속성이 아니라 **데이터 + 설계의 속성**이다. 같은 모델, 같은 알고리즘이라도 sampling design이 좋으면 파라미터가 분리되고, 나쁘면 강하게 상관된 채로 fit이 "성공적으로" 수렴한다. 따라서 정밀도 진단은 "모델 어떻게 고칠까?"가 아니라 "다음 실험을 어떻게 설계할까?"의 출발점이다.

3. **이 직관을 머릿속에 박고 아래를 읽어라**: 좋은 fit + 나쁜 정밀도는 모델 잘못이 아니라 데이터 잘못이다. 이 인식 전환이 §5.2.3 편미분 기반 설계로 가는 다리다.

---

#### A. Formal Definition

**정확도(accuracy)**: 추정치 $\hat{p}$가 참값 $p$에 얼마나 가까운가. Bias = $|p - \hat{p}|/p \cdot 100\%$ (p.380).

**정밀도(precision)**: 동일 실험을 반복했을 때 $\hat{p}$가 얼마나 일관되게 나오는가. 측정량:

$$CV\% = \frac{SE(\hat{p})}{\hat{p}} \cdot 100\quad \text{[Eq.4:52]}$$

$[\text{출처: Gabrielsson 5e, Ch.4 §4.7.5, p.380}]$

**파라미터 상관(correlation)**: 두 파라미터 추정치가 한쪽 변경 시 다른 쪽 변경으로 보상 가능한 정도. 상관행렬의 비대각 원소 $|r| \to 1$이면 강한 상관(p.383).

> **CONTEXT 통합 — Accuracy vs Precision dartboard (§4.7.4, Fig.4.52)**: 다트보드 비유에서 "한가운데 평균 + 분산 큼" = 정확도 OK, 정밀도 X. "한쪽 구석 집중" = 정확도 X, 정밀도 OK. 이상적 = 한가운데 집중. 좋은 fit이 좋은 추정치를 보장하지 않는다(p.380): "Even though a fit is good or acceptable in terms of good correspondence between the observed and predicted values, the resulting parameter estimates may be of no value."

#### B. Derivation / Code Structure

**[B-1] Univariate vs Planar 신뢰한계 (§4.7.5, p.380-381)**:

- **Univariate CI**: $\hat{p} \pm t \cdot SE(\hat{p})$, 다른 파라미터의 값 무시 → 좁은 구간.
- **Planar CI**: 파라미터 간 상관을 고려한 ellipsoidal 구간 → 항상 univariate보다 넓음.

p.381 박스 예시 (V, K):

| 파라미터 | 추정치 | SE | 95% CI (Univariate) | 95% CI (Planar) |
|---|---|---|---|---|
| V | 10.1789 | 0.311081 | (9.46, 10.89) | (9.19, 11.16) |
| K | 0.019048 | 0.000878 | (0.017, 0.021) | (0.016, 0.0218) |

**[B-2] 상관행렬 (§4.7.7, p.383)** — 동일 V, K 예시:

```
       V        K
V    1.000
K   -0.80962  1.000
```

$|r| = 0.81$ → 중간 정도 상관. $|r| > 0.95$이면 "Any small change in one of the parameters could be compensated for by making an appropriate adjustment in the other" (p.383).

**[B-3] 설계 A vs 설계 B (§4.7.7, Fig.4.56-4.57)**:

| 설계 | 시점/농도 분포 | 결과 (V vs Cl 또는 $E_{max}$ vs $IC_{50}$) |
|---|---|---|
| **Design A** (full): 시점이 잘 분포, plateau 포함 | 낮은 상관 ($r \approx -0.35$, Fig.4.57) | $E_{max}$, $IC_{50}$ 분리 가능 |
| **Design B** (reduced): 시점이 좁은 범위에 집중, plateau 없음 | 높은 상관 ($r \approx -0.95$, Fig.4.57) | 두 파라미터 분리 불가능 |

**[B-4] 고상관 + 고정밀도의 함정 (Fig.4.55)**: 신뢰구간이 좁아도 상관이 강하면 두 파라미터 중 하나만 fix하면 다른 하나의 CI가 더 좁아진다 — **"실제로 두 파라미터를 모두 추정한 것이 아닌"** 상황. 이것을 모르고 양쪽 추정치를 모두 보고하는 것이 빈번한 실수.

#### C. Structural Necessity

**왜 정밀도가 fit과 분리되는가?** Likelihood surface의 한 점이 minimum이라는 것은 fit가 좋다는 뜻. 하지만 그 minimum 주변의 곡률(2차 미분, Hessian 행렬의 역행렬 = 공분산행렬)이 정밀도를 결정한다. **Surface가 평평한(flat) minimum**이면 fit는 좋지만 추정치 변동에 OFV가 거의 안 변함 → 정밀도 낮음. 두 파라미터 방향으로 surface가 ridge 형태면 강한 상관.

**왜 설계가 정밀도를 결정하는가?** Fisher information matrix $\mathcal{I}(\theta)$는 sampling time과 모델 파라미터의 함수다. $\mathcal{I}$의 역이 공분산행렬 $\Sigma_\theta$. 따라서 sampling을 Fisher information이 커지는 시점에 배치하면 $\Sigma_\theta$가 줄고 정밀도가 향상. 이것이 §5.2.3 편미분 접근의 이론적 근거.

#### D. Assumptions & Boundary Conditions

- **Assumption 1**: 점근적 정규성 — SE가 의미를 가지려면 표본 크기가 충분.
- **Assumption 2**: Hessian이 positive definite — minimum이 well-defined.
- **Assumption 3**: 모델이 identifiable — 구조적으로 파라미터 분리 가능 (예: $V$와 $Cl$이 single observation에서 분리되려면 추가 정보 필요).
- **Assumption 4**: SE 계산이 first-order Taylor 근사에 기반 — 강한 비선형성에서 부정확.

#### E. Limitations

- **Structural unidentifiability**: 모델 자체에서 두 파라미터가 곱·합으로만 등장하면 어떤 설계로도 분리 불가능 (예: $A \cdot B$만 등장하면 $A=2, B=3$과 $A=6, B=1$이 동등).
- **Sample-size dependent**: SE가 표본 크기 √N에 반비례 → sparse data에서 항상 정밀도 낮음.
- **Local linearization 한계**: nonlinear 모델에서 95% CI는 점근적이며 실제 분포가 비대칭일 수 있음.
- **Correlation은 모델·설계 induced**: 생물학적 의미와 무관 — 같은 생리학적 시스템도 다른 parametrization으로 다른 상관 보일 수 있음.

#### F. Five Cognitive Layers

| 레이어 | 내용 |
|---|---|
| **L1 형식적 수학** | $\Sigma_\theta = \mathcal{I}(\theta)^{-1}$ (Fisher information의 역). $CV(\theta_i) = \sqrt{\Sigma_{ii}}/\theta_i$. Correlation $\rho_{ij} = \Sigma_{ij}/\sqrt{\Sigma_{ii} \Sigma_{jj}}$. |
| **L2 기하학적 직관** | Likelihood surface 주변의 95% CI ellipsoid. 길쭉한 ellipsoid = 강한 상관, 동그란 ellipsoid = 무상관. |
| **L3 구조적 동일성** | Cramér-Rao lower bound, 양자측정의 measurement uncertainty와 동형. 다중공선성(multicollinearity)의 비선형 일반화. |
| **L4 생리학적 의미** | Cl-V 상관: 두 파라미터가 모두 elimination time scale에 영향. $V_{max}$-$K_m$ 상관: 효소 포화 정도가 데이터에 충분히 안 보임. |
| **L5 실무 투영** | NONMEM `$COVARIANCE` step의 `OMEGA HAS A VARIANCE > 3.5` 경고 = 정밀도 문제. `EIGENVALUES` 출력에서 condition number $\kappa > 1000$ = 강한 상관. PsN `bootstrap` 또는 `sse` 시뮬레이션. |

#### G. Zettelkasten Atom

```yaml
---
aliases: [파라미터 정밀도, Parameter Precision, CV%, Correlation Matrix]
tags: [pharmacometrics/precision, design/sampling, gabrielsson/ch4-7-5, ch4-7-7]
up: "[[Modeling Carousel - Step 6 Analyze Output]]"
related: ["[[편미분 최적 샘플링]]", "[[Fisher Information]]", "[[Identifiability]]", "[[Design A vs B]]"]
source: "Gabrielsson & Weiner 5e, Ch.4 §4.7.5, §4.7.7, p.380-385"
---
```

파라미터 정밀도(CV% = SE/$\hat{p}$ × 100, Gabrielsson Eq.4:52)와 상관($|r|$ > 0.95이면 강한 상관, p.383)은 모델 fit과 분리된다 — 좋은 fit이 좋은 추정치를 보장하지 않는다(p.380). 정밀도는 모델의 속성이 아니라 **데이터 + 설계의 속성**이며, sampling이 잘 분포된 Design A에서 두 파라미터의 상관이 -0.35로 떨어지나, 좁은 시점에 집중된 Design B에서는 -0.95로 치솟는다(Fig.4.57). 따라서 정밀도 진단은 다음 실험 설계의 출발점이며, §5.2.3 편미분 접근으로 직결된다.

---

### ▣ MUST 5 — 편미분 기반 최적 샘플링 (Partial-Derivative Optimal Sampling)

<!-- MASTER LENS -->
**[개념 Big Idea: 거장의 시각]**

1. **왜 치명적으로 중요한가**: 임상시험에서 환자당 sampling 횟수는 윤리·예산·logistical 제약으로 제한된다. 동일한 8개 시점을 어디에 배치하느냐가 $V_{max}$ 추정 CV%를 50%로 만들지 5%로 만들지를 결정한다 — 그리고 **이 결정은 fit 결과를 본 후가 아니라 시험 시작 전에** 내려져야 한다. Phase 1 protocol에 잘못된 sampling time을 박은 채로 데이터를 수집하면 어떤 분석으로도 만회할 수 없다.

2. **체화해야 할 단 하나의 직관**: 파라미터 $\theta$에 대한 **편미분 $\partial C/\partial \theta$의 극값(maximum 또는 minimum)이 위치하는 시점이 그 파라미터의 정보가 최대로 담긴 시점**이다. 이 시점에서 측정한 값이 작은 변화도 $\theta$의 변화를 즉각 드러낸다. 평평한 곳에서는 어떻게 측정해도 $\theta$를 분리할 수 없다.

3. **이 직관을 머릿속에 박고 아래를 읽어라**: "골고루 sampling"은 잘못된 직관이다. **불균일한, 정보 기반 sampling**이 옳다.

---

#### A. Formal Definition

**편미분 기반 최적 샘플링(partial-derivative-based optimal sampling)**: 모델 $C(t; \theta)$의 각 파라미터 $\theta_i$에 대한 편미분 $\partial C/\partial \theta_i$를 시간 $t$의 함수로 plot하여, 그 절댓값이 극값(maximum 또는 minimum)을 갖는 시점에 sampling을 배치하는 정보 극대화 설계 기법. Fisher information matrix의 비선형 회귀 형태에서 도출된다.

#### B. Derivation / Code Structure

**[B-1] Bi-exponential 모델의 편미분 (§5.2.3, p.399-400)**:

$$C = A \cdot e^{-\alpha t} + B \cdot e^{-\beta t}\quad \text{[Eq.5:7]}$$

$[\text{출처: Gabrielsson 5e, Ch.5 §5.2.3, p.399}]$

Intercept 파라미터 ($A$, $B$)에 대한 편미분:

$$\frac{\partial C}{\partial A} = e^{-\alpha t}, \quad \frac{\partial C}{\partial B} = e^{-\beta t}\quad \text{[Eq.5:8]}$$

→ 둘 다 $t = 0$에서 maximum (=1) → **$A$, $B$ 정보는 초기 시점에 최대**.

Slope 파라미터 ($\alpha$, $\beta$)에 대한 편미분:

$$\frac{\partial C}{\partial \alpha} = -A \cdot t \cdot e^{-\alpha t}, \quad \frac{\partial C}{\partial \beta} = -B \cdot t \cdot e^{-\beta t}\quad \text{[Eq.5:9]}$$

극값 도출을 위해 시간에 대한 2차 편미분을 0으로:

$$\frac{d^2 C}{dt \, d\alpha} = A \alpha t e^{-\alpha t} - A e^{-\alpha t} = 0\quad \text{[Eq.5:10]}$$

$\Rightarrow t = 1/\alpha$ (마찬가지로 $t = 1/\beta$):

$$\begin{cases} t^*_\alpha = 1/\alpha \\ t^*_\beta = 1/\beta \end{cases}\quad \text{[Eq.5:11]}$$

**구체적 수치 (§5.2.3, p.400)**: $\alpha = 0.69\ h^{-1}$이면 $t^*_\alpha = 1.4\ h$, $\beta = 0.069\ h^{-1}$이면 $t^*_\beta = 14\ h$.

$[\text{출처: Gabrielsson 5e, Ch.5 §5.2.3, p.400}]$

**[B-2] Sigmoid $I_{max}$ 모델의 편미분 (§5.2.3, Eq.5:12-5:14)**:

$$E = E_0 - \frac{I_{max} \cdot C^n}{IC_{50}^n + C^n}\quad \text{[Eq.5:12]}$$

$$\frac{\partial E}{\partial I_{max}} = -\frac{C^n}{IC_{50}^n + C^n}\quad \text{[Eq.5:13]}$$

$$\frac{\partial E}{\partial IC_{50}} = -\frac{n \cdot I_{max} \cdot IC_{50}^{n-1} \cdot C^n}{(IC_{50}^n + C^n)^2}\quad \text{[Eq.5:14]}$$

극값 위치:
- $\partial E/\partial I_{max}$ → high concentration plateau에서 maximum → **$I_{max}$ 정보는 최고 농도에서**.
- $\partial E/\partial IC_{50}$ → $C = IC_{50}$에서 maximum (inflection point) → **$IC_{50}$ 정보는 half-maximal effect에서**.
- $\partial E/\partial n$ → 두 극값 (~20%와 ~80% effect 농도) → **$n$ 정보는 sigmoid의 가파른 부분에서**.

**[B-3] 5개 design points (§5.2.3, Fig.5.6, p.402)** — Sigmoid $E_{max}$ 모델 종합:

| Design point | 위치 | 정보 |
|---|---|---|
| 1 | Baseline (C → 0) | $E_0$ |
| 2 | ~20% effect 농도 | $n$ (sigmoidicity) |
| 3 | $C = EC_{50}$ (inflection) | $EC_{50}$ |
| 4 | ~80% effect 농도 | $n$ |
| 5 | High plateau (C → ∞) | $E_{max}$ |

**[B-4] Turnover 모델의 편미분 (§5.2.3, Fig.5.8, p.402-403)**:

$$\frac{dR}{dt} = k_{in} \cdot \frac{1}{I(C)} - k_{out} \cdot R, \quad I(C) = 1 + \left[\frac{(D_{iv}/V) \cdot e^{-Kt}}{IC_{50}}\right]^n\quad \text{[Eq.5:15-5:16]}$$

분석 결과 (warfarin-PCA, Fig.5.8): $k_{out}$의 편미분은 25 h와 ~100 h에서 두 극값. → 두 시점에서 sampling.

#### C. Structural Necessity

**왜 편미분 극값이 정보 최대 지점인가?** 모델 $C(t; \theta)$를 $\theta$에 대해 1차 Taylor 전개:

$$C(t; \theta + \delta\theta) \approx C(t; \theta) + \frac{\partial C}{\partial \theta} \cdot \delta\theta$$

따라서 $|\delta C| \approx |\partial C/\partial \theta| \cdot |\delta\theta|$. **편미분이 큰 시점에서는 $\theta$의 작은 변화도 $C$의 큰 변화로 amplify된다** → 측정 노이즈로부터 $\theta$ 신호를 잘 분리. 편미분이 0인 시점에서는 어떤 $\theta$ 값을 써도 $C$가 같다 → 정보 0.

**Fisher information matrix와의 연결**: $\mathcal{I}_{ij}(\theta) = \mathbb{E}\left[\frac{\partial \log L}{\partial \theta_i} \frac{\partial \log L}{\partial \theta_j}\right]$. 가우시안 노이즈 가정에서 $\mathcal{I}_{ij} \propto \int \frac{\partial C}{\partial \theta_i} \frac{\partial C}{\partial \theta_j} dt$. 따라서 편미분의 outer product를 적분한 양 = Fisher 정보. 편미분이 큰 시점이 $\mathcal{I}$ 적분에 큰 기여 → optimal design의 핵심.

#### D. Assumptions & Boundary Conditions

- **Assumption 1**: 초기 파라미터 추정치(prior)가 있어야 편미분 계산 가능 — "닭이 먼저냐 알이 먼저냐" 문제. 해결: 1차 실험으로 prior 도출 → 2차 실험 설계 개선 (반복적 modeling carousel).
- **Assumption 2**: 모델이 옳다는 전제. 모델 misspecification이 있으면 optimal design이 잘못된 방향.
- **Assumption 3**: 노이즈 모델이 일정 — homoscedastic 또는 알려진 heteroscedastic.
- **Assumption 4**: 단일 측정의 비용이 동일 — 시점별 비용이 다르면 cost-weighted optimization 필요.

#### E. Limitations

- **Local optimum**: 단일 prior에 최적 → prior가 부정확하면 robustness 약함. 해결: ED-optimal (expected D-optimal over prior 분포).
- **Single-objective**: 모든 파라미터를 동시에 최적화하지 않음 — A-optimal, D-optimal, E-optimal 등 trade-off.
- **Population vs individual design**: 개체간 변이가 클 때 robust design 필요 (population optimal design).
- **Practical constraints**: 윤리·시계열 제약(예: 새벽 3시 sampling 불가).

#### F. Five Cognitive Layers

| 레이어 | 내용 |
|---|---|
| **L1 형식적 수학** | Fisher Information $\mathcal{I}(\theta) = \mathbb{E}[(\partial \log L/\partial \theta)(\partial \log L/\partial \theta)^T]$. D-optimal: $\arg\max_\xi \det \mathcal{I}(\theta, \xi)$. |
| **L2 기하학적 직관** | $\partial C/\partial \theta$ 곡선의 peak가 정보의 "광원". Sampling은 그 광원의 빛이 가장 강한 곳에 측정기를 두는 행위. |
| **L3 구조적 동일성** | 광학의 diffraction-limited resolution, MRI의 k-space sampling, X-ray crystallography의 reciprocal-space optimization과 동형. |
| **L4 생리학적 의미** | 약물의 distribution phase: $\alpha = 0.69\ h^{-1}$이면 $t = 1.4\ h$가 분포 평형 시점 — 이 시점이 분포 정보의 핵심. Slow elimination phase($\beta$)는 long-tail에서 정보 누적. |
| **L5 실무 투영** | PFIM (R 패키지) — Population Fisher Information Matrix 계산. NONMEM `$DESIGN` 블록(미지원, PsN extension). PopED 소프트웨어. Phase 1 protocol의 PK sampling schedule 결정. |

#### G. Zettelkasten Atom

```yaml
---
aliases: [최적 샘플링, Optimal Sampling, Partial Derivative Design, Fisher Information Design]
tags: [pharmacometrics/design, optimal-design/d-optimal, gabrielsson/ch5-2-3]
up: "[[Optimal Experimental Design]]"
related: ["[[정밀도와 상관]]", "[[Fisher Information]]", "[[PopED]]", "[[민감도 분석]]"]
source: "Gabrielsson & Weiner 5e, Ch.5 §5.2.3, p.399-403"
---
```

편미분 $\partial C/\partial \theta$의 극값 시점이 파라미터 $\theta$의 정보 최대 지점이다. Bi-exponential의 경우 intercept ($A$, $B$)는 $t=0$에서, slope ($\alpha$, $\beta$)는 $t = 1/\alpha$, $1/\beta$에서 극값 (Gabrielsson Eq.5:11). $\alpha = 0.69\ h^{-1}$이면 $t = 1.4\ h$, $\beta = 0.069\ h^{-1}$이면 $t = 14\ h$ (p.400). Sigmoid $E_{max}$ 모델은 5개 design point: baseline → 20% effect → $EC_{50}$ → 80% effect → plateau (Fig.5.6). Fisher information matrix의 비선형 회귀 형태가 이론적 기반.

---

### ▣ MUST 6 — 민감도 분석 (Sensitivity Analysis)

<!-- MASTER LENS -->
**[개념 Big Idea: 거장의 시각]**

1. **왜 치명적으로 중요한가**: 데이터를 수집하기 **전에** 모델의 거동을 손으로 흔들어보지 않고 그대로 임상시험에 진입하면, "이 약물은 $V_d$가 클까 작을까?" 같은 1차원 질문에도 답하지 못하는 상태로 환자에게 dose를 결정하게 된다. **민감도 분석은 비용이 0인 사고실험**이지만 그것을 건너뛴 대가는 phase 1에서 $10M USD에 달하는 dose-finding study의 재실행이다.

2. **체화해야 할 단 하나의 직관**: 모든 파라미터는 농도-시간 곡선의 **고유한 위치(signature region)**를 지배한다 — $k_{in}$은 곡선의 수직 위치를, $k_{out}$은 baseline + 초기 downswing slope를, $IC_{50}$은 terminal phase의 수평 위치를, $t_{lag}$은 초반의 수평 shift를 결정한다. 이 매핑을 한눈에 그릴 수 있어야 다음 실험의 sampling을 어디에 둘지 결정할 수 있다.

3. **이 직관을 머릿속에 박고 아래를 읽어라**: 민감도 분석은 시뮬레이션이 아니라 **모델의 해부학(anatomy)**을 이해하는 도구다.

---

#### A. Formal Definition

**민감도 분석(sensitivity analysis)**: 초기 파라미터 추정치를 기준으로 각 파라미터를 +100% 증가, -50% 감소시키며 그 결과 농도-시간 또는 반응-시간 곡선의 형태 변화를 관찰하여, 각 파라미터가 곡선의 어느 영역에 영향을 미치는지를 시각적으로 매핑하는 기법. modeling carousel의 Step 1 (tentative model) 직후, fitting 전에 시행 (p.403).

#### B. Derivation / Code Structure

**[B-1] 절차 (§5.2.4, p.403)**:
1. 초기 추정치 $\theta_0$로 곡선 시뮬레이션.
2. 각 $\theta_i$에 대해 $0.5 \cdot \theta_{i,0}$, $\theta_{i,0}$, $2 \cdot \theta_{i,0}$ 세 값으로 곡선 생성, 다른 파라미터는 고정.
3. 세 곡선을 한 plot에 overlay.
4. 변화의 영역(early/middle/late, baseline/peak/plateau) 식별.
5. 각 파라미터의 sensitivity region이 sampling design의 직접 가이드.

**[B-2] Case Study PK18 (§5.2.4, Fig.5.9) — 2-compartment Michaelis-Menten 모델**:

| 파라미터 | 변화 시 영향 영역 | 함의 |
|---|---|---|
| $V_{max}$ | 전체 곡선 형태 (특히 saturation 영역) | 고농도 sampling 중요 |
| $K_m$ | terminal phase 형태 | terminal sampling 중요 |
| $V_c$ | 초기 distribution phase | 초기 시점(t < 1h) sampling |
| $V_t$ | 중간 phase | 중간 시점 sampling |

**[B-3] Case Study PD4 (§5.2.4, Fig.5.10) — warfarin-PCA turnover 모델**:

| 파라미터 | 변화 → 곡선 변화 | Sampling 함의 |
|---|---|---|
| $k_{in}$ ↑ | 곡선 전체 수직 상승 (baseline + steady state) | **Baseline drug-free sampling 필수** |
| $k_{out}$ ↑ | Baseline 낮아짐 + 초기 downswing 가파름 + trough 시점 좌측 이동 | 초기 downswing sampling |
| $IC_{50}$ ↑ | Terminal phase 수평 우측 shift | Upswing 시점 sampling |
| $t_{lag}$ ↑ | 초기 곡선 수평 우측 shift | 초기 시점 dense sampling |

**[B-4] CONTEXT 통합 — Toxicokinetic 설계 (§5.3.3, p.412-414)**:

§5.3.3의 핵심 통찰은 **capacity-dependent kinetics와 time-dependent kinetics의 혼동**. AUC_Day 1과 AUC_ss가 같아 보여도 saturation(capacity)과 induction(time)이 동시에 일어나면 둘 다 가려지는 phantom symmetry가 발생한다 (Fig.5.20). 따라서 toxicokinetic 설계는 minimalistic($C_{max}$만 측정)으로 충분 — full profile은 PK·DRF 단계에서만 (Table 5.6). 이 또한 사전 sensitivity 분석으로 도출된 통찰이다.

#### C. Structural Necessity

**왜 +100%/-50%인가?** 비대칭 — 파라미터는 0보다 작아질 수 없으므로(생리학적), 절반(0.5x)은 가능하지만 -100%는 불가능. 두 배(2x)는 transient toxicity 또는 신부전 환자를 표현. 따라서 +100%/-50%가 **생리학적으로 가능한 변동의 양극단**을 cover.

**왜 fitting 전에?** Fitting 후 결과로 모델 안정성을 평가하는 것은 사후 평가. 사전 sensitivity는 **모델이 데이터에 묻기 전에 모델 자체의 거동을 이해하는 행위**. 이를 통해 수렴이 안 되는 이유를 사전에 진단(예: 두 파라미터가 같은 영역에 영향 → 강한 상관 예측).

#### D. Assumptions & Boundary Conditions

- **Assumption 1**: 초기 추정치가 "physiologically plausible" — 비합리적 추정치에서 sensitivity는 의미 없음.
- **Assumption 2**: 모델 구조가 정성적으로 옳음 — 잘못된 모델의 sensitivity는 잘못된 가이드.
- **Assumption 3**: 단변량 분석 — 파라미터 하나씩만 흔듦. 다변량 상호작용은 별도 분석 필요.

#### E. Limitations

- **Local sensitivity**: 특정 추정치 주변의 거동만 — global sensitivity (Sobol indices 등)는 별도.
- **Time-domain only**: 빈도 도메인(주기적 dosing)에서의 거동은 추가 분석 필요.
- **One-at-a-time(OAT)의 한계**: 파라미터간 비선형 상호작용을 놓칠 수 있음.

#### F. Five Cognitive Layers

| 레이어 | 내용 |
|---|---|
| **L1 형식적 수학** | Local sensitivity coefficient $S_{ij} = \partial C(t_i)/\partial \theta_j \cdot \theta_j/C(t_i)$ (정규화). Global: Sobol total-order index $S_T^j$. |
| **L2 기하학적 직관** | 곡선을 손가락으로 잡고 흔들 때 어느 부분이 움직이는지 — 그곳이 그 파라미터의 "지문". |
| **L3 구조적 동일성** | 회로의 transfer function 분석, 기후모델의 perturbation analysis, 시스템 생물학의 metabolic control analysis와 동형. |
| **L4 생리학적 의미** | $k_{in}$ = 합성 속도 → 정상 상태 수준 결정 (수직). $k_{out}$ = turnover → 동역학 시간 스케일 결정 (slope + baseline). $t_{lag}$ = 흡수 지연 → 초반 시간 shift. |
| **L5 실무 투영** | NONMEM `$SIMULATION` 블록을 사전에 사용. R `mrgsolve::sim_ess()`. Phoenix WinNonlin "Trial Simulator". Phase 1 protocol을 작성하기 전 reviewer에게 "여기에 sensitivity plot 첨부" 권장. |

#### G. Zettelkasten Atom

```yaml
---
aliases: [민감도 분석, Sensitivity Analysis, Pre-fit Verification]
tags: [pharmacometrics/design, simulation/sensitivity, gabrielsson/ch5-2-4]
up: "[[Optimal Experimental Design]]"
related: ["[[편미분 최적 샘플링]]", "[[Toxicokinetic Design]]", "[[Local vs Global Sensitivity]]"]
source: "Gabrielsson & Weiner 5e, Ch.5 §5.2.4, p.403-405"
---
```

민감도 분석은 fitting 전에 각 파라미터를 +100%/-50%로 흔들어 곡선의 어느 영역에 영향을 미치는지 시각적으로 매핑한다 (Gabrielsson §5.2.4). Warfarin-PCA 모델(Case Study PD4)에서 $k_{in}$은 곡선 수직 위치를, $k_{out}$은 baseline + 초기 downswing slope를, $IC_{50}$은 terminal phase 수평 위치를, $t_{lag}$은 초반 수평 shift를 지배한다(Fig.5.10). 이 매핑이 다음 실험 sampling design의 직접 가이드. CONTEXT: §5.3.3 toxicokinetic 설계는 capacity vs time-dependent kinetics 혼동(phantom symmetry, Fig.5.20)을 사전 sensitivity로 회피하라고 권장.

---

## §5 — Confusion Pair Dissection

이 세션에서 진정으로 혼동 가능한 4개 쌍 식별. **Critical Blow는 #1 (F 검정 적용 조건)에 적용**.

---

### ▣ 혼동쌍 #1 — Nested + 동일 weighting (F-Test 적용 가능) vs Non-nested 또는 다른 weighting (F-Test 적용 불가)

<!-- CONFUSION -->

| 비교 차원 | 적용 가능 (Nested + Equal Weighting) | 적용 불가 (Non-nested 또는 Different Weighting) |
|---|---|---|
| **표면적 유사성** | 두 경우 모두 "두 모델 비교", 두 경우 모두 WRSS와 자유도가 출력됨, 두 경우 모두 통계 소프트웨어가 F 통계량을 계산해줌(거부 메시지 없이!) | |
| **수식/코드 형태** | $F^* = \frac{\|WRSS_1 - WRSS_2\|/(df_1-df_2)}{WRSS_2/df_2}$ valid (Eq.4:54) | 같은 수식이 nominally 계산되지만 분포가 F가 아니므로 $p$-value 의미 없음 |
| **구조적 지시체** | Reduced = full의 특정 파라미터 고정 (예: bi-exp에서 $B=0$ → mono-exp) | Mono-exp $C = A e^{-Kt}$ vs Linear $C = a - bt$: 어떤 파라미터 고정으로도 변환 불가 |
| **Weighting 조건** | OLS-OLS 또는 동일 WLS-WLS | OLS vs WLS, 또는 다른 $\lambda_z$의 WLS |
| **전형 사례** | Mono-exp ↔ Bi-exp ($B=0$), Ordinary $E_{max}$ ↔ Sigmoid $E_{max}$ ($n=1$), Hepatic distributed ↔ parallel-tube ($\varepsilon^2 \to 0$) | MM 소실 (가중) vs 1차 소실 (비가중): **이중 위반** (Table 4.8). Ordinary $E_{max}$ vs Linear (non-nested). |
| **변화 방향** | 모델이 더 복잡해질 때 → $WRSS$ 감소가 통계적으로 유의한지 검정. $F^* > F_{crit}$이면 추가 파라미터 채택. | 두 모델의 WRSS 차이가 어떤 분포를 따르는지 알 수 없음 → 검정 자체 불가능. |
| **실무 결과** | Phase 1 PK report: "Likelihood ratio test indicated bi-exponential model superior to mono-exponential ($\Delta OFV = 12.3$, $p < 0.001$)" — 채택 가능. | NDA Module 5: "Model selection between Michaelis-Menten and first-order elimination was based on F-test ($p < 0.01$)" → 심사관 코멘트: "Nested model assumption is violated; F-test is invalid." |
| **⚡ 기억 고리** | **F 검정은 "마트료시카 인형"의 통계학이다 — 작은 인형이 큰 인형 안에 정확히 들어맞을 때만 두 인형의 크기 차이를 비교할 수 있다. MM과 1차 소실은 마트료시카가 아니라 별개의 두 조각상이며, 한쪽이 다른 한쪽을 일부분으로 포함하지 않는다. 그리고 두 조각상의 무게를 다른 단위(kg vs lb)로 잰 것이 weighting 위반이다.** | |
| **🩸 치명적 타격 (Critical Blow)** | 이 혼동을 품고 NDA Module 5에 "F-test was used to compare Michaelis-Menten and first-order elimination models, supporting the selection of MM model ($p < 0.001$)" 문장을 포함시키면, FDA 심사관이 발급하는 Deficiency Letter는 "**The cited F-test is statistically invalid as the two models are non-nested and were fit under different weighting schemes (Table 4.8 of Gabrielsson & Weiner 5e). Resubmit with appropriate model discrimination methodology — e.g., information criteria under harmonized weighting or comparison via simulation-based posterior predictive checks.**" 이 결함이 Major Deficiency로 분류되면 6-month review extension. | |

---

### ▣ 혼동쌍 #2 — 상관계수 r vs 진정한 GOF (Goodness-of-Fit)

<!-- CONFUSION -->

| 비교 차원 | 상관계수 r (관찰 vs 예측) | 진정한 GOF (잔차 분석 + 정밀도 + 모델 적합 영역) |
|---|---|---|
| **표면적 유사성** | 둘 다 "관찰-예측 일치도"를 정량화하는 듯 보임. 둘 다 0~1 사이 값. 둘 다 "높을수록 좋다"는 직관 자극. | |
| **수식 형태** | $r = 1 - \frac{\sum (X_i - \bar{X})(C_i - \bar{C})}{\sum(X_i - \bar{X})^2 \sum(C_i - \bar{C})^2}$ (Eq.4:53) | 잔차 정규성 검정 + 잔차 패턴 + CV% + correlation matrix + AIC |
| **구조적 지시체** | 두 변량의 선형 관계 강도 (대칭 측정) | 모델 가정 위반 여부 (구조·변량·정규성 분리 진단) |
| **변화 방향** | 더 큰 dynamic range를 갖는 데이터에서는 r이 자동으로 높아짐 — outlier 효과 약화 | 잔차 패턴은 outlier·systematic deviation을 직접 노출 |
| **임상/모델링 결과** | **Fig.4.53 직접 인용**: 같은 데이터에 대해 OLS 적합 결과 $r = 0.96$, IRLS 적합 결과 $r = 0.94$ — 그러나 OLS는 terminal observation을 systematic 하게 underestimate (잘못된 fit), IRLS가 진정한 best fit. **r 값만 보면 OLS가 우수하다고 잘못 결론**. | 잔차 플롯에서 OLS는 terminal phase에서 systematic negative trend (구조 모델 결함 신호), IRLS는 random scatter — 진정한 fit 품질 정확히 반영. |
| **⚡ 기억 고리** | **상관계수 r은 "곡선이 데이터에 얼마나 가까운가"가 아니라 "두 변량이 얼마나 함께 변하는가"를 잰다. 큰 dynamic range를 가진 데이터에서는 어떤 모델이라도 r이 높아진다 — 마치 키 큰 사람과 작은 사람을 함께 plot하면 키-체중 상관이 자동으로 강해 보이는 것과 같다. r은 곡선이 데이터의 패턴을 따라가는지가 아니라 "모든 점이 대각선 근처에 있는지"만 묻는다. 따라서 r=0.96이라도 systematic underestimate가 있을 수 있고, r=0.94라도 random scatter의 best fit일 수 있다.** | |

---

### ▣ 혼동쌍 #3 — 구조 모델 오류 vs 변량 모델 오류 (잔차 패턴 진단)

<!-- CONFUSION -->

| 비교 차원 | 구조 모델 오류 (Structural Model Misspecification) | 변량 모델 오류 (Variance Model Misspecification) |
|---|---|---|
| **표면적 유사성** | 둘 다 "잔차 플롯에 패턴이 있다"로 표현됨. 둘 다 모델 결함의 신호. | |
| **잔차 플롯 형태** | 잔차 vs **시간** plot에서 systematic pattern: banana(U), inverted-U, linear drift (Fig.4.43, 4.50 upper row) | 잔차 vs **농도** plot에서 fan/funnel shape — 작은 농도에 작은 잔차, 큰 농도에 큰 잔차 (Fig.4.42 left, 4.50 lower row) |
| **수식적 원인** | 모델 함수 $f(t; \theta)$가 데이터의 진정한 메커니즘을 표현하지 못함 — 추가 항(exponential, lag-time, baseline) 필요 | $\varepsilon \sim N(0, \sigma^2)$의 가정 위반 — 분산이 농도에 비례 ($\sigma_i^2 \propto \hat{C}_i^{2}$) 등 |
| **시간 의존성** | 잔차 패턴이 시간 축에 따라 systematic — 특정 phase에서 over/under-prediction | 잔차 패턴이 농도(또는 예측값) 축에 따라 systematic — 분산의 heteroscedasticity |
| **처방** | (1) Exponential term 추가 (mono → bi → tri), (2) lag-time 추가, (3) baseline term 추가, (4) 다른 메커니즘(turnover, TMDD, MM) | (1) Constant absolute → constant relative weighting, (2) IRLS, (3) 변량 파라미터 $\lambda_z$ 추정 |
| **임상/모델링 결과** | 처방을 잘못 선택하면 (구조 결함을 변량 결함으로 진단): 가중치만 바꾸고 같은 잘못된 메커니즘으로 외삽 → Phase 2 dose-finding 실패 | 처방을 잘못 선택하면 (변량 결함을 구조 결함으로 진단): 불필요한 추가 파라미터로 모델 over-parameterize → 정밀도 악화 + 수렴 문제 |
| **⚡ 기억 고리** | **시간이 묻는 잔차 = "당신의 모델이 어떻게 생겼는가?" — 형태(structure) 결함. 농도가 묻는 잔차 = "당신의 모델이 어떤 노이즈를 가정하는가?" — 분산(variance) 결함. 잔차를 시간 축으로 plot하지 않고 농도 축으로만 plot하면 구조 결함이 변량 결함으로 보일 수 있다. 둘 다 plot하라.** | |

---

### ▣ 혼동쌍 #4 — Outlier Type A (수직 deviation, 저 leverage) vs Outlier Type B (시간축 deviation, 고 leverage)

<!-- CONFUSION -->

| 비교 차원 | Type A — Vertical Outlier (저 leverage) | Type B — High-Leverage Outlier |
|---|---|---|
| **표면적 유사성** | 둘 다 "이상치"로 분류, 둘 다 GOF 플롯에서 곡선에서 멀리 떨어진 점 | |
| **위치 (Fig.4.59)** | Y축(농도) 방향으로 곡선에서 멀리, 시간 축 위치는 평범 | Y축뿐 아니라 시간 축 방향으로도 데이터 범위 끝에 위치 |
| **회귀에 미치는 영향** | 파라미터 추정치 자체에는 큰 영향 없음 (curve를 끌어당기는 leverage가 약함) — 하지만 분산을 키워 **정밀도(CV%)를 악화** | $\lambda_z$ 등 terminal slope 파라미터 추정치를 그 outlier 방향으로 끌어당김(bias) — **정확도 악화 + 거짓 정밀도(낮은 CV%)** |
| **잔차에 미치는 영향** | Standardized residual이 크게 나타남 (>2 또는 <-2) — 쉽게 발견 | 회귀가 outlier를 향해 끌려가므로 그 점의 잔차가 작아질 수 있음 — **숨은 outlier** |
| **임상/모델링 결과** | 보고된 파라미터의 신뢰구간이 넓어져 임상 외삽 시 보수적 dose 선택 강제 | 보고된 파라미터가 잘못된 방향으로 정밀하게 추정 → 자신감 있게 잘못된 dose 결정 |
| **처방** | (1) outlier 원인 조사 (분석적 오류, 환자 비순응), (2) 가중치 robust regression, (3) 보고서에 outlier 명시 | (1) Leverage 진단 (Cook's distance, hat matrix), (2) 해당 시점 추가 sampling으로 leverage 분산, (3) sensitivity analysis로 그 점 제외 시 결과 변화 평가 |
| **⚡ 기억 고리** | **시소(Fig.4.59 inset)를 떠올려라 — 받침점에 가까운 outlier(Type A)는 시소를 거의 못 움직인다(낮은 leverage). 받침점에서 먼 outlier(Type B)는 같은 무게로도 시소를 크게 기울인다(높은 leverage). Type A는 "시끄럽지만 무력하다" — 정밀도만 떨어뜨린다. Type B는 "조용하지만 치명적이다" — 정확도를 망가뜨리고 거짓 정밀도로 위장한다.** | |

---

## §7 — Self-Test: Active Recall Module

총 9개 질문 — 회상 4개(★/★★) + 적용 5개(★★/○) + Socratic Dilemma 1개(★★ 보스).

---

### Q1. [회상 ★★]

<!-- SELF-TEST -->
Bi-exponential 모델 $C = A e^{-\alpha t} + B e^{-\beta t}$에서 $\alpha$ 파라미터의 정보가 최대로 담긴 sampling 시점을 도출하는 수식과 함께 답하라. $\alpha = 0.69\ h^{-1}$이면 구체적으로 몇 시간인가?

<details>
<summary>정답 공개</summary>

$$\frac{\partial C}{\partial \alpha} = -A \cdot t \cdot e^{-\alpha t}$$

이 함수의 절댓값이 maximum이 되는 시점을 구하기 위해 $t$에 대해 미분하고 0으로:

$$\frac{d^2 C}{dt\, d\alpha} = A \alpha t e^{-\alpha t} - A e^{-\alpha t} = 0$$
$$\Rightarrow t^* = \frac{1}{\alpha}$$

$\alpha = 0.69\ h^{-1}$이면 $t^* = 1/0.69 \approx 1.45\ h$. (Gabrielsson Eq.5:11, p.400 — 정확히 1.4 h)

**다음 깊이 질문**: 만약 sampling 횟수가 더 늘어나서 $\alpha$, $\beta$, $A$, $B$를 모두 잘 추정하고 싶다면, 단일 시점($t^* = 1/\alpha$)만 sampling하면 되는가? 그렇지 않다면 왜인가?
</details>

---

### Q2. [회상 ★★]

<!-- SELF-TEST -->
F 검정의 두 가지 적용 조건을 모두 명시하고, 각 조건이 위반되었을 때 통계적으로 무엇이 무너지는지 설명하라.

<details>
<summary>정답 공개</summary>

**조건 1 — Nested Models**: Reduced model이 full model의 특정 파라미터를 specific value(보통 0)로 고정하여 얻을 수 있어야 함.
- 위반 시 무너지는 것: $WRSS_1 - WRSS_2$가 $\chi^2$ 분포를 따르지 않음 → $F$ 통계량의 비율이 F 분포 아님 → $p$-value 무의미.

**조건 2 — Equal Weighting**: 두 모델이 동일한 weighting scheme(OLS or 동일 WLS)으로 적합되어야 함.
- 위반 시 무너지는 것: WRSS의 정의 자체가 다름 → 두 WRSS의 차이가 통계적으로 비교 불가능한 양 → likelihood function 자체가 다른 정의.

이중 위반의 전형: MM 소실(weighted) vs 1차 소실(unweighted) — Table 4.8 Gabrielsson p.389. AIC도 동일 weighting 제약을 받음.

**다음 깊이 질문**: 만약 두 모델이 nested이지만 weighting이 다르다면, weighting을 어느 한쪽으로 통일해서 다시 적합한 후 F 검정을 적용하는 것이 옳은가? 어떤 추가 검토가 필요한가?
</details>

---

### Q3. [회상 ★]

<!-- SELF-TEST -->
잔차 vs 시간 plot에서 banana shape(U자형) 패턴이 관찰되었다. 이것이 의미하는 모델 결함과 그 처방은 무엇인가? 같은 데이터의 잔차 vs 농도 plot에서 fan shape이 관찰된다면 처방은 어떻게 달라지는가?

<details>
<summary>정답 공개</summary>

**Banana shape (잔차 vs 시간)**: **구조 모델 결함** — 모델이 데이터의 메커니즘을 표현하지 못함. 처방: exponential term 추가 (mono → bi → tri-exponential), 또는 더 적절한 메커니즘 모델 채택. Gabrielsson Fig.4.43 A1.

**Fan shape (잔차 vs 농도)**: **변량 모델 결함** — 분산의 heteroscedasticity. $\sigma^2$가 농도 의존적. 처방: constant absolute weighting → constant relative weighting (Eq.4:49의 $\lambda_z = -2$)으로 전환. Gabrielsson Fig.4.42 left, Fig.4.50 D-F.

핵심: **시간 축은 "구조"를 묻고, 농도 축은 "분산"을 묻는다**. 두 plot 모두 보지 않으면 결함의 종류를 구별할 수 없다.

**다음 깊이 질문**: 두 결함이 동시에 존재할 가능성이 있을 때, 어느 결함을 먼저 해결해야 하는가? 그 순서의 이유는?
</details>

---

### Q4. [회상 ★]

<!-- SELF-TEST -->
Sigmoid $E_{max}$ 모델의 5개 design points(p.402, Fig.5.6)를 어디에 배치하는가? 각 시점에서 어떤 파라미터의 정보가 최대로 추출되는가?

<details>
<summary>정답 공개</summary>

| Design Point | 농도 위치 | 추출 파라미터 |
|---|---|---|
| 1 | Baseline (C → 0) | $E_0$ |
| 2 | ~20% effect 농도 | $n$ (sigmoidicity) |
| 3 | $C = EC_{50}$ (inflection point) | $EC_{50}$ |
| 4 | ~80% effect 농도 | $n$ |
| 5 | High plateau (C → ∞) | $E_{max}$ |

이는 편미분 $\partial E/\partial \theta$의 극값 위치 (Eq.5:12-5:14, Fig.5.5)에서 도출. $\partial E/\partial n$은 ~20%와 ~80%에서 두 극값 — 그래서 design points 2, 4가 모두 $n$에 기여. 실무에서는 이 5개 외에 robustness를 위해 추가 sampling.

**다음 깊이 질문**: 만약 환자 간 $EC_{50}$이 매우 다르다면(coefficient of variation 100%), 단일 prior에 기반한 5개 design points로 충분한가? 무엇을 추가해야 하는가?
</details>

---

### Q5. [적용 ★★]

<!-- SELF-TEST -->
당신은 Phase 1 SAD(Single Ascending Dose) 시험의 PK 분석을 수행 중이다. 1구획 IV bolus 모델로 적합 결과 $r = 0.97$, OFV가 매우 낮음, 모든 시점이 곡선 가까이에 위치. 그러나 잔차 vs 시간 plot에서 0–4 h는 systematic positive 잔차, 4–24 h는 systematic negative 잔차를 보인다. 다음 단계를 결정하라.

<details>
<summary>정답 공개</summary>

**진단**: 1구획 모델이 distribution phase를 capture하지 못함 — 잔차의 systematic pattern(banana shape의 좌우 반전 형태)이 명확한 구조 모델 결함 신호. 높은 r과 낮은 OFV는 dynamic range가 큰 데이터에서 자동으로 나타나는 현상이므로 신뢰할 수 없음(Fig.4.53 Gabrielsson 직접 인용).

**조치**:
1. 2구획 모델로 재적합 — bi-exponential decline 시도.
2. 두 모델은 nested(2구획에서 distribution phase의 추가 항을 0으로 고정 시 1구획에 가까워짐, 정확하게는 $\alpha \to \beta$ limit) — F 검정 또는 LRT 적용.
   - 단, "1구획"은 엄밀하게는 2구획의 nested case가 아닌 limiting case로 해석되는 경우가 있어 LRT의 boundary parameter problem 주의 — 보다 안전하게는 AIC 비교.
3. 잔차 플롯 재확인 — random scatter 회복 여부.
4. 정밀도(CV%)와 상관행렬 검토 — distribution rate constant들의 분리 가능성 평가.

**핵심**: r 값이나 OFV가 좋아도 잔차 패턴이 systematic이면 모델은 부적합. r은 곡선이 데이터를 따라가는지가 아니라 "모든 점이 대각선 근처인지"만 측정.

**다음 깊이 질문**: 만약 2구획 모델 적합 결과 $V_c$와 $V_t$의 상관이 $r = -0.96$이라면, 모델을 채택할 것인가? 다음 SAD cohort의 sampling을 어떻게 변경할 것인가?
</details>

---

### Q6. [적용 ★★]

<!-- SELF-TEST -->
warfarin-PCA turnover 모델(Fig.5.10)에서 $k_{out}$의 정밀도를 가장 효과적으로 향상시킬 수 있는 sampling 시점은 어디인가? 왜 그 시점이 다른 시점들보다 우월한가?

<details>
<summary>정답 공개</summary>

**최적 시점**: 약 25 h와 ~100 h 부근 (Fig.5.8, p.402-403).

**이유**:
- 25 h: 초기 downswing의 가장 가파른 부분 — $k_{out}$이 곡선 slope를 직접 결정하는 영역. $\partial R/\partial k_{out}$가 큰 negative 극값.
- 100 h: 회복(upswing) phase의 변곡점 부근 — turnover 동역학이 baseline 회복으로 표현되는 영역. $\partial R/\partial k_{out}$가 작은 positive 극값.

**왜 baseline(t=0)이 아닌가?** Baseline은 $k_{in}/k_{out}$ 비율만 결정 → $k_{in}$, $k_{out}$ 분리 불가능. 두 파라미터가 강하게 음의 상관.

**왜 plateau(steady state)가 아닌가?** Plateau에서는 $k_{in}$이 곡선 위치를 지배 → $k_{out}$ 정보 minimal.

**핵심**: sampling은 "균등하게 펼치는" 것이 아니라 **편미분이 극값인 시점에 집중**해야 한다. 민감도 분석(§5.2.4 Fig.5.10)에서 $k_{out}$ 변화가 곡선 형태를 가장 크게 바꾸는 영역이 곧 정보 영역.

**다음 깊이 질문**: 만약 환자 간 $k_{out}$ 변이가 크다면, 단일 환자의 25 h, 100 h 측정으로 충분한가? Population optimal design에서는 어떻게 달라지는가?
</details>

---

### Q7. [적용 ★★]

<!-- SELF-TEST -->
당신은 in vitro 효소 kinetics 데이터(반복 측정 가능)를 mono-exponential 모델로 적합했다. WRSS=92.67, df=25. 같은 시점 반복 측정에서 pure error SS=23.61, df=21. 이 모델이 데이터에 적합한지 통계적으로 판정하라. 부적합하다면 다음 모델은?

<details>
<summary>정답 공개</summary>

**Lack-of-Fit F 검정 (Eq.4:51, §4.7.3)**:

$$F_{LOF} = \frac{(WRSS - \text{Pure Error SS})/(df_{res} - df_{pure})}{\text{Pure Error SS}/df_{pure}}$$

$$= \frac{(92.67 - 23.61)/(25 - 21)}{23.61/21} = \frac{69.06/4}{1.124} = \frac{17.27}{1.124} = 15.35$$

**판정**: $F_{LOF} = 15.35$를 $F_{crit}(\alpha=0.05, \Delta df=4, df_2=21) = 2.76$과 비교 → $F_{LOF} \gg F_{crit}$ → **lack of fit이 통계적으로 유의** ($p < 0.05$). Mono-exponential 모델은 데이터에 부적합 (Gabrielsson Table 4.7 직접 인용).

**다음 모델**: Bi-exponential 시도. 이는 mono-exponential의 nested extension이므로 §4.8.1의 모델 비교 F 검정도 적용 가능 ($B = 0$ 고정 시 reduced).

**중요한 구분**: §4.7.3의 lack-of-fit F 검정과 §4.8.1의 모델 비교 F 검정은 **다른 도구**. 전자는 단일 모델의 적합도 검정 (반복 측정 필요), 후자는 두 모델 비교 (nested 필요).

**다음 깊이 질문**: 만약 데이터에 같은 시점 반복 측정이 없다면(예: 환자별 1회 측정), pure error를 어떻게 추정할 것인가? §4.7.3의 LOF F 검정은 그 경우 시행 가능한가?
</details>

---

### Q8. [적용 ○]

<!-- SELF-TEST -->
당신의 모델 적합 결과 두 파라미터 $V_{max}$와 $K_m$의 상관이 $r = -0.97$이다. 다른 GOF 지표는 모두 우수 (잔차 random, CV% < 30%, AIC 낮음). 이 모델을 NDA에 제출 가능한가? 그렇지 않다면 어떤 조치가 필요한가?

<details>
<summary>정답 공개</summary>

**진단**: 강한 음의 상관($|r| > 0.95$)은 데이터로 두 파라미터를 분리할 수 없다는 신호. 보고된 $V_{max}$와 $K_m$ 값은 "그 데이터에서 가능한 두 파라미터의 임의 조합 중 하나"일 뿐.

**왜 다른 GOF가 좋아도 문제인가**: 좋은 fit + 강한 상관 = "fit는 좋지만 추정치 자체가 의미 없음" (Gabrielsson p.380, p.383). 환자 간 외삽 시 두 파라미터 중 하나가 변하면 다른 하나로 보상되어 동일한 fit를 내지만 임상 결과는 크게 다를 수 있음.

**조치**:
1. **즉시 채택 금지** — NDA 제출 불가. 심사관 코멘트 예상: "The reported $V_{max}$ and $K_m$ are highly correlated ($r = -0.97$); independent identifiability is not established."
2. **Sampling design 점검** — Fig.4.55-4.57 Gabrielsson에 따라 농도 범위가 좁거나 plateau가 부족한지 확인.
3. **추가 실험 설계** — saturation 영역(고농도, $V_{max}$ 정보)과 linear 영역(저농도, $K_m$이 실질적 영향) 모두를 cover하는 dose range로 재설계.
4. **하나를 fix하는 옵션** — literature value 또는 in vitro 데이터로 $K_m$을 fix 후 $V_{max}$만 추정 (단, fix의 합리성을 정당화 필요).
5. **모델 단순화** — $C \ll K_m$이면 1차 소실로, $C \gg K_m$이면 0차로 단순화 (특수 케이스).

**핵심**: 좋은 fit이 좋은 추정치를 보장하지 않는다. 정밀도와 상관은 fit과 분리해서 진단해야 한다.

**다음 깊이 질문**: 만약 sampling design을 변경할 수 없다면(이미 끝난 임상시험), Bayesian 접근으로 prior를 도입하는 것이 옳은가? 그 prior는 무엇으로 정당화하는가?
</details>

---

### Q9. [보스 딜레마 ★★] — Socratic Dilemma

<!-- SELF-TEST -->
당신은 신약 X의 NDA Phase 3 PopPK 보고서를 마감 1주일 앞두고 있다. 기존 분석에서 1차 소실 모델(weighting: constant absolute, OLS)로 적합한 결과 GOF는 양호하지만, 일부 환자(고용량 cohort)에서 잔차의 systematic positive trend가 관찰되어 Michaelis-Menten 비선형 소실의 가능성이 제기되었다.

새로 MM 모델(weighting: constant relative — 고농도에서 분산이 농도에 비례하므로)로 적합한 결과, MM 모델이 systematically 더 낮은 WRSS를 보이고 잔차도 random하다. 그러나 두 모델 비교에 사용 가능한 통계 도구가 제한적이다:

**옵션 A**: F 검정으로 두 모델 비교, $p$-value 보고하며 MM 모델 채택. 마감을 지킬 수 있고 보고서 logic이 명료하다.

**옵션 B**: 두 모델을 동일 weighting (예: 둘 다 constant relative WLS)으로 재적합 후 AIC 비교. 추가 1주일 작업 필요, 마감 연장 신청해야 함.

**옵션 C**: F 검정과 AIC를 모두 포기하고, 잔차 패턴 + 임상 외삽 plausibility만으로 MM 모델 채택. "Statistical model discrimination was supplemented with mechanistic considerations" 문구로 방어.

NDA 심사관의 시각, 임상 약물학적 신뢰성, 마감 압박을 모두 고려하여 어느 옵션을 선택하는가? 그리고 그 선택을 어떻게 NDA 보고서에서 방어하는가?

<details>
<summary>정답 공개 — 수석 모델러의 Trade-off 논리</summary>

**먼저, 옵션 A는 절대 불가**. F 검정은 두 가지 동시 위반 — non-nested(MM과 1차 소실) + 다른 weighting (Table 4.8 Gabrielsson p.389). 보고서에 명시되면 심사관이 즉시 invalid로 판정 → Major Deficiency Letter. 마감을 지키는 듯 보이지만 6-month review extension을 자초.

**옵션 B가 정도(正道)**: 동일 weighting으로 통일 후 AIC 비교는 통계적으로 valid (단, AIC도 동일 weighting 조건은 Gabrielsson 명시). 어느 쪽 weighting을 선택할지의 추가 정당화도 필요(잔차 패턴 기반 = constant relative가 일반적으로 더 합리적). 마감 연장 신청은 정성적 손실이지만, 통계적 무결성을 확보. NDA 심사관 시각: "Given the model dimensionality difference and structural non-nestedness, AIC under harmonized weighting is the appropriate criterion; the choice of constant relative weighting is justified by [잔차 분석 인용]."

**옵션 C는 보조적**: 잔차 패턴 + 메커니즘 plausibility만으로의 채택은 통계 도구 부재 시의 fallback. 단독 사용은 권장되지 않으나, 옵션 B와 결합 시 강력한 cross-validation. "AIC indicated MM model superior ($\Delta AIC = X$); this conclusion is supported by [잔차 random scatter] and [고용량 환자에서 saturation kinetics의 임상 약물학적 plausibility]."

**최종 권장**: **옵션 B + 옵션 C 결합**. 마감 연장은 통계적 결함보다 가벼운 손실. 1주일 추가 작업의 비용 = 수십만 USD, 6-month extension의 비용 = 수천만 USD + 시장 진입 지연.

**규제 보고서 방어 논리**:
> "Following observation of systematic positive residuals at high doses, both first-order and Michaelis-Menten elimination models were evaluated. To enable valid statistical model discrimination, both models were refit under harmonized weighting (constant relative residual error model, justified by post-hoc residual analysis showing concentration-proportional variance). Akaike Information Criterion comparison favored the Michaelis-Menten model ($\Delta AIC = X$). This finding is mechanistically consistent with the saturable hepatic metabolism observed in vitro for compound X (CYP3A4 $K_m$ = Y µM, comparable to the maximal observed plasma concentration). F-test was not applied as the two models are non-nested (Gabrielsson & Weiner 5e, p.389)."

**핵심 통찰 (수석 모델러의 시각)**: 통계 도구의 적용 조건을 honoring하는 것은 마감 압박과 trade-off가 아니다. 잘못된 도구로 빠르게 도착하는 것은 실제로는 가장 늦게 도착하는 길이다. 통계적 무결성과 시간은 trade-off가 아니라 같은 방향이다 — 단, **사전에** 그 사실을 인식할 때만 그렇다.

</details>

---

## §8 — Meta-Frame & Big Picture

### A. Positioning (28세션 PK/PD 지식 아키텍처에서의 위치)

**이전에 온 것**:
- Session 01-04: Compartment 모델 ODE 도출 (1구획, 2구획, oral absorption, infusion)
- Session 05-08: PK 핵심 파라미터 (CL, Vd, hepatic extraction, F)
- Session 09-12: PD 모델 (sigmoid $E_{max}$, indirect response, turnover, TMDD)
- Session 13-14: Modeling carousel의 전반부 — Tentative model, Design, EDA의 시각화 도구

**바로 다음에 오는 것**:
- Session 16: 가중치 모델 심화 — `[확인 필요 — pp.365-367 누락분 보강]` Constant absolute, constant relative, mixed error model
- Session 17: NONMEM 추정 알고리즘 — FO, FOCE, FOCEI, Laplacian, SAEM의 수학적 차이와 OFV 해석
- Session 18-20: PopPK NLME — η-shrinkage, ε-shrinkage, $OMEGA·$SIGMA 행렬 진단

**이 기반에 결정적으로 의존하는 고급 도메인**:
- **PopPK / NLME**: §4.7.5의 정밀도 개념 → individual estimate의 η-shrinkage 진단. §4.7.7의 상관 → fixed effect 간 identifiability 평가.
- **Optimal Design Theory**: §5.2.3의 편미분 접근 → Population Fisher Information Matrix → PopED, PFIM 소프트웨어의 이론적 기반.
- **Bayesian Pharmacometrics**: §4.7.5 univariate vs planar CI → posterior credible interval의 marginal vs joint 차이.
- **Model-Based Drug Development (MBDD)**: §4.8.1의 모델 비교 → MID3 framework의 model selection step.
- **Regulatory Pharmacometrics (NDA/IND)**: §4.10 checklist → FDA Guidance "Population Pharmacokinetics" (Feb 2022)의 GOF 평가 항목과 직접 매핑.

### B. Dependencies — 본 세션을 대충 넘겼을 때의 구체적 실패 모드

**실패 모드 1 — F 검정의 nested + weighting 조건 무시**:
- **즉각 결과**: §4.8.1 도구를 무차별 적용 → Phase 3 PopPK 보고서에서 MM vs 1차 소실 비교에 F 검정 인용.
- **나비효과**: NDA Module 5에서 심사관이 Major Deficiency 발급 → 6-month review extension → 특허 보호 기간의 6개월 손실 (시장 가치 수천만~수억 USD).
- **추적 가능한 인과**: 잘못된 모델 선택 → 잘못된 dose-response 외삽 → Phase 4 환자에서 예상보다 높은 toxicity 또는 낮은 efficacy → 시판 후 dose adjustment 또는 black-box warning 추가.

**실패 모드 2 — 정밀도 진단의 sampling design으로의 환류 부재**:
- **즉각 결과**: Phase 1에서 두 파라미터의 상관이 $-0.95$로 나와도, 그것을 "모델 결함"으로 오인 후 모델을 단순화.
- **나비효과**: 진정한 메커니즘이 dose-response 외삽에서 다르게 작동 → Phase 2 dose-finding이 Phase 1 prediction과 불일치 → 추가 dose-finding cohort 필요 → 임상 개발 일정 지연.
- **추적 가능한 인과**: 정밀도 ≠ 모델 fit이라는 인식 부재 → "다음 실험 설계 변경"이 아닌 "모델 단순화"라는 잘못된 처방 → 동일한 sampling design으로 다른 cohort에서 동일한 문제 반복.

### C. Professional Moat — 이 섹션 내용에 직접·구체적으로 답하라

**Vol I 프레임 (Gabrielsson & Weiner 검출됨)**:

> "NONMEM을 실행하고 GOF 플롯을 생성할 수 있는 주니어 모델러와, 2구획 모델을 데이터에 적합시킬 수 있는 AI가 이미 존재한다. 이 섹션의 원리를 — 메커니즘이 아닌 구조적 이해의 수준에서 — 진정으로 내면화한 연구자는 그 둘 중 어느 것도 복제할 수 없는 무엇을 갖고 있는가?"

**답 — 구조적 필연성 수준의 답**:

이 세션의 6개 MUST 카드를 진정으로 내면화한 모델러는 다음을 가질 수 있다:

**(1) 통계 도구의 적용 조건을 즉시 판별하는 reflex** — F 검정이 nested + 동일 weighting의 두 조건을 동시에 만족할 때만 유효함을 본능적으로 안다. NONMEM 출력의 OFV difference를 보는 순간 "이것이 LRT의 $\chi^2$ 분포를 따르려면 두 모델이 nested여야 한다"는 검증을 자동으로 수행한다. AI는 출력값을 신뢰성 있게 비교할 수 있지만, **"이 비교가 의미 있는 비교인가?"**라는 메타 질문은 도구 외부의 판단이며, 이는 적용 조건의 구조적 이해에서만 나온다.

**(2) 잔차 패턴을 모델 결함의 청사진으로 즉시 번역하는 능력** — Banana shape를 보는 순간 "exponential term 부족", lag bulge를 보는 순간 "absorption delay", fan shape를 보는 순간 "weighting 모델 변경"이라는 처방이 즉각 도출된다. 이는 단순한 패턴 매칭이 아니라 **잔차의 시간 축 vs 농도 축 분해**라는 구조적 분리가 머릿속에 자리잡았기 때문에 가능하다. AI는 모든 가능성을 나열할 수 있지만, **어느 처방이 어느 결함과 1:1 대응하는지의 인과 사슬**은 §4.7.2 Fig.4.43, 4.50의 구조를 내면화한 사람만이 즉시 그릴 수 있다.

**(3) "좋은 fit + 나쁜 추정치"의 이중 진단 능력** — 이는 §4.7.5와 §4.7.7을 연결하는 통찰. r 값과 OFV가 좋아도 CV%와 correlation matrix를 보지 않으면 모델은 검증되지 않은 것. 이 사실을 모르는 모델러는 NDA 제출 전 Phase 3 데이터에서 "fit는 좋다"고 판정한 후 심사관에게 "your $V_{max}$ and $K_m$ are not independently identified"라는 코멘트를 받는다. AI는 모든 지표를 출력하지만, **어느 지표가 어느 단계에서 critical한지의 위계**는 modeling carousel 6단계의 구조를 사이클로 이해한 사람만이 안다.

**(4) Sampling design → 정밀도 → 모델 신뢰성의 환류 사슬을 사이클로 보는 시각** — §4.7.7의 정밀도 진단이 §5.2.3의 편미분 기반 설계로 환류된다는 것이 modeling carousel의 핵심. 이를 사이클로 이해한 모델러는 Phase 1 데이터의 정밀도 진단 결과를 즉시 Phase 2 protocol amendment의 sampling schedule 변경으로 번역한다. 단발성 분석이 아니라 **반복적 정보 축적의 설계자**가 된다.

**(5) 통계 무결성과 마감 압박을 trade-off가 아니라 같은 방향의 힘으로 인식하는 메타 시각** — 보스 딜레마(§7 Q9)에서 보았듯, 잘못된 도구로 빠르게 도착하는 것은 실제로 가장 늦게 도착하는 길이다. 이 인식은 단순한 "윤리"가 아니라 **규제 시스템과 임상 약물학의 구조적 작동 방식에 대한 깊은 이해**에서 나온다. 6-month review extension이 1-week 마감 연장보다 수십 배 큰 손실이라는 것은 통계 교과서가 가르치지 않지만, NDA 제출 경험이 있는 시니어 모델러는 그것을 직관으로 안다.

이 5가지 — **적용 조건 reflex + 잔차 청사진 reading + 이중 진단 + 사이클 환류 시각 + 통계-시간 정합 인식** — 이 본 세션의 진정한 학습 결과이며, 이것이 NONMEM 출력을 생성하는 능력 위에 쌓이는 **구조적 이해의 무형 자산**이다.

### D. CONTEXT 통합 — §4.10 Checklist (Gabrielsson p.391)

본 세션의 6개 MUST를 모두 통합하면, modeling carousel 한 사이클 종료 시 다음 5개 질문에 답할 수 있어야 한다:

1. 모델이 생물학적 타당성(biological relevance)을 갖는가? → MUST 1, 6
2. 적합 곡선이 데이터의 trend를 모방(mimic)하는가? → MUST 2
3. 파라미터가 충분한 정밀도로 추정되는가? → MUST 4
4. 잔차에 systematic deviation이 없는가? → MUST 2
5. 잔차 plot이 random scatter를 보이는가? → MUST 2

이 5개 질문 중 하나라도 답이 "No"이면, 모델 또는 weighting scheme이 잘못된 것 (Table 4.9 Gabrielsson). **이 checklist가 GOF 평가의 최종 종합 도구**이며, 6개 MUST의 통합 활용 사례다.

<!-- RECAP -->
**§8 종합**: 본 세션은 modeling carousel의 실행 척추다. 6개 MUST는 사이클의 6개 노드를 채우며, 4개 혼동쌍은 사이클이 무너지는 6가지 함정 중 가장 자주 일어나는 것들이다. F 검정의 적용 조건(Apex)은 NDA 심사의 가장 빈번한 결함 사유이며, 이것을 내면화한 모델러는 통계 도구의 권위에 위장된 무의미한 숫자를 즉시 식별한다. 다음 세션(NONMEM 추정 알고리즘)은 본 세션의 통계 추론 도구가 NLME 맥락에서 어떻게 OFV·LRT로 확장되는지를 다룬다.

---

## ✦ STEP 1 완료 (Phase 1 출력 종료)

다음이 준비되었습니다:
- §1 세션 헤더 & 로드맵 (modeling carousel 위치, Big Idea, 개념 항법도, 지식 그래프)
- §2 개념 해부 카드 (**6개** 개념, ⚡ Apex Concept: **F 검정 적용 조건**)
- §5 혼동 쌍 해부 (**4개** 쌍, 🩸 Critical Blow 적용: **F-Test Nested/Weighting 위반 → NDA Deficiency Letter**)
- §7 자기 테스트 (**9개** 질문, Socratic Dilemma 보스 딜레마 포함 — Q9 마감 압박 vs 통계 무결성)
- §8 메타프레임 & 빅 픽처 (5가지 무형 자산 + Checklist 통합)
- 감지된 소스 유형: **Vol I — 데이터 이론 (Gabrielsson & Weiner 5e)**
- Data Anchoring 소스: Fig.4.17 (IV bolus 두 피험자 K=0.01/min, t½≈65min, V=10L, AUC=100,000), Fig.4.18 (A=1, B=0.8, α=0.05, β=0.003), Eq.4:22 (warfarin-PCA $k_{out}$=0.03/h), Table 4.5-4.7 ($F_{LOF}$=15.35, $F_{crit}$=2.76), Fig.4.53 (r=0.96 OLS vs r=0.94 IRLS), §5.2.3 (α=0.69→1.4h, β=0.069→14h), §5.2.4 (Case Study PK18, PD4 — warfarin)
- 누락 구간 처리: pp.365-367 (§4.5 Minimization, §4.6 Weighting) — 본문 내 [확인 필요] 플래그 4개 위치 표시, 임의 보완 없음.

---

## Phase 1 → Phase 2 전달 사항

**Phase 2 (Source Fidelity Audit) 시 우선 검증 대상**:

1. **수치 검증 (T1)**:
   - Eq.4:16 IV bolus K=0.01/min, t½ 계산 (Eq.4:17)
   - Eq.4:18 AUC 계산 100,000
   - Eq.4:22 warfarin $k_{out}$=0.03/h
   - Eq.4:51 $F_{LOF}$ = 15.35, $F_{crit}$ = 2.76
   - Eq.5:11 $t^*$ = 1/α = 1.4 h, 1/β = 14 h
   - Table 4.3 Model 1 vs Model 4 WRSS·AIC·CV% 모든 수치
   - Table 4.4 boundary scaling 수치 (A, α, B, β)
   - Table 4.7 residual / pure / LOF SS 수치

2. **개념 적용 검증 (T2)**:
   - F 검정의 4가지 nested 분류 (§4.8.1.2-4.8.1.4)
   - Table 4.8 MM vs 1차 소실 이중 위반 명시
   - Fig.4.53 r 값 OLS/IRLS 함정의 정확한 인용 (p.382)
   - Fig.4.59 Outlier A vs B leverage 차이

3. **저자 핵심 메시지 검증 (T3)**:
   - p.353 Hill 방정식 초기값 함정 직접 인용
   - p.380 "good fit + poor estimates" 직접 인용
   - p.389 Table 4.8 "Cannot use F-test because of unnested models / Cannot use AIC because different weights" 인용

4. **Coverage Audit (T5)**:
   - §5.3.3 toxicokinetic이 CONTEXT로 처리되었는지(MUST 신설 금지) 확인
   - pp.365-367 누락 구간이 임의 보완 없이 [확인 필요] 처리되었는지 확인

5. **Figure Inventory (T6)**:
   - 핵심 Figure: Fig.4.16 (carousel), Fig.4.17 (IV bolus), Fig.4.18 (bi-exp), Fig.4.20-4.21 (warfarin), Fig.4.43 (잔차 패턴), Fig.4.50 (구조 vs 변량), Fig.4.52 (다트보드), Fig.4.53 (r 함정), Fig.4.55-4.57 (정밀도/상관), Fig.4.59 (outlier), Fig.5.4 (편미분), Fig.5.6 (5개 design points), Fig.5.10 (warfarin sensitivity)

"계속"을 입력하면 Step 2 HTML 컴파일러가 실행됩니다 — 본 세션은 그러나 **Phase 1 종료 시점이며, Phase 2 (Gemini Pro Source Fidelity Audit)가 다음 단계**임을 명심합니다.

---

*Phase 1 출력 완료. 본 문서는 `01_step1_draft_v0.md`로 저장하여 Phase 2 입력으로 사용.*

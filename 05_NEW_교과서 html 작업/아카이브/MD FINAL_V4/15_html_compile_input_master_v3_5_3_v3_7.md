# 세션 15 — 모델 구축의 기술: 초기값 · GOF · 모델 판별 · 실험 설계 — v3.7

<!-- 기호 통일: 원문 첫 등장 기준으로 $Cl$, $V$, $K$, $WRSS$, $AIC$, $SC$, $V_{max}$, $K_M$ 표기를 유지함 -->

> **출처 및 범위 노트**  
> 이 핸드아웃은 Gabrielsson & Weiner 5e, *Pharmacokinetic and Pharmacodynamic Data Analysis: Concepts and Applications*의 Ch.4 §4.4, §4.7–4.10 및 Ch.5 §5.2.3–5.2.4, §5.3.3을 범위로 합니다. 검증된 페이지 범위는 p.352–364 / p.368–392 / p.399–405 / p.412–414입니다. 업로드된 PDF에는 pp.365–367(§4.5 Minimization, §4.6 Weighting) 및 pp.406–411이 포함되어 있지 않으므로, 이 페이지들에 의존하는 내용은 `[확인 필요]`로 유지합니다.

### 임상 장면: 왜 이 세션이 필요한가

10 mg IV bolus 후 반로그 기울기에서 $K=0.01\ \text{min}^{-1}$를 읽고 $t_{1/2}\approx65\ \text{min}$, $AUC=100{,}000\ \mu g\cdot L^{-1}\cdot\text{min}$, $Cl=0.1\ L\cdot\text{min}^{-1}$, $V=10\ L$를 초기 anchor로 잡는 순간이 있습니다. [Eq.4:16–4:20, p.354]  
이 anchor가 틀리면 fit은 보기 좋은 곡선을 만들 수 있어도 잘못된 basin, 잘못된 WRSS, 잘못된 모델 비교로 이어집니다. 규제 관점에서는 "fit이 좋아 보인다"가 아니라 "잔차·정밀도·비교 조건을 통과했다"는 문장으로 방어되어야 합니다.

## 학습자 항법 안내

### 이 핸드아웃 사용법

먼저 §1을 읽고 모델링 회전고리(modeling carousel)의 논리 구조를 잡으시면 됩니다. 이후 MUST 카드 여섯 장을 순서대로 공부하세요: 초기값 → 잔차 진단 → F-test/AIC/SC 타당성 → 정밀도·상관 → 편미분 샘플링 → 민감도 분석. 학습을 마친 뒤에는 §5에서 혼동쌍을 해소하고, §7에서 능동 회상을 점검하며, §8에서 세션 전체를 하나의 워크플로우 문장으로 압축하시면 됩니다.

### 학습 경로

| 학습 단계 | 집중 포인트 | 이 단계 이후 할 수 있어야 하는 것 |
|---:|---|---|
| 1 | §1 로드맵 | 이 세션이 여섯 개의 독립 기술이 아니라 하나의 닫힌 모델링 루프인 이유를 설명할 수 있다. |
| 2 | MUST 1 | 그래프·NCA 기준점(anchor)에서 초기값을 도출하고, 초기값이 나쁠 때 적합(fitting)이 왜 잘못된 결과로 이어지는지 설명할 수 있다. |
| 3 | MUST 2 | 잔차 형태(banana, fan shape, leverage point)를 구조적 문제·분산/가중치(weighting) 문제·데이터/설계 문제에 각각 연결할 수 있다. |
| 4 | MUST 3 | F-test, AIC, SC를 적용할 수 있는 조건과 적용할 수 없는 조건을 판단할 수 있다. |
| 5 | MUST 4 | 좋은 곡선 적합(curve fit)과 파라미터 식별가능성(parameter identifiability)이 서로 다른 개념임을 구분할 수 있다. |
| 6 | MUST 5 | 편미분 극값(derivative peak)을 실제 샘플링(sampling) 위치로 변환할 수 있다. |
| 7 | MUST 6 | 민감도 분석을 사용해 예측이나 독성동태 해석이 무너질 수 있는 위치를 특정할 수 있다. |
| 8 | §5/§7/§8 | 혼동쌍을 해소하고, 본문을 보지 않고 자기 테스트에 답할 수 있다. |

### 그림 사용 안내

이 자료는 저작권이 있는 교과서 그림을 직접 재현하지 않습니다. 교과서 그림은 텍스트 전용 참조 콜아웃으로 안내하며, 학습용 새 도식은 HTML 렌더링 단계에서 별도로 구현할 수 있도록 Title과 Core message 중심으로 축약했습니다.


> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** F-test·AIC/SC·$-2\log likelihood$는 계산값이 아니라 적용 조건을 먼저 통과해야 읽을 수 있는 판단 언어다.

---

<!-- SLIDE_START: §1 | title: 세션 개요와 로드맵 -->

## §1 — 세션 개요와 로드맵

### ASCII 레이어 개념 지도

```text
레이어 1 — 무엇인가
초기값 | 잔차 | 중첩성 | 정밀도/상관 | 편미분 | 민감도

레이어 2 — 어떻게 계산되는가
K → t1/2/AUC/Cl/V | WRSS/σ | F*/AIC/SC | CV%/r | derivative peak | parameter perturbation

레이어 3 — 언제, 왜 중요한가
fit 출발점 | GOF 판독 | 모델 비교 조건 | 설계 취약성 | sampling 위치 | 다음 실험/규제 방어
```

🧭 **읽는 순서:**  
카드 1 (M1): fit을 시작하기 전 어떤 숫자를 어떻게 손으로 고정해야 하는가?  
카드 2 (M2): 곡선이 맞아 보여도 잔차는 어떤 거짓말을 드러내는가?  
카드 3 (M3): F-test/AIC/SC는 언제 쓸 수 있고 언제 금지되는가?  
카드 4 (M4): 좋은 fit과 식별 가능한 parameter는 왜 다른가?  
카드 5 (M5): 어느 시간점이 어떤 parameter를 가장 잘 보이게 하는가?  
카드 6 (M6): parameter 불확실성이 임상 결론을 어디까지 흔드는가?

### 지식 그래프 위치

```text
[선행 세션: 1구획·다구획 PK, NCA, 비선형 회귀, 오차 모델]
        → [이 세션: 초기값 → 잔차 → 모델 비교 → 정밀도/상관 → 설계 피드백]
        → [후속 세션: NONMEM/PsN/xpose 기반 qualification, VPC/NPDE/bootstrap/SIR]
```


### 이 세션의 정확한 위치

본 세션은 p.352 Fig.4.16의 **모델링 회전고리(modeling carousel)**, 즉 모델링 한 사이클의 반복 구조 가운데 Step 4 Explore data, Step 5 Fit model(s), Step 6 Analyze output을 다룹니다.  그 결과를 다음 실험의 설계(Design)로 되돌리므로, 초기값 획득에서 시작해 GOF 판독, 경쟁 모델 선택, 이상치(outlier) 판단, 편미분 기반 샘플링 설계(sampling design), 민감도 분석(sensitivity analysis)까지 이어지는 한 사이클의 실행 척추입니다. [p.352]


### 핵심 아이디어(Big Idea)

이 범위의 핵심은 "좋은 통계량을 계산하는 법"이 아니라 **통계량을 적용해도 되는 조건을 아는 법**입니다. F-test, AIC/SC, 상관계수(correlation coefficient), WRSS, 편미분(partial derivatives)은 각각 강력한 도구입니다. 그러나 중첩(nested) 조건, 가중치(weighting) 조건, 잔차의 무작위성(residual randomness), 파라미터 식별가능성(parameter identifiability), 샘플링 민감도(sampling sensitivity)를 벗어나면 이 숫자들은 오히려 잘못된 모델 확신을 만듭니다. [pp.369–391, pp.399–405]


### 개념 항법도

```text
[초기값 획득] → [잔차 진단] → [F-test/AIC/SC 모델 판별]
      ↑              ↓                  ↓
[민감도 분석] ← [편미분 sampling design] ← [정밀도·상관·설계]
```


위 흐름은 닫힌 고리입니다. 초기값이 나쁘면 회귀가 잘못된 최솟값(minimum)으로 갑니다. 잔차가 무작위가 아니면 모델 또는 가중치(weighting)가 틀린 것입니다. 모델 비교 조건을 어기면 통계 검정이 무의미합니다. 그리고 파라미터가 상관되면 다음 실험의 샘플링 설계(sampling design)를 바꿔야 합니다. [p.353, pp.369–389, pp.399–405]


### 지식 그래프 위치

**선행 지식**: 1구획/다구획 모델, 비구획분석(NCA, noncompartmental analysis), 비선형 회귀(nonlinear regression), 오차 모델(error model). Ch.4 §4.5 Minimization과 §4.6 Weighting은 pp.365–367 업로드 부재로 `[확인 필요 — pp.365–367 업로드 부재]`를 유지합니다.

**후행 지식**: 현대 PopPK에서는 이 세션의 잔차 진단(residual diagnostics), 파라미터 정밀도(parameter precision), $-2\cdot\log likelihood$ 비교, 설계 피드백(design feedback)이 NONMEM/PsN/xpose류 워크플로우(workflow)로 번역됩니다. 단, 이 도구명들은 업로드 PDF의 직접 내용이 아니라 구현 환경의 번역입니다.

$$
\underbrace{-2\cdot\log likelihood}_{\text{likelihood 목적좌표}}
$$


`[교과서 외 구현 번역 — Volume II / NONMEM module로 의도적으로 뒤로 넘기는 운영 도구 목록]`
>
> **v3.4 범위 정직성 콜아웃(Scope-Honesty Callout) — 이 장이 아직 다루지 않는 실제 PopPK 운영 도구**
>
> **A. 정직한 범위 선언(Honest Boundary Statement)**  
> 이 File 15는 모델 구축(model building)의 이론적·개념적 뼈대, 즉 초기값(initial estimates), 잔차 진단(residual diagnostics), F-test 타당성, 파라미터 정밀도(parameter precision), 샘플링 설계(sampling design)를 다룹니다. 그러나 이것만으로 실제 PopPK 모델 평가 훈련(model evaluation training)이 완성되는 것은 아닙니다.
>
> **B. 뒤로 넘기는 진단 도구(Deferred Diagnostic Tools)**  
> - 시각적 예측검사(VPC; visual predictive check): 모델이 관측 자료의 분포와 시간 경향을 예측적으로 재현하는지 확인한다.  
> - prediction-corrected VPC(pcVPC): 용량(dose)·노출(exposure) 차이로 단순 VPC 해석이 어려울 때 보정된 예측검사를 수행한다.  
> - normalized prediction distribution error(NPDE): 예측분포 내에서 관측치가 얼마나 일관되게 위치하는지 평가한다.  
> - 부트스트랩(bootstrap): 재표본추출을 통해 파라미터 불확실성(parameter uncertainty)과 신뢰구간(confidence interval)을 확인한다.  
> - 그 외 시뮬레이션 기반 불확실성 방법(SIR 등): 특정 소프트웨어(software) 환경에서 보조적으로 사용되는 추가 방법이며, Volume II에서 필요 시 소개합니다.
>
> **C. 뒤로 넘기는 추정법(Deferred Estimation Methods)**  
> 다음 추정법들은 Volume II / NONMEM module에서 추정법 선택(estimation method selection)과 함께 다룰 주제입니다.  
> - 일차 추정법(FO; first-order)  
> - 조건부 일차 추정법(FOCE; first-order conditional estimation)  
> - 상호작용(interaction) 포함 FOCE(FOCEI)  
> - 라플라스 근사(Laplacian)  
> - 확률근사 expectation-maximization(SAEM, stochastic approximation expectation-maximization)
>
> **D. 모델 적격성 평가 vs 모델 검증(Model Qualification vs Validation)**  
> - 모델 적격성 평가(model qualification): 현재 목적에 대해 모델이 충분히 잘 작동하는지 확인하는 실무적 판단입니다.  
> - 모델 검증(model validation): 외부 자료 또는 독립적 근거를 통해 모델의 일반화 가능성을 더 강하게 평가하는 절차입니다.  
> - File 15는 적격성 평가의 이론적 기반을 제공하지만, VPC/NPDE/bootstrap 같은 운영적 적격성 평가 도구(operational qualification toolkit)는 별도 모듈에서 다룹니다.
>
> **E. 학습자 보호 문장(Learner Protection Sentence)**  
> 따라서 이 장을 끝낸 학습자는 "모델 구축의 이론적 문법"을 익힌 것이지, 아직 "NONMEM 운영·진단 전체 훈련"을 마친 것은 아닙니다. 이 콜아웃(callout) 이후 §2 MUST 카드로 진입할 때에는, 본 장의 GOF·F-test·정밀도 도구들이 모델링 회전고리(modeling carousel)의 **이론 절반**을 책임지고, 위 B·C 항목의 운영 도구가 **나머지 절반**을 Volume II에서 책임진다는 분담 구조를 머릿속에 고정하시면 됩니다. 상세 알고리즘 유도는 Volume II 범위로 남기되, model building과 qualification 판단에 필요한 최소 직관은 여기서 잠급니다.


### 최소 추정법 브리지: FO/FOCE/FOCEI/Laplacian/SAEM을 어떻게 읽을 것인가 [EXPERT_INFERENCE, v3.5.2]

FO, FOCE, FOCEI, Laplacian, SAEM은 단순한 계산 옵션이 아니라 "모델을 어떤 근사 언어로 읽을 것인가"를 정하는 선택지입니다. FO는 가장 단순한 linearization 관점입니다. 빠르고 출발점으로 유용하지만, 비선형성이 강하거나 IIV가 크면 평균 개체 주변의 근사가 실제 개체별 거동을 충분히 따라가지 못할 수 있습니다. FOCE는 개체별 ETA 주변에서 conditional approximation을 수행한다는 직관으로 읽으면 됩니다. 그래서 EBE, ETA diagnostic, shrinkage를 해석할 때 "개체별 정보가 얼마나 추정에 반영되었는가"라는 질문과 자연스럽게 연결됩니다. FOCEI는 residual error와 ETA 또는 prediction의 interaction이 중요할 때 그 상호작용을 근사에 반영하려는 선택입니다. Laplacian은 likelihood curvature와 비정규·복잡 likelihood를 더 잘 다루기 위한 근사로 이해하면 됩니다. SAEM은 simulation-based estimation이므로 복잡한 비선형 mixed-effects 구조에서 강점을 가질 수 있지만, 항상 자동으로 우월한 방법은 아닙니다. 핵심은 estimation method가 OFV, parameter precision, EBE/shrinkage, diagnostic 해석에 영향을 주는 판단 조건이라는 점입니다.


### 최소 qualification 브리지: GOF만으로 끝나지 않는 이유 — VPC, pcVPC, NPDE, bootstrap, SIR [EXPERT_INFERENCE, v3.5.2]

GOF는 population fit과 individual fit을 먼저 보는 기본 시각 진단입니다. 그러나 곡선이 잘 맞아 보인다는 인상만으로 predictive performance가 보장되지는 않습니다. VPC는 모델이 관측자료의 central tendency와 variability envelope을 simulation으로 재현하는지 확인하는 check입니다. pcVPC는 dose, design, covariate, time-varying prediction 차이가 커서 단순 VPC가 "모델 실패"와 "예측 스케일 차이"를 섞어 보일 때 prediction correction으로 비교 좌표를 맞추는 장치입니다. NPDE는 simulated distribution 안에서 관측값이 얼마나 이상한 위치에 놓이는지 표준화해 보는 진단으로 이해하면 됩니다. Bootstrap은 반복 resampling으로 parameter stability와 uncertainty를 확인하고, SIR은 proposal distribution을 바탕으로 parameter uncertainty를 보정하거나 평가하는 도구입니다. 실무 판단 흐름은 "GOF → residual diagnostics → VPC/pcVPC/NPDE → bootstrap/SIR → clinical/scientific plausibility"로 닫는 것이 안전합니다. 여기서 qualification은 사용 목적에 맞게 모델이 충분히 신뢰 가능한지 보는 과정이며, validation을 절대적 진실 인증처럼 쓰면 안 됩니다.

---

<!-- SLIDE_START: §2 | title: 개념 해부 카드 -->

## §2 — 개념 해부 카드


<!-- SLIDE_START: M1 | title: 초기값 획득의 실전 기술(Initial Estimate Acquisition) -->

### 🃏 M1 — 초기값 획득의 실전 기술(Initial Estimate Acquisition)

> **거장의 시각**
> 초기값을 단순 시작 숫자로 읽으면, 알고리즘이 잘못된 basin으로 들어가도 그 오류를 모델 결함과 구분하지 못합니다.
> 그래프·NCA·선행 화합물 지식을 anchor로 고정하면 fit 전 sanity check가 생깁니다.

#### A. 형식적 정의(Formal Definition)

초기값 획득(initial estimate acquisition)은 비선형 회귀(nonlinear regression)를 시작하기 전에 그래프, 선형 회귀(linear regression), NCA, 선행 화합물 지식(prior compound knowledge)으로 시작 파라미터 벡터(starting parameter vector)를 구성하는 절차입니다. 이 단계는 적합(fit) 이전에 끝나야 합니다. 비선형 회귀는 시작 벡터(starting vector)가 주어진 뒤에야 목적함수 표면(objective function surface), 즉 파라미터 조합에 따라 잔차 제곱합 값이 분포하는 지형을 탐색하기 때문입니다. 이는 모델링 회전고리(modeling carousel)의 Explore data 단계에 속합니다. [pp.352–353]

#### B. 원전 고정 유도 기준점(Source-locked derivation anchors)


**B-1. IV bolus 1구획 예시(one-compartment example)**: 두 피험자에게 동일한 10 mg IV bolus를 투여한 뒤 반로그 농도-시간 도표(semi-log concentration–time plot)에서 기울기(slope)를 읽습니다. 이 기울기가 제거속도상수(elimination rate constant) $K$의 초기 기준점(anchor)이 됩니다. [pp.353–354]

$$
\underbrace{\text{slope}}_{\text{반로그 기울기}}=\frac{\overbrace{\ln(800)-\ln(400)}^{\text{log 농도차}}}{\underbrace{23-87}_{\text{시간차}}}=\underbrace{-0.01\ \text{min}^{-1}}_{\text{음의 slope}}=-\underbrace{K}_{\text{제거속도}} \quad [\text{Eq.4:16},\ p.354]
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $K$ | $\text{min}^{-1}$ 또는 $h^{-1}$ | 제거속도상수 | CL/V 변화, slope 판독 |
| $t_{1/2}$ | 시간 | 농도가 절반으로 감소하는 시간 | $K$ 감소 시 증가 |
| $AUC$ | 농도·시간 | 전신 노출 | $C^0$ 증가, $K$ 감소 |
| $Cl$ | 부피/시간 | 정화능 | Dose/AUC anchor |
| $V$ | 부피 | 겉보기 분포 공간 | Dose/$C^0$ anchor |

💡 **비유:** 초기값 사슬은 산길 등산의 첫 등산로 입구와 같습니다. 입구를 잘못 잡으면 지도는 맞아도 전혀 다른 능선으로 올라갑니다.

⚠️ **헷갈림 방지:** 위 수식은 계산값 자체보다 어떤 parameter가 어떤 관측 구간에서 식별되는지 확인하기 위한 anchor입니다.


이로부터 다음 초기값이 이어진다. [p.354]

$$
\underbrace{t_{1/2}}_{\text{반감기}}=\frac{\overbrace{\ln2}^{\text{절반 감소}}}{\underbrace{K}_{\text{제거속도}}}=\frac{0.693}{0.01}\approx\underbrace{65\ \text{min}}_{\text{반감기 anchor}} \quad [\text{Eq.4:17}]
$$

$$
\underbrace{AUC}_{\text{전신노출}}=\frac{\overbrace{C^0}^{\text{초기농도}}}{\underbrace{K}_{\text{제거속도}}}=\underbrace{100{,}000\ \mu g\cdot L^{-1}\cdot\text{min}}_{\text{노출 anchor}} \quad [\text{Eq.4:18}]
$$

$$
\underbrace{Cl}_{\text{정화 부피/시간}}=\underbrace{0.1\ L\cdot\text{min}^{-1}}_{\text{Dose/AUC}},\qquad \underbrace{V}_{\text{겉보기 공간}}=\underbrace{10\ L}_{\text{Dose/}C^0} \quad [\text{Eq.4:19–4:20}]
$$


**B-2. 이중지수 곡선 분리(Bi-exponential curve stripping)**: [p.354]

$$
\underbrace{C}_{\text{총농도}}=\overbrace{\underbrace{A}_{\text{초기 절편}}e^{-\underbrace{\alpha}_{\text{빠른 slope}}t}}^{\text{분포상}}+\overbrace{\underbrace{B}_{\text{말단 절편}}e^{-\underbrace{\beta}_{\text{느린 slope}}t}}^{\text{말단상}} \quad [\text{Eq.4:21},\ p.354]
$$

말단상(terminal phase)에서 $B$와 $\beta$를 먼저 읽고, 후방 외삽된 말단선(back-extrapolated terminal line)을 초기상(initial phase)에서 빼서 $A$와 $\alpha$를 얻습니다. Fig.4.18의 기준값(anchor values)은 $A=1.0\ \mu g\cdot L^{-1}$, $B=0.8\ \mu g\cdot L^{-1}$, $\alpha=0.05\ \text{min}^{-1}$, $\beta=0.003\ \text{min}^{-1}$입니다. [p.355]


**B-3. 동적 평형 반응(Dynamic equilibrium response)**: 반응-농도(response–concentration) 관계에서는 선형-선형 도표(lin-lin plot)와 반로그 도표(semi-log plot)가 서로 다른 정보를 줍니다. 반로그 도표는 $IC_{50}$ 이하 구간을 확장해 $IC_{50}$ 초기 추정값(initial estimate)을 더 쉽게 읽게 합니다. [pp.355–356]

**B-4. 동적 비정상상태 turnover(Dynamic non-steady-state turnover)**: Warfarin이 prothrombin complex synthesis를 차단하면 하강 구간 기울기(downswing slope)가 $-k_{out}$를 줍니다. [pp.356–357]

$$
\underbrace{\text{slope}}_{\text{하강 slope}}=\frac{\overbrace{\ln(124)-\ln(56.77)}^{\text{log 반응차}}}{\underbrace{24-0}_{\text{시간차}}}\approx\underbrace{-0.03\ h^{-1}}_{\text{원문 }-k_{out}} \quad [\text{Eq.4:22},\ p.356]
$$

*↑ 위 식은 원문 부호 불일치 가능성이 있어 하강 기울기를 $-k_{out}$ anchor로 읽는다.*

이 식은 PDF에 표시된 형태를 보존합니다. 다만 산술 부호에는 원전 내부 불일치(source-internal inconsistency)가 있습니다. 수학적으로 재작성하려면 $[\ln(56.77)-\ln(124)]/(24-0)$ 또는 $[\ln(124)-\ln(56.77)]/(0-24)$가 됩니다. 따라서 이는 draft source mismatch가 아니라 원문 내부 부호 문제입니다. Baseline 120 sec와 $k_{out}\approx0.03\ h^{-1}$로 $k_{in}=3.6\ \text{sec}\cdot h^{-1}$를 얻습니다. [p.357]


**B-5. 간접반응 모델 선택 예시(Indirect response model-choice example)**: Eq.4:23–4:33은 baseline, 정상상태(steady state), $E_{max}$, $k_{out}$, $k_{in}$, 지수(exponent) $n$을 그래프에서 순차 도출하는 예입니다. Table 4.3은 Model 1과 Model 4의 최종 추정값(final estimates)과 초기 추정값(initial estimates)을 비교하며, WRSS/AIC가 Model 1에서 7.3/83, Model 4에서 12/102로 제시됩니다. 이 예시는 "초기값 계산"이 곧 "모델 선택"의 전 단계임을 보여 줍니다. [pp.358–360]

**B-6. 반복투여 항불안제 예시(Repeated-dose anxiolytic example)**: Eq.4:34의 경구 PK 입력(oral PK input)은 $K_a=1.1\ h^{-1}$, $K=0.128\ h^{-1}$, $V/F=5.0\ L\cdot kg^{-1}$로 고정해 반응 모델(response model)에 넣습니다. PD turnover는 $dR/dt=k_{in}I(C)-k_{out}R$이고, $k_{out}\approx0.06\ h^{-1}$, $k_{in}=4.8$ units, $IC_{50}\approx0.25\ \mu g\cdot L^{-1}$가 초기 기준점(initial anchor)으로 사용됩니다. [pp.361–363]

$$
\underbrace{\frac{dR}{dt}}_{\text{반응 변화}}=\overbrace{\underbrace{k_{in}}_{\text{생성}}\underbrace{I(C)}_{\text{농도 억제}}}^{\text{입력}}-\overbrace{\underbrace{k_{out}}_{\text{소실}}\underbrace{R}_{\text{현재 반응}}}^{\text{출력}}
$$

**B-7. 다른 방법이 모두 어려울 때 — 경계값 스케일링(boundary scaling)**: 초기값을 직접 얻기 어렵다면 하한/상한 경계(lower/upper boundary)를 이용해 파라미터를 0–1 범위로 스케일링(scaling)합니다. [p.364]

$$
\underbrace{\frac{\overbrace{IE-LB}^{\text{하한 초과분}}}{\underbrace{UB-LB}_{\text{경계 폭}}}}_{\text{0--1 위치}} \quad [\text{Eq.4:44},\ p.364]
$$

원문은 일반적으로 $0.1\cdot IE$부터 $10\cdot IE$까지의 상대 범위(relative range)를 권합니다. 그러나 Table 4.4처럼 원전 특이적 경계(source-specific boundary)가 예외를 만들 수 있으므로, 이 규칙을 기계적으로 적용하면 안 됩니다. [p.364]


💼 **실무 인사이트:** 경계값 스케일링(boundary scaling)을 현대 비선형 추정(nonlinear estimation)에서 사용할 때 최종 추정값(final estimate)이 LB 또는 UB에 붙으면, 모델이 정보를 준 것이 아니라 경계(boundary)가 추정값을 만든 것일 수 있습니다. Table 4.4의 $\beta=0.05$와 UB=0.05는 그대로 모방할 처방(prescription)이 아니라 경계 의존성(boundary dependence)을 의심하게 하는 교육용 예시(teaching example)로 읽어야 합니다. [p.364]


#### C. 구조적 필연성(Structural Necessity)

이중지수 곡선 분리(bi-exponential curve stripping)가 가능한 이유는 $\alpha \gg \beta$일 때 말단상(terminal phase)에서 $Ae^{-\alpha t}$가 사라지고 $Be^{-\beta t}$만 남기 때문입니다. 즉, 반로그 도표(semi-log plot)는 시간 스케일 분리를 눈으로 확인하게 해주는 장치입니다. 두 기울기(slope)가 충분히 분리되지 않으면 곡선 분리는 불안정합니다. [pp.354–355]

#### D. 가정과 경계(Assumptions & Boundaries)

초기값은 "정확한 값"일 필요는 없습니다. 그러나 생리학적으로 타당해야(physiologically plausible) 하고, 목적함수 표면(objective function surface)에서 잘못된 분지(basin), 즉 수렴 가능한 극솟값 영역으로 들어가지 않을 정도로는 근접해야 합니다. 또한 화합물 지식 기반(compound knowledge base)을 일찍 만들고 회귀 목적(regression objective)을 명확히 해야 합니다. 그렇지 않으면 모델링(modeling)은 끝없는 여정(journey)이 됩니다. [p.353]


---

> **M1 체화 핵심**
> ① `fit 전 parameter 출발점 설정` → 그래프 slope·intercept·NCA anchor가 결정
> ② `초기값 vs 최종 추정값 혼동` → regression은 출발 basin을 스스로 교정하지 못함
> ⚡ `대충 넣어도 fit이 고쳐준다` → local minimum·불가능한 parameter 수렴으로 후속 진단 전체 실패


<!-- SLIDE_START: M2 | title: 잔차 기반 모델 진단(Residual-Based Diagnostics) -->

### 🃏 M2 — 잔차 기반 모델 진단(Residual-Based Diagnostics)

> **앞 카드에서 이 카드로:** 초기값이 회귀의 출발 좌표를 정했다면, 잔차는 그 출발 이후 모델이 실제 데이터에서 무엇을 놓쳤는지 드러냅니다.

> **거장의 시각**
> 곡선이 그럴듯해도 잔차의 부호와 순서가 남긴 구조적 흔적을 놓치면 GOF를 오판합니다.
> 잔차를 시간축과 예측값 축에 동시에 펼치면 구조 오류와 가중치 오류의 처방이 분리됩니다.

#### A. 형식적 정의(Formal Definition)

잔차(residual), 즉 관측값과 예측값의 차이는 관측값(observed value)과 계산/예측값(calculated/predicted value) 사이의 수직 거리(vertical distance)입니다.  [p.369]

$$
\underbrace{\epsilon}_{\text{잔차오차}}=\underbrace{N(0,\sigma^2)}_{\text{평균 0·분산 }\sigma^2} \quad [\text{Eq.4:46},\ p.369]
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $\epsilon$ | 관측 단위 | 관측값과 예측값의 차이 | 구조 오류, 분산 오류, 이상치 |
| $W_i$ | 가중치 | 특정 관측치가 WRSS에 기여하는 정도 | 농도 의존 분산, weighting 선택 |
| $WRSS$ | 가중 잔차제곱합 | 모델이 설명하지 못한 불일치 | residual pattern, weighting scheme |
| $\sigma$ | 관측 단위 | 잔차 표준편차 | $WRSS$와 잔차 자유도 |

💡 **비유:** WRSS는 바닥에 남은 발자국을 무게까지 반영해 합산한 것입니다. 발자국이 한쪽으로 휘어 있으면 청소 문제가 아니라 동선 설계 문제입니다.

⚠️ **헷갈림 방지:** 위 수식은 계산값 자체보다 어떤 parameter가 어떤 관측 구간에서 식별되는지 확인하기 위한 anchor입니다.


$$
\underbrace{residual_i}_{\text{i번째 잔차}}=\underbrace{C_{obs,i}}_{\text{관측농도}}-\underbrace{\hat C_{calc,i}}_{\text{예측농도}} \quad [\text{Fig.4.41},\ p.369]
$$

가중잔차제곱합(WRSS, weighted residual sum of squares)은 다음과 같습니다. [p.371]

$$
\underbrace{WRSS}_{\text{가중잔차합}}=\sum \underbrace{W_i}_{\text{가중치}}\underbrace{(C_i-\hat C_i)^2}_{\text{잔차제곱}} \quad [\text{Eq.4:47},\ p.371]
$$

$$
\underbrace{\sigma}_{\text{잔차 SD}}=\sqrt{\frac{\overbrace{WRSS}^{\text{남은 불일치}}}{\underbrace{N_{obs}-N_{par}}_{\text{잔차 자유도}}}} \quad [\text{Eq.4:48},\ p.371]
$$


#### B. 진단 패턴 목록(Diagnostic pattern catalogue)

잔차(residual)는 무작위 산포(random scatter)를 보여야 합니다. 따라서 연속적인 양성/음성 잔차(consecutive positive/negative residuals)가 run, 즉 같은 부호 잔차가 연속으로 이어지는 패턴으로 나타나거나 군집(cluster)이 생기면, 단순 잡음(noise)이 아니라 모델 부적절성(model inadequacy)을 의심해야 합니다. [pp.369–372]

- 잔차 대 시간(residual vs time)에서 banana/U-shape가 보이면 누락된 지수항(missing exponential term) 또는 잘못된 구조적 시간 스케일(wrong structural time scale)을 의심합니다. [pp.372–376]
- 잔차 진폭(residual amplitude)이 농도(concentration)와 함께 커지는 fan shape이면, 등분산 가정(constant variance assumption) 또는 가중치(weighting)가 틀렸을 수 있습니다. [pp.373–374]
- Ordinary Emax와 sigmoid Emax 비교에서는 예측 곡선(predicted curve)만으로 애매한 차이가 잔차 도표(residual plot)에서는 계통적 이탈(systematic deviation)로 드러납니다. [pp.372–373]
- 가중치 지수(weighting power/exponent)는 원문(source text)에서 $0$, $-1$, $-2$, $-n$으로 설명되며, Eq.4:49는 $C_i^{-\lambda_z}$ 또는 $\hat C_i^{-\lambda_z}$ 형태를 씁니다. 즉, "$\lambda_z=-1$"처럼 부호를 단정하지 말고 **가중치 지수(weighting power/exponent)**로 표기해야 합니다. [pp.373–374]

$$
\underbrace{C_i^{-\lambda_z}\ \text{ 또는 }\ \hat C_i^{-\lambda_z}}_{\text{농도 기반 가중치}}
$$


잔차 패턴은 단순한 그림 모양이 아닙니다. 이것은 "모델이 설명하지 못한 시간 스케일 또는 분산 구조"가 밖으로 드러난 형태입니다. Banana pattern은 빠른 상(phase)이 빠졌다는 신호일 수 있고, fan pattern은 구조보다 오차분산 모델(error variance model)의 문제일 수 있습니다. [pp.372–376]


#### C. 순수오차(Pure error) vs 적합결여(lack-of-fit)

반복 측정(replicate measurement)이 있는 in vitro dataset에서는 잔차오차(residual error)를 순수오차(pure error)와 적합결여(lack-of-fit)로 분해할 수 있습니다. Table 4.7의 예에서 residual SS는 92.67, pure error SS는 23.61, lack-of-fit SS는 69.06이고, Eq.4:51의 $F_{LOF}=15.35$는 $F_{crit}=2.76$보다 커서 lack-of-fit를 지지합니다. [pp.377–379]

$$
\underbrace{F_{LOF}}_{\text{LOF F값}}=\frac{\overbrace{(92.67-23.61)/(25-21)}^{\text{LOF 평균제곱}}}{\underbrace{23.61/21}_{\text{pure error 평균제곱}}}=\underbrace{15.35}_{\text{F 비교값}} \quad [\text{Eq.4:51},\ p.379]
$$


💼 **실무 인사이트:** §4.7.3의 LOF F-test는 같은 $x$값에서 반복 측정이 있어 순수오차(pure error)를 계산할 수 있을 때만 가능합니다. 환자별 희소 임상 PK(sparse clinical PK)처럼 같은 시점 반복이 없는 데이터에서는 LOF F-test를 억지로 만들지 말고, 잔차 패턴(residual pattern)과 모델 타당성(model plausibility)을 보아야 합니다.


💼 **실무 인사이트:** 잔차 대 시간(residual vs time)과 잔차 대 예측값/농도(residual vs predicted/concentration)를 함께 보아야 합니다. 한 축에서 무작위 산포(random scatter)처럼 보여도 다른 축에서 fan shape나 구조적 run(structural run)이 나타날 수 있습니다.


#### D. 구조적 필연성(Structural Necessity)

모델 오지정(model misspecification)은 관측 곡선 중첩(observed curve overlay)보다 잔차 도표(residual plot)에서 먼저 보입니다. 중첩(overlay)은 곡선과 데이터의 절대 위치를 보여 줍니다. 반면 잔차 도표는 오차의 부호와 순서를 보존하므로 계통적 이탈(systematic deviation)을 더 선명하게 드러냅니다. [pp.369–376]


---

> **M2 체화 핵심**
> ① `곡선은 맞아 보이는데 패턴이 남을 때` → residual sign/run이 구조 오류를 결정
> ② `banana vs fan shape 혼동` → 구조 모델 수정과 weighting 수정의 처방이 갈림
> ⚡ `잔차 패턴을 noise로 흡수` → 가짜 IIV·가짜 covariate signal 생성


<!-- SLIDE_START: M3 | title: F 검정 적용 조건(F-Test Validity Conditions) -->

### 🃏 M3 — F 검정 적용 조건(F-Test Validity Conditions) [⚡ Apex Concept]

> **앞 카드에서 이 카드로:** 잔차가 무작위인지 확인한 뒤에야, 두 후보 모델의 WRSS 감소가 검정 가능한 개선인지 물을 수 있습니다.

> **거장의 시각**
> 💢 **흔한 오해:** WRSS가 더 낮고 parameter가 하나 늘면 F-test를 쓰면 된다고 생각합니다.
> ✅ **실제는:** F-test는 nested + equal weighting이라는 비교 좌표가 맞을 때만 의미가 있습니다.
> 🎯 **체화할 단 하나의 직관:** 통계량을 계산하기 전에 두 모델이 같은 검정 세계에 있는지 먼저 판정해야 합니다.

#### A. 형식적 정의(Formal Definition)

중첩 모델(nested model), 즉 전체 모델(full model)의 제한 형태란 full model에서 특정 파라미터(parameter)를 고정하면 축소 모델(reduced model)로 접히는(collapse) 관계를 말합니다.  Sigmoid Emax model은 지수(exponent) $n=1$로 고정하면 ordinary Emax model이 되므로 nested 관계입니다. [p.388]

F 통계량(F statistic)은 다음 구조를 갖습니다. [p.387]

$$
\underbrace{F^*}_{\text{중첩 F값}}=\frac{\overbrace{(WRSS_{reduced}-WRSS_{full})/(df_{reduced}-df_{full})}^{\text{parameter당 개선}}}{\underbrace{WRSS_{full}/df_{full}}_{\text{full 잔차 평균제곱}}} \quad [\text{Eq.4:54},\ p.387]
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $WRSS_{reduced}$ | 가중 잔차제곱합 | 축소 모델의 남은 불일치 | parameter 제한, 구조 단순화 |
| $WRSS_{full}$ | 가중 잔차제곱합 | 전체 모델의 남은 불일치 | parameter 추가, 동일 weighting 필요 |
| $df$ | 자유도 | 비교 가능한 정보량 | $N_{obs}-N_{par}$ |
| $N_{par}$ | 개수 | 모델 복잡도 | parameter 추가/고정 |

💡 **비유:** F-test는 같은 트랙에서 달린 두 기록만 비교하는 심판입니다. 한 선수는 트랙, 다른 선수는 산길에서 달렸다면 시간 차이는 경기력이 아니라 경기장 차이입니다.

⚠️ **헷갈림 방지:** 위 수식은 계산값 자체보다 어떤 parameter가 어떤 관측 구간에서 식별되는지 확인하기 위한 anchor입니다.


$$
\underbrace{df}_{\text{잔차 자유도}}=\underbrace{N_{obs}}_{\text{관측수}}-\underbrace{N_{par}}_{\text{parameter 수}} \quad [\text{Eq.4:55},\ p.387]
$$


#### B. 유효한 예와 무효한 예(Valid vs invalid examples)

- **유효(Valid)**: ordinary Emax vs sigmoid Emax. Full sigmoid model에서 $n=1$을 고정하면 ordinary Emax로 줄어듭니다. [p.388]

$$
\underbrace{n}_{\text{sigmoidicity}}=\underbrace{1}_{\text{ordinary Emax 제한}}
$$

- **무효(Invalid)**: ordinary Emax vs linear response. $C\ll EC_{50}$라는 제한 상황에서만 근사적으로 연결될 뿐, 일반적으로 중첩 비교(nested comparison)가 아닙니다. [p.388]

$$
\underbrace{C}_{\text{농도}}\ll\underbrace{EC_{50}}_{\text{반최대 농도}}
$$

- **조건부 유효(Conditionally valid)**: hepatic distributed model과 parallel-tube model은 축소 관계(reduced relation)가 성립하는 경우 F-test를 사용할 수 있습니다. [pp.388–389]
- **이중 위반으로 무효(Invalid with double violation)**: Table 4.8의 Michaelis–Menten weighted fit과 first-order unweighted fit은 비중첩(non-nested)이고 weighting도 달라 F-test도 AIC도 사용할 수 없습니다. [p.389]

#### C. 구조적 필연성(Structural Necessity)


중첩(nested) 조건은 파라미터 개수 차이가 아니라 **한 모델이 다른 모델의 제한된 형태인가**의 문제입니다. 기하학적으로 말하면 축소 모델(reduced model)은 전체 모델 파라미터 공간(full model parameter space) 안의 제한된 부분공간이어야 합니다. 그래야 WRSS 감소량이 "추가 파라미터(parameter)가 설명한 개선"으로 해석됩니다.


#### D. AIC/SC 적용 경계(AIC/SC boundary)

AIC와 SC는 중첩 모델(nested model)을 요구하지 않지만, 동일 가중치(equal weighting)는 요구합니다. [p.389]

$$
\underbrace{AIC}_{\text{Akaike 기준}}=\underbrace{N_{obs}\ln(WRSS)}_{\text{불일치}}+\underbrace{2N_{par}}_{\text{복잡도 벌점}} \quad [\text{Eq.4:56},\ p.389]
$$

$$
\underbrace{SC}_{\text{Schwarz 기준}}=\underbrace{N_{obs}\ln(WRSS)}_{\text{불일치}}+\underbrace{N_{par}\ln(N_{obs})}_{\text{표본수 벌점}} \quad [\text{Eq.4:57},\ p.389]
$$

AIC/SC의 최저값(lowest value)이 자동으로 적절한 모델(adequate model)을 뜻하지는 않습니다. GOF, 즉 모델 적절성(model adequacy)의 종합 진단은 잔차(residuals), 파라미터 정밀도(parameter precision), 정확도(accuracy), 상관행렬(correlation matrix), 조건수(condition number), F-test, AIC/SC를 함께 보는 복합 진단 도구군(battery of tools)입니다.  [pp.387–391]

#### E. WRSS vs $-2\cdot\log likelihood$

원문은 역사적 WRSS 기반 프로그램(historical WRSS-based program)과 현대적 $-2\cdot\log likelihood$ 기반 프로그램(modern $-2\cdot\log likelihood$-based program)을 구분하되, 비교 원리는 동일하게 모델 적절성 기준(model adequacy criteria)과 연결된다고 설명합니다. [p.386] NONMEM의 OFV 비교로 번역할 수는 있지만, $\Delta$OFV threshold나 SCM rule은 이 PDF의 직접 내용이 아닙니다.


---

#### M. Plausible Fallacy — 나비효과 연쇄

**오류:** WRSS가 더 낮고 parameter가 하나 더 많으니 F-test를 쓰면 된다고 판단한다.  
**왜 그럴싸한가:** 같은 데이터에서 더 복잡한 모델이 더 작은 불일치를 만든 것처럼 보이기 때문이다.  
**나비효과:** 비중첩·다른 weighting 비교에 F-test 적용 → WRSS 감소를 추가 parameter 효과로 오독 → [임상] 잘못 선택한 모델로 용량·안전역 시뮬레이션 수행 → [규제] 비교 조건 위반 지적, 재분석 및 모델 선택 근거 재제출 요구.

> **M3 체화 핵심**
> ① `ordinary Emax vs sigmoid Emax` → nested + equal weighting이면 F-test 가능
> ② `MM weighted vs first-order unweighted` → non-nested + different weighting이면 F-test/AIC 모두 불가
> ⚡ `낮은 WRSS = 더 좋은 모델` → 비교 좌표 붕괴 → 잘못된 모델 선택과 재분석 요구


<!-- SLIDE_START: M4 | title: 파라미터 정밀도와 상관(Parameter Precision & Correlation) -->

### 🃏 M4 — 파라미터 정밀도와 상관(Parameter Precision & Correlation)

> **앞 카드에서 이 카드로:** 모델 비교 조건을 통과해도, 좋은 fit이 곧 식별 가능한 파라미터를 뜻하지는 않습니다.

> **거장의 시각**
> 좋은 곡선 적합을 좋은 parameter로 착각하면 ridge와 상관행렬이 숨긴 식별성 문제를 놓칩니다.
> precision과 correlation을 설계의 결과로 읽으면 다음 sampling을 어디서 보강해야 할지 보입니다.

#### A. 정확도(Accuracy), 정밀도(Precision), CV%

정확도(accuracy)는 편향(bias)과 관련되고, 정밀도(precision)는 추정값(estimate)의 불확실성(uncertainty)과 관련됩니다. 즉, 평균적으로 맞는가와 반복하면 얼마나 좁게 모이는가는 다른 질문입니다. 원문은 다트 과녁(dartboard) 비유를 통해 정확/부정확(accurate/inaccurate)과 정밀/부정밀(precise/imprecise)을 구분합니다. [pp.379–380]

$$
\underbrace{CV\%}_{\text{상대 SE}}=\frac{\overbrace{SE(\hat p)}^{\text{추정 SE}}}{\underbrace{\hat p}_{\text{parameter 값}}}\cdot100 \quad [\text{Eq.4:52},\ p.380]
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $CV\%$ | % | 추정값 대비 표준오차 | SE 증가, parameter estimate 감소 |
| $SE(\hat p)$ | parameter 단위 | 추정 불확실성 | sparse design, high correlation |
| $r$ | 무차원 | 원문상 GOF 보조량 | dynamic range, residual SS |
| correlation matrix | 무차원 | parameter trade-off | sampling design, ridge geometry |

💡 **비유:** 좋은 fit과 낮은 CV는 과녁 중심과 탄착군 폭의 관계입니다. 중심 근처에 보여도 탄착군이 길게 늘어지면 같은 실력을 뜻하지 않습니다.

⚠️ **헷갈림 방지:** 위 수식은 계산값 자체보다 어떤 parameter가 어떤 관측 구간에서 식별되는지 확인하기 위한 anchor입니다.


$p=0.01\pm0.005\ h^{-1}$의 CV 50% 예시는 "높은 불확실성(uncertainty)"을 보여주는 예시일 뿐, PDF가 정의한 기각 기준(PDF-defined rejection threshold)이 아닙니다. [p.380]


#### B. 상관계수 r은 GOF가 아닙니다(Correlation coefficient r is not GOF)

PDF는 상관계수(correlation coefficient)가 가장 많이 오용되는 GOF 기준 중 하나라고 설명합니다. Eq.4:53은 원문 표기를 보존합니다. [p.381]

$$
\underbrace{r}_{\text{원문 GOF 지표}}=1-\frac{\overbrace{\sum(C_i-\hat C_i)^2}^{\text{잔차제곱합}}}{\underbrace{\sum(C_i-\bar C)^2}_{\text{총변동}}} \quad [\text{Eq.4:53 source form},\ p.381]
$$

*↑ 원문 표기 $r$은 잔차제곱합/총변동 기반 GOF 보조량으로 읽는다.*

Fig.4.53에서 OLS fit은 $r=0.96$이지만 마지막 세 관측치를 계통적으로 과소예측(systematically underestimate)하고, IRLS fit은 $r=0.94$이지만 전체적으로 더 나은 적합(fit)을 보입니다. 따라서 높은 $r$은 좋은 fit의 충분조건이 아닙니다. [p.382]


> 💼 **실무 인사이트:** 동적 범위(dynamic range)가 넓은 농도-시간 자료(concentration–time data)에서는 $r$이 모델의 잔차 구조보다 전체 값의 범위에 강하게 끌릴 수 있습니다. 그래서 $r$은 잔차 도표(residual plot)와 함께 읽어야지, 단독 GOF 판정 기준으로 쓰면 안 됩니다.


#### C. 파라미터 상관과 능선 기하(Parameter correlation and ridge geometry)

파라미터 상관행렬(parameter correlation matrix)은 파라미터들이 독립적으로 추정(estimate)되는지, 또는 서로 trade-off하는지를 보여 줍니다. 원문은 높은 상관(high correlation)이 더 적은 파라미터(fewer parameters) 또는 더 많은 데이터(more data)의 필요성을 시사한다고 설명합니다. [pp.382–383]


Fig.4.55–4.57의 핵심은 **능선형 최솟값(ridge minimum)**, 즉 길게 늘어진 최솟값 영역입니다.  두 파라미터(parameter)가 능선(ridge) 위에서 같이 움직이면 OFV/WRSS가 거의 변하지 않습니다. 이 때문에 단변량 추정값(univariate estimate)은 그럴듯해도 결합 불확실성(joint uncertainty)은 큽니다. Design A/B 비교는 같은 모델도 샘플링 설계(sampling design)에 따라 $Cl/V$ 또는 $IC_{50}/I_{max}$ 상관이 크게 달라짐을 보여 줍니다. [pp.383–385]

#### D. 한 파라미터 고정(Fixing one parameter)

Fig.4.55는 한 파라미터(parameter)를 고정하면 다른 파라미터의 신뢰구간(confidence interval)이 작아질 수 있음을 보여 줍니다. [pp.383–384] 그러나 고정(fix) 전략은 정당화 부담을 통계에서 생물학/문헌/선행 연구(biology/literature/prior study)로 옮깁니다. 따라서 고정값(fix value)의 출처와 적용 가능성을 설명하지 못하면, 정밀도(precision)가 좋아진 것이 아니라 불확실성(uncertainty)을 숨긴 것입니다.

#### E. 한계(Limitations)

높은 상관(high correlation)에 대한 보편적 기준(universal cutoff)은 PDF에 없습니다. $|r|>0.95$ 같은 고정 기준(hard threshold) 대신, 상관행렬(correlation matrix), 신뢰 타원(confidence ellipse), 잔차 패턴(residual pattern), 설계 적절성(design adequacy)을 함께 읽어야 합니다. 조건수(condition number)나 covariance-step warning은 현대 구현에서 유용한 신호지만, 이 PDF의 직접 교육 포인트(teaching point)는 "상관(correlation)은 설계(design)의 결과"라는 점입니다.


---

> **M4 체화 핵심**
> ① `fit은 좋아 보이나 SE/CV가 클 때` → parameter identifiability가 지배
> ② `r 높음 vs true GOF` → residual pattern·precision·correlation이 따로 지배
> ⚡ `r이 높으면 충분` → terminal bias·ridge·design weakness를 놓침


<!-- SLIDE_START: M5 | title: 편미분 기반 최적 샘플링(Partial-Derivative Optimal Sampling) -->

### 🃏 M5 — 편미분 기반 최적 샘플링(Partial-Derivative Optimal Sampling)

> **앞 카드에서 이 카드로:** 파라미터 상관이 설계의 약점을 드러냈다면, 다음 질문은 어느 시간점이 그 파라미터를 가장 잘 보이게 하는가입니다.

> **거장의 시각**
> 편미분을 계산 문제로만 보면 최적 sampling의 실무 의미를 잃습니다.
> derivative peak를 정보가 가장 크게 생기는 시간·농도 위치로 읽으면 설계가 수식에서 바로 나옵니다.

#### A. 이중지수 편미분 설계(Bi-exponential derivative design)

원문은 이중지수 모델(bi-exponential model)을 예로 듭니다. [p.399]

$$
\underbrace{C}_{\text{총농도}}=\overbrace{\underbrace{A}_{\text{빠른 절편}}e^{-\underbrace{\alpha}_{\text{빠른 slope}}t}}^{\text{초기 정보}}+\overbrace{\underbrace{B}_{\text{느린 절편}}e^{-\underbrace{\beta}_{\text{느린 slope}}t}}^{\text{말단 정보}} \quad [\text{Eq.5:7},\ p.399]
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $A, B$ | 농도 | 초기/말단 절편 정보 | 초기·말단 sample 위치 |
| $\alpha, \beta$ | $\text{time}^{-1}$ | 빠른/느린 slope 정보 | derivative peak 위치 |
| $t=1/\alpha$ | 시간 | 빠른 slope 정보가 가장 큰 시간 | $\alpha$ 증가 시 앞당겨짐 |
| $t=1/\beta$ | 시간 | 말단 slope 정보가 가장 큰 시간 | $\beta$ 감소 시 늦어짐 |

💡 **비유:** 편미분 peak는 어두운 방에서 손전등이 가장 밝게 비추는 지점입니다. 그곳에 sample을 놓아야 해당 parameter의 윤곽이 선명해집니다.

⚠️ **헷갈림 방지:** 위 수식은 계산값 자체보다 어떤 parameter가 어떤 관측 구간에서 식별되는지 확인하기 위한 anchor입니다.


$A$와 $B$에 대한 편미분(derivatives)은 절편(intercept) 영역에서, $\alpha$와 $\beta$에 대한 편미분은 각각 $t=1/\alpha$, $t=1/\beta$에서 극값을 갖습니다. [pp.399–400]

$$
\underbrace{t}_{\text{민감도 peak}}=\frac{1}{\underbrace{\alpha}_{\text{빠른 slope}}},\qquad \underbrace{t}_{\text{민감도 peak}}=\frac{1}{\underbrace{\beta}_{\text{느린 slope}}} \quad [\text{Eq.5:11},\ p.400]
$$

예시 파라미터(parameter)가 $\alpha=0.69\ h^{-1}$, $\beta=0.069\ h^{-1}$이면 최적 시간(optimal time)은 약 1.4 h와 14 h입니다. Fig.5.4의 도표 예시(plotted example)에서는 $\alpha$와 $\beta$ 정보가 각각 약 20 min, 300 min 부근에 모입니다. [p.400]


#### B. Sigmoid Imax / Emax 설계(design)

Sigmoid Imax model의 편미분(derivatives)은 $IC_{50}$ 정보가 half-maximal effect 부근에, sigmoidicity factor $n$ 정보가 20%와 80% effect level 부근에 집중됨을 보여 줍니다. Fig.5.6은 $E_0$, $n$, $EC_{50}$, $n$, $E_{max}$에 대한 다섯 설계 지점(design points)을 제시합니다. [pp.400–402]

#### C. Turnover model 설계(design)

Turnover response model에서는 $k_{out}$ 민감도(sensitivity)가 25 h와 약 100 h post-dose에서 크고, 초기 시간(early time)에서는 $k_{out}$가 $IC_{50}$ 또는 $n$보다 민감합니다. 따라서 초기 샘플링(early sampling)은 $k_{out}$ 초기 추정값(initial estimate)을 직접 강화합니다. [pp.402–404]

#### D. 구조적 필연성(Structural Necessity)


편미분이 큰 위치는 예측(prediction)이 해당 파라미터(parameter) 변화에 크게 흔들리는 위치입니다. 이를 가능도 표면(likelihood surface), 즉 파라미터 공간에서 OFV 값이 분포하는 지형의 언어로 바꾸면, 그 위치의 관측치는 해당 파라미터 방향의 표면 곡률(surface curvature)을 키워 최솟값(minimum)을 더 좁고 깊게 만듭니다.


💼 **실무 인사이트:** 파라미터(parameter) 단위가 다르면 원자료(raw) $\partial C/\partial\theta$ 크기 비교가 왜곡될 수 있습니다. 실무에서는 $\theta_i(\partial C/\partial\theta_i)/C$ 같은 정규화 민감도(normalized sensitivity)를 함께 보아 파라미터 간 비교를 안정화합니다.

$$
\underbrace{\frac{\theta_i(\partial C/\partial\theta_i)}{C}}_{\text{정규화 민감도}}
$$


#### E. 경계 조건(Boundary Conditions)

참 파라미터 값(true parameter values)을 사전에 알 수 없으므로, 편미분 극값(derivative maxima)에만 샘플(sample)을 몰아넣으면 안 됩니다. 전체 농도 범위(concentration range)에도 추가 샘플(samples)을 두어야 합니다. 원문은 pooled data를 무비판적으로 설계 결정(design decision)에 쓰는 위험도 경고합니다. [p.402]


---

> **M5 체화 핵심**
> ① `어느 시간에 sample을 찍을까` → partial derivative peak가 결정
> ② `intercept 정보 vs slope 정보` → 초기/말단 시간대가 서로 다른 parameter를 지배
> ⚡ `균등 sampling이면 충분` → 민감도 낮은 구간 반복 → parameter precision 개선 실패


<!-- SLIDE_START: M6 | title: 민감도 분석(Sensitivity Analysis) -->

### 🃏 M6 — 민감도 분석(Sensitivity Analysis)

> **앞 카드에서 이 카드로:** 편미분이 정보가 생기는 위치를 말해 주었다면, 민감도 분석은 그 불확실성이 임상 결론을 얼마나 흔드는지 보여 줍니다.

> **거장의 시각**
> 민감도 분석을 사후 그림으로만 보면 예측 결론이 무너지는 지점을 놓칩니다.
> parameter perturbation을 다음 실험 전 stress test로 읽으면 안전역·AUC·sampling package를 조정할 근거가 생깁니다.

#### A. 형식적 정의(Formal Definition)

민감도 분석(sensitivity analysis)은 특정 파라미터(parameter)를 일정 비율로 변화시켜 농도-시간(concentration–time) 또는 반응-시간(response–time) 예측(prediction)이 어떻게 달라지는지 보는 절차입니다. 즉, 파라미터 불확실성(parameter uncertainty)이 실제 예측 불확실성(prediction uncertainty)으로 얼마나 번역되는지를 봅니다. 원문의 예시는 파라미터를 +100% 또는 -50%로 변화시켜 모델 출력(model output) 변화를 비교합니다. [pp.404–405]

#### B. PK 민감도 예시(PK sensitivity example)

Michaelis–Menten pharmacokinetic model에서 $V_{max}$, $K_M$, $V_c$, $V_t$를 변화시키면 농도-시간 프로파일(concentration–time profile)의 어느 구간이 어떤 파라미터(parameter)에 민감한지 드러납니다. Fig.5.9는 이것을 향후 샘플링 위치(future sampling location) 결정에 연결합니다. [p.405]

#### C. PD 민감도 예시(PD sensitivity example)

Warfarin-PCA model에서는 $IC_{50}$, $k_{in}$, $k_{out}$, $t_{lag}$의 변화가 반응-시간 프로파일(response-time profile)에 미치는 영향을 비교합니다. Fig.5.10의 목적은 "어떤 파라미터(parameter)를 더 잘 추정(estimate)하려면 어느 구간을 보강해야 하는가"를 읽는 것입니다. [p.405]


#### D. 독성동태 설계 맥락(Toxicokinetic design context)

독성동태 설계(toxicokinetic design)에서 만성시험(chronic studies)은 보통 노출(exposure) 확인을 위해 $C_{max}$ 샘플링(sampling)만으로 충분한 경우가 있으나, 예외가 있으며 연구자 판단(investigator judgment)이 필요합니다. Table 5.6은 PK/DRF/chronic study type별로 profile 또는 $C_{max}$ 중심 sampling package를 구분합니다. [p.413]

비선형 제거(nonlinear elimination)에서는 농도(concentration)가 일차 선형 동태(first-order linear kinetics) 또는 무시 가능한 수준(negligible level)에 도달할 때까지 샘플링(sampling)하지 않으면 진정한 무한대 외삽 AUC(true extrapolated AUC to infinity)를 얻을 수 없습니다. [p.414]

용량의존 동태(capacity-dependent kinetics)와 시간의존 동태(time-dependent kinetics)가 동시에 존재하면 Day 1 AUC와 정상상태 AUC(steady-state AUC) 비교가 상쇄될 수 있습니다. 이 경우 해석(interpretation)은 흐려집니다. Fig.5.20의 핵심은 노출(exposure)이 변하지 않는 것처럼 보여도 capacity와 induction이 동시에 작동할 수 있다는 점입니다. [p.414]


💼 **실무 인사이트:** 민감도 분석(sensitivity analysis)은 파라미터(parameter)를 "잘 추정했는지"보다 먼저 "잘못 추정하면 어떤 결론이 흔들리는지"를 묻습니다. 흔들리는 결론이 용량(dose), 안전역(safety margin), 샘플링 일정(sampling schedule)이면 다음 실험 설계를 바꿔야 합니다.


---

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $V_{max}$ | 양/시간 | 포화 제거 최대속도 | capacity 변화 |
| $K_M$ | 농도 | 반최대 제거 농도 | affinity/포화 위치 변화 |
| $IC_{50}$ | 농도 | 반최대 억제 농도 | potency 변화 |
| $k_{in}, k_{out}$ | 반응/시간, $\text{time}^{-1}$ | turnover 입력·출력 | synthesis/turnover 변화 |

💡 **비유:** 민감도 분석은 다리의 특정 볼트를 일부러 흔들어 보는 검사입니다. 흔들림이 용량·안전역 결론까지 전달되면 다음 실험 설계를 보강해야 합니다.

> **M6 체화 핵심**
> ① `parameter 불확실성이 결론을 흔드는가` → sensitivity analysis가 결정
> ② `PK profile vs Cmax 중심 TK sampling` → study type과 nonlinear elimination 여부가 지배
> ⚡ `노출이 같아 보이면 기전도 같다` → capacity/time-dependent kinetics 상쇄를 놓쳐 AUC 해석 실패


<!-- SLIDE_START: §5 | title: 혼동쌍 해부 -->

## §5 — 혼동쌍 해부(Confusion Pair Dissection)

### ▣ 혼동쌍 #1 — 중첩 + 동일 가중치(Nested + equal weighting) vs 비중첩 또는 다른 가중치(non-nested 또는 different weighting)

| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | 중첩 + 동일 가중치: F-test와 AIC/SC의 비교 좌표 | 비중첩 또는 다른 가중치: 서로 다른 WRSS 좌표 |
| 수식 내 위치 (분자/분모/지수) | $F^*$의 WRSS 차이와 $df$ 차이가 의미를 갖는 전제 | $WRSS_{reduced}-WRSS_{full}$ 해석 불가; AIC/SC도 동일 weighting 없으면 불가 |
| 변화 원인 (생물학적/병적) | full model에서 parameter 제한으로 reduced model이 접히고 weighting이 동일함 | model structure가 다르거나 weighting이 달라 비교 기준이 바뀜 |
| 혼동 시 임상 결과 | 적절한 추가 parameter 검정 가능 | 잘못된 모델 선택 → 후속 dose simulation·safety margin·sampling 권고 오염 [pp.387–389] |

💼 **실무 인사이트:** 가중치(weighting) 선택은 관행이 아니라 잔차 패턴(residual pattern)으로 정당화합니다. Fan shape이면 상대오차 가중치를 의심하고, 잔차 폭이 균질하면 고정 절대오차가 더 자연스럽습니다. [pp.373–374]

**기억 고리**: F-test는 "중첩(nested) + 같은 가중치(same weighting)"라는 잠금장치가 맞아야 열립니다.

### ▣ 혼동쌍 #2 — 상관계수 r(Correlation coefficient r) vs 진정한 GOF

| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | $r$: 무차원 보조 숫자 | 진정한 GOF: 곡선·잔차·정밀도·상관의 복합 판정 |
| 수식 내 위치 (분자/분모/지수) | 잔차제곱합/총변동 비율 기반 원문 지표 | residual vs time, residual vs prediction/concentration, precision matrix |
| 변화 원인 (생물학적/병적) | 농도 범위가 넓으면 높아질 수 있음 | terminal bias, systematic run, fan shape, poor precision이 드러남 |
| 혼동 시 임상 결과 | $r=0.96$ 같은 숫자에 안심 | terminal observations 과소예측 또는 IRLS 우월 패턴을 놓침 [pp.381–382] |

💼 **실무 인사이트:** PK data처럼 $y$-range가 넓으면 $r$은 동적 범위(dynamic range)의 영향을 크게 받을 수 있습니다. 따라서 $r$은 GOF 판정의 주연이 아니라 보조 숫자입니다.

**기억 고리 — [CRUCIBLE_DERIVED]**: $r$은 큰 방향을 보고, 잔차는 모델의 거짓말을 봅니다.

### ▣ 혼동쌍 #3 — 구조 모델 오류(Structural model error) vs 분산/가중치 모델 오류(variance/weighting model error)

| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | 구조 모델 오류: 시간 스케일/compartment/shape 문제 | 분산·가중치 오류: 관측오차 크기와 weighting 문제 |
| 수식 내 위치 (분자/분모/지수) | 빠진 exponential term, wrong Emax shape, lag-time omission | $W_i$, $C_i^{-\lambda_z}$ 또는 $\hat C_i^{-\lambda_z}$ |
| 변화 원인 (생물학적/병적) | Banana, U-shape, systematic runs | Fan shape, concentration-dependent spread |
| 혼동 시 임상 결과 | weighting만 바꾸어 구조 오류를 덮음 | compartment를 추가해 variance 문제를 복잡화 [pp.372–376] |

💼 **실무 인사이트:** Fan shape에 compartment를 추가하거나 banana pattern에 weighting만 바꾸면 문제의 원인은 그대로 남습니다.

**기억 고리**: 모양이 휘면 구조를 의심하고, 폭이 벌어지면 분산을 의심합니다.

### ▣ 혼동쌍 #4 — 이상치 A(Outlier A) vs 이상치 B(Outlier B)

| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | 이상치 A: 참 곡선에서의 수직 이탈 | 이상치 B: 시간축 이탈과 높은 leverage |
| 수식 내 위치 (분자/분모/지수) | residual 크기를 키워 precision 감소 | curve 방향 자체를 끌어 bias 유발 |
| 변화 원인 (생물학적/병적) | noisy point, vertical deviation | sampling time/reporting error 가능성, high leverage |
| 혼동 시 임상 결과 | 잡음점으로 처리 가능 | 잘못된 curve가 정밀해 보이는 편향 생성 [p.390] |

원문은 table만 보면 A와 B의 이탈점(deviating points)을 거의 알아보기 어렵다고 강조합니다. 따라서 이상치(outlier) 판단에서는 그래픽 제시(graphical presentation)가 매우 중요합니다. [p.390]

💼 **실무 인사이트:** Cook's distance나 hat matrix는 현대 회귀 진단에서 유용하지만, 이 PDF의 핵심은 먼저 plot에서 영향력(leverage)과 수직 이탈(vertical deviation)을 구분하는 것입니다.

**기억 고리**: A는 위아래로 튄 점이고, B는 시간을 잘못 말하는 점입니다. B가 더 위험한 이유는 곡선의 방향을 바꾸기 때문입니다.


<!-- SLIDE_START: §7 | title: 자기 점검: 능동 회상 모듈 -->

## §7 — 자기 점검: 능동 회상 모듈(Self-Test: Active Recall Module)

### Q1. [회상 ★★]


**문제**: 초기값이 부실할 때 Gabrielsson이 명시한 세 가지 위험은 무엇인가? [p.353]

**정답**: 잘못된 최종 추정값(wrong final values), 원치 않는 국소 최솟값(unwanted local minima), 생리학적으로 불가능한 파라미터 값(physiologically impossible parameter values)입니다. 초기값은 비선형 회귀(nonlinear regression)에서 단순한 편의값이 아니라, 알고리즘(algorithm)이 어떤 분지(basin)로 들어갈지 결정하는 EDA 산출물입니다.

---

### Q2. [계산 ★★]


**문제**: 10 mg IV bolus 예시에서 반로그 기울기(semi-log slope)가 $-0.01\ \text{min}^{-1}$일 때 $t_{1/2}$, AUC, Cl, V의 source anchor 값을 쓰세요. [p.354]

**정답**: $t_{1/2}\approx65\ \text{min}$, $AUC=100{,}000\ \mu g\cdot L^{-1}\cdot\text{min}$, $Cl=0.1\ L\cdot\text{min}^{-1}$, $V=10\ L$입니다. [Eq.4:17–4:20]

---

### Q3. [회상 ★]


**문제**: 이중지수 곡선 분리(bi-exponential curve stripping)에서 말단상(terminal phase)을 먼저 읽는 이유는 무엇인가요? [pp.354–355]

**정답**: 말단상(terminal phase)에서는 빠른 지수항(exponential term) $Ae^{-\alpha t}$가 거의 사라지고 $Be^{-\beta t}$가 지배합니다. 따라서 $B$와 $\beta$를 먼저 얻은 뒤 이를 후방 외삽(back-extrapolate)하여 초기상(initial phase)에서 빼면 $A$와 $\alpha$를 얻을 수 있습니다.

---

### Q4. [진단 ★★]


**문제**: 잔차 도표(residual plot)에서 banana pattern과 fan shape가 각각 시사하는 문제는 무엇인가요? [pp.372–376]

**정답**: Banana/U-shape는 구조적 시간 스케일(structural time-scale) 문제, 예를 들어 빠진 지수항(exponential term)이나 잘못된 모델 형태(wrong model shape)를 의심하게 합니다. Fan shape는 농도의존 분산(concentration-dependent variance) 또는 가중치 불일치(weighting mismatch)를 의심하게 합니다.

---


### Q5. [핵심 개념(Apex) 적용 ★★]


**문제**: Ordinary Emax model과 sigmoid Emax model 비교에는 F-test를 쓸 수 있나요? Linear response model과 ordinary Emax model 비교에는 어떤가요? [p.388]

**정답**: Ordinary Emax vs sigmoid Emax는 sigmoid model에서 $n=1$로 고정하면 ordinary Emax가 되므로 중첩(nested)이고 F-test가 가능합니다. Linear response vs ordinary Emax는 일반적으로 nested가 아니므로 F-test를 쓰면 안 됩니다.

---

### Q6. [판정 ★★]


**문제**: Michaelis–Menten weighted fit과 first-order unweighted fit에서 AIC가 더 낮은 모델을 선택해도 되는가? [p.389]

**정답**: 안 됩니다. Table 4.8은 두 모델이 비중첩(non-nested)이고 weighting도 다르므로 F-test도 AIC도 쓸 수 없음을 보여 줍니다. AIC/SC는 중첩(nested)을 요구하지 않지만 동일 가중치(equal weighting)는 요구합니다.

---

### Q7. [계산/개념 ★★]


**문제**: Table 4.7의 residual SS 92.67, pure error SS 23.61, df 25와 21로 계산한 $F_{LOF}$는 무엇이며 어떤 결론인가? [pp.378–379]

**정답**: $F_{LOF}=[(92.67-23.61)/(25-21)]/(23.61/21)=15.35$이고, $F_{crit}=2.76$보다 커서 적합결여(lack-of-fit)가 있습니다. 단, 이 검정은 반복 측정(replicate measurement)이 있어 순수오차(pure error)를 분리할 수 있을 때만 가능합니다.

---

### Q8. [설계 ★★]


**문제**: Fig.4.55–4.57에서 design A와 design B가 가르치는 핵심은 무엇인가요? [pp.383–385]

**정답**: 파라미터 상관(parameter correlation)과 신뢰 타원(confidence ellipse)은 모델 방정식(model equation)만의 문제가 아니라 샘플링 설계(sampling design)의 결과입니다. 좋은 설계(design)는 두 파라미터(parameter)가 서로 trade-off하지 않도록 정보 영역을 분리해 신뢰구간(confidence interval)과 상관(correlation)을 줄입니다.

---

### Q9. [보스 딜레마(Boss Dilemma) ★★]


**문제**: 두 경쟁 모델(competing model)이 있습니다. 하나는 더 낮은 WRSS(lower WRSS)를 보이지만 다른 가중치(weighting)를 사용했고, 다른 하나는 기전적으로 타당(mechanistically plausible)하지만 AIC 차이가 작습니다. 어떤 결정을 내려야 하나요?

**정답**: 먼저 같은 가중치(weighting)로 재적합해 비교 가능성을 확보합니다. 그래도 F-test/AIC가 단독 결론을 주지 못하면 잔차 패턴(residual pattern), 기전적 타당성(mechanism plausibility), 외부 데이터(external data), 시각적 예측(visual prediction)을 함께 삼각검증(triangulate)합니다. PDF는 AIC 차이 기준값(AIC difference threshold)을 정의하지 않습니다. 따라서 낮은 AIC 하나만으로 기전적 타당성(mechanistic plausibility)을 이길 수 없습니다. [p.389, p.391]


> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** 최종 GOF는 잔차·precision·correlation·comparison·design feedback이 모두 통과할 때만 닫힌다.

---

<!-- SLIDE_START: §8 | title: 메타 프레임과 큰 그림 -->

## §8 — 메타 프레임과 큰 그림(Meta-Frame & Big Picture)

### A. 위치 잡기(Positioning)


이 세션은 PK/PD 모델링에서 "모델을 세우는 기술"보다 "모델을 버리거나 다시 설계하는 기술"에 가깝습니다. 초기 추정값(initial estimates)은 적합(fit)의 출발점을 정합니다. 잔차(residuals)는 모델 결함을 드러냅니다. F-test/AIC/SC는 비교 조건을 제한합니다. 정밀도/상관(precision/correlation)은 설계의 약점을 노출합니다. 그리고 편미분(partial derivatives)과 민감도 분석(sensitivity analysis)은 다음 실험의 샘플링(sampling)을 바꿉니다. [p.353, pp.369–391, pp.399–405]

현대 PopPK workflow에서 이 한 사이클의 실무 단위는 단일 run이 아니라 **model/control file 한 버전 + GOF diagnostic plot set + 다음 cohort sampling recommendation**입니다. 세 가지가 함께 닫혀야 modeling carousel이 완주됩니다.

### B. 의존성 사슬(Dependency chain)

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| 초기값이 틀림 | starting parameter vector | → | 잘못된 수렴 또는 local minimum | EDA/NCA/graph anchor 재설정 [p.353] |
| 잔차가 계통적 | residual pattern | → | GOF 성립 불가 | 구조 또는 weighting 재검토 [pp.369–376] |
| 비중첩/다른 weighting 비교 | WRSS/AIC/SC 좌표 | → | F-test/AIC 무력화 | 기전·잔차·외부근거 삼각검증 [pp.387–389] |
| 파라미터 상관 높음 | precision/correlation | → | 식별성 취약 | 다음 sampling design 보강 [pp.382–385] |
| 정보 위치 불명확 | partial derivative/sensitivity | → | 예측 결론 흔들림 | derivative peak와 sensitivity 기반 설계 [pp.399–405] |

### C. 전문성 해자(Professional moat)

경험 많은 모델러는 "어느 모델의 AIC가 낮은가"만 보지 않습니다. 두 모델이 비슷한 WRSS/AIC를 보이는데 잔차 패턴(residual pattern)과 기전(mechanism)이 모두 애매하면, 어느 한쪽을 고르기 전에 **둘 다 잘못된 기전(wrong mechanism)일 가능성**을 의심합니다. 이 역방향 추론이 모델 선택(model selection)을 파라미터 수 게임(parameter-count game)이 아니라 기전 가설 수정(mechanistic hypothesis revision)으로 바꿉니다.


### D. Table 4.9에 고정된 GOF 체크리스트(GOF checklist locked from Table 4.9)


모델 적합성은 최소한 다음 다섯 질문으로 닫아야 한다. [p.391]

| 체크리스트 질문(Checklist question) | 고정 해석(Locked interpretation) |
|---|---|
| 모델에 생물학적 관련성(biological relevance)이 있는가? | 기전적 타당성(mechanistic plausibility)이 없는 낮은 AIC는 취약하다. |
| 적합된 곡선(fitted curve)이 데이터의 경향(trends in the data)을 재현하는가? | 곡선 중첩(curve overlay)은 첫 관문이다. |
| 파라미터가 충분한 정밀도(adequate precision)로 추정되었는가? | CV%, SE, 신뢰구간(confidence intervals)을 본다. |
| 잔차(residuals)에 계통적 이탈(systematic deviation)이 없는가? | Run, banana, fan, lag-time pattern을 본다. |
| 잔차 도표(residual plots)가 무작위 산포(random scatter)를 보이는가? | 잔차가 무작위가 아니면 모델 또는 가중치(weighting)를 다시 본다. |

### E. 최종 고정 요약(Final locked summary)


이 세션의 압축 명제는 다음과 같다.

> **초기값은 알고리즘의 출발점을 정하고, 잔차(residual)는 모델의 거짓말을 드러내며, F-test/AIC는 비교 가능한 모델에서만 의미가 있고, 정밀도/상관(precision/correlation)은 설계의 품질을 말하며, 편미분(partial derivative)과 민감도 분석(sensitivity analysis)은 다음 실험을 어디서 다시 해야 하는지 알려줍니다.**

이 문장을 체화하면 p.352의 모델링 회전고리(modeling carousel)는 단순한 그림이 아니라 실제 워크플로우(workflow)가 됩니다: Explore data에서 초기 추정값(initial estimates)을 만들고, Fit model 후 Analyze output에서 잔차/정밀도/비교(residual/precision/comparison)를 검토하며, 그 결과로 다음 설계(Design)를 수정합니다. [p.352, p.392, pp.399–405]


#

### F. 후속 세션 연결 지식 그래프

| 후속 세션 | 이 세션에서 열리는 개념 | 이 세션 없으면 실패하는 것 |
|---|---|---|
| NONMEM estimation method module | FO/FOCE/FOCEI/Laplacian/SAEM을 판단 조건으로 읽기 | OFV·precision·shrinkage 차이를 알고리즘 옵션으로만 오독 |
| Model qualification module | GOF → VPC/pcVPC/NPDE → bootstrap/SIR 흐름 | 곡선 적합을 predictive performance로 과잉해석 |
| Adaptive sampling/design module | derivative peak와 sensitivity를 다음 설계로 번역 | 정보 없는 시간점 반복 sampling |


---

## 출력 후 자가검증 체크리스트

| 항목 | 기준 | 결과 |
|---|---|---|
| SLIDE_START 개수 | §섹션수 + 카드수 합산 | 11 개 |
| 카드당 callout 합계 ≤ 6 | 전체 카드 | ✓ |
| [E] 박스 존재 | 모든 §2 카드 | ✓ |
| [D] 거장의 시각 존재 | 모든 §2 카드 | ✓ |
| [L] 파라미터 표 존재 | Apex 카드 + 정의 수식 카드 | ✓ |
| §5 혼동 쌍 표 행 순서 고정 (4행) | §5 전체 | ✓ |
| 기호 일관성 | 첫 등장 기준 통일 | ✓ |
| PART B 흔적 없음 | 전체 | ✓ |
| 수치 anchor 보존 | Compound A 등 원본 수치 | ✓ |
| [M] 나비효과 이중 종착점 | Apex 카드 전체 | ✓ |

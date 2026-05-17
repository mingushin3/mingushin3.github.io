## PART A — 학습자용 완성 핸드아웃

> **v3.6 note:** This version applies a source-preserving Equation Annotation + Slide Message Patch to PART A only. Existing learner-facing content, scientific claims, equations, numerical anchors, examples, page tags, source labels, figure marker boundaries/field keys, section/card structure, code blocks, and PART B guardrails are preserved. The patch only inserts annotated-equation blocks (underbrace/overbrace labeling) and slide-start markers with one-line 핵심 메시지 for future PPT-like HTML compilation. No existing content was rewritten, reordered, deleted, or scientifically expanded beyond equation-meaning clarification.


<!-- SLIDE_START: S01 | title: 세션 15 전체 프레임 | source_anchor: # 세션 15 -->
> **핵심 메시지:** 모델 구축은 fit 버튼이 아니라 초기값·잔차·비교조건·설계 피드백이 닫히는 판단 루프입니다.

# 세션 15 — 모델 구축의 기술: 초기값 · GOF · 모델 판별 · 실험 설계

> **출처 및 범위 노트**  
> 이 핸드아웃은 Gabrielsson & Weiner 5e, *Pharmacokinetic and Pharmacodynamic Data Analysis: Concepts and Applications*의 Ch.4 §4.4, §4.7–4.10 및 Ch.5 §5.2.3–5.2.4, §5.3.3을 범위로 합니다. 검증된 페이지 범위는 p.352–364 / p.368–392 / p.399–405 / p.412–414입니다. 업로드된 PDF에는 pp.365–367(§4.5 Minimization, §4.6 Weighting) 및 pp.406–411이 포함되어 있지 않으므로, 이 페이지들에 의존하는 내용은 `[확인 필요]`로 유지합니다.

<!-- SLIDE_START: S02 | title: 학습자 항법 안내 | source_anchor: ## 학습자 항법 안내 -->
> **핵심 메시지:** 이 자료는 여섯 기술을 따로 외우는 handout이 아니라 모델링 회전고리를 순서대로 통과하는 학습 지도입니다.

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

이 자료는 저작권이 있는 교과서 그림을 직접 재현하지 않습니다. `FIGURE_POINTER` 블록은 학습자를 원본 교과서 그림·표로 안내하는 텍스트 전용 콜아웃(callout)입니다. `FIGURE_SCHEMATIC` 블록은 학습용 새 도식의 구성 요소, 핵심 메시지, 캡션, 대체 텍스트를 지정하는 설명 블록이며, 교과서 그림을 직접 복제하지 않습니다.

---

<!-- SLIDE_START: S03 | title: 세션 개요와 Big Idea | source_anchor: §1 -->
> **핵심 메시지:** 좋은 통계량보다 먼저 필요한 것은 그 통계량을 적용해도 되는 조건을 판별하는 능력입니다.

## §1 — 세션 개요와 로드맵

### 이 세션의 정확한 위치

본 세션은 p.352 Fig.4.16의 **모델링 회전고리(modeling carousel)**, 즉 모델링 한 사이클의 반복 구조 가운데 Step 4 Explore data, Step 5 Fit model(s), Step 6 Analyze output을 다룹니다. <!-- ANNOTATION --> 그 결과를 다음 실험의 설계(Design)로 되돌리므로, 초기값 획득에서 시작해 GOF 판독, 경쟁 모델 선택, 이상치(outlier) 판단, 편미분 기반 샘플링 설계(sampling design), 민감도 분석(sensitivity analysis)까지 이어지는 한 사이클의 실행 척추입니다. [p.352]

<!-- MASTER LENS -->
### 핵심 아이디어(Big Idea)

이 범위의 핵심은 "좋은 통계량을 계산하는 법"이 아니라 **통계량을 적용해도 되는 조건을 아는 법**입니다. F-test, AIC/SC, 상관계수(correlation coefficient), WRSS, 편미분(partial derivatives)은 각각 강력한 도구입니다. 그러나 중첩(nested) 조건, 가중치(weighting) 조건, 잔차의 무작위성(residual randomness), 파라미터 식별가능성(parameter identifiability), 샘플링 민감도(sampling sensitivity)를 벗어나면 이 숫자들은 오히려 잘못된 모델 확신을 만듭니다. [pp.369–391, pp.399–405]

<!-- SLIDE_START: S04 | title: 모델링 회전고리 항법도 | source_anchor: §1 개념 항법도 -->
> **핵심 메시지:** 초기값·잔차·모델판별·설계는 직선 순서가 아니라 다음 실험으로 되돌아가는 폐루프입니다.

### 개념 항법도

```text
[초기값 획득] → [잔차 진단] → [F-test/AIC/SC 모델 판별]
      ↑              ↓                  ↓
[민감도 분석] ← [편미분 sampling design] ← [정밀도·상관·설계]
```

<!-- ANCHOR -->
위 흐름은 닫힌 고리입니다. 초기값이 나쁘면 회귀가 잘못된 최솟값(minimum)으로 갑니다. 잔차가 무작위가 아니면 모델 또는 가중치(weighting)가 틀린 것입니다. 모델 비교 조건을 어기면 통계 검정이 무의미합니다. 그리고 파라미터가 상관되면 다음 실험의 샘플링 설계(sampling design)를 바꿔야 합니다. [p.353, pp.369–389, pp.399–405]

<!-- SLIDE_START: S05 | title: 선행·후행 지식 경계 | source_anchor: §1 지식 그래프 위치 -->
> **핵심 메시지:** 이 세션은 고전 모델 구축 문법을 현대 PopPK workflow로 번역하되 원전 범위를 넘는 구현 규칙은 분리합니다.

### 지식 그래프 위치

**선행 지식**: 1구획/다구획 모델, 비구획분석(NCA, noncompartmental analysis), 비선형 회귀(nonlinear regression), 오차 모델(error model). Ch.4 §4.5 Minimization과 §4.6 Weighting은 pp.365–367 업로드 부재로 `[확인 필요 — pp.365–367 업로드 부재]`를 유지합니다.

**후행 지식**: `[교과서 외 구현 번역]` 현대 PopPK에서는 이 세션의 잔차 진단(residual diagnostics), 파라미터 정밀도(parameter precision), $-2\cdot\log likelihood$ 비교, 설계 피드백(design feedback)이 NONMEM/PsN/xpose류 워크플로우(workflow)로 번역됩니다. 단, 이 도구명들은 업로드 PDF의 직접 내용이 아니라 구현 환경의 번역입니다.

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{-2\cdot\log likelihood}_{\text{현대 likelihood 기반 목적함수 좌표}}
> $$
>
> - **항별 의미:** 이 항은 likelihood가 클수록 더 낮아지는 비교 좌표를 뜻하며, WRSS 기반 비교가 likelihood 기반 프로그램에서 어떤 언어로 번역되는지 보여 줍니다.
> - **실무 직관:** 값이 낮아지는 방향은 모델이 관측자료를 더 그럴듯하게 설명한다는 신호일 수 있습니다. 다만 같은 데이터·오차 구조의 비교 조건이 먼저 필요합니다.
> - **오해 방지:** 이 파일에서는 NONMEM threshold나 SCM rule까지 확장하지 않습니다. 해당 해석은 구현 번역일 뿐 원전 직접 내용이 아닙니다.

<!-- RECAP -->
**§1 요약(Recap)**: 이 세션의 목적은 모델링 결과를 "좋아 보인다"가 아니라 "조건을 만족하므로 비교·해석 가능하다"로 바꾸는 것입니다. 즉, 판단의 언어를 인상에서 조건으로 옮기는 것입니다.

> **거장의 한 줄 — [CRUCIBLE_DERIVED]**  
> 이 한 문장만 머릿속에 고정하고 §2로 진입하세요: **"좋은 적합(fit)은 가설이고, 잔차·정밀도·비교 조건이 그것을 통과시키는 검열이다."** 6개 MUST 카드는 각각 다른 도구처럼 보이지만, 모두 이 한 문장의 검열 절차를 구성합니다. 카드를 6개의 독립 기술로 외우면 사이클이 닫히지 않습니다. 같은 문장의 6개 검열 통과 조건으로 읽어야 모델링 회전고리(modeling carousel)가 회전합니다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.352, Fig.4.16, "잠정 모델에서 데이터 도표까지의 흐름."
Why this matters: 이 그림은 이 세션을 조직하는 원전의 중심 축입니다. EDA와 초기값(initial estimates)이 과정의 끝이 아니라, 적합(fitting), 출력 분석(output analysis), 그리고 다음 실험으로 이어진다는 점을 보여 줍니다.
When to look: §1 요약(Recap)을 읽은 뒤, MUST 카드로 들어가기 전에 확인하시면 됩니다.
Learner instruction: Explore data → Fit model(s) → Analyze output으로 이어진 뒤 다시 Design으로 돌아가는 화살표를 따라가 보세요. 모든 MUST 카드는 고립된 기술이 아니라, 이 루프의 한 부분으로 읽으시면 됩니다.
<!-- /FIGURE_POINTER -->

> **실무 렌즈(Practice Lens) — [CRUCIBLE_DERIVED]**  
> 이 세션은 "모델을 한 번 잘 맞추기"가 아니라, 출력(output)을 다음 설계(design)로 되돌리는 폐루프 사고를 훈련합니다. 각 MUST 카드는 독립 기술이 아니라 다음 실험을 더 정보성 있게 만들기 위한 판단 장치로 읽어야 합니다.

> <!-- SLIDE_START: S06 | title: Volume II로 넘기는 운영 도구 경계 | source_anchor: Scope-Honesty Callout -->
> **핵심 메시지:** File 15는 모델 구축의 이론 절반을 잠그고, VPC·NPDE·bootstrap·추정법 운영 훈련은 별도 모듈로 넘깁니다.

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

<!-- SLIDE_START: S07 | title: 추정법 브리지 | source_anchor: 최소 추정법 브리지 -->
> **핵심 메시지:** 추정법은 계산 옵션이 아니라 likelihood와 ETA를 어떤 근사 언어로 읽을지 정하는 해석 조건입니다.

### 최소 추정법 브리지: FO/FOCE/FOCEI/Laplacian/SAEM을 어떻게 읽을 것인가 [EXPERT_INFERENCE, v3.5.2]

FO, FOCE, FOCEI, Laplacian, SAEM은 단순한 계산 옵션이 아니라 "모델을 어떤 근사 언어로 읽을 것인가"를 정하는 선택지입니다. FO는 가장 단순한 linearization 관점입니다. 빠르고 출발점으로 유용하지만, 비선형성이 강하거나 IIV가 크면 평균 개체 주변의 근사가 실제 개체별 거동을 충분히 따라가지 못할 수 있습니다. FOCE는 개체별 ETA 주변에서 conditional approximation을 수행한다는 직관으로 읽으면 됩니다. 그래서 EBE, ETA diagnostic, shrinkage를 해석할 때 "개체별 정보가 얼마나 추정에 반영되었는가"라는 질문과 자연스럽게 연결됩니다. FOCEI는 residual error와 ETA 또는 prediction의 interaction이 중요할 때 그 상호작용을 근사에 반영하려는 선택입니다. Laplacian은 likelihood curvature와 비정규·복잡 likelihood를 더 잘 다루기 위한 근사로 이해하면 됩니다. SAEM은 simulation-based estimation이므로 복잡한 비선형 mixed-effects 구조에서 강점을 가질 수 있지만, 항상 자동으로 우월한 방법은 아닙니다. 핵심은 estimation method가 OFV, parameter precision, EBE/shrinkage, diagnostic 해석에 영향을 주는 판단 조건이라는 점입니다.

<!-- SLIDE_START: S08 | title: Qualification 브리지 | source_anchor: 최소 qualification 브리지 -->
> **핵심 메시지:** GOF는 출발점일 뿐이며 predictive performance와 parameter uncertainty는 simulation·resampling 진단으로 닫아야 합니다.

### 최소 qualification 브리지: GOF만으로 끝나지 않는 이유 — VPC, pcVPC, NPDE, bootstrap, SIR [EXPERT_INFERENCE, v3.5.2]

GOF는 population fit과 individual fit을 먼저 보는 기본 시각 진단입니다. 그러나 곡선이 잘 맞아 보인다는 인상만으로 predictive performance가 보장되지는 않습니다. VPC는 모델이 관측자료의 central tendency와 variability envelope을 simulation으로 재현하는지 확인하는 check입니다. pcVPC는 dose, design, covariate, time-varying prediction 차이가 커서 단순 VPC가 "모델 실패"와 "예측 스케일 차이"를 섞어 보일 때 prediction correction으로 비교 좌표를 맞추는 장치입니다. NPDE는 simulated distribution 안에서 관측값이 얼마나 이상한 위치에 놓이는지 표준화해 보는 진단으로 이해하면 됩니다. Bootstrap은 반복 resampling으로 parameter stability와 uncertainty를 확인하고, SIR은 proposal distribution을 바탕으로 parameter uncertainty를 보정하거나 평가하는 도구입니다. 실무 판단 흐름은 "GOF → residual diagnostics → VPC/pcVPC/NPDE → bootstrap/SIR → clinical/scientific plausibility"로 닫는 것이 안전합니다. 여기서 qualification은 사용 목적에 맞게 모델이 충분히 신뢰 가능한지 보는 과정이며, validation을 절대적 진실 인증처럼 쓰면 안 됩니다.

---

## §2 — 개념 해부 카드

<!-- SLIDE_START: S09 | title: MUST 1 — 초기값의 의미 | source_anchor: MUST 1 -->
> **핵심 메시지:** 초기값은 알고리즘 입력값이 아니라 모델러가 EDA에서 추출해 넘기는 도메인 지식 기반 판단입니다.

### ▣ MUST 1 — 초기값 획득의 실전 기술(Initial Estimate Acquisition)

<!-- MASTER LENS -->
**핵심 아이디어(Big Idea)**: 초기값은 회귀 알고리즘의 출발점이 아니라, 모델러가 EDA에서 추출해 알고리즘에 넘겨주는 **도메인 지식 기반 사전 추정값(domain-informed prior)**입니다. 즉, 알고리즘이 어디서 탐색을 시작할지 정하는 모델러의 첫 판단입니다. Gabrielsson은 초기값이 나쁘면 잘못된 최종 추정값(wrong final values), 원치 않는 국소 최솟값(unwanted local minima), 생리학적으로 불가능한 파라미터 값(physiologically impossible parameter values)으로 수렴할 수 있다고 경고합니다. [p.353]

#### A. 형식적 정의(Formal Definition)

초기값 획득(initial estimate acquisition)은 비선형 회귀(nonlinear regression)를 시작하기 전에 그래프, 선형 회귀(linear regression), NCA, 선행 화합물 지식(prior compound knowledge)으로 시작 파라미터 벡터(starting parameter vector)를 구성하는 절차입니다. 이 단계는 적합(fit) 이전에 끝나야 합니다. 비선형 회귀는 시작 벡터(starting vector)가 주어진 뒤에야 목적함수 표면(objective function surface), 즉 파라미터 조합에 따라 잔차 제곱합 값이 분포하는 지형을 탐색하기 때문입니다. 이는 모델링 회전고리(modeling carousel)의 Explore data 단계에 속합니다. [pp.352–353]

#### B. 원전 고정 유도 기준점(Source-locked derivation anchors)

<!-- SLIDE_START: S10 | title: IV bolus anchor 계산 | source_anchor: MUST 1 B-1 -->
> **핵심 메시지:** 반로그 기울기 하나는 K, 반감기, AUC, Cl, V로 이어지는 초기값 사슬의 첫 고리입니다.

**B-1. IV bolus 1구획 예시(one-compartment example)**: 두 피험자에게 동일한 10 mg IV bolus를 투여한 뒤 반로그 농도-시간 도표(semi-log concentration–time plot)에서 기울기(slope)를 읽습니다. 이 기울기가 제거속도상수(elimination rate constant) $K$의 초기 기준점(anchor)이 됩니다. [pp.353–354]

$$\text{slope}=\frac{\ln(800)-\ln(400)}{23-87}=-0.01\ \text{min}^{-1}=-K \quad [\text{Eq.4:16},\ p.354]$$

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{\text{slope}}_{\text{반로그 직선 기울기}}=\frac{\overbrace{\ln(800)-\ln(400)}^{\text{log 농도 차}}}{\underbrace{23-87}_{\text{시간 차}}}=\underbrace{-0.01\ \text{min}^{-1}}_{\text{음의 소실 기울기}}=-\underbrace{K}_{\text{제거속도상수}} \quad [\text{Eq.4:16},\ p.354]
> $$
>
> - **항별 의미:** 좌변은 반로그 농도-시간 직선의 기울기를 정의하며, 우변은 두 log 농도 차이를 시간 차이로 나누어 제거속도상수 K의 음수로 연결합니다.
> - **실무 직관:** K가 커질수록 기울기는 더 가파른 음수가 되고 농도는 더 빨리 감소합니다. 이 값은 half-life, AUC, clearance, volume 초기값의 출발점이 됩니다.
> - **오해 방지:** 기울기 자체를 K와 같은 양수로 읽으면 안 됩니다. 반로그 terminal slope는 보통 -K로 읽고, K는 그 절댓값입니다.

이로부터 다음 초기값이 이어진다. [p.354]

$$t_{1/2}=\frac{\ln2}{K}=\frac{0.693}{0.01}\approx65\ \text{min} \quad [\text{Eq.4:17}]$$

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{t_{1/2}}_{\text{반감기}}=\frac{\overbrace{\ln2}^{\text{50\% 감소 상수}}}{\underbrace{K}_{\text{제거속도상수}}}=\frac{0.693}{0.01}\approx\underbrace{65\ \text{min}}_{\text{초기 반감기 anchor}} \quad [\text{Eq.4:17}]
> $$
>
> - **항별 의미:** 좌변은 농도가 절반으로 감소하는 시간을 예측하고, 우변은 ln2를 제거속도상수 K로 나누어 그 시간을 계산합니다.
> - **실무 직관:** K가 증가하면 분모가 커지므로 t1/2는 짧아집니다. 반감기는 sampling window와 terminal phase 판독의 첫 기준점이 됩니다.
> - **오해 방지:** 반감기는 투여량에 직접 비례하지 않습니다. 이 식에서는 K가 반감기를 지배합니다.

$$AUC=\frac{C^0}{K}=100{,}000\ \mu g\cdot L^{-1}\cdot\text{min} \quad [\text{Eq.4:18}]$$

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{AUC}_{\text{전신 노출}}=\frac{\overbrace{C^0}^{\text{외삽 초기농도}}}{\underbrace{K}_{\text{제거속도상수}}}=\underbrace{100{,}000\ \mu g\cdot L^{-1}\cdot\text{min}}_{\text{노출 anchor}} \quad [\text{Eq.4:18}]
> $$
>
> - **항별 의미:** 좌변은 시간에 따른 농도 노출의 총량을 정의하고, 우변은 초기농도를 제거속도상수로 나누어 1구획 IV bolus의 노출을 계산합니다.
> - **실무 직관:** C0가 커지면 AUC는 커지고, K가 커지면 AUC는 작아집니다. AUC는 clearance 계산과 노출 비교의 기준 좌표입니다.
> - **오해 방지:** AUC를 단순한 그림의 면적으로만 보지 말고, 제거 능력과 연결되는 전신 노출 지표로 읽어야 합니다.

$$Cl=0.1\ L\cdot\text{min}^{-1},\qquad V=10\ L \quad [\text{Eq.4:19–4:20}]$$

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{Cl}_{\text{전신 청소율}}=\underbrace{0.1\ L\cdot\text{min}^{-1}}_{\text{dose/AUC 기반 값}},\qquad \underbrace{V}_{\text{분포용적}}=\underbrace{10\ L}_{\text{dose/}C^0\text{ 기반 값}} \quad [\text{Eq.4:19–4:20}]
> $$
>
> - **항별 의미:** 좌변들은 각각 체내에서 약물이 제거되는 용량-시간 개념인 Cl과, 초기농도를 설명하는 겉보기 분포공간 V를 나타냅니다.
> - **실무 직관:** AUC가 작을수록 같은 dose에서 Cl은 커지고, C0가 낮을수록 같은 dose에서 V는 커집니다. 두 값은 초기 THETA를 생리적으로 묶어 줍니다.
> - **오해 방지:** Cl과 V를 독립적인 숫자 두 개로 외우면 안 됩니다. 이 예시에서는 dose, AUC, C0에서 파생된 서로 연결된 anchor입니다.

<!-- SLIDE_START: S11 | title: 이중지수 곡선 분리 | source_anchor: MUST 1 B-2 -->
> **핵심 메시지:** Curve stripping은 말단 성분을 먼저 읽고 빼서 초기 성분을 드러내는 시간 스케일 분리 기술입니다.

**B-2. 이중지수 곡선 분리(Bi-exponential curve stripping)**: [p.354]

$$C=Ae^{-\alpha t}+Be^{-\beta t}\quad [\text{Eq.4:21},\ p.354]$$

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{C}_{\text{총 농도}}=\overbrace{\underbrace{A}_{\text{초기 빠른 성분}}e^{-\underbrace{\alpha}_{\text{빠른 기울기}}t}}^{\text{분포/초기상}}+\overbrace{\underbrace{B}_{\text{말단 성분}}e^{-\underbrace{\beta}_{\text{느린 기울기}}t}}^{\text{제거/말단상}} \quad [\text{Eq.4:21},\ p.354]
> $$
>
> - **항별 의미:** 좌변은 시간 t에서의 관측 농도를 예측하고, 우변은 빠른 초기 성분과 느린 말단 성분의 합으로 농도-시간 곡선을 구성합니다.
> - **실무 직관:** alpha가 클수록 A 성분은 빨리 사라지고, beta가 클수록 B 성분의 말단 소실도 빨라집니다. 두 기울기가 분리될수록 curve stripping이 안정적입니다.
> - **오해 방지:** 말단부에서 보이는 직선을 전체 소실 과정 전체와 동일시하면 안 됩니다. 초기 분포 성분 A exp(-alpha t)가 충분히 사라진 뒤에야 beta가 말단 기울기로 읽힙니다.

말단상(terminal phase)에서 $B$와 $\beta$를 먼저 읽고, 후방 외삽된 말단선(back-extrapolated terminal line)을 초기상(initial phase)에서 빼서 $A$와 $\alpha$를 얻습니다. Fig.4.18의 기준값(anchor values)은 $A=1.0\ \mu g\cdot L^{-1}$, $B=0.8\ \mu g\cdot L^{-1}$, $\alpha=0.05\ \text{min}^{-1}$, $\beta=0.003\ \text{min}^{-1}$입니다. [p.355]

<!-- SLIDE_START: S12 | title: 동적 response anchor | source_anchor: MUST 1 B-3/B-4 -->
> **핵심 메시지:** 동적 response에서는 농도-효과 관계와 turnover 하강 기울기가 PD 초기값의 실제 anchor가 됩니다.

**B-3. 동적 평형 반응(Dynamic equilibrium response)**: 반응-농도(response–concentration) 관계에서는 선형-선형 도표(lin-lin plot)와 반로그 도표(semi-log plot)가 서로 다른 정보를 줍니다. 반로그 도표는 $IC_{50}$ 이하 구간을 확장해 $IC_{50}$ 초기 추정값(initial estimate)을 더 쉽게 읽게 합니다. [pp.355–356]

**B-4. 동적 비정상상태 turnover(Dynamic non-steady-state turnover)**: Warfarin이 prothrombin complex synthesis를 차단하면 하강 구간 기울기(downswing slope)가 $-k_{out}$를 줍니다. [pp.356–357]

$$\text{slope}=\frac{\ln(124)-\ln(56.77)}{24-0}\approx -0.03\ h^{-1}\quad [\text{Eq.4:22},\ p.356]$$

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{\text{slope}}_{\text{하강 구간 기울기}}=\frac{\overbrace{\ln(124)-\ln(56.77)}^{\text{log 반응 차}}}{\underbrace{24-0}_{\text{시간 차}}}\approx\underbrace{-0.03\ h^{-1}}_{\text{원문 표시 }-k_{out}} \quad [\text{Eq.4:22},\ p.356]
> $$
>
> - **항별 의미:** 좌변은 turnover response의 하강 구간 기울기를 읽고, 우변은 두 반응값의 log 차이를 시간 차이로 나누어 kout의 초기 anchor로 연결합니다.
> - **실무 직관:** kout이 커질수록 response는 더 빠르게 baseline 쪽으로 움직입니다. 이 값은 kin과 turnover time scale을 결정하는 실무 기준점입니다.
> - **오해 방지:** 표시된 산술 부호를 그대로 계산식으로 기계 적용하면 문맥과 충돌할 수 있습니다. 이 식은 하강 기울기를 -kout로 읽는 문맥 안에서 해석해야 합니다.
>
> **검토 메모:** 이 수식은 문맥상 하강 구간 slope가 -kout을 주는 식으로 읽는 것이 자연스럽습니다. 단, 원문 보존 원칙에 따라 원 수식은 수정하지 않았습니다.

이 식은 PDF에 표시된 형태를 보존합니다. 다만 산술 부호에는 원전 내부 불일치(source-internal inconsistency)가 있습니다. 수학적으로 재작성하려면 $[\ln(56.77)-\ln(124)]/(24-0)$ 또는 $[\ln(124)-\ln(56.77)]/(0-24)$가 됩니다. 따라서 이는 draft source mismatch가 아니라 원문 내부 부호 문제입니다. Baseline 120 sec와 $k_{out}\approx0.03\ h^{-1}$로 $k_{in}=3.6\ \text{sec}\cdot h^{-1}$를 얻습니다. [p.357]

<!-- SLIDE_START: S13 | title: 간접반응·반복투여·경계 스케일링 | source_anchor: MUST 1 B-5/B-7 -->
> **핵심 메시지:** 초기값 계산은 단순 출발값 생성이 아니라 후보 모델 선택과 경계 의존성 점검으로 이어집니다.

**B-5. 간접반응 모델 선택 예시(Indirect response model-choice example)**: Eq.4:23–4:33은 baseline, 정상상태(steady state), $E_{max}$, $k_{out}$, $k_{in}$, 지수(exponent) $n$을 그래프에서 순차 도출하는 예입니다. Table 4.3은 Model 1과 Model 4의 최종 추정값(final estimates)과 초기 추정값(initial estimates)을 비교하며, WRSS/AIC가 Model 1에서 7.3/83, Model 4에서 12/102로 제시됩니다. 이 예시는 "초기값 계산"이 곧 "모델 선택"의 전 단계임을 보여 줍니다. [pp.358–360]

**B-6. 반복투여 항불안제 예시(Repeated-dose anxiolytic example)**: Eq.4:34의 경구 PK 입력(oral PK input)은 $K_a=1.1\ h^{-1}$, $K=0.128\ h^{-1}$, $V/F=5.0\ L\cdot kg^{-1}$로 고정해 반응 모델(response model)에 넣습니다. PD turnover는 $dR/dt=k_{in}I(C)-k_{out}R$이고, $k_{out}\approx0.06\ h^{-1}$, $k_{in}=4.8$ units, $IC_{50}\approx0.25\ \mu g\cdot L^{-1}$가 초기 기준점(initial anchor)으로 사용됩니다. [pp.361–363]

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{\frac{dR}{dt}}_{\text{반응 변화율}}=\overbrace{\underbrace{k_{in}}_{\text{생성 속도}}\underbrace{I(C)}_{\text{농도 의존 억제/입력 함수}}}^{\text{입력 항}}-\overbrace{\underbrace{k_{out}}_{\text{소실 속도}}\underbrace{R}_{\text{현재 반응}}}^{\text{출력 항}}
> $$
>
> - **항별 의미:** 좌변은 시간에 따른 response의 변화율이고, 우변은 생성/입력 항에서 소실/출력 항을 뺀 turnover balance입니다.
> - **실무 직관:** kin이나 I(C)가 커지면 response를 올리는 방향으로, kout이나 R이 커지면 response를 내리는 방향으로 작동합니다. baseline과 time-course를 동시에 설명합니다.
> - **오해 방지:** IC50만 보고 PD를 해석하면 안 됩니다. turnover 모델에서는 kout이 효과의 시간 지연과 회복 속도를 함께 지배합니다.

**B-7. 다른 방법이 모두 어려울 때 — 경계값 스케일링(boundary scaling)**: 초기값을 직접 얻기 어렵다면 하한/상한 경계(lower/upper boundary)를 이용해 파라미터를 0–1 범위로 스케일링(scaling)합니다. [p.364]

$$\frac{IE-LB}{UB-LB}\quad [\text{Eq.4:44},\ p.364]$$

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{\frac{\overbrace{IE-LB}^{\text{초기값이 하한에서 떨어진 거리}}}{\underbrace{UB-LB}_{\text{허용 경계 폭}}}}_{\text{0--1 스케일의 초기값 위치}} \quad [\text{Eq.4:44},\ p.364]
> $$
>
> - **항별 의미:** 이 식은 좌변 전체가 초기 추정값 IE가 lower boundary와 upper boundary 사이에서 어디에 위치하는지 정의합니다.
> - **실무 직관:** IE가 LB에 가까우면 값은 0에 가까워지고, UB에 가까우면 1에 가까워집니다. 경계 내부에서 탐색을 안정화하는 scaling 판단을 가능하게 합니다.
> - **오해 방지:** 스케일 값이 좋아 보인다고 해서 파라미터가 식별된 것은 아닙니다. 최종값이 LB/UB에 붙으면 정보가 아니라 경계가 값을 만든 것일 수 있습니다.

원문은 일반적으로 $0.1\cdot IE$부터 $10\cdot IE$까지의 상대 범위(relative range)를 권합니다. 그러나 Table 4.4처럼 원전 특이적 경계(source-specific boundary)가 예외를 만들 수 있으므로, 이 규칙을 기계적으로 적용하면 안 됩니다. [p.364]

<!-- TRENCH -->
**현장 수준 팁(Trench-Level Tip)**: `[교과서 외 구현 번역]` 경계값 스케일링(boundary scaling)을 현대 비선형 추정(nonlinear estimation)에서 사용할 때 최종 추정값(final estimate)이 LB 또는 UB에 붙으면, 모델이 정보를 준 것이 아니라 경계(boundary)가 추정값을 만든 것일 수 있습니다. Table 4.4의 $\beta=0.05$와 UB=0.05는 그대로 모방할 처방(prescription)이 아니라 경계 의존성(boundary dependence)을 의심하게 하는 교육용 예시(teaching example)로 읽어야 합니다. [p.364]

<!-- SLIDE_START: S14 | title: MUST 1 구조적 필연성과 recap | source_anchor: MUST 1 C/D -->
> **핵심 메시지:** 초기값이 생리적으로 그럴듯하지 않으면 비선형 회귀는 올바른 최솟값이 아니라 잘못된 basin을 성실히 찾을 수 있습니다.

#### C. 구조적 필연성(Structural Necessity)

이중지수 곡선 분리(bi-exponential curve stripping)가 가능한 이유는 $\alpha \gg \beta$일 때 말단상(terminal phase)에서 $Ae^{-\alpha t}$가 사라지고 $Be^{-\beta t}$만 남기 때문입니다. 즉, 반로그 도표(semi-log plot)는 시간 스케일 분리를 눈으로 확인하게 해주는 장치입니다. 두 기울기(slope)가 충분히 분리되지 않으면 곡선 분리는 불안정합니다. [pp.354–355]

#### D. 가정과 경계(Assumptions & Boundaries)

초기값은 "정확한 값"일 필요는 없습니다. 그러나 생리학적으로 타당해야(physiologically plausible) 하고, 목적함수 표면(objective function surface)에서 잘못된 분지(basin), 즉 수렴 가능한 극솟값 영역으로 들어가지 않을 정도로는 근접해야 합니다. 또한 화합물 지식 기반(compound knowledge base)을 일찍 만들고 회귀 목적(regression objective)을 명확히 해야 합니다. 그렇지 않으면 모델링(modeling)은 끝없는 여정(journey)이 됩니다. [p.353]

<!-- RECAP -->
**MUST 1 요약(Recap)**: 초기값은 계산 전의 사전 판단입니다. 그래프(graph) → 기울기/절편/고원(slope/intercept/plateau) → 초기 추정값(initial estimates) → 회귀(regression)라는 순서를 바꾸면, 알고리즘이 모델러의 눈을 대신할 수 없습니다.

> **체화 꿀팁 — [CRUCIBLE_DERIVED]**  
> Fit 버튼을 누르기 전에 종이에 (1) 각 파라미터(parameter)의 예상값과 (2) 그 근거(graph slope, NCA, 선행 화합물)를 적어두세요. 결과가 그 예상과 크게 어긋나면, 모델 결함이 아니라 초기값이 잘못된 분지(basin)에 들어갔을 가능성을 먼저 의심합니다. 이 한 단계가 적합(fit) 결과의 1차 타당성 점검(sanity check)이 됩니다.

<!-- SLIDE_START: S15 | title: MUST 1 도식과 practice brief | source_anchor: MUST 1 FIGURE_SCHEMATIC -->
> **핵심 메시지:** 이중지수 도식의 핵심은 말단 slope를 먼저 읽고 잔여 초기상을 분리해야 한다는 절차 기억입니다.

<!-- FIGURE_SCHEMATIC -->
Title: 이중지수 곡선 분리: 말단상 먼저 읽는 논리
Mode: R
Visual objective: 학습자가 5초 안에 말단 기울기(terminal slope)를 먼저 분리해 읽고, 이를 빼서 초기 기울기(initial slope)를 드러내는 순서를 파악해야 합니다.
Core message: 곡선 분리(curve stripping)는 빠른 시간 스케일과 느린 시간 스케일이 시각적으로 구분될 때만 작동합니다.
Elements to include: 반로그 농도-시간 축(semi-log concentration–time axes); 일반화된 관측 이중지수 곡선(observed bi-exponential curve); “B와 beta를 먼저 읽음”이라고 표시된 말단선(terminal line); 후방 외삽된 말단선(back-extrapolated terminal line); “말단 성분을 뺀 뒤 → A와 alpha를 읽음”이라고 표시된 잔여 초기선(residual initial line); “alpha ≈ beta이면 불안정” 경고 라벨.
Elements to exclude: 교과서 그림의 정확한 시각 양식; 과도하게 촘촘한 눈금 또는 원전 점의 정밀 복제; 본문에 이미 제시된 추가 PK 방정식.
Suggested rendering: SVG
Caption: 곡선 분리 논리를 단순화한 재도식입니다. 말단상 정보를 먼저 추출한 뒤, 이를 제거하여 초기상을 드러냅니다.
Alt text: 전체 이중지수 곡선, 후방 외삽된 말단선, 잔여 초기선을 함께 보여 주는 반로그 농도-시간 도식.
Source relation: 교과서 개념을 바탕으로 새로 그린 도식
<!-- /FIGURE_SCHEMATIC -->

> **실패 모드(Failure Mode) — [TEXTBOOK_DERIVED]**  
> 초기값이 "대충 맞는 숫자"처럼 보여도 목적함수(objective function)의 잘못된 분지(basin)로 들어가면 회귀는 그 오류를 스스로 고치지 못합니다. 따라서 적합(fit) 전에 그래프, 화합물 지식(compound knowledge), 회귀 목적(regression objective)을 먼저 명시하는 것이 초기값 계산의 일부입니다.

> **▶ 실무 체화 요약 (Practice Brief) — MUST 1 체화 4축 — [EXPERT_INFERENCE, v3.3]**
> - **왜 알아야 하는가**: 비선형 회귀(nonlinear regression)는 초기값 품질이 수렴(convergence)과 국소 최솟값(local minimum) 회피를 결정합니다. 따라서 그래프·잔차 기반 초기값 도출 없이 적합(fitting)을 시작하면 그 이후의 모든 진단(MUST 2)·모델 판별(MUST 3)·정밀도 평가(MUST 4)가 출발점부터 흔들립니다.
> - **흐름상 역할**: 본 세션의 입구이자 후속 5개 카드(MUST 2–6) 모두에 대한 사전 조건; EDA·항법도 사고를 §4 모델 구축 단계로 번역하는 다리.
> - **체화 꿀팁**: 본문의 그래프 방법(graphical method; semi-log slope·intercept·peeling)을 손으로 한 번 적용해 보세요. 그리고 "fitting을 열기 전에 종이 위에 초기값 후보 1개를 먼저 적는다"는 루틴을 30분 안에 정착시키면 됩니다.
> - **실무 활용**: 새 PK 데이터셋을 받았을 때 NONMEM control stream을 열기 전에 EDA 도표 위에서 $V$, $CL$, $K_a$ 초기값을 그래프로 도출(graphical derivation)하고, 이 값을 `$THETA` initial로 명시 입력하여 수렴 안정성을 확보합니다.

---

<!-- SLIDE_START: S16 | title: MUST 2 — 잔차 정의 | source_anchor: MUST 2 -->
> **핵심 메시지:** GOF는 곡선이 지나가는지보다 잔차가 시간·예측값 축에서 무작위로 남는지를 묻는 절차입니다.

### ▣ MUST 2 — 잔차 기반 모델 진단(Residual-Based Diagnostics)

<!-- MASTER LENS -->
**핵심 아이디어(Big Idea)**: 관측값 대 예측값 곡선(observed vs predicted curve)만 보면 계통오차(systematic error)가 숨어 보일 수 있습니다. 잔차 도표(residual plot)는 이 숨은 오차를 부호와 순서로 다시 펼쳐 줍니다. 따라서 모델이 놓친 구조, 시간 스케일, 또는 오차 모델(error model)을 노출하는 최소 진단 도구입니다. [pp.368–370]

#### A. 형식적 정의(Formal Definition)

잔차(residual), 즉 관측값과 예측값의 차이는 관측값(observed value)과 계산/예측값(calculated/predicted value) 사이의 수직 거리(vertical distance)입니다. <!-- ANNOTATION --> [p.369]

$$\epsilon=N(0,\sigma^2)\quad [\text{Eq.4:46},\ p.369]$$

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{\epsilon}_{\text{잔차오차}}=\underbrace{N(0,\sigma^2)}_{\text{평균 0, 분산 }\sigma^2\text{인 정규 오차}} \quad [\text{Eq.4:46},\ p.369]
> $$
>
> - **항별 의미:** 좌변은 모델이 설명하지 못한 잔차오차를 나타내고, 우변은 그 오차가 평균 0의 정규분포를 따른다는 오차 모델 가정을 둡니다.
> - **실무 직관:** sigma가 커질수록 관측값이 예측값 주변에 더 넓게 흩어질 수 있습니다. 이 가정은 잔차 도표가 무작위인지 판단하는 기준입니다.
> - **오해 방지:** epsilon은 구조 모델이 놓친 패턴을 무조건 흡수하는 쓰레기통이 아닙니다. 잔차에 run이나 fan shape가 있으면 오차 가정 자체가 흔들립니다.

$$residual_i=C_{obs,i}-\hat C_{calc,i}\quad [\text{Fig.4.41},\ p.369]$$

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{residual_i}_{\text{i번째 잔차}}=\underbrace{C_{obs,i}}_{\text{관측 농도}}-\underbrace{\hat C_{calc,i}}_{\text{모델 예측 농도}} \quad [\text{Fig.4.41},\ p.369]
> $$
>
> - **항별 의미:** 좌변은 i번째 관측점에서 모델이 남긴 오차를 정의하고, 우변은 관측 농도에서 계산/예측 농도를 뺀 값입니다.
> - **실무 직관:** 관측값이 예측값보다 크면 잔차는 양수, 작으면 음수입니다. 부호의 연속성은 모델이 놓친 시간 구조를 드러냅니다.
> - **오해 방지:** 잔차의 크기만 보면 안 됩니다. 부호와 시간 순서가 함께 보존되어야 systematic deviation을 진단할 수 있습니다.

가중잔차제곱합(WRSS, weighted residual sum of squares)은 다음과 같습니다. [p.371]

$$WRSS=\sum W_i(C_i-\hat C_i)^2\quad [\text{Eq.4:47},\ p.371]$$

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{WRSS}_{\text{가중잔차제곱합}}=\sum \underbrace{W_i}_{\text{i번째 가중치}}\underbrace{(C_i-\hat C_i)^2}_{\text{i번째 잔차 제곱}} \quad [\text{Eq.4:47},\ p.371]
> $$
>
> - **항별 의미:** 좌변은 모델-데이터 불일치의 가중 합을 정의하고, 우변은 각 잔차 제곱에 관측점별 가중치 Wi를 곱해 더합니다.
> - **실무 직관:** 잔차가 커지거나 가중치가 커지면 WRSS가 증가합니다. 모델 비교와 precision 계산의 수치 기반이 됩니다.
> - **오해 방지:** WRSS가 낮다고 항상 좋은 모델은 아닙니다. 서로 다른 weighting scheme에서 나온 WRSS는 같은 좌표계의 숫자가 아닐 수 있습니다.

$$\sigma=\sqrt{\frac{WRSS}{N_{obs}-N_{par}}}\quad [\text{Eq.4:48},\ p.371]$$

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{\sigma}_{\text{잔차 표준편차 추정}}=\sqrt{\frac{\overbrace{WRSS}^{\text{남은 불일치}}}{\underbrace{N_{obs}-N_{par}}_{\text{잔차 자유도}}}} \quad [\text{Eq.4:48},\ p.371]
> $$
>
> - **항별 의미:** 좌변은 잔차오차의 표준편차를 추정하고, 우변은 WRSS를 잔차 자유도로 나눈 뒤 제곱근을 취합니다.
> - **실무 직관:** WRSS가 커지면 sigma가 커지고, 같은 WRSS라도 파라미터 수가 많아져 자유도가 줄면 sigma가 커질 수 있습니다.
> - **오해 방지:** 파라미터를 많이 넣어 WRSS를 낮추는 것만으로는 충분하지 않습니다. 자유도 손실과 잔차 패턴을 함께 보아야 합니다.

<!-- SLIDE_START: S17 | title: 잔차 패턴 카탈로그 | source_anchor: MUST 2 B -->
> **핵심 메시지:** 잔차 모양은 구조 모델, 오차/가중치 모델, 데이터/설계 문제 중 어디를 고칠지 알려주는 분기 신호입니다.

#### B. 진단 패턴 목록(Diagnostic pattern catalogue)

잔차(residual)는 무작위 산포(random scatter)를 보여야 합니다. 따라서 연속적인 양성/음성 잔차(consecutive positive/negative residuals)가 run, 즉 같은 부호 잔차가 연속으로 이어지는 패턴으로 나타나거나 군집(cluster)이 생기면, 단순 잡음(noise)이 아니라 모델 부적절성(model inadequacy)을 의심해야 합니다. [pp.369–372]

- 잔차 대 시간(residual vs time)에서 banana/U-shape가 보이면 누락된 지수항(missing exponential term) 또는 잘못된 구조적 시간 스케일(wrong structural time scale)을 의심합니다. [pp.372–376]
- 잔차 진폭(residual amplitude)이 농도(concentration)와 함께 커지는 fan shape이면, 등분산 가정(constant variance assumption) 또는 가중치(weighting)가 틀렸을 수 있습니다. [pp.373–374]
- Ordinary Emax와 sigmoid Emax 비교에서는 예측 곡선(predicted curve)만으로 애매한 차이가 잔차 도표(residual plot)에서는 계통적 이탈(systematic deviation)로 드러납니다. [pp.372–373]
- 가중치 지수(weighting power/exponent)는 원문(source text)에서 $0$, $-1$, $-2$, $-n$으로 설명되며, Eq.4:49는 $C_i^{-\lambda_z}$ 또는 $\hat C_i^{-\lambda_z}$ 형태를 씁니다. 즉, "$\lambda_z=-1$"처럼 부호를 단정하지 말고 **가중치 지수(weighting power/exponent)**로 표기해야 합니다. [pp.373–374]

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{C_i^{-\lambda_z}\ \text{ 또는 }\ \hat C_i^{-\lambda_z}}_{\text{농도 또는 예측농도 기반 가중치 형태}}
> $$
>
> - **항별 의미:** 이 표현은 잔차에 적용되는 가중치가 관측 농도 또는 예측 농도의 거듭제곱 형태로 달라질 수 있음을 나타냅니다.
> - **실무 직관:** lambda_z가 바뀌면 고농도와 저농도 관측점의 상대적 영향력이 달라집니다. fan shape가 보일 때 weighting 점검을 가능하게 합니다.
> - **오해 방지:** 부호를 단정한 하나의 규칙으로 외우면 안 됩니다. 원문에서는 weighting power/exponent라는 넓은 개념으로 다룹니다.

<!-- ANCHOR -->
잔차 패턴은 단순한 그림 모양이 아닙니다. 이것은 "모델이 설명하지 못한 시간 스케일 또는 분산 구조"가 밖으로 드러난 형태입니다. Banana pattern은 빠른 상(phase)이 빠졌다는 신호일 수 있고, fan pattern은 구조보다 오차분산 모델(error variance model)의 문제일 수 있습니다. [pp.372–376]

<!-- SLIDE_START: S18 | title: Pure error와 lack-of-fit | source_anchor: MUST 2 C -->
> **핵심 메시지:** LOF F-test는 반복 측정으로 pure error를 분리할 수 있을 때만 모델 부적합을 정량 검정합니다.

#### C. 순수오차(Pure error) vs 적합결여(lack-of-fit)

반복 측정(replicate measurement)이 있는 in vitro dataset에서는 잔차오차(residual error)를 순수오차(pure error)와 적합결여(lack-of-fit)로 분해할 수 있습니다. Table 4.7의 예에서 residual SS는 92.67, pure error SS는 23.61, lack-of-fit SS는 69.06이고, Eq.4:51의 $F_{LOF}=15.35$는 $F_{crit}=2.76$보다 커서 lack-of-fit를 지지합니다. [pp.377–379]

$$F_{LOF}=\frac{(92.67-23.61)/(25-21)}{23.61/21}=15.35\quad [\text{Eq.4:51},\ p.379]$$

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{F_{LOF}}_{\text{적합결여 검정 통계량}}=\frac{\overbrace{(92.67-23.61)/(25-21)}^{\text{lack-of-fit 평균제곱}}}{\underbrace{23.61/21}_{\text{pure error 평균제곱}}}=\underbrace{15.35}_{\text{F 비교값}} \quad [\text{Eq.4:51},\ p.379]
> $$
>
> - **항별 의미:** 좌변은 적합결여를 검정하는 F 통계량이며, 우변은 lack-of-fit 평균제곱을 pure error 평균제곱으로 나눈 값입니다.
> - **실무 직관:** 분자가 커질수록 반복 측정으로 설명되는 순수오차를 넘어서는 모델 부적합 신호가 커집니다. Fcrit보다 크면 lack-of-fit을 지지합니다.
> - **오해 방지:** 반복 측정이 없는 sparse clinical PK 자료에 이 검정을 억지로 적용하면 안 됩니다. pure error가 분리될 때만 의미가 있습니다.

<!-- TRENCH -->
**현장 수준 팁(Trench-Level Tip)**: §4.7.3의 LOF F-test는 같은 $x$값에서 반복 측정이 있어 순수오차(pure error)를 계산할 수 있을 때만 가능합니다. 환자별 희소 임상 PK(sparse clinical PK)처럼 같은 시점 반복이 없는 데이터에서는 LOF F-test를 억지로 만들지 말고, 잔차 패턴(residual pattern)과 모델 타당성(model plausibility)을 보아야 합니다.

<!-- TRENCH -->
**현장 수준 팁(Trench-Level Tip)**: 잔차 대 시간(residual vs time)과 잔차 대 예측값/농도(residual vs predicted/concentration)를 함께 보아야 합니다. 한 축에서 무작위 산포(random scatter)처럼 보여도 다른 축에서 fan shape나 구조적 run(structural run)이 나타날 수 있습니다.

<!-- SLIDE_START: S19 | title: MUST 2 구조적 필연성과 도식 | source_anchor: MUST 2 D -->
> **핵심 메시지:** 잔차 도표는 overlay가 숨기는 오차의 부호와 순서를 복원해 systematic deviation을 드러냅니다.

#### D. 구조적 필연성(Structural Necessity)

모델 오지정(model misspecification)은 관측 곡선 중첩(observed curve overlay)보다 잔차 도표(residual plot)에서 먼저 보입니다. 중첩(overlay)은 곡선과 데이터의 절대 위치를 보여 줍니다. 반면 잔차 도표는 오차의 부호와 순서를 보존하므로 계통적 이탈(systematic deviation)을 더 선명하게 드러냅니다. [pp.369–376]

<!-- RECAP -->
**MUST 2 요약(Recap)**: GOF는 "곡선(curve)이 지나가는가"가 아니라 "잔차(residual)가 무작위인가"입니다. 잔차 패턴(residual pattern)이 있으면 모델(model), 가중치(weighting), 샘플링 설계(sampling design) 중 하나가 정보를 잘못 처리하고 있는 것입니다.

> **체화 꿀팁 — [CRUCIBLE_DERIVED]**  
> 잔차는 항상 두 축에 동시에 그립니다(plot): 잔차 대 시간(residual vs time)과 잔차 대 예측값/농도(residual vs predicted/concentration)입니다. 한 plot에서 무작위 산포(random scatter)처럼 보여도 다른 plot에서는 계통적(systematic) 패턴이 노출되는 일이 흔합니다. 두 plot이 모두 무작위일 때만 잔차가 무작위라고 판정합니다. 이 두 축 동시 점검을 무의식 단계까지 끌어내리면 GOF 진단의 절반이 자동화됩니다.

<!-- FIGURE_SCHEMATIC -->
Title: 잔차 패턴 분류: 모양 → 가능성 높은 실패 원인 → 다음 조치
Mode: N
Visual objective: 학습자가 5초 안에 각 잔차 패턴(residual pattern)을 올바른 진단 분기로 연결해야 합니다.
Core message: 잔차 모양(residual shape)은 다음 조치가 구조(structure), 가중치(weighting), 또는 데이터/설계(data/design) 중 어디를 겨냥해야 하는지를 결정합니다.
Elements to include: 네 개의 패턴 박스 — 무작위 산포(random scatter), 계통적 run/banana 패턴(systematic run/banana), 부채꼴 모양(fan shape), 고립된 영향점(isolated leverage point); 진단 라벨 — 허용 가능한 무작위성(acceptable randomness), 구조적 시간 스케일 오류(structural time-scale error), 분산/가중치 오류(variance/weighting error), 이상치/영향점 우려(outlier/leverage concern); 조치 화살표 — 유지/정밀도 확인, 구조 모델 수정, 오차/가중치 모델 수정, 원자료와 leverage 점검; 작은 경고 문구 “처방을 서로 바꾸지 마세요: fan ≠ compartment problem; banana ≠ weighting-only problem.”
Elements to exclude: 교과서 잔차 도표의 정확한 복제; 수치 threshold; 본문 범위에 없는 소프트웨어 특이적 진단.
Suggested rendering: Mermaid flowchart or CSS-card
Caption: 잔차 모양을 가장 그럴듯한 모델링 실패 원인 및 다음 조치와 연결하는 진단 분류 지도입니다.
Alt text: 잔차 산포, banana run, 부채꼴 퍼짐, leverage point를 서로 다른 모델링 대응으로 연결하는 흐름도.
Source relation: 새로 설계한 도식
<!-- /FIGURE_SCHEMATIC -->

> **체화 노트(Mastery Note) — [CRUCIBLE_DERIVED]**  
> 잔차의 시간 패턴은 모델이 놓친 시간 스케일이 밖으로 드러난 흔적입니다. Banana/run을 가중치(weighting) 문제 하나로 덮거나, fan shape를 구조 모델 추가로 해결하려 하면 원인과 처방이 어긋납니다.

<!-- SLIDE_START: S20 | title: MUST 2 practice brief | source_anchor: MUST 2 Practice Brief -->
> **핵심 메시지:** 잔차 패턴을 epsilon으로 덮으면 구조 결함이 가짜 variability나 가짜 covariate 신호로 번역될 수 있습니다.

> **▶ 실무 체화 요약 (Practice Brief) — MUST 2 체화 4축 — [EXPERT_INFERENCE, v3.3]**
> - **왜 알아야 하는가**: 잔차 패턴(residual pattern)에 추세(trend), 계통적 이탈(systematic deviation), 이분산성(heteroscedasticity)이 남아 있으면 그것은 무작위 잡음(random noise)이 아니라 **모델 결함(model misspecification)의 신호**입니다. 이를 $\epsilon$(잔차 분산)으로 흡수해 통과시키면 가짜 IIV 또는 가짜 공변량 신호(covariate signal)가 후속 모델에서 생성됩니다.
> - **흐름상 역할**: MUST 1의 fitting 결과를 검증하는 첫 관문; MUST 3의 F-test 적용 전 필수 단계; §8D GOF Checklist의 입력 단계.
> - **체화 꿀팁**: 본문 잔차 plot 패턴 분류(random scatter / systematic banana·run / fan-shaped heteroscedasticity / leverage point)를 빈 종이에 네 개 모양으로 그려 보세요. 각 모양이 시사하는 모델 결함 원인을 한 줄씩 옆에 적으면 됩니다.
> - **실무 활용**: NONMEM 적합 후 CWRES/IWRES vs time, vs IPRED plot에서 추세(trend)가 보이면 가중치(weighting) 변경 전에 **구조 모델 결함 가능성**을 먼저 보고서에 명시하고, fan shape에서만 weighting 재검토로 넘어갑니다.

---

<!-- SLIDE_START: S21 | title: MUST 3 — F-test apex | source_anchor: MUST 3 -->
> **핵심 메시지:** F-test는 WRSS가 줄었는지가 아니라 nested + equal weighting 조건에서 추가 파라미터가 의미 있는지를 묻습니다.

### ▣ MUST 3 — F 검정 적용 조건(F-Test Validity Conditions) ⚡ 핵심 개념(Apex Concept)

<!-- MASTER LENS -->
**핵심 아이디어(Big Idea)**: F-test는 "더 복잡한 모델이 WRSS(weighted residual sum of squares)를 줄였는가"를 묻는 도구가 아닙니다. <!-- ANNOTATION --> **전체 모델(full model)과 축소 모델(reduced model)이 계층적/중첩(hierarchical/nested) 관계이고, 같은 가중치 방식(weighting scheme)으로 적합(fit)되었을 때만** 추가 파라미터(parameter)의 의미를 검정하는 도구입니다. [pp.387–388]

#### A. 형식적 정의(Formal Definition)

중첩 모델(nested model), 즉 전체 모델(full model)의 제한 형태란 full model에서 특정 파라미터(parameter)를 고정하면 축소 모델(reduced model)로 접히는(collapse) 관계를 말합니다. <!-- ANNOTATION --> Sigmoid Emax model은 지수(exponent) $n=1$로 고정하면 ordinary Emax model이 되므로 nested 관계입니다. [p.388]

F 통계량(F statistic)은 다음 구조를 갖습니다. [p.387]

$$F^*=\frac{(WRSS_{reduced}-WRSS_{full})/(df_{reduced}-df_{full})}{WRSS_{full}/df_{full}}\quad [\text{Eq.4:54},\ p.387]$$

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{F^*}_{\text{중첩 모델 F 통계량}}=\frac{\overbrace{(WRSS_{reduced}-WRSS_{full})/(df_{reduced}-df_{full})}^{\text{추가 parameter당 개선}}}{\underbrace{WRSS_{full}/df_{full}}_{\text{full model 잔차 평균제곱}}} \quad [\text{Eq.4:54},\ p.387]
> $$
>
> - **항별 의미:** 좌변은 축소 모델 대비 전체 모델의 개선을 검정하는 F 통계량이고, 우변은 WRSS 감소를 자유도 손실로 보정해 full model 잔차 변동과 비교합니다.
> - **실무 직관:** WRSS 감소가 클수록 F는 커지지만, 추가 파라미터가 많을수록 개선은 자유도 차이로 나뉩니다. 중첩 모델에서 추가 파라미터의 필요성을 판단합니다.
> - **오해 방지:** 비중첩 모델이나 서로 다른 weighting으로 적합한 모델에는 이 식을 쓰면 안 됩니다. 숫자가 있어도 F 분포 해석이 무너집니다.

$$df=N_{obs}-N_{par}\quad [\text{Eq.4:55},\ p.387]$$

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{df}_{\text{잔차 자유도}}=\underbrace{N_{obs}}_{\text{관측값 수}}-\underbrace{N_{par}}_{\text{추정 parameter 수}} \quad [\text{Eq.4:55},\ p.387]
> $$
>
> - **항별 의미:** 좌변은 모델 적합 후 남는 자유도를 정의하고, 우변은 관측값 수에서 추정한 파라미터 수를 뺀 값입니다.
> - **실무 직관:** Npar가 증가하면 df는 감소합니다. 더 복잡한 모델이 얻는 WRSS 개선은 이 자유도 손실과 함께 평가되어야 합니다.
> - **오해 방지:** df를 단순 표기처럼 지나치면 안 됩니다. F-test, sigma, model comparison에서 복잡도 penalty의 핵심입니다.

<!-- SLIDE_START: S22 | title: F-test valid vs invalid | source_anchor: MUST 3 B/C -->
> **핵심 메시지:** 중첩이란 파라미터 수 차이가 아니라 한 모델이 다른 모델의 제한 형태로 접히는 관계입니다.

#### B. 유효한 예와 무효한 예(Valid vs invalid examples)

- **유효(Valid)**: ordinary Emax vs sigmoid Emax. Full sigmoid model에서 $n=1$을 고정하면 ordinary Emax로 줄어듭니다. [p.388]

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{n}_{\text{sigmoidicity factor}}=\underbrace{1}_{\text{ordinary Emax로 접히는 제한값}}
> $$
>
> - **항별 의미:** 이 식은 sigmoid Emax model이 특정 파라미터 제한을 통해 ordinary Emax model로 축소되는 nested 관계를 정의합니다.
> - **실무 직관:** n을 자유롭게 추정하면 sigmoidicity를 허용하고, n=1로 고정하면 일반 Emax 형태가 됩니다. F-test 적용 가능성을 판단하게 합니다.
> - **오해 방지:** 파라미터 수가 하나 더 많다는 이유만으로 nested가 되는 것은 아닙니다. 한 모델이 다른 모델의 제한 형태여야 합니다.
- **무효(Invalid)**: ordinary Emax vs linear response. $C\ll EC_{50}$라는 제한 상황에서만 근사적으로 연결될 뿐, 일반적으로 중첩 비교(nested comparison)가 아닙니다. [p.388]

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{C}_{\text{농도}}\ll\underbrace{EC_{50}}_{\text{반최대효과 농도}}
> $$
>
> - **항별 의미:** 이 부등식은 농도가 EC50보다 충분히 낮은 특수 근사 영역을 뜻하며, 일반적 nested 관계를 정의하는 등식 제한이 아닙니다.
> - **실무 직관:** C가 EC50보다 훨씬 작으면 Emax식이 국소적으로 거의 선형처럼 보일 수 있습니다. 그러나 이는 제한 상황의 근사일 뿐 모델 비교 조건이 아닙니다.
> - **오해 방지:** 근사적으로 닮았다는 것과 nested라는 것은 다릅니다. 이 혼동이 F-test 오용의 핵심입니다.
- **조건부 유효(Conditionally valid)**: hepatic distributed model과 parallel-tube model은 축소 관계(reduced relation)가 성립하는 경우 F-test를 사용할 수 있습니다. [pp.388–389]
- **이중 위반으로 무효(Invalid with double violation)**: Table 4.8의 Michaelis–Menten weighted fit과 first-order unweighted fit은 비중첩(non-nested)이고 weighting도 달라 F-test도 AIC도 사용할 수 없습니다. [p.389]

#### C. 구조적 필연성(Structural Necessity)

<!-- ANCHOR -->
중첩(nested) 조건은 파라미터 개수 차이가 아니라 **한 모델이 다른 모델의 제한된 형태인가**의 문제입니다. `[교과서 외 해석]` 기하학적으로 말하면 축소 모델(reduced model)은 전체 모델 파라미터 공간(full model parameter space) 안의 제한된 부분공간이어야 합니다. 그래야 WRSS 감소량이 "추가 파라미터(parameter)가 설명한 개선"으로 해석됩니다.

#### C-2. 그럴듯한 오류(Plausible Fallacy)

**오류(Fallacy)**: "WRSS가 더 낮고 파라미터(parameter)가 하나 더 많으니 F-test를 쓰면 된다."  
**교정(Correction)**: WRSS 감소량은 같은 오차/가중치 모델(error/weighting model)과 중첩(nested) 구조 안에서만 F 분포와 연결됩니다. 비중첩(non-nested) 구조에서는 두 WRSS가 같은 검정 좌표계 위에 있지 않습니다. [pp.387–389]

<!-- SLIDE_START: S23 | title: AIC/SC와 likelihood 비교 경계 | source_anchor: MUST 3 D/E -->
> **핵심 메시지:** AIC/SC는 nested를 요구하지 않지만 같은 weighting 좌표 위의 모델만 비교할 수 있습니다.

#### D. AIC/SC 적용 경계(AIC/SC boundary)

AIC와 SC는 중첩 모델(nested model)을 요구하지 않지만, 동일 가중치(equal weighting)는 요구합니다. [p.389]

$$AIC=N_{obs}\ln(WRSS)+2N_{par}\quad [\text{Eq.4:56},\ p.389]$$

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{AIC}_{\text{Akaike 정보기준}}=\underbrace{N_{obs}\ln(WRSS)}_{\text{불일치 항}}+\underbrace{2N_{par}}_{\text{복잡도 벌점}} \quad [\text{Eq.4:56},\ p.389]
> $$
>
> - **항별 의미:** 좌변은 모델의 상대적 정보기준을 정의하고, 우변은 WRSS 기반 불일치 항에 파라미터 수 벌점을 더합니다.
> - **실무 직관:** WRSS가 낮아지면 AIC는 낮아지지만, Npar가 늘면 벌점이 증가합니다. nested가 아니어도 같은 weighting 조건에서는 후보 모델 비교에 쓸 수 있습니다.
> - **오해 방지:** AIC 최저값은 adequate model의 자동 인증이 아닙니다. 잔차, parameter precision, 생물학적 타당성과 함께 읽어야 합니다.

$$SC=N_{obs}\ln(WRSS)+N_{par}\ln(N_{obs})\quad [\text{Eq.4:57},\ p.389]$$

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{SC}_{\text{Schwarz/Bayesian 정보기준}}=\underbrace{N_{obs}\ln(WRSS)}_{\text{불일치 항}}+\underbrace{N_{par}\ln(N_{obs})}_{\text{표본수 의존 복잡도 벌점}} \quad [\text{Eq.4:57},\ p.389]
> $$
>
> - **항별 의미:** 좌변은 Schwarz criterion을 정의하고, 우변은 WRSS 기반 불일치에 표본수 로그가 반영된 파라미터 벌점을 더합니다.
> - **실무 직관:** WRSS가 낮아지면 SC는 낮아지고, 파라미터 수가 많거나 Nobs가 클수록 벌점이 커집니다. 더 보수적인 모델 선택 판단을 지원합니다.
> - **오해 방지:** AIC/SC는 nested 조건은 요구하지 않지만 같은 weighting 조건은 요구합니다. weighting이 다르면 비교 좌표가 달라집니다.

AIC/SC의 최저값(lowest value)이 자동으로 적절한 모델(adequate model)을 뜻하지는 않습니다. GOF, 즉 모델 적절성(model adequacy)의 종합 진단은 잔차(residuals), 파라미터 정밀도(parameter precision), 정확도(accuracy), 상관행렬(correlation matrix), 조건수(condition number), F-test, AIC/SC를 함께 보는 복합 진단 도구군(battery of tools)입니다. <!-- ANNOTATION --> [pp.387–391]

#### E. WRSS vs $-2\cdot\log likelihood$

원문은 역사적 WRSS 기반 프로그램(historical WRSS-based program)과 현대적 $-2\cdot\log likelihood$ 기반 프로그램(modern $-2\cdot\log likelihood$-based program)을 구분하되, 비교 원리는 동일하게 모델 적절성 기준(model adequacy criteria)과 연결된다고 설명합니다. [p.386] `[교과서 외 구현 번역]` NONMEM의 OFV 비교로 번역할 수는 있지만, $\Delta$OFV threshold나 SCM rule은 이 PDF의 직접 내용이 아닙니다.

<!-- SLIDE_START: S24 | title: MUST 3 recap과 practice | source_anchor: MUST 3 Recap -->
> **핵심 메시지:** 모델 비교 전 nested와 weighting을 먼저 확인하면 통계량 오용의 대부분을 차단할 수 있습니다.

<!-- RECAP -->
**MUST 3 요약(Recap)**: F-test는 중첩(nested) + 동일 가중치(equal weighting)일 때만 씁니다. AIC/SC는 nested를 요구하지 않지만 equal weighting을 요구합니다. 어느 경우든 잔차(residual)와 생물학적 타당성(biology)을 대체하지는 못합니다.

> **체화 꿀팁 — [CRUCIBLE_DERIVED]**  
> 두 모델의 통계량을 비교하기 전에 두 질문을 먼저 적으세요: **(1) 한 모델이 다른 모델의 부분집합인가(nested)? (2) 두 모델이 같은 가중치(weighting)로 적합(fit)되었는가?** 둘 다 YES이면 F-test가 작동합니다. weighting만 같으면 AIC/SC만 작동합니다. 둘 다 NO이면 통계 검정 없이 잔차·메커니즘·외부 데이터로 삼각검증(triangulate)해야 합니다. 이 두 질문을 비교 전 루틴(routine)으로 만들면 Table 4.8 같은 이중 위반은 자동으로 차단됩니다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.389, Table 4.8, Michaelis–Menten weighted fit vs first-order unweighted fit 비교.
Why this matters: Table 4.8은 모델 구조와 가중치(weighting)가 모두 다를 때 F-test와 AIC가 모두 무효가 될 수 있음을 보여 주는 원전의 압축 예시입니다. 이 표는 Apex rule을 실제 판정 규칙으로 바꾸어 줍니다.
When to look: MUST 3 요약(Recap)을 읽은 뒤 확인하시면 됩니다.
Learner instruction: 두 위반을 따로 식별하세요: 비중첩(non-nested) 모델 구조와 서로 다른 가중치(different weighting)입니다. 이를 "모델이 다르다"는 모호한 문장 하나로 합치지 마세요.
<!-- /FIGURE_POINTER -->

> **판단 렌즈(Judgment Lens) — [CRUCIBLE_DERIVED]**  
> 중첩(nested) 조건은 단순히 파라미터(parameter) 수가 다른 관계가 아니라, 두 모델이 같은 비교 좌표계 위에 놓여 있다는 조건입니다. 이 조건이 없으면 WRSS 감소량은 "추가 parameter의 기여"가 아니라 서로 다른 문제에서 나온 두 숫자의 차이가 됩니다.

> **▶ 실무 체화 요약 (Practice Brief) — MUST 3 체화 4축 — [EXPERT_INFERENCE, v3.3]**
> - **왜 알아야 하는가**: F-test는 **nested + equal weighting** 두 조건에서만 유효(valid)합니다. 이 두 조건을 무시하고 비중첩(non-nested) 모델 비교나 서로 다른 가중치(different weighting) 비교에 F-test를 적용하면 통계적 결론 자체가 무의미해지며, 모델 판별의 정량적 근거가 무너집니다(Table 4.8의 이중 위반이 정확히 이 사례입니다).
> - **흐름상 역할**: 본 세션의 핵심 개념(Apex Concept)입니다. MUST 2의 잔차 진단을 통과한 모델 후보들 사이의 정량 비교 단계이며, §5 혼동쌍 #1(nested+equal vs non-nested 또는 different weighting)의 직접 모태입니다.
> - **체화 꿀팁**: "Nested + Equal Weighting" 두 조건을 만트라(mantra)처럼 고정하세요. 본문 F-test critical value·자유도(degrees of freedom)와 함께 "non-nested에는 AIC, weighting 다르면 F-test도 AIC도 불가"라는 분기 규칙을 카드 끝에서 자문(self-quiz)하시면 됩니다.
> - **실무 활용**: 모델 비교 보고서에서 F-test를 사용하기 전에 두 모델이 중첩(nested) 관계인지·잔차 가중치(weighting)가 동일한지를 본문에 명시 검증한 후에만 $\Delta$OFV 또는 F-statistic을 인용합니다.

---

<!-- SLIDE_START: S25 | title: MUST 4 — precision vs fit | source_anchor: MUST 4 -->
> **핵심 메시지:** 좋은 fit은 좋은 parameter를 보장하지 않으며, precision은 모델보다 sampling design이 만듭니다.

### ▣ MUST 4 — 파라미터 정밀도와 상관(Parameter Precision & Correlation)

<!-- MASTER LENS -->
**핵심 아이디어(Big Idea)**: 좋은 적합(fit)은 좋은 파라미터(parameter)를 보장하지 않습니다. 파라미터 정밀도(parameter precision)와 상관(correlation)은 모델 자체보다 **샘플링 설계(sampling design)가 파라미터를 서로 분리해 보여 주었는가**에 좌우됩니다. 즉, 같은 식이라도 잘못 찍은 시간점에서는 파라미터들이 서로 구별되지 않습니다. [pp.380–385]

#### A. 정확도(Accuracy), 정밀도(Precision), CV%

정확도(accuracy)는 편향(bias)과 관련되고, 정밀도(precision)는 추정값(estimate)의 불확실성(uncertainty)과 관련됩니다. 즉, 평균적으로 맞는가와 반복하면 얼마나 좁게 모이는가는 다른 질문입니다. 원문은 다트 과녁(dartboard) 비유를 통해 정확/부정확(accurate/inaccurate)과 정밀/부정밀(precise/imprecise)을 구분합니다. [pp.379–380]

$$CV\%=\frac{SE(\hat p)}{\hat p}\cdot100\quad [\text{Eq.4:52},\ p.380]$$

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{CV\%}_{\text{상대 표준오차}}=\frac{\overbrace{SE(\hat p)}^{\text{추정값의 표준오차}}}{\underbrace{\hat p}_{\text{parameter 추정값}}}\cdot100 \quad [\text{Eq.4:52},\ p.380]
> $$
>
> - **항별 의미:** 좌변은 파라미터 추정값의 상대적 정밀도를 백분율로 정의하고, 우변은 표준오차를 추정값으로 나누어 계산합니다.
> - **실무 직관:** SE가 커지면 CV%는 커지고, 같은 SE라도 추정값이 작으면 CV%는 커집니다. 파라미터 신뢰성과 식별가능성을 점검하는 첫 수치입니다.
> - **오해 방지:** CV%를 단독 기각 기준처럼 쓰면 안 됩니다. 상관행렬, 잔차, sampling design과 함께 해석해야 합니다.

$p=0.01\pm0.005\ h^{-1}$의 CV 50% 예시는 "높은 불확실성(uncertainty)"을 보여주는 예시일 뿐, PDF가 정의한 기각 기준(PDF-defined rejection threshold)이 아닙니다. [p.380]

<!-- SLIDE_START: S26 | title: r은 GOF가 아니다 | source_anchor: MUST 4 B -->
> **핵심 메시지:** 높은 r은 말단부 편향과 잔차 run을 숨길 수 있으므로 GOF의 주연이 될 수 없습니다.

#### B. 상관계수 r은 GOF가 아닙니다(Correlation coefficient r is not GOF)

PDF는 상관계수(correlation coefficient)가 가장 많이 오용되는 GOF 기준 중 하나라고 설명합니다. Eq.4:53은 원문 표기를 보존합니다. [p.381]

$$r=1-\frac{\sum(C_i-\hat C_i)^2}{\sum(C_i-\bar C)^2}\quad [\text{Eq.4:53 source form},\ p.381]$$

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{r}_{\text{원문 표기의 상관/설명 지표}}=1-\frac{\overbrace{\sum(C_i-\hat C_i)^2}^{\text{모델 잔차제곱합}}}{\underbrace{\sum(C_i-\bar C)^2}_{\text{평균 대비 총변동}}} \quad [\text{Eq.4:53 source form},\ p.381]
> $$
>
> - **항별 의미:** 좌변은 원문에서 r로 표기된 GOF 보조 지표이고, 우변은 잔차제곱합이 총변동에 비해 얼마나 작은지를 나타냅니다.
> - **실무 직관:** 잔차제곱합이 작아지면 값은 1에 가까워집니다. 그러나 값이 높아도 시간 순서의 편향이나 말단부 systematic error는 숨을 수 있습니다.
> - **오해 방지:** 이 값을 Pearson correlation처럼 단독 GOF 판정으로 쓰면 안 됩니다. 원문 표기를 보존하되, 잔차 도표와 함께 읽어야 합니다.
>
> **검토 메모:** 이 수식은 원문 표기상 r로 표시되어 있지만 문맥상 잔차제곱합/총변동 기반 GOF 보조량으로 읽는 것이 자연스럽습니다. 단, 원문 보존 원칙에 따라 원 수식은 수정하지 않았습니다.

Fig.4.53에서 OLS fit은 $r=0.96$이지만 마지막 세 관측치를 계통적으로 과소예측(systematically underestimate)하고, IRLS fit은 $r=0.94$이지만 전체적으로 더 나은 적합(fit)을 보입니다. 따라서 높은 $r$은 좋은 fit의 충분조건이 아닙니다. [p.382]

<!-- CONFUSION -->
`[교과서 외 해석]` 동적 범위(dynamic range)가 넓은 농도-시간 자료(concentration–time data)에서는 $r$이 모델의 잔차 구조보다 전체 값의 범위에 강하게 끌릴 수 있습니다. 그래서 $r$은 잔차 도표(residual plot)와 함께 읽어야지, 단독 GOF 판정 기준으로 쓰면 안 됩니다.

<!-- SLIDE_START: S27 | title: Parameter correlation과 ridge | source_anchor: MUST 4 C/D/E -->
> **핵심 메시지:** 능선형 최솟값에서는 점추정값이 그럴듯해도 결합 불확실성이 크게 남아 parameter가 분리되지 않습니다.

#### C. 파라미터 상관과 능선 기하(Parameter correlation and ridge geometry)

파라미터 상관행렬(parameter correlation matrix)은 파라미터들이 독립적으로 추정(estimate)되는지, 또는 서로 trade-off하는지를 보여 줍니다. 원문은 높은 상관(high correlation)이 더 적은 파라미터(fewer parameters) 또는 더 많은 데이터(more data)의 필요성을 시사한다고 설명합니다. [pp.382–383]

<!-- ANCHOR -->
Fig.4.55–4.57의 핵심은 **능선형 최솟값(ridge minimum)**, 즉 길게 늘어진 최솟값 영역입니다. <!-- ANNOTATION --> 두 파라미터(parameter)가 능선(ridge) 위에서 같이 움직이면 OFV/WRSS가 거의 변하지 않습니다. 이 때문에 단변량 추정값(univariate estimate)은 그럴듯해도 결합 불확실성(joint uncertainty)은 큽니다. Design A/B 비교는 같은 모델도 샘플링 설계(sampling design)에 따라 $Cl/V$ 또는 $IC_{50}/I_{max}$ 상관이 크게 달라짐을 보여 줍니다. [pp.383–385]

#### D. 한 파라미터 고정(Fixing one parameter)

Fig.4.55는 한 파라미터(parameter)를 고정하면 다른 파라미터의 신뢰구간(confidence interval)이 작아질 수 있음을 보여 줍니다. [pp.383–384] 그러나 `[교과서 외 실무 해석]` 고정(fix) 전략은 정당화 부담을 통계에서 생물학/문헌/선행 연구(biology/literature/prior study)로 옮깁니다. 따라서 고정값(fix value)의 출처와 적용 가능성을 설명하지 못하면, 정밀도(precision)가 좋아진 것이 아니라 불확실성(uncertainty)을 숨긴 것입니다.

#### E. 한계(Limitations)

높은 상관(high correlation)에 대한 보편적 기준(universal cutoff)은 PDF에 없습니다. $|r|>0.95$ 같은 고정 기준(hard threshold) 대신, 상관행렬(correlation matrix), 신뢰 타원(confidence ellipse), 잔차 패턴(residual pattern), 설계 적절성(design adequacy)을 함께 읽어야 합니다. `[교과서 외 구현 번역]` 조건수(condition number)나 covariance-step warning은 현대 구현에서 유용한 신호지만, 이 PDF의 직접 교육 포인트(teaching point)는 "상관(correlation)은 설계(design)의 결과"라는 점입니다.

<!-- SLIDE_START: S28 | title: MUST 4 recap과 practice | source_anchor: MUST 4 Recap -->
> **핵심 메시지:** 상관행렬을 overlay 옆에 놓고 보아야 fit이 좋은 모델과 식별 가능한 모델을 구분할 수 있습니다.

<!-- RECAP -->
**MUST 4 요약(Recap)**: 적합(fit)이 좋아 보여도 파라미터(parameter)가 식별되지 않을 수 있습니다. 정밀도(precision)는 모델이 아니라 설계가 만듭니다.

> **체화 꿀팁 — [CRUCIBLE_DERIVED]**  
> 적합(fit)이 끝나면 항상 두 가지를 동시에 봅니다: 관측/예측 중첩(observed/predicted overlay)과 파라미터 상관행렬(parameter correlation matrix)입니다. Overlay가 좋아 보여도 두 파라미터(parameter)가 강하게 짝지어 움직이면(소스는 보편적 cutoff을 정의하지 않는다는 점에 유의), 그 둘은 사실상 하나의 변형으로 작동합니다. 이때 처방은 모델 단순화가 아니라 다음 코호트(cohort)의 샘플링 설계(sampling design) 변경입니다. "fit이 좋다 → parameter가 좋다"라는 자동 연결을 의식적으로 끊는 것이 이 카드의 체화 핵심입니다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.382, Fig.4.53; pp.383–385, Fig.4.55–4.57.
Why this matters: Fig.4.53은 더 높은 $r$이 있어도 계통적인 말단부 편향(systematic terminal bias)이 숨을 수 있음을 보여 줍니다. 이어서 Fig.4.55–4.57은 그럴듯한 적합(fit)이라도 상관된 파라미터가 제대로 식별되지 않을 수 있음을 보여 줍니다.
When to look: MUST 4 요약(Recap)을 읽은 뒤, §5 혼동쌍으로 넘어가기 전에 확인하시면 됩니다.
Learner instruction: 먼저 $r=0.96$과 $r=0.94$를 비교하면서 어느 적합(fit)이 구조적으로 더 나은지 질문해 보세요. 그다음 신뢰 타원(confidence ellipses)과 설계 비교(design comparison)를 확인하면서 해당 파라미터 쌍이 정말 식별 가능한지 질문하시면 됩니다.
<!-- /FIGURE_POINTER -->

> **체화 노트(Mastery Note) — [CRUCIBLE_DERIVED]**  
> 능선형 최솟값(ridge minimum)을 떠올리면 파라미터 상관(parameter correlation)의 의미가 분명해집니다. 능선 위 여러 지점이 거의 같은 WRSS를 주기 때문에, 추정값(estimate) 하나가 그럴듯해도 결합 불확실성(joint uncertainty)은 크게 남을 수 있습니다.

> **▶ 실무 체화 요약 (Practice Brief) — MUST 4 체화 4축 — [EXPERT_INFERENCE, v3.3]**
> - **왜 알아야 하는가**: 정밀도(precision, CV%/SE)와 파라미터 간 상관(correlation)을 동시에 보지 않으면 점추정값(point estimate)의 신뢰성이 식별가능성(identifiability) 위에 있는지 알 수 없습니다. 능선형 최솟값(ridge minimum) 위에 놓인 파라미터 쌍을 놓치면 NONMEM 출력의 숫자가 데이터가 식별할 수 없는 양(quantity)을 추정한 가짜 결과일 수 있습니다.
> - **흐름상 역할**: $COV step 출력 해석의 척추(spine)입니다. MUST 3 F-test 통과 모델의 후속 검증 단계이며, MUST 5 샘플링 설계(sampling design)로 곧장 연결되는 진단(상관 높음 → 다음 cohort design 변경)입니다.
> - **체화 꿀팁**: NONMEM 출력 표를 받으면 파라미터 정밀도(SE/CV%) 칸과 상관행렬(correlation matrix)을 *동시에* 한 화면에 띄우세요. "fit이 좋다 → parameter가 좋다"라는 자동 추론을 끊고 두 신호를 30초 안에 교차 스캔하는 루틴을 정착시키면 됩니다(소스가 보편적 cutoff을 정의하지 않는다는 점에 유의).
> - **실무 활용**: PopPK 보고서에서 모든 파라미터에 점추정값 + SE/CV% + 주요 상관(correlation)을 함께 표기하고, 상관이 높은 파라미터 쌍에는 모델 단순화가 아니라 **다음 cohort sampling design 변경**을 권고로 명시합니다.

---

<!-- SLIDE_START: S29 | title: MUST 5 — derivative sampling | source_anchor: MUST 5 -->
> **핵심 메시지:** 편미분 peak는 어떤 시간·농도 영역에서 특정 파라미터가 가장 잘 보이는지를 알려주는 sampling 좌표입니다.

### ▣ MUST 5 — 편미분 기반 최적 샘플링(Partial-Derivative Optimal Sampling)

<!-- MASTER LENS -->
**핵심 아이디어(Big Idea)**: 편미분 도표(partial derivative plot), 즉 파라미터 변화에 대한 예측 변화율 그림은 "어디서 샘플링(sample)하면 어떤 파라미터(parameter)가 가장 잘 보이는가"를 말해 줍니다. <!-- ANNOTATION --> 예측값이 파라미터 변화에 민감한 시간·농도 영역이 그 파라미터를 추정(estimate)하는 정보의 중심입니다. [pp.399–403]

#### A. 이중지수 편미분 설계(Bi-exponential derivative design)

원문은 이중지수 모델(bi-exponential model)을 예로 듭니다. [p.399]

$$C=Ae^{-\alpha t}+Be^{-\beta t}\quad [\text{Eq.5:7},\ p.399]$$

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{C}_{\text{총 농도}}=\overbrace{\underbrace{A}_{\text{빠른 성분 절편}}e^{-\underbrace{\alpha}_{\text{빠른 소실 기울기}}t}}^{\text{초기 정보 성분}}+\overbrace{\underbrace{B}_{\text{느린 성분 절편}}e^{-\underbrace{\beta}_{\text{느린 소실 기울기}}t}}^{\text{말단 정보 성분}} \quad [\text{Eq.5:7},\ p.399]
> $$
>
> - **항별 의미:** 좌변은 이중지수 모델의 시간별 농도 예측값이고, 우변은 빠른 성분과 느린 성분의 합입니다.
> - **실무 직관:** 각 파라미터를 조금 바꿨을 때 C가 크게 변하는 시간대가 해당 파라미터를 잘 추정할 수 있는 sampling 위치입니다.
> - **오해 방지:** Eq.4:21과 같은 형태라도 여기서는 curve stripping보다 sampling information을 읽기 위한 민감도 기반 설계식으로 쓰입니다.

$A$와 $B$에 대한 편미분(derivatives)은 절편(intercept) 영역에서, $\alpha$와 $\beta$에 대한 편미분은 각각 $t=1/\alpha$, $t=1/\beta$에서 극값을 갖습니다. [pp.399–400]

$$t=\frac{1}{\alpha},\qquad t=\frac{1}{\beta}\quad [\text{Eq.5:11},\ p.400]$$

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{t}_{\text{최대 민감도 시간}}=\frac{1}{\underbrace{\alpha}_{\text{빠른 기울기}}},\qquad \underbrace{t}_{\text{최대 민감도 시간}}=\frac{1}{\underbrace{\beta}_{\text{느린 기울기}}} \quad [\text{Eq.5:11},\ p.400]
> $$
>
> - **항별 의미:** 좌변은 각 기울기 파라미터에 대해 정보가 커지는 시간 anchor를 뜻하고, 우변은 각 지수 기울기의 역수입니다.
> - **실무 직관:** alpha나 beta가 커지면 1/alpha 또는 1/beta는 작아져 최적 sampling 시간은 앞쪽으로 이동합니다. sampling design을 시간점으로 번역하게 해 줍니다.
> - **오해 방지:** 이 시간점만 찍으면 안 됩니다. 참 파라미터가 불확실하므로 peak 주변 anchor와 전체 concentration range 보완 샘플이 함께 필요합니다.

예시 파라미터(parameter)가 $\alpha=0.69\ h^{-1}$, $\beta=0.069\ h^{-1}$이면 최적 시간(optimal time)은 약 1.4 h와 14 h입니다. Fig.5.4의 도표 예시(plotted example)에서는 $\alpha$와 $\beta$ 정보가 각각 약 20 min, 300 min 부근에 모입니다. [p.400]

<!-- SLIDE_START: S30 | title: PD derivative design | source_anchor: MUST 5 B/C/D -->
> **핵심 메시지:** Emax·turnover design에서는 효과 수준과 시간대별 sensitivity가 각각 다른 parameter 정보를 담습니다.

#### B. Sigmoid Imax / Emax 설계(design)

Sigmoid Imax model의 편미분(derivatives)은 $IC_{50}$ 정보가 half-maximal effect 부근에, sigmoidicity factor $n$ 정보가 20%와 80% effect level 부근에 집중됨을 보여 줍니다. Fig.5.6은 $E_0$, $n$, $EC_{50}$, $n$, $E_{max}$에 대한 다섯 설계 지점(design points)을 제시합니다. [pp.400–402]

#### C. Turnover model 설계(design)

Turnover response model에서는 $k_{out}$ 민감도(sensitivity)가 25 h와 약 100 h post-dose에서 크고, 초기 시간(early time)에서는 $k_{out}$가 $IC_{50}$ 또는 $n$보다 민감합니다. 따라서 초기 샘플링(early sampling)은 $k_{out}$ 초기 추정값(initial estimate)을 직접 강화합니다. [pp.402–404]

#### D. 구조적 필연성(Structural Necessity)

<!-- ANCHOR -->
편미분이 큰 위치는 예측(prediction)이 해당 파라미터(parameter) 변화에 크게 흔들리는 위치입니다. `[교과서 외 해석]` 이를 가능도 표면(likelihood surface), 즉 파라미터 공간에서 OFV 값이 분포하는 지형의 언어로 바꾸면, 그 위치의 관측치는 해당 파라미터 방향의 표면 곡률(surface curvature)을 키워 최솟값(minimum)을 더 좁고 깊게 만듭니다.

<!-- TRENCH -->
**현장 수준 팁(Trench-Level Tip)**: `[교과서 외 구현 번역]` 파라미터(parameter) 단위가 다르면 원자료(raw) $\partial C/\partial\theta$ 크기 비교가 왜곡될 수 있습니다. 실무에서는 $\theta_i(\partial C/\partial\theta_i)/C$ 같은 정규화 민감도(normalized sensitivity)를 함께 보아 파라미터 간 비교를 안정화합니다.

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{\frac{\theta_i(\partial C/\partial\theta_i)}{C}}_{\text{정규화 민감도}}
> $$
>
> - **항별 의미:** 이 식은 파라미터의 절대 단위 차이를 줄이기 위해 파라미터 변화율에 대한 예측 변화율을 상대 스케일로 표현합니다.
> - **실무 직관:** theta_i 방향으로 예측 C가 크게 흔들릴수록 값의 절댓값이 커집니다. 서로 단위가 다른 파라미터의 sensitivity를 비교할 수 있게 합니다.
> - **오해 방지:** raw derivative의 크기만 비교하면 단위와 scale 때문에 잘못된 sampling 우선순위를 정할 수 있습니다.

<!-- SLIDE_START: S31 | title: MUST 5 boundary와 practice | source_anchor: MUST 5 E/Recap -->
> **핵심 메시지:** Derivative peak는 anchor이지 전부가 아니며, 참 파라미터 불확실성 때문에 전체 range 보완 샘플이 필요합니다.

#### E. 경계 조건(Boundary Conditions)

참 파라미터 값(true parameter values)을 사전에 알 수 없으므로, 편미분 극값(derivative maxima)에만 샘플(sample)을 몰아넣으면 안 됩니다. 전체 농도 범위(concentration range)에도 추가 샘플(samples)을 두어야 합니다. 원문은 pooled data를 무비판적으로 설계 결정(design decision)에 쓰는 위험도 경고합니다. [p.402]

<!-- RECAP -->
**MUST 5 요약(Recap)**: 최적 샘플링은 촘촘히 많이 찍는 것이 아니라, 각 파라미터(parameter)가 가장 크게 보이는 곳을 의도적으로 찍는 것입니다.

> **체화 꿀팁 — [CRUCIBLE_DERIVED]**  
> 다음 코호트 샘플링(cohort sampling)을 정할 때, 각 파라미터(parameter)에 대해 편미분 도표(partial derivative plot)를 그리고 peak 위치를 시간점으로 옮깁니다. 그 시간점들이 설계(design)의 기준점(anchor)이 됩니다. 그러나 anchor에만 sample을 몰아넣지 말고, 전체 농도 범위(concentration range)에 보완 샘플링(sampling)을 함께 두어야 합니다. 참 파라미터(true parameter)는 아직 모르므로 peak 추정은 이동할 수 있습니다. **"정보(information)가 모인 곳에 anchor + 전체 range에 보험"**의 두 층이 이 카드의 체화 골격입니다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, pp.400–402, Fig.5.4–5.6; p.403, Fig.5.8.
Why this matters: 이 그림들은 편미분 peak가 정보성 있는 샘플링 영역(informative sampling regions)을 정의한다는 핵심 시각 근거입니다. 이 도표가 없으면 "민감도(sensitivity)가 높은 곳에서 sample하라"는 규칙이 너무 추상적으로 남습니다.
When to look: MUST 5 요약(Recap)을 읽은 뒤 확인하시면 됩니다.
Learner instruction: 각 편미분 곡선(derivative curve)에서 곡선의 절댓값이 가장 큰 시간 또는 농도 영역을 짚어 보세요. 그 영역을 샘플링 설계 지점(sampling design point)으로 번역하시면 됩니다.
<!-- /FIGURE_POINTER -->

> **실무 렌즈(Practice Lens) — [CRUCIBLE_DERIVED]**  
> 편미분 peak는 "그 파라미터(parameter)가 보이는 시간 또는 농도 영역"을 표시합니다. 다만 참 파라미터(true parameter)가 아직 불확실하므로, peak 주변만 찍는 설계가 아니라 전체 범위(range)를 보존하는 보완 샘플링(sampling)이 함께 필요합니다.

> **▶ 실무 체화 요약 (Practice Brief) — MUST 5 체화 4축 — [EXPERT_INFERENCE, v3.3]**
> - **왜 알아야 하는가**: 채혈 시점(sampling time) 선택이 어떤 파라미터를 식별 가능하게 만드는지 정량화하지 못하면 임상시험 PK 설계(design)가 직관에 의존하게 됩니다. 결과적으로 MUST 4의 정밀도·상관 진단이 설계의 한계로 인해 무너지는 샘플링 식별가능성(sampling identifiability) 함정으로 직결됩니다.
> - **흐름상 역할**: MUST 4의 정밀도 평가를 *사전적*으로 설계하는 자리입니다. 임상시험 PK 채혈 protocol 설계의 정량 근거이며, sparse-data fitting이 가능한 design 입구입니다.
> - **체화 꿀팁**: 본문 편미분 $\partial C/\partial\theta$가 큰 시점이 그 파라미터에 *민감한* 시점이라는 직관을 손으로 1구획 모델에 적용해 $K_a$, $V$, $CL$ 각각의 sensitivity peak 시점을 그려 보세요. "information이 모인 곳에 anchor + 전체 range에 보험"의 두 층 골격으로 design을 잡으면 됩니다.
> - **실무 활용**: DDI 연구 또는 신약 Phase 1 PK study의 채혈 시점을 결정할 때 편미분 sensitivity 분석을 protocol의 정당화 근거로 첨부하여, "왜 이 시점인가"의 답을 통계적·정량적 언어로 제시합니다.

---

<!-- SLIDE_START: S32 | title: MUST 6 — sensitivity analysis | source_anchor: MUST 6 -->
> **핵심 메시지:** 민감도 분석은 fit 후 장식이 아니라 어떤 파라미터 불확실성이 결론을 흔드는지 보는 사전 stress test입니다.

### ▣ MUST 6 — 민감도 분석(Sensitivity Analysis)

<!-- MASTER LENS -->
**핵심 아이디어(Big Idea)**: 민감도 분석(sensitivity analysis), 즉 파라미터 교란(parameter perturbation)의 예측 영향 점검은 적합(fitting) 후 해석이 아닙니다. <!-- ANNOTATION --> 다음 실험을 설계하기 전 "어떤 파라미터 불확실성(parameter uncertainty)이 예측(prediction)을 얼마나 흔드는가"를 보는 사전 점검 절차(pre-fitting stress test)입니다. [pp.403–405]

#### A. 형식적 정의(Formal Definition)

민감도 분석(sensitivity analysis)은 특정 파라미터(parameter)를 일정 비율로 변화시켜 농도-시간(concentration–time) 또는 반응-시간(response–time) 예측(prediction)이 어떻게 달라지는지 보는 절차입니다. 즉, 파라미터 불확실성(parameter uncertainty)이 실제 예측 불확실성(prediction uncertainty)으로 얼마나 번역되는지를 봅니다. 원문의 예시는 파라미터를 +100% 또는 -50%로 변화시켜 모델 출력(model output) 변화를 비교합니다. [pp.404–405]

#### B. PK 민감도 예시(PK sensitivity example)

Michaelis–Menten pharmacokinetic model에서 $V_{max}$, $K_M$, $V_c$, $V_t$를 변화시키면 농도-시간 프로파일(concentration–time profile)의 어느 구간이 어떤 파라미터(parameter)에 민감한지 드러납니다. Fig.5.9는 이것을 향후 샘플링 위치(future sampling location) 결정에 연결합니다. [p.405]

#### C. PD 민감도 예시(PD sensitivity example)

Warfarin-PCA model에서는 $IC_{50}$, $k_{in}$, $k_{out}$, $t_{lag}$의 변화가 반응-시간 프로파일(response-time profile)에 미치는 영향을 비교합니다. Fig.5.10의 목적은 "어떤 파라미터(parameter)를 더 잘 추정(estimate)하려면 어느 구간을 보강해야 하는가"를 읽는 것입니다. [p.405]

<!-- SLIDE_START: S33 | title: Toxicokinetic sensitivity context | source_anchor: MUST 6 D -->
> **핵심 메시지:** 독성동태에서는 비슷한 exposure summary도 capacity-dependent와 time-dependent 과정의 상쇄를 숨길 수 있습니다.

#### D. 독성동태 설계 맥락(Toxicokinetic design context)

독성동태 설계(toxicokinetic design)에서 만성시험(chronic studies)은 보통 노출(exposure) 확인을 위해 $C_{max}$ 샘플링(sampling)만으로 충분한 경우가 있으나, 예외가 있으며 연구자 판단(investigator judgment)이 필요합니다. Table 5.6은 PK/DRF/chronic study type별로 profile 또는 $C_{max}$ 중심 sampling package를 구분합니다. [p.413]

비선형 제거(nonlinear elimination)에서는 농도(concentration)가 일차 선형 동태(first-order linear kinetics) 또는 무시 가능한 수준(negligible level)에 도달할 때까지 샘플링(sampling)하지 않으면 진정한 무한대 외삽 AUC(true extrapolated AUC to infinity)를 얻을 수 없습니다. [p.414]

용량의존 동태(capacity-dependent kinetics)와 시간의존 동태(time-dependent kinetics)가 동시에 존재하면 Day 1 AUC와 정상상태 AUC(steady-state AUC) 비교가 상쇄될 수 있습니다. 이 경우 해석(interpretation)은 흐려집니다. Fig.5.20의 핵심은 노출(exposure)이 변하지 않는 것처럼 보여도 capacity와 induction이 동시에 작동할 수 있다는 점입니다. [p.414]

<!-- TRENCH -->
**현장 수준 팁(Trench-Level Tip)**: 민감도 분석(sensitivity analysis)은 파라미터(parameter)를 "잘 추정했는지"보다 먼저 "잘못 추정하면 어떤 결론이 흔들리는지"를 묻습니다. 흔들리는 결론이 용량(dose), 안전역(safety margin), 샘플링 일정(sampling schedule)이면 다음 실험 설계를 바꿔야 합니다.

<!-- SLIDE_START: S34 | title: MUST 6 recap과 practice | source_anchor: MUST 6 Recap -->
> **핵심 메시지:** 흔들어도 살아남는 결론만 dose, safety margin, sampling schedule 판단으로 보고할 수 있습니다.

<!-- RECAP -->
**MUST 6 요약(Recap)**: 편미분(partial derivative)이 "어디서 정보가 생기는가"를 말한다면, 민감도 분석(sensitivity analysis)은 "정보가 부족하면 결론이 어디서 무너지는가"를 말합니다.

> **체화 꿀팁 — [CRUCIBLE_DERIVED]**  
> 해석을 시작하기 전, 즉 결과로부터 용량(dose), 안전역(safety margin), 샘플링 일정(sampling schedule)을 제안하기 전에 각 파라미터(parameter)를 ±50% 흔들어 그 결론들이 어떻게 변하는지 봅니다. 결론이 거의 같으면 그 파라미터의 정밀도는 충분합니다. 결론이 흔들리면 다음 실험에서 그 영역을 보강합니다. **"흔들어도 살아남는 결론만 보고하라"**가 이 카드의 체화 원칙입니다. Toxicokinetic 영역에서는 capacity-dependent와 time-dependent 과정이 동시에 작동하면 exposure summary가 비슷해 보여도 흔들기에서 두 효과의 역방향 상쇄가 노출되므로, 흔들기는 단일 결론을 검증하는 동시에 가설을 분리하는 도구가 됩니다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.405, Fig.5.10; p.414, Fig.5.20.
Why this matters: Fig.5.10은 파라미터 교란(parameter perturbations)이 반응-시간 프로파일(response-time profiles)을 어떻게 바꾸는지 보여 줍니다. Fig.5.20은 capacity-dependent process와 time-dependent process가 노출 해석(exposure interpretation)에서 서로를 가릴 수 있는 독성동태 함정(toxicokinetic trap)을 보여 줍니다.
When to look: MUST 6 요약(Recap)을 읽은 뒤, §5 혼동쌍으로 넘어가기 전에 확인하시면 됩니다.
Learner instruction: Fig.5.10에서는 각 파라미터(parameter)를 교란했을 때 어느 profile 영역이 움직이는지 확인하세요. Fig.5.20에서는 비슷해 보이는 exposure summary가 왜 두 개의 동시 kinetic process를 숨길 수 있는지에 집중하시면 됩니다.
<!-- /FIGURE_POINTER -->

> **실패 모드(Failure Mode) — [TEXTBOOK_DERIVED]**  
> 독성동태 설계(toxicokinetic design)에서 exposure summary가 비슷해 보여도 capacity-dependent process와 time-dependent process가 서로 상쇄될 수 있습니다. 따라서 민감도 분석(sensitivity analysis)은 수치가 변했는지보다 어떤 결론이 가려질 수 있는지를 묻는 단계입니다.

> **▶ 실무 체화 요약 (Practice Brief) — MUST 6 체화 4축 — [EXPERT_INFERENCE, v3.3]**
> - **왜 알아야 하는가**: 모델 파라미터 중 어느 파라미터가 출력(예측 농도·AUC·response profile)에 민감하고 어느 파라미터가 둔감한지를 모르면 모델의 견고성(robustness)을 평가할 수 없습니다. 규제 제출 시 "이 파라미터의 불확실성이 결론을 바꾸는가"라는 질문에도 답할 수 없습니다.
> - **흐름상 역할**: 본 세션의 종합 출구입니다. MUST 4의 정밀도 평가와 MUST 5의 샘플링 설계(sampling design)를 통합한 위험평가(risk assessment) 자리이며, modeling carousel의 사이클을 다음 실험 design으로 되돌리는 마지막 매듭입니다.
> - **체화 꿀팁**: 본문 민감도 분석 절차(파라미터를 ±50% 또는 +100%·-50%로 변동 → output 변화 측정)를 빈 종이에 한 파라미터에 대해 손으로 적용해 보세요. "민감 vs 둔감"을 한 줄로 분류한 뒤, **"흔들어도 살아남는 결론만 보고하라"** 원칙을 카드의 핵심 행동 규칙으로 고정하면 됩니다(Toxicokinetic 영역에서는 capacity-dependent와 time-dependent 과정이 동시에 작동하면 흔들기에서 두 효과의 역방향 상쇄가 노출됨).
> - **실무 활용**: NDA 또는 IND 제출 dossier에서 핵심 파라미터에 대한 민감도 분석(sensitivity analysis) 결과를 첨부하여, dose·safety margin·sampling schedule 결론을 흔들 수 있는 핵심 파라미터를 모델 risk 항목으로 명시합니다.

---

<!-- SLIDE_START: S35 | title: 혼동쌍 #1 | source_anchor: §5 Confusion Pair #1 -->
> **핵심 메시지:** Nested + equal weighting 조건을 놓치면 F-test와 AIC/SC가 모두 잘못된 비교 언어가 됩니다.

## §5 — 혼동쌍 해부(Confusion Pair Dissection)

### ▣ 혼동쌍 #1 — 중첩 + 동일 가중치(Nested + equal weighting) vs 비중첩 또는 다른 가중치(non-nested 또는 different weighting)

<!-- CONFUSION -->
| 항목 | 올바른 판정 |
|---|---|
| 흔한 오해 | "더 복잡한 모델이 WRSS를 줄이면 F-test를 쓴다." |
| 원전 교정(Source correction) | F-test는 계층적/중첩 모델(hierarchical/nested model)에서만 가능하고, 동일 가중치(equal weighting)가 필요하다. [pp.387–388] |
| AIC/SC 적용 경계(AIC/SC boundary) | AIC/SC는 중첩(nested)을 요구하지 않지만 동일 가중치(equal weighting)는 요구한다. [p.389] |
| 결정적 예(Critical example) | Table 4.8의 Michaelis–Menten weighted model vs first-order unweighted model은 F-test도 AIC도 사용할 수 없다. [p.389] |
| 변화 방향 | 통계 검정 하나로 결론 내리지 말고 잔차 패턴(residual pattern), 기전적 타당성(mechanism plausibility), 외부 근거(external evidence), 시각적 예측(visual prediction)을 삼각검증(triangulate)한다. |
| **치명적 타격(Critical Blow)** *— [교과서 외 실무 해석]* | 이 비교 조건 위반은 그 한 검정의 무효화에서 끝나지 않는다. 잘못된 모델 위에 쌓이는 후속 용량 시뮬레이션(dose simulation), 안전역(safety margin) 계산, 다음 cohort sampling 권고가 모두 같은 오류를 상속하므로, 한 차례의 부주의가 modeling carousel 전체 사이클을 오염시킨다. PDF는 이 워크플로우 전파를 명시하지 않으므로 거장의 실무 해석으로 라벨링한다. |

<!-- TRENCH -->
가중치(weighting) 선택은 관행이 아니라 잔차 패턴(residual pattern)으로 정당화합니다. Fan shape이면 상대오차 가중치(relative error weighting)를 의심합니다. 반대로 잔차 폭이 균질하면 고정 절대오차(constant absolute error)가 더 자연스럽습니다. [pp.373–374]

**기억 고리**: F-test는 "중첩(nested) + 같은 가중치(same weighting)"라는 잠금장치가 맞아야 열립니다. 하나라도 맞지 않으면 낮은 WRSS는 검정 통계량이 아니라 단순한 숫자입니다.

---

<!-- SLIDE_START: S36 | title: 혼동쌍 #2 | source_anchor: §5 Confusion Pair #2 -->
> **핵심 메시지:** r은 데이터 폭의 그림자일 수 있으며, 모델이 어디서 틀렸는지는 잔차의 부호와 순서가 말합니다.

### ▣ 혼동쌍 #2 — 상관계수 r(Correlation coefficient r) vs 진정한 GOF

<!-- CONFUSION -->
| 항목 | 올바른 판정 |
|---|---|
| 흔한 오해 | "r이 높으면 fit이 좋다." |
| 원전 교정(Source correction) | Fig.4.53에서 OLS는 $r=0.96$이지만 terminal observations를 underestimate하고, IRLS는 $r=0.94$이지만 더 나은 pattern을 보인다. [p.382] |
| 왜 위험한가 | $r$은 잔차 부호/연속 패턴(residual sign/run), 분산 패턴(variance pattern), 말단부 편향(terminal bias)을 직접 보여주지 못한다. [pp.381–382] |
| 필요한 증거 | 관측/예측 중첩(observed/predicted overlay) + 잔차 대 시간(residual vs time) + 잔차 대 예측값/농도(residual vs prediction/concentration) + 파라미터 정밀도(parameter precision). |

`[교과서 외 해석]` PK data처럼 $y$-range가 넓으면 $r$은 동적 범위(dynamic range)의 영향을 크게 받을 수 있습니다. 따라서 $r$은 "전체 설명력"의 보조 숫자일 뿐, GOF 판정의 주연이 아닙니다.

**기억 고리 — [CRUCIBLE_DERIVED]**: $r$은 데이터의 농도 폭이 클수록 자동으로 1에 가까워집니다. 즉 $r=0.95$라는 숫자는 모델의 적합도라기보다 데이터의 동적 범위(dynamic range)가 만들어낸 그림자입니다. 모델이 어디서 거짓말하는지는 $r$이 아니라 **잔차의 부호와 순서**에서 보입니다. $r$은 큰 방향을 보고, 잔차는 모델의 거짓말을 봅니다.

---

<!-- SLIDE_START: S37 | title: 혼동쌍 #3 | source_anchor: §5 Confusion Pair #3 -->
> **핵심 메시지:** Banana와 fan shape를 같은 처방으로 다루면 구조 결함과 분산 결함을 서로 바꿔 고치게 됩니다.

### ▣ 혼동쌍 #3 — 구조 모델 오류(Structural model error) vs 분산/가중치 모델 오류(variance/weighting model error)

<!-- CONFUSION -->
| 항목 | 구조 모델 오류(Structural model error) | 분산/가중치 모델 오류(Variance/weighting model error) |
|---|---|---|
| 전형적 잔차(residual) | Banana, U-shape, systematic runs | Fan shape, concentration-dependent spread |
| 원인 | 빠진 compartment, wrong Emax shape, lag-time omission | constant variance 가정 오류, weighting mismatch |
| 처방 | 구조 모델 수정, phase/time-scale 추가 | 오차 모델(error model) 또는 가중치(weighting) 재검토 |
| 원전 anchor 위치(Source anchor) | 잔차 패턴 예시 및 일반 잔차 도표(Residual pattern examples and common residual plots) [pp.372–376] | 가중치 및 오차분포 예시(Weighting and error distribution examples) [pp.373–374] |

<!-- TRENCH -->
두 종류의 오류를 바꿔 처방하면 모델이 더 복잡해지기만 합니다. 예를 들어 fan shape에 compartment를 추가하거나 banana pattern에 weighting만 바꾸면, 문제의 원인은 그대로 남습니다.

**기억 고리**: 모양이 휘면 구조를 의심하고, 폭이 벌어지면 분산(variance)을 의심합니다.

---

<!-- SLIDE_START: S38 | title: 혼동쌍 #4 | source_anchor: §5 Confusion Pair #4 -->
> **핵심 메시지:** 이상치는 삭제 대상이 아니라 원자료 오류와 영향점 여부를 분리해 판단해야 하는 진단 사건입니다.

### ▣ 혼동쌍 #4 — 이상치 A(Outlier A) vs 이상치 B(Outlier B)

<!-- CONFUSION -->
| 항목 | 이상치 A(Outlier A) | 이상치 B(Outlier B) |
|---|---|---|
| 원전 서술(Source description) | 참 곡선에서의 수직 이탈(Vertical deviation from true curve) | 높은 영향력을 가진 시간축 이탈(Time-axis deviation with high leverage) |
| 영향 | 정밀도(precision) 감소 | 편향(bias)을 만들면서 precision이 좋아 보일 수 있음 |
| 위험 | 잡음점(noisy point)으로 보임 | 잘못된 곡선(curve)을 강하게 끌고 감 |
| 원전 anchor 위치(Source anchor) | Fig.4.59 [p.390] | Fig.4.59 [p.390] |

원문은 table만 보면 A와 B의 이탈점(deviating points)을 거의 알아보기 어렵다고 강조합니다. 따라서 이상치(outlier) 판단에서는 그래픽 제시(graphical presentation)가 매우 중요합니다. [p.390]

`[교과서 외 통계 도구]` Cook's distance나 hat matrix는 현대 회귀 진단에서 유용하지만, 이 PDF의 핵심은 먼저 plot에서 영향력(leverage)과 수직 이탈(vertical deviation)을 구분하는 것입니다.

**기억 고리**: A는 위아래로 튄 점이고, B는 시간을 잘못 말하는 점입니다. B가 더 위험한 이유는 곡선(curve)의 방향을 바꾸기 때문입니다.

---

<!-- SLIDE_START: S39 | title: Self-Test Q1–Q4 | source_anchor: §7 Q1-Q4 -->
> **핵심 메시지:** 초반 self-test는 초기값, curve stripping, 잔차 패턴을 본문 없이 회상할 수 있는지 확인합니다.

## §7 — 자기 점검: 능동 회상 모듈(Self-Test: Active Recall Module)

### Q1. [회상 ★★]

<!-- SELF-TEST -->
**문제**: 초기값이 부실할 때 Gabrielsson이 명시한 세 가지 위험은 무엇인가? [p.353]

**정답**: 잘못된 최종 추정값(wrong final values), 원치 않는 국소 최솟값(unwanted local minima), 생리학적으로 불가능한 파라미터 값(physiologically impossible parameter values)입니다. 초기값은 비선형 회귀(nonlinear regression)에서 단순한 편의값이 아니라, 알고리즘(algorithm)이 어떤 분지(basin)로 들어갈지 결정하는 EDA 산출물입니다.

---

### Q2. [계산 ★★]

<!-- SELF-TEST -->
**문제**: 10 mg IV bolus 예시에서 반로그 기울기(semi-log slope)가 $-0.01\ \text{min}^{-1}$일 때 $t_{1/2}$, AUC, Cl, V의 source anchor 값을 쓰세요. [p.354]

**정답**: $t_{1/2}\approx65\ \text{min}$, $AUC=100{,}000\ \mu g\cdot L^{-1}\cdot\text{min}$, $Cl=0.1\ L\cdot\text{min}^{-1}$, $V=10\ L$입니다. [Eq.4:17–4:20]

---

### Q3. [회상 ★]

<!-- SELF-TEST -->
**문제**: 이중지수 곡선 분리(bi-exponential curve stripping)에서 말단상(terminal phase)을 먼저 읽는 이유는 무엇인가요? [pp.354–355]

**정답**: 말단상(terminal phase)에서는 빠른 지수항(exponential term) $Ae^{-\alpha t}$가 거의 사라지고 $Be^{-\beta t}$가 지배합니다. 따라서 $B$와 $\beta$를 먼저 얻은 뒤 이를 후방 외삽(back-extrapolate)하여 초기상(initial phase)에서 빼면 $A$와 $\alpha$를 얻을 수 있습니다.

---

### Q4. [진단 ★★]

<!-- SELF-TEST -->
**문제**: 잔차 도표(residual plot)에서 banana pattern과 fan shape가 각각 시사하는 문제는 무엇인가요? [pp.372–376]

**정답**: Banana/U-shape는 구조적 시간 스케일(structural time-scale) 문제, 예를 들어 빠진 지수항(exponential term)이나 잘못된 모델 형태(wrong model shape)를 의심하게 합니다. Fan shape는 농도의존 분산(concentration-dependent variance) 또는 가중치 불일치(weighting mismatch)를 의심하게 합니다.

---

<!-- SLIDE_START: S40 | title: Self-Test Q5–Q9 | source_anchor: §7 Q5-Q9 -->
> **핵심 메시지:** 후반 self-test는 nested 조건, LOF 검정, sampling design, boss dilemma를 실제 판단으로 적용하게 합니다.

### Q5. [핵심 개념(Apex) 적용 ★★]

<!-- SELF-TEST -->
**문제**: Ordinary Emax model과 sigmoid Emax model 비교에는 F-test를 쓸 수 있나요? Linear response model과 ordinary Emax model 비교에는 어떤가요? [p.388]

**정답**: Ordinary Emax vs sigmoid Emax는 sigmoid model에서 $n=1$로 고정하면 ordinary Emax가 되므로 중첩(nested)이고 F-test가 가능합니다. Linear response vs ordinary Emax는 일반적으로 nested가 아니므로 F-test를 쓰면 안 됩니다.

---

### Q6. [판정 ★★]

<!-- SELF-TEST -->
**문제**: Michaelis–Menten weighted fit과 first-order unweighted fit에서 AIC가 더 낮은 모델을 선택해도 되는가? [p.389]

**정답**: 안 됩니다. Table 4.8은 두 모델이 비중첩(non-nested)이고 weighting도 다르므로 F-test도 AIC도 쓸 수 없음을 보여 줍니다. AIC/SC는 중첩(nested)을 요구하지 않지만 동일 가중치(equal weighting)는 요구합니다.

---

### Q7. [계산/개념 ★★]

<!-- SELF-TEST -->
**문제**: Table 4.7의 residual SS 92.67, pure error SS 23.61, df 25와 21로 계산한 $F_{LOF}$는 무엇이며 어떤 결론인가? [pp.378–379]

**정답**: $F_{LOF}=[(92.67-23.61)/(25-21)]/(23.61/21)=15.35$이고, $F_{crit}=2.76$보다 커서 적합결여(lack-of-fit)가 있습니다. 단, 이 검정은 반복 측정(replicate measurement)이 있어 순수오차(pure error)를 분리할 수 있을 때만 가능합니다.

---

### Q8. [설계 ★★]

<!-- SELF-TEST -->
**문제**: Fig.4.55–4.57에서 design A와 design B가 가르치는 핵심은 무엇인가요? [pp.383–385]

**정답**: 파라미터 상관(parameter correlation)과 신뢰 타원(confidence ellipse)은 모델 방정식(model equation)만의 문제가 아니라 샘플링 설계(sampling design)의 결과입니다. 좋은 설계(design)는 두 파라미터(parameter)가 서로 trade-off하지 않도록 정보 영역을 분리해 신뢰구간(confidence interval)과 상관(correlation)을 줄입니다.

---

### Q9. [보스 딜레마(Boss Dilemma) ★★]

<!-- SELF-TEST -->
**문제**: 두 경쟁 모델(competing model)이 있습니다. 하나는 더 낮은 WRSS(lower WRSS)를 보이지만 다른 가중치(weighting)를 사용했고, 다른 하나는 기전적으로 타당(mechanistically plausible)하지만 AIC 차이가 작습니다. 어떤 결정을 내려야 하나요?

**정답**: 먼저 같은 가중치(weighting)로 재적합해 비교 가능성을 확보합니다. 그래도 F-test/AIC가 단독 결론을 주지 못하면 잔차 패턴(residual pattern), 기전적 타당성(mechanism plausibility), 외부 데이터(external data), 시각적 예측(visual prediction)을 함께 삼각검증(triangulate)합니다. PDF는 AIC 차이 기준값(AIC difference threshold)을 정의하지 않습니다. 따라서 낮은 AIC 하나만으로 기전적 타당성(mechanistic plausibility)을 이길 수 없습니다. [p.389, p.391]

---

<!-- SLIDE_START: S41 | title: Meta-frame synthesis | source_anchor: §8 A-C -->
> **핵심 메시지:** 이 세션의 전문성은 모델을 맞추는 손기술이 아니라 비교 조건과 설계 피드백을 통제하는 판단력입니다.

## §8 — 메타 프레임과 큰 그림(Meta-Frame & Big Picture)

### A. 위치 잡기(Positioning)

<!-- MASTER LENS -->
이 세션은 PK/PD 모델링에서 "모델을 세우는 기술"보다 "모델을 버리거나 다시 설계하는 기술"에 가깝습니다. 초기 추정값(initial estimates)은 적합(fit)의 출발점을 정합니다. 잔차(residuals)는 모델 결함을 드러냅니다. F-test/AIC/SC는 비교 조건을 제한합니다. 정밀도/상관(precision/correlation)은 설계의 약점을 노출합니다. 그리고 편미분(partial derivatives)과 민감도 분석(sensitivity analysis)은 다음 실험의 샘플링(sampling)을 바꿉니다. [p.353, pp.369–391, pp.399–405]

`[교과서 외 구현 번역]` 현대 PopPK workflow에서 이 한 사이클의 실무 단위는 단일 run이 아니라 **model/control file 한 버전 + GOF diagnostic plot set + 다음 cohort sampling recommendation**입니다. 세 가지가 함께 닫혀야 modeling carousel이 완주됩니다.

### B. 의존성 사슬(Dependency chain)

1. 초기값이 틀리면 수렴(convergence)이 틀릴 수 있습니다. [p.353]  
2. 잔차(residual)가 계통적(systematic)이면 GOF가 성립하지 않습니다. [pp.369–376]  
3. 비중첩(non-nested) 또는 다른 가중치 비교(different weighting comparison)이면 F-test/AIC가 무력화됩니다. [pp.387–389]  
4. 파라미터 상관(parameter correlation)이 높으면 다음 설계(next design)가 필요합니다. [pp.382–385]  
5. 편미분(partial derivatives)과 민감도 분석(sensitivity analysis)이 그 다음 설계(next design)의 위치를 정합니다. [pp.399–405]

### C. 전문성 해자(Professional moat)

경험 많은 모델러는 "어느 모델의 AIC가 낮은가"만 보지 않습니다. 두 모델이 비슷한 WRSS/AIC를 보이는데 잔차 패턴(residual pattern)과 기전(mechanism)이 모두 애매하면, 어느 한쪽을 고르기 전에 **둘 다 잘못된 기전(wrong mechanism)일 가능성**을 의심합니다. 이 역방향 추론이 모델 선택(model selection)을 파라미터 수 게임(parameter-count game)이 아니라 기전 가설 수정(mechanistic hypothesis revision)으로 바꿉니다.

<!-- SLIDE_START: S42 | title: GOF checklist와 최종 요약 | source_anchor: §8 D-E -->
> **핵심 메시지:** 최종 GOF 판단은 잔차, 정밀도, 상관, 비교조건, 설계 피드백이 모두 통과할 때만 닫힙니다.

### D. Table 4.9에 고정된 GOF 체크리스트(GOF checklist locked from Table 4.9)

<!-- RECAP -->
모델 적합성은 최소한 다음 다섯 질문으로 닫아야 한다. [p.391]

| 체크리스트 질문(Checklist question) | 고정 해석(Locked interpretation) |
|---|---|
| 모델에 생물학적 관련성(biological relevance)이 있는가? | 기전적 타당성(mechanistic plausibility)이 없는 낮은 AIC는 취약하다. |
| 적합된 곡선(fitted curve)이 데이터의 경향(trends in the data)을 재현하는가? | 곡선 중첩(curve overlay)은 첫 관문이다. |
| 파라미터가 충분한 정밀도(adequate precision)로 추정되었는가? | CV%, SE, 신뢰구간(confidence intervals)을 본다. |
| 잔차(residuals)에 계통적 이탈(systematic deviation)이 없는가? | Run, banana, fan, lag-time pattern을 본다. |
| 잔차 도표(residual plots)가 무작위 산포(random scatter)를 보이는가? | 잔차가 무작위가 아니면 모델 또는 가중치(weighting)를 다시 본다. |

### E. 최종 고정 요약(Final locked summary)

<!-- RECAP -->
이 세션의 압축 명제는 다음과 같다.

> **초기값은 알고리즘의 출발점을 정하고, 잔차(residual)는 모델의 거짓말을 드러내며, F-test/AIC는 비교 가능한 모델에서만 의미가 있고, 정밀도/상관(precision/correlation)은 설계의 품질을 말하며, 편미분(partial derivative)과 민감도 분석(sensitivity analysis)은 다음 실험을 어디서 다시 해야 하는지 알려줍니다.**

이 문장을 체화하면 p.352의 모델링 회전고리(modeling carousel)는 단순한 그림이 아니라 실제 워크플로우(workflow)가 됩니다: Explore data에서 초기 추정값(initial estimates)을 만들고, Fit model 후 Analyze output에서 잔차/정밀도/비교(residual/precision/comparison)를 검토하며, 그 결과로 다음 설계(Design)를 수정합니다. [p.352, p.392, pp.399–405]


## PART B — Compiler-Only Appendix

This appendix is not learner-facing. It exists only to protect Phase 5 rendering fidelity and prevent regression. Phase 5 must render PART A only unless explicitly instructed otherwise.

### B1. Compilation Contract

- PART A is the only learner-facing body.
- Phase 5 must render PART A without altering scientific content, equations, source page tags, or markers.
- PART B is instruction/guardrail only and must not be rendered as learner content.
- Do not restore deprecated material from Step 1 Draft v0.
- Do not add new scientific content, new equations, new page tags, new examples, or new figures.
- Do not generate HTML from PART B tables except as internal compiler guidance if explicitly requested.
- **ver2 추가**: Embodiment Tip blocks (체화 꿀팁), Master's One-liner block (거장의 한 줄), 그리고 혼동쌍 #1의 Critical Blow row, 혼동쌍 #2의 강화된 Memory Hook은 모두 PART A의 일부로서 그대로 렌더링한다. 이들은 **새 사실·새 수치·새 그림 마커가 아니라 학습자 체화를 강화하는 거장 시각의 박스 또는 행 추가**이며, 모두 [CRUCIBLE_DERIVED] 또는 [교과서 외 실무 해석] 라벨로 source-boundary 안에 격리되어 있다.
- **v3 추가**: v3 패치는 PART B에만 영향을 주며 PART A 내용을 변경하지 않는다. B12 Change Log와 파일 말미 Final v3 All-Pass Checklist는 compiler-only 메타데이터로, Phase 5 렌더링 대상이 아니다.
- **v3.1 추가**: v3.1 Korean Readability Patch는 PART A 학습자-facing 산문의 한국어 독해성만 개선한다. 모든 수식, 페이지 태그, source label, figure marker, HTML compiler marker, NONMEM/R 코드, 표준 약어, Mastery Augmentation Layer 위치·내용, Phase 5 splice anchor는 그대로 보존된다. PART B는 본 항목과 B12의 v3.1 entry 추가를 제외하면 무변경이다.
- **v3.2 추가**: v3.2 Korean-Dominant Readability Patch는 v3.1 위에서 PART A 학습자-facing 산문의 추가 한국어 정제만 수행한다. career-critical pharmacometrics 용어는 `한글(English)` 병기 형태를 유지한다. v3.1과 동일한 불변 영역(수식, 페이지 태그, source label, figure marker, HTML compiler marker, NONMEM/R 코드, 표준 약어, Mastery Augmentation Layer 위치·내용, Phase 5 splice anchor)은 그대로 보존된다. PART B는 본 항목, Phase 4E Certification 표의 v3.2 row, B10 Micro-Patch Log의 v3.2 entry, B12-B Change Log 신설, 파일 말미 v3.2 Final Checklist 추가를 제외하면 무변경이다.
- **v3.3 추가**: v3.3 Practice-Brief Uniformity Patch는 v3.2 위에서 PART A §2 MUST 1–6 카드 6개에 균일한 4축 실무 체화 요약(Practice Brief) blockquote 추가만 수행한다. 모든 Practice Brief는 라벨 `[EXPERT_INFERENCE, v3.3]`을 가지며, 카드 본문에 이미 존재하는 내용만으로 작성된다. 4축은 (1) 왜 알아야 하는가, (2) 흐름상 역할, (3) 체화 꿀팁, (4) 실무 활용으로 통일된다. 추가 위치는 각 카드의 마지막 Mastery Augmentation 블록(Failure Mode / Mastery Note / Judgment Lens / Practice Lens) 직후, 다음 카드의 `### ▣ MUST [N+1]` 헤더 직전(MUST 6은 `## §5` 직전). v3.2 불변 영역 모두 유지 + v3.3 추가 불변 영역: §2 MUST 1–6 카드의 모든 기존 본문(Big Idea, A–E subsections, Recap, 체화 꿀팁, 모든 Mastery Augmentation 블록, 모든 figure marker), §5 혼동쌍 4개 표 일체, §7 Q1–Q9 정답 방향 일체, §8 Meta-Frame 본문 일체, 특히 §8D **GOF Checklist locked from Table 4.9** 표·MUST 3 [⚡ Apex Concept] 배지·F-test validity conditions 본문 byte-level 보존. PART B는 본 항목, Phase 4E Certification 표의 v3.3 row, B8 v3.3 splice integrity note, B9 C15 row, B10 Micro-Patch Log의 v3.3 entry, B11 Mastery Augmentation Log의 #17–#22 entries, B12-C Change Log 신설, 파일 말미 v3.3 Final Checklist 추가를 제외하면 무변경이다.

### B2. Figure Rendering Instructions

**Image rights**: None. Do not embed copyrighted textbook images. Render `FIGURE_POINTER` as text-only callouts. Render `FIGURE_SCHEMATIC` as newly created, visually distinct teaching schematics according to the marker brief. Do not propose or add figures beyond the approved KEEP list.

#### Approved Figure Inventory

| # | Mode | Source figure/table | Location | Phase 5 rendering decision |
| --- | --- | --- | --- | --- |
| 1 | P | Fig.4.16 p.352 | §1 after Recap | Render as text-only pointer callout; no textbook image. |
| 2 | R | Fig.4.18 p.355 concept | MUST 1 after Recap | Render as distinct schematic; do not reproduce textbook figure. |
| 3 | N | Synthesis from residual figures pp.372–376 | MUST 2 after Recap | Render as new diagnostic triage schematic. |
| 4 | P | Table 4.8 p.389 | MUST 3 after Recap | Render as text-only pointer callout; no table image. |
| 5 | P | Fig.4.53 p.382; Fig.4.55–4.57 pp.383–385 | MUST 4 after Recap | Render as text-only pointer callout. |
| 6 | P | Fig.5.4–5.6 pp.400–402; Fig.5.8 p.403 | MUST 5 after Recap | Render as text-only pointer callout. |
| 7 | P | Fig.5.10 p.405; Fig.5.20 p.414 | MUST 6 after Recap | Render as text-only pointer callout. |

#### Rejected Figure Inventory — Do Not Restore

| # | Source | Decision | Reason |
| --- | --- | --- | --- |
| 8 | Fig.4.21 p.357; Table 4.3 p.360 | REJECT | Budget; lower ROI than Fig.4.18; content already preserved in MUST 1. |
| 9 | Fig.4.59 p.390 | REJECT | Budget; outlier distinction already stated in confusion pair. |
| 10 | Table 4.9 p.391 | REJECT | Redundant with §8 checklist. |

### B3. Page Tag Rendering Rules

- Preserve all `[p.XX]`, `[pp.XX–YY]`, `[pp.XX, YY]`, `[p.확인 필요]`, and `[확인 필요]` tags exactly as present in PART A.
- Render page tags visibly in HTML, preferably as `<span class="source-page">...</span>`.
- Render uncertainty tags with a visible uncertain style.
- Do not fabricate, delete, renumber, or relocate source page tags.
- Do not apply source-page detection inside code blocks or inside raw `FIGURE_*` marker blocks.
- Source page tags must remain visible in print mode.

### B4. HTML Compiler Requirements

#### Core rendering rule

Render content; do not alter it. Produce a single self-contained HTML file with custom CSS and JS inline. External runtime dependencies are allowed only for MathJax CDN, Mermaid CDN, and permitted CDN libraries for code highlighting.

#### Marker-to-component mapping

| Marker / Pattern | HTML component | Mandatory rendering note |
|---|---|---|
| `<!-- MASTER LENS -->` | Callout box | border-left gold; lightly tinted background |
| `<!-- ANNOTATION -->` | Inline abbr/tooltip or small italic annotation | preserve in text flow |
| `<!-- ANCHOR -->` | Bridge sentence | italic muted bridge style |
| `<!-- TRENCH -->` | Practical tip box | rose left border / practical warning |
| `<!-- CONFUSION -->` | Comparison component | side-by-side or table/card with amber styling |
| `<!-- SELF-TEST -->` | Click-to-reveal accordion | answer hidden by default |
| `<!-- RECAP -->` | Section summary box | blue left border |
| `[p.XX]`, `[pp.XX–YY]`, `[pp.XX, YY]` | Source page tag span | visible inline and in print |
| `[p.확인 필요]` / `[확인 필요]` | Uncertainty highlight | retain visibly; do not resolve unless verified |
| `<!-- FIGURE_POINTER -->` | Textbook reference callout | text-only; no image embedding |
| `<!-- FIGURE_SCHEMATIC -->` | Inline schematic figure | render from brief using distinct Mermaid/SVG/CSS, not textbook reproduction |
| `<!-- FIGURE_IMAGE_SLOT -->` | Image/placeholder figure | not used in this session because image rights are None |
| **블록쿼트 `> **거장의 한 줄 — [CRUCIBLE_DERIVED]**`** *(ver2)* | Master's capstone callout | gold-tinted callout, slightly larger type, immediately after §1 Recap; semantically distinct from MASTER LENS Big Idea |
| **블록쿼트 `> **체화 꿀팁 — [CRUCIBLE_DERIVED]**`** *(ver2)* | Embodiment tip callout | teal/green left border or distinct visual treatment from TRENCH; positioned directly after each MUST card's Recap and before the FIGURE marker; consistent styling across MUST 1–6 |
| **혼동쌍 표 행 `**치명적 타격(Critical Blow)** *— [교과서 외 실무 해석]*`** *(ver2, v3 단일화 확인)* | Highlighted row inside CONFUSION table | distinct row background (e.g., subtle red/amber tint) within the existing 혼동쌍 #1 table; not a separate table. *(v3 확인: §5 전체 스캔 결과 혼동쌍 #1 전용 단일 행으로 확인됨 — 혼동쌍 #2, #3, #4에는 Critical Blow 없음. Phase 5는 이 행을 혼동쌍 #1 테이블 안의 단일 강조 행으로만 렌더링한다.)* |
| **블록쿼트 `> **Mastery Note / Failure Mode / Practice Lens / Judgment Lens — [CRUCIBLE_DERIVED\|TEXTBOOK_DERIVED]**`** | Phase 4D mastery augmentation callout | preserve as-is from Phase 4D; existing styling (no change in ver2 or v3) |
| **블록쿼트 `> **▶ 실무 체화 요약 (Practice Brief) — MUST [N] 체화 4축 — [EXPERT_INFERENCE, v3.3]**`** *(v3.3 신설)* | Practice Brief callout | distinct visual treatment dedicated to v3.3 (예: 좌측 보라/인디고 보더 + 옅은 indigo 배경 + 4축 항목을 굵게 구분); §2 MUST 1–6 카드 각각의 마지막 Mastery Augmentation 블록 직후·`---` 직전에 1개씩 위치하며 모두 동일한 4축 구조(왜 알아야 하는가 / 흐름상 역할 / 체화 꿀팁 / 실무 활용)를 가짐. Phase 5는 6개 모든 카드에 동일 스타일을 일관되게 적용해야 함. |


#### Math, code, interaction, and layout

- MathJax: support inline `\(...\)` and display `\[...\]`, plus existing `$$...$$` blocks if present.
- Code: render `<pre><code>` with copy button; preserve code verbatim.
- Navigation: sticky left sidebar table of contents on desktop; collapsed/single-column behavior on mobile.
- Accordion: Self-Test answers must be hidden by default and revealed only on user click.
- Checklist state: if implemented, persist using `sessionStorage` only.
- Controls: include print/PDF button using `window.print()`.
- Responsive: ≤768px single-column; ≥1024px readable two-column or sidebar layout.
- Dark/light: support `prefers-color-scheme`.
- Print: remove unnecessary backgrounds, hide navigation, optimize page breaks, and keep source-page tags visible.

#### Navigation anchor integrity rules

- Use `<a href="#...">` links only in the sidebar.
- Every sidebar target must have a matching body `id`.
- Every major section heading (§1, §2, §5, §7, §8) must receive a stable id.
- Every §2 concept card should receive a stable id when possible.
- `href` values and body ids must match exactly.
- Do not create duplicate ids.
- Enable `html { scroll-behavior: smooth; }`.
- Before finalizing HTML, count sidebar hrefs, confirm each id exists exactly once, and fix all mismatches before output.

#### Figure rendering self-check

- Every `FIGURE_POINTER` becomes a text-only pointer callout with source, why it matters, when to look, and learner instruction.
- Every `FIGURE_SCHEMATIC` becomes a `<figure>` with caption and alt text.
- Do not reproduce the textbook figure's exact layout, color palette, or label placement.
- For Mermaid blocks, use valid directives and safe node IDs only; if the diagram cannot satisfy Mermaid syntax rules, use inline SVG or CSS cards instead.
- Do not emit a Mermaid block likely to fail rendering.

#### Prohibited in Phase 5

- Modifying PART A text, equations, or source page tags.
- Rendering markers as plain text.
- Showing Self-Test answers without interaction.
- Embedding textbook images or exact figure reproductions.
- Adding external local CSS/JS/font/image files not supplied by the user.
- Using `<iframe>` or `<embed>`.
- Creating sidebar links whose targets do not exist or duplicate ids.

### B5. Audit Guardrails

Do not restore the following rejected or unsupported material:

- Deficiency Letter, Major Deficiency, 6-month review extension, NDA Module 5, specific FDA/EMA reviewer quotes, or FDA Guidance claims as if textbook-derived.
- Unsupported cost, market-value, business-delay, or USD claims.
- Unsupported broad claim that "80% of modeling failures" come from these tool misuses.
- Modern implementation details as source facts: NONMEM, CWRES, NPDE, Pirana/xpose, SCM, ΔOFV thresholds, Bayesian TDM, Fisher information matrix, D-optimal/ED-optimal, PFIM, PopED, Sobol, mrgsolve. These may appear only as clearly labeled `[교과서 외 구현 번역]` or `[교과서 외 해석]` if already in PART A.
- Hard cutoffs such as `CV% > 50%` or `|r| > 0.95` as PDF-defined rejection thresholds.
- Incorrect continuous Ch.5 source range `p.399–414`; use the verified split range `p.399–405 / p.412–414` and retain missing pp.406–411.
- Any correction that treats Eq.4:22 or Eq.4:53 as a Draft-vs-PDF mismatch rather than a source-form/source-internal note.
- Unapproved code blocks, unapproved figure embedding, or unapproved figure generation.

### B6. Crucible Guardrails

- Crucible v1 is not a raw prose source at Phase 5.
- Preserve only insights already present in PART A or explicitly inserted as labeled Mastery Augmentation.
- Do not convert `[CRUCIBLE_DERIVED]` or `[EXPERT_INFERENCE]` notes into textbook-derived claims.
- Do not introduce omitted or rejected Crucible expansions such as VPC/PPC/NPDE expansion, additional cards, or new external optimal-design frameworks.

### B7. Deprecated and Forbidden Restorations

- Step 1 Draft v0 is deprecated.
- Do not restore rejected overclaims, unsupported numerical values, unsupported regulatory claims, source-unsupported examples, unapproved code, or unapproved figures.
- Do not use Step 1 Draft v0 as learner-body source except through a future Micro-Patch Gate.
- Do not broaden the source range beyond the uploaded PDF pages.

### B8. PATCH MODE Splice Verification Table

| Marker # | Anchor text | Anchor found? | Match count | Inserted? | Final location (§ + card) |
| --- | --- | --- | --- | --- | --- |
| 1 | **§1 Recap**: 이 세션의 목적은 모델링 결과를 "좋아 보인다"가 아니라 "조건을 만족하므로 비교·해석 가능하다"로 바꾸는 것이다. 즉, 판단의 언어를 … | YES | 1 | YES | §1 → before §2 |
| 2 | **MUST 1 Recap**: 초기값은 계산 전의 사전 판단이다. Graph → slope/intercept/plateau → initial estimates … | YES | 1 | YES | §2 MUST 1 — Initial Estimate Acquisition |
| 3 | **MUST 2 Recap**: GOF는 "curve가 지나가는가"가 아니라 "residual이 무작위인가"다. Residual pattern이 있으면 model… | YES | 1 | YES | §2 MUST 2 — Residual-Based Diagnostics |
| 4 | **MUST 3 Recap**: F-test는 nested + equal weighting일 때만 쓴다. AIC/SC는 nested를 요구하지 않지만 equal … | YES | 1 | YES | §2 MUST 3 — F-Test Validity Conditions |
| 5 | **MUST 4 Recap**: Fit이 좋아 보여도 parameter가 식별되지 않을 수 있다. Precision은 모델이 아니라 설계가 만든다. | YES | 1 | YES | §2 MUST 4 — Parameter Precision & Correlation |
| 6 | **MUST 5 Recap**: 최적 샘플링은 촘촘히 많이 찍는 것이 아니라, 각 parameter가 가장 크게 보이는 곳을 의도적으로 찍는 것이다. | YES | 1 | YES | §2 MUST 5 — Partial-Derivative Optimal Sampling |
| 7 | **MUST 6 Recap**: Partial derivative가 "어디서 정보가 생기는가"를 말한다면, sensitivity analysis는 "정보가 부족하… | YES | 1 | YES | §2 MUST 6 — Sensitivity Analysis |

**v3.1 splice integrity note**: PATCH MODE Splice Verification Table은 v3.1 Korean Readability Patch 적용 후에도 유효하다. 모든 anchor (각 MUST card Recap의 verbatim opening sentence)는 v3.1에서 변경되지 않았다. v3.1 패치 영역(Learner Navigation, MUST 카드의 first-use gloss, 영어 관용구 한국어화)은 splice anchor와 분리되어 있다.

**v3.2 splice integrity note**: PATCH MODE Splice Verification Table은 v3.2 Korean-Dominant Readability Patch 적용 후에도 유효하다. 모든 anchor (각 MUST card Recap의 verbatim opening sentence)는 v3.2에서 변경되지 않았다. v3.2 패치 영역(§1 후행 지식 영어 명사구 한영 병기, §5 혼동쌍 #1·#2·#3·#4 표 영어 라벨 한영 병기, §7 Q1 정답 영어 단어 나열 한영 병기)은 splice anchor와 분리되어 있다. §5 혼동쌍 표 라벨 변경은 표 내부 셀에 국한되며 §2 MUST card Recap의 anchor 텍스트에 영향을 주지 않는다.

**v3.3 splice integrity note**: PATCH MODE Splice Verification Table은 v3.3 Practice-Brief Uniformity Patch 적용 후에도 유효하다. 모든 anchor (각 MUST card Recap의 verbatim opening sentence)는 v3.3에서 변경되지 않았다. v3.3 패치는 각 MUST 카드의 **마지막 Mastery Augmentation 블록(Failure Mode / Mastery Note / Judgment Lens / Practice Lens) 직후·`---` 직전**에 Practice Brief blockquote를 1개씩 추가하는 것에 국한되며, splice anchor에 해당하는 Recap 첫 문장은 카드 중간에 위치하므로 v3.3 추가 영역과 분리되어 있다. MUST 1–6 카드 헤더 텍스트도 verbatim 보존됨.

### B9. Zero-Omission Coverage Matrix

| Domain | Required item | Evidence in PART A | Status | Action |
| --- | --- | --- | --- | --- |
| C1 Scope Lock concepts | Initial estimates, GOF/residuals, F-test/AIC/SC, precision/correlation, derivative sampling, sensitivity/toxicokinetic design | §1 roadmap; §2 MUST 1–6; §5 confusion pairs; §8 dependency chain | PRESENT | No action |
| C1 Scope page boundaries | p.352–364 / p.368–392 / p.399–405 / p.412–414; pp.365–367 and pp.406–411 not uploaded | PART A metadata and §1 선행 지식 note | PRESENT | No action |
| C2 Required data anchors | 10 mg IV bolus; K, half-life, AUC, Cl, V; bi-exponential A/B/alpha/beta; warfarin PCA; Table 4.3; repeated-dose anxiolytic; Table 4.4; LOF F-test; Table 4.8; derivative design; toxicokinetic Fig.5.20 | MUST 1 B-1–B-7; MUST 2 C; MUST 3 B/D; MUST 5 A–C; MUST 6 D | PRESENT | No action |
| C3 Audit MUST_FIX | Unsupported regulatory/financial/tool claims removed or labeled; page range corrected; weighting sign convention controlled | §1 후행 지식; MUST 2 B; MUST 3 E; PART B audit guardrails | PRESENT | No action |
| C3 Audit SHOULD_FIX | Eq.4:23–4:33/Table 4.3 restored; Fig.4.19 restored; regression objective/endless journey restored; hard thresholds removed | MUST 1 B-3/B-5/D; MUST 4 A/E | PRESENT | No action |
| C4 Audit T5 coverage | Dynamic non-steady-state, pure error/LOF, accuracy vs precision, WRSS vs −2LL, GOF checklist, toxicokinetic design | MUST 1, MUST 2, MUST 3, MUST 4, MUST 6, §8 D | PRESENT | No action |
| C5 Figure coverage KEEP | Approved Figure #1–#7 markers | PART A contains seven spliced markers after the approved recap anchors | PRESENT | No action |
| C5 Figure rejections | Dynamic non-steady-state pointer, Outlier A/B pointer, Table 4.9 pointer not restored | PART B figure inventory lists rejected items as non-renderable | PRESENT | No action |
| C6 Page tag integrity | Existing page tags preserved; no new tags created by augmentations | PART A body preserves [p.xx]/[pp.xx–yy]; augmentations have no page tags | PRESENT | No action |
| C7 Crucible Grade A preservation | Nested geometry, r misuse, derivative/information link, ridge geometry, residual pattern as time-scale exposure | MUST 2–5 canonical text and Mastery Notes #3–#6 | PRESENT_COMPRESSED | No action |
| C8 Deprecated Draft regression | No unsupported Deficiency Letter, review extension, USD, ΔOFV threshold, or unapproved software workflow restored as textbook content | PART A + PART B guardrails | PRESENT | No action |
| C9 Canonical body integrity | Content Lock v2 §1–§8 preserved; only approved 4C markers and labeled mastery notes inserted | Splice verification table; Mastery Augmentation Log | PRESENT | No action |
| C10 Embodiment coverage (ver2) | 각 MUST 카드별 체화 꿀팁, §1 거장의 한 줄 캡스톤, 혼동쌍 #1 Critical Blow 행, 혼동쌍 #2 강화된 Memory Hook | PART A의 8개 신규 ver2 augmentation; Phase 4E entries #8–#16 in B11 | PRESENT | No action |
| C11 Protocol-mandated structural elements (ver2) | PROMPT 1 §5 Critical Blow 행 (가장 파급력 큰 혼동쌍 1개) | 혼동쌍 #1 Critical Blow row, [교과서 외 실무 해석] labeled | PRESENT | No action |
| C12 v3 Surgical Patch (신설) | Critical Blow 단일화, Practice Brief 전 카드 충족, B12 Change Log, Final Checklist | B4 Critical Blow 단일성 명시 보강; B10 v3 패치 기록; B12 신설; 말미 Checklist | PRESENT | No action |
| C13 v3.1 Korean Readability Patch (신설) | Learner Navigation 한국어화, MUST 1–6 first-use gloss, 영어 관용구 한국어 정제 | Learner Navigation §A; MUST 1 Big Idea/A/D; MUST 2 B; MUST 3 D; MUST 4 A; MUST 5 D; MUST 6 Big Idea | PRESENT | No action |
| C14 v3.2 Korean-Dominant Readability Patch (신설) | §1 후행 지식 영어 명사구 한영 병기, §5 혼동쌍 #1·#2·#3·#4 표 영어 라벨 한영 병기, §7 Q1 정답 영어 단어 나열 한영 병기 | §1 후행 지식 단락; §5 혼동쌍 #1 표 헤더 3개; 혼동쌍 #2 표 헤더 1개; 혼동쌍 #3 표 헤더 1개; 혼동쌍 #4 표 헤더 2개; §7 Q1 정답 첫 문장 | PRESENT | No action |
| C15 v3.3 Practice-Brief Uniformity Patch (신설) | §2 MUST 1–6 카드 6개 모두에 균일한 4축 실무 체화 요약(Practice Brief) blockquote 추가 (왜 알아야 하는가 / 흐름상 역할 / 체화 꿀팁 / 실무 활용) | MUST 1 Failure Mode 직후; MUST 2 Mastery Note 직후; MUST 3 Judgment Lens 직후; MUST 4 Mastery Note 직후; MUST 5 Practice Lens 직후; MUST 6 Failure Mode 직후 (각 `---` 직전, 라벨 [EXPERT_INFERENCE, v3.3]) | PRESENT | No action |

### B10. Micro-Patch Log

**Phase 4D**: No micro-patches needed. PART A equals spliced learner-facing Content Lock v2 §1–§8 except approved Figure 4C markers and the bounded Mastery Augmentation Layer.

**Phase 4E (ver2)**: Eight bounded enrichment patches applied directly to PART A:
- 1× Master's One-liner capstone block (§1 after Recap)
- 6× Embodiment Tip blocks (one after each MUST 1–6 Recap)
- 1× Critical Blow row appended to 혼동쌍 #1 CONFUSION table (within existing table, not a new table)
- 1× Memory Hook strengthening (replacement of 혼동쌍 #2 hook; single line replacement, no new factual content beyond CRUCIBLE-derived dynamic-range mechanism)

All Phase 4E patches:
- preserve all existing source page tags ([p.XX], [pp.XX–YY], [pp.XX, YY], [확인 필요], [p.확인 필요])
- add no new page tags
- add no new equations
- add no new clinical scenarios, drug names, or dosing values
- add no new regulatory/business/USD claims
- add no new modern-tool names beyond what PART A already contains under [교과서 외 *] labels
- carry [CRUCIBLE_DERIVED] or compound-labeled provenance markers
- pass Audit Guardrail set B5 unchanged
- do not affect the PATCH MODE Splice Verification Table (which remains valid for the 7 Phase 4C figure markers)
- can be cleanly removed (rollback to Phase 4D state) if Phase 5 detects any rendering issue, by deleting the 8 inserted blocks/rows and reverting 혼동쌍 #2 hook

**Phase 4F / v3 (Surgical Patch)**: PART A 내용 무변경. PART B 메타데이터·가이드라인만 갱신.  [EXPERT_INFERENCE, v3]
- [PATCH 1] §5 Critical Blow 전수 스캔: `치명적 타격` 레이블이 붙은 행은 혼동쌍 #1에만 1개 존재. 혼동쌍 #2, #3, #4에는 해당 레이블 없음. 추가 레이블 변경 불필요. B4 마커 테이블에 단일성 확인 주석 추가.
- [PATCH 2] §2 MUST 1–6 Practice Brief 전수 점검: MUST 1–6 전 카드가 체화 꿀팁(다축 실천 정보 포함)을 보유하고 있어 신규 Practice Brief 추가 불필요. MUST 5는 체화 꿀팁 외 Practice Lens 블록도 별도 보유. 모든 카드 Pass.
- [PATCH 3-A] B12 v3 Change Log 신설.
- [PATCH 3-B] 파일 말미 Final v3 All-Pass Checklist (8항목) 추가.
- 모든 v3 패치: 신규 페이지 태그·수식·임상 예시·규제 주장 없음.

**v3.1 (Korean Readability Patch)**: 20개 Low-risk 패치 PART A에 적용. PART B는 본 항목과 B12 v3.1 entry 추가, B1 v3.1 contract clause, Phase 4E Certification 표의 v3.1 Certificate row, B8 splice integrity note, B9 C13 row 추가만 변경됨. 그 외 PART B 메타데이터 무변경.

v3.1 적용 패치 분류:
- **Learner Navigation 한국어화 (P-01 ~ P-11, 11개)**: How to use this handout 단락, Learning route 테이블 헤더 3개·8개 행 설명, Figure-use note 단락의 영어 산문을 한국어로 변환. 표준 약어, MUST/§ 번호 표기, FIGURE_POINTER/FIGURE_SCHEMATIC 마커명, technical 변수명 등 글로벌 표준은 영어 보존.
- **First-use gloss 추가 (P-12 ~ P-15, P-18, P-19, 6개)**: domain-informed prior(MUST 1 Big Idea), objective function surface(MUST 1 A), basin(MUST 1 D), run(MUST 2 B), dartboard(MUST 4 A), likelihood surface(MUST 5 D)에 각 1회 한국어 괄호 글로스 추가. 기존 글로스(modeling carousel, residual, ridge minimum 등)와 동일 형식.
- **영어 관용구 한국어화 (P-17, P-20, 2개)**: "battery of tools" → "복합 진단 도구군(battery of tools)" (MUST 3 D), "pre-fitting stress test" → "사전 점검 절차(pre-fitting stress test)" (MUST 6 Big Idea). 영어 원어 괄호 보존.
- **미시 연결어 정제 (P-16, 1개)**: MUST 2 B의 weighting power/exponent 표기 문장에서 "따라서"를 "즉,"으로 교체하여 인과 vs 동치 관계를 정확히 표현.

v3.1 미적용 패치:
- P-21 (Risk = Medium): MUST 4 체화 꿀팁의 괄호 분리 patch는 의미 보존 추가 검증이 필요하여 v3.1에서 보류. 차후 별도 검토 후 적용 여부 결정.

v3.1 무변경 영역:
- 모든 수식 ($CL$, $V$, $AUC$, $WRSS$, $F^*$, $r$, $C=Ae^{-\alpha t}+Be^{-\beta t}$ 등)
- 모든 페이지 태그 ([p.352], [pp.369–391], [pp.399–405], [확인 필요], [p.확인 필요] 등)
- 모든 source label ([CRUCIBLE_DERIVED], [TEXTBOOK_DERIVED], [EXPERT_INFERENCE, v3], [교과서 외 구현 번역], [교과서 외 해석], [교과서 외 실무 해석], [교과서 외 통계 도구])
- 모든 figure marker (`<!-- FIGURE_POINTER -->`, `<!-- FIGURE_SCHEMATIC -->`, `<!-- /FIGURE_POINTER -->`, `<!-- /FIGURE_SCHEMATIC -->`)
- 모든 HTML compiler marker (`<!-- MASTER LENS -->`, `<!-- TRENCH -->`, `<!-- CONFUSION -->`, `<!-- SELF-TEST -->`, `<!-- RECAP -->`, `<!-- ANCHOR -->`, `<!-- ANNOTATION -->`)
- 표준 약어 (CL, V, Vd, AUC, Cmax, Tmax, ka, ke0, EC50, IC50, Emax, Imax, IIV, BSV, RUV, OMEGA, SIGMA, ETA, EPS, OFV, VPC, GOF, CWRES, NONMEM, NCA, WRSS, AIC, SC, MM, PCA, PK, PD, IRLS, OLS, LOF, df, SE, CV%)
- Mastery Augmentation Layer 8개 항목의 위치·내용·라벨
- 거장의 한 줄 (§1 Master's One-liner) 본문
- 혼동쌍 #1 Critical Blow row 본문
- 혼동쌍 #2 강화된 Memory Hook 본문
- §7 Self-Test 9개 문제·정답·SR 태그
- §8 Final locked summary 압축 명제
- PATCH MODE Splice Verification Table의 모든 anchor (각 MUST Recap의 verbatim opening sentence)

**v3.2 (Korean-Dominant Readability Patch)**: 5개 Low-risk 패치 PART A에 적용. PART B는 본 항목과 B12-B v3.2 Change Log 신설, B1 v3.2 contract clause, Phase 4E Certification 표의 v3.2 Certificate row, B8 v3.2 splice integrity note, B9 C14 row 추가만 변경됨. 그 외 PART B 메타데이터 무변경.

v3.2 적용 패치 분류:
- **§1 후행 지식 영어 명사구 한영 병기 (Q-01, 1개)**: residual diagnostics, parameter precision, design feedback에 한국어 병기 추가. −2·log likelihood 비교는 표준 표기로 보존. NONMEM/PsN/xpose 도구명은 영어 보존.
- **§5 혼동쌍 표 영어 라벨 한영 병기 (Q-02 ~ Q-04, 3개 패치 / 7개 라벨)**: 혼동쌍 #1 표의 "Source correction", "AIC/SC boundary", "Critical example"; 혼동쌍 #2 표의 "Source correction"; 혼동쌍 #3 표의 "Source anchor"; 혼동쌍 #4 표의 "Source description", "Source anchor"에 한국어 병기 추가. 표 본문(설명 셀)은 무변경.
- **§7 Self-Test Q1 정답 영어 단어 나열 한영 병기 (Q-05, 1개)**: "wrong final values, unwanted local minima, physiologically impossible parameter values"에 각각 한국어 번역을 괄호로 병기. 영어 원어는 보존되어 PDF 원전 표현 추적성 유지.

v3.2 무변경 영역:
- v3.1 무변경 영역 전체 (수식, 페이지 태그, source label, figure marker, HTML compiler marker, 표준 약어, Mastery Augmentation Layer, 거장의 한 줄, Critical Blow row 본문, Memory Hooks, Self-Test 문제 본문 및 정답의 핵심 산문, §8 Final locked summary, PATCH MODE Splice Verification Table anchor)
- 추가 v3.2 무변경 영역:
  - PART A 헤더 metadata (Source, Scope, Verified page range, Missing uploaded pages, Mode, Learner-facing status 라벨 — metadata 성격으로 영어 유지)
  - Assembly Mode, Input Manifest 영문 본문 (compiler-only metadata)
  - §1 Big Idea, §1 개념 항법도 ASCII art, §1 Recap, 거장의 한 줄 (모두 v3.2 패치 영역과 분리)
  - §2 MUST 1–6 카드 본문 (Big Idea, A. Formal Definition, B. derivation, C. Structural Necessity, D. Assumptions, E. Limitations, Recap, 체화 꿀팁, Mastery Augmentation block 본문 모두 무변경)
  - §5 혼동쌍 #1, #2, #3, #4 표 본문 셀 (라벨 외 모든 설명 셀 무변경)
  - §5 모든 기억 고리(Memory Hook), TRENCH 블록 본문
  - §7 Q2–Q9 정답 (Q1만 패치)
  - §8 A. Positioning, B. Dependency chain, C. Professional moat, D. GOF checklist, E. Final locked summary 본문 무변경
  - 모든 FIGURE_POINTER / FIGURE_SCHEMATIC marker 내부 영문 brief (v3.2 prompt 명시 규칙: "figure marker의 위치와 내용은 절대 변경하지 마라")
  - 모든 NONMEM/R/Python 코드 블록 (없음, 본 세션은 코드 블록 부재)
  - PATCH MODE Splice Verification Table의 7개 anchor 전부 (각 MUST Recap 첫 문장)

**v3.3 (Practice-Brief Uniformity Patch)**: 6개 Low-risk 패치 PART A §2 MUST 1–6 카드에 적용. PART B는 본 항목과 B12-C v3.3 Change Log 신설, B1 v3.3 contract clause, Phase 4E Certification 표의 v3.3 Certificate row, B4 marker mapping의 Practice Brief 행 신설, B8 v3.3 splice integrity note, B9 C15 row, B11 Mastery Augmentation Log Phase 4F (v3.3) entries #17–#22 추가만 변경됨. 그 외 PART B 메타데이터 무변경.

| Patch ID | 적용 위치 | 수행 내용 | Change type | Risk |
| --- | --- | --- | --- | --- |
| Δ-V3.3-01 | §2 MUST 1 — Failure Mode 직후, `---` 직전 | 카드별 균일 4축 실무 체화 요약(Practice Brief) blockquote 추가. 라벨 [EXPERT_INFERENCE, v3.3]. 카드 본문에 이미 존재하는 graphical method, basin, compound knowledge, EDA, NONMEM `$THETA` 등 개념만 사용. 새 페이지 태그·수식·약물·수치 anchor·외부 reference 0건. | Practice-Brief uniformity (per-card) | Low |
| Δ-V3.3-02 | §2 MUST 2 — Mastery Note 직후, `---` 직전 | 카드별 균일 4축 실무 체화 요약 blockquote 추가. 라벨 [EXPERT_INFERENCE, v3.3]. 카드 본문에 이미 존재하는 residual pattern (random scatter / banana / fan / leverage), CWRES/IWRES, ε(잔차 분산) 개념만 사용. 새 페이지 태그·수식·약물·수치 anchor·외부 reference 0건. | Practice-Brief uniformity (per-card) | Low |
| Δ-V3.3-03 | §2 MUST 3 — Judgment Lens 직후, `---` 직전 | 카드별 균일 4축 실무 체화 요약 blockquote 추가. 라벨 [EXPERT_INFERENCE, v3.3]. 카드 본문에 이미 존재하는 nested/equal weighting 두 조건, F-test critical value, AIC/SC, ΔOFV 개념만 사용. Apex Concept 배지 무변경. 새 페이지 태그·수식·약물·수치 anchor·외부 reference 0건. | Practice-Brief uniformity (per-card) | Low |
| Δ-V3.3-04 | §2 MUST 4 — Mastery Note 직후, `---` 직전 | 카드별 균일 4축 실무 체화 요약 blockquote 추가. 라벨 [EXPERT_INFERENCE, v3.3]. 카드 본문에 이미 존재하는 정밀도(SE/CV%), 상관(correlation matrix), ridge minimum, $COV step, identifiability 개념만 사용. 보편적 cutoff 미정의 원칙 보존. 새 페이지 태그·수식·약물·수치 anchor·외부 reference 0건. | Practice-Brief uniformity (per-card) | Low |
| Δ-V3.3-05 | §2 MUST 5 — Practice Lens 직후, `---` 직전 | 카드별 균일 4축 실무 체화 요약 blockquote 추가. 라벨 [EXPERT_INFERENCE, v3.3]. 카드 본문에 이미 존재하는 편미분 ∂C/∂θ, sensitivity peak, anchor + 보험 두 층 design, sparse-data 개념만 사용. 새 페이지 태그·수식·약물·수치 anchor·외부 reference 0건. | Practice-Brief uniformity (per-card) | Low |
| Δ-V3.3-06 | §2 MUST 6 — Failure Mode 직후, `---`(§5 시작) 직전 | 카드별 균일 4축 실무 체화 요약 blockquote 추가. 라벨 [EXPERT_INFERENCE, v3.3]. 카드 본문에 이미 존재하는 sensitivity analysis 절차(±50% / +100%·−50%), capacity-dependent vs time-dependent process 상쇄, modeling carousel 사이클 개념만 사용. 새 페이지 태그·수식·약물·수치 anchor·외부 reference 0건. | Practice-Brief uniformity (per-card) | Low |

v3.3 무변경 영역:
- v3.2 무변경 영역 전체 (수식, 페이지 태그, source label, figure marker, HTML compiler marker, 표준 약어, Mastery Augmentation Layer 본문, Phase 5 splice anchor)
- 추가 v3.3 무변경 영역:
  - **§2 MUST 1–6 카드 헤더 텍스트 verbatim** (`### ▣ MUST 1 — 초기값 획득의 실전 기술 (Initial Estimate Acquisition)` 형식 일체) — Splice Verification Table anchor 보호
  - **MUST 3 [⚡ Apex Concept] 배지 + F-test validity conditions 본문** (Eq.4:54·4:55, Valid/Invalid/Conditionally valid examples, Plausible Fallacy 일체)
  - **§5 혼동쌍 4개의 표·잠금 일체** (Critical Blow row, Memory Hooks 4개, TRENCH 블록 모두 byte-level 보존)
  - **§7 Q9 Boss Dilemma 정답 방향** + Q1–Q8 모든 정답 방향
  - **§8D GOF Checklist locked from Table 4.9 표 전체** — 본 세션의 핵심 산출물
  - 모든 §2 카드 기존 본문 (Big Idea, A–E subsections, Recap, 체화 꿀팁, FIGURE marker, 모든 기존 Mastery Augmentation 블록)
  - PART B B8 Splice Verification Table의 7개 anchor (각 MUST Recap의 verbatim opening sentence)

### B11. Mastery Augmentation Log

#### Phase 4D entries (preserved from original master)

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | §1 after Figure #1 | W / workflow consequence | YES | CRUCIBLE_DERIVED | Frames the six cards as a closed modeling loop rather than isolated techniques. | Low |
| 2 | MUST 1 after Figure #2 | F / failure mode | YES | TEXTBOOK_DERIVED | Reinforces bad initial estimates entering the wrong objective-function basin. | Low |
| 3 | MUST 2 after Figure #3 | M / macro insight | YES | CRUCIBLE_DERIVED | Links residual time pattern to missing time scale and prevents treatment swapping. | Low |
| 4 | MUST 3 after Figure #4 | J / judgment lens | YES | CRUCIBLE_DERIVED | Explains nestedness as same-comparison-coordinate condition. | Low |
| 5 | MUST 4 after Figure #5 | M / macro insight | YES | CRUCIBLE_DERIVED | Turns parameter correlation into ridge-minimum geometry. | Low |
| 6 | MUST 5 after Figure #6 | W / workflow consequence | YES | CRUCIBLE_DERIVED | Connects derivative peaks to visible parameter regions while preserving boundary conditions. | Low |
| 7 | MUST 6 after Figure #7 | F / failure mode | YES | TEXTBOOK_DERIVED | Highlights toxicokinetic masking without adding new values or examples. | Low |

#### Phase 4E entries (ver2 — new)

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
| --- | --- | --- | --- | --- | --- | --- |
| 8 | §1 after Recap, before Figure #1 | C / capstone (Master's One-liner) | YES | CRUCIBLE_DERIVED | Provides a single quotable sentence that compresses the session into one master's frame; resolves the "거장 메타 통찰 캡스톤 부재" gap identified in ver1 review. | Low |
| 9 | MUST 1 after Recap | E / embodiment tip | YES | CRUCIBLE_DERIVED | Adds explicit embodiment instruction ("종이에 예상 parameter와 근거 적기") for Initial Estimate card, addressing "체화 꿀팁 부재" gap. | Low |
| 10 | MUST 2 after Recap | E / embodiment tip | YES | CRUCIBLE_DERIVED | Promotes "two-axis residual plot" routine to the level of card-default practice; complements the existing TRENCH on the same point. | Low |
| 11 | MUST 3 after Recap | E / embodiment tip | YES | CRUCIBLE_DERIVED | Converts the F-test/AIC validity rules into a two-question pre-comparison routine; addresses MUST 3 TRENCH absence. | Low |
| 12 | MUST 4 after Recap | E / embodiment tip | YES | CRUCIBLE_DERIVED | Forces the learner to break the automatic "good fit → good parameters" inference; addresses MUST 4 TRENCH absence; carefully avoids introducing new hard thresholds. | Low |
| 13 | MUST 5 after Recap | E / embodiment tip | YES | CRUCIBLE_DERIVED | Makes the "anchor + range" two-layer sampling design explicit as a card practice. | Low |
| 14 | MUST 6 after Recap | E / embodiment tip | YES | CRUCIBLE_DERIVED | Translates sensitivity analysis into a pre-interpretation perturbation routine; ties toxicokinetic masking back to the core practice. | Low |
| 15 | §5 혼동쌍 #1 — Critical Blow row | B / boss-impact row | YES | CRUCIBLE_DERIVED with [교과서 외 실무 해석] label | Restores PROMPT 1 §5 protocol mandate that was previously removed due to Audit MUST_FIX on Deficiency Letter framing; reframes consequence as workflow contamination without fabricating regulatory letters or USD claims. | Low–Medium (label-dependent) |
| 16 | §5 혼동쌍 #2 — Memory Hook | H / memory-hook strengthening | YES | CRUCIBLE_DERIVED | Encodes the dynamic-range mechanism behind r inflation directly into the hook, satisfying the PROMPT 1 §5 requirement that hooks encode structural reasons rather than restate differences. Replaces (not adds to) the previous thinner hook. | Low |

#### Phase 4F entries (v3.3 — new)

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
| --- | --- | --- | --- | --- | --- | --- |
| 17 | MUST 1 — Failure Mode 직후, `---` 직전 | P / Practice Brief 4-axis | YES | EXPERT_INFERENCE, v3.3 | MUST 1 카드별 균일 4축 실무 체화 요약. 4축: (1) 비선형 회귀에서 초기값 품질이 후속 모든 진단을 결정하므로 graphical/잔차 기반 초기값 도출 필수, (2) 후속 5개 카드의 사전 조건이자 EDA-§4 모델 구축 단계의 다리, (3) graphical method 손 적용 + 종이 위 초기값 후보 1개 선언 routine, (4) NONMEM control stream 전 EDA 도표 위 graphical 초기값 도출 → `$THETA` initial 명시 입력. | Low |
| 18 | MUST 2 — Mastery Note 직후, `---` 직전 | P / Practice Brief 4-axis | YES | EXPERT_INFERENCE, v3.3 | MUST 2 카드별 균일 4축 실무 체화 요약. 4축: (1) 잔차의 trend·systematic deviation·heteroscedasticity는 noise가 아닌 모델 결함 신호 (ε 흡수 시 가짜 IIV/covariate signal 생성), (2) MUST 1 fitting 검증 첫 관문 + MUST 3 F-test 사전 조건 + §8D GOF Checklist 입력, (3) 4가지 잔차 패턴 손 그리기 + 결함 원인 한 줄 매핑, (4) NONMEM CWRES/IWRES vs time·IPRED plot에서 trend → weighting 변경 전 구조 모델 결함 가능성 우선 보고. | Low |
| 19 | MUST 3 — Judgment Lens 직후, `---` 직전 | P / Practice Brief 4-axis | YES | EXPERT_INFERENCE, v3.3 | MUST 3 카드별 균일 4축 실무 체화 요약. 4축: (1) F-test는 nested + equal weighting에서만 valid, 두 조건 위반 시 통계적 결론 자체 무의미 (Table 4.8 더블 위반 사례), (2) 본 세션의 Apex Concept + MUST 2 통과 모델 후보들의 정량 비교 단계 + §5 혼동쌍 #1의 직접 모태, (3) "Nested + Equal Weighting" mantra + 분기 규칙 자문, (4) 모델 비교 보고서에서 nested 관계·동일 weighting 명시 검증 후에만 ΔOFV/F-statistic 인용. | Low |
| 20 | MUST 4 — Mastery Note 직후, `---` 직전 | P / Practice Brief 4-axis | YES | EXPERT_INFERENCE, v3.3 | MUST 4 카드별 균일 4축 실무 체화 요약. 4축: (1) 정밀도와 상관 동시 점검 없이는 점추정값 신뢰성·식별 가능성 판단 불가 (ridge minimum 위 파라미터 쌍은 데이터가 식별 못하는 quantity일 수 있음), (2) $COV step 출력 해석 spine + MUST 3 통과 모델 후속 검증 + MUST 5 sampling design으로 연결, (3) 정밀도(SE/CV%)·correlation matrix 한 화면 동시 스캔 routine + "fit 좋다 → parameter 좋다" 자동 추론 차단, (4) PopPK 보고서에 점추정값+SE/CV%+correlation 함께 표기, 상관 높은 쌍은 다음 cohort sampling design 변경 권고. | Low |
| 21 | MUST 5 — Practice Lens 직후, `---` 직전 | P / Practice Brief 4-axis | YES | EXPERT_INFERENCE, v3.3 | MUST 5 카드별 균일 4축 실무 체화 요약. 4축: (1) 채혈 시점이 어떤 파라미터를 식별 가능하게 하는지 정량화 못하면 design이 직관 의존, MUST 4 정밀도·상관이 design 한계로 무너지는 sampling identifiability 함정, (2) MUST 4 정밀도 평가의 사전적 design 자리 + 임상시험 PK 채혈 protocol 정량 근거 + sparse-data 입구, (3) ∂C/∂θ peak를 1구획 ka·V·CL에 손 적용 + "anchor + 전체 range 보험" 두 층 골격, (4) DDI/Phase 1 PK study 채혈 시점에 sensitivity 분석을 protocol 정당화 근거로 첨부. | Low |
| 22 | MUST 6 — Failure Mode 직후, `---`(§5 시작) 직전 | P / Practice Brief 4-axis | YES | EXPERT_INFERENCE, v3.3 | MUST 6 카드별 균일 4축 실무 체화 요약. 4축: (1) 출력 민감도 미평가 시 모델 robustness 평가 불가, 규제 제출 시 "파라미터 불확실성이 결론을 바꾸는가" 답변 불가, (2) 본 세션의 종합 출구 + MUST 4 정밀도·MUST 5 design 통합 risk assessment + modeling carousel 사이클을 다음 design으로 되돌리는 마지막 매듭, (3) ±50%·+100%·−50% 손 적용 + "민감 vs 둔감" 한 줄 분류 + "흔들어도 살아남는 결론만 보고하라" 행동 규칙, (4) NDA/IND dossier에 sensitivity analysis 결과 첨부, dose·safety margin·sampling schedule 흔드는 핵심 파라미터를 모델 risk 항목으로 명시. | Low |

#### Rejected or Deferred Augmentation Candidates (ver1 + ver2)

| Rejected candidate | Reason for rejection |
| --- | --- |
| Additional r/dynamic-range note in §5 | Rejected because canonical body already contains the same bounded interpretation. |
| Outlier A/B new figure or expanded leverage diagnostics | Rejected because Phase 4C rejected the figure and extra statistics would expand beyond the locked body. |
| External NONMEM/ΔOFV/PFIM/PopED implementation details | Rejected because Audit explicitly limits modern tools to labeled implementation translation and forbids unsupported thresholds. |
| Per-card "실무 활용 시나리오" section with full case study | Deferred — would require new clinical scenarios not in source PDF; out of scope. Embodiment tips (Phase 4E) cover the "how to use this in practice" function without introducing new cases. |
| Boss Dilemma Q9 expanded answer with explicit "둘 다 잘못된 모델" branch | Deferred — already covered in §8 Professional Moat; duplication risk. |
| §8 final master's seal beyond existing E. Final locked summary | Deferred — Final locked summary already serves capstone function for §8; ver2 adds master's one-liner at §1 entry which is the higher-leverage location. |
| New page tags on Phase 4E embodiment tips | REJECTED — Phase 1 Rule 8 closed page tagging at Phase 4A; embodiment tips are CRUCIBLE_DERIVED interpretations, not direct PDF citations, and therefore do not carry [p.XX]. |
| P-21 (MUST 4 체화 꿀팁 괄호 분리) | DEFERRED in v3.1 — Risk = Medium. 의미 보존 검증 필요. 차후 별도 검토 시 재평가. |
| Q-XX 후보: PART A 헤더 metadata 라벨(Source/Scope/Verified page range/Missing uploaded pages/Mode/Learner-facing status) 한영 병기 | DEFERRED in v3.2 — metadata 성격으로 영어 보존이 일관성·국제 실무 호환성에 더 적합. v3.2 prompt가 강조하는 "learner-facing 산문" 범위 외부로 판단. 차후 별도 정책 결정 후 재평가. |
| Q-XX 후보: §2 MUST 1 A "Initial estimate acquisition은 nonlinear regression을 시작하기 전에..." 정의 문장의 영어 명사구 추가 한영 병기 | DEFERRED in v3.2 — 이미 v3.1에서 핵심 용어(domain-informed prior, objective function surface, basin)에 first-use gloss 적용 완료. 동일 문장에 추가 병기 시 가독성이 오히려 저하될 수 있음. 현 정제 수준이 적절. |
| Q-XX 후보: §7 Q2–Q9 정답의 영어 명사구 추가 한영 병기 | DEFERRED in v3.2 — Q2–Q9 정답은 이미 한국어 위주로 작성되어 있고 영어 명사구는 표준 약어·기호·고유명사(NCA, IRLS, OLS, F-test, AIC, Emax, sigmoid Emax, weighted/unweighted fit 등)로 한정됨. career-critical 용어 보존 정책에 부합. |
| Q-XX 후보: FIGURE_POINTER / FIGURE_SCHEMATIC marker 내부 영문 brief 한국어화 | REJECTED in v3.2 — v3.2 prompt 명시 규칙 ("figure marker의 위치와 내용은 절대 변경하지 마라") 위반. Phase 5 HTML compiler가 marker 내부를 directive-aware하게 파싱하므로 영문 보존 필수. |

---

### B12. v3 Change Log  [EXPERT_INFERENCE, v3]

*(이 섹션은 compiler-only. Phase 5 렌더링 대상 아님.)*

| Patch ID | 적용 위치 | 수행 내용 | 근거 | 결과 |
| --- | --- | --- | --- | --- |
| P1-SCAN | §5 전체 (혼동쌍 #1–#4) | `치명적 타격` / Critical Blow 레이블 전수 스캔 | 프로토콜: 가장 파급력 높은 혼동쌍 1개에만 허용 | 혼동쌍 #1에만 1개 존재 확인; 혼동쌍 #2–#4 해당 없음. 추가 레이블 변경 불필요. |
| P1-B4 | PART B B4 마커 테이블 | Critical Blow 단일성 확인 주석 추가 ("v3 확인: 혼동쌍 #1 전용 단일 행") | Phase 5 compiler에게 단일 행 조건 명시 전달 | B4 테이블 해당 셀에 주석 삽입 완료 |
| P2-AUDIT | §2 MUST 1–6 전체 | Practice Brief / 4축 실천 블록 존재 여부 점검 | 4축 실천 정보 부재 카드에만 추가 지시 | MUST 1–6 전 카드 체화 꿀팁 보유 확인; MUST 5 Practice Lens 추가 보유; 신규 추가 없음 |
| P3-B9 | PART B B9 Zero-Omission Matrix | C12 행 신설 (v3 Surgical Patch 커버리지) | 패치 추적 완결성 | C12 행 추가 완료 |
| P3-B10 | PART B B10 Micro-Patch Log | Phase 4F/v3 패치 항목 추가 | 변경 이력 기록 | v3 3개 패치 항목 기록 완료 |
| P3-B12 | PART B 말미 | B12 v3 Change Log 신설 (이 표) | 패치 추적 및 감사 가능성 | 신설 완료 |
| P3-CHKLIST | 파일 최말미 | Final v3 All-Pass Checklist (8항목) 추가 | 품질 보증 최종 확인 | 추가 완료 |

**v3 패치 범위 제한 선언**: PART A 과학 내용·수식·페이지 태그·Embodiment Tips·Critical Blow·Memory Hooks·거장의 한 줄·모델-빌딩 워크플로우 일체 무변경. 모든 v3 추가는 PART B 메타데이터 및 파일 말미 Checklist에 국한됨.

---

### B12-A. v3.1 Korean Readability Patch — Change Log

*(이 섹션은 compiler-only. Phase 5 렌더링 대상 아님.)*

| Patch ID | 적용 위치 | 수행 내용 | Change type | Risk |
| --- | --- | --- | --- | --- |
| P-01 | Learner Navigation §A "How to use this handout" 단락 | 영어 산문 → 한국어 번역. 학습 진입 동선·MUST 카드 순서·§5/§7/§8 활용법을 한국어 명령형 문장으로 재구성. | Korean flow improvement | Low |
| P-02 | Learner Navigation §A Learning route 테이블 헤더 3개 | "Route step / Focus / What you should be able to do before moving on" → "학습 단계 / 집중 포인트 / 이 단계 이후 할 수 있어야 하는 것" | Korean flow improvement | Low |
| P-03 | Learning route Row 1 설명 | 영문 → 한국어 ("이 세션이 여섯 개의 독립 기술이 아니라 하나의 닫힌 모델링 루프인 이유를 설명할 수 있다") | Korean flow improvement | Low |
| P-04 | Learning route Row 2 설명 | 영문 → 한국어 (NCA anchor·초기값 도출·fitting 잘못된 결과 연결 설명) | Korean flow improvement | Low |
| P-05 | Learning route Row 3 설명 | 영문 → 한국어 (잔차 형태 → 구조/분산/설계 문제 매핑) | Korean flow improvement | Low |
| P-06 | Learning route Row 4 설명 | 영문 → 한국어 (F-test/AIC/SC 적용 가능 조건 판단) | Korean flow improvement | Low |
| P-07 | Learning route Row 5 설명 | 영문 → 한국어 + identifiability 글로스 | Korean flow improvement + First-use gloss | Low |
| P-08 | Learning route Row 6 설명 | 영문 → 한국어 (편미분 극값 → sampling 위치 변환) | Korean flow improvement | Low |
| P-09 | Learning route Row 7 설명 | 영문 → 한국어 (민감도 분석 → 실패 영역 특정) | Korean flow improvement | Low |
| P-10 | Learning route Row 8 설명 | 영문 → 한국어 (혼동쌍 해소·자기 테스트 답변) | Korean flow improvement | Low |
| P-11 | Learner Navigation §A "Figure-use note" 단락 | 영어 산문 → 한국어 번역. FIGURE_POINTER / FIGURE_SCHEMATIC 마커명·역할 설명을 한국어로 재구성. 마커명 자체는 영어 보존. | Korean flow improvement | Low |
| P-12 | MUST 1 — Big Idea (line 142 region) | "domain-informed prior" 첫 등장에 글로스 "(← 도메인 지식에 근거한 사전 추정값)" 추가 | First-use gloss | Low |
| P-13 | MUST 1 — A. Formal Definition | "objective function surface" 첫 등장에 글로스 "(← 파라미터 조합에 따라 잔차 제곱합 값이 분포하는 지형)" 추가 | First-use gloss | Low |
| P-14 | MUST 1 — D. Assumptions & Boundaries | "basin" 첫 등장에 글로스 "(← 수렴 가능한 극솟값 영역)" 추가 | First-use gloss | Low |
| P-15 | MUST 2 — B. Diagnostic pattern catalogue | "run" 첫 등장에 글로스 "(← 같은 부호 잔차가 연속으로 이어지는 패턴)" 추가 | First-use gloss | Low |
| P-16 | MUST 2 — B. Weighting power/exponent 문장 | 인과 접속 "따라서" → 동치 표현 "즉," 으로 교체. Weighting power/exponent 표기 권고 의미 명료화. | Concept clarification | Low |
| P-17 | MUST 3 — D. AIC/SC boundary | "battery of tools다" → "복합 진단 도구군(battery of tools)이다". 영어 관용구를 한국어 명사구로 풀고 영어 원어 괄호 보존. | Korean flow improvement | Low |
| P-18 | MUST 4 — A. Accuracy, precision, and CV% | "원문은 dartboard를 통해" → "원문은 다트 과녁(dartboard) 비유를 통해". 비유 대상 명시. | First-use gloss | Low |
| P-19 | MUST 5 — D. Structural Necessity | "likelihood surface" 첫 등장에 글로스 "(← 파라미터 공간에서 OFV 값이 분포하는 지형)" 추가 | First-use gloss | Low |
| P-20 | MUST 6 — Big Idea | "pre-fitting stress test다" → "사전 점검 절차(pre-fitting stress test)다". 영어 표현을 한국어 명사구로 풀고 영어 원어 괄호 보존. | Korean flow improvement | Low |

**v3.1 패치 범위 제한 선언**: PART A의 과학 내용·수식·페이지 태그·source label·figure marker·HTML compiler marker·NONMEM/R 코드·표준 약어·Mastery Augmentation Layer 위치 및 본문·Phase 5 splice anchor 일체 무변경. 모든 v3.1 추가는 (a) PART A의 학습자-facing 산문 한국어화 20개 패치(P-01 ~ P-20)와, (b) PART B의 본 Change Log 신설·B1 contract clause·Phase 4E Certification v3.1 row·B8 splice integrity note·B9 C13 row·B10 v3.1 micro-patch entry에 국한됨.

---

### B12-B. v3.2 Korean-Dominant Readability Patch — Change Log

*(이 섹션은 compiler-only. Phase 5 렌더링 대상 아님.)*

| Patch ID | 적용 위치 | 수행 내용 | Change type | Risk |
| --- | --- | --- | --- | --- |
| Q-01 | §1 — 지식 그래프 위치 / 후행 지식 단락 | "residual diagnostics, parameter precision, design feedback" 영어 명사구 3개에 한국어 병기 추가 → "잔차 진단(residual diagnostics)", "파라미터 정밀도(parameter precision)", "설계 피드백(design feedback)". "−2·log likelihood 비교"는 표준 표기로 보존. NONMEM/PsN/xpose 도구명은 영어 보존. | Korean-dominant flow improvement | Low |
| Q-02 | §5 혼동쌍 #1 표 — 라벨 셀 3개 | "Source correction" → "원전 교정(Source correction)". "AIC/SC boundary" → "AIC/SC 적용 경계(AIC/SC boundary)". "Critical example" → "결정적 예(Critical example)". 본문 셀 무변경. | Korean-dominant flow improvement (label-only) | Low |
| Q-03 | §5 혼동쌍 #2 표 — 라벨 셀 1개 | "Source correction" → "원전 교정(Source correction)". 본문 셀 무변경. | Korean-dominant flow improvement (label-only) | Low |
| Q-04 | §5 혼동쌍 #3·#4 표 — 라벨 셀 3개 | 혼동쌍 #3 "Source anchor" → "원전 anchor 위치(Source anchor)". 혼동쌍 #4 "Source description" → "원전 서술(Source description)". 혼동쌍 #4 "Source anchor" → "원전 anchor 위치(Source anchor)". 본문 셀 무변경. | Korean-dominant flow improvement (label-only) | Low |
| Q-05 | §7 Self-Test Q1 정답 첫 문장 | "wrong final values, unwanted local minima, physiologically impossible parameter values" 영어 단어 나열 3개에 한국어 병기 추가 → "잘못된 최종 추정값(wrong final values), 원치 않는 국소 최솟값(unwanted local minima), 생리학적으로 불가능한 parameter 값(physiologically impossible parameter values)". 영어 원어 보존으로 PDF 원전 표현 추적성 유지. 정답 두 번째 문장 무변경. | Korean-dominant flow improvement (term-pair) | Low |

**v3.2 패치 범위 제한 선언**: PART A의 과학 내용·수식·페이지 태그·source label·figure marker·HTML compiler marker·NONMEM/R 코드·표준 약어·Mastery Augmentation Layer 위치 및 본문·Phase 5 splice anchor 일체 무변경. 모든 v3.2 추가는 (a) PART A의 학습자-facing 산문 한국어 정제 5개 패치(Q-01 ~ Q-05)와, (b) PART B의 본 Change Log 신설·B1 v3.2 contract clause·Phase 4E Certification v3.2 row·B8 v3.2 splice integrity note·B9 C14 row·B10 v3.2 micro-patch entry·B11 deferred candidates 추가에 국한됨.

**v3.2 적용 원칙**:
1. **Career-critical 용어 보존**: 영어 원어를 한국어 병기 형식 `한글(English)`로 처리하여 학습자가 한국어로 즉시 이해하면서도 국제 학술·실무 환경에서 영어 용어를 알 수 있도록 함.
2. **Career-critical 용어 보존 (영어 단독 유지)**: 표준 약어·기호·수식 변수·고유명사·코드 변수명·NONMEM/R 구문은 영어 단독 유지 (예: CL, V, AUC, IIV, OFV, NONMEM, MathJax, $r$, $F^*$ 등).
3. **PDF 원전 표현 보존**: §7 Q1 정답의 영어 단어 나열은 PDF 원전 직접 인용 가능성이 있으므로 영어 원어를 괄호 안에 보존.
4. **Splice anchor 무변경**: PATCH MODE Splice Verification Table의 7개 anchor (각 MUST Recap의 verbatim opening sentence)는 일체 손대지 않음.
5. **Marker 내부 무변경**: FIGURE_POINTER / FIGURE_SCHEMATIC marker 내부 영문 brief는 v3.2 prompt 명시 규칙에 따라 보존.

---

### B12-C. v3.3 Practice-Brief Uniformity Patch — Change Log

*(이 섹션은 compiler-only. Phase 5 렌더링 대상 아님.)*

| Patch ID | 적용 위치 | 수행 내용 | Change type | Risk |
| --- | --- | --- | --- | --- |
| Δ-V3.3-01 | §2 MUST 1 — Failure Mode 직후, `---` 직전 | 카드별 균일 4축 실무 체화 요약(Practice Brief) blockquote 1개 추가. 라벨 [EXPERT_INFERENCE, v3.3]. 4축: (1) 왜 알아야 하는가, (2) 흐름상 역할, (3) 체화 꿀팁, (4) 실무 활용. 카드 본문에 이미 존재하는 graphical method, basin, $\theta$ initial, NONMEM 등 개념만 사용. | Practice-Brief uniformity (per-card) | Low |
| Δ-V3.3-02 | §2 MUST 2 — Mastery Note 직후, `---` 직전 | 카드별 균일 4축 Practice Brief blockquote 1개 추가. 라벨 [EXPERT_INFERENCE, v3.3]. 카드 본문에 이미 존재하는 잔차 패턴 4종, ε(잔차 분산), CWRES/IWRES, GOF Checklist 입력 개념만 사용. | Practice-Brief uniformity (per-card) | Low |
| Δ-V3.3-03 | §2 MUST 3 — Judgment Lens 직후, `---` 직전 | 카드별 균일 4축 Practice Brief blockquote 1개 추가. 라벨 [EXPERT_INFERENCE, v3.3]. 카드 본문에 이미 존재하는 nested + equal weighting 두 조건, F-test critical value, AIC/SC 분기, ΔOFV 개념만 사용. Apex Concept 배지·F-test validity 본문 무변경. | Practice-Brief uniformity (per-card) | Low |
| Δ-V3.3-04 | §2 MUST 4 — Mastery Note 직후, `---` 직전 | 카드별 균일 4축 Practice Brief blockquote 1개 추가. 라벨 [EXPERT_INFERENCE, v3.3]. 카드 본문에 이미 존재하는 정밀도(SE/CV%)·correlation matrix·ridge minimum·$COV step·identifiability 개념만 사용. 보편적 cutoff 미정의 원칙 보존. | Practice-Brief uniformity (per-card) | Low |
| Δ-V3.3-05 | §2 MUST 5 — Practice Lens 직후, `---` 직전 | 카드별 균일 4축 Practice Brief blockquote 1개 추가. 라벨 [EXPERT_INFERENCE, v3.3]. 카드 본문에 이미 존재하는 ∂C/∂θ peak·anchor + 보험 두 층 design·sparse-data·Phase 1 PK study 개념만 사용. | Practice-Brief uniformity (per-card) | Low |
| Δ-V3.3-06 | §2 MUST 6 — Failure Mode 직후, `---`(§5 시작) 직전 | 카드별 균일 4축 Practice Brief blockquote 1개 추가. 라벨 [EXPERT_INFERENCE, v3.3]. 카드 본문에 이미 존재하는 sensitivity 절차(±50% / +100%·−50%)·capacity-dependent vs time-dependent 상쇄·modeling carousel·NDA/IND dossier 개념만 사용. | Practice-Brief uniformity (per-card) | Low |

**v3.3 패치 범위 제한 선언**: PART A의 과학 내용·수식·페이지 태그·source label·figure marker·HTML compiler marker·NONMEM/R 코드·표준 약어·Mastery Augmentation Layer 본문(Phase 4D #1–7, Phase 4E #8–16) 일체 무변경. **§8D GOF Checklist locked from Table 4.9 표 byte-level 보존**, **MUST 3 [⚡ Apex Concept] 배지 + F-test validity conditions 본문 byte-level 보존**, **§5 혼동쌍 4개 표 잠금 일체 보존**, **§7 Q9 Boss Dilemma + Q1–Q8 정답 방향 byte-level 보존**, **MUST 1–6 카드 헤더 텍스트 verbatim 보존**, **PATCH MODE Splice Verification Table 7개 anchor verbatim 보존**. 모든 v3.3 추가는 (a) PART A §2 MUST 1–6 카드별 Practice Brief blockquote 6개 추가(Δ-V3.3-01 ~ Δ-V3.3-06)와, (b) PART B의 본 Change Log 신설·B1 v3.3 contract clause·Phase 4E Certification v3.3 row·B4 marker mapping Practice Brief 행·B8 v3.3 splice integrity note·B9 C15 row·B10 v3.3 micro-patch entry·B11 Phase 4F entries #17–#22 추가에 국한됨.

**v3.3 적용 원칙**:
1. **카드별 균일 4축 구조**: 모든 6개 Practice Brief가 동일한 4축(왜 알아야 하는가 / 흐름상 역할 / 체화 꿀팁 / 실무 활용)을 동일한 blockquote 형식으로 가짐. 단권화 학습자가 모든 카드에서 동일한 능동 회상 closure를 받도록 함.
2. **카드 본문 내용만 사용**: 각 Practice Brief는 카드 본문에 이미 존재하는 개념·예시·식·수치만 사용. 새 페이지 태그·새 약물·새 수치 anchor·새 외부 reference 0건 도입.
3. **라벨 일관성**: 모든 6개 Practice Brief가 라벨 `[EXPERT_INFERENCE, v3.3]`로 통일. 다른 source 라벨과 혼합 금지.
4. **Splice anchor 무변경**: PATCH MODE Splice Verification Table의 7개 anchor (각 MUST Recap의 verbatim opening sentence)는 카드 중간에 위치하므로 v3.3 추가 영역(카드 끝)과 분리되어 자동 보호됨.
5. **Apex / Boss Dilemma / GOF Checklist 보호**: MUST 3 Apex Concept 배지·F-test validity 본문, §7 Q9 Boss Dilemma 정답 방향, §8D Table 4.9 GOF Checklist 표는 절대 보존 영역으로 byte-level 무변경.
6. **카드 헤더 verbatim**: MUST 1–6 카드의 `### ▣ MUST [N] — ...` 헤더 텍스트는 일체 변경 없음(Splice Verification Table anchor 보호).

---

## Final v3 All-Pass Checklist  [EXPERT_INFERENCE, v3]

*(이 섹션은 compiler-only. Phase 5 렌더링 대상 아님.)*

| # | 검증 항목 | 결과 |
|---|---|---|
| 1 | §5 Critical Blow 단일화: `**치명적 타격(Critical Blow)**` 레이블이 혼동쌍 #1에만 1개 존재하는가? 나머지 혼동쌍(#2, #3, #4)에는 없는가? | ✅ PASS — 혼동쌍 #1 전용 단일 행 확인, #2–#4 없음 |
| 2 | §2 MUST 1–6 전체: 각 카드에 체화 꿀팁 또는 동등한 다축 실천 블록이 있는가? | ✅ PASS — 6개 카드 전원 체화 꿀팁 보유; MUST 5는 Practice Lens 추가 보유 |
| 3 | 기존 Memory Hooks, Embodiment Tips, Critical Blow, 거장의 한 줄, 모델-빌딩 워크플로우, Apex Concept 전면 보존되었는가? | ✅ PASS — PART A 내용 무변경 |
| 4 | [EXPERT_INFERENCE, v3] 이외 새 도구명·소프트웨어 임계값·규제 주장이 추가되지 않았는가? | ✅ PASS |
| 5 | 소스 페이지 태그 ([p.XX], [pp.XX–YY], [확인 필요]) 추가·삭제·이동 없음이 확인되는가? | ✅ PASS |
| 6 | PART A 과학 내용·수식·임상 예시가 변경되지 않았는가? | ✅ PASS — PART A 무변경 |
| 7 | PART B Audit Guardrails (B5), Crucible Guardrails (B6), 금지 복원 목록 (B7)을 위반하지 않았는가? | ✅ PASS |
| 8 | v3 Change Log (B12) 및 본 Checklist 첨부가 완료되었는가? | ✅ PASS |

> **v3 Surgical Patch — All 8 checks PASS.**  
> 과학 내용 무변경. Critical Blow 단일화 확인. Practice Brief 전 카드 충족. PART B 메타데이터·로그·체크리스트 only 갱신.

---

## v3.1 Final Checklist

*(이 섹션은 compiler-only. Phase 5 렌더링 대상 아님.)*

| # | 검증 항목 | 결과 |
|---|---|---|
| 1 | PART A readability improved (Learner Navigation 한국어화 + MUST 카드 first-use gloss 6개 + 영어 관용구 한국어 정제 2개) | ✅ PASS |
| 2 | Scientific content unchanged (모든 정의·도출·결론·임상 예시·실험 데이터 anchor 보존) | ✅ PASS |
| 3 | Equations preserved (MathJax inline·display 수식 모두 verbatim 보존; Eq.4:16 ~ Eq.5:11, Eq.4:46 ~ Eq.4:57, AIC/SC, $F^*$, $F_{LOF}$, CV%, $r$ 등) | ✅ PASS |
| 4 | Page tags preserved ([p.352], [pp.352–353], [pp.354–355], [pp.369–391], [pp.399–405], [p.확인 필요], [확인 필요 — pp.365–367 업로드 부재] 등 모든 형식 보존; 신규 태그 0건) | ✅ PASS |
| 5 | Figure markers preserved (`<!-- FIGURE_POINTER -->` 5개, `<!-- FIGURE_SCHEMATIC -->` 2개, 모든 marker brief 본문 verbatim 보존) | ✅ PASS |
| 6 | Source-boundary preserved ([CRUCIBLE_DERIVED], [TEXTBOOK_DERIVED], [EXPERT_INFERENCE, v3], [교과서 외 *] 라벨 모두 위치·표기 보존; B5 Audit Guardrails·B6 Crucible Guardrails·B7 Forbidden Restorations 일체 위반 없음) | ✅ PASS |
| 7 | HTML-readiness preserved (모든 HTML compiler marker `<!-- MASTER LENS -->`·`<!-- TRENCH -->`·`<!-- CONFUSION -->`·`<!-- SELF-TEST -->`·`<!-- RECAP -->`·`<!-- ANCHOR -->`·`<!-- ANNOTATION -->` 위치·구문 보존; PATCH MODE Splice Verification Table의 7개 anchor 모두 verbatim 일치) | ✅ PASS |
| 8 | Ready for Phase 5 HTML compilation (B1 Compilation Contract·B2 Figure Rendering·B3 Page Tag Rules·B4 Marker Mapping·B5–B7 Guardrails 모두 충족; v3.1 패치는 산문 가독성 개선에 국한되어 Phase 5 렌더링 파이프라인에 영향 없음) | ✅ PASS |

> **v3.1 Korean Readability Patch — All 8 checks PASS.**  
> PART A 한국어 독해성 개선 완료. 과학 내용·수식·페이지 태그·figure marker·source-boundary·HTML readiness 일체 보존. Phase 5 HTML compilation 진입 준비 완료.

---

## v3.2 Final Checklist

*(이 섹션은 compiler-only. Phase 5 렌더링 대상 아님.)*

| # | 검증 항목 | 결과 |
|---|---|---|
| 1 | PART A learner-facing readability further improved (§1 후행 지식 한영 병기, §5 혼동쌍 표 영어 라벨 한영 병기 7개, §7 Q1 정답 영어 단어 나열 한영 병기) | ✅ PASS |
| 2 | Career-critical pharmacometrics terms 처리 일관성 (`한글(English)` 병기 형태 유지) | ✅ PASS — 적용된 모든 용어가 한영 병기 형식 준수 (잔차 진단, 파라미터 정밀도, 설계 피드백, 원전 교정, AIC/SC 적용 경계, 결정적 예, 원전 서술, 원전 anchor 위치, 잘못된 최종 추정값, 원치 않는 국소 최솟값, 생리학적으로 불가능한 parameter 값) |
| 3 | Scientific content unchanged (모든 정의·도출·결론·임상 예시·실험 데이터 anchor·수치 보존) | ✅ PASS |
| 4 | Equations preserved (MathJax inline·display 수식 모두 verbatim 보존; Eq.4:16 ~ Eq.5:11, Eq.4:46 ~ Eq.4:57, AIC/SC, $F^*$, $F_{LOF}$, CV%, $r$ 등) | ✅ PASS |
| 5 | Page tags preserved (모든 [p.XX], [pp.XX–YY], [pp.XX, YY], [확인 필요], [p.확인 필요] 형식 보존; 신규 태그 0건; 기존 태그 위치 0건 이동) | ✅ PASS |
| 6 | Source labels preserved ([CRUCIBLE_DERIVED], [TEXTBOOK_DERIVED], [EXPERT_INFERENCE, v3], [교과서 외 *] 라벨 모두 위치·표기 보존) | ✅ PASS |
| 7 | Figure markers preserved (`<!-- FIGURE_POINTER -->` 5개, `<!-- FIGURE_SCHEMATIC -->` 2개, 모든 marker 내부 영문 brief 일체 verbatim 보존 — v3.2 prompt 명시 규칙 준수) | ✅ PASS |
| 8 | HTML compiler markers preserved (모든 `<!-- MASTER LENS -->`·`<!-- TRENCH -->`·`<!-- CONFUSION -->`·`<!-- SELF-TEST -->`·`<!-- RECAP -->`·`<!-- ANCHOR -->`·`<!-- ANNOTATION -->` 위치·구문 보존) | ✅ PASS |
| 9 | Standard abbreviations preserved (CL, V, Vd, AUC, Cmax, Tmax, ka, ke0, EC50, IC50, Emax, Imax, IIV, BSV, RUV, OMEGA, SIGMA, ETA, EPS, OFV, VPC, GOF, CWRES, NONMEM, NCA, WRSS, AIC, SC, MM, PCA, PK, PD, IRLS, OLS, LOF, df, SE, CV%, F-test 영어 단독 유지) | ✅ PASS |
| 10 | Mastery Augmentation Layer 위치·본문 보존 (Phase 4D 7개 entries + Phase 4E 8개 entries — 거장의 한 줄, 체화 꿀팁 6개, Critical Blow row, 강화된 Memory Hook 모두 v3.2에서 무변경) | ✅ PASS |
| 11 | PATCH MODE Splice Verification Table의 7개 anchor 모두 verbatim 일치 (각 MUST Recap의 첫 문장이 v3.2에서 변경되지 않음) | ✅ PASS |
| 12 | Section/card structure unchanged (§1, §2 MUST 1–6, §5 혼동쌍 #1–#4, §7 Q1–Q9, §8 A–E 구조 무변경) | ✅ PASS |
| 13 | No new scientific claims, no new numbers, no new examples, no new page tags, no new figures, no new source labels added | ✅ PASS |
| 14 | Code blocks not translated (본 세션 PART A에는 NONMEM/R/Python 코드 블록 없음 — 해당 없음으로 자동 PASS) | ✅ PASS |
| 15 | PART B guardrails (B5 Audit Guardrails, B6 Crucible Guardrails, B7 Forbidden Restorations) 일체 위반 없음 | ✅ PASS |
| 16 | PART B 변경은 v3.2 metadata에 국한 (B1 contract clause, Phase 4E Certification row, B8 splice integrity note, B9 C14 row, B10 micro-patch entry, B11 deferred candidates, B12-B Change Log, 본 Final Checklist만 추가/수정) | ✅ PASS |
| 17 | HTML-readiness preserved (Phase 5 PATCH MODE Splice Verification Table 유효성 유지; v3.2 패치 영역과 splice anchor 분리 확인됨) | ✅ PASS |
| 18 | Ready for Phase 5 HTML compilation (v3.2 패치는 산문 가독성 개선에 국한되어 Phase 5 렌더링 파이프라인에 영향 없음) | ✅ PASS |

> **v3.2 Korean-Dominant Readability Patch — All 18 checks PASS.**  
> PART A 한국어 중심 독해성 추가 정제 완료. 과학 내용·수식·페이지 태그·figure marker·source label·HTML compiler marker·표준 약어·Mastery Augmentation Layer·Phase 5 splice anchor 일체 보존. Phase 5 HTML compilation 진입 준비 완료.

---

## v3.3 Final Checklist

*(이 섹션은 compiler-only. Phase 5 렌더링 대상 아님.)*

| # | 검증 항목 | 결과 |
|---|---|---|
| 1 | §2 MUST 1–6 카드 6개 모두 Practice Brief blockquote 보유 | ✅ PASS — MUST 1 (Δ-V3.3-01), MUST 2 (Δ-V3.3-02), MUST 3 (Δ-V3.3-03), MUST 4 (Δ-V3.3-04), MUST 5 (Δ-V3.3-05), MUST 6 (Δ-V3.3-06) 모두 추가 완료 |
| 2 | 라벨 `[EXPERT_INFERENCE, v3.3]` 일관성 | ✅ PASS — 6개 Practice Brief 모두 동일 라벨 사용; v3 또는 v3.2 라벨 혼합 없음 |
| 3 | 4축(왜 알아야 / 흐름상 역할 / 체화 꿀팁 / 실무 활용) 모두 충족 | ✅ PASS — 6개 카드 모두 4축 구조 일관 적용 |
| 4 | v3.2 본문·수식·페이지 태그·marker 무변경 | ✅ PASS — 모든 §1·§2·§5·§7·§8 학습자 본문, 수식, [p.XX]/[pp.XX–YY]/[확인 필요] 태그, source label, FIGURE_*/HTML compiler marker byte-level 보존 |
| 5 | MUST 1–6 카드 헤더 텍스트 verbatim | ✅ PASS — 6개 카드 헤더(`### ▣ MUST 1 — 초기값 획득의 실전 기술 (Initial Estimate Acquisition)` 등) 모두 무변경; Splice Verification Table anchor 보호 |
| 6 | §8D GOF Checklist locked from Table 4.9 표 무변경 | ✅ PASS — 5개 행 본문(biological relevance, fitted curve mimic, parameters precision, residuals lack of systematic deviation, residual plots random scatter) byte-level 보존 |
| 7 | 새 페이지 태그·약물·수치·외부 reference 0건 | ✅ PASS — 6개 Practice Brief 모두 카드 본문에 이미 존재하는 개념·예시·식·수치만 사용; 추가 도입 0건 |
| 8 | Phase 5 HTML compile go | ✅ PASS — B4 marker mapping에 Practice Brief 행 신설, Phase 5 렌더링 가이드 명시 완료 |
| 9 | MUST 3 [⚡ Apex Concept] 배지 + F-test validity 본문 무변경 | ✅ PASS — 배지 위치, A. Formal Definition, Eq.4:54·4:55, B. Valid/Invalid/Conditionally valid examples, C-2 Plausible Fallacy, D. AIC/SC boundary, E. WRSS vs −2·log likelihood 모두 byte-level 보존 |
| 10 | §5 혼동쌍 4개 표·잠금 일체 무변경 | ✅ PASS — 혼동쌍 #1 Critical Blow row, 혼동쌍 #2 Memory Hook (CRUCIBLE_DERIVED 강화판), 혼동쌍 #3·#4 표 일체 byte-level 보존 |
| 11 | §7 Q9 Boss Dilemma + Q1–Q8 정답 방향 무변경 | ✅ PASS — Q1–Q9 문제·정답·SR 태그 byte-level 보존 |
| 12 | PART B B8 Splice Verification Table v3.2와 동일 | ✅ PASS — 7개 anchor (각 MUST Recap의 verbatim opening sentence) 모두 변경 없음; v3.3 splice integrity note만 추가 |
| 13 | 카드 본문 내용만 사용 (새 사실 도입 없음) | ✅ PASS — 6개 Practice Brief 모두 자체 검증 통과; 카드 외 새 약물/수치/페이지 태그/외부 reference 0건 |
| 14 | PART B B11 Mastery Augmentation Log Phase 4F entries #17–#22 추가 | ✅ PASS — 6개 entries 추가, Phase 4D #1–7 + Phase 4E #8–16과 분리된 별도 섹션으로 정리 |
| 15 | PART B B12-C v3.3 Change Log 신설 | ✅ PASS — Δ-V3.3-01 ~ Δ-V3.3-06 entries, 패치 범위 제한 선언, v3.3 적용 원칙 6항 모두 포함 |
| 16 | Phase 4E Certification 표에 Practice-Brief Uniformity Certificate (v3.3) 행 신설 | ✅ PASS — PASS 등급으로 신설 |
| 17 | B9 Zero-Omission Matrix C15 row 추가 | ✅ PASS — v3.3 패치 커버리지 명시; PRESENT, No action |
| 18 | Ready for Phase 5 HTML compilation | ✅ PASS — v3.3 패치는 §2 MUST 카드 끝에 균일 Practice Brief blockquote 6개 추가에 국한되어 Phase 5 렌더링 파이프라인에 영향 없음; B4 marker mapping에 dedicated 스타일 가이드 추가됨 |

> **v3.3 Practice-Brief Uniformity Patch — All 18 checks PASS.**  
> §2 MUST 1–6 카드 6개에 균일한 4축 실무 체화 요약(Practice Brief) blockquote 추가 완료. v3.2 source-fidelity byte-level 보존. §8D GOF Checklist·MUST 3 Apex Concept·§5 혼동쌍 4개 표·§7 Q9 Boss Dilemma·MUST 1–6 카드 헤더 일체 무변경. 새 페이지 태그·수식·약물·수치·외부 reference 0건 도입. Phase 5 HTML compilation 진입 준비 완료.

---

## Final Certification Summary (v3.3)

| Certificate | Status | Basis |
|---|---|---|
| Practice-Brief Uniformity Certificate (v3.3) | PASS | All 6 §2 cards (MUST 1–6) now carry a uniform 4-axis Practice Brief blockquote. No new page tags, equations, numerical anchors, drug examples, or external claims introduced. v3.2 source-fidelity preserved byte-level. §8D GOF Checklist locked from Table 4.9 unchanged. |
| Korean-Dominant Readability Certificate (v3.2, preserved) | PASS | General learner-facing English prose converted to Korean where possible; career-critical terms retained as Korean-English paired expressions. |
| Scientific Preservation Certificate | PASS | No scientific content, equation, number, example, page tag, or source label changed. |
| Marker Integrity Certificate | PASS | All figure markers, compiler markers, anchors, and section/card structures preserved. MUST 1–6 card headers verbatim. |
| HTML-Readiness Certificate | PASS | Phase 5 compatibility preserved; B4 marker mapping updated with Practice Brief styling guide; no HTML/Mermaid/SVG generated. |

---

*`15_html_compile_input_master_v3.3.md` — Practice-Brief Uniformity Patch Editor, 2026-05-08*  
*v3.2 base: Korean-Dominant Readability Patch Editor, 2026-05-08*  
*v3.1 base: Independent Pharmacometrics Master Reviewer & Korean Readability Patch Editor, 2026-05-07*  
*v3 base: Independent Pharmacometrics Master Reviewer & Surgical Patch Editor, 2026-05-07*

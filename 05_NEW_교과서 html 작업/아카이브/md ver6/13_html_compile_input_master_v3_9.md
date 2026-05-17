# 세션 13(Session 13) — 개체 간 변이(IIV/BSV)와 공변량 모델링 — v3.8

---

## 임상 장면 — 같은 평균, 다른 환자

CpD 566 µg을 5시간 IV infusion으로 받은 12명에서 total `CL`은 11.4 L·h⁻¹(CV 28%), 그러나 unbound `CL_u`는 720 L·h⁻¹(CV 9%)였습니다. 동시에 $f_u=0.016\pm0.0049$였고, 안전 경계는 total C $>50$ µg·L⁻¹로 회피해야 했습니다. `[G&W p.704–709]`

이 장면에서 물어야 할 질문은 "평균 CL이 얼마인가"가 아닙니다. **이 변이가 (1) total 좌표계의 단백결합 변이인지, (2) unbound 좌표계의 진짜 처분 변이인지, (3) 별도 PD 반응 변이인지** 입니다.

---

## 학습 경로

| 단계 | 섹션 | 목적 |
|---:|---|---|
| 1 | §1 | 변이 축 전체 지도 |
| 2 | §2 C1 | $\theta$/$\eta$/$\varepsilon$ · $\omega^2$/$\sigma^2$ 분리 |
| 3 | §2 C2 | 공변량 해석 전에 잔차 오차 구조부터 확정 |
| 4 | §2 C3 | 진짜 공변량 설명과 total/unbound 좌표계 변환 구분 |
| 5 | §2 C4 | 매끄러워 보이는 IIV 안의 불연속 유전 하위구조 |
| 6 | §5 | 혼동쌍 해소 |
| 7 | §7–§8 | 자기 테스트 + PopPK 커리큘럼 통합 |

**시작 전 확인**: CL, V, $t_{1/2}$, protein binding, NCA, 기본 NONMEM control-stream.

**이 세션을 마친 뒤 본인 언어로 설명할 수 있어야 합니다**:
- $\theta$만으로는 왜 부족한지
- 잔차 오차 모델 오지정이 왜 가짜 IIV 또는 가짜 공변량 신호를 만드는지
- PK50이 단지 "$f_u$가 $\omega^2$를 줄였다"가 아니라 **좌표계 변환과 재모수화** 수업인 이유
- 이봉형 농도/$\eta$ 분포를 매끄러운 로그정규 IIV 하나로 가리면 안 되는 이유

---

<!-- SLIDE_START: §1 | title: 세션 헤더 및 로드맵(Session Header & Roadmap) -->
<!-- SECTION_CORE: SC-01 -->

## §1 — 세션 헤더 및 로드맵(Session Header & Roadmap)

**Session 13 — 개체 간 변이(IIV / BSV)와 공변량 모델링**
*Source: R&T 5e Ch.12 (p.361–392) + Ch.13 (p.393–410); G&W 5e Ch.4 일부 (p.333–352) + PK50 (p.704–710)*

### ASCII 레이어 개념 지도

```text
Layer 1 — 무엇인가?
  θ = 모집단 중심
  η = 개인 위치
  ε = 관측 잔차
  IIV / IOV / RUV = 서로 다른 변이 그릇

Layer 2 — 어떻게 계산되는가?
  Yij = f(θ, ηi, xij) + g(θ, ηi, xij)εij
  CLi = CL·exp(ηi)
  residual error = additive / proportional / exponential
  covariate model = θ 구조로 설명 가능한 변이 이동
  reparameterization = total ↔ unbound 좌표계 변환

Layer 3 — 언제, 왜 중요한가?
  잔차 모델 오류 → ω² 오염 → 가짜 공변량
  total/unbound 혼동 → 용량·안전성 좌표계 불일치
  bimodal η → 유전 하위군 또는 phenotype 구조 의심
  보고서 방어 → θ, Ω, Σ, covariate, VPC의 일관성
```

### 지식 그래프 위치

```text
[선행: 1·2구획, CL/V/t1/2, 단백결합, NONMEM 기초]
        → [이 세션: IIV/IOV/RUV, θ/η/ε, Ω/Σ, 공변량, 유전 하위구조]
        → [후속: FOCE/FOCE-I, GOF/CWRES, η-EBE, shrinkage, stepwise covariate selection]
```

🧭 **읽는 순서:**
카드 1 (C1): 평균 파라미터만으로는 왜 개별 환자를 설명할 수 없는가?
카드 2 (C2): 잔차 오차를 먼저 고정하지 않으면 왜 공변량 신호가 가짜가 되는가?
카드 3 (C3): 공변량은 $\omega^2$를 줄이는 기술인가, 생리학적 좌표계를 다시 배정하는 일인가?
카드 4 (C4): 매끄러운 IIV처럼 보이는 분산 뒤에 유전형/표현형 하위군이 숨어 있을 때 어떻게 알아차리는가?

### 핵심 아이디어(Big Idea)

NONMEM 혼합효과 모델(mixed-effects model; 고정효과와 무작위효과를 함께 추정하는 구조)의 본질은 관측값을 **$\theta$(인구 평균), $\eta$(개체 편차), $\varepsilon$(잔차 noise)** 로 나누어 보고, 그 흔들림의 크기인 **$\omega^2$와 $\sigma^2$**를 따로 추정하는 것입니다. 공변량은 $\omega^2$에 섞여 있던 생리학적 원인을 꺼내는 도구이고, 유전 다형성은 매끄러워 보이는 $\omega^2$ 안에 숨어 있는 불연속 봉우리입니다. `[R&T p.369–373; p.393–410]`

G&W는 이론보다 먼저 데이터의 모양을 보라고 합니다. 그래서 공변량 모델은 control stream에서 시작하지 않습니다. 먼저 spaghetti plot · dose-normalized plot · transformed plot에서 **"어떤 개체들이 왜 갈라지는가"** 를 확인합니다. `[G&W p.334–336]`

> **체화 노트 — Variance Conservation 작업 가설**
> 이 세션 전체를 관통하는 단 하나의 가설은 **보존 법칙**입니다. 같은 데이터셋에서 $\omega^2$와 $\sigma^2$는 같은 총 미설명 변이를 두고 zero-sum으로 경쟁합니다. $\varepsilon$이 흡수하지 못한 분산은 반드시 $\eta$로 새고, 그 반대도 같습니다.
> 그래서 **C1(taxonomy) → C2(잔차 그릇) → C3($\eta$ 안의 설명가능 부분 이동) → C4($\eta$ 분포 모양 점검)** 순서가 결정됩니다. 이 순서를 어기면 NONMEM은 돌아가지만 dose individualization은 무너집니다.

### 로드맵(Roadmap)

```text
C1. θ / η / ε taxonomy
     ↓
C2. residual error model: ε의 형태를 정한다
     ↓
C3. covariate model: ω² 일부를 설명 가능한 생리학으로 옮긴다
     ↓
C4. genetic polymorphism: ω² 안의 불연속 substructure를 드러낸다
```

### 지식 그래프상 위치(Knowledge Graph Position)

| 위치 | 내용 |
|---|---|
| 선행 전제 | 1-구획·2-구획 모델, CL/V/$t_{1/2}$, 단백 결합, NONMEM 기초 syntax |
| 본 세션 | IIV / 시점 간 변이(IOV) / 잔차 미설명 변이(RUV), $\theta$/$\eta$/$\varepsilon$, $\omega^2$/$\sigma^2$, 공변량, 유전형/표현형 변이 |
| 직후 후속 | FOCE / FOCE-I, GOF / CWRES / $\eta$-EBE, shrinkage, stepwise covariate selection |
| 임상 번역 | Bayesian TDM, 용량 개체화, 치료적 창, PopPK 보고서 일관성 |

### IIV / IOV / RUV — 서로 다른 변이 그릇 `[실무 통합, v3.5.3]`

세 그릇을 한 표로 잡고 시작합니다.

| 그릇 | 무엇을 담는가? | 핵심 질문 | 어디에 들어가는가 |
|---|---|---|---|
| **IIV** (inter-individual) | 사람 사이의 **지속적** 차이 — 어떤 개인은 전반적으로 CL이 높고, 다른 개인은 낮음 | 사람마다 지속적으로 다른가? | $\omega^2$ |
| **IOV** (inter-occasion) | 같은 사람 안에서 occasion·period·cycle·visit 간 반복 차이 | 같은 사람 안에서 occasion마다 달라지는가? | occasion-level random effect (별도 분리) |
| **RUV** (residual unexplained) | 관측값 수준의 잔차 — 같은 개인, 같은 occasion, 같은 구조 모델 뒤에도 남는 흔들림 | 관측값 하나하나에서 남는 오차인가? | $\sigma^2$ |

**IOV를 무시하면 일어나는 일**: 같은 사람 안의 occasion별 변화가 IIV 또는 RUV로 잘못 흡수됩니다. 그 결과 $\omega^2$, $\sigma^2$, EBE, shrinkage, covariate signal 해석이 모두 왜곡됩니다. 특히 **repeated period · crossover · cycle-based oncology dosing · TDM 재방문 · enzyme induction/inhibition recovery · adherence fluctuation** 자료에서는 "사람이 다른 것"과 "같은 사람의 occasion이 다른 것"을 반드시 분리해야 합니다.

NONMEM 실무에서 IOV는 occasion-level ETA 또는 occasion-specific random effect로 구현됩니다. 핵심은 `$OMEGA` block을 늘리는 게 아니라 **어느 그릇에 어떤 반복 구조를 담을 것인가** 입니다. 다음 네 가지를 먼저 확인합니다:
- 같은 개인 안의 visit/cycle/period별 systematic shift가 보이는가
- residual plot만으로 설명되지 않는 occasion별 bias가 남는가
- 공변량 효과로 보이는 신호가 사실 occasion imbalance 때문일 가능성이 있는가
- IOV를 넣었을 때 IIV/RUV 또는 covariate effect가 해석 가능해지는가

**한 줄**: IIV는 사람 간 차이, IOV는 같은 사람 안의 occasion 간 차이, RUV는 관측값 수준의 남은 오차.

**§1 요약(Recap)**: 이 세션의 질문은 "사람마다 다르다"가 아닙니다. "그 다름 중 무엇이 $\theta$, 무엇이 $\eta$, 무엇이 $\varepsilon$, 무엇이 공변량인가"입니다.

---

<!-- SLIDE_START: §2 | title: 개념 해부 카드(Concept Anatomy Cards) -->
<!-- SECTION_CORE: SC-02 -->

## §2 — 개념 해부 카드(Concept Anatomy Cards)

---

<!-- SLIDE_START: C1 | title: 변이의 구조적 분해 — θ, η, ε 분류 체계(taxonomy) -->
<!-- SECTION_CORE: SC-03 -->

### C1. 변이의 구조적 분해 — $\theta$, $\eta$, $\varepsilon$ 분류 체계(taxonomy)

> **거장의 시각**
> $\theta$, $\eta$, $\varepsilon$를 단순 기호로 외우면 `$OMEGA`와 `$SIGMA`는 숫자표가 됩니다.
> 어느 변이가 어느 그릇에 들어가는지를 보면, C2의 잔차 모델 · C3의 공변량 · C4의 분포 구조가 한 줄로 연결됩니다.

#### A. 형식적 정의(Formal Definition)

`[교과서 외 구현/통계 번역; 개념 근거: R&T p.369–373]`

$$
\underbrace{Y_{ij}}_{\text{관측값}}
=
\underbrace{f(\boldsymbol{\theta},\boldsymbol{\eta_i},x_{ij})}_{\text{개인 예측}}
+
\underbrace{g(\boldsymbol{\theta},\boldsymbol{\eta_i},x_{ij})}_{\text{오차 스케일}}
\underbrace{\varepsilon_{ij}}_{\text{잔차}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $Y_{ij}$ | 농도 또는 반응 단위 | i번째 개인의 j번째 관측값 | 측정 시점, assay, 실제 노출 |
| $\theta$ | 파라미터별 단위 | 모집단 대표값 | 대상 집단, 모델 구조 |
| $\eta_i$ | 무차원 random effect | 개인이 모집단 중심에서 벗어난 위치 | 생리학, 유전형, 질병 상태, 미포착 공변량 |
| $\varepsilon_{ij}$ | 무차원 또는 관측 단위 | 관측 수준 잔차 | assay error, sampling error, 구조/오차 모델 결함 |
| $\omega^2$ / $\sigma^2$ | 분산 | 개인 간 변이 / 잔차 변이 크기 | 변이 배정, 모델 오지정, 자료 정보량 |

개인 청소율의 지수형 IIV(exponential IIV):

$$
\underbrace{CL_i}_{\text{개인 CL}}
=
\underbrace{CL}_{\text{모집단 CL}}
\cdot
\underbrace{\exp(\eta_i)}_{\text{IIV 배율}}
$$

R&T는 지수형 오차 모델이 CL을 음수로 만들지 않으면서 근사적으로 일정한 변동계수(approximate constant CV)를 주기 때문에 집단 분석에서 자주 쓰인다고 설명합니다. `[R&T p.371]` 작은 $\omega$에서는 $CV(\%) \approx \omega\cdot 100$을 교육용 근사로 씁니다.

> 💡 **세 층 비유** — $\theta$는 지도 위 도시 중심, $\eta$는 각 사람이 그 중심에서 어느 동네에 사는지, $\varepsilon$은 주소를 한 번 찍을 때마다 생기는 GPS 흔들림입니다. 이 세 층을 분리하지 않으면 `$OMEGA`와 `$SIGMA`는 의미 없는 숫자입니다.

⚠️ **헷갈림 방지**: $\omega^2$와 $\sigma^2$는 둘 다 "오차"가 아닙니다. $\omega^2$는 사람 간 지속 차이, $\sigma^2$는 관측값 수준의 잔차 흔들림입니다.

🔑 **코드 독해 순서**: `$OMEGA` 구조 → `$SIGMA` 구조 → `$THETA` 초기값. 이 순서로 보면 모델이 생리학적 상관과 잔차 구조를 어떻게 가정했는지 빠르게 읽힙니다.

#### B. 데이터 앵커(Data Anchor): 평균보다 분포가 먼저입니다

R&T의 **warfarin** 200명에서, 유사한 항응고 효과를 얻기 위한 1일 용량은 넓게 분포합니다. **Nortriptyline** 25 mg tid를 복용한 263명에서 정상상태 농도는 선형 스케일에서는 비대칭(skewed)이지만 로그 스케일에서는 거의 대칭(symmetric)입니다. → 평균만 보면 dose individualization 문제는 해결되는 것이 아니라 **가려집니다.** `[R&T p.362–363]`

G&W도 다중 피험자 자료에서 먼저 개별 프로파일과 통합 자료(pooled data)를 그려 보라고 합니다. Figure 4.2의 spaghetti plot은 같은 dose에서도 일본인 그룹과 백인 그룹의 노출 프로파일이 다를 수 있음을 보여 주며, 오차 막대를 가진 평균 곡선보다 spaghetti plot이 변이를 더 잘 드러냅니다. `[G&W p.335–336]`

**NAD/NPD/population bridge**: NAD(Naive Averaged Data)는 각 시간점의 평균 농도에 모델을 맞춥니다. NPD(Naive Pooled Data)는 모든 관측값을 한 개인의 자료처럼 적합합니다. G&W는 평균 자료 적합이 편향된 파라미터와 변이를 만들 수 있어 피해야 하며, 대안으로 집단 접근법이 필요하다고 합니다. `[G&W p.335–336]`

> 📖 **R&T 5e p.366, Figure 12-6** — 네 가상 약물 청소율의 빈도분포. 같은 평균이라도 CV와 분포 모양이 다르면 개별 용량 결정의 의미가 완전히 달라집니다. 특히 이봉형(bimodal) 분포에서는 평균이 모집단 대표값이 아니라 **가장 덜 그럴듯한 값**이 될 수 있습니다.

#### C. 구조적 필요성(Structural Necessity)

| 상황 | 파라미터 변화 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| $\theta$ 하나만 사용 | 개인별 $\eta$ 미표현 | → | 좁은 치료적 창에서 독성 또는 무효 노출 개인을 설명 못함 `[R&T p.370]` | IIV 구조 명시 |
| 잔차 모델이 산포를 설명 못함 | $\sigma^2$가 $\omega^2$로 새어 나감 | → | 가짜 IIV 또는 가짜 공변량 신호 | C2 잔차 모델 우선 검토 |
| 표준 2단계 분석에 rich sampling 부족 | 구조·분산 파라미터 분리 추정 불안정 | → | sparse data에서 편향 | population analysis로 동시 추정 `[R&T p.369]` |
| OFV만 보고 모델 채택 | $\theta$, $\omega$, $\sigma$ 동시 조정 결과 과해석 | → | 공변량의 생물학적 의미 과대 주장 | LRT/AIC + 진단 plot 병행 `[R&T p.373]` |

OFV는 적합의 언어입니다. 최대 가능도가 $\theta$, $\omega$, $\sigma$를 동시에 조정하여 OFV를 최소화합니다. 내포 모델에서는 $\Delta OFV \geq 3.84$(df=1, α=0.05)가 LRT 기준이고, 비내포 모델에서는 AIC를 씁니다. `[R&T p.373]`

#### D. 경계 조건(Boundary Conditions)

| 경계 조건 | 위반 시 신호 |
|---|---|
| $\eta$ 분포가 단봉형/로그정규여야 함 | 이봉형 히스토그램이면 유전형/표현형 하위군 가능성 `[R&T p.366, p.393–397]` |
| $\varepsilon$가 평균 0, 분산 $\sigma^2$의 무작위 잔차여야 함 | 잔차 추세가 남으면 구조 모델 또는 오차 모델이 변이의 원인을 설명 못한 것 `[R&T p.372]` |
| 희소 자료도 같은 모집단에서 왔다고 볼 수 있어야 함 | 이질적 모집단이 섞이면 모집단 평균과 $\omega^2$가 모두 왜곡 |
| 공변량이 식별 가능해야 함 | 데이터가 정보를 주지 않으면 파라미터는 숫자로만 존재 `[G&W p.348–351]` |

#### E. 실무 확장: EBE와 shrinkage는 $\eta$를 "보았다"는 착각을 만들 수 있습니다

EBE(empirical Bayes estimate; 경험적 베이즈 추정치)는 모집단 수준 파라미터($\theta$, $\omega^2$, $\sigma^2$)와 그 개인의 관측치를 함께 사용한 **사후추정치**입니다. 즉 EBE는 개인의 "참값"이 아니라, 모델 가정과 그 사람이 제공한 자료의 양·질이 허용하는 범위 안에서 나온 조건부 추정치입니다. **Shrinkage**는 그 개인이 제공한 정보가 부족할 때 EBE가 모집단 평균(0) 쪽으로 끌려가는 현상입니다.

| 연결 지점 | 실무 해석 |
|---|---|
| 높은 shrinkage | EBE-vs-covariate plot과 ETA diagnostic의 분해능이 약해집니다 |
| 약한 공변량 신호 | 생물학 부재가 아니라 정보 부족, residual misspecification, ETA–epsilon leakage, estimation approximation의 결과일 수 있습니다 |
| 공변량 모델링 | 진짜 생물학적 신호와 estimation artifact를 분리해야 합니다 |

기억 고리: **EBE plot은 현미경이 아니라, 모델·자료·추정법이 함께 만든 그림자입니다.**

```yaml
aliases: [IIV, BSV, NLME taxonomy, theta-eta-epsilon]
tags: [pharmacometrics/poppk, nonmem/omega, statistics/nlme]
source: "R&T p.369-373; G&W p.335-336; G&W PK50 p.704-708"
```

> **C1 체화 핵심**
> ① `개인별 CL·V가 평균에서 지속적으로 벗어날 때` → $\eta$와 $\omega^2$가 지배
> ② `같은 개인의 관측값이 예측 주변에서 흔들릴 때` → $\varepsilon$와 $\sigma^2$가 지배
> ③ `EBE plot을 개인 참값처럼 읽을 때` → shrinkage와 자료 정보량 먼저 점검
> ⚡ `잔차 실패를 IIV 성공으로 해석` → 공변량 탐색이 가짜 생리학을 만들어 dose individualization 실패

---

<!-- SLIDE_START: C2 | title: 잔차 오차 모델 — additive / proportional / exponential -->
<!-- SECTION_CORE: SC-04 -->

### C2. 잔차 오차 모델 — 가법형(additive) / 비례형(proportional) / 지수형(exponential)

> **앞 카드에서 이 카드로**: C1에서 $\eta$와 $\varepsilon$의 그릇을 분리했으므로, 이제 관측 수준 잔차가 어떤 스케일로 흔들리는지 먼저 정해야 합니다.

> **거장의 시각**
> 잔차 모델을 measurement noise의 부록으로만 보면, $\varepsilon$이 설명하지 못한 패턴이 $\eta$와 공변량 신호로 위장합니다.
> $\varepsilon$의 스케일을 먼저 정하면, C3에서 남은 $\omega^2$ 중 무엇이 진짜 생리학인지 보이기 시작합니다.

#### A. 형식적 정의(Formal Definition)

R&T가 제시하는 잔차 변이 모델은 세 가지입니다. `[R&T p.372]`

| 모델 | 식 | 해석 |
|---|---|---|
| 가법형(Additive) | $\underbrace{Y}_{\text{관측값}}=\underbrace{F}_{\text{예측값}}+\underbrace{\varepsilon}_{\text{절대오차}}$ | 절대오차가 농도와 무관하게 거의 일정 |
| 비례형(Proportional) | $\underbrace{Y}_{\text{관측값}}=\underbrace{F}_{\text{예측값}}(1+\underbrace{\varepsilon}_{\text{상대오차}})$ | 상대오차/CV가 농도 범위 전반에서 거의 일정 |
| 지수형(Exponential) | $\underbrace{Y}_{\text{관측값}}=\underbrace{F}_{\text{예측값}}\underbrace{\exp(\varepsilon)}_{\text{오차 배율}}$ | 양수 보장; 로그 영역에서 가법 오차가 됨 |

로그 변환 후 지수형 오차는 가법형이 됩니다. `[R&T p.373]`

$$
\underbrace{\ln Y}_{\text{로그 관측값}}
=
\underbrace{\ln F}_{\text{로그 예측값}}
+
\underbrace{\varepsilon}_{\text{로그 잔차}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $Y$ | 농도 또는 반응 단위 | 실제 관측값 | assay, sampling, 구조 모델 적합도 |
| $F$ | $Y$와 동일 | 모델 예측값 | $\theta$, $\eta$, 투여/시간 정보 |
| $\varepsilon$ | 오차 모델별 단위 | 관측 수준 잔차 | assay SD/CV, LLOQ, residual misspecification |
| $\sigma^2$ | 분산 | 잔차 변이 크기 | 오차 구조, 측정 정확도, 모델 누락 패턴 |

> 💡 **오차 스케일 한눈** — additive는 "몇 단위 틀리는가", proportional은 "몇 % 틀리는가", exponential은 "로그 스케일에서 얼마나 틀리는가"를 묻습니다.

⚠️ **헷갈림 방지**: combined/mixed residual model은 실무 NONMEM에서 자주 쓰이지만, R&T p.372가 직접 열거한 출처 모델은 가법형/비례형/지수형입니다. 따라서 결합형 모델은 source-derived가 아니라 구현 번역으로만 둡니다.

🔑 **잔차 우선 규칙**: 공변량을 넣기 전에 CWRES vs PRED/TIME에서 residual pattern이 구조적이지 않은지 먼저 확인합니다.

#### B. 코드 구조(Code Structure)

```nmtran
; [교과서 외 구현 번역]
$ERROR
IPRED = F                                       ; individual prediction을 잔차 모델의 중심으로 둔다
W     = SQRT((THETA(3)*IPRED)**2 + THETA(4)**2) ; 비례 성분과 가법 성분을 잔차 스케일 W로 결합
Y     = IPRED + W*EPS(1)                        ; 표준 잔차 EPS(1)를 W만큼 확대한 뒤 관측값 생성
```

$$
\underbrace{Y}_{\text{관측값}}
=
\underbrace{IPRED}_{\text{개인 예측}}
+
\overbrace{\sqrt{\underbrace{(\theta_{prop}\cdot IPRED)^2}_{\text{비례 성분}}+\underbrace{\theta_{add}^2}_{\text{가법 성분}}}}^{\text{잔차 스케일}}
\underbrace{\varepsilon}_{\text{표준 잔차}}
$$

> 💡 **W의 역할**: combined model의 $W$는 카메라 흔들림 보정 장치처럼 작동합니다. 어두운 영역(LLOQ 근처)의 절대 흔들림과 밝은 영역(고농도)의 상대 흔들림을 한 렌즈로 동시에 보정합니다.

이 코드는 비례 성분과 가법 성분을 하나의 `W`로 합친 구현입니다. 하지만 source-locked 본문의 핵심은 코드가 아니라 **잔차가 무작위, 평균 0, 분산 $\sigma^2$이어야 한다**는 R&T의 조건입니다. `[R&T p.372]`

#### C. 구조적 필요성(Structural Necessity)

잔차 모델 결정은 공변량 선택보다 반드시 앞서야 합니다. 예를 들어 고농도에서 잔차 산포가 커지는 자료에 가법 오차만 쓰면, 모델은 그 산포를 설명하려다 $\omega^2$를 과대 추정하거나 가짜 공변량 신호를 만듭니다. 반대로 LLOQ 근처 절대오차가 큰 자료에 비례 오차만 쓰면, 저농도 잔차 패턴이 체계적으로 남습니다.

R&T는 잔차 변이가 완전히 무작위여야 하며, 그렇지 않으면 구조 모델 또는 오차 모델이 중요한 변이의 원인을 설명하지 못한 것이라고 명시합니다. `[R&T p.372]`

| 상황 | 파라미터 변화 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| 고농도에서 residual spread 증가 | $\sigma^2$ 구조 부적합, $\omega^2$ 과대 가능 | → | 가짜 IIV 또는 가짜 공변량 | 비례/지수형 검토 |
| LLOQ 근처 절대오차 큼 | proportional-only가 저농도 spread를 설명 못함 | → | $\omega^2$(CL) inflate, leakage funnel | additive 또는 combined 성분 검토 |
| 농도 dynamic range ≥ 2 log | 로그 스케일 오차 구조 필요 | → | 원스케일 잔차 추세 | log-transform + additive on log scale 검토 |
| residual trend 잔존 | 구조/오차 모델 미설명 | → | covariate artifact | 공변량 전에 residual model 재검토 |

#### D. 경계 조건(Boundary Conditions)

| 상황 | 권장 사고 흐름 |
|---|---|
| 농도 범위가 좁고 측정 SD가 거의 일정 | 가법형 검토 |
| 넓은 농도 범위와 일정 CV 측정 | 비례형 또는 지수형 검토 |
| 여러 자릿수(order of magnitude)의 자료 | 자연로그 변환 + 변환된 오차 모델 `[R&T p.373; G&W p.337–339]` |
| 잔차 추세가 남음 | 공변량 전에 구조/오차 모델부터 재검토 |

> 📖 **R&T 5e p.371, Figure 12-12** — 등분산성(homoscedastic) vs 이분산성(heteroscedastic) 파라미터 변이. 가법형·비례형·지수형 오차 모델은 식만 보면 서로 다른 문법처럼 보입니다. 이 그림은 잔차 산포가 일정한지, 예측값 크기에 따라 커지는지를 눈으로 구분해 줍니다.

#### E. 한계 및 진단 시그니처

- Shrinkage 공식, 20–30% 임계, Savic & Karlsson 2009는 이 PDF 범위 밖입니다. 본 세션에서는 `[교과서 외 후속 구현 지식]`으로만 남깁니다.
- 희소 표본에서 $\eta$-EBE와 잔차 플롯을 해석할 때는, 낮은 shrinkage와 정규분포처럼 보이는 $\eta$ 히스토그램을 좋은 모델의 증거로 단정하지 마세요. 데이터가 EBE를 실제로 식별할 수 있었는지를 먼저 물어야 합니다.

> 💼 **실무 인사이트** — C2에서 한 가지만 외운다면 "**$\varepsilon$의 실패는 $\eta$의 성공처럼 보입니다**"입니다. 잔차 모델을 틀리면 공변량 모델은 정교해지는 게 아니라 정교하게 틀립니다.

> **진단 시그니처 1 — `ω²–σ² Leakage Funnel`**
> **시그니처**: proportional-only RUV를 LLOQ-rich data(저농도 관측이 많은 자료)에 쓰면, $\omega^2$(CL)이 비현실적으로 inflate되고 CWRES vs PRED plot에서 LLOQ 근처 funnel 모양과 $\eta$-shrinkage spike가 동시에 나타납니다.
> **메커니즘**: 저농도에서 절대오차가 큰 자료에 proportional error만 쓰면 잔차가 설명 못한 spread가 $\omega^2$로 새어 가짜 IIV를 만듭니다. C1의 보존 법칙이 실시간으로 작동하는 장면입니다.
> **꿀팁**: "$\omega^2$이 너무 크다"고 느낄 때 가장 먼저 의심할 것은 추가 covariate가 아니라 **잔차 모델 좌표계**입니다. CWRES plot의 funnel은 covariate 검색이 아니라 RUV 재구성을 가리킵니다.
> **실무 활용**: assay LLOQ가 관측 범위 하단에 가까우면 mixed residual로 a priori 시작하고, additive component는 assay validation 보고서의 SD에 a priori-tied하게 둡니다. post-hoc model selection 인상을 피하려면 mixed 채택 근거(assay characteristic, sampling design)를 모델 선택 시점에 동시 기록합니다.

```yaml
aliases: [RUV, residual error, sigma, additive error, proportional error]
tags: [pharmacometrics/nonmem, statistics/residuals]
source: "R&T p.371-373; G&W p.337-339"
```

> **C2 체화 핵심**
> ① `고농도에서 잔차 산포가 커질 때` → proportional/exponential error가 지배
> ② `LLOQ 근처 절대오차가 클 때` → additive 또는 combined 성분이 지배
> ③ `공변량 탐색 전 funnel이 보일 때` → covariate가 아니라 residual model을 먼저 수정
> ⚡ `ε 실패를 η 신호로 해석` → $\omega^2$ inflate → 가짜 covariate → VPC/CWRES 불일치

---

<!-- SLIDE_START: C3 | title: 공변량 모델링 — CrCl, fu, 재모수화(reparameterization) [⚡ Apex Concept] -->
<!-- SECTION_CORE: SC-05 -->

### C3. 공변량 모델링 — CrCl, $f_u$, 재모수화(reparameterization) `[⚡ Apex Concept]`

> **앞 카드에서 이 카드로**: C2에서 $\varepsilon$의 좌표계를 잠갔으므로, 이제 남은 $\omega^2$ 중 어떤 부분을 생리학적 설명변수로 옮길 수 있는지 판단합니다.

> **거장의 시각**
> 💢 **흔한 오해**: 공변량은 $\omega^2$를 줄여 OFV를 개선하는 통계적 장치다.
> ✅ **실제는**: 공변량 모델링은 $\omega^2$에 섞인 생리학을 $\theta$ 구조로 재배정하고, total/unbound 재모수화는 같은 자료를 다른 좌표계로 다시 읽는 작업이다.
> 🎯 **체화할 직관**: C3의 질문은 "줄었는가"가 아니라 "어느 좌표계에서 무엇이 설명되었는가"입니다.

#### A. 형식적 정의(Formal Definition)

공변량 모델링은 $\omega^2$을 **줄이는** 기술이 아닙니다. 더 정확히는 $\omega^2$에 섞인 생리학을 분리해 **이름을 붙이는** 작업입니다. R&T의 크레아티닌 청소율 예시는 신청소율의 생리학을 $CL_i$에 연결하고, G&W PK50은 $f_u$(fraction unbound)가 total parameter variability의 일부를 설명함을 보여 줍니다. `[R&T p.369–371; G&W p.706–709]`

R&T는 크레아티닌 청소율이 신청소율의 개체 간 차이를 설명하는 공변량이 될 수 있다고 합니다. 예시 구조: `[R&T p.369–371]`

$$
\underbrace{CL_i}_{\text{개인 CL}}
=
\underbrace{\theta_1}_{\text{기저 CL}}
+
\underbrace{\theta_2\cdot GFR_i}_{\text{GFR 설명분}}
+
\underbrace{\eta_i}_{\text{남은 편차}}
$$

NONMEM 구현에서는 흔히 다음과 같은 중심화 공변량 형태를 씁니다.

```nmtran
; [교과서 외 구현 번역]
CL = THETA(1) * (CRCL/90)**THETA(2) * EXP(ETA(1)) ; CRCL=90 기준 CL에 신기능 배율과 남은 IIV를 곱한다
```

$$
\underbrace{CL_i}_{\text{개인 CL}}
=
\underbrace{\theta_1}_{\text{기준값}}
\cdot
\overbrace{\left(\frac{CRCL_i}{90}\right)^{\theta_2}}^{\text{신기능 배율}}
\cdot
\underbrace{\exp(\eta_i)}_{\text{남은 IIV}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $CL_i$ | L·h⁻¹ | 개인 청소율 | 신기능, 간기능, 체중, 유전형, 병태 |
| $\theta_1$ | L·h⁻¹ | 기준 공변량값에서의 CL | 대상 집단, 기준 CRCL 설정 |
| $\theta_2$ | 무차원 | CRCL 변화가 CL에 미치는 탄성도 | 신청소율 기여도, 모델 구조 |
| $GFR_i$ / $CRCL_i$ | mL·min⁻¹ 등 | 신기능 지표 | 연령, 체중, 혈청 Cr, 신질환 |
| $\eta_i$ | 무차원 | 공변량으로 설명되지 않은 남은 IIV | 미포착 생리학, 유전형, adherence, 모델 오차 |
| $f_u$ | 무차원 | 비결합 분율 | 단백 결합, albumin, 질병 상태, 측정 변이 |

> 💡 **공변량 비유** — 방 안의 소음을 무작정 줄이는 게 아니라, 냉장고 소리·창밖 소리·사람 목소리를 따로 이름 붙이는 일입니다. 이름 붙인 소리는 $\eta$에서 $\theta$ 구조로 옮겨집니다. 그래서 $\left(CRCL_i/90\right)^{\theta_2}$는 단일 숫자가 아니라 **기준 신기능 대비 배율**이고, 묶음에는 underbrace보다 overbrace가 더 정확합니다.

⚠️ **헷갈림 방지**: $\Delta OFV$는 통계적 필터이지 생리학적 타당성의 증명서가 아닙니다. 잔차 모델 · VPC · phenotype cell · a priori physiology가 함께 맞아야 합니다.

🔑 **좌표계 규칙**: $f_u$가 deterministic reparameterization이면 total ↔ unbound 좌표 변환이고, population covariate model이면 남길 $\eta$와 $f_u$ 측정 변이를 분리해야 합니다.

#### B. PK50 앵커(Anchor): $f_u$는 "$\omega^2$ reduction"이 아니라 좌표계 변환입니다

여기서 놓치기 쉬운 전환은 **"공변량 모델"과 "재모수화"의 구분**입니다. 둘 다 변이 해석을 바꾸지만, 하나는 예측변수를 모델에 **추가**하는 것이고, 다른 하나는 같은 자료를 **다른 좌표계로 다시 표현**하는 것입니다.

G&W PK50에서 12명 환자가 CpD 566 µg을 5시간 IV infusion으로 받았고, 총 농도와 비결합 농도가 함께 해석되었습니다. 혈장 단백 결합 데이터인 $f_u$는 total disposition parameter로부터 unbound parameter를 도출하는 데 사용되었습니다. `[G&W p.704–707]`

| 파라미터 | Total estimate (CV%) | Unbound estimate (CV%) |
|---|---:|---:|
| CL | 11.4 L·h⁻¹ (28%) | 720 L·h⁻¹ (9%) |
| Cld | 4.35 L·h⁻¹ (39%) | 265 L·h⁻¹ (33%) |
| Vc | 19.9 L (29%) | 1270 L (18%) |
| Vt | 30.9 L (35%) | 2030 L (51%) |

`[G&W p.708, Table 50.1]`

> 💡 **좌표계 비유** — total과 unbound는 같은 도시를 보는 두 장의 지도입니다. 지도 축을 바꾸면 거리가 다르게 보이지만, 그 자체가 도로를 새로 만든 것은 아닙니다.

**원전 그대로의 해석**: PK50은 total CL CV 28%와 unbound $CL_u$ CV 9%를 보고합니다. 이것은 NONMEM 공변량 모델이 $\omega^2$(CL)을 28%에서 9%로 **"깎았다"**는 뜻이 **아닙니다.** 같은 12명 자료를 total 좌표와 unbound 좌표로 다시 표현했을 때 변이가 다르게 보인다는 뜻입니다. $f_u=0.016\pm0.0049$였으므로 단백 결합 변이가 total concentration/parameter variability의 일부를 설명합니다. `[G&W p.708–709]`

> 💼 **실무 인사이트**: $f_u$가 결정론적 재모수화이면 $CL=f_u\cdot CL_u$의 좌표계 변환으로 처리합니다. 반대로 집단 공변량 모델로 쓸 때는 `CL_u`에 남길 $\eta$와 $f_u$의 측정 변이를 분리해야 합니다. 두 경우를 섞으면 ETA가 생리학이 아니라 **회계 오차**를 흡수합니다.

$$
\underbrace{CL}_{\text{total CL}}
=
\underbrace{f_u}_{\text{비결합분율}}
\cdot
\underbrace{CL_u}_{\text{unbound CL}}
$$

> 📊 **개념 도식 (HTML에서 렌더링)**: PK50의 $f_u$는 NONMEM 공변량 모델의 $\omega^2$ reduction이 아니라, total coordinate를 unbound coordinate로 다시 표현하는 재모수화입니다. 이 변환 뒤에도 response variability는 별도 PD source로 남습니다.

$$
\underbrace{CL=11.4\ \mathrm{L\cdot h^{-1}}}_{\text{total CL}}\quad
(\underbrace{CV=28\%}_{\text{total CV}}),\qquad
\underbrace{CL_u=720\ \mathrm{L\cdot h^{-1}}}_{\text{unbound CL}}\quad
(\underbrace{CV=9\%}_{\text{unbound CV}})
$$

$$
\underbrace{C_{total}}_{\text{총 농도}}
>
\underbrace{50\ \mu\mathrm{g\cdot L^{-1}}}_{\text{안전경계}}
$$

#### C. PK vs PD 변이 분리

PK50의 결정적 메시지는 **단백 결합이 모든 변이를 설명하지 않는다**는 점입니다. CpD는 비슷한 노출에서도 반응이 8배(0.5–4.0 response units)까지 달랐습니다. 비결합 농도를 써도 EC50 변이는 오히려 커졌습니다. 저자들은 $E_{max}<1$인 무반응자가 **유전적 구성/수용체 밀도**와 관련된다고 해석했습니다. `[G&W p.707–709]`

$$
\underbrace{E_{max}}_{\text{최대 반응능}}
<
\underbrace{1}_{\text{완전반응 기준}}
$$

R&T도 혈장 농도와 반응을 함께 측정해야 PK 변이와 PD 변이를 구분할 수 있다고 합니다. `[R&T p.363–364]` 따라서 공변량이 PK 파라미터 변이를 설명했다고 해서 반응 변이까지 설명했다고 보면 안 됩니다.

#### D. 구조적 필요성 및 한계

| 단계 | 근거/가정 | 수식 또는 판단 |
|---|---|---|
| 1 | 공변량은 $\eta$를 없애는 변수가 아니라 설명 가능한 구성요소를 $\theta$ 구조로 옮기는 변수 | $CL_i=\theta_1\cdot(CRCL_i/90)^{\theta_2}\cdot\exp(\eta_i)$ |
| 2 | 공변량 도입 전 G&W식 EDA 선행 | individual profile, pooled data, dose normalization, transformation `[G&W p.334–336]` |
| 3 | 식별가능성이 없으면 이름만 생리학적일 뿐 noise source가 됨 | identifiability/estimability 점검 `[G&W p.348–351]` |
| 4 | 분산 전파식은 PDF에 없고 독립성·산술 검증도 성립하지 않음 | $CV(CL)^2 \approx CV(f_u)^2 + CV(CL_u)^2$는 본 문서에서 삭제 |
| 5 | total concentration safety threshold와 unbound concentration individualization은 서로 다른 좌표계 | total C $>50$ µg·L⁻¹ 회피와 unbound 기반 안전 여유 구분 `[G&W p.705, p.709]` |

```yaml
aliases: [covariate model, creatinine clearance, protein binding, fu, reparameterization]
tags: [pharmacometrics/covariate, pk/protein-binding, nonmem/eta]
source: "R&T p.369-371; G&W PK50 p.704-710"
```

#### M. Plausible Fallacy — `OFV-Driven Covariate Acceptance`

**오류**: "$\Delta OFV$가 3.84(df=1, α=0.05) 이상 감소하면 공변량이 의미 있습니다."
**왜 그럴싸한가**: $\Delta OFV>3.84$는 내포 모델 LRT의 통계적 필터이므로, 숫자 하나로 모델 선택을 끝낼 수 있어 보입니다.
**나비효과**: 잔차 모델 불안정 또는 작은 phenotype cell → 공변량이 $\varepsilon$ 변동이나 ETA 흡수를 대신 설명 → OFV는 감소하지만 VPC가 악화되는 `OFV-VPC Discordance` → 임상에서는 covariate extreme의 노출 예측 실패 또는 고위험군 용량 오류 → 규제에서는 "$\Delta OFV$ 단독 채택"에 대한 FDA Deficiency Letter 및 VPC·sensitivity analysis 재분석 요구.

$$
\underbrace{\Delta OFV}_{\text{OFV 변화}}
>
\underbrace{3.84}_{\text{LRT 기준}}
$$

**왜 틀렸는가**: $\Delta OFV > 3.84$ 기준은 **하나의 통계적 필터**이지 임상적·생물학적 의미의 증거가 아닙니다. 세 경로로 위양성이 생깁니다. (1) 잔차 오차 구조 오지정 시 공변량이 $\varepsilon$ 변동을 흡수하여 잘못된 $\Delta OFV$를 만듭니다 — 진단 시그니처 1 `Leakage Funnel`이 시간 축으로 펼쳐진 형태. (2) 표현형 셀 크기가 작으면(진단 시그니처 2 `Empty Phenotype Cell`) 범주형 공변량의 $\Delta OFV$가 작은 셀의 ETA 흡수로부터 인공적으로 발생합니다. (3) 진짜 mechanistic covariate가 빠지면 상관 공변량(weight, BSA가 CrCl을 대신함)이 가짜로 OFV 개선을 만듭니다 — 진단 시그니처 3 `Vanishing Covariate Cascade`의 거울상.

**임상·NONMEM 시그니처**: 체중을 CL에 추가했더니 OFV가 12 감소했지만, **VPC를 그려보니 예측 구간이 오히려 넓어진다** — 공변량을 추가했는데 모델 적합도가 *분포 수준에서* 악화됩니다. 이름: `OFV-VPC Discordance`. 발생 시 자문 세 가지: 잔차 모델이 안정화되었는가? phenotype cell n이 충분한가? a priori 후보 공변량이 base에 포함되어 있는가? 세 질문 모두 YES이기 전에는 $\Delta OFV$는 그저 한 줄 숫자일 뿐입니다.

**규제 방어 문구**: *"Covariate selection was guided by $\Delta OFV$ combined with VPC consistency at covariate extremes and a priori physiological plausibility; $\Delta OFV$ alone was not used as the acceptance criterion."*

> **진단 시그니처 3 — `Vanishing Covariate Cascade`**
> **시그니처**: 진짜 mechanistic covariate(예: renal clearance에서 CrCl)가 모델에 빠져 있으면 $\eta_{CL}$이 그것을 흡수하고, 후속 stepwise selection에서 상관 covariate(weight, BSA)가 가짜로 detect되는 cascade. 시각적으로는 $\eta_{EBE}$ vs CrCl scatter가 평탄해 보여 "CrCl 효과 없음"으로 잘못 읽히지만, **raw observation 좌표계의 $Cl_{obs}$ vs CrCl은 명확한 기울기**를 가집니다.
> **메커니즘**: stepwise는 $\eta$에 남은 잔여 신호로 covariate를 평가하므로, $\eta$가 이미 covariate를 흡수해 버리면 그 covariate는 통계적으로 사라집니다. "covariate는 $\eta$ 안의 설명 가능한 부분을 $\theta$ 구조로 옮기는 변수"라는 C3 정의가 시간 순서를 잘못 지키면 정반대로 작동합니다.
> **꿀팁**: $\eta$에 의존한 covariate scan 한 번, raw observation에 직접 적용한 covariate scan 한 번 — 두 결과가 일치하지 않으면 "효과 없음"이 아니라 **"효과 흡수됨"**을 의심합니다.
> **실무 활용**: domain knowledge 기반 candidate covariate(생리학적으로 CL을 결정하는 변수: CrCl, body size, hepatic function)를 a priori 정의해 모델 base에 포함시킨 뒤 stepwise를 시작합니다. stepwise에 모든 판단을 위임하지 않습니다.

> **C3 체화 핵심**
> ① `신기능이 CL 변이를 설명할 때` → CRCL/GFR 공변량이 $\theta$ 구조를 결정
> ② `total CL CV 28% vs unbound $CL_u$ CV 9%를 볼 때` → $f_u$ 재모수화와 좌표계가 지배
> ③ `비슷한 노출에서도 반응이 8배 다를 때` → PD variability가 별도 지배
> ④ `OFV만으로 공변량을 채택할 때` → VPC·cell size·physiology 방어 없으면 규제 재분석 위험
> ⚡ `공변량=ω² reduction이라고 해석` → 좌표계 혼동 → dose rationale 불일치

---

<!-- SLIDE_START: C4 | title: 유전적 다형성 — IIV의 불연속 하위구조(substructure) -->
<!-- SECTION_CORE: SC-06 -->

### C4. 유전적 다형성 — IIV의 불연속 하위구조(substructure)

> **앞 카드에서 이 카드로**: C3에서 설명 가능한 생리학을 $\theta$ 구조로 옮겼다면, 이제 남은 $\eta$가 정말 매끄러운 하나의 분포인지, 아니면 유전형/표현형 하위군의 혼합인지 확인해야 합니다.

> **거장의 시각**
> $\eta$ 히스토그램이 하나의 로그정규처럼 보인다고 해서 유전 하위구조가 없다고 결론 내리면, 작은 phenotype cell과 shrinkage가 만든 false negative를 놓칩니다.
> 분포 모양과 cell size를 함께 보면, "효과 없음"과 "효과를 볼 정보가 없음"을 구분할 수 있습니다.

#### A. 형식적 정의(Formal Definition)

C1–C3은 $\eta$를 대개 매끄러운 로그정규 분포로 다룹니다. 그러나 약리유전학은 $\eta$가 실제로는 하나의 매끄러운 분포가 아닐 수 있음을 보여 줍니다. 실제로는 PM/IM/EM/UM 또는 반응자/무반응자처럼 불연속적으로 구분되는 여러 하위집단의 혼합일 수 있습니다. `[R&T p.393–410]`

R&T는 유전 다형성을 모집단 안에서 유전 표현형이 다봉형 분포(polymodal distribution; 봉우리가 여러 개인 분포)를 만들 수 있는 현상으로 다룹니다. 핵심은 유전 형질이 다른 변이의 원인과 달리 **평생 지속되는 개인 특성**이라는 점입니다. `[R&T p.393]`

Hardy-Weinberg logic은 NAT2 acetylator 예시에서 제시됩니다.

$$
\underbrace{p^2}_{\text{동형접합 1}}
+
\underbrace{2pq}_{\text{이형접합}}
+
\underbrace{q^2}_{\text{동형접합 2}}
=
\underbrace{1}_{\text{총 빈도}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $p$, $q$ | 무차원 빈도 | 대립유전자 빈도 | 집단 유전 구조, ancestry, selection |
| $p^2$, $2pq$, $q^2$ | 무차원 빈도 | genotype class 빈도 | Hardy-Weinberg 가정, allele frequency |
| $\theta_2$ 또는 phenotype factor | 무차원 배율 | 특정 phenotype의 CL 변화 | 유전형 기능, 효소 활성, cell size |
| $\eta_i$ | 무차원 | phenotype으로 설명되지 않은 남은 개인차 | 미포착 유전형, 병태, residual artifact |

> 💡 **분포 모양 비유** — 단봉형 $\eta$는 한 언덕의 경사처럼 보이고, 다봉형 $\eta$는 산맥의 여러 봉우리처럼 보입니다. 평균은 계곡 한가운데에 놓일 수 있어, 실제 환자를 대표하지 못합니다.

R&T는 느린 acetylator가 열성 동형접합체일 때, 대립유전자 빈도로 이형접합/동형접합 빠른 acetylator 빈도를 계산하는 방식을 설명합니다. `[R&T p.402]`

⚠️ **헷갈림 방지**: 인종(ethnicity)은 유전형(genotype)의 **불완전한 proxy**입니다. 그룹 내 변이가 크므로 ethnicity term을 mechanistic genotype처럼 해석하면 안 됩니다. `[R&T p.395, p.409]`

🔑 **cell size 규칙**: 작은 phenotype cell에서는 "효과 없음"보다 **"식별할 정보 없음"**을 먼저 의심합니다.

#### B. 출처 고정 유전 예시

| 예시 | 출처 고정 사실 | 모델링 함의 |
|---|---|---|
| Nortriptyline 쌍둥이 | 일란성 쌍둥이의 쌍 내 변이가 이란성 쌍둥이보다 작아 유전이 PK 변이에 크게 기여 `[R&T p.394]` | "설명되지 않은 $\eta$" 안에 유전 성분이 있을 수 있음 |
| CYP2D6 / nortriptyline | 기능적 CYP2D6 유전자 사본 수가 많을수록 청소율이 커지고 노출이 낮아짐 `[R&T p.397]` | $\eta$(CL)이 매끄럽지 않고 유전자 사본 범주로 갈라질 수 있음 |
| CYP2C9 / warfarin | CYP2C9 변이가 S-warfarin 대사와 용량 변이에 기여 `[R&T p.398, p.406]` | PK 유전형(CYP2C9)과 PD 유전형(VKORC1)을 동시에 고려 |
| Codeine | CYP2D6-매개 모르핀 형성은 minor pathway라도 강력한 대사체 때문에 임상적으로 중요 `[R&T p.399, p.404]` | 모약물 청소율만 보면 독성/활성 대사체 위험을 놓침 |
| TPMT / thiopurines | TPMT 다형성은 thiopurine 용량과 독성에 큰 영향 `[R&T p.400]` | Poor metabolizer 하위군은 평균 용량으로 다룰 수 없음 |
| NAT2 / isoniazid | 483명에서 6시간째 isoniazid 농도의 이봉형 분포 `[R&T p.402]` | 이봉형 $\eta$ 분포의 대표 예시 |
| VKORC1 / warfarin | CYP2C9, VKORC1, 연령/체중 등이 warfarin 용량 분산을 나누어 설명 `[R&T p.406]` | 단일 공변량 결정론 금지 |

> 💡 **PM 빈도표 읽기** — 평균 용량을 결정하는 표가 아니라, 어떤 phenotype cell이 작아서 모델 식별성이 흔들릴 수 있는지를 미리 알려 주는 표입니다.

Table 13-1의 poor metabolizer 빈도(출처 값 보존): CYP2D6 PM은 백인 5–10%, 아프리카계 미국인 3.8%, 아시아인 0.9%; CYP2C9 PM은 백인 1%; CYP2C19 PM은 백인 3–5%, 아시아인 16%; TPMT 결핍은 백인 0.3%, 아시아인 0.04%; NAT2 느린 acetylator는 백인/아프리카계 미국인 60%, 아시아인 10–20%; UGT1A1 poor metabolizer 상태는 백인 11%, 아시아인 1–3%. `[R&T p.395]`

#### C. Code Structure

```nmtran
; [교과서 외 구현 번역]
IF (CYP2D6PM.EQ.1) THEN                  ; poor metabolizer indicator가 1이면 PM 효과를 CL에 곱한다
  CL = THETA(1) * THETA(2) * EXP(ETA(1)) ; THETA(2)는 PM phenotype factor, ETA(1)은 남은 IIV
ELSE                                      ; PM이 아니면 기준 CL 구조를 사용한다
  CL = THETA(1) * EXP(ETA(1))            ; 기준군 CL에 남은 IIV만 곱한다
ENDIF
```

$$
\underbrace{CL_i}_{\text{개인 CL}}
=
\underbrace{\theta_1}_{\text{기준 CL}}
\cdot
\overbrace{\theta_2^{I(CYP2D6PM_i=1)}}^{\text{PM 효과}}
\cdot
\underbrace{\exp(\eta_i)}_{\text{남은 IIV}}
$$

> 💼 **실무 인사이트**: 범주형 공변량은 수준별 표본 크기가 충분하지 않으면 THETA factor가 ETA에 흡수됩니다. PM $n=3$ 같은 빈 셀에서는 "효과 없음"이 아니라 **"효과를 식별할 정보가 없음"**일 수 있습니다.

#### D. 구조적 필요성 및 한계

| 상황 | 파라미터 변화 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| 이봉형 분포를 단일 로그정규 IIV로 적합 | $\omega^2$가 하위군 차이를 흡수 | → | 평균 dose가 subgroup toxicity/inefficacy를 숨김 `[R&T p.366]` | mixture 또는 phenotype 구조 검토 |
| 유전 다형성이 존재 | $\eta$ histogram의 두 봉우리가 생리학으로 번역 | → | PM/IM/EM/UM 용량 차이 가능 | genotype/phenotype cell size 확인 |
| ethnicity를 genotype으로 해석 | proxy effect를 mechanistic effect로 과해석 | → | 집단 내 고위험 개인 누락 | genotype 직접성·within-group variability 명시 `[R&T p.395, p.409]` |
| CYP3A4처럼 큰 변이는 있으나 명확한 유전 인자 없음 | 큰 $\omega^2$가 항상 genotype peak를 뜻하지 않음 | → | 유전형 과잉해석 | 다른 인구학·순응·병태 요인 검토 `[R&T p.399, p.410]` |

- HLA-B*5701 빈도, 최신 FDA 약리유전체 라벨 수, 자세한 PM/IM/EM/UM 빈도표는 이 PDF 범위 밖이므로 삭제합니다.
- 약리유전학은 강력하지만 완결된 설명이 아닙니다. R&T는 유전형 외에도 인구학적 특성, 복약 순응 등 다른 요인이 최적 용량 결정에 필요하다고 마무리합니다. `[R&T p.409]`

> 📖 **R&T 5e p.402, Figure 13-6** — 483명에서 9.8 mg/kg 경구 투여 후 6시간째 isoniazid 농도 분포. C4의 핵심은 유전 다형성이 단순 공변량 label이 아니라 **분포 모양 자체를 바꾼다**는 점입니다. 이 그림은 NAT2 acetylator status가 실제 농도 분포를 이봉형으로 만드는 장면을 보여 줍니다.

> **Failure Mode**
> 범주형 유전 구조가 실제로 존재하는데 표본의 한 subgroup이 작거나 비어 있으면, 모델은 그 효과를 독립된 phenotype 효과로 보지 못하고 $\eta$ 안에 흡수할 수 있습니다. 그래서 C4에서는 genotype label 자체보다 **$\eta$ 분포와 농도 분포의 모양이 단봉인지 다봉인지를 먼저 확인**해야 합니다.

> **진단 시그니처 2 — `Empty Phenotype Cell`**
> **시그니처**: phenotype 4-level full stratification(PM/IM/EM/UM)을 처음부터 펼쳤을 때, 작은 n cell(특히 $PM=3$ 같은 희귀 셀)의 THETA factor RSE가 80%를 넘고 `$COV step`이 "covariance matrix is non-positive definite"로 실패합니다. PM 환자 5명의 ETA(1)이 모두 약 0으로 보이는 것은 "효과 없음"이 아니라 **"효과 흡수됨"**의 가장 흔한 false negative 시그니처입니다.
> **메커니즘**: cell이 비면 모델은 그 phenotype 효과를 추정할 정보가 없어 ETA로 흡수하고, $\omega^2$이 인공적으로 inflate됩니다. 보존 법칙이 다시 작동합니다.
> **꿀팁**: PM($n=3$) 결과를 받았을 때 자문해야 할 질문은 "효과가 있는가?"가 아니라 **"효과를 식별할 정보가 데이터에 있는가?"**입니다. 이 둘은 다른 질문입니다.
> **실무 활용**: phenotype level은 데이터 size에 비례해 통합합니다. 인접 phenotype을 합쳐 "reduced function" 같은 단일 카테고리로 시작하거나, informative prior로 작은 cell을 안정화합니다. 4-level full stratification은 데이터가 명확히 허용할 때만 펼칩니다. 작은 cell의 categorical effect를 보고서에 "null result"로 기재하지 않습니다.

$$
\underbrace{RSE}_{\text{상대 표준오차}}
>
\underbrace{80\%}_{\text{불안정 경고}}
$$

*↑ 이 부등식은 원문에서 practice decision rule로 제시된 경고 기준입니다.*

```yaml
aliases: [pharmacogenetics, genetic polymorphism, CYP2D6, CYP2C9, NAT2, TPMT, VKORC1]
tags: [pharmacometrics/iiv, pharmacogenomics, nonmem/categorical-covariate]
source: "R&T p.393-410"
```

> **C4 체화 핵심**
> ① `η 분포가 두 봉우리로 보일 때` → genotype/phenotype subgroup이 결정
> ② `phenotype cell n이 작거나 비어 있을 때` → 식별가능성/ETA 흡수가 지배
> ③ `ethnicity covariate가 유의해 보일 때` → proxy와 mechanistic genotype을 분리
> ⚡ `효과 없음과 정보 부족을 혼동` → PM subgroup 위험 누락 → 평균 dose가 subgroup toxicity/inefficacy를 숨김

---

<!-- SLIDE_START: §5 | title: 혼동쌍 해부(Confusion Pair Dissection) -->
<!-- SECTION_CORE: SC-07 -->

## §5 — 혼동쌍 해부(Confusion Pair Dissection)

### Pair 1. $\omega^2$(IIV) vs $\sigma^2$(RUV)

| 비교 기준 | $\omega^2$ / $\eta$ | $\sigma^2$ / $\varepsilon$ |
|---|---|---|
| 단위 / 차원 | random effect 분산; `$OMEGA`; 개인 파라미터 수준 | residual variance; `$SIGMA`; 관측값 수준 |
| 수식 내 위치 | $CL_i=CL\cdot\exp(\eta_i)$의 지수 배율 또는 individual parameter 구조 | $Y=F+\varepsilon$, $Y=F(1+\varepsilon)$, $Y=F\exp(\varepsilon)$의 관측 잔차 |
| 변화 원인 | 개인별 CL·V 차이, 생리학, 유전형, 병태, 미포착 공변량 | assay error, sampling error, residual model misspecification |
| 혼동 시 임상 결과 | 측정 오차를 IIV로 해석해 가짜 covariate 탐색 | 진짜 IIV를 잔차 noise로 묻어 dose individualization 실패 |

**결정적 차이**: $\omega^2$와 $\sigma^2$는 같은 총 미설명 변이를 두고 경쟁합니다. 잔차 모델을 틀리면 공변량이 단순히 보이거나 사라지는 게 아니라 **분산이 잘못된 그릇으로 이동**합니다.

> **⚡ 기억 고리 — Pair 1**
> *개인 고유의 차이 vs 측정·모델의 잡음.* $\omega^2$(`$OMEGA`)는 같은 약물, 같은 용량에서도 개인마다 CL·V가 다른 **생물학적 개체간 차이** — 실제로 존재하는 차이. $\sigma^2$(`$SIGMA`)는 하나의 개인 안에서 예측값과 관측값이 일치하지 않는 **측정·모델·시간 내 노이즈** — 설명 실패.
> 따라서 처치법이 다릅니다: $\omega^2$를 줄이는 것은 IIV 원인 찾기(covariate 추가), $\sigma^2$를 줄이는 것은 모델 구조 또는 측정 오차 모델 개선(residual model 재선택, assay 재검증). 둘을 혼동하면 covariate를 늘려도 $\sigma^2$ 문제는 해결되지 않고, error model을 바꿔도 IIV는 그대로 남습니다.

### Pair 2. Total CL vs Unbound $CL_u$ — PK50 앵커 기반

| 비교 기준 | Total CL | Unbound $CL_u$ |
|---|---|---|
| 단위 / 차원 | CL 11.4 L·h⁻¹, CV 28% `[G&W p.708]` | $CL_u$ 720 L·h⁻¹, CV 9% `[G&W p.708]` |
| 수식 내 위치 | $CL=f_u\cdot CL_u$의 total 좌표계 결과 | $CL_u=CL/f_u$로 해석되는 unbound 좌표계 결과 |
| 변화 원인 | 단백 결합 변이가 total concentration/parameter variability에 섞임 | $f_u$로 재표현된 disposition; 유리 약물 기준 제거 능력 |
| 혼동 시 임상 결과 | total C $>50$ µg·L⁻¹ 회피 기준과 unbound 기반 안전 여유가 불일치 | 저알부민혈증에서 total 정상이어도 unbound 독성 위험 놓침 `[G&W p.705, p.709]` |

**수정된 치명적 타격**: PK50은 "$f_u$ covariate가 $\omega^2$을 줄였다"가 아니라, 같은 12명을 total과 unbound 좌표계로 비교했을 때 변이 해석이 달라짐을 보여 줍니다. 용량/안전성 판단에서 total C $>50$ µg·L⁻¹ 회피 기준과 unbound 기반 안전 여유가 혼동되면, 노출-반응 해석의 좌표계가 불일치합니다. `[G&W p.705, p.709]`

> **⚡ 기억 고리 — Pair 2**
> *전체 통행량 vs 무료 차선 통행량.* Total CL은 bound + unbound 약물 모두를 기준으로 한 **전체 제거 능력**. Unbound $CL_u = CL/f_u$는 유리 약물만을 기준으로 한 **실제 작용 약물의 제거 능력**. 저알부민혈증 환자에서 $f_u$가 증가하면 total CL이 변하지 않아도 unbound CL($= CL/f_u$) 좌표는 다르게 보입니다.
> PK50에서 보여준 것처럼, total 좌표에서 "IIV가 크다"(CV 28%)는 신호가 unbound 좌표로 변환되면 **다른 숫자(CV 9%)** 가 됩니다 — $\omega^2$이 줄어든 게 아니라 **좌표축이 회전한 것**. 좌표계를 잘못 고르면 covariate 탐색의 방향이 반대가 됩니다.

> **🔴 치명적 타격 — Pair 2**
> 이 혼동을 안고 NDA의 dose individualization 섹션을 강행하면, total 좌표에서 산출된 $\omega^2$을 마치 covariate 모델이 reduction을 만든 것처럼 보고하게 됩니다. 규제 reviewer는 (a) total/unbound coordinate split이 명시되지 않았거나, (b) safety threshold(total)와 dose recommendation(unbound 기반)이 좌표계 측면에서 일치하지 않음을 deficiency 사유로 지적합니다. 임상적으로는 저알부민혈증 환자에서 total 농도가 정상이어도 unbound이 높아 독성이 발생하는 시나리오를 보호하지 못합니다. `[G&W p.705, p.709]`

### Pair 3. PK 변이 vs PD 변이

| 비교 기준 | PK 변이 | PD 변이 |
|---|---|---|
| 단위 / 차원 | 농도-시간 프로파일, CL·V·F 등 PK 파라미터 | 반응(response), EC50·Emax·γ 등 PD 파라미터 |
| 수식 내 위치 | concentration-time model의 structural/random effect 위치 | exposure-response model의 response parameter 위치 |
| 변화 원인 | 흡수·분포·대사·배설, 단백결합, renal/hepatic function | receptor density, genetic makeup, target expression |
| 혼동 시 임상 결과 | 혈중농도만 맞추면 반응도 맞는다고 오판 | 비슷한 노출에서도 8배 반응 차이를 설명 못함 `[G&W p.707–709]` |

PK 변이는 **농도-시간 프로파일이 왜 다른가**를 묻고, PD 변이는 **같은 노출에서 반응이 왜 다른가**를 묻습니다. R&T는 혈장 농도 측정이 PK와 PD 변이를 분리하는 전제라고 합니다. `[R&T p.363–364]` PK50에서 단백 결합은 총 농도 변이의 일부를 설명했지만, 반응은 비슷한 노출에서도 8배 차이를 보였습니다 — 단일 공변량이 모든 변이를 설명한다는 사고가 왜 위험한지 보여 주는 핵심 예. `[G&W p.707–709]`

> **⚡ 기억 고리 — Pair 3**
> *약이 어떻게 움직이는가 vs 어떻게 반응하는가.* PK IIV는 개인별 CL·V·F의 차이 — 같은 용량에서 **농도가 얼마나 다른가**. PD variability는 개인별 EC50·Emax·γ의 차이 — 같은 농도에서 **반응이 얼마나 다른가**. 둘은 **수학적으로 독립적**이므로 PK IIV가 작아도 PD variability가 크면 농도만 맞춰도 반응 개체화는 어렵습니다. 개인화 의료에서 TDM이 혈중농도를 맞추는 것(PK 영역)과 반응을 맞추는 것(PD 영역)이 왜 다른 문제인지가 여기서 나옵니다. PK50의 "response 8배 차이"는 PK 좌표계의 covariate 모델로는 도달할 수 없는 잔여 variability입니다.

### Pair 4. 평균 분포(mean distribution) vs 분포 모양(shape distribution)

| 비교 기준 | 평균 분포(mean/CV 중심) | 분포 모양(shape 중심) |
|---|---|---|
| 단위 / 차원 | 평균, CV, 단일 로그정규 근사 | skewness, bimodality, polymodal distribution |
| 수식 내 위치 | $\theta$와 단일 $\omega^2$ 요약 | $\eta$ histogram, mixture/phenotype 구조 |
| 변화 원인 | 평균 CL·V와 전체 산포 | 유전형/표현형 하위군, residual artifact, data cell imbalance |
| 혼동 시 임상 결과 | 평균이 대표값이라고 오판 | 이봉형 분포의 계곡 평균을 용량 기준으로 사용해 subgroup 위험 누락 |

R&T의 nortriptyline 예시는 로그정규 분포를, 가상 청소율 분포는 이봉형 분포에서 평균이 치료적 대표값이 되기 어렵다는 점을 보여 줍니다. `[R&T p.363, p.366]` 평균과 CV만 보고 $\eta$ 분포의 모양을 확인하지 않으면, C4에서 다룬 유전 하위군을 놓칩니다.

> **⚡ 기억 고리 — Pair 4**
> *진짜 신호 vs 모델 결함의 메아리.* Residual error model이 잘못 지정되면(예: 실제로는 proportional+additive인데 proportional만 쓴 경우) $\sigma^2$가 저농도에서 과소평가되어 이 오차가 $\eta$에 흡수됩니다. 그 결과 $\omega^2$가 부풀어 오르고, 이 부풀어 오른 $\omega^2$를 "설명하기" 위해 covariate가 $\Delta OFV$를 달성합니다 — 그러나 그 covariate는 **residual model artifact의 흡수통로**에 불과합니다. 진짜 covariate signal과 model artifact를 구분하려면 **순서를 지킵니다**: residual model을 먼저 안정화한 뒤 covariate를 탐색합니다. 진단 시그니처 1(`Leakage Funnel`)이 정적 시그니처라면, 이 hook은 그 신호가 시간 축으로 펼쳐져 covariate selection 단계까지 왜곡되는 동적 시그니처입니다.

**§5 요약**: 이 세션의 혼동은 거의 모두 "**어느 좌표계의 변이인가**"로 귀결됩니다. 즉 개체 vs 잔차, total vs unbound, PK vs PD, 평균 vs 모양을 구분해야 합니다.

---

<!-- SLIDE_START: §7 | title: 자기 테스트(Self-Test): 능동 회상 모듈(Active Recall Module) -->
<!-- SECTION_CORE: SC-08 -->

## §7 — 자기 테스트(Self-Test): 능동 회상 모듈(Active Recall Module)

### Q1. $CL_i=CL\cdot\exp(\eta_i)$를 쓰는 가장 직접적인 이유는?

**정답**: CL이 음수가 되지 않도록 보장하면서 $\eta$를 정규 분포로 둘 수 있기 때문입니다. R&T는 지수형 오차 모델이 근사적 일정 CV를 주고 계산상의 어려움(computational difficulty)을 줄인다고 설명합니다. `[R&T p.371]`

$$
\underbrace{CL_i}_{\text{개인 CL}}
=
\underbrace{CL}_{\text{모집단 중심}}
\cdot
\underbrace{\exp(\eta_i)}_{\text{양수 배율}}
$$

### Q2. 잔차 변이가 평균 0의 무작위가 아니면 무엇을 뜻하는가?

**정답**: 구조 모델 또는 오차 모델이 아직 중요한 변이의 원인을 설명하지 못했다는 뜻입니다. 이 상태에서 공변량을 찾으면, 공변량이 생물학이 아니라 잔차 모델의 잘못된 지정을 설명할 수 있습니다. `[R&T p.372]`

### Q3. PK50에서 "total CL CV 28%, unbound $CL_u$ CV 9%"를 어떻게 해석해야 하는가?

**정답**: $f_u$를 공변량으로 넣어 $\omega^2$을 28%에서 9%로 줄였다는 뜻이 **아닙니다.** 같은 12명 CpD 자료를 total 좌표와 unbound 좌표로 표현했을 때, 단백 결합 변이가 total parameter variability의 일부를 설명한다는 뜻입니다. `[G&W p.706–709]`

### Q4. $CV(CL)^2 \approx CV(f_u)^2 + CV(CL_u)^2$를 이 문서에서 쓰지 않는 이유는?

**정답**: 이 분산 전파식은 첨부 PDF에 없고, 독립성 가정도 제시되지 않았으며, Audit에서 산술적으로도 검증되지 않는다고 판정되었습니다. 따라서 source-locked Content Lock에서는 삭제합니다.

$$
\underbrace{CV(CL)^2}_{\text{CL 변이}}
\approx
\underbrace{CV(f_u)^2}_{\text{fu 변이}}
+
\underbrace{CV(CL_u)^2}_{\text{CL_u 변이}}
$$

*↑ 원문은 이 식을 사용하지 않는 이유를 설명합니다.*

### Q5. PK50에서 비결합 농도를 써도 PD 변이가 남은 이유는?

**정답**: 단백 결합은 PK 좌표계 변이의 일부를 설명하지만, 반응 변이는 수용체 밀도/유전적 구성 같은 PD 원인을 포함합니다. G&W는 $E_{max}<1$인 무반응자가 표적의 완전한 발현을 결여한 것으로 해석합니다. `[G&W p.707–709]`

$$
\underbrace{E_{max}}_{\text{최대효과}}
<
\underbrace{1}_{\text{완전반응 기준}}
$$

### Q6. $\eta$-EBE 히스토그램이 두 봉우리로 보이면 가장 먼저 무엇을 의심해야 하는가?

**정답**: 매끄러운 로그정규 IIV 하나가 아니라, **유전형/표현형 하위군 또는 혼합형 모집단 구조**가 섞였는지 의심해야 합니다. 단, 희소 표본이면 히스토그램 자체의 정보량을 먼저 점검해야 합니다. `[R&T p.366, p.393–397]`

### Q7. 인종 공변량을 유전형처럼 해석하면 왜 위험한가?

**정답**: R&T는 인종이 개인 유전 형질의 **불완전한 대체지표(proxy)**이며, 그룹 내 변이도 크다고 경고합니다. 인종 항목은 탐색적 공변량일 수 있지만 mechanistic 유전형의 대체물은 아닙니다. `[R&T p.395, p.409]`

### Q8. 잔차 모델 오지정 vs 공변량 추가 — 어느 것을 먼저 고치는가?

> **⚡ 보스 딜레마 ★★**
> 잔차 모델 오지정이 의심되는 상황에서 공변량 탐색을 시작하려 합니다. 두 전략이 충돌합니다:
>
> **선택지 A — 잔차 안정화 우선**: $\varepsilon$ 구조를 먼저 잡습니다. $\varepsilon$이 자리 잡으면 $\omega^2$의 진짜 공변량 신호가 드러납니다. 단점: 잔차 모델 선택이 지연되면 전체 모델 구축 일정이 늦어지고, sponsor가 timeline pressure를 가하는 후기 단계에서 부담이 됩니다.
>
> **선택지 B — 공변량 탐색 우선**: $\omega^2$ 감소 패턴이 어떤 공변량이 IIV를 설명하는지 보여 주고, 이후 잔차 모델을 조정합니다. 단점: 잔차 모델 artifact가 공변량으로 잘못 흡수될 위험(진단 시그니처 1 `Leakage Funnel`이 시간축으로 펼쳐지는 시나리오; Pair 4 기억 고리 참조).
>
> 각 선택을 규제 보고서에서 어떻게 방어하는가?

**정답(표층)**: 잔차 모델 오지정을 먼저 고칩니다. $\varepsilon$ 구조가 틀린 상태에서 공변량을 추가하면 $\omega^2$와 $\sigma^2$의 경쟁이 왜곡되어, 생물학이 아니라 오차 모델의 실패를 공변량이 설명하게 됩니다. `[R&T p.371–373]`

**거장의 상충 논리(Trade-off)**: A는 순서상 올바르지만 초기 데이터 탐색 단계에서는 잔차 모델이 아직 불확실하므로 무한 재탐색 루프에 빠질 수 있습니다. 실무 베테랑은 **A를 default로 하되 single-iteration 한도를 둡니다** — 즉 잔차 모델 후보 2–3개를 a priori 정의하고 단 한 번의 비교로 결정한 뒤 공변량 탐색으로 진행합니다. B는 탐색적이지만 최종 모델에서 잔차 모델을 명시적으로 재검토했다는 증거를 제시해야 합니다. 이 경로를 택한다면 보고서에 **반드시 민감도 분석**(다른 잔차 모델에서 공변량 선택 결과가 어떻게 달라지는지)을 명시합니다.

**규제 방어 문구**:
- 선택지 A 채택 시: *"Residual error model was finalized prior to covariate evaluation based on a priori candidate set {additive, proportional, combined} compared by $\Delta OFV$ and CWRES distribution; covariate selection proceeded only after residual model lock."*
- 선택지 B 채택 시: *"Residual error model misspecification influence on covariate selection was assessed by sensitivity analysis: covariate model {final} was re-fitted under alternative residual structures and $\Delta OFV$ directionality, parameter estimate stability, and VPC consistency were verified."*

**다음 깊이 질문**: 그렇다면 민감도 분석이 통과하지 못했을 때 — 즉 잔차 모델 변경 시 공변량 선택 결과가 뒤집힐 때 — 그 공변량을 보고서에서 어떻게 처리할 것인가? (선행: 모델 평균? 후행: 두 모델 모두 보고? 결정: 더 보수적인 모델 채택?)

**SR 태그**: ★★ (다음 세션 반드시 재등장)

**§7 요약**: 시험 문제의 정답은 대부분 "**변이의 원인을 잘못된 그릇에 넣지 말라**"입니다.

---

<!-- SLIDE_START: §8 | title: 메타 프레임 및 큰 그림(Meta-Frame & Big Picture) -->
<!-- SECTION_CORE: SC-09 -->

## §8 — 메타 프레임 및 큰 그림(Meta-Frame & Big Picture)

### A. 위치 설정 — 28-session architecture

이 세션은 PopPK 커리큘럼의 **분산 축(variance axis)**입니다. 이전 세션들이 CL, V, ka, $t_{1/2}$ 같은 구조 파라미터의 평균을 세웠다면, 이 세션은 그 평균 주변의 개인차와 잔차를 분해합니다. 따라서 이후 FOCE/FOCE-I, GOF, 공변량 선택, Bayesian TDM은 모두 이 분해 위에서만 의미가 있습니다.

### B. 의존성 — 대충 넘겼을 때 발생하는 실패

| 의존 항목 | 대충 넘기면 생기는 실패 |
|---|---|
| C1 $\theta$/$\eta$/$\varepsilon$ | `$OMEGA`와 `$SIGMA`를 숫자로만 읽고, 생리학과 잔차 noise를 구분하지 못함 |
| C2 잔차 오차 | 잘못된 $\varepsilon$가 $\omega^2$로 새어 가짜 IIV 또는 가짜 공변량을 만듦 |
| C3 공변량/재모수화 | $f_u$, CrCl, 체중을 모두 같은 방식의 공변량으로 취급해 좌표계 변환과 인과적 예측변수를 혼동 |
| C4 유전 다형성 | 이봉형 분포를 단일 로그정규 $\eta$로 덮어 하위군 용량 위험을 숨김 |
| EDA 우선 | spaghetti plot과 변환 플롯 없이 control stream부터 쓰다가 하위군 신호를 놓침 `[G&W p.334–336]` |
| 규제 PopPK 일관성 | $\theta$, $\omega^2$, $\sigma^2$, 잔차 모델, 공변량 효과가 서로 일관되지 않으면 보고서 표는 완성되어 있어도 용량 근거가 무너짐 `[R&T p.373]` |

> **체화 노트 — NDA Section 5.2 line-item 일관성**
> 규제 reviewer는 PopPK 보고서의 $\omega^2$, $\sigma^2$, 잔차 모델, $\eta_{EBE}$ 분포, 공변량 효과를 순차적인 line item으로 읽습니다. 그러나 실제로 감사하는 것은 line item 각각이 아니라 **그들 사이의 상호 일관성**입니다. 예를 들어 $\sigma^2$(proportional)로 보고된 CV가 분석법 검증 보고서의 CV와 동떨어지면, 모델 전체의 prior justification이 흔들리고 첫 번째 의문 한 줄이 후속 모든 표에 cascade됩니다.
> **꿀팁**: Session 13의 모든 분산 결정은 자체로 정합적일 뿐 아니라 **인접 보고서들의 좌표계와 일치해야 합니다** — 즉 $\sigma^2$ ↔ assay CV, total threshold ↔ unbound dose recommendation, $\eta$ 분포 모양 ↔ 모집단 약리유전 컨텍스트가 한 묶음으로 검토됩니다.
> **실무 활용**: 모델 lock 전에 (1) bioanalytical CV 표, (2) 안전 임계 좌표계, (3) 모집단 유전 reference를 한 번 더 펼쳐 line item별 cross-check sheet를 만듭니다. 이는 R&T p.373이 말하는 "regulatory requirement"의 실무 번역입니다.

### C. 전문가의 해자 — 이 세션이 전문가를 가르는 지점

초급자는 "IIV가 큽니다"라고 말합니다. 중급자는 "CL에 covariate를 넣겠습니다"라고 말합니다. 전문가는 다음 질문을 던집니다.

| 거장의 질문 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| PK인가 PD인가? `[R&T p.363–364; G&W p.707–709]` | $\eta_{CL}$ vs $\eta_{EC50}$ | → | 농도 개체화와 반응 개체화 혼동 | PK/PD 별도 적합 후 IIV 비교 |
| $\eta$인가 $\varepsilon$인가? `[R&T p.369–373]` | OMEGA vs SIGMA | → | assay/잔차 문제를 공변량으로 오인 | residual model 변경 전후 OMEGA/SIGMA 비교 |
| total 좌표인가 unbound 좌표인가? `[G&W p.706–709]` | $\omega^2$(CL) vs $\omega^2$($CL_u$) | → | safety threshold와 dose recommendation 좌표계 불일치 | total/unbound 모델 병렬 보고 |
| smooth distribution인가 subgroup/phenotype structure인가? `[R&T p.366, p.393–410]` | $\eta$-EBE histogram, mixture effect | → | 평균 dose가 하위군 위험을 숨김 | bimodality 및 cell size 확인 |
| mechanistic covariate인가 proxy인가? `[G&W p.348–351; R&T p.395]` | covariate THETA, RSE, condition number | → | 식별 불가능한 accounting device를 생리학으로 보고 | bootstrap/SIR, 공선성, identifiability 점검 |

### D. 후속 세션 연결 — 지식 그래프

| 후속 세션 | 이 세션에서 열리는 개념 | 이 세션 없으면 실패하는 것 |
|---|---|---|
| FOCE / FOCE-I | $\theta$–$\eta$–$\varepsilon$ 동시 추정과 EBE 조건부 해석 | EBE를 개인 참값으로 오해 |
| GOF / CWRES | residual model 안정화와 leakage funnel 진단 | 공변량 탐색 전에 잔차 artifact 미제거 |
| $\eta$-EBE / shrinkage | 개체별 정보량과 분산 분해능 | high-shrinkage plot 과해석 |
| Stepwise covariate selection | $\omega^2$ 중 설명 가능한 생리학의 이동 | OFV-driven fishing |
| Bayesian TDM | 개인 $\eta$ 업데이트와 용량 개체화 | 평균 dose 또는 잘못된 좌표계에 의존 |

> **🔬 NONMEM 출력 시그니처 매핑**
> 위 질문은 추상적 사고가 아닙니다. 각 질문은 **실제 NONMEM 출력 또는 진단 파일의 특정 시그니처**로 답해야 합니다. 전문가 해석 지점은 질문을 던지는 능력이 아니라, 그 질문을 출력 파일에서 읽어 내는 능력입니다.
>
> | 거장의 질문 | NONMEM/진단 출력 시그니처 |
> |---|---|
> | Q1. PK인가 PD인가? | PK 자료(농도)와 PD 자료(반응)을 **별도 모델로 적합** 후 $\omega^2$(PK)와 $\omega^2$(PD)를 비교; 같은 환자에서 $\eta_{CL}$과 $\eta_{EC50}$의 상관이 낮으면 두 영역이 독립적인 IIV 원인임을 보여줍니다. |
> | Q2. $\eta$인가 $\varepsilon$인가? | **OMEGA 행렬 대각 원소 변화** vs **SIGMA 추정값 변화**를 잔차 모델 변경 전후로 비교. $\varepsilon$ 모델 변경 시 $\omega^2$(CL)이 크게 움직이면 진단 시그니처 1 leakage funnel 작동 중. $\eta$-shrinkage $<30\%$일 때만 $\eta$-EBE 기반 진단을 신뢰합니다. |
> | Q3. Total인가 unbound인가? | Total 적합 출력의 $\omega^2$(CL)과 unbound 적합 출력의 $\omega^2$($CL_u$)을 **나란히 비교**; PK50 패턴(28% vs 9%)이 재현되면 $f_u$가 결정론적 재모수화로 작동 중. $f_u$ 자체에 $\eta$를 부여한 모델과 부여하지 않은 모델의 $\Delta OFV$로 $f_u$ 측정 변이 분리 여부 판정. |
> | Q4. Smooth인가 하위군 구조인가? | **$\eta$-EBE 히스토그램**(R: `xpose4::eta.dist()` 또는 PsN sse output)에서 이봉형 여부 확인; 혼합 모델 `$MIX`의 $\Delta OFV$ vs 단일 로그정규 IIV — 단, 작은 n cell에서는 진단 시그니처 2 `Empty Phenotype Cell`(RSE $>80\%$, `$COV step` 실패) 우선 점검. |
> | Q5. Mechanistic인가 proxy인가? | **Bootstrap 또는 SIR**으로 공변량 효과의 95% CI 폭 확인; CI가 0을 포함하지 않더라도 폭이 비대칭하거나 매우 넓으면 식별가능성 결손 의심. `$COV step`의 condition number($>1000$이면 ill-conditioned)와 공변량-공변량 상관행렬($|r|>0.7$이면 다중공선성)을 함께 봅니다. |
>
> $$
> \underbrace{\eta\text{-shrinkage}}_{\text{EBE 분해능}}<\underbrace{30\%}_{\text{경고선}},\quad
> \underbrace{RSE}_{\text{불확실성}}>\underbrace{80\%}_{\text{불안정}},\quad
> \underbrace{condition\ number}_{\text{수치 조건성}}>\underbrace{1000}_{\text{조건성 경고}},\quad
> \underbrace{|r|}_{\text{상관}} > \underbrace{0.7}_{\text{공선성 경고}}
> $$
>
> **꿀팁**: 각 거장 질문에 NONMEM 출력 한 곳을 1:1로 매핑하지 못하면 그 질문은 보고서에서 방어할 수 없습니다. 보고서 line item마다 어느 출력에서 그 결론이 나왔는지 cross-reference 가능해야 합니다 — 이것이 NDA 5.2 line-item consistency가 실무에서 작동하는 방식입니다.

### 최종 요약(Final Recap)

Session 13의 최종 메시지는 하나입니다. **$\omega^2$은 "남은 변이"가 아니라 아직 이름 붙이지 못한 생리학·유전학·행동·측정 구조의 혼합물입니다.** C2는 잔차 noise를 정리하고, C3는 설명 가능한 생리학을 꺼냅니다. C4는 매끄러운 IIV 안에 숨어 있는 유전적 불연속성을 드러냅니다. 이 순서를 지키지 않으면 NONMEM은 돌아가지만, 용량 개체화는 성립하지 않습니다.

---

<!--
## 출력 후 자가검증 체크리스트

| 항목 | 기준 | 결과 |
|---|---|---|
| SLIDE_START 개수 | §섹션수 + 카드수 합산 | 9개 |
| 카드당 callout 합계 ≤ 6 | 전체 카드 | ✓ |
| [E] 박스 존재 | 모든 §2 카드 | ✓ |
| [D] 거장의 시각 존재 | 모든 §2 카드 | ✓ |
| [L] 파라미터 표 존재 | Apex 카드 + 정의 수식 카드 | ✓ |
| §5 혼동 쌍 표 행 순서 고정 (4행) | §5 전체 | ✓ |
| 기호 일관성 | 첫 등장 기준 통일 | ✓ |
| PART B 흔적 없음 | 전체 | ✓ |
| 수치 anchor 보존 | Compound A 등 원본 수치 | ✓ |
| [M] 나비효과 이중 종착점 | Apex 카드 전체 | ✓ |

**검증 메모**: Compound A 수치 anchor는 원본 PART A 범위에 존재하지 않아 추가하지 않았습니다. PK50, poor metabolizer 빈도, OFV 3.84, shrinkage/RSE/condition number/correlation 경고선 등 원본 PART A의 수치 anchor는 보존했습니다.
-->

<!-- v3.8 변환 노트
- 활자량 감축: v3.7 913줄 → v3.8 약 555줄 (감축률 약 39%; 컨텐츠 보존을 위해 목표 40–55%의 하단에 맞춤)
- 보존 감사:
  · SLIDE_START 마커: 9개 = v3.7 일치 (§1, §2, C1, C2, C3, C4, §5, §7, §8)
  · 수식 $$ 블록: 20개 = v3.7 일치 (C1×2, C2×2, C3×7, C4×3, §7×3, §8×1)
  · 출처 anchor: G&W·R&T·실무통합·교과서 외 구현 모두 v3.7과 1:1 일치
  · 수치 anchor: $f_u=0.016\pm0.0049$, CL 11.4 (CV 28%), CL_u 720 (CV 9%), Cld 4.35 (CV 39%), Vc 19.9 (CV 29%), Vt 30.9 (CV 35%), C>50 µg/L, PM 빈도표(CYP2D6/2C9/2C19/TPMT/NAT2/UGT1A1), ΔOFV 3.84, RSE 80%, shrinkage 30%, condition number 1000, |r| 0.7 — 모두 일치
  · 약물명: warfarin, nortriptyline, codeine, thiopurines, isoniazid, CpD — 모두 일치
- 의도된 수식 중복 (v3.7에서 자기참조 학습 구조로 설계됨):
  · $CL_i=CL\cdot\exp(\eta_i)$ — C1 § A(개념 정의) + §7 Q1(능동 회상) — 보존
  · $E_{max}<1$ — C3 § C(PK vs PD 분리) + §7 Q5(능동 회상) — 보존
  이 두 식은 학습 구조상 의도된 재등장이므로 §3 HARD PRESERVE 적용
- 주요 변환:
  · 메타 문구 제거: "Target filename", "Source file", "편집 범위", "기호 통일 내역", "확인 시점: 이 카드를 읽은 뒤 확인하시면 됩니다", "[EXPERT_INFERENCE, v3]"/"[CRUCIBLE_DERIVED]" 태그, "<!-- 편집 주: ... -->" HTML 코멘트, "이 교재 활용법" 분류된 학습 안내 → 약 80건 제거
  · 자기참조 해소: "M14의 결론이~" 형태는 원문에 없었음 (이미 비교적 직접적). "진단 시그니처 3은~" 식 forward reference는 그 자리에서 한 줄로 의미를 풀고 (→ 진단 시그니처 N) 포인터만 남김 — 약 12건
  · §5/§7/§8 Memory Hook 및 보스 딜레마: 번역체 문장을 §10 Ex-A~D 패턴으로 풀어쓰되 모든 결정 규칙·규제 방어 문구는 byte 단위 보존
  · §1 "학습자 네비게이션 안내" 35줄을 "학습 경로" 표 + 4줄 자기 점검 박스로 압축
  · 콜아웃 단일화: C1의 💡(184)+💡(198) 중복을 하나로 통합, C3의 💡 비유(433)+💡 묶음 역할(435)를 하나로 통합
- 추가/삭제/재배열: 0건 (§15 SCOPE 준수)
-->

# 세션 13(Session 13) — 개체 간 변이(IIV/BSV)와 공변량 모델링 — v4.2 보강본_final

---

## 임상 장면 — 같은 약, 같은 용량, 다른 사람

먼저 한 장면을 띄워 놓고 시작할게요. **CpD**라는 약을 566 µg, 5시간 IV infusion으로 12명 환자에게 줍니다. 그러고 나서 청소율을 보면 — **총 농도(total) 기준 CL은 11.4 L·h⁻¹인데 사람마다 28%씩 흔들려요**. 그런데 **비결합(unbound) 기준 $CL_u$로 다시 보면 720 L·h⁻¹에 흔들림이 9%로 뚝 떨어집니다**. 이게 별 차이 아닌 것 같지만, 같은 환자들이에요. 그 사이에 변한 건 우리가 어느 좌표에서 봤느냐 — total이냐 unbound이냐 — 그것뿐이에요. 동시에 비결합 분율은 $f_u = 0.016 \pm 0.0049$였고, 안전상 total C가 50 µg·L⁻¹를 넘으면 안 되는 약입니다. `[G&W p.704–709]`

자, 이 장면에서 우리가 물어야 할 질문은 "**평균 CL이 얼마냐**"가 아니에요. 그건 평균 한 줄로 끝나니까. 진짜 물어야 할 건 이거예요 — **사람마다 다른 그 28%의 흔들림이 (1) 단백결합이 사람마다 달라서 그렇게 보이는 거냐, (2) 정말 약을 제거하는 능력 자체가 사람마다 달라서 그러냐, (3) 아니면 PK는 비슷한데 약에 대한 반응(PD)만 사람마다 다른 거냐**. 세 답이 완전히 다른 임상 결론을 가져옵니다.

오늘 한 세션 내내 이 질문 하나를 따라갑니다. "**그 다름이 어디서 오는가**".

---

## 학습 경로

| 단계 | 섹션 | 목적 |
|---:|---|---|
| 1 | §1 | 변이 축 전체 지도 |
| 2 | §2 C1 | $\theta$/$\eta$/$\varepsilon$ · $\omega^2$/$\sigma^2$ 분리 |
| 3 | §2 C2 | 공변량 해석 전에 잔차 오차 구조부터 확정 |
| 4 | §2 C3 | 진짜 공변량 설명과 total/unbound 좌표 변환 구분 |
| 5 | §2 C4 | 매끄러워 보이는 IIV 안의 불연속 유전 하위구조 |
| 6 | §5 | 혼동쌍 해소 |
| 7 | §7–§8 | 자기 테스트 + PopPK 커리큘럼 통합 |

시작 전 본인 머리에 들어 있어야 하는 것: CL, V, $t_{1/2}$, 단백 결합 개념, NCA 기본, 그리고 NONMEM control-stream을 한 번이라도 열어본 경험.

이 세션을 마친 뒤 본인 입으로 설명할 수 있어야 합니다 — $\theta$만으로는 왜 부족한지, 잔차 모델을 잘못 정하면 왜 가짜 IIV나 가짜 공변량 신호가 만들어지는지, PK50 사례가 단순히 "$f_u$가 흔들림을 줄였다"가 아니라 **좌표계를 바꾸고 모델을 다시 쓴 수업**인 이유, 그리고 이봉형 농도/$\eta$ 분포를 매끄러운 로그정규 하나로 덮으면 왜 위험한지.

---

<!-- SLIDE_START: §1 | title: 세션 헤더 및 로드맵(Session Header & Roadmap) -->
<!-- SECTION_CORE: SC-01 -->

## §1 — 세션 헤더 및 로드맵(Session Header & Roadmap)

**Session 13 — 개체 간 변이(IIV / BSV)와 공변량 모델링**
*Source: Rowland M, Tozer TN. **Clinical Pharmacokinetics and Pharmacodynamics: Concepts and Applications**, 5th ed. Lippincott Williams & Wilkins/Wolters Kluwer (이하 **R&T 5e**) Ch.12 (p.361–392) + Ch.13 (p.393–410); Gabrielsson J, Weiner D. **Pharmacokinetic and Pharmacodynamic Data Analysis: Concepts and Applications**, 5th ed. Swedish Pharmaceutical Press, Stockholm (이하 **G&W 5e**) Ch.4 일부 (p.333–352) + PK50 (p.704–710)*

> 📚 **출처 인용 약어 규약** — 본 자료에서 `[R&T p.xxx]`는 Rowland & Tozer 5e의 해당 페이지를, `[G&W p.xxx]`는 Gabrielsson & Weiner 5e의 해당 페이지를 가리킵니다. 두 교과서 외 후속 구현·규제 표준은 `[교과서 외 구현/규제 표준]` 태그로 명시하며, 가능한 경우 1차 문헌(Beal 2001; Savic & Karlsson 2009; Jonsson & Karlsson 1998; Bergstrand & Karlsson 2009 등)을 함께 기재합니다.

### 세 층의 사고 지도

오늘 머릿속에 세 층을 동시에 띄워 놓고 들으시면 됩니다.

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

이 세션이 PopPK 커리큘럼에서 어디 있는지도 한 번 짚고 갈게요.

```text
[선행: 1·2구획, CL/V/t1/2, 단백결합, NONMEM 기초]
        → [이 세션: IIV/IOV/RUV, θ/η/ε, Ω/Σ, 공변량, 유전 하위구조]
        → [후속: FOCE/FOCE-I, GOF/CWRES, η-EBE, shrinkage, stepwise covariate selection]
```

🧭 **카드를 읽는 순서:**
C1 — 평균 파라미터만으로는 왜 개별 환자를 설명할 수 없을까.
C2 — 잔차 오차를 먼저 정하지 않으면 왜 뒤이은 공변량 신호가 가짜가 될까.
C3 — 공변량은 $\omega^2$를 깎는 통계 기법인가, 아니면 생리학에 이름을 붙이는 일인가.
C4 — 매끈해 보이는 $\eta$ 안에 유전형 하위군이 숨어 있을 때 뭘 보면 알아차릴까.

### 오늘의 핵심 아이디어

NONMEM의 혼합효과 모델(고정효과인 $\theta$와 무작위효과 $\eta$/$\varepsilon$을 같이 추정하는 구조)은 결국 한 가지를 합니다 — **관측값을 $\theta$(인구 평균), $\eta$(개체 편차), $\varepsilon$(잔차)로 쪼개고, 그 흔들림의 크기인 $\omega^2$와 $\sigma^2$를 따로 따로 추정**해요. 공변량은 $\omega^2$에 섞여 있던 생리학을 끄집어내 이름 붙이는 도구고, 유전 다형성은 매끈해 보이던 $\omega^2$ 안에 숨어 있는 불연속 봉우리입니다. `[R&T p.369–373; p.393–410]`

G&W는 항상 이론보다 먼저 데이터의 모양을 보라고 해요. 그래서 공변량 모델은 control stream에서 시작하는 게 아닙니다. **spaghetti plot · dose-normalized plot · 변환 plot에서 "어떤 환자들이 왜 갈라지는지"를 눈으로 먼저 확인하는 데서 시작**합니다. `[G&W p.334–336]`

> 💡 **오늘 세션을 관통하는 한 가지 — 변이 보존 법칙**
> 같은 데이터셋에서 $\omega^2$와 $\sigma^2$는 같은 "전체 미설명 변이"를 두고 zero-sum으로 다툽니다. $\varepsilon$이 못 흡수한 분산은 반드시 $\eta$로 새고, 그 반대도 같아요. 그래서 카드 순서가 **C1(그릇 분류) → C2(잔차 그릇 잠그기) → C3($\eta$ 안의 설명가능 부분을 $\theta$로 옮기기) → C4($\eta$ 분포 모양 점검)** 으로 결정됩니다. 이 순서를 어기면 NONMEM은 돌아가지만 용량 개체화는 무너집니다.

### 카드 흐름 한눈에

```text
C1. θ / η / ε taxonomy
     ↓
C2. residual error model: ε의 형태를 정한다
     ↓
C3. covariate model: ω² 일부를 설명 가능한 생리학으로 옮긴다
     ↓
C4. genetic polymorphism: ω² 안의 불연속 substructure를 드러낸다
```

### 지식 그래프상 위치

| 위치 | 내용 |
|---|---|
| 선행 전제 | 1-구획·2-구획 모델, CL/V/$t_{1/2}$, 단백 결합, NONMEM 기초 syntax |
| 본 세션 | IIV / 시점 간 변이(IOV) / 잔차 미설명 변이(RUV), $\theta$/$\eta$/$\varepsilon$, $\omega^2$/$\sigma^2$, 공변량, 유전형/표현형 변이 |
| 직후 후속 | FOCE / FOCE-I, GOF / CWRES / $\eta$-EBE, shrinkage, stepwise covariate selection |
| 임상 번역 | Bayesian TDM, 용량 개체화, 치료적 창, PopPK 보고서 일관성 |

### IIV · IOV · RUV — 세 그릇의 차이부터 잡고 갑니다 `[실무 통합, v3.5.3]`

이름이 비슷해서 헷갈리는데, 셋은 완전히 다른 그릇이에요.

| 그릇 | 무엇을 담는가 | 핵심 질문 | NONMEM에서는 |
|---|---|---|---|
| **IIV** (inter-individual) | 사람 사이의 **지속적** 차이 — 어떤 사람은 평소 CL이 크고, 어떤 사람은 평소 작고 | 사람마다 지속적으로 다른가? | $\omega^2$ |
| **IOV** (inter-occasion) | 같은 사람 안에서 visit/cycle/period 사이의 반복 차이 | 같은 사람도 occasion마다 달라지는가? | occasion-level random effect (별도 ETA로 분리) |
| **RUV** (residual unexplained) | 관측값 하나하나에서 남는 흔들림 — 같은 사람, 같은 occasion, 같은 구조 모델 뒤에도 남는 noise | 한 시점 관측값 자체에 남는 오차인가? | $\sigma^2$ |

**IOV를 무시하면 어떻게 망가지냐.** 같은 사람 안의 occasion별 변화가 IIV나 RUV로 잘못 흡수돼요. 그러면 $\omega^2$, $\sigma^2$, EBE, shrinkage, covariate signal 해석이 다 같이 왜곡됩니다. 특히 **반복 period crossover 시험, oncology cycle dosing, TDM 재방문, 효소 유도/억제 회복 자료, 복약 순응도 변동 자료** — 이런 데이터에서는 "사람이 다른 것"과 "같은 사람의 occasion이 다른 것"을 반드시 분리해야 해요.

NONMEM에서 IOV는 occasion-level ETA로 구현됩니다. 핵심은 `$OMEGA` block을 무작정 늘리는 게 아니라 **어느 그릇에 어떤 반복 구조를 담을지** 결정하는 거예요. 다음 네 가지를 먼저 봅니다:
- 같은 사람 안에서 visit/cycle/period별로 일관된 shift가 보이는가
- residual plot만으로 설명되지 않는 occasion 단위 bias가 남는가
- 공변량 효과처럼 보이는 신호가 사실은 occasion imbalance 때문일 가능성은 없는가
- IOV를 넣었더니 IIV·RUV·covariate effect가 더 해석 가능해지는가

**한 줄로:** IIV는 사람 간 차이, IOV는 같은 사람 안의 occasion 간 차이, RUV는 관측값 수준의 남은 오차.

**IOV vs TVC — 같은 변동처럼 보이지만 다른 그릇.** `[교과서 외 구현/규제 표준; 개념 근거: R&T p.371]`

같은 사람 안에서 시간에 따라 변하는 신호가 두 가지 형태로 나타나요. 둘은 들어가는 그릇과 처리 방식이 완전히 다릅니다.

| 구분 | IOV (inter-occasion variability) | TVC (time-varying covariate) |
|---|---|---|
| 어디로 들어가는가 | random effect로 — occasion별 $\eta$ (`$OMEGA`) | $\theta$ 구조 안으로 — 시간에 따라 변하는 공변량 값 |
| 무엇을 표현하는가 | 같은 사람의 visit/cycle 간 **이름 붙일 수 없는 무작위 변동** | 측정한 시간 가변 변수(체중, SCr, 동반약물)가 PK를 변화시키는 **구조적·인과적 효과** |
| NONMEM 구현 | occasion ETA를 별도 OMEGA로 추가 | `$INPUT`에 시점별 공변량 + `IF (TIME≥...) CL = θ₁·(SCr_t/SCr_ref)^θ₂` 분기 |
| 임상 예시 | crossover 시험 period 간 흡수 변동 | ICU 환자의 일별 SCr 변동, oncology cycle 간 체중 손실, 효소 유도제(rifampin) 추가 시점 |

특히 **ICU·oncology·만성질환 추적 데이터**에서 결정적이에요. 환자의 SCr이 입원 중 매일 변하면, baseline SCr 하나로 fixed covariate 처리하는 게 아니라 시점별 SCr을 TVC로 넣어야 합니다. 이걸 IOV로 잘못 처리하면 "SCr이 CL을 결정한다"는 mechanistic 신호가 random effect로 흡수돼 사라져요 — 진단 시그니처 3 `Vanishing Covariate Cascade`의 시간 가변 버전입니다.

$$
\underbrace{CL_{ij}}_{\text{i번째 환자, j번째 시점 CL}}
=
\underbrace{\theta_1}_{\text{기준 CL}}
\cdot
\overbrace{\left(\frac{SCr_{ij}}{SCr_{ref}}\right)^{\theta_2}}^{\text{시점별 신기능 배율 (TVC)}}
\cdot
\underbrace{\exp(\eta_i)}_{\text{지속적 IIV}}
\cdot
\underbrace{\exp(\eta_{ik})}_{\text{occasion k의 IOV}}
$$

⚠️ **흔한 오해.** "시간에 따라 변하는 값이니까 IOV로 처리한다"는 직관은 틀려요. **변동의 원인이 측정 가능한 변수(SCr, 체중)이면 TVC**, 측정 불가능한 무작위 변동이면 IOV입니다.

**§1 정리.** 이 세션의 질문은 "사람마다 다르다"가 아닙니다. "그 다름 중에서 무엇이 $\theta$이고, 무엇이 $\eta$이고, 무엇이 $\varepsilon$이고, 무엇이 공변량이냐"입니다.

---

<!-- SLIDE_START: §2 | title: 개념 해부 카드(Concept Anatomy Cards) -->
<!-- SECTION_CORE: SC-02 -->

## §2 — 개념 해부 카드(Concept Anatomy Cards)

---

<!-- SLIDE_START: C1 | title: 변이의 구조적 분해 — θ, η, ε 분류 체계(taxonomy) -->
<!-- SECTION_CORE: SC-03 -->

### C1. 변이의 구조적 분해 — $\theta$, $\eta$, $\varepsilon$ 분류 체계(taxonomy)

> **거장의 시각**
> $\theta$, $\eta$, $\varepsilon$를 그냥 기호로만 외우면 `$OMEGA`랑 `$SIGMA`는 보고서에서 숫자 두 개로 끝나요. 그런데 어느 변이가 어느 그릇에 들어가는지를 한 번 잡으면, 뒤에 나올 C2의 잔차 모델, C3의 공변량, C4의 분포 구조가 한 줄로 꿰입니다.

#### A. 형식적 정의

`[교과서 외 구현/통계 번역; 개념 근거: R&T p.369–373]`

$$
\underbrace{Y_{ij}}_{\text{관측값}}
=
\underbrace{f(\boldsymbol{\theta},\boldsymbol{\eta_i},x_{ij})}_{\text{개인 예측}}
+
\underbrace{g(\boldsymbol{\theta},\boldsymbol{\eta_i},x_{ij})}_{\text{오차 스케일}}
\underbrace{\varepsilon_{ij}}_{\text{잔차}}
$$

| 파라미터 | 단위 | 무엇을 뜻하나 | 무엇 때문에 변하나 |
|---|---|---|---|
| $Y_{ij}$ | 농도 또는 반응 단위 | i번째 사람의 j번째 관측값 | 측정 시점, assay, 실제 노출 |
| $\theta$ | 파라미터별 단위 | 모집단 대표값 | 대상 집단, 모델 구조 |
| $\eta_i$ | 무차원 random effect | 그 사람이 모집단 중심에서 얼마나 벗어났는지 | 생리학, 유전형, 질병 상태, 우리가 아직 못 잡은 공변량 |
| $\varepsilon_{ij}$ | 무차원 또는 관측 단위 | 관측 한 점의 잔차 | assay 오차, sampling 오차, 구조/오차 모델 결함 |
| $\omega^2$ / $\sigma^2$ | 분산 | 사람 간 흔들림 / 관측 잔차 흔들림의 크기 | 그릇 배정, 모델 오지정, 자료 정보량 |

개인 청소율을 지수형 IIV(exponential IIV)로 쓰면 이렇게 됩니다.

$$
\underbrace{CL_i}_{\text{개인 CL}}
=
\underbrace{CL}_{\text{모집단 CL}}
\cdot
\underbrace{\exp(\eta_i)}_{\text{IIV 배율}}
$$

왜 지수형이냐. **CL을 음수로 만들지 않으면서 변동계수(CV)가 농도 범위 전반에서 거의 일정하게 유지되거든요**. 그래서 집단 분석에서 디폴트로 자주 씁니다. `[R&T p.371]` 작은 $\omega$에서는 교육용 근사로 $CV(\%) \approx \omega \cdot 100$을 쓰고요.

> 💡 **세 층을 한 번에 떠올리는 비유** — $\theta$는 지도 위 도시 중심, $\eta$는 그 사람이 그 중심에서 어느 동네에 사는지, $\varepsilon$은 주소를 GPS로 찍을 때마다 생기는 좌표 흔들림입니다. 셋을 분리하지 않으면 `$OMEGA`랑 `$SIGMA`는 의미 없는 숫자가 돼요.

⚠️ **헷갈리지 마세요.** $\omega^2$와 $\sigma^2$ 둘 다 "오차"가 아닙니다. $\omega^2$는 **사람 간 지속적인 차이**, $\sigma^2$는 **관측값 한 점에서 남는 흔들림**.

🔑 **control stream 읽는 순서.** `$OMEGA` 구조부터 → `$SIGMA` 구조 → `$THETA` 초기값. 이 순서로 보면 모델러가 생리학적 상관과 잔차 구조를 어떻게 가정했는지 빠르게 잡혀요.

#### B. 데이터 앵커: 평균보다 분포가 먼저예요

R&T의 **warfarin**(비타민K 길항 항응고제, CYP2C9로 대사, 표적은 VKORC1) 200명 자료에서, 비슷한 항응고 효과를 얻는 1일 용량이 사람마다 굉장히 넓게 흩어집니다. **Nortriptyline**(삼환계 항우울제, CYP2D6로 대사) 25 mg tid를 복용한 263명의 정상상태 농도는 선형 스케일로 보면 비대칭(skewed)인데 로그 스케일로 옮기면 거의 대칭이에요. → 그래서 **같은 약, 같은 평균이라도 분포 모양을 안 보면 dose individualization 문제는 해결되는 게 아니라 가려진다**는 사실의 임상 예입니다. `[R&T p.362–363]`

G&W도 다중 환자 자료는 먼저 개별 프로파일과 통합 자료(pooled data)를 그려 보라고 합니다. Figure 4.2의 spaghetti plot은 같은 용량을 받아도 일본인 그룹과 백인 그룹의 노출 프로파일이 달라질 수 있음을 보여 줘요. 평균 + 오차 막대보다 spaghetti plot이 변이를 훨씬 더 잘 드러냅니다. `[G&W p.335–336]`

**NAD/NPD vs population approach.** NAD(Naive Averaged Data)는 시간점별 평균 농도에 모델을 맞추는 방식, NPD(Naive Pooled Data)는 모든 관측값을 한 사람 자료처럼 합쳐서 적합하는 방식이에요. G&W는 이런 평균 자료 적합이 편향된 파라미터와 변이를 만들 수 있다고 명확히 경고합니다 — 그래서 집단 접근법(population analysis)이 필요해요. `[G&W p.335–336]`

> 📖 **R&T 5e p.366, Figure 12-6** — 네 가상 약물 청소율의 빈도분포를 한 장에 같이 띄워 놓은 그림이에요. 핵심은 이거예요: 같은 평균이라도 CV와 분포 모양이 다르면 개별 용량 결정의 의미가 완전히 달라집니다. 특히 이봉형(bimodal) 분포에서는 **평균이 모집단 대표값이 아니라 오히려 가장 덜 그럴듯한 값**이 됩니다.

#### C. 왜 이런 구조여야 하는가

| 상황 | 파라미터 변화 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| $\theta$ 하나만 사용 | 개인별 $\eta$가 모델에 없음 | → | 좁은 치료적 창에서 독성/무효 노출 환자를 설명 못함 `[R&T p.370]` | IIV 구조 명시 |
| 잔차 모델이 산포를 설명 못함 | $\sigma^2$가 $\omega^2$로 새어 나감 | → | 가짜 IIV 또는 가짜 공변량 신호 | C2 잔차 모델 우선 검토 |
| 표준 2단계 분석에 rich sampling 부족 | 구조·분산 파라미터 분리 추정 불안정 | → | sparse data에서 편향 | population approach로 동시 추정 `[R&T p.369]` |
| OFV만 보고 모델 채택 | $\theta$, $\omega$, $\sigma$ 동시 조정 결과 과해석 | → | 공변량의 생물학적 의미 과대 주장 | LRT/AIC + 진단 plot 병행 `[R&T p.373]` |

OFV는 적합의 언어예요. 최대가능도가 $\theta$, $\omega$, $\sigma$를 동시에 조정하면서 OFV를 최소화합니다. 내포 모델에서는 $\Delta OFV \geq 3.84$(df=1, α=0.05)가 LRT 기준, 비내포 모델에서는 AIC를 씁니다. `[R&T p.373]`

#### D. 이 모델이 작동하는 경계 조건

| 경계 조건 | 어겼을 때 신호 |
|---|---|
| $\eta$ 분포가 단봉형/로그정규여야 함 | 이봉형 히스토그램 → 유전형/표현형 하위군 가능성 `[R&T p.366, p.393–397]` |
| $\varepsilon$가 평균 0, 분산 $\sigma^2$의 무작위 잔차여야 함 | 잔차에 추세가 남으면 구조 모델 또는 오차 모델이 변이의 원인을 아직 설명 못한 것 `[R&T p.372]` |
| 희소 자료도 같은 모집단에서 왔다고 볼 수 있어야 함 | 이질적 모집단이 섞이면 모집단 평균과 $\omega^2$가 모두 왜곡 |
| 공변량이 식별 가능해야 함 | 데이터가 정보를 주지 않으면 파라미터는 숫자로만 존재 `[G&W p.348–351]` |

#### E. EBE와 shrinkage — "$\eta$를 봤다"는 착각이 어떻게 생기나

EBE(empirical Bayes estimate; 경험적 베이즈 추정치)는 모집단 수준 파라미터($\theta$, $\omega^2$, $\sigma^2$)와 그 사람의 관측치를 같이 써서 나온 **사후추정치**예요. 즉 EBE는 그 사람의 "참값"이 아니라, 모델 가정과 그 사람이 제공한 자료의 양·질이 허용하는 범위 안에서 나온 조건부 추정치입니다. **Shrinkage**는 그 사람이 제공한 정보가 부족할 때 EBE가 모집단 평균(0) 쪽으로 끌려가는 현상이에요.

**$\eta$-shrinkage의 정량적 정의 (Savic & Karlsson, 2009).** `[교과서 외 후속 구현/규제 표준; 1차 문헌: Savic RM, Karlsson MO. Importance of shrinkage in empirical Bayes estimates for diagnostics. *AAPS J.* 2009;11(3):558–569]`

$$
\underbrace{\eta\text{-shrinkage}}_{\text{EBE 압축률}}
=
1 - \frac{\overbrace{SD(\eta_{EBE,i})}^{\text{개인 EBE의 표본 표준편차}}}{\underbrace{\omega}_{\text{모집단 표준편차}}}
$$

해석은 간단해요. **자료가 개인 $\eta$를 잘 식별하면 EBE 분포의 표본 SD가 모집단 $\omega$에 가까워지고 (shrinkage ≈ 0), 자료 정보가 부족하면 EBE가 0 쪽으로 압축되면서 SD($\eta_{EBE}$) < $\omega$가 됩니다.** Savic-Karlsson은 다음 임계를 제시합니다.

| Shrinkage 값 | 해석 | EBE 기반 진단의 신뢰도 |
|---|---|---|
| < 20% | 자료가 $\eta$를 잘 식별 | 신뢰 가능 |
| 20–30% | 주의 영역 | 해석 조심 |
| > 30% | **자료 정보 부족; EBE가 모집단 평균으로 압축** | **EBE 기반 plot 신뢰 불가** |

§8의 거장의 질문 표에서 등장하는 "$\eta$-shrinkage < 30%" 경고선의 출처가 바로 이 임계예요. 30%를 넘으면 $\eta_{EBE}$-vs-covariate scatter, $\eta$ histogram, GOF에서의 individual prediction plot이 모두 분해능을 잃고, 진짜 공변량 신호와 estimation artifact를 구분하기 어려워집니다.

| 연결 지점 | 실무 해석 |
|---|---|
| 높은 shrinkage | EBE-vs-covariate plot이랑 ETA diagnostic의 분해능이 떨어집니다 |
| 약한 공변량 신호 | 생물학이 없는 게 아니라 정보 부족 / residual misspecification / ETA-epsilon leakage / 추정 알고리즘 한계일 수 있어요 |
| 공변량 모델링 | 진짜 생물학 신호와 estimation artifact를 분리해서 봐야 합니다 |

기억할 한 줄: **EBE plot은 현미경이 아니라, 모델·자료·추정법이 함께 만든 그림자**예요.

#### F. 상관된 random effect — OMEGA BLOCK 구조 `[교과서 외 구현/규제 표준; 개념 근거: R&T p.369–373]`

C1 §A의 IIV 식은 각 파라미터에 독립된 $\eta$를 하나씩 부여하는 **diagonal $\Omega$** 구조였어요. 그런데 실무 PopPK 분석을 한 번이라도 돌려 보면 곧 깨닫습니다 — **CL과 V의 $\eta$는 거의 항상 상관**됩니다. 체격이 큰 환자는 보통 CL도 크고 V도 크니까요. 같은 사람의 두 random effect가 공유하는 변이가 있는데, 이걸 무시하고 diagonal로만 가면 다음 세 가지가 동시에 일어나요.

- $\omega^2(CL)$과 $\omega^2(V)$가 **과대 추정**됩니다 (공유 변이를 두 그릇이 각자 흡수)
- Bayesian TDM의 posterior CL·V 예측이 부정확해집니다 (개인 추정 시 두 $\eta$가 사전 독립으로 가정됨)
- $\eta$-shrinkage 진단이 왜곡됩니다 (참 상관이 무시되면 EBE 압축 패턴이 실제와 달라짐)

NONMEM `$OMEGA BLOCK(2)`은 대각 분산뿐 아니라 off-diagonal **공분산** $\omega_{CL,V}$를 같이 추정해서 이 상관을 명시적으로 모델링합니다.

$$
\underbrace{\Omega}_{\text{IIV 분산-공분산 행렬}}
=
\begin{pmatrix}
\overbrace{\omega^2_{CL}}^{\text{CL 분산}} & \overbrace{\omega_{CL,V}}^{\text{공분산}} \\
\underbrace{\omega_{CL,V}}_{\text{공분산}} & \underbrace{\omega^2_{V}}_{\text{V 분산}}
\end{pmatrix}
$$

상관 계수는 다음으로 변환해 해석합니다.

$$
\underbrace{\rho_{CL,V}}_{\text{CL-V 상관계수}}
=
\frac{\overbrace{\omega_{CL,V}}^{\text{공분산}}}{\underbrace{\omega_{CL}\cdot\omega_{V}}_{\text{표준편차 곱}}}
$$

| $|\rho|$ 범위 | 해석 | 조치 |
|---|---|---|
| < 0.3 | 약한 상관 | diagonal로 유지하거나 BLOCK 선택사항 |
| 0.4–0.7 | 의미 있는 상관 | **BLOCK 구조 정당화** — 권장 |
| > 0.9 | 거의 완전 상관 | 두 파라미터가 사실상 같은 정보 — **모델 식별성 재점검** |

```nmtran
; [교과서 외 구현 번역]
$OMEGA BLOCK(2)
 0.09             ; ω²(CL) 초기값 (CV ≈ 30%)
 0.04  0.09       ; ω(CL,V) 공분산, ω²(V)
```

> 💼 **실무 인사이트.** Diagonal로 시작해 OFV·shrinkage·VPC가 모두 안정된 다음 BLOCK으로 확장하세요. 정보량이 부족한 자료에서 BLOCK을 처음부터 잡으면 `$COV step`이 "non-positive definite"로 실패하기 쉽고, 그 실패 자체가 자료 정보량 부족의 신호예요. NDA 보고서에서는 diagonal vs BLOCK 비교 OFV와 $\rho_{CL,V}$의 95% CI를 함께 제시하는 게 표준입니다.

⚠️ **헷갈림 방지.** "$\omega^2$가 커 보이면 BLOCK으로 풀면 줄어든다"는 직관은 절반만 맞아요. **공유 변이가 있으면** 줄어들지만, **참으로 독립인 변이**까지 BLOCK으로 묶으면 오히려 추정이 불안정해집니다. Diagonal-우선 원칙은 보수성과 식별성 둘 다를 보호하는 장치예요.

```yaml
aliases: [IIV, BSV, NLME taxonomy, theta-eta-epsilon]
tags: [pharmacometrics/poppk, nonmem/omega, statistics/nlme]
source: "R&T p.369-373; G&W p.335-336; G&W PK50 p.704-708"
```

**이번 카드 핵심내용**
- 개인 CL·V가 평균에서 지속적으로 벗어나면 → $\eta$와 $\omega^2$의 영역
- 같은 사람의 관측값이 예측 주변에서 흔들리면 → $\varepsilon$와 $\sigma^2$의 영역
- EBE plot을 그 사람의 참값처럼 읽기 전에 → shrinkage와 자료 정보량을 먼저 보세요
- 잔차 실패를 IIV 성공으로 잘못 해석하는 순간 → 공변량 탐색이 가짜 생리학을 만들어내고, dose individualization이 무너집니다

---

<!-- SLIDE_START: C2 | title: 잔차 오차 모델 — additive / proportional / exponential -->
<!-- SECTION_CORE: SC-04 -->

### C2. 잔차 오차 모델 — 가법형(additive) / 비례형(proportional) / 지수형(exponential)

앞 C1에서 $\eta$와 $\varepsilon$의 그릇을 나눠 잡았으니, 이번엔 그 잔차 그릇 ($\varepsilon$) 이 어떤 스케일로 흔들리는지를 먼저 정해야 합니다.

> **거장의 시각**
> 잔차 모델을 그냥 "측정 노이즈 부록" 정도로 보면, $\varepsilon$이 못 설명한 패턴이 $\eta$와 공변량 신호로 둔갑해서 모델 안에 들어옵니다. $\varepsilon$의 스케일을 먼저 잡아두면, C3에서 남은 $\omega^2$ 중 무엇이 진짜 생리학인지 보이기 시작해요.

#### A. 형식적 정의

R&T가 제시하는 잔차 변이 모델은 세 가지입니다. `[R&T p.372]`

| 모델 | 식 | 어떻게 읽나 |
|---|---|---|
| 가법형(Additive) | $\underbrace{Y}_{\text{관측값}}=\underbrace{F}_{\text{예측값}}+\underbrace{\varepsilon}_{\text{절대오차}}$ | 절대오차가 농도와 거의 무관하게 일정 |
| 비례형(Proportional) | $\underbrace{Y}_{\text{관측값}}=\underbrace{F}_{\text{예측값}}(1+\underbrace{\varepsilon}_{\text{상대오차}})$ | CV가 농도 범위 전반에서 거의 일정 |
| 지수형(Exponential) | $\underbrace{Y}_{\text{관측값}}=\underbrace{F}_{\text{예측값}}\underbrace{\exp(\varepsilon)}_{\text{오차 배율}}$ | 양수 보장; 로그 영역에서 가법 오차가 됨 |

로그 변환 후 지수형 오차는 가법형이 됩니다. `[R&T p.373]`

$$
\underbrace{\ln Y}_{\text{로그 관측값}}
=
\underbrace{\ln F}_{\text{로그 예측값}}
+
\underbrace{\varepsilon}_{\text{로그 잔차}}
$$

| 파라미터 | 단위 | 무엇을 뜻하나 | 무엇 때문에 변하나 |
|---|---|---|---|
| $Y$ | 농도 또는 반응 단위 | 실제 관측값 | assay, sampling, 구조 모델 적합도 |
| $F$ | $Y$와 동일 | 모델 예측값 | $\theta$, $\eta$, 투여/시간 정보 |
| $\varepsilon$ | 오차 모델별 단위 | 관측 수준 잔차 | assay SD/CV, LLOQ, residual misspecification |
| $\sigma^2$ | 분산 | 잔차 변이 크기 | 오차 구조, 측정 정확도, 모델 누락 패턴 |

> 💡 **세 모델을 한 줄로 구분.** Additive는 "몇 단위 틀리는가", proportional은 "몇 % 틀리는가", exponential은 "로그 스케일에서 얼마나 틀리는가"를 묻는 모델이에요.

⚠️ **헷갈림 방지.** 실무에서 combined/mixed residual model을 정말 자주 쓰는데, R&T p.372에 직접 열거된 출처 모델은 가법형·비례형·지수형 세 가지예요. 그래서 결합형은 source-derived가 아니라 구현 번역으로 둡니다.

🔑 **잔차 우선 규칙.** 공변량을 넣기 전에 CWRES vs PRED/TIME에서 residual pattern이 구조적이지 않은지 먼저 확인하세요.

#### B. 코드 구조

```nmtran
; [교과서 외 구현 번역]
$ERROR
IPRED = F                                       ; individual prediction을 잔차 모델의 중심으로
W     = SQRT((THETA(3)*IPRED)**2 + THETA(4)**2) ; 비례 성분 + 가법 성분을 잔차 스케일 W로 결합
Y     = IPRED + W*EPS(1)                        ; 표준 잔차 EPS(1)을 W만큼 확대해 관측값 생성
```

$$
\underbrace{Y}_{\text{관측값}}
=
\underbrace{IPRED}_{\text{개인 예측}}
+
\overbrace{\sqrt{\underbrace{(\theta_{prop}\cdot IPRED)^2}_{\text{비례 성분}}+\underbrace{\theta_{add}^2}_{\text{가법 성분}}}}^{\text{잔차 스케일}}
\underbrace{\varepsilon}_{\text{표준 잔차}}
$$

> 💡 **$W$의 역할.** Combined model의 $W$는 카메라 흔들림 보정 장치 같아요. LLOQ 근처(어두운 영역)의 절대 흔들림과 고농도(밝은 영역)의 상대 흔들림을 한 렌즈로 동시에 잡아주는 역할입니다.

이 코드는 비례 성분과 가법 성분을 하나의 `W`로 합친 구현입니다. 하지만 본문의 핵심은 코드가 아니라 R&T가 못 박는 조건 — **잔차가 무작위, 평균 0, 분산 $\sigma^2$이어야 한다**는 것입니다. `[R&T p.372]`

#### C. 왜 잔차를 먼저 잡아야 하나

잔차 모델 결정은 공변량 선택보다 반드시 앞서야 합니다. 예를 들어 고농도에서 잔차 산포가 커지는 자료에 가법 오차만 쓰면, 모델은 그 산포를 어떻게든 설명하려고 $\omega^2$를 과대 추정하거나 가짜 공변량 신호를 만들어요. 반대로 LLOQ 근처 절대오차가 큰 자료에 비례 오차만 쓰면, 저농도 잔차 패턴이 체계적으로 남습니다.

R&T는 명시적으로 적습니다 — 잔차 변이가 완전히 무작위여야 하며, 그렇지 않으면 구조 모델 또는 오차 모델이 중요한 변이의 원인을 설명하지 못한 것이다. `[R&T p.372]`

| 상황 | 파라미터 변화 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| 고농도에서 residual spread 증가 | $\sigma^2$ 구조 부적합, $\omega^2$ 과대 가능 | → | 가짜 IIV 또는 가짜 공변량 | 비례/지수형 검토 |
| LLOQ 근처 절대오차 큼 | proportional-only가 저농도 spread를 설명 못함 | → | $\omega^2$(CL) 과대 — funnel 패턴 | additive 또는 combined 성분 검토 |
| 농도 dynamic range ≥ 2 log | 로그 스케일 오차 구조 필요 | → | 원스케일 잔차 추세 | log-transform + additive on log scale 검토 |
| residual trend 잔존 | 구조/오차 모델 미설명 | → | covariate artifact | 공변량 전에 residual model 재검토 |

#### D. 경계 조건

| 자료의 모습 | 권장 첫 모델 |
|---|---|
| 농도 범위가 좁고 측정 SD가 거의 일정 | 가법형 검토 |
| 넓은 농도 범위에 CV가 거의 일정 | 비례형 또는 지수형 검토 |
| 여러 자릿수(order of magnitude)의 자료 | 자연로그 변환 + 변환된 오차 모델 `[R&T p.373; G&W p.337–339]` |
| 잔차에 추세가 남음 | 공변량 전에 구조/오차 모델부터 재검토 |

> 📖 **R&T 5e p.371, Figure 12-12** — 등분산성(homoscedastic)과 이분산성(heteroscedastic) 파라미터 변이를 옆에 같이 띄워 보여 주는 그림이에요. 가법형·비례형·지수형이 식만 보면 서로 다른 문법처럼 보이는데, 이 그림 한 장이 잔차 산포가 일정한지 예측값 크기에 따라 커지는지를 눈으로 한 번에 잡아 줍니다.

#### E. 한계 — 이 카드 결과를 PopPK로 가져갈 때의 위험

- Shrinkage의 정량적 공식과 20–30% 임계는 본 자료 C1 §E에서 다룹니다 (Savic & Karlsson, 2009). 본 카드에서는 잔차 모델 결정이 shrinkage에 미치는 영향만 다루며, EBE 진단의 신뢰도 평가는 C1 §E의 임계 기준에 따릅니다.
- 희소 표본에서 $\eta$-EBE와 잔차 플롯을 해석할 때, 낮은 shrinkage와 정규분포처럼 보이는 $\eta$ 히스토그램을 "좋은 모델의 증거"로 단정하지 마세요. **데이터가 EBE를 실제로 식별할 수 있었는지를 먼저 물어야** 합니다.

> 💼 **실무에서 한 가지만 가져간다면** — "**잔차 모델이 틀리면 그 흔들림이 IIV 신호로 둔갑해서 보입니다**". 잔차를 틀리면 공변량 모델은 정교해지는 게 아니라 정교하게 틀립니다.

> 🔬 **진단 시그니처 1 — `ω²–σ² Leakage Funnel`**
> **어떤 모습인가:** Proportional-only RUV를 LLOQ-rich data(저농도 관측이 많은 자료)에 쓰면, $\omega^2$(CL)이 비현실적으로 부풀고, CWRES vs PRED plot에서 LLOQ 근처에 funnel 모양이 보이며, 동시에 $\eta$-shrinkage가 치솟습니다.
> **왜 일어나나:** 저농도에서 절대오차가 큰 자료에 proportional error만 쓰면 잔차가 설명 못한 spread가 $\omega^2$로 새어 가짜 IIV를 만들어요. C1의 보존 법칙이 실시간으로 작동하는 장면입니다.
> **꿀팁:** "$\omega^2$이 너무 크다"는 느낌이 들 때 가장 먼저 의심할 건 새 covariate가 아니라 **잔차 모델 좌표**입니다. CWRES plot의 funnel은 covariate 검색을 시작하라는 신호가 아니라 RUV를 다시 짜라는 신호예요.
> **실무 활용:** Assay LLOQ가 관측 범위 하단에 가까우면 a priori로 mixed residual로 시작하고, additive component는 assay validation 보고서의 SD에 a priori-tied하게 둡니다. 모델 lock 시점에 mixed 채택 근거(assay characteristic, sampling design)를 같이 기록해야 post-hoc 인상을 피할 수 있어요.

#### F. BQL/LOQ 데이터 처리 — M1/M3/M5/M6 (Beal, 2001) `[교과서 외 구현/규제 표준; 1차 문헌: Beal SL. Ways to fit a PK model with some data below the quantification limit. *J Pharmacokinet Pharmacodyn.* 2001;28(5):481–504]`

C2 §A–E가 정의한 잔차 모델은 LLOQ(lower limit of quantification) **위쪽** 관측값만을 다루는 도구예요. 그런데 현대 PopPK 분석의 5–30%는 LLOQ 미만 (**BQL**, below quantification limit) 관측을 어떻게 처리하느냐로 결과가 달라집니다. 진단 시그니처 1 `Leakage Funnel`이 실제로 가장 심하게 일어나는 영역이 바로 LLOQ 근처예요 — BQL 처리법을 정하지 않은 채 funnel을 보면 "어떻게 고치지?"의 답을 받을 수 없습니다.

Beal (2001)이 정리한 표준 처리법은 다음과 같습니다.

| 방법 | 처리 방식 | 편향 | 권고 |
|---|---|---|---|
| **M1** | BQL 관측을 단순 제외 | 큰 편향 — 분포의 한쪽 꼬리가 잘림 | 권고하지 않음 |
| **M2** | LLOQ 미만 관측 likelihood 조건부 처리 (드물게 사용) | 모델·자료에 따라 다름 | 제한적 사용 |
| **M3** | BQL을 **censored data**로 likelihood에 통합 | 가장 작음 (편향 최소) | **현대 표준** |
| **M5** | BQL을 LLOQ/2 단일 값으로 대입 | 중간 — 농도 분포 왜곡 | 보조적 사용 |
| **M6** | 같은 환자의 BQL 첫 관측만 LLOQ/2로 대입, 이후 연속 BQL은 제외 | M5보다 작음 | 보조적 사용 |

M3의 핵심은 "관측값이 정확히 얼마인지는 모르지만, **LLOQ 미만이라는 것은 안다**"는 정보를 부분 likelihood로 살리는 데 있어요. 정량 관측은 정규 likelihood, BQL 관측은 누적분포 likelihood로 분기 처리합니다.

$$
\underbrace{L_i^{BQL}}_{\text{BQL 관측의 likelihood}}
=
\overbrace{\Phi\!\left(\frac{\underbrace{LLOQ}_{\text{정량한계}} - \underbrace{F_{ij}}_{\text{개인 예측}}}{\underbrace{W_{ij}}_{\text{잔차 스케일}}}\right)}^{\text{관측이 LLOQ 미만일 확률}}
$$

여기서 $\Phi$는 표준정규 CDF, $F_{ij}$는 모델 예측값, $W_{ij}$는 C2 §B에서 정의한 combined 잔차 스케일입니다. NONMEM에서는 `$ERROR` 블록의 `F_FLAG=1` 분기로 구현해요.

```nmtran
; [교과서 외 구현 번역; Beal 2001 M3 method]
$ERROR
IPRED = F
W     = SQRT((THETA(3)*IPRED)**2 + THETA(4)**2)

IF (BQL.EQ.0) THEN          ; 정량 가능 관측 → 정규 잔차 모델
  Y      = IPRED + W*EPS(1)
  F_FLAG = 0
ELSE                         ; BQL 관측 → CDF likelihood
  CUMD   = PHI((LLOQ - IPRED)/W)
  Y      = CUMD
  F_FLAG = 1                ; LAPLACE 방법으로 추정 (FOCE-LAPLACE)
ENDIF
```

| 상황 | M1 (제외) | M3 (censoring) | 임상적 함의 |
|---|---|---|---|
| BQL fraction < 5% | 거의 무영향 | 동일 결과 | M1 허용 |
| BQL fraction 5–15% | $\omega^2$(CL) 5–15% 부풀음 | 안정 | M3 권장 |
| BQL fraction > 15% | $\omega^2$·공변량 효과 모두 왜곡 | **M3 필수** | M3로 가지 않으면 funnel 그대로 |
| Terminal phase BQL 다수 | $t_{1/2}$ 추정 편향 | 안정 | M3 + extrapolation 검증 |

> 📚 **출처 주의 — BQL 분율 임계값의 진짜 출처.** `[교과서 외 후속 구현/규제 표준]`
> 위 표의 **5%, 15% 분율 임계는 Beal 2001 원 논문에는 명시되어 있지 않습니다.** Beal 2001은 method 자체 (M1/M3/M5/M6 정의와 likelihood 공식) 의 1차 문헌이지만, **어느 BQL 비율에서 어느 방법이 위험한가**라는 정량 임계는 후속 검증 연구에서 PopPK 실무 표준으로 정착된 값이에요. 핵심 1차 문헌은 다음입니다.
> - **Bergstrand M, Karlsson MO.** Handling data below the limit of quantification in mixed effect models. *AAPS J.* 2009;11(2):371–380 — 시뮬레이션 기반 비교로 5–10% 이상에서 M1의 편향이 임상적으로 의미 있어지고, 15–20% 이상에서 M3 채택이 필수임을 정량적으로 보였습니다.
> - **Ahn JE, Karlsson MO, Dunne A, Ludden TM.** Likelihood based approaches to handling data below the quantification limit using NONMEM VI. *J Pharmacokinet Pharmacodyn.* 2008;35(4):401–421 — 추정 방법별 편향과 권고 사용 영역을 정리했습니다.
>
> 규제 보고서에서는 method 출처(Beal 2001)와 임계 출처(Bergstrand-Karlsson 2009)를 **분리해서** 기재해야 reviewer가 두 권고를 같은 출처로 오인하지 않습니다. "Per Beal (2001), BQL fraction > 15% requires M3" 같은 기술은 부정확해요 — Beal 2001은 임계를 정의하지 않았으니까요.

🔬 **진단 시그니처 1 (Leakage Funnel)과의 직접 연결.** Funnel이 보일 때 가장 먼저 의심해야 할 두 가지가 (1) 잔차 모델 오지정과 (2) BQL 처리 부적절이에요. M1으로 BQL을 제외하고 proportional-only residual을 쓰면, 저농도 정보가 통째로 버려지면서 LLOQ 근처 $\eta$가 인공적으로 부풀어요. **M3 + combined residual model**이 두 문제를 동시에 잡습니다.

> 💼 **규제 방어 문구.** *"Below quantification limit observations were handled using the M3 method (Beal, 2001), with the likelihood of each BQL observation specified as the cumulative probability of falling below LLOQ given individual prediction and residual error model. The decision threshold for M3 adoption (BQL fraction > ~15%) followed Bergstrand & Karlsson (2009). Sensitivity to BQL handling was assessed by re-fitting under M1 and M6 with documented impact on $\omega^2$ and covariate effects (sensitivity table appended)."*

⚠️ **헷갈림 방지.** M3는 추정 방법으로 **FOCE-LAPLACE** 또는 그 이상이 필요해요 (FO·FOCE는 CDF likelihood를 다룰 수 없음). M3를 켜고 FOCE를 그대로 쓰면 NONMEM이 silently fail합니다 — 추정은 끝나지만 BQL 처리가 적용되지 않은 결과가 나와요.

```yaml
aliases: [RUV, residual error, sigma, additive error, proportional error]
tags: [pharmacometrics/nonmem, statistics/residuals]
source: "R&T p.371-373; G&W p.337-339"
```

**이번 카드 핵심내용**
- 고농도에서 잔차 산포가 커진다 → proportional/exponential error의 영역
- LLOQ 근처 절대오차가 크다 → additive 또는 combined 성분의 영역
- 공변량 탐색 전 funnel이 보인다 → covariate가 아니라 residual model을 먼저 수정
- $\varepsilon$ 실패를 $\eta$ 신호로 해석하는 순간 → $\omega^2$ 부풀림 → 가짜 covariate → VPC/CWRES 불일치

---

<!-- SLIDE_START: C3 | title: 공변량 모델링 — CrCl, fu, 재모수화(reparameterization) [⚡ Apex Concept] -->
<!-- SECTION_CORE: SC-05 -->

### C3. 공변량 모델링 — CrCl, $f_u$, 재모수화(reparameterization) `[⚡ Apex Concept]`

C2에서 $\varepsilon$의 좌표를 잠갔어요. 그러면 이제 남은 $\omega^2$ 중에서 **어떤 부분을 생리학적 설명변수로 옮길 수 있는지**를 판단할 차례입니다.

> **거장의 시각**
> 흔한 오해는 이거예요 — "공변량은 $\omega^2$을 줄여 OFV를 개선하는 통계 도구다". 실무에서는 그렇게 보이지만, 사실 **공변량 모델링은 $\omega^2$에 섞여 있던 생리학을 꺼내서 $\theta$ 구조로 옮기고, 그 자리에 이름을 붙이는 일**입니다. Total/unbound 재모수화는 한 발 더 나아가서, 같은 데이터를 아예 다른 좌표에서 다시 읽는 작업이고요.
> 그래서 C3의 질문은 "$\omega^2$이 줄었느냐"가 아니라 "**어느 좌표에서 무엇이 설명되었느냐**"입니다.

#### A. 형식적 정의

공변량 모델링은 $\omega^2$를 **줄이는 기술이 아니에요**. 정확히 말하면 $\omega^2$에 섞여 있던 생리학을 분리해서 **이름을 붙이는 작업**입니다. R&T의 크레아티닌 청소율 예시는 신청소율의 생리학을 $CL_i$에 연결하고, G&W PK50은 비결합 분율 $f_u$(fraction unbound)가 total parameter variability의 일부를 설명한다는 걸 보여 줘요. `[R&T p.369–371; G&W p.706–709]`

R&T는 크레아티닌 청소율이 신청소율 IIV를 설명하는 공변량이 될 수 있다고 합니다. 예시 구조: `[R&T p.369–371]`

$$
\underbrace{CL_i}_{\text{개인 CL}}
=
\underbrace{\theta_1}_{\text{기저 CL}}
+
\underbrace{\theta_2\cdot GFR_i}_{\text{GFR 설명분}}
+
\underbrace{\eta_i}_{\text{남은 편차}}
$$

NONMEM 실무에서는 흔히 중심화 공변량 형태를 씁니다.

```nmtran
; [교과서 외 구현 번역]
CL = THETA(1) * (CRCL/90)**THETA(2) * EXP(ETA(1)) ; CRCL=90 기준 CL × 신기능 배율 × 남은 IIV
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

> 💡 **왜 하필 90인가 — centering value의 선택.** `[교과서 외 구현/규제 표준]`
> $CRCL/90$의 분모 **90 mL·min⁻¹**는 **고정된 보편 기준이 아닙니다.** Dataset-specific choice이며, 다음 세 가지 후보 중 하나를 명시적 근거로 선택합니다.
>
> | 선택지 | $\theta_1$의 임상적 해석 | 사용 맥락 |
> |---|---|---|
> | **모집단 중앙값** (가장 흔함) | 표본 중심의 신기능을 가진 환자의 CL | 일반 PopPK |
> | **정상 신기능 기준** (120 mL·min⁻¹) | 정상 신기능 환자의 CL | 신기능 광범위 자료 |
> | **임상 cutoff** (60 mL·min⁻¹, CKD stage 3 경계) | 신기능 저하 진입 시점의 CL | 신부전 환자 자료 |
>
> 즉 centering value는 단순한 정규화 상수가 아니라 **$\theta_1$의 해석 좌표 자체**를 결정해요. 90은 본 예시 데이터셋의 평균 신기능을 대표하는 값으로 잡은 거지, NONMEM이나 R&T가 정해 준 표준이 아닙니다. 보고서에서는 항상 다음을 명시해야 합니다 — (1) 선택한 centering 값, (2) 그 값의 근거 (모집단 중앙값 / 임상 기준 / 정상값), (3) $\theta_1$이 어떤 신기능 환자의 CL을 의미하는지.

$$
\underbrace{\theta_1}_{\text{보고서의 CL 추정치}}
=
\overbrace{CL\big|_{CRCL=90}}^{\text{centering value에서의 CL}}
\neq
\underbrace{CL_{\text{normal}}}_{\text{정상 환자의 CL (일반적 기대)}}
$$

⚠️ **흔한 함정.** Centering value를 명시하지 않으면 reviewer가 $\theta_1$을 "정상 환자 CL"로 잘못 읽어요. Centering이 90이고 정상이 120이면, 보고된 $\theta_1$은 이미 신기능이 약간 저하된 환자 기준입니다.

| 파라미터 | 단위 | 무엇을 뜻하나 | 무엇 때문에 변하나 |
|---|---|---|---|
| $CL_i$ | L·h⁻¹ | 개인 청소율 | 신기능, 간기능, 체중, 유전형, 병태 |
| $\theta_1$ | L·h⁻¹ | 기준 공변량값에서의 CL | 대상 집단, 기준 CRCL 설정 |
| $\theta_2$ | 무차원 | CRCL 변화가 CL에 미치는 탄성도 | 신청소율 기여도, 모델 구조 |
| $GFR_i$ / $CRCL_i$ | mL·min⁻¹ 등 | 신기능 지표 | 연령, 체중, 혈청 Cr, 신질환 |
| $\eta_i$ | 무차원 | 공변량으로 설명되지 않은 남은 IIV | 못 잡은 생리학, 유전형, adherence, 모델 오차 |
| $f_u$ | 무차원 | 비결합 분율 | 단백 결합, albumin, 질병 상태, 측정 변이 |

> 💡 **공변량을 직관적으로** — 방 안의 소음을 그냥 줄이는 게 아니라, "이건 냉장고 소리, 이건 창밖 자동차 소리, 이건 옆방 목소리"라고 **이름을 붙이는 일**이에요. 이름이 붙은 순간 그 소음은 $\eta$에서 $\theta$ 구조로 자리를 옮깁니다. 그래서 $(CRCL_i/90)^{\theta_2}$는 단일 숫자가 아니라 **기준 신기능 대비 배율**이고, 식 표기에서도 underbrace보다 overbrace가 의미를 더 정확히 잡아 줍니다.

⚠️ **헷갈림 방지.** $\Delta OFV$는 통계 필터일 뿐, 생리학적 타당성의 증명서가 아니에요. 잔차 모델·VPC·phenotype cell·a priori physiology가 함께 맞아야 합니다.

🔑 **좌표 규칙.** $f_u$가 결정론적 재모수화면 total ↔ unbound 좌표 변환으로 처리, population covariate로 쓸 거면 $\eta$와 $f_u$ 측정 변이를 분리해야 해요.

#### B. PK50 앵커 — $f_u$는 "$\omega^2$ 줄이기"가 아니라 좌표를 바꾸는 일

여기서 놓치기 쉬운 전환이 있어요. **"공변량 모델"과 "재모수화"의 구분**입니다. 둘 다 변이 해석을 바꾸는데, 하나는 예측변수를 모델에 **새로 추가**하는 것이고, 다른 하나는 같은 자료를 **다른 좌표에서 다시 쓰는 것**이에요.

G&W PK50 — 12명 환자가 CpD 566 µg을 5시간 IV infusion으로 받았고, 총 농도와 비결합 농도를 같이 분석했습니다. 혈장 단백 결합 데이터 $f_u$를 써서 total disposition parameter로부터 unbound parameter를 도출했어요. `[G&W p.704–707]`

| 파라미터 | Total estimate (CV%) | Unbound estimate (CV%) |
|---|---:|---:|
| CL | 11.4 L·h⁻¹ (28%) | 720 L·h⁻¹ (9%) |
| Cld | 4.35 L·h⁻¹ (39%) | 265 L·h⁻¹ (33%) |
| Vc | 19.9 L (29%) | 1270 L (18%) |
| Vt | 30.9 L (35%) | 2030 L (51%) |

`[G&W p.708, Table 50.1]`

> 💡 **Total과 unbound를 보는 법** — 같은 도시를 보는 두 장의 지도예요. 지도 축(좌표)을 바꾸면 거리가 다르게 보이지만, 그 자체가 도로를 새로 만든 건 아닙니다. 우리가 어디서 보느냐만 달라진 거예요.

**원전 그대로의 해석.** PK50이 보여주는 것은 total CL이 CV 28%, unbound $CL_u$가 CV 9%라는 사실입니다. **이것은 NONMEM 공변량 모델이 $\omega^2$(CL)을 28%에서 9%로 "깎았다"는 뜻이 아닙니다.** 같은 12명을 total 좌표로 봤을 때랑 unbound 좌표로 봤을 때 변이의 크기가 다르게 보인다는 뜻이에요. $f_u = 0.016 \pm 0.0049$였으니까 단백 결합 변이가 total concentration/parameter variability의 일부를 설명하고 있는 거고요. `[G&W p.708–709]`

> 💼 **실무 인사이트.** $f_u$를 결정론적 재모수화로 쓸 거면 $CL = f_u \cdot CL_u$의 좌표 변환으로 처리하세요. 반대로 집단 공변량 모델로 쓸 거면 $CL_u$에 남길 $\eta$와 $f_u$ 자체의 측정 변이를 따로 분리해야 합니다. 둘을 섞으면 ETA가 생리학을 흡수하는 게 아니라 **회계 오차를 흡수**합니다.

$$
\underbrace{CL}_{\text{total CL}}
=
\underbrace{f_u}_{\text{비결합분율}}
\cdot
\underbrace{CL_u}_{\text{unbound CL}}
$$

> 📊 **개념 도식 (HTML에서 렌더링).** PK50의 $f_u$는 NONMEM 공변량 모델의 $\omega^2$ 감소가 아니라, total coordinate를 unbound coordinate로 다시 표현하는 재모수화입니다. 이 변환을 거친 뒤에도 반응(PD) 변이는 별도 source로 남아 있어요.

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

#### C. PK 변이와 PD 변이는 따로

PK50에는 한 가지 결정적인 메시지가 더 있어요 — **단백 결합이 모든 변이를 설명하지는 않는다**는 점입니다. CpD에서 비슷한 노출을 받은 환자들 사이에서도 반응이 8배(0.5–4.0 response units)까지 갈렸어요. 비결합 농도로 다시 표현해도 EC50 변이는 오히려 더 커졌습니다. 저자들은 $E_{max} < 1$인 무반응자가 **유전적 구성/수용체 밀도**와 관련된다고 해석했어요. `[G&W p.707–709]`

$$
\underbrace{E_{max}}_{\text{최대 반응능}}
<
\underbrace{1}_{\text{완전반응 기준}}
$$

R&T도 같은 말을 합니다 — 혈장 농도와 반응을 같이 측정해야 PK 변이와 PD 변이를 구분할 수 있다. `[R&T p.363–364]` 그래서 공변량이 PK 파라미터 변이를 설명했다고 해서 반응 변이까지 설명한다고 보면 안 돼요.

#### D. 구조적 필요성 및 한계

| 단계 | 근거/가정 | 수식 또는 판단 |
|---|---|---|
| 1 | 공변량은 $\eta$를 없애는 변수가 아니라 설명 가능한 구성요소를 $\theta$ 구조로 옮기는 변수 | $CL_i=\theta_1\cdot(CRCL_i/90)^{\theta_2}\cdot\exp(\eta_i)$ |
| 2 | 공변량 도입 전 G&W식 EDA 선행 | individual profile, pooled data, dose normalization, transformation `[G&W p.334–336]` |
| 3 | 식별가능성이 없으면 이름만 생리학적일 뿐 noise source가 됨 | identifiability/estimability 점검 `[G&W p.348–351]` |
| 4 | 분산 전파식은 **로그 스케일에서 $f_u$와 $CL_u$가 독립일 때만 성립하는 일차 근사**임 | $CV(CL)^2 \approx CV(f_u)^2 + CV(CL_u)^2$는 본 문서에서 채택하지 않음 — 사유는 산술적 오류가 아니라 **임상 데이터에서 $f_u$와 $CL_u$가 종종 상관** (예: 알부민 변동이 $CL_u$에도 영향)되어 독립성 가정이 비현실적이기 때문 |
| 5 | total concentration safety threshold와 unbound concentration individualization은 서로 다른 좌표 | total C $>50$ µg·L⁻¹ 회피와 unbound 기반 안전 여유 구분 `[G&W p.705, p.709]` |

#### E. Stepwise Covariate Model(SCM) 정량 임계 — forward·backward 비대칭 `[교과서 외 구현/규제 표준; 1차 문헌: Jonsson EN, Karlsson MO. Automated covariate model building within NONMEM. *Pharm Res.* 1998;15(9):1463–1468 + 후속 표준화: Jonsson EN, Karlsson MO. Stat Med 1998;17(15):1745–1757]`

§M의 "$\Delta OFV > 3.84$만으로 채택 위험" 경고를 정량 절차로 풀 자리예요. SCM은 forward와 backward의 **비대칭 임계**가 핵심입니다 — R&T p.373이 명시한 $\Delta OFV \geq 3.84$ (df=1, α=0.05) 한 줄을 그대로 모델 선택의 끝으로 쓰는 게 아니라, **두 단계의 다른 α를 통과해야** 한 covariate가 최종 모델에 남습니다.

$$
\overbrace{\text{Forward Selection}}^{\text{후보 추가 단계}}:\quad
\underbrace{\Delta OFV}_{\text{OFV 감소}}
\geq
\underbrace{3.84}_{\chi^2_{df=1,\,\alpha=0.05}}
$$

$$
\overbrace{\text{Backward Elimination}}^{\text{최종 정리 단계}}:\quad
\underbrace{\Delta OFV}_{\text{OFV 증가}}
\geq
\underbrace{6.63}_{\chi^2_{df=1,\,\alpha=0.01}}
$$

| 단계 | 방향 | α (df=1) | 임계 ΔOFV | 목적 |
|---|---|---|---|---|
| **Forward Selection** | covariate 추가 | 0.05 | **3.84** `[R&T p.373]` | 관대한 기준으로 후보 covariate 포함 |
| **Backward Elimination** | covariate 제거 | 0.01 | **6.63** | 엄격한 기준으로 multiple testing 보정 |

**왜 비대칭인가.** Forward 단계의 multiple testing이 false positive 위험을 만들어요 — covariate 후보 10개를 α=0.05로 각각 검정하면 family-wise error가 약 40%까지 누적됩니다. Backward 단계에서 더 엄격한 α=0.01를 통과해야 살아남도록 설계해서 이 누적 위험을 보정해요. 이 비대칭이 Jonsson-Karlsson SCM의 핵심 설계 원리입니다. `[교과서 외 구현; 개념 근거: R&T p.373 (3.84 임계만 명시)]`

$$
\underbrace{P_{\text{FWE},\,\text{Forward}}}_{\text{누적 false positive 위험}}
\approx
\overbrace{1-(1-\alpha)^k}^{\text{k개 후보의 가족별 오류}}
\xrightarrow[\alpha=0.05,\,k=10]{}
\underbrace{0.40}_{\text{약 40\%}}
$$

> 💼 **규제 보고서 표준 문구.** *"Covariate selection followed a stepwise approach (Jonsson & Karlsson, 1998): forward inclusion at $\Delta OFV \geq 3.84$ (df=1, α=0.05) and backward elimination at $\Delta OFV \geq 6.63$ (df=1, α=0.01). Final model retention required both forward inclusion and backward retention thresholds, supplemented by VPC consistency and a priori physiological plausibility (see §M)."*

⚠️ **흔한 함정.** Forward만 돌리고 backward를 생략하면 PopPK 보고서에서 reviewer가 거의 반드시 deficiency를 발견합니다 — multiple testing 보정 없이 통계적 유의성을 주장한 결과예요. **SCM은 양방향이 한 묶음**이며, forward-only 결과를 "SCM"으로 보고하면 안 됩니다.

🔑 **§M과의 연결.** §M이 "$\Delta OFV$ 단독 판단의 위험"을 정성적으로 경고했다면, 이 §E는 그 정량 절차예요. 두 카드는 함께 읽어야 합니다 — §E의 비대칭 임계로 **통계적** false positive를 보정하고, §M의 VPC·cell size·a priori physiology로 **mechanistic** false positive를 보정합니다. 둘 중 하나만 통과한 covariate는 최종 모델에 들어가면 안 돼요.

#### F. 범주형 공변량의 다층 처리 — multi-level categorical covariate `[교과서 외 구현/규제 표준; 개념 근거: R&T p.369 (age, weight, sex, race를 covariate 후보로 명시)]`

§A의 CRCL은 연속형, C4의 CYP2D6 PM은 이항 범주형이었어요. 그런데 실무 PopPK 자료에서는 **다층 범주형 공변량** — sex (2-level) × race (3-level) × genotype (4-level) 같은 3-way categorical structure — 가 더 흔합니다. R&T가 p.369에서 명시적으로 열거한 covariate 후보(age, weight, sex, race, disease)에서 sex·race가 모두 범주형이에요. NONMEM에서 이를 다루는 세 가지 처리 방식이 있고, **어느 방식을 쓰느냐가 covariate selection 결정의 출발점**이에요.

| 처리 방식 | NONMEM 구현 | 장점 | 단점 |
|---|---|---|---|
| **Multiple THETA (full stratification)** | level마다 독립 THETA: `IF (RACE.EQ.1) F1=θ_1; IF (RACE.EQ.2) F1=θ_2; ...` | level 효과를 독립 추정, 해석 명확 | level 수 증가 시 파라미터 폭발, 작은 cell 식별 실패 |
| **Indicator variable (dummy coding)** | reference + binary dummy: `F1 = 1 + θ_1·(RACE.EQ.2) + θ_2·(RACE.EQ.3)` | reference level 명시, 비교 용이 | reference 선택이 임상적 해석에 영향 |
| **Hierarchical structure** | shared variance 또는 mixture: `$MIX` 또는 partial pooling prior | 작은 cell에서도 정보 공유로 안정 | 모델 식별성·prior 가정 필요 |

```nmtran
; [교과서 외 구현 번역; multiple THETA 방식 — sex × CYP2D6 phenotype 2-way 예시]
IF (SEX.EQ.1.AND.PHEN.EQ.1) CLF = THETA(1)                       ; Male EM (reference)
IF (SEX.EQ.1.AND.PHEN.EQ.2) CLF = THETA(1) * THETA(2)            ; Male IM/PM (phenotype 배율)
IF (SEX.EQ.2.AND.PHEN.EQ.1) CLF = THETA(1) * THETA(3)            ; Female EM (성별 배율)
IF (SEX.EQ.2.AND.PHEN.EQ.2) CLF = THETA(1) * THETA(2) * THETA(3) ; Female IM/PM (곱셈 가정)
CL = CLF * EXP(ETA(1))
```

$$
\underbrace{CL_i}_{\text{개인 CL}}
=
\underbrace{\theta_1}_{\text{Male EM 기준}}
\cdot
\overbrace{\theta_2^{\,I(\text{PHEN}_i\,\in\,\text{IM/PM})}}^{\text{phenotype 배율}}
\cdot
\overbrace{\theta_3^{\,I(\text{SEX}_i\,=\,\text{Female})}}^{\text{성별 배율}}
\cdot
\underbrace{\exp(\eta_i)}_{\text{남은 IIV}}
$$

⚠️ **곱셈 가정 vs 상호작용.** 위 식은 **곱셈 가정** (interaction-free main effect 모델) 입니다. 실제로는 sex × phenotype 상호작용이 존재할 수 있어요 — 예를 들어 여성 CYP2D6 PM의 CL 감소 폭이 남성 PM보다 클 수 있습니다. Full stratification으로 4 cell 각각의 THETA를 추정하면 interaction을 잡을 수 있지만 파라미터가 4개로 폭발하고, 작은 cell에서 식별 실패가 일어나요 (진단 시그니처 2 `Empty Phenotype Cell`). **Cell n이 작으면 곱셈 가정 + main effect만 권장**합니다.

> 💼 **실무 결정 트리 — multi-level categorical 어떻게 시작하나.**
>
> 1. **모든 level cell n ≥ 30** → multiple THETA full stratification으로 시작, interaction 평가 가능
> 2. **일부 cell n ∈ [5, 30)** → indicator + 곱셈 가정 (main effect만), interaction은 다음 iteration
> 3. **일부 cell n < 5** → hierarchical 또는 인접 level 통합 (예: IM/PM 묶음), 단일 binary indicator로 축소
>
> 진단 시그니처 2 `Empty Phenotype Cell` (C4 §D) 이 다층 범주형에서 가장 자주 작동해요. Full stratification으로 시작했다가 RSE 폭발(>80%)을 보고서야 통합으로 후퇴하는 게 흔한 실수입니다 — **시작할 때 cell size를 먼저 보세요.** "효과 없음"과 "정보 부족"의 구분이 C4와 정확히 같은 논리예요.

🔑 **§E 비대칭 임계의 자동 보정.** Multi-level categorical에서 SCM을 돌릴 때, level 수가 K개면 forward에서 추가되는 ΔOFV의 자유도(df)는 (K-1)이에요. df=1이 아닙니다.

$$
\underbrace{\mathrm{df}}_{\text{자유도}}
=
\underbrace{K}_{\text{level 수}}
-
\underbrace{1}_{\text{reference level}}
$$

3-level race를 추가하면 df=2이고, 임계는 $\chi^2_{df=2,\alpha=0.05} = 5.99$ (forward), $\chi^2_{df=2,\alpha=0.01} = 9.21$ (backward)로 자동 보정됩니다. df=1만 외워서 모든 covariate에 3.84/6.63을 적용하면 multi-level에서 통계적으로 잘못된 결정을 합니다 — reviewer가 가장 자주 잡아내는 지점 중 하나예요.

| level 수 K | df | Forward 임계 ($\alpha=0.05$) | Backward 임계 ($\alpha=0.01$) |
|---:|---:|---:|---:|
| 2 (binary) | 1 | 3.84 | 6.63 |
| 3 | 2 | **5.99** | **9.21** |
| 4 | 3 | **7.81** | **11.34** |

```yaml
aliases: [covariate model, creatinine clearance, protein binding, fu, reparameterization, SCM, stepwise covariate model, categorical covariate]
tags: [pharmacometrics/covariate, pk/protein-binding, nonmem/eta, nonmem/scm]
source: "R&T p.369-371, p.373; G&W PK50 p.704-710"
```

#### M. 흔한 오해 — "$\Delta OFV > 3.84$면 공변량 채택"

이 한 줄이 모델 선택을 끝내는 것처럼 보여요. $\Delta OFV > 3.84$(df=1, α=0.05)는 내포 모델 LRT의 통계적 필터니까, 숫자 하나로 결정이 나는 것처럼 깔끔하잖아요. 그런데 실무에서는 이게 가장 흔한 함정 중 하나예요.

$$
\underbrace{\Delta OFV}_{\text{OFV 변화}}
>
\underbrace{3.84}_{\text{LRT 기준}}
$$

이걸 그대로 두면 어떻게 되냐. **잔차 모델이 불안정하거나 phenotype cell이 작으면 → 공변량이 $\varepsilon$ 변동이나 ETA 흡수를 대신 설명하면서 OFV는 떨어지는데 VPC는 오히려 악화**돼요. 이걸 `OFV-VPC Discordance`라고 부릅니다. 임상에서는 covariate 극단값에서 노출 예측이 빗나가거나 고위험군 용량이 잘못 잡히고, 규제에서는 "$\Delta OFV$만으로 채택"한 covariate에 대해 FDA Deficiency Letter가 날아오면서 VPC와 sensitivity analysis 재분석을 요구받습니다.

왜 틀렸는지를 세 경로로 정리하면. (1) 잔차 오차 구조 오지정 시 공변량이 $\varepsilon$ 변동을 흡수해서 $\Delta OFV$가 잘못 계산됩니다 — **진단 시그니처 1 Leakage Funnel이 시간 축으로 펼쳐진 형태**예요. (2) Phenotype cell 크기가 작으면 (→ 진단 시그니처 2) 범주형 공변량의 $\Delta OFV$가 작은 셀의 ETA 흡수로부터 인공적으로 생깁니다. (3) 진짜 mechanistic covariate가 빠지면 상관 공변량(체중, BSA가 CrCl을 대신함)이 가짜로 OFV 개선을 만들어요 — **진단 시그니처 3 Vanishing Covariate Cascade의 거울상**이죠.

**임상·NONMEM 시그니처.** 체중을 CL에 추가했더니 OFV가 12 감소했는데, **VPC를 그려보니 예측 구간이 오히려 넓어진다** — 공변량을 넣었는데 분포 수준 적합도가 악화되는 경우입니다. 이 신호가 보이면 세 가지를 자문하세요. 잔차 모델이 안정화되었는가? Phenotype cell의 n이 충분한가? A priori 후보 공변량이 base에 포함되어 있는가? 셋 다 YES이기 전에는 $\Delta OFV$는 그저 한 줄 숫자일 뿐입니다.

**규제 방어 문구:** *"Covariate selection was guided by $\Delta OFV$ combined with VPC consistency at covariate extremes and a priori physiological plausibility; $\Delta OFV$ alone was not used as the acceptance criterion. SCM thresholds followed §E (forward α=0.05, backward α=0.01)."*

> 🔬 **진단 시그니처 3 — `Vanishing Covariate Cascade`**
> **어떤 모습인가:** 진짜 mechanistic covariate(예: 신청소율의 CrCl)가 모델에서 빠져 있으면 $\eta_{CL}$이 그걸 흡수해 버려요. 그 뒤에 돌린 stepwise selection에서는 상관 covariate(체중, BSA)가 가짜로 detect됩니다. 시각적으로는 $\eta_{EBE}$ vs CrCl scatter가 평탄해 보여서 "CrCl 효과 없음"으로 잘못 읽히는데, **raw observation 좌표의 $Cl_{obs}$ vs CrCl을 그리면 명확한 기울기가 나옵니다**.
> **왜 일어나나:** Stepwise는 $\eta$에 남은 잔여 신호로 covariate를 평가하니까, $\eta$가 이미 covariate를 흡수해 버린 다음에는 그 covariate가 통계적으로 사라져 보여요. "covariate는 $\eta$ 안의 설명 가능한 부분을 $\theta$로 옮기는 변수"라는 C3 정의가 시간 순서를 잘못 지키면 정반대로 작동합니다.
> **꿀팁:** $\eta$에 의존한 covariate scan 한 번, raw observation에 직접 적용한 scan 한 번 — 두 결과가 일치하지 않으면 "효과 없음"이 아니라 **"효과 흡수됨"**을 의심하세요.
> **실무 활용:** Domain knowledge 기반 candidate covariate(CL을 결정하는 생리학적 변수: CrCl, body size, hepatic function)를 a priori 정의해서 모델 base에 포함시킨 뒤 stepwise를 시작합니다. Stepwise에 모든 판단을 위임하지 마세요.

**이번 카드 핵심내용**
- 신기능이 CL 변이를 설명할 때 → CRCL/GFR 공변량이 $\theta$ 구조를 결정
- Total CL CV 28% vs unbound $CL_u$ CV 9%를 볼 때 → $f_u$ 재모수화와 좌표 변환의 문제
- 비슷한 노출에서도 반응이 8배 다를 때 → PD variability는 별도의 영역
- OFV만으로 공변량을 채택할 때 → VPC·cell size·physiology 방어가 없으면 규제 재분석 위험
- SCM을 forward만 돌리고 backward를 생략할 때 → multiple testing 보정 결손으로 regulator deficiency
- Multi-level categorical에 df=1 임계를 그대로 쓸 때 → df=(K-1) 자동 보정 미적용으로 통계 오류
- 공변량을 "$\omega^2$ reduction"으로만 해석하는 순간 → 좌표 혼동 → dose rationale 불일치

---

<!-- SLIDE_START: C4 | title: 유전적 다형성 — IIV의 불연속 하위구조(substructure) -->
<!-- SECTION_CORE: SC-06 -->

### C4. 유전적 다형성 — IIV의 불연속 하위구조(substructure)

C3에서 설명 가능한 생리학을 $\theta$ 구조로 옮겼다고 합시다. 그럼 이제 남은 $\eta$가 진짜 매끄러운 하나의 분포인지, 아니면 유전형/표현형 하위군의 혼합인지를 확인해야 해요.

> **거장의 시각**
> $\eta$ 히스토그램이 매끈한 로그정규처럼 보인다고 해서 "유전 하위구조 없음"으로 결론 내리면 안 됩니다. 작은 phenotype cell과 shrinkage가 만든 false negative를 그대로 놓치게 돼요. **분포 모양과 cell 크기를 같이 봐야 "효과 없음"과 "효과를 볼 정보가 없음"을 구분**할 수 있습니다.

#### A. 형식적 정의

C1부터 C3까지는 $\eta$를 대체로 매끄러운 로그정규 분포로 다뤘어요. 그런데 약리유전학은 다른 그림을 보여 줍니다 — $\eta$가 실제로는 하나의 매끄러운 분포가 아닐 수 있어요. PM/IM/EM/UM(저대사/중간/광범위/초고속 대사자)이나 반응자/무반응자처럼 불연속적으로 갈라지는 여러 하위집단의 혼합일 수 있습니다. `[R&T p.393–410]`

R&T는 유전 다형성을 모집단 안에서 유전 표현형이 다봉형 분포(polymodal distribution; 봉우리가 여러 개인 분포)를 만드는 현상으로 다룹니다. 핵심은 유전 형질이 다른 변이의 원인과 다르게 **평생 지속되는 개인 특성**이라는 점이에요. `[R&T p.393]`

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

| 파라미터 | 단위 | 무엇을 뜻하나 | 무엇 때문에 변하나 |
|---|---|---|---|
| $p$, $q$ | 무차원 빈도 | 대립유전자 빈도 | 집단 유전 구조, ancestry, selection |
| $p^2$, $2pq$, $q^2$ | 무차원 빈도 | genotype class 빈도 | Hardy-Weinberg 가정, allele frequency |
| $\theta_2$ 또는 phenotype factor | 무차원 배율 | 특정 phenotype의 CL 변화 | 유전형 기능, 효소 활성, cell size |
| $\eta_i$ | 무차원 | phenotype으로 설명되지 않은 남은 개인차 | 못 잡은 유전형, 병태, residual artifact |

> 💡 **단봉 vs 다봉** — 단봉형 $\eta$는 하나의 언덕 경사처럼 보이고, 다봉형 $\eta$는 봉우리가 여러 개인 산맥처럼 보여요. 다봉형에서는 **평균이 계곡 한가운데에 떨어져서, 실제 환자 누구도 대표하지 못하는 값**이 됩니다.

R&T는 느린 acetylator가 열성 동형접합체일 때, 대립유전자 빈도로 이형접합/동형접합 빠른 acetylator 빈도를 계산하는 방식을 설명해 줍니다. `[R&T p.402]`

⚠️ **헷갈림 방지.** 인종(ethnicity)은 유전형(genotype)의 **불완전한 proxy**예요. 그룹 내 변이가 크기 때문에 ethnicity term을 mechanistic genotype처럼 해석하면 안 됩니다. `[R&T p.395, p.409]`

🔑 **Cell size 규칙.** 작은 phenotype cell에서는 "효과 없음"보다 **"식별할 정보 없음"**을 먼저 의심하세요.

#### B. 출처 고정 유전 예시

| 예시 | 출처 고정 사실 | 모델링 함의 |
|---|---|---|
| Nortriptyline 쌍둥이 | 일란성 쌍둥이의 쌍 내 변이가 이란성 쌍둥이보다 작아 유전이 PK 변이에 크게 기여 `[R&T p.394]` | "설명되지 않은 $\eta$" 안에 유전 성분이 있을 수 있음 |
| CYP2D6 / nortriptyline | 기능적 CYP2D6 유전자 사본 수가 많을수록 청소율이 커지고 노출이 낮아짐 `[R&T p.397]` | $\eta$(CL)이 매끄럽지 않고 유전자 사본 범주로 갈라질 수 있음 |
| CYP2C9 / warfarin | CYP2C9 변이가 S-warfarin 대사와 용량 변이에 기여 `[R&T p.398, p.406]` | PK 유전형(CYP2C9)과 PD 유전형(VKORC1)을 동시에 고려 |
| Codeine | CYP2D6-매개 모르핀 형성이 minor pathway이지만 활성 대사체가 강력해서 임상적으로 중요 `[R&T p.399, p.404]` | 모약물 청소율만 보면 독성/활성 대사체 위험을 놓침 |
| TPMT / thiopurines | TPMT 다형성이 thiopurine 용량과 독성에 크게 영향 `[R&T p.400]` | Poor metabolizer 하위군은 평균 용량으로 다룰 수 없음 |
| NAT2 / isoniazid | 483명에서 6시간째 isoniazid 농도의 이봉형 분포 `[R&T p.402]` | 이봉형 $\eta$ 분포의 대표 예시 |
| VKORC1 / warfarin | CYP2C9, VKORC1, 연령/체중 등이 warfarin 용량 분산을 나눠 설명 `[R&T p.406]` | 단일 공변량 결정론 금지 |

여기서 약 몇 개만 입에 붙는 사례로 풀고 갑니다. **Warfarin**(앞서 본 비타민K 길항 항응고제)에서 CYP2C9는 약의 농도/약동학을 결정하고, VKORC1은 같은 농도에서도 환자의 감수성을 결정해요. 그래서 **CYP2C9 변이가 같아도 VKORC1이 다르면 같은 INR을 얻는 용량이 또 갈라집니다** — PharmGKB가 genotype-guided dosing을 권고하는 이유예요. → 그래서 단일 유전자 하나로 용량을 결정할 수 없다는 사실의 임상 예입니다. **Codeine**(opioid prodrug)은 CYP2D6에 의해 morphine으로 변환되는데, CYP2D6 UM(초고속 대사자)에서는 모르핀이 과량 생성돼서 호흡 억제 위험이 커집니다. → 그래서 모약물 청소율만 봐서는 안 되고, 활성 대사체의 좌표를 같이 봐야 한다는 사실의 임상 예고요. **Thiopurines**(6-MP, azathioprine; 백혈병·IBD 치료제)는 TPMT 결핍자에서 골수 독성이 치명적이어서, 표준 용량을 그대로 주면 사망 위험이 있어요. → 그래서 평균 용량으로 다룰 수 없는 하위군의 대표 예입니다.

> 💡 **PM 빈도표 읽는 법** — 평균 용량을 결정하기 위한 표가 아니에요. **어느 phenotype cell이 작아서 모델 식별성이 흔들릴 수 있는지를 미리 알려 주는 표**입니다.

Table 13-1의 poor metabolizer 빈도(출처 값 보존): CYP2D6 PM은 백인 5–10%, 아프리카계 미국인 3.8%, 아시아인 0.9%; CYP2C9 PM은 백인 1%; CYP2C19 PM은 백인 3–5%, 아시아인 16%; TPMT 결핍은 백인 0.3%, 아시아인 0.04%; NAT2 느린 acetylator는 백인/아프리카계 미국인 60%, 아시아인 10–20%; UGT1A1 poor metabolizer 상태는 백인 11%, 아시아인 1–3%. `[R&T p.395]`

#### C. Code Structure

```nmtran
; [교과서 외 구현 번역]
IF (CYP2D6PM.EQ.1) THEN                  ; PM indicator가 1이면 PM 효과를 CL에 곱한다
  CL = THETA(1) * THETA(2) * EXP(ETA(1)) ; THETA(2)는 PM phenotype factor, ETA(1)은 남은 IIV
ELSE                                      ; PM이 아니면 기준 CL 구조를 사용
  CL = THETA(1) * EXP(ETA(1))            ; 기준군 CL × 남은 IIV
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

> 💼 **실무 인사이트.** 범주형 공변량은 수준별 표본 크기가 충분치 않으면 THETA factor가 ETA에 흡수돼 버려요. PM이 n=3 같은 빈 셀에서는 "효과 없음"이 아니라 **"효과를 식별할 정보가 없음"** 일 수 있습니다. 다층 범주형 처리의 결정 트리는 C3 §F를 참고하세요.

#### D. 구조적 필요성 및 한계

| 상황 | 파라미터 변화 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| 이봉형 분포를 단일 로그정규 IIV로 적합 | $\omega^2$가 하위군 차이를 흡수 | → | 평균 dose가 subgroup toxicity/inefficacy를 숨김 `[R&T p.366]` | mixture 또는 phenotype 구조 검토 |
| 유전 다형성이 존재 | $\eta$ histogram의 두 봉우리가 생리학으로 번역 | → | PM/IM/EM/UM 용량 차이 가능 | genotype/phenotype cell size 확인 |
| ethnicity를 genotype으로 해석 | proxy effect를 mechanistic effect로 과해석 | → | 집단 내 고위험 개인 누락 | genotype 직접성·within-group variability 명시 `[R&T p.395, p.409]` |
| CYP3A4처럼 큰 변이는 있으나 명확한 유전 인자 없음 | 큰 $\omega^2$가 항상 genotype peak를 뜻하지 않음 | → | 유전형 과잉해석 | 다른 인구학·순응·병태 요인 검토 `[R&T p.399, p.410]` |

- HLA-B*5701 빈도, 최신 FDA 약리유전체 라벨 수, 자세한 PM/IM/EM/UM 빈도표는 이 PDF 범위 밖이므로 다루지 않습니다.
- 약리유전학이 강력하긴 하지만 완결된 설명은 아니에요. R&T는 유전형 외에도 인구학적 특성, 복약 순응 등 다른 요인이 최적 용량 결정에 같이 필요하다고 마무리합니다. `[R&T p.409]`

> 📖 **R&T 5e p.402, Figure 13-6** — 483명에게 9.8 mg/kg isoniazid를 경구 투여하고 6시간째 농도를 그린 분포입니다. C4의 핵심 메시지가 이 그림 한 장에 들어 있어요 — **유전 다형성은 단순 공변량 label이 아니라 분포 모양 자체를 바꾼다**는 것. NAT2 acetylator status가 실제 농도 분포를 두 봉우리로 갈라놓는 장면이 보입니다.

이 카드에서 가장 자주 발생하는 실패는 한 가지예요. **범주형 유전 구조가 실제로 존재하는데 표본의 한 subgroup이 작거나 비어 있으면, 모델은 그 효과를 독립된 phenotype 효과로 못 보고 $\eta$ 안에 흡수해 버립니다.** 그래서 C4에서 가장 먼저 보는 건 genotype label 자체가 아니라 **$\eta$ 분포와 농도 분포의 모양이 단봉인지 다봉인지**예요.

> 🔬 **진단 시그니처 2 — `Empty Phenotype Cell`**
> **어떤 모습인가:** Phenotype을 4-level full stratification(PM/IM/EM/UM)으로 처음부터 펼쳤는데, 작은 n cell(특히 PM=3 같은 희귀 셀)의 THETA factor RSE가 80%를 넘고 `$COV step`이 "covariance matrix is non-positive definite"로 실패합니다. PM 환자 5명의 ETA(1)이 다 0 근처에 모여 있는 모습은 "효과 없음"이 아니라 **"효과 흡수됨"** 의 가장 흔한 false negative 시그니처예요.
> **왜 일어나나:** Cell이 비어 있으면 모델은 그 phenotype 효과를 추정할 정보가 없으니까 ETA로 흡수하고, $\omega^2$이 인공적으로 부풀어요. 변이 보존 법칙이 다시 작동하는 장면입니다.
> **꿀팁:** PM(n=3) 결과를 받았을 때 자문해야 할 질문은 "효과가 있는가?"가 아니라 **"효과를 식별할 정보가 데이터에 있는가?"** 예요. 둘은 다른 질문입니다.
> **실무 활용:** Phenotype level은 데이터 크기에 비례해서 통합하세요. 인접 phenotype을 합쳐 "reduced function" 같은 단일 카테고리로 시작하거나, informative prior로 작은 cell을 안정화합니다. 4-level full stratification은 데이터가 명확히 허용할 때만 펼치고요. 작은 cell의 categorical effect를 보고서에 "null result"로 기재하면 안 됩니다. C3 §F의 결정 트리 참조.

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

**이번 카드 핵심내용**
- $\eta$ 분포가 두 봉우리로 보일 때 → genotype/phenotype subgroup의 영역
- Phenotype cell의 n이 작거나 비어 있을 때 → 식별가능성과 ETA 흡수가 결정
- Ethnicity 공변량이 유의해 보일 때 → proxy와 mechanistic genotype을 분리해서 봐야 함
- "효과 없음"과 "정보 부족"을 혼동하는 순간 → PM subgroup 위험 누락 → 평균 dose가 subgroup toxicity/inefficacy를 숨김

---

<!-- SLIDE_START: §5 | title: 혼동쌍 해부(Confusion Pair Dissection) -->
<!-- SECTION_CORE: SC-07 -->

## §5 — 혼동쌍 해부(Confusion Pair Dissection)

오늘 세션 전체에서 헷갈리기 쉬운 네 쌍을 한 번씩 짚고 갑니다. 보면 다 같은 질문으로 환원돼요 — "**지금 보고 있는 변이가 어느 좌표에 있느냐**".

### Pair 1. $\omega^2$(IIV) vs $\sigma^2$(RUV)

| 비교 기준 | $\omega^2$ / $\eta$ | $\sigma^2$ / $\varepsilon$ |
|---|---|---|
| 단위 / 차원 | random effect 분산; `$OMEGA`; 개인 파라미터 수준 | residual variance; `$SIGMA`; 관측값 수준 |
| 수식 내 위치 | $CL_i=CL\cdot\exp(\eta_i)$의 지수 배율 또는 individual parameter 구조 | $Y=F+\varepsilon$, $Y=F(1+\varepsilon)$, $Y=F\exp(\varepsilon)$의 관측 잔차 |
| 변화 원인 | 개인별 CL·V 차이, 생리학, 유전형, 병태, 미포착 공변량 | assay 오차, sampling 오차, residual model misspecification |
| 혼동 시 임상 결과 | 측정 오차를 IIV로 해석해 가짜 covariate 탐색 | 진짜 IIV를 잔차 noise로 묻어 dose individualization 실패 |

**결정적 차이.** $\omega^2$와 $\sigma^2$는 같은 "전체 미설명 변이"를 두고 경쟁합니다. 잔차 모델을 틀리면 공변량이 단순히 보이거나 사라지는 게 아니라 **변이가 잘못된 그릇으로 이동**해요.

> ⚡ **Pair 1 한 번 더 — 개인 고유의 차이 vs 측정·모델의 노이즈.**
> $\omega^2$(`$OMEGA`)는 같은 약, 같은 용량에서도 사람마다 CL·V가 다른 **생물학적 개체간 차이** — 실제로 존재하는 차이예요. $\sigma^2$(`$SIGMA`)는 한 사람 안에서 예측값과 관측값이 안 맞는 **측정·모델·시점 내 노이즈** — 설명 실패고요.
> 그래서 처치도 달라요. $\omega^2$를 줄이려면 IIV 원인을 찾아야 하고(covariate 추가), $\sigma^2$를 줄이려면 모델 구조나 측정 오차 모델을 손봐야 합니다(residual model 재선택, assay 재검증). 둘을 혼동하면 covariate를 아무리 늘려도 $\sigma^2$ 문제는 그대로고, error model을 바꿔도 IIV는 그대로 남아요.

### Pair 2. Total CL vs Unbound $CL_u$ — PK50 앵커 기반

| 비교 기준 | Total CL | Unbound $CL_u$ |
|---|---|---|
| 단위 / 차원 | CL 11.4 L·h⁻¹, CV 28% `[G&W p.708]` | $CL_u$ 720 L·h⁻¹, CV 9% `[G&W p.708]` |
| 수식 내 위치 | $CL=f_u\cdot CL_u$의 total 좌표 결과 | $CL_u=CL/f_u$로 해석되는 unbound 좌표 결과 |
| 변화 원인 | 단백 결합 변이가 total concentration/parameter variability에 섞임 | $f_u$로 재표현된 disposition; 유리 약물 기준 제거 능력 |
| 혼동 시 임상 결과 | total C $>50$ µg·L⁻¹ 회피 기준과 unbound 기반 안전 여유가 불일치 | 저알부민혈증에서 total 정상이어도 unbound 독성 위험 놓침 `[G&W p.705, p.709]` |

**핵심 한 방.** PK50은 "$f_u$ covariate가 $\omega^2$을 줄였다"가 아니라, **같은 12명을 total과 unbound 좌표로 비교했을 때 변이 해석이 달라진다는 사실**을 보여 줍니다. 용량/안전성 판단에서 total C $>50$ µg·L⁻¹ 회피 기준과 unbound 기반 안전 여유가 혼동되면 노출-반응 해석의 좌표가 어긋나요. `[G&W p.705, p.709]`

> ⚡ **Pair 2 한 번 더 — 전체 통행량 vs 무료 차선 통행량.**
> Total CL은 bound + unbound 약물 모두 기준으로 한 **전체 제거 능력**, Unbound $CL_u = CL/f_u$는 유리 약물만 기준으로 한 **실제 작용 약물의 제거 능력**입니다. 저알부민혈증 환자에서 $f_u$가 올라가면 total CL이 안 변해도 unbound 좌표는 다르게 보여요.
> PK50에서 본 것처럼, total 좌표에서 "IIV가 크다"(CV 28%)는 신호가 unbound 좌표로 옮기면 **다른 숫자(CV 9%)** 가 됩니다 — $\omega^2$이 줄어든 게 아니라 **좌표축이 회전한 것**이에요. 좌표를 잘못 고르면 covariate 탐색의 방향이 반대로 갑니다.

> 🔴 **Pair 2에서 가장 큰 위험**
> 이 혼동을 안고 NDA dose individualization 섹션을 강행하면, total 좌표에서 나온 $\omega^2$을 마치 covariate 모델이 reduction을 만든 것처럼 보고하게 돼요. 규제 reviewer는 (a) total/unbound coordinate split이 명시되지 않았거나, (b) safety threshold(total)와 dose recommendation(unbound 기반)이 좌표 면에서 일치하지 않는 점을 deficiency로 지적합니다. 임상적으로는 저알부민혈증 환자에서 total 농도가 정상으로 보이는데 unbound이 높아 독성이 나는 시나리오를 보호하지 못해요. `[G&W p.705, p.709]`

### Pair 3. PK 변이 vs PD 변이

| 비교 기준 | PK 변이 | PD 변이 |
|---|---|---|
| 단위 / 차원 | 농도-시간 프로파일, CL·V·F 등 PK 파라미터 | 반응(response), EC50·Emax·γ 등 PD 파라미터 |
| 수식 내 위치 | concentration-time model의 structural/random effect 위치 | exposure-response model의 response parameter 위치 |
| 변화 원인 | 흡수·분포·대사·배설, 단백결합, renal/hepatic function | receptor density, genetic makeup, target expression |
| 혼동 시 임상 결과 | 혈중농도만 맞추면 반응도 맞는다고 오판 | 비슷한 노출에서도 8배 반응 차이를 설명 못함 `[G&W p.707–709]` |

PK 변이는 **농도-시간 프로파일이 왜 다른가**를 묻고, PD 변이는 **같은 노출에서 반응이 왜 다른가**를 묻습니다. R&T는 혈장 농도 측정이 PK와 PD 변이를 분리하는 전제 조건이라고 못 박아요. `[R&T p.363–364]` PK50에서 단백 결합은 총 농도 변이의 일부를 설명했지만, 반응은 비슷한 노출에서도 8배 차이가 났어요 — 단일 공변량이 모든 변이를 설명한다는 생각이 왜 위험한지를 보여주는 핵심 예입니다. `[G&W p.707–709]`

> ⚡ **Pair 3 한 번 더 — 약이 어떻게 움직이는가 vs 어떻게 반응하는가.**
> PK IIV는 개인별 CL·V·F의 차이 — 같은 용량에서 **농도가 얼마나 다른가**. PD variability는 개인별 EC50·Emax·γ의 차이 — 같은 농도에서 **반응이 얼마나 다른가**. 둘은 **수학적으로 독립**이라서 PK IIV가 작아도 PD variability가 크면 농도만 맞춰도 반응 개체화는 어려워요. 개인화 의료에서 TDM이 혈중농도를 맞추는 것(PK 영역)과 반응을 맞추는 것(PD 영역)이 다른 문제인 이유가 여기서 나옵니다. PK50의 "response 8배 차이"는 PK 좌표의 covariate 모델로는 도달할 수 없는 잔여 variability예요.

### Pair 4. 평균 분포(mean distribution) vs 분포 모양(shape distribution)

| 비교 기준 | 평균 분포(mean/CV 중심) | 분포 모양(shape 중심) |
|---|---|---|
| 단위 / 차원 | 평균, CV, 단일 로그정규 근사 | skewness, bimodality, polymodal distribution |
| 수식 내 위치 | $\theta$와 단일 $\omega^2$ 요약 | $\eta$ histogram, mixture/phenotype 구조 |
| 변화 원인 | 평균 CL·V와 전체 산포 | 유전형/표현형 하위군, residual artifact, data cell imbalance |
| 혼동 시 임상 결과 | 평균이 대표값이라고 오판 | 이봉형 분포의 계곡 평균을 용량 기준으로 사용해 subgroup 위험 누락 |

R&T의 nortriptyline 예시는 로그정규 분포의 사례를, 가상 청소율 분포 예시는 이봉형에서 평균이 치료적 대표값이 되기 어렵다는 점을 보여 줍니다. `[R&T p.363, p.366]` 평균과 CV만 보고 $\eta$ 분포의 모양을 확인하지 않으면, C4에서 다룬 유전 하위군을 통째로 놓치게 돼요.

> ⚡ **Pair 4 한 번 더 — 진짜 신호 vs 모델 결함의 메아리.**
> Residual error model이 잘못 지정되면(예: 실제로는 proportional+additive인데 proportional만 쓴 경우) $\sigma^2$가 저농도에서 과소평가되면서 이 오차가 $\eta$로 흡수됩니다. 그 결과 $\omega^2$가 부풀고, 이 부풀어 오른 $\omega^2$를 "설명하기 위해" covariate가 $\Delta OFV$를 달성해요 — 그런데 그 covariate는 사실 **residual model artifact의 흡수통로**일 뿐입니다. 진짜 covariate 신호와 model artifact를 구분하려면 **순서를 지켜야 해요**: residual model을 먼저 안정화한 뒤에 covariate 탐색을 시작합니다. 진단 시그니처 1(`Leakage Funnel`)이 정적 시그니처라면, 이 고리는 그 신호가 시간 축으로 펼쳐져서 covariate selection 단계까지 왜곡되는 동적 시그니처예요.

**§5 정리.** 이 세션의 혼동은 거의 모두 "**어느 좌표의 변이인가**"로 환원됩니다. 개체 vs 잔차, total vs unbound, PK vs PD, 평균 vs 모양 — 이 네 축을 구분하면 됩니다.

---

<!-- SLIDE_START: §7 | title: 자기 테스트(Self-Test): 능동 회상 모듈(Active Recall Module) -->
<!-- SECTION_CORE: SC-08 -->

## §7 — 자기 테스트(Self-Test): 능동 회상 모듈(Active Recall Module)

### Q1. $CL_i=CL\cdot\exp(\eta_i)$를 쓰는 가장 직접적인 이유는?

**정답.** CL이 음수가 되지 않도록 보장하면서 $\eta$를 정규 분포로 둘 수 있기 때문이에요. R&T는 지수형 오차 모델이 근사적 일정 CV를 주고 계산상의 어려움(computational difficulty)을 줄인다고 설명합니다. `[R&T p.371]`

$$
\underbrace{CL_i}_{\text{개인 CL}}
=
\underbrace{CL}_{\text{모집단 중심}}
\cdot
\underbrace{\exp(\eta_i)}_{\text{양수 배율}}
$$

### Q2. 잔차 변이가 평균 0의 무작위가 아니면 무엇을 뜻하나?

**정답.** 구조 모델이나 오차 모델이 아직 중요한 변이의 원인을 설명하지 못했다는 뜻이에요. 이 상태에서 공변량을 찾으면, **공변량이 생물학이 아니라 잔차 모델의 잘못된 지정을 설명하게 됩니다**. `[R&T p.372]`

### Q3. PK50의 "total CL CV 28%, unbound $CL_u$ CV 9%"를 어떻게 해석해야 하나?

**정답.** $f_u$를 공변량으로 넣어서 $\omega^2$을 28%에서 9%로 줄였다는 뜻이 **아닙니다**. 같은 12명 CpD 자료를 total 좌표와 unbound 좌표로 표현했을 때, 단백 결합 변이가 total parameter variability의 일부를 설명한다는 뜻이에요. `[G&W p.706–709]`

### Q4. $CV(CL)^2 \approx CV(f_u)^2 + CV(CL_u)^2$를 이 문서에서 쓰지 않는 이유는?

**정답.** 이 분산 전파식은 **로그 스케일에서 $f_u$와 $CL_u$가 독립일 때만 성립하는 일차 근사**입니다. 식 자체가 수학적으로 틀린 게 아니라, **그 독립성 가정이 임상에서 비현실적**이에요 — 실제로 알부민 변동은 $f_u$에도 $CL_u$에도 동시에 영향을 주고, 단백결합 변동이 큰 약물에서는 두 변이가 양 또는 음의 상관을 보입니다. 따라서 본 문서에서는 PK50 자료의 total/unbound 차이를 **분산 전파**가 아니라 **좌표 재모수화**(§C3 B항)로 다루며, 부정확할 수 있는 일차 근사식은 채택하지 않습니다. `[교과서 외 구현 해석; 개념 근거: G&W p.706–709]`

$$
\underbrace{CV(CL)^2}_{\text{CL 변이}}
\approx
\underbrace{CV(f_u)^2}_{\text{fu 변이}}
+
\underbrace{CV(CL_u)^2}_{\text{CL_u 변이}}
+
\overbrace{2\rho\cdot CV(f_u)\cdot CV(CL_u)}^{\text{상관 보정항 (실무에서 종종 0이 아님)}}
$$

*↑ 위 식의 오른쪽 마지막 항(상관 보정항)이 0이라는 보장이 없기 때문에 단순 가법 분산 전파는 적용하지 않습니다.*

### Q5. PK50에서 비결합 농도를 써도 PD 변이가 남은 이유는?

**정답.** 단백 결합은 PK 좌표 변이의 일부를 설명하지만, 반응 변이는 수용체 밀도·유전적 구성 같은 PD 원인을 포함해요. G&W는 $E_{max} < 1$인 무반응자가 표적의 완전한 발현을 결여한 것으로 해석합니다. `[G&W p.707–709]`

$$
\underbrace{E_{max}}_{\text{최대효과}}
<
\underbrace{1}_{\text{완전반응 기준}}
$$

### Q6. $\eta$-EBE 히스토그램이 두 봉우리로 보이면 가장 먼저 무엇을 의심하나?

**정답.** 매끄러운 로그정규 IIV 하나가 아니라, **유전형/표현형 하위군 또는 혼합형 모집단 구조**가 섞였는지 의심해야 합니다. 단, 희소 표본이면 히스토그램 자체의 정보량을 먼저 점검해야 해요. `[R&T p.366, p.393–397]`

### Q7. 인종 공변량을 유전형처럼 해석하면 왜 위험한가?

**정답.** R&T는 인종이 개인 유전 형질의 **불완전한 proxy**이며, 그룹 내 변이도 크다고 경고합니다. 인종 항목은 탐색적 공변량일 수 있지만 mechanistic 유전형의 대체물이 아니에요. `[R&T p.395, p.409]`

### Q8. 잔차 모델 오지정 vs 공변량 추가 — 어느 것을 먼저 고치나?

> ⚡ **보스 딜레마 ★★**
> 잔차 모델 오지정이 의심되는 상황에서 공변량 탐색을 시작하려고 합니다. 두 전략이 충돌해요.
>
> **선택지 A — 잔차 안정화 우선:** $\varepsilon$ 구조를 먼저 잡습니다. $\varepsilon$이 자리 잡으면 $\omega^2$ 안의 진짜 공변량 신호가 드러나요. **단점:** 잔차 모델 결정이 지연되면 전체 모델 구축 일정이 늦어지고, sponsor가 timeline pressure를 거는 후기 단계에서는 부담이 됩니다.
>
> **선택지 B — 공변량 탐색 우선:** $\omega^2$ 감소 패턴을 보면서 어떤 공변량이 IIV를 설명하는지 확인한 뒤, 잔차 모델을 조정합니다. **단점:** 잔차 모델 artifact가 공변량으로 잘못 흡수될 위험 (진단 시그니처 1 Leakage Funnel이 시간 축으로 펼쳐지는 시나리오; Pair 4의 기억 고리 참조).
>
> 각 선택을 규제 보고서에서 어떻게 방어할 건가요?

**정답(표층).** 잔차 모델 오지정을 먼저 고칩니다. $\varepsilon$ 구조가 틀린 상태에서 공변량을 추가하면 $\omega^2$와 $\sigma^2$의 경쟁이 왜곡돼서, **생물학이 아니라 오차 모델의 실패를 공변량이 설명하게** 돼요. `[R&T p.371–373]`

**거장의 상충 논리(Trade-off).** A가 순서상 올바르지만 초기 데이터 탐색 단계에서는 잔차 모델이 아직 불확실하니까 무한 재탐색 루프에 빠질 위험이 있어요. 실무 베테랑이 쓰는 방법은 **A를 default로 두되 single-iteration 한도를 두는 것** — 즉 잔차 모델 후보 2–3개를 a priori 정의해 두고, 단 한 번의 비교로 결정한 뒤 공변량 탐색으로 넘어갑니다. B는 탐색적이지만, 최종 모델에서 잔차 모델을 명시적으로 재검토했다는 증거가 필요해요. 이 경로를 택한다면 보고서에 **반드시 민감도 분석** (다른 잔차 모델에서 공변량 선택 결과가 어떻게 달라지는지)을 명시합니다.

**규제 방어 문구**
- 선택지 A 채택 시: *"Residual error model was finalized prior to covariate evaluation based on a priori candidate set {additive, proportional, combined} compared by $\Delta OFV$ and CWRES distribution; covariate selection proceeded only after residual model lock."*
- 선택지 B 채택 시: *"Residual error model misspecification influence on covariate selection was assessed by sensitivity analysis: covariate model {final} was re-fitted under alternative residual structures and $\Delta OFV$ directionality, parameter estimate stability, and VPC consistency were verified."*

**다음 깊이 질문.** 그렇다면 민감도 분석이 통과하지 못했을 때 — 즉 잔차 모델 변경 시 공변량 선택 결과가 뒤집힐 때 — 그 공변량을 보고서에서 어떻게 처리할 것인가? (선행: 모델 평균? 후행: 두 모델 모두 보고? 결정: 더 보수적인 모델 채택?)

**SR 태그:** ★★ (다음 세션 반드시 재등장)

### Q9. SCM forward·backward 임계가 비대칭(α=0.05 vs α=0.01)인 이유는?

**정답.** Forward selection은 다수 covariate 후보에 대한 multiple testing을 거치기 때문에 family-wise error rate가 누적돼요 — 후보 10개에 α=0.05를 각각 적용하면 누적 false positive 위험이 약 40%에 이릅니다. Backward elimination에서 더 엄격한 α=0.01 (ΔOFV ≥ 6.63) 을 통과해야 살아남도록 설계해서 이 누적 위험을 보정하는 게 Jonsson-Karlsson SCM (1998) 의 핵심 설계예요. `[교과서 외 구현/규제 표준; 1차 문헌: Jonsson EN, Karlsson MO. *Pharm Res* 1998;15(9):1463–1468]` C3 §E 참조.

$$
\underbrace{P_{\text{FWE}}}_{\text{family-wise error}}
\approx
\overbrace{1-(1-\alpha)^k}^{\text{누적 위험}}
$$

### Q10. 3-level race covariate에 ΔOFV ≥ 3.84를 쓰면 왜 잘못인가?

**정답.** 3-level race는 reference 외 2개 indicator를 추가하므로 자유도 df = K-1 = 2예요. 이 때 forward 임계는 $\chi^2_{df=2,\,\alpha=0.05} = 5.99$이고 backward는 $\chi^2_{df=2,\,\alpha=0.01} = 9.21$입니다. df=1의 3.84/6.63을 그대로 쓰면 실제 임계보다 관대하게 적용돼 false positive가 발생합니다. Multi-level categorical은 covariate가 추가될 때마다 df를 자동 보정해야 해요. C3 §F 참조.

$$
\underbrace{\mathrm{df}}_{\text{자유도}}
=
\underbrace{K}_{\text{level 수}}
-
\underbrace{1}_{\text{reference}}
$$

**§7 정리.** 시험 문제의 정답은 거의 다 한 줄로 환원돼요 — "**변이의 원인을 잘못된 그릇에 담지 말라**".

---

<!-- SLIDE_START: §8 | title: 메타 프레임 및 큰 그림(Meta-Frame & Big Picture) -->
<!-- SECTION_CORE: SC-09 -->

## §8 — 메타 프레임 및 큰 그림(Meta-Frame & Big Picture)

### A. 28-session 커리큘럼에서 이 세션의 위치

이 세션은 PopPK 커리큘럼의 **분산 축(variance axis)**입니다. 이전 세션들이 CL, V, ka, $t_{1/2}$ 같은 구조 파라미터의 평균을 세웠다면, 이 세션은 그 평균 주변의 개인차와 잔차를 분해해요. 그래서 이후 FOCE/FOCE-I, GOF, 공변량 선택, Bayesian TDM은 모두 이 분해 위에서만 의미를 가집니다.

### B. 의존성 — 대충 넘기면 어디서 무너지나

| 의존 항목 | 대충 넘기면 생기는 실패 |
|---|---|
| C1 $\theta$/$\eta$/$\varepsilon$ | `$OMEGA`와 `$SIGMA`를 숫자로만 읽고, 생리학과 잔차 noise를 구분하지 못함 |
| C2 잔차 오차 | 잘못된 $\varepsilon$가 $\omega^2$로 새어 가짜 IIV 또는 가짜 공변량을 만듦 |
| C3 공변량/재모수화 | $f_u$, CrCl, 체중을 모두 같은 방식의 공변량으로 취급해 좌표 변환과 인과 예측변수를 혼동 |
| C3 §E SCM 비대칭 임계 | forward만 돌리거나 multi-level df 보정 누락 시 multiple testing이 통제되지 않음 |
| C3 §F 다층 범주형 | full stratification으로 시작하다가 작은 cell RSE 폭발로 모델 식별 실패 |
| C4 유전 다형성 | 이봉형 분포를 단일 로그정규 $\eta$로 덮어 하위군 용량 위험을 숨김 |
| EDA 우선 | spaghetti plot과 변환 플롯 없이 control stream부터 쓰다가 하위군 신호를 놓침 `[G&W p.334–336]` |
| 규제 PopPK 일관성 | $\theta$, $\omega^2$, $\sigma^2$, 잔차 모델, 공변량 효과가 서로 일관되지 않으면 보고서 표는 완성되어 있어도 용량 근거가 무너짐 `[R&T p.373]` |

> 💼 **NDA Section 5.2의 line-item 일관성 — 실무 한 줄**
> 규제 reviewer는 PopPK 보고서의 $\omega^2$, $\sigma^2$, 잔차 모델, $\eta_{EBE}$ 분포, 공변량 효과를 순차 line item으로 읽습니다. 하지만 실제로 감사하는 건 line item 각각이 아니라 **그들 사이의 상호 일관성**이에요. 예를 들어 $\sigma^2$(proportional)로 보고된 CV가 분석법 검증 보고서의 CV와 동떨어져 있으면 모델 전체의 prior justification이 흔들리고, 첫 의문 한 줄이 후속 모든 표로 cascade됩니다.
> **꿀팁:** Session 13의 모든 분산 결정은 자체로 정합적일 뿐 아니라 **인접 보고서들의 좌표와 일치해야** 해요 — 즉 $\sigma^2$ ↔ assay CV, total threshold ↔ unbound dose recommendation, $\eta$ 분포 모양 ↔ 모집단 약리유전 컨텍스트가 한 묶음으로 검토됩니다.
> **실무 활용:** 모델 lock 전에 (1) bioanalytical CV 표, (2) 안전 임계 좌표, (3) 모집단 유전 reference를 펼쳐서 line item별 cross-check sheet를 만드세요. R&T p.373이 말하는 "regulatory requirement"의 실무 번역이 바로 이거예요.

### C. 전문가가 갈리는 지점 — 다섯 가지 질문

초급자는 "IIV가 큽니다"라고 말합니다. 중급자는 "CL에 covariate를 넣겠습니다"라고 말해요. 전문가는 다음 다섯 질문을 던집니다.

| 거장의 질문 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| PK인가 PD인가? `[R&T p.363–364; G&W p.707–709]` | $\eta_{CL}$ vs $\eta_{EC50}$ | → | 농도 개체화와 반응 개체화 혼동 | PK/PD 별도 적합 후 IIV 비교 |
| $\eta$인가 $\varepsilon$인가? `[R&T p.369–373]` | OMEGA vs SIGMA | → | assay/잔차 문제를 공변량으로 오인 | residual model 변경 전후 OMEGA/SIGMA 비교 |
| Total인가 unbound인가? `[G&W p.706–709]` | $\omega^2$(CL) vs $\omega^2$($CL_u$) | → | safety threshold와 dose recommendation 좌표 불일치 | total/unbound 모델 병렬 보고 |
| smooth distribution인가 subgroup/phenotype 구조인가? `[R&T p.366, p.393–410]` | $\eta$-EBE histogram, mixture effect | → | 평균 dose가 하위군 위험을 숨김 | bimodality 및 cell size 확인 |
| mechanistic covariate인가 proxy인가? `[G&W p.348–351; R&T p.395]` | covariate THETA, RSE, condition number | → | 식별 불가능한 accounting device를 생리학으로 보고 | bootstrap/SIR, 공선성, identifiability 점검 |

### D. 후속 세션 연결

| 후속 세션 | 이 세션에서 열리는 개념 | 이 세션 없으면 실패하는 것 |
|---|---|---|
| FOCE / FOCE-I | $\theta$–$\eta$–$\varepsilon$ 동시 추정과 EBE 조건부 해석 | EBE를 개인 참값으로 오해 |
| GOF / CWRES | residual model 안정화와 leakage funnel 진단 | 공변량 탐색 전에 잔차 artifact 미제거 |
| $\eta$-EBE / shrinkage | 개체별 정보량과 분산 분해능 | high-shrinkage plot 과해석 |
| Stepwise covariate selection | $\omega^2$ 중 설명 가능한 생리학의 이동 | OFV-driven fishing; forward-only 보고; df 보정 누락 |
| Bayesian TDM | 개인 $\eta$ 업데이트와 용량 개체화 | 평균 dose 또는 잘못된 좌표에 의존 |

> 🔬 **거장의 질문을 NONMEM 출력으로 번역하기**
> 위 다섯 질문은 추상적 사고가 아니에요. 각 질문은 **실제 NONMEM 출력이나 진단 파일의 특정 시그니처로 답해야** 합니다. 전문가의 해석 능력은 질문을 던지는 데 있는 게 아니라, **그 질문을 출력 파일에서 읽어내는 능력**에 있어요.
>
> | 거장의 질문 | NONMEM/진단 출력 시그니처 |
> |---|---|
> | Q1. PK인가 PD인가? | PK 자료(농도)와 PD 자료(반응)를 **별도 모델로 적합**한 뒤 $\omega^2$(PK)와 $\omega^2$(PD)를 비교. 같은 환자의 $\eta_{CL}$과 $\eta_{EC50}$이 상관이 낮으면 두 영역의 IIV 원인이 독립적이라는 신호. |
> | Q2. $\eta$인가 $\varepsilon$인가? | **OMEGA 행렬 대각 원소 변화** vs **SIGMA 추정값 변화**를 잔차 모델 변경 전후로 비교. $\varepsilon$ 모델을 바꿨더니 $\omega^2$(CL)이 크게 움직이면 진단 시그니처 1 leakage funnel이 작동 중. $\eta$-shrinkage가 30% 미만일 때만 $\eta$-EBE 기반 진단을 신뢰. |
> | Q3. Total인가 unbound인가? | Total 적합의 $\omega^2$(CL)과 unbound 적합의 $\omega^2$($CL_u$)을 **나란히 비교**. PK50 패턴(28% vs 9%)이 재현되면 $f_u$가 결정론적 재모수화로 작동 중인 것. $f_u$ 자체에 $\eta$를 부여한 모델과 안 부여한 모델의 $\Delta OFV$로 $f_u$ 측정 변이 분리 여부를 판정. |
> | Q4. Smooth인가 하위군 구조인가? | **$\eta$-EBE 히스토그램**(R `xpose4::eta.dist()` 또는 PsN sse output)에서 이봉형 여부 확인. 혼합 모델 `$MIX`의 $\Delta OFV$ vs 단일 로그정규 IIV. 단, 작은 n cell에서는 진단 시그니처 2 `Empty Phenotype Cell`(RSE >80%, `$COV step` 실패)을 먼저 점검. |
> | Q5. Mechanistic인가 proxy인가? | **Bootstrap 또는 SIR**으로 공변량 효과의 95% CI 폭을 확인. CI가 0을 포함하지 않더라도 폭이 비대칭하거나 매우 넓으면 식별가능성 결손 의심. `$COV step`의 condition number(>1000이면 ill-conditioned)와 공변량-공변량 상관행렬(|r|>0.7이면 다중공선성)을 같이 본다. |
>
> $$
> \underbrace{\eta\text{-shrinkage}}_{\text{EBE 분해능}}<\underbrace{30\%}_{\text{경고선}},\quad
> \underbrace{RSE}_{\text{불확실성}}>\underbrace{80\%}_{\text{불안정}},\quad
> \underbrace{condition\ number}_{\text{수치 조건성}}>\underbrace{1000}_{\text{조건성 경고}},\quad
> \underbrace{|r|}_{\text{상관}} > \underbrace{0.7}_{\text{공선성 경고}}
> $$
>
> **꿀팁:** 거장의 질문 각각에 NONMEM 출력 한 곳을 1:1로 매핑하지 못하면, 그 질문은 보고서에서 방어할 수 없어요. 보고서 line item마다 어느 출력에서 그 결론이 나왔는지를 cross-reference할 수 있어야 합니다 — 이게 NDA 5.2 line-item consistency가 실무에서 작동하는 방식이에요.

### 최종 정리

Session 13의 최종 메시지는 하나예요. **$\omega^2$은 "남은 변이"가 아니라, 아직 이름 붙이지 못한 생리학·유전학·행동·측정 구조의 혼합물입니다.** C2가 잔차 noise를 정리하고, C3가 설명 가능한 생리학을 꺼내요. C4는 매끄러운 IIV 안에 숨어 있는 유전적 불연속성을 드러냅니다. 이 순서를 지키지 않으면 NONMEM은 돌아가지만, 용량 개체화는 성립하지 않습니다.

v4.2 보강본은 여기에 한 줄을 더 추가합니다 — **그 분해를 통과한 covariate라도 statistical false positive (SCM 비대칭 임계 미적용) 와 mechanistic false positive (VPC·cell size·a priori physiology 검증 누락) 의 두 관문을 같이 통과해야** 한다는 것. C3 §E와 §M이 그 두 관문의 양쪽 문을 잡고 있어요.

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
| v4.2 신규 보강 항목 1:1 매핑 | C2 §F footnote, C3 §E, C3 §F | ✓ |
| 신규 §7 Q9·Q10 SCM/categorical | 출처 인용 명시 | ✓ |
| 신규 수식 annotation overbrace/underbrace | C3 §E·§F 전체 | ✓ |

**검증 메모**: v4.1 → v4.2 보강은 (1) C2 §F의 BLOQ 임계값 출처 명확화 (Beal 2001 vs Bergstrand-Karlsson 2009 분리 인용), (2) C3 §E SCM 비대칭 임계 신설 (Jonsson-Karlsson 1998), (3) C3 §F 다층 범주형 처리 신설, (4) §7 Q9·Q10 신설, (5) §8 B·D 행 추가로 구성됩니다. 모든 원본 SLIDE_START·SECTION_CORE 마커·수치 anchor·약물명·G&W·R&T 페이지 anchor는 byte-preserved.
-->

<!-- v4.2 보강 노트 (v4.1 → v4.2)
- v4.1 → v4.2: 임상·규제 실무 readiness 추가 보강 (3차 전문가 검토 의견 반영)
- 보존 감사 (1:1 매핑): 기존 모든 SLIDE_START 마커, SECTION_CORE 마커(SC-01~SC-09), 수치 anchor (PK50: 11.4/28%, 720/9%, 4.35/39%, 19.9/29%, 30.9/35%, 265/33%, 1270/18%, 2030/51%, fu=0.016±0.0049, C>50 µg/L; PM 빈도; ΔOFV 3.84; RSE 80%; shrinkage 30%; condition number 1000; |r| 0.7), 약물명 (warfarin, nortriptyline, codeine, thiopurines, isoniazid, CpD), 카드 ID (C1~C4), 출처 anchor (R&T p.361–410, G&W p.333–352·p.704–710) 모두 byte-preserved
- v4.2 신규 보강 항목 (3개, 모두 [교과서 외 구현/규제 표준] 태그):
  1. **C2 §F BLOQ 임계값 footnote** — 5%/15% 임계가 Beal 2001 원전이 아니라 Bergstrand-Karlsson 2009 후속 검증에서 정착된 값임을 명시. method 출처(Beal 2001)와 임계 출처(Bergstrand-Karlsson 2009; Ahn 2008)를 분리해서 인용하도록 규제 보고서 표준 문구 보강. (1차 문헌: Bergstrand M, Karlsson MO. AAPS J 2009;11(2):371–380)
  2. **C3 §E Stepwise Covariate Model(SCM) 정량 임계 신설** — forward(ΔOFV ≥ 3.84, α=0.05) vs backward(ΔOFV ≥ 6.63, α=0.01) 비대칭 임계 표 + family-wise error 식 + 규제 보고서 표준 문구 추가. (1차 문헌: Jonsson EN, Karlsson MO. Pharm Res 1998;15(9):1463–1468; Stat Med 1998;17(15):1745–1757)
  3. **C3 §F 다층 범주형 covariate 처리 신설** — multiple THETA / indicator variable / hierarchical structure 비교 표 + sex × phenotype 2-way NMTRAN 예시 + 곱셈 가정 식 + 실무 결정 트리 (cell size n≥30 / 5–30 / <5) + multi-level df = K-1 자동 보정 표. (개념 근거: R&T p.369 — sex·race를 covariate 후보로 명시)
- v4.2 부수 변경:
  - §1 출처 인용 약어 규약 박스에 Jonsson-Karlsson 1998 및 Bergstrand-Karlsson 2009 추가
  - C4 §C 실무 인사이트에 "C3 §F 결정 트리 참조" 크로스 링크 추가
  - C4 §D 진단 시그니처 2에 "C3 §F의 결정 트리 참조" 크로스 링크 추가
  - C3 카드 yaml의 aliases/tags/source에 SCM·multi-level categorical·R&T p.373 추가
  - §7에 **Q9 (SCM 비대칭 임계 근거)** 및 **Q10 (multi-level df 보정)** 신설
  - §8 B 의존성 표에 SCM·다층 범주형 항목 2행 추가
  - §8 D 후속 세션 표 stepwise covariate selection 행에 "forward-only 보고·df 보정 누락" 함정 추가
  - 최종 정리에 v4.2 한 줄 메시지 추가 (statistical false positive + mechanistic false positive 두 관문)
- 수식 annotation: 신규 수식 전체에 overbrace/underbrace 적용 (Forward/Backward 임계 표시, family-wise error, df 공식, multi-level CL 식)
- 인용 강화: 신규 1차 문헌 5건 정식 서지 (Beal 2001 JPP 28(5):481–504, Bergstrand-Karlsson 2009 AAPS J 11(2):371–380, Ahn 2008 JPP 35(4):401–421, Savic-Karlsson 2009 AAPS J 11(3):558–569, Jonsson-Karlsson 1998 Pharm Res 15(9):1463–1468)
- 변경 없는 영역: 임상 장면, 학습 경로, §1 헤더의 본문, §1 IIV·IOV·RUV·IOV vs TVC 표, C1 §A–F 전부, C2 §A–E, C3 §A–D·§M, C4 전체, §5, §7 Q1–Q8 — 모두 byte-preserved
-->
<!-- v4.1 보강 노트 (v4.0 → v4.1)
- v4.0 → v4.1: 임상·규제 실무 readiness 보강 (전문가 검토 의견 반영)
- 보존 감사 (1:1 매핑): 기존 모든 SLIDE_START 마커, SECTION_CORE 마커, 수치 anchor, 약물명, 카드 ID, 출처 anchor 그대로 유지
- 보강 항목 (6개, 모두 [교과서 외 구현/규제 표준] 태그):
  1. §1 IIV/IOV/RUV 표 다음에 **IOV vs TVC 구분 표 + 수식** 추가 (개념 근거: R&T p.371)
  2. C1에 **§F 상관된 random effect / OMEGA BLOCK** 신설 — diagonal vs BLOCK, ρ_CL,V 해석, 임계 (개념 근거: R&T p.369–373)
  3. C1 §E **η-shrinkage 정량 정의** Savic & Karlsson 2009 수식 + 20/30% 임계 표 추가 (1차 문헌: AAPS J 2009;11(3):558–569)
  4. C2에 **§F BQL/LOQ 처리** Beal 2001 M1/M3/M5/M6 표 + likelihood 수식 + NMTRAN 코드 추가 (1차 문헌: JPP 2001;28(5):481–504)
  5. C3 §A에 **centering value 90 선택 근거 박스** 추가 — 모집단 중앙값/정상/CKD cutoff 비교 표
  6. C3 §D row 4 + §7 Q4 **분산 전파식 삭제 근거 재작성** — "산술 오류"가 아니라 "독립성 가정의 임상적 비현실성"으로 정정; 상관 보정항을 명시한 확장식 제시
- 수식 annotation: 추가 수식 전체에 overbrace/underbrace 적용
- 인용 강화: 제목 헤더 Source 라인을 Rowland & Tozer (R&T 5e) / Gabrielsson & Weiner (G&W 5e) 정식 서지로 확장; 인용 약어 규약 박스 추가
- 변경 없는 영역: 임상 장면, 학습 경로, §1 헤더, C1 §A–E, C2 §A–E, C3 §B–C·M, C4 전체, §5, §8 — 모두 byte-preserved
-->
<!-- v4.0 변환 노트
- v3.9 → v4.0: Spoken-Voice Rewrite, Byte-Preserved Scope
- 보존 감사 (1:1 매핑):
  · SLIDE_START 마커: 9개 (§1, §2, C1, C2, C3, C4, §5, §7, §8) — v3.9와 동일
  · SECTION_CORE 마커: SC-01~SC-09 — v3.9와 동일
  · 수식 $$ 블록: 20개 — v3.9와 동일
  · 출처 anchor: G&W·R&T 페이지 anchor 전체 보존, 인라인 위치 유지
  · 수치 anchor: 모두 일치
  · 약물명: warfarin, nortriptyline, codeine, thiopurines, isoniazid, CpD — 모두 일치 (각 약물 첫 등장 시 분류·기전·임상특징 즉맥락 3-step 적용)
  · 카드 ID: C1, C2, C3, C4 위치·이름 보존
- 주요 표현 변환 (Park 교수 본능):
  · 번역체/관념어 제거
  · 메타-언어 헤더 삭제·산문화
  · 약물 즉맥락 3-step
  · 임상 장면 hook 강화
- 콜아웃 단일화: 각 카드 callout 6개 이하 유지
- 거장의 시각: §4 기준 (실무 함정/경계 조건/압축 한 줄) 셋 중 하나에 부합하도록 재작성
- 추가/삭제/재배열: §9 자유 보강 범위 내
-->

---

C-260517-085412-7K9

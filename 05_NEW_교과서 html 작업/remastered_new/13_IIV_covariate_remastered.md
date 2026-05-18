# 세션 13 리마스터 — 개체 간 변이(IIV)와 공변량 모델링: "이 흔들림이 어느 그릇에 들어가야 하는가"

*Source anchor: Rowland M, Tozer TN. **Clinical Pharmacokinetics and Pharmacodynamics: Concepts and Applications**, 5th ed. (이하 **R&T 5e**) Ch.12 (p.361–392) + Ch.13 (p.393–410); Gabrielsson J, Weiner D. **Pharmacokinetic and Pharmacodynamic Data Analysis: Concepts and Applications**, 5th ed. (이하 **G&W 5e**) Ch.4 일부 (p.333–352) + PK50 (p.704–710). 후속 구현·규제 표준은 `[교과서 외 구현/규제 표준]` 태그로 명시함.*

---

## 0. 시작하기 전에 — 이 세션의 치트키 한 줄

이 세션을 절반쯤 듣다 보면 자꾸 길을 잃게 됨. $\theta$, $\eta$, $\varepsilon$, $\omega^2$, $\sigma^2$, IIV, IOV, RUV, covariate, reparameterization, mixture, phenotype… 기호가 한꺼번에 쏟아지기 때문임. 그래서 이 모든 걸 끌고 가는 **단 하나의 마스터 질문**을 먼저 박고 시작하겠음.

> 🎯 **마스터 질문 (Session 13의 모든 문제는 이 한 줄로 환원됨)**
> "지금 내가 보고 있는 이 **흔들림**은, 도대체 **어느 그릇**에 들어가야 하는가?"

그릇은 딱 네 종류임:

| 그릇 | 무엇을 담는가 | NONMEM 위치 |
|---|---|---|
| ① $\theta$ 구조 (covariate로 설명됨) | 측정 가능한 변수로 이름 붙일 수 있는 변이 | `$THETA` + 구조식 |
| ② $\eta$ (IIV) | 사람 사이의 **지속적**·이름 못 붙인 차이 | `$OMEGA` 대각 (개체별) |
| ③ $\eta$ (IOV) | 같은 사람 안의 occasion 간 변동 | `$OMEGA` (occasion 차원 별도) |
| ④ $\varepsilon$ (RUV) | 한 관측 시점의 측정·모델 잔차 | `$SIGMA` |

같은 데이터셋에서 이 네 그릇의 합은 **고정**되어 있음 — "전체 미설명 분산"은 zero-sum으로 다툼. 이게 **변이 보존 법칙**임. 한 그릇에 잘못 담으면 다른 그릇에서 새거나 부풀어 오름. 그래서 그릇 배정 순서를 잘못 잡으면 NONMEM은 돌아가는데, 용량 개체화는 무너짐.

> 💡 **이 세션 전체를 한 줄로** — *"$\omega^2$이 줄었다"가 아니라 "어느 좌표에서 무엇이 설명되었느냐"가 진짜 질문임.*

오늘 강의 전체는 이 마스터 질문에 대답하는 **강제 순서**를 따라감:

```text
0단계: 마스터 질문 + 변이 보존 법칙 박기
1단계: 그릇 4종을 머리에 띄우기 (IIV/IOV/RUV/covariate)
2단계: ε 그릇 먼저 잠그기 (잘못된 ε는 ω²로 새서 가짜 covariate를 만듦)
3단계: ω² 안의 설명 가능한 부분을 θ로 옮기기
       — 좌표 회전(reparameterization)과 변수 추가(covariate)를 구분
4단계: 남은 η의 분포 모양 검사 (smooth vs 다봉/하위군)
5단계: 같은 법칙이 만드는 3가지 진단 시그니처 통합
6단계: 혼동쌍 정리 + 자기 테스트 + 큰 그림
```

이 순서를 어기면 어떤 일이 벌어지는지는 매 단계마다 짚어줄 것임. **순서 자체가 카드의 본문**임을 기억하길.

---

## 1. Hook — 같은 12명, 같은 약, CV가 28% → 9%로 바뀐 장면

본격적인 개념 들어가기 전에 G&W PK50 장면 하나만 띄워놓고 시작하겠음. 이 장면을 머리에 박아두면 §3, §4가 한방에 이해됨.

CpD라는 약을 566 µg, 5시간 IV infusion으로 12명 환자에게 줌. 그리고 청소율을 봄. `[G&W p.704–709]`

$$
\underbrace{CL = 11.4\ \mathrm{L\cdot h^{-1}}}_{\text{총 농도(total) 기준}}\quad
(\overbrace{CV = 28\%}^{\text{사람 사이 흔들림}})
$$

CL 평균 11.4 L·h⁻¹, 사람마다 28%씩 흔들림. 자, 여기까지는 흔한 PopPK 결과임.

그런데 같은 환자, 같은 자료를 **비결합(unbound) 기준 $CL_u$**로 다시 봤더니:

$$
\underbrace{CL_u = 720\ \mathrm{L\cdot h^{-1}}}_{\text{비결합 기준}}\quad
(\overbrace{CV = 9\%}^{\text{흔들림 1/3로 줄어듦}})
$$

CV가 28%에서 9%로 떨어짐. **세 배 가까이 줄어들었음**. 동시에 비결합 분율은 $f_u = 0.016 \pm 0.0049$였고, 안전 경계는 total C > 50 µg·L⁻¹임. `[G&W p.704–709]`

> 🚨 **여기서 가장 흔한 오해 — 그리고 이 세션의 결정적 분기점**
> "와, 단백결합을 covariate로 넣었더니 IIV가 28%에서 9%로 줄어든 거구나!"
> **틀림.** 우리가 한 일은 covariate를 추가한 게 아님. 같은 12명을 **다른 좌표에서 다시 본 것**뿐임.

이게 §4에서 다룰 **재모수화(reparameterization) vs covariate addition**의 결정적 차이임. 두 작업은 NONMEM 코드 한두 줄 차이로 보이지만, 임상적·규제적 의미가 완전히 다름.

자, 이 장면을 머리 한쪽에 띄워놓고 §2부터 그릇 분류 들어감.

---

## 2. 그릇 4종을 머리에 띄우기 — IIV / IOV / RUV / covariate-explained

### 2-1. 왜 그릇부터 잡아야 하는가

PopPK 초보자가 가장 자주 망하는 지점이 여기임. "변동이 크네요, IIV가 크네요"라는 한 줄로 그릇 분류를 안 하고 넘어감. 그러면 다음 단계에서 무조건 막힘. 왜냐하면 같은 "변동"이라도 어느 그릇에 들어가느냐에 따라 처치가 완전히 다르기 때문임.

| 그릇 | 핵심 질문 | 처치 |
|---|---|---|
| **IIV** (inter-individual) | 사람마다 **지속적으로** 다른가? | covariate 탐색, $\omega^2$ 분해 |
| **IOV** (inter-occasion) | 같은 사람도 visit/cycle마다 달라지는가? | occasion-level ETA 추가 |
| **RUV** (residual unexplained) | 한 관측값 자체에 남는 흔들림인가? | $\sigma^2$ 구조 (additive/proportional/exp) 재선택 |
| **TVC** (time-varying covariate) | 측정 가능한 변수가 시점별로 변해서 PK를 흔드는가? | $\theta$ 구조 안에 시점별 covariate |

이 표 한 장을 머리에 띄워놓고 NONMEM control stream을 읽으면, `$OMEGA` block 구조가 왜 그렇게 짜여 있는지가 바로 보임.

### 2-2. IIV vs IOV — 같은 사람 안의 변동을 어디에 담을 것인가

여기서 진짜 헷갈리는 게 IIV와 IOV의 구분임. crossover 시험, oncology cycle dosing, TDM 재방문 자료에서 이걸 잘못 다루면 모든 후속 추정이 비뚤어짐.

**한 줄 요약**: IIV는 사람이 달라서 생기는 변동, IOV는 같은 사람의 시간(occasion)이 달라서 생기는 변동임.

**잘못 다루면 어떻게 망가지는가**: 같은 사람 안의 occasion 간 변동을 IOV로 안 잡고 IIV에 그냥 묻으면, $\omega^2$이 부풀고, 그 부풀어 오른 $\omega^2$를 설명하려고 가짜 covariate가 detect됨. 또는 RUV로 흡수되어 $\sigma^2$가 비현실적으로 커지면서 잔차 진단이 망가짐. 변이 보존 법칙이 작동하는 첫 번째 장면임.

NONMEM에서 IOV는 occasion-level ETA로 표현됨:

$$
\underbrace{CL_{ij}}_{\text{i번째 환자, j번째 occasion}}
=
\underbrace{\theta_1}_{\text{모집단 CL}}
\cdot
\overbrace{\exp(\eta_i)}^{\text{IIV: 지속적 개체차}}
\cdot
\overbrace{\exp(\eta_{ik})}^{\text{IOV: occasion k의 변동}}
$$

### 2-3. IOV vs TVC — 결정적 분기점

이게 진짜 함정임. "시간에 따라 변하는 신호"가 같은 사람 안에서 보이면, 두 가지 해석이 가능함:

| 구분 | IOV | TVC |
|---|---|---|
| 변동 원인 | **측정 불가능**한 무작위 변동 | **측정 가능**한 변수(SCr, 체중, 동반약물) |
| 어디로 들어가나 | random effect ($\eta_{ik}$, `$OMEGA`) | 구조식 ($\theta$ 구조 안의 시간 가변 변수) |
| 임상 예시 | crossover period 간 흡수 변동 | ICU 환자 일별 SCr, oncology cycle 간 체중 손실, rifampin 추가 시점 |

⚠️ **흔한 오류**: "시간에 따라 변하니까 IOV"라는 직관은 **틀림**. **변동의 원인이 측정 가능한 변수면 TVC**임. 측정 불가능하면 IOV.

$$
\underbrace{CL_{ij}}_{\text{i번째 환자, j번째 시점}}
=
\underbrace{\theta_1}_{\text{기준 CL}}
\cdot
\overbrace{\left(\frac{SCr_{ij}}{SCr_{ref}}\right)^{\theta_2}}^{\text{TVC: 시점별 신기능 배율}}
\cdot
\underbrace{\exp(\eta_i)}_{\text{지속 IIV}}
\cdot
\underbrace{\exp(\eta_{ik})}_{\text{occasion IOV}}
$$

ICU 환자 SCr이 매일 변하는데 baseline 한 점만 잡고 fixed covariate로 처리하면, 신기능 변동이 IOV나 RUV로 흡수됨 — "SCr이 CL을 결정한다"는 mechanistic 신호가 random effect에 묻혀 사라짐. 이게 §5에서 다룰 **Vanishing Covariate Cascade**의 시간축 버전임. `[교과서 외 구현/규제 표준; 개념 근거: R&T p.371]`

---

## 3. 강제 순서 1단계 — $\varepsilon$ 그릇부터 잠그기 (RUV 모델 결정)

### 3-1. 왜 잔차부터인가

이 부분이 원본 자료에서 가장 자주 놓치는 부분임. 학습자는 "covariate가 핵심이지!"라고 생각해서 곧장 covariate 탐색으로 뛰어들고 싶어함. **그러면 100% 망함**. 이유는 단순함.

> 🔑 **변이 보존 법칙의 첫 번째 발현**
> $\varepsilon$이 못 흡수한 분산은 **반드시** $\eta$로 새어 나감. 그 새어 나간 분산을 $\eta$로 받으면 $\omega^2$이 부풀고, 부풀어 오른 $\omega^2$를 줄이려고 covariate를 넣으면, 그 covariate는 **생리학이 아니라 $\varepsilon$ 모델의 실패를 설명**하게 됨.

즉, 잔차 모델이 틀린 채 covariate를 채택하면, 그 covariate는 **실재하는 인과관계가 아니라 모델 결함의 메아리**임. 규제 reviewer가 가장 먼저 잡는 deficiency가 이거임.

### 3-2. 세 가지 잔차 모델 — 외울 게 아니라 데이터 모양과 매칭하는 것임

R&T가 명시한 세 가지 형태: `[R&T p.372]`

| 모델 | 식 | 언제 쓰나 (데이터 시그니처) |
|---|---|---|
| **Additive** | $Y = F + \varepsilon$ | 농도 범위가 좁고 절대오차가 일정 |
| **Proportional** | $Y = F(1+\varepsilon)$ | 농도 범위 전반에서 CV가 거의 일정 |
| **Exponential** | $Y = F\cdot\exp(\varepsilon)$ | 양수 보장 필요 + 로그 스케일에서 가법 |

지수형은 로그 변환 후 가법형이 됨: `[R&T p.373]`

$$
\underbrace{\ln Y}_{\text{로그 관측값}}
=
\underbrace{\ln F}_{\text{로그 예측값}}
+
\underbrace{\varepsilon}_{\text{로그 잔차}}
$$

실무에서 진짜 자주 쓰는 건 **combined model**임 — additive와 proportional을 합쳐서 LLOQ 근처와 고농도를 한 렌즈로 잡음 `[교과서 외 구현 번역]`:

```nmtran
$ERROR
IPRED = F
W     = SQRT((THETA(3)*IPRED)**2 + THETA(4)**2)   ; 비례 + 가법 결합 스케일
Y     = IPRED + W*EPS(1)
```

$$
\underbrace{Y}_{\text{관측값}}
=
\underbrace{IPRED}_{\text{개인 예측}}
+
\overbrace{\sqrt{\underbrace{(\theta_{prop}\cdot IPRED)^2}_{\text{비례 성분}}+\underbrace{\theta_{add}^2}_{\text{가법 성분}}}}^{\text{$W$: 결합 잔차 스케일}}
\cdot
\underbrace{\varepsilon}_{\text{표준 잔차}}
$$

> 💡 **$W$의 직관** — 카메라 흔들림 보정 같은 거임. 어두운 곳(LLOQ 근처)의 절대 흔들림과 밝은 곳(고농도)의 상대 흔들림을 한 렌즈로 동시에 잡음.

### 3-3. 진단 시그니처 1 — Leakage Funnel

> 🔬 **시그니처 1 — `$\omega^2$–$\sigma^2$ Leakage Funnel`**
>
> **어떻게 생겼나**: Proportional-only RUV로 LLOQ-rich 자료를 적합하면, CWRES vs PRED plot에서 **저농도 영역이 깔때기처럼 벌어짐**. 동시에 $\omega^2$(CL)이 비현실적으로 부풀고, $\eta$-shrinkage가 치솟음.
>
> **왜 생기나**: 저농도의 절대오차가 큰데 proportional만 쓰면, 그 흔들림을 $\sigma^2$가 못 잡음 → 남은 분산이 $\eta$로 새어 $\omega^2$ 부풀림 → 변이 보존 법칙.
>
> **잘못된 처치**: "$\omega^2$이 크네, covariate를 찾아보자!"
> **올바른 처치**: "잔차 모델 좌표가 틀렸다, additive 성분을 추가하자."
>
> **핵심**: $\omega^2$이 너무 크다는 느낌이 들 때 가장 먼저 의심할 건 **새 covariate가 아니라 잔차 모델 좌표**임.

### 3-4. BLOQ 처리 — M1 vs M3, 그리고 임계값의 진짜 출처

§3-2가 다룬 잔차 모델은 LLOQ **위쪽** 관측만 다룸. 그런데 현대 PopPK 분석의 5–30%는 LLOQ 미만(**BQL**) 관측을 어떻게 처리하느냐로 결과가 달라짐. Leakage Funnel이 가장 심하게 일어나는 영역이 바로 LLOQ 근처임 — BQL 처리법을 안 정하면 funnel을 봐도 고칠 수가 없음.

Beal (2001)의 표준 처리: `[교과서 외 구현; 1차 문헌: Beal SL. *J Pharmacokinet Pharmacodyn.* 2001;28(5):481–504]`

| 방법 | 처리 방식 | 편향 | 권고 |
|---|---|---|---|
| **M1** | BQL 단순 제외 | 큰 편향 — 분포 꼬리 잘림 | 권고 안 함 |
| **M3** | BQL을 **censored data**로 likelihood에 통합 | 가장 작음 | **현대 표준** |
| **M5** | BQL을 LLOQ/2로 대입 | 중간 | 보조 |
| **M6** | 첫 BQL만 LLOQ/2, 이후 연속 BQL 제외 | M5보다 작음 | 보조 |

M3의 핵심은 "값은 모르지만 **LLOQ 미만이라는 것은 안다**"는 정보를 부분 likelihood로 살리는 것임:

$$
\underbrace{L_i^{BQL}}_{\text{BQL 관측의 likelihood}}
=
\overbrace{\Phi\!\left(\frac{\underbrace{LLOQ}_{\text{정량한계}} - \underbrace{F_{ij}}_{\text{개인 예측}}}{\underbrace{W_{ij}}_{\text{잔차 스케일}}}\right)}^{\text{관측이 LLOQ 미만일 확률}}
$$

```nmtran
; [교과서 외 구현; Beal 2001 M3]
$ERROR
IPRED = F
W     = SQRT((THETA(3)*IPRED)**2 + THETA(4)**2)
IF (BQL.EQ.0) THEN
  Y      = IPRED + W*EPS(1)
  F_FLAG = 0
ELSE
  CUMD   = PHI((LLOQ - IPRED)/W)
  Y      = CUMD
  F_FLAG = 1           ; FOCE-LAPLACE 필요
ENDIF
```

> 📚 **중요 — 임계값(5%, 15%)의 진짜 출처** `[교과서 외 후속 구현/규제 표준]`
> "BQL fraction > 15%면 M3 필수"라는 임계는 **Beal 2001 원전에 없음**. Beal 2001은 method 정의의 1차 문헌일 뿐임. 임계값은 후속 검증 연구에서 정착됨:
> - **Bergstrand M, Karlsson MO.** *AAPS J.* 2009;11(2):371–380 — 시뮬레이션으로 5–10%부터 M1 편향이 임상적으로 의미 있어지고, 15–20%부터 M3 필수임을 정량화
> - **Ahn JE et al.** *J Pharmacokinet Pharmacodyn.* 2008;35(4):401–421 — 추정 방법별 편향 정리
>
> 규제 보고서에 "*Per Beal (2001), BQL > 15% requires M3*"라고 쓰면 **부정확함** — Beal 2001은 임계를 정의한 적이 없음. method 출처와 임계 출처를 분리해서 기재해야 함.

⚠️ **흔한 silent failure**: M3는 **FOCE-LAPLACE 이상**이 필요함 (FO·FOCE는 CDF likelihood 못 다룸). M3 켜고 FOCE 그대로 돌리면 NONMEM이 silently fail함 — 추정은 끝나는데 BQL 처리가 적용되지 않은 결과가 나옴.

> 💼 **규제 방어 표준 문구**
> *"Below quantification limit observations were handled using the M3 method (Beal, 2001), with the likelihood specified as the cumulative probability of falling below LLOQ given individual prediction and residual error model. The decision threshold for M3 adoption (BQL fraction > ~15%) followed Bergstrand & Karlsson (2009). Sensitivity to BQL handling was assessed by re-fitting under M1 and M6."*

### 3-5. 이 단계 핵심

- 농도 dynamic range ≥ 2 log → 자연로그 변환 + 변환된 오차 모델
- LLOQ-rich data → additive 또는 combined 성분
- BQL > 15% → M3 필수 (FOCE-LAPLACE 이상)
- 잔차에 추세가 남는다 → **공변량 전에 구조/오차 모델부터 재검토**

이 단계가 끝나야 §4로 넘어갈 자격이 생김.

---

## 4. 강제 순서 2단계 — $\omega^2$ 안의 설명 가능한 부분을 $\theta$로 옮기기

### 4-1. 본 단계의 첫 번째 함정 — "공변량은 $\omega^2$을 줄이는 통계 기법"이라는 오해

여기서 §1의 PK50 hook을 회수함. 학습자 대부분이 공변량 모델링을 **"$\omega^2$을 깎는 통계 기술"**로 이해함. NONMEM이 그렇게 행동하기도 함 — covariate 넣으면 $\Delta OFV$ 떨어지고 $\omega^2$ 줄어듦.

그런데 진짜 본질은 이거임:

> 🎯 **공변량 모델링의 정의 (외워둘 것)**
> 공변량은 $\omega^2$을 **줄이는** 게 아니라, $\omega^2$ 안에 섞여 있던 **설명 가능한 생리학을 $\theta$ 구조로 옮기고 이름을 붙이는 작업**임.
> 그래서 결과적으로 $\omega^2$이 작아지는 거지, $\omega^2$을 작게 만드는 게 목표인 게 아님.

방 안의 소음을 그냥 줄이는 게 아니라, "이건 냉장고 소리, 이건 창밖 차 소리, 이건 옆방 목소리"라고 **이름을 붙이는 일**임. 이름이 붙은 순간 그 소음은 $\eta$ 그릇에서 $\theta$ 그릇으로 자리를 옮김.

### 4-2. 표준 형태 — 신기능을 CL에 옮기기

R&T가 든 대표 예시 `[R&T p.369–371]`:

```nmtran
; [교과서 외 구현 번역]
CL = THETA(1) * (CRCL/90)**THETA(2) * EXP(ETA(1))
```

$$
\underbrace{CL_i}_{\text{개인 CL}}
=
\underbrace{\theta_1}_{\text{기준 CL}}
\cdot
\overbrace{\left(\frac{CRCL_i}{90}\right)^{\theta_2}}^{\text{기준 신기능 대비 배율}}
\cdot
\underbrace{\exp(\eta_i)}_{\text{이름 못 붙인 나머지}}
$$

여기서 자주 놓치는 디테일이 **분모 90의 정체**임.

> 💡 **Centering value 90은 보편 기준이 아님** `[교과서 외 구현/규제 표준]`
> 분모 90 mL·min⁻¹는 NONMEM이나 R&T가 정해준 표준이 아님. **Dataset-specific choice**임.
>
> | 선택지 | $\theta_1$의 임상적 의미 |
> |---|---|
> | 모집단 중앙값 (가장 흔함) | 표본 중심의 신기능을 가진 환자의 CL |
> | 정상 신기능 (120 mL·min⁻¹) | 정상 신기능 환자의 CL |
> | 임상 cutoff (60, CKD stage 3 경계) | 신기능 저하 진입 시점의 CL |
>
> Centering 값은 단순한 정규화 상수가 아니라 **$\theta_1$ 해석 좌표 자체**를 결정함.

$$
\underbrace{\theta_1}_{\text{보고서의 CL}}
=
\overbrace{CL\big|_{CRCL=90}}^{\text{centering value에서의 CL}}
\neq
\underbrace{CL_{\text{normal}}}_{\text{정상 환자 CL (일반적 기대)}}
$$

⚠️ Centering value를 명시 안 하면 reviewer가 $\theta_1$을 "정상 환자 CL"로 잘못 읽음. Centering이 90이고 정상이 120이면, 보고된 $\theta_1$은 이미 신기능이 약간 저하된 환자 기준임.

### 4-3. 결정적 분기점 — 공변량 추가 vs 좌표 재모수화

자, 이제 §1의 PK50 미스터리를 풀 시간임.

| 작업 | 무엇을 하는가 | NONMEM 코드 변화 | $\omega^2$에 일어나는 일 |
|---|---|---|---|
| **공변량 추가** | $\eta$ 안의 설명 가능한 부분을 $\theta$ 구조로 **옮김** | covariate term 추가 | $\omega^2$ 줄어듦 (실제 분산 일부가 $\theta$ 설명분으로 이동) |
| **재모수화** | 같은 데이터를 **다른 좌표**로 다시 표현 | 파라미터 정의 자체 변경 ($CL → CL_u$) | $\omega^2$의 **수치가 달라짐** (실제로 변이가 줄어든 게 아니라 좌표축이 회전한 것) |

PK50에서 일어난 일을 다시 보자 `[G&W p.704–710]`:

$$
\underbrace{CL}_{\text{total}} = \underbrace{f_u}_{\text{비결합분율}} \cdot \underbrace{CL_u}_{\text{unbound}}
$$

| 파라미터 | Total estimate (CV%) | Unbound estimate (CV%) |
|---|---:|---:|
| CL | 11.4 L·h⁻¹ (**28%**) | 720 L·h⁻¹ (**9%**) |
| Cld | 4.35 L·h⁻¹ (39%) | 265 L·h⁻¹ (33%) |
| Vc | 19.9 L (29%) | 1270 L (18%) |
| Vt | 30.9 L (35%) | 2030 L (51%) |

`[G&W p.708, Table 50.1]`

> 🚨 **PK50의 진짜 메시지** — 다시 한 번
> Total 좌표에서 CV 28%, unbound 좌표에서 CV 9%는 **NONMEM이 공변량 모델로 $\omega^2$을 깎은 결과가 아님**. 같은 12명을 다른 좌표에서 봤더니 변이가 다르게 보이는 것뿐임.
>
> Total과 unbound는 **같은 도시를 보는 두 장의 지도**임. 좌표축을 바꾸면 거리가 다르게 보이지만, 도로가 새로 생긴 건 아님.

⚠️ **결정 규칙** `[G&W p.706–709 해석]`:
- $f_u$를 **결정론적 재모수화**로 쓸 거면 → $CL = f_u \cdot CL_u$ 좌표 변환으로 처리
- $f_u$를 **집단 공변량 모델**로 쓸 거면 → $CL_u$에 남길 $\eta$와 $f_u$ 자체의 측정 변이를 분리

둘을 섞으면 ETA가 생리학을 흡수하는 게 아니라 **회계 오차를 흡수**함.

### 4-4. 안전 좌표 — Total vs Unbound가 임상에서 왜 결정적인가

CpD의 안전 경계는 **total C > 50 µg·L⁻¹ 회피**임 `[G&W p.705]`. 즉 safety threshold는 total 좌표에 있음. 그런데 dose individualization은 unbound 기반 안전 여유로 해야 정확함.

$$
\underbrace{C_{total}}_{\text{총 농도, 안전 경계}}
>
\underbrace{50\ \mu\mathrm{g\cdot L^{-1}}}_{\text{회피 임계}}
$$

저알부민혈증 환자에서 $f_u$가 올라가면, total 농도가 안 변해도 unbound 농도(실제 작용 약물)는 올라감 → total 기준으로는 안전해 보이는데 실제로는 독성. 좌표를 잘못 잡으면 환자가 다침. 규제 reviewer가 NDA Section 5.2에서 잡는 deficiency 중 하나가 "safety threshold(total)와 dose recommendation(unbound 기반)이 좌표 면에서 일치하지 않는다"임 `[G&W p.705, p.709]`.

### 4-5. PD 변이는 PK 좌표로 도달 못함

PK50에 한 가지 메시지가 더 있음. CpD에서 비슷한 노출을 받은 환자들 사이에서도 **반응이 8배(0.5–4.0 response units)까지 갈렸음**. 비결합 농도로 다시 표현해도 EC50 변이는 오히려 더 커졌음. 저자들은 $E_{max} < 1$인 무반응자를 **유전적 구성/수용체 밀도**와 연결지음 `[G&W p.707–709]`.

$$
\underbrace{E_{max}}_{\text{최대 반응능}}
<
\underbrace{1}_{\text{완전반응 기준}}
$$

R&T도 같은 말을 함 — 혈장 농도와 반응을 같이 측정해야 PK 변이와 PD 변이를 구분할 수 있음 `[R&T p.363–364]`. 즉:

> 🔑 **PK 좌표의 한계**
> 공변량이 PK 파라미터 변이를 다 설명해도, PD variability는 별도 source로 남음. 단일 공변량으로 모든 변이를 설명하려는 야심은 위험함.

### 4-6. 진단 시그니처 2 — Vanishing Covariate Cascade

> 🔬 **시그니처 2 — `Vanishing Covariate Cascade`**
>
> **어떻게 생겼나**: 진짜 mechanistic covariate(예: 신청소율 약물의 CrCl)가 모델 base에 빠져 있음. $\eta_{CL}$이 그 효과를 흡수해 버림. 그 다음 stepwise selection 돌리면 상관 covariate(체중, BSA)가 가짜로 detect됨. **$\eta_{EBE}$ vs CrCl scatter는 평탄해 보이는데, raw observation의 $CL_{obs}$ vs CrCl scatter는 명확한 기울기**가 나옴.
>
> **왜 생기나**: Stepwise는 $\eta$에 남은 잔여 신호로 covariate를 평가함. $\eta$가 이미 covariate를 흡수해 버린 다음에는 그 covariate가 통계적으로 사라져 보임.
>
> **꿀팁**: $\eta$ 기반 covariate scan과 raw observation 기반 scan을 둘 다 돌려서, 두 결과가 일치하지 않으면 "효과 없음"이 아니라 **"효과 흡수됨"**을 의심.
>
> **실무 처방**: Domain knowledge 기반 candidate covariate(CL을 결정하는 생리학적 변수: CrCl, body size, hepatic function)를 a priori 정의해서 모델 base에 포함시킨 뒤 stepwise를 시작. Stepwise에 모든 판단을 위임하지 말 것.

### 4-7. SCM의 비대칭 임계 — forward와 backward가 다른 α를 쓰는 이유

여기서 학습자가 가장 자주 틀리는 게 SCM(Stepwise Covariate Model) 임계값임. R&T p.373이 말하는 $\Delta OFV \geq 3.84$ (df=1, α=0.05) 한 줄을 SCM 전체에 그대로 쓰면 **통계적으로 잘못된 결정**을 함.

Jonsson-Karlsson SCM (1998)의 설계는 **forward와 backward가 비대칭**임 `[교과서 외 구현/규제 표준; 1차 문헌: Jonsson EN, Karlsson MO. *Pharm Res.* 1998;15(9):1463–1468]`:

| 단계 | 방향 | α (df=1) | 임계 $\Delta OFV$ | 목적 |
|---|---|---|---:|---|
| **Forward Selection** | covariate 추가 | 0.05 | **3.84** | 후보를 관대하게 포함 |
| **Backward Elimination** | covariate 제거 | 0.01 | **6.63** | 엄격한 기준으로 multiple testing 보정 |

$$
\overbrace{\text{Forward}}^{\text{관대}}:\
\underbrace{\Delta OFV}_{\text{OFV 감소}}
\geq
\underbrace{3.84}_{\chi^2_{df=1,\,\alpha=0.05}}
\qquad
\overbrace{\text{Backward}}^{\text{엄격}}:\
\underbrace{\Delta OFV}_{\text{OFV 증가}}
\geq
\underbrace{6.63}_{\chi^2_{df=1,\,\alpha=0.01}}
$$

**왜 비대칭인가**: Forward 단계의 multiple testing이 false positive를 누적시킴. 후보 10개를 α=0.05로 각각 검정하면 family-wise error가 약 40%까지 누적됨.

$$
\underbrace{P_{\text{FWE},\,\text{Forward}}}_{\text{누적 위양성}}
\approx
\overbrace{1-(1-\alpha)^k}^{\text{k개 후보의 가족별 오류}}
\xrightarrow[\alpha=0.05,\,k=10]{}
\underbrace{0.40}_{\approx 40\%}
$$

Backward에서 더 엄격한 α=0.01로 통과해야 살아남도록 설계해서 이 누적 위험을 보정함. 이게 핵심 설계 원리임.

> 💼 **규제 방어 문구**
> *"Covariate selection followed a stepwise approach (Jonsson & Karlsson, 1998): forward inclusion at $\Delta OFV \geq 3.84$ (df=1, α=0.05) and backward elimination at $\Delta OFV \geq 6.63$ (df=1, α=0.01). Final model retention required both thresholds, supplemented by VPC consistency and a priori physiological plausibility."*

⚠️ Forward만 돌리고 backward 생략하면 PopPK 보고서에서 reviewer가 거의 반드시 deficiency를 찾음 — multiple testing 보정 없이 통계적 유의성을 주장한 결과임. **SCM은 양방향이 한 묶음**임.

### 4-8. 다층 범주형 covariate의 df 자동 보정

여기서 또 자주 틀림. **Race(3-level), CYP2D6 phenotype(4-level)** 같은 multi-level categorical에 df=1 임계 3.84를 그대로 쓰면 안 됨. df = K - 1 (K는 level 수)임 `[교과서 외 구현/규제 표준]`:

$$
\underbrace{\mathrm{df}}_{\text{자유도}}
=
\underbrace{K}_{\text{level 수}}
-
\underbrace{1}_{\text{reference level}}
$$

| level 수 K | df | Forward 임계 (α=0.05) | Backward 임계 (α=0.01) |
|---:|---:|---:|---:|
| 2 (binary) | 1 | 3.84 | 6.63 |
| 3 | 2 | **5.99** | **9.21** |
| 4 | 3 | **7.81** | **11.34** |

3-level race에 3.84를 그대로 적용하면 실제 임계보다 관대해져서 false positive가 발생함. Reviewer가 가장 자주 잡는 지점.

**다층 범주형 구현 결정 트리**:

| Cell 크기 | 추천 처리 |
|---|---|
| 모든 cell n ≥ 30 | Multiple THETA full stratification, interaction 평가 가능 |
| 일부 cell n ∈ [5, 30) | Indicator + 곱셈 가정 (main effect만) |
| 일부 cell n < 5 | Hierarchical 또는 인접 level 통합 (예: IM/PM 묶음) |

```nmtran
; [교과서 외 구현; sex × CYP2D6 phenotype 2-way, 곱셈 가정]
IF (SEX.EQ.1.AND.PHEN.EQ.1) CLF = THETA(1)                       ; Male EM (reference)
IF (SEX.EQ.1.AND.PHEN.EQ.2) CLF = THETA(1) * THETA(2)            ; Male IM/PM
IF (SEX.EQ.2.AND.PHEN.EQ.1) CLF = THETA(1) * THETA(3)            ; Female EM
IF (SEX.EQ.2.AND.PHEN.EQ.2) CLF = THETA(1) * THETA(2) * THETA(3) ; Female IM/PM
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

### 4-9. $\Delta OFV$만 본 covariate 채택의 위험

마지막으로, SCM 임계를 통과한 covariate도 **두 번째 관문**을 통과해야 함:

> ⚠️ **흔한 오해 — "$\Delta OFV > 3.84$면 covariate 채택"**
> 이 한 줄이 모델 선택을 끝내는 것처럼 보임. 그런데 잔차 모델이 불안정하거나 phenotype cell이 작으면, covariate가 $\varepsilon$ 변동이나 ETA 흡수를 대신 설명하면서 OFV는 떨어지는데 **VPC는 오히려 악화**됨. 이걸 **OFV-VPC Discordance**라고 부름.
>
> 임상에서는 covariate 극단값에서 노출 예측이 빗나가고, 규제에서는 FDA Deficiency Letter가 날아옴.

**Covariate 채택의 두 관문**:
1. **통계적 관문** — SCM 비대칭 임계 (forward α=0.05, backward α=0.01) + df 자동 보정
2. **Mechanistic 관문** — VPC 일관성 + phenotype cell size + a priori physiology

둘 다 통과해야 covariate가 최종 모델에 들어감.

---

## 5. 강제 순서 3단계 — 남은 $\eta$의 분포 모양 검사

### 5-1. 매끄러운 단봉이라는 가정이 무너지는 순간

§3에서 잔차 잠그고, §4에서 설명 가능한 부분을 $\theta$로 옮겼음. 그러면 남은 $\eta$는 매끄러운 로그정규 단봉형이어야 함 — 그게 이론적 가정임.

그런데 실제로는 그렇지 않을 수 있음. 약리유전학이 보여주는 그림은 다음과 같음 `[R&T p.393–410]`:

> 🎯 **이 단계의 핵심 통찰**
> $\eta$ 분포가 매끄러운 로그정규처럼 보이는 건 우리 가정일 뿐임. 실제로는 PM/IM/EM/UM 같은 **불연속 phenotype subgroup의 혼합**일 수 있음. 평균을 그어버리면 그 평균이 **실제 환자 누구도 대표하지 못하는 계곡 한가운데 값**이 됨.

R&T가 든 결정적 예시 — Isoniazid 483명에게 9.8 mg/kg 경구 투여 후 6시간째 농도가 **두 봉우리로 갈라짐** `[R&T p.402, Figure 13-6]`. NAT2 acetylator status가 분포 모양 자체를 바꿈.

### 5-2. 약물별 유전 다형성 — 외울 게 아니라 패턴을 보는 것임

| 약물 | 분류·기전 | 유전 인자 | 임상 의미 |
|---|---|---|---|
| **Warfarin** | 비타민K 길항 항응고제 | CYP2C9 (PK) + VKORC1 (PD) | 같은 INR을 얻는 용량이 유전형별로 갈라짐 — 단일 유전자만으로 용량 결정 불가 `[R&T p.398, p.406]` |
| **Nortriptyline** | 삼환계 항우울제 | CYP2D6 사본 수 | 기능적 사본 수가 많을수록 CL ↑, 노출 ↓ `[R&T p.397]` |
| **Codeine** | Opioid prodrug | CYP2D6 (morphine 생성) | UM(초고속 대사자)에서 morphine 과량 → 호흡 억제 위험 `[R&T p.399, p.404]` |
| **Thiopurines** (6-MP, azathioprine) | 백혈병·IBD 치료제 | TPMT | TPMT 결핍자에서 표준 용량 시 골수 독성 치명적 `[R&T p.400]` |
| **Isoniazid** | 항결핵제 | NAT2 acetylator | 농도 분포 자체가 이봉형 `[R&T p.402]` |

PM(poor metabolizer) 빈도 — 출처 값 보존 `[R&T p.395]`:
- CYP2D6 PM: 백인 5–10%, 아프리카계 미국인 3.8%, 아시아인 0.9%
- CYP2C9 PM: 백인 1%
- CYP2C19 PM: 백인 3–5%, 아시아인 16%
- TPMT 결핍: 백인 0.3%, 아시아인 0.04%
- NAT2 느린 acetylator: 백인/아프리카계 미국인 60%, 아시아인 10–20%
- UGT1A1 poor metabolizer: 백인 11%, 아시아인 1–3%

> 💡 **PM 빈도표 읽는 법** — 평균 용량 결정용이 아님. **어느 phenotype cell이 작아서 모델 식별성이 흔들리는지를 미리 알려주는 표**임.

⚠️ 인종(ethnicity)은 유전형(genotype)의 **불완전한 proxy**임. 그룹 내 변이가 커서 ethnicity term을 mechanistic genotype처럼 해석하면 안 됨 `[R&T p.395, p.409]`.

### 5-3. 진단 시그니처 3 — Empty Phenotype Cell

> 🔬 **시그니처 3 — `Empty Phenotype Cell`**
>
> **어떻게 생겼나**: Phenotype을 4-level(PM/IM/EM/UM)로 처음부터 펼쳤는데, 희귀 cell(PM n=3)의 THETA factor RSE가 80%를 넘고 `$COV step`이 "covariance matrix is non-positive definite"로 실패함. PM 환자 5명의 ETA(1)이 다 0 근처에 모여 있음.
>
> **왜 생기나**: Cell이 비어 있으면 모델은 그 phenotype 효과를 추정할 정보가 없으니 ETA로 흡수함 → $\omega^2$ 인공적 부풀림 → 변이 보존 법칙.
>
> **결정적 분기**: PM(n=3) 결과를 받았을 때 자문해야 할 질문은 "효과가 있는가?"가 아니라 **"효과를 식별할 정보가 데이터에 있는가?"** 둘은 다른 질문임.
>
> **실무 처방**: §4-8의 cell size 결정 트리에 따라 인접 phenotype을 통합해서 "reduced function" 같은 단일 카테고리로 시작. 4-level full stratification은 데이터가 명확히 허용할 때만 펼침. 작은 cell의 categorical effect를 "null result"로 보고하면 안 됨.

$$
\underbrace{RSE}_{\text{상대 표준오차}}
>
\underbrace{80\%}_{\text{불안정 경고}}
$$

### 5-4. 단봉형 $\eta$ 안에서도 변이가 큰 약물 — CYP3A4

마지막 함정. CYP3A4 같은 효소는 큰 IIV가 있지만 **명확한 유전 인자가 없음** `[R&T p.399, p.410]`. 큰 $\omega^2$가 항상 genotype peak를 뜻하는 게 아님 — 다른 인구학 요인, 동반약물, 복약 순응, 식이 등이 섞여 있을 수 있음.

> 🔑 **이 단계의 마지막 한 줄**
> $\eta$ histogram이 두 봉우리로 보일 때 → genotype/phenotype 영역.
> 단봉이어도 변이가 크면 → 모든 게 유전이라고 단정하지 말고 인구학·순응·병태 요인도 의심.

---

## 6. 세 가지 진단 시그니처를 한 줄로 꿰기 — 같은 법칙의 세 발현

§3, §4, §5에서 봤던 진단 시그니처 1·2·3은 모두 **변이 보존 법칙의 세 변주**임. 한 표로 압축함:

| # | 시그니처 | 어디서 새나 | 어디로 새나 | 잘못된 처치 | 올바른 처치 |
|---|---|---|---|---|---|
| **1** | Leakage Funnel | $\varepsilon$ 모델 (RUV) | $\eta$ (IIV)로 부풀림 | "$\omega^2$ 크네, covariate 찾자" | 잔차 모델 좌표 재선택 (combined·log·exp) |
| **2** | Vanishing Covariate Cascade | 진짜 mechanistic covariate가 base에서 누락 | $\eta$가 그 효과를 흡수 | "효과 없음" 결론 | A priori covariate를 base에 포함 후 stepwise |
| **3** | Empty Phenotype Cell | Phenotype 작은 cell의 정보 부족 | $\theta$ factor가 식별 안 됨 → $\eta$ 흡수 | "유의하지 않음" 결론 | Cell size별 결정 트리, 인접 통합 |

세 시그니처 모두 같은 메커니즘: **분산이 잘못된 그릇으로 흘러감 → 잘못된 결론 → 잘못된 dose**.

> 🎯 **이 세션 전체를 한 표로 회수**
> 변이 보존 법칙이 작동하는 방식은 항상 똑같음. "어느 그릇에 들어갔어야 할 분산이 어디로 새고 있는가?"를 진단할 수 있으면, 세 시그니처는 같은 질문의 세 가지 표현일 뿐임.

---

## 7. $\eta$를 봤다는 착각 — EBE와 Shrinkage

### 7-1. EBE의 정체

여기까지 와서 한 가지 더 짚고 가야 함. NONMEM이 출력하는 **$\eta_{EBE}$**(empirical Bayes estimate)를 "그 사람의 참 $\eta$"로 읽으면 안 됨.

EBE는 모집단 수준 파라미터($\theta$, $\omega^2$, $\sigma^2$)와 그 사람의 관측치를 같이 써서 나온 **사후추정치**임. 모델 가정과 그 사람이 제공한 자료의 양·질이 허용하는 범위 안에서 나온 조건부 추정치임.

### 7-2. Shrinkage — 정보 부족의 정량 측정

자료가 부족하면 EBE가 모집단 평균(0) 쪽으로 끌려감. 이게 **shrinkage**임 `[교과서 외 후속 구현; 1차 문헌: Savic RM, Karlsson MO. *AAPS J.* 2009;11(3):558–569]`:

$$
\underbrace{\eta\text{-shrinkage}}_{\text{EBE 압축률}}
=
1 - \frac{\overbrace{SD(\eta_{EBE,i})}^{\text{EBE 표본 SD}}}{\underbrace{\omega}_{\text{모집단 SD}}}
$$

| Shrinkage | 해석 | EBE 진단 신뢰도 |
|---|---|---|
| < 20% | 자료가 $\eta$를 잘 식별 | 신뢰 가능 |
| 20–30% | 주의 영역 | 해석 조심 |
| **> 30%** | **자료 정보 부족; EBE가 평균으로 압축** | **EBE 기반 plot 신뢰 불가** |

> 🔑 **EBE plot의 정체**
> EBE plot은 현미경이 아니라, **모델·자료·추정법이 함께 만든 그림자**임. Shrinkage > 30%면 $\eta_{EBE}$ vs covariate scatter, $\eta$ histogram, GOF의 individual prediction plot이 모두 분해능을 잃음. 진짜 covariate 신호와 estimation artifact를 구분하기 어려워짐.

### 7-3. 상관된 random effect — OMEGA BLOCK

지금까지 $\eta$를 각 파라미터에 독립으로 부여했음(diagonal $\Omega$). 그런데 실무에서는 **CL과 V의 $\eta$는 거의 항상 상관됨** — 체격이 큰 환자는 CL도 크고 V도 큼.

이걸 무시하고 diagonal로만 가면:
- $\omega^2(CL)$과 $\omega^2(V)$가 **과대 추정** (공유 변이를 두 그릇이 각자 흡수)
- Bayesian TDM posterior가 부정확
- $\eta$-shrinkage 진단 왜곡

`$OMEGA BLOCK(2)`은 off-diagonal 공분산까지 같이 추정함 `[교과서 외 구현/규제 표준]`:

$$
\underbrace{\Omega}_{\text{IIV 분산-공분산}}
=
\begin{pmatrix}
\overbrace{\omega^2_{CL}}^{\text{CL 분산}} & \overbrace{\omega_{CL,V}}^{\text{공분산}} \\
\underbrace{\omega_{CL,V}}_{\text{공분산}} & \underbrace{\omega^2_{V}}_{\text{V 분산}}
\end{pmatrix}
\qquad
\underbrace{\rho_{CL,V}}_{\text{상관계수}}
=
\frac{\omega_{CL,V}}{\omega_{CL}\cdot\omega_{V}}
$$

| $|\rho|$ | 해석 | 조치 |
|---|---|---|
| < 0.3 | 약한 상관 | Diagonal 유지 가능 |
| 0.4–0.7 | 의미 있는 상관 | **BLOCK 구조 정당화** |
| > 0.9 | 거의 완전 상관 | 모델 식별성 재점검 |

```nmtran
$OMEGA BLOCK(2)
 0.09             ; ω²(CL)
 0.04  0.09       ; ω(CL,V), ω²(V)
```

> 💼 **실무 순서**: Diagonal로 시작 → OFV·shrinkage·VPC 안정 확인 → BLOCK으로 확장. 처음부터 BLOCK 잡으면 `$COV step`이 "non-positive definite"로 실패하기 쉬움, 그 자체가 자료 정보량 부족 신호임.

---

## 8. 혼동쌍 정리 — "어느 좌표 문제인가"로 환원

이 세션의 모든 혼동은 단 하나의 질문으로 환원됨: **"지금 보고 있는 변이가 어느 좌표/그릇에 있느냐?"**

### Pair 1. $\omega^2$ (IIV) vs $\sigma^2$ (RUV)

| 기준 | $\omega^2$ / $\eta$ | $\sigma^2$ / $\varepsilon$ |
|---|---|---|
| 위치 | `$OMEGA`, 개인 파라미터 수준 | `$SIGMA`, 관측값 수준 |
| 원인 | 생리학, 유전형, 미포착 covariate | assay 오차, sampling, 모델 misspecification |
| 처치 | covariate 추가 | residual model 재선택 |
| 혼동 시 | covariate 아무리 늘려도 $\sigma^2$ 문제 그대로 | error model 바꿔도 IIV 그대로 |

### Pair 2. Total CL vs Unbound $CL_u$

| 기준 | Total | Unbound |
|---|---|---|
| 좌표 | $CL = f_u \cdot CL_u$의 left side | $CL_u = CL/f_u$의 left side |
| PK50 수치 | CV 28% | CV 9% |
| 안전 경계 위치 | total C > 50 µg·L⁻¹ | unbound 기반 안전 여유 |
| 혼동 시 | 저알부민혈증 환자에서 total 정상인데 unbound 독성 |

### Pair 3. PK 변이 vs PD 변이

| 기준 | PK | PD |
|---|---|---|
| 질문 | 같은 용량에서 **농도가** 왜 다른가 | 같은 농도에서 **반응이** 왜 다른가 |
| 파라미터 | CL, V, F | EC50, Emax, γ |
| 독립성 | PK IIV 작아도 PD variability 클 수 있음 | PK 좌표로 도달 못함 |
| 혼동 시 | 농도만 맞추면 반응도 맞는다고 오판 |

### Pair 4. 평균 분포 vs 분포 모양

| 기준 | 평균 중심 (mean/CV) | 모양 중심 (shape) |
|---|---|---|
| 표현 | $\theta$와 단일 $\omega^2$ | $\eta$ histogram, mixture |
| 놓치는 것 | 다봉형, skewness, subgroup | — |
| 혼동 시 | 이봉형 분포의 계곡 평균을 dose 기준으로 사용 → subgroup 위험 누락 |

### Pair 5. Covariate 추가 vs 좌표 재모수화 (이 세션의 핵심 분기)

| 기준 | Covariate 추가 | Reparameterization |
|---|---|---|
| 무엇을 하나 | $\eta$ 안의 설명분을 $\theta$로 옮김 | 같은 데이터를 다른 좌표에서 다시 표현 |
| NONMEM 코드 | covariate term 추가 | 파라미터 정의 자체 변경 |
| $\omega^2$ 변화 | 실제 분산이 $\theta$로 이동 | 수치가 다르게 나옴 (축이 회전) |
| 예시 | $CL = \theta_1 \cdot (CRCL/90)^{\theta_2}$ | $CL = f_u \cdot CL_u$ |
| 혼동 시 | PK50을 "$\omega^2$ 28% → 9% 감소"로 잘못 해석 |

---

## 9. 자기 테스트 — 10문항

### Q1. $CL_i = CL \cdot \exp(\eta_i)$를 쓰는 가장 직접적인 이유?

**정답**: CL이 음수가 되지 않도록 보장하면서 $\eta$를 정규분포로 둘 수 있음. 지수형은 근사적 일정 CV를 주고 계산상 어려움을 줄임 `[R&T p.371]`.

$$
\underbrace{CL_i}_{\text{개인 CL}}
=
\underbrace{CL}_{\text{모집단 중심}}
\cdot
\underbrace{\exp(\eta_i)}_{\text{양수 배율}}
$$

### Q2. 잔차가 평균 0의 무작위가 아니면?

**정답**: 구조 모델 또는 오차 모델이 중요한 변이의 원인을 아직 설명 못 한 것임. 이 상태에서 covariate를 찾으면 **covariate가 생물학이 아니라 잔차 모델 실패를 설명**하게 됨 `[R&T p.372]`.

### Q3. PK50의 "total CV 28% → unbound CV 9%"를 어떻게 해석?

**정답**: $f_u$를 covariate로 넣어 $\omega^2$을 줄인 게 아님. 같은 12명을 total 좌표와 unbound 좌표로 표현했을 때, 단백 결합 변이가 total parameter variability의 일부를 설명한다는 뜻임. 재모수화이지 covariate 추가가 아님 `[G&W p.706–709]`.

### Q4. $CV(CL)^2 \approx CV(f_u)^2 + CV(CL_u)^2$를 안 쓰는 이유?

**정답**: 이 분산 전파식은 **로그 스케일에서 $f_u$와 $CL_u$가 독립일 때만** 성립하는 일차 근사임. 식 자체가 산술적으로 틀린 게 아니라, **독립성 가정이 임상에서 비현실적**임 — 알부민 변동이 $f_u$와 $CL_u$ 둘 다에 영향. 본 자료는 PK50을 분산 전파가 아니라 좌표 재모수화로 처리함:

$$
\underbrace{CV(CL)^2}_{\text{CL 변이}}
\approx
\underbrace{CV(f_u)^2}_{\text{fu 변이}}
+
\underbrace{CV(CL_u)^2}_{\text{CL_u 변이}}
+
\overbrace{2\rho\cdot CV(f_u)\cdot CV(CL_u)}^{\text{상관 보정항 (종종 ≠ 0)}}
$$

### Q5. PK50에서 unbound 좌표로 봐도 PD 변이가 남는 이유?

**정답**: 단백 결합은 PK 좌표 변이의 일부를 설명함. 반응 변이는 수용체 밀도·유전적 구성 같은 PD 영역에 속함. $E_{max} < 1$ 무반응자는 표적의 완전 발현 결여로 해석됨 `[G&W p.707–709]`.

### Q6. $\eta$-EBE histogram이 두 봉우리로 보이면?

**정답**: 매끄러운 로그정규 IIV가 아니라 **유전형/표현형 subgroup 혼합**을 의심. 단, 희소 표본이면 histogram 자체의 정보량을 먼저 점검 (shrinkage > 30% 여부) `[R&T p.366, p.393–397]`.

### Q7. 인종 covariate를 유전형처럼 해석하면 위험한 이유?

**정답**: 인종은 개인 유전 형질의 **불완전한 proxy**이며 그룹 내 변이도 큼. 탐색적 covariate일 수는 있어도 mechanistic 유전형의 대체물이 아님 `[R&T p.395, p.409]`.

### Q8. 잔차 모델 오지정 vs 공변량 추가 — 무엇을 먼저?

**정답 (표층)**: 잔차 모델 오지정을 먼저 고침. $\varepsilon$ 구조가 틀린 상태에서 covariate를 넣으면 $\omega^2$와 $\sigma^2$ 경쟁이 왜곡되어, **생물학이 아니라 오차 모델 실패를 covariate가 설명**함.

**실무 trade-off**: A(잔차 먼저)가 default이되 무한 재탐색 루프 방지를 위해 잔차 후보 2–3개를 a priori 정의하고 단 한 번의 비교로 결정한 뒤 covariate 탐색으로 넘어감. B(covariate 먼저)를 택한다면 보고서에 **민감도 분석**(다른 잔차 모델에서 covariate 선택 결과가 어떻게 달라지는지) 필수.

**규제 방어 문구**:
- A: *"Residual error model was finalized prior to covariate evaluation based on a priori candidate set {additive, proportional, combined} compared by $\Delta OFV$ and CWRES distribution."*
- B: *"Residual error model misspecification influence on covariate selection was assessed by sensitivity analysis."*

### Q9. SCM forward/backward 임계가 비대칭(α=0.05 vs α=0.01)인 이유?

**정답**: Forward는 다수 후보에 대한 multiple testing을 거치므로 family-wise error가 누적됨 (10 후보 × α=0.05면 약 40%). Backward에서 더 엄격한 α=0.01를 통과해야 살아남도록 설계해서 이 누적 위험을 보정함. Jonsson-Karlsson SCM (1998)의 핵심 설계 원리 `[교과서 외 구현/규제 표준]`.

$$
\underbrace{P_{\text{FWE}}}_{\text{family-wise error}}
\approx
\overbrace{1-(1-\alpha)^k}^{\text{누적 위험}}
$$

### Q10. 3-level race covariate에 $\Delta OFV \geq 3.84$를 그대로 쓰면 왜 잘못?

**정답**: 3-level race는 reference 외 2 indicator를 추가하므로 df = K - 1 = 2임. 임계는 $\chi^2_{df=2,\,\alpha=0.05} = 5.99$ (forward), $\chi^2_{df=2,\,\alpha=0.01} = 9.21$ (backward). df=1의 3.84/6.63을 그대로 쓰면 실제보다 관대해져서 false positive 발생.

$$
\underbrace{\mathrm{df}}_{\text{자유도}}
=
\underbrace{K}_{\text{level 수}}
-
\underbrace{1}_{\text{reference}}
$$

---

## 10. 큰 그림 — 거장의 다섯 질문을 NONMEM 출력으로 번역

### 10-1. 이 세션의 위치

이 세션은 PopPK 커리큘럼의 **분산 축(variance axis)**임. 이전 세션이 CL, V, ka, $t_{1/2}$의 평균을 세웠다면, 이 세션은 그 평균 주변의 개인차와 잔차를 분해함. 이후 FOCE/FOCE-I, GOF, covariate selection, Bayesian TDM은 모두 이 분해 위에서만 의미를 가짐.

### 10-2. 의존성 — 대충 넘기면 어디서 무너지나

| 항목 | 대충 넘기면 |
|---|---|
| §2 그릇 4종 | IOV/TVC 혼동으로 신기능 효과 사라짐 |
| §3 잔차 좌표 | Leakage Funnel → 가짜 IIV → 가짜 covariate |
| §3-4 BQL | M1 + funnel 그대로, $\omega^2$ 15% 부풀음 |
| §4 covariate vs reparam | PK50을 "$\omega^2$ 감소"로 오해 → safety threshold 좌표 불일치 |
| §4-7 SCM 비대칭 임계 | Forward-only 보고로 multiple testing 미보정 → regulatory deficiency |
| §4-8 multi-level df | df=1 그대로 적용 → 통계적 false positive |
| §5 유전 다형성 | 이봉형을 단일 로그정규로 덮음 → subgroup 위험 누락 |
| §7 shrinkage | EBE plot 과해석 → 모델 결함을 생리학으로 잘못 보고 |

### 10-3. 거장의 다섯 질문 — 그리고 그것을 출력 파일에서 읽어내는 능력

초급자는 "IIV가 큽니다"라고 함. 중급자는 "CL에 covariate를 넣겠습니다"라고 함. 전문가는 다음 다섯 질문을 던지고, **각 질문을 NONMEM 출력 한 곳에 1:1로 매핑**함.

| # | 거장의 질문 | NONMEM/진단 출력 시그니처 |
|---|---|---|
| 1 | PK인가 PD인가? `[R&T p.363–364; G&W p.707–709]` | PK·PD 별도 적합 후 $\omega^2$(PK)와 $\omega^2$(PD) 비교. $\eta_{CL}$과 $\eta_{EC50}$ 상관이 낮으면 독립 |
| 2 | $\eta$인가 $\varepsilon$인가? `[R&T p.369–373]` | 잔차 모델 변경 전후 OMEGA 대각·SIGMA 추정값 비교. $\varepsilon$ 모델 변경 시 $\omega^2$(CL)이 크게 움직이면 Leakage Funnel |
| 3 | Total인가 unbound인가? `[G&W p.706–709]` | Total 적합의 $\omega^2$(CL)과 unbound 적합의 $\omega^2$($CL_u$) 나란히 비교. PK50 패턴(28% vs 9%) 재현 여부 |
| 4 | Smooth인가 subgroup 구조인가? `[R&T p.366, p.393–410]` | $\eta$-EBE histogram (xpose4::eta.dist 또는 PsN sse) 이봉형 여부. `$MIX` $\Delta OFV$. 단 shrinkage < 30%, RSE < 80% 선행 점검 |
| 5 | Mechanistic인가 proxy인가? `[G&W p.348–351; R&T p.395]` | Bootstrap/SIR 95% CI. `$COV step` condition number > 1000 (ill-conditioned), covariate 상관 |r| > 0.7 (다중공선성) |

$$
\underbrace{\eta\text{-shrinkage}}_{\text{EBE 분해능}}<\underbrace{30\%}_{\text{경고}},\quad
\underbrace{RSE}_{\text{불확실성}}>\underbrace{80\%}_{\text{불안정}},\quad
\underbrace{\kappa}_{\text{condition number}}>\underbrace{1000}_{\text{조건성}},\quad
\underbrace{|r|}_{\text{상관}} > \underbrace{0.7}_{\text{공선성}}
$$

> 💼 **NDA Section 5.2의 line-item 일관성**
> 규제 reviewer가 감사하는 건 line item 각각이 아니라 **그들 사이의 상호 일관성**임. $\sigma^2$(proportional) CV가 분석법 검증 보고서 CV와 동떨어져 있으면 첫 의문 한 줄이 후속 모든 표로 cascade됨.
>
> 모델 lock 전 cross-check sheet:
> - $\sigma^2$ ↔ bioanalytical CV
> - Safety threshold (total) ↔ dose recommendation (unbound)
> - $\eta$ 분포 모양 ↔ 모집단 약리유전 reference
>
> R&T p.373이 말하는 "regulatory requirement"의 실무 번역이 바로 이거임.

### 10-4. 후속 세션 연결

| 후속 | 이 세션에서 열리는 개념 | 이 세션 없으면 |
|---|---|---|
| FOCE / FOCE-I | $\theta$–$\eta$–$\varepsilon$ 동시 추정, EBE 조건부 해석 | EBE를 참값으로 오해 |
| GOF / CWRES | 잔차 모델 안정화, Leakage Funnel 진단 | covariate 탐색 전 artifact 미제거 |
| $\eta$-EBE / shrinkage | 개체별 정보량과 분산 분해능 | high-shrinkage plot 과해석 |
| Stepwise covariate selection | $\omega^2$ 중 설명 가능한 부분 이동 | OFV fishing, forward-only, df 미보정 |
| Bayesian TDM | 개인 $\eta$ 업데이트, dose individualization | 평균 dose 또는 잘못된 좌표 의존 |

---

## 11. 최종 정리 — 이 세션의 한 문장

Session 13의 최종 메시지는 단 하나임.

> 🎯 **$\omega^2$은 "남은 변이"가 아니라, 아직 이름 붙이지 못한 생리학·유전학·행동·측정 구조의 혼합물임.**

§3이 잔차 noise를 정리하고, §4가 설명 가능한 생리학을 꺼내며, §5가 매끄러운 IIV 안에 숨어 있는 유전적 불연속성을 드러냄. 이 순서를 지키지 않으면 NONMEM은 돌아가지만 용량 개체화는 성립하지 않음.

여기에 v4.2가 추가한 한 줄: **그 분해를 통과한 covariate라도 두 관문을 같이 통과해야 함** — (1) statistical false positive 관문 (SCM 비대칭 임계 + df 자동 보정), (2) mechanistic false positive 관문 (VPC + cell size + a priori physiology).

그리고 이 모든 것을 끌고 가는 마스터 질문 한 줄:

> **"지금 내가 보고 있는 이 흔들림은, 도대체 어느 그릇에 들어가야 하는가?"**

이 질문을 던질 수 있으면, 진단 시그니처 1·2·3은 같은 법칙의 세 변주로 보임. 거장의 다섯 질문은 NONMEM 출력 다섯 위치로 매핑됨. 보고서 line-item은 자동으로 cross-reference됨. NDA reviewer가 잡을 deficiency가 사전에 차단됨.

이 세션이 PopPK 커리큘럼의 분산 축인 이유, 그리고 이 세션을 대충 넘기면 이후 모든 세션이 흔들리는 이유가 여기 있음.

---

C-260518-024715-K4M

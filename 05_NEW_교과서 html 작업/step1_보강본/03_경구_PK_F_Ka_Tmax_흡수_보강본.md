# 03 — 경구(혈관외) PK: F · ka · tmax · 흡수 — v4.0 보강본

## 임상 장면으로 시작합시다 — 같은 숫자, 완전히 다른 결론

R&T 6장에 이런 예가 있어요. 같은 약을 i.m.으로 주면 $F$가 97%, 경구 용액으로 주면 $F$가 46%로 나옵니다 [R&T Table 6-1 / Fig.6-14, pp.183–184]. 이 두 숫자를 보고 "경구는 흡수가 느린 거구나"라고 말하는 순간, **속도(얼마나 빨리, $k_a$)와 양(얼마나 많이, $F$)이 머릿속에서 섞이기 시작합니다.** $F$는 속도가 아니라 도달한 양이거든요.

더 위험한 상황이 하나 더 있어요. 경구만 가지고 있는 데이터에서 $V/F$·$CL/F$·terminal slope를 각각 $V$·$CL$·$k_{el}$처럼 보고하는 경우입니다. 이 한 줄의 보고 문장이 임상 판단과 규제 판단을 통째로 흔들 수 있어요. 오늘 다룰 게 그 한 줄을 어떻게 정직하게 쓰는지입니다.

> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** 경구 PK는 수식 암기가 아닙니다. $C(t)$·$F$·$k_a$·$V/F$·flip-flop을 보면서 **"이 곡선에서 무엇이 진짜 식별됐고, 무엇이 그냥 가정인지"**를 자동으로 의심하는 눈을 만드는 훈련이에요.

---

## 출처 및 범위 노트

> **Source A (G&W):** Gabrielsson & Weiner, *Pharmacokinetic and Pharmacodynamic Data Analysis: Concepts and Applications*, 5th ed., Ch.2 §§2.2.4–2.2.12 (pp.28–47), §2.7.1 (graphical analysis of nonlinear systems, p.40), PK2 (pp.476–482), PK3 (pp.483–486)
> **Source B (R&T):** Rowland & Tozer, *Clinical Pharmacokinetics and Pharmacodynamics: Concepts and Applications*, 5th ed.(현 4판 기반 학습 자료에서는 4판 표시), Ch.6 (pp.169–195), Ch.7 (pp.197–220; context only — BCS §pp.218–220, Table 7-5 p.211, Table 7-8/7-9 pp.219–220), Appendix F (pp.781–784)
> **기호 약속:** $k_a$ = 흡수 속도상수, $k_{el}$ = 소실 속도상수, $V/F$ = 경구 데이터의 겉보기 분포용적, $CL/F$ = 겉보기 경구 청소율.

---

## §0. 큐레이션 지도

### 필수(MUST) — 체화할 5개 카드

| # | 개념 | 핵심 수식 / 출처 |
|---|---|---|
| 1 | **$C(t)$ Master Equation** | G&W Eq.2:32–2:35 [G&W p.30]; R&T Eq.6-3 [R&T p.172] + 적분해 Eq.F-1 [R&T p.782] |
| 2 | **$t_{max}$ / $C_{max}$** | G&W Eq.2:49–2:55 [G&W pp.34–35]; R&T Eq.F-6 [R&T p.783] |
| 3 | **생체이용률 $F$** | G&W Eq.2:71–2:74 [G&W pp.41–42]; R&T Eq.6-9–6-17 [R&T pp.183–186]; 소변 Eq.6-18–6-21 [R&T pp.187–188] |
| 4 | **APEX: $V/F$ + Flip-flop** | $V/F$ [G&W p.32; R&T p.185]; flip-flop [G&W Fig.2.17, p.30; R&T Case C, pp.175–176] |
| 5 | **$k_{a,app}$ vs $k_{a,true}$** | [G&W pp.40–41]; Eq.2:70 [G&W p.41] |

$$
\underbrace{V/F}_{\text{겉보기 V}},\quad \underbrace{CL/F}_{\text{겉보기 CL}},\quad \underbrace{F=\frac{k_{a,true}}{k_{a,true}+k_d}}_{\text{흡수/손실 경쟁}}
$$

### 맥락(CONTEXT) — 본문에 압축

| 항목 | 위치 | 처리 |
|---|---|---|
| Lag time | Card 1, 2 | Eq.2:39–2:42 [G&W pp.32–33]를 1차 흡수식의 시간 이동으로. |
| Method of Residuals | Card 2 | 초기 추정 알고리즘; Appendix F [R&T pp.781–783]. |
| Zero-order input | Card 1, §5 | Eq.2:66–2:67 [G&W p.38], Fig.6-2 [R&T p.171], PK3 [G&W pp.483–486] — "다른 입력 함수"로. |
| 다회투여/축적 | §8 | $R=1/(1-e^{-k_{el}\cdot\tau})$, Eq.2:78 [G&W p.45]는 다음 세션 의존성. |
| 다중 흡수 부위 | Card 5, §8 | Eq.2:80–2:82 [G&W pp.46–47] — 다중 peak / site heterogeneity 경고 한 줄. |
| Saturable absorption | Card 5, §5 | G&W §2.7.1 [G&W p.40] dose-normalized AUC 진단 + R&T Ch.7 transporter [R&T p.203] |
| Saturable first-pass | §8 | R&T Table 7-5 [R&T p.211] — extent의 dose 의존성. |
| BCS / BDDCS | §8 | R&T Table 7-8/7-9 [R&T pp.219–220] — Class I-IV 매트릭스와 biowaiver 결정. |
| Ch.7 흡수 생리학 | §8 | 위배출·초회 통과를 흡수 변동성의 배경으로 [R&T pp.197–220]. |
| Pidgeon-Pitlick / Vaughan, 국소 topical BE / microdialysis | 제외 | 본 세션 범위 밖. |

$$
\underbrace{R}_{\text{축적}}=\frac{1}{\underbrace{1-e^{-k_{el}\cdot\tau}}_{\text{잔존분 보정}}}
$$

---

<!-- SLIDE_START: §1 | title: 세션 헤더 및 로드맵 -->
<!-- SECTION_CORE: SC-01 -->

## §1. 세션 헤더 및 로드맵

**제목:** 경구 및 혈관외 투여의 PK — $F$ · $k_a$ · $t_{max}$ 그리고 흡수 단계가 만드는 모든 것

### 개념 지도 (3 layer)

```text
Layer 1 — 무엇인가
  Oral input | F | ka | tmax | flip-flop | apparent parameter

Layer 2 — 어떻게 계산되는가
  C(t) Master Equation | tmax 식 | F/Frel 식 | AUC = Dose/(CL/F) | ka,app 분해

Layer 3 — 언제, 왜 중요한가
  BE/food effect | V/F·CL/F reporting | terminal slope label | dose interval/accumulation | regulatory caveat
```

### 지식 그래프 위치

```text
[IV bolus 1구획 PK]
  → [이 세션: 경구/혈관외 흡수, F, ka, tmax, V/F, flip-flop]
  → [multiple dosing · modified-release · oral PopPK absorption model · BE/food effect]
```

🧭 **읽는 순서:**
- 카드 1 (M1): 경구 농도곡선은 왜 두 지수함수의 차이로 생기는가?
- 카드 2 (M2): 최고농도 시점은 왜 "흡수 완료"가 아니라 rate balance인가?
- 카드 3 (M3): $F$는 왜 속도가 아니라 전신 도달 정도인가?
- 카드 4 (M4): 경구 단독 데이터는 왜 $V$, $CL$, terminal slope label을 확정하지 못하는가?
- 카드 5 (M5): 적합된 $k_a$는 왜 실제 흡수속도가 아닐 수 있는가?

### 큰 그림

IV bolus는 약이 들어오자마자 전신 순환에 풀려서 **초기 농도 $C_0$**가 그 자리에서 만들어집니다. 경구나 혈관외 경로는 완전히 다르죠. 농도가 0에서 시작해서 천천히 올라가는데, 그게 그냥 "약이 늦게 들어오는" 일이 아니에요. **흡수와 소실이 동시에 일어나면서, 두 지수함수의 차이로 곡선이 만들어집니다.**

이 구조 때문에 $F$와 $V$가 $V/F$로 한 덩어리로 묶이고, $k_a$와 $k_{el}$이 terminal slope에서 자리바꿈할 수 있어요. 같은 dose라도 흡수 단계가 끼어드는 순간 oral 곡선의 peak는 IV bolus보다 낮아지고 시점도 뒤로 밀려요. 흡수는 단순히 "약이 늦게 들어오는 단계"가 아니에요 — **peak의 높이와 시점을 둘 다 다시 정하는 단계입니다** [R&T Fig.6-3, p.172].

### 한 줄 항법도

```
C(t) Master Equation
  → tmax/Cmax: 흡수속도 = 소실속도
  → F: 흡수 extent는 AUC로 본다
  → V/F + flip-flop: 경구 단독 데이터의 식별 한계
  → ka,app vs ka,true: 적합된 ka가 흡수인가 장관 손실인가
```

📍 **선행·후속**
- **선행**: IV bolus 1구획 PK($CL$, $V$, $t_{1/2}$, $AUC$), 1차 ODE, 지수함수, AUC 사다리꼴법.
- **직후**: multiple dosing, accumulation, two-compartment oral, transit/Erlang/Weibull input, modified-release, BE.
- **실무 연결**: NONMEM ADVAN2/ADVAN4, oral PopPK reporting, food effect, formulation effect, flip-flop 검증.

**§1 요약:** 수식 암기가 아닙니다. oral curve에서 "무엇이 실제로 식별되는가"를 자동으로 의심하는 눈을 만드는 게 이 세션의 목표예요.

---

<!-- SLIDE_START: §2 | title: 개념 해부 카드 -->
<!-- SECTION_CORE: SC-02 -->

## §2. 개념 해부 카드

> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** $C(t)$ Master Equation은 장관 입력과 중심 소실, 이 두 개의 직렬 ODE가 만드는 차이지수 곡선이에요. 여기서부터 $F$·$V$·$k_a$·$k_{el}$의 이름표를 **따로따로** 떼어 놓아야 뒤가 안 꼬입니다.

---

<!-- SLIDE_START: M1 | title: C(t) Master Equation -->
<!-- SECTION_CORE: SC-03 -->

### Card 1. $C(t)$ Master Equation — 경구 PK가 시작되는 한 줄

> **앞 카드에서 이 카드로**
> IV bolus에서는 $C_0$가 즉시 만들어졌어요. 경구에서는 농도가 0에서 시작해 흡수와 소실이 경쟁하며 곡선이 만들어집니다 — 그 곡선의 정체부터 풀어봅시다.

> **거장의 시각**
> 경구 1구획 모델을 단일 곡선 하나로만 보면 상승부와 하강부의 이름표를 잘못 붙이기 쉬워요. $C(t)$를 **장관 입력과 중심 소실이 직렬로 만든, 두 지수함수의 차이 신호**로 봐야 합니다. 상승부는 아직 흡수가 남아 있다는 신호고, 하강부가 항상 소실만의 신호인 건 아니에요. 분모의 $k_a-k_{el}$도 그냥 분모가 아니에요 — **두 과정이 시간축에서 얼마나 떨어져 보이는지를 정하는 항**입니다. $k_a \approx k_{el}$이면 두 과정이 거의 분리가 안 돼서 한계식으로 수렴하고, $k_a<k_{el}$이면 혈장에 들어온 약은 빠르게 사라지지만 관찰되는 terminal decline은 남은 흡수 때문에 천천히 보일 수 있어요.

#### A. 형식적 정의 + 핵심 수식

가정은 1구획·1차 흡수·1차 소실·선형 PK(← dose 비례성 유지)입니다 [G&W p.30; R&T pp.171–172].

흡수 부위:

$$
\underbrace{\frac{dA_g}{dt}}_{\text{장관 변화}} = -\underbrace{k_a}_{\text{장관 소실}}\underbrace{A_g}_{\text{장관 잔량}}
$$

혈장/중심 구획:

$$
\underbrace{\frac{dC}{dt}}_{\text{농도 변화}} = \underbrace{\frac{k_a F D_{po} e^{-k_a t}}{V}}_{\text{전신 입력}} - \underbrace{k_{el} C}_{\text{중심 소실}}
$$

`[Source: G&W Eq.2:32–2:34, p.30; R&T Eq.6-2–6-3, pp.171–172]`

이걸 풀면:

$$
\underbrace{C(t)}_{\text{혈장 농도}}=\frac{\overbrace{k_a F D_{po}}^{\text{전신 입력}}}{\underbrace{V(k_a-k_{el})}_{\text{희석·분리}}}\left(\underbrace{e^{-k_{el}t}}_{\text{소실 지수}}-\underbrace{e^{-k_a t}}_{\text{흡수 지수}}\right)
$$

`[Source: G&W Eq.2:35, p.30; R&T Appendix F Eq.F-1, p.782]`

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $F$ | fraction | 전신 순환 도달 분율 | 제형, food effect, first-pass |
| $D_{po}$ | amount | 경구 투여량 | 용량군, 복약 순응도 |
| $V$ | volume | 농도 희석 공간 | 체성분, 조직분포, 단백결합 |
| $k_a$ | time$^{-1}$ | 장관/흡수부위 소실 속도 | 용출, 위배출, 장관 손실 |
| $k_{el}$ | time$^{-1}$ | 중심구획 소실 속도 | $CL/V$, 신장·간 기능 |

> 💡 두 모래시계가 겹쳐 있다고 보시면 돼요. 장관에서 빠지는 모래시계가 $k_a$, 중심구획에서 사라지는 모래시계가 $k_{el}$. 우리가 관찰하는 농도는 두 흐름의 **차이**예요. 그래서 하강부가 보인다고 무조건 elimination phase가 아닙니다 — $k_a<k_{el}$이면 terminal slope는 **흡수가 정하는 감소(absorption-limited decline)**일 수 있어요.

#### C. Lag-time(← 흡수 시작 전 지연시간)

투여 시각이 아니라 실제 흡수가 시작된 이후의 시간만 식에 들어갑니다.

$$
C(t)=0 \quad (t<t_{lag})
$$

$$
\underbrace{C(t)}_{\text{지연 후 농도}}=\frac{\overbrace{k_a F D_{po}}^{\text{입력 크기}}}{\underbrace{V(k_a-k_{el})}_{\text{희석·분리}}}\left(\underbrace{e^{-k_{el}(t-t_{lag})}}_{\text{소실 지수}}-\underbrace{e^{-k_a(t-t_{lag})}}_{\text{흡수 지수}}\right)\quad (\underbrace{t\ge t_{lag}}_{\text{흡수 후}})
$$

`[Source: G&W Eq.2:39–2:42, pp.32–33]`

#### D. 0차 입력 — 다른 입력 함수

0차 흡수는 중심 소실은 그대로 두고 입력 함수만 바꾼 경우예요. 흡수 중에는 입력이 거의 일정하다가, 흡수가 끝나면 washout만 남습니다 [G&W Eq.2:66–2:67, p.38; R&T Fig.6-2, p.171]. G&W의 PK3 사례에서는 zero-order model의 AIC가 first-order보다 좋게 나왔는데, 여기서 조심해야 할 점이 있어요. **AIC가 더 좋다고 해서 "이건 진짜 0차 흡수다"가 증명되는 건 아닙니다** — 진짜 기전을 확정하려면 여러 dose, 반복투여, IV 비교 같은 추가 근거가 필요해요 [G&W pp.483–486].

> 💼 **실무 인사이트:** NONMEM ADVAN2 oral model에서 KA의 initial은 큰 값과 작은 값을 둘 다 시도해봐야 해요. 서로 다른 initial이 다른 해로 가거나 비슷한 OFV로 수렴하면 flip-flop 또는 practical identifiability 문제를 의심합니다.

**Card 1 요약:** Oral $C(t)$는 "흡수 지수 − 소실 지수". $F$와 $V$는 진폭을 정하고, $k_a$와 $k_{el}$은 곡선 모양과 terminal slope 해석을 지배합니다.

여기서 꼭 잡고 가야 할 게 셋이에요. 첫째, 경구 농도곡선이 늦게 올라오는 이유는 $k_a$와 $k_{el}$의 **차이지수 구조**가 만드는 거예요. 둘째, "하강부 = elimination"이라는 단정은 위험합니다 — flip-flop이면 흡수가 terminal slope를 지배해요. 셋째, "좋은 fit = 진짜 생리학"으로 받아들이면 안 됩니다 — apparent fit을 true mechanism으로 오독하면 초기값 설정도 보고서 문장도 같이 무너집니다.

---

<!-- SLIDE_START: M2 | title: tmax/Cmax -->
<!-- SECTION_CORE: SC-04 -->

### Card 2. $t_{max}$ / $C_{max}$ — 흡수속도와 소실속도가 같아지는 순간

> **앞 카드에서 이 카드로**
> 차이지수 곡선의 구조를 봤어요. 다음은 그 곡선의 기울기가 언제 0이 되는가입니다.

> **거장의 시각**
> $t_{max}$를 "흡수가 가장 많이 끝난 시간"으로 읽으면 rate와 amount가 섞입니다. **$dC/dt=0$**의 관점으로 보면 $F$나 dose나 $V$가 아니라 **$k_a/k_{el}$의 상대 위치**가 peak 시간을 정한다는 게 즉시 보여요. $t_{max}$는 가장 많이 흡수된 시간이 아니라 **순유입이 0이 되는 시간** — 흡수 속도와 소실 속도가 같아지는 순간입니다 [R&T p.173; G&W pp.34–35].

#### A. 도출

Master equation을 미분해서 $dC/dt=0$으로 두면:

$$
\underbrace{\frac{dC}{dt}}_{\text{농도 기울기}}=\frac{\overbrace{k_a F D_{po}}^{\text{scale}}}{\underbrace{V(k_a-k_{el})}_{\text{scale}}}\left(\overbrace{-\underbrace{k_{el}e^{-k_{el}t}}_{\text{소실 기여}}+\underbrace{k_a e^{-k_a t}}_{\text{흡수 기여}}}^{\text{속도 균형}}\right)=\underbrace{0}_{\text{peak 조건}}
$$

$$
\underbrace{t_{max}}_{\text{peak 시간}}=\frac{\underbrace{\ln(k_a/k_{el})}_{\text{속도 로그비}}}{\underbrace{k_a-k_{el}}_{\text{속도 차}}}
$$

`[Source: G&W Eq.2:49–2:52, pp.34–35; R&T Eq.F-6, p.783]`

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $t_{max}$ | time | 최고농도 도달 시각 | $k_a/k_{el}$ balance |
| $k_a$ | time$^{-1}$ | 흡수부위 소실 속도 | 용출, 위배출, 제형 |
| $k_{el}$ | time$^{-1}$ | 중심구획 소실 속도 | $CL/V$, 장기 기능 |

> 🔑 $t_{max}$는 저수지 수위가 가장 높은 순간이에요. 수도꼭지로 들어오는 속도와 배수구로 빠지는 속도가 같아지는 시점이지, **물이 다 들어온 시점이 아니에요.** linear 1구획에서는 $F$와 dose가 높이를 바꾸지만 $t_{max}$ 위치는 바꾸지 않습니다.

$k_a \gg k_{el}$일 때:

$$
\underbrace{C_{max}}_{\text{최고농도}}\approx \underbrace{\frac{F D_{po}}{V}}_{\text{도달량/부피}}\underbrace{e^{-k_{el}t_{max}}}_{\text{peak 전 소실}}
$$

`[Source: G&W Eq.2:53, p.35]`

Lag-time이 있으면 관찰되는 $t_{max}$는 $t_{lag}$만큼 뒤로 이동합니다 [G&W Eq.2:54–2:55, p.35].

#### B. 왜 $F$와 $V$가 $t_{max}$ 식에서 사라지는가

$F$, dose, $V$는 곡선의 높이를 위아래로 scale만 할 뿐, 기울기가 0이 되는 시간 위치는 안 바꿉니다. 그래서 linear 1구획에서 dose나 $F$가 바뀌면 $C_{max}$와 $AUC$는 바뀌지만 $t_{max}$는 그대로예요 [R&T Fig.6-5, p.174].

**근데 이건 absorption 단계만 건드렸을 때의 이야기예요.** $CL$이 변하면 $AUC$뿐 아니라 $t_{max}$와 $C_{max}$가 같이 움직이고, $V$가 변하면 $C_{max}$와 $t_{max}$가 서로 다른 방향으로 이동합니다. 그래서 "$F\cdot dose$만 변했을 때"의 곡선 변화 패턴과 "disposition($CL/V$)이 변했을 때"의 곡선 변화 패턴이 다르다는 점 — 이게 흡수 변화와 disposition 변화를 가르는 첫 단서예요 [R&T Figs.6-10–6-11, pp.179–180].

#### C. 잔차법(Method of Residuals)

말기 직선 구간에서 $k_{el}$을 먼저 추정한 다음, 그 직선을 역으로 외삽해서 관찰 농도를 빼면 잔차 직선이 나와요. 그 직선의 기울기가 $-k_a$입니다. 두 직선의 교점은 lag-time 추정에 씁니다 [G&W pp.31–33; R&T Appendix F pp.781–783]. 단, 이 방법은 **terminal slope가 정말 elimination을 반영한다는 전제** 위에 있어요 — flip-flop 상황에서는 이 전제가 깨져서 위험합니다.

> 💼 **실무 인사이트:** 잔차법에서 terminal point 선택은 눈대중이 아니에요. 최소 3점 이상의 terminal points, log-linear fit이 충분히 좋게 떨어져야 하고, $C_{max}$ 이후 충분히 늦은 시점이어야 합니다. 안 그러면 $k_a$와 $k_{el}$ 초기값이 서로 오염돼요.

#### D. 극한: $k_a=k_{el}$

$$
\underbrace{C(t)}_{\text{한계 농도}}=\underbrace{\frac{k' F D_{po}}{V}}_{\text{입력 scale}}\underbrace{t}_{\text{시간항}}\underbrace{e^{-k't}}_{\text{공통 감쇠}}
$$

`[Source: G&W Eq.2:58, p.37]`

**Card 2 요약:** $t_{max}$는 rate balance의 시점이에요. linear 조건에서는 $F$, dose, $V$가 아니라 $k_a$와 $k_{el}$의 상대 크기가 정합니다.

핵심 세 가지를 정리하면, peak가 언제 생기는지는 rate balance가 정해줍니다. AUC·$C_{max}$ 같은 scale 변화와 peak 시간 변화를 혼동하면 안 돼요 — $F$나 dose는 높이만 바꾸지만, disposition이 변하면 시간 위치까지 흔들립니다. 그리고 "$t_{max}$ = 흡수 완료 시점"이라는 단정 — 이게 가장 흔한 오해입니다. 흡수는 $t_{max}$ 이후에도 계속돼요. 단지 소실이 더 빨라서 농도가 내려갈 뿐이에요.

---

<!-- SLIDE_START: M3 | title: 생체이용률 F -->
<!-- SECTION_CORE: SC-05 -->

### Card 3. 생체이용률 $F$ — 흡수의 "양"을 $AUC$로 읽습니다

> **앞 카드에서 이 카드로**
> rate balance 얘기가 끝났으니, 이제 전체 노출량을 묻습니다 — 전신 순환에 누적으로 얼마나 도달했는가.

> **거장의 시각**
> $k_a$는 "얼마나 빨리", $F$는 "얼마나 많이 전신 순환에 도달했는가"예요. 두 개념을 섞으면 food effect·BE·formulation effect 해석이 흐려집니다. **$F$를 'AUC가 읽는 extent'로 박아 놓으면** rate($k_a$)와 extent($F$)가 완전히 분리됩니다.

#### A. 절대 생체이용률

IV 기준 투여가 있을 때 $F$(← 전신 순환 도달 분율)는:

$$
\underbrace{F}_{\text{절대 F}}=\underbrace{\frac{AUC_{po}}{AUC_{iv}}}_{\text{노출 비율}}\cdot\underbrace{\frac{D_{iv}}{D_{po}}}_{\text{용량 보정}}
$$

`[Source: G&W Eq.2:74, p.42; R&T Eq.6-11, p.183]`

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $F$ | fraction | IV 대비 전신 도달 분율 | 흡수 분율, 장관·간 first-pass |
| $AUC_{po}$ | conc·time | 경구 투여 후 총 노출 | $F$, dose, $CL$ |
| $AUC_{iv}$ | conc·time | IV 기준 총 노출 | dose, $CL$ |
| $D_{iv}/D_{po}$ | ratio | route 간 용량 보정 | 시험 설계 |

> 🔑 $F$는 "얼마나 빨리"가 아니라 **"얼마나 많이 도달했는가"**. $AUC$가 감소했다고 곧바로 $k_a$ 감소로 읽으면 rate와 extent를 섞게 됩니다.

전제는 두 투여 사이에 clearance가 같다는 점이에요 [R&T p.183]. R&T 예시는 i.m. dose의 $F$를 97%, oral solution의 $F$를 46%로 계산해서 route별로 extent 차이가 얼마나 나는지를 보여줍니다 [R&T Table 6-1 / Fig.6-14, pp.183–184].

#### B. 상대 생체이용률

두 혈관외 제형 A·B를 비교할 때:

$$
\underbrace{F_{rel}}_{\text{상대 F}}=\underbrace{\frac{AUC_B}{AUC_A}}_{\text{B/A 노출}}\cdot\underbrace{\frac{D_A}{D_B}}_{\text{용량 보정}}
$$

`[Source: R&T Eq.6-15, p.185]`

IV 기준 투여 없이도 두 제품의 전신 전달 차이를 비교할 수 있어요 [R&T pp.183–185].

#### C. 소변 데이터 — 주의점

요중 배설 데이터로도 $F$, $F_{rel}$, 신장 청소율을 추정할 수 있습니다. 단 **미변화체 배설 분율과 신장 처리가 비교 조건에서 일정**해야 해요 [R&T Eq.6-18–6-21, pp.187–188].

#### D. 기전적 $F$

$$
\underbrace{F}_{\text{전체 F}}\approx\underbrace{F_F}_{\text{흡수·제형}}\cdot\underbrace{F_G}_{\text{장관 생존}}\cdot\underbrace{F_H}_{\text{간 생존}}
$$

`[Source: R&T Ch.7 context, pp.197–220]`

$F$는 그냥 "용해되어 들어온 양"이 아니라 **장관 → 장벽 → 간을 차례로 통과한 결과**라는 걸 기억하는 용도로 둡니다.

#### E. 생동성(BE) 맥락

R&T는 시험/기준 ratio의 90% CI와 0.80–1.25 기준을 설명합니다 [R&T Fig.6-13, p.183]. 핵심 질문은 이거예요 — **"$F_{rel}$만 같으면 충분한가?"** $F_{rel}$이 같아서 $AUC$가 비슷하더라도, $k_a$가 다르면 $C_{max}$·$t_{max}$가 달라집니다. extent와 rate는 항상 같이 봐야 해요.

**Card 3 요약:** $F$는 extent, $k_a$는 rate. $AUC$는 $F\cdot \mathrm{Dose}/CL$이지만, 경구 단독에서는 $CL$이 아니라 $CL/F$가 추정됩니다.

세 줄로 정리하면, "얼마나 많이 도달했는가"는 $F$와 $AUC$가 답합니다. "얼마나 빨리 peak에 도달했는가"는 $k_a$와 input function이 답해요. 그리고 "$AUC$ 변화 = 흡수속도 변화"라는 단정 — 이게 가장 위험한 혼동이에요. extent와 rate를 섞는 순간 food/formulation effect 보고서 문장이 실패합니다.

---

<!-- SLIDE_START: M4 | title: APEX V/F 식별불가능성 + Flip-flop -->
<!-- SECTION_CORE: SC-06 -->

### Card 4. APEX — $V/F$를 따로 못 푸는 문제 + Flip-flop 동정

> **앞 카드에서 이 카드로**
> $F$가 extent라는 걸 잡으면, 경구 단독 데이터에서 $F$와 $V$, $F$와 $CL$이 왜 묶여 보이는지가 이번 카드의 핵심 문제가 됩니다.

> **거장의 시각 (Apex)**
> OFV가 좋게 나오고 RSE가 작으면 oral-only 모델에서도 $V$·$CL$·$k_{el}$이 다 잡혔다고 많이들 생각하는데, 사실은 그렇지 않아요. 경구 곡선은 **입력 함수($k_a$·lag·gastric emptying·multiple sites), $F$, disposition($CL$·$V$) — 이 세 가지가 합쳐져서 만들어진 결과**입니다. 같은 곡선이 서로 다른 조합으로 나올 수 있어요. 그래서 oral-only 모델 결과는 항상 $V/F$, $CL/F$, terminal slope ambiguity를 남기는 **'apparent parameter 보고서'**라는 걸 잊으면 안 됩니다.

`[⚡ Apex Concept]`

좀 더 정확히 말씀드리면, 경구 농도-시간 곡선은 입력 함수($k_a$·lag·gastric emptying·multiple sites)와 $F$와 disposition($CL$·$V$)의 **합성곱**이에요. 어느 한 축만 보고는 곡선 형태가 결정되지 않고, 같은 곡선이 서로 다른 조합으로 만들어질 수 있다는 뜻이죠. 이게 $V/F$로 묶이는 이유, terminal slope label이 뒤집힐 수 있는 이유, fitted $k_a$가 실제 흡수가 아닐 수 있는 이유 — 이 세 가지를 **한꺼번에** 설명해줍니다.

여기서 한 가지 중요한 구분이 있어요. 좋은 OFV·작은 RSE는 "이 모델이 이 데이터를 잘 설명한다"는 뜻일 뿐이에요. "$V$와 $F$가 원리적으로 따로 추정 가능하다"는 뜻이 아닙니다. **수치적 식별가능성과 구조적 식별가능성(structural identifiability, ← 원리적으로 두 파라미터를 따로 추정할 수 있는가)은 완전히 다른 문제예요.**

#### A. $V/F$ 구조적 식별가능성

Master equation을 다시 보면, $F$와 $V$는 항상 $F/V$ 형태로 같이 등장합니다.

위 식(앞에서 본 경구 $C(t)$)에서 $F/V$가 한 묶음으로만 나타나기 때문에, **경구 단독으로는 $V/F$만 추정**할 수 있고 clearance도 $CL/F$로 보고해야 합니다 [G&W p.32; R&T p.185].

$$
\underbrace{AUC}_{\text{전신 노출}}=\underbrace{\frac{F\cdot Dose}{CL}}_{\text{도달량/CL}}=\underbrace{\frac{Dose}{CL/F}}_{\text{경구 관찰형}}
$$

$\mathrm{Dose}/(CL/F)$와 $F\cdot \mathrm{Dose}/CL$은 대수적으로 같은 식이지만, **$AUC$만 봐서는 변화의 원인이 $F$인지 $CL$인지 가를 수 없습니다.**

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $V/F$ | volume | apparent volume | $V$ 변화 또는 $F$ 변화 |
| $CL/F$ | volume/time | apparent clearance | $CL$ 변화 또는 $F$ 변화 |
| terminal slope | time$^{-1}$ | 관찰 말기 감소율 | $k_{el}$ 또는 $k_a$ 병목 |
| $AUC$ | conc·time | 총 전신 노출 | $F\cdot Dose/CL$ |

> 💡 안개 낀 유리창 너머로 방의 크기와 창문이 얼마나 열려있는지를 동시에 추정해야 하는 상황이에요. 방이 큰 건지($V$가 큰지) 창문이 덜 열린 건지($F$가 작은지) — 같은 농도 하나로는 가를 수 없어요. **$V/F=50\ \mathrm{L}$라는 숫자는 절대 "$V=50\ \mathrm{L}$"라는 뜻이 아닙니다.** IV나 absolute $F$ 근거가 없으면 $V/F$, $CL/F$로 보고하는 게 맞아요.

**저자의 4-part 결론 [R&T p.185]:** 단일 oral dose만 있을 때 — **(i)** $AUC$는 사다리꼴법으로 *계산 가능*. **(ii)** $CL$은 $F$를 모르므로 *계산 불가*. **(iii)** terminal half-life는 무엇이 rate-limiting인지 모르면 elimination/absorption 어느 쪽에도 *confidently 할당 불가*. **(iv)** $V$는 *추정 불가*. 이 네 줄이 Apex의 핵심 메시지입니다.

#### B. Flip-flop 실용적 식별가능성

일반적으로 $k_a>k_{el}$이면 경구 말기 기울기는 소실을 반영해요. 그런데 $k_a<k_{el}$이면 **남은 흡수 과정이 더 느린 과정**이 되니까, 관찰되는 말기 기울기는 흡수를 반영할 수 있습니다 [G&W Fig.2.17, p.30; R&T Case C, pp.175–176].

**핵심 경고:** "상승부 = 흡수, 하강부 = 소실"이라는 라벨은 flip-flop에서는 통째로 뒤집어집니다 [G&W pp.29–30; R&T pp.173–176].

#### C. 사례 앵커

- **Fluticasone propionate**(흡입 코르티코스테로이드): median $t_{max}$ 90분, $C_{max}$ 30–90분, 그런데 흡수 반감기는 3.8–4시간. → 그래서 **빠른 $t_{max}$가 빠른 흡수를 증명하지 않는다**는 사실의 사례입니다 [R&T Fig.6-7, p.177].
- **Theophylline**(저추출 기관지확장제): 음식이나 물 같은 흡수 조건을 바꿔도 말기 반감기는 약 6.3 h로 유지됩니다. → 그래서 **흡수 변화와 disposition 변화는 다르게 보인다**는 사실을 가르는 사례입니다 [R&T Fig.6-8, p.178].
- **Penicillin G**(난용성 근육주사 항생제): 난용성 제형은 흡수가 rate-limiting이 될 수 있어요. → 그래서 **flip-flop이 일어나는 전형적인 상황**의 사례입니다 [R&T Fig.6-9, p.178].
- **PK2:** lag-time model에서 $K_a=0.043\ \mathrm{min}^{-1}$, $K=0.0088\ \mathrm{min}^{-1}$, $V/F=32\ \mathrm{L}$, $t_{lag}=16\ \mathrm{min}$ [G&W p.480]. 같은 사례에서 $F=82\%$와 $true\ V=20\ \mathrm{L}$도 함께 제시되는데, 산술로 보면 $32\times0.82\approx26\ \mathrm{L}$이 나와서 원문 20 L와 맞지 않아요. 본 handout은 이 충돌을 "원문 수치 충돌 [확인 필요]"로 표시해 두고 어느 쪽도 확정값으로 쓰지 않습니다 [G&W p.480].

> 🔎 **충돌의 가능한 출처 가설 (보강):** 원문을 다시 정독하면 PK2의 V/F 추정은 **solution II에서 나온 회귀값**과 **deconvolution으로 구한 F=82%**의 곱으로 V≈20 L가 보고됩니다 [G&W p.480]. 동일 사례에서 NCA 기반 F는 ~64%로도 제시되어 있어요 [G&W p.480]. 이 충돌의 가능한 출처는 세 가지로 추정됩니다 — **(i)** solution II의 V/F가 정확히 32 L가 아니라 25 L 영역일 가능성(원문 본문에는 V/F = 30 L가 *initial estimate*, solution III에서는 V/F = 6.54 L도 등장 — 즉 동일 PK2가 여러 solution path별로 다른 V/F를 갖는다 [G&W pp.481–482]), **(ii)** F가 deconvolved 82%인지 NCA 60–64%인지에 따라 V 환산값이 24~26 L vs 19~20 L로 갈림, **(iii)** 원문이 V≈20 L로 반올림 보고. 학습자가 모델링 보고서를 검토할 때 이런 **"같은 사례 내 다른 추정 경로"가 만드는 V·F·CL 환산 충돌**을 진단하는 훈련용 사례로 보시면 됩니다.

- **PK2 Solution III:** 역전된 초기 추정치가 다른 $k_a/k_{el}/V/F$ 해로 수렴할 수 있다는 점을 보여주는 사례 [G&W pp.481–482]. → flip-flop의 살아있는 증거예요.
- **PK3:** 1차 모델에서는 $K_a\approx K_e$로 나오고 큰 CV/RSE가 함께 옵니다. 0차 모델은 AIC가 더 낮게 나와요(85.2 → 76.2). 하지만 **더 좋은 적합이 진짜 0차 흡수의 증명은 아닙니다** [G&W Table 3.1, p.486].

#### C-2. 그럴듯한 오류

$C_{max}$가 내려가고 $T_{max}$가 늘어났으니까 흡수가 느려진 거라고 많이들 단정해요. 맞는 얘기 같은데, 사실은 그렇지 않을 수 있는 경우가 많습니다. 그 단정으로 가면 $k_a$ 감소 해석을 따라서 제형을 다시 만들거나 absorption model을 transit compartment로 복잡화하게 되죠. 그런데 만약 진짜 원인이 first-pass 증가나 용해도 저하, 아니면 flip-flop이면 어떻게 될까요? 임상에서는 노출·독성·치료실패 예측이 통째로 어긋나고, 모델링·규제 쪽에서는 IV나 route comparison 없이 $F$와 $k_a$를 분리했다고 주장한 게 BE 의사결정을 잘못 만들어내서 재분석을 요구받을 위험이 생깁니다.

#### D. NONMEM 보고

경구 단독 PopPK에서는 $F$를 1로 고정하고 $V/F$, $CL/F$로 보고하는 게 구조적으로 정직한 방법이에요. `F1`을 추정하거나 임의 값으로 고정한 다음에 $V$·$CL$을 absolute 값처럼 보고하면 **사전 가정이 추정된 파라미터처럼 보이는 위험**이 생깁니다.

> 💼 **실무 인사이트 — 세 가지 함정:**
> ① **쌍둥이 억제(Twin Suppression):** $k_a$·$k_{el}$의 두 해가 모두 그럴듯해 보일 때 ETA(KA)와 ETA(KEL)가 서로 강하게 보상하면서 OFV가 안정되어 보입니다.
> ② **$V/F$ 드리프트:** 같은 covariate가 $V/F$와 $CL/F$에 비례적으로 들어가면 $F$-driven 변화를 의심해야 해요. 진짜 분포·청소율 변화가 아닐 수 있습니다.
> ③ **가상 분포용적(Phantom Volume):** $V/F$ 변화를 $V$ 변화로 그냥 보고하는 경우. 핵심 식을 기억합시다 — $AUC=F\cdot \mathrm{Dose}/CL=\mathrm{Dose}/(CL/F)$.

**Card 4 요약:** 경구 단독은 $V$와 $F$를 못 가립니다. flip-flop에서는 terminal slope도 $k_{el}$로 확정되지 않아요. 좋은 fit은 진짜 parameter의 증거가 아닙니다.

이 카드의 핵심을 다시 강조하면 — oral-only에서는 보고할 게 정해져 있어요. $V/F$, $CL/F$, 그리고 terminal slope ambiguity. 이 세 가지를 명시하는 게 정직한 보고예요. 작은 RSE와 좋은 OFV는 numerical precision이지 structural identifiability가 해결됐다는 뜻이 아닙니다. 그리고 가장 위험한 한 줄 — "$V/F$를 $V$로 보고"하는 순간 phantom volume interpretation이 생기고, 임상 쪽에서는 용량·축적 판단 오류로, 규제 쪽에서는 재분석 요구로 돌아옵니다.

---

<!-- SLIDE_START: M5 | title: ka_app vs ka_true -->
<!-- SECTION_CORE: SC-07 -->

### Card 5. $k_{a,app}$ vs $k_{a,true}$ — $k_a$가 실제로 측정하는 것은 무엇인가

> **앞 카드에서 이 카드로**
> $V/F$와 terminal slope가 apparent label이라면, $k_a$ 역시 실제 흡수속도인지 먼저 의심해야 합니다.

> **거장의 시각**
> fitted $k_a$를 그대로 true absorption으로 부르면 장관 손실·분해·site heterogeneity를 모두 흡수속도 변화로 오해하게 돼요. **gut compartment에서 "사라진 속도"와 systemic circulation에 "도달한 속도"를 따로 떼어 놓으면** food effect·formulation effect 해석이 안전해집니다. 모델 output의 $k_a$는 겉보기 parameter일 수 있다는 걸 항상 의심하세요.

#### A. 겉보기 장관 소실

장관에서 사라지는 경로가 실제 흡수($k_{a,true}$)와 장내 분해/손실($k_d$)로 나뉜다고 보면:

$$
\underbrace{k_{a,app}}_{\text{겉보기 소실}}=\underbrace{k_{a,true}}_{\text{실제 흡수}}+\underbrace{k_d}_{\text{장관 손실}}
$$

`[Source: G&W Fig.2.24 and text, pp.40–41]`

$$
\underbrace{F}_{\text{도달 분율}}=\frac{\underbrace{k_{a,true}}_{\text{흡수 경로}}}{\underbrace{k_{a,true}+k_d}_{\text{전체소실}}}
$$

`[Source: G&W Eq.2:70, p.41]`

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $k_{a,app}$ | time$^{-1}$ | 장관에서 사라지는 전체 속도 | 실제 흡수 + 장관 손실 |
| $k_{a,true}$ | time$^{-1}$ | 전신 입력으로 이어지는 실제 흡수 속도 | 용출, 투과, 위배출 |
| $k_d$ | time$^{-1}$ | 장관 분해/손실 속도 | 불안정성, fecal loss, 장관 대사 |
| $F$ | fraction | 사라진 약물 중 전신 도달 분율 | $k_{a,true}/(k_{a,true}+k_d)$ |

> 💡 장관 구획은 **출구가 두 개인 싱크대**라고 보시면 돼요. 하나는 전신 순환으로 가는 배수구($k_{a,true}$), 다른 하나는 손실 배수구($k_d$). $k_{a,app}$가 커졌다는 건 흡수가 빨라졌다는 뜻이 아니라 **장관에서 더 빨리 사라졌다**는 뜻일 수 있어요. 어느 배수구로 더 빠지는지는 별도로 봐야 합니다.

#### B. 해석

fitted $k_a$가 커졌다고 곧바로 "흡수가 빨라졌다"가 되지 않아요. "gut compartment에서 더 빨리 사라졌다"일 수도 있습니다. **$AUC$가 함께 변하지 않으면** onset/rate 변화로, **$AUC$도 함께 변하면** extent 변화가 동반된 것으로 해석합니다 [G&W pp.40–41].

#### C. 다중 흡수 부위

흡수 부위가 여러 개면 곡선이 다중 peak를 보이거나 비정형 상승부가 나타나요. buccal + GI 같은 구조가 Eq.2:80–2:82로 제시됩니다 [G&W pp.46–47]. 이 경우 단일 $k_a$는 여러 입력 과정을 하나로 눌러 담은 요약 파라미터일 뿐이에요.

#### D. 비선형 흡수 — capacity-limited input (보강)

지금까지 본 $k_{a,app}$ 분해는 **선형 1차 입력** 안에서의 이야기입니다. 그런데 흡수 자체가 **수송체 매개**일 때는 dose가 올라가면 $F$가 **dose-dependent하게 떨어지는** 또 다른 비선형성이 나타나요. 대표 사례가 **gabapentin** — L-amino acid transporter(LAT/OATP3)에 의한 능동 흡수에 의존하기 때문에 transporter가 포화되면 $F$가 명시적으로 감소합니다 [R&T p.203].

$$
\underbrace{\text{Input rate}}_{\text{유입속도}}=\underbrace{\frac{V_{max,abs}\cdot A_g}{K_{m,abs}+A_g}}_{\text{Michaelis-Menten 입력}}
$$

dose ↑ → $A_g$ ↑ → input rate가 $V_{max,abs}$ 근처에서 plateau → 결과적으로 **$F$가 감소**합니다.

**진단의 첫 신호**는 G&W §2.7.1에 명시되어 있어요 — **"dose-normalized $AUC$ vs dose 그림이 dose 증가에 따라 *감소하는 직선*을 보이면, decreasing bioavailability, saturable input, 또는 zero-order input을 의심한다"** [G&W p.40]. 핵심은 이거예요 — Card 5의 mass action 분해($k_{a,app}=k_{a,true}+k_d$)와 **saturable input은 다른 좌표축**입니다. 전자는 *동일 dose 안에서* 두 경로 분할의 문제, 후자는 *dose 간* 입력 함수 자체가 비선형이 되는 문제예요.

| 비선형성 종류 | 진단 신호 | 사례 |
|---|---|---|
| 선형 1차 + 장관 손실($k_d$↑) | $AUC$ 비례, $F$ 일정 | $k_a$ apparent ↑, but extent 그대로 |
| Saturable absorption ($V_{max,abs}$ 포화) | dose-normalized $AUC$가 dose↑에서 ↓ | gabapentin (LAT/OATP3) [R&T p.203] |
| Saturable first-pass (간/장 대사 포화) | $F$가 dose↑에서 ↑ | alprenolol, propranolol, verapamil 등 [R&T Table 7-5, p.211] |
| Zero-order input (서방형/용해도 제한) | flat plateau, AIC 우월하나 IV·dose range 검증 필요 | PK3 [G&W pp.483–486] |

> ⚠️ **혼동 주의 (G&W p.40 원문):** "dose-normalized AUC가 dose↑에서 감소"는 saturable input뿐 아니라 **decreasing $F$ 또는 zero-order input과도 혼동**됩니다. IV 데이터 없이는 이 셋을 분리할 수 없다는 게 G&W의 원문 경고예요 — "Unless intravenous dosing data are also available, zero-order input and capacity limited elimination confound each other" [G&W p.40].

> 💼 **실무 인사이트:** food effect 보고서에서 "$k_a$ 감소 = 흡수 저하"라고 절대 쓰면 안 됩니다. $F_{rel}$($AUC$ ratio)을 같이 보고해야 해요. $AUC$ 변화 없이 $k_a$만 바뀌면 onset/rate 변화, $AUC$도 같이 바뀌면 extent 변화로 가릅니다. 그리고 **dose escalation에서 $F$가 떨어지면** transporter-mediated saturable absorption을 의심하세요 — superposition 위배 검사(Card 1의 dose 비례성)가 첫 번째 진단입니다.

**Card 5 요약:** $k_a$는 항상 "진짜 흡수속도"가 아닙니다. fitted $k_a$의 생리학적 의미는 모델 구조와 외부 evidence가 같이 정해줍니다.

이 카드 핵심 세 줄. fitted $k_a$가 변했으면 먼저 $k_{a,app}=k_{a,true}+k_d$ 구조를 의심하세요. $AUC$ 변화가 같이 일어났는지를 봐야 rate 변화인지 extent 변화인지 가릴 수 있어요. "$k_a$ 감소 = 흡수 저하"라는 단정은 장관 손실·다중 흡수부위·food effect를 모두 단일 흡수속도로 뭉뚱그리는 오독이고, 그 위에 dose escalation에서 $F$가 떨어지는 saturable absorption까지 합치면 비선형 흡수의 두 축(extent 비선형 vs rate 분해)이 한꺼번에 보입니다.

---

<!-- SLIDE_START: §5 | title: 혼동쌍 해부 -->
<!-- SECTION_CORE: SC-08 -->

## §5. 혼동쌍 해부

다섯 개 카드를 거쳤으니, 이제 임상 보고서나 PopPK 보고에서 가장 자주 라벨이 뒤바뀌는 다섯 가지 페어를 정리합니다. 같은 숫자라도 라벨이 바뀌면 임상 결론이 완전히 달라져요.

### 혼동쌍 1. $k_a$ vs $k_{el}$ under flip-flop — 결정타

| 비교 기준 | $k_a$ | $k_{el}$ |
|---|---|---|
| 단위 / 차원 | time$^{-1}$, 흡수부위 소실 속도 | time$^{-1}$, 중심구획 소실 속도 |
| 수식 내 위치 | $e^{-k_a t}$ input 지수항 | $e^{-k_{el}t}$ disposition 지수항 |
| 변화 원인 | 용출, 위배출, 흡수부위, 제형 | $CL/V$, 신장·간 기능, 분포 변화 |
| 혼동 시 임상 결과 | flip-flop에서 terminal slope label 오류 | dosing interval, accumulation, washout 판단 오류 |

**결정타:** terminal half-life를 elimination half-life로 착각하면 dosing interval·accumulation·washout 판단이 한꺼번에 흔들립니다.

**⚡ 기억 고리 — 어느 쪽이 병목인가:** flip-flop은 $k_a<k_{el}$이니까 **흡수가 병목** — 그러면 terminal slope는 $k_a$를 따릅니다. Disposition-limited는 $k_{el}<k_a$이니까 **제거나 분포가 병목** — terminal slope는 $k_{el}$. **IV 크로스오버 없이 경구만 가지고는 두 메커니즘을 가를 수 없다는 점이 결정적인 함정이에요.**

**⚡ 기억 고리 — 정점 시각 vs 흡수 종료 시각:** $T_{max}$는 흡수 속도와 제거 속도가 같아지는 **교차점**이에요. 흡수가 다 끝난 시점이 아닙니다. $T_{max}$ 이후에도 흡수는 계속되고, 단지 제거가 더 빠를 뿐이에요.

### 혼동쌍 2. $F$ vs $k_a$ — extent와 rate

| 비교 기준 | $F$ | $k_a$ |
|---|---|---|
| 단위 / 차원 | fraction, 전신 도달 분율 | time$^{-1}$, 흡수부위 소실 속도 |
| 수식 내 위치 | 진폭·AUC scale: $F\cdot Dose/CL$ | 지수항과 $t_{max}$ 식의 rate term |
| 변화 원인 | 흡수 분율, 장관·간 first-pass, 제형 | 용출, 위배출, 흡수부위 이동 |
| 혼동 시 임상 결과 | AUC와 peak timing 변화 원인 혼동 | food/formulation effect 보고 오류 |

$$
\underbrace{\frac{k_a}{K}}_{\text{속도 비율}}=\underbrace{\frac{k_a}{CL\cdot V}}_{\text{원문대비}}
$$

**⚡ 기억 고리 — "얼마나 들어오나" vs "얼마나 빨리":** $F$는 systemic circulation에 도달하는 **비율**, $k_a$는 흡수 부위에서 얼마나 빠른지의 **속도**. $AUC$는 $F$에 비례하고, $T_{max}$·$C_{max}$ 형태는 $k_a/K$ 비율이 정합니다.

**⚡ 기억 고리 — 속도계 vs 적산계:** $k_a$는 **속도계(순간 속도)**, $F$는 **적산계(누적 도달량)**. $k_a$를 키워도 $F$가 그대로면 $AUC$는 그대로예요.

### 혼동쌍 3. $V/F$ vs $V$ — 결정타

| 비교 기준 | $V/F$ | $V$ |
|---|---|---|
| 단위 / 차원 | volume, apparent | volume, true distribution volume |
| 수식 내 위치 | oral-only 보고, $F$와 묶임 | IV 또는 $F$ 근거가 있어야 분리 |
| 변화 원인 | $V$ 변화 또는 $F$ 변화 | 조직분포, 체성분, 단백결합 |
| 혼동 시 임상 결과 | $F$ 변화가 분포용적 변화처럼 보임 | phantom interpretation, covariate 해석 오류 |

**결정타:** $V/F$를 $V$로 바꿔 쓰는 순간, **흡수율 변화가 분포용적 변화처럼 보이는 phantom interpretation**이 생깁니다.

### 혼동쌍 4. First-order $k_a$ vs Zero-order input

| 비교 기준 | First-order $k_a$ | Zero-order input |
|---|---|---|
| 단위 / 차원 | time$^{-1}$, 남은 양 비례 입력 | amount/time, 일정 입력 |
| 수식 내 위치 | $e^{-k_a t}$ 지수항 | 일정 입력률, 종료 후 washout |
| 변화 원인 | 속방형 용액/정제 근사, 용출·위배출 | controlled-release, 삼투펌프, 용출 제한 |
| 혼동 시 임상 결과 | 0차 모델의 better fit을 진짜 0차 흡수로 과장 | PK3처럼 AIC 우월이 기전 증명을 뜻하지 않음 [G&W pp.483–486] |

### 혼동쌍 5. Linear absorption vs Saturable absorption (보강)

| 비교 기준 | Linear 1st-order absorption | Saturable absorption |
|---|---|---|
| 단위 / 차원 | $k_a$ (time$^{-1}$), dose 비례 | $V_{max,abs}/K_{m,abs}$ (Michaelis-Menten) |
| 수식 내 위치 | $-k_a A_g$ 항 | $-V_{max,abs}\cdot A_g/(K_{m,abs}+A_g)$ |
| 변화 원인 | 수동 확산, 용출/위배출 의존 | 능동 수송체 (LAT, PEPT1, OATP) 포화 |
| 진단 신호 | dose-normalized $AUC$ 일정 | dose-normalized $AUC$ ↓ at high dose [G&W p.40] |
| 사례 | 대부분의 small-molecule 경구약 | gabapentin (LAT/OATP3) [R&T p.203], L-dopa, amoxicillin |
| 혼동 시 임상 결과 | dose escalation 시 노출 예측 정상 | dose ↑에서 $C_{max}$ plateau, 치료실패·BE 해석 오류 |

**⚡ 기억 고리 — Superposition 검사:** dose를 2배로 올렸을 때 $AUC$가 2배가 안 나오면 비선형성을 의심하세요. **dose-normalized $AUC$가 dose↑에서 *감소*하면** → saturable input/decreasing $F$/zero-order input 중 하나 (셋은 IV 없이 분리 불가 [G&W p.40]). **dose-normalized $AUC$가 dose↑에서 *증가*하면** → saturable first-pass [R&T Table 7-5, p.211].

**§5 요약:** 경구 PK에서 가장 위험한 혼동은 slope label·apparent parameter·rate/extent를 서로 바꿔 부르는 거예요. 이름표가 바뀌면 같은 숫자도 다른 임상 결론을 만듭니다. 그리고 다섯 번째 혼동쌍 — **linear vs saturable absorption**은 dose range를 확장할 때 가장 먼저 깨지는 가정입니다.

---

<!-- SLIDE_START: §7 | title: 자기 테스트 -->
<!-- SECTION_CORE: SC-09 -->

## §7. 자기 테스트: 능동 회상

### Q1. Master equation을 쓰고 각 항의 의미를 설명하세요.

$$
\underbrace{C(t)}_{\text{혈장 농도}}=\frac{\overbrace{k_a F D_{po}}^{\text{전신 입력}}}{\underbrace{V(k_a-k_{el})}_{\text{희석·분리}}}\left(\underbrace{e^{-k_{el}t}}_{\text{소실 지수}}-\underbrace{e^{-k_a t}}_{\text{흡수 지수}}\right)
$$

$k_a$는 흡수부위 소실 속도, $F$는 전신 도달 분율, $D_{po}$는 투여량, $V$는 분포용적, $k_{el}$은 소실 속도. 괄호 안은 소실 지수와 흡수 지수의 차이예요 [G&W p.30; R&T p.782].

### Q2. 왜 $t_{max}$ 식에 $F$, $V$, dose가 없는가?

$t_{max}$는 $dC/dt=0$이 되는 시점이에요. linear system에서 $F$·$V$·dose는 곡선의 높이만 scale할 뿐, 기울기가 0이 되는 시간 위치는 바꾸지 않습니다. $t_{max}=\ln(k_a/k_{el})/(k_a-k_{el})$ [G&W p.35].

### Q3. $F_{rel}=1.0$인 두 oral formulation이 임상적으로 완전히 같은가?

아니에요. $F_{rel}=1.0$은 extent가 같다는 뜻일 뿐 — $k_a$가 다르면 $C_{max}$·$t_{max}$가 달라지고, onset이나 peak-related safety가 중요한 약물에서는 임상적 차이가 분명히 남습니다 [R&T pp.181–183].

### Q4. PK2에서 $V/F=32\ \mathrm{L}$, $F=0.82$일 때 진짜 $V$는?

산술적으로는 $V=32\times0.82\approx26\ \mathrm{L}$이에요. 그런데 원문은 $true\ V=20\ \mathrm{L}$이라고 서술해서 산술값과 충돌합니다. 본 handout은 26 L를 확정값으로 쓰지 않고 "원문 수치 충돌 [확인 필요]"로 표시해 둡니다 [G&W p.480].

$$
\underbrace{V}_{\text{true V}}=\underbrace{(V/F)}_{\text{apparent V}}\times\underbrace{F}_{\text{F 보정}}=\underbrace{32\times0.82}_{\text{산술 환산}}\approx\underbrace{26\ \mathrm{L}}_{\text{계산 V}}
$$

> 🔎 **충돌 가설 (보강):** 원문 PK2는 동일 사례 안에서 V/F가 *initial estimate*(30 L), *solution II*, *solution III*(6.54 L)별로 다르게 등장하고, F도 *deconvolved*(82%)와 *NCA*(60~64%) 두 값이 함께 제시됩니다 [G&W pp.480–482]. 그러므로 V≈20 L는 **solution II의 V/F × deconvolved F**의 곱으로 보고된 결과이고, 32 L는 다른 solution path의 V/F일 가능성이 높습니다. 학습자가 모델링 보고서를 검토할 때 같은 데이터셋에서도 **추정 경로(NCA, deconvolution, NLR solution I/II/III)에 따라 V·F·CL 환산값이 다르게 떨어진다**는 점을 진단하는 훈련 사례예요.

### Q5. Oral-only fit에서 $k_a=0.05\ \mathrm{hr}^{-1}$, $k_{el}=0.5\ \mathrm{hr}^{-1}$. 관찰 terminal half-life를 $\ln 2/0.5=1.4\ \mathrm{h}$로 써도 되는가?

안 됩니다. $k_a<k_{el}$이면 관찰 terminal slope가 더 작은 $k_a$를 따를 수 있어서 terminal half-life는 약 $\ln 2/0.05=13.9\ \mathrm{h}$로 나옵니다. $k_{el}=0.5\ \mathrm{hr}^{-1}$가 진짜 elimination일 가능성도 있지만, oral-only로는 확정할 수 없어요.

$$
\underbrace{t_{1/2,obs}}_{\text{관찰 반감기}}=\frac{\underbrace{\ln 2}_{\text{반감기 상수}}}{\underbrace{0.05}_{\text{병목}}}\approx\underbrace{13.9\ \mathrm{h}}_{\text{flip-flop}}
$$

### Q6. PK3에서 zero-order model의 AIC가 first-order보다 낮았다. "진짜 0차 흡수"라고 결론 가능한가?

아니에요. PK3는 zero-order input model이 해당 dataset을 더 잘 설명한다는 것만 보여줍니다 — 진짜 기전을 확정하려면 용량 범위, 반복 투여, IV 데이터 같은 추가 근거가 필요합니다 [G&W pp.483–486].

### Q7. $k_{a,app}=1.0\ \mathrm{hr}^{-1}$, $k_d=0.4\ \mathrm{hr}^{-1}$일 때 $k_{a,true}$와 $F$는?

$k_{a,true}=1.0-0.4=0.6\ \mathrm{hr}^{-1}$.

$$
F=\frac{k_{a,true}}{k_{a,true}+k_d}=\frac{0.6}{1.0}=0.6
$$

$$
\underbrace{F}_{\text{도달 분율}}=\frac{\underbrace{k_{a,true}}_{\text{흡수 }0.6}}{\underbrace{k_{a,true}+k_d}_{\text{전체 }1.0}}=\underbrace{0.6}_{\text{60\% 도달}}
$$

G&W Eq.2:70의 구조를 그대로 적용한 해석이에요. 실데이터에서는 $k_d$를 별도 evidence 없이 분리하기가 어렵습니다 [G&W p.41].

### Q8. Boss dilemma: terminal slope가 $0.18\ \mathrm{hr}^{-1}$이고 alternative model로는 $k_{el}=0.69\ \mathrm{hr}^{-1}$도 가능. 무엇을 보고할 것인가?

관찰 terminal half-life는 $\ln 2/0.18\approx3.85\ \mathrm{h}$로 계산됩니다. 그런데 flip-flop 가능성이 있으면 0.18이 $k_{el}$인지 $k_a$인지 확정할 수 없어요. 안전한 보고는 이렇게 합니다 — **"oral-only data에서 terminal slope는 $0.18\ \mathrm{hr}^{-1}$로 관찰되었으나, IV 또는 route·formulation comparison 없이는 이를 elimination rate로 확정할 수 없다. Dose recommendation은 두 해석에 대한 sensitivity analysis로 방어한다."**

$$
\underbrace{t_{1/2,terminal}}_{\text{말기 반감기}}=\frac{\underbrace{\ln 2}_{\text{반감기 상수}}}{\underbrace{0.18\ \mathrm{hr}^{-1}}_{\text{obs slope}}}\approx\underbrace{3.85\ \mathrm{h}}_{\text{계산 반감기}}
$$

### Q9. (보강) 어떤 약물의 단회 경구 dose escalation 결과, 100 mg에서 AUC = 50 mg·h/L, 300 mg에서 AUC = 100 mg·h/L, 900 mg에서 AUC = 150 mg·h/L를 보입니다. 진단은?

Dose-normalized AUC를 계산해봅시다.

$$
\underbrace{\frac{AUC}{Dose}}_{\text{용량보정 노출}}=\begin{cases}\underbrace{0.50}_{\text{100 mg}}\\ \underbrace{0.33}_{\text{300 mg}}\\ \underbrace{0.17}_{\text{900 mg}}\end{cases}\ \mathrm{h/L}
$$

dose가 올라갈수록 dose-normalized AUC가 **감소**합니다. G&W §2.7.1의 진단 신호에 정확히 부합해요 — **decreasing bioavailability, saturable input, 또는 zero-order input** 중 하나입니다 [G&W p.40]. IV 데이터 없이는 셋을 분리할 수 없어요. Gabapentin 같은 transporter-mediated absorption(LAT/OATP3)이 의심되면 saturable input 가설을 우선 검증합니다 [R&T p.203].

→ 만약 반대 패턴(dose↑에서 dose-normalized AUC ↑)이 나오면 **saturable first-pass metabolism**입니다 [R&T Table 7-5, p.211] — alprenolol, propranolol, verapamil이 대표 사례.

---

## ⚡ 보스 딜레마 ★★ — 최종 자기 테스트 캡스톤

### Boss Dilemma. 제형 변경 후 $C_{max}$↓·$T_{max}$↑: 두 가설을 어떻게 방어할 것인가?

**시나리오:** 경구 단독 Phase 1 결과에서 $C_{max}$가 내려가고 $T_{max}$가 늘어났어요. 제형 팀은 "흡수가 느려졌다($k_a$ 감소)"고 결론을 내립니다. 모델러 입장에서는 두 가지 방어 가능한 해석이 있어요.

- **(A) $k_a$ 감소**로 해석 → absorption model을 first-order에서 transit compartment로.
- **(B) $F$ 감소** (first-pass 효율 감소나 다른 이유로 apparent $CL$ 증가 → $AUC$ 감소)로 해석 → $F$에 영향을 주는 공변량 탐색이 우선.

**거장의 절충 판단:**

(A)는 모델 복잡도를 높이면서 $T_{max}$ 재현에 집중합니다. 그런데 IV 없이는 $F$와 $k_a$의 교락(confounding, ← 두 요인이 얽혀서 분리가 안 되는 상태)을 풀 수 없어요 (Card 4의 합성곱 관점). 보고할 때는 **"transit compartment가 $T_{max}$ 지연을 더 잘 설명하지만, $F$ 동시 변화 가능성을 본 데이터로 배제할 수 없다"**고 명시해야 합니다.

(B)는 파라미터 수를 단순하게 두지만, $k_a$ 변화가 진짜 원인이었다면 $AUC$ 자체와 곡선 형태가 어긋날 수 있어요. 보고할 때는 **"$AUC$ ratio가 유의하게 감소해서 $F$-driven 해석을 지지하지만, $k_a$ 변화 가능성을 sensitivity analysis로 평가했다"**고 기술합니다.

**규제 방어 — 어떻게 가르는가:**

> **1단계.** "$AUC$가 같은가, 다른가"로 가설을 분리합니다.
> &nbsp;&nbsp;— $AUC$ 변화 없음 + $C_{max}$↓·$T_{max}$↑ → (A) $k_a$ 감소가 우세
> &nbsp;&nbsp;— $AUC$ 감소 + $C_{max}$↓·$T_{max}$↑ → (B) $F$ 감소, 또는 (A+B) 복합
> **2단계.** IV 크로스오버를 요청하거나, 그게 안 되면 **두 모델을 모두 적합시키고 sensitivity analysis로 명시.**
> **3단계.** 단일 가설을 채택하지 말고, **"두 해석 모두 데이터와 정합적이며, 임상 dosing이 두 해 모두에서 안전한 영역인가"**를 평가합니다.

→ 가장 위험한 자세는 **"$k_a$ 감소 = 흡수 불량 = 제형 재조제"**라는 단순 추론이에요. Card 4의 그럴듯한 오류 단락이 경고한 함정이고, BE trial의 의사결정 사슬을 잘못 만들어냅니다.

**§7 요약:** 계산보다 중요한 건 label이에요. 같은 숫자라도 $k_a$인지 $k_{el}$인지, $V$인지 $V/F$인지를 잘못 붙이면 임상 결론이 통째로 달라집니다.

---

> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** 경구 PK의 전문성은 $V/F$, $CL/F$, $k_{a,app}$, terminal slope ambiguity를 숨기지 않고 명시하는 데서 완성됩니다.

---

<!-- SLIDE_START: §8 | title: 메타프레임과 큰 그림 -->
<!-- SECTION_CORE: SC-10 -->

## §8. 메타프레임과 큰 그림

### A. 이 세션의 위치

이 세션은 IV bolus 이후 첫 임상 현실 — **흡수 단계가 들어있는 계**를 다뤘어요. 앞으로 다회투여·modified-release·food effect·BE·PopPK 흡수 모델로 가더라도, 판단 기준은 결국 다음 네 질문으로 돌아옵니다.

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| 입력 함수가 1차가 아님 | $k_a$, lag, input duration | → | $C_{max}$·$t_{max}$ 재현 실패 | lag/zero-order/transit 후보 평가 |
| $F$가 제형·식사·first-pass로 변함 | $F$, $CL/F$ | → | AUC 차이와 apparent clearance 변화 | $F_{rel}$, AUC ratio, sensitivity |
| terminal slope label 불명확 | $k_a$ 또는 $k_{el}$ | → | 반감기·축적 판단 오류 | IV/route comparison 또는 dual-solution 방어 |
| $V$, $CL$을 absolute처럼 보고 | $V/F$, $CL/F$ | → | covariate effect 오해 | apparent parameter 명시 |
| Dose 비례성 위배 | 흡수·대사·배설의 비선형성 | → | dose escalation에서 노출·반응 예측 실패 | dose-normalized AUC 진단 [G&W p.40] |

### B. 의존성 — 놓치면 어떻게 무너지는가

| 실패 모드 | 실제 결과 |
|---|---|
| $V/F$를 $V$로 보고 | 공변량 효과를 분포 변화로 오해 |
| $CL/F$를 $CL$로 보고 | $F$ 변화가 clearance 변화처럼 보임 |
| 말기 기울기를 무조건 $k_{el}$로 해석 | flip-flop에서 반감기·축적 판단 오류 |
| $k_a$ 변화를 extent 변화로 단정 | food/formulation effect 메시지 오류 |
| $t_{max}$의 용량 의존성을 무시 | 포화성 흡수·초회 통과 포화·비선형 소실 신호를 놓침 |
| 0차 모델의 더 나은 적합을 기전 증명으로 단정 | 서방형·용해도·용출 근사를 생리학적 확정으로 과장 |
| Dose escalation에서 superposition 위배를 noise로 처리 | saturable absorption/first-pass 신호를 놓침 [G&W p.40; R&T p.211] |

### C. 전문가가 실제로 보는 지점

> 💼 **실무 인사이트:** 30년 차 pharmacometrics 연구자가 경구 모델 결과를 볼 때 가장 먼저 묻는 질문은 "모델이 맞았는가?"가 아닙니다. **"무엇이 식별되었는가?"**예요. Phase 1 SAD(단회 상승 용량 시험) 회의에서 senior가 던지는 질문은 단순해요 — **"FIH(최초 임상 투여) 단계에서 IV arm이나 absolute $F$ 확인 가능성을 평가했는가?"** 이 한 줄의 질문이 $F$, $V/F$, $CL/F$, flip-flop, $k_{a,app}$의 모든 위험을 앞으로 끌어냅니다.

| 후속 세션 | 이 세션에서 열리는 개념 | 없으면 실패하는 것 |
|---|---|---|
| multiple dosing / accumulation | terminal slope label, $k_{el}$ vs $k_a$ | 축적계수·washout 해석 오류 |
| modified-release / zero-order input | input function 구분 | better fit을 기전 증명으로 과장 |
| oral PopPK absorption | $V/F$, $CL/F$, $k_{a,app}$ | apparent를 true로 보고 |
| BE / food effect | rate vs extent 분리 | $AUC$, $C_{max}$, $t_{max}$ 메시지 혼동 |
| nonlinear absorption / TDM | superposition test, dose-normalized AUC | saturable input/first-pass 신호 누락 |

### D. BCS · BDDCS — 흡수 변동성의 정량적 좌표계 (보강)

여기까지의 모든 카드는 **수식 모델**의 정직성을 다뤘어요. 그런데 임상에서 식사 효과·제형 변경·BE waiver 같은 결정을 내릴 때는, 약물의 **물리화학적 위치**가 미리 답의 절반을 가르쳐줍니다. 그 좌표계가 BCS(Biopharmaceutics Classification System)예요.

#### D-1. BCS Class I–IV 매트릭스 [R&T Table 7-8, pp.219–220]

BCS는 두 축으로 약물을 분류합니다 — **용해도(solubility)**와 **장관 투과도(intestinal permeability)**.

| | High Permeability | Low Permeability |
|---|---|---|
| **High Solubility** | **Class I** | **Class III** |
| **Low Solubility** | **Class II** | **Class IV** |

용해도 기준: 최고 강도(highest strength)가 pH 1–7.5 범위에서 250 mL의 물에 녹는가. 투과도 기준: 장관 흡수가 완전한가 또는 in vitro에서 highly permeable로 입증되는가 [R&T p.219]. 그리고 BCS는 **즉방형(immediate-release) 제형**에 한해 적용됩니다(15분 내 85% 용출).

| Class | 특성 | 흡수 율속 단계 | 식사 효과 패턴 | Biowaiver 가능성 |
|---|---|---|---|---|
| **I** (high sol·high perm) | 빠른 용출·완전 흡수 | 위배출 (제형 차이 영향 적음) | 일반적으로 작거나 무시 가능 | **가능** (즉방형) [R&T p.219] |
| **II** (low sol·high perm) | 용출 제한 흡수 | Dissolution | 고지방식이 $F$↑ (담즙·미셀 효과) | 불가 |
| **III** (high sol·low perm) | 투과도 제한 흡수 | Permeability | 식사가 transit 시간·transporter 영향 | 불가 (특정 조건 제외) |
| **IV** (low sol·low perm) | 두 축 모두 제한 | 두 가지 모두 | 변동성 큼, 예측 어려움 | 불가 |

**Class I 약물 예시 [R&T Table 7-9, p.220]:** acetaminophen, caffeine, diazepam, theophylline, metoprolol, propranolol, verapamil, valproic acid, midazolam, fluoxetine, levodopa, atenolol(다만 atenolol은 low perm으로 Class III에 분류되기도 함 — source에 따라 일부 boundary 약물 변동), zidovudine 등. → 이들 약물은 즉방형 제형에서 formulation 차이가 흡수에 영향을 줄 가능성이 낮아 **biowaiver(BE 시험 면제)** 대상이 됩니다 [R&T p.219].

#### D-2. BDDCS — Disposition을 추가한 보완 framework

BCS는 흡수까지만 다뤄요. Benet 그룹의 **BDDCS(Biopharmaceutics Drug Disposition Classification System)**는 같은 두 축을 쓰면서 **disposition route**(주된 제거 경로 — 대사 vs 미변화체 신/담즙 배설)를 더해 transporter 영향 예측까지 가능하게 했습니다 [R&T Table 7-9 footnote: Benet LZ, Broccatelli F, Oprea TI. *BDDCS applied to over 900 drugs*. AAPS J 2011;13:519–547].

| BDDCS Class | BCS 등가 | Transporter 효과 예측 |
|---|---|---|
| 1 | I (high sol·high perm) | 수동확산 우세 → transporter 영향 미미 |
| 2 | II (low sol·high perm) | **장관 efflux**(P-gp 등) 영향, intestinal metabolism 중요 |
| 3 | III (high sol·low perm) | **장관 uptake transporter** 의존, efflux 영향도 큼 |
| 4 | IV (low sol·low perm) | 모든 transporter 영향 가능 |

→ Card 5에서 다룬 **gabapentin의 saturable absorption**(LAT/OATP3) 사례는 BDDCS Class 3의 전형입니다 — high solubility지만 low passive permeability라 능동 수송체에 의존, 그러므로 dose escalation에서 transporter 포화로 $F$ 감소.

> 💼 **실무 인사이트 — BCS가 답을 미리 알려주는 자리:** 신약 개발 초기에 BCS class만 알아도 다음 의사결정의 절반은 정해집니다 — (1) 식사 효과 시험을 priority로 할지 (Class II·IV는 필수), (2) biowaiver를 노릴지 (Class I만 가능), (3) transporter DDI 시험을 어디까지 할지 (BDDCS Class 2·3 우선), (4) controlled-release formulation 개발 적합성 (Class I에 가장 적합 [R&T p.220]). 모델링 한 줄로 풀 수 없는 답을 BCS는 한 표로 줍니다.

#### D-3. BCS와 modified-release 연결

Class I 약물의 즉방형은 위배출 의존이지만, **non-disintegrating controlled-release 제형**은 위배출의 영향을 덜 받습니다 — 위에 머물러 있어도 약물은 계속 십이지장으로 빠져나가니까요 [R&T p.220]. 다만 환자의 식사 습관·복약 시간 불일치로 인한 변동성, 그리고 대장 도달 후 (12–16 hr 이후) 압축에 의한 release 신뢰성 저하가 한계로 남습니다.

### E. Ch.7 맥락

$k_a$와 $F$의 변동성이 어디서 오느냐를 보면, BCS, 위배출, 용출, 수송체, 장관·간 초회 통과 같은 생리·물리화학적 요인들이 있어요. 이 세션의 수식들은 그 복잡성을 **1차 입력과 $F$라는 두 개의 apparent 축**으로 한꺼번에 다루는 첫 단계입니다 [R&T pp.197–220].

> 📖 **G&W p.47, Fig.2.32:** 경구 농도-시간 곡선을 정하는 요인들이 chapter conclusion 수준에서 하나의 구조로 다시 묶입니다 — 이 그림은 지금까지 다룬 모든 카드가 어떻게 한 그림 안에 들어가는지를 보여주는 클로징 다이어그램이에요.

### F. 최종 확정 문장

**최종 요약:** 경구 PK의 핵심은 $C(t)$를 잘 맞추는 데서 끝나지 않습니다. 그것보다 더 중요한 게 있어요 — **$C(t)$에서 실제로 분리 가능한 것과 분리 불가능한 것을 정직하게 가르는 일.** 경구 단독 데이터는 $V/F$, $CL/F$, 겉보기 $k_a$, terminal slope ambiguity를 남깁니다. 이 네 가지를 명시하면 handout은 안전하고, 생략하면 모델은 그럴듯하지만 위험해집니다. 그리고 마지막 한 축 — **BCS/BDDCS는 수식 이전에 약물의 물리화학적 좌표가 답의 절반을 미리 결정한다는 사실을 보여주는 framework**입니다.

---

<!--
## v3.8 자가검증 체크리스트 (보강본 업데이트)

| 항목 | 기준 | 결과 |
|---|---|---|
| SLIDE_START 개수 | §섹션수 + 카드수 합산 | 10 개 (원본 보존) |
| 카드당 callout 합계 ≤ 6 | 전체 카드 | ✓ |
| [E] 박스 존재 | 모든 §2 카드 | ✓ |
| [D] 거장의 시각 존재 | 모든 §2 카드 | ✓ |
| [L] 파라미터 표 존재 | Apex 카드 + 정의 수식 카드 | ✓ |
| §5 혼동 쌍 표 행 순서 고정 (5행, 보강 후) | §5 전체 | ✓ |
| 기호 일관성 | 첫 등장 기준 통일 | ✓ |
| PART B 흔적 없음 | 전체 | ✓ |
| 수치 anchor 보존 | 원본 수치 anchor | ✓ |
| [M] 나비효과 이중 종착점 | Apex 카드 전체 | ✓ |
| 보강 항목 표시 | "(보강)" 명시, 출처 포함 | ✓ |

보강 항목 요약:
- Card 4 사례 앵커: PK2 V=20 vs 26 충돌의 가능한 출처 가설 박스 추가 (§7 Q4와 연동)
- Card 5: §D 비선형 흡수 (capacity-limited input) 신설 — gabapentin LAT/OATP3 [R&T p.203], G&W §2.7.1 진단 신호 [G&W p.40], saturable first-pass [R&T Table 7-5, p.211]
- §5: 혼동쌍 5 (Linear vs Saturable absorption) 추가
- §7: Q9 (dose-normalized AUC 진단) 추가
- §8: §D BCS·BDDCS framework 추가 [R&T Tables 7-8/7-9, pp.219–220]
- §8: 변화 상황 표 1행 + 실패 모드 표 1행 추가 (superposition 위배)
- 표기 일관성: 수식 annotation에 overbrace/underbrace 보강
-->

<!-- 변환 노트
- v3.7 → v3.8 변환: 메타 콘텐츠 정리, 학습자 메타 노출 차단
- v3.7 → v3.9 변환: v3.8 메타데이터 회귀 보정, SECTION_CORE 마커 적용, 출처 표기 [G&W]/[R&T] 표준 통일
- v3.9 → v4.0 변환: Spoken-Voice Rewrite, Park 교수 페르소나 빙의, 메타-언어 헤더(체화 핵심·Plausible Fallacy·진단 시그니처) 제거 후 산문 흡수, 자기참조 해소, 약물 사례 3-Step 즉맥락 적용 (Fluticasone/Theophylline/Penicillin G), Apex 박스 자연 산문화. 콘텐츠 스코프·약물·수치·출처·수식·SLIDE_START/SECTION_CORE 마커 전수 보존
- v4.0 → v4.0 보강본 변환: 검토 의견 III-11/VI-A1/VI-B3 반영. (1) Card 4 사례 앵커에 PK2 V/F 충돌 가설 박스 추가, (2) Card 5 §D 신설 — 비선형 흡수(saturable absorption) 분기 (gabapentin LAT/OATP3 [R&T p.203], G&W §2.7.1 진단 [G&W p.40], saturable first-pass [R&T Table 7-5, p.211]), (3) §5 혼동쌍 5 신설 (Linear vs Saturable absorption), (4) §7 Q9 추가 (dose-normalized AUC 진단), (5) §8 §D BCS·BDDCS framework 신설 [R&T Tables 7-8/7-9, pp.219–220]. 원본 콘텐츠·약물·수치·출처·수식·SLIDE_START/SECTION_CORE 마커 전수 보존, 보강 부분은 "(보강)" 또는 별도 박스로 명시.
-->

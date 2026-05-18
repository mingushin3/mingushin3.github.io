# 03 — 경구(혈관외) PK: F · ka · tmax · 흡수 — Remastered Edition

---

## 🎯 한 줄 치트키 — 이것만 잡으면 나머지는 자동으로 풀림

> **경구 곡선 = (입력함수) ⊛ (disposition).**
> 즉, **합성곱 구조임.** 그래서 같은 곡선이 입력만 다르게, F만 다르게, 둘 다 다르게 — 여러 조합으로 만들어질 수 있음. **모든 게 apparent가 되는 근원이 바로 이 합성곱 구조임.**

이 한 줄이 핵심임. 아래 모든 카드는 결국 이 한 줄의 따름정리(corollary)임:

- $V$와 $F$가 분리 안 됨 → **$V/F$**만 추정 가능함
- $CL$과 $F$가 분리 안 됨 → **$CL/F$**만 추정 가능함
- terminal slope가 $k_a$인지 $k_{el}$인지 라벨이 뒤집힐 수 있음 → **flip-flop**
- fitted $k_a$가 진짜 흡수속도가 아닐 수 있음 → **$k_{a,app} = k_{a,true} + k_d$**
- "좋은 fit"이 "진짜 메커니즘"의 증명이 아님 → numerical vs structural identifiability

**그래서 실무에서 위험한 한 줄은 다음 다섯 개임:**
1. "$V/F$"를 "$V$"로 적기
2. "$CL/F$"를 "$CL$"로 적기
3. "terminal slope = $k_{el}$"로 단정하기
4. "$k_a$ 감소 = 흡수 저하"로 단정하기
5. "AIC 더 좋음 = 진짜 0차 흡수"로 단정하기

이 다섯 줄을 보고서에 적는 순간 임상·규제 양쪽에서 일이 터짐. **이걸 어떻게 피하는가 — 이 챕터 전체가 그 답임.**

---

## 임상 오프닝 — 같은 숫자, 완전히 다른 결론

R&T 6장에 이런 사례 있음. 같은 약물을 **i.m.으로 주면 $F$ = 97%**, **경구 용액으로 주면 $F$ = 46%**로 나옴 [R&T Table 6-1 / Fig.6-14, pp.183–184]. 이 두 숫자를 보고 "경구는 흡수가 느린 거구나"라고 말하는 순간 — **속도($k_a$, 얼마나 빨리)와 양($F$, 얼마나 많이)이 머릿속에서 섞이기 시작함.** $F$는 속도가 아님. $F$는 도달한 양임.

더 위험한 상황 하나 더 있음. 경구만 가지고 있는 데이터에서 $V/F$, $CL/F$, terminal slope를 각각 $V$, $CL$, $k_{el}$처럼 보고하는 경우임. **이 한 줄의 보고 문장이 임상 판단과 규제 판단을 통째로 흔들 수 있음.** 오늘 다룰 게 그 한 줄을 어떻게 정직하게 쓰는지임.

---

## 출처 및 범위 노트

> **Source A (G&W):** Gabrielsson & Weiner, *Pharmacokinetic and Pharmacodynamic Data Analysis*, 5th ed., Ch.2 §§2.2.4–2.2.12 (pp.28–47), §2.7.1 (p.40), PK2 (pp.476–482), PK3 (pp.483–486)
> **Source B (R&T):** Rowland & Tozer, *Clinical Pharmacokinetics and Pharmacodynamics*, 5th ed.(현 4판 학습자료에서는 4판 표시), Ch.6 (pp.169–195), Ch.7 (pp.197–220), Appendix F (pp.781–784)
> **기호 약속:** $k_a$ = 흡수 속도상수, $k_{el}$ = 소실 속도상수, $V/F$ = 겉보기 분포용적, $CL/F$ = 겉보기 청소율

---

## §0. 빅 픽처 — 다섯 카드의 위치

| # | 카드 | 한 줄 메시지 |
|---|---|---|
| 1 | **$C(t)$ Master Equation** | 경구 곡선은 두 지수함수의 차이임. 상승부 = 흡수, 하강부 = 소실이라는 단순한 라벨은 위험함 |
| 2 | **$t_{max}$ / $C_{max}$** | $t_{max}$는 "흡수 완료 시점"이 아니라 **rate balance의 시점**임 |
| 3 | **생체이용률 $F$** | $F$는 "얼마나 많이"임. **$AUC$가 읽는 extent**임. 절대 속도 개념이 아님 |
| 4 | **Apex — $V/F$ + Flip-flop** | 경구 단독 데이터는 **합성곱 구조** 때문에 원리적으로 분리 못 하는 게 있음 |
| 5 | **$k_{a,app}$ vs $k_{a,true}$** | fitted $k_a$는 흡수 + 장관손실의 합임. "진짜 흡수속도"가 아닐 수 있음 |

```
[IV bolus 1구획 PK]
  → [이 세션: 경구/혈관외 흡수, F, ka, tmax, V/F, flip-flop]
  → [multiple dosing · modified-release · oral PopPK absorption · BE/food effect]
```

🧭 **읽는 순서:**
- Card 1: 경구 농도곡선은 왜 "두 지수함수의 차이"인가?
- Card 2: 최고농도 시점은 왜 "흡수 완료"가 아닌가?
- Card 3: $F$는 왜 "속도"가 아닌가?
- Card 4: 경구 단독으로는 왜 $V$·$CL$·terminal slope를 확정할 수 없는가?
- Card 5: 적합된 $k_a$는 왜 실제 흡수속도가 아닐 수 있는가?

---

<!-- SLIDE_START: M1 | title: C(t) Master Equation -->
<!-- SECTION_CORE: SC-03 -->

## §1. Card 1 — $C(t)$ Master Equation: 골격이 여기서 끝남

### 🎯 이 카드의 치트키

**"경구 곡선 = 흡수 지수 − 소실 지수." 그게 다임.** 그리고 분모의 $(k_a - k_{el})$이 두 과정이 시간축에서 얼마나 떨어져 보이는지를 정함.

### 왜 이게 중요한가

IV bolus에서는 약이 들어오자마자 $C_0$가 즉시 만들어졌음. 경구는 완전히 다름. **농도가 0에서 시작해서 천천히 올라가는데, 이건 그냥 "약이 늦게 들어오는" 게 아님.** 흡수와 소실이 **동시에** 일어나면서, 두 지수함수의 **차이**로 곡선이 만들어짐. 이 구조 때문에:
- $F$와 $V$가 $V/F$로 묶임
- $k_a$와 $k_{el}$이 terminal slope에서 자리바꿈할 수 있음 (flip-flop)
- "상승부 = 흡수, 하강부 = 소실"이라는 단순 라벨이 위험해짐

### 수식 — 골격 한 줄

가정: 1구획 · 1차 흡수 · 1차 소실 · 선형 PK (dose 비례성 유지) [G&W p.30; R&T pp.171–172]

**흡수 부위 (장관):**

$$
\underbrace{\frac{dA_g}{dt}}_{\text{장관 변화}} = -\underbrace{k_a}_{\text{장관 소실}}\underbrace{A_g}_{\text{장관 잔량}}
$$

**혈장 / 중심구획:**

$$
\underbrace{\frac{dC}{dt}}_{\text{농도 변화}} = \underbrace{\frac{k_a F D_{po} e^{-k_a t}}{V}}_{\text{전신 입력}} - \underbrace{k_{el} C}_{\text{중심 소실}}
$$

`[Source: G&W Eq.2:32–2:34, p.30; R&T Eq.6-2–6-3, pp.171–172]`

**적분해 — 이게 골격임:**

$$
\underbrace{C(t)}_{\text{혈장 농도}}=\frac{\overbrace{k_a F D_{po}}^{\text{전신 입력}}}{\underbrace{V(k_a-k_{el})}_{\text{희석·분리}}}\left(\underbrace{e^{-k_{el}t}}_{\text{소실 지수}}-\underbrace{e^{-k_a t}}_{\text{흡수 지수}}\right)
$$

`[Source: G&W Eq.2:35, p.30; R&T Appendix F Eq.F-1, p.782]`

### 한 줄 비유 — 두 모래시계

**두 모래시계가 겹쳐있다고 보면 됨.** 장관에서 빠지는 모래시계가 $k_a$, 중심구획에서 사라지는 모래시계가 $k_{el}$. 우리가 보는 농도는 **두 흐름의 차이**임. 그래서 하강부가 보인다고 무조건 elimination phase가 아님 — $k_a < k_{el}$이면 terminal slope는 **흡수가 정하는 감소(absorption-limited decline)**일 수 있음.

### 파라미터 정의표

| 파라미터 | 단위 | 의미 | 변화 원인 |
|---|---:|---|---|
| $F$ | fraction | 전신 순환 도달 분율 | 제형, food effect, first-pass |
| $D_{po}$ | amount | 경구 투여량 | 용량군, 순응도 |
| $V$ | volume | 농도 희석 공간 | 체성분, 조직분포, 단백결합 |
| $k_a$ | time$^{-1}$ | 장관/흡수부위 소실 속도 | 용출, 위배출, 장관 손실 |
| $k_{el}$ | time$^{-1}$ | 중심구획 소실 속도 | $CL/V$, 신장·간 기능 |

### Lag-time — 흡수 시작 전 지연

투여 시각이 아니라 실제 흡수 시작 이후의 시간만 식에 들어감.

$$
C(t)=0 \quad (t<t_{lag})
$$

$$
\underbrace{C(t)}_{\text{지연 후 농도}}=\frac{\overbrace{k_a F D_{po}}^{\text{입력 크기}}}{\underbrace{V(k_a-k_{el})}_{\text{희석·분리}}}\left(\underbrace{e^{-k_{el}(t-t_{lag})}}_{\text{소실 지수}}-\underbrace{e^{-k_a(t-t_{lag})}}_{\text{흡수 지수}}\right)\quad (t \ge t_{lag})
$$

`[Source: G&W Eq.2:39–2:42, pp.32–33]`

### 0차 입력 — 다른 입력 함수

0차 흡수는 중심 소실은 그대로 두고 입력 함수만 바꾼 경우임. 흡수 중에는 입력이 거의 일정하다가, 흡수가 끝나면 washout만 남음 [G&W Eq.2:66–2:67, p.38; R&T Fig.6-2, p.171]. G&W PK3 사례에서는 zero-order model의 AIC가 first-order보다 좋게 나왔음. 근데 여기서 함정 — **AIC가 더 좋다고 해서 "이건 진짜 0차 흡수다"가 증명되는 건 아님.** 진짜 기전 확정은 dose range, 반복투여, IV 비교 같은 추가 evidence가 필요함 [G&W pp.483–486].

### 💼 실무 인사이트

NONMEM ADVAN2 oral model에서 **KA initial을 큰 값과 작은 값 둘 다 시도해봐야 함.** 서로 다른 initial이 다른 해로 가거나 비슷한 OFV로 수렴하면 → **flip-flop 또는 practical identifiability 문제 의심.**

### Card 1 요약

- 경구 $C(t)$는 "**흡수 지수 − 소실 지수**"임
- $F$와 $V$는 진폭을 정하고, $k_a$와 $k_{el}$은 곡선 모양과 terminal slope 해석을 지배함
- "하강부 = elimination" 단정은 위험함 (flip-flop에서 깨짐)
- "좋은 fit = 진짜 생리학"으로 받아들이면 안 됨

---

<!-- SLIDE_START: M2 | title: tmax/Cmax -->
<!-- SECTION_CORE: SC-04 -->

## §2. Card 2 — $t_{max}$: 흡수 완료가 아니라 Rate Balance

### 🎯 이 카드의 치트키

**$t_{max}$는 "흡수가 가장 많이 끝난 시간"이 아님. $t_{max}$는 "$dC/dt = 0$이 되는 시간" — 즉, 흡수 속도와 소실 속도가 같아지는 순간임.** 한국말로는 "**순유입이 0이 되는 시점**"임 [R&T p.173; G&W pp.34–35].

### 왜 이게 중요한가

학생들이 가장 많이 잘못 외우는 게 "$t_{max}$ 도달 = 흡수 완료"임. **틀림.** $t_{max}$ 이후에도 흡수는 계속 진행 중임. 단지 소실이 더 빨라서 농도가 내려가는 것뿐임.

### 수식 도출

Master equation을 미분해서 $dC/dt = 0$으로 두면:

$$
\underbrace{\frac{dC}{dt}}_{\text{농도 기울기}}=\frac{\overbrace{k_a F D_{po}}^{\text{scale}}}{\underbrace{V(k_a-k_{el})}_{\text{scale}}}\left(\overbrace{-\underbrace{k_{el}e^{-k_{el}t}}_{\text{소실 기여}}+\underbrace{k_a e^{-k_a t}}_{\text{흡수 기여}}}^{\text{속도 균형}}\right)=\underbrace{0}_{\text{peak 조건}}
$$

$$
\underbrace{t_{max}}_{\text{peak 시간}}=\frac{\underbrace{\ln(k_a/k_{el})}_{\text{속도 로그비}}}{\underbrace{k_a-k_{el}}_{\text{속도 차}}}
$$

`[Source: G&W Eq.2:49–2:52, pp.34–35; R&T Eq.F-6, p.783]`

### 🔑 핵심 — 왜 $t_{max}$ 식에 $F$, $V$, $D$가 없는가?

$F$, dose, $V$는 곡선의 **높이를 위아래로 scale만** 함. **기울기가 0이 되는 시간 위치는 안 바꿈.** 그래서 linear 1구획에서:

- dose 또는 $F$ 변화 → $C_{max}$, $AUC$는 바뀌지만 **$t_{max}$는 그대로** [R&T Fig.6-5, p.174]
- $CL$ 변화 → $AUC$, $C_{max}$, $t_{max}$ 모두 같이 움직임
- $V$ 변화 → $C_{max}$, $t_{max}$가 서로 다른 방향으로 이동

→ **"$F$·dose만 변했을 때"의 패턴과 "disposition($CL/V$)이 변했을 때"의 패턴이 다름.** 이게 흡수 변화와 disposition 변화를 가르는 첫 단서임 [R&T Figs.6-10–6-11, pp.179–180].

### 🔑 한 줄 비유 — 저수지 수위

$t_{max}$는 **저수지 수위가 가장 높은 순간**임. 수도꼭지(흡수)로 들어오는 속도와 배수구(소실)로 빠지는 속도가 같아지는 시점임. **물이 다 들어온 시점이 아님.** linear 1구획에서는 $F$와 dose가 높이를 바꾸지만 $t_{max}$ 위치는 안 바꿈.

### $k_a \gg k_{el}$일 때

$$
\underbrace{C_{max}}_{\text{최고농도}}\approx \underbrace{\frac{F D_{po}}{V}}_{\text{도달량/부피}}\underbrace{e^{-k_{el}t_{max}}}_{\text{peak 전 소실}}
$$

`[Source: G&W Eq.2:53, p.35]`

Lag-time이 있으면 관찰 $t_{max}$는 $t_{lag}$만큼 뒤로 이동함 [G&W Eq.2:54–2:55, p.35].

### 잔차법 (Method of Residuals)

말기 직선 구간에서 $k_{el}$을 먼저 추정 → 그 직선을 역외삽해서 관찰 농도를 뺌 → 잔차 직선이 나옴 → 그 직선 기울기가 $-k_a$임. 두 직선의 교점은 lag-time 추정에 사용 [G&W pp.31–33; R&T Appendix F pp.781–783].

**중요한 함정:** 잔차법은 "**terminal slope가 진짜 elimination을 반영한다**"는 전제 위에 있음. **flip-flop 상황에서는 이 전제가 깨짐.**

### 💼 실무 인사이트

잔차법에서 **terminal point 선택은 눈대중이 아님.** 최소 3점 이상, log-linear fit이 충분히 좋게 떨어져야 함, $C_{max}$ 이후 충분히 늦은 시점이어야 함. 안 그러면 $k_a$와 $k_{el}$ 초기값이 서로 오염됨.

### 극한 — $k_a = k_{el}$

$$
\underbrace{C(t)}_{\text{한계 농도}}=\underbrace{\frac{k' F D_{po}}{V}}_{\text{입력 scale}}\underbrace{t}_{\text{시간항}}\underbrace{e^{-k't}}_{\text{공통 감쇠}}
$$

`[Source: G&W Eq.2:58, p.37]`

### Card 2 요약

- $t_{max}$는 **rate balance**의 시점임 (흡수 완료가 아님)
- linear 조건에서 $F$, dose, $V$는 $t_{max}$ 위치를 안 바꿈. $k_a$/$k_{el}$ 상대 크기만 정함
- 가장 흔한 오해 — "$t_{max}$ = 흡수 완료". 틀림. 흡수는 $t_{max}$ 이후에도 진행 중임

---

<!-- SLIDE_START: M3 | title: 생체이용률 F -->
<!-- SECTION_CORE: SC-05 -->

## §3. Card 3 — $F$: "얼마나 많이" vs $k_a$: "얼마나 빨리"

### 🎯 이 카드의 치트키

**$k_a$는 속도계(순간 속도), $F$는 적산계(누적 도달량).** 두 개를 섞는 순간 food effect / BE / formulation effect 해석이 다 무너짐. $F$를 "**$AUC$가 읽는 extent**"로 박아 놓으면 rate와 extent가 완전히 분리됨.

### 왜 이게 중요한가

"$AUC$ 변화 = 흡수속도 변화"라는 한 줄 — **이게 가장 위험한 혼동임.** extent와 rate를 섞는 순간 food effect 보고서, formulation 비교 보고서, BE 보고서 모두 실패함.

### 절대 생체이용률

IV reference가 있을 때:

$$
\underbrace{F}_{\text{절대 F}}=\underbrace{\frac{AUC_{po}}{AUC_{iv}}}_{\text{노출 비율}}\cdot\underbrace{\frac{D_{iv}}{D_{po}}}_{\text{용량 보정}}
$$

`[Source: G&W Eq.2:74, p.42; R&T Eq.6-11, p.183]`

전제: **두 투여 사이에 clearance가 같다**는 가정 [R&T p.183].

| 파라미터 | 단위 | 의미 | 변화 원인 |
|---|---:|---|---|
| $F$ | fraction | IV 대비 전신 도달 분율 | 흡수 분율, 장관·간 first-pass |
| $AUC_{po}$ | conc·time | 경구 후 총 노출 | $F$, dose, $CL$ |
| $AUC_{iv}$ | conc·time | IV 기준 총 노출 | dose, $CL$ |

R&T 예시: i.m. dose $F$ = 97%, oral solution $F$ = 46% — route별 extent 차이를 보여주는 anchor [R&T Table 6-1, p.183].

### 상대 생체이용률

IV 없이 두 혈관외 제형 A, B 비교:

$$
\underbrace{F_{rel}}_{\text{상대 F}}=\underbrace{\frac{AUC_B}{AUC_A}}_{\text{B/A 노출}}\cdot\underbrace{\frac{D_A}{D_B}}_{\text{용량 보정}}
$$

`[Source: R&T Eq.6-15, p.185]`

### 소변 데이터

요중 배설로도 $F$, $F_{rel}$, 신장 청소율 추정 가능. **단 미변화체 배설 분율 + 신장 처리가 비교 조건에서 일정**해야 함 [R&T Eq.6-18–6-21, pp.187–188].

### 기전적 $F$

$$
\underbrace{F}_{\text{전체 F}}\approx\underbrace{F_F}_{\text{흡수·제형}}\cdot\underbrace{F_G}_{\text{장관 생존}}\cdot\underbrace{F_H}_{\text{간 생존}}
$$

`[Source: R&T Ch.7 context, pp.197–220]`

$F$는 "용해되어 들어온 양"이 아니라 **장관 → 장벽 → 간을 차례로 통과한 결과**임.

### BE 맥락 — $F_{rel}$만 같으면 충분한가?

R&T는 시험/기준 ratio의 90% CI와 0.80–1.25 기준을 설명 [R&T Fig.6-13, p.183]. **핵심 질문:** $F_{rel}$이 같아서 $AUC$가 비슷해도, **$k_a$가 다르면 $C_{max}$·$t_{max}$가 다름.** extent와 rate는 항상 같이 봐야 함.

### Card 3 요약

- $F$ = extent, $k_a$ = rate. **절대 섞지 말 것**
- $AUC = F \cdot \text{Dose} / CL$. 단, oral-only에서는 $CL$이 아니라 $CL/F$가 추정됨
- "$AUC$ 변화 = 흡수속도 변화" 단정 → 위험. extent와 rate를 섞는 순간 망함

---

<!-- SLIDE_START: M4 | title: APEX V/F + Flip-flop -->
<!-- SECTION_CORE: SC-06 -->

## §4. Card 4 — APEX: $V/F$의 구조적 식별불가능성 + Flip-flop

### 🎯 이 카드의 치트키 — 챕터 전체의 중심

**경구 농도-시간 곡선 = (입력함수) ⊛ (F) ⊛ (disposition)의 합성곱임.**

세 가지가 합쳐져서 곡선이 만들어지므로, 같은 곡선이 서로 다른 조합으로 나올 수 있음. 이게 **$V/F$로 묶이는 이유, terminal slope label이 뒤집힐 수 있는 이유, fitted $k_a$가 실제 흡수가 아닐 수 있는 이유 — 이 세 가지를 한꺼번에 설명**해줌.

### 🚨 가장 중요한 한 줄

**좋은 OFV · 작은 RSE = "이 모델이 이 데이터를 잘 설명한다"는 뜻일 뿐임. "$V$와 $F$가 원리적으로 따로 추정 가능하다"는 뜻이 아님.**

→ **수치적 식별가능성(numerical identifiability)**과 **구조적 식별가능성(structural identifiability)**은 완전히 다른 문제임.

`[⚡ Apex Concept]`

### A. $V/F$가 분리 안 되는 진짜 이유 — 대수적 증명

Master equation을 다시 보면 $F$와 $V$는 **항상 $F/V$ 형태로만 등장함.**

위 식 ($\S1$ Card 1의 $C(t)$)에서 $F$와 $V$가 어디에 있는지 보면, $F/V$가 한 묶음으로만 나타남. 즉 **경구 단독으로는 $V/F$만 추정 가능**, clearance도 $CL/F$로 보고해야 함 [G&W p.32; R&T p.185].

$$
\underbrace{AUC}_{\text{전신 노출}}=\underbrace{\frac{F\cdot Dose}{CL}}_{\text{도달량/CL}}=\underbrace{\frac{Dose}{CL/F}}_{\text{경구 관찰형}}
$$

대수적으로는 같은 식이지만, **$AUC$만 봐서는 변화의 원인이 $F$인지 $CL$인지 가를 수 없음.**

| 파라미터 | 단위 | 의미 | 변화 원인 |
|---|---:|---|---|
| $V/F$ | volume | apparent volume | $V$ 변화 또는 $F$ 변화 |
| $CL/F$ | volume/time | apparent clearance | $CL$ 변화 또는 $F$ 변화 |
| terminal slope | time$^{-1}$ | 관찰 말기 감소율 | $k_{el}$ 또는 $k_a$ 병목 |
| $AUC$ | conc·time | 총 전신 노출 | $F \cdot Dose / CL$ |

### 🔑 한 줄 비유 — 안개 낀 유리창

**안개 낀 유리창 너머로 방의 크기와 창문이 얼마나 열려있는지를 동시에 추정해야 하는 상황임.** 방이 큰 건지($V$가 큰지) 창문이 덜 열린 건지($F$가 작은지) — 같은 농도 하나로는 가를 수 없음. **$V/F = 50\ \text{L}$라는 숫자는 절대 "$V = 50\ \text{L}$"라는 뜻이 아님.** IV나 absolute $F$ 근거 없이는 $V/F$, $CL/F$로 보고하는 게 맞음.

### R&T 저자의 4-part 결론 — 외워둘 것 [R&T p.185]

단일 oral dose만 있을 때:
1. **$AUC$ — 사다리꼴법으로 계산 가능**
2. **$CL$ — $F$를 모르므로 계산 불가**
3. **terminal half-life — 무엇이 rate-limiting인지 모르면 elimination/absorption 어느 쪽에도 확정 할당 불가**
4. **$V$ — 추정 불가**

이 네 줄이 Apex의 핵심 메시지임.

### B. Flip-flop — 실용적 식별불가능성

- 일반적: $k_a > k_{el}$ → 경구 말기 기울기는 **소실**을 반영
- **Flip-flop:** $k_a < k_{el}$ → 남은 흡수 과정이 더 느린 과정 → 관찰 말기 기울기는 **흡수**를 반영 [G&W Fig.2.17, p.30; R&T Case C, pp.175–176]

**핵심 경고:** "상승부 = 흡수, 하강부 = 소실" 라벨은 flip-flop에서 **통째로 뒤집힘** [G&W pp.29–30; R&T pp.173–176].

### C. 사례 앵커 — 외워둘 것

**1. Fluticasone propionate** (흡입 코르티코스테로이드)
- median $t_{max}$ 90분, $C_{max}$ 30–90분
- BUT 흡수 반감기는 **3.8–4시간**
- → **빠른 $t_{max}$가 빠른 흡수를 증명하지 않음**의 사례 [R&T Fig.6-7, p.177]

**2. Theophylline** (저추출 기관지확장제)
- 음식·물 같은 흡수 조건을 바꿔도 **말기 반감기는 약 6.3 hr로 유지**
- → **흡수 변화와 disposition 변화는 다르게 보인다**의 사례 [R&T Fig.6-8, p.178]

**3. Penicillin G** (난용성 근육주사 항생제)
- 난용성 제형은 흡수가 rate-limiting이 될 수 있음
- → **flip-flop이 일어나는 전형적 상황**의 사례 [R&T Fig.6-9, p.178]

**4. 장기지속형 주사 제형 (LAI/Depot) — flip-flop의 임상 끝판왕**
- **Sandostatin LAR Depot** (octreotide acetate, 매 4주)
- **Zolodex** (goserelin acetate implant, 매 3개월)
- **Mirena** (levonorgestrel-releasing IUD, 5년)

이런 modified-release 비경구 제형은 **흡수 자체가 수 주~수 년 단위로 율속**됨 [R&T p.170]. 관찰 terminal slope는 본질적으로 **흡수 속도상수**임 ($k_a < k_{el}$):

$$
\underbrace{\lambda_z}_{\text{관찰 terminal slope}} \approx \underbrace{k_a}_{\text{느린 흡수 ← 율속}} \ll \underbrace{k_{el}}_{\text{빠른 소실}}
\quad\Rightarrow\quad
\underbrace{t_{1/2,obs}}_{\text{관찰 반감기}} = \frac{\ln 2}{k_a}\;(\text{not}\;k_{el})
$$

NONMEM 구현: ADVAN2에서 매우 작은 KA를 두거나, ADVAN1+TRANS2에 시간 의존 입력으로 처리. → **terminal half-life를 "elimination half-life"로 보고하면 dose adjustment 판단이 완전히 어긋나는 가장 명확한 사례군**임.

**5. PK2 사례** [G&W p.480]
- lag-time model에서 $K_a = 0.043\ \text{min}^{-1}$, $K = 0.0088\ \text{min}^{-1}$, $V/F = 32\ \text{L}$, $t_{lag} = 16\ \text{min}$
- 같은 사례에서 $F = 82\%$, $\text{true}\ V = 20\ \text{L}$도 함께 제시됨
- 산술: $32 \times 0.82 \approx 26\ \text{L}$ — 원문 20 L와 맞지 않음

> 🔎 **충돌의 가능한 출처 가설**
>
> 원문 PK2의 V/F 추정은 solution별로 다름 — initial estimate 30 L, solution II, solution III 6.54 L [G&W pp.480–482]. F도 deconvolved 82%와 NCA 60–64% 두 값이 함께 제시됨. 가능한 출처 4가지:
> - (i) solution II의 V/F가 정확히 32 L가 아닐 가능성
> - (ii) F가 deconvolved 82%인지 NCA 60–64%인지에 따라 V 환산값 변동
> - (iii) 원문이 V ≈ 20 L로 반올림 보고
> - (iv) **IV reference의 dose range가 oral dose 영역과 다를 가능성** — linearity 위배 시 $F$ 산정에 systematic bias가 들어가고, 이게 그대로 $V = (V/F) \times F$ 환산에 흘러감
>
> $$
> \underbrace{V_{est}}_{\text{환산 V}}=\underbrace{(V/F)_{NLR}}_{\text{solution별 다름}}\times\underbrace{F_{?}}_{\text{NCA or deconv}}
> \quad\text{where}\quad F_{?} \in \{\overbrace{F_{NCA}}^{\sim 0.60-0.64},\;\overbrace{F_{deconv}}^{\sim 0.82}\}
> $$
>
> → 학습자가 모델링 보고서 검토 시 만나는 **"같은 사례 내 다른 추정 경로가 만드는 환산 충돌"**의 훈련용 사례임. 특히 NCA → NLR 전환 단계에서 가장 흔한 systematic bias 출처가 (iv)임.

**6. PK2 Solution III** [G&W pp.481–482]
- 역전된 초기 추정치가 다른 $k_a/k_{el}/V/F$ 해로 수렴
- → **flip-flop의 살아있는 증거**

**7. PK3** [G&W Table 3.1, p.486]
- 1차 모델: $K_a \approx K_e$, 큰 CV/RSE
- 0차 모델: AIC 더 낮음 (85.2 → 76.2)
- BUT **"better AIC ≠ 진짜 0차 흡수의 증명"**

### C-2. 가장 흔한 그럴듯한 오류

"$C_{max}$가 내려가고 $T_{max}$가 늘어났으니까 흡수가 느려진 거구나" → **이 단정이 위험함.**

이 단정 따라 가면:
- 제형 재조제 또는 transit compartment로 복잡화
- 만약 진짜 원인이 first-pass 증가, 용해도 저하, 또는 flip-flop이면 → **임상: 노출·독성·치료실패 예측이 통째로 어긋남.** **규제: IV/route comparison 없이 $F$와 $k_a$를 분리했다고 주장 → BE 의사결정 오류 → 재분석 요구.**

### D. NONMEM 보고 — 정직한 형식

경구 단독 PopPK에서는:
- **$F$를 1로 고정**
- **$V/F$, $CL/F$로 보고**

`F1`을 추정하거나 임의 값으로 고정한 다음 $V$·$CL$을 absolute 값처럼 보고하면 → **사전 가정이 추정된 파라미터처럼 보이는 위험.**

### 💼 실무 인사이트 — 세 가지 함정

① **쌍둥이 억제 (Twin Suppression)**
$k_a$·$k_{el}$의 두 해가 모두 그럴듯할 때 ETA(KA)와 ETA(KEL)가 서로 강하게 보상하면서 OFV가 안정되어 보임.

② **$V/F$ 드리프트 (V/F Drift)**
같은 covariate가 $V/F$와 $CL/F$에 비례적으로 들어가면 → **$F$-driven 변화 의심.** 진짜 분포·청소율 변화 아닐 수 있음.

③ **가상 분포용적 (Phantom Volume)**
$V/F$ 변화를 $V$ 변화로 그냥 보고. 핵심 식 기억할 것:
$$AUC = F \cdot \text{Dose} / CL = \text{Dose} / (CL/F)$$

### Card 4 요약

- 경구 단독은 $V$와 $F$를 **원리적으로 못 가림**
- flip-flop에서는 terminal slope도 $k_{el}$로 확정 불가
- **좋은 fit은 진짜 parameter의 증거가 아님**
- 정직한 보고 = $V/F$ + $CL/F$ + terminal slope ambiguity 명시
- "$V/F$ → $V$" 한 줄이 phantom volume interpretation을 만들어 → 임상 용량 오류 + 규제 재분석 요구

---

<!-- SLIDE_START: M5 | title: ka_app vs ka_true -->
<!-- SECTION_CORE: SC-07 -->

## §5. Card 5 — $k_{a,app}$ vs $k_{a,true}$: $k_a$ 자체를 의심하라

### 🎯 이 카드의 치트키

**장관 구획은 "출구가 두 개인 싱크대"임.** 하나는 전신 순환으로 가는 출구 ($k_{a,true}$), 다른 하나는 손실 출구 ($k_d$). **fitted $k_a$는 두 출구의 합**임.

$$
\underbrace{k_{a,app}}_{\text{겉보기 소실}}=\underbrace{k_{a,true}}_{\text{실제 흡수}}+\underbrace{k_d}_{\text{장관 손실}}
$$

`[Source: G&W Fig.2.24 and text, pp.40–41]`

$$
\underbrace{F}_{\text{도달 분율}}=\frac{\underbrace{k_{a,true}}_{\text{흡수 경로}}}{\underbrace{k_{a,true}+k_d}_{\text{전체소실}}}
$$

`[Source: G&W Eq.2:70, p.41]`

### 왜 이게 중요한가

fitted $k_a$가 변했다고 곧바로 "**흡수가 빨라/느려졌다**"고 보고하는 순간 — 장관 손실, 분해, site heterogeneity, food effect를 모두 단일 흡수속도로 뭉뚱그리는 **오독**이 됨.

### 진단의 키 — $AUC$가 같이 변했는가?

- **$AUC$가 변하지 않음** → onset/rate 변화 (extent 일정)
- **$AUC$도 같이 변함** → **extent 변화가 동반된 것**

`[Source: G&W pp.40–41]`

| 파라미터 | 단위 | 의미 | 변화 원인 |
|---|---:|---|---|
| $k_{a,app}$ | time$^{-1}$ | 장관에서 사라지는 전체 속도 | 실제 흡수 + 장관 손실 |
| $k_{a,true}$ | time$^{-1}$ | 전신 입력으로 이어지는 실제 흡수 속도 | 용출, 투과, 위배출 |
| $k_d$ | time$^{-1}$ | 장관 분해/손실 속도 | 불안정성, fecal loss, 장관 대사 |
| $F$ | fraction | 사라진 약물 중 전신 도달 분율 | $k_{a,true}/(k_{a,true}+k_d)$ |

### 다중 흡수 부위

흡수 부위가 여러 개면 곡선이 **다중 peak** 또는 **비정형 상승부**를 보임. buccal + GI 같은 구조는 G&W Eq.2:80–2:82로 제시됨 [G&W pp.46–47]. 이 경우 단일 $k_a$는 여러 입력 과정을 **하나로 눌러 담은 요약 파라미터**일 뿐임.

### D. 비선형 흡수 — Capacity-Limited Input

지금까지의 $k_{a,app}$ 분해는 **선형 1차 입력** 안에서의 이야기임. 흡수 자체가 **수송체 매개**일 때는 dose가 올라가면 $F$가 **dose-dependent하게 떨어지는** 또 다른 비선형성이 나타남.

**대표 사례: Gabapentin**
- L-amino acid transporter (LAT/OATP3)에 의한 능동 흡수
- transporter 포화 → $F$ 명시적 감소 [R&T p.203]

$$
\underbrace{\text{Input rate}}_{\text{유입속도}}=\underbrace{\frac{V_{max,abs}\cdot A_g}{K_{m,abs}+A_g}}_{\text{Michaelis-Menten 입력}}
$$

dose ↑ → $A_g$ ↑ → input rate가 $V_{max,abs}$ 근처에서 plateau → **$F$ 감소**

### 진단 신호 — 외워둘 것

**G&W §2.7.1 [G&W p.40]:** "**dose-normalized $AUC$ vs dose 그림이 dose 증가에 따라 *감소하는 직선*을 보이면, decreasing bioavailability / saturable input / zero-order input을 의심한다.**"

| 비선형성 종류 | 진단 신호 | 사례 |
|---|---|---|
| 선형 1차 + 장관 손실 ($k_d$↑) | $AUC$ 비례, $F$ 일정 | $k_a$ apparent ↑, extent 그대로 |
| Saturable absorption ($V_{max,abs}$ 포화) | dose-normalized $AUC$ ↓ at high dose | gabapentin (LAT/OATP3) [R&T p.203] |
| Saturable first-pass | $F$ ↑ at high dose | alprenolol, propranolol, verapamil [R&T Table 7-5, p.211] |
| Zero-order input | flat plateau, AIC 우월하나 IV 검증 필요 | PK3 [G&W pp.483–486] |

### ⚠️ 혼동 주의

dose-normalized AUC ↓ at high dose는 **saturable input뿐 아니라 decreasing $F$ / zero-order input과도 혼동**됨. IV 데이터 없이는 이 셋을 분리할 수 없음 — **G&W 원문 경고: "Unless intravenous dosing data are also available, zero-order input and capacity limited elimination confound each other"** [G&W p.40].

### 💼 실무 인사이트

Food effect 보고서에서 **"$k_a$ 감소 = 흡수 저하"라고 절대 쓰면 안 됨.**

올바른 보고:
- $F_{rel}$ ($AUC$ ratio)을 같이 보고
- $AUC$ 변화 없이 $k_a$만 바뀜 → **onset/rate 변화**
- $AUC$도 같이 바뀜 → **extent 변화**
- Dose escalation에서 $F$ 감소 → **transporter-mediated saturable absorption 의심** (superposition 위배 검사가 첫 진단)

### Card 5 요약

- fitted $k_a$가 변했으면 먼저 $k_{a,app} = k_{a,true} + k_d$ 구조를 의심할 것
- $AUC$ 변화 동반 여부가 rate 변화 vs extent 변화의 가르는 기준
- "$k_a$ 감소 = 흡수 저하" 단정 = 장관손실 + 다중흡수부위 + food effect를 모두 단일 흡수속도로 뭉뚱그리는 오독
- Dose escalation에서 $F$ ↓ → saturable absorption의 두 축 (extent 비선형 vs rate 분해)이 한꺼번에 보임

---

## §6. BCS·BDDCS — 수식 이전의 좌표계

### 🎯 이 섹션의 치트키

**약물 만나면 BCS class부터 묻기. 매트릭스 한 표로 식사효과·biowaiver·DDI 우선순위가 미리 정해짐. 수식 한 줄 쓰기 전에 답의 절반은 이미 결정됨.**

### A. BCS Class I–IV 매트릭스 [R&T Table 7-8, pp.219–220]

두 축: **용해도(solubility)**와 **장관 투과도(permeability)**.

| | High Permeability | Low Permeability |
|---|---|---|
| **High Solubility** | **Class I** | **Class III** |
| **Low Solubility** | **Class II** | **Class IV** |

용해도 기준: 최고 강도가 pH 1–7.5 범위에서 250 mL 물에 녹는가
투과도 기준: 장관 흡수 완전 또는 in vitro highly permeable

BCS는 **즉방형(immediate-release) 제형**에만 적용 (15분 내 85% 용출).

| Class | 특성 | 흡수 율속 | 식사 효과 | Biowaiver |
|---|---|---|---|---|
| **I** (high sol·high perm) | 빠른 용출·완전 흡수 | 위배출 | 일반적으로 작거나 무시 가능 | **가능** [R&T p.219] |
| **II** (low sol·high perm) | 용출 제한 | Dissolution | 고지방식이 → $F$↑ (담즙·미셀) | 불가 |
| **III** (high sol·low perm) | 투과도 제한 | Permeability | transit·transporter 영향 | 불가 (조건부) |
| **IV** (low sol·low perm) | 두 축 모두 제한 | 두 축 모두 | 변동성 큼 | 불가 |

**Class I 예시** [R&T Table 7-9, p.220]: acetaminophen, caffeine, diazepam, theophylline, metoprolol, propranolol, verapamil, valproic acid, midazolam, fluoxetine, levodopa, zidovudine 등. → **biowaiver 대상**임.

### B. BDDCS — Disposition까지 더한 보완

Benet 그룹의 BDDCS는 같은 두 축 + **disposition route** (대사 vs 미변화체 신/담즙 배설). Transporter 영향 예측까지 가능.

| BDDCS Class | BCS 등가 | Transporter 효과 |
|---|---|---|
| 1 | I | 수동확산 우세, transporter 영향 미미 |
| 2 | II | 장관 efflux (P-gp), intestinal metabolism 중요 |
| 3 | III | 장관 uptake transporter 의존, efflux도 큼 |
| 4 | IV | 모든 transporter 영향 가능 |

→ Card 5의 **gabapentin saturable absorption** (LAT/OATP3) = BDDCS Class 3의 전형. High solubility지만 low passive permeability라 능동 수송체에 의존, dose escalation에서 transporter 포화로 $F$ 감소.

### 💼 실무 인사이트 — BCS가 미리 답을 알려주는 자리

신약 개발 초기에 BCS class만 알아도 다음 의사결정의 절반이 정해짐:
1. **식사 효과 시험을 priority로 할지** → Class II·IV는 필수
2. **Biowaiver를 노릴지** → Class I만 가능
3. **Transporter DDI 시험을 어디까지 할지** → BDDCS Class 2·3 우선
4. **Controlled-release 개발 적합성** → Class I에 가장 적합 [R&T p.220]

**→ 모델링 한 줄로 풀 수 없는 답을 BCS는 한 표로 줌.**

### C. BCS와 Modified-Release 연결

Class I의 즉방형은 위배출 의존이지만, **non-disintegrating controlled-release**는 위배출 영향을 덜 받음 — 위에 머물러 있어도 약물은 계속 십이지장으로 빠져나감 [R&T p.220]. 다만 식사 습관·복약 시간 불일치 변동성, 그리고 대장 도달 후 (12–16 hr) 압축에 의한 release 신뢰성 저하가 한계임.

---

## §7. 1차 입력이 안 맞을 때 — Transit / Erlang / Weibull

### 🎯 이 섹션의 치트키

**1차 흡수로 fit 안 되고 lag-time이 비현실적으로 커지거나 sigmoidal rise가 보이면 → 1차 강제 적합 말고 transit/Weibull로 옮길 것.** Card 4의 식별가능성 논리가 그대로 이어짐 — 새 좌표계로 옮기는 순간 새 apparent parameter가 또 등장함.

> **출처 범위 노트:** 본 핸드아웃의 주 출처(G&W 5e Ch.2, R&T 5e Ch.6–7)는 transit/Erlang/Weibull을 명시적으로 다루지 않음. 이 섹션은 PopPK 실무에서 1차 흡수가 안 맞을 때의 확장 좌표계 개념 anchor이며, 정량 anchor는 외부 reference에 기댐.

### A. Transit Compartment / Erlang

흡수 부위에서 중심까지를 **n개의 직렬 통과 단계**로 모델링:

$$
\underbrace{\frac{dA_i}{dt}}_{\text{i단계 변화}} = \underbrace{k_{tr}\cdot A_{i-1}}_{\text{직전 유입}} - \underbrace{k_{tr}\cdot A_i}_{\text{다음 유출}}
\quad(i=1,2,\ldots,n)
$$

마지막 transit의 입력:

$$
\underbrace{\text{Input}_{\text{central}}(t)}_{\text{중심구획 유입}} = \underbrace{F\cdot D\cdot \frac{(k_{tr}\,t)^n\, e^{-k_{tr}\,t}}{n!}\cdot k_{tr}}_{\text{Erlang(n+1, k}_{tr}\text{) 분포 곡선}}
$$

특성:
- **NTR = 1** → 1차 흡수와 동일 ($k_a = k_{tr}$)
- **NTR ≫ 1** → sigmoidal 입력 + 자연스러운 lag (별도 $t_{lag}$ 불필요)
- **Mean Transit Time:**

$$
\underbrace{MTT}_{\text{평균 통과시간}} = \underbrace{\frac{n+1}{k_{tr}}}_{\text{n개 chain 누적시간}}
$$

`[참고 — 출처 범위 밖: Savic RM, Jonker DM, Kerbusch T, Karlsson MO. J Pharmacokinet Pharmacodyn 2007;34(5):711–726.]`

### B. Weibull — 서방형·용해도 제한

누적 흡수 분율:

$$
\underbrace{F(t)}_{\text{누적 흡수분율}} = 1 - \exp\!\left[-\overbrace{\left(\frac{t}{T_d}\right)^\beta}^{\text{Weibull power-law}}\right]
$$

순간 입력률:

$$
\underbrace{\frac{dF}{dt}}_{\text{순간 흡수율}} = \underbrace{\frac{\beta}{T_d}\left(\frac{t}{T_d}\right)^{\beta-1}}_{\text{shape × scale}}\cdot\underbrace{\exp\!\left[-\left(\frac{t}{T_d}\right)^\beta\right]}_{\text{지수 감쇠}}
$$

특성:
- **β < 1**: 초반 빠른 release, 점차 둔화 (burst release)
- **β = 1**: 1차 흡수와 등가 ($k_a = 1/T_d$)
- **β > 1**: sigmoidal release (controlled-release, osmotic pump)

`[참고 — 출처 범위 밖: Langenbucher F. J Pharm Pharmacol 1972;24(12):979–981.]`

### C. 어느 모델을 언제 쓰는가 — 진단표

| 곡선 특징 | 1차 적합 시 증상 | 권장 입력 |
|---|---|---|
| step function처럼 lag 후 시작 | lag-time이 비현실적으로 커짐 | Transit (NTR 작은 정수) |
| 흡수 시작이 점차 가속 (sigmoidal rise) | $k_a$가 작은 값에 고착, residual 증가 | Transit (NTR 큰 값) or Weibull (β > 1) |
| Modified-release release shape 어긋남 | poor fit at multiple time points | Weibull (β fit) |
| 다중 peak / 비정형 상승부 | OFV 안정되나 잔차 패턴 이상 | Multiple absorption sites [G&W pp.46–47] |
| Dose escalation에서 곡선 형태 변화 + dose-normalized AUC ↓ | 1차 모델 점점 안 맞음 | Card 5 §D saturable input |

### 💼 실무 인사이트 — Transit과 Lag의 Trade-off

같은 sigmoidal 시작을 **lag로 잡을 수도, transit으로 잡을 수도** 있음. 두 파라미터를 동시 추정하면 식별가능성 떨어짐. **일반적으로 lag = 0 고정 + transit으로만 흡수 시작 잡는 게 안전**한 경우가 많음.

$$
\underbrace{\text{Lag model}}_{\text{step function 시작}}: t < t_{lag} \Rightarrow C=0
$$

$$
\underbrace{\text{Transit chain}}_{\text{sigmoidal 시작}}: \underbrace{MTT}_{(n+1)/k_{tr}}\text{ 와 } \underbrace{NTR}_{\text{chain 길이}}\text{ 가 } t_{lag}\text{와 confounded}
$$

→ Card 4의 식별가능성 논리 그대로 이어짐 — 새 좌표계로 옮기는 순간 새 apparent parameter ($k_{tr}$, NTR, $T_d$, β) 등장.

---

## §8. 혼동쌍 5종 세트 — 라벨이 뒤집히는 순간

다섯 개 카드 끝났으니 임상·PopPK 보고서에서 가장 자주 라벨이 뒤바뀌는 다섯 페어를 정리. **같은 숫자라도 라벨이 바뀌면 임상 결론이 완전히 달라짐.**

### 혼동쌍 1. $k_a$ vs $k_{el}$ under Flip-flop — **결정타**

| 기준 | $k_a$ | $k_{el}$ |
|---|---|---|
| 단위 | time$^{-1}$, 흡수부위 소실 | time$^{-1}$, 중심구획 소실 |
| 위치 | $e^{-k_a t}$ input 지수 | $e^{-k_{el}t}$ disposition 지수 |
| 원인 | 용출, 위배출, 흡수부위 | $CL/V$, 신/간 기능 |
| 혼동 결과 | flip-flop terminal slope label 오류 | dosing interval, accumulation, washout 오류 |

**⚡ 기억 고리 — 어느 쪽이 병목인가:**
- Flip-flop: $k_a < k_{el}$ → **흡수가 병목** → terminal slope = $k_a$
- Disposition-limited: $k_{el} < k_a$ → **제거가 병목** → terminal slope = $k_{el}$
- **IV crossover 없이는 두 메커니즘을 가를 수 없음** ← 결정적 함정

**⚡ 기억 고리 — 정점 시각 vs 흡수 종료 시각:**
$T_{max}$ = 흡수 속도와 제거 속도가 같아지는 **교차점**. **흡수 완료 시점이 아님.** $T_{max}$ 이후에도 흡수는 계속, 단지 제거가 더 빠를 뿐.

### 혼동쌍 2. $F$ vs $k_a$ — extent vs rate

| 기준 | $F$ | $k_a$ |
|---|---|---|
| 단위 | fraction, 전신 도달 분율 | time$^{-1}$, 흡수부위 소실 |
| 위치 | $F\cdot Dose/CL$ scale | 지수항 + $t_{max}$ rate term |
| 원인 | 흡수 분율, first-pass, 제형 | 용출, 위배출, 흡수부위 |
| 혼동 결과 | AUC·peak timing 원인 혼동 | food/formulation effect 오류 |

$$
\underbrace{\frac{k_a}{K}}_{\text{속도 비율}}=\underbrace{\frac{k_a}{CL\cdot V}}_{\text{원문대비}}
$$

**⚡ 기억 고리 — 속도계 vs 적산계:**
$k_a$ = 속도계 (순간 속도). $F$ = 적산계 (누적 도달량). **$k_a$를 키워도 $F$가 그대로면 $AUC$는 그대로.**

### 혼동쌍 3. $V/F$ vs $V$ — **결정타**

| 기준 | $V/F$ | $V$ |
|---|---|---|
| 단위 | volume, apparent | volume, true distribution |
| 위치 | oral-only 보고, $F$와 묶임 | IV 또는 $F$ 근거 필요 |
| 원인 | $V$ 변화 또는 $F$ 변화 | 조직분포, 체성분, 단백결합 |
| 혼동 결과 | $F$ 변화가 분포 변화처럼 보임 | phantom interpretation, covariate 오류 |

**결정타:** $V/F$를 $V$로 바꿔 쓰는 순간 → **흡수율 변화가 분포용적 변화처럼 보이는 phantom interpretation 발생.**

### 혼동쌍 4. First-order $k_a$ vs Zero-order Input

| 기준 | First-order $k_a$ | Zero-order Input |
|---|---|---|
| 단위 | time$^{-1}$, 잔량 비례 | amount/time, 일정 입력 |
| 위치 | $e^{-k_a t}$ 지수 | 일정 입력률, 종료 후 washout |
| 원인 | 속방형 용액/정제, 용출·위배출 | controlled-release, 삼투펌프 |
| 혼동 결과 | 0차 모델 better fit을 진짜 0차 흡수로 과장 | PK3처럼 AIC 우월이 기전 증명을 뜻하지 않음 [G&W pp.483–486] |

### 혼동쌍 5. Linear vs Saturable Absorption

| 기준 | Linear 1st-order | Saturable |
|---|---|---|
| 단위 | $k_a$ (time$^{-1}$), dose 비례 | $V_{max,abs}/K_{m,abs}$ (M-M) |
| 위치 | $-k_a A_g$ | $-V_{max,abs}\cdot A_g/(K_{m,abs}+A_g)$ |
| 원인 | 수동확산, 용출/위배출 | 능동 수송체 (LAT, PEPT1, OATP) 포화 |
| 진단 신호 | dose-normalized $AUC$ 일정 | dose-normalized $AUC$ ↓ at high dose [G&W p.40] |
| 사례 | 대부분의 small-molecule | gabapentin (LAT/OATP3) [R&T p.203], L-dopa, amoxicillin |
| 혼동 결과 | dose escalation 노출 예측 정상 | dose↑에서 $C_{max}$ plateau, 치료실패 + BE 오류 |

**⚡ 기억 고리 — Superposition 검사:**
Dose 2배 → $AUC$가 2배 안 나오면 비선형 의심.
- **dose-normalized $AUC$ ↓ at high dose** → saturable input / decreasing $F$ / zero-order input 중 하나 (셋은 IV 없이 분리 불가 [G&W p.40])
- **dose-normalized $AUC$ ↑ at high dose** → saturable first-pass [R&T Table 7-5, p.211]

### §8 요약

경구 PK에서 가장 위험한 혼동은 **slope label · apparent parameter · rate/extent**를 서로 바꿔 부르는 것임. 이름표가 바뀌면 같은 숫자도 다른 임상 결론을 만듦. 그리고 5번째 — **linear vs saturable absorption은 dose range를 확장할 때 가장 먼저 깨지는 가정**임.

---

## §9. 자기 테스트 — 능동 회상 9문항

### Q1. Master equation을 쓰고 각 항의 의미를 설명할 것

$$
\underbrace{C(t)}_{\text{혈장 농도}}=\frac{\overbrace{k_a F D_{po}}^{\text{전신 입력}}}{\underbrace{V(k_a-k_{el})}_{\text{희석·분리}}}\left(\underbrace{e^{-k_{el}t}}_{\text{소실 지수}}-\underbrace{e^{-k_a t}}_{\text{흡수 지수}}\right)
$$

$k_a$ = 흡수부위 소실 속도, $F$ = 전신 도달 분율, $D_{po}$ = 투여량, $V$ = 분포용적, $k_{el}$ = 소실 속도. 괄호 안 = 소실 지수와 흡수 지수의 차이 [G&W p.30; R&T p.782].

### Q2. 왜 $t_{max}$ 식에 $F$, $V$, dose가 없는가?

$t_{max}$는 $dC/dt = 0$이 되는 시점. linear system에서 $F$·$V$·dose는 곡선의 높이만 scale, 기울기가 0이 되는 시간 위치는 안 바꿈. $t_{max} = \ln(k_a/k_{el})/(k_a - k_{el})$ [G&W p.35].

### Q3. $F_{rel} = 1.0$인 두 oral formulation이 임상적으로 완전히 같은가?

**아님.** $F_{rel} = 1.0$ = extent가 같다는 뜻일 뿐. $k_a$가 다르면 $C_{max}$·$t_{max}$가 다름. onset이나 peak-related safety가 중요한 약물에서는 임상적 차이가 분명히 남음 [R&T pp.181–183].

### Q4. PK2에서 $V/F = 32\ \text{L}$, $F = 0.82$일 때 진짜 $V$는?

산술: $V = 32 \times 0.82 \approx 26\ \text{L}$. **단** 원문은 $\text{true}\ V = 20\ \text{L}$로 서술 — 산술값과 충돌. 본 handout은 26 L를 확정값으로 쓰지 않고 "원문 수치 충돌 [확인 필요]"로 표시 [G&W p.480].

$$
\underbrace{V}_{\text{true V}}=\underbrace{(V/F)}_{\text{apparent V}}\times\underbrace{F}_{\text{F 보정}}=\underbrace{32\times0.82}_{\text{산술 환산}}\approx\underbrace{26\ \text{L}}_{\text{계산 V}}
$$

> 🔎 **충돌 가설:** PK2는 동일 사례 안에서 V/F가 *initial estimate*(30 L), *solution II*, *solution III*(6.54 L)별로 다름. F도 *deconvolved*(82%) vs *NCA*(60–64%) 두 값이 함께 [G&W pp.480–482]. **추가 가설:** IV reference dose range가 oral dose 영역과 다르면 F 산정에 linearity violation systematic bias가 들어가고, 그게 V 환산값으로 흘러감:
>
> $$
> \underbrace{V_{est}}_{\text{환산 V}}=\underbrace{(V/F)_{NLR}}_{\text{solution별 다름}}\times\underbrace{F_{ref}}_{\text{NCA vs deconv}}
> $$
>
> → 학습자가 모델링 보고서 검토 시 만나는 진단 훈련 사례임. **IV reference의 dose linearity가 F 산정에 sneaky하게 들어간다**는 점이 핵심.

### Q5. Oral-only fit에서 $k_a = 0.05\ \text{hr}^{-1}$, $k_{el} = 0.5\ \text{hr}^{-1}$. 관찰 terminal half-life를 $\ln 2 / 0.5 = 1.4\ \text{h}$로 써도 되는가?

**안 됨.** $k_a < k_{el}$ → 관찰 terminal slope가 더 작은 $k_a$를 따를 수 있음. 따라서 terminal half-life는 약 $\ln 2 / 0.05 = 13.9\ \text{h}$로 나옴. $k_{el} = 0.5$가 진짜 elimination일 가능성도 있지만 **oral-only로는 확정 불가.**

$$
\underbrace{t_{1/2,obs}}_{\text{관찰 반감기}}=\frac{\underbrace{\ln 2}_{\text{반감기 상수}}}{\underbrace{0.05}_{\text{병목}}}\approx\underbrace{13.9\ \text{h}}_{\text{flip-flop}}
$$

### Q6. PK3에서 zero-order model의 AIC가 first-order보다 낮음. "진짜 0차 흡수"라고 결론 가능?

**불가.** PK3는 zero-order input model이 해당 dataset을 더 잘 설명한다는 것만 보여줌. 진짜 기전 확정은 용량 범위, 반복 투여, IV 데이터 같은 추가 evidence 필요 [G&W pp.483–486].

### Q7. $k_{a,app} = 1.0\ \text{hr}^{-1}$, $k_d = 0.4\ \text{hr}^{-1}$일 때 $k_{a,true}$와 $F$는?

$k_{a,true} = 1.0 - 0.4 = 0.6\ \text{hr}^{-1}$.

$$
\underbrace{F}_{\text{도달 분율}}=\frac{\underbrace{k_{a,true}}_{\text{흡수 }0.6}}{\underbrace{k_{a,true}+k_d}_{\text{전체 }1.0}}=\underbrace{0.6}_{\text{60\% 도달}}
$$

G&W Eq.2:70의 구조 그대로 적용. **실데이터에서는 $k_d$를 별도 evidence 없이 분리하기 어려움** [G&W p.41].

### Q8. Boss Dilemma — terminal slope $0.18\ \text{hr}^{-1}$, alternative model로는 $k_{el} = 0.69\ \text{hr}^{-1}$도 가능. 무엇을 보고할 것인가?

관찰 terminal half-life = $\ln 2 / 0.18 \approx 3.85\ \text{h}$. **단** flip-flop 가능성이 있으면 0.18이 $k_{el}$인지 $k_a$인지 확정 불가.

**안전한 보고:** "Oral-only data에서 terminal slope는 $0.18\ \text{hr}^{-1}$로 관찰되었으나, IV 또는 route·formulation comparison 없이는 이를 elimination rate로 확정할 수 없다. Dose recommendation은 두 해석에 대한 sensitivity analysis로 방어한다."

$$
\underbrace{t_{1/2,terminal}}_{\text{말기 반감기}}=\frac{\underbrace{\ln 2}_{\text{반감기 상수}}}{\underbrace{0.18\ \text{hr}^{-1}}_{\text{obs slope}}}\approx\underbrace{3.85\ \text{h}}_{\text{계산 반감기}}
$$

### Q9. 단회 경구 dose escalation: 100 mg에서 AUC = 50, 300 mg에서 AUC = 100, 900 mg에서 AUC = 150 mg·h/L. 진단은?

Dose-normalized AUC:

$$
\underbrace{\frac{AUC}{Dose}}_{\text{용량보정 노출}}=\begin{cases}\underbrace{0.50}_{\text{100 mg}}\\ \underbrace{0.33}_{\text{300 mg}}\\ \underbrace{0.17}_{\text{900 mg}}\end{cases}\ \text{h/L}
$$

**dose ↑일수록 dose-normalized AUC ↓** → G&W §2.7.1 진단 신호 정확 부합 [G&W p.40]: **decreasing bioavailability / saturable input / zero-order input 중 하나** (IV 없이 분리 불가). Gabapentin 같은 transporter-mediated absorption (LAT/OATP3) 의심되면 saturable input 가설 우선 검증 [R&T p.203].

→ **반대 패턴** (dose↑에서 dose-normalized AUC ↑)이 나오면 **saturable first-pass metabolism** [R&T Table 7-5, p.211] — alprenolol, propranolol, verapamil이 대표.

---

## §10. ⚡ 보스 딜레마 캡스톤 — 제형 변경 후 $C_{max}$↓ · $T_{max}$↑

### 시나리오

경구 단독 Phase 1 결과에서 $C_{max}$ 내려가고 $T_{max}$ 늘어남. 제형 팀은 "**흡수가 느려졌다 ($k_a$ 감소)**"고 결론. 모델러 입장에서는 **방어 가능한 해석이 두 개** 있음.

### 두 가지 해석

**(A) $k_a$ 감소 해석**
- absorption model을 first-order → transit compartment로
- $T_{max}$ 지연 재현에 집중

**(B) $F$ 감소 해석**
- first-pass 효율 감소 또는 apparent $CL$ 증가 → $AUC$ 감소
- $F$에 영향을 주는 공변량 탐색 우선

### 거장의 절충 판단

**(A)의 약점:**
- 모델 복잡도 ↑하면서 $T_{max}$ 재현에 집중
- BUT IV 없이는 $F$와 $k_a$의 confounding 풀 수 없음 (Card 4 합성곱 관점)
- 보고: **"transit compartment가 $T_{max}$ 지연을 더 잘 설명하지만, $F$ 동시 변화 가능성을 본 데이터로 배제할 수 없다"**

**(B)의 약점:**
- 파라미터 수는 단순하게 두지만, $k_a$ 변화가 진짜 원인이었으면 $AUC$ 자체와 곡선 형태가 어긋날 수 있음
- 보고: **"$AUC$ ratio가 유의하게 감소해서 $F$-driven 해석을 지지하지만, $k_a$ 변화 가능성을 sensitivity analysis로 평가했다"**

### 규제 방어 — 어떻게 가르는가

> **1단계.** "$AUC$가 같은가, 다른가"로 가설 분리
> - $AUC$ 변화 없음 + $C_{max}$↓·$T_{max}$↑ → **(A) $k_a$ 감소가 우세**
> - $AUC$ 감소 + $C_{max}$↓·$T_{max}$↑ → **(B) $F$ 감소**, 또는 **(A+B) 복합**
>
> **2단계.** IV crossover 요청, 안 되면 **두 모델 모두 적합 + sensitivity analysis 명시**
>
> **3단계.** 단일 가설 채택 금지. **"두 해석 모두 데이터와 정합적이며, 임상 dosing이 두 해 모두에서 안전 영역인가"** 평가

### ⚠️ 가장 위험한 자세

**"$k_a$ 감소 = 흡수 불량 = 제형 재조제"**라는 단순 추론. Card 4의 그럴듯한 오류 단락이 경고한 함정이고, BE trial의 의사결정 사슬을 잘못 만듦.

### §10 요약

계산보다 중요한 건 **라벨**임. 같은 숫자라도 $k_a$인지 $k_{el}$인지, $V$인지 $V/F$인지를 잘못 붙이면 임상 결론이 통째로 달라짐.

---

## §11. 메타프레임 — 한 바느질로 꿰기

### A. 이 세션의 위치

IV bolus 이후 첫 임상 현실 — **흡수 단계가 들어있는 계.** 다회투여·modified-release·food effect·BE·PopPK 흡수 모델로 가더라도, 판단 기준은 결국 네 질문으로 회귀:

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| 입력 함수가 1차 아님 | $k_a$, lag, input duration | → | $C_{max}$·$t_{max}$ 재현 실패 | lag/zero-order/transit 후보 평가 |
| $F$가 제형·식사·first-pass로 변함 | $F$, $CL/F$ | → | AUC + apparent clearance 변화 | $F_{rel}$, AUC ratio, sensitivity |
| Terminal slope label 불명확 | $k_a$ 또는 $k_{el}$ | → | 반감기·축적 판단 오류 | IV/route comparison or dual-solution 방어 |
| $V$, $CL$을 absolute처럼 보고 | $V/F$, $CL/F$ | → | covariate 오해 | apparent parameter 명시 |
| Dose 비례성 위배 | 흡수·대사·배설 비선형 | → | dose escalation 예측 실패 | dose-normalized AUC 진단 [G&W p.40] |

### B. 의존성 — 놓치면 어떻게 무너지는가

| 실패 모드 | 실제 결과 |
|---|---|
| $V/F$ → $V$로 보고 | covariate를 분포 변화로 오해 |
| $CL/F$ → $CL$로 보고 | $F$ 변화가 clearance 변화처럼 보임 |
| 말기 기울기 = $k_{el}$로 단정 | flip-flop에서 반감기·축적 오류 |
| $k_a$ 변화 = extent 변화로 단정 | food/formulation effect 메시지 오류 |
| $t_{max}$의 dose 의존성 무시 | 포화성 흡수·초회 통과 포화·비선형 소실 신호 누락 |
| 0차 모델 better AIC = 기전 증명으로 단정 | 서방형·용해도 근사를 생리학적 확정으로 과장 |
| Dose escalation superposition 위배를 noise로 처리 | saturable absorption/first-pass 신호 누락 |

### C. 전문가가 실제로 보는 지점

> 💼 **30년 차 pharmacometrics 연구자가 경구 모델 결과를 볼 때 가장 먼저 묻는 질문은 "모델이 맞았는가?"가 아님. "무엇이 식별되었는가?"임.**
>
> Phase 1 SAD(단회 상승 용량) 회의에서 senior가 던지는 질문은 단순함 — **"FIH(최초 임상 투여) 단계에서 IV arm이나 absolute $F$ 확인 가능성을 평가했는가?"** 이 한 줄의 질문이 $F$, $V/F$, $CL/F$, flip-flop, $k_{a,app}$의 모든 위험을 앞으로 끌어냄.

### D. 후속 세션 — 이 세션에서 무엇이 열리는가

| 후속 | 이 세션에서 열리는 개념 | 없으면 실패하는 것 |
|---|---|---|
| Multiple dosing / accumulation | terminal slope label, $k_{el}$ vs $k_a$ | 축적계수·washout 해석 오류 |
| Modified-release / zero-order input | input function 구분 | better fit을 기전 증명으로 과장 |
| Oral PopPK absorption | $V/F$, $CL/F$, $k_{a,app}$ | apparent를 true로 보고 |
| BE / food effect | rate vs extent 분리 | $AUC$, $C_{max}$, $t_{max}$ 메시지 혼동 |
| Nonlinear absorption / TDM | superposition test, dose-normalized AUC | saturable input/first-pass 누락 |

### E. Ch.7 맥락 — $k_a$와 $F$의 변동성은 어디서 오는가

BCS, 위배출, 용출, 수송체, 장관·간 초회 통과 같은 생리·물리화학적 요인. 이 세션의 수식들은 그 복잡성을 **1차 입력과 $F$라는 두 개의 apparent 축**으로 한꺼번에 다루는 첫 단계임 [R&T pp.197–220].

> 📖 **G&W p.47 Fig.2.32:** 경구 농도-시간 곡선을 정하는 요인들이 chapter conclusion 수준에서 하나의 구조로 다시 묶임 — 모든 카드가 어떻게 한 그림 안에 들어가는지 보여주는 클로징 다이어그램임.

### F. 최종 한 줄 — 외워둘 것

**경구 PK의 핵심은 $C(t)$를 잘 맞추는 데서 끝나지 않음.**

더 중요한 건 — **$C(t)$에서 실제로 분리 가능한 것과 분리 불가능한 것을 정직하게 가르는 일.**

경구 단독 데이터는 다음 네 가지를 남김:
1. $V/F$
2. $CL/F$
3. 겉보기 $k_a$
4. Terminal slope ambiguity

**이 네 가지를 명시하면 handout은 안전. 생략하면 모델은 그럴듯하지만 위험.**

그리고 마지막 두 축:
- **BCS/BDDCS는 수식 이전에 약물의 물리화학적 좌표가 답의 절반을 미리 결정한다**는 사실의 framework
- **Transit/Erlang/Weibull은 1차 입력 가정이 깨질 때 다음 좌표계가 어디인지** 알려주는 확장 framework

---

## 📌 부록 — 한 페이지 치트시트

### 보고서에 절대 쓰면 안 되는 다섯 문장

1. ❌ "V/F = 50 L → V = 50 L"
2. ❌ "CL/F = 10 L/hr → CL = 10 L/hr"
3. ❌ "Terminal slope = elimination rate"
4. ❌ "ka 감소했으므로 흡수가 저하됨"
5. ❌ "AIC가 더 좋으므로 0차 흡수가 맞음"

### 보고서에 항상 같이 봐야 할 다섯 쌍

1. ✅ AUC 변화 ↔ Cmax/tmax 변화 (extent vs rate 가르기)
2. ✅ Dose 변화 ↔ Dose-normalized AUC 변화 (linearity 검사)
3. ✅ Terminal slope ↔ flip-flop 시나리오 (IV crossover 있나?)
4. ✅ V/F · CL/F ↔ covariate (F-driven인지 확인)
5. ✅ Fitted ka ↔ AUC 동반 변화 (ka,app 분해 의심)

### Phase 1 senior가 던질 한 줄

> **"IV arm이나 absolute F 확인 가능성을 평가했는가?"**

이 한 줄을 미리 답할 수 있으면 이 챕터를 완전히 체화한 것임.

---

*이 문서는 v4.0 보강본_final의 콘텐츠를 보존하면서 narrative flow와 학습 효율성을 위해 재구성한 remastered edition임. 모든 출처 표기, 수식 annotation, SLIDE_START 마커, 약물 사례, 수치 anchor는 원본과 동일하게 유지됨.*

**Document ID:** C-260518-064237-9XQ

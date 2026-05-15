# 03 — 경구(혈관외) PK: F · ka · tmax · 흡수 — v3.8

## 임상 장면: 같은 AUC ratio, 다른 결론

R&T 예시에서 i.m. 투여의 $F$는 97%, oral solution의 $F$는 46%로 제시됩니다 [R&T Table 6-1 / Fig.6-14, pp.183–184]. 이 숫자를 "oral 흡수가 느리다"로 읽는 순간 rate($k_a$)와 extent($F$)가 섞입니다. 더 위험한 건 경구 단독 자료에서 $V/F$, $CL/F$, terminal slope를 각각 $V$, $CL$, $k_{el}$처럼 보고하는 경우입니다. 이 세션은 그 한 줄의 보고 문장이 어떻게 임상·규제 판단을 흔드는지 보여줍니다.

> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** 경구 PK는 식 암기가 아니라 $C(t)$·$F$·$k_a$·$V/F$·flip-flop에서 무엇이 식별되고 무엇이 가정인지 가르는 훈련입니다.

---

## 출처 및 범위 노트

> **Source A (G&W):** Gabrielsson & Weiner 5e, Ch.2 §§2.2.4–2.2.12 (pp.28–47), PK2 (pp.476–482), PK3 (pp.483–486)
> **Source B (R&T):** Rowland & Tozer 5e, Ch.6 (pp.169–195), Ch.7 (pp.197–220; context only), Appendix F (pp.781–784)
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
| Ch.7 흡수 생리학 / BCS | §8 | BCS·위배출·초회 통과를 흡수 변동성의 배경으로만 [R&T pp.197–220]. |
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
카드 1 (M1): 경구 농도곡선은 왜 두 지수함수의 차이로 생기는가?
카드 2 (M2): 최고농도 시점은 왜 "흡수 완료"가 아니라 rate balance인가?
카드 3 (M3): $F$는 왜 속도가 아니라 전신 도달 정도인가?
카드 4 (M4): 경구 단독 데이터는 왜 $V$, $CL$, terminal slope label을 확정하지 못하는가?
카드 5 (M5): 적합된 $k_a$는 왜 실제 흡수속도가 아닐 수 있는가?

### 핵심 아이디어(Big Idea)

IV bolus에서는 약물이 투여 직후 전신 순환에 들어와 **초기 농도 $C_0$**를 만듭니다. 경구/혈관외에서는 농도가 0에서 시작해 흡수와 소실이 경쟁하며 **두 지수함수의 차이로 된 곡선**이 만들어집니다. 그래서 $F$와 $V$는 $V/F$로 묶이고, $k_a$와 $k_{el}$은 terminal slope 해석에서 서로 뒤바뀔 수 있습니다. 같은 dose 기준 비교에서 흡수 단계가 끼어드는 순간 oral 곡선의 peak는 IV bolus 대비 낮아지고 시점도 뒤로 밀립니다 — 흡수는 "늦게 들어오는 것"이 아니라 peak의 높이와 시점을 동시에 다시 정하는 단계입니다 [R&T Fig.6-3, p.172].

### 한 줄 항법도

```
C(t) Master Equation
  → tmax/Cmax: 흡수속도 = 소실속도
  → F: 흡수 extent는 AUC로 본다
  → V/F + flip-flop: 경구 단독 데이터의 식별 한계
  → ka,app vs ka,true: 적합된 ka가 흡수인가 장관 손실인가
```

📍 **선행·후속**
• **선행**: IV bolus 1구획 PK($CL$, $V$, $t_{1/2}$, $AUC$), 1차 ODE, 지수함수, AUC 사다리꼴법.
• **직후**: multiple dosing, accumulation, two-compartment oral, transit/Erlang/Weibull input, modified-release, BE.
• **실무 연결**: NONMEM ADVAN2/ADVAN4, oral PopPK reporting, food effect, formulation effect, flip-flop 검증.

**§1 요약:** 식 암기가 아닙니다. oral curve에서 "무엇이 실제로 식별되는가"를 자동으로 의심하는 눈을 만드는 게 목표입니다.

---

<!-- SLIDE_START: §2 | title: 개념 해부 카드 -->
<!-- SECTION_CORE: SC-02 -->

## §2. 개념 해부 카드

> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** $C(t)$ Master Equation은 장관 입력과 중심 소실의 직렬 ODE가 만든 차이지수 곡선 — $F$, $V$, $k_a$, $k_{el}$의 이름표를 여기서부터 따로 떼어 놓아야 합니다.

---

<!-- SLIDE_START: M1 | title: C(t) Master Equation -->
<!-- SECTION_CORE: SC-03 -->

### Card 1. $C(t)$ Master Equation — 경구 PK가 시작되는 한 줄

> **앞 카드에서 이 카드로**
> IV bolus에서는 $C_0$가 즉시 만들어졌습니다. 경구에서는 농도가 0에서 시작해 흡수와 소실이 경쟁하며 곡선이 만들어집니다 — 그 곡선의 정체부터 풉니다.

> **거장의 시각**
> 경구 1구획 모델을 단일 곡선으로만 보면 상승부와 하강부의 이름표를 잘못 붙입니다. $C(t)$를 **장관 입력과 중심 소실이 직렬로 만든 두 지수함수의 차이 신호**로 읽어야 합니다 — 상승부는 흡수가 아직 남아 있다는 신호, 하강부가 항상 소실만의 신호인 것은 아닙니다. $k_a-k_{el}$은 단순한 분모가 아니라 **두 과정이 시간축에서 얼마나 떨어져 보이는지를 정하는 항**입니다. $k_a \approx k_{el}$이면 두 과정이 거의 분리되지 않아 한계식으로 수렴하고, $k_a<k_{el}$이면 혈장에 들어온 약물은 빠르게 사라지지만 관찰 terminal decline은 남은 흡수 때문에 느리게 보일 수 있습니다.

#### A. 형식적 정의 + 핵심 수식

1구획·1차 흡수·1차 소실·선형 PK(← dose 비례성 유지) 가정 [G&W p.30; R&T pp.171–172].

흡수 부위:

$$
\underbrace{\frac{dA_g}{dt}}_{\text{장관 변화}} = -\underbrace{k_a}_{\text{장관 소실}}\underbrace{A_g}_{\text{장관 잔량}}
$$

혈장/중심 구획:

$$
\underbrace{\frac{dC}{dt}}_{\text{농도 변화}} = \underbrace{\frac{k_a F D_{po} e^{-k_a t}}{V}}_{\text{전신 입력}} - \underbrace{k_{el} C}_{\text{중심 소실}}
$$

`[Source: G&W Eq.2:32–2:34, p.30; R&T Eq.6-2–6-3, pp.171–172]`

적분 해:

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

> 💡 두 모래시계가 겹쳐 있다고 보면 됩니다 — 장관에서 빠지는 모래시계($k_a$)와 중심구획에서 사라지는 모래시계($k_{el}$). 관찰 농도는 두 흐름의 **차이**입니다. 그래서 하강부가 보인다고 항상 elimination phase는 아닙니다 — $k_a<k_{el}$이면 terminal slope는 **흡수가 정하는 감소(absorption-limited decline)**일 수 있습니다.

#### C. Lag-time(← 흡수 시작 전 지연시간)

투여 시각이 아니라 실제 흡수 시작 이후의 시간만 식에 들어갑니다.

$$
C(t)=0 \quad (t<t_{lag})
$$

$$
\underbrace{C(t)}_{\text{지연 후 농도}}=\frac{\overbrace{k_a F D_{po}}^{\text{입력 크기}}}{\underbrace{V(k_a-k_{el})}_{\text{희석·분리}}}\left(\underbrace{e^{-k_{el}(t-t_{lag})}}_{\text{소실 지수}}-\underbrace{e^{-k_a(t-t_{lag})}}_{\text{흡수 지수}}\right)\quad (\underbrace{t\ge t_{lag}}_{\text{흡수 후}})
$$

`[Source: G&W Eq.2:39–2:42, pp.32–33]`

#### D. 0차 입력 — 다른 입력 함수

0차 흡수는 중심 소실은 그대로 두고 입력 함수만 바꾼 경우입니다. 흡수 중에는 입력이 거의 일정하고, 끝나면 washout만 남습니다 [G&W Eq.2:66–2:67, p.38; R&T Fig.6-2, p.171]. PK3에서 zero-order model의 AIC가 first-order보다 좋았지만 **이게 "진짜 zero-order absorption"의 증명은 아닙니다** — 여러 dose, 반복투여, IV 비교가 있어야 기전 해석이 가능합니다 [G&W pp.483–486].

> 💼 **실무 인사이트:** NONMEM ADVAN2 oral model의 KA initial은 큰 값·작은 값을 모두 시도합니다. 서로 다른 initial이 다른 해 또는 비슷한 OFV로 수렴하면 flip-flop 또는 practical identifiability 문제를 의심합니다.

**Card 1 요약:** Oral $C(t)$는 "흡수 지수 − 소실 지수". $F$와 $V$는 진폭을, $k_a$와 $k_{el}$은 모양과 terminal slope 해석을 지배합니다.

> **M1 체화 핵심**
> ① 경구 농도곡선이 늦게 올라오는 이유 → $k_a$와 $k_{el}$의 차이지수가 정합니다.
> ② 하강부 = elimination이라는 단정 → flip-flop에서는 흡수가 terminal slope를 지배합니다.
> ⚡ "좋은 fit = 진짜 생리학" → apparent fit을 true mechanism으로 오독하여 초기값·보고 문장이 실패합니다.

---

<!-- SLIDE_START: M2 | title: tmax/Cmax -->
<!-- SECTION_CORE: SC-04 -->

### Card 2. $t_{max}$ / $C_{max}$ — 흡수속도와 소실속도가 같아지는 순간

> **앞 카드에서 이 카드로**
> 차이지수 곡선의 구조를 알았으니, 다음은 그 곡선의 기울기가 언제 0이 되는가입니다.

> **거장의 시각**
> $t_{max}$를 "흡수가 가장 많이 끝난 시간"으로 읽으면 rate와 amount를 섞게 됩니다. **$dC/dt=0$**의 관점으로 보면 $F$, dose, $V$가 아니라 $k_a/k_{el}$의 상대 위치가 peak 시간을 정한다는 점이 즉시 보입니다. $t_{max}$는 가장 많이 흡수된 시간이 아니라 **순유입이 0이 되는 시간** — 흡수 속도와 소실 속도가 같아지는 순간입니다 [R&T p.173; G&W pp.34–35].

#### A. 도출

Master equation을 미분하고 $dC/dt=0$으로 두면:

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

> 🔑 **Peak 시간 규칙:** $t_{max}$는 저수지 수위가 가장 높은 순간 — 수도꼭지 유입과 배수구 유출 속도가 같아지는 순간이지, 물이 모두 들어온 순간이 아닙니다. linear 1구획에서 $F$와 dose는 높이를 바꾸지만 $t_{max}$ 위치는 바꾸지 않습니다.

$k_a \gg k_{el}$이면:

$$
\underbrace{C_{max}}_{\text{최고농도}}\approx \underbrace{\frac{F D_{po}}{V}}_{\text{도달량/부피}}\underbrace{e^{-k_{el}t_{max}}}_{\text{peak 전 소실}}
$$

`[Source: G&W Eq.2:53, p.35]`

Lag-time이 있으면 관찰 $t_{max}$는 $t_{lag}$만큼 뒤로 이동합니다 [G&W Eq.2:54–2:55, p.35].

#### B. 왜 $F$와 $V$가 $t_{max}$ 식에서 사라지는가

$F$, dose, $V$는 곡선의 높이를 위아래로 scale할 뿐 기울기 0의 시간 위치는 바꾸지 않습니다. 그래서 linear 1구획에서 dose나 $F$가 바뀌면 $C_{max}$와 $AUC$는 바뀌지만 $t_{max}$는 그대로입니다 [R&T Fig.6-5, p.174]. **단, 이건 absorption 단계만 건드렸을 때의 이야기**입니다 — $CL$이 변하면 $AUC$뿐 아니라 $t_{max}$와 $C_{max}$가 함께 움직이고, $V$가 변하면 $C_{max}$와 $t_{max}$가 서로 다른 방향으로 이동합니다. "$F\cdot dose$만 변했을 때"와 "disposition($CL/V$)이 변했을 때"의 곡선 변화 패턴이 다르다는 점이 absorption 변화와 disposition 변화를 가르는 첫 단서입니다 [R&T Figs.6-10–6-11, pp.179–180].

#### C. 잔차법(Method of Residuals)

말기 직선 구간에서 $k_{el}$을 먼저 추정한 뒤, 역외삽 직선에서 관찰 농도를 빼 잔차 직선을 만들면 그 기울기가 $-k_a$입니다. 두 직선의 교점은 lag-time 추정에 씁니다 [G&W pp.31–33; R&T Appendix F pp.781–783]. 단, terminal slope가 정말 elimination을 반영한다는 전제 위에 있어 flip-flop 상황에서는 위험합니다.

> 💼 **실무 인사이트:** 잔차법 terminal point 선택은 눈대중이 아닙니다 — 최소 3개 이상의 terminal points, 충분한 log-linear fit, $C_{max}$ 이후 충분히 늦은 시점. 안 그러면 $k_a$와 $k_{el}$ 초기값이 서로 오염됩니다.

#### D. 극한: $k_a=k_{el}$

$$
\underbrace{C(t)}_{\text{한계 농도}}=\underbrace{\frac{k' F D_{po}}{V}}_{\text{입력 scale}}\underbrace{t}_{\text{시간항}}\underbrace{e^{-k't}}_{\text{공통 감쇠}}
$$

`[Source: G&W Eq.2:58, p.37]`

**Card 2 요약:** $t_{max}$는 rate balance의 시점. linear 조건에서는 $F$, dose, $V$가 아니라 $k_a$와 $k_{el}$의 상대 크기가 정합니다.

> **M2 체화 핵심**
> ① peak가 언제 생기는가 → rate balance가 정합니다.
> ② AUC·Cmax scale 변화와 peak 시간 변화 혼동 → $F$·dose는 높이만, disposition 변화는 시간 위치까지 흔듭니다.
> ⚡ "$t_{max}$ = 흡수 완료 시점" → 흡수는 $t_{max}$ 이후에도 계속됩니다. onset/extent 해석 실패.

---

<!-- SLIDE_START: M3 | title: 생체이용률 F -->
<!-- SECTION_CORE: SC-05 -->

### Card 3. 생체이용률 $F$ — 흡수의 정도(extent)를 $AUC$로 읽습니다

> **앞 카드에서 이 카드로**
> rate balance가 끝났으니, 이제 전체 노출량을 묻습니다 — 전신 순환에 누적으로 얼마나 도달했는가.

> **거장의 시각**
> $k_a$는 "얼마나 빨리", $F$는 "얼마나 많이 전신 순환에 도달했는가"입니다. 두 개념을 섞으면 food effect, BE, formulation effect 해석이 흐려집니다. **$F$를 AUC가 읽는 extent로 박아 놓으면** rate($k_a$)와 extent($F$)가 분리됩니다.

#### A. 절대 생체이용률

IV 기준 투여가 있을 때, $F$(← 전신 순환 도달 분율):

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

> 🔑 **Extent 규칙:** $F$는 "얼마나 빨리"가 아니라 "얼마나 많이 도달했는가". $AUC$ 감소를 곧바로 $k_a$ 감소로 읽으면 rate와 extent를 섞게 됩니다.

전제는 두 투여 사이 clearance가 같다는 점입니다 [R&T p.183]. R&T 예시는 i.m. dose의 $F$를 97%, oral solution의 $F$를 46%로 계산하여 route별 extent 차이를 보여줍니다 [R&T Table 6-1 / Fig.6-14, pp.183–184].

#### B. 상대 생체이용률

두 혈관외 제형 A/B 비교:

$$
\underbrace{F_{rel}}_{\text{상대 F}}=\underbrace{\frac{AUC_B}{AUC_A}}_{\text{B/A 노출}}\cdot\underbrace{\frac{D_A}{D_B}}_{\text{용량 보정}}
$$

`[Source: R&T Eq.6-15, p.185]`

IV 기준 투여 없이도 두 제품의 전신 전달 차이를 비교할 수 있습니다 [R&T pp.183–185].

#### C. 소변 데이터 — 주의점

요중 배설 데이터로도 $F$, $F_{rel}$, 신장 청소율을 추정할 수 있습니다. 단 **미변화체 배설 분율과 신장 처리가 비교 조건에서 일정**해야 합니다 [R&T Eq.6-18–6-21, pp.187–188].

#### D. 기전적 $F$

$$
\underbrace{F}_{\text{전체 F}}\approx\underbrace{F_F}_{\text{흡수·제형}}\cdot\underbrace{F_G}_{\text{장관 생존}}\cdot\underbrace{F_H}_{\text{간 생존}}
$$

`[Source: R&T Ch.7 context, pp.197–220]`

$F$는 "용해되어 들어온 양"이 아니라 장관·장벽·간을 통과한 결과임을 기억하는 용도로 둡니다.

#### E. 생동성(BE) 맥락

R&T는 시험/기준 ratio의 90% CI와 0.80–1.25 기준을 설명합니다 [R&T Fig.6-13, p.183]. 핵심 질문: **"$F_{rel}$만 같아도 충분한가?"** $F_{rel}$이 같아 $AUC$가 비슷해도 $k_a$가 다르면 $C_{max}$·$t_{max}$가 달라집니다. extent와 rate는 항상 같이 봐야 합니다.

**Card 3 요약:** $F$는 extent, $k_a$는 rate. $AUC$는 $F\cdot \mathrm{Dose}/CL$이지만, 경구 단독에서는 $CL$이 아니라 $CL/F$가 추정됩니다.

> **M3 체화 핵심**
> ① 얼마나 많이 도달했는가 → $F$와 $AUC$가 정합니다.
> ② 얼마나 빨리 peak에 도달했는가 → $k_a$와 input function이 정합니다.
> ⚡ "$AUC$ 변화 = 흡수속도 변화" → extent와 rate를 섞어 food/formulation effect 문장이 실패합니다.

---

<!-- SLIDE_START: M4 | title: APEX V/F 식별불가능성 + Flip-flop -->
<!-- SECTION_CORE: SC-06 -->

### Card 4. APEX — $V/F$ 식별불가능성 + Flip-flop 동정

> **앞 카드에서 이 카드로**
> $F$가 extent라는 점을 알면, 경구 단독 데이터에서 왜 $F$와 $V$, $F$와 $CL$이 묶여 보이는지가 핵심 문제가 됩니다.

> **거장의 시각 (Apex)**
> 💢 **흔한 오해:** 좋은 OFV와 작은 RSE가 나오면 oral-only 모델에서도 $V$, $CL$, $k_{el}$이 확정되었다고 생각합니다.
> ✅ **실제:** 경구 곡선은 **입력 함수 ⊗ $F$ ⊗ disposition의 합성곱** — 같은 곡선이 서로 다른 기전 조합으로 만들어질 수 있습니다.
> 🎯 **체화할 단 하나의 직관:** oral-only 결과는 $V/F$, $CL/F$, terminal slope ambiguity를 남기는 apparent parameter 보고서입니다.

`[⚡ Apex Concept]`

**Convolution lens:** 경구 농도-시간 곡선은 입력 함수($k_a$·lag·gastric emptying·multiple sites), $F$, disposition($CL$·$V$)의 합성곱입니다. 어느 한 축만으로는 곡선 형태가 결정되지 않고, 같은 곡선이 서로 다른 조합으로 나올 수 있습니다. 이게 $V/F$로 묶이는 이유, terminal slope label이 뒤집힐 수 있는 이유, fitted $k_a$가 실제 흡수가 아닐 수 있는 이유를 **한꺼번에** 설명합니다. 좋은 OFV·작은 RSE는 "모델이 데이터를 잘 설명한다"는 뜻일 뿐, "$V$와 $F$가 원리적으로 분리되었다"는 뜻이 아닙니다 — **수치적 식별가능성과 구조적 식별가능성(structural identifiability, ← 원리적으로 두 파라미터를 따로 추정할 수 있는가)은 다른 문제**입니다.

#### A. $V/F$ 구조적 식별가능성

Master equation에서 $F$와 $V$는 항상 $F/V$ 형태로 같이 등장합니다.

위 식(앞서 정의한 경구 $C(t)$)의 양변에 $F/V$ 식별가능성 맥락을 대입하면

경구 단독은 $V/F$만 추정하고, clearance도 $CL/F$로 보고해야 합니다 [G&W p.32; R&T p.185].

$$
\underbrace{AUC}_{\text{전신 노출}}=\underbrace{\frac{F\cdot Dose}{CL}}_{\text{도달량/CL}}=\underbrace{\frac{Dose}{CL/F}}_{\text{경구 관찰형}}
$$

$\mathrm{Dose}/(CL/F)$와 $F\cdot \mathrm{Dose}/CL$은 대수적으로 같지만, $AUC$만 보고는 변화 원인이 $F$인지 $CL$인지 가를 수 없습니다.

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $V/F$ | volume | apparent volume | $V$ 변화 또는 $F$ 변화 |
| $CL/F$ | volume/time | apparent clearance | $CL$ 변화 또는 $F$ 변화 |
| terminal slope | time$^{-1}$ | 관찰 말기 감소율 | $k_{el}$ 또는 $k_a$ 병목 |
| $AUC$ | conc·time | 총 전신 노출 | $F\cdot Dose/CL$ |

> 💡 안개 낀 유리창 너머로 방 크기와 창문 개방률을 동시에 추정하는 상황 — 방이 큰지($V$), 창문이 덜 열렸는지($F$)는 같은 농도 하나로 가를 수 없습니다. **$V/F=50\ \mathrm{L}$는 $V=50\ \mathrm{L}$라는 뜻이 아닙니다.** IV 또는 absolute $F$ 근거가 없으면 $V/F$, $CL/F$로 보고합니다.

**저자의 4-part 결론 [R&T p.185]:** 단일 oral dose만 있을 때 — **(i)** $AUC$는 사다리꼴법으로 *계산 가능*, **(ii)** $CL$은 $F$를 모르므로 *계산 불가*, **(iii)** terminal half-life는 무엇이 rate-limiting인지 모르면 elimination/absorption 어느 쪽에도 *confidently 할당 불가*, **(iv)** $V$는 *추정 불가*. 이 네 줄이 Apex의 핵심 메시지입니다.

#### B. Flip-flop 실용적 식별가능성

일반적으로 $k_a>k_{el}$이면 경구 말기 기울기는 소실을 반영합니다. 그러나 $k_a<k_{el}$이면 **남은 흡수 과정이 더 느린 과정**이 되므로 관찰 말기 기울기는 흡수를 반영할 수 있습니다 [G&W Fig.2.17, p.30; R&T Case C, pp.175–176].

**핵심 경고:** "rising limb = absorption, declining limb = elimination"은 flip-flop에서는 틀립니다 [G&W pp.29–30; R&T pp.173–176].

#### C. 사례 앵커

- **Fluticasone propionate**(흡입 스테로이드): median $t_{max}$ 90분, $C_{max}$ 30–90분, 흡수 반감기 3.8–4시간. → **빠른 $t_{max}$가 빠른 흡수를 증명하지 않는다**는 사례 [R&T Fig.6-7, p.177].
- **Theophylline**(저추출 기관지확장제): 음식/물은 흡수 동역학을 바꿔도 말기 반감기는 약 6.3 h로 유지. → **흡수 변화와 disposition 변화를 가르는** 사례 [R&T Fig.6-8, p.178].
- **Penicillin G**(난용성 근육주사 항생제): 난용성 제형은 흡수가 rate-limiting이 될 수 있음 [R&T Fig.6-9, p.178].
- **PK2:** lag-time model은 $K_a=0.043\ \mathrm{min}^{-1}$, $K=0.0088\ \mathrm{min}^{-1}$, $V/F=32\ \mathrm{L}$, $t_{lag}=16\ \mathrm{min}$ [G&W p.480]. 같은 사례의 $F=82\%$와 $true\ V=20\ \mathrm{L}$는 $32\times0.82\approx26\ \mathrm{L}$과 산술 충돌이므로 "원문 수치 충돌 [확인 필요]"로 둡니다 [G&W p.480].
- **PK2 Solution III:** 역전된 초기 추정치가 다른 $k_a/k_{el}/V/F$ 해로 수렴 가능 [G&W pp.481–482].
- **PK3:** 1차 모델은 $K_a\approx K_e$와 큰 CV/RSE, 0차 모델은 AIC 더 낮음(85.2 vs 76.2). 그러나 **더 좋은 적합이 진짜 0차 흡수의 증명은 아닙니다** [G&W Table 3.1, p.486].

#### C-2. 그럴듯한 오류(Plausible Fallacy)

**오류:** $C_{max}$↓, $T_{max}$↑이므로 흡수가 느려졌다고 단정.
**나비효과:** $k_a$ 감소 해석 → 제형 재조제 또는 absorption model 복잡화 → [임상] 실제 원인이 first-pass 증가·용해도 저하·flip-flop이면 노출/독성/치료실패 예측 오류 → [모델링/규제] IV 또는 route comparison 없이 $F$·$k_a$ 분리 주장, BE 의사결정 오류, 재분석 요구 위험.

#### D. NONMEM 보고

경구 단독 PopPK에서는 $F$를 1로 고정하고 $V/F$, $CL/F$로 보고하는 것이 구조적으로 정직합니다. `F1`을 추정하거나 임의 값으로 고정한 뒤 $V$·$CL$을 절대값처럼 보고하면 **사전 가정이 추정된 파라미터처럼 보일 위험**이 있습니다.

> 💼 **실무 인사이트:**
> ① **쌍둥이 억제(Twin Suppression):** $k_a$·$k_{el}$의 두 해가 모두 plausible → ETA(KA)와 ETA(KEL)가 강하게 보상.
> ② **$V/F$ 드리프트:** 같은 covariate가 $V/F$와 $CL/F$에 비례적으로 나타나면 $F$-driven 변화 의심.
> ③ **가상 분포용적(Phantom Volume):** $V/F$ 변화를 $V$ 변화로 보고. 핵심 식: $AUC=F\cdot \mathrm{Dose}/CL=\mathrm{Dose}/(CL/F)$.

**Card 4 요약:** 경구 단독은 $V$와 $F$를 가르지 못합니다. flip-flop에서는 terminal slope도 $k_{el}$로 확정되지 않습니다. 좋은 fit은 진짜 parameter의 증거가 아닙니다.

> **M4 체화 핵심**
> ① oral-only에서 무엇을 보고할 것인가 → $V/F$, $CL/F$, terminal slope ambiguity가 정합니다.
> ② 작은 RSE·좋은 OFV → numerical precision일 뿐 structural identifiability 해결이 아닙니다.
> ⚡ "$V/F$를 $V$로 보고" → phantom volume interpretation → [임상] 용량·축적 판단 오류 / [규제] 재분석 요구 위험.

---

<!-- SLIDE_START: M5 | title: ka_app vs ka_true -->
<!-- SECTION_CORE: SC-07 -->

### Card 5. $k_{a,app}$ vs $k_{a,true}$ — $k_a$가 측정하는 것은 무엇인가

> **앞 카드에서 이 카드로**
> $V/F$와 terminal slope가 apparent label이라면, $k_a$ 역시 실제 흡수속도인지 먼저 의심해야 합니다.

> **거장의 시각**
> fitted $k_a$를 곧바로 true absorption으로 부르면 장관 손실·분해·site heterogeneity를 모두 흡수속도 변화로 오해합니다. **gut compartment에서 "사라진 속도"와 systemic circulation에 "도달한 속도"를 따로 떼어 놓으면** food/formulation effect 해석이 안전해집니다. 모델 output의 $k_a$는 겉보기 parameter일 수 있습니다.

#### A. 겉보기 장관 소실

장관 소실 경로가 실제 흡수($k_{a,true}$)와 장내 분해/손실($k_d$)로 나뉘면:

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

> 💡 장관 구획은 **출구가 두 개인 싱크대** — 하나는 전신 순환 배수구($k_{a,true}$), 다른 하나는 손실 배수구($k_d$). $k_{a,app}$가 커졌다는 말은 흡수가 빨라졌다는 뜻이 아니라 **장관에서 더 빨리 사라졌다**는 뜻일 수 있습니다.

#### B. 해석

fitted $k_a$가 커졌다고 곧 "흡수가 빨라졌다"가 아닙니다 — "gut compartment에서 더 빨리 사라졌다"일 수도 있습니다. **$AUC$가 함께 변하지 않으면** onset/rate 변화, **$AUC$도 함께 변하면** extent 변화가 동반된 것입니다 [G&W pp.40–41].

#### C. 다중 흡수 부위

흡수 부위가 여러 개면 곡선이 다중 peak 또는 비정형 상승부를 보입니다. buccal + GI 같은 구조는 Eq.2:80–2:82로 제시됩니다 [G&W pp.46–47]. 이 경우 단일 $k_a$는 여러 입력 과정을 하나로 눌러 담은 요약 파라미터입니다.

> 💼 **실무 인사이트:** food effect 보고서에서 "$k_a$ 감소 = 흡수 저하"라고 쓰지 않습니다. $F_{rel}$($AUC$ ratio)을 함께 보고하여, $AUC$ 변화 없이 $k_a$만 바뀌면 onset/rate, $AUC$도 바뀌면 extent 변화로 가릅니다.

**Card 5 요약:** $k_a$는 항상 "진짜 흡수속도"가 아닙니다. fitted $k_a$의 생리학적 의미는 모델 구조와 외부 evidence가 정합니다.

> **M5 체화 핵심**
> ① fitted ka가 변했을 때 → $k_{a,app}=k_{a,true}+k_d$ 구조가 먼저 결정됩니다.
> ② AUC 변화가 동반된 상황 → rate만이 아니라 extent 또는 loss 변화가 지배합니다.
> ⚡ "$k_a$ 감소 = 흡수 저하" → 장관 손실·다중 흡수부위·food effect를 단일 흡수속도로 오독합니다.

---

<!-- SLIDE_START: §5 | title: 혼동쌍 해부 -->
<!-- SECTION_CORE: SC-08 -->

## §5. 혼동쌍 해부

### 혼동쌍 1. $k_a$ vs $k_{el}$ under flip-flop — 결정타

| 비교 기준 | $k_a$ | $k_{el}$ |
|---|---|---|
| 단위 / 차원 | time$^{-1}$, 흡수부위 소실 속도 | time$^{-1}$, 중심구획 소실 속도 |
| 수식 내 위치 | $e^{-k_a t}$ input 지수항 | $e^{-k_{el}t}$ disposition 지수항 |
| 변화 원인 | 용출, 위배출, 흡수부위, 제형 | $CL/V$, 신장·간 기능, 분포 변화 |
| 혼동 시 임상 결과 | flip-flop에서 terminal slope label 오류 | dosing interval, accumulation, washout 판단 오류 |

**결정타:** terminal half-life를 elimination half-life로 착각하면 dosing interval, accumulation, washout 판단이 모두 흔들립니다.

**⚡ 기억 고리 — 병목이 어느 쪽에 있는가:** flip-flop은 $k_a<k_{el}$이므로 **흡수가 병목** — terminal slope가 $k_a$. disposition-limited는 $k_{el}<k_a$이므로 **제거/분포가 병목** — terminal slope가 $k_{el}$. **IV 크로스오버 없이 경구만으로는 두 메커니즘을 가를 수 없다는 점이 핵심 함정입니다.**

**⚡ 기억 고리 — 정점 시각 vs 흡수 종료 시각:** $T_{max}$는 흡수 속도와 제거 속도가 같아지는 **교차점**, 흡수가 완료되는 시점이 아닙니다. $T_{max}$ 이후에도 흡수는 계속되며 단지 제거가 더 빠를 뿐입니다.

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

**⚡ 기억 고리 — 얼마나 들어오나 vs 얼마나 빨리:** $F$는 systemic circulation 도달 **비율**, $k_a$는 흡수 부위에서 얼마나 빠른지의 **속도**. $AUC$는 $F$에 비례, $T_{max}$·$C_{max}$ 형태는 $k_a/K$ 비율이 정합니다.

**⚡ 기억 고리 — 속도계 vs 적산계:** $k_a$는 **속도계(순간 속도)**, $F$는 **적산계(누적량)**. $k_a$를 키워도 $F$가 그대로면 $AUC$는 그대로입니다.

### 혼동쌍 3. $V/F$ vs $V$ — 결정타

| 비교 기준 | $V/F$ | $V$ |
|---|---|---|
| 단위 / 차원 | volume, apparent | volume, true distribution volume |
| 수식 내 위치 | oral-only 보고, $F$와 묶임 | IV 또는 $F$ 근거가 있어야 분리 |
| 변화 원인 | $V$ 변화 또는 $F$ 변화 | 조직분포, 체성분, 단백결합 |
| 혼동 시 임상 결과 | $F$ 변화가 분포용적 변화처럼 보임 | phantom interpretation, covariate 해석 오류 |

**결정타:** $V/F$를 $V$로 바꿔 쓰는 순간, 흡수율 변화가 분포용적 변화처럼 보이는 phantom interpretation이 생깁니다.

### 혼동쌍 4. First-order $k_a$ vs Zero-order input

| 비교 기준 | First-order $k_a$ | Zero-order input |
|---|---|---|
| 단위 / 차원 | time$^{-1}$, 남은 양 비례 입력 | amount/time, 일정 입력 |
| 수식 내 위치 | $e^{-k_a t}$ 지수항 | 일정 입력률, 종료 후 washout |
| 변화 원인 | 속방형 용액/정제 근사, 용출·위배출 | controlled-release, 삼투펌프, 용출 제한 |
| 혼동 시 임상 결과 | 0차 모델의 better fit을 진짜 0차 흡수로 과장 | PK3처럼 AIC 우월이 기전 증명을 뜻하지 않음 [G&W pp.483–486] |

**§5 요약:** 경구 PK의 가장 위험한 혼동은 slope label, apparent parameter, rate/extent를 서로 바꿔 부르는 것입니다. 이름표가 바뀌면 같은 숫자도 다른 임상 결론을 만듭니다.

---

<!-- SLIDE_START: §7 | title: 자기 테스트 -->
<!-- SECTION_CORE: SC-09 -->

## §7. 자기 테스트: 능동 회상

### Q1. Master equation을 쓰고 각 항의 의미를 설명하세요.

$$
\underbrace{C(t)}_{\text{혈장 농도}}=\frac{\overbrace{k_a F D_{po}}^{\text{전신 입력}}}{\underbrace{V(k_a-k_{el})}_{\text{희석·분리}}}\left(\underbrace{e^{-k_{el}t}}_{\text{소실 지수}}-\underbrace{e^{-k_a t}}_{\text{흡수 지수}}\right)
$$

$k_a$ 흡수부위 소실 속도, $F$ 전신 도달 분율, $D_{po}$ 투여량, $V$ 분포용적, $k_{el}$ 소실 속도. 괄호 안은 소실 지수와 흡수 지수의 차이 [G&W p.30; R&T p.782].

### Q2. 왜 $t_{max}$ 식에 $F$, $V$, dose가 없는가?

$t_{max}$는 $dC/dt=0$의 시간. linear system에서 $F$·$V$·dose는 높이만 scale할 뿐 기울기 0의 시간 위치는 안 바꿉니다. $t_{max}=\ln(k_a/k_{el})/(k_a-k_{el})$ [G&W p.35].

### Q3. $F_{rel}=1.0$인 두 oral formulation이 임상적으로 완전히 같은가?

아닙니다. $F_{rel}=1.0$은 extent가 같다는 뜻일 뿐 — $k_a$가 다르면 $C_{max}$·$t_{max}$가 달라지고, onset이나 peak-related safety가 중요한 약물에서는 임상적 차이가 남습니다 [R&T pp.181–183].

### Q4. PK2에서 $V/F=32\ \mathrm{L}$, $F=0.82$일 때 진짜 $V$는?

산술적으로는 $V=32\times0.82\approx26\ \mathrm{L}$. 그러나 원문은 $true\ V=20\ \mathrm{L}$이라고 서술하여 산술값과 충돌 — 본 handout은 26 L를 확정값으로 쓰지 않고 "원문 수치 충돌 [확인 필요]"로 둡니다 [G&W p.480].

$$
\underbrace{V}_{\text{true V}}=\underbrace{(V/F)}_{\text{apparent V}}\times\underbrace{F}_{\text{F 보정}}=\underbrace{32\times0.82}_{\text{산술 환산}}\approx\underbrace{26\ \mathrm{L}}_{\text{계산 V}}
$$

### Q5. Oral-only fit에서 $k_a=0.05\ \mathrm{hr}^{-1}$, $k_{el}=0.5\ \mathrm{hr}^{-1}$. 관찰 terminal half-life를 $\ln 2/0.5=1.4\ \mathrm{h}$로 써도 되는가?

안 됩니다. $k_a<k_{el}$이면 관찰 terminal slope는 더 작은 $k_a$를 따를 수 있어 terminal half-life는 약 $\ln 2/0.05=13.9\ \mathrm{h}$. $k_{el}=0.5\ \mathrm{hr}^{-1}$는 진짜 elimination일 수 있지만 oral-only로는 확정 불가.

$$
\underbrace{t_{1/2,obs}}_{\text{관찰 반감기}}=\frac{\underbrace{\ln 2}_{\text{반감기 상수}}}{\underbrace{0.05}_{\text{병목}}}\approx\underbrace{13.9\ \mathrm{h}}_{\text{flip-flop}}
$$

### Q6. PK3에서 zero-order model의 AIC가 first-order보다 낮았다. "진짜 0차 흡수"라고 결론 가능한가?

아닙니다. PK3는 zero-order input model이 해당 dataset을 더 잘 설명한다는 것만 보여줍니다 — 진짜 기전 확정에는 용량 범위, 반복 투여, IV 데이터 등 추가 근거가 필요합니다 [G&W pp.483–486].

### Q7. $k_{a,app}=1.0\ \mathrm{hr}^{-1}$, $k_d=0.4\ \mathrm{hr}^{-1}$일 때 $k_{a,true}$와 $F$는?

$k_{a,true}=1.0-0.4=0.6\ \mathrm{hr}^{-1}$.

$$
F=\frac{k_{a,true}}{k_{a,true}+k_d}=\frac{0.6}{1.0}=0.6
$$

$$
\underbrace{F}_{\text{도달 분율}}=\frac{\underbrace{k_{a,true}}_{\text{흡수 }0.6}}{\underbrace{k_{a,true}+k_d}_{\text{전체 }1.0}}=\underbrace{0.6}_{\text{60\% 도달}}
$$

G&W Eq.2:70 구조 해석입니다. 실데이터에서는 $k_d$를 별도 evidence 없이 분리하기 어렵습니다 [G&W p.41].

### Q8. Boss dilemma: terminal slope가 $0.18\ \mathrm{hr}^{-1}$이고 alternative model은 $k_{el}=0.69\ \mathrm{hr}^{-1}$도 가능. 무엇을 보고?

관찰 terminal half-life는 $\ln 2/0.18\approx3.85\ \mathrm{h}$. 그러나 flip-flop 가능성이 있으면 0.18이 $k_{el}$인지 $k_a$인지 확정 불가. 안전한 보고 — "oral-only data에서 terminal slope는 $0.18\ \mathrm{hr}^{-1}$로 관찰되었으나, IV 또는 route/formulation comparison 없이는 이를 elimination rate로 확정할 수 없습니다. Dose recommendation은 두 해에 대한 sensitivity analysis로 방어합니다."

$$
\underbrace{t_{1/2,terminal}}_{\text{말기 반감기}}=\frac{\underbrace{\ln 2}_{\text{반감기 상수}}}{\underbrace{0.18\ \mathrm{hr}^{-1}}_{\text{obs slope}}}\approx\underbrace{3.85\ \mathrm{h}}_{\text{계산 반감기}}
$$

---

## ⚡ 보스 딜레마 ★★ — 최종 자기 테스트 캡스톤

### Boss Dilemma. 제형 변경 후 $C_{max}$↓·$T_{max}$↑: 두 가설을 어떻게 방어하는가?

**시나리오:** 경구 단독 Phase 1에서 $C_{max}$↓·$T_{max}$↑. 제형 팀은 "흡수가 느려졌다($k_a$ 감소)"고 결론. 모델러로서 두 가지 방어 가능한 해석:

- **(A) $k_a$ 감소**로 해석 → absorption model을 first-order에서 transit compartment로.
- **(B) $F$ 감소 (first-pass 효율 감소, apparent $CL$ 증가 → $AUC$ 감소)**로 해석 → $F$의 공변량 탐색 우선.

**거장의 절충 판단:**

(A)는 모델 복잡도를 높이고 $T_{max}$ 재현에 집중하지만, IV 없이는 $F$와 $k_a$의 교락(confounding, ← 두 요인이 얽혀 분리되지 않는 상태)을 풀 수 없습니다 (Card 4의 convolution lens). 보고 시 "transit compartment가 $T_{max}$ 지연을 더 잘 설명하지만 $F$ 동시 변화 가능성은 본 데이터로 배제 불가"라고 명시.

(B)는 파라미터 수를 단순하게 두지만, $k_a$ 변화가 진짜 원인이었다면 $AUC$와 곡선 형태가 어긋날 수 있습니다. 보고 시 "$AUC$ ratio가 유의하게 감소해 $F$-driven 해석을 지지하지만 $k_a$ 변화 가능성을 sensitivity analysis로 평가"라고 기술.

**규제 방어 — 분리 진단 알고리즘:**

> **1단계.** "$AUC$가 같은가 다른가"로 가설 분리.
> &nbsp;&nbsp;— $AUC$ 변화 없음 + $C_{max}$↓·$T_{max}$↑ → (A) $k_a$ 감소 우세
> &nbsp;&nbsp;— $AUC$ 감소 + $C_{max}$↓·$T_{max}$↑ → (B) $F$ 감소 또는 (A+B) 복합
> **2단계.** IV 크로스오버를 요청하거나, 안 되면 **두 모델 모두 적합 + sensitivity analysis로 명시.**
> **3단계.** 단일 가설을 채택하지 않고 "두 해석 모두 데이터와 정합적이며, 임상 dosing이 두 해 모두에서 안전한 영역인가"를 평가.

→ **가장 위험한 자세는 "$k_a$ 감소 = 흡수 불량 = 제형 재조제"라는 단순 추론.** Card 4 Plausible Fallacy(C-2)가 경고한 함정이며, BE trial 의사결정 사슬을 잘못 만들어냅니다.

**§7 요약:** 계산보다 중요한 건 label입니다. 같은 숫자라도 $k_a$인지 $k_{el}$인지, $V$인지 $V/F$인지 잘못 붙이면 임상 결론이 달라집니다.

---

> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** 경구 PK의 전문성은 $V/F$, $CL/F$, $k_{a,app}$, terminal slope ambiguity를 숨기지 않고 명시하는 데서 완성됩니다.

---

<!-- SLIDE_START: §8 | title: 메타프레임과 큰 그림 -->
<!-- SECTION_CORE: SC-10 -->

## §8. 메타프레임과 큰 그림

### A. 위치

본 세션은 IV bolus 이후 첫 임상 현실 — **흡수 단계가 있는 계**를 다룹니다. 이후 다회투여, modified-release, food effect, BE, PopPK 흡수 모델로 가더라도 판단 기준은 결국 다음 네 질문으로 돌아옵니다.

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| 입력 함수가 1차가 아님 | $k_a$, lag, input duration | → | $C_{max}$·$t_{max}$ 재현 실패 | lag/zero-order/transit 후보 평가 |
| $F$가 제형·식사·first-pass로 변함 | $F$, $CL/F$ | → | AUC 차이와 apparent clearance 변화 | $F_{rel}$, AUC ratio, sensitivity |
| terminal slope label 불명확 | $k_a$ 또는 $k_{el}$ | → | 반감기·축적 판단 오류 | IV/route comparison 또는 dual-solution 방어 |
| $V$, $CL$을 absolute처럼 보고 | $V/F$, $CL/F$ | → | covariate effect 오해 | apparent parameter 명시 |

### B. 의존성 — 놓치면 생기는 실패 모드

| 실패 모드 | 실제 결과 |
|---|---|
| $V/F$를 $V$로 보고 | 공변량 효과를 분포 변화로 오해. |
| $CL/F$를 $CL$로 보고 | $F$ 변화가 clearance 변화처럼 보임. |
| 말기 기울기를 무조건 $k_{el}$로 해석 | flip-flop에서 반감기·축적 판단 오류. |
| $k_a$ 변화를 extent 변화로 단정 | food/formulation effect 메시지 오류. |
| $t_{max}$ 용량 의존성을 무시 | 포화성 흡수·초회 통과 포화·비선형 소실 신호를 놓침. |
| 0차 모델의 더 나은 적합을 기전 증명으로 단정 | 서방형/용해도/용출 근사를 생리학적 확정으로 과장. |

### C. 전문가 해석 지점

> 💼 **실무 인사이트:** 30년 차 pharmacometrics 연구자는 경구 모델 결과를 볼 때 먼저 "모델이 맞았는가?"가 아니라 "무엇이 식별되었는가?"를 묻습니다. Phase 1 SAD(단회 상승 용량 시험) 회의에서 senior가 던지는 실무 질문은 단순합니다 — **"FIH(최초 임상 투여) 단계에서 IV arm 또는 absolute $F$ 확인 가능성을 평가했는가?"** 이 질문 하나가 $F$, $V/F$, $CL/F$, flip-flop, $k_{a,app}$의 모든 위험을 앞으로 끌어냅니다.

| 후속 세션 | 이 세션에서 열리는 개념 | 없으면 실패하는 것 |
|---|---|---|
| multiple dosing / accumulation | terminal slope label, $k_{el}$ vs $k_a$ | 축적계수·washout 해석 오류 |
| modified-release / zero-order input | input function 구분 | better fit을 기전 증명으로 과장 |
| oral PopPK absorption | $V/F$, $CL/F$, $k_{a,app}$ | apparent를 true로 보고 |
| BE / food effect | rate vs extent 분리 | $AUC$, $C_{max}$, $t_{max}$ 메시지 혼동 |

### D. Ch.7 맥락

$k_a$와 $F$의 변동성은 BCS, 위배출, 용출, 수송체, 장관/간 초회 통과 같은 생리·물리화학적 요인에서 옵니다. 본 세션의 수식은 그 복잡성을 **1차 입력과 $F$라는 두 apparent 축**으로 한꺼번에 다루는 첫 단계입니다 [R&T pp.197–220].

> 📖 **Gabrielsson & Weiner 5e, p.47, Fig.2.32:** 경구 농도-시간 곡선을 정하는 요인들이 chapter conclusion 수준에서 하나의 구조로 다시 묶입니다.

### E. 최종 확정 문장

**최종 요약:** 경구 PK의 핵심은 $C(t)$를 맞추는 데서 끝나지 않습니다. 더 중요한 건 $C(t)$에서 실제로 분리 가능한 것과 분리 불가능한 것을 가르는 일입니다. 경구 단독 데이터는 $V/F$, $CL/F$, 겉보기 $k_a$, terminal slope ambiguity를 남깁니다. 이 네 가지를 명시하면 handout은 안전하고, 생략하면 모델은 그럴듯하지만 위험해집니다.

---

<!--
## v3.8 자가검증 체크리스트

| 항목 | 기준 | 결과 |
|---|---|---|
| SLIDE_START 개수 | §섹션수 + 카드수 합산 | 10 개 |
| 카드당 callout 합계 ≤ 6 | 전체 카드 | ✓ |
| [E] 박스 존재 | 모든 §2 카드 | ✓ |
| [D] 거장의 시각 존재 | 모든 §2 카드 | ✓ |
| [L] 파라미터 표 존재 | Apex 카드 + 정의 수식 카드 | ✓ |
| §5 혼동 쌍 표 행 순서 고정 (4행) | §5 전체 | ✓ |
| 기호 일관성 | 첫 등장 기준 통일 | ✓ |
| PART B 흔적 없음 | 전체 | ✓ |
| 수치 anchor 보존 | 원본 수치 anchor | ✓ |
| [M] 나비효과 이중 종착점 | Apex 카드 전체 | ✓ |

✗ 항목: 없음.
-->

<!-- v3.8 변환 노트
- v3.7 → v3.8 변환: 메타 콘텐츠 정리, 학습자 메타 노출 차단
- v3.7 → v3.9 변환: v3.8 메타데이터 회귀 보정, SECTION_CORE 마커 적용, 출처 표기 [G&W]/[R&T] 표준 통일
- 보존 감사: SLIDE_START 10개, 약물명·수치 앵커 전수, 수식 블록 전수
- v3.9 변환 사항: 메타 헤더 v3.7→v3.8 갱신, 변환 노트 신설, C(t) master equation 중복 1건 해소
-->

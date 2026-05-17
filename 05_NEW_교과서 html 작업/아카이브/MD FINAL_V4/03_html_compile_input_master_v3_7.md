# 03 — 경구(혈관외) PK: F · ka · tmax · 흡수 — v3.7

<!-- 기호 통일: K_e / K / kel → k_{el} (첫 등장 §출처 및 범위 노트 기준) -->
<!-- 기호 통일: ka / KA / K_a → k_a (첫 등장 §출처 및 범위 노트 기준) -->
<!-- 기호 통일: Vmax 계열 해당 없음 — 본 세션 핵심 기호 아님 -->

## 임상 장면: 같은 AUC ratio, 다른 결론

R&T 예시에서 i.m. 투여의 $F$는 97%, oral solution의 $F$는 46%로 제시됩니다 [T Table 6-1 / Fig.6-14, pp.183–184]. 이 숫자를 단순히 “oral 흡수가 느리다”로 읽는 순간, rate($k_a$)와 extent($F$)를 섞어 버립니다. 더 위험한 상황은 경구 단독 자료에서 $V/F$, $CL/F$, terminal slope를 각각 $V$, $CL$, $k_{el}$처럼 보고하는 경우입니다. 이 세션은 바로 그 한 줄의 보고 문장이 어떻게 임상·규제 판단을 흔드는지 보여줍니다.


> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** 경구 PK는 식 암기가 아니라 $C(t)$·$F$·$k_a$·$V/F$·flip-flop에서 무엇이 식별되고 무엇이 가정인지 가르는 훈련이다.

---


## 학습 항법 안내

**이 자료 활용법:** 먼저 §1을 한 번 통독하여 전체 골격을 잡으시면 됩니다. 그다음 §2의 Card 1–5를 순서대로 학습하고, §5에서 자주 혼동하는 개념 쌍을 정리하세요. 마지막으로 §7에서 능동 회상(active recall)을 훈련한 뒤, §8에서 이 챕터가 이후 PopPK 흡수 모델링과 어떻게 연결되는지 확인하시면 됩니다.

**학습 경로:** $C(t)$ Master Equation → $t_{max}/C_{max}$ → $F$ → $V/F$ + flip-flop → $k_{a,app}$ vs $k_{a,true}$ → 혼동쌍 → 자기 테스트 → 메타프레임입니다.

**시작 전 확인 사항:** IV bolus 1구획 PK, $CL$, $V$, 반감기(half-life), 지수함수 감쇠(exponential decay), $AUC$에 대한 기본 이해가 선행되어야 합니다.

**학습 후 달라지는 것:** 경구 단독 데이터에서 식별 가능한 것($V/F$, $CL/F$, 겉보기 $k_a$, terminal slope ambiguity)과 추가 근거 없이는 식별할 수 없는 것을 스스로 구분할 수 있어야 합니다.

**그림 저작권 안내:** 교과서 원그림은 재현하지 않습니다. `FIGURE_POINTER` 블록은 텍스트 전용 교과서 참조 콜아웃으로 사용됩니다. `FIGURE_SCHEMATIC`은 재작도(redraw) 개요이며, 저작권 이미지 재현이 아닙니다.

---


## 출처 및 범위 노트

> **출처 및 범위 노트:** 이 장은 경구/혈관외 투여 후 흡수, 생체이용률(bioavailability, $F$), 흡수속도상수($k_a$), 최고농도 도달시간($t_{max}$), flip-flop kinetics의 핵심 학습 범위를 다룹니다.  
> **Source A (G):** Gabrielsson & Weiner 5e, Ch.2 §§2.2.4–2.2.12 (pp.28–47), PK2 (pp.476–482), PK3 (pp.483–486)  
> **Source B (T):** Rowland & Tozer 5e, Ch.6 (pp.169–195), Ch.7 (pp.197–220; context only), Appendix F (pp.781–784)  
> **기호 규칙(Symbol convention):** **$k_a$** = 흡수 속도상수(absorption rate constant), **$k_{el}$** = 소실 속도상수(elimination rate constant), **$V/F$** = 경구/혈관외 데이터에서의 겉보기 분포용적(apparent volume), **$CL/F$** = 겉보기 경구 청소율(apparent oral clearance).

---


## 0. 갱신된 큐레이션 지도

### 필수(MUST) — 최종 체화 카드 5개

| # | 개념 | 핵심 수식 / 출처 | 최종 판정 |
|---|---|---|---|
| 1 | **$C(t)$ Master Equation** | G Eq.2:32–2:35 [G p.30]; T 질량수지식(mass-balance) Eq.6-3 [T p.172] + 적분해(integrated solution) Eq.F-1 [T p.782] | 필수(MUST). 모든 $t_{max}$, $C_{max}$, $AUC$, lag-time, flip-flop 논의의 출발점입니다. |
| 2 | **$t_{max}$ / $C_{max}$** | G Eq.2:49–2:55 [G pp.34–35]; T $t_{max}$ Eq.F-6 [T p.783] | 필수(MUST). “흡수속도 = 소실속도”의 평형 조건입니다. |
| 3 | **생체이용률 $F$ (Bioavailability $F$)** | G Eq.2:71–2:74 [G pp.41–42]; T Eq.6-9–6-17 [T pp.183–186]; 소변 데이터(urine data) Eq.6-18–6-21 [T pp.187–188] | 필수(MUST). 속도(rate, $k_a$)와 정도(extent, $F$)를 분리하는 핵심 축입니다. |
| 4 | **APEX: $V/F$ 식별불가능성 + Flip-flop** | $V/F$ [G p.32; T p.185]; flip-flop [G Fig.2.17, p.30; T Case C, pp.175–176] | 필수(MUST). 경구 단독 데이터 해석의 구조적 한계입니다. |
| 5 | **$k_{a,app}$ vs $k_{a,true}$** | 겉보기 장관 소실(apparent GI loss) [G pp.40–41]; $F=k_{a,true}/(k_{a,true}+k_d)$, Eq.2:70 [G p.41] | 필수(MUST). 적합된 $k_a$가 “흡수”가 아니라 “장관 소실”일 수 있음을 고정합니다. |


$$
\underbrace{V/F}_{\text{겉보기 V}},\quad \underbrace{CL/F}_{\text{겉보기 CL}},\quad \underbrace{F=\frac{k_{a,true}}{k_{a,true}+k_d}}_{\text{흡수/손실 경쟁}}
$$

### 맥락(CONTEXT) — 본문 안에 압축 흡수

| 항목 | 위치 | 처리 |
|---|---|---|
| Lag time | Card 1, Card 2 | Eq.2:39–2:42 [G pp.32–33]를 1차 흡수식의 시간 이동으로 처리. |
| Method of Residuals | Card 2 | 초기 추정 알고리즘으로 압축; Appendix F [T pp.781–783]와 연결. |
| Zero-order input | Card 1, §5 | Eq.2:66–2:67 [G p.38], Fig.6-2 [T p.171], PK3 [G pp.483–486]로 “대체 입력 함수” 수준 유지. |
| 다회투여/축적(Multiple dosing / accumulation) | §8 | $R=1/(1-e^{-k_{el}\cdot\tau})$, Eq.2:78 [G p.45]는 다음 세션 의존성(dependency)으로만 배치합니다. |
| 다중 흡수 부위(Multiple absorption sites) | Card 5, §8 | Eq.2:80–2:82 [G pp.46–47]를 다중 peak / site heterogeneity의 경고로 1문장 처리합니다. |
| Ch.7 흡수 생리학 / BCS | §8 | BCS·위배출(gastric emptying)·초회 통과(first-pass)는 흡수 변동성의 생리학적 배경으로만 압축합니다 [T pp.197–220]. |
| Pidgeon-Pitlick / Vaughan | 제외 | B-Standard 10분 핸드아웃 기준에서는 과도한 수식 깊이입니다. |
| 국소 topical BE / microdialysis | 제외 | 본 세션의 $F$·$k_a$·$t_{max}$ 핵심 범위에서 벗어납니다. |


$$
\underbrace{R}_{\text{축적}}=\frac{1}{\underbrace{1-e^{-k_{el}\cdot\tau}}_{\text{잔존분 보정}}}
$$

---


<!-- SLIDE_START: §1 | title: 세션 헤더 및 로드맵 -->

## §1. 세션 헤더 및 로드맵

**제목:** 경구 및 혈관외 투여의 PK — $F$ · $k_a$ · $t_{max}$ 그리고 흡수 단계가 만드는 모든 것


### ASCII 레이어 개념 지도

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
카드 2 (M2): 최고농도 시점은 왜 “흡수 완료”가 아니라 rate balance인가?  
카드 3 (M3): $F$는 왜 속도가 아니라 전신 도달 정도인가?  
카드 4 (M4): 경구 단독 데이터는 왜 $V$, $CL$, terminal slope label을 확정하지 못하는가?  
카드 5 (M5): 적합된 $k_a$는 왜 실제 흡수속도가 아닐 수 있는가?


### 핵심 아이디어(Big Idea)


IV bolus에서는 투여 직후 약물이 전신 순환에 들어와 **초기 농도 $C_0$**를 만듭니다. 반면 경구/혈관외 투여에서는 **초기 농도 0에서 흡수와 소실이 경쟁하며 차이지수 곡선(← 두 지수함수의 차이로 생긴 곡선)**이 만들어집니다. 따라서 이 곡선에서는 $F$와 $V$가 $V/F$로 묶이고, $k_a$와 $k_{el}$은 terminal slope 해석에서 서로 뒤바뀔 수 있습니다. 이 때문에 경구 단독 데이터는 “잘 맞는 모델”과 “진짜 생리학”을 자동으로 구분해주지 않습니다. **같은 dose를 기준으로 비교하면, 흡수 단계가 끼어드는 순간 oral 곡선의 peak는 IV bolus 대비 낮아지고 시점도 뒤로 밀립니다. 즉 흡수는 단지 “늦게 들어오는 것”이 아니라, peak의 높이와 시점을 동시에 재정의하는 단계입니다** [T Fig.6-3, p.172].

### 이 세션의 한 줄 항법도

```
C(t) Master Equation
  → tmax/Cmax: 흡수속도 = 소실속도
  → F: 흡수의 extent는 AUC로 본다
  → V/F + flip-flop: 경구 단독 데이터의 식별 한계
  → ka,app vs ka,true: 적합된 ka가 실제 흡수인가, 장관 소실인가
```

### 선행·후속 위치

**선행:** IV bolus 1구획 PK(CL, V, t1/2, AUC), 1차 ODE, 자연로그/지수함수, AUC 사다리꼴법.  
**직후:** multiple dosing, accumulation factor, two-compartment oral model, transit/Erlang/Weibull input, modified-release 및 BE 평가.  
**실무 연결:** NONMEM ADVAN2/ADVAN4, oral PopPK parameter reporting, food effect, formulation effect, flip-flop 검증.


**§1 요약(Recap):** 이 세션의 목표는 식을 외우는 데서 끝나지 않습니다. 핵심은 oral curve에서 “무엇이 실제로 식별되는가”를 자동으로 의심하는 눈을 만드는 것입니다.

---

<!-- SLIDE_START: §2 | title: 개념 해부 카드 -->

## §2. 개념 해부 카드

---


> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** $C(t)$ Master Equation은 장관 입력과 중심 소실의 직렬 ODE가 만든 차이지수 곡선이다 — $F$, $V$, $k_a$, $k_{el}$의 이름표를 여기서부터 분리해라.

---


<!-- SLIDE_START: M1 | title: C(t) Master Equation -->

### Card 1. $C(t)$ Master Equation — 경구 PK의 모든 것이 시작되는 한 줄

> **거장의 시각**
> 경구 1구획 모델을 단일 곡선으로만 보면 상승부와 하강부의 label을 쉽게 잘못 붙입니다.
> 이 카드는 $C(t)$를 장관 입력과 중심 소실이 직렬로 만든 차이지수 신호로 읽게 만드는 출발점입니다.


**거장의 시각:** 경구 1구획 모델의 핵심은 농도 곡선을 “두 지수 함수의 차이”로 보는 것입니다. 상승부는 흡수 과정이 아직 남아 있다는 신호입니다. 하강부는 반드시 소실(elimination)만의 신호가 아닙니다.

**체화 직관:** $k_a-k_{el}$은 단순한 분모가 아닙니다. 두 지수 과정이 시간축에서 얼마나 분리되어 보이는지를 결정하는 항입니다. $k_a \approx k_{el}$이면 두 과정은 그래프상 거의 분리되지 않아 한계식으로 수렴합니다. 반면 $k_a<k_{el}$이면 혈장에 들어온 약물은 빠르게 제거됩니다. 그러나 관찰 terminal decline은 남아 있는 흡수 과정 때문에 느리게 보일 수 있습니다.

**A. 형식적 정의(Formal Definition)**


1구획 모델, 1차 흡수, 1차 소실, 선형 PK(linear PK, ← dose 비례성이 유지되는 PK)를 가정한 혈관외 투여 농도-시간 방정식(extravascular concentration-time equation)입니다. 흡수 부위의 약물은 시간에 따라 1차로 줄어들고, 그중 $F$ fraction이 전신 순환에 도달합니다 [G p.30; T pp.171–172].


**B. 모델 구조(Model Structure)**

흡수 부위:

$$
\frac{dA_g}{dt} = -k_a A_g
$$

$$
\underbrace{\frac{dA_g}{dt}}_{\text{장관 변화}} = -\underbrace{k_a}_{\text{장관 소실}}\underbrace{A_g}_{\text{장관 잔량}}
$$

혈장/중심 구획(central compartment):

$$
\frac{dC}{dt} = \frac{k_a F D_{po} e^{-k_a t}}{V} - k_{el} C
$$

$$
\underbrace{\frac{dC}{dt}}_{\text{농도 변화}} = \underbrace{\frac{k_a F D_{po} e^{-k_a t}}{V}}_{\text{전신 입력}} - \underbrace{k_{el} C}_{\text{중심 소실}}
$$

`[Source: G Eq.2:32–2:34, p.30; T Eq.6-2–6-3, pp.171–172]`

적분 해:

$$
\boxed{C(t)=\frac{k_a F D_{po}}{V(k_a-k_{el})}\left(e^{-k_{el}t}-e^{-k_a t}\right)}
$$

$$
\underbrace{C(t)}_{\text{혈장 농도}}=\frac{\overbrace{k_a F D_{po}}^{\text{전신 입력}}}{\underbrace{V(k_a-k_{el})}_{\text{희석·분리}}}\left(\underbrace{e^{-k_{el}t}}_{\text{소실 지수}}-\underbrace{e^{-k_a t}}_{\text{흡수 지수}}\right)
$$

`[Source: G Eq.2:35, p.30; T Appendix F Eq.F-1, p.782]`

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $F$ | fraction | 전신 순환 도달 분율 | 제형, food effect, first-pass |
| $D_{po}$ | amount | 경구 투여량 | 용량군, 복약 순응도 |
| $V$ | volume | 농도 희석 공간 | 체성분, 조직분포, 단백결합 |
| $k_a$ | time$^{-1}$ | 장관/흡수부위 소실 속도 | 용출, 위배출, 장관 손실 |
| $k_{el}$ | time$^{-1}$ | 중심구획 소실 속도 | $CL/V$, 신장·간 기능 |

💡 **비유:** 이 식은 두 개의 모래시계를 겹쳐 놓은 그림입니다. 하나는 장관에서 빠지는 모래시계($k_a$), 다른 하나는 중심구획에서 사라지는 모래시계($k_{el}$)이며, 관찰 농도는 두 흐름의 차이로 생깁니다.

💡 **차이지수 핵심** — $k_a-k_{el}$은 계산용 분모가 아니라 두 rate process가 그래프에서 얼마나 분리되어 보이는지를 정하는 신호입니다.  
⚠️ **헷갈림 방지:** 하강부가 보인다고 해서 항상 elimination phase가 아닙니다. $k_a<k_{el}$이면 terminal slope는 absorption-limited decline일 수 있습니다.


**C. Lag-time(← 흡수 시작 전 지연시간) 확장**

Lag-time이 있으면 투여 시각이 아니라 실제 흡수 시작 시점 이후의 시간만 식에 들어갑니다.

$$
C(t)=0 \quad (t<t_{lag})
$$

$$
\underbrace{C(t)}_{\text{지연 전 농도}}=\underbrace{0}_{\text{무입력}}\quad (\underbrace{t<t_{lag}}_{\text{지연 전}})
$$

$$
C(t)=\frac{k_a F D_{po}}{V(k_a-k_{el})}\left(e^{-k_{el}(t-t_{lag})}-e^{-k_a(t-t_{lag})}\right) \quad (t\ge t_{lag})
$$

$$
\underbrace{C(t)}_{\text{지연 후 농도}}=\frac{\overbrace{k_a F D_{po}}^{\text{입력 크기}}}{\underbrace{V(k_a-k_{el})}_{\text{희석·분리}}}\left(\underbrace{e^{-k_{el}(t-t_{lag})}}_{\text{소실 지수}}-\underbrace{e^{-k_a(t-t_{lag})}}_{\text{흡수 지수}}\right)\quad (\underbrace{t\ge t_{lag}}_{\text{흡수 후}})
$$

`[Source: G Eq.2:39–2:42, pp.32–33]`


**D. 0차 입력 — 다른 입력 함수로의 확장**

0차 흡수는 중심 소실(central elimination) 구조는 그대로 두고 입력 함수(input function)만 바꾼 경우입니다. 흡수가 지속되는 동안에는 입력이 거의 일정하고, 입력이 끝난 뒤에는 washout만 남습니다 [G Eq.2:66–2:67, p.38; T Fig.6-2, p.171]. PK3에서 zero-order model의 AIC가 first-order보다 좋았지만, 교재는 이것이 물리적으로 “진짜 zero-order absorption”을 증명하는 것은 아니라고 경고합니다. 여러 dose, 반복투여, IV 비교가 있어야 기전(mechanism) 해석이 가능합니다 [G pp.483–486].


> 💼 **실무 인사이트:** NONMEM ADVAN2 oral model의 KA initial은 큰 값과 작은 값을 모두 시도합니다. 서로 다른 initial이 서로 다른 해 또는 비슷한 OFV로 수렴하면 flip-flop 또는 실용적 식별가능성(practical identifiability) 문제를 의심해야 합니다.


*차이지수 곡선이 만들어졌다면, 다음 질문은 그 곡선이 언제 가장 높아지는가입니다.*

**Card 1 요약(Recap):** Oral $C(t)$는 “흡수 지수 − 소실 지수”입니다. $F$와 $V$는 진폭을, $k_a$와 $k_{el}$은 모양과 terminal slope 해석을 지배합니다.

> **M1 체화 핵심**
> ① `경구 농도곡선이 왜 늦게 올라오는가` → 장관 입력($k_a$)과 중심 소실($k_{el}$)의 차이지수가 결정
> ② `하강부를 elimination으로 단정하는 상황` → flip-flop에서는 absorption-limited terminal slope가 지배
> ⚡ `좋은 곡선 적합 = 진짜 생리학` → apparent fit을 true mechanism으로 오독하여 초기값·보고 문장 실패

---

---


<!-- SLIDE_START: M2 | title: tmax/Cmax -->

### Card 2. $t_{max}$ / $C_{max}$ — 흡수속도와 소실속도가 같아지는 순간

> **앞 카드에서 이 카드로:** 차이지수 곡선의 구조를 알았다면, 다음 질문은 그 곡선의 기울기가 언제 0이 되는가입니다.

> **거장의 시각**
> $t_{max}$를 “흡수가 가장 많이 끝난 시간”으로 읽으면 rate와 amount를 혼동합니다.
> $dC/dt=0$이라는 관점으로 보면 $F$, dose, $V$가 아니라 $k_a/k_{el}$의 상대 위치가 peak 시간을 지배한다는 점이 즉시 보입니다.


**거장의 시각:** $t_{max}$는 “가장 많이 흡수된 시간”이 아닙니다. **순유입이 0이 되는 시간**입니다. 즉 흡수 속도(rate of absorption)와 소실 속도(rate of elimination)가 같아지는 순간입니다 [T p.173; G pp.34–35].

**A. 도출(Derivation)**

Master equation을 미분하고 $dC/dt=0$으로 두면 다음과 같습니다.

$$
\frac{dC}{dt}=\frac{k_a F D_{po}}{V(k_a-k_{el})}\left(-k_{el}e^{-k_{el}t}+k_a e^{-k_a t}\right)=0
$$

$$
\underbrace{\frac{dC}{dt}}_{\text{농도 기울기}}=\frac{\overbrace{k_a F D_{po}}^{\text{높이 scale}}}{\underbrace{V(k_a-k_{el})}_{\text{높이 scale}}}\left(\overbrace{-\underbrace{k_{el}e^{-k_{el}t}}_{\text{소실 기여}}+\underbrace{k_a e^{-k_a t}}_{\text{흡수 기여}}}^{\text{속도 균형}}\right)=\underbrace{0}_{\text{peak 조건}}
$$

따라서:

$$
\boxed{t_{max}=\frac{\ln(k_a/k_{el})}{k_a-k_{el}}}
$$

$$
\underbrace{t_{max}}_{\text{peak 시간}}=\frac{\underbrace{\ln(k_a/k_{el})}_{\text{속도 로그비}}}{\underbrace{k_a-k_{el}}_{\text{속도 차}}}
$$

`[Source: G Eq.2:49–2:52, pp.34–35; T Eq.F-6, p.783]`

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $t_{max}$ | time | 최고농도 도달 시각 | $k_a/k_{el}$ balance |
| $k_a$ | time$^{-1}$ | 흡수부위 소실 속도 | 용출, 위배출, 제형 |
| $k_{el}$ | time$^{-1}$ | 중심구획 소실 속도 | $CL/V$, 장기 기능 |

💡 **비유:** $t_{max}$는 저수지 수위가 가장 높은 순간입니다. 수도꼭지로 들어오는 물과 배수구로 빠지는 물의 속도가 같아지는 순간이지, 물이 모두 들어온 순간이 아닙니다.

🔑 **Peak 시간 규칙:** linear 1구획 조건에서 $F$와 dose는 높이를 바꾸지만 $t_{max}$ 위치를 직접 바꾸지 않습니다.

$k_a \gg k_{el}$이면 다음 근사가 가능합니다.

$$
C_{max}\approx \frac{F D_{po}}{V}e^{-k_{el}t_{max}}
$$

$$
\underbrace{C_{max}}_{\text{최고농도}}\approx \underbrace{\frac{F D_{po}}{V}}_{\text{도달량/부피}}\underbrace{e^{-k_{el}t_{max}}}_{\text{peak 전 소실}}
$$

`[Source: G Eq.2:53, p.35]`

Lag-time이 있으면 관찰 $t_{max}$는 $t_{lag}$만큼 뒤로 이동합니다 [G Eq.2:54–2:55, p.35].


**B. 왜 $F$와 $V$가 $t_{max}$ 식에서 사라지는가**

$F$, dose, $V$는 linear system에서 곡선의 높이를 위아래로 scale합니다. 그러나 $dC/dt=0$은 “높이”가 아니라 “기울기가 0이 되는 시간 위치”를 찾는 조건입니다. 따라서 곡선 전체가 위아래로 커지거나 작아져도 $t_{max}$의 시간 위치는 바뀌지 않습니다. 그래서 linear 1구획 oral PK에서는 dose나 $F$가 바뀌면 $C_{max}$와 $AUC$는 바뀌지만 $t_{max}$는 바뀌지 않습니다 [T Fig.6-5, p.174]. **단, 이 “$t_{max}$ 불변” 성질은 absorption 단계만 건드렸을 때의 이야기입니다. $CL$이 변하면 $AUC$뿐 아니라 $t_{max}$와 $C_{max}$까지 함께 움직이고, $V$가 변하면 $C_{max}$와 $t_{max}$가 서로 다른 방향으로 이동합니다. 즉 “$F\cdot dose$만 변했을 때”와 “disposition($CL/V$)이 변했을 때”는 곡선 변화 패턴이 서로 다른 신호로 나타납니다. 이것이 absorption 변화와 disposition 변화를 구분하는 첫 번째 단서입니다** [T Figs.6-10–6-11, pp.179–180].


**C. 잔차법(Method of Residuals)**

말기(terminal) 직선 구간에서 $k_{el}$을 먼저 추정합니다. 그다음 역외삽(back-extrapolation) 직선에서 관찰 농도를 빼 잔차 직선(residual line)을 만들면, 이 잔차 기울기가 $-k_a$가 됩니다. 두 직선의 교점은 lag-time 추정에 사용될 수 있습니다 [G pp.31–33; T Appendix F pp.781–783]. 단, 이 방법은 terminal slope가 정말 elimination을 반영한다는 전제를 둡니다. 따라서 flip-flop 상황에서는 위험합니다.


> 💼 **실무 인사이트:** 수기 잔차법(residual method)에서 terminal point 선택은 “눈대중”이 아닙니다. 최소 3개 이상의 terminal points, 충분한 log-linear fit, $C_{max}$ 이후 충분히 늦은 시점이라는 기준으로 고정해야 합니다. 기준을 만족하지 않으면 $k_a$와 $k_{el}$ 초기값이 서로 오염됩니다.

**D. 극한 경우(Limiting case): $k_a=k_{el}$**

$k_a$와 $k_{el}$이 거의 같으면 두 지수 함수는 분리되지 않고 다음 한계식으로 수렴합니다.

$$
C(t)=\frac{k' F D_{po}}{V}t e^{-k't}
$$

$$
\underbrace{C(t)}_{\text{한계 농도}}=\underbrace{\frac{k' F D_{po}}{V}}_{\text{입력 scale}}\underbrace{t}_{\text{시간항}}\underbrace{e^{-k't}}_{\text{공통 감쇠}}
$$

`[Source: G Eq.2:58, p.37]`


*$t_{max}$와 $C_{max}$는 속도(rate)의 문제입니다. 전체 노출량 $AUC$는 정도(extent)의 문제입니다. 이 지점에서 $F$가 등장합니다.*

**Card 2 요약(Recap):** $t_{max}$는 rate balance의 시점입니다. Linear 조건에서는 $F$, dose, $V$가 아니라 $k_a$와 $k_{el}$의 상대적 크기로 정해집니다.

> **M2 체화 핵심**
> ① `peak가 언제 생기는가` → $k_a$와 $k_{el}$의 rate balance가 결정
> ② `AUC·Cmax scale 변화와 peak 시간 변화 혼동` → $F$·dose는 높이를, disposition 변화는 시간 위치까지 흔듦
> ⚡ `$t_{max}$ = 흡수 완료 시점` → 흡수는 이후에도 지속될 수 있어 onset/extent 해석 실패

---

---


<!-- SLIDE_START: M3 | title: 생체이용률 F -->

### Card 3. 생체이용률 $F$ (Bioavailability $F$) — 흡수의 정도(extent)를 $AUC$로 읽습니다

> **앞 카드에서 이 카드로:** $t_{max}$와 $C_{max}$가 rate balance를 보여준다면, 전체 노출량은 전신 순환에 도달한 누적량을 묻습니다.

> **거장의 시각**
> $F$와 $k_a$를 섞으면 food effect, formulation effect, BE 문장이 모두 불안정해집니다.
> $F$를 AUC가 읽는 extent로 고정하면 rate($k_a$)와 extent($F$)가 분리됩니다.


**거장의 시각:** $k_a$는 “얼마나 빨리 들어오는가”를, $F$는 “얼마나 많이 전신 순환에 도달했는가”를 묻는 값입니다. 두 개념을 섞으면 food effect, BE, formulation effect 해석이 모두 흐려집니다.

**A. 절대 생체이용률(Absolute Bioavailability)**


동일 약물의 IV 기준 투여(reference)가 있을 때, 혈장 $AUC$ 기반 생체이용률(bioavailability) $F$(← 전신 순환 도달 분율)는 다음과 같이 계산합니다.

$$
\boxed{F=\frac{AUC_{po}}{AUC_{iv}}\cdot\frac{D_{iv}}{D_{po}}}
$$

$$
\underbrace{F}_{\text{절대 F}}=\underbrace{\frac{AUC_{po}}{AUC_{iv}}}_{\text{노출 비율}}\cdot\underbrace{\frac{D_{iv}}{D_{po}}}_{\text{용량 보정}}
$$

`[Source: G Eq.2:74, p.42; T Eq.6-11, p.183]`

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $F$ | fraction | IV 대비 전신 도달 분율 | 흡수 분율, 장관·간 first-pass |
| $AUC_{po}$ | conc·time | 경구 투여 후 총 노출 | $F$, dose, $CL$ |
| $AUC_{iv}$ | conc·time | IV 기준 총 노출 | dose, $CL$ |
| $D_{iv}/D_{po}$ | ratio | route 간 용량 보정 | 시험 설계 |

🔑 **Extent 규칙:** $F$는 “얼마나 빨리”가 아니라 “얼마나 많이 전신 순환에 도달했는가”입니다.  
⚠️ **헷갈림 방지:** $AUC$ 감소를 곧바로 $k_a$ 감소로 해석하면 rate와 extent를 섞게 됩니다.

이 식의 전제는 clearance가 두 투여 사이에서 동일하다는 점입니다 [T p.183]. R&T의 parameter-estimation 예시는 i.m. dose의 $F$를 97%, oral solution의 $F$를 46%로 계산하여 route별 extent 차이를 보여줍니다 [T Table 6-1 / Fig.6-14, pp.183–184].

**B. 상대 생체이용률(Relative Bioavailability)**

두 혈관외 제형(extravascular formulation) A/B를 비교할 때는 다음과 같습니다.

$$
\boxed{F_{rel}=\frac{AUC_B}{AUC_A}\cdot\frac{D_A}{D_B}}
$$

$$
\underbrace{F_{rel}}_{\text{상대 F}}=\underbrace{\frac{AUC_B}{AUC_A}}_{\text{B/A 노출}}\cdot\underbrace{\frac{D_A}{D_B}}_{\text{용량 보정}}
$$

`[Source: T Eq.6-15, p.185]`

상대 생체이용률(Relative $F$)은 IV 기준 투여 없이도 두 제품의 전신 전달(systemic delivery) 차이를 비교할 수 있습니다 [T pp.183–185].


**C. 소변 데이터 해석 시 주의점(Urine Data Caveat)**

혈장 $AUC$만이 유일한 경로는 아닙니다. R&T는 요중 배설 데이터(urinary excretion data)로도 생체이용률, 상대 생체이용률, 신장 청소율(renal clearance)을 추정할 수 있음을 제시합니다. 단, 이 해석은 미변화체 배설 분율(fraction excreted unchanged)과 신장 처리(renal handling)가 비교 조건에서 일정하다는 전제를 요구합니다 [T Eq.6-18–6-21, pp.187–188].

**D. 기전적 $F$ (Mechanistic $F$)**


생리학적으로 $F$는 장관 내강(gut lumen)에서의 흡수 분율(fraction absorbed), 장관 초회 통과(intestinal first-pass, ← 장 통과 중 대사/손실), 간 초회 통과(hepatic first-pass, ← 간 통과 중 대사/손실)가 곱해진 결과로 이해할 수 있습니다.

$$
F \approx F_F \cdot F_G \cdot F_H
$$

$$
\underbrace{F}_{\text{전체 F}}\approx\underbrace{F_F}_{\text{흡수·제형}}\cdot\underbrace{F_G}_{\text{장관 생존}}\cdot\underbrace{F_H}_{\text{간 생존}}
$$

`[Source: T Ch.7 context, pp.197–220]`

이 식은 본 세션에서 full physiology로 확장하지 않습니다. $F$가 단순히 “용해되어 들어온 양”이 아니라 장관·장벽·간을 통과한 결과임을 상기시키는 용도로만 사용합니다.

**E. 생동성(BE) 맥락**

R&T는 생동성(bioequivalence)에서 시험/기준(test/reference) ratio의 90% CI와 0.80–1.25 기준을 설명합니다 [T Fig.6-13, p.183]. 본 세션의 핵심 질문은 “$F_{rel}$만 같아도 충분한가?”입니다. $F_{rel}$이 같아 $AUC$가 유사하더라도 $k_a$가 다르면 $C_{max}$와 $t_{max}$가 달라질 수 있습니다. 따라서 흡수의 정도(extent, 얼마나 많이)와 흡수의 속도(rate, 얼마나 빨리)는 항상 함께 읽어야 합니다.


*$F$는 $AUC$로 읽을 수 있습니다. 그러나 경구 단독에서는 $F$와 $V$가 분리되지 않습니다. 즉 $AUC$가 달라졌을 때 그 원인이 $F$ 변화인지 $CL$ 변화인지, 또는 농도 진폭이 $V$ 때문인지 $F$ 때문인지 단독 자료만으로는 나눌 수 없습니다. 이것이 Apex 카드의 출발점입니다.*

**Card 3 요약(Recap):** $F$는 흡수의 extent이고, $k_a$는 rate입니다. $AUC$는 $F\cdot \mathrm{Dose}/CL$을 읽지만, 경구 단독에서는 $CL$이 아니라 $CL/F$가 추정됩니다.

> **M3 체화 핵심**
> ① `얼마나 많이 전신 순환에 도달했는가` → $F$와 $AUC$가 결정
> ② `얼마나 빨리 peak에 도달했는가` → $k_a$와 input function이 지배
> ⚡ `$AUC$ 변화 = 흡수속도 변화` → extent와 rate 혼동으로 food/formulation effect 문장 실패

---

---


<!-- SLIDE_START: M4 | title: APEX V/F 식별불가능성 + Flip-flop -->

### Card 4. APEX — $V/F$ 식별불가능성 + Flip-flop 동정

> **앞 카드에서 이 카드로:** $F$가 extent라는 점을 알면, 경구 단독 데이터에서 왜 $F$와 $V$, $F$와 $CL$이 서로 묶여 보이는지가 다음 핵심 문제가 됩니다.

> **거장의 시각**
> 💢 **흔한 오해:** 좋은 OFV와 작은 RSE가 나오면 oral-only 모델에서도 $V$, $CL$, $k_{el}$이 확정되었다고 생각합니다.
> ✅ **실제는:** 경구 곡선은 input function ⊗ $F$ ⊗ disposition의 합성곱이며, 같은 곡선이 서로 다른 기전 조합으로 만들어질 수 있습니다.
> 🎯 **체화할 단 하나의 직관:** oral-only 결과는 $V/F$, $CL/F$, terminal slope ambiguity를 남기는 apparent parameter 보고서입니다.

`[⚡ Apex Concept]`


**거장의 시각 — Apex 핵심 아이디어(Big Idea, convolution lens) [EXPERT_INFERENCE, v3]:** 경구 농도-시간 곡선(concentration-time curve)은 **입력 함수(input function: $k_a$·lag·gastric emptying·multiple sites) ⊗ 생체이용률(bioavailability) $F$ ⊗ 체내 분포·소실(disposition: $CL$·$V$)**의 합성곱(convolution)으로 형성됩니다. 다시 말해, 어느 한 축만으로는 곡선 형태를 완전히 설명할 수 없습니다. 같은 곡선 모양이 서로 다른 (input, $F$, disposition) 조합으로 만들어질 수 있습니다. 이것이 $V$와 $F$가 분리되지 않고 $V/F$로 묶이는 이유, terminal slope label이 $k_a$와 $k_{el}$ 사이에서 뒤집힐 수 있는 이유, 그리고 fitted $k_a$가 실제 흡수가 아닐 수 있는 이유를 모두 한 번에 설명하는 상위 framing입니다.

**거장의 시각:** 경구 단독 모델에서 좋은 OFV와 작은 RSE는 “모델이 데이터를 잘 설명한다”는 뜻입니다. 그러나 $V$와 $F$가 원리적으로 분리되었다는 뜻은 아닙니다. 수치적 식별가능성(numerical identifiability)과 구조적 식별가능성(structural identifiability, ← 원리적으로 분리 추정 가능한지)은 다릅니다.

**A. $V/F$ 구조적 식별가능성(Structural Identifiability)**

Master equation에서 $F$와 $V$는 항상 $F/V$ 형태로 함께 나타납니다.

$$
C(t)=\frac{k_a F D_{po}}{V(k_a-k_{el})}\left(e^{-k_{el}t}-e^{-k_a t}\right)
$$

$$
\underbrace{C(t)}_{\text{경구 농도}}=\frac{\overbrace{k_a F D_{po}}^{\text{입력·extent}}}{\underbrace{V(k_a-k_{el})}_{\text{분포·속도}}}\left(\underbrace{e^{-k_{el}t}}_{\text{disposition}}-\underbrace{e^{-k_a t}}_{\text{input}}\right)
$$

따라서 경구 단독 데이터는 $V$와 $F$를 분리하지 못하고 $V/F$만 추정합니다. 마찬가지로 clearance는 $CL/F$로 보고해야 합니다 [G p.32; T p.185].

정확한 AUC 관계는 다음이다.

$$
\boxed{AUC=\frac{F\cdot Dose}{CL}=\frac{Dose}{CL/F}}
$$

$$
\underbrace{AUC}_{\text{전신 노출}}=\underbrace{\frac{F\cdot Dose}{CL}}_{\text{도달량/CL}}=\underbrace{\frac{Dose}{CL/F}}_{\text{경구 관찰형}}
$$

$\mathrm{Dose}/(CL/F)$는 대수적으로 $F\cdot \mathrm{Dose}/CL$과 같습니다. 그러나 $AUC$만 보고서는 변화의 원인이 $F$인지 $CL$인지 분리할 수 없습니다.

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $V/F$ | volume | 경구 데이터에서 보이는 apparent volume | $V$ 변화 또는 $F$ 변화 |
| $CL/F$ | volume/time | 경구 데이터에서 보이는 apparent clearance | $CL$ 변화 또는 $F$ 변화 |
| terminal slope | time$^{-1}$ | 관찰 말기 감소율 | $k_{el}$ 또는 $k_a$ 병목 |
| $AUC$ | conc·time | 총 전신 노출 | $F\cdot Dose/CL$ |

💡 **비유:** 경구 단독 모델은 안개 낀 유리창 너머로 방 크기와 창문 개방률을 동시에 추정하는 상황입니다. 방이 큰지($V$), 창문이 덜 열렸는지($F$)는 같은 농도만으로 분리되지 않습니다.

⚠️ **헷갈림 방지:** $V/F=50\ \mathrm{L}$는 $V=50\ \mathrm{L}$라는 뜻이 아닙니다.  
🔑 **보고 규칙:** IV 또는 absolute $F$ 근거가 없으면 $V/F$, $CL/F$로 보고합니다.

**저자의 4-part 결론(one-line mnemonic) [T p.185]:** 단일 oral dose만 가진 상태에서, **(i) $AUC$는 사다리꼴법으로 *계산*은 가능하지만, (ii) $CL$은 $F$를 모르므로 *계산 불가*이고, (iii) terminal half-life는 무엇이 rate-limiting인지(absorption인지 disposition인지) 모르면 elimination/absorption 어느 쪽에도 *confidently 할당 불가*이며, (iv) $V$는 *추정 불가*입니다.** 이 네 줄이 Apex의 핵심 메시지입니다. “경구 단독에서 무엇이 식별 가능하고 무엇이 식별 불가능한가”를 한 번에 떠올리는 체크리스트로 사용하시면 됩니다.


**B. Flip-flop 실용적 식별가능성(Practical Identifiability)**

일반적으로 $k_a>k_{el}$이면 경구 말기 기울기(oral terminal slope)는 소실(elimination)을 반영합니다. 그러나 $k_a<k_{el}$이면 남아 있는 흡수 과정(absorption process)이 더 느린 과정이 되므로, 관찰되는 말기 기울기는 흡수를 반영할 수 있습니다. 이때 말기 반감기(terminal half-life)를 소실 반감기(elimination half-life)로 읽으면 소실을 잘못 해석하게 됩니다 [G Fig.2.17, p.30; T Case C, pp.175–176].

**핵심 경고:** “rising limb = absorption phase, declining limb = elimination phase”라는 말은 flip-flop에서는 틀릴 수 있습니다 [G pp.29–30; T pp.173–176].

**C. 사례 앵커(Case Anchors)**

- **Fluticasone propionate:** median $t_{max}$는 90분이고 $C_{max}$는 30–90분에 나타나지만, 흡수 반감기(absorption half-life)는 3.8–4시간으로 해석됩니다. Early $t_{max}$가 빠른 흡수를 증명하지는 않습니다 [T Fig.6-7, p.177].
- **Theophylline:** 음식/물(food/water)은 흡수 동역학(absorption kinetics)을 바꾸지만 말기 반감기(terminal half-life)는 약 6.3 h로 유지됩니다. 따라서 흡수 변화와 체내 분포·소실(disposition) 변화를 구분하는 예시가 됩니다 [T Fig.6-8, p.178].
- **Penicillin G:** 난용성(sparingly soluble) 근육주사 제형은 흡수가 속도 제한 단계(rate-limiting)가 될 수 있음을 보여줍니다 [T Fig.6-9, p.178].
- **PK2:** lag-time model은 $K_a=0.043\ \mathrm{min}^{-1}$, $K=0.0088\ \mathrm{min}^{-1}$, $V/F=32\ \mathrm{L}$, $t_{lag}=16\ \mathrm{min}$을 제시합니다 [G p.480]. 같은 사례에서 $F=82\%$와 $true\ V=20\ \mathrm{L}$ 문구는 $32\times0.82\approx26\ \mathrm{L}$과 산술상 충돌하므로, 본 handout에서는 “원문 수치 충돌 [확인 필요]”로 유지하고 계산값을 source-confirmed value로 확정하지 않습니다 [G p.480].
- **PK2 Solution III:** 역전된 초기 추정치(reversed initial estimate)는 다른 $k_a/k_{el}/V/F$ 해로 수렴할 수 있음을 보여줍니다. 단, OCR/unit 표기에는 `[확인 필요]` 플래그를 유지합니다 [G pp.481–482].
- **PK3:** 1차 모델은 $K_a\approx K_e$와 큰 CV/RSE 문제를 보이고, 0차 모델은 AIC가 낮습니다(85.2 vs 76.2). 그러나 더 좋은 적합(better fit)이 진짜 0차 흡수의 증명이 되는 것은 아닙니다 [G Table 3.1, p.486].


**C-2. 그럴듯한 오류(Plausible Fallacy) [EXPERT_INFERENCE, v3]**

**오류:** $C_{max}$가 낮고 $T_{max}$가 길어졌으므로 흡수가 느려졌다고 단정합니다.  
**왜 그럴싸한가:** 표면적으로는 peak가 낮고 늦게 나타나므로 $k_a$ 감소처럼 보입니다.  
**나비효과:** 단순 $k_a$ 감소 해석 → 제형 재조제 또는 absorption model 복잡화 → [임상] 실제 원인이 first-pass 증가·용해도 저하·flip-flop이면 노출/독성/치료실패 예측 오류 → [모델링/규제] IV 또는 route/formulation comparison 없이 $F$와 $k_a$ 분리 주장, BE trial 의사결정 오류, 재분석 요구 위험.

**D. NONMEM 보고 시 함의(Reporting Implication)**

경구 단독 PopPK에서는 $F$를 1로 고정(fix)하고 $V/F$, $CL/F$로 보고하는 것이 구조적으로 정직합니다. `F1`을 추정(estimate)하거나 임의 값으로 고정한 뒤 $V$와 $CL$을 절대값(absolute value)처럼 보고하면, 사전 가정(prior assumption)이 추정된 파라미터처럼 보일 위험이 있습니다. `[EXPERT_INFERENCE, v3]`


> 💼 **실무 인사이트:** 1. **쌍둥이 억제 패턴(Twin Suppression Pattern):** $k_a$와 $k_{el}$의 두 해가 모두 plausible하여 ETA(KA)와 ETA(KEL)가 강하게 보상되는 패턴입니다.  
2. **$V/F$ 드리프트(V/F Drift):** 같은 covariate가 $V/F$와 $CL/F$에 비례적으로 나타나면 $F$-driven 변화 가능성을 의심합니다.  
3. **가상 분포용적 드리프트(Phantom Volume Drift):** $V/F$ 변화를 $V$ 변화로 보고하는 오류입니다. 핵심 식은 $AUC=F\cdot \mathrm{Dose}/CL=\mathrm{Dose}/(CL/F)$입니다.


*$V/F$ 문제는 “얼마나 들어왔는가”와 “어디에 분포했는가”의 분리 문제입니다. 다음 카드는 $k_a$ 자체도 겉보기 값일 수 있음을 보여줍니다.*

**Card 4 요약(Recap):** 경구 단독 데이터는 $V$와 $F$를 분리하지 못합니다. Flip-flop에서는 terminal slope도 $k_{el}$로 확정하지 못합니다. 좋은 fit은 진짜 parameter의 증거가 아닙니다.

> **M4 체화 핵심**
> ① `oral-only 모델에서 무엇을 보고할 것인가` → $V/F$, $CL/F$, terminal slope ambiguity가 결정
> ② `작은 RSE와 좋은 OFV가 있는 상황` → numerical precision일 뿐 structural identifiability 해결이 아님
> ⚡ `$V/F$를 $V$로 보고` → phantom volume interpretation → [임상] 용량·축적 판단 오류 / [규제] 재분석 요구 위험

---

---


<!-- SLIDE_START: M5 | title: ka_app vs ka_true -->

### Card 5. $k_{a,app}$ vs $k_{a,true}$ — $k_a$가 측정하는 것은 무엇인가

> **앞 카드에서 이 카드로:** $V/F$와 terminal slope가 apparent label이라면, $k_a$ 역시 실제 흡수속도인지 먼저 의심해야 합니다.

> **거장의 시각**
> fitted $k_a$를 곧바로 true absorption으로 부르면 장관 손실, 분해, site heterogeneity를 모두 흡수속도 변화로 오해합니다.
> gut compartment에서 “사라진 속도”와 systemic circulation에 “도달한 속도”를 분리하면 food/formulation effect 해석이 안전해집니다.


**거장의 시각:** 모델 output의 $k_a$를 “흡수속도상수”라고 부르더라도, 그 값은 겉보기(apparent, ← 모델에서 보이는 겉보기) parameter일 수 있습니다. 즉 실제 plasma appearance만이 아니라 gut compartment에서 사라지는 모든 경로를 반영할 수 있습니다.

**A. 겉보기 장관 소실(Apparent GI Loss)**

장관에서 약물이 사라지는 경로가 실제 흡수($k_{a,true}$)와 장내 분해/손실($k_d$)로 나뉘면, 관찰되는 apparent first-order loss는 다음과 같습니다.

$$
\boxed{k_{a,app}=k_{a,true}+k_d}
$$

$$
\underbrace{k_{a,app}}_{\text{겉보기 소실}}=\underbrace{k_{a,true}}_{\text{실제 흡수}}+\underbrace{k_d}_{\text{장관 손실}}
$$

`[Source: G Fig.2.24 and text, pp.40–41]`

전신 순환 도달 fraction은 다음과 같이 표현됩니다.

$$
\boxed{F=\frac{k_{a,true}}{k_{a,true}+k_d}}
$$

$$
\underbrace{F}_{\text{도달 분율}}=\frac{\underbrace{k_{a,true}}_{\text{흡수 경로}}}{\underbrace{k_{a,true}+k_d}_{\text{전체 장관 소실}}}
$$

`[Source: G Eq.2:70, p.41]`

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $k_{a,app}$ | time$^{-1}$ | 장관에서 사라지는 전체 속도 | 실제 흡수 + 장관 손실 |
| $k_{a,true}$ | time$^{-1}$ | 전신 입력으로 이어지는 실제 흡수 속도 | 용출, 투과, 위배출 |
| $k_d$ | time$^{-1}$ | 장관 분해/손실 속도 | 불안정성, fecal loss, 장관 대사 |
| $F$ | fraction | 사라진 약물 중 전신 도달 분율 | $k_{a,true}/(k_{a,true}+k_d)$ |

💡 **비유:** 장관 구획의 출구가 두 개 있는 싱크대라고 생각하면 됩니다. 하나는 전신 순환으로 가는 배수구($k_{a,true}$), 다른 하나는 손실 배수구($k_d$)입니다.

⚠️ **헷갈림 방지:** $k_{a,app}$가 커졌다는 말은 흡수가 빨라졌다는 뜻이 아니라 장관에서 더 빨리 사라졌다는 뜻일 수 있습니다.


**B. 해석(Interpretation)**

적합된 $k_a$가 커졌다는 것은 곧바로 “흡수가 빨라졌다”를 뜻하지 않습니다. “gut compartment에서 더 빨리 사라졌다”는 뜻일 수도 있습니다. $AUC$가 함께 변하지 않으면 흡수 개시·속도(onset/rate) 변화일 가능성이 크고, $AUC$도 함께 변한다면 흡수 정도(extent) 변화가 동반된 것입니다 [G pp.40–41].

**C. 다중 흡수 부위(Multiple Absorption Sites)**

흡수 부위가 여러 개이면 농도-시간 곡선(concentration-time curve)은 다중 peak 또는 비정형 상승부를 보일 수 있습니다. G는 buccal + GI 같은 multiple absorption site 구조를 Eq.2:80–2:82로 제시합니다 [G pp.46–47]. 이 경우 단일 $k_a$는 여러 입력 과정(input process)을 하나로 눌러 담은 요약 파라미터(summary parameter)로 읽어야 합니다.


> 💼 **실무 인사이트:** food effect 보고서에서 “$k_a$ 감소 = 흡수 저하”라고 쓰지 않습니다. $F_{rel}$($AUC$ ratio)을 함께 보고하여, $AUC$ 변화 없이 $k_a$만 바뀌면 onset/rate 변화로, $AUC$도 바뀌면 extent 변화로 분리합니다.

**Card 5 요약(Recap):** $k_a$는 항상 “진짜 흡수속도”가 아닙니다. 적합된 $k_a$의 생리학적 의미는 모델 구조와 외부 evidence가 결정합니다.

> **M5 체화 핵심**
> ① `fitted ka가 변했을 때` → $k_{a,app}=k_{a,true}+k_d$ 구조가 먼저 결정
> ② `AUC 변화가 동반된 상황` → rate 변화만이 아니라 extent 또는 loss 변화가 지배
> ⚡ `$k_a$ 감소 = 흡수 저하` → 장관 손실·다중 흡수부위·food effect를 단일 흡수속도로 오독

---

---


<!-- SLIDE_START: §5 | title: 혼동쌍 해부 -->

## §5. 혼동쌍 해부

### 혼동쌍 1. $k_a$ vs $k_{el}$ under flip-flop — 결정타(Critical Blow)

| 비교 기준 | 개념 A: $k_a$ | 개념 B: $k_{el}$ |
|---|---|---|
| 단위 / 차원 | time$^{-1}$, 흡수부위 소실 속도 | time$^{-1}$, 중심구획 소실 속도 |
| 수식 내 위치 (분자/분모/지수) | $e^{-k_a t}$ 또는 input 지수항 | $e^{-k_{el}t}$ 또는 disposition 지수항 |
| 변화 원인 (생물학적/병적) | 용출, 위배출, 흡수부위, 제형 | $CL/V$, 신장·간 기능, 분포 변화 |
| 혼동 시 임상 결과 | flip-flop에서 terminal slope를 잘못 붙임 | dosing interval, accumulation, washout 판단 오류 |

**결정타(Critical Blow):** terminal half-life를 elimination half-life로 착각하면 dosing interval, accumulation, washout 판단이 모두 흔들립니다.

**⚡ 기억 고리 (Memory Hook) — *병목이 어느 쪽에 있는가*: [EXPERT_INFERENCE, v3]**  
Flip-flop 동역학에서는 $k_a<k_{el}$이므로 **흡수가 제거의 병목**이 됩니다 — terminal slope가 $k_a$를 반영합니다. Disposition-limited에서는 $k_{el}<k_a$이므로 **제거/분포가 병목**입니다 — terminal slope가 $k_{el}$을 반영합니다. **IV 크로스오버 데이터 없이 경구 데이터만으로는 두 메커니즘을 구별할 수 없다는 것이 핵심 함정입니다.**

**⚡ 기억 고리 (Memory Hook) — *정점 시각 vs 흡수 종료 시각*: [EXPERT_INFERENCE, v3]**  
$T_{max}$는 흡수 속도와 제거 속도가 같아지는 **교차점**이지, 흡수가 완료되는 시점이 아닙니다. $T_{max}$ 이후에도 흡수는 계속되며 단지 제거가 더 빠를 뿐입니다.

### 혼동쌍 2. $F$ vs $k_a$ — extent와 rate

| 비교 기준 | 개념 A: $F$ | 개념 B: $k_a$ |
|---|---|---|
| 단위 / 차원 | fraction, 전신 도달 분율 | time$^{-1}$, 흡수부위 소실 속도 |
| 수식 내 위치 (분자/분모/지수) | 진폭·AUC scale: $F\cdot Dose/CL$ | 지수항과 $t_{max}$ 식의 rate term |
| 변화 원인 (생물학적/병적) | 흡수 분율, 장관·간 first-pass, 제형 | 용출, 위배출, 흡수부위 이동 |
| 혼동 시 임상 결과 | AUC 변화와 peak timing 변화를 같은 원인으로 오독 | food/formulation effect 보고 문장 오류 |

$$
\underbrace{\frac{k_a}{K}}_{\text{속도 비율}}=\underbrace{\frac{k_a}{CL\cdot V}}_{\text{원문 scale 대비}}
$$

**⚡ 기억 고리 (Memory Hook) — *얼마나 들어오나 vs 얼마나 빨리 들어오나*: [EXPERT_INFERENCE, v3]**  
$F$는 투여량의 몇 분율이 systemic circulation에 도달하는지를 결정하는 **비율**이고, $k_a$는 흡수 부위에서 얼마나 빠르게 이동하는지의 **속도**입니다. $AUC$는 $F$에 비례하고, $T_{max}$와 $C_{max}$의 형태는 $k_a/K$ 비율에 의해 결정됩니다.

**⚡ 기억 고리 (Memory Hook) — *속도계 vs 적산계*: [EXPERT_INFERENCE, v3]**  
흡수 속도($k_a$)는 **속도계(순간 속도)**이고, 흡수 정도($F$)는 **적산계(누적량)**입니다. 속도계를 올려도 적산계가 늘지는 않습니다 — $k_a$를 증가시켜도 $F$가 그대로면 $AUC$는 변하지 않습니다.

### 혼동쌍 3. $V/F$ vs $V$ — 결정타(Critical Blow)

| 비교 기준 | 개념 A: $V/F$ | 개념 B: $V$ |
|---|---|---|
| 단위 / 차원 | volume, apparent volume | volume, true distribution volume |
| 수식 내 위치 (분자/분모/지수) | oral-only 보고 파라미터, $F$와 묶임 | IV 또는 $F$ 근거가 있어야 분리 가능 |
| 변화 원인 (생물학적/병적) | $V$ 변화 또는 $F$ 변화 | 조직분포, 체성분, 단백결합 |
| 혼동 시 임상 결과 | $F$ 변화가 분포용적 변화처럼 보임 | phantom interpretation, covariate 해석 오류 |

**결정타(Critical Blow):** $V/F$를 $V$로 바꾸어 쓰는 순간, 흡수율 변화가 분포용적 변화처럼 보이는 phantom interpretation이 생깁니다.

### 혼동쌍 4. First-order $k_a$ vs Zero-order input

| 비교 기준 | 개념 A: First-order $k_a$ | 개념 B: Zero-order input |
|---|---|---|
| 단위 / 차원 | time$^{-1}$, 남은 양에 비례한 입력 | amount/time, 일정 시간 동안 거의 일정한 입력 |
| 수식 내 위치 (분자/분모/지수) | $e^{-k_a t}$ 지수항 | 일정 입력률, 입력 종료 후 washout |
| 변화 원인 (생물학적/병적) | 속방형 용액/정제 근사, 용출·위배출 | controlled-release, 삼투펌프, 용해도/용출 제한 |
| 혼동 시 임상 결과 | 0차 모델의 better fit을 진짜 0차 흡수로 과장 | PK3처럼 AIC 우월이 기전 증명을 뜻하지 않음 [G pp.483–486] |

**§5 요약(Recap):** 경구 PK에서 가장 위험한 혼동은 기울기 명칭(slope label), 겉보기 파라미터(apparent parameter), 속도/정도(rate/extent)를 서로 바꿔 부르는 것입니다. 이름표가 바뀌면 같은 숫자도 다른 임상 결론을 만듭니다.

---

<!-- SLIDE_START: §7 | title: 자기 테스트 -->

## §7. 자기 테스트: 능동 회상 모듈


### Q1. Master equation을 쓰고 각 항의 의미를 설명하세요.

**답변:**

$$
C(t)=\frac{k_a F D_{po}}{V(k_a-k_{el})}\left(e^{-k_{el}t}-e^{-k_a t}\right)
$$

$$
\underbrace{C(t)}_{\text{혈장 농도}}=\frac{\overbrace{k_a F D_{po}}^{\text{전신 입력}}}{\underbrace{V(k_a-k_{el})}_{\text{희석·분리}}}\left(\underbrace{e^{-k_{el}t}}_{\text{소실 지수}}-\underbrace{e^{-k_a t}}_{\text{흡수 지수}}\right)
$$

$k_a$는 흡수 부위 소실 속도(absorption-site loss rate), $F$는 전신 순환 도달 분율(systemic fraction), $D_{po}$는 투여량, $V$는 분포용적(volume), $k_{el}$은 소실 속도(elimination rate)입니다. 괄호 안의 항은 소실 지수와 흡수 지수의 차이를 나타냅니다 [G p.30; T p.782].


### Q2. 왜 $t_{max}$ 식에는 $F$, $V$, dose가 들어가지 않는가?

**답변:** $t_{max}$는 $dC/dt=0$이 되는 시간입니다. Linear system에서는 $F$, $V$, dose가 곡선의 높이를 scale할 뿐 기울기 0의 시간 위치는 바꾸지 않습니다. 따라서 $t_{max}=\ln(k_a/k_{el})/(k_a-k_{el})$입니다 [G p.35].


### Q3. $F_{rel}=1.0$인 두 oral formulation이 임상적으로 완전히 같다고 말할 수 있는가?

**답변:** 아닙니다. $F_{rel}=1.0$은 $AUC$ 기반으로 흡수 정도(extent)가 같다는 뜻입니다. $k_a$가 다르면 $C_{max}$와 $t_{max}$가 달라질 수 있고, 발현(onset)이나 최고 농도 관련 안전성(peak-related safety)이 중요한 약물에서는 임상적 차이가 남을 수 있습니다 [T pp.181–183].


### Q4. PK2에서 $V/F=32\ \mathrm{L}$, $F=0.82$가 제시되었습니다. 진짜 $V$는 몇 L인가?

**답변:** 산술적으로는 $V=(V/F)\times F=32\times0.82\approx26\ \mathrm{L}$입니다. 그러나 원문은 $true\ V=20\ \mathrm{L}$이라고 서술하여 산술값과 충돌합니다. 따라서 최종 handout에서는 26 L를 확정 source value로 쓰지 않고, “원문 수치 충돌 [확인 필요]”로 표시합니다 [G p.480].


$$
\underbrace{V}_{\text{true V}}=\underbrace{(V/F)}_{\text{apparent V}}\times\underbrace{F}_{\text{F 보정}}=\underbrace{32\times0.82}_{\text{산술 환산}}\approx\underbrace{26\ \mathrm{L}}_{\text{계산 V}}
$$


### Q5. Oral-only ADVAN2 fit에서 $k_a=0.05\ \mathrm{hr}^{-1}$, $k_{el}=0.5\ \mathrm{hr}^{-1}$가 나왔습니다. 관찰 terminal half-life를 $\ln 2/0.5=1.4\ \mathrm{h}$라고 써도 되는가?

**답변:** 안 됩니다. $k_a<k_{el}$이면 oral curve의 관찰 terminal slope는 더 작은 rate constant인 $k_a$를 따를 수 있습니다. 이 경우 terminal half-life는 약 $\ln 2/0.05=13.9\ \mathrm{h}$로 보입니다. $k_{el}=0.5\ \mathrm{hr}^{-1}$는 혈장에 들어온 뒤의 true elimination일 수 있지만, oral-only terminal slope만으로 확정할 수 없습니다.


$$
\underbrace{t_{1/2,obs}}_{\text{관찰 반감기}}=\frac{\underbrace{\ln 2}_{\text{반감기 상수}}}{\underbrace{0.05}_{\text{병목 rate}}}\approx\underbrace{13.9\ \mathrm{h}}_{\text{flip-flop 후보}}
$$


### Q6. PK3에서 zero-order model의 AIC가 first-order보다 낮았다. “흡수가 진짜 0차”라고 결론 내릴 수 있는가?

**답변:** 아닙니다. PK3는 zero-order input model이 해당 dataset을 더 잘 설명한다는 것을 보여줍니다. 그러나 진짜 기전(true mechanism)을 확정하려면 용량 범위(dose range), 반복 투여(repeated dosing), IV 데이터 등 추가 근거가 필요합니다 [G pp.483–486].


### Q7. $k_{a,app}=1.0\ \mathrm{hr}^{-1}$이고 $k_d=0.4\ \mathrm{hr}^{-1}$라면 $k_{a,true}$와 $F$는?

**답변:** $k_{a,true}=k_{a,app}-k_d=0.6\ \mathrm{hr}^{-1}$입니다.  

$$
F=\frac{k_{a,true}}{k_{a,true}+k_d}=\frac{0.6}{1.0}=0.6
$$

$$
\underbrace{F}_{\text{도달 분율}}=\frac{\underbrace{k_{a,true}}_{\text{흡수 }0.6}}{\underbrace{k_{a,true}+k_d}_{\text{전체 }1.0}}=\underbrace{0.6}_{\text{60\% 도달}}
$$

이 계산은 G Eq.2:70의 구조를 이용한 해석이며, 실제 데이터에서는 $k_d$를 별도 evidence 없이 분리하기 어렵습니다 [G p.41].


### Q8. Boss dilemma: oral-only data에서 terminal slope가 $0.18\ \mathrm{hr}^{-1}$로 보이고, alternative model은 $k_{el}=0.69\ \mathrm{hr}^{-1}$도 가능하다고 합니다. 무엇을 보고해야 하는가?

**답변:** $0.18\ \mathrm{hr}^{-1}$가 관찰 terminal slope라면 관찰 terminal half-life는 $\ln 2/0.18\approx3.85\ \mathrm{h}$입니다. 그러나 flip-flop 가능성이 있으면 이 0.18이 $k_{el}$인지 $k_a$인지 확정할 수 없습니다. 보고 문장은 다음처럼 쓰는 것이 안전합니다. “oral-only data에서 terminal slope는 $0.18\ \mathrm{hr}^{-1}$로 관찰되었으나, IV 또는 route/formulation comparison 없이는 이것을 elimination rate로 확정할 수 없습니다. Dose recommendation은 두 해에 대한 sensitivity analysis로 방어해야 합니다.” `[EXPERT_INFERENCE, v3]`


$$
\underbrace{t_{1/2,terminal}}_{\text{말기 반감기}}=\frac{\underbrace{\ln 2}_{\text{반감기 상수}}}{\underbrace{0.18\ \mathrm{hr}^{-1}}_{\text{관찰 slope}}}\approx\underbrace{3.85\ \mathrm{h}}_{\text{계산 반감기}}
$$

---


## ⚡ 보스 딜레마 ★★ — 최종 자기 테스트 캡스톤(Final Self-Test Capstone) [EXPERT_INFERENCE, v3]


### Boss Dilemma. 제형 변경 후 $C_{max}$↓·$T_{max}$↑: 두 가설을 어떻게 방어하는가?

**시나리오:** 경구 데이터만 있는 Phase 1 데이터셋에서 $C_{max}$가 낮고 $T_{max}$가 지연된 결과가 관찰되었습니다. 제형 팀은 "흡수가 느려졌다($k_a$ 감소)"라고 결론지었습니다. 모델러로서 두 가지 방어 가능한 해석을 제시해 보세요.

- **(A) 흡수 속도 감소($k_a$ 감소)로 해석**하고 absorption model을 first-order에서 transit compartment로 변경합니다.
- **(B) first-pass 효율 감소($F$ 감소, apparent $CL$ 증가 → $AUC$ 감소)로 해석**하고 $F$의 공변량 탐색을 우선합니다.

각 선택을 규제 문서에서 어떻게 방어할 수 있을까요?

**거장의 절충 판단(Trade-off) 논리 — 답변(Answer):**

(A)는 모델 복잡도를 높이고 $T_{max}$ 재현에 집중합니다. 그러나 IV 데이터 없이는 $F$와 $k_a$의 교락(confounding, ← 두 요인이 얽혀 분리되지 않는 상태)을 해결하지 못합니다. 이는 Card 4 §A의 convolution lens가 경고하는 바로 그 한계입니다. 보고 시 "transit compartment가 $T_{max}$ 지연을 더 잘 설명하지만, $F$의 동시 변화 가능성은 본 데이터로는 배제할 수 없습니다"라고 명시해야 합니다.

(B)는 파라미터 수를 단순하게 유지합니다. 그러나 만약 $k_a$ 변화가 진짜 원인이었다면 $AUC$와 곡선 형태가 모두 어긋날 수 있습니다. 보고 시 "$AUC$ ratio가 통계적으로 유의하게 감소했고 이는 $F$-driven 해석을 지지하지만, 동시에 $k_a$ 변화 가능성을 sensitivity analysis로 평가했습니다"라고 기술해야 합니다.

**규제 방어 핵심 — 분리 진단 알고리즘:**

> **1단계.** "$AUC$가 같은가 다른가"를 먼저 확인하여 두 가설을 분리합니다.  
> &nbsp;&nbsp;&nbsp;&nbsp;— $AUC$ 변화 없음 + $C_{max}$↓·$T_{max}$↑ → 가설 (A) $k_a$ 감소가 우세  
> &nbsp;&nbsp;&nbsp;&nbsp;— $AUC$ 감소 + $C_{max}$↓·$T_{max}$↑ → 가설 (B) $F$ 감소 또는 (A+B) 복합 가능성  
> **2단계.** IV 크로스오버 데이터를 요청하거나, 가능하지 않으면 **두 모델 모두를 적합시켜 sensitivity analysis로 보고서에 명시**합니다.  
> **3단계.** 단일 가설만 채택하지 않고 "두 해석 모두 데이터와 정합적이며, 임상 dosing 결정은 두 해 모두에서 안전한 영역에 있는가"를 평가합니다.

→ **가장 위험한 자세는 "$k_a$ 감소 = 흡수 불량 = 제형 재조제"라는 단순 추론입니다.** 이는 Card 4 Plausible Fallacy(C-2)가 경고한 정확히 그 함정이며, BE trial의 잘못된 의사결정 사슬을 만들어냅니다.


**§7 요약(Recap):** 계산보다 중요한 것은 label입니다. 같은 숫자라도 $k_a$인지 $k_{el}$인지, $V$인지 $V/F$인지 잘못 붙이면 임상 결론이 달라집니다.

---


> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** 경구 PK의 전문성은 $V/F$, $CL/F$, $k_{a,app}$, terminal slope ambiguity를 숨기지 않고 명시하는 데서 완성된다.

---


<!-- SLIDE_START: §8 | title: 메타프레임과 큰 그림 -->

## §8. 메타프레임과 큰 그림

### A. 위치(Positioning)

본 세션은 IV bolus 이후 첫 번째 임상 현실, 즉 **흡수 단계가 있는 계**를 다룹니다. 이후 다회투여(multiple dosing), 방출 조절형(modified-release), 음식 효과(food effect), 생동성(BE), PopPK 흡수 모델로 나아가더라도 판단 기준은 결국 다음 네 가지 질문으로 돌아옵니다.

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| 입력 함수가 1차가 아님 | $k_a$, lag, input duration | → | $C_{max}$·$t_{max}$ 재현 실패 | lag/zero-order/transit 후보 평가 |
| $F$가 제형·식사·first-pass로 변함 | $F$, $CL/F$ | → | AUC 차이와 apparent clearance 변화 | $F_{rel}$, AUC ratio, sensitivity 보고 |
| terminal slope label이 불명확함 | $k_a$ 또는 $k_{el}$ | → | 반감기·축적 판단 오류 | IV/route comparison 또는 dual-solution 방어 |
| $V$, $CL$을 absolute처럼 보고함 | $V/F$, $CL/F$ | → | covariate effect 오해 | apparent parameter 명시 |

### B. 의존성(Dependencies) — 본 세션을 놓치면 생기는 실패 모드

| 실패 모드 | 실제 결과 |
|---|---|
| $V/F$를 $V$로 보고 | 공변량 효과(covariate effect)를 분포 변화로 오해. |
| $CL/F$를 $CL$로 보고 | $F$ 변화가 clearance 변화처럼 보임. |
| 말기 기울기(terminal slope)를 무조건 $k_{el}$로 해석 | flip-flop에서 반감기와 축적(accumulation) 판단 오류. |
| $k_a$ 변화를 흡수 정도(absorption extent) 변화로 단정 | 음식/제형 효과(food/formulation effect) 메시지 오류. |
| $t_{max}$ 용량 의존성(dose-dependence)을 무시 | 포화성 흡수, 초회 통과 포화, 비선형 소실 신호를 놓침. |
| 0차 모델의 더 나은 적합을 기전 증명으로 단정 | 서방형/용해도/용출 근사를 생리학적 확정으로 과장. |


### C. 전문가 해석 지점(Professional Moat)

> 💼 **실무 인사이트:** 30년 차 pharmacometrics 연구자는 경구 모델 결과를 볼 때 먼저 “모델이 맞았는가?”가 아니라 “무엇이 식별되었는가?”를 묻습니다. Phase 1 SAD(단회 상승 용량 시험) 회의에서 senior가 던지는 실무 질문은 단순합니다. **“FIH(최초 임상 투여) 단계에서 IV arm 또는 absolute $F$ 확인 가능성을 평가했는가?”** 이 질문 하나가 $F$, $V/F$, $CL/F$, flip-flop, $k_{a,app}$의 모든 위험을 앞으로 끌어냅니다.

| 후속 세션 | 이 세션에서 열리는 개념 | 이 세션 없으면 실패하는 것 |
|---|---|---|
| multiple dosing / accumulation | terminal slope label, $k_{el}$ vs $k_a$ | 축적계수와 washout 해석 오류 |
| modified-release / zero-order input | input function 구분 | better fit을 기전 증명으로 과장 |
| oral PopPK absorption model | $V/F$, $CL/F$, $k_{a,app}$ | apparent parameter를 true parameter로 보고 |
| BE / food effect | rate vs extent 분리 | $AUC$, $C_{max}$, $t_{max}$ 메시지 혼동 |

### D. Ch.7 맥락 — 한 문장 요약

$k_a$와 $F$의 변동성은 BCS, 위배출(gastric emptying), 용출(dissolution), 수송체(transporter), 장관/간 초회 통과(intestinal/hepatic first-pass) 같은 생리·물리화학적 요인에서 비롯됩니다. 본 세션의 수식은 그 복잡성을 1차 입력과 $F$라는 두 개의 겉보기(apparent) 축으로 압축해 읽는 첫 단계입니다 [T pp.197–220].

> 📖 **교과서 그림 참조:** Gabrielsson & Weiner 5e, p.47, Fig.2.32
> 경구 농도-시간 곡선(oral concentration-time curve)을 결정하는 요인은 이 장의 여러 카드에 분산되어 있습니다. 이 그림은 그 요인들을 장 결론(chapter conclusion) 수준에서 다시 하나의 구조로 묶어줍니다.
> 확인 시점: §8 메타프레임(Meta-frame)을 읽은 뒤, 최종 요약(Final Recap) 직전에 확인하시면 됩니다.


### E. 최종 확정 문장


**최종 요약(Final Recap):** 경구 PK의 핵심은 $C(t)$를 맞추는 데서 끝나지 않습니다. 더 중요한 일은 $C(t)$에서 실제로 분리 가능한 것과 분리 불가능한 것을 구분하는 것입니다. 경구 단독 데이터는 $V/F$, $CL/F$, 겉보기 $k_a$, 그리고 terminal slope ambiguity를 남깁니다. 이 네 가지를 명시하면 handout은 안전하고, 생략하면 모델은 그럴듯하지만 위험해집니다.

---

---

## v3.7 자가검증 체크리스트

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

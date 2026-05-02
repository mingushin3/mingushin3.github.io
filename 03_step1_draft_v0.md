# Step 1 Draft v0 — 경구(혈관외) PK: F · ka · tmax · 흡수

**Source A (G):** Gabrielsson & Weiner 5e, Ch.2 §§2.2.4–2.2.12 (pp.28–47), PK2 (pp.476–482), PK3 (pp.483–486)
**Source B (T):** Rowland & Tozer 5e, Ch.6 (pp.169–195), Appendix F (pp.781–784)
**Mode:** B-Standard
**Symbol Convention:** **ka** (흡수속도상수), **kel** (소실속도상수, G의 K·T의 k 통일), **V/F** (겉보기 분포용적, 경구 단독 시), **CL/F** (경구 청소율)

---

## 📋 CURATION MAP

### MUST (체화 필수) — 5개 Concept Cards

| # | 개념 | 핵심 수식 / 출처 | MUST 판정 근거 |
|---|---|---|---|
| 1 | **C(t) 통합 방정식 (Master Equation)** | Eq.2:35 / G p.30; Eq.6-3 / T p.172 | 이 식 없이는 tmax·Cmax·AUC 모든 후속 개념이 무너짐. lag-time(Eq.2:39), 0차 입력(Eq.2:66)도 이 식의 변형. |
| 2 | **tmax / Cmax 해석적 도출** | Eq.2:52, Eq.2:53 / G p.35 | "흡수속도 = 소실속도"라는 동역학 평형 조건을 수식으로 결정화. 임상 PK·BE 평가의 표준 지표. |
| 3 | **Bioavailability F (정도 — Extent)** | Eq.2:74 / G p.42 | F는 ka(속도)와 본질적으로 다른 차원. AUC 비율법으로 추정. 경구 PK의 두 축(rate·extent) 중 하나. |
| 4 | **⚡ APEX: V/F 식별불가능성 + Flip-flop 동정** | §2.2.4 / G p.32; Ch.6 Case C / T p.175 | **이 세션의 가장 깊은 임상·규제 함의.** 경구 단독 데이터에서 추정한 모든 파라미터는 "겉보기(apparent)"이며, IV 비교 없이는 V·F·ka·kel 어느 것도 진짜 값이 아니다. PopPK 모델 해석·NDA 방어의 기본 전제. |
| 5 | **ka,app vs ka,true** | Eq.2:70 / G p.41 [확인 필요 — Fig.2.24 캡션 다이어그램; 별도 번호 수식 없음] | "ka는 무엇을 측정하는가"의 기계론적 답. 모델 적합 결과의 ka는 장관 소실(흡수 + 분해)을 모두 포함한 겉보기 값이라는 인식이 임상 해석의 기초. |

### CONTEXT (이해 보완) — 1–2문장으로 본문 내 흡수

| 항목 | 흡수될 카드 | 처리 방식 |
|---|---|---|
| Lag time (Eq.2:39, Eq.2:42) | Card 1 (C(t) 방정식) | "지연을 포함한 확장형"으로 1–2문장 추가 |
| 0차 흡수 모델 (Eq.2:66) + AIC 판별 (PK3) | Card 1 + §5 Confusion Pair | "대체 입력 함수"로 언급 + 혼동쌍에서 비교 |
| Method of Residuals (Eq.2:40–2:42, 2:53) | Card 2 (추정) | "초기 추정 그래프 기법"으로 1–2문장 + Trench Tip |
| Multiple absorption sites (Eq.2:80–2:82) | Card 5 (ka 해석) 또는 §8 | "ka의 다중 site 분해" 1문장 |
| Accumulation factor R (Eq.2:78), Multiple dosing | §8 Dependencies | 후속 개념으로 위치만 명시 |
| BCS, gastric emptying (T Ch.7) | §8 Big Picture | 흡수 변동성의 생리학적 근거로 1문장 |
| Vaughan / Pidgeon-Pitlick 대안 ka 추정법 (Eq.2:56, 2:57) | 본문 생략 | scope 외 (수식 도출 깊이 불필요, B-Standard) |

> **Note:** Rowland Ch.7(흡수 생리학, BCS, 위장 운동성)은 Scope Lock의 Phase 1 주의사항 ①에 따라 **수식 없는 서술적 내용은 §8 Big Picture에 1–2문장**으로만 처리. Crohn 질환·의약 운반체 등은 Phase 4 이후 압축 단계에서 재검토.

---

## §1. SESSION HEADER & ROADMAP

**Source:** Gabrielsson & Weiner 5e, Ch.2 §§2.2.4–2.2.12 + PK2/PK3 / Rowland & Tozer 5e, Ch.6 + Appendix F
**Pages:** G pp.28–47, 476–486 / T pp.169–195, 781–784
**Title:** **경구 및 혈관외 투여의 PK — F · ka · tmax 그리고 흡수 단계가 만드는 모든 것**

### Big Idea (단 한 문장)

> **IV bolus는 "초기 농도 C₀를 제공하지만", 경구 투여는 "초기 농도가 0인 상태에서 두 개의 지수 함수가 경쟁하며 만들어내는 그래프"이며, 이 경쟁 구조 안에 V·F·ka·kel 네 파라미터가 서로 얽혀 IV 데이터 없이는 풀 수 없는 식별불가능성이 잠재되어 있다.**

### 개념 항법도 (이 세션의 5개 MUST)

```
①  C(t) Master Equation [Eq.2:35]
       │  "왜 이 형태인가" — ka·F·D / [V·(ka−kel)] · 차이지수
       ▼
②  tmax / Cmax [Eq.2:52, 2:53]
       │  "두 지수가 균형을 이루는 시점"의 해석적 결정
       ▼
③  F (Bioavailability) [Eq.2:74]
       │  "AUC 비율로만 측정 가능" — 정도(extent)의 척도
       ▼
④  ⚡ APEX: V/F 식별불가능성 + Flip-flop
       │  "경구 단독 데이터의 구조적 한계" — IV 없이는 진실을 모른다
       ▼
⑤  ka,app vs ka,true [Eq.2:70]
          "ka가 측정하는 것은 흡수가 아니라 장관 소실"
```

### 지식 그래프 위치

**선행 지식 (반드시 완료):**
- IV bolus PK (CL, V, t½, AUC) — 1구획 기본 동역학
- 1차 ODE 적분, 자연로그 / 지수 함수 미적분
- AUC 사다리꼴법 (NCA의 기초)

**바로 다음:** Multiple dosing (Eq.2:78 accumulation factor) → PopPK absorption submodels (transit compartment, Weibull) → Flip-flop 인식 하의 NONMEM 모델 코딩.

**결정적으로 의존하는 고급 도메인:**
- PopPK 흡수 서브모델 (NONMEM ADVAN2 / ADVAN4 / 사용자 정의 ODE)
- Bioequivalence 평가 (90% CI 0.80–1.25 기준)
- TDM 시 oral clearance(CL/F) 사용의 전제 조건
- 비선형 흡수 (포화 흡수, EHC), modified-release 제형 평가

---

## §2. CONCEPT ANATOMY CARDS

---

### **Card 1. C(t) Master Equation — 경구 PK의 모든 것이 시작되는 한 줄**

<!-- MASTER LENS -->
**[개념 Big Idea: 거장의 시각]**

**왜 치명적으로 중요한가:** 이 한 식의 *구조*를 멀리서 알아보지 못하면, NONMEM에서 ADVAN2 출력값을 보고도 "Cmax는 왜 dose에 비례하지 않을까?"라는 초보적 혼란에 빠진다. 그리고 Phase 1 보고서에 "V는 50L"라고 적었다가 심사관에게 "V/F 아닙니까?"라고 지적받는다.

**체화해야 할 단 하나의 직관:** *이 곡선은 "농도 함수"가 아니라, "두 지수의 차이 함수"다.* — 흡수가 만드는 상승 지수 e^(−ka·t)와 소실이 만드는 하강 지수 e^(−kel·t)가 시간 축 위에서 빼기를 수행한 결과이며, 두 지수의 *상대적 크기*가 곡선의 모양을 결정한다. ka ≫ kel이면 빠르게 올라갔다가 천천히 내려오고, ka ≪ kel이면 천천히 올라갔다가 빠르게 내려와야 하지만 — *바로 이 지점에서 flip-flop의 함정이 시작된다(Card 4 참조)*.

**이 직관을 머릿속에 박고 아래를 읽어라:** 모든 후속 수식 — tmax, Cmax, AUC, lag-time, V/F, ka,app — 은 이 차이 함수를 어떻게 측정하고 분해할 것인가에 대한 답이다.

---

**A. Formal Definition**

1구획 모델, 1차 흡수, 1차 소실을 가정한 경구 투여 후 혈장 농도 시간 곡선의 적분 해. 흡수 부위에서의 약물 양 감소(rate_loss = ka·D_po·e^(−ka·t))와 혈장 구획으로의 입력(rate_input = ka·F·D_po·e^(−ka·t))이 결합된 계의 해.

**B. Derivation / Code Structure**

ODE 시스템:

$$\frac{dA_g}{dt} = -k_a \cdot A_g \quad\text{(장관 소실)}$$

$$\frac{dC}{dt} = \frac{k_a \cdot F \cdot D_{po} \cdot e^{-k_a t}}{V} - k_{el} \cdot C \quad \text{(혈장 변화)}$$

`[출처: G 5e, Ch.2, p.30, Eq.2:32–2:34]`

적분 결과(Master Equation):

$$\boxed{C(t) = \frac{k_a \cdot F \cdot D_{po}}{V \cdot (k_a - k_{el})} \cdot \left[ e^{-k_{el} \cdot t} - e^{-k_a \cdot t} \right]}$$

`[출처: G 5e, Ch.2, p.30, Eq.2:35; T 5e, Ch.6 (서술적 설명, 수식은 Appendix F p.782, Eq.F-1)]`

**Lag-time 확장형 (실제 데이터 적합 시 거의 항상 필요):**

$$C(t) = \frac{k_a \cdot F \cdot D_{po}}{V \cdot (k_a - k_{el})} \cdot \left[ e^{-k_{el}(t-t_{lag})} - e^{-k_a(t-t_{lag})} \right], \quad C=0 \text{ if } t < t_{lag}$$

`[출처: G 5e, Ch.2, p.32, Eq.2:39]`

**라인별 해부:**
- 분자 `ka·F·D_po`: 흡수 부위에서 혈장으로 들어오는 *순간* 입력 강도(rate)
- 분모 `V·(ka−kel)`: 분포용적과 두 속도상수 차이의 곱 — *(ka−kel)은 두 지수의 시간 분리도*
- 대괄호 `[e^(−kel·t) − e^(−ka·t)]`: t=0에서 0(둘 다 1), t=∞에서 0(둘 다 0), 중간에 양수 피크 → tmax에서 최대

**대체 입력 함수 — 0차 흡수 모델 (PK3):**

$$C(t) = \frac{R_{in}}{V \cdot k_{el}} \left[ 1 - e^{-k_{el} \cdot T_{abs}} \right] e^{-k_{el} \cdot t'}$$

여기서 R_in = 0차 입력률, T_abs = 흡수 지속 시간(parameter로 추정), t' = t − T_abs (흡수 종료 후 시간). `[출처: G 5e, Ch.2, p.38, Eq.2:66]` 이는 동일한 1구획 + 정주 infusion 모델 구조의 변형 — *입력 함수만 다르다*.

**C. Structural Necessity**

왜 이 형태일 수밖에 없는가? 1차 ODE 시스템 두 개(장관 → 혈장 → 소실)가 직렬로 연결되어 있고, 각각이 1차 동역학을 따르면, 적분해는 *반드시* 두 지수의 차이 형태를 가진다. 다른 형태는 다음과 같은 가정 위반 시에만 발생:
- 흡수 또는 소실이 비선형(Michaelis-Menten) → 차이지수 형태 깨짐
- 장관에서 혈장으로의 입력이 0차 → 위 0차 모델로 변형
- 다구획 분포(2-compartment) → 대괄호 안에 항이 추가됨

**ka = kel 한계 사례:** 분모 (ka − kel) = 0이 되어 식이 발산. 극한 처리 시 `C = (k'·F·D_po/V)·t·e^(−k'·t)` 형태(Eq.2:58 / G p.37). controlled-release 제형에서 가끔 등장.

**D. Assumptions & Boundary Conditions**

| 가정 | 위반 시 결과 |
|---|---|
| 1구획 분포 | 다지수 감쇠 → 2-compartment 모델 필요 |
| 1차 흡수, 1차 소실 | dose-dependent kinetics → 비선형 모델 |
| F·V·ka·kel 시간 불변 | non-stationarity → 시간 가변 covariate 필요 |
| 흡수와 소실이 독립적 | 장간순환(EHC) → 다중 peak |
| ka ≠ kel | 한계식(Eq.2:58)으로 reparameterization 필요 |
| 흡수 부위 한 곳 | 다중 peak (sublingual + GI 흡수, Eq.2:82) |

**E. Limitations**

- *부르카노프 효과:* 같은 데이터를 두 다른 (ka, kel) 조합이 동등하게 잘 적합할 수 있다 → **flip-flop (Card 4)**.
- 첫 시점(t < 흡수 lag)의 농도가 0이 아닌 경우 → lag-time 또는 Erlang/transit compartment 필요.
- Cmax 부근 곡선이 평평하여 tmax 추정 노이즈 큼 → BE 평가 시 tmax는 90% CI 비교 대상이 아님 (T pp.182–183).

**F. Five Cognitive Layers (요약 매핑)**

| Layer | 이 카드 안에서의 의미 |
|---|---|
| L1 형식적 수학 | Eq.2:35의 ODE 도출 + 적분 + lag-time 확장 |
| L2 기하학적 직관 | 두 지수의 차이로 만드는 "솟은 후 가라앉는" 곡선 |
| L3 구조적 동일성 | 화학공학의 CSTR 직렬 반응, RC회로의 충방전 cascade |
| L4 생리학적 의미 | 장관 — 혈장 — 소실 기관의 순차 전달; F는 장벽·간 1차 통과를 모두 포함 |
| L5 실무 투영 | NONMEM ADVAN2 (`$SUBROUTINE ADVAN2 TRANS2`); R nlmixr2 `linCmt(ka, kel, ...)` |

**G. Zettelkasten Atom**

```yaml
---
aliases: [Master Equation, Bateman Equation, Oral 1-compartment first-order absorption]
tags: [pharmacometrics/pk/oral, model/1-compartment, equation/master]
up: "[[Oral PK MOC]]"
related: ["[[tmax derivation]]", "[[V over F identifiability]]", "[[Flip-flop]]", "[[Method of Residuals]]"]
source: "Gabrielsson 5e Ch.2 p.30 Eq.2:35; Rowland & Tozer 5e Appendix F p.782 Eq.F-1"
---
```
경구 1구획 1차 흡수 1차 소실 PK의 적분해는 두 지수의 차이 함수다: C = (ka·F·D)/(V·(ka−kel))·[e^(−kel·t) − e^(−ka·t)]. ka·F·D/V는 입력 강도, (ka−kel)은 두 지수의 시간 분리도. lag-time 추가 시 t를 (t−tlag)로 치환. ka = kel일 때만 한계식 C = (k'·F·D/V)·t·e^(−k't) 사용. *모든* 후속 oral PK 개념(tmax, Cmax, F 추정, flip-flop, V/F)이 이 한 식의 변형 또는 한계.

---

<!-- ANCHOR -->
*Master Equation의 형태 자체로는 tmax가 어디인지 알 수 없다 — 미분해서 0이 되는 시점을 찾아야 한다. 이것이 다음 카드의 출발점이다.*

---

### **Card 2. tmax / Cmax — "흡수속도 = 소실속도" 평형의 수학화**

<!-- MASTER LENS -->
**[개념 Big Idea: 거장의 시각]**

**왜 치명적으로 중요한가:** Bioequivalence 심사에서 Cmax 90% CI가 0.80–1.25를 벗어나면 BE 실패다. 그런데 학생들은 "Cmax는 dose/V"라는 IV 직관을 경구에 그대로 적용해서, 제형 변경 후 Cmax 변화를 *V 변화*로 잘못 해석한다. tmax가 ka와 kel 모두의 함수라는 사실(Eq.2:52)을 *외워둔* 사람과 *유도해본* 사람은 데이터 해석 깊이가 다르다.

**체화해야 할 단 하나의 직관:** *tmax는 시간 축 위에서 "흡수 펌프"와 "소실 펌프"의 출력이 정확히 같아지는 순간*이다 — Cmax는 "거기서의 농도"일 뿐, 별도의 본질적 의미는 없다. dC/dt = 0 조건은 ka·A_g(t) = kel·A(t)와 *같은* 진술이다.

**이 직관을 머릿속에 박고 아래를 읽어라:** 아래 도출은 "두 지수의 차이를 미분해서 0이 되는 점을 찾는다"는 직관의 형식적 표현이다.

---

**A. Formal Definition**

tmax = peak time, 혈장 농도가 최대값에 도달하는 시점. Cmax = 그 시점의 농도. 두 값 모두 ka, kel, F, D_po, V (단, tmax는 ka와 kel만의 함수)에 의해 결정.

**B. Derivation / Code Structure**

C(t) (Eq.2:35)를 t에 대해 미분:

$$\frac{dC}{dt} = \frac{k_a \cdot F \cdot D_{po}}{V \cdot (k_a - k_{el})} \cdot \left[ -k_{el} \cdot e^{-k_{el} t} + k_a \cdot e^{-k_a t} \right]$$

`[출처: G 5e, Ch.2, p.35, Eq.2:49]`

dC/dt = 0 조건에서, 분자 `ka·F·D_po·V/(ka−kel)`는 0이 아니므로 대괄호 = 0:

$$k_a \cdot e^{-k_a t_{max}} = k_{el} \cdot e^{-k_{el} \cdot t_{max}}$$

양변 자연로그 + 정리:

$$\boxed{t_{max} = \frac{1}{k_a - k_{el}} \cdot \ln\left(\frac{k_a}{k_{el}}\right)}$$

`[출처: G 5e, Ch.2, p.35, Eq.2:52]`

**Cmax는 tmax를 Eq.2:35에 대입:** ka ≫ kel 가정 하에:

$$C_{max} \approx \frac{F \cdot D_{po}}{V} \cdot e^{-k_{el} \cdot t_{max}}$$

`[출처: G 5e, Ch.2, p.35, Eq.2:53]`

이 근사형은 IV bolus의 C₀ = D/V를 흡수 후 *t_max만큼 시간이 지난 농도*로 본다는 의미.

**Lag-time 포함 시:** tmax → tmax + tlag, Cmax 식에서 t를 (tmax − tlag)로 대체. `[출처: G 5e, Ch.2, p.35, Eq.2:54, 2:55]`

**Method of Residuals — 초기 추정의 실무적 알고리즘 (CONTEXT 흡수):**
종말기 직선의 기울기 → kel 추정 → 후방 외삽선 → 관측값 차이(residual) → residual 직선 기울기 → ka 추정. 두 직선의 교점 → tlag. `[출처: G Ch.2 pp.32–33, Eq.2:40–2:42; T Appendix F p.782]` PK2 사례 적용 결과: ka = 0.043 min⁻¹, kel = 0.0088 min⁻¹, V/F = 32 L, tlag = 16 min `[출처: G PK2, p.480, Solution II]`.

<!-- TRENCH -->
**[Trench-Level Tip]** Method of Residuals로 얻은 ka, kel을 NONMEM `$THETA` 초기값으로 사용할 때, **고도로 상관된(correlated) 두 파라미터**임을 명심하라. PK2 Solution I처럼 둘이 거의 동일하면 표준오차가 폭발한다 (CV% 3400%). reparameterization으로 kel → CL/F (kel = CL/V)를 사용하면 상관이 줄어든다 — *CL/F는 종말기뿐 아니라 전체 곡선 정보로 결정되기 때문* `[출처: G p.38]`.

**C. Structural Necessity**

왜 tmax가 ka와 kel "둘 다"의 함수인가? 흡수와 소실 두 1차 과정의 *경쟁*이 tmax를 결정하기 때문. ka가 클수록 빨리 차오르지만, kel이 크면 빨리 빠진다. 두 인자의 *비율*이 tmax를 결정 (Eq.2:52에서 ln(ka/kel)이 분자). kel만으로 결정되는 IV의 t½ 직관과 결정적으로 다른 지점.

**D. Assumptions & Boundary Conditions**

- 1구획, 1차 흡수, 1차 소실 (Card 1과 동일)
- ka ≠ kel (한계 사례에서는 Eq.2:63: tmax = 1/k')
- 단일 흡수 부위 (다중 peak 시 명확한 tmax 정의 어려움)

**E. Limitations**

- 고차 모델(2-compartment with absorption)에서는 *해석적 tmax 공식이 없다* `[출처: G p.36 명시]`. 수치 미분 또는 시뮬레이션 필요.
- BE 평가에서 tmax는 90% CI 비교 대상이 아님 — 곡선이 peak 부근에서 평평해 sampling time에 민감 (T p.182).
- Method of Residuals는 ka·t와 kel·t가 명확히 분리될 때만 유효. PK2 Solution I처럼 둘이 비슷하면 실패 → lag-time 모델 또는 0차 모델 시도.

**F. Five Cognitive Layers**

| Layer | 의미 |
|---|---|
| L1 | dC/dt = 0 → 자연로그 변환 → 닫힌 해 (Eq.2:52) |
| L2 | 두 지수 곡선의 "교차점" — 한쪽 펌프 출력 = 다른 쪽 펌프 출력 |
| L3 | RC회로 charging→discharging 평형, predator-prey 동역학의 turning point |
| L4 | 위장관 통과 시간 + 간 1차 통과 + 분포로 결정되는 임상적 onset 시점 |
| L5 | NONMEM 출력에서 PRED tmax vs OBS tmax 비교; BE 평가 (FDA guidance) |

**G. Zettelkasten Atom**

```yaml
---
aliases: [tmax, peak time, Cmax, peak concentration]
tags: [pharmacometrics/pk/oral, parameter/derived]
up: "[[Master Equation Eq 2-35]]"
related: ["[[Method of Residuals]]", "[[Bioequivalence]]", "[[Flip-flop]]"]
source: "Gabrielsson 5e Ch.2 p.35 Eq.2:52, Eq.2:53"
---
```
tmax = ln(ka/kel)/(ka−kel)는 dC/dt=0의 해석해. tmax는 ka·kel 비율의 함수이며 dose에 무관, Cmax는 dose에 비례 (선형 PK). lag-time 시 tmax→tmax+tlag. 2-compartment 등 고차 모델에서는 해석해가 없어 수치 계산. BE에서 tmax는 90% CI 평가 대상이 아니다.

---

<!-- ANCHOR -->
*tmax/Cmax는 단일 곡선의 *형태(rate)*를 결정하지만, 두 약물이 같은 형태라도 *총량*이 다를 수 있다. 경구 흡수의 두 번째 축 — 정도(extent) — 는 별도의 측정 도구가 필요하다.*

---

### **Card 3. F (Bioavailability) — 정도(Extent)의 절대적 측정**

<!-- MASTER LENS -->
**[개념 Big Idea: 거장의 시각]**

**왜 치명적으로 중요한가:** F를 *속도(rate)*와 혼동한 채 NDA를 제출하면 심사관은 "F는 AUC 비율로 정의되며, ka는 별개의 파라미터"라는 한 줄 코멘트로 회신한다. F = 0.5는 "흡수가 절반"이지 "흡수가 절반 속도로"가 아니다. 그리고 F는 *오직 IV 비교*로만 추정 가능하다.

**체화해야 할 단 하나의 직관:** F는 *시간을 모두 적분한 후*의 비율이다 — AUC라는 면적이 시간 정보를 모두 흡수해버리고 *총량*만 남긴 것. 따라서 F를 측정하려면 같은 약물의 IV AUC가 *반드시* 필요하다(Eq.2:74). 이 사실이 V/F 식별불가능성(Card 4)의 출발점이다.

**이 직관을 머릿속에 박고 아래를 읽어라:** F의 정의식에 IV AUC가 들어있다는 사실을 보면, 왜 경구 단독으로는 F를 알 수 없는지가 즉각 이해된다.

---

**A. Formal Definition**

F (bioavailability) = 투여한 dose 중 *전신 순환에 도달한 분율*. 단위 없음. IV 직접 투여의 F = 1 (정의상). 경구·근주·피하 등 혈관외 투여의 F ≤ 1.

**B. Derivation / Code Structure**

청소율 일정 가정 하에 (CL_iv = CL_po):

IV: $\quad D_{iv} = CL \cdot AUC_{iv}$

경구: $\quad F \cdot D_{po} = CL \cdot AUC_{po}$

두 식 나누기:

$$\boxed{F = \frac{AUC_{po}}{AUC_{iv}} \cdot \frac{D_{iv}}{D_{po}}}$$

`[출처: G 5e, Ch.2, p.42, Eq.2:74; T 5e, Ch.6, p.183, Eq.6-11]`

**상대적 생체이용률 (Relative Bioavailability) — IV 데이터 없을 때:**

$$F_{rel} = \frac{F_B}{F_A} = \frac{AUC_B}{AUC_A} \cdot \frac{D_A}{D_B}$$

`[출처: T 5e, Ch.6, p.185, Eq.6-15]`

두 경구 제형 간 비교 또는 BE 평가에 사용. *절대적 F는 알 수 없지만 비율은 알 수 있다*.

**Compartmental approach (동시 적합):** Civ + Cpo 합 모델로 두 데이터셋 동시 적합, F·V·CL·ka 모두 분리 추정. `[출처: G 5e, Ch.2, p.42, Eq.2:71–2:73]`

**기계론적 분해:** F는 흡수 부위에서의 투과율(F_F), 장벽 1차 통과(F_G), 간 1차 통과(F_H)의 곱:

$$F = F_F \cdot F_G \cdot F_H$$

`[출처: T 5e, Ch.7, Eq.7-1, p.204]`

여기서 F_H = 1 − E_H (간 추출률)이며 Q_H · CL_H 관계식으로 예측 가능 (T Eq.7-4 well-stirred model).

**C. Structural Necessity**

F가 AUC 비율로만 정의될 수밖에 없는 이유: bioavailability는 본질적으로 *총량 보존* 원리에서 나온다. 흡수된 총량 = 소실된 총량 = CL × AUC. 따라서 같은 CL을 두 경로에서 공유한다고 가정하면, AUC 비율이 흡수된 총량 비율(=F)이 된다. 시간 의존적 정보(ka, tmax)는 모두 적분으로 사라진다.

**D. Assumptions & Boundary Conditions**

| 가정 | 위반 시 |
|---|---|
| CL_iv = CL_po (시간·경로 불변) | 효소 유도/억제 → F 추정 편향 |
| 선형 PK (dose-proportional AUC) | 비선형 → dose별 F 다름 |
| AUC가 t=∞까지 적분 가능 | 종말 외삽 오차 → 작은 dose일수록 AUC_inf 추정 어려움 |
| 동일 화학적 형태로 측정 | 활성 대사체 간섭 → 청정 측정법 필수 |

**E. Limitations**

- IV 제형이 없거나 (대분자 약물 등) 안전성 이슈로 IV 투여 불가능한 경우, **절대 F는 영원히 알 수 없다**.
- 위장관 분해(F_F < 1)와 간 1차 통과(F_H < 1)를 *plasma 데이터만으로는* 분해 불가 → 동위원소 표지 또는 도관(portal vein cannulation) 동물 실험 필요.
- F < 1의 원인이 ka,true 감소(흡수 자체)인지 kd 증가(장관 분해)인지를 plasma 데이터로 분리 불가 → Card 5 (ka,app vs ka,true)로 연결.

**F. Five Cognitive Layers**

| Layer | 의미 |
|---|---|
| L1 | F = AUC_po·D_iv / (AUC_iv·D_po) (Eq.2:74) |
| L2 | 두 곡선이 만드는 "면적 비율" — 시간 정보가 적분으로 휘발 |
| L3 | 회계의 "유입 총합 / 발행 총합" 비율; 화학 반응의 yield |
| L4 | F = F_F·F_G·F_H — 위장관 흡수율 × 장벽 통과율 × 간 통과율 |
| L5 | NCA toolset (Phoenix WinNonlin, R `PKNCA`); NONMEM `F1` parameter |

**G. Zettelkasten Atom**

```yaml
---
aliases: [bioavailability, F, extent of absorption, relative bioavailability]
tags: [pharmacometrics/pk/oral, parameter/extent]
up: "[[Oral PK MOC]]"
related: ["[[V over F identifiability]]", "[[ka,app vs ka,true]]", "[[Bioequivalence]]"]
source: "Gabrielsson 5e Ch.2 p.42 Eq.2:74; Rowland & Tozer 5e Ch.6 p.183 Eq.6-11"
---
```
F = (AUC_po/AUC_iv)·(D_iv/D_po). CL 일정 가정 필수. F는 *오직* IV 데이터 비교로 추정 가능. 두 경구 제형 비교는 F_rel만 가능. F = F_F·F_G·F_H로 위장관·장벽·간 1차 통과로 분해. F<1의 원인을 분해하려면 동위원소 또는 portal cannulation 필요 — plasma 데이터만으로는 불가.

---

<!-- ANCHOR -->
*F가 IV 데이터를 요구한다는 사실이 결정적 결과를 낳는다 — 경구 단독 데이터로 추정한 V는 V가 아니라 V/F이고, ka는 ka가 아니라 겉보기 ka다. 이 식별불가능성이 다음 카드의 핵심.*

---

### **Card 4. ⚡ APEX — V/F 식별불가능성 + Flip-flop 동정**

> **[⚡ Apex Concept]** *이 세션의 가장 깊은 함의를 담은 카드. 임상·규제·NONMEM 실무 모두에 직접적 파급력을 가진다.*

<!-- MASTER LENS -->
**[개념 Big Idea: 거장의 시각]**

**왜 치명적으로 중요한가:** 신약개발 회의에서 후배 모델러가 "Phase 1 oral 데이터로 V = 32 L, CL = 2.8 L/h를 얻었다"고 발표한다. 30년 차 senior 모델러는 한 마디로 끝낸다 — *"V/F 아니면 V?"* 이 질문에 즉답하지 못하는 모델러는, 그 모든 covariate analysis와 PopPK 모델을 *겉보기 파라미터의 환상* 위에 쌓아올린 것이다. 그리고 flip-flop을 모르는 채 "이 약은 t½가 4시간이다"라고 임상의에게 보고했다가, 사실 그것이 ka였음이 IV 후속 시험에서 드러나면 — 용량 간격 결정 전체가 틀린다.

**체화해야 할 단 하나의 직관:** *경구 데이터만으로 적합한 모델의 모든 파라미터에는 보이지 않는 1/F이 곱해져 있거나(V/F, CL/F), 또는 ka와 kel이 서로 자리를 바꿔도 데이터를 동등하게 잘 설명한다(flip-flop).* 이 두 모호성은 같은 뿌리에서 나온다 — *Master Equation에 F와 V가 결합된 형태로만 나타나며, ka와 kel은 대칭 위치에 있다*. **확실성의 유일한 출처는 IV 비교 데이터다.**

**이 직관을 머릿속에 박고 아래를 읽어라:** 아래는 두 식별불가능성 — V/F (구조적 identifiability)와 flip-flop (수치적 identifiability) — 이 같은 모델 구조에서 어떻게 출현하는지를 추적한다.

---

**A. Formal Definition**

**V/F 식별불가능성:** 경구 투여 단독 데이터에서, F와 V는 항상 비율 V/F로만 추정 가능하며 개별 분리 불가능. 이것은 **구조적(structural) identifiability** 결손 — 모델 식 자체가 두 파라미터를 결합된 형태로만 포함.

**Flip-flop:** ka와 kel을 서로 교환한 두 모델이 동일한 C(t) 곡선을 산출. 이것은 **수치적(practical) identifiability** 결손 — 데이터 적합 시 두 해(solution)가 동등하게 best fit. ka < kel일 때 (controlled-release 또는 일부 long t½ 약물) 발생.

**B. Derivation / Code Structure**

**V/F의 출현 — Eq.2:35를 다시 보자:**

$$C(t) = \frac{k_a \cdot F \cdot D_{po}}{V \cdot (k_a - k_{el})} \cdot \left[ e^{-k_{el} t} - e^{-k_a t} \right]$$

분자에 F, 분모에 V가 있다. 두 인자의 비 F/V는 *함께* 곡선의 진폭(amplitude)에 작용한다. 데이터 적합 알고리즘은 *F/V*를 추정하지, F와 V 각각을 분리할 수 없다. 따라서 추정된 V는 실제로는 V/F (apparent volume), CL은 CL/F (oral clearance). `[출처: G 5e, Ch.2, p.32 명시]`

**PK2 검증 사례:** Solution II에서 V/F = 32 L 추정. 같은 환자 IV 데이터로부터 deconvolution한 F = 0.82를 적용 → 진짜 V = V/F · F = 32 × 0.82 ≈ 26 L. *그러나 본문에는 V = 20 L로 보고됨 — 이는 F=0.625 가정 시* `[확인 필요 — G p.480, "F of 82%, one can calculate the true volume of distribution V of 20 L" 라고 명시됨; 0.82 × 32 ≠ 20이므로 본문 명시값과 계산 불일치, 별도 deconvolution 결과 또는 다른 산출 경로 추정]`.

**Flip-flop의 출현:**

Eq.2:35의 대괄호 안 `[e^(−kel·t) − e^(−ka·t)]`에서, ka와 kel을 swap하면:
- `[e^(−ka·t) − e^(−kel·t)]` = `−[e^(−kel·t) − e^(−ka·t)]` (부호만 반대)

분모 (ka − kel)도 (kel − ka)로 부호 반대. **부호가 두 번 뒤집어져 결과적으로 동일한 C(t)**. 따라서 (ka, kel) = (1.0, 0.1)과 (ka, kel) = (0.1, 1.0)이 동일한 곡선을 만든다.

**판별의 유일한 길:** IV bolus 후 종말기 기울기로 *진짜 kel*을 측정. 경구 곡선의 종말기와 비교:
- 평행 (parallel) → 경구 종말기 기울기 = kel → ka > kel (정상)
- 비평행 → 경구 종말기 기울기 = ka → ka < kel (flip-flop). `[출처: G Fig.2.17, p.30; T Ch.6 Case C, p.175]`

**Fluticasone propionate 예시 (T Fig.6-7):** tmax 30–90분으로 빠르지만 흡수 t½는 3.8시간 — 흡수가 율속 단계. IV 데이터 없이는 빠른 onset처럼 보이는 곡선이 사실은 흡수-제한임을 알 수 없음.

**PK2 Solution III 검증:** 초기 추정값 ka = 0.01, kel = 0.1 min⁻¹로 reverse 적합 시, 최종 추정값은 ka = 0.0088, kel = 0.043 min⁻¹로 *수렴*. 같은 데이터에 두 해(0.0088/0.043과 0.043/0.0088)가 동등하게 적합. V/F 추정값도 32 L → 6.54 L로 *6배 변동* → 임상 용량 결정에 치명적.

**C. Structural Necessity**

V/F는 왜 분리 불가능한가? 입력 함수가 `ka·F·D_po`이고 출력 함수가 `kel·V·C`인데, 적합되는 데이터는 C 단독이다. 두 식에서 F와 V는 각각 한 번씩만 등장하며, 같은 식 (Eq.2:35) 안에서 곱으로만 결합되어 출현. **따라서 데이터로 분리할 수 없는 것이 수학적 필연이다.**

Flip-flop은 왜 발생하는가? 두 지수의 차이 함수는 두 지수에 대해 *대칭적* — 어느 것이 흡수이고 어느 것이 소실인지 식 자체에는 구분 정보가 없다. 라벨(label)은 *외부* 정보 (IV 데이터)에서만 온다.

---

**[C-2 Plausible Fallacy — 그럴싸한 오류]**

**오류의 형태:** "Phase 1 oral 데이터로 PopPK 모델을 적합시켜 V_pop = 50 L, CL_pop = 5 L/h를 얻었다. 이 환자군의 신부전(CrCl 30) 영향을 보기 위해 V_pop을 그대로 covariate analysis 기준값으로 쓰면 된다." — 직관적으로는 합리적, *근본적으로 오류*.

**나비효과 추적:**
1. V_pop은 사실 V/F이며, 신부전이 F에 영향을 미치는지(예: 장관 P-gp 발현 변화, 간 효소 변화) plasma 데이터로 분해 불가능.
2. NONMEM에서 "신부전 환자의 V/F가 30% 증가"가 관측되어도, 이것이 진짜 V 증가인지 F 감소인지 알 수 없음.
3. 만약 F 감소가 원인이라면, 진짜 V는 변하지 않은 것 — 부하 용량(loading dose)을 조정할 필요 없음. 그러나 "V가 30% 증가"라고 해석하면 부하 용량을 30% 증가시켜 *과량 투여*.
4. AUC = F·D/(CL/F)·F = D/CL_true이므로, *AUC 자체는 covariate effect로 정확히 측정됨* — 그러나 partition을 잘못한 채 dose 조정을 V·CL 분해로 하면 위험.

**GOF Signature 명명 — "Phantom Volume Drift":**
이 오류는 *직접적인 GOF 플롯에는 보이지 않음*. 모델이 데이터를 잘 적합시키고, η-shrinkage도 정상이며, OFV 감소도 합당함. **그러나 IV 데이터를 추가한 후속 시험 또는 multiple-dose accumulation profile에서 예측이 빗나간다** — 단일 dose에서 합당했던 V/F가 multiple dose의 steady-state 농도를 과소/과대 예측하면, 사실 F의 dose-dependence(첫 통과 포화) 또는 다른 비선형성이 숨어있을 가능성. *진단의 유일한 길은 외부 IV 데이터 또는 mass balance study 추가.*

---

**D. Assumptions & Boundary Conditions**

| 조건 | V/F 분리 가능 여부 |
|---|---|
| Oral 단독 single dose | 불가능 |
| Oral 단독 multiple dose | 여전히 불가능 (정상상태도 V/F·CL/F) |
| Oral + IV (cross-over) | **가능** — F·V·CL 모두 분리 |
| Oral + 안정 동위원소 IV (동시) | 가능 (가장 정확) |
| Oral + 활성대사체 monitoring | 부분적 — F_H 부분 분해 가능 |

**E. Limitations**

- 대분자 약물(monoclonal antibodies 등) IV 투여는 가능하나 IM/SC가 일반적; 절대 F 추정에 IV 비교가 항상 필요.
- Flip-flop 동정 후에도, 어느 쪽이 "진짜 ka"인지 결정은 *생리학적 plausibility*에 의존 (예: controlled-release 제형이면 ka가 작은 게 맞을 가능성).
- 식별불가능성은 *추정*의 문제이지 *예측*의 문제는 아님 — single dose AUC, Cmax는 잘 예측되지만, dose 변경·제형 변경·신기능 변화 영향의 *해석*에서 오류 발생.

**F. Five Cognitive Layers**

| Layer | 의미 |
|---|---|
| L1 | Eq.2:35 구조에서 F·V 결합 + ka·kel 대칭성의 수학적 추적 |
| L2 | 파라미터 공간에서 (V/F, CL/F)는 "하나의 점", (V, F, CL)은 "하나의 선" — 오직 IV 평면이 선을 점으로 만든다 |
| L3 | 광학의 "phase ambiguity"; 신호처리의 "spectral folding"; 경제학의 latent variable identification |
| L4 | 장관 흡수 효율(F)과 분포 용적(V) — 생물학적으로 분리된 두 현상이 데이터에서는 융합 |
| L5 | NONMEM에서 `F1` parameter 사용 시 V·CL 추정값 해석 주의; NDA "Population PK Analysis" section에 IV 비교 데이터 명시 |

**G. Zettelkasten Atom**

```yaml
---
aliases: [V/F identifiability, structural identifiability, flip-flop, apparent volume]
tags: [pharmacometrics/pk/oral, identifiability, regulatory]
up: "[[Oral PK MOC]]"
related: ["[[Master Equation Eq 2-35]]", "[[Bioavailability F]]", "[[NONMEM oral models]]"]
source: "Gabrielsson 5e Ch.2 §2.2.4 p.32, PK2 p.481 Solution III; Rowland & Tozer 5e Ch.6 Case C p.175"
---
```
경구 단독 데이터에서 추정한 V·CL은 모두 V/F·CL/F (apparent values). F·V·CL 분리는 IV 비교 데이터로만 가능. Flip-flop은 ka와 kel swap이 동일 C(t) 산출 — 종말기 기울기로 어느 쪽이 진짜 kel인지 IV로 확인 필요. PK2 Solution III: 초기값 reverse 시 ka·kel·V/F 모두 다른 해로 수렴 — flip-flop 실증. 임상 의의: dose 조정·covariate 해석·BE 평가의 모든 결정이 이 식별불가능성을 인지한 채로 이루어져야 함.

---

<!-- ANCHOR -->
*V/F 식별불가능성은 F와 V의 결합을 다룬다. 그러나 ka 자체에도 또 다른 결합이 숨어있다 — ka가 측정하는 것은 흡수가 아니라 장관 소실 전체다.*

---

### **Card 5. ka,app vs ka,true — ka가 측정하는 것은 무엇인가**

<!-- MASTER LENS -->
**[개념 Big Idea: 거장의 시각]**

**왜 치명적으로 중요한가:** 학생들은 "ka는 흡수속도상수"라고 외우고, ka 증가를 "흡수가 빨라졌다"로 해석한다. *틀렸다*. ka는 *장관에서 약물이 사라지는* 1차 속도상수이며, 그 사라짐의 일부는 혈장으로 흡수되고 일부는 분변으로 배출되거나 장내에서 분해된다. 이 인식이 없으면, ka 변화를 보고 "흡수 개선" 또는 "흡수 저하"라고 단순 해석하는 임상 자문 보고서를 쓰게 된다.

**체화해야 할 단 하나의 직관:** *모델 적합으로 얻은 ka는 "ka,app(겉보기)"이며, ka,app = ka,true + kd*. F와 ka,true가 서로 *얽혀* 있으며, 이 둘의 분리는 mass balance 데이터(분변 회수율) 또는 portal vein 농도 측정 없이는 불가능. ka가 같아도 F가 다를 수 있고, ka가 달라도 F가 같을 수 있다.

**이 직관을 머릿속에 박고 아래를 읽어라:** 이 카드는 ka의 *해부학적·생리학적 의미*를 명확히 한다 — 그리고 왜 GI 분해성 약물의 약리학적 평가가 어려운지 설명한다.

---

**A. Formal Definition**

**ka,true:** 장관에서 혈장으로 *진짜로 흡수되는* 1차 속도상수.
**kd:** 장관 내 화학적 분해 또는 분변 배설로 잃어버리는 1차 속도상수.
**ka,app:** 모델 적합으로 추정되는 ka — 장관에서 약물이 *어떤 경로로든* 사라지는 총 1차 속도상수.

$$k_{a,app} = k_{a,true} + k_d$$

`[출처: G 5e, Ch.2, Fig.2.24 캡션, p.40 — 확인 필요: Fig.2.24 다이어그램으로 표현, 본문에는 별도 번호 수식 없음]`

**B. Derivation / Code Structure**

장관 약물량 A_g 변화의 ODE:

$$\frac{dA_g}{dt} = -k_{a,true} \cdot A_g - k_d \cdot A_g = -(k_{a,true} + k_d) \cdot A_g = -k_{a,app} \cdot A_g$$

혈장 입력률에는 *오직 ka,true가 기여*:

$$\text{Rate}_{input,plasma} = k_{a,true} \cdot D_{po} \cdot e^{-k_{a,app} \cdot t}$$

`[출처: G Eq.2:34 변형, p.30; G Fig.2.25 도식, p.41]`

분변 손실률:

$$\text{Rate}_{loss,fecal} = k_d \cdot D_{po} \cdot e^{-k_{a,app} \cdot t}$$

**F의 분해:**

$$\boxed{F = \frac{k_{a,true}}{k_{a,true} + k_d}}$$

`[출처: G 5e, Ch.2, p.41, Eq.2:70 — 확인 필요: 본문 수식 번호는 2:70이나 도출 맥락은 Fig.2.24/2.25 캡션 의존]`

이 수식이 **결정적으로 중요**: ka,app 단독으로는 ka,true도 kd도 알 수 없다. F를 추가로 알아야 ka,true를 분리 가능 — *그런데 F는 IV 비교가 필요하다 (Card 3)*. 따라서 ka,true는 IV 비교 + 분변 회수 둘 다 필요.

**다중 흡수 부위 (Multiple absorption sites — CONTEXT, Eq.2:80–2:82):**
sublingual 제형처럼 협부(buccal)와 장(GI tract)에서 동시에 흡수되는 경우, 두 ka (ka,rapid, ka,delayed)와 fraction Frct로 분해된 다중 peak 모델 — ka가 *물리적으로 다른 경로*에서 다른 값을 가질 수 있음을 보여준다. `[출처: G p.46, Eq.2:80–2:82]`

**C. Structural Necessity**

ka가 *총 장관 소실*을 측정하는 이유: 1차 ODE의 본질. dA_g/dt에 들어가는 모든 1차 손실 항은 합쳐서 하나의 effective rate constant가 된다. 이 합산은 수학적 필연이며 데이터로 분해 불가능 — 같은 dA_g/dt 시간 추이를 만드는 (ka,true, kd) 조합은 무한히 많다.

F = ka,true/(ka,true + kd) 형태가 자연스러운 이유: F는 *경쟁하는 두 1차 과정의 분율 결과*. 흡수와 분해가 *같은 약물 풀(pool)*에서 *동시에* 작용하므로, 흡수가 이긴 비율이 F.

**D. Assumptions & Boundary Conditions**

- 장관 내 분해와 흡수가 모두 1차 (포화되지 않음)
- 장관에서 혈장으로의 흐름이 단방향 (exsorption 무시)
- 흡수 부위가 단일 (다중 흡수 부위 시 별도 모델 — Eq.2:80–2:82)
- 위반 사례: P-gp 외향 운반체 → exsorption 발생, ka 더 작아짐; pH 의존 분해 → kd가 시간/위치 의존적

**E. Limitations**

- ka,true와 kd 분리에는 *3중 데이터*가 필요 — plasma + IV (F 추정) + 분변 회수 (분해 분율 측정).
- 활성대사체가 분해 산물이면 약리학적 평가 더욱 복잡.
- Permeability(투과도) 자체도 ka,true 안에 포함된 더 미세한 인자 — Caco-2, PAMPA in vitro 시험은 이 미세 인자의 *상대적* 비교만 제공.

**F. Five Cognitive Layers**

| Layer | 의미 |
|---|---|
| L1 | ka,app = ka,true + kd; F = ka,true/(ka,true+kd) (Eq.2:70) |
| L2 | 장관 약물 풀에서 두 흐름(흡수·분해)의 경쟁 |
| L3 | 화학반응 평행 1차 동역학 (parallel first-order); 인구학의 출생률·이주율 |
| L4 | 장벽 효소·미생물·pH·permeability·P-gp 모두가 ka 안에 잠재 |
| L5 | BCS Class II/IV 약물 (저용해성)의 in vivo ka는 *제형 의존적* — formulation은 ka,true와 kd를 동시에 변화 |

**G. Zettelkasten Atom**

```yaml
---
aliases: [ka apparent, ka true, kd intestinal degradation, gut wall metabolism]
tags: [pharmacometrics/pk/oral, mechanism]
up: "[[Bioavailability F]]"
related: ["[[Master Equation Eq 2-35]]", "[[V over F identifiability]]", "[[BCS]]"]
source: "Gabrielsson 5e Ch.2 p.40-41 Fig.2.24, Eq.2:70 (캡션 다이어그램)"
---
```
모델 적합 ka는 ka,app이며 ka,true(흡수) + kd(분해)의 합. F = ka,true/(ka,true+kd). ka,app만으로 분리 불가 — IV + 분변 회수 데이터 필요. 다중 흡수 부위(sublingual)에서는 ka가 *물리적으로 다른* 두 값. ka 변화 해석 시 "흡수 개선/저하"가 아니라 "장관 약물 잔존 시간 변화"가 정확.

---

<!-- ANCHOR -->
*다섯 카드를 거치며 우리는 경구 PK의 모든 파라미터가 *얽혀* 있음을 보았다 — F·V·ka 모두 IV 비교 없이는 진짜 값이 아니다. 이제 가장 빈번한 혼동 쌍들을 명시적으로 해부한다.*

---

## §5. CONFUSION PAIR DISSECTION

이 세션에서 4개의 혼동 쌍을 식별한다. 가장 임상·규제 파급력이 큰 **혼동쌍 1 (ka vs kel under flip-flop)**에 **Critical Blow** 적용.

---

<!-- CONFUSION -->
### **혼동쌍 1: ka vs kel — Flip-flop 상황** ⚠️ Critical Blow 적용

| 비교 차원 | ka (흡수속도상수) | kel (소실속도상수) |
|---|---|---|
| **표면적 유사성** | 둘 다 1차 속도상수, 단위 동일 (시간⁻¹), Master Equation에서 대칭 위치 출현. *식별 정보가 식 자체에 없음.* | (좌측 셀과 동일 — 둘이 swap되어도 곡선 동일) |
| **수식/코드 형태** | 흡수 부위에서의 약물 사라짐: dA_g/dt = −ka·A_g | 혈장에서의 약물 사라짐: dA/dt = ka·A_g·F − kel·A |
| **생리학적 지시체** | 장관 mucosa 통과 + 위장관 운반체 + 분해 (포괄) | 간 추출 + 신 배설 + 기타 청소 경로 |
| **변화 방향 (제형 변경 시)** | controlled-release → ka 감소 | 본질적으로 약물의 청소 경로 변화 없음 → kel 불변 |
| **변화 방향 (간기능 저하 시)** | 일반적으로 변동 적음 | CL_H 감소 → kel 감소 |
| **임상/모델링 결과** | ka 오인 (실제로 kel) → "이 약은 빨리 흡수된다"고 잘못 보고 → 임상 onset 예측 오류 | kel 오인 (실제로 ka) → "이 약 t½ = 4h"라 보고 → Q12h dosing 결정 시 *실제 t½ = 12h*면 누적 toxicity |
| **⚡ 기억 고리** | **"두 지수가 자리를 바꾸어도 카메라는 같은 사진을 찍는다 — 단, IV bolus만이 그 카메라 앞에 명찰을 붙여준다." Master Equation의 (ka−kel) 차이지수는 부호 swap에 대해 *대칭*이며, 외부 라벨(IV terminal slope)만이 그 대칭을 깨뜨린다.** | (좌측과 동일 기억 고리) |
| **🩸 치명적 타격 (Critical Blow)** | **이 혼동을 품고 NDA를 제출하면**: "Flip-flop has not been ruled out; please provide IV pharmacokinetic data or justify the assumption that the terminal phase reflects elimination." 이는 FDA Deficiency Letter의 표준 문장이다. 임상 시나리오로는: 장기 작용 SC 제형(예: depot injection)을 oral 데이터의 "kel = 0.05 hr⁻¹"로 추정해 Q24h dosing 결정 → 실제 ka가 율속이라 약물이 *주기 사이에 누적*되어 독성 농도 도달. (T Fig.6-7 fluticasone propionate 사례가 이 위험의 documented 근거.) | |

---

<!-- CONFUSION -->
### **혼동쌍 2: F (extent) vs ka (rate)**

| 비교 차원 | F (생체이용률) | ka (흡수속도상수) |
|---|---|---|
| **표면적 유사성** | 둘 다 "흡수"를 측정하는 것처럼 보임. 학생들은 종종 "F = 0.5"를 "흡수 절반 속도"로 잘못 읽음. | (대조) |
| **수식/코드 형태** | 단위 없음 (분율). AUC 비율로 정의 | 시간⁻¹ 단위. 곡선 형태(time-shape)로 정의 |
| **차원성** | 시간 적분 후 *살아남는* 양 | 시간 미분의 *형태* |
| **변화 방향 (제형 변경)** | 위장관 분해 감소 → F 증가 | 입자 크기 감소 → ka 증가 (extent 무관) |
| **변화 방향 (식사 영향)** | 간 1차 통과 변화 → F 변화 가능 | 위배출 지연 → ka *겉보기* 감소 |
| **임상/모델링 결과** | F 변화는 AUC를 변화시킴 → 효능 강도 변화 | ka 변화는 tmax·Cmax를 변화시킴 → 효능 onset/peak 변화 |
| **⚡ 기억 고리** | **"AUC는 양이고, tmax는 형태다 — 양이 변하면 효능이 변하고, 형태만 변하면 onset이 변한다." F가 0.5로 떨어진 약물은 *2배 dose*로 보상 가능. ka가 절반이 된 약물은 *그저 천천히 작용*할 뿐 — 다른 dose로 보상되지 않는다.** | |

---

<!-- CONFUSION -->
### **혼동쌍 3: V/F vs V (apparent vs true volume)**

| 비교 차원 | V/F (겉보기 분포용적) | V (진짜 분포용적) |
|---|---|---|
| **표면적 유사성** | 같은 단위(L), 같은 모델 출력값 위치, 임상의·연구자 모두 "분포 용적"이라 부름 | (대조) |
| **수식/코드 형태** | 경구 데이터 적합 결과 — 항상 V/F | IV 데이터 또는 IV+oral 동시 적합 결과 |
| **생리학적 지시체** | "F가 1이라 가정한 가상의 분포용적" — F<1이면 실제 V를 *과대*추정 | 실제 약물이 분포한 조직 부피의 약리학적 추정치 |
| **변화 방향 (covariate analysis)** | 신부전 환자에서 V/F 30% 증가 — V 변화? F 변화? **분해 불가** | covariate effect가 *진짜 V*에만 작용한다고 단언 가능 (mechanism 파악 시) |
| **임상/모델링 결과** | 부하 용량 계산 시 V/F를 V로 오해 → 잘못된 dose 조정 | 정확한 부하 용량 계산 |
| **⚡ 기억 고리** | **"슬래시(/) 뒤의 F는 보이지 않는 동반자 — 모든 oral PK 출력에 1/F가 곱해진 채 따라다닌다. IV bolus가 도착할 때까지 그 동반자의 정체는 영원히 미스터리." 따라서 oral 단독 결과를 *반드시* "V/F = ..." 또는 "apparent V = ..."로 명기하라.** | |

---

<!-- CONFUSION -->
### **혼동쌍 4: First-order Ka vs Zero-order Rin (입력 함수 모델)**

| 비교 차원 | First-order Ka | Zero-order Rin |
|---|---|---|
| **표면적 유사성** | 둘 다 "흡수 모델", 둘 다 1구획에 입력 | (대조) |
| **수식/코드 형태** | rate = ka · A_g (시간 의존, 지수 감쇠) | rate = R_in (constant during T_abs) |
| **데이터 시그니처** | 반대수 plot에서 흡수 phase가 *직선* (after MoR 처리) | 반대수 plot에서 흡수 phase가 *비선형 convex* |
| **physiological 의미** | 수동 확산 흡수 (대부분의 약물) | 운반체 매개 포화 흡수 또는 controlled-release; transdermal patch |
| **PK3 사례 데이터 시그니처** | CV% 3400% (ka·kel 비분해), AIC = 85.2, residuals 패턴 비무작위 | CV% 5–14% (안정), AIC = 76.2, residuals 무작위 |
| **변화 방향 (dose 증가 시)** | AUC dose 비례 (선형) | AUC < dose 비례 (포화) → flat plateau |
| **임상/모델링 결과** | 표준 ADVAN2 사용 가능 | $DES 또는 ADVAN6/8 사용자 정의 필요; T_abs estimate |
| **⚡ 기억 고리** | **"1차 흡수는 '빠질수록 천천히 빠지는 양동이', 0차 흡수는 '일정 속도로 채우는 IV 펌프 + 갑자기 꺼지는 스위치'." 0차는 흡수 *지속 시간*이라는 추가 parameter T_abs를 가지며, 흡수 종료 후 곡선이 단순 1구획 IV 종료 후 와시아웃이 된다 — 이것이 PK3의 결정적 데이터 시그니처.** | |

---

<!-- RECAP -->
*§5 요약: 네 혼동 쌍은 모두 "겉보기 동등성 vs 구조적 차이"의 변주다 — ka↔kel(flip-flop), F↔ka(rate↔extent), V/F↔V(apparent↔true), 1차↔0차(input function 형태). 모든 혼동의 해소는 (a) 추가 데이터 (IV, mass balance) 또는 (b) 모델 비교 (AIC, GOF, residual pattern)을 요구한다.*

---

## §7. SELF-TEST: ACTIVE RECALL MODULE

총 8문제. 회상 3문제(38%) / 적용 5문제(62%). 마지막 문제는 보스 딜레마(Socratic Dilemma).

---

<!-- SELF-TEST -->
### **Q1 [회상, ★★]**

C(t) Master Equation (Eq.2:35)을 lag-time 포함 형태(Eq.2:39)로 재현하라. 각 항(분자·분모·대괄호)이 의미하는 바를 한 문장씩 설명하라.

<details><summary>📖 정답 공개</summary>

$$C(t) = \frac{k_a \cdot F \cdot D_{po}}{V \cdot (k_a - k_{el})} \cdot \left[ e^{-k_{el}(t-t_{lag})} - e^{-k_a(t-t_{lag})} \right]$$

- **분자 ka·F·D_po**: 흡수 부위에서 혈장으로의 *순간* 입력 강도
- **분모 V·(ka−kel)**: 분포용적과 두 지수의 시간 분리도 곱
- **대괄호**: 흡수와 소실 두 1차 과정의 차이 함수

t < tlag일 때 C = 0.

**다음 깊이 질문:** 이 식에서 ka = kel일 때 분모가 0이 된다. 한계 사례에서 식은 어떻게 되며, 어떤 약물에서 관측되는가?

</details>

---

<!-- SELF-TEST -->
### **Q2 [회상, ★]**

tmax 공식을 dC/dt = 0 조건에서 도출하라 (Eq.2:52). 이 공식이 *F와 V에 무관*함을 확인하고, 그 이유를 설명하라.

<details><summary>📖 정답 공개</summary>

dC/dt = 0 → ka·e^(−ka·tmax) = kel·e^(−kel·tmax) → 양변 자연로그 → tmax = ln(ka/kel)/(ka−kel).

**F·V 무관 이유:** dC/dt에서 ka·F·D_po/[V·(ka−kel)] 인자는 0 조건과 무관하게 인수분해되어 약분됨. 따라서 *peak의 *시점*은 두 속도상수만의 함수, peak의 *크기*는 F·D_po/V에 비례.

**다음 깊이 질문:** 이 사실은 "두 약물이 같은 ka·kel를 가지면 dose에 무관하게 tmax가 동일"하다는 결과를 함의한다. BE 평가에서 tmax 비교가 어려운 이유와 어떻게 연결되는가?

</details>

---

<!-- SELF-TEST -->
### **Q3 [회상, ★★]**

F (절대 생체이용률)와 F_rel (상대 생체이용률)의 정의 식을 각각 쓰라. 후자가 BE 시험에서 핵심적으로 사용되는 이유는?

<details><summary>📖 정답 공개</summary>

F = (AUC_po · D_iv) / (AUC_iv · D_po) — 절대 F, IV 비교 필요.

F_rel = F_B/F_A = (AUC_B · D_A) / (AUC_A · D_B) — 두 경구 제형 비교, IV 불필요.

**BE 시험 사용 이유:** BE는 *innovator product와 generic product의 동등성*을 평가하는 것이지 절대 흡수율을 묻는 것이 아님. 두 oral 제형의 AUC·Cmax 비율의 90% CI가 0.80–1.25에 들어가면 BE 선언 (T pp.182–183).

**다음 깊이 질문:** F_rel = 1.0 (완전 동등)이라도, 두 제형이 *다른 ka·tmax*를 가질 수 있다 — 이것이 BE에서 Cmax도 평가하는 이유. 그러나 tmax는 90% CI 평가 대상이 아닌 이유는?

</details>

---

<!-- SELF-TEST -->
### **Q4 [적용, ★★]**

PK2 데이터에서 V/F = 32 L, 같은 환자 IV deconvolution F = 0.82가 얻어졌다. 다음을 계산하고 해석하라:
(a) 진짜 V는?
(b) 만약 후속 실험에서 신부전 환자의 V/F = 48 L로 측정되었다 (F는 미측정). 이 결과를 어떻게 보고하겠는가?

<details><summary>📖 정답 공개</summary>

(a) V = V/F · F = 32 × 0.82 ≈ 26 L. *(원문은 V = 20 L로 기재되어 있으나 계산상 26 L. 본문 Solution II 결과와 deconvolution 결과의 산출 경로 차이로 추정 — `[확인 필요]` 플래그.)*

(b) **잘못된 보고:** "신부전 환자의 V가 50% 증가했다." → V/F를 V로 오인.
**올바른 보고:** "신부전 환자의 V/F가 32 → 48 L (50% 증가)로 관측되었다. 이 변화의 원인이 V 자체의 증가인지 F의 감소인지는 본 데이터로 분리 불가능하다. 분해를 위해서는 IV 비교 데이터 또는 mass balance study가 필요하다."

**다음 깊이 질문:** 만약 F가 0.82 → 0.55로 감소했다고 가정하면, 진짜 V는 몇 L인가? V가 *변하지 않았다*고 가정할 수 있는가?

</details>

---

<!-- SELF-TEST -->
### **Q5 [적용, ★★]**

Phase 1 oral 데이터 (single dose)로 적합한 NONMEM 1구획 ADVAN2 모델에서 다음이 얻어졌다:
- ka = 0.05 hr⁻¹
- kel = 0.5 hr⁻¹
- V/F = 100 L

종말기 t½는 1.4시간으로 보고되었다. 이 모델에 대해 다음을 평가하라:
(a) 종말기 t½의 해석은 적절한가?
(b) 후속 IV 시험을 추천하는 근거를 작성하라.

<details><summary>📖 정답 공개</summary>

(a) **부적절.** ka = 0.05 < kel = 0.5는 *flip-flop 시그니처*이다. 종말기 곡선의 기울기는 *kel*이 아니라 *ka*를 반영할 가능성이 매우 높다. 보고된 "종말기 t½ = 1.4 hr"는 사실 *흡수 t½*일 가능성. 진짜 소실 t½는 ln(2)/0.5 = 1.4 hr이지만, *어느 값이 진짜인지 oral 데이터만으로는 알 수 없다*.

(b) IV bolus 시험 권장 근거:
1. ka < kel 추정 결과는 flip-flop 가능성 시사 (G p.30, Fig.2.17; T Ch.6 Case C).
2. 종말기 기울기가 흡수를 반영하는지 소실을 반영하는지를 IV 종말기와 *평행/비평행*으로 직접 검증 필요.
3. 검증 없이 진행 시: dose interval 결정에 결정적 오류 — 흡수 t½ 1.4h를 소실 t½로 오인하면 Q6h dosing 결정 → 실제 소실 t½가 1.4h가 아닌 더 긴 값(예: depot effect)이라면 누적 toxicity 위험.

**다음 깊이 질문:** IV 시험에서 종말기 기울기가 oral 종말기와 평행하다고 *확인된* 후에도, V·F·CL 분리 추정을 위해 어떤 추가 데이터가 필요한가?

</details>

---

<!-- SELF-TEST -->
### **Q6 [적용, ★]**

PK3 사례에서 1차 흡수 모델의 CV%가 3400%로 폭발했다. 0차 흡수 모델은 CV% 5–14%로 안정. 모델 선택의 근거 4가지를 제시하라.

<details><summary>📖 정답 공개</summary>

PK3 (G p.486, Table 3.1) 모델 선택 근거:

1. **Parameter precision (CV%):** 1차 모델 ka·kel·V/F 모두 CV% 3400% (사실상 비추정), 0차 T_abs CV% 5%, kel CV% 14%, V/F CV% 11%.
2. **AIC 차이:** 1차 모델 AIC = 85.2, 0차 모델 AIC = 76.2 (Δ ≈ 9, 결정적 우위).
3. **Residual 패턴:** 1차 모델은 systematic deviation, 0차 모델은 random scatter.
4. **Mean standard deviation (√(WRSS/df)):** 0차 모델에서 더 낮음 — fit 자체의 quality.

**Reparameterization tip:** 0차 모델에서도 V/F vs kel 상관(-0.94)이 있으나, kel을 CL/F로 reparameterize하면 상관 감소 — *CL/F는 전체 곡선 정보로 결정되기 때문*.

**다음 깊이 질문:** 0차 모델이 더 잘 적합되는 사실이 *물리적으로 0차 흡수가 일어나고 있다*는 증명인가? 아니면 다른 가능성은?

</details>

---

<!-- SELF-TEST -->
### **Q7 [적용, ★]**

ka,app = 0.8 hr⁻¹로 추정된 약물에서, 분변 회수 시험으로 12%가 분변에서 확인되었다. F = 0.7이라 가정하면, ka,true와 kd는 각각 얼마인가?

<details><summary>📖 정답 공개</summary>

F = ka,true / (ka,true + kd) = ka,true / ka,app

→ ka,true = F · ka,app = 0.7 × 0.8 = **0.56 hr⁻¹**

→ kd = ka,app − ka,true = 0.8 − 0.56 = **0.24 hr⁻¹**

**검증:** ka,true / (ka,true + kd) = 0.56 / 0.80 = 0.70 ✓

분변 회수 12%는 ka,true의 결과로 흡수된 약물이 *전신 청소 후* 분변으로 배설된 것일 수도 있고, kd로 직접 분해되어 분변으로 나간 것일 수도 있다 — *이 둘을 분해하려면 동위원소 표지 또는 기질-대사체 정량이 추가로 필요*.

**다음 깊이 질문:** 같은 약물의 후속 시험에서 식사와 함께 투여 시 ka,app = 0.6 hr⁻¹, F = 0.85로 변화. 이 결과는 ka,true와 kd 중 어느 것이 변화한 것을 의미하는가?

</details>

---

<!-- SELF-TEST -->
### **Q8 [⚡ 보스 딜레마, ★★] — Socratic Dilemma**

**시나리오:**

당신은 신약 후보 X (oral controlled-release tablet)의 Phase 2a 시작 직전 PopPK 모델 작성 책임자다. Phase 1 결과:

- Single dose oral PK (n = 24): C(t) 1구획 1차 흡수 lag-time 모델로 양호한 적합. ka = 0.18 hr⁻¹, kel = 0.69 hr⁻¹, V/F = 280 L, F는 측정되지 않음 (IV 제형 미개발).
- 종말기 t½ ≈ 1.0 hr.

**Phase 2a 프로토콜 위원회가 두 옵션을 제시:**

**옵션 A — Q12h dosing 채택 (모델 그대로 사용):**
- 종말기 t½가 1시간이므로 Q12h은 4 t½만에 농도 정점 도달 후 회복 — 안전.
- 모델은 적합, 통계적 유의성 확보.
- 후속 IV 시험은 Phase 2b 또는 Phase 3에서 진행.

**옵션 B — Q24h dosing + IV PK substudy 동시 진행:**
- ka < kel 신호로 *flip-flop 가능성 무시할 수 없음* — 만약 진짜 ka가 0.69, 진짜 kel이 0.18이라면 진짜 t½ = 3.85 hr → Q12h 누적 위험.
- IV substudy는 4주 지연·예산 추가.
- 그러나 prospective 식별 가능.

**당신의 결정과 그 결정을 NDA Population PK Analysis section에서 어떻게 방어할 것인가?**

<details><summary>📖 정답 공개 — 수석 모델러의 Trade-off 논리</summary>

**단순한 정답은 없다 — 두 결정 모두 방어 가능하나, 방어의 질이 결정의 질을 만든다.**

---

**옵션 A 방어 시 (Q12h, IV 지연):**

규제 문서 작성:
> "We acknowledge that flip-flop cannot be definitively ruled out from oral-only data. However, the controlled-release formulation rationale supports a true ka < kel scenario only if the formulation release rate is the rate-limiting step, which is *consistent with the observed terminal slope of 0.18 hr⁻¹*. Conservative dosing rationale: if flip-flop is operative, the true t½ would be ln(2)/0.69 = 1.0 hr (still short), and Q12h would result in negligible accumulation. Therefore, the dosing decision is *robust to flip-flop ambiguity*. IV PK substudy is planned for Phase 2b to formally resolve identifiability."

이 방어의 핵심: *flip-flop 시나리오에서도 안전성 결론이 변하지 않음*을 보임. Trade-off는 "Phase 2 dose decision의 통계적 power" vs "identifiability 검증의 방법론적 청결성".

---

**옵션 B 방어 시 (Q24h, IV 즉시):**

규제 문서 작성:
> "Per ICH M9 and FDA Population PK Guidance (2022), structural identifiability of disposition parameters in extravascular models requires at minimum cross-over IV comparison or stable isotope tracer data. Given the observed ka·kel ratio (0.26) suggests flip-flop possibility, prospective resolution of identifiability prior to dose-ranging is methodologically sound and reduces downstream risk of dose-decision reversal in Phase 3."

이 방어의 핵심: *방법론적 청결성 우선*. Trade-off는 "4주 지연 + 예산" vs "Phase 3 단계의 dose 변경 위험".

---

**수석 모델러의 진짜 통찰:**

1. **두 결정 모두 *명시적 trade-off 인식*이 핵심.** 어느 쪽이든, "flip-flop 가능성을 모르고 진행했다"는 인상을 주면 deficiency letter는 보장된다.

2. **B가 더 보수적이지만 *항상* 옳지는 않다.** Phase 2a 빠른 PoC가 mission-critical이고, 안전 여유가 충분하면 A가 합리적.

3. **"IV 시험을 *언제* 할 것인가"는 결정의 본질이 아니라 *언제 할지를 명시적으로 commit하는가*가 본질.** Phase 2b로 미루는 결정이라도, protocol에 timeline을 박아두면 방어 가능.

4. **NDA에서 *불확실성을 인정한 결정*은 *불확실성을 모르는 결정*보다 항상 강하다.** 심사관은 모델러가 식별불가능성을 인지하고 있는지를 본다 — 정답을 내는 것이 아니라.

5. **이 딜레마의 메타 교훈:** PK는 데이터 분석이 아니라 *불확실성 관리* — 모든 결정은 어떤 가정이 깨졌을 때의 위험을 prospective하게 quantify하는 작업이다.

</details>

---

## §8. META-FRAME & BIG PICTURE

### A. Positioning (28-세션 PK/PD 아키텍처에서의 위치)

**이전에 온 것 (선행):**
- IV bolus 1구획 PK (CL, V, t½, AUC)
- 1차 ODE의 적분, 자연로그·지수 함수 미적분
- AUC 사다리꼴법 (NCA 기초)
- Fundamental concepts: bioavailability 정의, 청소율의 의미

**바로 다음 (직후 세션):**
- Multiple dosing & accumulation: 누적 인자 R = 1/(1−e^(−kel·τ)) (Eq.2:78), Css 추정 — *경구 단일 dose의 모든 파라미터를 multiple dose로 확장*
- Multi-compartment oral models (2-compartment with absorption): peak 곡선의 추가 inflection — Master Equation의 다지수 확장
- PopPK 흡수 서브모델: transit compartment, Erlang, Weibull — 1차 흡수 가정의 일반화
- Bioequivalence formal evaluation: 90% CI 0.80–1.25, FDA guidance

**결정적으로 의존하는 고급 도메인:**
- **PopPK NONMEM 흡수 모델링** — ADVAN2/ADVAN4 vs 사용자 정의 transit compartment 결정은 본 세션의 1차/지연/0차 판별 직관 위에 구축
- **TDM (therapeutic drug monitoring)**: oral clearance(CL/F)로 dose 조정 시, F의 변동성(식사·약물상호작용)이 직접적으로 dose 결정에 들어감
- **TMDD with oral input**: 표적 매개 소실의 비선형성 + oral 흡수의 결합은 본 세션의 1구획 선형 가정을 모두 깨뜨림 — 그러나 시작점은 본 모델
- **Modified-release 제형 평가**: GSS, gastroretentive systems, BCS Class II/IV 약물 — 본 세션의 ka 해석 + dissolution rate-limiting 직관 위에 구축
- **NDA / IND submission Population PK section**: V/F 식별불가능성 인지 + flip-flop 검증은 모든 oral 약물 NDA의 표준 요구사항

**BCS·생리학 맥락 (1문장):** 본 세션의 ka 변동성은 BCS 분류(Class I 고용해·고투과 vs Class IV 저용해·저투과), 위배출·장 통과 시간(T Ch.7), 운반체(P-gp) 상호작용 등의 생리학적 인자가 만드는 것이며, 이 인자들이 *F의 식사 효과·약물상호작용*의 메커니즘이다.

---

### B. Dependencies — 본 세션 미체화 시 고급 모델링에서의 실패 모드

**실패 모드 1 — PopPK V/F 해석 오류 → 부하용량 잘못 결정:**
경구 PopPK 모델에서 V/F를 V로 오인. 신부전 환자에서 V/F가 30% 증가한 covariate effect를 "분포용적 30% 증가"로 해석하여 부하 용량 30% 증액. 그러나 실제 변화가 F의 감소(예: 신부전으로 인한 장관 vascular 변화에 따른 absorption 감소)였다면, 진짜 V는 불변이고 부하 용량은 *그대로*가 옳다. 결과: 첫 dose에서 *과량 투여*. 추적 가능한 인과관계: covariate analysis의 mechanism을 분리할 데이터가 없는 채로 dose 조정 → toxicity.

**실패 모드 2 — Flip-flop 미인식 → dose interval 잘못 결정:**
Long t½로 보이는 약물(실제로는 흡수 율속) → Q24h dosing 채택. 그러나 흡수가 율속이면 *진짜 소실은 빠른* 것이며 dose 사이에 약물이 거의 모두 빠져나간다 → 약물 농도가 *MIC 아래로* 떨어지는 시간 발생 → 약효 부전. 또는 반대로, depot 효과로 누적된 약물이 multiple dose 시 점진적 toxicity 도달. 추적 가능한 인과관계: PK2 Solution III 사례처럼 ka·kel·V/F가 모두 *6배 변동*하는 dual solution을 인지하지 못한 채 single dose 모델을 multiple dose 시뮬레이션에 사용 → steady-state 예측 오류.

**실패 모드 3 — ka 변화 해석 오류 → 임상 자문 보고서 오류:**
식사와 함께 투여 시 ka,app 50% 감소를 "흡수 50% 저하"로 보고. 그러나 이것이 ka,true 감소(흡수 메커니즘 영향)인지 kd 감소(장 분해 감소로 *오히려 이득*)인지 분리되지 않음. F가 동시에 측정되지 않으면 정확한 해석 불가. 임상의는 "식후 투여 금기" 결정 → 사실은 식후 투여가 *F를 증가*시켜 효능을 개선하는 경우일 수도 있음 (예: griseofulvin, T pp.197–220 BCS class II 약물).

---

### C. Professional Moat — 30년 차 모델러만이 갖는 것

> *"NONMEM을 실행하고 GOF 플롯을 생성할 수 있는 주니어 모델러와, 1구획 1차 흡수 모델을 데이터에 적합시킬 수 있는 AI가 이미 존재한다. 본 세션의 원리를 — 메커니즘이 아닌 구조적 이해의 수준에서 — 진정으로 내면화한 연구자는 그 둘 중 어느 것도 복제할 수 없는 무엇을 갖고 있는가?"*

**답 (구조적 필연성 수준):**

본 세션에서 진정한 Professional Moat는 **세 종류의 식별불가능성을 *동시에* 추적하는 능력**이다:

1. **구조적 식별불가능성 (V/F):** 모델 식 자체에 결합된 채로만 등장하는 파라미터 — 데이터 quality·quantity로 해결 불가, *모델 재구성 또는 외부 데이터 추가*가 유일한 길.

2. **수치적 식별불가능성 (Flip-flop):** 동일한 데이터에 두 해(solution)가 동등하게 적합 — 알고리즘이 어느 해로 수렴할지는 *초기 추정값 의존*. PK2 Solution III에서 ka·kel을 reverse 시 *6배 다른* V/F로 수렴한 사례.

3. **기계론적 식별불가능성 (ka,app vs ka,true):** 한 파라미터가 여러 생리학적 과정의 합 — *plasma 데이터의 본질적 한계*. mass balance·동위원소·portal cannulation 외엔 분해 불가.

세 식별불가능성을 *동시에 머릿속에 들고* 모델 출력을 보는 연구자는:

- *"V/F를 V로 보고하는 부하 용량 계산"*에서 자동으로 멈춘다.
- *"종말기 t½ = elimination t½"라는 default 가정*을 ka·kel 비율로 즉시 검증한다.
- *"ka 변화 = 흡수 변화"라는 단순 해석*을 ka,app 분해 가능성으로 즉시 의심한다.

이것이 NONMEM 출력값의 *어떤 숫자도 단독으로 믿지 않는* 모델러의 직관이다. AI는 출력값을 *생성*할 수 있지만, 어느 출력값이 *겉보기 값인지*를 모델 식의 구조에서 즉각 읽어내는 능력은 — 본 세션과 같은 식별불가능성의 *수학적 계보를 추적해본* 연구자만의 자산이다.

> **한 줄 요약:** 본 세션을 체화한 모델러는 *어떤 oral PK 출력값도 IV 비교 데이터의 맥락 없이는 단언하지 않으며, 식별불가능성을 prospective하게 design한다*. 이것이 NDA Population PK Analysis section의 *모든 문장이 식별 가능한 파라미터에 기반함*을 보장하는 직업적 기준선이다.

---

```
✦ STEP 1 DRAFT v0 완료.

산출물 구성:
  • Curation Map: MUST 5개, CONTEXT 7개 (본문 흡수)
  • §1 세션 헤더 & 로드맵 (Big Idea + 개념 항법도 + 지식 그래프 위치 + 기호 통일 방침)
  • §2 개념 해부 카드 5개 (Apex: Card 4 — V/F 식별불가능성 + Flip-flop)
  • §5 혼동 쌍 해부 4쌍 (Critical Blow 적용: Pair 1 — ka vs kel under flip-flop)
  • §7 자기 테스트 8문항 (회상 3 / 적용 5, 마지막 보스 딜레마)
  • §8 메타프레임 (positioning + 실패모드 3 + Professional Moat)
  • 감지된 소스 유형: 혼합 (Vol I — Gabrielsson 데이터/수식 도출 + Rowland & Tozer 임상/생리)
  • Data Anchoring 소스: G PK2 (100 µg drug A, 단일 환자) + PK3 (20 mg highly polar drug, 1 volunteer); 가상 수치 사용 없음 — 모든 임상 시나리오는 책에 명시된 실제 사례 기반
  • [확인 필요] 플래그 2건:
      (a) Eq.2:70 — 본문 수식 번호는 2:70이나 도출 맥락은 Fig.2.24 캡션 다이어그램 의존
      (b) PK2 V = 20 L 본문 명시 vs V/F · F = 32 × 0.82 ≈ 26 L 계산 결과 불일치 (Q4 정답 노트)
  • 마커 적용: <!-- MASTER LENS --> 5건, <!-- ANCHOR --> 5건, <!-- TRENCH --> 1건,
              <!-- CONFUSION --> 4건, <!-- SELF-TEST --> 8건, <!-- RECAP --> 1건
  • Phase 4C 대상: FIGURE 마커는 본 단계에서 의도적으로 미삽입 (워크플로우 v3.3.2 준수)

다음 단계: Phase 2 (Source Fidelity Audit, Gemini Pro) 진행 권장.
첨부 파일: 원본 PDF 2종 (G + T) + 본 Step 1 Draft v0
```

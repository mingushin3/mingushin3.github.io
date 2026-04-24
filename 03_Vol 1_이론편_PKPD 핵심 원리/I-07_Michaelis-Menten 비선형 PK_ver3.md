아래는 확정 내용에 주석·부연설명을 추가한 최종 Step 1입니다. 💡 표시가 추가된 부분입니다 — 총 10곳, 각 2–4문장 이내.

---

# §1 — 세션 헤더 & 로드맵

**소스 정보**

| 소스 | 챕터/섹션 | 제목 | 페이지 범위 |
|---|---|---|---|
| Gabrielsson & Weiner 5e | §2.7.1–2.7.5, PK17 pp.553–555, PK21 pp.123–128 | Nonlinear Systems – Capacity, Time, Flow and Binding | pp.112–134 |
| Rowland & Tozer 5e | Ch.16 | Nonlinearities | pp.491–529 |

**Big Idea (한 문장)**

비선형 PK란 "용량을 올리면 농도가 폭발하는 현상"이 아니라, 동일한 투여 경로·제형·방법에서 dose-normalized 농도·AUC·소변 회수율·$f_u$·$V$·$CL_R$·$F$ 중 하나 이상이 superposition하지 않는 구조적 실패이며, 수석 모델러의 임무는 그 붕괴가 Capacity·Time·Flow·Binding·흡수·신배설·표적결합 중 어느 계층에서 비롯되었는지 역추론하고 — NONMEM 파이프라인에서 어떤 ODE 구조로 번역하는지 — 판단하는 것이다.

**개념 항법도**

1. **진단학으로서의 비선형 PK** — superposition 붕괴, 4단계 인식 워크플로우, R&T Table 16-1
2. **Capacity-limited elimination — Michaelis-Menten 소실 동역학** [⚡ Apex]
3. **입력 속도 Catastrophe — Phenytoin & Alcohol plateau**
4. **혼합 병렬 경로 (MM + 1차)** — salicylic acid
5. **비선형 흡수 & 포화 초회통과**
6. **신배설 비선형성**
7. **단백·조직결합 비선형성 & TMDD 브리지**
8. **시간 의존성 동역학**

**지식 그래프 위치**

- **선행**: I-01, I-03, I-05
- **다음**: I-08 (TMDD), I-09 (Emax), I-10 (Indirect Response), II-04 (General ADVAN/$DES)
- **의존 도메인**: PopPK ($\eta$ 위치 선택), PBPK (간 효소 포화), TMDD, QSP

---

# §2 — 개념 해부 카드

---

## 카드 1. 진단학으로서의 비선형 PK — 거장이 먼저 보는 좌표계

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가**: 비선형 PK를 "대사 포화"로만 반사적으로 연결하는 순간, 포화 흡수로 인한 $F$ 감소(amoxicillin), 포화 초회통과로 인한 $F$ 증가(nicardipine), 단백결합 포화로 인한 총농도 plateau(naproxen), 조직 표적결합에 의한 $V_{ss}$ 감소(bosentan)를 모두 "대사 증가"로 오진하게 된다 — Phase 1 용량 설계가 통째로 틀어진다.

**체화해야 할 단 하나의 직관**: 비선형이 관찰되면 첫 질문은 "왜 농도가 폭발했는가?"가 아니라 **"무엇이 dose-normalized superposition하지 않는가?"**이다. 동일한 AUC/Dose 이상이라도 $F$가 올라간 것인지, $CL$이 내려간 것인지, $f_u$가 바뀐 것인지 — 각각의 임상 결론이 완전히 달라진다.

**이 직관을 머릿속에 박고 아래를 읽어라**: 이 세션의 모든 수식과 예시는 superposition 붕괴라는 공통 문법의 서로 다른 방언일 뿐이다.

---

**A. 중첩 원리 정의**

선형 PK에서는 동일 경로·제형·방법 하에서 용량 보정된 혈장 농도, AUC, 소변 회수율이 모든 시점에서 superimpose된다. 이 원리가 성립하지 않으면 pharmacokinetics is **dose-dependent or nonlinear**. 투여 경로·제형·방법 변경에 의한 붕괴는 포함하지 않는다.

**시간 의존성 정의**: Levy [1982]:
> *"If that was a true time-dependent system, drug clearance should change with time while drug concentration is time invariant."*

---

**B. Gabrielsson 탐색적 분석 권장 절차 (G&W §2.7.1)**

linear plot → semi-log plot → dose-normalized C-time plot → AUC vs Dose → **AUC/Dose vs Dose**.

G&W Figure 2.86 — 4가지 AUC/Dose vs Dose 패턴:

| 패턴 | AUC/Dose 형태 | 의미 |
|---|---|---|
| 선형 | 수평 | 정상 |
| Feedback-governed | 하강 | 면역글로불린처럼 약물이 자신의 소실을 촉진 |
| MM 소실 | 단조 상승 | 대사 효소 포화 → AUC가 dose보다 빠르게 증가 |
| MM + 1차 병렬 | 저용량 상승 후 plateau | salicylic acid — 두 기전이 공존 |

> 💡 **[AUC/Dose vs Dose 그래프 읽는 법]** 이 그래프를 "비선형성 탐지기"로 생각하라. X축은 용량, Y축은 AUC를 용량으로 나눈 값(= 단위 용량당 노출). 선형 약물이라면 이 값이 항상 일정해서 수평선이 된다. 선이 올라가면 "같은 용량을 더 투여해도 비례보다 훨씬 많은 노출이 발생한다"는 적신호다.

---

**C. R&T Table 16-1 분류 체계 (p.496)**

| 과정 | 기전 | 영향 파라미터 | 대표 예 |
|---|---|---|---|
| 용해도 | Limited solubility | $F$↓ | Griseofulvin |
| 장관 능동 수송 | Saturable active absorption | $F$↓ | Amoxicillin |
| 신 분비 | Tubular secretion 포화 | $CL_R$↓ | Dicloxacillin |
| 신 재흡수 | Active reabsorption 포화 | $CL_R$↑ | Ascorbic acid |
| 대사 | Capacity-limited | $CL$↓ | Phenytoin, paroxetine |
| 포화 초회통과 | Saturable first-pass | $F$↑ | Nicardipine |
| 자가유도 | Autoinduction | $CL$↑ | Carbamazepine |
| mechanism-based 억제 | Autoinhibition | $CL$↓ | Clarithromycin |
| 단백결합 | Saturable plasma binding | $V$↑ | Salicylate, naproxen |
| 조직결합/TMDD | Saturable target binding | $V$↓ | Bosentan, imirestat |

*[출처: R&T 5e, Ch.16, Table 16-1, p.496]*

---

**D. R&T 4단계 비선형 인식 워크플로우 (pp.519–521)**

1. 선형 동역학과 비교: dose-normalized superimpose 확인
2. 변화한 파라미터 방향 식별
3. Primary PK 파라미터 ($CL_H$, $CL_R$, $V$, $K_a$, $F$, $f_u$) 결정
4. 기전과의 일치 여부 확인

---

**E. Zettelkasten Atom**

```yaml
aliases: [비선형 PK 진단, superposition 붕괴, 비선형 인식 워크플로우]
tags: [pharmacometrics/pk/nonlinear, clinical/TDM, pharmacometrics/methodology]
source: "R&T 5e, Ch.16, pp.491–496, 519–521; G&W 5e, §2.7.1, pp.112–114"
```

비선형 PK의 핵심은 superposition 붕괴이며, 그 방향($F$↑/$F$↓/$CL$↑/$CL$↓/$V$↑/$V$↓)이 기전을 결정한다. Dose-normalized AUC vs Dose plot의 기울기 방향이 기전 감별의 첫 관문이며, R&T 4단계 워크플로우가 체계적 역추론의 도구다.

---

---

## 카드 2. Michaelis-Menten 소실 동역학 [⚡ Apex Concept]

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가**: 페니토인 300 mg/day → 500 mg/day 증량 시 혈중 농도 4 mg/L → 36 mg/L로 9배 폭증해 독성 뇌증이 발생한다 — 이 하나의 사실이 MM 소실을 임상약리학 전체에서 가장 위험한 개념으로 만든다. 그리고 PK17처럼 데이터가 $K_m$ 주변 곡률을 포함하지 않으면 $V_{max}$와 $K_m$이 분리 추정되지 않아 — 선형처럼 보이는 피팅 결과가 Phase 2에서 독성 폭발을 유발한다.

**체화해야 할 단 하나의 직관**: **고농도에서 maximal인 것은 rate(소실 속도)이고, 저농도에서 maximal인 것은 clearance(청소율)이다.** 이 두 축을 헷갈리면 모든 임상·NONMEM 추론이 거꾸로 된다.

**이 직관을 머릿속에 박고 아래를 읽어라**: 아래 수식들은 모두 "효소가 포화될수록 처리 효율(clearance)이 떨어지는 것"을 수학으로 번역한 것이다.

---

**A. Formal Definition**

MM 소실 동역학이란, 약물 소실 속도가 효소 포화로 인해 농도에 비례하지 않고 최대 소실 속도 $V_{max}$에 점근하는 saturable 과정이다. 치료 농도가 $K_m$ 값에 근접하거나 초과할 때 동역학이 비선형이 된다.

---

**B. Derivation — IV Bolus + 상수속도주입 통합**

**Step 1. 선형 소실 기준**

$$\frac{dC}{dt} = -\frac{CL}{V} \cdot C, \quad CL = \text{상수} \tag{G\&W Eq.2:265}$$

**Step 2. MM 소실로 청소율 대체**

$$CL(C) = \frac{V_{max}}{K_m + C} \tag{G\&W Eq.2:266}$$

| 파라미터 | 단위 | 생물학적 의미 |
|---|---|---|
| $V_{max}$ | µg/min | 효소 총량에 비례하는 최대 대사 속도 |
| $K_m$ | µg/mL | 소실 속도가 $V_{max}/2$일 때의 기질 농도; 효소 친화도의 역수 |

*[출처: G&W 5e, §2.7.2, Eq.2:266, p.115; R&T 5e, Ch.16, Eq.16-1~16-2, p.494]*

**⚠️ 필수 구분** (G&W Figure 2.88):
- $C$↑ → **$CL$↓** (hyperbola, $C=0$에서 $V_{max}/K_m$ 최대)
- $C$↑ → **Rate↑** (saturation curve, $V_{max}$에 점근)

> 💡 **[Rate와 CL이 반대 방향인 이유]** 공장(효소) 비유로 기억하라. Rate = "하루 생산량". CL = "단위 원료당 생산 효율". 원료(약물)가 넘쳐날 때(고농도), 공장은 최대 속도로 돌아가 하루 생산량(Rate)이 최대지만 — 원료 한 단위를 처리하는 효율(CL)은 오히려 바닥이다. 반대로 원료가 희박할 때(저농도), 공장이 원료 하나하나를 즉시 처리하므로 효율(CL)은 최대지만 총 생산량(Rate)은 적다.

**Step 3. IV Bolus ODE**

$$\frac{dC}{dt} = -\frac{V_{max} \cdot C}{K_m + C} \cdot \frac{1}{V} \tag{G\&W Eq.2:270}$$

**Step 4. 상수속도주입 ODE**

$$\frac{dC}{dt} = \left( Input - \frac{V_{max} \cdot C}{K_m + C} \right) \cdot \frac{1}{V} \tag{G\&W Eq.2:273}$$

$Input = Dose/T_{inf}$ (주입 중), $0$ (주입 후).

> 💡 **[Input > Vmax이면 왜 항정상태가 불가능한가]** 양동이에 물을 붓는 데 구멍(효소)은 최대 분당 107 µg밖에 배출을 못 하는데, 수도꼭지(Input)가 분당 138 µg을 쏟아 붓고 있는 상황이다. 아무리 기다려도 양동이의 물 수위는 계속 오르기만 한다 — 수학적으로 $dC/dt > 0$이 항상 성립하므로 $C_{ss}$가 존재할 수 없다. PK17 slow infusion rate = 138.4 µg/min > $V_{max}$ = 107 µg/min이 바로 이 상황이다.

*[출처: G&W 5e, §2.7.2.2, Eq.2:273, p.118]*

**Step 5. 두 극한 조건**

*극한 1: $C \gg K_m$ (포화)*
$$Rate \approx V_{max} \tag{G\&W Eq.2:268}$$

*극한 2: $C \ll K_m$ (불포화)*
$$Rate \approx \frac{V_{max}}{K_m} \cdot C = K' \cdot C \tag{G\&W Eq.2:269}$$

⚠️ G&W (p.119): **"The system may already behave in a nonlinear fashion at concentrations which are 10-20% of $K_m$."**

**Step 6. AUC 공식 (IV bolus)**

$$AUC = \frac{C^0}{V_{max} \cdot 2} \cdot \left[K_m + \frac{C^0}{2}\right] \tag{G\&W Eq.2:271}$$

*[출처: G&W 5e, §2.7.2.1, Eq.2:271, p.117]*

> 💡 **[왜 AUC가 C⁰의 이차함수인가]** 전개하면 $AUC = \frac{K_m \cdot C^0}{2V_{max}} + \frac{(C^0)^2}{4V_{max}}$다. 첫 항은 $C^0$에 선형, 둘째 항은 $(C^0)^2$에 비례한다. 저농도($C^0 \ll K_m$)에서 둘째 항이 작아 AUC가 거의 선형처럼 보이지만, 농도가 올라갈수록 제곱항이 지배해 AUC가 용량보다 훨씬 빠르게 증가한다. 이것이 "고농도 코호트 없이는 비선형성을 포착 못 한다"는 말의 수학적 근거다.

→ AUC는 $C^0$의 이차 함수 — 투여량 2배 시 AUC > 2배.

**Step 7. 순간 반감기**

$$t_{1/2}^{inst}(C) = \ln(2) \cdot \frac{V}{V_{max}} \cdot (K_m + C) \tag{G\&W Eq.2:272; PK17 Eq.17:3}$$

*[출처: G&W 5e, Eq.2:272, p.117]*

> 💡 **["순간(instantaneous)" 반감기란]** "지금 이 농도에서의 소실 속도로 계속 달린다면 반감에 얼마가 걸리겠는가"라는 스냅샷이다. 실제로는 농도가 내려가면 소실이 빨라지므로 이 값은 계속 줄어든다 — 즉 선형 PK의 고정된 $t_{1/2}$와 달리, MM 반감기는 농도가 내려갈수록 같이 줄어드는 움직이는 표적이다. 그래서 "$5 \times t_{1/2}$에 항정상태 도달" 공식을 MM 약물에 쓰면 항정상태 도달 시간을 심각하게 과소추정한다.

→ $C$↑ → $t_{1/2}$↑. 고농도에서 반감기가 더 길다. 선형 PK와 정반대.

**PK17 실제 파라미터** (Agent X, G&W):

| 파라미터 | Linear | MM | CV% |
|---|---|---|---|
| $V$ (mL) | 1380 | 1450 | 5 |
| $CL$ (mL/min) | 43.3 | — | — |
| $V_{max}$ (µg/min) | — | 107 | 2 |
| $K_m$ (µg/mL) | — | 0.56 | 5 |

- 최단 t½ ≈ 5 min ($C=0$); 선형 모델 예측 ≈ 20 min → **4배 차이**
- $K_m$–$V$ 상관 = **−0.96**

> 💡 **[상관 −0.96의 기하학적 의미]** NONMEM이 파라미터 공간에서 OFV를 최소화할 때, $K_m$이 커지면 $V$를 줄여도 데이터를 비슷하게 설명할 수 있다는 뜻이다. 비유하면, 두 사람이 한 팀으로 줄다리기를 하는데 한 명이 더 당기면 다른 한 명은 덜 당겨도 되는 상황 — 두 파라미터가 협박과 양보로 서로 얽혀 있어서, 각자의 "진짜 값"을 독립적으로 특정할 수 없다. 이것이 **structural identifiability 실패**다. 정밀도(CV%)가 좋아 보여도 외삽은 금지다.

- G&W: "pilot study에 불과" — 고용량 코호트 추가 필수

**NONMEM 구현 코드 (L5)**

```fortran
$SUBROUTINES ADVAN13 TOL=6

$MODEL
  COMP (CENTRAL)

$PK
  VMAX  = THETA(1) * EXP(ETA(1))   ;; µg/min
  KM    = THETA(2) * EXP(ETA(2))   ;; µg/mL
  V     = THETA(3) * EXP(ETA(3))   ;; mL
  S1    = V                         ;; IPRED = A(1)/S1

$DES
  C       = A(1) / V
  RATE    = VMAX * C / (KM + C)     ;; Eq.2:270
  DADT(1) = R1 - RATE               ;; R1=0이면 bolus, R1>0이면 infusion

$ERROR
  IPRED = A(1) / S1
  W     = SQRT(SIGMA(1,1)**2 * IPRED**2 + SIGMA(2,2)**2)
  Y     = IPRED + W * EPS(1)

$THETA
  (0, 107)   ;; VMAX — PK17 기준
  (0, 0.56)  ;; KM
  (0, 1450)  ;; V

$OMEGA
  0.04  ;; IIV-VMAX
  0.04  ;; IIV-KM
  0.04  ;; IIV-V

$SIGMA
  0.04  ;; proportional
  0.1   ;; additive (µg/mL)²

$ESTIMATION METHOD=1 INTERACTION MAXEVAL=9999
$COVARIANCE PRINT=E
```

*대안: `ADVAN10` (1구획 MM 내장) — 단순하지만 2구획 확장 불가.*

*[출처: PK17, G&W 5e, pp.553–555]*

---

**C. Structural Necessity**

MM 방정식이 이 쌍곡선 형태인 이유: 효소-기질 복합체 $[ES]$가 자유 기질 $[S]$보다 훨씬 빠르게 평형에 도달한다는 **quasi-steady-state(준정상상태) 가정**에서 유일하게 유도된다.

> 💡 **[quasi-steady-state 가정이란]** 효소(E)와 기질(S)이 만나 $[ES]$를 형성하는 속도가 너무 빨라서, 임의의 순간에 $[ES]$의 농도는 항상 S의 농도에 비례해 "이미 평형에 있다"고 가정하는 것이다. 이 가정이 있어야 Michaelis와 Menten의 원래 ODE 시스템이 단 하나의 쌍곡선으로 단순화된다. 가정이 깨지는 경우 — 예컨대 효소 농도가 기질 농도와 비슷하게 높을 때 — 더 복잡한 TMDD 유형 모델이 필요해진다.

---

**C-2. Plausible Fallacy [⚡ Apex]**

**오류**: "$K_m$보다 훨씬 낮은 치료 농도에서 선형 PK라고 가정하고 고용량 AUC를 선형 외삽해도 된다."

**왜 그럴싸한가**: 저용량 Phase 1에서 dose-normalized 프로파일이 superimpose되고 GOF도 좋다.

**나비효과**: G&W 경고대로 $K_m$의 10–20% 농도에서 이미 비선형이 시작되므로, 선형 외삽으로 Phase 2를 설계하면 목표 농도 계산이 완전히 틀린다.

**NONMEM 시그니처**: CWRES가 고농도에서 체계적 양(+), 저농도에서 음(−) 편향 → **"정현파 CWRES 편향"** 패턴.

---

**D. Assumptions & Boundary Conditions**

- 1구획 순간 혼합: 위반 시 분포상 → MM 파라미터 추정 편향
- 단일 효소 경로 ($f_m=1$): 병렬 경로 존재 시 비선형성 완화
- $K_m$·$V_{max}$ 시간 불변: 자가유도 시 $V_{max}(t)$
- Input $\leq V_{max}$: 초과 시 항정상태 불가능

**E. Limitations**

- **반감기 개념 붕괴**: $5 \times t_{1/2}$ 공식 사용 불가
- **AUC 기반 $F$ 계산 부적절**: IV microtracer 필수
- **$V_{max}$–$K_m$ 상관**: 고농도 데이터 없으면 분리 추정 불가

**F. Five Cognitive Layers**

| 레이어 | 내용 |
|---|---|
| **L1 형식적 수학** | Eq.2:270 (bolus), Eq.2:273 (infusion), Eq.2:271 (AUC), Eq.2:272 (t½) |
| **L2 기하학적 직관** | Semi-log: 고농도 완만→저농도 가팔라짐 (선형 PK와 정반대) |
| **L3 구조적 동일성** | MM효소↔Emax PD↔수송체($T_m/K_T$)↔단백결합($B_{max}/K_d$) — 동일 쌍곡선 |
| **L4 생리학적 의미** | $V_{max}$∝CYP 발현량; $K_m$=효소 친화도 역수. 유도→$V_{max}$↑; 경쟁억제→$K_m$↑ |
| **L5 실무 투영** | ADVAN13+$DES; ADVAN10 대안; 상관−0.96=identifiability 선언; 고농도 코호트 FDA 협의 |

**G. Zettelkasten Atom**

```yaml
aliases: [Michaelis-Menten PK, MM 소실, 포화 동역학]
tags: [pharmacometrics/pk/nonlinear/capacity, nonmem/DES/ADVAN13, clinical/TDM]
source: "G&W 5e, §2.7.2, PK17 pp.553–555; R&T 5e, Ch.16, pp.493–495"
```

MM 소실에서 저농도 = maximal clearance, 고농도 = maximal rate. $K_m$의 10–20% 농도에서 비선형이 시작된다. 상수속도주입 시 Input > $V_{max}$이면 항정상태 자체가 불가능(Eq.2:273). PK17 상관 −0.96은 structural identifiability 실패이며, 외삽이 금지된다.

---

---

## 카드 3. 입력 속도 Catastrophe — Phenytoin & Alcohol Plateau

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가**: 페니토인 $V_m=500$ mg/day 환자에서 425 mg/day → $C_{ss}$=22.7 mg/L, 400 mg/day → 16 mg/L다. 25 mg/day 차이가 7 mg/L 차이를 만든다. $V_m$과 동일한 용량을 투여하면 항정상태 자체가 수학적으로 존재하지 않는다.

**체화해야 할 단 하나의 직관**: 발산 경계는 $R_0 \to V_m$이고, $K_m$은 hard threshold가 아니라 농도 축의 scale을 결정한다.

---

**A & B. 항정상태 수식 및 임상 수치**

$$C_{u,ss} = \frac{K_m \cdot R_0}{V_m - R_0} \tag{R\&T Eq.16-6, p.501}$$

*[출처: R&T 5e, Ch.16, Eq.16-6, p.501]*

| $R_0$ (mg/day) | $C_{ss}$ (mg/L) |
|---|---|
| 300 | 6.0 |
| 350 | 9.3 |
| 400 | 16.0 |
| 425 | 22.7 |

*[R&T Figure 16-10; $K_m'$=4 mg/L, $V_m$=500 mg/day, $V$=50 L]*

**개막 사례**: 300 mg/day ($C_{ss}$=4 mg/L) → 500 mg/day → nystagmus·ataxia, $C_{ss}$=36 mg/L. 67% 증량에 9배 폭증.

$$t_{90} = \frac{K_m' \cdot V(2.303 \cdot V_m - 0.9 R_0)}{(V_m - R_0)^2} \tag{R\&T Eq.16-10, p.504}$$

**$V_m$ vs $K_m$ 변화의 비대칭성**:
- $V_m$ 20% 감소 → $C_{ss}$ **2배** (비선형 폭발)
- $K_m$ 50% 증가(cimetidine) → $C_{ss}$ 50% **선형 비례**

**알코올**: $V_m \approx 10$ g/hr, $K_m \approx 100$ mg/L. $R_0 > V_m$이면 항정상태 불가능.

**E. Zettelkasten Atom**

```yaml
aliases: [페니토인 Css, MM 항정상태, plateau, 발산 경계]
source: "R&T 5e, Ch.16, Eq.16-6~16-10, pp.500–506"
```

발산 경계는 $R_0 \to V_m$. $V_m$ 변화는 비선형 폭발, $K_m$ 변화는 선형 비례. $t_{90} \propto (V_m-R_0)^{-2}$이므로 pseudosteady-state 오인 위험이 크다.

---

---

## 카드 4. 혼합 병렬 경로 (MM + 1차) — Salicylic Acid

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가**: salicylic acid의 총 clearance가 치료 범위에서 비교적 일정해 선형처럼 보인다. 실제로는 비결합 농도가 dosing rate 초비례로 쌓이고 있다 — 총 농도만 보면 안전해 보이는 약물이 비결합 독성 농도에 있을 수 있다.

---

**A. 병렬 경로 수식**

$$CL = CL_{lin} + \frac{V_{max} \cdot C}{K_m + C} \tag{R\&T Eq.16-11, p.506}$$

*[출처: R&T 5e, Ch.16, Eq.16-11, p.506]*

**$f_m$ 임계값**: saturable 경로 $f_m \geq 0.5$이어야 총 clearance에 실질적 영향.

**Salicylic Acid 소변 회수율** (Levy 1965):

| 용량 (mg) | Unchanged SA (%) | Salicyluric acid (%) |
|---|---|---|
| 192 | 3 | 83 |
| 1533 | 17 | 59 |
| 3000 | 14 | 50 |

총 $CL$은 비교적 일정 — saturable metabolism($CL_u$↓)과 saturable binding($f_u$↑)이 서로 상쇄. 그러나 **비결합 $C_{u,ss}$는 dosing rate 초비례 증가** (R&T Figure 16-29).

---

## 카드 5. 비선형 흡수 & 포화 초회통과

**Nicardipine** (Wagner 1987, R&T Table 16-2): 10→40 mg q8h, $F$ 19%→36%. 반감기 변화 없음.

**Amoxicillin** (Sjövall 1985): 375→3000 mg, dose-normalized AUC·$C_{max}$ 감소, $t_{max}$ 유사.

> 💡 **[$t_{max}$가 변하지 않는 이유]** Amoxicillin은 소장의 특정 구역에 있는 peptide transporter를 통해서만 흡수된다. 용량이 아무리 달라져도 약물이 그 흡수 구역을 지나는 시간은 변하지 않으므로 $t_{max}$도 거의 일정하다. 만약 비선형성이 흡수 속도(Ka)의 포화 때문이 아니라 용해도 제한 때문이라면 $t_{max}$가 용량에 따라 달라질 것이다 — 이 차이가 기전 감별의 단서가 된다.

**감별 핵심**: Oral 데이터만으로 $F$↓($CL$ 일정) vs $CL$↑($F$ 일정) 구분 불가 → **IV comparator 필수**.

---

## 카드 6. 신배설 비선형성

**포화 분비 (Dicloxacillin, Nauta 1976)**: $f_u=0.04$, 1g→2g IV, $CL_R$ 감소.

**포화 재흡수 (Ascorbic acid)**: 75mg→10,000mg/day(133배), $C_{ss}$ 9→19 mg/L(2배). $CL_R$ < 0.5→21 mL/min(42배 증가).

**결합 artifact (Disopyramide, Giacomini 1982)**: 총 $CL_R$ 시간에 따라 감소, 비결합 $CL_R$ 일정 → $\alpha_1$-AGP 포화에 의한 $f_u$ 변화가 총 $CL_R$ 겉보기 이상을 만듦.

---

## 카드 7. 단백·조직결합 비선형성 & TMDD 브리지

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가**: Warfarin-phenylbutazone 상호작용의 실제 원인은 단백결합 경쟁이 아니라 CYP2C9 억제다. in vitro 결합 데이터를 in vivo로 잘못 외삽하는 수십 년의 오류가 여기서 끊어진다.

**체화해야 할 단 하나의 직관**: In vivo 개방계에서 $C_u^{ss} = Dose\ rate / CL_u$이므로, $f_u$만 변하고 $CL_u$ 불변이면 $C_u^{ss}$ 불변 → 약효 불변.

---

**$f_u$ 비선형 거동 (G&W Eqs.2:297–2:299)**:

저농도: $f_u$ = 상수, 고농도($C_u \gg 1/K_a$): $f_u \to 1$.

*[출처: G&W 5e, §2.7.5, Eqs.2:297–2:299, pp.130–131]*

**TMDD 예시들**: Bosentan($V_{ss}$ 용량 의존 감소), trandolaprilat(biphasic decline ← binding 동역학, 분포 아님), imirestat, draflazine. → I-08 TMDD 브리지.

---

## 카드 8. 시간 의존성 동역학

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가**: carbamazepine 단기 PK 데이터로 만든 투여 계획이 외래 2–3주 후 완전히 무효. clarithromycin은 7번째 투여에서 반감기가 단회보다 길어진다.

**체화해야 할 단 하나의 직관**: Capacity-dependence = "농도 때문에" CL이 바뀜. Time-dependence = "몸이 바뀌어서" CL이 바뀜.

---

**효소 Turnover ODE**

$$\frac{dE}{dt} = R_{in} - k_{out} \cdot E \tag{G\&W Eq.2:275}$$

$$Cl_t = Cl' - (Cl' - Cl) \cdot e^{-k_{out}(t-t_{lag})} \tag{G\&W Eq.2:282}$$

*[출처: G&W 5e, §2.7.3.2, p.121]*

> 💡 **[$k_{out}$이 새 항정상태 도달 속도를 결정하는 이유]** 유도제가 $R_{in}$을 올리면 효소가 더 많이 만들어지지만, 효소가 새 수준까지 쌓이는 속도는 효소의 자연 분해 속도($k_{out}$)에 달려 있다. 비유하면, 수도꼭지(합성)를 더 세게 틀어도 욕조(효소 pool)가 가득 차는 시간은 배수구(분해, $k_{out}$) 크기가 결정한다 — 배수구가 작으면($k_{out}$이 작으면) 채워지는 것도 느리다. 따라서 carbamazepine처럼 $k_{out}$ t½가 수일~수십일인 약물은 자가유도가 완전히 발현되기까지 몇 주가 걸린다.

**G&W Table 2.16 선택값**: Carbamazepine $k_{out}$ t½ = 24–806 h; Phenobarbital→NT = 140 h.

**PK21 (NT-Pb, von Bahr 1998)**: Pre-induction $Cl_{po}$=46 L/h → 118 L/h; $k_{out}$ t½=**158 h**; MRT 36→14 h.

설계 강점: repeated trough values가 $k_{out}$ 추정에 결정적.

**Product inhibition** (G&W Figure 2.87 우측 열): 대사물이 $V_{max}$를 억제 → $CL$ 감소. 농도가 낮아져도 $CL$이 회복되지 않으면 time-dependence의 증거.

---

---

# §5 — 혼동 쌍 해부

---

## 혼동 쌍 1: $V_{max}$ vs. $K_m$ — Critical Blow ←

| 비교 차원 | $V_{max}$ | $K_m$ |
|---|---|---|
| **수식 위치** | $CL = V_{max}/(K_m+C)$ — 분자 | 분모의 일부 |
| **생물학적 지시체** | 효소 총량에 비례 | 효소 친화도의 역수 |
| **변화 유발 원인** | 유도↑, 간경변↓, 비경쟁 억제↓ | 경쟁적 억제→↑; 유도는 불변 |
| **$C_{ss}$ 반응** | **비선형 폭발**: 20% 감소 → 2배 상승 | **선형 비례**: 50% 증가 → 50% 상승 |
| **⚡ 기억 고리** | **$V_{max}$는 공장 전체 생산 한계 — 조금 줄어도 분모$(V_m-R_0)$가 0에 급격히 수렴한다. $K_m$은 기계 정밀도 — 낮아지면 그만큼 선형으로 비례 반응한다. 비선형 폭발을 만드는 것은 항상 $V_{max}$다.** | |
| **치명적 타격** | 간경변 환자에서 $V_{max}$ 20% 감소를 $K_m$ 변화(선형 비례)로 오인 → "50% 농도 증가"로 예측하고 50% 감량 → 실제로는 2배 상승을 막기에 부족해 독성 진입. | |

---

## 혼동 쌍 2: MM 순간 반감기 vs. 선형 PK terminal half-life — **신규**

| 비교 차원 | MM $t_{1/2}^{inst}(C)$ | 선형 terminal $t_{1/2}$ |
|---|---|---|
| **수식** | $\ln(2) \cdot V/V_{max} \cdot (K_m+C)$ | $0.693 \cdot V/CL$ |
| **농도 의존성** | 농도에 **비례 증가** | **농도 무관** |
| **Semi-log 패턴** | 시간이 지날수록 slope 가팔라짐 | 직선 |
| **$5 \times t_{1/2}$ 공식** | **사용 불가** | 신뢰 가능 |
| **⚡ 기억 고리** | **MM 반감기는 약물 자신이 결정하는 순간의 초상화 — 농도가 내려갈수록 화가의 붓질이 빨라진다. 선형 반감기는 처음부터 끝까지 같은 속도로 그려지는 정물화다.** | |

---

## 혼동 쌍 3: 저농도에서 Maximal한 것 — Rate vs. Clearance

| 비교 차원 | Elimination Rate | Intrinsic Clearance |
|---|---|---|
| **수식** | $V_{max}C/(K_m+C)$ | $V_{max}/(K_m+C)$ |
| **저농도** | 작음 | **최대** ($V_{max}/K_m$) |
| **고농도** | **최대** ($\approx V_{max}$) | 최소 (→0) |
| **⚡ 기억 고리** | **효소는 약을 먹는 기계: 배고플 때(저농도) 먹는 '효율(CL)'이 최고지만 '양(Rate)'은 적다. 포화될 때(고농도) '양(Rate)'이 최대지만 '효율(CL)'은 최저다.** | |

---

## 혼동 쌍 4: Capacity-dependent vs. Time-dependent

| 비교 차원 | Capacity-dependent | Time-dependent |
|---|---|---|
| **Levy 판별 기준** | 농도 불변 시 CL도 불변 | 농도 불변 시에도 CL이 변함 |
| **진단 설계** | 여러 dose level, 단회 투여 | 반복 투여 trough series |
| **⚡ 기억 고리** | **농도가 바뀌어 시스템이 달라 보이면 capacity. 시간이 지나 몸이 바뀌어 시스템이 달라지면 time-dependence.** | |

---

## 혼동 쌍 5: In vitro 단백결합 증가 → 약효 감소 vs. In vivo → 약효 불변

| 비교 차원 | In vitro 폐쇄계 | In vivo 개방계 |
|---|---|---|
| **핵심 관계** | 총 약물량 고정 → $C_u$↓ → 약효↓ | $C_u^{ss}=Dose\ rate/CL_u$ → $f_u$ 무관 → 약효 불변 |
| **⚡ 기억 고리** | **시험관은 저수지 없는 수영장. 생체는 계속 물이 공급되는 수영장 — 진짜 약효를 결정하는 것은 배수구 크기($CL_u$)지, 수영장 벽 두께($f_u$)가 아니다.** | |

---

# §7 — Self-Test: Active Recall Module

---

**Q1** [○] MM 방정식에서 "저농도에서 maximal"인 것과 "고농도에서 maximal"인 것은? $CL=V_{max}/2$가 되는 농도 조건을 도출하라.

<details><summary>정답 공개</summary>

**저농도 maximal: Clearance** ($V_{max}/K_m$). **고농도 maximal: Rate** ($V_{max}$). 조건: $C=K_m$.

G&W: $K_m$의 10–20%에서 이미 비선형 시작 — "$K_m$이 경계"라는 단순화는 위험.

**다음 깊이 질문**: PK17에서 관찰 기간 대부분이 $C > K_m$ 구간이었다는 것의 임상적 의미는?
</details>

---

**Q2** [★★] 페니토인 $K_m'=4$, $V_m=500$ mg/day, $V=50$ L. $R_0=400$ mg/day에서 $C_{ss}$를, $V_m$ 20% 감소 시 결과를 계산하라.

<details><summary>정답 공개</summary>

$C_{ss}=4\times400/(500-400)=\mathbf{16}$ mg/L. $V_m=400$ mg/day → 분모=0 → **항정상태 불가능**. $R_0=300$으로 감량 시: 12 mg/L.

**다음 깊이 질문**: cimetidine이 $K_m'$을 4→6 mg/L로 올리면 $R_0=400$ mg/day에서 $C_{ss}$는?
</details>

---

**Q3** [★★] PK17에서 "pilot study에 불과"한 두 가지 이유를 수학적 근거와 함께. ADVAN10 vs ADVAN13 선택 이유는?

<details><summary>정답 공개</summary>

①  slow infusion rate=138.4 µg/min > $V_{max}$=107 → Eq.2:273에서 항정상태 불가능. ② $K_m$–$V$ 상관 −0.96 → structural identifiability 실패, 외삽 금지.

**ADVAN13+$DES**: 2구획·TMDD 등 복잡한 모델로 확장 가능. ADVAN10은 단순하지만 1구획으로 제한.

**다음 깊이 질문**: 상관 −0.96의 파라미터 공간 기하학적 의미는?
</details>

---

**Q4** [★] Eq.2:273에서 항정상태 존재의 필수 조건을 도출하고, PK17 slow infusion이 이를 만족하는지 확인하라.

<details><summary>정답 공개</summary>

$dC/dt=0$ → $Input=V_{max}C_{ss}/(K_m+C_{ss})$ → 이 식이 양의 $C_{ss}$를 갖으려면 반드시 $Input < V_{max}$. PK17: 138.4 > 107 → **불만족, 항정상태 불가능**.

**다음 깊이 질문**: Input이 $V_{max}$를 초과하면 농도는 어떤 거동을 보이는가?
</details>

---

**Q5** [★] AUC/Dose↓ + $t_{max}$ 불변 vs. AUC/Dose↑ + 반감기 변화 없음 — 각각 기전과 감별법.

<details><summary>정답 공개</summary>

↓ + $t_{max}$ 불변 → Saturable active intestinal absorption (amoxicillin). IV comparator로 감별.

↑ + 반감기 불변 → Saturable first-pass (nicardipine). IV microtracer로 $F$ 직접 측정.

**다음 깊이 질문**: IV에서도 AUC/Dose↑라면 어떤 기전인가?
</details>

---

**Q6** [★] G&W PK21 핵심 수치 3개와 "설계의 강점"은?

<details><summary>정답 공개</summary>

① $Cl_{po}$ 46→118 L/h (2.6배). ② $k_{out}$ t½=158 h. ③ MRT 36→14 h.

강점: "the repeated trough values of NT throughout the experimental period. This captures information about the fractional turnover rate kout."

**다음 깊이 질문**: Pb 중단 후 NT 농도 회복 시간은 어느 반감기가 지배하는가?
</details>

---

**Q7** [○] Disopyramide의 총 $CL_R$이 시간에 따라 감소하지만 비결합 $CL_R$은 일정하다. 의미는?

<details><summary>정답 공개</summary>

$\alpha_1$-AGP 포화에 의한 **단백결합 artifact**. 고농도 시 $f_u$↑ → 총 $CL_R$ 높아 보임 → 농도 감소에 따라 $f_u$↓ → 총 $CL_R$ 겉보기 감소. 실제 신기능 변화 아님. 고단백결합 약물의 신배설 이상은 반드시 비결합 농도와 함께 분석해야 한다.

**다음 깊이 질문**: Prospective하게 피하려면 PK 연구 설계에서 무엇을 추가해야 하는가?
</details>

---

**Q8** [★] NONMEM $DES 블록에서 상수속도주입과 IV bolus를 단일 코드로 처리하는 방법은?

<details><summary>정답 공개</summary>

```fortran
$DES
  C       = A(1) / V
  RATE    = VMAX * C / (KM + C)
  DADT(1) = R1 - RATE
```

`R1`은 NONMEM이 데이터셋 RATE column에서 자동 제공하는 현재 주입 속도. IV bolus 시 R1=0 → 자동으로 Eq.2:270으로 작동.

**다음 깊이 질문**: FOCE INTERACTION vs FO — MM 모델에서 어느 것이 더 정확하며 그 이유는?
</details>

---

**Q9 — 보스 딜레마** [★★]

> **시나리오**: Oral 항간질제 Phase 1 FIH. 저용량(100–200 mg)에서 dose-normalized AUC 약간 증가 경향. MM 모델 $K_m'$=30 mg/L (95% CI: 5–150 mg/L). 치료 목표 10–20 mg/L. 규제 팀: "유의하지 않으니 선형 가정으로 Phase 2(500 mg) 설계 가능." 모델링 팀: "$K_m'$ CI가 너무 넓어 위험." 수석 모델러로서 어느 방향을 지지하는가?

<details><summary>수석 모델러의 Trade-off 논리</summary>

**규제 팀 취약점**: $K_m'$ CI=5–150 mg/L는 선형 확인이 아니라 **structural identifiability 실패**를 의미한다.

> 💡 **[Structural identifiability 평이하게]** "$V_{max}$와 $K_m$을 독립적으로 알아낼 수 있는 충분한 정보가 데이터에 없다"는 뜻이다. 두 파라미터가 얽혀 있어서, $V_{max}$를 크게 잡고 $K_m$도 크게 잡아도, 또는 둘 다 작게 잡아도 데이터를 비슷하게 설명할 수 있다. 이 상태에서 추정된 $K_m'$=30 mg/L는 "진짜 $K_m$이 30 mg/L"라는 뜻이 아니라 "어떤 값이어도 현재 데이터를 설명하는 데 크게 불이익이 없다"는 의미다.

치료 목표(10–20 mg/L)가 $K_m'$ 추정치(30 mg/L)의 60–70% 수준이므로, G&W 경고(10–20% $K_m$에서 비선형 시작)에 따라 치료 농도 전반이 이미 비선형 구간일 수 있다.

**결정**:
1. MM·선형 모두 피팅 → OFV, $K_m'$ RSE%, dose-normalized AUC 방향을 규제 문서에 투명하게 기술
2. **고용량 코호트(400 mg) 추가 권고** — $K_m'$ CI를 좁혀 Phase 2 용량이 $V_m$ 근방인지 판별
3. FDA Type B meeting: "추가 코호트 없이 Phase 2 진입 불동의" 서면화
4. $COV step: $K_m'$ RSE%>50% 또는 condition number>1000이면 identifiability 실패로 추가 데이터 필요성 강화
</details>

---

# §8 — Meta-Frame & Big Picture

### A. Positioning

I-07은 28세션 아키텍처에서 선형 PK의 안전한 세계가 무너지는 첫 번째 관문이자, I-08~I-10과 II-04의 생물학적 근거를 제공하는 허브다.

- **이전**: I-01, I-03, I-05
- **다음**: I-08 (TMDD), I-09 (Emax), I-10 (Indirect Response), II-04 ($DES)
- **의존 도메인**: PopPK ($\eta$ 위치), PBPK (간 효소 포화), TMDD, QSP

### B. Dependencies

**실패 1**: Bosentan처럼 $V_{ss}$ 용량 의존적인 약물을 단순 2구획으로 피팅 → $CL$ 과소추정.

**실패 2**: Oral AUC/Dose↑를 대사 포화로만 해석 → 포화 초회통과($F$↑)와 혼동 → II-08 공변량 분석 오류.

**실패 3**: PK17 상관 −0.96을 단순 정밀도 문제로 무시 → Phase 2 독성. II-09b ($COV step, condition number)의 concrete anchor가 바로 이 사례다.

### C. Professional Moat

AI와 소프트웨어는 MM 모델을 피팅하고 $V_{max}$·$K_m$을 수치로 출력할 수 있다. 그러나 이 세션을 진정으로 내면화한 모델러만이 다음을 할 수 있다:

$COV step 출력에서 $K_m$–$V$ 상관 −0.96, $K_m$ RSE%=45%, condition number=847을 보는 순간 — "이것은 정밀도 문제가 아니라 structural identifiability 실패다. 현재 추정된 $V_{max}$와 $K_m$은 독립 추정치가 아니라 $V_{max}/K_m$ 비율 하나만 추정한 것이다" — 라고 즉시 판단한다. 동시에 Phase 2 용량이 Eq.2:273의 발산 조건($Input \geq V_{max}$)에 해당하는지 계산하고, 이것을 FDA Deficiency Letter 방어 언어로 번역할 수 있다. 이것은 알고리즘이 복제할 수 없는 **수식의 구조적 의미와 임상·규제 결과를 연결하는 인과 추론 역량**이다.

---

```
---
✦ STEP 1 완료. (Enhanced + Annotated Edition)

추가된 주석 위치 요약:
  1. [AUC/Dose vs Dose 읽는 법] — §1 카드 B, 탐색적 분석 절차 뒤
  2. [Rate와 CL이 반대 방향인 이유] — 카드 2, 필수 구분 박스 뒤
  3. [Input > Vmax이면 왜 항정상태가 불가능한가] — Eq.2:273 뒤
  4. [왜 AUC가 C⁰의 이차함수인가] — Eq.2:271 뒤
  5. ["순간 반감기"란 무엇인가] — Eq.2:272 뒤
  6. [Km-V 상관 -0.96의 기하학적 의미] — PK17 파라미터 표 뒤
  7. [quasi-steady-state 가정이란] — C. Structural Necessity 뒤
  8. [$t_{max}$가 변하지 않는 이유] — 카드 5, Amoxicillin 뒤
  9. [$k_{out}$이 새 항정상태 도달 속도를 결정하는 이유] — 카드 8, 효소 Turnover ODE 뒤
  10. [Structural identifiability 평이하게] — Q9 보스 딜레마 답 안

"계속"을 입력하면 Step 2(V5.1 Apex Edition HTML 컴파일러)가 실행됩니다.
---
```

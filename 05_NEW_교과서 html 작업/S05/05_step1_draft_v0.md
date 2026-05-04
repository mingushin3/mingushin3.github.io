# PK/PD Mastery Session 05 · Step 1 Draft v0
## 2구획 모델 — 이중지수 분해 / α·β 재파라미터화 / V₁·Vss·Vβ 체계

> **Source:** Gabrielsson & Weiner 5e Ch.2 §2.4.1–2.4.6 + Case Studies PK7/PK8 (p.57–77, p.505–517) + Rowland & Tozer 5e Ch.19 (p.613–656)
> **Mode:** A-Critical | **Output:** Phase 1 Master's Lens Draft v0
> **Source role split:** G&W = 수식 도출·실험 수치·재파라미터화 5종 / R&T = 임상 해석·분포 속도론 결과·terminal half-life 함정

---

## 0. CURATION MAP — Master's Lens First

### MUST (체화 필수 — §2 정식 카드 5개)

| # | 개념 | MUST 판정 근거 (붕괴 테스트) |
|---|---|---|
| **M1** | **이중지수 방정식 + 잔차법 (Method of Residuals)** | 이것 없이는 macro-constant가 어디서 오는지 알 수 없고, 모든 후속 변환식이 공중에 뜬다. 곡선을 두 phase로 분리하는 수학적 조작 자체가 2구획의 본질이다. |
| **M2** | **Macro ↔ Micro ↔ Physiological 3중 좌표계 변환** | Eq.2:121–2:128 (G&W) / Table 19-1 (R&T). NONMEM ADVAN3/4/11/12 선택 근거가 이 변환표 위에 직접 얹힌다. 변환식을 손으로 도출하지 못하면 NONMEM `$PK` 블록이 외워야 할 마법 주문으로 남는다. |
| **M3** | **⚡ V₁ / Vss / Vβ 3중 분포용적 체계** [Apex Concept] | R&T가 명시적으로 *"terminal half-life ceases to have simple application"* 라고 경고한 영역. Gentamicin (Vβ=345L vs Vss=56L, 6배 차이) — 이 셋을 혼동하면 신부전 환자 용량 조정에서 신독성/약효부전이 동시 발생. **Plausible Fallacy 집중 카드.** |
| **M4** | **재파라미터화 5종과 condition number** | G&W PK8 Table 8.1: 동일 데이터에 5개 모델, WRSS는 비슷하나 **condition number 가 29.69 ~ 4,104 사이를 200배 진폭으로 흔들린다.** NONMEM `$COV step` 실패와 NDA Deficiency Letter의 실제 발화점. |
| **M5** | **분포속도론의 임상적 파급 — terminal half-life의 함정** | R&T 핵심 메시지. Nicardipine (terminal t½=12 hr인데 50% Css 도달 1 hr) / Gentamicin (terminal t½ 길지만 plasma는 4-hr 반감기로 행동) — terminal half-life ≠ elimination half-life. f₁/f₂ 분율이 진정한 결정자. |

### CONTEXT (이해 보완 — 인접 MUST 카드 내 1–2문장 처리)

- **AUMC 도출 / MRT = AUMC/AUC** → M2 카드 끝부분 1문장 (1구획에서 이미 학습)
- **Takada / Colburn time-dependent volume models** → M4 카드 내 5종 비교표 한 행으로 처리 (G&W PK8에서 한 케이스로만 등장)
- **Constant-rate infusion / extravascular dose / urine data 미분방정식** → M5 카드 끝 1문장 (G&W §2.4.4–2.4.6은 dose route 응용일 뿐, 2구획 본질은 동일)
- **Catenary vs Mammillary system 구분** → M1 카드 도입부 1문장 (mammillary 가 mainstream)
- **3구획 모델 / SHAM 분석 / AIC·F-test 모델 판별** → §8 후속 지식 그래프에서 언급
- **Bolus + infusion 보정 (eptifibatide 사례) / 다회투여 시 Vss 적용가능 영역** → M5 카드 내 1문장

### 제외 (out of scope)

- Albumin binding / fu·fuT 분포 결정인자 (Ch.4 R&T → 별도 세션)
- Hemodialysis rebound / drug redistribution (R&T §"Drug Redistribution" → 임상약리 별도)
- Pharmacodynamics 전반 (R&T 후반부 → PD 세션)

### Apex / Critical Blow 지정

- **§2 [⚡ Apex Concept]: M3 (V₁/Vss/Vβ)** — C-2 Plausible Fallacy 여기에 집중
- **§5 [▶ Critical Blow]: Vss vs Vβ 혼동쌍** — NDA Deficiency Letter 시나리오

---

## §1 — Session Header & Roadmap

**Session 05 · 2구획 모델: 이중지수 분해와 α·β 재파라미터화**

<!-- MASTER LENS -->
**Big Idea (단 한 문장):**
이중지수곡선의 4개 macro-constant ($A, \alpha, B, \beta$)는 단지 곡선 형상의 수학적 분해가 아니라, **분포(distribution)와 소실(elimination)을 두 phase로 물리적으로 분리해주는 좌표계 변환**이다. 이 변환의 선택(어느 좌표계를 NONMEM에 넘기느냐)이 모델의 수치 안정성($COV step), parameter precision (RSE), 그리고 임상 해석의 정확도를 **동시에** 결정한다.

**개념 항법도 — 다섯 카드:**

```
M1. 이중지수 + 잔차법 [곡선 분해의 수학적 조작]
       ↓ (분해된 4개 상수가 무엇을 의미하는가?)
M2. 3중 좌표계 변환  [Macro ↔ Micro ↔ Physiological]
       ↓ (어느 좌표계의 V를 임상에 쓰는가?)
M3. V₁ / Vss / Vβ   [⚡ Apex — 가장 치명적 혼동]
       ↓ (5종 좌표계의 수치적 행동은 어떻게 다른가?)
M4. 재파라미터화 5종 + condition number
       ↓ (이 모든 것이 왜 임상에서 중요한가?)
M5. 분포속도론의 임상 파급 + terminal half-life의 함정
```

**지식 그래프 위치:**

- **선행 지식 (전제):**
  - 1구획 모델 ($C = C_0 \cdot e^{-k\cdot t}$, $V_d = CL/k$, $AUC = Dose/CL$)
  - MRT = AUMC/AUC 정의 (Session I-?? Mean Residence Time)
  - General ADVAN/$DES (Session II-04) — 미분방정식으로 다구획 표현하는 법
- **이번 세션이 열어주는 후속 지식:**
  - **NONMEM ADVAN3 / ADVAN4 / ADVAN11 / ADVAN12 선택 근거** ← M2·M4가 직접 정당화
  - **Population PK 공변량 모델링에서 Vss vs Vβ 선택** ← M3가 직접 결정
  - **η-shrinkage 해석 / OMEGA 행렬 양정치성 디버깅** ← M4 condition number 이해 필수
  - **3구획·다구획 모델 (deep peripheral compartment, target tissue PK)** ← M1·M2의 자연스러운 확장
  - **TMDD parameter 해석 (Session I-08과의 재접속)** ← V_central vs V_tissue 구분이 TMDD에서 다시 핵심

---

## §2 — Concept Anatomy Cards

---

### 🔹 Card M1 — 이중지수 방정식과 잔차법 (Method of Residuals)

<!-- MASTER LENS -->
**[개념 Big Idea: 거장의 시각]**

1. **왜 치명적으로 중요한가:**
   IV bolus 후 plasma 농도가 semilog 평면에서 *직선이 아니라 두 직선의 합*으로 보인다는 사실 — 이 단순한 관찰을 "잡음"이 아니라 *조직 분포의 시간 지연*이라는 물리 현상으로 읽어내는 것이 2구획 분석의 출발점 전체다. R&T가 보여준 aspirin 1구획 모델 (CL=985 mL/min) vs 2구획 모델 (CL=683 mL/min) — **clearance가 30% 빗나간다.** 초기 sampling을 놓치고 1구획으로 fit하면 모든 후속 용량 계산이 30% 과소평가된다.

2. **체화해야 할 단 하나의 직관:**
   Bi-exponential은 두 개의 *다른 약물*이 같은 sample에 섞여 있는 것처럼 다뤄라. *"분율 $f_1$만큼은 빠르게 사라지는 약물 A, 분율 $f_2$만큼은 느리게 사라지는 약물 B."* 이 trick을 R&T가 명시적으로 "mathematical aid"라고 부르며 (Eq.19-13), 이 시각이 multiple dosing/infusion 행동을 모두 1구획 직관으로 환원시킨다.

3. **이 직관을 머릿속에 박고 아래를 읽어라:**
   잔차법은 곧 "두 약물 분리법"이다. 곡선의 꼬리를 외삽해서 빼면 머리만 남는다.

---

#### A. Formal Definition

IV bolus 투여 후 2구획 mammillary system의 plasma 농도-시간 곡선은 두 개의 1차 지수의 합으로 표현된다:

$$C(t) = A \cdot e^{-\alpha t} + B \cdot e^{-\beta t}, \quad \alpha > \beta > 0$$

여기서 $A, B$ (단위: 농도, e.g. mg/L)는 zero-time intercept, $\alpha, \beta$ (단위: time⁻¹)는 각각 초기·말기 phase의 1차 속도상수다. Semilog plot에서 $-\alpha$, $-\beta$가 두 phase의 기울기로 나타난다.

#### B. Derivation / Code Structure ← Vol I 도출 모드

**[잔차법(method of residuals)의 단계별 도출]:**

1. **Terminal phase 외삽**: Semilog plot에서 후기 $\beta$-phase가 직선으로 보이는 구간을 log-linear regression. $\Rightarrow B, \beta$ 획득. $-\beta$는 그 구간의 기울기. $B$는 t=0 외삽 절편.

2. **Residual concentration 계산**: 초기 phase의 각 관측 농도 $C_{\text{obs}}(t_i)$에서 외삽한 $\beta$-phase 기여 $B \cdot e^{-\beta t_i}$를 뺀다:
$$C_{\text{resid}}(t_i) = C_{\text{obs}}(t_i) - B \cdot e^{-\beta t_i}$$

3. **Residual에 다시 log-linear regression**: $\ln C_{\text{resid}}$ vs $t$가 직선이면 그 기울기가 $-\alpha$, 절편이 $A$. 만약 직선이 아니라면 → 3구획 (tri-exponential) 가능성.

4. **검증**: $C_0 = A + B$ (Eq.2:117, G&W). G&W Fig.2.43 참조 — $A \approx 70$ mg/L, $B = 28$ mg/L, $\alpha = \ln(70/10)/130 = 0.0150$ min⁻¹, $\beta = \ln(28/10)/450 = 0.00229$ min⁻¹. `[출처: Gabrielsson 5e, Ch.2, p.60, Fig.2.43]`

**핵심 secondary parameters (macro-constants 기반):**

$$AUC_0^\infty = \frac{A}{\alpha} + \frac{B}{\beta} \quad \text{[출처: G\&W Eq.2:130]}$$

$$AUMC_0^\infty = \frac{A}{\alpha^2} + \frac{B}{\beta^2} \quad \text{[출처: G\&W Eq.2:136]}$$

$$t_{1/2,\alpha} = \frac{\ln 2}{\alpha}, \quad t_{1/2,\beta} = \frac{\ln 2}{\beta}$$

**Fractional area (어느 phase가 elimination을 지배하는가):**
$$f_1 = \frac{A/\alpha}{AUC}, \quad f_2 = \frac{B/\beta}{AUC}, \quad f_1 + f_2 = 1$$

`[출처: G&W Eq.2:133-2:134; R&T Eq.19-12]`

> **Trench-level 주의:** $f_2$ (terminal phase 분율)이 1에 가까우면 → 통상적인 "elimination = terminal phase" 직관이 성립. $f_2$가 작으면 (gentamicin: $f_2 \approx 0$) → terminal phase는 *redistribution*이고, *elimination은 초기 phase에서 일어난다*. R&T가 명시한 aminoglycoside 사례. <!-- TRENCH -->

#### C. Structural Necessity

**왜 정확히 두 개의 지수합인가? 왜 sum-of-Gaussians이 아니고, 왜 1차 지수만으로 충분한가?**

2구획 mammillary system의 ODE 시스템:
$$\frac{dA_1}{dt} = -k_{12}A_1 - k_{10}A_1 + k_{21}A_2$$
$$\frac{dA_2}{dt} = +k_{12}A_1 - k_{21}A_2$$

이는 선형 상수계수 ODE 시스템이다. 행렬 형태로 쓰면:
$$\frac{d}{dt}\begin{pmatrix}A_1\\A_2\end{pmatrix} = \begin{pmatrix}-(k_{12}+k_{10}) & k_{21}\\ k_{12} & -k_{21}\end{pmatrix}\begin{pmatrix}A_1\\A_2\end{pmatrix}$$

**선형대수의 정리에 의해, $n \times n$ 선형 상수계수 ODE의 해는 정확히 $n$개의 지수항의 선형결합.** 2구획이면 정확히 두 개의 지수. 3구획이면 세 개. 이것이 "왜 bi-exponential인가"의 수학적 필연성이다. $\alpha, \beta$는 위 행렬의 두 고윳값(eigenvalue)의 음수이며, 이 성질이 Eq.2:124-2:125 ($\alpha\beta = k_{21}k_{10}$, $\alpha+\beta = k_{12}+k_{21}+k_{10}$)의 출처이기도 하다 (행렬의 trace = 고윳값 합, det = 고윳값 곱).

#### D. Assumptions & Boundary Conditions

| 가정 | 위반 시 발생하는 일 |
|---|---|
| **선형성 (linear)**: $k_{12}, k_{21}, k_{10}$이 농도 무관 상수 | Saturable elimination (MM) 또는 nonlinear binding이면 지수합 형태 자체가 깨짐 → ODE 직접 fit 필수 |
| **Mammillary 구조**: peripheral은 central 통해서만 교환 | Catenary 구조면 (예: enterohepatic recirculation) bi-exp로 fit되지 않음 |
| **Elimination from central only**: $k_{20} = 0$ | G&W Fig.2.46 model 2/3에서 보듯 — peripheral elimination 가정해도 동일한 bi-exp curve. **Plasma 데이터만으로는 구별 불가능** (구조적 비식별성, structural non-identifiability) |
| **순간적 mixing in central**: bolus 직후 $C_0 = A+B$ | 짧은 short infusion에서는 위반 → C_max 낮아짐 (R&T Fig.19-7 midazolam 사례) |
| **Sampling이 distribution phase를 포착**: 첫 sampling이 $\alpha$-phase 안에 있어야 | 후기 sampling만 있으면 1구획으로 오인 → $V_d$ underestimate, $CL$ overestimate (aspirin: 985 → 683 mL/min, 30% overestimate `[출처: R&T 5e, Ch.19, p.620]`) |

#### E. Limitations

- **Bi-exp는 두 개의 시간 스케일만 분리.** 실제로 3개 phase가 있으면 ($\gamma$-phase 존재) tri-exp가 필요. G&W §2.4.4 Fig.2.52에서 infusion 후 3-exp decline 사례 제시.
- **잔차법은 sampling design에 매우 민감.** $\beta$-phase 외삽이 부정확하면 $A$ 추정이 연쇄 편향. 이 때문에 nonlinear regression이 NCA보다 안정적.
- **Bi-exp는 plasma 농도만 표현 — peripheral 조직의 농도 추적 불가.** Fig.2.42에서 peripheral compartment는 농도가 0에서 시작해 peak를 거쳐 declining하는 unimodal curve지만, plasma만 보면 알 수 없다.

#### F. Five Cognitive Layers

| Layer | 내용 |
|---|---|
| **L1 형식적 수학** | Bi-exp는 $2 \times 2$ 선형 ODE의 fundamental solution. $\alpha, \beta$ = system matrix의 고윳값(부호반전). $A, B$ = 초기조건과 고유벡터로부터 결정. |
| **L2 기하학적 직관** | Semilog plot에서 곡선의 *곡률 변화점(knee)* 의 위치가 $\alpha/\beta$ 비율을 반영. 두 phase의 기울기 차이가 클수록 knee가 뚜렷. |
| **L3 구조적 동일성** | 방사능 핵종 붕괴 사슬 (parent-daughter), RC 회로 두 단계 캐스케이드, 두 단계 화학반응 평형도달 — 모두 같은 형태의 ODE → 같은 bi-exp 해. |
| **L4 생리학적 의미** | $\alpha$-phase: plasma + 빠르게 평형화하는 장기(간·신·폐·심). $\beta$-phase: 느리게 평형화하는 조직(근육·지방·골수)으로의 redistribution + 동시적 elimination. R&T Fig.19-1 thiopental: liver는 5분 내 plasma와 평형, fat는 3시간에도 미평형. |
| **L5 실무 투영** | NONMEM `$SUBROUTINES ADVAN3 TRANS3` (parameters: CL, V, Q, VSS) 또는 `ADVAN3 TRANS4` (CL, V1, Q, V2). 잔차법 직접 코딩은 불필요 — `$ESTIMATION METHOD=COND`가 자동으로 fit. 그러나 *$THETA initial estimate*는 잔차법으로 손계산해서 넣어야 수렴. |

#### G. Zettelkasten Atom

```yaml
---
aliases: [이중지수, bi-exponential, method of residuals, curve stripping]
tags: [pharmacometrics/pk/2-compartment, nonmem/advan3]
up: "[[2-Compartment Model MOC]]"
related: ["[[Method of Residuals]]", "[[Macro Constants A α B β]]", "[[NONMEM ADVAN3]]"]
source: "Gabrielsson 5e Ch.2 §2.4.2 / R&T 5e Ch.19"
---

IV bolus 후 plasma 농도가 semilog 평면에서 두 직선의 합으로 보일 때, 그 곡선은 2×2 선형 ODE의 해이며 정확히 두 개의 지수합으로 표현된다. 잔차법은 terminal phase를 외삽해 빼고 남은 residual을 다시 log-linear fit해서 초기 phase parameter를 분리하는 *조작 절차*다. 핵심 secondary parameters AUC = A/α + B/β, AUMC = A/α² + B/β². fractional area f₁, f₂가 어느 phase가 elimination을 지배하는지 결정 — gentamicin은 f₂≈0이라 terminal phase가 elimination이 *아니다*.
```

---

### 🔹 Card M2 — Macro ↔ Micro ↔ Physiological 3중 좌표계 변환

<!-- ANCHOR -->
앞 카드에서 분리한 4개 macro-constant ($A, \alpha, B, \beta$) 그 자체는 *측정량의 곡선 모수*일 뿐이다. 이를 *생리학적으로 해석 가능한* 양 ($CL, V_c, Cl_d, V_t$) 또는 *NONMEM 내부가 다루는* 양 ($k_{10}, k_{12}, k_{21}, V_c$)으로 변환해야 비로소 약물 행동을 예측할 수 있다.

<!-- MASTER LENS -->
**[개념 Big Idea: 거장의 시각]**

1. **왜 치명적으로 중요한가:**
   NONMEM의 `$SUBROUTINES ADVAN3 TRANS3` vs `TRANS4` 선택은 단순한 syntactic 선택이 아니다. **TRANS3는 (CL, V, Q, VSS)를, TRANS4는 (CL, V1, Q, V2)를 estimate**한다. 이 두 좌표계는 동일한 모델을 표현하지만 *parameter 간 상관성*이 다르다. 잘못된 좌표계 선택은 `$COV step` 실패의 직접 원인이다.

2. **체화해야 할 단 하나의 직관:**
   *"세 좌표계는 같은 약물 행동을 보는 세 개의 카메라 — Macro는 곡선이 보이는 모양 그대로, Micro는 ODE의 흐름을 그대로, Physiological은 임상의가 해석하는 그대로."* 셋은 정보량이 동일하지만 *축이 회전된* 형태일 뿐이다. NONMEM은 임의의 회전을 좋아하지 않는다 — 가장 *덜 상관된* 축을 선택하라.

3. **이 직관을 머릿속에 박고 아래를 읽어라:**
   변환식들은 단순한 algebra가 아니라 *축 회전 행렬의 각 성분*이다.

---

#### A. Formal Definition

**세 가지 동등한 (information-equivalent) 파라미터 집합:**

| 좌표계 | 파라미터 | 갯수 | 단위 차원 |
|---|---|---|---|
| **Macro** | $A, \alpha, B, \beta$ | 4 | (농도, t⁻¹, 농도, t⁻¹) |
| **Micro** | $V_c, k_{10}, k_{12}, k_{21}$ | 4 | (volume, t⁻¹, t⁻¹, t⁻¹) |
| **Physiological** | $V_c, CL, Cl_d, V_t$ | 4 | (volume, vol/t, vol/t, volume) |

#### B. Derivation / Code Structure

**[Macro → Micro 변환 (G&W Eq.2:121–2:128)]:**

$$A = \frac{D_{iv}}{V_c} \cdot \frac{\alpha - k_{21}}{\alpha - \beta}, \quad B = \frac{D_{iv}}{V_c} \cdot \frac{\beta - k_{21}}{\beta - \alpha} \quad \text{[출처: G\&W Eq.2:121-2:122]}$$

역방향:
$$V_c = \frac{D_{iv}}{A + B} \quad \text{[Eq.2:129]}$$

$$k_{21} = \frac{A\beta + B\alpha}{A + B} \quad \text{[Eq.2:128]}$$

$$k_{10} = \frac{\alpha\beta}{k_{21}} \quad \text{[Eq.2:126]}$$

$$k_{12} = \alpha + \beta - k_{21} - k_{10} \quad \text{[Eq.2:127]}$$

**[Micro → Physiological 변환]:**

$$CL = k_{10} \cdot V_c$$

$$Cl_d = k_{12} \cdot V_c = k_{21} \cdot V_t \quad \text{[Eq.2:120, G\&W; Eq.2:158, R\&T]}$$

따라서:
$$V_t = \frac{Cl_d}{k_{21}} = V_c \cdot \frac{k_{12}}{k_{21}}$$

**[NONMEM 구현 — Physiological 좌표계가 표준]:**

```fortran
$SUBROUTINES ADVAN3 TRANS4
$PK
   CL  = THETA(1)*EXP(ETA(1))   ; 청소율 (central elim only 가정)
   V1  = THETA(2)*EXP(ETA(2))   ; 중앙구획 용적 = V_c
   Q   = THETA(3)*EXP(ETA(3))   ; intercompartmental clearance = Cl_d
   V2  = THETA(4)*EXP(ETA(4))   ; 말초구획 용적 = V_t
   K   = CL/V1
   K12 = Q/V1
   K21 = Q/V2
   S1  = V1                     ; concentration scaling
```

`[출처: NONMEM ADVAN3 TRANS4 표준 코드 패턴 — NONMEM 7.x manual]`

> **Trench-level 주의:** TRANS3 (CL, V, Q, VSS)와 TRANS4 (CL, V1, Q, V2)는 동일한 모델이지만 TRANS3가 "VSS = V1 + V2"를 직접 estimate해서 V1과 VSS의 상관이 V1과 V2보다 보통 더 낮다 → `$COV step` 안정. TRANS4는 V1과 V2 둘 다 작을 때 두 양이 강하게 상관될 수 있다. 실무에서는 TRANS4 시작 → 수렴 안되면 TRANS3 전환이 합리적. <!-- TRENCH -->

#### C. Structural Necessity

**왜 정확히 4개 파라미터로 충분한가? 왜 더 많지도, 적지도 않은가?**

2구획 mammillary system은 4개의 자유도를 가진다: $V_c, V_t, k_{10}, k_{12}$ (혹은 $k_{21}$). G&W Fig.2.46이 보여주듯, 같은 bi-exp curve를 만드는 세 가지 *구조적으로 다른* 2구획 모델이 존재한다 (model 1: central elim only; model 2: peripheral elim only; model 3: both). **plasma 데이터만으로는 이 셋이 구조적으로 비식별(structurally non-identifiable)이다.** 따라서 우리는 통상 model 1 (central elim only)을 *가정*하고 4개 파라미터를 fit한다 — 이것이 4개로 충분한 이유, 동시에 4개가 *최소*인 이유.

#### C-2. *(C-2 Plausible Fallacy는 본 카드 아닌 M3 Apex 카드에서 다룸)*

#### D. Assumptions & Boundary Conditions

- **모든 변환식은 elimination이 central에서만 일어난다는 가정 위에 성립.** 이 가정이 깨지면 (peripheral elim 존재) Macro→Micro 매핑이 underdetermined → tissue sampling 필요.
- **Linear 가정.** 농도 의존성이 있으면 $k_{10}$이 $C$의 함수가 되어 변환식 자체가 시간 종속.
- **3구획 이상으로 확장 시:** Macro→Micro 변환은 closed-form이 사라지고 numerical eigenvalue 분해로만 가능 → ADVAN5/ADVAN6/ADVAN13 직접 ODE 사용 필요 (Session II-04 참조).

#### E. Limitations

- **3개 좌표계가 동등하지만, NONMEM의 수치적 안정성에는 큰 차이.** Macro 좌표계로 직접 fit하면 (`A, ALPHA, B, BETA`) 약물 정보로 자연스러운 prior가 만들어지지 않아 보통 condition number가 폭증한다. Physiological 좌표계가 covariate modeling에 가장 적합 — *왜냐하면 CL과 V는 체중·신기능·간기능 등 covariate와 직접적인 메커니즘 연결이 있기 때문이다.*

#### F. Five Cognitive Layers

| Layer | 내용 |
|---|---|
| **L1** | $\alpha, \beta$는 system matrix의 두 고윳값. $\alpha + \beta = k_{12}+k_{21}+k_{10}$ (trace), $\alpha\beta = k_{21}k_{10}$ (det). |
| **L2** | 4차원 parameter 공간에서 세 좌표계는 *동일 manifold*의 서로 다른 chart. NONMEM의 OFV gradient가 어느 chart에서 더 잘 정의되는지가 수치 안정성을 결정. |
| **L3** | 좌표 변환은 본질적으로 좌표 자코비안 행렬 — 회로이론의 admittance vs impedance, 양자역학의 position vs momentum representation과 동형. |
| **L4** | $CL$ = 간/신 청소 능력의 합 (생리학적). $Cl_d$ = 조직 관류·확산·능동수송의 합 (혈류와 같은 단위). $V_t$ = 조직 분포 용적 (Kp·V_T 합). $k_{12}, k_{21}$ 자체는 *unphysical*. |
| **L5** | 좌표계 선택 = NONMEM `$PK` 블록의 첫 줄. ADVAN3 TRANS4 (`CL, V1, Q, V2`)가 covariate 모델링 표준. 한국 PIPET 교재에서도 동일한 컨벤션. |

#### G. Zettelkasten Atom

```yaml
---
aliases: [parameter conversion, reparameterization, ADVAN3 TRANS4, coordinate change]
tags: [pharmacometrics/pk/2-compartment, nonmem/advan3, nonmem/parameterization]
up: "[[2-Compartment Model MOC]]"
related: ["[[Macro Constants]]", "[[Micro Constants k12 k21 k10]]", "[[Physiological CL V Q]]", "[[Condition Number $COV]]"]
source: "G&W Eq.2:120-2:129 / R&T Table 19-1"
---

2구획 모델은 4개 자유도를 가지며 Macro/Micro/Physiological 세 좌표계로 동등하게 표현 가능하다. 변환식 (k21 = (Aβ+Bα)/(A+B), CL = k10·Vc 등)은 algebra가 아니라 좌표 자코비안의 성분이다. NONMEM의 수치 안정성은 어느 좌표계를 estimation 변수로 삼느냐에 강하게 의존한다 — Physiological이 covariate 모델링 표준. 반드시 elimination from central only 가정 위에서만 모든 변환식이 성립.
```

> **CONTEXT (1문장 처리):** $MRT = AUMC/AUC$ (Eq.2:138)는 1구획에서 이미 학습한 noncompartmental 결과이며, 2구획에서도 동일한 정의가 유지되되 $V_{ss} = MRT \cdot CL$ (Eq.2:164)로 *분포 정보를 별도로 추출*하는 도구가 된다.

---

### 🔹 Card M3 — V₁ / Vss / Vβ — 분포용적 3중 체계 [⚡ Apex Concept]

<!-- ANCHOR -->
앞 카드에서 본 좌표계 변환의 *가장 위험한 분기점*이 바로 분포용적이다. 2구획에서는 *세 개*의 분포용적이 등장하며 — 이 셋의 차이를 무시하고 하나의 "$V$"로 다루는 순간 임상 결정과 규제 제출이 무너진다.

[⚡ **Apex Concept**] — 본 세션에서 가장 난해하고 임상·규제 파급력이 큰 단 하나의 카드.

<!-- MASTER LENS -->
**[개념 Big Idea: 거장의 시각]**

1. **왜 치명적으로 중요한가:**
   R&T가 직접 *"terminal half-life ceases to have simple application"*이라고 경고한 이유의 핵심이 여기에 있다. R&T 데이터: aspirin (V=13.7L vs Vss=10.4L, 32% 차이), salicylic acid (V=10.5L vs Vss=10.2L, 거의 동일), gentamicin (**V=345L vs Vss=56L, 6배 차이!**). 신부전 환자에서 gentamicin 용량을 Vβ 기준으로 조정하면 신독성과 약효부전을 *동시에* 발생시킬 수 있다. NDA 제출에서 "어느 V로 분포 변동을 보고했는가"가 Deficiency Letter 직접 사유.

2. **체화해야 할 단 하나의 직관:**
   *"Vss는 약물이 모든 조직과 평형을 이루었을 때의 진짜 배포 부피 — 형광등이 켜진 방의 실제 크기. Vβ는 terminal phase에서 plasma 농도 하락이 distribution 평형보다 빠른 elimination 때문에 부풀려진 가짜 부피 — 빛이 방 밖으로 너무 빨리 빠져나가서 실제보다 큰 방으로 보이는 착시. Elimination이 distribution보다 빠를수록 착시가 커진다."* Aspirin은 잠깐의 착시(32%), gentamicin은 거대한 착시(6배).

3. **이 직관을 머릿속에 박고 아래를 읽어라:**
   $V_\beta = V_{ss} \times (\text{착시 보정계수})$, 보정계수는 elimination/distribution 속도 비.

---

#### A. Formal Definition

| 부피 | 정의 | 측정 시점 |
|---|---|---|
| **$V_1$ (= $V_c$, initial dilution volume)** | $V_1 = \dfrac{\text{Dose}}{A+B} = \dfrac{D_{iv}}{C_0}$ | t=0 직후 (mixing은 끝났으나 distribution은 시작 전) |
| **$V_{ss}$ (volume of distribution at steady state)** | $V_{ss} = MRT \cdot CL = \dfrac{V_1 \cdot k_{12} + V_t \cdot k_{21}}{...} = V_1 \cdot \left(1 + \dfrac{k_{12}}{k_{21}}\right)$ | 가상의 *완전 평형* 상태 (constant-rate infusion으로 도달 가능) |
| **$V_\beta$ (= $V$, $V_z$, volume during terminal phase)** | $V_\beta = \dfrac{CL}{\beta} = \dfrac{D_{iv}}{AUC \cdot \beta}$ | terminal phase 중 (pseudo-equilibrium, but elimination ongoing) |

`[출처: G&W Eq.2:140-2:142, Eq.2:164; R&T Table 19-1]`

#### B. Derivation / Code Structure

**[$V_{ss}$의 도출 — 본질은 "elimination이 없다고 가정한 분포 공간"]:**

Steady state에서 net flux는 0:
$$k_{12} A_{1,ss} = k_{21} A_{2,ss}$$
$$\Rightarrow A_{2,ss} = \frac{k_{12}}{k_{21}} A_{1,ss}$$

$$A_{ss,total} = A_{1,ss} + A_{2,ss} = V_1 \cdot C_{ss} \cdot \left(1 + \frac{k_{12}}{k_{21}}\right)$$

$$V_{ss} = V_1 \cdot \left(1 + \frac{k_{12}}{k_{21}}\right) \quad \text{[출처: G\&W Eq.2:141 / R\&T Eq.19-18]}$$

물리적 해석: $V_{ss} = V_1 + V_t \cdot (k_{12} V_1)/(k_{21} V_t) = V_1 + V_t$ (만약 partition coefficient가 1이면). 정확히 *central + peripheral*의 진짜 부피.

**[$V_\beta$의 도출 — 본질은 "elimination이 분포평형을 빠르게 만들 때의 착시"]:**

Terminal phase에서:
$$C(t) = B \cdot e^{-\beta t}, \quad A_{body}(t) = V_\beta \cdot C(t)$$

총 *남아있는 amount to be eliminated*는 $CL \cdot AUC_{terminal} = CL \cdot B/\beta$.
이것이 곧 terminal phase 시작 시점의 body amount $V_\beta \cdot B$.
$$V_\beta \cdot B = CL \cdot \frac{B}{\beta} \Rightarrow V_\beta = \frac{CL}{\beta} \quad \text{[출처: R\&T Eq.19-11]}$$

**핵심 부등식 (R&T Fig.19-9):**
$$V_1 \leq V_{ss} \leq V_\beta$$

등호는 elimination이 distribution보다 *훨씬 느릴 때만* (즉 $f_2 \approx 1$일 때 $V_{ss} \approx V_\beta$).

**Closed-form via macro-constants:**

$$V_{ss} = D_{iv} \cdot \frac{(C_1/\lambda_1^2 + C_2/\lambda_2^2)}{(C_1/\lambda_1 + C_2/\lambda_2)^2} = \text{Dose} \cdot \frac{AUMC}{AUC^2} \quad \text{[출처: R\&T Table 19-1]}$$

$$V_\beta = \frac{\text{Dose}}{AUC \cdot \beta}$$

#### C. Structural Necessity

**왜 셋이 일반적으로 다른가?**
- $V_1$과 $V_{ss}$가 다른 이유: Distribution이 *시간을 요구*하기 때문. $V_1$은 t=0 직후, $V_{ss}$는 t→∞.
- $V_{ss}$와 $V_\beta$가 다른 이유: Terminal phase에서도 plasma가 tissue를 *완전히* 따라잡지 못함. Tissue 농도가 plasma보다 높은 채로 두 phase가 평행 하강. 이 *gap*이 apparent volume을 부풀린다 (R&T Fig.19-9B).

**왜 fast elimination이 $V_\beta$를 부풀리는가?**

Tissue → plasma redistribution이 천천히 진행되는 동안 elimination이 plasma 농도를 빠르게 끌어내림 → tissue/plasma 비율이 *진짜 평형값보다 높게* 유지 → apparent $K_p$ (그리고 $V_\beta = V_p + K_{p,app} \cdot V_T$)가 부풀려짐.

#### C-2. 🔴 [Plausible Fallacy] (Apex 카드 전용)

**그럴싸한 오류 (초보 모델러가 가장 자주 저지르는):**

> *"Vβ는 terminal phase 직접 측정에서 가장 신뢰성 있게 추출되니까, NONMEM에서 V (= V_β)로 parameterize하면 가장 robust할 것이다. 그리고 어차피 V와 Vss는 비슷하잖아."*

**오류의 구체적 형태:**
1. NONMEM `$PK`에서 `V = THETA(2)*EXP(ETA(2))`로 둠 (즉 $V_\beta$를 직접 estimate)
2. Covariate 모델에서 "체중→V 관계"를 fitting (그러나 *체중이 영향 주는 것은 $V_{ss}$ 또는 $V_t$이지 $V_\beta$가 아니다*)

**이 오류가 NONMEM/임상에 미치는 나비효과 (기계론적 추적):**

`Vβ를 직접 estimate` → `Vβ = CL/β` 관계를 NONMEM이 모름 → CL과 Vβ 사이에 *내재된 강한 positive 상관* 발생 → `$OMEGA` block이 거의 singular → `$COV step` 실패 → RSE > 50% → covariate effect *전부 부정확* → Phase 3 dose selection이 **6배(gentamicin 사례)까지 빗나갈 수 있음**.

특히 신부전 환자에서: 신부전 → CL 감소 → β도 감소 → $V_\beta = CL/\beta$가 *거의 변하지 않음*. 그래서 신부전이 "분포에 영향을 안 준다"는 *잘못된 결론*. 사실은 $V_{ss}$는 진짜 변하지 않는데, $V_\beta$ 측정이 그 사실을 *우연히* 맞춘 것뿐. 그러나 *축적*에 대한 예측 (신부전 환자에서 정상 다회투여 시 plasma vs tissue 농도)은 $V_\beta$로 계산하면 완전히 빗나간다.

**GOF 시그니처 패턴 (이 오류를 발견하는 진단 시그니처) — *"Pseudo-Stable Volume Across Renal Function"*:**

신기능을 covariate로 한 visual predictive check (VPC)에서:
- $V_\beta$ vs CrCl plot이 *거의 평탄* → "분포에 신기능 영향 없음"으로 잘못 해석
- 그러나 동일 환자에서 multiple-dose plasma trough VPC가 신부전군에서 *systematic underprediction* (실제 trough가 모델 예측보다 높음)
- 이 두 패턴의 *공존*이 시그니처: $V_\beta$를 모델 변수로 잘못 채택했음을 시사

**해결 방향:** Always parameterize as $V_c, V_t, CL, Cl_d$ (i.e. ADVAN3 TRANS4), and report $V_{ss}$ as derived secondary parameter. NDA submission에서도 $V_{ss}$ 보고가 표준 (FDA Population PK Guidance).

---

#### D. Assumptions & Boundary Conditions

- **$V_{ss}$의 정의는 *no-elimination* idealization.** 실제로 elimination이 항상 있으므로 $V_{ss}$는 *간접* 계산 (MRT·CL, 또는 Eq.2:140).
- **$V_\beta$ 계산은 sampling이 진정한 terminal phase까지 도달했음을 가정.** $\gamma$-phase가 숨어있으면 $V_\beta$ overestimate.
- **$V_1$ 의 측정은 첫 sample이 mixing 완료 직후.** Short infusion이면 $V_1$ 추정이 부풀려짐.

#### E. Limitations

- **$V_\beta$의 임상적 직접 효용은 거의 없다.** "Terminal phase에서 농도 X일 때 body amount는 얼마인가"의 질문에만 답한다.
- **$V_{ss}$만이 covariate 분석에서 의미 있는 분포 측정.**
- **Gentamicin같이 $V_\beta \gg V_{ss}$인 약물에서, terminal half-life $t_{1/2,\beta}$도 elimination half-life가 *아니다*** — *redistribution half-life*다. Aminoglycoside 신독성/이독성의 측정에 plasma trough가 둔감한 이유.

#### F. Five Cognitive Layers

| Layer | 내용 |
|---|---|
| **L1** | $V_{ss} = MRT \cdot CL$ (NCA), $V_\beta = CL/\beta$, $V_1 = D_{iv}/C_0$. 부등식 $V_1 \leq V_{ss} \leq V_\beta$ 항상 성립. |
| **L2** | R&T Fig.19-4B에서 보듯 "효과적 분포용적 $A/C$"는 시간에 따라 $V_1$에서 $V_\beta$로 monotonic 증가하는 곡선이다. $V_{ss}$는 그 곡선의 *limit*이지만 항상 도달하지는 않는다. |
| **L3** | $V_\beta - V_{ss}$ 은 *non-equilibrium gap의 정량* — 열역학에서 "비평형 상태가 실효 부피를 부풀리는" 현상과 동형. |
| **L4** | $V_{ss}$는 약물의 *조직 친화도*만 반영. $V_\beta$는 *조직 친화도 + 소실 속도/분포 속도 비*를 동시에 반영. 그래서 $V_\beta$는 elimination에 *오염된* 측정. |
| **L5** | NONMEM TRANS4: V1, V2 ← Vc, Vt에 대응. TRANS3: V, VSS ← Vβ, Vss에 대응. **Covariate model에서는 TRANS4 + Vss derived가 표준.** |

#### G. Zettelkasten Atom

```yaml
---
aliases: [Vss, Vbeta, Vz, V1, central volume, steady-state volume of distribution, terminal phase volume]
tags: [pharmacometrics/pk/2-compartment, pharmacometrics/distribution-volume, regulatory/popPK]
up: "[[2-Compartment Model MOC]]"
related: ["[[V1 Initial Dilution Volume]]", "[[Vss True Distribution]]", "[[Vbeta Apparent]]", "[[Terminal Half-life Trap]]"]
source: "G&W Eq.2:140-2:142 / R&T Ch.19 p.620-630, Table 19-1"
---

2구획에서 분포용적은 셋이며 일반적으로 V1 < Vss ≤ Vβ. Vss는 elimination이 없다고 가정한 진짜 평형 부피(MRT·CL), Vβ는 terminal phase의 apparent volume(CL/β). 차이는 elimination/distribution 속도 비에서 오는 *비평형 gap*. Aspirin은 작은 차이(32%), gentamicin은 6배. NONMEM은 ADVAN3 TRANS4로 Vc·Vt를 estimate하고 Vss는 derived로 보고하는 것이 표준 — Vβ 직접 estimate는 CL과의 내재 상관으로 $COV step 실패 사유. 신부전에서 Vβ는 거의 변하지 않으나 이는 *우연*이며 분포 자체가 변하지 않음의 증거가 아니다.
```

---

### 🔹 Card M4 — 재파라미터화 5종과 Condition Number

<!-- ANCHOR -->
지금까지 macro·micro·physiological 세 좌표계를 봤다. G&W는 여기에 두 가지 *시간 의존 부피* 모델 (Takada, Colburn)을 추가해 *5종 재파라미터화*를 제시한다. PK8 케이스 스터디는 이 다섯이 동일 데이터에 어떻게 다른 수치적 행동을 보이는지를 정량적으로 보여준다.

<!-- MASTER LENS -->
**[개념 Big Idea: 거장의 시각]**

1. **왜 치명적으로 중요한가:**
   G&W PK8 Table 8.1 — 동일한 100 µg IV bolus 데이터에 5종 모델을 fit. WRSS는 0.0169 ~ 0.0437 사이로 *비슷*. 그러나 **condition number는 29.69 ~ 4,104 사이로 200배 진폭**. NONMEM에서 condition number > 1,000은 보통 `$COV step` 경고/실패의 임계값 — 즉, *데이터에 거의 동등하게 잘 fit되는 모델 중 하나는 covariance 추정 가능, 나머지는 불가능하다.* 좌표계 선택이 곧 model qualification을 결정한다.

2. **체화해야 할 단 하나의 직관:**
   *"Goodness-of-fit (WRSS, OFV)는 모델이 데이터에 얼마나 잘 맞는가만 본다. Condition number는 추정된 파라미터들이 서로 얼마나 헷갈리지 않는가를 본다. 좋은 fit + 나쁜 condition number = 답은 맞지만 답을 어떻게 알았는지는 알 수 없는 모델."*

3. **이 직관을 머릿속에 박고 아래를 읽어라:**
   재파라미터화 선택은 좌표 회전을 통해 *parameter 간 정보 충돌을 줄이는* 작업이다.

---

#### A. Formal Definition

**Condition number (NONMEM 출력의 `Eigenvalue Ratio`):**
$$\kappa = \frac{\lambda_{\max}(I^{-1})}{\lambda_{\min}(I^{-1})} = \frac{\lambda_{\max}(\text{Cov matrix})}{\lambda_{\min}(\text{Cov matrix})}$$

(여기서 $I$는 Fisher information matrix, $\lambda$는 고윳값.)

**해석:** $\kappa$는 covariance matrix의 가장 긴 축과 가장 짧은 축의 비. 큰 $\kappa$ = parameter들이 서로 강하게 상관 = *어느 한 방향으로는 데이터가 정보를 거의 안 줌* = practical non-identifiability.

#### B. Derivation / Code Structure

**[5종 재파라미터화 — G&W Table 2.6 + PK8 Table 8.1]:**

| # | 모델 | 추정 파라미터 | PK8 WRSS | PK8 Cond. No. |
|---|---|---|---|---|
| 1 | **Macro (bi-exp)** | $A, \alpha, B, \beta$ | 0.0437 | **125.2** |
| 2 | **Takada** | $V_c, \beta, V_{max}, K_d$ | 0.0169 | 3,186 |
| 3 | **Colburn** | $V_c, \beta, V_{max}, K_v$ | 0.0294 | 2,243 |
| 4 | **Reparameterized $Cl$-model** | $CL, \alpha, B, \beta$ | 0.0435 | 2,306 |
| 5 | **Differential equation (ODE)** | $V_c, CL, Cl_d, V_t$ | 0.0436 | **29.69** |

`[출처: G&W 5e Ch.7 Table 8.1 (PK8 case study)]`

**Takada 모델 (시간 의존 부피, hyperbolic):**
$$C = \frac{D_{iv}}{V_c + V_t} \cdot e^{-\beta t}, \quad V_t = \frac{V_{max} \cdot t}{K_d + t} \quad \text{[Eq.2:150-2:151]}$$

**Colburn 모델 (시간 의존 부피, exponential):**
$$C = \frac{D_{iv}}{V_c + V_t} \cdot e^{-\beta t}, \quad V_t = V_{max}(1 - e^{-K_v t}) \quad \text{[Eq.2:152-2:153]}$$

**Reparameterized $Cl$-model (G&W Eq.2:148-2:149):**
$$A = \alpha \cdot \left(\frac{D_{iv}}{CL} - \frac{B}{\beta}\right)$$
$$C = \alpha \cdot \left(\frac{D_{iv}}{CL} - \frac{B}{\beta}\right) \cdot e^{-\alpha t} + B \cdot e^{-\beta t}$$

(이는 Macro 모델에서 $A$를 $CL$로 *대체*한 4-parameter 모델.)

**ODE 모델:** Eq.2:159-2:160 (Card M2 NONMEM 코드와 동일).

> **Trench-level 통찰:** PK8에서 ODE 모델의 condition number(29.69)가 macro 모델(125.2)보다도 *낮다.* 이는 ODE 좌표계 ($V_c, CL, Cl_d, V_t$)에서 parameter들의 정보 직교성이 가장 좋다는 것 — *왜냐하면 각 파라미터가 ODE의 서로 다른 항에 등장하기 때문*. Macro에서는 $A$가 $\alpha, \beta$ 모두와 얽혀있다. <!-- TRENCH -->

#### C. Structural Necessity

**왜 ODE 모델이 condition number 측면에서 가장 우수한가?**

5종 모델은 모두 동일한 4-자유도 정보를 표현하지만, *parameter가 OFV gradient에 들어가는 방식*이 다르다.

- ODE 모델 ($V_c, CL, Cl_d, V_t$): 각 parameter가 ODE 시스템의 *독립적인 항*에 단일하게 등장. Fisher information matrix에서 off-diagonal이 작음. → $\kappa$ 작음.
- Takada/Colburn: $V_t$가 시간 함수 자체를 통해 모든 시점의 농도에 *비선형으로* 영향. Parameter 간 상관이 본질적. → $\kappa$ 큼.
- Reparameterized $Cl$-model: $A$가 $CL, \alpha, B, \beta$ 모두의 함수로 *암묵적으로* 정의됨. → $\kappa$ 큼.

#### D. Assumptions & Boundary Conditions

- Takada/Colburn 모델은 *peripheral compartment를 명시적으로 모델링하지 않음.* 대신 "central 부피가 시간에 따라 부풀어 오른다"는 phenomenological 묘사. PBPK 해석이나 covariate modeling에는 부적합.
- ODE 모델은 *항상* mammillary 가정 + central elim only 가정 위에서.

#### E. Limitations

- **Condition number만으로 모델을 평가하면 안 된다.** WRSS/OFV/AIC/잔차 패턴 + bootstrap RSE + VPC를 함께 봐야. Takada는 PK8에서 WRSS 최소 + 잔차 random scatter — 모델 *적합도*는 우수. 그러나 covariance 추정 불안정.
- **ODE 모델의 condition number 우위는 *해당 데이터/parametrization*에서만 보장.** 일반론은 아님. Sparse data에서는 ODE 모델도 condition number 폭증 가능.

#### F. Five Cognitive Layers

| Layer | 내용 |
|---|---|
| **L1** | $\kappa = \lambda_{\max}/\lambda_{\min}$. Information matrix의 spectral 성질이 parameterization에 강하게 의존. |
| **L2** | OFV 등고선이 parameter 공간에서 *길고 좁은 valley*면 큰 $\kappa$. *원형*에 가까우면 작은 $\kappa$. 좌표 회전으로 valley 방향을 축에 align할 수 있다면 $\kappa$ 감소. |
| **L3** | 좌표 변환으로 conditioning을 개선하는 것은 numerical linear algebra의 *preconditioning* 기법과 동형. |
| **L4** | Physiological parameters ($CL, V_c, Cl_d, V_t$)는 서로 다른 *생리 메커니즘*에 매핑되어 있어 자연스럽게 정보 직교. |
| **L5** | NONMEM 출력에서 `CONDITION NUMBER` 또는 `EIGENVALUE RATIO` 확인 → 1000 초과 시 좌표계 변경 + initial estimates 재검토 + boundary 점검. PIPET 한국어 교재에서도 동일 임계값. |

#### G. Zettelkasten Atom

```yaml
---
aliases: [reparameterization, condition number, parameter identifiability, $COV step]
tags: [pharmacometrics/nonmem/numerics, pharmacometrics/popPK/qualification]
up: "[[Model Qualification MOC]]"
related: ["[[$COV Step Failure]]", "[[Fisher Information Matrix]]", "[[ADVAN3 TRANS4]]"]
source: "G&W 5e PK8 Table 8.1 / NONMEM 7.x manual"
---

2구획 모델은 5종 이상의 동등한 재파라미터화가 가능하며 (Macro/Micro/Physiological/Takada/Colburn), 동일 데이터에 fit되어도 condition number가 200배 차이날 수 있다. PK8 사례: ODE physiological(29.69) << Macro(125.2) << Reparam-Cl(2,306) ≈ Colburn(2,243) << Takada(3,186). Condition number는 parameter 간 정보 직교성의 척도이며 NONMEM $COV step 안정성의 직접적 결정자. ODE physiological은 각 parameter가 서로 다른 ODE 항에 등장하기 때문에 가장 자연스러운 직교성을 가진다.
```

---

### 🔹 Card M5 — 분포속도론의 임상 파급 + Terminal Half-life의 함정

<!-- ANCHOR -->
앞 4개 카드가 *모델 내부* 의 수학·수치 안정성을 다뤘다면, 이 마지막 카드는 그 모든 것이 *왜 환자 옆에서 중요한가*를 다룬다. R&T Ch.19의 핵심 메시지가 여기에 응축된다: **terminal half-life는 elimination half-life가 아니다.**

<!-- MASTER LENS -->
**[개념 Big Idea: 거장의 시각]**

1. **왜 치명적으로 중요한가:**
   "Terminal half-life = 50% Css 도달 시간 = 5×t½에 plateau 도달" — *이 1구획 직관이 2구획에서 통째로 무너진다.* R&T가 nicardipine으로 보여준 충격 사례: terminal t½ = 12 hr인데 *50% Css 도달은 1 hr*. 거꾸로 gentamicin은 terminal t½ = 87 hr이지만 plasma는 약 4 hr 반감기로 사라진다. 임상의가 1구획 직관으로 dosing interval을 정하면 *항상* 빗나간다.

2. **체화해야 할 단 하나의 직관:**
   *"Plasma 농도가 plateau에 도달하는 시간은 terminal half-life가 아니라 $f_2$ 가중 half-life다."* $f_2$가 0에 가까우면 ($\alpha$-phase가 elimination 지배) plasma는 *초기 phase의 half-life*로 plateau 도달. $f_2$가 1에 가까우면 ($\beta$-phase가 elimination 지배) terminal half-life가 plateau 결정. R&T Fig.19-11이 이 광경 전체를 한 그림에 압축.

3. **이 직관을 머릿속에 박고 아래를 읽어라:**
   "어느 phase가 elimination을 지배하는가?"가 모든 임상 결정의 분기점.

---

#### A. Formal Definition

**Plateau 도달 식 (Eq.19-26, R&T):**
$$\frac{C(t)}{C_{ss}} = f_1 \cdot (1 - e^{-\alpha t}) + f_2 \cdot (1 - e^{-\beta t})$$

여기서 $f_1, f_2$는 fractional area: $f_1 = (A/\alpha)/AUC$, $f_2 = (B/\beta)/AUC$, $f_1 + f_2 = 1$.

**Effective half-life (Eq.2:139, G&W):**
$$t_{1/2,e} = \ln(2) \cdot MRT$$

이것이 진정한 "elimination 본위의 half-life" — bolus 후 평균 분자가 체내에 머무는 시간.

**다회투여 축적 지수 (gentamicin 사례):**
$$\text{Accumulation index for terminal phase} = \frac{1}{1 - e^{-\beta \tau}}$$

R&T 사례: gentamicin τ=8hr, β-phase t½=87hr → 축적 지수 = 16. 그러나 *plasma trough*는 16배 축적되지 *않는다* — 왜냐하면 plasma는 $\alpha$-phase가 지배하므로 ($f_2 \approx 0$) 거의 축적 안됨. Tissue (slowly equilibrating pool)가 진짜 16배 축적의 무대.

#### B. Derivation / Code Structure

**[$f_2 = 0$ 극한과 $f_2 = 1$ 극한 — 양 극단 직관]:**

- $f_2 \to 1$ (분포가 elimination보다 *훨씬 빠름*): $C/C_{ss} \to (1 - e^{-\beta t})$ — 1구획 행동. Terminal half-life가 plateau 결정. 대부분의 약물이 이 영역.
- $f_2 \to 0$ (elimination이 분포보다 *훨씬 빠름*): $C/C_{ss} \to (1 - e^{-\alpha t})$ — 또 다른 1구획 행동, 그러나 *초기 phase의* half-life로! Body는 분배되기 전에 비워짐. Gentamicin·tobramycin이 이 영역.

R&T Fig.19-11이 정확히 이 양 극단 사이의 *연속 스펙트럼*을 한 그림으로 보여준다 ($f_2 = 0.01, 0.1, 0.5, 0.9, 1$).

**[Nicardipine 사례 — 어떻게 12hr 반감기 약물이 1hr에 plateau 도달하는가?]:**

R&T Fig.19-10. Nicardipine은 첫 phase t½ ≈ 20 min, terminal phase t½ ≈ 12 hr이지만 **$f_1$이 매우 큼** (대부분의 elimination이 초기 phase에서). 따라서 plasma 농도 상승은 20-min half-life로 빠르게 진행, terminal phase는 plateau의 *상위 10%* 만을 채움. *50% Css*는 첫 phase 만으로 1시간에 달성, *90% Css*는 약 15시간에 달성 (terminal phase 채우기).

#### C. Structural Necessity

**왜 $f_2$가 plateau 도달의 결정자인가?**

Plateau 도달이란 *infusion = elimination*의 균형. 어느 phase가 elimination을 *부피로* (즉 AUC 비중으로) 지배하느냐가 plateau의 위치를 결정. $f_1, f_2$는 정확히 그 비중. 따라서 plasma 농도가 plateau에 *얼마나* 빠르게 도달하느냐도 동일 비중으로 결정.

#### D. Assumptions & Boundary Conditions

- Constant-rate infusion 가정. Bolus + maintenance regimen에서는 R&T Fig.19-13 (eptifibatide)에서 보듯, 단일 bolus + 단일 infusion으로는 distribution gap을 채울 수 없어 *"distribution dip"* 발생. 보충 bolus 필요.
- Multiple oral dose에서는 흡수 동력학이 추가 되어 $f_2$ 직관이 부분적으로만 적용. R&T Fig.19-15: 흡수가 distribution보다 느리면 distribution phase가 *사라진다* (digoxin 사례).

#### E. Limitations

- $f_2$ 직관은 plasma compartment에만 적용. Slowly equilibrating tissue의 축적은 *terminal half-life*가 결정 (R&T Fig.19-12, gentamicin tissue accumulation). 따라서 *효능*과 *독성* 부위가 다른 compartment에 있는 약물에서 dosing 결정이 비대칭.
- Aminoglycoside 사례: plasma trough monitoring이 tissue accumulation에 *둔감* — 대신 totaal duration of therapy 제한이 더 효과적 보호.

#### F. Five Cognitive Layers

| Layer | 내용 |
|---|---|
| **L1** | $C/C_{ss} = f_1(1-e^{-\alpha t}) + f_2(1-e^{-\beta t})$. 두 1구획 가상 약물의 가중합. |
| **L2** | Plateau 도달 곡선이 두 시간스케일을 가진 *bi-phase rise*. 빠른 상승 후 느린 미끄러짐. R&T Fig.19-10 Nicardipine. |
| **L3** | RC 회로 캐스케이드 응답 (두 시정수)와 동형. 빠른 capacitor가 먼저 충전, 느린 capacitor가 뒤따라 충전. |
| **L4** | $f_1$ 큰 약물 = 빠르게 plasma 평형 도달, slowly equilibrating tissue는 천천히 축적. $f_2$ 큰 약물 = plasma도 천천히 — 1구획처럼. |
| **L5** | 임상에서 *dosing interval = terminal half-life × 1*은 $f_2 \approx 1$일 때만 안전. Aminoglycoside 같이 $f_2 \approx 0$이면 *initial phase half-life* 기반 짧은 interval + 전체 치료기간 제한이 표준. |

> **CONTEXT (1문장 처리):** Constant-rate infusion 후 stop, extravascular dose (oral 흡수 + 분포 + 소실), urine cumulative excretion, bolus + infusion 보정 (eptifibatide, R&T Fig.19-13) — 이들은 모두 동일한 2구획 ODE의 *입력함수만 바꾼* 변형이며 본 카드의 $f_1, f_2$ 직관이 통째로 transfer된다.

#### G. Zettelkasten Atom

```yaml
---
aliases: [terminal half-life trap, f2 fractional area, effective half-life, plateau time, distribution kinetics clinical]
tags: [pharmacometrics/pk/clinical, pharmacometrics/dosing-regimen]
up: "[[Distribution Kinetics MOC]]"
related: ["[[Effective Half-life]]", "[[Aminoglycoside TDM]]", "[[Nicardipine]]"]
source: "R&T Ch.19 Eq.19-26 / G&W Eq.2:139, Eq.2:168"
---

Plasma 농도의 plateau 도달 시간은 terminal half-life가 아니라 fractional area로 가중된 두 phase half-life의 mixture가 결정한다. f₂가 1에 가까우면 terminal half-life가 결정자(통상 약물), f₂가 0에 가까우면 초기 phase가 결정자(aminoglycoside). Nicardipine: terminal t½=12hr인데 50% Css가 1hr (f₁ 큼). Gentamicin: terminal t½=87hr인데 plasma는 4hr로 행동(f₂≈0). Effective half-life = ln(2)·MRT가 진정한 elimination 본위 측정. Tissue accumulation은 plasma trough에 둔감하므로 aminoglycoside는 총 치료기간 제한이 표준 보호 전략.
```

<!-- RECAP -->
**§2 흐름 요약:** 곡선 분리(M1) → 좌표계 변환(M2) → 분포용적 3중 체계(M3, Apex) → 좌표계 선택의 수치 비용(M4) → 모든 것의 임상 귀결(M5). M3의 Apex 위치가 §5 Critical Blow와 짝을 이룬다.

---

## §5 — Confusion Pair Dissection

본 세션에서 진정으로 혼동 가능한 4개 쌍을 식별하고 해부한다. **Critical Blow는 Vss vs Vβ 쌍** (Apex Concept과 짝).

---

<!-- CONFUSION -->
### 혼동쌍 #1: $V_{ss}$ vs $V_\beta$ (= V, Vz) ⚡ **[▶ Critical Blow 적용]**

| 비교 차원 | $V_{ss}$ | $V_\beta$ |
|---|---|---|
| **표면적 유사성** | "둘 다 분포 평형 부근의 부피" — 보통 비슷한 값을 가짐 (aspirin: 10.4 vs 13.7L, 32% 차이). 그래서 *항상* 비슷할 거라는 잘못된 일반화. | |
| **수식/코드 형태** | $V_{ss} = MRT \cdot CL = D_{iv} \cdot AUMC/AUC^2$ | $V_\beta = CL/\beta = D_{iv}/(AUC \cdot \beta)$ |
| **생리학적/구조적 지시체** | *Elimination이 없다고 가정한* 약물의 진정한 분포 부피. 조직 친화도만의 함수. | Terminal phase에서의 *apparent* 부피. 조직 친화도 + elimination/distribution 속도 비의 함수. |
| **변화 방향** | 신부전 (CL↓): **불변** (분포 자체와 무관) | 신부전 (CL↓): **거의 불변** ($\beta$도 비례 감소). 그러나 이는 *우연*. |
| | 체중 증가: 비례 증가 (조직 부피 증가) | 체중 증가: 거의 비례 증가 (단, distribution 속도 변화 시 왜곡) |
| | $f_2 \to 1$ (distribution 빠름): $V_\beta \to V_{ss}$ | |
| | $f_2 \to 0$ (elimination 빠름): $V_\beta \gg V_{ss}$ | |
| **임상/모델링 결과** | NONMEM에서 *secondary derived parameter*로 보고. Covariate (체중·환자군)와 진정한 *분포* 관계. NDA에서 분포 변동성 보고의 표준. | NONMEM에서 *primary parameter*로 estimate하면 CL과 강한 내재 상관 → `$COV step` 실패 → covariate effect 부정확 → Phase 3 dose selection 6배까지 빗나감. |
| **⚡ 기억 고리** | **"$V_{ss}$는 켜진 형광등 아래 방의 진짜 크기 (분포 친화도). $V_\beta$는 빛이 너무 빨리 새는 천창 때문에 부풀어 보이는 가짜 크기 (분포 + 새는 속도). 새는 속도가 0에 가까울수록 두 크기가 같아진다 — $f_2 \to 1$. 새는 속도가 분포보다 빠르면 가짜 크기가 진짜의 6배까지 부풀어 오른다 — gentamicin이 그 사례다."** | |
| **🔴 치명적 타격 (Critical Blow)** | NDA 제출 시 PopPK 모델에서 분포 covariate effect를 $V_\beta$ 기준으로 보고하면 — FDA 심사관이 신부전 환자에서의 multiple-dose simulation을 요청할 때, 모델이 plasma trough를 systematic하게 underpredict함. Deficiency Letter 사유: *"The reported volume of distribution does not adequately characterize tissue accumulation in renal impairment, which may lead to underestimation of toxicity risk in the proposed dosing regimen."* 임상적으로는 gentamicin/aminoglycoside 환자에서 신독성/이독성을 예측 못함 — 누적 cochlear/renal 손상의 직접 원인. | |

---

<!-- CONFUSION -->
### 혼동쌍 #2: Initial phase ($\alpha$-phase) vs Terminal phase ($\beta$-phase) — *어느 것이 "elimination phase"인가?*

| 비교 차원 | $\alpha$-phase | $\beta$-phase |
|---|---|---|
| **표면적 유사성** | "끝 phase가 항상 elimination phase다" — 통상적 직관. 그러나 *fractional area*가 진짜 결정자. | |
| **수식/코드 형태** | $A \cdot e^{-\alpha t}$, $f_1 = (A/\alpha)/AUC$ | $B \cdot e^{-\beta t}$, $f_2 = (B/\beta)/AUC$ |
| **생리학적/구조적 지시체** | 통상: distribution + 부분 elimination. 그러나 *aminoglycoside류*에서는 거의 모든 elimination이 여기서. | 통상: redistribution + 잔여 elimination. 그러나 일부 약물에서 *redistribution만*. |
| **변화 방향** | $f_1$ 큰 약물 (nicardipine): 이 phase가 *elimination phase*. | $f_2$ 큰 약물 (대부분의 약물, aspirin): 이 phase가 *elimination phase*. |
| **임상/모델링 결과** | $f_1$ 큰 약물에서 dosing interval 결정자. Plasma trough monitoring이 *이 phase의 half-life*에 맞춰져야. | $f_2$ 큰 약물에서 plateau 도달 시간 결정자. |
| **⚡ 기억 고리** | **"Terminal phase = elimination phase는 *기본값*이지 *법칙*이 아니다. Fractional area $f_2$가 0.5 미만이면 terminal phase는 elimination이 아니라 *redistribution*이며, 진짜 elimination은 초기 phase에서 끝나고 약물이 plasma에서 사라진 뒤에도 tissue가 천천히 비워지는 것이 terminal phase의 정체다 — gentamicin이 살아있는 반례다."** | |

---

<!-- CONFUSION -->
### 혼동쌍 #3: Macro-constants (A, α, B, β) vs Micro-constants (k₁₀, k₁₂, k₂₁)

| 비교 차원 | Macro | Micro |
|---|---|---|
| **표면적 유사성** | "둘 다 1차 속도상수 (단위 t⁻¹)니까 비슷하지 않을까?" — *완전히 다른 양*. | |
| **수식/코드 형태** | $\alpha + \beta = k_{12} + k_{21} + k_{10}$ — *합*은 같다. | $\alpha\beta = k_{21}k_{10}$ — *곱*은 단순 관계. |
| **생리학적/구조적 지시체** | $\alpha, \beta$ = system matrix의 두 *고윳값*. 어떤 단일 생리 메커니즘에도 직접 매핑 안 됨 ("emergent property"). | $k_{10}$ = central에서 elimination 속도. $k_{12}, k_{21}$ = compartment 간 flux. *통상적으로* unphysical하지만 ODE의 흐름을 직접 표현. |
| **변화 방향** | 신부전 (CL↓): $\alpha, \beta$ *모두* 감소 (둘 다 $k_{10}$의 영향 받음). | 신부전 (CL↓): $k_{10}$만 감소. $k_{12}, k_{21}$은 불변. |
| **임상/모델링 결과** | Macro 직접 fit 시 $A, B, \alpha, \beta$ 간 강한 상관 → condition number 상승. Covariate 모델링에서 $\alpha$가 신기능과 *섞인 관계*. | 좌표계로서는 ODE의 자연스러운 변수. 그러나 $k$들은 $V_c$가 동시에 estimate되어야 무차원 정보 균형. |
| **⚡ 기억 고리** | **"Macro = 곡선이 보이는 모양 (하늘에서 본 강의 두 굴곡). Micro = 강물의 실제 흐름 속도 (땅에서 본 물의 움직임). 두 굴곡(α,β)은 세 흐름속도(k₁₀,k₁₂,k₂₁) 의 *조합*이지 그 자체가 흐름이 아니다 — 행렬의 고윳값과 행렬 성분의 차이다."** | |

---

<!-- CONFUSION -->
### 혼동쌍 #4: Effective half-life ($t_{1/2,e}$) vs Terminal half-life ($t_{1/2,\beta}$)

| 비교 차원 | $t_{1/2,e} = \ln 2 \cdot MRT$ | $t_{1/2,\beta} = \ln 2 / \beta$ |
|---|---|---|
| **표면적 유사성** | "둘 다 half-life니까 약물이 절반 빠지는 시간 아닌가?" — 정의는 다르고 값도 다르다. | |
| **수식/코드 형태** | $t_{1/2,e} = \ln 2 \cdot AUMC/AUC = t_{1/2,\alpha} \cdot f_1 + t_{1/2,\beta} \cdot f_2$ | $t_{1/2,\beta} = 0.693/\beta$ |
| **생리학적/구조적 지시체** | 평균 분자가 체내에 머무는 시간 × ln 2. 진정한 *시스템 평균* half-life. | Terminal phase에서 plasma 농도가 절반으로 감소하는 시간. *시스템 전체의 비움*과 무관. |
| **변화 방향** | 약물의 elimination 능력 변화에 비례 반응. $CL$↓ → $t_{1/2,e}$↑ 비례. | $f_2$가 작은 약물에서는 $CL$ 변화에 *둔감*. Gentamicin: 신부전에서 $t_{1/2,\beta}$는 비례 증가하지 않음 (initial phase가 진짜 변화). |
| **임상/모델링 결과** | Multiple dosing의 진정한 plateau 시간을 결정. R&T가 명시: "appropriate half-life defining elimination after a bolus dose is 0.693/λ₁" for gentamicin-like drugs. | 통상 약물에서는 elimination 표지자로 작동. 그러나 $f_2 < 0.5$ 약물에서는 *misleading metric*. |
| **⚡ 기억 고리** | **"Terminal half-life는 곡선의 마지막 기울기 — 마라톤 마지막 100m의 속도. Effective half-life는 전 구간 평균 속도 (시간 가중). 마라토너가 마지막 100m를 빠르게 달려도 평균은 느릴 수 있고, 천천히 달려도 평균은 빠를 수 있다 — terminal과 effective는 그렇게 어긋날 수 있다."** | |

---

## §7 — Self-Test: Active Recall Module

총 9개 질문 (회상 4 / 적용 5). 각 질문 끝 "**다음 깊이 질문**" 포함. **마지막 질문은 보스 딜레마 (Socratic Dilemma)**.

---

<!-- SELF-TEST -->
### Q1 (★★, 회상)

**질문:** 2구획 mammillary 모델에서 IV bolus 후 plasma 농도가 따르는 이중지수 방정식을 쓰고, 그 4개 macro-constant ($A, \alpha, B, \beta$)의 단위와 의미를 각각 명시하라.

**[정답 공개]**
$$C(t) = A \cdot e^{-\alpha t} + B \cdot e^{-\beta t}, \quad \alpha > \beta > 0$$

- $A$ [mg/L 또는 µg/L 등 농도 단위]: 초기 phase의 zero-time intercept. semilog plot에서 초기 직선의 y절편.
- $\alpha$ [time⁻¹]: 초기 phase의 1차 속도상수. semilog plot에서 초기 phase 기울기의 음수.
- $B$ [농도]: 후기 phase의 zero-time intercept. terminal phase 외삽한 직선의 y절편.
- $\beta$ [time⁻¹]: terminal phase의 1차 속도상수. 통상 $\beta < \alpha$.
- $C_0 = A + B$ (Eq.2:117).

**다음 깊이 질문:** $A$가 음수가 될 수 있는가? 어떤 투여 경로에서 가능한가?

---

### Q2 (★★, 회상)

**질문:** $V_{ss}, V_\beta, V_1$ 각각의 정의식 (macro-constant로) 을 쓰고, 일반적으로 성립하는 부등식과 부등식이 등호가 되는 조건을 명시하라.

**[정답 공개]**
- $V_1 = D_{iv}/(A+B)$
- $V_{ss} = D_{iv} \cdot (A/\alpha^2 + B/\beta^2)/(A/\alpha + B/\beta)^2 = MRT \cdot CL$
- $V_\beta = CL/\beta = D_{iv}/(AUC \cdot \beta)$
- 부등식: $V_1 \leq V_{ss} \leq V_\beta$
- 등호 조건:
  - $V_1 = V_{ss}$: 1구획 약물 (분포 즉시).
  - $V_{ss} = V_\beta$: $f_2 \to 1$, 즉 distribution이 elimination보다 *훨씬 빠를 때*. 사실상 1구획처럼 행동.

**다음 깊이 질문:** Aspirin에서 $V_\beta/V_{ss} = 13.7/10.4 = 1.32$. Gentamicin에서 $V_\beta/V_{ss} = 345/56 \approx 6.2$. 이 비율 차이를 어떤 단일 무차원 수가 결정하는가? (힌트: $f_2$).

---

### Q3 (★, 회상)

**질문:** Macro-constants에서 micro-constant $k_{21}$을 도출하는 식 $k_{21} = (A\beta + B\alpha)/(A+B)$을 *직관적으로* 설명하라. 왜 *가중평균*인가?

**[정답 공개]**
$k_{21}$은 peripheral compartment에서 central로 돌아오는 first-order rate constant. 이는 $\alpha$와 $\beta$ *사이의 어떤 값*이어야 한다 (만약 $k_{21}$이 $\alpha$나 $\beta$ 어느 한쪽보다 더 크거나 작으면 system matrix의 구조가 깨짐).

증명 스케치: $\alpha + \beta = k_{12}+k_{21}+k_{10}$, $\alpha\beta = k_{21}k_{10}$. 이로부터 $k_{21}$은 $\alpha$와 $\beta$ 사이 어딘가. 정확한 위치는 $A$와 $B$의 비중으로 결정 — *fractional area $f_1, f_2$의 가중*과 동일한 직관.

**다음 깊이 질문:** $A = B$이면 $k_{21}$의 위치는?

---

### Q4 (★★, 적용)

**질문:** R&T aspirin 데이터: $C(t) = 67e^{-0.23t} + 33e^{-0.05t}$ (mg/L, t in min), 650 mg IV bolus. 다음을 계산하라:
- (a) $V_1, V_{ss}, V_\beta, CL$
- (b) $f_1, f_2$
- (c) $t_{1/2,e}$ (effective half-life)

**[정답 공개]**
- $C_0 = A+B = 100$ mg/L → $V_1 = 650/100 = 6.5$ L.
- $AUC = 67/0.23 + 33/0.05 = 291.3 + 660 = 951.3$ mg·min/L → $CL = 650/951.3 = 0.683$ L/min = **683 mL/min**.
- $AUMC = 67/0.23^2 + 33/0.05^2 = 1267 + 13200 = 14467$ → $MRT = 14467/951.3 = 15.2$ min → $V_{ss} = MRT \cdot CL = 15.2 \cdot 0.683 = $ **10.4 L**.
- $V_\beta = CL/\beta = 0.683/0.05 = $ **13.7 L**.
- $f_1 = 291.3/951.3 = 0.31$, $f_2 = 660/951.3 = 0.69$.
- $t_{1/2,e} = \ln 2 \cdot 15.2 = 10.5$ min.
- $t_{1/2,\beta} = \ln 2 / 0.05 = 13.9$ min, $t_{1/2,\alpha} = \ln 2/0.23 = 3.0$ min.

**해석:** Aspirin은 $f_2 = 0.69$, 즉 elimination의 약 70%가 terminal phase에서. 따라서 terminal half-life (14 min)와 effective half-life (10.5 min)가 가까움. Aspirin은 "거의 1구획처럼" 행동.

**다음 깊이 질문:** 만약 sampling을 1시간 후부터만 했다면 어떤 값이 나왔을까? CL과 $V_d$의 추정 오차 방향은?

---

### Q5 (★★, 적용 — Apex 직접 시험)

**질문:** R&T gentamicin 환자: terminal $t_{1/2,\beta} = 87$ hr, initial phase $t_{1/2,\alpha} \approx 4$ hr, $f_2 \approx 0$, $V_\beta = 345$ L, $V_{ss} = 56$ L. 8시간마다 80 mg IM 다회투여 시:
- (a) Plasma trough가 plateau에 도달하는 시간을 결정하는 것은 $t_{1/2,\beta}$인가 $t_{1/2,\alpha}$인가? 왜?
- (b) Slowly equilibrating tissue에 약물이 plateau에 도달하는 시간은?
- (c) 신부전 (CL을 정상의 25%) 환자에서 dose 조정 시 $V_\beta$ 또는 $V_{ss}$ 어느 것을 기준 삼아야 하는가?

**[정답 공개]**
- (a) **$t_{1/2,\alpha} \approx 4$ hr 이 결정.** 왜냐하면 $f_2 \approx 0$ → R&T Eq.19-26의 두 항 중 $f_1 \cdot (1 - e^{-\alpha t})$ 항이 사실상 전부. Plasma trough는 4 hr 반감기로 빠르게 plateau 도달, 거의 축적 안됨. *R&T Fig.19-14에서 plasma trough가 처음부터 거의 안정*하게 보이는 이유.
- (b) **$t_{1/2,\beta} = 87$ hr이 결정 → 약 12일 (3.3 × 87 hr).** Tissue는 *terminal half-life*에 의해 천천히 축적. 축적 지수 $1/(1-e^{-\beta\tau}) \approx 16$ — 즉 plateau에서 tissue 농도는 첫 dose 후의 16배. R&T Fig.19-14가 정확히 이 광경.
- (c) **$V_{ss}$ 기준.** $V_{ss}$는 신부전과 무관하게 분포 친화도만 반영하므로, dose 조정의 기준은 *유지 농도 × $V_{ss}$* 가 되어야 amount in body의 진정한 추정. $V_\beta$는 신부전에서 *우연히* 거의 변하지 않지만 (R&T Eq.19-30 참조), 이를 기준 삼으면 multiple-dose 시 tissue 축적을 *정량적으로* 예측 못함.

**다음 깊이 질문:** Gentamicin 신독성/이독성이 *plasma trough*에 둔감한 이유는?

---

### Q6 (★, 적용)

**질문:** G&W PK8 case (100 µg IV bolus, Compound X). Table 8.1 발췌:

| 모델 | WRSS | Condition number |
|---|---|---|
| Bi-exponential (Macro) | 0.0437 | 125.2 |
| Takada | 0.0169 | 3,186 |
| Differential equation (ODE) | 0.0436 | 29.69 |

NDA 제출용 PopPK 분석에서 어느 모델을 1차 후보로 선택해야 하며, 그 이유는?

**[정답 공개]**
**ODE 모델 ($V_c, CL, Cl_d, V_t$).** 이유:
1. Condition number 29.69로 압도적으로 낮음 — `$COV step` 안정. covariate effect의 RSE 신뢰성 보장.
2. WRSS는 Macro와 거의 동일 (0.0436 vs 0.0437) → 적합도 손실 없음.
3. Parameter들이 *생리학적 의미 직접* — 체중·신기능·간기능 covariate 모델링이 자연스러움.
4. NONMEM ADVAN3 TRANS4와 정확히 일치 → 표준 도구로 재현 가능.

Takada 모델은 WRSS는 가장 낮지만 (0.0169) condition number 3,186 — covariance 추정 불안정. 또한 $V_t$의 시간의존 hyperbolic 형태는 covariate 모델링/PBPK 해석 어려움. *Goodness-of-fit ≠ Model qualifiability*.

**다음 깊이 질문:** Takada가 WRSS는 가장 낮은데 왜 condition number는 높은가? 이 모순을 한 문장으로 설명하라.

---

### Q7 (○, 적용)

**질문:** R&T Nicardipine: terminal $t_{1/2} = 12$ hr인데 50% Css 도달은 1 hr (Fig.19-10). 이 현상을 $f_1, f_2$ 직관으로 설명하고, 이런 행동의 임상적 함의 (loading dose 필요 여부)를 논하라.

**[정답 공개]**
Nicardipine은 $f_1$이 매우 큰 약물 (R&T 본문 추정: 첫 phase t½ ≈ 20 min, terminal phase t½ ≈ 12 hr이지만 $f_1 \approx 0.85+$). 따라서 R&T Eq.19-26에서:

$$\frac{C(t)}{C_{ss}} \approx 0.85 \cdot (1 - e^{-\ln 2/(20 \min)\cdot t}) + 0.15 \cdot (1 - e^{-\ln 2/(12 hr)\cdot t})$$

$t = 1$ hr에서 첫 항은 사실상 0.85에 도달, 두 번째 항은 약 0.083 → 합 약 0.93 — 그래서 1 hr에 50% 훨씬 넘게 도달.

**임상 함의:** Loading dose 불필요. 단순 constant infusion만으로 1시간 내 효능 농도 도달. 그러나 *마지막 10%의 plateau 채움*은 12-hr terminal half-life로 천천히 — *steady state 실제 도달*은 약 40 hr 필요. 전체 정상상태 행동을 보고하려면 충분한 monitoring 기간 필수.

**다음 깊이 질문:** 만약 Nicardipine을 1구획 모델로 잘못 fit해서 $V_d$를 과소 추정하면 어떤 임상 결과가 나타날까?

---

### Q8 (★★, 적용)

**질문:** NONMEM `$SUBROUTINES ADVAN3 TRANS4` 사용 시 $V_{ss}$를 어떻게 보고하는가? `$PK` 블록에 직접 `VSS = THETA(5)`로 estimate해야 하는가, 아니면 다른 방식인가?

**[정답 공개]**
**$V_{ss}$는 derived secondary parameter로 보고.** Direct estimation 금지.

```fortran
$PK
   CL  = THETA(1)*EXP(ETA(1))
   V1  = THETA(2)*EXP(ETA(2))
   Q   = THETA(3)*EXP(ETA(3))
   V2  = THETA(4)*EXP(ETA(4))
   ; ...

$ERROR
   ; ... residual model ...

$TABLE ID TIME ... CL V1 Q V2 NOPRINT ONEHEADER FILE=sdtab1
```

`Vss`는 후처리 (R/Excel/Pirana 보고서)에서 `Vss = V1 + V2` 또는 더 일반적으로 sd:`Vss = V1 + (Q/K21)·... etc` — 그러나 ADVAN3 TRANS4 가정 (central elim only) 하에서는 단순히 $V_{ss} = V_1 + V_2$.

**왜 Direct estimation 금지인가?** Vss는 V1, V2의 *합*이라는 *constraint*를 가진다. 이를 별도 THETA로 estimate하면 system이 over-parameterized + V1, V2와 강하게 상관 → singular OMEGA → `$COV step` 실패. 이는 Card M3 Plausible Fallacy의 NONMEM 실현.

**다음 깊이 질문:** 만약 covariate (예: 체중)이 V1과 V2에 *다르게* 영향 준다면 어떻게 모델링하는가?

---

### Q9 (★★, 보스 딜레마 — Socratic Dilemma) ⚡

**질문:**
> *NDA 제출용 PopPK 모델 선택 회의. 두 후보 모델이 동일 데이터 (300 healthy + patient subjects)에 fit 되었다.*
>
> - **모델 A** (Macro reparameterization, $A, \alpha, B, \beta$ 직접 estimate): OFV = 12,346, condition number = 1,840, WRSS = 8.12. Bootstrap RSE: $A$ 18%, $B$ 22%, $\alpha$ 14%, $\beta$ 8%. Covariate effect: 신기능이 $\beta$에 -0.41 (95% CI: -0.52 to -0.30). VPC: 모든 sub-population에서 95% CI 내 관측치 92% 포함.
>
> - **모델 B** (Physiological, ADVAN3 TRANS4, $CL, V_c, Q, V_t$ estimate): OFV = 12,358 (ΔOFV = +12 vs A), condition number = 47, WRSS = 8.31. Bootstrap RSE: $CL$ 6%, $V_c$ 9%, $Q$ 11%, $V_t$ 8%. Covariate effect: 신기능이 $CL$에 -0.78 (95% CI: -0.85 to -0.71). VPC: 95% CI 내 관측치 91%.
>
> **OFV는 A가 12 낮고 (likelihood ratio test로 통계적으로 유의), parameter precision은 B가 우수, condition number는 B가 압도적, covariate interpretability는 B가 명확.**
>
> 당신은 이 모델 선택 회의의 senior modeler다. NDA 제출용 *primary analysis model*로 어느 쪽을 선택하며, FDA 심사관 앞에서 그 선택을 어떻게 방어하는가?

**[정답 공개 — 거장의 Trade-off 논리]**

**선택: 모델 B (Physiological, ADVAN3 TRANS4).**

**왜 OFV 우위(모델 A)를 포기하는가 — 4단 방어 논리:**

1. **OFV ΔOFV = 12의 의미를 재해석:** χ² test에서 12는 p < 0.001로 통계적으로 유의하지만, *임상적으로 유의한가*는 별개. 두 모델의 VPC coverage (92% vs 91%)는 거의 동일 — 즉 데이터 설명력은 사실상 동일. ΔOFV 12는 *parameterization의 산물*이지 *모델 적합도의 본질*이 아닐 가능성이 높다.

2. **Condition number의 임상적 함의:** 1,840 (모델 A) vs 47 (모델 B). 모델 A는 covariance matrix의 가장 긴 축과 가장 짧은 축의 비가 1,840 — 즉 *어떤 parameter 조합 방향으로는 데이터가 정보를 거의 안 주고 있다*. Bootstrap이 이를 부분적으로 흡수했을 뿐. *Subgroup simulation의 외삽 신뢰도가 제한된다.*

3. **Covariate interpretability — 가장 결정적:** 신기능 → $\beta$의 -0.41 vs 신기능 → $CL$의 -0.78. 두 추정치는 *동일 사실의 다른 좌표 표현*이지만, 임상의/심사관에게 의미 있는 covariate는 $CL$이지 $\beta$가 아니다. $CL = k_{10} \cdot V_c$이고 $\beta$는 $\alpha\beta = k_{21}k_{10}$을 통해 *간접적으로*만 신기능에 연결. 모델 A의 -0.41은 신기능의 *진짜 효과* (-0.78)가 다른 macro-parameters에 분산된 결과. **FDA Population PK Guidance (2022)는 명시적으로 physiological parameterization 권장.**

4. **Subgroup dose simulation의 robust성:** Phase 3 dose justification에서 신부전 subgroup의 multiple-dose simulation을 수행해야. 모델 A는 신기능 → $A, B$에도 *간접 영향*을 covariate화하지 않으면 simulation이 부정확. 모델 B는 단일 covariate ($CL$)로 충분히 mechanistic.

**FDA 심사관 앞에서의 한 문장 방어:**
> *"We selected the physiological parameterization despite a marginal OFV penalty (ΔOFV = 12) because it provides the lowest condition number (47 vs 1,840), most precisely characterizes the renal function effect on a mechanistically interpretable parameter (clearance), and aligns with FDA Population PK Guidance recommendations for covariate model interpretability and dose-justification simulations in renal subgroups."*

**중요한 단서:** 만약 모델 A의 ΔOFV가 12가 아니라 *50 이상*이었다면, 그리고 VPC가 의미있게 더 좋았다면 — 그것은 모델 *구조* 자체의 차이를 시사 (예: 3구획 vs 2구획). 이 경우는 단순한 좌표계 차이가 아니므로 model misspecification을 추가 검토. **OFV는 항상 *먼저*가 아니라 *마지막*에 본다 — 우선은 condition number, parameter precision, covariate interpretability, VPC를 본다.**

---

## §8 — Meta-Frame & Big Picture

### A. Positioning — 28-세션 PK/PD 지식 아키텍처에서의 위치

**이 세션 전에 와야 했던 것:**
- 1구획 모델, $CL = Dose/AUC$, $V_d = CL/k$, MRT 정의 (Vol I 기초 세션)
- TMDD와 antibody PK (Session I-08) — 다구획 비선형 모델의 극단 사례
- NONMEM 데이터셋 구축 (Session II-02) — 다회투여/잔류 농도 표현
- General ADVAN/$DES (Session II-04) — ODE 직접 코딩법

**이 세션 직후:**
- ADVAN3/4/11/12 표준 모델 라이브러리 활용 — 본 세션의 좌표계 변환표가 직접 정당화
- Population PK 공변량 모델링 — 어느 분포용적($V_{ss}$ vs $V_\beta$)을 covariate화할지 결정 (M3 Apex 직접 활용)
- Goodness-of-fit 진단 (CWRES, $\eta$-shrinkage, VPC) — condition number와 함께 모델 qualification 도구

**이 세션이 결정적으로 떠받치는 고급 도메인:**

1. **PopPK NDA/IND submission**: 분포 변동성 보고 시 $V_{ss}$ vs $V_\beta$ 선택 + reparameterization condition number reporting. Deficiency Letter 핵심 발화점.
2. **PBPK (Physiologically-Based PK)**: 본 세션의 $V_c, V_t, Cl_d$가 PBPK의 organ blood flow / partition coefficient로 자연 확장.
3. **TMDD 모델 재방문**: TMDD에서도 $V_c$ vs $V_t$ 구분이 receptor occupancy 해석에 핵심. Session I-08 재접속.
4. **QSP (Quantitative Systems Pharmacology) 다구획 시스템**: 본 세션의 선형 ODE → 비선형 시스템으로 자연 확장, 그러나 *parameter identifiability 진단 도구*는 동일 (condition number, eigenvalue analysis).
5. **TDM / Bayesian dose optimization**: prior $V_{ss}, CL$의 분포 형태가 환자별 dose adjustment 신뢰성 결정.

### B. Dependencies — 이 섹션을 대충 넘겼을 때의 구체적 실패 모드

**실패 모드 1: NONMEM `$COV step` 실패의 만성화**

→ Card M4의 condition number 이해 부족
→ macro 또는 잘못된 reparameterization로 fit 시도
→ `R MATRIX ALGORITHMICALLY SINGULAR` 에러 빈번 발생
→ Bootstrap으로 우회 시도, 그러나 covariate effect의 RSE 신뢰도 사라짐
→ Covariate model 구축 단계에서 forward inclusion / backward elimination 진행 불가
→ Phase 3 dose justification 모델이 결국 부정확한 변동성 추정 위에 구축됨

**실패 모드 2: 신부전 환자 dose 조정의 systematic error (gentamicin류 약물)**

→ Card M3의 $V_{ss}$ vs $V_\beta$ 혼동
→ 신부전에서 $V_\beta$가 거의 변하지 않음을 보고 "분포에 영향 없음" 결론
→ Maintenance dose는 $CL$ 비례 감소시키되 dosing interval은 그대로 유지하는 잘못된 처방
→ 그러나 진실은 *tissue accumulation은 동일 dosing rate에서 신부전과 무관* ($V_{ss} \cdot C_{ss}$가 보존)
→ 만성 환자에서 cochlear/renal toxicity 누적 — terminal half-life 잘못 해석으로 *치료 기간 제한* 미적용

### C. Professional Moat — Vol I 프레임에서의 답

> *"NONMEM을 실행하고 GOF 플롯을 생성할 수 있는 주니어 모델러와, 2구획 모델을 데이터에 적합시킬 수 있는 AI가 이미 존재한다. 이 섹션의 원리를 — 메커니즘이 아닌 구조적 이해의 수준에서 — 진정으로 내면화한 연구자는 그 둘 중 어느 것도 복제할 수 없는 무엇을 갖고 있는가?"*

**구조적 답:** 본 세션을 *진정으로* 체화한 연구자는 — *동일한 약물 시스템의 동일한 데이터*가 *5종 이상의 동등한 좌표계로 표현될 수 있고, 그 좌표계 선택이 NONMEM 수치 안정성·임상 covariate 해석·규제 외삽 신뢰도를 동시에 결정한다는* 사실을 이해한다.

이 이해의 구조적 결과:
- **WRSS 0.0436 vs 0.0437이 본질적으로 같다는 것을 *즉시* 알아본다.** 그러나 condition number 29.69 vs 4,104의 차이는 *모델 qualification의 운명*을 결정한다는 것도 안다.
- **신부전 환자에서 $V_\beta$가 거의 변하지 않음을 보고 *놀라지 않는다*.** 그것이 elimination/distribution 속도 비의 *우연한* 결과이지 분포 자체의 불변이 아님을 안다.
- **Nicardipine이 12-hr terminal half-life에도 1시간에 50% Css에 도달함을 보고 *놀라지 않는다*.** $f_1$이 큰 약물의 자연스러운 행동임을 안다.
- **NONMEM `$COV step` 실패를 보고 *데이터 부족*으로 진단하지 않는다.** 좌표계의 informational 직교성 부족이 우선 의심 대상임을 안다.
- **FDA 심사관의 *"Why this parameterization?"* 질문에 4단 논리로 답할 수 있다** (보스 딜레마 답변).

이 능력은 *NONMEM 자동화 도구가 복제할 수 없다* — 왜냐하면 그것은 *결과*가 아니라 *판단*이기 때문이다. 그리고 AI가 해당 좌표계 변환과 condition number를 *계산*해줄 수는 있어도 — *왜 이 선택이 옳은가*를 FDA 심사관 앞에서 *방어 가능한 논리*로 구성하는 것은 구조적 이해의 산물이다.

---

```
---
✦ STEP 1 완료.

다음이 준비되었습니다:
  • §1 세션 헤더 & 로드맵 (Big Idea + 5-카드 항법도)
  • §2 개념 해부 카드 (5개 개념: M1 이중지수+잔차법 / M2 3중 좌표계 변환 / 
                       M3 V₁·Vss·Vβ [⚡Apex] / M4 5종 재파라미터화+condition number /
                       M5 분포속도론 임상파급)
                       Apex: M3 (V₁/Vss/Vβ — Plausible Fallacy 적용)
  • §5 혼동 쌍 해부 (4개 쌍: Vss vs Vβ / 초기 vs terminal phase / Macro vs Micro /
                    Effective vs Terminal half-life)
                    Critical Blow 적용: Vss vs Vβ (Apex와 짝)
  • §7 자기 테스트 (9개 질문 — 회상 4 / 적용 5, 보스 딜레마 Q9 포함)
  • §8 메타프레임 & 빅 픽처 (Positioning + Dependencies + Professional Moat Vol I 프레임)
  
  • 감지된 소스 유형: 혼합 (Vol I — G&W + R&T)
    - G&W: 수식 도출(Eq.2:117-2:170), PK7/PK8 케이스 수치
    - R&T: 임상 해석(Ch.19), aspirin/nicardipine/gentamicin 사례
  
  • Data Anchoring 소스: 
    - G&W Fig.2.43 (A=70, B=28 µg/L), PK7 (D=100µg, AUC=250, CL=0.4L/min, MRT=280, Vss=110L),
      PK8 Table 8.1 (5종 모델 WRSS·Cond.No 비교, Compound X)
    - R&T Aspirin (650mg IV, C=67e^(-0.23t)+33e^(-0.05t), V₁=6.5L, Vss=10.4L, V=13.7L, CL=683mL/min)
    - R&T Nicardipine (terminal t½=12hr, 50% Css 1hr — Fig.19-10)
    - R&T Gentamicin (t½β=87hr, t½α≈4hr, Vβ=345L, Vss=56L, accumulation index=16)
  
  • 마커 사용: <!-- MASTER LENS --> 5개 (Big Idea 블록), <!-- ANCHOR --> 4개 (개념 가교),
              <!-- TRENCH --> 3개 (Trench-Level Tip), <!-- CONFUSION --> 4개 (혼동쌍),
              <!-- SELF-TEST --> 1개 (§7 시작), <!-- RECAP --> 1개 (§2 흐름 요약)
  • FIGURE 마커: 없음 (Phase 4C 전담)

"계속"을 입력하면 Step 2 HTML 컴파일러가 실행됩니다.
Step 2는 위 내용 전체(§1·§2·§5·§7·§8) +
§3(구조적 동형성 지도) + §4(인터랙티브 시뮬레이터 + Assumption Collapse 토글) +
§6(실용 시나리오 & 진단 병리)를 단일 완성 HTML 파일로 통합합니다.
---
```

---

C-260502-094217-K7M

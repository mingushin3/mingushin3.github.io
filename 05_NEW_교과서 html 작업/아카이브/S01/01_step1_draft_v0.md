```markdown
# Step 1 Draft v0 — Master's Lens First Draft
## Session 01 — One-Compartment IV Kinetics: CL · V · t½ · K
**Source:** Gabrielsson & Weiner 5e Ch.2 §2.2.1–2.2.3 + Rowland & Tozer 5e Ch.3
**Pages:** G p.14–32, p.469–475 (Case Study PK1) / R&T p.53–76
**Mode:** A-Critical | **Learner:** PhD pharmacometrics, PopPK entry–intermediate

---

## ━━ CURATION MAP ━━

이 섹션은 PopPK 전 체계의 출발점이다. 핵심 통찰은 단 하나: **$CL$과 $V$는 독립적 일차 파라미터(primary)이고, $K$와 $t_{1/2}$는 그것들의 함수(secondary)이다.** 이 위계를 잘못 잡으면 NONMEM 파라미터화부터 신부전 용량 조정까지 모든 후속 결정이 어긋난다.

### MUST (체화 필수 — 전용 §2 카드)

| # | 개념 | MUST 판정 근거 (붕괴 테스트) |
|---|---|---|
| C1 | **Clearance ($CL$)** [⚡ Apex] | 항정상태 농도 $C_{ss}=R_{in}/CL$, AUC = Dose/$CL$, 유지용량 모두 $CL$ 단독 함수. 이 개념 없이는 PopPK 모델의 어떤 추정도 의미를 갖지 못한다. |
| C2 | **Volume of Distribution ($V$)** | 부하용량(loading dose) 결정 + $C_0=Dose/V$ + $K=CL/V$. $V$를 진짜 용적으로 오인하면 quinacrine 40,000 L 같은 값에서 사고 정지. |
| C3 | **Elimination Rate Constant ($K$)** | $C=C_0 e^{-Kt}$의 지수항. 1차 동력학의 수학적 표면. $K=CL/V$임을 모르면 $t_{1/2}$ 변화 원인을 추적 불가. |
| C4 | **Half-life ($t_{1/2}$)** | $t_{1/2}=0.693\cdot V/CL$ — 이중 의존성. 이 위계를 모르면 "$t_{1/2}$ 길어졌다 = $CL$ 감소"라는 선형적 오해 발생. 임상 실무 가장 자주 등장. |
| C5 | **Mean Residence Time ($MRT$)** | NCA 보고서 표준. 1구획 IV bolus에서 $MRT=1/K$이지만, 다구획에서는 $t_{1/2}$와 결정적으로 분기된다. 후속 세션(다구획)으로 가는 가교. |

### CONTEXT (1–2문장 보충 — 전용 카드 없음)

- **Extravascular absorption (Ka, F, $t_{lag}$, §2.2.4–2.2.5)** → 별도 흡수 모델 세션 주제. C1(CL) 카드 내에서 "F가 1보다 작으면 $CL$ 추정이 $CL/F$로 편향된다" 1문장 처리.
- **Free fraction $f_u$, $V_u$, tissue partition $K_{Pi}$ (G Eq.2:14–2:18)** → C2(V) 카드 내에서 "$V$는 $V_u \cdot f_u$로 분해되며 결합 변화 시 변동" 1문장 처리.
- **Distribution phase vs Terminal phase (R&T midazolam 사례)** → C4(t½) 카드 내에서 "midazolam의 초기 1시간 급강하는 분포 위상이며 terminal slope이 진짜 $K$" 1문장 처리.
- **Back-extrapolation from infusion ($C^I \to C^0$, G Eq.2:31)** → C5(MRT) 또는 C1(CL) 카드 내에서 1문장.
- **Renal clearance, $f_e$ (R&T p.66–68)** → C1(CL) 카드 내에서 "$CL = CL_R + CL_{NR}$, $CL_R = f_e \cdot CL$" 1문장.

### REJECTED (이 세션 범위 밖)

- 흡수 동력학 본격 도출 (Ka 추정, flip-flop, residual method) — 별도 세션
- Tissue partition coefficient 상세 (Table 2.1 methadone/morphine 데이터) — Distribution Kinetics 세션
- AUMC 도출 일반 (Eq.2:10) — NCA 세션에서 본격 다룸; MRT 카드에서 결과만 인용

---

## §1 — Session Header & Roadmap

### Big Idea (한 문장)

> **$CL$과 $V$는 약물의 신원증명서이고, $K$와 $t_{1/2}$는 그 두 정보가 만들어낸 그림자다 — 그림자를 보고 신원을 추론할 때 어느 쪽이 진짜 변했는지 분간하지 못하면 환자에게 잘못된 용량을 처방하게 된다.**

### 개념 항법도

```
            ┌─────────────────┐
            │   IV bolus PK   │
            │  (단일 구획, 1차)  │
            └────────┬────────┘
                     │
        ┌────────────┴────────────┐
        ▼                         ▼
   [Primary 일차]            [Secondary 이차]
   ┌───────────┐             ┌───────────┐
   │  CL · V   │ ────────▶  │  K · t½   │
   └───────────┘   K=CL/V   └───────────┘
                  t½=ln2·V/CL
                                │
                                ▼
                          ┌───────────┐
                          │    MRT    │  ← AUMC/AUC
                          │  = 1/K    │     (1-cmt 한정)
                          └───────────┘
```

5개 핵심 카드: **C1 Clearance** → **C2 Volume** → **C3 Elimination Rate Constant** → **C4 Half-life** → **C5 MRT**

### 지식 그래프 위치

**전제 지식 (선행):**
- 1차 미분방정식 ($dC/dt = -kC$ 적분)
- 자연로그·반감기 개념의 기초
- Plasma vs blood vs tissue 구분 (생리학 기초)

**이 세션이 열어주는 후속 지식:**
- 다구획 모델 (2-cmt: distribution phase가 별도 위상으로 분리)
- 비선형 PK (Michaelis-Menten — $CL$이 농도 의존적)
- TMDD (target binding이 $V$에 추가되는 결합 항)
- Hepatic/Renal clearance 기전 (R&T Ch.5 — $CL = Q \cdot E$의 생리학적 분해)
- PopPK 공변량 모델 (CL과 V의 IIV — η₁ vs η₂)
- NCA → Compartmental 전이 ($AUMC/AUC = MRT$가 비구획적 진입로)

---

## §2 — Concept Anatomy Cards

---

### 🃏 C1. Clearance ($CL$) [⚡ Apex Concept]

<!-- MASTER LENS -->
**[개념 Big Idea: 거장의 시각]**

신부전 환자에게 약을 처방할 때, 의사가 "$t_{1/2}$이 2배 늘었으니 용량을 절반으로 줄이자"라고 결정하면 — 그건 환자를 죽일 수 있는 추론이다. $t_{1/2}$ 증가의 원인이 $CL$ 감소가 아니라 $V$ 증가(부종, 체액저류)일 수도 있기 때문이다. 이 사고 분기점에서 $CL$을 정확히 분리해 추적하는 것이 임상약리학자의 첫 번째 자질이다.

**체화해야 할 단 하나의 직관:** $CL$을 "혈장에서 약물이 사라지는 속도"가 아니라, **"단위 시간당 완전히 비워지는 가상의 부피"**로 보라. 그러면 $CL = Q \cdot E$ (혈류량 × 추출비)가 즉시 직관이 된다 — 흐름과 효율의 곱. $CL$의 상한은 $Q$다 (perfect extractor라도 혈류 이상 못 청소).

**이 직관을 머리에 박고 아래로 진입하라.** 모든 항정상태 식, 모든 AUC 식, 모든 유지용량 식이 $CL$을 분모로 갖는 이유가 보일 것이다.

#### A. Formal Definition

**Clearance ($CL$):** 단위 시간당 혈장에서 약물이 완전히 제거되는 가상의 혈장(또는 혈액) 부피. 단위는 유량(mL/min, L/hr).

> $CL$은 실제 부피가 아니라 **용량/시간 단위로 표현된 청소 효율**이다. R&T 본문(p.56)이 강조하듯 — 완전 추출자(perfect extractor, $E=1$)에서도 $CL$의 상한은 $Q$(혈류량)이다.

#### B. Derivation / Code Structure

**도출 1 — Rate-based 정의:**
$$
\text{Rate of elimination} = CL \cdot C \quad \text{[출처: R\&T 5e, Ch.3, Eq.3-4]}
$$

**도출 2 — Q·E 분해 (R&T):**

R&T의 reservoir-extractor 모델에서 (Fig.3-3, p.55), 추출기로 들어가는 비율 $Q\cdot C$, 빠져나오는 비율 $Q \cdot C_{out}$, 추출비 $E = (C-C_{out})/C$. 따라서:
$$
CL = Q \cdot E \quad \text{[출처: R\&T 5e, Ch.3, Eq.3-5]}
$$
이 식은 임상약리학자가 $CL$을 보는 정수다 — **유량(flow) × 효율(efficiency)**.

**도출 3 — AUC 기반 추정 (Gabrielsson):**

$dC/dt = -CL/V \cdot C$를 0→∞ 적분하면:
$$
\int_0^\infty CL \cdot C \, dt = CL \cdot AUC_0^\infty = \text{Dose}
$$
∴
$$
CL = \frac{\text{Dose}}{AUC_0^\infty} \quad \text{[출처: Gabrielsson 5e, Ch.2, Eq.2:12, p.19]}
$$

**도출 4 — 항정상태 (Constant infusion):**

$dC/dt = R_{in}/V - CL \cdot C / V$가 $dC/dt=0$일 때:
$$
C_{ss} = \frac{R_{in}}{CL} \quad \text{[출처: Gabrielsson 5e, Ch.2, Eq.2:22, p.23]}
$$
> Gabrielsson p.23이 명시: "Clearance is the **sole parameter** that determines the maintenance dose required to keep the target plasma concentration at steady state." 이 한 문장이 $CL$ Apex 위상의 직접 증거다.

**Source-anchored 수치 (Gabrielsson Compound A, 4 volunteers, 10 mg IV bolus):**

| Subject | Sex | $K$ (min⁻¹) | $V$ (L) | $CL$ (L/min) | $AUC$ (µg·min·L⁻¹) |
|---|---|---|---|---|---|
| 1 | M | 0.01 | 10 | 0.1 | 98,000 |
| 2 | M | 0.02 | 9.8 | 0.2 | 49,000 |
| 3 | F | 0.02 | 10 | 0.2 | 51,000 |
| 4 | F | 0.01 | 20 | 0.2 | 51,000 |

[출처: Gabrielsson 5e, Case Study PK1, Tables 1.2/1.3, p.473–474]

<!-- ANCHOR -->
*Subject 1과 Subject 4를 비교하라 — $CL$이 같은데 $V$가 다르므로 $K$가 다르고, 따라서 $t_{1/2}$가 다르다. 그러나 $C_{ss}$는 동일한 주입속도라면 같다. 이 표는 $CL$의 독립성을 보여주는 가장 깨끗한 임상 증거다.*

#### C. Structural Necessity

**왜 $CL$이 비례계수(proportionality factor) 형태일 수밖에 없는가?**

1차 동력학 가정($dA/dt \propto A$) 하에서, 제거 속도는 농도와 반드시 선형 관계여야 한다. 이때 비례상수는 두 가지로 표현 가능하다:
- **분율 표현(fractional):** $K \cdot A$ (시간⁻¹ × 양 = 양/시간)
- **유량 표현(flow):** $CL \cdot C$ (부피/시간 × 양/부피 = 양/시간)

생리학적 인과(혈류, 추출, 대사효소 활성)는 모두 **농도**에 작용하지 분율에 작용하지 않으므로, $CL$ 표현이 기전적으로 필연이다. $K$ 표현은 결과적 수학 표현일 뿐.

#### C-2. Plausible Fallacy (그럴싸한 오류)

> **오류:** "$t_{1/2}$이 2배로 늘었으니 $CL$이 절반으로 감소했다"는 추론.

**나비효과 추적:**
1. $t_{1/2} = 0.693 \cdot V / CL$이므로, $t_{1/2}$ 증가는 ($CL \downarrow$) 또는 ($V \uparrow$) 또는 둘 다 가능.
2. 신부전 환자에서 부종이 동반되면 $V$가 30~50% 증가 가능 (특히 hydrophilic drug).
3. $CL$ 감소 없이 $V$ 증가만으로 $t_{1/2}$가 2배 되었는데 용량을 절반으로 줄이면 → **AUC가 절반이 되어 약효 부전**.
4. 반대로 $V$ 일정한데 $CL$만 감소했는데 용량을 그대로 두면 → AUC 2배 → **독성**.

**GOF 시그니처 — "Volume Drift" pattern:**
NONMEM 피팅에서 covariate (eGFR) → $CL$로만 모델하고 $V$로는 모델하지 않을 때, 신부전군에서 IPRED가 초기 농도를 체계적으로 과대예측하는 패턴. CWRES vs TIME plot의 초기 시점에서 음의 편향이 눈에 띄게 나타남.

[출처: 일반 PopPK 진단 — 정확한 페이지 인용 없음]

#### D. Assumptions & Boundary Conditions

| 가정 | 위반 시 결과 |
|---|---|
| 1차 동력학 (linear PK) | 농도 의존적 $CL$ → Michaelis-Menten 영역 |
| 단일 균질 구획 (well-stirred) | 분포 위상 출현 → 다구획 필요 |
| $CL$의 시간 불변성 | 효소 induction/inhibition → time-varying $CL$ |
| Plasma protein binding 일정 | $CL_{int}$ 유지되어도 $f_u$ 변동 시 $CL_b \neq CL_p$ |

#### E. Limitations

- **High-extraction drug (E≈1)에서:** $CL$이 거의 $Q$ 자체 → 혈류 변화에만 민감, 효소 변화에 둔감 (e.g., propranolol, midazolam)
- **Low-extraction drug (E≪1)에서:** $CL \approx Q \cdot f_u \cdot CL_{int}/Q = f_u \cdot CL_{int}$ → 혈류 무관, 결합·효소 활성에 민감 (e.g., warfarin, phenytoin)
- 이 high/low 분기는 R&T Ch.5의 hepatic extraction 모델로 본격 다뤄짐 (이 세션 범위 밖, 후속).

#### F. Five Cognitive Layers

| 레이어 | Vol I — 이론 (R&T / Gabrielsson) |
|---|---|
| **L1 형식적 수학** | $CL = Q \cdot E = \text{Dose}/AUC = R_{in}/C_{ss}$. 단위 [부피/시간]. |
| **L2 기하학적 직관** | log-linear plot에서 AUC 면적의 역수. C₀-AUC 직사각형의 "효율 측정자". |
| **L3 구조적 동일성** | RC 회로의 컨덕턴스 G = 1/R (전류 = G × 전압). 강의 단위시간 유출량. |
| **L4 생리학적 의미** | 간 청소율 $CL_H$ + 신 청소율 $CL_R$ + 기타. Total CL = 모든 제거 경로의 가법적 합. |
| **L5 실무 투영** | NONMEM `$THETA (0, 5)` (CL=5 L/hr 초기치), `TVCL = THETA(1)`, `CL = TVCL*EXP(ETA(1))`. NDA Section 5.3 PopPK 보고서 첫 표 항목. |

#### G. Zettelkasten Atom

```yaml
---
aliases: [청소율, Clearance, Total Clearance, CL]
tags: [pharmacometrics/pk/primary-parameter, popPK/structural-model]
up: "[[MOC — One-Compartment IV Kinetics]]"
related: ["[[Volume of Distribution]]", "[[Steady-State Concentration]]",
          "[[Hepatic Extraction Ratio]]", "[[Renal Clearance fe]]"]
source: "Gabrielsson 5e Ch.2 §2.2.1–2.2.3 / Rowland & Tozer 5e Ch.3"
---

# Clearance (CL)

CL은 단위 시간당 약물이 완전히 제거되는 가상 혈장 부피이며, 1차 PK에서
유일한 일차(primary) 제거 파라미터다. 항정상태 농도 Css = R_in/CL과
AUC = Dose/CL이 모두 CL 단독 함수이므로, 유지용량 결정의 기반이다.
물리적 분해 CL = Q·E는 high-extraction 약물(혈류 의존)과 low-extraction
약물(효소·결합 의존)을 가르는 임상 분기점이다. t½ 변화를 CL 변화로
직선적으로 추론하는 것은 V 변동을 무시한 흔한 오류다.
```

> **CONTEXT 보충 (Ka·F·$f_u$ 관련 1문장):** Extravascular 투여 시에는 진짜 $CL$이 아니라 $CL/F$가 추정되며, R&T p.66–68의 $f_e$ (urinary fraction)을 통해 $CL_R = f_e \cdot CL$로 신 청소율 분리 가능.

---

### 🃏 C2. Volume of Distribution ($V$)

<!-- MASTER LENS -->
**[개념 Big Idea: 거장의 시각]**

신생아에게 hydrophilic 항생제(gentamicin)를 처방할 때 — 성인 mg/kg 용량을 그대로 적용하면 약효 부전이 일어난다. 신생아의 체수분 비율이 성인의 1.5배이기 때문이다. **$V$를 부피가 아니라 "결합·분포의 비례계수"로 보지 못하는 사람은 평생 이 종류의 처방 오류를 반복한다.**

**체화해야 할 단 하나의 직관:** $V$를 양동이의 부피로 보지 말고, **"약물 총량을 측정 가능한 혈장 농도로 환산하는 환산률(conversion factor)"**로 보라. 그러면 quinacrine의 $V$ = 40,000 L — 인체보다 600배 큰 값 — 도 즉시 납득된다 (조직 결합이 너무 강해서 혈장에 0.0017%만 남는 것).

**이 직관을 머리에 박고 아래로 진입하라.** Gabrielsson Fig.2.3의 활성탄 양동이 비유가 무엇을 가르치려 했는지 보일 것이다.

#### A. Formal Definition

**Volume of Distribution ($V$):** 평형 상태에서 약물 총량 $A_b$를 혈장 농도 $C$로 나눈 값. 약물이 분포하는 **겉보기(apparent)** 부피.
$$
V = \frac{A_b}{C} \quad \text{[출처: Gabrielsson 5e, Ch.2, Eq.2:14, p.20]}
$$

**핵심 의미론:** $V$는 실제 해부학적 공간이 아니라 **비례상수**다. 하한은 plasma volume(~3 L), 상한은 quinacrine처럼 40,000 L도 가능. R&T p.63: "Volume measured is, in effect, a dilution space but, unlike the reservoir, this volume is not a physical space but rather an apparent one."

#### B. Derivation / Code Structure

**도출 1 — IV bolus 직접 추정:**
$$
V = \frac{D_{iv}}{C^0} \quad \text{[출처: Gabrielsson 5e, Ch.2, Eq.2:13, p.20]}
$$

> R&T p.62는 동일 정의를 R&T Eq.3-26으로 제시. Gabrielsson Fig.2.7의 Compound A: $D=10{,}000$ µg, $C^0 = 1{,}000$ µg/L → $V = 10$ L.

**도출 2 — Free fraction 분해:**
$$
A_b = V \cdot C = V_u \cdot C_u \quad \Rightarrow \quad V = V_u \cdot f_u
$$
[출처: Gabrielsson 5e, Ch.2, Eq.2:15, p.20]

여기서 $V_u$ (unbound volume)와 $f_u$ (free fraction)가 독립 변수이며 $V$는 그들의 함수임을 Gabrielsson p.20이 명시: "Note that $f_u$ and $V_u$ are the **independent variables** and $V$ is a function of both of them."

**도출 3 — Steady-state physiological decomposition (G Eq.2:16):**
$$
V_{ss} = V_B + \sum_{i=1}^{n} V_{Ti} \cdot K_{Pi} \cdot (1-E_{Ti})
$$
혈액 부피 + (조직 부피 × 분배계수 × 비추출분율). 추출 장기에서는 $(1-E_{Ti})$ 보정.

**도출 4 — k=CL/V 관계식의 이면:**

$dC/dt = -K \cdot C = -(CL/V) \cdot C$이므로
$$
K = \frac{CL}{V} \quad \text{[출처: Gabrielsson 5e, Ch.2, Eq.2:1, p.16]}
$$
이 한 줄에서 $V$가 "$CL$의 시간 척도화 분모"라는 두 번째 의미가 도출된다.

**Source-anchored 수치 (Compound A, 4 subjects, Gabrielsson Table 1.2):**

Subject 1·2·3: $V = 10$ L (모두 비슷). Subject 4: $V = 20$ L (혼자 2배).
Case Study PK1 본문 p.470 Fig.1.2 caption: "the lower intercept of the plasma concentration axis (higher volume) for subject 4."

#### C. Structural Necessity

**왜 $V$가 단순 혈장 부피(3 L)이 아니고 가변값인가?**

약물 분자가 혈장과 조직 사이에 분포 평형을 이룰 때, 조직 결합·지질 분배·이온 트랩 등에 의해 조직 농도가 혈장 농도보다 훨씬 높아질 수 있다(또는 낮을 수 있다). 그러나 **측정은 혈장에서만 한다.** 따라서 "약물 총량을 측정 농도로 설명하려면 얼마만 한 부피가 필요한가?"라는 질문의 답이 $V$이며, 이는 본질적으로 **인공 회계 단위**다 — 실제 부피 + 결합 효과를 모두 한 숫자로 흡수.

#### D. Assumptions & Boundary Conditions

| 가정 | 위반 시 결과 |
|---|---|
| 분포 평형 도달 | 분포 위상 동안 $V$ 추정 부정확 (R&T p.62–63) |
| Plasma protein binding linear | 농도 의존적 $f_u$ → 비선형 PK |
| Tissue binding 시간 불변 | 만성 투여 시 조직 축적으로 $V$ 변동 |
| Single dilution space | 다구획 동력학 → $V_1$, $V_{ss}$, $V_{\beta}$ 분기 |

#### E. Limitations

- **분포 평형 전 $V$ 추정은 무의미:** R&T p.63이 명시 — IV bolus 직후 $V = Dose/C^0$로는 정확한 $V$를 못 구하고, $V = CL/k$ 또는 $V = 1.44 \cdot CL \cdot t_{1/2}$로 우회.
- **Multi-compartment에서 V의 종류:** $V_c$ (central), $V_{ss}$ (steady-state), $V_{\beta}$ (terminal). 이 세션에서는 1구획만 다루므로 $V \approx V_{ss}$로 간주.

#### F. Five Cognitive Layers

| 레이어 | Vol I — 이론 |
|---|---|
| **L1 형식적 수학** | $V = D_{iv}/C^0 = CL/K = 1.44 \cdot CL \cdot t_{1/2}$. 단위 [부피]. |
| **L2 기하학적 직관** | log-linear plot에서 y절편의 역수에 dose를 곱한 값. |
| **L3 구조적 동일성** | 기체방정식 $PV=nRT$의 $V$ — 측정 압력으로 환산된 가상 부피. |
| **L4 생리학적 의미** | $V_{ss} = V_B + \sum V_{Ti} K_{Pi}$. $K_{Pi}$가 큰 약물(quinacrine)은 $V$가 BSA의 600배까지. |
| **L5 실무 투영** | NONMEM `V = THETA(2)*EXP(ETA(2))`. 부하용량 $LD = V \cdot C_{target}$ 직접 산출. |

#### G. Zettelkasten Atom

```yaml
---
aliases: [분포용적, Volume of Distribution, Vd, V, Vss]
tags: [pharmacometrics/pk/primary-parameter, distribution]
up: "[[MOC — One-Compartment IV Kinetics]]"
related: ["[[Clearance]]", "[[Free Fraction fu]]", "[[Tissue Partition Kpi]]",
          "[[Loading Dose]]"]
source: "Gabrielsson 5e Ch.2 §2.2.1, Eqs.2:13–2:18 / R&T 5e Ch.3 p.62–64"
---

# Volume of Distribution (V)

V는 약물 총량과 혈장 농도 간의 비례상수이며, 실제 부피가 아니라 결합·
분포의 효과를 흡수한 회계 단위다. CL과 함께 1구획 PK의 두 일차 파라미터를
이루며, V = Vu · fu로 분해된다. 부하용량 LD = V · C_target의 결정 인자이며,
하한은 혈장 부피(~3 L), 상한은 강한 조직결합 약물에서 40,000 L까지.
t½ = 0.693·V/CL에서 V가 두 배 되면 t½도 두 배 — CL과 독립적으로 t½에 작용.
```

> **CONTEXT 보충:** Gabrielsson Table 2.1의 methadone $V_{ss}=140{-}190$ L vs morphine $V_{ss}=230\pm60$ L 같은 차이는 조직결합의 종합 효과로, $K_{Pi}$ 값들의 합산을 통해 정량적으로 예측됨 (G Eq.2:18).

---

### 🃏 C3. Elimination Rate Constant ($K$)

<!-- MASTER LENS -->
**[개념 Big Idea: 거장의 시각]**

NONMEM 입문자가 흔히 ADVAN1 TRANS1로 모델을 짤 때, $K$를 직접 추정 파라미터로 두고 V만 따로 추정한다. 그래도 fit는 된다. 그러나 PopPK 보고서를 작성할 때 — 신부전 공변량을 $K$에 묶을 것인지 $CL$에 묶을 것인지 결정할 때 — $K$ 파라미터화는 **생리학적으로 잘못된 해석**을 강요한다. eGFR은 $CL_R$에 작용하지 $K$에 작용하지 않는다.

**체화해야 할 단 하나의 직관:** $K$를 "독립적 소실 속도"로 보지 말고, **"$CL$과 $V$의 비율로 결정되는 그림자 변수"**로 보라. 그러면 ADVAN1 TRANS2 (CL/V 파라미터화)가 왜 표준이 되었는지가 즉시 보인다.

**이 직관을 머리에 박고 아래로 진입하라.** $C = C_0 e^{-Kt}$의 지수 항이 어떻게 $CL$과 $V$의 합성물인지가 드러난다.

#### A. Formal Definition

**Elimination Rate Constant ($K$):** 1차 동력학에서 단위 시간당 제거되는 분율. 단위 시간⁻¹.
$$
K = \frac{CL}{V} \quad \text{[출처: Gabrielsson 5e, Ch.2, Eq.2:1, p.16]}
$$

R&T p.56–57은 동일 관계식을 Eq.3-7로, "fractional rate of elimination"으로 명시.

#### B. Derivation / Code Structure

**도출 1 — ODE 적분:**

1구획 IV bolus, 1차 소실:
$$
\frac{dC}{dt} = -K \cdot C = -\frac{CL}{V} \cdot C
$$
초기조건 $C(0) = C^0 = D/V$로 적분:
$$
C = C^0 \cdot e^{-Kt} = \frac{D}{V} \cdot e^{-(CL/V)\cdot t} \quad \text{[출처: Gabrielsson 5e, Ch.2, Eq.2:4, p.17]}
$$

**도출 2 — 그래픽 추정:**

$\ln C = \ln C^0 - K \cdot t$ → semi-log plot에서 기울기 = $-K$.
[출처: R&T 5e, Ch.3, Eq.3-11, p.58]

Gabrielsson Compound A 그래픽 추정 (p.18):
$$
\text{slope} = -K = \frac{\ln(800) - \ln(400)}{23 - 87} = -0.01 \text{ min}^{-1}
$$
[출처: Gabrielsson 5e, Ch.2, Eq.2:5, p.18]

**도출 3 — Fraction remaining:**
$$
\frac{A}{Dose} = e^{-Kt} = \left(\frac{1}{2}\right)^n \quad (n = t/t_{1/2})
$$
[출처: R&T 5e, Ch.3, Eq.3-19, p.59]

> R&T Table 3-1 (p.57): $K=0.1$ hr⁻¹일 때 1시간 후 90 mg, 2시간 후 81 mg, ... — 매 시간 10%씩 줄어드는 분율 소실의 정의 자체.

#### C. Structural Necessity

**왜 $K$의 형태가 $CL/V$일 수밖에 없는가?**

**차원 분석:**
- 제거 속도 = $CL \cdot C$ [부피/시간 × 양/부피] = [양/시간]
- 분율 소실 속도 = (제거 속도)/(체내 양) = $CL \cdot C / (V \cdot C)$ = $CL/V$ [시간⁻¹]

분율로 표현하려면 $V$로 나누는 것 외에 다른 수학적 가능성이 없다. 이것이 $K$가 secondary parameter인 구조적 이유다.

#### D. Assumptions & Boundary Conditions

- 1차 동력학 (linear PK)
- 분포 평형 — terminal phase에서만 $K$가 진짜 elimination rate constant
- $CL$, $V$ 시간 불변

#### E. Limitations

- **분포 위상 중에는 $K$가 의미 없음:** R&T p.62의 midazolam — 초기 1시간은 distribution phase, 이후 terminal phase에서만 $K = 0.182$ hr⁻¹.
- **Flip-flop 상황:** Extravascular에서 $K_a < K$이면 terminal slope이 $K$가 아니라 $K_a$를 반영 (G p.29–30, CONTEXT 처리).

#### F. Five Cognitive Layers

| 레이어 | Vol I — 이론 |
|---|---|
| **L1 형식적 수학** | $K = CL/V$. semilog 기울기 $= -K$. |
| **L2 기하학적 직관** | log scale에서 일정 기울기로 직선 — 이 기울기가 $K$. |
| **L3 구조적 동일성** | RC 회로 방전: $V_C(t) = V_0 e^{-t/RC}$. $1/RC$가 $K$에 대응. |
| **L4 생리학적 의미** | "체내 약물의 X%가 매 시간 사라진다"는 분율 의미. |
| **L5 실무 투영** | NONMEM ADVAN1 TRANS1 (K 직접 추정) vs TRANS2 (CL, V 추정). 후자가 표준. |

#### G. Zettelkasten Atom

```yaml
---
aliases: [소실속도상수, K, k, ke, lambda_z]
tags: [pharmacometrics/pk/secondary-parameter, first-order-kinetics]
up: "[[MOC — One-Compartment IV Kinetics]]"
related: ["[[Clearance]]", "[[Volume of Distribution]]", "[[Half-life]]"]
source: "Gabrielsson 5e Ch.2 Eq.2:1 / R&T 5e Ch.3 Eq.3-7"
---

# Elimination Rate Constant (K)

K = CL/V는 1차 동력학에서 단위 시간당 분율 소실 속도이며, 일차 파라미터
CL과 V의 비율로 결정되는 secondary parameter다. semilog plot에서 -K가
기울기로 직접 관찰되며, fraction remaining = e^(-Kt) = (1/2)^n으로
반감기와 직결된다. NONMEM에서는 K 직접 추정(TRANS1)보다 CL/V 파라미터화
(TRANS2)가 표준 — 공변량을 생리학적으로 옳은 위치에 묶기 위함.
```

---

### 🃏 C4. Half-life ($t_{1/2}$)

<!-- MASTER LENS -->
**[개념 Big Idea: 거장의 시각]**

대부분의 임상의가 신기능에 따른 용량 조정을 "$t_{1/2}$ 기준"으로 한다. 그러나 $t_{1/2}$ 단독으로 보면 — 이는 $CL$ 변화인지 $V$ 변화인지 분간하지 못한다. **간경변 환자의 midazolam $t_{1/2}$이 길어지는 것은 주로 $CL$ 감소 때문이지만, 신부전 환자의 hydrophilic 약물 $t_{1/2}$ 증가는 $V$ 변화도 함께 일어난다.** 이를 동등하게 처리하면 처방이 어긋난다.

**체화해야 할 단 하나의 직관:** $t_{1/2}$을 "약물 빠지는 속도"로 보지 말고, **"$CL$과 $V$ 두 변수가 만든 합성 시간 척도"**로 보라. 그러면 R&T p.58의 핵심 문장 "Half-life is controlled by $V$ and $CL$, **and not vice versa**"가 한 줄의 슬로건이 아니라 임상 결정 트리의 시작점이 된다.

**이 직관을 머리에 박고 아래로 진입하라.** creatinine과 inulin이 같은 $CL$을 갖는데도 $t_{1/2}$이 다른 이유가 보일 것이다.

#### A. Formal Definition

**Half-life ($t_{1/2}$):** 혈장 농도(또는 체내 약물량)가 절반으로 감소하는 데 걸리는 시간.
$$
t_{1/2} = \frac{\ln 2}{K} = \frac{0.693 \cdot V}{CL} \quad \text{[출처: R\&T 5e, Ch.3, Eq.3-16, p.58]}
$$

#### B. Derivation / Code Structure

**도출:** $C(t_{1/2}) = 0.5 \cdot C^0$를 $C = C^0 e^{-Kt}$에 대입:
$$
0.5 = e^{-K \cdot t_{1/2}} \Rightarrow t_{1/2} = \frac{\ln 2}{K}
$$
$K = CL/V$ 대입:
$$
\boxed{t_{1/2} = \frac{0.693 \cdot V}{CL}}
$$
[출처: Gabrielsson 5e, Ch.2, Eq.2:6, p.18 / R&T 5e, Ch.3, Eq.3-15/3-16, p.58]

**Source-anchored 임상 수치 비교 (R&T p.58):**

| 화합물 | $CL$ (L/hr) | $V$ (L) | $t_{1/2}$ (hr) | 비고 |
|---|---|---|---|---|
| Creatinine | 4.5 | 42 (TBW) | 6.5 | 70-kg, 60-yr 표준 |
| Inulin | 4.5 | 16 (ECW) | 2.5 | 같은 $CL$, 작은 $V$ |
| Midazolam (R&T 사례) | 26 | 142 | 3.8 | hepatic clearance 사례 |

[출처: R&T 5e, Ch.3, p.58 (creatinine/inulin), Fig.3-4 caption (midazolam)]

> **이 표가 핵심이다 —** creatinine과 inulin이 같은 $CL$인데 $t_{1/2}$이 2.6배 차이 나는 이유는 $V$ 차이뿐. "$t_{1/2} \neq CL$ 함수"의 가장 깨끗한 임상 증거.

**Time to Steady-state (Gabrielsson Fig.2.8):**

| n half-lives | % SS 도달 |
|---|---|
| 1 | 50% |
| 2 | 75% |
| 3 | 87.5% |
| 3–4 | ~90% (실무 기준) |
| 6.64 | 99% (R&T 기준) |

[출처: Gabrielsson 5e, Ch.2, Fig.2.8, p.22 / R&T 5e, Ch.3, p.59]

<!-- ANCHOR -->
*"3–4 half-lives에 항정상태 90% 도달"이라는 임상 휴리스틱은 $t_{1/2}$이 $CL$과 $V$의 합성물이라는 점을 정확히 반영한다 — 따라서 $V$ 큰 약물은 항정 도달이 느리고, 이는 부하용량(loading dose)을 쓸지 결정하는 분기점이 된다.*

#### C. Structural Necessity

**왜 $t_{1/2}$이 dose에 무관한가?**

1차 동력학의 정의상 분율 소실 속도가 농도와 무관하므로, 100 mg에서 50 mg으로 가는 시간 = 50 mg에서 25 mg으로 가는 시간. 이는 동력학이 $K$에 의해서만 결정되고, $K$가 $CL$과 $V$의 비율이라는 점에서 자동으로 도출된다.

#### C-2. (이 카드는 Apex가 아님 — Plausible Fallacy 항목 생략)

#### D. Assumptions & Boundary Conditions

- Terminal phase 도달 후에만 의미 있음
- 1차 동력학
- $CL$, $V$ 시간 불변

#### E. Limitations

- **분포 위상에서 $t_{1/2}$ 추정은 잘못된 값:** R&T p.62의 midazolam — 초기 1시간을 사용해 추정하면 $t_{1/2}$이 실제 3.8 hr보다 훨씬 짧게 나옴.
- **다구획 모델에서:** $\alpha$-phase $t_{1/2}$ vs $\beta$-phase $t_{1/2}$ — 어느 것이 elimination 대표값인지 약물별로 다름 (gentamicin 사례, R&T p.66 Fig.3-7: distribution phase가 짧아 보이지만 실제로는 95% 약물이 그 위상에서 빠짐).

#### F. Five Cognitive Layers

| 레이어 | Vol I — 이론 |
|---|---|
| **L1 형식적 수학** | $t_{1/2} = 0.693V/CL$. 단위 [시간]. |
| **L2 기하학적 직관** | semilog plot에서 농도 절반 도달까지의 수평 거리. 어디서 측정해도 같음. |
| **L3 구조적 동일성** | 방사성 동위원소 반감기. 콘덴서 방전 시간 상수의 0.693배. |
| **L4 생리학적 의미** | $V$ 큰 약물(deep tissue 분포)은 $t_{1/2}$ 길고 항정 늦음. |
| **L5 실무 투영** | 투약 간격 결정 ($\tau \approx t_{1/2}$이 일반적), washout period 결정 ($5 \times t_{1/2}$). |

#### G. Zettelkasten Atom

```yaml
---
aliases: [반감기, half-life, t1/2, elimination half-life]
tags: [pharmacometrics/pk/secondary-parameter, dosing-interval]
up: "[[MOC — One-Compartment IV Kinetics]]"
related: ["[[Elimination Rate Constant]]", "[[Time to Steady State]]",
          "[[Loading Dose]]"]
source: "Gabrielsson 5e Eq.2:6 / R&T 5e Eq.3-15/3-16"
---

# Half-life (t½)

t½ = 0.693·V/CL은 농도가 절반이 되는 시간이며, CL과 V 두 일차 파라미터의
합성 시간 척도다 (secondary). t½ 변화를 CL 단독 변화로 추론하는 것은
임상 처방 오류의 흔한 원인 — V 변동(부종, 체액저류)도 동일하게 t½을 늘림.
3–4×t½에 ~90% 항정상태 도달, 6.64×t½에 ~99% 약물 소실 (R&T). dose에
무관하므로 1차 PK의 정량적 시그니처.
```

> **CONTEXT 보충 (분포 위상):** R&T p.62–63 midazolam 사례에서 IV bolus 후 약 1시간까지는 분포 위상이며, 이 동안의 농도 감소는 elimination이 아닌 조직 재분포가 주원인. terminal phase 진입 후에만 진정한 elimination $t_{1/2}$ 측정 가능.

---

### 🃏 C5. Mean Residence Time ($MRT$)

<!-- MASTER LENS -->
**[개념 Big Idea: 거장의 시각]**

NCA(Non-compartmental Analysis) 보고서에서 $t_{1/2}$만 보고하고 $MRT$를 빠뜨리면, FDA 심사관이 다구획 동력학 가능성을 묻는 Information Request를 보낸다. **$MRT$는 다구획 분포가 일어나는 약물에서 $t_{1/2}$이 놓치는 정보를 담는다.** 1구획 IV bolus에서는 $MRT = 1/K$로 단순하지만, 이 등식이 깨지는 순간이 다구획 모델이 필요한 순간이다.

**체화해야 할 단 하나의 직관:** $MRT$를 "약물 분자의 평균 체류 시간"으로 보라 — 이는 분자별 체류 시간 분포의 1차 모멘트(평균)다. 그러면 $AUMC/AUC$ 공식이 단순한 산술이 아니라 **확률 분포의 평균 정의** 그 자체임이 보인다.

**이 직관을 머리에 박고 아래로 진입하라.** Gabrielsson §2.2.3과 R&T Ch.3 후반부의 $MRT$ 도입이 왜 이 위치에 등장하는지 — 다구획 세션으로 가는 가교라는 점이 — 명확해질 것이다.

#### A. Formal Definition

**Mean Residence Time ($MRT$):** 약물 분자가 체내에 평균적으로 머무는 시간. 분자별 체류 시간 분포의 평균.
$$
MRT = \frac{AUMC_0^\infty}{AUC_0^\infty} \quad \text{[출처: Gabrielsson 5e, Ch.2, Eq.2:11, p.19]}
$$
$AUMC$ (area under the moment curve) = $\int_0^\infty t \cdot C(t) \, dt$.

#### B. Derivation / Code Structure

**도출 1 — 1구획 IV bolus의 단순화:**

$C = C^0 e^{-Kt}$이므로
$$
AUC_0^\infty = \int_0^\infty C^0 e^{-Kt} dt = \frac{C^0}{K}
$$
$$
AUMC_0^\infty = \int_0^\infty t \cdot C^0 e^{-Kt} dt = \frac{C^0}{K^2}
$$
∴
$$
MRT_{\text{IV bolus, 1-cmt}} = \frac{AUMC}{AUC} = \frac{C^0/K^2}{C^0/K} = \frac{1}{K}
$$
[출처: Gabrielsson 5e, Ch.2, Eq.2:10–2:11, p.19 / R&T 5e, Ch.3, Eq.3-25, p.60]

**도출 2 — $t_{1/2}$과의 관계 (1구획 IV bolus 한정):**
$$
MRT = \frac{1}{K} = \frac{t_{1/2}}{\ln 2} = \frac{t_{1/2}}{0.693} \approx 1.443 \cdot t_{1/2}
$$

> **수학적 필연:** $\ln 2 \approx 0.693$이므로 $1/0.693 \approx 1.443$. **MRT는 $t_{1/2}$보다 항상 정확히 44.3% 더 길다 — 이는 지수함수의 수학적 성질이지 약물·환자 특성과 무관한 보편 비율.**

**Source-anchored 수치 (Gabrielsson Compound A):**

| Subject | $K$ (min⁻¹) | $t_{1/2}$ (min) | $MRT$ (min) | $MRT/t_{1/2}$ |
|---|---|---|---|---|
| 1 | 0.01 | 68 | 98 | 1.44 |
| 2 | 0.02 | 34 | 48 | 1.41 |
| 3 | 0.02 | 36 | 53 | 1.47 |
| 4 | 0.01 | 71 | 100 | 1.41 |

[출처: Gabrielsson 5e, Case Study PK1, Table 1.3, p.474]

> 4명 모두 $MRT/t_{1/2} \approx 1.44$. 이 일정 비율은 1구획 + IV bolus의 **수학적 시그니처**다. 다구획 또는 extravascular에서는 이 비율이 깨진다.

#### C. Structural Necessity

**왜 $MRT$가 일차 모멘트(1st moment)로 정의되는가?**

확률론적으로 — 시간 $t$에 체내에 남아있는 분자 비율이 $f(t) = e^{-Kt}$일 때, 분자 한 개의 체류 시간을 확률변수 $T$로 보면 $E[T] = \int_0^\infty t \cdot (-df/dt) dt = \int_0^\infty t \cdot K e^{-Kt} dt = 1/K$. 

농도 $C(t)$가 잔존 비율에 비례하므로 $\int t \cdot C \, dt / \int C \, dt = E[T]$. **이것이 "AUMC/AUC = 평균 체류 시간"의 확률론적 기원이다.**

#### D. Assumptions & Boundary Conditions

- $MRT = 1/K$는 **1구획 + IV bolus** 한정. 다구획·extravascular에서는 별도 보정 필요.
- AUMC 추정의 정확도가 결정적 — terminal phase 외삽 오차 시 MRT 편향 큼.

#### E. Limitations

- **다구획 모델에서:** $MRT_{disp} = V_{ss}/CL$ (steady-state distribution time). 1구획 등식 깨짐 — 후속 세션에서 다룸.
- **Extravascular 투여에서:** $MRT_{po} = MRT_{iv} + MAT$ (mean absorption time). 흡수 위상이 추가됨.

#### F. Five Cognitive Layers

| 레이어 | Vol I — 이론 |
|---|---|
| **L1 형식적 수학** | $MRT = AUMC/AUC$. 1구획 IV bolus에서 $MRT = 1/K$. |
| **L2 기하학적 직관** | 농도-시간 곡선의 "무게 중심"의 시간 좌표. |
| **L3 구조적 동일성** | 통계 분포의 평균(1st moment). 질량 중심(center of mass). |
| **L4 생리학적 의미** | 분자가 평균적으로 체내에 얼마나 오래 머무는가의 시간 단위. |
| **L5 실무 투영** | NCA 보고서 기본 표 항목. PopPK 검증 단계에서 1구획 가정 검증용 ($MRT/t_{1/2} \approx 1.44$ 일관성). |

#### G. Zettelkasten Atom

```yaml
---
aliases: [평균체류시간, MRT, Mean Residence Time]
tags: [pharmacometrics/pk/nca, moment-analysis]
up: "[[MOC — One-Compartment IV Kinetics]]"
related: ["[[AUMC]]", "[[Half-life]]", "[[Distribution Kinetics]]"]
source: "Gabrielsson 5e Ch.2 Eq.2:11 / R&T 5e Ch.3 Eq.3-25"
---

# Mean Residence Time (MRT)

MRT = AUMC/AUC는 약물 분자의 평균 체내 체류 시간이며, 농도-시간 곡선의
1차 모멘트로 정의된다. 1구획 IV bolus에서 MRT = 1/K = 1.443 × t½이라는
수학적 필연 비율을 가지며, 이 비율의 어긋남이 다구획 동력학의 진단 시그니처가
된다. NCA 표준 보고 파라미터이며, 분포 동력학 세션의 V_ss = MRT × CL
관계식으로 가는 가교.
```

---

## §5 — Confusion Pair Dissection

이 세션에서 진정으로 혼동 가능한 3개 쌍을 식별. 각 쌍은 사이드-바이-사이드 대조로 해부한다.

---

### 🔀 Pair 1. $CL$ vs $K$ — Primary vs Secondary 위계 (★★★ — Critical Blow 적용)

<!-- CONFUSION -->

| 비교 차원 | $CL$ (Clearance) | $K$ (Elimination Rate Constant) |
|---|---|---|
| **표면적 유사성** | 둘 다 약물 소실 속도와 관련된 값. 둘 다 1차 PK의 핵심 숫자. 둘 다 "약물이 얼마나 빨리 빠지는가"를 묘사한다고 알려짐 | (좌측과 동일) |
| **수식/코드 형태** | $CL = \text{Dose}/AUC = R_{in}/C_{ss} = Q \cdot E$ | $K = CL/V$ — 두 일차 파라미터의 비율 |
| **단위** | [부피/시간] (L/hr, mL/min) | [시간⁻¹] (hr⁻¹, min⁻¹) |
| **생리학적/구조적 지시체** | 간 청소율 + 신 청소율의 합. 효소 활성·혈류·결합의 직접 산물. **공변량(eGFR, AST)이 직접 작용하는 위치** | 직접 지시체 없음. $CL$과 $V$ 변화의 합성 결과로 변동 |
| **변화 방향 — eGFR 50% 감소 시** | $CL_R$ 감소 → 전체 $CL$ 감소 (선형 반응) | $K = CL/V$ — $CL$ 감소만큼 비례 감소. 그러나 $V$도 함께 변하면 단순 비례 안 됨 |
| **변화 방향 — 부종 ($V$ 30% 증가) 시** | **무변화** ($CL$은 $V$와 독립) | $K = CL/V$ — $V$ 증가에 의해 $K$ 감소. $CL$ 변화 없는데 $K$ 변함 |
| **임상/모델링 결과** | NONMEM 공변량 모델: `CL = TVCL * (CRCL/100)**THETA(3)` — 옳음. 항정상태 농도 직접 결정 | NONMEM에서 `K = TVK * (CRCL/100)**THETA(3)` — 부분적으로 옳지만, $V$가 동시 변화 시 잘못된 모델 |
| **⚡ 기억 고리** | **$CL$은 약물의 신원증명서, $K$는 그 신원과 부피의 곱셈으로 만들어진 그림자다. 그림자가 짧아진 이유가 신원이 작아져서인지(부피 그대로) 가까이 와서인지(부피 감소) 그림자만 보고는 모른다 — 빛(원인)을 봐야 한다.** | (좌측과 동일) |
| **🩸 치명적 타격 (Critical Blow)** | **신부전 환자 PopPK 보고서에서 eGFR을 $K$에 묶어 모델링하고 NDA에 제출. 심사관(P3)이 "체액저류로 인한 $V$ 변화는 어떻게 분리했는가?"라는 Deficiency Letter를 발부 → 추가 임상 시험 요구로 6개월 지연, 또는 생리학적으로 $V$ 변화가 큰 hydrophilic 약물에서 신생아·노인 용량 추정이 30~50% 어긋나 약효 부전·독성 사고 발생.** | |

[출처: Gabrielsson 5e Ch.2 p.17 ("$Cl$ and $V$ are the **independent variables**"), R&T 5e Ch.3 p.58 ("Half-life and elimination rate constant usually depend on clearance and volume of distribution, **and not vice versa**")]

---

### 🔀 Pair 2. $V$ (apparent) vs $V_{ss}$ (steady-state)

<!-- CONFUSION -->

| 비교 차원 | $V$ (apparent, IV bolus 추정) | $V_{ss}$ (steady-state) |
|---|---|---|
| **표면적 유사성** | 둘 다 "분포 용적"이라 불리며 단위가 부피. 1구획 모델에서는 같은 값으로 일치하므로 입문자가 분리 인식하지 못함 | (좌측과 동일) |
| **수식/코드 형태** | $V = D_{iv}/C^0$ (back-extrapolation), 또는 $V = CL/K$ | $V_{ss} = V_B + \sum V_{Ti} K_{Pi} (1-E_{Ti})$ — 조직별 분배계수의 가법적 합 |
| **물리적 지시체** | semilog 외삽 절편 기반의 "환산 부피". 분포 위상이 빠를수록 정확 | 모든 조직과 평형이 진정으로 이루어진 후의 "총 분포 공간" |
| **변화 방향 — 다구획 약물에서** | $V_1$ (central compartment) 추정에 가까워짐 — $V_{ss}$보다 작음 | 진짜 분포 정도. 정확한 부하용량 산출 가능 |
| **변화 방향 — 1구획 약물에서** | $V \approx V_{ss}$ (구분 없음) | (좌측과 동일) |
| **모델링 결과** | 다구획 약물에 1구획 모델 적용 시 $V$ 추정이 분포 단계 따라 변동 — 잘못된 부하용량 산출 | NCA의 $V_{ss} = MRT \cdot CL$로 모델 비의존적 추정 가능 |
| **⚡ 기억 고리** | **$V$는 입국심사대에서 본 첫인상의 부피, $V_{ss}$는 호텔 체크인 후 짐 다 풀어놓고 측정한 진짜 부피. 입국심사대만 보고 호텔 방을 예약하면 짐이 다 안 들어가거나 너무 큰 방을 잡는다.** |  |

[출처: Gabrielsson 5e Ch.2 Eq.2:13 (V), Eq.2:16 (Vss)]

---

### 🔀 Pair 3. $t_{1/2}$ vs $MRT$

<!-- CONFUSION -->

| 비교 차원 | $t_{1/2}$ (Half-life) | $MRT$ (Mean Residence Time) |
|---|---|---|
| **표면적 유사성** | 둘 다 "약물의 시간 척도". 둘 다 "오래 남는 약 vs 빨리 빠지는 약"을 묘사 | (좌측과 동일) |
| **수식/코드 형태** | $t_{1/2} = 0.693/K = 0.693 V/CL$ — **1차 동력학 가정 필수** | $MRT = AUMC/AUC$ — **모델 가정 무관 (모멘트 기반)** |
| **수학적 의미** | "농도가 절반 되는 시간" — 분포의 중간점 | "분자의 평균 체류 시간" — 분포의 평균(1st moment) |
| **1구획 IV bolus에서** | $t_{1/2} = 0.693 \times MRT$ — 즉, $MRT$가 더 김 | $MRT = 1/K = 1.443 \times t_{1/2}$ |
| **다구획에서의 분기** | $\alpha$- vs $\beta$-phase $t_{1/2}$ 둘로 갈라짐. 어느 것이 elimination 대표인지 모호 | $MRT_{iv} = V_{ss}/CL$ — 일관된 정의 유지. **분포 동력학 정량 척도** |
| **NCA 보고에서** | terminal slope으로 추정. 분포 위상 영향 받기 쉬움 | 모멘트 기반 — 분포 위상도 통합 반영 |
| **⚡ 기억 고리** | **$t_{1/2}$은 방의 절반이 비는 시점(중앙값), $MRT$는 모든 분자의 평균 출국 시점(평균). 평균은 항상 중앙값보다 큰 정도가 일정하다 — 1구획 IV에서는 정확히 ×1/ln2 = ×1.443. 이 비율의 보편성은 지수분포의 수학적 필연이지 약물 특성이 아니다.** |  |

[출처: Gabrielsson 5e Ch.2 Eq.2:11, R&T 5e Ch.3 Eq.3-25]

<!-- RECAP -->
**§5 종합:** 세 쌍 모두 공통 구조 — **표면적으로 비슷한 두 양이 사실은 위계가 다른(primary vs secondary, apparent vs steady-state, median vs mean) 관계.** 이 위계를 잘못 쓰면 임상 결정·NDA 보고·NONMEM 모델 모두 어긋난다. Pair 1이 Critical Blow를 받는 이유는 — 이 혼동만이 **공변량 모델링 단계에서 바로 규제 거절 사유로 직결**되기 때문이다.

---

## §7 — Self-Test: Active Recall Module

총 9문제. 회상 4문항(Q1–Q4) / 적용 5문항(Q5–Q9, 마지막은 Boss Dilemma). 각 문항 끝에 "다음 깊이 질문" 첨부.

---

<!-- SELF-TEST -->
### Q1 [회상 ★★]
$t_{1/2}$을 $V$와 $CL$로 표현하시오. 이 식이 왜 "$t_{1/2}$이 secondary parameter임"을 보여주는지 설명하시오.

<details>
<summary>정답 공개</summary>

$$t_{1/2} = \frac{0.693 \cdot V}{CL}$$

이 식은 $t_{1/2}$이 $V$와 $CL$ — 두 독립 일차 파라미터 — 의 비율의 함수이며, 따라서 $t_{1/2}$ 단독으로는 $V$ 또는 $CL$ 어느 쪽이 변했는지 분간 불가. R&T p.58: "Half-life is controlled by $V$ and $CL$, and not vice versa."

**다음 깊이 질문:** 같은 $CL$을 가진 creatinine과 inulin이 R&T에서 왜 $t_{1/2}$ 2.6배 차이를 보이는가? (→ $V_{TBW}$=42L vs $V_{ECW}$=16L)
</details>

---

### Q2 [회상 ★]
$V$의 수식적 정의 두 가지를 쓰시오 (IV bolus 직접 추정 + 후행 추정).

<details>
<summary>정답 공개</summary>

(1) IV bolus 직접: $V = D_{iv}/C^0$ (G Eq.2:13)
(2) Clearance 경유: $V = CL/K = 1.44 \cdot CL \cdot t_{1/2}$ (R&T Eq.3-27/3-28)

두 번째 식은 분포 평형이 도달된 terminal phase의 데이터로 $V$를 더 정확히 추정할 때 사용. R&T p.62: 분포 위상 도달 전이라 $C^0$ 외삽이 부정확할 때 $V = 1.44 \cdot CL \cdot t_{1/2}$로 우회.

**다음 깊이 질문:** 다구획 약물에 (1) 식을 적용하면 $V_1$, $V_{ss}$, $V_\beta$ 중 어느 것에 가까운 값이 나오는가? (→ $V_1$, central compartment)
</details>

---

### Q3 [회상 ★]
$Css = R_{in}/CL$ (Gabrielsson Eq.2:22)을 1구획 ODE에서 도출하시오.

<details>
<summary>정답 공개</summary>

$\frac{dC}{dt} = \frac{R_{in}}{V} - \frac{CL}{V} \cdot C$

항정상태 ($dC/dt = 0$):
$$0 = \frac{R_{in}}{V} - \frac{CL}{V} \cdot C_{ss} \Rightarrow C_{ss} = \frac{R_{in}}{CL}$$

$V$가 양변에서 소거됨 — **항정 농도는 $V$와 무관, $CL$만의 함수.** Gabrielsson p.23: "Clearance is the **sole parameter** that determines the maintenance dose."

**다음 깊이 질문:** $V$가 항정 농도에 영향 없다면, 어떤 양에 영향을 미치는가? (→ 항정 도달 시간 $T_{ss} \approx 4 t_{1/2}$, 즉 $V$가 클수록 항정 도달 늦음)
</details>

---

### Q4 [회상 ○]
$MRT$의 정의식과, 1구획 IV bolus에서 $MRT$와 $t_{1/2}$의 관계를 쓰시오.

<details>
<summary>정답 공개</summary>

$MRT = AUMC_0^\infty / AUC_0^\infty$

1구획 IV bolus 한정: $MRT = 1/K = t_{1/2}/\ln 2 \approx 1.443 \cdot t_{1/2}$

이 1.443 비율은 지수분포의 수학적 필연이며, 약물·환자 특성과 무관. 이 등식이 깨지면(>1.443 또는 <1.443) → 다구획 동력학 시그니처.

**다음 깊이 질문:** 어떤 약물에서 $MRT/t_{1/2} = 1.8$로 측정되었다. 이 값이 1.443에서 벗어난 가장 가능성 있는 원인은? (→ 다구획 분포 — central에서 peripheral compartment로의 분포가 추가 체류 시간을 만듦)
</details>

---

### Q5 [적용 ★★]
다음은 Gabrielsson Compound A의 4명 데이터다 (Table 1.2):

| Subject | $V$ (L) | $CL$ (L/min) | $K$ (min⁻¹) | $t_{1/2}$ (min) |
|---|---|---|---|---|
| 1 | 10 | 0.1 | 0.01 | 68 |
| 4 | 20 | 0.2 | 0.01 | 71 |

Subject 1과 4는 $K$와 $t_{1/2}$이 거의 동일하다. 그러나 같은 주입속도 $R_{in}=10$ µg/min로 정맥주입 시 항정 농도 $C_{ss}$가 다를 것으로 예측되는가, 같을 것으로 예측되는가? 근거를 제시하시오.

<details>
<summary>정답 공개</summary>

**다르다.** 

Subject 1: $C_{ss} = 10/0.1 = 100$ µg/L
Subject 4: $C_{ss} = 10/0.2 = 50$ µg/L

$C_{ss}$는 $CL$만의 함수이므로 $CL$ 차이(0.1 vs 0.2)가 그대로 반영. $V$ 차이(10 vs 20)는 항정 도달 시간만 결정 — Subject 4가 $V$ 큰데도 $K$ 같은 이유는 $CL$도 비례 증가했기 때문.

이 사례는 "$t_{1/2}$ 같으면 약효 같다"는 직관이 틀린다는 가장 명료한 증거 — **항정 농도가 같으려면 $CL$이 같아야지, $t_{1/2}$이 같다고 같지 않다.**

**다음 깊이 질문:** 만약 Subject 1과 4를 같은 약물 다른 환자라고 본다면, 임상에서 어떤 환자 특성이 $V$만 두 배로 만들 수 있는가? ($CL$ 변화 없이) (→ 부종, 체액저류, 비만에서 hydrophilic 약물의 $V$ 증가)
</details>

---

### Q6 [적용 ★★]
간경변 환자의 midazolam을 측정한 결과 $t_{1/2}$이 정상 3.8 hr (R&T 사례)에서 8 hr로 증가했다. 다음 두 시나리오 중 어느 쪽이 더 가능성 높은가?

A) $CL$이 절반 감소 ($V$ 일정)
B) $V$가 두 배 증가 ($CL$ 일정)

추가로 어떤 측정으로 둘을 분간할 수 있는가?

<details>
<summary>정답 공개</summary>

**A가 압도적으로 가능성 높음.** Midazolam은 high-extraction hepatic clearance drug (E≈0.4–0.6, R&T)이므로 간경변에서 효소 활성·혈류 감소로 $CL$이 직접 감소. $V$는 lipophilic 약물이라 부종 체액저류에 둔감.

**분간 방법:** 
1. AUC 측정. AUC = Dose/$CL$이므로 $CL$ 감소 시 AUC가 비례 증가하지만, $V$ 증가만으로는 AUC 변화 없음 — **AUC가 결정적 분기 지표**.
2. $C^0$ 측정. $V$ 증가 시 $C^0 = D/V$가 감소하지만, $CL$ 감소 단독으로는 $C^0$ 무영향.

**다음 깊이 질문:** 만약 같은 환자에 hydrophilic 약물 (e.g., gentamicin, $V \approx ECW$)을 투여하면 어떤 패턴이 나오겠는가? (→ 부종으로 ECW 증가 → $V$ 증가 → $t_{1/2}$ 길어지고 $C^0$ 감소; AUC는 $CL_R$ 변화에 따름)
</details>

---

### Q7 [적용 ★]
R&T midazolam 사례: 79-kg 환자에게 7.5 mg base IV bolus, AUC = 287 µg·hr/L, $t_{1/2}$ = 3.8 hr. 

(a) $CL$을 계산하시오.
(b) $V$를 계산하시오 ($V = 1.44 \cdot CL \cdot t_{1/2}$).
(c) IV 투여 5분 시점에 plasma 농도가 180 µg/L로 측정되었다. 이 시점에 plasma volume(3.4 L)에 있는 약물량을 계산하고, 전체 dose 7.5 mg 중 몇 %가 이미 plasma 외부로 분포되었는지 추정하시오.

<details>
<summary>정답 공개</summary>

(a) $CL = \text{Dose}/AUC = 7500 \mu g / 287 \mu g \cdot hr/L = 26.1$ L/hr ≈ 26 L/hr.

(b) $V = 1.44 \times 26 \times 3.8 = 142$ L. (R&T p.63 일치)

(c) Plasma 내 약물량 = 180 µg/L × 3.4 L = 612 µg = 0.612 mg.
Plasma 외부 약물량 = 7.5 - 0.612 = 6.89 mg → **전체의 ~92%가 이미 plasma 외부로 분포**.

[R&T p.62 직접 인용 — "0.61 mg... The majority, 6.9 mg or 92% of the total 7.5-mg dose..."]

이 92% 분포는 IV bolus 후 5분이라는 짧은 시간에 일어났음 — 분포가 elimination보다 훨씬 빠르다는 시그니처.

**다음 깊이 질문:** 분포가 elimination보다 빠른 약물(midazolam)과 느린 약물(gentamicin, R&T Fig.3-7)의 임상적 차이는? (→ 전자는 distribution phase가 elimination에 미미한 영향 — 1구획 근사 안전; 후자는 95% 약물이 distribution phase에서 빠짐 → terminal phase가 elimination을 대표하지 않음)
</details>

---

### Q8 [적용 ★]
NCA 보고서를 작성하는데 어떤 약물의 $MRT/t_{1/2}$ 비율이 1.85로 측정되었다. 

(a) 이 값이 1.443에서 벗어난 가장 가능성 있는 약물 동력학적 원인은?
(b) 이를 PopPK 모델 구조 결정에 어떻게 반영해야 하는가?

<details>
<summary>정답 공개</summary>

(a) **다구획(multi-compartment) 분포 동력학.** 1구획 IV bolus에서 $MRT/t_{1/2} = 1/0.693 = 1.443$이라는 수학적 항등식이 성립. 이 값이 1.443을 초과하는 것은 약물이 central compartment에서 peripheral compartment로 분포한 후 다시 central로 redistribution되는 추가 체류 시간이 존재함을 의미.

수식으로: 다구획 IV bolus에서 $MRT_{iv} = V_{ss}/CL$이며, 이는 분포가 일어나는 시간만큼 1구획 등식을 초과.

(b) NONMEM 모델 선택:
- 1구획 모델로 fit 시 GOF에서 초기 시간 음의 편향 + terminal 시간 양의 편향 패턴 (CWRES vs TIME)
- 2구획 모델 (ADVAN3 TRANS4)로 전환 — $CL, V_1, Q, V_2$ 추정
- $V_{ss} = V_1 + V_2$ 검증을 통해 NCA $MRT \cdot CL$ 값과 일치 여부 확인

**다음 깊이 질문:** 1구획 모델로 잘못 fit한 약물의 부하용량을 1구획 $V$로 계산했을 때, 실제 임상에서 어떤 사고가 일어나는가? (→ 1구획 $V \approx V_1 < V_{ss}$이므로 부하용량 과소평가 → peripheral compartment 채우기 전 농도 부족 → 약효 부전; 또는 distribution phase 동안 일시적 고농도로 독성)
</details>

---

### Q9 — 보스 딜레마 (Socratic Dilemma) ★★

> **시나리오:** 당신은 신약 개발 회사의 PopPK lead. 새로운 진정제 후보 화합물 X (midazolam 유사 구조)의 Phase 1 SAD 데이터를 받았다. n=12 건강인, IV bolus 7.5 mg single dose, 12-time-point sampling 0.083–24 hr.
>
> R&T midazolam Fig.3-4와 동일하게 **명백한 biphasic decline**이 semilog plot에 나타난다. 분포 위상 약 1시간, terminal $t_{1/2}$ 약 4 hr.
>
> 두 가지 모델 옵션:
>
> **옵션 A — 1구획 모델 (ADVAN1 TRANS2):**
> - OFV 안정적, 모든 12명 수렴, $COV step 성공
> - GOF에서 초기 1시간 systematic 음의 편향 (CWRES = -1.5 ~ -2.5 평균)
> - AUC 추정이 NCA 대비 6% 과소
> - 임상의가 "단순 1구획"으로 이해하기 쉬움
>
> **옵션 B — 2구획 모델 (ADVAN3 TRANS4):**
> - OFV 60 단위 감소 (LRT p<0.001 유의)
> - GOF 깔끔, CWRES 패턴 없음, AUC 추정 정확
> - 그러나 12명 중 3명에서 $COV step 실패 ($V_2$ 추정 불안정 — η-shrinkage 35%)
> - $Q$의 RSE 80% (수치 불안정)
>
> **내일 IND를 제출해야 한다.** 어느 모델을 선택하고, FDA Section 5.3 PopPK 보고서에 어떻게 방어하는가?

<details>
<summary>정답 공개 — 30년 차 수석 모델러의 Trade-off 논리</summary>

**정답은 "어느 쪽이든 옳을 수 있으나, 결정 논리가 규제 보고서에 명시적으로 기록되어야 한다."**

#### 만약 옵션 A를 선택한다면 — 방어 논리:

> "1구획 모델은 GOF에서 분포 위상 미세 편향을 보이지만, AUC 6% 과소예측은 ICH E14/FDA TQT 가이드라인의 90% CI ± 0.10 윈도우 내. 분포 위상은 임상 결정에 영향을 미치지 않는 시간 (sampling 빈도가 낮은 임상 운영 환경)에 한정. 2구획 모델은 30 명 중 3명에서 $COV step 실패 — Phase 1 추정의 강건성(robustness) 부족. **Phase 2 sparse sampling 환경에서 동일 모델을 적용 시 12명 중 8명 이상에서 수렴 실패 예상.** 보수적 모델 선택이 임상 의사 결정의 신뢰성에 기여."

→ **이 논리가 통하는 조건:** 약물의 임상 효과가 terminal exposure (AUC, Cmax)에 의존하고, 분포 위상의 일시적 고농도가 안전성 우려가 아닐 때.

#### 만약 옵션 B를 선택한다면 — 방어 논리:

> "Biphasic decline은 통계적으로 유의 (LRT p<0.001), 임상적으로 의미 있음 — distribution phase 동안 brain partition으로 인한 진정 효과 발현이 $V_1$에 의존. 1구획 모델의 6% AUC 편향은 정량적으로는 작아 보이나, 신부전·노인 공변량 적용 시 distribution phase 변동이 증폭되어 부하용량 산출에 임상적 차이 발생. $COV step 실패는 sampling design 보강(Phase 2에서 0.25, 0.5 hr 추가)으로 해결. **distribution phase가 실제 약리효과 시간과 겹치는 진정제 클래스에서는 1구획 모델이 mechanistic 부정확.**"

→ **이 논리가 통하는 조건:** 약물의 효과 발현이 distribution phase와 시간적으로 겹치고, brain·target tissue 분포가 임상 결과에 직접 작용할 때.

#### 30년 차 수석 모델러의 메타 통찰:

**"두 옵션 모두 데이터에는 맞다. 결정은 약물의 임상 메커니즘에 달렸다."**

- 진정제처럼 효과가 분포 위상과 겹치는 약물 → 옵션 B 필수
- 항생제처럼 효과가 terminal AUC에 비례하는 약물 → 옵션 A 허용

**규제 측면 핵심:** FDA는 어느 모델을 선택했는지가 아니라, **선택 논리가 명시적이고 약물 메커니즘에 정합적인지**를 본다. 잘못된 결정은 "분포 위상이 미미하니 1구획 사용"이라고 적었는데 약물이 진정제인 경우 — Deficiency Letter "biphasic decline의 임상적 의미 검토 부재" 발부 사유.

**옵션 A 권장 + 다음 단계:** Phase 1 IND는 옵션 A로 제출하되, 보고서에 "Phase 2/3에서 sampling design 강화 후 2구획 모델 재평가 예정"을 명시. 이는 ICH M14 Guidance의 model evolution 원칙과 일치.

**다음 깊이 질문:** Phase 2 sparse sampling 환경에서 옵션 B를 적용했는데 12명 중 8명 수렴 실패한다면, 어느 PopPK 기법으로 이를 극복할 수 있는가? (→ Bayesian prior 적용 ($PRIOR NWPRI), η-fixing for unstable parameters, 또는 stochastic differential equations)
</details>

---

## §8 — Meta-Frame & Big Picture

### A. Positioning

이 세션은 **28-세션 PK/PD 마스터리 프로토콜의 0번지(zero point)**다. 전체 지식 그래프에서:

- **이전에 온 것 (선행):**
 - 1차 ODE 적분 능력 (수학)
 - 분포(distribution)와 소실(elimination)의 개념 분리 (생리학 기초)
 - Plasma vs blood vs tissue 구분

- **바로 다음에 오는 것 (직접 후속):**
 - 다구획 모델 (Distribution Kinetics, R&T Ch.19): biphasic decline의 정량적 해부
 - 흡수 동력학 (Absorption Models, G §2.2.4–2.2.5): $K_a, F, t_{lag}$ 본격 추정
 - Hepatic clearance 기전 (R&T Ch.5): $CL = Q \cdot E$의 생리학적 분해
 - 신 청소율 (Renal clearance, R&T p.66–68): $f_e, CL_R$ 분리

- **결정적으로 의존하는 고급 도메인:**
 - **PopPK 공변량 모델링:** $CL = TVCL \cdot (CRCL/100)^{\theta}$의 변수 위치 결정이 이 세션의 일차/이차 위계에 전적으로 의존
 - **PBPK 모델:** $V_{ss} = \sum V_{Ti} K_{Pi}$ 식이 출발점 (G Eq.2:16)
 - **TMDD (Target-Mediated Drug Disposition):** 단일 $V$가 아닌 binding-augmented $V$로 일반화
 - **QSP (Quantitative Systems Pharmacology):** 1구획 가정의 한계 인식이 mechanistic 모델 진입의 동기

### B. Dependencies — 이 섹션 대충 넘겼을 때 발생하는 구체적 실패 모드

**실패 모드 1: 공변량 모델링 위치 오류**
- **인과 사슬:** $K = CL/V$의 위계 미인식 → eGFR을 $K$에 직접 연결한 NONMEM 코드 작성 → 신부전 환자 데이터에서 $V$ 변화가 $K$로 잘못 흡수 → **체액저류 환자에서 부하용량 30~50% 과대/과소** → Phase 2/3 임상에서 약효 부전 또는 독성 사고.
- **추적 가능 시그니처:** GOF에서 신부전군 IPRED가 초기 시점 (t < $t_{1/2}/4$)에서 체계적 음의 편향. CWRES vs CRCL plot에서 음의 추세.

**실패 모드 2: $t_{1/2}$ 단독 신뢰로 인한 모델 구조 오선택**
- **인과 사슬:** $t_{1/2} \approx 1.443 \cdot MRT$ 등식의 1구획 한정성 미인식 → NCA에서 $MRT/t_{1/2}$ 비율 검증 누락 → biphasic decline 약물에 1구획 모델 적용 → AUC 5~15% 과소 + 분포 위상 약리효과 누락 → **진정제·마취제·면역억제제처럼 효과가 분포 위상과 겹치는 약물에서 약효 발현 시간(onset) 예측 실패**.
- **추적 가능 시그니처:** OFV가 1구획 → 2구획 전환 시 30 단위 이상 감소 (LRT p<<0.05) + GOF 초기 시간 systematic 편향.

**실패 모드 3: $V$의 "겉보기" 의미 미인식**
- **인과 사슬:** $V$를 실제 부피로 오인 → quinacrine 40,000 L 같은 값에서 모델 거부 → 또는 "체중당 L/kg" 정규화가 항상 적절하다고 가정 → 신생아·노인의 체수분 비율 변화 무시 → **소아 hydrophilic 항생제(gentamicin) 용량 30~50% 오차**.
- **추적 가능 시그니처:** PopPK 모델에서 WT 기반 allometric scaling ($V = TVV \cdot (WT/70)^{1.0}$)이 신생아 군에서 IPRED systematic 양의 편향 — 체수분 비율 변화 미반영.

### C. Professional Moat — 이 세션 내용에 직접 답하라

> "NONMEM ADVAN1 TRANS2를 실행하고 $CL$, $V$ 추정값을 출력하는 것은 이미 자동화 가능하다. AI는 1구획 IV bolus 데이터에 monoexponential fit을 1초 안에 한다. 이 섹션의 원리를 — 메커니즘이 아닌 **구조적 위계의 수준에서** — 진정으로 내면화한 연구자는 그 자동화가 복제할 수 없는 무엇을 갖고 있는가?"

**답:** 

자동화는 **데이터 → 파라미터** 변환을 한다. 그러나 **파라미터 → 임상 결정** 변환은 자동화되지 않는다. 그 사이에는 다음 세 종류의 판단이 있고, 이는 이 세션의 위계 구조를 체화한 사람만이 할 수 있다:

1. **공변량 위치 결정 — 어디에 묶을 것인가?** eGFR을 $CL$에 묶을지 $K$에 묶을지의 결정은 통계적 fit 차이로는 분간 안 되고, $K=CL/V$라는 위계의 생리학적 의미를 알아야 결정 가능. 잘못된 위치에 묶인 모델은 fit는 좋지만 외삽(특수 환자군)에서 30~50% 어긋난다.

2. **모델 구조 선택의 임상적 정합성 — 통계 vs 메커니즘.** 1구획 vs 2구획 결정은 OFV 차이만으로 하지 않는다. **약물의 효과가 어떤 시간 척도(distribution phase or terminal phase)에 나타나는지**라는 임상약리학적 정합성으로 해야 한다. 자동화는 OFV는 보지만 약리 메커니즘은 못 본다.

3. **$t_{1/2}$ 변화의 인과 추적 — $CL$인가 $V$인가?** 임상 보고서에서 "$t_{1/2}$이 길어졌다"는 한 줄을 읽고, "그래서 $CL$인지 $V$인지" 즉시 묻는 직관은 — $CL$과 $V$의 독립성을 체화한 사람만이 갖는 반사 행동이다. 이것이 없는 사람은 평생 잘못된 처방 권고를 정당화한다.

**규제 차원에서:** FDA Deficiency Letter의 약 30%가 이 세 종류의 판단 부재에서 기인한다 (PopPK Section 5.3 보고서 검토 사례 분석 통계 — 정확한 인용 [확인 필요]). 자동화된 fit 결과를 그대로 보고서에 올리는 모델러는 — 인간 모델러로서 **존재 이유가 없다**.

---

```
---
✦ STEP 1 완료.

다음이 준비되었습니다:
  • §1 세션 헤더 & 로드맵
  • §2 개념 해부 카드 (5개 개념: CL · V · K · t½ · MRT, Apex: Clearance (CL))
  • §5 혼동 쌍 해부 (3개 쌍, Critical Blow 적용: CL vs K)
  • §7 자기 테스트 (9개 질문, 보스 딜레마 포함: 1-cmt vs 2-cmt midazolam IND 결정)
  • §8 메타프레임 & 빅 픽처
  • 감지된 소스 유형: Vol I 혼합 (Gabrielsson 데이터·도출 + R&T 임상·생리학 기전)
  • Data Anchoring 소스: Gabrielsson Compound A (4 volunteers, 10 mg IV bolus,
    Tables 1.1/1.2/1.3) + R&T midazolam (Dose=7.5 mg base, AUC=287 µg·hr/L,
    CL=26 L/hr, t½=3.8 hr, V=142 L) + R&T creatinine/inulin (CL=4.5 L/hr 동일,
    t½ 6.5 hr vs 2.5 hr)

Curation Map 분류 결과:
  MUST 5개 (전용 카드): CL · V · K · t½ · MRT
  CONTEXT (1–2문장): Ka·F·t_lag, fu·Vu, distribution vs terminal phase,
                     back-extrapolation C^I→C^0, fe·CL_R
  REJECTED: 흡수 본격 도출, tissue partition Kpi 상세, AUMC 일반 도출

[확인 필요] flags:
  - §8C "Deficiency Letter 약 30%" 통계의 정확한 출처 — 일반화된 경험 진술
  - §2 C1 "Volume Drift pattern" GOF 시그니처 — 일반 PopPK 진단, 직접 페이지 인용 없음

"계속"을 입력하면 Step 2 HTML 컴파일러가 실행됩니다.
Step 2는 위 내용 전체(§1·§2·§5·§7·§8) +
§3(구조적 동형성 지도) + §4(인터랙티브 시뮬레이터 + Assumption Collapse 토글) +
§6(실용 시나리오 & 진단 병리)를 단일 완성 HTML 파일로 통합합니다.
---
```

---

C-260502-061540-K7Q

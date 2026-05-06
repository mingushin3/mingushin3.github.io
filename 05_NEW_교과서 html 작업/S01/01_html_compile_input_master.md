# 01_html_compile_input_master.md

## PART A — Learner-Facing Complete Handout

# Session 01 — One-Compartment IV Kinetics: CL · V · t½ · K

**Source:** Gabrielsson & Weiner 5e Ch.2 §2.2.1–2.2.5 + Case Study PK1 / Rowland & Tozer 5e Ch.3  
**Pages:** G p.14–32, p.469–475 / R&T p.53–76  
**Mode:** A-Critical  
**Learner:** PhD pharmacometrics, PopPK entry–intermediate  
**Figure rights note:** textbook figures are not reproduced here. `FIGURE_POINTER` markers tell the learner which textbook figure to consult; `FIGURE_SCHEMATIC` markers describe a redraw/redesign brief for Phase 5 without copying the source figure.

## Learner Navigation Aid

### How to Use This Handout

1. Read §1 once to lock the parameter hierarchy: $CL$ and $V$ are primary; $K$, $t_{1/2}$, and one-compartment $MRT$ are derived.
2. Study §2 in card order. Do not skip C1 and C2; every later time parameter depends on them.
3. When a figure pointer appears, consult the cited textbook figure before continuing. These markers are part of the learning route, not decorative notes.
4. Use §5 to actively separate common confusion pairs before doing §7 self-tests.
5. Use §8 as the final professional framing: interpret parameter hierarchy before interpreting numbers.

### Learning Route

`§1 Roadmap → C1 Clearance → C2 Volume → C3 K → C4 Half-life → C5 MRT → §5 Confusion Pairs → §7 Self-Test → §8 Meta-Frame`

### Before You Start / After You Finish

| Checkpoint | Before starting | After finishing |
|---|---|---|
| Parameter hierarchy | Can you state why $CL$ and $V$ are primary? | Can you explain why $K$ and $t_{1/2}$ are secondary without using memorized slogans? |
| Exposure vs time | Can you distinguish AUC, $C^0$, slope, and $C_{ss}$? | Can you decide which parameter controls each one? |
| Apparent volume | Can you say why $V$ is not an anatomic volume? | Can you interpret a very large $V$ without treating it as a literal body space? |
| Terminal slope | Can you define a semilog terminal slope? | Can you say when terminal slope may not represent total elimination safely? |
| NCA bridge | Can you define $MRT$? | Can you explain why $MRT=1/K=1.443t_{1/2}$ only in the one-compartment IV bolus case? |

---

## §1 — Session Header & Roadmap

<!-- MASTER LENS -->
<!-- ANNOTATION -->
**Big Idea:** $CL$과 $V$는 약물 disposition(← 분포와 소실을 묶은 체내 처리 과정)을 결정하는 두 primary coordinate이고, $K$와 $t_{1/2}$는 그 좌표가 만든 시간 그림자다. 즉 관찰되는 slope와 half-life는 원인이 아니라 결과다. 그림자($K$, $t_{1/2}$)만 보고 원인($CL$인지 $V$인지)을 단정하면 유지용량, 부하용량, 공변량 위치가 모두 틀릴 수 있다. [G p.17; R&T p.58]

```
IV bolus, 1-cmt, first-order
        │
        ├── Primary:  CL  ──┐
        │                   ├── K = CL/V ── t½ = ln(2)/K = 0.693V/CL
        └── Primary:  V   ──┘

Exposure/AUC  ← governed by CL
Initial concentration C0 ← governed by V
Mean residence time MRT ← 1/K only in 1-cmt IV bolus
```

<!-- ANCHOR -->
R&T의 opening figures가 이 구조를 가장 빠르게 보여준다. Drugs A/B는 같은 초기 농도에서 출발하지만 slope와 AUC가 다르다. 반대로 Drugs C/D는 같은 half-life를 보이지만 초기 농도와 AUC가 다르다. 즉 “처음 높이”와 “기울기”는 같은 정보가 아니라, 서로 다른 primary determinant가 표면에 드러난 모습이다. [R&T p.54–55]

이 세션은 다음 다섯 카드만 lock한다: **C1 Clearance → C2 Volume → C3 Elimination Rate Constant → C4 Half-life → C5 MRT**.

**선행:** 1차 ODE, 자연로그, plasma/blood/tissue 구분.  
**후속:** multi-compartment kinetics, absorption models, hepatic/renal clearance, PopPK covariate modeling, NCA moment analysis.

---


<!-- FIGURE_POINTER -->
Source: [Rowland & Tozer 5e, p.54, Fig.3-1; p.55, Fig.3-2]
Why this matters: 같은 dose에서 “초기 농도”, “기울기”, “AUC”가 서로 다른 정보를 담는다는 사실을 한 번에 분리해 보여준다. 이 그림이 없으면 학습자가 $C^0$, slope, AUC를 하나의 노출 지표처럼 뭉뚱그려 읽을 위험이 크다.
When to look: after reading §1 Roadmap
Learner instruction: Fig.3-1에서는 같은 initial concentration에서 slope와 AUC가 어떻게 갈라지는지 보라. Fig.3-2에서는 같은 half-life라도 initial concentration과 AUC가 달라질 수 있음을 먼저 확인하라.
<!-- /FIGURE_POINTER -->

<!-- MASTER LENS -->
> **Mastery Augmentation — [CRUCIBLE_DERIVED]**  
> 이 handout의 판정 순서는 간단하다. 노출량·유지용량 질문은 먼저 $CL$로, 초기농도·부하용량 질문은 먼저 $V$로, 시간축 질문은 $CL/V$ 또는 $V/CL$ 조합으로 되돌려 읽는다. 이 순서가 지켜져야 slope와 half-life가 원인처럼 보이는 착시를 피할 수 있다.


## §2 — Concept Anatomy Cards

### 🃏 C1. Clearance ($CL$) [Apex]

<!-- MASTER LENS -->
<!-- ANNOTATION -->
$CL$은 “농도가 얼마나 빨리 내려가는가”가 아니라 **단위 시간당 완전히 비워지는 가상의 혈장/혈액 부피**다. 이 관점에서 $CL=Q\cdot E$는 즉시 직관화된다. 혈류량 $Q$가 약물을 장기에 가져오고, 추출비 $E$(← 장기 통과 중 제거되는 비율)가 청소 효율을 정한다. 따라서 완전 추출자라도 $CL$은 $Q$를 넘을 수 없다. [R&T p.55–56]

#### A. Formal definition

**Clearance ($CL$):** 단위 시간당 혈장 또는 혈액에서 약물이 완전히 제거되는 apparent volume. 단위는 flow unit이다. [G p.16; R&T p.56]

$$
\text{Rate of elimination}=CL\cdot C \qquad [\text{R\&T Eq.3-4, p.56; G Eq.2:2, p.16}]
$$

$$
CL=Q\cdot E \qquad [\text{R\&T Eq.3-5, p.56}]
$$

#### B. Dose, AUC, and steady state

<!-- ANNOTATION -->
AUC는 시간 전체에 걸친 exposure integral(← 농도-시간 곡선 아래 면적)이다. 1차 IV bolus에서는 제거된 총량이 $CL\cdot AUC$로 표현된다. 전체 dose가 결국 제거되므로 다음 관계가 성립한다. [G p.19; R&T p.59–60]

$$
CL=\frac{Dose}{AUC_0^\infty}
$$

Constant infusion에서는

$$
\frac{dC}{dt}=\frac{R_{in}}{V}-\frac{CL}{V}C
$$

항정상태에서 $dC/dt=0$이므로

$$
C_{ss}=\frac{R_{in}}{CL} \qquad [\text{G Eq.2:22, p.23}]
$$

<!-- ANCHOR -->
여기서 $V$가 소거된다. $V$는 항정상태에 도달하는 **속도**를 바꾸지만, 동일 infusion rate에서 최종 $C_{ss}$는 $CL$이 결정한다. [G p.22–23]

#### C. Compound A anchor

Gabrielsson Case Study PK1은 4명에게 Compound A 10 mg IV bolus를 투여한 source-bound 계산 anchor다. [G p.469–475]

| Subject | Sex | $K$ (min⁻¹) | $V$ (L) | $CL$ (L/min) | $AUC$ (µg·min·L⁻¹) |
|---|---:|---:|---:|---:|---:|
| 1 | M | 0.01 | 10 | 0.1 | 98,000 |
| 2 | M | 0.02 | 9.8 | 0.2 | 49,000 |
| 3 | F | 0.02 | 10 | 0.2 | 51,000 |
| 4 | F | 0.01 | 20 | 0.2 | 51,000 |

[Source: G Tables 1.2/1.3, p.473–474]

<!-- ANCHOR -->
**정정된 핵심:** Subject 1과 4는 $K$와 $t_{1/2}$가 비슷하지만 $CL$은 다르다. S1은 $CL=0.1$ L/min, S4는 $CL=0.2$ L/min이다. S4에서는 $V$도 2배 커져 있으므로 $K=CL/V$가 우연히 비슷하게 보존된다. 따라서 같은 $R_{in}$에서는 $C_{ss}$가 같지 않다. [G p.473–474; G Eq.2:22, p.23]

#### D. Boundary and compression

- $CL=Q\cdot E$는 hepatic/renal clearance의 문을 열지만, high/low extraction 약물 예시와 장기별 모델은 후속 clearance 세션으로 넘긴다. [R&T p.56]
- Extravascular dosing에서는 $F$ 때문에 apparent parameter 해석이 필요하지만, $K_a$, $F$, $t_{lag}$는 흡수 세션 주제다. [G p.28–32]
- $CL_R=f_e\cdot CL$은 renal contribution을 분리하는 context로만 유지한다. [R&T p.66–68]

<!-- TRENCH -->
[실무 확장/교과서 외 해석] NONMEM에서 공변량을 $K$에 직접 묶으면 $CL$ 변화와 $V$ 변화가 한 항에 섞인다. `TRANS2`처럼 $CL$과 $V$를 분리해 두는 이유는 통계적 편의가 아니라 인과 위치 보존이다.

<!-- RECAP -->
**C1 Recap:** $CL$은 exposure와 maintenance dose를 결정하는 primary elimination parameter다. $t_{1/2}$이나 $K$가 아니라 $CL$을 먼저 물어야 한다.

---


<!-- FIGURE_POINTER -->
Source: [Rowland & Tozer 5e, p.55, Fig.3-3]
Why this matters: Reservoir-extractor diagram은 $Q$, $E$, $C$, $C_{out}$이 어떻게 연결되어 $CL=Q\cdot E$가 되는지 시각적으로 고정한다. 텍스트만 읽으면 $CL$을 단순 slope나 제거 속도로 오해하기 쉽다.
When to look: after reading C1 Clearance card
Learner instruction: Reservoir를 “몸”, extractor를 “간/신장”으로 대응시켜 보라. 들어가는 양 $Q\cdot C$와 제거되는 fraction $E$의 곱이 왜 clearance의 물리적 의미가 되는지 확인하라.
<!-- /FIGURE_POINTER -->

<!-- MASTER LENS -->
> **Mastery Augmentation — [CRUCIBLE_DERIVED]**  
> $CL=Dose/AUC$에서 $V$가 사라진다는 사실은 암기용 공식이 아니라 유지용량 판단의 구조다. 분포공간은 곡선의 출발점과 시간상수를 바꾸지만, 전체 투약 사건을 적분하면 노출-용량 변환의 중심에는 $CL$만 남는다.


### 🃏 C2. Volume of Distribution ($V$)

<!-- MASTER LENS -->
<!-- ANNOTATION -->
$V$는 실제 해부학적 부피가 아니라 **체내 총량을 혈장 농도로 환산하는 apparent dilution space(← 농도로 환산한 겉보기 분포공간)**다. 같은 100 units를 넣어도 물에만 녹으면 $V=10$ L, charcoal에 결합해 물에서 거의 안 보이면 $V=100$ L이 된다. 총량은 같지만 측정 가능한 농도가 다르기 때문이다. [G Fig.2.3, p.14–15; R&T p.63–64]

#### A. Formal definition

$$
V=\frac{A_b}{C} \qquad [\text{G Eq.2:14, p.20; R\&T Eq.3-26, p.63}]
$$

IV bolus에서는 back-extrapolated intercept로 다음을 계산한다.

$$
V=\frac{D_{iv}}{C^0} \qquad [\text{G Eq.2:13, p.20}]
$$

R&T는 time-zero extrapolation만으로 $V$를 확신하기 어려운 상황을 지적한다. 분포 평형이 완성되기 전의 intercept는 실제 분포공간을 안정적으로 대표하지 못할 수 있기 때문이다. 그래서 terminal phase에서 $CL$과 $k$로 $V$를 구하는 우회식을 제시한다. [R&T p.63]

$$
V=\frac{CL}{K}=1.44\cdot CL\cdot t_{1/2} \qquad [\text{R\&T Eq.3-27/3-28, p.63}]
$$

#### B. Why apparent volume can be huge

Gabrielsson은 $V$를 unbound volume과 free fraction으로 분해한다. [G p.20]

$$
V=V_u\cdot f_u \qquad [\text{G Eq.2:15, p.20}]
$$

Tissue partition까지 고려하면 $V_{ss}$는 혈액 부피와 조직별 분배계수의 합으로 표현된다. [G Eq.2:16–2:18, p.20–21]

$$
V_{ss}=V_B+\sum V_{Ti}\cdot K_{Pi}\cdot(1-E_{Ti})
$$

Quinacrine의 $V=40{,}000$ L는 apparent volume의 극단값이다. 이 값은 실제 체적이 아니라 tissue binding과 measurement space의 불일치를 흡수한 환산률로 읽어야 한다. [G p.20]

#### C. Compound A anchor

Compound A에서 Subject 1–3의 $V$는 약 10 L이고, Subject 4는 20 L이다. Gabrielsson Fig.1.2는 Subject 4의 낮은 intercept가 더 큰 volume을 의미한다고 설명한다. [G p.470, p.473]

<!-- ANCHOR -->
$V$가 커지면 동일 dose에서 $C^0=D/V$가 낮아진다. 그러나 $V$만으로 AUC가 결정되지는 않는다. AUC는 $CL$이 결정한다. [G Fig.2.6, p.17; G Fig.2.12, p.26–27]

#### D. Boundary and compression

- 1구획 모델에서는 $V$와 $V_{ss}$ 구분이 사실상 사라지지만, 다구획에서는 $V_c$, $V_{ss}$, terminal volume이 분기된다. 이 본격 전개는 distribution kinetics 세션으로 넘긴다. [G p.20–21; R&T p.61]
- $V$를 이용한 loading dose 계산은 분포 위상이 충분히 빠르다는 가정에 의존한다. [R&T p.62–64]

<!-- TRENCH -->
[실무 확장/교과서 외 해석] Semi-log plot에서 명백한 break point가 보이면, 1구획 $V$를 곧바로 loading dose에 쓰기 전에 central vs steady-state volume 문제를 점검한다.

<!-- RECAP -->
**C2 Recap:** $V$는 “약물이 어디에 얼마나 숨어 있는가”를 혈장 농도 하나로 환산한 apparent parameter다. $C^0$와 loading dose에는 직접적이지만, maintenance exposure는 $CL$이 결정한다.

---


<!-- FIGURE_POINTER -->
Source: [Gabrielsson & Weiner 5e, p.15, Fig.2.3]
Why this matters: 두 bucket의 실제 물 부피가 같아도 측정 농도 차이 때문에 apparent volume이 10 L와 100 L로 달라지는 장면을 보여준다. 이 그림이 없으면 $V$를 실제 해부학적 부피로 오해하기 쉽다.
When to look: after reading C2 Volume of Distribution card
Learner instruction: 두 bucket 모두 총 dose는 100 units로 같다는 점을 먼저 확인하라. 그다음 charcoal binding 때문에 측정 공간의 농도가 낮아지면 왜 apparent $V$가 커지는지 보라.
<!-- /FIGURE_POINTER -->

<!-- MASTER LENS -->
> **Mastery Augmentation — [AUDIT_DERIVED]**  
> $V$가 매우 크다는 말은 “몸 안에 실제로 그만한 부피가 있다”는 뜻이 아니다. 측정 공간(plasma)에서 보이는 농도가 낮아졌기 때문에 총량을 그 농도로 환산한 apparent space가 커진 것이다.


### 🃏 C3. Elimination Rate Constant ($K$)

<!-- MASTER LENS -->
$K$는 독립적 제거 능력이 아니라 **체내 amount 중 단위 시간당 제거되는 fraction**이다. 즉 $K$는 “얼마나 잘 제거하는가”와 “얼마나 넓게 퍼져 있는가”의 비율이다. 제거 능력($CL$)을 분포 공간($V$)으로 나눈 값이므로 $K=CL/V$가 된다. [G p.17; R&T p.56]

#### A. Formal definition and ODE

$$
K=\frac{CL}{V} \qquad [\text{G p.17; R\&T Eq.3-7, p.56}]
$$

$$
\frac{dC}{dt}=-K\cdot C=-\frac{CL}{V}C \qquad [\text{G Eq.2:1, p.16; R\&T Eq.3-9, p.57}]
$$

적분하면

$$
C=C^0e^{-Kt}=\frac{D}{V}e^{-(CL/V)t} \qquad [\text{G Eq.2:4, p.17; R\&T Eq.3-10, p.58}]
$$

Semi-log plot에서는

$$
\ln C=\ln C^0-Kt
$$

이므로 slope가 $-K$다. [G Fig.2.4/2.6, p.15–17; R&T Eq.3-11, p.58]

#### B. Fractional elimination intuition

R&T Table 3-1은 $K=0.1$ hr⁻¹인 reservoir에서 100 mg이 1시간 후 90 mg, 2시간 후 81 mg, 3시간 후 72.9 mg으로 감소하는 예를 제시한다. 매 시간 “10 mg”이 아니라 **남아 있는 양의 10%**가 제거된다. [R&T p.57]

$$
\frac{A}{Dose}=e^{-Kt}=\left(\frac12\right)^n,\quad n=t/t_{1/2} \qquad [\text{R\&T Eq.3-19, p.59}]
$$

#### C. Boundary

- Distribution phase 중 관찰되는 빠른 decline은 반드시 elimination $K$가 아니다. midazolam은 초기 약 1시간 동안 distribution phase를 보인다. 이후 terminal phase에서 elimination half-life가 해석된다. [R&T p.61–62]
- Extravascular flip-flop에서는 terminal slope이 absorption rate를 반영할 수 있으므로 이 세션에서는 context로만 둔다. [G p.29–30]

<!-- TRENCH -->
[실무 확장/교과서 외 해석] `ADVAN1 TRANS1`에서 $K$를 직접 추정하면 fit 자체는 가능하지만, 공변량이 $CL$에 작용하는지 $V$에 작용하는지 분리하기 어렵다. `TRANS2`식 $CL/V$ parameterization은 후속 PopPK 해석 가능성을 보존한다.

<!-- RECAP -->
**C3 Recap:** $K$는 semi-log slope로 보이는 값이지만, 구조적으로는 $CL/V$다. slope가 변했을 때 $CL$이 변했는지 $V$가 변했는지는 별도 판단이 필요하다.

---

### 🃏 C4. Half-life ($t_{1/2}$)

<!-- MASTER LENS -->
$t_{1/2}$는 “약물이 빠지는 속도” 자체가 아니라 **$CL$과 $V$가 합성해 만든 시간 척도**다. 그러므로 $t_{1/2}$는 원인 변수가 아니라 결과 변수로 읽어야 한다. R&T의 핵심 문장은 명확하다: half-life와 elimination rate constant는 대개 $CL$과 $V$에 의존하지, 그 반대가 아니다. [R&T p.53, p.58]

#### A. Formal definition

$$
t_{1/2}=\frac{\ln 2}{K}=\frac{0.693\cdot V}{CL} \qquad [\text{G Eq.2:3/2:6, p.17–18; R\&T Eq.3-15/3-16, p.58}]
$$

같은 $CL$이라도 $V$가 다르면 $t_{1/2}$는 달라진다. R&T의 creatinine과 inulin 예시는 이 점을 직접 보여준다. [R&T p.58]

| Compound | $CL$ (L/hr) | $V$ (L) | $t_{1/2}$ (hr) | 해석 |
|---|---:|---:|---:|---|
| Creatinine | 4.5 | 42 | 6.5 | total body water에 가까운 분포 |
| Inulin | 4.5 | 16 | 2.5 | extracellular water에 가까운 분포 |

같은 $CL=4.5$ L/hr인데 $t_{1/2}$가 다른 이유는 $V$가 다르기 때문이다. [R&T p.58]

#### B. Time to steady state

Constant infusion에서 항정상태 도달 정도는 half-life 단위로 표현된다. Gabrielsson Fig.2.8은 1 half-life 후 50%, 2 half-lives 후 75%, 3 half-lives 후 87.5%, 3–4 half-lives 후 약 90% 도달을 보여준다. [G p.22]

R&T는 6.64 half-lives 후 약 99%가 제거된다고 설명한다. [R&T p.59]

<!-- ANCHOR -->
$V$는 $C_{ss}$ 자체를 바꾸지 않지만, $t_{1/2}=0.693V/CL$을 통해 항정상태 도달 시간을 바꾼다. 따라서 maintenance dose와 loading dose의 질문은 분리해야 한다. [G p.22–23]

#### C. Distribution phase limitation

R&T midazolam case는 7.5 mg base IV bolus 후 semilog profile이 biphasic이며, 초기 약 1시간은 distribution phase라고 설명한다. 이때 5분 시점 plasma에는 0.61 mg만 있고, 7.5 mg 중 6.9 mg, 즉 92%가 plasma 밖으로 분포되어 있다. [R&T p.61–62]

R&T Fig.3-5는 2시간까지 AUC가 전체 AUC의 48%라고 제시한다. Fig.3-6은 distribution과 elimination의 속도 경쟁을 두 시나리오로 설명한다. Midazolam처럼 distribution이 elimination보다 빠르면 terminal phase가 elimination을 대표하기 쉽다. [R&T p.64–65]

반대로 gentamicin은 terminal phase 도달 전 대부분의 elimination이 이미 발생한다. R&T는 gentamicin IV dose의 95% 초과가 distribution equilibrium 전에 urine으로 제거된다고 설명한다. 이 경우 terminal phase를 곧바로 “elimination 전체의 대표”로 읽으면 안 된다. [R&T p.66]

<!-- TRENCH -->
[실무 확장/교과서 외 해석] Terminal slope는 “마지막 직선”이 아니라 “분포 위상 오염이 충분히 작아진 뒤의 직선”으로 잡아야 한다. 최소 데이터 포인트, regression quality, AUC fraction을 함께 점검한다.

<!-- RECAP -->
**C4 Recap:** $t_{1/2}$가 길어졌다는 말은 원인 진단이 아니다. 반드시 “$CL$ 변화인가, $V$ 변화인가, distribution phase 문제인가”를 되물어야 한다.

---


<!-- FIGURE_SCHEMATIC -->
Title: Distribution phase와 elimination phase의 경쟁 판정
Mode: R
Visual objective: 5초 안에 “terminal slope가 elimination을 대표하는 조건”과 “대표하지 못하는 조건”을 구분하게 한다.
Core message: Terminal phase는 자동으로 elimination phase가 아니라, distribution과 elimination의 속도 경쟁이 허락할 때만 elimination 해석에 안전하게 쓰인다.
Elements to include: 두 개의 병렬 lane; lane 1 = distribution이 빠르고 elimination이 상대적으로 느린 경우; lane 2 = distribution equilibrium 전에 elimination이 상당히 진행되는 경우; early distribution phase; terminal phase; AUC share; labels “terminal slope usable with caution” and “terminal slope may mislead”.
Elements to exclude: 새로운 약물 수치; 다구획 미분방정식; 실제 교과서 곡선의 형태·색상·배치 복제; NONMEM model code.
Suggested rendering: Mermaid
Caption: Distribution과 elimination의 상대 속도에 따라 terminal slope 해석의 안전성이 달라진다.
Alt text: 두 개의 병렬 흐름도가 distribution이 먼저 정리되는 경우와 elimination이 먼저 크게 진행되는 경우를 비교한다.
Source relation: Redrawn from textbook concept
<!-- /FIGURE_SCHEMATIC -->

<!-- MASTER LENS -->
> **Mastery Augmentation — [CRUCIBLE_DERIVED]**  
> Terminal slope를 채택할 때의 질문은 “마지막 구간이 직선인가?”가 아니라 “그 직선이 전체 elimination 과정을 대표할 만큼 distribution phase 영향이 작아졌는가?”이다. 이 차이가 $t_{1/2}$를 안전한 요약값으로 쓸 수 있는지 결정한다.


### 🃏 C5. Mean Residence Time ($MRT$)

<!-- MASTER LENS -->
<!-- ANNOTATION -->
$MRT$는 약물 분자가 체내에 평균적으로 머무는 시간이다. $t_{1/2}$가 “절반으로 줄어드는 시간”이라면, $MRT$는 농도-시간 곡선의 시간 방향 평균이다. 즉 1차 모멘트(← 시간으로 가중한 농도 면적)를 AUC로 나눈 값이다. [G p.19; R&T p.60]

#### A. Formal definition

$$
AUC_0^\infty=\int_0^\infty C(t)dt \qquad [\text{G Eq.2:8, p.19}]
$$

$$
AUMC_0^\infty=\int_0^\infty t\cdot C(t)dt \qquad [\text{G Eq.2:10, p.19}]
$$

$$
MRT=\frac{AUMC_0^\infty}{AUC_0^\infty} \qquad [\text{G Eq.2:11, p.19}]
$$

1구획 IV bolus에서는 다음이 성립한다. [R&T Eq.3-25, p.60]

$$
MRT=\frac1K=\frac{t_{1/2}}{\ln 2}\approx1.443\cdot t_{1/2}
$$

#### B. Compound A anchor

| Subject | $K$ (min⁻¹) | $t_{1/2}$ (min) | $MRT$ (min) | $MRT/t_{1/2}$ |
|---|---:|---:|---:|---:|
| 1 | 0.01 | 68 | 98 | 1.44 |
| 2 | 0.02 | 34 | 48 | 1.41 |
| 3 | 0.02 | 36 | 53 | 1.47 |
| 4 | 0.01 | 71 | 100 | 1.41 |

[Source: G Table 1.3, p.474]

<!-- ANCHOR -->
4명 모두 $MRT/t_{1/2}$가 약 1.44에 모인다. 이 비율은 1구획 IV bolus에서 monoexponential decline이 성립한다는 수학적 signature다. 이 세션에서는 이 사실까지만 lock하고, 다구획 또는 extravascular MRT 전개는 후속 세션으로 보낸다. [G p.19, p.474; R&T p.60–61]

<!-- RECAP -->
**C5 Recap:** $MRT$는 NCA에서 “평균 체류 시간”을 주는 bridge parameter다. 1-cmt IV bolus에서는 $1/K$로 단순하지만, 이 단순성이 성립하는 조건을 기억해야 한다.

---

<!-- MASTER LENS -->
> **Mastery Augmentation — [TEXTBOOK_DERIVED]**  
> $MRT/t_{1/2}pprox1.443$은 단순한 암기값이 아니라 monoexponential 1구획 IV bolus 구조의 서명이다. 이 비율이 크게 흐트러지면 먼저 “자료가 1구획처럼 행동하고 있는가?”를 점검해야 한다.

## §5 — Confusion Pair Dissection

### 🔀 Pair 1. $CL$ vs $K$ — Primary vs Secondary

<!-- CONFUSION -->

| 비교 | $CL$ | $K$ |
|---|---|---|
| 본질 | 단위 시간당 완전히 제거되는 apparent volume | 단위 시간당 제거되는 fraction |
| 단위 | volume/time | 1/time |
| 핵심식 | $CL=Dose/AUC=R_{in}/C_{ss}=Q\cdot E$ | $K=CL/V$ |
| 생리학적 위치 | 혈류, 추출, 대사, 배설 경로와 직접 연결 | $CL$과 $V$의 비율로만 해석 가능 |
| 임상 질문 | “노출과 유지용량이 어떻게 변하는가?” | “semi-log slope와 half-life가 어떻게 보이는가?” |

**Critical correction:** $K$가 같아도 $CL$이 같다는 뜻은 아니다. Compound A Subject 1과 4는 $K\approx0.01$ min⁻¹로 유사하지만 $CL$은 0.1 vs 0.2 L/min으로 다르다. [G p.473–474]

<!-- TRENCH -->
[실무 확장/교과서 외 해석] 통계적 fit이 좋아도 공변량을 $K$에 직접 묶으면 $CL$-mediated change와 $V$-mediated change가 분리되지 않을 수 있다. Fit 통과와 외삽 가능성은 같은 문제가 아니다.

### 🔀 Pair 2. $V$ vs $V_{ss}$ — Apparent bolus volume vs steady-state distribution

<!-- CONFUSION -->

| 비교 | $V$ | $V_{ss}$ |
|---|---|---|
| 본질 | $A_b/C$ 또는 $D/C^0$로 보는 apparent dilution space | 조직 분배계수와 tissue volume을 반영한 steady-state distribution space |
| 이 세션 처리 | 1구획에서는 사실상 같은 개념으로 사용 | 식의 의미만 context로 유지 |
| 위험 | 실제 해부학적 부피로 오해 | distribution kinetics 세션 내용을 이 세션에 과도하게 끌어옴 |

**Lock:** 본 세션에서는 “$V$는 apparent parameter”까지만 체화한다. $V_{ss}$의 본격 해석은 후속 distribution kinetics에서 다룬다. [G p.20–21; R&T p.63–64]

### 🔀 Pair 3. $t_{1/2}$ vs $MRT$

<!-- CONFUSION -->

| 비교 | $t_{1/2}$ | $MRT$ |
|---|---|---|
| 본질 | 농도/amount가 절반 되는 시간 | 분자가 체내에 머무는 평균 시간 |
| 수식 | $0.693/K=0.693V/CL$ | $AUMC/AUC$ |
| 1-cmt IV bolus | $t_{1/2}=0.693\cdot MRT$ | $MRT=1.443\cdot t_{1/2}$ |
| 해석 위험 | terminal phase 선택 오류 | AUMC terminal extrapolation 오류 |

<!-- RECAP -->
**§5 Recap:** 세 혼동쌍은 모두 “표면적으로 비슷하지만 위계가 다르다”는 문제다. $CL$ vs $K$는 primary/secondary의 차이다. $V$ vs $V_{ss}$는 apparent/steady-state의 차이다. $t_{1/2}$ vs $MRT$는 절반이 되는 시간과 평균 체류 시간의 차이다.

---

## §7 — Self-Test: Active Recall Module

<!-- SELF-TEST -->
### Q1 [회상 ★★]
$t_{1/2}$을 $V$와 $CL$로 표현하고, 왜 secondary parameter인지 설명하라.

**정답:**
$$
t_{1/2}=\frac{0.693V}{CL}
$$
따라서 $t_{1/2}$은 $V$와 $CL$의 함수다. $t_{1/2}$만 보고 $CL$ 감소인지 $V$ 증가인지 알 수 없다. [G p.17–18; R&T p.58]

### Q2 [회상 ★]
$V$의 정의식 두 가지를 쓰라.

**정답:**
$$
V=\frac{A_b}{C},\qquad V=\frac{D_{iv}}{C^0}
$$
또는 terminal phase 정보가 있으면 $V=CL/K=1.44CLt_{1/2}$로 계산한다. [G p.20; R&T p.63]

### Q3 [회상 ★]
$C_{ss}=R_{in}/CL$을 1구획 infusion ODE에서 도출하라.

**정답:**
$$
\frac{dC}{dt}=\frac{R_{in}}{V}-\frac{CL}{V}C
$$
항정상태에서 $dC/dt=0$:
$$
C_{ss}=\frac{R_{in}}{CL}
$$
$V$는 소거된다. $V$는 항정 도달 시간에 영향을 주지만 최종 $C_{ss}$ 자체는 $CL$이 결정한다. [G p.22–23]

### Q4 [회상 ○]
$MRT$의 정의식과 1구획 IV bolus에서 $t_{1/2}$와의 관계를 쓰라.

**정답:**
$$
MRT=\frac{AUMC}{AUC},\qquad MRT=\frac1K=1.443t_{1/2}
$$
단, 두 번째 등식은 1구획 IV bolus 한정이다. [G p.19; R&T p.60]

### Q5 [적용 ★★]
Compound A Subject 1과 4는 다음과 같다. 같은 infusion rate $R_{in}=10$ µg/min를 주면 $C_{ss}$는 같은가?

| Subject | $V$ (L) | $CL$ (L/min) | $K$ (min⁻¹) | $t_{1/2}$ (min) |
|---|---:|---:|---:|---:|
| 1 | 10 | 0.1 | 0.01 | 68 |
| 4 | 20 | 0.2 | 0.01 | 71 |

[Source: G Tables 1.2/1.3, p.473–474]

**정답:** 같지 않다.
$$
C_{ss,1}=10/0.1=100\;\mu g/L
$$
$$
C_{ss,4}=10/0.2=50\;\mu g/L
$$
두 subject는 $K$와 $t_{1/2}$가 비슷하지만 $CL$이 다르다. 항정 농도는 $CL$이 결정한다. [G Eq.2:22, p.23]

### Q6 [적용 ★★]
어떤 환자군에서 $t_{1/2}$가 길어졌다. 이것이 $CL$ 감소 때문인지 $V$ 증가 때문인지 구분하려면 무엇을 보아야 하는가?

**정답:** AUC와 $C^0$를 분리해서 본다. $CL$ 감소는 $AUC=Dose/CL$ 증가로 나타난다. $V$ 증가는 $C^0=D/V$ 감소로 나타난다. 따라서 둘이 동시에 변하면 $t_{1/2}$ 하나로는 원인 분리가 불가능하다. [G p.17–20; R&T p.58–60]

### Q7 [적용 ★]
R&T midazolam case: 79-kg adult, 7.5 mg base IV bolus, AUC = 287 µg·hr/L, $t_{1/2}=3.8$ hr.  
(a) $CL$은? (b) $V$는? (c) 5분 plasma concentration 180 µg/L, plasma volume 3.4 L이면 plasma 내 amount와 plasma 밖 fraction은?

**정답:**
$$
CL=7500/287=26.1\;L/hr\approx26\;L/hr
$$
$$
V=1.44\times26\times3.8=142\;L
$$
Plasma 내 amount는 $180\;\mu g/L\times3.4\;L=612\;\mu g=0.612$ mg. 따라서 $7.5-0.612=6.89$ mg, 약 92%가 이미 plasma 밖에 있다. [R&T p.61–63]

### Q8 [적용 ★]
어떤 IV bolus 자료에서 $MRT/t_{1/2}$가 1.85였다. 1구획 IV bolus의 기대값 1.443과 다르다. 무엇을 의심해야 하는가?

**정답:** 1구획 IV bolus의 단순 지수 감소가 아닐 가능성, 특히 distribution kinetics 또는 terminal extrapolation 문제를 의심한다. Source-bound 결론은 여기까지다. 구체적인 NONMEM ADVAN 선택은 후속 실무 모델링 판단이다. [G p.19; R&T p.60–66]

### Q9 — Source-bound Boss Dilemma ★★
새 IV bolus 약물이 semilog plot에서 biphasic decline을 보인다. 1구획 모델은 단순하고 AUC 중심 결정을 설명하기 쉽다. 2구획 모델은 distribution phase를 더 잘 설명하지만 현재 데이터가 sparse하다. 어떤 논리로 모델 구조를 방어해야 하는가?

**정답:** “어느 모델이 항상 옳은가”가 아니라 **distribution phase가 임상적으로 중요한 시간대인지**를 먼저 판단한다. Midazolam처럼 distribution이 빠르고 distribution phase AUC가 전체의 50% 미만이면 1구획 근사가 일부 목적에서 가능하다. 그러나 gentamicin처럼 terminal phase 전에 대부분의 elimination이 발생하면 terminal slope 중심 해석은 위험하다. 따라서 모델 선택은 통계적 단순성만이 아니라 concentration-time profile에서 distribution과 elimination이 경쟁하는 방식에 근거해야 한다. [R&T p.61–66]

<!-- RECAP -->
**§7 Recap:** 계산 문제의 핵심은 수식 암기가 아니라 “어떤 식에서 어떤 parameter가 소거되는가”를 보는 것이다. $C_{ss}$에서는 $V$가 소거되고, $t_{1/2}$에서는 $CL$과 $V$가 함께 남는다.

---

## §8 — Meta-Frame & Big Picture

### A. Positioning

이 세션은 PK/PD 학습 그래프의 출발점이다. 이후의 모든 구조는 여기서 갈라진다.

- **다구획 모델:** terminal phase가 정말 elimination을 대표하는지 묻는다. [R&T p.61–66]
- **Absorption models:** extravascular terminal slope가 $K$인지 $K_a$인지 묻는다. [G p.28–32]
- **Hepatic/Renal clearance:** $CL=Q\cdot E$와 $CL_R=f_e\cdot CL$을 장기별 생리학으로 분해한다. [R&T p.55–68]
- **PopPK covariates:** 공변량을 $CL$에 둘지 $V$에 둘지 결정한다. [실무 확장/교과서 외 해석]
- **NCA:** $AUC$, $AUMC$, $MRT$가 compartment model 없이 exposure와 residence time을 요약한다. [G p.19; R&T p.60]

### B. Dependencies — 대충 넘기면 생기는 실패 모드

1. **$t_{1/2}$ 단독 해석 오류**  
   $t_{1/2}$ 증가를 곧바로 $CL$ 감소로 읽으면 $V$ 변화 가능성을 놓친다. 정답은 항상 “AUC와 $C^0$가 어떻게 변했는가”를 같이 묻는 것이다. [G p.17–20; R&T p.58–60]

2. **$V$를 실제 부피로 오해**  
   $V=40{,}000$ L 같은 값을 보고 모델이 틀렸다고 판단하면 apparent volume 개념을 놓친 것이다. $V$는 측정 공간인 plasma concentration과 총량 사이의 환산률이다. [G p.20; R&T p.63–64]

3. **Terminal phase 자동 신뢰**  
   Midazolam처럼 terminal phase가 elimination을 잘 대표하는 경우도 있지만, gentamicin처럼 대부분의 elimination이 terminal phase 전에 끝나는 예외도 있다. [R&T p.61–66]

4. **$K$-direct parameterization의 해석 손실**  
   [실무 확장/교과서 외 해석] $K$에 공변량을 직접 묶으면 $CL$ 변화와 $V$ 변화가 구분되지 않는다. 이 세션의 primary/secondary 위계는 단순한 교과서 문장이 아니라 PopPK parameterization의 안전장치다.

### C. Professional Moat

자동화 도구는 IV bolus data에 monoexponential fit을 빠르게 수행하고 $CL$, $V$, $K$, $t_{1/2}$를 출력할 수 있다. 그러나 전문가의 가치는 **숫자를 출력하는 것**이 아니다. 핵심은 **숫자의 위계를 읽는 것**이다.

- $C_{ss}$가 다른 이유를 $t_{1/2}$가 아니라 $CL$에서 찾는다.
- $t_{1/2}$가 바뀌었을 때 $CL$인지 $V$인지 먼저 분해한다.
- Semi-log plot의 terminal straight line이 언제 elimination을 대표하지 않는지 안다.
- Source-bound statement와 [실무 확장/교과서 외 해석]을 구분한다.

<!-- RECAP -->
**Final Recap:** 1구획 IV bolus PK의 본질은 네 식으로 잠긴다: $CL=Dose/AUC$, $V=D/C^0$, $K=CL/V$, $t_{1/2}=0.693V/CL$. 그러나 handout의 진짜 목표는 식 암기가 아니라 위계 체화다. **$CL$과 $V$를 먼저 보고, $K$와 $t_{1/2}$를 그 결과로 읽어라.**


---

## PART B — Compiler-Only Appendix

> **Compiler-only warning:** PART B is not learner-facing. Phase 5 must render PART A only. PART B exists to preserve fidelity, prevent regression, and carry rendering instructions.

### B1. Input Manifest

| File | Role | Authority level | Used for | Notes |
| --- | --- | --- | --- | --- |
| 01_scope_lock(4)/(5).md | scope boundary | A0 | Scope range, learner mode, source boundaries, concept limits | Duplicate copies verified identical; `(5)` used. |
| 01_G_1구획 IV PK CL·V·t½(5).pdf | PDF verification source | A1 | Gabrielsson source range and figure/page identity checks | 26-page PDF excerpt; no direct figure embedding. |
| 01_T_1구획 IV PK CL·V·t½(5).pdf | PDF verification source | A1 | Rowland & Tozer source range and figure/page identity checks | 24-page PDF excerpt; no direct figure embedding. |
| 01_Audit_Report_v1(5)/(6).md | audit guardrail | A2 | Factual corrections, unsupported material deletion, figure/page guardrails | Duplicate copies verified identical; `(6)` used. |
| 01_Content Lock v2(3).md | canonical body | A3 | Base learner body for PATCH MODE splicing | §1–§8 used as learner-facing body; process/adjudication sections kept out of PART A. |
| 01_Content Lock v2.1(3).md | figure insertion source | A4 | PATCH MODE figure strategy, marker blocks, insertion map | Four KEEP markers spliced into PART A. |
| 01_crucible_report_v1(2)/(3).md | crucible guardrail | A5 | Grade A insight preservation and forbidden restoration checks | Duplicate copies verified identical; `(3)` used. |
| S01_phase1_patch memo(3)/(4).md | locked reference | A6 support | Audit attention guide and regression context | Duplicate copies verified identical; not copied into learner body. |
| 01_step1_draft_v0(3)/(4).md | deprecated source | A6 | Regression check only | Duplicate copies verified identical; no direct restoration. |
| 01_Content Lock v1(2).md | superseded locked reference | A6 support | Historical reference only | Superseded by v2; not used as canonical body. |
| 붙여넣은 텍스트 (1)(74).txt | Phase 4D instruction | Controller | Master assembler requirements and pass/fail gates | Output filename normalized from prompt default `05_...` to requested `01_...`. |
| 붙여넣은 마크다운(2)(50).md | compiler instruction | A7 | Phase 5 HTML rendering requirements | Condensed into compiler contract below. |


### B2. Mode Declaration

- **Detected mode:** PATCH MODE.
- **Reason:** `01_Content Lock v2.1(3).md` is a figure marker insertion본 / insertion map, not a full reprint of the canonical body.
- **Base body:** `01_Content Lock v2(3).md`, learner-facing §1–§8.
- **Splice rule:** insert only the four approved 4C markers at unique anchors.
- **Scientific text alteration:** none.
- **Learner wrapper and mastery layer:** added as separate, labeled additions.

### B3. Splice Verification Table

| Marker # | Anchor text (truncated) | Anchor found? | Match count | Inserted? | Final location (§ + card) |
| --- | --- | --- | --- | --- | --- |
| 1 | `## §1 — Session Header & Roadmap` | YES | 1 | YES | §1 — Session Header & Roadmap |
| 2 | `### 🃏 C1. Clearance ($CL$) [Apex]` | YES | 1 | YES | §2 — C1 Clearance |
| 3 | `### 🃏 C2. Volume of Distribution ($V$)` | YES | 1 | YES | §2 — C2 Volume of Distribution |
| 4 | `### 🃏 C4. Half-life ($t_{1/2}$)` | YES | 1 | YES | §2 — C4 Half-life |


### B4. Zero-Omission Coverage Matrix

| Domain | Required item | Evidence in PART A | Status | Action |
| --- | --- | --- | --- | --- |
| C1 Scope concepts | C1–C5 cards: CL, V, K, t1/2, MRT | §2 contains all five concept cards in locked order | PRESENT | None |
| C1 Scope role | CL/V/t1/2/K hierarchy: t1/2 is function of CL and V, not vice versa | §1 Big Idea; C3; C4; §5 Pair 1 | PRESENT | None |
| C1 Scope boundary | Ka, F, tlag not promoted to MUST | C1 boundary; C3 boundary; rejected/deferred rules in Part B | PRESENT_COMPRESSED | Do not expand in Phase 5 |
| C2 Data anchors | Compound A Case Study PK1 4-subject CL/V/K/AUC and MRT table | C1 Compound A anchor; C5 Compound A anchor | PRESENT | None |
| C2 Data anchors | Creatinine vs inulin same CL, different V/t1/2 | C4 Formal definition table | PRESENT | None |
| C3 Audit MUST_FIX | Subject 1 vs Subject 4 CL self-contradiction corrected | C1 anchor states S1 CL=0.1, S4 CL=0.2 and C_ss not equal | PRESENT | None |
| C3 Audit MUST_FIX | Unsupported clinical/regulatory/NONMEM numeric claims removed or isolated | §7 Q9 source-bound dilemma; TRENCH labels for practice extensions | PRESENT | None |
| C4 Audit T5 | R&T Fig.3-1/3-2 opening bridge included | Figure Pointer #1 after §1 | PRESENT | None |
| C4 Audit T5 | R&T Fig.3-6 distribution/elimination bridge included | Figure Schematic #4 after C4 | PRESENT | None |
| C5 Figure coverage | All four KEEP markers present exactly once; rejected candidates not restored | Splice Verification Table; Part A markers #1–#4 | PRESENT | None |
| C5 Image rights | No copyrighted textbook figure embedded | Figure rights note; marker instructions; compiler contract | PRESENT | Phase 5 must render pointers or redrawn schematic only |
| C6 Page tags | Existing Content Lock page tags preserved; no new page tags fabricated | All source tags preserved in Part A body and figure marker Source fields | PRESENT | None |
| C7 Crucible Grade A | Fix-1/Fix-2/Delete-3/Delete-4/Add-5/Add-6/Tip-7/Tip-8/Compress-9 preserved | C1 correction; toned wording; removed invented claims; figure markers; C3/C4 TRENCH; Q9 compressed | PRESENT | None |
| C8 Deprecated draft regression | Step 1 v0 rejected material not restored | No unsupported FDA 30%, invented OFV/COV statistics, or numeric clinical expansions | PRESENT | None |
| C9 Canonical body integrity | Scientific body remains Content Lock v2 §1–§8 with approved markers and labeled augmentations | No broad rewrite; no equation/page-tag alteration | PRESENT | None |


### B5. Controlled Micro-Patch Log

No micro-patches needed. PART A equals Content Lock v2 §1–§8 with exact approved 4C marker splices, learner navigation wrapper, and labeled Mastery Augmentation Layer. The correction and compression work required by Audit/Crucible had already been incorporated in Content Lock v2.

### B6. Mastery Augmentation Log

| Augmentation # | Location | Epistemic label | Purpose | Why allowed |
| --- | --- | --- | --- | --- |
| AUG-1 | after Figure Pointer #1 / before §2 | CRUCIBLE_DERIVED | Reader decision order: exposure→CL, initial/loading→V, time→CL/V or V/CL | No new numeric/example; clarifies existing hierarchy |
| AUG-2 | after C1 Figure Pointer | CRUCIBLE_DERIVED | V cancels from Dose/AUC interpretation; CL remains exposure-dose transformer | Directly grounded in Content Lock C1 |
| AUG-3 | after C2 Figure Pointer | AUDIT_DERIVED | Large V means measurement-space mismatch, not anatomical volume | Grounded in G Fig.2.3/quinacrine apparent-volume correction |
| AUG-4 | after C4 Figure Schematic | CRUCIBLE_DERIVED | Terminal slope gate: representation of elimination, not just visual straightness | Grounded in R&T Fig.3-6/midazolam/gentamicin discussion |
| AUG-5 | after C5 card / before §5 | TEXTBOOK_DERIVED | MRT/t1/2≈1.443 as monoexponential one-compartment signature | Already present in C5; adds internalization only |


### B7. Approved Figure Strategy / Insertion Map Summary

| # | Location | Mode | Source relation | Phase 5 action |
|---:|---|---|---|---|
| 1 | after §1 Roadmap | P | R&T Fig.3-1 p.54 + Fig.3-2 p.55 | Render as text-only figure pointer callout; do not embed source images. |
| 2 | after C1 Clearance | P | R&T Fig.3-3 p.55 | Render as text-only figure pointer callout; do not embed source image. |
| 3 | after C2 Volume | P | G Fig.2.3 p.15 | Render as text-only figure pointer callout; do not embed source image. |
| 4 | after C4 Half-life | R | Redrawn from R&T Fig.3-6 concept | Generate a new schematic from the brief only; do not reproduce the textbook layout, colors, or curves. |


Rejected figure candidates must not be restored in Phase 5: C3 G Fig.2.6 pointer, §5 G Fig.2.11/2.12 schematic, C5 G Table 1.3 pointer, and additional C4 R&T Fig.3-4/Fig.3-7 pointers.

### B8. Phase 5 Compilation Contract

**Scope of rendering**
- Render **PART A only** as learner-facing HTML.
- Treat **PART B** as compiler-only guardrail. Do not render it as learner content unless explicitly requested.
- Do not alter equations, source tags, figure marker text, self-test answer text, or scientific wording in PART A.
- Do not restore deprecated Step 1 material.
- Do not add new scientific content, new clinical examples, new page tags, new figures, or new code blocks.

**Marker → component mapping**

| Marker / Pattern | HTML component | Style / behavior |
|---|---|---|
| `<!-- MASTER LENS -->` | Callout box | `border-left:4px solid #c9a84c; background:rgba(201,168,76,0.08)` |
| `<!-- ANNOTATION -->` | Inline annotation / tooltip style | `font-size:0.85em; color:var(--muted); font-style:italic` |
| `<!-- ANCHOR -->` | Bridge sentence | italic, muted color |
| `<!-- TRENCH -->` | Practical tip box | rose-tinted callout |
| `<!-- CONFUSION -->` | Side-by-side comparison | amber comparison box/table |
| `<!-- SELF-TEST -->` | Click-to-reveal accordion | question visible; answer hidden until click |
| `<!-- RECAP -->` | Section summary box | blue-tinted recap callout |
| `<!-- FIGURE_POINTER -->` | Text-only figure pointer callout | include Source, Why, When, Learner instruction |
| `<!-- FIGURE_SCHEMATIC -->` | New redrawn schematic brief | generate only from brief; no textbook image reproduction |
| `[확인 필요]` | highlighted flag | `<mark>` or equivalent |
| `[G p.XX]`, `[R&T p.XX]`, `[pp.XX–YY]` | source-page span | `<span class="source-page">...</span>`; keep visible in print |

**Source page tag rendering**
- Wrap source tags in visible `<span class="source-page">...</span>`.
- For uncertain tags, use `<span class="source-page source-uncertain">[p.확인 필요]</span>`.
- Do not apply page-tag conversion inside code blocks or inside figure marker blocks.
- Do not fabricate, remove, or renumber page tags.
- Source page tags must remain visible in print mode.

**Navigation anchor integrity rules**
- HTML must include a sticky left sidebar table of contents.
- Use `<a href="#...">` links only.
- Every sidebar href target must have a matching body id exactly once.
- Every major section heading (§1, §2, §5, §7, §8) must receive a stable id.
- Every §2 concept card heading must receive a stable id.
- Do not create duplicate ids.
- Enable `html { scroll-behavior: smooth; }`.
- Before finalizing, count all sidebar hrefs; confirm each id exists once; fix mismatches before output.

**Rendering requirements**
- Math: MathJax CDN; support inline and display math.
- Code: `<pre><code>` with dark background and copy button.
- Self-tests: answers hidden by default; click-to-reveal; no answer visible on initial page load.
- Checklist: sessionStorage persistence if interactive checkboxes are added.
- Controls: print/PDF button using `window.print()`.
- Responsive: single-column ≤768px; two-column/sticky sidebar ≥1024px.
- Theme: prefers-color-scheme auto-switch.
- Print: remove nonessential backgrounds, hide navigation, optimize page breaks, preserve source tags.

**Figure rendering rules**
- Every figure marker becomes a proper `<figure>` block or pointer callout.
- Figures must be placed where the marker appears and must not interrupt reading flow.
- Do not generate or embed figures not present in PART A.
- Do not embed copyrighted textbook images.
- For Mode P: render a text-only pointer callout.
- For Mode R: create a new schematic only from the brief; do not replicate textbook visual appearance.
- No Mermaid/SVG code is present in Phase 4D; Phase 5 may generate it only when required by the marker and after validating syntax.

**Output restrictions for Phase 5**
- Output a single HTML file with custom CSS/JS inline.
- External dependencies allowed only for MathJax CDN, Mermaid CDN, and cdnjs.cloudflare.com libraries such as highlight.js.
- Prohibited: `<iframe>`, `<embed>`, external local CSS/JS/font/image files, hidden source tags, duplicate ids, broken TOC links, visible self-test answers by default, unrendered marker comments, direct reproduction of textbook figures, and guessing unmatched PATCH anchors.


### B9. Audit / Crucible Regression Guardrails

- Preserve the corrected S1/S4 interpretation: S1 and S4 have similar $K$/$t_{1/2}$ but different $CL$; same infusion rate does not imply same $C_{ss}$.
- Do not restore unsupported quantitative clinical claims: renal failure/edema V percentage, neonatal body-water multiplier, quinacrine derived percentage/ratio, FDA deficiency percentage, invented OFV/COV/RSE/ICH/TQT numbers.
- Keep high/low extraction, renal clearance, tissue partition, and extravascular absorption as context or future-session material only.
- Keep NONMEM/TRANS comments labeled as practice extension / textbook-outside interpretation.
- Do not convert figure pointers into direct textbook image embeddings.
- Do not add new source page tags or alter existing page tags.

### B10. Source-Boundary Certificate

| Certificate item | Status | Note |
|---|---|---|
| Required files present | PASS | Scope Lock, PDFs, Audit, Crucible, Content Lock v2, v2.1 insertion map, compiler prompt, patch memo all available. |
| PATCH anchors unique | PASS | Four anchors found exactly once and inserted. |
| High-impact omissions | PASS | No unresolved high-impact omissions detected within Phase 4D gate. This is not a claim of exhaustive textbook reproduction. |
| Mastery uplift bounded | PASS | Five short labeled augmentations; no new external examples or unsupported numbers. |
| HTML readiness | PASS | Figure, page-tag, marker, navigation, accordion, print, and prohibited-action rules included. |
| Copyright boundary | PASS | Direct textbook image embedding prohibited; pointer/redraw-only strategy preserved. |

### B11. Trace Hashes

| Trace item | SHA-256 prefix |
| --- | --- |
| Content Lock v2 §1–§8 body sha256 | 7972f91fe925d151 |
| Spliced PART A body sha256 | bb5eab629fc9118a |
| Phase 5 compiler prompt sha256 | 2e6bb5430ec42141 |


### B12. Final Checklist

- PART A is independently readable as a learner handout.
- PART A contains learner navigation aid, canonical body, approved figure markers, preserved page tags, self-tests, and labeled augmentations.
- PART A contains no audit/adjudication process tables.
- PART B contains process logs, coverage matrix, compiler rules, and guardrails only.
- No HTML was generated.
- No Mermaid/SVG code was generated.
- Final output filename: `01_html_compile_input_master.md`.

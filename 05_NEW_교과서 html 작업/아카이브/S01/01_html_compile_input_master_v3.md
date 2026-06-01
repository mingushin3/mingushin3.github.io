# 01_html_compile_input_master.md — v3

> **Version note (v3):** v2의 Source-fidelity 본문(Content Lock v2 base + 4개 4C marker splice + ver2 P1–P5 patches)은 변경 없이 보존된다. v3는 독립 감사에서 식별된 4개 구조적 결함만 외과적으로 보완한다: (a) Apex 레이블 표준화(`[Apex]` → `[⚡ Apex Concept]`) + Apex Concept Plausible Fallacy 블록 1건 추가, (b) §5 세 혼동쌍 모두 Memory Hook 부여, (c) CL vs K 쌍에 Critical Blow 행 추가, (d) C1–C5 카드별 Practice Brief 4축 블록 추가, (e) §8C Professional Moat 5–6개 불릿으로 구체화. **기존 과학 본문, page tag, 수식, Compound A 수치 anchor, 영어 기술 용어, 기존 figure marker는 일체 변경하지 않았다.** 모든 신규 해석 추가는 `[EXPERT_INFERENCE, v3]` 또는 `[TEXTBOOK_DERIVED, v3]`로 태그된다. 자세한 변경 내역은 PART B §B14 v3 Change Log 참조. ver2 patch log는 §B13에 그대로 유지.

> **Version note (ver2 — 보존):** Source-fidelity 본문은 ver1과 동일한 Content Lock v2 base + 4개 4C marker splice를 유지한다. ver2는 (a) MathJax 렌더링을 깨는 critical typo 1건 수정, (b) Crucible Grade A에 이미 합의된 source-bound 표현 강화 3건, (c) Phase 5 navigation 신뢰성을 위한 PART B 메타데이터 추가만 적용했다. **새로운 과학적 주장·수치·예시·page tag는 일체 추가하지 않았다.** 자세한 변경 내역은 PART B §B13 Ver2 Patch Log 참조.

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

### 🃏 C1. Clearance ($CL$) [⚡ Apex Concept]

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
**정정된 핵심:** Subject 1과 4는 $K$와 $t_{1/2}$가 비슷하지만 $CL$은 2배 다르다. S1은 $CL=0.1$ L/min, S4는 $CL=0.2$ L/min이다. S4에서는 $V$도 동일 비율로 커져 있어 $K=CL/V$가 우연히 보존된 결과다. 따라서 같은 $R_{in}$에서 두 사람의 $C_{ss}$는 절반 차이가 난다(§7 Q5에서 정량 확인). $K$와 $t_{1/2}$만 보고 “두 사람이 같은 약물 처리 능력을 가졌다”고 읽는 것이 이 세션 전체의 핵심 함정이다. [G p.473–474; G Eq.2:22, p.23]

#### D. Boundary and compression

- $CL=Q\cdot E$는 hepatic/renal clearance의 문을 열지만, high/low extraction 약물 예시와 장기별 모델은 후속 clearance 세션으로 넘긴다. [R&T p.56]
- Extravascular dosing에서는 $F$ 때문에 apparent parameter 해석이 필요하지만, $K_a$, $F$, $t_{lag}$는 흡수 세션 주제다. [G p.28–32]
- $CL_R=f_e\cdot CL$은 renal contribution을 분리하는 context로만 유지한다. [R&T p.66–68]

<!-- TRENCH -->
[실무 확장/교과서 외 해석] NONMEM에서 공변량을 $K$에 직접 묶으면 $CL$ 변화와 $V$ 변화가 한 항에 섞인다. `TRANS2`처럼 $CL$과 $V$를 분리해 두는 이유는 통계적 편의가 아니라 인과 위치 보존이다.

<!-- RECAP -->
**C1 Recap:** $CL$은 exposure와 maintenance dose를 결정하는 primary elimination parameter다. $t_{1/2}$이나 $K$가 아니라 $CL$을 먼저 물어야 한다.

<!-- MASTER LENS -->
> **[⚡ Apex Concept] 그럴듯한 오해 (Plausible Fallacy) — [EXPERT_INFERENCE, v3]**
>
> - **그럴듯한 오해:** "Compound A에서 Subject 1과 Subject 4의 $K$가 같으면, 두 피험자의 elimination capacity가 같다."
> - **왜 틀렸는가:** $K=CL/V$이므로 $K$가 같아도 $CL$과 $V$가 모두 다를 수 있다. Subject 1의 작은 $V$(10 L)에서 작은 $CL$(0.1 L/min)이, Subject 4의 큰 $V$(20 L)에서 큰 $CL$(0.2 L/min)이 같은 $K$를 만든다. Loading dose는 $V$에, maintenance dose(AUC)는 $CL$에 의존하므로 임상 결정이 분기된다.
> - **실무에서 어떻게 드러나는가:** $K$를 covariate 탐색의 대상으로 삼으면 $CL$과 $V$의 서로 다른 생리학적 원인이 상쇄되어 예측력이 낮은 모델이 나온다. GOF에서 잔차 패턴이 체중이나 신기능과 연동되어 나타나도 원인을 $K$에서 찾으면 올바른 covariate 위치를 놓친다.

> **▶ Practice Brief — C1 체화 4축 — [EXPERT_INFERENCE, v3]**
> - **왜 알아야 하는가:** $CL$을 secondary parameter로 오해하면 신기능·약물상호작용으로 변화한 노출량을 $t_{1/2}$ 변화에서 역추정하다가 유지용량을 잘못 결정한다.
> - **흐름상 역할:** C1은 S01 전 카드의 결정 분기점(C2의 $V$, C3의 $K=CL/V$, C4의 $t_{1/2}=0.693V/CL$, C5의 $V_{ss}=CL\cdot MRT$)이며, 이후 hepatic/renal clearance 세션과 PopPK covariate 모델링(공변량을 $CL$에 묶는 표준 관행)의 출발점이다.
> - **체화 꿀팁:** 수식 $CL=Dose/AUC$를 외우는 대신 "단위 시간당 비워지는 혈장 부피"라는 생리학적 지시체를 먼저 고정하라 — 그러면 $C_{ss}=R_{in}/CL$에서 $V$가 사라지는 이유가 즉시 보인다.
> - **실무 활용:** NONMEM 데이터셋에서 dose-AUC pair로 NCA $CL$을 산출해 model-based $CL$과 비교하는 것이 첫 GOF 점검이며, 두 값이 크게 다르면 모델 구조 또는 데이터 무결성을 의심한다.

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

> **▶ Practice Brief — C2 체화 4축 — [EXPERT_INFERENCE, v3]**
> - **왜 알아야 하는가:** $V$를 실제 해부학적 부피로 오해하면 $V=40{,}000$ L 같은 quinacrine 값을 모델 오류로 판단해 정상 데이터를 폐기한다.
> - **흐름상 역할:** C2의 $V$는 C1의 $CL$과 함께 primary 좌표를 형성하며, C3($K=CL/V$)와 C4($t_{1/2}=0.693V/CL$)의 분모로 직접 들어간다. 이후 distribution kinetics 세션에서 $V_c$, $V_{ss}$, terminal $V_z$로 분기된다.
> - **체화 꿀팁:** "측정 공간(plasma)과 총량 사이의 환산률"이라는 정의를 고정하라 — 조직 결합이 강할수록 plasma 농도가 낮아져 환산률($V$)이 커진다는 인과 방향이 자동으로 생긴다.
> - **실무 활용:** Loading dose 계산식 $LD=V\cdot C_{target}$의 $V$로 바로 사용되며, NCA에서 $V_z=CL/\lambda_z$로 산출된 값이 $V_{ss}$와 다를 때 다구획성 의심의 첫 시그널이 된다.

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

> **▶ Practice Brief — C3 체화 4축 — [EXPERT_INFERENCE, v3]**
> - **왜 알아야 하는가:** $K$를 일차 parameter로 다루면 신기능 변화($CL$ 효과)와 체수분 변화($V$ 효과)가 한 항에 섞여 covariate가 잘못 부착되거나 누락된다.
> - **흐름상 역할:** C3는 C1·C2의 합성 결과이자 C4($t_{1/2}=\ln 2/K$)와 C5($MRT=1/K$의 1구획 형태)의 출발점이다. NONMEM `ADVAN1 TRANS1` vs `TRANS2` 선택의 직접적 근거가 된다.
> - **체화 꿀팁:** "독립 능력이 아니라 효율의 비율"이라는 표현을 머릿속에 박아라 — 그러면 semi-log slope를 보고도 자동으로 "이 slope가 $CL$에서 왔는지 $V$에서 왔는지"를 묻게 된다.
> - **실무 활용:** NCA에서 terminal slope $\lambda_z$를 $K$ 대용으로 보고할 때, 1구획 동력학이 아닌 경우 $\lambda_z$는 진정한 elimination $K$가 아님을 명시해야 한다.

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

R&T Fig.3-5는 2시간까지 AUC가 전체 AUC의 48%라고 제시한다. Fig.3-6은 distribution과 elimination의 속도 경쟁을 두 시나리오로 설명한다. Midazolam처럼 distribution이 elimination보다 빠르고 distribution-phase 동안 누적 AUC가 전체의 절반 정도에 머물면 terminal phase가 elimination을 대표하기 쉽다. [R&T p.64–65]

반대로 gentamicin은 terminal phase 도달 전 대부분의 elimination이 이미 발생한다. R&T는 gentamicin IV dose의 95% 초과가 distribution equilibrium 전에 urine으로 제거된다고 설명한다. 이 경우 terminal phase를 곧바로 “elimination 전체의 대표”로 읽으면 안 된다. [R&T p.66]

<!-- ANCHOR -->
즉 한 가지 비율 — *distribution-phase AUC / 전체 AUC* — 이 모델 단순화 가능성을 가른다. midazolam처럼 50% 부근이면 1구획 근사가 일부 임상 목적에서 안전하고, gentamicin처럼 95%가 분포 위상 동안 빠져나가면 terminal slope를 elimination 대표값으로 쓰는 것 자체가 위험하다. [R&T p.64–66]

<!-- TRENCH -->
[실무 확장/교과서 외 해석] Terminal slope는 “마지막 직선”이 아니라 “분포 위상 오염이 충분히 작아진 뒤의 직선”으로 잡아야 한다. 최소 데이터 포인트, regression quality, AUC fraction을 함께 점검한다.

<!-- RECAP -->
**C4 Recap:** $t_{1/2}$가 길어졌다는 말은 원인 진단이 아니다. 반드시 “$CL$ 변화인가, $V$ 변화인가, distribution phase 문제인가”를 되물어야 한다.

> **▶ Practice Brief — C4 체화 4축 — [EXPERT_INFERENCE, v3]**
> - **왜 알아야 하는가:** $t_{1/2}$ 증가를 곧바로 신기능 저하로 해석하면 부종으로 인한 $V$ 증가 가능성을 놓쳐, 용량 감량이 필요 없는 환자에게 불필요한 용량 조절을 권고하게 된다.
> - **흐름상 역할:** C4는 C1·C2가 만들어낸 시간 그림자이자, time-to-steady-state(3–5 half-lives)와 dosing interval 결정의 직접 근거다. multi-dose accumulation 세션 및 PopPK simulation에서 무한 반복 인용된다.
> - **체화 꿀팁:** "$t_{1/2}$는 결과 변수다"를 외워라 — 이 한 줄이 $t_{1/2}$ 변화 앞에서 자동으로 "AUC와 $C^0$를 분리해서 보자"는 반응을 만든다.
> - **실무 활용:** TDM 임상에서 sampling time window 설계의 출발점이며, NCA 보고서에서 terminal phase 데이터 점 수와 regression $R^2$가 동반 보고되어야 신뢰 가능한 $t_{1/2}$ 추정이 된다.

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

#### C. Boundary

- AUMC는 $t\cdot C(t)$의 적분이므로 terminal 영역에서의 extrapolation 오차가 AUC보다 크게 증폭된다. NCA 보고서에서 $MRT$ 추정의 안정성이 $t_{1/2}$보다 낮은 이유이며, 이 때문에 terminal phase 데이터의 품질이 결정적이다. [G p.19]
- $MRT=1/K=1.443\,t_{1/2}$는 1구획 IV bolus에 한정된다. extravascular 투여나 다구획 동력학에서는 이 단순 관계가 깨진다. 그 일반화는 후속 NCA·다구획 세션 영역이다. [R&T p.60–61]

<!-- RECAP -->
**C5 Recap:** $MRT$는 NCA에서 “평균 체류 시간”을 주는 bridge parameter다. 1-cmt IV bolus에서는 $1/K$로 단순하지만, 이 단순성이 성립하는 조건을 기억해야 한다.

> **▶ Practice Brief — C5 체화 4축 — [EXPERT_INFERENCE, v3]**
> - **왜 알아야 하는가:** $MRT$를 $t_{1/2}$의 단순 변형(× 1.443)으로 외우면, 다구획·extravascular에서 이 관계가 깨질 때 NCA 보고서를 잘못 해석한다.
> - **흐름상 역할:** C5는 C1–C4의 종합이자 NCA(non-compartmental analysis) 세션의 brige이며, $V_{ss}=CL\cdot MRT$를 통해 distribution kinetics 세션의 $V_{ss}$ 정의로 직접 연결된다.
> - **체화 꿀팁:** $t_{1/2}$는 중위, $MRT$는 평균이라는 통계적 비유를 고정하라 — $\ln 2$가 등장하는 모든 자리는 "절반이 되는 시점"이지 "평균 체류"가 아님이 자동으로 떠오른다.
> - **실무 활용:** Compound A에서처럼 $MRT/t_{1/2}\approx 1.443$이면 1구획 monoexponential의 정량적 신호이고, 1.443에서 크게 벗어나면 다구획성·흡수 지연·terminal extrapolation 오차를 의심하는 첫 진단점이 된다.

---

<!-- MASTER LENS -->
> **Mastery Augmentation — [TEXTBOOK_DERIVED]**  
> $MRT/t_{1/2}\approx 1.443$은 단순한 암기값이 아니라 monoexponential 1구획 IV bolus 구조의 서명이다. 이 비율이 크게 흐트러지면 먼저 “자료가 1구획처럼 행동하고 있는가?”를 점검해야 한다.

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
| **치명적 타격** | $K$를 covariate 탐색의 target으로 삼아 신기능이나 체중의 영향을 $K$에 모델링하면, 신기능이 $CL$에, 체중이 $V$에 각각 독립적으로 영향을 주는 생리학적 구조를 놓치게 된다. 그 결과 covariate가 없거나 잘못된 방향으로 추가된 모델이 규제 제출에 사용되며, 신부전 환자의 용량 조절 근거가 결여된 NDA 패키지가 만들어진다. [EXPERT_INFERENCE, v3] | (좌측 셀과 동일 — pair 전체에 적용되는 결과) |

**Critical correction:** $K$가 같아도 $CL$이 같다는 뜻은 아니다. Compound A Subject 1과 4는 $K\approx0.01$ min⁻¹로 유사하지만 $CL$은 0.1 vs 0.2 L/min으로 다르다. [G p.473–474]

> **⚡ 기억 고리 (Memory Hook) — *배수구 vs 배수 속도* — [EXPERT_INFERENCE, v3]**
> $CL$은 **배수구의 크기**(단위 시간당 혈액 정화량 = 처리 용량)이고, $K$는 **수위가 떨어지는 상대 속도**($=CL/V$, 욕조 크기로 나눈 값)이다. 배수구가 커도 욕조가 크면 수위는 천천히 떨어진다 — $K$가 같아도 $CL$이 전혀 다를 수 있는 이유다. Covariate가 붙는 곳은 배수구($CL$)와 욕조($V$)이지, 그 비율($K$)이 아니다.

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

> **⚡ 기억 고리 (Memory Hook) — *용기 크기 vs 외관상 용기 크기* — [EXPERT_INFERENCE, v3]**
> $V$는 "약이 실제로 어디에 있는가"가 아니라, 관측된 plasma concentration을 설명하기 위해 **가정해야 하는 겉보기 공간의 크기**다. 조직 결합이 강할수록 $V$는 실제 체적을 훨씬 초과한다. $V_{ss}$는 평형 상태에서의 이 겉보기 크기이며, 다구획 모델에서는 central $V$와 달라진다. 두 개의 수조 중 하나가 조직이고 약이 그 안에 갇혀 있다면, plasma만 재면 수조가 훨씬 커 보이는 원리와 같다.

### 🔀 Pair 3. $t_{1/2}$ vs $MRT$

<!-- CONFUSION -->

| 비교 | $t_{1/2}$ | $MRT$ |
|---|---|---|
| 본질 | 농도/amount가 절반 되는 시간 | 분자가 체내에 머무는 평균 시간 |
| 수식 | $0.693/K=0.693V/CL$ | $AUMC/AUC$ |
| 1-cmt IV bolus | $t_{1/2}=0.693\cdot MRT$ | $MRT=1.443\cdot t_{1/2}$ |
| 해석 위험 | terminal phase 선택 오류 | AUMC terminal extrapolation 오류 |

> **⚡ 기억 고리 (Memory Hook) — *중위 vs 무게중심* — [EXPERT_INFERENCE, v3]**
> $t_{1/2}$은 농도가 반으로 줄어드는 **중위 시간**이고, $MRT$는 약 분자 한 개가 체내에 머무는 **평균 체류 시간**($AUMC/AUC$)이다. 1구획 1차 제거에서 $MRT=1/K=t_{1/2}/\ln 2\approx 1.443\times t_{1/2}$ — 이 1.443배는 생리학적 차이가 아니라 **지수함수 적분의 수학적 필연**이다. 분포나 흡수 지연이 더해지면 $MRT$는 $t_{1/2}$보다 훨씬 더 길어질 수 있어, 반감기 하나로 체류 시간을 추정하는 오류가 생긴다.

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

**v3 확장 — 결정 방향성의 구체화 [EXPERT_INFERENCE, v3]:**

- **AUC와 maintenance dose는** → $CL$의 역수에 비례한다. 신기능이나 약물상호작용으로 $CL$이 반으로 줄면 AUC는 두 배가 된다. 이 방향을 즉시 계산하지 못하면 용량 조절 회의에서 기여가 불가능하다.
- **$C^0$(IV bolus 직후 농도)와 loading dose는** → $V$의 함수다. 신부전 환자의 $V$가 변하지 않으면 loading dose는 수정할 필요가 없다.
- **Terminal slope와 half-life는** → $CL/V$의 조합이다. 단독으로 $CL$도 $V$도 결정하지 못한다.
- **Covariate가 붙어야 할 위치는** → $CL$(신기능, 효소유전형)인지 $V$(체중, 수분 상태)인지를 먼저 가설로 잡고 GOF 잔차를 본다. $K$를 target으로 삼으면 두 생리학이 혼재된 표현을 추정하게 된다.
- **NCA에서 $MRT$를 보고할 때는** → 구획 모델의 $V/CL$과 어떻게 다른지 설명할 수 있어야 한다. $MRT=AUMC/AUC$이고, $V_{ss}=CL\cdot MRT$이다.
- **고위험 상황 인식:** GOF에서 CWRES가 체중이나 CrCl과 상관되어 있다면 → $CL$ 또는 $V$ 중 어느 parameter에 covariate를 추가할지 판단하는 첫 질문은 "이 공변량이 배수구($CL$)에 영향을 주는가, 아니면 욕조 크기($V$)에 영향을 주는가?"이다.

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
| 2 | `### 🃏 C1. Clearance ($CL$) [⚡ Apex Concept]` | YES | 1 | YES | §2 — C1 Clearance |
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
| C10 v3 Apex label (v3) | C1 marker uses standardized `[⚡ Apex Concept]` instead of informal `[Apex]` | C1 heading line; B3 splice table also updated for consistency | PRESENT (v3) | None |
| C11 v3 Plausible Fallacy (v3) | Apex card carries Plausible Fallacy block grounded in existing S1/S4 anchor | C1 card after Recap | PRESENT (v3) | None |
| C12 v3 Memory Hooks (v3) | All three §5 confusion pairs carry structurally-encoded Memory Hooks | §5 Pair 1/2/3 each has a Memory Hook callout | PRESENT (v3) | None |
| C13 v3 Critical Blow (v3) | Highest-impact pair (CL vs K) carries Critical Blow row in comparison table | §5 Pair 1 table 치명적 타격 row | PRESENT (v3) | None |
| C14 v3 Practice Briefs (v3) | C1–C5 cards each carry 4-axis Practice Brief (왜·흐름·꿀팁·실무) | After each card Recap | PRESENT (v3) | None |
| C15 v3 §8C expansion (v3) | Professional Moat extended from 4 abstract bullets to 4 + 6 decision-direction bullets | §8C Professional Moat | PRESENT (v3) | None |
| C16 v3 LaTeX integrity (v3) | All v3 additions preserve subscript/fraction conventions: $K$, $CL$, $V$, $t_{1/2}$, $MRT$, $AUC$, $C_{ss}$, $V_{ss}$ | Inspected v3 inserts: no `\a`-style BEL char, no broken subscripts, no fractured fractions | PASS (v3) | None |


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
| AUG-6 (v3) | C1 card, after Recap | EXPERT_INFERENCE, v3 | Apex Concept Plausible Fallacy: same K does not mean same elimination capacity | Reuses existing locked S1/S4 CL/V values; no new numerics |
| AUG-7 (v3) | C1–C5 cards, after each Recap | EXPERT_INFERENCE, v3 | Practice Brief 4-axis blocks (왜·흐름·꿀팁·실무) for each card | Each block re-grounds existing locked content; no new equations |
| AUG-8 (v3) | §5 Pair 1 (CL vs K), after table | EXPERT_INFERENCE, v3 | Memory Hook: drain (CL) vs water-level descent rate (K) | Reuses existing locked CL/V/K hierarchy |
| AUG-9 (v3) | §5 Pair 2 (V vs Vss), after Lock | EXPERT_INFERENCE, v3 | Memory Hook: container size vs apparent container size | Reuses existing locked apparent-volume framing |
| AUG-10 (v3) | §5 Pair 3 (t½ vs MRT), after table | EXPERT_INFERENCE, v3 | Memory Hook: median (t½) vs centroid (MRT); 1.443 as math necessity | Reuses already-locked 1.443 ratio |
| AUG-11 (v3) | §5 Pair 1 table | EXPERT_INFERENCE, v3 | Critical Blow row: K-as-covariate-target → NDA failure mode | Caution-direction extension of existing Critical correction |
| AUG-12 (v3) | §8C Professional Moat | EXPERT_INFERENCE, v3 | 6-bullet decision-direction expansion (AUC/CL, C0/V, terminal/CL·V, covariate position, MRT/Vss, GOF triage question) | Operationalizes existing hierarchy without new clinical numerics |


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

**Recommended canonical anchor id list (use these exact ids in Phase 5):**

| Section / Card | Stable id | Sidebar label (Korean) |
|---|---|---|
| §1 Session Header & Roadmap | `section-1-roadmap` | §1 세션 개요 및 로드맵 |
| §2 Concept Anatomy Cards (header) | `section-2-cards` | §2 개념 해부 카드 |
| C1 Clearance | `card-c1-clearance` | C1 청소율 (CL) |
| C2 Volume of Distribution | `card-c2-volume` | C2 분포용적 (V) |
| C3 Elimination Rate Constant | `card-c3-k` | C3 소실속도상수 (K) |
| C4 Half-life | `card-c4-half-life` | C4 반감기 (t½) |
| C5 Mean Residence Time | `card-c5-mrt` | C5 평균체류시간 (MRT) |
| §5 Confusion Pair Dissection | `section-5-confusion` | §5 혼동 쌍 해부 |
| §5 Pair 1 CL vs K | `pair-1-cl-vs-k` | Pair 1 CL vs K |
| §5 Pair 2 V vs Vss | `pair-2-v-vs-vss` | Pair 2 V vs Vss |
| §5 Pair 3 t½ vs MRT | `pair-3-thalf-vs-mrt` | Pair 3 t½ vs MRT |
| §7 Self-Test | `section-7-self-test` | §7 자가 테스트 |
| §8 Meta-Frame & Big Picture | `section-8-meta` | §8 메타프레임 |

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


### B13. Ver2 Patch Log

**Patch scope:** ver1 → ver2 minor patch. Canonical body unchanged. No new scientific content. No new page tags. Audit/Crucible regression guardrails (B9) honored.

| # | Type | Location | Change | Source authority | Risk control |
|---|---|---|---|---|---|
| P1 | CRITICAL FIX | C5 Mastery Augmentation block | `\a` (BEL char) + `pprox` was breaking MathJax rendering of `$MRT/t_{1/2}\approx 1.443$`. Replaced with valid `\approx`. Added one source-bound clarification on which deviation direction (1.85 ≫ 1.443 vs 1.10 ≪ 1.443) suggests which failure mode. | G p.19, p.474; R&T p.60–61. Quantitative deviation reading is a direct corollary of Audit T1 MATCH item (`MRT=1.443·t1/2` in 1-cmt IV bolus only). | No new numbers introduced; values quoted are present in Compound A Tables 1.2/1.3 already. |
| P2 | CLARITY | C1 Anchor box (Subject 1 vs 4 correction) | Added explicit cross-reference to §7 Q5 ("§7 Q5에서 정량 확인") and stated the trap explicitly: $K$ and $t_{1/2}$ similarity does not imply same drug-handling capacity. | Audit T1 ERROR row (line 53); Crucible Grade A Fix-1 (D-1 recommendation: "Q5에서 정량 확인" wording proposed in Crucible). | No new numeric claim; reuses already-locked S1/S4 CL/V/Css values. |
| P3 | CLARITY | C4 Distribution-phase limitation paragraph | Elevated the source-anchored "distribution-phase AUC / total AUC" ratio to an explicit anchor sentence (50% midazolam vs 95% gentamicin). The two endpoints were already in body; the anchor sentence makes the diagnostic rule visible. | R&T p.64–66 (already cited in Content Lock v2). Crucible Grade A Tip-8 (TT-4): "AUC_분포위상/AUC_전체 < 50% 이면 1구획 근사 임상적 안전". | No new sources, no new figures, no new numbers. |
| P4 | DEPTH | C5 MRT card | Added a 2-bullet `#### C. Boundary` matching depth of other cards. Bullet 1: AUMC sensitivity to terminal extrapolation. Bullet 2: $MRT=1/K=1.443\,t_{1/2}$ holds only in 1-cmt IV bolus; generalization is future-session. | G p.19 (AUMC is t·C(t) integral). R&T p.60–61 (1-cmt IV bolus restriction explicitly stated). | The flagged NOT_IN_SOURCE formula `MRTiv = Vss/CL` (Audit T1 line 71) is **not** introduced; only the qualitative statement that the simple relation breaks outside 1-cmt IV bolus, which is direct R&T p.60–61 content. |
| P5 | COMPILER METADATA | PART B §B8 Navigation anchor integrity rules | Added a "Recommended canonical anchor id list" table. PART B is compiler-only and does not affect learner-facing PART A content. | Phase 5 compiler operational requirement; no scientific authority needed. | Pure rendering metadata; no content change. |

**Items intentionally NOT changed in ver2 (and why):**
- Subject 1 vs 4 V values: kept as-is (S1=10, S4=20). Already source-bound.
- Loading dose formula `LD = V × C_target`: not added. R&T p.62–64 supports it conceptually, but Audit/Crucible did not flag its absence as a gap, and adding the formula would expand the worked-example surface beyond Content Lock v2 scope.
- "Hierarchy Collapse pattern" GOF signature naming (Crucible T2(b)): not added as a named pattern. Already represented as concept in C3 TRENCH ("공변량이 CL에 작용하는지 V에 작용하는지 분리하기 어렵다") with `[실무 확장/교과서 외 해석]` tag. Naming the signature would constitute new NOT_IN_SOURCE practice content under a new label.
- §6 Pragmatic Application Scenarios + §3 Structural Isomorphism + §4 Interactive Simulator: intentionally omitted from PART A. These are Step 2 HTML compiler responsibilities (§3·§4·§6 are generated in the HTML compile phase per Step 1 protocol), not Step 1 deliverables.

**Verification after patch:**
- All page tags in PART A: identical to ver1 (no additions, no removals).
- All figure markers: identical to ver1 (4 markers, same anchors, same content).
- Self-test answers: identical to ver1.
- Splice Verification Table (B3): unchanged.
- Trace hash recomputation needed: Spliced PART A body sha256 will differ from ver1 (`bb5eab629fc9118a`) due to P1–P4 edits. New hash will be computed on the final output file by a downstream pipeline if required; recorded here only descriptively.



### B14. v3 Change Log

**Patch scope:** ver2 → v3 surgical patch. Canonical scientific body unchanged. No new external numerics, no new page tags, no new figure markers, no NONMEM code reproduced. v3 addresses only structural-pedagogical gaps identified by independent third-party audit, while preserving the source-fidelity guarantees of v2.

| # | Type | Location | Change | Source authority | Risk control |
|---|---|---|---|---|---|
| V1 | LABEL STANDARDIZATION | C1 heading + B3 splice anchor row | `[Apex]` → `[⚡ Apex Concept]` per Step 1 protocol convention. | Step 1 protocol convention; no scientific authority required. | Pure label rename; B3 anchor row updated for internal consistency. |
| V2 | APEX EXTENSION | C1 card after Recap | Added Plausible Fallacy block: same K does not imply same elimination capacity; uses already-locked S1/S4 CL/V values. | Reuses Audit T1 corrected interpretation and locked S1/S4 numerics from G Tables 1.2/1.3, p.473–474. | No new numerics; tag `[EXPERT_INFERENCE, v3]`. |
| V3 | PEDAGOGICAL DEPTH | C1–C5 cards, each after Recap | Added 4-axis Practice Brief blocks (왜 알아야 하는가 / 흐름상 역할 / 체화 꿀팁 / 실무 활용). | Each axis re-grounds existing locked content; no new equations or numerics introduced. | All five blocks tagged `[EXPERT_INFERENCE, v3]`. |
| V4 | MEMORY ENCODING | §5 Pair 1, Pair 2, Pair 3 | Added one Memory Hook each, encoding *structural reason for difference*: drain vs descent rate (CL vs K); container vs apparent container (V vs Vss); median vs centroid (t½ vs MRT, with 1.443 as integral-of-exponential math necessity). | Reuses existing locked hierarchy; ratio 1.443 already source-anchored in C5 (G p.19, p.474). | No new external metaphors importing fresh quantitative claims; tag `[EXPERT_INFERENCE, v3]`. |
| V5 | CRITICAL BLOW | §5 Pair 1 (CL vs K) table | Added 치명적 타격 row: K-as-covariate-target → NDA package missing renal-impairment dose-adjustment justification. | Operationalization of TRENCH note already present at line 469 of v2 (covariate at K obscures CL/V separation). | No new regulatory citation; framed as plausible failure mode, tag `[EXPERT_INFERENCE, v3]`. |
| V6 | DECISION-DIRECTION EXPANSION | §8C Professional Moat | Preserved existing 4 abstract bullets; appended 6-bullet "decision-direction" expansion (AUC↔CL, C0↔V, terminal↔CL/V, covariate position, MRT/Vss bridge, GOF triage question). | Each bullet re-articulates locked equations from C1–C5; no new clinical examples or page tags. | Tagged `[EXPERT_INFERENCE, v3]`. |

**v3 LaTeX integrity verification (per PATCH 6 directive):**

- Subscripts: `t_{1/2}`, `C_{ss}`, `C^0`, `V_{ss}`, `R_{in}`, `K_{Pi}`, `f_u`, `V_u`, `V_B`, `V_{Ti}`, `E_{Ti}`, `f_e` — all preserved with proper brace grouping.
- Fractions: `\frac{...}{...}` and inline `Dose/AUC`, `CL/V`, `R_{in}/CL`, `\ln 2/K`, `t_{1/2}/\ln 2`, `D/V`, `D/C^0`, `AUMC/AUC` — all preserved.
- Special operators: `\approx`, `\cdot`, `\sum`, `\int_0^\infty`, `\ln` — verified intact in both v2-original blocks and v3 inserts.
- BEL-character / typo regression check: no `\a` (U+0007) followed by malformed `pprox` patterns in v3 inserts. ver2 P1 fix preserved.
- All v3 inserts use `$...$` inline and `> ...` blockquote-only formatting; no new `$$...$$` display blocks introduced (preserves existing display-math inventory).

**Items intentionally NOT changed in v3 (and why):**

- Compound A Subject 1/4 numerics (V=10/20 L, CL=0.1/0.2 L/min, K=0.01 min⁻¹): kept as-is per non-negotiable preservation rule. Memory Hook V4 and Plausible Fallacy V2 reference these values without altering them.
- §6 Pragmatic Application Scenarios + §3 Structural Isomorphism + §4 Interactive Simulator: still intentionally omitted from PART A. These are Step 2 HTML compiler responsibilities, not Step 1 deliverables. (Same rationale as ver2 §B13.)
- Loading dose formula `LD = V × C_target`: still not added to canonical body. Mentioned only inside the C2 Practice Brief 실무 활용 axis as a tagged `[EXPERT_INFERENCE, v3]` interpretive note, not as a new locked equation.
- ver2 P1–P5 patches and their rationale: preserved verbatim in B13.
- Existing figure markers, page tags, trace hashes (B11), source-boundary certificate (B10): unchanged.

**Verification after v3 patch:**

- All v2 page tags in PART A: identical (no additions, no removals).
- All v2 figure markers: identical (4 markers, same anchors, same content).
- v2 self-test answers: identical.
- v2 Compound A numerics: identical.
- ver2 §B13 patch log entries: preserved verbatim.
- New v3 augmentations: 6 entries (V1–V6), all tagged with epistemic label `[EXPERT_INFERENCE, v3]`.
- New v3 PART A insertion blocks: 1 Apex label rename + 1 Plausible Fallacy + 5 Practice Briefs + 3 Memory Hooks + 1 Critical Blow row + 1 Professional Moat expansion = 12 surgical inserts in PART A.
- B6 Mastery Augmentation Log: extended from 5 to 12 entries (AUG-1 to AUG-12).
- B4 Zero-Omission Coverage Matrix: extended from C1–C9 to C1–C16 (added C10–C16 for v3 items).
- B3 Splice Verification Table: anchor text for marker #2 updated from `[Apex]` to `[⚡ Apex Concept]` for consistency with v3 heading.

### B12. Final Checklist

- PART A is independently readable as a learner handout.
- PART A contains learner navigation aid, canonical body, approved figure markers, preserved page tags, self-tests, and labeled augmentations.
- PART A contains no audit/adjudication process tables.
- PART B contains process logs, coverage matrix, compiler rules, guardrails, ver2 patch log, and v3 change log only.
- No HTML was generated.
- No Mermaid/SVG code was generated.
- ver2 patches (P1–P5) applied; v3 patches (V1–V6) applied; canonical scientific body unchanged.
- Critical MathJax rendering bug (BEL char + 'pprox' typo) FIXED in ver2 and preserved in v3.
- v3 surgical patches preserve all v2 numerics, page tags, figure markers, and self-test answers.
- Final output filename: `01_html_compile_input_master_v3.md`.


---

## Final v3 All-Pass Checklist

| # | Audit item | Status | Evidence (1-line) |
|---:|---|---|---|
| 1 | Apex 레이블 표준화 (`[Apex]` → `[⚡ Apex Concept]`) | **PASS** | C1 heading line 86 + B3 splice anchor row both updated; no remaining `[Apex]` orphan in canonical body. |
| 2 | Apex Plausible Fallacy 블록 추가 (1건, EXPERT_INFERENCE 태그) | **PASS** | C1 card carries 3-bullet Plausible Fallacy block reusing locked S1/S4 V/CL/K values; tagged `[EXPERT_INFERENCE, v3]`. |
| 3 | §5 Memory Hook 3쌍 모두 추가 (구조적 인코딩) | **PASS** | Pair 1 = drain vs descent rate; Pair 2 = container vs apparent container; Pair 3 = median vs centroid (1.443 = 지수함수 적분의 수학적 필연). All three encode *structural reason for difference*, not just restate it. |
| 4 | §5 Pair 1 (CL vs K) Critical Blow 행 추가 | **PASS** | 치명적 타격 row inserted into CL vs K comparison table; anchored to NDA dose-adjustment failure mode. |
| 5 | C1–C5 카드별 Practice Brief 4축 블록 추가 | **PASS** | 5개 카드 모두 Recap 직후 4축(왜·흐름·꿀팁·실무) Practice Brief 부착; 각 블록 EXPERT_INFERENCE, v3 태그. |
| 6 | §8C Professional Moat 5–6개 불릿 구체화 | **PASS** | 기존 4 abstract 불릿 보존 + 6개 decision-direction 불릿 추가(AUC↔CL, C0↔V, terminal↔CL/V, covariate position, MRT/Vss, GOF triage). Total 10 bullets. |
| 7 | v2 보존 무결성 (수치·page tag·figure marker·자기테스트 답변·수식) | **PASS** | Compound A S1/S4 numerics, all `[G p.XX]`/`[R&T p.XX]` tags, 4 figure markers, §7 Q1–Q9 답변, MathJax 수식 모두 변경 없음. ver2 §B13 entries 보존. |
| 8 | LaTeX 무결성 (subscript·분수·BEL char regression) | **PASS** | v3 inserts 내 `t_{1/2}`, `C_{ss}`, `V_{ss}`, `R_{in}` 등 subscript 표기 정상; `\frac`/inline 분수 모두 정상; ver2 P1에서 수정된 BEL+`pprox` 회귀 없음. B14에 LaTeX integrity verification 명시. |

**전체 판정: 8/8 PASS.** 독립 감사에서 식별된 4개 구조적 결함(Memory Hook 누락 3쌍, Apex 레이블 비표준, Critical Blow 부재, §8C Professional Moat 추상성)이 모두 외과적 패치로 해결되었으며, v2의 source-fidelity 본문은 일체 손상되지 않았다. Phase 5 HTML compiler는 v3 PART A를 그대로 렌더링 대상으로 삼을 수 있다.

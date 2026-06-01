# PK/PD Mastery Protocol — Step 1 Draft v0
## Session 12 · Effect Compartment · Tolerance & Rebound · Transduction

---

## ▶ Source Detection & Adaptation Log

- **[Primary] Gabrielsson & Weiner 5e** — Vol I, 데이터·수식 도출·실험 수치 앵커링 담당
- **[Secondary] Rowland & Tozer 5e** — Vol I, 임상·생리학적 해석·hysteresis 진단 논리 담당
- **혼합 처리 규칙**: G&W = ODE 도출/Case Study 수치, R&T = clockwise/counterclockwise 판별 논리, system flux 개념. PD13 데이터는 §3.11 Tolerance 카드에 귀속, §3.9 Effect Compartment 카드에서는 Plausible Fallacy 사례로만 인용.
- **§3.10 Dose-Response-Time Models 명시적 제외** — Scope Lock의 page range가 §3.9(pp.261–272) → §3.11(pp.284–302)로 §3.10(pp.272–284)을 건너뛴다. Curation Map에서도 제외 처리.

---

## ▶▶ CURATION MAP

거장의 시각으로 우선 묻는다 — *"이 페이지 범위에서, 다음 개념을 이해하기 위해 반드시 먼저 체화되어야 하는 것은 무엇인가?"*

### MUST (체화 필수)

| # | 개념 | 왜 MUST인가 — 구조적 의존성 |
|---|------|------------------------|
| 1 | **Effect Compartment Model & $k_{e0}$** ⚡ Apex | 분포 지연(distributional hysteresis)을 수학적으로 포착하는 유일한 도구. 이 개념을 모르면 §3.11의 Tolerance와 §3.13의 Transduction이 "왜 별개의 모델이 필요한가"를 설명할 수 없다. 또한 §3.9.7 PD13 사례(Link 모델을 turnover 데이터에 잘못 적용 → EC50 용량 분기)가 Apex Concept의 직접 근거. |
| 2 | **Hysteresis 방향 판별 (시계/반시계) 및 기계론적 분류** | R&T Ch.8의 핵심 진단 도구. 방향 자체가 모델 선택을 결정 — 반시계 = distribution delay 또는 indirect response, 시계 = tolerance 또는 antagonistic metabolite. 이 판별 능력 없이 §3.11 Tolerance 카드의 의미를 읽을 수 없다. |
| 3 | **Tolerance/Rebound — Negative Feedback via Moderator M** | §3.11.9–11의 ODE 쌍은 이 세션 가장 깊은 수학 구조 (2차 다항식 정상상태). PD13 Model II가 Model I, III를 압도하는 이유(AIC=−97.5, WRSS=0.083)를 이해하려면 Moderator M 구조 필수. |
| 4 | **Transduction Model — Catenary Transit Compartments** | §3.13의 chain ODE는 PD35의 15–20시간 onset delay를 설명하는 유일한 구조. Indirect response 단일 구획으로는 절대 포착 불가. transit 수 n과 τ의 관계, kout = 1/τ의 동등성 인지 필수. |

### CONTEXT (이해 보완 — 1–2문장으로 MUST 카드에 흡수)

- **Pool/Precursor 모델** (§3.11.7 Model III) → MUST 3 카드에 흡수: Moderator 모델의 대안 구조이나 PD13에서 WRSS=0.28로 열등.
- **Colburn-Eldon 시간-의존 파라미터 약화** (§3.11.3) → MUST 3 카드에 흡수: 비기계론적 smoothing 접근, 단일 dose 한정·rebound 미포착의 한계 1문장 언급.
- **Antagonistic metabolite 모델** (§3.11.4) → MUST 3 카드에 흡수: rebound를 포착할 수 없다는 한계 1문장.
- **$t_{max}$ 불변 원칙** (§3.9.1 말미) → MUST 1 카드의 D Assumptions에 핵심 도구로 통합 — Link 모델은 dose에 무관하게 같은 $t_{max}$를 예측, 이것이 turnover와의 진단 갈림길.
- **Receptor binding kon/koff 모델** (PD21) → MUST 1 카드의 비교 항목으로 흡수, koff와 ke0의 단위 동일성 언급.
- **Systems analysis (Urquhart, Veng-Pedersen)** (§3.11.2) → MUST 3 카드 G에 1문장 언급.

### 의도적 제외 (Scope 외)

- §3.10 Dose-Response-Time Models 전체
- §3.12 Receptor occupancy theory (별도 세션 PD41 영역)
- §3.14 Synergistic effects (다음 세션)

---

# §1 — Session Header & Roadmap

**Source**: Gabrielsson & Weiner 5e (primary) + Rowland & Tozer 5e (secondary)
**Chapter**: G&W Ch.3 §3.9 / §3.11 / §3.13 + Case Studies PD13, PD20, PD21, PD35
**Pages**: G&W pp.261–272, 284–302, 323–325, 805–809, 836–848, 910–914 / R&T pp.233–264

<!-- MASTER LENS -->
**Big Idea (한 문장)**: 임상시험 데이터에서 plasma와 response 사이의 시간 지연을 보았을 때, 그것이 *분포 지연*인지(Link), *시스템 적응*인지(Turnover/Tolerance), *신호 전달 연쇄*인지(Transduction)를 ODE 한 줄로 판별하지 못하면, EC50가 용량별로 3배씩 흔들리는 모델을 들고 NDA 제출장에 들어가게 된다.

### 개념 항법도

```
Hysteresis 관찰 (R&T Ch.8)
        ↓
   방향 판별 (시계 vs 반시계)
        ↓
   기계론적 분류 — 세 갈래 분기
   ├─ 분포 지연        → §3.9  Effect Compartment (Link / ke0)
   ├─ 시스템 적응       → §3.11 Tolerance/Rebound (Moderator M / ktol)
   └─ 신호 전달 연쇄    → §3.13 Transduction (Transit / τ)
        ↓
   진단 갈림길: t_max 불변 (Link) vs t_max peak shift (Turnover)
        ↓
   PD13 참사: Link을 turnover 데이터에 적용 → EC50 dose-dependence
```

### 지식 그래프 위치

- **선행 지식 (있어야 함)**: Emax/Hill 방정식 §3.2, Indirect Response 4모델 §3.7 (kin/kout 구조), 1·2구획 PK 수식과 ODE 적분
- **이 세션이 열어주는 후속 지식**: TMDD (분포 지연 + receptor binding 결합 구조), PKPD 시뮬레이션 (multi-dose tolerance), 규제 제출용 임상-PD 모델, QSP의 cascade 신호 전달

---

# §2 — Concept Anatomy Cards

---

## ━━ 카드 1: Effect Compartment Model & $k_{e0}$ [⚡ Apex Concept] ━━

<!-- MASTER LENS -->
### [개념 Big Idea: 거장의 시각]

**왜 치명적으로 중요한가**: 마취과 회복실에서 succinylcholine 추가 투여 시점을 판단할 때, t½,ke0 = 4 min이라는 사실 하나가 환자의 호흡 마비 재발과 안전 발관을 가른다. 마찬가지로 Phase 1 first-in-human 용량 결정에서 hysteresis loop을 보고 "분포 지연이군 — Link 모델로 가자"고 단정하면, 데이터가 실제로는 turnover 시스템이었을 때 PD13처럼 EC50가 1차 용량 0.681, 10차 용량 4.85, 100차 용량 0.941로 7배 분기되는 모델을 NDA에 제출하게 된다.

**체화해야 할 단 하나의 직관**: $k_{e0}$는 약물 분자가 plasma와 receptor 사이의 *물리적 다리*를 건너는 속도다 — 다리 길이는 dose와 무관하다. 그래서 Link 모델의 시그니처는 단 하나: *모든 용량에서 동일한 $t_{max}$*. 이 단 하나의 진단 도구를 머릿속에 박으면, 아래 모든 수식이 자연스럽게 읽힌다.

**이 직관을 박고 아래를 읽어라.** 다리 길이는 변하지 않는다. 그러므로 dose가 커져도 도달 시간은 같다. Turnover 시스템처럼 "댐 수위"가 차오르는 데 시간이 걸리는 것이 아니다.

### A. Formal Definition

Effect Compartment Model (Link Model)은 *분포 지연*을 포착하기 위해 PK 모델 위에 가상의 1차 분포 구획을 덧붙이는 구조다. Receptor가 위치한 biophase의 농도 $C_e$를 plasma 농도 $C$로부터 1차 속도상수 $k_{e0}$로 평형에 도달시킨다. 이때 $C_e$는 직접 측정되지 않으며 response 시간 경과로부터 *역추정*된다. — Segre [1968], Wagner [1968], Sheiner et al [1979]의 원형 구조.

### B. Derivation

Plasma 1구획 IV bolus의 amount profile:
$$A_p = D \cdot e^{-K \cdot t} \quad \text{[출처: G&W 5e, Ch.3, p.264, Eq.3:126]}$$

Effect compartment의 amount 변화율:
$$\frac{dA_e}{dt} = k_{1e} \cdot A_p - k_{e0} \cdot A_e \quad \text{[출처: G&W 5e, Ch.3, p.264, Eq.3:127]}$$

여기서 $k_{1e}$는 plasma → effect compartment, $k_{e0}$는 effect compartment → out. 적분하면:
$$A_e = \frac{k_{1e} \cdot D}{k_{e0} - K} \cdot \left[ e^{-K \cdot t} - e^{-k_{e0} \cdot t} \right] \quad \text{[Eq.3:128]}$$

**핵심 식별가능성 제약**: $k_{1e}$와 $k_{e0}$를 동시에 추정할 수 없다 (identifiability problem). 정상상태에서 $k_{1e} \cdot A_p = k_{e0} \cdot A_e$이고 $K_p = C_e/C$ (분배계수)를 1로 두면 $V_e = (k_{1e} \cdot V_c)/(k_{e0} \cdot K_p)$이고, $k_{1e} = k_{e0}$ 가정 하에:

$$\boxed{\;C_e = \frac{k_{e0} \cdot D}{V_c \cdot (k_{e0} - K)} \cdot \left[ e^{-K \cdot t} - e^{-k_{e0} \cdot t} \right]\;} \quad \text{[출처: G&W 5e, Ch.3, p.265, Eq.3:134]}$$

대안 ODE 형태 (convolution 표현):
$$\frac{dC_e}{dt} = k_{e0} \cdot C - k_{e0} \cdot C_e \quad \text{[Eq.3:143]}$$

이 ODE 형태는 *plasma kinetics가 비선형이거나 table function일 때도* 유효하다 — PD21에서 oral 흡수가 깨끗한 first-order에 맞지 않을 때 plasma 데이터를 직접 table function으로 입력하는 근거.

평형 반감기:
$$t_{1/2,k_{e0}} = \frac{\ln 2}{k_{e0}} \quad \text{[G&W Table 3.9 기반]}$$

R&T Ch.8 Eq.8-3의 "log-linear region"에서 graded response의 시간 감소율:
$$\text{Response}(t) = E(0) - m \cdot k \cdot t \quad \text{[출처: R&T 5e, Ch.8, p.239]}$$
이 zero-order 감소가 Link 모델의 distribution-rate-limited region에서 관찰되는 *직선* 거동의 수학적 근거.

**실제 문헌 수치 (G&W Table 3.9)**: terbutaline FEV-1 t½,ke0 = 7.5 min, theophylline FEV-1 = 11 min, d-tubocurarine = 4 min, fentanyl spectral edge = 6.4 min, QT-quinidine = 8 min. **분포 율속의 t½,ke0는 일반적으로 분 단위**.

**PD20 임상 수치**: analgesic IV bolus D=45 µg/kg, V=1 L/kg, K=0.50 h⁻¹, 추정 ke0≈0.1 h⁻¹, EC50≈1.5 µg/L, Emax≈3–5.

### C. Structural Necessity

이 ODE 형태가 *왜 정확히 이 모양*이어야 하는가?

(1) **1차 분포의 수학적 필연**: biophase 진입이 농도 구배에 비례하고 (Fick 확산), 농도가 plasma처럼 동적이면, 결과는 반드시 두 지수항의 차 — 입력 지수 $e^{-K \cdot t}$와 출력 지수 $e^{-k_{e0} \cdot t}$. 이것이 Bateman 방정식의 보편 형태다.

(2) **$k_{1e} = k_{e0}$ 가정의 필연**: 만약 둘이 다르다면 $V_e \neq V_c \cdot K_p$가 되어 effect compartment에 *질량 보존이 깨진다*. Identifiability를 위해서가 아니라 *물리적 정합성*을 위해 강제됨 — Sheiner et al [1979] 이래의 표준.

(3) **$t_{max}$ 불변의 필연**: linear PK 가정 하에 $C_e$의 maximum은 $C$와 $C_e$ 곡선의 교점에서 일어나며, 이 시점은 $K$와 $k_{e0}$만의 함수이고 dose에 *수학적으로 독립*이다. 이것이 Link vs Turnover 진단의 골든 룰.

<!-- ANCHOR -->
이 세 필연성이 동시에 성립할 때만 Link 모델이 정당하다 — 하나라도 위반되면 PD13의 EC50 분기 참사로 직결.

### C-2. Plausible Fallacy (그럴싸한 오류) — Apex 전용

**오류의 형태**: 임상시험 데이터에서 반시계 hysteresis loop을 관찰하고 "분포 지연이다 → Link 모델"을 곧바로 적합한다. 단일 dose 데이터에서는 구분 불가능하므로 fit이 *수치적으로* 좋아 보인다.

**나비효과 — 기계론적 추적**:
1. 실제 데이터가 turnover 시스템에서 생성되었음 (G&W §3.9.7, Models 1–4 시뮬레이션).
2. Link 모델을 *각 dose에 개별적으로* 적합 → 각 dose마다 다른 EC50, Emax, n 값 산출.
3. PD13 Table 3.10 사례: dose 1 → EC50=0.681, n=1.33 / dose 10 → EC50=4.85, n=0.88 / dose 100 → EC50=0.941, n=1.62. **EC50가 7배, n이 1.8배 분기**.
4. 동시 적합 시 시스템적 deviation 발생: link-predicted curve가 실제 데이터보다 일찍 peak (Fig 3.59).
5. NDA 제출 시 "PD parameters change with dose"는 *생물학적으로 불가능* — receptor sensitivity가 dose에 의존할 수 없으므로.

**GOF 시그니처 패턴 이름**: **"EC50 용량 분기 패턴" (Dose-Bifurcating EC50 Signature)** — 같은 데이터를 dose-stratified로 individual fit했을 때 EC50가 dose에 따라 단조 증가 또는 비단조 분기. 이 패턴이 보이면 Link 모델 가정이 깨졌다는 명확한 신호.

### D. Assumptions & Boundary Conditions

| 가정 | 위반 시 무엇이 일어나는가 |
|------|----------------------|
| Plasma kinetics가 linear | 비선형 시 ODE 형태(Eq.3:143)는 유효하나 닫힌 해(Eq.3:134) 무효 |
| $k_{1e} = k_{e0}$ (identifiability) | 위반 시 effect compartment의 질량 보존 위반, $V_e$ 추정 불가 |
| $K_p = 1$ (no partitioning) | 위반 시 $C_e \neq C$ at steady state, 추정된 EC50가 *biophase EC50가 아닌* surrogate |
| Receptor 결합이 *순간적* | 위반 시 receptor binding model (kon/koff) 필요 — PD21 비교 |
| Response 시스템이 *순간적*으로 $C_e$ 추적 | **위반 시 turnover/transduction 모델 필요** — Link 모델의 가장 흔한 위반 |
| **$t_{max}$가 dose-invariant** (Eq.3:126 가정의 결론) | 위반 = peak shift 발견 = **Link 모델 즉시 기각** |

### E. Limitations

- **Effect compartment의 농도는 직접 측정 불가** — 오직 response time course로부터 역추정. Steady-state 데이터만으로는 추정 불가능 (rise와 fall 둘 다 필요).
- **Turnover 시스템 데이터에 적용 시 위에 서술한 PD13 참사**.
- **Active metabolite, receptor up-regulation, slow on/off binding 등**의 다른 hysteresis 원인을 distribution delay로 잘못 동일시.
- 다음 수준: TMDD, indirect response model (Dayneka et al [1993]), receptor binding kinetics (PD21).

### F. Five Cognitive Layers

| 레이어 | 내용 |
|------|----|
| **L1 형식적 수학** | Eq.3:127→3:134의 도출, Bateman two-exponential 구조, identifiability 제약 |
| **L2 기하학적 직관** | $C_e$ 곡선이 $C$ 곡선의 *지연된 평활화*; 두 곡선의 교점이 $t_{max,e}$ — dose 무관 |
| **L3 구조적 동일성** | RC 회로(plasma=AC source, biophase=capacitor, $k_{e0}$=1/RC), 욕조-물탱크 연쇄 흐름, convolution operator $E = k_{e0} * C^0 e^{-K t}$ (Eq.3:142) |
| **L4 생리학적 의미** | $t_{1/2,k_{e0}}$는 organ size, tissue binding, perfusion+diffusion의 합성 결과. 분 단위 → distribution delay (succinylcholine 4 min). 시간 단위 → 다른 메커니즘 의심 (G&W p.269 명시) |
| **L5 실무 투영** | NONMEM `$DES`: `DADT(2) = KE0*A(1)/V1 - KE0*A(2)`; PD21 사례에서 plasma data를 table function으로 driver 사용 |

### G. Zettelkasten Atom

```yaml
---
aliases: [Effect Compartment, Link Model, ke0 model, biophase model]
tags: [pharmacometrics/pd, hysteresis, distributional-delay, gabrielsson]
up: "[[MOC — PK-PD Time Delay Models]]"
related: ["[[ke0 vs kout 구분]]", "[[hysteresis 방향 진단]]", "[[Turnover model]]", "[[t_max invariance test]]", "[[PD13 — Link misapplication]]"]
source: "Gabrielsson & Weiner 5e, Ch.3 §3.9, pp.261–272"
---

Effect Compartment Model은 plasma C와 biophase Ce 사이의 1차 분포 지연을
ke0 단일 파라미터로 포착한다. 핵심 시그니처는 *dose-invariant t_max* — 
이 한 가지가 Link 모델의 정당성을 결정한다. Identifiability 제약(k1e = ke0)과 
Kp = 1 가정 하에 Ce = (ke0·D)/(Vc(ke0-K)) · [e^(-Kt) - e^(-ke0·t)]. 
적합한 거장의 사용처는 분 단위 t½,ke0를 갖는 distribution-rate-limited 약물
(succinylcholine, fentanyl spectral edge, QT-quinidine). Turnover 시스템 데이터에 
적용 시 EC50가 dose마다 분기 — biologically implausible, NDA Deficiency Letter 직결.
```

<!-- RECAP -->
Effect Compartment 카드의 한 줄 회수: *다리 길이는 dose에 무관하다 — 그러므로 모든 용량에서 같은 $t_{max}$. 이것이 깨지면 Link 모델은 거짓이다.*

---

## ━━ 카드 2: Hysteresis 방향 판별 및 기계론적 분류 ━━

<!-- MASTER LENS -->
### [개념 Big Idea: 거장의 시각]

**왜 치명적으로 중요한가**: Concentration-vs-response plot의 화살표 방향이 시계인지 반시계인지를 *5초 내에* 읽지 못하면, 그 다음 모델 선택 회의에서 30분간 잘못된 방향으로 토론한다. R&T Ch.8 Fig 8-2의 naproxen은 반시계 (분포 지연), Fig 8-9의 ibuprofen은 반시계 (system flux), 반면 cocaine tolerance는 시계 (G&W Fig 3.80) — 화살표 하나가 완전히 다른 모델 패밀리를 가리킨다.

**체화해야 할 단 하나의 직관**: Hysteresis 방향은 시간의 *굴절 방향*을 보여준다. 반시계 = response가 concentration 뒤를 *따라온다* = system이 plasma보다 *느리다*. 시계 = response가 concentration 앞을 *치고 빠진다* = system이 plasma의 효과를 *상쇄*한다 (tolerance) 또는 active metabolite이 *반대 방향*으로 작용한다.

**이 직관을 박고 아래를 읽어라.** 화살표는 시간의 흐름이다 — 어느 방향으로 휘는지가 메커니즘을 가른다.

### A. Formal Definition

Hysteresis는 동일 농도에 대해 농도가 *상승할 때*와 *하강할 때*의 response가 다른 현상. Plot 위의 chronological arrow가 반시계 방향(counterclockwise)이면 *response lag*, 시계 방향(clockwise)이면 *response lead*. R&T Ch.8 Fig 8-2 (naproxen)와 G&W Fig 3.51이 표준 도식.

### B. Derivation / 진단 매트릭스

R&T Ch.8 (pp.234–245)의 진단 논리를 ODE 형식으로 정리:

| Hysteresis 방향 | 가능 메커니즘 | ODE 시그니처 | 진단 후속 질문 |
|---|---|---|---|
| **반시계 (lag)** | (i) 분포 지연 | $\dot{C_e} = k_{e0}(C - C_e)$ | t_max가 dose-invariant인가? |
| | (ii) Indirect response (turnover) | $\dot{R} = k_{in} \cdot S(C) - k_{out} \cdot R$ | dose 증가 시 t_max peak shift가 있는가? |
| | (iii) Slow ligand-receptor on-rate | $\dot{[RC]} = k_{on}[C][R] - k_{off}[RC]$ | $k_{off}$ 단독 추정 가능한가? |
| | (iv) Active metabolite (concordant) | metabolite ODE 추가 | metabolite plasma 추적 가능한가? |
| **시계 (lead)** | (i) Tolerance / desensitization | $\dot{R} = k_{in} \cdot S(C) - k_{out} \cdot M$, M=moderator | 다회 dose에서 tolerance 발달 보이는가? |
| | (ii) Antagonistic metabolite | $\dot{C_M} = k_M(C_p - C_M)$, opposing effect | metabolite가 약리학적으로 길항인가? |
| | (iii) Receptor down-regulation | turnover with feedback | 회복 시간이 receptor synthesis 시간과 일치하는가? |

**R&T Ch.8 직접 인용**: "Tolerance is often manifested by a clockwise response *versus* concentration relationship provided a stimulatory response... an anti-clockwise response *versus* concentration curve may occur, provided the rate of input of drug into the system is more rapid than the rate of distribution or tolerance development, or when there is an inhibitory action on drug response." [출처: R&T 5e, Ch.8, p.296의 G&W 인용 부분]

**핵심 진단 트릭** (R&T pp.245–247의 collapse method, PD21에 적용): hysteresis loop을 *collapse*시키는 ke0 값을 찾으면, 그 값이 분포 지연의 추정치다. PD21에서 ke0 ≈ 0.025 min⁻¹이 hysteresis를 거의 완전히 collapse시킴.

### B-2. 임상 사례 — R&T Ch.8 핵심 수치

- **Digoxin** (R&T Fig 8-1, p.234): IV bolus 1 mg, 0–4시간 plasma 하강 중 left ventricular ejection-time index 상승 → 대표적 반시계 hysteresis, 6시간까지 distribution equilibrium 도달.
- **Naproxen** (R&T Fig 8-2): oral 500 mg, peak 3–4 h, effect compartment 모델로 hysteresis 제거 → 단일 EC50, Emax 추정 가능 (Fig 8-14).
- **Warfarin** (R&T Fig 8-10): oral 1.5 mg/kg, prothrombin complex nadir ~48 h, t½ complex ≈1–2 days — system flux의 대표 사례, 분포 지연 아님.
- **Aspirin** (R&T Fig 8-20): 650 mg oral, plasma t½ = 15 min이지만 antiplatelet effect가 며칠 지속 — covalent receptor 비가역 결합으로 인한 PD rate-limited decline.
- **Succinylcholine** (R&T Fig 8-18, 8-24): 0.5 mg/kg IV, T50≈6 min, k≈0.2 min⁻¹, 80→20% response가 22%/min 직선 감소 — Region 2 log-linear region.

### C. Structural Necessity

방향이 *왜 정확히 두 가지뿐*인가? Concentration이 단조롭게 상승했다 하강하고 (extravascular dose), response가 단일 메커니즘으로 결정되면, plot 위의 trajectory는 닫힌 곡선(loop)이 되고 화살표는 두 방향 중 하나를 가질 수밖에 없다. 두 방향 모두 갖는 *figure-eight* 패턴은 두 메커니즘이 동시에 작용 (예: 분포 지연 + tolerance) — 이 경우 모델 식별 매우 어려움.

### D. Assumptions

- 단일 dose, monotonic plasma profile (extravascular). Steady-state infusion에서는 hysteresis loop이 형성되지 않음.
- 단일 dominant 메커니즘 가정. 복합 메커니즘 시 figure-eight 가능.
- Response가 *연속적*으로 측정됨. 이산 sample 간격이 크면 방향 판별 불가.

### E. Limitations

- 단일 dose 데이터로는 sub-mechanism 구분 불가 (반시계 안에서 i/ii/iii/iv 구분 못함). **다회 dose 또는 multi-route 설계 필수**.
- Active metabolite의 concordant vs antagonistic 효과는 metabolite plasma 추적 없이는 추론 불가.
- 매우 빠른 ke0 (≪관측 간격)에서는 hysteresis가 보이지 않아 direct response로 오판.

### F. Five Cognitive Layers

| 레이어 | 내용 |
|----|----|
| **L1** | Loop의 chronological arrow direction = sign of $\partial R / \partial C - \partial R / \partial t \cdot dt/dC$ |
| **L2** | Phase plane diagram의 vector field; loop은 limit cycle의 단편 |
| **L3** | 전기공학의 magnetic hysteresis (B-H curve), 열역학의 Carnot cycle, 생태학의 predator-prey loop |
| **L4** | 반시계 = "받는 시스템이 느리다" (distribution OR turnover OR slow binding). 시계 = "받는 시스템이 적응한다 또는 길항한다" |
| **L5** | NONMEM에서 `IPRED vs DV` plot이 hysteresis 보이면 모델 misspecification — direct response로 시작해서 link → turnover → tolerance 순으로 escalate |

### G. Zettelkasten Atom

```yaml
---
aliases: [Hysteresis 방향, Counterclockwise hysteresis, Clockwise hysteresis]
tags: [pharmacometrics/pd, model-discrimination, diagnostic]
up: "[[MOC — PK-PD Time Delay Models]]"
related: ["[[Effect Compartment]]", "[[Tolerance]]", "[[Indirect Response]]", "[[Active metabolite]]"]
source: "Rowland & Tozer 5e, Ch.8, pp.234–245"
---

Hysteresis 방향은 5초 진단 도구다. 반시계(counterclockwise) = response가 concentration보다
뒤따라옴 → 분포 지연/turnover/slow binding/concordant metabolite. 시계(clockwise) = response가
concentration보다 먼저 빠짐 → tolerance/antagonistic metabolite/down-regulation. 단일 dose만으로는
sub-mechanism 구분 불가 — 반드시 다회 dose 또는 t_max peak shift 검정으로 보강. Loop의 collapse를
유발하는 ke0 값이 분포 지연 추정치 (PD21 method).
```

<!-- TRENCH -->
**Trench-Level Tip**: 임상시험 데이터를 받자마자 plot을 그릴 때, x축을 plasma 농도, y축을 response, 각 시간점을 작은 화살표로 연결하라. 5초 안에 화살표 방향이 보이지 않으면 데이터가 너무 sparse한 것이고, 보이면 그 방향이 그 다음 모델 토론 30분을 결정한다.

<!-- RECAP -->
Hysteresis 카드의 한 줄 회수: *화살표 방향 = 시간의 굴절 방향 = 메커니즘 패밀리.*

---

## ━━ 카드 3: Tolerance & Rebound — Negative Feedback via Moderator M ━━

<!-- MASTER LENS -->
### [개념 Big Idea: 거장의 시각]

**왜 치명적으로 중요한가**: Nitroglycerin 작업자의 "월요일 두통, 일요일 angina" 패턴 — Hat TDS 일화 (G&W Fig 3.71) — 을 ODE로 옮기지 못하면, 임상시험에서 weekend dosing holiday를 설계해서 환자에게 rebound vasoconstriction에 의한 심근경색을 안긴다. Cocaine 심혈관 효과의 acute tolerance, β-agonist의 desensitization, opioid의 점진적 내성 — 모두 같은 Moderator M 구조의 변주이고, 이 구조 없이 multi-dose simulation을 돌리면 PD13 Model II가 잡아낸 AIC=−97.5의 적합력을 Model I (no feedback, AIC=−39.0)이나 Model III (pool, AIC=−43.5)이 절대 따라잡지 못하는 이유를 설명할 수 없다.

**체화해야 할 단 하나의 직관**: Moderator M은 Response R의 *늦게 따라오는 그림자*다. 약물이 R을 자극하면 M이 천천히 따라 자라며 R을 *반대로 끌어내린다* (tolerance). 약물이 사라지면 R 자극은 즉시 없어지지만 M은 아직 높이 남아있다 — 그래서 R이 baseline 아래로 떨어진다 (rebound). M의 t½ = ln(2)/ktol이 tolerance 발달과 rebound 회복 모두를 지배한다.

**이 직관을 박고 아래를 읽어라.** 한 ODE 쌍이 두 임상 현상(tolerance, rebound)과 한 통계적 자국(AUC asymmetry: AUC_response > AUC_rebound) 모두를 동시에 생성한다.

### A. Formal Definition

Tolerance는 약물 반복 노출 시 response가 점진적으로 감소하는 현상 (desensitization, tachyphylaxis 포함). Rebound는 약물 중지 후 response가 baseline 아래(억제성 약물의 경우 위)로 떨어졌다 회귀하는 현상. Moderator 모델은 endogenous modulator M이 R에 *반대 방향*으로 작용하면서 R의 변화를 따라잡는 음성 피드백 구조 (Ackerman et al [1964], 후일 Ahlström et al [2012] review).

### B. Derivation — Negative Feedback via Moderator (PD13 Model II 구조)

핵심 ODE 쌍 [출처: G&W 5e, Ch.3, p.299, Eqs.3:193–194]:

$$\boxed{\;\frac{dR}{dt} = k_{in} \cdot S(C) - k_{out} \cdot M\;}$$

$$\boxed{\;\frac{dM}{dt} = k_{tol} \cdot R - k_{tol} \cdot M\;}$$

여기서:
- $S(C) = 1 + \frac{E_{max} \cdot C^n}{EC_{50}^n + C^n}$ (Emax-type 자극)
- $k_{in}$: response의 turnover rate
- $k_{out}$: response의 fractional turnover rate (단위: 시간⁻¹)
- $k_{tol}$: moderator의 fractional turnover rate (tolerance의 시간 척도 결정)
- M의 생성과 소실 모두 같은 $k_{tol}$로 가정 (PD13의 단순화 — 데이터에 더 많은 정보가 있으면 분리)

**기저 조건**: 약물이 없을 때 $S(C) = 1$, R = M, $R_0 = k_{in}/k_{out}$.

**정상상태 응답** (drug 존재 시): R = M이라는 등가 가정 하에:
$$R_{ss} = \frac{k_{in}}{k_{out}} \cdot S(C)$$

이는 tolerance *없는* indirect response와 동일한 정상상태 — 즉 Moderator 모델은 *과도기에만* tolerance를 만들고 정상상태에서는 회복한다 (Fig 3.82 좌측: overshoot → shoulder → tolerance).

**M50을 고려한 더 일반적 형태** [Eq.3:205]:
$$\frac{dR}{dt} = k_{in} \cdot S(C) - k_{out} \cdot M \cdot \left[1 + \frac{M}{M_{50}}\right]$$

M50 = 1 가정 하에 정상상태 R는 *2차 다항식*의 양근:
$$R_{ss} = -\frac{1}{2} + \sqrt{\frac{1}{4} + \frac{k_{in}}{k_{out}} \cdot S(C)} \quad \text{[Eq.3:216]}$$

**반감기 관계** [Eq.3:204]:
$$t_{1/2,k_{out}} = \frac{\ln 2 \cdot R_0}{k_{in} \cdot S(C)}$$

자극 S(C)가 클수록 (강한 약물 또는 고용량) response의 *겉보기 반감기는 짧아진다* — 이것이 high-dose에서 tolerance가 더 빠르게 발달하는 수학적 이유.

**PD13 핵심 수치** [출처: G&W Case Study PD13, Table 13.1, p.808]:

| 파라미터 | Model I (no FB) | **Model II (Moderator)** | Model III (pool) |
|--------|-----|-----|-----|
| kin | 21 ± 10 | **30 ± 5** | 94 ± 10 |
| kout | 7.3 ± 10 | **2.9 ± 6** | 35 ± 9 |
| ktol | — | **4.2 ± 10** | 0.05 ± 60 |
| EC50/IC50 | 390 ± 3 | **350 ± 1** | 270 ± 2 |
| Emax/Imax | 4.8 ± 10 | **9.8 ± 4** | 0.84 ± 1 |
| AIC | −39.0 | **−97.5** | −43.5 |
| WRSS | 0.33 | **0.083** | 0.28 |

**$k_{tol} > k_{out}$ 관찰**: Model II에서 ktol=4.2 > kout=2.9 — tolerance가 R 변화보다 *빠르게* 발달, 그래서 단일 infusion 내에서도 관찰 가능 (G&W p.808 명시).

### B-2. Bauer & Fung Counter-Regulation (CONTEXT — §3.11.6)

Nitroglycerin 모델의 직접적 vasoconstriction 길항은 vasodilation의 적분 출력을 입력으로 받아 vasoconstriction을 생성하는 cascade 구조 [Eq.3:184]. 이는 Moderator 모델의 *변주* — physiological counter-regulation이 명시적으로 별도 compartment로 표현된 형태.

### B-3. Pool/Precursor (CONTEXT — Model III)

Pool 모델 [Eq.3:5–6]:
$$\frac{dP}{dt} = k_{in} - I(C) \cdot k_{tol} \cdot P, \quad \frac{dR}{dt} = I(C) \cdot k_{tol} \cdot P - k_{out} \cdot R$$
PD13에서 WRSS=0.28로 Model II에 명백히 열등 — *완전 tolerance*만 예측, partial tolerance 포착 못함.

### B-4. Colburn-Eldon Time-Dependent Attenuation (CONTEXT — §3.11.3)

$EC_{50}(t) = EC_{50} \cdot [1 + Q \cdot (1 - e^{-K_1 t})]$ [Eq.3:170] — 비기계론적 smoothing, single dose 한정, rebound 미포착. 매우 제한적 사용.

### B-5. Antagonistic Metabolite (CONTEXT — §3.11.4)

Porchet et al [1989] nicotine 모델: 가상의 길항 metabolite가 R을 *상쇄*. Rebound 포착 불가, 매우 경험적 — Moderator 모델에 의해 대부분 대체됨.

### C. Structural Necessity

(1) **두 ODE의 필연**: Tolerance + rebound + AUC asymmetry를 *동시에* 생성하려면 R의 동역학을 시간 지연시키는 추가 상태 변수가 필요하다. 단일 ODE로는 overshoot은 가능하지만 rebound 후 baseline 회귀는 만들 수 없다. M의 적분 메모리가 rebound의 수학적 원천.

(2) **음성 피드백의 필연**: M이 R과 *같은 방향*으로 작용하면 발산 (positive feedback → instability). 음성 부호가 homeostasis의 수학적 강제.

(3) **AUC asymmetry의 필연** [Fig 3.82 좌측 그래프]: AUC_E (response 동안의 area above baseline) > AUC_R (rebound 동안의 area below baseline). 왜? 약물이 R을 직접 자극할 때는 두 효과(약물 + M의 누적)이 모두 작용하지만, 약물 중지 후에는 M의 잔존만 — 비대칭의 수학적 근거.

### D. Assumptions

- $k_{tol1} = k_{tol2}$ (M의 생성·소실 동일 속도) — 데이터에 더 많은 dose level이 있으면 분리 가능
- M50 = 1 (단순화) — 일반 케이스는 Eq.3:205
- $S(C)$는 instantaneous (effect compartment 추가 가능, R&T Ch.8 sluggish system 결합)
- 약물 plasma kinetics는 별도 모델로 driver — table function 또는 closed-form
- Single negative feedback path. 다중 feedback은 더 복잡

### E. Limitations

- Multi-receptor feedback은 ODE 수가 폭증, NONMEM 수렴 불안정
- $k_{tol}$과 $k_{out}$의 식별가능성: 단일 dose 데이터에서 trade-off 강함, **multi-dose 또는 multi-route 설계 필수** (PD13 핵심 교훈)
- Drug effect on $k_{out}$ vs $k_{in}$ vs M turnover 위치 식별: I/O experiment 또는 mechanism 정보 필요
- Circadian rhythm의 time-varying $k_{in}$은 별도 모델

### F. Five Cognitive Layers

| 레이어 | 내용 |
|---|---|
| **L1** | 두 ODE의 결합 시스템; eigenvalue 분석으로 oscillation 가능성 (under-/critically/over-damped) |
| **L2** | Phase plane (R, M)의 trajectory: drug ON → 우상향 spiral, drug OFF → 좌하향 spiral; trajectory가 baseline 통과 후 rebound |
| **L3** | 자동 온도 조절기 (thermostat with delayed sensor), 화학 반응의 Le Chatelier 원리, predator-prey Lotka-Volterra의 damped 변형 |
| **L4** | M = receptor down-regulation (G-protein internalization), enzyme depletion, second-messenger desensitization, antibody formation, metabolic induction (G&W p.285 5가지 메커니즘) |
| **L5** | NONMEM `$DES`: `DADT(2)=KIN*S - KOUT*A(3); DADT(3)=KTOL*A(2) - KTOL*A(3)`; multi-dose simulation 시 R0=KIN/KOUT 초기조건 명시 |

### G. Zettelkasten Atom

```yaml
---
aliases: [Tolerance Model, Moderator M, Negative Feedback PD, Rebound, PD13 Model II]
tags: [pharmacometrics/pd, tolerance, feedback, rebound, indirect-response]
up: "[[MOC — PK-PD Time Delay Models]]"
related: ["[[Effect Compartment]]", "[[Indirect Response 4 models]]", "[[Counter-regulation Bauer-Fung]]", "[[Pool/Precursor model]]", "[[AUC asymmetry]]"]
source: "Gabrielsson & Weiner 5e, Ch.3 §3.11.9–11, pp.297–302; Case Study PD13, pp.805–809"
---

Moderator M 모델은 dR/dt = kin·S(C) - kout·M, dM/dt = ktol·R - ktol·M 의 ODE 쌍으로
tolerance와 rebound를 *동시에* 생성한다. M은 R의 늦게 따라오는 그림자 — 약물이 R을 밀어올리면
M이 천천히 따라 자라며 R을 끌어내린다. 약물 중지 후 M의 잔존이 R을 baseline 아래로 끌어내려 rebound.
PD13에서 Model II (Moderator) AIC=-97.5, WRSS=0.083으로 Model I (no FB), Model III (pool)을 압도.
ktol > kout 관찰 — tolerance가 response 변화보다 빠르게 발달, 단일 infusion 내에서도 관찰 가능.
ktol과 kout의 식별을 위해 multi-dose 또는 multi-route 설계 필수.
```

<!-- TRENCH -->
**Trench-Level Tip**: 임상시험 데이터에서 두 번째 dose의 trough 값이 첫 번째 dose의 trough와 *다르면* (PD13 Fig 13.1 처럼), 이것이 Moderator M 활성화의 직접 시그니처다 — Model II로 즉시 escalate.

<!-- RECAP -->
Tolerance 카드의 한 줄 회수: *Moderator M은 R의 늦게 따라오는 그림자 — 약이 떠난 후에도 그림자는 남는다.*

---

## ━━ 카드 4: Transduction Model — Catenary Transit Compartments ━━

<!-- MASTER LENS -->
### [개념 Big Idea: 거장의 시각]

**왜 치명적으로 중요한가**: PD35 사례 (G&W p.911) — 인간 자원자의 3-dose response 데이터에서 응답 onset이 *15–20시간 지연*되었다. 단순 indirect response (단일 turnover compartment)는 이 lag를 절대 포착하지 못한다 — 모델이 데이터보다 너무 빨리 peak에 도달한다 (Fig 3.59 link-predicted curve와 동일한 시그니처). 신호 전달 cascade — receptor → second messenger → gene transcription → protein synthesis → functional response — 의 *직렬 연결성*을 transit compartment 연쇄로 옮기지 못하면, GPCR 약물의 onset 평가에서 약효 없음으로 오판하고 임상시험을 조기 중단한다.

**체화해야 할 단 하나의 직관**: n개의 transit compartment는 *n개의 sequential 1차 지연*이다. 각 구획의 transit time τ는 동일하고, kout = 1/τ. n이 커지면 onset이 *날카로워지면서 늦어진다* (G&W Fig 3.100 우측: "several and rapid compartments"). n이 작으면 onset이 *완만하면서 일찍* 시작된다 (좌측: "few and slow compartments"). 같은 총 transit time을 어떻게 분할하느냐가 모양을 결정한다.

**이 직관을 박고 아래를 읽어라.** 같은 평균 지연이라도 분할 방식이 곡선 형태를 완전히 바꾼다 — 이것이 transit n 결정의 핵심.

### A. Formal Definition

Transduction Model은 receptor coupling과 observed functional response 사이의 신호 전달 cascade를 *직렬로 연결된 n개의 transit compartment*로 모델링. 각 구획은 동일한 transit time τ를 가지며, fractional turnover rate $k_{out} = 1/\tau$. PD35의 인간 in vivo 데이터에서 n=3이 최적, n=4가 약간 개선, n=5가 악화 — 데이터로부터 결정되는 모델 차원.

### B. Derivation

Receptor compartment $R_e$의 동역학 [출처: G&W 5e, Ch.3, p.911, Eq.35:5]:
$$\frac{dR_e}{dt} = \frac{1}{\tau} \cdot \left( E_0 \cdot S(C) - R_e \right)$$

여기서 $E_0$는 기저값 (baseline), $S(C) = 1 + \frac{E_{max} \cdot C}{EC_{50} + C}$.

Transit chain의 각 구획 [Eq.35:6]:
$$\boxed{\;\frac{dR_i}{dt} = \frac{1}{\tau} \cdot \left( R_{i-1} - R_i \right), \quad i = 1, 2, \ldots, n\;}$$

Observed functional response $R_{obs} = R_n$.

**증폭 변형** [Eq.3:261]:
$$\frac{dR_i}{dt} = \frac{1}{\tau} \cdot \left( R_{i-1}^{\gamma} - R_i \right)$$
γ > 1이면 cascade에 *증폭* 도입.

**PD35 핵심 수치** [출처: G&W Case Study PD35, Table 35.1, p.914]:

| n (transit steps) | EC50 (µg/L) | Emax | τ (h) | E0 (mmHg) | WRSS |
|---|---|---|---|---|---|
| 1 | 0.33 ± 15 | 7.2 ± 12 | 20 ± 5 | 15 ± 11 | 1319 |
| 2 | 0.34 ± 11 | 6.0 ± 8 | 13 ± 3 | 18 ± 7 | 789 |
| **3** | **0.35 ± 10** | **5.4 ± 7** | **9.8 ± 3** | **19 ± 6** | **642** |
| 4 | 0.35 ± 9 | 5.1 ± 6 | 7.8 ± 2 | 20 ± 6 | 632 |
| 5 | 0.34 ± 10 | 4.8 ± 6 | 6.4 ± 2 | 20 ± 5 | 682 |

**관찰**: n=3 vs n=4는 WRSS 차이 미미 (642 vs 632), n=5는 다시 악화 (682) — 모델 복잡도 증가가 *over-fitting*. **실용적 결정: n=3 채택** (parsimony). EC50과 baseline은 n에 거의 무관 — robust 추정. τ는 n과 trade-off (n×τ ≈ 총 transit time 일정).

**PD35 PK 수치**: C0 = 1.05 nmol/L (저용량), 4×1.05 (중간), 16×1.05 (고용량); K = 0.0228 h⁻¹ (t½ ≈ 30 h); 초기 EC50 추정 = 16·1.05·e^(−0.0228·216) ≈ 0.12 nmol/L (216 h 시점에서 50% response 가정).

**중요한 동등성** [G&W p.911 명시]: $k_{out} = 1/\tau$. NONMEM 코드에서 `RATE = 1/TAU`로 표현해도 같은 적합. 단지 parameterization 차이 — τ 표현이 transit time 의미를 명시.

### C. Structural Necessity

(1) **단일 구획으로 불가능한 이유**: indirect response 단일 compartment의 lag time은 본질적으로 $\tau_{single}$이고 onset 곡선은 *exponential approach* — 즉 t=0에서 *최대 기울기*. PD35의 데이터는 t=0에서 거의 평탄하다가 t=15–20h에서 급격히 상승 — 이것은 *sigmoidal* 형태이고 단일 exponential은 만들 수 없다. n개 sequential 1차 시스템의 합성은 gamma 분포의 PDF에 비례 — 지연된 sigmoid 형태.

(2) **동일 τ의 가정**: 각 구획의 transit time이 다르면 (τ1, τ2, ..., τn) 식별가능성 폭발. 동일 τ는 단순화 + identifiability 보장. 데이터에 더 많은 정보가 있으면 분리 가능.

(3) **Sequential vs parallel의 필연**: 직렬 연결만 sigmoidal lag를 생성. 병렬은 단순 평균이고 lag 못 만듦.

### D. Assumptions

- 각 transit step은 동일 τ — 비대칭이면 별도 추정
- Cascade는 *직렬* — branching은 추가 ODE
- $S(C)$는 instantaneous — 분포 지연이 추가로 있으면 ke0 추가 (PK→Ce→receptor→cascade)
- Linear cascade — saturation, Hill 형태, γ exponent로 확장 가능

### E. Limitations

- n과 τ의 trade-off: 같은 전체 lag time을 다른 (n, τ) 조합으로 적합 가능, BIC/AIC로 결정
- 진짜 메커니즘 (몇 단계 cascade인가)을 데이터로부터만 추론 — 생물학적 근거와 별도일 수 있음
- 매우 큰 n에서는 계산 부담 증가, ODE solver 안정성 저하

### F. Five Cognitive Layers

| 레이어 | 내용 |
|---|---|
| **L1** | n개 sequential 1차 시스템의 transfer function: $H(s) = \prod_{i=1}^{n} \frac{1}{1 + \tau s}$ — 합성 응답은 gamma PDF |
| **L2** | Bode plot 의미: -20n dB/decade slope; phase lag = -n·90° at high freq |
| **L3** | 화학공학의 PFR (plug flow reactor) tanks-in-series 모델, 통신공학의 RC delay line, 통계학의 Erlang 분포 (n개 exponential의 합) |
| **L4** | Receptor → G-protein → cAMP → PKA → 표적 단백질 인산화 → 기능적 효과 — 각 단계가 transit compartment. Glucocorticoid receptor → mRNA → 효소 합성 (Ramakrishnan et al [2002]) |
| **L5** | NONMEM `$DES`: `DADT(I+1) = (A(I) - A(I+1))/TAU` 의 do-loop 구조; n을 model selection 변수로 (1, 2, 3, 4, 5 비교) |

### G. Zettelkasten Atom

```yaml
---
aliases: [Transduction Model, Transit Compartment Chain, PD35]
tags: [pharmacometrics/pd, signal-transduction, lag, catenary]
up: "[[MOC — PK-PD Time Delay Models]]"
related: ["[[Indirect Response]]", "[[Effect Compartment]]", "[[Erlang distribution]]", "[[Tanks-in-series]]"]
source: "Gabrielsson & Weiner 5e, Ch.3 §3.13, pp.323–325; Case Study PD35, pp.910–914"
---

Transduction model은 receptor coupling과 observed response 사이의 cascade를 n개 sequential
transit compartment로 모델링. 각 구획은 동일 τ, kout=1/τ. dRi/dt = (R(i-1) - Ri)/τ. 
PD35의 인간 in vivo 데이터에서 n=3 최적 (WRSS=642, n=4 미세 개선 632, n=5 over-fit 682).
같은 총 transit time을 어떻게 n×τ로 분할하느냐가 곡선 형태를 결정 — 작은 n은 완만한 일찍 시작,
큰 n은 날카로운 늦은 시작. 단일 indirect response (n=1)는 PD35의 15-20h sigmoidal lag를 절대 포착 못함.
NONMEM에서는 do-loop 구조로 구현; n을 model selection 변수로.
```

<!-- RECAP -->
Transduction 카드의 한 줄 회수: *같은 평균 지연도 분할 방식에 따라 곡선 형태가 완전히 다르다 — n과 τ는 trade-off, 데이터가 결정한다.*

---

# §5 — Confusion Pair Dissection

본 세션에서 진정으로 혼동 가능한 4개 쌍을 식별, 마스터 모델러가 5초 내에 구분하는 진단 도구를 제공한다.

---

<!-- CONFUSION -->
## Pair 1: $k_{e0}$ (Link / Distribution Delay) vs $k_{out}$ (Turnover / System Delay) ⚠️ Critical Blow

| 비교 차원 | $k_{e0}$ (Effect Compartment) | $k_{out}$ (Indirect Response) |
|------|----|----|
| **표면적 유사성** | 두 개 모두 1차 속도상수, 단위 시간⁻¹, response의 time delay를 만든다, hysteresis loop을 생성한다 — *모양만 보면 거의 동일하게 보인다* | |
| **수식/코드 형태** | $\frac{dC_e}{dt} = k_{e0}(C - C_e)$ | $\frac{dR}{dt} = k_{in} - k_{out} \cdot R$ (또는 $\cdot S(C)$ 자극 항) |
| **생리학적/구조적 지시체** | Plasma와 biophase 사이 *물리적* 분포 다리 (perfusion + diffusion + tissue binding) | Endogenous substance의 *생산-소실* 회전 (synthesis/degradation rate) |
| **변화 방향 — Dose↑ 시** | $t_{max,response}$ *불변* (수학적으로 dose-independent) | $t_{max,response}$ *peak shift* — dose↑ 시 saturation에 따라 시간 이동 가능 |
| **임상/모델링 결과** | $t_{1/2,k_{e0}}$는 분 단위 (G&W Table 3.9: terbutaline 7.5min, fentanyl 6.4min) | $t_{1/2,k_{out}}$는 시간~일 단위 (warfarin clotting factor 1–2 days) |
| **혼동 시 치명적 오류** | Link 모델을 turnover 데이터에 적용 → **EC50가 dose마다 분기** (PD13 Table 3.10: dose 1 → EC50=0.681, dose 10 → 4.85, dose 100 → 0.941, **7배 분기**) | |
| **⚡ 기억 고리** | $k_{e0}$는 *약물의 여행 시간* (다리 길이) — dose 무관 고정. $k_{out}$은 *시스템의 기억* (댐 수위) — dose에 따라 채워지는 시간 다름. 다리 길이는 변하지 않지만, 댐은 dose-dependent하게 차오른다. | |
| 🔴 **Critical Blow** | NDA 제출에서 turnover 시스템 데이터에 Link 모델을 적용했을 때, 심사관이 dose-stratified individual fit 결과를 보고 "EC50가 dose마다 변동하는 것은 *biologically implausible* — receptor sensitivity가 dose에 의존할 수 없다"고 Deficiency Letter 발행. 모델 재구축으로 6개월 지연, 환자 등록 중단, 시판 일정 표류. (G&W §3.9.7 직접 인용: "biologically implausible situation where sensitivity IC50/EC50, the capacity Emax, and the n value for a system change with dose") | |

---

<!-- CONFUSION -->
## Pair 2: Counterclockwise vs Clockwise Hysteresis

| 비교 차원 | 반시계 (Counterclockwise) | 시계 (Clockwise) |
|------|----|----|
| **표면적 유사성** | 둘 다 hysteresis loop, 둘 다 time delay 시그니처 — loop이 닫혀있는 것만 보면 같은 현상으로 보인다 | |
| **Plot 위 거동** | Response가 concentration보다 *뒤따라온다* — 같은 농도에서 상승 phase보다 하강 phase의 response가 더 크다 | Response가 concentration보다 *먼저 빠진다* — 같은 농도에서 하강 phase의 response가 더 작다 |
| **생리학적 지시체** | (i) 분포 지연, (ii) Indirect response, (iii) Slow on-rate, (iv) Concordant active metabolite | (i) Tolerance/desensitization, (ii) Antagonistic metabolite, (iii) Receptor down-regulation |
| **임상 표준 사례** | Naproxen (R&T Fig 8-2), digoxin (Fig 8-1), warfarin (Fig 8-10), aspirin (Fig 8-20) | Cocaine acute tolerance (G&W Fig 3.80 우측), nitroglycerin tolerance, β-agonist desensitization |
| **혼동 시 결과** | 반시계를 시계로 잘못 읽으면 → tolerance 모델로 시작 → 데이터에 적합 안 됨 → 진단 30분 잘못된 방향 | 시계를 반시계로 잘못 읽으면 → distribution delay 가정 → tolerance 발견 못함 → multi-dose simulation 실패 |
| **⚡ 기억 고리** | 화살표 방향은 *시간의 굴절 방향*이다. 반시계 = "시스템이 plasma보다 *느리다*" — 다리를 건너거나 댐에 차오르는 데 시간 걸림. 시계 = "시스템이 plasma의 효과를 *상쇄*한다" — 길항 또는 적응. 시간이 어느 쪽으로 휘는가가 메커니즘 패밀리를 가른다. | |

---

<!-- CONFUSION -->
## Pair 3: Tolerance (Dosing 동안의 attenuation) vs Rebound (Dose 중지 후의 overshoot)

| 비교 차원 | Tolerance | Rebound |
|------|----|----|
| **표면적 유사성** | 같은 Moderator M 모델에서 동시 발생, 같은 ODE 쌍에서 둘 다 자연스럽게 emergence — *분리된 두 현상*처럼 가르치지만 *수학적으로 같은 phenomenon의 두 phase* | |
| **시간 phase** | Drug dose 동안: R이 overshoot 후 PD steady-state로 *내려간다* (tolerance) | Drug dose 중지 후: R이 baseline *아래로* 떨어졌다 회귀 (rebound) |
| **Moderator M의 상태** | Drug ON 동안 M이 *천천히 따라잡으며* R을 끌어내림 | Drug OFF 시점에 M이 *아직 높은* 상태로 남아 있음 — 자극은 사라졌지만 그림자는 남아 R을 baseline 아래로 끌어내림 |
| **AUC 거동** | $AUC_{response}$ (response phase) | $AUC_{rebound}$ (rebound phase) — 항상 더 작다 (Fig 3.82 명시: $AUC_R < AUC_E$) |
| **임상 현현** | Nitroglycerin 두통이 며칠 후 사라짐, β-agonist 효과 감소 | Nitroglycerin 작업자의 주말 angina (G&W Fig 3.71), clonidine 중지 후 혈압 reactive 상승, opioid withdrawal |
| **혼동 시 결과** | Tolerance만 모델링하고 rebound 무시 → multi-dose simulation에서 dose holiday의 위험 과소평가 → 환자에게 rebound 사고 | |
| **⚡ 기억 고리** | Tolerance와 Rebound는 *같은 그림자(M)의 두 상태*다. 약이 비추는 동안 그림자가 자라며 빛을 흐리게 한다 (tolerance). 약이 사라지면 그림자는 *남아서 어둠을 만든다* (rebound). 빛(drug)과 그림자(M)의 시간 차이가 두 phenomenon 모두를 한 번에 생성. | |

---

<!-- CONFUSION -->
## Pair 4: Distribution Delay (Link, single ke0) vs Sequential Cascade (Transduction, n×τ)

| 비교 차원 | Single ke0 (Link) | n × τ (Transduction) |
|------|----|----|
| **표면적 유사성** | 둘 다 onset lag을 만들고, 반시계 hysteresis를 생성 | |
| **수학 구조** | 단일 1차 ODE → exponential approach (t=0에서 *최대 기울기*) | n개 sequential 1차 → gamma PDF 형태 (t=0에서 *0 기울기*, sigmoidal lag) |
| **곡선 형태** | Onset이 *즉시* 시작하며 점근선으로 부드럽게 접근 | Onset이 *지연되어 시작*, 일정 시간 후 *급격히* 상승 |
| **임상 표준 사례** | succinylcholine 4 min, fentanyl spectral edge 6.4 min (G&W Table 3.9) | PD35의 15–20시간 onset delay |
| **n=1 vs n>1 진단** | n=1로 적합 시 데이터의 *t=0 부근 평탄 구간*을 포착 못함 (PD35: WRSS 1319) | n=3 적합 시 WRSS 642 — 같은 데이터에서 2배 개선 |
| **혼동 시 결과** | PD35-type 데이터에 Link 모델 적합 → onset이 너무 빠르게 예측 → 임상시험 onset 평가 시점 잘못 잡음 → 약효 없음으로 오판하고 trial 조기 중단 | |
| **⚡ 기억 고리** | Single ke0는 *하나의 다리* — 즉시 출발해서 점차 도달. n×τ는 *n개의 다리 연속* — 끝 도달까지 모든 다리를 통과해야 하므로 처음에는 도달자가 없다가 일정 시간 후 *몰려서* 도착. 같은 평균 시간이라도 분할 방식이 곡선 형태를 완전히 바꾼다. | |

---

# §7 — Self-Test: Active Recall Module

비율: 40% 회상 / 60% 적용. 마지막 질문은 보스 딜레마 (Socratic Dilemma).

---

<!-- SELF-TEST -->
**Q1 [회상 / ★★]**: Effect compartment의 ODE 형태(Eq.3:143)를 *기억으로부터* 재현하라. 그리고 closed-form 해 $C_e$ (Eq.3:134)에서 $k_{1e} = k_{e0}$ 가정이 *왜* 강제되는지 한 문장으로 설명하라.

> **정답 공개**: $\frac{dC_e}{dt} = k_{e0} \cdot C - k_{e0} \cdot C_e$. Closed-form은 $C_e = \frac{k_{e0} \cdot D}{V_c (k_{e0} - K)}[e^{-Kt} - e^{-k_{e0}t}]$. $k_{1e} = k_{e0}$ 가정의 이유: identifiability problem — 두 파라미터가 정상상태에서 *질량 보존*을 통해서만 연결되어 있어 데이터로 분리 추정 불가능 + $V_e = V_c \cdot K_p$ 가정이 동시에 강제된다.
> **다음 깊이 질문**: $K_p \neq 1$인 약물에서 추정된 EC50는 무엇을 의미하는가?

---

<!-- SELF-TEST -->
**Q2 [회상 / ★]**: Moderator M 모델의 ODE 쌍을 기억으로부터 쓰라. 그리고 정상상태에서 $R = M$이라는 결론이 *왜* 성립하는지 설명하라.

> **정답 공개**: $\frac{dR}{dt} = k_{in} S(C) - k_{out} M$, $\frac{dM}{dt} = k_{tol} R - k_{tol} M$. 정상상태에서 두 ODE 모두 0 → $k_{tol}(R - M) = 0$ → $R = M$ (단, $k_{tol} \neq 0$). 이는 M의 생성과 소실이 *같은* $k_{tol}$로 가정되었기 때문 — 두 별도 상수 $k_{tol1}, k_{tol2}$로 분리하면 $R = M$이 더 이상 강제되지 않음.
> **다음 깊이 질문**: M50 ≠ 1인 일반 케이스 (Eq.3:205)에서 정상상태 R는 왜 2차 다항식의 양근 형태를 갖는가?

---

<!-- SELF-TEST -->
**Q3 [회상 / ★]**: Transduction 모델 (PD35)에서 transit compartment 수 n과 transit time τ 사이의 관계를 설명하라. PD35에서 n=3 vs n=4 vs n=5의 WRSS를 외워라.

> **정답 공개**: 각 구획의 fractional turnover rate $k_{out} = 1/\tau$ — 동등 표현. PD35 WRSS: n=1 → 1319, n=2 → 789, **n=3 → 642**, n=4 → 632, n=5 → 682. n=3과 n=4는 거의 차이 없음, n=5는 over-fitting으로 악화. 실용 결정: n=3 (parsimony principle). 총 transit time ≈ n·τ는 모델 간에 거의 일정 (≈ 30 h), 분할 방식만 다름.
> **다음 깊이 질문**: n×τ가 같다면 두 모델이 동등할 텐데 왜 onset 곡선 형태가 다른가?

---

<!-- SELF-TEST -->
**Q4 [적용 / ★★]**: 임상시험 데이터에서 plasma concentration vs response plot의 chronological arrow가 *시계 방향(clockwise)*임을 관찰했다. 가능한 메커니즘 3가지를 나열하고, 각각을 구분하기 위해 추가로 어떤 데이터/실험이 필요한지 명시하라.

> **정답 공개**: (i) **Tolerance/desensitization** — multi-dose 또는 long infusion에서 tolerance 발달 확인, $k_{tol}$ 추정 가능 여부 검토 (PD13 Model II 적합). (ii) **Antagonistic metabolite** — metabolite plasma 추적 + metabolite의 in vitro 약리학적 길항 확인. (iii) **Receptor down-regulation** — receptor density 직접 측정 또는 회복 시간이 receptor 합성 시간과 일치하는지 검정. 추가 도구: dose-stratified individual fit으로 EC50 분기 검사, washout phase의 rebound 관찰 여부, mechanism-specific in vitro assay.
> **다음 깊이 질문**: 시계 방향 hysteresis와 antagonistic metabolite를 in vitro 정보 없이 in vivo 데이터만으로 구분할 수 있는가?

---

<!-- SELF-TEST -->
**Q5 [적용 / ★★]**: 한 임상시험에서 한 약물의 IV bolus dose 1, 4, 16 mg을 투여하고 각각의 response time course를 기록했다. 세 dose 모두에서 *peak response가 정확히 t = 12 h*에서 발생했고, 같은 데이터를 dose-stratified individual fit (Link 모델)했을 때 EC50 = 0.5, 0.5, 0.5로 *일관*되게 추정되었다. 이 데이터에 적합한 모델 패밀리는? 그 이유는?

> **정답 공개**: **Effect Compartment (Link) 모델 적합**. 진단 근거: (i) $t_{max}$가 dose-invariant — Link 모델의 핵심 시그니처 (Eq.3:126의 가정에서 도출되는 결론). (ii) EC50가 dose에 무관하게 일관 — turnover 시스템이라면 PD13처럼 분기될 것. 이 두 조건이 모두 만족되면 Link 모델이 정당. 추가 검증: hysteresis collapse method로 ke0 추정 후 단일 EC50, Emax 동시 적합 시 fit 양호 여부 확인.
> **다음 깊이 질문**: 만약 EC50는 일관인데 $t_{max}$가 dose마다 다르다면? 어느 가정이 깨진 것인가?

---

<!-- SELF-TEST -->
**Q6 [적용 / ★]**: PD13 Case Study의 Model II 결과 ($k_{tol} = 4.2 > k_{out} = 2.9$ h⁻¹)를 보고, 이 약물의 multi-dose simulation에서 *처음 dose의 trough 값과 두 번째 dose의 trough 값*이 같을지 다를지 예측하라. 이유와 함께.

> **정답 공개**: **두 trough 값은 다르다**. 이유: $k_{tol} > k_{out}$이므로 tolerance 발달이 response 변화보다 *빠르다*. 첫 번째 infusion 동안 M이 이미 높은 수준으로 발달, 두 번째 infusion 시작 시 M이 (washout이 충분치 않아) 여전히 높은 상태에서 시작 → 두 번째 trough가 첫 번째보다 *더 깊다* 또는 다르다 (carry-over). PD13 Fig 13.1에서 직접 관찰됨 — "the trough value is not the same during the second infusion regimen as it was in the first" (G&W p.808 명시). 이 carry-over 자체가 Moderator 활성화의 시그니처.
> **다음 깊이 질문**: 이 carry-over 효과를 제거하려면 두 infusion 사이에 얼마의 washout이 필요한가? (힌트: $t_{1/2,k_{tol}}$의 몇 배?)

---

<!-- SELF-TEST -->
**Q7 [적용 / ★★]**: PD35-type 데이터 (15–20 h sigmoidal lag onset)를 받았는데, 단일 indirect response 모델 (n=1)로만 적합 가능한 NONMEM 환경이라고 가정하자. (n>1 transit chain을 코딩할 수 없는 제약). 이 경우 fit이 데이터에 *어떤 시그니처 GOF 패턴*을 만들어낼지 예측하고, 이 misspecification을 reviewer에게 어떻게 정당화하지 않을지 제시하라.

> **정답 공개**: **GOF 시그니처**: (i) early time points (t < 10 h)에서 *systematic positive residuals* — 모델이 너무 일찍 response 상승을 예측. (ii) peak 부근에서 underprediction — 데이터의 sharp rise를 단일 exponential approach가 못 따라감. (iii) CWRES vs time plot에서 *S자 곡선 패턴* — under-over-under 패턴. (iv) IPRED vs DV plot에서 systematic deviation. **정당화 불가**: reviewer에게 "n=1로 한정된 코딩 환경"은 핑계가 되지 않음 — Model misspecification은 mechanism 정보 손실. 옳은 대응: 별도 환경에서 n=2, 3, 4 비교하여 ΔOFV로 결정. PD35는 n=1 → n=3 시 WRSS가 1319 → 642로 *2배 개선*, 이것은 통계적으로 유의한 model improvement.
> **다음 깊이 질문**: 만약 n과 τ가 trade-off로 비식별이면 어떤 외부 정보 (mechanism, prior data)로 결정해야 하는가?

---

<!-- SELF-TEST -->
**Q8 [적용 / ★]**: R&T Ch.8 Fig 8-11에서 acenocoumarol (t½ = 15 h)과 phenprocoumon (t½ = 5 days)은 같은 메커니즘 (clotting factor 합성 억제)으로 작용하지만 baseline 회귀 시간이 *3 days vs 2 weeks*로 매우 다르다. 두 약물의 baseline 회귀를 *각각 무엇이* rate-limit하는가?

> **정답 공개**: **Acenocoumarol (t½=15h)**: baseline 회귀가 **clotting factor turnover (kout)**에 의해 rate-limited. 약물이 빠르게 제거되어 24 h 시점부터 더 이상 inhibition 없음, 이후 회귀는 prothrombin complex의 t½ ≈ 1–2 days에 의해 결정. **Phenprocoumon (t½=5 days)**: baseline 회귀가 **drug elimination (k)**에 의해 rate-limited. 약물이 너무 천천히 제거되어 inhibition이 계속 작용, clotting factor turnover보다 drug clearance가 *느려서* 회귀 시간을 지배. 일반 원칙 (R&T Ch.8): 회귀는 *둘 중 더 느린 process*에 의해 결정 — kinetics와 dynamics 중 어느 쪽이 rate-limiting인가가 약물에 따라 다름.
> **다음 깊이 질문**: warfarin (t½=1.5 days)은 두 한계의 *경계*에 있다. 이것이 임상적으로 어떤 의미를 갖는가? (왜 warfarin 용량 조절이 까다로운가?)

---

<!-- SELF-TEST -->
**Q9 [적용 / ★★]**: 한 약물이 hysteresis loop을 보이는데, 같은 약을 *다른 두 환자*에서 측정하니 한 명은 반시계, 다른 한 명은 시계 방향이었다. 가능한 설명을 2가지 제시하라.

> **정답 공개**: **(i) 두 메커니즘의 동시 작용 (figure-eight 가능성)**: 약물이 distribution delay와 tolerance를 *동시에* 만들 때, dose level과 시간 척도에 따라 두 환자에서 다른 phase가 dominant하게 보일 수 있음. 한 환자에서는 distribution delay phase가 관찰 (반시계), 다른 환자에서는 tolerance phase가 빨리 발달 (시계). 같은 데이터를 더 길게 관찰하면 figure-eight가 보일 수 있음. **(ii) 환자 간 PK 차이**: 한 환자가 약물 입력 속도가 distribution rate보다 *느리면* (slow oral absorption, slow infusion) 시계 방향이 나타나고 (R&T Ch.8 명시: "rate of input is more rapid than the rate of distribution or tolerance development"), 다른 환자에서 입력이 빠르면 반시계가 dominant. 이는 *individual covariate effects* (e.g., gastric emptying, hepatic metabolism)와 연결.
> **다음 깊이 질문**: 환자 간 hysteresis 방향 변동이 NONMEM의 IIV (interindividual variability)로 어떻게 표현되어야 하는가?

---

<!-- SELF-TEST -->
**Q10 [보스 딜레마 / ★★]**: **모델 선택의 Trade-off 정상회담**

당신은 항우울제 신약 X의 Phase 2b 임상시험 데이터를 분석 중이다. 데이터는 4개 dose level (10, 30, 100, 300 mg)에서 각각 100 환자, MADRS (우울 척도) 시간 변화를 28일간 측정한다. 두 모델 후보가 있다:

**Model A — Effect Compartment (Link) Model**:
- ODE 1개 추가 (ke0)
- 적합 결과: NONMEM 수렴 안정적, $COV step 성공, OFV = -2,450, 모든 환자에서 $t_{max,response}$가 dose에 무관하게 ≈ 14일.
- **그러나**: dose-stratified individual fit 시 EC50가 dose 1 → 30 nM, dose 2 → 45 nM, dose 3 → 25 nM, dose 4 → 60 nM로 *2배 분기*.

**Model B — Indirect Response with Moderator M (Tolerance)**:
- ODE 2개 추가 (kout, ktol)
- 적합 결과: OFV = -2,520 (Model A보다 70 좋음, ΔOFV → χ² 검정 p < 0.001 유의), 그러나 NONMEM 수렴이 종종 실패 (10번 중 4번), $COV step 50% 실패율, 모든 환자에서 단일 EC50 = 35 nM 추정 (CV 12%).

**FDA 제출 90일 전이다.** Final model로 Model A와 Model B 중 어느 쪽을 선택하는가? 그리고 그 선택을 NDA의 Population Pharmacokinetic-Pharmacodynamic Report에서 어떻게 *방어*하는가?

> **정답 공개 — 수석 모델러의 Trade-off 논리**:
>
> **결정: Model B를 선택한다 (특정 조건 하에).** 그러나 단순한 답은 없다 — 두 옵션 모두 위험을 내포.
>
> **Model A를 선택한 경우의 위험**: EC50가 dose에 따라 2배 분기 — 이는 G&W §3.9.7의 PD13 참사와 정확히 동일 시그니처. FDA 심사관이 dose-stratified subgroup analysis를 (반드시) 요구하면 즉시 노출됨. "Receptor sensitivity가 dose에 의존하는 것은 biologically implausible"의 표준 Deficiency Letter 문구가 곧장 적용 — 6개월 지연, label 변경, 시판 일정 표류. 이는 *과학적 무결성 위반*에 가까운 risk.
>
> **Model B를 선택한 경우의 위험**: $COV step 50% 실패는 confidence interval 추정 불가 → label에 명시할 PK/PD parameters의 정밀도 보고 불가. ICH E9(R1) 및 FDA Population PK guidance 위반 risk.
>
> **거장의 합의된 해법 — 단계적 escalation**:
> 1. **Model B의 수렴 안정화 작업 우선 수행** — initial estimates 개선 (sensitivity analysis로 $k_{tol}$ 초기값 sweep), $\eta$ correlation 점검 후 OMEGA block 재구성, MU-referencing으로 covariate model 정리, FOCE → FOCE-I 또는 SAEM 전환 검토. 이 작업에 2–3주 투입.
> 2. **Bootstrap 또는 SIR (Sampling Importance Resampling) 활용** — $COV step 실패 시 95% CI 추정의 백업 도구. NONMEM 7.5의 BAYES 옵션 검토.
> 3. **그래도 수렴이 안정되지 않으면**: 두 모델 모두 보고서에 포함, **Model B를 primary, Model A를 sensitivity analysis로**. NDA에 두 모델의 결과를 *투명하게* 제시하고, "EC50의 dose-dependence는 Model A의 misspecification 시그니처이며, mechanistically valid한 Model B가 단일 EC50를 산출했음을 보여준다"고 서술.
> 4. **규제 방어 언어** (실제 NDA 제출 문구):
>    > "The effect compartment (Link) model fit demonstrated dose-stratified EC50 variation, which is biologically implausible for a single mechanism. The indirect response model with feedback (Moderator) was therefore selected as the primary model, supported by the consistent EC50 estimate across all dose groups. Model B's superior fit was confirmed by a likelihood ratio test (ΔOFV = 70, p < 0.001). Limited convergence robustness in the Moderator model was addressed through bootstrap-based parameter precision estimation and is fully documented in Appendix X."
>
> **핵심 교훈 — ICH E9(R1) 정신**: *Statistical convenience가 mechanistic validity를 절대 우선할 수 없다.* PD13의 EC50 분기는 단순한 통계 노이즈가 아니라 *모델 misspecification의 직접 증거*. 이를 알면서 Model A를 final로 제출하는 것은 윤리적 문제에 가까움. 거장은 모델 misspecification을 *수정*하지, *덮지* 않는다. NONMEM 수렴 문제는 기술적 challenge — 해결책이 있다 (bootstrap, SIR, SAEM). 모델 misspecification은 *과학적* problem — 해결책이 없다 (다른 모델로 가야 함).
>
> **만약 시간 압박이 더 심해서 Model B 안정화가 불가능하다면**: regulatory pre-submission meeting (Type B)을 즉시 요청하여 FDA division과 사전 합의. 단독 결정으로 제출하지 말 것. — 이것이 *진짜* 수석 모델러의 행동.

---

# §8 — Meta-Frame & Big Picture

## A. Positioning

이 세션은 28-세션 PK/PD Mastery Architecture의 *기둥 세션*이다. 전체 지식 그래프에서:

- **이전 세션이 만들어 준 기반**: §3.2 Emax/Hill 방정식 (S(C) 함수의 형태), §3.7 Indirect Response 4 모델 (kin/kout 회전 구조와 4가지 약물 작용점), 1·2 구획 PK ODE 및 Bateman 방정식.
- **이 세션이 새로 짓는 것**: 시간 지연을 *세 가지 메커니즘 패밀리*로 분류하는 능력 — Link (분포), Turnover/Moderator (시스템 적응), Transit Cascade (신호 전달 연쇄). 각 패밀리의 ODE 시그니처와 진단 도구.
- **바로 다음 세션이 의존하는 것**: TMDD 모델은 Link 모델의 분포 지연 + Receptor binding kinetics + Saturable 결합을 동시에 통합한다. 이 세션의 카드 1과 2를 체화하지 않으면 TMDD의 quasi-equilibrium / quasi-steady-state / Michaelis-Menten approximation 사이 결정이 *완전히 안개*에 들어간다.
- **고급 도메인이 결정적으로 의존하는 것**:
  - **PopPK/PD 통합 모델링**: NONMEM에서 covariate model 구축 시 시간 지연 메커니즘을 식별하지 못하면 IIV가 inflate되어 fit이 망가진다.
  - **PBPK + PD coupling**: 조직 농도가 effect compartment를 대체할 때 ke0의 생리학적 해석 (perfusion + diffusion + binding)이 직접적 사용.
  - **QSP (Quantitative Systems Pharmacology)**: cascade 신호 전달의 transit chain은 QSP 모델의 핵심 building block.
  - **임상 약물 상호작용 평가**: tolerance/feedback 약물의 DDI는 단순 PK 수준을 넘어 PD 수준까지 시뮬레이션 필요.

## B. Dependencies — 이 세션을 대충 넘겼을 때의 실패 모드

**실패 모드 1: TMDD 모델에서 Receptor Binding과 Distribution Delay 혼동**.
TMDD는 (a) drug-target binding ($k_{on}/k_{off}$), (b) target turnover ($k_{deg}$), (c) drug elimination ($k_e$), (d) distribution delay (선택적 effect compartment)를 동시에 다룬다. 이 세션의 카드 1과 2를 체화하지 못한 모델러는 koff와 ke0를 단위만으로 구분하지 못해 TMDD에서 두 파라미터를 혼동, 결과적으로 binding kinetics를 distribution delay로 오인하여 receptor 동역학에 대한 *완전히 잘못된* 결론에 도달. 추적 가능한 인과: PD21이 보여준 ke0 = 0.025, kout = 0.031, koff = 0.018 min⁻¹의 *수치적 근접성*이 함정.

**실패 모드 2: Long-term clinical PK/PD simulation에서 Tolerance 미반영**.
6개월 chronic dosing 임상시험을 single-dose Link 모델로 외삽하면, 실제로는 tolerance가 발달하여 효과가 50% 이하로 감소하는데도 모델은 *steady-state response*를 일정하게 예측. 결과: Phase 3 design에서 dose-titration 일정을 잘못 설정, primary endpoint 미달, 임상시험 실패. 이것은 G&W §3.11의 핵심 메시지 — "tolerance를 모델링하지 못하면 long-term efficacy 예측은 환상".

**실패 모드 3: GPCR 또는 nuclear receptor 약물의 onset 시간 misprediction**.
Cascade 신호 전달이 있는 약물 (corticosteroid, thyroid hormone analog, antidepressant)을 단일 indirect response로 모델링하면 PD35의 sigmoidal lag를 포착 못함. 임상시험 efficacy 평가 시점을 lag 이전에 설정 → 약효 없음으로 잘못 결론 → drug development pipeline에서 promising compound 탈락.

## C. Professional Moat

> *"NONMEM을 실행하고 GOF 플롯을 생성할 수 있는 주니어 모델러와, multi-compartment ODE를 적합시킬 수 있는 AI가 이미 존재한다. 이 섹션의 원리를 — 메커니즘이 아닌 구조적 이해의 수준에서 — 진정으로 내면화한 연구자는 그 둘 중 어느 것도 복제할 수 없는 무엇을 갖고 있는가?"*

이 세션 내용에 대한 직접·구체적 답:

**그 연구자는 임상시험 데이터의 hysteresis loop을 5초 안에 보고**, $t_{max}$ peak shift 검정 한 가지로 Link / Turnover 분기를 결정하며, dose-stratified individual fit에서 EC50가 dose에 따라 분기하는 *biologically implausible* 시그니처를 *데이터를 보기도 전에* 예측한다. 이 능력은 PD13 Table 3.10을 외워서 얻어지지 않는다 — 그것은 Effect Compartment 모델의 $k_{1e} = k_{e0}$ 제약이 *물리적 질량 보존*에서 도출된 것임을 알고, 이 제약이 깨지는 순간 모델 자체가 *가짜*가 되는 것을 ODE 수준에서 보는 능력이다.

**그 연구자는 NDA 심사관의 Deficiency Letter를 받기 *전에***, 자신의 모델이 PD13 패턴을 만들어낼지 *시뮬레이션 단계에서* 미리 진단한다. AI는 데이터로부터 모델을 적합할 수 있지만, "이 모델이 생성한 EC50의 dose-dependence가 ICH E9(R1)의 mechanism validity 요건과 충돌하는가"를 자율적으로 판단하지 못한다. 이 판단은 G&W의 §3.9.7과 R&T Ch.8의 hysteresis 진단을 *통합*한 사람만이 할 수 있다.

**그 연구자는 Phase 2b → Phase 3 transition 결정 회의에서**, "tolerance 발달이 long-term efficacy를 50% 감소시킬 가능성"을 PD13 Model II의 ktol/kout 비율로부터 *계산*하고, dose titration schedule을 mathematically grounded하게 설계한다. 이는 카드 3의 Moderator M 모델을 단순히 "tolerance 모델"로 외운 사람은 할 수 없는 작업 — 두 ODE의 결합 시스템에서 carry-over 효과의 시간 척도를 phase-plane 분석으로 추론하는 능력이 필요하다.

**그리고 가장 결정적으로**, 그 연구자는 NONMEM 수렴 실패 vs 모델 misspecification을 구분한다. 주니어 모델러는 둘 다 "fit이 안 된다"로 본다. AI는 OFV와 GOF로 모델을 비교한다. 거장은 *수렴 실패는 기술적 problem이고 misspecification은 과학적 problem*임을 안다 — 전자는 해결책이 있고 (bootstrap, SAEM, initial estimate 개선), 후자는 해결책이 없다 (다른 모델로 가야 함). PD13에서 EC50가 dose에 따라 분기하는 것은 *수렴이 잘 되어도* 잘못된 모델의 시그니처라는 사실을 — 이 세션을 체화한 사람만이 ODE 수준에서 본다.

---

```
---
✦ STEP 1 완료.

다음이 준비되었습니다:
  • §1 세션 헤더 & 로드맵 (Big Idea: hysteresis 시간 지연 3대 메커니즘 분류)
  • §2 개념 해부 카드 (4개 개념, Apex: Effect Compartment Model & ke0)
    - 카드 1: Effect Compartment & ke0 [⚡ Apex] — Plausible Fallacy: PD13 EC50 용량 분기
    - 카드 2: Hysteresis 방향 판별 (시계/반시계)
    - 카드 3: Tolerance/Rebound — Moderator M Model
    - 카드 4: Transduction — Catenary Transit Compartments
  • §5 혼동 쌍 해부 (4개 쌍, Critical Blow 적용: ke0 vs kout)
    - Pair 1: ke0 (Link) vs kout (Turnover) ⚠️ Critical Blow — NDA Deficiency Letter
    - Pair 2: Counterclockwise vs Clockwise Hysteresis
    - Pair 3: Tolerance (during dosing) vs Rebound (after cessation)
    - Pair 4: Single ke0 vs n×τ Transit Cascade
  • §7 자기 테스트 (10개 질문, 보스 딜레마 포함 — Model A vs Model B regulatory dilemma)
  • §8 메타프레임 & 빅 픽처 (TMDD/PopPK/QSP로의 전이 명시)
  • 감지된 소스 유형: 혼합 [G&W primary — 수식·실험 데이터 / R&T secondary — 임상 hysteresis 진단 논리]
  • Data Anchoring 소스: G&W PD13 (Table 13.1: Model II AIC=-97.5, ktol=4.2, kout=2.9), 
    PD20 (analgesic IV bolus 45 µg/kg, ke0≈0.1 h⁻¹), PD21 (rabbit oral 1·2 µmol/kg antagonist X, 
    ke0=0.025, kout=0.031, koff=0.018 min⁻¹), PD35 (human male, 3 doses C0=1.05·{1,4,16} nmol/L, 
    K=0.0228 h⁻¹, n=3 optimal WRSS=642), G&W Table 3.9 (terbutaline FEV-1 7.5 min, fentanyl 6.4 min,
    QT-quinidine 8 min); R&T Ch.8 (digoxin Fig 8-1, naproxen Fig 8-2, warfarin Fig 8-10, 
    aspirin Fig 8-20, succinylcholine Fig 8-18/8-24, acenocoumarol vs phenprocoumon Fig 8-11)
  • Marker 시스템: <!-- MASTER LENS --> 4개, <!-- ANCHOR --> 1개, <!-- TRENCH --> 2개,
    <!-- CONFUSION --> 4개, <!-- SELF-TEST --> 10개, <!-- RECAP --> 4개
  • FIGURE markers: 0개 (Phase 4C 전담 — 의도적 누락)

Phase 2 (Source Fidelity Audit, Gemini Pro)로 다음 단계 진행 권장:
  - T1 Equation/Numerical Verification (특히 PD13 Table 13.1, PD35 Table 35.1 수치 대조)
  - T5 Coverage Audit (§3.10 의도적 제외 정당성, §3.11.2 Systems analysis 흡수 적절성 검토)
  - T6 Figure Inventory (G&W Fig 3.51, 3.52, 3.59, 3.71, 3.72, 3.74, 3.79, 3.80, 3.82, 3.98, 3.100; 
    R&T Fig 8-1, 8-2, 8-10, 8-11, 8-13, 8-14, 8-18, 8-20, 8-22 — visual inspection 필요)
---
```

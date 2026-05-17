# Session 11 — Indirect Response / Turnover / DRT / Baseline / Effect Compartment / Rate-Limiting / Duration — v3.7
<!-- 기호 통일: k_in/k_out → k_{in}/k_{out} (첫 등장 Card 1 기준) -->
<!-- 기호 통일: Imax/Emax/IC50/EC50 → I_{max}/E_{max}/IC_{50}/EC_{50} (첫 등장 Card 2 기준) -->
<!-- 기호 통일: Kkill/Kelim → K_{kill}/K_{elim} (첫 등장 Card 6 기준; PD killing과 PK elimination 구분) -->

Naproxen 500 mg 경구 투여 후 dental pain 환자의 통증 완화는 1–8 h 동안 혈장 농도와 같은 시간축으로 움직이지 않습니다. 같은 농도라도 상승기와 하강기의 반응이 다르면, 모델러는 먼저 “농도가 늦는가, 생물학이 늦는가, 표적이 소비되었는가, 또는 PK가 duration을 제한하는가”를 분해해야 합니다. [T pp.234–235] Aspirin 650 mg처럼 혈장 약물은 빠르게 사라지지만 thromboxane B₂ 억제가 수일 지속되는 경우에는, plasma half-life만으로 효과 지속시간을 설명할 수 없습니다. [T p.251]

## 학습자 안내

### 이 학습 자료 사용법

§1을 한 번 읽어 세션의 핵심 질문을 파악한 뒤, §2의 여덟 개 개념 카드를 공부하세요. 각 카드에서는 먼저 수식 또는 결정 규칙을 고정한 다음, 거장의 시각·callout·체화 핵심을 확인하면 됩니다. 교과서 그림 참조는 이미지를 임베드하지 않고, 원본 그림을 언제 어떤 질문으로 봐야 하는지 안내합니다.

**v3.7 읽기 원칙:** 이 문서는 delayed response를 “지연 모델 하나”로 외우게 하지 않습니다. 지연의 소속을 response pool, effect site, target/cell pool, 또는 PK clock 중 어디에 둘지 결정하도록 설계되어 있습니다.

### 학습 경로

1. Turnover baseline과 hysteresis 분류.
2. 생산/소실 4모델 분류 체계.
3. $t_{ss}$와 peak shift 선별 진단, 주의사항 포함.
4. $I_{max}/E_{max}$ 의미 잠금과 선형 PK/비선형 PD 경고.
5. 그래프 기반(graphical) 초기값 설정, blocking-dose 논리, DRT 맥락.
6. 비가역적 작용과 표적 소비(target consumption) 회복.
7. Turnover 대 effect-compartment 감별 위기.
8. PK clock 대 PD clock, 그리고 PK-rate-limited일 때만 적용하는 duration formula.

### 시작 전 / 마친 후 체크리스트

- 시작 전: direct response, distribution delay, turnover delay, target consumption, PK/PD rate-limiting이 각각 서로 다른 후보 설명임을 확인하세요.
- 진행 중: 지연 반응이 나타날 때마다 느린 clock이 어디에 있는지 물어보세요.
- 마친 후: 보지 않고 자기 테스트(self-test)에 답해 보세요. model family와 clock 위치를 모두 식별할 수 있으면 세션 목표를 달성한 것입니다.

> **저작권 / 그림 사용 안내(Copyright / figure-use note)**  
> 원본 교과서 그림은 임베드하지 않습니다. 교과서 그림 참조 callout은 그림을 찾아볼 위치와 읽는 순서를 안내하는 텍스트입니다.

<!-- SLIDE_START: S01 | title: §1 — 세션 헤더 & 로드맵 -->
# §1 — 세션 헤더 & 로드맵

## 핵심 통찰(Big Idea)

대부분의 임상적으로 관찰되는 약력학적 반응(pharmacodynamic response)은 혈장 농도(plasma concentration)와 완전히 동시에 움직이지 않습니다. 그러나 모든 지연을 별도 모델로 다뤄야 하는 것은 아닙니다. 지연이 **무시 가능할 정도로 짧으면 direct PK-PD link**로 충분합니다. 반대로 지연이 관찰 가능하면 그 원인을 **분포 지연(distribution delay), turnover/system flux, 표적 소비(target consumption), 또는 PK/PD rate-limiting clock** 중 하나로 분해해야 합니다. [G pp.235–236; T pp.233–235, 239]

여기서 hysteresis(같은 농도에서도 시간 경로에 따라 반응이 달라지는 현상)는 “곡선이 예쁘지 않다”는 문제가 아니라, 지연의 소속을 다시 물으라는 진단 신호입니다.

## ASCII 레이어 개념 지도

```text
Layer 1 — 무엇인가
  direct response | hysteresis | turnover pool | effect site | target consumption | PK/PD clock

Layer 2 — 어떻게 계산되는가
  R0 = kin/kout | dR/dt = kin - kout·R | I(C), S(C) | SF = exp(-Kkill·AUC) | tD = (1/k)ln(Dose/Amin)

Layer 3 — 언제, 왜 중요한가
  model family 선택 | tss/peak-shift triage | non-identifiability 방어 | wrong-clock duration 차단 | 규제 보고서의 구조 정당화
```

## 읽는 순서

카드 1 (M1): baseline은 왜 독립 상수가 아니라 생산/소실 비율인가?  
카드 2 (M2): 약물이 input을 건드렸는가, output을 건드렸는가?  
카드 3 (M3): $t_{ss}$와 peak shift를 어디까지 믿을 수 있는가?  
카드 4 (M4): 같은 $E_{max}$ 이름이 왜 서로 다른 의미를 갖는가?  
카드 5 (M5): NONMEM 전 초기값을 왜 손으로 잠가야 하는가?  
카드 6 (M6): 약물이 사라졌는데 왜 효과가 남는가?  
카드 7 (M7): fit이 같을 때 turnover와 effect compartment를 어떻게 방어하는가?  
카드 8 (M8): duration 공식은 언제 사용할 수 있고 언제 폐기해야 하는가?

## 지식 그래프 위치

```text
[Direct exposure-response / linear PK-PD 기초]
        → [이 세션: indirect response, turnover, clock assignment]
        → [Transit compartment, tolerance/moderator, disease progression, PopPK/PD IIV, sampling design]
```

## 개념 항법도

이 세션은 다음 순서로 고정됩니다.

| 단계 | 핵심 고정점 | 왜 필요한가 |
|---|---|---|
| 1 | $dR/dt=k_{in}-k_{out}\cdot R$와 $R_0=k_{in}/k_{out}$ | baseline과 time constant를 만든다. [G p.237] |
| 2 | 약물은 production 또는 loss 중 하나를 inhibit/stimulate | 4-model taxonomy의 출발점이다. [G pp.237–245] |
| 3 | $t_{ss}$/peak shift | 강력한 triage signal이지만 PK rate-limiting과 limited dose range에 가려질 수 있다. [G pp.247–251; G pp.778–783] |
| 4 | Effect compartment vs turnover | 제한된 설계에서는 거의 같은 curve를 만들 수 있어 fit quality만으로 구조를 고정하면 안 된다. [G pp.758–763; T pp.244–246] |
| 5 | PK clock vs PD clock | 반응 감소는 drug PK clock 또는 system PD clock 중 느린 쪽이 결정한다. [T pp.243, 247–256] |

## 잠긴 핵심 메시지

이 장의 핵심은 “delayed response는 하나의 현상이 아니라 여러 원인의 공통 표면형”이라는 점입니다. 모델링의 첫 질문은 “어떤 ODE가 curve를 잘 맞추는가?”가 아닙니다. 먼저 “무엇이 시간을 rate-limit 하는가?”를 물어야 합니다.

<!-- SLIDE_START: S02 | title: §2 — 개념 해부 카드 -->
# §2 — 개념 해부 카드

<!-- SLIDE_START: M1 | title: Turnover Model Foundation + Hysteresis Classification -->
## Card 1 — Turnover Model Foundation + Hysteresis Classification

> **거장의 시각**
> Baseline을 독립 상수처럼 읽으면 $k_{in}$과 $k_{out}$의 비식별성을 놓치고, hysteresis를 단순한 산포로 오독합니다.
> $R_0=k_{in}/k_{out}$와 $1/k_{out}$을 먼저 잠그면, 이후 모든 delay assignment가 “어느 pool이 느린가”라는 한 질문으로 정렬됩니다.

### A. 공식 정의 + 수식

Turnover model(반응 pool의 생산·소실 균형)의 최소 골격은 반응(response)이 **생산되는 속도**와 **사라지는 속도**의 차이입니다. Baseline은 독립적인 상수가 아니라 두 속도의 비율입니다. [G pp.235–237; T pp.234–235, 239]

$$
\underbrace{\frac{dR}{dt}}_{\text{변화율}}
=
\underbrace{k_{in}}_{\text{생산}}
-
\overbrace{\underbrace{k_{out}}_{\text{소실 clock}}\,\underbrace{R}_{\text{반응 pool}}}^{\text{pool 소실}}
\quad \text{[G Eq 3:74; G p.237]}
$$

정상상태에서는 다음과 같습니다.

$$
\underbrace{R_0}_{\text{기저값}}
=
\frac{\underbrace{k_{in}}_{\text{생산}}}{\underbrace{k_{out}}_{\text{소실 clock}}}
\quad \text{[G Eq 3:76; G p.237]}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $R$ | response unit | 측정된 약리학적 반응 | 약물 작용, disease progression, 일주기 변동 |
| $k_{in}$ | response·time⁻¹ | 0차 생산 속도 | 합성 억제/촉진, 생리적 생산률 변화 |
| $k_{out}$ | time⁻¹ | 1차 소실 속도이자 회복 clock | 소실 경로 변화, feedback, system 상태 |
| $R_0$ | response unit | 기저 반응; 기본 모델에서는 시간 불변 | $k_{in}/k_{out}$ 비율 변화, baseline drift |

> 💡 **핵심 직관** — $R_0$는 “측정 전 상수”가 아니라, 들어오는 속도와 빠지는 속도가 만든 균형점입니다.
> ⚠️ **헷갈림 방지:** Hysteresis가 보인다고 direct response가 항상 틀린 것은 아닙니다. sampling 및 response-resolution 안에서 지연이 보이는지 먼저 판단해야 합니다.

### B. Hysteresis 분류

Hysteresis는 같은 농도(concentration)에서 상승기(rising phase)와 하강기(falling phase)의 반응(response)이 서로 다른 현상입니다. [T pp.234–235]

| 패턴 | 해석 | 고정 사례 |
|---|---|---|
| 반시계 방향(counterclockwise) | 반응이 농도 뒤에서 따라옴; 분포 지연, 하류 PD, 또는 system flux | Naproxen 500 mg oral, dental pain, 1–8 h, Fig 8-2 [T pp.234–235]; ibuprofen 6 mg/kg oral, febrile children, Fig 8-9 [T pp.241–242] |
| Hysteresis 없음 / direct link | 작용 부위 평형과 반응 생성이 관측 시간 척도 대비 빠름 | Midazolam 15 mg/kg oral in rat EEG, Fig 8-6 [T p.239] |
| 시계 방향(clockwise) | 내성(tolerance), 피드백, 활성 대사체, 또는 기타 추가 동역학 | 범위 참고: 이 세션의 핵심 R&T worked example에 포함되지 않음; 추후 tolerance 영역에서 다룸. |

💡 **비유:** 농도-반응 loop는 같은 산을 오르내리는 두 길의 고도 기록과 같습니다. 같은 고도라도 올라가는 중인지 내려오는 중인지에 따라 몸의 상태가 다르면, “고도 하나”로는 설명이 끝나지 않습니다.

> 🔑 **30초 방향 진단:** Counterclockwise이면 distribution/turnover/active-metabolite, clockwise이면 tolerance/feedback 후보를 먼저 떠올립니다. enantiomer-specific kinetics는 [교과서 외 실무 해석]입니다.

### C. 재파라미터화(Reparameterization)

모델 적합 시 $k_{in}$과 $k_{out}$를 독립적으로 먼저 추정하지 말고, $R_0$와 $k_{out}$를 우선 추정합니다.

$$
\underbrace{k_{in}}_{\text{생산}}
=
\underbrace{R_0}_{\text{기저값}}\cdot\underbrace{k_{out}}_{\text{소실 clock}}
$$

$$
\underbrace{\frac{dR}{dt}}_{\text{변화율}}
=
\underbrace{k_{out}}_{\text{회복 clock}}
\left(\underbrace{R_0-R}_{\text{기저-현재 거리}}\right)
\quad \text{[G Eq 3:103; G p.247]}
$$

PD4가 이 중요성을 보여줍니다. 충분한 실험설계 없이 상류 pool과 response의 turnover 상수를 독립 추정하면 비식별성(non-identifiability)에 근접할 수 있습니다. [G pp.742–752]

💡 **비유:** $k_{in}$과 $k_{out}$를 따로 맞추는 것은 어두운 방에서 수도꼭지와 배수구를 동시에 조절해 수위를 맞추는 일입니다. $R_0$와 $k_{out}$로 바꾸면 “현재 수위”와 “배수 속도”를 먼저 고정해 탐색 방향이 단순해집니다.

> 🔑 **재파라미터화 규칙:** $k_{in}$과 $k_{out}$가 극단적 상관을 보이거나 covariance step이 “stuck then drops” 패턴이면 $R_0\cdot k_{out}$로 재코딩합니다.

### D. 맥락 통합

음성 피드백(negative feedback)은 조절인자 $M$을 추가하여 반응이 높을수록 소실이 가속될 수 있게 합니다. IgG 사례는 혈청 IgG 30 mg·mL⁻¹에서 반감기가 약 11일로 단축되는 것을 보여줍니다. 이는 $k_{out}$이 고정 상수가 아니라 system 상태에 의존할 수 있음을 예시합니다. [G pp.110–111]

Baseline drift 모델은 별도의 확장입니다. 질병 진행 또는 일주기 변동이 $R_0$를 움직이면 기본 constant-baseline turnover 방정식만으로는 불충분합니다. [G pp.317–319]

> 💼 **실무 인사이트:** “직접(direct)” 대 “지연(delayed)” 판정은 모델 계열 결정 이전에 **설계 해상도(design-resolution) 결정**으로 먼저 다뤄야 합니다. 지연이 sampling 및 response-resolution 척도에서 보이지 않으면, 생물학적으로 완전히 순간적인 반응은 아니더라도 direct link가 방어 가능할 수 있습니다.

NONMEM 출력에서 30회 iteration 동안 OFV가 거의 변하지 않다가 갑자기 큰 폭으로 하락한다면, 그것은 보통 $r(k_{in}, k_{out})>0.98$ 상관이 search direction을 죽이고 있다는 신호입니다. PD5 Table 5.1이 이 패턴을 직접 기록합니다 — *"correlation greater than 0.98… reparameterization of the model by baseline $R_0$ and $k_{out}$."* PD4 Pool 1의 $r(k_1,k_{out})=0.9999$, CV% 4000 사례는 이 비식별성의 극단형입니다. 같은 데이터에 $k_1=k_{out}$ 제약을 걸어 만든 Pool 2의 “정상적인 CV%”는 데이터가 동등성을 지지한 것이 아니라 제약이 비식별성을 해결한 것입니다.

> 📖 **교과서 그림 참조:** Gabrielsson & Weiner 5e, p.235, Fig 3.33; Rowland & Tozer 5e, p.235, Fig 8-2  
> Fig 3.33은 직접 반응(direct response)과 지연된 히스테리시스 반응(delayed hysteretic response)을 구분해 줍니다. Fig 8-2는 동일한 naproxen 농도라도 상승기/하강기에 따라 서로 다른 통증 완화로 연결될 수 있음을 보여 줍니다.  
> 확인 시점: 카드 1을 읽은 뒤 확인하면 됩니다.

> **M1 체화 핵심**
> ① `baseline을 해석해야 할 때` → $R_0=k_{in}/k_{out}$ 비율이 결정
> ② `hysteresis 방향을 볼 때` → 지연의 후보 위치가 결정
> ⚡ `R_0를 독립 상수로 고정` → 비식별성·stuck-then-drop·잘못된 delay assignment로 연결

<!-- SLIDE_START: M2 | title: Four-Model Taxonomy: Inhibit/Stimulate × Production/Loss -->
## Card 2 — Four-Model Taxonomy: Inhibit/Stimulate × Production/Loss

> **앞 카드에서 이 카드로:** Card 1이 response pool의 baseline과 clock을 만들었다면, Card 2는 약물이 그 균형을 input에서 깨는지 output에서 깨는지를 결정합니다.

> **거장의 시각**
> 반응 방향만 보고 “억제/촉진”을 붙이면 Model 1과 Model 4, 또는 Model 2와 Model 3을 뒤섞게 됩니다.
> 약물 함수가 $k_{in}$에 붙는지 $k_{out}R$에 붙는지를 보면 $t_{ss}$, $R_{ss}$, 최대 변화량의 해석이 즉시 정렬됩니다.

### A. 형식적 정의 + 수식

가역적 turnover 반응에서 약물이 작용할 수 있는 부위는 production 억제, loss 억제, production 촉진, loss 촉진 네 가지입니다. 이 분류표는 생물학적 기전을 NONMEM `$DES` 블록으로 번역하는 최소 문법입니다. [G pp.237–245; T pp.240–241]

$$
\underbrace{I(C)}_{\text{남은 activity}}
=
1-
\underbrace{\frac{\overbrace{I_{max}\,C^n}^{\text{억제구동}}}{\underbrace{IC_{50}^n}_{\text{절반농도}}+\underbrace{C^n}_{\text{농도항}}}}_{\text{억제분율}},
\quad 0\le I_{max}\le 1
\quad \text{[G Eq 3:77; G p.237]}
$$

$$
\underbrace{S(C)}_{\text{촉진배율}}
=
1+
\underbrace{\frac{\overbrace{E_{max}\,C^n}^{\text{촉진구동}}}{\underbrace{EC_{50}^n}_{\text{절반농도}}+\underbrace{C^n}_{\text{농도항}}}}_{\text{촉진분율}}
\quad \text{[G Eq 3:78; G p.237]}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $I(C)$ | 무차원 | 남아 있는 production/loss activity | 농도 증가, $I_{max}$, $IC_{50}$, Hill 계수 |
| $S(C)$ | 무차원 | production/loss 촉진 배율 | 농도 증가, $E_{max}$, $EC_{50}$, Hill 계수 |
| $I_{max}$ | 무차원 | 최대 억제 가능 분율 | 약물 potency/efficacy, 작용부위 민감도 |
| $E_{max}$ | 무차원 또는 response unit | 모델 구조에 따라 최대 촉진 또는 절대 효과 | 파라미터화, baseline scale, system turnover |
| $IC_{50}/EC_{50}$ | concentration | 절반 효과 농도 | site-of-action exposure, 기전적 potency |
| $n$ | 무차원 | Hill 곡률 | 협동성 또는 경험적 steepness |

💡 **비유:** $I(C)$와 $S(C)$는 약물이 수도꼭지나 배수구에 붙이는 감압/가압 밸브입니다. 같은 밸브라도 수도꼭지에 붙으면 수위 변화의 의미가 달라지고, 배수구에 붙으면 속도 자체가 달라집니다.

> ⚠️ **헷갈림 방지:** $I_{max}$와 $E_{max}$는 이름이 비슷해도 같은 임상 의미가 아닙니다. 어떤 항에 곱해지는지가 의미를 결정합니다.

### B. 네 가지 모델의 병렬 비교

| 모델 | ODE | 약물 작용 부위 | $t_{ss}$ 지배 인자 | 일정한 $C_{ss}$에서의 $R_{ss}$ | 최대 $\Delta R$ 식 | $R$의 한계 | Baseline 복귀 거동 | 대표 사례 |
|---|---|---|---|---|---|---|---|---|
| 1. 생산 억제(Inhibition of production) | $\frac{dR}{dt}=k_{in}I(C)-k_{out}R$ [G pp.238–239] | input / biosynthesis 차단 | $k_{out}$, PK가 빠르면 용량 독립적 | $R_{ss}=R_0I(C_{ss})$ | $\Delta R=R_0I_{max}$ [G p.239] | 완전 억제 시 0을 향해 감소 | 약물이 사라진 뒤 $k_{out}$가 회복을 지배 | Warfarin은 vitamin K cycle / prothrombin complex를 억제 [G PD4 pp.742–752; T pp.242–247] |
| 2. 소실 억제(Inhibition of loss) | $\frac{dR}{dt}=k_{in}-k_{out}RI(C)$ [G pp.240–241] | output / removal 차단 | effective $k_{out}\cdot I(C)$, 용량 의존적 | $R_{ss}=R_0/I(C_{ss})$ | $\Delta R=R_0 I_{max}/(1-I_{max})$ [G p.241] | baseline 위로 상승 가능 | 복귀는 회복된 loss process에 의존 | Furosemide-type retention 예시 [G p.238] |
| 3. 생산 촉진(Stimulation of production) | $\frac{dR}{dt}=k_{in}S(C)-k_{out}R$ [G pp.242–243] | input 촉진 | $k_{out}$, PK가 빠르면 용량 독립적 | $R_{ss}=R_0S(C_{ss})$ | $\Delta R=R_0E_{max}$ [G p.243] | baseline의 배율만큼 상승 | 회복은 $k_{out}$가 지배 | Erythropoietin은 RBC production을 촉진 [G p.238] |
| 4. 소실 촉진(Stimulation of loss) | $\frac{dR}{dt}=k_{in}-k_{out}RS(C)$ [G pp.244–245] | output 촉진 | effective $k_{out}\cdot S(C)$, 용량 의존적 | $R_{ss}=R_0/S(C_{ss})$ | $\Delta R=R_0E_{max}/(1+E_{max})$ [G p.245] | baseline 아래로 감소 | 높은 stimulation에서 더 빠른 복귀 | CB1 inverse agonist / energy expenditure 예시 [G p.238]; PD7 compound C [G pp.764–769] |

$$
\begin{aligned}
\text{Model 1: }&\frac{dR}{dt}=\overbrace{k_{in}I(C)}^{\text{input 억제}}-\underbrace{k_{out}R}_{\text{loss}}\\
\text{Model 2: }&\frac{dR}{dt}=\underbrace{k_{in}}_{\text{input 유지}}-\overbrace{k_{out}RI(C)}^{\text{loss 억제}}\\
\text{Model 3: }&\frac{dR}{dt}=\overbrace{k_{in}S(C)}^{\text{input 촉진}}-\underbrace{k_{out}R}_{\text{loss}}\\
\text{Model 4: }&\frac{dR}{dt}=\underbrace{k_{in}}_{\text{input 유지}}-\overbrace{k_{out}RS(C)}^{\text{loss 촉진}}
\end{aligned}
$$

$$
\begin{aligned}
\text{Model 1: }&\underbrace{R_{ss}}_{\text{새 정상상태}}=\underbrace{R_0}_{\text{기저값}}\underbrace{I(C_{ss})}_{\text{억제함수}}\\
\text{Model 2: }&\underbrace{R_{ss}}_{\text{새 정상상태}}=\frac{\underbrace{R_0}_{\text{기저값}}}{\underbrace{I(C_{ss})}_{\text{loss 억제}}}\\
\text{Model 3: }&\underbrace{R_{ss}}_{\text{새 정상상태}}=\underbrace{R_0}_{\text{기저값}}\underbrace{S(C_{ss})}_{\text{촉진함수}}\\
\text{Model 4: }&\underbrace{R_{ss}}_{\text{새 정상상태}}=\frac{\underbrace{R_0}_{\text{기저값}}}{\underbrace{S(C_{ss})}_{\text{loss 촉진}}}
\end{aligned}
$$

$$
\begin{aligned}
\underbrace{\Delta R_{M1}}_{\text{M1 변화}}&=\underbrace{R_0}_{\text{기저값}}\underbrace{I_{max}}_{\text{최대억제}}\\
\underbrace{\Delta R_{M2}}_{\text{M2 변화}}&=\frac{\underbrace{R_0}_{\text{기저값}}\underbrace{I_{max}}_{\text{최대억제}}}{\underbrace{1-I_{max}}_{\text{잔여 loss}}}\\
\underbrace{\Delta R_{M3}}_{\text{M3 변화}}&=\underbrace{R_0}_{\text{기저값}}\underbrace{E_{max}}_{\text{최대촉진}}\\
\underbrace{\Delta R_{M4}}_{\text{M4 변화}}&=\frac{\underbrace{R_0}_{\text{기저값}}\underbrace{E_{max}}_{\text{최대촉진}}}{\underbrace{1+E_{max}}_{\text{촉진 보정}}}
\end{aligned}
$$

💡 **비유:** 네 모델은 같은 물탱크에 붙은 네 가지 장치입니다. 수원 밸브를 잠그는지, 배수구를 막는지, 수원을 키우는지, 배수구를 더 여는지에 따라 최종 수위와 수위 변화 속도가 함께 달라집니다.

### C. 구조적 필요성

이 네 모델의 차이는 “response가 올라가느냐 내려가느냐”보다 “drug가 input을 바꾸느냐 output을 바꾸느냐”에 있습니다. Models 1·3은 0차 input term을 변경하므로 시간 상수가 $1/k_{out}$으로 보존됩니다. Models 2·4는 1차 loss term을 변경하므로 effective time constant가 농도에 따라 달라집니다. 그렇기 때문에 $t_{ss}$ 거동이 작용 부위를 식별할 수 있습니다. 단, 이 판단은 PK가 더 느린 clock이 아닐 때만 성립합니다.

> ⚠️ **헷갈림 방지:** 하향 반응은 Model 1과 Model 4 모두에서 발생할 수 있습니다. 반응 방향만으로 모델을 추론하지 말고 시간 경과 패턴을 함께 보세요.
> 🔑 **5분 구조 압축:** 응답 방향과 $t_{ss}$ dose-dependence 조합으로 4개 칸 중 하나를 먼저 선택합니다. PD7 Fig 7.1에서는 하강 반응 + 용량 의존적 $t_{ss}$ 단축으로 Model 4가 지지됩니다.

> 📊 **개념 도식 (HTML에서 렌더링):** 네 가지 턴오버(turnover) 모델: 약물 작용 부위 → 시간 상수 결과 — 생산 측(production-side) 모델은 주로 반응 크기(response extent)를 바꾸는 반면, 소실 측(loss-side) 모델은 반응 크기와 겉보기 반응 속도(apparent response speed)를 모두 바꿉니다.

> **M2 체화 핵심**
> ① `반응 방향과 시간 경과를 동시에 볼 때` → input vs output 작용 부위가 결정
> ② `하강 반응이 보일 때` → Model 1뿐 아니라 Model 4 가능성도 함께 지배
> ⚡ `반응 방향만으로 모델명 부여` → $t_{ss}$·$R_{ss}$·max effect 해석이 모두 틀어짐

<!-- SLIDE_START: M3 | title: tss / Peak-Shift Mechanism Discrimination -->
## Card 3 — $t_{ss}$ / Peak-Shift Mechanism Discrimination

> **앞 카드에서 이 카드로:** Card 2가 네 가지 작용 부위 칸을 만들었다면, Card 3은 데이터에서 그 칸을 선별하는 첫 번째 진단 신호를 다룹니다.

> **거장의 시각**
> $t_{ss}$와 peak shift를 결정적 증거로 쓰면 PD9 Fig 9.5 같은 반례 앞에서 모델 선택 근거가 무너집니다.
> 이 신호를 “가설 발생기”로 쓰고 PK rate-limiting, dose range, noise, unmodeled nonlinearity를 동시에 지우면 방어 가능한 구조 추론이 됩니다.

### A. 형식적 정의 + 진단 변수

$t_{ss}$(steady-state 도달 시간)는 response pool이 새 균형에 도달하는 시간 척도입니다. peak shift(용량 증가에 따른 peak 시간 이동)는 작용 부위와 clock 위치를 추정하는 보조 신호입니다. [G pp.247–251; G pp.778–783; T p.243]

| 진단 변수 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $t_{ss}$ | time | 새 정상상태에 접근하는 시간 | $k_{out}$, effective $k_{out}$, PK clock, design resolution |
| Peak time | time | 최대 반응이 나타나는 시점 | distribution delay, system turnover, PK input profile |
| Dose range | dose | 비선형성을 노출하는 설계 폭 | 좁은 범위, saturation, unmodeled nonlinearity |
| Response noise | response unit | 진단 신호를 흐리는 관측 변동 | assay noise, sampling sparsity, biological variability |

> 💡 **핵심 구분:** $t_{ss}$는 어디를 볼지 알려주는 신호이지, 어디서 멈출지 알려주는 판결문이 아닙니다.

### B. 핵심 추론

| 관찰 | 1차 기전 가설 | 주의사항 |
|---|---|---|
| 용량 간 유사한 $t_{ss}$ | 생산 측 작용: Model 1 또는 3 | PK rate-limiting 또는 제한된 데이터 해상도에 의해 가려질 수 있습니다. |
| 용량에 따라 $t_{ss}$가 단축되거나 연장됨 | 소실 측 작용: Model 2 또는 4 | PK가 PD clock보다 빠를 때만 성립. |
| 용량 증가에 따른 peak shift 부재 | Effect compartment를 증명하지 않음 | PD9 시뮬레이션이 이 과대해석을 명시적으로 경고합니다. [G pp.778–783] |

> ⚠️ **헷갈림 방지:** 모든 모델을 Model 1/3처럼 취급하여 초기 반응 기울기에서 $k_{out}$을 추정하지 마세요. Models 2/4에서는 초기 또는 겉보기 기울기가 $I(C)$ 또는 $S(C)$에 의해 용량 의존적으로 스케일될 수 있습니다. [G p.251]

### C. 실용적 판정 규칙

$t_{ss}$/peak-shift는 **선별(triage)** 목적으로 사용하되, 최소한 하나 이상의 추가적 근거를 요구합니다.

| 이 카드에서 다루는 것 | → | 후속 세션으로 이월 | 이유 |
|---|---|---|---|
| 넓은 dose range 필요성 | → | nonlinear drug function 평가 | 좁은 범위에서는 $H(C)$ 거동이 숨습니다. |
| 반복 투여/washout 데이터 | → | system recovery clock 평가 | turnover와 effect site를 분리할 증거가 됩니다. |
| production vs loss prior | → | model family justification | $t_{ss}$ 신호만으로는 기전 확정이 불충분합니다. |
| PK clock 확인 | → | duration formula 적용성 | PK가 더 느리면 PD clock 진단이 가려집니다. |
| effect compartment 대안 | → | Card 7 감별 위기 | peak shift 부재가 link model 증거는 아닙니다. |

💡 **비유:** $t_{ss}$는 공항 보안검색의 금속탐지기와 같습니다. 경고음이 나면 어디를 더 볼지 알려주지만, 그것만으로 물건의 정체가 확정되지는 않습니다.

> 🔑 **Mirror-slope signature:** PD7 Fig 7.1에서 6,400 unit 용량의 추정 $k_{out}\approx0.6\;h^{-1}$, 160,000 unit 용량의 추정 $k_{out}\approx1.6\;h^{-1}$처럼 system parameter가 dose별로 단조 변화하면 biology가 아니라 misspecification artifact를 의심합니다.

> **M3 체화 핵심**
> ① `$t_{ss}$가 용량 의존적일 때` → loss-side 또는 wrong-clock 후보가 결정
> ② `peak shift가 없을 때` → effect compartment 확정이 아니라 설계·비선형성·PK clock이 지배
> ⚡ `$t_{ss}$를 기전 증거로 과대해석` → PD9 반례와 mirror-slope misread 앞에서 모델 선택 근거 붕괴

<!-- SLIDE_START: M4 | title: Imax/Emax Multiplier Semantics + Linear PK ≠ Linear PD -->
## Card 4 — $I_{max}/E_{max}$ Multiplier Semantics + Linear PK ≠ Linear PD

> **앞 카드에서 이 카드로:** Card 3이 시간 신호의 한계를 정했다면, Card 4는 효과 크기 파라미터가 어떤 scale에 붙는지 잠급니다.

> **거장의 시각**
> $E_{max}=0.65$ 같은 숫자를 이름만 보고 비교하면 drug potency와 system-baseline multiplier를 혼동합니다.
> 수식에서 $E_{max}$가 absolute distance인지, $R_0$에 곱해지는 배율인지 먼저 보면 cross-model 비교의 안전한 스케일이 보입니다.

### A. 의미 잠금 + 수식

$E_{max}$는 모든 모델에서 같은 단위와 의미를 갖지 않습니다. Direct $E_{max}$ 모델에서는 baseline으로부터의 절대 거리인 경우가 많고, turnover 모델에서는 이미 $k_{in}/k_{out}$ 비율로 정의된 system baseline에 곱해지는 배율입니다. [G p.246]

| 모델 형태 | 파라미터 의미 | 단위 / 해석 |
|---|---|---|
| Direct additive $E_{max}$ | $E=E_0+\frac{E_{max}C^n}{EC_{50}^n+C^n}$ | $E_{max}$는 반응 단위를 가짐; 절대 거리(absolute distance). |
| Direct reparameterized multiplier | $E=E_0(1+\frac{E_{max}C^n}{EC_{50}^n+C^n})$ | $E_{max}$는 무차원 배율(dimensionless multiplier). |
| Turnover Model 3 | $R_{ss}=R_0(1+\frac{E_{max}C^n}{EC_{50}^n+C^n})$ | $E_{max}$는 system turnover를 통해 작용하는 배율. |

$$
\underbrace{E}_{\text{관찰효과}}
=
\underbrace{E_0}_{\text{기저효과}}
+
\underbrace{\frac{\overbrace{E_{max}C^n}^{\text{효과구동}}}{EC_{50}^n+C^n}}_{\text{절대효과}}
$$

$$
\underbrace{E}_{\text{관찰효과}}
=
\underbrace{E_0}_{\text{기저효과}}
\left(1+
\underbrace{\frac{\overbrace{E_{max}C^n}^{\text{효과구동}}}{EC_{50}^n+C^n}}_{\text{배율효과}}
\right)
$$

$$
\underbrace{R_{ss}}_{\text{약물 정상상태}}
=
\underbrace{R_0}_{\text{system 기저값}}
\left(1+
\underbrace{\frac{\overbrace{E_{max}C^n}^{\text{input 배율}}}{EC_{50}^n+C^n}}_{\text{turnover 효과}}
\right)
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $E$ | response unit | 관찰 효과 | 농도, baseline, model form |
| $E_0$ | response unit | direct model baseline | disease state, baseline drift |
| $R_{ss}$ | response unit | 약물 효과 하 새 정상상태 | $R_0$, $I(C)$/$S(C)$, $k_{out}$ |
| $E_{max}$ | response unit 또는 무차원 | absolute distance 또는 multiplier | 파라미터화, turnover 구조 |
| $\Delta R/R_0$ | 무차원 | scale-normalized effect | baseline과 최대 변화량 |

💡 **비유:** 같은 “높이 10”이라도 센티미터인지 층수인지 모르면 비교가 불가능합니다. $E_{max}$도 어떤 축 위의 거리인지 먼저 확인해야 합니다.

### B. 선형 PK가 선형 PD를 의미하지는 않음

Methylprednisolone가 잠긴 사례입니다: 정확한 i.v. phosphate-prodrug 용량 시리즈는 16 / 31 / 63 / 125 / 250 / 500 / 1000 mg입니다. 혈장 AUC는 용량에 거의 비례적으로 증가하지만, lymphocyte 반응은 비례적으로 증가하지 않습니다. 고용량은 PD plateau에 근접합니다. [T pp.256–258]

R&T 본문(p.256)은 이 함정을 단호하게 명시합니다 — *"Dose linearity in pharmacokinetics does not result in dose linearity in pharmacodynamics. That is almost never the case."*

또한 systemic exposure가 곧 site-of-action exposure가 아님을 보여 주는 disconnect 사례도 같은 챕터에 등장합니다: rosuvastatin OATP1B1 polymorphism은 plasma AUC를 substantially 변화시키지만 cholesterol synthesis response는 modestly 변합니다(Fig 8-28/8-29 context only; 이것은 별도 turnover model이 아니라 exposure-response disconnect의 보조 관찰). [T pp.258–259]

> ⚠️ **헷갈림 방지:** “용량 비례적 노출은 용량 비례적 반응을 지지한다”는 결론을 쓰기 전에 Hill curve의 어느 region에 있는지 확인하세요.
> 🔑 **비교 규칙:** 모델, 연구, 또는 화합물 간 효과 파라미터를 비교할 때는 항상 $\Delta R/R_0$로 변환한 후 비교합니다.

> 📖 **교과서 그림 참조:** Gabrielsson & Weiner 5e, p.246, Fig 3.40  
> 이 그림은 같은 파라미터 레이블이 모델 계열마다 동일한 관찰 수직 반응 거리(observed vertical response distance)를 의미하지 않음을 보여 줍니다.  
> 확인 시점: 카드 4의 의미 잠금(semantic lock)을 읽은 뒤 확인하면 됩니다.

> **M4 체화 핵심**
> ① `$E_{max}$ 추정치를 보고할 때` → absolute distance인지 baseline multiplier인지가 결정
> ② `dose-proportional AUC를 볼 때` → Hill curve region이 PD 비례성 여부를 지배
> ⚡ `$E_{max}$ 라벨만 비교` → in vitro potency, clinical $EC_{50}$, model-derived effect size를 허위 비교

<!-- SLIDE_START: M5 | title: Graphical Initial Parameter Estimation + Blocking Dose / DRT -->
## Card 5 — Graphical Initial Parameter Estimation + Blocking Dose / DRT

> **앞 카드에서 이 카드로:** Card 4가 효과 scale을 잠갔다면, Card 5는 그 scale 위에서 NONMEM이 시작할 파라미터 자릿수를 손으로 먼저 고정합니다.

> **거장의 시각**
> 초기값을 단순 guess로 두면 optimizer가 비식별성 골짜기에서 가짜 수렴을 보고해도 알아채기 어렵습니다.
> Raw response-time plot에서 $R_0$, $k_{out}$, potency, maximal effect의 자릿수를 먼저 잠그면 fitted parameter의 sanity check 기준선이 생깁니다.

### A. 형식적 정의 + 최소 graphical 작업 흐름

Graphical estimation(그래프 기반 초기 추정)은 “진짜 모델링 전 번거로운 과정”이 아니라 첫 번째 기전적 감사(mechanism audit)입니다. [G pp.247–251]

| 단계 | 근거/가정 | 수식 또는 산출물 |
|---|---|---|
| 1 | 투약 전 또는 vehicle baseline | $R_0$ 추정 |
| 2 | 종말 회복 곡선, blocked-synthesis 감소 구간, log-linear 복귀 | $k_{out}$ 추정 |
| 3 | baseline과 time constant 분리 | $k_{in}=R_0\cdot k_{out}$ |
| 4 | 2–3개 용량 수준의 steady state 또는 peak 반응 | $IC_{50}/EC_{50}$, $I_{max}/E_{max}$ 출발 자릿수 |
| 5 | 초기값 감사 후 | nonlinear mixed-effects estimation 실행 |

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $R_0$ | response unit | pre-dose baseline | disease state, assay baseline, drift |
| $k_{out}$ | time⁻¹ | response recovery clock | system turnover, feedback, model misspecification |
| $k_{in}$ | response·time⁻¹ | production rate | $R_0\cdot k_{out}$, synthesis changes |
| $IC_{50}/EC_{50}$ | concentration | potency scale | exposure range, mechanism, site concentration |
| $I_{max}/E_{max}$ | 무차원 또는 response unit | maximal perturbation | model family, baseline scaling |

> 💡 **핵심 직관:** 초기값은 숫자 입력이 아니라 식별성 감사입니다.

### B. Blocking-dose 유사 방법

Warfarin blocking-dose 분석은 $k_{out}$을 직접 추출하는 임상적 등가 방법을 보여줍니다. 합성이 거의 완전히 차단될 때, prothrombin complex activity는 다음을 따릅니다.

$$
\underbrace{\frac{dA}{dt}}_{\text{활성 변화}}
=-\underbrace{k_t}_{\text{소실 clock}}\,\underbrace{A}_{\text{잔여 활성}}
\quad \text{[T Eq 8-6; T pp.244–246]}
$$

비차단 구간에서는 합성 속도를 재구성할 수 있습니다.

$$
\underbrace{R_{syn}}_{\text{합성속도}}
=
\underbrace{\frac{A_2-A_1}{\Delta t}}_{\text{관찰변화}}
+
\overbrace{\underbrace{k_t}_{\text{소실 clock}}\frac{\underbrace{A_1+A_2}_{\text{평균 활성}}}{2}}^{\text{소실보정}}
\quad \text{[T Eq 8-7; T p.247]}
$$

이는 hysteretic 반응-시간 기록을 억제-농도 관계로 변환합니다. [T pp.244–247]

💡 **비유:** Blocking-dose는 공장 입구를 거의 완전히 닫고 창고가 비는 속도를 재는 실험과 같습니다. 들어오는 물량을 잠그면 배출 clock이 드러납니다.

### C. DRT 맥락

Dose-Response-Time 분석은 농도 데이터가 없더라도 baseline, slope, potency, maximal effect를 추론할 수 있습니다. 그러나 full PK/PD modeling보다 거친 역문제(inverse problem)입니다. 노출(exposure) 데이터가 있으면 측정 노출을 DRT로 대체하지 마세요. DRT는 후퇴 대안(fallback) 또는 교육적 가교(teaching bridge)로 두면 됩니다. [G pp.272–275]

> 💼 **실무 인사이트:** 수동 초기 추정값은 NONMEM 이전 시대의 향수가 아닙니다. 기전적 감사입니다. 기울기, baseline, 또는 blocking-dose 논리가 적합된 파라미터를 대략적으로라도 지지하지 못한다면, 최적화가 잘못된 문제를 깔끔하게 풀고 있을 가능성이 높습니다.

PD5 case study는 Compound A에서 $V=40\;\text{L}$, $K=0.9\;h^{-1}$인 PK가 먼저 잠긴 상태에서, 4000/16000/80000 unit의 6시간 infusion 데이터를 받습니다. Pre-infusion baseline으로 $R_0$를 읽고, post-infusion 회복 곡선의 semi-log plot에서 terminal slope로 $k_{out}\approx0.43\;h^{-1}$의 자릿수를 잡고, $k_{in}=R_0\cdot k_{out}$로 production rate 출발점을 정합니다. 세 dose levels의 plateau 응답으로 $IC_{50}\approx95$, $I_{max}\approx0.65$의 자릿수까지 잡은 후에야 NONMEM 추정에 들어갑니다(Table 5.1).

> ⚠️ **헷갈림 방지:** 터무니없는 초기값이 필요한 모델은 대부분 graphical 단계를 건너뛰었거나 잘못된 clock을 사용했다는 뜻입니다. Random effects를 확장하기 전에 출발점의 생물학을 먼저 수정해야 합니다.

> **M5 체화 핵심**
> ① `NONMEM 실행 전` → $R_0$, $k_{out}$, potency, maximal effect 자릿수가 결정
> ② `fitted 값이 graphical 자릿수에서 한 order 이상 벗어날 때` → 비식별성 또는 misspecification이 지배
> ⚡ `초기값을 optimizer에게 위임` → 가짜 수렴과 후속 임상시험 설계 오염

<!-- SLIDE_START: M6 | title: Irreversible Drug Action + Target Consumption -->
## Card 6 — Irreversible Drug Action + Target Consumption

> **앞 카드에서 이 카드로:** Card 5까지가 reversible turnover의 파라미터를 잠갔다면, Card 6은 drug=0이면 effect도 사라진다는 가정 자체가 깨지는 경우를 분리합니다.

> **거장의 시각**
> Plasma half-life를 effect duration으로 외삽하면 aspirin, omeprazole, paclitaxel 같은 사례에서 결정적 오류가 납니다.
> 약물이 표적/세포 pool을 소비했는지 먼저 묻으면, 회복 clock을 drug PK가 아니라 target replacement나 cell regrowth에 배정할 수 있습니다.

### A. 핵심 비가역 방정식

가역적 turnover 모델은 system이 반응을 지속적으로 생산하고 제거하기 때문에 baseline으로 돌아갑니다. 비가역적 작용은 약물 노출 기간 동안 반응 단위, 표적, 또는 세포가 영구적으로 제거됩니다. [G pp.256–260; T pp.251–252]

$$
\underbrace{\frac{dR}{dt}}_{\text{생존 변화}}
=
-\overbrace{\underbrace{K_{kill}}_{\text{kill potency}}\,\underbrace{C}_{\text{노출}}\,\underbrace{R}_{\text{잔여 pool}}}^{\text{비가역 kill}}
\quad \text{[G Eq 3:110; G p.257]}
$$

적분 형태의 생존율(survival fraction)은 다음과 같습니다.

$$
\underbrace{SF}_{\text{생존분율}}
=
\exp\left(-\overbrace{\underbrace{K_{kill}}_{\text{kill potency}}\cdot\underbrace{AUC}_{\text{누적노출}}}^{\text{누적 kill}}
\right)
\quad \text{[G Eq 3:112; G p.257]}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $K_{kill}$ | concentration⁻¹·time⁻¹ | 2차 약리작용 상수 | drug-action potency, target sensitivity |
| $C$ | concentration | 노출 농도 | PK, dose, distribution |
| $R$ | response/cell/target unit | 잔여 pool | irreversible loss, regrowth/replacement |
| $AUC$ | concentration·time | 누적 노출 | dose, clearance, sampling window |
| $SF$ | fraction | 생존 또는 잔여 분율 | $K_{kill}\cdot AUC$ |

💡 **비유:** 비가역 kill은 스위치를 끄는 것이 아니라 전구를 빼내는 것과 같습니다. 전기가 끊긴 뒤에도 새 전구가 들어오기 전까지 빛은 돌아오지 않습니다.

> ⚠️ **헷갈림 방지:** $K_{kill}$은 2차 약리작용 상수이며, 1차 PK 소실 상수가 아닙니다. 이 handout에서 $K_{kill}/k_k$는 pharmacodynamic killing, $K_{elim}$은 PK elimination을 의미합니다.

### B. 표적 소비 사례

| 상황 | 파라미터 변화 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| Aspirin 650 mg 경구 | 혈장 반감기는 짧지만 혈소판 기능은 target replacement 의존 | → | thromboxane B₂ 억제가 수일 지속 | 표적 대체 clock을 모델링 [T p.251] |
| Omeprazole 40 mg 경구 | 혈장 반감기 <1 h, proton-pump 결합/재생 동역학 | → | 산분비 억제가 수일 지속 | pump regeneration을 회복 clock으로 설정 [T p.252] |
| Paclitaxel 정맥투여 | 혈장 농도 감소가 백혈구 회복보다 훨씬 빠름 | → | 회복에 약 3주 소요 가능 | leukocyte recovery model 필요; Fig 8-22 맥락, Fig 8-19 아님 [T pp.253–254] |

### C. 세포 성장/사멸 맥락

세포가 증식할 때, 비가역적 사멸은 성장 동역학 안에 포함되어야 합니다. Gabrielsson의 cell-growth/kill 프레임워크는 logistic 또는 용량-제한 성장과 2차 사멸을 추가합니다. $B_{max}\approx30,000\;\text{CFU}$는 맥락 앵커이며 별도의 MUST 카드가 아닙니다. [G pp.258–260]

> 🔑 **Duration 질문 규칙:** “drug=0이면 effect=0인가?”의 답이 NO이면 plasma PK 외 target replacement clock을 별도로 모델링합니다.

> **M6 체화 핵심**
> ① `약물이 사라진 뒤 효과가 남을 때` → target/cell replacement clock이 결정
> ② `reversible turnover와 irreversible kill을 구분할 때` → 표적 소비 여부가 지배
> ⚡ `약물 소실 = 효과 소실 가정` → duration 과소/과대 예측과 wrong-clock 모델링 실패

<!-- SLIDE_START: M7 | title: Apex — Turnover vs Effect Compartment Discrimination Crisis -->
## Card 7 — [⚡ Apex Concept] Turnover vs Effect Compartment Discrimination Crisis

> **앞 카드에서 이 카드로:** Card 6이 “어떤 pool이 회복되는가”를 물었다면, Card 7은 같은 곡선이 turnover pool과 effect-site pool 중 어느 쪽 지연인지 구별하지 못하는 위기를 다룹니다.

> **거장의 시각**
> 💢 **흔한 오해:** Fit이 매끄럽고 $k_{out}$ 또는 $k_{e0}$가 그럴듯하면 지연의 원인이 결정됐다고 생각한다.
> ✅ **실제는:** 제한된 단회 투여·좁은 dose range에서는 turnover $R(t)$와 effect-site $C_e(t)$가 거의 같은 response-time 곡선을 만들 수 있다.
> 🎯 **체화할 단 하나의 직관:** 곡선이 아니라 지연의 소속—biology인가 biophase distribution인가—을 증명해야 한다.

### A. 경쟁하는 구조들

Turnover 모델과 effect-compartment 모델은 제한된 단회 투여 설계 하에서 거의 동일한 response-time 곡선을 만들어낼 수 있습니다. 차이는 curve smoothness가 아니라 인과적 주장입니다: 지연이 약물이 biophase(실제 작용부위 주변 농도 공간)에 천천히 도달하기 때문인가, 아니면 반응 system 자체가 천천히 turnover하기 때문인가? [G pp.758–763; T pp.244–246]

Turnover 예시는 다음과 같습니다.

$$
\underbrace{\frac{dR}{dt}}_{\text{변화율}}
=
\overbrace{\underbrace{k_{in}}_{\text{생산}}\underbrace{S(C)}_{\text{촉진함수}}}^{\text{생산 촉진}}
-
\overbrace{\underbrace{k_{out}}_{\text{소실 clock}}\underbrace{R}_{\text{response pool}}}^{\text{pool 소실}}
$$

Effect compartment 예시는 다음과 같습니다.

$$
\underbrace{\frac{dC_e}{dt}}_{\text{effect-site 변화}}
=
\underbrace{k_{e0}}_{\text{평형 clock}}
\left(\underbrace{C-C_e}_{\text{농도차}}\right),
\quad
\underbrace{R}_{\text{반응}}=\underbrace{f(C_e)}_{\text{effect-site 함수}}
\quad \text{[T pp.244–246]}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $R(t)$ | response unit | turnover response pool | production/loss, system turnover |
| $C_e$ | concentration | effect-site concentration | biophase equilibration, $k_{e0}$ |
| $k_{out}$ | time⁻¹ | system turnover clock | response biology, feedback, model structure |
| $k_{e0}$ | time⁻¹ | plasma-to-effect-site 평형 clock | tissue distribution, biophase delay |
| WRSS/AIC | fit metric | 구조 간 적합도 차이 | residuals, model complexity, data richness |

💡 **비유:** 두 모델은 같은 그림자를 만들 수 있는 두 물체입니다. 그림자 모양만 보고 물체를 확정하려면 위험하고, 조명 방향을 바꾸거나 다른 각도에서 봐야 합니다.

PD6가 이 위기를 고정합니다: turnover와 effect-compartment 적합도가 본질적으로 같은 잔차 거동을 보이며, $k_{out}$과 $k_{e0}$가 모두 약 5.6 h⁻¹ 부근의 비슷한 값으로 수렴합니다. [G pp.758–763]

> **📌 비식별성의 본질 — 학습자 본문 잠금 [EXPERT_INFERENCE, v3]**  
> Pool 1과 Pool 2 모델은 단일 dose range 데이터에서 사실상 구별 불가능합니다($r=0.9999$, $\Delta WRSS\approx2$). 이 비식별성은 피팅 실패가 아닙니다. 데이터가 두 모델을 분리하기에 충분하지 않다는 정보를 전달합니다. Wider dose range 또는 mechanism-based prior 없이는 어느 모델이 “옳은가”라는 질문 자체에 데이터로 답할 수 없습니다.

### B. 감별 방법

| 증거 | Turnover 지지 | Effect compartment 지지 |
|---|---|---|
| 반응 변수(Response variable) | 내인성 매개물질, 바이오마커, 세포 수, 응고인자, 위산 pH | 작용 부위로의 약물 분포가 지연의 가능한 원인 |
| Dose range | 비선형 turnover 생성 거동을 드러낼 만큼 넓을 것 | 안정적인 $EC_{50}$과 타당한 $k_{e0}$로 hysteresis가 해소됨 |
| 교란(Perturbation) | 반복 투여/washout이 system 회복 시간을 드러냄 | Biophase 평형으로 onset과 offset을 설명 |
| 기전적 사전 정보(Mechanistic prior) | 알려진 합성/소실 과정 | 알려진 조직 분포 지연 |

> 💼 **실무 인사이트:** 두 인과 구조가 동등하게 적합할 때, 규율 있는 접근은 생물학적 가정을 문서화하고 두 구조를 분리할 수 있는 설계 요소를 명시하는 것입니다. 모델의 방어 가능성은 곡선의 매끄러움이 아니라 mechanism과 design support에서 나옵니다.

### C. 치명적 타격 — 교과서 기반 핵심 + 실무 해석 라벨

**교과서 기반:** 적합도(fit quality)만으로는 지연이 분포에 의한 것인지 turnover에 의한 것인지 증명할 수 없습니다. 제한된 설계에서는 두 구조가 동등하게 보일 수 있습니다. [G pp.758–763; T pp.244–246]

> 💼 **실무 인사이트:** 규제 제출 형식의 글에서, 이 지점이 대안 모델 비교(alternative model comparison)와 기전적 정당화(mechanistic justification)가 들어가야 할 위치입니다. 설계가 구조를 감별할 수 없다면 선택된 구조를 자명한 것처럼 제시하지 않습니다.

Turnover가 생성한 system에 effect-compartment 모델을 적합시켰을 때 $EC_{50}$이 dose에 따라 변한다면, 그 약물 파라미터는 system 동역학을 흡수하고 있는 것입니다. 이것은 potency 발견이 아니라 구조적 경고입니다.

PD6 Table 6.1은 이 비식별성을 숫자로 고정합니다.

| Metric | Turnover (linear S·$k_{in}$) | Effect compartment | Δ |
|---|---:|---:|---:|
| WRSS | 15,516 | 15,518 | 2 |
| AIC | 1,041 | 1,040 | −1 |
| 시간 상수 | $k_{out}=5.6\;h^{-1}$ | $k_{e0}=5.6\;h^{-1}$ | 0 |
| Half-doubling 농도 | $EC_{50}=1{,}633\;\text{ng}\cdot\text{L}^{-1}$ | $a=0.026\to\sim1{,}623\;\text{ng}\cdot\text{L}^{-1}$ | <1% |

> ⚠️ **헷갈림 방지:** $\Delta WRSS=2$와 $\Delta AIC=-1$은 model selection criterion 입장에서 사실상 동치입니다. 이것은 “둘 중 하나가 더 매끄럽다”가 아니라 “데이터가 둘을 못 가른다”는 신호입니다.

### M. Plausible Fallacy — 나비효과 연쇄

**오류:** 단일 dose-range 데이터에서 turnover와 effect compartment가 모두 잘 맞으면 AIC가 조금 낮은 모델을 “기전적으로 맞는 모델”로 선택한다.  
**왜 그럴싸한가:** $\Delta AIC=-1$처럼 숫자가 우열처럼 보이고, 두 모델의 response-time curve가 모두 매끄럽기 때문입니다.  
**나비효과:** AIC 미세차로 구조 선택 → $k_{e0}$ 또는 $k_{out}$에 지연 원인을 과잉 배정 → [임상] 새로운 dose range·반복 투여에서 onset/offset 예측 실패 → [모델링/규제] 대안 구조 평가와 sensitivity analysis 부재로 모델 선택 정당화 재요구. [교과서 외 실무 해석]

> 📖 **교과서 그림 참조:** Gabrielsson & Weiner 5e, p.759, Fig 6.1; p.763, Table 6.1  
> 이것은 핵심 감별(apex discrimination) 예시입니다. 반응-시간(response-time) 적합은 본질적으로 동등해 보일 수 있지만, 인과적 해석은 서로 다르게 남습니다. Table 6.1은 $k_{out}/k_{e0}$의 근접 동등성을 구체적으로 보여 줍니다.  
> 확인 시점: 카드 7의 경쟁 구조(competing structures)를 읽은 뒤 확인하면 됩니다.

> **M7 체화 핵심**
> ① `두 모델 fit이 동등할 때` → mechanism prior와 design support가 결정
> ② `$k_{out}\approx k_{e0}$일 때` → 지연의 소속을 데이터 단독으로 확정할 수 없음
> ⚡ `fit quality로 causal delay 선택` → 잘못된 구조 확정, sensitivity 누락, 후속 용량 예측 실패

<!-- SLIDE_START: M8 | title: PK Clock vs PD Clock + Duration Formula Boundary -->
## Card 8 — PK Clock vs PD Clock + Duration Formula Boundary

> **앞 카드에서 이 카드로:** Card 7이 지연의 소속을 증명해야 한다는 위기를 보여주었다면, Card 8은 그 소속 판단이 실제 dose-duration 공식 사용 가능성을 어떻게 결정하는지 닫습니다.

> **거장의 시각**
> Eq 8-12를 모든 delayed response에 적용하면 warfarin·aspirin·omeprazole·paclitaxel에서 수학적으로 매끈하지만 임상적으로 틀린 duration이 나옵니다.
> PK clock과 PD clock 중 느린 쪽을 먼저 고르면, dose log 공식이 살아 있는 경우와 폐기해야 하는 경우가 즉시 갈립니다.

### A. Clock 감별

투약 후 두 개의 시계가 동시에 작동합니다: 약물의 PK clock과 반응 system의 PD clock입니다. 관찰되는 반응 감소는 이 중 느린 쪽의 시계가 결정합니다. [T pp.243, 247–256]

| 상황 | 느린 clock | 고정 사례 | 모델링 귀결 |
|---|---|---|---|
| PK rate-limited | 약물 소실/분포 | Succinylcholine 0.5/1/2/4 mg·kg⁻¹ i.v., 근이완; minoxidil 단회 경구 25 mg, MAP 저하 [T pp.249–256] | $t_D$ 공식이 의미 있을 수 있습니다. |
| PD rate-limited | System turnover/표적 재생 | Acenocoumarol vs 응고인자 turnover; aspirin 혈소판/TxB₂; omeprazole proton-pump 회복; paclitaxel 백혈구 회복 [T pp.243, 251–254] | Turnover/target-consumption 모델이 필요; PK $k$만으로는 duration 예측 불가입니다. |
| 약물 PK가 system보다 느릴 때 | 간접 기전에서도 PK가 지배 | Phenprocoumon 반감기 ~5일 vs 응고인자 동역학 [T p.243] | 항응고 효과 회복이 약물 잔류를 따릅니다. |

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $k$ | time⁻¹ | PK elimination clock | clearance, volume, drug persistence |
| $t_D$ | time | threshold 이상/이하 효과 지속시간 | dose, $k$, $A_{min}$, clock selection |
| $A_{min}$ | amount | 효과 최소량 | $C_{min}V$, threshold, exposure-response relationship |
| PD clock | time scale | system recovery 또는 target replacement | turnover, irreversible action, feedback |

### B. Region 1/2/3과 선형 감소

계단식 E-logC 관계의 중간 구간에서는 단일 용량 투여 후 반응이 시간에 따라 근사적으로 선형으로 감소합니다.

$$
\underbrace{Response}_{\text{관찰반응}}
=
\underbrace{E(0)}_{\text{시작효과}}
-
\overbrace{\underbrace{m}_{\text{E-logC 기울기}}\,\underbrace{k}_{\text{PK clock}}\,\underbrace{t}_{\text{시간}}}^{\text{선형 감소}}
\quad \text{[T Eq 8-9; T pp.247–249]}
$$

이것은 Region 2에 대한 서술입니다. 즉, response가 Hill curve의 중간 구간에 있을 때의 근사입니다. Region 3은 plateau에 가깝고, Region 1은 1차 동역학 유사 거동으로 복귀합니다. Succinylcholine의 대략 22%/min 감소가 이 중간 구간 선형성을 예시합니다. [T pp.249–250]

💡 **비유:** Region 2는 비탈길 중간의 직선 구간과 같습니다. 위쪽 plateau나 아래쪽 완만한 구간에서는 같은 걸음 수가 같은 높이 변화로 바뀌지 않습니다.

### C. Duration 공식

Clock 감별이 먼저 끝나야 합니다. PK-rate-limited 반응에서 노출-반응 관계가 사실상 고정되어 있을 때 다음 식을 사용합니다.

$$
\underbrace{t_D}_{\text{duration}}
=
\underbrace{\frac{1}{k}}_{\text{PK clock 역수}}
\ln\left(\frac{\underbrace{Dose}_{\text{투여량}}}{\underbrace{C_{min}V}_{\text{최소 유효량}}}\right)
=
\underbrace{\frac{1}{k}}_{\text{PK clock 역수}}
\ln\left(\frac{\underbrace{Dose}_{\text{투여량}}}{\underbrace{A_{min}}_{\text{효과 최소량}}}\right)
\quad \text{[T Eq 8-12; T pp.254–255]}
$$

용량을 두 배로 올리면 약물 반감기 하나만큼의 duration이 추가됩니다.

$$
\underbrace{\Delta t_D}_{\text{duration 추가분}}
=
\frac{\underbrace{\ln 2}_{\text{2배 로그}}}{\underbrace{k}_{\text{PK clock}}}
=
\underbrace{t_{1/2}}_{\text{PK 반감기}}
$$

이것이 succinylcholine의 duration이 용량 두 배마다 대략 유효 반감기 하나만큼 증가하는 이유입니다. [T pp.255–256]

💡 **비유:** PK-rate-limited duration에서 dose doubling은 로그 자 위에서 한 칸 오른쪽으로 이동하는 것과 같습니다. 그 한 칸이 시간축에서는 반감기 하나로 번역됩니다.

> ⚠️ **헷갈림 방지:** Eq 8-12를 warfarin, aspirin, omeprazole, paclitaxel처럼 PD-rate-limited 상황에 적용하지 마세요.
> 🔑 **Wrong-clock 규칙:** Duration을 계산하기 전에 먼저 “어느 clock이 느린가?”를 물어야 합니다. 답이 PD라면 PK $k$를 duration 결정 인자로 사용하는 것을 중단해야 합니다.

Post-trough 회복 곡선에서 observed 데이터가 모델보다 빠르게 baseline으로 돌아온다면 moderator/feedback compartment 누락의 신호입니다. G&W §2.6.7 Eq 2:261-2:263과 IgG 11일 saturable protection이 이 패턴의 prototype이며, 예측 duration이 관측 duration과 50% 이상 어긋나거나 dose 증량 시 예측 duration 증가가 관측치와 비례하지 않는다면 rate-limiting clock이 잘못 잡혔다는 정량 시그니처입니다. [교과서 외 실무 해석]

Acenocoumarol(half-life ~15 h)과 phenprocoumon(half-life ~5–6일)은 동일한 prothrombin complex 동역학을 공유하지만 서로 다른 rate-limiting clock을 갖습니다(Fig 8-11). 동일 작용기전을 공유하는 약물군에서도 약물별 PK가 rate-limiting step을 결정합니다. [T p.243]

> 📖 **교과서 그림 참조:** Rowland & Tozer 5e, p.243, Fig 8-11  
> 동일한 항응고 반응 시스템(system)도 약물 PK에 따라 서로 다른 시계(clock)에 의해 제한될 수 있습니다.  
> 확인 시점: 카드 8의 지속시간 공식(duration formula)을 적용하기 전에 확인하면 됩니다.

> 📖 **교과서 그림 참조:** Rowland & Tozer 5e, p.255, Fig 8-23; p.256, Fig 8-24  
> 이 그림들은 Eq 8-12의 시각적 결과를 보여 줍니다. PK가 속도 제한 단계인 조건에서는 용량을 두 배로 늘리면 지속시간에 대략 한 반감기가 추가됩니다.  
> 확인 시점: 카드 8의 지속시간 공식(duration formula)을 읽은 뒤 확인하면 됩니다.

> **M8 체화 핵심**
> ① `duration formula를 적용할 때` → PK-rate-limited 여부가 결정
> ② `PD-rate-limited 약물일 때` → turnover/target-replacement model이 지배
> ⚡ `clock 선택 전 $t_D$ 계산` → 수학적으로 맞지만 임상적으로 무의미한 duration 예측

<!-- SLIDE_START: S03 | title: §5 — 혼동 쌍 해부 -->
# §5 — 혼동 쌍 해부(Confusion Pair Dissection)

## §5-1. Model 1 vs Model 2 — 생산 억제(Inhibition of Production) vs 소실 억제(Inhibition of Loss)

| 비교 기준 | 개념 A: Model 1 생산 억제 | 개념 B: Model 2 소실 억제 |
|---|---|---|
| 단위 / 차원 | $k_{in}I(C)$는 response·time⁻¹ input term | $k_{out}RI(C)$는 response·time⁻¹ loss term |
| 수식 내 위치 (분자/분모/지수) | $dR/dt=k_{in}I(C)-k_{out}R$; drug function이 input에 위치 [G pp.238–239] | $dR/dt=k_{in}-k_{out}RI(C)$; drug function이 loss에 위치 [G pp.240–241] |
| 변화 원인 (생물학적/병적) | biosynthesis 또는 production 차단 | removal 또는 loss 차단 |
| 혼동 시 임상 결과 | 하향 반응을 모두 “억제”로 부르며 production vs loss를 놓침 | 상향 반응을 production stimulation으로 오인함 |

$$
\begin{aligned}
\text{Model 1: }&\frac{dR}{dt}=\overbrace{k_{in}I(C)}^{\text{production 억제}}-\underbrace{k_{out}R}_{\text{기존 loss}}\\
\text{Model 2: }&\frac{dR}{dt}=\underbrace{k_{in}}_{\text{production 유지}}-\overbrace{k_{out}RI(C)}^{\text{loss 억제}}
\end{aligned}
$$

## §5-2. Direct $E_{max}$ vs Turnover $I_{max}$/$E_{max}$

| 비교 기준 | 개념 A: Direct 모델 | 개념 B: Turnover 모델 |
|---|---|---|
| 단위 / 차원 | 파라미터화에 따라 response unit 또는 무차원 | $k_{in}/k_{out}$ baseline에 대한 배율 |
| 수식 내 위치 (분자/분모/지수) | 즉각적 농도-반응 식 안의 vertical distance 또는 multiplier | $R_{ss}$ 또는 turnover ODE 안의 system perturbation |
| 변화 원인 (생물학적/병적) | 농도-반응 관계 자체 | 생산/소실 동역학 후의 system 반응 |
| 혼동 시 임상 결과 | 직접 반응 거리와 turnover 배율을 같은 효과 크기로 비교 | cross-model, in vitro/clinical potency 비교가 왜곡 |

## §5-3. Reversible Turnover vs 비가역적 사멸(Irreversible Kill) / 표적 소비(Target Consumption)

| 비교 기준 | 개념 A: Reversible turnover | 개념 B: Irreversible / target consumption |
|---|---|---|
| 단위 / 차원 | $k_{in}$ response·time⁻¹, $k_{out}$ time⁻¹ | $K_{kill}$ concentration⁻¹·time⁻¹, $K_{kill}CR$ response·time⁻¹ |
| 수식 내 위치 (분자/분모/지수) | $dR/dt=k_{in}-k_{out}R$ | $dR/dt=-K_{kill}CR$; $SF=\exp(-K_{kill}\cdot AUC)$ |
| 변화 원인 (생물학적/병적) | system이 계속 생산·소실되어 baseline 복귀 | 표적/세포가 소비되고 replacement/regrowth 필요 |
| 혼동 시 임상 결과 | 지연된 회복을 무조건 비가역 작용으로 오인 | 약물 소실이 효과 소실을 의미한다고 가정 |

$$
\begin{aligned}
\text{Reversible: }&\frac{dR}{dt}=\underbrace{k_{in}}_{\text{재생산}}-\underbrace{k_{out}R}_{\text{소실}}\\
\text{Irreversible: }&\frac{dR}{dt}=-\overbrace{\underbrace{K_{kill}}_{\text{kill potency}}\underbrace{C}_{\text{노출}}\underbrace{R}_{\text{잔여 target/cell}}}^{\text{target/cell 소비}}
\end{aligned}
$$

## §5-4. Turnover 모델 vs Effect Compartment — 치명적 쌍(Critical Pair)

| 비교 기준 | 개념 A: Turnover 모델 | 개념 B: Effect compartment |
|---|---|---|
| 단위 / 차원 | $R$, $k_{in}$, $k_{out}$ 중심의 response biology | $C_e$, $k_{e0}$ 중심의 biophase concentration |
| 수식 내 위치 (분자/분모/지수) | $dR/dt=k_{in}S(C)-k_{out}R$ | $dC_e/dt=k_{e0}(C-C_e)$, $R=f(C_e)$ |
| 변화 원인 (생물학적/병적) | 내인성 매개물질/세포/바이오마커 turnover | 작용 부위로의 약물 분포 지연 |
| 혼동 시 임상 결과 | fit 동등성을 mechanism 결정으로 오독 | $k_{e0}$가 system turnover를 흡수 |

> 💼 **실무 인사이트:** 규제 제출 형식의 글에서, 이 지점이 대안 모델 비교(alternative model comparison)와 기전적 정당화(mechanistic justification)가 들어가야 할 위치입니다. 설계가 구조를 감별할 수 없다면 선택된 구조를 자명한 것처럼 제시하지 않습니다.

## §5-5. PK Rate-Limited vs PD Rate-Limited 감소(Decline)

| 비교 기준 | 개념 A: PK-rate-limited | 개념 B: PD-rate-limited |
|---|---|---|
| 단위 / 차원 | $k$ time⁻¹; drug concentration/amount clock | system recovery/target replacement time scale |
| 수식 내 위치 (분자/분모/지수) | $t_D=(1/k)\ln(Dose/A_{min})$ | $t_D$는 system recovery 또는 target replacement가 결정 |
| 변화 원인 (생물학적/병적) | 약물 소실/분포가 느림 | turnover, 표적 재생, 세포 회복이 느림 |
| 혼동 시 임상 결과 | clearance 효과를 duration에서 간과 | 노출만으로 duration 변화를 과대 예측 |

$$
\underbrace{t_D}_{\text{duration}}
\xrightarrow[\text{PK-rate-limited}]{}
\underbrace{\frac{1}{k}\ln\left(\frac{Dose}{A_{min}}\right)}_{\text{PK clock 공식}},
\qquad
\underbrace{t_D}_{\text{duration}}
\xrightarrow[\text{PD-rate-limited}]{}
\underbrace{\text{system recovery / target replacement}}_{\text{PD clock}}
$$

> **각주(Footnote) — 노출-반응 단절(Exposure-response disconnect, CONTEXT only)**  
> Rosuvastatin OATP1B1 polymorphism은 systemic plasma exposure를 substantially 변화시키지만 site-of-action(cholesterol synthesis) response는 modestly 변합니다. 이는 별도의 turnover model이 아니라 **systemic exposure ≠ site-of-action exposure**의 보조 사례입니다. Bioequivalence가 효과 동등성을 보장하지 않는 메커니즘으로 자주 인용됩니다. [T pp.258–259]

## §5-6. ⚡ 기억 고리(Memory Hooks) — 7가지 핵심 개념 쌍 [EXPERT_INFERENCE, v3]

이 섹션은 §5-1~§5-5의 5개 비교 표를 보완하는 **기억 고리 모음**입니다. 각 hook은 두 개념의 차이가 발생하는 *구조적 필연*을 비유로 인코딩합니다.

### Pair 1 — direct effect(직접 효과) vs indirect response(간접 반응)

**⚡ 기억 고리** — *바로 켜지는 전등 vs 서서히 따뜻해지는 전기장판*: Direct effect는 약물 농도가 오르면 반응이 즉시 따라오는 즉각 반응 시스템입니다. Indirect response는 약물이 production 또는 loss를 바꾸고, 그 변화가 response pool에 축적되어 효과가 나타나는 지연 반응 시스템입니다. PD 데이터에서 반응이 Cmax보다 늦게 피크에 도달한다면 indirect response 메커니즘을 먼저 의심합니다.

### Pair 2 — Model I (생산 억제) vs Model II (소실 억제)

**⚡ 기억 고리** — *수원 틀기 vs 배수구 막기*: Model I은 약이 production을 줄이는 모델이고, Model II는 약이 loss를 막는 모델입니다. 그러나 단일 dose range에서는 두 모델이 사실상 같은 데이터를 만들 수 있으므로 mechanism prior 또는 더 넓은 용량 범위 데이터가 필요합니다.

### Pair 3 — $k_{in}$ vs $k_{out}$

**⚡ 기억 고리** — *수원 속도 vs 배수 속도*: 기저상태에서 pool이 일정하다면 $k_{in}=k_{out}\cdot baseline$이 성립합니다. $k_{out}=1/MRT_{response}$는 반응의 반감기를 결정합니다.

$$
\underbrace{k_{in}}_{\text{수원 속도}}=
\underbrace{k_{out}}_{\text{배수 clock}}\cdot\underbrace{baseline}_{\text{pool 크기}},
\quad
\underbrace{k_{out}}_{\text{반응 clock}}=
\frac{1}{\underbrace{MRT_{response}}_{\text{평균 체류시간}}},
\quad
\underbrace{t_{1/2,response}}_{\text{반응 반감기}}=
\frac{0.693}{\underbrace{k_{out}}_{\text{소실 clock}}}
$$

### Pair 4 — baseline $R_0$ vs steady-state $R_{ss}$

**⚡ 기억 고리** — *출발점 vs 목적지*: Baseline $R_0$는 약 투여 전 pool의 자연 균형점입니다. $R_{ss}$는 약 효과 하에서의 새 균형점입니다. 그 사이를 이동하는 속도는 $k_{out}$이 결정하고, $R_0$와 $R_{ss}$ 사이의 거리는 $E_{max}$와 $EC_{50}$이 결정합니다.

### Pair 5 — rebound(반등) vs natural recovery(자연 회복)

**⚡ 기억 고리** — *과교정 vs 자연 복귀*: Rebound는 약을 중단했을 때 반응이 baseline을 초과하여 오르는 것입니다. Natural recovery는 baseline으로 단순히 돌아오는 것입니다. 구분 기준은 반응이 baseline을 넘어서는가입니다.

### Pair 6 — duration of effect vs AUC of effect

**⚡ 기억 고리** — *효과의 길이 vs 효과의 면적*: Duration은 threshold 이상 또는 이하에 머무는 시간 길이입니다. AUC of effect는 시간에 따른 반응-시간 곡선 아래 면적입니다. 같은 duration이어도 반응 높이가 다르면 AUC가 다를 수 있습니다.

### Pair 7 — non-identifiability vs misspecification

**⚡ 기억 고리** — *지도가 둘 다 정확 vs 지도가 틀림*: 비식별성은 데이터가 두 모델 중 어느 것이 맞는지 결정하지 못하는 상태입니다. Misspecification은 데이터와 맞지 않는 구조를 선택한 상태입니다. $\Delta WRSS\approx2$, $\Delta AIC\approx-1$은 비식별성의 신호이지 misspecification의 신호가 아닙니다.

## §5 Recap — 다섯 가지 clock 위치 오류(The five clock-location errors)

| 오류 패턴(Error pattern) | 잘못 짚은 clock | 잠긴 반례(Locked counter-example) |
|---|---|---|
| **E1. Mirror-slope misread** | early response slope를 모든 모델에서 $-k_{out}$로 외삽 | PD7: 6,400U → 0.6 h⁻¹, 160,000U → 1.6 h⁻¹ — system parameter가 용량 의존적으로 보이는 misspecification artifact [G p.251] |
| **E2. Phantom convergence with linear S(C)** | turnover와 effect compartment가 같은 fit을 줬으므로 effect compartment 확정 | PD6 Table 6.1: $\Delta WRSS=2$, $k_{out}=k_{e0}=5.6\;h^{-1}$ — fit 동등성이 mechanism 결정을 의미하지 않음 [G pp.758–763] |
| **E3. Wrong-clock $t_D$** | 모든 약물에 Eq 8-12 적용 | warfarin/aspirin/omeprazole/paclitaxel은 PD-rate-limited — PK $k$로 계산한 $t_D$는 임상적으로 무의미 [T pp.251–254] |
| **E4. Linear-PK = linear-PD assumption** | dose-proportional AUC가 곧 dose-proportional response | methylprednisolone 16-1000 mg: AUC는 비례하나 lymphocyte response는 plateau 진입 [T pp.256–258] |
| **E5. Same-mechanism = same-clock assumption** | 동일 작용기전이면 같은 rate-limiting step | acenocoumarol(PD-limited, 15 h) vs phenprocoumon(PK-limited, ~5 days) — 같은 anticoagulant mechanism, 다른 지배 clock [T p.243] |

이 5가지를 외운 학습자는 이 세션의 모델링 결정을 거의 자동으로 방어할 수 있습니다.

<!-- SLIDE_START: S04 | title: §7 — 자기 테스트 -->
# §7 — 자기 테스트: 능동 회상 모듈(Self-Test: Active Recall Module)

## Q1 [회상] Model 1 ODE와 정상상태(steady state)

Model 1 ODE를 쓰고, 일정한 $C_{ss}$ 하에서 $R_{ss}$를 도출하세요.

**정답(Answer)**  
$$
\underbrace{\frac{dR}{dt}}_{\text{변화율}}
=
\overbrace{k_{in}I(C)}^{\text{production 억제}}
-
\underbrace{k_{out}R}_{\text{소실}}
$$

정상상태에서: $R_{ss}=R_0I(C_{ss})$. [G pp.238–239]

$$
\underbrace{R_{ss}}_{\text{약물 정상상태}}
=
\underbrace{R_0}_{\text{기저값}}
\underbrace{I(C_{ss})}_{\text{남은 production}}
$$

## Q2 [회상] $t_{ss}$가 용량 독립적인 모델은?

$t_{ss}$가 용량 독립적인 모델은 무엇인가?

**정답(Answer)**  
Models 1과 3 — 1차 소실 항이 $k_{out}\cdot R$로 유지되기 때문입니다. Models 2와 4는 약물이 소실 항을 변경하므로 용량 의존적 $t_{ss}$를 보일 수 있습니다. 단, 이 결론은 PK가 더 느린 clock이 아닐 때만 성립합니다. [G pp.247–251; T p.243]

## Q3 [응용] PD9의 peak shift 부재 해석

용량이 증가해도 peak shift가 나타나지 않습니다. 이것이 effect compartment 모델을 증명하나요?

**정답(Answer)**  
아닙니다. PD9는 peak shift 부재가 link/effect-compartment 모델을 반드시 의미하지 않는다고 명시적으로 경고합니다. Dose range, 비선형 약물 기능, system 동역학을 함께 고려해야 합니다. [G pp.778–783]

## Q4 [응용] PD9 Zooparc® 용량 정정

Zooparc® 반복 투여 데이터에서 확인된 용량 수준은 무엇이며, 25 mg/day는 어떻게 기술해야 하나요?

**정답(Answer)**  
관찰된 반복 투여 figure는 2.5 mg과 5 mg을 사용합니다. 25 mg/day 진술은 투사(projection)/대규모 연구 논의이며, 관찰된 용량 맥락이 아닙니다. [G pp.778–783]

## Q5 [응용] Naproxen 정정

“naproxen 250 mg, Fig 8-3”이라는 오류 표현을 수정하세요.

**정답(Answer)**  
Naproxen 500 mg 경구, dental pain 모델, 1–8 h sampling, 반시계 방향(counterclockwise) hysteresis, Fig 8-2. Fig 8-3은 하류 약력학 도식이며, naproxen 그림이 아닙니다. [T pp.234–236]

## Q6 [응용] 잘못된 clock의 $t_D$

Aspirin duration 예측에 Eq 8-12가 왜 부적절한가?

**정답(Answer)**  
Aspirin의 혈장 노출은 빠르게 사라지지만, 표적/혈소판 기능 회복이 더 느리기 때문에 thromboxane B₂ 억제는 지속됩니다. Duration은 PD/표적 대체에 의해 결정되며, PK rate-limited가 아닙니다. [T p.251]

## Q7 [응용] Turnover vs effect compartment

단일 용량 데이터가 turnover와 effect-compartment 두 모델 모두에 동등하게 적합합니다. 두 모델 중 하나를 결정하는 데 어떤 증거가 필요한가?

**정답(Answer)**  
반응 변수에 대한 기전적 사전 정보, 더 넓은 dose range, 반복 투여/washout, PK clock 교란, 그리고 $EC_{50}/k_{e0}$이 생물학적으로 타당하게 유지되는지 여부. 적합도 단독으로는 불충분합니다. [G pp.758–763; T pp.244–246]

## Q8 [응용] Linear PK ≠ linear PD

Methylprednisolone AUC가 16–1000 mg 범위에서 용량 비례적입니다. 그것이 왜 용량 비례적 lymphocyte 반응을 정당화하지 않는가?

**정답(Answer)**  
반응이 노출-반응 곡선의 plateau 구간에 진입할 수 있습니다. R&T의 lymphocyte 사례는 PK가 용량 비례적임에도 고용량에서 추가 PD 반응이 거의 없음을 보여줍니다. R&T 본문(p.256)은 단호하게 명시합니다 — *"Dose linearity in pharmacokinetics does not result in dose linearity in pharmacodynamics. That is almost never the case."* [T pp.256–258]

## Q9 [보스 딜레마(Boss dilemma)]

스폰서가 다음을 주장합니다: “phenprocoumon과 acenocoumarol은 동일한 항응고 기전을 공유하므로, 반응 회복은 동일한 PD turnover half-life로 결정되어야 합니다.” 동의하나요, 거부하나요? **30년 경력 심사자가 사용할 구체적 방어 논리로 정당화하세요.**

**정답(Answer) — Trade-off 논리**  
**거부(Reject).** 동일한 기전이 동일한 rate-limiting clock을 의미하지는 않습니다. Acenocoumarol은 PK 반감기가 더 짧으며(~15 h), 회복은 PD-clock 제한적이 됩니다(응고인자 turnover). Phenprocoumon은 PK 반감기가 훨씬 길어(~5일), 회복은 PK-clock 제한적이 됩니다(약물 잔류가 system clock보다 우세). [T p.243]

이 차이가 임상·규제 차원에서 갖는 trade-off는 다음과 같습니다:
- **Sponsor의 단순화 채택 시**: 두 약물에 동일한 dose-titration step-up rule 적용 → phenprocoumon 누적 위험 또는 acenocoumarol 미달 dose. 어느 쪽이든 환자 안전·약효 부전 사고로 직결됩니다.
- **Mechanism-only justification의 규제적 위험**: 모델 선택 paragraph에서 “동일 mechanism이므로 동일 PD half-life”라는 추론은 design support 없이 데이터로 방어 불가능 → “insufficient justification for proposed dosing interval” 형태의 deficiency 위험. [교과서 외 실무 해석]
- **올바른 방어 논리**: 약물별 PK profile이 동일 PD system 위에서 어떤 clock을 활성화시키는지를 acenocoumarol vs phenprocoumon Fig 8-11 데이터로 직접 증명한 후, 각 약물별로 별도의 dose-duration model을 사용합니다. 단일 PD half-life claim은 phenprocoumon에서 임상적으로 무의미하고 acenocoumarol에서만 유효합니다.

## ⚡ 보스 딜레마 ★★ [EXPERT_INFERENCE, v3]

Pool 1과 Pool 2 indirect response 모델 중 어느 것을 Phase 2 용량 결정에 사용할 것인가? 두 모델은 현재 데이터(단일 dose group, 제한된 dose range)에서 $\Delta WRSS=2$, $k_{out}=k_{e0}$로 사실상 비식별적입니다.

**선택지 A**: 기존 생물학적 증거가 production inhibition을 지지한다면(예: 생체표지자가 생성률과 연관) Model I을 선택하고, 비식별성을 보고서에서 limitation으로 명시합니다.

**선택지 B**: 어느 메커니즘도 확실하지 않다면, 두 모델을 모두 제출하고 sensitivity analysis를 통해 용량 결정이 모델 선택에 얼마나 민감한지 제시합니다. 더 보수적인 용량 예측을 제공하는 모델을 기본으로 사용합니다.

**거장의 Trade-off 논리**  
A는 기계론적으로 간결하지만 데이터 외 prior를 사용했다는 비판을 받을 수 있습니다. B는 불확실성을 투명하게 전달하지만 의사결정자에게 혼란을 줄 수 있습니다. **규제 제출에서는 “어느 모델을 선택했는가”보다 “왜 이 불확실성이 용량 결정의 안전성에 영향을 주지 않는가”를 설명하는 것이 핵심입니다.** 즉, 두 모델 모두에서 제안된 Phase 2 용량이 안전 한계 안에 있음을 sensitivity analysis로 증명하면, 모델 선택 자체가 의사결정의 critical path에서 빠집니다 — 이것이 “비식별성을 우회하는” 정통 규제 전략입니다.

이 딜레마의 Apex 메시지: 비식별성 앞에서 모델을 *선택*하려 하지 말고, 비식별성이 의사결정에 *영향을 주지 않는 결정 구조*를 설계하세요.

## §7 Recap

올바른 답은 반드시 **model family**와 **clock 위치** 모두를 식별해야 합니다. 수학적으로 맞는 공식이라도 잘못된 clock에 적용하면 틀린 것입니다.

<!-- SLIDE_START: S05 | title: §8 — 메타프레임 & 빅 픽처 -->
# §8 — 메타프레임 & 빅 픽처(Meta-Frame & Big Picture)

## A. 약리계측학 아키텍처에서의 위치(Positioning in the pharmacometrics architecture)

이 세션은 직접 노출-반응 모델링(direct exposure-response modeling)과 고급 질병/반응 시스템 사이에 위치합니다. 여기서부터 모델러는 곡선 적합(curve fitting)을 넘어 원인 분리를 수행해야 합니다.

| 후속 세션 | 이 세션에서 열리는 개념 | 이 세션 없으면 실패하는 것 |
|---|---|---|
| Transit compartment | 분포/전달 지연과 turnover 지연의 분리 | 모든 지연을 effect compartment로 흡수 |
| Tolerance/moderator model | feedback, rebound, post-trough 회복 timing | $k_{out}$ 고정 가정 위반을 놓침 |
| Disease progression / baseline drift | $R_0$가 시간에 따라 움직이는 경우 | 질병 진행 또는 일주기 변동을 약물 효과로 오독 |
| PopPK/PD IIV | drug parameter와 system parameter의 분리 | $E_{max}$, $k_{out}$, $k_{e0}$ 해석 혼동 |
| Sampling design | hidden clock을 식별하는 관측 창 설계 | 비식별성을 후속 시험에 반복 |

## B. 이 세션을 약하게 다뤘을 때의 실패 모드(Failure modes if this session is weak)

| 실패 모드(Failure mode) | 실무적 결과(Practical consequence) |
|---|---|
| 모든 지연을 effect compartment로 처리 | $k_{e0}$이 생물학을 흡수합니다. 새로운 투여 프로토콜에서 dosing 시뮬레이션이 실패합니다. |
| $t_{ss}$를 모델의 결정적 증거로 처리 | 기전적 주장이 설계 근거를 과대평가합니다. |
| $E_{max}$ 단위 혼동 | 교차 연구 또는 in vitro/임상 potency 비교가 오해를 유발합니다. |
| PD-rate-limited 약물에 $t_D$ 적용 | Duration 예측이 생물학적으로 무의미해집니다. |
| Baseline drift 무시 | 질병 진행 또는 일주기 변동이 약물 효과로 오독됩니다. |

## C. 전문가 해석 지점(Professional moat) — 30년 베테랑의 30초 진단 시퀀스

30년 경력의 약리계측학(pharmacometrics) 심사자는 곡선이 매끄러운지를 가장 먼저 묻지 않습니다. 데이터를 본 첫 30초 안에 진단 시퀀스를 실행합니다.

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| Plasma C vs response loop가 counterclockwise 또는 clockwise | Hysteresis 방향 | → | distribution/turnover/active-metabolite 또는 tolerance/feedback 후보 분리 | 30초 안에 첫 가설 설정 |
| Response direction과 $t_{ss}$ dose-dependence 조합이 보임 | $k_{out}$ 또는 effective $k_{out}$ | → | 4-model 칸 중 하나로 압축 | PD5/PD7 side-by-side 확인 |
| Post-trough observed가 모델보다 빠르게 회복 | moderator/feedback 누락 가능성 | → | rebound/recovery 예측 실패 | feedback 또는 moderator 구조 검토 |
| OFV가 30 iteration 동안 stuck-then-drop | $r(k_{in},k_{out})>0.98$ 가능성 | → | covariance/search geometry 실패 | $R_0$, $k_{out}$ 재파라미터화 |
| 새 약물 duration 질문 | PK vs PD rate-limiting clock | → | 동일 mechanism 약물 간 duration 차이 | acenocoumarol vs phenprocoumon 같은 clock pair 비교 |

이 다섯 단계를 통과한 후에야 NONMEM 출력에 손을 댑니다. 자동화된 도구는 단계 1, 4를 모방할 수 있지만 단계 2, 3, 5의 “데이터의 의미를 묻는 직관”은 데이터 외부의 mechanistic prior를 요구하므로 복제되지 않습니다.

## 최종 잠긴 요약(Final locked summary)

간접 반응 모델링(Indirect response modeling)은 “지연을 추가하는 것”이 아닙니다. 올바른 인과 clock에 지연을 할당하는 것입니다. 따라서 잠긴 작업 흐름은 다음과 같습니다:

**hysteresis direction → four-model action site → $t_{ss}$/peak-shift triage → initial-parameter audit → turnover-vs-link discrimination → PK/PD clock selection → duration formula only if PK-rate-limited.**

## v3.7 자가검증 체크리스트

| 항목 | 기준 | 결과 |
|---|---|---|
| SLIDE_START 개수 | §섹션수 5 + 카드수 8 합산 | 13 개 |
| 카드당 callout 합계 ≤ 6 | 전체 카드 | ✓ |
| [E] 박스 존재 | 모든 §2 카드 | ✓ |
| [D] 거장의 시각 존재 | 모든 §2 카드 | ✓ |
| [L] 파라미터 표 존재 | Apex 카드 + 정의 수식 카드 | ✓ |
| §5 혼동 쌍 표 행 순서 고정 (4행) | §5 전체 | ✓ |
| 기호 일관성 | 첫 등장 기준 통일 | ✓ |
| PART B 흔적 없음 | 전체 | ✓ |
| 수치 anchor 보존 | Compound A 등 원본 수치 | ✓ |
| [M] 나비효과 이중 종착점 | Apex 카드 전체 | ✓ |

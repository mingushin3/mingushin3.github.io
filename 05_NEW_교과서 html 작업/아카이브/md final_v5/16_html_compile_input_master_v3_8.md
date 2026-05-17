# 16_HTML Compile Input Master — Session 016 v3.8

# Session 016 — 임상 통합 캡스톤: 패턴 인식 · TDM · 질환 · 치료 의사결정 — v3.8

> **임상 장면**
> 55세 60 kg CHF 남성. digoxin(Lanoxicap) 0.2 mg daily 복용. 458 h 농도 2.5 µg/L, 479 h 농도 0.9 µg/L. Bayesian 추정값은 $CL$ 5.7 L/h, $V$ 119.6 L, $t_{1/2}$ 14.5 h로 population 값($CL_{pop}$ 1.8 L/h, $V_{pop}$ 500 L)과 크게 달랐습니다 [G&W pp.641–643].
> 이 숫자를 처방으로 옮기기 전에 던져야 할 질문은 하나입니다 — **"그 농도가 실제로 어떤 파라미터를 식별했는가?"**

## §0 — 빠른 시작

이 세션은 **모델 선택 → 질환 보정 → 개인 추정 → 처방·모니터링 → 노출 보고**로 이어지는 임상 의사결정 체인을 다룹니다.

시간이 부족하면 **M1 → M4 → M5 → M8 → M9** 다섯 카드만 순서대로 읽어도 이 세션의 의사결정 체계가 작동합니다.

| 카드 | 이 경로에서의 역할 |
|---|---|
| **M1** | shape를 읽어 모델 후보를 줄인다 |
| **M4** | Bayesian posterior로 개인 파라미터를 추정한다 |
| **M5** | $f_e \times RF$로 신질환 보정을 계산한다 |
| **M8** | TCS 기준으로 모니터링 시작 여부를 가른다 |
| **M9** | LD($V$)와 MD($CL$)를 분리해 어떤 dose를 바꿀지 정한다 |

**머릿속에 둘 네 가지 구분**:
- 진단 신호 ≠ 모델 증명
- 환자 속성($RF$) ≠ 약물 속성($f_e$)
- $V$ 기반 LD ≠ $CL$ 기반 MD
- 측정 농도 ≠ 해석 가능한 농도

---

## 소스 범위

- **Gabrielsson & Weiner 5e**: Ch.6 Pattern Recognition [pp.423–466], PK15 Toxicokinetics [pp.546–548], PK35 Bayesian model — Digoxin [pp.641–643]
- **Rowland & Tozer 5e**: Ch.15 Disease [pp.443–489], Ch.18 Initiating and Managing Therapy [pp.577–610]

---

<!-- SLIDE_START: §1 | title: 세션 헤더 & 로드맵 -->

# §1 — 세션 헤더 & 로드맵 (Session Header & Roadmap)

**Session ID**: 016 — 임상 통합 캡스톤: pattern recognition, TDM(농도 측정으로 용량 판단을 보정하는 전략), disease, therapeutic decision-making

**핵심 통찰 (Big Idea)**
데이터의 **형태(shape)는 그 데이터를 만든 동역학 메커니즘의 흔적**입니다. 질환은 그 메커니즘의 파라미터를 모집단에서 벗어나게 만들고, Bayesian TDM은 환자별 편차를 추정하며, Ch.18은 그 추정을 용량·채혈·모니터링 결정으로 바꿉니다.

**캡스톤 척추 (Capstone spine)**

```text
[Ch.6 Pattern Recognition]   → 어떤 PD 구조가 가능한가?
[Ch.15 Disease]              → 환자 parameter가 population에서 왜 벗어났는가?
[PK35 Bayesian TDM]          → 관측 농도와 prior를 어떻게 결합하는가?
[Ch.18 Initiating/Managing]  → loading, maintenance, TCS, missed dose를 어떻게 판단하는가?
[PK15 Toxicokinetics]        → 선택된 용량의 exposure와 safety margin을 어떻게 보고하는가?
```

### 3층 개념 지도

```text
레이어 1. 무엇인가
  ├─ plot shape: baseline / delay / peak-shift / saturation
  ├─ 환자 속성: RF, SCr trend, dialysis state
  └─ 약물 속성: f_e, F, V, CL, therapeutic window

레이어 2. 어떻게 계산되는가
  ├─ Bayesian objective: concentration likelihood + population prior
  ├─ renal adjustment: R_d = RF·f_e + (1-f_e)
  ├─ dialysis: k_D = (CL_u + CL_{uD})/V_u
  └─ dosing: LD는 V, MD는 CL, missed dose는 superposition

레이어 3. 언제, 왜 중요한가
  ├─ posterior가 식별 가능한 정보 위에 있는가?
  ├─ renal label과 drug f_e를 분리했는가?
  ├─ TCS가 다음 처방 결정을 실제로 바꾸는가?
  └─ exposure/safety margin 보고가 source boundary 안에 있는가?
```

🧭 **읽는 순서**
- 카드 1 (M1): plot shape는 어떻게 모델 후보를 줄이는가?
- 카드 2 (M2): peak-shift와 saturation은 왜 판결이 아니라 진단 신호인가?
- 카드 3 (M3): delay가 어느 state($C_e$, $R$, $RC$)에 박혀 있는가?
- 카드 4 (M4): Bayesian posterior는 농도와 prior 중 무엇에 의해 움직이는가?
- 카드 5 (M5): renal dosing에서 약물 속성($f_e$)과 환자 속성($RF$)을 어떻게 분리하는가?
- 카드 6 (M6): Cockcroft-Gault 숫자는 왜 시간 지연과 함께 읽어야 하는가?
- 카드 7 (M7): 투석 보충 용량은 왜 half-life가 아니라 body amount 문제인가?
- 카드 8 (M8): TCS는 언제 "측정 가능"을 넘어 "결정 가능" 전략이 되는가?
- 카드 9 (M9): loading dose와 maintenance dose는 왜 서로 다른 파라미터가 지배하는가?
- 카드 10 (M10): missed/unequal/erratic dosing은 어떻게 superposition 문제로 바뀌는가?

### 유지된 데이터 앵커

- **PK35 digoxin**: 55세 60 kg CHF 남성; Lanoxicap 0.2 mg daily; 458 h 2.5 µg/L, 479 h 0.9 µg/L; $CL_{pop}$ 1.8 L/h, $V_{pop}$ 500 L; 추정 $CL$ 5.7 L/h, $V$ 119.6 L, $t_{1/2}$ 14.5 h [G&W pp.641–643].
- **PK15 toxicokinetics**: 10/56/320 µmol·day⁻¹·kg⁻¹ dose levels, Cmax/AUC 노출 보고, therapeutic 농도 0.05–0.1 µM, high-dose Cmax 약 50 µM, safety margin >100배 [G&W pp.546–548].
- **Ch.18**: Table 18-6 데이터 수집, Eq.18-1–18-4 dosing irregularity 식, Fig.18-13 채혈 시점별 $V$ vs $CL$ 신뢰도 [R&T pp.597, 601–605].

> **§1 recap**: 이 세션은 "모델 선택 → 질환 보정 → 개인 추정 → 처방·모니터링 → 노출 보고" 체인을 잠급니다.

> 📊 **개념 도식 (HTML 렌더링)**: Session 016 캡스톤 척추 — 데이터 형태에서 노출 보고까지. Ch.6은 모델 후보를, Ch.15는 환자별 편차를, PK35는 사후 파라미터를, Ch.18은 용량·모니터링 결정을, PK15는 노출·안전역 보고를 만듭니다.

---

<!-- SLIDE_START: §2 | title: 개념 해부 카드 -->

# §2 — 개념 해부 카드 (Concept Anatomy Cards)

> 🎯 plot shape는 모델을 확정하는 도장이 아니라 후보를 줄이는 triage 언어입니다. baseline·delay·peak-shift·saturation 순서를 먼저 잠그세요.

---

<!-- SLIDE_START: M1 | title: 패턴 인식 의사결정 흐름(Pattern-recognition decision workflow) -->

### 🃏 M1 — 패턴 인식 의사결정 흐름(Pattern-recognition decision workflow) [G&W pp.423–424, pp.465–466] [⚡ Apex Concept]

> **거장의 시각**
> 흔한 오해는 "population model이 검증되면 posterior, TDM, dosing decision은 자동으로 따라온다"는 것입니다. 실제로는 shape 관찰 하나가 잘못되면 모델 후보부터 노출 보고까지 같은 방향으로 기울어집니다. 체화할 한 가지 직관 — **plot shape는 모델 확정 도장이 아니라 임상 의사결정 체인의 첫 triage 언어입니다.**

> 💡 **Shape-first 원칙** — plot을 보자마자 모델명을 말하지 말고 baseline → delay → peak-shift → saturation 순서로 묘사합니다. 빠른 후보 축소는 모델 검증이 아닙니다 — fitting, diagnostics, sampling adequacy가 그 뒤에 남습니다.

**A. 형식적 정의와 핵심 구조**

**핵심**: response-time, concentration-time, concentration-response plot은 먼저 baseline, time-delay, peak-shift, saturation/slope 순서로 읽습니다. 그 다음 Fig.6.12 workflow처럼 C/R vs time, C-R plot(농도-반응 관계를 시간과 분리해 보는 그림), hysteresis(시간 지연으로 C-R 관계가 고리처럼 보이는 현상), rebound, tolerance 여부를 순서대로 확인합니다.

**확정된 형식**

```text
1. Baseline: 안정한가? 표류하는가? 질병 진행/적응이 있는가?
2. Time-delay: 농도 peak와 response 극값이 분리되는가?
3. Peak-shift: dose 증가에 따라 response 극값이 좌/우로 이동하는가?
4. Saturation/slope: high dose에서 평탄 구간 또는 비선형 변화가 보이는가?
5. C-R plot: direct, indirect, rebound, tolerance, hysteresis 중 어느 후보가 남는가?
```

**현장 팁**: 단일 dose response-time curve 하나만으로 mechanism을 확정하지 마세요. **중요한 건 dose escalation에서 shape가 어떻게 바뀌는가**입니다. 이 변화가 model-class narrowing의 핵심입니다.

§2.1은 plot-reading grammar이고, §2.2–§2.3은 그 grammar가 실제 ODE 후보로 내려가는 첫 번째 mechanistic bridge입니다.

> 📖 **G&W Ch.6 Fig.6.1 [p.423], Fig.6.12 [pp.465–466]**: Fig.6.1은 baseline·delay·peak-shift·saturation·slope라는 초기 시각 문법을 보여주고, Fig.6.12는 그 문법을 실제 분석 workflow로 바꿉니다.

**Plausible Fallacy — 나비효과 연쇄**
**오류**: 집단 모델이 검증되면 TDM과 용량 결정은 소프트웨어가 자동으로 처리한다.
**왜 그럴싸한가**: Bayesian TDM 소프트웨어가 항상 posterior mean과 개인 $CL/V$ 값을 출력하기 때문입니다.
**나비효과**: model validation을 decision automation으로 오독 → sampling timing과 posterior uncertainty 점검 생략 → 실제 clearance와 무관한 dose로 독성 또는 치료 실패 → 식별 불가 parameter에 기반한 exposure 보고로 reviewer가 sampling identifiability와 dose-rationale 재분석을 요구.

> **M1 체화 핵심**
> ① 새 response-time plot을 처음 볼 때 → baseline·delay·peak-shift·saturation 순서가 후보를 결정
> ② 검증된 모델 vs 실제 dosing decision → sampling identifiability와 posterior uncertainty가 지배
> ⚡ 모델 검증 후 decision 자동화 → 식별 불가 posterior를 dose에 반영해 치료 실패 또는 독성 예측 실패

---

<!-- SLIDE_START: M2 | title: 피크 이동 + 포화: 결정 규칙이 아니라 진단 신호(Peak-shift + saturation) -->

### 🃏 M2 — 피크 이동 + 포화: 결정 규칙이 아니라 진단 신호(Peak-shift + saturation) [G&W pp.424–428]

> **앞 카드에서 이 카드로**
> M1에서 shape-reading 순서를 정했으므로, 이제 peak-shift와 saturation이 어떤 후보를 남기는지 분리합니다.

> **거장의 시각**
> Peak-shift 방향을 모델명으로 곧장 번역하면 turnover와 receptor on/off 후보를 너무 일찍 닫아 버립니다. 방향과 saturation을 함께 읽으면 "확정"이 아니라 남겨야 할 competing candidates가 보입니다.

> 💡 **방향은 단서일 뿐** — left/right movement는 후보 목록을 줄이는 sign이지 단일 mechanism을 확정하지 않습니다. left-shift를 곧바로 $k_{on}$ 증가로 읽으면 turnover loss stimulation 후보를 지워 버립니다.

**A. 형식적 정의와 핵심 구조**

**핵심**: peak-shift 방향은 모델 클래스 그 자체가 아닙니다. competing model candidates를 좁히는 1차 진단 신호입니다.

| 관찰된 패턴 | 확정된 해석 |
|---|---|
| Case A: plasma peak이 $R_{min}$까지 걸리는 시간의 약 1/3 시점에 발생 | response delay가 존재합니다. direct-effect 모델 단독은 가능성이 낮습니다. |
| Case B: 고용량에서 trough가 좌측 이동 | turnover loss stimulation 또는 receptor on/off가 후보로 떠오를 수 있습니다. 자동 결론은 아닙니다. |
| Case C: 최고용량에서 trough가 우측 이동 + flat 구간 출현 | saturation을 동반한 input inhibition이 강한 후보 신호입니다. |

**현장 팁**: Case B의 left-shift를 "$k_{on}$이 큰 약물"로 외우지 마세요. receptor on/off에서는 finite receptor pool 때문에 nadir가 빨라질 수 있고, turnover model에서도 loss stimulation이 유사한 패턴을 만듭니다.

> 📖 **G&W Ch.6 Fig.6.2 [p.424], Fig.6.3 [p.428]**: Fig.6.2는 반응-시간 움직임이 좌측 또는 우측으로 이동하는 모습을, Fig.6.3은 competing alternatives를 함께 보여주어 하나의 pattern을 하나의 model에 바로 대응시키는 오류를 막아 줍니다.

> **M2 체화 핵심**
> ① peak가 좌우로 움직일 때 → 방향과 saturation 유무가 후보군을 결정
> ② 방향 신호 vs 모델 확정 → competing candidates를 유지하는 것이 지배
> ⚡ peak-shift 방향 = 모델 클래스 → deterministic overclaim으로 보고서 신뢰도 저하

---

<!-- SLIDE_START: M3 | title: 효과구획 / turnover / receptor on-off 원형(Effect compartment / turnover / receptor on-off prototypes) -->

### 🃏 M3 — 효과구획 / turnover / receptor on-off 원형(Effect compartment / turnover / receptor on-off prototypes) [G&W pp.425–427]

> **앞 카드에서 이 카드로**
> M2가 peak-shift를 후보 축소 신호로 제한했으므로, 이제 그 후보들이 실제 ODE state에서 어떻게 갈라지는지 봅니다.

> **거장의 시각**
> effect compartment, turnover, receptor on/off를 식 이름으로만 외우면 새 plot에서 delay의 위치를 놓칩니다. **delay가 $C_e$, $R$, $RC$ 중 어느 state에 박혔는가**를 묻는 순간 세 prototype이 분리됩니다.

> 🔑 **Delayed state 규칙**: link model은 $C_e$, turnover는 $R$, receptor binding은 $RC$에 지연이 걸립니다. 모든 hysteresis가 effect compartment를 뜻하지는 않습니다 — baseline/rebound/adaptation이 있으면 turnover를 다시 확인합니다.

**A. 형식적 정의와 핵심 구조**

**핵심**: Ch.6의 Case A–I 수식들은 외울 목록이 아니라, 세 prototype(반복적으로 재사용되는 대표 구조)을 구분하는 pattern library입니다.

#### Prototype 1 — 효과구획 (Effect compartment)

Time-delay는 있으나 dose 증가에 따른 clear peak-shift가 약하면 link model을 먼저 의심합니다.

$$
\underbrace{\frac{dC_e}{dt}}_{\text{$C_e$ 변화}}
=
\underbrace{k_{e0}}_{\text{평형 속도}}
\overbrace{\left(\underbrace{C}_{\text{혈장}}-\underbrace{C_e}_{\text{효과부위}}\right)}^{\text{농도 차}}
$$

**파라미터 해부 표**

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $C_e$ | 농도 | effect site 농도 | distribution delay, equilibration speed |
| $k_{e0}$ | 시간⁻¹ | plasma와 effect site 평형 속도 | tissue access, link-model dynamics |
| $R$ | response 단위 | turnover system의 반응량 | input/loss modulation |
| $k_{in}$, $k_{out}$ | response/time, 시간⁻¹ | 생성·소실 속도 | disease state, drug effect |
| $RC$ | receptor complex | 결합된 receptor pool | $k_{on}$, $k_{off}$, finite receptor pool |

💡 **비유**: effect compartment는 혈장이라는 복도에서 실제 효과 방으로 약물이 들어가는 작은 대기실입니다. 복도 농도는 이미 높아도 대기실 농도가 늦게 차면 반응도 늦습니다.

Response model은 $C$가 아니라 $C_e$에 연결됩니다. Counter-clockwise hysteresis는 effect-site equilibration delay의 전형적 신호입니다 [G&W p.426].

#### Prototype 2 — 회전 모델 (Turnover model)

Response variable $R$은 생성과 소실의 동적 평형 위에 있을 수 있습니다. 이때 drug은 input 또는 loss process를 억제하거나 자극합니다.

$$
\underbrace{\frac{dR}{dt}}_{\text{$R$ 순변화}}
=
\overbrace{\underbrace{k_{in}}_{\text{생성}}\cdot\underbrace{I(C)}_{\text{농도 조절}}}^{\text{input}}
-
\underbrace{k_{out}R}_{\text{소실}}
$$

$$
\underbrace{\frac{dR}{dt}}_{\text{$R$ 순변화}}
=
\underbrace{k_{in}}_{\text{기본 생성}}
-
\overbrace{\underbrace{k_{out}R}_{\text{기본 소실}}\cdot\underbrace{S(C)}_{\text{농도 자극}}}^{\text{loss}}
$$

💡 **비유**: turnover는 물탱크의 수도꼭지와 배수구입니다. 약물은 물탱크 크기 자체보다 들어오는 속도나 빠지는 속도를 바꿔 새 수위를 만듭니다.

Baseline $R_0=k_{in}/k_{out}$는 정적 ratio가 아니라 dynamic equilibrium입니다. 새 평형으로 이동하는 속도는 주로 $k_{out}$이 정합니다.

#### Prototype 3 — 수용체 on/off (Receptor on/off)

Receptor binding이 finite pool을 가진다면 response 극값의 timing은 $k_{on}\cdot C\cdot(R_T-RC)$와 $k_{off}\cdot RC$의 경쟁으로 결정됩니다.

$$
\underbrace{\frac{dRC}{dt}}_{\text{$RC$ 변화}}
=
\overbrace{\underbrace{k_{on}}_{\text{결합 속도}}\underbrace{C}_{\text{농도}}\underbrace{(R_T-RC)}_{\text{free 수용체}}}^{\text{결합 형성}}
-
\underbrace{k_{off}RC}_{\text{해리}}
$$

**현장 팁**: Case A–I 식 전수 암기보다 **direct delay / turnover delay / finite-pool binding** 중 어느 failure mode가 지금 plot을 설명하는지 먼저 판단하세요.

**§2.1–§2.3 recap**: Ch.6의 목적은 shape에서 모델 후보를 줄이는 것입니다. Pattern은 proof가 아니라 triage signal입니다.

> **M3 체화 핵심**
> ① delay가 있으나 peak-shift가 약할 때 → $C_e$ equilibration이 지배
> ② baseline/rebound/adaptation이 보일 때 → $R$ turnover가 지배
> ⚡ Case A–I 식 전수 암기 → 새 데이터에서 delayed state를 놓쳐 ODE 후보 선택 실패

---

<!-- SLIDE_START: M4 | title: 개인 TDM을 위한 베이지안 목적함수(Bayesian objective function for individual TDM) -->

### 🃏 M4 — 개인 TDM을 위한 베이지안 목적함수(Bayesian objective function for individual TDM) [G&W pp.641–643; R&T pp.605–606]

> **앞 카드에서 이 카드로**
> M3가 가능한 구조를 세 prototype으로 줄였으므로, 이제 그 구조 안에서 이 환자의 파라미터가 어디에 있는지 추정합니다.

> **거장의 시각**
> Bayesian posterior 숫자를 그대로 개인 진실로 읽으면, sampling time과 prior variance가 만든 착시를 놓칩니다. **posterior가 어떤 parameter를 실제로 식별했는지** 보면 dosing decision에 옮겨도 되는 숫자와 아닌 숫자가 갈립니다.

> 💡 **Posterior는 힘겨루기** — 농도 likelihood와 population prior 중 어느 쪽 variance가 작은지가 추정값을 끌고 갑니다. posterior mean은 항상 출력되지만, 식별 가능한 정보 위에 있지 않으면 dose 결정의 근거가 아닙니다.

**A. 형식적 정의와 핵심 구조**

**핵심**: Bayesian TDM은 observed concentrations만 믿지 않고, population average만 믿지도 않습니다. **농도 likelihood와 population prior의 상대적 variance**를 함께 보고 개인 parameter를 추정합니다.

§2.1–§2.3이 "어떤 구조가 가능한가"를 줄였다면, §2.4는 "이 환자의 parameter가 어디에 있는가"를 추정합니다.

**개념적 목적함수**

$$
\underbrace{OBJ_{Bayes}}_{\text{총 penalty}}
\approx
\underbrace{\sum_i\frac{\left(C_{obs,i}-\hat C_i\right)^2}{\operatorname{var}(\hat C_i)}}_{\text{농도 mismatch}}
+
\underbrace{\sum_j\frac{\left(P_{pop,j}-\hat P_j\right)^2}{\operatorname{var}(\hat P_j)}}_{\text{prior 이탈}}
$$

**파라미터 해부 표**

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $OBJ_{Bayes}$ | 무차원 penalty | 농도 mismatch와 prior 이탈의 합 | assay error, prior variance, model misspecification |
| $C_{obs,i}$ | 농도 | 관측 농도 | sampling time, adherence, assay |
| $\hat C_i$ | 농도 | model-predicted 농도 | $CL$, $V$, dose history |
| $P_{pop,j}$ | parameter별 | population prior | reference population, covariate model |
| $\hat P_j$ | parameter별 | individual posterior estimate | likelihood-prior balance |

💡 **비유**: Bayesian TDM은 두 사람이 줄다리기를 하는 장면입니다. 농도 자료의 줄이 약하면 prior가 끌고, prior가 약하면 농도가 끌며, 어느 쪽 줄이 튼튼한지는 variance가 정합니다.

- 농도 없음 → population average가 사실상 estimate가 됩니다.
- prior 없음 → maximum-likelihood concentration fitting에 가까워집니다.
- 농도 + prior 있음 → complete Bayesian method가 됩니다.

**PK35 digoxin 앵커**: 55세 60 kg CHF 남성, Lanoxicap 0.2 mg daily, 458 h 2.5 µg/L, 479 h 0.9 µg/L, $CL_{pop}$ 1.8 L/h, $V_{pop}$ 500 L, 추정 $CL$ 5.7 L/h, $V$ 119.6 L, $t_{1/2}$ 14.5 h [G&W pp.641–643].

**채혈 식별가능성 앵커**: R&T Fig.18-13은 **early sample이 $V$에 더 민감하고 late/plateau sample이 $CL$에 더 민감**함을 보여줍니다. 따라서 $1\times t_{1/2}$ 근처 sampling만으로는 $CL$ 1/3 변화와 $V$ 3배 변화를 구분하기 어렵습니다. $CL$을 정확히 추정하려면 $4\times t_{1/2}$ 또는 steady-state 시점의 정보가 필요합니다 [R&T pp.605–606].

**현장 팁**: Bayesian posterior(관측 후 갱신된 개인 추정값)가 이상한 $V$를 내면 "환자가 이상하다"고 먼저 결론내리지 마세요. sampling time, dosing history, prior variance, assay error, adherence를 먼저 점검합니다.

**경계**: PK35 digoxin은 $CL/V/t_{1/2}$ 추정 사례입니다. Loading dose 0.4 mg, maintenance 0.1–0.125 mg/day 같은 처방 문장은 교과서의 직접 권고가 아니라 `[교과서 외 통합 추론 예시]`로만 다룹니다. Sheiner 1977을 NONMEM의 직접 조상으로 단정하는 표현은 `[확인 필요]`입니다.

> 📖 **G&W PK35 Fig.35.1 [pp.641–642]; R&T Ch.18 Fig.18-13 [pp.605–606]**: Fig.35.1은 환자별 청소율 변동성이 농도-시간 거동과 어떻게 연결되는지를, Fig.18-13은 채혈 시점에 따라 $V$ vs $CL$ 추정 신뢰도가 왜 달라지는지를 보여 줍니다.

> **M4 체화 핵심**
> ① 농도와 prior가 모두 있을 때 → variance-weighted compromise가 posterior를 결정
> ② early sample vs late/steady-state sample → $V$와 $CL$ 식별가능성이 달라짐
> ⚡ posterior number = 개인 진실 → sampling geometry 무시로 placebo individualization

---

<!-- SLIDE_START: M5 | title: 질환/$RF$/$R_d$ 프레임워크: $f_e$와 환자 신기능을 분리하세요 -->

### 🃏 M5 — 질환/$RF$/$R_d$ 프레임워크: $f_e$와 환자 신기능을 분리하세요 [R&T pp.450–464]

> **앞 카드에서 이 카드로**
> M4가 개인 posterior의 해석 조건을 세웠으므로, 이제 질환과 신기능이 population parameter를 왜 벗어나게 만드는지 계산합니다.

> **거장의 시각**
> renal impairment라는 환자 라벨만 보고 maintenance dose를 줄이면 약물별 renal dependence를 놓칩니다. **$f_e$와 $RF$를 분리하면 같은 신부전이라도 dose 조정이 왜 달라지는지** 계산으로 보입니다.

> 🔑 **Drug × Patient 규칙**: $f_e$는 약물 속성, $RF$는 환자 속성입니다. 둘을 곱한 renal contribution이 maintenance 조정의 크기를 정합니다. $R_d$는 loading dose 공식이 아닙니다 — $V$가 변하지 않으면 LD는 별도 판단입니다.

**A. 형식적 정의와 핵심 구조**

**핵심**: renal impairment dosing은 "신장 나쁘니 줄인다"가 아닙니다. **약물 속성 $f_e$와 환자 속성 $RF$를 분리한 뒤, 그 조합으로 maintenance 요구량을 줄이는** 작업입니다.

$$
\underbrace{R_d}_{\text{유지용량 비율}}
=
\overbrace{\underbrace{RF}_{\text{신기능}}\cdot\underbrace{f_e}_{\text{renal 의존}}}^{\text{renal 기여}}
+
\underbrace{(1-f_e)}_{\text{비신 기여}}
$$

**파라미터 해부 표**

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $R_d$ | 비율 | maintenance requirement 비율 | $RF$ 감소, $f_e$ 크기 |
| $RF$ | 비율 | typical 대비 환자 신기능 | renal impairment, AKI/recovery |
| $f_e$ | 비율 | 미변화체 신장 배설분율 | drug property |
| $CL_{non\text{-}renal}$ | clearance | 비신장 제거 | hepatic/metabolic function |
| $CL_{total}$ | clearance | 기준 총 청소율 | population/covariate 차이 |

💡 **비유**: $R_d$는 두 개의 다이얼입니다. 하나는 약물이 원래 신장에 얼마나 의존하는지($f_e$), 다른 하나는 현재 환자 신장이 얼마나 남아 있는지($RF$)를 조절합니다.

- $f_e$ = 미변화체 배설분율; drug-specific.
- $RF$ = typical 대비 신기능; patient-specific.
- maintenance dose 또는 dosing rate는 $R_d$에 비례하여 조정합니다.

**임상 분류**

| 상황 | 파라미터 변화 | 임상 결과 | 조치 |
|---|---|---|---|
| $f_e \leq 0.30$ | renal contribution 작음 | renal function 감소가 maintenance exposure에 미치는 영향이 작을 수 있음 | major renal dose change보다 non-renal 경로 확인 |
| $RF \geq 0.70$ | typical 대비 renal function 보존 | 많은 경우 major regimen change가 필요하지 않음 | routine regimen 유지 여부 평가 |
| renal impairment + unchanged $V$ | $CL$ 변화가 LD를 직접 지배하지 않음 | LD 자동 감량은 부적절할 수 있음 | LD는 $V$ 기반으로 별도 판단; digoxin uremia처럼 $V$ 감소 예외 확인 [R&T p.464] |

**$R_d$ framework 결정 테이블**

| $f_e\times RF$ 영역 | 해석 | 모델링 함의 | 용량/TDM 지침 |
|---|---|---|---|
| $f_e\cdot RF$ < 0.1 | 신기능이 전체 제거에 미미한 기여 | $CL_{renal}$ 거의 무시; 간/대사 경로 파라미터에 집중 | 신기능 기반 maintenance 조절 불필요; 간기능 covariate 우선 탐색 |
| $f_e\cdot RF$ 0.1–0.5 | 신기능이 부분 기여 | $CL=CL_{non-renal}+f_e\cdot CL_{total}\cdot RF$로 분리; $RF$를 covariate로 탐색 | 신기능 저하 시 부분 maintenance 감량; TDM으로 개별화 필요 |
| $f_e\cdot RF$ > 0.5 | 신기능이 주요 제거 경로 | $CL$이 $RF$에 강하게 의존; 신기능 covariate가 $\omega^2$의 주요 설명 변수 | 유지 용량 적극적 감량; loading dose는 $V$ 기반으로 **별도** 결정; TDM 필수 |

$$
\underbrace{CL}_{\text{총 CL}}
=
\underbrace{CL_{non\text{-}renal}}_{\text{비신 CL}}
+
\overbrace{\underbrace{f_e}_{\text{renal 의존}}\cdot\underbrace{CL_{total}}_{\text{기준 CL}}\cdot\underbrace{RF}_{\text{신기능}}}^{\text{renal CL}}
$$

참고: $f_e$ = fraction excreted unchanged, $RF$ = patient CrCl / normal CrCl. 컬럼 4의 "loading dose는 $V$ 기반으로 별도 결정"은 §2.9 $V/CL$ 분리 원칙과 연결됩니다.

**간 질환 대조**: Cirrhosis에서는 high-extraction oral drug의 first-pass loss 감소와 portal bypass로 $F$가 증가할 수 있습니다. 반대로 low-extraction albumin-bound drug에서는 $f_u$ 증가가 total $CL$을 높일 수 있지만, unbound $CL$(단백결합 안 된 약물 기준 청소율)은 크게 변하지 않을 수 있습니다 [R&T pp.444–446].

**현장 팁**: **phenytoin**(albumin-bound, 저추출 항경련제)처럼 단백결합과 저추출이 결합된 약물에서는 $f_u\uparrow$가 total 농도 해석을 망칩니다. total target을 그대로 쓰면 같은 unbound exposure를 과소평가합니다. → 그래서 $f_e$와 $RF$만 분리해서는 부족하고, low-extraction + protein binding 맥락까지 같이 봐야 한다는 사례입니다.

> 📊 **개념 도식 (HTML 렌더링)**: $R_d$ 프레임워크 — 약물 속성 $f_e$ × 환자 속성 $RF$. 유지요법 조절은 약물이 신장 배설에 상당히 의존하고 환자의 신기능이 의미 있게 감소했을 때 커집니다.

> **M5 체화 핵심**
> ① renal-excreted drug에서 $RF$ 저하 → $f_e\times RF$ renal contribution이 maintenance 조정을 결정
> ② renal impairment but low $f_e$ → non-renal contribution이 지배
> ⚡ 신부전이면 모든 dose 감량 → LD/MD 혼동으로 초기 치료 실패 또는 과소투여

---

<!-- SLIDE_START: M6 | title: Cockcroft-Gault + creatinine lag -->

### 🃏 M6 — Cockcroft-Gault + creatinine lag [R&T pp.457–461]

> **앞 카드에서 이 카드로**
> M5가 $RF$를 renal dosing의 환자 축으로 세웠으므로, 이제 그 $RF$ 입력값이 얼마나 현재 신기능을 반영하는지 검토합니다.

> **거장의 시각**
> Cockcroft-Gault 값을 실시간 신기능으로 읽으면 AKI 초기에 과거 신기능을 현재값으로 오독합니다. SCr lag를 함께 보면 계산값의 정확성과 임상적 현재성이 분리됩니다.

> 💡 **SCr는 뒤늦은 거울** — AKI에서는 오늘의 SCr가 오늘의 RF가 아니라 이전 신기능의 흔적일 수 있습니다. C-G 값은 안정 상태에서 강하고, 급성 변화에서는 trend slope와 함께 해석합니다.

**A. 형식적 정의와 핵심 구조**

**핵심**: Cockcroft-Gault는 $RF$의 입력값을 만듭니다. 그러나 SCr는 실시간 신기능의 거울이 아닙니다 — **creatinine turnover가 반영된 지연 지표**이기 때문입니다.

$$
\underbrace{CL_{cr}}_{\text{CrCL 추정}}\;(\mathrm{mL/min})
=
\frac{\underbrace{(140-age)}_{\text{연령}}\cdot\underbrace{WT}_{\text{체중}}}{\underbrace{72\cdot SCr}_{\text{SCr 보정}}}
$$

**파라미터 해부 표**

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $CL_{cr}$ | mL/min | creatinine clearance 추정값 | age, WT, SCr |
| age | year | 신기능 추정의 연령 항 | aging, frailty |
| WT | kg | body size proxy | obesity, sarcopenia, edema |
| SCr | mg/dL | creatinine 농도 | muscle mass, AKI lag, renal function |

여성에서는 일반적으로 0.85를 곱합니다. 이 식은 adult, stable renal function, body size 해석을 전제로 합니다 [R&T p.457].

**AKI 주의사항**: Acute renal failure에서는 SCr 상승이 신기능 감소보다 늦습니다. R&T Table 15-6은 renal function이 낮을수록 creatinine turnover time과 half-life가 길어짐을 보여줍니다 [R&T pp.459–461]. **오늘 측정한 SCr로 오늘의 RF를 과신하면 초기 24–48시간 동안 독성 축적을 놓칠 수 있습니다.**

**현장 팁**: C-G는 snapshot 계산이 아니라 trend 해석과 함께 써야 합니다. 특히 노인, 근감소, 비만, AKI에서는 체중 선택과 SCr lag가 dose error의 주된 원인입니다.

> **M6 체화 핵심**
> ① stable renal function adult → Cockcroft-Gault가 $RF$ 입력값을 결정
> ② AKI 또는 급성 변화 → creatinine turnover lag가 지배
> ⚡ 오늘 SCr = 오늘 RF → 첫 24–48시간 nephrotoxic accumulation 예측 실패

---

<!-- SLIDE_START: M7 | title: 혈액투석 좌표 평면: $V_u$와 $CL_u$를 함께 보세요 -->

### 🃏 M7 — 혈액투석 좌표 평면: $V_u$와 $CL_u$를 함께 보세요 [R&T pp.466–474]

> **앞 카드에서 이 카드로**
> M6가 신기능 숫자의 시간 지연을 보였으므로, 이제 intermittent dialysis처럼 제거 과정 자체가 시간 구간으로 바뀌는 상황을 봅니다.

> **거장의 시각**
> 투석 중 half-life가 짧아졌다는 사실만으로 보충 용량을 결정하면 high-$V_u$ 약물을 과보충할 수 있습니다. **$V_u$, $CL_u$, $CL_{uD}$ 좌표를 함께 보면 실제 session 동안 빠진 body amount가 보입니다.**

> 💡 **세션 제거량 관점** — 투석 결정의 endpoint는 반감기 단축이 아니라 session 동안 빠진 body amount입니다. $V_u$가 크면 투석 clearance가 커도 체내 총량에서 빠지는 비율은 작을 수 있습니다.

**A. 형식적 정의와 핵심 구조**

**핵심**: hemodialysis 보충 용량은 "half-life가 줄었는가"만으로 결정하지 않습니다. **dialysis session 동안 body amount가 의미 있게 빠졌는지**가 핵심입니다.

**확정된 수정**

```text
삭제: Vu < 120 L AND CLu < CLuD이면 보충 용량 필요.
채택: Vu·CLu 평면에서 dialysis effectiveness를 읽는다.
```

R&T Fig.15-18은 high-flux 3시간 dialysis에서 unbound $V$가 약 120 L보다 크거나, 환자 own unbound clearance가 dialysis clearance보다 훨씬 크면 dialysis가 제거하는 fraction이 20% 미만으로 작아질 수 있음을 보여 줍니다 [R&T pp.471–472]. 따라서 이는 hard AND gate가 아니라 continuous trade-off입니다.

**핵심 수식 — 개념 수준**

- 투석 중: $k_D = (CL_u + CL_{uD})/V_u$
- 세션 동안 제거된 분율: $1 − \exp(−k_D\cdot T)$
- Dialysis 기여도: $CL_{uD}/(CL_u + CL_{uD})$
- 보충 용량은 dialysis 후 amount를 dialysis 없이 예상된 amount로 복원하는 양으로 검토합니다 [R&T pp.471–474].

$$
\underbrace{k_D}_{\text{투석 중 제거}}
=
\frac{\overbrace{\underbrace{CL_u}_{\text{자체 CL}}+\underbrace{CL_{uD}}_{\text{투석 CL}}}^{\text{총 unbound CL}}}{\underbrace{V_u}_{\text{unbound V}}},
\qquad
\underbrace{1-\exp(-k_D\cdot T)}_{\text{session 제거율}},
\qquad
\underbrace{\frac{CL_{uD}}{CL_u+CL_{uD}}}_{\text{투석 기여}}
$$

**파라미터 해부 표**

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $k_D$ | 시간⁻¹ | 투석 중 전체 제거 속도상수 | $CL_u$, $CL_{uD}$, $V_u$ |
| $CL_u$ | clearance | 환자 자체 unbound clearance | residual renal/nonrenal function |
| $CL_{uD}$ | clearance | dialysis unbound clearance | membrane, flow, modality |
| $V_u$ | L | unbound 기준 분포용적 | tissue binding, distribution |
| $T$ | 시간 | dialysis session duration | session prescription |

💡 **비유**: 투석은 수영장에서 물을 퍼내는 펌프입니다. 펌프 성능($CL_{uD}$)이 좋아도 수영장($V_u$)이 너무 크면 3시간 동안 수위는 조금만 내려갑니다.

**CAPD 대조**: CAPD clearance는 대부분의 약물에서 혈액투석 clearance보다 낮습니다. 따라서 '투석 환자'라는 단일 라벨로 용량 규칙을 하나로 묶을 수 없습니다 [R&T pp.475–477].

**현장 팁**: **phenobarbital**(고용량 진정·항경련제)은 투석 중 half-life가 크게 줄어도 single 3시간 session에서 body amount가 충분히 빠지지 않을 수 있습니다. → 반감기 단축과 세션 중 제거된 약물량은 같은 endpoint가 아니라는 사례입니다.

> 📖 **R&T Ch.15 Fig.15-18 [p.471], Fig.15-19 [p.473]**: Fig.15-18은 투석 제거가 hard threshold가 아니라 $V_u$와 $CL_u$의 연속 함수임을, Fig.15-19는 투석 중 제거량을 보충 용량 개념과 연결합니다.

> **M7 체화 핵심**
> ① dialysis session 중 약물 제거 → $V_u$, $CL_u$, $CL_{uD}$ 좌표가 결정
> ② half-life 단축 vs body amount 제거 → 보충 용량 판단 endpoint가 다름
> ⚡ 혈액투석 = 자동 보충 → high-$V_u$ 약물에서 불필요한 추가 용량과 독성 위험

---

<!-- SLIDE_START: M8 | title: 목표농도전략 기준(Target Concentration Strategy criteria) -->

### 🃏 M8 — 목표농도전략 기준(Target Concentration Strategy criteria) [R&T pp.594–597]

> **앞 카드에서 이 카드로**
> M7까지 환자별 제거와 보충의 조건을 분리했으므로, 이제 농도 monitoring이 실제 처방 결정을 바꾸는 조건을 따집니다.

> **거장의 시각**
> TCS 후보 약물이라는 이름만으로 monitoring을 시작하면 decision을 바꾸지 못하는 placebo monitoring이 됩니다. **5 criteria를 sequential filter로 읽으면** 농도값이 처방 결정을 바꿀 수 있는 조건이 분리됩니다.

> 🔑 **Sequential filter 규칙**: TCS 5 criteria는 병렬 checklist가 아닙니다. 하나라도 막히면 decision value가 줄어드는 순차 관문입니다. measured concentration은 dosing history와 sampling time 없이는 decision object가 아닙니다.

**A. 형식적 정의와 핵심 구조**

**핵심**: TCS는 특정 약물명에 자동 적용되는 필수 전략이 아닙니다. 핵심은 "농도를 잴 수 있는가"가 아니라 **그 농도가 다음 임상 결정을 바꿀 만큼 제때·정확하게 해석되는가**입니다. 기준이 대부분 충족될 때 치료 시작·모니터링 단계의 보조 전략(adjunct strategy)이 됩니다.

**기준 잠금**

1. Concentration-response relationship이 충분히 좋아야 합니다.
2. Therapeutic failure 가능성이 높아야 합니다: low therapeutic index, large PK variability, 유전·질환·상호작용 위험, nonadherence/erratic absorption 가능성.
3. Population PK information이 있어야 합니다.
4. Reliable assay가 가능해야 합니다.
5. Assay turnaround가 다음 therapeutic decision 전에 도착해야 합니다.

**Table 18-5 잠금**: **cyclosporine**(면역억제제), **digoxin**(강심배당체), **gentamicin**(아미노글리코사이드 항생제), **nortriptyline**(삼환계 항우울제), **phenytoin**(항경련제), **theophylline**(기관지확장제)은 TCS가 임상적으로 도움이 되어 온 대표 후보군입니다. → 약물명만으로 TCS가 필수라는 뜻은 아니라는 사례입니다 [R&T pp.595–596].

**Table 18-6 해석 관문**: Measured concentration 하나만으로는 해석이 끝나지 않습니다. 완전한 해석에는 dosing history, sampling time, previous concentrations, clinical status, renal/hepatic lab data, protein binding, concurrent drugs, assay method, usual PK parameters가 모두 필요합니다 [R&T p.597].

**페니토인 잠금**: **phenytoin**은 saturable metabolism과 altered protein binding의 영향을 받아 monitoring 정당성이 강합니다 [R&T pp.588, 595–596]. 그러나 uremia, surgery, displacement drugs에서는 total target을 unbound target에 맞추도록 조정해야 합니다 [R&T p.596].

**현장 팁**: TCS의 5 criteria는 checklist가 아니라 sequential filter입니다. 하나가 실패하면 measured number가 있어도 임상 의사결정에 도움이 되지 않을 수 있습니다.

> **M8 체화 핵심**
> ① 농도가 다음 dose 결정을 바꿀 수 있을 때 → TCS criteria가 결정
> ② assay turnaround가 늦거나 history가 불완전할 때 → monitoring value가 감소
> ⚡ TCS 후보 약물 = routine monitoring → placebo monitoring과 부주의한 인용 위험

---

<!-- SLIDE_START: M9 | title: Loading dose vs maintenance dose -->

### 🃏 M9 — Loading dose vs maintenance dose [R&T pp.582, pp.584–586]

> **앞 카드에서 이 카드로**
> M8이 monitoring의 의사결정 조건을 세웠으므로, 이제 target concentration을 어느 dose component에 반영할지 분리합니다.

> **거장의 시각**
> 신기능 저하를 LD와 MD에 같은 방식으로 적용하면 초기 치료 실패와 장기 독성이 동시에 생길 수 있습니다. **LD는 $V$, MD는 $CL$이라는 분리를 고정하면** 어떤 dose component를 바꿀지 즉시 결정됩니다.

> 💡 **채우기와 유지의 분리** — LD는 목표 수위까지 채우는 문제, MD는 새는 양을 계속 보충하는 문제입니다. 신부전이라는 라벨만으로 LD를 줄이면 초기 target concentration을 놓칠 수 있습니다.

**A. 형식적 정의와 핵심 구조**

**핵심**: loading dose와 maintenance dose는 서로 다른 parameter가 지배합니다. TCS가 target concentration을 정해 주더라도 **어떤 dose component를 바꿀지는 $V$와 $CL$을 분리해서 결정**해야 합니다. LD는 $V$와 target concentration의 문제, MD는 $CL$과 target average exposure의 문제입니다.

$$
\underbrace{D_L}_{\text{loading dose}}
=
\frac{\underbrace{V}_{\text{분포 공간}}\cdot\underbrace{C_{target}}_{\text{목표 농도}}}{\underbrace{F}_{\text{이용률}}}
$$

**파라미터 해부 표**

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $D_L$ | dose | loading dose | $V$, $C_{target}$, $F$ |
| $D_M$ | dose/interval | maintenance dose | $CL$, $C_{target}$, $\tau$, $F$ |
| $V$ | L | target 농도 달성에 필요한 분포 공간 | body size, tissue distribution, disease |
| $CL$ | L/time | 반복 투여에서 빠져나가는 제거 능력 | renal/hepatic function, interaction |
| $F$ | 비율 | bioavailability | formulation, first-pass, disease |

💡 **비유**: LD는 빈 욕조를 목표 수위까지 한 번 채우는 일, MD는 배수구로 빠지는 만큼 계속 보충하는 일입니다.

**Fig.18-5 수정 잠금**: Step 1의 "$V$ 90% 설명" 또는 "$V$ 5–10% 정확도" 표현은 삭제합니다. 이 표현들은 Fig.18-5의 의미를 prediction accuracy로 잘못 읽게 합니다. R&T Fig.18-5의 variability partition은 대략 다음을 보여 줍니다 — **$V$는 body weight 25% + age 10% + renal function 10%로 약 45% explained, 55% unaccounted; hepatic $CL$은 약 40% explained, 60% unaccounted; renal $CL$은 renal function 50% + body weight 15% + age 15%로 약 80% explained; $F$는 약 5%만 explained** [R&T p.582].

**임상적 함의**

| 상황 | 파라미터 변화 | 임상 결과 | 조치 |
|---|---|---|---|
| Renal-clearance dominant drug | $RF$가 $CL$을 강하게 설명 | maintenance exposure 예측 가능성 증가 | $RF/R_d$ 기반 MD 조정 |
| Hepatic-clearance dominant drug | demographic covariate만으로 설명되지 않는 IIV 큼 | 개인 노출 불확실성 증가 | TCS criteria 충족 시 monitoring 고려 |
| Theoretical LD가 매우 큰 경우 | $V\cdot C_{target}$ 요구량 큼 | 단회 투여 독성·투여 가능성 문제 | distribution kinetics, 투여속도, formulation, dose strength, 독성 위험을 고려해 divided loading 검토 |

**현장 팁**: "신부전이므로 LD도 줄인다"는 자동 규칙은 틀릴 수 있습니다. LD는 $V$ 문제, MD는 $CL$ 문제입니다. 단, **digoxin** uremia처럼 $V$ 자체가 변하는 예외는 따로 잡습니다.

> 📖 **R&T Ch.18 Fig.18-5 [p.582]**: 이 그림은 $V/CL$ 예측 정확도를 잘못 읽는 오류를 바로잡는 데 핵심입니다. 용량 정확도(dosing precision)를 약속하는 그림이 아니라 변동성 분할(variability partition)입니다.

> **M9 체화 핵심**
> ① 초기 target concentration 달성 → $V$와 $C_{target}$이 LD를 결정
> ② 장기 평균 노출 유지 → $CL$, $RF$, $R_d$가 MD를 결정
> ⚡ 신부전이라 LD도 감량 → 초기 치료 농도 미달과 내성 선택 압력 위험

---

<!-- SLIDE_START: M10 | title: Missed / unequal / erratic dosing framework -->

### 🃏 M10 — Missed / unequal / erratic dosing framework [R&T pp.600–605]

> **앞 카드에서 이 카드로**
> M9가 LD와 MD의 지배 파라미터를 분리했으므로, 이제 실제 투약 간격이 깨졌을 때 농도 해석을 복원합니다.

> **거장의 시각**
> missed dose와 unequal interval을 자료 오염으로 처리하면 실제 투약 이력이 만든 농도 기여를 IIV로 흡수합니다. **superposition으로 읽으면** 불규칙 투약도 이전 dose들의 잔여 기여 합산 문제로 바뀝니다.

> 🔑 **Superposition 규칙**: irregular dosing은 이전 dose들의 남은 기여를 더하고 빼는 문제입니다. dose history를 모르면 TDM 농도는 해석 가능한 농도가 아니라 문맥 없는 숫자입니다.

**A. 형식적 정의와 핵심 구조**

**핵심**: nonadherence, unequal interval, erratic ICU dosing은 TDM 해석을 망치는 예외가 아닙니다. **superposition**(각 용량의 남은 농도 기여를 더하는 원리)으로 정량화할 수 있는 일반 상황입니다.

**세 가지 시나리오**

| 시나리오 | 수식 | 확정된 활용 |
|---|---|---|
| 한 번의 missed dose | Eq.18-1 | 예상 정상상태 농도에서 missed dose의 잔여 기여를 뺍니다. |
| 연속된 두 번의 missed doses | Eq.18-2 | 두 missed doses의 기여를 뺍니다. |
| 9-13-17-21 institutional regimen | Eq.18-3 | 일중 간격이 unequal한 24시간 반복 cycle. |
| Dose와 interval 모두 unequal | Eq.18-4 | 이전 dose들의 잔여량을 합산; 환자 $4\times t_{1/2}$ 이전 dose는 무시 가능. |

💡 **비유**: superposition은 방 안에 남아 있는 향수 냄새를 더하는 것과 같습니다. 새로 뿌린 향만 보지 않고 이전에 뿌린 향이 얼마나 남았는지를 모두 합산합니다.

**유지된 풀이 예제**

- **Digoxin** (강심배당체): typical patient가 0.25 mg daily dose를 두 번 missed한 경우, expected 농도 0.39 µg/L. therapeutic range 0.8–2.0 µg/L보다 낮습니다 [R&T p.602].
- **Vancomycin 9-13-17-21** (글리코펩타이드 항생제): 20 kg, 5세 환아, $V$ 14 L, $CL$ 3.3 L/h, $k$ 0.24 h⁻¹, 250 mg regimen은 8:00 농도 2.03 mg/L를 만듭니다. therapeutic 5–15 mg/L보다 낮습니다 [R&T pp.602–603].
- **Erratic vancomycin**: 68 kg, 60세 남성, SCr 2.2 mg/dL, $CL_{cr}$ 34 mL/min, $V$ 42.2 L, $k$ 0.049 h⁻¹; observed 34 mg/L vs predicted 33.7 mg/L. → kinetics는 일관되지만 dose가 너무 높음을 보여주는 사례입니다 [R&T p.604].

**삭제된 주장**: "TDM 환자의 80%"는 source-backed 표현이 아니므로 삭제합니다.

**현장 팁**: adherence phantom을 IIV로 흡수하지 마세요. dosing history와 sampling time은 사무적 디테일이 아니라 model input입니다.

$$
\underbrace{\frac{t_{1/2}}{\tau}}_{\text{시간 여유}}
\times
\underbrace{\text{therapeutic window}}_{\text{농도 여유}}
\Rightarrow
\underbrace{\text{forgiving/unforgiving regimen}}_{\text{missed-dose 내성}}
$$

**파라미터 해부 표**

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $t_{1/2}/\tau$ | 비율 | missed-dose 시간 여유 | half-life, dosing interval |
| therapeutic window | 농도 범위 | 농도 허용 여유 | efficacy/toxicity boundary |
| superposition term | 농도 기여 | 이전 dose의 남은 영향 | dose amount, interval, $k$ |
| $k$ | 시간⁻¹ | elimination rate constant | $CL/V$ |

**§2 recap**: Ch.6이 model 후보를 만들고, Ch.15가 patient-specific parameter deviation을 설명하며, PK35가 posterior parameter를 추정하고, Ch.18이 그 추정을 dosing and monitoring decision으로 변환합니다.

> **M10 체화 핵심**
> ① missed/unequal dosing 이후 농도 해석 → superposition이 결정
> ② forgiving vs unforgiving regimen → $t_{1/2}/\tau$와 therapeutic window가 지배
> ⚡ 불규칙 투약 = 자료 오염 → adherence phantom을 IIV로 흡수해 TDM 해석 실패


<!-- SLIDE_START: §5 | title: 혼동 쌍 해부 -->

# §5 — 혼동 쌍 해부 (Confusion Pair Dissection)

> 🎯 Confusion pair는 시험용 암기가 아니라 실무 오류 차단 장치입니다 — $C_e/R/RC$, $RF/f_e$, $V/CL$, sampling confidence를 끝까지 분리하세요.

## §5.1 — 효과구획(effect compartment) vs turnover

| 비교 기준 | 개념 A: Effect compartment | 개념 B: Turnover |
|---|---|---|
| 단위 / 차원 | $C_e$: 농도; $k_{e0}$: 시간⁻¹ | $R$: response 단위; $k_{in}$: response/time; $k_{out}$: 시간⁻¹ |
| 수식 내 위치 | $dC_e/dt=k_{e0}(C-C_e)$의 link state | $dR/dt=k_{in}\cdot I(C)-k_{out}R$ 또는 loss modulation state |
| 변화 원인 | plasma–effect site equilibration delay | production/loss process, baseline, rebound, adaptation |
| 혼동 시 임상 결과 | delay를 모두 turnover로 과해석 | response system 변화를 link model로 축소해 model candidate 누락 |

**한 줄 요약**: Effect compartment는 response site equilibration delay, turnover는 response system의 input/output rate가 drug에 의해 변하는 것입니다 [G&W pp.425–426].

> **⚡ 기억 고리 — *분포 지연 vs 시스템 지연***
> Effect compartment는 약이 plasma에서 effect site로 **이동하는 데 걸리는 시간**이 지연 원인입니다. Turnover는 약이 effect site에 도달했지만 **response system 자체가 바뀌는 데 걸리는 시간**이 지연 원인입니다. 진단 단서 — dose-dependent peak shift가 보이면 turnover, 안 보이면 effect compartment 가능성이 높습니다.

## §5.2 — 좌측 이동 vs 우측 이동 (Peak movement)

| 비교 기준 | 개념 A: 좌측 trough shift | 개념 B: 우측 trough shift + flat high-dose portion |
|---|---|---|
| 단위 / 차원 | 시간축 극값이 earlier로 이동 | 시간축 극값이 later로 이동하고 high-dose flat portion 동반 |
| 수식 내 위치 | turnover loss stimulation 또는 receptor on/off 후보 | input inhibition with saturation 후보 |
| 변화 원인 | finite receptor pool, loss process stimulation 등 | saturation을 동반한 input inhibition |
| 혼동 시 임상 결과 | "무조건 receptor on/off"로 과잉 확정 | absorption delay로 오독해 mechanism 후보 누락 |

**한 줄 요약**: 방향은 확정 규칙이 아니라 competing models를 줄이는 신호입니다 [G&W pp.424–428].

> **⚡ 기억 고리 — *방향은 단서이지 결론이 아니다***
> Peak 이동 방향은 메커니즘을 구분하는 **1차 필터**이지 최종 판단이 아닙니다. 방향을 보고 가설 목록을 좁힌 뒤 추가 데이터로 하나씩 제거하는 방식이 맞습니다.

## §5.3 — Bayesian "no concentration" vs "no prior"

| 비교 기준 | 개념 A: 농도 없음 | 개념 B: Prior 없음 |
|---|---|---|
| 단위 / 차원 | population average가 추정값을 지배 | concentration-only maximum likelihood에 가까움 |
| 수식 내 위치 | objective의 prior penalty가 상대적으로 지배 | concentration mismatch term이 상대적으로 지배 |
| 변화 원인 | 개인 관측 정보 부재 | sparse/mistimed concentration 또는 weak prior |
| 혼동 시 임상 결과 | 환자 특이 deviation을 놓침 | 생리학적으로 불가능한 $V/CL$ 생성 가능 |

**한 줄 요약**: Bayesian TDM의 핵심 역량은 posterior number를 믿는 것이 아니라, **그 농도가 어떤 parameter를 식별할 수 있는 시점에 얻어졌는지를 판단**하는 것입니다 [G&W pp.641–643; R&T pp.597, 605–606].

> **⚡ 기억 고리 — *데이터 없음 vs 사전 지식 없음***
> 좋은 Bayesian TDM은 prior의 강도와 likelihood의 강도를 동시에 평가하고 어느 쪽이 지배하는지 인식하는 것입니다.

## §5.4 — 간 고추출 약물 vs 신장 배설 약물

| 비교 기준 | 개념 A: 간 고추출/단백결합 맥락 | 개념 B: 신장 배설 미변화 약물 |
|---|---|---|
| 단위 / 차원 | $F$, extraction ratio, $f_u$, unbound $CL$ | $RF$, $f_e$, renal $CL$ component |
| 수식 내 위치 | oral exposure에서 $F$ 증가와 $CL$ 변화가 노출을 지배 | $R_d=RF\cdot f_e+(1-f_e)$의 renal contribution |
| 변화 원인 | cirrhosis, portal bypass, hypoalbuminemia, displacement | renal impairment, residual renal function |
| 혼동 시 임상 결과 | "간 질환 = 모든 CL 감소"로 total/unbound 해석 오류 | drug/patient 속성 혼동으로 maintenance dose 오류 |

**한 줄 요약**: 간 질환이 있다고 해서 $CL$이 모두 감소하지는 않습니다. extraction ratio, $F$, 단백결합, unbound $CL$이 변화 방향을 정합니다 [R&T pp.444–446].

> **⚡ 기억 고리 — *간 질환 = CL 감소?의 함정***
> High-extraction 경구 약물에서 간경변은 $F$를 올리고 $CL$을 낮춰 노출을 급격히 올립니다. Low-extraction albumin-bound 약물에서는 total target의 재해석이 필요할 수 있습니다.

## §5.5 — Loading dose vs maintenance dose

| 비교 기준 | 개념 A: Loading dose | 개념 B: Maintenance dose |
|---|---|---|
| 단위 / 차원 | dose; $V\times C_{target}/F$ | dose rate; $CL\times C_{target}\times\tau/F$ |
| 수식 내 위치 | $V$와 target concentration이 분자에서 지배 | $CL$, $RF$, $R_d$가 반복 노출을 지배 |
| 변화 원인 | body size, tissue distribution, $V$ 변화 | renal/hepatic function, interaction, disease |
| 혼동 시 임상 결과 | 신부전만으로 LD를 줄여 초기 농도 미달 | 장기 dosing에 $V$ 논리를 적용해 accumulation/underdosing |

**Fig.18-5 수정된 진술**: Fig.18-5의 schematic variability partition에서 $V$ 약 45%, hepatic $CL$ 약 40%, renal $CL$ 약 80%, $F$ 약 5%가 covariate로 설명됩니다. 이는 loading-dose의 정확도(accuracy) 값이 아닙니다 [R&T p.582].

> **⚡ 기억 고리 — *욕조 채우기 vs 욕조 유지하기***
> Loading dose는 **욕조를 목표 수위까지 채우는** 일회성 작업, Maintenance dose는 **수위 유지를 위해 배수구로 빠지는 만큼 채우는** 반복 작업입니다. 신부전이 있어도 $V$가 변하지 않으면 LD를 줄일 이유가 없습니다.

## §5.6 — 채혈 식별가능성 vs point estimate confidence

| 비교 기준 | 개념 A: 채혈 식별가능성 | 개념 B: point estimate confidence |
|---|---|---|
| 단위 / 차원 | sampling geometry; $t/t_{1/2}$, trough/steady-state 위치 | posterior mean, RSE, shrinkage 등 추정 출력 |
| 수식 내 위치 | early sample은 $V$-information, late/steady-state sample은 $CL$-information | 같은 likelihood를 갖는 여러 $(V,CL)$ 조합 위의 점 추정 |
| 변화 원인 | sampling time, dose history, assay timing | prior strength, sparse data, model covariance |
| 혼동 시 임상 결과 | $CL$ collapse를 개인 clearance로 오독 | 식별 불가 posterior로 individual dosing 결정 |

**한 줄 요약**: Bayesian posterior의 신뢰는 number 자체가 아니라 **그 number가 sampling geometry 위에서 식별 가능한가**에 달려 있습니다 [G&W pp.641–643; R&T pp.605–606].

> **⚡ 기억 고리 — *지도가 식별 가능한 영역에 있는가***
> $1\times t_{1/2}$ 이전 샘플들은 $V$는 잘 추정하지만 $CL$은 population prior로 collapse합니다. TDM 농도는 **그 농도가 $CL$을 실제로 추정한 것인지** 먼저 물어야 의미가 있습니다.

> **실패 모드**
> NONMEM 진단에서 η-shrinkage on $CL$ > 30%이면서 $V$는 < 15%, 그리고 RSE($CL$) > 50%인데 fit은 통과한다면, 이는 거의 **"sampling time mismatch"의 신호**입니다.

**§5 recap**: 대부분의 오류는 하나의 관찰값을 하나의 원인으로 고정할 때 발생합니다. 이 세션의 판단 단위는 단일 수치가 아니라 **shape, covariate, dose history, sampling time의 joint interpretation**입니다.


<!-- SLIDE_START: §7 | title: 자기 테스트 -->

# §7 — 자기 테스트: 능동 회상 모듈 (Self-Test: Active Recall Module)

> 🎯 Self-test는 답 확인이 아니라 판단 사슬의 누수 검사입니다 — shape, posterior, renal dosing, LD/MD를 스스로 연결해 보세요.

---

## Q1
Response-time curve에서 baseline, time-delay, peak-shift, saturation/slope를 왜 같은 순서로 읽어야 합니까?

**정답**: baseline이 drift하거나 adaptation/rebound가 있으면 direct model 해석이 먼저 깨집니다. time-delay와 peak-shift는 effect-site delay, turnover, receptor on/off 후보를 구분하는 신호이고, saturation/slope는 high-dose에서 비선형 process를 드러냅니다 [G&W pp.423–424].

## Q2
Case B leftward peak-shift를 "모델 클래스 확정"으로 쓰면 왜 위험한가?

**정답**: leftward shift는 turnover loss stimulation이나 receptor on/off 등 복수 후보를 남기는 진단 신호입니다. 원문은 potential models를 평가하라고 제시하지, 방향만으로 model을 확정하라고 하지 않습니다 [G&W pp.424–428].

## Q3
Effect compartment와 turnover model의 가장 짧은 구분법은?

**정답**: Effect compartment는 농도가 effect site로 늦게 equilibration되는 delay이고, turnover는 response variable의 production/loss rate 자체가 drug에 의해 변하는 delay입니다 [G&W pp.425–426].

## Q4
Bayesian TDM에서 농도가 없을 때와 prior가 없을 때의 극단은 어떻게 다른가?

**정답**: 농도가 없으면 population average가 추정값이 되고, prior가 없으면 concentration-only maximum likelihood에 가까워집니다. Sparse concentration + weak prior는 생리학적으로 불가능한 $V/CL$을 만들 수 있습니다 [G&W pp.641–643].

## Q5
PK35 digoxin case에서 반드시 보존해야 할 수치 앵커는?

**정답**: 55세 60 kg CHF 남성, Lanoxicap 0.2 mg daily, 458 h 2.5 µg/L, 479 h 0.9 µg/L, $CL_{pop}$ 1.8 L/h, $V_{pop}$ 500 L, 추정 $CL$ 5.7 L/h, $V$ 119.6 L, $t_{1/2}$ 14.5 h [G&W pp.641–643].

## Q6
$R_d=RF\cdot f_e+(1-f_e)$에서 $f_e$와 $RF$를 분리해야 하는 이유는?

$$
\underbrace{R_d}_{\text{유지용량 비율}}
=
\overbrace{\underbrace{RF}_{\text{신기능}}\cdot\underbrace{f_e}_{\text{renal 의존}}}^{\text{renal 기여}}
+
\underbrace{(1-f_e)}_{\text{비신 기여}}
$$

**정답**: $f_e$는 drug property, $RF$는 patient property입니다. 둘을 분리해야 renal impairment가 maintenance exposure에 미치는 영향을 정량화할 수 있습니다 [R&T pp.450–453].

## Q7
AKI에서 Cockcroft-Gault를 그대로 적용하면 왜 위험한가?

**정답**: SCr는 신기능의 즉시값이 아니라 creatinine turnover가 반영된 지연값입니다. 급성 변화에서는 실제 $RF$가 SCr 기반 추정보다 더 낮을 수 있습니다 [R&T pp.459–461].

## Q8
Hemodialysis에서 half-life가 크게 줄면 보충 용량이 항상 필요한가?

**정답**: 아닙니다. **dialysis session 동안 실제 body amount가 얼마나 제거되었는지**가 중요합니다. $V_u$가 크거나 $CL_u$가 $CL_{uD}$보다 훨씬 크면 single session의 fraction removed는 작을 수 있습니다 [R&T pp.471–472].

## Q9
TCS 후보 약물이면 항상 농도 모니터링을 해야 하는가?

**정답**: 아닙니다. concentration-response가 양호하고, therapeutic failure 가능성이 높으며, population PK 정보가 있고, reliable assay가 가능하고, decision 전에 도착하는 turnaround time이 대부분 충족되어야 routine strategy가 됩니다 [R&T pp.594–597].

## Q10
**phenytoin**에서 total concentration target을 그대로 해석하면 왜 틀릴 수 있는가?

**정답**: phenytoin은 albumin binding과 saturable metabolism이 중요합니다. Uremia, surgery, displacement drugs에서 단백결합 변화가 예상되면 same unbound therapeutic concentration을 맞추도록 total target을 조정해야 합니다 [R&T pp.588, 595–596].

## Q11
Loading dose와 maintenance dose를 한 문장으로 구분하라.

**정답**: LD는 $V$와 target concentration의 문제이고, MD는 $CL$과 target average exposure의 문제입니다 [R&T pp.584–586].

## Q12
Fig.18-5를 "V는 정확히 예측 가능하다"로 읽으면 왜 틀린가?

**정답**: Fig.18-5는 variability partition입니다. $V$는 약 45% explained, 55% unaccounted, hepatic $CL$은 약 40%, renal $CL$은 약 80% explained로 제시됩니다. 이는 prediction accuracy 값이 아닙니다 [R&T p.582].

## Q13
Vancomycin 9-13-17-21 regimen 예제가 가르치는 핵심은?

**정답**: 24시간 total daily dose가 같아도 unequal intra-day interval은 trough를 크게 낮출 수 있습니다. 예제에서 250 mg 9-13-17-21 regimen은 8:00 농도 2.03 mg/L로 therapeutic range 5–15 mg/L보다 낮습니다 [R&T pp.602–603].

## Q14
PK35 digoxin 처방 권고를 source-locked 답으로 쓰면 안 되는 이유는?

**정답**: PK35는 Bayesian $CL/V/t_{1/2}$ 추정 사례이지 loading 0.4 mg 또는 maintenance 0.1–0.125 mg/day를 직접 권고하는 처방 문서가 아닙니다. 그런 답은 `[교과서 외 통합 추론 예시]`로만 제시해야 합니다 [G&W pp.641–643].

## ⚡ 보스 딜레마 ★★

## Q15  *(트레이드오프 / 보스 딜레마 — ★★ SR)*
Hepatic-$CL$ dominant 약물 X로 maintenance 단계에 있는 환자가 있습니다. R&T Fig.18-5에 따르면 hepatic $CL$은 demographic covariate로 약 40%만 설명됩니다. TCS 5 criteria 중 "concentration-response 양호"는 충족되지만, "decision 전 도착하는 turnaround time"이 marginal입니다. 이 환자에게 routine TDM을 도입할지, demographic 기반 표준 regimen으로 갈지 어느 쪽을 택하고 어떻게 방어하겠습니까?

**정답**: 정답은 양자택일이 아닙니다. **두 trade-off를 명시적으로 분리해 인식**하는 것이 핵심입니다.
- **Demographic-only로 갈 경우의 비용**: hepatic $CL$의 60% IIV가 covariate로 설명되지 않아 individual exposure가 target에서 ±50% 이상 벗어날 수 있습니다. 그러나 sampling/assay/turnaround 운영 risk는 0입니다.
- **Routine TDM으로 갈 경우의 비용**: 60% IIV를 individualize할 수 있습니다. 그러나 turnaround이 marginal이라면 도착한 농도가 다음 dose 결정 시점을 *지나서* 와서, 측정값은 있지만 의사결정 input은 아닌 상태가 됩니다.
- **마스터 모델러의 선택**: TCS criterion이 *대부분* 충족되므로 도입 *후보*는 맞습니다. 그러나 turnaround marginal을 운영적으로 해결할 방법(샘플링 시점 조정, lab cutoff 협의)이 없으면 TDM은 데이터만 쌓고 결정을 못 바꾸는 *placebo monitoring*이 됩니다. 따라서 운영 조건이 fix되기 전까지는 demographic-based regimen + clinical response monitoring으로 가되, "이 약물이 hepatic-$CL$ dominant이고 demographic으로 60%가 설명되지 않아 IIV outlier가 발생할 수 있다"는 점을 명시 보고합니다. 운영 조건이 fix되면 즉시 TCS로 전환합니다 [R&T pp.582, 594–597].

## Q16  *(NONMEM 신호 해독)*
Vancomycin PopPK fit에서 η-shrinkage on $CL$ > 30%, $V$는 < 15%, COV step은 통과했지만 RSE($CL$) > 50%입니다. 데이터셋은 ICU 첫 24h dense sampling으로 구성되어 있습니다. 이 결과는 무엇을 말합니까?

**정답**: "fit은 통과했지만 데이터가 식별할 수 없던 quantity를 추정하려 했다"는 신호입니다. $1\times t_{1/2}$ 이전 sample에서는 $CL\times 1/3$과 $V\times 3$이 거의 같은 likelihood를 가지므로, NONMEM은 $V$는 잘 잡고 $CL$은 population mean으로 collapse합니다. 해결 — $V$를 population strong prior로 고정하고 $CL$만 individualize하거나, $\geq 4\times t_{1/2}$ post-infusion sample을 추가합니다 [R&T pp.605–606].

$$
\underbrace{CL\times\frac{1}{3}}_{\text{낮은 CL}}
\;\approx_{\text{early sample 구분 불가}}\;
\underbrace{V\times3}_{\text{큰 V}},
\qquad
\underbrace{t\geq4\times t_{1/2}}_{\text{늦은 CL anchor}}
$$

**§7 recap**: self-test의 목적은 계산 정답보다 "**어떤 정보가 없으면 해석이 불가능한가**"를 즉시 말하게 만드는 것입니다. Q15·Q16은 단일 정답이 없는 trade-off를 어떻게 *방어 가능한 추론*으로 변환하는지를 묻습니다.

---

<!-- SLIDE_START: §8 | title: 메타프레임과 큰 그림 -->

# §8 — 메타프레임과 큰 그림 (Meta-Frame & Big Picture)

> 🎯 Session 016의 moat는 source-locked 판단 언어입니다 — 모델·질환·TDM·용량·노출 보고를 한 줄 chain으로 말할 수 있어야 합니다.

## A. 이 세션의 위치

이 세션은 pharmacometrics 학습에서 "model building"과 "clinical dosing decision" 사이의 연결부를 다룹니다. 모델을 구성한 뒤 실제 환자 용량 판단으로 넘어가는 지점입니다. Ch.6은 model structure를 좁히는 눈을 만들고, Ch.15는 disease가 parameter를 어떻게 움직이는지 설명하며, PK35는 individual parameter를 posterior로 만들고, Ch.18은 그 estimate를 loading, maintenance, monitoring, missed-dose interpretation으로 바꿉니다.

## B. 네 가지 메타 패턴

1. **두 인자의 곱**: $R_d$는 $f_e\times RF$, forgiveness는 $t_{1/2}/\tau\times\text{therapeutic window}$, TCS는 $\text{risk}\times\text{measurability}$처럼 두 축이 함께 움직입니다.

$$
\underbrace{R_d}_{\text{renal 조정}}
\sim
\overbrace{\underbrace{f_e}_{\text{약물 속성}}\times\underbrace{RF}_{\text{환자 속성}}}^{\text{renal 의존}},
\qquad
\underbrace{\text{forgiveness}}_{\text{missed-dose 내성}}
\sim
\overbrace{\underbrace{\frac{t_{1/2}}{\tau}}_{\text{시간 여유}}\times\underbrace{\text{therapeutic window}}_{\text{농도 여유}}}^{\text{허용 여유}},
\qquad
\underbrace{TCS}_{\text{monitoring 전략}}
\sim
\overbrace{\underbrace{\text{risk}}_{\text{위험}}\times\underbrace{\text{measurability}}_{\text{측정성}}}^{\text{TCS 필요}}
$$

2. **식별가능성은 채혈 시점에 달린다**: early concentration은 $V$를, later/steady-state concentration은 $CL$을 더 잘 식별합니다.
3. **현실은 연속적, 소통은 이산적**: renal impairment stage, TCS candidate list, dialysis threshold는 communication tool이지 hard biological cutoff가 아닙니다.
4. **$CL$의 해부학이 용량 논리를 결정한다**: renal $CL$-dominant, hepatic $CL$-dominant, high-extraction, low-extraction, protein-bound drug은 같은 "$CL$ 감소" 언어로 묶을 수 없습니다.

## C. 소스 잠금 전문가 해석 지점

- Plot shape를 보고 ODE 후보를 줄입니다.
- $f_e/RF/R_d$로 신질환 maintenance adjustment를 계산합니다.
- C-G를 쓰되 SCr lag와 body composition caveat를 같이 판단합니다.
- Bayesian output을 prior, concentration, sampling time, dosing history의 산물로 읽습니다.
- TCS를 약물명 자동 적용이 아니라 criteria-based adjunct strategy로 운용합니다.
- LD와 MD를 $V$ vs $CL$ 문제로 분리합니다.
- Missed/erratic dosing을 "자료 오염"이 아니라 superposition problem으로 계산합니다.

## D. PK15 마무리 브리지

PK15는 처방 자체가 아니라 "선택된 용량에서 어떤 exposure와 safety margin을 보고할 것인가"를 담당합니다. 10/56/320 µmol·day⁻¹·kg⁻¹ dose levels, Cmax/AUC exposure 보고, therapeutic 농도 0.05–0.1 µM, high-dose Cmax 약 50 µM, >100배 safety margin은 임상 dosing chain의 마지막 reporting layer로만 사용합니다 [G&W pp.546–548].

## E. 최종 잠금 주의 목록

아래 표현은 source boundary 위반 또는 overclaim 위험이 있어 대체 표현으로 교체합니다.

**사용 금지 표현 (Do not say)**:

```text
- peak-shift direction = model class
- TCS candidate drug = mandatory TCS
- V/CL Fig.18-5 percentages = dosing accuracy
- PK35 digoxin case = direct prescription recommendation
- TDM patients are 80% irregular dosing
- hemodialysis decision = simple Vu<120 AND CLu<CLuD rule
- NDA/IND/RMP/software workflow = textbook source claim
```

**대신 사용할 표현 (Say instead)**:

```text
- peak-shift direction narrows competing models
- TCS is useful as adjunct when criteria are satisfied
- Fig.18-5 is variability partition
- PK35 estimates individual CL/V/t½; prescription is separate inference
- missed/unequal/erratic dosing is common enough to need equations, without source-free percentages
- dialysis effectiveness lies on Vu·CLu·CLuD coordinate plane
- implementation/regulatory extrapolations require [교과서 외 구현/규제 번역]
```

**최종 요약**: 이 세션의 캡스톤 척추는 "**shape로 모델 후보를 좁히고, 질환과 환자 특성으로 파라미터 편차를 설명한 뒤, Bayesian TDM과 dosing equation으로 치료 의사결정에 연결한다**"입니다. 핵심 주의점은 deterministic overclaim, 근거 없는 백분율, 라벨 없는 규제·소프트웨어 외삽, PDF에 없는 직접 처방 주장으로 넘어가지 않는 것입니다.

---

# 출력 후 자가검증 체크리스트

| 항목 | 기준 | 결과 |
|---|---|---|
| SLIDE_START 개수 | §섹션수 + 카드수 합산 | 15 개 |
| 카드당 callout 합계 ≤ 6 | 전체 카드 | ✓ |
| [E] 박스 존재 | 모든 §2 카드 | ✓ |
| [D] 거장의 시각 존재 | 모든 §2 카드 | ✓ |
| [L] 파라미터 표 존재 | Apex 카드 + 정의 수식 카드 | ✓ |
| §5 혼동 쌍 표 행 순서 고정 (4행) | §5 전체 | ✓ |
| 기호 일관성 | 첫 등장 기준 통일 | ✓ |
| PART B 흔적 없음 | 전체 | ✓ |
| 수치 anchor 보존 | PK35/PK15 등 원본 수치 | ✓ |
| [M] 나비효과 이중 종착점 | Apex 카드 전체 | ✓ |

<!-- v3.8 변환 노트
보존 감사 (HARD PRESERVE):
  - 출처 anchor: v3.7 55건 = v3.8 55건 (일치)
  - 수식 블록: v3.7 28개 = v3.8 28개 (일치)
  - SLIDE_START 마커: v3.7 15개 = v3.8 15개 (일치)
  - 카드 ID M1~M10: 10개 보존, 영문 원어 제목 그대로
  - 약물명 등장: v3.7과 동일하거나 증가(즉맥락화로 1회 추가된 약물 다수)
  - 수치 anchor (PK35 digoxin, PK15 toxicokinetics, R&T Ch.18 등): 모두 보존

활자량 감축:
  - 줄 수: 1120 → 995 (감축률 약 11%)
  - 바이트: 76235 → 약 68000 (감축률 약 11%)
  - 목표(40-55%)에 미달한 이유: 원본 v3.7이 이미 상당히 정제된 상태였음
    (한 카드당 평균 메타 문장이 1-2줄 수준). 한국어 한자어 압축의
    구조적 한계와 hard-preserve 항목(수식·표·앵커·수치)의 비중도 영향.

주요 변환:
  - 학습자 항법 안내 → §0 빠른 시작 박스로 단순화
    (5카드 핵심 경로 M1→M4→M5→M8→M9 명시)
  - (P01)~(P20) 감사 태그 17건 일괄 제거
  - 컴파일러 태그 [EXPERT_INFERENCE, v3], CRUCIBLE_DERIVED 제거 (내용 보존)
  - HTML 코멘트 "기호 통일" 2건 제거
  - 카드 끝 "확인 시점" 안내 일괄 제거
  - 💡+⚠️ 이중 콜아웃을 단일 콜아웃으로 통합 (전 카드)
  - 약물 예시 즉맥락화:
    digoxin → 강심배당체 / phenytoin → 항경련제 / vancomycin → 글리코펩타이드 항생제
    phenobarbital → 진정·항경련제 / cyclosporine → 면역억제제
    gentamicin → 아미노글리코사이드 항생제 / nortriptyline → 삼환계 항우울제
    theophylline → 기관지확장제
  - 번역체 관념어 자동 변환표 적용 ("분기된다"→"달라진다",
    "측정 교량"→"잇는 다리", "원칙을 고정"→"원칙을 정한다" 등)
  - "[교과서 외 통합 추론 예시]", "[확인 필요]" 등 정직성 마커는 보존
  - "Plausible Fallacy", "Memory Hook" 같은 학습 장치는 보존

컨텐츠 손실: 0건 (수식·앵커·수치·약물·결론 메시지 100% 보존)
-->

# 12 — Effect Compartment · Tolerance/Rebound · Transduction — v3.7

<!-- 기호 통일: ke0 → $k_{e0}$ (첫 등장 Card 1 기준) -->
<!-- 기호 통일: koff → $k_{off}$ (첫 등장 Card 1/PD21 기준) -->
<!-- 기호 통일: ktol → $k_{tol}$ (첫 등장 Card 3 기준) -->

임상 PK/PD 데이터에서 반시계방향 loop가 보이면, 가장 쉬운 답은 $k_{e0}$ 하나를 추가하는 것입니다. 그러나 PD21에서는 $k_{e0}=0.025\ \text{min}^{-1}$, $k_{out}=0.031\ \text{min}^{-1}$, $k_{off}=0.018\ \text{min}^{-1}$가 모두 비슷한 크기로 나타나 같은 단위가 같은 기전을 뜻하지 않음을 보여줍니다 [G&W p.846]. 반복 infusion의 trough drift와 rebound까지 보이면 문제는 더 이상 “효과부위로 늦게 도달했는가”가 아니라 “시스템 메모리 $M$이 남았는가”가 됩니다 [G&W pp.805–809]. 이 세션은 delay term을 붙이기 전에 지연되는 hidden state를 먼저 명명하도록 훈련합니다.

## 학습 항법 안내

**이 학습 자료 사용 방법**

1. 먼저 §1을 한 번 훑어 트리아지 지도로 사용하세요. 관찰된 농도-반응(concentration–response) 지연 하나가 서로 다른 세 가지 숨은 상태(hidden state)를 의미할 수 있습니다.
2. §2의 네 장 카드를 순서대로 학습하세요: 링크(Link) → 이력현상 트리아지(hysteresis triage) → 내성/반동(tolerance/rebound) → 신호전달(transduction).
3. 그림 포인터(Figure Pointer)가 나올 때마다 교과서·PDF 원본을 열어 확인하세요. 이 자료는 저작권 보호 교과서 그림을 직접 재현하지 않습니다.
4. §7로 가기 전에 §5를 먼저 보세요. 혼동 쌍(confusion pair)은 자기점검(자기점검(Self-Test)) 전에 가장 흔한 모델 선택 오류를 미리 막기 위해 설계되었습니다.
5. §6은 §5 이후, §7 이전에 보세요. 진단 시그니처(diagnostic-signature) 사전은 혼동 쌍을 정리한 뒤에 가장 유용하며, 자기점검에 필요한 구체적인 진단 어휘를 제공합니다.

**시작하기 전**

- 학습 전 전제: $E_{max}$/Hill 모델, 1구획 기초 PK, 간접반응(indirect response) 모델 용어에 이미 익숙해야 합니다.
- 읽는 내내 이 질문을 눈에 띄는 곳에 두세요: "지연된 숨은 상태(hidden state)는 무엇인가?"

**학습을 마친 뒤**

- $k_{e0}$, $k_{out}$, $k_{tol}$, $k_{off}$를 각각이 지배하는 시계(clock)가 무엇인지로 구분할 수 있어야 합니다.
- 이력현상 방향(hysteresis direction)이 최종 모델 선택 규칙이 아니라 진단 단서인 이유를 설명할 수 있어야 합니다. 또한 *이력현상 접힘 기법(hysteresis collapse method)*이 루프 기하학(loop geometry)을 수치 $k_{e0}$로 바꾸는 원리(PD21)를 설명할 수 있어야 합니다.
- PD13이 내성/반동(tolerance/rebound)에 속하는 이유와 G&W Table 3.10이 링크 모델(Link model) 함정인 이유를 설명할 수 있어야 합니다.
- PD13 Model I/II/III 파라미터 테이블 전체를 읽고, Model II가 단순히 우세하다는 사실을 넘어서 *왜* 우세한지 설명할 수 있어야 합니다.
- PD35가 신호전달 연쇄(transduction chain)를 지지하면서도 $n$이 정확한 생물학적 신호전달 단계 수를 의미하지 않는 이유를 설명할 수 있어야 합니다.
- 네 가지 GOF 진단 시그니처($EC_{50}$ 용량 분기, trough drift, S자형 CWRES 잔차, OFV plateau)와 각각이 함의하는 기계론적 의미를 명명할 수 있어야 합니다.


<!-- SLIDE_START: §1 | title: §1 — 세션 헤더와 로드맵 -->
# §1 — 세션 헤더와 로드맵

**소스(Source):** Gabrielsson & Weiner 5e + Rowland & Tozer 5e  
**챕터 범위:** G&W Ch.3 §3.9/§3.11/§3.13 + PD13/20/21/35; R&T Ch.8  
**핵심 과제:** 농도-반응 사이의 시간 지연을 **분포 지연(distributional delay)**, **시스템 적응(system adaptation)**, 또는 **신호전달 연쇄(transduction cascade)** 중 하나로 분류하는 것입니다.


## 3-layer 개념 지도

```text
Layer 1 — 무엇인가
  Delay · Hysteresis · Tolerance/Rebound · Transduction
        ↓
Layer 2 — 어떻게 계산되는가
  dCe/dt = ke0(C-Ce)
  dR/dt, dM/dt = turnover/moderator ODE
  dRi/dt = (Ri-1 - Ri)/tau
        ↓
Layer 3 — 언제, 왜 중요한가
  loop collapse · dose-scaling · trough drift · rebound · delayed sigmoid onset
```

🧭 **읽는 순서:**
카드 1 (Card 1): 관찰된 delay를 $C_e$와 $k_{e0}$로 설명할 수 있는가?
카드 2 (Card 2): loop 방향을 모델 선택이 아니라 triage gate로 어떻게 쓰는가?
카드 3 (Card 3): 반복 노출에서 tolerance와 rebound를 만드는 system memory는 무엇인가?
카드 4 (Card 4): 단일 turnover로 안 되는 delayed sigmoid onset은 언제 transit chain을 요구하는가?

**지식 그래프 위치:**
`[선행 세션: Direct response · Emax/Hill · 기본 turnover] → [이 세션: delay hidden-state triage] → [후속 세션: TMDD · PBPK-PD coupling · QSP]`


**핵심 통찰:** 혈장(plasma) 농도와 반응(response)은 서로 다른 기전적 이유로 시간상 분리될 수 있습니다. 전문가의 첫 판단은 단순히 "지연 항(delay term)을 하나 붙이는 것"이 아닙니다. 먼저 그 지연이 **약물 분포(drug distribution, $k_{e0}$)**, **시스템 회전/적응(system turnover/adaptation, $k_{out}$/$k_{tol}$)**, 또는 **하류 신호 전파(downstream signal propagation, $n \times \tau$)** 중 어디에 속하는지 정해야 합니다.


### 개념 로드맵

```text
Observed concentration–response time delay
        ↓
Hysteresis direction = first diagnostic clue
        ↓
Mechanism triage
   ├─ Distributional delay       → Effect compartment / Link / $k_{e0}$
   ├─ System turnover/adaptation → Indirect response / Tolerance / Moderator M
   └─ Signal transduction chain  → Transit compartments / tau / n
        ↓
Discrimination checks
   ├─ linear PK first, then tmax dose-invariance
   ├─ dose-stratified EC50/Emax/n plausibility
   ├─ repeated-dose trough drift / rebound
   └─ onset shape: immediate exponential vs delayed sigmoid
```


> 📊 **개념 도식 (HTML에서 렌더링):** F12-01 — PK/PD 시간 지연 뒤의 세 가지 숨은 시계 — 링크(Link), 내성(tolerance), 신호전달(transduction)은 병렬 레이블이 아니라 기전 트리아지(mechanism-triage) 순서로 다루어야 합니다.


챕터 순서 자체가 에스컬레이션(escalation) 논리입니다. §3.9는 "분포 지연(distributional delay)인가?"를 묻고, §3.11은 "시스템이 적응하고 있는가?"를 묻습니다. §3.13은 "측정된 반응(measured response)이 하류 cascade 뒤에 나타나는가?"를 묻습니다.

 따라서 같은 시간 지연(time delay)이라도 숨은 상태(hidden state)가 다르면 모델도 달라집니다. 이 세션의 핵심은 지연의 *크기*가 아니라, **무엇이 지연되는 상태(delayed state)인지**를 명명하는 것입니다.

> **거장의 시각(Mastery Lens) — [EXPERT_INFERENCE | SOURCE-AWARE]**  
> 이 세션에서 "지연(delay)"은 시간 차이 자체가 아니라 *숨은 상태(hidden state)를 찾으라*는 신호입니다. 먼저 지연된 상태의 이름을 붙인 뒤에야 ODE family를 선택할 수 있습니다. 실무 에스컬레이션 순서는 직접반응(direct response) → 효과구획(effect compartment, Link) → 간접반응(indirect response, turnover) → 내성(tolerance, Moderator) → 신호전달(transduction, transit chain)입니다. 이 순서는 §3.7 → §3.9 → §3.11 → §3.13의 G&W 챕터 순서와 동형이며, 새 데이터를 받으면 *어느 단계에서 시작할지*가 첫 5초의 판단이 됩니다.

---



<!-- SLIDE_START: §2 | title: §2 — 개념 해부 카드 -->
# §2 — 개념 해부 카드

---


<!-- SLIDE_START: Card 1 | title: Card 1 — 효과구획 모델(Effect Compartment Model)과 $k_{e0}$ [⚡ Apex Concept] -->
## Card 1 — 효과구획 모델(Effect Compartment Model)과 $k_{e0}$ [⚡ Apex Concept]

> **거장의 시각**
> 💢 **흔한 오해:** CCW hysteresis가 보이면 곧바로 effect compartment가 정답이라고 생각한다.
> ✅ **실제는:** $C_e$ 가설은 선형 PK, 용량 불변 $t_{max}$, loop collapse, 용량별 PD 파라미터 안정성을 모두 통과해야 살아남는다.
> 🎯 **체화할 단 하나의 직관:** Delay는 mechanism이 아니라 hidden state를 찾으라는 신호다.


> **⚡ Apex 명제(thesis) — [EXPERT_INFERENCE, v3]**  
> 관찰된 농도-반응 지연(concentration-response delay)은 진단의 **단서**이지 메커니즘 그 자체가 아닙니다. 모델러의 임무는 그 지연을 만드는 **숨겨진 상태(hidden state)에 이름을 붙이는 것**입니다. Card 1은 그 명명 작업의 첫 후보인 생체상 농도(biophase concentration) $C_e$를 다룹니다. 그러나 동일한 이력현상(hysteresis) 패턴은 이후 카드들의 다른 hidden state로도 만들어질 수 있습니다. 따라서 $C_e$ 가설을 채택하기 전에 반드시 *용량 스케일링(dose-scaling)* 검증과 *루프 접힘(loop-collapse)* 검사를 통과시켜야 합니다.
효과구획 모델(Effect Compartment Model)은 **분포 지연(distributional delay)**을 다루는 표준 링크 모델(link model)입니다. 혈장(plasma) 농도 $C$가 관찰되지 않는 생체상 농도(biophase concentration) $C_e$를 움직이고, $C_e$가 반응(response)을 움직입니다. 실무에서 가장 강한 시그니처는 **용량을 올려도 반응의 $t_{max}$가 동일**하다는 점입니다. 다만 이 판단은 PK가 선형일 때만 유효합니다 [G&W p.264].


### A. 형식적 정의

효과구획(effect compartment)은 혈장(plasma)과 생체상(biophase) 사이의 가상 1차(first-order) 분포 링크입니다 (← 약물이 작용하는 효과 부위). $C_e$는 직접 측정되지 않습니다. 따라서 반응-시간(response-time) 데이터로부터 역추정해야 합니다. 상승기(rising phase)와 하강기(falling phase) 정보가 모두 필요하므로, 정상상태(steady-state) 데이터만으로는 $k_{e0}$ 추정이 불가능합니다 [G&W p.263].

> 💡 **관측값과 숨은 상태 구분** — $C$는 측정 농도이고 $C_e$는 반응 곡선을 통해 역추정되는 biophase 상태입니다.
> ⚠️ **헷갈림 방지:** 정상상태 자료만 있으면 $C_e$와 PD shape가 분리되지 않아 $k_{e0}$가 식별되지 않습니다.
> 🔑 **채택 규칙:** 선형 PK, dose-invariant response $t_{max}$, single $k_{e0}$ loop collapse가 함께 보여야 합니다.


> 📖 **교과서 그림 참조:** G&W Fig.3.53 (p.263)
> F12-02는 $C_e$가 직접 측정되지 않고 반응-시간 데이터로부터 *추론*되는 이유를 시각적으로 이해하도록 돕습니다.
> 확인 시점: 효과구획 수식 도출을 읽기 전에, 혈장(plasma) 농도 → 효과구획 농도 $C_e$ → $C_e$ 대비 반응 → 반응-시간으로 이어지는 흐름을 확인할 때 사용하세요.


### B. 핵심 방정식

1구획 IV bolus 이후 혈장(plasma) 내 약물량(amount):

$$
\underbrace{A_p}_{\text{혈장량}}=\underbrace{D}_{\text{투여량}}\,\overbrace{e^{-\underbrace{K}_{\text{K: 혈장 제거}}t}}^{\text{잔존 분율}}
$$

효과구획 내 약물량:

$$
\underbrace{\frac{dA_e}{dt}}_{\text{Ae 변화율}}=\overbrace{k_{1e}A_p}^{\text{혈장→효과 유입}}-\overbrace{k_{e0}A_e}^{\text{효과구획 이탈}}
$$

적분된 약물량(integrated amount):

$$
\underbrace{A_e}_{\text{효과구획량}}=\overbrace{\frac{\underbrace{k_{1e}}_{\text{유입 속도}}\underbrace{D}_{\text{투여량}}}{\underbrace{k_{e0}-K}_{\text{속도 차}}}}^{\text{크기 스케일}}\left(\overbrace{e^{-Kt}}^{\text{혈장 입력 감소}}-\overbrace{e^{-k_{e0}t}}^{\text{효과구획 추종}}\right)
$$

표준 단순화 가정인 $k_{1e}=k_{e0}$와 분배 비율 무시($K_p=1$)를 적용하면, 생체상 농도는 다음과 같이 정리됩니다:

$$
\underbrace{k_{1e}=k_{e0}}_{\text{유입=평형화}},\qquad \underbrace{K_p=1}_{\text{분배비=1}}
$$

$$
\underbrace{C_e}_{\text{생체상 농도}}=\overbrace{\frac{\underbrace{k_{e0}}_{\text{$k_{e0}$ 평형화}}\underbrace{D}_{\text{투여량}}}{\underbrace{V_c}_{\text{Vc 희석공간}}\left(\underbrace{k_{e0}-K}_{\text{속도 차}\,}\right)}}^{\text{농도 스케일}}\left(\overbrace{e^{-Kt}}^{\text{혈장 감소}}-\overbrace{e^{-k_{e0}t}}^{\text{생체상 추종}}\right)
$$

 닫힌형(closed-form) 식은 bolus 상황에서 직관을 줍니다. 실제 피팅(fitting)에서는 같은 의미를 더 일반적으로 표현하는 ODE 형태(ODE form)가 중요합니다.

동등한 ODE 형태:

$$
\underbrace{\frac{dC_e}{dt}}_{\text{Ce 변화율}}=\underbrace{k_{e0}}_{\text{$k_{e0}$ 추종속도}}\left(\overbrace{C}^{\text{혈장 농도}}-\overbrace{C_e}^{\text{생체상 농도}}\right)
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $C_e$ | concentration | 효과부위/생체상 농도 | 직접 관찰 불가; 반응-시간 자료로 역추정 |
| $C$ | concentration | 혈장 농도 구동 함수 | PK profile, dose, input function |
| $k_{e0}$ | $\text{time}^{-1}$ | plasma–biophase 평형화 속도 | 분포 지연; 용량과 무관해야 함 |
| $K$ | $\text{time}^{-1}$ | 혈장 제거 속도 상수 | 선형 PK 제거 특성 |
| $V_c$ | volume | central dilution space | 분포용적/스케일링 가정 |

💡 **비유:** $C_e$는 혈장이라는 큰 도로에서 effect site라는 골목으로 들어간 뒤에야 보이는 신호입니다. $k_{e0}$는 그 골목 입구가 얼마나 빨리 열리는지를 나타내는 문 속도입니다.


이 ODE 형태가 유연한 이유는 구동(driving) 역할을 하는 혈장 농도 $C(t)$를 선형 PK, 비선형 PK, 또는 table function으로 넣을 수 있기 때문입니다 [G&W p.269; PD21 pp.840–841].

> **거장의 시각(Mastery Lens) — [EXPERT_INFERENCE | TEXTBOOK_CONSISTENT]**  
> $C_e$는 "관측 농도"가 아니라, 혈장 프로파일(plasma profile)과 반응 곡선(response curve)이 동시에 정합적이도록 강제되는 *숨은 상태(hidden state)*입니다. 따라서 $k_{e0}$ 추정의 품질은 농도 자료만이 아니라 반응(response)의 상승·하강 정보가 얼마나 잘 포착되었는지에 의해 제한됩니다.



### C. 핵심 가정과 경계조건

| 가정 | 유지 | 위반 시 경계 |
|---|---|---|
| $C_e$는 반응-시간(response-time) 데이터로부터 추론됨 | 예 | 상승/하강 반응 데이터가 없으면 → $k_{e0}$와 PD 형상(shape)이 분리되지 않습니다 [G&W p.263]. |
| $t_{max}$ 검사를 위한 선형 PK | 예 | 비선형 PK는 겉보기 peak shift를 만들 수 있습니다. $t_{max}$를 모델 식별자(discriminator)로 쓰기 전에 먼저 노출(exposure) 비례성을 확인하세요 [G&W p.264]. |
| $k_{1e}=k_{e0}$ | 예(수정 적용) | 이는 식별가능성(identifiability) 기반의 단순화 가정이지, 보편적 물리적 등식이 아닙니다 [G&W pp.263, 265]. |
| $K_p=1$ | 단순화 가정으로만 사용 | 분배(partitioning)가 존재하면 정상상태에서도 $C_e$와 $C$가 다를 수 있습니다. 추정된 $EC_{50}$는 혈장 스케일(plasma-scale) 대리(surrogate)값입니다 [G&W pp.263, 265–266]. |
| 반응이 $C_e$를 즉시 추종 | 조건부 | 시스템 회전(system turnover)이나 하류 cascade가 우세하면 간접반응/내성/신호전달(indirect response/tolerance/transduction)로 이동하세요. |


**현장 팁(Trench-Level Tip):** PK 선형성을 먼저 확인하지 않은 상태에서 $t_{max}$ 용량 불변성 검사(dose-invariance test)를 돌리지 마세요. G&W는 same-$t_{max}$ 성질을 "약물 동태가 선형이라는 가정 하에"라고 명시합니다 [G&W p.264].


### D. 보정된 수치 앵커

- **G&W Table 3.9:** 반응 평형 반감기(response equilibration half-lives) — terbutaline FEV-1 7.5 min, theophylline FEV-1 11 min, d-tubocurarine/vecuronium 근이완 4 min, fentanyl spectral edge 6.4 min, QT-quinidine 8 min [G&W p.269].
- **R&T succinylcholine은 별개의 사례입니다:** succinylcholine은 *용량-지속시간(dose-duration)* 예시입니다 — 0.5 mg/kg IV, $T_{50}\approx6$ min, $k\approx0.2\ \text{min}^{-1}$, 그리고 80→20% 반응 감소가 약 22%/min [R&T pp.249–256]. G&W Table 3.9의 $t_{1/2,k_{e0}}=4$ min 사례로 잘못 라벨링하지 마세요.
- **PD20:** 진통제 IV bolus 예시 — $D=45\ \mu\text{g/kg}$, $V=1\ \text{L/kg}$, $K=0.50\ \text{h}^{-1}$, 초기 추정값 $E_{max}\approx3{-}5$, $EC_{50}\approx1.5\ \mu\text{g/L}$, $k_{e0}\approx0.1\ \text{h}^{-1}$. G&W는 데이터셋이 단일 용량만 포함했기 때문에 $EC_{50}$ 정밀도가 낮다고 기술합니다 [G&W pp.836–839].


### E. 그럴듯한 오해 — 회전 데이터에 링크 모델을 끼워 맞추는 경우

여기서 함정은 PD13이 아닙니다. **G&W §3.9.7 Table 3.10**이 진짜 주의 대상입니다. 여기서는 회전으로 생성된 데이터(turnover-generated data)를 효과구획 모델(effect-compartment model)에 끼워 맞춥니다. 그 결과 용량별 피팅(dose-stratified fits)에서 생물학적으로 비현실적인(biologically implausible) $EC_{50}$/$E_{max}$/$n$ 변화가 나타납니다: dose 1 $EC_{50}=0.681$, dose 10 $EC_{50}=4.85$, dose 100 $EC_{50}=0.941$. 약 7배의 $EC_{50}$ 분산은 소스에서 유도된 계산입니다 [G&W p.271]. Fig.3.59는 PD13이 아니라 PD12 데이터를 사용한 것으로 설명됩니다.

**진단명:** *$EC_{50}$ 용량 분기(dose-bifurcation) 패턴*. 용량별 피팅(dose-stratified fit)이 기전적 근거 없이 수용체 민감도(receptor sensitivity)나 용량(capacity)이 용량에 따라 바뀐다는 것을 함의한다면, 링크(Link) 모델이 회전/적응(turnover/adaptation) 오설정(misspecification)을 흡수하고 있을 가능성이 높습니다 [G&W pp.271–272]. 전체 시그니처 사전은 §6 진단 렌즈(Diagnostic Lens)를 참조하세요.


> 📖 **교과서 그림 참조:** G&W Fig.3.59와 Table 3.10 (p.271)
> F12-03은 이 함정이 PD13이 아니라 §3.9.7/Table 3.10(PD12 데이터)에 해당함을 정정하고, link 모델 오설정의 시각적·수치적 신호를 확인하기 위함입니다.
> 확인 시점: 회전으로 생성된 데이터(turnover-generated data)를 효과구획 모델(effect-compartment model)에 끼워 맞춘 결과를 해석할 때 사용하세요.


> **실패 양식(Failure Mode) — [AUDIT_DERIVED]**  
> 용량별 $EC_{50}$/$E_{max}$/$n$이 크게 흔들릴 때 첫 질문은 "PD가 dose-dependent한가?"가 아닙니다. 먼저 "링크(Link) 모델이 다른 *지연된 시스템 상태(delayed system state)*를 대신 흡수하고 있지는 않은가?"를 물어야 합니다. Table 3.10 함정은 이 질문을 자동화하기 위한 경고 표지입니다.


### M. Plausible Fallacy — 나비효과 연쇄

**오류:** “반시계방향 이력현상이 보이면 효과구획 모델이 답이고, $k_{e0}$를 추가하면 된다.”

**왜 그럴싸한가:** 단회투여 데이터에서는 $k_{e0}$라는 추가 자유도가 표면적 fit을 거의 항상 개선하고, CCW loop가 실제로 분포 지연에서도 나타나기 때문입니다.

**나비효과:** CCW loop를 effect compartment로 고정 → 용량별 $k_{e0}$ migration 또는 $EC_{50}$/$E_{max}$/$n$ 분기 무시 → [임상] 반복투여 trough drift·rebound·고용량 지연 반응 예측 실패 → [모델링/규제] turnover/transduction 대안 모델 비교와 dose-scaling 재분석 요구.

**GOF 진단 시그니처:** 용량별 $k_{e0}$ 이동, dose-stratified PD parameter instability, loop collapse 실패.


### F. $k_{e0}$ vs $k_{out}$ vs $k_{off}$

PD21은 *동일한 단위가 동일한 의미를 함의하지 않는 이유*를 보여줍니다. $k_{e0}=0.025$, $k_{out}=0.031$, $k_{off}=0.018\ \text{min}^{-1}$는 수치적으로 유사할 수 있지만, 서로 다른 *시계(clock)*를 가리킵니다: 생체상 평형(biophase equilibration), 시스템 회전(system turnover), 수용체 해리(receptor dissociation) [G&W p.846].

$$
\overbrace{k_{e0}=0.025}^{\text{Ce 평형 시계}},\quad \overbrace{k_{out}=0.031}^{\text{turnover 시계}},\quad \overbrace{k_{off}=0.018\ \text{min}^{-1}}^{\text{$k_{off}$ 해리 시계}}
$$


---



### E. 핵심 요약 박스

> **Card 1 체화 핵심**
> ① `CCW hysteresis가 처음 보일 때` → $C_e$와 $k_{e0}$ 가설이 첫 후보가 된다.
> ② `반복투여 carry-over 또는 용량별 parameter migration` → turnover/tolerance/transduction이 지배할 수 있다.
> ⚡ `CCW loop = effect compartment 확정` → loop collapse와 dose-scaling 검증 생략 → 임상 예측과 규제 방어 모두 실패한다.


<!-- SLIDE_START: Card 2 | title: Card 2 — 이력현상(Hysteresis) 방향과 기전 트리아지(Mechanism Triage) -->
## Card 2 — 이력현상(Hysteresis) 방향과 기전 트리아지(Mechanism Triage)

> **앞 카드에서 이 카드로:** $C_e$와 $k_{e0}$ 후보를 검토했지만, loop 방향만으로는 어떤 hidden state가 늦는지 확정할 수 없기 때문에 hysteresis triage가 필요하다.

> **거장의 시각**
> Loop 방향을 최종 판결로 읽으면 turnover·tolerance·transduction을 link model 하나로 흡수하는 실수가 생긴다.
> Direction → sampling density → input-rate artifact → loop collapse → 반복투여/기전 증거 순서로 읽으면 모델 family가 좁혀진다.

이력현상(hysteresis) 방향은 **첫 진단 단서(first diagnostic clue)**이지 최종 판결이 아닙니다. 반시계방향(counterclockwise) 루프는 대개 반응(response)이 농도보다 늦는다는 뜻입니다. 시계방향(clockwise) 루프는 내성(tolerance), 길항(antagonism), 또는 적응(adaptation)을 시사합니다. 그러나 최종 모델 선택에는 추가 근거가 필요합니다 [R&T pp.234–246; G&W pp.295–296].

> 💡 **방향은 필터다** — Hysteresis 방향은 후보 family를 줄일 뿐, mechanism을 확정하지 않습니다.
> ⚠️ **헷갈림 방지:** 빠른 IV bolus의 input-rate artifact는 tolerance처럼 보이는 clockwise loop를 만들 수 있습니다.
> 🔑 **진단 순서:** 방향 판독 다음에는 sampling density와 loop collapse를 확인합니다.


### A. 정의

이력현상(hysteresis)이란 농도가 상승할 때와 하강할 때 반응이 서로 다른 경로를 따르는 현상을 말합니다. R&T는 이를 digoxin과 naproxen으로 보여줍니다. Digoxin에서는 IV 투여 후 첫 4시간 동안 혈장(plasma) 농도가 감소하는 *동안* 심장 효과(cardiac effect)는 오히려 증가합니다. Naproxen에서는 경구 500 mg 투여 후 통증 완화(pain relief)에서 반시계방향(counterclockwise) 이력현상이 나타납니다 [R&T pp.234–235].


> 📖 **교과서 그림 참조:** R&T Fig.8-2 (p.235)
> F12-04는 이력현상(hysteresis) 방향을 단어 레이블이 아니라 시간순 경로로 시각화하도록 돕습니다.
> 확인 시점: 진단 매트릭스를 사용하기 전에, naproxen 루프에서 같은 농도가 서로 다른 반응에 대응하는 지점을 확인할 때 사용하세요.


### B. 진단 매트릭스

| 방향 | 1차 해석 | 검증할 기전 후보 | 필요한 후속 분석 |
|---|---|---|---|
| 반시계방향(Counterclockwise) | 반응이 농도보다 늦음 | 분포 지연, 간접반응(indirect response), 느린 수용체 결합, 동조성 대사체(concordant metabolite) | 용량별 $t_{max}$ 패턴, 상승/하강 반응, 대사체/표적 데이터, 모델 비교 |
| 시계방향(Clockwise) | 반응이 농도보다 일찍 약화 | 내성/탈감작(tolerance/desensitization), 길항성 대사체, 수용체 down-regulation | 반복 투여 패턴, 반동(rebound), 대사체 약리, 회복 동역학 |
| 8자형/혼합 | 경쟁하는 시간 척도 | 분포 지연 + 내성, 희소 샘플링 artifact, 다중 기전 | 모델 확정 전 더 조밀한 샘플링과 기전 기반 실험 설계 |


### B-2. 이력현상 collapse 기법 — 루프 기하학을 수치로 변환하기

R&T는 Card 1과 Card 2를 잇는 강력한 진단 수단을 소개합니다. 시간으로 짝지은 농도-반응 데이터를 효과구획 변환(effect-compartment transformation)하면, 분포 지연이 우세한 기전일 때 반시계방향 루프를 단일 농도-반응 곡선으로 *collapse*시킬 수 있습니다 [R&T pp.245–246, Fig.8-14]. 가장 깨끗한 collapse를 만드는 $k_{e0}$ 값이 곧 분포 지연 추정치입니다.

PD21이 이를 구체화합니다. 길항제 X 실험에서 보고된 $k_{e0}\approx0.025\ \text{min}^{-1}$은 반응 데이터를 $C$ 대신 $C_e$에 투영했을 때 상승부와 하강부 데이터를 하나의 매끄러운 곡선으로 묶어주는 값입니다 [G&W PD21 pp.840–846]. 이는 §2 Card 1 도출에서 나타난 동일한 수치적 시계지만, 여기서는 *그래픽 기반 모델 식별 도구*로 운용됩니다.

> **거장의 시각(Mastery Lens) — [TEXTBOOK_DERIVED | SOURCE-AWARE]**  
> Loop collapse가 깨끗하게 일어나면 분포 지연 가설은 살아남습니다. Collapse가 깔끔하지 않거나 용량마다 서로 다른 $k_{e0}$가 필요하다면, 다른 숨은 상태(turnover 또는 transduction)가 작용 중이라는 신호입니다. 이때 다음 카드(Card 3, Card 4)로 넘어가는 결정이 강제됩니다.



### C. R&T 임상 앵커

- **Digoxin:** IV 투여 후 0–4시간 동안 plasma는 감소하지만 효과는 상승; 심장 조직으로의 분포와 표적 결합이 느리기 때문 [R&T p.234].
- **Naproxen:** 경구 500 mg에서 반시계방향 이력현상; 효과구획 변환으로 루프를 더 명료한 농도-반응 관계로 collapse 가능 [R&T pp.235, 245–246].
- **Warfarin:** 지연된 prothrombin complex 반응은 단순 조직 분포가 아니라 *시스템 회전(system turnover)*을 반영한다 [R&T pp.242–248].
- **Succinylcholine:** 반응 지속 시간이 *용량-지속시간(dose-duration)* 논리를 따른다; 감소/지속 교육에는 유용하나 G&W Table 3.9의 효과구획 반감기와 동일하지 않다 [R&T pp.249–256].

> **범위 마이크로패치(Scope Micro-Patch) — [TEXTBOOK_DERIVED | SCOPE_REQUIRED]**  
> 기전 트리아지를 위해 다음 R&T 지속시간 앵커들은 가시 상태로 유지되어야 한다: naproxen 500 mg 경구는 반시계방향 이력현상과 지연된 peak-response 패턴; warfarin 1.5 mg/kg 경구는 약 48시간 지연된 prothrombin-complex nadir와 1–2일 수준의 시스템 회전; aspirin 650 mg는 짧은 plasma 반감기에도 항혈소판 반응이 수일 지속; succinylcholine 0.5 mg/kg IV는 *용량-지속시간 예시*로 유지되어야 하며 G&W Table 3.9의 4-min $t_{1/2,k_{e0}}$ 사례로 재라벨링하면 안 된다 [Scope Lock; R&T pp.234–256].


**현장 팁(Trench-Level Tip):** 희소 샘플링은 *가짜 8자형*을 만들어낼 수 있습니다. 방향을 해석하기 전에 농도와 반응 모두에서 상승/하강을 포착할 만큼 샘플링 밀도가 충분한지 확인하세요. 그렇지 않으면 루프 기하학은 *기전이 아니라 플롯팅 아티팩트*입니다.


### D. 구조적 해석

시계/반시계 방향은 시간으로 짝지은 농도와 반응의 상평면(phase-plane) 궤적을 기술합니다. 방향은 모델 family를 좁혀주지만, 그것만으로 분포 지연과 회전 지연을 구분하지는 못합니다. 결정적 질문은 이것입니다: **무엇이 지연되고 있는가 — 생체상의 약물 농도($C_e$)인가, 생리학적 반응 시스템($R$)인가, 아니면 하류 cascade의 신호($R_n$)인가?**

R&T가 명시하는 중요한 경계 조건이 있습니다. 약물 주입 속도가 분포 속도나 tolerance 발달 속도를 압도하면 — 예컨대 매우 빠른 IV bolus에서 — 시계방향 루프가 나타날 수 있습니다 [R&T p.236]. 이것은 tolerance가 아니라 *입력 속도 아티팩트(input-rate artifact)*이며, 더 느린 infusion이나 경구 데이터로 재검증하면 사라집니다. 이 아티팩트를 tolerance로 오인하면 불필요한 Moderator 모델 피팅으로 이어집니다.

> **실무 시각(Practice Lens) — [CRUCIBLE_DERIVED]**  
> 이력현상 방향은 모델 family를 줄여주는 *필터*이지 판결문이 아닙니다. *방향 → 선형성/$t_{max}$ → 반복 투여 패턴 → 기전 증거* 순으로 검증해야 루프 기하학을 기전으로 과해석하지 않습니다.


---



### E. 핵심 요약 박스

> **Card 2 체화 핵심**
> ① `loop 방향을 처음 판독할 때` → 후보 모델 family를 좁히는 triage가 결정한다.
> ② `방향은 같지만 collapse가 실패할 때` → $C_e$가 아니라 $R$, $M$, 또는 $R_n$이 지연될 수 있다.
> ⚡ `hysteresis 방향 = mechanism` → input-rate artifact와 turnover를 놓쳐 잘못된 ODE family로 고정된다.


<!-- SLIDE_START: Card 3 | title: Card 3 — 조절자 $M$을 통한 내성·반동(Tolerance/Rebound via Moderator $M$) -->
## Card 3 — 조절자 $M$을 통한 내성·반동(Tolerance/Rebound via Moderator $M$)

> **앞 카드에서 이 카드로:** Loop collapse가 깨끗하지 않거나 반복투여에서 carry-over가 보이면, 지연되는 것은 $C_e$가 아니라 시스템의 반조절 상태일 수 있다.

> **거장의 시각**
> Tolerance와 rebound를 별개의 현상으로 읽으면 반복 infusion의 trough drift와 washout 후 overshoot를 한 구조로 설명하지 못한다.
> $M$을 system memory로 보면 dosing 중 효과 감소와 중단 후 rebound가 같은 ODE 쌍의 두 phase로 정리된다.

내성(tolerance)과 반동(rebound)은 서로 무관한 두 현상이 아닙니다. 조절자 모델(Moderator model)에서 $M$은 반응(response)을 뒤따라 형성되는 지연된 반조절 상태(delayed counter-regulatory state)입니다. 투여(dosing) 중에는 $M$이 response를 줄입니다. 투여가 중단된 뒤에는 $M$이 남아 baseline 너머의 rebound를 만들 수 있습니다 [G&W pp.297–300].

이 추상적 ODE 쌍이 임상에서 나타나는 모습은 매우 구체적입니다. Nitroglycerin 작업자의 "월요일 두통, 일요일 angina" 패턴(G&W Fig.3.71의 hat TDS 일화) — 약물이 반복 노출되면 효과가 줄고(tolerance), 주말 dose holiday에 baseline 너머의 vasoconstrictive rebound가 발생할 수 있다는 임상 신호 — 가 같은 ODE 쌍의 두 phase로 나타납니다 [G&W pp.284–286]. β-agonist의 점진적 desensitization, opioid의 점진적 내성, cocaine의 acute cardiovascular tolerance는 모두 같은 Moderator 구조의 변주입니다 [G&W pp.284–286, 295–296].


### A. 형식적 정의

내성(tolerance)은 노출이 지속되는 동안 반응이 점진적으로 감소하는 현상이고, 반동(rebound)은 약물 투여 중단 후 반응이 기저치를 벗어나 과도하게 움직이는 현상입니다. G&W는 tolerance의 분자 메커니즘으로 수용체 down-regulation/internalization, 신호 전달계 변화, cofactor 고갈, mRNA/단백질 수준 변화, 항체 형성, 효소 유도(enzyme induction)를 열거합니다 [G&W pp.284–286].

> 💡 **같은 방정식의 두 얼굴** — 투여 중에는 $M$이 tolerance를 만들고, 중단 후에는 남은 $M$이 rebound를 만듭니다.
> ⚠️ **헷갈림 방지:** Rebound는 약물이 남아서가 아니라 counter-regulatory state가 남아서 생길 수 있습니다.
> 🔑 **반복투여 규칙:** trough drift와 second-cycle carry-over가 보이면 $k_{e0}$ 단독 모델을 의심합니다.


### B. 조절자 ODE

핵심 음의 되먹임 모델(core negative-feedback model):

$$
\underbrace{\frac{dR}{dt}}_{\text{R 변화율}}=\overbrace{k_{in}S(C)}^{\text{자극 입력}}-\overbrace{k_{out}M}^{\text{M 억제}}
$$

$$
\underbrace{\frac{dM}{dt}}_{\text{M 변화율}}=\underbrace{k_{tol}}_{\text{$k_{tol}$ 적응속도}}\left(\overbrace{R}^{\text{현재 R}}-\overbrace{M}^{\text{지연 M}}\right)
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $R$ | response unit | 관찰 또는 모델링되는 반응 수준 | drug stimulus와 system turnover |
| $M$ | response/moderator unit | 지연된 반조절 상태, system memory | $R$을 따라 형성; washout 후 잔류 가능 |
| $k_{in}$ | response/time | 반응 생성률 | baseline turnover 설정 |
| $k_{out}$ | $\text{time}^{-1}$ | 반응 소실/회전 속도 | system turnover |
| $k_{tol}$ | $\text{time}^{-1}$ | moderator 적응 속도 | tolerance/rebound 발달·회복 속도 |
| $S(C)$ | dimensionless | 약물 자극 함수 | 농도와 PD 모델 형태 |

💡 **비유:** $R$은 현재 체온계 숫자이고 $M$은 늦게 따라오는 자동온도조절기입니다. 약물이 사라져도 조절기가 한동안 이전 방향으로 밀고 있기 때문에 rebound가 생깁니다.


기저 상태(baseline)에서 $S(C)=1$이고 $R_0=k_{in}/k_{out}$이다 [G&W pp.299–300]. 단순형에서 정상 상태(steady state)에 도달하면 $dM/dt=0$이므로 $k_{tol}(R-M)=0$, 즉 $R=M$이 된다 ($k_{tol}\neq0$ 가정 하에).

$$
\underbrace{S(C)=1}_{\text{기저 자극}},\quad \underbrace{R_0=\frac{k_{in}}{k_{out}}}_{\text{기저 R}},\quad \underbrace{\frac{dM}{dt}=0}_{\text{정상상태}}\Rightarrow \underbrace{k_{tol}(R-M)=0}_{\text{R-M=0}}\Rightarrow \underbrace{R=M}_{\text{M=R}}
$$

겉보기 반응 반감기(apparent response half-life)는 자극(stimulus) 의존 표현으로 지배된다 [G&W p.299, Eq.3:204]:

$$
\underbrace{t_{1/2,k_{out}}}_{\text{겉보기 반감기}}=\frac{\overbrace{\ln 2}^{\text{반감기 상수}}\,\overbrace{R_0}^{\text{기저 R 크기}}}{\underbrace{k_{in}}_{\text{생성률}}\,\underbrace{S(C)}_{\text{약물 자극}}}
$$

자극 $S(C)$가 클수록(고용량 또는 강한 약물) response의 *겉보기 반감기*는 짧아진다. 이것이 "왜 고용량에서 tolerance가 더 빠르게 발달하는가"에 대한 수학적 답이다. 단, kinetics 자체가 빨라지는 것이 아니다. 같은 kinetic constant 아래에서 driver인 $S(C)$가 커짐으로써 effective time scale이 단축될 뿐이다.

💡 **비유:** 같은 배수관이라도 물탱크에 압력이 더 크게 걸리면 눈에 보이는 수위 변화는 더 빨라 보입니다. 관의 물리적 직경이 바뀐 것이 아니라 driving force가 커진 것입니다.

> **거장의 시각(Mastery Lens) — [CRUCIBLE_DERIVED]**  
> $M$은 약물 구획(drug compartment)이 아니라 *시스템 메모리(system memory)*이다. Rebound가 생기는 이유는 약물이 남아서가 아니라, 약물이 사라진 뒤에도 *반조절 상태(counter-regulatory state)*가 남아 반응 방정식을 계속 밀기 때문이다.

더 일반적인 "조절자 + 반응 수준(moderator + level of response)" 형식은 비선형 $M$ 효과를 도입하고 2차 정상상태 해(second-order steady-state solution)를 만든다 [G&W pp.301–302, Eq.3:205–3:216]. 이 핸드아웃의 핵심 포인트는 대수적 전개 자체가 아니라 그 *결과*다 — 되먹임 강도가 반응 수준과 회복 행동을 바꾼다.


### B-2. 음의 되먹임 부호가 수학적으로 필요한 이유

Eq.3:193에서 moderator $M$은 반응 방정식에 *빼기* 부호로 진입한다 — 자극에 맞서는 방향이다. 만약 부호가 반전되어 $M$이 $S(C)$를 더하는 방향으로 작용했다면, 시스템은 homeostasis로 돌아오는 대신 self-amplify하여 발산했을 것이다. 따라서 음의 부호는 임의의 modeling 선택이 아니라, homeostasis를 만들어야 하는 모든 모델의 *구조적 안정성 요구사항*이다 [G&W pp.297–300; structural commentary, source-bounded].

이 부호 하나가 PD13 Model II의 $AIC=-97.5$ 우위를 만드는 *수학적 정합성*의 출처이다. Model I (no feedback) 또는 Model III (pool/precursor)이 같은 수치적 적합도를 흉내낼 수는 있어도, *반복 dose에서 baseline-traversing rebound와 partial tolerance를 함께* 생성하는 구조적 필연은 음성 피드백 부호로부터만 emerge한다.


### C. AUC 비대칭성 — 내장된 시그니처

Moderator 시스템에서 dosing 중 기저치 상방 반응 면적($AUC_E$)은 일반적으로 투여 중단 후 기저치 하방 rebound 면적($AUC_R$)보다 크다: $AUC_R < AUC_E$ [G&W Fig.3.82, p.298]. 이 비대칭의 구조적 이유는 다음과 같다 — dosing 중에는 drug stimulus와 아직 상승 중인 $M$이 함께 $R$을 밀지만, 투여 중단 후에는 잔류 $M$만이 편차를 만들기 때문이다. 이 비대칭은 진단 체크로 바로 활용된다: 데이터에서 명확한 비대칭이 보이는데 모델이 $AUC_R \approx AUC_E$를 예측한다면, moderator 구조가 잘못 설정된 것이다.

$$
\underbrace{AUC_R}_{\text{rebound AUC}}<\underbrace{AUC_E}_{\text{효과 AUC}},\qquad \underbrace{AUC_R\approx AUC_E}_{\text{대칭 예측 경고}}
$$



### D. PD13 앵커 — 반복 infusion에서의 내성/반동

PD13은 반복 IV infusion의 정식 사례 연구다. 이 사례는 일반 회전(ordinary turnover), 음의 되먹임 조절자(negative-feedback moderator), pool/precursor 구조를 비교한다 [G&W pp.805–809]. 가장 잘 맞는 것은 Model II, 즉 조절자(moderator) 모델이다. 이는 단순 진술이 아니라 *비교*로 읽어야 한다 — 다음 표가 그 비교다 [G&W p.808, Table 13.1].

| 파라미터 | Model I (no FB) | **Model II (Moderator)** | Model III (pool/precursor) |
|---|---:|---:|---:|
| $k_{in}$ | 21 | **30** | 94 |
| $k_{out}$ | 7.3 | **2.9** | 35 |
| $k_{tol}$ | — | **4.2** | 0.05 |
| $EC_{50}$ / $IC_{50}$ | 390 | **350** | 270 |
| $E_{max}$ / $I_{max}$ | 4.8 | **9.8** | 0.84 |
| n (Hill) | — | **7.4** | — |
| AIC | −39.0 | **−97.5** | −43.5 |
| WRSS | 0.33 | **0.083** | 0.28 |

읽는 방법: AIC/WRSS만 보고 Model II를 채택하면 학습이 절반에 그친다. 핵심 mechanistic 발견은 따로 있다 — *Model II의 $k_{tol}=4.2 > k_{out}=2.9$*, 즉 tolerance 발달(memory build-up) 속도가 response turnover 속도보다 빠르다는 부등식이다 [G&W p.808]. 이 부등식이 단일 infusion 안에서도 tolerance가 가시화되는 이유이고, Model III의 $k_{tol}=0.05$가 임상적으로 비현실적인 이유이다.

$$
\overbrace{k_{tol}=4.2}^{\text{$k_{tol}$ 내성속도}}>\underbrace{k_{out}=2.9}_{\text{kout turnover}},\qquad \underbrace{k_{tol}=0.05}_{\text{느린 precursor}}
$$

핵심 해석은 **trough drift / carry-over**입니다. 반복 infusion에서는 조절자 상태(moderator state)가 완전히 돌아오지 않았기 때문에 두 번째 trough가 첫 번째 trough로 단순히 초기화(reset)되지 않습니다. 이 때문에 내성(tolerance)을 보려면 single-dose 데이터보다 *반복 투여 데이터*가 훨씬 더 정보적입니다 [G&W p.808].


> 📖 **교과서 그림 참조:** G&W Fig.13.1과 Table 13.1 (pp.806–808)
> F12-05는 Model II의 우월성을 단순한 AIC/WRSS 수치가 아니라 가시적인 반복 투여 메모리와 연결하기 위함입니다.
> 확인 시점: PD13 반복 IV infusion 단락을 읽은 뒤, 두 번째 infusion이 깨끗한 reset인지 또는 숨은 조절자 상태(hidden moderator state)의 carry-over를 보이는지 판단할 때 사용하세요.


**현장 팁(Trench-Level Tip):** 비슷한 노출(exposure) 하에서 두 번째 trough가 첫 번째 trough와 다르다면, 숨은 조절자 상태(hidden moderator state)를 의심하세요. 직접반응(direct response)이나 순수 link 모델은 그 메모리를 자연스럽게 운반하지 못한다.


### E. 대안적 내성/반동 구조 — 압축 맥락

- **시간 의존 감쇠(Time-dependent attenuation, Colburn–Eldon):** 시간에 따른 potency/capacity의 경험적 평활화; 유용하나 기전성이 약하고 rebound 설명에 취약하다 [G&W pp.291–292].
- **길항성 대사체(Antagonistic metabolite):** 길항(antagonism)은 설명할 수 있으나 추가 구조 없이는 rebound를 다루지 못한다 [G&W pp.292–293].
- **내성 구획 / 반작용 기전(Tolerance compartment / counteracting mechanisms):** 적응 시스템을 위한 대안적 상태변수 형식 [G&W pp.293–295].
- **Pool/precursor 모델 (PD13의 Model III):** 이 데이터셋에서 검증되었으나 조절자 Model II보다 열등하다 [G&W pp.807–808]; 완전 내성만 예측하고 부분 내성은 설명하지 못한다.


### F. 부호가 중요한 이유

조절자 $M$은 $R$을 뒤따르지만, 반응 방정식에서는 *반작용(counteracting) 항*으로 나타난다. 이 음의 되먹임(negative-feedback) 부호 덕분에 시스템은 *자기증폭형(self-amplifying)*이 아니라 *항상성(homeostatic)*으로 작동한다. 여기서 필요한 한 줄짜리 기전 메모리는 다음과 같다: **약이 R을 밀고(drug pushes R), R이 M을 키우고(R builds M), M이 되받아 민다(M pushes back).**


---



### E. 핵심 요약 박스

> **Card 3 체화 핵심**
> ① `반복 노출 중 효과가 줄고 trough가 drift할 때` → moderator $M$과 $k_{tol}$이 결정한다.
> ② `약물 중단 뒤 baseline을 넘어 반동할 때` → 남아 있는 system memory $M$이 지배한다.
> ⚡ `rebound = 약물이 남은 효과` → washout 후 반조절 상태를 놓쳐 반복투여 예측이 실패한다.


<!-- SLIDE_START: Card 4 | title: Card 4 — 신호전달 모델 / Transit Chain(Transduction Model / Transit Chain) -->
## Card 4 — 신호전달 모델 / Transit Chain(Transduction Model / Transit Chain)

> **앞 카드에서 이 카드로:** $M$ 하나로도 delayed onset의 S자형 전파가 설명되지 않으면, 측정 반응까지 여러 하류 단계가 지연되는지 확인해야 한다.

> **거장의 시각**
> Transit chain의 $n$을 실제 생물학적 단계 수로 직역하면 과해석과 과모수화가 동시에 발생한다.
> $n\times\tau$를 onset 형상을 재현하는 effective signal clock으로 보면 PD35의 WRSS 개선과 정보 한계를 함께 해석할 수 있다.

신호전달(transduction) 모델은 수용체 활성화(receptor activation)와 관찰된 기능적 반응(observed functional response) 사이의 *연쇄(chain)*를 표현합니다. 반응 개시(onset)가 즉각적인 지수형(immediate exponential)이 아니라 *지연된 시그모이드(delayed sigmoid)*라면, 단일 회전 구획(단일 회전(single turnover) compartment)은 깊이가 부족할 수 있습니다. 이때 *순차적 transit compartments*가 필요합니다 [G&W pp.323–325].


### A. 형식적 정의

신호전달 모델은 수용체-리간드 결합과 관찰된 반응 사이에 *구획 또는 사건의 연쇄*를 사용합니다. 각 transit 단계는 고유한 transit time $\tau$와 그에 대응하는 분획 회전율(fractional turnover rate) $k_{out}=1/\tau$를 갖습니다 [G&W pp.323–325].

> 💡 **연쇄가 만드는 형상** — Transit chain은 단순 지연량이 아니라 onset curve의 S자형 모양을 만듭니다.
> ⚠️ **헷갈림 방지:** $n$은 관찰 가능한 생물학적 단계 수가 아니라 effective chain depth로 해석해야 합니다.
> 🔑 **채택 규칙:** $n=1$에서 early/late residual이 S자형으로 남고 $n=2,3$에서 WRSS가 크게 줄면 chain을 검토합니다.

$$
\underbrace{k_{out}}_{\text{transit 회전율}}=\frac{1}{\underbrace{\tau}_{\text{통과시간}}}
$$


> 📖 **교과서 그림 참조:** G&W Fig.3.98과 Fig.3.99 (p.323)
> F12-07은 "약물이 부위에 늦게 도달함"과 "측정 반응까지의 신호 전파가 느림"을 구분하도록 돕습니다.
> 확인 시점: 신호전달 ODE를 읽기 전에, 수용체-반응(receptor-to-response) 연쇄와 15–20시간 onset 지연 패턴을 확인할 때 사용하세요.


### B. 핵심 방정식

수용체-구동 단계(receptor-driving step):

$$
\underbrace{\frac{dR_e}{dt}}_{\text{Re 변화율}}=\underbrace{\frac{1}{\tau}}_{\text{단계 전달속도}}\left(\overbrace{E_0S(C)}^{\text{목표 반응}}-\overbrace{R_e}^{\text{현재 Re}}\right)
$$

순차적 transit compartments:

$$
\underbrace{\frac{dR_i}{dt}}_{\text{transit i 변화율}}=\underbrace{\frac{1}{\tau}}_{\text{단계 전달}}\left(\overbrace{R_{i-1}}^{\text{상류 상태}}-\overbrace{R_i}^{\text{현재 상태}}\right),\quad \underbrace{i=1,2,\ldots,n}_{\text{단계 인덱스}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $R_e$ | response unit | receptor-driven entry response | $E_0S(C)$와 현재 $R_e$ 차이 |
| $R_i$ | response unit | i번째 transit state | 이전 단계 $R_{i-1}$의 전달 |
| $n$ | count | effective chain depth | onset shape와 정보량에 의해 선택 |
| $\tau$ | time | 각 transit 단계 평균 통과 시간 | 하류 신호 전달 지연 |
| $1/\tau$ | $\text{time}^{-1}$ | 단계 전달 속도 | transit time의 역수 |

💡 **비유:** Transit chain은 릴레이 경주와 같습니다. 첫 주자가 움직여도 결승선의 반응은 마지막 주자가 도착할 때까지 늦게, 그리고 S자형으로 나타납니다.


관찰된 반응은 *연쇄의 최종 하류 상태*입니다: $R_{obs}=R_n$.

$$
\underbrace{R_{obs}}_{\text{관찰 반응}}=\underbrace{R_n}_{\text{최종 transit}}
$$

 여기서 지연되는 것은 *약물의 이동*이 아니라 *반응 신호(response signal)의 전달*입니다. 따라서 Link 모델의 "약물이 부위에 도달했는가" 질문과 신호전달 모델의 "신호가 측정 지점에 도달했는가" 질문은 *서로 다릅니다*.


### C. PD35 앵커 — onset 지연과 $n$ 선택

PD35는 건강한 남성 지원자에서 3가지 용량 수준(기저 저용량 $C_0=1.05$ nmol/L, 4배, 16배)을 사용한 사례 연구입니다. $K=0.0228\ \text{h}^{-1}$이며 반감기는 약 30시간입니다 [G&W pp.910–914]. 단순한 1-state 간접반응 모델로는 15–20시간의 onset 지연을 재현하기에 역부족이었습니다. 따라서 반응을 설명하려면 *신호전달 연쇄(transduction chain)*가 필요했습니다 [G&W p.323, pp.910–914].

Table 35.1은 모델 비교 시퀀스를 보여줍니다 [G&W p.914]:

| 신호전달 단계 수 | $EC_{50}$ | $E_{max}$ | $\tau$ (h) | $E_0$ | WRSS |
|---:|---:|---:|---:|---:|---:|
| 1 | 0.33 | 7.2 | 20 | 15 | 1319 |
| 2 | 0.34 | 6.0 | 13 | 18 | 789 |
| 3 | 0.35 | 5.4 | 9.8 | 19 | 642 |
| 4 | 0.35 | 5.1 | 7.8 | 20 | 632 |
| 5 | 0.34 | 4.8 | 6.4 | 20 | 682 |

$n=3$은 **기전적 진실(mechanistic truth)**이 아니라 **실용적 충분성(practical sufficiency)**으로 이해해야 합니다. $n=4$는 WRSS를 약간 더 낮추지만, $n=5$에서는 오히려 악화됩니다. 이 패턴은 실제 생물학적 신호전달 단계 수가 아니라 데이터셋의 *정보 수용 한계(information-capacity ceiling)*를 보여줍니다.

또한 $EC_{50}$와 $E_0$가 $n$에 거의 무관(robust)하다는 점, 그리고 $n \times \tau \approx$ 상수라는 trade-off(총 transit time은 거의 일정, 분할 방식만 다름)는 모델 파라미터화에 두 가지 안전감을 동시에 줍니다 [G&W p.914].

$$
\overbrace{n\times\tau}^{\text{총 지연}}\approx \text{상수},\qquad \underbrace{EC_{50},\ E_0}_{\text{민감도/기저스케일}}\approx \text{n 변화에도 안정}
$$

> **실무 시각(Practice Lens) — [CRUCIBLE_DERIVED]**  
> PD35의 $n$ 선택은 "진짜 생물학적 단계 수를 맞혔다"는 선언이 아니라, *현재 데이터가 구분 가능한 지연 구조의 해상도를 읽는 작업*입니다. $n=3$ 이후 WRSS 이득이 작고 $n=5$에서 악화되면, 추가 cascade 디테일은 설명력보다 불안정성을 더할 수 있습니다.


**현장 팁(Trench-Level Tip):** "가장 낮은 WRSS"만으로 $n$을 선택하지 마세요. PD35의 $1319\to789\to642\to632\to682$ 시퀀스가 말해주는 것은 분명합니다. 모델은 1단계보다 더 필요하고, $n=3$이면 실용적으로 충분하며, 데이터는 정확한 cascade 깊이를 *해상하지 못합니다*.



### D. 구조적 직관

1개의 1차 지연(first-order delay)은 $t=0$에서 즉시 반응을 시작합니다. Transit chain은 물질이 순차적 상태를 통과해야 하므로 가시적 반응이 나타나기까지의 시간이 지연됩니다. [구조적 비유 — 교과서 외 확장] 수학적으로는 동일한 지수 대기시간(exponential waiting time)들의 합이 *Erlang형 지연*과 닮아 있어, 지연되고 더 가파른 onset 형상을 설명합니다. 이 비유는 학습 보조 수단으로만 유지되며 교과서적 주장이 아닙니다.


### E. 경계 조건

- 각 단계에서 $\tau$를 동일하게 놓는 것은 *식별가능성(identifiability)*을 확보하기 위한 단순화 가정입니다.
- $n$과 $\tau$는 trade-off 관계입니다. 단계 수를 늘리면 단계당 $\tau$를 줄일 수 있고 전체 지연은 비슷하게 유지됩니다.
- 이 연쇄는 *반응 전파(response propagation)*를 기술하지, *약물 분포(drug distribution)*를 기술하지 않습니다. 분포 지연은 상류에 별도로 존재하여 여전히 $C_e$를 요구할 수 있습니다.
- [구현 번역] ODE 소프트웨어에서 이 연쇄는 순차적 1차 ODE로 구현됩니다. 정확한 NONMEM syntax는 이 핸드아웃 범위 밖입니다.


---



### E. 핵심 요약 박스

> **Card 4 체화 핵심**
> ① `onset이 즉각적 지수형이 아니라 delayed sigmoid일 때` → transit chain $n\times\tau$가 결정한다.
> ② `단일 turnover가 early/late residual을 남길 때` → 하류 신호 단계 $R_1,\ldots,R_n$이 지배한다.
> ⚡ `$n$ = 실제 생물학 단계 수` → 과해석과 과모수화로 이어져 정보 한계를 넘긴 모델을 정당화하게 된다.


<!-- SLIDE_START: §5 | title: §5 — 혼동 쌍 해부 -->
# §5 — 혼동 쌍 해부

> **V3 재구성 노트 — [EXPERT_INFERENCE, v3]**  
> §5는 *5쌍의 혼동 쌍(confusion pair)*으로 재구성되었으며, 각 쌍은 단순한 재진술이 아니라 *구별이 생기는 이유*를 인코딩하는 구조적 *기억 고리(Memory Hook)*에 앵커됩니다. *치명적 타격(Critical Blow)*은 Pair 1에 유지됩니다. 내성(Tolerance) vs 반동(Rebound) — 동일한 Moderator 방정식의 두 phase — 은 v3에서 *혼동 쌍이 아닙니다*. 그 기전적 관계는 Card 3 §C/§D에 AUC 비대칭 시그니처와 함께 정착됩니다. 대신 v3 §5는 *내성 vs 적응(Tolerance vs Adaptation, Pair 4)*을 묻는데, 이는 더 깊은 개념적 축(시스템 피로 vs 항상성 재보정)을 탐사합니다.

---


## Pair 1 — $k_{e0}$ vs $k_{out}$ vs $k_{off}$

| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | $k_{e0}$: $\text{time}^{-1}$ | $k_{out}$/$k_{off}$: $\text{time}^{-1}$ |
| 수식 내 위치 (분자/분모/지수) | $dC_e/dt$의 plasma–biophase 평형화 항 | turnover 소실항 또는 receptor dissociation 항 |
| 변화 원인 (생물학적/병적) | 분포 지연과 effect-site equilibration | system turnover 또는 receptor-ligand 해리 |
| 혼동 시 임상 결과 | 모든 delay를 link로 처리 | recovery, washout, 반복투여 행동 예측 실패 |


| 차원 (Dimension) | $k_{e0}$ | $k_{out}$ | $k_{off}$ |
|---|---|---|---|
| 무엇의 시계인가? | Plasma–생체상 평형 | 내인성 반응-시스템 회전 | 수용체-리간드 해리 |
| 대표 모델 | 효과구획(effect compartment) | 간접반응(indirect response)/turnover | 수용체 결합(receptor binding) |
| 단위 | $\text{time}^{-1}$ | $\text{time}^{-1}$ | $\text{time}^{-1}$ |
| 혼동 이유 | 단위가 같고 때로 크기가 비슷 | 유사한 이력현상 형태 | 유사한 single-dose fit |
| PD21 값 | 0.025 $\text{min}^{-1}$ | 0.031 $\text{min}^{-1}$ | 0.018 $\text{min}^{-1}$ [G&W p.846] |
| 식별자(Discriminator) | 선형 PK 하의 $t_{max}$와 loop collapse | 회전/회복 및 반복 투여 행동 | 결합/washout 행동과 표적 정보 |

**⚡ 기억 고리(Memory Hook) — *다리 통행 속도 vs 수조 배수 속도 vs 빗장 풀림 속도*:** [EXPERT_INFERENCE, v3]  
$k_{e0}$는 plasma와 effect site 사이 **다리의 통행 속도**입니다 — 약이 effect site에 도달하는 rate입니다. $k_{out}$은 response pool의 **수조 배수 속도**입니다 — system이 response를 잃는 rate입니다. $k_{off}$는 receptor-ligand의 **빗장 풀림 속도**입니다 — drug-target bond가 해체되는 rate입니다. 세 시계가 같은 단위를 가져도 *대상이 다릅니다* — 다리, 수조, 빗장입니다. PD21에서 세 값이 $0.025/0.031/0.018\ \text{min}^{-1}$로 비슷한 것은 우연이지 동치가 아닙니다. Single-dose data로는 셋을 구분하지 못하므로 dose stratification, repeated dosing, washout 같은 *richer design*이 필요합니다.

**치명적 타격(Critical Blow) — 정정:** G&W §3.9.7은 *회전(turnover) 데이터를 분포/link 모델로 피팅하면 생물학적으로 비현실적인 dose-dependent $EC_{50}$/$E_{max}$/$n$이 생길 수 있다*고 경고합니다 [G&W pp.271–272]. 
> 💼 **실무 인사이트:** 모델 정당화 상황에서 이 패턴은 대안 모델 비교와 민감도 분석 요구로 이어집니다. 단, 교과서 자체는 특정 규제 결과를 단언하지 않습니다.

---


## Pair 2 — 효과구획 모델 vs 회전/간접반응 모델

| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | $C_e$ 농도 상태 | $R$ 반응 pool 상태 |
| 수식 내 위치 (분자/분모/지수) | $dC_e/dt=k_{e0}(C-C_e)$ | $dR/dt=k_{in}S(C)-k_{out}R$ |
| 변화 원인 (생물학적/병적) | drug distribution delay | system turnover delay |
| 혼동 시 임상 결과 | dose-invariant delay를 과신 | dose-dependent response timing과 carry-over 누락 |


| 차원 (Dimension) | 효과구획(Effect compartment) | 회전/간접반응(Turnover, indirect response) |
|---|---|---|
| 지연의 출처 | 약물이 effect site로 *느리게 이동* | 약물은 즉시 작용하지만 *반응 변수*가 느리게 변함 |
| 숨은 상태 | 생체상 농도 $C_e$ | $k_{in}/k_{out}$이 지배하는 반응 풀(pool) $R$ |
| 구동 관계식 | $dC_e/dt = k_{e0}(C - C_e)$ | $dR/dt = k_{in}\,S(C) - k_{out}\,R$ |

$$
\underbrace{\frac{dC_e}{dt}=k_{e0}(C-C_e)}_{\text{Ce 지연}}\quad \text{vs}\quad \underbrace{\frac{dR}{dt}=k_{in}S(C)-k_{out}R}_{\text{R turnover 지연}}
$$
| 용량 스케일링 검사 | 선형 PK 하 모든 용량에서 동일한 반응 $t_{max}$ [G&W p.264] | $k_{out}$은 고정이고 $S(C)$만 변하므로 반응 $t_{max}$가 용량에 따라 이동 |
| 반복 투여 행동 | 단일 $k_{e0}$로 loop가 collapse됨 | 풀이 reset되지 않으면 메모리 carry-over 가능 |
| 해당 위치 | G&W §3.9, PD20/PD21 | G&W §3.10–3.11, PD13/PD20 |

**⚡ 기억 고리(Memory Hook) — *분포 지연 vs 시스템 지연*:** [EXPERT_INFERENCE, v3]  
Effect compartment는 약이 **distribution 지연** 때문에 effect site에 늦게 도달하는 모델입니다 — plasma와 effect site 사이의 *약물 이동*이 rate-limiting입니다. Turnover는 약이 **생물학적 시스템의 response dynamics** 때문에 효과가 느리게 나타나는 모델입니다 — 약은 즉시 작용하지만 *response pool*이 천천히 바뀝니다. 핵심 진단 질문은 하나입니다: **투여량을 올리면 response peak의 timing이 달라지는가?** 달라지면 effect compartment는 깨집니다(분포 지연은 dose에 무관해야 하기 때문). 달라지지 않으면 turnover의 가능성이 높습니다(turnover는 $S(C)$가 커져도 peak shape 변화가 있지만 *분포 시계*는 영향받지 않음).

---


## Pair 3 — 반시계방향 vs 시계방향 이력현상

| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | Counterclockwise loop 방향 | Clockwise loop 방향 |
| 수식 내 위치 (분자/분모/지수) | 시간-짝지은 phase-plane 경로 | 시간-짝지은 phase-plane 경로 |
| 변화 원인 (생물학적/병적) | response delay, distribution, turnover, binding | tolerance, antagonist metabolite, input-rate artifact |
| 혼동 시 임상 결과 | 모든 CCW를 link로 고정 | 모든 CW를 tolerance로 고정 |


| 차원 (Dimension) | 반시계방향(Counterclockwise) | 시계방향(Clockwise) |
|---|---|---|
| 시각적 의미 | 반응이 농도보다 지연 | 반응이 농도 대비 약화·역전 |
| 같은 농도, 두 방문 | 두 번째(나중) 방문에서 *더 강한* 효과 | 두 번째(나중) 방문에서 *더 약한* 효과 |
| 흔한 기전 | 분포 지연, 시스템 회전, 느린 결합, 동조성 대사체 | 내성, 길항성 대사체, down-regulation, *입력 속도 아티팩트* |
| 예시 | Naproxen/digoxin/warfarin 논리 [R&T pp.234–246] | Cocaine/nitroglycerin 형 내성 논리 [G&W pp.284–296]; 느린 생체상으로의 빠른 IV bolus [R&T p.236] |
| 진단 수순 | 먼저 $k_{e0}$ 기반 loop collapse 시도 | 반복 투여 패턴 확인; 내성 확정 전 입력 속도 아티팩트를 배제 |
| 과독(overread) 시 오류 | 모든 지연을 Link로 처리 | 모든 약화를 단일 내성 기전으로 처리 |
| 올바른 사용 | 첫 진단 단서 | 첫 진단 단서 |

**⚡ 기억 고리(Memory Hook) — *먼저 오는 것이 무엇인가*:** [EXPERT_INFERENCE, v3]  
Counterclockwise hysteresis는 같은 농도에서 **나중 방문에 더 강한 효과**를 보입니다 — 약이 effect site에 늦게 도달하거나(effect compartment), turnover로 response가 누적되기 때문입니다. Clockwise hysteresis는 같은 농도에서 **나중 방문에 더 약한 효과**를 보입니다 — tolerance, acute desensitization, 또는 antagonistic metabolite formation이 후보입니다. 방향은 *"같은 concentration이라는 약속 장소에 두 번 들렀을 때, 두 번째 방문에서 더 환영받는가(CCW) 아니면 덜 환영받는가(CW)"*로 기억하면 됩니다. Loop direction 자체는 mechanism을 결정하지 않습니다. *후보 가족*만 좁힐 뿐입니다.

---


## Pair 4 — 내성 vs 적응

| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | Tolerance: response capacity 변화 | Adaptation: homeostatic setpoint 재보정 |
| 수식 내 위치 (분자/분모/지수) | moderator $M$ 또는 desensitization state | negative feedback/setpoint 항 |
| 변화 원인 (생물학적/병적) | receptor down-regulation, mediator depletion 등 | physiological feedback, homeostasis |
| 혼동 시 임상 결과 | rebound·느린 회복 누락 | 일시적 재보정을 장기 내성으로 과해석 |


| 차원 (Dimension) | 내성(Tolerance) | 적응(Adaptation) |
|---|---|---|
| 기저 기전 | 시스템 *피로* — 수용체 down-regulation, 매개체 고갈, cofactor 소진 | 항상성 *재보정* — 생리학적 되먹임이 기저치 회복 |
| 가역성 | 약물 washout 이후에도 지속될 수 있음 (느린 회복) | 약물 노출 종료 시 즉각 역전 |
| 필요한 모델 요소 | 반응에 따라 자라는 숨은 상태 $M$ (조절자, Moderator) | 시스템이 정의한 setpoint를 갖는 음의 되먹임 루프 |
| 시간적 시그니처 | *지속* 노출 동안 점진적 효과 감소 | *지속* 노출 *중*에도 반응이 기저치로 접근 |
| 진단적 분리 | 약물 중단; 느린 역전 또는 반동 관찰 | 약물 중단; 반동 없이 빠른 복귀 관찰 |
| 해당 위치 | G&W §3.11, PD13 (Moderator) [G&W pp.297–300, 805–809] | G&W §3.11 개념적 대비; 다수 생리학적 시스템 |

**⚡ 기억 고리(Memory Hook) — *피로 vs 재보정*:** [EXPERT_INFERENCE, v3]  
Tolerance는 같은 노출에서 시간이 지날수록 효과가 줄어드는 **시스템 피로**입니다 — 약에 대한 반응 capacity가 둔화됩니다. Adaptation은 생리학적 homeostasis로 인해 반응이 기저치로 돌아오려는 **재보정** 과정입니다 — 시스템이 새로운 setpoint로 적응합니다. 두 현상이 겹치는 경우도 있으나, **tolerance는 약 노출이 없어져도 지속될 수 있고, adaptation은 노출 제거 시 바로 역전됩니다**. 이 reversibility 차이가 데이터에서 둘을 구분하는 가장 강한 신호입니다.

---


## Pair 5 — 단일 효과구획 링크 vs 신호전달 연쇄

| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | 단일 $C_e$ 상태 | $R_1,\ldots,R_n$ transit states |
| 수식 내 위치 (분자/분모/지수) | 1개 first-order smoothing ODE | $n$개 sequential first-order ODE |
| 변화 원인 (생물학적/병적) | distributional equilibration | downstream signal propagation |
| 혼동 시 임상 결과 | delayed sigmoid onset 과소적합 | $n$을 생물학 단계 수로 과해석 |


| 차원 (Dimension) | 단일 $k_{e0}$ link | Transit chain $n\times\tau$ |
|---|---|---|
| 지연되는 상태 | 생체상의 약물 농도 ($C_e$) | 하류 생물학적 반응 상태들 ($R_1, \ldots, R_n$) |
| ODE 형태 | 1개의 1차 평활화(smoothing) ODE | 순차적 1차 연쇄 ($n$개 방정식) |
| Onset 형상 | 즉각적 평활 접근 ($t=0$에서 최대 기울기) | 지연된 시그모이드형 전파 ($t=0$에서 기울기 0) |
| 핵심 진단 | 선형 PK 하의 동일한 $t_{max}$ | $n=1$이 지연된 onset을 피팅하지 못함; $n=1\to3$에서의 WRSS 급락 |
| 앵커 | G&W §3.9, PD20 | G&W §3.13, PD35 (Table 35.1: $n=1,2,3$에 대해 WRSS $1319\to789\to642$) |

**⚡ 기억 고리(Memory Hook) — *릴레이 경주 vs 단거리 경주*:** [EXPERT_INFERENCE, v3]  
Transduction chain은 신호가 여러 중간 단계(transit compartments)를 거쳐 효과에 도달하는 **릴레이 경주**입니다 — 각 선수(compartment)가 시간을 소모합니다. Single effect compartment는 plasma에서 effect site로 직접 이동하는 **단거리 경주**입니다. 릴레이는 단거리보다 *늦게 시작*하고(첫 선수가 출발선 떠날 때까지 다음 선수는 가만히 있음 — 이것이 zero slope at $t=0$의 정체), relay 선수 수가 많을수록 onset의 sigmoidal sharpness가 커집니다. **Transduction이 필요한 신호는 다음과 같습니다: 용량이 커져도 onset의 *형상*(sigmoidal sharpness)이 유지되며, 단순한 first-order curve로 fit하면 early phase residual이 S-curve로 누적됩니다(§6 Signature 3).**

---



# §6 — 거장의 진단 렌즈(GOF 시그니처 사전)

> **소스 경계 주의(Source-boundary note) — [EXPERT_INFERENCE | TEXTBOOK_DERIVED]**  
> 아래 네 가지 명명된 시그니처는 교과서 앵커와 Crucible-Grade-B 전문가 리뷰에서 도출된 *교육용 기억술(mnemonic)*이다. *패턴*은 교과서 데이터(G&W §3.9.7, PD13, PD35)와 표준 NONMEM 진단 플롯에서 관찰 가능하나, *이름*은 교육적이며 교과서의 직접 명명이 아니다. NONMEM 특정 구현 언어는 의도적으로 최소화되었다.

피팅이 수렴했지만 뭔가 맞지 않는 느낌이 들 때, re-parameterization 전에 데이터를 다음 네 가지 진단 렌즈에 통과시켜라. 각 렌즈의 메시지는 단 하나다: "이 패턴이 보이면, 모델 트리아지의 다음 escalation은 X다."


### Signature 1 — $EC_{50}$ 용량 분기 패턴($EC_{50}$ dose-bifurcation pattern)

- **관찰 패턴:** 모델을 용량별로(individual fits) 피팅하면 $EC_{50}$, $E_{max}$, $n$ 값이 용량군 간에 *기전적 정당화가 없는* 방향이나 크기로 크게 변동한다.
- **기계론적 의미:** Link 모델이 회전/적응(turnover/adaptation) 효과를 강제로 흡수하고 있습니다. 모델링되지 않은 동역학을 보상하기 위해 $EC_{50}$이 *이동(migrate)*합니다.
- **교과서 근거:** G&W §3.9.7 Table 3.10 — dose-stratified $EC_{50}$가 0.681, 4.85, 0.941(약 7배 분산); simultaneous fit에서 체계적 편차가 나타납니다 [G&W p.271].
- **다음 단계:** Link → 간접반응(turnover)으로 이동하세요. *단일 $EC_{50}$이 회복되는지* 검증하면 됩니다.


### Signature 2 — Trough drift / carry-over 패턴

- **관찰 패턴:** 반복 투여 데이터에서, 노출(AUC)이 비슷한데도 *2번째 cycle 종료 시 trough가 1번째 cycle 종료 시 trough와 다릅니다*. 연속된 trough들이 같은 방향으로 깊어지거나 이동합니다.
- **기계론적 의미:** 숨은 상태(hidden state)가 cycle 간에 *메모리를 운반*하고 있습니다. 내성/반동 시스템에서는 다음 투여가 도착하기 전에 조절자 $M$이 완전히 washout되지 않습니다.
- **교과서 근거:** G&W p.808은 PD13의 2번째 투여 trough가 첫 번째와 같지 않음을 명시하며, 이것이 조절자 활성화의 시그니처임을 진술한다 [G&W pp.805–809].
- **다음 단계:** 간접반응 → 조절자(Moderator, Model II)로 이동; AIC/WRSS를 비교하고 $k_{tol}/k_{out}$ 비율을 확인하세요.


### Signature 3 — 지연된 onset / S자형 onset 잔차 패턴

- **관찰 패턴:** 긴 onset 지연을 가진 데이터에 단일 회전(single-turnover, $n=1$) 간접반응 모델을 피팅합니다. 모델은 반응이 *너무 일찍* 상승한다고 예측하지만, 데이터는 더 늦게, 더 급격히 상승합니다. 시간에 따른 잔차가 onset 부근에서 *under-then-over-then-under* 패턴을 형성합니다.
- **기계론적 의미:** 단일 1차 지연으로는 평탄한 초기 phase 뒤에 급격한 상승을 만들어낼 수 없습니다. *순차적 transit compartments*가 필요합니다.
- **교과서 근거:** PD35 Table 35.1 — WRSS가 1319 ($n=1$) → 789 ($n=2$) → 642 ($n=3$)로 감소합니다. $n=1$ vs $n=3$은 약 2배 개선이며, 이는 onset 형상이 단일-회전이 아니라 *cascade에 의해* 생성된다는 신호입니다 [G&W p.914].
- **다음 단계:** 간접반응 → transit chain으로 이동하세요. 절약 원칙(parsimony)에 따라 데이터가 지지하는 $n$을 선택하세요.


### Signature 4 — OFV / WRSS plateau 패턴

- **관찰 패턴:** 구조적 시퀀스를 따라 모델 복잡도를 에스컬레이션하면(예: $n=1,2,3,4,5$ transit compartments; 또는 single → moderator → moderator+M50), OFV 또는 WRSS가 개선된 뒤 *plateau*에 도달하고, 이후 *소폭 악화*를 보입니다.
- **기계론적 의미:** 데이터가 해당 기전에 대해 *정보 수용 한계(information-capacity ceiling)*에 도달했습니다. 추가 파라미터는 더 이상 구조를 포착하지 못하고 *잡음을 흡수*하기 시작합니다.
- **교과서 근거:** PD35 시퀀스 1319 → 789 → 642 → 632 → 682 ($n=1\to5$). 642→632 단계는 작고, 632→682는 *악화*이며, 이는 $n=3$ 또는 $n=4$를 넘는 *과적합(over-parameterization)*을 시사합니다 [G&W p.914].
- **다음 단계:** 에스컬레이션을 *멈추세요*. 절약 원칙이 지지하는 모델을 선택하세요. *데이터가 더 미세한 구조를 해상하지 못한다*는 사실을 문서화하면 됩니다.

> **거장의 시각(Mastery Lens) — [EXPERT_INFERENCE | SOURCE-AWARE]**  
> 네 시그니처는 모델 오설정(misspecification)의 *서로 다른 위치*를 가리킵니다 — Signature 1은 *모델 패밀리 선택*의 오류, Signature 2는 *반복 노출 메모리*의 누락, Signature 3은 *cascade 깊이*의 부족, Signature 4는 *데이터 해상도* 한계입니다. 이 네 패턴을 구분하지 못하면, 잘못된 한 개 패치(예: 재모수화, re-parameterization)로 다른 시그니처를 덮으려 하다가 모델이 오히려 손상됩니다.

---



<!-- SLIDE_START: §7 | title: §7 — 자기점검: 능동 회상 모듈 -->
# §7 — 자기점검: 능동 회상 모듈


## Q1 — 회상
효과구획 ODE를 쓰고, $k_{1e}=k_{e0}$이 사용되는 이유를 서술하세요.

**정답:** $dC_e/dt=k_{e0}(C-C_e)$ [G&W pp.268–269]. 이 등식은 보편적 물리 법칙이 아니라 *식별가능성(identifiability) 기반의 표준 단순화*입니다 [G&W pp.263, 265].

---


## Q2 — 적용
3개 용량 연구에서 모든 용량의 반응 $t_{max}$가 동일하게 관찰되었다. 즉시 Link 모델을 선택해도 되는가?

**정답:** 아니오. 먼저 *선형 PK*를 검증하세요. Same-$t_{max}$ 성질은 선형 약물 동태 가정 하에서만 진술됩니다 [G&W p.264]. 그 다음 dose-stratified PD 파라미터의 정합성과 모델 적합을 확인하세요.

---


## Q3 — 오류 탐지
어떤 초안에 "PD13 Table 3.10이 Link 오설정 하의 $EC_{50}$ 용량 분기를 보여준다"고 적혀 있습니다. 이를 정정하세요.

**정답:** "G&W §3.9.7 Table 3.10 link-model pitfall; Fig.3.59는 PD12 데이터이다"로 정정해야 합니다. PD13은 *반복 IV infusion 내성/반동 모델 비교 사례*입니다 [G&W pp.271, 805–809].

---


## Q4 — 기전 트리아지
농도-반응 플롯이 반시계방향입니다. 가능한 기전 3가지와 각각에 대한 *추가 식별자(discriminator)* 1개씩을 나열하세요.

**정답:** 분포 지연 → 선형 PK 하 $t_{max}$ 용량 불변성 검사 + $k_{e0}$ 기반 loop collapse 시도; 회전 지연 → peak shift와 시스템 회복 시간 확인; 느린 결합 → 표적/결합 또는 washout 행동 검사입니다. 대사체 기여는 대사체 농도/약리 데이터가 필요합니다.

---


## Q5 — PD13 추론
PD13에서 Model II는 $k_{in}=30$, $k_{out}=2.9$, $k_{tol}=4.2$, $EC_{50}=350$, $E_{max}=9.8$, $n=7.4$, $AIC=-97.5$, $WRSS=0.083$를 보고하며, Model I(되먹임 없음, $AIC=-39.0$)과 Model III(pool, $AIC=-43.5$)보다 우수합니다. AIC를 넘어서, *Model II를 기전적으로 옳은 답으로 만드는 단 하나의 파라미터 관계*는 무엇입니까?

**정답:** $k_{tol}=4.2 > k_{out}=2.9$, 즉 *조절자 발달이 반응 회전보다 빠르다*는 점입니다. 이 부등식은 단일 infusion *내에서도* 내성이 가시화됨을 예측하며, 2번째 cycle에서 carry-over/trough-drift가 관찰되도록 만드는 핵심입니다 [G&W p.808]. Model III의 $k_{tol}=0.05$는 관찰된 패턴에 대해 *생물학적으로 비현실적*입니다.

---



## Q6 — PD21 추론
$k_{e0}$, $k_{out}$, $k_{off}$가 모두 $\text{min}^{-1}$ 단위에 비슷한 크기라는 이유만으로 *동일한 의미*라고 결론짓는 것이 안전하지 않은 이유는?

**정답:** 셋은 *서로 다른 물리적/생물학적 시계*를 가리킵니다 — 생체상 평형, 시스템 회전, 수용체 해리. PD21은 유사한 값(0.025, 0.031, 0.018 $\text{min}^{-1}$)을 보고하지만 *서로 다른 기전 모델*을 비교합니다 [G&W p.846].

---


## Q7 — PD35 추론
PD35 Table 35.1은 $n=1\to5$에 대해 WRSS $1319\to789\to642\to632\to682$를 보여 줍니다. WRSS가 가장 낮다는 이유만으로 단순히 $n=4$를 선택하면 안 되는 이유는 무엇입니까?

**정답:** $n=4$는 $n=3$ 대비 미미한 개선(642→632)에 그치며, $n=5$에서는 *악화*(632→682)됩니다. 이 패턴은 $n=3$ 부근에서 *실용적 충분성*과 *정보 수용 한계*에 도달했음을 시사합니다. $n=3$은 절약 원칙이 지지하는 선택이며, $n=4$가 "더 좋은" 모델이라고 선언하는 것은 *데이터가 해상하는 것 이상을 주장*하는 것입니다 [G&W p.914].

---


## Q8 — 보스 딜레마, 압축형
모델 A는 안정적인 Link 모델이지만 dose-dependent EC50을 만들어낸다. 모델 B는 계산적으로 덜 안정하지만 *생물학적으로 정합적인 단일 EC50*를 유지하고 내성도 포착한다. 어떤 원칙이 선택을 지도하는가?

**정답:** *기전적 타당성(mechanistic validity)이 통계적 편의성에 우선한다*. 기전 없이 dose-dependent 수용체 민감도를 함의하는 모델은 G&W §3.9.7 함정(§6 Signature 1 참조)을 반복한다. 계산적 불안정성은 *기술적 문제*지만, 생물학적으로 비현실적인 파라미터 행동은 *모델 타당성 문제*다.

---


## Q9 — 율속 단계 비교 (R&T 앵커)
Acenocoumarol(plasma $t_{1/2} \approx 15$ h)과 phenprocoumon(plasma $t_{1/2} \approx 5$ days)은 동일 표적(응고 인자 합성 억제)에 작용하지만, *기저치 회복 시간*은 약 한 자리수 차이가 납니다. 각 약물의 회복을 율속(rate-limit)하는 단계는 무엇입니까?

**정답:** 회복은 (i) 약물 제거(kinetics)와 (ii) 응고 인자 회전(dynamics) 중 *더 느린 과정*에 의해 율속됩니다 [R&T Ch.8, Fig.8-11]. Acenocoumarol에서는 약물 청소(clearance)가 빠르고 응고 인자 회전($t_{1/2} \approx 1{-}2$ days)이 율속이 되어 회복 시간이 *동역학(dynamics)에 의해 제한*됩니다. Phenprocoumon에서는 약물 청소 자체가 가장 느린 단계($t_{1/2} \approx 5$ days)이므로 회복 시간이 *동태(kinetics)에 의해 제한*됩니다. Warfarin($t_{1/2} \approx 1.5$ days)은 경계에 위치하며, 이는 warfarin 용량 적정이 임상적으로 *민감한* 구조적 이유 중 하나입니다.

---


## Q10 — 환자 간 이력현상 변이
동일 약물을 투여받은 두 환자에서 이력현상 루프가 관찰된다. 환자 A의 루프는 반시계방향, 환자 B의 루프는 시계방향이다. 이 세션의 프레임워크에 근거한 두 가지 그럴듯한 설명을 나열하세요.

**정답:** (1) **두 가지 기전이 서로 다른 상대적 우세도로 동시에 작동.** 분포 지연과 내성이 모두 기여할 때, 관찰 가능한 방향은 *관찰 창(observation window) 동안 어느 쪽이 우세한가*에 달려 있다 — 환자 A는 주로 분포 지연 phase에서, 환자 B는 주로 내성 phase에서 샘플링되었을 수 있고, 더 긴 관찰은 양쪽 모두에서 *8자형*을 드러낼 수 있다. (2) **입력 속도 vs 분포 속도 불일치.** R&T는 *약물 입력 속도가 분포 또는 내성 발달 속도보다 빠를 때*에도 시계방향 루프가 나타날 수 있음을 명시한다 [R&T p.236]; 환자 간 경구 흡수 속도, infusion 속도, 또는 first-pass 동태 차이는 *기저 기전이 다르지 않아도* 겉보기 방향을 뒤집을 수 있다.

---


## ⚡ Q11 — 보스 딜레마(보스 딜레마(Boss Dilemma)) ★★ [EXPERT_INFERENCE, v3]

반시계방향 이력현상(counterclockwise hysteresis)이 PD 데이터에서 명확히 관찰되었습니다. PK는 선형(linear)이고, 샘플링(sampling)은 충분하며, 3개 용량 수준(dose levels)에서 일관된 CCW direction이 나타났습니다. 이제 두 가지 모델링 경로 사이에서 결정해야 합니다.

- **선택지 A — 효과구획(effect compartment) 모델($k_{e0}$ 추가).** 즉시 구현할 수 있고, 파라미터 집합(parameter set)이 간결합니다($k_{e0}$ 하나 추가). Card 2 §B-2의 hysteresis collapse method가 깨끗하게 작동하면 수치 $k_{e0}$를 확보할 수 있습니다. 단점은 $k_{e0}$가 용량 의존적으로 변하면 모델 정당성이 흔들리고, 반복투여 내성/반동(repeated-dose tolerance/rebound)을 *전혀* 설명하지 못한다는 점입니다.
- **선택지 B — Indirect response / turnover 모델 ($k_{in}, k_{out}, S(C)$).** Mechanism이 production/loss pathway 변화로 정당화되면 생물학적으로 더 의미 있다. Repeated-dose에서 trough drift나 carry-over가 있으면 Moderator로 자연스럽게 확장 가능. 단점: parameter 추정에 *더 넓은* 데이터가 필요 — single-dose만으로는 $k_{in}/k_{out}$이 $C_{baseline}=k_{in}/k_{out}$ 비율로만 결정되어 individually identifiable하지 않다.

**질문:** 각 선택을 *규제 문서*에서 어떻게 방어하는가?

> **정답 공개 — 거장의 Trade-off 논리**

**핵심 통찰: 어느 쪽을 선택하든, 답변의 70%는 "다른 쪽을 *왜 배제했는지*"이다.** 모델 선택은 *증명*이 아니라 *경쟁 가설의 체계적 기각*이다.

**선택지 A (Effect compartment)를 방어하는 경우:**
- (i) Hysteresis collapse method가 3개 용량 수준 모두에서 단일 $k_{e0}$ ±20%로 작동했다는 수치 근거(numerical evidence)를 제시합니다.
- (ii) 반복투여 데이터(repeated-dose data, 가능하면 ≥2 cycles)에서 *no trough drift*, *no rebound*를 보여 turnover/Moderator 가설을 기각합니다.
- (iii) PD13(G&W p.808) 같은 turnover-data 사례와의 *비교 피팅(comparison fit)*을 첨부합니다. 같은 데이터에 turnover 모델을 fit했을 때 $EC_{50}$ 용량 분기(§6 Signature 1) 또는 trough drift(§6 Signature 2)가 나타나지 *않음*을 보여 distribution 가설을 강화합니다.
- (iv) 기전(mechanism)이 그럴듯한지(plausible)를 확인합니다. 약물의 logP, 표적 조직 분배(target tissue partitioning), 관류(perfusion)가 distributional delay 가설과 *일관*되는지에 대한 생물학적 논거(biological argument)를 추가합니다.

**선택지 B (Indirect response)를 방어하는 경우:**
- (i) 약물의 알려진 mechanism이 receptor-mediated production/loss라는 *사전 생물학적 근거(prior biological evidence)*를 제시합니다(literature, in-vitro data, target identity).
- (ii) Effect compartment 모델을 *동일 데이터에* fit한 결과를 첨부하고, dose-stratified $k_{e0}$나 $EC_{50}$/$E_{max}$/$n$ migration(§6 Signature 1) 같은 misspecification 신호를 보여 distribution 가설을 기각합니다.
- (iii) Turnover model의 $k_{in}/k_{out}/S(C)$ identifiability를 위한 *experimental design*을 동반합니다(multiple doses, ideally washout phase 또는 endogenous baseline 측정).
- (iv) Repeated-dose data가 있으면 trough drift 또는 rebound asymmetry($AUC_R<AUC_E$) 관찰을 *명시적 양성 근거(explicit positive evidence)*로 첨부합니다.

**규제 reviewer가 둘 중 어느 하나를 *반드시 묻는* 질문:**  
> "왜 다른 모델이 아닌가?"

준비된 답이 없으면, 어느 모델이든 불충분한 정당화(inadequate justification)로 평가됩니다. 따라서 master modeler의 작업 흐름은 *처음부터 두 모델을 같이 fit하고*, *어느 하나가 명확히 우세한 evidence*를 만든 뒤 *그 evidence를 문서화*하는 것입니다. Fit 결과만 첨부하는 것으로는 충분하지 않습니다.

**현장 단서(Trench-level 단서):** 실제 Phase 1 환경에서 단회투여(single dose)만 있는 경우, A를 *잠정* 선택하되 Phase 1b/2 protocol에서 반복투여 확장(repeated-dose extension)을 미리 *계획*하세요. 그래야 향후 Moderator 가설로 escalate할 수 있는 evidence를 능동적으로 수집할 수 있습니다. 단회투여 effect compartment 모델은 그 자체로 unfalsifiable하기 때문입니다.

---


## Q12 — 제한된 샘플링에서의 메커니즘 판별 ★★ [EXPERT_INFERENCE, v3.4]

> **출처 경계 라벨:** [EXPERT_INFERENCE — mechanism discrimination patch; File 11의 discrimination crisis와 File 12의 hysteresis triage를 연결하기 위한 자기점검 보강]

**시나리오 (시나리오)**

신규 후보 약물의 단회투여(single dose) 임상시험 데이터를 받았습니다. 샘플링 설계는 비용·침습성 제약 때문에 *제한된 샘플링(limited sampling)*만 허용했고, 혈장 농도(plasma concentration)와 효과 표지(effect marker)를 각각 5개 시간점에서만 측정했습니다. 관찰 결과는 다음과 같습니다:

- 혈장 농도는 빠르게 peak에 도달한 뒤 단조 감소한다.
- 효과는 농도 peak보다 *늦게* peak를 보이며, 농도–효과 평면에서 명확한 *반시계방향 이력현상 고리(counterclockwise hysteresis loop)*가 관찰됩니다.
- 두 후보 모델을 동일 데이터에 적합시켰을 때 GOF(goodness-of-fit) 지표가 사실상 동등하다:
  1. **효과구획 모델(effect compartment model)** — $k_{e0}$로 생체상 지연(biophase delay)을 설명합니다.
  2. **간접반응 / 턴오버 모델(indirect response / turnover model)** — $k_{in}/k_{out}$ 또는 반응 풀 턴오버(response pool turnover)로 지연을 설명합니다.

**질문 (질문)**

이 상황에서 단순히 GOF가 비슷하다는 이유로 효과구획 모델을 잠정 선택하면 안 되는 *구조적 이유*는 무엇인가? 그리고 제한된 샘플링(limited sampling) 환경에서 두 메커니즘을 *판별*하기 위해 다음 연구·분석 설계에서 어떤 정보를 추가로 확보해야 하는가?

> **정답 공개 — 메커니즘 판별 논리**

**1. 반시계방향 고리(counterclockwise loop)는 단서이지 결정증거가 아니다.**  
CCW loop는 "효과가 농도보다 늦게 변한다"는 *현상*만을 보여줄 뿐, 그 지연이 *어디에서 오는지*를 결정하지 못합니다. Card 1 §E-2의 그럴듯한 오해(Plausible Fallacy)와 §6 진단 시그니처 사전(Master's Diagnostic Lens)이 가르치는 핵심은 동일합니다. 동일한 CCW 패턴은 효과구획·간접반응·신호전달연쇄(transduction chain) 등 5가지 이상 서로 다른 메커니즘에서 동일하게 생성됩니다.

**2. 효과구획 모델은 주로 *분포·생체상 지연(distributional / biophase delay)*을 설명한다.**  
즉 약물이 측정 가능한 혈장 구획(plasma compartment)에서 작용 부위(effect site)로 도달하는 데 걸리는 시간입니다. 이때 시계는 *약물 시계(drug clock)*이며, $k_{e0}$가 그 속도를 지배합니다(Card 1 hidden state: $C_e$).

**3. 간접반응·턴오버 모델은 *반응 시스템 자체의 생성·소실 속도* 때문에 지연이 생긴다.**  
약물은 plasma에서 즉시 작용하지만, 약물이 변화시키는 것은 내인성 반응 풀의 $k_{in}$ 또는 $k_{out}$입니다. 풀이 새로운 항정상태로 재평형하는 데 걸리는 시간이 *시스템 시계(system clock)*를 만듭니다. 이 경우 $t_{1/2,k_{out}}$이 지연의 본질입니다(Card 3 §B, Eq.3:204 [G&W p.299]).

**4. 제한된 샘플링에서는 모델 식별성(model identifiability)이 구조적으로 약하다.**  
단회투여 + 5개 시간점이라는 데이터 정보량은 두 모델을 *수치적으로* 분리할 만한 자유도를 주지 못합니다. 두 모델 모두 CCW loop와 단조 감소하는 농도 곡선을 *비슷한 RSS·OFV로 재현*할 수 있습니다. GOF만으로 잠그면 사실상 *데이터 식별성이 아니라 prior assumption*에 의해 모델이 결정됩니다. 이는 규제 검토에서 reviewer가 즉시 지적하는 결함입니다.

**5. 판별을 위해 다음 중 일부를 추가로 확보해야 한다.**

- **더 이른 시간점의 효과 샘플링(effect sampling)** — 농도 peak 이전에 효과가 *얼마나 빨리 움직이기 시작하는지*가 두 모델을 분리합니다. 효과구획 모델은 즉각적 출발 후 부드러운 ramp-up을, 턴오버 모델은 *느린 출발(lag-like onset)*을 예측합니다.
- **효과 peak 전후의 촘촘한 샘플링(dense sampling around effect peak)** — peak 시각 자체와 그 형상(둥근 vs 뾰족한)이 hidden state의 차수와 수를 시사합니다.
- **반복용량(repeated dose) 또는 다른 용량 수준(dose level)에서의 $t_{max}$, effect onset, recovery pattern 비교** — 효과구획 모델은 용량 변화에도 onset이 *변하지 않으며*, $k_{e0}$가 dose-independent해야 합니다. 턴오버 모델은 §6 Signature 1($EC_{50}$ 용량 분기), Signature 2(trough drift) 같은 진단 시그니처를 자연스럽게 만듭니다.
- **기저선 회복(baseline recovery)과 반동·내성(rebound / tolerance) 검사** — 효과구획 모델은 *비대칭 회복*을 설명하지 못합니다. $AUC_R < AUC_E$ 같은 비대칭(Card 3 §C, [G&W Fig.3.82])이 보이면 즉시 turnover/Moderator 쪽으로 escalation해야 합니다.
- **독립적 생리학적 지식(independent physiological knowledge)** — 표지 분자(biomarker)의 고유 턴오버 반감기, 생성·소실 속도, receptor 동태 같은 외부 정보입니다. 이 prior가 없으면 데이터만으로 hidden state를 명명할 수 없습니다.

**6. 결론 (결론 원칙)**  
> **Delay는 단순한 시간 지연항이 아니라 숨은 상태(hidden state)를 가리키는 신호이며, 그 숨은 상태가 biophase인지 response turnover인지 구분하는 것이 File 12의 핵심입니다.**

이 원칙은 §8 capstone "지연은 메커니즘이 아닙니다. 지연되는 상태에 이름을 붙이세요(A delay is not a mechanism. Name the delayed state.)"의 직접적 운영 형태입니다. File 11의 discrimination crisis(서로 다른 모델이 동일 데이터를 동등하게 설명하는 위기)와 File 12의 hysteresis triage(loop 방향만으로 잠그는 함정)를 잇는 자기점검입니다.


**좋은 답안의 최소 구조 (좋은 답안의 최소 구조)**

1. **Loop 방향 → 후보 메커니즘 나열** (CCW = 효과구획 OR 턴오버 OR 신호전달연쇄; 방향만으로는 결정 불가).
2. **GOF만으로 잠금 금지** (제한된 샘플링에서 두 모델은 모델 식별성(identifiability)이 약하므로 RSS·OFV 비교로 잠그면 prior에 의한 결정에 가깝다).
3. **추가 sampling/design으로 판별** (이른 시간점, peak 전후 dense sampling, 반복투여 또는 dose escalation, baseline recovery·rebound 검사, 독립적 생리학적 지식).

---



<!-- SLIDE_START: §8 | title: §8 — 메타 프레임과 큰 그림 -->
# §8 — 메타 프레임과 큰 그림


## A. PK/PD 지식 그래프에서의 위치

이 세션은 기본 $E_{max}$/Hill/간접반응 모델과 TMDD, PBPK-PD coupling, QSP 같은 고급 통합 PK/PD 시스템 *사이*에 위치합니다. 세 가지 *시계(clock)*의 구분을 가르칩니다:

1. **약물 시계(Drug clock):** 농도가 생체상에 도달하는 속도 — $k_{e0}$.
2. **시스템 시계(System clock):** 생리학적 반응이 생성·소실·적응하는 속도 — $k_{out}$/$k_{tol}$.
3. **신호 시계(Signal clock):** 측정 반응이 나타나기까지의 하류 단계 수 — $n \times \tau$.

| 후속 세션 | 이 세션에서 열리는 개념 | 이 세션 없으면 실패하는 것 |
|---|---|---|
| TMDD | binding/receptor state와 $k_{off}$ 해석 | $k_{e0}$·$k_{off}$ 단위 혼동 |
| PBPK-PD coupling | tissue/biophase delay와 system response 분리 | 조직분포와 생리학적 turnover 혼동 |
| QSP | downstream cascade와 feedback state 명명 | transit chain과 true biology 과해석 |


## B. 이 세션을 피상적으로 학습했을 때 발생하는 실패 모드

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| Link overuse | $k_{e0}$ | → | 용량 의존적 $EC_{50}$/$E_{max}$/$n$ | turnover/transduction 대안 비교 |
| Tolerance blindness | $M$, $k_{tol}$ | → | trough drift와 rebound 누락 | 반복투여·washout 자료 확인 |
| Cascade underfitting | $n\times\tau$ | → | delayed onset misprediction | transit chain 및 WRSS 변화 확인 |
| Over-parameterization | $n$, $\tau$ | → | 정보 한계를 넘은 기전 주장 | OFV/WRSS plateau와 identifiability 확인 |
| Unit-level confusion | $k_{e0}$/$k_{out}$/$k_{off}$ | → | 같은 단위의 다른 시계 혼동 | 파라미터가 지배하는 hidden state를 먼저 명명 |

(교차 참조: §6 거장의 진단 렌즈(Master's Diagnostic Lens)는 이 네 가지 시그니처를 명시적으로 명명합니다.)


## C. 전문가 해석 지점

지속적인 기술은 ODE를 외우는 것이 아닙니다. 핵심은 *피팅 전에* 데이터가 어떤 *숨은 상태(hidden state)*를 요구하는지 *보는 것*입니다: 숨은 **생체상 농도**, 숨은 **적응성 조절자(adaptive moderator)**, 또는 숨은 **신호전달 상태들(transduction states)**. 이 구분이 *수학적으로 수렴했지만 생물학적으로 비현실적인* PK/PD 모델을 막습니다.

> **거장의 시각(Mastery Lens) — [EXPERT_INFERENCE | SOURCE-AWARE]**  
> 세 모델군의 공통점은 모두 "시간 지연"을 설명한다는 점이고, 차이는 *지연되는 상태(delayed state)*의 정체입니다. 좋은 모델러는 rate constant의 *단위*를 먼저 보지 않고, 그 rate constant가 *무엇의 시계인지*를 먼저 묻습니다. 그리고 fit 결과에서 자기 모델이 §6의 네 시그니처 중 어느 하나를 만들어내고 있지는 않은지 — *수렴 이전에* — 검사합니다.

> **V3 capstone echo — [EXPERT_INFERENCE, v3]**  
> 각 §2 카드의 마지막 줄은 그 카드의 hidden state를 명시한다:
> - **Card 1:** 효과부위/생체상 농도(effect-site/biophase concentration) $C_e$
> - **Card 2:** loop direction이 가리키는 시간 지연의 정체(어느 hidden state로 escalation할지에 대한 진단 게이트)
> - **Card 3:** 조절자 상태(Moderator state) $M$(system memory; drug compartment 아님)
> - **Card 4:** 순차적 transit compartments $R_1, \ldots, R_n$
>
> 새 PK/PD 데이터를 받으면 이 네 hidden states 중 *어느 것이 작동 중인지*를 **수식 쓰기 전에** 결정합니다. ODE 선택은 *결과*이지 *시작*이 아닙니다.



---

# 출력 후 자가검증 체크리스트

| 항목 | 기준 | 결과 |
|---|---|---|
| SLIDE_START 개수 | §섹션수 + 카드수 합산 | 9개 |
| 카드당 callout 합계 ≤ 6 | 전체 카드 | ✓ |
| [E] 박스 존재 | 모든 §2 카드 | ✓ |
| [D] 거장의 시각 존재 | 모든 §2 카드 | ✓ |
| [L] 파라미터 표 존재 | Apex 카드 + 정의 수식 카드 | ✓ |
| §5 혼동 쌍 표 행 순서 고정 (4행) | §5 전체 | ✓ |
| 기호 일관성 | 첫 등장 기준 통일 | ✓ |
| PART B 흔적 없음 | 전체 | ✓ |
| 수치 anchor 보존 | Compound A 등 원본 수치 | ✓ |
| [M] 나비효과 이중 종착점 | Apex 카드 전체 | ✓ |

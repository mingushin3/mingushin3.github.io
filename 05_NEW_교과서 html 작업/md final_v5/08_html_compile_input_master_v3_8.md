# 08_HTML Compile Input Master — v3.8

## 출처 및 범위 노트

이 장은 Gabrielsson & Weiner의 비선형 PK 영역과 Rowland & Tozer Ch.16–17(nonlinearities/DDI)을 바탕으로 합니다. 다루는 범위는 **비선형 PK, Michaelis–Menten, mechanism-based inhibition, nonlinear binding, drug–metabolite model, DDI, mass-action equivalence triangle**입니다. `FIGURE_POINTER`는 교과서 원본 그림 확인 위치를 안내하는 텍스트입니다. 첨부 출처 밖의 규제 지침·CPIC·NONMEM 코드는 본문 근거로 쓰지 않습니다.

> 🎯 **이 세션의 한 줄 이유** — $AUC/Dose$로 선형성 실패를 먼저 잡고, capacity·time·binding·DDI로 갈라 들어가야 비선형 PK가 암기 목록이 아니라 판단 순서가 됩니다.

---
## PART A — Learner-Facing Complete Handout

## 임상 장면 — 왜 이 세션이 필요한가

Phenytoin을 **300 mg/day에서 500 mg/day**로 올렸더니 농도가 **4 mg/L에서 36 mg/L**로 뛰는 환자를 떠올려 보세요. 용량은 67% 증가했는데 농도는 **9배**가 됐습니다. 이건 단순한 "용량 비례 실패"가 아니라, **$R_0$가 $V_m$에 가까워질 때 정상상태 분모가 무너지는** 용량 한계 현상입니다. 이 장의 목적은 이런 장면을 보고 곧바로 **capacity / time / binding / DDI** 중 어느 병목을 의심해야 하는지 결정하는 감각을 만드는 것입니다. [T16 pp.491, 503–506]

## §1.5 빠른 읽기 경로

시간이 부족하면 **C1 → C2 → C3 → C5** 네 카드만 순서대로 읽어도 이 장의 의사결정 체계가 작동합니다. C4(결합)와 C6(복합 DDI)는 임상 상황에서 그 사례가 나타날 때 다시 펼쳐 읽는 카드입니다.

---

> 🎯 **이 세션의 첫 질문** — 비선형 PK의 첫 질문은 "선형이 깨졌는가?"가 아니라 **"$V_{max}/K_m$, $f_u$, $f_m$ 중 어떤 병목이 관측값을 흔드는가?"**입니다.

---

<!-- SLIDE_START: §1 | title: 세션 헤더 및 로드맵 -->

# §1. 세션 헤더 및 로드맵(Session Header & Roadmap)

이번 세션의 한 문장 핵심은 다음과 같습니다.

> **비선형 PK = "선형 중첩이 깨진 현상"이 아닙니다. 용량(capacity)·시간(time)·혈류(flow)·결합(binding)·상호작용(interaction) 중 어느 물리적 병목이, 농도·시간·투여 경로·환자 유전형과 결합해 비선형성을 만들어내는지를 식별하는 문제입니다.**

중첩 원리(superposition; 용량 보정 프로파일이 겹치는 성질)는 진단 출발점일 뿐입니다. Gabrielsson은 이 문제를 기전과 ODE로 보여주고, Rowland & Tozer Ch.16은 phenytoin·alcohol·ascorbic acid 같은 임상 용량-반응 비대칭으로 보여주며, Ch.17은 그 비대칭이 DDI의 AUC ratio, induction time course, PM 위험, route effect로 어떻게 확장되는지 보여줍니다. [G pp.112–114], [T16 pp.491–492], [T17 pp.531–532]

읽는 순서는 **진단 → capacity → time → binding → DDI → PD interaction**입니다. 먼저 dose-normalized plot으로 "선형이 아닌지"를 확인하고, 그다음 $V_{max}/K_m$, enzyme turnover, $f_u$(unbound fraction; 단백에 결합되지 않은 자유 약물 분율 — 약리 활성과 unbound clearance를 결정), $f_m$(해당 경로가 담당하는 제거 비율), route/extraction 순으로 점검합니다.

$$
\underbrace{V_{max}/K_m}_{\text{저농도 기울기}}\quad;
\quad\underbrace{f_u}_{\text{fu: 자유분율}}\quad;
\quad\underbrace{f_m}_{\text{fm: 경로몫}}
$$

$f_m$은 DDI 예측에서 "막힌 경로가 전체 제거에서 얼마나 큰가"를 묻는 변수입니다. 이 순서를 어기면 비선형 모델을 fitting할 수는 있어도, **왜 파라미터가 흔들리는지는 설명하지 못합니다.** [G p.113], [T16 p.492], [T17 pp.532–533]

## 1.0 ASCII 레이어 개념 지도

```text
[레이어 1: 무엇인가]
  superposition failure
  ├─ dose-normalized exposure
  ├─ capacity limitation
  ├─ time-dependent kinetics
  ├─ binding / unbound concentration
  └─ DDI / PD interaction

[레이어 2: 어떻게 계산되는가]
  AUC/Dose → CL(C)=Vmax/(Km+C)
           → dE/dt = Rin - kout·E
           → Cu = K0/CLu
           → AUC ratio = 1 / {fm/(1+Cu,I/KI) + (1-fm)}

[레이어 3: 언제, 왜 중요한가]
  dose escalation → toxicity / treatment failure
  repeated dosing → trough drift / delayed recovery
  total-only monitoring → unbound exposure misread
  oral vs IV DDI → first-pass / route-specific decision
```

## 1.0b 지식 그래프 위치

```text
[선행 세션: 선형 PK·중첩 원리·AUC/CL 기초]
        → [이 세션: 비선형 PK와 DDI mechanism triage]
        → [후속 세션: PopPK covariate modeling·TDM·DDI/PD 모델링]
```

🧭 **읽는 순서:**  
카드 1 (C1): "선형이 깨졌다는 것을 어떤 그림으로 먼저 확인하는가?"  
카드 2 (C2): "용량 한계가 왜 작은 증량을 큰 노출 변화로 바꾸는가?"  
카드 3 (C3): "농도 시계와 효소 시계가 어긋나면 무엇이 달라지는가?"  
카드 4 (C4): "총 농도와 비결합 농도 중 무엇을 믿어야 하는가?"  
카드 5 (C5): "DDI 크기를 억제제 이름이 아니라 어떤 분모로 계산하는가?"  
카드 6 (C6): "AUC, Cmax, t½가 서로 다른 방향으로 움직이면 어떻게 기전을 분리하는가?"

## 1.1 지식 그래프 위치

| 층위(Layer) | 질문 | 대표 기전(Mechanism) | 실패 시그널 |
|---|---|---|---|
| 진단(Diagnostics) | 농도/노출이 용량에 비례하는가? | 중첩 원리(superposition), AUC/Dose vs Dose | 용량 보정 곡선이 겹치지 않음 |
| 용량(Capacity) | 병목이 용량 한계인가? | MM 대사/수송, 포화성 초회 통과 | 작은 용량 변화가 큰 Css 변화를 만듦 |
| 시간(Time) | 파라미터가 시간에 따라 바뀌는가? | enzyme turnover, induction, MBI | trough envelope drift, 지연 독성/회복 |
| 결합(Binding) | 총 농도가 오해를 유발하는가? | 포화성 단백/조직/표적 결합 | total vs unbound가 서로 다른 결론 |
| DDI | 다른 약물이 CL/F/V/PD를 바꾸는가? | 억제, 유도, 수송체, PD 상호작용 | AUC ratio, 투여경로 차이, PM 증폭 |

## 1.2 거장의 30초 진단 시그널

| # | 시그널 (원시 데이터 관찰) | 1차 의심 기전 | 검증 단계 |
|---|---|---|---|
| 1 | semi-log concentration plot에서 **terminal slope이 dose에 따라 달라짐** | MM capacity ($V_{max}/K_m$ saturable elimination) | dose-normalized curve 중첩 여부 확인 [G p.116, Fig.2.89] |
| 2 | 같은 dose 반복투여에서 **trough가 systematic한 방향으로 이동** | autoinduction 또는 time-dependent CL | single-dose vs multi-dose model fit 차이 확인 [G pp.580–585, PK22] |
| 3 | total CLR은 **불변**인데 unbound CLR이 **변함** | nonlinear plasma protein binding (**metabolic induction 아님**) | $f_u$를 용량 수준별로 측정 [T16 pp.511–516] |
| 4 | inhibitor 병용에서 **oral interaction > IV interaction** | gut wall/first-pass metabolism component 우세 (단순 hepatic CL inhibition 아님) | IV/oral crossover 또는 $F_G$, $F_H$ 분리 [T17 pp.553–554] |
| 5 | $V_{max}/K_m$ 값이 **hepatic blood flow $Q_H$에 근접** | flow-extraction 분기점 (high-extraction ↔ low-extraction); ethanol prototype | $E_H$(extraction ratio = $CL_H/Q_H$, 0–1 범위; 간을 한 번 통과할 때 제거되는 분율) 계산 후 well-stirred 가정 점검 [G p.140, Fig.18.4] |
| 6 | single-dose model fit이 multiple-dose에서 **systematic over/underprediction** | time-dependent kinetics (autoinduction, MBI, withdrawal trap) | enzyme turnover compartment 추가 시도 [G pp.580–585], [T16 pp.516–519] |

$$
\underbrace{E_H}_{\text{간 추출분율}}
=
\frac{\underbrace{CL_H}_{\text{간 CL}}}{\underbrace{Q_H}_{\text{QH 혈류}}}
\qquad;
\qquad
\underbrace{V_{max}/K_m}_{\text{저농도 처리능}}\approx \underbrace{Q_H}_{\text{혈류한계}}
$$

이 6개 시그널은 §2 C1–C6의 "진단 시그니처" 섹션에서 다시 만나면서 의미가 누적되도록 설계돼 있습니다. 지금 외울 필요는 없습니다.

**요약:** 이 세션은 "비선형 PK = 용량 비례 실패"에서 멈추지 않습니다. 최종 목표는 비선형성의 원인을 **근원 기전으로 분해**하고, 그것을 실험 설계·TDM 해석·PopPK 모델 진단·DDI 위험 예측으로 옮기는 것입니다.

---

> 📊 **개념 도식 (HTML에서 렌더링):** Session 08 기전 분류 지도 — 중첩 원리 실패에서 시작해 capacity·time·binding·DDI/PD interaction으로 분기하고, 이를 PopPK/TDM/DDI 의사결정으로 옮기는 흐름.

> 🎯 **C1으로 들어가기 전 한 줄** — $AUC/Dose$와 dose-normalized profile을 **먼저** 그려라. 여기서 $CL$, $F$, 분포, 결합, 시간 의존성의 다음 검증 축이 갈라집니다.

---

<!-- SLIDE_START: §2 | title: 개념 해부 카드 -->

# §2. 개념 해부 카드(Concept Anatomy Cards)

<!-- SLIDE_START: C1 | title: 비선형성 진단(Nonlinearity Diagnostics) — 중첩 원리(superposition)가 깨지는 순간부터 시작합니다 -->

## C1. 비선형성 진단(Nonlinearity Diagnostics) — 중첩 원리(superposition)가 깨지는 순간부터 시작합니다

> **거장의 시각**  
> 비선형성을 모델 이름으로 먼저 부르면 CL, F, 분포, 결합, 시간 의존성 중 무엇이 흔들렸는지 놓치게 됩니다. **dose-normalized plot과 AUC/Dose 방향을 먼저** 보면 다음 카드로 들어갈 기전 후보가 강제로 좁혀집니다.

**핵심 아이디어:** 비선형성의 첫 진단은 "모델을 무엇으로 짤까?"가 아닙니다. 같은 route·formulation·method에서 dose-normalized concentration-time profile, AUC vs Dose, AUC/Dose vs Dose가 **겹치는지(superimpose)** 확인하는 것입니다. 선형이면 dose-normalized 관측값이 겹칩니다. 비선형이면 **CL, F, 분포, binding 중 적어도 하나가 dose나 time의 함수**가 됩니다. [G pp.112–114], [T16 p.492]

### 핵심 해부(Core Anatomy)

- **중첩 원리(Superposition):** 선형 PK에서는 용량을 두 배로 하면 농도와 AUC도 두 배가 됩니다. [G pp.113–115], [T16 p.492]
- **Dose-normalized AUC 패턴:** $AUC/Dose$가 용량과 함께 **증가**하면 CL 감소 또는 F 증가를 의심하고, **감소**하면 CL 증가 또는 F 감소를 의심합니다. [G p.113]

$$
\underbrace{AUC/Dose}_{\text{AUC/용량}}
$$

- **시간 의존 동역학의 정의:** 농도가 변해서 파라미터가 달라 **보이는** 것만으로는 시간 의존성이 아닙니다. **실제 효소량·수송체 활성·관류 같은 생리/생화학 상태가 시간에 따라 변해야** 시간 의존성입니다. [G p.112], [T16 p.492]

### 실무 판독 규칙

🔑 **실무 규칙:** 비선형 PK 검토에서 **첫 그림은 spaghetti concentration-time plot이 아닙니다.** **dose-normalized concentration-time plot + AUC/Dose vs Dose**입니다. 이 두 그림 없이 바로 $V_{max}/K_m$를 fitting하면, capacity limitation인지 F 변화인지, time-dependence인지 binding artifact인지 구분할 수 없습니다. [G p.113]

**요약:** C1의 목적은 비선형성을 **선언**하는 게 아니라, 다음 질문을 **강제**하는 것입니다 — "AUC/Dose가 올라갔는가, 내려갔는가, 시간이 지나며 변했는가, total과 unbound가 다른 말을 하는가?"

이 카드의 30초 진단 질문(§1.2 #1): **dose-normalized profile이 superimpose되는가?** 겹치면 선형, 안 겹치면 C2~C6 중 어느 카드로 들어갈지가 정해집니다.

> 📖 **Gabrielsson & Weiner, p.113, Fig.2.85·Fig.2.86**: $AUC/Dose$ 패턴 인식을 시각적 분류로 익히는 그림입니다. 이 그림 없이 텍스트로만 보면 패턴 인식이 기억에 의존하게 됩니다.

> 🎯 **C2로 들어가기 전 한 줄** — MM kinetics는 $K_m+C$ 분모 하나로 $CL(C)$ 감소, rate plateau, $C_{ss}$ 폭증을 **동시에** 만듭니다.

---

> **C1 체화 핵심**  
> ① `용량 보정 곡선이 겹치지 않을 때` → CL, F, 분포, binding, time-dependence 중 하나가 상수가 아님  
> ② `AUC/Dose 증가 vs 감소` → CL 감소/F 증가 vs CL 증가/F 감소를 분리해 검증  
> ⚡ `비선형 모델부터 적합` → capacity/F/binding artifact 혼재 → 파라미터 해석 실패



<!-- SLIDE_START: C2 | title: 용량 한계 Michaelis–Menten 동역학(Capacity-limited Michaelis–Menten Kinetics) — $V_{max}/K_m$가 용량 조정의 비대칭성을 만듭니다 -->

## C2. 용량 한계 Michaelis–Menten 동역학(Capacity-limited Michaelis–Menten Kinetics) — $V_{max}/K_m$가 용량 조정의 비대칭성을 만듭니다

> **앞 카드에서 이 카드로**  
> C1에서 dose-normalized profile이 안 겹친다는 걸 확인했다면, 다음 질문은 "그 실패가 제거 capacity의 분모에서 왔는가?"입니다.

> **거장의 시각**  
> 💢 **흔한 오해:** MM kinetics는 "포화되면 zero-order"라는 암기 항목이라고 생각하기 쉽습니다.  
> ✅ **실제는:** $K_m+C$ 분모 하나가 $CL(C)$ 감소, rate plateau, $C_{ss}$ 폭증, DDI 분모를 **같은 구조로 묶습니다.**  
> 🎯 **체화할 단 하나의 직관:** capacity 근처에서는 작은 용량 변화가 분모를 깎아 큰 노출 변화로 증폭됩니다.

> **⚡ Apex Concept** — 본 세션의 가장 임상·실무 파급력이 큰 단일 개념. 용량-노출 관계가 비례 스케일링이 아니라 **기전 기반 국면 진단**으로 전환되는 분기점입니다.

**핵심 아이디어:** Michaelis–Menten 용량 한계는 **청소율이 상수가 아니라 농도의 함수가 되는 상황**입니다. 같은 약물이라도 농도 영역이 바뀌면 겉보기 청소율과 $t_{1/2}$ 해석이 달라집니다. Gabrielsson의 MM clearance는 Eq.2:266–2:274 영역입니다. Eq.2:264는 linear superposition 식이라 MM ODE의 출처로 쓰지 않습니다. [G pp.114–119]

**거장의 시각 — 분모의 정체:** $V_{max}$와 $K_m$의 분모 $K_m+C$는 기질–효소 가역 결합의 **quasi-steady-state assumption (QSSA)**이 만든 질량 작용의 산물입니다. 이 분모가 그대로 C5의 DDI에서 competitive 분모 $K_m(1+C_{u,I}/K_I)+C$로 확장됩니다 — **C2 분모와 C5 DDI 분모는 같은 mass action 골격이 다른 맥락에서 나타난 것입니다.** 또한 $V_{max}/K_m$ 비율이 hepatic blood flow $Q_H$ 근처가 되면 high-extraction ↔ low-extraction 분기점에 도달합니다. 세 식의 명시적 비교는 C5의 mass action equivalence triangle에서 다룹니다. [G pp.115–118], [G p.140 Fig.18.4]

$$
\underbrace{K_m+C}_{\text{MM 분모}}
\quad\Longrightarrow\quad
\underbrace{K_m\left(1+C_{u,I}/K_I\right)+C}_{\text{억제 분모}}
$$

### 핵심 수식 및 출처 태그

$$
\underbrace{CL(C)}_{\text{농도의존 CL}}
=
\frac{\overbrace{V_{max}}^{\text{Vmax 처리상한}}}{\underbrace{K_m}_{\text{Km 반포화}}+\underbrace{C}_{\text{현재 C}}}
$$

[수식 계열(Equation family): G Eq.2:266; source tag: G p.115]

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $CL(C)$ | volume/time | 농도에 따라 달라지는 겉보기 청소율 | $C$ 증가 시 감소 |
| $V_{max}$ | amount/time 또는 concentration/time | 효소/수송체 처리 상한 | 효소량, 유도/억제, 간기능 |
| $K_m$ | concentration | 반최대 처리 농도 scale | 기질-효소 affinity, 경쟁 억제 |
| $C$ | concentration | 현재 기질 농도 | 투여량, 축적, 분포 |

💡 **비유:** 좁은 톨게이트에 차가 몰릴수록 차 한 대당 통과 속도가 느려지는 상황입니다. 톨게이트의 최대 처리량이 $V_{max}$, 정체가 보이기 시작하는 교통량 scale이 $K_m$입니다.

$$
\underbrace{Rate}_{\text{처리속도}}
=
\frac{\overbrace{V_{max}}^{\text{Vmax 상한}}\cdot\underbrace{C}_{\text{기질 C}}}{\underbrace{K_m}_{\text{Km scale}}+\underbrace{C}_{\text{포화구동 C}}}
$$

[G pp.115–116], [T16 p.494]

Bolus ODE는 $V_{max}$가 농도/시간 단위면 $dC/dt=-V_{max}C/(K_m+C)$로 쓸 수 있지만, $V_{max}$가 총량/시간 단위면 부피 보정이 필요합니다. 본문에서는 약식으로만 사용하고 주 출처 태그는 Eq.2:266–2:274로 둡니다. [G pp.115–118]

$$
\underbrace{\frac{dC}{dt}}_{\text{C 변화율}}
=
-\frac{\overbrace{V_{max}}^{\text{제거상한}}\cdot\underbrace{C}_{\text{현재 C}}}{\underbrace{K_m+C}_{\text{포화분모}}}
$$

$$
\underbrace{AUC}_{\text{AUC 노출}}
=
\frac{\underbrace{C^0}_{\text{초기 C}}}{2\overbrace{V_{max}}^{\text{제거상한}}}
\left(
\underbrace{K_m}_{\text{Km scale}}+\frac{\underbrace{C^0}_{\text{초기 C}}}{2}
\right)
\quad\text{(IV bolus, MM)}
$$

[G Eq.2:271; source tag: G p.117]

이 AUC 식의 의미는 다음과 같습니다 — 고농도에서는 농도 감소가 거의 선형이라 시간평균 농도가 $C^0/2$에 가깝지만, 농도가 $K_m$ 부근으로 내려오면 소실이 지수적으로 가속돼 시간평균은 그보다 작아집니다. **AUC 식 안에 $K_m$이 들어와 있다는 것 자체가 용량 한계의 수학적 흔적**입니다. [G p.117]

### 두 극한 사례

- **저농도 영역:** $C\ll K_m$이면 $CL\approx V_{max}/K_m$이고 겉보기 1차 속도처럼 보입니다. [G pp.115–117]
- **고농도 영역:** $C\gg K_m$이면 제거 속도가 $V_{max}$에 접근하고 겉보기 청소율은 감소합니다. 이 영역에서는 작은 용량 증가가 **불균형적인** AUC/Css 증가를 만듭니다. [G pp.115–119], [T16 pp.500–506]

$$
\underbrace{C\ll K_m}_{\text{저농도}}\Rightarrow \underbrace{CL}_{\text{CL 상수화}}\approx \frac{V_{max}}{K_m}
\qquad;
\qquad
\underbrace{C\gg K_m}_{\text{고농도}}\Rightarrow \underbrace{Rate}_{\text{처리속도}}\approx V_{max}
$$

### 임상 앵커 — 정량 사례

**1. Phenytoin — 용량 한계의 정량 원형(prototype)** [T16 pp.491, 503–506]:

- 전형적 성인: $V_m\approx 500$ mg/day, $K_m\approx 0.4$ mg/L (unbound 기준), $f_u\approx 0.1$ → total 기준 $K_m'\approx 4$ mg/L
- 치료역(total) 10–20 mg/L → 이미 $K_m'$의 **2.5–5배 영역**. 즉 임상 농도 자체가 용량 한계 근처라는 뜻입니다.
- 도입 사례: 300 mg/day에서 4 mg/L이던 환자가 500 mg/day로 증량 후 36 mg/L → **67% 용량 증가가 9배 농도 증가**.
- 정상상태 분모 방정식:

$$
\underbrace{C_{u,ss}}_{\text{Css,u}}
=
\frac{\underbrace{K_m}_{\text{Km,u scale}}\cdot\underbrace{R_0}_{\text{투여 속도}}}{\underbrace{V_m-R_0}_{\text{남은 capacity}}}
$$

[T16 Eq.16-7; source tag: T16 p.503]

이 식의 핵심은 **$R_0$가 $V_m$에 가까워질수록 분모가 작아진다**는 점입니다. 따라서 $C_{u,ss}$는 선형이 아니라 급격히 상승합니다. $K_m$은 unbound 기준이므로 total로 작업할 때의 $K_m'$와 구분해야 합니다. [T16 pp.503–506]

- $V_m$ 민감도: $V_m$ 20% 감소가 $C_{ss}$를 **2배**로, $V_m$ 20% 증가가 $C_{ss}$를 약 **33% 감소**시킵니다. capacity 근처에서는 $V_m$의 작은 변화가 $C_{ss}$를 **비대칭적으로** 흔듭니다. [T16 p.506]

- **정상상태 도달 시간 발산 (Eq.16-10):** 300/350/400/425 mg/day 각각의 plateau는 6/9.3/16/22.7 mg/L이지만, 그 plateau에 도달하는 **시간이 용량이 $V_m$에 가까울수록 수일에서 수주로 발산**합니다. 용량 한계 근처에서는 모니터링 간격을 정상상태 도달 추정 이후로 옮겨야 한다는 임상 함의로 직접 연결됩니다. [T16 Fig.16-10, p.505]

- **혼합 경로 (Eq.16-11):** 한 약물의 제거 경로 중 비선형 경로의 비중 $f_m^{NL}$이 **0.5 이상**이면 용량-반응 비대칭이 임상적으로 의미 있는 수준으로 나타납니다. [T16 p.506]

**2. Alcohol (에탄올)** [T16 pp.500–502], [G pp.139–141], [G pp.556–562]:

- 근사값: $V_m\approx 10$ g/hr, $K_m\approx 100$ mg/L, $V_d\approx 42$ L (70 kg) → 0차 소실에 가까운 임상 직관을 제공합니다.
- 임상 앵커: 1 drink ≈ 14 g. **4 drinks/hr = 56 g/hr**는 $V_m$을 크게 초과하므로 농도가 무한정 누적되지만, **0.5 drink/hr = 7 g/hr**는 $V_m$ 안에 머무르므로 정상 pseudo-steady state는 $C_{ss}\approx 233$ mg/L 부근입니다. [T16 pp.501–502]
- 단, ethanol 사례는 capacity뿐 아니라 흡수·혈류·시간 인자가 겹치므로 단일 MM 사례처럼 과단순화하지 않습니다.

**3. Ascorbic acid (비타민 C) — phenytoin의 거울상(역방향 비선형성)** [T16 p.492]:

- 75 mg/day에서 9 mg/L, 10,000 mg/day에서 약 19 mg/L → **133배 용량 증가가 약 2배 농도 증가만** 만듭니다.
- 이유: 농도 상승과 함께 신장 청소율이 크게 증가($CL_R < 0.5$ mL/min @ 9 mg/L → 21 mL/min @ 19 mg/L, **>42배 증가**). 포화성 재흡수가 풀리는 **배출 밸브(escape valve)** 효과입니다.
- → 같은 "비선형 PK"이지만 임상 결과는 정반대입니다: **phenytoin은 고용량에서 독성 위험 폭증, ascorbic acid는 고용량에서 추가 노출 효율이 급격히 감소.**

> 🎯 **C3로 들어가기 전 한 줄** — $V_{max}$와 $K_m$는 곡률 구간을 통과한 데이터 없이는 ridge에 묶입니다. **수렴 성공을 예측 성공으로 착각하지 마세요.**

---
### 설계 및 적합 시사점

🔑 **실무 규칙:** $V_{max}$와 $K_m$를 따로 추정하려면 농도 범위가 **곡률 영역**을 지나야 하고, 특히 **$K_m$ 주변 또는 그 이하의 관측값**이 필요합니다. high-concentration plateau만 있으면 $V_{max}$와 $K_m$이 ridge처럼 같이 움직입니다. [G p.117]

🔑 **실무 규칙:** PK18처럼 비선형 적합을 시작하기 전에는 **그래프 방법**으로 $V_{max}/K_m$, $V_c$, distribution terms의 초기 추정값을 손산출해야 합니다. nonlinear fitting은 초기값에 민감하므로 손산출 30분이 모델 디버깅을 크게 줄입니다. [G pp.556–562]

### 진단 시그니처 — 명명 진단

> **거장의 명명 진단**  
> **"Vmax–Km Ridge Lock"** — 단일 용량 데이터 또는 좁은 용량 범위 데이터로 $V_{max}, K_m, V_d$ 동시 추정 시 $\rho(V_{max}, K_m) > 0.9$ (Gabrielsson p.116에서 −0.96 사례 보고). $V_d$와 $K_m$ 사이도 −0.95 부근의 음의 상관이 흔합니다. **구제 전략:** 용량 수준 추가, 외부 정보로 $K_m$ 사전 고정, 또는 sampling을 $K_m$ 근방까지 낮춰 곡률을 포착. [G p.116, p.117]

### 그럴듯한 오해(Plausible Fallacy) — Apex 전용

**오류:** 단일 용량 fit이 좋으면 다중 투여 예측도 정확하다고 판단한다.  
**왜 그럴싸한가:** 단일 용량 데이터에서는 여러 $(V_{max}, K_m)$ 조합이 비슷한 농도 궤적과 좋은 OFV 수렴을 만들 수 있습니다.  
**나비효과:** 단일 용량 fit 신뢰 → $V_{max}$–$K_m$ ridge 방치 → 다중 투여 trough envelope 오예측 → [임상] phenytoin 독성 농도(>20 mg/L) 또는 무효 농도(<10 mg/L) 미예측 → [모델링/규제] NONMEM RSE·상관구조 악화, dose ladder 또는 $K_m$ prior fix를 요구받는 재분석 위험.

**진단 시그니처:** OFV는 수렴하지만 $V_{max}$–$K_m$ RSE가 모두 50% 이상이고 $\rho(V_{max}, K_m)$가 강하면 **"Single-dose Fit Trap"**을 의심합니다. 이 패턴에서는 단일 모델 fit으로 임상 의사결정을 내리지 말고, **용량 사다리(dose ladder)를 추가하거나 $K_m$를 외부 정보로 사전 고정**한 뒤 재추정합니다.

이 카드의 30초 진단 질문(§1.2 #1, #5): **terminal slope이 dose에 따라 달라지는가? 그리고 $V_{max}/K_m$가 $Q_H$에 근접하는가?** 전자는 capacity-limited elimination을, 후자는 flow-extraction 분기점을 가리킵니다.

### 핵심 주의사항

> ⚠️ **헷갈림 방지:** AUC 증가는 F 증가일 수도 있고 CL 감소일 수도 있습니다. **비선형 구간에서 AUC만 보고 bioavailability를 단정하지 마세요.**

AUC 기반 생체이용률 계산은 청소율이 상수일 때만 안전합니다. CL이 농도 의존적이면 AUC 변화가 F 변화인지 CL 변화인지 분리되지 않으므로, "AUC가 늘었다 = F가 늘었다"로 결론 내리면 안 됩니다. [G p.116]

C2는 C5 DDI의 수학적 원형입니다. $K_m+C$의 분모 구조를 이해해야 inhibitor가 $1+C_{u,I}/K_I$ factor를 만드는 Eq.17-9–17-11도 새 식처럼 외우지 않게 됩니다. [G pp.115–118], [T17 pp.550–552]

**요약:** MM kinetics의 핵심은 "포화되면 zero-order"가 아닙니다. **CL이 농도의 함수가 되어 용량 조정, AUC 해석, $t_{1/2}$, steady-state 도달 시간이 전부 비선형화된다**는 것입니다.

> 📖 **Gabrielsson p.115 Fig.2.88; Rowland & Tozer p.503 Fig.16-9, p.505 Fig.16-10**: 같은 분모 직관이 세 가지 형태로 — 청소율은 감소하고, 속도는 plateau에 닿고, 임상 정상상태는 용량 한계 근처에서 급격히 민감해집니다. 농도 또는 투여 속도가 capacity에 가까워질 때 무엇이 변하는지를 따라가며 읽으세요.

> 🎯 **C3로 들어가기 전 한 줄** — 시간 의존성은 농도 변화가 아니라 **enzyme pool의 시계**입니다. $dE/dt=R_{in}-k_{out}E$를 보지 않으면 induction과 MBI를 놓칩니다.

---

> **C2 체화 핵심**  
> ① `용량 증가 시 농도가 비례 이상 증가할 때` → $K_m+C$ 분모와 capacity가 지배  
> ② `저농도 선형처럼 보이는 구간` → $V_{max}/K_m$만 보이고 $V_{max}$와 $K_m$는 분리 안 됨  
> ③ `정상상태 분모 $V_m-R_0$가 작아질 때` → 작은 용량 변화가 큰 $C_{ss}$ 변화로 증폭  
> ⚡ `단일 용량 fit 신뢰` → Single-dose Fit Trap → 다중투여 독성/무효 예측 실패



<!-- SLIDE_START: C3 | title: 시간 의존적 전환과 기전 기반 억제(Time-dependent Turnover and Mechanism-Based Inhibition) — 농도 시계와 효소 시계를 분리합니다 -->

## C3. 시간 의존적 전환과 기전 기반 억제(Time-dependent Turnover and Mechanism-Based Inhibition) — 농도 시계와 효소 시계를 분리합니다

> **앞 카드에서 이 카드로**  
> C2가 농도에 따른 capacity 병목이었다면, C3는 **파라미터 자체가 시간에 따라 움직이는** 두 번째 시계를 분리합니다.

> **거장의 시각**  
> 시간 의존성을 농도 변화로만 읽으면 induction, autoinduction, MBI, washout trap이 한꺼번에 뒤섞입니다. **약물 농도 시계와 enzyme pool 시계를 분리**하면 trough drift와 지연 회복의 원인이 즉시 보입니다.

**핵심 아이디어:** 시간 의존적 약동학은 **농도가 달라져서 청소율이 달라 보이는 현상이 아닙니다.** 효소·수송체·생리학 자체가 시간에 따라 변하는 현상입니다. 따라서 **약물 농도 시계와 효소 전환 시계라는 두 개의 시계를 분리**해서 읽어야 합니다. [G p.112], [G pp.119–129], [T16 pp.516–519]

**주 시계(Master clock) 위계:** induction이나 MBI에서는 **세 개의 시계가 동시에 돕니다** — 약물 자체의 $t_{1/2}^{drug}$, perpetrator(inducer/inhibitor)의 $t_{1/2}^{perpetrator}$, 그리고 enzyme pool의 $t_{1/2}^{enzyme} = \ln 2/k_{out}$. 관찰되는 dynamics는 이 셋 중 **가장 느린 시계**가 지배합니다. **Phenobarbital–Dicumarol**에서 plateau 도달이 3–4주 걸리는 건 phenobarbital 자체 $t_{1/2}\approx 4$ days가 가장 느려서 induction이 그것에 묶이기 때문입니다. [G pp.119–129], [T17 pp.560–561]

### 핵심 전환 방정식

$$\frac{dE}{dt}=R_{in}-k_{out}E$$  

$$
\underbrace{\frac{dE}{dt}}_{\text{효소 변화율}}
=
\underbrace{R_{in}}_{\text{효소 생성}}-
\underbrace{k_{out}E}_{\text{효소 소실}}
\qquad;
\qquad
\underbrace{E_{ss}}_{\text{효소 정상상태}}
=
\frac{\underbrace{R_{in}}_{\text{생성속도}}}{\underbrace{k_{out}}_{\text{소실상수}}}
$$

[G Eq.2:275–2:278; source tag: G pp.120–121]

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $E$ | enzyme amount/activity | 효소 또는 수송체 pool | 유도, MBI, 회복 |
| $R_{in}$ | amount/time | 효소 생성 속도 | 유도, 생리학적 조절 |
| $k_{out}$ | 1/time | 효소 소실 속도상수 | 효소 turnover, 질환 상태 |
| $E_{ss}$ | enzyme amount/activity | 효소 정상상태 | $R_{in}/k_{out}$ 균형 |

💡 **비유:** 농도 시계는 혈액 속 약물이 사라지는 시계이고, 효소 시계는 공장 설비가 새로 설치되거나 고장 난 뒤 교체되는 시계입니다. MBI에서는 약물이 사라져도 설비 교체가 끝나야 처리능이 회복됩니다.

효소 수준이 변하면 $CL(t)$가 변합니다. **유도(induction)**는 효소량 증가로 $V_{max}$ 또는 내인성 청소율($CL_{int}$; 비결합 약물에 대한 효소/수송체의 본질적 처리 능력으로, well-stirred 간 청소율은 $CL_H=Q_H\cdot f_u\cdot CL_{int}/(Q_H+f_u\cdot CL_{int})$로 표현됨) capacity를 끌어올립니다. 반대로 **탈유도나 MBI**는 효소 활성 회복을 $k_{out}$ 시계에 묶어 처리 능력 회복을 지연시킵니다. [G pp.120–128], [T17 pp.557–561]

$$
\underbrace{CL_H}_{\text{간 CL}}
=
\frac{\underbrace{Q_H}_{\text{QH 혈류}}\cdot\underbrace{f_u}_{\text{fu: 자유분율}}\cdot\underbrace{CL_{int}}_{\text{CLint 효소능}}}{\underbrace{Q_H}_{\text{혈류한계}}+\underbrace{f_u\cdot CL_{int}}_{\text{fu·CLint}}}
$$

### 자가유도 및 타가유도 앵커

- **PK22 자가유도(autoinduction):** **Compound X** 반복 주입 데이터에서 모델 파라미터는 $V_c$, $V_t$, $a$, $k_{12}$, $k_{21}$, $k_{out}$, $E_0$ 7개. Table 22.2의 핵심 추정값은 $a\approx 0.041$, $k_{out}\approx 0.023$ h⁻¹입니다. 효소 시상수 $1/k_{out}\approx 43$ h, $t_{1/2}^{enzyme}\approx 30$ h. **설계 강점:** trough sampling이 효소 동역학의 시간 척도를 직접 잡아내므로 $a$(농도-CL 기울기)와 $k_{out}$(시간 차원)을 따로 식별할 수 있습니다. [G pp.580–585], [G p.583]
- **Carbamazepine**(항경련제, 자가유도 prototype): 전환 시간 약 5일. 반복투여 첫 1–2주 동안 청소율이 시간에 따라 변하는 임상 앵커입니다. [T16 p.518]
- **Phenobarbital–Dicumarol**(barbiturate inducer × 항응고제 substrate): 유도 시작/종료가 즉시 일어나지 않고 3–4주 scale로 보이는 건 inducer/효소 전환 시계 때문. **phenobarbital $t_{1/2}\approx 4$ days**가 sustained release처럼 작용하므로 induction plateau도 $4$–$5\ t_{1/2}\approx 16$–$20$일 영역에서 도달합니다. [T17 pp.560–561]

### 기전 기반 억제(MBI): 전환 파괴 기전

MBI는 가역적 억제와 달리 **효소를 기능적으로 제거**합니다. 여기서 "제거"는 효소량이 사라진다는 뜻만이 아니라, **효소 활성이 회복 전까지 유효하지 않다**는 뜻입니다. 회복은 억제제 농도가 사라지는 속도뿐 아니라 **효소 재합성/분해 시계**에 의해 제한됩니다.

### 정량적 MBI 앵커

**Clarithromycin–CYP3A4 MBI**(macrolide 항생제, CYP3A4 MBI prototype) [T17 p.558]:

- $k_{inact}\approx 0.07$ min⁻¹ (포화 억제제 조건의 불활성화 속도)
- $k_E\approx 0.23$ day⁻¹ (효소 자연 분해 속도상수) → 효소 자연 $t_{1/2}\approx \ln 2/k_E \approx 3$ days (CYP3A4 baseline turnover)
- $C_{u,I}/K_I\approx 0.025$ (clarithromycin 임상 노출)
- $k_{inact}/k_E$ 비율 ≈ **438** → 효소가 자연 전환으로 회복하는 속도보다 불활성화가 약 438배 빠릅니다.
- 결과: 같은 $C_{u,I}/K_I=0.025$로 **가역적 억제로 평가하면 CL은 1.025배만 감소**하지만, **MBI 식(Eq.17-13/14)으로 평가하면 약 11배 CL 감소**. 같은 inhibitor 노출에서 두 기전의 결과가 **한 자릿수 단위**로 차이 납니다.
- CYP3A4 활성 회복은 inhibitor 중단 후 효소 재합성에 묶이며, **2주 또는 그 이상**이 필요할 수 있습니다. → 임상에서 "inhibitor 중단했으니 안전하다"는 timing 가정은 위험합니다.

Eq.17-13/17-14의 MBI 항은 C3 전환 ODE의 정상상태 사고를 DDI 예측에 붙인 것입니다. **가역적 억제는 "분모에 억제제 경쟁을 더하는 문제"**이고, **MBI는 "효소 풀 자체를 줄인 뒤 회복 시계까지 계산하는 문제"**입니다. [T17 p.558]

### 진단 시그니처 — 명명 진단

> **거장의 명명 진단**  
> - **"Trough Envelope Drift"**: 같은 dose 반복투여에서 trough가 한 방향으로 체계적으로 이동. IIV로 설명하기 전에 **time-varying CL을 먼저 의심**합니다. autoinduction이면 trough가 점차 낮아지고, MBI나 자기억제에서는 점차 높아집니다. [G pp.126–129], [G pp.580–585]
> - **"Single-dose Fit Trap"**: 단일 용량만 잘 맞는 모델이 반복투여에서 systematic over/underprediction을 보입니다. autoinduction 또는 time-dependent inhibition을 의심합니다. PK22 design rationale의 핵심 — single-dose data만으로는 효소 compartment가 식별되지 않습니다. [G pp.580–585], [T16 pp.516–519]
> - **"Washout Trap"**: MBI에서 perpetrator 중단 후 substrate exposure가 즉시 정상화된다고 가정하면 안 됩니다. 회복은 enzyme clock($2$–$3\,t_{1/2}\times \ln 2/k_E$)에 묶입니다. Clarithromycin MBI에서 회복이 2주에 이르는 게 그 예입니다. [T17 pp.557–558]

🔑 **실무 규칙:** 자가유도 연구에서 **dense single-dose sampling만 늘리는 것은 $k_{out}$ 식별에 충분하지 않을 수 있습니다.** multiple-dose trough envelope가 enzyme clock을 더 직접적으로 보여줍니다. [G pp.580–585]

**요약:** C3의 핵심 질문은 "약물 농도가 낮아졌는가?"가 아니라 **"enzyme pool이 회복되었는가?"**입니다. 이 질문 하나가 induction, autoinduction, MBI, withdrawal trap을 하나로 묶습니다.

이 카드의 30초 진단 질문(§1.2 #2, #6): **반복투여 trough가 한 방향으로 움직이는가, 그리고 single-dose 모델이 multiple-dose에서 systematic over/underprediction을 보이는가?** 둘 다 yes면 enzyme clock을 drug concentration clock과 분리해 식별해야 합니다.

> 📊 **개념 도식 (HTML에서 렌더링):** 비선형 PK의 두 시계 — 농도 시계 vs 효소 전환 시계. 가역적 억제는 주로 perpetrator 농도 시계를 따르지만, induction과 MBI는 **효소 전환/회복 시계**가 별도로 필요합니다.

> 🎯 **C4로 들어가기 전 한 줄** — 결합 비선형성은 **total concentration의 함정**입니다. $C_u$, $f_u$, 열린 계 clearance를 먼저 보지 않으면 해석이 뒤틀립니다.

---

> **C3 체화 핵심**  
> ① `반복투여 trough가 한 방향으로 이동할 때` → enzyme turnover와 $k_{out}$ 시계가 지배  
> ② `inhibitor 중단 후에도 회복이 느릴 때` → reversible inhibition보다 MBI/enzyme resynthesis가 지배  
> ⚡ `농도만 사라지면 상호작용도 끝난다` → washout trap → carry-over interaction 오염



<!-- SLIDE_START: C4 | title: 결합, TMDD, 치환 단독 DDI(Binding, TMDD, and Displacement-only DDI) — 총 농도(total concentration)를 그대로 믿지 않습니다 -->

## C4. 결합, TMDD, 치환 단독 DDI(Binding, TMDD, and Displacement-only DDI) — 총 농도(total concentration)를 그대로 믿지 않습니다

> **앞 카드에서 이 카드로**  
> C3가 시간에 따른 처리능 변화를 다뤘다면, C4는 **총 농도가 실제 활성 농도를 가리는 관측 경계 문제**로 넘어갑니다.

> **거장의 시각**  
> total concentration을 그대로 노출로 읽으면 protein binding displacement와 실제 unbound exposure 변화를 혼동합니다. **open system mass balance를 먼저 놓으면** displacement-only DDI가 왜 지속적 unbound exposure 증가가 아닌지 설명됩니다.

**핵심 아이디어:** 비선형 결합은 **total과 unbound의 관계를 비선형화**합니다. 따라서 total만으로 노출이나 효과를 판단하기 어렵습니다. 특히 **열린 생체 계와 닫힌 시험관 결합 실험을 혼동하면**, 단백 결합 치환을 실제 비결합 노출 변화로 과대해석하게 됩니다. [G pp.129–134], [T17 pp.538–544]

**물질수지의 강제성:** 열린 계 정상상태에서는 mass balance가 $C_u = K^0/CL_u$ ($K^0$ = unbound input rate, $CL_u$ = unbound clearance)라는 외부 경계조건을 **강제**합니다. 단백 결합이 어떻게 변하든 정상상태 $C_u$는 그 비율로 묶이고, total concentration이 free fraction 변화에 따라 자유롭게 조정됩니다. 이게 **"열린 계에서 displacement-only는 unbound steady state를 지속적으로 바꾸지 못한다"**는 결론의 수학적 출처입니다. [G §2.7.5, Eq.2:303]

$$
\underbrace{C_u}_{\text{Css,u}}
=
\frac{\underbrace{K^0}_{\text{비결합 입력}}}{\underbrace{CL_u}_{\text{비결합 CL}}}
$$

### 핵심 결합 방정식

$$
\underbrace{C_b}_{\text{결합 C}}
=
\frac{\underbrace{n}_{\text{자리 수}}\cdot\underbrace{P_t}_{\text{총 결합자리}}\cdot\underbrace{C_u}_{\text{자유 C}}}{\underbrace{K_d}_{\text{Kd}}+\underbrace{C_u}_{\text{포화구동 C}}}
$$

[G Eq.2:294; source tag: G p.129]

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $C_b$ | concentration | 결합된 약물 농도 | 결합자리 포화, 경쟁 치환 |
| $n$ | dimensionless | 결합 자리 수 | 단백/표적 특성 |
| $P_t$ | concentration | 총 결합자리 농도 | albumin, AAG, 표적 발현 |
| $C_u$ | concentration | 비결합 약물 농도 | 투여량, $f_u$, clearance |
| $K_d$ | concentration | 결합 친화도 scale | 단백/표적 affinity |

💡 **비유:** 좌석 수가 정해진 강의실에 학생이 몰리는 장면입니다. 빈 좌석이 많을 때는 대부분 앉지만, 좌석이 차면 추가 학생은 서 있게 되고 이것이 unbound fraction 증가로 보입니다.

결합 자리가 포화 가능하면 total이 크게 변해도 unbound 해석은 따로 해야 합니다. 저추출 약물의 정상상태에서는 unbound가 input rate와 unbound clearance에 의해 지배되므로, **displacement-only는 total을 낮출 수는 있어도 unbound 정상상태 노출을 지속적으로 올리지는 못합니다.** [G pp.129–134], [T17 pp.538–544]

### 열린 계 vs 닫힌 계

- **닫힌 시험관 계:** 총량이 고정되어 치환이 곧 비결합 분율 증가처럼 보입니다. [G pp.131–132]
- **열린 생체 계:** 유입·청소율·분포가 함께 작동하므로 총 농도 변화가 곧 약리학적 효과 변화는 아닙니다. [G pp.132–134]

차이의 핵심은 **"시험관 안의 총량 고정"과 "몸 안의 지속적 제거·재분포"**입니다.

### 포화성 결합 사례 — 정량 앵커

**Plasma protein/tissue binding nonlinearity prototypes** [T16 pp.511–516]:

- **Naproxen**(NSAID): 0–4 g 경구 dose 범위에서 AUC 비선형. albumin 결합 포화가 dose↑와 함께 $f_u$를 올려 unbound AUC가 total AUC보다 더 가파르게 증가. [T16 Fig.16-17]
- **Cefonicid**(cephalosporin 항생제): 30 mg/kg i.v. saturable albumin binding의 prototype. 같은 album site 경쟁이 임상 노출을 농도의존적으로 만듭니다. [T16 Fig.16-18]
- **Disopyramide**(항부정맥제): α₁-acid glycoprotein(AAG) 결합의 비선형성 — total CLR과 unbound CLR이 서로 다른 방향 신호를 줄 수 있습니다. [T16 Fig.16-16]
- **Trandolaprilat**(ACE 억제제): ACE 결합 자체가 nonlinear. $f_u$가 0.05→0.20 영역으로 dose에 따라 변함. [T16 p.514]
- **Bosentan**(endothelin 수용체 길항제, TMDD prototype): dose 증량 시 $V_{ss}$가 **0.67 → 0.16 L/kg로 감소** — high-affinity, low-capacity 수용체 결합이 포화되면서 organ에 잠긴 약물 비율이 줄어들기 때문. **저분자 약물에서도 TMDD 거동이 나타나는 사례.** [T16 Fig.16-20, p.515]
- **Dicloxacillin**(penicillin 항생제): $f_u\approx 0.04$, 1 g dose에서 $CL_R \approx 104$ mL/min, 2 g dose에서 $CL_R \approx 63$ mL/min — saturable renal secretion. [T16 Fig.16-13, p.508]

**Salicylic acid (아스피린 대사체) — 반대 방향 비선형성 두 개가 동시에** [T16 Figs.16-27~16-29, pp.520–522]:

같은 약물에서 **두 비선형성이 반대 방향으로 동시 작동**하는 사례. 단백 결합 포화는 $f_u$를 올리고, 대사 capacity 포화는 unbound CL을 떨어뜨립니다. 결과적으로 total $C_{ss}$ vs dosing rate 곡선의 모양은 **단일 기전으로 설명되지 않습니다.** → **비선형 PK는 단일 기전의 단순한 dose-response 곡선이 아닐 수 있으므로, 진단은 후보 기전 셋 이상을 동시에 손에 쥐고 진행해야 합니다.**

### 포화성 수송 방정식 [T16 p.495]

$$
\underbrace{Rate}_{\text{수송속도}}
=
\frac{\overbrace{T_m}^{\text{Tm 상한}}\cdot\underbrace{C_u}_{\text{자유 C}}}{\underbrace{K_T}_{\text{KT scale}}+\underbrace{C_u}_{\text{점유 C}}}
\quad\text{(Eq.16-3)}
$$

renal secretion(분비)과 reabsorption(재흡수)은 **같은 분모를 공유하지만 방향이 반대**라 임상 결과가 정반대로 나타납니다 — Dicloxacillin은 saturable secretion으로 고용량에서 $CL_R$ ↓, Ascorbic acid는 saturable reabsorption escape valve로 고용량에서 $CL_R$ ↑.

> 🎯 **C5로 들어가기 전 한 줄** — TMDD·metabolite·displacement-only DDI는 모두 **계의 경계를 묻는 질문**입니다. formation, disposition, unbound exposure를 한 통에 섞지 마세요.

---
### TMDD 및 조직/표적 결합

표적 매개 약물 disposition(TMDD)은 **고친화성·저용량 표적/조직 결합**이 disposition을 바꾸는 경우입니다. Tozer Ch.16은 저분자에서도 bosentan, imirestat, trandolaprilat, draflazine, mitoxantrone 같은 prototype을 제시합니다. 본 단계에서는 TMDD full mechanistic code나 Mager–Jusko implementation으로 확장하지 않습니다. [T16 pp.511–516]

### 약물-대사체 비선형 모델 — §2.7.6

활성 대사체가 효과나 독성에 기여하는 약물(carbamazepine-10,11-epoxide, irinotecan-SN38, codeine-morphine 영역)에서는, 모약물과 대사체가 **같은 MM 효소를 공유**할 때 disposition이 비선형으로 결합됩니다. [G pp.135–139]

- **모델 구조:** 2-compartment drug + 1-compartment metabolite + MM elimination. ODE는 Eq.2:304–2:308 영역, 파라미터 추정값은 Tables 2.18–2.20. 이때 대사체 농도 프로파일에서 **prolonged tail**이 나타날 수 있는데, **이게 대사체 자체의 분포 kinetics가 아니라 모약물의 MM elimination이 대사체 형성 속도를 제한하기 때문일 수 있어 오독 위험이 높습니다.**
- **출처 기반 경고:** parent–metabolite 동시 관측만으로는 대사체 disposition kinetics를 **추론적으로 외삽하면 안 됩니다.** 대사체를 단독 투여한 disposition 데이터가 없으면 대사체 청소율·분포·$t_{1/2}$가 식별되지 않을 수 있습니다 (G p.137 명시 경고). [G p.137]

### Displacement-only DDI 격하

**Phenytoin–Valproate**(항경련제 × 항경련제, displacement-only prototype): total phenytoin이 낮아져도 unbound phenytoin은 상대적으로 유지됩니다. 이 사례의 가치는 "용량을 줄여라"가 아니라 **"total만 보고 toxicity/efficacy를 판단하지 말라"**입니다. [T17 p.543]

**Warfarin–Phenylbutazone**(항응고제 × NSAID): 단순 displacement만이 아니라 **inhibition까지 겹친 multifaceted example**이므로 displacement 단독으로 다루면 안 됩니다. [T17 p.563]

🔑 **실무 규칙:** 단백 결합 비선형성이 의심되는 Phase 1/PopPK package에서는 **total만 모으지 말고 용량 수준별 $f_u$를 측정**하세요. total-only dataset은 binding nonlinearity와 clearance nonlinearity를 구분하기 어렵게 만듭니다. [G pp.129–134], [T16 pp.511–516]

**요약:** C4는 "protein binding이 변하면 위험하다"가 아니라, **total과 unbound가 서로 다른 질문에 답한다**는 원칙입니다.

이 카드의 30초 진단 질문(§1.2 #3): **total CLR은 불변인데 unbound CLR이 변하는가?** Yes면 비선형 plasma protein binding(metabolic induction 아님)을 의심하고 용량 수준별 $f_u$를 직접 측정해 검증합니다.

> 📖 **Gabrielsson p.132–133, Fig.2.104–2.105**: 닫힌 시험관 안에서는 단백질에서 떨어져 나온 약물이 다 그 안에 갇혀 있지만, 살아있는 사람 몸에서는 떨어져 나온 비결합 약물이 곧바로 청소율 경로로 빠져나갑니다. → **그래서 단순 displacement만으로 임상적 위험을 예측하면 안 됩니다.**

> 🎯 **C5로 들어가기 전 한 줄** — DDI 크기는 inhibitor 이름보다 **$f_m$과 $C_{u,I}/K_I$가 결정합니다.** AUC ratio 분모가 victim drug의 취약성을 드러냅니다.

---

> **C4 체화 핵심**  
> ① `total과 unbound가 다른 말을 할 때` → $f_u$와 binding saturation이 지배  
> ② `displacement-only vs inhibition 혼동` → 열린 계에서는 $C_u=K^0/CL_u$ mass balance가 우선  
> ⚡ `total 농도만 보고 용량 조정` → efficacy/toxicity 판단 오류



<!-- SLIDE_START: C5 | title: 정량적 DDI 예측(Quantitative DDI Prediction) — $f_m$, 억제제 강도(inhibitor strength), 투여 경로(route)가 AUC ratio를 만듭니다 -->

## C5. 정량적 DDI 예측(Quantitative DDI Prediction) — $f_m$, 억제제 강도(inhibitor strength), 투여 경로(route)가 AUC ratio를 만듭니다

> **앞 카드에서 이 카드로**  
> C4에서 unbound와 system boundary를 분리했으므로, C5에서는 그 논리를 **억제 경로 비율과 DDI AUC ratio 계산**으로 확장합니다.

> **거장의 시각**  
> DDI를 inhibitor 이름으로 분류하면 victim drug의 pathway dependence를 놓칩니다. **$f_m$과 $C_{u,I}/K_I$를 분모에 넣어 보면** 같은 inhibitor라도 AUC ratio가 왜 완전히 달라지는지 보입니다.

**핵심 아이디어:** Ch.17의 DDI 정량 프레임워크는 "상호작용이 있다/없다"를 묻지 않습니다. **피영향 약물의 청소율 중 얼마가 억제된 경로에 의존하는지($f_m$), 억제제 노출이 $K_I$에 비해 얼마나 큰지, 투여 경로/초회통과가 얼마나 관여하는지**를 묻습니다. [T17 pp.531–532], [T17 pp.546–552]

**질량 작용 등가 삼각형(Mass Action Equivalence Triangle):** 본 세션의 수학적 정점은 다음 세 식이 **같은 분모 구조의 다른 표현**이라는 점입니다.

$$
\overbrace{CL=\frac{V_{max}}{K_m+C}}^{\text{C-CL capacity}}
\quad\Longleftrightarrow\quad
\overbrace{C_{u,ss}=\frac{K_m R_0}{V_m-R_0}}^{\text{Css 분모 민감}}
\quad\Longleftrightarrow\quad
\overbrace{\text{AUC ratio}\approx\frac{1}{\frac{f_m}{1+C_{u,I}/K_I}+(1-f_m)}}^{\text{DDI 경로몫}}
$$

세 식 모두 **기질-효소 가역 결합의 질량 작용(QSSA)이 만든 같은 골격**을 다른 변수로 표현한 것입니다. Eq.2:266은 농도-CL의 질량 작용 직접 표현, Eq.16-7은 그것의 정상상태 분모 발산 형태, Eq.17-11은 억제제가 분모에 추가됐을 때의 노출 비율 형태입니다. **이 세 식을 한 줄로 보면 비선형 PK·DDI 직관 전부가 동일한 mass action 분모로 회수됩니다.** [G pp.115–118], [T16 p.503], [T17 pp.550–552]

### 가역적 경쟁 억제 핵심 골격

Eq.17-9–17-12는 **억제된 경로의 청소율 감소와 전신 AUC ratio를 연결**합니다. 한 경로의 억제가 전체 노출을 얼마나 바꾸는지 계산하는 핵심 골격입니다. 핵심 직관은 다음입니다. [T17 pp.550–552]

$$
\underbrace{\text{AUC ratio}}_{\text{병용 노출비}}
\approx
\frac{1}{
\underbrace{\frac{f_m}{1+C_{u,I}/K_I}}_{\text{억제경로 잔여몫}}
+
\underbrace{(1-f_m)}_{\text{우회경로 몫}}
}
$$

이 식은 Rowland & Tozer의 textbook 기반 DDI 식으로만 다룹니다. 첨부 출처 범위를 넘어 특정 규제 지침의 핵심식으로 확장하지 않습니다. [T17 pp.550–552]

### 임상 앵커 — 정량 사례

**Theophylline–Enoxacin** (Rogge et al. 1989; Enoxacin 400 mg q12h × 4 days; theophylline은 bronchodilator/CYP1A2 substrate, enoxacin은 fluoroquinolone/CYP1A2 inhibitor) [T17 pp.546–550, Fig.17-6, Fig.17-7]:

- $t_{1/2}$ 8.8 h → 22 h (**2.5배 연장**)
- 평균 투여간격 Css 4 mg/L → 9 mg/L (**약 2.25배**)
- $CL_{inhib}/CL_{normal}=0.44$
- $f_m\approx 0.67$ (CYP1A2 의존성)
- Eq.17-9–17-12의 **단계적 억제**를 보여 주는 주요 임상 예시. 같은 fluoroquinolone 계열에서 enoxacin 용량이 낮아지면 억제가 단계적으로 약해지고, 계열 비교(ciprofloxacin > enoxacin > norfloxacin)에서도 직접 보입니다.

**Desipramine–Quinidine** (CYP2D6; desipramine = TCA, quinidine = CYP2D6/P-gp inhibitor) [T17 pp.549–550]:
- $f_m^{CYP2D6}\approx 0.75$
- CL이 약 **4배 감소**
- 즉 **$f_m$이 높을 때 한 경로의 억제가 전신 CL을 거의 같은 비율로 떨어뜨릴 수 있습니다.**

**Desipramine–Fluoxetine** (Bergstrom 1992; Table 17-11; fluoxetine = SSRI/CYP2D6 inhibitor, 긴 $t_{1/2}$) [T17 p.552]:
- AUC: 284 → 2110 µg·hr/L (**약 7.4배**)
- $t_{1/2}$: 16.1 h → 63.8 h (약 4배)
- CL/F: 289 → 27.1 L/hr (약 10.7배 감소)
- 같은 desipramine victim에 대해 **fluoxetine은 quinidine보다 더 강한** 효과를 보이는데, 이는 fluoxetine 자체의 긴 $t_{1/2}$와 활성 대사체 norfluoxetine까지 더해진 결과입니다.

**Diltiazem–Lovastatin** (Table 17-7; diltiazem = CCB/CYP3A4 inhibitor, lovastatin = statin/CYP3A4 substrate) [T17 p.553]:
- AUC ratio: **1.27 (i.v.) vs 3.57 (oral)** → 경구 상호작용이 IV보다 **약 3배** 큽니다.
- → **장벽/초회통과 component가 크다는 직접 증거.** 간 청소율 억제만으로는 경구·IV 차이를 설명할 수 없습니다.

**Fluconazole–Midazolam** (Fig.17-10; fluconazole 400 mg; fluconazole = azole 항진균제/CYP3A4 inhibitor, midazolam = BZD/CYP3A4 substrate) [T17 p.554]:
- 경구 AUC: ↑5.6배
- IV AUC: ↑2배
- F: 24% → 63%
- $F_H$: 0.42 → 0.72 ($F_H$ = 간 생체이용률)
- $F_G$: 0.57 → 0.88 ($F_G$ = 장벽 생체이용률)
- **$F_G$가 $F_H$보다 더 큰 비율로 변한다는 것은 midazolam의 경구 초회통과가 장에 상당 부분 위치한다는 뜻**입니다.

### 억제제 분류 — Table 17-5 [T17 p.549]

| 분류 | 기준 (기질 AUC 배수 증가) | 추가 표시 |
|---|---|---|
| 강함(Strong) | ≥5배 또는 >80% CL 감소 | MBI는 별도 (b) 표시 |
| 중등도(Moderate) | 2–5배 | — |
| 약함(Weak) | 1.25–2배 | — |

**기질 민감도 분류 (Table 17-6):** 강한 억제제와 병용 시 **≥4배 AUC 증가**를 보이는 기질이 별도 분류됩니다. 여기서는 textbook reference의 실무 어휘로만 다루고, 다른 규제문서의 분류 체계와 직접 동일시하지 않습니다.

### PM × 억제제 증폭

Eq.17-18은 다형성 경로와 비다형성 잔여 경로가 동시에 고려될 때 **최대 노출 비율이 커질 수 있음**을 보여줍니다. PM 환자에서 남은 비다형성 경로까지 강한 억제제가 막으면 노출 비율이 크게 뛸 수 있습니다.

$$
\underbrace{\text{Maximum exposure ratio}}_{\text{최대 노출비}}
=
\frac{1}{
\underbrace{1-f_m^{POLY}-f_m^{NP}}_{\text{잔여 CL 분율}}
}
$$

[T17 Eq.17-18; source tag: T17 pp.558–559]

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| Maximum exposure ratio | fold | 잔여 경로가 막힐 때 가능한 최대 노출 증가 | PM 상태, 잔여 경로 억제 |
| $f_m^{POLY}$ | fraction | 다형성 경로 제거 비율 | 유전형 |
| $f_m^{NP}$ | fraction | 비다형성 잔여 경로 제거 비율 | inhibitor 병용, 대체 경로 의존성 |

💡 **비유:** 두 배수구 중 하나가 원래 막힌 상태(PM)에서 남은 배수구까지 막으면 물이 갑자기 차오릅니다. 분모의 잔여 CL 여유가 작을수록 노출 ratio는 급격히 커집니다.

Fig.17-15의 omeprazole–clarithromycin example은 high ratio 사례로 유지하되, 특정 배수값은 exact printed number가 아니라 시각 추정/확인 필요로 둡니다. 본문에서는 "매우 큰 exposure ratio 사례"로만 사용합니다. [T17 p.559]

### 투여 순서와 중단

> 🔑 **DDI 판독 규칙:** inhibitor 추가와 제거는 **대칭 사건이 아닙니다.** MBI와 induction에서는 회복 시계가 별도로 남습니다.

상호작용은 all-or-none이 아니라 농도·시점·순서·시작/중단에 따라 단계적으로 나타납니다. 따라서 inhibitor를 추가할 때와 제거할 때의 위험은 대칭이 아닙니다. **induction/MBI에서는 특히 회복 지연이 치명적**입니다. [T17 pp.532–534], [T17 pp.557–561]

🔑 **실무 규칙:** DDI 예측표에는 최소한 **$f_m$ uncertainty band**를 붙이세요. $f_m$가 0.5인지 0.8인지에 따라 같은 inhibitor라도 AUC ratio 해석이 완전히 달라집니다. [T17 pp.550–552]

**요약:** C5의 핵심은 억제제 이름이 아니라 **affected drug의 pathway dependence**입니다. $C_{u,I}/K_I$가 커도 $f_m$가 작으면 whole-body AUC ratio는 제한되고, $f_m$가 크면 작은 inhibitor effect도 임상적으로 커집니다.

이 카드의 30초 진단 질문(§1.2 #4): **inhibitor 병용에서 oral interaction이 IV interaction보다 큰가?** Yes면 gut wall/first-pass metabolism component가 우세입니다 — hepatic CL inhibition만으로 설명하지 마세요. **Diltiazem-Lovastatin (1.27 IV vs 3.57 oral)과 Fluconazole-Midazolam ($F_G$ 0.57→0.88)**이 직접 anchor입니다.

> 📖 **Rowland & Tozer p.550, Fig.17-8**: AUC ratio 식은 베끼기는 쉽지만 직관으로 체감하기는 어렵습니다. 이 그림은 **같은 억제제가 $f_m$에 따라 작은 노출 변화만 만들지 큰 노출 변화를 만들지를 어떻게 조절하는지** 보여줍니다. 먼저 inhibitor strength를 고정하고 $f_m$를 움직이며 읽은 뒤, $f_m$를 고정하고 inhibitor strength를 바꾸며 다시 읽으세요.

> 🎯 **C6로 들어가기 전 한 줄** — 복합 DDI와 PD interaction은 **AUC 하나로 끝나지 않습니다.** $C_{max}$, $t_{1/2}$, V/F, route, EC50, Emax를 함께 읽어야 합니다.

---

> **C5 체화 핵심**  
> ① `inhibitor 병용 시 AUC ratio 예측` → $f_m$과 $C_{u,I}/K_I$가 지배  
> ② `oral interaction이 IV보다 클 때` → hepatic CL 억제만이 아니라 gut/first-pass component가 지배  
> ⚡ `inhibitor strength만 보고 판단` → victim pathway dependence 무시 → DDI 위험 과소/과대평가



<!-- SLIDE_START: C6 | title: 복합/수송체 및 PD 상호작용(Multifaceted/Transporter and PD Interactions) — 하나의 가해 약물(perpetrator)이 하나의 기전만 갖는다고 가정하지 않습니다 -->

## C6. 복합/수송체 및 PD 상호작용(Multifaceted/Transporter and PD Interactions) — 하나의 가해 약물(perpetrator)이 하나의 기전만 갖는다고 가정하지 않습니다

> **앞 카드에서 이 카드로**  
> C5가 한 억제 경로의 정량화를 다뤘다면, C6는 **실제 임상 DDI처럼 여러 기전이 동시에 움직이는** 경우를 판독합니다.

> **거장의 시각**  
> AUC 하나만 보면 transporter, distribution, induction, PD interaction이 전부 metabolic inhibition처럼 보입니다. **Cmax, $t_{1/2}$, V/F, route, timing을 한 표에 놓으면** 복합 DDI의 방향성이 분리됩니다.

**핵심 아이디어:** 실제 DDI는 **대사 억제 하나로 끝나지 않습니다.** 수송체 억제, 분포 변화, 장벽/간 초회통과, 유도, PD 가산성/상승작용/길항이 겹칠 수 있습니다. 이 때문에 같은 drug라도 **급성/만성, 경구/정맥 조건에서 반대 방향 효과**를 보일 수 있습니다. [T17 pp.563–567]

### 복합 기전 앵커 — 정량 사례

**1. Digoxin–Quinidine** (digoxin = 강심배당체/P-gp substrate, quinidine = 항부정맥제/P-gp inhibitor; Table 17-8) [T17 p.564]:
- CL: 140 → 72 mL/min (**약 절반**)
- CLR: 101 → 51 mL/min (P-gp inhibition으로 renal secretion 감소)
- $V_d$: 500 → 240 L (P-gp inhibition으로 tissue 분포 감소)
- F: 0.75 → 0.85 (intestinal P-gp inhibition으로 absorption 증가)
- → **quinidine은 digoxin의 CL, $V_d$, F 셋을 동시에 변화시킵니다.** 단일 대사 기전만으로는 이 패턴을 설명할 수 없습니다.

**2. Atorvastatin–Rifampin** (acute IV; atorvastatin = statin/OATP1B1·CYP3A4 substrate, rifampin = 항결핵제; Fig.17-19) [T17 p.565]:
- Cmax ↑10배
- AUC ↑7배
- $t_{1/2}$: 8 h → 3 h (**감소** — 단순 metabolic inhibition과 반대 방향)
- 기전: **급성** rifampin이 OATP1B1(간 uptake transporter)을 억제해 atorvastatin의 간 분포를 차단합니다. → 혈중 누적으로 Cmax/AUC ↑, distribution-limited terminal phase가 사라져 $t_{1/2}$ ↓.

**3. Rosuvastatin–Cyclosporine** (rosuvastatin = statin/OATP1B1·BCRP substrate, cyclosporine = 면역억제제/OATP·BCRP inhibitor; Fig.17-11, heart transplant recipients) [T17 p.555]:
- Cmax ↑11배
- AUC ↑7배
- 기전: cyclosporine이 **OATP1B1 + BCRP를 동시에** 억제해 rosuvastatin의 간 흡수와 담즙 배출을 모두 차단합니다.

**4. Phenobarbital–Dicumarol** (Fig.17-17) [T17 p.561]:
- Plateau 도달까지 **3–4주**
- 이유: **phenobarbital $t_{1/2}\approx 4$ days가 유도 시작의 rate-limiter**입니다. $4$–$5\ t_{1/2}\approx 16$–$20$일 영역에서 inducer가 정상상태에 도달하고, 그 이후에 효소량이 새 plateau로 진입합니다.
- C3의 master clock 위계의 직접 anchor — **가장 느린 시계(phenobarbital)가 동역학을 지배**합니다.

**5. Fluconazole–Midazolam / Diltiazem–Lovastatin:** oral vs IV 차이가 gut wall/first-pass contribution을 분리하는 단서입니다. C5에서 정량값을 다뤘으므로 여기서는 기전 어휘로만 회수합니다. [T17 pp.553–554]

### 급성/만성 × 경구/정맥 진단 매트릭스

**Rifampin** 같은 perpetrator는 **급성 수송체 억제와 만성 효소 유도가 서로 반대 방향**의 효과를 만들 수 있습니다. 따라서 실무적으로는 acute IV, acute oral, chronic IV, chronic oral을 구분해 기전을 생각해야 합니다. [T17 pp.560–565]

| 조건 | 우세 기전 | 예 |
|---|---|---|
| 급성 정맥(Acute IV) | Transporter inhibition (예: OATP1B1) | Atorvastatin–rifampin acute |
| 급성 경구(Acute oral) | 수송체 + 장벽/초회통과 | Rosuvastatin–cyclosporine |
| 만성 정맥(Chronic IV) | Enzyme induction onset | Carbamazepine 자가유도 |
| 만성 경구(Chronic oral) | 효소 유도 × 초회통과 × 수송체 복합 | Long-term rifampin/rifabutin |

### PD 상호작용 층위 — 수식 골격

**수용체 수준 PD 상호작용** [G pp.224–227]:

- **다중 결합 부위 모델 (Eq.3:48)** [G p.224]: 한 리간드가 여러 결합 부위에 협동적으로 결합할 때의 반응 곡선. Hill 형태 fitting의 기전적 출처입니다.
- **경쟁적 길항 (Eq.3:49)** [G p.225]:

$$
\underbrace{E}_{\text{효과}}
=
\frac{\overbrace{E_{max}}^{\text{Emax 보존}}\cdot\underbrace{C}_{\text{작용제 C}}}{
\underbrace{C}_{\text{작용제 C}}+
\underbrace{EC_{50}}_{\text{기본 EC50}}
\cdot
\overbrace{(1+A/EA_{50})}^{\text{경쟁 shift}}
}
$$

→ 길항제 A가 들어오면 EC50이 $(1+A/EA_{50})$ factor만큼 **오른쪽으로 이동**하지만 $E_{max}$는 보존됩니다. **더 높은 농도를 쓰면 같은 효과를 회복할 수 있다**는 뜻입니다. 질량 작용 등가성의 분모 구조와 동일합니다.

- **비경쟁적 길항 (Eq.3:50)** [G pp.225–226]:

$$
\underbrace{E}_{\text{효과}}
=
\frac{\overbrace{E_{max}}^{\text{기존 Emax}}}{\underbrace{(1+A/EA_{50})}_{\text{Emax 감소}}}
\cdot
\frac{\underbrace{C}_{\text{작용제 C}}}{\underbrace{C+EC_{50}}_{\text{작용제 potency}}}
$$

→ $E_{max}$가 $(1+A/EA_{50})$로 **감소**하고, EC50은 단순 비경쟁 모델에서 보존됩니다. 효현제 농도를 무한정 올려도 원래 $E_{max}$는 회복되지 않습니다 — **이게 비경쟁적 길항의 임상적으로 다른 결과**입니다.

- **경험적 두 약물 모델 (Eq.3:51, Table 3.2)** [G p.226]: 두 효과가 작용 부위도 기전도 다를 때의 일반화된 합산/곱셈 framework.
- **거울이성질체 상호작용 (Eq.3:52–3:53)** [G p.227]: 같은 receptor의 R/S enantiomer가 서로 다른 affinity를 가질 때. ketamine R-/S- enantiomer 농도-효과 관계가 직접 예시입니다.

**동일 수용체 완전 효현제 조합** [T17 pp.567–570]:

- **Emax 천장 효과 (Eq.17-19~17-21):** 두 완전 효현제가 같은 receptor에 작용하면 **$E_{max}$는 단일 agonist 단독 사용과 같은 ceiling**에 도달합니다. 두 약물의 "더하기"가 효과를 두 배로 만들지는 않는다는 뜻입니다.

$$
\underbrace{E}_{\text{공유수용체 효과}}
=
\frac{
\overbrace{E_{max}}^{\text{공유 Emax}}\cdot
\left(\underbrace{C_A/EC_{50,A}}_{\text{A drive}}+
\underbrace{C_B/EC_{50,B}}_{\text{B drive}}\right)
}{
1+\underbrace{C_A/EC_{50,A}}_{\text{A drive}}+
\underbrace{C_B/EC_{50,B}}_{\text{B drive}}
}
$$

[T17 Eq.17-21; source tag: T17 p.568]

- **등효능선(Isobologram, Fig.17-21):** 일정 효과 수준(예: 50% Emax)을 만드는 두 약물 농도 조합을 $(x,y)$ 평면에 그렸을 때:
  - 직선 = 가산적(단순 mass action 합산)
  - 직선 아래로 휨 = 상승작용(synergy, 예: midazolam–propofol)
  - 직선 위로 휨 = less-than-additive (예: isoproterenol–propranolol antagonism)

- **Greco general response surface (Eq.17-22):** 두 약물의 임의 PD interaction을 한 식으로 통합하는 advanced reference. 본 session의 master card로 독립 확장하지 않고 reference로만 둡니다. [T17 p.569]

🔑 **실무 규칙:** DDI 사례를 검토할 때 **"AUC가 증가했다"로 끝내지 말고, 함께 움직인 Cmax, $t_{1/2}$, V/F, oral/IV ratio를 보세요.** 예를 들어 AUC↑와 $t_{1/2}$↓가 같이 나오면 단순 metabolic inhibition만으로 설명하기 어렵습니다 — distribution/transporter 기전을 의심해야 합니다. [T17 pp.563–565]

**요약:** C6는 단일 기전 모델의 과신을 막습니다. 같은 DDI pair라도 **route, timing, chronicity에 따라 전혀 다른 기전 시그니처**가 나타납니다.

이 카드의 30초 진단 질문(§1.2 전 시그널 통합): **AUC↑와 $t_{1/2}$↓가 같은 case에서 함께 보이는가, 또는 acute IV와 chronic oral 결과가 반대 방향인가?** 둘 중 하나라도 yes면 단일 기전 모델은 부적절합니다 — transporter / induction / PD interaction matrix를 모두 손에 쥐고 진단해야 합니다 (Atorvastatin-Rifampin acute IV signature가 anchor).

> 📖 **Rowland & Tozer p.565, Fig.17-19**: 텍스트만으로는 평평하게 처리되기 쉬운 시그니처를 보여줍니다 — **AUC와 Cmax는 증가하면서 반감기는 감소**할 수 있다는 사실. 이 그림 없이 텍스트로만 보면 해당 사례를 단순 대사 억제로 과도 해석하기 쉽습니다. AUC, Cmax, $t_{1/2}$를 함께 보세요 — 핵심은 단일 지표가 아니라 **지표들의 결합 패턴**입니다.

> 🎯 **§5로 들어가기 전 한 줄** — 혼동쌍은 관측값 하나를 기전 하나로 단정하는 습관을 끊습니다. $CL$, $F$, $C_u$, enzyme clock을 분리해야 합니다.

---

> **C6 체화 핵심**  
> ① `AUC↑와 t½↓가 함께 보일 때` → 단순 metabolic inhibition보다 transporter/distribution signature가 지배  
> ② `acute vs chronic, oral vs IV 결과가 반대일 때` → timing × route × mechanism matrix가 지배  
> ⚡ `DDI를 하나의 mechanism으로 축약` → Cmax/V/F/PD 변화를 놓쳐 임상 권고 실패



<!-- SLIDE_START: §5 | title: 혼동쌍 해부 -->

# §5. 혼동쌍 해부(Confusion Pair Dissection)

## CP1. 용량 의존적 capacity vs 진성 시간 의존 동역학

| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | dose/concentration에 따른 capacity 변화 | 시간에 따른 효소·수송체·생리상태 변화 |
| 수식 내 위치 | $K_m+C$, $V_m-R_0$ 같은 capacity 분모 | $dE/dt=R_{in}-k_{out}E$ 같은 turnover 식 |
| 변화 원인 | 농도 증가, 포화성 대사/수송/재흡수 | 효소 유도, MBI, 회복 지연 |
| 혼동 시 임상 결과 | dose ladder 문제를 time-dependent CL로 오해 → 설계·모니터링 실패 | 시간 의존 변화를 단순 dose nonlinearity로 오해 → trough drift 예측 실패 |

> **⚡ 기억 고리 — *농도 때문인가, 시간 때문인가***  
> MM 동역학에서는 농도가 시간에 따라 줄기 때문에 apparent CL도 변하지만, **enzyme 자체는 변하지 않습니다 — 이건 농도 구동 변화**입니다. True time-dependent kinetics는 **효소량이나 생리학 자체가 시간에 따라 변하는 것**입니다. 진단 기준: "같은 농도에서 시간이 달라도 CL이 다른가?" → 그렇다면 time-dependent 기전입니다.

## CP2. 자가유도(autoinduction) vs 일반적 반복투여 축적(accumulation)

| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | 반복투여에 따른 효소량 변화 | 선형 PK의 투여간격별 축적 |
| 수식 내 위치 | $k_{out}$, enzyme pool, time-varying CL | 축적비, half-life, dosing interval |
| 변화 원인 | autoinduction으로 CL 증가 | 동일 CL에서 input/output equilibrium 형성 |
| 혼동 시 임상 결과 | trough 감소를 adherence 문제나 단순 축적으로 오해 | 자가유도 모델 필요성을 놓침 |

> **⚡ 기억 고리 — *수위 상승 vs 배수구가 넓어짐***  
> 일반 축적은 linear 파라미터만으로 예측 가능한 **수위 상승**입니다. Autoinduction은 enzyme이 시간에 따라 새로 합성되어 처리 능력이 커지는 **배수구 자체가 넓어지는 과정**입니다. 따라서 autoinduction에서 trough는 단순 축적 예측보다 낮고, 정상상태까지의 시간도 enzyme turnover half-life에 묶입니다. **single-dose fit으로 multiple-dose를 예측하면 trough가 systematic하게 과대추정됩니다.**

## CP3. 용량 한계 제거(capacity-limited elimination) vs 혈류/초회통과 효과

| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | intrinsic capacity 제한 | 혈류·초회통과·route effect |
| 수식 내 위치 | $V_{max}/(K_m+C)$, $V_m-R_0$ | $Q_H$, $F_G$, $F_H$, extraction ratio |
| 변화 원인 | 효소/수송체 포화 | 간혈류, gut wall/hepatic first-pass 변화 |
| 혼동 시 임상 결과 | AUC 증가를 F 증가 또는 CL 감소 중 하나로 성급히 단정 | oral/IV 근거 없이 bioavailability 결론 오류 |

> **⚡ 기억 고리 — *공장 한계 vs 도로 한계***  
> Capacity-limited elimination은 **공장(효소)의 최대 처리 능력**이 한계입니다 — 원료(약물)가 아무리 많아도 기계(효소)가 처리할 수 있는 최대치를 넘을 수 없습니다. Flow/first-pass effect는 **도로(혈류)의 용량**이 한계입니다 — 공장이 아무리 빨라도 원료가 도착하는 속도 이상으로 처리할 수 없습니다. 둘 다 AUC/Dose를 증가시키지만 방향이 다릅니다: **공장 한계는 고용량에서 폭발적 비선형성, 도로 한계는 고혈류 상황에서 선형 변화.**

## CP4. 열린 생체 내 결합 vs 닫힌 시험관 내 결합

| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | 유입·청소율·분포가 작동하는 생체 계 | 총량이 고정된 in vitro 결합 계 |
| 수식 내 위치 | $C_u=K^0/CL_u$ | binding equilibrium 식 |
| 변화 원인 | 간·신장 제거, 재분포, unbound clearance | 단백 결합 치환, 고정 총량 |
| 혼동 시 임상 결과 | displacement-only를 지속적 unbound exposure 증가로 과대해석 | 시험관 결과를 생체 용량조정으로 직행 |

> **⚡ 기억 고리 — *열린 계 vs 닫힌 계***  
> In vitro에서는 총 약물량이 고정된 **닫힌 계**이므로 displacement가 생기면 unbound가 지속적으로 높아집니다. In vivo에서는 신장·간이 계속 unbound drug를 제거하는 **열린 계**이므로, displacement 후 새 평형에서 unbound concentration은 제거 속도에 따라 결정됩니다. **In vitro에서 "강한 displacement"라도 in vivo에서 unbound 변화가 임상적으로 의미 없을 수 있는 이유가 여기서 나옵니다.**

## CP5. 치환 단독 DDI(displacement-only) vs 억제 DDI(inhibition)

| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | 결합 자리 치환 | 대사/수송 경로 억제 |
| 수식 내 위치 | $f_u$, $C_u$ 해석 | $CL_{int}$, $f_m/(1+C_{u,I}/K_I)$ |
| 변화 원인 | protein binding displacement | enzyme/transporter inhibition |
| 혼동 시 임상 결과 | total 감소만 보고 dose 감량 | 지속 AUC 증가를 displacement로 축소 해석 |

> **⚡ 기억 고리 — *자리 뺏기 vs 공장 멈추기***  
> Displacement는 결합 자리를 빼앗아 unbound concentration을 **일시적으로** 올리지만, 열린 계에서 새 정상상태로 빠르게 재수렴됩니다 — "자리 뺏기"는 일시적 효과. Inhibition DDI는 **$CL_{int}$를 직접 줄여 약물 처리 공장 자체를 느리게** 하므로 AUC가 지속적으로 증가합니다. 두 기전이 겹치면(warfarin–phenylbutazone) displacement 단독보다 훨씬 큰 AUC 증가가 나타나므로 반드시 분리해서 평가해야 합니다.

## CP6. 가역적 억제 vs MBI

| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | inhibitor 농도 감소와 함께 회복 | enzyme pool 재합성 뒤 회복 |
| 수식 내 위치 | $1+C_{u,I}/K_I$ 경쟁 분모 | $k_{inact}/k_E$, turnover clock |
| 변화 원인 | 가역적 결합 억제 | 효소 기능적 제거와 재합성 지연 |
| 혼동 시 임상 결과 | washout을 inhibitor half-life만으로 설정 | carry-over interaction과 회복 지연 누락 |

> **⚡ 기억 고리 — *문 막기 vs 자물쇠 교체***  
> Reversible inhibition은 **문을 막고 있는 것** — inhibitor가 사라지면 문이 다시 열립니다. MBI는 **자물쇠 자체를 망가뜨린 것** — inhibitor가 없어져도 새 자물쇠(효소)가 합성돼야 회복됩니다. 이 때문에 **MBI 약물을 중단해도 interaction이 enzyme resynthesis 기간(CYP3A4 ≈ 2주) 동안 지속됩니다.** Washout period 설계에서 이 차이를 놓치면 carry-over interaction이 임상 시험 데이터를 오염시킵니다.

## CP7. 억제 vs 유도, 그리고 rifampin 급성/만성 전환

| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | 급성 transporter/enzyme inhibition | 만성 enzyme/transporter induction |
| 수식 내 위치 | $C_{u,I}/K_I$ | $R_{in}$ 증가, enzyme turnover |
| 변화 원인 | acute rifampin OATP 억제 | chronic rifampin CYP/P-gp 유도 |
| 혼동 시 임상 결과 | 같은 rifampin을 항상 exposure 감소로 단정 | timing·route별 상반 방향 예측 실패 |

> **⚡ 기억 고리 — *방향 전환 스위치***  
> Rifampin은 만성 투여 시 **유도자(inducer)** — CYP3A4와 P-gp를 증가시켜 substrate exposure를 낮춥니다. 하지만 급성 IV 투여 시에는 **OATP 억제자** — hepatic uptake를 막아 일부 substrate(atorvastatin)의 Cmax를 10배, AUC를 7배 올립니다. **같은 약이 투여 경로와 시간에 따라 상반된 방향의 interaction을 일으키는 사례입니다.** Timing × Route × Mechanism의 3차원 매트릭스 없이는 방향 예측이 불가능합니다.

## CP8. PK DDI vs PD DDI

| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | 농도-시간 프로파일 변화 | 같은 농도에서 response 변화 |
| 수식 내 위치 | AUC, CL, F, Cmax, t½ | EC50 shift, Emax 감소, isobologram |
| 변화 원인 | 대사/수송/분포 변화 | receptor·효소·생리학적 상호작용 |
| 혼동 시 임상 결과 | response 변화를 모두 concentration 변화로 오해 | PD interaction을 PK 모델 오류로 잘못 처리 |

> **⚡ 기억 고리 — *농도 바꾸기 vs 반응 바꾸기***  
> PK DDI는 농도-시간 프로파일 자체를 변화시켜 response가 달라지는 것(약이 더 많이 쌓이거나 덜 쌓임). PD DDI는 **같은 농도에서 효과 크기가 달라지는 것**(receptor, 효소, 생리학적 경로의 상호작용). 구분 기준: **unbound concentration이 변하지 않는데 response가 달라지면 PD interaction을 의심합니다.** Isobologram이 분리의 실험 도구입니다.



<!-- SLIDE_START: §7 | title: 자기 테스트: 능동 회상 모듈 -->

# §7. 자기 테스트: 능동 회상 모듈(Self-Test: Active Recall Module)

## Q1. [회상]
비선형성 진단에서 dose-normalized concentration-time plot과 AUC/Dose vs Dose plot을 먼저 그리는 이유는?  
**정답:** 선형이면 dose-normalized 관측값이 겹칩니다. 겹치지 않으면 **CL, F, V/distribution, binding, time-dependent process 중 하나가 dose/time의 함수라는 신호**입니다. 즉 이 그림은 "어떤 파라미터가 상수가 아니게 되었는가?"를 묻는 첫 필터입니다. [G pp.112–114], [T16 p.492]

## Q2. [적용]
AUC/Dose가 dose와 함께 증가합니다. 가능한 두 가지 기전은?  
**정답:** **CL 감소 또는 F 증가.** capacity-limited elimination뿐 아니라 first-pass saturation도 가능하므로 **IV/oral 근거가 필요**합니다. [G p.113], [T16 pp.499–506]

## Q3. [회상]
왜 Eq.2:264를 MM ODE citation으로 쓰면 안 되는가?  
**정답:** Eq.2:264는 linear superposition 식입니다. MM clearance/rate/bolus/infusion/input 식은 **Eq.2:266–2:274** 영역입니다. [G pp.114–118]

## Q4. [적용]
Phenytoin 300 mg/day에서 4 mg/L, 500 mg/day에서 36 mg/L가 된 이유를 Eq.16-7의 분모 관점에서 설명하세요.  
**정답:** $C_{u,ss}=K_mR_0/(V_m-R_0)$에서 dosing rate $R_0$가 **$V_m\approx 500$ mg/day에 가까워질수록 분모가 작아져** 농도가 비선형적으로 증가합니다. 전형값은 $K_m\approx 0.4$ mg/L (unbound 기준), $f_u\approx 0.1$이므로 total $K_m'\approx 4$ mg/L. **치료역 10–20 mg/L는 이미 capacity 근처**입니다. [T16 pp.491, 503]

## Q5. [적용]
Ascorbic acid는 **133배 dose 증가**에도 농도가 약 2배만 증가했습니다. phenytoin과 반대 방향의 비선형성이 생긴 이유는?  
**정답:** 농도 상승과 함께 **renal clearance가 saturable reabsorption escape valve로 증가**하기 때문 ($CL_R < 0.5$ mL/min @ 9 mg/L → 21 mL/min @ 19 mg/L, **>42배 증가**). saturable reabsorption은 고농도에서 약물 제거를 가속하는 역방향 비선형성을 만듭니다. [T16 p.492], [T16 pp.507–510]

> 🎯 **Q6 이후로 들어가기 전 한 줄** — $V_{max}$–$K_m$ 식별성, enzyme turnover, $C_u$, $f_m$, route effect를 계산 직관으로 연결해야 답이 흔들리지 않습니다.

---
## Q6. [회상]
MM 모델에서 $V_{max}$와 $K_m$를 따로 추정하려면 어떤 농도 범위가 필요한가? "Vmax–Km Ridge Lock"이란?  
**정답:** **곡률(curvature)을 포함하고, 특히 $K_m$ 주변 또는 그 이하의 농도**가 필요합니다. high-concentration plateau만으로는 $V_{max}/K_m$ ridge가 생깁니다 — single-dose data에서 흔히 $\rho(V_{max}, K_m) > 0.9$ (Gabrielsson p.116에서 −0.96 사례). 이를 **"Vmax–Km Ridge Lock"**이라 부릅니다. **구제:** 용량 수준 추가 또는 $K_m$ prior fix. [G p.116, p.117]

## Q7. [적용]
반복투여 중 trough가 계속 낮아지고 single-dose model은 잘 맞습니다. 어떤 기전을 먼저 의심해야 하는가? 명명 진단으로?  
**정답:** **autoinduction 또는 time-dependent CL 증가** — **"Trough Envelope Drift" + "Single-dose Fit Trap"**의 결합. enzyme turnover compartment와 $k_{out}$ 식별 가능성을 확인합니다. PK22 design에서 $k_{out}\approx 0.023$ h⁻¹, 즉 **enzyme $t_{1/2}\approx 30$ h**가 식별됩니다. [G pp.126–129], [G pp.580–585]

## Q8. [적용]
Clarithromycin 병용 후 midazolam exposure가 multiple dosing에서 더 커지고 회복도 느립니다. reversible inhibition과 어떻게 정량적으로 다른가?  
**정답:** **기전 기반 억제(MBI)는 enzyme activity를 제거**하므로, 회복은 inhibitor 농도 소실뿐 아니라 **enzyme resynthesis/degradation clock**에 묶입니다. 정량값: $k_{inact}\approx 0.07$ min⁻¹, $k_E\approx 0.23$ day⁻¹, $k_{inact}/k_E\approx 438$, $C_{u,I}/K_I\approx 0.025$ → 같은 inhibitor 노출에서 **reversible 식은 1.025배 CL 감소를 예측하지만 MBI 식은 약 11배 CL 감소를 예측**합니다. CYP3A4 회복은 약 **2주** 필요. [T17 pp.557–558]

## Q9. [적용]
Valproate 병용 후 total phenytoin은 낮아졌지만 unbound phenytoin은 유지됩니다. 용량을 줄여야 하는가?  
**정답:** **displacement-only에서는 total이 misleading**할 수 있습니다. **unbound 농도와 임상 반응을 기준으로 판단**해야 하며, total 감소만으로 dose 감량하면 안 됩니다. 열린 계 mass balance ($C_u = K^0/CL_u$)에서는 unbound clearance가 변하지 않는 한 unbound steady state가 유지됩니다. [T17 p.543], [G §2.7.5]

## Q10. [계산 직관]
Affected drug의 $f_m$가 0.8이고 inhibitor가 해당 경로를 강하게 억제합니다. 왜 $f_m=0.3$인 약물보다 AUC ratio가 훨씬 커지는가?  
**정답:** Eq.17-11에서 inhibited pathway term $f_m/(1+C_{u,I}/K_I)$가 작아져도 **residual $(1-f_m)$가 exposure ratio의 바닥을 정합니다.** $f_m=0.8$이면 **남은 경로가 0.2뿐**이라 ratio가 크게 뛰지만, $f_m=0.3$이면 0.7의 우회 경로가 있어 ratio 상승이 제한됩니다. [T17 pp.550–552]

## Q11. [적용]
Oral midazolam interaction이 IV midazolam interaction보다 큽니다. 어떤 기전을 시사하는가? Fluconazole–midazolam 정량 anchor를 인용하세요.  
**정답:** **gut wall/first-pass metabolism component가 크다**는 뜻. fluconazole 400 mg 병용 시 oral midazolam AUC ↑5.6배, IV ↑2배; F 24%→63%; $F_H$ 0.42→0.72; $F_G$ 0.57→0.88로 **$F_G$가 더 큰 비율로 변함** → midazolam의 oral first-pass에 gut wall 기여가 상당함을 의미. [T17 pp.553–554, Fig.17-10]

> 🎯 **Q12 이후로 들어가기 전 한 줄** — PM, rifampin, PD interaction, parent–metabolite, MBI, 보스 딜레마는 모두 **$f_m$, route, timing, recovery clock**을 순서대로 묻습니다.

---
## Q12. [회상]
Eq.17-18의 PM × inhibitor risk가 큰 이유는?  
**정답:** 다형성 경로가 **이미 결손된 PM**에서 남은 비다형성 경로가 inhibitor에 의해 막히면 **잔여 청소율이 매우 작아질 수 있기 때문**입니다. $\text{Maximum exposure ratio}=1/(1-f_m^{POLY}-f_m^{NP})$이므로 **두 항의 합이 1에 가까울수록 ratio가 발산**합니다. [T17 pp.558–559]

$$
\underbrace{\text{Maximum exposure ratio}}_{\text{PM+억제 위험}}
=
\frac{1}{\underbrace{1-f_m^{POLY}-f_m^{NP}}_{\text{남은 CL 여유}}}
$$

## Q13. [적용]
Rifampin 병용에서 acute IV study는 AUC 증가, chronic oral 병용은 AUC 감소를 보일 수 있습니다. 왜 모순이 아닌가?  
**정답:** **acute rifampin은 OATP1B1 같은 transporter 억제**로 hepatic uptake를 차단해 혈중 누적시키고, **chronic rifampin은 enzyme induction**으로 CL을 올려 노출을 감소시킵니다. **timing과 route가 기전을 바꾸는 것**입니다. Atorvastatin-rifampin acute IV: Cmax 10×, AUC 7×, $t_{1/2}$ 8→3h가 직접 anchor (**transporter signature: AUC↑ + $t_{1/2}$↓**). [T17 pp.560–565, Fig.17-19]

## Q14. [적용]
Response는 크게 변했지만 unbound 농도-시간 프로파일은 거의 변하지 않았습니다. 무엇을 의심해야 하는가? 경쟁적 길항과 비경쟁적 길항을 수식 한 줄로 구분하세요.  
**정답:** **PK DDI보다 PD interaction을 의심**합니다. 경쟁적 길항(Eq.3:49)은 $E=E_{max}\cdot C/[C+EC_{50}\cdot(1+A/EA_{50})]$ — **EC50을 shift시키지만 Emax는 보존**됩니다. 비경쟁적 길항(Eq.3:50)은 $E=E_{max}/(1+A/EA_{50})\cdot C/(C+EC_{50})$ — **Emax를 감소**시킵니다. 같은 receptor의 두 full agonist는 Eq.17-21로 Emax ceiling을 공유합니다. [G pp.225–226], [T17 pp.567–570]

$$
\overbrace{E=\frac{E_{max}\cdot C}{C+EC_{50}\cdot(1+A/EA_{50})}}^{\text{경쟁: EC50↑}}
\qquad\text{vs}\qquad
\overbrace{E=\frac{E_{max}}{1+A/EA_{50}}\cdot\frac{C}{C+EC_{50}}}^{\text{비경쟁: Emax↓}}
$$

## Q15. [회상]
Drug–metabolite nonlinear model (G §2.7.6)에서 활성 대사체의 disposition을 parent–metabolite 동시 관측 데이터만으로 추론적으로 외삽하면 안 되는 이유는? 출처 경고와 임상 함의를 답하세요.  
**정답:** Gabrielsson p.137 명시 — "대사체 단독 투여 데이터 없이는 대사체 disposition kinetics에 대한 추가 외삽은 안 됩니다." 모약물과 대사체가 같은 MM 효소를 공유하면 **대사체의 prolonged tail이 (i) 자체 분포 kinetics 때문인지, (ii) 모약물의 saturable elimination이 대사체 형성 속도를 제한하기 때문인지 식별되지 않습니다.** → 임상적으로 활성 대사체의 toxicity/efficacy 기여가 큰 약물(carbamazepine-10,11-epoxide, codeine-morphine 영역)에서는 **대사체 단독 투여 disposition study가 식별성 보강 단계로 필요**할 수 있습니다. [G pp.135–139]

## Q16. [회상]
R&T Table 17-5의 inhibitor strength 분류 기준을 답하세요. Strong/Moderate/Weak는 substrate AUC 변화로 어떻게 구분되는가? MBI는 별도 표시 이유는?  
**정답:** **Strong = ≥5배 AUC 또는 >80% CL 감소; Moderate = 2–5배 AUC; Weak = 1.25–2배 AUC.** MBI inhibitor는 reversible 식만으로 분류하면 강도를 **과소평가**하므로 별도 표시 — 같은 $C_{u,I}/K_I$에서도 **reversible 1.025× vs MBI 11× CL 감소처럼 자릿수 단위로 다른 결과**가 나옵니다. 이 분류는 textbook reference이며 다른 규제문서의 분류 체계와 직접 동일시하지 않습니다. [T17 p.549]

## Q17. [보스 딜레마]
Sponsor가 "inhibitor 병용 시 AUC가 증가하니 label에 일괄 dose reduction을 쓰자"고 합니다. 10분 안에 기전 기반 검토 순서를 말하세요.  
**정답:**  
(1) **affected drug의 $f_m$와 inhibited pathway 확인** — $f_m$가 작으면 강한 inhibitor라도 whole-body AUC ratio는 제한된다 (Eq.17-11);  
(2) **$C_{u,I}/K_I$와 reversible vs MBI 구분** — MBI라면 $k_{inact}/k_E$ 평가 + enzyme recovery clock 고려;  
(3) **oral/IV route effect 확인** — Diltiazem-Lovastatin 1.27 vs 3.57 (Table 17-7) 패턴이면 gut wall first-pass component 우세;  
(4) **PM 또는 잔여 경로 risk 확인** — Eq.17-18 분모 발산 위험;  
(5) **acute/chronic perpetrator effect와 withdrawal sequence 확인** — phenobarbital-dicumarol 3–4주 plateau onset, MBI 2주 recovery washout trap;  
(6) **transporter/multifaceted signature 확인** — AUC↑+$t_{1/2}$↓ 패턴이면 metabolic inhibition이 아니라 transporter;  
(7) **Mass action equivalence triangle 점검** — Eq.2:266 ↔ Eq.16-7 ↔ Eq.17-11이 같은 기전의 다른 표현임을 sponsor에게 명확히 전달.  
단, 여기서는 textbook 기반 기전 체크리스트로만 둡니다. [T17 pp.546–565], [G pp.115–118]

**요약:** Self-test는 식 암기가 아니라 **기전 분류(triage)**를 묻습니다. 각 답은 "어떤 파라미터가 상수가 아니게 되었는가?"로 되돌아가야 합니다.

---

> 🎯 **§8로 들어가기 전 한 줄** — 마지막에는 모든 세부식을 **mass action 분모와 기전 분류로 회수**해야 합니다. 그래야 PopPK, TDM, DDI, PD 모델링이 같은 언어를 씁니다.

---


<!-- SLIDE_START: §8 | title: 메타프레임 및 전체 조망 -->

# §8. 메타프레임 및 전체 조망(Meta-Frame & Big Picture)

## 8.1 한 페이지 기억 모델

Session 08의 기억 모델은 다음 일곱 문장으로 고정합니다. 세부식을 외우기 전, **기전 분류 순서를 유지하기 위한 압축본**입니다.

1. **비선형성은 중첩 원리 실패(superposition failure)로 발견합니다.** [G pp.112–114], [T16 p.492]
2. **용량 한계(capacity limitation)는 $CL(C)$를 만들고, $R_0\to V_m$에서 정상상태가 발산합니다.** [G pp.115–119], [T16 pp.500–506]

$$
\underbrace{CL(C)}_{\text{농도의존 CL}}
\qquad;
\qquad
\underbrace{R_0\to V_m}_{\text{R0→Vm}}
\Rightarrow
\underbrace{C_{ss}\uparrow\uparrow}_{\text{Css 급상승}}
$$

3. **시간 의존성은 효소/수송체/생리학 시계가 약물 농도 시계와 분리될 때 생긴다.** 주 시계 = $\max(t_{1/2}^{enzyme}, t_{1/2}^{inducer}, t_{1/2}^{drug})$. [G pp.119–129], [T16 pp.516–519], [T17 pp.560–561]
4. **결합은 total을 속이고, 열린 계에서는 $C_u=K^0/CL_u$ 물질 수지가 비결합 노출을 강제합니다.** [G pp.129–134], [T17 pp.538–544]

$$
\underbrace{C_u}_{\text{자유 노출}}
=
\frac{\underbrace{K^0}_{\text{입력}}}{\underbrace{CL_u}_{\text{자유 CL}}}
$$

5. **DDI 예측은 $f_m$, 억제제 강도($C_{u,I}/K_I$, $k_{inact}/k_E$), 투여 경로, PM/잔여 경로, 유도/MBI 회복을 함께 봅니다.** [T17 pp.546–561]

$$
\underbrace{f_m}_{\text{경로몫}}
\quad;
\quad
\underbrace{C_{u,I}/K_I}_{\text{가역 억제}}
\quad;
\quad
\underbrace{k_{inact}/k_E}_{\text{MBI/회복}}
$$

6. **복합 DDI와 PD 상호작용은 "AUC 하나"로 기전을 단정하지 못하게 합니다.** Cmax, $t_{1/2}$, V/F, 경구/정맥 비율, 등효능선(isobologram)을 함께 봅니다. [T17 pp.563–570]
7. **질량 작용 등가 삼각형:** 비선형 PK·TDM·DDI 직관은 같은 분모 구조의 다른 표현입니다 (Eq.2:266 ↔ Eq.16-7 ↔ Eq.17-11). 상세 비교는 C5에서 확인하세요. [G p.115], [T16 p.503], [T17 p.550]

## 8.2 후속 계량약리학 작업의 의존성

| 후속 세션 | 이 세션에서 열리는 개념 | 이 세션 없으면 실패하는 것 |
|---|---|---|
| PopPK 모델 구축 | 비선형 CL, 시간 변동 CL, 결합 비선형성, 수송체 DDI 구분 | 파라미터 변동성이 기전 오류를 가림 |
| TDM | phenytoin형 capacity limitation, total-only monitoring 한계, plateau 도달 시간 발산 | 작은 용량 변화와 치환/결합 상황을 잘못 해석 [T16 pp.491–506], [T17 p.543] |
| DDI 연구 해석 | reversible inhibition, MBI, induction, transporter, route effect 분리 | 약물 시작/중단 권고 오류 [T17 pp.546–565] |
| 약물-대사체 모델링 | parent–metabolite 동시 관측의 식별성 한계 | metabolite disposition을 부당하게 외삽 [G pp.135–139] |
| PD 상호작용 모델링 | EC50 이동, Emax 감소, Emax ceiling, isobologram | PK 변화 없는 response 변화를 PK 모델 오류로 오해 [G pp.224–227], [T17 pp.567–570] |

**최종 요약:** 이 장의 최종 골격은 **"비선형성 진단 → capacity/time/binding 기전 식별 → DDI 예측으로 옮기기 → route/timing/unbound/PM 함정 피하기 → mass action equivalence triangle로 회수"**입니다. 이 골격을 PhD 1년차가 확실히 체화하면 비선형 PK와 DDI 챕터의 대부분은 암기가 아니라 기전 분류로 회수됩니다. 정량 anchor는 수식 골격을 임상 정량값으로 채워, "수식을 외운 것"이 아니라 **"수식을 임상 case에 즉시 매핑할 수 있는 것"**으로 학습 목표를 끌어올립니다.

<!-- v3.8 변환 노트
- 활자량: v3.7 1131줄 / 99,792 bytes → v3.8 1086줄 / 88,977 bytes (bytes 기준 약 11% 감축)
- 보존 감사 결과:
    · SLIDE_START 마커: v3.7=11, v3.8=11 (v3.7 line 1121의 12번째 'SLIDE_START' 문자열은 자가검증 체크리스트 항목명으로 PART B 흔적이라 제거됨)
    · 수식 블록($$): v3.7=53, v3.8=53 — 동일 LaTeX 중복 0건
    · 출처 anchor: [G p.]=21=21, [T16 p.]=16=16, [T17 p.]=18=18
    · 약물명·수치: phenytoin·ascorbic·clarithromycin 모두 ±1 (문장 통합·재맥락화로 동일 수치 anchor 100% 보존)
- 주요 변환: 메타 문구(학습자 네비, §1.5 정독 경로 분기, 그림 권한 안내, "본 Content Lock", "확인 시점/학습 지시" 등) 제거, 자기참조 해소, 약물 예시 즉맥락화, 콜아웃 단일화, 자가검증 체크리스트 (PART B 흔적) 제거
- 분량 목표 (§2.3 40–55%) 미달 사유: Ch.08은 비선형 PK + DDI 통합 챕터로 §3 HARD PRESERVE 항목(수식 53개·정량 anchor·약물명·출처·임상 장면)의 밀도가 매우 높음. 컨텐츠 보존을 우선해 활자량 감축률은 §2.3 목표보다 낮게 마무리함 (사용자 요청: "컨텐츠 손실 없도록").
-->

# 08_HTML Compile Input Master — v3.5.3

> **v3.6.1 note:** This version applies a Compact Equation Annotation + Section Core Declaration Patch to PART A only. OP-1: All "Annotated equation — 수식 해부" bullet lists (항별 의미·실무 직관·오해 방지) removed; underbrace/overbrace labels refined for compactness and clarity from a pharmacometrics expert perspective. OP-2 (Replace mode): All per-slide 핵심 메시지 blocks removed; replaced by SECTION_CORE markers with single-line vivid 핵심 요지 declarations at thematic section boundaries. All SLIDE_START markers, figure markers, page tags, source labels, numerical anchors, tables, code blocks, and PART B content are preserved unchanged from v3.6.

> **v3.6.1 보존 검증 통과:** OP-1(수식 bullet 제거·레이블 정제) + OP-2(슬라이드별 핵심 메시지 전부 제거·SECTION_CORE 핵심 요지 삽입) 외 원문 무변경 확인. SLIDE_START 마커 수·figure marker·page tag·source label·수치 anchor·표·코드·PART B 전부 보존. 잔존 핵심 메시지 행: 0건.


## 출처 및 범위 노트

이 장은 Gabrielsson & Weiner의 nonlinear PK 관련 범위와 Rowland & Tozer Ch.16–17의 nonlinearities/DDI 범위를 바탕으로 합니다. 핵심 범위는 nonlinear PK, Michaelis–Menten, mechanism-based inhibition, nonlinear binding, drug–metabolite model, DDI, mass-action equivalence triangle입니다. 교과서 원본 그림은 직접 복제하지 않고, `FIGURE_POINTER`는 원본 그림 확인 위치를 안내하며 `FIGURE_SCHEMATIC`은 새 해설 도식으로 제시합니다. 첨부 출처 범위 밖의 규제 지침 직접 인용, 특정 허가문구, CPIC/민족 빈도, 전체 NONMEM 코드, 출처가 확인되지 않은 외부 주장은 학습 본문 근거로 사용하지 않습니다. 기존 page tag, source label, 수식, 수치 anchor, figure marker 구조는 원안 기준을 유지합니다.
<!-- SECTION_CORE: SC-01 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** $AUC/Dose$로 선형성 실패를 먼저 잡고, capacity·time·binding·DDI로 분기해야 비선형 PK가 암기 목록이 아니라 판단 순서가 된다.

---
<!-- SLIDE_START: S01 | title: PART A 학습 본문 시작 | source_anchor: part-a -->

## PART A — Learner-Facing Complete Handout

<!-- SLIDE_START: S02 | title: 학습자 네비게이션 안내 | source_anchor: learner-navigation -->

## 학습자 네비게이션 안내

**이 자료 활용법:** PART A는 학습자 본문입니다. §1을 한 번 읽어 기전 분류(mechanism triage) 지도를 파악한 뒤, C1–C6를 순서대로 학습하세요. FIGURE_POINTER 블록은 교과서 원본 그림을 직접 확인하라는 안내이고, 마지막으로 §5 혼동쌍과 §7 자기테스트로 마무리하세요.

**학습 순서:**
1. 중첩 원리(superposition)와 용량 보정 노출(dose-normalized exposure) 패턴으로 비선형성을 진단합니다.
2. 용량(capacity), 시간(time), 결합(binding), DDI/수송체(transporter), PD 상호작용 중 유력한 기전을 식별합니다.
3. 해당 기전을 모델링, TDM, DDI 해석으로 번역합니다.
4. §5 혼동쌍과 보스 딜레마(Boss Dilemma, §7)로 자기점검합니다.

**그림 권한 안내:** 교과서 원본 그림은 이 파일에 수록되지 않습니다. `FIGURE_POINTER` 블록은 교과서 해당 그림을 직접 찾아보라는 텍스트 안내이며, `FIGURE_SCHEMATIC` 블록은 교과서 원본 복제가 아니라 새 해설 도식으로 제시됩니다.

---

<!-- SECTION_CORE: SC-02 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** 비선형 PK의 첫 질문은 선형성 파괴 여부가 아니라 $V_{max}/K_m$, $f_u$, $f_m$ 중 어떤 병목이 관측값을 흔드는가이다.

---
<!-- SLIDE_START: S03 | title: 세션 헤더 및 로드맵 | source_anchor: section-1-roadmap -->

# §1. 세션 헤더 및 로드맵(Session Header & Roadmap)

<!-- MASTER LENS -->
이번 세션의 한 문장 핵심은 다음입니다. **비선형 PK는 "선형 중첩 원리(superposition)가 깨지는 현상"에 머무르지 않습니다. 즉, 용량(capacity)·시간(time)·혈류(flow)·결합(binding)·상호작용(interaction) 중 어느 물리적 병목이 농도, 시간, 투여 경로(route), 환자 유전형(genotype)과 결합하여 비선형성을 만드는지를 식별하는 문제입니다.**

<!-- ANNOTATION -->
중첩 원리(superposition)(← 용량 보정 프로파일(dose-normalized profile)이 겹치는 성질)는 여기서 진단 출발점일 뿐입니다. Gabrielsson은 이 문제를 기전(mechanism)과 ODE로 보여주고, Rowland & Tozer Ch.16은 phenytoin·alcohol·ascorbic acid 같은 임상 용량-반응 비대칭으로 보여 줍니다. Ch.17은 그 비대칭이 약물 상호작용(drug interaction)의 AUC ratio, 유도 시간 경과(induction time course), PM 위험, 투여 경로 효과(route effect)로 확장되는 방식을 보여 줍니다. [G pp.112–114], [T16 pp.491–492], [T17 pp.531–532]

<!-- ANCHOR -->
읽는 순서는 진단 → capacity → time → binding → DDI → PD interaction입니다. 먼저 dose-normalized plot으로 "선형이 아닌지"를 확인합니다. 그 다음 $V_{max}/K_m$, enzyme turnover, $f_u$(← unbound fraction, plasma protein에 결합되지 않은 자유 약물 분율 — pharmacologic activity와 unbound clearance를 결정합니다) [v3], $f_m$, route/extraction을 순서대로 점검합니다.

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{V_{max}/K_m}_{\text{저농도 기울기}}\quad;
> \quad\underbrace{f_u}_{\text{fu: 자유분율}}\quad;
> \quad\underbrace{f_m}_{\text{fm: 경로몫}}
> $$

<!-- ANNOTATION -->
$f_m$(← 해당 경로가 담당하는 제거 비율)은 DDI 예측에서 "막힌 경로가 전체 제거에서 얼마나 큰가"를 묻는 변수입니다. 이 순서를 어기면 nonlinear 모델(model)을 fitting할 수는 있어도, 왜 파라미터(parameter)가 흔들리는지는 설명하지 못합니다. [G p.113], [T16 p.492], [T17 pp.532–533]

<!-- SLIDE_START: S04 | title: 지식 그래프 위치 | source_anchor: section-1-1-knowledge-graph -->

## 1.1 지식 그래프 위치

| 층위(Layer) | 질문 | 대표 기전(Mechanism) | 실패 시그널 |
|---|---|---|---|
| 진단(Diagnostics) | 농도/노출이 용량(dose)에 비례하는가? | 중첩 원리(superposition), AUC/Dose vs Dose | 용량 보정 곡선(dose-normalized curve)이 겹치지 않음 |
| 용량(Capacity) | 병목이 용량 한계인가? | MM 대사/수송, 포화성 초회 통과(first-pass) | 작은 용량 변화가 큰 Css 변화를 만듭니다 |
| 시간(Time) | 파라미터가 시간에 따라 바뀌는가? | 효소 전환(enzyme turnover), 유도(induction), MBI | 최저농도 포락선 이동(trough envelope drift), 지연 독성/회복 |
| 결합(Binding) | 총 농도(total concentration)가 오해를 유발하는가? | 포화성 단백/조직/표적 결합 | 총 농도 vs 비결합 프로파일이 서로 다른 결론 |
| DDI | 다른 약물이 CL/F/V/PD를 바꾸는가? | 억제(inhibition), 유도(induction), 수송체(transporter), PD 상호작용 | AUC ratio, 투여경로 차이, PM 증폭 |

<!-- SLIDE_START: S05 | title: 거장의 30초 진단 시그널 | source_anchor: section-1-2-diagnostic-signals -->

## 1.2 거장의 30초 진단 시그널

> **실무 렌즈(Practice Lens) — [CRUCIBLE_DERIVED + TEXTBOOK_DERIVED]**  
> 30년차 모델러는 raw data plot을 보는 첫 30초 안에 다음 6개 시각/패턴 시그널로 mechanism 후보를 좁힙니다. 각 시그널은 그 자체로 진단이 아니라 **"다음에 어떤 검증을 할 것인가"의 출발점**입니다.

| # | 시그널 (원시 데이터 관찰) | 1차 의심 기전 | 검증 단계 |
|---|---|---|---|
| 1 | semi-log concentration plot에서 **terminal slope이 dose에 따라 달라짐** | MM capacity ($V_{max}/K_m$ saturable elimination) | dose-normalized curve 중첩 여부 확인 [G p.116, Fig.2.89] |
| 2 | 같은 dose 반복투여에서 **trough가 systematic 한 방향으로 이동** | autoinduction 또는 time-dependent CL | single-dose vs multi-dose model fit 차이 확인 [G pp.580–585, PK22] |
| 3 | total CLR은 **불변**인데 unbound CLR이 **변함** | nonlinear plasma protein binding (binding nonlinearity, **metabolic induction 아님**) | $f_u$를 용량 수준(dose level)별로 측정 [T16 pp.511–516] |
| 4 | inhibitor 병용에서 **oral interaction > IV interaction** | gut wall/first-pass metabolism component 우세 (단순 hepatic CL inhibition 아님) | IV/oral crossover 또는 $F_G$, $F_H$ 분리 [T17 pp.553–554] |
| 5 | $V_{max}/K_m$ 값이 **hepatic blood flow $Q_H$에 근접** | flow-extraction 분기 (high-extraction ↔ low-extraction 전환점); ethanol prototype | $E_H$(← extraction ratio, 한 번 간을 통과할 때 제거되는 약물 분율; $E_H=CL_H/Q_H$, 0–1 범위) [v3] 계산 후 well-stirred model 가정 점검 [G p.140, Fig.18.4] |
| 6 | single-dose model fit이 multiple-dose에서 **systematic over/underprediction** | time-dependent kinetics (autoinduction, MBI, withdrawal trap 후보) | enzyme turnover compartment 추가 시도 [G pp.580–585], [T16 pp.516–519] |

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{E_H}_{\text{간 추출분율}}
> =
> \frac{\underbrace{CL_H}_{\text{간 CL}}}{\underbrace{Q_H}_{\text{QH 혈류}}}
> \qquad;
> \qquad
> \underbrace{V_{max}/K_m}_{\text{저농도 처리능}}\approx \underbrace{Q_H}_{\text{혈류한계}}
> $$

이 6개 시그널은 §2 C1–C6의 진단 어휘로 그대로 회수됩니다. 학습자는 이 표를 처음 보고 외우지 않아도 되며, 각 §2 카드의 "진단 시그니처" 섹션에서 다시 만나면서 의미가 누적되도록 설계되었습니다.

<!-- RECAP -->
**요약(Recap):** 이 세션은 "비선형 PK = 용량 비례 실패(dose-proportionality failure)"에서 멈추지 않습니다. 최종 목표는 비선형성의 원인을 근원 기전(source mechanism)으로 분해하고, 실험 설계·TDM 해석·PopPK 모델 진단·DDI 위험 예측으로 번역하는 것입니다.

---

<!-- SLIDE_START: S06 | title: Session 08 기전 분류 지도 | source_anchor: figure-session-08-mechanism-map -->

<!-- FIGURE_SCHEMATIC -->
Title: Session 08 기전 분류 지도
Mode: N
Visual objective: 학습자가 5초 안에 이 세션이 비선형 PK 사실의 목록이 아니라 의사결정 경로임을 볼 수 있어야 합니다.
Core message: 중첩 원리(superposition) 실패에서 시작한 뒤, 기전을 용량(capacity), 시간(time), 결합(binding), DDI/PD 상호작용으로 분류하고, 이를 PopPK/TDM/DDI 의사결정으로 번역합니다.
Elements to include: 진단 진입 노드; 용량 보정 도표(dose-normalized plot) 트리거; 용량, 시간, 결합, DDI/PD 기전 분기; 모델 진단, TDM 해석, DDI 예측으로 이어지는 하위 산출물; 순서 화살표.
Elements to exclude: 교과서 그림 패널; 사례별 정량값; 도식 내부의 source-page citation; 규제 label 문구.
Suggested rendering: Mermaid
Caption: Session 08은 중첩 원리 실패에서 계량약리학 의사결정으로 이어지는 기전 분류 워크플로로 구성됩니다.
Alt text: 중첩 원리 실패에서 시작한 흐름도가 용량, 시간, 결합, 상호작용 기전으로 갈라지고, 각 기전이 모델링, TDM, DDI 해석으로 이어집니다.
Source relation: 신규 설계
<!-- /FIGURE_SCHEMATIC -->

<!-- SECTION_CORE: SC-03 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** $AUC/Dose$와 dose-normalized profile을 먼저 그려라 — 여기서 $CL$, $F$, 분포, 결합, 시간 의존성의 다음 검증 축이 갈린다.

---
<!-- SLIDE_START: S07 | title: 개념 해부 카드 | source_anchor: section-2-concept-cards -->

# §2. 개념 해부 카드(Concept Anatomy Cards)

<!-- SLIDE_START: S08 | title: C1 비선형성 진단 | source_anchor: c1-nonlinearity-diagnostics -->

## C1. 비선형성 진단(Nonlinearity Diagnostics) — 중첩 원리(superposition)가 깨지는 순간부터 시작합니다

<!-- MASTER LENS -->
**핵심 아이디어(Big Idea):** 비선형성의 첫 진단은 "모델을 무엇으로 짤까?"가 아닙니다. 같은 route·formulation·method에서 dose-normalized concentration-time profile, AUC vs Dose, AUC/Dose vs Dose가 superimpose되는지 확인하는 것입니다. 선형이면 dose-normalized 관측값이 겹칩니다. 비선형이면 clearance, bioavailability, distribution, binding 중 적어도 하나가 dose 또는 time의 함수가 됩니다. [G pp.112–114], [T16 p.492]

<!-- SLIDE_START: S09 | title: C1 핵심 해부 | source_anchor: c1-core-anatomy -->

### 핵심 해부(Core Anatomy)

- **중첩 원리(Superposition principle):** 선형 PK에서는 용량(dose)을 두 배로 하면 농도(concentration)와 AUC도 두 배가 됩니다. [G pp.113–115], [T16 p.492]
- **용량 보정 AUC 패턴(Dose-normalized AUC pattern):** $AUC/Dose$가 용량(dose)과 함께 증가하면 CL 감소 또는 F 증가를 의심하고, 감소하면 CL 증가 또는 F 감소를 의심합니다. [G p.113]

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{AUC/Dose}_{\text{AUC/용량}}
> $$
- **시간 의존 동역학(Time-dependent kinetics)의 정의:** 농도(concentration)가 변해서 파라미터(parameter)가 달라 보이는 것만으로는 시간 의존성(time-dependence)이 아닙니다. 실제 효소량(enzyme amount), 수송체 활성(transporter activity), 관류(perfusion) 같은 생리학적/생화학적 상태(physiological/biochemical state)가 시간에 따라 변해야 합니다. [G p.112], [T16 p.492]

<!-- SLIDE_START: S10 | title: C1 실무 판독 규칙 | source_anchor: c1-practice-reading -->

### 실무 판독 규칙

<!-- TRENCH -->
**실무 팁(Trench Tip):** 비선형 PK 검토에서 첫 그림은 spaghetti concentration-time plot이 아니라 **dose-normalized concentration-time plot + AUC/Dose vs Dose**입니다. 이 두 그림 없이 바로 $V_{max}/K_m$를 적합(fitting)하면 안 됩니다. capacity limitation인지 F 변화인지, time-dependence인지, binding artifact인지 구분하지 못하기 때문입니다. [G p.113]


<!-- RECAP -->
**요약(Recap):** C1의 목적은 비선형성을 선언하는 것이 아니라, 다음 질문을 강제하는 것입니다. "AUC/Dose가 올라갔는가, 내려갔는가, 시간이 지나며 변했는가, total과 unbound가 다른 말을 하는가?"

이 기전(mechanism)에서 30초 진단 질문 (§1.2 #1과 직결): **dose-normalized concentration-time profile이 superimpose되는가?** 이 한 장의 그림이 §2 전체의 진입 결정을 합니다 — 겹치면 선형, 겹치지 않으면 §2 C2~C6 중 어느 카드로 들어갈지가 정해집니다. [v3]

> **실무 체화 요약(Practice Brief) — [EXPERT_INFERENCE, v3]**  
> 원시 농도 도표(raw concentration plot)를 받으면 첫 30분 동안 모델(model)을 짜지 말고, dose-normalized concentration-time plot 한 장과 AUC/Dose vs Dose plot 한 장을 손으로 그리세요. 두 그림의 superposition failure 방향(↑/↓/시간 변화)이 §2의 어느 기전(mechanism) 카드로 들어갈지를 강제합니다. 이 단계를 건너뛰고 곧장 NONMEM에서 비선형 모델(nonlinear model)을 적합(fitting)하면, capacity인지 F 변화인지 binding artifact인지 구분하지 못한 채 파라미터(parameter)만 흔들립니다.

---

> **실무 렌즈(Practice Lens) — [CRUCIBLE_DERIVED]**  
> C1은 기전 명명(mechanism naming) 전에 수행하는 분류(triage) 단계입니다. AUC/Dose 방향만으로 원인을 확정하지 말고, CL·F·distribution·time-dependence 중 어떤 파라미터(parameter)가 상수가 아니게 되었는지를 다음 카드에서 분리해 검증합니다.

<!-- SLIDE_START: S11 | title: C1 비선형성 진단 Figure Pointer | source_anchor: figure-c1-nonlinearity-diagnostics -->

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner, p.113, Fig.2.85 and Fig.2.86
Why this matters: 이 그림들은 비선형성 진단의 시각 문법을 가장 빠르게 익히는 방법입니다. 이 그림이 없으면 $AUC/Dose$ 패턴 인식이 시각적 분류가 아니라 기억에 의존하게 됩니다.
When to look: C1을 읽기 전에 먼저 확인하고, C1 요약(Recap)을 읽은 뒤 다시 한 번 확인하면 됩니다.
Learner instruction: 먼저 $AUC/Dose$ 변화 방향을 확인하세요. 그런 다음 기전 모델 이름을 붙이기 전에, 그 방향을 가능한 CL, F 또는 분포 변화에 대응시켜 보시면 됩니다.
<!-- /FIGURE_POINTER -->

<!-- SECTION_CORE: SC-04 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** MM kinetics는 $K_m+C$ 분모 하나로 $CL(C)$ 감소, rate plateau, $C_{ss}$ 폭증을 동시에 만든다.

---
<!-- SLIDE_START: S12 | title: C2 Michaelis–Menten 용량 한계 | source_anchor: c2-mm-capacity -->

## C2. 용량 한계 Michaelis–Menten 동역학(Capacity-limited Michaelis–Menten Kinetics) — $V_{max}/K_m$가 용량 조정의 비대칭성을 만듭니다

> **[⚡ Apex Concept — v3]** 본 세션의 가장 난해하고 임상·실무 파급력이 큰 단일 개념. 용량-노출 관계가 비례 스케일링이 아닌 mechanism 기반 국면 진단으로 전환되는 핵심 분기점. 아래 Plausible Fallacy + Diagnostic signatures + Practice Brief는 모두 이 카드의 Apex 지위에서 도출됩니다.

<!-- MASTER LENS -->
**핵심 아이디어(Big Idea):** Michaelis–Menten 용량 한계(capacity limitation)는 청소율(clearance)이 상수가 아니라 농도(concentration)의 함수가 되는 상황입니다. 즉, 같은 약물(drug)이라도 농도 영역이 바뀌면 겉보기 청소율(apparent clearance)과 $t_{1/2}$ 해석이 달라집니다. Gabrielsson의 MM clearance는 Eq.2:266–2:274 영역에 속합니다. Eq.2:264는 linear superposition 식이므로 MM ODE의 citation으로 쓰지 않습니다. [G pp.114–119]

<!-- ANNOTATION -->
**거장의 시각 — [CRUCIBLE_DERIVED]:** $V_{max}$와 $K_m$의 분모 구조 $K_m+C$는 substrate–enzyme reversible binding의 **quasi-steady-state assumption (QSSA)**이 만든 질량 작용(mass action)의 산물입니다. 이 분모가 그대로 Stage 3 DDI에서 inhibitor competitive term $K_m(1+C_{u,I}/K_I)+C$로 확장된다 — **즉, C2의 분모와 C5의 DDI 분모는 같은 mass action 골격이 서로 다른 맥락에서 표현된 것입니다.** 또한 $V_{max}/K_m$ 비율이 hepatic blood flow $Q_H$ 근처가 되면 high-extraction ↔ low-extraction 분기점에 도달합니다. → 세 식의 명시적 등식 비교는 **§2 C5 mass action equivalence triangle 참조** [v3 consolidation]. [G pp.115–118], [G p.140 Fig.18.4]

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{K_m+C}_{\text{MM 분모}}
> \quad\Longrightarrow\quad
> \underbrace{K_m\left(1+C_{u,I}/K_I\right)+C}_{\text{억제 분모}}
> $$

<!-- SLIDE_START: S13 | title: C2 핵심 수식 | source_anchor: c2-core-equations -->

### 핵심 수식 및 출처 태그

$$CL(C)=\frac{V_{max}}{K_m+C}$$  

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{CL(C)}_{\text{농도의존 CL}}
> =
> \frac{\overbrace{V_{max}}^{\text{Vmax 처리상한}}}{\underbrace{K_m}_{\text{Km 반포화}}+\underbrace{C}_{\text{현재 C}}}
> $$
[수식 계열(Equation family): G Eq.2:266; source tag: G p.115]

$$Rate=\frac{V_{max}\cdot C}{K_m+C}$$  

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{Rate}_{\text{처리속도}}
> =
> \frac{\overbrace{V_{max}}^{\text{Vmax 상한}}\cdot\underbrace{C}_{\text{기질 C}}}{\underbrace{K_m}_{\text{Km scale}}+\underbrace{C}_{\text{포화구동 C}}}
> $$
[G pp.115–116], [T16 p.494]

Bolus ODE는 $V_{max}$가 농도/시간 단위로 파라미터화(parameterized)되면 $dC/dt=-V_{max}C/(K_m+C)$처럼 쓸 수 있지만, $V_{max}$가 총량/시간 단위이면 용적 보정(volume scaling)이 필요합니다. 따라서 본문에서는 약식 표기로만 사용하고, 주 출처 태그는 Eq.2:266–2:274로 유지합니다. [G pp.115–118]

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{\frac{dC}{dt}}_{\text{C 변화율}}
> =
> -\frac{\overbrace{V_{max}}^{\text{제거상한}}\cdot\underbrace{C}_{\text{현재 C}}}{\underbrace{K_m+C}_{\text{포화분모}}}
> $$

$$AUC=\frac{C^0}{2V_{max}}\Big(K_m+\frac{C^0}{2}\Big)\quad\text{(IV bolus, MM)}$$  

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{AUC}_{\text{AUC 노출}}
> =
> \frac{\underbrace{C^0}_{\text{초기 C}}}{2\overbrace{V_{max}}^{\text{제거상한}}}
> \left(
> \underbrace{K_m}_{\text{Km scale}}+\frac{\underbrace{C^0}_{\text{초기 C}}}{2}
> \right)
> \quad\text{(IV bolus, MM)}
> $$
[G Eq.2:271; source tag: G p.117]

이 AUC 식의 의미는 다음과 같습니다. high-C 영역에서는 농도 감소가 거의 선형이므로 시간평균 농도가 $C^0/2$에 가깝습니다. 반면 농도가 $K_m$ 부근으로 들어오면 소실 속도가 exponential하게 가속되어 시간평균은 그보다 작아집니다. **AUC 안에 $K_m$이 들어와 있다는 것이 용량 한계(capacity limitation)의 수학적 흔적**입니다. [G p.117]

<!-- SLIDE_START: S14 | title: C2 저농도/고농도 극한 | source_anchor: c2-limiting-cases -->

### 두 극한 사례

- **저농도 영역(Low concentration):** $C\ll K_m$이면 $Cl\approx V_{max}/K_m$이고 1차 속도(first-order)처럼 보입니다. [G pp.115–117]
- **고농도 영역(High concentration):** $C\gg K_m$이면 제거 속도(elimination rate)가 $V_{max}$에 접근하고 겉보기 청소율(apparent clearance)은 감소합니다. 이 영역에서는 작은 용량 증가가 불균형적인(disproportionate) AUC/Css 증가를 만듭니다. [G pp.115–119], [T16 pp.500–506]

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{C\ll K_m}_{\text{저농도}}\Rightarrow \underbrace{CL}_{\text{CL 상수화}}\approx \frac{V_{max}}{K_m}
> \qquad;
> \qquad
> \underbrace{C\gg K_m}_{\text{고농도}}\Rightarrow \underbrace{Rate}_{\text{처리속도}}\approx V_{max}
> $$

<!-- SLIDE_START: S15 | title: C2 임상 정량 앵커 | source_anchor: c2-clinical-anchors -->

### 임상 앵커(Clinical Anchors) — 정량 앵커

**1. Phenytoin — 용량 한계(capacity limitation)의 정량 원형(prototype)** [T16 pp.491, 503–506]:

- 전형적 성인 추정값: $V_m\approx 500$ mg/day, $K_m\approx 0.4$ mg/L (unbound 기준), $f_u\approx 0.1$, 따라서 총 농도(total) 기준 $K_m'\approx 4$ mg/L
- 치료역(total): 10–20 mg/L → 이미 $K_m'$의 2.5–5배 영역에 머문다는 의미. 즉 임상 농도 자체가 용량 한계(capacity) 근처라는 뜻입니다
- 도입 임상 사례: 300 mg/day에서 4 mg/L이던 환자가 500 mg/day로 증량 후 36 mg/L → **67% 용량 증가가 9배 농도 증가를 초래**
- 정상상태 분모 방정식:

$$C_{u,ss}=\frac{K_m\cdot R_0}{V_m-R_0}$$  

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{C_{u,ss}}_{\text{Css,u}}
> =
> \frac{\underbrace{K_m}_{\text{Km,u scale}}\cdot\underbrace{R_0}_{\text{투여 속도}}}{\underbrace{V_m-R_0}_{\text{남은 capacity}}}
> $$
[T16 Eq.16-7; source tag: T16 p.503]

이 식의 핵심은 $R_0$가 $V_m$에 가까워질수록 분모(denominator)가 작아진다는 점입니다. 따라서 $C_{u,ss}$는 선형적으로가 아니라 급격히 상승합니다. $K_m$은 unbound concentration 기준이고, total concentration으로 작업할 때의 $K_m'$와 구분해야 합니다. [T16 pp.503–506]

- $V_m$ 민감도: $V_m$ 20% 감소가 $C_{ss}$를 **2배**로 만들고, $V_m$ 20% 증가가 $C_{ss}$를 약 **33% 감소**시킵니다. 즉 capacity 근처에서는 $V_m$의 작은 변화가 $C_{ss}$를 비대칭적으로 흔듭니다. [T16 p.506]

- **정상상태 도달 시간 발산(Time-to-Plateau Divergence, Eq.16-10):** 300/350/400/425 mg/day 각각의 plateau는 6/9.3/16/22.7 mg/L이지만, 그 plateau에 도달하는 시간은 용량(dose)이 $V_m$에 가까울수록 **수일에서 수주로 발산**합니다. 용량 한계 근처에서는 모니터링 간격을 정상상태 도달 추정 이후로 옮겨야 한다는 임상 함의로 직접 연결됩니다. [T16 Fig.16-10, p.505]

- **혼합 경로(Mixed Pathway, Eq.16-11):** 한 약물의 제거 경로 중 nonlinear 경로의 비중 ($f_m^{NL}$)이 0.5 이상이면 용량-반응 비대칭이 임상적으로 의미 있는 수준으로 나타납니다. [T16 p.506]

**2. Alcohol(에탄올)** [T16 pp.500–502], [G pp.139–141], [G pp.556–562]:

- 근사값(Approximate): $V_m\approx 10$ g/hr, $K_m\approx 100$ mg/L, $V_d\approx 42$ L (70 kg) → zero-order 소실에 가까운 임상 직관을 제공합니다
- 임상 앵커(anchor): $1\ 	ext{drink}\approx 14\ 	ext{g}$, $4\ 	ext{drinks/hr}=56\ 	ext{g/hr}$는 $V_m$을 크게 초과하므로 농도가 무한정 누적됩니다. 반대로 $0.5\ 	ext{drink/hr}=7\ 	ext{g/hr}$는 $V_m$ 안에 머무르므로 정상 pseudo-steady state는 $C_{ss}\approx 233$ mg/L 부근입니다. [T16 pp.501–502]

> **검토 메모:** 이 inline LaTeX는 문맥상 `\text{drink}`, `\text{drinks/hr}`, `\text{g/hr}` 표기로 읽는 것이 자연스럽습니다. 단, 원문 보존 원칙에 따라 원 수식 문자열은 수정하지 않았습니다.
- 단, ethanol 사례는 용량(capacity)뿐 아니라 흡수(absorption), 혈류(flow), 시간(time) 인자가 겹치므로 단일 MM 사례처럼 과단순화하지 않습니다.

**3. Ascorbic acid — phenytoin의 거울상(역방향 비선형성)** [T16 p.492]:

- 75 mg/day에서 9 mg/L, 10,000 mg/day에서 약 19 mg/L → **133배 용량 증가가 약 2배 농도 증가만** 만듭니다.
- 이유: 농도 상승과 함께 신장 청소율(renal clearance)이 크게 증가($CL_R < 0.5$ mL/min @ 9 mg/L → 21 mL/min @ 19 mg/L, **>42-fold 증가**) — 포화성 재흡수(saturable reabsorption)의 배출 밸브(escape valve)
- Phenytoin과 ascorbic acid는 같은 "비선형 PK"이지만 임상적 결과는 정반대입니다: phenytoin은 dose 비례 이상의 toxicity 위험, ascorbic acid는 high-dose에서 추가 노출 효율이 급격히 감소.

<!-- SECTION_CORE: SC-05 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** $V_{max}$와 $K_m$는 곡률 구간을 통과한 데이터 없이는 ridge에 묶인다 — 수렴 성공을 예측 성공으로 착각하지 마라.

---
<!-- SLIDE_START: S16 | title: C2 설계 및 적합 시사점 | source_anchor: c2-design-fitting -->

### 설계 및 적합 시사점

<!-- TRENCH -->
**실무 팁(Trench Tip):** $V_{max}$와 $K_m$를 따로 추정하려면 농도 범위가 곡률(curvature) 영역을 지나야 합니다. 특히 $K_m$ 주변 또는 그 이하의 관측값이 필요합니다. high-concentration plateau만 있으면 $V_{max}$와 $K_m$가 ridge처럼 같이 움직입니다. [G p.117]

<!-- TRENCH -->
**실무 팁(Trench Tip):** PK18처럼 비선형 적합(nonlinear fit)을 시작하기 전에는 그래프 방법(graphical method)으로 $V_{max}/K_m$, $V_c$, distribution terms의 초기 추정값(initial estimate)을 손산출해야 합니다. nonlinear fitting은 initial estimate에 민감하므로, 손산출 30분이 모델 디버깅(model debugging)을 크게 줄입니다. [G pp.556–562]

<!-- SLIDE_START: S17 | title: C2 진단 시그니처 | source_anchor: c2-diagnostic-signatures -->

### 진단 시그니처(Diagnostic Signatures) — 명명 진단

> **거장의 명명 진단(Master's Named Diagnostic) — [CRUCIBLE_DERIVED]**  
> **"Vmax–Km Ridge Lock"** — 단일 용량 데이터(single-dose data) 또는 좁은 용량 범위 데이터(dose range data)로 $V_{max}, K_m, V_d$ 동시 추정 시 $\rho(V_{max}, K_m) > 0.9$ (Gabrielsson p.116에서 −0.96 사례 보고). $V_d$와 $K_m$ 사이도 −0.95 부근의 음의 상관이 흔합니다. **구제 전략(rescue):** 용량 수준(dose level) 추가, 외부 정보로 $K_m$ 사전 고정(prior fix), 또는 sampling을 $K_m$ 근방까지 낮추어 곡률(curvature)을 포착합니다. [G p.116, G p.117]

<!-- SLIDE_START: S18 | title: C2 Single-dose Fit Trap | source_anchor: c2-plausible-fallacy -->

### 그럴듯한 오해(Plausible Fallacy) — Apex Concept 전용 [EXPERT_INFERENCE, v3]

> **⚠️ 그럴듯한 오해(Plausible Fallacy):** "단일 용량 적합(fit)이 좋으면 다중 투여 예측도 정확하다."
>
> **왜 틀렸는가 — 구조적 분석:** MM 동역학에서 단일 용량 적합(fit)은 $V_{max}$–$K_m$ 공간의 ridge를 따라 **여러 $(V_{max}, K_m)$ 조합이 동일한 적합 결과를 만들 수 있습니다.** 단일 용량 데이터는 한 시점의 농도 궤적만 제약하지 분모 $K_m+C$의 곡률 영역을 좁게만 통과하기 때문입니다. 다중 투여로 농도가 trough까지 떨어지고 다시 쌓이는 동안, 같은 $V_{max}/K_m$ ratio를 갖지만 절댓값이 다른 두 모델은 trough envelope를 **완전히 다른 위치**로 예측합니다. 즉, $V_{max}$ 단독도 $K_m$ 단독도 아닌 **곡률 영역 통과 여부**가 다중 투여 예측 정확도를 결정합니다.
>
> **실무 발현 패턴:** Phenytoin 단일 용량 PK 적합(fitting)으로 다중 투여 $C_{ss}$를 예측한 뒤, 환자에서 독성 농도($>20$ mg/L) 또는 무효 농도($<10$ mg/L)가 나오는 패턴. NONMEM에서는 OFV가 잘 수렴하더라도 $V_{max}$–$K_m$ RSE가 모두 50% 이상이고 $\rho(V_{max}, K_m)$가 음수로 강하게 나오면 즉시 **"Single-dose Fit Trap"**을 의심합니다. 이 패턴이 보이면 단일 모델 fit으로 임상 의사결정을 내리지 말고, 용량 사다리(dose ladder)를 추가하거나 $K_m$를 외부 정보로 사전 고정(prior fix)한 뒤 재추정합니다. [v3]

이 기전(mechanism)에서 30초 진단 질문 (§1.2 #1, #5와 직결): **terminal slope이 dose에 따라 달라지는가, 그리고 $V_{max}/K_m$가 $Q_H$에 근접하는가?** 전자는 capacity-limited elimination을, 후자는 flow-extraction 분기를 가리킵니다. [v3]

<!-- SLIDE_START: S19 | title: C2 핵심 주의사항 | source_anchor: c2-cautions -->

### 핵심 주의사항

AUC 기반 생체이용률(bioavailability) 계산은 청소율(clearance)이 상수(constant)일 때만 안전합니다. CL이 농도 의존적(concentration-dependent)이면 AUC 변화가 F 변화인지 CL 변화인지 분리되지 않으므로, "AUC가 늘었다 = F가 늘었다"로 결론 내리면 안 됩니다. [G p.116]

<!-- ANCHOR -->
C2는 Stage 3 DDI의 수학적 원형입니다. $K_m+C$의 분모 구조를 이해해야 합니다. 그렇지 않으면 inhibitor가 등장해 $1+C_{u,I}/K_I$ factor를 만드는 Eq.17-9–17-11도 새 식처럼 외우게 됩니다. [G pp.115–118], [T17 pp.550–552]

<!-- RECAP -->
**요약(Recap):** MM kinetics의 핵심은 "포화되면 zero-order"가 아닙니다. 핵심은 **CL이 농도의 함수가 되어 용량 조정, AUC 해석, $t_{1/2}$, steady-state 도달 시간이 모두 비선형화된다는 점**입니다.

> **실무 체화 요약(Practice Brief) — [EXPERT_INFERENCE, v3]**  
> 용량 한 단계만 가진 데이터셋으로 $V_{max}$, $K_m$를 적합(fitting)하지 마세요. 손산출(graphical) initial estimate 30분이 NONMEM debugging 시간을 절반으로 줄입니다. NONMEM 출력에서 $\rho(V_{max}, K_m)$가 0.9 이상이거나 $V_{max}/K_m$ RSE가 모두 50% 이상이면 즉시 dose ladder 추가, $K_m$ prior fix, 또는 sampling을 $K_m$ 근방까지 확장하는 옵션 중 하나를 선택해 재추정하세요 — 그렇지 않으면 다중 투여 예측에서 Single-dose Fit Trap에 그대로 떨어집니다.

---

> **실패 모드(Failure Mode) — [TEXTBOOK_DERIVED]**  
> MM kinetics를 "포화되면 zero-order"로만 기억하면 용량 조정(dose adjustment) 판단이 무너집니다. 실무 위험은 $R_0$ 또는 concentration이 capacity 근처로 접근할 때 small dose change가 large exposure change로 바뀌는 비대칭성입니다.

<!-- SLIDE_START: S20 | title: C2 MM capacity Figure Pointer | source_anchor: figure-c2-mm-capacity -->

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner, p.115, Fig.2.88; Rowland & Tozer, p.503, Fig.16-9; Rowland & Tozer, p.505, Fig.16-10
Why this matters: C2는 같은 분모 직관이 세 가지 형태로 나타난다는 점을 보아야 이해됩니다. 즉, 청소율은 감소하고, 속도는 plateau에 도달하며, 임상 정상상태는 용량 한계 근처에서 급격히 민감해집니다.
When to look: C2의 수식을 읽은 뒤, C2 임상 앵커를 읽기 전에 확인하면 됩니다.
Learner instruction: 농도 또는 투여 속도가 용량 한계(capacity)에 가까워질 때 무엇이 변하는지 따라가 보세요. 이 곡선들을 단순한 비례적 용량-반응 도표로 읽으면 안 됩니다.
<!-- /FIGURE_POINTER -->

<!-- SECTION_CORE: SC-06 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** 시간 의존성은 농도 변화가 아니라 enzyme pool의 시계다 — $dE/dt=R_{in}-k_{out}E$를 보지 않으면 induction과 MBI를 놓친다.

---
<!-- SLIDE_START: S21 | title: C3 시간 의존적 전환과 MBI | source_anchor: c3-time-dependent-turnover-mbi -->

## C3. 시간 의존적 전환과 기전 기반 억제(Time-dependent Turnover and Mechanism-Based Inhibition) — 농도 시계와 효소 시계를 분리합니다

<!-- MASTER LENS -->
**핵심 아이디어(Big Idea):** 시간 의존적 약동학(time-dependent kinetics)은 농도가 달라져서 청소율이 달라 보이는 현상이 아닙니다. 효소/수송체/생리학 자체가 시간에 따라 변하는 현상입니다. 따라서 약물 농도 시간 경과(concentration time course)와 효소 전환 시간 경과(enzyme turnover time course)라는 두 개의 시계를 분리해서 읽어야 합니다. [G p.112], [G pp.119–129], [T16 pp.516–519]

<!-- ANNOTATION -->
**주 시계(Master clock) 위계 — [CRUCIBLE_DERIVED]:** induction이나 MBI에서는 **세 개의 시계가 동시에 돌아갑니다** — 약물 자체의 $t_{1/2}^{drug}$, perpetrator(inducer/inhibitor)의 $t_{1/2}^{perpetrator}$, 그리고 enzyme pool의 $t_{1/2}^{enzyme} = \ln 2/k_{out}$. 관찰되는 dynamics는 이 셋 중 **가장 느린 시계**가 지배합니다. Phenobarbital–Dicumarol에서 plateau 도달이 3–4주 걸리는 것은 phenobarbital 자체 $t_{1/2}\approx 4$ days가 가장 느려서 induction이 그것에 묶이기 때문입니다. [G pp.119–129], [T17 pp.560–561]

<!-- SLIDE_START: S22 | title: C3 핵심 전환 방정식 | source_anchor: c3-turnover-equation -->

### 핵심 전환 방정식(Turnover Equation)

$$\frac{dE}{dt}=R_{in}-k_{out}E$$  
$$E_{ss}=\frac{R_{in}}{k_{out}}$$  

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{\frac{dE}{dt}}_{\text{효소 변화율}}
> =
> \underbrace{R_{in}}_{\text{효소 생성}}-
> \underbrace{k_{out}E}_{\text{효소 소실}}
> \qquad;
> \qquad
> \underbrace{E_{ss}}_{\text{효소 정상상태}}
> =
> \frac{\underbrace{R_{in}}_{\text{생성속도}}}{\underbrace{k_{out}}_{\text{소실상수}}}
> $$
[G Eq.2:275–2:278; source tag: G pp.120–121]

효소 수준(enzyme level)이 변하면 $CL(t)$가 변합니다. 유도(induction)는 효소량(enzyme amount) 증가로 $V_{max}$ 또는 내인성 청소율(intrinsic clearance, $CL_{int}$ ← 비결합 약물(unbound drug)에 대한 효소/수송체의 본질적 처리 능력; well-stirred model에서 간 청소율(hepatic CL)은 $CL_H=Q_H\cdot f_u\cdot CL_{int}/(Q_H+f_u\cdot CL_{int})$로 표현됩니다) [v3] capacity를 끌어올립니다. 반대로 탈유도(de-induction)나 기전 기반 억제(mechanism-based inhibition)는 효소 활성 회복(enzyme activity recovery)을 $k_{out}$ 시계(clock)에 묶어 처리 능력 회복을 지연시킵니다. [G pp.120–128], [T17 pp.557–561]

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{CL_H}_{\text{간 CL}}
> =
> \frac{\underbrace{Q_H}_{\text{QH 혈류}}\cdot\underbrace{f_u}_{\text{fu: 자유분율}}\cdot\underbrace{CL_{int}}_{\text{CLint 효소능}}}{\underbrace{Q_H}_{\text{혈류한계}}+\underbrace{f_u\cdot CL_{int}}_{\text{fu·CLint}}}
> $$

<!-- SLIDE_START: S23 | title: C3 자가유도 및 타가유도 앵커 | source_anchor: c3-induction-anchors -->

### 자가유도 및 타가유도 앵커

- **PK22 자가유도(autoinduction):** Compound X 반복 주입 데이터(repeated infusion data)에서 자가유도 모델 파라미터(autoinduction model parameter)는 $V_c$, $V_t$, $a$, $k_{12}$, $k_{21}$, $k_{out}$, $E_0$ 7개로 구성됩니다. Table 22.2의 최종 추정값(final estimates) 중 핵심은 $a\approx 0.041$, $k_{out}\approx 0.023$ h⁻¹입니다. 따라서 효소 시상수는 $1/k_{out}\approx 43$ h, $t_{1/2}^{enzyme}\approx 30$ h입니다. 설계 강점(design strength)은 trough sampling이 효소 동역학(enzyme dynamics)의 시간 척도를 직접 포착(capture)하기 때문에 $a$(농도-CL slope)와 $k_{out}$(시간 차원)을 분리 식별할 수 있다는 점입니다. [G pp.580–585], [G p.583]
- **Carbamazepine:** Tozer Ch.16의 자가유도 예시(autoinduction example)로, 전환 시간(turnover time)은 약 5일입니다. 반복투여 첫 1–2주 동안 청소율(clearance)이 시간에 따라 변하는 임상 앵커(anchor)입니다. [T16 p.518]
- **Phenobarbital–Dicumarol:** 유도 시작/종료(induction onset/offset)가 즉시 일어나지 않고 3–4주 scale로 보이는 이유는 유도제/효소 전환 시계(inducer/enzyme turnover clock) 때문입니다. Phenobarbital $t_{1/2}\approx 4$ days가 sustained release처럼 작용하므로 induction plateau도 $4$–$5\ t_{1/2}\approx 16$–$20$일 영역에서 도달합니다. [T17 pp.560–561]

<!-- SLIDE_START: S24 | title: C3 MBI 전환 파괴 기전 | source_anchor: c3-mbi-mechanism -->

### 기전 기반 억제(MBI): 전환 파괴 기전

기전 기반 억제(mechanism-based inhibition, MBI)는 가역적 억제(reversible inhibition)와 달리 효소를 기능적으로 제거합니다.

<!-- ANNOTATION -->
여기서 "제거"는 효소량이 사라진다는 뜻만이 아니라, 효소 활성(enzyme activity)이 회복 전까지 유효하지 않다는 뜻입니다. 회복은 억제제 농도가 사라지는 속도만이 아니라 효소 재합성/분해 시계(enzyme resynthesis/degradation clock)에 의해 제한됩니다.

<!-- SLIDE_START: S25 | title: C3 정량적 MBI 앵커 | source_anchor: c3-quantitative-mbi-anchor -->

### 정량적 MBI 앵커

**Clarithromycin–CYP3A4 MBI** [T17 p.558]:

- $k_{inact}\approx 0.07$ min⁻¹ (포화 억제제 조건의 불활성화 속도, inactivation rate at saturating inhibitor)
- $k_E\approx 0.23$ day⁻¹ (효소 자연 분해 속도상수, enzyme natural degradation rate constant)
- 이로부터 효소 자연 $t_{1/2}\approx \ln 2/k_E \approx 3$ days입니다(CYP3A4 baseline turnover).
- $C_{u,I}/K_I\approx 0.025$ (clarithromycin 임상 노출, clinical exposure)
- $k_{inact}/k_E$ 비율(ratio)은 $\approx 438$입니다. 즉 효소가 자연 전환(turnover)으로 회복하는 속도보다 불활성화(inactivation)가 약 438배 빠릅니다.
- 결과: 같은 $C_{u,I}/K_I=0.025$로 가역적 억제(reversible inhibition)를 평가하면 CL은 1.025배만 감소하지만, MBI 식(Eq.17-13/14)으로 평가하면 **약 11배 CL 감소**를 만듭니다. → 같은 억제제 노출(inhibitor exposure)에서 두 기전(mechanism)의 결과가 한 자리수 차이를 보입니다.
- CYP3A4 활성 회복은 억제제(inhibitor) 중단 후 효소 재합성(enzyme resynthesis)에 묶이며, **2주 또는 그 이상**이 필요할 수 있습니다. → 임상에서 "inhibitor 중단했으니 안전하다"는 timing 가정은 위험합니다.

<!-- ANCHOR -->
Eq.17-13/17-14의 MBI 항(term)은 C3 전환 ODE(turnover ODE)의 정상상태 사고방식을 DDI 예측(DDI prediction)에 붙인 것입니다. 가역적 억제(reversible inhibition)는 "분모에 억제제 경쟁(inhibitor competition)을 더하는 문제"입니다. 반면 MBI는 "효소 풀(enzyme pool) 자체를 줄인 뒤 회복 시계(clock)까지 계산하는 문제"입니다. [T17 p.558]

<!-- SLIDE_START: S26 | title: C3 진단 시그니처 | source_anchor: c3-diagnostic-signatures -->

### 진단 시그니처(Diagnostic Signatures) — 명명 진단

> **거장의 명명 진단(Master's Named Diagnostics) — [CRUCIBLE_DERIVED]**  
> 
> - **"Trough Envelope Drift"**: 같은 dose 반복투여에서 trough가 일정 방향으로 체계적으로(systematic하게) 이동. IIV로 설명하기 전에 시간 변동 CL(time-varying CL)을 먼저 의심합니다. autoinduction이면 trough가 점차 낮아지고, MBI나 자기억제에서는 점차 높아집니다. [G pp.126–129], [G pp.580–585]
> - **"Single-dose Fit Trap"**: 단일 용량 데이터(single-dose data)만 잘 맞는 모델(model)이 반복투여(multiple-dose)에서 체계적 과소/과대예측(systematic over/underprediction)을 보입니다. autoinduction 또는 time-dependent inhibition을 의심합니다. PK22 design rationale의 핵심 — single-dose data만으로는 효소 compartment가 식별되지 않습니다. [G pp.580–585], [T16 pp.516–519]
> - **"Washout Trap"**: MBI에서 perpetrator 중단 후 substrate exposure가 즉시 정상화된다고 가정하면 안 됩니다. 회복은 enzyme clock(2–3 $t_{1/2}$ × $\ln 2/k_E$)에 묶입니다. Clarithromycin MBI에서 회복이 2주에 이르는 것이 그 예입니다. [T17 pp.557–558]

<!-- TRENCH -->
**실무 팁(Trench Tip):** 자가유도 연구(autoinduction study)에서 조밀한 단일 용량 채혈(dense single-dose sampling)만 늘리는 것은 $k_{out}$ 식별에 충분하지 않을 수 있습니다. multiple-dose trough envelope가 enzyme clock을 더 직접적으로 보여 줍니다. [G pp.580–585]

<!-- RECAP -->
**요약(Recap):** C3의 핵심 질문은 "약물 농도가 낮아졌는가?"가 아니라 "enzyme pool이 회복되었는가?"입니다. 이 질문이 induction, autoinduction, MBI, withdrawal trap을 하나로 묶습니다.

이 기전(mechanism)에서 30초 진단 질문 (§1.2 #2, #6과 직결): **반복투여 trough가 systematic 한 방향으로 이동하는가, 그리고 single-dose 모델(model)이 multiple-dose에서 systematic over/underprediction을 보이는가?** 둘 다 yes이면 enzyme clock을 drug concentration clock과 분리해 식별해야 합니다. [v3]

> **실무 체화 요약(Practice Brief) — [EXPERT_INFERENCE, v3]**  
> trough envelope drift가 의심되면 single-dose data만 더 빽빽하게 모으지 말고 **multiple-dose trough sampling 설계**를 추가하세요 — enzyme clock $1/k_{out}$은 multiple-dose에서만 직접 식별됩니다 (PK22 design rationale). MBI가 의심되면 perpetrator 중단 후 substrate exposure를 enzyme half-life × 2~3 기간(CYP3A4의 경우 ~2주) 동안 계속 추적해야 하며, 이 추적 기간을 누락한 study design은 carry-over interaction을 다음 cohort에 그대로 흘려보냅니다.

---

> **체화 메모(Mastery Note) — [EXPERT_INFERENCE]**  
> C3를 읽을 때는 관측값이 concentration clock을 따라 회복되는지, enzyme pool clock을 따라 늦게 회복되는지를 먼저 묻습니다. 이 한 질문이 reversible inhibition, induction, MBI, withdrawal trap을 구분하는 가장 빠른 mental check입니다.

<!-- SLIDE_START: S27 | title: C3 농도 시계 vs 효소 시계 Figure Schematic | source_anchor: figure-c3-two-clocks -->

<!-- FIGURE_SCHEMATIC -->
Title: 비선형 PK의 두 시계: 농도 시계 vs 효소 전환 시계
Mode: N
Visual objective: 학습자가 5초 안에 농도 구동 겉보기 CL 변화와 진성 시간 의존적 효소 풀 변화의 차이를 구분할 수 있어야 합니다.
Core message: 가역적 억제(reversible inhibition)는 주로 가해 약물(perpetrator) 농도 시계를 따르지만, 유도(induction)와 MBI는 효소 전환/회복 시계가 필요합니다.
Elements to include: 왼쪽에는 약물/가해 약물 농도 시계 lane; 오른쪽에는 효소 풀 시계 lane; 가역적 억제, 유도, MBI, 회복 노드; trough drift와 지연 회복 같은 관찰 시그니처로 이어지는 화살표.
Elements to exclude: 정량적 속도상수; 사례별 파라미터 추정값; 교과서 전환 도식의 정확한 재현.
Suggested rendering: Mermaid
Caption: 시간 의존적 동역학에는 두 번째 시계가 필요합니다. 효소 또는 수송체 풀은 혈장 농도 프로파일보다 더 느리게 변합니다.
Alt text: 두 lane 도식이 약물 농도 시계와 효소 전환 시계를 대비시키고, 가역적 억제, 유도, MBI가 서로 다른 회복 패턴으로 어떻게 연결되는지를 보여 줍니다.
Source relation: 신규 설계
<!-- /FIGURE_SCHEMATIC -->

<!-- SECTION_CORE: SC-07 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** 결합 비선형성은 total concentration의 함정이다 — $C_u$, $f_u$, 열린 계 clearance를 먼저 보지 않으면 해석이 뒤틀린다.

---
<!-- SLIDE_START: S28 | title: C4 결합, TMDD, 치환 단독 DDI | source_anchor: c4-binding-tmdd-displacement -->

## C4. 결합, TMDD, 치환 단독 DDI(Binding, TMDD, and Displacement-only DDI) — 총 농도(total concentration)를 그대로 믿지 않습니다

<!-- MASTER LENS -->
**핵심 아이디어(Big Idea):** 비선형 결합(nonlinear binding)은 총 농도(total concentration)와 비결합 농도(unbound concentration)의 관계를 비선형화합니다. 따라서 총 농도만으로 노출(exposure)이나 약효(effect)를 판단하기 어렵다. 특히 열린 생체 계(open in vivo system)와 닫힌 시험관 결합 실험(closed in vitro binding experiment)을 혼동하면, 단백 결합 치환(protein binding displacement)을 실제 비결합 노출 변화로 과대해석하게 됩니다. [G pp.129–134], [T17 pp.538–544]

<!-- ANNOTATION -->
**물질수지(Mass-balance) 강제성 — [CRUCIBLE_DERIVED]:** open system 정상상태에서는 mass balance가 $C_u = K^0/CL_u$ ($K^0$ = unbound input rate, $CL_u$ = unbound clearance)라는 외부 경계조건을 강제합니다. 단백 결합이 어떻게 변하든 정상상태 $C_u$는 그 비율로 강제되며, total concentration이 free fraction 변화에 따라 자유롭게 조정됩니다. 이것이 "open system에서 displacement-only는 unbound steady state를 지속적으로 바꾸지 못한다"는 결론의 수학적 출처다. [G §2.7.5, Eq.2:303]

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{C_u}_{\text{Css,u}}
> =
> \frac{\underbrace{K^0}_{\text{비결합 입력}}}{\underbrace{CL_u}_{\text{비결합 CL}}}
> $$

<!-- SLIDE_START: S29 | title: C4 핵심 결합 방정식 | source_anchor: c4-binding-equation -->

### 핵심 결합 방정식

$$C_b=\frac{n\cdot P_t\cdot C_u}{K_d+C_u}$$  

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{C_b}_{\text{결합 C}}
> =
> \frac{\underbrace{n}_{\text{자리 수}}\cdot\underbrace{P_t}_{\text{총 결합자리}}\cdot\underbrace{C_u}_{\text{자유 C}}}{\underbrace{K_d}_{\text{Kd}}+\underbrace{C_u}_{\text{포화구동 C}}}
> $$
[G Eq.2:294; source tag: G p.129]

Binding site가 saturable이면 total concentration이 크게 변해도 unbound concentration의 해석은 별도로 해야 합니다. Low-extraction drug의 steady state에서는 unbound concentration이 input rate와 unbound clearance에 의해 지배되므로, displacement-only는 total concentration을 낮출 수 있어도 unbound steady-state exposure를 지속적으로 올리지 않는 경우가 많다. [G pp.129–134], [T17 pp.538–544]

<!-- SLIDE_START: S30 | title: C4 열린 계와 닫힌 계 | source_anchor: c4-open-vs-closed -->

### 열린 계 vs 닫힌 계(Open vs Closed System)

- **닫힌 시험관 계(Closed in vitro system):** 총량이 고정되어 치환이 곧 비결합 분율 증가처럼 보입니다. [G pp.131–132]
- **열린 생체 계(Open in vivo system):** 유입, 청소율, 분포가 함께 작동하므로 총 농도 변화가 곧 약리학적 효과 변화는 아닙니다. [G pp.132–134]

<!-- ANNOTATION -->
닫힌 계/열린 계의 차이는 "시험관 안의 총량 고정"과 "몸 안의 지속적 제거·재분포"의 차입니다.

<!-- SLIDE_START: S31 | title: C4 포화성 결합 사례 | source_anchor: c4-saturable-binding-anchors -->

### 포화성 결합 사례 — 정량 앵커

**Plasma protein/tissue binding nonlinearity prototypes** [T16 pp.511–516]:

- **Naproxen:** 0–4 g 경구 dose 범위에서 AUC 비선형. albumin binding saturation이 dose ↑와 함께 $f_u$를 올려 unbound AUC가 total AUC보다 더 가파르게 증가. [T16 Fig.16-17]
- **Cefonicid:** 30 mg/kg i.v. saturable albumin binding의 prototype — 같은 album site 경쟁이 임상 노출을 농도의존적으로 만듭니다. [T16 Fig.16-18]
- **Disopyramide:** α₁-acid glycoprotein 결합의 비선형성 — total CLR과 unbound CLR이 서로 다른 방향 신호를 줄 수 있습니다. [T16 Fig.16-16]
- **Trandolaprilat:** ACE 결합이 nonlinear인 ACE 억제제로, $f_u$가 0.05→0.20 영역으로 dose에 따라 변함. [T16 p.514]
- **Bosentan (TMDD prototype):** dose 증량 시 $V_{ss}$가 $0.67$ → $0.16$ L/kg로 **감소** — high-affinity, low-capacity endothelin receptor target binding이 포화되면서 organ에 잠긴 약물 비율이 줄어들기 때문. 저분자 약물에서도 TMDD 거동이 나타나는 사례. [T16 Fig.16-20, p.515]
- **Dicloxacillin:** $f_u\approx 0.04$, 1 g dose에서 $CL_R \approx 104$ mL/min, 2 g dose에서 $CL_R \approx 63$ mL/min — saturable renal secretion. [T16 Fig.16-13, p.508]

**Salicylic acid — opposing nonlinearities** [T16 Figs.16-27 ~ 16-29, pp.520–522]:

같은 약물에서 **두 개의 비선형성이 반대 방향으로 동시에 작동**하는 사례. 단백 결합 saturation이 $f_u$를 올리고, metabolic capacity saturation이 unbound CL을 떨어뜨립니다. 결과적으로 total $C_{ss}$ vs dosing rate 곡선의 모양은 단일 mechanism으로 설명되지 않는다. **교훈:** 비선형 PK는 단일 mechanism의 단순한 dose-response 곡선이 아닐 수 있습니다. 진단은 mechanism 후보 셋 이상을 동시에 손에 쥐고 진행해야 합니다.

<!-- SLIDE_START: S32 | title: C4 포화성 수송 방정식 | source_anchor: c4-saturable-transport -->

### 포화성 수송 방정식(Saturable Transport Equation) [T16 p.495]

$$Rate=\frac{T_m\cdot C_u}{K_T+C_u}\quad\text{(Eq.16-3)}$$

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{Rate}_{\text{수송속도}}
> =
> \frac{\overbrace{T_m}^{\text{Tm 상한}}\cdot\underbrace{C_u}_{\text{자유 C}}}{\underbrace{K_T}_{\text{KT scale}}+\underbrace{C_u}_{\text{점유 C}}}
> \quad\text{(Eq.16-3)}
> $$

— renal secretion(분비)과 reabsorption(재흡수)는 같은 분모 형태를 공유하나, 방향이 반대라 임상 결과가 정반대로 나타납니다 (e.g., Dicloxacillin은 saturable secretion으로 high dose에서 CLR ↓; Ascorbic acid는 saturable reabsorption escape valve로 high dose에서 CLR ↑).

<!-- SECTION_CORE: SC-08 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** TMDD·metabolite·displacement-only DDI는 모두 계의 경계를 묻는다 — formation, disposition, unbound exposure를 섞지 마라.

---
<!-- SLIDE_START: S33 | title: C4 TMDD 및 조직/표적 결합 | source_anchor: c4-tmdd-target-binding -->

### TMDD 및 조직/표적 결합

표적 매개 약물 disposition(Target-mediated drug disposition, TMDD)은 고친화성(high-affinity)·저용량(low-capacity) 표적/조직 결합(target/tissue binding)이 disposition을 바꾸는 경우입니다. Tozer Ch.16은 저분자 약물(small molecule)에서도 bosentan, imirestat, trandolaprilat, draflazine, mitoxantrone 같은 prototype을 제시하지만, 본 단계에서는 TMDD full mechanistic code나 Mager–Jusko implementation으로 확장하지 않습니다. [T16 pp.511–516]

<!-- SLIDE_START: S34 | title: C4 약물-대사체 비선형 모델 | source_anchor: c4-drug-metabolite-model -->

### 약물-대사체 비선형 모델 — §2.7.6 출처 기반

활성 대사체(active metabolite)가 임상 효과나 독성(toxicity)에 기여하는 약물(carbamazepine-10,11-epoxide, irinotecan-SN38, codeine-morphine 영역)에서는 모약물(parent)과 대사체(metabolite)가 동일한 MM 효소(MM enzyme)를 공유할 때 disposition이 비선형으로 결합됩니다. [G pp.135–139]

- **모델 구조(Model 구조):** 2-compartment drug + 1-compartment metabolite + MM elimination입니다. ODEs는 Eq.2:304–2:308 영역, 파라미터 추정값(parameter estimates)은 Tables 2.18–2.20에 제시됩니다. 이때 metabolite 농도 프로파일에서 prolonged tail이 나타날 수 있습니다. 이것이 metabolite 자체의 분포 kinetics가 아니라 parent의 MM elimination이 metabolite 형성 속도를 제한하기 때문일 수 있으므로, 오독 위험이 높습니다.
- **출처 기반 경고(Source-backed warning):** parent–metabolite 동시 관측만으로는 metabolite의 disposition kinetics를 추론적 외삽(inferential extrapolation)을 해서는 안 됩니다. metabolite를 단독 투여한 disposition 데이터가 없으면 metabolite 청소율·분포·t½가 식별되지 않을 수 있습니다 (G p.137 명시 경고). [G p.137]

<!-- SLIDE_START: S35 | title: C4 Displacement-only DDI 격하 | source_anchor: c4-displacement-only-ddi -->

### Displacement-only DDI 격하

Phenytoin–valproate는 total phenytoin이 낮아져도 unbound phenytoin은 상대적으로 유지되는 displacement-only prototype으로 제시됩니다. 이 사례의 가치는 "용량(dose)을 줄이라"가 아니라 "total concentration만 보고 toxicity/efficacy를 판단하지 말라"는 데 있습니다. [T17 p.543]

Warfarin–phenylbutazone은 단순 displacement만이 아니라 inhibition까지 겹친 multifaceted example로 다루어야 합니다. [T17 p.563]

<!-- TRENCH -->
**실무 팁(Trench Tip):** 단백 결합 비선형성(protein binding nonlinearity)이 의심되는 Phase 1/PopPK package에서는 총 농도(total concentration)만 모으지 말고 용량 수준(dose level)별 $f_u$를 측정하세요. total-only dataset은 binding nonlinearity와 clearance nonlinearity를 서로 구분하기 어렵게 만듭니다. [G pp.129–134], [T16 pp.511–516]

<!-- RECAP -->
**요약(Recap):** C4는 "protein binding이 변하면 위험하다"가 아니라, **total과 unbound가 서로 다른 질문에 답한다**는 원칙을 고정합니다.

이 기전(mechanism)에서 30초 진단 질문 (§1.2 #3과 직결): **total CLR은 불변인데 unbound CLR이 변하는가?** Yes이면 비선형 혈장 단백 결합(nonlinear plasma protein binding, metabolic induction이 아님)을 의심하고 용량 수준(dose level)별 $f_u$를 직접 측정해 검증합니다. [v3]

> **실무 체화 요약(Practice Brief) — [EXPERT_INFERENCE, v3]**  
> binding nonlinearity가 의심되면 total concentration만 모은 데이터셋(dataset)으로 결론 내리지 말고 용량 수준(dose level)별 $f_u$를 직접 측정하는 sub-study를 설계하세요. open vs closed system 구분이 흐릿한 reviewer 질의가 들어오면 mass balance 식 $C_u = K^0/CL_u$ 한 줄로 답할 수 있어야 합니다 — open in vivo system에서는 displacement-only가 unbound steady state를 지속적으로 바꾸지 못한다는 결론이 이 한 식에서 직접 도출됩니다.

---

> **실무 렌즈(Practice Lens) — [TEXTBOOK_DERIVED]**  
> 결합(binding) 문제에서는 총 농도(total concentration) 변화가 곧 약리학적 노출(pharmacologic exposure) 변화라는 가정을 보류합니다. 먼저 unbound concentration, system boundary(open vs closed), 그리고 unbound clearance가 함께 변했는지를 확인합니다.

<!-- SLIDE_START: S36 | title: C4 열린 계 vs 닫힌 계 Figure Pointer | source_anchor: figure-c4-open-closed-binding -->

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner, p.132, Fig.2.104; Gabrielsson & Weiner, p.133, Fig.2.105
Why this matters: C4의 혼동은 계(system)의 경계에 달려 있습니다. 이 그림들이 없으면 학습자는 닫힌 계 결합 직관을 열린 생체 내 해석으로 그대로 옮기기 쉽습니다.
When to look: C4의 열린 계 vs 닫힌 계(Open vs Closed System) 소절을 읽은 뒤 확인하면 됩니다.
Learner instruction: 어떤 양이 고정되어 있고, 어떤 양이 계 밖으로 나갈 수 있는지 비교하세요. 그런 다음 이 경계를 염두에 두고 치환 단독(displacement-only) 경고를 다시 읽으면 됩니다.
<!-- /FIGURE_POINTER -->

<!-- SECTION_CORE: SC-09 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** DDI 크기는 inhibitor 이름보다 $f_m$과 $C_{u,I}/K_I$가 결정한다 — AUC ratio 분모가 victim drug의 취약성을 드러낸다.

---
<!-- SLIDE_START: S37 | title: C5 정량적 DDI 예측 | source_anchor: c5-quantitative-ddi -->

## C5. 정량적 DDI 예측(Quantitative DDI Prediction) — $f_m$, 억제제 강도(inhibitor strength), 투여 경로(route)가 AUC ratio를 만듭니다

<!-- MASTER LENS -->
**핵심 아이디어(Big Idea):** Ch.17의 DDI 정량 프레임워크(framework)는 "상호작용이 있다/없다"를 묻지 않는다. 피영향 약물(affected drug)의 청소율 중 얼마가 억제된 경로(inhibited pathway)에 의존하는지($f_m$), 억제제 노출이 $K_I$에 비해 얼마나 큰지, 투여 경로/초회통과(first-pass)가 얼마나 관여하는지를 묻습니다. [T17 pp.531–532], [T17 pp.546–552]

<!-- ANNOTATION -->
**질량 작용 등가 삼각형(Mass Action Equivalence Triangle) — [CRUCIBLE_DERIVED]:** 본 세션의 수학적 정점은 다음 세 식이 **같은 분모 구조의 다른 표현**이라는 점입니다.

$$\text{Eq.2:266: } CL=\frac{V_{max}}{K_m+C}\quad\Longleftrightarrow\quad \text{Eq.16-7: } C_{u,ss}=\frac{K_m R_0}{V_m-R_0}\quad\Longleftrightarrow\quad \text{Eq.17-11: } \text{AUC ratio}\approx\frac{1}{\frac{f_m}{1+C_{u,I}/K_I}+(1-f_m)}$$

> **Annotated equation — 수식 해부**
>
> $$
> \overbrace{CL=\frac{V_{max}}{K_m+C}}^{\text{C-CL capacity}}
> \quad\Longleftrightarrow\quad
> \overbrace{C_{u,ss}=\frac{K_m R_0}{V_m-R_0}}^{\text{Css 분모 민감}}
> \quad\Longleftrightarrow\quad
> \overbrace{\text{AUC ratio}\approx\frac{1}{\frac{f_m}{1+C_{u,I}/K_I}+(1-f_m)}}^{\text{DDI 경로몫}}
> $$

세 식 모두 기질-효소 가역 결합(substrate-enzyme reversible binding)의 질량 작용(mass action, QSSA)이 만든 같은 골격을 다른 변수로 표현한 것입니다. Eq.2:266은 농도-CL의 질량 작용(mass action) 직접 표현이고, Eq.16-7은 그것의 정상상태 분모 발산 형태이며, Eq.17-11은 억제제(inhibitor)가 분모에 추가되었을 때의 노출 비율(exposure ratio) 형태입니다. **이 세 식을 한 줄로 보면 모든 비선형 PK·DDI 직관이 동일한 질량 작용(mass action) 분모로 회수됩니다.** [G pp.115–118], [T16 p.503], [T17 pp.550–552]

<!-- SLIDE_START: S38 | title: C5 가역적 경쟁 억제 골격 | source_anchor: c5-reversible-inhibition -->

### 가역적 경쟁 억제 핵심 골격

Eq.17-9–17-12는 억제된 경로(inhibited pathway)의 청소율 감소와 전신(whole-body) AUC ratio를 연결합니다. 즉, 한 경로(pathway)의 억제가 전체 노출(exposure)을 얼마나 바꾸는지 계산하는 핵심 골격(spine)입니다. 핵심 직관은 다음입니다. [T17 pp.550–552]

$$\text{AUC ratio}\approx\frac{1}{\frac{f_m}{1+C_{u,I}/K_I}+(1-f_m)}$$

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{\text{AUC ratio}}_{\text{병용 노출비}}
> \approx
> \frac{1}{
> \underbrace{\frac{f_m}{1+C_{u,I}/K_I}}_{\text{억제경로 잔여몫}}
> +
> \underbrace{(1-f_m)}_{\text{우회경로 몫}}
> }
> $$

이 식은 본 자료에서 Rowland & Tozer의 textbook 기반 DDI 식으로만 다룹니다. 첨부 출처 범위를 넘어 특정 규제 지침의 핵심식으로 확장해 해석하지 않습니다. [T17 pp.550–552]

<!-- SLIDE_START: S39 | title: C5 임상 정량 앵커 | source_anchor: c5-clinical-anchors -->

### 임상 앵커(Clinical Anchors) — 정량 앵커

**Theophylline–Enoxacin (Rogge et al. 1989; Enoxacin 400 mg q12h × 4 days)** [T17 pp.546–550, Fig.17-6, Fig.17-7]:

- $t_{1/2}$ 8.8 h → 22 h (2.5배 연장)
- 평균 투여간격 Css(Average interdose Css) 4 mg/L → 9 mg/L (약 2.25배)
- $CL_{inhib}/CL_{normal}=0.44$
- $f_m\approx 0.67$ (CYP1A2 의존성, CYP1A2 dependence)
- Eq.17-9–17-12의 단계적 억제(graded inhibition)를 보여 주는 주요 임상 예시(primary clinical example)입니다. enoxacin 용량(dose)이 낮아지면 억제(inhibition)가 단계적으로 약해진다는 점이 같은 fluoroquinolone 계열(ciprofloxacin > enoxacin > norfloxacin) 비교에서 직접 보입니다.

**Desipramine–Quinidine (CYP2D6)** [T17 pp.549–550]:
- $f_m^{CYP2D6}\approx 0.75$
- CL이 약 4배 감소
- 즉, $f_m$이 높을 때 한 경로(pathway)의 억제가 전신 청소율(whole-body CL)을 거의 같은 비율로 떨어뜨릴 수 있습니다.

**Desipramine–Fluoxetine (Bergstrom 1992; Table 17-11)** [T17 p.552]:
- AUC: 284 → 2110 µg·hr/L (**약 7.4배**)
- $t_{1/2}$: 16.1 h → 63.8 h (약 4배)
- CL/F: 289 → 27.1 L/hr (약 10.7배 감소)
- 같은 desipramine victim에 대해 fluoxetine은 quinidine보다 강한 효과를 보입니다. 이는 fluoxetine 자체의 긴 $t_{1/2}$와 활성 대사체(active metabolite) norfluoxetine까지 더해진 결과입니다.

**Diltiazem–Lovastatin (Table 17-7)** [T17 p.553]:
- AUC ratio: **1.27 (i.v.) vs 3.57 (oral)**
- 즉 경구 상호작용(oral interaction)이 IV보다 약 3배 큽니다. → 장벽/초회통과(gut wall/first-pass) component가 크다는 직접 증거입니다. 간 청소율 억제(hepatic CL inhibition)만으로는 경구·IV 차이를 설명할 수 없습니다.

**Fluconazole–Midazolam (Fig.17-10; fluconazole 400 mg)** [T17 p.554]:
- 경구 AUC(Oral AUC): ↑5.6배
- IV AUC: ↑2배
- F: 24% → 63%
- $F_H$: 0.42 → 0.72 ($F_H$ = 간 생체이용률, hepatic availability)
- $F_G$: 0.57 → 0.88 ($F_G$ = 장벽 생체이용률, gut wall availability)
- $F_G$가 $F_H$보다 더 큰 비율로 변하는 것은 midazolam의 경구 초회통과(oral first-pass)가 장(gut)에 상당 부분 위치함을 의미합니다.

<!-- SLIDE_START: S40 | title: C5 억제제 분류 | source_anchor: c5-inhibitor-classification -->

### 억제제 분류(Inhibitor Classification) — Table 17-5 [T17 p.549]

| 분류 | 기준 (기질 AUC 배수 증가) | 추가 표시 |
|---|---|---|
| 강함(Strong) | ≥5배 또는 >80% CL 감소 | MBI는 별도 (b) 표시(marking) |
| 중등도(Moderate) | 2–5배 | — |
| 약함(Weak) | 1.25–2배 | — |

**기질 민감도 분류(Substrate Sensitivity, Table 17-6):** 강한 억제제와 병용 시 **≥4배 AUC 증가**를 보이는 기질(substrate)이 별도 분류됩니다. 이 분류는 여기서는 textbook reference 기반의 실무 어휘로만 다루며, 다른 규제문서의 분류 체계와 직접 동일시하지 않습니다.

<!-- SLIDE_START: S41 | title: C5 PM × 억제제 증폭 | source_anchor: c5-pm-inhibitor-amplification -->

### PM × 억제제 증폭(PM × Inhibitor Amplification)

Eq.17-18은 다형성 경로(polymorphic pathway)와 비다형성 잔여 경로(nonpolymorphic residual pathway)가 동시에 고려될 때 최대 노출 비율(maximum exposure ratio)이 커질 수 있음을 보여 줍니다. PM 환자에서 남은 비다형성 경로까지 강한 억제제(strong inhibitor)가 막으면 노출 비율이 크게 뛸 수 있습니다.

$$\text{Maximum exposure ratio}=\frac{1}{1-f_m^{POLY}-f_m^{NP}}$$  

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{\text{Maximum exposure ratio}}_{\text{최대 노출비}}
> =
> \frac{1}{
> \underbrace{1-f_m^{POLY}-f_m^{NP}}_{\text{잔여 CL 분율}}
> }
> $$
[T17 Eq.17-18; source tag: T17 pp.558–559]

Fig.17-15의 omeprazole–clarithromycin example은 high ratio 사례로 유지하되, 특정 배수값은 exact printed number가 아니라 시각 추정/확인필요로 취급합니다. 따라서 본문에서는 "매우 큰 exposure ratio example"로만 사용합니다. [T17 p.559]

<!-- SLIDE_START: S42 | title: C5 투여 순서와 중단 | source_anchor: c5-sequence-withdrawal -->

### 투여 순서와 중단(Sequence and Withdrawal)

상호작용은 전무(all-or-none)가 아니라 농도, 시점, 순서, 시작/중단(initiation/withdrawal)에 따라 단계적(graded)으로 나타납니다. 따라서 inhibitor를 추가할 때와 제거할 때의 위험은 대칭이 아닙니다. 유도(induction)/MBI에서는 특히 회복 지연이 치명적입니다. [T17 pp.532–534], [T17 pp.557–561]

<!-- TRENCH -->
**실무 팁(Trench Tip):** DDI 예측표에는 최소한 $f_m$ uncertainty band를 붙이세요. $f_m$가 0.5인지 0.8인지에 따라 같은 inhibitor라도 AUC ratio 해석이 완전히 달라집니다. [T17 pp.550–552]

<!-- RECAP -->
**요약(Recap):** C5의 핵심은 억제제(inhibitor) 이름이 아니라 **affected drug의 pathway dependence**다. $C_{u,I}/K_I$가 커도 $f_m$가 작으면 whole-body AUC ratio는 제한되며, $f_m$가 크면 작은 inhibitor effect도 임상적으로 커집니다.

이 기전(mechanism)에서 30초 진단 질문 (§1.2 #4와 직결): **inhibitor 병용에서 oral interaction이 IV interaction보다 큰가?** Yes이면 gut wall/first-pass metabolism component가 우세합니다 — hepatic CL inhibition만으로 설명하지 마세요. Diltiazem-Lovastatin (1.27 IV vs 3.57 oral)과 Fluconazole-Midazolam ($F_G$ 0.57→0.88)이 직접 anchor입니다. [v3]

> **실무 체화 요약(Practice Brief) — [EXPERT_INFERENCE, v3]**  
> DDI 예측표(DDI prediction table)를 작성할 때 점추정 AUC ratio만 적지 말고 $f_m$ 불확실성 범위(uncertainty band)를 함께 적으세요. 같은 inhibitor + 같은 substrate라도 $f_m$가 0.5인지 0.8인지에 따라 ratio 해석이 임상적으로 갈립니다(예: $C_{u,I}/K_I=10$, $f_m=0.5$이면 ratio $\approx 1.83$; $f_m=0.8$이면 ratio $\approx 3.85$). Inhibitor strength 분류 (Table 17-5)는 textbook reference로만 인용하고, 다른 규제문서의 분류 체계와 직접 동일시하지 마세요.

---

> **판단 렌즈(Judgment Lens) — [CRUCIBLE_DERIVED]**  
> DDI 예측(DDI prediction)에서 $f_m$은 "inhibitor strength가 임상적으로 증폭될 수 있는 구조적 취약성"입니다. 같은 inhibitor라도 victim drug이 해당 pathway에 얼마나 의존하는지에 따라 AUC ratio의 의미가 달라집니다.

<!-- SLIDE_START: S43 | title: C5 AUC ratio Figure Pointer | source_anchor: figure-c5-auc-ratio -->

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer, p.550, Fig.17-8
Why this matters: AUC ratio 식은 베끼기는 쉽지만 직관으로 체감하기는 어렵습니다. 이 그림은 주어진 억제제가 작은 노출 변화만 만들지, 큰 노출 변화를 만들지를 $f_m$이 왜 조절하는지 보여 줍니다.
When to look: C5의 가역적 경쟁 억제(reversible competitive inhibition) 식을 읽은 직후 확인하면 됩니다.
Learner instruction: 먼저 억제제 강도(inhibitor strength)를 고정하고 $f_m$을 움직이며 그림을 읽어 보세요. 그런 다음 $f_m$을 고정하고 억제제 강도를 바꾸어 보시면 됩니다.
<!-- /FIGURE_POINTER -->

<!-- SECTION_CORE: SC-10 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** 복합 DDI와 PD interaction은 AUC 하나로 끝나지 않는다 — $C_{max}$, $t_{1/2}$, $V/F$, route, EC50, Emax를 함께 읽어라.

---
<!-- SLIDE_START: S44 | title: C6 복합/수송체 및 PD 상호작용 | source_anchor: c6-multifaceted-transporter-pd -->

## C6. 복합/수송체 및 PD 상호작용(Multifaceted/Transporter and PD Interactions) — 하나의 가해 약물(perpetrator)이 하나의 기전만 갖는다고 가정하지 않습니다

<!-- MASTER LENS -->
**핵심 아이디어(Big Idea):** 실제 DDI는 대사 억제(metabolic inhibition) 하나로 끝나지 않습니다. 수송체 억제(transporter inhibition), 분포 변화, 장벽/간 초회통과(gut/hepatic first-pass), 유도(induction), PD 가산성/상승작용/길항(additivity/synergy/antagonism)이 겹칠 수 있습니다. 이 때문에 같은 drug라도 급성/만성, 경구/정맥 조건에서 반대 방향 효과를 보일 수 있습니다. [T17 pp.563–567]

<!-- SLIDE_START: S45 | title: C6 복합 기전 앵커 | source_anchor: c6-multifaceted-anchors -->

### 복합 기전 앵커(Multifaceted Anchors) — 정량 앵커

**1. Digoxin–Quinidine (Table 17-8)** [T17 p.564]:
- CL: 140 → 72 mL/min (약 절반)
- CLR: 101 → 51 mL/min (P-gp inhibition으로 renal secretion 감소)
- $V_d$: 500 → 240 L (P-gp inhibition으로 tissue 분포 감소)
- F: 0.75 → 0.85 (intestinal P-gp inhibition으로 absorption 증가)
- → quinidine은 digoxin의 CL, $V_d$, F 셋을 동시에 변화시킨다. 단일 대사 기전(metabolic mechanism)으로는 이 패턴을 모두 설명할 수 없습니다.

**2. Atorvastatin–Rifampin (acute IV; Fig.17-19)** [T17 p.565]:
- Cmax ↑10배
- AUC ↑7배
- $t_{1/2}$: 8 h → 3 h ($t_{1/2}$가 **감소**한다는 점이 단순 metabolic inhibition과 반대)
- 기전(mechanism): 급성(acute) rifampin이 OATP1B1(간 uptake transporter) 억제(inhibition)로 atorvastatin의 간 분포(hepatic distribution)를 차단합니다. → 혈중에 누적되어 Cmax/AUC ↑, distribution-limited terminal phase가 사라져 $t_{1/2}$ ↓.

**3. Rosuvastatin–Cyclosporine (Fig.17-11; heart transplant recipients)** [T17 p.555]:
- Cmax ↑11배
- AUC ↑7배
- 기전(mechanism): cyclosporine이 OATP1B1 + BCRP를 동시에 억제(inhibit)하여 rosuvastatin의 간 흡수(hepatic uptake)와 담즙 배출(biliary efflux)을 모두 차단합니다.

**4. Phenobarbital–Dicumarol (Fig.17-17)** [T17 p.561]:
- Plateau 도달까지 3–4주 (vs 즉시 효과 가정 위반)
- 이유: phenobarbital $t_{1/2}\approx 4$ days가 유도 시작(induction onset)의 rate-limiter입니다. $4$–$5\ t_{1/2}\approx 16$–$20$일 영역에서 inducer가 정상상태에 도달하고, 그 이후에 효소량(enzyme amount)이 새 plateau로 진입합니다.
- 이것이 §2 C3에서 본 주 시계(master clock) 위계의 직접 앵커(anchor)입니다. 가장 느린 시계(phenobarbital)가 동역학(dynamics)을 지배합니다.

**5. Fluconazole–Midazolam / Diltiazem–Lovastatin:** oral vs IV 차이는 gut wall/first-pass contribution을 분리하는 실험적 단서입니다. C5에서 정량값을 다뤘으므로 여기서는 기전(mechanism) 어휘로만 회수합니다. [T17 pp.553–554]

<!-- SLIDE_START: S46 | title: C6 급성/만성 × 경구/정맥 매트릭스 | source_anchor: c6-acute-chronic-route-matrix -->

### 급성/만성 × 경구/정맥 진단 매트릭스

Rifampin 같은 가해 약물(perpetrator)은 급성 수송체 억제(acute transporter inhibition)와 만성 효소 유도(chronic enzyme induction)가 서로 반대 방향 효과(effect)를 만들 수 있습니다. 따라서 실무적으로는 acute IV, acute oral, chronic IV, chronic oral을 구분해 mechanism을 생각해야 합니다. 이는 교과서 사례에서 도출한 진단 프레임워크(diagnostic framework)입니다. [T17 pp.560–565]

| 조건 | 우세 기전 | 예 |
|---|---|---|
| 급성 정맥(Acute IV) | 수송체 억제(Transporter inhibition, 예: OATP1B1) | Atorvastatin–rifampin acute |
| 급성 경구(Acute oral) | 수송체 + 장벽/초회통과(gut/first-pass) | Rosuvastatin–cyclosporine |
| 만성 정맥(Chronic IV) | 효소 유도 개시(Enzyme induction onset) | Carbamazepine 자가유도 |
| 만성 경구(Chronic oral) | 효소 유도 × 초회통과 × 수송체 복합 | Long-term rifampin rifabutin |

<!-- SLIDE_START: S47 | title: C6 PD 상호작용 수식 골격 | source_anchor: c6-pd-interaction-equations -->

### PD 상호작용 층위 — 수식 골격

**수용체 수준 PD 상호작용(Receptor-level PD Interactions)** [G pp.224–227]:

- **다중 결합 부위 모델(Multiple Binding Sites, Eq.3:48)** [G p.224]: 한 리간드(ligand)가 여러 결합 부위(binding site)에 협동적으로(cooperative하게) 결합할 때의 반응(response) 곡선입니다. Hill 형태 적합(fitting)의 기전적 출처(mechanistic source)입니다.
- **경쟁적 길항(Competitive Antagonism, Eq.3:49)** [G p.225]:

$$E=\frac{E_{max}\cdot C}{C+EC_{50}\cdot(1+A/EA_{50})}$$

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{E}_{\text{효과}}
> =
> \frac{\overbrace{E_{max}}^{\text{Emax 보존}}\cdot\underbrace{C}_{\text{작용제 C}}}{
> \underbrace{C}_{\text{작용제 C}}+
> \underbrace{EC_{50}}_{\text{기본 EC50}}
> \cdot
> \overbrace{(1+A/EA_{50})}^{\text{경쟁 shift}}
> }
> $$

— 길항제 A가 들어오면 EC50이 $(1+A/EA_{50})$ factor만큼 **오른쪽으로 이동(shift)**하지만 $E_{max}$는 보존됩니다. 즉 더 높은 농도를 쓰면 같은 효과를 회복할 수 있습니다. 질량 작용 등가성(mass action equivalence)과 같은 분모 구조에 주목하세요.

- **비경쟁적 길항(Noncompetitive Antagonism, Eq.3:50)** [G pp.225–226]:

$$E=\frac{E_{max}}{(1+A/EA_{50})}\cdot\frac{C}{C+EC_{50}}$$

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{E}_{\text{효과}}
> =
> \frac{\overbrace{E_{max}}^{\text{기존 Emax}}}{\underbrace{(1+A/EA_{50})}_{\text{Emax 감소}}}
> \cdot
> \frac{\underbrace{C}_{\text{작용제 C}}}{\underbrace{C+EC_{50}}_{\text{작용제 potency}}}
> $$

— $E_{max}$가 $(1+A/EA_{50})$로 **감소**하고, EC50은 단순 비경쟁 모델에서 보존됩니다. 효현제(agonist) 농도를 무한정 올려도 원래 $E_{max}$는 회복되지 않습니다. 이것이 비경쟁적 길항의 임상적으로 다른 결과입니다.

- **경험적 두 약물 모델(Empirical Two-Drug Model, Eq.3:51, Table 3.2)** [G p.226]: 두 효과가 작용 부위(site)도 기전(mechanism)도 다를 때의 일반화된 합산/곱셈 framework입니다.
- **거울이성질체 상호작용(Enantiomer Interaction, Eq.3:52–3:53)** [G p.227]: 같은 receptor의 R/S 거울이성질체가 서로 다른 affinity를 가질 때입니다. ketamine R-/S- enantiomer 농도-효과 관계가 직접 예시(example)입니다.

**동일 수용체 완전 효현제 조합(Same-Receptor Full Agonist Combination)** [T17 pp.567–570]:

- **Emax 천장 효과(Emax Ceiling, Eq.17-19~17-21):** 두 완전 효현제(full agonist)가 같은 receptor에 작용하면 $E_{max}$는 단일 agonist 단독 사용 시와 같은 ceiling에 도달합니다. 즉 두 약물의 "더하기"가 effect를 두 배로 만들지는 않습니다.

$$E=\frac{E_{max}\cdot(C_A/EC_{50,A}+C_B/EC_{50,B})}{1+C_A/EC_{50,A}+C_B/EC_{50,B}}$$  

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{E}_{\text{공유수용체 효과}}
> =
> \frac{
> \overbrace{E_{max}}^{\text{공유 Emax}}\cdot
> \left(\underbrace{C_A/EC_{50,A}}_{\text{A drive}}+
> \underbrace{C_B/EC_{50,B}}_{\text{B drive}}\right)
> }{
> 1+\underbrace{C_A/EC_{50,A}}_{\text{A drive}}+
> \underbrace{C_B/EC_{50,B}}_{\text{B drive}}
> }
> $$
[T17 Eq.17-21; source tag: T17 p.568]

- **등효능선(Isobologram, Fig.17-21):** 일정 효과 수준(effect level, 예: 50% Emax)을 만드는 두 약물 농도 조합을 $(x,y)$ plane에 그렸을 때:
  - 직선 = 가산적(additive, 단순 mass action 합산)
  - 직선 아래로 휨 = 상승작용(synergy, 예: midazolam–propofol)
  - 직선 위로 휨 = less-than-additive (예: isoproterenol–propranolol antagonism)

- **Greco general response surface (Eq.17-22):** 두 약물의 임의 PD 상호작용(PD interaction)을 한 식으로 통합하는 advanced reference입니다. 본 session의 master card로 독립 확장하지 않고 reference로만 둡니다. [T17 p.569]

<!-- TRENCH -->
**실무 팁(Trench Tip):** DDI 사례(DDI case)를 검토할 때 "AUC가 증가했다"로 끝내지 말고, 함께 움직인 Cmax, t½, V/F, oral/IV ratio를 보세요. 예를 들어 AUC↑와 t½↓가 같이 나오면 단순 metabolic inhibition만으로 설명하기 어렵다. distribution/transporter mechanism을 의심해야 합니다. [T17 pp.563–565]

<!-- RECAP -->
**요약(Recap):** C6는 단일 기전 모델(mechanism model)의 과신을 막습니다. 같은 DDI pair라도 route, timing, chronicity에 따라 전혀 다른 mechanism signature가 나타납니다.

이 기전(mechanism)에서 30초 진단 질문 (§1.2 전 시그널의 통합): **AUC↑와 $t_{1/2}$↓가 같은 case에서 함께 보이는가, 또는 acute IV와 chronic oral 결과가 반대 방향인가?** 둘 중 하나라도 yes이면 단일 기전 모델(mechanism model)은 부적절합니다 — transporter / induction / PD interaction matrix를 모두 손에 쥐고 진단해야 합니다 (Atorvastatin-Rifampin acute IV signature가 anchor). [v3]

> **실무 체화 요약(Practice Brief) — [EXPERT_INFERENCE, v3]**  
> DDI 사례 검토에서 "AUC가 증가했다"로 결론을 내리기 전에 AUC, Cmax, $t_{1/2}$, V/F, oral/IV ratio를 모두 같은 표에 나란히 적으세요. AUC↑와 $t_{1/2}$↓가 함께 나오면 transporter signature입니다. 이는 metabolic inhibition signature가 아닙니다. Sponsor 미팅 전 acute/chronic × oral/IV 4-quadrant matrix를 명시적으로 채워두면 mechanism direction을 흔들리지 않게 방어할 수 있습니다 — 한 칸이라도 비어 있으면 그 칸이 곧 reviewer의 deficiency 항목이 됩니다.

---

> **실패 모드(Failure Mode) — [TEXTBOOK_DERIVED]**  
> 복합 DDI(multifaceted DDI)를 한 기전(mechanism)으로 축약하면 AUC, Cmax, t½가 서로 다른 방향으로 움직이는 signature를 놓칩니다. C6에서는 단일 지표가 아니라 지표들의 조합과 투여 timing을 함께 읽습니다.

<!-- SLIDE_START: S48 | title: C6 transporter signature Figure Pointer | source_anchor: figure-c6-transporter-signature -->

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer, p.565, Fig.17-19
Why this matters: 이 원본 도표는 텍스트만으로는 평평하게 처리되기 쉬운 시그니처를 보여 줍니다. 즉, AUC와 Cmax는 증가하면서 반감기는 감소할 수 있습니다. 이 그림이 없으면 해당 사례를 단순 대사 억제로 과도하게 해석하기 쉽습니다.
When to look: C6의 핵심 복합 기전 앵커를 읽은 뒤 확인하면 됩니다.
Learner instruction: AUC, Cmax, 반감기를 함께 확인하세요. 핵심은 단일 지표가 아니라 지표들의 결합 패턴입니다.
<!-- /FIGURE_POINTER -->

<!-- SECTION_CORE: SC-11 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** 혼동쌍은 관측값 하나를 mechanism 하나로 단정하는 습관을 끊는다 — $CL$, $F$, $C_u$, enzyme clock을 분리해라.

---
<!-- SLIDE_START: S49 | title: 혼동쌍 해부 | source_anchor: section-5-confusion-pairs -->

# §5. 혼동쌍 해부(Confusion Pair Dissection)

<!-- SLIDE_START: S50 | title: CP1 용량 의존적 capacity vs 진성 시간 의존성 | source_anchor: cp1-capacity-vs-time-dependence -->

## CP1. 용량 의존적 용량 한계(Dose-dependent capacity) vs 진성 시간 의존 동역학(true time-dependent kinetics)

<!-- CONFUSION -->
- **흔한 오해:** "CL이 시간에 따라 변했으니 time-dependent kinetics입니다."
- **교정:** MM kinetics에서는 concentration이 시간에 따라 떨어지므로 apparent CL도 함께 변합니다. 그러나 enzyme amount나 physiology가 실제로 변하지 않으면 true time-dependence가 아닙니다. [G p.112], [G pp.115–119]
- **검증:** 같은 concentration에서 시간이 달라도 CL이 달라지는가? 그렇다면 time-dependent mechanism을 의심합니다.

> **⚡ 기억 고리 (Memory Hook) — *농도 때문인가, 시간 때문인가*** [EXPERT_INFERENCE, v3]  
> MM 동역학에서는 농도가 시간에 따라 줄기 때문에 apparent CL도 변하지만, enzyme 자체는 변하지 않는다 — 이것은 **농도 구동 변화**다. True time-dependent kinetics는 **효소량이나 생리학 자체가 시간에 따라 변하는 것**입니다. 진단 기준: "같은 concentration에서 시간이 달라도 CL이 다른가?" — 그렇다면 time-dependent mechanism입니다.

<!-- SLIDE_START: S51 | title: CP2 자가유도 vs 일반 축적 | source_anchor: cp2-autoinduction-vs-accumulation -->

## CP2. 자가유도(autoinduction) vs 일반적 반복투여 축적(ordinary multiple-dose accumulation)

<!-- CONFUSION -->
- **흔한 오해:** 반복투여 중 trough가 변하면 accumulation 때문입니다.
- **교정:** accumulation은 linear parameter로도 예측 가능하지만, autoinduction은 enzyme turnover 때문에 trough envelope가 시간이 지나며 구조적으로 이동합니다. [G pp.126–129], [G pp.580–585]
- **검증:** single-dose fit이 multiple-dose trough를 systematic하게 벗어나면 $k_{out}$-linked enzyme compartment를 고려합니다.

> **⚡ 기억 고리 (Memory Hook) — *구조적 이동 vs 예측 가능한 누적*** [EXPERT_INFERENCE, v3]  
> 일반 축적(accumulation)은 linear 파라미터만으로 예측 가능한 **수위 상승**입니다. Autoinduction은 enzyme이 시간에 따라 새로 합성되어 처리 능력이 커지는 **배수구 자체가 넓어지는 과정**입니다. 따라서 autoinduction에서 trough는 단순 축적 예측보다 낮고, steady state까지의 시간도 enzyme turnover half-life에 묶입니다. single-dose fit으로 multiple-dose를 예측하면 trough가 systematic하게 과대추정됩니다.

> **🚨 치명적 타격 (Critical Blow) — [EXPERT_INFERENCE, v3]**  
> Autoinduction을 단순 accumulation으로 오해하여 carbamazepine 또는 phenobarbital의 multiple-dose PK를 single-dose fit으로 예측하면, enzyme induction이 완료되기 이전에 계산된 trough를 정상 농도로 해석하고 발작 예방이 불충분한 환자를 퇴원시키는 시나리오가 발생합니다. NONMEM에서는 OFV가 수렴해도 VPC의 trough systematic underprediction이 이 오류의 유일한 가시적 신호이며, single-dose data만으로는 enzyme compartment가 식별되지 않으므로 GOF plot이 평온해 보일 수 있습니다. → 이 confusion pair는 본 세션의 8개 쌍 중 임상 파급력이 가장 큰 단 1개로 식별됩니다.

<!-- SLIDE_START: S52 | title: CP3 capacity-limited elimination vs flow/first-pass | source_anchor: cp3-capacity-vs-flow-first-pass -->

## CP3. 용량 한계 제거(capacity-limited elimination) vs 혈류/초회통과 효과(flow/first-pass effect)

<!-- CONFUSION -->
- **흔한 오해:** AUC/Dose가 증가하면 무조건 hepatic enzyme saturation입니다.
- **교정:** AUC/Dose 증가는 CL 감소 또는 F 증가 모두에서 발생합니다. First-pass saturation, solubility limitation, flow effect도 같은 방향의 AUC pattern을 만들 수 있습니다. [G p.113], [T16 pp.496–500]
- **검증:** IV/oral crossover 또는 bioavailability 변화 근거(evidence)를 확인합니다.

> **⚡ 기억 고리 (Memory Hook) — *공장 한계 vs 도로 한계*** [EXPERT_INFERENCE, v3]  
> Capacity-limited elimination은 **공장(효소)의 최대 처리 능력**이 한계다 — 원료(약물)가 아무리 많아도 기계(효소)가 처리할 수 있는 최대치를 넘을 수 없습니다. Flow/first-pass effect는 **도로(혈류)의 용량**이 한계다 — 공장이 아무리 빨라도 원료가 도착하는 속도 이상으로 처리할 수 없습니다. 둘 다 AUC/Dose를 증가시키지만 방향이 다르다: 공장 한계는 고용량에서 폭발적 비선형성, 도로 한계는 고혈류 상황에서 선형 변화.

<!-- SLIDE_START: S53 | title: CP4 열린 생체 결합 vs 닫힌 시험관 결합 | source_anchor: cp4-open-vs-closed-binding -->

## CP4. 열린 생체 내 결합(open in vivo binding) vs 닫힌 시험관 내 결합(closed in vitro binding)

<!-- CONFUSION -->
- **흔한 오해:** displacement가 있으면 unbound concentration이 지속적으로 오릅니다.
- **교정:** open system에서는 input과 unbound clearance가 unbound steady state를 결정합니다. total concentration 변화만으로 dose adjustment를 결정하지 않는다. [G pp.129–134], [T17 pp.538–544]
- **검증:** total과 unbound concentration을 같이 보고, low/high extraction context를 분리합니다.

> **⚡ 기억 고리 (Memory Hook) — *열린 계 vs 닫힌 계*** [EXPERT_INFERENCE, v3]  
> In vitro에서는 총 약물량이 고정된 **닫힌 계**이므로 displacement가 생기면 unbound가 지속적으로 높아진다. In vivo에서는 신장·간이 계속 unbound drug를 제거하는 **열린 계**이므로, displacement 후 새 평형에서 unbound concentration은 제거 속도에 따라 결정됩니다. In vitro 실험에서 "강한 displacement"라도 in vivo에서 unbound concentration 변화가 임상적으로 의미 없을 수 있는 이유가 여기서 나온다.

<!-- SECTION_CORE: SC-12 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** 억제·유도·PD interaction의 표면 신호는 비슷해도 복구 시계와 반응 축이 다르다 — reversible, MBI, induction, EC50/Emax를 따로 판독해라.

---
<!-- SLIDE_START: S54 | title: CP5 치환 단독 DDI vs 억제 DDI | source_anchor: cp5-displacement-vs-inhibition -->

## CP5. 치환 단독 DDI(displacement-only DDI) vs 억제 DDI(inhibition DDI)

<!-- CONFUSION -->
- **흔한 오해:** phenytoin total concentration이 내려가면 efficacy가 낮아졌습니다.
- **교정:** valproate displacement example에서는 total phenytoin이 낮아져도 unbound concentration은 유지될 수 있습니다. 반대로 warfarin–phenylbutazone은 displacement와 inhibition이 겹쳐 단순 displacement로 설명하면 안 됩니다. [T17 p.543], [T17 p.563]
- **검증:** unbound concentration과 clearance/time-course를 함께 확인합니다.

> **⚡ 기억 고리 (Memory Hook) — *자리 뺏기 vs 공장 멈추기*** [EXPERT_INFERENCE, v3]  
> Displacement는 결합 자리를 빼앗아 unbound concentration을 일시적으로 올리지만, open system에서 새 정상상태로 빠르게 재수렴된다 — "자리 뺏기"는 일시적 효과. Inhibition DDI는 $CL_{int}$를 직접 줄여 약물 처리 공장 자체를 느리게 하므로 AUC가 지속적으로 증가합니다. 두 메커니즘이 겹치면(warfarin-phenylbutazone) displacement 단독보다 훨씬 큰 AUC 증가가 나타나므로 반드시 분리해서 평가해야 합니다.

<!-- SLIDE_START: S55 | title: CP6 가역적 억제 vs MBI | source_anchor: cp6-reversible-vs-mbi -->

## CP6. 가역적 억제(reversible inhibition) vs MBI

<!-- CONFUSION -->
- **흔한 오해:** inhibitor를 중단하면 interaction은 inhibitor half-life만큼 사라집니다.
- **교정:** reversible inhibition은 inhibitor concentration이 줄면 빠르게 회복될 수 있지만, MBI는 enzyme pool recovery가 필요합니다. Clarithromycin-like MBI는 회복 시간이 enzyme resynthesis에 묶인다 (CYP3A4의 경우 ~2주). [T17 pp.557–558]
- **검증:** single-dose vs multiple-dose perpetrator exposure에서 affected drug PK 변화가 질적으로 달라지는지 봅니다. $k_{inact}/k_E$ ratio가 클수록 reversible 식과 결과가 크게 다릅니다.

> **⚡ 기억 고리 (Memory Hook) — *문 막기 vs 자물쇠 교체*** [EXPERT_INFERENCE, v3]  
> Reversible inhibition은 **문을 막고 있는 것** — inhibitor가 사라지면 문이 다시 열린다. MBI는 **자물쇠 자체를 망가뜨린 것** — inhibitor가 없어져도 새 자물쇠(효소)가 합성되어야 회복됩니다. 이 때문에 MBI 약물을 중단해도 interaction이 enzyme resynthesis 기간(CYP3A4 $\approx 2$주) 동안 지속됩니다. Washout period 설계에서 이 차이를 놓치면 carry-over interaction이 임상 시험 데이터를 오염시킨다.

<!-- SLIDE_START: S56 | title: CP7 억제 vs 유도와 rifampin 전환 | source_anchor: cp7-inhibition-vs-induction -->

## CP7. 억제(inhibition) vs 유도(induction), 그리고 rifampin 급성/만성 전환(acute vs chronic switch)

<!-- CONFUSION -->
- **흔한 오해:** rifampin은 inducer이므로 substrate exposure를 낮춥니다.
- **교정:** chronic rifampin induction은 exposure를 낮출 수 있지만, acute rifampin은 transporter inhibition으로 exposure를 올릴 수 있다 (Atorvastatin-Rifampin acute IV에서 Cmax 10×, AUC 7×). Timing과 route를 분리해야 합니다. [T17 pp.560–565]
- **검증:** acute/chronic × oral/IV matrix로 예상 방향을 따로 적습니다.

> **⚡ 기억 고리 (Memory Hook) — *방향 전환 스위치*** [EXPERT_INFERENCE, v3]  
> Rifampin은 만성 투여 시 **유도자(inducer)** — CYP3A4와 P-gp를 증가시켜 substrate exposure를 낮춥니다. 하지만 급성 IV 투여 시 **OATP 억제자** — hepatic uptake를 막아 일부 substrate(atorvastatin)의 Cmax를 10배, AUC를 7배 올립니다. 같은 약이 투여 경로와 시간에 따라 상반된 방향으로 interaction을 일으키는 사례다. Timing × Route × Mechanism의 3차원 매트릭스 없이는 방향 예측이 불가능하다.

<!-- SLIDE_START: S57 | title: CP8 PK DDI vs PD DDI | source_anchor: cp8-pk-vs-pd-ddi -->

## CP8. PK DDI vs PD DDI

<!-- CONFUSION -->
- **흔한 오해:** response가 변하면 concentration이 변했을 것입니다.
- **교정:** PD interaction은 concentration-time profile이 크게 변하지 않아도 response가 additive, synergistic, antagonistic하게 변할 수 있습니다. 경쟁적 길항(Eq.3:49)은 EC50을 $(1+A/EA_{50})$로 shift하고, 비경쟁적 길항(Eq.3:50)은 Emax를 $(1+A/EA_{50})^{-1}$로 감소시키며, 같은 receptor의 두 full agonist는 Emax ceiling을 공유합니다. [G pp.224–227], [T17 pp.567–570]
- **검증:** unbound concentration-response relationship을 같이 확인하고, 같은 효과 level을 isobologram에 표시해 additivity 가정을 점검합니다.

> **⚡ 기억 고리 (Memory Hook) — *농도 바꾸기 vs 반응 바꾸기*** [EXPERT_INFERENCE, v3]  
> PK DDI는 농도-시간 프로파일 자체를 변화시켜 response가 달라지는 것(약이 더 많이 쌓이거나 덜 쌓임). PD DDI는 같은 농도에서 효과 크기가 달라지는 것(receptor, 효소, 생리학적 경로의 상호작용). 구분 기준: unbound concentration이 변하지 않는데 response가 달라지면 PD interaction을 의심합니다. Isobologram이 분리의 실험 도구다.

<!-- RECAP -->
**요약(Recap):** 혼동쌍(confusion pair)의 공통 원인은 "관측값 하나로 mechanism 하나를 단정하는 습관"입니다. total concentration, AUC, t½, route, timing, response를 함께 읽어야 합니다.

---

<!-- SECTION_CORE: SC-13 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** 자기테스트 전반부는 $AUC/Dose$, $K_m+C$, $R_0\to V_m$, saturable reabsorption을 실제 triage 순서로 회상하게 만든다.

---
<!-- SLIDE_START: S58 | title: 자기 테스트 능동 회상 모듈 | source_anchor: section-7-self-test -->

# §7. 자기 테스트: 능동 회상 모듈(Self-Test: Active Recall Module)

<!-- SLIDE_START: S59 | title: Q1 회상 | source_anchor: q1-recall -->

## Q1. [회상(Recall)]
<!-- SELF-TEST -->
비선형성 진단에서 dose-normalized concentration-time plot과 AUC/Dose vs Dose plot을 먼저 그리는 이유는 무엇인가?  
**정답:** 선형이면 dose-normalized 관측값이 superimpose됩니다. 겹치지 않으면 CL, F, V/distribution, binding, time-dependent process 중 하나가 dose/time의 함수라는 신호다. 즉, 이 그림은 "어떤 파라미터(parameter)가 상수가 아니게 되었는가?"를 묻는 첫 필터다. [G pp.112–114], [T16 p.492]

<!-- SLIDE_START: S60 | title: Q2 적용 | source_anchor: q2-application -->

## Q2. [적용(Application)]
<!-- SELF-TEST -->
AUC/Dose가 dose와 함께 증가합니다. 가능한 두 가지 mechanism은?  
**정답:** clearance 감소 또는 bioavailability 증가. capacity-limited elimination뿐 아니라 first-pass saturation도 가능하므로 IV/oral 근거(evidence)가 필요합니다. [G p.113], [T16 pp.499–506]

<!-- SLIDE_START: S61 | title: Q3 회상 | source_anchor: q3-recall -->

## Q3. [회상(Recall)]
<!-- SELF-TEST -->
왜 Eq.2:264를 MM ODE citation으로 쓰면 안 되는가?  
**정답:** Eq.2:264는 linear superposition 식입니다. MM clearance/rate/bolus/infusion/input 식은 Eq.2:266–2:274 영역에 있습니다. [G pp.114–118]

<!-- SLIDE_START: S62 | title: Q4 적용 | source_anchor: q4-application -->

## Q4. [적용(Application)]
<!-- SELF-TEST -->
Phenytoin 300 mg/day에서 4 mg/L, 500 mg/day에서 36 mg/L가 된 이유를 Eq.16-7의 denominator 관점에서 설명하세요.  
**정답:** $C_{u,ss}=K_mR_0/(V_m-R_0)$에서 dosing rate $R_0$가 $V_m\approx 500$ mg/day에 가까워질수록 denominator가 작아져 concentration이 비선형적으로 증가합니다. typical $K_m\approx 0.4$ mg/L (unbound 기준), $f_u\approx 0.1$이므로 total $K_m'\approx 4$ mg/L; 치료역 10–20 mg/L는 이미 capacity 근처다. [T16 pp.491, 503]

<!-- SLIDE_START: S63 | title: Q5 적용 | source_anchor: q5-application -->

## Q5. [적용(Application)]
<!-- SELF-TEST -->
Ascorbic acid는 133-fold dose increase에도 concentration이 약 2-fold만 증가했습니다. phenytoin과 반대 방향의 비선형성이 생긴 이유는?  
**정답:** 농도 상승과 함께 renal clearance가 saturable reabsorption escape valve로 인해 증가하기 때문입니다 (CLR < 0.5 mL/min @ 9 mg/L → 21 mL/min @ 19 mg/L, >42-fold 증가). saturable reabsorption은 high-concentration에서 약물 제거를 가속하는 역방향 비선형성을 만듭니다. [T16 p.492], [T16 pp.507–510]

<!-- SECTION_CORE: SC-14 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** $V_{max}$–$K_m$ 식별성, enzyme turnover, $C_u$, $f_m$, route effect를 계산 직관으로 연결해야 답이 흔들리지 않는다.

---
<!-- SLIDE_START: S64 | title: Q6 회상 | source_anchor: q6-recall -->

## Q6. [회상(Recall)]
<!-- SELF-TEST -->
MM model에서 $V_{max}$와 $K_m$를 따로 추정하려면 어떤 concentration range가 필요한가? "Vmax–Km Ridge Lock"이란 무엇인가?  
**정답:** curvature를 포함하고, 특히 $K_m$ 주변 또는 그 이하의 concentration이 필요합니다. high concentration plateau만으로는 $V_{max}/K_m$ ridge가 생긴다 — single-dose data에서 흔히 $\rho(V_{max}, K_m) > 0.9$ (Gabrielsson p.116에서 $-0.96$ 사례). 이를 "Vmax–Km Ridge Lock"이라 부른다. rescue: 용량 수준(dose level) 추가 또는 $K_m$ prior fix. [G p.116, p.117]

<!-- SLIDE_START: S65 | title: Q7 적용 | source_anchor: q7-application -->

## Q7. [적용(Application)]
<!-- SELF-TEST -->
반복투여 중 trough가 계속 낮아지고 single-dose model은 잘 맞습니다. 어떤 mechanism을 먼저 의심해야 하는가? 이를 명명한 진단 시그너처로 부른다면?  
**정답:** autoinduction 또는 time-dependent increase in clearance — "Trough Envelope Drift" + "Single-dose Fit Trap"의 결합. enzyme turnover compartment와 $k_{out}$ 식별 가능성을 확인합니다. PK22 design에서 $k_{out}\approx 0.023$ h⁻¹, 즉 enzyme $t_{1/2}\approx 30$ h가 식별됩니다. [G pp.126–129], [G pp.580–585]

<!-- SLIDE_START: S66 | title: Q8 적용 | source_anchor: q8-application -->

## Q8. [적용(Application)]
<!-- SELF-TEST -->
Clarithromycin 병용 후 midazolam exposure가 multiple dosing에서 더 커지고 회복도 느립니다. reversible inhibition과 어떻게 정량적으로 다른가?  
**정답:** mechanism-based inhibition은 enzyme activity를 제거하므로, 회복은 inhibitor 농도 소실뿐 아니라 enzyme resynthesis/degradation clock에 묶입니다. clarithromycin 정량값으로: $k_{inact}\approx 0.07$ min⁻¹, $k_E\approx 0.23$ day⁻¹, $k_{inact}/k_E\approx 438$, $C_{u,I}/K_I\approx 0.025$ → 같은 inhibitor exposure로 reversible 식은 1.025-fold CL 감소를 예측하지만 MBI 식은 **약 11-fold** CL 감소를 예측합니다. CYP3A4 회복은 ~2주 필요. [T17 pp.557–558]

<!-- SLIDE_START: S67 | title: Q9 적용 | source_anchor: q9-application -->

## Q9. [적용(Application)]
<!-- SELF-TEST -->
Valproate 병용 후 total phenytoin은 낮아졌지만 unbound phenytoin은 유지됩니다. 용량(dose)을 줄여야 하는가?  
**정답:** displacement-only에서는 total concentration이 misleading할 수 있습니다. unbound concentration과 clinical response를 기준으로 판단해야 하며, total 감소만으로 dose 감량하면 안 됩니다. open in vivo system mass balance ($C_u = K^0/CL_u$)에서는 unbound clearance가 변하지 않는 한 unbound steady state가 유지되기 때문입니다. [T17 p.543], [G §2.7.5]

<!-- SLIDE_START: S68 | title: Q10 계산 직관 | source_anchor: q10-computational-intuition -->

## Q10. [계산 직관(Computational Intuition)]
<!-- SELF-TEST -->
Affected drug의 $f_m$가 0.8이고 inhibitor가 해당 pathway를 강하게 억제합니다. 왜 $f_m$가 0.3인 drug보다 AUC ratio가 훨씬 커지는가?  
**정답:** Eq.17-11에서 inhibited pathway term $f_m/(1+C_{u,I}/K_I)$가 작아져도 residual $(1-f_m)$가 exposure ratio의 바닥을 정합니다. $f_m=0.8$이면 남은 pathway가 0.2뿐이라 ratio가 크게 뛴다. 반대로 $f_m=0.3$이면 0.7의 우회 경로가 있어 ratio 상승이 제한됩니다. [T17 pp.550–552]

<!-- SLIDE_START: S69 | title: Q11 적용 | source_anchor: q11-application -->

## Q11. [적용(Application)]
<!-- SELF-TEST -->
Oral midazolam interaction이 IV midazolam interaction보다 크다. 어떤 mechanism을 시사하는가? Fluconazole–midazolam 정량 anchor를 인용하세요.  
**정답:** gut wall/first-pass metabolism component가 크다는 뜻입니다. fluconazole 400 mg 병용 시 oral midazolam AUC는 5.6× 증가, IV는 2× 증가; F 24%→63%; $F_H$ 0.42→0.72; $F_G$ 0.57→0.88로 $F_G$가 더 큰 비율로 변한다 → midazolam의 oral first-pass에 gut wall 기여가 상당함을 의미. [T17 pp.553–554, Fig.17-10]

<!-- SECTION_CORE: SC-15 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** PM, rifampin, PD interaction, parent–metabolite, MBI, 보스 딜레마는 모두 $f_m$, route, timing, recovery clock을 순서대로 묻는다.

---
<!-- SLIDE_START: S70 | title: Q12 회상 | source_anchor: q12-recall -->

## Q12. [회상(Recall)]
<!-- SELF-TEST -->
Eq.17-18의 PM × inhibitor risk가 큰 이유는?  
**정답:** polymorphic pathway가 이미 결손된 PM에서 남은 nonpolymorphic pathway가 inhibitor에 의해 막히면 residual clearance가 매우 작아질 수 있기 때문입니다. $\text{Maximum exposure ratio}=1/(1-f_m^{POLY}-f_m^{NP})$이므로 두 항의 합이 1에 가까울수록 ratio가 발산. [T17 pp.558–559]

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{\text{Maximum exposure ratio}}_{\text{PM+억제 위험}}
> =
> \frac{1}{\underbrace{1-f_m^{POLY}-f_m^{NP}}_{\text{남은 CL 여유}}}
> $$

<!-- SLIDE_START: S71 | title: Q13 적용 | source_anchor: q13-application -->

## Q13. [적용(Application)]
<!-- SELF-TEST -->
Rifampin 병용에서 acute IV study는 AUC 증가, chronic oral 병용은 AUC 감소를 보일 수 있습니다. 왜 모순이 아닌가?  
**정답:** acute rifampin은 OATP1B1 같은 transporter inhibition으로 hepatic uptake를 차단해 혈중 누적; chronic rifampin은 enzyme induction으로 CL을 올려 노출을 감소. timing과 route가 mechanism을 바꿉니다. Atorvastatin-rifampin acute IV: Cmax 10×, AUC 7×, $t_{1/2}$ 8→3h가 직접 anchor (transporter signature: AUC↑ + $t_{1/2}$↓). [T17 pp.560–565, Fig.17-19]

<!-- SLIDE_START: S72 | title: Q14 적용 | source_anchor: q14-application -->

## Q14. [적용(Application)]
<!-- SELF-TEST -->
Response는 크게 변했지만 unbound concentration-time profile은 거의 변하지 않았습니다. 무엇을 의심해야 하는가? 경쟁적 길항과 비경쟁적 길항을 수식 한 줄로 구분하세요.  
**정답:** PK DDI보다 PD interaction을 의심합니다. 경쟁적 길항(Eq.3:49)은 $E=E_{max}\cdot C/[C+EC_{50}\cdot(1+A/EA_{50})]$ — EC50을 shift하지만 Emax는 보존됩니다. 비경쟁적 길항(Eq.3:50)은 $E=E_{max}/(1+A/EA_{50})\cdot C/(C+EC_{50})$ — Emax를 감소시킵니다. 같은 receptor 두 full agonist는 Eq.17-21로 Emax ceiling 공유. [G pp.225–226], [T17 pp.567–570]

> **Annotated equation — 수식 해부**
>
> $$
> \overbrace{E=\frac{E_{max}\cdot C}{C+EC_{50}\cdot(1+A/EA_{50})}}^{\text{경쟁: EC50↑}}
> \qquad\text{vs}\qquad
> \overbrace{E=\frac{E_{max}}{1+A/EA_{50}}\cdot\frac{C}{C+EC_{50}}}^{\text{비경쟁: Emax↓}}
> $$

<!-- SLIDE_START: S73 | title: Q15 회상 | source_anchor: q15-recall -->

## Q15. [회상(Recall)]
<!-- SELF-TEST -->
Drug–metabolite nonlinear model (G §2.7.6)에서 active metabolite의 disposition을 parent–metabolite 동시 관측 데이터만으로 inferential extrapolation하면 안 되는 이유는? Source-backed 경고 한 줄과 임상 implication을 답하세요.  
**정답:** Gabrielsson p.137 명시: "metabolite 단독 투여 데이터 없이는 metabolite의 disposition kinetics에 대한 추가 extrapolation은 안 됩니다." parent와 metabolite가 같은 MM enzyme을 공유하면 metabolite의 prolonged tail이 자체 distribution kinetics 때문인지 parent의 saturable elimination이 metabolite 형성 속도를 제한하기 때문인지 식별되지 않는다. → 임상적으로 active metabolite의 toxicity/efficacy 기여가 큰 약물(carbamazepine-10,11-epoxide, codeine-morphine 영역)에서는 metabolite 단독 투여 disposition study가 식별성 보강 단계로 필요할 수 있습니다. [G pp.135–139]

<!-- SLIDE_START: S74 | title: Q16 회상 | source_anchor: q16-recall -->

## Q16. [회상(Recall)]
<!-- SELF-TEST -->
R&T Table 17-5의 inhibitor strength 분류 기준을 답하세요. Strong/Moderate/Weak는 substrate AUC 변화로 어떻게 구분되는가? MBI는 별도 표시 이유는?  
**정답:** Strong = ≥5-fold AUC increase 또는 >80% CL 감소; Moderate = 2- to 5-fold AUC; Weak = 1.25- to 2-fold AUC. MBI inhibitor는 Reversible 식만으로 분류하면 강도를 과소평가하므로 별도 표시(MBI marker) — 같은 $C_{u,I}/K_I$에서도 reversible 1.025× vs MBI 11× CL 감소처럼 결과가 자릿수 단위로 다르기 때문. 이 분류는 textbook reference이며 다른 규제문서의 분류 체계와 직접 동일시하지 않습니다. [T17 p.549]

<!-- SLIDE_START: S75 | title: Q17 보스 딜레마 | source_anchor: q17-boss-dilemma -->

## Q17. [보스 딜레마(Boss Dilemma)]
<!-- SELF-TEST -->
Sponsor가 "inhibitor 병용 시 AUC가 증가하니 label에 일괄 dose reduction을 쓰자"고 합니다. 10분 안에 mechanism-based 검토 순서를 말하세요.  
**정답:** (1) affected drug의 $f_m$와 inhibited pathway 확인 — $f_m$가 작으면 강한 inhibitor라도 whole-body AUC ratio는 제한된다 (Eq.17-11); (2) $C_{u,I}/K_I$와 reversible vs MBI 구분 — MBI라면 $k_{inact}/k_E$ 평가 + enzyme recovery clock 고려; (3) oral/IV route effect 확인 — Diltiazem-Lovastatin 1.27 vs 3.57 (Table 17-7) 패턴이면 gut wall first-pass component 우세; (4) PM 또는 residual pathway risk 확인 — Eq.17-18 분모 발산 위험; (5) acute/chronic perpetrator effect와 withdrawal sequence 확인 — phenobarbital-dicumarol 3-4주 plateau onset, MBI 2주 recovery washout trap; (6) transporter/multifaceted signature 확인 — AUC↑+$t_{1/2}$↓ 패턴이면 metabolic inhibition이 아닌 transporter; (7) Mass action equivalence triangle 점검 — Eq.2:266 ↔ Eq.16-7 ↔ Eq.17-11이 같은 mechanism의 다른 표현임을 sponsor에게 명확히 전달. 단, 여기서는 textbook-based mechanism checklist로만 둡니다. [T17 pp.546–565], [G pp.115–118]

<!-- RECAP -->
**요약(Recap):** Self-test는 식 암기가 아니라 mechanism triage를 묻습니다. 각 답은 "어떤 파라미터(parameter)가 상수가 아니게 되었는가?"로 되돌아가야 합니다.

---

<!-- SECTION_CORE: SC-16 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** 마지막에는 모든 세부식을 mass action denominator와 mechanism triage로 회수해라 — 그래야 PopPK, TDM, DDI, PD 모델링이 같은 언어를 쓴다.

---
<!-- SLIDE_START: S76 | title: 메타프레임 및 전체 조망 | source_anchor: section-8-meta-frame -->

# §8. 메타프레임 및 전체 조망(Meta-Frame & Big Picture)

<!-- SLIDE_START: S77 | title: 한 페이지 기억 모델 | source_anchor: section-8-1-one-page-memory -->

## 8.1 한 페이지 기억 모델(One-Page Memory Model)

<!-- MASTER LENS -->
Session 08의 기억 모델은 다음 일곱 문장으로 고정합니다. 이 일곱 문장은 세부식을 외우기 전, mechanism triage 순서를 유지하기 위한 압축본입니다.

1. **비선형성은 중첩 원리 실패(superposition failure)로 발견합니다.** [G pp.112–114], [T16 p.492]
2. **용량 한계(capacity limitation)는 $CL(C)$를 만들고, $R_0\to V_m$에서 정상상태가 발산합니다.** [G pp.115–119], [T16 pp.500–506]

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{CL(C)}_{\text{농도의존 CL}}
> \qquad;
> \qquad
> \underbrace{R_0\to V_m}_{\text{R0→Vm}}
> \Rightarrow
> \underbrace{C_{ss}\uparrow\uparrow}_{\text{Css 급상승}}
> $$
3. **시간 의존성(time-dependence)은 효소/수송체/생리학의 시계가 약물 농도 시계와 분리될 때 생긴다; 주 시계(master clock) = $\max(t_{1/2}^{enzyme}, t_{1/2}^{inducer}, t_{1/2}^{drug})$.** [G pp.119–129], [T16 pp.516–519], [T17 pp.560–561]
4. **결합(binding)은 총 농도를 속이고, 열린 계(open system)에서는 $C_u=K^0/CL_u$ 물질 수지(mass balance)가 비결합 노출을 강제합니다.** [G pp.129–134], [T17 pp.538–544]

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{C_u}_{\text{자유 노출}}
> =
> \frac{\underbrace{K^0}_{\text{입력}}}{\underbrace{CL_u}_{\text{자유 CL}}}
> $$
5. **DDI 예측은 $f_m$, 억제제 강도(inhibitor strength, $C_{u,I}/K_I$, $k_{inact}/k_E$), 투여 경로, PM/잔여 경로, 유도/MBI 회복을 함께 봅니다.** [T17 pp.546–561]

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{f_m}_{\text{경로몫}}
> \quad;
> \quad
> \underbrace{C_{u,I}/K_I}_{\text{가역 억제}}
> \quad;
> \quad
> \underbrace{k_{inact}/k_E}_{\text{MBI/회복}}
> $$
6. **복합 DDI와 PD 상호작용은 "AUC 하나"로 기전을 단정하지 못하게 만듭니다 — Cmax, $t_{1/2}$, V/F, 경구/정맥 비율, 등효능선(isobologram)을 함께 봅니다.** [T17 pp.563–570]
7. **질량 작용 등가 삼각형(Mass Action Equivalence Triangle):** 비선형 PK·TDM·DDI 직관은 같은 분모 구조의 다른 표현이다 → **§2 C5 mass action equivalence triangle 참조**. 상세 식 비교와 도출은 §2 C5 ANNOTATION에서 확인하세요. [G p.115], [T16 p.503], [T17 p.550]

<!-- SLIDE_START: S78 | title: 후속 계량약리학 작업의 의존성 | source_anchor: section-8-2-downstream-dependencies -->

## 8.2 후속 계량약리학 작업의 의존성

- **PopPK 모델 구축:** 비선형 CL, 시간 변동 CL, 결합 비선형성, 수송체 DDI를 구분하지 못하면 파라미터 변동성이 기전 오류를 가립니다.
- **TDM:** phenytoin형 용량 한계(capacity limitation)에서는 작은 용량 변화가 큰 농도 변화를 만들고 (Vm 20%↓ → Css 2× 변화), 총 농도만의 모니터링(total-only monitoring)은 치환/결합(displacement/binding) 상황에서 오해를 유발합니다. 정상상태(plateau) 도달 시간이 용량 한계에 근접할수록 발산한다는 점 역시 모니터링 간격 결정과 직결됩니다. [T16 pp.491–506], [T17 p.543]
- **DDI 연구 해석:** 가역적 억제(reversible inhibition), MBI ($k_{inact}/k_E$), 유도(induction, 주 시계 위계), 수송체 효과(급성 vs 만성), 투여 경로 효과를 분리하지 못하면 약물 시작/중단 권고가 잘못됩니다. [T17 pp.546–565]
- **약물-대사체 모델링:** 모약물-대사체(parent-metabolite) 동시 관측만으로 대사체 분포(metabolite disposition)가 충분히 식별된다고 가정하지 않습니다. 대사체 단독 분포 연구(disposition study)가 식별가능성(identifiability) 보강의 표준 단계입니다. 이 항목은 출처 기반 식별가능성 주의사항으로만 유지합니다. [G pp.135–139]
- **PD 상호작용 모델링:** 경쟁적(Eq.3:49 EC50 이동), 비경쟁적(Eq.3:50 Emax 감소), 동일 수용체 완전 효현제 조합(Eq.17-21 천장), 등효능선(isobologram)의 가산성 가정 점검 — PK 변화 없이 반응이 변하는 경우 PD 상호작용이 1차 후보. [G pp.224–227], [T17 pp.567–570]

<!-- RECAP -->
**최종 요약(Final Recap):** 이 장의 최종 골격(spine)은 "diagnose nonlinearity → identify capacity/time/binding mechanism → translate to DDI prediction → avoid route/timing/unbound/PM traps → return to mass action equivalence triangle"입니다. 이 spine을 PhD 1년차가 확실히 체화하면, 비선형 PK와 DDI chapter의 대부분은 암기가 아니라 mechanism triage로 회수됩니다. 정량 anchor는 수식 spine을 임상 정량값으로 채워 "수식을 외운 것"이 아니라 "수식을 임상 case에 즉시 매핑할 수 있는 것"으로 학습 목표를 끌어올립니다.


## PART B — Compiler-Only Appendix

This appendix is not learner-facing. It exists only to protect Phase 5 rendering fidelity.

### B1. Compilation Contract

- PART A is the only learner-facing body.
- Phase 5 must render PART A without altering content.
- PART B is instruction/guardrail only and must not be rendered as learner content unless explicitly requested.
- Do not restore deprecated material, add new scientific content, add new page tags, or modify equations/source tags.
- Do not generate HTML in Phase 4D; Phase 5 alone generates the single self-contained HTML.

### B2. Figure Rendering Instructions

- Preserve approved Figure Strategy decisions from `08_Content Lock v2.1.md`.
- Approved KEEP markers in PART A: #1, #2, #4, #6, #8, #10, #12.
- Rejected figures are not restored.
- Image rights = None. Do not embed copyrighted textbook images.
- Render `FIGURE_POINTER` as a text-only textbook-reference callout showing Source, Why this matters, When to look, and Learner instruction.
- Render `FIGURE_SCHEMATIC` as a newly designed schematic based only on the marker brief. Do not reproduce textbook layout, palette, or label placement.
- Do not propose or add new figures in Phase 5.

### B3. Page Tag Rendering Rules

- Preserve all existing source tags and page tags, including `[p.XX]`, `[pp.XX–YY]`, `[pp.XX, YY]`, and `[p.확인 필요]` if present.
- Render visible source page tags in HTML using `<span class="source-page">...</span>`.
- Render `[p.확인 필요]` as `<span class="source-page source-uncertain">[p.확인 필요]</span>`.
- Do not fabricate, delete, renumber, or relocate page tags.
- Do not apply page-tag regex inside code blocks or inside `FIGURE_*` marker blocks.
- Source page tags must remain visible in print mode.

### B4. HTML Compiler Requirements

- Render content; do not alter it.
- Output one self-contained HTML file with inline custom CSS and JS.
- Permitted external runtime dependencies only: MathJax CDN, Mermaid CDN, and permitted CDN libraries such as highlight.js.
- MathJax: support inline `\(...\)` and display `\[...\]` math while preserving existing dollar-delimited equations if the compiler normalizes them safely.
- Code blocks: dark `<pre><code>` style with copy buttons.
- Self-test blocks: render `<!-- SELF-TEST -->` as click-to-reveal accordions; answers hidden by default.
- Controls: print/PDF button via `window.print()` and checklist/session state persistence if checklists are rendered.
- Responsive: mobile single-column/collapsed navigation; desktop two-column with sticky left sidebar.
- Dark/light: respect `prefers-color-scheme`.
- Print: hide navigation, avoid broken cards, and keep source page tags visible.

#### Marker-to-component mapping

| Marker / Pattern | HTML Component | Rendering rule |
|---|---|---|
| `<!-- MASTER LENS -->` | Callout box | border-left gold; subtle background |
| `<!-- ANNOTATION -->` | Annotation/tooltip-style note | muted italic style |
| `<!-- ANCHOR -->` | Bridge sentence | muted italic style |
| `<!-- TRENCH -->` | Practical tip box | rose-accented practical callout |
| `<!-- CONFUSION -->` | Confusion comparison | amber comparison box |
| `<!-- SELF-TEST -->` | Accordion | question visible, answer hidden until click |
| `<!-- RECAP -->` | Section recap | blue-accented summary box |
| `<!-- FIGURE_POINTER -->` | Textbook pointer callout | text-only; no image embedding |
| `<!-- FIGURE_SCHEMATIC -->` | Schematic figure | Mermaid/inline SVG/CSS only as appropriate |
| `[확인 필요]` | Highlight flag | visible mark/highlight |

#### Navigation anchor integrity rules

- HTML must include a sticky left sidebar table of contents.
- Use `<a href="#...">` links only.
- Every sidebar target must have exactly one matching body id.
- Every major section heading (§1, §2, §5, §7, §8) must receive a stable id.
- Every §2 concept card heading must receive a stable id.
- Every named diagnostic block ("Vmax–Km Ridge Lock", "Trough Envelope Drift", "Single-dose Fit Trap", "Washout Trap") and the §1.2 거장 시그널 subsection must receive stable ids for cross-link from §7 self-test.
- Do not create duplicate ids or TOC links whose target id does not exist.
- Enable smooth scrolling with `html { scroll-behavior: smooth; }`.
- Before finalizing HTML, count all sidebar `href="#id"` values, confirm each id exists exactly once, and fix any mismatch.

#### Mermaid/schematic self-check

- Mermaid blocks must start with a valid directive such as `flowchart TD`, `flowchart LR`, `graph TD`, or `graph LR`.
- Node IDs must use only `[A-Za-z0-9_]`.
- Labels with Korean text, parentheses, slashes, symbols, or spaces must be quoted.
- Edge labels with special characters must use quoted edge-label syntax.
- If Mermaid cannot be made robust, use inline SVG or CSS cards.
- Do not emit a Mermaid block likely to fail rendering.

### B5. Audit Guardrails

Regression-prevention items:

- Do not restore the unsupported direct claim that textbook Eq.17-11/Eq.17-18 are FDA Guidance equations unless an external guidance source is separately supplied and audited.
- Do not restore NDA Section 12.3, contraindication, or dose-reduction label wording as source-backed textbook content.
- Do not restore CPIC, ethnicity, Korean/Asian/White poor-metabolizer frequency claims.
- Do not restore Mager-Jusko TMDD code, quasi-equilibrium TMDD implementation, or full NONMEM code blocks.
- Do not reduce all nonlinear PK to a single "carrier saturation" geometry.
- Do not restore unsupported exact values such as omeprazole-clarithromycin observed maximum ratio = 33 unless separately verified and labeled.
- Do not restore unapproved figure embedding or any copyrighted textbook image.
- Keep Eq.2:264 as linear superposition, not MM ODE; MM belongs to Eq.2:266–2:274 family.
- ver2-specific guardrail: clarithromycin MBI numerics ($k_{inact}=0.07$ min⁻¹, $k_E\approx 0.23$ day⁻¹, $k_{inact}/k_E=438$, $C_{u,I}/K_I=0.025$, 11× vs 1.025×) are textbook-derived from T17 p.558 — do not relabel them as FDA guidance or NDA submission language.
- ver2-specific guardrail: phenytoin numerics ($V_m\approx 500$ mg/day, $K_m\approx 0.4$ mg/L, $f_u\approx 0.1$, $K_m'\approx 4$ mg/L, 치료역 10–20 mg/L, $V_m$ 20%↓→Css 2× sensitivity) are textbook-derived from T16 pp.503–506 — do not relabel as patient-specific NDA examples.
- ver2-specific guardrail: PK22 Table 22.2 numerics ($a\approx 0.041$, $k_{out}\approx 0.023$ h⁻¹) are direct case-study anchors from G p.585 — do not extrapolate to other autoinduction drugs without source.
- ver2-specific guardrail: mass action equivalence triangle (Eq.2:266 ↔ Eq.16-7 ↔ Eq.17-11) is CRUCIBLE_DERIVED interpretive synthesis grounded in the three textbook equations — do not present as "the textbook explicitly states" without keeping the labeled status.
- v3-specific guardrail: mass action equivalence triangle은 §2 C5에 단일 canonical form으로만 등장하며, §2 C2와 §8.1 #7은 cross-reference로만 표기됨. 이 cross-reference 구조를 다시 3중 풀어 쓰지 말 것 (v3 consolidation 회복 금지).
- v3-specific guardrail: C2 [⚡ Apex Concept] 배지와 Plausible Fallacy "Single-dose Fit Trap" 구조적 분석은 EXPERT_INFERENCE, v3 label 보존 의무 — textbook 직접 인용으로 relabel 금지. 단일 용량 fit ridge lock 분석은 G p.116 ρ=−0.96 사례를 압축한 v3 interpretive synthesis임.
- v3-specific guardrail: §5 CP1~CP8의 ⚡ 기억 고리 8개와 CP2의 🚨 치명적 타격 1개는 모두 EXPERT_INFERENCE, v3 — 구조적 비유 인코딩 (예: "공장 한계 vs 도로 한계", "문 막기 vs 자물쇠 교체")이지 textbook 직접 인용이 아님. 비유의 구체적 어휘를 textbook anchor로 재label 금지.
- v3-specific guardrail: §2 C1~C6 카드 말미의 "이 mechanism에서 30초 진단 질문" 6개는 §1.2 거장 시그널 6개를 §2 카드 메커니즘에 mapping한 EXPERT_INFERENCE, v3 — 새 진단 시그널을 추가하거나 §1.2 표의 6개 시그널 번호 매핑을 변경하지 말 것.
- v3-specific guardrail: §2 C1~C6의 Practice Brief 6개는 EXPERT_INFERENCE, v3 — 즉각 실행 지시 (도구·순서·기간) 형식. 새 정량값 threshold 추가하지 말 것 ($\rho > 0.9$, RSE > 50%, FG/FH 사례 등은 ver2 본문 또는 G p.116/T17 pp.553–554 anchor의 재인용임).

### B6. Crucible Guardrails

- Crucible is not a raw content source at this stage.
- Preserve only already-adopted or explicitly allowed Grade A logic.
- Do not reintroduce omitted or rejected Crucible items.
- Do not convert expert interpretation into textbook-derived fact.
- Expert additions must remain labeled as `EXPERT_INFERENCE` or `CRUCIBLE_DERIVED` if not directly textbook-derived.
- ver2 Crucible additions (30-second 진단 시그널 6개, Master clock 위계, Mass action equivalence triangle, named diagnostic signatures) all carry CRUCIBLE_DERIVED label and remain bounded — do not unmark them.
- v3 additions (C2 Apex badge, C2 Plausible Fallacy, §1.2 ↔ §2 30-second echo questions, Practice Briefs, CP1~CP8 Memory Hooks, CP2 Critical Blow) all carry EXPERT_INFERENCE, v3 label — interpretive synthesis 또는 구조적 비유 encoding이지 textbook 직접 인용 또는 Crucible Grade A logic이 아니다. v3 추가는 EXPERT_INFERENCE 등급에 머물며, Phase 5 HTML rendering에서도 이 label이 학습자 본문에 visible inline 또는 callout box로 표시되어야 함.

### B7. Deprecated and Forbidden Restorations

- Step 1 Draft v0 is deprecated.
- Do not copy Step 1 prose into the learner body except through a formally logged micro-patch.
- Do not restore rejected overclaims, unsupported numerical values, unsupported regulatory claims, source-unsupported examples, unapproved code, or unapproved figures.
- Do not use Audit/Crucible as broad rewrite sources.

### B8. PATCH MODE Splice Verification Table (ver1과 동일 — figure marker 위치 불변)

| Marker # | Anchor text | Anchor found? | Match count | Inserted? | Final location (§ + card) |
| --- | --- | --- | --- | --- | --- |
| 1 | `## 1.1 지식 그래프 위치` | YES | 1 | YES | §1.1 지식 그래프 위치 |
| 2 | `## C1. Nonlinearity Diagnostics — superposition이 깨지는 순간부터 시작한다` | YES | 1 | YES | §2 C1. Nonlinearity Diagnostics |
| 4 | `## C2. Capacity-limited Michaelis–Menten Kinetics — $V_{max}$/$K_m$가 dose 조정의 비대칭성을 만든다` | YES | 1 | YES | §2 C2. Capacity-limited Michaelis–Menten Kinetics |
| 6 | `## C3. Time-dependent Turnover and Mechanism-Based Inhibition — 농도 시계와 enzyme 시계를 분리한다` | YES | 1 | YES | §2 C3. Time-dependent Turnover and MBI |
| 8 | `## C4. Binding, TMDD, and Displacement-only DDI — total concentration을 그대로 믿지 않는다` | YES | 1 | YES | §2 C4. Binding, TMDD, and Displacement-only DDI |
| 10 | `## C5. Quantitative DDI Prediction — $f_m$, inhibitor strength, route가 AUC ratio를 만든다` | YES | 1 | YES | §2 C5. Quantitative DDI Prediction |
| 12 | `## C6. Multifaceted/Transporter and PD Interactions — 하나의 perpetrator가 하나의 mechanism만 갖는다고 가정하지 않는다` | YES | 1 | YES | §2 C6. Multifaceted/Transporter and PD Interactions |

### B9. Zero-Omission Coverage Matrix (ver2 업데이트 — PRESENT_COMPRESSED → PRESENT)

| Domain | Required item | Evidence in PART A | Status | Action |
| --- | --- | --- | --- | --- |
| C1 Scope concepts | Nonlinearity diagnostics, superposition, AUC/Dose vs Dose | §1.2 거장 시그널 #1, §2 C1, §7 Q1–Q3 | PRESENT | No action |
| C1 Scope concepts | Capacity-limited MM, CL(C), two limits, phenytoin/alcohol/ascorbic acid 정량 anchors | §2 C2 (ver2 정량 보강), §7 Q4–Q6 | **PRESENT (ver2)** | Verbatim 정량값 회수 |
| C1 Scope concepts | Time-dependent turnover, auto/heteroinduction, MBI 정량, recovery clock | §1.2 #2, §2 C3 (ver2 MBI numerics 보강), §5 CP1–CP2/CP6–CP7, §7 Q7–Q8 | **PRESENT (ver2)** | clarithromycin numerics 회수 |
| C1 Scope concepts | Binding, TMDD, open vs closed system, displacement-only DDI caution, drug-metabolite model | §2 C4 (ver2 metabolite + binding 사례 보강), §5 CP4–CP5, §7 Q9·Q15 | **PRESENT (ver2)** | §2.7.6 drug-metabolite + saturable binding 사례 회수 |
| C1 Scope concepts | Quantitative DDI prediction: reversible inhibition 정량, fm, route, PM amplification, induction/withdrawal, inhibitor classification | §2 C5 (ver2 정량 보강 + Table 17-5), §7 Q10–Q12·Q16, §1.2 #4 | **PRESENT (ver2)** | Theophylline-Enoxacin / Desipramine-Quinidine·Fluoxetine / Diltiazem-Lovastatin / Fluconazole-Midazolam / Inhibitor classification 회수 |
| C1 Scope concepts | Multifaceted/transporter and PD interactions 정량 + 수식 spine | §2 C6 (ver2 정량 anchor + Eq.3:48–3:53 + Eq.17-19~22 보강), §5 CP7–CP8, §7 Q13–Q14·Q17, §1.2 #5 | **PRESENT (ver2)** | Digoxin-Quinidine / Rosuvastatin-Cyclosporine / Phenobarbital-Dicumarol / PD 수식 spine 회수 |
| C1 Scope concepts | Flow-dependent kinetics, ethanol integrated case | §1.2 #5, §2 C2 alcohol 정량 anchor, §8.2 Dependencies | PRESENT | Compressed by Content Lock |
| C2 Required data anchors | Phenytoin Vm/Km/fu/Km'/therapeutic/Eq.16-10 t90/Eq.16-11/Vm sensitivity; alcohol Vm/Km/Vd/임상 anchor; ascorbic acid CLR 변화 | §2 C2 Clinical anchors (ver2 신설) | **PRESENT (ver2)** | Verbatim |
| C2 Required data anchors | Theophylline-enoxacin (8.8→22h, 4→9, fm=0.67, CLratio=0.44), desipramine-quinidine/fluoxetine 정량, MBI numerics, diltiazem-lovastatin (1.27 vs 3.57), fluconazole-midazolam (FH/FG), digoxin-quinidine (CL/CLR/Vd/F), rosuvastatin-cyclosporine (Cmax 11×, AUC 7×), atorvastatin-rifampin acute, phenobarbital-dicumarol (4 days, 3-4주), inhibitor strength classification | §2 C5–C6 (ver2 정량 보강), §7 Q8/Q11/Q13/Q16 | **PRESENT (ver2)** | All Audit T1 MATCH 정량값 회수 |
| C3 Audit MUST_FIX/SHOULD_FIX | Wrong Eq.2:264 MM citation correction | §2 C2 and §7 Q3 | PRESENT | No action |
| C3 Audit MUST_FIX/SHOULD_FIX | Remove unsupported FDA Guidance/NDA/CPIC/code/TMDD overclaims | §8.3 plus PART B B5–B7 | PRESENT | Forbidden restoration guardrails included |
| C3 Audit MUST_FIX/SHOULD_FIX | AUC-based F warning when CL is not constant | §2 C2 Critical caution | PRESENT | No action |
| C3 Audit MUST_FIX/SHOULD_FIX | Vmax/Km separate estimation needs concentration around/below Km | §2 C2 Trench tip + ver2 Vmax–Km Ridge Lock | PRESENT | Named diagnostic |
| C4 Audit T5 findings | High-impact omissions checked against compressed Content Lock structure | §2 C1–C6, §5, §7, §8 | PRESENT | No unresolved HIGH item |
| C4 Audit T5 findings | §2.7.6 drug-metabolite model self-contained inclusion | §2 C4 ver2 신설 단락 | **PRESENT (ver2)** | Audit Trigger 5 sourced warning included |
| C4 Audit T5 findings | Salicylic acid opposing nonlinearities (Fig.16-28) | §2 C4 ver2 신설 단락 | **PRESENT (ver2)** | Source-backed |
| C5 Figure coverage | Approved KEEP markers #1/#2/#4/#6/#8/#10/#12 | PART A figure marker blocks | PRESENT | All markers spliced exactly once |
| C6 Page/source tags | Existing source tags and [확인 필요] policy preserved; no fabricated new page tags | PART A source tags; PART B B3 | PRESENT | ver2 추가 anchor 모두 Audit MATCH source page tag 보존 |
| C7 Crucible Grade A preservation | Mechanism-triad, two clocks, fm vulnerability, mass action equivalence triangle, master clock 위계, named diagnostic signatures, 30-second signals | §1.2 (신설), §2 C2/C3/C5 augmentation, §7 Q15–Q17, §8.1 #7 | **PRESENT (ver2)** | All bounded, labeled CRUCIBLE_DERIVED |
| C8 Deprecated draft regression | Unsupported overclaims, external examples, code blocks, unapproved figures not restored | §8.3 and PART B B5–B7 | PRESENT | Regression guardrails preserved |
| C9 Canonical body integrity | Content Lock v2 §1 onward preserved with approved markers plus labeled augmentations and ver2 audit-MATCH anchor restoration | PART A | PRESENT | No canonical scientific rewrite performed; all ver2 additions are surgical injections at named locations |

### B10. Micro-Patch Log (ver2 + v3 통합)

ver1 Phase 4D 결과는 PART A 본문을 변경하지 않은 상태였으므로 micro-patch 0건이었다. ver2에서는 surgical 추가 39건(MP-01 ~ MP-39)을 수행하였다. v3에서는 Independent Master Reviewer NO-GO 판정에 대응하여 추가 surgical patch 19건(MP-V3-01 ~ MP-V3-19)을 수행하였다. 본문의 기존 문장은 어느 단계에서도 변경하지 않았다. 모든 추가는 (a) 새 Annotation/Subsection/Equation/Callout 블록 형태로 기존 문장 사이에 삽입되었거나, (b) 이미 존재하는 anchor list/answer를 추가 정량값으로 확장한 형태이며, ver1과 ver2의 모든 기존 문장과 figure marker 위치는 보존되었다.

| # | Location | Type | Source | Inserted text 요약 |
| --- | --- | --- | --- | --- |
| MP-01 | §1.2 (신설 subsection) | NEW SUBSECTION | CRUCIBLE_DERIVED + Audit MATCH | 거장의 30초 진단 시그널 6개 표 + 짧은 도입 문단 |
| MP-02 | §2 C2 Master Lens 직후 ANNOTATION | NEW ANNOTATION | CRUCIBLE_DERIVED | mass action QSSA 출처 + flow-extraction 분기점 통찰 |
| MP-03 | §2 C2 Core equations | NEW EQUATION BLOCK | TEXTBOOK_DERIVED (G Eq.2:271, p.117) | AUC = (C0/2Vmax)(Km + C0/2) IV bolus 식 + 해석 |
| MP-04 | §2 C2 Clinical anchors | EXPANDED | TEXTBOOK_DERIVED (T16 pp.491, 503–506) | Phenytoin Vm/Km/fu/Km'/therapeutic + Eq.16-10 t90 + Eq.16-11 + Vm sensitivity 정량값 |
| MP-05 | §2 C2 Clinical anchors | EXPANDED | TEXTBOOK_DERIVED (T16 pp.501–502) | Alcohol drink/hr 임상 anchor 추가 |
| MP-06 | §2 C2 Clinical anchors | EXPANDED | TEXTBOOK_DERIVED (T16 p.492) | Ascorbic acid CLR < 0.5 → 21 mL/min 정량 |
| MP-07 | §2 C2 Diagnostic signatures | NEW DIAGNOSTIC NAMING | CRUCIBLE_DERIVED | "Vmax–Km Ridge Lock" 정식 명명 + rescue 지침 |
| MP-08 | §2 C3 Master Lens 직후 ANNOTATION | NEW ANNOTATION | CRUCIBLE_DERIVED + TEXTBOOK_DERIVED (T17 pp.560–561) | Master clock 위계 통찰 |
| MP-09 | §2 C3 Autoinduction anchors | EXPANDED | TEXTBOOK_DERIVED (G p.585) | PK22 Table 22.2 a ≈ 0.041, k_out ≈ 0.023 h⁻¹ + carbamazepine 5일 + phenobarbital-dicumarol clock 위계 |
| MP-10 | §2 C3 NEW SUBSECTION | NEW SUBSECTION | TEXTBOOK_DERIVED (T17 p.558) | Quantitative MBI anchors (clarithromycin numerics) |
| MP-11 | §2 C3 Diagnostic signatures | NEW DIAGNOSTIC NAMING | CRUCIBLE_DERIVED | "Trough Envelope Drift" / "Single-dose Fit Trap" / "Washout Trap" 정식 명명 표 |
| MP-12 | §2 C4 Master Lens 직후 ANNOTATION | NEW ANNOTATION | CRUCIBLE_DERIVED (G Eq.2:303) | Mass-balance 강제성 ($C_u = K^0/CL_u$) 통찰 |
| MP-13 | §2 C4 NEW SUBSECTION (Saturable binding 사례) | NEW SUBSECTION | TEXTBOOK_DERIVED (T16 pp.508, 511–516, 520–522) | Naproxen, Cefonicid, Disopyramide, Trandolaprilat, Bosentan (Vss 0.67→0.16), Dicloxacillin (CLR 1g vs 2g), Salicylic acid opposing nonlinearities |
| MP-14 | §2 C4 NEW SUBSECTION (Saturable transport) | NEW EQUATION + SUBSECTION | TEXTBOOK_DERIVED (T16 p.495 Eq.16-3) | Eq.16-3 saturable transport rate + secretion vs reabsorption 방향 |
| MP-15 | §2 C4 NEW SUBSECTION (Drug-metabolite) | NEW SUBSECTION | TEXTBOOK_DERIVED (G pp.135–139, Audit Trigger 5) | §2.7.6 drug-metabolite nonlinear model 한 단락 + p.137 source-backed 경고 |
| MP-16 | §2 C5 Master Lens 직후 ANNOTATION | NEW ANNOTATION + EQUATION | CRUCIBLE_DERIVED + TEXTBOOK_DERIVED | Mass action equivalence triangle: Eq.2:266 ↔ Eq.16-7 ↔ Eq.17-11 |
| MP-17 | §2 C5 Clinical anchors | EXPANDED | TEXTBOOK_DERIVED (T17 pp.546–554) | Theophylline-Enoxacin, Desipramine-Quinidine, Desipramine-Fluoxetine, Diltiazem-Lovastatin, Fluconazole-Midazolam 정량값 |
| MP-18 | §2 C5 NEW SUBSECTION (Inhibitor classification) | NEW SUBSECTION | TEXTBOOK_DERIVED (T17 p.549, Table 17-5) | Strong/Moderate/Weak 분류표 |
| MP-19 | §2 C6 Core multifaceted anchors | EXPANDED | TEXTBOOK_DERIVED (T17 Table 17-8, Fig.17-11, Fig.17-17, Fig.17-19) | Digoxin-Quinidine 정량, Rosuvastatin-Cyclosporine 정량, Atorvastatin-Rifampin 정량, Phenobarbital-Dicumarol 정량 |
| MP-20 | §2 C6 Acute/chronic × oral/IV diagnostic matrix | NEW TABLE | TEXTBOOK_DERIVED (T17 pp.553–565) | 4-quadrant matrix |
| MP-21 | §2 C6 PD interaction layer | EXPANDED with EQUATIONS | TEXTBOOK_DERIVED (G pp.224–227, T17 pp.567–570) | Eq.3:48 multiple binding, Eq.3:49 competitive shift, Eq.3:50 noncompetitive 감소, Eq.3:52–53 enantiomer (ketamine), Eq.17-21 ceiling 식, isobologram 분류, Greco Eq.17-22 1줄 reference |
| MP-22 | §5 CP6 Test 보강 | EXPANDED | TEXTBOOK_DERIVED (T17 pp.557–558) | $k_{inact}/k_E$ ratio 점검 추가 |
| MP-23 | §5 CP7 Correction 정량 보강 | EXPANDED | TEXTBOOK_DERIVED (Fig.17-19) | Atorvastatin-Rifampin acute 정량 추가 |
| MP-24 | §5 CP8 Correction 수식 보강 | EXPANDED | TEXTBOOK_DERIVED (Eq.3:49, Eq.3:50, Eq.17-21) | 경쟁/비경쟁/full agonist 수식 한 줄 spine |
| MP-25 | §7 Q4 Answer 정량 보강 | EXPANDED | TEXTBOOK_DERIVED (T16 pp.491, 503) | Phenytoin parameters 추가 |
| MP-26 | §7 Q5 Answer 정량 보강 | EXPANDED | TEXTBOOK_DERIVED (T16 p.492) | Ascorbic acid CLR 정량 추가 |
| MP-27 | §7 Q6 Answer 명명 보강 | EXPANDED | CRUCIBLE_DERIVED | "Vmax–Km Ridge Lock" 명명 + ρ 사례 추가 |
| MP-28 | §7 Q7 Answer 명명 보강 | EXPANDED | CRUCIBLE_DERIVED + TEXTBOOK_DERIVED | "Trough Envelope Drift" + "Single-dose Fit Trap" 명명 + PK22 k_out 정량 |
| MP-29 | §7 Q8 Answer 정량 보강 | EXPANDED | TEXTBOOK_DERIVED (T17 p.558) | Clarithromycin MBI numerics 정량 (kinact, kE, ratio, 11× vs 1.025×) |
| MP-30 | §7 Q9 Answer 수식 보강 | EXPANDED | CRUCIBLE_DERIVED (G §2.7.5) | Mass-balance 강제성 한 줄 ($C_u = K^0/CL_u$) |
| MP-31 | §7 Q11 Answer 정량 보강 | EXPANDED | TEXTBOOK_DERIVED (T17 pp.553–554) | Fluconazole-Midazolam $F_H$, $F_G$ 정량 |
| MP-32 | §7 Q13 Answer 정량 보강 | EXPANDED | TEXTBOOK_DERIVED (Fig.17-19) | Atorvastatin-Rifampin Cmax 10×, AUC 7×, t½ 8→3h |
| MP-33 | §7 Q14 Answer 수식 보강 | EXPANDED | TEXTBOOK_DERIVED (Eq.3:49, Eq.3:50, Eq.17-21) | 경쟁/비경쟁 수식 한 줄 spine |
| MP-34 | §7 Q15 신설 | NEW QUESTION | TEXTBOOK_DERIVED (G pp.135–139) | Drug–metabolite identifiability question |
| MP-35 | §7 Q16 신설 | NEW QUESTION | TEXTBOOK_DERIVED (T17 p.549) | Inhibitor classification question |
| MP-36 | §7 Boss Dilemma → Q17 재번호 | RENUMBER | — | Q15 (Boss Dilemma) → Q17. Splice anchor 변화 없음 |
| MP-37 | §7 Q17 (Boss Dilemma) Answer 보강 | EXPANDED | CRUCIBLE_DERIVED + TEXTBOOK_DERIVED | (7) Mass action equivalence triangle 점검 항목 추가 |
| MP-38 | §8.1 7번 문장 신설 | NEW SENTENCE | CRUCIBLE_DERIVED | Mass action equivalence triangle 한 문장 |
| MP-39 | §8.4 Compression check | EXPANDED | — | ver2 보강 통계 메모 |
| MP-V3-01 | §2 C2 heading 직후 | NEW BADGE | EXPERT_INFERENCE, v3 | [⚡ Apex Concept — v3] 배지 + Apex 지위 선언 |
| MP-V3-02 | §2 C2 (Diagnostic signatures 직후, Critical caution 직전) | NEW SUBSECTION | EXPERT_INFERENCE, v3 | Plausible Fallacy "Single-dose Fit Trap" 구조적 분석 + 실무 발현 패턴 |
| MP-V3-03 | §2 C2 ANNOTATION (mass action 부분) | CONSOLIDATION | v3 consolidation | Eq.2:266 ↔ Eq.16-7 ↔ Eq.17-11 명시 등식 → "→ §2 C5 mass action equivalence triangle 참조"로 cross-ref 축약. QSSA + flow-extraction 통찰은 보존. |
| MP-V3-04 | §8.1 #7 | CONSOLIDATION | v3 consolidation | "→ §2 C5 mass action equivalence triangle 참조"로 cross-ref 축약 |
| MP-V3-05 | §2 C1 RECAP 직후 | NEW CALLOUT | EXPERT_INFERENCE, v3 | "이 mechanism에서 30초 진단 질문 (§1.2 #1)" + Practice Brief |
| MP-V3-06 | §2 C2 (Plausible Fallacy 끝) | NEW LINE | EXPERT_INFERENCE, v3 | "이 mechanism에서 30초 진단 질문 (§1.2 #1, #5)" |
| MP-V3-07 | §2 C2 RECAP 직후 | NEW CALLOUT | EXPERT_INFERENCE, v3 | Practice Brief — Single-dose Fit Trap rescue 지시 |
| MP-V3-08 | §2 C3 RECAP 직후 | NEW CALLOUT | EXPERT_INFERENCE, v3 | "이 mechanism에서 30초 진단 질문 (§1.2 #2, #6)" + Practice Brief |
| MP-V3-09 | §2 C4 RECAP 직후 | NEW CALLOUT | EXPERT_INFERENCE, v3 | "이 mechanism에서 30초 진단 질문 (§1.2 #3)" + Practice Brief |
| MP-V3-10 | §2 C5 RECAP 직후 | NEW CALLOUT | EXPERT_INFERENCE, v3 | "이 mechanism에서 30초 진단 질문 (§1.2 #4)" + Practice Brief |
| MP-V3-11 | §2 C6 RECAP 직후 | NEW CALLOUT | EXPERT_INFERENCE, v3 | "이 mechanism에서 30초 진단 질문 (§1.2 통합)" + Practice Brief |
| MP-V3-12 | §5 CP1 직후 | NEW CALLOUT | EXPERT_INFERENCE, v3 | ⚡ 기억 고리 "농도 때문인가, 시간 때문인가" |
| MP-V3-13 | §5 CP2 직후 | NEW CALLOUT × 2 | EXPERT_INFERENCE, v3 | ⚡ 기억 고리 "구조적 이동 vs 예측 가능한 누적" + 🚨 치명적 타격 (Critical Blow) |
| MP-V3-14 | §5 CP3 직후 | NEW CALLOUT | EXPERT_INFERENCE, v3 | ⚡ 기억 고리 "공장 한계 vs 도로 한계" |
| MP-V3-15 | §5 CP4 직후 | NEW CALLOUT | EXPERT_INFERENCE, v3 | ⚡ 기억 고리 "열린 계 vs 닫힌 계" |
| MP-V3-16 | §5 CP5 직후 | NEW CALLOUT | EXPERT_INFERENCE, v3 | ⚡ 기억 고리 "자리 뺏기 vs 공장 멈추기" |
| MP-V3-17 | §5 CP6 직후 | NEW CALLOUT | EXPERT_INFERENCE, v3 | ⚡ 기억 고리 "문 막기 vs 자물쇠 교체" |
| MP-V3-18 | §5 CP7 직후 | NEW CALLOUT | EXPERT_INFERENCE, v3 | ⚡ 기억 고리 "방향 전환 스위치" |
| MP-V3-19 | §5 CP8 직후 + §1 ANCHOR + §1.2 #5 + §2 C3 prose | NEW CALLOUT + 3 INLINE ANNOT | EXPERT_INFERENCE, v3 | ⚡ 기억 고리 "농도 바꾸기 vs 반응 바꾸기" + $f_u$ / $E_H$ / $CL_{int}$ 첫 등장 inline parenthetical 정의 (PATCH 6) |

### B11. Mastery Augmentation Log (ver1 + ver2 + v3 통합)

ver1에서 인정된 6개 augmentation에 ver2의 정량 anchor 회수 + 명명 진단 시그너처 + mass action equivalence triangle augmentation 8개를 통합 기록하였고, v3에서는 Independent Master Reviewer 지적에 대응한 5개 augmentation을 추가 통합한다.

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
| --- | --- | --- | --- | --- | --- | --- |
| 1 (ver1) | §2 C1 | J/W | YES | CRUCIBLE_DERIVED | Converts diagnostic plot reading into mechanism-triage workflow | Low |
| 2 (ver1) | §2 C2 | F | YES | TEXTBOOK_DERIVED | Prevents reduction of MM to zero-order slogan and emphasizes dose-adjustment asymmetry | Low |
| 3 (ver1) | §2 C3 | M/J | YES | EXPERT_INFERENCE | Short mental check for concentration clock vs enzyme pool clock | Medium; labeled |
| 4 (ver1) | §2 C4 | J | YES | TEXTBOOK_DERIVED | Prevents total-only exposure interpretation in binding/displacement contexts | Low |
| 5 (ver1) | §2 C5 | J/R | YES | CRUCIBLE_DERIVED | Frames fm as DDI vulnerability without adding external thresholds | Low |
| 6 (ver1) | §2 C6 | F | YES | TEXTBOOK_DERIVED | Prevents single-mechanism overcall when PK metrics move discordantly | Low |
| 7 (ver2) | §1.2 | M/W | YES | CRUCIBLE_DERIVED + TEXTBOOK_DERIVED | 거장의 30초 진단 시그널 6개 표 — Crucible T1(c) 압축 + Audit MATCH 출처 | Low |
| 8 (ver2) | §2 C2 | M | YES | CRUCIBLE_DERIVED | mass action QSSA + flow-extraction 분기 통찰 (Big Idea 직후 annotation) | Low |
| 9 (ver2) | §2 C2 + §7 Q6 | NAMED DIAGNOSTIC | YES | CRUCIBLE_DERIVED | "Vmax–Km Ridge Lock" 정식 명명 + rescue 지침 | Low |
| 10 (ver2) | §2 C3 + §7 Q7/Q8 | NAMED DIAGNOSTICS | YES | CRUCIBLE_DERIVED | "Trough Envelope Drift" / "Single-dose Fit Trap" / "Washout Trap" 정식 명명 표 | Low |
| 11 (ver2) | §2 C3 | M/W | YES | CRUCIBLE_DERIVED + TEXTBOOK_DERIVED (T17 pp.560–561) | Master clock 위계 통찰 ($\max(t_{1/2}^{enzyme}, t_{1/2}^{inducer}, t_{1/2}^{drug})$ 가장 느린 시계 지배) | Low |
| 12 (ver2) | §2 C4 | M | YES | CRUCIBLE_DERIVED (G §2.7.5) | Mass-balance 강제성 ($C_u = K^0/CL_u$) 통찰 (Big Idea 직후 annotation) | Low |
| 13 (ver2) | §2 C5 + §8.1 #7 | M/W (3중 회수) | YES | CRUCIBLE_DERIVED + TEXTBOOK_DERIVED | Mass action equivalence triangle: Eq.2:266 ↔ Eq.16-7 ↔ Eq.17-11 — 본 세션 수학적 정점 | Low |
| 14 (ver2) | §2 C2/C3/C4/C5/C6 (정량 회수) | F (정량 보강) | YES | TEXTBOOK_DERIVED (Audit T1 MATCH list) | Phenytoin/alcohol/ascorbic acid; Clarithromycin MBI; PK22 numerics; Theophylline-Enoxacin/Desipramine 정량; Diltiazem-Lovastatin/Fluconazole-Midazolam route 정량; Digoxin-Quinidine/Rosuvastatin-Cyclosporine/Atorvastatin-Rifampin/Phenobarbital-Dicumarol 정량; Inhibitor classification table; Saturable binding 사례 (Bosentan/Cefonicid/Naproxen/Disopyramide/Salicylic acid); §2.7.6 drug-metabolite model; PD interaction 수식 spine (Eq.3:48–3:53, Eq.17-19~22) — 모두 Audit MATCH 분류 | Low |
| 15 (v3) | §2 C2 | APEX DESIGNATION + PLAUSIBLE FALLACY | YES | EXPERT_INFERENCE, v3 | C2를 본 세션 Apex Concept으로 정식 지정. "Single-dose Fit Trap"의 ridge-lock 메커니즘과 NONMEM 진단 패턴을 구조적으로 분석 (G p.116 ρ=−0.96 사례 압축). | Medium; labeled |
| 16 (v3) | §2 C1~C6 (각 카드 말미) | ECHO CIRCUIT | YES | EXPERT_INFERENCE, v3 | "이 mechanism에서 30초 진단 질문" 6개를 §1.2 거장 시그널 6개와 1:1 mapping. §1.2 isolated 상태 해소, 양방향 회로 형성. | Low |
| 17 (v3) | §2 C1~C6 (각 카드 RECAP 직후) | PRACTICE BRIEFS | YES | EXPERT_INFERENCE, v3 | 즉각 실행 지시 6개 (도구·순서·기간 명시). C2의 ρ>0.9 임계, C3의 enzyme half-life × 2~3 추적 기간 등은 ver2 anchor의 실무 재인용. | Low |
| 18 (v3) | §5 CP1~CP8 + CP2 | MEMORY HOOKS + CRITICAL BLOW | YES | EXPERT_INFERENCE, v3 | 8개 구조적 비유 인코딩 (공장/도로, 문/자물쇠, 자리/공장, 닫힌계/열린계, 농도/시간, 농도/반응, 누적/구조이동, 방향전환). CP2에 임상 파급력 최대 1쌍 Critical Blow 추가 (carbamazepine/phenobarbital 발작 예방 부전 시나리오). | Low |
| 19 (v3) | §2 C2 ANNOTATION + §8.1 #7 | CONSOLIDATION | YES | v3 consolidation | Mass action equivalence triangle 3중 중복을 §2 C5 단일 canonical + 2개 cross-reference 구조로 정리. ver2 통찰 손실 없음. | Low |

#### Rejected augmentation candidates (ver1 + ver2)

| Rejected candidate | Reason for rejection |
| --- | --- |
| New regulatory label wording for DDI dose adjustment | Rejected: would restore NDA/FDA-style external claim without attached regulatory source |
| New named examples beyond PDFs | Rejected: would violate source-boundary and no-new-example rule |
| Additional numerical thresholds for strong/moderate inhibitors beyond locked content | Rejected: would require external verification or broader rewrite |
| Mager-Jusko TMDD code restoration | Rejected: textbook scope에 없는 implementation; B5/B7 가드 |
| FDA Guidance "AUC ratio threshold" 명시 | Rejected: external source 없음; B5 가드 |
| CPIC ethnicity PM 빈도 회복 | Rejected: PDF 직접 근거 없음; B5 가드 |
| Omeprazole-clarithromycin "33×" exact 수치 | Rejected: textbook visual 추정값이고 정확 인쇄값 아님 (Audit MUST_FIX #7) |
| Step 1 Draft v0 "AI/ML moat" claims 회복 | Rejected: textbook 범위 외 (Audit T4 REJECT) |
| Atorvastatin-rifampin "Vd/F 17×, CL/F 9×" 회복 | Rejected: derived ratios 출처 불명 (Audit MUST_FIX #8) — Cmax/AUC/t½만 회수 |
| Carbamazepine, alcohol auto-induction에 PK22 numerics 외삽 | Rejected: PK22는 단일 case, 외삽 source 없음; B5 ver2 guardrail |

---

## v3 Final Phase 4D Re-certification Statement

ver2의 14개 augmentation을 모두 보존한 상태에서 v3 surgical augmentation 5개 항목 (B11 #15~#19)을 추가하였다. 모든 v3 추가 항목은:

1. **Source-boundary 위반 없음** — v3 추가는 모두 [EXPERT_INFERENCE, v3] label로 epistemic status 명시. 신규 FDA·EMA·CPIC·NDA threshold 또는 외부 가이드라인 인용 추가 없음. 기존 ver2 page tag·인용·정량값 변경 없음. C2 Plausible Fallacy의 ridge-lock 분석은 G p.116 ρ=−0.96 사례를 압축한 v3 interpretive synthesis이며, Memory Hook 8개는 textbook anchor의 구조적 비유 인코딩이지 신규 source claim이 아님.
2. **Splice Verification Table B8 변경 없음** — figure marker 위치는 ver1·ver2와 동일하므로 anchor·match count·inserted 모두 변동 없음. v3 추가는 figure marker 사이의 본문 그리고 §5/§8 영역에만 surgical하게 삽입됨.
3. **Regression guardrails (B5/B6/B7) 강화** — v3-specific guardrail 6개를 B5에 추가하였다: (a) mass action triangle은 §2 C5 단일 canonical만 유지, (b) C2 Apex 배지·Plausible Fallacy는 EXPERT_INFERENCE 등급 보존 의무, (c) Memory Hook의 구조적 비유는 textbook 인용으로 relabel 금지, (d) 30초 진단 질문 6개는 §1.2와 1:1 mapping 보존, (e) Practice Brief의 정량 임계는 ver2 anchor 재인용임을 명시. B6에는 v3 EXPERT_INFERENCE label 유지 의무 추가.
4. **Zero-Omission Coverage Matrix B9 변동 없음** — ver2의 PRESENT 상태가 모두 보존됨. v3는 누락 회복이 아니라 학습 회로 강화이므로 B9 status 변경 사유 아님.
5. **Mastery-Uplift 강화 — 3단 통합 회로 완성:** §1.2 거장의 30초 진단 시그널(6개) → §2 C1~C6 카드 말미의 30초 진단 질문(6개, §1.2와 1:1 mapping) → §2 C2 Apex Concept + Plausible Fallacy "Single-dose Fit Trap" → §5 CP1~CP8 Memory Hook(8개 구조적 비유) + CP2 Critical Blow → §8.1 #7 mass action triangle(§2 C5 cross-ref). ver2의 통합 회로(2단)에 v3는 (a) Apex 지정으로 학습 우선순위, (b) Memory Hook으로 confusion pair 영구 각인, (c) Critical Blow로 임상 파급력 최대 쌍 강조 — 이 세 축을 추가하여 학습자가 "수식 외움"에서 "mechanism mapping + 임상 위험 직관"까지 한 회로로 회수하도록 끌어올렸다.

**최종 판정: 5개 인증서 모두 PASS — Phase 5 HTML compile go.**

---

## Final v3 All-Pass Checklist (8항목)

| # | 항목 | 상태 | 검증 위치 |
|---|---|---|---|
| 1 | Apex Concept 지정 + 배지 + Plausible Fallacy 추가 (C2 단독) | ✅ PASS | §2 C2 heading 직후 [⚡ Apex Concept — v3] 배지; "### Plausible Fallacy" subsection (Single-dose Fit Trap 구조 분석) |
| 2 | §1.2 거장 시그널 ↔ §2 카드 echo 회로 형성 (C1~C6 모두) | ✅ PASS | §2 C1, C2, C3, C4, C5, C6 각 카드 말미 "이 mechanism에서 30초 진단 질문" 6개 — §1.2 시그널 #1~#6과 1:1 mapping |
| 3 | §5 Memory Hook 8개 모두 추가 (CP1~CP8) — 구조적 비유 인코딩 | ✅ PASS | §5 CP1(농도/시간), CP2(누적/구조이동), CP3(공장/도로), CP4(닫힌계/열린계), CP5(자리뺏기/공장멈추기), CP6(문/자물쇠), CP7(방향전환), CP8(농도/반응) |
| 4 | §5 Critical Blow 1개 추가 (임상 파급력 최대 1쌍에만) | ✅ PASS | §5 CP2 직후 🚨 치명적 타격 — carbamazepine/phenobarbital autoinduction을 accumulation으로 오해 시 발작 예방 부전 시나리오 |
| 5 | Mass action equivalence triangle 3중 중복 정리 (§2 C5 canonical 단일 유지) | ✅ PASS | §2 C5 ANNOTATION에 full triangle 보존; §2 C2 ANNOTATION과 §8.1 #7은 "→ §2 C5 mass action equivalence triangle 참조"로 cross-ref 축약 |
| 6 | §2 C1~C6 Practice Brief 6개 추가 (즉각 실행 지시) | ✅ PASS | 각 카드 RECAP 직후 `> **실무 체화 요약(Practice Brief) — [EXPERT_INFERENCE, v3]**` blockquote 6개 |
| 7 | 첫 등장 ANNOTATION 추가 ($f_u$, $E_H$, $CL_{int}$) — $CL_b$/$CL_H$는 본문 부재로 vacuous | ✅ PASS | §1 ANCHOR ($f_u$ inline), §1.2 표 #5 행 ($E_H$ inline), §2 C3 prose ($CL_{int}$ inline) — 모두 [v3] tag |
| 8 | PART B 업데이트 + 비-위반 검증 (신규 FDA/CPIC/NDA threshold 추가 없음, page tag·정량값 변경 없음, figure marker 위치 불변) | ✅ PASS | Phase 4D Cert table v3 재인증 / v3 Change Log / §8.4 / B5 v3 guardrail 6개 / B6 v3 EXPERT_INFERENCE 유지 의무 / B10 MP-V3-01~MP-V3-19 / B11 #15~#19. Splice Verification Table B8 ver2 동일 |

**최종 판정 (v3): 8/8 PASS — Independent Master Reviewer NO-GO 판정 3개 구조 gap 모두 해소됨. Phase 5 HTML compile go.**

---

*v3 file generated by surgical patch editor. Source: 08_html_compile_input_master_ver2.md → 08_html_compile_input_master_v3.md. All v3 additions labeled [EXPERT_INFERENCE, v3] except `v3 consolidation` and `v3 ANNOTATION` per change log. Body integrity: ver2의 모든 기존 문장·정량값·page tag·figure marker 위치 100% 보존.*

---

## v3.1 Final Checklist

| # | 항목 | 상태 | 검증 위치 |
|---|---|---|---|
| 1 | PART A readability improved | ✅ PASS | 11개 surgical patch (P-01 ~ P-11) 적용. Learner Navigation Aid 한국어화 (P-01~P-03), §1 MASTER LENS 연결어 추가 (P-04), §2 C2 ANNOTATION 표현 정제 (P-05), §2 C2 AUC 해석 sentence split (P-06), Alcohol intuition phrasing 정제 (P-07), §2 C3 turnover sentence split (P-08), §2 C4 metabolite sentence split (P-09), §2 C4 TMDD 첫 등장 gloss (P-10), §8.2 TDM 마지막 문장 grammar (P-11) |
| 2 | Scientific content unchanged | ✅ PASS | 수치, 임상 anchor, 정량값, parameter symbol, source label 전부 v3와 동일. 11개 patch는 표현 개선에 한정됨. |
| 3 | Equations preserved | ✅ PASS | 모든 MathJax 수식 ($...$, $$...$$), Eq. 번호, 파라미터 symbol ($V_{max}$, $K_m$, $C_{u,ss}$, $f_m$, $C_{u,I}/K_I$, $k_{inact}/k_E$ 등) 변경 없음. |
| 4 | Page tags preserved | ✅ PASS | [G pp.XX–YY], [T16 pp.XX–YY], [T17 pp.XX–YY], [G Eq.X:YYY], [G p.XX, Fig.X.YY] 등 모든 source page tag 변경 없음. 새 page tag 추가 없음. |
| 5 | Figure markers preserved | ✅ PASS | `<!-- FIGURE_POINTER -->`, `<!-- FIGURE_SCHEMATIC -->`, `<!-- /FIGURE_POINTER -->`, `<!-- /FIGURE_SCHEMATIC -->` 모든 marker 위치·내용 v3와 동일. Splice Verification Table B8 변경 없음. |
| 6 | Source-boundary preserved | ✅ PASS | [EXPERT_INFERENCE, v3], [CRUCIBLE_DERIVED], [TEXTBOOK_DERIVED], [v3 consolidation], [v3 ANNOTATION] 모든 epistemic label 보존. PART B B5 (Audit Guardrails) / B6 (Crucible Guardrails) / B7 (Deprecated Restorations) 전부 보존. 새 FDA·EMA·CPIC·NDA threshold 또는 외부 가이드라인 인용 추가 없음. |
| 7 | HTML-readiness preserved | ✅ PASS | PART B 전체 (B1~B11) 변경 없음. Marker-to-component mapping, navigation anchor rules, Mermaid self-check, page tag rendering rules, MathJax delimiter 모두 v3와 동일. `<!-- MASTER LENS -->`, `<!-- ANCHOR -->`, `<!-- ANNOTATION -->`, `<!-- TRENCH -->`, `<!-- CONFUSION -->`, `<!-- SELF-TEST -->`, `<!-- RECAP -->` 모든 HTML compiler marker 보존. |
| 8 | Ready for Phase 5 HTML compilation | ✅ PASS | 8/8 PASS. 보류된 4개 High-risk 항목 (H-01 ~ H-04, compiler artifact가 학습자 본문에 노출된 부분)은 Phase 5에서 CSS-level muted 스타일 또는 `display:none` 처리로 위임. 본 v3.1은 Phase 5 HTML compile에 즉시 진입 가능. |

**최종 판정 (v3.1): 8/8 PASS — PART A 한국어 독해성이 개선되었으며 v3의 모든 과학적 무결성·HTML-readiness·source boundary가 보존되었다. Phase 5 HTML compile go.**

---

## v3.2 Final Checklist

| # | 항목 | 상태 | 검증 위치 |
|---|---|---|---|
| 1 | PART A 영어 산문의 포괄적 한국어 전환 | ✅ PASS | §1~§8 전역. v3.1의 11개 surgical patch에 더해, 섹션 헤더 30+개, 인라인 레이블 패턴(Recap, Trench tip, Answer, Wrong shortcut 등), 블록 레이블(Practice Lens/Brief, Failure Mode 등), 설명문 내 영어 산문을 한국어 중심으로 전환. |
| 2 | 전문용어 `한글(English)` 병기 | ✅ PASS | 첫 등장 시 병기 완료: 중첩 원리(superposition), 용량 한계(capacity limitation), 시간 의존적(time-dependent), 비결합 농도(unbound concentration), 질량 작용 등가 삼각형(Mass Action Equivalence Triangle), 포화성 재흡수(saturable reabsorption), 억제제 강도(inhibitor strength), 등효능선(isobologram) 등. |
| 3 | 과학적 내용 보존 | ✅ PASS | 수치, 임상 anchor, 정량값, parameter symbol, source label 전부 v3.1과 동일. 새 과학적 주장·수치·예시·reference 추가 없음. |
| 4 | 수식 보존 | ✅ PASS | 모든 MathJax 수식, Eq. 번호, 파라미터 symbol 변경 없음. |
| 5 | Page tag 보존 | ✅ PASS | 모든 source page tag 변경 없음. 새 page tag 추가 없음. |
| 6 | Figure marker 보존 | ✅ PASS | 모든 marker 위치·내용 v3.1과 동일. Splice Verification Table B8 변경 없음. |
| 7 | Source-boundary 보존 | ✅ PASS | 모든 epistemic label 보존. PART B 전부 보존. 새 FDA·EMA·CPIC·NDA threshold 추가 없음. |
| 8 | HTML-readiness 보존 | ✅ PASS | PART B 전체 변경 없음. 모든 HTML compiler marker 보존. Phase 5 HTML compile 즉시 진입 가능. |

**최종 판정 (v3.2): 8/8 PASS — PART A 학습자 본문의 영어 산문이 전면 한국어화되었으며, 전문용어는 한글-영어 병기 형식으로 유지된다. v3.1의 모든 과학적 무결성·HTML-readiness·source boundary가 보존되었다. Phase 5 HTML compile go.**

---

*v3.2 file generated by Korean-Dominant Readability Patch editor. Source: 08_html_compile_input_master_v3.1.md → 08_html_compile_input_master_v3.2.md. v3.2 patches applied as comprehensive Korean prose conversion. No new scientific claims, page tags, numerical anchors, figure decisions, equations, or external references were added. Body integrity: v3.1의 모든 기존 수치·수식·source label·page tag·figure marker 100% 보존.*

| Certificate | Status | Basis |
|---|---|---|
| Korean-Dominant Readability Certificate | PASS | General learner-facing English prose converted to Korean where possible; career-critical terms retained as Korean-English paired expressions. |
| Scientific Preservation Certificate | PASS | No scientific content, equation, number, example, page tag, or source label changed. |
| Marker Integrity Certificate | PASS | All figure markers, compiler markers, anchors, and section/card structures preserved. |
| HTML-Readiness Certificate | PASS | Phase 5 compatibility preserved; no HTML/Mermaid/SVG generated. |

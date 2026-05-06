# 07_HTML Compile Input Master

## Phase 4D Certification

| Certificate | Status | Basis |
|---|---|---|
| Learner-Standalone Certificate | PASS | PART A contains the learner navigation aid, curation map, locked concept cards, confusion pairs, self-test, and meta-frame; compiler/audit/process material is isolated in PART B. |
| Zero-Omission Certificate | PASS | Scope concepts M1–M10, Audit MUST_FIX/SHOULD_FIX items, Phase 4C KEEP markers, and adopted Crucible logic are present, repaired in Content Lock v2, or justifiably omitted. |
| Mastery-Uplift Certificate | PASS | Eight bounded augmentation notes were inserted adjacent to MUST concepts and labeled by epistemic status. |
| Source-Boundary Certificate | PASS | No augmentation adds new numerical values, new named examples, new page tags, or unsupported textbook claims; expert interpretations are labeled EXPERT_INFERENCE. |
| HTML-Readiness Certificate | PASS | PART B includes Phase 5 rendering rules, figure/page-tag rules, splice verification, audit/crucible guardrails, and forbidden-restoration rules. |

## Assembly Mode

PATCH MODE — `07_Content Lock v2.1` is a figure-marker patch/insertion map, so the learner-facing body was constructed from the learner portion of `07_Content Lock v2` with the seven approved Phase 4C markers spliced at exact anchors.

## Input Manifest

| File | Role | Authority level | Used for | Notes |
|---|---|---|---|---|
| 07_scope_lock(5).md | Scope Lock | A0 | scope boundary | Defines source range, learner, chapter role, hard boundaries, and required conceptual functions. |
| 07_G_치료역·항정상태 다중투여·축적(6).pdf | Original textbook PDF — Gabrielsson & Weiner | A1 | PDF verification source | Used to verify constant-rate infusion, multiple dosing, flip-flop, PK11, and PK13 page/source anchors. |
| 07_T_..._01(6).pdf | Original textbook PDF — Rowland & Tozer Ch.9 + Appendix | A1 | PDF verification source | Used to verify therapeutic window/utility and accumulation appendix scope. |
| 07_T_..._02(6).pdf | Original textbook PDF — Rowland & Tozer Ch.10 | A1 | PDF verification source | Used to verify constant-rate input, plateau, bolus+infusion, post-infusion, response clocks. |
| 07_T_..._03(6).pdf | Original textbook PDF — Rowland & Tozer Ch.11 | A1 | PDF verification source | Used to verify multiple-dose regimens, accumulation, TW algorithm, daptomycin figure/table anchors. |
| 07_Audit_Report_v1(4).md | Audit Report v1 | A2 | audit guardrail | Controls factual corrections and regression prevention; all MUST_FIX/SHOULD_FIX items checked. |
| 07_Content Lock v2(4).md | Content Lock v2 | A3 | canonical body | Primary locked scientific body before figure-marker insertion; learner body extracted from curation map through §8. |
| 07_Content Lock v2.1(1).md | Figure Marker Patch / Phase 4C | A4 | figure insertion source | PATCH MODE strategy table, figure briefs, and insertion map. |
| 07_Crucible_Report_v1(1).md | Crucible Report v1 | A5 | crucible guardrail | Used only to preserve adopted Grade A logic and bounded insight; not used as raw prose source. |
| 붙여넣은 마크다운(2)(56).md | Step 2 HTML Compiler Prompt / Prompt 5 | A7 | compiler instruction | Controls rendering, marker-to-component mapping, source page tags, navigation, responsive/print behavior, and prohibitions. |
| 07_step1_draft_v0(3).md | Step 1 Draft v0 | A6 | deprecated source | Used only for regression checking; not copied into learner body except through locked Content Lock/Micro-Patch gates. |
| S07_phase1_patch memo(2).md | Phase 1 Patch Memo | A6 / locked reference | deprecated/locked reference | Used only to confirm early known issues were resolved by Audit/Content Lock. |
| 07_Content Lock v1(8).md | Content Lock v1 | locked reference | locked reference | Used only for continuity/compression reference; not learner-body source. |
| 붙여넣은 텍스트 (1)(85).txt | Phase 4D assembler prompt | instruction | assembly instruction | Defines this master-file generation contract; output filename adapted from 05 to 07 per user request. |

## PART A — Learner-Facing Complete Handout

## Learner Navigation Aid

**How to use this handout**: 먼저 Curation Map에서 M1–M10의 결정자 구조를 훑고, §2의 concept cards를 순서대로 읽은 뒤, §5 confusion pairs와 §7 self-test로 오개념을 제거한다. Figure pointer는 교과서 원그림을 복제하지 않으므로, 표시된 source figure를 원문 PDF에서 직접 확인하는 학습 신호로 사용한다.

**Learning route**: M1–M2에서 `level`과 `time`을 분리하고, M3–M4에서 `accumulation`, `fluctuation`, `average concentration`, `average amount`를 분리한다. M5–M6에서 input/response 해석의 예외를 잠근 뒤, M7–M8에서 loading, maintenance, therapeutic-window design으로 조립한다.

**Before you start**: `CL`, `t1/2`, `τ/t1/2`, `Cav,ss`, `Aav,ss`, therapeutic window가 서로 다른 질문에 답한다는 점을 기억한다.  
**After you finish**: §7 Q8–Q12와 Boss Dilemma를 풀면서 “어떤 식이 어떤 조건에서만 유효한가”를 설명할 수 있어야 한다.

---

## Updated Curation Map (MUST / CONTEXT)

### MUST — 10분 handout에 반드시 남길 개념

| ID | 개념 | 핵심 잠금 문장 | 핵심 수식 / anchor | Source tag |
|---|---|---|---|---|
| M1 | 정속 주입 plateau 농도 | 항정상태 농도 수준은 `t1/2`가 아니라 `CL`(← 단위 시간당 제거되는 용적)이 정한다. | $C_{ss}=R_{in}/CL$ | [G p.23; R&T p.288] |
| M2 | plateau 도달 시간 | 목표 plateau 수준이 높든 낮든 접근 시간표는 half-life의 함수다. | $C(t)=C_{ss}(1-e^{-Kt})$; 1, 2, 3, 3–4 half-lives ≈ 50%, 75%, 87.5%, ≈90% | [G pp.22–23; R&T pp.290–292] |
| M3 | 다중투여 accumulation factor | 축적 정도는 dose가 아니라 $\tau/t_{1/2}$가 정한다. | $R_{ac}=1/(1-e^{-K\tau})=1/(1-2^{-\tau/t_{1/2}})$ | [G pp.43–45; R&T pp.322–326; R&T pp.795–797] |
| M4 | 평균 plateau: concentration vs amount 분리 | `Cav,ss`와 `Aav,ss`를 등치하지 말라. 농도는 `CL`, amount는 `MRT`를 거쳐 표현된다. | $C_{av,ss}=F\text{Dose}/(CL\tau)$; $A_{av,ss}=1.44F\text{Dose}t_{1/2}/\tau$; 1-compartment에서만 $C_{av,ss}=A_{av,ss}/V$ | [G p.45; R&T p.324; R&T p.337] |
| M5 | Flip-flop | terminal slope가 elimination이 아니라 absorption을 말할 수 있다. | $K_a<K$이면 terminal slope ≈ $K_a$ | [G pp.45–46; R&T pp.332–334, 337–338] |
| M6 | Therapeutic Window | TW는 “좋은 농도 범위”가 아니라 benefit과 harm의 balance를 농도 축 위에 투영한 의사결정 구간이다. | therapeutic window(← benefit–harm balance의 농도 구간)와 therapeutic concentration range 구별; TI는 전임상 ratio와 임상 exposure sensitivity가 다름 | [R&T pp.267–281] |
| M7 | Loading + maintenance | plateau를 기다리지 않고 목표 근처에서 시작하려면 loading dose가 필요하고, 유지에는 average input rate가 필요하다. | $D_M=D_L(1-e^{-K\tau})$; $D_L=R_{ac}D_M$; bolus+infusion anchor | [R&T pp.293–295; R&T pp.326–329; G pp.537–539] |
| M8 | TW-driven dosage design | `Cupper`, `Clower`, `t1/2`, `V`, `F`가 있으면 interval과 dose의 상한을 계산할 수 있다. | $\tau_{max}=1.44t_{1/2}\ln(C_{upper}/C_{lower})$; $D_{M,max}=(V/F)(C_{upper}-C_{lower})$ | [R&T pp.334–337] |
| M9 | PD-driven plateau | effect plateau는 drug PK plateau보다 늦을 수 있다. 무엇의 half-life인지 먼저 물어야 한다. | atorvastatin: PK $t_{1/2}=14$ h, PD plateau 3–4 weeks; erythropoietin: PK $t_{1/2}=9$ h, hematocrit plateau ≈70 days | [R&T pp.341–345] |
| M10 | Dose fractionation toxicity | 같은 daily dose라도 fractionation이 recovery time을 바꾸면 toxicity가 달라진다. | Daptomycin Study A: 75 mg/kg q24h vs 25 mg/kg q8h, CPK 991 vs 3996 U/L | [R&T pp.351–353] |

### CONTEXT — 유지하되 1–2문장 이상 확장하지 않을 항목

| ID | Context item | Lock decision | Source tag |
|---|---|---|---|
| C1 | Steady state vs thermodynamic equilibrium | 용어를 엄밀히 분리하되 독립 카드로 확장하지 않음. | [G p.25] |
| C2 | Input function taxonomy | bolus, zero-order, first-order, multiple input을 “입력 함수가 달라지면 concentration-time profile이 달라진다” 수준으로만 유지. | [G p.43] |
| C3 | Multiple absorption sites | multiple peaks가 곧 enterohepatic recirculation을 의미하지 않는다는 주의만 유지. | [G p.46] |
| C4 | PK11 | PK clock = PD clock의 단순 anchor로만 사용. | [G pp.528–531] |
| C5 | PK13 | bolus+infusion IC coding anchor로 사용. | [G pp.537–539] |
| C6 | Constant-rate devices | infusion 원리 확장 예시로만 유지. | [R&T pp.284–286] |
| C7 | Post-infusion decline | infusion 중단 후 concentration은 half-life에 따라 감소하되, extravascular continued input은 예외가 될 수 있음. | [R&T p.291] |
| C8 | Clobazam single-dose AUC | single-dose AUC로 plateau average를 예측할 수 있다는 1문장 anchor. | [R&T p.336] |
| C9 | Modified release | intentional flip-flop의 임상 활용으로 morphine MR, leuprolide depot만 짧게 유지. | [R&T pp.337–338] |
| C10 | Regimen evaluation | fluctuation, relative bioavailability, renal clearance는 evaluation context로만 유지. | [R&T pp.339–341] |
| C11 | DDI patterns | ER 중심 4패턴만 유지; protein binding 단독 논리 금지. | [R&T pp.309–310; R&T pp.350–351] |
| C12 | Study problems | 본문에는 통합하지 않음; §7에서 가상/응용 문항으로만 사용 가능. | [R&T pp.353–358] |

---

# §1 — Session Header & Roadmap

<!-- MASTER LENS -->
## 1. Master Lens

이 세션의 핵심은 **항정상태를 하나의 숫자가 아니라 세 개의 독립 질문으로 분해하는 능력**이다.

<!-- ANNOTATION -->
항정상태(steady state)(← 입력률과 제거률이 같아진 상태)는 “도달했는가/얼마인가/얼마나 출렁이는가”를 따로 물어야 한다.

1. **언제 도달하는가?** → $t_{1/2}$가 정한다.
2. **평균 수준은 어디인가?** → $CL$과 평균 입력속도가 정한다.
3. **얼마나 출렁이는가?** → $\tau/t_{1/2}$가 정한다.

R&T Fig. 11-3의 메시지는 이 분리를 가장 잘 보여준다. 같은 average dosing rate라면 average amount의 plateau 접근 시간 경로는 같다. 그러나 dosing interval이 길수록 fluctuation은 커진다 [R&T p.325]. 이 분리를 이해하면 `SS=1`, `ADDL/II`, loading dose, maintenance dose, therapeutic window 기반 regimen design을 같은 구조로 읽을 수 있다.

<!-- ANCHOR -->

<!-- FIGURE_SCHEMATIC -->
Title: 항정상태를 지배하는 세 질문: timing × level × amplitude
Mode: N
Visual objective: 학습자가 5초 안에 “도달 시간, 평균 수준, fluctuation은 서로 다른 지배자를 가진다”를 볼 수 있어야 한다.
Core message: 항정상태는 하나의 숫자가 아니라 `언제 도달하는가`, `어디에 머무는가`, `얼마나 출렁이는가`의 세 질문으로 분해된다.
Elements to include: 중앙 노드 `Steady-state regimen interpretation`; branch 1 `Timing → t1/2 → 3–4 half-lives ≈ 90%`; branch 2 `Average level → CL + average input rate → Css/Cav,ss`; branch 3 `Amplitude/fluctuation → τ/t1/2 → Rac and peak–trough swing`; 하단 warning `Do not collapse these into one steady-state idea`.
Elements to exclude: 개별 약물 수치; NONMEM code; 교과서 figure의 곡선 재현.
Suggested rendering: Mermaid
Caption: 항정상태 해석의 핵심은 timing, level, amplitude를 서로 다른 parameter 질문으로 분리하는 것이다.
Alt text: Steady-state interpretation branches into timing controlled by half-life, average level controlled by clearance and input rate, and fluctuation controlled by dosing interval relative to half-life.
Source relation: Newly designed
<!-- /FIGURE_SCHEMATIC -->

## 2. Roadmap

- **M1–M2**: 정속 주입에서 `CL`은 plateau level, `t1/2`는 approach time을 결정한다.
- **M3–M4**: 다중투여에서 accumulation과 average plateau를 계산한다. 이때 `amount`와 `concentration`의 차원을 분리해야 한다.
- **M5**: absorption이 느리면 terminal slope가 elimination을 말하지 않는다.
- **M6**: therapeutic window는 PK 식의 결과가 아니라 clinical utility의 제약조건이다.
- **M7–M8**: loading/maintenance와 TW-driven algorithm은 위 분리를 실제 dosing regimen으로 변환한다.

<!-- RECAP -->
**Session Lock**: 항정상태는 “시간=t½, 수준=CL, 진폭=τ/t½”의 세 축으로 잠근다. 이 세 축을 섞는 순간 NONMEM steady-state coding, TDM adjustment, loading dose rationale, therapeutic-window design이 동시에 흐려진다.

---

# §2 — Concept Anatomy Cards

## §2-M1. 정속 주입 항정상태 농도: $C_{ss}=R_{in}/CL$

<!-- MASTER LENS -->
### Big Idea

정속 주입에서 plateau concentration은 **얼마나 빨리 없어지는가(CL)**와 **얼마나 빨리 넣는가($R_{in}$)**의 균형이다. Volume은 초기 상승 곡선의 속도를 바꾸지만, plateau 농도의 높이를 직접 결정하지 않는다 [G p.23; R&T p.288].

### Source-locked equations

$$\frac{dC}{dt}=\frac{R_{in}}{V}-\frac{CL}{V}C$$

$$C(t)=\frac{R_{in}}{CL}\left(1-e^{-(CL/V)t}\right)$$

$$C_{ss}=\frac{R_{in}}{CL}$$

### What to remember

Maintenance dosing을 시작할 때 먼저 묻는 것은 “target concentration × clearance”이다. 목표 $C_{ss}$를 맞추려면 $R_{in}$을 조정하고, 환자의 $CL$ 변화를 반영해야 한다. $V$는 loading이나 onset의 문제로 이동한다.

<!-- TRENCH -->
**Trench-Level Tip**: infusion 중 관찰 농도가 기대 plateau보다 낮다고 해서 곧바로 CL 증가로 해석하지 않는다. 먼저 actual input rate, line interruption, sampling time, infusion stop/start 기록을 확인한다. 교과서가 보증하는 것은 $C_{ss}=R_{in}/CL$ 구조이지, 특정 현장 오류의 빈도 숫자가 아니다.

<!-- RECAP -->
**Recap**: steady-state concentration의 지배자는 clearance다. Half-life는 plateau까지 가는 시간의 지배자다.

---

> **Practice Lens — [EXPERT_INFERENCE]**  
> 정속 주입 해석에서는 먼저 “입력률이 정확했는가?”와 “clearance 가정이 맞는가?”를 분리한다. 관찰 농도가 plateau와 다를 때 시간상 아직 approach 중인지, 실제 input이 달랐는지, CL이 달랐는지를 같은 문장 안에서 섞지 않는 것이 숙련자의 기본 점검 순서다.

## §2-M2. 항정상태 도달 시간: 3–4 $t_{1/2}$ 규칙

<!-- MASTER LENS -->
### Big Idea

정속 주입이든 다중투여든 plateau 접근 속도는 **elimination half-life**가 정한다. 즉, 목표 plateau가 높든 낮든 “몇 %까지 접근했는가”의 시간표는 half-life로 움직인다. 1 half-life 후 50%, 2 half-lives 후 75%, 3 half-lives 후 87.5%, 3–4 half-lives 후 약 90%에 도달한다 [G p.22; R&T pp.290–292].

### Source-locked equation

$$C(t)=C_{ss}(1-e^{-Kt})$$

도달률은 $1-e^{-Kt}$이며, $K=\ln2/t_{1/2}$이다. 90% 도달 시간은 $t=\ln(10)/K\approx3.32t_{1/2}$이다 [R&T p.291].

### Practical interpretation

`t1/2`가 2.5시간인 eptifibatide는 plateau에 비교적 빨리 접근하고, `t1/2`가 5분인 t-PA는 약 17분이면 90% 수준에 접근한다 [R&T pp.288–293]. 반대로 phenobarbital처럼 $t_{1/2}=4$ days이면 plateau 접근 자체가 느리다 [R&T pp.324–325].

<!-- ANCHOR -->
**Bridge to NONMEM**: steady-state assumption은 “평균적으로 충분히 오래 투여했다”는 시간 조건이다. `SS=1`을 쓰기 전에 실제 투여 이력이 최소 3–4 half-lives 이상인지 먼저 확인한다.

<!-- RECAP -->
**Recap**: target level이 바뀌어도 approach fraction의 시간표는 half-life로 움직인다.

---

> **Failure Mode — [EXPERT_INFERENCE]**  
> 3–4 half-lives 규칙은 “목표가 맞다”는 보증이 아니라 “정해진 목표 plateau의 몇 %에 접근했는가”를 말한다. 잘못 잡은 목표 농도도 half-life 시간표를 따라 성실하게 도달하므로, target 설정과 approach-time 판단을 분리해야 한다.

## §2-M3. Apex Concept — 다중투여 축적인자 $R_{ac}=1/(1-e^{-K\tau})$

<!-- MASTER LENS -->
### Big Idea

다중투여 accumulation은 새 dose가 들어올 때 이전 dose의 잔여량이 얼마나 남아 있는지의 문제다.

<!-- ANNOTATION -->
accumulation factor(← 단회 투여 대비 plateau 증가비)는 농도값 자체가 아니라 반복 투여가 만든 배율이다.

1차 선형계에서 이전 dose의 잔여 비율은 $e^{-K\tau}$이고, 무한 반복하면 등비수열 합으로 닫힌 형태가 된다 [G pp.43–45; R&T pp.795–797].

### Source-locked equation

$$R_{ac}=\frac{1}{1-e^{-K\tau}}=\frac{1}{1-2^{-\tau/t_{1/2}}}$$

이 식은 dose가 들어가지 않는다. 축적 정도는 `dose size`가 아니라 **dose interval relative to half-life**가 정한다 [G pp.44–45; R&T pp.325–326].

<!-- ANCHOR -->
### Three-dominator lock

- **Timing**: plateau 접근 시간 = $t_{1/2}$.
- **Level**: average plateau concentration = $CL$과 average input rate.
- **Amplitude**: peak-trough fluctuation과 accumulation factor = $\tau/t_{1/2}$.

R&T의 200 mg/day 예시는 average dosing rate가 같으면 average amount의 접근 시간은 같다는 점을 보여준다. 달라지는 것은 dosing interval이 길어질수록 커지는 fluctuation이다 [R&T p.325].

### Phenobarbital label lock

Phenobarbital 예시는 “slow half-life + short interval”이 큰 accumulation과 느린 plateau approach를 만든다는 좋은 anchor다. 단, 라벨을 분리해야 한다. R&T는 $t_{1/2}=4$ days, 100 mg q24h 사례에서 본문상 accumulation index 5.8을 언급하지만, Eq. 11-3/11-10의 peak/trough accumulation index로 계산하면 $A_{max,ss}/Dose=630/100\approx6.3$이다. 5.8은 $A_{av,ss}/Dose\approx5.76$에 해당하는 average accumulation ratio로 이해해야 한다 [R&T pp.324–326].

<!-- TRENCH -->
**Trench-Level Tip — Phantom Plateau Bias**: 투여 시작 직후 자료에 `SS=1`을 부적절하게 적용하면 observed rising limb를 이미 plateau인 것처럼 강제로 설명하게 된다. 이때 CL, bioavailability, interindividual variability 추정이 연쇄적으로 왜곡될 수 있다. 수치적 손상률이나 제출 실패 같은 외부 단정은 본문에서 삭제한다.

<!-- RECAP -->
**Recap**: accumulation factor는 dose 독립, $\tau/t_{1/2}$ 의존이다. Dose를 키우면 level이 올라가지만, accumulation ratio 자체가 바뀌지는 않는다.

---

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.325, Fig. 11-3
Why this matters: 같은 average dose rate가 같은 average amount plateau approach를 만들지만, dosing frequency는 fluctuation을 바꾼다는 점을 직접 보여준다. M3의 “dose가 아니라 τ/t1/2가 축적과 fluctuation을 지배한다”는 해석의 핵심 시각 anchor다.
When to look: §2-M3의 `Three-dominator lock`을 읽은 직후.
Learner instruction: 두 곡선의 average approach가 같은지 먼저 보고, 그 다음 peak–trough swing이 어떻게 달라지는지 보라. “평균 수준”과 “출렁임”을 같은 말로 읽지 말라.
<!-- /FIGURE_POINTER -->

> **Mastery Note — [CRUCIBLE_DERIVED]**  
> $R_{ac}$는 노출의 절대값이 아니라 반복투여가 만든 배율이다. 선형 PK에서는 dose를 키우면 곡선 전체가 커지지만, 같은 $	au/t_{1/2}$에서 “배율” 자체는 그대로라는 점이 이 카드의 핵심이다.

## §2-M4. 항정상태 평균농도와 평균 amount: $C_{av,ss}$ vs $A_{av,ss}$

<!-- MASTER LENS -->
### Big Idea

이 세션에서 가장 위험한 오류는 **average concentration**과 **average amount**를 같은 식으로 쓰는 것이다.

<!-- ANNOTATION -->
average concentration(← 용적당 평균 농도)과 average amount(← 체내 평균 약물량)는 단위부터 다르다.

R&T는 두 식을 분리한다 [R&T p.324; R&T p.337].

### Source-locked equations

$$C_{av,ss}=\frac{AUC_{0-\tau,ss}}{\tau}=\frac{F\cdot Dose}{CL\cdot\tau}$$

$$A_{av,ss}=\frac{1.44\cdot F\cdot Dose\cdot t_{1/2}}{\tau}$$

첫 식의 단위는 concentration이고, 두 번째 식의 단위는 amount다. 1-compartment에서 $MRT=V/CL=1.44t_{1/2}$가 성립할 때만 $C_{av,ss}=A_{av,ss}/V$로 연결된다 [R&T p.289; R&T p.324]. Multi-compartment에서는 amount-to-concentration 변환이 모델 구조에 의존한다.

<!-- ANCHOR -->
### Why this matters

$C_{av,ss}$는 clinical target, TDM interpretation, exposure-response 분석의 언어다. 반면 $A_{av,ss}$는 body burden과 residence time의 언어다. 따라서 둘을 섞으면 “농도 목표”와 “체내 amount”의 차원이 무너진다.

### Example anchors

- Table 11-1의 200 mg q24h 예시는 single-dose profile을 superposition(← 단회 투여 곡선을 시간 이동해 더함)하여 repeated-dose profile을 예측할 수 있음을 보여준다 [R&T pp.320–321].
- Clobazam 예시는 single-dose AUC와 dosing interval로 average plateau concentration을 예측하는 논리를 보강한다 [R&T p.336].
- Amoxicillin, naproxen, piroxicam 예시는 half-life와 dosing interval이 fluctuation과 accumulation을 어떻게 바꾸는지 비교한다 [R&T pp.330–332].

<!-- RECAP -->
**Recap**: $C_{av,ss}$는 $CL$ 기반 농도식, $A_{av,ss}$는 $MRT$ 기반 amount식이다. 두 식은 차원이 다르다.

---

<!-- FIGURE_SCHEMATIC -->
Title: Cav,ss와 Aav,ss의 차원 방화벽
Mode: N
Visual objective: 학습자가 농도식과 amount식을 같은 줄에 등치하면 안 된다는 것을 즉시 볼 수 있어야 한다.
Core message: Cav,ss는 concentration이고 Aav,ss는 amount이며, 1-compartment 조건에서 V를 거칠 때만 서로 연결된다.
Elements to include: 좌측 box `Cav,ss = average concentration`, unit `concentration`, equation `F·Dose/(CL·τ)`; 우측 box `Aav,ss = average amount`, unit `amount`, equation `1.44·F·Dose·t1/2/τ`; 중앙 firewall label `Do not equate directly`; 조건부 bridge `Only when 1-compartment and V known: Cav,ss = Aav,ss/V`.
Elements to exclude: MRT의 추가 도출; locked sentence를 넘어서는 multi-compartment 예외; 추가 수치 예시.
Suggested rendering: CSS-card
Caption: 평균농도와 평균 amount는 같은 steady-state idea에서 나오지만 차원이 다르므로 직접 등치하면 안 된다.
Alt text: A comparison card separates average concentration from average amount, with a firewall between them and a conditional bridge through volume only in a one-compartment setting.
Source relation: Newly designed
<!-- /FIGURE_SCHEMATIC -->

> **Failure Mode — [AUDIT_DERIVED]**  
> $A_{av,ss}$ 식을 $C_{av,ss}$ 식으로 잘못 옮기는 오류는 단순 표기 문제가 아니라 단위 방화벽 붕괴다. 보고서나 슬라이드에서 이 줄이 무너지면 TDM target, exposure-response target, body burden 해석이 한꺼번에 섞인다.

## §2-M5. Flip-flop 동태: $K_a<K$일 때 terminal slope의 정체

<!-- MASTER LENS -->
### Big Idea

Extravascular dosing에서 terminal slope는 항상 elimination을 의미하지 않는다.

<!-- ANNOTATION -->
Flip-flop(← 흡수가 제거보다 느린 상태)에서는 말단 기울기의 해석 주체가 elimination에서 absorption으로 바뀐다.

흡수가 더 느리면 terminal phase는 absorption-limited phase가 된다 [G pp.45–46].

### Source-locked relation

$$K_a<K \Rightarrow \text{terminal slope}\approx K_a$$

일반적인 경우는 $K_a>K$이고 terminal slope가 $K$를 반영한다. Flip-flop에서는 terminal half-life가 길어 보이지만, 그것은 drug elimination이 느리다는 뜻이 아니라 absorption input이 오래 지속된다는 뜻일 수 있다.

<!-- ANCHOR -->
### Clinical asymmetry

Modified-release products와 depot formulations는 의도적으로 input을 느리게 만들어 fluctuation을 줄인다. 즉, formulation이 absorption/input을 지배하면 terminal slope와 dosing interval의 임상 의미가 달라진다. Morphine MR은 짧은 elimination half-life에도 q24h regimen을 가능하게 하고, leuprolide depot은 짧은 half-life에도 월 1회 투여를 가능하게 한다 [R&T pp.337–338]. 이것은 “나쁜 flip-flop”이 아니라 **의도된 input control**이다.

<!-- RECAP -->
**Recap**: terminal slope를 곧바로 elimination으로 번역하지 말라. 먼저 route, formulation, absorption duration을 확인한다.

---

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.45, Fig. 2.29
Why this matters: Flip-flop은 문장으로는 “흡수가 느리다”로 지나가기 쉽지만, 실제 오류는 terminal slope를 elimination slope로 잘못 읽는 데서 발생한다. 그림은 ordinary case와 flip-flop case의 terminal phase 정체를 분리해준다.
When to look: §2-M5의 `Clinical asymmetry`를 읽기 전.
Learner instruction: terminal tail이 더 길어졌을 때 먼저 `Ka < K` 가능성을 확인하라. 긴 terminal half-life를 곧바로 느린 elimination으로 번역하지 말라.
<!-- /FIGURE_POINTER -->

> **Mastery Note — [TEXTBOOK_DERIVED]**  
> Terminal phase는 항상 elimination phase라는 이름을 붙이기 전에 route와 input function을 먼저 확인해야 한다. Flip-flop은 “느린 elimination”이 아니라 “느린 absorption이 terminal slope를 지배하는 상황”으로 읽어야 한다.

## §2-M6. Therapeutic Window — PK 식을 임상 의사결정으로 바꾸는 제약조건

<!-- MASTER LENS -->
### Big Idea

Therapeutic window는 단순한 농도 구간이 아니라, benefit과 harm을 동시에 고려해 regimen을 정하는 clinical utility frame이다. R&T는 dosage regimen을 dose, dosage form, route, interval, duration으로 구성하고, 이를 systemic exposure와 beneficial/adverse response에 연결한다 [R&T pp.267–268].

### Term lock

- **Therapeutic concentration range**: 임상 경험상 효과가 있고 위해가 받아들여질 만한 농도 범위 [R&T p.272].
- **Therapeutic window**: utility curve threshold 이상으로 정의되는 더 의사결정적인 구간이다. 즉, 두 범위는 겹칠 수 있지만 같은 개념은 아니다 [R&T pp.273–274].
- **Therapeutic index**: 전임상에서는 $TD_{50}/ED_{50}$ ratio로, 임상에서는 exposure 변화에 대한 개별 환자의 limiting effect sensitivity로 이해해야 한다 [R&T p.278].

### Utility formalization lock

$U(C)=\sum w_iP_i(C)$ 같은 표현은 **교과서 원수식이 아니라 교육적 formalization**이다.

<!-- ANNOTATION -->
formalization(← 개념을 계산식 형태로 표현)은 출처 식과 구별해 읽어야 한다.

R&T Fig. 9-4의 가중치 예시는 저자 판단에 따른 illustrative weighting으로만 써야 하며, 표준 regulatory weight처럼 쓰면 안 된다 [R&T p.273].

### PK/PD and response clocks

Plasma concentration이 항상 effect를 즉시 설명하지 않는다. Atorvastatin은 PK half-life가 약 14시간이지만 cholesterol response plateau는 3–4주가 걸릴 수 있고, erythropoietin은 PK half-life가 약 9시간이어도 hematocrit plateau는 약 70일에 걸친다 [R&T pp.343–344]. 여기서 질문은 “drug의 half-life인가, turnover system의 half-life인가”이다.

### Antimicrobial anchor

Antimicrobial regimen은 PK index가 다르면 dosing logic도 달라진다. β-lactam 계열처럼 time above MIC가 중요한 경우 prolonged/continuous infusion이 합리적일 수 있고, aminoglycoside처럼 peak/MIC와 toxicity window가 중요한 경우 once-daily fractionation이 합리적일 수 있다 [R&T pp.307–312; R&T pp.347–348]. R&T Fig. 11-20의 AUC/MIC >101 예시는 resistance avoidance 논리의 정량 anchor다 [R&T p.348].

<!-- TRENCH -->
**Trench-Level Tip — DDI variable lock**: protein binding만으로 DDI 민감도를 설명하지 않는다. R&T의 low/high extraction ratio 예시는 plateau 변화의 핵심 변수가 hepatic extraction ratio임을 보여준다 [R&T pp.309–310; R&T pp.350–351].

<!-- RECAP -->
**Recap**: TW는 PK 식의 마지막 줄이 아니라 regimen design의 제약조건이다. 목표농도, fluctuation, PD delay, toxicity mechanism을 동시에 제한한다.

---

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.272, Fig. 9-3
Why this matters: Therapeutic window를 단순 농도범위가 아니라 effectiveness, adverse response, utility의 balance로 보게 하는 원문 핵심 그림이다. Content Lock v2의 utility formalization lock을 원문 곡선 직관으로 되돌려준다.
When to look: §2-M6의 `Term lock`과 `Utility formalization lock` 사이.
Learner instruction: effectiveness curve와 utility curve를 같은 것으로 보지 말고, utility가 benefit과 harm을 함께 반영한다는 점을 확인하라. TW는 농도축 위에 그려진 decision zone이다.
<!-- /FIGURE_POINTER -->

> **Practice Lens — [CRUCIBLE_DERIVED]**  
> Therapeutic window는 계산이 끝난 뒤 붙이는 장식이 아니라 regimen이 통과해야 하는 제약조건이다. 숙련자는 먼저 benefit–harm balance가 허용하는 농도 영역을 정하고, 그 다음 PK 식이 그 영역을 유지할 수 있는지 묻는다.

## §2-M7. Loading Dose + Maintenance: 목표 즉시 도달과 유지의 분리

<!-- MASTER LENS -->
### Big Idea

Loading dose(← 초기에 목표에 빨리 올리는 용량)는 “기다리는 시간”을 줄이는 도구이고, maintenance dose(← 목표를 유지하는 반복 용량)는 “유지되는 평균 입력속도”를 맞추는 도구다. 둘은 목적이 다르다 [R&T pp.326–329].

### Source-locked equations

$$D_M=D_L(1-e^{-K\tau})$$

$$D_L=\frac{D_M}{1-e^{-K\tau}}=R_{ac}D_M$$

Doxycycline 예시는 $t_{1/2}=24$ h, $D_L=200$ mg, $D_M=100$ mg/day, $R_{ac}=2$라는 단순 anchor를 제공한다 [R&T p.327]. Sirolimus는 $t_{1/2}=2.5$ days, loading 6 mg, maintenance 2 mg/day의 임상 예시로, 이론식과 실제 tolerability 사이의 조정 필요성을 보여준다 [R&T pp.326–327].

### Bolus + infusion anchor

정속 주입에서 즉시 plateau 근처로 올리려면 bolus와 infusion을 결합할 수 있다. 먼저 bolus가 초기 농도 위치를 만들고, infusion이 이후 input rate를 유지한다. Gabrielsson PK13은 400 µg/kg bolus + 800 µg/kg over 26 min, therapeutic window 50–300 µg/L, $V_c=2.0$ L/kg, $CL=1.0$ L/min/kg, $CL_d=1.0$ L/min/kg, $V_t=5.0$ L/kg의 수치 anchor를 제공한다 [G pp.537–539].

### Daptomycin fractionation anchor

Daptomycin Study A의 같은 daily dose 비교는 **75 mg/kg q24h vs 25 mg/kg q8h**이다. 둘 다 75 mg/kg/day이지만 CPK는 991 vs 3996 U/L로 크게 달랐다 [R&T pp.351–353]. Study B에서는 같은 Cmax 58 µg/mL 조건에서도 AUC와 CPK가 달랐다. 이 예시는 Cmax 또는 AUC 하나만으로 toxicity를 설명하지 말고 recovery time/fractionation을 함께 보라는 anchor다.

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.352 Fig. 11-24 and p.353 Table 11-7
Why this matters: Daptomycin anchor는 본 세션에서 “same daily dose” 비교군을 잘못 잡으면 결론 전체가 뒤집히는 고위험 지점이다. Fig. 11-24와 Table 11-7을 함께 보아야 concentration profile, daily dose, CPK 결과가 분리된다.
When to look: §2-M7의 `Daptomycin fractionation anchor`를 읽은 직후.
Learner instruction: Study A에서 같은 daily dose 비교가 `75 mg/kg q24h` vs `25 mg/kg q8h`인지 확인하라. 그 다음 CPK 열을 보면서 fractionation/recovery time이 toxicity 해석에 왜 필요한지 확인하라.
<!-- /FIGURE_POINTER -->

<!-- RECAP -->
**Recap**: loading은 initial condition, maintenance는 long-run input rate, fractionation은 recovery time과 fluctuation을 바꾼다.

---

> **Practice Lens — [EXPERT_INFERENCE]**  
> Loading과 maintenance는 같은 “용량”이라는 단어를 쓰지만 데이터셋과 해석에서는 서로 다른 질문이다. Loading은 시작 위치를 정하고, maintenance는 반복 입력률을 정하므로 dose event와 steady-state assumption을 분리해 기록해야 한다.

## §2-M8. TW-Driven Dosage Design Algorithm

<!-- MASTER LENS -->
### Big Idea

Therapeutic window가 $C_{lower}$와 $C_{upper}$로 주어지고 PK parameter가 있으면, 최대 투여간격과 최대 maintenance dose를 계산할 수 있다 [R&T pp.334–337].

### Source-locked equations

$$C_{lower}=C_{upper}e^{-K\tau_{max}}$$

$$\tau_{max}=\frac{\ln(C_{upper}/C_{lower})}{K}=1.44t_{1/2}\ln\left(\frac{C_{upper}}{C_{lower}}\right)$$

$$D_{M,max}=\frac{V}{F}(C_{upper}-C_{lower})$$

$$C_{ss,av}=\frac{C_{upper}-C_{lower}}{\ln(C_{upper}/C_{lower})}$$

### Algorithm lock

1. $C_{lower}$, $C_{upper}$를 정한다.
2. $t_{1/2}$로 $\tau_{max}$를 계산한다.
3. $V/F$로 $D_{M,max}$를 계산한다.
4. 실제 제형 strength와 adherence를 고려해 practical $\tau$와 $D_M$을 선택한다.
5. 필요 시 $D_L$로 initial target에 접근한다.

<!-- TRENCH -->
**Trench-Level Tip**: 이 알고리즘은 linear PK, fixed interval, target concentration과 response의 충분한 연결을 전제한다. Single-dose therapy나 PD plateau가 turnover로 지배되는 약물에서는 그대로 적용하지 않는다 [R&T p.279; R&T pp.341–345].

<!-- RECAP -->
**Recap**: M8은 M1–M7을 dosing algorithm으로 묶는 끝점이다. 즉, `Cupper/Clower`는 interval, `V/F`는 dose size, `CL`은 average concentration을 각각 제약한다.

---

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.335, Fig. 11-10
Why this matters: M8의 식들은 각각 맞더라도, learner는 Cupper, Clower, τmax, DM, DL이 하나의 regimen design sequence라는 점을 놓칠 수 있다. 이 그림은 therapeutic window와 loading/maintenance profile을 같은 frame 안에 묶는다.
When to look: §2-M8의 `Algorithm lock`을 읽은 직후.
Learner instruction: 먼저 upper/lower bound가 투여간격을 어떻게 제한하는지 보고, 그 다음 maintenance dose와 loading dose가 profile 안에서 어떤 위치를 차지하는지 확인하라.
<!-- /FIGURE_POINTER -->

> **Practice Lens — [EXPERT_INFERENCE]**  
> TW-driven algorithm은 최종 처방 자동생성기가 아니라 선형 PK와 즉각적 concentration-response 가정이 통과되는지 확인하는 feasibility screen이다. 조건이 깨지면 interval이나 dose를 억지로 고르는 대신 모델 확장 또는 PD 시간척도 검토로 돌아가야 한다.

# §5 — Confusion Pair Dissection

## §5-쌍1. $C_{ss}$ vs $C_{av,ss}$ vs $A_{av,ss}$

<!-- CONFUSION -->
| 혼동 | 정확한 분리 | 왜 중요한가 |
|---|---|---|
| $C_{ss}$ | 정속 주입 plateau concentration: $R_{in}/CL$ | infusion maintenance target |
| $C_{av,ss}$ | 다중투여 interval 평균 concentration: $F\text{Dose}/(CL\tau)$ | TDM/exposure-response target |
| $A_{av,ss}$ | plateau 평균 amount: $1.44F\text{Dose}t_{1/2}/\tau$ | residence time/body burden |

**Critical Blow**: $1.44F\text{Dose}t_{1/2}/\tau$를 concentration 식으로 쓰면 단위가 틀린다. 1-compartment와 known $V$를 명시하지 않으면 amount-to-concentration 변환은 성립하지 않는다 [R&T p.324; R&T p.337].

---

## §5-쌍2. NONMEM `SS=1` vs `SS=2`

<!-- CONFUSION -->
| 항목 | `SS=1` | `SS=2` |
|---|---|---|
| 의미 | steady-state dose event | steady-state infusion/input condition |
| 위험 | 실제 accumulation phase를 plateau로 오인 | bolus/infusion initial condition을 잘못 설정 |
| 선행 질문 | 충분한 투여 이력이 있었는가? | input이 어떤 형태였는가? |

**Critical Blow**: steady-state flag는 “편의상 넣는 옵션”이 아니라 initial condition을 수학적으로 바꾸는 명령이다. 투여 이력이 plateau 조건을 만족하지 않으면 쓰지 않는다.

---

## §5-쌍3. Flip-flop vs ordinary extravascular decline

<!-- CONFUSION -->
| Ordinary | Flip-flop |
|---|---|
| $K_a>K$ | $K_a<K$ |
| terminal slope ≈ elimination | terminal slope ≈ absorption |
| terminal half-life가 drug elimination 정보를 줌 | terminal half-life가 formulation/input 정보를 줄 수 있음 |

**Critical Blow**: terminal slope만 보고 elimination half-life를 확정하지 않는다. route, formulation, absorption duration이 먼저다 [G pp.45–46].

---

## §5-쌍4. 도달 시간 vs 축적 정도 vs fluctuation

<!-- CONFUSION -->
| 질문 | 결정자 | 대표식 |
|---|---|---|
| plateau에 언제 도달하는가? | $t_{1/2}$ | $1-e^{-Kt}$ |
| 얼마나 축적되는가? | $\tau/t_{1/2}$ | $R_{ac}=1/(1-e^{-K\tau})$ |
| 평균 level은 어디인가? | $CL$과 average input | $C_{av,ss}=F\text{Dose}/(CL\tau)$ |
| peak-trough 진폭은? | $\tau/t_{1/2}$ | dosing interval이 길수록 커짐 |

**Critical Blow**: dose를 두 배로 하면 concentration level은 올라가지만, $R_{ac}$ 자체는 변하지 않는다.

---

## §5-쌍5. Therapeutic Window vs Therapeutic Index

<!-- CONFUSION -->
| 개념 | 정확한 의미 | 오해 |
|---|---|---|
| Therapeutic Window | utility threshold 이상인 concentration region | “경험적 치료농도범위”와 동의어로 사용 |
| Therapeutic Concentration Range | 임상 경험상 효과와 허용 가능한 위해를 만족하는 농도 범위 | TW와 항상 같은 수치라고 가정 |
| Therapeutic Index | 전임상 ratio 또는 임상 exposure sensitivity | high TI가 모든 환자의 안전을 보장한다고 해석 |

**Critical Blow**: wide therapeutic window와 high therapeutic index는 같은 문장이 아니다. 전자는 concentration bound, 후자는 exposure 변화에 대한 safety margin/sensitivity 문제다 [R&T pp.272–278].

---

## §5-쌍6. MRT vs half-life

<!-- CONFUSION -->
| 항목 | 의미 | 주의 |
|---|---|---|
| $t_{1/2}$ | amount/concentration이 절반이 되는 시간 | 1차 decline의 slope 기반 |
| MRT | molecule이 체내에 머무는 평균 시간 | moment-based: $AUMC/AUC$ |
| 1-compartment | $MRT=1/K=1.44t_{1/2}=V/CL$ | 단순식 가능 |
| multi-compartment | $MRT=AUMC_{0-\infty}/AUC_{0-\infty}$ | $V/CL$ 단순 치환 위험 |

**Critical Blow**: $1.44t_{1/2}$는 1차 선형 시스템의 시간척도일 뿐, 어떤 compartment의 concentration을 대표하는지는 모델 구조가 결정한다 [R&T p.289; R&T pp.299–304].

---

## §5-쌍7. Acquired Resistance vs Tolerance

<!-- CONFUSION -->
| 항목 | Acquired resistance | Tolerance |
|---|---|---|
| 본질 | 세포/미생물 population 또는 mutation 변화 | 환자/시스템의 PD adaptation |
| 시간 구조 | selection pressure와 population shift | receptor desensitization 또는 homeostatic feedback |
| 관리 논리 | exposure target, resistance window 회피 | drug holiday, modified release, rate-of-change control |

**Critical Blow**: 효과 감소가 보인다고 모두 tolerance가 아니다. 항균제에서는 resistance selection, nitrate/nicotine/nifedipine에서는 PD adaptation이 핵심일 수 있다 [R&T pp.346–348].

<!-- RECAP -->
**§5 Recap**: 위험한 혼동은 “수학식의 기호가 비슷해서”만 생기지 않는다. 더 자주 생기는 원인은 결정자가 다른 질문을 같은 질문으로 취급하는 것이다.

---

# §7 — Self-Test Module

## §7-Recall Layer

<!-- SELF-TEST -->
### Q1. 정속 주입에서 $C_{ss}$를 결정하는 parameter는 무엇인가?
**Answer**: $C_{ss}=R_{in}/CL$이므로 plateau 농도 수준은 clearance와 input rate가 정한다 [G p.23; R&T p.288].

### Q2. 90% plateau에 도달하는 데 필요한 시간은 대략 몇 half-lives인가?
**Answer**: 약 3.3 half-lives, 실무적으로 3–4 half-lives [G p.22; R&T p.291].

### Q3. 다중투여 accumulation factor에 dose가 들어가지 않는 이유는?
**Answer**: 같은 dose가 반복될 때 잔여분의 비율은 $e^{-K\tau}$이고, 반복합은 등비수열이므로 ratio는 $\tau/t_{1/2}$에만 의존한다 [G pp.44–45; R&T pp.795–797].

### Q4. $C_{av,ss}$와 $A_{av,ss}$의 차원은 각각 무엇인가?
**Answer**: $C_{av,ss}$는 concentration, $A_{av,ss}$는 amount다. $A_{av,ss}$를 concentration처럼 쓰면 차원 오류다 [R&T p.324; R&T p.337].

### Q5. Flip-flop에서 terminal slope는 무엇을 반영하는가?
**Answer**: $K_a<K$이면 terminal slope는 absorption rate를 반영한다 [G pp.45–46].

---

## §7-Application Layer

<!-- SELF-TEST -->
### Q6. 어떤 약물의 $t_{1/2}=8$ h이고 q24h 투여한다. 축적은 클까?
**Answer**: $\tau/t_{1/2}=3$이므로 $R_{ac}=1/(1-2^{-3})=1.14$ 정도로 크지 않다. q24h라도 half-life 대비 interval이 길면 accumulation은 작다.

### Q7. 같은 daily dose를 q24h에서 q8h로 바꾸면 무엇이 변하는가?
**Answer**: average input rate가 같으므로 $C_{av,ss}$는 원칙적으로 같지만, peak-trough fluctuation은 줄어든다. 단 toxicity가 recovery time/fractionation에 의존하면 결과가 달라질 수 있다 [R&T p.325; R&T pp.351–353].

### Q8. $C_{av,ss}=F\text{Dose}/(CL\tau)=1.44F\text{Dose}t_{1/2}/\tau$라고 쓴 문장을 교정하라.
**Answer**: 앞 식은 concentration, 뒤 식은 amount다. 정확히는 $C_{av,ss}=F\text{Dose}/(CL\tau)$이고, $A_{av,ss}=1.44F\text{Dose}t_{1/2}/\tau$이다. 1-compartment에서만 $C_{av,ss}=A_{av,ss}/V$이다.

### Q9. Phenobarbital 100 mg q24h, $t_{1/2}=4$ days에서 R&T의 5.8과 식의 6.3을 어떻게 설명할 것인가?
**Answer**: 5.8은 $A_{av,ss}/Dose\approx5.76$에 해당하는 average accumulation ratio이고, peak/trough accumulation index $R_{ac}$는 Eq. 11-10 기준 약 6.3이다. 둘을 같은 라벨로 쓰지 않는다 [R&T pp.324–326].

### Q10. Atorvastatin에서 PK plateau와 PD plateau가 다를 수 있는 이유는?
**Answer**: plasma concentration의 half-life와 cholesterol turnover response의 time scale이 다르기 때문이다. Atorvastatin은 $t_{1/2}\approx14$ h이나 maximal cholesterol response는 3–4주가 걸릴 수 있다 [R&T p.343].

### Q11. Daptomycin Study A에서 “같은 daily dose” 비교군은 무엇인가?
**Answer**: 75 mg/kg q24h와 25 mg/kg q8h이다. 둘 다 75 mg/kg/day이며, CPK는 991 vs 3996 U/L로 달랐다 [R&T pp.351–353].

### Q12. TW algorithm에서 $C_{upper}/C_{lower}$ ratio가 주로 결정하는 것은?
**Answer**: 허용 가능한 dosing interval의 상한이다. $\tau_{max}=1.44t_{1/2}\ln(C_{upper}/C_{lower})$이다 [R&T p.334].

---

## §7-Boss Dilemma

<!-- SELF-TEST -->
### Q-BD. A new oral drug has linear PK, $F=0.6$, $V=100$ L, $t_{1/2}=4$ h, and a proposed therapeutic window of 1–4 mg/L. The team proposes 300 mg q12h without loading. What should you check first?

**Answer**:
1. 먼저 이 사례가 교과서 등재 약물이 아니라 **가상 연습 문제**임을 명시한다.
2. $\tau_{max}=1.44\times4\times\ln(4/1)=7.98$ h이므로 q12h는 window를 벗어날 가능성이 크다.
3. $D_{M,max}=(V/F)(4-1)=500$ mg이지만, dose size만으로는 충분하지 않고 interval이 먼저 제약된다.
4. q8h 등 practical interval을 검토하고, 초기 목표 접근이 필요하면 loading dose를 별도로 계산한다.
5. PD delay, active metabolite, tolerance, flip-flop absorption이 있으면 단순 TW algorithm 적용을 중단하고 모델을 확장한다.

<!-- RECAP -->
**§7 Recap**: 계산 문제의 핵심은 숫자를 넣는 것이 아니라 “어떤 식이 어떤 조건에서만 유효한가”를 먼저 잠그는 것이다.

---

# §8 — Meta-Frame & Big Picture

## §8A — Positioning

<!-- MASTER LENS -->
Session 07은 pharmacometrics의 “steady-state grammar”를 만든다. 이전 세션의 single-dose PK는 시간-농도 곡선의 기본 모양을 제공한다. 이 세션은 그 곡선을 반복·유지·제약하는 법을 제공한다. 이후 TDM, PopPK covariate interpretation, exposure-response, Phase 1 multiple ascending dose design은 모두 이 문법 위에 올라간다.

---

## §8B — Dependencies and Failure Modes

| 실패 모드 | 원인 | 결과 |
|---|---|---|
| Early data에 `SS=1` 적용 | plateau 시간 조건 무시 | CL/F, V/F, ETA 추정 왜곡 |
| $A_{av,ss}$를 $C_{av,ss}$로 표기 | amount/concentration 차원 혼합 | dose rationale 오류 |
| dose 크기로 accumulation ratio 설명 | $R_{ac}$의 dose independence 미이해 | regimen 변경 효과 오판 |
| terminal half-life를 elimination으로 고정 | flip-flop 미인식 | formulation/absorption 해석 오류 |
| TW와 TI 혼용 | concentration bound와 safety sensitivity 혼동 | dose justification 불명확 |
| PD plateau를 PK plateau로 가정 | turnover/cell lifespan 무시 | effect onset/duration 예측 실패 |
| Cmax 또는 AUC 단일 변수로 toxicity 설명 | fractionation/recovery time 무시 | regimen selection 오류 |

---

## §8C — Professional Moat

<!-- ANCHOR -->
전문가의 해자는 복잡한 식을 많이 외우는 데 있지 않다. 같은 regimen 질문을 다음 결정자 표로 즉시 분해하는 데 있다.

| 질문 | 결정자 | 대표 사용처 |
|---|---|---|
| 목표 평균 농도는? | $CL$, average input rate | maintenance dose, TDM |
| 목표에 얼마나 빨리 도달하나? | $t_{1/2}$ | washout, Day-to-SS, sampling schedule |
| peak-trough 진폭은? | $\tau/t_{1/2}$ | dosing interval, adherence, toxicity |
| loading이 필요한가? | target onset, $V/F$, $R_{ac}$ | urgent therapy, bolus+infusion |
| TW 안에 머무르는가? | $C_{upper}$, $C_{lower}$, $V/F$, $t_{1/2}$ | regimen design |
| effect가 늦게 오나? | turnover/cell lifespan | statin, EPO, indirect response |
| formulation이 terminal slope를 바꾸나? | absorption/input duration | MR/depot/flip-flop |
| toxicity가 recovery time에 의존하나? | fractionation, minimum exposure duration | daptomycin-like cases |

[교과서 외 실무 해석] 이 표는 regulatory submission 문장을 대신 쓰는 것이 아니라, 교과서 수식을 제출 가능한 정량 논리로 번역하기 위한 내부 검토 틀이다. unsupported 수치, “deficiency letter”, “NDA refusal” 같은 외부 단정은 본 Content Lock에서 삭제했다.

---

## §8D — 28-Session Navigation

<!-- RECAP -->
이 세션이 잠그는 것은 네 가지다.

1. **Constant-rate input**: $C_{ss}=R_{in}/CL$.
2. **Time to steady state**: $t_{1/2}$ controls approach.
3. **Multiple dosing**: $R_{ac}$ and fluctuation depend on $\tau/t_{1/2}$.
4. **Regimen design**: therapeutic window converts PK parameters into dose and interval constraints.

다음 세션으로 넘어갈 때 이 문장을 유지한다.

> “항정상태는 하나의 숫자가 아니라, 시간·수준·진폭·임상제약을 분리해 다시 조립하는 작업이다.”

---

## PART B — Compiler-Only Appendix

This appendix is not learner-facing. It exists only to protect Phase 5 rendering fidelity.

### B1. Compilation Contract

- PART A is the only learner-facing body.
- Phase 5 must render PART A without altering scientific content, equations, source tags, headings, marker blocks, or mastery-note labels.
- PART B is instruction/guardrail only and must not be rendered as learner content unless explicitly requested.
- Do not restore deprecated Step 1 Draft v0 content.
- Do not add new scientific content, new page tags, new examples, or new figures during HTML compilation.

### B2. Figure Rendering Instructions

Approved KEEP markers in PART A:

- #1 — FIGURE_SCHEMATIC, N, Three-dominator chapter map.
- #3 — FIGURE_POINTER, R&T Fig.11-3, same average dosing rate / different fluctuation.
- #4 — FIGURE_SCHEMATIC, N, Cav,ss vs Aav,ss dimension firewall.
- #5 — FIGURE_POINTER, G Fig.2.29, flip-flop terminal slope.
- #6 — FIGURE_POINTER, R&T Fig.9-3, therapeutic utility / window.
- #9 — FIGURE_POINTER, R&T Fig.11-10, TW-driven dosage design.
- #10 — FIGURE_POINTER, R&T Fig.11-24 + Table 11-7, daptomycin fractionation.

Rejected and not to be restored: #2 G Fig.2.8/R&T Table 10-4 candidate, #7 antimicrobial figures candidate, #8 doxycycline Fig.11-4 candidate, #11 atorvastatin/EPO PD candidate. Image rights status = None; do not embed copyrighted textbook images.


Marker-to-rendering constraints:

- `<!-- FIGURE_POINTER -->`: render as text-only textbook-reference callout with Source / Why this matters / When to look / Learner instruction.
- `<!-- FIGURE_SCHEMATIC -->`: render as a newly designed schematic from the brief; do not copy textbook layout, color palette, or figure geometry.
- No `FIGURE_IMAGE_SLOT` is approved for this session.
- Preserve Source fields and captions/alt text from marker blocks.
- Do not generate Mermaid/SVG in Phase 4D. Phase 5 may generate Mermaid/SVG only under the compiler rules below.

### B3. Page Tag Rendering Rules

- Preserve all `[p.XX]`, `[pp.XX–YY]`, `[pp.XX, YY]`, and `[p.확인 필요]` tags exactly as text in PART A.
- HTML compiler must wrap page tags visibly with `.source-page` spans.
- Do not fabricate, delete, renumber, normalize into different page values, or relocate page tags.
- `[p.확인 필요]` remains visible unless already resolved by Audit/Content Lock.
- Print CSS must keep page tags visible.

### B4. HTML Compiler Requirements

Essential requirements:

- Render content; do not alter it.
- Generate a single self-contained HTML file with inline custom CSS/JS.
- Use MathJax for inline/display math.
- Convert marker comments to mapped components; no marker should remain as plain text in final HTML.
- Generate sticky left sidebar TOC with valid stable anchors for all major sections and §2 cards.
- Verify every sidebar `href="#id"` has exactly one matching body id; do not create duplicate ids.
- Render self-test answers as click-to-reveal accordions hidden by default.
- Include copy/print controls; hide navigation in print; keep source tags visible in print.
- Use responsive layout; no unauthorized external local CSS/JS/images/fonts.
- External runtime dependencies allowed only as stated in Prompt 5.

#### Full Step 2 HTML Compiler Prompt / Prompt 5

```text
ROLE: Education UX Engineer.
Function: transform Content Lock v2.1 into a production-quality HTML file.
You render content. You do not alter it.

If inputs include a PATCH MODE Insertion Map (instead of a fully-marked v2.1):
  Step 1 (mandatory): Splice each marker block into Content Lock v2 at the specified
                      anchor location, producing a working v2.1 in memory.
                      Do not modify any other text.
  Step 2 (mandatory): Output a Splice Verification Table BEFORE rendering HTML.
                      If any anchor cannot be matched exactly, STOP and report.
  Step 3:             Render HTML as below.

INPUT: Content Lock v2.1 (or Content Lock v2 + Insertion Map)
DESIGN REFERENCE: [attach reference HTML — T.E.A. Loop Playbook or equivalent]

=== PATCH MODE SPLICE VERIFICATION ===

When rendering from PATCH MODE inputs, output the following table BEFORE the HTML:

## Splice Verification Table (PATCH MODE only)

| Marker # | Anchor text (truncated to 60 chars) | Anchor found? | Match count | Inserted? | Final location (§ + card) |
|----------|-------------------------------------|---------------|-------------|-----------|---------------------------|

Rules:
- Anchor found?  : YES if exact substring match found in Content Lock v2; NO otherwise.
- Match count    : number of times the anchor appears (must be exactly 1 — see below).
- Inserted?      : YES only if Anchor found = YES AND Match count = 1.
- Final location : the § and concept card immediately preceding the inserted marker.

HALT CONDITIONS (do NOT proceed to HTML rendering if any apply):
  H1. Any "Anchor found?" = NO.
  H2. Any "Match count" ≠ 1 (zero matches OR multiple matches → ambiguous).
  H3. Any "Inserted?" = NO.

If a HALT condition triggers:
  Stop rendering. Output:
    "PATCH MODE SPLICE FAILED — N markers could not be inserted unambiguously.
     Return to Phase 4C and request anchor revision (verbatim, unique, ≥40 chars,
     extend to ≥60 chars if collision)."
  Do NOT guess insertion location.
  Do NOT proceed to HTML output.

If all markers pass: continue to HTML rendering and include the Splice Verification Table
as a comment block at the top of the HTML file (inside <!-- ... --> for traceability).

=== MARKER → COMPONENT MAPPING (mandatory) ===

| Marker / Pattern                  | HTML Component              | Style specification                                              |
|-----------------------------------|-----------------------------|------------------------------------------------------------------|
| <!-- MASTER LENS -->              | Callout box                 | border-left:4px solid #c9a84c; background:rgba(201,168,76,0.08)  |
| <!-- ANNOTATION -->               | Inline abbr / tooltip       | font-size:0.85em; color:var(--muted); font-style:italic          |
| <!-- ANCHOR -->                   | Bridge sentence             | font-style:italic; color:var(--muted)                            |
| <!-- TRENCH -->                   | Practical tip box           | border-left:4px solid var(--rose); background:rose-tint          |
| <!-- CONFUSION -->                | Side-by-side comparison     | .box.amber class                                                 |
| <!-- SELF-TEST -->                | Click-to-reveal accordion   | Question visible; answer hidden until click                      |
| <!-- RECAP -->                    | Section summary box         | border-left:4px solid var(--blue); background:blue-tint          |
| [확인 필요]                        | Highlighted flag            | <mark> tag                                                       |
| [p.XX] / [pp.XX–YY] / [pp.XX, YY] | Inline source page tag      | <span class="source-page">[p.XX]</span> — see CSS below          |
| [p.확인 필요]                      | Source page uncertainty tag | <span class="source-page source-uncertain">[p.확인 필요]</span>  |
| <!-- FIGURE_POINTER -->           | Textbook reference callout  | border-left:4px solid var(--purple); 📖 icon                     |
| <!-- FIGURE_SCHEMATIC -->         | Inline schematic <figure>   | Render via Mermaid (default) or inline SVG; <figcaption> below   |
| <!-- FIGURE_IMAGE_SLOT -->        | Image figure or placeholder | <figure> with <img> if file provided; styled placeholder if not  |

=== SOURCE PAGE TAG RENDERING RULES (v3.3.3 신설) ===

Source page tags are NOT HTML comment markers — they appear as plain text in
Content Lock v2.1 (e.g., "Concept Anatomy: Hepatic Clearance [p.123]").
The HTML compiler must detect them via pattern matching and wrap them in <span> elements.

Pattern detection (regex-equivalent, applied to body text only):
  - \[p\.(\d+)\]                 → standard single-page tag
  - \[pp\.(\d+)[–-](\d+)\]       → range tag (en-dash or hyphen)
  - \[pp\.(\d+(?:,\s*\d+)+)\]    → multi-page non-contiguous tag
  - \[p\.확인 필요\]              → uncertainty tag

Rendering:
  Standard tags  → <span class="source-page">[p.XX]</span>
  Uncertain tags → <span class="source-page source-uncertain">[p.확인 필요]</span>

Detection scope:
  - APPLY pattern detection to body text inside §2 cards, equation captions, and example headings.
  - DO NOT apply pattern detection inside <pre><code> blocks (preserve verbatim in code).
  - DO NOT apply pattern detection inside <!-- FIGURE_* --> marker blocks (those have their own
    internal "Source:" fields and are not body content tags).

Fabrication prohibition:
  - DO NOT add page tags that are not present in Content Lock v2.1.
  - DO NOT silently remove page tags during rendering.
  - DO NOT alter page numbers (e.g., normalizing en-dash to em-dash is permitted; changing
    page numbers is forbidden).

=== RENDERING REQUIREMENTS ===

Math      : MathJax CDN — inline \(...\), display \[...\]
Code      : <pre><code> dark background, language class attribute
Navigation: sticky left sidebar, anchor jump per § section
Accordion : Self-Test answers hidden by default; revealed on user click
Checklist : sessionStorage state persistence across page reload
Controls  : code block copy button, print/PDF button (window.print())
Responsive: ≤768px single-column + collapsed nav; ≥1024px two-column
Dark/Light: prefers-color-scheme auto-switch
Print     : remove backgrounds, hide navigation, optimize page-break-inside
            Source page tags MUST remain visible in print mode (do not hide via @media print).

=== NAVIGATION ANCHOR INTEGRITY RULES ===

The HTML must include a sticky left sidebar table of contents.

For every sidebar link:
- Use <a href="#..."> links only.
- Every href target must have a matching id in the body.
- Every major section heading (§1, §2, §3...) must receive a stable id.
- Every concept card inside §2 must also receive a stable id when possible.
- The href value and body id must match exactly, including spelling and hyphens.
- Do not create TOC links whose target id does not exist.
- Do not create duplicate ids.
- Enable smooth scrolling with:

html { scroll-behavior: smooth; }

Before finalizing, self-check:
1. Count all sidebar href="#id" values.
2. Confirm each id exists exactly once in the document.
3. Confirm no duplicate id exists in the body.
4. If any mismatch exists, fix before output.

Required implementation:
- The sidebar must be placed on the left side on desktop.
- The sidebar must remain visible while scrolling unless the viewport is mobile-sized.
- Each major section must be reachable by clicking the sidebar entry.
- Each §2 concept card should be reachable by clicking its sidebar sub-entry when concept-card headings are present.
- The active section may be highlighted using IntersectionObserver or equivalent JavaScript.
- On mobile viewports, the sidebar may collapse, but anchor navigation must still work.

=== FIGURE RENDERING RULES ===

GENERAL:
- Every figure marker becomes a proper <figure> block (or pointer callout) with caption and alt text.
- Figures must not interrupt reading flow — place at end of the concept card they belong to.
- Visual style consistent with the design system. No decorative imagery.
- Do not generate or embed figures not present in Content Lock v2.1.

FIGURE_POINTER:
- Render as a compact callout box with class .figure-pointer:
    border-left: 4px solid var(--purple);
    background: rgba(155, 89, 182, 0.06);
    icon: 📖
- Display: Source / Why this matters / When to look / Learner instruction.
- Do NOT generate or embed an image — pointer is text-only.

FIGURE_SCHEMATIC (Mode R or N):
- Default rendering: Mermaid via CDN (https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js).
  Use <div class="mermaid">...</div> inside <figure>.
- Use inline SVG only when the schematic requires curve plotting, precise spatial layout,
  or shapes Mermaid cannot express (e.g., concentration-time curves, radar plots).
- For comparison-style figures (Confusion-pair), CSS side-by-side cards (no SVG) are acceptable
  if the brief's "Suggested rendering" specifies CSS-card.
- Implement the brief faithfully: include only listed elements; exclude listed exclusions.
- Do not reproduce the textbook figure's exact layout, color palette, or label placement
  even when "Redrawn from textbook concept" — visual distinctness is mandatory.
- Caption: render as <figcaption>.
- Alt text: render as alt attribute on SVG container or aria-label on <figure>.
- Mermaid initialization in inline JS:
    mermaid.initialize({ startOnLoad: true, theme: 'neutral',
                         themeVariables: { fontFamily: 'var(--font)' } });

MERMAID SELF-CHECK (생성 직후 self-validate):
After generating each Mermaid block, verify all of the following BEFORE finalizing:
  M1. Block opens with a valid directive: flowchart TD | flowchart LR |
      graph TD | graph LR | sequenceDiagram | classDiagram | stateDiagram-v2 | erDiagram.
  M2. Node IDs contain ONLY [A-Za-z0-9_]. No parentheses, slashes, dots, hyphens,
      Korean characters, spaces, or quotes inside IDs.
  M3. Any label containing parentheses, special characters, or non-ASCII characters
      is wrapped in double quotes:  A["Clearance (CL)"]
  M4. Edge labels with special chars use the |"label"| form:  A -->|"Q × E"| B
  M5. Subgraph titles, when used, are quoted:  subgraph "Hepatic"
  M6. No trailing semicolons inside node definitions.
  M7. If any of M1–M6 cannot be satisfied OR Mermaid expressiveness is insufficient,
      FALLBACK to one of:
        - inline SVG (for spatial/curve figures)
        - CSS side-by-side cards (for comparison figures)
      Do not emit a Mermaid block that is likely to fail rendering.

FIGURE_IMAGE_SLOT:
- If Rights = User-supplied AND image file exists in working directory:
    <figure><img src="..." alt="..." /><figcaption>...</figcaption></figure>
- If Rights = Open-license AND license/attribution provided in marker:
    <figure>
      <img src="..." alt="..." />
      <figcaption>
        [Caption text]
        <span class="figure-attribution">
          Source: [Attribution]. License: [License type].
          [<a href="[Source URL]">link</a>]
        </span>
      </figcaption>
    </figure>
- If Rights = placeholder OR file unavailable:
    Render styled placeholder box with class .figure-placeholder:
    [📖 교과서 원그림 삽입 위치 — Source: Book, p.XX, Fig.Y]
    Do not generate an approximation of the textbook figure.

CAPTION & ALT TEXT (all schematic/image figures):
- Caption mandatory. Alt text mandatory. Both from the brief.

=== CSS DESIGN SYSTEM (inherit from reference) ===

Variables: --bg, --surface, --surface-2, --ink, --muted, --faint,
           --line, --line-strong, --blue, --green, --purple, --amber, --rose,
           --radius, --radius-sm, --shadow, --font, --mono

Add for navigation:
  html {
    scroll-behavior: smooth;
  }
  .sidebar {
    position: sticky;
    top: 0;
    align-self: start;
    height: 100vh;
    overflow-y: auto;
  }
  .sidebar a {
    display: block;
    text-decoration: none;
  }
  .sidebar a.active {
    font-weight: 700;
    border-left: 3px solid var(--purple);
  }
  @media (max-width: 768px) {
    .sidebar {
      position: static;
      height: auto;
      max-height: none;
    }
  }

Add for v3.3 figure components:
  .figure-pointer { border-left: 4px solid var(--purple); ... }
  figure { margin: 1.5em 0; }
  figcaption { color: var(--muted); font-size: 0.9em; margin-top: 0.5em; }
  .figure-attribution { display: block; font-size: 0.8em; margin-top: 0.3em;
                        color: var(--faint); }
  .figure-placeholder { border: 2px dashed var(--line-strong); padding: 2em;
                         text-align: center; color: var(--muted); }

Add for v3.3.3 source page tag components:
  .source-page {
    font-size: 0.78em;
    color: var(--purple);
    background: rgba(155, 89, 182, 0.10);
    padding: 2px 6px;
    border-radius: 6px;
    vertical-align: super;
    white-space: nowrap;
    margin-left: 0.25em;
    font-weight: 500;
    letter-spacing: 0.01em;
  }
  .source-page.source-uncertain {
    color: var(--amber);
    background: rgba(245, 158, 11, 0.12);
    border: 1px dashed var(--amber);
  }
  /* Print: keep tags visible for offline traceability */
  @media print {
    .source-page {
      background: transparent;
      color: #000;
      border: 1px solid #888;
    }
  }
  /* Hover: subtle elevation to confirm interactivity (if linked to PDF in future) */
  .source-page:hover {
    background: rgba(155, 89, 182, 0.18);
  }

=== OUTPUT SPECIFICATION ===

Single HTML file with all custom CSS and custom JS inline.
External runtime dependencies are allowed ONLY for:
  - MathJax CDN
  - Mermaid CDN
  - cdnjs.cloudflare.com library list (e.g., highlight.js for code coloring)
No external local .css / .js / font / image files unless explicitly supplied by the user.
File header comment block: document title | chapter | generation date.
PATCH MODE only: include Splice Verification Table as a comment block in the HTML header.

=== PROHIBITED ===

- <iframe>, <embed>, external .js files (other than permitted CDNs), external local .css
  files, external font files (other than permitted CDNs).
- Any modification to Content Lock v2.1 text content (including page tag text).
- Self-Test answer text visible without user interaction.
- Markers rendered as plain text (every marker must become its mapped component).
- Source page tags rendered as plain bracketed text without <span> wrapping.
- Reproducing copyrighted textbook figures exactly when rendering R/N schematics.
- Embedding textbook images without User-supplied or Open-license rights with attribution.
- Emitting Mermaid blocks that fail M1–M6 self-check.
- Proceeding to HTML rendering when any PATCH MODE Splice Verification HALT condition
  (H1–H3) is triggered.
- Guessing insertion location for unmatched anchors.
- Adding new source page tags or altering existing ones during HTML compilation.
- Hiding source page tags via @media print or display:none under any condition.
- Creating sidebar TOC links whose target ids do not exist.
- Creating duplicate body ids.
- Creating body ids that are not stable or that change across repeated generations for the same heading text.

Output (PATCH MODE):
  1. Splice Verification Table
  2. (only if all markers pass) Complete HTML from <!DOCTYPE html> to </html>

Output (FULL MODE):
  Complete HTML from <!DOCTYPE html> to </html>.
```

### B5. Audit Guardrails

Session-specific forbidden restorations:

- Do not restore `Cav,ss = ... = 1.44·F·Dose·t1/2/τ` as a concentration equation; this is an amount equation unless divided by V under stated one-compartment assumptions.
- Do not state that `25 mg/kg q24h` vs `25 mg/kg q8h` is the same daily dose comparison in daptomycin Study A; the same-daily-dose comparison is `75 mg/kg q24h` vs `25 mg/kg q8h`.
- Do not label phenobarbital 5.8 as the peak/trough accumulation index; keep 5.8/5.76 as average amount per dose and ≈6.3 as Rac/peak-trough accumulation index.
- Do not restore unsupported numerical or causal chains: `30–40%`, `AUC 30–80%`, `SAE`, `NDA refusal`, `deficiency letter`, or similar.
- Do not present `FDA Clinical Pharmacology Section`, `NDA standard language`, or reviewer-response phrasing as textbook-derived content.
- Do not present `U(C)=Σw_iP_i(C)` as an R&T source equation; it is only a pedagogical formalization when explicitly labeled.
- Do not add unapproved code blocks, unapproved figures, source-unsupported external examples, or textbook image embedding.
- Generic regression guardrails from the assembler prompt remain active where applicable: unsupported OFV thresholds, unsupported FDA/EMA reviewer claims, and any NOT_IN_SOURCE item rejected by Audit/Content Lock must not be restored.


### B6. Crucible Guardrails

- Crucible Report v1 is not a raw prose source for Phase 5.
- Preserve only the logic already adopted in Content Lock v2 or explicitly represented in approved figure markers and mastery notes.
- Do not turn expert interpretation into textbook fact.
- Do not re-expand rejected Grade B/C material, study-problem material, or low-priority example chains.
- Any new expert framing must remain labeled EXPERT_INFERENCE and must not add numerical values, page tags, or named external examples.


### B7. Deprecated and Forbidden Restorations

- Step 1 Draft v0 is deprecated.
- Do not use Step 1 Draft v0 as learner-body source except through the Micro-Patch Gate.
- Do not restore rejected overclaims, unsupported numbers, unsupported regulatory claims, source-unsupported examples, unapproved code, or unapproved figures.
- Do not broaden Content Lock v2 into Content Lock v3 during HTML compilation.
- Do not convert PART B logs, matrices, or guardrails into learner-facing cards.

### B8. PATCH MODE Splice Verification Table

| Marker # | Anchor text | Anchor found? | Match count | Inserted? | Final location (§ + card) |
|---|---|---|---|---|---|
| 1 | ## 1. Master Lens | YES | 1 | YES | §1 — Master Lens |
| 3 | ## §2-M3. Apex Concept — 다중투여 축적인자 $R_{ac}=1/(1-e^{-K\tau})$ | YES | 1 | YES | §2-M3 — Apex Concept |
| 4 | ## §2-M4. 항정상태 평균농도와 평균 amount: $C_{av,ss}$ vs $A_{av,ss}$ | YES | 1 | YES | §2-M4 — Cav,ss vs Aav,ss |
| 5 | ## §2-M5. Flip-flop 동태: $K_a<K$일 때 terminal slope의 정체 | YES | 1 | YES | §2-M5 — Flip-flop |
| 6 | ## §2-M6. Therapeutic Window — PK 식을 임상 의사결정으로 바꾸는 제약조건 | YES | 1 | YES | §2-M6 — Therapeutic Window |
| 9 | ## §2-M8. TW-Driven Dosage Design Algorithm | YES | 1 | YES | §2-M8 — TW-Driven Dosage Design Algorithm |
| 10 | ### Daptomycin fractionation anchor | YES | 1 | YES | §2-M7 — Daptomycin fractionation anchor |

### B9. Zero-Omission Coverage Matrix

| Domain | Required item | Evidence in PART A | Status | Action |
|---|---|---|---|---|
| C1 Scope Lock Required Concepts | M1 constant-rate plateau concentration | §2-M1 and Curation Map M1 | PRESENT | None |
| C1 Scope Lock Required Concepts | M2 plateau approach time by half-life | §2-M2 and Curation Map M2 | PRESENT | None |
| C1 Scope Lock Required Concepts | M3 accumulation factor and dose-independence | §2-M3 and §5-쌍4 | PRESENT | None |
| C1 Scope Lock Required Concepts | M4 Cav,ss vs Aav,ss dimension separation | §2-M4, §5-쌍1, Figure #4 marker | PRESENT | None |
| C1 Scope Lock Required Concepts | M5 flip-flop terminal slope | §2-M5 and §5-쌍3 | PRESENT | None |
| C1 Scope Lock Required Concepts | M6 therapeutic window / utility / TI distinction | §2-M6 and §5-쌍5 | PRESENT | None |
| C1 Scope Lock Required Concepts | M7 loading + maintenance, bolus + infusion anchor | §2-M7 | PRESENT | None |
| C1 Scope Lock Required Concepts | M8 TW-driven dosage design algorithm | §2-M8 and §7 Q12/BD | PRESENT | None |
| C1 Scope Lock Required Concepts | M9 PD-driven plateau | Curation Map M9, §2-M6, §7 Q10 | PRESENT_COMPRESSED | Kept compressed per Content Lock. |
| C1 Scope Lock Required Concepts | M10 dose fractionation toxicity | Curation Map M10, §2-M7 daptomycin anchor, Figure #10 marker | PRESENT | None |
| C2 Required Data Anchors | Eptifibatide and t-PA plateau-time anchors | §2-M2 Practical interpretation | PRESENT | None |
| C2 Required Data Anchors | Phenobarbital t1/2=4 days, 100 mg q24h, 5.8 vs 6.3 label lock | §2-M3 Phenobarbital label lock; §7 Q9 | PRESENT | None |
| C2 Required Data Anchors | PK13 bolus + infusion anchor | §2-M7 Bolus + infusion anchor | PRESENT | None |
| C2 Required Data Anchors | Clobazam single-dose AUC to plateau-average context | Curation Map C8 / §2-M8 applicability lock | PRESENT_COMPRESSED | Kept context-level. |
| C2 Required Data Anchors | Atorvastatin / erythropoietin PD delay anchors | Curation Map M9; §2-M6 PK/PD and response clocks; §7 Q10 | PRESENT_COMPRESSED | No extra figure marker restored. |
| C2 Required Data Anchors | Daptomycin Study A corrected same daily dose and CPK values | §2-M7, Curation Map M10, §7 Q11, Figure #10 marker | PRESENT | None |
| C3 Audit MUST_FIX / SHOULD_FIX | M4 amount/concentration dimension error | Corrected in Curation Map M4, §2-M4, §5-쌍1 | PRESENT | No further patch. |
| C3 Audit MUST_FIX / SHOULD_FIX | Daptomycin same-daily-dose comparison | Corrected as 75 mg/kg q24h vs 25 mg/kg q8h | PRESENT | No further patch. |
| C3 Audit MUST_FIX / SHOULD_FIX | Phenobarbital R=5.8 ambiguity | Separated average accumulation ratio from peak/trough Rac | PRESENT | No further patch. |
| C3 Audit MUST_FIX / SHOULD_FIX | Unsupported numerical/regulatory chains | Removed from PART A; guardrail in PART B | PRESENT | Forbidden restoration. |
| C3 Audit MUST_FIX / SHOULD_FIX | Utility formula source labeling | §2-M6 labels formula as pedagogical formalization, not source equation | PRESENT | No further patch. |
| C3 Audit MUST_FIX / SHOULD_FIX | PK13 anchor placement | §2-M7 bolus + infusion anchor | PRESENT | No further patch. |
| C3 Audit MUST_FIX / SHOULD_FIX | Steady-state vs equilibrium nuance | Curation Map C1 / §5-쌍2 context | PRESENT_COMPRESSED | Context-level. |
| C3 Audit MUST_FIX / SHOULD_FIX | Evaluation-of-multiple-dose-regimen context Eq.11-23~25 | Curation Map C10 and §8 dependencies | PRESENT_COMPRESSED | No independent expansion. |
| C4 Audit T5 Coverage Findings | G §2.2.2, §2.2.10, §2.2.11 | §2-M1–M5 | PRESENT | None |
| C4 Audit T5 Coverage Findings | G PK11 | Curation Map C4 | JUSTIFIABLY_OMITTED | Context anchor only; no high-impact omission after Content Lock. |
| C4 Audit T5 Coverage Findings | R&T Ch.9–11 core headings | §2-M3–M8 and §5/§7 | PRESENT | None |
| C4 Audit T5 Coverage Findings | Study problems and low-priority tables | Excluded or transformed only into clearly labeled self-test when needed | JUSTIFIABLY_OMITTED | Exercises not restored as source body. |
| C5 Figure Coverage | KEEP markers #1, #3, #4, #5, #6, #9, #10 | All seven marker blocks present exactly once in PART A | PRESENT | Splice table PASS. |
| C5 Figure Coverage | Rejected figures #2, #7, #8, #11 | Not restored as markers | PRESENT | Guardrail in PART B. |
| C5 Figure Coverage | Image rights = None | Figure pointers text-only; schematics newly designed; no textbook images embedded | PRESENT | Phase 5 guardrail. |
| C6 Page Tag Integrity | Preserve source page tags | All existing page tags remain in PART A; no new page tags added by augmentation | PRESENT | HTML compiler must wrap visibly. |
| C7 Crucible Grade A Preservation | Three-dominator lens, dimension firewall, daptomycin correction, utility lens | Preserved in §1, §2-M3/M4/M6/M7 and figure markers | PRESENT | None |
| C8 Deprecated Draft Regression | Unsupported overclaims/numbers/regulatory chains/source-unsupported examples | Not restored; explicitly forbidden in PART B | PRESENT | None |
| C9 Canonical Body Integrity | Content Lock v2 learner body + approved Phase 4C markers + labeled augmentations | PART A constructed in PATCH MODE; no broad rewrite | PRESENT | No micro-patch required. |

### B10. Micro-Patch Log

No micro-patches needed. PART A equals the learner-facing portion of Content Lock v2 plus the approved Phase 4C marker splice and the labeled Mastery Augmentation Layer.

### B11. Mastery Augmentation Log

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
|---|---|---|---|---|---|---|
| 1 | §2-M1 | J | YES | EXPERT_INFERENCE | 정속 주입 해석에서는 먼저 “입력률이 정확했는가?”와 “clearance 가정이 맞는가?”를 분리한다. 관찰 농도가 plateau와 다를 때 시… | Medium |
| 2 | §2-M2 | F | YES | EXPERT_INFERENCE | 3–4 half-lives 규칙은 “목표가 맞다”는 보증이 아니라 “정해진 목표 plateau의 몇 %에 접근했는가”를 말한다. 잘못 잡은 목표… | Medium |
| 3 | §2-M3 | M | YES | CRUCIBLE_DERIVED | $R_{ac}$는 노출의 절대값이 아니라 반복투여가 만든 배율이다. 선형 PK에서는 dose를 키우면 곡선 전체가 커지지만, 같은 $	au/t_… | Low |
| 4 | §2-M4 | F | YES | AUDIT_DERIVED | $A_{av,ss}$ 식을 $C_{av,ss}$ 식으로 잘못 옮기는 오류는 단순 표기 문제가 아니라 단위 방화벽 붕괴다. 보고서나 슬라이드에서 … | Low |
| 5 | §2-M5 | K | YES | TEXTBOOK_DERIVED | Terminal phase는 항상 elimination phase라는 이름을 붙이기 전에 route와 input function을 먼저 확인해야… | Low |
| 6 | §2-M6 | J | YES | CRUCIBLE_DERIVED | Therapeutic window는 계산이 끝난 뒤 붙이는 장식이 아니라 regimen이 통과해야 하는 제약조건이다. 숙련자는 먼저 benefi… | Low |
| 7 | §2-M7 | W | YES | EXPERT_INFERENCE | Loading과 maintenance는 같은 “용량”이라는 단어를 쓰지만 데이터셋과 해석에서는 서로 다른 질문이다. Loading은 시작 위치를… | Medium |
| 8 | §2-M8 | R | YES | EXPERT_INFERENCE | TW-driven algorithm은 최종 처방 자동생성기가 아니라 선형 PK와 즉각적 concentration-response 가정이 통과되는… | Medium |

Rejected/deferred candidates:

| Rejected candidate | Reason for rejection |
|---|---|
| Additional antimicrobial figure sidebar | Rejected by Phase 4C figure budget; would restore candidate #7. |
| Additional doxycycline loading/maintenance figure pointer | Rejected by Phase 4C; M8 figure covers the higher-ROI design logic. |
| Additional PD-delay figure pointer for atorvastatin/EPO | Rejected by Phase 4C budget; Content Lock text retains the anchor. |
| External regulatory/NDA phrasing augmentation | Rejected because it would add unsupported external claim and violate Audit guardrails. |


# 10_HTML Compile Input Master

## Phase 4D Certification

| Certificate | Status | Basis |
|---|---|---|
| Learner-Standalone Certificate | PASS | PART A contains only the learner navigation aid, locked learner body, approved figure markers, and bounded mastery notes; compiler/audit/process material is kept in PART B. |
| Zero-Omission Certificate | PASS | Scope-required C1–C5 concepts, data anchors, Audit MUST_FIX/SHOULD_FIX corrections, Phase 4C KEEP figures, and adopted Crucible logic are present, repaired in Content Lock v2, or justifiably bounded. |
| Mastery-Uplift Certificate | PASS | Seven short, source-labeled augmentations were inserted adjacent to relevant concepts without broad rewriting or unsupported numeric claims. |
| Source-Boundary Certificate | PASS | All augmentations are labeled as TEXTBOOK_DERIVED, AUDIT_DERIVED, CRUCIBLE_DERIVED, or EXPERT_INFERENCE and do not masquerade as textbook statements. |
| HTML-Readiness Certificate | PASS | PART B contains Phase 5 rendering rules, figure rules, page-tag rules, navigation integrity rules, audit/crucible guardrails, and splice verification. |

## Assembly Mode

**PATCH MODE.** `10_Content Lock v2.1.md` is a Figure Marker Insertion Patch rather than a full re-emission of the canonical body. Therefore, the learner body was assembled from `10_Content Lock v2(4).md` with the seven approved Phase 4C marker blocks spliced into exact anchors.

## Input Manifest

| File | Role | Authority level | Used for | Notes |
|---|---|---|---|---|
| 10_scope_lock(3).md | Scope Lock | A0 | scope boundary; source range; required data anchors; image rights | Two-source scope: G&W + R&T; pp.225–228 boundary preserved |
| 010_G_PD 모델 기초 Emax·Hill·AUEC(4).pdf | Original textbook PDF | A1 | PDF verification source | G&W extract; 42 PDF pages available; textbook images not embedded |
| 010_T_PD 모델 기초 Emax·Hill·AUEC(4).pdf | Original textbook PDF | A1 | PDF verification source | R&T Ch.8 extract; 32 PDF pages available; textbook images not embedded |
| 10_Audit_Report_v1(4).md | Source Fidelity Audit v1 | A2 | audit guardrail; MUST_FIX/SHOULD_FIX; forbidden restorations | Conditional Go; unsupported claims controlled |
| 10_Content Lock v2(4).md | Content Lock v2 | A3 | canonical learner body base | Primary text-final body before figure marker insertion |
| 10_Content Lock v2.1.md | Content Lock v2.1 Patch | A4 | figure insertion source; Strategy Table; Insertion Map | PATCH MODE only; marker blocks spliced into v2 |
| 10_Crucible_Report_v1(1).md | Crucible Report v1 | A5 | crucible guardrail; mastery insight candidates | Only adopted or explicitly allowed Grade A logic used; not a raw prose source |
| 10_step1_draft_v0(3).md | Step 1 Draft v0 | A6 | deprecated source; regression check only | No raw Step 1 prose restored |
| S10_phase1_patch memo(2).md | Phase 1 Patch Memo | A6 | deprecated/locked reference; regression and audit context | Used to confirm Phase 1 was not HTML-ready and known weaknesses were fixed later |
| 붙여넣은 마크다운(2)(59).md | Step 2 HTML Compiler Prompt / Prompt 5 | A7 | compiler instruction; marker mapping; page tag rendering; navigation integrity | Essential rendering rules incorporated in PART B |
| 붙여넣은 텍스트 (1)(80).txt | Phase 4D Master Assembler Prompt | process instruction | assembly protocol | Adapted output filename from 05 to 10 per user request |
| 10_Content Lock v1(3).md | Content Lock v1 | locked reference | not used as canonical source | Superseded by Content Lock v2 |

## Source Verification Snapshot

| PDF | Declared source range | File check | Use restriction |
|---|---|---|---|
| G&W PDF | p.199–224; p.229–234; p.732–741 | 42 PDF pages available | Used to verify page-scope, equation/figure identity, PD3 anchors |
| R&T PDF | p.233–264 | 32 PDF pages available | Used to verify time-delay, hysteresis, effect-compartment, duration examples |

## PART A — Learner-Facing Complete Handout

## Learner Navigation Aid

**How to use this handout:** 먼저 §1에서 C1–C5의 위치를 잡고, §2의 각 Concept Anatomy Card를 순서대로 읽는다. `FIGURE_POINTER`는 교과서 원그림을 직접 보라는 안내이며, 본 문서에는 저작권 그림을 삽입하지 않는다. `FIGURE_SCHEMATIC`은 Phase 5에서 원그림과 구조적으로 구별되는 재도식으로 렌더링될 항목이다.

**Learning route:** C1에서 `Kd`와 `EC50`의 층위를 분리하고, C2에서 Hill `n`을 steepness/design parameter로 고정한다. C3–C4에서는 hysteresis가 보일 때 direct plasma-response 가정을 내려놓고 delay topology를 선택하는 법을 익힌다. C5에서는 AUEC와 duration이 drug half-life만으로 결정되지 않는다는 점을 response-time scale에서 확인한다.

**Before you start:** equilibrium, first-order elimination, baseline response, concentration-time curve, response-time curve의 차이를 떠올린다.  
**After you finish:** `Kd ≠ EC50`, `n ≠ mechanism proof`, `hysteresis ≠ noise`, `drug t1/2 ≠ effect duration`을 각각 한 문장으로 설명할 수 있어야 한다.

---

# §1 — Session Header & Roadmap

**Source 통합:** G&W Ch.3는 receptor binding → Emax/Hill → non-steady-state response/AUEC의 수식적 골격을 제공한다. R&T Ch.8은 같은 개념을 임상 시간축, hysteresis, effect compartment, indirect response, duration of effect로 번역한다.

<!-- MASTER LENS -->
**Big Idea:** PD 모델링의 본질은 농도-효과 관계의 **비선형성(Emax / Hill `n`)**과 **시간 지연(hysteresis)**을 동시에 해부하는 것이다. 전자는 dose escalation의 step size와 농도범위 설계를 결정한다. 후자는 onset/offset, dosing interval, rate-limiting process 판단을 결정한다.

G&W는 PK/PD modeling의 목적을 생리·병리 조건에서 response magnitude와 time course를 예측하는 핵심 in vivo property의 식별로 제시한다. 따라서 dose-response만으로는 충분하지 않다. Relevant compartment(← 효과와 연결되는 생체 내 위치)에서의 exposure over time과 biological response를 연결해야 한다. Ideal PD measure는 sensitive, gradual, meaningful, objective, reproducible해야 하며, control과 2–4 dose levels 중 하나의 maximum response 도달이 권장된다. [G&W p.199–200]

**개념 항법도:**
- C1. Law of Mass Action → Emax 골격. [G&W p.202–204]
- C2. Sigmoid Emax / Hill model [Apex]. [G&W p.216–220; PD3 p.732–741]
- C3. Hysteresis — 시간 지연의 시각적 진단. [R&T p.233–235]
- C4. Effect Compartment + Systems-in-flux / Indirect Response. [R&T p.241–248]
- C5. AUEC + Duration + PK/PD rate-limiting. [G&W p.229–234; R&T p.249–259]

<!-- ANCHOR -->
**구조적 흐름:** 질량작용법칙(C1) → Emax 쌍곡선 → Hill `n` 도입으로 sigmoid 일반화(C2) → 평형 가정의 붕괴가 hysteresis로 드러남(C3) → effect compartment 또는 system turnover로 시간 지연을 흡수(C4) → response-time curve의 적분량과 duration을 설계 지표로 사용(C5).

**Scope boundary:** G&W §3.6.1의 competitive antagonism 시작부까지만 본문에 포함한다. G&W §3.6.2–§3.6.5 및 G&W §3.12 baseline modeling은 `[확인 필요 — 첨부 PDF 미포함 구간]`으로 유지하고 본 세션에서 추정하지 않는다.

---

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.199, Fig.3.1
Why this matters: This figure frames the whole session as two linked PD problems: concentration-response sensitivity and response-time behavior. Without it, C1–C5 may look like separate formulas rather than one PK→PD translation chain.
When to look: before reading §1 Roadmap or immediately after the §1 Big Idea
Learner instruction: Inspect the left panel for potency/efficacy and the right panel for onset/intensity/duration. Then map C1–C2 to the left panel and C3–C5 to the right panel.
<!-- /FIGURE_POINTER -->

---

# §2 — Concept Anatomy Cards

---

## Card C1 — Law of Mass Action → Emax 골격


<!-- MASTER LENS -->
### [개념 Big Idea]

Kd는 ligand-receptor 결합 친화도의 지표다. EC50는 결합 이후 transduction과 tissue response까지 포함한 functional sensitivity의 지표다. **Kd와 EC50가 다를 수 있다는 사실**이 C1의 핵심이다. 그 차이를 만드는 대표 이유가 spare receptor와 cascade amplification이다. [G&W p.203–206]

<!-- ANNOTATION -->
즉, 결합이 강하다는 말과 조직에서 절반 효과가 낮은 농도에서 나온다는 말은 같은 뜻이 아니다.

<!-- ANCHOR -->
평형 결합의 미시적 동역학을 occupancy 식으로 정리하면, Emax 모델의 분자와 분모가 왜 같은 농도 단위를 가져야 하는지 드러난다.

### A. Formal Definition

가역적 1:1 drug-receptor binding에서 response `E`는 occupied receptor complex(← 약물이 결합한 receptor pool) `[RC]`에 비례한다. 모든 receptor가 occupied되면 `Emax = α[R_T]`이며, `α`는 intrinsic activity다. [G&W p.203]

### B. Derivation

**평형 결합:**

$$
\frac{d[RC]}{dt}=k_1[R][C]-k_{-1}[RC]=0
$$

따라서

$$
K_d=\frac{k_{-1}}{k_1}=\frac{[C][R]}{[RC]}
$$

총 receptor 농도 `[R_T]=[R]+[RC]`를 대입하면

$$
\frac{[RC]}{[R_T]}=\frac{[C]}{[C]+K_d}
$$

Response proportionality를 적용하면

$$
\frac{E}{E_{max}}=\frac{[C]}{[C]+K_d}, \qquad E=\frac{E_{max}\cdot [C]}{[C]+K_d}
$$

Functional response에서는 `Kd` 대신 `EC50`가 사용된다.

$$
E=\frac{E_{max}\cdot C}{EC_{50}+C}
$$

`[출처: G&W 5e, Ch.3, p.202–204, Eq.3:1–3:10]`

### C. Structural Necessity

분자 `[C]`는 available ligand가 늘수록 receptor occupancy가 증가한다는 질량작용법칙의 결과다. 분모 `[C]+Kd`는 receptor conservation을 반영한다. 이 구조 때문에 occupancy는 0–1 사이에 머물며, response도 `Emax`를 초과하지 않는다.

### D. Assumptions & Boundary Conditions

- 1:1 reversible binding, equilibrium, single effective biophase concentration.
- Response is proportional to `[RC]`; full effect may occur before full receptor occupancy if receptor reserve(← 여분 수용체에 의한 증폭 여지) exists.
- `EC50 ≠ Kd`일 수 있다. G&W는 occupancy-response 불일치와 signal amplification을 명시한다. [G&W p.204–206]

### E. Limitations

Spare receptor가 많거나 cascade gain이 큰 tissue에서는 small occupancy가 large response를 만들 수 있다. G&W Fig.3.5는 10% occupancy가 90% response로 증폭되는 cascade 예를 제시한다. Fig.3.6은 동일 response에 필요한 occupancy가 tissue마다 다를 수 있음을 보여준다. [G&W p.205–206]

Saturation/displacement binding과 Cheng-Prusoff 변환은 receptor binding assay의 Ki/IC50 해석에 필요하지만, 본 세션에서는 functional EC50와 binding Kd를 혼동하지 않는 boundary로만 사용한다. [G&W p.206–210]

<!-- TRENCH -->
**[Trench-Level Tip]** EC50 covariate effect가 보이면 먼저 “drug-side 변화인가, system-side 변화인가?”를 분리한다. Total concentration 기반 EC50 변화는 protein binding 변화일 수 있으므로 unbound concentration 분석이 없으면 receptor sensitivity 변화로 단정하지 않는다. `[실무 구현 번역]`

### F. Zettelkasten Atom

**Atom C1:** `Kd`는 결합 강도, `EC50`는 결합 이후 조직·신호 시스템까지 포함한 functional sensitivity다. Emax 식의 쌍곡선은 receptor conservation과 equilibrium mass action에서 나온다.

<!-- RECAP -->
**Recap:** C1은 Emax 모델을 “경험식”이 아니라 receptor occupancy와 response transduction의 압축형으로 보게 만든다.

> **Mastery Note — [AUDIT_DERIVED]**  
> C1을 읽은 뒤에는 `Kd`, total `EC50`, unbound `EC50`, tissue response sensitivity를 같은 층위의 숫자로 배열하지 않는다. 어느 숫자가 binding assay에서 왔고, 어느 숫자가 functional response에서 왔는지를 먼저 분리해야 downstream covariate 해석이 무너지지 않는다.

<!-- FIGURE_SCHEMATIC -->
Title: Kd와 EC50의 분리: receptor occupancy → transduction → response
Mode: R
Visual objective: In 5 seconds, the learner should see that the functional response curve can be left-shifted from the receptor occupancy curve.
Core message: Kd belongs to binding affinity, whereas EC50 belongs to the amplified tissue/system response.
Elements to include: shared concentration x-axis; receptor occupancy/stimulus curve labeled Kd; functional response curve shifted left and labeled EC50; receptor occupancy → stimulus/transduction → response arrow chain; note that EC50 may differ from Kd and exceptions exist.
Elements to exclude: Cheng-Prusoff derivation; full/partial agonist profiles; exact textbook layout; original color scheme; receptor cartoon details.
Suggested rendering: SVG
Caption: Receptor binding and functional response need not align; transduction/cascade amplification can make EC50 differ from Kd.
Alt text: Two concentration-response curves share one concentration axis; the functional response curve is left-shifted from receptor occupancy, illustrating EC50–Kd separation.
Source relation: Redrawn from textbook concept
<!-- /FIGURE_SCHEMATIC -->


---

## Card C2 — Sigmoid Emax / Hill Model [Apex]


<!-- MASTER LENS -->
### [개념 Big Idea]

Hill `n`은 mechanism proof가 아니라 **curve steepness/flexibility parameter**(← 곡선의 급경사와 굽힘을 설명하는 파라미터)다. 그러나 임상적으로는 강력하다. `n`이 커질수록 50% effect에서 90% effect로 이동하는 데 필요한 concentration ratio가 줄어든다. 따라서 dose-titration step size와 safety margin 해석이 더 민감해진다. [G&W p.216, p.220]

Linear/log-linear effect models는 제한된 농도 범위에서는 유용하다. 그러나 effect plateau(← 농도 증가에도 효과가 더 늘지 않는 구간)와 steep transition을 설명하려면 ordinary Emax를 넘어 sigmoid Emax가 필요하다. [G&W p.210–216]

### A. Formal Definition

Sigmoid Emax model:

$$
E=\frac{E_{max}\cdot C^n}{EC_{50}^n+C^n}
$$

Baseline이 있는 inhibitory response에서는 다음과 같이 쓴다.

$$
E=E_0-\frac{I_{max}\cdot C^n}{IC_{50}^n+C^n}
$$

`[출처: G&W 5e, Ch.3, p.216, p.218, Eq.3:32, Eq.3:34–3:35]`

### B. Parameter Recovery and PD3 Anchor

Graphical slope 관계:

$$
m=\frac{n\cdot E_{max}}{4}, \qquad n=\frac{4m}{E_{max}}
$$

Intercept recovery:

$$
C_0=EC_{50}\cdot e^{-2/n}
$$

`[출처: G&W p.219, Eq.3:38–3:42]`

PD3 blood-pressure inhibitory Imax case는 initial graphical estimate와 final model estimate를 연결한다. 0–800 µg/L design의 sigmoid Imax model에서 `E0=171`, `Imax=34.7`, `IC50=140`, `n=2.03`, AIC=45.6이 제시되며, ordinary Imax model은 `E0=177`, `Imax=49.8`, `IC50=175`, AIC=50.8로 비교된다. [G&W p.733–735]

PD3의 핵심은 “추가 parameter는 항상 overfitting”이 아니라는 점이다. Sigmoid model에서 IC50 precision이 개선되고 AIC/F-test/VIF가 함께 지지하면, `n`은 단순 장식이 아니다. 이 경우 `n`은 데이터가 요구하는 curvature parameter(← 곡선 굽힘을 설명하는 파라미터)가 된다. [G&W p.734–741]

### C. Structural Necessity

`C^n`이 분자와 분모에 동시에 들어가는 이유는 effect가 concentration의 nonlinear transformation을 거치더라도 0–Emax boundary를 보존해야 하기 때문이다. `n=1`이면 ordinary Emax로 돌아간다. `n>1`이면 transition이 steep해지고, `n<1`이면 active metabolite, multiple receptor sites, heterogeneity 같은 가능성을 시사할 수 있다. 단, 이는 단독 mechanism proof가 아니다. [G&W p.216]

Unbound concentration transformation에서도 `n`은 보존된다.

$$
E=\frac{E_{max}(C_u/f_u)^n}{EC_{50}^n+(C_u/f_u)^n}
=\frac{E_{max}\cdot C_u^n}{EC_{u50}^n+C_u^n}
$$

단백결합 차이가 큰 비교에서는 total EC50가 아니라 unbound EC50를 점검해야 한다. 그래야 potency 변화와 protein binding 변화를 혼동하지 않는다. [G&W p.216–217]

### C-2. Plausible Fallacy: “Curvature Suppression”

<!-- CONFUSION -->
**오류:** “sigmoid해 보이지만 ordinary Emax도 대충 맞으니 `n=1`로 단순화한다.”  
**교정:** PD3는 같은 약물이라도 0–500 µg/L design에서는 F-test가 sigmoid superiority를 통과하지 못하고, 0–800 µg/L까지 확장하면 통과하는 사례를 보여준다. 따라서 결론은 “sigmoid가 필요 없다”가 아니다. 결론은 “농도 범위가 curvature를 볼 만큼 충분한가?”다. [G&W p.734–735, p.740–741]

Hill `n`을 “positive cooperativity가 증명되었다”라고 쓰면 source fidelity가 깨진다. Orthogonal binding evidence가 없는 한, `n`은 steepness와 dose-titration sensitivity의 현상학적 파라미터로 기술한다. `[교과서 기반 + 교과서 외 규제 해석]`

### D. Assumptions & Boundary Conditions

- 농도 범위가 `EC50` 주변과 plateau를 충분히 포함해야 `n`과 `Emax/Imax`가 식별된다.
- Baseline `E0`가 시간에 따라 변하면 baseline model이 필요하다. `[확인 필요 — G&W §3.12 첨부 PDF 미포함 구간]`
- Target concentration inversion은 absolute response와 baseline-relative response를 구분해야 한다. [G&W p.221]

### E. Limitations

Composite Emax는 하나의 simple sigmoid로 설명되지 않는 response를 두 개 이상의 sub-response로 분리한다. 즉, 관찰된 곡선 하나가 실제 생물학적 process 하나를 의미한다고 단정하지 않는다. Lundström et al. 예시는 `IC50,1=1.8`, `IC50,2=23 µg/L`, `Imax,1=4`, `Imax,2=3.2`, `n1=1.4`, `n2=3.7`을 제시한다. [G&W p.221–223]

Multiple binding site model은 caffeine brain concentration 예처럼 비단조 또는 복합 곡선의 가능성을 보여주지만, 본 세션에서는 “single Hill curve가 모든 생물학을 증명하지 않는다”는 boundary로만 둔다. [G&W p.224]

<!-- TRENCH -->
**[Trench-Level Tip]** Sigmoid Emax fitting은 ordinary Emax/Imax로 먼저 `E0/Emax/EC50` 초기값을 잡은 뒤 `n=1`에서 시작한다. PD3처럼 error가 커지면 `n` precision이 악화될 수 있으므로 “폭발” 같은 표현 대신 CV와 sensitivity analysis로 말한다. [G&W p.738–739] `[실무 구현 번역]`

**[Trench-Level Tip]** `[실무 구현 번역]` `Range-Starved Hill`은 농도 범위가 `IC50` 주변과 upper plateau를 충분히 건드리지 못하는 상황이다. 이때 `n`은 1로 수렴하거나 RSE가 커질 수 있다. 이는 알고리즘 문제가 아니라 design information 부족이다.

### F. Zettelkasten Atom

**Atom C2:** Hill `n`은 기전의 증명이 아니라 concentration-effect curve가 얼마나 급하게 전환되는지를 나타내는 sensitivity lever다. PD3는 그 lever가 모델 선택과 농도범위 설계에 어떻게 연결되는지 보여준다.

<!-- RECAP -->
**Recap:** C2는 “curvature를 본다”는 것이 단순한 시각적 취향이 아니라 dose range, precision, target concentration 해석의 문제임을 고정한다.

> **Practice Lens — [CRUCIBLE_DERIVED]**  
> Hill `n`을 보고 가장 먼저 던질 질문은 “무슨 기전인가?”가 아니라 “이 농도 범위가 `IC50/EC50` 주변과 plateau를 충분히 지나갔는가?”이다. 이 질문을 먼저 통과해야 `n`을 titration sensitivity 또는 model discrimination의 언어로 방어할 수 있다.

> **Failure Mode — [AUDIT_DERIVED]**  
> `n>1`을 positive cooperativity의 증거라고 단정하면 교과서 경계를 넘는다. 보고서 문장에서는 “steepness/flexibility를 설명하는 현상학적 parameter이며 가능한 기전 가설을 제시할 수 있다” 정도로 낮추는 것이 안전하다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, Case Study PD3, p.733 Fig.PD3-3.1; p.735 Table PD3-3.2; p.741 Table PD3-3.4
Why this matters: The key lesson is not merely that a sigmoid model fits better. The original PD3 materials show how concentration range changes model discrimination and parameter precision.
When to look: after reading Card C2 §B and §C-2
Learner instruction: Compare the 0–500 and 0–800 µg/L designs before reading the VIF discussion. Ask whether the data range is wide enough to reveal curvature around IC50 and the upper response region.
<!-- /FIGURE_POINTER -->


---

## Card C3 — Hysteresis: 시간 지연의 진단 도구


<!-- MASTER LENS -->
### [개념 Big Idea]

Hysteresis(← 같은 농도에서도 시간 방향에 따라 효과가 달라지는 현상)는 단순히 “농도와 효과가 다르게 움직인다”는 현상이 아니다. Plasma concentration이 site-of-action 또는 downstream response를 즉시 대표하지 못한다는 진단 신호다. R&T Ch.8은 time이 항상 고려되어야 한다고 시작하며, single dose 후 response가 plasma concentration을 따라가지 않는 사례를 제시한다. [R&T p.233–235]

<!-- ANNOTATION -->
즉, hysteresis는 그림의 잡음이 아니라 model structure를 바꾸라는 신호다.

### A. Formal Definition

Hysteresis는 concentration이 rising phase에 있을 때와 falling phase에 있을 때 concentration-response path가 달라지는 현상이다. Oral naproxen 500 mg dental pain model에서 unbound plasma concentration과 mean pain relief를 직접 plotting하면 counterclockwise loop가 나타난다. 같은 농도라도 시간 순서가 다르면 effect가 다르게 보인다는 뜻이다. [R&T p.234–235]

### B. Diagnostic Logic

Digoxin 1 mg i.v. bolus 후 첫 4시간 동안 plasma concentration은 감소하지만 left ventricular ejection-time index는 증가한다. 겉으로는 낮은 농도에서 더 큰 효과가 나는 것처럼 보인다. R&T는 cardiac tissue distribution과 receptor binding이 느리므로 plasma-effect 관계를 해석하려면 약 6시간의 distribution equilibrium을 기다려야 한다고 설명한다. [R&T p.234]

Naproxen 500 mg oral 예시는 시간-농도/효과 plot에서는 delay가 약하게 보이지만, effect를 unbound concentration에 직접 plot하면 loop가 명확해진다는 점을 보여준다. [R&T p.234–235]

### C. Structural Necessity

Counterclockwise hysteresis는 보통 effect가 plasma보다 늦는 상황이다. 원인은 크게 두 축으로 나뉜다.

1. **Kinetic delay:** drug가 site of action에 늦게 도달하거나 slow binding/dissociation을 보인다. [R&T p.235–238]
2. **Dynamic delay:** measured response가 downstream compartment나 turnover system에 의해 늦게 변한다. [R&T p.236–244]

### D. Assumptions & Boundary Conditions

- Plasma concentration이 site concentration을 즉시 대표하지 못할 수 있다.
- Measured endpoint가 target engagement에 가까울수록 delay가 작고, downstream response일수록 delay가 커진다. [R&T p.236–238]
- Counterclockwise loop는 delay를 말하지만, delay의 원인이 distribution인지 turnover인지는 별도 진단이 필요하다.

### E. Limitations

Sampling이 sparse하면 hysteresis loop의 방향과 폭이 왜곡될 수 있다. 또한 placebo correction, baseline drift, endogenous rhythm이 있으면 concentration-response loop를 causal path로 과해석하면 안 된다. 이 경우 loop는 진단 단서이지 최종 mechanism proof가 아니다. [R&T p.244]

<!-- TRENCH -->
**[Trench-Level Tip]** Hysteresis loop를 보면 먼저 (1) loop width가 drug half-life의 몇 배인지, (2) peak effect time이 dose-dependent인지 확인한다. Peak time이 dose-dependent이면 effect compartment 가능성이 커지고, dose-invariant이면 turnover/indirect response 쪽으로 기운다. `[실무 구현 번역]`

### F. Zettelkasten Atom

**Atom C3:** Hysteresis는 모델 선택 전에 보는 EDA diagnostic이다. 농도-효과 loop는 “어떤 link function을 쓸 것인가”보다 먼저 “plasma가 effect site를 대표하는가”를 묻는다.

<!-- RECAP -->
**Recap:** C3는 시간 지연을 그림으로 감지하는 단계이며, C4의 effect compartment와 indirect response는 이 지연을 구조적으로 흡수하는 방식이다.

> **Mastery Note — [TEXTBOOK_DERIVED]**  
> Hysteresis plot은 단순한 시각화가 아니라 모델 선택의 triage 도구다. 시간-농도/효과 plot에서 지연이 애매해도 concentration-response loop가 생기면, plasma가 causal biophase를 즉시 대표한다는 가정을 내려놓아야 한다.

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.234 Fig.8-1; p.235 Fig.8-2
Why this matters: Hysteresis cannot be fully understood as prose. The visual loop shows why the same plasma concentration can correspond to different response values depending on whether concentration is rising or falling.
When to look: after reading Card C3 §A–B
Learner instruction: In Fig.8-2, follow the chronological sampling numbers around the loop. Focus on the fact that concentration-response is path-dependent, not a single static curve.
<!-- /FIGURE_POINTER -->


---

## Card C4 — Effect Compartment + Systems-in-flux / Indirect Response


<!-- MASTER LENS -->
### [개념 Big Idea]

C4의 첫 질문은 “response가 plasma concentration에 늦게 따라오는가?”가 아니다. 진짜 질문은 **delay가 site-of-action equilibration 때문인가, 아니면 biological system turnover 때문인가?**이다. 전자라면 effect compartment가 더 자연스럽다. 후자라면 indirect response / systems-in-flux가 더 자연스럽다. [R&T p.245–248]

### A. C4a. Effect Compartment

Effect compartment(← plasma와 response 사이 지연을 흡수하는 가상 구획)는 plasma concentration과 response를 연결하기 위해 도입한 hypothetical compartment다. R&T는 naproxen hysteresis를 effect compartment를 통해 줄이고, effect-site concentration과 response를 더 직접적으로 연결하는 그림을 제시한다. [R&T p.245–246]

이 compartment는 microscopic organ compartment가 아니라 lumped delay representation(← 여러 지연 원인을 하나로 묶은 표현)이다. Tissue perfusion, permeability, tissue affinity, binding kinetics, signal transduction lag가 합쳐져 보일 수 있다. 따라서 `ke0`를 특정 생리상수처럼 외삽하지 않는다. [R&T p.235–236, p.245–246]

### B. C4b. Systems-in-flux / Indirect Response

Systems-in-flux에서는 drug가 endogenous substance 또는 physiological response의 formation/loss process를 바꾼다. Warfarin은 prothrombin complex turnover를 통해 plasma concentration과 effect가 분리되는 대표 예다. Sodium warfarin 1.5 mg/kg oral 투여 후 prothrombin complex response는 turnover half-life 1–2 days의 영향을 받는다. 즉, plasma concentration이 변해도 response는 system recovery 속도에 묶인다. [R&T p.241–248]

General turnover skeleton:

$$
\frac{dR}{dt}=k_{in}-k_{out}R
$$

Drug는 `k_in` 또는 `k_out`을 stimulation/inhibition할 수 있다. 본 식은 G&W non-steady-state response framework와 R&T systems-in-flux 설명을 연결하는 최소 골격이다. [G&W p.229–230; R&T p.241–248]

### C. Structural Necessity

Effect compartment는 plasma와 effect site 사이의 equilibration delay를 흡수한다. Indirect response는 response variable 자체가 느린 turnover를 갖기 때문에 delay가 생긴다. 이 둘을 구분하지 않으면 fit은 비슷해도 외삽이 달라진다. 특히 dose 변경이나 dosing interval 변경에서 차이가 커진다.

<!-- ANCHOR -->
**Dose-invariant peak time diagnostic:** Indirect response에서는 peak가 `dR/dt=0` 조건, 즉 input/output balance에 의해 결정된다. Dose가 response amplitude를 바꿔도 system turnover time scale이 변하지 않으면 peak time이 거의 일정할 수 있다. Effect compartment에서는 dose와 concentration-time profile이 effect-site equilibration의 모양을 바꾼다. 따라서 peak time이 dose-dependent해질 가능성이 크다. `[교과서 기반 개념 + 실무 진단 번역]`

### D. Assumptions

- Effect compartment는 hypothetical link이며 source compartment가 아니다. [R&T p.245]
- Indirect response는 endogenous system의 formation/loss process를 전제로 한다. [R&T p.241–248]
- Warfarin-like response에서는 plasma concentration이 빨리 변해도 response는 prothrombin complex turnover에 의해 느리게 변한다. [R&T p.242, p.247]

### E. Limitations

NONMEM `$DES`, grid search, eta placement는 R&T 원문이 아니라 implementation layer다. 본 Content Lock에서는 모델링 실무로 연결할 때만 `[실무 구현 번역]`이라고 명시한다.

<!-- TRENCH -->
**[Trench-Level Tip]** `[실무 구현 번역]` Hysteresis 모델 선택은 plasma direct → effect compartment → indirect response 순서로 fit한다. 각 단계에서 dose group별 peak time의 dose-dependence가 사라지는지 본다. Effect compartment에서 충분히 사라지면 distribution delay가 주원인이고, indirect response에서만 설명되면 turnover system이 본질이다.

**[Trench-Level Tip]** `[실무 구현 번역]` `PK-Aliased ke0`는 estimated effect half-life가 plasma half-life와 너무 가까워 `ke0`와 elimination rate가 분리되지 않는 패턴이다. 이때 `ke0` 수치 자체보다 dense sampling 또는 sensitivity analysis가 더 중요하다.

### F. Zettelkasten Atom

**Atom C4:** Effect compartment는 “site equilibration delay”, indirect response는 “system turnover delay”다. Hysteresis를 줄이는 fit보다 더 중요한 것은 어떤 delay를 외삽할 것인지의 구조 선택이다.

<!-- RECAP -->
**Recap:** C4는 C3에서 감지한 time lag를 구조화한다. 같은 loop라도 distribution 문제인지 system turnover 문제인지에 따라 dosing interval, onset 예측, special population extrapolation이 달라진다.

> **Practice Lens — [CRUCIBLE_DERIVED]**  
> Effect compartment는 ‘site equilibration delay’를 흡수하고, indirect response는 ‘system turnover delay’를 설명한다. 둘이 모두 fit될 수 있을 때는 peak-time의 dose-dependence, response recovery scale, biological plausibility를 먼저 비교해야 한다.

<!-- FIGURE_SCHEMATIC -->
Title: Delay-source topology: effect-site equilibration vs system turnover
Mode: R
Visual objective: In 5 seconds, the learner should distinguish a plasma-to-effect-site delay from a downstream response-turnover delay.
Core message: Effect compartment and indirect response are not interchangeable delay patches; they encode different causal structures.
Elements to include: Path A with plasma concentration C(t) → effect-site concentration Ce(t) → response E(t); Path B with plasma concentration C(t) → modulation of kin/kout → turnover response R(t); labels for site equilibration delay and system turnover delay; diagnostic callout for peak-time dose-dependence vs dose-invariance.
Elements to exclude: NONMEM code; numerical ke0; dense feedback loops; more than one downstream turnover compartment.
Suggested rendering: Mermaid
Caption: The same delayed response pattern can arise from site equilibration or from biological turnover; model choice determines extrapolation behavior.
Alt text: Two parallel causal paths show plasma concentration leading either to an effect-site compartment and response, or to kin/kout turnover control and delayed response.
Source relation: Redrawn from textbook concept
<!-- /FIGURE_SCHEMATIC -->


---

## Card C5 — AUEC + Duration + PK/PD Rate-Limiting


<!-- MASTER LENS -->
### [개념 Big Idea]

효과 지속 시간은 drug half-life만으로 결정되지 않는다. Plasma concentration이 사라져도 response가 남는 경우는 흔하다. 이때 율속은 PK elimination이 아니라 receptor binding, irreversible action, target turnover, downstream system recovery일 수 있다. [R&T p.249–253]

Methylprednisolone 예시는 PK AUC가 dose-proportional이어도 lymphocyte response는 high-dose 구간에서 saturate될 수 있음을 보여준다. 즉 PK linearity는 PD linearity를 보장하지 않는다. [R&T p.257–258]

### A. Formal Definition

AUEC(← response-time curve의 면적)는 response-time curve를 하나의 면적값으로 요약한 지표다.

$$
AUEC=\int_0^{\infty}E(t)dt
$$

One-compartment first-order elimination과 ordinary Emax model에서 G&W는 다음 closed form을 제시한다.

$$
AUEC=\frac{E_{max}}{K}\ln\left(1+\frac{D}{EC_{50}\cdot V}\right)
$$

`[출처: G&W p.233–234, Eq.3:72–3:73]`

Sigmoid Emax에서는 동일한 closed form이 source에 제시되지 않았다. 따라서 numerical integration 필요성은 `[수학적 추론]`으로만 표시한다.

### B. Duration of Effect

R&T는 response decline의 중간 영역(약 80–20% maximum)에서 response가 시간에 대해 거의 선형적으로 감소할 수 있음을 설명한다. 또한 duration이 dose의 logarithm에 비례하는 관계를 제시한다. [R&T p.249, p.254–256]

$$
t_D=\frac{1}{K}\ln\left(\frac{D}{A_{min}}\right)
$$

Dose를 두 배로 늘리면 조건이 맞을 때 duration은 약 one half-life만큼 증가한다. Succinylcholine 0.5 mg/kg i.v. bolus 예시는 `k≈0.2 min^-1`, t1/2≈4 min의 효과 decline과 dose-duration 관계를 보여준다. 여기서 핵심은 dose 증가가 peak effect보다 duration을 더 읽기 쉽게 바꿀 수 있다는 점이다. [R&T p.249–256]

### C. PK-rate-limited vs PD-rate-limited

- **PK-rate-limited:** effect decline이 plasma concentration decline과 같은 시간 척도에서 움직인다.
- **PD-rate-limited:** plasma concentration은 빠르게 사라지지만 response는 receptor/system turnover에 의해 오래 지속된다.

Aspirin은 650 mg oral 투여 후 plasma t1/2가 약 15 min이지만 antiplatelet activity가 several days 지속되는 예다. 즉, plasma에서 약물이 빨리 사라져도 response system은 더 늦게 회복될 수 있다. [R&T p.251]

Omeprazole은 40 mg oral 후 plasma t1/2가 just less than 1 h이고 약 3 h 후 plasma에는 거의 남지 않지만, gastric acid secretion inhibition은 days 단위로 회복된다. [R&T p.252]

Paclitaxel은 plasma에는 2 days 후 거의 남지 않지만 leukocyte fraction 변화가 weeks scale로 움직이는 예다. [R&T p.253]

Acenocoumarol과 phenprocoumon 비교에서는 acenocoumarol t1/2 15 h, phenprocoumon t1/2 6 days 및 response recovery time 차이가 PK vs PD rate-limiting 판단의 교육적 anchor가 된다. [R&T p.243–244]

### D. Assumptions

- AUEC closed form은 ordinary Emax + first-order elimination 조건에서만 source-grounded다. [G&W p.233]
- Duration log-dose relation은 minimum effective amount, first-order decline, 일정한 threshold 등의 조건을 전제로 한다. [R&T p.254–255]
- PD-rate-limited example은 “약물이 아직 많다”가 아니라 “system이 아직 회복되지 않았다”는 뜻일 수 있다. [R&T p.249–253]

### E. Limitations

Aspirin 75 mg, perioperative 7일 중단, bleeding guideline은 본 PDF source 밖이므로 삭제한다. 이 세션의 source-grounded aspirin statement는 650 mg oral, t1/2 15 min, antiplatelet activity several days까지만이다. [R&T p.251]

Special population dose adjustment에서 PK change만 보고 dosing interval을 정하면 PD-rate-limited 약물에서는 과소 또는 과대 조정이 생길 수 있다. 단, 특정 label/guidance 조항은 본 PDF 범위 밖이다. 따라서 해당 적용은 `[확인 필요 — 교과서 외 규제 적용]`으로 남긴다.

<!-- TRENCH -->
**[Trench-Level Tip]** Plot의 x-axis가 한 자리 이상 다른 시간 단위로 벌어지면 PD-rate-limited 가능성이 크다. Aspirin은 plasma plot이 hours, antiplatelet effect plot이 days scale로 보인다. 따라서 “concentration-driven duration”이라는 직관을 즉시 버려야 한다. [R&T p.251]

**[Trench-Level Tip]** Dose-response가 high-dose에서 평탄해지면 더 높은 dose가 정보를 늘리는 것이 아니라 plateau를 반복 확인할 가능성이 크다. Methylprednisolone처럼 PK AUC는 증가해도 PD response가 포화되면 downstream biomarker 또는 dosing interval endpoint를 다시 설계한다. [R&T p.257–258] `[실무 구현 번역]`

### F. Zettelkasten Atom

**Atom C5:** AUEC와 duration은 concentration-time curve를 response-time curve로 번역한 면적·시간 지표다. Effect persistence는 drug half-life가 아니라 더 느린 process가 결정한다.

<!-- RECAP -->
**Recap:** C5는 “농도가 없어졌는데 효과가 남는다”는 현상을 예외가 아니라 PD 모델링의 핵심 설계 문제로 바꾼다.

> **Failure Mode — [TEXTBOOK_DERIVED]**  
> Effect duration을 plasma half-life만으로 요약하면 PD-rate-limited drug에서 가장 중요한 recovery process를 지워버린다. Duration 또는 AUEC를 보고할 때는 어떤 threshold, 어떤 response variable, 어떤 time scale에서 정의했는지 함께 고정해야 한다.

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.251 Fig.8-20; p.252 Fig.8-21
Why this matters: These examples force the learner to separate plasma half-life from effect duration. The visual time-axis gap is the key structural signal.
When to look: after reading Card C5 §C
Learner instruction: Compare the plasma concentration time course with the response time course. Do not infer aspirin perioperative guidance or omeprazole clinical rules from this figure; use it only to recognize PD-rate-limited persistence.
<!-- /FIGURE_POINTER -->

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.255 Fig.8-23; p.256 Fig.8-24
Why this matters: The duration equation is compact, but the learner must see how dose changes translate into threshold-crossing time. Fig.8-24 anchors the abstract relationship in the succinylcholine example.
When to look: after reading Card C5 §B
Learner instruction: Trace where each dose curve crosses the minimum effective amount/effect threshold. Then connect that crossing time to the statement that dose doubling can extend duration by about one half-life under the stated assumptions.
<!-- /FIGURE_POINTER -->


---

# §5 — Confusion Pair Dissection

## Pair 1 — Kd vs EC50

<!-- CONFUSION -->
| Axis | Kd | EC50 |
|---|---|---|
| 본질 | Binding affinity of drug-target complex | Functional sensitivity of drug + tissue/system |
| 변화 원인 | Ligand-receptor binding 변화 | Binding, receptor density, cascade gain, tissue response 변화 모두 가능 |
| 기억 고리 | “얼마나 잘 붙는가” | “얼마나 적은 농도에서 효과가 반쯤 나는가” |

**Critical correction:** EC50가 covariate에 따라 변하면 그것이 drug-side binding 변화인지 system-side sensitivity 변화인지 구분해야 한다. Unbound concentration과 binding evidence 없이 total EC50 변화만으로 mechanism을 단정하지 않는다. 이 구분이 없으면 covariate effect를 생물학적 sensitivity 변화로 과해석하기 쉽다. [G&W p.203–206, p.215–217]

## Pair 2 — Ordinary Emax (`n=1`) vs Sigmoid Emax (`n≠1`)

<!-- CONFUSION -->
| Axis | Ordinary Emax | Sigmoid Emax |
|---|---|---|
| Curve | Hyperbolic, gradual | Steeper or flatter transition 가능 |
| Parameter | `Emax`, `EC50` | `Emax`, `EC50`, `n` |
| Risk | Plateau 없는 데이터에서 Emax 식별 불안정 | 농도범위가 좁으면 `n` 식별 불안정 |

`n>1`은 “cooperativity 증명”이 아니다. It is a phenomenologic steepness parameter that can suggest hypotheses but does not prove them. [G&W p.216, p.220]

## Pair 3 — PK Rate-Limited vs PD Rate-Limited Decline

<!-- CONFUSION -->
| Axis | PK-rate-limited | PD-rate-limited |
|---|---|---|
| 율속 | Drug elimination/distribution | Receptor binding, irreversible action, turnover, downstream recovery |
| Plot signal | Plasma and response share similar time scale | Plasma time scale and response time scale diverge |
| Examples | Succinylcholine dose-duration under first-order decline | Aspirin, omeprazole, paclitaxel |

**Critical blow:** Drug half-life가 짧다고 effect duration도 짧다고 결론 내리면 PD-rate-limited drug에서 틀린다. Aspirin은 plasma t1/2 약 15 min이지만 antiplatelet activity는 several days 지속된다. Omeprazole도 plasma는 빠르게 사라지지만 acid inhibition은 days scale로 회복된다. 따라서 dosing interval 판단에는 plasma half-life뿐 아니라 response recovery time이 필요하다. [R&T p.251–252]

## Pair 4 — Direct Link / Effect Compartment vs Indirect Response

<!-- CONFUSION -->
| Axis | Direct / Effect Compartment | Indirect Response |
|---|---|---|
| Delay source | Plasma-site equilibration or effect-site concentration | Formation/loss of endogenous response variable |
| Diagnostic | Effect-site concentration로 hysteresis가 줄어듦 | Peak time이 system turnover에 의해 dose-invariant할 수 있음 |
| Risk | `ke0`를 microscopic physiology로 오해 | `kin/kout`을 단순 curve-fitting parameter로 오해 |

**Fast diagnostic:** hysteresis loop의 폭과 peak effect time의 dose-dependence를 먼저 본다. Dose-dependent peak time이면 effect compartment 가능성, dose-invariant peak time이면 indirect response 가능성이 커진다. 이 판단은 fit statistic보다 먼저 보는 구조 진단이다. `[실무 구현 번역]`

<!-- RECAP -->
**Recap:** 가장 위험한 혼동은 “농도가 response를 즉시 drive한다”는 가정이다. 이 가정이 깨지는 순간 Kd/EC50, Emax/Hill, effect compartment/indirect response, PK/PD rate-limiting이 모두 연결된다.

> **Mastery Note — [EXPERT_INFERENCE]**  
> 네 개의 confusion pair는 모두 같은 질문으로 환원된다: “현재 숫자는 binding, site concentration, measured response, system recovery 중 어느 층위를 대표하는가?” 이 층위를 분리하면 parameter naming은 단순 암기가 아니라 모델 구조 검토가 된다.

---

# §7 — Self-Test: Active Recall Module

<!-- SELF-TEST -->
## Q1. Law of Mass Action에서 Emax 식을 도출하라.

**Prompt:** `d[RC]/dt = k1[R][C] - k-1[RC]`와 `[R_T]=[R]+[RC]`에서 `E = Emax·C/(Kd+C)`를 도출하라.

**Answer key:** 평형에서 `k1[R][C]=k-1[RC]`, `Kd=[C][R]/[RC]`. `[R]=[R_T]-[RC]`를 대입하면 `[RC]/[R_T]=C/(C+Kd)`. 여기에 `E=α[RC]`, `Emax=α[R_T]`를 대입하면 `E/Emax=C/(C+Kd)`가 된다. [G&W p.202–204]

## Q2. Kd와 EC50가 다른 이유를 한 문장으로 설명하라.

**Answer key:** Kd는 receptor binding affinity이고 EC50는 receptor occupancy 이후 tissue transduction과 response amplification까지 포함하므로, spare receptor/cascade가 있으면 EC50는 Kd와 달라질 수 있다. [G&W p.204–206]

## Q3. Hill `n=2.03`을 “cooperativity 증거”라고 쓰면 왜 틀리는가?

**Answer key:** G&W는 Hill exponent가 direct biological interpretation을 갖지 않는다고 설명한다. `n=2.03`은 PD3 데이터의 steepness를 설명하는 parameter이며, cooperativity는 가능한 hypothesis일 뿐 proof가 아니다. [G&W p.216, p.220, p.735]

## Q4. Sigmoid inhibitory Imax model에서 target response를 해석할 때 baseline-relative와 absolute response를 구분하라.

**Prompt:** `E = E0 - Imax·C^n/(IC50^n+C^n)`에서 target `E_target`이 주어졌을 때 어떤 값을 inhibition fraction으로 넣어야 하는가?

**Answer key:** Absolute response로 주어진 `E_target`은 먼저 `I = E0 - E_target`으로 inhibition magnitude를 계산한다. 그 다음 `I/Imax`를 fraction으로 두고 concentration을 역산한다. Baseline-relative response를 absolute response처럼 넣으면 부호와 비율이 틀어진다. [G&W p.218–221]

## Q5. Naproxen hysteresis에서 unsupported `ke0` 수치를 쓰지 말고, source-grounded conclusion만 말하라.

**Answer key:** R&T는 naproxen 500 mg oral dental-pain model에서 unbound concentration과 pain relief가 counterclockwise hysteresis를 보이고, effect compartment가 이 hysteresis를 줄이는 conceptual model을 제시한다. `ke0≈0.5–1 hr^-1` 수치는 본 PDF 범위에서 확인되지 않으므로 쓰지 않는다. [R&T p.234–246]

## Q6. Warfarin response가 plasma concentration을 즉시 따라가지 않는 이유는 무엇인가?

**Answer key:** Warfarin effect는 prothrombin complex turnover에 의해 나타나므로 plasma concentration 변화와 response 변화가 분리된다. R&T는 sodium warfarin 1.5 mg/kg oral 후 prothrombin complex activity가 system turnover half-life의 영향을 받는 예를 제시한다. [R&T p.242, p.247]

## Q7. AUEC closed form의 적용 조건을 말하라.

**Answer key:** G&W의 `AUEC = Emax/K · ln(1 + D/(EC50·V))`는 ordinary Emax와 first-order elimination 조건에서 source-grounded하다. Sigmoid Emax의 AUEC numerical integration은 합리적 수학 추론이지만 본문에 closed form으로 제시된 source 사실은 아니다. [G&W p.233–234]

## Q8. Aspirin과 omeprazole 예시로 PD-rate-limited duration을 설명하라.

**Answer key:** Aspirin 650 mg oral은 plasma t1/2가 약 15 min이지만 antiplatelet activity가 several days 지속된다. Omeprazole 40 mg oral은 plasma t1/2가 just less than 1 h이고 약 3 h 후 plasma가 거의 사라지지만 acid suppression은 days scale로 회복된다. 두 예시는 effect duration이 drug half-life가 아니라 system/receptor recovery에 의해 제한될 수 있음을 보여준다. [R&T p.251–252]

## Q9. Boss Dilemma — Phase 2 PK/PD dataset에서 counterclockwise hysteresis가 보인다. Plasma direct, effect compartment, indirect response 중 어떤 순서로 검토할 것인가?

**Answer key:** 먼저 plasma direct model로 misspecification의 크기를 본다. 다음 effect compartment를 적용해 hysteresis가 줄어드는지 확인한다. 그래도 dose group별 peak time이 dose-invariant하거나 response recovery가 system time scale을 보이면 indirect response를 검토한다. 즉, 모델 선택은 AIC만으로 하지 않는다. Dose-dependence of peak time, sampling density, biological plausibility를 함께 본다. `[실무 구현 번역]`

---

# §8 — Meta-Frame & Big Picture

## A. Positioning & Failure Modes

이 세션은 PK/PD architecture에서 “concentration-time profile을 response-time profile로 변환하는 첫 관문”이다. C1–C2는 concentration-response nonlinearity를 담당한다. C3–C4는 time delay를, C5는 response integration/duration을 담당한다.

이 세션을 대충 넘기면 다음 실패가 발생한다.

1. **Kd를 EC50처럼 사용:** binding affinity를 functional potency로 오인한다.
2. **Hill `n`을 mechanism proof로 과해석:** curve fitting parameter를 biological evidence로 둔갑시킨다.
3. **Hysteresis를 noise로 처리:** site equilibration 또는 turnover delay를 놓친다.
4. **PK half-life로 dosing interval을 결정:** PD-rate-limited response에서 duration을 잘못 예측한다.
5. **AUEC를 단순 AUC처럼 취급:** response integration의 모델 조건을 잊는다.

## B. Professional Moat

Pharmacometrician의 moat는 복잡한 식을 많이 아는 데 있지 않다. 같은 concentration-effect 데이터를 보고 부족한 것이 무엇인지 구분하는 데 있다. 더 좋은 optimizer가 필요한가, 더 넓은 concentration range가 필요한가, 더 가까운 biomarker가 필요한가, 더 긴 response sampling이 필요한가를 판단해야 한다.

PD3는 이 moat의 좋은 예다. 0–500 µg/L design에서는 sigmoid superiority가 명확하지 않다. 그러나 0–800 µg/L design은 model discrimination을 가능하게 한다. 이는 model selection이 통계기법 문제만이 아니라 experimental design 문제임을 보여준다. [G&W p.734–741]

R&T Ch.8은 또 다른 moat를 준다. Plasma concentration이 낮아졌는데 effect가 남아 있을 때 “약물이 없는데 효과가 이상하게 남았다”고 보지 않는다. 대신 “system turnover 또는 irreversible action이 더 느린 process인가?”를 묻는다. [R&T p.249–253]

## C. Boundary Flags Preserved

[확인 필요 — 첨부 PDF 미포함 구간]:
- G&W §3.6.2–§3.6.5 (pp.225–228): competitive antagonism 이후 interaction model 연속부. 본 세션에서 추정·보완하지 않음.
- G&W §3.12 baseline modeling: C2 limitation에서 baseline time-varying issue로만 언급. 본 세션에서 상세 모델링 보류.
- `[확인 필요 — 교과서 외 규제 적용]`: PD-rate-limited drug의 special population dose adjustment나 FDA guidance 문구는 본 PDF 범위 밖이므로 일반 원칙으로만 유지.

<!-- RECAP -->
**Final Recap:** 이 세션의 압축 결론은 세 문장이다.  
1. Emax/Hill 모델은 receptor binding에서 시작하지만 response system을 포함한다.  
2. Hysteresis는 plasma concentration이 effect를 즉시 대표하지 못한다는 시각적 경고다.  
3. Duration과 AUEC는 drug half-life보다 더 느린 biological process를 찾아야 제대로 해석된다.

> **Practice Lens — [EXPERT_INFERENCE]**  
> 이 세션을 HTML로 학습할 때 최종 목표는 식을 외우는 것이 아니라 “이 데이터로 어떤 질문은 방어 가능하고, 어떤 질문은 아직 설계가 부족한가?”를 말할 수 있게 되는 것이다. `Emax/Hill`, hysteresis, AUEC는 모두 모델 결과가 아니라 study design의 충분성을 되묻는 언어다.

---

## PART B — Compiler-Only Appendix

This appendix is not learner-facing. It exists only to protect Phase 5 rendering fidelity.

### B1. Compilation Contract

- PART A is the only learner-facing body.
- Phase 5 must render PART A without altering the scientific content, equations, page tags, figure marker content, or mastery-note labels.
- PART B is instruction/guardrail only and must not appear as learner content unless explicitly requested.
- Do not restore deprecated material from Step 1 Draft v0.
- Do not add new scientific content, new examples, new page tags, new figures, or new regulatory claims during HTML compilation.
- Do not generate HTML, Mermaid, or SVG at Phase 4D; Phase 5 handles rendering.

### B2. Figure Rendering Instructions

**Image rights:** None. Do not embed copyrighted textbook figures. Render `FIGURE_POINTER` as text-only callouts. Render `FIGURE_SCHEMATIC` as structurally distinct redraws based only on the brief.

| # | Mode | Source | Phase 5 action | Decision |
|---|---|---|---|---|
| 1 | P | G&W p.199 Fig.3.1 | Text-only textbook pointer | KEEP |
| 3 | R | G&W p.204 Fig.3.4; p.205 Fig.3.5 | Structurally distinct schematic brief | KEEP |
| 5 | P | G&W PD3 p.733 Fig.PD3-3.1; p.735 Table PD3-3.2; p.741 Table PD3-3.4 | Text-only textbook pointer | KEEP |
| 6 | P | R&T p.234 Fig.8-1; p.235 Fig.8-2 | Text-only textbook pointer | KEEP |
| 7 | R | R&T p.236 Fig.8-3 | Structurally distinct schematic brief | KEEP |
| 8 | P | R&T p.251 Fig.8-20; p.252 Fig.8-21 | Text-only textbook pointer | KEEP |
| 9 | P | R&T p.255 Fig.8-23; p.256 Fig.8-24 | Text-only textbook pointer | KEEP |
| 2 | P | G&W p.202 Fig.3.3 | Rejected as redundant within C1 budget | REJECT |
| 4 | P | G&W p.213 Fig.3.12; p.216 Fig.3.16 | Rejected as lower ROI than PD3 | REJECT |
| 10 | N | None | Rejected due to budget and drift control | REJECT |

Additional constraints:

- Preserve P/R/N/I decisions and all Source fields in marker blocks.
- Do not propose or generate new figures.
- Do not render rejected figure candidates #2, #4, or #10.
- Place rendered figures at the end of the relevant concept card unless the marker position already makes a safer local placement obvious.
- For redrawn schematics, preserve conceptual relation but avoid the textbook’s exact layout, color palette, and figure composition.

### B3. Page Tag Rendering Rules

- Preserve all existing `[p.XX]`, `[pp.XX–YY]`, `[pp.XX, YY]`, and `[p.확인 필요]` tokens.
- Do not fabricate, delete, renumber, or relocate page tags.
- Apply page-tag wrapping only to body text; do not wrap tags inside code blocks or inside `FIGURE_*` marker blocks.
- Source page tags must remain visible in print mode.
- `[확인 필요 — 첨부 PDF 미포함 구간]` remains visible unless a later verified source explicitly resolves it.

### B4. HTML Compiler Requirements

#### Marker-to-component mapping

| Marker / Pattern | HTML Component | Required handling |
|---|---|---|
| `<!-- MASTER LENS -->` | Callout box | border-left gold; low-opacity gold background |
| `<!-- ANNOTATION -->` | Inline annotation / tooltip style | muted italic small text |
| `<!-- ANCHOR -->` | Bridge sentence | muted italic text |
| `<!-- TRENCH -->` | Practical tip box | rose-left-border callout |
| `<!-- CONFUSION -->` | Side-by-side comparison | amber comparison component |
| `<!-- SELF-TEST -->` | Accordion | prompt visible; answer hidden until click |
| `<!-- RECAP -->` | Recap box | blue-left-border summary |
| `[확인 필요]` | Highlighted flag | render with `<mark>` |
| `[p.XX]`, `[pp.XX–YY]`, `[pp.XX, YY]` | Inline source-page tag | wrap in `<span class="source-page">…</span>` |
| `[p.확인 필요]` | Uncertain source tag | wrap in `<span class="source-page source-uncertain">…</span>` |
| `<!-- FIGURE_POINTER -->` | Text-only textbook reference callout | never embed textbook image |
| `<!-- FIGURE_SCHEMATIC -->` | Inline schematic `<figure>` | generate visually distinct Mermaid/SVG/CSS from brief only |
| `<!-- FIGURE_IMAGE_SLOT -->` | Image/placeholder figure | not used in this session unless user-supplied/open-license file exists |

#### Rendering, navigation, interaction, and output requirements

- Render PART A only as learner-facing content; do not render PART B unless explicitly requested.
- Produce one self-contained HTML file with inline CSS/JS.
- Preserve text content; do not rewrite scientific body, equations, examples, or page tags.
- MathJax: support inline and display equations.
- Navigation: sticky left sidebar TOC on desktop; mobile-collapse allowed; each major § heading and each §2 concept card should have stable unique ids.
- Navigation anchor integrity: every sidebar `href="#id"` must match exactly one body `id`; no duplicate ids; `html { scroll-behavior: smooth; }` must be present.
- Self-test: render answer keys hidden by default and revealed on user click.
- Controls: code-copy button where code exists, print/PDF button via `window.print()`.
- Responsive/print: ≤768px single-column; hide navigation in print; preserve source-page tags in print.
- Figure pointers: render as text-only callouts with Source / Why this matters / When to look / Learner instruction.
- Figure schematics: render from brief only; do not reproduce textbook layout, color scheme, or exact figure.
- Mermaid self-check: use valid Mermaid syntax only; if node labels/special characters make Mermaid fragile, fall back to inline SVG or CSS cards.
- Allowed external runtime dependencies only: MathJax CDN, Mermaid CDN, and permitted highlighting libraries; no external local CSS/JS/font/image files.
- Prohibited: iframe/embed, unauthorized textbook images, visible self-test answers by default, raw markers left unrendered, raw page tags left unwrapped, duplicate/unstable ids, unmatched TOC targets, new figure ideas, or new scientific content.

### B5. Audit Guardrails

Do not restore or add any of the following:

- “5–100배 오차,” FIH dose overprediction, NDA recommended dose, FDA deficiency letter, clinical hold, or similar regulatory claims as source-derived statements.
- Hill `n` as direct proof of cooperativity, cascade, receptor-effector heterogeneity, or a named mechanism without orthogonal evidence.
- Aspirin 75 mg, 7–10 days, perioperative stopping rules, or bleeding-guideline claims; source scope supports aspirin 650 mg, plasma t1/2 about 15 min, antiplatelet effect several days only.
- Naproxen `ke0 ≈ 0.5–1 hr⁻¹` or any unverified effect-compartment numeric range.
- Untagged NONMEM `$DES`, grid-search, IIV-on-EC50/Emax/n, reviewer-deficiency, or submission consequences as textbook facts.
- G&W §3.6.2–§3.6.5 content from pp.225–228; keep `[확인 필요 — 첨부 PDF 미포함 구간]` rather than reconstructing.
- New page tags, new named drug examples, unapproved code blocks, unapproved figures, or copyrighted textbook image embedding.

### B6. Crucible Guardrails

- Crucible is a judgment/insight source, not a raw learner-prose source at Phase 4D.
- Preserve only adopted or explicitly allowed Grade A logic: Hill `n` as titration/design lever, IDR peak-time diagnostic logic, `ke0` as lumped/phenomenologic delay, PD3 concentration-range design lesson, and PK/PD rate-limiting as a relative time-scale problem.
- Do not turn expert inference into textbook-derived fact.
- Do not add unsupported numeric expert claims from Crucible unless already present in Content Lock v2 and properly tagged.
- Do not reintroduce lower-priority, speculative, external, or rejected Crucible material.

### B7. Deprecated and Forbidden Restorations

- Step 1 Draft v0 is deprecated and must not be used as a learner-body source except through the Micro-Patch Gate.
- Content Lock v1 is superseded by Content Lock v2 and must not override the v2 body.
- Phase 1 Patch Memo is contextual only; it must not override Audit v1 or Content Lock v2.
- Do not restore rejected overclaims, unsupported numbers, unsupported regulatory claims, source-unsupported examples, unapproved code, unapproved figures, or any NOT_IN_SOURCE item rejected by Audit/Content Lock.

### B8. PATCH MODE Splice Verification Table

| Marker # | Anchor text | Anchor found? | Match count | Inserted? | Final location (§ + card) |
|---|---|---|---|---|---|
| 1 | # §1 — Session Header & Roadmap | YES | 1 | YES | §1 — Session Header & Roadmap |
| 2 | ## Card C1 — Law of Mass Action → Emax 골격 | YES | 1 | YES | §2 / Card C1 |
| 3 | ## Card C2 — Sigmoid Emax / Hill Model [Apex] | YES | 1 | YES | §2 / Card C2 |
| 4 | ## Card C3 — Hysteresis: 시간 지연의 진단 도구 | YES | 1 | YES | §2 / Card C3 |
| 5 | ## Card C4 — Effect Compartment + Systems-in-flux / Indirect… | YES | 1 | YES | §2 / Card C4 |
| 6 | ## Card C5 — AUEC + Duration + PK/PD Rate-Limiting | YES | 1 | YES | §2 / Card C5 |
| 7 | ## Card C5 — AUEC + Duration + PK/PD Rate-Limiting | YES | 1 | YES | §2 / Card C5 |

### B9. Zero-Omission Coverage Matrix

| Domain | Required item | Evidence in PART A | Status | Action |
|---|---|---|---|---|
| C1 Scope Lock Required Concepts | C1 Mass Action/Emax; C2 Sigmoid Emax/Hill; C3 Hysteresis; C4 Effect Compartment/IDR; C5 AUEC/Duration | PART A §1 roadmap and §2 C1–C5 cards | PRESENT | None |
| C2 Scope Lock Required Data Anchors | PD3 E0/Imax/IC50/n; Lundström composite Imax values; R&T examples including digoxin, naproxen, warfarin, aspirin, omeprazole, succinylcholine | PART A C2, C3, C4, C5 and self-test Q5–Q8 | PRESENT | None |
| C3 Audit MUST_FIX | Unsupported 5–100×/FIH/NDA claims removed; Hill n mechanism proof downgraded; aspirin/naproxen/NONMEM regulatory overclaims controlled | PART A C1–C5, §5, §7; PART B guardrails | PRESENT | Regression forbidden in PART B |
| C4 Audit T5 Coverage | Ideal PD measure, control + 2–4 dose levels, missing author messages, design range, source-supported examples | PART A §1 and C2/PD3; C5 examples | PRESENT | None |
| C5 Figure Coverage | Phase 4C KEEP items #1, #3, #5, #6, #7, #8, #9 | PART A contains 5 FIGURE_POINTER and 2 FIGURE_SCHEMATIC markers exactly once | PRESENT | No image embedding; rejected #2/#4/#10 not restored |
| C6 Page Tag Integrity | Preserve G&W/R&T page tags and uncertainty flags | PART A inherited v2 source tags; B3 enforces rendering without fabrication | PRESENT | No new page tags added |
| C7 Crucible Grade A Preservation | Dose-invariant peak time, Hill n as titration lever, ke0 as lumped delay, PD3 design range, PK/PD rate-limiting ratio | PART A C2/C4/C5 plus mastery notes; no unsupported numeric expert claims added | PRESENT_COMPRESSED | Preserved as bounded interpretation |
| C8 Deprecated Draft Regression | Step 1 rejected material not restored | PART A uses Content Lock v2 base; B5/B7 prohibit restorations | PRESENT | None |
| C9 Canonical Body Integrity | Content Lock v2 learner body retained with approved 4C markers plus labeled augmentations | PART A §1–§8; B8 splice verification | PRESENT | No broad rewrite |

### B10. Micro-Patch Log

No micro-patches needed. PART A equals the learner portion of Content Lock v2 spliced with approved Phase 4C figure markers, plus the separately labeled Mastery Augmentation Layer. No source page tags were added or changed.

### B11. Mastery Augmentation Log

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
|---|---|---|---|---|---|---|
| 1 | §2 / Card C1 | J | True | AUDIT_DERIVED | Kd–EC50 혼동 및 total/unbound 해석 과잉을 예방 | Low |
| 2 | §2 / Card C2 | J/F | True | CRUCIBLE_DERIVED + AUDIT_DERIVED | Hill n의 해석 경계와 설계 판단을 고정 | Low |
| 3 | §2 / Card C3 | M | True | TEXTBOOK_DERIVED | R&T hysteresis figure의 진단적 의미를 학습 동선으로 고정 | Low |
| 4 | §2 / Card C4 | J | True | CRUCIBLE_DERIVED | Effect compartment와 indirect response의 topology 구분을 강화 | Low |
| 5 | §2 / Card C5 | F | True | TEXTBOOK_DERIVED | AUEC/duration 정의와 PD-rate-limiting 오해 예방 | Low |
| 6 | §5 / Confusion Pair Dissection | M | True | EXPERT_INFERENCE | 혼동쌍을 하나의 층위 분리 mental model로 통합 | Medium |
| 7 | §8 / Meta-Frame | W | True | EXPERT_INFERENCE | 세션 전체를 모델링/설계 판단으로 연결 | Medium |

#### Rejected or Deferred Augmentation Candidates

| Rejected candidate | Reason for rejection |
|---|---|
| Reintroduce “5–100× FIH/NDA” warning | Rejected: Audit classifies direct support as NOT_IN_SOURCE for this PDF scope |
| Add new clinical dosing/guideline examples for aspirin or omeprazole | Rejected: would add external clinical guidance beyond source pages |
| Add numerical ke0 range for naproxen or effect compartment examples | Rejected: Audit identifies the specific naproxen ke0 range as unsupported in the PDF |
| Add new Mermaid/SVG code in Phase 4D | Rejected: Phase 4D may include briefs/markers only; Phase 5 renders visuals |


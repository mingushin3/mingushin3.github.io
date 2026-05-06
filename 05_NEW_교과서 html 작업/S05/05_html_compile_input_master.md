# 05_HTML Compile Input Master

## Phase 4D Certification

| Certificate | Status | Basis |
|---|---|---|
| Learner-Standalone Certificate | PASS | PART A starts at learner-facing §1, excludes audit/compiler/process tables, and contains the complete spliced study handout. |
| Zero-Omission Certificate | PASS | Scope, Audit, Crucible, Content Lock v2, PDF anchors, and Phase 4C marker coverage were checked; no unresolved high-impact omission remains. |
| Mastery-Uplift Certificate | PASS | Five bounded expert-synthesis augmentations were inserted adjacent to M1–M5 without rewriting canonical scientific content. |
| Source-Boundary Certificate | PASS | All augmentations are explicitly labeled EXPERT_INFERENCE/source-bound synthesis and add no new page tags, numbers, drugs, or external claims. |
| HTML-Readiness Certificate | PASS | PART B includes compilation contract, marker mapping, page-tag rules, figure rules, navigation-anchor integrity rules, and guardrails for Phase 5. |

## Assembly Mode

**PATCH MODE** — `05_Content Lock v2.1(2).md` is a Figure Marker Patch / Insertion Map, not a full marked body. The learner body was constructed by taking the learner-facing §1–§8 body from `05_Content Lock v2(2).md`, removing only non-learner process carry-forward text, inserting seven approved Phase 4C figure markers at exact card-end anchors, and adding five visibly labeled mastery-augmentation blocks.

## Input Manifest

| File | Role | Authority level | Used for | Notes |
|---|---|---|---|---|
| `05_scope_lock(4).md` | scope boundary | A0 | Required scope, source range, learner, image rights, chapter role | All MUST concepts checked against this boundary |
| `05_G_2구획 모델 α:β·재파라미터화(4).pdf` | PDF verification source | A1 | G&W equations, figures, PK7/PK8 anchors | 34-page PDF present; no image embedded |
| `05_T_2구획 모델 α:β·재파라미터화(4).pdf` | PDF verification source | A1 | R&T distribution kinetics, clinical examples, volume/half-life anchors | 44-page PDF present; no image embedded |
| `05_Audit_Report_v1(3).md` | audit guardrail | A2 | MUST/SHOULD fixes, source-fidelity regression prevention | Used as mandatory correction and forbidden-restoration source |
| `05_Content Lock v2(2).md` | canonical body | A3 | Base learner body | Process/adjudication preamble excluded from PART A; §1 onward used |
| `05_Content Lock v2.1(2).md` | figure insertion source | A4 | PATCH MODE figure plan, insertion map, marker blocks | 7 approved markers inserted exactly once |
| `05_crucible_report_v1(1).md` | crucible guardrail | A5 | Adopted internalization and practical-risk insights | Used only through already-adopted Content Lock logic and bounded augmentations |
| `붙여넣은 마크다운(2)(54).md` | compiler instruction | A7 | Prompt 5 rendering requirements, marker mapping, source tag rules, navigation rules | Summarized in PART B |
| `05_step1_draft_v0(2).md` | deprecated source | A6 | Regression check only | Not copied into learner body |
| `S05_phase1_patch memo(3).md` | locked reference / deprecated support | A6 | Audit attention guide | Not directly adopted |
| `05_Content Lock v2_trace(3).md` | locked reference | A3 support | Readability/annotation trace | Used only for traceability |
| `05_Content Lock v1(2).md` | locked reference | A3 predecessor | Historical Content Lock predecessor | Not used as body source |
| `붙여넣은 텍스트 (1)(77).txt` | Phase 4D instruction | controller | Master assembly contract and certification rules | Used to structure this file |

## PART A — Learner-Facing Complete Handout

# Session 05 · 2구획 모델 — 이중지수 분해 / α·β 재파라미터화 / V₁·Vss·Vβ 체계

> **Source:** Gabrielsson & Weiner 5e Ch.2 §2.4.1–2.4.6 + Case Studies PK7/PK8 [G&W pp.57–77, 505–517] + Rowland & Tozer 5e Ch.19 [R&T pp.613–656]  
> **Mode:** A-Critical  
> **Phase 4D note:** Canonical Content Lock v2 body with approved Phase 4C figure markers and bounded mastery augmentation. No HTML, Mermaid, SVG, or textbook image embedding is included here.

## §1 — Session Header & Roadmap

**Session 05 · 2구획 모델: 이중지수 분해와 α·β 재파라미터화**

<!-- MASTER LENS -->
**Big Idea:** 2구획 모델은 “곡선이 두 번 꺾인다”는 관찰을 $A,\alpha,B,\beta$라는 macro-constant<!-- ANNOTATION -->(← 곡선의 절편·기울기 상수)로 분해한다. 그다음 이를 $CL,Q,V_1,V_2$ 또는 $V_c,CL,Cld,V_t$처럼 해석 가능한 좌표계로 다시 옮긴다. 이 좌표계 선택은 단순 notation 문제가 아니라, clearance 추정, volume 해석, covariance stability, multiple-dosing simulation을 동시에 바꾼다. [G&W pp.59–71; R&T pp.615–641]

**개념 항법도:**

```text
M1. 이중지수 + 잔차법
       ↓  두 지수항의 slope/intercept는 무엇을 뜻하는가?
M2. Macro ↔ Micro ↔ Physiological 좌표계
       ↓  어느 좌표계의 V를 임상·모델에 쓸 것인가?
M3. V₁ / Vss / Vβ
       ↓  용적 혼동이 loading dose, amount in body, tissue accumulation을 어떻게 왜곡하는가?
M4. 재파라미터화 5종 + condition number
       ↓  같은 curve라도 왜 어떤 parameterization은 안정하고 어떤 것은 불안정한가?
M5. 분포속도론의 임상 파급
       ↓  terminal half-life가 언제 유용하고 언제 위험한가?
```

<!-- ANCHOR -->
**Workflow anchor:** PopPK covariate model building의 forward inclusion 단계에서는 다섯 카드가 동시에 켜진다. 먼저 $f_2$는 신기능 변화가 어느 phase를 바꿀지 예측한다(M1/M5). 다음으로 좌표계는 covariate를 $CL$에 붙일지 $\beta$에 붙일지 결정한다(M2). $V_{ss}$와 $V_\beta$ 구분은 체중·tissue amount 해석을 좌우하고(M3), condition number/RSE는 그 covariate model을 실제로 유지할 수 있는지 판단한다(M4). [실무 통합]

**선행 지식:** 1구획 IV bolus, $AUC=Dose/CL$, $V_d=CL/k$, MRT/AUMC, linear ODE.

**후속 지식:** NONMEM ADVAN3/4/11/12 선택, sparse sampling design, $\eta$-shrinkage<!-- ANNOTATION -->(← ETA 정보 부족 지표) 해석, 3구획 모델, tissue/target-site PK, clinical multiple-dosing simulation.

<!-- RECAP -->
**이 세션의 한 줄 회수:** 2구획 모델의 본질은 “두 지수항을 외우는 것”이 아니라, **곡선 분해 → 좌표계 변환 → volume 선택 → dosing 해석**을 한 번에 연결하는 것이다.

---

## §2 — Concept Anatomy Cards

### Card M1 — 이중지수 방정식과 잔차법(Method of Residuals)

<!-- MASTER LENS -->
**개념 Big Idea:** IV bolus 뒤 plasma curve가 semilog plot<!-- ANNOTATION -->(← 농도축만 로그인 그래프)에서 하나의 직선이 아니라 두 직선의 합으로 보인다면, 이것은 단순한 시각적 꺾임이 아니다. early phase는 주로 distribution + 일부 elimination, terminal phase는 느린 return/distribution process와 elimination의 합성 결과로 해석해야 한다. 2구획 분석은 이 curve를 “두 phase의 합”으로 분해하는 데서 시작한다. [G&W pp.59–60; R&T pp.615–616]

**Formal definition:**

$$C(t)=A\cdot e^{-\alpha t}+B\cdot e^{-\beta t},\qquad \alpha>\beta>0$$

$A,B$는 zero-time intercept<!-- ANNOTATION -->(← t=0 외삽 절편), $\alpha,\beta$는 phase slope의 절댓값이다. Semilog plot에서 기울기는 각각 $-\alpha$, $-\beta$이고, $C_0=A+B$다. [G&W pp.59–60; R&T pp.615–617]

**잔차법의 핵심 절차:** terminal $\beta$-phase를 먼저 log-linear regression으로 외삽하여 $B e^{-\beta t}$를 얻는다. 그런 다음 초기 관측치에서 이를 빼서 residual curve $C_{resid}(t)=C_{obs}(t)-B e^{-\beta t}$를 만든다. 이 residual이 semilog에서 직선이면 그 기울기가 $-\alpha$, 절편이 $A$다. [G&W p.60; R&T p.616]

**G&W Fig.2.43 anchor:** $A\approx70$, $B=28$, $\alpha=\ln(70/10)/130=0.0150\ \text{min}^{-1}$, $\beta=\ln(28/10)/450=0.00229\ \text{min}^{-1}$로 제시된다. Source figure/caption의 단위 표기가 혼재되어 보이므로 최종 시각화 단계에서는 `[단위 확인 필요]`를 유지한다. [G&W p.60]

**Secondary parameters:**

$$AUC_0^\infty=\frac{A}{\alpha}+\frac{B}{\beta},\qquad
AUMC_0^\infty=\frac{A}{\alpha^2}+\frac{B}{\beta^2}$$

$$t_{1/2,\alpha}=\frac{\ln2}{\alpha},\qquad t_{1/2,\beta}=\frac{\ln2}{\beta}$$

$$f_1=\frac{A/\alpha}{AUC},\qquad f_2=\frac{B/\beta}{AUC},\qquad f_1+f_2=1$$

$f_2$가 크면 terminal phase가 elimination interpretation에 가까워진다. 반대로 $f_2$가 작으면 terminal slope는 elimination보다 redistribution을 더 많이 반영할 수 있다. [G&W p.63; R&T pp.622–623]

<!-- TRENCH -->
**Trench tip:** 잔차법은 production NONMEM 알고리즘이 아니다. 종이에서 curve-stripping을 손으로 하는 이유는 simultaneous nonlinear regression에 넣을 initial estimate 감각을 얻기 위해서다. [실무 확장]

**Structural necessity:** 2구획 central/peripheral amount ODE는 다음과 같다.

$$\frac{dA_1}{dt}=-(k_{12}+k_{10})A_1+k_{21}A_2$$

$$\frac{dA_2}{dt}=k_{12}A_1-k_{21}A_2$$

[수학적 해석] 선형 상수계수 2×2 ODE의 해가 두 지수항의 합으로 나타나기 때문에, $\alpha$와 $\beta$는 이 system matrix에서 유래한다. 따라서 $\alpha+\beta=k_{12}+k_{21}+k_{10}$, $\alpha\beta=k_{21}k_{10}$ 관계가 생기며, macro 4개는 임의로 움직이는 4개 숫자가 아니라 micro-parameter space의 제약을 반영한다. [G&W pp.61–62; R&T pp.618–619]

**그래프를 볼 때 3초 checklist:** knee가 어디 있는가($\alpha/\beta$), 두 phase의 면적 비율이 어느 쪽으로 기우는가($f_1/f_2$), terminal line이 정말 직선인가(3구획 가능성). [G&W p.63; R&T p.632]

**Aspirin warning:** R&T의 aspirin 650 mg IV bolus 예시는 early sampling을 놓치면 terminal-only one-compartment 해석으로 $CL=0.98$ L/min을 얻게 되지만, biexponential 해석에서는 $CL=683$ mL/min이다. 즉 terminal-only one-compartment 해석은 CL을 약 44% overestimate하고, 이로부터 maintenance dose를 계산하면 과대평가 위험이 있다. [R&T pp.615–620]

**Boundary conditions:** linear kinetics, central에서의 빠른 mixing, distribution phase sampling, mammillary structure, central elimination assumption이 필요하다. 이 조건이 깨지면 bi-exponential fit은 가능해도 physiological interpretation은 흔들린다. [G&W pp.57–65; R&T pp.617–619]

<!-- RECAP -->
**Recap:** M1에서 기억할 것은 “$A,\alpha,B,\beta$를 구하라”가 아니라, **곡선을 phase별로 분해한 뒤 각 phase가 AUC와 elimination interpretation에 얼마나 기여하는지 읽는 것**이다.


> **[MASTER AUGMENTATION — EXPERT_INFERENCE | source-bound synthesis]** Semilog curve-stripping을 ‘계산법’으로만 보지 말고, sampling adequacy를 진단하는 lens로 읽는다. early point가 없으면 \(A,\alpha\)가 약해지고, terminal line이 휘면 2구획 자체가 부족할 수 있으며, \(f_2\)가 작으면 terminal slope를 elimination label로 부르는 순간 clinical time-scale 판단이 흔들린다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.60, Fig.2.43 — Semi-logarithmic plot of bi-exponential decay after IV bolus.
Why this matters: This is the central visual for residual method. It shows that the observed curve is the sum of two extrapolated phase lines rather than one terminal line.
When to look: After reading the M1 formal definition and before reading the residual-method procedure.
Learner instruction: Inspect the terminal line first, then visually subtract it from the early observations. Confirm where A, B, -alpha, and -beta appear on the semilog plot.
<!-- /FIGURE_POINTER -->

---

### Card M2 — Macro ↔ Micro ↔ Physiological 3중 좌표계 변환

<!-- MASTER LENS -->
**개념 Big Idea:** 같은 2구획 curve는 세 좌표계로 표현된다. Macro는 curve description, micro는 ODE transition, physiological은 clearance/volume language다. 실무에서는 대개 physiological 좌표계를 쓰지만, 그 좌표계가 왜 같은 curve를 설명하는지는 macro/micro 변환을 이해할 때 보인다. [G&W pp.60–71; R&T pp.618–619]

| 좌표계 | Parameter set | 역할 |
|---|---|---|
| Macro | $A,\alpha,B,\beta$ | 관측 plasma curve의 두 지수항 표현 |
| Micro | $V_c,k_{10},k_{12},k_{21}$ | compartment ODE의 fractional rate constants |
| Physiological | $V_c,CL,Cld,V_t$ | clearance, distribution clearance, central/peripheral volume로 해석 |

<!-- ANNOTATION -->
좌표계라는 말은 같은 curve를 서로 다른 질문에 맞춰 다시 쓰는 방식이라는 뜻이다. curve를 잘 설명하는 좌표와 임상적으로 해석하기 좋은 좌표가 반드시 같지는 않다.

**Core conversions:**

$$CL=k_{10}V_c$$

$$Cld=k_{12}V_c=k_{21}V_t$$

$$V_c=\frac{D_{iv}}{A+B}$$

$$k_{21}=\frac{A\beta+B\alpha}{A+B}$$

$$k_{10}=\frac{\alpha\beta}{k_{21}}$$

$$k_{12}=\alpha+\beta-k_{21}-k_{10}$$

[G&W pp.60–62, 68–71; R&T pp.618–619]

<!-- ANCHOR -->
**왜 4개인가:** M1에서 본 두 지수항은 curve를 설명하는 4개 자유도다. source-supported 4-parameter sets는 micro $(V_c,k_{10},k_{12},k_{21})$ 또는 physiological $(V_c,CL,Cld,V_t)$이며, 혼합표현 $(V_c,V_t,k_{10},k_{12})$를 독립 자유도처럼 쓰면 안 된다. [G&W pp.60–62, 71]

**비식별성의 핵심:** plasma biexponential curve만으로는 central elimination only, peripheral elimination only, both-compartment elimination을 구별할 수 없다. 통상 central elimination only model을 쓰는 이유는 생리적으로 그럴듯하기 때문이지, plasma data가 그것을 증명했기 때문이 아니다. [G&W p.65; R&T pp.618–619]

**Reporting caveat:** 보고서에서는 “elimination from central compartment only” 및 “peripheral compartment lumping” 가정을 명시해야 한다. tissue PK, large protein drugs, target-mediated elimination이 의심되는 경우에는 이 가정의 mechanistic justification이 필요하다. [R&T p.618–619; 실무 추론]

**NONMEM bridge:** `[실무 확장]` ADVAN3/TRANS4의 표준 표현은 $CL,V_1,Q,V_2$이며, $K=CL/V_1$, $K_{12}=Q/V_1$, $K_{21}=Q/V_2$로 ODE transition을 만든다. 이 코드는 supplied PDFs의 직접 내용이 아니므로 implementation note로만 둔다.

**Partition caveat:** physiological ODE에서 central/peripheral concentration이 steady state에서 같아진다는 표현은 partitioning이 없다는 가정 위에 있다. 실제 tissue concentration이 plasma와 다르면 서로 다른 distribution clearance 또는 partition coefficient가 필요하지만, 두 compartment 모두의 data 없이는 식별이 어렵다. [G&W p.70]

<!-- RECAP -->
**Recap:** M2의 실무 의미는 “macro를 micro로 바꾸는 공식 암기”가 아니라, **plasma curve만으로 식별되는 것과 가정으로 보충하는 것을 분리하는 능력**이다.


> **[MASTER AUGMENTATION — EXPERT_INFERENCE | source-bound synthesis]** 좌표계 변환의 장인적 규칙은 “fit은 macro로 이해하고, ODE는 micro로 점검하며, 보고와 covariate 해석은 physiological parameter로 닫는다”이다. 세 언어를 섞으면 freedom, assumption, interpretation이 뒤섞여 reviewer가 묻는 질문에 답하기 어려워진다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.65, Fig.2.46 — Three two-compartment models that fit the same biexponential plasma profile.
Why this matters: It prevents the false inference that a biexponential plasma curve identifies the elimination site. The figure makes structural non-identifiability visible.
When to look: After reading M2 “비식별성의 핵심”.
Learner instruction: Compare the three structures and ask what is identical across them: the plasma curve. Then identify what plasma data alone cannot tell you: where elimination truly occurs.
<!-- /FIGURE_POINTER -->

---

### Card M3 — V₁ / Vss / Vβ 3중 분포용적 체계

<!-- MASTER LENS -->
**개념 Big Idea:** 2구획에서 “volume of distribution”은 하나가 아니다. $V_1$은 bolus 직후 central dilution이고, $V_{ss}$는 distribution equilibrium에서 amount/C를 뜻한다. $V_\beta$는 terminal slope와 CL로 계산되는 apparent terminal volume이다. 이 셋을 섞으면 amount in body, loading dose, tissue accumulation 해석이 흔들린다. [R&T pp.617, 628–630; G&W pp.63–65]

| Volume | Source-supported formula | 의미 | 주의 |
|---|---|---|---|
| $V_1$ | $V_1=Dose/(A+B)$ | initial dilution/central volume | bolus 직후 central + very rapidly equilibrating tissues |
| $V_{ss}$ | $V_{ss}=MRT\cdot CL=Dose\cdot AUMC/AUC^2$ | steady-state amount-to-plasma ratio | 표준 2구획 central elimination에서는 $V_{ss}=V_1(1+k_{12}/k_{21})$ |
| $V_\beta$ or $V$ | $V_\beta=CL/\beta=Dose/(AUC\cdot\beta)$ | terminal slope 기반 apparent volume | terminal slope가 distribution return에 지배되면 크게 부풀 수 있음 |

[G&W pp.63–65; R&T pp.617, 621–630]

<!-- ANNOTATION -->
따라서 “volume이 얼마인가?”라는 질문은 불완전하다. 먼저 bolus 직후인지, steady state인지, terminal extrapolation인지 물어야 한다.

**Ordering:** 표준 central-elimination 2구획 가정에서 $V_1\le V_{ss}\le V_\beta$로 생각할 수 있다. 하지만 이 부등식은 universal law가 아니라 source model assumption 안에서의 working rule이다. [R&T pp.629–630]

**Aspirin anchor:** aspirin은 $V_1=6.5$ L, $V_{ss}=10.4$ L, $V_\beta=13.7$ L로 차이는 있지만 치명적으로 벌어지지는 않는다. [R&T pp.617, 629–630]

**Gentamicin anchor:** gentamicin에서는 $V_1=14$ L, $V_{ss}=56$ L, $V_\beta=345$ L로 $V_\beta$가 $V_{ss}$보다 약 6배 크다. terminal half-life 87 hr는 plasma elimination half-life처럼 행동하지 않으며, 초기 phase half-life 약 4 hr가 therapeutic plasma concentration 조절에 더 중요해진다. [R&T pp.630, 635–641]

**Thiopental intuition:** R&T thiopental dog example에서 fat partitioning이 크고 adipose tissue가 total apparent Vd의 큰 몫을 차지하므로, lipophilicity·perfusion·partitioning 정보는 새 약물의 $V_{ss}/V_1$과 $V_\beta$ 부풀림을 사전에 의심하게 해주는 단서다. [R&T pp.614–615]

<!-- CONFUSION -->
**Plausible Fallacy:** “terminal slope가 가장 늦은 phase이므로 $V_\beta$가 가장 진짜 volume이다.”  
**Correction:** $V_\beta$는 terminal slope로 계산된 apparent volume이다. slowly equilibrating tissue에서 plasma로 돌아오는 속도가 terminal slope를 지배하면, $V_\beta$는 body amount를 직접 나타내는 volume이 아니라 terminal curve geometry의 산물이 된다. [R&T pp.628–630]

**Clinical use rule:** loading dose나 amount-at-steady-state 사고에는 $V_{ss}$가 더 적절하고, terminal phase extrapolation에는 $V_\beta$가 쓰인다. 다회투여 interval 내에서는 fluctuation이 작고 true steady state에 가까울 때 $V_{ss}$가 쓸 만하며, interval 말기 distribution equilibrium에 가까워진 뒤에는 $V_\beta$가 approximate amount estimate에 쓰일 수 있다. gentamicin-like case처럼 interval 내 distribution disequilibrium이 크면 둘 다 단순 적용하기 어렵다. [R&T pp.638–639]

<!-- RECAP -->
**Recap:** 2구획에서 volume을 묻는 질문에는 먼저 “어느 volume?”이라고 답해야 한다. $V_1$, $V_{ss}$, $V_\beta$는 서로 다른 질문에 대한 답이다.


> **[MASTER AUGMENTATION — EXPERT_INFERENCE | source-bound synthesis]** \(V_1\), \(V_{ss}\), \(V_\beta\)는 서로 다른 숫자가 아니라 서로 다른 임상 질문의 label이다. “지금 필요한 것은 bolus 직후 dilution인가, steady-state amount인가, terminal extrapolation인가?”를 먼저 고르면 volume 오용의 대부분이 사라진다.

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.628, Fig.19-9 — Distribution-volume terms and the effect of elimination on V and Vss.
Why this matters: This is the best source visual for why V1, Vss, and Vbeta are not interchangeable. It turns the volume table into a time-dependent interpretation problem.
When to look: After reading the M3 volume table and before reading the Aspirin/Gentamicin anchors.
Learner instruction: Track how apparent volume changes as distribution and elimination proceed. Then map each part of the curve back to V1, Vss, or Vbeta.
<!-- /FIGURE_POINTER -->

<!-- FIGURE_SCHEMATIC -->
Title: When can Vss or Vbeta estimate amount during multiple dosing?
Mode: R
Visual objective: In 5 seconds, the learner should see three regimes: Vss usable, Vbeta approximately usable, and neither volume safely usable.
Core message: Volume terms are not universal calculators; their use depends on dosing interval, fluctuation, and distribution equilibrium.
Elements to include: One horizontal dosing-interval timeline; Zone 1: true or near steady state with small fluctuation → “Vss useful for amount estimate”; Zone 2: late interval after distribution equilibrium → “Vbeta may approximate amount”; Zone 3: distribution disequilibrium throughout interval → “neither simple volume term”; warning label “gentamicin-like case: terminal term ≠ plasma fluctuation”; cross-reference labels “M3 Clinical use rule” and “M5 Multiple dosing volume rule”.
Elements to exclude: Exact reproduction of R&T Fig.19-16; dense equations beyond Vss and Vbeta labels; more than three regime categories.
Suggested rendering: SVG
Caption: Vss and Vbeta answer different amount-estimation questions during a dosing interval; neither should be used blindly under persistent distribution disequilibrium.
Alt text: A dosing-interval timeline split into regimes where Vss, Vbeta, or neither volume term is appropriate for estimating amount in the body.
Source relation: Redrawn from textbook concept
<!-- /FIGURE_SCHEMATIC -->

---

### Card M4 — 재파라미터화 5종과 condition number

<!-- MASTER LENS -->
**개념 Big Idea:** 같은 biexponential data를 5개 parameterization으로 fit하면 WRSS는 비슷해도 parameter precision과 condition number<!-- ANNOTATION -->(← 추정 불안정성의 수치 지표)는 크게 달라진다. 즉 model form이 같아도 좌표계가 estimation geometry를 바꾼다. [G&W pp.513–517]

**PK8 anchor:** Compound X 100 µg IV bolus data에서 G&W는 5가지 parameterization을 비교한다. Table 8.1의 condition number는 ODE model 29.69, Macro model 125.2, Colburn 2243, Reparameterized model 2306, Takada 3186이다. 따라서 PK8의 범위는 **29.69–3,186**이고, 최대/최소 비율은 약 **107배**다. [G&W pp.513–517]

| Model family | 핵심 parameterization | Content Lock 판단 |
|---|---|---|
| Macro | $A,\alpha,B,\beta$ | curve description에는 직관적이나 intercept/slope correlation 가능성 큼 |
| Takada | time-dependent $V(t)$ | WRSS가 낮아도 condition number가 큼 |
| Colburn | exponential approach of $V(t)$ | time-dependent volume intuition 제공 |
| Reparameterized CL model | $D_{iv},CL$ 포함 | clearance language로 bridge |
| ODE physiological | $CL,V_c,Cld,V_t$ | PK8에서 lowest condition number |

**Core lesson:** 가장 낮은 WRSS가 production model의 충분조건은 아니다. Takada model은 WRSS가 낮아도 condition number가 높다. 반대로 ODE model은 condition number가 가장 낮다. [G&W p.516]

<!-- TRENCH -->
**Trench tip:** condition number가 폭증하면 좌표계부터 바꾸기 전에 THETA 초기치를 먼저 확인한다. 초기치가 자릿수부터 틀리면 좌표계와 무관하게 information matrix가 나빠질 수 있다. 디버깅 순서: initial estimate → log-domain parameterization → reparameterization. [실무 디버깅 순서]

**RSE caveat:** condition number는 parameter 간 정보 직교성을, RSE는 각 parameter 자체의 추정 신뢰성을 본다. PK8 Table 8.1에는 RSE가 없으므로 그 표만으로 production 결정을 끝내지 않는다. [실무 확장]

**PK7 model discrimination bridge:** G&W PK7은 mono/bi/tri-exponential discrimination에서 AIC/F-test, precision, correlations, residuals, simplest adequate model rule을 함께 보게 한다. 특히 weighting scheme이 다른 model을 단순 F-test로 비교하면 안 된다. [G&W pp.505–512]

**NCA fallback:** G&W PK8은 initial phase가 거의 보이지 않지만 배제할 수 없을 때 NCA가 제안될 수 있음을 언급한다. 이것은 “2구획 fit을 무조건 강행”하라는 세션이 아니라, data가 phase를 식별할 때만 parametric 2구획 해석을 신뢰하라는 경고다. [G&W p.517]

<!-- RECAP -->
**Recap:** M4에서 기억할 숫자는 “29.69–3,186” 자체보다, **fit이 비슷해 보여도 좌표계가 covariance geometry를 100배 이상 바꿀 수 있다**는 사실이다.


> **[MASTER AUGMENTATION — EXPERT_INFERENCE | source-bound synthesis]** Reparameterization은 같은 모델을 예쁘게 다시 쓰는 작업이 아니라 estimation geometry를 바꾸는 preconditioning이다. WRSS가 model fit의 축이라면 condition number는 그 fit을 반복 가능하게 추정할 수 있는지의 축이다.

<!-- FIGURE_SCHEMATIC -->
Title: PK8 model selection: WRSS axis vs condition-number axis
Mode: R
Visual objective: In 5 seconds, the learner should see that the model with the lowest WRSS is not the model with the lowest condition number.
Core message: Similar fit quality does not imply similar estimation stability.
Elements to include: Five model rows: Bi-exponential, Takada, Colburn, Reparameterized CL, ODE physiological; WRSS mini-bar or badge for each model; condition-number mini-bar or badge for each model; highlight Takada as lowest WRSS with high condition number; highlight ODE physiological as similar WRSS with lowest condition number; one summary callout “fit axis ≠ estimation geometry axis”.
Elements to exclude: Direct facsimile of Table 8.1 layout; parameter-estimate details not needed for the comparison; any threshold not present in the Content Lock text.
Suggested rendering: CSS-card
Caption: PK8 shows that reparameterization can leave fit quality similar while changing condition number by roughly two orders of magnitude.
Alt text: A comparison card showing five parameterizations with separate WRSS and condition-number indicators; Takada has the lowest WRSS but high condition number, whereas the ODE model has the lowest condition number.
Source relation: Redrawn from textbook concept
<!-- /FIGURE_SCHEMATIC -->

---

### Card M5 — 분포속도론의 임상 파급과 terminal half-life의 함정

<!-- MASTER LENS -->
**개념 Big Idea:** terminal half-life는 자주 유용하다. 그러나 distribution kinetics가 강할 때는 “약물이 사라지는 속도”보다 “slow tissue에서 plasma로 돌아오는 속도”를 더 많이 반영할 수 있다. 그래서 plateau 도달, tissue accumulation, renal impairment dosing은 $f_1/f_2$와 투여 방식까지 함께 봐야 한다. [R&T pp.631–641]

**Plateau equation:**

$$\frac{C(t)}{C_{ss}}=f_1(1-e^{-\alpha t})+f_2(1-e^{-\beta t})$$

<!-- ANNOTATION -->
이 식은 두 phase가 $C_{ss}$로 접근하는 정도를 $f_1/f_2$로 가중합한다. 그래서 half-life 하나가 아니라 phase별 AUC 기여도가 plateau 해석을 결정한다.

$f_2$가 크면 terminal half-life가 plateau 도달을 대체로 설명한다. 반대로 $f_2$가 작으면 terminal half-life가 길어도 plasma plateau는 훨씬 빨리 접근할 수 있다. [R&T pp.631–633]

**Nicardipine anchor:** terminal half-life가 약 12 hr로 길지만, plasma concentration은 1 hr 안에 약 50% Css에 도달하고 약 15 hr에 90% Css에 도달한다. terminal half-life만 보고 loading dose 필요성을 판단하면 초기 과량 투여 위험이 생길 수 있다. [R&T p.631]

**Gentamicin anchor:** terminal half-life가 87 hr이어도 plasma therapeutic behavior는 약 4 hr 초기 phase에 의해 좌우된다. terminal term 기반 accumulation index는 16배가 될 수 있지만, 이것은 plasma peak/trough accumulation과 동일하지 않고 slowly equilibrating tissue accumulation을 말한다. [R&T pp.635–641]

**Tissue vs plasma plateau:** plasma가 plateau에 빨리 접근해도 slowly equilibrating tissue는 훨씬 늦게 접근할 수 있다. 따라서 response site가 peripheral/tissue 쪽이면 plasma half-life만으로 onset/duration을 해석하면 안 된다. [R&T pp.633–634]

**Multiple dosing volume rule:** fluctuation이 작고 true steady state에 가까울 때는 $V_{ss}$가 amount estimate에 유용하다. interval 말기 distribution equilibrium에 가까우면 terminal volume $V$도 approximation으로 쓰일 수 있다. 그러나 gentamicin-like 경우처럼 interval 전체가 distribution disequilibrium이면 어느 volume도 단순 amount calculator가 되지 않는다. [R&T pp.638–639]

**Softened warning:** “terminal half-life는 항상 틀린다”가 아니다. R&T는 많은 약물에서 $f_2>0.8$이면 terminal phase가 plateau/time-course를 잘 설명한다고 말한다. 핵심은 “terminal인지 effective인지, plasma인지 tissue인지, $f_2$가 얼마인지”를 확인하는 것이다. [R&T pp.631–641]

<!-- TRENCH -->
**Lab rule:** 누군가 “이 약물의 half-life는 X시간”이라고 말하면 바로 묻는다: “terminal? effective? plasma? tissue?” 둘이 다르면 multiple-dosing simulation이 달라진다. [실무 확장]

<!-- RECAP -->
**Recap:** M5의 실전 규칙은 **half-life 하나로 dosing을 말하지 말고, $f_1/f_2$, volume term, input pattern, sampling time을 같이 본다**는 것이다.


> **[MASTER AUGMENTATION — EXPERT_INFERENCE | source-bound synthesis]** Half-life를 들었을 때의 첫 반응은 계산이 아니라 분류여야 한다. terminal인지 effective인지, plasma인지 tissue인지, single dose인지 multiple dosing인지가 정해진 뒤에야 그 half-life가 dosing interval이나 plateau 판단에 들어갈 수 있다.

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.631, Fig.19-10 — Nicardipine approach to plateau despite long terminal half-life.
Why this matters: It is the clearest visual for why terminal half-life may not predict early plasma plateau. It directly supports the M5 warning against half-life-only dosing reasoning.
When to look: After reading the M5 plateau equation and Nicardipine anchor.
Learner instruction: Compare the terminal half-life label with the observed approach to 50% Css. Do not infer plateau timing from terminal slope alone until f1/f2 is checked.
<!-- /FIGURE_POINTER -->

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.636, Fig.19-14 — Gentamicin plasma/tissue multiple-dosing accumulation.
Why this matters: This figure separates terminal-term accumulation from therapeutic plasma fluctuation. It is the best visual anchor for the gentamicin half-life trap.
When to look: After reading the M5 Gentamicin anchor and before the §5 terminal/effective half-life confusion pair.
Learner instruction: Follow plasma concentration and slowly equilibrating tissue behavior separately. Identify why a terminal accumulation index can be large without implying the same plasma peak/trough accumulation.
<!-- /FIGURE_POINTER -->

---

## §5 — Confusion Pairs & Critical Blow

### Pair 1 — Bi-exponential curve vs “two elimination processes”

<!-- CONFUSION -->
| Trap | Correction | Critical cue |
|---|---|---|
| 두 지수항을 두 개의 independent elimination pathway로 해석한다. | 두 지수항은 linear ODE system의 eigen-components다. elimination은 central clearance로 계속 일어나지만, observed phase는 distribution과 elimination의 합성 결과다. | $f_2$가 작으면 terminal phase를 elimination phase라 부르면 위험하다. [G&W p.63; R&T pp.622–623] |

### Pair 2 — $V_{ss}$ vs $V_\beta$ [Critical Blow]

<!-- CONFUSION -->
| Trap | Correction | Critical Blow |
|---|---|---|
| terminal slope로 계산한 $V_\beta$를 body amount/loading dose용 volume으로 쓴다. | steady-state amount 또는 loading dose 사고에는 $V_{ss}$가 더 가까운 volume이다. $V_\beta$는 terminal slope geometry의 산물이다. | Gentamicin: $V_\beta=345$ L, $V_{ss}=56$ L, $V_1=14$ L. $V_\beta$를 “진짜 body volume”처럼 쓰면 tissue redistribution과 plasma dosing을 혼동한다. [R&T pp.630, 635–641] |

### Pair 3 — Macro vs Micro vs Physiological parameterization

<!-- CONFUSION -->
| Trap | Correction |
|---|---|
| $A,\alpha,B,\beta$를 “모델 파라미터”로만 외우고 $CL,Q,V_1,V_2$와 별개로 생각한다. | Macro는 curve description, micro는 ODE transition, physiological은 interpretation/reporting 좌표계다. 같은 model이라도 좌표계가 condition number와 interpretability를 바꾼다. [G&W pp.60–71; R&T pp.618–619] |

### Pair 4 — Terminal half-life vs Effective/clinical half-life [Critical Blow]

<!-- CONFUSION -->
| Trap | Correction | Critical Blow |
|---|---|---|
| 논문에 half-life가 12 hr라고 적혀 있으면 plateau 도달에도 12 hr 단위를 그대로 적용한다. | terminal half-life인지, effective half-life인지, plasma/tissue 중 어디의 half-life인지 확인한다. | Nicardipine-style case: terminal $t_{1/2}\approx12$ hr이지만 50% Css는 약 1 hr. terminal half-life만 보고 loading dose를 권하면 초기 과량 투여 판단이 나올 수 있다. [R&T p.631] |

### Pair 5 — Better WRSS vs better model

<!-- CONFUSION -->
| Trap | Correction |
|---|---|
| WRSS가 가장 낮은 parameterization을 무조건 채택한다. | WRSS, residual pattern, precision/RSE, condition number, correlation, biological plausibility를 함께 본다. G&W PK8에서 ODE model은 lowest condition number이고, Takada는 낮은 WRSS에도 high condition number다. [G&W pp.513–517] |

<!-- RECAP -->
**Confusion recap:** 이 세션의 치명적 혼동은 모두 “curve geometry를 physiological truth로 바로 읽는 것”에서 생긴다. curve는 evidence다. interpretation은 assumption과 좌표계를 통해 얻어진다.

---

## §7 — Self-Test Blocks

### Q1. Residual method reconstruction

<!-- SELF-TEST -->
G&W Fig.2.43에서 terminal phase를 외삽하여 $B=28$, $\beta=\ln(28/10)/450$를 얻었다. 초기 관측치에서 무엇을 빼야 $\alpha$ phase를 얻는가?

**Answer key:** 각 초기 관측치 $C_{obs}(t_i)$에서 $B e^{-\beta t_i}$를 뺀다. residual을 semilog plot에 다시 놓고 slope/intercept를 구하면 $\alpha$와 $A$가 나온다. [G&W p.60]

### Q2. Aspirin CL direction

<!-- SELF-TEST -->
Aspirin 650 mg IV bolus에서 terminal-only one-compartment 해석은 $CL=0.98$ L/min, biexponential 해석은 $CL=683$ mL/min이다. terminal-only 해석은 true CL을 과소평가하는가, 과대평가하는가?

**Answer key:** 과대평가한다. $0.98$ L/min은 683 mL/min보다 약 44% 높다. 따라서 maintenance dose 계산은 과대평가 위험이 있다. [R&T pp.615–620]

### Q3. Volume ratio application

<!-- SELF-TEST -->
Aspirin과 gentamicin 중 $V_\beta/V_{ss}$ 비율이 더 큰 약물은 무엇이며, 왜 중요한가?

**Answer key:** Gentamicin이다. Aspirin은 $13.7/10.4\approx1.3$이지만 gentamicin은 $345/56\approx6.2$다. 큰 비율은 terminal slope-derived volume을 steady-state amount volume처럼 쓰면 안 된다는 경고다. [R&T pp.629–641]

### Q4. Structural non-identifiability

<!-- SELF-TEST -->
동일한 biexponential plasma curve를 central elimination only, peripheral elimination only, both elimination model이 모두 설명할 수 있다. plasma data만으로 무엇을 결론낼 수 없나?

**Answer key:** elimination site를 식별할 수 없다. central elimination only는 보통 physiologic plausibility 때문에 선택되는 working assumption이며, tissue data나 mechanistic justification 없이 plasma curve만으로 증명된 것이 아니다. [G&W p.65; R&T pp.618–619]

### Q5. Terminal half-life trap

<!-- SELF-TEST -->
Nicardipine처럼 terminal half-life가 12 hr인데 1 hr에 50% Css에 도달하는 case에서 terminal half-life만으로 loading dose를 권하면 왜 위험한가?

**Answer key:** plateau approach가 terminal term만으로 결정되지 않고 $f_1/f_2$ 가중합으로 결정되기 때문이다. plasma는 이미 빠르게 올라가는데 terminal half-life만 보면 “너무 늦게 도달한다”고 오판하여 과도한 loading을 권할 수 있다. [R&T pp.631–633]

### Q6. PK8 model selection

<!-- SELF-TEST -->
PK8에서 Takada model은 WRSS가 낮고 ODE model은 condition number가 낮다. 어느 하나만 보고 결정하면 안 되는 이유는?

**Answer key:** WRSS는 fit residual 크기, condition number는 parameter estimation geometry를 본다. 둘 중 하나만 좋다고 deployable model은 아니다. PK8의 핵심은 “동일 데이터/비슷한 fit에서도 좌표계가 condition number를 크게 바꾼다”는 것이다. [G&W pp.513–517]

### Q7. Sparse design diagnosis

<!-- SELF-TEST -->
첫 sample이 distribution phase 이후에만 존재하는 sparse design에서 ADVAN3 TRANS4 fit 후 $V_2$ RSE >100%, ETA(V2) shrinkage >80%, early CWRES positive trend가 보인다. 가장 먼저 의심할 것은?

**Answer key:** “약물의 $V_2$가 진짜 작다”가 아니라 distribution phase가 data에 없어 $V_2$가 식별되지 않는 Phantom V2 상황을 의심한다. [실무 확장]

### Q8. Half-life lab rule

<!-- SELF-TEST -->
회의에서 누군가 “half-life가 87 hr이므로 8시간 간격 투여하면 plasma가 16배 축적된다”고 말한다. 무엇을 되물어야 하는가?

**Answer key:** terminal half-life인지 effective/plasma half-life인지, $f_2$가 얼마인지, 축적이 plasma인지 slowly equilibrating tissue인지 물어야 한다. Gentamicin-like case에서는 terminal term accumulation과 plasma therapeutic fluctuation을 구분해야 한다. [R&T pp.635–641]

<!-- RECAP -->
**Self-test recap:** 8개 질문을 모두 통과하면, 2구획 모델을 “공식”이 아니라 “모델 선택·volume 해석·dosing simulation의 사고 도구”로 사용할 준비가 된 것이다.

---

## §8 — Knowledge Graph, Failure Modes, and Professional Moat

### A. 이번 세션 직후 연결되는 지식

| Next node | 이 세션에서 가져가는 것 |
|---|---|
| NONMEM ADVAN3/4/11/12 | $CL,V_1,Q,V_2$ 좌표계가 macro/micro와 어떻게 연결되는지 이해 |
| Sparse sampling design | distribution phase sample 없이는 $V_2$, $Q$, $\alpha$ 식별이 약해짐 |
| Covariate model building | covariate는 보통 slope/half-life가 아니라 $CL,V,Q$ 같은 physiological parameter에 붙인다 |
| Multiple-dosing simulation | terminal half-life 하나가 아니라 $f_1/f_2$, input duration, $V_{ss}/V_\beta$를 같이 본다 |
| 3구획 model | biexponential이 residual에서 다시 휘면 tri-exponential 또는 deeper tissue compartment 의심 |

### B. Failure modes

| Failure mode | Signature | Preventive rule |
|---|---|---|
| **Terminal-only CL error** | early sampling 누락, 1-compartment CL overestimate | distribution phase sampling을 확보하고 biexponential 가능성 확인 |
| **Vβ-as-Vss error** | $V_\beta/V_{ss}$가 큰데 loading/amount 계산에 $V_\beta$ 사용 | amount/steady-state에는 $V_{ss}$ 우선, terminal extrapolation에는 $V_\beta$ |
| **Phantom V2** | sparse design, $V_2$ RSE >100%, ETA(V2) shrinkage >80% | “작은 $V_2$” 결론 전 distribution-phase identifiability 확인 |
| **Macro Drift** | $A/B$ high correlation, covariance instability | production에는 physiological parameterization 우선 고려 |
| **Initial Estimate Trap** | condition number 폭증, 초기치 변경만으로 결과 급변 | initial estimate → log-domain → reparameterization 순서로 디버깅 |
| **WRSS-only selection** | lowest WRSS model이 high condition number | residual, precision, condition number, biological plausibility를 함께 판단 |
| **F-test misuse** | weighting scheme 다른 model을 단순 F-test 비교 | PK7 rule: residual/precision/correlation/simplest adequate model을 함께 사용 |

### C. Professional moat — 30년차 모델러가 1분 안에 보는 것

1. Semilog curve의 knee와 terminal straightness를 보고 2구획/3구획 가능성을 가른다.  
2. $f_2$를 보고 terminal half-life가 clinical time scale을 대표할지 판단한다.  
3. $V_\beta/V_{ss}$ 비율로 terminal volume 오용 위험을 본다.  
4. WRSS가 낮아도 condition number/RSE/correlation이 나쁘면 production model로 보류한다.  
5. CWRES vs TIME이 early positive 또는 S-shaped pattern이면 structural misspecification 또는 missing distribution phase를 의심한다.  
6. $\eta$-shrinkage가 높으면 covariate effect의 해석 가능성을 낮게 본다. [실무 기준]

### D. Minimal practical algorithm

```text
1. Plot semilog C-time curve.
2. Early sampling이 distribution phase를 포착했는지 확인.
3. Bi-exponential 가능성이 있으면 A, α, B, β를 rough estimate.
4. AUC, f1, f2, V1, Vss, Vβ를 계산.
5. Vβ/Vss와 f2를 보고 terminal half-life 해석 가능성을 평가.
6. Physiological parameterization으로 CL, Q/Cld, V1, V2를 설정.
7. Fit 후 residual, RSE, correlation, condition number를 함께 확인.
8. Sparse design 또는 high shrinkage이면 V2/Q/covariate 해석을 보류.
9. Multiple dosing은 terminal half-life 하나가 아니라 f1/f2-weighted plateau equation으로 점검.
```

<!-- RECAP -->
**Final recap:** 2구획 모델의 mastery는 $C=Ae^{-\alpha t}+Be^{-\beta t}$를 외우는 것이 아니다. 좋은 모델러는 그 식을 보는 순간 **sampling adequacy, CL bias direction, volume choice, condition number risk, half-life misuse**를 함께 읽는다.

---

## PART B — Compiler-Only Appendix

This appendix is not learner-facing. It exists only to protect Phase 5 rendering fidelity.

### B1. Compilation Contract

- Phase 5 must render the PART A body; it must not alter, compress, expand, or reinterpret the scientific text.
- Input mode is PATCH MODE already resolved in this master file: Content Lock v2 was used as the canonical body and all approved Phase 4C markers were spliced into the learner body.
- Output target for Phase 5 is a single self-contained HTML file.
- Do not generate new scientific content during HTML compilation.
- Do not generate additional figures, additional markers, or additional page/source tags.
- Do not embed textbook images. Image rights are None.
- Do not generate Mermaid/SVG at Phase 4D level. Phase 5 may render schematic markers according to its own rendering rules.

### B2. Figure Rendering Instructions

Approved marker inventory:

| Marker | Mode | Source relation | Required Phase 5 treatment |
|---|---|---|---|
| FIG-05-01 | POINTER | G&W p.60 Fig.2.43 | Render as textbook-reference pointer callout only; do not embed source image. |
| FIG-05-02 | POINTER | G&W p.65 Fig.2.46 | Render as textbook-reference pointer callout only; do not embed source image. |
| FIG-05-03 | POINTER | R&T p.628 Fig.19-9 | Render as textbook-reference pointer callout only; do not embed source image. |
| FIG-05-04 | SCHEMATIC REDRAW | R&T p.639 Fig.19-16 concept | Render as new/redrawn schematic using the marker brief; do not facsimile textbook layout. |
| FIG-05-05 | SCHEMATIC REDRAW | G&W p.516 Table 8.1 concept | Render as new comparison schematic/CSS card; do not copy source table layout. |
| FIG-05-06 | POINTER | R&T p.631 Fig.19-10 | Render as textbook-reference pointer callout only; do not embed source image. |
| FIG-05-07 | POINTER | R&T p.636 Fig.19-14 | Render as textbook-reference pointer callout only; do not embed source image. |

General figure rules:

- Every `FIGURE_POINTER` marker block becomes a compact source-inspection callout with source, why-this-matters, when-to-look, and learner instruction.
- Every `FIGURE_SCHEMATIC` marker block becomes a proper `<figure>` with caption and alt text.
- Figures must stay at the end of the concept card where the marker appears.
- No decorative imagery.
- No figure not present in PART A may be generated.
- No textbook image may be embedded, screenshotted, traced, or reproduced as a facsimile.

### B3. Page Tag Rendering Rules

Source page tags are plain text, not HTML comments. Detect and wrap them in HTML only during Phase 5.

Patterns:

```text
[p.XX]                    -> standard single-page tag
[pp.XX–YY] or [pp.XX-YY]  -> page range tag
[pp.XX, YY]               -> non-contiguous multi-page tag
[p.확인 필요]              -> source-page uncertainty tag
```

Rendering:

```text
Standard tags  -> <span class="source-page">[p.XX]</span>
Uncertain tags -> <span class="source-page source-uncertain">[p.확인 필요]</span>
```

Rules:

- Apply detection to body text, equation captions, and example headings.
- Do not apply detection inside `<pre><code>` blocks.
- Do not apply detection inside figure marker blocks; those blocks have internal source fields.
- Do not add, remove, or renumber page tags.
- Source page tags must remain visible in print mode.

### B4. HTML Compiler Requirements

Marker/component mapping:

| Marker / Pattern | HTML Component | Required style/behavior |
|---|---|---|
| `MASTER LENS` comment marker | Callout box | gold left border; subtle gold background |
| `ANNOTATION` comment marker | Inline annotation/tooltip | small muted italic text |
| `ANCHOR` comment marker | Bridge sentence | italic muted text |
| `TRENCH` comment marker | Practical tip box | rose left border/background tint |
| `CONFUSION` comment marker | Comparison box/table | amber comparison treatment |
| `SELF-TEST` comment marker | Click-to-reveal accordion | question visible, answer hidden until user click |
| `RECAP` comment marker | Section summary box | blue left border/background tint |
| `[확인 필요]` | Highlighted uncertainty | `<mark>` |
| `FIGURE_POINTER` comment marker | Textbook pointer callout | purple left border/source-inspection style |
| `FIGURE_SCHEMATIC` comment marker | Inline schematic figure | `<figure>` with caption and alt text |
| `FIGURE_IMAGE_SLOT` comment marker | Image/placeholder figure | only if user supplies image file; otherwise placeholder |
| `MASTER AUGMENTATION — EXPERT_INFERENCE` blockquote | Expert synthesis callout | visually distinct from canonical textbook-derived body |

Rendering requirements:

- Math: MathJax CDN; support inline `\(...\)` and display `\[...\]` / `$$...$$`.
- Code: render fenced code as `<pre><code>` with dark background and language class when available.
- Navigation: sticky left sidebar on desktop; anchor jump to every major section and §2 card.
- Accordions: self-test answer keys hidden by default and revealed on click.
- Checklist/session state: use sessionStorage where applicable.
- Controls: code-copy button and print/PDF button using `window.print()`.
- Responsive layout: ≤768px single-column/collapsed nav; ≥1024px two-column layout allowed.
- Theme: support prefers-color-scheme dark/light.
- Print: remove backgrounds where necessary, hide navigation, avoid page-break-inside for cards/figures, and keep source page tags visible.
- External dependencies allowed only for MathJax CDN, Mermaid CDN if used for schematic rendering, and permitted CDN libraries such as highlight.js. No local external CSS/JS/font/image files unless user supplies them.

Navigation-anchor integrity rules:

- Use only `<a href="#...">` links in the sidebar.
- Every sidebar href target must have a matching `id` in the body.
- Every major section heading (§1, §2, §5, §7, §8) must receive a stable id.
- Every §2 concept card heading must receive a stable id.
- href values and body ids must match exactly.
- Do not create duplicate ids.
- Include `html { scroll-behavior: smooth; }`.
- Before finalizing HTML, count sidebar href values, confirm each id exists exactly once, and fix any mismatch before output.

### B5. Audit Guardrails

Regression-prevention items:

- Keep PK8 condition-number range as `29.69–3,186`, not `29.69–4,104`.
- Keep maximum/minimum ratio as approximately 107-fold / roughly 100-fold-plus, not 200-fold.
- Keep aspirin direction: terminal-only one-compartment interpretation overestimates CL versus biexponential interpretation; maintenance dose may be overestimated.
- Keep NONMEM implementation and regulatory implications labeled as practical extension/inference, not textbook-derived fact.
- Keep eigenvalue explanation labeled as mathematical interpretation.
- Keep `V_{ss}` formula restricted to source-supported expressions; do not restore malformed ellipsis expression.
- Keep terminal half-life warning softened: useful in many cases, dangerous when `f2`, dosing pattern, plateau, and tissue accumulation are ignored.
- Do not restore source-unsupported FDA/EMA guidance claims, direct NDA deficiency-letter claims, unsupported thresholds, unapproved examples, unapproved code blocks, or unapproved figure embeddings.

### B6. Crucible Guardrails

- Crucible is not a raw prose source for Phase 5.
- Preserve only logic already adopted in Content Lock or explicitly allowed as bounded expert synthesis.
- Do not reintroduce lower-priority or rejected scope-creep items.
- Do not convert speculative insight into textbook-derived fact.
- Keep expert synthesis visibly separated and labeled as `EXPERT_INFERENCE`.

### B7. Deprecated and Forbidden Restorations

- Step 1 Draft v0 is deprecated.
- Do not restore the old PK8 `4,104` maximum as if it belonged to PK8.
- Do not restore “200배” condition-number language.
- Do not restore aspirin “dose underestimation” direction error.
- Do not restore source-like NONMEM/FDA/PIPET claims.
- Do not restore catenary=enterohepatic recirculation analogy.
- Do not restore PD-response expansion, hemodialysis/lithium redistribution, PBPK/QSP/TMDD expansion, or full NONMEM debugging tree.
- Do not restore textbook figures as embedded images.

### B8. PATCH MODE Splice Verification Table

| Marker # | Anchor text (truncated to 60 chars) | Anchor found? | Match count | Inserted? | Final location (§ + card) |
|---:|---|---|---:|---|---|
| FIG-05-01 | `### Card M1 — 이중지수 방정식과 잔차법(Method of Residuals)` | YES | 1 | YES | §2 + Card M1 |
| FIG-05-02 | `### Card M2 — Macro ↔ Micro ↔ Physiological 3중 좌표계 변환` | YES | 1 | YES | §2 + Card M2 |
| FIG-05-03, FIG-05-04 | `### Card M3 — V₁ / Vss / Vβ 3중 분포용적 체계` | YES | 1 | YES | §2 + Card M3 |
| FIG-05-05 | `### Card M4 — 재파라미터화 5종과 condition number` | YES | 1 | YES | §2 + Card M4 |
| FIG-05-06, FIG-05-07 | `### Card M5 — 분포속도론의 임상 파급과 terminal half-life의 함정` | YES | 1 | YES | §2 + Card M5 |

### B9. Zero-Omission Coverage Matrix

| Domain | Status | Basis |
|---|---|---|
| C1. Scope Lock required concepts | PASS | M1–M5 cover biexponential/residual method, coordinate conversion, V1/Vss/Vβ, reparameterization/condition number, and clinical distribution-kinetic impact. |
| C2. Scope Lock required data anchors | PASS | G&W Fig.2.43, PK7/PK8, R&T aspirin/nicardipine/gentamicin/volume anchors retained in PART A. |
| C3. Audit MUST_FIX / SHOULD_FIX | PASS | PK8 29.69–3,186 correction, aspirin CL direction, source-tag separation, Vss formula repair, terminal half-life softening retained. |
| C4. Audit T5 coverage findings | PASS | High-impact equation, figure, example, and author-message findings are represented; low-scope/PD/redistribution materials remain excluded. |
| C5. Audit T6 / Phase 4C figure coverage | PASS | All 7 approved markers inserted exactly once in PART A; 5 pointer markers and 2 schematic markers; no textbook image embedded. |
| C6. Page tag/source tag integrity | PASS | Existing bracketed page/source tags preserved; no new page tags fabricated by augmentation. |
| C7. Crucible Grade A preservation | PASS | Adopted insights remain: eigenvalue constraint tag, f1/f2 graph reading, volume intuition, WRSS/condition-number split, half-life lab rule. |
| C8. Deprecated/forbidden restoration check | PASS | Step 1 unsupported condition range, aspirin direction error, source-like FDA/NDA claims, unapproved examples/code/figures not restored. |

### B10. Micro-Patch Log

| # | Location | Type | Change | Scientific body altered? | Rationale |
|---|---|---|---|---|---|
| MP-01 | PART A construction | Non-scientific hygiene patch | Excluded Content Lock v2 adjudication/process tables before §1 from learner-facing PART A; retained their guardrail function in PART B. | NO | Prevents audit/process text from appearing in learner handout; no scientific content altered. |
| MP-02 | §8 after Minimal practical algorithm | Non-scientific hygiene patch | Removed the §8.E “Scope carry-forward to Phase 4C” process subsection from PART A and moved its substance into PART B figure/compilation rules. | NO | Prevents Phase 4C process note from appearing in learner handout; no scientific content altered. |
| MP-03 | §2 cards M1–M5 | PATCH MODE marker splice | Inserted FIG-05-01 through FIG-05-07 at approved card-end positions. | NO | Required by Phase 4C insertion map. |
| MP-04 | §2 cards M1–M5 | Mastery augmentation layer | Inserted five labeled EXPERT_INFERENCE blocks adjacent to relevant concept cards. | AUGMENTATION ONLY | Allowed bounded uplift; no source tags or numerical claims added. |

### B11. Mastery Augmentation Log

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
|---|---|---|---|---|---|---|
| AUG-01 | §2 Card M1 | expert mental model | YES | EXPERT_INFERENCE grounded in M1/R&T/G&W + Crucible | Turns residual method into sampling/phase-diagnosis lens | Low; no new numbers/examples |
| AUG-02 | §2 Card M2 | coordinate-system discipline | YES | EXPERT_INFERENCE grounded in M2 + Audit source-boundary rule | Separates macro/micro/physiological roles | Low; no new source claims |
| AUG-03 | §2 Card M3 | clinical question framing | YES | EXPERT_INFERENCE grounded in M3/R&T volume logic | Prevents volume-term misuse | Low; no new formulas |
| AUG-04 | §2 Card M4 | estimation-geometry lens | YES | EXPERT_INFERENCE grounded in PK8 condition-number logic | Clarifies WRSS vs condition-number axes | Low; no external threshold |
| AUG-05 | §2 Card M5 | half-life classification rule | YES | EXPERT_INFERENCE grounded in M5/R&T examples | Improves dosing-interpretation transfer | Low; no new examples |

Rejected augmentation candidates:

| Rejected candidate | Reason for rejection |
|---|---|
| Additional named clinical examples beyond aspirin, thiopental, nicardipine, gentamicin | Would add source-boundary risk and exceed bounded augmentation. |
| New numerical thresholds for condition number, RSE, or shrinkage | Would require external source support not present in the supplied PDFs. |
| Full regulatory reviewer narrative | Source scope explicitly excludes direct FDA/EMA/NDA claims unless externally grounded. |

### Final Checklist Result

| Checklist group | Status | Notes |
|---|---|---|
| Learner completeness | PASS | PART A is independently readable; audit/compiler/process material is not inside learner handout. |
| Content integrity | PASS | Approved markers present exactly once in PART A; no unapproved figure markers added; no page tags fabricated. |
| Mastery augmentation | PASS | Five labeled, bounded blocks only; no new examples/numbers/page tags. |
| HTML readiness | PASS | PART B contains marker, figure, source-tag, navigation, print, and forbidden-restoration rules. |


# 15_HTML Compile Input Master

**Target file**: `15_html_compile_input_master.md`  
**Assembly date**: 2026-05-06  
**Assembly mode**: PATCH MODE  
**Phase**: 4D — Learner-Complete + Mastery-Enriched + HTML-Ready Master Assembly

## Phase 4D Certification

| Certificate | Status | Basis |
| --- | --- | --- |
| Learner-Standalone Certificate | PASS | PART A contains learner navigation, source metadata, §1–§8 learner body, approved figure markers, and no audit/process tables. |
| Zero-Omission Certificate | PASS | High-impact Scope/Audit/Crucible/PDF-required items are present, repaired earlier in Content Lock v2, or justifiably omitted; no HOLD_UNRESOLVED rows remain. |
| Mastery-Uplift Certificate | PASS | PART A includes seven bounded, adjacent, source-labeled mastery augmentations without broad rewriting. |
| Source-Boundary Certificate | PASS | All augmentations are labeled TEXTBOOK_DERIVED or CRUCIBLE_DERIVED and add no new page tags, unsupported values, or external examples. |
| HTML-Readiness Certificate | PASS | PART B contains Phase 5 rendering rules, figure/page-tag rules, navigation integrity rules, audit guardrails, splice table, and logs. |

## Assembly Mode

**PATCH MODE** — `15_Content Lock v2.1(2).md` is a Figure Marker Insertion Patch, not a full re-emitted learner body. The canonical learner-facing body was constructed from `15_Content Lock v2(3).md` §1–§8, with the seven approved Phase 4C marker blocks inserted after exact unique anchors. No scientific text was rewritten during splicing.

## Input Manifest

| File | Role | Authority level | Used for | Notes |
| --- | --- | --- | --- | --- |
| 15_scope_lock(3).md | Scope Lock | A0 | source boundary; learner; page range; image rights; hard rules | Used to constrain scope and figure rights. |
| 015_G_모델 구축의 기술 초기값·GOF·실험설계(4).pdf | Original textbook PDF | A1 | PDF verification source | Rendered to PNG for figure/table inspection; used only for source/page/figure verification and high-impact omission checks. |
| 15_Audit_Report_v1(5).md | Source Fidelity Audit | A2 | audit guardrail | MUST_FIX/SHOULD_FIX and forbidden-restoration guardrails applied. |
| 15_Content Lock v2(3).md | Content Lock v2 | A3 | canonical body | Primary text-final body; learner-facing §1–§8 used as canonical body. |
| 15_Content Lock v2.1(2).md | Phase 4C Figure Marker Insertion Patch | A4 | figure insertion source | PATCH MODE insertion map and marker blocks #1–#7 spliced into Content Lock v2. |
| 15_crucible_report_v1(1).md | Insight Crucible Report v1 | A5 | crucible guardrail | Used only for accepted high-value insight preservation and labeled mastery notes. |
| 붙여넣은 텍스트 (1)(89).txt | Phase 4D assembler prompt | A7 / process instruction | master assembly contract | Controls PART A/PART B structure, micro-patch gate, augmentation gate, and certification. |
| 붙여넣은 마크다운(2)(64).md | Step 2 HTML Compiler prompt / Prompt 5 | A7 | compiler instruction | Rendering, marker mapping, page-tag, navigation, and output constraints summarized in PART B. |
| 15_step1_draft_v0(3).md | Step 1 Draft v0 | A6 | deprecated source | Not used as learner-body source; only regression-prevention reference. |
| 15_Content Lock v1(2).md | Content Lock v1 | locked reference | reference only | Not used as canonical body because v2 supersedes it. |
| S15_phase1_patch memo(2).md | Phase 1 Patch Memo | audit support / locked reference | reference only | Already adjudicated through Audit/Content Lock; not used as raw learner content. |

## PART A — Learner-Facing Complete Handout

# Session 15 — 모델 구축의 기술: 초기값 · GOF · 모델 판별 · 실험 설계

**Source**: Gabrielsson & Weiner 5e, *Pharmacokinetic and Pharmacodynamic Data Analysis: Concepts and Applications*  
**Scope**: Ch.4 §4.4, §4.7–4.10 + Ch.5 §5.2.3–5.2.4, §5.3.3  
**Verified page range**: p.352–364 / p.368–392 / p.399–405 / p.412–414  
**Missing uploaded pages**: pp.365–367 (§4.5 Minimization, §4.6 Weighting) and pp.406–411 are not included in the uploaded PDF. Any dependence on these pages remains `[확인 필요]`.  
**Mode**: A-Critical  
**Learner-facing status**: Phase 4D learner-complete handout with approved figure markers and bounded mastery augmentation.

## Learner Navigation Aid

### How to use this handout

Read §1 first to lock the modeling carousel logic. Then study the six MUST cards in order: initial estimates → residual diagnostics → F-test/AIC/SC validity → precision/correlation → partial-derivative sampling → sensitivity analysis. After that, use §5 to prevent common confusions, §7 to test active recall, and §8 to compress the whole session into one workflow sentence.

### Learning route

| Route step | Focus | What you should be able to do before moving on |
|---:|---|---|
| 1 | §1 Roadmap | Explain why the session is one closed modeling loop rather than six isolated techniques. |
| 2 | MUST 1 | Derive starting values from graphical/NCA anchors and state why bad initial estimates can mislead fitting. |
| 3 | MUST 2 | Map residual shapes to structural, variance/weighting, or data/design problems. |
| 4 | MUST 3 | Decide when F-test, AIC, and SC are valid or invalid. |
| 5 | MUST 4 | Separate good curve fit from parameter identifiability. |
| 6 | MUST 5 | Translate derivative peaks into sampling locations. |
| 7 | MUST 6 | Use sensitivity analysis to decide where prediction or toxicokinetic interpretation may fail. |
| 8 | §5/§7/§8 | Resolve confusion pairs and answer self-tests without looking back. |

### Figure-use note

This handout does not reproduce copyrighted textbook figures. `FIGURE_POINTER` blocks tell the HTML compiler to render a text-only callout directing the learner to the original textbook figure or table. `FIGURE_SCHEMATIC` blocks specify newly redrawn or newly designed teaching schematics for Phase 5; Phase 4D does not generate HTML, Mermaid, SVG, or image files.

---

## §1 — Session Header & Roadmap

### 이 세션의 정확한 위치

본 세션은 p.352 Fig.4.16의 **modeling carousel**(← 모델링 한 사이클의 반복 구조) 중 Step 4 Explore data, Step 5 Fit model(s), Step 6 Analyze output를 다룬다. <!-- ANNOTATION --> 그 결과를 다음 실험의 Design으로 되돌리므로, 초기값 획득에서 시작해 GOF 판독, 경쟁 모델 선택, outlier 판단, 편미분 기반 sampling design, sensitivity analysis까지 이어지는 한 사이클의 실행 척추다. [p.352]

<!-- MASTER LENS -->
### Big Idea

이 범위의 핵심은 “좋은 통계량을 계산하는 법”이 아니라 **통계량을 적용해도 되는 조건을 아는 법**이다. F-test, AIC/SC, correlation coefficient, WRSS, partial derivatives는 각각 강력하다. 그러나 nested 조건, weighting 조건, residual randomness, parameter identifiability, sampling sensitivity를 벗어나면 이 숫자들은 오히려 잘못된 모델 확신을 만든다. [pp.369–391, pp.399–405]

### 개념 항법도

```text
[초기값 획득] → [잔차 진단] → [F-test/AIC/SC 모델 판별]
      ↑              ↓                  ↓
[민감도 분석] ← [편미분 sampling design] ← [정밀도·상관·설계]
```

<!-- ANCHOR -->
위 흐름은 닫힌 고리다. 초기값이 나쁘면 회귀가 잘못된 minimum으로 간다. 잔차가 무작위가 아니면 모델 또는 weighting이 틀린다. 모델 비교 조건을 어기면 통계 검정이 무의미하다. 그리고 파라미터가 상관되면 다음 실험의 sampling design을 바꿔야 한다. [p.353, pp.369–389, pp.399–405]

### 지식 그래프 위치

**선행 지식**: 1구획/다구획 모델, noncompartmental analysis, nonlinear regression, error model. Ch.4 §4.5 Minimization과 §4.6 Weighting은 pp.365–367 업로드 부재로 `[확인 필요 — pp.365–367 업로드 부재]`를 유지한다.

**후행 지식**: `[교과서 외 구현 번역]` 현대 PopPK에서는 이 세션의 residual diagnostics, parameter precision, −2·log likelihood 비교, design feedback가 NONMEM/PsN/xpose류 workflow로 번역된다. 단, 이 도구명들은 업로드 PDF의 직접 내용이 아니라 구현 환경의 번역이다.

<!-- RECAP -->
**§1 Recap**: 이 세션의 목적은 모델링 결과를 “좋아 보인다”가 아니라 “조건을 만족하므로 비교·해석 가능하다”로 바꾸는 것이다. 즉, 판단의 언어를 인상에서 조건으로 옮기는 것이다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.352, Fig.4.16, “From tentative model to plot of data.”
Why this matters: This figure is the source’s organizing spine for the session. It shows that EDA and initial estimates feed fitting, output analysis, and the next experiment rather than ending the process.
When to look: after reading §1 Recap, before entering MUST cards.
Learner instruction: Trace the arrow from Explore data to Fit model(s) to Analyze output, then back to Design. Read every MUST card as one part of this loop, not as an isolated technique.
<!-- /FIGURE_POINTER -->

> **Practice Lens — [CRUCIBLE_DERIVED]**  
> 이 세션은 “모델을 한 번 잘 맞추기”가 아니라, output을 다음 design으로 되돌리는 폐루프 사고를 훈련한다. 각 MUST 카드는 독립 기술이 아니라 다음 실험을 더 정보성 있게 만들기 위한 판단 장치로 읽어야 한다.

---

## §2 — Concept Anatomy Cards

### ▣ MUST 1 — 초기값 획득의 실전 기술 (Initial Estimate Acquisition)

<!-- MASTER LENS -->
**Big Idea**: 초기값은 회귀 알고리즘의 출발점이 아니라, 모델러가 EDA에서 추출해 알고리즘에 넘겨주는 **domain-informed prior**다. 즉, 알고리즘이 어디서 탐색을 시작할지 정하는 모델러의 첫 판단이다. Gabrielsson은 초기값이 나쁘면 wrong final values, unwanted local minima, physiologically impossible parameter values로 수렴할 수 있다고 경고한다. [p.353]

#### A. Formal Definition

Initial estimate acquisition은 nonlinear regression을 시작하기 전에 그래프, linear regression, NCA, prior compound knowledge로 starting parameter vector를 구성하는 절차다. 이 단계는 fit 이전에 끝나야 한다. 왜냐하면 nonlinear regression은 starting vector가 주어진 뒤에야 objective function surface를 탐색하기 때문이다. 이는 modeling carousel의 Explore data 단계에 속한다. [pp.352–353]

#### B. Source-locked derivation anchors

**B-1. IV bolus one-compartment example**: 두 피험자에게 동일한 10 mg IV bolus를 투여한 뒤 semi-log concentration–time plot에서 slope를 읽는다. 이 slope가 elimination rate constant $K$의 초기 anchor가 된다. [pp.353–354]

$$\text{slope}=\frac{\ln(800)-\ln(400)}{23-87}=-0.01\ \text{min}^{-1}=-K \quad [\text{Eq.4:16},\ p.354]$$

이로부터 다음 초기값이 이어진다. [p.354]

$$t_{1/2}=\frac{\ln2}{K}=\frac{0.693}{0.01}\approx65\ \text{min} \quad [\text{Eq.4:17}]$$

$$AUC=\frac{C^0}{K}=100{,}000\ \mu g\cdot L^{-1}\cdot\text{min} \quad [\text{Eq.4:18}]$$

$$Cl=0.1\ L\cdot\text{min}^{-1},\qquad V=10\ L \quad [\text{Eq.4:19–4:20}]$$

**B-2. Bi-exponential curve stripping**: [p.354]

$$C=Ae^{-\alpha t}+Be^{-\beta t}\quad [\text{Eq.4:21},\ p.354]$$

Terminal phase에서 $B$와 $\beta$를 먼저 읽고, back-extrapolated terminal line을 초기 phase에서 빼서 $A$와 $\alpha$를 얻는다. Fig.4.18의 anchor values는 $A=1.0\ \mu g\cdot L^{-1}$, $B=0.8\ \mu g\cdot L^{-1}$, $\alpha=0.05\ \text{min}^{-1}$, $\beta=0.003\ \text{min}^{-1}$이다. [p.355]

**B-3. Dynamic equilibrium response**: Response–concentration 관계에서는 lin-lin plot과 semi-log plot이 서로 다른 정보를 준다. Semi-log plot은 IC50 이하 구간을 확장해 IC50 initial estimate를 더 쉽게 읽게 한다. [pp.355–356]

**B-4. Dynamic non-steady-state turnover**: Warfarin이 prothrombin complex synthesis를 차단하면 downswing slope가 $-k_{out}$를 준다. [pp.356–357]

$$\text{slope}=\frac{\ln(124)-\ln(56.77)}{24-0}\approx -0.03\ h^{-1}\quad [\text{Eq.4:22},\ p.356]$$

이 식은 PDF에 표시된 형태를 보존한다. 다만 산술 부호에는 source-internal inconsistency가 있다. 수학적으로 재작성하려면 $[\ln(56.77)-\ln(124)]/(24-0)$ 또는 $[\ln(124)-\ln(56.77)]/(0-24)$가 된다. 따라서 이는 Draft source mismatch가 아니라 원문 내부 부호 문제다. Baseline 120 sec와 $k_{out}\approx0.03\ h^{-1}$로 $k_{in}=3.6\ \text{sec}\cdot h^{-1}$를 얻는다. [p.357]

**B-5. Indirect response model-choice example**: Eq.4:23–4:33은 baseline, steady state, $E_{max}$, $k_{out}$, $k_{in}$, exponent $n$를 그래프에서 순차 도출하는 예다. Table 4.3은 Model 1과 Model 4의 final estimates와 initial estimates를 비교하며, WRSS/AIC가 Model 1에서 7.3/83, Model 4에서 12/102로 제시된다. 이 예시는 “초기값 계산”이 곧 “모델 선택”의 전 단계임을 보여준다. [pp.358–360]

**B-6. Repeated-dose anxiolytic example**: Eq.4:34의 oral PK input은 $K_a=1.1\ h^{-1}$, $K=0.128\ h^{-1}$, $V/F=5.0\ L\cdot kg^{-1}$로 고정해 response model에 넣는다. PD turnover는 $dR/dt=k_{in}I(C)-k_{out}R$이고, $k_{out}\approx0.06\ h^{-1}$, $k_{in}=4.8$ units, $IC_{50}\approx0.25\ \mu g\cdot L^{-1}$가 initial anchor로 사용된다. [pp.361–363]

**B-7. When all else fails — boundary scaling**: 초기값을 직접 얻기 어렵다면 lower/upper boundary를 이용해 parameter를 0–1 범위로 scaling한다. [p.364]

$$\frac{IE-LB}{UB-LB}\quad [\text{Eq.4:44},\ p.364]$$

원문은 일반적으로 $0.1\cdot IE$부터 $10\cdot IE$까지의 relative range를 권한다. 그러나 Table 4.4처럼 source-specific boundary가 예외를 만들 수 있으므로, 이 규칙을 기계적으로 적용하면 안 된다. [p.364]

<!-- TRENCH -->
**Trench-Level Tip**: `[교과서 외 구현 번역]` Boundary scaling을 현대 nonlinear estimation에서 사용할 때 final estimate가 LB 또는 UB에 붙으면 model이 정보를 준 것이 아니라 boundary가 estimate를 만든 것일 수 있다. Table 4.4의 $\beta=0.05$와 UB=0.05는 그대로 모방할 prescription이 아니라 boundary dependence를 의심하게 하는 teaching example로 읽어야 한다. [p.364]

#### C. Structural Necessity

Bi-exponential curve stripping이 가능한 이유는 $\alpha \gg \beta$일 때 terminal phase에서 $Ae^{-\alpha t}$가 사라지고 $Be^{-\beta t}$만 남기 때문이다. 즉, semi-log plot은 시간 스케일 분리를 눈으로 확인하게 해주는 장치이며, 두 slope가 충분히 분리되지 않으면 curve stripping은 불안정하다. [pp.354–355]

#### D. Assumptions & Boundaries

초기값은 “정확한 값”일 필요는 없다. 그러나 physiologically plausible해야 하고, objective function surface에서 잘못된 basin으로 들어가지 않을 정도로는 근접해야 한다. 또한 compound knowledge base를 일찍 만들고 regression objective를 명확히 해야 한다. 그렇지 않으면 modeling은 끝없는 journey가 된다. [p.353]

<!-- RECAP -->
**MUST 1 Recap**: 초기값은 계산 전의 사전 판단이다. Graph → slope/intercept/plateau → initial estimates → regression이라는 순서를 바꾸면 알고리즘이 모델러의 눈을 대신할 수 없다.

<!-- FIGURE_SCHEMATIC -->
Title: Bi-exponential curve stripping: terminal-first logic
Mode: R
Visual objective: In 5 seconds, the learner should see that terminal slope is isolated first, then subtracted to reveal the initial slope.
Core message: Curve stripping works only when the fast and slow time scales are visually separable.
Elements to include: semi-log concentration–time axes; observed bi-exponential curve as a generic trajectory; terminal line labeled “read B and beta first”; back-extrapolated terminal line; residual initial line labeled “subtract terminal component → read A and alpha”; warning label “unstable if alpha ≈ beta.”
Elements to exclude: exact textbook visual style; dense tick marks or exact point replication; additional PK equations already present in the text.
Suggested rendering: SVG
Caption: A simplified redraw of the curve-stripping logic: terminal-phase information is extracted first, then removed to expose the initial phase.
Alt text: Semi-log concentration–time schematic showing a total bi-exponential curve, a terminal back-extrapolated line, and a residual initial line.
Source relation: Redrawn from textbook concept
<!-- /FIGURE_SCHEMATIC -->

> **Failure Mode — [TEXTBOOK_DERIVED]**  
> 초기값이 “대충 맞는 숫자”처럼 보여도 objective function의 잘못된 basin으로 들어가면 회귀는 그 오류를 스스로 고치지 못한다. 따라서 fit 전에 그래프, compound knowledge, regression objective를 먼저 명시하는 것이 초기값 계산의 일부다.

---

### ▣ MUST 2 — 잔차 기반 모델 진단 (Residual-Based Diagnostics)

<!-- MASTER LENS -->
**Big Idea**: Observed vs predicted curve만 보면 systematic error가 숨어 보인다. Residual plot은 이 숨은 오차를 부호와 순서로 다시 펼쳐준다. 따라서 모델이 놓친 구조, 시간 스케일, 또는 error model을 노출하는 최소 진단 도구다. [pp.368–370]

#### A. Formal Definition

Residual(← 관측값과 예측값의 차이)은 observed value와 calculated/predicted value 사이의 vertical distance다. <!-- ANNOTATION --> [p.369]

$$\epsilon=N(0,\sigma^2)\quad [\text{Eq.4:46},\ p.369]$$

$$residual_i=C_{obs,i}-\hat C_{calc,i}\quad [\text{Fig.4.41},\ p.369]$$

Weighted residual sum of squares는 다음과 같다. [p.371]

$$WRSS=\sum W_i(C_i-\hat C_i)^2\quad [\text{Eq.4:47},\ p.371]$$

$$\sigma=\sqrt{\frac{WRSS}{N_{obs}-N_{par}}}\quad [\text{Eq.4:48},\ p.371]$$

#### B. Diagnostic pattern catalogue

Residual은 random scatter가 되어야 한다. 따라서 consecutive positive/negative residuals가 run으로 나타나거나 cluster가 생기면, 단순 noise가 아니라 model inadequacy를 의심해야 한다. [pp.369–372]

- Residual vs time에서 banana/U-shape가 보이면 missing exponential term 또는 wrong structural time scale을 의심한다. [pp.372–376]
- Residual amplitude가 concentration과 함께 커지는 fan shape이면 constant variance assumption 또는 weighting이 틀렸을 수 있다. [pp.373–374]
- Ordinary Emax와 sigmoid Emax 비교에서는 predicted curve만으로 애매한 차이가 residual plot에서는 systematic deviation으로 드러난다. [pp.372–373]
- Weighting power/exponent는 source text에서 0, −1, −2, −n으로 설명되며, Eq.4:49는 $C_i^{-\lambda_z}$ 또는 $\hat C_i^{-\lambda_z}$ 형태를 쓴다. 따라서 “$\lambda_z=-1$”처럼 부호를 단정하지 말고 **weighting power/exponent**라고 표기한다. [pp.373–374]

<!-- ANCHOR -->
잔차 패턴은 단순한 그림 모양이 아니다. 이것은 “모델이 설명하지 못한 시간 스케일 또는 분산 구조”가 밖으로 드러난 형태다. Banana pattern은 빠른 phase가 빠졌다는 신호일 수 있고, fan pattern은 구조보다 error variance model의 문제일 수 있다. [pp.372–376]

#### C. Pure error vs lack-of-fit

Replicate measurement가 있는 in vitro dataset에서는 residual error를 pure error와 lack-of-fit으로 분해할 수 있다. Table 4.7의 예에서 residual SS 92.67, pure error SS 23.61, lack-of-fit SS 69.06이고, Eq.4:51의 $F_{LOF}=15.35$는 $F_{crit}=2.76$보다 커서 lack-of-fit를 지지한다. [pp.377–379]

$$F_{LOF}=\frac{(92.67-23.61)/(25-21)}{23.61/21}=15.35\quad [\text{Eq.4:51},\ p.379]$$

<!-- TRENCH -->
**Trench-Level Tip**: §4.7.3의 LOF F-test는 같은 x값에서 반복 측정이 있어 pure error를 계산할 수 있을 때만 가능하다. 환자별 sparse clinical PK처럼 같은 시점 반복이 없는 데이터에서는 LOF F-test를 억지로 만들지 말고 residual pattern과 model plausibility를 본다.

<!-- TRENCH -->
**Trench-Level Tip**: Residual vs time과 residual vs predicted/concentration을 함께 본다. 한 축에서 random scatter처럼 보여도 다른 축에서 fan shape나 structural run이 나타날 수 있다.

#### D. Structural Necessity

Model misspecification은 observed curve overlay보다 residual plot에서 먼저 보인다. Overlay는 curve와 data의 절대 위치를 보여준다. 반면 residual plot은 오차의 부호와 순서를 보존하므로 systematic deviation을 더 선명하게 드러낸다. [pp.369–376]

<!-- RECAP -->
**MUST 2 Recap**: GOF는 “curve가 지나가는가”가 아니라 “residual이 무작위인가”다. Residual pattern이 있으면 model, weighting, sampling design 중 하나가 정보를 잘못 처리하고 있다.

<!-- FIGURE_SCHEMATIC -->
Title: Residual pattern triage: shape → likely failure → next action
Mode: N
Visual objective: In 5 seconds, the learner should map each residual pattern to the correct diagnostic branch.
Core message: Residual shape determines whether the next action should target structure, weighting, or data/design.
Elements to include: four pattern boxes — random scatter, systematic run/banana, fan shape, isolated leverage point; diagnostic labels — acceptable randomness, structural time-scale error, variance/weighting error, outlier/leverage concern; action arrows — keep/check precision, revise structural model, revise error/weighting model, inspect source data and leverage; small warning “do not swap treatments: fan ≠ compartment problem; banana ≠ weighting-only problem.”
Elements to exclude: exact textbook residual plots; numerical thresholds; software-specific diagnostics not in Content Lock v2.
Suggested rendering: Mermaid flowchart or CSS-card
Caption: A diagnostic triage map linking residual shape to the most plausible modeling failure and next action.
Alt text: Flowchart connecting residual scatter, banana runs, fan-shaped spread, and leverage points to different modeling responses.
Source relation: Newly designed
<!-- /FIGURE_SCHEMATIC -->

> **Mastery Note — [CRUCIBLE_DERIVED]**  
> 잔차의 시간 패턴은 모델이 놓친 시간 스케일이 밖으로 드러난 흔적이다. Banana/run을 weighting 문제 하나로 덮거나, fan shape를 구조 모델 추가로 해결하려 하면 원인과 처방이 어긋난다.

---

### ▣ MUST 3 — F 검정 적용 조건 (F-Test Validity Conditions) ⚡ Apex Concept

<!-- MASTER LENS -->
**Big Idea**: F-test는 “더 복잡한 모델이 WRSS(← weighted residual sum of squares)를 줄였는가”를 묻는 도구가 아니다. <!-- ANNOTATION --> **Full model과 reduced model이 hierarchical/nested이고, 같은 weighting scheme으로 fit되었을 때만** 추가 parameter의 의미를 검정하는 도구다. [pp.387–388]

#### A. Formal Definition

Nested model(← full model의 제한 형태)이란 full model에서 특정 parameter를 고정하면 reduced model로 collapse되는 관계다. <!-- ANNOTATION --> Sigmoid Emax model은 exponent $n=1$로 고정하면 ordinary Emax model이 되므로 nested 관계다. [p.388]

F statistic은 다음 구조를 갖는다. [p.387]

$$F^*=\frac{(WRSS_{reduced}-WRSS_{full})/(df_{reduced}-df_{full})}{WRSS_{full}/df_{full}}\quad [\text{Eq.4:54},\ p.387]$$

$$df=N_{obs}-N_{par}\quad [\text{Eq.4:55},\ p.387]$$

#### B. Valid vs invalid examples

- **Valid**: ordinary Emax vs sigmoid Emax. Full sigmoid model에서 $n=1$을 고정하면 ordinary Emax로 줄어든다. [p.388]
- **Invalid**: ordinary Emax vs linear response. $C\ll EC_{50}$라는 제한 상황에서만 근사적으로 연결될 뿐, 일반적으로 nested comparison이 아니다. [p.388]
- **Conditionally valid**: hepatic distributed model과 parallel-tube model은 reduced relation이 성립하는 경우 F-test를 사용할 수 있다. [pp.388–389]
- **Invalid with double violation**: Table 4.8의 Michaelis–Menten weighted fit과 first-order unweighted fit은 non-nested이고 weighting도 달라 F-test도 AIC도 사용할 수 없다. [p.389]

#### C. Structural Necessity

<!-- ANCHOR -->
Nested 조건은 parameter 개수 차이가 아니라 **한 모델이 다른 모델의 제한된 형태인가**의 문제다. `[교과서 외 해석]` 기하학적으로 말하면 reduced model은 full model parameter space 안의 제한된 부분공간이어야 한다. 그래야 WRSS 감소량이 “추가 parameter가 설명한 개선”으로 해석된다.

#### C-2. Plausible Fallacy

**Fallacy**: “WRSS가 더 낮고 parameter가 하나 더 많으니 F-test를 쓰면 된다.”  
**Correction**: WRSS 감소량은 같은 error/weighting model과 nested 구조 안에서만 F 분포와 연결된다. Non-nested 구조에서는 두 WRSS가 같은 검정 좌표계 위에 있지 않다. [pp.387–389]

#### D. AIC/SC boundary

AIC와 SC는 nested model을 요구하지 않지만, equal weighting은 요구한다. [p.389]

$$AIC=N_{obs}\ln(WRSS)+2N_{par}\quad [\text{Eq.4:56},\ p.389]$$

$$SC=N_{obs}\ln(WRSS)+N_{par}\ln(N_{obs})\quad [\text{Eq.4:57},\ p.389]$$

AIC/SC의 lowest value가 자동으로 adequate model을 뜻하지 않는다. GOF(← model adequacy의 종합 진단)는 residuals, parameter precision, accuracy, correlation matrix, condition number, F-test, AIC/SC를 함께 보는 battery of tools다. <!-- ANNOTATION --> [pp.387–391]

#### E. WRSS vs −2·log likelihood

원문은 historical WRSS 기반 프로그램과 modern −2·log likelihood 기반 프로그램을 구분하되, 비교 원리는 동일하게 model adequacy criteria와 연결된다고 설명한다. [p.386] `[교과서 외 구현 번역]` NONMEM의 OFV 비교로 번역할 수는 있지만, ΔOFV threshold나 SCM rule은 이 PDF의 직접 내용이 아니다.

<!-- RECAP -->
**MUST 3 Recap**: F-test는 nested + equal weighting일 때만 쓴다. AIC/SC는 nested를 요구하지 않지만 equal weighting을 요구하며, 어느 경우든 residual과 biology를 대체하지 못한다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.389, Table 4.8, Michaelis–Menten weighted fit vs first-order unweighted fit comparison.
Why this matters: Table 4.8 is the compact source example showing why F-test and AIC can both become invalid when model structure and weighting differ. It operationalizes the Apex rule.
When to look: after reading MUST 3 Recap.
Learner instruction: Identify the two violations separately: non-nested model structure and different weighting. Do not collapse them into a vague statement that “models are different.”
<!-- /FIGURE_POINTER -->

> **Judgment Lens — [CRUCIBLE_DERIVED]**  
> Nested 조건은 단순히 parameter 수가 다른 관계가 아니라, 두 모델이 같은 비교 좌표계 위에 놓여 있다는 조건이다. 이 조건이 없으면 WRSS 감소량은 “추가 parameter의 기여”가 아니라 서로 다른 문제에서 나온 두 숫자의 차이가 된다.

---

### ▣ MUST 4 — 파라미터 정밀도와 상관 (Parameter Precision & Correlation)

<!-- MASTER LENS -->
**Big Idea**: 좋은 fit은 좋은 parameter를 보장하지 않는다. Parameter precision과 correlation은 모델 자체보다 **sampling design이 parameter를 서로 분리해 보여주었는가**에 좌우된다. 즉, 같은 식이라도 잘못 찍은 시간점에서는 parameter들이 서로 구별되지 않는다. [pp.380–385]

#### A. Accuracy, precision, and CV%

Accuracy는 bias와 관련되고, precision은 estimate의 uncertainty와 관련된다. 즉, 평균적으로 맞는가와 반복하면 얼마나 좁게 모이는가는 다른 질문이다. 원문은 dartboard를 통해 accurate/inaccurate와 precise/imprecise를 구분한다. [pp.379–380]

$$CV\%=\frac{SE(\hat p)}{\hat p}\cdot100\quad [\text{Eq.4:52},\ p.380]$$

$p=0.01\pm0.005\ h^{-1}$의 CV 50% 예시는 “높은 uncertainty”를 보여주는 예시일 뿐, PDF-defined rejection threshold가 아니다. [p.380]

#### B. Correlation coefficient r is not GOF

PDF는 correlation coefficient가 가장 많이 오용되는 GOF 기준 중 하나라고 설명한다. Eq.4:53은 원문 표기를 보존한다. [p.381]

$$r=1-\frac{\sum(C_i-\hat C_i)^2}{\sum(C_i-\bar C)^2}\quad [\text{Eq.4:53 source form},\ p.381]$$

Fig.4.53에서 OLS fit은 $r=0.96$이지만 마지막 세 관측치를 systematic하게 underestimate하고, IRLS fit은 $r=0.94$이지만 전체적으로 더 나은 fit을 보인다. 따라서 높은 r은 좋은 fit의 충분조건이 아니다. [p.382]

<!-- CONFUSION -->
`[교과서 외 해석]` Dynamic range가 넓은 concentration–time data에서는 r이 모델의 잔차 구조보다 전체 값의 범위에 강하게 끌릴 수 있다. 그래서 r은 residual plot과 함께 읽어야지 단독 GOF 판정 기준으로 쓰면 안 된다.

#### C. Parameter correlation and ridge geometry

Parameter correlation matrix는 parameter들이 독립적으로 estimate되는지, 또는 서로 trade-off하는지를 보여준다. 원문은 high correlation이 fewer parameters 또는 more data 필요성을 시사한다고 설명한다. [pp.382–383]

<!-- ANCHOR -->
Fig.4.55–4.57의 핵심은 **ridge minimum**(← 길게 늘어진 최솟값 영역)이다. <!-- ANNOTATION --> 두 parameter가 ridge 위에서 같이 움직이면 OFV/WRSS가 거의 변하지 않는다. 이 때문에 univariate estimate는 그럴듯해도 joint uncertainty는 크다. Design A/B 비교는 같은 모델도 sampling design에 따라 Cl/V 또는 IC50/Imax correlation이 크게 달라짐을 보여준다. [pp.383–385]

#### D. Fixing one parameter

Fig.4.55는 한 parameter를 고정하면 다른 parameter의 confidence interval이 작아질 수 있음을 보여준다. [pp.383–384] 그러나 `[교과서 외 실무 해석]` fix 전략은 정당화 부담을 통계에서 biology/literature/prior study로 옮긴다. 따라서 fix value의 출처와 적용 가능성을 설명하지 못하면, precision이 좋아진 것이 아니라 uncertainty를 숨긴 것이다.

#### E. Limitations

High correlation에 대한 universal cutoff는 PDF에 없다. $|r|>0.95$ 같은 hard threshold 대신, correlation matrix, confidence ellipse, residual pattern, design adequacy를 함께 읽는다. `[교과서 외 구현 번역]` Condition number나 covariance-step warning은 현대 구현에서 유용한 신호지만, 이 PDF의 직접 teaching point는 “correlation은 design의 결과”라는 점이다.

<!-- RECAP -->
**MUST 4 Recap**: Fit이 좋아 보여도 parameter가 식별되지 않을 수 있다. Precision은 모델이 아니라 설계가 만든다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.382, Fig.4.53; pp.383–385, Fig.4.55–4.57.
Why this matters: Fig.4.53 demonstrates that a higher r can still hide systematic terminal bias. Fig.4.55–4.57 then show that even a plausible fit can have poorly identified correlated parameters.
When to look: after reading MUST 4 Recap, before §5 confusion pairs.
Learner instruction: First compare r=0.96 versus r=0.94 and ask which fit is structurally better. Then inspect the confidence ellipses/design comparison and ask whether the parameter pair is truly identifiable.
<!-- /FIGURE_POINTER -->

> **Mastery Note — [CRUCIBLE_DERIVED]**  
> Ridge minimum을 떠올리면 parameter correlation의 의미가 분명해진다. 능선 위 여러 지점이 거의 같은 WRSS를 주기 때문에, estimate 하나가 그럴듯해도 joint uncertainty는 크게 남을 수 있다.

---

### ▣ MUST 5 — 편미분 기반 최적 샘플링 (Partial-Derivative Optimal Sampling)

<!-- MASTER LENS -->
**Big Idea**: Partial derivative plot(← 파라미터 변화에 대한 예측 변화율 그림)은 “어디서 sample하면 어떤 parameter가 가장 잘 보이는가”를 말해준다. <!-- ANNOTATION --> 예측값이 parameter 변화에 민감한 시간·농도 영역이 그 parameter를 estimate하는 정보의 중심이다. [pp.399–403]

#### A. Bi-exponential derivative design

원문은 bi-exponential model을 예로 든다. [p.399]

$$C=Ae^{-\alpha t}+Be^{-\beta t}\quad [\text{Eq.5:7},\ p.399]$$

$A$와 $B$에 대한 derivatives는 intercept 영역에서, $\alpha$와 $\beta$에 대한 derivatives는 각각 $t=1/\alpha$, $t=1/\beta$에서 극값을 갖는다. [pp.399–400]

$$t=\frac{1}{\alpha},\qquad t=\frac{1}{\beta}\quad [\text{Eq.5:11},\ p.400]$$

예시 parameter가 $\alpha=0.69\ h^{-1}$, $\beta=0.069\ h^{-1}$이면 optimal time은 약 1.4 h와 14 h다. Fig.5.4의 plotted example에서는 $\alpha$와 $\beta$ 정보가 각각 약 20 min, 300 min 부근에 모인다. [p.400]

#### B. Sigmoid Imax / Emax design

Sigmoid Imax model의 derivatives는 $IC_{50}$ 정보가 half-maximal effect 부근에, sigmoidicity factor $n$ 정보가 20%와 80% effect level 부근에 집중됨을 보여준다. Fig.5.6은 $E_0$, $n$, $EC_{50}$, $n$, $E_{max}$에 대한 다섯 design points를 제시한다. [pp.400–402]

#### C. Turnover model design

Turnover response model에서는 $k_{out}$ sensitivity가 25 h와 약 100 h post-dose에서 크고, early time에서는 $k_{out}$가 $IC_{50}$ 또는 $n$보다 민감하다. 따라서 early sampling은 $k_{out}$ initial estimate를 직접 강화한다. [pp.402–404]

#### D. Structural Necessity

<!-- ANCHOR -->
편미분이 큰 위치는 prediction이 해당 parameter 변화에 크게 흔들리는 위치다. `[교과서 외 해석]` 이를 likelihood surface 언어로 바꾸면, 그 위치의 관측치는 해당 parameter 방향의 surface curvature를 키워 minimum을 더 좁고 깊게 만든다.

<!-- TRENCH -->
**Trench-Level Tip**: `[교과서 외 구현 번역]` Parameter 단위가 다르면 raw $\partial C/\partial\theta$ 크기 비교가 왜곡될 수 있다. 실무에서는 $\theta_i(\partial C/\partial\theta_i)/C$ 같은 normalized sensitivity를 함께 보아 parameter 간 비교를 안정화한다.

#### E. Boundary Conditions

True parameter values를 사전에 알 수 없으므로, derivative maxima에만 sample을 몰아넣으면 안 된다. 전체 concentration range에도 추가 samples를 두어야 한다. 원문은 pooled data를 무비판적으로 design decision에 쓰는 위험도 경고한다. [p.402]

<!-- RECAP -->
**MUST 5 Recap**: 최적 샘플링은 촘촘히 많이 찍는 것이 아니라, 각 parameter가 가장 크게 보이는 곳을 의도적으로 찍는 것이다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, pp.400–402, Fig.5.4–5.6; p.403, Fig.5.8.
Why this matters: These figures are the core visual evidence that derivative peaks define informative sampling regions. Without the plots, the rule “sample where sensitivity is high” remains too abstract.
When to look: after reading MUST 5 Recap.
Learner instruction: For each derivative curve, point to the time or concentration region where the curve is largest in magnitude. Translate that region into a sampling design point.
<!-- /FIGURE_POINTER -->

> **Practice Lens — [CRUCIBLE_DERIVED]**  
> 편미분 peak는 “그 parameter가 보이는 시간 또는 농도 영역”을 표시한다. 다만 true parameter가 아직 불확실하므로, peak 주변만 찍는 설계가 아니라 전체 range를 보존하는 보완 sampling이 함께 필요하다.

---

### ▣ MUST 6 — 민감도 분석 (Sensitivity Analysis)

<!-- MASTER LENS -->
**Big Idea**: Sensitivity analysis(← parameter perturbation의 예측 영향 점검)는 fitting 후 해석이 아니다. <!-- ANNOTATION --> 다음 실험을 설계하기 전 “어떤 parameter uncertainty가 prediction을 얼마나 흔드는가”를 보는 pre-fitting stress test다. [pp.403–405]

#### A. Formal Definition

Sensitivity analysis는 특정 parameter를 일정 비율로 변화시켜 concentration–time 또는 response–time prediction이 어떻게 달라지는지 보는 절차다. 즉, parameter uncertainty가 실제 prediction uncertainty로 얼마나 번역되는지를 본다. 원문의 예시는 parameter를 +100% 또는 −50%로 변화시켜 model output 변화를 비교한다. [pp.404–405]

#### B. PK sensitivity example

Michaelis–Menten pharmacokinetic model에서 $V_{max}$, $K_M$, $V_c$, $V_t$를 변화시키면 concentration–time profile의 어느 구간이 어떤 parameter에 민감한지 드러난다. Fig.5.9는 이것을 future sampling location 결정에 연결한다. [p.405]

#### C. PD sensitivity example

Warfarin-PCA model에서는 $IC_{50}$, $k_{in}$, $k_{out}$, $t_{lag}$의 변화가 response-time profile에 미치는 영향을 비교한다. Fig.5.10의 목적은 “어떤 parameter를 더 잘 estimate하려면 어느 구간을 보강해야 하는가”를 읽는 것이다. [p.405]

#### D. Toxicokinetic design context

Toxicokinetic design에서 chronic studies는 보통 exposure 확인을 위해 Cmax sampling만으로 충분한 경우가 있으나, 예외가 있으며 investigator judgment가 필요하다. Table 5.6은 PK/DRF/chronic study type별로 profile 또는 Cmax 중심 sampling package를 구분한다. [p.413]

Nonlinear elimination에서는 concentration이 first-order linear kinetics 또는 negligible level에 도달할 때까지 sampling하지 않으면 true extrapolated AUC to infinity를 얻을 수 없다. [p.414]

Capacity-dependent kinetics와 time-dependent kinetics가 동시에 존재하면 Day 1 AUC와 steady-state AUC 비교가 상쇄될 수 있다. 이 경우 interpretation은 흐려진다. Fig.5.20의 핵심은 exposure가 변하지 않는 것처럼 보여도 capacity와 induction이 동시에 작동할 수 있다는 점이다. [p.414]

<!-- TRENCH -->
**Trench-Level Tip**: Sensitivity analysis는 parameter를 “잘 추정했는지”보다 먼저 “잘못 추정하면 어떤 결론이 흔들리는지”를 묻는다. 흔들리는 결론이 dose, safety margin, sampling schedule이면 다음 실험 설계를 바꿔야 한다.

<!-- RECAP -->
**MUST 6 Recap**: Partial derivative가 “어디서 정보가 생기는가”를 말한다면, sensitivity analysis는 “정보가 부족하면 결론이 어디서 무너지는가”를 말한다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.405, Fig.5.10; p.414, Fig.5.20.
Why this matters: Fig.5.10 shows how parameter perturbations alter response-time profiles. Fig.5.20 shows the toxicokinetic trap where capacity-dependent and time-dependent processes can mask each other in exposure interpretation.
When to look: after reading MUST 6 Recap, before moving to §5 confusion pairs.
Learner instruction: In Fig.5.10, identify which profile region moves when each parameter is perturbed. In Fig.5.20, focus on why similar-looking exposure summaries can hide two simultaneous kinetic processes.
<!-- /FIGURE_POINTER -->

> **Failure Mode — [TEXTBOOK_DERIVED]**  
> Toxicokinetic design에서 exposure summary가 비슷해 보여도 capacity-dependent process와 time-dependent process가 서로 상쇄될 수 있다. 따라서 sensitivity analysis는 수치가 변했는지보다 어떤 결론이 가려질 수 있는지를 묻는 단계다.

---

## §5 — Confusion Pair Dissection

### ▣ 혼동쌍 #1 — Nested + equal weighting vs non-nested 또는 different weighting

<!-- CONFUSION -->
| 항목 | 올바른 판정 |
|---|---|
| 흔한 오해 | “더 복잡한 모델이 WRSS를 줄이면 F-test를 쓴다.” |
| Source correction | F-test는 hierarchical/nested model에서만 가능하고, equal weighting이 필요하다. [pp.387–388] |
| AIC/SC boundary | AIC/SC는 nested를 요구하지 않지만 equal weighting은 요구한다. [p.389] |
| Critical example | Table 4.8의 Michaelis–Menten weighted model vs first-order unweighted model은 F-test도 AIC도 사용할 수 없다. [p.389] |
| 변화 방향 | 통계 검정 하나로 결론 내리지 말고 residual pattern, mechanism plausibility, external evidence, visual prediction을 triangulate한다. |

<!-- TRENCH -->
Weighting 선택은 관행이 아니라 residual pattern으로 정당화한다. Fan shape이면 relative error weighting을 의심한다. 반대로 잔차 폭이 균질하면 constant absolute error가 더 자연스럽다. [pp.373–374]

**기억 고리**: F-test는 “nested + same weighting”이라는 잠금장치가 맞아야 열린다. 하나라도 맞지 않으면 낮은 WRSS는 검정 통계량이 아니라 단순한 숫자다.

---

### ▣ 혼동쌍 #2 — Correlation coefficient r vs 진정한 GOF

<!-- CONFUSION -->
| 항목 | 올바른 판정 |
|---|---|
| 흔한 오해 | “r이 높으면 fit이 좋다.” |
| Source correction | Fig.4.53에서 OLS는 r=0.96이지만 terminal observations를 underestimate하고, IRLS는 r=0.94이지만 더 나은 pattern을 보인다. [p.382] |
| 왜 위험한가 | r은 residual sign/run, variance pattern, terminal bias를 직접 보여주지 못한다. [pp.381–382] |
| 필요한 증거 | observed/predicted overlay + residual vs time + residual vs prediction/concentration + parameter precision. |

`[교과서 외 해석]` PK data처럼 y-range가 넓으면 r은 dynamic range의 영향을 크게 받을 수 있다. 따라서 r은 “전체 설명력”의 보조 숫자일 뿐, GOF 판정의 주연이 아니다.

**기억 고리**: r은 curve의 큰 방향을 본다. Residual plot은 모델이 어디서 거짓말하는지 본다.

---

### ▣ 혼동쌍 #3 — Structural model error vs variance/weighting model error

<!-- CONFUSION -->
| 항목 | Structural model error | Variance/weighting model error |
|---|---|---|
| 전형적 residual | Banana, U-shape, systematic runs | Fan shape, concentration-dependent spread |
| 원인 | 빠진 compartment, wrong Emax shape, lag-time omission | constant variance 가정 오류, weighting mismatch |
| 처방 | 구조 모델 수정, phase/time-scale 추가 | error model 또는 weighting 재검토 |
| Source anchor | Residual pattern examples and common residual plots [pp.372–376] | Weighting and error distribution examples [pp.373–374] |

<!-- TRENCH -->
두 종류의 오류를 바꿔 처방하면 모델이 더 복잡해지기만 한다. 예를 들어 fan shape에 compartment를 추가하거나 banana pattern에 weighting만 바꾸면, 문제의 원인은 그대로 남는다.

**기억 고리**: 모양이 휘면 구조를 의심하고, 폭이 벌어지면 variance를 의심한다.

---

### ▣ 혼동쌍 #4 — Outlier A vs Outlier B

<!-- CONFUSION -->
| 항목 | Outlier A | Outlier B |
|---|---|---|
| Source description | Vertical deviation from true curve | Time-axis deviation with high leverage |
| 영향 | Precision 감소 | Bias를 만들면서 precision이 좋아 보일 수 있음 |
| 위험 | noisy point로 보임 | 잘못된 curve를 강하게 끌고 감 |
| Source anchor | Fig.4.59 [p.390] | Fig.4.59 [p.390] |

원문은 table만 보면 A와 B의 deviating points를 거의 알아보기 어렵다고 강조한다. 따라서 outlier 판단에서는 graphical presentation이 매우 중요하다. [p.390]

`[교과서 외 통계 도구]` Cook’s distance나 hat matrix는 현대 회귀 진단에서 유용하지만, 이 PDF의 핵심은 먼저 plot에서 leverage와 vertical deviation을 구분하는 것이다.

**기억 고리**: A는 위아래로 튄 점이고, B는 시간을 잘못 말하는 점이다. B가 더 위험한 이유는 curve의 방향을 바꾸기 때문이다.

---

## §7 — Self-Test: Active Recall Module

### Q1. [회상 ★★]

<!-- SELF-TEST -->
**문제**: 초기값이 부실할 때 Gabrielsson이 명시한 세 가지 위험은 무엇인가? [p.353]

**정답**: wrong final values, unwanted local minima, physiologically impossible parameter values. 초기값은 nonlinear regression에서 단순한 편의값이 아니라 algorithm이 어떤 basin으로 들어갈지 결정하는 EDA 산출물이다.

---

### Q2. [계산 ★★]

<!-- SELF-TEST -->
**문제**: 10 mg IV bolus 예시에서 semi-log slope가 −0.01 min⁻¹일 때 $t_{1/2}$, AUC, Cl, V의 source anchor 값을 쓰라. [p.354]

**정답**: $t_{1/2}\approx65$ min, $AUC=100{,}000\ \mu g\cdot L^{-1}\cdot min$, $Cl=0.1\ L\cdot min^{-1}$, $V=10\ L$. [Eq.4:17–4:20]

---

### Q3. [회상 ★]

<!-- SELF-TEST -->
**문제**: Bi-exponential curve stripping에서 terminal phase를 먼저 읽는 이유는 무엇인가? [pp.354–355]

**정답**: terminal phase에서는 빠른 exponential term $Ae^{-\alpha t}$가 거의 사라지고 $Be^{-\beta t}$가 지배하므로, $B$와 $\beta$를 먼저 얻은 뒤 이를 back-extrapolate하여 초기 phase에서 빼면 $A$와 $\alpha$를 얻을 수 있다.

---

### Q4. [진단 ★★]

<!-- SELF-TEST -->
**문제**: Residual plot에서 banana pattern과 fan shape가 각각 시사하는 문제는 무엇인가? [pp.372–376]

**정답**: Banana/U-shape는 structural time-scale 문제, 예를 들어 빠진 exponential term이나 wrong model shape를 의심하게 한다. Fan shape는 concentration-dependent variance 또는 weighting mismatch를 의심하게 한다.

---

### Q5. [Apex 적용 ★★]

<!-- SELF-TEST -->
**문제**: Ordinary Emax model과 sigmoid Emax model 비교에는 F-test를 쓸 수 있는가? Linear response model과 ordinary Emax model 비교에는 어떤가? [p.388]

**정답**: Ordinary Emax vs sigmoid Emax는 sigmoid model에서 $n=1$로 고정하면 ordinary Emax가 되므로 nested이고 F-test 가능하다. Linear response vs ordinary Emax는 일반적으로 nested가 아니므로 F-test를 쓰면 안 된다.

---

### Q6. [판정 ★★]

<!-- SELF-TEST -->
**문제**: Michaelis–Menten weighted fit과 first-order unweighted fit에서 AIC가 더 낮은 모델을 선택해도 되는가? [p.389]

**정답**: 안 된다. Table 4.8은 두 모델이 non-nested이고 weighting도 다르므로 F-test도 AIC도 쓸 수 없음을 보여준다. AIC/SC는 nested를 요구하지 않지만 equal weighting은 요구한다.

---

### Q7. [계산/개념 ★★]

<!-- SELF-TEST -->
**문제**: Table 4.7의 residual SS 92.67, pure error SS 23.61, df 25와 21로 계산한 $F_{LOF}$는 무엇이며 어떤 결론인가? [pp.378–379]

**정답**: $F_{LOF}=[(92.67-23.61)/(25-21)]/(23.61/21)=15.35$이고, $F_{crit}=2.76$보다 커서 lack-of-fit가 있다. 단, 이 검정은 replicate measurement가 있어 pure error를 분리할 수 있을 때만 가능하다.

---

### Q8. [설계 ★★]

<!-- SELF-TEST -->
**문제**: Fig.4.55–4.57에서 design A와 design B가 가르치는 핵심은 무엇인가? [pp.383–385]

**정답**: Parameter correlation과 confidence ellipse는 model equation만의 문제가 아니라 sampling design의 결과다. 좋은 design은 두 parameter가 서로 trade-off하지 않도록 정보 영역을 분리해 confidence interval과 correlation을 줄인다.

---

### Q9. [Boss Dilemma ★★]

<!-- SELF-TEST -->
**문제**: 두 competing model이 있다. 하나는 lower WRSS를 보이지만 다른 weighting을 사용했고, 다른 하나는 mechanistically plausible하지만 AIC 차이가 작다. 어떤 결정을 내려야 하는가?

**정답**: 먼저 같은 weighting으로 재적합해 비교 가능성을 확보한다. 그래도 F-test/AIC가 단독 결론을 주지 못하면 residual pattern, mechanism plausibility, external data, visual prediction을 함께 triangulate한다. PDF는 AIC difference threshold를 정의하지 않는다. 따라서 낮은 AIC 하나만으로 mechanistic plausibility를 이길 수 없다. [p.389, p.391]

---

## §8 — Meta-Frame & Big Picture

### A. Positioning

<!-- MASTER LENS -->
이 세션은 PK/PD 모델링에서 “모델을 세우는 기술”보다 “모델을 버리거나 다시 설계하는 기술”에 가깝다. Initial estimates는 fit의 출발점을 정한다. Residuals는 모델 결함을 드러낸다. F-test/AIC/SC는 비교 조건을 제한한다. Precision/correlation은 설계의 약점을 노출한다. 그리고 partial derivatives와 sensitivity analysis는 다음 실험의 sampling을 바꾼다. [p.353, pp.369–391, pp.399–405]

`[교과서 외 구현 번역]` 현대 PopPK workflow에서 이 한 사이클의 실무 단위는 단일 run이 아니라 **model/control file 한 버전 + GOF diagnostic plot set + 다음 cohort sampling recommendation**이다. 세 가지가 함께 닫혀야 modeling carousel이 완주된다.

### B. Dependency chain

1. 초기값이 틀리면 convergence가 틀릴 수 있다. [p.353]  
2. Residual이 systematic하면 GOF가 성립하지 않는다. [pp.369–376]  
3. Non-nested 또는 different weighting comparison이면 F-test/AIC가 무력화된다. [pp.387–389]  
4. Parameter correlation이 높으면 next design이 필요하다. [pp.382–385]  
5. Partial derivatives와 sensitivity analysis가 그 next design의 위치를 정한다. [pp.399–405]

### C. Professional moat

경험 많은 모델러는 “어느 모델의 AIC가 낮은가”만 보지 않는다. 두 모델이 비슷한 WRSS/AIC를 보이는데 residual pattern과 mechanism이 모두 애매하면, 어느 한쪽을 고르기 전에 **둘 다 wrong mechanism일 가능성**을 의심한다. 이 역방향 추론이 model selection을 parameter-count game이 아니라 mechanistic hypothesis revision으로 바꾼다.

### D. GOF checklist locked from Table 4.9

<!-- RECAP -->
모델 적합성은 최소한 다음 다섯 질문으로 닫아야 한다. [p.391]

| Checklist question | Locked interpretation |
|---|---|
| Does the model have biological relevance? | Mechanistic plausibility가 없는 낮은 AIC는 취약하다. |
| Does the fitted curve mimic trends in the data? | Curve overlay는 첫 관문이다. |
| Are the parameters estimated with adequate precision? | CV%, SE, confidence intervals를 본다. |
| Do the residuals show lack of systematic deviation? | Run, banana, fan, lag-time pattern을 본다. |
| Do residual plots display random scatter? | 잔차가 무작위가 아니면 모델 또는 weighting을 다시 본다. |

### E. Final locked summary

<!-- RECAP -->
이 세션의 압축 명제는 다음과 같다.

> **초기값은 알고리즘의 출발점을 정하고, residual은 모델의 거짓말을 드러내며, F-test/AIC는 비교 가능한 모델에서만 의미가 있고, precision/correlation은 설계의 품질을 말하며, partial derivative와 sensitivity analysis는 다음 실험을 어디서 다시 해야 하는지 알려준다.**

이 문장을 체화하면 p.352의 modeling carousel은 단순한 그림이 아니라 실제 workflow가 된다: Explore data에서 initial estimates를 만들고, Fit model 후 Analyze output에서 residual/precision/comparison을 검토하며, 그 결과로 다음 Design을 수정한다. [p.352, p.392, pp.399–405]


## PART B — Compiler-Only Appendix

This appendix is not learner-facing. It exists only to protect Phase 5 rendering fidelity and prevent regression. Phase 5 must render PART A only unless explicitly instructed otherwise.

### B1. Compilation Contract

- PART A is the only learner-facing body.
- Phase 5 must render PART A without altering scientific content, equations, source page tags, or markers.
- PART B is instruction/guardrail only and must not be rendered as learner content.
- Do not restore deprecated material from Step 1 Draft v0.
- Do not add new scientific content, new equations, new page tags, new examples, or new figures.
- Do not generate HTML from PART B tables except as internal compiler guidance if explicitly requested.

### B2. Figure Rendering Instructions

**Image rights**: None. Do not embed copyrighted textbook images. Render `FIGURE_POINTER` as text-only callouts. Render `FIGURE_SCHEMATIC` as newly created, visually distinct teaching schematics according to the marker brief. Do not propose or add figures beyond the approved KEEP list.

#### Approved Figure Inventory

| # | Mode | Source figure/table | Location | Phase 5 rendering decision |
| --- | --- | --- | --- | --- |
| 1 | P | Fig.4.16 p.352 | §1 after Recap | Render as text-only pointer callout; no textbook image. |
| 2 | R | Fig.4.18 p.355 concept | MUST 1 after Recap | Render as distinct schematic; do not reproduce textbook figure. |
| 3 | N | Synthesis from residual figures pp.372–376 | MUST 2 after Recap | Render as new diagnostic triage schematic. |
| 4 | P | Table 4.8 p.389 | MUST 3 after Recap | Render as text-only pointer callout; no table image. |
| 5 | P | Fig.4.53 p.382; Fig.4.55–4.57 pp.383–385 | MUST 4 after Recap | Render as text-only pointer callout. |
| 6 | P | Fig.5.4–5.6 pp.400–402; Fig.5.8 p.403 | MUST 5 after Recap | Render as text-only pointer callout. |
| 7 | P | Fig.5.10 p.405; Fig.5.20 p.414 | MUST 6 after Recap | Render as text-only pointer callout. |

#### Rejected Figure Inventory — Do Not Restore

| # | Source | Decision | Reason |
| --- | --- | --- | --- |
| 8 | Fig.4.21 p.357; Table 4.3 p.360 | REJECT | Budget; lower ROI than Fig.4.18; content already preserved in MUST 1. |
| 9 | Fig.4.59 p.390 | REJECT | Budget; outlier distinction already stated in confusion pair. |
| 10 | Table 4.9 p.391 | REJECT | Redundant with §8 checklist. |

### B3. Page Tag Rendering Rules

- Preserve all `[p.XX]`, `[pp.XX–YY]`, `[pp.XX, YY]`, `[p.확인 필요]`, and `[확인 필요]` tags exactly as present in PART A.
- Render page tags visibly in HTML, preferably as `<span class="source-page">...</span>`.
- Render uncertainty tags with a visible uncertain style.
- Do not fabricate, delete, renumber, or relocate source page tags.
- Do not apply source-page detection inside code blocks or inside raw `FIGURE_*` marker blocks.
- Source page tags must remain visible in print mode.

### B4. HTML Compiler Requirements

#### Core rendering rule

Render content; do not alter it. Produce a single self-contained HTML file with custom CSS and JS inline. External runtime dependencies are allowed only for MathJax CDN, Mermaid CDN, and permitted CDN libraries for code highlighting.

#### Marker-to-component mapping

| Marker / Pattern | HTML component | Mandatory rendering note |
|---|---|---|
| `<!-- MASTER LENS -->` | Callout box | border-left gold; lightly tinted background |
| `<!-- ANNOTATION -->` | Inline abbr/tooltip or small italic annotation | preserve in text flow |
| `<!-- ANCHOR -->` | Bridge sentence | italic muted bridge style |
| `<!-- TRENCH -->` | Practical tip box | rose left border / practical warning |
| `<!-- CONFUSION -->` | Comparison component | side-by-side or table/card with amber styling |
| `<!-- SELF-TEST -->` | Click-to-reveal accordion | answer hidden by default |
| `<!-- RECAP -->` | Section summary box | blue left border |
| `[p.XX]`, `[pp.XX–YY]`, `[pp.XX, YY]` | Source page tag span | visible inline and in print |
| `[p.확인 필요]` / `[확인 필요]` | Uncertainty highlight | retain visibly; do not resolve unless verified |
| `<!-- FIGURE_POINTER -->` | Textbook reference callout | text-only; no image embedding |
| `<!-- FIGURE_SCHEMATIC -->` | Inline schematic figure | render from brief using distinct Mermaid/SVG/CSS, not textbook reproduction |
| `<!-- FIGURE_IMAGE_SLOT -->` | Image/placeholder figure | not used in this session because image rights are None |


#### Math, code, interaction, and layout

- MathJax: support inline `\(...\)` and display `\[...\]`, plus existing `$$...$$` blocks if present.
- Code: render `<pre><code>` with copy button; preserve code verbatim.
- Navigation: sticky left sidebar table of contents on desktop; collapsed/single-column behavior on mobile.
- Accordion: Self-Test answers must be hidden by default and revealed only on user click.
- Checklist state: if implemented, persist using `sessionStorage` only.
- Controls: include print/PDF button using `window.print()`.
- Responsive: ≤768px single-column; ≥1024px readable two-column or sidebar layout.
- Dark/light: support `prefers-color-scheme`.
- Print: remove unnecessary backgrounds, hide navigation, optimize page breaks, and keep source-page tags visible.

#### Navigation anchor integrity rules

- Use `<a href="#...">` links only in the sidebar.
- Every sidebar target must have a matching body `id`.
- Every major section heading (§1, §2, §5, §7, §8) must receive a stable id.
- Every §2 concept card should receive a stable id when possible.
- `href` values and body ids must match exactly.
- Do not create duplicate ids.
- Enable `html { scroll-behavior: smooth; }`.
- Before finalizing HTML, count sidebar hrefs, confirm each id exists exactly once, and fix all mismatches before output.

#### Figure rendering self-check

- Every `FIGURE_POINTER` becomes a text-only pointer callout with source, why it matters, when to look, and learner instruction.
- Every `FIGURE_SCHEMATIC` becomes a `<figure>` with caption and alt text.
- Do not reproduce the textbook figure’s exact layout, color palette, or label placement.
- For Mermaid blocks, use valid directives and safe node IDs only; if the diagram cannot satisfy Mermaid syntax rules, use inline SVG or CSS cards instead.
- Do not emit a Mermaid block likely to fail rendering.

#### Prohibited in Phase 5

- Modifying PART A text, equations, or source page tags.
- Rendering markers as plain text.
- Showing Self-Test answers without interaction.
- Embedding textbook images or exact figure reproductions.
- Adding external local CSS/JS/font/image files not supplied by the user.
- Using `<iframe>` or `<embed>`.
- Creating sidebar links whose targets do not exist or duplicate ids.

### B5. Audit Guardrails

Do not restore the following rejected or unsupported material:

- Deficiency Letter, Major Deficiency, 6-month review extension, NDA Module 5, specific FDA/EMA reviewer quotes, or FDA Guidance claims as if textbook-derived.
- Unsupported cost, market-value, business-delay, or USD claims.
- Unsupported broad claim that “80% of modeling failures” come from these tool misuses.
- Modern implementation details as source facts: NONMEM, CWRES, NPDE, Pirana/xpose, SCM, ΔOFV thresholds, Bayesian TDM, Fisher information matrix, D-optimal/ED-optimal, PFIM, PopED, Sobol, mrgsolve. These may appear only as clearly labeled `[교과서 외 구현 번역]` or `[교과서 외 해석]` if already in PART A.
- Hard cutoffs such as `CV% > 50%` or `|r| > 0.95` as PDF-defined rejection thresholds.
- Incorrect continuous Ch.5 source range `p.399–414`; use the verified split range `p.399–405 / p.412–414` and retain missing pp.406–411.
- Any correction that treats Eq.4:22 or Eq.4:53 as a Draft-vs-PDF mismatch rather than a source-form/source-internal note.
- Unapproved code blocks, unapproved figure embedding, or unapproved figure generation.

### B6. Crucible Guardrails

- Crucible v1 is not a raw prose source at Phase 5.
- Preserve only insights already present in PART A or explicitly inserted as labeled Mastery Augmentation.
- Do not convert `[CRUCIBLE_DERIVED]` or `[EXPERT_INFERENCE]` notes into textbook-derived claims.
- Do not introduce omitted or rejected Crucible expansions such as VPC/PPC/NPDE expansion, additional cards, or new external optimal-design frameworks.

### B7. Deprecated and Forbidden Restorations

- Step 1 Draft v0 is deprecated.
- Do not restore rejected overclaims, unsupported numerical values, unsupported regulatory claims, source-unsupported examples, unapproved code, or unapproved figures.
- Do not use Step 1 Draft v0 as learner-body source except through a future Micro-Patch Gate.
- Do not broaden the source range beyond the uploaded PDF pages.

### B8. PATCH MODE Splice Verification Table

| Marker # | Anchor text | Anchor found? | Match count | Inserted? | Final location (§ + card) |
| --- | --- | --- | --- | --- | --- |
| 1 | **§1 Recap**: 이 세션의 목적은 모델링 결과를 “좋아 보인다”가 아니라 “조건을 만족하므로 비교·해석 가능하다”로 바꾸는 것이다. 즉, 판단의 언어를 … | YES | 1 | YES | §1 → before §2 |
| 2 | **MUST 1 Recap**: 초기값은 계산 전의 사전 판단이다. Graph → slope/intercept/plateau → initial estimates … | YES | 1 | YES | §2 MUST 1 — Initial Estimate Acquisition |
| 3 | **MUST 2 Recap**: GOF는 “curve가 지나가는가”가 아니라 “residual이 무작위인가”다. Residual pattern이 있으면 model… | YES | 1 | YES | §2 MUST 2 — Residual-Based Diagnostics |
| 4 | **MUST 3 Recap**: F-test는 nested + equal weighting일 때만 쓴다. AIC/SC는 nested를 요구하지 않지만 equal … | YES | 1 | YES | §2 MUST 3 — F-Test Validity Conditions |
| 5 | **MUST 4 Recap**: Fit이 좋아 보여도 parameter가 식별되지 않을 수 있다. Precision은 모델이 아니라 설계가 만든다. | YES | 1 | YES | §2 MUST 4 — Parameter Precision & Correlation |
| 6 | **MUST 5 Recap**: 최적 샘플링은 촘촘히 많이 찍는 것이 아니라, 각 parameter가 가장 크게 보이는 곳을 의도적으로 찍는 것이다. | YES | 1 | YES | §2 MUST 5 — Partial-Derivative Optimal Sampling |
| 7 | **MUST 6 Recap**: Partial derivative가 “어디서 정보가 생기는가”를 말한다면, sensitivity analysis는 “정보가 부족하… | YES | 1 | YES | §2 MUST 6 — Sensitivity Analysis |

### B9. Zero-Omission Coverage Matrix

| Domain | Required item | Evidence in PART A | Status | Action |
| --- | --- | --- | --- | --- |
| C1 Scope Lock concepts | Initial estimates, GOF/residuals, F-test/AIC/SC, precision/correlation, derivative sampling, sensitivity/toxicokinetic design | §1 roadmap; §2 MUST 1–6; §5 confusion pairs; §8 dependency chain | PRESENT | No action |
| C1 Scope page boundaries | p.352–364 / p.368–392 / p.399–405 / p.412–414; pp.365–367 and pp.406–411 not uploaded | PART A metadata and §1 선행 지식 note | PRESENT | No action |
| C2 Required data anchors | 10 mg IV bolus; K, half-life, AUC, Cl, V; bi-exponential A/B/alpha/beta; warfarin PCA; Table 4.3; repeated-dose anxiolytic; Table 4.4; LOF F-test; Table 4.8; derivative design; toxicokinetic Fig.5.20 | MUST 1 B-1–B-7; MUST 2 C; MUST 3 B/D; MUST 5 A–C; MUST 6 D | PRESENT | No action |
| C3 Audit MUST_FIX | Unsupported regulatory/financial/tool claims removed or labeled; page range corrected; weighting sign convention controlled | §1 후행 지식; MUST 2 B; MUST 3 E; PART B audit guardrails | PRESENT | No action |
| C3 Audit SHOULD_FIX | Eq.4:23–4:33/Table 4.3 restored; Fig.4.19 restored; regression objective/endless journey restored; hard thresholds removed | MUST 1 B-3/B-5/D; MUST 4 A/E | PRESENT | No action |
| C4 Audit T5 coverage | Dynamic non-steady-state, pure error/LOF, accuracy vs precision, WRSS vs −2LL, GOF checklist, toxicokinetic design | MUST 1, MUST 2, MUST 3, MUST 4, MUST 6, §8 D | PRESENT | No action |
| C5 Figure coverage KEEP | Approved Figure #1–#7 markers | PART A contains seven spliced markers after the approved recap anchors | PRESENT | No action |
| C5 Figure rejections | Dynamic non-steady-state pointer, Outlier A/B pointer, Table 4.9 pointer not restored | PART B figure inventory lists rejected items as non-renderable | PRESENT | No action |
| C6 Page tag integrity | Existing page tags preserved; no new tags created by augmentations | PART A body preserves [p.xx]/[pp.xx–yy]; augmentations have no page tags | PRESENT | No action |
| C7 Crucible Grade A preservation | Nested geometry, r misuse, derivative/information link, ridge geometry, residual pattern as time-scale exposure | MUST 2–5 canonical text and Mastery Notes #3–#6 | PRESENT_COMPRESSED | No action |
| C8 Deprecated Draft regression | No unsupported Deficiency Letter, review extension, USD, ΔOFV threshold, or unapproved software workflow restored as textbook content | PART A + PART B guardrails | PRESENT | No action |
| C9 Canonical body integrity | Content Lock v2 §1–§8 preserved; only approved 4C markers and labeled mastery notes inserted | Splice verification table; Mastery Augmentation Log | PRESENT | No action |

### B10. Micro-Patch Log

No micro-patches needed. PART A equals spliced learner-facing Content Lock v2 §1–§8 except approved Figure 4C markers and the bounded Mastery Augmentation Layer.

### B11. Mastery Augmentation Log

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | §1 after Figure #1 | W / workflow consequence | YES | CRUCIBLE_DERIVED | Frames the six cards as a closed modeling loop rather than isolated techniques. | Low |
| 2 | MUST 1 after Figure #2 | F / failure mode | YES | TEXTBOOK_DERIVED | Reinforces bad initial estimates entering the wrong objective-function basin. | Low |
| 3 | MUST 2 after Figure #3 | M / macro insight | YES | CRUCIBLE_DERIVED | Links residual time pattern to missing time scale and prevents treatment swapping. | Low |
| 4 | MUST 3 after Figure #4 | J / judgment lens | YES | CRUCIBLE_DERIVED | Explains nestedness as same-comparison-coordinate condition. | Low |
| 5 | MUST 4 after Figure #5 | M / macro insight | YES | CRUCIBLE_DERIVED | Turns parameter correlation into ridge-minimum geometry. | Low |
| 6 | MUST 5 after Figure #6 | W / workflow consequence | YES | CRUCIBLE_DERIVED | Connects derivative peaks to visible parameter regions while preserving boundary conditions. | Low |
| 7 | MUST 6 after Figure #7 | F / failure mode | YES | TEXTBOOK_DERIVED | Highlights toxicokinetic masking without adding new values or examples. | Low |

#### Rejected or Deferred Augmentation Candidates

| Rejected candidate | Reason for rejection |
| --- | --- |
| Additional r/dynamic-range note in §5 | Rejected because canonical body already contains the same bounded interpretation. |
| Outlier A/B new figure or expanded leverage diagnostics | Rejected because Phase 4C rejected the figure and extra statistics would expand beyond the locked body. |
| External NONMEM/ΔOFV/PFIM/PopED implementation details | Rejected because Audit explicitly limits modern tools to labeled implementation translation and forbids unsupported thresholds. |


# 15_Content Lock v2.1 — Figure Marker Insertion Patch

**Output mode: PATCH MODE**

**Mode decision rationale**: Content Lock v2 is long, and re-emitting the full body would create avoidable text drift. This file therefore provides only the Phase 4C figure strategy, figure briefs, and insertion map. The unchanged Content Lock v2 body should be spliced with the marker blocks below during Phase 5.

**Image rights check**: Scope Lock declares `Image rights: None`; therefore no Mode I image insert is used. Textbook figures are referenced only by POINTER markers, and schematic items are specified as Phase 5 redraw/new-schematic briefs without code.

---

## (A) Reading-order Figure Plan — PRIMARY VIEW

| # | Reading order | Location (§ + concept card) | Mode | Source figure/table | Trigger | Why text alone is insufficient | Expected learning gain | Decision |
|---:|---|---|---|---|---|---|---|---|
| 1 | §1 | Session Header & Roadmap | P | Fig.4.16, p.352 | G3, G5 | The text says the workflow is cyclic, but learners may still read the chapter as a linear list of topics. | The learner sees that initial estimates, fitting, output analysis, and next design are one closed modeling loop. | KEEP |
| 2 | §2 | MUST 1 — Initial Estimate Acquisition | R | Fig.4.18, p.355 | G1, G5 | Curve stripping is fundamentally spatial: terminal slope, back-extrapolation, residual line, and initial slope must be visually separated. | The learner understands why terminal phase is read first and why alpha/beta separation is required. | KEEP |
| 3 | §2 | MUST 2 — Residual-Based Diagnostics | N | Concept synthesis from Fig.4.43, Fig.4.45, Fig.4.50 [pp.372–376] | G2, G4, G5 | The text lists banana, fan, run, and residual patterns, but learners can still map the wrong pattern to the wrong fix. | The learner links residual shape → likely failure mode → next modeling action. | KEEP |
| 4 | §2 | MUST 3 — F-Test Validity Conditions | P | Table 4.8, p.389 | G2, G5 | The nested/equal-weighting rule is easy to memorize but hard to police in real model comparisons. | The learner sees the canonical double violation: non-nested structure plus different weighting. | KEEP |
| 5 | §2 | MUST 4 — Parameter Precision & Correlation | P | Fig.4.53, p.382; Fig.4.55–4.57, pp.383–385 | G1, G2, G5 | r misuse and parameter-correlation geometry are both visual failures: the learner must see the misleading high r and the ridge/ellipse trade-off. | The learner separates “high apparent fit” from “valid parameter identifiability.” | KEEP |
| 6 | §2 | MUST 5 — Partial-Derivative Optimal Sampling | P | Fig.5.4–5.6, pp.400–402; Fig.5.8, p.403 | G1, G5 | The core concept is not the derivative formula but where each derivative peaks in time or concentration space. | The learner sees sampling as information placement rather than dense sampling. | KEEP |
| 7 | §2 | MUST 6 — Sensitivity Analysis | P | Fig.5.10, p.405; Fig.5.20, p.414 | G1, G2, G5 | Sensitivity and toxicokinetic masking both depend on how perturbations alter full profiles, which prose compresses too aggressively. | The learner sees how parameter uncertainty changes predictions and how capacity/induction can mask exposure interpretation. | KEEP |
| 8 | §2 | MUST 1 — Dynamic non-steady-state worked example | P | Fig.4.21, p.357; Table 4.3, p.360 | G1, G5 | The worked example is useful, but the current card already preserves the numerical logic and model-choice anchor. | Would strengthen the example but would not change the learner’s structural map enough to justify another pointer slot. | REJECT — budget; lower ROI than Fig.4.18 |
| 9 | §5 | 혼동쌍 #4 — Outlier A vs Outlier B | P | Fig.4.59, p.390 | G2, G5 | The outlier distinction is visual, but the v2 confusion table already states vertical deviation vs time-axis leverage clearly. | Optional reinforcement only. | REJECT — budget; lower ROI than r/correlation and derivative figures |
| 10 | §8 | Meta-Frame & Big Picture | P | Table 4.9, p.391 | G3, G5 | The checklist is important, but it is already reproduced as a locked interpretation table in §8. | Redundant with existing table. | REJECT — redundant |

---

## (B) Type-sorted Summary — AUXILIARY VIEW

**Pointers (P): #1, #4, #5, #6, #7 → 5 / max 5**

- #1 Fig.4.16 — modeling carousel spine.
- #4 Table 4.8 — F-test/AIC invalid-comparison boundary.
- #5 Fig.4.53 + Fig.4.55–4.57 — r misuse and parameter-correlation geometry.
- #6 Fig.5.4–5.6 + Fig.5.8 — derivative-based sampling regions.
- #7 Fig.5.10 + Fig.5.20 — sensitivity and toxicokinetic masking.

**Schematics (R/N): #2, #3 → 2 / max 2**

- #2 R — bi-exponential curve stripping schematic.
- #3 N — residual-pattern diagnostic triage map.

**Images (I): none → 0**

- No image slots because `Image rights: None`.

---

## Figure Briefs — KEEP Items Only

### Figure #1 — POINTER

- **Source**: Gabrielsson & Weiner 5e, p.352, Fig.4.16, “From tentative model to plot of data.”
- **Why this figure matters**: This figure is the source’s organizing spine for the session. It shows that EDA and initial estimates do not end the process; they feed fitting, output analysis, and the next experiment.
- **When to look**: After reading §1 Recap, before entering MUST cards.
- **Learner instruction**: Trace the arrow from Explore data to Fit model(s) to Analyze output, then back to Design. Read every MUST card as one part of this loop, not as an isolated technique.

### Figure #2 — REDRAW

- **Title**: Bi-exponential curve stripping: terminal-first logic
- **Visual objective**: In 5 seconds, the learner should see that terminal slope is isolated first, then subtracted to reveal the initial slope.
- **Core message**: Curve stripping works only when the fast and slow time scales are visually separable.
- **Elements to include**:
  - Semi-log concentration–time axes.
  - Observed bi-exponential curve as a smooth generic trajectory.
  - Terminal line labeled “read B and beta first.”
  - Back-extrapolated terminal line.
  - Residual initial line labeled “subtract terminal component → read A and alpha.”
  - Warning label: “unstable if alpha ≈ beta.”
- **Elements to exclude**:
  - Exact textbook visual style.
  - Dense tick marks or exact point replication.
  - Additional PK equations already present in the text.
- **Suggested rendering**: SVG.
- **Caption**: A simplified redraw of the curve-stripping logic: terminal-phase information is extracted first, then removed to expose the initial phase.
- **Alt text**: Semi-log concentration–time schematic showing a total bi-exponential curve, a terminal back-extrapolated line, and a residual initial line.
- **Source relation**: Redrawn from textbook concept, not an exact reproduction.

### Figure #3 — NEW SCHEMATIC

- **Title**: Residual pattern triage: shape → likely failure → next action
- **Visual objective**: In 5 seconds, the learner should map each residual pattern to the correct diagnostic branch.
- **Core message**: Residual shape determines whether the next action should target structure, weighting, or data/design.
- **Elements to include**:
  - Four pattern boxes: random scatter, systematic run/banana, fan shape, isolated leverage point.
  - Diagnostic labels: acceptable randomness, structural time-scale error, variance/weighting error, outlier/leverage concern.
  - Action arrows: keep/check precision, revise structural model, revise error/weighting model, inspect source data and leverage.
  - A small “do not swap treatments” warning: fan ≠ compartment problem; banana ≠ weighting-only problem.
- **Elements to exclude**:
  - Exact textbook residual plots.
  - Numerical thresholds.
  - Software-specific diagnostics not in Content Lock v2.
- **Suggested rendering**: Mermaid flowchart or CSS comparison card.
- **Caption**: A diagnostic triage map linking residual shape to the most plausible modeling failure and next action.
- **Alt text**: Flowchart connecting residual scatter, banana runs, fan-shaped spread, and leverage points to different modeling responses.
- **Source relation**: Newly designed synthesis from textbook residual-pattern concepts.

### Figure #4 — POINTER

- **Source**: Gabrielsson & Weiner 5e, p.389, Table 4.8, Michaelis–Menten weighted fit vs first-order unweighted fit comparison.
- **Why this figure matters**: Table 4.8 is the compact source example showing why F-test and AIC can both become invalid when model structure and weighting differ. It operationalizes the Apex rule.
- **When to look**: After reading MUST 3 Recap.
- **Learner instruction**: Identify the two violations separately: non-nested model structure and different weighting. Do not collapse them into a vague statement that “models are different.”

### Figure #5 — POINTER

- **Source**: Gabrielsson & Weiner 5e, p.382, Fig.4.53; pp.383–385, Fig.4.55–4.57.
- **Why this figure matters**: Fig.4.53 demonstrates that a higher r can still hide systematic terminal bias. Fig.4.55–4.57 then show that even a plausible fit can have poorly identified correlated parameters.
- **When to look**: After reading MUST 4 Recap, before §5 confusion pairs.
- **Learner instruction**: First compare r=0.96 versus r=0.94 and ask which fit is structurally better. Then inspect the confidence ellipses/design comparison and ask whether the parameter pair is truly identifiable.

### Figure #6 — POINTER

- **Source**: Gabrielsson & Weiner 5e, pp.400–402, Fig.5.4–5.6; p.403, Fig.5.8.
- **Why this figure matters**: These figures are the core visual evidence that derivative peaks define informative sampling regions. Without the plots, the rule “sample where sensitivity is high” remains too abstract.
- **When to look**: After reading MUST 5 Recap.
- **Learner instruction**: For each derivative curve, point to the time or concentration region where the curve is largest in magnitude. Translate that region into a sampling design point.

### Figure #7 — POINTER

- **Source**: Gabrielsson & Weiner 5e, p.405, Fig.5.10; p.414, Fig.5.20.
- **Why this figure matters**: Fig.5.10 shows how parameter perturbations alter response-time profiles. Fig.5.20 shows the toxicokinetic trap where capacity-dependent and time-dependent processes can mask each other in exposure interpretation.
- **When to look**: After reading MUST 6 Recap, before moving to §5 confusion pairs.
- **Learner instruction**: In Fig.5.10, identify which profile region moves when each parameter is perturbed. In Fig.5.20, focus on why similar-looking exposure summaries can hide two simultaneous kinetic processes.

---

## Insertion Map (PATCH MODE)

| # | Reading order | Anchor copied verbatim from Content Lock v2 | Insert position | Marker block |
|---:|---|---|---|---|
| 1 | §1 → before §2 | `**§1 Recap**: 이 세션의 목적은 모델링 결과를 “좋아 보인다”가 아니라 “조건을 만족하므로 비교·해석 가능하다”로 바꾸는 것이다. 즉, 판단의 언어를 인상에서 조건으로 옮기는 것이다.` | after this anchor card | See Marker Block #1 below |
| 2 | §2 MUST 1 | `**MUST 1 Recap**: 초기값은 계산 전의 사전 판단이다. Graph → slope/intercept/plateau → initial estimates → regression이라는 순서를 바꾸면 알고리즘이 모델러의 눈을 대신할 수 없다.` | after this anchor card | See Marker Block #2 below |
| 3 | §2 MUST 2 | `**MUST 2 Recap**: GOF는 “curve가 지나가는가”가 아니라 “residual이 무작위인가”다. Residual pattern이 있으면 model, weighting, sampling design 중 하나가 정보를 잘못 처리하고 있다.` | after this anchor card | See Marker Block #3 below |
| 4 | §2 MUST 3 | `**MUST 3 Recap**: F-test는 nested + equal weighting일 때만 쓴다. AIC/SC는 nested를 요구하지 않지만 equal weighting을 요구하며, 어느 경우든 residual과 biology를 대체하지 못한다.` | after this anchor card | See Marker Block #4 below |
| 5 | §2 MUST 4 | `**MUST 4 Recap**: Fit이 좋아 보여도 parameter가 식별되지 않을 수 있다. Precision은 모델이 아니라 설계가 만든다.` | after this anchor card | See Marker Block #5 below |
| 6 | §2 MUST 5 | `**MUST 5 Recap**: 최적 샘플링은 촘촘히 많이 찍는 것이 아니라, 각 parameter가 가장 크게 보이는 곳을 의도적으로 찍는 것이다.` | after this anchor card | See Marker Block #6 below |
| 7 | §2 MUST 6 | `**MUST 6 Recap**: Partial derivative가 “어디서 정보가 생기는가”를 말한다면, sensitivity analysis는 “정보가 부족하면 결론이 어디서 무너지는가”를 말한다.` | after this anchor card | See Marker Block #7 below |

---

## Marker Blocks — Full Text for Splicing

### Marker Block #1

```text
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.352, Fig.4.16, “From tentative model to plot of data.”
Why this matters: This figure is the source’s organizing spine for the session. It shows that EDA and initial estimates feed fitting, output analysis, and the next experiment rather than ending the process.
When to look: after reading §1 Recap, before entering MUST cards.
Learner instruction: Trace the arrow from Explore data to Fit model(s) to Analyze output, then back to Design. Read every MUST card as one part of this loop, not as an isolated technique.
<!-- /FIGURE_POINTER -->
```

### Marker Block #2

```text
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
```

### Marker Block #3

```text
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
```

### Marker Block #4

```text
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.389, Table 4.8, Michaelis–Menten weighted fit vs first-order unweighted fit comparison.
Why this matters: Table 4.8 is the compact source example showing why F-test and AIC can both become invalid when model structure and weighting differ. It operationalizes the Apex rule.
When to look: after reading MUST 3 Recap.
Learner instruction: Identify the two violations separately: non-nested model structure and different weighting. Do not collapse them into a vague statement that “models are different.”
<!-- /FIGURE_POINTER -->
```

### Marker Block #5

```text
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.382, Fig.4.53; pp.383–385, Fig.4.55–4.57.
Why this matters: Fig.4.53 demonstrates that a higher r can still hide systematic terminal bias. Fig.4.55–4.57 then show that even a plausible fit can have poorly identified correlated parameters.
When to look: after reading MUST 4 Recap, before §5 confusion pairs.
Learner instruction: First compare r=0.96 versus r=0.94 and ask which fit is structurally better. Then inspect the confidence ellipses/design comparison and ask whether the parameter pair is truly identifiable.
<!-- /FIGURE_POINTER -->
```

### Marker Block #6

```text
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, pp.400–402, Fig.5.4–5.6; p.403, Fig.5.8.
Why this matters: These figures are the core visual evidence that derivative peaks define informative sampling regions. Without the plots, the rule “sample where sensitivity is high” remains too abstract.
When to look: after reading MUST 5 Recap.
Learner instruction: For each derivative curve, point to the time or concentration region where the curve is largest in magnitude. Translate that region into a sampling design point.
<!-- /FIGURE_POINTER -->
```

### Marker Block #7

```text
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.405, Fig.5.10; p.414, Fig.5.20.
Why this matters: Fig.5.10 shows how parameter perturbations alter response-time profiles. Fig.5.20 shows the toxicokinetic trap where capacity-dependent and time-dependent processes can mask each other in exposure interpretation.
When to look: after reading MUST 6 Recap, before moving to §5 confusion pairs.
Learner instruction: In Fig.5.10, identify which profile region moves when each parameter is perturbed. In Fig.5.20, focus on why similar-looking exposure summaries can hide two simultaneous kinetic processes.
<!-- /FIGURE_POINTER -->
```

---

## Phase 5 Splicing Note

Use the exact anchors above against the unchanged `15_Content Lock v2.md`. Insert each marker block on its own lines immediately after the matched anchor card. Do not alter any existing body text, source page tags, equations, annotations, or card order.

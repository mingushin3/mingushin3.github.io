# 05_Content Lock v2.1 — Figure Marker Patch
## 2구획 모델 — 이중지수 분해 / α·β 재파라미터화 / V₁·Vss·Vβ 체계

> **Output mode:** PATCH MODE  
> **Reason:** Content Lock v2 is long, and Phase 4C must avoid body-text drift. This file therefore provides the Strategy Table, Figure Briefs, and Insertion Map only. The unchanged `05_Content Lock v2.md` body should be patched using the marker blocks below.  
> **Image rights:** None. No textbook image is embedded. Allowed modes are POINTER and schematic REDRAW/NEW only.  
> **Phase boundary:** This file decides figures and marker placement only. It does not generate Mermaid, SVG, HTML, or final image code.

---

## A. Reading-order Figure Plan

| # | Reading order | Location (§ + concept card) | Mode | Source figure/table | Trigger | Why text alone is insufficient | Expected learning gain | Decision |
|---:|---|---|---|---|---|---|---|---|
| 1 | §2 → M1 | Card M1 — 이중지수 방정식과 잔차법 | P | G&W p.60, Fig.2.43 | G5, G1, G2 | 잔차법은 slope/intercept, terminal back-extrapolation, residual subtraction이 동시에 보이는 절차다. 텍스트와 식만으로는 “꼬리를 빼서 머리를 얻는다”는 curve-stripping 동작이 한 번에 보이지 않는다. | $A,\alpha,B,\beta$를 네 기호가 아니라 semilog curve geometry로 읽게 한다. | KEEP |
| 2 | §2 → M2 | Card M2 — Macro ↔ Micro ↔ Physiological 좌표계 | P | G&W p.65, Fig.2.46 | G5, G2 | “plasma data alone으로 elimination site를 식별할 수 없다”는 문장은 추상적이다. 세 mammillary variants를 나란히 보면 같은 biexponential curve가 서로 다른 구조 가정과 양립할 수 있음을 즉시 이해한다. | central elimination only가 데이터로 증명된 것이 아니라 working assumption임을 각인한다. | KEEP |
| 3 | §2 → M3 | Card M3 — V₁ / Vss / Vβ | P | R&T p.628, Fig.19-9 | G5, G2 | $V_1$, $V_{ss}$, $V_\beta$의 정의표는 정적이다. Fig.19-9는 elimination이 있을 때 effective volume이 시간에 따라 어떻게 달라지는지 보여주므로, “어느 volume?” 질문을 시각적으로 고정한다. | $V_\beta$를 “진짜 body volume”으로 오독하는 오류를 줄인다. | KEEP |
| 4 | §2 → M3 | Card M3 — Clinical use rule | R | R&T p.639, Fig.19-16 concept | G5, G2, G4 | 다회투여 interval 안에서 언제 $V_{ss}$ 또는 $V_\beta$가 amount estimate에 쓸 수 있는지는 문장으로 읽으면 조건문이 겹친다. 사용 가능/불가 조건을 별도 gate로 분리해야 한다. | loading/amount 해석에서 $V_{ss}$, $V_\beta$, neither를 상황별로 구분하게 한다. | KEEP |
| 5 | §2 → M4 | Card M4 — 재파라미터화 5종 + condition number | R | G&W p.516, Table 8.1 | G5, G2, G4 | Table 8.1의 숫자는 핵심이지만, 숫자표만으로는 “WRSS가 낮은 모델”과 “condition number가 낮은 모델”이 다를 수 있다는 축 분리가 즉시 보이지 않는다. | Takada vs ODE model의 대비를 통해 model fit axis와 estimation geometry axis를 분리한다. | KEEP |
| 6 | §2 → M5 | Card M5 — Nicardipine plateau trap | P | R&T p.631, Fig.19-10 | G5, G2 | terminal half-life가 길어도 plasma plateau는 빠르게 접근할 수 있다는 점은 식과 수치만으로는 직관화가 어렵다. curve를 보아야 “12 hr terminal t½”와 “1 hr 50% Css”가 동시에 참일 수 있음을 받아들인다. | terminal half-life 하나로 loading dose를 판단하는 오류를 줄인다. | KEEP |
| 7 | §2 → M5 | Card M5 — Gentamicin plasma/tissue accumulation | P | R&T p.636, Fig.19-14 | G5, G2 | terminal term accumulation과 plasma peak/trough fluctuation은 서로 다른 현상이다. 텍스트만으로는 slowly equilibrating tissue accumulation과 therapeutic plasma behavior를 분리하기 어렵다. | terminal half-life trap을 aminoglycoside multiple-dosing 맥락에서 구조적으로 이해한다. | KEEP |

---

## B. Type-sorted Summary

- **Pointers (P):** #1, #2, #3, #6, #7 → **5 / 5** under A-Critical budget.
- **Schematics (R/N combined):** #4, #5 → **2 / 2** under A-Critical budget.
- **Images (I):** none → image rights are None; textbook figures must not be embedded.

### Rejected or deferred candidates

| Candidate | Decision | Reason |
|---|---|---|
| G&W Fig.2.39, Fig.2.41, Fig.2.42 | REJECT | Useful orientation, but lower ROI than the retained residual-method and non-identifiability figures. |
| G&W Fig.2.44 / Fig.2.48 / Table 2.6 | REJECT by budget | M2 formulas and parameter-set table are already explicit in v2. Fig.2.46 prevents the larger learner failure: assuming elimination site is identified from plasma alone. |
| G&W Table 2.4 / Fig.2.45 | REJECT by budget | Fractional-area teaching is retained textually in M1/M5 and visually reinforced by R&T Fig.19-10 and Fig.19-14. |
| G&W Fig.8.1 | REJECT by budget | PK8 model-family context is captured more efficiently by a redrawn Table 8.1 comparison schematic. |
| R&T Fig.19-1 / Fig.19-2 / Fig.19-3 / Table 19-1 / Fig.19-4 | REJECT by budget | Essential but redundant with retained G&W Fig.2.43, Fig.2.46, and R&T Fig.19-9 for the specific v2 learning path. |
| R&T Fig.19-11 / Fig.19-12 | REJECT by budget | Plateau and tissue-accumulation logic is covered by Fig.19-10 and Fig.19-14 with higher clinical payoff. |
| R&T Fig.19-13 / Fig.19-15 / Fig.19-17 / Fig.19-18 | DEFER | Useful dosing/renal boundary contexts, but not necessary for the 10-minute handout core. |
| R&T Fig.19-19–19-32 and Tables 19-2–19-5 | REJECT | Redistribution/PD/worked examples are outside the current Content Lock scope. |

---

## C. Figure Briefs for Phase 5

### Figure #1 — POINTER

- **Source:** Gabrielsson & Weiner 5e, p.60, Fig.2.43, semi-logarithmic plot of bi-exponential decay after IV bolus.
- **Why this figure matters:** This is the central visual for residual method. It shows that the observed curve is the sum of two extrapolated phase lines rather than one terminal line.
- **When to look:** After reading the M1 formal definition and before reading the residual-method procedure.
- **Learner instruction:** Inspect the terminal line first, then visually subtract it from the early observations. Confirm where $A$, $B$, $-\alpha$, and $-\beta$ appear on the semilog plot.

### Figure #2 — POINTER

- **Source:** Gabrielsson & Weiner 5e, p.65, Fig.2.46, three two-compartment models that fit the same biexponential plasma profile.
- **Why this figure matters:** It prevents the false inference that a biexponential plasma curve identifies the elimination site. The figure makes structural non-identifiability visible.
- **When to look:** After reading M2 “비식별성의 핵심”.
- **Learner instruction:** Compare the three structures and ask what is identical across them: the plasma curve. Then identify what plasma data alone cannot tell you: where elimination truly occurs.

### Figure #3 — POINTER

- **Source:** Rowland & Tozer 5e, p.628, Fig.19-9, distribution-volume terms and the effect of elimination on $V$ and $V_{ss}$.
- **Why this figure matters:** This is the best source visual for why $V_1$, $V_{ss}$, and $V_\beta$ are not interchangeable. It turns the volume table into a time-dependent interpretation problem.
- **When to look:** After reading the M3 volume table and before reading the Aspirin/Gentamicin anchors.
- **Learner instruction:** Track how apparent volume changes as distribution and elimination proceed. Then map each part of the curve back to $V_1$, $V_{ss}$, or $V_\beta$.

### Figure #4 — REDRAW

- **Title:** When can $V_{ss}$ or $V_\beta$ estimate amount during multiple dosing?
- **Visual objective:** In 5 seconds, the learner should see three regimes: $V_{ss}$ usable, $V_\beta$ approximately usable, and neither volume safely usable.
- **Core message:** Volume terms are not universal calculators; their use depends on dosing interval, fluctuation, and distribution equilibrium.
- **Elements to include:**
  - One horizontal dosing-interval timeline.
  - Zone 1: true or near steady state with small fluctuation → “$V_{ss}$ useful for amount estimate”.
  - Zone 2: late interval after distribution equilibrium → “$V_\beta$ may approximate amount”.
  - Zone 3: distribution disequilibrium throughout interval → “neither simple volume term”.
  - A warning label: “gentamicin-like case: terminal term ≠ plasma fluctuation”.
  - Cross-reference labels: M3 Clinical use rule / M5 Multiple dosing volume rule.
- **Elements to exclude:**
  - Exact reproduction of R&T Fig.19-16.
  - Dense equations beyond $V_{ss}$ and $V_\beta$ labels.
  - More than three regime categories.
- **Suggested rendering:** inline SVG.
- **Caption:** $V_{ss}$ and $V_\beta$ answer different amount-estimation questions during a dosing interval; neither should be used blindly under persistent distribution disequilibrium.
- **Alt text:** A dosing-interval timeline split into regimes where $V_{ss}$, $V_\beta$, or neither volume term is appropriate for estimating amount in the body.
- **Source relation:** Redrawn from textbook concept (no exact reproduction).

### Figure #5 — REDRAW

- **Title:** PK8 model selection: WRSS axis vs condition-number axis
- **Visual objective:** In 5 seconds, the learner should see that the model with the lowest WRSS is not the model with the lowest condition number.
- **Core message:** Similar fit quality does not imply similar estimation stability.
- **Elements to include:**
  - Five model rows: Bi-exponential, Takada, Colburn, Reparameterized CL, ODE physiological.
  - WRSS mini-bar or badge for each model.
  - Condition-number mini-bar or badge for each model.
  - Highlight Takada: lowest WRSS, high condition number.
  - Highlight ODE physiological: similar WRSS, lowest condition number.
  - One summary callout: “fit axis ≠ estimation geometry axis”.
- **Elements to exclude:**
  - Direct facsimile of Table 8.1 layout.
  - Parameter-estimate details not needed for the comparison.
  - Any threshold not present in the Content Lock text.
- **Suggested rendering:** CSS comparison card.
- **Caption:** PK8 shows that reparameterization can leave fit quality similar while changing condition number by roughly two orders of magnitude.
- **Alt text:** A comparison card showing five parameterizations with separate WRSS and condition-number indicators; Takada has the lowest WRSS but high condition number, whereas the ODE model has the lowest condition number.
- **Source relation:** Redrawn from textbook concept (no exact reproduction).

### Figure #6 — POINTER

- **Source:** Rowland & Tozer 5e, p.631, Fig.19-10, nicardipine approach to plateau despite long terminal half-life.
- **Why this figure matters:** It is the clearest visual for why terminal half-life may not predict early plasma plateau. It directly supports the M5 warning against half-life-only dosing reasoning.
- **When to look:** After reading the M5 plateau equation and Nicardipine anchor.
- **Learner instruction:** Compare the terminal half-life label with the observed approach to 50% Css. Do not infer plateau timing from terminal slope alone until $f_1/f_2$ is checked.

### Figure #7 — POINTER

- **Source:** Rowland & Tozer 5e, p.636, Fig.19-14, gentamicin plasma/tissue multiple-dosing accumulation.
- **Why this figure matters:** This figure separates terminal-term accumulation from therapeutic plasma fluctuation. It is the best visual anchor for the gentamicin half-life trap.
- **When to look:** After reading the M5 Gentamicin anchor and before the §5 terminal/effective half-life confusion pair.
- **Learner instruction:** Follow plasma concentration and slowly equilibrating tissue behavior separately. Identify why a terminal accumulation index can be large without implying the same plasma peak/trough accumulation.

---

## D. Insertion Map (PATCH MODE)

| # | Reading order | Anchor copied from Content Lock v2 | Insert position | Marker block |
|---:|---|---|---|---|
| 1 | §2 → M1 | `### Card M1 — 이중지수 방정식과 잔차법(Method of Residuals)` | after this anchor card; before `### Card M2 — Macro ↔ Micro ↔ Physiological 3중 좌표계 변환` | FIG-05-01 |
| 2 | §2 → M2 | `### Card M2 — Macro ↔ Micro ↔ Physiological 3중 좌표계 변환` | after this anchor card; before `### Card M3 — V₁ / Vss / Vβ 3중 분포용적 체계` | FIG-05-02 |
| 3 | §2 → M3 | `### Card M3 — V₁ / Vss / Vβ 3중 분포용적 체계` | after this anchor card; before `### Card M4 — 재파라미터화 5종과 condition number`; insert before FIG-05-04 | FIG-05-03 |
| 4 | §2 → M3 | `### Card M3 — V₁ / Vss / Vβ 3중 분포용적 체계` | after this anchor card; before `### Card M4 — 재파라미터화 5종과 condition number`; insert after FIG-05-03 | FIG-05-04 |
| 5 | §2 → M4 | `### Card M4 — 재파라미터화 5종과 condition number` | after this anchor card; before `### Card M5 — 분포속도론의 임상 파급과 terminal half-life의 함정` | FIG-05-05 |
| 6 | §2 → M5 | `### Card M5 — 분포속도론의 임상 파급과 terminal half-life의 함정` | after this anchor card; before `## §5 — Confusion Pairs & Critical Blow`; insert before FIG-05-07 | FIG-05-06 |
| 7 | §2 → M5 | `### Card M5 — 분포속도론의 임상 파급과 terminal half-life의 함정` | after this anchor card; before `## §5 — Confusion Pairs & Critical Blow`; insert after FIG-05-06 | FIG-05-07 |

### Marker block FIG-05-01

```text
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.60, Fig.2.43 — Semi-logarithmic plot of bi-exponential decay after IV bolus.
Why this matters: This is the central visual for residual method. It shows that the observed curve is the sum of two extrapolated phase lines rather than one terminal line.
When to look: After reading the M1 formal definition and before reading the residual-method procedure.
Learner instruction: Inspect the terminal line first, then visually subtract it from the early observations. Confirm where A, B, -alpha, and -beta appear on the semilog plot.
<!-- /FIGURE_POINTER -->
```

### Marker block FIG-05-02

```text
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.65, Fig.2.46 — Three two-compartment models that fit the same biexponential plasma profile.
Why this matters: It prevents the false inference that a biexponential plasma curve identifies the elimination site. The figure makes structural non-identifiability visible.
When to look: After reading M2 “비식별성의 핵심”.
Learner instruction: Compare the three structures and ask what is identical across them: the plasma curve. Then identify what plasma data alone cannot tell you: where elimination truly occurs.
<!-- /FIGURE_POINTER -->
```

### Marker block FIG-05-03

```text
<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.628, Fig.19-9 — Distribution-volume terms and the effect of elimination on V and Vss.
Why this matters: This is the best source visual for why V1, Vss, and Vbeta are not interchangeable. It turns the volume table into a time-dependent interpretation problem.
When to look: After reading the M3 volume table and before reading the Aspirin/Gentamicin anchors.
Learner instruction: Track how apparent volume changes as distribution and elimination proceed. Then map each part of the curve back to V1, Vss, or Vbeta.
<!-- /FIGURE_POINTER -->
```

### Marker block FIG-05-04

```text
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
```

### Marker block FIG-05-05

```text
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
```

### Marker block FIG-05-06

```text
<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.631, Fig.19-10 — Nicardipine approach to plateau despite long terminal half-life.
Why this matters: It is the clearest visual for why terminal half-life may not predict early plasma plateau. It directly supports the M5 warning against half-life-only dosing reasoning.
When to look: After reading the M5 plateau equation and Nicardipine anchor.
Learner instruction: Compare the terminal half-life label with the observed approach to 50% Css. Do not infer plateau timing from terminal slope alone until f1/f2 is checked.
<!-- /FIGURE_POINTER -->
```

### Marker block FIG-05-07

```text
<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.636, Fig.19-14 — Gentamicin plasma/tissue multiple-dosing accumulation.
Why this matters: This figure separates terminal-term accumulation from therapeutic plasma fluctuation. It is the best visual anchor for the gentamicin half-life trap.
When to look: After reading the M5 Gentamicin anchor and before the §5 terminal/effective half-life confusion pair.
Learner instruction: Follow plasma concentration and slowly equilibrating tissue behavior separately. Identify why a terminal accumulation index can be large without implying the same plasma peak/trough accumulation.
<!-- /FIGURE_POINTER -->
```

---

## E. Patch application rule

1. Start from the unchanged `05_Content Lock v2.md` file.
2. Apply the seven marker blocks in the reading order above.
3. Place each marker block at the end of the specified card, on its own lines, immediately before the next card or section heading.
4. Do not modify any body text, existing markers, equations, annotations, source page tags, or `[확인 필요]` flags.
5. Do not embed textbook images. Mode P is a source-inspection pointer; Mode R/N is only a Phase 5 rendering brief.

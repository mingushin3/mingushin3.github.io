# 08_Content Lock v2.1 — Figure Marker Patch Plan

**OUTPUT MODE: PATCH MODE**

**Mode rationale:** Content Lock v2 is a long text-final document (>6,000 whitespace tokens). Re-emitting the full body would create unnecessary text-drift risk. This v2.1 deliverable therefore provides only the figure strategy, figure briefs, and exact insertion map for marker splicing.

**Image rights status:** None. Textbook figures must not be reproduced as images. Therefore, no Mode I image insertion is proposed. Textbook visuals are used only as POINTERs; newly needed synthesis visuals are specified as schematic briefs for Phase 5.

---

## 1. Figure Strategy Table — View A: Reading-order Figure Plan

| # | Reading order | Location (§ + concept card) | Mode | Source figure (if any) | Trigger | Why text alone is insufficient | Expected learning gain | Decision |
|---:|---|---|---|---|---|---|---|---|
| 1 | §1 → before §2 | §1.1 지식 그래프 위치 | N | None | G3, G4 | The roadmap has multiple layers: diagnostic entry, mechanistic causes, DDI modifiers, and downstream pharmacometrics uses. Text can list them, but does not force the learner to see the triage sequence. | The learner sees the whole session as one decision path: detect nonlinearity → assign mechanism → translate to modeling/TDM/DDI risk. | **KEEP** |
| 2 | §2 C1 | Nonlinearity diagnostics | P | Gabrielsson & Weiner p.113 Fig.2.85–2.86 | G2, G5 | The diagnostic distinction depends on visual curve patterns: AUC vs Dose, AUC/Dose vs Dose, and superposition failure. A prose description cannot reliably prevent pattern-mapping errors. | The learner learns to classify the direction of AUC/Dose change before naming a mechanism. | **KEEP** |
| 3 | §2 C1/C2 boundary | Linear vs nonlinear superposition contrast | P | Gabrielsson & Weiner p.115 Fig.2.87 | G2, G5 | This is useful, but its core function overlaps with #2 and #3. Keeping it would exceed the high-yield visual density for the opening mechanism cards. | N/A | **REJECT — overlap with retained diagnostics and MM figures** |
| 4 | §2 C2 | Capacity-limited Michaelis–Menten kinetics | P | Gabrielsson & Weiner p.115 Fig.2.88; Rowland & Tozer p.503 Fig.16-9; Rowland & Tozer p.505 Fig.16-10 | G1, G2, G5 | The C2 card combines three visual intuitions: CL falls with concentration, elimination rate plateaus, and phenytoin Css/time-to-plateau blow up near capacity. These are curve-shape concepts. | The learner connects the equation denominator to the clinical asymmetry of phenytoin dosing. | **KEEP** |
| 5 | §2 C2 context | Ethanol capacity/flow/oral F visuals | P/R candidate | Gabrielsson & Weiner p.139 Fig.2.110; Gabrielsson & Weiner p.561 Fig.18.3 | G1, G5 | Ethanol is a strong integrated case, but Content Lock v2 downranks it to an anchor example rather than a full master card. | N/A | **REJECT — lower priority than the core MM and DDI visuals** |
| 6 | §2 C3 | Time-dependent turnover and MBI | N | None | G1, G2, G4 | The key confusion is not one textbook figure but a cross-source distinction: drug concentration clock versus enzyme turnover/recovery clock. A new synthesis schematic is more useful than pointing to one source panel. | The learner stops treating delayed recovery after MBI as ordinary inhibitor washout. | **KEEP** |
| 7 | §2 C3 context | Autoinduction case structure | P candidate | Gabrielsson & Weiner p.581 Fig.22.1–22.2; p.585 Table 22.2 | G1, G5 | The case is valuable but narrower than the two-clock schematic. | N/A | **REJECT — covered by retained C3 synthesis schematic** |
| 8 | §2 C4 | Binding, TMDD, and displacement-only DDI | P | Gabrielsson & Weiner p.132 Fig.2.104; p.133 Fig.2.105 | G1, G2, G5 | Open versus closed system is a structural distinction. Without seeing the system boundary, learners may over-transfer in vitro displacement intuition to in vivo dose decisions. | The learner separates total concentration change from sustained unbound exposure change. | **KEEP** |
| 9 | §2 C4 context | Drug–metabolite model topology | R/P candidate | Gabrielsson & Weiner p.136 Fig.2.107 | G1, G5 | The topology is important, but Content Lock v2 compresses the parent–metabolite model into context rather than a main card. | N/A | **REJECT — context item, not high enough ROI for current budget** |
| 10 | §2 C5 | Quantitative DDI prediction | P | Rowland & Tozer p.550 Fig.17-8 | G1, G2, G5 | Eq.17-11 is a denominator problem with two axes: inhibitor strength and pathway fraction. Text alone does not show why the same inhibitor behaves differently at different fm. | The learner sees fm as the exposure-ratio amplifier, not as a decorative covariate. | **KEEP** |
| 11 | §2 C5 context | Route effect and PM amplification figures | P candidate | Rowland & Tozer p.554 Fig.17-10; p.559 Fig.17-15 | G2, G5 | Both are useful, but C5 already receives a pointer to the core AUC-ratio surface. Adding both would crowd the DDI section. | N/A | **REJECT — retained as source-reading optionality inside C5 brief only** |
| 12 | §2 C6 | Multifaceted/transporter DDI | P | Rowland & Tozer p.565 Fig.17-19 | G1, G2, G5 | C6 asks the learner to notice a non-intuitive signature: exposure can rise while half-life shortens. This pattern is hard to internalize without the source plot. | The learner learns not to label every AUC increase as metabolic inhibition. | **KEEP** |
| 13 | §2 C6 / §5 CP8 | PD additivity/synergy/antagonism | P/R candidate | Rowland & Tozer p.568 Fig.17-21; Gabrielsson & Weiner p.225–226 Fig.3.24–3.25 | G2, G5 | Isobologram and PD curves are useful, but the current session spine is PK nonlinearity and DDI prediction. | N/A | **REJECT — lower priority than transporter/multifaceted DDI under A-Critical budget** |

---

## 2. Figure Strategy Table — View B: Type-sorted Summary

### Pointers (P)

- #2 — C1 diagnostics: Gabrielsson & Weiner Fig.2.85–2.86
- #4 — C2 MM kinetics: Gabrielsson & Weiner Fig.2.88 + Rowland & Tozer Fig.16-9/16-10
- #8 — C4 open vs closed binding systems: Gabrielsson & Weiner Fig.2.104–2.105
- #10 — C5 quantitative inhibition: Rowland & Tozer Fig.17-8
- #12 — C6 multifaceted transporter DDI: Rowland & Tozer Fig.17-19

**Count:** 5 / max 5 for A-Critical → within budget.

### Schematics (R/N combined)

- #1 — N schematic: Session 08 mechanism triage map
- #6 — N schematic: Drug concentration clock vs enzyme turnover clock

**Count:** 2 / max 2 for A-Critical → within budget.

### Images (I)

- None.

**Count:** 0. Image rights are None, so Mode I is not permitted.

---

## 3. Figure Briefs — KEEP Items

### Figure #1 — N schematic

- **Title:** Session 08 mechanism triage map
- **Visual objective:** In 5 seconds, the learner should see that the session is a decision path, not a list of nonlinear PK facts.
- **Core message:** Start with superposition failure, then triage the mechanism as capacity, time, binding, or DDI/PD interaction before translating it into PopPK/TDM/DDI decisions.
- **Elements to include:** diagnostic entry node; dose-normalized plot trigger; four mechanism branches: capacity, time, binding, DDI/PD; downstream outputs: model diagnosis, TDM interpretation, DDI prediction; arrows showing sequence.
- **Elements to exclude:** textbook figure panels; numerical case values; source-page citations inside the schematic; regulatory label wording.
- **Suggested rendering:** Mermaid flowchart.
- **Caption:** Session 08 is organized as a mechanism-triage workflow from superposition failure to pharmacometrics decisions.
- **Alt text:** A flowchart starts with superposition failure and branches to capacity, time, binding, and interaction mechanisms, which then feed modeling, TDM, and DDI interpretation.
- **Source relation:** Newly designed.

### Figure #2 — P pointer

- **Source:** Gabrielsson & Weiner, p.113, Fig.2.85 “Linear and nonlinear absorption and disposition” and Fig.2.86 “Linear, feedback-governed, saturable, and mixed elimination”.
- **Why this figure matters:** These figures are the fastest way to learn the visual grammar of nonlinearity diagnostics. Removing them would make AUC/Dose pattern recognition depend on memory rather than visual classification.
- **When to look:** Before reading C1, then once again after C1 Recap.
- **Learner instruction:** First inspect the direction of AUC/Dose change. Then map that direction to possible CL, F, or distribution changes before naming a mechanistic model.

### Figure #4 — P pointer

- **Source:** Gabrielsson & Weiner, p.115, Fig.2.88 “Concentration-dependent clearance and elimination rate”; Rowland & Tozer, p.503, Fig.16-9 “Phenytoin steady-state concentration vs dosing rate”; Rowland & Tozer, p.505, Fig.16-10 “Phenytoin time-to-plateau vs dosing rate”.
- **Why this figure matters:** C2 depends on seeing the same denominator intuition in three forms: clearance decreases, rate plateaus, and clinical steady state becomes sharply sensitive near capacity.
- **When to look:** After reading the C2 equations and before the C2 clinical anchors.
- **Learner instruction:** Track what happens as concentration or dosing rate approaches capacity. Do not read the curves as simple proportional dose-response plots.

### Figure #6 — N schematic

- **Title:** Two clocks in nonlinear PK: concentration clock vs enzyme turnover clock
- **Visual objective:** In 5 seconds, the learner should distinguish concentration-driven apparent CL change from true time-dependent enzyme-pool change.
- **Core message:** Reversible inhibition mainly follows the perpetrator concentration clock, whereas induction and MBI require an enzyme turnover/recovery clock.
- **Elements to include:** left lane: drug/perpetrator concentration clock; right lane: enzyme pool clock; nodes for reversible inhibition, induction, MBI, recovery; arrows to observed signatures: trough drift and delayed recovery.
- **Elements to exclude:** numerical rate constants; case-specific parameter estimates; exact reproduction of textbook turnover diagrams.
- **Suggested rendering:** Mermaid flowchart.
- **Caption:** Time-dependent kinetics requires a second clock: the enzyme or transporter pool changes more slowly than the plasma concentration profile.
- **Alt text:** A two-lane diagram contrasts a drug concentration clock with an enzyme turnover clock and shows how reversible inhibition, induction, and MBI map to different recovery patterns.
- **Source relation:** Newly designed.

### Figure #8 — P pointer

- **Source:** Gabrielsson & Weiner, p.132, Fig.2.104 “Three in vitro binding systems” and p.133, Fig.2.105 “Three in vivo open binding systems”.
- **Why this figure matters:** The C4 confusion hinges on system boundaries. Removing these figures would let the learner transfer closed-system binding intuition into open-system in vivo interpretation.
- **When to look:** After reading the C4 Open vs closed system subsection.
- **Learner instruction:** Compare which quantities are fixed and which can leave the system. Then re-read the displacement-only warning with those boundaries in mind.

### Figure #10 — P pointer

- **Source:** Rowland & Tozer, p.550, Fig.17-8 “Effect of inhibitor strength and fraction metabolized on AUC ratio”.
- **Why this figure matters:** The AUC-ratio equation is easy to copy but hard to feel. This figure shows why fm controls whether a given inhibitor produces a small or large exposure change.
- **When to look:** Immediately after the C5 reversible competitive inhibition equation.
- **Learner instruction:** Read the figure by holding inhibitor strength constant and moving fm. Then hold fm constant and vary inhibitor strength.

### Figure #12 — P pointer

- **Source:** Rowland & Tozer, p.565, Fig.17-19 “Atorvastatin–rifampin acute transporter-mediated interaction”.
- **Why this figure matters:** This source plot shows the signature that text alone tends to flatten: AUC and Cmax can rise while half-life falls. Removing it would encourage overcalling the case as simple metabolic inhibition.
- **When to look:** After reading the C6 core multifaceted anchors.
- **Learner instruction:** Inspect AUC, Cmax, and half-life together. The key lesson is the joint pattern, not any single metric.

---

## 4. Insertion Map (PATCH MODE)

| # | Reading order | Anchor copied verbatim from Content Lock v2 | Insert position | Marker block |
|---:|---|---|---|---|
| 1 | §1 → before §2 | `## 1.1 지식 그래프 위치` | before next §heading | See Marker Block #1 below |
| 2 | §2 C1 | `## C1. Nonlinearity Diagnostics — superposition이 깨지는 순간부터 시작한다` | before next §heading | See Marker Block #2 below |
| 4 | §2 C2 | `## C2. Capacity-limited Michaelis–Menten Kinetics — $V_{max}$/$K_m$가 dose 조정의 비대칭성을 만든다` | before next §heading | See Marker Block #4 below |
| 6 | §2 C3 | `## C3. Time-dependent Turnover and Mechanism-Based Inhibition — 농도 시계와 enzyme 시계를 분리한다` | before next §heading | See Marker Block #6 below |
| 8 | §2 C4 | `## C4. Binding, TMDD, and Displacement-only DDI — total concentration을 그대로 믿지 않는다` | before next §heading | See Marker Block #8 below |
| 10 | §2 C5 | `## C5. Quantitative DDI Prediction — $f_m$, inhibitor strength, route가 AUC ratio를 만든다` | before next §heading | See Marker Block #10 below |
| 12 | §2 C6 | `## C6. Multifaceted/Transporter and PD Interactions — 하나의 perpetrator가 하나의 mechanism만 갖는다고 가정하지 않는다` | before next §heading | See Marker Block #12 below |

### Marker Block #1

```markdown
<!-- FIGURE_SCHEMATIC -->
Title: Session 08 mechanism triage map
Mode: N
Visual objective: In 5 seconds, the learner should see that the session is a decision path, not a list of nonlinear PK facts.
Core message: Start with superposition failure, then triage the mechanism as capacity, time, binding, or DDI/PD interaction before translating it into PopPK/TDM/DDI decisions.
Elements to include: diagnostic entry node; dose-normalized plot trigger; mechanism branches for capacity, time, binding, and DDI/PD; downstream outputs for model diagnosis, TDM interpretation, and DDI prediction; sequence arrows.
Elements to exclude: textbook figure panels; numerical case values; source-page citations inside the schematic; regulatory label wording.
Suggested rendering: Mermaid
Caption: Session 08 is organized as a mechanism-triage workflow from superposition failure to pharmacometrics decisions.
Alt text: A flowchart starts with superposition failure and branches to capacity, time, binding, and interaction mechanisms, which then feed modeling, TDM, and DDI interpretation.
Source relation: Newly designed
<!-- /FIGURE_SCHEMATIC -->
```

### Marker Block #2

```markdown
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner, p.113, Fig.2.85 and Fig.2.86
Why this matters: These figures are the fastest way to learn the visual grammar of nonlinearity diagnostics. Removing them would make AUC/Dose pattern recognition depend on memory rather than visual classification.
When to look: Before reading C1, then once again after C1 Recap.
Learner instruction: First inspect the direction of AUC/Dose change. Then map that direction to possible CL, F, or distribution changes before naming a mechanistic model.
<!-- /FIGURE_POINTER -->
```

### Marker Block #4

```markdown
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner, p.115, Fig.2.88; Rowland & Tozer, p.503, Fig.16-9; Rowland & Tozer, p.505, Fig.16-10
Why this matters: C2 depends on seeing the same denominator intuition in three forms: clearance decreases, rate plateaus, and clinical steady state becomes sharply sensitive near capacity.
When to look: After reading the C2 equations and before the C2 clinical anchors.
Learner instruction: Track what happens as concentration or dosing rate approaches capacity. Do not read the curves as simple proportional dose-response plots.
<!-- /FIGURE_POINTER -->
```

### Marker Block #6

```markdown
<!-- FIGURE_SCHEMATIC -->
Title: Two clocks in nonlinear PK: concentration clock vs enzyme turnover clock
Mode: N
Visual objective: In 5 seconds, the learner should distinguish concentration-driven apparent CL change from true time-dependent enzyme-pool change.
Core message: Reversible inhibition mainly follows the perpetrator concentration clock, whereas induction and MBI require an enzyme turnover/recovery clock.
Elements to include: left lane for drug/perpetrator concentration clock; right lane for enzyme pool clock; nodes for reversible inhibition, induction, MBI, and recovery; arrows to observed signatures such as trough drift and delayed recovery.
Elements to exclude: numerical rate constants; case-specific parameter estimates; exact reproduction of textbook turnover diagrams.
Suggested rendering: Mermaid
Caption: Time-dependent kinetics requires a second clock: the enzyme or transporter pool changes more slowly than the plasma concentration profile.
Alt text: A two-lane diagram contrasts a drug concentration clock with an enzyme turnover clock and shows how reversible inhibition, induction, and MBI map to different recovery patterns.
Source relation: Newly designed
<!-- /FIGURE_SCHEMATIC -->
```

### Marker Block #8

```markdown
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner, p.132, Fig.2.104; Gabrielsson & Weiner, p.133, Fig.2.105
Why this matters: The C4 confusion hinges on system boundaries. Removing these figures would let the learner transfer closed-system binding intuition into open-system in vivo interpretation.
When to look: After reading the C4 Open vs closed system subsection.
Learner instruction: Compare which quantities are fixed and which can leave the system. Then re-read the displacement-only warning with those boundaries in mind.
<!-- /FIGURE_POINTER -->
```

### Marker Block #10

```markdown
<!-- FIGURE_POINTER -->
Source: Rowland & Tozer, p.550, Fig.17-8
Why this matters: The AUC-ratio equation is easy to copy but hard to feel. This figure shows why fm controls whether a given inhibitor produces a small or large exposure change.
When to look: Immediately after the C5 reversible competitive inhibition equation.
Learner instruction: Read the figure by holding inhibitor strength constant and moving fm. Then hold fm constant and vary inhibitor strength.
<!-- /FIGURE_POINTER -->
```

### Marker Block #12

```markdown
<!-- FIGURE_POINTER -->
Source: Rowland & Tozer, p.565, Fig.17-19
Why this matters: This source plot shows the signature that text alone tends to flatten: AUC and Cmax can rise while half-life falls. Removing it would encourage overcalling the case as simple metabolic inhibition.
When to look: After reading the C6 core multifaceted anchors.
Learner instruction: Inspect AUC, Cmax, and half-life together. The key lesson is the joint pattern, not any single metric.
<!-- /FIGURE_POINTER -->
```

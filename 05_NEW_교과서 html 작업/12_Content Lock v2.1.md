# 12_Content Lock v2.1 — Figure Marker Patch
## Session 12 · Effect Compartment · Tolerance/Rebound · Transduction

**Output mode:** PATCH MODE  
**Reason:** Content Lock v2 is long enough that full-body re-emission risks text drift. This v2.1 file therefore provides **Strategy Table + Figure Briefs + Insertion Map only**. Apply the listed markers to Content Lock v2 without otherwise rewriting the body.

**Phase boundary:** Phase 4C decides figures only. It does **not** generate Mermaid, SVG, plots, or embedded textbook images.  
**Image rights:** None. Textbook figures must be handled as **POINTER** callouts only; no source image insertion. Newly designed schematics are allowed only as Phase 5 render briefs.

---

# 1. Figure Opportunity Scan — Retained Decisions

## 1A. Reading-order Figure Plan

| # | Reading order | Location (§ + concept card) | Mode | Source figure/table | Trigger | Why text alone is insufficient | Expected learning gain | Decision |
|---:|---|---|---|---|---|---|---|---|
| F12-01 | First | §1 Session Header & Roadmap — after `Concept roadmap` block | **N** | None | G3, G4 | The text roadmap lists the branches, but a learner may still treat Link, Tolerance, and Transduction as parallel chapter topics rather than an escalation logic based on the **delayed hidden state**. | Reader sees the entire session as one triage algorithm: delayed drug state vs delayed system state vs delayed signal chain. | **KEEP** |
| F12-02 | Second | §2 Card 1 — after `A. Formal definition` | **P** | G&W Fig.3.53, p.263 | G1, G5 | The sentence “$C_e$ is inferred, not measured” is structurally hard to internalize without seeing the four-panel sequence: plasma C → effect-compartment kinetics → response vs $C_e$ → response-time. | Prevents the learner from treating $C_e$ as an observed concentration or a free fitted curve. | **KEEP** |
| F12-03 | Third | §2 Card 1 — after `E. Plausible fallacy — Link model fitted to turnover data` | **P** | G&W Fig.3.59 + Table 3.10, p.271 | G2, G5 | The pitfall is not only numerical; the visual/model mismatch is what makes dose-dependent EC50/Emax/n obviously implausible. | Learner remembers that Table 3.10 is the link-model pitfall and **not PD13**, reducing the most important case-label error. | **KEEP** |
| F12-04 | Fourth | §2 Card 2 — after `A. Definition` | **P** | R&T Fig.8-2, p.235 | G2, G5 | Hysteresis direction is a phase-plane concept; prose cannot substitute for the chronological arrows around the counterclockwise loop. | Learner can visually connect “same concentration, different response” to sampling time/order and avoid over-reading direction as final model choice. | **KEEP** |
| F12-05 | Fifth | §2 Card 3 — after `C. PD13 anchor — repeated infusion tolerance/rebound` | **P** | G&W Fig.13.1 + Table 13.1, pp.806–808 | G1, G5 | Trough drift/carry-over is a time-course pattern; the text gives values but does not show why repeated infusion reveals the hidden moderator state. | Learner ties Model II superiority to visible repeated-dose memory rather than to AIC/WRSS alone. | **KEEP** |
| F12-06 | Sixth | §2 Card 3 — after `E. Why the sign matters` | **N** | None | G1, G4 | The negative-feedback sign is easy to read algebraically but hard to see dynamically: drug pushes R, R builds M, M pushes back, M persists. | Learner forms a stable mental model for tolerance and rebound as one feedback loop, not two separate phenomena. | **KEEP** |
| F12-07 | Seventh | §2 Card 4 — after `A. Formal definition` and before `B. Core equations` | **P** | G&W Fig.3.98 + Fig.3.99, p.323 | G1, G5 | Transit-chain logic is spatial/temporal: receptor coupling and observed response are separated by sequential events, and the 15–20 h onset delay is the core visual evidence. | Learner distinguishes “drug reaches site slowly” from “signal propagates downstream slowly.” | **KEEP** |

## 1B. Type-sorted Summary and Budget Check

- **Pointers (P):** F12-02, F12-03, F12-04, F12-05, F12-07 → **5 / max 5** for A-Critical.
- **Schematics (R/N combined):** F12-01, F12-06 → **2 / max 2** for A-Critical.
- **Images (I):** none → image rights do not permit textbook image insertion.

**Budget verdict:** PASS.

---

# 2. Downselected / Rejected Candidate Notes

| Candidate | Decision | Reason |
|---|---|---|
| G&W Fig.3.51, p.262 — direct vs delayed response and hysteresis | REJECT as separate marker | Conceptually important, but F12-04 covers the learner’s phase-plane need with a concrete R&T counterclockwise example; F12-02 covers the Link model mechanism. |
| G&W Fig.3.52, p.262 — PK→Link→PD chain | REJECT as separate marker | Useful, but F12-02 uses the richer G&W Fig.3.53, which includes the time sequence and inference logic. |
| G&W Fig.3.54, p.266 — effect of $k_{e0}$ on equilibration speed | REJECT | Helpful for $t_{1/2,k_{e0}}$, but the card’s ODE and assumptions table already carry the concept; budget reserved for more confusion-prone visuals. |
| G&W Table 3.9, p.269 — literature $t_{1/2,k_{e0}}$ examples | REJECT as figure marker | Numeric anchors are already included in text; the visual table adds little structural value. |
| R&T Fig.8-3 / Fig.8-5, pp.236/238 — downstream measurement sites | REJECT as separate marker | Their conceptual role is absorbed into F12-01 and F12-07; adding them would duplicate downstream/cascade messaging. |
| R&T Fig.8-18 / Fig.8-24, pp.250/256 — succinylcholine duration | REJECT | Important for correcting the succinylcholine attribution, but it is a context anchor rather than a core structural figure for this Content Lock. |
| PD20 Fig.20.1 / Fig.20.2, pp.836/839 | REJECT | PD20 is retained as numeric anchor; figures are useful but not necessary once F12-02 and F12-03 are included. |
| PD21 Table 21.1, p.845 | REJECT | The $k_{e0}$/$k_{out}$/$k_{off}$ comparison is already in Confusion Pair 1; a separate marker would not add a new visual structure. |
| PD35 Table 35.1, p.914 | REJECT as marker | The full table is already reproduced in Card 4. F12-07 should instead direct attention to the transduction architecture/onset-delay figure. |

---

# 3. Figure Briefs for Phase 5

## F12-01 — NEW SCHEMATIC

- **Title:** Three Hidden Clocks Behind PK/PD Time Delay
- **Visual objective:** In 5 seconds, the learner should see that one observed delay branches into three different delayed states.
- **Core message:** A delay is not a mechanism; the model depends on whether the delayed state is $C_e$, $R/M$, or downstream transit states.
- **Elements to include:**
  - Start node: `Observed concentration–response time delay`
  - Decision node: `Which hidden state is delayed?`
  - Branch 1: `Drug at biophase → Link model / $k_{e0}$`
  - Branch 2: `Physiological response/adaptation → Turnover/Tolerance / $k_{out}$, $k_{tol}$, $M$`
  - Branch 3: `Signal propagation → Transduction / $n \times \tau$`
  - Bottom row: diagnostic checks — `linear PK + same $t_{max}$`, `trough drift/rebound`, `delayed sigmoidal onset`
- **Elements to exclude:** Specific drug examples, EC50 values, AIC/WRSS, NONMEM code.
- **Suggested rendering:** Mermaid flowchart.
- **Caption:** Observed delay is first triaged by naming the delayed hidden state.
- **Alt text:** Flowchart showing one observed concentration–response delay branching into biophase delay, system adaptation, and signal-transduction delay.
- **Source relation:** Newly designed synthesis schematic.

## F12-02 — POINTER

- **Source:** Gabrielsson & Weiner 5e, p.263, Fig.3.53, “Schematic diagram of the effect compartment model.”
- **Why this figure matters:** It shows the full inference path from plasma concentration to $C_e$ to response, making clear why $C_e$ is not directly measured and why response-time data are required.
- **When to look:** Immediately after reading Card 1 `A. Formal definition`, before reading the one-compartment derivation.
- **Learner instruction:** In the source figure, follow the numbered sequence from plasma concentration to effect-compartment concentration and then to response. Ask which panel would be impossible to draw if only steady-state data were available.

## F12-03 — POINTER

- **Source:** Gabrielsson & Weiner 5e, p.271, Fig.3.59 and Table 3.10, “Problems and pitfalls” link-model example.
- **Why this figure matters:** The Table 3.10 values show how fitting turnover-generated data with a Link model can create implausible dose-dependent PD parameters; the figure/table pair anchors the corrected point that this is **not PD13**.
- **When to look:** After reading Card 1 `E. Plausible fallacy — Link model fitted to turnover data`.
- **Learner instruction:** Compare the simultaneous fit with dose-stratified fits. Focus on how EC50 and Emax change by dose; then verify that the label is §3.9.7/Table 3.10, not PD13.

## F12-04 — POINTER

- **Source:** Rowland & Tozer 5e, p.235, Fig.8-2, naproxen counterclockwise hysteresis after oral 500 mg.
- **Why this figure matters:** Hysteresis is easiest to misunderstand unless the learner sees the chronological path around the concentration–response loop.
- **When to look:** After Card 2 `A. Definition`, before using the diagnostic matrix.
- **Learner instruction:** Trace the time labels around the loop. Identify where the same concentration corresponds to different responses, then state why loop direction is only a diagnostic clue.

## F12-05 — POINTER

- **Source:** Gabrielsson & Weiner 5e, pp.806–808, Fig.13.1 and Table 13.1, PD13 repeated-infusion tolerance/rebound model comparison.
- **Why this figure matters:** PD13 is the proper tolerance/rebound case, and its value is the repeated-infusion memory pattern, not merely the numerical AIC/WRSS comparison.
- **When to look:** After Card 3 `C. PD13 anchor — repeated infusion tolerance/rebound`.
- **Learner instruction:** Inspect whether the second infusion behaves like a reset of the first. Then connect that pattern to the moderator state $M$ and Model II’s superior fit.

## F12-06 — NEW SCHEMATIC

- **Title:** Moderator Memory Loop: Drug Pushes R, R Builds M, M Pushes Back
- **Visual objective:** In 5 seconds, the learner should see how one negative-feedback loop can produce both tolerance during dosing and rebound after withdrawal.
- **Core message:** Tolerance and rebound are different time phases of the same delayed counter-regulatory state.
- **Elements to include:**
  - `Drug stimulus S(C)` → positive arrow to `Response R`
  - `Response R` → delayed positive arrow to `Moderator M`
  - `Moderator M` → negative arrow back to `Response R`
  - Time labels: `During dosing: M rises and suppresses R`; `After withdrawal: M persists and can pull R beyond baseline`
  - Small equation labels: `dR/dt = k_in S(C) − k_out M`; `dM/dt = k_tol(R − M)`
- **Elements to exclude:** Jacobian, trace/determinant, PD13 numerical parameter values, unrelated tolerance mechanisms.
- **Suggested rendering:** Mermaid flowchart or inline SVG if negative feedback arrow layout is clearer.
- **Caption:** The moderator model turns tolerance and rebound into one delayed negative-feedback system.
- **Alt text:** Diagram showing drug stimulus increasing response, response building a delayed moderator, and the moderator suppressing response.
- **Source relation:** Newly designed synthesis schematic grounded in the moderator ODEs, not an exact textbook reproduction.

## F12-07 — POINTER

- **Source:** Gabrielsson & Weiner 5e, p.323, Fig.3.98 receptor transduction model and Fig.3.99 15–20 h onset-delay example.
- **Why this figure matters:** Transduction is not another distribution delay; it is a sequence between receptor coupling and observed response. The paired figures show both the chain concept and the onset-delay pattern that motivates it.
- **When to look:** After Card 4 `A. Formal definition`, before the transduction ODEs.
- **Learner instruction:** First inspect the chain from receptor-ligand coupling to response, then inspect the 15–20 h onset-delay pattern. State why a single $k_{e0}$ link would answer a different question.

---

# 4. Insertion Map — Apply These Markers to Content Lock v2

> **Rule:** Insert only the marker blocks below. Do not change surrounding prose, equations, page tags, `<!-- ANNOTATION -->`, or existing semantic markers.

---

## Insert F12-01

**Location:** §1 Session Header & Roadmap, immediately after the `Concept roadmap` code block and before the existing `<!-- ANCHOR -->` paragraph.

**Anchor text before insertion:**

```md
   └─ onset shape: immediate exponential vs delayed sigmoid
```

**Marker block to insert:**

```md
<!-- FIGURE_DECISION: F12-01 | MODE=N | PHASE5_RENDER=Mermaid flowchart -->
**Figure Marker F12-01 — Three Hidden Clocks Behind PK/PD Time Delay**  
Phase 5 should render a new schematic showing that one observed concentration–response delay branches into three delayed hidden states: biophase concentration $C_e$, adaptive response/moderator state $R/M$, and downstream transit states $n \times \tau$.  
**Purpose:** prevent the reader from treating Link, Tolerance, and Transduction as parallel labels rather than a mechanism-triage sequence.  
**Do not render in Phase 4C.**
```

---

## Insert F12-02

**Location:** §2 Card 1, immediately after `A. Formal definition` paragraph and before `### B. Core equations`.

**Anchor text before insertion:**

```md
... steady-state data alone are insufficient [G&W p.263].
```

**Marker block to insert:**

```md
<!-- FIGURE_DECISION: F12-02 | MODE=P | POINTER_ONLY -->
**Figure Pointer F12-02 — Effect-compartment inference sequence**  
Inspect **G&W Fig.3.53 (p.263)** before reading the derivation. Follow the source figure from plasma concentration to effect-compartment concentration $C_e$, then to response vs $C_e$ and response-time.  
**Purpose:** show why $C_e$ is inferred from response-time data rather than directly measured.  
**No image insertion; source figure must be viewed in the textbook/PDF.**
```

---

## Insert F12-03

**Location:** §2 Card 1, immediately after subsection `E. Plausible fallacy — Link model fitted to turnover data`, after the paragraph ending with `absorbing turnover/adaptation misspecification [G&W pp.271–272].`

**Anchor text before insertion:**

```md
... the Link model is likely absorbing turnover/adaptation misspecification [G&W pp.271–272].
```

**Marker block to insert:**

```md
<!-- FIGURE_DECISION: F12-03 | MODE=P | POINTER_ONLY -->
**Figure Pointer F12-03 — Link-model pitfall is Table 3.10, not PD13**  
Inspect **G&W Fig.3.59 and Table 3.10 (p.271)** after this pitfall paragraph. Compare simultaneous and dose-stratified fits, focusing on the implausible dose-dependent EC50/Emax/n pattern.  
**Purpose:** anchor the corrected case identity: this is §3.9.7/Table 3.10 with PD12 data, not PD13.  
**No image insertion; source figure/table must be viewed in the textbook/PDF.**
```

---

## Insert F12-04

**Location:** §2 Card 2, immediately after `A. Definition` paragraph and before `### B. Diagnostic matrix`.

**Anchor text before insertion:**

```md
... counterclockwise hysteresis가 나타난다 [R&T pp.234–235].
```

**Marker block to insert:**

```md
<!-- FIGURE_DECISION: F12-04 | MODE=P | POINTER_ONLY -->
**Figure Pointer F12-04 — Counterclockwise hysteresis as chronological loop**  
Inspect **R&T Fig.8-2 (p.235)** before using the diagnostic matrix. Trace the time labels around the naproxen loop and identify where the same concentration corresponds to different responses.  
**Purpose:** make hysteresis direction a visible time-ordered path, not a verbal label.  
**No image insertion; source figure must be viewed in the textbook/PDF.**
```

---

## Insert F12-05

**Location:** §2 Card 3, immediately after the paragraph in `C. PD13 anchor — repeated infusion tolerance/rebound` ending with `more informative than a single dose for tolerance [G&W p.808].`

**Anchor text before insertion:**

```md
... repeated-dose data are more informative than a single dose for tolerance [G&W p.808].
```

**Marker block to insert:**

```md
<!-- FIGURE_DECISION: F12-05 | MODE=P | POINTER_ONLY -->
**Figure Pointer F12-05 — PD13 repeated-infusion memory pattern**  
Inspect **G&W Fig.13.1 and Table 13.1 (pp.806–808)** after the PD13 paragraph. Focus on whether the second infusion behaves like a clean reset or shows carry-over from the hidden moderator state.  
**Purpose:** connect Model II superiority to visible repeated-dose memory, not only to AIC/WRSS values.  
**No image insertion; source figure/table must be viewed in the textbook/PDF.**
```

---

## Insert F12-06

**Location:** §2 Card 3, immediately after `E. Why the sign matters` paragraph and before `<!-- RECAP -->`.

**Anchor text before insertion:**

```md
... **drug pushes R, R builds M, M pushes back**.
```

**Marker block to insert:**

```md
<!-- FIGURE_DECISION: F12-06 | MODE=N | PHASE5_RENDER=Mermaid flowchart or inline SVG -->
**Figure Marker F12-06 — Moderator Memory Loop**  
Phase 5 should render a new schematic: `Drug stimulus S(C) → Response R → delayed Moderator M ┤ Response R`, with phase labels for dosing and withdrawal. Include the compact ODE labels `dR/dt = k_in S(C) − k_out M` and `dM/dt = k_tol(R − M)`.  
**Purpose:** show tolerance and rebound as two phases of one delayed negative-feedback loop.  
**Do not render in Phase 4C.**
```

---

## Insert F12-07

**Location:** §2 Card 4, immediately after `A. Formal definition` paragraph and before `### B. Core equations`.

**Anchor text before insertion:**

```md
... corresponding fractional turnover rate $k_{out}=1/\tau$ [G&W pp.323–325].
```

**Marker block to insert:**

```md
<!-- FIGURE_DECISION: F12-07 | MODE=P | POINTER_ONLY -->
**Figure Pointer F12-07 — Transduction chain and delayed onset**  
Inspect **G&W Fig.3.98 and Fig.3.99 (p.323)** before reading the transduction ODEs. First identify the receptor-to-response chain, then inspect the 15–20 h onset-delay pattern.  
**Purpose:** separate “drug reaches the site slowly” from “signal propagation to the measured response is slow.”  
**No image insertion; source figures must be viewed in the textbook/PDF.**
```

---

# 5. Phase 5 Rendering Queue

| Figure ID | Phase 5 action | Rendering constraint |
|---|---|---|
| F12-01 | Generate new Mermaid flowchart | Do not reproduce textbook figures; use only abstract nodes/arrows from Content Lock logic. |
| F12-02 | Convert to styled pointer callout | No image; include source page/figure instruction only. |
| F12-03 | Convert to styled pointer callout | No image; emphasize “not PD13.” |
| F12-04 | Convert to styled pointer callout | No image; learner must inspect source loop direction. |
| F12-05 | Convert to styled pointer callout | No image; pair Fig.13.1 with Table 13.1. |
| F12-06 | Generate new Mermaid or inline SVG feedback loop | Must show negative feedback clearly; avoid stability/Jacobian math. |
| F12-07 | Convert to styled pointer callout | No image; pair Fig.3.98 with Fig.3.99. |

---

# 6. Completion Note

- Figure work separated from text-final Content Lock body.
- No Mermaid, SVG, generated chart, or textbook image inserted in Phase 4C.
- Pointer budget and schematic budget both within A-Critical limits.
- Source-image rights respected: no textbook image embedding.
- PATCH MODE prevents unintended changes to Content Lock v2 prose, equations, page tags, and existing annotation markers.

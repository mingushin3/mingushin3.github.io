# 10_Content Lock v2.1 — Figure Marker Insertion Patch

**Output mode: PATCH MODE**

**Mode decision:** Content Lock v2 is long enough that full-body re-emission would create avoidable text-drift risk. Therefore this deliverable provides the Strategy Table, Figure Briefs, and Insertion Map only. The Content Lock v2 body should remain unchanged; Phase 5 should splice the marker blocks below into the specified anchors.

**Image rights:** None. Textbook figures are not embedded. All source figures are handled as `POINTER` callouts or structurally distinct redraw briefs.

**Figure budget:** A-Critical mode → Pointer max 5, Schematic max 2, Image none.

---

# (A) Reading-order Figure Plan

| # | Reading order | Location (§ + concept card) | Mode | Source figure/table | Trigger | Why text alone is insufficient | Expected learning gain | Decision |
|---:|---|---|---|---|---|---|---|---|
| 1 | §1 | Session Header & Roadmap | P | G&W p.199, Fig.3.1 | G3, G5 | The text lists C1–C5 sequentially, but the learner may not yet see the two orthogonal axes: concentration-response sensitivity and response-time behavior. | Establishes the whole session as a dual-axis PK→PD translation problem before detailed cards begin. | KEEP |
| 2 | §2 C1 | Law of Mass Action derivation | P | G&W p.202, Fig.3.3 | G5 | The receptor equilibrium figure is useful, but the derivation already states the reversible binding system, and C1 receives a higher-ROI Kd/EC50 schematic below. | Lower incremental gain after C1 derivation and schematic. | REJECT — redundant within C1 budget |
| 3 | §2 C1 | Kd vs EC50, cascade, spare receptor boundary | R | G&W p.204, Fig.3.4; p.205, Fig.3.5 | G1, G2, G5 | Text alone cannot make the left-shift between receptor occupancy and functional response visually stable. This is the highest-risk confusion in C1. | Prevents mapping Kd directly onto EC50; makes transduction/cascade amplification visible. | KEEP |
| 4 | §2 C2 | Ordinary Emax vs Sigmoid Emax curve family | P | G&W p.213, Fig.3.12; p.216, Fig.3.16 | G5 | The equations and PD3 anchor already carry the conceptual load. Adding another curve pointer would compete with the more important PD3 design-discrimination evidence. | Limited additional gain beyond existing equations and selected PD3 pointer. | REJECT — lower ROI than PD3 |
| 5 | §2 C2 | PD3 model discrimination and concentration-range design | P | G&W Case Study PD3 p.733, Fig.PD3-3.1; p.735, Table PD3-3.2; p.741, Table PD3-3.4 | G4, G5 | The text states that 0–800 µg/L design enables model discrimination, but the learner must inspect the original figure/table pattern to see why this is a design-information problem. | Converts “sigmoid model fit” from a parameter story into a concentration-range and precision story. | KEEP |
| 6 | §2 C3 | Hysteresis as time-delay diagnostic | P | R&T p.234, Fig.8-1; p.235, Fig.8-2 | G2, G5 | Hysteresis is inherently visual. Text can define “different path,” but cannot show the same concentration producing different responses during rising/falling phases. | Makes counterclockwise hysteresis and plasma-response dissociation immediately visible. | KEEP |
| 7 | §2 C4 | Effect compartment vs downstream/indirect response topology | R | R&T p.236, Fig.8-3 | G1, G2, G5 | The C4 distinction is structural: site equilibration delay and turnover delay can both fit delayed response, but they imply different causal topology. | Prevents the learner from treating effect compartment and indirect response as interchangeable delay patches. | KEEP |
| 8 | §2 C5 | PD-rate-limited persistence after plasma decline | P | R&T p.251, Fig.8-20; p.252, Fig.8-21 | G2, G5 | The core message depends on seeing plasma concentration disappear while response remains. This time-axis separation is hard to internalize from text alone. | Anchors aspirin/omeprazole as PD-rate-limited examples without adding guideline-level extrapolation. | KEEP |
| 9 | §2 C5 | Duration vs dose and succinylcholine dose-duration relation | P | R&T p.255, Fig.8-23; p.256, Fig.8-24 | G1, G5 | The logarithmic dose-duration relationship is mathematically compact but visually non-intuitive. | Links the duration equation to the empirical “dose doubling adds about one half-life” pattern. | KEEP |
| 10 | §8 | Meta-frame / professional moat synthesis | N | None | G3, G4 | A synthesis diagram would be attractive, but the budget is already filled by concept-critical figures that remove larger local misunderstandings. | Low incremental gain at this stage. | REJECT — budget and drift control |

---

# (B) Type-sorted Summary

**Pointers (P):** #1, #5, #6, #8, #9 → 5 / 5 used.

**Schematics (R/N):** #3, #7 → 2 / 2 used.

**Images (I):** none → Image rights are None; textbook image insertion is not allowed.

**Rejected:** #2, #4, #10. Rejections are based on redundancy or lower ROI, not because the source figures are poor.

---

# Figure Briefs for KEEP Items

## Figure #1 — POINTER

- **Source:** Gabrielsson & Weiner 5e, p.199, Fig.3.1 — pharmacodynamic characteristics: exposure drives efficacy, potency, onset, intensity, duration.
- **Why this figure matters:** It frames the session as two linked problems: concentration-response sensitivity and response-time behavior. Without this frame, C1–C5 may feel like separate formulas rather than a single PK→PD translation chain.
- **When to look:** Before reading §1 Roadmap, or immediately after the §1 Big Idea.
- **Learner instruction:** Inspect the left panel for potency/efficacy and the right panel for onset/intensity/duration. Then map C1–C2 to the left panel and C3–C5 to the right panel.

## Figure #3 — REDRAW

- **Title:** Kd와 EC50의 분리: receptor occupancy → transduction → response
- **Visual objective:** In 5 seconds, the learner should see that the functional response curve can be left-shifted from the receptor occupancy curve.
- **Core message:** `Kd` belongs to binding affinity, whereas `EC50` belongs to the amplified tissue/system response.
- **Elements to include:**
  - Shared x-axis: concentration.
  - Curve 1: receptor occupancy / stimulus curve labeled `Kd`.
  - Curve 2: functional response curve shifted left and labeled `EC50`.
  - A simple arrow chain: receptor occupancy → stimulus/transduction → response.
  - Small note: “EC50 may differ from Kd; exceptions exist.”
- **Elements to exclude:** Cheng-Prusoff derivation, full/partial agonist profiles, exact textbook layout, original color scheme, receptor cartoon details.
- **Suggested rendering:** inline SVG.
- **Caption:** Receptor binding and functional response need not align; transduction/cascade amplification can make EC50 differ from Kd.
- **Alt text:** Two concentration-response curves share one concentration axis; the functional response curve is left-shifted from receptor occupancy, illustrating EC50–Kd separation.
- **Source relation:** Redrawn from textbook concept (no exact reproduction).

## Figure #5 — POINTER

- **Source:** Gabrielsson & Weiner 5e, Case Study PD3, p.733 Fig.PD3-3.1; p.735 Table PD3-3.2; p.741 Table PD3-3.4.
- **Why this figure matters:** The point is not merely that a sigmoid model fits better. The original PD3 materials show how dose/concentration range changes model discrimination and parameter precision.
- **When to look:** After reading Card C2 §B and §C-2.
- **Learner instruction:** Compare the 0–500 and 0–800 µg/L designs before reading the VIF discussion. Ask whether the data range is wide enough to reveal curvature around IC50 and the upper response region.

## Figure #6 — POINTER

- **Source:** Rowland & Tozer 5e, p.234 Fig.8-1; p.235 Fig.8-2.
- **Why this figure matters:** Hysteresis cannot be fully understood as prose. The visual loop shows why the same plasma concentration can correspond to different response values depending on whether concentration is rising or falling.
- **When to look:** After reading Card C3 §A–B.
- **Learner instruction:** In Fig.8-2, follow the chronological sampling numbers around the loop. Focus on the fact that concentration-response is path-dependent, not a single static curve.

## Figure #7 — REDRAW

- **Title:** Delay-source topology: effect-site equilibration vs system turnover
- **Visual objective:** In 5 seconds, the learner should distinguish a plasma-to-effect-site delay from a downstream response-turnover delay.
- **Core message:** Effect compartment and indirect response are not interchangeable delay patches; they encode different causal structures.
- **Elements to include:**
  - Path A: plasma concentration `C(t)` → effect-site concentration `Ce(t)` → response `E(t)`.
  - Path B: plasma concentration `C(t)` → modulation of `kin/kout` → turnover response `R(t)`.
  - Labels: “site equilibration delay” and “system turnover delay.”
  - Diagnostic callout: “peak-time dose-dependence vs dose-invariance.”
- **Elements to exclude:** NONMEM code, numerical `ke0`, dense feedback loops, more than one downstream turnover compartment.
- **Suggested rendering:** Mermaid flowchart.
- **Caption:** The same delayed response pattern can arise from site equilibration or from biological turnover; model choice determines extrapolation behavior.
- **Alt text:** Two parallel causal paths show plasma concentration leading either to an effect-site compartment and response, or to kin/kout turnover control and delayed response.
- **Source relation:** Redrawn from textbook concept (no exact reproduction).

## Figure #8 — POINTER

- **Source:** Rowland & Tozer 5e, p.251 Fig.8-20; p.252 Fig.8-21.
- **Why this figure matters:** These examples force the learner to separate plasma half-life from effect duration. The visual time-axis gap is the key structural signal.
- **When to look:** After reading Card C5 §C.
- **Learner instruction:** Compare the plasma concentration time course with the response time course. Do not infer aspirin perioperative guidance or omeprazole clinical rules from this figure; use it only to recognize PD-rate-limited persistence.

## Figure #9 — POINTER

- **Source:** Rowland & Tozer 5e, p.255 Fig.8-23; p.256 Fig.8-24.
- **Why this figure matters:** The duration equation is compact, but the learner must see how dose changes translate into threshold-crossing time. Fig.8-24 anchors the abstract relationship in the succinylcholine example.
- **When to look:** After reading Card C5 §B.
- **Learner instruction:** Trace where each dose curve crosses the minimum effective amount/effect threshold. Then connect that crossing time to the statement that dose doubling can extend duration by about one half-life under the stated assumptions.

---

# Insertion Map (PATCH MODE)

Use these anchors to splice marker blocks into the unchanged `10_Content Lock v2.md` body. Insert markers in the listed reading order.

| # | Reading order | Anchor copied from Content Lock v2 | Insert position | Marker block ID |
|---:|---|---|---|---|
| 1 | §1 | `# §1 — Session Header & Roadmap` | before next §heading | Marker Block #1 |
| 2 | §2 C1 | `## Card C1 — Law of Mass Action → Emax 골격` | after this anchor card | Marker Block #2 |
| 3 | §2 C2 | `## Card C2 — Sigmoid Emax / Hill Model [Apex]` | after this anchor card | Marker Block #3 |
| 4 | §2 C3 | `## Card C3 — Hysteresis: 시간 지연의 진단 도구` | after this anchor card | Marker Block #4 |
| 5 | §2 C4 | `## Card C4 — Effect Compartment + Systems-in-flux / Indirect Response` | after this anchor card | Marker Block #5 |
| 6 | §2 C5 | `## Card C5 — AUEC + Duration + PK/PD Rate-Limiting` | after this anchor card | Marker Block #6 |
| 7 | §2 C5 | `## Card C5 — AUEC + Duration + PK/PD Rate-Limiting` | after Marker Block #6, same anchor card | Marker Block #7 |

## Marker Block #1

```text
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.199, Fig.3.1
Why this matters: This figure frames the whole session as two linked PD problems: concentration-response sensitivity and response-time behavior. Without it, C1–C5 may look like separate formulas rather than one PK→PD translation chain.
When to look: before reading §1 Roadmap or immediately after the §1 Big Idea
Learner instruction: Inspect the left panel for potency/efficacy and the right panel for onset/intensity/duration. Then map C1–C2 to the left panel and C3–C5 to the right panel.
<!-- /FIGURE_POINTER -->
```

## Marker Block #2

```text
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
```

## Marker Block #3

```text
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, Case Study PD3, p.733 Fig.PD3-3.1; p.735 Table PD3-3.2; p.741 Table PD3-3.4
Why this matters: The key lesson is not merely that a sigmoid model fits better. The original PD3 materials show how concentration range changes model discrimination and parameter precision.
When to look: after reading Card C2 §B and §C-2
Learner instruction: Compare the 0–500 and 0–800 µg/L designs before reading the VIF discussion. Ask whether the data range is wide enough to reveal curvature around IC50 and the upper response region.
<!-- /FIGURE_POINTER -->
```

## Marker Block #4

```text
<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.234 Fig.8-1; p.235 Fig.8-2
Why this matters: Hysteresis cannot be fully understood as prose. The visual loop shows why the same plasma concentration can correspond to different response values depending on whether concentration is rising or falling.
When to look: after reading Card C3 §A–B
Learner instruction: In Fig.8-2, follow the chronological sampling numbers around the loop. Focus on the fact that concentration-response is path-dependent, not a single static curve.
<!-- /FIGURE_POINTER -->
```

## Marker Block #5

```text
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
```

## Marker Block #6

```text
<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.251 Fig.8-20; p.252 Fig.8-21
Why this matters: These examples force the learner to separate plasma half-life from effect duration. The visual time-axis gap is the key structural signal.
When to look: after reading Card C5 §C
Learner instruction: Compare the plasma concentration time course with the response time course. Do not infer aspirin perioperative guidance or omeprazole clinical rules from this figure; use it only to recognize PD-rate-limited persistence.
<!-- /FIGURE_POINTER -->
```

## Marker Block #7

```text
<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.255 Fig.8-23; p.256 Fig.8-24
Why this matters: The duration equation is compact, but the learner must see how dose changes translate into threshold-crossing time. Fig.8-24 anchors the abstract relationship in the succinylcholine example.
When to look: after reading Card C5 §B
Learner instruction: Trace where each dose curve crosses the minimum effective amount/effect threshold. Then connect that crossing time to the statement that dose doubling can extend duration by about one half-life under the stated assumptions.
<!-- /FIGURE_POINTER -->
```

---

# Patch Completion Notes

- Content Lock v2 body is not re-emitted in this file.
- No Mermaid, SVG, or HTML code is generated; only Phase 5 briefs and marker blocks are provided.
- No image insertion is proposed because image rights are None.
- Source page tags in Content Lock v2 remain untouched.
- Selected markers comply with A-Critical budget: Pointers 5/5, Schematics 2/2, Images 0.

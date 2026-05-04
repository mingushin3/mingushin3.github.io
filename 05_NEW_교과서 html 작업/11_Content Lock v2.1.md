# 11_Content Lock v2.1 — Figure Marker Insertion Plan

**Output mode declaration: PATCH MODE**

**Mode rationale**: Content Lock v2 is long (>6000 words; approximately 6935 whitespace-delimited tokens in the local file). Therefore the full Content Lock body is not re-emitted. This v2.1 deliverable contains only the visual strategy, briefs, and insertion map needed to splice figure markers into the unchanged Content Lock v2 file.

**Phase boundary**: This file decides figures only. It does not generate Mermaid, SVG, HTML, or any image. Source textbook images are not embedded because image rights are not available; all source textbook visuals are handled as POINTERs, and one structurally distinct REDRAW brief is provided for Phase 5.

---

## Figure Strategy Table — View A. Reading-order Figure Plan

| # | Reading order | Location (§ + concept card) | Mode | Source figure(s) | Trigger | Why text alone is insufficient | Expected learning gain | Decision |
|---:|---|---|---|---|---|---|---|---|
| 1 | §2-1 | Card 1 — Turnover Model Foundation + Hysteresis Classification | P | G&W Fig 3.33 [G p.235] + R&T Fig 8-2 [T p.235] | G2, G5 | Direct vs delayed response and counterclockwise hysteresis are temporal patterns; prose definitions do not show that the same concentration can map to different responses depending on time path. | Learner can visually separate direct link, delayed response, and hysteresis loop before reading later model-discrimination cards. | KEEP |
| 2 | §2-2 | Card 2 — Four-Model Taxonomy: Inhibit/Stimulate × Production/Loss | R | Redrawn from G&W Table 3.3, Table 3.5, Figs 3.35–3.39 concept set [G pp.238–247] | G1, G2, G4 | The existing table lists ODEs, but the learner must mentally infer how input/output site controls `tss`; that inference is central and error-prone. | A single structural map links action site → effective time constant → expected `tss` behavior. | KEEP |
| 3 | §2-4 | Card 4 — Imax/Emax Multiplier Semantics + Linear PK ≠ Linear PD | P | G&W Fig 3.40 [G p.246] | G2, G5 | The semantic trap is geometric: `Emax`, `Imax`, and observed `ΔR` are not the same vertical distance across direct and turnover forms. | Prevents cross-model parameter comparison errors by making the `ΔR/R0` distinction visible. | KEEP |
| 4 | §2-5 | Card 5 — Graphical Initial Parameter Estimation + Blocking Dose / DRT | P | R&T Fig 8-15 [T p.246] | G1, G5 | Blocking-dose logic is a slope-extraction procedure; equations alone do not show how the observed response-time profile is converted into synthesis-rate reasoning. | Learner sees why blocked synthesis exposes a degradation clock and why manual initial estimation is mechanistic, not cosmetic. | REJECT — useful, but lower ROI than Card 7/8 figures under pointer budget. |
| 5 | §2-6 | Card 6 — Irreversible Drug Action + Target Consumption | P | G&W Fig 3.47 [G p.256] or R&T Figs 8-20–8-21 [T pp.251–252] | G2, G5 | Reversible vs irreversible persistence is visually helpful, but the current Card 6 text already separates `drug-off` turnover from target/cell replacement. | Would reinforce target-consumption intuition. | REJECT — lower ROI than the clock and duration figures because Card 6 is not the session’s apex decision point. |
| 6 | §2-7 | Card 7 — Turnover vs Effect Compartment Discrimination Crisis | P | G&W Fig 6.1 [G p.759] + G&W Table 6.1 [G p.763] | G2, G5 | The apex lesson is that two causal models can look nearly the same; the learner must inspect the fit/estimate equivalence, not only read the warning. | Makes “fit quality alone is insufficient” concrete by pairing curve similarity with similar `kout/ke0`. | KEEP |
| 7 | §2-8A | Card 8 — PK Clock vs PD Clock + Duration Formula Boundary | P | R&T Fig 8-11 [T p.243] | G2, G5 | PK vs PD rate-limiting is a comparative time-course concept; text alone can hide that the same mechanism can have different limiting clocks across drugs. | Learner sees acenocoumarol vs phenprocoumon as the canonical “same PD system, different slow clock” example. | KEEP |
| 8 | §2-8C | Card 8 — PK Clock vs PD Clock + Duration Formula Boundary | P | R&T Fig 8-23 [T p.255] + R&T Fig 8-24 [T p.256] | G1, G5 | `tD` and dose-doubling are logarithmic time relationships; without the source plot, the formula can be memorized without understanding its visual consequence. | Learner sees why dose doubling adds one half-life of duration only under the PK-rate-limited boundary. | KEEP |
| 9 | §8 | Meta-Frame & Big Picture | N | Newly designed workflow overview | G3, G4 | A workflow schematic would be attractive, but the final locked summary already states the sequence explicitly. | Would reinforce the overall workflow. | REJECT — decorative/summary value; not necessary under strict visual ROI. |

---

## Figure Strategy Table — View B. Type-sorted Summary

**Pointers (P): #1, #3, #6, #7, #8 → 5 / max 5**

- #1 Card 1 paired pointer: direct/delayed response + clinical hysteresis.
- #3 Card 4 pointer: Imax/Emax semantic distinction.
- #6 Card 7 pointer: turnover vs effect-compartment equivalence.
- #7 Card 8 pointer: PK vs PD rate-limiting clocks.
- #8 Card 8 pointer: duration-log dose relationship.

**Schematics (R/N): #2 → 1 / max 2**

- #2 Card 2 REDRAW: four-model action-site map.

**Images (I): none → 0**

- Image rights status: none. No textbook image insertion is allowed.

**Rejected candidates**: #4 blocking-dose pointer, #5 irreversible/target-consumption pointer, #9 meta-workflow schematic. All are educationally useful but fail the strict “measurable degradation if removed” test under the current budget.

---

# Figure Briefs — KEEP Items Only

## Figure 1 — Card 1 pointer

- **Source**: Gabrielsson & Weiner 5e, p.235, Fig 3.33 — direct response vs delayed hysteretic response; Rowland & Tozer 5e, p.235, Fig 8-2 — naproxen 500 mg oral concentration-response hysteresis.
- **Why this figure matters**: Fig 3.33 gives the structural contrast between one-to-one direct response and delayed response. Fig 8-2 gives the clinical hysteresis loop where the same naproxen concentration has different pain relief depending on the rising/falling phase.
- **When to look**: After reading Card 1.
- **Learner instruction**: First inspect the time plots, then inspect the concentration-response loop. Follow the time labels to verify that hysteresis is a time-ordered path, not scatter around a static curve.

## Figure 2 — Card 2 redraw brief

- **Title**: Four Turnover Models: Drug Action Site → Time-Constant Consequence
- **Visual objective**: Within 5 seconds, the learner should see whether the drug acts on input or output and why that changes `tss` behavior.
- **Core message**: Production-side models mainly change response extent, whereas loss-side models change both response extent and apparent response speed.
- **Elements to include**:
  - 2×2 grid: inhibition vs stimulation; production/input vs loss/output.
  - Central baseline relation: `R0 = kin/kout`.
  - Input-side labels: `kin × I(C)` and `kin × S(C)`.
  - Output-side labels: `kout × I(C)` and `kout × S(C)`.
  - Bottom strip: Models 1/3 → `tss` mostly governed by `kout`; Models 2/4 → concentration-dependent apparent `kout`.
- **Elements to exclude**:
  - Full ODEs already printed in Card 2.
  - Case-study parameter values.
  - Full response-time curves.
- **Suggested rendering**: Mermaid.
- **Caption**: Drug action site determines whether the drug changes response extent alone or also changes the apparent response clock.
- **Alt text**: A 2 by 2 map of the four turnover models showing input-side and output-side drug effects and their expected tss consequences.
- **Source relation**: Redrawn from textbook concept (no exact reproduction).

## Figure 3 — Card 4 pointer

- **Source**: Gabrielsson & Weiner 5e, p.246, Fig 3.40 — direct-effect vs turnover-model `Imax/Emax` meaning.
- **Why this figure matters**: The figure shows that the same parameter label does not represent the same observed vertical response distance across model classes. Without the visual, learners may compare `Emax` values across direct and turnover models as if they had identical semantics.
- **When to look**: After reading Card 4 Semantic lock.
- **Learner instruction**: Compare the vertical distance corresponding to observed `ΔR` with the model parameter label. Ask whether the parameter is an absolute response distance or a baseline-scaled multiplier.

## Figure 4 — Card 7 pointer

- **Source**: Gabrielsson & Weiner 5e, p.759, Fig 6.1 — PD6 observed response and model fit; p.763, Table 6.1 — turnover vs effect-compartment estimates.
- **Why this figure matters**: This is the apex discrimination example: the response-time fits can appear essentially equivalent while the causal interpretations remain different. Table 6.1 makes the `kout/ke0` near-equivalence concrete.
- **When to look**: After reading Card 7 Competing structures.
- **Learner instruction**: Inspect the response-time fit first, then inspect the `kout` and `ke0` estimates. Do not decide the mechanism from smoothness of fit alone.

## Figure 5 — Card 8 clock pointer

- **Source**: Rowland & Tozer 5e, p.243, Fig 8-11 — acenocoumarol vs phenprocoumon PK vs PD rate-limiting comparison.
- **Why this figure matters**: The same anticoagulant response system can be limited by different clocks depending on drug PK. This figure prevents the common error of assigning recovery only to the shared PD mechanism.
- **When to look**: Before applying the Card 8 duration formula.
- **Learner instruction**: Compare the recovery time-course for the short-PK and long-PK anticoagulant. Identify which curve is governed by system recovery and which is governed by drug persistence.

## Figure 6 — Card 8 duration pointer

- **Source**: Rowland & Tozer 5e, p.255, Fig 8-23 — duration vs log dose; p.256, Fig 8-24 — succinylcholine T50 vs log dose.
- **Why this figure matters**: These figures show the visual consequence of Eq 8-12: under PK-rate-limited conditions, dose doubling adds approximately one half-life of duration. Without this plot, the formula is easy to memorize but easy to misuse.
- **When to look**: After reading Card 8 Duration formula.
- **Learner instruction**: Trace how equal log-dose increments translate into equal time increments. Then re-check that the example is PK-rate-limited before generalizing the formula.

---

# Insertion Map (PATCH MODE)

The following map is authoritative for v2 → v2.1 splicing. Do not re-output or rewrite the Content Lock v2 body. Insert each marker block at the end of the specified concept card, on its own lines, before the next card or section heading.

| # | Reading order | Anchor copied verbatim from Content Lock v2 | Insert position | Marker block |
|---:|---|---|---|---|
| 1 | §2-1 | `## Card 1 — Turnover Model Foundation + Hysteresis Classification` | after this anchor card | See Marker Block 1 below |
| 2 | §2-2 | `## Card 2 — Four-Model Taxonomy: Inhibit/Stimulate × Production/Loss` | after this anchor card | See Marker Block 2 below |
| 3 | §2-4 | `## Card 4 — Imax/Emax Multiplier Semantics + Linear PK ≠ Linear PD` | after this anchor card | See Marker Block 3 below |
| 4 | §2-7 | `## Card 7 — Turnover vs Effect Compartment Discrimination Crisis` | after this anchor card | See Marker Block 4 below |
| 5 | §2-8A | `## Card 8 — PK Clock vs PD Clock + Duration Formula Boundary` | after this anchor card | See Marker Block 5 below |
| 6 | §2-8C | `## Card 8 — PK Clock vs PD Clock + Duration Formula Boundary` | after this anchor card, immediately after Marker Block 5 | See Marker Block 6 below |

## Marker Block 1

```text
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.235, Fig 3.33; Rowland & Tozer 5e, p.235, Fig 8-2
Why this matters: Fig 3.33 separates direct response from delayed hysteretic response. Fig 8-2 shows that the same naproxen concentration can map to different pain relief depending on the rising/falling phase.
When to look: after reading Card 1
Learner instruction: First inspect the time plots, then inspect the concentration-response loop. Follow the time labels to verify that hysteresis is a time-ordered path, not scatter around a static curve.
<!-- /FIGURE_POINTER -->
```

## Marker Block 2

```text
<!-- FIGURE_SCHEMATIC -->
Title: Four Turnover Models: Drug Action Site → Time-Constant Consequence
Mode: R
Visual objective: Within 5 seconds, show whether the drug acts on input or output and why that changes tss behavior.
Core message: Production-side models mainly change response extent, whereas loss-side models change both response extent and apparent response speed.
Elements to include: 2×2 grid of inhibition/stimulation by production/loss; central R0 = kin/kout baseline relation; input-side labels kin × I(C) and kin × S(C); output-side labels kout × I(C) and kout × S(C); bottom strip stating Models 1/3 → tss mostly kout, Models 2/4 → concentration-dependent apparent kout.
Elements to exclude: Full ODEs already printed in Card 2; case-study parameter values; full response-time curves.
Suggested rendering: Mermaid
Caption: Drug action site determines whether the drug changes response extent alone or also changes the apparent response clock.
Alt text: A 2 by 2 map of the four turnover models showing input-side and output-side drug effects and their expected tss consequences.
Source relation: Redrawn from textbook concept
<!-- /FIGURE_SCHEMATIC -->
```

## Marker Block 3

```text
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.246, Fig 3.40
Why this matters: The figure shows that the same parameter label does not represent the same observed vertical response distance across model classes. Without the visual, learners may compare Emax values across direct and turnover models as if they had identical semantics.
When to look: after reading Card 4 Semantic lock
Learner instruction: Compare the vertical distance corresponding to observed ΔR with the model parameter label. Ask whether the parameter is an absolute response distance or a baseline-scaled multiplier.
<!-- /FIGURE_POINTER -->
```

## Marker Block 4

```text
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.759, Fig 6.1; p.763, Table 6.1
Why this matters: This is the apex discrimination example: the response-time fits can appear essentially equivalent while the causal interpretations remain different. Table 6.1 makes the kout/ke0 near-equivalence concrete.
When to look: after reading Card 7 Competing structures
Learner instruction: Inspect the response-time fit first, then inspect the kout and ke0 estimates. Do not decide the mechanism from smoothness of fit alone.
<!-- /FIGURE_POINTER -->
```

## Marker Block 5

```text
<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.243, Fig 8-11
Why this matters: The same anticoagulant response system can be limited by different clocks depending on drug PK. This figure prevents the common error of assigning recovery only to the shared PD mechanism.
When to look: before applying the Card 8 duration formula
Learner instruction: Compare the recovery time-course for the short-PK and long-PK anticoagulant. Identify which curve is governed by system recovery and which is governed by drug persistence.
<!-- /FIGURE_POINTER -->
```

## Marker Block 6

```text
<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.255, Fig 8-23; p.256, Fig 8-24
Why this matters: These figures show the visual consequence of Eq 8-12: under PK-rate-limited conditions, dose doubling adds approximately one half-life of duration. Without this plot, the formula is easy to memorize but easy to misuse.
When to look: after reading Card 8 Duration formula
Learner instruction: Trace how equal log-dose increments translate into equal time increments. Then re-check that the example is PK-rate-limited before generalizing the formula.
<!-- /FIGURE_POINTER -->
```

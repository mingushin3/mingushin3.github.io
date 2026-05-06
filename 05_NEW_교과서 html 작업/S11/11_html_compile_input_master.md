# 11_HTML Compile Input Master

## Phase 4D Certification

| Certificate | Status | Basis |
|---|---|---|
| Learner-Standalone Certificate | PASS | PART A starts with navigation aid and then contains only learner-facing §1–§8 handout content; audit/process/compiler material is isolated in PART B. |
| Zero-Omission Certificate | PASS | Scope/Audit/Crucible/PDF high-impact items are present, compressed by Content Lock, or justifiably omitted; no HOLD_UNRESOLVED items remain. |
| Mastery-Uplift Certificate | PASS | Eight bounded, adjacent, source-labeled augmentation notes were inserted; no broad rewrite was performed. |
| Source-Boundary Certificate | PASS | Augmentations are labeled TEXTBOOK_DERIVED, AUDIT_DERIVED, CRUCIBLE_DERIVED, or EXPERT_INFERENCE and do not masquerade as textbook facts. |
| HTML-Readiness Certificate | PASS | PART B preserves figure, page-tag, marker-to-component, navigation-anchor, responsive/print, and forbidden-restoration rules for Phase 5. |

## Assembly Mode

PATCH MODE

Rationale: `11_Content Lock v2.1(2).md` is a figure marker insertion plan, not a full re-emitted canonical body. Therefore the learner-facing Content Lock v2 body was used as base, and six approved marker blocks were inserted at the specified card locations. The duplicate Card 8 anchor is intentional: Marker Blocks 5 and 6 both belong to the same Card 8 and were inserted sequentially at that card's end.


## Input Manifest

| File | Role | Authority level | Used for | Notes |
|---|---|---|---|---|
| `11_scope_lock(3).md` | scope boundary | A0 | source range, learner, image-right boundary, hard rules | Defines A-Critical mode and no copyrighted figure embedding. |
| `011_G_Indirect Response Turnover·DRT·Baseline(4).pdf` | PDF verification source | A1 | G&W source-page, equation, figure, case-study verification | Render/text cross-check used for G pp.110–111, 235–260, 272–275, 317–319, 742–784. |
| `011_T_Indirect Response Turnover·DRT·Baseline(4).pdf` | PDF verification source | A1 | R&T Ch.8 source-page, example, figure, duration formula verification | Render/text cross-check used for T pp.233–264. |
| `11_Audit_Report_v1(3).md` | audit guardrail | A2 | MUST_FIX/SHOULD_FIX corrections, forbidden restoration list, coverage audit | Controls naproxen, figure-number, minoxidil, Zooparc, direct-link, tss, and regulatory-claim corrections. |
| `11_Content Lock v2(2).md` | canonical body | A3 | learner body base | PART A uses the learner-facing §1–§8 body; process/adjudication tables are not learner-facing. |
| `11_Content Lock v2.1(2).md` | figure insertion source | A4 | PATCH MODE figure strategy, marker blocks, insertion map | Six approved marker blocks spliced into PART A. |
| `11_crucible_report_v1(1).md` | crucible guardrail | A5 | Grade A insight preservation and mastery augmentation candidates | Used only for adopted logic; not used as raw learner prose. |
| `붙여넣은 텍스트 (1)(81).txt` | Phase 4D assembly instruction | A7/process | certification, Part A/Part B contract, augmentation and micro-patch gates | Adapted from Session 05 to Session 11 naming. |
| `붙여넣은 마크다운(2)(60).md` | compiler instruction | A7 | Phase 5 rendering requirements | Preserved as essential compiler contract in PART B. |
| `S11_phase1_patch memo(2).md` | locked reference / deprecated draft review | A6 guardrail | confirms known Phase 1 defects and required corrections | Not used as raw learner body. |
| `11_step1_draft_v0(3).md` | deprecated source | A6 | regression check only | Not copied into PART A. |
| `11_Content_Lock_v1(3).md` | locked reference | lower than v2 | historical comparison only | Not used as body because v2 supersedes it. |

## PART A — Learner-Facing Complete Handout

## Learner Navigation Aid

### Obsidian-compatible YAML frontmatter to preserve in Phase 5

```yaml
title: "Session 11 — Indirect Response / Turnover / DRT / Baseline / Effect Compartment / Rate-Limiting / Duration"
source_universe:
  - "Gabrielsson & Weiner 5e: Ch.2 §2.6.7; Ch.3 §3.7–3.8, §3.10, §3.12; PD4/PD5/PD6/PD7/PD9"
  - "Rowland & Tozer 5e: Ch.8 pp.233–264"
learner: "PhD pharmacometrics student, entry–intermediate"
mode: "A-Critical"
image_rights: "None; render source textbook figures only as pointers or visually distinct redraws"
phase: "4D HTML compile input"
```

### How to use this handout

Read §1 once for the governing question, then study §2 as eight concept cards. For each card, first lock the equation or decision rule, then inspect the adjacent Mastery/Practice/Failure note, then use the approved figure pointer or redraw instruction where present. Do not treat the figure pointer blocks as images; they are Phase 5 instructions or textbook consultation prompts.

### Learning route

1. Turnover baseline and hysteresis classification.
2. Four-model production/loss taxonomy.
3. `tss` and peak-shift triage, with caveats.
4. Imax/Emax semantic lock and the linear-PK/nonlinear-PD warning.
5. Graphical initialization, blocking-dose logic, and DRT context.
6. Irreversible action and target-consumption recovery.
7. Turnover-versus-effect-compartment discrimination crisis.
8. PK clock versus PD clock, followed by the duration formula only when PK-rate-limited.

### Before you start / after you finish checklist

- Before: confirm that direct response, distribution delay, turnover delay, target consumption, and PK/PD rate-limiting are separate candidate explanations.
- During: for every delayed response, ask where the slow clock is located.
- After: answer the self-test without looking; if you can identify both model family and clock location, the session objective is met.

> **Copyright / figure-use note**  
> Source textbook figures are not embedded. `FIGURE_POINTER` blocks should render as text-only callouts, and the single `FIGURE_SCHEMATIC` block should be a visually distinct redraw rather than a reproduction of the textbook layout.


# §1 — Session Header & Roadmap

<!-- MASTER LENS -->
## Big Idea

대부분의 임상적으로 관찰되는 pharmacodynamic response는 plasma concentration과 완전히 동시에 움직이지 않는다. 그러나 모든 지연을 별도 모델로 다루는 것은 아니다. 지연이 **무시 가능할 정도로 짧으면 direct PK-PD link**로 충분하다. 반대로 지연이 관찰 가능하면 그 원인을 **distribution delay, turnover/system flux, target consumption, 또는 PK/PD rate-limiting clock** 중 하나로 분해해야 한다. [G pp.235–236; T pp.233–235, 239]

<!-- ANNOTATION --> 여기서 hysteresis는 “같은 농도에서도 시간 경로에 따라 response가 달라지는 현상”이다.

<!-- ANCHOR -->
## Conceptual navigation

이 세션은 다음 순서로 잠긴다.

1. `dR/dt = kin − kout·R`가 baseline과 time constant를 만든다. [G p.237]
2. 약물은 production 또는 loss 중 하나를 inhibit/stimulate한다. [G pp.237–245]
3. tss/peak shift는 작용 부위의 강력한 신호지만, PK rate-limiting과 limited dose range에 의해 가려질 수 있다. [G pp.247–251; G pp.778–783]
4. Effect compartment와 turnover model은 제한된 설계에서 거의 같은 curve를 낼 수 있다. 따라서 fit quality만으로 구조를 잠그면 안 된다. [G pp.758–763; T pp.244–246]
5. Response decline은 drug PK clock 또는 system PD clock 중 느린 쪽이 결정한다. 이 때문에 `tD` formula는 PK-rate-limited일 때만 사용한다. [T pp.243, 247–256]

<!-- RECAP -->
## Locked takeaway

이 장의 핵심은 “delayed response는 하나의 현상이 아니라 여러 원인의 공통 표면형”이라는 점이다. 모델링의 첫 질문은 “어떤 ODE가 curve를 잘 맞추는가?”가 아니라 “무엇이 시간을 rate-limit 하는가?”이다.

---

# §2 — Concept Anatomy Cards

## Card 1 — Turnover Model Foundation + Hysteresis Classification

<!-- MASTER LENS -->
### Big Idea

Turnover model의 최소 골격은 response가 **생산되는 속도**와 **사라지는 속도**의 차이다. Baseline은 독립적인 상수가 아니라 두 속도의 비율이다. Hysteresis loop는 이 system이 plasma concentration을 즉시 따라가지 못한다는 시각적 신호다. 이 말은 direct response를 부정한다는 뜻이 아니다. 먼저 **지연이 data resolution 안에서 보이는지**를 판단한다. [G pp.235–237; T pp.234–235, 239]

### A. Formal definition

$$\frac{dR}{dt}=k_{in}-k_{out}R \quad \text{[G Eq 3:74; G p.237]}$$

정상상태에서는:

$$R_0=\frac{k_{in}}{k_{out}} \quad \text{[G Eq 3:76; G p.237]}$$

- `R`: measured pharmacological response.
- `kin`: zero-order production rate, response·time⁻¹.
- `kout`: first-order loss rate, time⁻¹.
- `R0`: baseline response; basic model에서는 time-invariant로 둔다.

### B. Hysteresis classification

Hysteresis는 같은 concentration에서 rising phase와 falling phase response가 서로 다른 현상이다. [T pp.234–235]

| Pattern | Interpretation | Locked examples |
|---|---|---|
| Counterclockwise | Response lags behind concentration; distribution delay, downstream PD, or system flux | Naproxen 500 mg oral, dental pain, 1–8 h, Fig 8-2 [T pp.234–235]; ibuprofen 6 mg/kg oral, febrile children, Fig 8-9 [T pp.241–242] |
| No hysteresis / direct link | Effect-site equilibration and response generation are fast relative to observation | Midazolam 15 mg/kg oral in rat EEG, Fig 8-6 [T p.239] |
| Clockwise | Tolerance, feedback, active metabolite, or other additional dynamics | Scope note: not a core R&T worked example in this session; treat as later tolerance territory. |

### C. Reparameterization

For model fitting, `kin` and `kout`를 독립적으로 먼저 추정하지 말고 `R0`와 `kout`를 우선 추정한다:

$$k_{in}=R_0 k_{out}$$

$$\frac{dR}{dt}=k_{out}(R_0-R) \quad \text{[G Eq 3:103; G p.247]}$$

PD4 shows why this matters: a pool model can produce near-nonidentifiability when upstream and response turnover constants are estimated without sufficient design support. [G pp.742–752]

<!-- TRENCH -->
### Trench-level tip

If `kin` and `kout` show extreme correlation or the covariance step behaves like it is “stuck then drops,” recode as `R0 × kout`. This is not cosmetic. It changes the search geometry from two poorly separable rates to one baseline and one time constant.

### D. Context integration

Negative feedback adds a moderator `M`, so higher response can accelerate loss. The IgG example shows half-life shortening toward about 11 days at 30 mg·mL⁻¹ serum IgG, illustrating that `kout` can be system-state dependent rather than fixed. [G pp.110–111]

Baseline drift models are separate extensions; when disease progression or circadian drivers move `R0`, the basic constant-baseline turnover equation is no longer sufficient. [G pp.317–319]

<!-- RECAP -->
### Recap

Baseline is a ratio, hysteresis is a time-delay diagnostic, and reparameterization is the first practical defense against turnover-model nonidentifiability.

---

> **Practice Lens — [AUDIT_DERIVED]**  
> Treat “direct” versus “delayed” as a design-resolution decision before treating it as a model-family decision. If the delay is invisible at the sampling and response-resolution scale, a direct link can be defensible even though biology is never literally instantaneous.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.235, Fig 3.33; Rowland & Tozer 5e, p.235, Fig 8-2
Why this matters: Fig 3.33 separates direct response from delayed hysteretic response. Fig 8-2 shows that the same naproxen concentration can map to different pain relief depending on the rising/falling phase.
When to look: after reading Card 1
Learner instruction: First inspect the time plots, then inspect the concentration-response loop. Follow the time labels to verify that hysteresis is a time-ordered path, not scatter around a static curve.
<!-- /FIGURE_POINTER -->

## Card 2 — Four-Model Taxonomy: Inhibit/Stimulate × Production/Loss

<!-- MASTER LENS -->
### Big Idea

A reversible turnover response has only four canonical drug-action sites: inhibit production, inhibit loss, stimulate production, or stimulate loss. This table is not just classification. It is the minimal grammar for translating a biological mechanism into a NONMEM `$DES` block. [G pp.237–245; T pp.240–241]

### A. Drug functions

$$I(C)=1-\frac{I_{max}C^n}{IC_{50}^n+C^n}, \quad 0\le I_{max}\le 1 \quad \text{[G Eq 3:77; G p.237]}$$

$$S(C)=1+\frac{E_{max}C^n}{EC_{50}^n+C^n} \quad \text{[G Eq 3:78; G p.237]}$$

### B. Four models side-by-side

| Model | ODE | Drug action site | `tss` governor | `Rss` at constant `Css` | Maximal `ΔR` expression | Limit of `R` | Return-to-baseline behavior | Canonical example |
|---|---|---|---|---|---|---|---|---|
| 1. Inhibition of production | $\frac{dR}{dt}=k_{in}I(C)-k_{out}R$ [G pp.238–239] | Blocks input / biosynthesis | `kout`, dose-independent if PK fast | $R_{ss}=R_0I(C_{ss})$ | $\Delta R=R_0I_{max}$ [G p.239] | Down toward 0 if full inhibition | Recovery governed by `kout` after drug disappears | Warfarin inhibits vitamin K cycle / prothrombin complex [G PD4 pp.742–752; T pp.242–247] |
| 2. Inhibition of loss | $\frac{dR}{dt}=k_{in}-k_{out}RI(C)$ [G pp.240–241] | Blocks output / removal | effective `kout·I(C)`, dose-dependent | $R_{ss}=R_0/I(C_{ss})$ | $\Delta R=R_0 I_{max}/(1-I_{max})$ [G p.241] | Can rise above baseline | Return depends on restored loss process | Furosemide-type retention example [G p.238] |
| 3. Stimulation of production | $\frac{dR}{dt}=k_{in}S(C)-k_{out}R$ [G pp.242–243] | Stimulates input | `kout`, dose-independent if PK fast | $R_{ss}=R_0S(C_{ss})$ | $\Delta R=R_0E_{max}$ [G p.243] | Rises to multiplier of baseline | Recovery governed by `kout` | Erythropoietin stimulates RBC production [G p.238] |
| 4. Stimulation of loss | $\frac{dR}{dt}=k_{in}-k_{out}RS(C)$ [G pp.244–245] | Stimulates output | effective `kout·S(C)`, dose-dependent | $R_{ss}=R_0/S(C_{ss})$ | $\Delta R=R_0E_{max}/(1+E_{max})$ [G p.245] | Falls below baseline | Faster return at high stimulation | CB1 inverse agonist / energy expenditure example [G p.238]; PD7 compound C [G pp.764–769] |

### C. Structural necessity

<!-- ANNOTATION --> 이 네 모델의 차이는 “response가 올라가느냐 내려가느냐”보다 “drug가 input을 바꾸느냐 output을 바꾸느냐”에 있다. 따라서 다음 Card 3의 `tss` 판별도 이 input/output 구분에서 나온다.

Models 1 and 3 alter the zero-order input term; therefore the time constant remains `1/kout`. Models 2 and 4 alter the first-order loss term; therefore the apparent time constant changes with concentration. This is why `tss` behavior can identify action site, but only when PK is not the slower clock.

<!-- TRENCH -->
### Trench-level tip

Do not infer the model from response direction alone. A downward response can arise from Model 1 or Model 4. You need the time pattern: production-side models mainly change extent; loss-side models change both extent and apparent speed.

<!-- RECAP -->
### Recap

The four-model table is the session’s structural lock. Every later claim — tss, peak shift, initial estimates, and model discrimination — is a consequence of whether the drug changes input or output.

---

> **Mastery Note — [CRUCIBLE_DERIVED]**  
> The taxonomy is not a naming exercise; it is an action-site assignment. Once the drug is placed on input or output, the expected `tss` behavior and the interpretation of `kout` change.

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

## Card 3 — tss / Peak-Shift Mechanism Discrimination

<!-- MASTER LENS -->
### Big Idea

`tss` and peak-shift are high-value diagnostic signals, not verdicts. Models 1 and 3 tend to show dose-independent time to PD steady state because the loss rate is unchanged. Models 2 and 4 can show dose-dependent `tss` because the drug changes the loss term. 이 규칙은 강하지만 절대 판정은 아니다. PK가 느리거나, dose range가 좁거나, response가 noisy하거나, mechanism에 unmodeled nonlinearity가 있으면 깨질 수 있다. [G pp.247–251; G pp.778–783; T p.243]

### A. Core inference

| Observation | First mechanistic hypothesis | Caveat |
|---|---|---|
| Similar `tss` across doses | Production-side effect: Model 1 or 3 | Could be masked by PK rate-limiting or limited data resolution. |
| Shorter or longer `tss` with dose | Loss-side effect: Model 2 or 4 | Requires PK to be faster than PD clock. |
| No peak shift with increasing dose | Does not prove effect compartment | PD9 simulations explicitly warn against this overinterpretation. [G pp.778–783] |

<!-- TRENCH -->
### Trench-level tip — Mirror-slope misread

Do not estimate `kout` from every early response slope as if all models were Model 1/3. For Models 2/4, early or apparent slope can be dose-scaled by `I(C)` or `S(C)`. A dose-dependent `kout` estimate is often not biology; it is a misspecified structural readout. [G p.251]

### B. Practical decision rule

Use `tss/peak-shift` as **triage**, then require at least one additional support:

- broad enough dose range to expose nonlinear `H(C)` behavior;
- repeated-dose or washout data;
- credible mechanistic prior about production vs loss;
- PK clock faster than PD clock;
- model comparison that includes effect compartment alternatives.

<!-- RECAP -->
### Recap

`tss` tells you where to look, not where to stop. The safest phrase is: “The `tss` pattern supports a production-side/loss-side mechanism under the observed PK-rate conditions.”

---

> **Failure Mode — [AUDIT_DERIVED]**  
> The common overreach is to treat `tss` or peak shift as a proof of mechanism. Use it as a strong triage signal, then test whether PK rate-limiting, limited dose range, or nonlinear drug function could mask the expected pattern.

## Card 4 — Imax/Emax Multiplier Semantics + Linear PK ≠ Linear PD

<!-- MASTER LENS -->
### Big Idea

`Emax` is not a universal unit. In a direct Emax model it is often an absolute distance from baseline. In a turnover model it is a multiplier on a system whose baseline already contains `kin/kout`. 이 의미를 혼동하면 in vitro potency, clinical EC50, and model-derived effect size가 서로 비교 가능한 것처럼 보인다. 실제로는 그렇지 않다. [G p.246]

### A. Semantic lock

| Model form | Parameter meaning | Unit / interpretation |
|---|---|---|
| Direct additive Emax | $E=E_0+\frac{E_{max}C^n}{EC_{50}^n+C^n}$ | `Emax` has response units; it is an absolute distance. |
| Direct reparameterized multiplier | $E=E_0(1+\frac{E_{max}C^n}{EC_{50}^n+C^n})$ | `Emax` is dimensionless multiplier of baseline. |
| Turnover Model 3 | $R_{ss}=R_0(1+\frac{E_{max}C^n}{EC_{50}^n+C^n})$ | `Emax` is a multiplier acting through system turnover. |

### B. Linear PK does not imply linear PD

Methylprednisolone is the locked example: exact i.v. phosphate-prodrug dose series is 16 / 31 / 63 / 125 / 250 / 500 / 1000 mg. Plasma AUC increases approximately in proportion to dose, but lymphocyte response does not increase proportionally; high doses approach a PD plateau. [T pp.256–258]

<!-- TRENCH -->
### Trench-level tip

Before writing “dose-proportional exposure supports dose-proportional response,” force the response through the Hill-curve lens. If the proposed dose range sits in Region 3, more exposure mainly extends plateau duration or toxicity risk; it does not double response.

<!-- RECAP -->
### Recap

Always translate effect parameters into `ΔR/R0` before comparing models, studies, or compounds.

---

> **Mastery Note — [CRUCIBLE_DERIVED]**  
> When comparing across models, compare what is observable on the response scale before comparing parameter labels. In turnover models, the same label can encode a baseline-scaled system perturbation rather than a direct vertical response distance.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.246, Fig 3.40
Why this matters: The figure shows that the same parameter label does not represent the same observed vertical response distance across model classes. Without the visual, learners may compare Emax values across direct and turnover models as if they had identical semantics.
When to look: after reading Card 4 Semantic lock
Learner instruction: Compare the vertical distance corresponding to observed ΔR with the model parameter label. Ask whether the parameter is an absolute response distance or a baseline-scaled multiplier.
<!-- /FIGURE_POINTER -->

## Card 5 — Graphical Initial Parameter Estimation + Blocking Dose / DRT

<!-- MASTER LENS -->
### Big Idea

Initial estimates are not a nuisance before “real modeling.” In turnover PD, graphical estimation is the first mechanistic check. NONMEM이 탐색을 시작하기 전에 baseline, time constant, potency, and maximal effect를 먼저 분리해 두는 단계다. [G pp.247–251]

### A. Minimal graphical workflow

1. Estimate `R0` from pre-dose or vehicle baseline.
2. Estimate `kout` from terminal recovery, blocked-synthesis decay, or log-linear return.
3. Compute `kin = R0·kout`.
4. Use steady-state or peak response at 2–3 dose levels to initialize `IC50/EC50` and `Imax/Emax`.
5. Only then run nonlinear mixed-effects estimation.

### B. Blocking-dose analogue

Warfarin blocking-dose analysis shows the clinical equivalent of direct `kout` extraction. When synthesis is nearly fully blocked, prothrombin complex activity follows:

$$\frac{dA}{dt}=-k_tA \quad \text{[T Eq 8-6; T pp.244–246]}$$

For nonblocking intervals, synthesis rate can be reconstructed:

$$R_{syn}=\frac{A_2-A_1}{\Delta t}+k_t\frac{A_1+A_2}{2} \quad \text{[T Eq 8-7; T p.247]}$$

This converts a hysteretic response-time record into an inhibition-vs-concentration relationship. [T pp.244–247]

### C. DRT context

Dose-Response-Time analysis can infer baseline, slope, potency, and maximal effect even when concentration data are absent. 그러나 full PK/PD modeling보다 거친 inverse problem이다. Exposure가 있으면 measured exposure를 대체하지 말고, fallback 또는 teaching bridge로 둔다. [G pp.272–275]

<!-- TRENCH -->
### Trench-level tip

A model that requires absurd starting values usually means the graphical stage was skipped or the wrong clock was used. Fix the starting biology before expanding random effects.

<!-- RECAP -->
### Recap

Manual initial estimates are not old-fashioned; they are the first identifiability audit.

---

> **Practice Lens — [CRUCIBLE_DERIVED]**  
> Manual initial estimates are not a nostalgic pre-NONMEM ritual. They are a mechanism audit: if the slope, baseline, or blocking-dose logic cannot roughly support the fitted parameters, optimization is likely solving the wrong problem cleanly.

## Card 6 — Irreversible Drug Action + Target Consumption

<!-- MASTER LENS -->
### Big Idea

Reversible turnover models regain baseline because the system continues to produce and remove response. Irreversible action is different. Drug exposure permanently removes response units, targets, or cells during the exposure window. 따라서 drug may disappear while the biological consequence persists. [G pp.256–260; T pp.251–252]

### A. Core irreversible equation

$$\frac{dR}{dt}=-K_{kill}\,C\,R \quad \text{[G Eq 3:110; G p.257]}$$

Integrated survival:

$$SF=\exp(-K_{kill}\cdot AUC) \quad \text{[G Eq 3:112; G p.257]}$$

`Kkill` is a second-order drug-action constant; it is not the first-order PK elimination constant.

> [확인 필요] Source notation uses `K` in more than one context across irreversible kill and PK elimination. In this locked handout, `Kkill/kk` means pharmacodynamic killing; `Kelim` means PK elimination.

### B. Target consumption examples

- Aspirin 650 mg oral: plasma half-life is short, but thromboxane B₂ inhibition persists for days because platelet function depends on target replacement. [T p.251]
- Omeprazole 40 mg oral: plasma half-life is <1 h, but acid-output inhibition persists for days due to proton-pump binding/regeneration dynamics. [T p.252]
- Paclitaxel i.v.: plasma decline occurs long before leukocyte recovery, which may take about 3 weeks; use Fig 8-22 context, not Fig 8-19. [T pp.253–254]

### C. Cell growth/kill context

When cells replicate, irreversible kill must be embedded in growth dynamics. Gabrielsson’s cell-growth/kill framework adds logistic or capacity-limited growth and second-order kill; `Bmax≈30,000 CFU` is a context anchor, not a separate MUST card. [G pp.258–260]

<!-- RECAP -->
### Recap

If drug equals zero and biological loss still continues by system turnover, use reversible turnover. If exposure has consumed target/cells and recovery depends on replacement, consider irreversible/target-consumption logic.

---

> **Failure Mode — [TEXTBOOK_DERIVED]**  
> Do not equate drug disappearance with effect disappearance. Once recovery depends on target replacement, cell regrowth, or system repair, plasma PK no longer supplies the recovery clock by itself.

## Card 7 — Turnover vs Effect Compartment Discrimination Crisis

<!-- MASTER LENS -->
### Big Idea — Apex Concept

A turnover model and an effect-compartment model can produce nearly identical response-time curves under a limited single-dose design. The difference is not curve smoothness. The difference is the causal claim: **Is the delay because drug arrives slowly at the <!-- ANNOTATION --> biophase(← 실제 작용부위 주변 농도 공간), or because the response system itself turns over slowly?** [G pp.758–763; T pp.244–246]

### A. Competing structures

Turnover example:

$$\frac{dR}{dt}=k_{in}S(C)-k_{out}R$$

Effect compartment example:

$$\frac{dC_e}{dt}=k_{e0}(C-C_e), \quad R=f(C_e) \quad \text{[T pp.244–246]}$$

PD6 locks the crisis: turnover and effect-compartment fits can show essentially the same residual behavior, with `kout` and `ke0` converging to similar values around 5.6 h⁻¹. [G pp.758–763]

### B. How to discriminate

| Evidence | Supports turnover | Supports effect compartment |
|---|---|---|
| Response variable | Endogenous mediator, biomarker, cell count, clotting factor, gastric pH | Drug distribution to effect site is the plausible delay |
| Dose range | Broad enough to expose nonlinear turnover-generated behavior | Hysteresis collapses with stable `EC50` and plausible `ke0` |
| Perturbation | Repeated dosing/washout reveals system recovery time | Biophase equilibration explains onset and offset |
| Mechanistic prior | Known synthesis/loss process | Known tissue distribution delay |

<!-- CONFUSION -->
### Critical Blow — source-grounded core + labeled practical extrapolation

**교과서 기반**: fit quality alone cannot prove that a delay is distributional or turnover-driven. Limited designs can make both structures appear equivalent. [G pp.758–763; T pp.244–246]

**[교과서 외 실무 해석]**: In a regulatory modeling report, this means the model-selection paragraph should include alternative structure evaluation, mechanistic justification, and sensitivity analysis. Avoid unsupported phrases such as “NDA deficiency” unless clearly labeled as practical extrapolation.

<!-- TRENCH -->
### Trench-level tip

If `EC50` changes with dose when fitting an effect-compartment model to a turnover-generated system, the drug parameter is absorbing system dynamics. That is a structural warning, not a potency finding.

<!-- RECAP -->
### Recap

Effect compartment says “drug is late.” Turnover says “biology is slow.” The curve alone may not tell you which is true.

---

> **Practice Lens — [EXPERT_INFERENCE]**  
> When two causal structures fit equally well, the disciplined move is to document the biological assumption and identify the design feature that would separate them. For this card, model defensibility comes from mechanism plus design support, not from curve smoothness alone.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.759, Fig 6.1; p.763, Table 6.1
Why this matters: This is the apex discrimination example: the response-time fits can appear essentially equivalent while the causal interpretations remain different. Table 6.1 makes the kout/ke0 near-equivalence concrete.
When to look: after reading Card 7 Competing structures
Learner instruction: Inspect the response-time fit first, then inspect the kout and ke0 estimates. Do not decide the mechanism from smoothness of fit alone.
<!-- /FIGURE_POINTER -->

## Card 8 — PK Clock vs PD Clock + Duration Formula Boundary

<!-- MASTER LENS -->
### Big Idea

Two clocks run after dosing: the drug PK clock and the system PD clock. The slower clock controls the observed decline of response. 따라서 drug elimination에 근거한 duration formula는 response가 PK-rate-limited이고 exposure-response relationship이 사실상 고정되어 있을 때만 유효하다. [T pp.243, 247–256]

### A. Clock discrimination

| Situation | Slower clock | Locked examples | Modeling consequence |
|---|---|---|---|
| PK rate-limited | Drug elimination/distribution | Succinylcholine 0.5/1/2/4 mg·kg⁻¹ i.v., muscle paralysis; minoxidil single oral 25 mg, MAP lowering [T pp.249–256] | `tD` formula can be meaningful. |
| PD rate-limited | System turnover/target regeneration | Acenocoumarol vs clotting factor turnover; aspirin platelet/TxB₂; omeprazole proton-pump recovery; paclitaxel leukocyte recovery [T pp.243, 251–254] | Turnover/target-consumption model needed; PK `k` alone cannot predict duration. |
| Drug PK slower than system | PK dominates even for indirect mechanism | Phenprocoumon half-life ~5 days vs clotting-factor dynamics [T p.243] | Anticoagulant effect recovery follows drug persistence. |

### B. Region 1/2/3 and linear decline

In the middle portion of a graded E-logC relationship, response declines approximately linearly with time after a single dose:

$$Response=E(0)-mkt \quad \text{[T Eq 8-9; T pp.247–249]}$$

This is a Region 2 statement. 즉, response가 Hill curve의 중간 구간에 있을 때의 근사다. Region 3 is plateau-like; Region 1 returns toward first-order-looking behavior. Succinylcholine’s roughly 22%/min decline illustrates this middle-region linearity. [T pp.249–250]

### C. Duration formula

<!-- ANNOTATION --> 따라서 clock discrimination이 먼저 끝나야 한다. For a PK-rate-limited response with fixed exposure-response relationship:

$$t_D=\frac{1}{k}\ln\left(\frac{Dose}{C_{min}V}\right)=\frac{1}{k}\ln\left(\frac{Dose}{A_{min}}\right) \quad \text{[T Eq 8-12; T pp.254–255]}$$

Dose doubling adds one drug half-life of duration:

$$\Delta t_D=\frac{\ln 2}{k}=t_{1/2}$$

This is why succinylcholine duration increases approximately one effective half-life per dose doubling. [T pp.255–256]

<!-- TRENCH -->
### Wrong-clock warning

Do not apply Eq 8-12 to warfarin, aspirin, omeprazole, or paclitaxel-like PD-rate-limited situations. If the system clock is slower than drug disappearance, the formula returns a mathematically neat but biologically wrong duration.

### D. Exposure-response disconnect context

Rosuvastatin OATP1B1 shows that systemic plasma exposure can change substantially while site-of-action response changes modestly; this is context, not a separate turnover model. [T pp.258–259]

<!-- RECAP -->
### Recap

Before computing duration, ask: “Which clock is slow?” If the answer is PD, stop using PK `k` as the duration driver.

---

> **Failure Mode — [AUDIT_DERIVED]**  
> The duration formula becomes dangerous when it is applied before clock selection. Always decide whether PK or PD is rate-limiting first; only then does the logarithmic dose-duration relation have the intended meaning.

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.243, Fig 8-11
Why this matters: The same anticoagulant response system can be limited by different clocks depending on drug PK. This figure prevents the common error of assigning recovery only to the shared PD mechanism.
When to look: before applying the Card 8 duration formula
Learner instruction: Compare the recovery time-course for the short-PK and long-PK anticoagulant. Identify which curve is governed by system recovery and which is governed by drug persistence.
<!-- /FIGURE_POINTER -->

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.255, Fig 8-23; p.256, Fig 8-24
Why this matters: These figures show the visual consequence of Eq 8-12: under PK-rate-limited conditions, dose doubling adds approximately one half-life of duration. Without this plot, the formula is easy to memorize but easy to misuse.
When to look: after reading Card 8 Duration formula
Learner instruction: Trace how equal log-dose increments translate into equal time increments. Then re-check that the example is PK-rate-limited before generalizing the formula.
<!-- /FIGURE_POINTER -->

# §5 — Confusion Pair Dissection

<!-- CONFUSION -->
## §5-1. Model 1 vs Model 2 — Inhibition of Production vs Inhibition of Loss

| Dimension | Model 1: inhibit production | Model 2: inhibit loss |
|---|---|---|
| ODE | $dR/dt=k_{in}I(C)-k_{out}R$ [G pp.238–239] | $dR/dt=k_{in}-k_{out}RI(C)$ [G pp.240–241] |
| Direction | Response decreases | Response increases |
| `tss` | Mainly `kout`, dose-independent if PK fast | effective `kout·I(C)`, dose-dependent |
| Common error | Calling any downward response “inhibition” without specifying production vs loss | Treating an increasing response as production stimulation without checking loss inhibition |
| Memory lock | Drug closes the faucet. | Drug blocks the drain. |

<!-- CONFUSION -->
## §5-2. Direct Emax vs Turnover Imax/Emax

| Dimension | Direct model | Turnover model |
|---|---|---|
| Parameter surface | Immediate concentration-response | System response after production/loss dynamics |
| `Emax` meaning | Absolute response distance or baseline multiplier depending on parameterization | Multiplier on `kin/kout` baseline |
| Safe comparison | Compare observed response units directly if same scale | Compare `ΔR/R0` and mechanism-specific `IC50/EC50` |
| Key example | Midazolam direct link [T p.239] | PD5/PD7 turnover parameter tables [G pp.753–769] |

<!-- CONFUSION -->
## §5-3. Reversible Turnover vs Irreversible Kill / Target Consumption

| Dimension | Reversible turnover | Irreversible / target consumption |
|---|---|---|
| Drug-off behavior | System returns by `kin/kout` | Effect may persist until target/cell replacement |
| Core equation | $dR/dt=k_{in}-k_{out}R$ | $dR/dt=-K_{kill}CR$ |
| Example | Warfarin/clotting factor turnover [T pp.242–247] | Aspirin/TxB₂, omeprazole/proton pump [T pp.251–252] |
| Error | Assuming delayed recovery implies irreversible action | Assuming drug disappearance means effect disappearance |

<!-- CONFUSION -->
## §5-4. Turnover Model vs Effect Compartment — Critical Pair

| Dimension | Turnover model | Effect compartment |
|---|---|---|
| Delay belongs to | Response biology | Drug distribution to biophase |
| Parameter | `kin`, `kout`, `R0`, `IC50/EC50` | `ke0`, `Ce`, direct response parameters |
| Best prior | Endogenous mediator/cell/biomarker turnover | Tissue equilibration delay |
| Trap | Fit can mimic link model | Fit can absorb system turnover into `ke0` |
| Locked interpretation | Use mechanistic prior + design support, not fit alone. | Same. |

**[교과서 외 실무 해석]** In submission-style writing, this is where alternative model comparison and mechanistic justification belong; do not present the selected structure as self-evident if the design cannot discriminate it.

<!-- CONFUSION -->
## §5-5. PK Rate-Limited vs PD Rate-Limited Decline

| Dimension | PK-rate-limited | PD-rate-limited |
|---|---|---|
| Slow clock | Drug concentration decline | System recovery/target replacement |
| Formula | `tD` formula can apply | `tD` formula using PK `k` is wrong-clock use |
| Example | Succinylcholine; minoxidil [T pp.249–256] | Acenocoumarol, aspirin, omeprazole, paclitaxel [T pp.243, 251–254] |
| Clinical failure | Overlooking clearance effect on duration | Overpredicting duration change from exposure alone |

<!-- RECAP -->
## §5 Recap

Most errors in this session are not algebra errors. They are **clock-location errors**. 즉, wrong input/output site, wrong source of delay, wrong meaning of `Emax`, or wrong rate-limiting process를 잘못 지정한 오류다.

---

# §7 — Self-Test: Active Recall Module

<!-- SELF-TEST -->
## Q1 [Recall] Model 1 ODE and steady state

Write Model 1 ODE and derive `Rss` under constant `Css`.

**Answer**  
$$\frac{dR}{dt}=k_{in}I(C)-k_{out}R$$  
At steady state: $R_{ss}=R_0I(C_{ss})$. [G pp.238–239]

<!-- SELF-TEST -->
## Q2 [Recall] Which models show dose-independent `tss`?

**Answer**  
Models 1 and 3, because the first-order loss term remains `kout·R`. Models 2 and 4 can show dose-dependent `tss` because drug modifies the loss term. Caveat: this assumes PK is not the slower clock. [G pp.247–251; T p.243]

<!-- SELF-TEST -->
## Q3 [Application] Interpret no peak shift in PD9

No peak shift appears as dose increases. Does this prove an effect compartment model?

**Answer**  
No. PD9 explicitly warns that lack of peak shift does not necessarily imply a link/effect-compartment model; dose range, nonlinear drug function, and system kinetics must be considered. [G pp.778–783]

<!-- SELF-TEST -->
## Q4 [Application] PD9 Zooparc® dose correction

What observed dose levels should be locked for Zooparc® repeated-dose data, and how should 25 mg/day be described?

**Answer**  
Observed repeated-dose figures use 2.5 mg and 5 mg. The 25 mg/day statement is a projection/larger-study discussion, not the observed dose context. [G pp.778–783]

<!-- SELF-TEST -->
## Q5 [Application] Naproxen correction

Correct the erroneous phrase “naproxen 250 mg, Fig 8-3.”

**Answer**  
Naproxen 500 mg oral, dental pain model, 1–8 h sampling, counterclockwise hysteresis, Fig 8-2. Fig 8-3 is a downstream pharmacodynamic schematic, not the naproxen figure. [T pp.234–236]

<!-- SELF-TEST -->
## Q6 [Application] Wrong-clock `tD`

Why is Eq 8-12 inappropriate for aspirin duration?

**Answer**  
Aspirin’s plasma exposure disappears quickly, but thromboxane B₂ inhibition persists because target/platelet function recovery is slower. Duration is PD/target-replacement limited, not PK-rate-limited. [T p.251]

<!-- SELF-TEST -->
## Q7 [Application] Turnover vs effect compartment

A single-dose dataset fits both turnover and effect-compartment models equally well. What evidence should decide between them?

**Answer**  
Mechanistic prior about the response variable, broader dose range, repeated dosing/washout, perturbation of PK clock, and whether `EC50/ke0` remains biologically plausible. Fit quality alone is insufficient. [G pp.758–763; T pp.244–246]

<!-- SELF-TEST -->
## Q8 [Application] Linear PK ≠ linear PD

Methylprednisolone AUC is dose proportional from 16 to 1000 mg. Why does that not justify dose-proportional lymphocyte response?

**Answer**  
The response can enter the plateau region of the exposure-response curve; R&T’s lymphocyte example shows little added PD response at high doses despite dose-proportional PK. [T pp.256–258]

<!-- SELF-TEST -->
## Q9 [Boss dilemma]

A sponsor proposes: “Because phenprocoumon and acenocoumarol share the same anticoagulant mechanism, their response recovery should be governed by the same PD turnover half-life.” Accept or reject?

**Answer**  
Reject. The same mechanism does not imply the same rate-limiting clock. Acenocoumarol has shorter PK half-life and can become PD-clock limited; phenprocoumon has much longer PK persistence and can become PK-clock limited. [T p.243]

<!-- RECAP -->
## §7 Recap

A correct answer must identify both **model family** and **clock location**. A mathematically correct formula used on the wrong clock is still wrong.

---

# §8 — Meta-Frame & Big Picture

## A. Positioning in the pharmacometrics architecture

This session sits between direct exposure-response modeling and advanced disease/response systems. 여기서부터 modeler는 curve fitting을 넘어 원인 분리를 해야 한다. It is the first point where the modeler must separate:

- drug parameters from system parameters;
- distribution delay from biological turnover delay;
- exposure extent from response duration;
- model fit from model meaning.

It unlocks later work on transit compartments, tolerance/moderator models, disease progression, PopPK/PD with IIV on system parameters, and clinical trial sampling design.

## B. Failure modes if this session is weak

| Failure mode | Practical consequence |
|---|---|
| Treating every delay as effect compartment | `ke0` absorbs biology; dosing simulations fail under new regimens. |
| Treating tss as deterministic model proof | Mechanistic claim overstates design support. |
| Confusing `Emax` units | Cross-study or in vitro/clinical potency comparisons become misleading. |
| Applying `tD` to PD-rate-limited drugs | Duration predictions become biologically meaningless. |
| Ignoring baseline drift | Disease progression or circadian trends are misread as drug effect. |

## C. Professional moat

A 30-year pharmacometrics reviewer does not ask first whether the curve is smooth. They ask:

1. Is the delay visible relative to sampling resolution?
2. Does the delay belong to drug distribution or response turnover?
3. Which clock is slower: PK or PD?
4. Are `R0`, `kout`, and potency separately identifiable?
5. Would the selected structure survive a different dose range or dosing interval?

<!-- RECAP -->
## Final locked summary

Indirect response modeling is not “adding a delay.” It is assigning delay to the correct causal clock. 따라서 locked workflow is:

**hysteresis direction → four-model action site → tss/peak-shift triage → initial-parameter audit → turnover-vs-link discrimination → PK/PD clock selection → duration formula only if PK-rate-limited.**


## PART B — Compiler-Only Appendix

This appendix is not learner-facing. It exists only to protect Phase 5 rendering fidelity.

### B1. Compilation Contract

- PART A is the only learner-facing body.
- Phase 5 must render PART A without altering content.
- PART B is instruction/guardrail only.
- Do not restore deprecated material.
- Do not add new scientific content.
- Do not render PART B as learner content unless explicitly requested.

### B2. Figure Rendering Instructions

- Preserve P/R/N/I decisions from the Figure Strategy / Insertion Map.
- If Image rights = None: do not embed copyrighted textbook images. Render `FIGURE_POINTER` as text-only callout.
- `FIGURE_SCHEMATIC` must be a visually distinct redraw; do not reproduce textbook layout, color palette, or label placement.
- Do not propose new figures.
- Do not generate Mermaid/SVG in Phase 4D; Phase 5 performs rendering.

#### Approved Figure Strategy / Insertion Map

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

### B3. Page Tag Rendering Rules

- Preserve all `[p.XX]`, `[pp.XX–YY]`, `[pp.XX, YY]`, `[p.확인 필요]`, `[G ...]`, and `[T ...]` source tags as visible traceability text.
- Render page tags visibly in HTML.
- Do not fabricate, delete, renumber, or relocate page tags.
- `[p.확인 필요]` remains visible unless already resolved by Audit/Content Lock.
- Do not apply source-page regex inside code blocks or inside figure marker blocks.

### B4. HTML Compiler Requirements

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

Regression-prevention items for Session 11:

- Do not restore `naproxen 250 mg` or `Fig 8-3` as the naproxen anchor; the locked correction is naproxen 500 mg oral, dental pain, 1–8 h, counterclockwise hysteresis, Fig 8-2.
- Do not restore `ibuprofen Fig 8-4`; the locked figure is Fig 8-9.
- Do not restore `paclitaxel Fig 8-19`; Fig 8-19 is minoxidil and paclitaxel is Fig 8-22.
- Do not frame the minoxidil figure as topical; the locked example is single oral 25 mg with MAP-lowering context.
- Do not restore Zooparc® `5 mg or 25 mg q24h` as observed repeated-dose data; observed repeated-dose figures are 2.5 mg and 5 mg, while 25 mg/day is a projection/larger-study statement.
- Do not present NDA/IND/FDA reviewer/deficiency-letter wording as textbook-derived. Keep any such language explicitly labeled `[교과서 외 실무 해석]` or omit it.
- Do not restore an absolute “all measurable responses are delayed” claim without the direct-response caveat.
- Do not treat `tss` or peak shift as deterministic proof of mechanism; preserve the data-resolution, dose-range, PK-rate-limiting, and mechanistic-prior caveats.
- Do not round methylprednisolone 31/63 mg to 32/64 mg.
- Do not collapse `Kkill/kk` and `Kelim` in learner rendering; preserve the notation-disambiguation warning.
- Do not expand rosuvastatin, ranitidine, propranolol, or study-problem material beyond the locked CONTEXT/optional role.
- Do not add unapproved code blocks, new figures, new clinical examples, new numerical values, or new page tags.


### B6. Crucible Guardrails

- Crucible is not a raw content source at this stage.
- Preserve only already-adopted or explicitly allowed Grade A logic.
- Do not reintroduce omitted or rejected Crucible items.
- Do not convert speculative insight into textbook-derived fact.
- Grade A concepts are preserved only where Content Lock adopted them: tss first-order analogue blindness, ΔR/Emax semantic overload, Region 2/3 duration boundary, PK clock vs PD clock non-identifiability, single-dose duration-to-dose extension, hysteresis direction diagnosis, wrong-clock `tD`, and linear PK ≠ linear PD.

### B7. Deprecated and Forbidden Restorations

- Step 1 Draft v0 is deprecated.
- Do not restore rejected overclaims, unsupported numbers, unsupported regulatory claims, source-unsupported examples, unapproved code, or unapproved figures.
- Do not use Step 1 Draft v0 as learner-body source except through the Micro-Patch Gate.
- Do not restore Phase 1 card overgrowth; Cards 8–9 remain merged in Card 8.
- Do not restore rejected figure candidates #4, #5, or #9 from v2.1.


### B8. PATCH MODE Splice Verification Table

| Marker # | Anchor text | Anchor found? | Match count | Inserted? | Final location (§ + card) |
|---:|---|---|---:|---|---|
| 1 | `## Card 1 — Turnover Model Foundation + Hysteresis Classification` | YES | 1 | YES | Card 1 — Turnover Model Foundation + Hysteresis Classification |
| 2 | `## Card 2 — Four-Model Taxonomy: Inhibit/Stimulate × Production/Loss` | YES | 1 | YES | Card 2 — Four-Model Taxonomy: Inhibit/Stimulate × Production/Loss |
| 3 | `## Card 4 — Imax/Emax Multiplier Semantics + Linear PK ≠ Linear PD` | YES | 1 | YES | Card 4 — Imax/Emax Multiplier Semantics + Linear PK ≠ Linear PD |
| 4 | `## Card 7 — Turnover vs Effect Compartment Discrimination Crisis` | YES | 1 | YES | Card 7 — Turnover vs Effect Compartment Discrimination Crisis |
| 5 | `## Card 8 — PK Clock vs PD Clock + Duration Formula Boundary` | YES | 1 | YES | Card 8 — PK Clock vs PD Clock + Duration Formula Boundary |
| 6 | `## Card 8 — PK Clock vs PD Clock + Duration Formula Boundary` | YES | 1 | YES | Card 8 — PK Clock vs PD Clock + Duration Formula Boundary, immediately after Marker Block 5 |

### B9. Zero-Omission Coverage Matrix

| Domain | Required item | Evidence in PART A | Status | Action |
|---|---|---|---|---|
| C1 Scope concepts | Turnover foundation, four models, tss/peak-shift, Imax/Emax semantics, initial estimates, irreversible action, effect compartment discrimination, PK/PD clock + duration | §2 Cards 1–8 | PRESENT | None |
| C1 Scope chapter role | Separate distribution delay, turnover delay, target consumption, and rate-limiting clocks | §1 Big Idea; §8 Final locked summary | PRESENT | None |
| C2 Required data anchors | G&W PD4/PD5/PD6/PD7/PD9 anchors retained where Content Lock v2 locked them | §2 Cards 3, 5, 7 and self-test Q3–Q4 | PRESENT_COMPRESSED | Do not expand beyond Content Lock. |
| C2 Required data anchors | R&T clinical anchors: digoxin, naproxen, midazolam, ibuprofen, warfarin, acenocoumarol/phenprocoumon, succinylcholine, minoxidil, aspirin/omeprazole/paclitaxel, methylprednisolone, rosuvastatin | §2 Cards 1, 4, 6, 8; §5; §7 | PRESENT_COMPRESSED | Kept at MUST/CONTEXT level. |
| C3 Audit MUST_FIX | Naproxen correction: 500 mg oral, Fig 8-2, dental pain, 1–8 h, counterclockwise hysteresis | Card 1 table; Q5 | PRESENT | Forbidden restoration: 250 mg / Fig 8-3. |
| C3 Audit MUST_FIX | Ibuprofen figure corrected to Fig 8-9 | Card 1 table | PRESENT | None |
| C3 Audit MUST_FIX | Paclitaxel corrected to Fig 8-22 and leukocyte/leukopenia framing | Card 6/§5 context | PRESENT_COMPRESSED | None |
| C3 Audit MUST_FIX | Minoxidil corrected to single oral 25 mg MAP-lowering context, not topical | §5-5 | PRESENT_COMPRESSED | Do not restore topical framing. |
| C3 Audit MUST_FIX | Zooparc observed repeated doses corrected to 2.5 mg and 5 mg; 25 mg/day as projection | Q4 and Card 3/PD9 context | PRESENT | None |
| C3 Audit MUST_FIX | Unsupported NDA/IND/FDA reviewer claims labeled or removed | §5-4 contains only `[교과서 외 실무 해석]` label | PRESENT | Do not convert label into textbook claim. |
| C3 Audit MUST_FIX | “All responses delayed” hedged by direct-link caveat | §1 Big Idea; Card 1 | PRESENT | None |
| C3 Audit MUST_FIX | tss/peak-shift toned down from deterministic rule | Card 3; Q2/Q3 | PRESENT | None |
| C3 SHOULD_FIX | Methylprednisolone exact 16/31/63/125/250/500/1000 mg doses | Card 4 | PRESENT | None |
| C3 SHOULD_FIX | `Kkill/kk` vs `Kelim` notation separation | Card 6 | PRESENT | `[확인 필요]` retained as source-notation caution. |
| C4 Audit T5 | T Key Relationships / direct-link vs delayed bridge / slower-clock author message | §1; §8; Card 8 | PRESENT | None |
| C5 Figure coverage | Approved KEEP figures #1, #2, #3, #6, #7, #8 | Six figure marker blocks in Cards 1, 2, 4, 7, 8 | PRESENT | Render only approved markers. |
| C5 Figure rights | No copyrighted textbook images embedded | Learner navigation note; PART B B2/B4 | PRESENT | Render pointers or distinct redraw only. |
| C6 Page tags | Existing `[G ...]` and `[T ...]` page tags preserved | PART A body | PRESENT | No new page tags fabricated. |
| C7 Crucible Grade A | tss first-order analogue, ΔR/Emax semantics, Region 2 boundary, PK/PD clock non-identifiability, wrong-clock warning | Cards 3, 4, 8; §5; §7 | PRESENT_COMPRESSED | Preserved only as adopted logic. |
| C8 Deprecated draft regression | unsupported regulatory overclaims, wrong figure numbers, wrong naproxen/minoxidil/Zooparc framing, broad scope creep | PART B B5/B7 guardrails | PRESENT | Do not restore Step 1 text. |
| C9 Canonical body integrity | Content Lock v2 learner body spliced with approved markers; no broad rewrite | PART A §1–§8 | PRESENT | Only learner wrappers and labeled augmentations added. |

### B10. Micro-Patch Log

No micro-patches needed. PART A equals the learner-facing Content Lock v2 body exact-spliced with approved Phase 4C markers, plus allowed learner wrappers and labeled Mastery Augmentation Layer. No scientific page tags were added, deleted, or renumbered.

### B11. Mastery Augmentation Log

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
|---:|---|---|---|---|---|---|
| 1 | Card 1 | J/W | YES | AUDIT_DERIVED | Clarifies direct-vs-delayed as resolution-sensitive before model selection. | Low |
| 2 | Card 2 | M/J | YES | CRUCIBLE_DERIVED | Converts taxonomy into action-site and clock reasoning. | Low |
| 3 | Card 3 | F | YES | AUDIT_DERIVED | Prevents deterministic overuse of tss/peak shift. | Low |
| 4 | Card 4 | M/K | YES | CRUCIBLE_DERIVED | Prevents parameter-label comparison errors. | Low |
| 5 | Card 5 | W/J | YES | CRUCIBLE_DERIVED | Frames manual estimates as mechanistic sanity checks. | Low |
| 6 | Card 6 | F | YES | TEXTBOOK_DERIVED | Prevents drug-disappearance/effect-disappearance confusion. | Low |
| 7 | Card 7 | J/R | YES | EXPERT_INFERENCE | Adds model-defensibility lens without new data or examples. | Medium |
| 8 | Card 8 | F | YES | AUDIT_DERIVED | Prevents wrong-clock application of duration formula. | Low |

| Rejected candidate | Reason for rejection |
|---|---|
| Add new named clinical examples beyond G&W/R&T source universe | Would violate source boundary and require external support. |
| Add Mermaid/SVG code in Phase 4D | Phase 4D decides content/markers only; Phase 5 renders visuals. |
| Add extra figure candidates for negative feedback, DRT, or target consumption | Rejected by v2.1 visual ROI/budget logic. |


# 11_Content Lock v1 — Indirect Response / Turnover / DRT / Baseline / Effect Compartment / Rate-Limiting / Duration

**Source Universe**: Gabrielsson & Weiner 5e, Ch.2 §2.6.7; Ch.3 §3.7–3.8, §3.10, §3.12; PD4/PD5/PD6/PD7/PD9 + Rowland & Tozer 5e, Ch.8 pp.233–264  
**Output status**: Content Lock v1  
**Compression status**: Step 1 Draft v0보다 짧게 압축. Cards 8–9는 Crucible Grade A 판단에 따라 단일 Card 8로 통합.  
**Source-page policy**: MUST cards, equation blocks, and key examples retain verified page tags. Unresolved `[확인 필요]` items are retained.

---

## Updated Curation Map

이 세션의 Telos는 **plasma concentration과 measured response가 동시에 움직이지 않을 때, 그 지연이 distribution 문제인지, turnover 문제인지, target-consumption 문제인지, 또는 PK/PD rate-limiting clock 문제인지 판단하는 것**이다. Content Lock 단계에서는 Draft v0의 9개 MUST를 8개로 압축한다. Card 8과 Card 9는 R&T Ch.8의 단일 논리 흐름 — “느린 clock을 먼저 판별하고, PK-rate-limited일 때만 duration formula를 적용한다” — 으로 합친다.

### MUST — §2 카드 발급 대상

| # | Locked MUST concept | Source page tags | Lock decision |
|---:|---|---|---|
| 1 | Turnover foundation + hysteresis classification | [G pp.235–237; T pp.234–235, 239] | Retain. Direct response caveat added. |
| 2 | Four-model taxonomy: inhibit/stimulate × production/loss | [G pp.237–245; T pp.240–241] | Retain. Four models shown side-by-side. |
| 3 | tss / peak-shift mechanism discrimination | [G pp.247–251; G pp.778–783] | Retain with caveat: diagnostic signal, not deterministic rule. |
| 4 | Imax/Emax multiplier semantics + linear PK ≠ linear PD | [G p.246; T pp.256–258] | Retain. Methylprednisolone exact doses corrected. |
| 5 | Graphical initial parameter estimation + blocking-dose / DRT logic | [G pp.247–251, 272–275; T pp.244–247] | Retain and compress. |
| 6 | Irreversible second-order drug action + target consumption | [G pp.256–260; T pp.251–252] | Retain. `Kkill/kk` vs `Kelim` notation separated; `[확인 필요]` note retained. |
| 7 | Turnover vs effect compartment discrimination crisis | [G pp.758–763; T pp.244–246] | Retain as Apex Concept. Regulatory language labeled `[교과서 외 실무 해석]`. |
| 8 | PK clock vs PD clock + duration formula boundary | [T pp.243, 247–256] | Merge former Cards 8–9. Wrong-clock `tD` warning added. |

### CONTEXT — MUST 카드에 1–2문장으로 통합

Negative feedback/moderator model [G pp.110–111], baseline drift/disease progression [G pp.317–319], DRT without measured concentration [G pp.272–275], cell growth/kill [G pp.258–260], rosuvastatin OATP1B1 exposure-response disconnect [T pp.258–259], ranitidine/ibuprofen/minoxidil/paclitaxel examples [T pp.240–254], and study problems [T pp.260–264] are retained only as context or self-test anchors. They do not receive separate MUST cards.

---

## Adjudication Table Summary

Audit T6 Figure Inventory is excluded here by instruction and flows unchanged to Phase 4C.

### A. Audit v1 adjudication ledger

| Source | Item | Verdict | Rationale |
|---|---|---|---|
| Audit Executive | Core spine: turnover foundation, four-model taxonomy, tss/peak-shift, effect compartment vs turnover, PK/PD rate-limiting, duration-log dose | ADOPT | These are the session’s mechanistic spine and are directly supported by G/T sources. |
| Audit T1 | Turnover ODE, `kin/kout` semantics, `R0=kin/kout` | ADOPT | Core equations match G p.237. |
| Audit T1 | Hysteresis definition | ADOPT | T p.234–235 directly supports rising/falling-phase path difference. |
| Audit T1 | Direct response caveat | ADOPT | G delayed-nature framing is retained but hedged against T direct-link examples. |
| Audit T1 | Negative feedback equations and IgG half-life anchor | PARTIAL_ADOPT | Retained as CONTEXT in Card 1, not a separate card. |
| Audit T1 | Four-model taxonomy and `I(C)` / `S(C)` functions | ADOPT | Required for all subsequent model selection. |
| Audit T1 | Models 1–4 ODEs | ADOPT | All four ODEs retained in Card 2 side-by-side table. |
| Audit T1 | tss discrimination | PARTIAL_ADOPT | Retained as strong signal, not deterministic rule; rate-limiting/dose-range caveat added. |
| Audit T1 | Imax/Emax semantics | ADOPT | Retained in Card 4 as a major semantic trap. |
| Audit T1 | Initial parameter estimate table / manual derivation | ADOPT | Retained in Card 5, compressed to operational rules. |
| Audit T1 | Blocking-dose equations and synthesis-rate inversion | ADOPT | Retained as clinical analogue of `R0/kout` extraction. |
| Audit T1 | DRT framework | PARTIAL_ADOPT | Retained as one context paragraph in Card 5. |
| Audit T1 | Irreversible kill and survival fraction | ADOPT | Retained in Card 6 with notation disambiguation. |
| Audit T1 | Cell growth/kill and `Bmax≈30,000 CFU` | PARTIAL_ADOPT | Retained as antimicrobial application, not full derivation. |
| Audit T1 | K notation conflict | ADOPT | Educational notation split into `Kkill/kk` vs `Kelim`; `[확인 필요]` retained. |
| Audit T1 | Effect compartment ODE and PD6 equivalence | ADOPT | Locked as Card 7 Apex Concept. |
| Audit T1 | `tD` formula and dose-doubling rule | ADOPT | Merged into Card 8 after rate-limiting boundary. |
| Audit T1 | Succinylcholine linear decline and doses | ADOPT | Retained as the clean PK-rate-limited example. |
| Audit T1 | Naproxen late summary `250 mg / Fig 8-3` | ADOPT | Corrected to 500 mg oral, Fig 8-2, dental pain, 1–8 h. |
| Audit T1/T2 | Ibuprofen late figure number | ADOPT | Corrected to Fig 8-9. |
| Audit T1/T2 | Minoxidil `topical` framing | ADOPT | Corrected to single oral 25 mg, MAP lowering. |
| Audit T1/T2 | Paclitaxel Fig 8-19 / ANC phrasing | ADOPT | Corrected to Fig 8-22, leukocyte fraction/leukopenia. |
| Audit T1/T2 | Methylprednisolone rounded 32/64 mg | ADOPT | Corrected to exact 31/63 mg. |
| Audit T1/T2 | PD9 Zooparc observed dose | ADOPT | Corrected to observed 2.5 mg and 5 mg repeated dosing; 25 mg/day labeled projection. |
| Audit T1/T4 | Regulatory/NDA/IND/FDA reviewer claims | PARTIAL_ADOPT | Kept only as `[교과서 외 실무 해석]` in §5 Critical Blow; removed from source-fidelity claims. |
| Audit T2 | Digoxin, tissue distribution, midazolam, dexamphetamine, ranitidine | PARTIAL_ADOPT | Retained as diagnostic examples; direct-link examples compressed. |
| Audit T2 | Warfarin blocking, acenocoumarol/phenprocoumon, succinylcholine, aspirin, omeprazole | ADOPT | These are high-yield clinical anchors for Cards 5, 6, 8. |
| Audit T2 | Rosuvastatin OATP1B1 | PARTIAL_ADOPT | Reduced to context footnote under exposure-response disconnect. |
| Audit T2 | Propranolol and endogenous-substance study problems | REJECT | Exercise-level material; not needed for 10-minute handout. |
| Audit T3 | “Time must always be considered” author message | ADOPT | Becomes §1 master lens. |
| Audit T3 | Direct link vs delayed response distinction | ADOPT | Explicitly inserted into Card 1 and §1. |
| Audit T3 | Slower of PK/PD clocks controls decline | ADOPT | Becomes Card 8 master lens. |
| Audit T3 | Linear PK does not imply linear PD | ADOPT | Becomes Card 4/8 warning. |
| Audit T3 | Lack of peak shift does not prove link model | ADOPT | Inserted into Card 3/7. |
| Audit T5 | G §2.6.7 feedback and G §3.12 baseline | PARTIAL_ADOPT | Retained only as context. |
| Audit T5 | G §3.7 reversible turnover | ADOPT | Core of Cards 1–5. |
| Audit T5 | G §3.8 irreversible action | ADOPT | Core of Card 6. |
| Audit T5 | G §3.10 DRT | PARTIAL_ADOPT | Retained in Card 5 and §7 self-test only. |
| Audit T5 | G PD4–PD7/PD9 cases | ADOPT | Retained as numeric anchors after corrections. |
| Audit T5 | T Ch.8 core headings through duration | ADOPT | Mapped to Cards 1, 5, 7, 8. |
| Audit T5 | T Key Relationships | PARTIAL_ADOPT | Condensed into §8 recap. |
| Audit T5 | T Study Problems | REJECT | Not central enough for locked handout. |

### B. Crucible v1 adjudication ledger

| Source | Item | Verdict | Rationale |
|---|---|---|---|
| Crucible T1 Wall #1 | tss first-order analogue blindness | ADOPT | Inserted into Card 3 and §7 Q2. |
| Crucible T1 Wall #2 | ΔR / Emax semantic overload | ADOPT | Inserted into Card 4. |
| Crucible T1 Wall #3 | Region 2/3 time behavior | ADOPT | Inserted into Card 8 as `tD` applicability boundary. |
| Crucible T1 Wall #4 | PK clock vs PD clock non-identifiability | ADOPT | Becomes Card 8 master lens. |
| Crucible T1 Integration #1 | Five-minute structural model choice | PARTIAL_ADOPT | Retained as §8 professional moat; detailed PD7 walk-through compressed. |
| Crucible T1 Integration #2 | NDA Module framing | PARTIAL_ADOPT | Retained only under `[교과서 외 실무 해석]`. |
| Crucible T1 Integration #3 | DDI sampling-time shift | PARTIAL_ADOPT | Retained as §8 failure mode, not a card. |
| Crucible T1 Integration #4 | Single-dose duration → dose extension | ADOPT | Integrated into Card 8. |
| Crucible T1 Intuition #1 | Post-trough rebound timing | PARTIAL_ADOPT | Retained as §8C expert check. |
| Crucible T1 Intuition #2 | OFV stuck-then-drop | PARTIAL_ADOPT | Retained as Card 5 trench tip. |
| Crucible T1 Intuition #3 | Response peak before Cmax | PARTIAL_ADOPT | Retained as self-test warning. |
| Crucible T1 Intuition #4 | Hysteresis 30-second direction diagnosis | ADOPT | Inserted into Card 1 and §5. |
| Crucible T2 Risk #1 | tss/peak-shift deterministic overclaim | ADOPT | Directly applied to Card 3. |
| Crucible T2 Risk #2 | “all delayed” absolute statement | ADOPT | Directly hedged in §1/Card 1. |
| Crucible T2 Risk #3 | Wrong-clock `tD` calculation | ADOPT | Directly applied to Card 8. |
| Crucible T2 Risk #4 | Linear PK ≠ linear PD | ADOPT | Directly applied to Card 4/8. |
| Crucible T2 Signature #1 | Dose-scaled kout mirage | ADOPT | Added to Card 3 trench tip. |
| Crucible T2 Signature #2 | Phantom convergence with constraint | PARTIAL_ADOPT | Retained in Card 7, compressed. |
| Crucible T2 Signature #3 | False half-life compression | PARTIAL_ADOPT | Retained in §8 failure modes. |
| Crucible T2 Signature #4 | Wrong-clock `tD` calculation | ADOPT | Card 8. |
| Crucible T3 Tip 1 | Mirror-slope misread | ADOPT | Card 3 and §5. |
| Crucible T3 Tip 2 | Linear S(C) turnover ≈ effect compartment | ADOPT | Card 7 and §5 Critical Blow. |
| Crucible T3 Tip 3 | `kin/kout` reparameterization | ADOPT | Card 1 and Card 5. |
| Crucible T3 Tip 4 | K notation split | ADOPT | Card 6. |
| Crucible T3 Tip 5 | Linear PK ≠ linear PD | ADOPT | Card 4/8. |
| Crucible T4 Items 1–4 | Hedge all-delayed; tone down tss; label regulatory; fix naproxen | ADOPT | All applied. |
| Crucible T4 Item 5 | MUST/CONTEXT separation of R&T examples | ADOPT | Dense examples compressed. |
| Crucible T4 Item 6 | Replace K tag with explicit split | PARTIAL_ADOPT | Explicit split added while `[확인 필요]` retained. |
| Crucible T4 Item 7 | Card 8–9 merge | ADOPT | Implemented. |
| Crucible T4 Items 8–10 | Direct-link compression; rosuvastatin footnote; duration derivation compression | ADOPT | All compressed. |
| Crucible Grade C | Anti-AI moat, curriculum redefinition, Bayesian TDM/transit extensions, direct-link expansion, study-problem expansion, ke0 algorithm details | REJECT | Scope creep or duplicate material. |

---

# §1 — Session Header & Roadmap

<!-- MASTER LENS -->
## Big Idea

대부분의 임상적으로 관찰되는 pharmacodynamic response는 plasma concentration과 완전히 동시에 움직이지 않는다. 그러나 그 지연이 **무시 가능할 정도로 짧으면 direct PK-PD link**로 충분하고, 지연이 관찰 가능하면 그 원인을 **distribution delay, turnover/system flux, target consumption, 또는 PK/PD rate-limiting clock** 중 하나로 분해해야 한다. [G pp.235–236; T pp.233–235, 239]

<!-- ANCHOR -->
## Conceptual navigation

이 세션은 다음 순서로 잠긴다.

1. `dR/dt = kin − kout·R`가 baseline과 time constant를 만든다. [G p.237]
2. 약물은 production 또는 loss 중 하나를 inhibit/stimulate한다. [G pp.237–245]
3. tss/peak shift는 작용 부위의 강력한 신호지만, PK rate-limiting과 limited dose range에 의해 가려질 수 있다. [G pp.247–251; G pp.778–783]
4. Effect compartment와 turnover model은 제한된 설계에서 거의 같은 curve를 낼 수 있으므로, fit quality만으로 구조를 잠그면 안 된다. [G pp.758–763; T pp.244–246]
5. Response decline은 drug PK clock 또는 system PD clock 중 느린 쪽이 결정한다. `tD` formula는 PK-rate-limited일 때만 사용한다. [T pp.243, 247–256]

<!-- RECAP -->
## Locked takeaway

이 장의 핵심은 “delayed response는 하나의 현상이 아니라 여러 원인의 공통 표면형”이라는 점이다. 모델링의 첫 질문은 “어떤 ODE가 curve를 잘 맞추는가?”가 아니라 “무엇이 시간을 rate-limit 하는가?”이다.

---

# §2 — Concept Anatomy Cards

## Card 1 — Turnover Model Foundation + Hysteresis Classification

<!-- MASTER LENS -->
### Big Idea

Turnover model의 최소 골격은 response가 **생산되는 속도**와 **사라지는 속도**의 차이다. Baseline은 독립적인 상수가 아니라 두 속도의 비율이며, hysteresis loop는 이 system이 plasma concentration을 즉시 따라가지 못한다는 시각적 신호다. Direct response를 부정하는 것이 아니라, **지연이 data resolution 안에서 보이는지**를 먼저 판단한다. [G pp.235–237; T pp.234–235, 239]

### A. Formal definition

$$rac{dR}{dt}=k_{in}-k_{out}R \quad \text{[G Eq 3:74; G p.237]}$$

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

For model fitting, estimate `R0` and `kout`, not `kin` and `kout` independently:

$$k_{in}=R_0 k_{out}$$

$$\frac{dR}{dt}=k_{out}(R_0-R) \quad \text{[G Eq 3:103; G p.247]}$$

PD4 shows why this matters: a pool model can produce near-nonidentifiability when upstream and response turnover constants are estimated without sufficient design support. [G pp.742–752]

<!-- TRENCH -->
### Trench-level tip

If `kin` and `kout` show extreme correlation or the covariance step behaves like it is “stuck then drops,” recode as `R0 × kout`. This is not cosmetic; it changes the search geometry from two poorly separable rates to one baseline and one time constant.

### D. Context integration

Negative feedback adds a moderator `M`, so higher response can accelerate loss. The IgG example shows half-life shortening toward about 11 days at 30 mg·mL⁻¹ serum IgG, illustrating that `kout` can be system-state dependent rather than fixed. [G pp.110–111]

Baseline drift models are separate extensions; when disease progression or circadian drivers move `R0`, the basic constant-baseline turnover equation is no longer sufficient. [G pp.317–319]

<!-- RECAP -->
### Recap

Baseline is a ratio, hysteresis is a time-delay diagnostic, and reparameterization is the first practical defense against turnover-model nonidentifiability.

---

## Card 2 — Four-Model Taxonomy: Inhibit/Stimulate × Production/Loss

<!-- MASTER LENS -->
### Big Idea

A reversible turnover response has only four canonical drug-action sites: inhibit production, inhibit loss, stimulate production, or stimulate loss. This table is not just taxonomy; it is the minimal grammar for translating a biological mechanism into a NONMEM `$DES` block. [G pp.237–245; T pp.240–241]

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

Models 1 and 3 alter the zero-order input term; therefore the time constant remains `1/kout`. Models 2 and 4 alter the first-order loss term; therefore the apparent time constant changes with concentration. This is why `tss` behavior can identify action site, but only when PK is not the slower clock.

<!-- TRENCH -->
### Trench-level tip

Do not infer the model from response direction alone. A downward response can arise from Model 1 or Model 4. You need the time pattern: production-side models mainly change extent; loss-side models change both extent and apparent speed.

<!-- RECAP -->
### Recap

The four-model table is the session’s structural lock. Every later claim — tss, peak shift, initial estimates, and model discrimination — is a consequence of whether the drug changes input or output.

---

## Card 3 — tss / Peak-Shift Mechanism Discrimination

<!-- MASTER LENS -->
### Big Idea

`tss` and peak-shift are high-value diagnostic signals, not verdicts. Models 1 and 3 tend to show dose-independent time to PD steady state because the loss rate is unchanged. Models 2 and 4 can show dose-dependent `tss` because the drug changes the loss term. But this rule fails when PK is slow, the dose range is narrow, the response is noisy, or the mechanism has unmodeled nonlinearities. [G pp.247–251; G pp.778–783; T p.243]

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

## Card 4 — Imax/Emax Multiplier Semantics + Linear PK ≠ Linear PD

<!-- MASTER LENS -->
### Big Idea

`Emax` is not a universal unit. In a direct Emax model it is often an absolute distance from baseline; in a turnover model it is a multiplier on a system whose baseline already contains `kin/kout`. Confusing these meanings makes in vitro potency, clinical EC50, and model-derived effect size appear comparable when they are not. [G p.246]

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

## Card 5 — Graphical Initial Parameter Estimation + Blocking Dose / DRT

<!-- MASTER LENS -->
### Big Idea

Initial estimates are not a nuisance before “real modeling.” In turnover PD, graphical estimation is the first mechanistic check. It separates baseline, time constant, potency, and maximal effect before NONMEM is allowed to search. [G pp.247–251]

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

Dose-Response-Time analysis can infer baseline, slope, potency, and maximal effect even when concentration data are absent, but it is a coarser inverse problem than full PK/PD modeling. Retain it as a fallback or teaching bridge, not as a replacement for measured exposure when exposure is available. [G pp.272–275]

<!-- TRENCH -->
### Trench-level tip

A model that requires absurd starting values usually means the graphical stage was skipped or the wrong clock was used. Fix the starting biology before expanding random effects.

<!-- RECAP -->
### Recap

Manual initial estimates are not old-fashioned; they are the first identifiability audit.

---

## Card 6 — Irreversible Drug Action + Target Consumption

<!-- MASTER LENS -->
### Big Idea

Reversible turnover models regain baseline because the system continues to produce and remove response. Irreversible action is different: drug exposure permanently removes response units, targets, or cells during the exposure window. The drug may disappear while the biological consequence persists. [G pp.256–260; T pp.251–252]

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

## Card 7 — Turnover vs Effect Compartment Discrimination Crisis

<!-- MASTER LENS -->
### Big Idea — Apex Concept

A turnover model and an effect-compartment model can produce nearly identical response-time curves under a limited single-dose design. They differ not in curve smoothness but in causal claim: **Is the delay because drug arrives slowly at the biophase, or because the response system itself turns over slowly?** [G pp.758–763; T pp.244–246]

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

## Card 8 — PK Clock vs PD Clock + Duration Formula Boundary

<!-- MASTER LENS -->
### Big Idea

Two clocks run after dosing: the drug PK clock and the system PD clock. The slower clock controls the observed decline of response. Duration formulas based on drug elimination are valid only when response is PK-rate-limited and exposure-response is effectively fixed. [T pp.243, 247–256]

### A. Clock discrimination

| Situation | Slower clock | Locked examples | Modeling consequence |
|---|---|---|---|
| PK rate-limited | Drug elimination/distribution | Succinylcholine 0.5/1/2/4 mg·kg⁻¹ i.v., muscle paralysis; minoxidil single oral 25 mg, MAP lowering [T pp.249–256] | `tD` formula can be meaningful. |
| PD rate-limited | System turnover/target regeneration | Acenocoumarol vs clotting factor turnover; aspirin platelet/TxB₂; omeprazole proton-pump recovery; paclitaxel leukocyte recovery [T pp.243, 251–254] | Turnover/target-consumption model needed; PK `k` alone cannot predict duration. |
| Drug PK slower than system | PK dominates even for indirect mechanism | Phenprocoumon half-life ~5 days vs clotting-factor dynamics [T p.243] | Anticoagulant effect recovery follows drug persistence. |

### B. Region 1/2/3 and linear decline

In the middle portion of a graded E-logC relationship, response declines approximately linearly with time after a single dose:

$$Response=E(0)-mkt \quad \text{[T Eq 8-9; T pp.247–249]}$$

This is a Region 2 statement. Region 3 is plateau-like; Region 1 returns toward first-order-looking behavior. Succinylcholine’s roughly 22%/min decline illustrates this middle-region linearity. [T pp.249–250]

### C. Duration formula

For a PK-rate-limited response with fixed exposure-response relationship:

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

Most errors in this session are not algebra errors. They are **clock-location errors**: wrong input/output site, wrong source of delay, wrong meaning of `Emax`, or wrong rate-limiting process.

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

This session sits between direct exposure-response modeling and advanced disease/response systems. It is the first point where the modeler must separate:

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

Indirect response modeling is not “adding a delay.” It is assigning delay to the correct causal clock. The locked workflow is:

**hysteresis direction → four-model action site → tss/peak-shift triage → initial-parameter audit → turnover-vs-link discrimination → PK/PD clock selection → duration formula only if PK-rate-limited.**


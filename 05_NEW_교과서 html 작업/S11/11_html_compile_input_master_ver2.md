# 11_HTML Compile Input Master — v2 (Mastery-Strengthened)

## Version Note

**v1 → v2 변경 사유**: v1은 5대 Certificate(Learner-Standalone, Zero-Omission, Mastery-Uplift, Source-Boundary, HTML-Readiness)를 모두 통과했으나, Crucible v1이 Grade A로 채택한 거장 통찰 5종(PD4 Pool 1/2 r=0.9999 비식별성, OFV stuck-then-drop pattern, Hysteresis 30초 방향 진단, Mirror-Slope Misread PD7 정량 수치, Post-trough rebound timing 직관)이 v1에서는 일반화·압축되어 거장 voice가 약화되어 있었다. v2는 **content lock v2 본문(fact·equation·page tag·marker)을 100% 무손상 유지**한 채로, Phase 4D의 Mastery Augmentation Layer를 확장하여 위 5종을 명시적으로 복원한다. 또한 Card 8.D의 Rosuvastatin 절을 §5-5 footnote로 이동하여 흐름 정합성을 높이고, §8C Professional Moat와 §5 Recap을 거장의 30초 진단 sequence 형태로 강화한다.

## Phase 4D Certification (v2)

| Certificate | Status | Basis (v2) |
|---|---|---|
| Learner-Standalone Certificate | PASS | PART A는 §1–§8 학습자 본문만 포함; audit/process/compiler 자료는 PART B에 격리 (v1과 동일). |
| Zero-Omission Certificate | PASS | Scope/Audit/Crucible Grade A 항목 모두 PRESENT 또는 PRESENT_COMPRESSED. **v2 추가**: Crucible Grade A 5종(Wall #4 PD4 비식별성·Intuition #2 OFV stuck-then-drop·Intuition #4 Hysteresis 30초 진단·T3 Tip 1 Mirror-Slope PD7 수치·Intuition #1 Post-trough rebound)을 Mastery Augmentation Layer로 명시 복원. HOLD_UNRESOLVED 없음. |
| Mastery-Uplift Certificate | PASS | v1의 8개 augmentation notes 위에 **v2에서 5개 Mastery Anchor를 추가**(Card 1·3·5·7·8). 모두 bounded·adjacent·source-labeled. 본문 재작성은 수행되지 않음. |
| Source-Boundary Certificate | PASS | 모든 augmentation은 TEXTBOOK_DERIVED, AUDIT_DERIVED, CRUCIBLE_DERIVED, EXPERT_INFERENCE 중 하나로 라벨링. v2 추가 항목도 동일 라벨 체계 적용. |
| HTML-Readiness Certificate | PASS | PART B B1-B11 + 신규 B12(v1→v2 변경 로그) 완비. Marker·page tag·navigation anchor·responsive/print·forbidden restoration 규칙 보존. |

## Assembly Mode

PATCH MODE (v2 유지)

Rationale: `11_Content Lock v2.1.md`는 figure marker insertion plan이며, learner-facing canonical body는 `11_Content Lock v2.md`에서 가져옴. 6개의 marker block이 지정 위치에 splice됨. v2는 v1의 splice 결과를 변경하지 않는다(B8 Splice Verification Table v1 그대로 유지).

## Input Manifest (v2 추가 행만 표시; 나머지는 v1과 동일)

| File | Role | Authority level | Used for | Notes |
|---|---|---|---|---|
| `11_html_compile_input_master.md` (v1) | v2 base substrate | A8 | v2의 모든 §1-§8 본문은 v1에서 그대로 carry-over | v2는 Mastery Augmentation Layer만 확장 |
| (v1의 Input Manifest 모든 항목 carry-over) | — | — | — | v2는 v1 위에 누적적으로 작업 |

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
phase: "4D HTML compile input — v2 mastery-strengthened"
```

### How to use this handout

Read §1 once for the governing question, then study §2 as eight concept cards. For each card, first lock the equation or decision rule, then inspect the adjacent Mastery/Practice/Failure note, then use the approved figure pointer or redraw instruction where present. Do not treat the figure pointer blocks as images; they are Phase 5 instructions or textbook consultation prompts.

**v2 학습 사용법 추가**: 각 카드의 첫 단락(Big Idea)은 세 가지 질문에 동시에 답하도록 구성되어 있다 — ① **이 지식이 왜 이번 세션의 critical path에 있는가**(임상·모델링 결과 차원), ② **앞 카드와 뒤 카드 사이에서 어떤 인과적 다리를 놓는가**(흐름 위치), ③ **이 카드를 5초 안에 활용하기 위해 잡아야 할 핵심 mental model은 무엇인가**(체화 핵심 직관). 카드별로 이 셋이 한 단락에 자연스럽게 녹아 있도록 적었다. 이어지는 본문은 이 mental model을 잡은 상태로 읽어야 가장 효율적이다.

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

<!-- ANNOTATION --> 여기서 hysteresis는 "같은 농도에서도 시간 경로에 따라 response가 달라지는 현상"이다.

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

이 장의 핵심은 "delayed response는 하나의 현상이 아니라 여러 원인의 공통 표면형"이라는 점이다. 모델링의 첫 질문은 "어떤 ODE가 curve를 잘 맞추는가?"가 아니라 "무엇이 시간을 rate-limit 하는가?"이다.

---

# §2 — Concept Anatomy Cards

## Card 1 — Turnover Model Foundation + Hysteresis Classification

<!-- MASTER LENS -->
### Big Idea

Turnover model의 최소 골격은 response가 **생산되는 속도**와 **사라지는 속도**의 차이다. Baseline은 독립적인 상수가 아니라 두 속도의 비율이다. Hysteresis loop는 이 system이 plasma concentration을 즉시 따라가지 못한다는 시각적 신호다. 이 말은 direct response를 부정한다는 뜻이 아니다. 먼저 **지연이 data resolution 안에서 보이는지**를 판단한다. [G pp.235–237; T pp.234–235, 239]

> **왜 첫 카드인가**: 이후 일곱 카드의 모든 결정 — 4-model 작용 부위, tss 진단, Emax 의미, graphical 초기값, irreversible 여부, effect compartment 가설, PK/PD clock 선택 — 은 이 두 줄짜리 ODE에서 분기한다. **`R0=kin/kout`을 비율로 보지 못하면 다음 카드들은 모두 암기 대상이 된다.** 이 카드의 체화 목표는 단 하나다: response 곡선을 보자마자 머릿속에서 "두 개의 수도꼭지 — 들어오는 양 vs 빠지는 양 — 의 균형이 깨진 시간 경로"로 자동 변환되어야 한다.

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

If `kin` and `kout` show extreme correlation or the covariance step behaves like it is "stuck then drops," recode as `R0 × kout`. This is not cosmetic. It changes the search geometry from two poorly separable rates to one baseline and one time constant.

### D. Context integration

Negative feedback adds a moderator `M`, so higher response can accelerate loss. The IgG example shows half-life shortening toward about 11 days at 30 mg·mL⁻¹ serum IgG, illustrating that `kout` can be system-state dependent rather than fixed. [G pp.110–111]

Baseline drift models are separate extensions; when disease progression or circadian drivers move `R0`, the basic constant-baseline turnover equation is no longer sufficient. [G pp.317–319]

<!-- RECAP -->
### Recap

Baseline is a ratio, hysteresis is a time-delay diagnostic, and reparameterization is the first practical defense against turnover-model nonidentifiability.

---

> **Practice Lens — [AUDIT_DERIVED]**  
> Treat "direct" versus "delayed" as a design-resolution decision before treating it as a model-family decision. If the delay is invisible at the sampling and response-resolution scale, a direct link can be defensible even though biology is never literally instantaneous.

> **Mastery Anchor #1 — Hysteresis 30-second direction diagnosis [CRUCIBLE_DERIVED]**  
> 30년 베테랑은 plasma C vs response 산점도를 받자마자 loop 회전 방향만으로 1차 분류를 끝낸다. **Counterclockwise**(R&T naproxen Fig 8-2, ibuprofen Fig 8-9의 시계반대 회전) → 효과가 농도를 *뒤따르는* 양상 → 후보 3가지: ① 효과 부위 분포 지연(effect compartment), ② Systems-in-flux(turnover), ③ active metabolite 생성 지연. **Clockwise** → 효과가 농도보다 *앞서가는* 양상 → 후보군: ① tolerance/down-regulation, ② counter-regulatory feedback, ③ enantiomer-specific kinetics(이 후자 분류는 [교과서 외 실무 해석]; 전자 3분류는 R&T 본문 직접 도출). 이 30초 진단이 끝나야 Card 2-3의 4-model 분류가 efficient하게 작동한다.

> **Mastery Anchor #2 — Reparameterization signature: OFV "stuck-then-drop" [CRUCIBLE_DERIVED]**  
> NONMEM 출력에서 30회 iteration 동안 OFV가 거의 변하지 않다가 갑자기 큰 폭으로 하락한다면, 그것은 보통 `r(kin, kout) > 0.98` 상관이 search direction을 죽이고 있다는 신호다. PD5 Table 5.1이 이 패턴을 직접 기록한다 — *"correlation greater than 0.98… reparameterization of the model by baseline R0 and kout."* 이 패턴을 본 베테랑은 $COV step 결과를 기다리지 않고 즉시 Eq 3:103의 (R0, kout) 재파라미터화로 옮겨간다. PD4 Pool 1의 `r(k1, kout) = 0.9999`, CV% 4000 사례가 이 비식별성의 극단형이며, 같은 데이터에 k1=kout 제약을 걸어 만든 Pool 2의 "정상적인 CV%"는 데이터가 동등성을 *지지*한 것이 아니라 제약이 비식별성을 *해결*한 것일 뿐이라는 점을 PD4 §Comparison이 직접 지적한다.

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

> **흐름에서의 역할**: Card 1이 baseline을 비율로 봤다면, Card 2는 그 비율을 약물이 어디에서 깨는가를 결정한다. Card 3의 tss 거동, Card 4의 Emax 의미, Card 5의 초기값 도출, Card 7의 effect compartment 감별까지 — **모두 "input을 건드렸나 output을 건드렸나"라는 이 카드의 한 가지 질문에서 분기**한다. 체화 목표는 PD 데이터 한 장면을 보고 4개 칸 중 하나로 자동 분류하는 것이다.

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

<!-- ANNOTATION --> 이 네 모델의 차이는 "response가 올라가느냐 내려가느냐"보다 "drug가 input을 바꾸느냐 output을 바꾸느냐"에 있다. 따라서 다음 Card 3의 `tss` 판별도 이 input/output 구분에서 나온다.

Models 1 and 3 alter the zero-order input term; therefore the time constant remains `1/kout`. Models 2 and 4 alter the first-order loss term; therefore the apparent time constant changes with concentration. This is why `tss` behavior can identify action site, but only when PK is not the slower clock.

<!-- TRENCH -->
### Trench-level tip

Do not infer the model from response direction alone. A downward response can arise from Model 1 or Model 4. You need the time pattern: production-side models mainly change extent; loss-side models change both extent and apparent speed.

<!-- RECAP -->
### Recap

The four-model table is the session's structural lock. Every later claim — tss, peak shift, initial estimates, and model discrimination — is a consequence of whether the drug changes input or output.

---

> **Mastery Note — [CRUCIBLE_DERIVED]**  
> The taxonomy is not a naming exercise; it is an action-site assignment. Once the drug is placed on input or output, the expected `tss` behavior and the interpretation of `kout` change.

> **Mastery Anchor #3 — 5-minute structural model compression [CRUCIBLE_DERIVED]**  
> PD7 Fig 7.1 데이터를 본 30년 베테랑은 5분 안에 Model 4(stimulation of loss)로 압축한다. 추론 절차: ① 응답이 baseline에서 **하강** → 직접 자극은 production stimulation에서만 가능 → 따라서 stimulation은 loss 측에서 일어난다. ② tss가 **dose-dependent로 단축** → Models 1, 3 제외(이들은 loss term을 건드리지 않으므로 tss는 dose-independent이어야 한다). ③ ΔR 방향이 baseline 아래 → Model 2 제외 → **Model 4 확정**. PD5(Model 2: 응답이 baseline 위로 상승, tss 길어짐)와 PD7(Model 4: 응답이 baseline 아래로 하강, tss 짧아짐)을 side-by-side로 학습하면 이 추론이 "암송 가능"에서 "수행 가능"으로 전환된다.

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

> **흐름에서의 역할**: Card 2가 4개 분류 칸을 만들었다면, Card 3은 그 칸 중 어디에 있는지를 *데이터 한 장*에서 판독하는 첫 진단 도구다. **이 카드를 deterministic rule로 외우는 순간 NDA Population PK/PD Analysis 모델 선택 근거가 PD9 Fig 9.5의 명시적 반례 한 장에 무력화**된다. 체화 목표는 tss를 "강한 1차 가설 발생기"로 쓰되, 동시에 4가지 가림 조건(PK rate-limiting, narrow dose range, noisy response, unmodeled nonlinearity)을 동시에 떠올리는 것이다.

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

`tss` tells you where to look, not where to stop. The safest phrase is: "The `tss` pattern supports a production-side/loss-side mechanism under the observed PK-rate conditions."

---

> **Failure Mode — [AUDIT_DERIVED]**  
> The common overreach is to treat `tss` or peak shift as a proof of mechanism. Use it as a strong triage signal, then test whether PK rate-limiting, limited dose range, or nonlinear drug function could mask the expected pattern.

> **Mastery Anchor #4 — Mirror-Slope Misread quantitative signature [CRUCIBLE_DERIVED]**  
> Mirror-slope misread는 추상적 경고가 아니라 **dose-level별 추정 `kout` 값의 단조 변화**라는 정량 시그니처를 갖는다. PD7 Fig 7.1을 사례로 보면 6,400 unit 용량에서 추정 `kout ≈ 0.6 h⁻¹`, 160,000 unit 용량에서 추정 `kout ≈ 1.6 h⁻¹` — 같은 system parameter이어야 할 `kout`이 dose에 따라 단조 증가한다. System parameter는 정의상 dose-invariant여야 하므로, **이 단조 변화는 biology가 아니라 misspecification artifact의 직접 신호**다. Table 3.6의 'Initial ΔR/Δt' 행은 Models 1·4에서만 −kout이고, Models 2·3에서는 zero-order kin이라는 점이 이 misread의 수학적 뿌리다. 정확한 처방: 초기 기울기를 `kout`로 외삽하기 전에 먼저 4-model taxonomy로 작용 부위를 확정한다.

## Card 4 — Imax/Emax Multiplier Semantics + Linear PK ≠ Linear PD

<!-- MASTER LENS -->
### Big Idea

`Emax` is not a universal unit. In a direct Emax model it is often an absolute distance from baseline. In a turnover model it is a multiplier on a system whose baseline already contains `kin/kout`. 이 의미를 혼동하면 in vitro potency, clinical EC50, and model-derived effect size가 서로 비교 가능한 것처럼 보인다. 실제로는 그렇지 않다. [G p.246]

> **흐름에서의 역할**: Card 1-3이 *시간*과 *작용 부위*를 잠갔다면, Card 4는 *효과 크기의 의미*를 잠근다. 이 카드를 놓치면 `Emax = 0.65` 같은 단일 추정치 하나가 *drug-specific potency*인지 *system-baseline에 대한 multiplier*인지 구분이 안 되며, in vitro IC50과 PopPK IC50의 비교가 의미 있는 것처럼 보이는 함정에 빠진다. 체화 목표는 모델 코드를 보자마자 `Emax`의 단위와 의미를 자동으로 분류하는 것이다.

### A. Semantic lock

| Model form | Parameter meaning | Unit / interpretation |
|---|---|---|
| Direct additive Emax | $E=E_0+\frac{E_{max}C^n}{EC_{50}^n+C^n}$ | `Emax` has response units; it is an absolute distance. |
| Direct reparameterized multiplier | $E=E_0(1+\frac{E_{max}C^n}{EC_{50}^n+C^n})$ | `Emax` is dimensionless multiplier of baseline. |
| Turnover Model 3 | $R_{ss}=R_0(1+\frac{E_{max}C^n}{EC_{50}^n+C^n})$ | `Emax` is a multiplier acting through system turnover. |

### B. Linear PK does not imply linear PD

Methylprednisolone is the locked example: exact i.v. phosphate-prodrug dose series is 16 / 31 / 63 / 125 / 250 / 500 / 1000 mg. Plasma AUC increases approximately in proportion to dose, but lymphocyte response does not increase proportionally; high doses approach a PD plateau. [T pp.256–258]

R&T 본문(p.256)은 이 함정을 단호하게 명시한다 — *"Dose linearity in pharmacokinetics does not result in dose linearity in pharmacodynamics. That is almost never the case."*

또한 systemic exposure가 곧 site-of-action exposure가 아닌 disconnect 사례도 같은 챕터에 등장한다: rosuvastatin OATP1B1 polymorphism은 plasma AUC를 substantially 변화시키지만 cholesterol synthesis response는 modestly 변한다(Fig 8-28/8-29 context only; 이것은 별도 turnover model이 아니라 exposure-response disconnect의 보조 관찰). [T pp.258–259]

<!-- TRENCH -->
### Trench-level tip

Before writing "dose-proportional exposure supports dose-proportional response," force the response through the Hill-curve lens. If the proposed dose range sits in Region 3, more exposure mainly extends plateau duration or toxicity risk; it does not double response.

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

Initial estimates are not a nuisance before "real modeling." In turnover PD, graphical estimation is the first mechanistic check. NONMEM이 탐색을 시작하기 전에 baseline, time constant, potency, and maximal effect를 먼저 분리해 두는 단계다. [G pp.247–251]

> **흐름에서의 역할**: Card 1-4가 *어떤 모델*인지 결정했다면, Card 5는 *그 모델의 파라미터 출발점*을 손으로 분리해 두는 단계다. 이 단계가 부실하면 NONMEM은 정답을 알면서도 그 위치까지 못 가거나, 비식별성 골짜기에 갇힌 채 가짜 수렴을 보고한다. 체화 목표는 raw response-time plot 한 장에서 `R0`, `kout`, 그리고 (potency, maximal effect)의 자릿수까지를 5분 안에 추정해보는 손버릇이다 — 이 손버릇이 fitted parameters의 sanity check 기준선이 된다.

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

> **Mastery Anchor #5 — Graphical workflow as identifiability backstop [TEXTBOOK_DERIVED]**  
> PD5 case study가 이 워크플로우의 표준형이다. Compound A에서 `V = 40 L`, `K = 0.9 h⁻¹`인 PK가 먼저 잠긴 상태에서, 4000/16000/80000 unit의 6시간 infusion 데이터를 받는다. ① pre-infusion baseline으로 `R0`를 직접 읽고, ② post-infusion 회복 곡선의 semi-log plot에서 terminal slope로 `kout ≈ 0.43 h⁻¹`의 자릿수를 손으로 잡고, ③ `kin = R0 × kout`로 production rate의 출발점을 정한다. ④ 세 dose levels의 plateau 응답으로 `IC50 ≈ 95`, `Imax ≈ 0.65`의 자릿수까지 잡은 후에야 NONMEM 추정에 들어간다(Table 5.1). 이 손버릇이 빠진 워크플로우에서는 PD4 Pool 1 같은 `r(k1, kout) = 0.9999` 비식별성이 잡히지 않은 채 통과하고, "다음 시험의 sampling time horizon이 절반으로 단축된다"는 PD4 §Comparison 메시지처럼 **잘못된 모델 선택이 후속 임상시험 설계를 비가역적으로 오염**시킨다.

## Card 6 — Irreversible Drug Action + Target Consumption

<!-- MASTER LENS -->
### Big Idea

Reversible turnover models regain baseline because the system continues to produce and remove response. Irreversible action is different. Drug exposure permanently removes response units, targets, or cells during the exposure window. 따라서 drug may disappear while the biological consequence persists. [G pp.256–260; T pp.251–252]

> **흐름에서의 역할**: Card 1-5가 모두 *reversible* turnover의 다양한 형태를 다뤘다면, Card 6은 그 가정 — drug=0이면 system이 baseline으로 돌아온다 — 자체를 깨는 사례를 잠근다. 이 카드를 놓치면 aspirin, omeprazole, paclitaxel 같은 약물의 duration을 plasma half-life로 외삽하는 결정적 오류로 이어진다. 체화 목표는 "drug 사라짐 = effect 사라짐"이라는 무의식적 가정을 분리해서 — Card 7-8의 effect compartment·rate-limiting clock 결정에 필요한 사전 분기점을 만드는 것이다.

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

When cells replicate, irreversible kill must be embedded in growth dynamics. Gabrielsson's cell-growth/kill framework adds logistic or capacity-limited growth and second-order kill; `Bmax≈30,000 CFU` is a context anchor, not a separate MUST card. [G pp.258–260]

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

> **왜 Apex인가**: 이 세션에서 가장 자주 발생하는 실무 오류는 *틀린 모델 선택*이 아니라 *데이터가 두 모델 중 하나를 결정해주지 못한다는 사실 자체를 보지 못하는 것*이다. PD6는 그 비식별성을 정량화한 단일 사례다. 체화 목표는 fit이 아무리 깔끔해도 — 특히 단일 dose-range 데이터 위에서 — 인과 구조 두 가지가 동치 표면 위에 있다는 사실을 자동으로 의심하는 습관이다.

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

**[교과서 외 실무 해석]**: In a regulatory modeling report, this means the model-selection paragraph should include alternative structure evaluation, mechanistic justification, and sensitivity analysis. Avoid unsupported phrases such as "NDA deficiency" unless clearly labeled as practical extrapolation.

<!-- TRENCH -->
### Trench-level tip

If `EC50` changes with dose when fitting an effect-compartment model to a turnover-generated system, the drug parameter is absorbing system dynamics. That is a structural warning, not a potency finding.

<!-- RECAP -->
### Recap

Effect compartment says "drug is late." Turnover says "biology is slow." The curve alone may not tell you which is true.

---

> **Practice Lens — [EXPERT_INFERENCE]**  
> When two causal structures fit equally well, the disciplined move is to document the biological assumption and identify the design feature that would separate them. For this card, model defensibility comes from mechanism plus design support, not from curve smoothness alone.

> **Mastery Anchor #6 — PD6 quantitative equivalence (the crisis as numbers) [CRUCIBLE_DERIVED]**  
> PD6 Table 6.1이 이 비식별성을 숫자로 박는다. 같은 데이터에 두 구조를 적합시켰을 때:
>
> | Metric | Turnover (linear S·kin) | Effect compartment | Δ |
> |---|---|---|---|
> | WRSS | 15,516 | 15,518 | 2 |
> | AIC | 1,041 | 1,040 | −1 |
> | 시간 상수 | `kout = 5.6 h⁻¹` | `ke0 = 5.6 h⁻¹` | 0 |
> | Half-doubling 농도 | `EC50 = 1,633 ng·L⁻¹` | `a = 0.026 → ~1,623 ng·L⁻¹` | <1% |
>
> ΔWRSS = 2와 ΔAIC = −1은 model selection criterion 입장에서 사실상 동치다. PD9 §Perspectives Fig 9.5 right panel의 단언(*"a lack of peak shift with increasing doses does not necessarily imply an effect compartment (link) model"*)이 이 카드의 한 줄짜리 잠금장치다. **mechanism prior 또는 wider dose range 없이는 두 모델 분리가 불가능**하다는 것이 이 표의 메시지이며, 이것이 Card 7의 Apex 위상을 정당화한다.

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

> **세션 닫음 카드의 역할**: Card 1-7이 모델 *구조*에 관한 결정이었다면, Card 8은 그 구조 위에서 *임상 dose-duration 의사결정*이 가능한지 여부를 결정한다. 이 카드를 거치지 않고 Eq 8-12를 사용하면 warfarin·aspirin·omeprazole·paclitaxel 같은 PD-rate-limited 약물에 대해 수학적으로 매끈하지만 임상적으로 무의미한 duration 예측이 나온다. 체화 목표는 어떤 약물에서든 duration 질문을 받았을 때 자동으로 *"PK clock과 PD clock 중 어느 쪽이 느린가?"*를 먼저 묻는 reflex다.

### A. Clock discrimination

| Situation | Slower clock | Locked examples | Modeling consequence |
|---|---|---|---|
| PK rate-limited | Drug elimination/distribution | Succinylcholine 0.5/1/2/4 mg·kg⁻¹ i.v., muscle paralysis; minoxidil single oral 25 mg, MAP lowering [T pp.249–256] | `tD` formula can be meaningful. |
| PD rate-limited | System turnover/target regeneration | Acenocoumarol vs clotting factor turnover; aspirin platelet/TxB₂; omeprazole proton-pump recovery; paclitaxel leukocyte recovery [T pp.243, 251–254] | Turnover/target-consumption model needed; PK `k` alone cannot predict duration. |
| Drug PK slower than system | PK dominates even for indirect mechanism | Phenprocoumon half-life ~5 days vs clotting-factor dynamics [T p.243] | Anticoagulant effect recovery follows drug persistence. |

### B. Region 1/2/3 and linear decline

In the middle portion of a graded E-logC relationship, response declines approximately linearly with time after a single dose:

$$Response=E(0)-mkt \quad \text{[T Eq 8-9; T pp.247–249]}$$

This is a Region 2 statement. 즉, response가 Hill curve의 중간 구간에 있을 때의 근사다. Region 3 is plateau-like; Region 1 returns toward first-order-looking behavior. Succinylcholine's roughly 22%/min decline illustrates this middle-region linearity. [T pp.249–250]

### C. Duration formula

<!-- ANNOTATION --> 따라서 clock discrimination이 먼저 끝나야 한다. For a PK-rate-limited response with fixed exposure-response relationship:

$$t_D=\frac{1}{k}\ln\left(\frac{Dose}{C_{min}V}\right)=\frac{1}{k}\ln\left(\frac{Dose}{A_{min}}\right) \quad \text{[T Eq 8-12; T pp.254–255]}$$

Dose doubling adds one drug half-life of duration:

$$\Delta t_D=\frac{\ln 2}{k}=t_{1/2}$$

This is why succinylcholine duration increases approximately one effective half-life per dose doubling. [T pp.255–256]

<!-- TRENCH -->
### Wrong-clock warning

Do not apply Eq 8-12 to warfarin, aspirin, omeprazole, or paclitaxel-like PD-rate-limited situations. If the system clock is slower than drug disappearance, the formula returns a mathematically neat but biologically wrong duration.

<!-- RECAP -->
### Recap

Before computing duration, ask: "Which clock is slow?" If the answer is PD, stop using PK `k` as the duration driver.

---

> **Failure Mode — [AUDIT_DERIVED]**  
> The duration formula becomes dangerous when it is applied before clock selection. Always decide whether PK or PD is rate-limiting first; only then does the logarithmic dose-duration relation have the intended meaning.

> **Mastery Anchor #7 — Post-trough rebound timing as moderator/feedback signal [CRUCIBLE_DERIVED]**  
> 30년 베테랑은 turnover 모델 fit을 받자마자 **post-trough 회복 곡선의 타이밍**을 본다. observed 데이터가 모델보다 빠르게 baseline으로 돌아온다면 그것은 moderator/feedback compartment 누락의 즉각적 신호다 — `kout`이 시간에 따라 변하지 않는다는 basic turnover 가정의 위반이다. G&W §2.6.7 Eq 2:261-2:263과 IgG 11일 saturable protection이 이 패턴의 prototype이며(serum IgG 30 mg·mL⁻¹에서 half-life가 11일로 단축), `$COV step` 결과가 출력되기 전에 이 시각 점검이 끝나야 한다. 같은 logic이 Card 8의 wrong-clock 진단에도 적용된다 — 예측 duration이 관측 duration과 50% 이상 어긋나거나 dose 증량 시 예측 duration의 증가가 관측치와 비례하지 않는다면, 그것은 rate-limiting clock이 잘못 잡혔다는 정량 시그니처다.

> **Mastery Anchor #8 — Acenocoumarol vs Phenprocoumon as the canonical clock-pair [CRUCIBLE_DERIVED]**  
> 동일한 prothrombin complex 동역학을 공유하는 두 약물에서 acenocoumarol(half-life ~15 h)은 PD clock이 baseline 복귀를 지배하고, phenprocoumon(half-life ~5–6일)은 PK clock이 지배한다(Fig 8-11). 이는 *동일 작용기전을 공유하는 약물군에서도 약물별 PK가 rate-limiting step을 결정한다*는 사실의 결정판이다. **단일 약물 데이터에 갇힌 학습자에게는 이 사실 자체가 보이지 않는다.** 따라서 새로운 약물의 duration 질문을 받을 때, 같은 mechanism을 공유하는 다른 약물의 PK profile을 함께 비교하는 것이 첫 번째 reflex가 되어야 한다.

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
| Common error | Calling any downward response "inhibition" without specifying production vs loss | Treating an increasing response as production stimulation without checking loss inhibition |
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

> **Footnote — Exposure-response disconnect (CONTEXT only)**  
> Rosuvastatin OATP1B1 polymorphism은 systemic plasma exposure를 substantially 변화시키지만 site-of-action(cholesterol synthesis) response는 modestly 변한다. 이는 별도의 turnover model이 아니라 **systemic exposure ≠ site-of-action exposure**의 보조 사례다. Bioequivalence가 효과 동등성을 보장하지 않는 메커니즘으로 자주 인용된다. [T pp.258–259]

<!-- RECAP -->
## §5 Recap — The five clock-location errors

이 세션에서 발생하는 거의 모든 오류는 algebra 오류가 아니라 **clock-location 오류**다. 즉, 시간을 지배하는 *느린 clock의 위치*를 잘못 짚었기 때문에 발생하는 오류다. 5가지 표준 패턴으로 정리한다.

| Error pattern | 잘못 짚은 clock | Locked counter-example |
|---|---|---|
| **E1. Mirror-slope misread** | early response slope를 모든 모델에서 −kout로 외삽 | PD7: 6,400U → 0.6 h⁻¹, 160,000U → 1.6 h⁻¹ — system parameter가 dose-dependent로 보이는 misspecification artifact [G p.251] |
| **E2. Phantom convergence with linear S(C)** | turnover와 effect compartment가 같은 fit을 줬으므로 effect compartment 확정 | PD6 Table 6.1: ΔWRSS = 2, kout = ke0 = 5.6 h⁻¹ — fit 동등성이 mechanism 결정을 의미하지 않음 [G pp.758–763] |
| **E3. Wrong-clock tD** | 모든 약물에 Eq 8-12 적용 | warfarin/aspirin/omeprazole/paclitaxel은 PD-rate-limited — PK k로 계산한 tD는 임상적으로 무의미 [T pp.251–254] |
| **E4. Linear-PK = linear-PD assumption** | dose-proportional AUC가 곧 dose-proportional response | methylprednisolone 16-1000 mg: AUC는 비례하나 lymphocyte response는 plateau 진입 [T pp.256–258] |
| **E5. Same-mechanism = same-clock assumption** | 동일 작용기전이면 같은 rate-limiting step | acenocoumarol(PD-limited, 15 h) vs phenprocoumon(PK-limited, ~5 days) — 같은 anticoagulant mechanism, 다른 지배 clock [T p.243] |

이 5가지를 외운 학습자는 이 세션의 모델링 결정을 거의 자동으로 방어할 수 있다.

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

Correct the erroneous phrase "naproxen 250 mg, Fig 8-3."

**Answer**  
Naproxen 500 mg oral, dental pain model, 1–8 h sampling, counterclockwise hysteresis, Fig 8-2. Fig 8-3 is a downstream pharmacodynamic schematic, not the naproxen figure. [T pp.234–236]

<!-- SELF-TEST -->
## Q6 [Application] Wrong-clock `tD`

Why is Eq 8-12 inappropriate for aspirin duration?

**Answer**  
Aspirin's plasma exposure disappears quickly, but thromboxane B₂ inhibition persists because target/platelet function recovery is slower. Duration is PD/target-replacement limited, not PK-rate-limited. [T p.251]

<!-- SELF-TEST -->
## Q7 [Application] Turnover vs effect compartment

A single-dose dataset fits both turnover and effect-compartment models equally well. What evidence should decide between them?

**Answer**  
Mechanistic prior about the response variable, broader dose range, repeated dosing/washout, perturbation of PK clock, and whether `EC50/ke0` remains biologically plausible. Fit quality alone is insufficient. [G pp.758–763; T pp.244–246]

<!-- SELF-TEST -->
## Q8 [Application] Linear PK ≠ linear PD

Methylprednisolone AUC is dose proportional from 16 to 1000 mg. Why does that not justify dose-proportional lymphocyte response?

**Answer**  
The response can enter the plateau region of the exposure-response curve; R&T's lymphocyte example shows little added PD response at high doses despite dose-proportional PK. R&T 본문(p.256)은 단호하게 명시한다 — *"Dose linearity in pharmacokinetics does not result in dose linearity in pharmacodynamics. That is almost never the case."* [T pp.256–258]

<!-- SELF-TEST -->
## Q9 [Boss dilemma]

A sponsor proposes: "Because phenprocoumon and acenocoumarol share the same anticoagulant mechanism, their response recovery should be governed by the same PD turnover half-life." Accept or reject? **Justify with the specific defensibility logic a 30-year reviewer would use.**

**Answer (Trade-off logic)**  
**Reject.** The same mechanism does not imply the same rate-limiting clock. Acenocoumarol has a shorter PK half-life (~15 h) and recovery becomes PD-clock limited (clotting factor turnover). Phenprocoumon has a much longer PK half-life (~5 days) and recovery becomes PK-clock limited (drug persistence dominates over the system clock). [T p.243]

이 차이가 임상·규제 차원에서 갖는 trade-off는 다음과 같다:
- **Sponsor의 단순화 채택 시**: 두 약물에 동일한 dose-titration step-up rule 적용 → phenprocoumon 누적 위험 또는 acenocoumarol 미달 dose. 어느 쪽이든 환자 안전·약효 부전 사고로 직결.
- **Mechanism-only justification의 규제적 위험**: 모델 선택 paragraph에서 "동일 mechanism이므로 동일 PD half-life"라는 추론은 design support 없이 데이터로 방어 불가능 → "insufficient justification for proposed dosing interval" 형태의 deficiency 위험. [교과서 외 실무 해석]
- **올바른 방어 논리**: 약물별 PK profile이 동일 PD system 위에서 어떤 clock을 활성화시키는지를 acenocoumarol vs phenprocoumon Fig 8-11 데이터로 직접 증명한 후, 각 약물별로 별도의 dose-duration model을 사용한다. 단일 PD half-life claim은 phenprocoumon에서 임상적으로 무의미하고 acenocoumarol에서만 유효하다.

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

## C. Professional moat — the 30-year veteran's 30-second diagnostic sequence

A 30-year pharmacometrics reviewer does not ask first whether the curve is smooth. They run a diagnostic sequence within the first 30 seconds of seeing the data. **이 sequence가 NONMEM을 실행할 수 있는 주니어 모델러와의 본질적 차이다 — 같은 데이터를 보고도 도달하는 결론의 정확성과 속도가 완전히 다르다.**

1. **Hysteresis 방향 (Mastery Anchor #1)**: plasma C vs response 산점도에서 loop 방향만으로 1차 분류 — counterclockwise는 distribution/turnover/active-metabolite, clockwise는 tolerance/feedback/enantiomer-specific. 30초 안에 첫 가설이 잡힌다.
2. **Response direction × tss 거동 (Mastery Anchor #3)**: 응답 방향과 tss의 dose-dependence 조합으로 4-model 칸 중 하나를 5분 안에 압축. PD5(Model 2)와 PD7(Model 4) side-by-side가 이 추론의 표준 reference.
3. **Post-trough rebound timing (Mastery Anchor #7)**: turnover fit이 나오자마자 회복 곡선의 타이밍을 본다. observed가 모델보다 빠르면 moderator/feedback 누락 신호. `$COV step` 결과를 기다리지 않는다.
4. **OFV 궤적 패턴 (Mastery Anchor #2)**: OFV가 30 iteration 동안 stuck-then-drop이면 즉시 (R0, kout) 재파라미터화로 옮겨간다. 이것은 cosmetic이 아니라 search geometry의 본질적 변경이다.
5. **Clock pair 비교 (Mastery Anchor #8)**: 새 약물의 duration 질문을 받으면 같은 mechanism을 공유하는 다른 약물의 PK profile을 함께 본다. acenocoumarol vs phenprocoumon이 표준 reference pair.

이 다섯 단계를 30초 안에 통과한 후에야 NONMEM 출력에 손을 댄다. 자동화된 도구는 단계 1, 4를 모방할 수 있지만 단계 2, 3, 5의 *데이터의 의미를 묻는 직관*은 데이터 외부의 mechanistic prior를 요구하므로 복제되지 않는다.

<!-- RECAP -->
## Final locked summary

Indirect response modeling is not "adding a delay." It is assigning delay to the correct causal clock. 따라서 locked workflow is:

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
| 5 | §2-6 | Card 6 — Irreversible Drug Action + Target Consumption | P | G&W Fig 3.47 [G p.256] or R&T Figs 8-20–8-21 [T pp.251–252] | G2, G5 | Reversible vs irreversible persistence is visually helpful, but the current Card 6 text already separates `drug-off` turnover from target/cell replacement. | Would reinforce target-consumption intuition. | REJECT — lower ROI than the clock and duration figures because Card 6 is not the session's apex decision point. |
| 6 | §2-7 | Card 7 — Turnover vs Effect Compartment Discrimination Crisis | P | G&W Fig 6.1 [G p.759] + G&W Table 6.1 [G p.763] | G2, G5 | The apex lesson is that two causal models can look nearly the same; the learner must inspect the fit/estimate equivalence, not only read the warning. | Makes "fit quality alone is insufficient" concrete by pairing curve similarity with similar `kout/ke0`. | KEEP |
| 7 | §2-8A | Card 8 — PK Clock vs PD Clock + Duration Formula Boundary | P | R&T Fig 8-11 [T p.243] | G2, G5 | PK vs PD rate-limiting is a comparative time-course concept; text alone can hide that the same mechanism can have different limiting clocks across drugs. | Learner sees acenocoumarol vs phenprocoumon as the canonical "same PD system, different slow clock" example. | KEEP |
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

(v1과 동일. Education UX Engineer role definition, PATCH MODE Splice Verification halt conditions, marker → component mapping table, page tag rendering rules, CSS variable requirements 모두 v1에서 carry-over. v2는 이 섹션 변경 없음.)

### B5. Audit Guardrails

Regression-prevention items for Session 11:

- Do not restore `naproxen 250 mg` or `Fig 8-3` as the naproxen anchor; the locked correction is naproxen 500 mg oral, dental pain, 1–8 h, counterclockwise hysteresis, Fig 8-2.
- Do not restore `ibuprofen Fig 8-4`; the locked figure is Fig 8-9.
- Do not restore `paclitaxel Fig 8-19`; Fig 8-19 is minoxidil and paclitaxel is Fig 8-22.
- Do not frame the minoxidil figure as topical; the locked example is single oral 25 mg with MAP-lowering context.
- Do not restore Zooparc® `5 mg or 25 mg q24h` as observed repeated-dose data; observed repeated-dose figures are 2.5 mg and 5 mg, while 25 mg/day is a projection/larger-study statement.
- Do not present NDA/IND/FDA reviewer/deficiency-letter wording as textbook-derived. Keep any such language explicitly labeled `[교과서 외 실무 해석]` or omit it.
- Do not restore an absolute "all measurable responses are delayed" claim without the direct-response caveat.
- Do not treat `tss` or peak shift as deterministic proof of mechanism; preserve the data-resolution, dose-range, PK-rate-limiting, and mechanistic-prior caveats.
- Do not round methylprednisolone 31/63 mg to 32/64 mg.
- Do not collapse `Kkill/kk` and `Kelim` in learner rendering; preserve the notation-disambiguation warning.
- Do not expand rosuvastatin, ranitidine, propranolol, or study-problem material beyond the locked CONTEXT/optional role.
- Do not add unapproved code blocks, new figures, new clinical examples, new numerical values, or new page tags.
- **v2 추가**: Mastery Anchor #1-#8은 모두 source-labeled augmentation으로, 새 fact·equation·page tag·figure를 추가하지 않는다. v2에서 이들을 확장하거나 신규 anchor를 추가할 때도 동일 원칙 적용.

### B6. Crucible Guardrails

- Crucible is not a raw content source at this stage.
- Preserve only already-adopted or explicitly allowed Grade A logic.
- Do not reintroduce omitted or rejected Crucible items.
- Do not convert speculative insight into textbook-derived fact.
- Grade A concepts are preserved only where Content Lock adopted them: tss first-order analogue blindness, ΔR/Emax semantic overload, Region 2/3 duration boundary, PK clock vs PD clock non-identifiability, single-dose duration-to-dose extension, hysteresis direction diagnosis, wrong-clock `tD`, and linear PK ≠ linear PD.
- **v2 추가**: v2의 Mastery Anchor 8개는 모두 Crucible v1 Grade A 항목 또는 ADOPT 항목에서 직접 도출됨. 신규 사실 도입 없음.

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

### B9. Zero-Omission Coverage Matrix (v2 update)

| Domain | Required item | Evidence in PART A | Status | Action |
|---|---|---|---|---|
| C1 Scope concepts | Turnover foundation, four models, tss/peak-shift, Imax/Emax semantics, initial estimates, irreversible action, effect compartment discrimination, PK/PD clock + duration | §2 Cards 1–8 | PRESENT | None |
| C1 Scope chapter role | Separate distribution delay, turnover delay, target consumption, and rate-limiting clocks | §1 Big Idea; §8 Final locked summary | PRESENT | None |
| C2 Required data anchors | G&W PD4/PD5/PD6/PD7/PD9 anchors retained where Content Lock v2 locked them | §2 Cards 3, 5, 7 and self-test Q3–Q4 | PRESENT_COMPRESSED | Do not expand beyond Content Lock. |
| C2 Required data anchors | R&T clinical anchors: digoxin, naproxen, midazolam, ibuprofen, warfarin, acenocoumarol/phenprocoumon, succinylcholine, minoxidil, aspirin/omeprazole/paclitaxel, methylprednisolone, rosuvastatin | §2 Cards 1, 4, 6, 8; §5; §7 | PRESENT_COMPRESSED | Kept at MUST/CONTEXT level. |
| C3 Audit MUST_FIX | (v1과 동일 — naproxen, ibuprofen, paclitaxel, minoxidil, Zooparc, regulatory, "all delayed", tss deterministic, methylprednisolone, K notation 모두 PRESENT) | (v1 위치 carry-over) | PRESENT | (v1과 동일) |
| C4 Audit T5 | T Key Relationships / direct-link vs delayed bridge / slower-clock author message | §1; §8; Card 8 | PRESENT | None |
| C5 Figure coverage | Approved KEEP figures #1, #2, #3, #6, #7, #8 | Six figure marker blocks in Cards 1, 2, 4, 7, 8 | PRESENT | Render only approved markers. |
| C5 Figure rights | No copyrighted textbook images embedded | Learner navigation note; PART B B2/B4 | PRESENT | Render pointers or distinct redraw only. |
| C6 Page tags | Existing `[G ...]` and `[T ...]` page tags preserved | PART A body | PRESENT | No new page tags fabricated. |
| C7 Crucible Grade A — basic adopted set | tss first-order analogue, ΔR/Emax semantics, Region 2 boundary, PK/PD clock non-identifiability, wrong-clock warning | Cards 3, 4, 8; §5; §7 | PRESENT_COMPRESSED | Preserved only as adopted logic. |
| **C7-v2 Crucible Grade A — mastery-anchor 5종 (v2 신규 강화)** | **PD4 Pool 1/2 r=0.9999 비식별성 (Wall #4) → Card 1 Anchor #2** | **Card 1 Mastery Anchor #2** | **PRESENT** | **v1에서 일반화되었던 reparameterization tip을 정량화된 비식별성 사례로 강화** |
| **C7-v2** | **OFV stuck-then-drop pattern (Intuition #2) → Card 1 Anchor #2** | **Card 1 Mastery Anchor #2** | **PRESENT** | **v1의 단순 trench tip을 진단 시그니처로 강화** |
| **C7-v2** | **Hysteresis 30-second direction diagnosis (Intuition #4) → Card 1 Anchor #1** | **Card 1 Mastery Anchor #1** | **PRESENT** | **v1의 Card 1.B 표 상태를 30초 진단 sequence로 명시화** |
| **C7-v2** | **Mirror-Slope Misread PD7 quantitative (T3 Tip 1) → Card 3 Anchor #4** | **Card 3 Mastery Anchor #4** | **PRESENT** | **v1의 abstract trench tip을 6,400U → 0.6 h⁻¹, 160,000U → 1.6 h⁻¹ 정량 시그니처로 강화** |
| **C7-v2** | **Post-trough rebound timing diagnosis (Intuition #1) → Card 8 Anchor #7** | **Card 8 Mastery Anchor #7** | **PRESENT** | **v1의 §8C 한 줄을 카드 단위 진단 anchor로 강화** |
| **C7-v2** | **5-minute structural model compression (Integration #1) → Card 2 Anchor #3** | **Card 2 Mastery Anchor #3** | **PRESENT** | **v1의 추상적 분류를 PD7 추론 절차 3단계로 명시화** |
| **C7-v2** | **PD6 quantitative equivalence Table (T2(c) Critical Blow) → Card 7 Anchor #6** | **Card 7 Mastery Anchor #6** | **PRESENT** | **v1의 한 줄 수치 언급을 ΔWRSS=2/ΔAIC=−1/kout=ke0=5.6 정량 표로 강화** |
| **C7-v2** | **Acenocoumarol vs Phenprocoumon canonical clock-pair (Wall #4 + Integration #4) → Card 8 Anchor #8** | **Card 8 Mastery Anchor #8** | **PRESENT** | **v1의 Card 8.A 표 한 행을 same-mechanism≠same-clock 결정판 reference로 강화** |
| C8 Deprecated draft regression | unsupported regulatory overclaims, wrong figure numbers, wrong naproxen/minoxidil/Zooparc framing, broad scope creep | PART B B5/B7 guardrails | PRESENT | Do not restore Step 1 text. |
| C9 Canonical body integrity | Content Lock v2 learner body spliced with approved markers; no broad rewrite | PART A §1–§8 | PRESENT | Only learner wrappers, labeled augmentations, and v2 Mastery Anchors added. |
| **C10-v2 Layout adjustments** | **Card 8 Section D (Rosuvastatin) → §5-5 footnote 이동** | **§5-5 Footnote** | **PRESENT** | **v1의 Card 8 흐름 어색함 해소; 본문 fact·page tag 동일 유지** |

### B10. Micro-Patch Log (v2)

v1과 비교하여 추가된 micro-patch:

1. **Big Idea 3-pillar 강화**: Card 1, 2, 3, 4, 5, 6, 7, 8의 Big Idea 직후 1단락의 mental model anchor를 추가. 기존 fact·equation·page tag·marker는 변경하지 않음.
2. **Card 8.D Rosuvastatin → §5-5 footnote 이동**: Card 8 흐름 정합성 향상. 본문 wording은 그대로 유지 (T pp.258–259 page tag 보존).
3. **Card 4.B에 R&T 명시 인용 추가**: *"Dose linearity in pharmacokinetics does not result in dose linearity in pharmacodynamics. That is almost never the case."* 라는 R&T p.256 직접 인용 추가. 이는 fabrication이 아닌 source-supported quote이며 Audit T3 Author Key Messages에서 INCLUDED_CORRECT로 검증된 메시지.
4. **§5 Recap → §5-Recap 5-error 구조화**: v1의 1단락 추상 메시지를 5개 표준 error 패턴으로 구조화. 모든 데이터·수치·page tag는 본문 cards에 이미 존재하는 것만 인용.
5. **§7 Q9 답변 확장**: Trade-off logic을 sponsor 시나리오 + 규제 위험 + 올바른 방어 논리 3단으로 확장. 새 fact·page tag·약물 추가 없음.
6. **§8C → 30-second diagnostic sequence**: 5단계로 구조화. 각 단계는 Mastery Anchor #1·#2·#3·#7·#8과 cross-reference.

No micro-patches modified scientific content. PART A v2 = PART A v1 + bounded, source-labeled augmentations.

### B11. Mastery Augmentation Log

#### v1 inserted (carry-over)

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
|---:|---|---|---|---|---|---|
| 1 | Card 1 | Practice Lens | YES | AUDIT_DERIVED | Clarifies direct-vs-delayed as resolution-sensitive before model selection. | Low |
| 2 | Card 2 | Mastery Note | YES | CRUCIBLE_DERIVED | Converts taxonomy into action-site and clock reasoning. | Low |
| 3 | Card 3 | Failure Mode | YES | AUDIT_DERIVED | Prevents deterministic overuse of tss/peak shift. | Low |
| 4 | Card 4 | Mastery Note | YES | CRUCIBLE_DERIVED | Prevents parameter-label comparison errors. | Low |
| 5 | Card 5 | Practice Lens | YES | CRUCIBLE_DERIVED | Frames manual estimates as mechanistic sanity checks. | Low |
| 6 | Card 6 | Failure Mode | YES | TEXTBOOK_DERIVED | Prevents drug-disappearance/effect-disappearance confusion. | Low |
| 7 | Card 7 | Practice Lens | YES | EXPERT_INFERENCE | Adds model-defensibility lens without new data or examples. | Medium |
| 8 | Card 8 | Failure Mode | YES | AUDIT_DERIVED | Prevents wrong-clock application of duration formula. | Low |

#### v2 newly inserted (Mastery Anchors)

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
|---:|---|---|---|---|---|---|
| 1 | Card 1 | Mastery Anchor | YES | CRUCIBLE_DERIVED (Intuition #4) | 30-second hysteresis direction diagnosis로 카드의 진단 reflex를 명시화. 기존 Card 1.B 표 상태를 sequence로 변환. | Low |
| 2 | Card 1 | Mastery Anchor | YES | CRUCIBLE_DERIVED (Intuition #2 + Wall #4) | OFV stuck-then-drop signature와 PD4 Pool 1/2 r=0.9999/CV% 4000 비식별성을 정량화하여 reparameterization의 정당성을 강화. | Low |
| 3 | Card 2 | Mastery Anchor | YES | CRUCIBLE_DERIVED (Integration #1) | 5-minute structural model compression의 PD7 추론 3단계로 4-model 분류 reflex를 표준화. | Low |
| 4 | Card 3 | Mastery Anchor | YES | CRUCIBLE_DERIVED (Tip 1) | Mirror-Slope Misread를 PD7 6,400U → 0.6 h⁻¹, 160,000U → 1.6 h⁻¹의 정량 시그니처로 강화. | Low |
| 5 | Card 5 | Mastery Anchor | YES | TEXTBOOK_DERIVED (PD5 Table 5.1) | Graphical workflow를 PD5 Compound A 4단계 절차로 구체화. PD5 Table 5.1 수치 인용 유지. | Low |
| 6 | Card 7 | Mastery Anchor | YES | CRUCIBLE_DERIVED (T2(c) Critical Blow) | PD6 Table 6.1 ΔWRSS/ΔAIC/kout=ke0/EC50 정량 표로 비식별성 결정타를 cement. | Low |
| 7 | Card 8 | Mastery Anchor | YES | CRUCIBLE_DERIVED (Intuition #1) | Post-trough rebound timing 진단을 카드 단위 anchor로 elevate. moderator/feedback 누락 신호로 명시. | Low |
| 8 | Card 8 | Mastery Anchor | YES | CRUCIBLE_DERIVED (Wall #4 + Integration #4) | Acenocoumarol vs Phenprocoumon을 same-mechanism≠same-clock canonical pair로 elevate. §7 Q9 trade-off 답변과 cross-reference. | Low |

#### Rejected v2 candidates

| Rejected candidate | Reason for rejection |
|---|---|
| Add new named clinical examples beyond G&W/R&T source universe | Would violate source boundary and require external support. |
| Add Mermaid/SVG code in v2 | Phase 4D decides content/markers only; Phase 5 renders visuals. |
| Add extra figure candidates for negative feedback, DRT, or target consumption | Rejected by v2.1 visual ROI/budget logic; v2 maintains v1 figure budget. |
| Add NONMEM `$DES` code blocks for taxonomy demonstration | G&W/R&T source universe does not include NONMEM control streams; would require [교과서 외 실무 해석] label and dilute source-boundary discipline. |
| Expand Card 8.D Rosuvastatin into a separate sub-card | Rejected. Rosuvastatin is exposure-response disconnect CONTEXT only; promoting it violates the locked Content Lock v2 MUST/CONTEXT separation. v2 instead moves it to §5-5 footnote where it belongs structurally. |

### B12. v1 → v2 Change Log (NEW)

이 섹션은 v2가 v1으로부터 무엇을 변경했는지에 대한 완전한 audit trail이다. v2는 다음 6가지만 변경했고, 그 외는 모두 v1과 동일하다.

| Change # | 위치 | 변경 종류 | v1 상태 | v2 상태 | Source authorization |
|---:|---|---|---|---|---|
| 1 | Card 1-8 Big Idea 직후 | augmentation | 단독 단락 | + 1단락 mental model anchor (3-pillar: 왜 중요/흐름 위치/체화 직관) | self-derived synthesis from existing Big Idea content; no new fact added |
| 2 | Card 1, 2, 3, 5, 7, 8 | new Mastery Anchor | 0개 | 8개 (Mastery Anchor #1-#8) | All from Crucible v1 Grade A or Audit T1/T3 INCLUDED_CORRECT |
| 3 | Card 8 Section D | relocation | Card 8.D 본문 | §5-5 footnote | Wording, page tag (T pp.258–259), source-boundary 모두 보존 |
| 4 | Card 4.B | source quote 추가 | indirect reference | 직접 인용 *"Dose linearity in pharmacokinetics... almost never the case."* | R&T p.256 직접 인용; Audit T3 INCLUDED_CORRECT |
| 5 | §5 Recap | structuring | 1단락 prose | 5-error 표 (E1-E5) | 모든 5개 error는 본문 cards에 이미 존재 |
| 6 | §7 Q9 답변 + §8C Professional Moat | expansion | 단순 답 / 5-question prose | trade-off 3단 logic / 5-step 30-second diagnostic sequence | Cross-references existing Mastery Anchors only |

#### Invariants preserved (v1 = v2)

- 모든 source page tags ([G ...], [T ...], [p.확인 필요]).
- 모든 equations and their numbering.
- 모든 figure marker blocks (B8 Splice Verification Table 그대로).
- 모든 [확인 필요] flags.
- 모든 [교과서 외 실무 해석] labels.
- PART B B1-B8의 모든 가드레일 (B5/B6/B7 forbidden restoration list).
- Compilation Contract (B1).
- Approved figure budget (5 pointers + 1 schematic; v2.1 Insertion Map identical).

v2의 모든 변경은 boundedness·adjacency·source-labeling 규칙 안에서 이루어졌다. v2 PART A에 있는 모든 추가 prose는 (a) Mastery Anchor 라벨이 명시되어 있거나, (b) 기존 Big Idea 직후 단일 단락 내에 위치하거나, (c) 표 구조화된 §5 Recap 내에 위치한다. PART A의 §1, §2 본문, §5 표, §7 Q1-Q8, §8A, §8B는 v1과 byte-level 동일하다.

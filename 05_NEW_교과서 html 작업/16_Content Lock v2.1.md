# 16_Content Lock v2.1 — Figure Marker Patch
## 임상 통합 캡스톤: 패턴 인식 · TDM · 질환 · 치료 의사결정

**Output mode declaration**: PATCH MODE

**Mode rationale**: Content Lock v2는 본문 재출력 시 text drift 위험이 있는 장문 문서이므로, v2 본문 전체를 재출력하지 않는다. 본 산출물은 Strategy Table + Briefs + Insertion Map만 제공한다. Phase 5 operator는 아래 marker block을 Content Lock v2 원문에 splice하여 v2.1을 생성한다.

**Telos**: 그림을 만들지 않고, 그림의 필요성·위치·역할만 결정한다. Mermaid/SVG/HTML rendering은 Phase 5로 이월한다.

**Image rights decision**: Scope Lock의 Image rights = None. 따라서 원문 교과서 figure는 삽입하지 않고, 필요한 경우 Pointer(P) 또는 visually distinct schematic brief(R/N)만 사용한다.

---

## 1. Figure Strategy Table — View (A) Reading-order Figure Plan

| # | Reading order | Location (§ + concept card) | Mode | Source figure (if any) | Trigger | Why text alone is insufficient | Expected learning gain | Decision |
|---:|---|---|---|---|---|---|---|---|
| F01 | 1 | §1 — Session Header & Roadmap / Capstone spine | N | None | G3, G4 | Text lists the chain, but the learner may not see that each block hands a specific decision object to the next block. | 전체 세션을 “model candidate → patient deviation → posterior parameter → dose decision → exposure report”의 단방향 clinical pharmacometrics pipeline으로 고정한다. | KEEP |
| F02 | 2 | §2.1 — Pattern-recognition decision workflow | P | G&W Fig.6.1 [p.423]; G&W Fig.6.12 [pp.465–466] | G1, G3, G5 | Baseline/time-delay/peak-shift/saturation checks and the Fig.6.12 workflow are sequential operations; prose alone can make them sound like a flat checklist. | pattern recognition을 “관찰 항목 목록”이 아니라 “후보 모델 축소 절차”로 읽게 한다. | KEEP |
| F03 | 3 | §2.2 — Peak-shift + saturation | P | G&W Fig.6.2 [p.424]; G&W Fig.6.3 [p.428] | G2, G5 | left/right shift, flat portion, and competing model options are spatial pattern differences; text alone invites deterministic over-reading. | “peak-shift direction = model class” 오류를 막고, directionality를 diagnostic signal로 위치시킨다. | KEEP |
| F04 | 4 | §2.4 — Bayesian objective function for individual TDM | P | G&W Fig.35.1 [pp.641–642]; R&T Fig.18-13 [pp.605–606] | G1, G2, G5 | Bayesian prior/likelihood weighting and sampling-time identifiability are difficult to internalize from equations alone. | posterior estimate를 “농도 하나의 산물”이 아니라 prior, concentration, timing geometry의 결합으로 읽게 한다. | KEEP |
| F05 | 5 | §2.5 — Disease/RF/Rd framework | R | R&T Fig.15-8 [p.453]; R&T Fig.15-9 [p.454] | G1, G2, G5 | `fe` and `RF` are two axes; prose makes learners collapse drug property and patient property into one “renal impairment” label. | Rd를 drug-specific `fe`와 patient-specific `RF`의 product decision으로 보는 구조가 고정된다. | KEEP |
| F06 | 6 | §2.7 — Hemodialysis coordinate plane | P | R&T Fig.15-18 [p.471]; R&T Fig.15-19 [p.473] | G1, G2, G5 | dialysis effectiveness is a continuous Vu·CLu·CLuD surface, not a verbal threshold; text alone reverts to hard-rule thinking. | half-life shortening과 amount removed를 분리하고, post-dialysis supplement 판단을 좌표 평면으로 읽게 한다. | KEEP |
| F07 | 7 | §2.9 — Loading dose vs maintenance dose | P | R&T Fig.18-5 [p.582] | G2, G5 | Fig.18-5 was a prior source of misreading as “accuracy”; learners need to inspect it as variability partition. | V, hepatic CL, renal CL, F의 explained/unaccounted variability를 dose-component confidence 문제로 연결한다. | KEEP |
| R01 | — | §2.8 — Target Concentration Strategy criteria | P candidate | R&T Table 18-5 [pp.595–596]; Table 18-6 [p.597] | G2, G5 | Important but table content is already summarized in the card. | Could reinforce interpretation gate, but would exceed pointer budget. | REJECT — budget lower than F02/F03/F04/F06/F07 |
| R02 | — | §2.10 — Missed / unequal / erratic dosing framework | P candidate | R&T Fig.18-11 [p.601]; Fig.18-12 [p.603] | G1, G5 | Superposition is visual, but the card already includes equations and worked examples. | Useful for Phase 5 optional expansion, not essential in v2.1 budget. | REJECT — pointer budget exhausted |
| R03 | — | §8 — PK15 closing bridge | P candidate | G&W Fig.15.1–15.3 [pp.546–548] | G3, weak G5 | PK15 is a closing reporting layer, not a §2 core mechanism card. | Would support safety-margin reporting but not structural understanding of the capstone spine. | REJECT — B-standard bridge; lower ROI |

---

## 2. Figure Strategy Table — View (B) Type-sorted Summary

**Pointers (P)**: F02, F03, F04, F06, F07 → 5 / max 5 for A-Critical budget.

**Schematics (R/N combined)**: F01, F05 → 2 / max 2 for A-Critical budget.

**Images (I)**: none → Image rights = None; no direct image insertion.

**Rejected after budget enforcement**: R01, R02, R03. These are educationally useful but not retained because they either repeat text already locked, exceed pointer budget, or belong to a lower-priority closing bridge.

---

## 3. Figure Briefs — KEEP Items Only

### F01 — New schematic: Capstone decision pipeline

- **Title**: Session 016 Capstone Spine — from data shape to exposure report
- **Mode**: N
- **Visual objective**: 5초 안에 “각 챕터가 다음 챕터에 넘기는 decision object”를 보이게 한다.
- **Core message**: Ch.6은 model candidate를, Ch.15는 patient deviation을, PK35는 posterior parameter를, Ch.18은 dose/monitoring decision을, PK15는 exposure/safety-margin report를 만든다.
- **Elements to include**:
  - Five horizontal blocks: Ch.6 Pattern Recognition → Ch.15 Disease/RF/Rd → PK35 Bayesian TDM → Ch.18 Dosing/Monitoring → PK15 Toxicokinetics
  - Under each block: output label only — model candidate, patient deviation, posterior parameter, dose decision, exposure report
  - One small caution strip: “implementation/regulatory translation requires label”
- **Elements to exclude**:
  - Drug examples, numeric anchors, source page tags, software names beyond the caution label
  - Any regulatory workflow diagram
- **Suggested rendering**: Mermaid flowchart
- **Caption**: Session 016은 독립 개념 묶음이 아니라, data shape에서 clinical exposure reporting으로 이어지는 단일 decision chain이다.
- **Alt text**: Five-step left-to-right pipeline connecting pattern recognition, disease adjustment, Bayesian estimation, therapeutic decision-making, and toxicokinetic reporting.
- **Source relation**: Newly designed

### F02 — Pointer: Pattern-recognition checklist and workflow

- **Source**: Gabrielsson & Weiner Ch.6, Fig.6.1 [p.423] and Fig.6.12 [pp.465–466]
- **Why this figure matters**: Fig.6.1 shows the initial visual grammar — baseline, time-delay, peak-shift, saturation, slopes. Fig.6.12 converts that grammar into a practical analysis workflow.
- **When to look**: After reading §2.1, before moving to §2.2.
- **Learner instruction**: Inspect Fig.6.1 first as the checklist, then Fig.6.12 as the decision workflow. Do not treat the checklist items as independent facts; follow how each observation narrows the next model question.

### F03 — Pointer: Peak-shift and competing model options

- **Source**: Gabrielsson & Weiner Ch.6, Fig.6.2 [p.424] and Fig.6.3 [p.428]
- **Why this figure matters**: Fig.6.2 makes the leftward vs rightward response-time movement visible. Fig.6.3 prevents the common error of mapping one pattern to one model by showing competing alternatives.
- **When to look**: Immediately after reading the table in §2.2.
- **Learner instruction**: Compare Case A, B, and C by looking only at timing of the trough and high-dose flattening. Then check Fig.6.3 to ask which competing models remain rather than choosing one model prematurely.

### F04 — Pointer: Bayesian estimation and sampling-time confidence

- **Source**: Gabrielsson & Weiner PK35, Fig.35.1 [pp.641–642]; Rowland & Tozer Ch.18, Fig.18-13 [pp.605–606]
- **Why this figure matters**: Fig.35.1 links patient-specific clearance variability to concentration-time behavior. Fig.18-13 shows why sampling time changes confidence in V vs CL estimates.
- **When to look**: After the “Sampling identifiability anchor” paragraph in §2.4.
- **Learner instruction**: First inspect how CL variability changes predicted concentration-time curves. Then inspect Fig.18-13 and ask whether the available sample is V-informative, CL-informative, or ambiguous.

### F05 — Redraw: Rd as a two-axis decision surface

- **Title**: Rd Framework — drug property `fe` × patient property `RF`
- **Mode**: R
- **Visual objective**: 5초 안에 renal dose adjustment가 “renal impairment label”이 아니라 `fe`와 `RF`의 interaction임을 보이게 한다.
- **Core message**: Maintenance adjustment becomes large only when the drug depends substantially on renal excretion and the patient’s renal function is meaningfully reduced.
- **Elements to include**:
  - X-axis: `RF` from normal to severe impairment
  - Y-axis or layered bands: `fe` low / moderate / high
  - Output zone: `Rd` close to 1 vs reduced
  - Annotation: `fe = drug property`, `RF = patient property`, `Rd = maintenance requirement`
  - Small callout: “LD is separate unless V changes”
- **Elements to exclude**:
  - Exact reproduction of textbook curves
  - Multiple drug examples
  - Cockcroft-Gault equation details
- **Suggested rendering**: inline SVG
- **Caption**: Rd는 신기능 저하 자체가 아니라 drug-specific `fe`와 patient-specific `RF`의 조합으로 maintenance requirement를 줄인다.
- **Alt text**: A two-axis conceptual surface showing renal function on one axis, fraction excreted unchanged on another, and maintenance dose requirement decreasing most when both renal dependence and impairment are high.
- **Source relation**: Redrawn from textbook concept

### F06 — Pointer: Hemodialysis fraction removed and supplement principle

- **Source**: Rowland & Tozer Ch.15, Fig.15-18 [p.471] and Fig.15-19 [p.473]
- **Why this figure matters**: Fig.15-18 shows why dialysis removal is a continuous function of Vu and CLu, not a hard threshold. Fig.15-19 connects removal during dialysis to the replacement-dose concept.
- **When to look**: After the “Locked correction” block in §2.7.
- **Learner instruction**: Inspect Fig.15-18 before applying any supplement rule. Ask whether the patient-drug pair sits in a region where dialysis removes clinically meaningful body amount during the session.

### F07 — Pointer: Variability partition for PK parameters

- **Source**: Rowland & Tozer Ch.18, Fig.18-5 [p.582]
- **Why this figure matters**: This figure was central to correcting the mistaken “V/CL prediction accuracy” reading. It should be inspected as a variability partition, not as a promise of dosing precision.
- **When to look**: Immediately after the “Corrected Fig.18-5 lock” paragraph in §2.9.
- **Learner instruction**: Read the figure by asking what fraction of variability is explained and what remains unaccounted. Then connect that to why renal CL may support stronger maintenance prediction than hepatic CL or F.

---

## 4. Insertion Map (PATCH MODE)

| # | Reading order | Anchor copied verbatim from Content Lock v2 | Insert position | Marker block ID |
|---:|---|---|---|---|
| F01 | 1 | `**§1 recap**: 이 세션은 “모델 선택 → 질환 보정 → 개인 추정 → 처방·monitoring → exposure reporting”의 단일 clinical pharmacometrics chain을 잠근다.` | after this anchor paragraph | MB-F01 |
| F02 | 2 | `§2.1은 plot-reading grammar이고, §2.2–§2.3은 그 grammar가 실제 ODE 후보로 내려가는 첫 번째 mechanistic bridge이다.` | after this anchor card, before `## §2.2` | MB-F02 |
| F03 | 3 | `**Trench-Level Tip**: Case B left-shift를 “kon이 큰 약물”로 외우지 말라. receptor on/off에서는 finite receptor pool 때문에 nadir가 빨라질 수 있고, turnover model에서도 loss stimulation이 유사한 pattern을 만들 수 있다.` | after this anchor card, before `## §2.3` | MB-F03 |
| F04 | 4 | `PK35 digoxin 사례는 CL/V/t½ 추정 사례이다. Loading dose 0.4 mg, maintenance 0.1–0.125 mg/day 같은 처방 문장은 교과서 직접 권고가 아니라 `[교과서 외 통합 추론 예시]`로만 다룬다. Sheiner 1977을 NONMEM의 직접 조상으로 단정하는 표현은 `[확인 필요]`이다.` | after this anchor card, before `## §2.5` | MB-F04 |
| F05 | 5 | `**Trench-Level Tip**: phenytoin처럼 albumin-bound low-extraction drug에서는 fu↑가 total concentration 해석을 망친다. total target을 그대로 쓰면 같은 unbound exposure를 과소평가할 수 있다.` | after this anchor card, before `## §2.6` | MB-F05 |
| F06 | 6 | `**Trench-Level Tip**: Phenobarbital의 dialysis half-life가 크게 줄어도 single 3 h session에서 body amount가 충분히 빠지지 않을 수 있다. half-life shortening and amount removed are not the same endpoint.` | after this anchor card, before `## §2.8` | MB-F06 |
| F07 | 7 | `**Trench-Level Tip**: “신부전이므로 LD도 줄인다”는 자동 규칙은 틀릴 수 있다. LD는 V 문제이고 MD는 CL 문제이다. 단, digoxin uremia처럼 V 자체가 변하는 예외는 따로 잡는다.` | after this anchor card, before `## §2.10` | MB-F07 |

---

## 5. Marker Block Registry

### MB-F01

```text
<!-- FIGURE_SCHEMATIC -->
Title: Session 016 Capstone Spine — from data shape to exposure report
Mode: N
Visual objective: 5초 안에 각 챕터가 다음 챕터에 넘기는 decision object를 보이게 한다.
Core message: Ch.6은 model candidate를, Ch.15는 patient deviation을, PK35는 posterior parameter를, Ch.18은 dose/monitoring decision을, PK15는 exposure/safety-margin report를 만든다.
Elements to include: Five horizontal blocks: Ch.6 Pattern Recognition → Ch.15 Disease/RF/Rd → PK35 Bayesian TDM → Ch.18 Dosing/Monitoring → PK15 Toxicokinetics; under each block, output label only: model candidate, patient deviation, posterior parameter, dose decision, exposure report; one small caution strip: implementation/regulatory translation requires label.
Elements to exclude: Drug examples, numeric anchors, source page tags, software names beyond the caution label, any regulatory workflow diagram.
Suggested rendering: Mermaid
Caption: Session 016은 독립 개념 묶음이 아니라, data shape에서 clinical exposure reporting으로 이어지는 단일 decision chain이다.
Alt text: Five-step left-to-right pipeline connecting pattern recognition, disease adjustment, Bayesian estimation, therapeutic decision-making, and toxicokinetic reporting.
Source relation: Newly designed
<!-- /FIGURE_SCHEMATIC -->
```

### MB-F02

```text
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner Ch.6, Fig.6.1 [p.423] and Fig.6.12 [pp.465–466]
Why this matters: Fig.6.1 shows the initial visual grammar — baseline, time-delay, peak-shift, saturation, slopes. Fig.6.12 converts that grammar into a practical analysis workflow.
When to look: after reading this card, before moving to §2.2
Learner instruction: Inspect Fig.6.1 first as the checklist, then Fig.6.12 as the decision workflow. Do not treat the checklist items as independent facts; follow how each observation narrows the next model question.
<!-- /FIGURE_POINTER -->
```

### MB-F03

```text
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner Ch.6, Fig.6.2 [p.424] and Fig.6.3 [p.428]
Why this matters: Fig.6.2 makes the leftward vs rightward response-time movement visible. Fig.6.3 prevents the common error of mapping one pattern to one model by showing competing alternatives.
When to look: immediately after reading this card
Learner instruction: Compare Case A, B, and C by looking only at timing of the trough and high-dose flattening. Then check Fig.6.3 to ask which competing models remain rather than choosing one model prematurely.
<!-- /FIGURE_POINTER -->
```

### MB-F04

```text
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner PK35, Fig.35.1 [pp.641–642]; Rowland & Tozer Ch.18, Fig.18-13 [pp.605–606]
Why this matters: Fig.35.1 links patient-specific clearance variability to concentration-time behavior. Fig.18-13 shows why sampling time changes confidence in V vs CL estimates.
When to look: after the Sampling identifiability anchor paragraph in this card
Learner instruction: First inspect how CL variability changes predicted concentration-time curves. Then inspect Fig.18-13 and ask whether the available sample is V-informative, CL-informative, or ambiguous.
<!-- /FIGURE_POINTER -->
```

### MB-F05

```text
<!-- FIGURE_SCHEMATIC -->
Title: Rd Framework — drug property fe × patient property RF
Mode: R
Visual objective: 5초 안에 renal dose adjustment가 renal impairment label이 아니라 fe와 RF의 interaction임을 보이게 한다.
Core message: Maintenance adjustment becomes large only when the drug depends substantially on renal excretion and the patient’s renal function is meaningfully reduced.
Elements to include: X-axis: RF from normal to severe impairment; Y-axis or layered bands: fe low, moderate, high; output zone: Rd close to 1 vs reduced; annotation: fe = drug property, RF = patient property, Rd = maintenance requirement; small callout: LD is separate unless V changes.
Elements to exclude: Exact reproduction of textbook curves, multiple drug examples, Cockcroft-Gault equation details.
Suggested rendering: SVG
Caption: Rd는 신기능 저하 자체가 아니라 drug-specific fe와 patient-specific RF의 조합으로 maintenance requirement를 줄인다.
Alt text: A two-axis conceptual surface showing renal function on one axis, fraction excreted unchanged on another, and maintenance dose requirement decreasing most when both renal dependence and impairment are high.
Source relation: Redrawn from textbook concept
<!-- /FIGURE_SCHEMATIC -->
```

### MB-F06

```text
<!-- FIGURE_POINTER -->
Source: Rowland & Tozer Ch.15, Fig.15-18 [p.471] and Fig.15-19 [p.473]
Why this matters: Fig.15-18 shows why dialysis removal is a continuous function of Vu and CLu, not a hard threshold. Fig.15-19 connects removal during dialysis to the replacement-dose concept.
When to look: after the Locked correction block in this card
Learner instruction: Inspect Fig.15-18 before applying any supplement rule. Ask whether the patient-drug pair sits in a region where dialysis removes clinically meaningful body amount during the session.
<!-- /FIGURE_POINTER -->
```

### MB-F07

```text
<!-- FIGURE_POINTER -->
Source: Rowland & Tozer Ch.18, Fig.18-5 [p.582]
Why this matters: This figure was central to correcting the mistaken V/CL prediction accuracy reading. It should be inspected as a variability partition, not as a promise of dosing precision.
When to look: immediately after the Corrected Fig.18-5 lock paragraph in this card
Learner instruction: Read the figure by asking what fraction of variability is explained and what remains unaccounted. Then connect that to why renal CL may support stronger maintenance prediction than hepatic CL or F.
<!-- /FIGURE_POINTER -->
```

---

## 6. Phase 5 Splicing Notes

1. Apply marker blocks in reading order F01 → F07.
2. Do not modify any Content Lock v2 body text, source page tags, equations, annotations, `[확인 필요]`, or `[p.확인 필요]` items.
3. Mode P markers remain callouts only; no textbook image should be embedded.
4. Mode R/N markers are briefs only. Phase 5 may render them as visually distinct Mermaid/SVG outputs, but must not reproduce copyrighted textbook figures.

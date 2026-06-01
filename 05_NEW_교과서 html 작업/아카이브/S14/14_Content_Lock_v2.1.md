# 14_Content Lock v2.1 — Figure Marker Patch
## Session 14 · Allometric Scaling: Inter-Species Extrapolation, Body Weight, and Age

**OUTPUT MODE:** PATCH MODE  
**Reason:** Content Lock v2 is long (>6,000 words; local word count ≈6,241). Full re-emission would create avoidable text drift. This v2.1 therefore provides **Strategy Table + Figure Briefs + Insertion Map only**. The unchanged Content Lock v2 body should be spliced with the markers below during Phase 5.

**Scope rule applied:** Image rights = None. Therefore, textbook figures are **not embedded**. Retained textbook visuals are handled as **POINTER (P)** callouts only. No Mermaid/SVG/HTML figure code is generated in this phase.

---

## 1. Figure Opportunity Scan — Decision Principles

Retained figures were selected only when removing the visual would measurably weaken structural understanding for a PhD-level learner. Decorative or merely available textbook figures were rejected. The chapter mode is **A-Critical**, so the strict figure budget is:

| Mode group | Budget | Used | Status |
|---|---:|---:|---|
| Pointer (P) | max 5 | 5 | PASS |
| Schematic (R/N combined) | max 2 | 2 | PASS |
| Image insert (I) | optional, only if rights permit | 0 | PASS |

---

## 2. Figure Strategy Table

### 2A. Reading-order Figure Plan — PRIMARY VIEW

| # | Reading order | Location (§ + concept card) | Mode | Source figure (if any) | Trigger | Why text alone is insufficient | Expected learning gain | Decision |
|---:|---|---|---|---|---|---|---|---|
| F1 | §1 후, §2 진입 전 | §1 Session Header & Roadmap | N | None | G3, G4 | 현재 §1의 concept map은 선형 관계를 보여주지만, C1–C5가 실제 판단 workflow로 어떻게 작동하는지 한 화면에서 압축하지 못한다. | 학습자가 `Y=a·BW^b → CL/V/time → Dedrick/dose/age caveat`를 하나의 spine으로 잡는다. | KEEP |
| F2 | C2 말미 | §2 C2 Clearance Exponent — `b=1` fallacy | P | R&T p.733, Fig.22-2 | G2, G5 | 7.7배 오류는 수식으로 읽을 수 있지만, `b=1`과 `b=0.75`가 log-log 공간에서 얼마나 벌어지는지는 시각적으로 확인해야 한다. | `0.75 vs 1.0` 차이가 작은 지수 차이가 아니라 human projection의 큰 차이라는 점을 고정한다. | KEEP |
| F3 | C2 말미 | §2 C2 Failure Conditions | P | G&W p.174, Fig.2.145 | G4, G5 | allometry failure는 문장으로는 단순 예외처럼 보인다. scalable vs less scalable의 prediction interval 차이를 보면 failure가 mechanism/data-quality signal임을 이해한다. | `allometry works`와 `allometry can fail badly`를 동시에 기억하게 한다. | KEEP |
| F4 | C3 말미 | §2 C3 Volume Exponent / §5 Pair 1 연결 | N | None | G2, G4 | `t1/2 ∝ BW^(d-b)`와 `kel ∝ BW^(b-d)`는 수식만으로는 서로 분리 암기되기 쉽다. | CL=flow, V=extent, time=V/CL, rate constant=CL/V의 방향성을 한 번에 분리한다. | KEEP |
| F5 | C4 말미 | §2 C4 Elementary Dedrick / PK28 | P | G&W PK28 p.613, Fig.28.2 | G1, G5 | Kallynochron은 normalized axes를 실제 curve collapse로 봐야 의미가 생긴다. 텍스트만으로는 “왜 같은 곡선이 되는가”가 남는다. | elementary Dedrick이 per-kg time normalization이라는 점을 시각적으로 체화한다. | KEEP |
| F6 | C4 말미 | §2 C4 Complex Dedrick / PK29 | P | G&W PK29 p.619, Fig.29.3 | G1, G5 | Complex Dedrick은 $d\neq1$가 들어가므로 수식 부담이 크다. raw fit과 transformed superposition을 함께 봐야 전환 이유가 보인다. | Apolysichron이 `d`를 반영한 generalized physiological time scale임을 확인한다. | KEEP |
| F7 | C5 말미 | §2 C5 Pediatric/elderly context | P | R&T p.430, Fig.14-20 | G3, G5 | C5의 age adjustment 경고는 문장만으로는 `BW^0.75`가 충분하지 않은 이유를 약하게 전달한다. | 소아·노인 dose adjustment가 BW allometry 위에 age/function layer를 더해야 한다는 점을 고정한다. | KEEP |

### 2B. Type-sorted Summary — AUXILIARY VIEW

**Pointers (P):** F2, F3, F5, F6, F7 → 5/5, PASS  
**Schematics (R/N):** F1, F4 → 2/2, PASS  
**Images (I):** none → rights rule respected

### 2C. Rejected / Deferred Candidates

| Candidate | Source | Rejection / deferral reason |
|---|---|---|
| Physiologic origin figure | G&W Fig.2.144 or R&T Fig.22-1 | Important, but C1 text plus F1 spine schematic covers the role of physiologic exponent. Direct fallacy/failure/Dedrick/age visuals have higher ROI under budget. |
| Core exponent table | G&W Table 2.22 or R&T Fig.22-4 | Strong for b/d distinction, but F4 schematic directly targets the same confusion with less table-reading burden. |
| Dose-variability figures | G&W Fig.2.151 / Fig.2.153 / Fig.2.154 | Useful for FIH caution, but Content Lock v2 already corrected the FIH overclaim. Including these would shift emphasis from allometric spine to dose-justification uncertainty. |
| R&T renal maturation visual | R&T Fig.14-7 / Table 14-4 | Highly relevant, but F7 Fig.14-20 more directly matches C5’s maintenance-dose message. Use as optional expansion only if Phase 5 increases pointer budget. |
| Protein-binding boundary visual | R&T Fig.22-9 / Table 22-1 | Important boundary condition, but C2 TRENCH text is sufficient for this session. Retain for a future protein binding / unbound clearance session. |
| R&T BSA nuance | R&T Fig.22-3 | Useful for Pair 3, but not needed once C5 and §5 already frame BSA as a clinical approximation rather than a replacement for allometry. |

---

## 3. Figure Briefs — KEEP Only

### F1 — NEW SCHEMATIC

- **Title:** Allometric spine: variable type → exponent → time/dose consequence
- **Visual objective:** 5초 안에 C1–C5가 하나의 workflow라는 점을 보이게 한다.
- **Core message:** `Y=a·BW^b`는 독립 수식이 아니라 CL, V, time, Dedrick, equal-AUCu dose translation을 연결하는 spine이다.
- **Elements to include:**
  - Start node: `Y=a·BW^b`
  - Branch 1: `CL / flow / b≈0.75`
  - Branch 2: `V / extent / d≈1`
  - Derived nodes: `t1/2 ∝ BW^(d-b)`, `kel ∝ BW^(b-d)`
  - Application nodes: `Dedrick superposition`, `Equal-AUCu dose backbone`
  - Caveat gates: `fu`, `metabolism route`, `nonlinear PK`, `functional age`
- **Elements to exclude:** regulatory agency logos, unsupported ICH/FDA claims, detailed PBPK/QSP submodels, animal cartoons.
- **Suggested rendering:** Mermaid flowchart
- **Caption:** Allometric scaling should be read as a connected decision spine, not as five isolated formulas.
- **Alt text:** A flowchart begins with `Y=a·BW^b`, branches to CL and V exponents, then connects to half-life, rate constant, Dedrick plots, and dose translation caveats.
- **Source relation:** Newly designed

### F2 — POINTER

- **Source:** Rowland & Tozer 5e, Ch.22, p.733, Fig.22-2
- **Why this figure matters:** This is the cleanest source-side visual for the `b=1` versus `b=0.75` error. It makes the 7.7-fold mouse-human gap visible rather than merely calculable.
- **When to look:** After reading C2 Plausible Fallacy and before moving to C2 Failure Conditions.
- **Learner instruction:** Compare the `b=1` and `b=0.75` projections at the human body-weight end. Then restate in one sentence why mg/kg linear scaling overestimates human CL/dose in target-AUC logic.

### F3 — POINTER

- **Source:** Gabrielsson & Weiner 5e, §2.10.3, p.174, Fig.2.145
- **Why this figure matters:** The figure separates compounds where allometry gives a useful prediction from compounds where prediction intervals become dangerously wide. This directly supports the C2 message that failure is often a mechanism/data-quality signal, not just noise.
- **When to look:** After reading C2 Failure Conditions.
- **Learner instruction:** Identify which panel represents a scalable compound and which represents a less scalable compound. Then map the broad prediction interval back to at least two C2 failure triggers.

### F4 — NEW SCHEMATIC

- **Title:** Flow vs extent split: why $b$ and $d$ cannot be swapped
- **Visual objective:** 5초 안에 CL, V, half-life, and $k_{el}$의 방향성을 분리한다.
- **Core message:** CL은 flow라서 $b≈0.75$, V는 extent라서 $d≈1$이며, 두 지수의 차이가 time과 rate constant를 반대 방향으로 만든다.
- **Elements to include:**
  - Two-column layout: `CL = a·BW^b` vs `V = c·BW^d`
  - Labels: `flow/rate` vs `space/extent`
  - Derived arrows: `V/CL → t1/2 ∝ BW^(d-b)`; `CL/V → kel ∝ BW^(b-d)`
  - Warning strip: `Do not use d=1 for CL scaling`; `Do not use b=0.75 for V scaling without evidence`
- **Elements to exclude:** new animal examples, extra species-specific numbers, study-problem calculations.
- **Suggested rendering:** CSS comparison card or Mermaid graph
- **Caption:** The clinical error is not forgetting 0.75; it is swapping a flow exponent and a volume exponent.
- **Alt text:** A two-column diagram contrasts clearance as flow with exponent 0.75 and volume as extent with exponent 1, then shows half-life and elimination rate constant as opposite ratios.
- **Source relation:** Newly designed

### F5 — POINTER

- **Source:** Gabrielsson & Weiner 5e, Case Study PK28, p.613, Fig.28.2
- **Why this figure matters:** It is the best learner-facing view of elementary Dedrick superposition for methadone. The learner sees that normalization is meant to collapse mouse, rat, and human concentration-time curves onto a shared physiological time scale.
- **When to look:** After reading C4 Data Anchor — PK28 and before reading C4 limitations.
- **Learner instruction:** Focus on the axis transformations, not only the curve shapes. Ask what assumption about $d$ is required for this elementary version to work.

### F6 — POINTER

- **Source:** Gabrielsson & Weiner 5e, Case Study PK29, p.619, Fig.29.3
- **Why this figure matters:** This is the final visual proof of why Complex Dedrick is needed when $d\neq1$ and multicompartment scaling enters. It connects the allometric parameter set to curve superposition.
- **When to look:** After F5 and after reading C4 Complex Dedrick / PK29 material.
- **Learner instruction:** Compare this figure mentally against the elementary Dedrick logic. Identify where the $BW^d$ normalization changes the concentration axis and why that matters for compound X.

### F7 — POINTER

- **Source:** Rowland & Tozer 5e, Ch.14, p.430, Fig.14-20
- **Why this figure matters:** It visually prevents the common mistake that $BW^{0.75}$ alone solves pediatric/elderly dosing. It shows maintenance-dose fraction varying across age, which is exactly the C5 caveat.
- **When to look:** After reading C5 Pediatric and elderly context and before the C5 recap.
- **Learner instruction:** Track how dose fraction changes from infancy through old age. Then state why functional age and renal/hepatic function must sit on top of BW allometry.

---

## 4. Insertion Map (PATCH MODE)

| # | Reading order | Anchor (exact heading or first ≥40 chars from Content Lock v2) | Insert position | Marker block (full text) |
|---:|---|---|---|---|
| F1 | §1 후, §2 진입 전 | `## §1 — Session Header & Roadmap` | before next §heading (`## §2 — Concept Anatomy Cards`) | `<!-- FIGURE_SCHEMATIC --><br>Title: Allometric spine: variable type → exponent → time/dose consequence<br>Mode: N<br>Visual objective: 5초 안에 C1–C5가 하나의 workflow라는 점을 보이게 한다.<br>Core message: Y=a·BW^b는 독립 수식이 아니라 CL, V, time, Dedrick, equal-AUCu dose translation을 연결하는 spine이다.<br>Elements to include: Start node Y=a·BW^b; CL / flow / b≈0.75; V / extent / d≈1; t1/2 ∝ BW^(d-b); kel ∝ BW^(b-d); Dedrick superposition; Equal-AUCu dose backbone; caveat gates fu, metabolism route, nonlinear PK, functional age.<br>Elements to exclude: regulatory agency logos, unsupported ICH/FDA claims, detailed PBPK/QSP submodels, animal cartoons.<br>Suggested rendering: Mermaid<br>Caption: Allometric scaling should be read as a connected decision spine, not as five isolated formulas.<br>Alt text: A flowchart begins with Y=a·BW^b, branches to CL and V exponents, then connects to half-life, rate constant, Dedrick plots, and dose translation caveats.<br>Source relation: Newly designed<br><!-- /FIGURE_SCHEMATIC -->` |
| F2 | C2 말미 | `CL의 $b\approx0.75$는 시간당 처리량의 지수다. 그럼 V는 왜 $d\approx1$인가? 답은 V가 “흐름”이 아니라 “공간”이기 때문이다.` | after this anchor card | `<!-- FIGURE_POINTER --><br>Source: Rowland & Tozer 5e, Ch.22, p.733, Fig.22-2<br>Why this matters: This is the cleanest source-side visual for the b=1 versus b=0.75 error. It makes the 7.7-fold mouse-human gap visible rather than merely calculable.<br>When to look: After reading C2 Plausible Fallacy and before moving to C2 Failure Conditions.<br>Learner instruction: Compare the b=1 and b=0.75 projections at the human body-weight end. Then restate in one sentence why mg/kg linear scaling overestimates human CL/dose in target-AUC logic.<br><!-- /FIGURE_POINTER -->` |
| F3 | C2 말미 | `CL의 $b\approx0.75$는 시간당 처리량의 지수다. 그럼 V는 왜 $d\approx1$인가? 답은 V가 “흐름”이 아니라 “공간”이기 때문이다.` | after this anchor card, immediately after F2 | `<!-- FIGURE_POINTER --><br>Source: Gabrielsson & Weiner 5e, §2.10.3, p.174, Fig.2.145<br>Why this matters: The figure separates compounds where allometry gives a useful prediction from compounds where prediction intervals become dangerously wide. This directly supports the C2 message that failure is often a mechanism/data-quality signal, not just noise.<br>When to look: After reading C2 Failure Conditions.<br>Learner instruction: Identify which panel represents a scalable compound and which represents a less scalable compound. Then map the broad prediction interval back to at least two C2 failure triggers.<br><!-- /FIGURE_POINTER -->` |
| F4 | C3 말미 | `**C3 핵심:** $d\approx1$은 분포 공간이 체중에 비례한다는 뜻이고, $b<d$는 큰 동물에서 제거 fraction이 느려진다는 뜻이다. $d-b$와 $b-d$를 동시에 볼 수 있어야 half-life와 rate constant를 같은 구조로 이해한다.` | after this anchor card | `<!-- FIGURE_SCHEMATIC --><br>Title: Flow vs extent split: why b and d cannot be swapped<br>Mode: N<br>Visual objective: 5초 안에 CL, V, half-life, and kel의 방향성을 분리한다.<br>Core message: CL은 flow라서 b≈0.75, V는 extent라서 d≈1이며, 두 지수의 차이가 time과 rate constant를 반대 방향으로 만든다.<br>Elements to include: Two-column layout CL = a·BW^b vs V = c·BW^d; labels flow/rate vs space/extent; arrows V/CL → t1/2 ∝ BW^(d-b); CL/V → kel ∝ BW^(b-d); warning strip Do not use d=1 for CL scaling and Do not use b=0.75 for V scaling without evidence.<br>Elements to exclude: new animal examples, extra species-specific numbers, study-problem calculations.<br>Suggested rendering: CSS-card<br>Caption: The clinical error is not forgetting 0.75; it is swapping a flow exponent and a volume exponent.<br>Alt text: A two-column diagram contrasts clearance as flow with exponent 0.75 and volume as extent with exponent 1, then shows half-life and elimination rate constant as opposite ratios.<br>Source relation: Newly designed<br><!-- /FIGURE_SCHEMATIC -->` |
| F5 | C4 말미 | `**C4 핵심:** Dedrick superposition은 curve-fitting 장식이 아니라 CL exponent와 V exponent를 동시에 검증하는 diagnostic이다. Elementary가 실패하면 “plot이 안 예쁜 것”이 아니라 “d=1 가정이 깨졌을 가능성”을 먼저 본다.` | after this anchor card | `<!-- FIGURE_POINTER --><br>Source: Gabrielsson & Weiner 5e, Case Study PK28, p.613, Fig.28.2<br>Why this matters: It is the best learner-facing view of elementary Dedrick superposition for methadone. The learner sees that normalization is meant to collapse mouse, rat, and human concentration-time curves onto a shared physiological time scale.<br>When to look: After reading C4 Data Anchor — PK28 and before reading C4 limitations.<br>Learner instruction: Focus on the axis transformations, not only the curve shapes. Ask what assumption about d is required for this elementary version to work.<br><!-- /FIGURE_POINTER -->` |
| F6 | C4 말미 | `**C4 핵심:** Dedrick superposition은 curve-fitting 장식이 아니라 CL exponent와 V exponent를 동시에 검증하는 diagnostic이다. Elementary가 실패하면 “plot이 안 예쁜 것”이 아니라 “d=1 가정이 깨졌을 가능성”을 먼저 본다.` | after this anchor card, immediately after F5 | `<!-- FIGURE_POINTER --><br>Source: Gabrielsson & Weiner 5e, Case Study PK29, p.619, Fig.29.3<br>Why this matters: This is the final visual proof of why Complex Dedrick is needed when d≠1 and multicompartment scaling enters. It connects the allometric parameter set to curve superposition.<br>When to look: After F5 and after reading C4 Complex Dedrick / PK29 material.<br>Learner instruction: Compare this figure mentally against the elementary Dedrick logic. Identify where the BW^d normalization changes the concentration axis and why that matters for compound X.<br><!-- /FIGURE_POINTER -->` |
| F7 | C5 말미 | `**C5 핵심:** C5의 수식은 equal unbound AUC를 맞추는 allometric backbone이다. FIH dose justification이나 pediatric/elderly dosing에서는 이 backbone 위에 functional age, renal/hepatic function, body composition, binding, PD metric, safety margin을 얹어야 한다.` | after this anchor card | `<!-- FIGURE_POINTER --><br>Source: Rowland & Tozer 5e, Ch.14, p.430, Fig.14-20<br>Why this matters: It visually prevents the common mistake that BW^0.75 alone solves pediatric/elderly dosing. It shows maintenance-dose fraction varying across age, which is exactly the C5 caveat.<br>When to look: After reading C5 Pediatric and elderly context and before the C5 recap.<br>Learner instruction: Track how dose fraction changes from infancy through old age. Then state why functional age and renal/hepatic function must sit on top of BW allometry.<br><!-- /FIGURE_POINTER -->` |

---

## 5. Phase 5 Operator Notes

1. Apply the markers in reading order F1 → F7.
2. Do not alter the Content Lock v2 body text, source page tags, equations, `[확인 필요]` flags, or existing markers.
3. For repeated anchors (F2/F3 and F5/F6), insert both markers sequentially in the listed order.
4. No textbook image should be embedded. POINTER markers instruct the learner to inspect the original source figure.
5. For F1 and F4, Phase 5 may render a new Mermaid/CSS-card schematic, but must not reproduce textbook layout, labels, or artwork.


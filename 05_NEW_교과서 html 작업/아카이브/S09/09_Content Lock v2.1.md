# 09_Content Lock v2.1 — Figure Marker Patch

**Role**: Visual Pedagogy Editor  
**Output mode**: **PATCH MODE**  
**Reason**: Content Lock v2 is long (>6,000 words). Re-emitting the full body would increase text-drift risk. This v2.1 deliverable therefore provides Strategy Table + Figure Briefs + Insertion Map only.  
**Phase boundary**: 그림을 만들지 않는다. Mermaid/SVG/HTML code를 생성하지 않는다. 여기서는 “어떤 그림이, 왜, 어디에 필요한가”만 결정한다.  
**Image rights**: None → Mode I 금지. Textbook figures are handled as POINTER only.  
**Budget applied**: A-Critical → Pointer max 5; Schematic (R/N combined) max 2; Image none.

---

# 1. Figure Opportunity Scan — Executive Decision

Content Lock v2의 구조적 이해를 실제로 강화하는 figure slot은 총 7개로 확정한다.

```text
KEEP = 7 markers
- Pointer (P): 5/5 budget used
- New schematic (N): 2/2 budget used
- Redraw (R): 0/2 budget used
- Image insert (I): 0, because Image rights = None
```

핵심 선택 원칙은 다음과 같다.

1. **M1 Turnover**에는 `kin`과 `kout` 조작의 비대칭성을 직접 보게 하는 pointer가 필요하다.
2. **M2 Protein/Antibody PK**는 textbook figure들이 흩어져 있으므로, 전체 ADME gate는 새 schematic으로 통합하고, FcRn salvage만 source figure pointer로 둔다.
3. **M3/M5 TMDD 4-phase와 MM boundary**는 textbook의 원그림 학습 가치가 높으므로 pointer가 우선이다.
4. **M4 Full TMDD**는 source topology pointer와, dataset richness가 ODE term 식별성을 어떻게 높이는지 보여주는 새 schematic이 모두 필요하다.
5. Lymphatic recovery, renal sieving, table-heavy Vd/SC bioavailability 자료는 모두 중요하지만 budget상 M2 gate schematic에 흡수한다.

---

# 2. Figure Strategy Table

## 2A. Reading-order Figure Plan

| # | Reading order | Location (§ + concept card) | Mode | Source figure (if any) | Trigger | Why text alone is insufficient | Expected learning gain | Decision |
|---:|---|---|---|---|---|---|---|---|
| 1 | §2 → M1 | Card M1 — Turnover Paradigm | P | G&W p.97, Fig.2.70 | G2, G5 | `kin` 변화와 `kout` 변화가 모두 “농도 변화”처럼 읽히기 쉽다. 곡선으로 level 변화와 time-to-steady-state 변화를 동시에 봐야 한다. | `kin`은 level만, `kout`은 level + time scale을 함께 바꾼다는 비대칭성 고정. | KEEP |
| 2 | §2 → M2 | Card M2 — Protein/Antibody Distinctive PK | N | none | G1, G3, G4 | M2는 Vd 제한, lymphatic input, renal cutoff, proteolysis/RME, FcRn salvage가 분산적으로 제시되어 있어 텍스트만으로는 “gate system”이 형성되기 어렵다. | mAb PK를 four-gate ADME map으로 압축해 sc profile, Vd, renal disease, FcRn half-life를 한 프레임에 배치. | KEEP |
| 3 | §2 → M2 | Card M2 — FcRn and FcγR | P | R&T p.709, Fig.21-5 | G1, G5 | FcRn salvage는 endosome pH, binding, recycling, degradation avoidance가 순환 구조라서 문장만으로는 방향성이 흐려진다. | “mAb half-life ≈ 21 days”가 단순 느린 제거가 아니라 salvage/recycling의 결과임을 시각화. | KEEP |
| 4 | §2 → M2 | Card M2 — lymphatic absorption route | P | R&T p.718, Fig.21-13 | G1, G5 | Blood capillary vs lymphatic route는 중요하지만 M2 gate schematic이 이를 통합할 수 있다. | 별도 pointer를 두면 M2가 과도하게 absorption 중심으로 쏠릴 위험이 있다. | REJECT — covered by #2; pointer budget 보존 |
| 5 | §2 → M2 | Card M2 — lymph recovery trend | P | R&T p.720, Fig.21-16 | G5 | Figure 자체는 ESSENTIAL이지만 v2는 이미 “directionality only, no 150 kDa extrapolation”을 명시한다. | 별도 pointer는 150 kDa 정량 외삽 유혹을 다시 키울 수 있다. | REJECT — directionality는 #2 + 본문으로 충분 |
| 6 | §2 → M3 | Card M3 — TMDD 4-Phase Profile | P | R&T p.712, Fig.21-9; supporting: G&W p.610, Fig.27.7 | G1, G2, G5 | Phase A–D는 시간 순서가 아니라 concentration hierarchy라는 점을 텍스트만으로는 쉽게 놓친다. | `Kd`, `Km`, saturation boundary와 four-phase curve를 한 번에 연결. | KEEP |
| 7 | §2 → M4 | Card M4 — Full TMDD Model | P | R&T p.711, Fig.21-8; supporting: G&W p.604, Fig.27.2 | G1, G5 | Full TMDD는 ligand, target, complex, sink가 얽힌 topology이므로 ODE 문장만으로는 state relationship이 흐려진다. | ligand central/tissue, free target, complex, elimination/sink의 구조적 연결을 고정. | KEEP |
| 8 | §2 → M4 | Card M4 — Identifiability and data richness | N | none; based on G&W Table 27.2 concept | G3, G4 | CV% hierarchy는 표로 읽히지만, “어떤 관측값이 어떤 ODE term을 가르치는가”는 표만으로 즉시 보이지 않는다. | Dataset I/II/III → observable L/R/RL → `kon/koff/ke(RL)` precision 개선의 causal chain 체화. | KEEP |
| 9 | §2 → M5 | Card M5 — MM approximation boundary | P | G&W p.609, Fig.27.6 | G2, G5 | “high-dose fit은 괜찮고 low-dose에서 무너짐”은 TMDD/MM 판단의 critical blow인데, 수치 문장만으로는 residual pattern의 구조가 덜 남는다. | `Km=3.7` vs `0.03` bias가 왜 low-concentration extrapolation 문제인지 즉시 확인. | KEEP |
| 10 | §2 → M5 | Card M5 — concentration regimes / clearance-vs-C | P | G&W p.604, Fig.27.3 | G2, G5 | Useful but overlaps with #6 and #9. | Fig.21-9와 Fig.27.6 조합이 더 높은 learning ROI. | REJECT — pointer budget 초과 |
| 11 | §5 → Pair 3 | `Kd` vs `Km` comparison | N/R | none | G2 | Pair table already separates definition and meaning clearly. | Visual card would be decorative relative to existing table. | REJECT — already clear |
| 12 | §8 → Professional moat | Diagnostic GOF workflow | N | none | G4 | Interesting, but it would add workflow content beyond current Content Lock body. | Better deferred to Phase 5 interactive/diagnostic module, not Content Lock marker. | REJECT — scope creep risk |

## 2B. Type-sorted Summary

```text
Pointers (P): #1, #3, #6, #7, #9 → 5/5 used
Schematics (R/N): #2, #8 → 2/2 used
Images (I): none → Image rights = None
Rejected: #4, #5, #10, #11, #12
```

---

# 3. Figure Briefs — KEEP Only

## Figure #1 — Mode P

- **Source**: Gabrielsson & Weiner 5e, p.97, Fig.2.70 — impact of changing turnover rate `Rin/kin` vs fractional turnover rate `kout`.
- **Why this figure matters**: M1의 핵심은 `kin`과 `kout`이 같은 “rate”가 아니라 서로 다른 축을 움직인다는 점이다. Fig.2.70은 steady-state level과 time-to-steady-state가 어떻게 다르게 반응하는지 한 번에 보여준다.
- **When to look**: M1의 “B. Intuition: faucet vs drain”을 읽은 직후.
- **Learner instruction**: 왼쪽 패널에서는 새 steady-state level만 바뀌는지 확인하라. 오른쪽 패널에서는 level과 `Tss`가 동시에 바뀌는지 확인하라.

## Figure #2 — Mode N

- **Title**: Protein/Antibody PK Four-Gate Map
- **Visual objective**: 5초 안에 mAb PK가 “큰 분자라서 느림”이 아니라 four physiological gates의 결과임을 보게 한다.
- **Core message**: mAb PK는 restricted distribution, lymphatic input, size-dependent elimination, FcRn rescue가 동시에 작동하는 gate system이다.
- **Elements to include**:
  - 중심 노드: `mAb / protein drug`
  - Gate 1: Distribution gate — small `Vss`, plasma/interstitial restriction
  - Gate 2: Absorption gate — sc/im → lymphatic route → delayed input
  - Gate 3: Elimination gate — renal cutoff for small proteins; proteolysis/RME for larger proteins
  - Gate 4: Rescue gate — FcRn salvage → degradation avoidance → longer apparent half-life
  - Downstream interpretation nodes: terminal slope caution; renal disease caution; TMDD curve-reading caution
- **Elements to exclude**:
  - Full numerical tables
  - individual drug lists
  - 150 kDa mAb lymph recovery percentage extrapolation
  - antibody structural Fab/Fc detail beyond FcRn-facing label
- **Suggested rendering**: Mermaid flowchart
- **Caption**: Protein/antibody PK should be read as a set of physiological gates before interpreting terminal slope or nonlinear clearance.
- **Alt text**: A central mAb node branches into distribution, absorption, elimination, and FcRn rescue gates, each leading to a specific PK interpretation caution.
- **Source relation**: Newly designed

## Figure #3 — Mode P

- **Source**: Rowland & Tozer 5e, p.709, Fig.21-5 — FcRn recycling protects IgG/mAbs from degradation.
- **Why this figure matters**: FcRn salvage is a cycle, not a single clearance parameter. The figure makes clear why IgG/mAbs can avoid lysosomal degradation and return to circulation.
- **When to look**: M2의 “C. FcRn and FcγR”를 읽은 직후.
- **Learner instruction**: Endosome 안에서 FcRn binding이 일어나는 위치와, 어떤 분획이 degradation으로 가지 않고 recycling되는지 따라가라. “half-life ≈ 21 days”를 단순 terminal slope가 아니라 recycling outcome으로 읽어라.

## Figure #4 — Mode P

- **Source**: Rowland & Tozer 5e, p.712, Fig.21-9 — four-phase TMDD profile with `Km`/`Kd`; supporting cross-check: Gabrielsson & Weiner 5e, p.610, Fig.27.7.
- **Why this figure matters**: M3의 난점은 Phase A–D를 시간 구간으로만 외우는 것이다. 이 figure는 phase가 concentration regime과 target saturation state에 의해 바뀐다는 점을 보여준다.
- **When to look**: M3 전체를 읽은 직후, M5로 넘어가기 전.
- **Learner instruction**: Phase A–D를 순서대로 보되, 각 phase를 “시간”이 아니라 ligand concentration이 `Kd`, `Km`, `R0` 관련 boundary를 지나가는 상태로 해석하라.

## Figure #5 — Mode P

- **Source**: Rowland & Tozer 5e, p.711, Fig.21-8 — Mager-Jusko general TMDD model; supporting cross-check: Gabrielsson & Weiner 5e, p.604, Fig.27.2.
- **Why this figure matters**: Full TMDD의 핵심은 parameter count가 아니라 topology다. 이 figure는 ligand, receptor/target, complex, internalization/sink가 어떻게 연결되는지 보여준다.
- **When to look**: M4의 “A. Formal structure”와 “B. Mechanistic equations”를 읽은 직후.
- **Learner instruction**: 먼저 state variables를 찾고, 그다음 `kon`, `koff`, `ke(RL)`가 각각 어느 arrow에 해당하는지 매핑하라. `kin`은 binding arrow가 아니라 target turnover input임을 분리하라.

## Figure #6 — Mode N

- **Title**: Data Richness → ODE Term Identifiability Map
- **Visual objective**: 5초 안에 dataset I/II/III가 왜 `kon`, `koff`, `ke(RL)` precision을 다르게 만드는지 보이게 한다.
- **Core message**: target and complex assays are not decorative; they isolate otherwise hidden ODE terms.
- **Elements to include**:
  - Row 1: Dataset I = ligand only → visible ligand profile → nonspecific disposition + gross phase structure
  - Row 2: Dataset II = ligand + target → target recovery/saturation boundary → better `kon`, `koff`
  - Row 3: Dataset III = ligand + target + complex → complex sink trajectory → better `ke(RL)`
  - Right-side summary: Table 27.2 CV% improvement signal: `kon` 17→2→1; `koff` 27→13→3; `ke(RL)` 27→23→2
  - Bottom message: “Observed species determine estimable mechanism.”
- **Elements to exclude**:
  - full Table 27.2 reproduction
  - all non-key parameters
  - statistical estimation details outside Content Lock v2
  - NONMEM implementation settings
- **Suggested rendering**: Mermaid flowchart
- **Caption**: Adding target and complex observations converts hidden TMDD mechanisms into estimable ODE terms.
- **Alt text**: Three dataset rows show ligand-only, ligand-plus-target, and ligand-plus-target-plus-complex data progressively improving the identifiability of binding and complex-loss parameters.
- **Source relation**: Newly designed

## Figure #7 — Mode P

- **Source**: Gabrielsson & Weiner 5e, p.609, Fig.27.6 — MM fit deviation and `Km` over-prediction.
- **Why this figure matters**: M5의 “MM은 observed range에서는 맞아 보일 수 있으나 low-concentration extrapolation에서 무너진다”는 메시지는 curve pattern으로 봐야 고정된다. Fig.27.6은 high concentration fit과 low-dose systematic deviation의 차이를 보여주는 critical blow다.
- **When to look**: M5의 “C. When MM breaks”를 읽은 직후.
- **Learner instruction**: 세 high-dose profiles와 lowest-dose profile을 따로 보라. `Km=3.7` vs `0.03`의 차이를 단순 숫자가 아니라 “외삽 영역에서 모델 구조가 바뀌는 신호”로 해석하라.

---

# 4. Insertion Map (PATCH MODE)

## 4A. Map Table

| # | Reading order | Anchor (verbatim from Content Lock v2) | Insert position | Marker block |
|---:|---|---|---|---|
| 1 | §2 → M1 | `## ▌ Card M1 — Turnover Paradigm (`kin`/`kout`)` | after this anchor card | See Marker Block #1 below |
| 2 | §2 → M2 | `## ▌ Card M2 — Protein/Antibody Distinctive PK` | after this anchor card; before Marker Block #3 | See Marker Block #2 below |
| 3 | §2 → M2 | `## ▌ Card M2 — Protein/Antibody Distinctive PK` | after this anchor card; after Marker Block #2 | See Marker Block #3 below |
| 4 | §2 → M3 | `## ▌ Card M3 — TMDD 4-Phase Concentration-Time Profile` | after this anchor card | See Marker Block #4 below |
| 5 | §2 → M4 | `## ▌ Card M4 — Full TMDD Model ⚡ Apex Concept` | after this anchor card; before Marker Block #6 | See Marker Block #5 below |
| 6 | §2 → M4 | `## ▌ Card M4 — Full TMDD Model ⚡ Apex Concept` | after this anchor card; after Marker Block #5 | See Marker Block #6 below |
| 7 | §2 → M5 | `## ▌ Card M5 — Michaelis-Menten Approximation Boundary` | after this anchor card | See Marker Block #7 below |

## 4B. Full Marker Blocks

### Marker Block #1

```text
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.97, Fig.2.70
Why this matters: This figure fixes the asymmetric logic of turnover: changing `kin` changes steady-state level, whereas changing `kout` changes both level and time-to-steady-state. Without seeing both panels, learners often treat both as generic “rate changes.”
When to look: after reading Card M1.
Learner instruction: Compare the left and right panels. Ask which manipulation changes only the new level and which also changes the approach time.
<!-- /FIGURE_POINTER -->
```

### Marker Block #2

```text
<!-- FIGURE_SCHEMATIC -->
Title: Protein/Antibody PK Four-Gate Map
Mode: N
Visual objective: Show in 5 seconds that mAb PK is controlled by four physiological gates, not by “large molecule = slow elimination” alone.
Core message: Protein/antibody PK emerges from restricted distribution, lymphatic input, size-dependent elimination, and FcRn rescue.
Elements to include: central `mAb / protein drug`; Distribution gate (`Vss` small, plasma/interstitial restriction); Absorption gate (sc/im to lymphatic route, delayed input); Elimination gate (renal cutoff for small proteins, proteolysis/RME for larger proteins); Rescue gate (FcRn salvage, degradation avoidance, longer apparent half-life); downstream cautions for terminal slope, renal disease, and TMDD curve reading.
Elements to exclude: full numerical tables; long drug lists; 150 kDa lymph recovery percentage extrapolation; decorative antibody anatomy.
Suggested rendering: Mermaid
Caption: Protein/antibody PK should be read as a set of physiological gates before interpreting terminal slope or nonlinear clearance.
Alt text: A central mAb node branches into distribution, absorption, elimination, and FcRn rescue gates, each leading to a specific PK interpretation caution.
Source relation: Newly designed
<!-- /FIGURE_SCHEMATIC -->
```

### Marker Block #3

```text
<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.709, Fig.21-5
Why this matters: FcRn salvage is a recycling mechanism, not just a long half-life label. The figure shows how IgG/mAbs avoid degradation and return to circulation.
When to look: after reading Card M2.
Learner instruction: Trace the endosomal route. Identify which path leads to degradation and which path returns IgG/mAb to the systemic circulation.
<!-- /FIGURE_POINTER -->
```

### Marker Block #4

```text
<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.712, Fig.21-9; cross-check Gabrielsson & Weiner 5e, p.610, Fig.27.7
Why this matters: This figure prevents the common mistake of memorizing TMDD Phase A–D as mere time segments. The phases should be read as concentration-regime signatures linked to target saturation and `Km`/`Kd` boundaries.
When to look: after reading Card M3, before reading Card M5.
Learner instruction: Follow Phase A–D while asking what concentration regime the ligand is in. Then map the phase transition to the MM boundary discussion.
<!-- /FIGURE_POINTER -->
```

### Marker Block #5

```text
<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.711, Fig.21-8; cross-check Gabrielsson & Weiner 5e, p.604, Fig.27.2
Why this matters: Full TMDD is a topology problem before it is a parameter-count problem. The figure shows how ligand, target, complex, binding, dissociation, and sink are connected.
When to look: after reading Card M4.
Learner instruction: Locate ligand, free target, and complex first. Then map `kon`, `koff`, and `ke(RL)` to arrows, and keep `kin` separate as target turnover input.
<!-- /FIGURE_POINTER -->
```

### Marker Block #6

```text
<!-- FIGURE_SCHEMATIC -->
Title: Data Richness → ODE Term Identifiability Map
Mode: N
Visual objective: Show in 5 seconds why ligand-only, ligand+target, and ligand+target+complex datasets identify different TMDD mechanisms.
Core message: Target and complex assays are not decorative; they isolate hidden ODE terms.
Elements to include: Dataset I = ligand only → nonspecific disposition + gross phase structure; Dataset II = ligand + target → target recovery/saturation boundary → improved `kon`/`koff`; Dataset III = ligand + target + complex → complex sink trajectory → improved `ke(RL)`; summary CV% improvement signal: `kon` 17→2→1, `koff` 27→13→3, `ke(RL)` 27→23→2; bottom message “Observed species determine estimable mechanism.”
Elements to exclude: full Table 27.2 reproduction; non-key parameters; estimation software settings; NONMEM control stream details.
Suggested rendering: Mermaid
Caption: Adding target and complex observations converts hidden TMDD mechanisms into estimable ODE terms.
Alt text: Three dataset rows show ligand-only, ligand-plus-target, and ligand-plus-target-plus-complex data progressively improving identifiability of binding and complex-loss parameters.
Source relation: Newly designed
<!-- /FIGURE_SCHEMATIC -->
```

### Marker Block #7

```text
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.609, Fig.27.6
Why this matters: Fig.27.6 is the critical blow against unqualified MM extrapolation: high-dose fit can look acceptable while the lowest-dose profile shows systematic deviation and `Km` is over-predicted. Without seeing this, learners may equate fit quality with mechanistic validity.
When to look: after reading Card M5.
Learner instruction: Compare the three higher profiles against the lowest profile. Treat the mismatch as a model-boundary signal, not as a cosmetic fit issue.
<!-- /FIGURE_POINTER -->
```

---

# 5. Phase 5 Operator Note

Apply Marker Blocks #1–#7 to the unchanged Content Lock v2 body at the anchors specified above. Do not alter any existing prose, page tags, equations, source flags, or non-figure markers. The resulting spliced file is **09_Content Lock v2.1 — figure marker insertion본**.

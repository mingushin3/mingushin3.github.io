# 03_Content Lock v2.1 — Figure Marker Patch

## 1. Output Mode Declaration

**PATCH MODE**

- 적용 근거: Content Lock v2는 약 5,166 words로 6,000 words 이하이나, 최종 KEEP marker 수가 4개로 `marker count ≤4` 조건에 해당한다.
- 목적: Content Lock v2 본문을 재출력하지 않고, Phase 5에서 원문 v2에 marker만 splice하여 v2.1을 생성한다.
- Image rights: Scope Lock상 `Image rights = None`이므로 textbook figure 원본 삽입은 금지한다. Mode I는 사용하지 않는다. Copyrighted textbook figures는 pointer 또는 구조적으로 구분되는 redraw brief로만 처리한다.

---

## 2. Figure Strategy Table — View (A) Reading-order Figure Plan

| # | Reading order | Location (§ + concept card) | Mode | Source figure (if any) | Trigger | Why text alone is insufficient | Expected learning gain | Decision |
|---|---|---|---|---|---|---|---|---|
| 1 | §2 → Card 1 | Card 1. C(t) Master Equation | R | Textbook basis: G Fig.2.15; T Fig.6-4 | G1, G2 | ODE와 적분식만으로는 `gut loss`, `systemic input`, `central elimination`, `observed C(t)`가 같은 시스템의 다른 층위라는 점이 한눈에 보이지 않는다. | learner가 Master Equation을 단순 공식이 아니라 compartment topology에서 나온 결과로 읽게 된다. | KEEP |
| 2 | §2 → Card 2 | Card 2. tmax / Cmax, Method of Residuals | P | G Fig.2.18–2.19 | G1, G5 | residual method와 lag-time 교점은 시각화가 있으면 이해가 빠르지만, v2에서는 context-level 처리이고 B-Standard figure budget에서 Apex보다 우선순위가 낮다. | residual method의 보조 이해. | REJECT — budget triage; residual method는 Card 2 본문과 equation anchor로 충분히 방어 가능. |
| 3 | §2 → Card 3 | Card 3. Bioavailability F | P | T Fig.6-5; T Fig.6-13; T Table 6-1 | G2, G5 | F, Frel, BE, urine-data estimation은 여러 figure/table로 흩어져 있어 하나를 고르면 오히려 범위가 확장된다. | rate vs extent 보조 이해. | REJECT — Card 3은 equation과 caveat 중심이며, visual ROI가 Card 4/5보다 낮다. |
| 4 | §2 → Card 4 | Card 4. APEX — V/F 식별불가능성 + Flip-flop | P | G Fig.2.17 | G2, G5 | parallel/non-parallel IV/PO terminal slope는 텍스트만으로는 slope label 전환이 잘못 매핑되기 쉽다. | learner가 terminal slope를 자동으로 kel로 읽는 습관을 중단한다. | KEEP |
| 5 | §5 | Confusion Pair 4. First-order ka vs Zero-order input | P | T Fig.6-2; G PK3 Fig.3.1 / Table 3.1 | G2, G5 | first-order vs zero-order는 유용한 비교지만 v2의 core risk는 apparent parameter와 flip-flop이다. | input-function 비교 보조 이해. | REJECT — §5 본문 표와 PK3 설명으로 충분하며, B-Standard budget 초과. |
| 6 | §2 → Card 5 | Card 5. ka,app vs ka,true | P | G Fig.2.24 | G2, G5 | `ka,app = ka,true + kd`는 식으로는 간단하지만, gut compartment에서 disappearance와 systemic appearance가 분리된다는 구조는 시각화 없이는 쉽게 놓친다. | learner가 fitted ka를 곧바로 true absorption으로 부르지 않게 된다. | KEEP |
| 7 | §8 | Meta-frame & Big Picture | P | G Fig.2.32 | G3, G5 | 전체 oral concentration-time curve determinants는 본문 여러 카드에 분산되어 있어, 마지막에 source summary를 보지 않으면 chapter-level 구조가 흩어진 채 끝난다. | learner가 F·ka·V/F·CL/F·input-function을 하나의 oral curve determinant map으로 재결합한다. | KEEP |

---

## 3. Figure Strategy Table — View (B) Type-sorted Summary

**Pointers (P):** #4, #6, #7 → 3 / 3 allowed for B-Standard  
**Schematics (R/N):** #1 → 1 / 1 allowed for B-Standard  
**Images (I):** none → 0; Image rights = None  
**Rejected due to budget or lower ROI:** #2, #3, #5

Budget decision: **PASS** — B-Standard strict budget satisfied.

---

## 4. Figure Briefs — KEEP Items Only

### Figure #1 — R schematic brief

- **Title:** 1차 extravascular input의 compartment topology
- **Visual objective:** learner가 5초 안에 `Dpo → gut compartment → F-scaled input → central compartment → elimination` 흐름을 본다.
- **Core message:** Master Equation은 두 지수의 차이로 보이지만, 그 뿌리는 gut loss와 central elimination이 직렬로 연결된 1차 ODE 구조다.
- **Elements to include:**
  - Oral dose `Dpo`
  - Gut/absorption site `Ag`
  - first-order gut loss arrow labeled `ka·Ag`
  - systemic input branch labeled `F·ka·Ag`
  - optional non-systemic loss branch labeled `(1−F)` or `gut loss / degradation`
  - central compartment `C` or `A/V`
  - elimination arrow labeled `kel·C` or `CL·C`
  - output label: `C(t) = difference of exponentials`
- **Elements to exclude:**
  - textbook bucket/reservoir drawing style
  - empirical concentration-time curves
  - zero-order, multiple absorption sites, transit compartments
  - numerical values
- **Suggested rendering:** Mermaid flowchart
- **Caption:** 1차 흡수 oral model은 gut에서 사라지는 과정과 central compartment에서 제거되는 과정이 직렬로 결합된 구조다.
- **Alt text:** Oral dose가 gut compartment를 거쳐 F-scaled input으로 central compartment에 들어가고, central compartment에서 elimination되는 흐름도.
- **Source relation:** Redrawn from textbook concept (no exact reproduction)

### Figure #4 — P pointer brief

- **Source:** Gabrielsson & Weiner 5e, p.30, Fig.2.17
- **Why this figure matters:** 이 figure는 IV와 PO terminal slope가 parallel이면 oral terminal phase를 elimination으로 볼 수 있지만, non-parallel이면 absorption-limited terminal decline이 될 수 있음을 직접 보여준다.
- **When to look:** Card 4를 읽은 직후.
- **Learner instruction:** 왼쪽 panel에서는 IV와 PO terminal slope가 어떻게 같은 방향으로 떨어지는지 확인하라. 오른쪽 panel에서는 PO terminal slope가 IV slope와 달라질 때, terminal slope label이 kel에서 ka로 바뀔 수 있음을 확인하라.

### Figure #6 — P pointer brief

- **Source:** Gabrielsson & Weiner 5e, p.40, Fig.2.24
- **Why this figure matters:** 이 figure는 `ka,app`가 true absorption만이 아니라 gut degradation/loss를 포함할 수 있음을 compartment 구조로 분리한다.
- **When to look:** Card 5를 읽은 직후.
- **Learner instruction:** gut compartment에서 사라지는 흐름과 systemic circulation에 실제로 들어가는 흐름을 분리해서 보라. fitted ka가 왜 곧바로 `ka,true`가 아닌지 확인하라.

### Figure #7 — P pointer brief

- **Source:** Gabrielsson & Weiner 5e, p.47, Fig.2.32
- **Why this figure matters:** 이 figure는 oral concentration-time curve를 결정하는 요인을 chapter conclusion 수준에서 압축한다.
- **When to look:** §8 Meta-frame을 읽은 뒤, Final Recap 직전.
- **Learner instruction:** figure의 각 determinant를 Content Lock의 5개 MUST card에 다시 매핑하라. 특히 F, input rate, elimination/distribution, apparent parameter가 서로 다른 질문에 답한다는 점을 확인하라.

---

## 5. Insertion Map (PATCH MODE)

| # | Reading order | Anchor (exact heading or unique text from Content Lock v2) | Insert position | Marker block |
|---|---|---|---|---|
| 1 | §2 → Card 1 | `### Card 1. C(t) Master Equation — 경구 PK의 모든 것이 시작되는 한 줄` | after this anchor card; immediately before `### Card 2. tmax / Cmax — 흡수속도와 소실속도가 같아지는 순간` | See Marker Block #1 below |
| 4 | §2 → Card 4 | `### Card 4. APEX — V/F 식별불가능성 + Flip-flop 동정` | after this anchor card; immediately before `### Card 5. ka,app vs ka,true — ka가 측정하는 것은 무엇인가` | See Marker Block #4 below |
| 6 | §2 → Card 5 | `### Card 5. ka,app vs ka,true — ka가 측정하는 것은 무엇인가` | after this anchor card; immediately before `## §5. CONFUSION PAIR DISSECTION` | See Marker Block #6 below |
| 7 | §8 | `### D. Ch.7 context in one sentence` | after this subsection; immediately before `### E. Final lock sentence` | See Marker Block #7 below |

### Marker Block #1

```text
<!-- FIGURE_SCHEMATIC -->
Title: 1차 extravascular input의 compartment topology
Mode: R
Visual objective: 5초 안에 Dpo → gut compartment → F-scaled input → central compartment → elimination 흐름을 보게 한다.
Core message: Master Equation은 두 지수의 차이로 보이지만, 그 뿌리는 gut loss와 central elimination이 직렬로 연결된 1차 ODE 구조다.
Elements to include: Oral dose Dpo; gut/absorption site Ag; first-order gut loss arrow labeled ka·Ag; systemic input branch labeled F·ka·Ag; optional non-systemic loss branch labeled (1−F) or gut loss/degradation; central compartment C or A/V; elimination arrow labeled kel·C or CL·C; output label C(t) = difference of exponentials.
Elements to exclude: textbook bucket/reservoir drawing style; empirical concentration-time curves; zero-order input; multiple absorption sites; transit compartments; numerical values.
Suggested rendering: Mermaid
Caption: 1차 흡수 oral model은 gut에서 사라지는 과정과 central compartment에서 제거되는 과정이 직렬로 결합된 구조다.
Alt text: Oral dose가 gut compartment를 거쳐 F-scaled input으로 central compartment에 들어가고, central compartment에서 elimination되는 흐름도.
Source relation: Redrawn from textbook concept
<!-- /FIGURE_SCHEMATIC -->
```

### Marker Block #4

```text
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.30, Fig.2.17
Why this matters: IV와 PO terminal slope가 parallel이면 oral terminal phase를 elimination으로 해석할 수 있지만, non-parallel이면 absorption-limited terminal decline이 될 수 있다. 이 figure는 terminal slope label이 kel에서 ka로 바뀌는 지점을 직접 보여준다.
When to look: Card 4를 읽은 직후.
Learner instruction: 왼쪽 panel에서는 IV와 PO terminal slope가 어떻게 같은 방향으로 떨어지는지 확인하라. 오른쪽 panel에서는 PO terminal slope가 IV slope와 달라질 때, terminal slope label이 kel에서 ka로 바뀔 수 있음을 확인하라.
<!-- /FIGURE_POINTER -->
```

### Marker Block #6

```text
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.40, Fig.2.24
Why this matters: ka,app는 true absorption만이 아니라 gut degradation/loss를 포함할 수 있다. 이 figure는 fitted ka를 생리학적 true absorption으로 바로 읽으면 안 되는 이유를 compartment 구조로 분리한다.
When to look: Card 5를 읽은 직후.
Learner instruction: gut compartment에서 사라지는 흐름과 systemic circulation에 실제로 들어가는 흐름을 분리해서 보라. fitted ka가 왜 곧바로 ka,true가 아닌지 확인하라.
<!-- /FIGURE_POINTER -->
```

### Marker Block #7

```text
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.47, Fig.2.32
Why this matters: oral concentration-time curve를 결정하는 요인은 Content Lock의 여러 카드에 분산되어 있다. 이 figure는 그 요인들을 chapter conclusion 수준에서 다시 하나의 구조로 묶어준다.
When to look: §8 Meta-frame을 읽은 뒤, Final Recap 직전.
Learner instruction: figure의 각 determinant를 Content Lock의 5개 MUST card에 다시 매핑하라. 특히 F, input rate, elimination/distribution, apparent parameter가 서로 다른 질문에 답한다는 점을 확인하라.
<!-- /FIGURE_POINTER -->
```

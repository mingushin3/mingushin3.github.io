# 04_Content Lock v2.1 — Figure Marker Patch

**Output mode**: PATCH MODE  
**Reason**: Content Lock v2는 장문 텍스트 확정본이며, 본 Phase 4C의 목적은 본문 재출력이 아니라 figure marker의 위치와 brief를 확정하는 것이다. 따라서 본문 전체를 재출력하지 않고 Strategy Table + Briefs + Insertion Map만 제공한다.  
**Image rights**: None. 교재 원본 figure 직접 삽입은 사용하지 않는다. Mode I는 사용하지 않는다.  
**Phase boundary**: Mermaid, SVG, HTML code는 생성하지 않는다. Phase 5에서만 rendering한다.

---

## 1. Figure Strategy Table — View A. Reading-order Figure Plan

| # | Reading order | Location (§ + concept card) | Mode | Source figure / source object | Trigger | Why text alone is insufficient | Expected learning gain | Decision |
|---:|---|---|---|---|---|---|---|---|
| 1 | §1 | Why This Chapter Matters | N | None — source-synthesized overview | G3, G4 | 본문은 M1–M14를 순서대로 설명하지만, `CL`, organ extraction, route, parent–metabolite, renal impairment가 하나의 decision space에서 어떻게 연결되는지는 한눈에 보이지 않는다. | 학습자가 “어떤 clearance인가?”를 네 축 질문으로 분해하는 전체 항법도를 먼저 얻는다. | KEEP |
| 2 | §2 | M3. ARE plot vs Excretion Rate plot | P | Gabrielsson p.50, Fig 2.35 | G2, G5 | ARE plot의 actual time과 rate plot의 midpoint convention은 텍스트 표만으로는 머릿속에서 쉽게 섞인다. | urinary plot을 “같은 slope를 추정하지만 시간 정보가 다른 두 도구”로 분리한다. | KEEP |
| 3 | §2 | M4. Well-stirred hepatic clearance + 4-model compression | P | Gabrielsson p.79, Fig 2.58; optional companion: Tozer p.131, Fig 5-7 | G1, G5 | well-stirred 식은 `Q_H`, `f_{ub}`, `CL_int`가 하나의 분수식에 들어가므로, organ input-output 구조를 보지 않으면 분모의 의미가 추상화된다. | hepatic extraction을 “혈류가 들어오고, 일부가 제거되고, 나머지가 나가는 organ balance”로 고정한다. | KEEP |
| 4 | §2 | M5. High/low extraction + route × extraction × `f_u` matrix | N | Newly designed from source equations/cases | G1, G2, G4 | high/low extraction, IV/oral route, total/unbound concentration이 동시에 바뀌므로 문장형 설명은 4사분면 오개념을 막기 어렵다. | “High extraction이면 `f_u` 무관”이라는 반쪽 문장을 route와 concentration 기준으로 교정한다. | KEEP |
| 5 | §2 | M10. Extended clearance: transporter–enzyme architecture | P | Tozer p.136, Fig 5-11; companion equations: Tozer App.E pp.778–779, Eq E-9–E-15 | G1, G5 | uptake, metabolism, efflux, permeability가 cell membrane을 사이에 두고 배열되는 구조는 수식만으로는 위치 관계가 흐려진다. | well-stirred model이 transporter/permeability step이 빠른 특수한 경우임을 시각적으로 분리한다. | KEEP |
| 6 | §2 | M11. Rate-limiting step in metabolite disposition | P | Tozer p.660, Fig 20-1 | G1, G2, G5 | formation-limited와 elimination-limited의 차이는 terminal slope가 parent를 따르는지 metabolite를 따르는지의 시간 패턴 문제다. | “metabolite terminal half-life = metabolite own half-life”라는 자동 해석을 차단한다. | KEEP |
| 7 | §2 | M14. Renal impairment active-metabolite scenario + interconversion | P | Tozer p.674, Fig 20-10 and Table 20-4 | G1, G2, G5 | parent와 active metabolite가 renal impairment에서 서로 다른 폭으로 상승하는 위험은 숫자표와 profile을 함께 봐야 구조가 잡힌다. | parent-only dose adjustment가 왜 active metabolite accumulation을 놓치는지 한 번에 확인한다. | KEEP |
| R1 | §2 | M2. Renal clearance decomposition | P/R candidate | Tozer p.140, Fig 5-14 | G1, G5 | filtration/secretion/reabsorption은 시각적으로 유용하다. | M2 식 이해 보조. | REJECT — budget 초과 시 M3 urinary-plot confusion이 더 큰 learner failure를 제거함. |
| R2 | §2 | M6. IVIVE pitfalls | P/R candidate | Gabrielsson pp.88–89, Fig 2.63–2.65 | G2, G5 | single-point, MMP, data condensation의 위험을 그림으로 볼 수 있다. | IVIVE audit mindset 강화. | REJECT — 본문에 3 trap이 이미 명시되어 있고, schematic budget은 §1 overview와 M5 matrix에 배정. |
| R3 | §2 | M7. PK5 simultaneous plasma+urine fitting | P candidate | Gabrielsson pp.495–497, PK5 Fig 5.1 and Fig 5.3 | G1, G5 | simultaneous fitting 구조는 중요하다. | plasma+urine fitting implementation 강화. | REJECT — implementation evidence figure로는 가치가 높지만, 본 v2.1의 core conceptual budget에서는 M10/M11/M14보다 낮음. |
| R4 | §2 | M8. Plasma-to-blood ratio and blood clearance | P candidate | Tozer App.D pp.775–776, Eq D-1–D-8 | G1, G5 | mass-balance derivation은 시각적 보조가 가능하다. | `C/C_b`, `f_u`, hematocrit 연결 강화. | REJECT — M8 본문 equation block이 충분하고, organ extraction failure는 M4/M5 marker로 더 직접 해결됨. |
| R5 | §2 | M13. First-pass metabolite contribution + steady-state metabolite | P candidate | Tozer pp.666–668, Fig 20-5–20-7; p.671 Fig 20-8 | G1, G5 | oral first-pass metabolite input과 accumulation profile은 figure 가치가 있다. | route-dependent metabolite exposure 강화. | REJECT — M14 active-metabolite renal impairment가 더 큰 safety/decision failure를 제거함. |

---

## 2. Figure Strategy Table — View B. Type-sorted Summary

- **Pointers (P)**: #2, #3, #5, #6, #7 → **5 / max 5** for A-Critical budget.
- **Schematics (R/N combined)**: #1, #4 → **2 / max 2** for A-Critical budget.
- **Images (I)**: none → Image rights = None; no direct textbook image insertion.
- **Rejected due to budget / lower marginal ROI**: R1–R5.

**Budget verdict**: PASS. No Mode I proposed. No textbook image reproduction proposed.

---

## 3. Figure Briefs — KEEP Items Only

### Figure #1 — New schematic

- **Title**: Clearance universe decision map: organ, route, concentration basis, and metabolite axis
- **Visual objective**: 5초 안에 `CL` 해석이 total number가 아니라 네 가지 질문으로 분해됨을 보이게 한다.
- **Core message**: `CL` 해석은 “어느 농도 기준인가, 어느 장기인가, 어느 route인가, parent인가 metabolite인가?”를 순서대로 묻는 구조적 문제다.
- **Elements to include**:
  - Center node: observed `CL`, `t1/2`, `AUC`, `AUC(m)/AUC`
  - Branch 1: concentration basis → plasma `CL` vs blood `CL_b`
  - Branch 2: organ route → renal `CL_R`, hepatic `CL_H`, other
  - Branch 3: hepatic determinants → `Q_H`, `f_{ub}`, `CL_int`, permeability/transporter
  - Branch 4: metabolite axis → `f_m`, `CL(m)`, rate-limiting step, renal impairment
  - Final decision node: dose/label/model interpretation
- **Elements to exclude**:
  - Numerical examples
  - Full equations beyond variable labels
  - Regulatory claims not already in Content Lock v2
- **Suggested rendering**: Mermaid flowchart
- **Caption**: Clearance interpretation begins by splitting one observed number into concentration basis, organ route, route/extraction behavior, and metabolite-specific clearance.
- **Alt text**: A flowchart starts from observed clearance-related metrics and branches to plasma versus blood basis, renal/hepatic routes, hepatic determinants, and metabolite-specific axes.
- **Source relation**: Newly designed

### Figure #2 — Pointer

- **Source**: Gabrielsson & Weiner, p.50, Fig 2.35 — ARE plot and excretion-rate plot schematic.
- **Why this figure matters**: M3의 핵심 혼동은 두 plot의 slope가 모두 `K`를 주더라도 시간 배치와 noise 민감도가 다르다는 점이다. 원 figure는 ARE의 actual time과 rate plot의 midpoint convention을 직접 보여준다.
- **When to look**: After reading M3.
- **Learner instruction**: 두 panel에서 x-axis time이 무엇을 의미하는지 먼저 확인하라. 그 다음 `X_{u,0-∞}` 의존성과 midpoint averaging이 각각 어느 plot에 들어가는지 표시하라.

### Figure #3 — Pointer

- **Source**: Gabrielsson & Weiner, p.79, Fig 2.58 — extraction across eliminating organ; optional companion: Rowland & Tozer, p.131, Fig 5-7 — perfusion effect on hepatic clearance/extraction.
- **Why this figure matters**: well-stirred equation은 organ input-output 구조에서 출발한다. 그림을 보지 않으면 `Q_H`가 단순 covariate가 아니라 organ에 들어오는 blood flow ceiling이라는 점이 약해진다.
- **When to look**: Before reading the limiting-case table in M4.
- **Learner instruction**: 먼저 inlet concentration, outlet concentration, blood flow, extracted fraction을 하나의 organ balance로 읽어라. 그런 다음 `f_{ub}·CL_int >> Q_H`와 `f_{ub}·CL_int << Q_H`가 각각 어느 병목을 뜻하는지 대응시켜라.

### Figure #4 — New schematic

- **Title**: Route × extraction × protein binding interpretation matrix
- **Visual objective**: 5초 안에 IV/oral과 high/low extraction이 `f_u` 변화 해석을 바꾸는 4사분면임을 보이게 한다.
- **Core message**: Protein binding effect는 drug label 하나로 결정되지 않고 route, extraction class, total/unbound endpoint에 따라 바뀐다.
- **Elements to include**:
  - 2×2 matrix: rows = IV / oral; columns = high extraction / low extraction
  - Each cell: total concentration/AUC response and unbound concentration/AUC response
  - Side label: “Do not transfer IV DDI conclusion to oral route without first-pass check”
  - Small legend: total `C` vs unbound `C_u`
- **Elements to exclude**:
  - Drug-specific mini profiles
  - Numeric fold changes
  - Detailed Table 2.9 formula variants
- **Suggested rendering**: CSS-card
- **Caption**: The same protein-binding change can have different clinical meaning depending on route, extraction ratio, and whether total or unbound concentration is interpreted.
- **Alt text**: A two-by-two matrix compares IV and oral dosing against high and low extraction, with separate notes for total and unbound concentration interpretation.
- **Source relation**: Newly designed

### Figure #5 — Pointer

- **Source**: Rowland & Tozer, p.136, Fig 5-11 — hepatocyte transporter/enzyme location and extended clearance; companion: Tozer App.E pp.778–779, Eq E-9–E-15 for `ρ`.
- **Why this figure matters**: M10은 cell membrane을 사이에 둔 uptake, metabolism, efflux의 위치 관계가 핵심이다. 이 위치 관계를 보지 않으면 permeability-limited clearance를 단순 low `CL_int`로 오해하기 쉽다.
- **When to look**: After reading M9 and before reading M10.
- **Learner instruction**: Sinusoidal uptake, intracellular metabolism, canalicular efflux, basolateral efflux를 서로 다른 arrow로 구분하라. 그 다음 `ρ<1`이 어느 membrane step의 병목을 뜻하는지 찾아라.

### Figure #6 — Pointer

- **Source**: Rowland & Tozer, p.660, Fig 20-1 — rate-limiting step in metabolite disposition.
- **Why this figure matters**: metabolite terminal slope는 formation과 elimination 중 더 느린 step에 의해 결정된다. 원 figure는 parent → metabolite → eliminated metabolite 흐름에서 `k_f`, `k(m)`, other elimination을 동시에 보여준다.
- **When to look**: Before reading the Case table in M11.
- **Learner instruction**: `k_f`와 `k(m)` 중 작은 rate constant가 terminal behavior를 지배한다는 점을 그림 위에 표시하라. Parallel decline을 보면 metabolite own half-life라고 쓰기 전에 formation-limited 가능성을 먼저 점검하라.

### Figure #7 — Pointer

- **Source**: Rowland & Tozer, p.674, Fig 20-10 and Table 20-4 — active metabolite accumulation in renal insufficiency.
- **Why this figure matters**: M14의 위험은 parent exposure 상승보다 active metabolite exposure 상승이 훨씬 클 수 있다는 비대칭성이다. Fig 20-10/Table 20-4는 parent-only dose adjustment가 왜 실패하는지 보여주는 핵심 evidence object다.
- **When to look**: After reading the Tozer worked scenario in M14.
- **Learner instruction**: 정상 상태와 anuric condition에서 parent와 metabolite contribution을 따로 비교하라. 최종 dose ratio를 보기 전에 metabolite `CL(m)`이 얼마나 무너지는지 먼저 확인하라.

---

## 4. Insertion Map (PATCH MODE)

| # | Reading order | Anchor copied verbatim from Content Lock v2 | Insert position | Marker block ID |
|---:|---|---|---|---|
| 1 | §1 | `## §1 Why This Chapter Matters` | before next §heading | Marker block #1 |
| 2 | §2 / M3 | `### M3. ARE plot vs Excretion Rate plot` | after this anchor card | Marker block #2 |
| 3 | §2 / M4 | `### M4. Well-stirred hepatic clearance + 4-model compression` | after this anchor card | Marker block #3 |
| 4 | §2 / M5 | `### M5. High/low extraction + route × extraction × \`f_u\` matrix` | after this anchor card | Marker block #4 |
| 5 | §2 / M10 | `### M10. Extended clearance: transporter–enzyme architecture` | after this anchor card | Marker block #5 |
| 6 | §2 / M11 | `### M11. Rate-limiting step in metabolite disposition` | after this anchor card | Marker block #6 |
| 7 | §2 / M14 | `### M14. Renal impairment active-metabolite scenario + interconversion` | after this anchor card | Marker block #7 |

### Marker block #1

```text
<!-- FIGURE_SCHEMATIC -->
Title: Clearance universe decision map: organ, route, concentration basis, and metabolite axis
Mode: N
Visual objective: 5초 안에 `CL` 해석이 total number가 아니라 네 가지 질문으로 분해됨을 보이게 한다.
Core message: `CL` 해석은 “어느 농도 기준인가, 어느 장기인가, 어느 route인가, parent인가 metabolite인가?”를 순서대로 묻는 구조적 문제다.
Elements to include: center node observed `CL`/`t1/2`/`AUC`/`AUC(m)/AUC`; branch concentration basis with plasma `CL` vs blood `CL_b`; branch organ route with renal `CL_R`, hepatic `CL_H`, other; branch hepatic determinants with `Q_H`, `f_{ub}`, `CL_int`, permeability/transporter; branch metabolite axis with `f_m`, `CL(m)`, rate-limiting step, renal impairment; final decision node dose/label/model interpretation.
Elements to exclude: numerical examples; full equations beyond variable labels; regulatory claims not already in Content Lock v2.
Suggested rendering: Mermaid
Caption: Clearance interpretation begins by splitting one observed number into concentration basis, organ route, route/extraction behavior, and metabolite-specific clearance.
Alt text: A flowchart starts from observed clearance-related metrics and branches to plasma versus blood basis, renal/hepatic routes, hepatic determinants, and metabolite-specific axes.
Source relation: Newly designed
<!-- /FIGURE_SCHEMATIC -->
```

### Marker block #2

```text
<!-- FIGURE_POINTER -->
Source: [Gabrielsson & Weiner, p.50, Fig 2.35]
Why this matters: M3의 핵심 혼동은 두 plot의 slope가 모두 `K`를 주더라도 시간 배치와 noise 민감도가 다르다는 점이다. 원 figure는 ARE의 actual time과 rate plot의 midpoint convention을 직접 보여준다.
When to look: after reading this card
Learner instruction: 두 panel에서 x-axis time이 무엇을 의미하는지 먼저 확인하라. 그 다음 `X_{u,0-∞}` 의존성과 midpoint averaging이 각각 어느 plot에 들어가는지 표시하라.
<!-- /FIGURE_POINTER -->
```

### Marker block #3

```text
<!-- FIGURE_POINTER -->
Source: [Gabrielsson & Weiner, p.79, Fig 2.58; optional companion: Rowland & Tozer, p.131, Fig 5-7]
Why this matters: Well-stirred equation은 organ input-output 구조에서 출발한다. 그림을 보지 않으면 `Q_H`가 단순 covariate가 아니라 organ에 들어오는 blood flow ceiling이라는 점이 약해진다.
When to look: before reading this card
Learner instruction: 먼저 inlet concentration, outlet concentration, blood flow, extracted fraction을 하나의 organ balance로 읽어라. 그런 다음 `f_{ub}·CL_int >> Q_H`와 `f_{ub}·CL_int << Q_H`가 각각 어느 병목을 뜻하는지 대응시켜라.
<!-- /FIGURE_POINTER -->
```

### Marker block #4

```text
<!-- FIGURE_SCHEMATIC -->
Title: Route × extraction × protein binding interpretation matrix
Mode: N
Visual objective: 5초 안에 IV/oral과 high/low extraction이 `f_u` 변화 해석을 바꾸는 4사분면임을 보이게 한다.
Core message: Protein binding effect는 drug label 하나로 결정되지 않고 route, extraction class, total/unbound endpoint에 따라 바뀐다.
Elements to include: 2×2 matrix with rows IV/oral and columns high extraction/low extraction; in each cell, total concentration/AUC response and unbound concentration/AUC response; side label “Do not transfer IV DDI conclusion to oral route without first-pass check”; small legend for total `C` vs unbound `C_u`.
Elements to exclude: drug-specific mini profiles; numeric fold changes; detailed Table 2.9 formula variants.
Suggested rendering: CSS-card
Caption: The same protein-binding change can have different clinical meaning depending on route, extraction ratio, and whether total or unbound concentration is interpreted.
Alt text: A two-by-two matrix compares IV and oral dosing against high and low extraction, with separate notes for total and unbound concentration interpretation.
Source relation: Newly designed
<!-- /FIGURE_SCHEMATIC -->
```

### Marker block #5

```text
<!-- FIGURE_POINTER -->
Source: [Rowland & Tozer, p.136, Fig 5-11; companion equations: Tozer App.E pp.778–779, Eq E-9–E-15]
Why this matters: M10은 cell membrane을 사이에 둔 uptake, metabolism, efflux의 위치 관계가 핵심이다. 이 위치 관계를 보지 않으면 permeability-limited clearance를 단순 low `CL_int`로 오해하기 쉽다.
When to look: before reading this card
Learner instruction: Sinusoidal uptake, intracellular metabolism, canalicular efflux, basolateral efflux를 서로 다른 arrow로 구분하라. 그 다음 `ρ<1`이 어느 membrane step의 병목을 뜻하는지 찾아라.
<!-- /FIGURE_POINTER -->
```

### Marker block #6

```text
<!-- FIGURE_POINTER -->
Source: [Rowland & Tozer, p.660, Fig 20-1]
Why this matters: Metabolite terminal slope는 formation과 elimination 중 더 느린 step에 의해 결정된다. 원 figure는 parent → metabolite → eliminated metabolite 흐름에서 `k_f`, `k(m)`, other elimination을 동시에 보여준다.
When to look: before reading this card
Learner instruction: `k_f`와 `k(m)` 중 작은 rate constant가 terminal behavior를 지배한다는 점을 그림 위에 표시하라. Parallel decline을 보면 metabolite own half-life라고 쓰기 전에 formation-limited 가능성을 먼저 점검하라.
<!-- /FIGURE_POINTER -->
```

### Marker block #7

```text
<!-- FIGURE_POINTER -->
Source: [Rowland & Tozer, p.674, Fig 20-10 and Table 20-4]
Why this matters: M14의 위험은 parent exposure 상승보다 active metabolite exposure 상승이 훨씬 클 수 있다는 비대칭성이다. Fig 20-10/Table 20-4는 parent-only dose adjustment가 왜 실패하는지 보여주는 핵심 evidence object다.
When to look: after reading this card
Learner instruction: 정상 상태와 anuric condition에서 parent와 metabolite contribution을 따로 비교하라. 최종 dose ratio를 보기 전에 metabolite `CL(m)`이 얼마나 무너지는지 먼저 확인하라.
<!-- /FIGURE_POINTER -->
```

---

## 5. Operator Note for Phase 5

- 이 파일은 PATCH MODE 산출물이므로 Content Lock v2 본문을 재출력하지 않는다.
- Phase 5에서는 위 Insertion Map의 anchor를 기준으로 marker block만 삽입하여 `04_Content Lock v2.1`을 생성한다.
- Marker block의 fenced code fence는 복사 대상이 아니다. Code fence 내부의 marker text만 삽입한다.
- Source page tags in Content Lock v2 body must remain unchanged.
- Figure rendering must occur only in Phase 5.

**END — 04_Content Lock v2.1 Figure Marker Patch**

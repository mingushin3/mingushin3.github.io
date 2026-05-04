# 01_Content Lock v2.1 — Figure Marker Insertion본

**Output mode declaration:** PATCH MODE  
**Mode rationale:** Content Lock v2는 6,000 whitespace words 이하이나, Phase 4C의 목적은 본문 재출력이 아니라 figure decision lock이다. 학습 ROI가 높은 figure marker를 4개로 제한했으므로 marker count ≤4 조건에 따라 PATCH MODE를 적용한다. 본문 재출력은 하지 않는다.

---

## Figure Strategy Table — View (A) Reading-order Figure Plan

| # | Reading order | Location (§ + concept card) | Mode | Source figure (if any) | Trigger (G1–G5) | Why text alone is insufficient | Expected learning gain | Decision |
|---:|---|---|---|---|---|---|---|---|
| 1 | §1 Roadmap 뒤 | §1 — Session Header & Roadmap | P | R&T Fig.3-1 p.54 + Fig.3-2 p.55 | G2, G5 | $C^0$, slope, AUC는 서로 다른 정보를 주지만, 텍스트만으로는 하나의 “노출 변화”로 합쳐 읽기 쉽다. | 초기 농도, slope, AUC가 서로 다른 primary determinant의 표면이라는 구조를 초반에 고정한다. | KEEP |
| 2 | C1 카드 끝 | C1 — Clearance | P | R&T Fig.3-3 p.55 | G1, G5 | $CL=Q\cdot E$는 flow와 extraction의 공간적 관계가 핵심이다. 문장만으로는 clearance의 물리적 의미가 약해진다. | $CL$을 단순 slope가 아니라 reservoir-extractor system의 apparent flow로 체화한다. | KEEP |
| 3 | C2 카드 끝 | C2 — Volume of Distribution | P | G Fig.2.3 p.15 | G2, G5 | Apparent volume은 “실제 부피가 아님”이라는 설명만으로는 mental image가 약하다. | 같은 실제 bucket에서 apparent $V$가 달라지는 장면을 통해 $V$ 오해를 차단한다. | KEEP |
| 4 | C4 카드 끝 | C4 — Half-life | R | R&T Fig.3-6 p.65 concept | G1, G2, G5 | Distribution phase와 terminal phase의 경계는 시간축 경쟁 구조다. 텍스트만으로는 “마지막 직선 = elimination” 오류가 남을 수 있다. | terminal slope 해석의 조건과 예외를 midazolam/gentamicin 논리로 분리한다. | KEEP |
| R1 | C3 후보 | C3 — Elimination Rate Constant | P | G Fig.2.6 p.17 | G2, G5 | Intercept–slope–area map은 유익하지만, 본문 수식과 §1 pointer가 이미 core hierarchy를 지지한다. | 시각 예산 보존. | REJECT — lower ROI under marker ≤4 |
| R2 | §5 후보 | §5 — Confusion Pair Dissection | R | G Fig.2.11 p.26 + Fig.2.12 p.26–27 concept | G2, G4, G5 | CL/V 분기 schematic은 유익하지만 C1–C4 marker 4개가 더 직접적인 concept failure를 막는다. | 후속 Phase 5 optional 후보로만 유지 가능. | REJECT — budget/ROI |
| R3 | C5 후보 | C5 — MRT | P | G Table 1.3 p.474 | G5 | Content Lock v2 본문에 이미 Table 1.3 기반 MRT/t½ 표가 들어 있다. | 추가 시각 이득 낮음. | REJECT — already represented as table |
| R4 | C4 후보 | C4 — Half-life | P | R&T Fig.3-4 p.61; Fig.3-7 p.66 | G5 | 각각의 원그림은 중요하지만 #4 schematic이 terminal interpretation의 핵심 구조를 더 압축한다. | 별도 pointer 남발 방지. | REJECT — absorbed into #4 brief |

---

## Figure Strategy Table — View (B) Type-sorted Summary

- **Pointers (P):** #1, #2, #3 → 3 / max 5 for A-Critical
- **Schematics (R/N):** #4 → 1 / max 2 for A-Critical
- **Images (I):** none → Image rights = None; no direct textbook image insertion
- **Total retained markers:** 4
- **Budget verdict:** PASS

---

## Figure Briefs — KEEP Items

### #1 — Mode P
- **Source:** Rowland & Tozer 5e, p.54 Fig.3-1; p.55 Fig.3-2
- **Why this figure matters:** Same dose에서 initial concentration, slope, AUC가 서로 독립적으로 달라지는 모습을 저자가 opening device로 제시한다.
- **When to look:** §1 Roadmap을 읽은 직후.
- **Learner instruction:** Fig.3-1은 같은 initial concentration에서 slope와 AUC가 갈라지는 경우를, Fig.3-2는 같은 half-life에서 initial concentration과 AUC가 갈라지는 경우를 비교한다.

### #2 — Mode P
- **Source:** Rowland & Tozer 5e, p.55 Fig.3-3
- **Why this figure matters:** $CL=Q\cdot E$를 flow와 extraction의 곱으로 보게 만드는 구조 그림이다.
- **When to look:** C1 Clearance card를 읽은 직후.
- **Learner instruction:** Reservoir, extractor, $Q$, $C$, $C_{out}$, $E$가 어떤 방향으로 연결되는지 추적한다.

### #3 — Mode P
- **Source:** Gabrielsson & Weiner 5e, p.15 Fig.2.3
- **Why this figure matters:** $V$가 실제 부피가 아니라 측정 농도에 의해 결정되는 apparent volume임을 가장 직관적으로 보여준다.
- **When to look:** C2 Volume of Distribution card를 읽은 직후.
- **Learner instruction:** 두 bucket의 dose가 같다는 점과 charcoal 때문에 측정 농도가 낮아지는 점을 연결한다.

### #4 — Mode R
- **Title:** Distribution phase와 elimination phase의 경쟁 판정
- **Visual objective:** 5초 안에 terminal slope 해석이 안전한 경우와 위험한 경우를 구분한다.
- **Core message:** Terminal phase는 자동으로 elimination phase가 아니라, distribution과 elimination의 속도 경쟁이 허락할 때만 elimination 해석에 안전하게 쓰인다.
- **Elements to include:** 두 병렬 lane; distribution fast/elimination slower; substantial elimination before distribution equilibrium; early distribution phase; terminal phase; AUC share; “terminal slope usable with caution”; “terminal slope may mislead”.
- **Elements to exclude:** 새로운 약물 수치; 다구획 미분방정식; 실제 교과서 곡선 복제; NONMEM code.
- **Suggested rendering:** Mermaid
- **Caption:** Distribution과 elimination의 상대 속도에 따라 terminal slope 해석의 안전성이 달라진다.
- **Alt text:** 두 개의 병렬 흐름도가 distribution이 먼저 정리되는 경우와 elimination이 먼저 크게 진행되는 경우를 비교한다.
- **Source relation:** Redrawn from textbook concept (R&T Fig.3-6 concept; no exact reproduction)

---

## Insertion Map (PATCH MODE)

| # | Reading order | Anchor (exact heading or first ≥40 chars of card) | Insert position | Marker block |
|---:|---|---|---|---|
| 1 | §1 Roadmap 뒤 | `## §1 — Session Header & Roadmap` | before next §heading | See Marker Block #1 |
| 2 | C1 카드 끝 | `### 🃏 C1. Clearance ($CL$) [Apex]` | after this anchor card | See Marker Block #2 |
| 3 | C2 카드 끝 | `### 🃏 C2. Volume of Distribution ($V$)` | after this anchor card | See Marker Block #3 |
| 4 | C4 카드 끝 | `### 🃏 C4. Half-life ($t_{1/2}$)` | after this anchor card | See Marker Block #4 |

### Marker Block #1

```markdown
<!-- FIGURE_POINTER -->
Source: [Rowland & Tozer 5e, p.54, Fig.3-1; p.55, Fig.3-2]
Why this matters: 같은 dose에서 “초기 농도”, “기울기”, “AUC”가 서로 다른 정보를 담는다는 사실을 한 번에 분리해 보여준다. 이 그림이 없으면 학습자가 $C^0$, slope, AUC를 하나의 노출 지표처럼 뭉뚱그려 읽을 위험이 크다.
When to look: after reading §1 Roadmap
Learner instruction: Fig.3-1에서는 같은 initial concentration에서 slope와 AUC가 어떻게 갈라지는지 보라. Fig.3-2에서는 같은 half-life라도 initial concentration과 AUC가 달라질 수 있음을 먼저 확인하라.
<!-- /FIGURE_POINTER -->
```

### Marker Block #2

```markdown
<!-- FIGURE_POINTER -->
Source: [Rowland & Tozer 5e, p.55, Fig.3-3]
Why this matters: Reservoir-extractor diagram은 $Q$, $E$, $C$, $C_{out}$이 어떻게 연결되어 $CL=Q\cdot E$가 되는지 시각적으로 고정한다. 텍스트만 읽으면 $CL$을 단순 slope나 제거 속도로 오해하기 쉽다.
When to look: after reading C1 Clearance card
Learner instruction: Reservoir를 “몸”, extractor를 “간/신장”으로 대응시켜 보라. 들어가는 양 $Q\cdot C$와 제거되는 fraction $E$의 곱이 왜 clearance의 물리적 의미가 되는지 확인하라.
<!-- /FIGURE_POINTER -->
```

### Marker Block #3

```markdown
<!-- FIGURE_POINTER -->
Source: [Gabrielsson & Weiner 5e, p.15, Fig.2.3]
Why this matters: 두 bucket의 실제 물 부피가 같아도 측정 농도 차이 때문에 apparent volume이 10 L와 100 L로 달라지는 장면을 보여준다. 이 그림이 없으면 $V$를 실제 해부학적 부피로 오해하기 쉽다.
When to look: after reading C2 Volume of Distribution card
Learner instruction: 두 bucket 모두 총 dose는 100 units로 같다는 점을 먼저 확인하라. 그다음 charcoal binding 때문에 측정 공간의 농도가 낮아지면 왜 apparent $V$가 커지는지 보라.
<!-- /FIGURE_POINTER -->
```

### Marker Block #4

```markdown
<!-- FIGURE_SCHEMATIC -->
Title: Distribution phase와 elimination phase의 경쟁 판정
Mode: R
Visual objective: 5초 안에 “terminal slope가 elimination을 대표하는 조건”과 “대표하지 못하는 조건”을 구분하게 한다.
Core message: Terminal phase는 자동으로 elimination phase가 아니라, distribution과 elimination의 속도 경쟁이 허락할 때만 elimination 해석에 안전하게 쓰인다.
Elements to include: 두 개의 병렬 lane; lane 1 = distribution이 빠르고 elimination이 상대적으로 느린 경우; lane 2 = distribution equilibrium 전에 elimination이 상당히 진행되는 경우; early distribution phase; terminal phase; AUC share; labels “terminal slope usable with caution” and “terminal slope may mislead”.
Elements to exclude: 새로운 약물 수치; 다구획 미분방정식; 실제 교과서 곡선의 형태·색상·배치 복제; NONMEM model code.
Suggested rendering: Mermaid
Caption: Distribution과 elimination의 상대 속도에 따라 terminal slope 해석의 안전성이 달라진다.
Alt text: 두 개의 병렬 흐름도가 distribution이 먼저 정리되는 경우와 elimination이 먼저 크게 진행되는 경우를 비교한다.
Source relation: Redrawn from textbook concept
<!-- /FIGURE_SCHEMATIC -->
```

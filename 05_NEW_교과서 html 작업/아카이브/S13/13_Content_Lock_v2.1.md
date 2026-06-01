# 13_Content Lock v2.1 — Figure Marker Insertion Patch

**Output mode**: PATCH MODE  
**Reason**: Content Lock v2는 본문 재출력 시 text drift 위험이 있고, retained marker count가 4개이므로 PATCH MODE를 적용한다. 본 파일은 Content Lock v2 본문을 재출력하지 않고, Figure Strategy Table + Briefs + Insertion Map만 제공한다. Phase 5 operator는 아래 Insertion Map을 사용해 unchanged Content Lock v2에 figure marker를 splice하여 v2.1을 생성한다.

**Image rights status**: None. 교과서 원그림 삽입(I)은 금지. 허용 모드는 Figure Pointer(P)와 새 도식 brief(N)뿐이다.

---

## 1. Figure Strategy Table — View A. Reading-order Figure Plan

| ID | Reading order | Location (§ + concept card) | Mode | Source figure / source object | Trigger | Why text alone is insufficient | Expected learning gain | Decision |
|---|---:|---|---|---|---|---|---|---|
| F1 | 1 | §1 — Session Header & Roadmap | N | Newly designed overview candidate | G3 | §1 Roadmap이 이미 C1→C2→C3→C4의 흐름을 텍스트와 code block으로 충분히 고정한다. 새 overview 도식은 장식적 중복이 될 가능성이 높다. | Incremental only. | **REJECT** — 제거해도 구조 이해가 크게 떨어지지 않음. |
| F2 | 2 | §2 C1. 변이의 구조적 분해 — θ, η, ε taxonomy | P | R&T p.366, Fig.12-6 — clearance distributions with same mean but different CV/shape | G2, G5 | “평균보다 분포가 먼저다”는 문장은 중요하지만, 같은 mean에서도 CV와 distribution shape가 달라지는 장면은 그림 없이는 즉시 보이지 않는다. | Learner가 θ 평균값만 보는 습관에서 벗어나, ω²와 shape가 dose individualization의 핵심임을 즉시 파악한다. | **KEEP** |
| F3 | 3 | §2 C2. 잔차 오차 모델 — additive / proportional / exponential | P | R&T p.371, Fig.12-12 — homoscedastic vs heteroscedastic parameter variability | G2, G5 | Additive/proportional/exponential error model은 식으로 읽으면 암기 항목이 되기 쉽다. Residual spread가 prediction scale에 따라 어떻게 달라지는지 시각적으로 봐야 ε model 선택의 의미가 생긴다. | Learner가 “ε의 실패가 η의 성공처럼 보인다”는 C2 tip을 residual spread pattern과 연결한다. | **KEEP** |
| F4 | 4 | §2 C3. 공변량 모델링 — CrCl, fu, and reparameterization | P | R&T p.369, Fig.12-9 — creatinine clearance covariate | G5 | CrCl covariate는 source-essential이지만 Content Lock v2의 C3 중심은 CrCl보다 PK50의 fu coordinate/reparameterization 구분이다. | Covariate의 일반론 보강은 가능하지만 PK50 confusion을 직접 해소하지는 못한다. | **REJECT** — C3의 핵심 혼동 제거 ROI가 F6보다 낮음. |
| F5 | 5 | §2 C3. 공변량 모델링 — CrCl, fu, and reparameterization | P | G&W p.705 Fig.50.1; p.707 Fig.50.2; p.708 Tables 50.1–50.2 | G2, G5 | PK50 원자료는 essential이지만 Fig.50.1, Fig.50.2, Table 50.1, Table 50.2를 모두 pointer로 열면 learner가 “무엇을 비교해야 하는지”보다 source object 탐색에 주의를 빼앗긴다. | High but fragmented. | **REJECT/MERGE** — F6의 새 schematic brief로 통합. |
| F6 | 6 | §2 C3. 공변량 모델링 — CrCl, fu, and reparameterization | N | Newly designed synthesis from PK50 source objects; no exact reproduction | G2, G4 | C3의 가장 위험한 혼동은 “fu가 ω²을 줄였다”와 “같은 자료를 total/unbound coordinate로 다시 표현했다”를 섞는 것이다. 이 구분은 단일 textbook figure 하나로는 충분히 정리되지 않는다. | Learner가 total→fu→unbound reparameterization과, 여전히 남는 PD variability를 한 장에서 분리한다. | **KEEP** |
| F7 | 7 | §2 C4. 유전적 다형성 — IIV의 불연속 substructure | P | R&T p.397 Fig.13-2 / p.398 Fig.13-4 candidate | G5 | CYP2D6 nortriptyline과 CYP2C9 warfarin은 중요한 예시이나, C4의 주된 교육 목표는 개별 약물 사례 확대가 아니라 smooth η가 polymodal substructure를 가질 수 있음을 체화시키는 것이다. | Useful but example-heavy. | **REJECT** — pharmacogenetic 사례 확장으로 C4가 비대해질 위험. |
| F8 | 8 | §2 C4. 유전적 다형성 — IIV의 불연속 substructure | P | R&T p.402, Fig.13-6 — isoniazid 6-h concentration bimodal acetylator distribution | G2, G5 | “polymodal distribution”은 텍스트로는 추상적이다. 실제 inherited phenotype이 bimodal concentration distribution으로 나타나는 장면을 보지 않으면 C4가 단순한 genotype list로 오해될 수 있다. | Learner가 genetic polymorphism을 covariate 목록이 아니라 η distribution의 모양 변화로 이해한다. | **KEEP** |

---

## 2. Figure Strategy Table — View B. Type-sorted Summary

### Pointers (P)
- **KEEP**: F2, F3, F8 → **3 / max 5**
- **REJECT**: F4, F5, F7
- Budget status: within A-Critical pointer budget.

### Schematics (R/N combined)
- **KEEP**: F6 → **1 / max 2**
- **REJECT**: F1
- Budget status: within A-Critical schematic budget.

### Images (I)
- **KEEP**: none → **0**
- Rationale: Image rights = None. 교과서 원그림 삽입은 금지.

### Final retained marker count
- Total retained markers: **4**
- Output mode consequence: marker count ≤4이므로 PATCH MODE 유지.

---

## 3. Figure Briefs — KEEP Items Only

### F2 — Mode P

- **Source**: Rowland & Tozer 5e, p.366, Figure 12-6 — frequency distributions for clearance of four hypothetical drugs.
- **Why this figure matters**: 같은 mean을 가져도 CV와 distribution shape가 다르면 individual dose decision의 의미가 완전히 달라진다. 특히 bimodal distribution에서는 mean이 population의 대표값이 아니라 오히려 가장 덜 그럴듯한 값이 될 수 있다.
- **When to look**: C1 card를 읽은 직후.
- **Learner instruction**: A/B/C에서 mean은 같지만 spread가 달라지는 점을 먼저 본다. 그다음 D에서 두 봉우리 사이에 mean이 놓이는 장면을 보고, 왜 θ만으로는 subgroup risk를 설명할 수 없는지 연결한다.

### F3 — Mode P

- **Source**: Rowland & Tozer 5e, p.371, Figure 12-12 — homoscedastic vs heteroscedastic parameter variability.
- **Why this figure matters**: Additive, proportional, exponential error model은 식만 보면 서로 다른 문법처럼 보인다. Figure 12-12는 residual spread가 일정한지, prediction 크기에 따라 커지는지를 눈으로 구분하게 해 준다.
- **When to look**: C2 card의 Formal Definition과 Code Structure를 읽은 뒤.
- **Learner instruction**: Error spread가 concentration 또는 prediction scale과 함께 변하는지 확인한다. 그 pattern을 C2의 “ε를 잘못 선언하면 ω² 또는 covariate 효과처럼 보인다”는 문장에 다시 연결한다.

### F6 — Mode N

- **Title**: PK50 coordinate split — total variability, fu reparameterization, and remaining PD variability
- **Visual objective**: 5초 안에 “protein binding은 total PK variability 일부를 설명하지만, PD response variability는 그대로 남는다”를 보이게 한다.
- **Core message**: PK50의 `fu`는 NONMEM covariate-model ω² reduction이 아니라 total coordinate를 unbound coordinate로 다시 표현하는 reparameterization이며, 이 변환 후에도 response variability는 별도 PD source로 남는다.
- **Elements to include**:
  - Left lane: `Total coordinate` — `Cl = 11.4 L·h⁻¹ (CV 28%)`, total concentration, total C >50 µg·L⁻¹ avoid.
  - Center node: `fu = 0.016 ± 0.0049` — deterministic reparameterization / coordinate change.
  - Right lane: `Unbound coordinate` — `Clu = 720 L·h⁻¹ (CV 9%)`, unbound-based safety margin.
  - Lower branch: `PD variability remains` — response 8-fold, `EC50 total 1.8 (CV 40%)` vs `EC50 unbound 0.029 (CV 60%)`, responder/non-responder.
  - Warning label: `Do not read as: fu covariate reduced ω²(CL) 28%→9%`.
- **Elements to exclude**:
  - Individual subject-level Table 50.3 values.
  - Infusion regimen calculation details.
  - Exact reproduction of Fig.50.1, Fig.50.2, Table 50.1, or Table 50.2 layout.
  - New variance propagation equations.
- **Suggested rendering**: Mermaid flowchart.
- **Caption**: PK50 shows that `fu` changes the coordinate system for PK interpretation, while PD response variability remains a separate source of between-subject variability.
- **Alt text**: Flow diagram showing total PK parameters transformed by `fu` into unbound parameters, with a separate lower branch indicating remaining pharmacodynamic response variability.
- **Source relation**: Newly designed.

### F8 — Mode P

- **Source**: Rowland & Tozer 5e, p.402, Figure 13-6 — isoniazid 6-hour concentration distribution after 9.8 mg/kg oral dose in 483 subjects.
- **Why this figure matters**: C4의 핵심은 유전 다형성이 단순 covariate label이 아니라 distribution shape 자체를 바꾼다는 점이다. Figure 13-6은 NAT2 acetylator status가 실제 concentration distribution을 bimodal하게 만드는 장면을 보여 준다.
- **When to look**: C4 card를 읽은 직후.
- **Learner instruction**: 두 peak가 어디에 생기는지 먼저 확인한다. 그런 다음 “η histogram이 두 봉우리라면 smooth log-normal IIV 하나로 덮으면 안 된다”는 C4 recap과 연결한다.

---

## 4. Insertion Map (PATCH MODE)

| ID | Reading order | Anchor (exact heading or first ≥40 chars of card) | Insert position | Marker block (full text) |
|---|---:|---|---|---|
| F2 | 2 | `### C1. 변이의 구조적 분해 — θ, η, ε taxonomy` | after this anchor card | `<!-- FIGURE_POINTER -->`<br>`Source: Rowland & Tozer 5e, p.366, Figure 12-6 — frequency distributions for clearance of four hypothetical drugs.`<br>`Why this matters: 같은 mean을 가져도 CV와 distribution shape가 다르면 individual dose decision의 의미가 완전히 달라진다. 특히 bimodal distribution에서는 mean이 population의 대표값이 아니라 오히려 가장 덜 그럴듯한 값이 될 수 있다.`<br>`When to look: after reading this card`<br>`Learner instruction: A/B/C에서 mean은 같지만 spread가 달라지는 점을 먼저 본다. 그다음 D에서 두 봉우리 사이에 mean이 놓이는 장면을 보고, 왜 θ만으로는 subgroup risk를 설명할 수 없는지 연결한다.`<br>`<!-- /FIGURE_POINTER -->` |
| F3 | 3 | `### C2. 잔차 오차 모델 — additive / proportional / exponential` | after this anchor card | `<!-- FIGURE_POINTER -->`<br>`Source: Rowland & Tozer 5e, p.371, Figure 12-12 — homoscedastic vs heteroscedastic parameter variability.`<br>`Why this matters: Additive, proportional, exponential error model은 식만 보면 서로 다른 문법처럼 보인다. Figure 12-12는 residual spread가 일정한지, prediction 크기에 따라 커지는지를 눈으로 구분하게 해 준다.`<br>`When to look: after reading this card`<br>`Learner instruction: Error spread가 concentration 또는 prediction scale과 함께 변하는지 확인한다. 그 pattern을 C2의 “ε를 잘못 선언하면 ω² 또는 covariate 효과처럼 보인다”는 문장에 다시 연결한다.`<br>`<!-- /FIGURE_POINTER -->` |
| F6 | 6 | `### C3. 공변량 모델링 — CrCl, fu, and reparameterization` | after this anchor card | `<!-- FIGURE_SCHEMATIC -->`<br>`Title: PK50 coordinate split — total variability, fu reparameterization, and remaining PD variability`<br>`Mode: N`<br>`Visual objective: 5초 안에 “protein binding은 total PK variability 일부를 설명하지만, PD response variability는 그대로 남는다”를 보이게 한다.`<br>`Core message: PK50의 fu는 NONMEM covariate-model ω² reduction이 아니라 total coordinate를 unbound coordinate로 다시 표현하는 reparameterization이며, 이 변환 후에도 response variability는 별도 PD source로 남는다.`<br>`Elements to include: Left lane: Total coordinate — Cl = 11.4 L·h⁻¹ (CV 28%), total concentration, total C >50 µg·L⁻¹ avoid; Center node: fu = 0.016 ± 0.0049 — deterministic reparameterization / coordinate change; Right lane: Unbound coordinate — Clu = 720 L·h⁻¹ (CV 9%), unbound-based safety margin; Lower branch: PD variability remains — response 8-fold, EC50 total 1.8 (CV 40%) vs EC50 unbound 0.029 (CV 60%), responder/non-responder; Warning label: Do not read as: fu covariate reduced ω²(CL) 28%→9%.`<br>`Elements to exclude: Individual subject-level Table 50.3 values; infusion regimen calculation details; exact reproduction of Fig.50.1, Fig.50.2, Table 50.1, or Table 50.2 layout; new variance propagation equations.`<br>`Suggested rendering: Mermaid`<br>`Caption: PK50 shows that fu changes the coordinate system for PK interpretation, while PD response variability remains a separate source of between-subject variability.`<br>`Alt text: Flow diagram showing total PK parameters transformed by fu into unbound parameters, with a separate lower branch indicating remaining pharmacodynamic response variability.`<br>`Source relation: Newly designed`<br>`<!-- /FIGURE_SCHEMATIC -->` |
| F8 | 8 | `### C4. 유전적 다형성 — IIV의 불연속 substructure` | after this anchor card | `<!-- FIGURE_POINTER -->`<br>`Source: Rowland & Tozer 5e, p.402, Figure 13-6 — isoniazid 6-hour concentration distribution after 9.8 mg/kg oral dose in 483 subjects.`<br>`Why this matters: C4의 핵심은 유전 다형성이 단순 covariate label이 아니라 distribution shape 자체를 바꾼다는 점이다. Figure 13-6은 NAT2 acetylator status가 실제 concentration distribution을 bimodal하게 만드는 장면을 보여 준다.`<br>`When to look: after reading this card`<br>`Learner instruction: 두 peak가 어디에 생기는지 먼저 확인한다. 그런 다음 “η histogram이 두 봉우리라면 smooth log-normal IIV 하나로 덮으면 안 된다”는 C4 recap과 연결한다.`<br>`<!-- /FIGURE_POINTER -->` |

---

## 5. Phase 5 Splicing Note

- 본 PATCH는 Content Lock v2 본문을 수정하지 않는다.
- 각 marker block은 해당 concept card의 끝, 다음 `###` heading 직전에 독립 block으로 삽입한다.
- 기존 source page tags, `[확인 필요]`, `<!-- ANNOTATION -->`, `<!-- MASTER LENS -->`, `<!-- ANCHOR -->`, `<!-- TRENCH -->`, `<!-- CONFUSION -->`, `<!-- SELF-TEST -->`, `<!-- RECAP -->` marker는 이동하거나 변경하지 않는다.
- Mode P는 교과서 원그림을 삽입하지 않고 학습자에게 source figure inspection을 지시하는 pointer다.
- Mode N은 Phase 5에서 새로 rendering할 brief이며, Mermaid/SVG/HTML code는 이 단계에서 생성하지 않는다.

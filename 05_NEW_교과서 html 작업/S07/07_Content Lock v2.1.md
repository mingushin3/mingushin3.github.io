# 07_Content Lock v2.1 — Figure Marker Patch
## Session 07: 치료역·항정상태·다중투여·축적

**Output mode declaration: PATCH MODE**

Content Lock v2는 약 11,000 words 수준으로 6,000 words를 초과한다. 따라서 본문 전체를 재출력하지 않고, Strategy Table + Figure Briefs + Insertion Map만 제공한다. Phase 5에서는 아래 marker block을 Content Lock v2 원문에 splice하여 v2.1을 생성한다.

**Image rights status**: None. 교과서 원그림은 삽입하지 않고 Pointer(P)로만 처리한다. 새 그림은 Content Lock의 locked text를 바탕으로 한 신규 schematic(N) brief만 제공하며, Mermaid/SVG/HTML 코드는 생성하지 않는다.

---

## 1. Figure Strategy Table — View A. Reading-order Figure Plan

| # | Reading order | Location (§ + concept card) | Mode | Source figure (if any) | Trigger | Why text alone is insufficient | Expected learning gain | Decision |
|---|---|---|---|---|---|---|---|---|
| 1 | §1 | Master Lens | N | None | G3, G4 | 이 세션의 핵심은 timing, level, amplitude의 분리인데, 본문만으로는 세 지배자가 서로 다른 질문에 답한다는 구조가 한눈에 고정되지 않는다. | 이후 M1–M8을 “세 지배자” 구조로 읽게 하는 chapter-level map을 제공한다. | KEEP |
| 2 | §2-M2 | 항정상태 도달 시간 | P candidate | G Fig.2.8 / R&T Table 10-4 | G5 | half-life별 plateau 접근은 중요하지만, Content Lock v2의 수식·숫자 설명과 #1 schematic이 이미 핵심을 충분히 고정한다. | 예산 초과 방지를 위해 제외. | REJECT — covered by #1 and text |
| 3 | §2-M3 | Apex Concept — 다중투여 축적인자 | P | R&T Fig.11-3 | G1, G2, G5 | “같은 average dosing rate인데 fluctuation만 달라진다”는 메시지는 텍스트만으로는 rate, interval, plateau approach, fluctuation의 분리가 쉽게 섞인다. | average level과 fluctuation을 분리하여 M3/M4 오류를 줄인다. | KEEP |
| 4 | §2-M4 | $C_{av,ss}$ vs $A_{av,ss}$ | N | None | G2, G4 | 이 세션의 MUST_FIX였던 차원 오류는 식을 읽어도 재발하기 쉽다. 농도식과 amount식을 같은 줄에 놓고 “V를 거칠 때만 변환”되는 방화벽을 시각화해야 한다. | concentration vs amount 차원 혼동을 차단하고 M4 식 잠금을 강화한다. | KEEP |
| 5 | §2-M5 | Flip-flop 동태 | P | G Fig.2.29 | G2, G5 | terminal slope의 정체가 elimination에서 absorption으로 바뀌는 순간은 곡선 모양을 보지 않으면 잘못 해석하기 쉽다. | Ka와 K의 역할 전환을 시각적으로 고정한다. | KEEP |
| 6 | §2-M6 | Therapeutic Window | P | R&T Fig.9-3 | G2, G5 | therapeutic concentration range, utility, threshold가 문장으로만 제시되면 TW를 단순 “좋은 농도 범위”로 오해하기 쉽다. | utility curve 관점으로 TW를 clinical decision frame으로 이해한다. | KEEP |
| 7 | §2-M6 | Antimicrobial anchor | P candidate | R&T Fig.10-20 / Fig.11-19 / Fig.11-20 | G5 | PK/PD index는 중요하지만 M6의 중심 그림은 TW/utility이고, antimicrobial figures는 보조 anchor 성격이다. | 예산 초과 방지를 위해 제외. | REJECT — context-level under current budget |
| 8 | §2-M7 | Loading + maintenance | P candidate | R&T Fig.11-4 | G5 | doxycycline loading/maintenance 그림은 유용하지만, M8의 TW-driven design figure가 loading/maintenance까지 포함해 더 넓은 ROI를 제공한다. | M8 pointer로 통합 대체. | REJECT — covered by #9 |
| 9 | §2-M8 | TW-Driven Dosage Design Algorithm | P | R&T Fig.11-10 | G1, G3, G5 | $C_{upper}$, $C_{lower}$, $	au_{max}$, $D_M$, $D_L$의 관계는 텍스트만으로는 algorithm flow와 concentration-time profile이 분리되어 보인다. | 치료역 기반 regimen design을 계산 절차와 농도 궤적으로 동시에 이해한다. | KEEP |
| 10 | §2-M7 | Daptomycin fractionation anchor | P | R&T Fig.11-24 + Table 11-7 | G2, G5 | “same daily dose” 비교군 교정과 CPK 차이는 표/프로파일을 직접 보지 않으면 25 q24h vs 25 q8h로 다시 오독될 위험이 있다. | fractionation, recovery time, toxicity를 Cmax/AUC 단일 지표와 분리해 읽는다. | KEEP |
| 11 | §2-M9-like content inside M6 | PD-driven plateau | P candidate | R&T Fig.11-16 / Fig.11-17 | G5 | atorvastatin/EPO는 강한 예시지만 Content Lock v2가 숫자 anchor를 충분히 제공하고, 그림 예산상 chapter-core보다 후순위다. | 필요 시 Phase 5에서 optional sidebar로 검토. | REJECT — budget priority |

---

## 2. Figure Strategy Table — View B. Type-sorted Summary

### Pointers (P)

- #3 — R&T Fig.11-3: same average dosing rate, different fluctuation.
- #5 — G Fig.2.29: flip-flop vs ordinary terminal slope.
- #6 — R&T Fig.9-3: therapeutic effectiveness/utility curves.
- #9 — R&T Fig.11-10: TW-driven regimen design.
- #10 — R&T Fig.11-24 + Table 11-7: daptomycin fractionation/toxicity.

**Budget check**: Pointers 5 / max 5 for A-Critical — compliant.

### Schematics (R/N combined)

- #1 — N: Three-dominator chapter map.
- #4 — N: $C_{av,ss}$ vs $A_{av,ss}$ dimension firewall.

**Budget check**: Schematics 2 / max 2 for A-Critical — compliant.

### Images (I)

- None.

**Budget check**: Image mode not used because Image rights = None.

---

## 3. Figure Briefs — KEEP Items Only

### Figure #1 — Three-dominator chapter map

- **Title**: 항정상태를 지배하는 세 질문: timing × level × amplitude
- **Mode**: N
- **Visual objective**: 학습자가 5초 안에 “도달 시간, 평균 수준, fluctuation은 서로 다른 지배자를 가진다”를 볼 수 있어야 한다.
- **Core message**: 항정상태는 하나의 숫자가 아니라 `언제 도달하는가`, `어디에 머무는가`, `얼마나 출렁이는가`의 세 질문으로 분해된다.
- **Elements to include**:
  - 중앙 노드: `Steady-state regimen interpretation`
  - 좌측 branch: `Timing` → `$t_{1/2}$` → `3–4 half-lives ≈ 90%`
  - 중앙 branch: `Average level` → `CL + average input rate` → `$C_{ss}$ / $C_{av,ss}$`
  - 우측 branch: `Amplitude / fluctuation` → `τ/t1/2` → `$R_{ac}$ and peak–trough swing`
  - 하단 warning: `Do not collapse these into one “steady-state” idea`
- **Elements to exclude**:
  - 개별 약물 수치
  - NONMEM code
  - 교과서 figure의 곡선 재현
- **Suggested rendering**: Mermaid
- **Caption**: 항정상태 해석의 핵심은 timing, level, amplitude를 서로 다른 parameter 질문으로 분리하는 것이다.
- **Alt text**: Steady-state interpretation branches into timing controlled by half-life, average level controlled by clearance and input rate, and fluctuation controlled by dosing interval relative to half-life.
- **Source relation**: Newly designed

### Figure #3 — R&T Fig.11-3 pointer

- **Source**: Rowland & Tozer 5e, p.325, Fig. 11-3.
- **Why this figure matters**: 이 그림은 같은 average dose rate가 같은 average amount plateau approach를 만들지만, dosing frequency는 fluctuation을 바꾼다는 점을 직접 보여준다. M3의 “dose가 아니라 τ/t1/2가 축적과 fluctuation을 지배한다”는 해석의 핵심 시각 anchor다.
- **When to look**: §2-M3의 `Three-dominator lock`을 읽은 직후.
- **Learner instruction**: 두 곡선의 average approach가 같은지 먼저 보고, 그 다음 peak–trough swing이 어떻게 달라지는지 보라. “평균 수준”과 “출렁임”을 같은 말로 읽지 말라.

### Figure #4 — $C_{av,ss}$ vs $A_{av,ss}$ dimension firewall

- **Title**: $C_{av,ss}$와 $A_{av,ss}$의 차원 방화벽
- **Mode**: N
- **Visual objective**: 학습자가 농도식과 amount식을 같은 줄에 등치하면 안 된다는 것을 즉시 볼 수 있어야 한다.
- **Core message**: $C_{av,ss}$는 concentration이고 $A_{av,ss}$는 amount이며, 1-compartment 조건에서 V를 거칠 때만 서로 연결된다.
- **Elements to include**:
  - 좌측 box: `$C_{av,ss}` = average concentration` / unit: concentration / equation: `$F·Dose/(CL·τ)$`
  - 우측 box: `$A_{av,ss}` = average amount` / unit: amount / equation: `$1.44·F·Dose·t_{1/2}/τ$`
  - 중앙 firewall label: `Do not equate directly`
  - 조건부 bridge: `Only when 1-compartment and V known: $C_{av,ss}=A_{av,ss}/V$`
- **Elements to exclude**:
  - additional derivation of MRT
  - multi-compartment exceptions beyond the locked sentence
  - extra numerical examples
- **Suggested rendering**: CSS-card
- **Caption**: 평균농도와 평균 amount는 같은 steady-state idea에서 나오지만 차원이 다르므로 직접 등치하면 안 된다.
- **Alt text**: A comparison card separates average concentration from average amount, with a firewall between them and a conditional bridge through volume only in a one-compartment setting.
- **Source relation**: Newly designed

### Figure #5 — G Fig.2.29 pointer

- **Source**: Gabrielsson & Weiner 5e, p.45, Fig. 2.29.
- **Why this figure matters**: Flip-flop은 문장으로는 “흡수가 느리다”로 지나가기 쉽지만, 실제 오류는 terminal slope를 elimination slope로 잘못 읽는 데서 발생한다. 그림은 ordinary case와 flip-flop case의 terminal phase 정체를 분리해준다.
- **When to look**: §2-M5의 `Clinical asymmetry`를 읽기 전.
- **Learner instruction**: terminal tail이 더 길어졌을 때 먼저 `Ka < K` 가능성을 확인하라. 긴 terminal half-life를 곧바로 느린 elimination으로 번역하지 말라.

### Figure #6 — R&T Fig.9-3 pointer

- **Source**: Rowland & Tozer 5e, p.272, Fig. 9-3.
- **Why this figure matters**: Therapeutic window를 단순 농도범위가 아니라 effectiveness, adverse response, utility의 balance로 보게 하는 원문 핵심 그림이다. Content Lock v2의 utility formalization lock을 원문 곡선 직관으로 되돌려준다.
- **When to look**: §2-M6의 `Term lock`과 `Utility formalization lock` 사이.
- **Learner instruction**: effectiveness curve와 utility curve를 같은 것으로 보지 말고, utility가 benefit과 harm을 함께 반영한다는 점을 확인하라. TW는 농도축 위에 그려진 decision zone이다.

### Figure #9 — R&T Fig.11-10 pointer

- **Source**: Rowland & Tozer 5e, p.335, Fig. 11-10.
- **Why this figure matters**: M8의 식들은 각각 맞더라도, learner는 $C_{upper}$, $C_{lower}$, $	au_{max}$, $D_M$, $D_L$이 하나의 regimen design sequence라는 점을 놓칠 수 있다. 이 그림은 therapeutic window와 loading/maintenance profile을 같은 frame 안에 묶는다.
- **When to look**: §2-M8의 `Algorithm lock`을 읽은 직후.
- **Learner instruction**: 먼저 upper/lower bound가 투여간격을 어떻게 제한하는지 보고, 그 다음 maintenance dose와 loading dose가 profile 안에서 어떤 위치를 차지하는지 확인하라.

### Figure #10 — Daptomycin figure/table pointer

- **Source**: Rowland & Tozer 5e, p.352 Fig. 11-24 and p.353 Table 11-7.
- **Why this figure matters**: Daptomycin anchor는 본 세션에서 “same daily dose” 비교군을 잘못 잡으면 결론 전체가 뒤집히는 고위험 지점이다. Fig. 11-24와 Table 11-7을 함께 보아야 concentration profile, daily dose, CPK 결과가 분리된다.
- **When to look**: §2-M7의 `Daptomycin fractionation anchor`를 읽은 직후.
- **Learner instruction**: Study A에서 같은 daily dose 비교가 `75 mg/kg q24h` vs `25 mg/kg q8h`인지 확인하라. 그 다음 CPK 열을 보면서 fractionation/recovery time이 toxicity 해석에 왜 필요한지 확인하라.

---

## 4. Insertion Map (PATCH MODE)

| # | Reading order | Anchor copied verbatim from Content Lock v2 | Insert position | Marker block |
|---|---|---|---|---|
| 1 | §1 | `## 1. Master Lens` | before next §heading | See Marker Block #1 |
| 3 | §2-M3 | `## §2-M3. Apex Concept — 다중투여 축적인자 $R_{ac}=1/(1-e^{-K\tau})$` | before next §heading | See Marker Block #3 |
| 4 | §2-M4 | `## §2-M4. 항정상태 평균농도와 평균 amount: $C_{av,ss}$ vs $A_{av,ss}$` | before next §heading | See Marker Block #4 |
| 5 | §2-M5 | `## §2-M5. Flip-flop 동태: $K_a<K$일 때 terminal slope의 정체` | before next §heading | See Marker Block #5 |
| 6 | §2-M6 | `## §2-M6. Therapeutic Window — PK 식을 임상 의사결정으로 바꾸는 제약조건` | before next §heading | See Marker Block #6 |
| 9 | §2-M8 | `## §2-M8. TW-Driven Dosage Design Algorithm` | before next §heading | See Marker Block #9 |
| 10 | §2-M7 | `### Daptomycin fractionation anchor` | after this anchor subsection, before `<!-- RECAP -->` | See Marker Block #10 |

### Marker Block #1

```markdown
<!-- FIGURE_SCHEMATIC -->
Title: 항정상태를 지배하는 세 질문: timing × level × amplitude
Mode: N
Visual objective: 학습자가 5초 안에 “도달 시간, 평균 수준, fluctuation은 서로 다른 지배자를 가진다”를 볼 수 있어야 한다.
Core message: 항정상태는 하나의 숫자가 아니라 `언제 도달하는가`, `어디에 머무는가`, `얼마나 출렁이는가`의 세 질문으로 분해된다.
Elements to include: 중앙 노드 `Steady-state regimen interpretation`; branch 1 `Timing → t1/2 → 3–4 half-lives ≈ 90%`; branch 2 `Average level → CL + average input rate → Css/Cav,ss`; branch 3 `Amplitude/fluctuation → τ/t1/2 → Rac and peak–trough swing`; 하단 warning `Do not collapse these into one steady-state idea`.
Elements to exclude: 개별 약물 수치; NONMEM code; 교과서 figure의 곡선 재현.
Suggested rendering: Mermaid
Caption: 항정상태 해석의 핵심은 timing, level, amplitude를 서로 다른 parameter 질문으로 분리하는 것이다.
Alt text: Steady-state interpretation branches into timing controlled by half-life, average level controlled by clearance and input rate, and fluctuation controlled by dosing interval relative to half-life.
Source relation: Newly designed
<!-- /FIGURE_SCHEMATIC -->
```

### Marker Block #3

```markdown
<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.325, Fig. 11-3
Why this matters: 같은 average dose rate가 같은 average amount plateau approach를 만들지만, dosing frequency는 fluctuation을 바꾼다는 점을 직접 보여준다. M3의 “dose가 아니라 τ/t1/2가 축적과 fluctuation을 지배한다”는 해석의 핵심 시각 anchor다.
When to look: §2-M3의 `Three-dominator lock`을 읽은 직후.
Learner instruction: 두 곡선의 average approach가 같은지 먼저 보고, 그 다음 peak–trough swing이 어떻게 달라지는지 보라. “평균 수준”과 “출렁임”을 같은 말로 읽지 말라.
<!-- /FIGURE_POINTER -->
```

### Marker Block #4

```markdown
<!-- FIGURE_SCHEMATIC -->
Title: Cav,ss와 Aav,ss의 차원 방화벽
Mode: N
Visual objective: 학습자가 농도식과 amount식을 같은 줄에 등치하면 안 된다는 것을 즉시 볼 수 있어야 한다.
Core message: Cav,ss는 concentration이고 Aav,ss는 amount이며, 1-compartment 조건에서 V를 거칠 때만 서로 연결된다.
Elements to include: 좌측 box `Cav,ss = average concentration`, unit `concentration`, equation `F·Dose/(CL·τ)`; 우측 box `Aav,ss = average amount`, unit `amount`, equation `1.44·F·Dose·t1/2/τ`; 중앙 firewall label `Do not equate directly`; 조건부 bridge `Only when 1-compartment and V known: Cav,ss = Aav,ss/V`.
Elements to exclude: MRT의 추가 도출; locked sentence를 넘어서는 multi-compartment 예외; 추가 수치 예시.
Suggested rendering: CSS-card
Caption: 평균농도와 평균 amount는 같은 steady-state idea에서 나오지만 차원이 다르므로 직접 등치하면 안 된다.
Alt text: A comparison card separates average concentration from average amount, with a firewall between them and a conditional bridge through volume only in a one-compartment setting.
Source relation: Newly designed
<!-- /FIGURE_SCHEMATIC -->
```

### Marker Block #5

```markdown
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.45, Fig. 2.29
Why this matters: Flip-flop은 문장으로는 “흡수가 느리다”로 지나가기 쉽지만, 실제 오류는 terminal slope를 elimination slope로 잘못 읽는 데서 발생한다. 그림은 ordinary case와 flip-flop case의 terminal phase 정체를 분리해준다.
When to look: §2-M5의 `Clinical asymmetry`를 읽기 전.
Learner instruction: terminal tail이 더 길어졌을 때 먼저 `Ka < K` 가능성을 확인하라. 긴 terminal half-life를 곧바로 느린 elimination으로 번역하지 말라.
<!-- /FIGURE_POINTER -->
```

### Marker Block #6

```markdown
<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.272, Fig. 9-3
Why this matters: Therapeutic window를 단순 농도범위가 아니라 effectiveness, adverse response, utility의 balance로 보게 하는 원문 핵심 그림이다. Content Lock v2의 utility formalization lock을 원문 곡선 직관으로 되돌려준다.
When to look: §2-M6의 `Term lock`과 `Utility formalization lock` 사이.
Learner instruction: effectiveness curve와 utility curve를 같은 것으로 보지 말고, utility가 benefit과 harm을 함께 반영한다는 점을 확인하라. TW는 농도축 위에 그려진 decision zone이다.
<!-- /FIGURE_POINTER -->
```

### Marker Block #9

```markdown
<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.335, Fig. 11-10
Why this matters: M8의 식들은 각각 맞더라도, learner는 Cupper, Clower, τmax, DM, DL이 하나의 regimen design sequence라는 점을 놓칠 수 있다. 이 그림은 therapeutic window와 loading/maintenance profile을 같은 frame 안에 묶는다.
When to look: §2-M8의 `Algorithm lock`을 읽은 직후.
Learner instruction: 먼저 upper/lower bound가 투여간격을 어떻게 제한하는지 보고, 그 다음 maintenance dose와 loading dose가 profile 안에서 어떤 위치를 차지하는지 확인하라.
<!-- /FIGURE_POINTER -->
```

### Marker Block #10

```markdown
<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.352 Fig. 11-24 and p.353 Table 11-7
Why this matters: Daptomycin anchor는 본 세션에서 “same daily dose” 비교군을 잘못 잡으면 결론 전체가 뒤집히는 고위험 지점이다. Fig. 11-24와 Table 11-7을 함께 보아야 concentration profile, daily dose, CPK 결과가 분리된다.
When to look: §2-M7의 `Daptomycin fractionation anchor`를 읽은 직후.
Learner instruction: Study A에서 같은 daily dose 비교가 `75 mg/kg q24h` vs `25 mg/kg q8h`인지 확인하라. 그 다음 CPK 열을 보면서 fractionation/recovery time이 toxicity 해석에 왜 필요한지 확인하라.
<!-- /FIGURE_POINTER -->
```

---

## 5. Patch Application Notes

1. Content Lock v2 본문 문장은 수정하지 않는다.
2. 위 7개 marker block만 지정 anchor 위치에 삽입한다.
3. 교과서 그림은 원본 이미지로 삽입하지 않는다. Pointer(P)는 “source figure를 보라”는 callout으로만 렌더링한다.
4. N schematic은 Phase 5에서 새로 그리되, 교과서 그림의 배치·색·형태를 복제하지 않는다.
5. 이 patch를 적용한 산출물이 `07_Content Lock v2.1`이다.

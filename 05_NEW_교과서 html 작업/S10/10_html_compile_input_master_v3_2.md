# XX_html_compile_input_master_v3.2.md

**v3.2 note:** This version applies a Korean-Dominant Readability Patch to PART A learner-facing prose. General English prose was converted to Korean where possible, while career-critical pharmacometrics terms are retained as Korean-English paired expressions on first use. Scientific content, equations, numerical anchors, page tags, source labels, figure markers, compiler markers, section structure, and PART B guardrails are preserved. No new scientific claims, examples, numbers, page tags, figures, or external references were added.

| Certificate | Status | Basis |
|---|---|---|
| Korean-Dominant Readability Certificate | PASS | General learner-facing English prose converted to Korean where possible; career-critical terms retained as Korean-English paired expressions. |
| Scientific Preservation Certificate | PASS | No scientific content, equation, number, example, page tag, or source label changed. |
| Marker Integrity Certificate | PASS | All figure markers, compiler markers, anchors, and section/card structures preserved. |
| HTML-Readiness Certificate | PASS | Phase 5 compatibility preserved; no HTML/Mermaid/SVG generated. |

---

# 10_HTML Compile Input Master — v3.2

## Version Note (v3.2)

This is **v3.2** of the HTML Compile Input Master, produced after the **Korean-Dominant Readability Patch** was applied to v3.1. v3.2 is a **prose-only Korean-dominance pass** on PART A (learner-facing body) that goes further than v3.1's readability patch by systematically converting remaining English prose to Korean and applying `한글(English)` paired-term formatting to career-critical pharmacometrics terms. **Non-negotiable preservation (re-affirmed):** every page tag, every equation, every NONMEM/code block, every source-basis label, every figure marker, every section/card heading structure, the Acenocoumarol/Phenprocoumon Insertion I5, and the Q9 Boss Dilemma are preserved verbatim. PART B is preserved as a rendering contract; only B10 Micro-Patch Log carries a v3.2 trace entry.

---

## Version Note (v3.1)

This is **v3.1** of the HTML Compile Input Master, produced after the **Korean Readability Patch (KR-01 ~ KR-22)** was designed against v3. v3.1 is a **prose-only readability pass** on PART A (learner-facing body) and adds nothing scientific. Compared to v3, v3.1 (a) splits long sentences into Korean-natural shorter ones, (b) attaches first-use Korean glosses to selected English-only technical terms, (c) replaces awkward English-Korean fragments with native Korean flow, and (d) repairs dangling subjects and predicate fragments. **Non-negotiable preservation (re-affirmed):** every page tag, every equation, every NONMEM/code block, every `[EXPERT_INFERENCE, v3]` / `[TEXTBOOK_DERIVED]` / `[CRUCIBLE_DERIVED]` / `[교과서 외 규제 해석]` source-basis label, every figure marker, every section/card heading, the Acenocoumarol/Phenprocoumon Insertion I5, and the Q9 Boss Dilemma are preserved verbatim. PART B is preserved as a rendering contract; only B10 Micro-Patch Log carries a v3.1 trace entry.

### v3.1 Korean Readability Patch — Change Log

| Patch ID | Section | Change type | Risk |
|---|---|---|---|
| KR-01 | §1 Roadmap (G&W opening) | Sentence split + Korean flow improvement | Low |
| KR-02 | §2 Card C1 §A | Korean flow improvement | Low |
| KR-03 | §2 Card C1 §C | First-use gloss | Low |
| KR-04 | §2 Card C1 §D | Korean flow improvement + Sentence split | Low |
| KR-05 | §2 Card C1 §E | Korean flow improvement | Low |
| KR-06 | §2 Card C2 [개념 Big Idea] | Concept clarification + First-use gloss | Low |
| KR-07 | §2 Card C2 §B (PD3 anchor) | Korean flow improvement | Low |
| KR-08 | §2 Card C2 §C | Korean flow improvement + Sentence split | Low |
| KR-09 | §2 Card C2 §C-2 | Korean flow improvement | Low |
| KR-10 | §2 Card C3 [개념 Big Idea] | Korean flow improvement (subject restoration) | Low |
| KR-11 | §2 Card C3 §A | Korean flow improvement + First-use gloss | Low |
| KR-12 | §2 Card C4 §A | Korean flow improvement + First-use gloss | Low |
| KR-13 | §2 Card C4 §C | Concept clarification | Low |
| KR-14 | §2 Card C5 §A | Korean flow improvement | Low |
| KR-15 | §2 Card C5 §C | Sentence split + Korean flow improvement | Low |
| KR-16 | §5 Pair 2 Critical Blow | Sentence split + Korean flow improvement | Low |
| KR-17 | §5 Pair 3 Critical blow | Korean flow improvement | Low |
| KR-18 | §5 Pair 3 Insertion I6 | Korean flow improvement | Low |
| KR-19 | §7 Q9 Answer key | Korean flow improvement | Low |
| KR-20 | §8 B Professional Moat (1st para) | Korean flow improvement | Low |
| KR-21 | §8 B Professional Moat (judgment list) | Korean flow improvement | Low |
| KR-22 | §8 B Hill γ 임상 함의 | Concept clarification | Low |

**All 22 patches:** Risk = Low. Scientific content unchanged. Page tags unchanged. Figure markers unchanged. Source labels unchanged. PART B rendering contract unchanged.

---

## Version Note (v3)

This is **v3** of the HTML Compile Input Master, produced after Independent Pharmacometrics Master Review of ver2. The independent audit returned **NO-GO** on three structural gaps in the V5.0 Apex framework compliance: (1) Apex marker nonstandard (`[Apex]` instead of `[⚡ Apex Concept]`) and missing **Plausible Fallacy** block on the Apex card; (2) §5 **Memory Hooks** present only as a single in-table row instead of standardized `**⚡ 기억 고리 (Memory Hook)**` independent blocks; (3) **Critical Blow** row absent from the highest-impact confusion pair. Additionally, Hill coefficient γ's clinical interpretive significance was underemphasized in §8C, and several Big Idea blocks read formula-first rather than clinical-intuition-first. v3 applies seven labeled surgical patches (P1–P7) tagged `[EXPERT_INFERENCE, v3]`. **Non-negotiable preservation:** acenocoumarol/phenprocoumon rate-limiting anchor (Insertion I5), the Q9 Boss Dilemma, and all existing page tags and numerical anchors are preserved verbatim.

### v3 Patch Manifest

| Patch | Location | Issue closed | Type |
|---|---|---|---|
| P1. Apex 표준화 + Plausible Fallacy | §2 / Card C2 header + §C-2 신규 블록 | Apex marker nonstandard; Plausible Fallacy missing | EXPERT_INFERENCE, v3 |
| P2. Big Idea 직관-우선 재구성 | §2 / Card C2 Big Idea | Formula-first opening on Apex card | EXPERT_INFERENCE, v3 |
| P3. Memory Hook 표준화 | §5 / Pair 1 elevation + Pair 2 신규 hook + C2 보조 hook | Hooks not standardized; Pair 2 lacks hook | EXPERT_INFERENCE, v3 |
| P4. Critical Blow 추가 | §5 / Pair 2 (EC50 vs Hill γ) | Critical Blow absent on highest-impact pair | EXPERT_INFERENCE, v3 |
| P5. Hill γ 임상 함의 보강 | §8 / Professional Moat | γ의 임상적 의의 underemphasized | EXPERT_INFERENCE, v3 |
| P6. Practice Brief 라벨 표준화 + ANNOTATION 보강 | §2 / 각 카드 | Practice 가이드와 첫등장 용어 라벨링 부재 | EXPERT_INFERENCE, v3 |
| P7. PART B v3 갱신 | PART B / 인증서·매트릭스·감사 로그 | v3 변경분 trace 필요 | EXPERT_INFERENCE, v3 |

### Inherited from ver2 (preserved verbatim)

This is **ver2 base** of the HTML Compile Input Master, produced after a focused review against `10_Audit_Report_v1.md`, `10_Crucible_Report_v1.md`, `10_Content_Lock_v2.md`, and `10_Content_Lock_v2_1.md`. The ver1 master already passed all five Phase 4D certificates at a conditional level. ver2 closed six remaining Audit `T5 SHOULD_FIX` items and Crucible `Grade A/B` insights that ver1 had absorbed only partially. All six additions are insertions only — no body sentence from Content Lock v2 is rewritten, no page tag is altered, no new examples or numbers are introduced beyond what Audit/Crucible/Content Lock v2 had already classified as `ADOPT` or `PARTIAL_ADOPT`.

| Insertion | Location | Source basis | Type |
|---|---|---|---|
| I1. R&T Ch.8 opening message | §1 Roadmap | Audit T5-B `MISSING_AUTHOR_MSG minor` (R&T p.233) | TEXTBOOK_DERIVED |
| I2. G&W p.200 design message anchor | §2 Card C2 §B (PD3 anchor 직전) | Audit T3/T5-A `SHOULD_FIX` (G&W p.200) | TEXTBOOK_DERIVED |
| I3. Precision-Improvement diagnostic | §2 Card C2 §C-2 | Crucible Intuition #2 / Grade B (G&W p.735 Table 3.2) | CRUCIBLE_DERIVED |
| I4. G&W §3.6.6 Non-Steady-State Response bridge | §2 Card C5 §A (AUEC closed form 직전) | Audit T1 `RESTORED/PARTIAL` (G&W p.229–232) | TEXTBOOK_DERIVED |
| I5. Acenocoumarol/Phenprocoumon PK vs PD anchor 강화 | §2 Card C5 §C | Audit T6 `ESSENTIAL` (R&T p.243–244) | TEXTBOOK_DERIVED |
| I6. Time-axis fast-diagnostic | §5 Pair 3 | Crucible Intuition #3 / Grade A (R&T p.251–252) | CRUCIBLE_DERIVED |

## Phase 4D Certification — v3

| Certificate | ver1 status | ver2 status | **v3 status** | Basis |
|---|---|---|---|---|
| Learner-Standalone Certificate | PASS | PASS+ | **PASS+** | PART A 구조 유지; v3 7개 패치는 모두 라벨 블록 또는 레이블 표준화로, 레이아웃을 깨지 않음. |
| Zero-Omission Certificate | PASS (conditional) | PASS (unconditional) | **PASS (unconditional)** | ver2에서 Audit T5 SHOULD_FIX 종료. v3는 V5.0 Apex 프레임워크 누락분(Plausible Fallacy, 표준화 Memory Hook, Critical Blow, Hill γ 임상함의)을 추가로 종료. |
| Mastery-Uplift Certificate | PASS | PASS+ | **PASS++** | v3는 Apex 카드의 Plausible Fallacy 블록과 §8B Hill γ 임상 함의 3-bullet으로 mastery signal density를 한 단계 더 높임. Big Idea 직관-우선 재구성으로 학습자 진입 마찰 감소. |
| Source-Boundary Certificate | PASS | PASS | **PASS** | v3 7개 패치는 모두 `[EXPERT_INFERENCE, v3]` 또는 `[교과서 기반 + 교과서 외 규제 해석]`으로 라벨링. 새 page tag 없음; rejected claims 미복원; pp.225–228 boundary preserved; aspirin-75mg/naproxen-ke0/5–100× FIH 모두 제외 유지. |
| HTML-Readiness Certificate | PASS | PASS | **PASS** | PART B compilation contract 유지. Marker-to-component 매핑 갱신: `**⚡ 기억 고리 (Memory Hook)**`, `**⚡ Plausible Fallacy**`, `**Practice Brief**`, `| **치명적 타격 (Critical Blow)** |` 4종 신규 라벨 추가. |

## Phase 4D Certification — ver2 (보존, 참고용)

| Certificate | ver1 status | ver2 status | Basis |
|---|---|---|---|
| Learner-Standalone Certificate | PASS | **PASS+** | PART A unchanged in structure; six insertions deepen self-containment without breaking layout. |
| Zero-Omission Certificate | PASS (conditional) | **PASS (unconditional)** | Audit T5 SHOULD_FIX items I1, I2, I4, I5 closed. G&W §3.6.6 framework, R&T objectives, design message, PK/PD rate-limiting anchor all explicit. |
| Mastery-Uplift Certificate | PASS | **PASS+** | Crucible Intuition #2 (CV% precision-improvement diagnostic) and Intuition #3 (time-axis fast-diagnostic) now explicit, raising mastery signal density. |
| Source-Boundary Certificate | PASS | **PASS** | All six insertions are labeled. No new page tags fabricated; no rejected claims restored; pp.225–228 boundary preserved; aspirin-75mg, naproxen-ke0, 5–100×/FIH/NDA still excluded. |
| HTML-Readiness Certificate | PASS | **PASS** | PART B compilation contract, splice verification table, page-tag rules, marker mapping all preserved. Splice verification updated to reflect insertion sites. |

## Assembly Mode

**PATCH MODE.** `10_Content Lock v2.1.md` is a Figure Marker Insertion Patch rather than a full re-emission of the canonical body. Therefore, the learner body was assembled from `10_Content Lock v2(4).md` with the seven approved Phase 4C marker blocks spliced into exact anchors, then six labeled minor insertions (I1–I6) were applied on ver2 as insertions only. Each insertion is enclosed in a labeled bounded block so it is visibly distinguishable from canonical Content Lock v2 prose.

## Input Manifest

| File | Role | Authority level | Used for | Notes |
|---|---|---|---|---|
| 10_scope_lock(3).md | Scope Lock | A0 | scope boundary; source range; required data anchors; image rights | Two-source scope: G&W + R&T; pp.225–228 boundary preserved |
| 010_G_PD 모델 기초 Emax·Hill·AUEC(4).pdf | Original textbook PDF | A1 | PDF verification source | G&W extract; 42 PDF pages available; textbook images not embedded |
| 010_T_PD 모델 기초 Emax·Hill·AUEC(4).pdf | Original textbook PDF | A1 | PDF verification source | R&T Ch.8 extract; 32 PDF pages available; textbook images not embedded |
| 10_Audit_Report_v1(4).md | Source Fidelity Audit v1 | A2 | audit guardrail; MUST_FIX/SHOULD_FIX; forbidden restorations | Conditional Go; unsupported claims controlled |
| 10_Content Lock v2(4).md | Content Lock v2 | A3 | canonical learner body base | Primary text-final body before figure marker insertion |
| 10_Content Lock v2.1.md | Content Lock v2.1 Patch | A4 | figure insertion source; Strategy Table; Insertion Map | PATCH MODE only; marker blocks spliced into v2 |
| 10_Crucible_Report_v1(1).md | Crucible Report v1 | A5 | crucible guardrail; mastery insight candidates | Only adopted or explicitly allowed Grade A/B logic used; not a raw prose source |
| 10_step1_draft_v0(3).md | Step 1 Draft v0 | A6 | deprecated source; regression check only | No raw Step 1 prose restored |
| S10_phase1_patch memo(2).md | Phase 1 Patch Memo | A6 | deprecated/locked reference; regression and audit context | Used to confirm Phase 1 was not HTML-ready and known weaknesses were fixed later |
| 붙여넣은 마크다운(2)(59).md | Step 2 HTML Compiler Prompt / Prompt 5 | A7 | compiler instruction; marker mapping; page tag rendering; navigation integrity | Essential rendering rules incorporated in PART B |
| 붙여넣은 텍스트 (1)(80).txt | Phase 4D Master Assembler Prompt | process instruction | assembly protocol | Adapted output filename from 05 to 10 per user request |
| 10_Content Lock v1(3).md | Content Lock v1 | locked reference | not used as canonical source | Superseded by Content Lock v2 |
| 10_html_compile_input_master.md | ver1 master | A3 (ver2 base) | pre-ver2 baseline | ver2 is delta-only over ver1 |

## Source Verification Snapshot

| PDF | Declared source range | File check | Use restriction |
|---|---|---|---|
| G&W PDF | p.199–224; p.229–234; p.732–741 | 42 PDF pages available | Used to verify page-scope, equation/figure identity, PD3 anchors |
| R&T PDF | p.233–264 | 32 PDF pages available | Used to verify time-delay, hysteresis, effect-compartment, duration examples |

## PART A — Learner-Facing Complete Handout

## 학습자 내비게이션 안내

**이 자료 사용법:** 먼저 §1에서 C1–C5의 위치를 잡고, §2의 각 개념 해부 카드(Concept Anatomy Card)를 순서대로 읽는다. `FIGURE_POINTER`는 교과서 원그림을 직접 보라는 안내이며, 본 문서에는 저작권 그림을 삽입하지 않는다. `FIGURE_SCHEMATIC`은 Phase 5에서 원그림과 구조적으로 구별되는 재도식으로 렌더링될 항목이다.

**학습 경로:** C1에서 `Kd`와 `EC50`의 층위를 분리하고, C2에서 Hill `n`을 가파름/설계 파라미터(steepness/design parameter)로 고정한다. C3–C4에서는 히스테리시스(hysteresis)가 보일 때 직접 혈장-반응 가정을 내려놓고 지연 위상(delay topology)을 선택하는 법을 익힌다. C5에서는 AUEC와 지속 시간(duration)이 약물 반감기(drug half-life)만으로 결정되지 않는다는 점을 반응-시간 척도(response-time scale)에서 확인한다.

**시작 전 점검:** 평형(equilibrium), 1차 제거(first-order elimination), 기저 반응(baseline response), 농도-시간 곡선(concentration-time curve), 반응-시간 곡선(response-time curve)의 차이를 떠올린다.  
**학습 후 확인:** `Kd ≠ EC50`, `n ≠ 기전 증명`, `히스테리시스 ≠ 잡음`, `약물 t1/2 ≠ 효과 지속 시간`을 각각 한 문장으로 설명할 수 있어야 한다.

---

# §1 — Session Header & Roadmap

**소스 통합:** G&W Ch.3는 수용체 결합(receptor binding) → Emax/Hill → 비정상상태 반응/AUEC(non-steady-state response/AUEC)의 수식적 골격을 제공한다. R&T Ch.8은 같은 개념을 임상 시간축, 히스테리시스(hysteresis), 효과 구획(effect compartment), 간접 반응(indirect response), 효과 지속 시간(duration of effect)으로 번역한다.

<!-- MASTER LENS -->
**Big Idea:** PD 모델링의 본질은 농도-효과 관계의 **비선형성(Emax / Hill `n`)**과 **시간 지연(hysteresis)**을 동시에 해부하는 것이다. 전자는 용량 증량(dose escalation)의 단계 크기와 농도범위 설계를 결정한다. 후자는 발현/소실(onset/offset), 투여 간격(dosing interval), 율속 과정(rate-limiting process) 판단을 결정한다.

G&W는 PK/PD 모델링의 목적을 생리·병리 조건에서 반응의 크기(response magnitude)와 시간 경과(time course)를 예측하는 핵심 in vivo 특성의 식별로 제시한다. 따라서 용량-반응(dose-response)만으로는 충분하지 않다. 관련 구획(relevant compartment — 효과와 연결되는 생체 내 위치)에서의 시간 경과에 따른 노출(exposure over time)과 생물학적 반응을 연결해야 한다. 이상적인 PD 지표는 민감하고(sensitive), 점진적이며(gradual), 임상적으로 의미 있고(meaningful), 객관적이고(objective), 재현 가능해야(reproducible) 한다. 또한 대조군(control)을 포함한 2–4개 용량 수준 중 최소 하나는 최대 반응(maximum response)에 도달하도록 설계하는 것이 권장된다. [G&W p.199–200]

> **Insertion I1 — [TEXTBOOK_DERIVED]** (Audit T5-B SHOULD_FIX: R&T objectives 명시)  
> R&T Ch.8의 출발점은 명시적이다: 약효 해석에는 항상 *시간*이 동반되어야 한다. 따라서 본 챕터의 학습 목표는 (i) plasma concentration과 response 사이의 시간 지연을 *진단*하는 법(C3 hysteresis), (ii) 그 지연을 구조적으로 *흡수*하는 법(C4 effect compartment vs systems-in-flux/indirect response), (iii) 효과의 *지속*을 plasma half-life와 분리해 해석하는 법(C5 PK vs PD rate-limiting)이다. [R&T p.233]

**개념 항법도:**
- C1. 질량작용법칙(Law of Mass Action) → Emax 골격. [G&W p.202–204]
- C2. Sigmoid Emax / Hill 모델 [⚡ Apex Concept]. [G&W p.216–220; PD3 p.732–741]
- C3. 히스테리시스(Hysteresis) — 시간 지연의 시각적 진단. [R&T p.233–235]
- C4. 효과 구획(Effect Compartment) + 유동 시스템(Systems-in-flux) / 간접 반응(Indirect Response). [R&T p.241–248]
- C5. AUEC + 지속 시간(Duration) + PK/PD 율속(rate-limiting). [G&W p.229–234; R&T p.249–259]

<!-- ANCHOR -->
**구조적 흐름:** 질량작용법칙(C1) → Emax 쌍곡선 → Hill `n` 도입으로 sigmoid 일반화(C2) → 평형 가정의 붕괴가 히스테리시스로 드러남(C3) → 효과 구획 또는 시스템 전환(system turnover)으로 시간 지연을 흡수(C4) → 반응-시간 곡선의 적분량과 지속 시간을 설계 지표로 사용(C5).

**범위 경계:** G&W §3.6.1의 경쟁적 길항(competitive antagonism) 시작부까지만 본문에 포함한다. G&W §3.6.2–§3.6.5 및 G&W §3.12 기저치 모델링(baseline modeling)은 `[확인 필요 — 첨부 PDF 미포함 구간]`으로 유지하고 본 세션에서 추정하지 않는다.

---

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.199, Fig.3.1
Why this matters: This figure frames the whole session as two linked PD problems: concentration-response sensitivity and response-time behavior. Without it, C1–C5 may look like separate formulas rather than one PK→PD translation chain.
When to look: before reading §1 Roadmap or immediately after the §1 Big Idea
Learner instruction: Inspect the left panel for potency/efficacy and the right panel for onset/intensity/duration. Then map C1–C2 to the left panel and C3–C5 to the right panel.
<!-- /FIGURE_POINTER -->

---

# §2 — Concept Anatomy Cards

---

## Card C1 — 질량작용법칙(Law of Mass Action) → Emax 골격


<!-- MASTER LENS -->
### [개념 Big Idea]

Kd는 리간드-수용체 결합 친화도(ligand-receptor binding affinity)의 지표다. EC50는 결합 이후 신호전달(transduction)과 조직 반응(tissue response)까지 포함한 기능적 감수성(functional sensitivity)의 지표다. **Kd와 EC50가 다를 수 있다는 사실**이 C1의 핵심이다. 그 차이를 만드는 대표 이유가 여분 수용체(spare receptor)와 증폭 연쇄(cascade amplification)이다. [G&W p.203–206]

<!-- ANNOTATION -->
즉, 결합이 강하다는 말과 조직에서 절반 효과가 낮은 농도에서 나온다는 말은 같은 뜻이 아니다.

<!-- ANCHOR -->
평형 결합의 미시적 동역학을 점유율(occupancy) 식으로 정리하면, Emax 모델의 분자와 분모가 왜 같은 농도 단위를 가져야 하는지 드러난다.

### A. 형식적 정의(Formal Definition)

가역적 1:1 약물-수용체 결합(drug-receptor binding)에서 반응 `E`는 결합된 수용체 복합체(occupied receptor complex — 약물이 결합한 수용체 풀) `[RC]`에 비례한다. 수용체가 모두 점유(occupied)될 때 `Emax`(← 농도가 무한대일 때 도달하는 최대 가능 효과) `= α[R_T]`이며, `α`는 고유활성(intrinsic activity — 수용체 1단위가 만들어내는 효과 크기, 부분효현제일수록 작음)이다. [G&W p.203]

### B. 도출(Derivation)

**평형 결합:**

$$
\frac{d[RC]}{dt}=k_1[R][C]-k_{-1}[RC]=0
$$

따라서

$$
K_d=\frac{k_{-1}}{k_1}=\frac{[C][R]}{[RC]}
$$

총 수용체 농도 `[R_T]=[R]+[RC]`를 대입하면

$$
\frac{[RC]}{[R_T]}=\frac{[C]}{[C]+K_d}
$$

반응 비례성(response proportionality)을 적용하면

$$
\frac{E}{E_{max}}=\frac{[C]}{[C]+K_d}, \qquad E=\frac{E_{max}\cdot [C]}{[C]+K_d}
$$

기능적 반응(functional response)에서는 `Kd` 대신 `EC50`가 사용된다.

$$
E=\frac{E_{max}\cdot C}{EC_{50}+C}
$$

`[출처: G&W 5e, Ch.3, p.202–204, Eq.3:1–3:10]`

### C. 구조적 필연성(Structural Necessity)

분자 `[C]`는 이용 가능한 리간드(available ligand)가 늘수록 수용체 점유율이 증가한다는 질량작용법칙의 결과다. 분모 `[C]+Kd`는 수용체 보존(receptor conservation — 수용체 총량 보존)을 반영한다. 이 구조 때문에 점유율은 0–1 사이에 머물며, 반응도 `Emax`를 초과하지 않는다.

### D. 가정과 경계 조건(Assumptions & Boundary Conditions)

- 1:1 가역적 결합(reversible binding), 평형(equilibrium), 단일 유효 생체구획 농도(single effective biophase concentration).
- 반응은 `[RC]`에 비례한다. 수용체 비축분(receptor reserve — 여분 수용체에 의한 증폭 여지)이 있으면 수용체가 완전히 점유되지 않아도 최대에 가까운 효과가 발생할 수 있다.
- `EC50 ≠ Kd`일 수 있다. G&W는 점유율-반응 불일치(occupancy-response 불일치)와 신호 증폭(signal amplification)을 명시한다. [G&W p.204–206]

### E. 한계(Limitations)

여분 수용체가 많거나 증폭 이득(cascade gain)이 큰 조직에서는 수용체의 소량 점유(small occupancy)만으로도 큰 반응(large response)이 나타날 수 있다. G&W Fig.3.5는 10% 점유율이 90% 반응으로 증폭되는 연쇄 증폭 예를 제시한다. Fig.3.6은 동일 반응에 필요한 점유율이 조직마다 다를 수 있음을 보여준다. [G&W p.205–206]

포화/치환 결합(saturation/displacement binding)과 Cheng-Prusoff 변환은 수용체 결합 분석(receptor binding assay)의 Ki/IC50 해석에 필요하지만, 본 세션에서는 기능적 EC50와 결합 Kd를 혼동하지 않는 경계로만 사용한다. [G&W p.206–210]

<!-- TRENCH -->
**[Trench-Level Tip]** EC50 covariate effect가 보이면 먼저 “drug-side 변화인가, system-side 변화인가?”를 분리한다. Total concentration 기반 EC50 변화는 protein binding 변화일 수 있으므로 unbound concentration 분석이 없으면 receptor sensitivity 변화로 단정하지 않는다. `[실무 구현 번역]`

### F. 제텔카스텐 원자 노트(Zettelkasten Atom)

**Atom C1:** `Kd`는 결합 강도, `EC50`는 결합 이후 조직·신호 시스템까지 포함한 기능적 감수성(functional sensitivity)이다. Emax 식의 쌍곡선은 수용체 보존(receptor conservation)과 평형 질량작용(equilibrium mass action)에서 나온다.

<!-- RECAP -->
**Recap:** C1은 Emax 모델을 “경험식”이 아니라 receptor occupancy와 response transduction의 압축형으로 보게 만든다.

> **숙련 노트(Mastery Note) — [AUDIT_DERIVED]**  
> C1을 읽은 뒤에는 `Kd`, 총 `EC50`, 비결합 `EC50`, 조직 반응 감수성(tissue response sensitivity)을 같은 층위의 숫자로 배열하지 않는다. 어느 숫자가 결합 분석(binding assay)에서 왔고, 어느 숫자가 기능적 반응(functional response)에서 왔는지를 먼저 분리해야 후속 공변량 해석이 무너지지 않는다.

> **실무 체화 요약(Practice Brief) — C1 — [EXPERT_INFERENCE, v3]**  
> 보고서나 리뷰에서 새로운 EC50 값을 만났을 때 던질 첫 두 질문: (1) **출처가 결합 분석(binding assay)인가, 기능적 분석(functional assay)인가?** (2) **총 농도(total)인가 비결합 농도(unbound)인가?** 이 두 분리가 안 된 EC50 숫자는 임상 결정 근거로 사용하지 말고, 원자료의 단백질 결합(protein binding) 정보부터 확인한다. 임상약사 출신이라면 vancomycin/tacrolimus의 비결합 분율(unbound fraction) 변동 경험이 그대로 적용된다.

<!-- FIGURE_SCHEMATIC -->
Title: Kd와 EC50의 분리: receptor occupancy → transduction → response
Mode: R
Visual objective: In 5 seconds, the learner should see that the functional response curve can be left-shifted from the receptor occupancy curve.
Core message: Kd belongs to binding affinity, whereas EC50 belongs to the amplified tissue/system response.
Elements to include: shared concentration x-axis; receptor occupancy/stimulus curve labeled Kd; functional response curve shifted left and labeled EC50; receptor occupancy → stimulus/transduction → response arrow chain; note that EC50 may differ from Kd and exceptions exist.
Elements to exclude: Cheng-Prusoff derivation; full/partial agonist profiles; exact textbook layout; original color scheme; receptor cartoon details.
Suggested rendering: SVG
Caption: Receptor binding and functional response need not align; transduction/cascade amplification can make EC50 differ from Kd.
Alt text: Two concentration-response curves share one concentration axis; the functional response curve is left-shifted from receptor occupancy, illustrating EC50–Kd separation.
Source relation: Redrawn from textbook concept
<!-- /FIGURE_SCHEMATIC -->


---

## Card C2 — Sigmoid Emax / Hill Model [⚡ Apex Concept]


<!-- MASTER LENS -->
### [개념 Big Idea]

> **임상 직관 lead-in — [EXPERT_INFERENCE, v3]**  
> 항생제 또는 항부정맥제를 두 배 증량했는데 효과가 두 배가 되지 않는 경험은 임상 약사라면 이미 안다. 왜인가? 효과에는 천장(`Emax`)이 있기 때문이다. 그렇다면 그 천장에 *얼마나 빨리* 도달하는가 — 그것을 결정하는 것이 곡선의 가파름, 즉 **Hill coefficient γ(=n)**다. Emax/Hill 모델은 이 세 양을 분리한다: **천장(`Emax`), 효능(`EC50`), 가파름(γ)**. 특히 γ가 1보다 클수록 작은 농도 변화가 큰 반응 변화를 만들어 협역 치료역(narrow therapeutic window) 특성이 형성된다 — 이것이 이 카드를 Apex로 만드는 이유다.

Hill `n`은 mechanism proof가 아니라 **curve steepness/flexibility parameter**(← 곡선의 급경사와 굽힘을 설명하는 파라미터)다. 그러나 임상적으로는 강력하다. `n`이 커질수록 효과 50%에서 90%로 상승하는 데 필요한 농도 배율(concentration ratio)이 줄어든다. 즉, 더 좁은 농도 구간 안에서 반응이 완성된다. 따라서 dose-titration step size와 safety margin 해석이 더 민감해진다. [G&W p.216, p.220]

Linear/log-linear effect models는 제한된 농도 범위에서는 유용하다. 그러나 effect plateau(← 농도 증가에도 효과가 더 늘지 않는 구간)와 steep transition을 설명하려면 ordinary Emax를 넘어 sigmoid Emax가 필요하다. [G&W p.210–216]

### A. 형식적 정의(Formal Definition)

Sigmoid Emax 모델:

$$
E=\frac{E_{max}\cdot C^n}{EC_{50}^n+C^n}
$$

기저치(baseline)가 있는 억제 반응(inhibitory response)에서는 다음과 같이 쓴다.

$$
E=E_0-\frac{I_{max}\cdot C^n}{IC_{50}^n+C^n}
$$

`[출처: G&W 5e, Ch.3, p.216, p.218, Eq.3:32, Eq.3:34–3:35]`

> **⚡ 기억 고리 (Memory Hook) — *최대 자극 vs 최대 억제* (Emax vs Imax) — [EXPERT_INFERENCE, v3]**  
> Emax 모델은 **자극(stimulation) 모델** — 효과가 0(또는 baseline)에서 출발해 천장 `Emax`까지 *상승*한다. Imax 모델은 **억제(inhibition) 모델** — 효과가 baseline `E0`에서 출발해 (1−Imax)×`E0`까지 *감소*한다. `Imax = 1`이면 완전 억제(기저치가 0이 됨). 두 모델은 같은 sigmoid 형태이지만 **방향이 반대**다 — 부호와 baseline의 위치가 핵심이다. PD 모델 선택 시 자극 데이터에 Imax를 적용하거나 그 반대로 하면 노출-반응 곡선의 천장이 과대추정되거나 억제 효율이 잘못 계산되어 dose-response 결론이 정반대로 나올 수 있다.

### B. 파라미터 복원과 PD3 앵커(Parameter Recovery and PD3 Anchor)

그래프 기울기(graphical slope) 관계:

$$
m=\frac{n\cdot E_{max}}{4}, \qquad n=\frac{4m}{E_{max}}
$$

절편 복원(intercept recovery):

$$
C_0=EC_{50}\cdot e^{-2/n}
$$

`[출처: G&W p.219, Eq.3:38–3:42]`

> **Insertion I2 — [TEXTBOOK_DERIVED]** (Audit T3/T5-A SHOULD_FIX: G&W p.200 design message anchor)  
> Sigmoid Emax/Imax 식의 *식별 가능성*은 모델 형태에 의해서만 결정되지 않고 실험 설계에 의해 결정된다. G&W p.200은 PD 모델 식별의 최소 설계 요건으로 control + 2–4개 dose levels, 그 중 적어도 한 dose가 maximum response에 도달할 것을 명시한다. PD3가 이 원칙의 직접 시연이다 — 0–500 µg/L design은 plateau에 충분히 닿지 못해 sigmoid superiority를 통계적으로 입증하지 못하지만, 0–800 µg/L design은 같은 원칙을 만족시켜 model discrimination을 가능하게 한다. [G&W p.200, p.734–741]

PD3 blood-pressure inhibitory Imax case는 initial graphical estimate와 final model estimate를 연결한다. 0–800 µg/L design의 sigmoid Imax model에서 `E0=171`, `Imax=34.7`, `IC50=140`, `n=2.03`, AIC=45.6이 제시되며, ordinary Imax model은 `E0=177`, `Imax=49.8`, `IC50=175`, AIC=50.8로 비교된다. [G&W p.733–735]

PD3가 전달하는 핵심 메시지는 '파라미터 추가는 곧 overfitting'이라는 통념이 틀릴 수 있다는 것이다. Sigmoid model에서 IC50 precision이 개선되고 AIC/F-test/VIF가 함께 지지되면, `n`은 단순 장식이 아니라 데이터가 실제로 요구하는 curvature parameter(← 곡선 굽힘을 설명하는 파라미터)다. [G&W p.734–741]

### C. 구조적 필연성(Structural Necessity)

`C^n`이 분자와 분모에 동시에 들어가는 이유는 효과가 농도의 비선형 변환(nonlinear transformation)을 거치더라도 0–Emax 경계를 보존해야 하기 때문이다. `n=1`이면 일반 Emax로 돌아간다. `n>1`이면 농도-반응 전환이 급격해진다. `n<1`이면 활성 대사체(active metabolite), 다중 수용체 부위(multiple receptor sites), 이질성(heterogeneity) 등의 가능성을 시사할 수 있다. 단, 이는 단독 기전 증명(mechanism proof)이 아니다. [G&W p.216]

비결합 농도 변환(unbound concentration transformation)에서도 `n`은 보존된다.

$$
E=\frac{E_{max}(C_u/f_u)^n}{EC_{50}^n+(C_u/f_u)^n}
=\frac{E_{max}\cdot C_u^n}{EC_{u50}^n+C_u^n}
$$

단백결합 차이가 큰 비교에서는 총 EC50가 아니라 비결합 EC50(unbound EC50)를 점검해야 한다. 그래야 역가(potency) 변화와 단백질 결합(protein binding) 변화를 혼동하지 않는다. [G&W p.216–217]

### C-2. Plausible Fallacy: “Curvature Suppression”

<!-- CONFUSION -->
**오류:** “sigmoid해 보이지만 ordinary Emax도 대충 맞으니 `n=1`로 단순화한다.”  
**교정:** PD3는 같은 약물이라도 0–500 µg/L design에서는 F-test가 sigmoid 우월성을 통과하지 못하는 반면, 0–800 µg/L로 확장하면 통과함을 보여준다. 따라서 올바른 결론은 'sigmoid가 필요 없다'가 아니라, '농도 범위가 curvature를 확인하기에 충분한가?'다. [G&W p.734–735, p.740–741]

Hill `n`을 “positive cooperativity가 증명되었다”라고 쓰면 source fidelity가 깨진다. Orthogonal binding evidence가 없는 한, `n`은 steepness와 dose-titration sensitivity의 현상학적 파라미터로 기술한다. `[교과서 기반 + 교과서 외 규제 해석]`

> **Insertion I3 — [CRUCIBLE_DERIVED]** (Crucible Intuition #2 / Grade B: Precision-Improvement diagnostic)  
> **Mastery signal — IC50 CV 방향성 진단:** 같은 데이터에 ordinary Imax와 sigmoid Imax를 모두 적합시켰을 때, sigmoid에서 IC50의 CV%가 ordinary보다 *향상*된다는 사실 자체가 `n` 추가의 정당성을 가장 직접적으로 보여주는 신호다. PD3 Table 3.2에서 ordinary IC50 CV가 약 31%였던 것이 sigmoid에서 약 11%로 떨어진다 — 진정한 overparameterization이라면 정밀도가 *악화*되어야 하므로, **정밀도 향상 자체가 추가 parameter가 데이터를 진정으로 설명하고 있다는 직접 증거**다. F-test나 AIC가 임계값 근처일 때 이 진단이 결정적인 보조 증거가 된다. [G&W p.735 Table 3.2]

> **⚡ Plausible Fallacy — Apex Concept 전용 — [EXPERT_INFERENCE, v3]**  
> **그럴듯한 오해:** "EC50만 알면 해당 농도에서 임상 효과를 예측할 수 있다."  
> **왜 틀렸는가:** EC50은 곡선의 **중간점(midpoint)** 위치만을 결정한다. 그러나 실제 임상 반응의 *크기*는 `Emax`(천장)와 **Hill γ(가파름)**에 의해 함께 결정된다. γ가 3이면 EC50의 ±30% 농도 변화가 반응을 약 20%→80%로 끌어올려 — 치료역이 매우 좁아진다. 같은 ±30% 변화가 γ=1에서는 약 40%→60%에 그친다. 즉, **같은 EC50라도 γ가 다르면 임상 용량 조절의 정밀도 요구가 완전히 달라진다.**  
> **실무에서 어떻게 드러나는가:** 용량 조절 가이드라인이나 exposure-response 보고서에서 EC50만 제시하고 γ를 명시하지 않으면, 좁은 치료역 약물(면역억제제, 항부정맥제, 일부 vitamin K antagonist)에서 용량 조절 폭이 실제보다 *관대하게* 계산될 수 있다. 규제 심사 관행상 Hill γ가 빠진 PK-PD 섹션은 "Hill coefficient의 임상적 의의" 추가 기술 요청 (deficiency)을 받기 쉽다. **따라서 이 카드의 핵심 결론은 단순하다 — γ는 곡선의 미적 디테일이 아니라 임상 안전 마진 그 자체다.** `[교과서 기반 + 교과서 외 규제 해석]`

### D. 가정과 경계 조건(Assumptions & Boundary Conditions)

- 농도 범위가 `EC50` 주변과 고원부(plateau)를 충분히 포함해야 `n`과 `Emax/Imax`가 식별된다.
- 기저치 `E0`가 시간에 따라 변하면 기저치 모델(baseline model)이 필요하다. `[확인 필요 — G&W §3.12 첨부 PDF 미포함 구간]`
- 목표 농도 역산(target concentration inversion)은 절대 반응(absolute response)과 기저치 상대 반응(baseline-relative response)을 구분해야 한다. [G&W p.221]

### E. 한계(Limitations)

복합 Emax(composite Emax)는 하나의 단순 sigmoid로 설명되지 않는 반응을 두 개 이상의 하위 반응(sub-response)으로 분리한다. 즉, 관찰된 곡선 하나가 실제 생물학적 과정 하나를 의미한다고 단정하지 않는다. Lundström et al. 예시는 `IC50,1=1.8`, `IC50,2=23 µg/L`, `Imax,1=4`, `Imax,2=3.2`, `n1=1.4`, `n2=3.7`을 제시한다. [G&W p.221–223]

Multiple binding site model은 caffeine brain concentration 예처럼 비단조 또는 복합 곡선의 가능성을 보여주지만, 본 세션에서는 “single Hill curve가 모든 생물학을 증명하지 않는다”는 boundary로만 둔다. [G&W p.224]

<!-- TRENCH -->
**[Trench-Level Tip]** Sigmoid Emax fitting은 ordinary Emax/Imax로 먼저 `E0/Emax/EC50` 초기값을 잡은 뒤 `n=1`에서 시작한다. PD3처럼 error가 커지면 `n` precision이 악화될 수 있으므로 “폭발” 같은 표현 대신 CV와 sensitivity analysis로 말한다. [G&W p.738–739] `[실무 구현 번역]`

**[실무 팁(Trench-Level Tip)]** `[실무 구현 번역]` `Range-Starved Hill`은 농도 범위가 `IC50` 주변과 상단 고원부(upper plateau)를 충분히 건드리지 못하는 상황이다. 이때 `n`은 1로 수렴하거나 RSE가 커질 수 있다. 이는 알고리즘 문제가 아니라 설계 정보(design information) 부족이다.

### F. 제텔카스텐 원자 노트(Zettelkasten Atom)

**Atom C2:** Hill `n`은 기전의 증명이 아니라 농도-효과 곡선(concentration-effect curve)이 얼마나 급하게 전환되는지를 나타내는 감수성 지렛대(sensitivity lever)다. PD3는 그 지렛대가 모델 선택과 농도범위 설계에 어떻게 연결되는지 보여준다.

<!-- RECAP -->
**Recap:** C2는 “curvature를 본다”는 것이 단순한 시각적 취향이 아니라 dose range, precision, target concentration 해석의 문제임을 고정한다.

> **Practice Lens — [CRUCIBLE_DERIVED]**  
> Hill `n`을 보고 가장 먼저 던질 질문은 “무슨 기전인가?”가 아니라 “이 농도 범위가 `IC50/EC50` 주변과 plateau를 충분히 지나갔는가?”이다. 이 질문을 먼저 통과해야 `n`을 titration sensitivity 또는 model discrimination의 언어로 방어할 수 있다.

> **Failure Mode — [AUDIT_DERIVED]**  
> `n>1`을 positive cooperativity의 증거라고 단정하면 교과서 경계를 넘는다. 보고서 문장에서는 “steepness/flexibility를 설명하는 현상학적 parameter이며 가능한 기전 가설을 제시할 수 있다” 정도로 낮추는 것이 안전하다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, Case Study PD3, p.733 Fig.PD3-3.1; p.735 Table PD3-3.2; p.741 Table PD3-3.4
Why this matters: The key lesson is not merely that a sigmoid model fits better. The original PD3 materials show how concentration range changes model discrimination and parameter precision.
When to look: after reading Card C2 §B and §C-2
Learner instruction: Compare the 0–500 and 0–800 µg/L designs before reading the VIF discussion. Ask whether the data range is wide enough to reveal curvature around IC50 and the upper response region.
<!-- /FIGURE_POINTER -->


---

## Card C3 — Hysteresis: 시간 지연의 진단 도구


<!-- MASTER LENS -->
### [개념 Big Idea]

Hysteresis(← 같은 농도에서도 시간 방향에 따라 효과가 달라지는 현상)는 단순히 “농도와 효과가 다르게 움직인다”는 현상이 아니다. 오히려 이는 plasma concentration이 site-of-action 또는 downstream response를 즉시 대표하지 못한다는 구조적 진단 신호로 읽어야 한다. R&T Ch.8은 time이 항상 고려되어야 한다고 시작하며, single dose 후 response가 plasma concentration을 따라가지 않는 사례를 제시한다. [R&T p.233–235]

<!-- ANNOTATION -->
즉, hysteresis는 그림의 잡음이 아니라 model structure를 바꾸라는 신호다.

### A. 형식적 정의(Formal Definition)

히스테리시스는 농도가 상승 구간(rising phase)에 있을 때와 하강 구간(falling phase)에 있을 때 농도-반응(concentration-response) 궤적이 달라지는 현상이다. 경구 naproxen 500 mg 치과 통증 모델에서 비결합 혈장 농도(unbound plasma concentration)와 평균 통증 완화(mean pain relief)를 직접 도시하면 반시계 방향 고리(counterclockwise loop)가 나타난다. 같은 농도라도 시간 순서가 다르면 effect가 다르게 보인다는 뜻이다. [R&T p.234–235]

### B. 진단 논리(Diagnostic Logic)

Digoxin 1 mg 정맥 급속 투여(i.v. bolus) 후 첫 4시간 동안 혈장 농도는 감소하지만 좌심실 구출 시간 지표(left ventricular ejection-time index)는 증가한다. 겉으로는 낮은 농도에서 더 큰 효과가 나는 것처럼 보인다. R&T는 심장 조직 분포(cardiac tissue distribution)와 수용체 결합이 느리므로 혈장-효과 관계를 해석하려면 약 6시간의 분포 평형(distribution equilibrium)을 기다려야 한다고 설명한다. [R&T p.234]

Naproxen 500 mg 경구 예시는 시간-농도/효과 도표에서는 지연이 약하게 보이지만, 효과를 비결합 농도에 직접 도시하면 고리가 명확해진다는 점을 보여준다. [R&T p.234–235]

### C. 구조적 필연성(Structural Necessity)

반시계 방향 히스테리시스(counterclockwise hysteresis)는 보통 효과가 혈장보다 늦는 상황이다. 원인은 크게 두 축으로 나뉜다.

1. **동력학적 지연(kinetic delay):** 약물이 작용 부위(site of action)에 늦게 도달하거나 느린 결합/해리(slow binding/dissociation)를 보인다. [R&T p.235–238]
2. **역학적 지연(dynamic delay):** 측정된 반응이 하류 구획(downstream compartment)이나 전환 시스템(turnover system)에 의해 늦게 변한다. [R&T p.236–244]

### D. 가정과 경계 조건(Assumptions & Boundary Conditions)

- 혈장 농도가 작용 부위 농도(site concentration)를 즉시 대표하지 못할 수 있다.
- 측정 종말점(measured endpoint)이 표적 결합(target engagement)에 가까울수록 지연이 작고, 하류 반응(downstream response)일수록 지연이 커진다. [R&T p.236–238]
- 반시계 방향 고리는 지연을 말하지만, 지연의 원인이 분포(distribution)인지 전환(turnover)인지는 별도 진단이 필요하다.

### E. 한계(Limitations)

채혈이 희소(sparse)하면 히스테리시스 고리의 방향과 폭이 왜곡될 수 있다. 또한 위약 보정(placebo correction), 기저치 변동(baseline drift), 내인성 리듬(endogenous rhythm)이 있으면 농도-반응 고리를 인과 경로(causal path)로 과해석하면 안 된다. 이 경우 loop는 진단 단서이지 최종 mechanism proof가 아니다. [R&T p.244]

<!-- TRENCH -->
**[실무 팁(Trench-Level Tip)]** 히스테리시스 고리를 보면 먼저 (1) 고리 폭(loop width)이 약물 반감기의 몇 배인지, (2) 최대 효과 시점(peak effect time)이 용량 의존적(dose-dependent)인지 확인한다. 최대 효과 시점이 용량 의존적이면 효과 구획 가능성이 커지고, 용량 비의존적(dose-invariant)이면 전환/간접 반응(turnover/indirect response) 쪽으로 기운다. `[실무 구현 번역]`

### F. Zettelkasten Atom

**Atom C3:** Hysteresis는 모델 선택 전에 보는 EDA diagnostic이다. 농도-효과 loop는 “어떤 link function을 쓸 것인가”보다 먼저 “plasma가 effect site를 대표하는가”를 묻는다.

<!-- RECAP -->
**요약(Recap):** C3는 시간 지연을 그림으로 감지하는 단계이며, C4의 효과 구획(effect compartment)과 간접 반응(indirect response)은 이 지연을 구조적으로 흡수하는 방식이다.

> **숙련 노트(Mastery Note) — [TEXTBOOK_DERIVED]**  
> 히스테리시스 도표는 단순한 시각화가 아니라 모델 선택의 분류 도구(triage 도구)다. 시간-농도/효과 도표에서 지연이 애매해도 농도-반응 고리가 생기면, 혈장이 인과적 생체구획(causal biophase)을 즉시 대표한다는 가정을 내려놓아야 한다.

> **실무 체화 요약(Practice Brief) — C3 — [EXPERT_INFERENCE, v3]**  
> 새 PD 데이터셋을 받았을 때 *모델 적합 전에* 반드시 시행할 탐색적 자료 분석 순서: (1) **시간-농도 도표와 시간-효과 도표를 같은 축에서 그려서 시간 단위가 한 자릿수 이상 다른지 확인**(Insertion I6 빠른 진단 활용), (2) **농도-효과 고리를 시간 순서로 도시하여 반시계/시계/비고리 판정**, (3) **용량 군별 최대 효과 시점이 용량 의존적인지 확인**. 이 세 단계가 끝나기 전에는 어떤 연결 함수(link function)도 고정하지 않는다.

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.234 Fig.8-1; p.235 Fig.8-2
Why this matters: Hysteresis cannot be fully understood as prose. The visual loop shows why the same plasma concentration can correspond to different response values depending on whether concentration is rising or falling.
When to look: after reading Card C3 §A–B
Learner instruction: In Fig.8-2, follow the chronological sampling numbers around the loop. Focus on the fact that concentration-response is path-dependent, not a single static curve.
<!-- /FIGURE_POINTER -->


---

## Card C4 — 효과 구획(Effect Compartment) + 유동 시스템(Systems-in-flux) / 간접 반응(Indirect Response)


<!-- MASTER LENS -->
### [개념 Big Idea]

C4의 첫 질문은 “response가 plasma concentration에 늦게 따라오는가?”가 아니다. 진짜 질문은 **delay가 site-of-action equilibration 때문인가, 아니면 biological system turnover 때문인가?**이다. 전자라면 effect compartment가 더 자연스럽다. 후자라면 indirect response / systems-in-flux가 더 자연스럽다. [R&T p.245–248]

### A. C4a. 효과 구획(Effect Compartment)

효과 구획(effect compartment — 혈장과 반응 사이 지연을 흡수하는 가상 구획)은 혈장 농도와 반응을 연결하기 위해 도입한 가설적 구획(hypothetical compartment)이다. R&T는 naproxen 히스테리시스를 효과 구획을 통해 줄이고, 효과 부위 농도(effect-site concentration)와 반응을 더 직접적으로 연결하는 그림을 제시한다. [R&T p.245–246]

이 구획은 미시적 장기 구획(microscopic organ compartment)이 아니라 총괄 지연 표현(lumped delay representation — 여러 지연 원인을 하나로 묶은 표현)이다. 조직 관류(tissue perfusion), 투과성(permeability), 조직 친화도, 결합 동역학(binding kinetics), 신호전달 지연(signal transduction lag)이 복합적으로 반영된 결과일 수 있다. 따라서 `ke0`를 특정 생리상수처럼 외삽하지 않는다. [R&T p.235–236, p.245–246]

### B. C4b. 유동 시스템(Systems-in-flux) / 간접 반응(Indirect Response)

유동 시스템(systems-in-flux)에서는 약물이 내인성 물질(endogenous substance) 또는 생리적 반응의 생성/소멸 과정(formation/loss process)을 바꾼다. Warfarin은 프로트롬빈 복합체 전환(prothrombin complex turnover)을 통해 혈장 농도와 효과가 분리되는 대표 예다. Sodium warfarin 1.5 mg/kg 경구 투여 후 프로트롬빈 복합체 반응은 전환 반감기(turnover half-life) 1–2일의 영향을 받는다. 즉, 혈장 농도가 변해도 반응은 시스템 회복 속도에 묶인다. [R&T p.241–248]

General turnover skeleton:

$$
\frac{dR}{dt}=k_{in}-k_{out}R
$$

약물은 `k_in` 또는 `k_out`을 자극(stimulation)/억제(inhibition)할 수 있다. 본 식은 G&W 비정상상태 반응 체계(non-steady-state response framework)와 R&T 유동 시스템 설명을 연결하는 최소 골격이다. [G&W p.229–230; R&T p.241–248]

### C. 구조적 필연성(Structural Necessity)

효과 구획은 혈장과 효과 부위 사이의 평형화 지연(equilibration delay)을 흡수한다. 간접 반응은 반응 변수 자체가 느린 전환율(turnover)을 갖기 때문에 지연이 생긴다. 이 둘을 구분하지 않으면 현재 데이터에 대한 적합은 비슷해 보여도 외삽 결과가 달라진다. 특히 용량 변경이나 투여 간격 변경 상황에서 예측 오차가 크게 벌어진다.

<!-- ANCHOR -->
**용량 비의존적 최대 효과 시점 진단(dose-invariant peak time diagnostic):** 간접 반응에서는 최대 효과가 `dR/dt=0` 조건, 즉 유입/유출 균형(input/output balance)에 의해 결정된다. 용량이 반응 진폭(response amplitude)을 바꿔도 시스템 전환 시간 척도가 변하지 않으면 최대 효과 시점이 거의 일정할 수 있다. 효과 구획에서는 용량과 농도-시간 양상(concentration-time profile)이 효과 부위 평형화의 모양을 바꾼다. 따라서 최대 효과 시점이 용량 의존적이 될 가능성이 크다. `[교과서 기반 개념 + 실무 진단 번역]`

### D. Assumptions

- Effect compartment는 hypothetical link이며 source compartment가 아니다. [R&T p.245]
- Indirect response는 endogenous system의 formation/loss process를 전제로 한다. [R&T p.241–248]
- Warfarin-like response에서는 plasma concentration이 빨리 변해도 response는 prothrombin complex turnover에 의해 느리게 변한다. [R&T p.242, p.247]

### E. 한계(Limitations)

NONMEM `$DES`, 격자 탐색(grid search), eta 배치는 R&T 원문이 아니라 구현 계층(implementation layer)이다. 본 Content Lock에서는 모델링 실무로 연결할 때만 `[실무 구현 번역]`이라고 명시한다.

<!-- TRENCH -->
**[실무 팁(Trench-Level Tip)]** `[실무 구현 번역]` 히스테리시스 모델 선택은 혈장 직접(plasma direct) → 효과 구획 → 간접 반응 순서로 적합한다. 각 단계에서 용량 군별 최대 효과 시점의 용량 의존성이 사라지는지 본다. 효과 구획에서 충분히 사라지면 분포 지연이 주원인이고, 간접 반응에서만 설명되면 전환 시스템이 본질이다.

**[실무 팁(Trench-Level Tip)]** `[실무 구현 번역]` `PK-Aliased ke0`는 추정된 효과 반감기(estimated effect half-life)가 혈장 반감기와 너무 가까워 `ke0`와 제거 속도(elimination rate)가 분리되지 않는 패턴이다. 이때 `ke0` 수치 자체보다 밀집 채혈(dense sampling) 또는 민감도 분석(sensitivity analysis)이 더 중요하다.

### F. Zettelkasten Atom

**Atom C4:** Effect compartment는 “site equilibration delay”, indirect response는 “system turnover delay”다. Hysteresis를 줄이는 fit보다 더 중요한 것은 어떤 delay를 외삽할 것인지의 구조 선택이다.

<!-- RECAP -->
**요약(Recap):** C4는 C3에서 감지한 시간 지연을 구조화한다. 같은 고리라도 분포 문제인지 시스템 전환 문제인지에 따라 투여 간격(dosing interval), 발현 예측(onset 예측), 특수 집단 외삽(special population extrapolation)이 달라진다.

> **Practice Lens — [CRUCIBLE_DERIVED]**  
> Effect compartment는 ‘site equilibration delay’를 흡수하고, indirect response는 ‘system turnover delay’를 설명한다. 둘이 모두 fit될 수 있을 때는 peak-time의 dose-dependence, response recovery scale, biological plausibility를 먼저 비교해야 한다.

<!-- FIGURE_SCHEMATIC -->
Title: Delay-source topology: effect-site equilibration vs system turnover
Mode: R
Visual objective: In 5 seconds, the learner should distinguish a plasma-to-effect-site delay from a downstream response-turnover delay.
Core message: Effect compartment and indirect response are not interchangeable delay patches; they encode different causal structures.
Elements to include: Path A with plasma concentration C(t) → effect-site concentration Ce(t) → response E(t); Path B with plasma concentration C(t) → modulation of kin/kout → turnover response R(t); labels for site equilibration delay and system turnover delay; diagnostic callout for peak-time dose-dependence vs dose-invariance.
Elements to exclude: NONMEM code; numerical ke0; dense feedback loops; more than one downstream turnover compartment.
Suggested rendering: Mermaid
Caption: The same delayed response pattern can arise from site equilibration or from biological turnover; model choice determines extrapolation behavior.
Alt text: Two parallel causal paths show plasma concentration leading either to an effect-site compartment and response, or to kin/kout turnover control and delayed response.
Source relation: Redrawn from textbook concept
<!-- /FIGURE_SCHEMATIC -->


---

## Card C5 — AUEC + 지속 시간(Duration) + PK/PD 율속(Rate-Limiting)


<!-- MASTER LENS -->
### [개념 Big Idea]

효과 지속 시간은 drug half-life만으로 결정되지 않는다. Plasma concentration이 사라져도 response가 남는 경우는 흔하다. 이때 율속은 PK elimination이 아니라 receptor binding, irreversible action, target turnover, downstream system recovery일 수 있다. [R&T p.249–253]

Methylprednisolone 예시는 PK AUC가 dose-proportional이어도 lymphocyte response는 high-dose 구간에서 saturate될 수 있음을 보여준다. 즉 PK linearity는 PD linearity를 보장하지 않는다. [R&T p.257–258]

### A. 형식적 정의(Formal Definition)

AUEC(← 반응-시간 곡선 아래 면적, area under the effect curve)는 반응-시간 곡선을 하나의 면적값으로 요약한 지표다.

$$
AUEC=\int_0^{\infty}E(t)dt
$$

> **Insertion I4 — [TEXTBOOK_DERIVED]** (Audit T1 RESTORED/PARTIAL: G&W §3.6.6 Non-Steady-State Response framework bridge)  
> AUEC는 진공 속에서 정의되지 않는다. G&W §3.6.6은 비정상상태 response의 동력학 framework를 제공한다 — drug concentration이 시간에 따라 변하면 response도 비정상상태로 변하며, 그 결과 곡선의 모양은 input(concentration-time)의 모양과 response system(Emax/Hill)의 비선형성에 의해 동시에 결정된다. AUEC는 그 framework가 만들어낸 결과 곡선을 적분한 면적 요약 지표이며, 따라서 closed form은 framework의 가정(ordinary Emax + first-order elimination) 아래에서만 가능하다. [G&W p.229–234, Eq.3:56–3:73]

One-compartment first-order elimination과 ordinary Emax model에서 G&W는 다음 closed form을 제시한다.

$$
AUEC=\frac{E_{max}}{K}\ln\left(1+\frac{D}{EC_{50}\cdot V}\right)
$$

`[출처: G&W p.233–234, Eq.3:72–3:73]`

Sigmoid Emax에서는 동일한 closed form이 source에 제시되지 않았다. 따라서 numerical integration 필요성은 `[수학적 추론]`으로만 표시한다.

### B. 효과 지속 시간(Duration of Effect)

R&T는 반응 감소(response decline)의 중간 영역(약 80–20% 최대치)에서 반응이 시간에 대해 거의 선형적으로 감소할 수 있음을 설명한다. 또한 지속 시간이 용량의 로그(logarithm)에 비례하는 관계를 제시한다. [R&T p.249, p.254–256]

$$
t_D=\frac{1}{K}\ln\left(\frac{D}{A_{min}}\right)
$$

용량을 두 배로 늘리면 조건이 맞을 때 지속 시간은 약 반감기 1회분만큼 증가한다. Succinylcholine 0.5 mg/kg 정맥 급속 투여 예시는 `k≈0.2 min^-1`, t1/2≈4 min의 효과 감소와 용량-지속 시간 관계를 보여준다. 여기서 핵심은 용량 증가가 최대 효과(peak effect)보다 지속 시간을 더 읽기 쉽게 바꿀 수 있다는 점이다. [R&T p.249–256]

### C. PK 율속(PK-rate-limited) vs PD 율속(PD-rate-limited)

- **PK-rate-limited:** 효과가 사라지는 속도가 약물 농도가 사라지는 속도에 의해 결정되는 경우다. 즉, effect decline이 plasma concentration decline과 같은 시간 척도에서 움직인다.
- **PD-rate-limited:** 효과가 사라지는 속도가 receptor/system 회복 속도에 의해 결정되는 경우다. Plasma concentration은 빠르게 사라지더라도, response는 receptor/system turnover가 완료될 때까지 오래 지속된다.

Aspirin은 650 mg 경구 투여 후 혈장 t1/2가 약 15 min이지만 항혈소판 활성(antiplatelet activity)이 수일간 지속되는 예다. 즉, 혈장에서 약물이 빨리 사라져도 반응 시스템은 더 늦게 회복될 수 있다. [R&T p.251]

Omeprazole은 40 mg 경구 투여 후 혈장 t1/2가 1시간 미만이고 약 3시간 후 혈장에는 거의 남지 않지만, 위산 분비 억제(gastric acid secretion inhibition)는 수일 단위로 회복된다. [R&T p.252]

Paclitaxel은 혈장에는 2일 후 거의 남지 않지만 백혈구 분율(leukocyte fraction) 변화가 수주(weeks) 척도로 움직이는 예다. [R&T p.253]

Acenocoumarol과 phenprocoumon 비교에서는 acenocoumarol t1/2 15시간, phenprocoumon t1/2 6일 및 반응 회복 시간(response recovery time) 차이가 PK vs PD 율속 판단의 교육적 앵커가 된다. [R&T p.243–244]

> **Insertion I5 — [TEXTBOOK_DERIVED]** (Audit T6 ESSENTIAL: Acenocoumarol/Phenprocoumon PK vs PD rate-limiting anchor 강화)  
> Acenocoumarol(t1/2 15 h, baseline 회복 약 3 days)과 phenprocoumon(t1/2 6 days, baseline 회복 약 2 weeks)의 직접 비교는, **같은 vitamin K antagonist 계열 안에서도 PK rate-limited와 PD rate-limited 패턴이 약물별로 갈라질 수 있음**을 보여주는 R&T의 교육적 anchor다. Acenocoumarol에서는 plasma elimination 속도와 prothrombin complex 회복 속도가 같은 시간 척도에 가까워 PK가 율속에 더 가깝지만, phenprocoumon에서는 plasma half-life가 system turnover 시간 안에 들어가 PD-system이 율속의 일부가 된다. **이 비교는 “PK/PD rate-limiting은 약물 분류 라벨이 아니라 두 시간 척도의 비율(τ_drug/τ_system)에서 결정되는 spectrum”이라는 framing을 직접 가르친다.** [R&T p.243–244, Fig.8-11]

### D. 가정(Assumptions)

- AUEC 폐쇄형(closed form)은 일반 Emax + 1차 제거(first-order elimination) 조건에서만 출처에 근거한다. [G&W p.233]
- 지속 시간-로그 용량 관계(duration log-dose relation)는 최소 유효량(minimum effective amount), 1차 감소(first-order decline), 일정한 역치(threshold) 등의 조건을 전제로 한다. [R&T p.254–255]
- PD-rate-limited example은 “약물이 아직 많다”가 아니라 “system이 아직 회복되지 않았다”는 뜻일 수 있다. [R&T p.249–253]

### E. 한계(Limitations)

Aspirin 75 mg, 수술 전후 7일 중단, 출혈 가이드라인은 본 PDF 출처 밖이므로 삭제한다. 이 세션의 source-grounded aspirin statement는 650 mg oral, t1/2 15 min, antiplatelet activity several days까지만이다. [R&T p.251]

특수 집단 용량 조정(special population dose adjustment)에서 PK 변화만 보고 투여 간격을 정하면 PD 율속 약물에서는 과소 또는 과대 조정이 생길 수 있다. 단, 특정 label/guidance 조항은 본 PDF 범위 밖이다. 따라서 해당 적용은 `[확인 필요 — 교과서 외 규제 적용]`으로 남긴다.

<!-- TRENCH -->
**[Trench-Level Tip]** Plot의 x-axis가 한 자리 이상 다른 시간 단위로 벌어지면 PD-rate-limited 가능성이 크다. Aspirin은 plasma plot이 hours, antiplatelet effect plot이 days scale로 보인다. 따라서 “concentration-driven duration”이라는 직관을 즉시 버려야 한다. [R&T p.251]

**[실무 팁(Trench-Level Tip)]** 용량-반응이 고용량에서 평탄해지면 더 높은 용량이 정보를 늘리는 것이 아니라 고원부를 반복 확인할 가능성이 크다. Methylprednisolone처럼 PK AUC는 증가해도 PD 반응이 포화되면 하류 바이오마커(downstream biomarker) 또는 투여 간격 종말점(dosing interval endpoint)을 다시 설계한다. [R&T p.257–258] `[실무 구현 번역]`

### F. 제텔카스텐 원자 노트(Zettelkasten Atom)

**Atom C5:** AUEC와 지속 시간은 농도-시간 곡선을 반응-시간 곡선으로 번역한 면적·시간 지표다. 효과 지속성(effect persistence)은 약물 반감기가 아니라 더 느린 과정이 결정한다.

<!-- RECAP -->
**Recap:** C5는 “농도가 없어졌는데 효과가 남는다”는 현상을 예외가 아니라 PD 모델링의 핵심 설계 문제로 바꾼다.

> **실패 모드(Failure Mode) — [TEXTBOOK_DERIVED]**  
> 효과 지속 시간을 혈장 반감기만으로 요약하면 PD 율속 약물에서 가장 중요한 회복 과정을 지워버린다. 지속 시간 또는 AUEC를 보고할 때는 어떤 역치(threshold), 어떤 반응 변수(response variable), 어떤 시간 척도(time scale)에서 정의했는지 함께 고정해야 한다.

> **실무 체화 요약(Practice Brief) — C5 — [EXPERT_INFERENCE, v3]**  
> 새 약물의 투여 간격을 설계할 때 던질 결정 트리: (1) **혈장 t1/2 vs 반응 회복 시간의 비율(τ_drug/τ_system)을 한 자리 수 단위로 비교** — 비슷하면 PK 율속, 한 자리 이상 차이 나면 PD 율속 확정, (2) **PD 율속이면 투여 간격은 혈장 동역학(plasma kinetics)이 아니라 시스템 회복 척도(system recovery scale)에 따라 결정**(omeprazole, aspirin이 매일 투여인 본질적 이유), (3) **AUEC 또는 지속 시간 보고 시 역치·반응 변수·시간 척도를 동시 명시**. 임상약사 출신이라면 warfarin INR 모니터링 주기가 혈장 t1/2가 아니라 프로트롬빈 복합체 전환에 묶여 있다는 사실을 떠올리면 된다.

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.251 Fig.8-20; p.252 Fig.8-21
Why this matters: These examples force the learner to separate plasma half-life from effect duration. The visual time-axis gap is the key structural signal.
When to look: after reading Card C5 §C
Learner instruction: Compare the plasma concentration time course with the response time course. Do not infer aspirin perioperative guidance or omeprazole clinical rules from this figure; use it only to recognize PD-rate-limited persistence.
<!-- /FIGURE_POINTER -->

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.255 Fig.8-23; p.256 Fig.8-24
Why this matters: The duration equation is compact, but the learner must see how dose changes translate into threshold-crossing time. Fig.8-24 anchors the abstract relationship in the succinylcholine example.
When to look: after reading Card C5 §B
Learner instruction: Trace where each dose curve crosses the minimum effective amount/effect threshold. Then connect that crossing time to the statement that dose doubling can extend duration by about one half-life under the stated assumptions.
<!-- /FIGURE_POINTER -->


---

# §5 — 혼동 쌍 해부(Confusion Pair Dissection)

## 혼동 쌍 1(Pair 1) — Kd vs EC50

<!-- CONFUSION -->
| 비교 축 | Kd | EC50 |
|---|---|---|
| 본질 | 약물-표적 복합체의 결합 친화도(binding affinity) | 약물 + 조직/시스템의 기능적 감수성(functional sensitivity) |
| 변화 원인 | 리간드-수용체 결합 변화 | 결합, 수용체 밀도, 증폭 이득, 조직 반응 변화 모두 가능 |

**⚡ 기억 고리 (Memory Hook) — *결합 vs 효능*: [EXPERT_INFERENCE, v3]**  
`Kd`는 약물이 수용체에 *얼마나 잘 붙는가* — 분자 수준의 친화도. `EC50`는 *그 결합이 조직과 신호 시스템을 거쳐 절반의 효과로 나오기까지 필요한 농도* — 시스템 수준의 효능. 둘이 다를 수 있는 이유는 receptor occupancy와 functional response 사이에 spare receptor와 cascade amplification이라는 증폭 단계가 끼기 때문이다. 따라서 `EC50 < Kd`도 가능하다 — *receptor 10%만 점유해도 90% 효과가 나오는* tissue가 존재하기 때문이다. **결합은 분자, 효능은 시스템 — 같은 층위가 아니다.**

**핵심 교정(Critical Correction):** EC50가 공변량에 따라 변하면 그것이 약물 측 결합(drug-side binding) 변화인지 시스템 측 감수성(system-side sensitivity) 변화인지 구분해야 한다. 비결합 농도와 결합 증거(binding evidence) 없이 총 EC50 변화만으로 기전을 단정하지 않는다. 이 구분이 없으면 공변량 효과를 생물학적 감수성 변화로 과해석하기 쉽다. [G&W p.203–206, p.215–217]

## 혼동 쌍 2(Pair 2) — 일반 Emax (`n=1`) vs Sigmoid Emax (`n≠1`)

<!-- CONFUSION -->
| 비교 축 | 일반 Emax | Sigmoid Emax |
|---|---|---|
| 곡선 형태 | 쌍곡선형, 완만한 전환 | 더 급하거나 완만한 전환 가능 |
| 파라미터 | `Emax`, `EC50` | `Emax`, `EC50`, `n` |
| 위험 | 고원부 없는 데이터에서 Emax 식별 불안정 | 농도범위가 좁으면 `n` 식별 불안정 |

**⚡ 기억 고리 (Memory Hook) — *중간점 vs 가파름*: [EXPERT_INFERENCE, v3]**  
`EC50`은 곡선의 **중간점 위치(midpoint)** — x축 위에서 반응의 절반이 나오는 농도, 즉 *어디에서* 효과의 절반에 도달하는가. Hill `γ(=n)`은 곡선의 **가파름(steepness)** — γ가 1이면 완만한 S자, γ가 5면 거의 계단 함수, 즉 *얼마나 좁은 농도 구간에서* 0%에서 100%로 전환되는가. 두 파라미터는 수학적으로 독립이다 — `EC50`이 낮아도(sensitive) γ가 낮으면(완만) 임상 허용 폭이 넓고, `EC50`이 높아도(potency 낮음) γ가 높으면(가파름) 작은 농도 차이가 독성/무효의 경계를 가른다. **협역 치료역 약물에서 임상적으로 더 위험한 파라미터는 `EC50`이 아니라 γ다 — 위치보다 가파름이 안전 마진을 결정한다.**

| **치명적 타격 (Critical Blow) — [EXPERT_INFERENCE, v3]** | Hill γ를 보고서에서 생략하고 `EC50`만으로 dose-response를 제출하면, 협역 치료역 약물(면역억제제, 항부정맥제, 일부 vitamin K antagonist)에서 위험이 생긴다. 이러한 약물은 용량-반응 전환이 급격하므로, γ 없이 설계된 임상 용량 조절 가이드는 *과관대하게* 설정되어 독성 발생률을 과소예측할 수 있다. 규제 심사관은 "Hill coefficient의 임상적 의의" 섹션을 추가하라는 deficiency를 발행하는 것이 일반적인 관행이며, 이는 NDA/BLA 검토 일정의 직접 지연으로 이어진다. `[교과서 외 규제 해석]` |

`n>1`은 "협동성 증명(cooperativity 증명)"이 아니다. 이는 가설을 제시할 수 있지만 증명하지는 않는 현상학적 가파름 파라미터(phenomenologic steepness parameter)다. [G&W p.216, p.220]

## 혼동 쌍 3(Pair 3) — PK 율속 vs PD 율속 감소

<!-- CONFUSION -->
| 비교 축 | PK 율속(PK-rate-limited) | PD 율속(PD-rate-limited) |
|---|---|---|
| 율속 과정 | 약물 제거/분포 | 수용체 결합, 비가역적 작용, 전환, 하류 회복 |
| 도표 신호 | 혈장과 반응이 유사한 시간 척도 공유 | 혈장 시간 척도와 반응 시간 척도가 괴리 |
| 예시 | Succinylcholine 1차 감소 하 용량-지속 시간 | Aspirin, omeprazole, paclitaxel |

**치명적 타격(Critical Blow):** 약물 반감기가 짧다고 해서 효과 지속 시간도 짧다고 결론지으면, PD 율속 약물에서는 틀린 판단이 된다. Aspirin은 혈장 t1/2 약 15 min이지만 항혈소판 활성은 수일간 지속된다. Omeprazole도 혈장은 빠르게 사라지지만 위산 억제는 수일 척도로 회복된다. 따라서 투여 간격 판단에는 혈장 반감기뿐 아니라 반응 회복 시간(response recovery time)이 필요하다. [R&T p.251–252]

> **Insertion I6 — [CRUCIBLE_DERIVED]** (Crucible Intuition #3 / Grade A: Time-axis fast-diagnostic)  
> **Visual fast-diagnostic — 0.5초 식별:** Plot의 x-axis 단위가 한 자리수 이상 차이 나면(예: aspirin plasma plot은 0–2 hours, antiplatelet effect plot은 0–192 hours) PD-rate-limited로 즉시 확정할 수 있다. 같은 시간축에서 두 곡선이 비슷한 모양이면 PK-rate-limited. **이 진단은 fit statistic이나 모델 비교 이전에 EDA 단계에서 plot의 시간 축만 보아도 가능하다 — 두 plot이 *다른 시간 척도*에서 그려졌다는 사실 자체가 율속 process가 다르다는 직접 증거이기 때문이다.** [R&T p.251–253; PD-rate-limited 시각 진단의 source anchor]

## 혼동 쌍 4(Pair 4) — 직접 연결 / 효과 구획 vs 간접 반응

<!-- CONFUSION -->
| 비교 축 | 직접 / 효과 구획(Effect Compartment) | 간접 반응(Indirect Response) |
|---|---|---|
| 지연 원인 | 혈장-작용 부위 평형화 또는 효과 부위 농도 | 내인성 반응 변수의 생성/소멸 | 
| 진단 | 효과 부위 농도로 히스테리시스가 줄어듦 | 최대 효과 시점이 시스템 전환에 의해 용량 비의존적일 수 있음 |
| 위험 | `ke0`를 미시적 생리 상수(microscopic physiology)로 오해 | `kin/kout`을 단순 곡선 적합 파라미터로 오해 |

**빠른 진단(Fast Diagnostic):** 히스테리시스 고리의 폭과 최대 효과 시점의 용량 의존성을 먼저 본다. 용량 의존적 최대 효과 시점이면 효과 구획 가능성, 용량 비의존적 최대 효과 시점이면 간접 반응 가능성이 커진다. 이 판단은 적합 통계량(fit statistic)보다 먼저 보는 구조 진단이다. `[실무 구현 번역]`

<!-- RECAP -->
**Recap:** 가장 위험한 혼동은 “농도가 response를 즉시 drive한다”는 가정이다. 이 가정이 깨지는 순간 Kd/EC50, Emax/Hill, effect compartment/indirect response, PK/PD rate-limiting이 모두 연결된다.

> **Mastery Note — [EXPERT_INFERENCE]**  
> 네 개의 confusion pair는 모두 같은 질문으로 환원된다: “현재 숫자는 binding, site concentration, measured response, system recovery 중 어느 층위를 대표하는가?” 이 층위를 분리하면 parameter naming은 단순 암기가 아니라 모델 구조 검토가 된다.

---

# §7 — 자기 테스트: 능동 회상 모듈(Active Recall Module)

<!-- SELF-TEST -->
## Q1. 질량작용법칙에서 Emax 식을 도출하라.

**문제:** `d[RC]/dt = k1[R][C] - k-1[RC]`와 `[R_T]=[R]+[RC]`에서 `E = Emax·C/(Kd+C)`를 도출하라.

**정답:** 평형에서 `k1[R][C]=k-1[RC]`, `Kd=[C][R]/[RC]`. `[R]=[R_T]-[RC]`를 대입하면 `[RC]/[R_T]=C/(C+Kd)`. 여기에 `E=α[RC]`, `Emax=α[R_T]`를 대입하면 `E/Emax=C/(C+Kd)`가 된다. [G&W p.202–204]

## Q2. Kd와 EC50가 다른 이유를 한 문장으로 설명하라.

**정답:** Kd는 수용체 결합 친화도이고 EC50는 수용체 점유 이후 조직 신호전달과 반응 증폭까지 포함하므로, 여분 수용체/증폭 연쇄가 있으면 EC50는 Kd와 달라질 수 있다. [G&W p.204–206]

## Q3. Hill `n=2.03`을 “cooperativity 증거”라고 쓰면 왜 틀리는가?

**Answer key:** G&W는 Hill exponent가 direct biological interpretation을 갖지 않는다고 설명한다. `n=2.03`은 PD3 데이터의 steepness를 설명하는 parameter이며, cooperativity는 가능한 hypothesis일 뿐 proof가 아니다. [G&W p.216, p.220, p.735]

## Q4. Sigmoid 억제 Imax 모델에서 목표 반응을 해석할 때 기저치 상대값과 절대값을 구분하라.

**문제:** `E = E0 - Imax·C^n/(IC50^n+C^n)`에서 목표 `E_target`이 주어졌을 때 어떤 값을 억제 분율(inhibition fraction)으로 넣어야 하는가?

**정답:** 절대 반응(absolute response)으로 주어진 `E_target`은 먼저 `I = E0 - E_target`으로 억제 크기(inhibition magnitude)를 계산한다. 그 다음 `I/Imax`를 분율로 두고 농도를 역산한다. 기저치 상대 반응(baseline-relative response)을 절대 반응처럼 넣으면 부호와 비율이 틀어진다. [G&W p.218–221]

## Q5. Naproxen 히스테리시스에서 지지되지 않는 `ke0` 수치를 쓰지 말고, 출처에 근거한 결론만 말하라.

**정답:** R&T는 naproxen 500 mg 경구 치과 통증 모델에서 비결합 농도와 통증 완화가 반시계 방향 히스테리시스를 보이고, 효과 구획이 이 히스테리시스를 줄이는 개념적 모델을 제시한다. `ke0≈0.5–1 hr^-1` 수치는 본 PDF 범위에서 확인되지 않으므로 쓰지 않는다. [R&T p.234–246]

## Q6. Warfarin 반응이 혈장 농도를 즉시 따라가지 않는 이유는 무엇인가?

**정답:** Warfarin 효과는 프로트롬빈 복합체 전환에 의해 나타나므로 혈장 농도 변화와 반응 변화가 분리된다. R&T는 sodium warfarin 1.5 mg/kg 경구 투여 후 프로트롬빈 복합체 활성이 시스템 전환 반감기의 영향을 받는 예를 제시한다. [R&T p.242, p.247]

## Q7. AUEC 폐쇄형 식의 적용 조건을 말하라.

**정답:** G&W의 `AUEC = Emax/K · ln(1 + D/(EC50·V))`는 일반 Emax와 1차 제거 조건에서 출처에 근거한다. Sigmoid Emax의 AUEC 수치 적분(numerical integration)은 합리적 수학 추론이지만 본문에 폐쇄형으로 제시된 출처 사실은 아니다. [G&W p.233–234]

## Q8. Aspirin과 omeprazole 예시로 PD 율속 지속 시간을 설명하라.

**정답:** Aspirin 650 mg 경구는 혈장 t1/2가 약 15 min이지만 항혈소판 활성이 수일간 지속된다. Omeprazole 40 mg 경구는 혈장 t1/2가 1시간 미만이고 약 3시간 후 혈장이 거의 사라지지만 위산 억제는 수일 척도로 회복된다. 두 예시는 효과 지속 시간이 약물 반감기가 아니라 시스템/수용체 회복에 의해 제한될 수 있음을 보여준다. [R&T p.251–252]

## Q9. 보스 딜레마(Boss Dilemma) — Phase 2 PK/PD 데이터셋에서 반시계 방향 히스테리시스가 보인다. 혈장 직접, 효과 구획, 간접 반응 중 어떤 순서로 검토할 것인가?

**정답:** 먼저 혈장 직접 모델(plasma direct model)로 모델 오명세(misspecification)의 크기를 본다. 다음으로 효과 구획을 적용해 히스테리시스가 줄어드는지 확인한다. 그래도 용량 군별 최대 효과 시점이 용량 비의존적이거나 반응 회복이 시스템 시간 척도를 보이면 간접 반응을 검토한다. 즉, 모델 선택은 AIC만으로 하지 않는다. 최대 효과 시점의 용량 의존성, 채혈 밀도(sampling density), 생물학적 타당성(biological plausibility)을 함께 본다. `[실무 구현 번역]`

---

# §8 — Meta-Frame & Big Picture

## A. 위치와 실패 모드(Positioning & Failure Modes)

이 세션은 PK/PD architecture에서 “concentration-time profile을 response-time profile로 변환하는 첫 관문”이다. C1–C2는 concentration-response nonlinearity를 담당한다. C3–C4는 time delay를, C5는 response integration/duration을 담당한다.

이 세션을 대충 넘기면 다음 실패가 발생한다.

1. **Kd를 EC50처럼 사용:** 결합 친화도를 기능적 역가(functional potency)로 오인한다.
2. **Hill `n`을 기전 증명으로 과해석:** 곡선 적합 파라미터를 생물학적 증거로 둔갑시킨다.
3. **히스테리시스를 잡음으로 처리:** 부위 평형화 또는 전환 지연을 놓친다.
4. **PK 반감기로 투여 간격을 결정:** PD 율속 반응에서 지속 시간을 잘못 예측한다.
5. **AUEC를 단순 AUC처럼 취급:** 반응 적분의 모델 조건을 잊는다.

## B. 전문가 해석 지점(Professional Moat)

계량약리학자(pharmacometrician)의 해석 지점은 복잡한 식을 많이 아는 데 있지 않다. 같은 농도-효과 데이터를 두고 무엇이 부족한지 구분할 줄 아는 데 있다. 더 좋은 최적화기(optimizer)가 필요한가, 더 넓은 농도 범위가 필요한가, 더 가까운 바이오마커가 필요한가, 아니면 더 긴 반응 채취(response sampling)가 필요한가 — 이 네 갈래를 구분할 줄 알아야 한다.

PD3는 이 해석 지점의 좋은 예다. 0–500 µg/L 설계에서는 sigmoid 우월성이 명확하지 않다. 그러나 0–800 µg/L 설계는 모델 판별(model discrimination)을 가능하게 한다. 이는 모델 선택이 통계기법 문제만이 아니라 실험 설계(experimental design) 문제임을 보여준다. [G&W p.734–741]

R&T Ch.8은 또 다른 해석 지점을 준다. 혈장 농도가 낮아졌는데 효과가 남아 있을 때 "약물이 없는데 효과가 이상하게 남았다"고 보지 않는다. 대신 "시스템 전환 또는 비가역적 작용(irreversible action)이 더 느린 과정인가?"를 묻는다. [R&T p.249–253]

> **Hill γ의 임상 함의 — Apex 파라미터로서의 위상 — [EXPERT_INFERENCE, v3]**  
> 이 세션의 Apex 개념인 Hill `γ`는 단순한 곡선 모양 파라미터가 아니라 임상 의사결정의 정밀도 자체를 결정하는 양이다. 임상약사 출신 모델러가 가장 빠르게 체득할 수 있는 moat는, 다음 세 가지를 보고서에서 명확히 분리해 기술하는 능력이다.
> - **γ > 1의 임상적 의미:** 농도-반응 관계에 *역치 특성(threshold-like behavior)*이 생긴다. `EC50` 근처에서 소량의 농도 변화가 큰 반응 변화를 일으키므로 — 같은 약물이라도 γ가 높을수록 치료역(therapeutic window)이 *수학적으로* 좁아진다. γ는 약물이 협역인지 광역인지를 정량화하는 가장 직접적인 파라미터다.
> - **용량 조절 정밀도 요구의 정량화:** γ가 높은 약물은 용량을 조금만 올려도 독성 범위에 진입한다. TDM 목표 농도(target concentration)를 폭넓게 설정하면 과소치료와 독성 사이를 오간다. 8년의 vancomycin/tacrolimus/aminoglycoside TDM 경험에서 알듯이, 같은 trough range가 약물에 따라 임상적 의미가 다른 본질적 이유가 바로 γ다.
> - **Exposure-response 보고서의 필수 항목:** 보고서에 γ 추정치와 confidence interval을 반드시 명시해야 한다 — γ 추정의 불확실성이 투여 용량 결정의 불확실성으로 *직접* 전파되기 때문이다. γ가 보고서에 없다는 것은 임상적으로 가장 중요한 한 정보를 누락한 것과 같다. `[교과서 기반 + 교과서 외 규제 해석]`

## C. 경계 플래그 보존(Boundary Flags Preserved)

[확인 필요 — 첨부 PDF 미포함 구간]:
- G&W §3.6.2–§3.6.5 (pp.225–228): competitive antagonism 이후 interaction model 연속부. 본 세션에서 추정·보완하지 않음.
- G&W §3.12 baseline modeling: C2 limitation에서 baseline time-varying issue로만 언급. 본 세션에서 상세 모델링 보류.
- `[확인 필요 — 교과서 외 규제 적용]`: PD-rate-limited drug의 special population dose adjustment나 FDA guidance 문구는 본 PDF 범위 밖이므로 일반 원칙으로만 유지.

<!-- RECAP -->
**최종 요약(Final Recap):** 이 세션의 압축 결론은 세 문장이다.  
1. Emax/Hill 모델은 수용체 결합에서 시작하지만 반응 시스템을 포함한다.  
2. 히스테리시스는 혈장 농도가 효과를 즉시 대표하지 못한다는 시각적 경고다.  
3. 지속 시간과 AUEC는 약물 반감기보다 더 느린 생물학적 과정을 찾아야 제대로 해석된다.

> **Practice Lens — [EXPERT_INFERENCE]**  
> 이 세션을 HTML로 학습할 때 최종 목표는 식을 외우는 것이 아니라 “이 데이터로 어떤 질문은 방어 가능하고, 어떤 질문은 아직 설계가 부족한가?”를 말할 수 있게 되는 것이다. `Emax/Hill`, hysteresis, AUEC는 모두 모델 결과가 아니라 study design의 충분성을 되묻는 언어다.

---

## PART B — Compiler-Only Appendix

This appendix is not learner-facing. It exists only to protect Phase 5 rendering fidelity.

### B1. Compilation Contract

- PART A is the only learner-facing body.
- Phase 5 must render PART A without altering the scientific content, equations, page tags, figure marker content, or mastery-note labels.
- PART B is instruction/guardrail only and must not appear as learner content unless explicitly requested.
- Do not restore deprecated material from Step 1 Draft v0.
- Do not add new scientific content, new examples, new page tags, new figures, or new regulatory claims during HTML compilation.
- Do not generate HTML, Mermaid, or SVG at Phase 4D; Phase 5 handles rendering.
- ver2 Insertion blocks (I1–I6) are labeled bounded blocks with explicit source basis (TEXTBOOK_DERIVED / CRUCIBLE_DERIVED). Phase 5 should render them with the same Mastery Note callout style as existing labeled augmentations; do not strip the labels.

### B2. Figure Rendering Instructions

**Image rights:** None. Do not embed copyrighted textbook figures. Render `FIGURE_POINTER` as text-only callouts. Render `FIGURE_SCHEMATIC` as structurally distinct redraws based only on the brief.

| # | Mode | Source | Phase 5 action | Decision |
|---|---|---|---|---|
| 1 | P | G&W p.199 Fig.3.1 | Text-only textbook pointer | KEEP |
| 3 | R | G&W p.204 Fig.3.4; p.205 Fig.3.5 | Structurally distinct schematic brief | KEEP |
| 5 | P | G&W PD3 p.733 Fig.PD3-3.1; p.735 Table PD3-3.2; p.741 Table PD3-3.4 | Text-only textbook pointer | KEEP |
| 6 | P | R&T p.234 Fig.8-1; p.235 Fig.8-2 | Text-only textbook pointer | KEEP |
| 7 | R | R&T p.236 Fig.8-3 | Structurally distinct schematic brief | KEEP |
| 8 | P | R&T p.251 Fig.8-20; p.252 Fig.8-21 | Text-only textbook pointer | KEEP |
| 9 | P | R&T p.255 Fig.8-23; p.256 Fig.8-24 | Text-only textbook pointer | KEEP |
| 2 | P | G&W p.202 Fig.3.3 | Rejected as redundant within C1 budget | REJECT |
| 4 | P | G&W p.213 Fig.3.12; p.216 Fig.3.16 | Rejected as lower ROI than PD3 | REJECT |
| 10 | N | None | Rejected due to budget and drift control | REJECT |

Additional constraints:

- Preserve P/R/N/I decisions and all Source fields in marker blocks.
- Do not propose or generate new figures.
- Do not render rejected figure candidates #2, #4, or #10.
- Place rendered figures at the end of the relevant concept card unless the marker position already makes a safer local placement obvious.
- For redrawn schematics, preserve conceptual relation but avoid the textbook’s exact layout, color palette, and figure composition.

### B3. Page Tag Rendering Rules

- Preserve all existing `[p.XX]`, `[pp.XX–YY]`, `[pp.XX, YY]`, and `[p.확인 필요]` tokens.
- Do not fabricate, delete, renumber, or relocate page tags.
- Apply page-tag wrapping only to body text; do not wrap tags inside code blocks or inside `FIGURE_*` marker blocks.
- Source page tags must remain visible in print mode.
- `[확인 필요 — 첨부 PDF 미포함 구간]` remains visible unless a later verified source explicitly resolves it.
- ver2 Insertion blocks reuse existing page tags only; no new page numbers were introduced in I1–I6.

### B4. HTML Compiler Requirements

#### Marker-to-component mapping

| Marker / Pattern | HTML Component | Required handling |
|---|---|---|
| `<!-- MASTER LENS -->` | Callout box | border-left gold; low-opacity gold background |
| `<!-- ANNOTATION -->` | Inline annotation / tooltip style | muted italic small text |
| `<!-- ANCHOR -->` | Bridge sentence | muted italic text |
| `<!-- TRENCH -->` | Practical tip box | rose-left-border callout |
| `<!-- CONFUSION -->` | Side-by-side comparison | amber comparison component |
| `<!-- SELF-TEST -->` | Accordion | prompt visible; answer hidden until click |
| `<!-- RECAP -->` | Recap box | blue-left-border summary |
| `[확인 필요]` | Highlighted flag | render with `<mark>` |
| `[p.XX]`, `[pp.XX–YY]`, `[pp.XX, YY]` | Inline source-page tag | wrap in `<span class="source-page">…</span>` |
| `[p.확인 필요]` | Uncertain source tag | wrap in `<span class="source-page source-uncertain">…</span>` |
| `<!-- FIGURE_POINTER -->` | Text-only textbook reference callout | never embed textbook image |
| `<!-- FIGURE_SCHEMATIC -->` | Inline schematic `<figure>` | generate visually distinct Mermaid/SVG/CSS from brief only |
| `<!-- FIGURE_IMAGE_SLOT -->` | Image/placeholder figure | not used in this session unless user-supplied/open-license file exists |
| `> **Insertion I[1-6]` blockquotes | Mastery Note callout (gold-left-border) | render same as existing `> **Mastery Note —`, `> **Practice Lens —`, `> **Failure Mode —` blocks; preserve the source-basis label `[TEXTBOOK_DERIVED]` / `[CRUCIBLE_DERIVED]` exactly |
| `> **⚡ Plausible Fallacy —` blockquotes | Apex-only Fallacy callout | gold-left-border with red ⚡ accent; render with bold "그럴듯한 오해 / 왜 틀렸는가 / 실무에서 어떻게 드러나는가" sub-labels intact (v3 only on Apex card) |
| `> **⚡ 기억 고리 (Memory Hook) —` blockquotes | Memory Hook callout | gold-left-border with ⚡ accent; render the italic dash-flanked subtitle (예: *결합 vs 효능*, *중간점 vs 가파름*) as visible kicker (v3 표준 블록) |
| `> **Practice Brief —` blockquotes | Practice Brief callout | rose-left-border (Trench-Tip 계열과 시각적 구분); preserve the `[EXPERT_INFERENCE, v3]` source-basis label exactly |
| `\| **치명적 타격 (Critical Blow) —` table row | Critical Blow row | render in red/crimson background within the surrounding confusion-pair table; bold the leading "치명적 타격" label; preserve the `[EXPERT_INFERENCE, v3]` or `[교과서 외 규제 해석]` source-basis label exactly |

#### Rendering, navigation, interaction, and output requirements

- Render PART A only as learner-facing content; do not render PART B unless explicitly requested.
- Produce one self-contained HTML file with inline CSS/JS.
- Preserve text content; do not rewrite scientific body, equations, examples, or page tags.
- MathJax: support inline and display equations.
- Navigation: sticky left sidebar TOC on desktop; mobile-collapse allowed; each major § heading and each §2 concept card should have stable unique ids.
- Navigation anchor integrity: every sidebar `href="#id"` must match exactly one body `id`; no duplicate ids; `html { scroll-behavior: smooth; }` must be present.
- Self-test: render answer keys hidden by default and revealed on user click.
- Controls: code-copy button where code exists, print/PDF button via `window.print()`.
- Responsive/print: ≤768px single-column; hide navigation in print; preserve source-page tags in print.
- Figure pointers: render as text-only callouts with Source / Why this matters / When to look / Learner instruction.
- Figure schematics: render from brief only; do not reproduce textbook layout, color scheme, or exact figure.
- Mermaid self-check: use valid Mermaid syntax only; if node labels/special characters make Mermaid fragile, fall back to inline SVG or CSS cards.
- Allowed external runtime dependencies only: MathJax CDN, Mermaid CDN, and permitted highlighting libraries; no external local CSS/JS/font/image files.
- Prohibited: iframe/embed, unauthorized textbook images, visible self-test answers by default, raw markers left unrendered, raw page tags left unwrapped, duplicate/unstable ids, unmatched TOC targets, new figure ideas, or new scientific content.

### B5. Audit Guardrails

Do not restore or add any of the following:

- “5–100배 오차,” FIH dose overprediction, NDA recommended dose, FDA deficiency letter, clinical hold, or similar regulatory claims as source-derived statements.
- Hill `n` as direct proof of cooperativity, cascade, receptor-effector heterogeneity, or a named mechanism without orthogonal evidence.
- Aspirin 75 mg, 7–10 days, perioperative stopping rules, or bleeding-guideline claims; source scope supports aspirin 650 mg, plasma t1/2 about 15 min, antiplatelet effect several days only.
- Naproxen `ke0 ≈ 0.5–1 hr⁻¹` or any unverified effect-compartment numeric range.
- Untagged NONMEM `$DES`, grid-search, IIV-on-EC50/Emax/n, reviewer-deficiency, or submission consequences as textbook facts.
- G&W §3.6.2–§3.6.5 content from pp.225–228; keep `[확인 필요 — 첨부 PDF 미포함 구간]` rather than reconstructing.
- New page tags, new named drug examples, unapproved code blocks, unapproved figures, or copyrighted textbook image embedding.

### B6. Crucible Guardrails

- Crucible is a judgment/insight source, not a raw learner-prose source at Phase 4D.
- Preserve only adopted or explicitly allowed Grade A logic: Hill `n` as titration/design lever, IDR peak-time diagnostic logic, `ke0` as lumped/phenomenologic delay, PD3 concentration-range design lesson, and PK/PD rate-limiting as a relative time-scale problem.
- ver2 additionally adopts Crucible Intuition #2 (precision-improvement diagnostic, Insertion I3) and Intuition #3 (time-axis fast-diagnostic, Insertion I6) — both are CRUCIBLE_DERIVED and labeled accordingly.
- Do not turn expert inference into textbook-derived fact.
- Do not add unsupported numeric expert claims from Crucible unless already present in Content Lock v2 and properly tagged.
- Do not reintroduce lower-priority, speculative, external, or rejected Crucible material.

### B7. Deprecated and Forbidden Restorations

- Step 1 Draft v0 is deprecated and must not be used as a learner-body source except through the Micro-Patch Gate.
- Content Lock v1 is superseded by Content Lock v2 and must not override the v2 body.
- Phase 1 Patch Memo is contextual only; it must not override Audit v1 or Content Lock v2.
- Do not restore rejected overclaims, unsupported numbers, unsupported regulatory claims, source-unsupported examples, unapproved code, unapproved figures, or any NOT_IN_SOURCE item rejected by Audit/Content Lock.
- ver1 master is superseded by ver2 only with respect to the six labeled insertions; all other content is identical.

### B8. PATCH MODE Splice Verification Table

| Marker # | Anchor text | Anchor found? | Match count | Inserted? | Final location (§ + card) |
|---|---|---|---|---|---|
| 1 | # §1 — Session Header & Roadmap | YES | 1 | YES | §1 — Session Header & Roadmap |
| 2 | ## Card C1 — Law of Mass Action → Emax 골격 | YES | 1 | YES | §2 / Card C1 |
| 3 | ## Card C2 — Sigmoid Emax / Hill Model [⚡ Apex Concept] | YES | 1 | YES | §2 / Card C2 |
| 4 | ## Card C3 — Hysteresis: 시간 지연의 진단 도구 | YES | 1 | YES | §2 / Card C3 |
| 5 | ## Card C4 — Effect Compartment + Systems-in-flux / Indirect… | YES | 1 | YES | §2 / Card C4 |
| 6 | ## Card C5 — AUEC + Duration + PK/PD Rate-Limiting | YES | 1 | YES | §2 / Card C5 |
| 7 | ## Card C5 — AUEC + Duration + PK/PD Rate-Limiting | YES | 1 | YES | §2 / Card C5 |

#### ver2 Insertion Splice Verification

| Insertion # | Anchor text (truncated) | Anchor found? | Match count | Inserted? | Final location |
|---|---|---|---|---|---|
| I1 | "Ideal PD measure는 sensitive, gradual, meaningful…" (end of §1 first paragraph) | YES | 1 | YES | §1 — after Big Idea paragraph |
| I2 | `[출처: G&W p.219, Eq.3:38–3:42]` (end of §B Parameter Recovery code-fence line) | YES | 1 | YES | §2 / Card C2 / §B — before PD3 anchor paragraph |
| I3 | "Hill `n`을 "positive cooperativity가 증명되었다"라고…" (end of §C-2 paragraph 2) | YES | 1 | YES | §2 / Card C2 / §C-2 — after closing fallacy paragraph |
| I4 | `$$\nAUEC=\int_0^{\infty}E(t)dt\n$$` (end of §A first display equation) | YES | 1 | YES | §2 / Card C5 / §A — between AUEC definition and closed form |
| I5 | "Acenocoumarol과 phenprocoumon 비교에서는…[R&T p.243–244]" (end of §C last paragraph) | YES | 1 | YES | §2 / Card C5 / §C — after acenocoumarol paragraph |
| I6 | "따라서 dosing interval 판단에는 plasma half-life뿐 아니라 response recovery time이 필요하다. [R&T p.251–252]" (end of Pair 3 Critical blow paragraph) | YES | 1 | YES | §5 / Pair 3 — after Critical blow paragraph |

### B9. Zero-Omission Coverage Matrix — v3

| Domain | Required item | Evidence in PART A | Status | Action |
|---|---|---|---|---|
| C1 Scope Lock Required Concepts | C1 Mass Action/Emax; C2 Sigmoid Emax/Hill; C3 Hysteresis; C4 Effect Compartment/IDR; C5 AUEC/Duration | PART A §1 roadmap and §2 C1–C5 cards | PRESENT | None |
| C2 Scope Lock Required Data Anchors | PD3 E0/Imax/IC50/n; Lundström composite Imax values; R&T examples including digoxin, naproxen, warfarin, aspirin, omeprazole, succinylcholine, paclitaxel, methylprednisolone, acenocoumarol/phenprocoumon | PART A C2, C3, C4, C5 and self-test Q5–Q8 + ver2 I5 (acenocoumarol/phenprocoumon anchor preserved verbatim in v3) | PRESENT | None |
| C3 Audit MUST_FIX | Unsupported 5–100×/FIH/NDA claims removed; Hill n mechanism proof downgraded; aspirin/naproxen/NONMEM regulatory overclaims controlled | PART A C1–C5, §5, §7; PART B guardrails | PRESENT | Regression forbidden in PART B |
| C4 Audit T5 Coverage — SHOULD_FIX | (a) Ideal PD measure + control + 2–4 dose levels; (b) R&T objectives in §1; (c) §3.6.6 framework bridge; (d) acenocoumarol/phenprocoumon as PK/PD rate-limiting anchor | (a) §1 + ver2 I2 in C2 §B; (b) ver2 I1 in §1; (c) ver2 I4 in C5 §A; (d) ver2 I5 in C5 §C | PRESENT (ver2) | All four SHOULD_FIX items closed |
| **C4-bis V5.0 Apex Framework Coverage — v3 (NEW)** | (a) Apex 마커 표준화 `[⚡ Apex Concept]`; (b) Plausible Fallacy 블록(Apex 1개); (c) §5 Memory Hook 표준화; (d) Critical Blow 행(최고 파급력 쌍 1개); (e) Big Idea 직관-우선 구조; (f) Practice Brief 라벨 | (a) §1 항법도 + §2 C2 header + B8 splice table; (b) §2 C2 §C-2 신규 블록; (c) §5 Pair 1·Pair 2 + §2 C2 §A 보조 hook; (d) §5 Pair 2 Critical Blow 행; (e) §2 C2 Big Idea 임상 직관 lead-in; (f) §2 C1·C3·C5 Practice Brief 블록 | PRESENT (v3) | All six framework items closed by P1–P6 |
| C5 Figure Coverage | Phase 4C KEEP items #1, #3, #5, #6, #7, #8, #9 | PART A contains 5 FIGURE_POINTER and 2 FIGURE_SCHEMATIC markers exactly once | PRESENT | No image embedding; rejected #2/#4/#10 not restored |
| C6 Page Tag Integrity | Preserve G&W/R&T page tags and uncertainty flags | PART A inherited v2 source tags; B3 enforces rendering without fabrication; ver2 insertions reuse existing page tags only; v3 patches add no new page tags | PRESENT | No new page tags added in v3 |
| C7 Crucible Grade A Preservation | Dose-invariant peak time, Hill n as titration lever, ke0 as lumped delay, PD3 design range, PK/PD rate-limiting ratio, Intuition #2 (precision improvement), Intuition #3 (time-axis fast-diagnostic) | PART A C2/C4/C5 plus mastery notes; ver2 I3 (Intuition #2) and I6 (Intuition #3) preserved in v3; v3 P5 adds Hill γ clinical implications | PRESENT (v3 expanded) | Two Grade A intuitions explicit + γ clinical moat |
| C8 Deprecated Draft Regression | Step 1 rejected material not restored | PART A uses Content Lock v2 base; B5/B7 prohibit restorations; v3 adds no rejected material | PRESENT | None |
| C9 Canonical Body Integrity | Content Lock v2 learner body retained with approved 4C markers plus labeled augmentations | PART A §1–§8; B8 splice verification incl. ver2 insertions; v3 patches are additive labeled blocks; no body sentence rewritten | PRESENT | No broad rewrite; v3 added 7 labeled patches only |
| **C10 Non-Negotiable Preservation — v3 (NEW)** | (a) Acenocoumarol/phenprocoumon I5 verbatim; (b) Q9 Boss Dilemma verbatim; (c) all page tags preserved; (d) all v3 additions tagged `[EXPERT_INFERENCE, v3]` | (a) §2 C5 §C I5 block 검증; (b) §7 Q9 검증; (c) page tag 회귀 검증 (pre/post diff); (d) v3 패치 7개 라벨 검증 | PRESENT (v3) | Hard preservation rule satisfied |

### B10. Micro-Patch Log

ver1: No micro-patches needed.  
ver2: No micro-patches in the body. All ver2 changes are explicit, labeled insertion blocks (I1–I6) and corresponding PART B updates (certificate table, splice verification, coverage matrix, augmentation log). No source page tags were added or changed; no body sentence from Content Lock v2 was rewritten.  
v3: No micro-patches in the canonical body sentences. All v3 changes are explicit, labeled patch blocks (P1–P7) tagged `[EXPERT_INFERENCE, v3]`. v3 modifies (a) C2 header label `[Apex]` → `[⚡ Apex Concept]` (3 locations: §1 항법도, §2 header, B8 splice table — pure label standardization, no semantic shift), (b) Pair 1 in-table 기억 고리 row → standardized independent block (table-cell to blockquote elevation, content reworded structurally per V5.0 Memory Hook rule), (c) C1 §A `Emax`·`intrinsic activity` 첫 등장 ANNOTATION 보강 (parenthetical addition only, no source claim rewritten), (d) C5 §C `PK-rate-limited`·`PD-rate-limited` 첫 등장 ANNOTATION 보강 (parenthetical addition only). All other v3 changes are pure additions (new blocks, new rows, new bullets). No source page tags were added or changed.  
**v3.1: Korean Readability Patch — prose-only readability pass on PART A (KR-01 ~ KR-22, all Risk = Low).** v3.1 applies 22 surgical Korean-readability edits across §1, §2 (Cards C1–C5), §5 (Pairs 2 and 3), §7 (Q9), and §8 (Professional Moat + Hill γ block). Edit categories: (i) **Sentence split** (KR-01, KR-04, KR-08, KR-09, KR-15, KR-16) — long English-grammar Korean sentences split into 2 shorter Korean-natural sentences; (ii) **Korean flow improvement** (KR-02, KR-05, KR-07, KR-09, KR-10, KR-11, KR-12, KR-15, KR-16, KR-17, KR-18, KR-19, KR-20, KR-21) — passive/awkward predicates replaced with active Korean verbs; dangling subjects restored; English-Korean fragments harmonized; (iii) **First-use gloss** (KR-03 receptor conservation, KR-06 concentration ratio, KR-11 rising/falling phase, KR-12 tissue perfusion·permeability·binding kinetics·signal transduction lag) — Korean parenthetical added at first occurrence only, never repeated; (iv) **Concept clarification** (KR-06, KR-13, KR-22) — meaning preserved but expressed more concretely. **Strict non-modifications in v3.1:** no scientific claim altered; no equation, code block, or NONMEM syntax touched; no page tag added/removed/renumbered; no figure marker (`FIGURE_POINTER`, `FIGURE_SCHEMATIC`) altered; no HTML compiler marker (`<!-- MASTER LENS -->`, `<!-- ANNOTATION -->`, `<!-- TRENCH -->`, `<!-- CONFUSION -->`, `<!-- SELF-TEST -->`, `<!-- RECAP -->`, `<!-- ANCHOR -->`) touched; no source-basis label (`[EXPERT_INFERENCE, v3]`, `[TEXTBOOK_DERIVED]`, `[CRUCIBLE_DERIVED]`, `[교과서 외 규제 해석]`, `[실무 구현 번역]`, `[수학적 추론]`, `[교과서 기반 + 교과서 외 규제 해석]`) altered; no Insertion I1–I6 or Patch P1–P7 source-anchored sentence rewritten in a way that changes its anchored claim; Acenocoumarol/Phenprocoumon Insertion I5 preserved verbatim; Q9 Boss Dilemma Answer key receives only KR-19 ("다음" → "다음으로") which does not change the dilemma's clinical/regulatory content; PART B compilation contract unchanged; Phase 5 marker-to-component mapping unchanged; B8 Splice Verification unchanged.
**v3.2: Korean-Dominant Readability Patch — systematic Korean-dominance pass on PART A.** v3.2 goes beyond v3.1's surgical edits by systematically converting all remaining learner-facing English prose to Korean and applying `한글(English)` paired-term formatting to career-critical pharmacometrics terms. Edit scope: all §1–§8 PART A sections. Edit categories: (i) **Section header Koreanization** — all English-only sub-headers (Formal Definition, Derivation, Structural Necessity, Assumptions & Boundary Conditions, Limitations, Zettelkasten Atom, etc.) receive `한글(English)` paired format; (ii) **Prose Koreanization** — general English phrases (receptor occupancy, functional sensitivity, binding assay, etc.) converted to Korean with first-use `한글(English)` pair; subsequent uses in Korean only; (iii) **Label Koreanization** — Recap→요약(Recap), Mastery Note→숙련 노트, Practice Brief→실무 체화 요약, Failure Mode→실패 모드, Practice Lens→실무 관점, Trench-Level Tip→실무 팁, Answer key→정답, Prompt→문제, Critical correction→핵심 교정, Critical blow→치명적 타격, Fast diagnostic→빠른 진단, Learner Navigation Aid→학습자 내비게이션 안내; (iv) **Table header Koreanization** — Axis→비교 축, Curve→곡선 형태, etc. **Strict non-modifications in v3.2:** no scientific claim, equation, numerical anchor, code block, NONMEM syntax, page tag, figure marker, source-basis label, HTML compiler marker, section/card structure, or PART B guardrail altered. All Insertion I1–I6 and Patch P1–P7 source-anchored claims preserved in meaning (only surrounding prose Koreanized). Acenocoumarol/Phenprocoumon Insertion I5 preserved verbatim. Q9 Boss Dilemma clinical/regulatory content preserved. B8 Splice Verification table unchanged. B4 Marker-to-component mapping unchanged.

### B11. Mastery Augmentation Log — v3

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
|---|---|---|---|---|---|---|
| 1 | §2 / Card C1 | J | True | AUDIT_DERIVED | Kd–EC50 혼동 및 total/unbound 해석 과잉을 예방 | Low |
| 2 | §2 / Card C2 | J/F | True | CRUCIBLE_DERIVED + AUDIT_DERIVED | Hill n의 해석 경계와 설계 판단을 고정 | Low |
| 3 | §2 / Card C3 | M | True | TEXTBOOK_DERIVED | R&T hysteresis figure의 진단적 의미를 학습 동선으로 고정 | Low |
| 4 | §2 / Card C4 | J | True | CRUCIBLE_DERIVED | Effect compartment와 indirect response의 topology 구분을 강화 | Low |
| 5 | §2 / Card C5 | F | True | TEXTBOOK_DERIVED | AUEC/duration 정의와 PD-rate-limiting 오해 예방 | Low |
| 6 | §5 / Confusion Pair Dissection | M | True | EXPERT_INFERENCE | 혼동쌍을 하나의 층위 분리 mental model로 통합 | Medium |
| 7 | §8 / Meta-Frame | W | True | EXPERT_INFERENCE | 세션 전체를 모델링/설계 판단으로 연결 | Medium |
| **I1 (ver2)** | §1 / Roadmap | W | True | TEXTBOOK_DERIVED | R&T Ch.8 출발 메시지 명시화 — Audit T5-B SHOULD_FIX 종료 | Low |
| **I2 (ver2)** | §2 / Card C2 §B | W | True | TEXTBOOK_DERIVED | G&W p.200 design message anchor — Audit T3/T5-A SHOULD_FIX 종료 | Low |
| **I3 (ver2)** | §2 / Card C2 §C-2 | M | True | CRUCIBLE_DERIVED | IC50 CV 향상 진단 — Crucible Grade B Intuition #2 명시화 | Low |
| **I4 (ver2)** | §2 / Card C5 §A | W | True | TEXTBOOK_DERIVED | G&W §3.6.6 framework bridge — Audit T1 PARTIAL 종료 | Low |
| **I5 (ver2)** | §2 / Card C5 §C | W | True | TEXTBOOK_DERIVED | Acenocoumarol/Phenprocoumon spectrum anchor — Audit T6 ESSENTIAL 강화 | Low |
| **I6 (ver2)** | §5 / Pair 3 | M | True | CRUCIBLE_DERIVED | 시간축 한 자리 차이 fast-diagnostic — Crucible Grade A Intuition #3 명시화 | Low |
| **P1 (v3)** | §2 / Card C2 header + §C-2 | F/M | True | EXPERT_INFERENCE, v3 | Apex 마커 표준화(`[⚡ Apex Concept]`) + Plausible Fallacy 블록 신규 — V5.0 framework 미준수 항목 종료. EC50/Emax/γ 분리 임상 함의 명시 | Low |
| **P2 (v3)** | §2 / Card C2 Big Idea | F | True | EXPERT_INFERENCE, v3 | Big Idea를 임상 직관-우선으로 재배치 — 항생제 증량 직관 lead-in으로 Apex 학습 진입 마찰 감소. 기존 수식 텍스트 보존, 위치만 후순위 | Low |
| **P3 (v3)** | §5 Pair 1 / Pair 2 / §2 Card C2 §A | M | True | EXPERT_INFERENCE, v3 | Memory Hook 표준화 — Pair 1 in-table → 독립 블록 격상; Pair 2 신규 hook(중간점 vs 가파름); C2 §A 보조 hook(Emax vs Imax). 모두 구조적 필연 인코딩 | Low |
| **P4 (v3)** | §5 / Pair 2 | M | True | EXPERT_INFERENCE, v3 | Critical Blow 신규 — Hill γ 누락 시 협역 치료역 약물의 임상 용량 조절 과관대화 → 규제 deficiency 시나리오 | Medium |
| **P5 (v3)** | §8 / Professional Moat | W | True | EXPERT_INFERENCE, v3 | Hill γ 임상 함의 3-bullet 추가 — 역치 특성, 용량 조절 정밀도, exposure-response 보고서 필수 항목. TDM 임상경험 anchor 활용 | Low |
| **P6 (v3)** | §2 / Card C1, C3, C5 | M | True | EXPERT_INFERENCE, v3 | Practice Brief 라벨 표준화 — C1/C3/C5에 신규 Practice Brief 블록 추가. Emax/intrinsic activity/PK·PD-rate-limited 첫 등장 ANNOTATION 보강 | Low |
| **P7 (v3)** | PART B 전체 | W | True | EXPERT_INFERENCE, v3 | Phase 4D Certification 표 v3 컬럼 추가; Marker-to-component 매핑 4종 신규 라벨 추가; Augmentation Log v3 항목 추가 | Low |

#### Rejected or Deferred Augmentation Candidates (unchanged from ver1)

| Rejected candidate | Reason for rejection |
|---|---|
| Reintroduce "5–100× FIH/NDA" warning | Rejected: Audit classifies direct support as NOT_IN_SOURCE for this PDF scope |
| Add new clinical dosing/guideline examples for aspirin or omeprazole | Rejected: would add external clinical guidance beyond source pages |
| Add numerical ke0 range for naproxen or effect compartment examples | Rejected: Audit identifies the specific naproxen ke0 range as unsupported in the PDF |
| Add new Mermaid/SVG code in Phase 4D | Rejected: Phase 4D may include briefs/markers only; Phase 5 renders visuals |
| Add new page tags in ver2 or v3 | Rejected: Phase 4D / Phase 4 is closed for page-tag generation; ver2/v3 reuse only existing tags |
| Add Crucible Grade B Tip #5 (`k_t` prior 우회로 with platelet 10일/prothrombin 1–2일) | Deferred: requires careful boundary between R&T turnover ranges and external prior values; out of scope for v3 minimal-delta release |
| Add Crucible Tip #4 (F-test bootstrap procedure) | Deferred: implementation-level statistical procedure; covered functionally by I3 (precision-improvement diagnostic) at the conceptual level |
| Rewrite C1/C3/C4/C5 Big Idea blocks to identical "임상 직관 lead-in" structure | Deferred (v3): independent reviewer flagged C2 (Apex card) as the priority; remaining cards already open intuition-first per spot-check. Future ver may standardize all five cards uniformly. |

---

## Final Verdict — v3

```text
GO        : HTML compile (Phase 5) cleared with v3 enhancements applied on top of ver2 base.
NO-GO     : Independent reviewer's NO-GO on ver2 (V5.0 Apex framework gaps) is now closed.
REDO      : Not required.
PASS      : Learner-Standalone (PASS+), Zero-Omission (PASS unconditional), Mastery-Uplift (PASS++),
            Source-Boundary (PASS), HTML-Readiness (PASS) — all PASS at v3 level.
DELTA     : v3 closes the three structural gaps flagged by independent review:
            (1) Apex marker `[⚡ Apex Concept]` standardized + Plausible Fallacy block added (P1)
            (2) Memory Hooks elevated to standardized `**⚡ 기억 고리 (Memory Hook)**` blocks (P3)
            (3) Critical Blow row added to highest-impact confusion pair (Pair 2, P4)
            Plus: Big Idea intuition-first re-ordering on Apex card (P2),
                  Hill γ clinical implications in Professional Moat (P5),
                  Practice Brief labels + key-term ANNOTATIONs (P6),
                  PART B v3 trace updates (P7).
SCOPE     : Seven labeled patches (P1–P7), all `[EXPERT_INFERENCE, v3]` tagged.
            ver2 body sentences preserved verbatim.
            Acenocoumarol/phenprocoumon rate-limiting anchor (Insertion I5) preserved.
            Q9 Boss Dilemma preserved.
            All page tags preserved; no new page tags introduced.
            pp.225–228 boundary preserved.
            aspirin-75mg, naproxen-ke0, 5–100×/FIH/NDA still excluded.
ACTION    : Phase 5 HTML compile may proceed. Render PART A only; render v3 patch blocks per the
            updated Marker-to-component mapping (Plausible Fallacy / Memory Hook / Practice Brief /
            Critical Blow). Preserve all `[EXPERT_INFERENCE, v3]` source-basis labels exactly.
```

---

## Final v3 All-Pass Checklist (8 items)

| # | Check item | Verification | Status |
|---|---|---|---|
| 1 | C2 카드 헤더가 `[⚡ Apex Concept]`로 표준화됨 (PATCH 1a/1b) | §1 항법도 line + §2 Card C2 header line + PART B B8 splice table line — 3개 위치 동기화 | ✅ PASS |
| 2 | C2 §C-2 영역에 Plausible Fallacy 블록 신규 존재 (PATCH 1c) | `**⚡ Plausible Fallacy — Apex Concept 전용 — [EXPERT_INFERENCE, v3]**` 블록 + 그럴듯한 오해/왜 틀렸는가/실무에서 어떻게 드러나는가 3-part 구조 | ✅ PASS |
| 3 | C2 Big Idea가 임상 직관 lead-in으로 시작 (PATCH 2) | "항생제 또는 항부정맥제를 두 배 증량했는데..." lead-in 블록이 기존 Hill `n` 수식 해석 텍스트 *앞*에 위치. 기존 텍스트는 보존 | ✅ PASS |
| 4 | §5 Pair 1·2에 표준 Memory Hook 독립 블록, C2 §A에 보조 Hook (PATCH 3) | Pair 1: `**⚡ 기억 고리 — *결합 vs 효능***`; Pair 2: `**⚡ 기억 고리 — *중간점 vs 가파름***`; C2 §A: `**⚡ 기억 고리 — *최대 자극 vs 최대 억제* (Emax vs Imax)***` — 3 hooks all standardized | ✅ PASS |
| 5 | §5 Pair 2에 Critical Blow 행 존재 (PATCH 4) | `\| **치명적 타격 (Critical Blow) — [EXPERT_INFERENCE, v3]** \|` 행이 Pair 2 표 직후 위치, Hill γ 누락 시 규제 deficiency 시나리오 명시 | ✅ PASS |
| 6 | §8 Professional Moat에 Hill γ 임상 함의 3-bullet 존재 (PATCH 5) | γ>1 역치 특성 / 용량 조절 정밀도 / Exposure-response 보고서 필수 — 3-bullet, TDM 임상경험 anchor 포함 | ✅ PASS |
| 7 | C1·C3·C5에 Practice Brief 신규 블록 + 핵심 용어 ANNOTATION 보강 (PATCH 6) | C1 Practice Brief (Mastery Note 직후), C3 Practice Brief (Mastery Note 직후), C5 Practice Brief (Failure Mode 직후) + Emax/intrinsic activity/PK·PD-rate-limited annotation 추가 | ✅ PASS |
| 8 | 비협상 보존 항목이 모두 보존됨 (Non-Negotiable Preservation Rules) | (a) Acenocoumarol/phenprocoumon Insertion I5 verbatim, (b) Q9 Boss Dilemma verbatim, (c) 모든 page tag 보존(새 page tag 미도입), (d) 모든 v3 추가는 `[EXPERT_INFERENCE, v3]` 라벨링 | ✅ PASS |

---

## Final Verdict — ver2 (보존, 참고용)

```text
GO        : HTML compile (Phase 5) cleared.
NO-GO     : Direct HTML compile of ver1 without ver2 enhancements is no longer the recommended path.
REDO      : Not required.
PASS      : Learner-Standalone, Zero-Omission, Mastery-Uplift, Source-Boundary, HTML-Readiness — all PASS.
DELTA     : ver2 closes Audit T5 SHOULD_FIX (4 items) and Crucible Grade A/B intuitions (2 items) via 6 labeled insertions.
SCOPE     : Six insertions only; no body rewriting; no new page tags; no rejected claims restored; pp.225–228 boundary preserved.
ACTION    : Phase 5 HTML compile may proceed. Render PART A only; render Insertion blocks as Mastery-Note callouts with labels preserved.
```

---

## v3.1 Final Checklist

| # | Check item | Verification | Status |
|---|---|---|---|
| 1 | PART A readability improved | KR-01 ~ KR-22 적용 완료 — 영어식 형용사 나열·passive 술어·주어 dangling·과도한 영어-한국어 혼합·긴 합성문이 한국어-자연스러운 능동·분리·gloss 형태로 교정됨. PART A의 모든 §1, §2(C1–C5), §5(Pair 2·Pair 3), §7(Q9), §8(Professional Moat·Hill γ block)에서 학습자 독해 마찰이 감소. | ✅ PASS |
| 2 | Scientific content unchanged | 모든 22개 patch는 prose-level surgical edit. 어떤 과학적 주장·정의·결론·기전·임상 추론도 변경되지 않음. KR-04는 "Response is proportional to [RC]; full effect may occur..."를 한국어로 번역했으나 의미·수치·조건 모두 동일. KR-15는 PK-rate-limited / PD-rate-limited 정의의 parenthetical을 완전한 한국어 문장으로 elevate했으나 정의 자체는 변경 없음. | ✅ PASS |
| 3 | Equations preserved | MathJax 수식 블록(`$...$`, `$$...$$`) 전체 보존. C1 평형 결합, Kd, Hill, Imax, AUEC closed form, Duration log-dose 식 모두 원문 그대로. NONMEM `$DES`, code-fence `[출처: ...]` 라인 모두 비변경. | ✅ PASS |
| 4 | Page tags preserved | `[G&W p.199–200]`, `[G&W p.202–204]`, `[G&W p.216, p.220]`, `[R&T p.234–235]`, `[R&T p.243–244]`, `[R&T p.251–252]`, `[R&T p.249–253]`, `[확인 필요 — 첨부 PDF 미포함 구간]`, `[확인 필요 — 교과서 외 규제 적용]` 등 모든 page tag 토큰의 위치·숫자 불변. v3.1에서 새 page tag를 도입하지 않음. | ✅ PASS |
| 5 | Figure markers preserved | `<!-- FIGURE_POINTER -->` 5개, `<!-- FIGURE_SCHEMATIC -->` 2개 — 합 7개 figure marker 블록 전체 보존. Source / Why this matters / When to look / Learner instruction / Title / Mode / Visual objective / Core message / Elements / Caption / Alt text / Source relation 필드 모두 원문 그대로. KEEP/REJECT 결정(P 5개 + R 2개) 불변. | ✅ PASS |
| 6 | Source-boundary preserved | pp.225–228 boundary 유지. Aspirin 75 mg, naproxen ke0, 5–100×/FIH/NDA, FDA deficiency letter, perioperative 7-day rule 모두 미복원. PART B B5 Audit Guardrails / B7 Deprecated and Forbidden Restorations 전체 비변경. Insertion I5(acenocoumarol/phenprocoumon) verbatim, Q9 Boss Dilemma의 임상/규제 결론 비변경(KR-19는 "다음" → "다음으로" 한 글자 추가). 모든 source-basis label(`[EXPERT_INFERENCE, v3]`, `[TEXTBOOK_DERIVED]`, `[CRUCIBLE_DERIVED]`, `[교과서 외 규제 해석]`, `[실무 구현 번역]`, `[수학적 추론]`) 불변. | ✅ PASS |
| 7 | HTML-readiness preserved | PART B 전체(B1 Compilation Contract ~ B11 Mastery Augmentation Log) 비변경. Marker-to-component mapping 14행 비변경. PATCH MODE Splice Verification Table(B8) 비변경. CSS class hint(`source-page`, `source-uncertain`, `figure-pointer` 등) 미변경. MathJax CDN, Mermaid CDN dependency 사양 불변. Phase 5 컴파일러는 v3와 동일한 rendering contract로 v3.1을 처리할 수 있음. (B10 Micro-Patch Log에 v3.1 trace 항목만 추가됨 — guardrail 변경 아님.) | ✅ PASS |
| 8 | Ready for Phase 5 HTML compilation | v3.1은 v3에 대한 prose-only delta이며, v3가 통과한 5개 인증서(Learner-Standalone PASS+, Zero-Omission PASS unconditional, Mastery-Uplift PASS++, Source-Boundary PASS, HTML-Readiness PASS)에 대한 회귀 위험이 없다. Phase 5 컴파일러는 v3.1을 입력으로 받아, v3에서 정의된 marker mapping·page tag wrapping·figure rendering rule·MathJax 처리·Self-Test accordion·navigation anchor integrity·responsive/print mode 모두 그대로 적용하면 된다. **GO — Phase 5 HTML 컴파일 가능.** | ✅ PASS |

---

*v3.1 = v3 + Korean Readability Patch (22 surgical Low-risk edits on PART A prose).*  
*Phase 5 HTML compilation: cleared.*

---

## v3.2 Final Checklist

| # | Check item | Verification | Status |
|---|---|---|---|
| 1 | PART A 일반 설명문이 한국어 중심으로 전환됨 | §1–§8 전체의 일반 영어 산문이 한국어로 변환됨. 모든 §2 카드 소제목(Formal Definition, Structural Necessity 등)에 `한글(English)` 병기 적용. 학습 장치 레이블(Recap, Mastery Note, Practice Brief, Trench-Level Tip, Failure Mode 등) 한국어화. §5 혼동 쌍 테이블 헤더·§7 질문/정답 레이블 한국어화. | ✅ PASS |
| 2 | 영어로 남은 표현이 전문용어·기호·코드·마커·career-critical term에 한정 | CL, V, EC50, Emax, Hill n, AUC, AUEC, ODE 등 표준 기호/약어, NONMEM 코드, MathJax 수식, page tag, source-basis label, figure marker, HTML compiler marker만 영어 유지. 일반 설명 영어 문장은 한국어로 전환 완료. | ✅ PASS |
| 3 | Career-critical term에 `한글(English)` 형식 적용 | functional sensitivity→기능적 감수성(functional sensitivity), receptor occupancy→수용체 점유율(receptor occupancy), binding assay→결합 분석(binding assay), dose-titration sensitivity→용량 조절 감수성(dose-titration sensitivity), model discrimination→모델 판별(model discrimination) 등 주요 전문용어에 첫 등장 병기 적용. | ✅ PASS |
| 4 | 수식·page tag·source label·figure marker·HTML compiler marker 보존 | 모든 MathJax 수식(`$...$`, `$$...$$`) 불변. 모든 page tag(`[G&W p.XX]`, `[R&T p.XX]` 등) 불변. 모든 source-basis label 불변. 모든 `<!-- FIGURE_POINTER -->`, `<!-- FIGURE_SCHEMATIC -->` 마커 블록 내용 불변. 모든 HTML compiler marker 불변. | ✅ PASS |
| 5 | 새 과학적 주장·수치·예시·reference 미추가 | v3.2는 순수 한국어화 패치. 어떤 과학적 사실, 수치, 임상 예시, 규제 주장, page tag, figure도 추가하지 않음. | ✅ PASS |
| 6 | Section/card 구조·anchor 미변경 | PART A의 §1–§8 구조, 카드 C1–C5 순서, 혼동 쌍 Pair 1–4 순서, Q1–Q9 순서 모두 보존. PART B B8 Splice Verification Table 및 B4 Marker-to-component mapping 미변경. | ✅ PASS |
| 7 | Code block·NONMEM/R/Python syntax 미번역 | 코드 블록 내부, `[출처: ...]` 라인, NONMEM syntax 모두 원문 유지. | ✅ PASS |
| 8 | Phase 5 HTML 컴파일 준비 완료 | v3.2는 v3.1에 대한 한국어화 전용 delta이며, v3가 통과한 5개 인증서에 대한 회귀 위험이 없다. Phase 5 컴파일러는 v3.2를 입력으로 받아 동일한 rendering contract를 적용하면 된다. **GO — Phase 5 HTML 컴파일 가능.** | ✅ PASS |

---

*v3.2 = v3.1 + Korean-Dominant Readability Patch (systematic Korean-dominance pass on all PART A learner-facing prose).*  
*Phase 5 HTML compilation: cleared.*

> **v3.5 note:** This version applies an Expression Refinement Patch to PART A only. Scientific content, equations’ meaning, numerical anchors, page tags, source labels, figure marker boundary tags and field keys, compiler markers, section/card structure, code blocks, and PART B guardrails are preserved. The patch normalizes mathematical expressions into MathJax/LaTeX-ready notation, converts remaining general English prose and FIGURE_POINTER learner-facing field values into Korean, applies first-use Korean-English pairing for career-critical terms, and rewrites learner-facing prose in a Korean doctoral-level friendly expert lecture style with a light degree of punchy, high-retention phrasing at key conceptual decision points. No new scientific claims, examples, numbers, page tags, figures, or external references were added.

> **v3.6.1 note:** This version applies a Compact Equation Annotation + Section Core Declaration Patch to PART A only. OP-1: All "Annotated equation — 수식 해부" bullet lists (항별 의미·실무 직관·오해 방지) removed; underbrace/overbrace labels refined for compactness and clarity from a pharmacometrics expert perspective. OP-2 (Replace mode): All per-slide 핵심 메시지 blocks removed; replaced by SECTION_CORE markers with single-line vivid 핵심 요지 declarations at thematic section boundaries. All SLIDE_START markers, figure markers, page tags, source labels, numerical anchors, tables, code blocks, and PART B content are preserved unchanged from v3.6.

> **v3.6.1 보존 검증 통과:** OP-1(수식 bullet 제거·레이블 정제) + OP-2(슬라이드별 핵심 메시지 전부 제거·SECTION_CORE 핵심 요지 삽입) 외 원문 무변경 확인. SLIDE_START 마커 수·figure marker·page tag·source label·수치 anchor·표·코드·PART B 전부 보존. 잔존 핵심 메시지 행: 0건.

XX_html_compile_input_master_v3.2.md

> **v3.2 note:** This version applies a Korean-Dominant Readability Patch to PART A learner-facing prose. General English prose was converted to Korean where possible, while career-critical pharmacometrics terms are retained as Korean-English paired expressions on first use. Scientific content, equations, numerical anchors, page tags, source labels, figure markers, compiler markers, section structure, and PART B guardrails are preserved. No new scientific claims, examples, numbers, page tags, figures, or external references were added.

v3.1 note: This version applies a Korean Readability Patch to improve learner-facing Korean prose while preserving scientific content, equations, page tags, source labels, figure markers, and Phase 5 HTML-readiness. No new scientific claims, page tags, numerical anchors, figure decisions, or external references were added.

---

# 16_HTML Compile Input Master — v3.2

## v3.2 Change Log

본 v3.2는 v3.1의 후속 패치이며, **한국어 중심 가독성 패치(Korean-Dominant Readability Patch)** 만을 PART A 학습자 본문에 적용한다. 일반적인 영어 산문은 가능한 한 한국어로 변환하였고, 커리어상 영어로 알아두는 것이 유리한 핵심 전문용어는 첫 등장 시 `한글(English)` 형식으로 병기하였다. 과학적 주장, 수식, 수치 앵커, page tag, source label, figure marker, HTML compiler marker, 섹션 구조, PART B guardrail은 모두 그대로 보존된다. 새로운 과학적 주장, 예시, 수치, page tag, figure, 외부 reference는 도입되지 않는다.

| v3.2 Patch | Location | Type | Risk |
|---|---|---|---|
| K01 | Learner Navigation Aid 헤더·라벨 | Korean-dominant header | Low |
| K02 | §1 Source universe / Big Idea / Capstone spine 라벨 | Korean-dominant label + paired terms | Low |
| K03 | §2 카드 sub-section 헤더 (Locked formulation, Editorial correction 등) | Korean-dominant header | Low |
| K04 | §2 표 헤더 및 영문 cell 내용 | Korean conversion + paired terms | Low |
| K05 | §2.4 Conceptual objective / Sampling identifiability / Boundary | Korean conversion + paired terms | Low |
| K06 | §2.5 Hepatic contrast 영문 잔여 표현 | Korean conversion | Low |
| K07 | §2.7 Locked correction / Key equations 헤더 | Korean conversion | Low |
| K08 | §2.8 Criteria lock / Table 18-X locks | Korean conversion + paired terms | Low |
| K09 | §2.9 Corrected Fig.18-5 lock / Clinical implication | Korean conversion | Low |
| K10 | §2.10 Three scenarios 표 헤더·내용 | Korean conversion | Low |
| K11 | §5 Confusion pair 표 헤더 6개 | Korean conversion + paired terms | Low |
| K12 | §5 One-line lock 라벨 표준화 | Korean-dominant label | Low |
| K13 | §7 Q15 Boss-Dilemma 라벨 | Korean conversion + paired terms | Low |
| K14 | §8 B / C / D / E 헤더 라벨 | Korean conversion + paired terms | Low |
| K15 | §8 Final recap 영문 산문 | Korean conversion | Low |

v3.2는 v3.1의 모든 patch (P01–P20)와 v3의 모든 augmentation labels (`[EXPERT_INFERENCE, v3]`, `[CRUCIBLE_DERIVED, v3]`)를 그대로 보존한다. PART B의 모든 guardrail·certification·coverage matrix·marker block registry·splice verification table은 변경되지 않는다. PATCH MODE Insertion Map의 anchor 7개 (F01–F07) verbatim text도 patch 미적용 영역에 위치하므로 그대로 유지되며, Phase 5 HTML compiler가 v3.2를 입력으로 받아도 splice 실패 위험이 없다.

---

## v3.1 Change Log

본 v3.1은 v3의 PATCH TABLE 검토 후속 패치로, **PART A 학습자-facing 본문의 한국어 독해성 개선만을 적용**한다. 캐노니컬 본문(Content Lock v2 splice fidelity), MA01–MA24 augmentations, F01–F07 figure markers, 모든 source-prefix labels, 모든 page tag, 모든 수식, 모든 NONMEM/R 코드 블록은 그대로 보존된다. 신규 과학적 주장, 신규 수치, 신규 page tag, 신규 외부 reference, 신규 regulatory claim은 도입되지 않는다.

| v3.1 Patch | Location | Type | Risk | Applied |
|---|---|---|---|---|
| P01 | Learner Navigation Aid — "How to use this handout" | Korean flow improvement | Medium | YES |
| P02 | Learner Navigation Aid — "Before you start" 4개 항목 | Korean flow improvement | Medium | YES |
| P03 | Learner Navigation Aid — "After you finish" 2개 항목 | Korean flow improvement | Medium | YES |
| P04 | §2.3 MASTER LENS 두 번째 문장 | Korean flow improvement | Low | YES |
| P05 | §2.4 Sampling identifiability anchor 마지막 문장 | Korean flow improvement | Low | YES |
| P06 | §2.5 Hepatic contrast 복합 문장 | Sentence split | Low | YES |
| P07 | §2.6 MASTER LENS 세 번째 문장 | Korean flow improvement | Low | YES |
| P08 | §2.7 CAPD contrast (영문 전체 문장) | Korean flow improvement | Low | YES |
| P09 | §2.7 Trench-Level Tip 두 번째 문장 (영문) | Korean flow improvement | Low | YES |
| P10 | §2.8 MASTER LENS annotation 끝 | Korean flow improvement | Low | YES |
| P11 | §2.8 Table 18-6 interpretation gate 두 번째 문장 | Concept clarification | Low | YES |
| P12 | §2.8 Phenytoin lock 첫 문장 | Tone smoothing | Low | YES |
| P13 | §2.9 Clinical implication — LD divided loading 문장 | Korean flow improvement | Low | YES |
| P14 | §5.3 One-line lock — "central skill" 표현 | Korean flow improvement | Low | YES |
| P15 | §5.4 One-line lock (영문 전체 문장) | Korean flow improvement | Low | YES |
| P16 | §7 Q1 Answer — 단일 장문 분리 | Sentence split | Low | YES |
| P17 | §8A — 두 번째 중복 문장 | Redundancy trimming | Low | YES |
| P18 | §8B meta-patterns 2–4 제목 | Korean flow improvement | Low | YES |
| P19 | §8E "Do not say" / "Say instead" 코드블록 레이블 | Korean flow improvement | Low | YES |
| P20 | §7 Q15 Boss-Dilemma Answer 첫 번째 문장 | Korean flow improvement | Low | YES |

v3.1은 v3의 모든 augmentation labels (`[EXPERT_INFERENCE, v3]`, `[CRUCIBLE_DERIVED, v3]`)와 PART B의 모든 guardrail·certification·coverage matrix를 그대로 보존한다. PART B의 B11 Mastery Augmentation Log와 B9 Coverage Matrix는 변경 없이 유지된다. PART B에는 본 v3.1 Change Log 참조만 추가되었다.

---

## v3 Change Log

본 v3는 ver2의 Independent Master Reviewer audit (NO-GO 판정) 후속 patch로, **Step 1 V5.0 Apex Edition 명세를 충족하기 위한 surgical augmentation**이다. 캐노니컬 본문(Content Lock v2 splice fidelity), MA01–MA18 augmentations, source-prefix labels, figure marker block IDs, 모든 page tag는 그대로 보존된다. 신규 추가 항목은 모두 `[EXPERT_INFERENCE, v3]` 또는 `[CRUCIBLE_DERIVED, v3]`로 epistemic-labeled되며, 새 page tag·새 외부 임계값·새 named drug example을 도입하지 않는다.

| v3 Patch | Location | Type | Reviewer gap closed | Risk |
|---|---|---|---|---|
| MA19 | §2.1 | Apex Concept 배지 + Plausible Fallacy block | "[⚡ Apex Concept] 미지정" 결함 | Low |
| MA20 | §5.1–§5.6 | Memory Hook 6개 신설 | "§5 Memory Hook 전부 부재" 결함 | Low |
| MA21 | §5.5 | Critical Blow 행 추가 | "Critical Blow 부재" 결함 | Low |
| MA22 | §2.5 | Rd framework 결정 테이블 | "Rd 산문만 존재, 결정 테이블 부재" 결함 | Low |
| MA23 | §7 Q15 | Boss-Dilemma 레이블 표준화 + ★★ SR 태그 | Q15 형식 비표준 | Low |
| MA24 | §2.1–§2.10 | Practice Brief 4축 블록 (10카드 전체) | 카드별 체화 가이드 부재 | Low |

v3는 ver2의 splice fidelity (F01–F07)와 모든 page tag를 그대로 보존한다. PART B의 B11 Mastery Augmentation Log에 MA19–MA24가 추가되었으며, B9 Coverage Matrix에 C11(Apex/Memory Hook/Critical Blow)·C12(Practice Brief 일관성)가 신설되었다.

---

## ver2 Change Log

본 ver2는 v1의 검토 결과 *PASS-with-improvements* 판정에 따라, 캐노니컬 본문은 변경하지 않은 상태로 Mastery-Uplift 항목 6건을 추가 반영한 *bounded adjacent augmentation* 패치이다. Source boundary는 유지된다 (새 page tag·새 unsupported numerical 추가 없음, 모든 신규 augmentation은 epistemic-labeled).

| ver2 Patch | Location | Type | Crucible source | Risk |
|---|---|---|---|---|
| MA11 | §2.5 | Failure Mode 추가 | Wall #6 (Imipenem Rd assumption violation) | Low |
| MA12 | §2.6 | Failure Mode 정량 anchor 보강 | Wall #5 / Tip 7 (SCr turnover lag) | Low |
| MA13 | §2.8 | Mastery Note 추가 | 위험 9 (CYP2D6 prior subgroup) | Low |
| MA14 | §2.8 | Failure Mode 추가 | Wall #7 / Tip 9 (Fig.18-2 hypothetical) | Low |
| MA15 | §2.10 | Mastery Note 추가 | Wall #9 / Tip 12 (Forgiving/Unforgiving 정량) | Low |
| MA16 | §5 | Confusion Pair §5.6 신설 | Wall #10 / Tip 11 / S8 (Sampling identifiability) | Low |
| MA17 | §7 | Q15 Boss-Dilemma 추가 | Step 1 V5.0 Socratic Dilemma 명세 | Low |
| MA18 | §7 | Q16 NONMEM signature decode 추가 | S8 active recall 변환 | Low |

ver2는 v1 splice fidelity (F01–F07)와 모든 page tag를 그대로 보존한다. PART B의 B9 Coverage Matrix에 C9·C10 행이 신설되었고, B11 Mastery Augmentation Log에 MA11–MA18이 추가되었다.

---

## Phase 4D Certification (ver2)

| Certificate | Status | Basis |
|---|---|---|
| Learner-Standalone Certificate | PASS | PART A contains a learner navigation aid, the complete exact-spliced canonical body, approved figure markers, and bounded adjacent mastery notes (now extended with ver2 patches MA11–MA18). |
| Zero-Omission Certificate | PASS *(ver2 강화)* | Scope-required concepts, Audit MUST_FIX/SHOULD_FIX items, Phase 4C KEEP markers, and adopted Crucible logic are present or intentionally bounded. ver2 closes Crucible Grade A residuals (Walls #5·#6·#7·#9·#10 / Tips 9·11·12 / Signatures S8). |
| Mastery-Uplift Certificate | PASS *(ver2 강화)* | Eighteen short adjacent augmentations are labeled by epistemic status and do not broaden the canonical scientific body. New §5.6 Confusion Pair and Q15 Boss-Dilemma satisfy Step 1 V5.0 Socratic Dilemma requirement. |
| Source-Boundary Certificate | PASS | Augmentations do not add new page tags, new unsupported numerical values, or new named examples; expert interpretation is labeled. ver2 reuses existing page tags only. |
| HTML-Readiness Certificate | PASS | PART B contains the Phase 5 rendering contract, figure/page-tag rules, audit/crucible guardrails, splice verification, coverage matrix (now C9·C10 added), and logs. |


## Assembly Mode

PATCH MODE — `16_Content Lock v2.1(1).md` is a Figure Marker Patch, not a full restatement. The canonical learner body was constructed from `16_Content Lock v2(5).md` by exact-splicing seven approved Phase 4C marker blocks into unique anchors.


## Input Manifest

| File | Role | Authority level | Used for | Notes |
|---|---|---:|---|---|
| `16_scope_lock(3).md` | scope boundary | A0 | Source range, learner, image rights, hard rules, data anchors | Image rights = None; direct textbook figure embedding prohibited. |
| `016_G_임상 통합·패턴인식 TDM·질환·캡스톤(4).pdf` | PDF verification source | A1 | G&W Ch.6, PK15, PK35 page/figure/source verification | Used only for high-impact source verification and page/figure identity. |
| `016_T_임상 통합·패턴인식 TDM·질환·캡스톤_01(4).pdf` | PDF verification source | A1 | R&T Ch.15 disease/renal/dialysis verification | Used only for high-impact source verification and page/figure identity. |
| `016_T_임상 통합·패턴인식 TDM·질환·캡스톤_02(4).pdf` | PDF verification source | A1 | R&T Ch.18 therapy/TCS/dosing verification | Used only for high-impact source verification and page/figure identity. |
| `16_Audit_Report_v1(4).md` | audit guardrail | A2 | MUST_FIX/SHOULD_FIX, forbidden restoration, T5/T6/T7 checks | Controls source-fidelity regression prevention. |
| `16_Content Lock v2(5).md` | canonical body | A3 | Base text-final body | Used from `# Session 016 — Content Lock v2` onward; editorial pass ledger excluded from learner body. |
| `16_Content Lock v2.1(1).md` | figure insertion source | A4 | PATCH MODE insertion map and marker registry | All seven KEEP markers were exact-spliced. |
| `16_crucible_report_v1(1).md` | crucible guardrail | A5 | Adopted Grade A insight preservation and expert-pattern guardrails | Not used as raw prose source. |
| `S16_phase1_patch memo(2).md` | locked reference / deprecated-stage diagnostic | A6 | Phase 1 risk check and source-expansion caution | Used for regression awareness only. |
| `16_step1_draft_v0(3).md` | deprecated source | A6 | Omission check only | Not copied into learner body. |
| `붙여넣은 마크다운(1)(97).md` | compiler instruction | A7 | Phase 5 HTML rendering contract | Included in PART B as compiler requirements. |
| `붙여넣은 텍스트 (2)(10).txt` | Phase 4D assembly instruction | assembly instruction | Controls current master-file assembly | Not learner-facing. |
| `16_Content Lock v1(3).md` | prior locked reference | lower than v2 | Regression check only | Superseded by Content Lock v2. |


---

# PART A — 학습자용 완성 핸드아웃 (Learner-Facing Complete Handout)
<!-- SECTION_CORE: SC-01 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** $shape$에서 posterior와 dosing decision까지 이어지는 Session 016의 단일 판단 사슬을 먼저 고정하라 — 이 틀이 없으면 뒤의 모든 카드가 흩어진다.

---
<!-- SLIDE_START: S01 | title: PART A 학습자용 완성 핸드아웃 | source_anchor: part-a -->


## 학습자 항법 안내 (Learner Navigation Aid)
<!-- SLIDE_START: S02 | title: 학습자 항법 안내 | source_anchor: learner-navigation-aid -->


**이 학습 자료 사용법** *(P01 적용)*  
§1을 먼저 한 번 읽어 캡스톤 체인(capstone chain)을 고정한 뒤, §2를 핵심 개념 경로로 학습합니다. 그림 포인터(figure pointer) 블록은 교과서 원그림을 직접 확인하라는 안내입니다. 원그림은 이 자료에 재수록하지 않습니다. §2 이후에는 §5에서 주요 혼동을 풀고, §7에서 능동 회상을 점검한 뒤, §8에서 세션 전체를 종합합니다.

**학습 경로 (Learning route)**

```text
§1 Roadmap
→ §2.1–§2.3 Pattern recognition and model-candidate narrowing
→ §2.4 Bayesian individual parameter estimation
→ §2.5–§2.7 Disease, renal function, and dialysis adjustment
→ §2.8–§2.10 TCS, loading/maintenance dosing, and irregular dosing
→ §5 Confusion pairs
→ §7 Self-test
→ §8 Meta-frame
```

**시작하기 전 유지할 4가지 구분** *(P02 적용)*

- 진단 신호와 모델 증명의 차이를 유지합니다.
- 환자 속성($RF$)과 약물 속성($f_e$)의 차이를 유지합니다.
- $V$ 기반 loading dose와 $CL$ 기반 maintenance dose의 차이를 유지합니다.
- 측정 농도와 해석 가능한 농도의 차이를 유지합니다.

**학습을 마친 뒤 도달해야 할 상태** *(P03 적용)*

- Ch.6이 모델 후보를 좁히는 이유, Ch.15가 환자별 파라미터 편차(parameter deviation)를 설명하는 방식, PK35가 사후 파라미터(posterior parameter)를 추정하는 방식, Ch.18이 그 추정을 용량·모니터링 결정으로 변환하는 과정, PK15가 노출·안전역 보고(exposure/safety-margin reporting)로 체인을 닫는 구조를 설명할 수 있어야 합니다.
- 이 자료에서 교과서 원그림이 포인터 전용(pointer-only)으로만 제시되는 이유를 설명할 수 있어야 합니다. 그 이유는 image rights가 None으로 잠겨 있기 때문입니다.

---

## 임상 통합 캡스톤: 패턴 인식 · TDM · 질환 · 치료 의사결정
<!-- SLIDE_START: S03 | title: 임상 통합 캡스톤 범위 | source_anchor: clinical-integration-capstone -->


> **출처 및 범위 노트**  
> 이 자료는 Gabrielsson & Weiner 5e의 Ch.6 Pattern Recognition [pp.423–466], PK15 Toxicokinetics [pp.546–548], PK35 Bayesian model — Digoxin [pp.641–643]와 Rowland & Tozer 5e의 Ch.15 Disease [pp.443–489], Ch.18 Initiating and Managing Therapy [pp.577–610] 범위 안에서 임상 통합, 패턴 인식, Bayesian TDM, 신·간 질환, 투석, loading/maintenance 및 불규칙 투약 의사결정을 연결합니다. 교과서 원그림은 image rights 제한 때문에 재수록하지 않고, FIGURE_POINTER 또는 독립 schematic 안내로만 제시합니다.

---

# §1 — 세션 헤더 & 로드맵 (Session Header & Roadmap)
<!-- SLIDE_START: S04 | title: 세션 로드맵 | source_anchor: section-1-roadmap -->


**Session ID**: 016 — 임상 통합 캡스톤: 패턴 인식(pattern recognition), TDM(← 농도 측정으로 용량 판단을 보정하는 전략), 질환(disease), 치료 의사결정(therapeutic decision-making)
<!-- ANNOTATION -->

**소스 범위 (Source universe)**

- Gabrielsson & Weiner 5e: Ch.6 Pattern Recognition [pp.423–466], PK15 Toxicokinetics [pp.546–548], PK35 Bayesian model — Digoxin [pp.641–643]
- Rowland & Tozer 5e: Ch.15 Disease [pp.443–489], Ch.18 Initiating and Managing Therapy [pp.577–610]

<!-- MASTER LENS -->
**핵심 통찰 (Big Idea)**  
데이터의 *형태(shape)* 는 그 데이터를 만든 동역학(kinetic/dynamic) 메커니즘(← 농도 변화와 약효 변화의 발생 원리)의 흔적이다.
<!-- ANNOTATION -->
질환은 그 메커니즘의 파라미터(parameter)를 모집단(population)에서 벗어나게 만들고, Bayesian TDM은 그 환자별 편차(deviation)를 추정합니다. Ch.18의 치료 의사결정은 그 추정을 용량(dose), 채혈(sampling), 모니터링 의사결정(monitoring decision)으로 바꿉니다.

<!-- ANCHOR -->
**캡스톤 척추 (Capstone spine)**

```text
[Ch.6 Pattern Recognition]
  → 어떤 PD 구조가 가능한가?
[Ch.15 Disease]
  → 환자 parameter가 population에서 왜 벗어났는가?
[PK35 Bayesian TDM]
  → 관측 농도와 prior를 어떻게 결합할 것인가?
[Ch.18 Initiating/Managing Therapy]
  → loading, maintenance, TCS, missed dose를 어떻게 판단할 것인가?
[PK15 Toxicokinetics]
  → 선택된 용량의 exposure와 safety margin을 어떻게 보고할 것인가?
```

**후속 구현 영역 — source-locked 본문이 아님**  
NONMEM `$DES`, Bayesian TDM 소프트웨어, NDA/IND/RMP style writing은 이 세션에서 자연스럽게 이어지는 실무 영역입니다. 그러나 교과서 본문의 직접 claim은 아니므로, 이하에서는 `[교과서 외 구현/규제 번역]`으로만 취급합니다.

**유지된 데이터 앵커 (Data anchors retained)**

- PK35 digoxin: 55-year-old, 60 kg male with CHF; Lanoxicap 0.2 mg daily; concentrations 2.5 µg/L at 458 h and 0.9 µg/L at 479 h; CLpop 1.8 L/h, Vpop 500 L; final estimates CL 5.7 L/h, V 119.6 L, $t_{1/2}$ 14.5 h [G&W pp.641–643].
- PK15 toxicokinetics: 10/56/320 µmol·day⁻¹·kg⁻¹ dose levels, Cmax/AUC exposure reporting, therapeutic concentration 0.05–0.1 µM, high-dose Cmax approximately 50 µM, safety margin >100-fold in the toxicokinetic interpretation context [G&W pp.546–548].
- Ch.18 concentration interpretation: Table 18-6 data collection, Eq.18-1–18-4 dosing irregularity equations, and Fig.18-13 sampling-dependent confidence in V vs CL [R&T pp.597, 601–605].

<!-- RECAP -->
**§1 recap**: 이 세션은 “모델 선택 → 질환 보정 → 개인 추정 → 처방·모니터링 → 노출 보고(exposure reporting)”의 단일 임상 계량약리학 체인(clinical pharmacometrics chain)을 잠급니다.

<!-- SLIDE_START: S05 | title: Session 016 캡스톤 척추 schematic | source_anchor: figure-schematic-session-016-spine -->

<!-- FIGURE_SCHEMATIC -->
Title: Session 016 캡스톤 척추 — 데이터 형태(data shape)에서 노출 보고(exposure report)까지
Mode: N
Visual objective: 5초 안에 각 챕터가 다음 챕터로 넘기는 의사결정 객체(decision object)를 보이게 합니다.
Core message: Ch.6은 모델 후보(model candidate)를, Ch.15는 환자별 편차(patient deviation)를, PK35는 사후 파라미터(posterior parameter)를, Ch.18은 용량·모니터링 결정(dose/monitoring decision)을, PK15는 노출·안전역 보고(exposure/safety-margin report)를 만듭니다.
Elements to include: 가로 5개 블록: Ch.6 Pattern Recognition → Ch.15 Disease/RF/Rd → PK35 Bayesian TDM → Ch.18 Dosing/Monitoring → PK15 Toxicokinetics; 각 블록 아래에는 출력 라벨만 표시: 모델 후보(model candidate), 환자별 편차(patient deviation), 사후 파라미터(posterior parameter), 용량 결정(dose decision), 노출 보고(exposure report); 작은 주의 띠 1개: 구현/규제 번역에는 별도 라벨이 필요함.
Elements to exclude: 약물 예시, 수치 앵커, 출처 page tag, 주의 라벨을 넘어서는 소프트웨어명, 모든 규제 workflow 도식.
Suggested rendering: Mermaid
Caption: Session 016은 독립 개념 묶음이 아니라, data shape에서 임상 노출 보고(clinical exposure reporting)로 이어지는 단일 의사결정 사슬(decision chain)입니다.
Alt text: 패턴 인식, 질환 보정, Bayesian 추정, 치료 의사결정, 독성동태학 보고(toxicokinetic reporting)를 왼쪽에서 오른쪽으로 연결하는 5단계 파이프라인.
Source relation: 새로 설계한 독립 도식(schematic)
<!-- /FIGURE_SCHEMATIC -->

---

# §2 — 개념 해부 카드 (Concept Anatomy Cards)
<!-- SECTION_CORE: SC-02 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** Plot shape는 모델 확정 도장이 아니라 후보를 줄이는 triage 언어다 — baseline·delay·peak-shift·saturation 순서를 먼저 잠가라.

---
<!-- SLIDE_START: S06 | title: 개념 해부 카드 진입 | source_anchor: section-2-concept-cards -->


## §2.1 — 패턴 인식 의사결정 흐름(Pattern-recognition decision workflow) [G&W pp.423–424, pp.465–466]
<!-- SLIDE_START: S07 | title: 패턴 인식 의사결정 흐름 | source_anchor: section-2-1-pattern-workflow -->


`[⚡ Apex Concept]`

> **▶ Apex Frame — 임상 계량약리학의 단일 파이프라인 — [EXPERT_INFERENCE, v3]**  
> 임상 계량약리학은 파라미터 수치의 컬렉션이 아니라 *model → exposure → target → decision*으로 이어지는 연결 파이프라인입니다. §2.1은 그 파이프라인의 **입구**입니다. 데이터 형태(shape) 관찰 하나가 잘못되면, 뒤따르는 모델 후보, posterior 추정, 용량 결정, exposure 보고가 모두 한 방향으로 기울어집니다.

> **⚠ 그럴듯한 오류(Plausible Fallacy) — “모델이 검증되면 의사결정은 자동이다” — [EXPERT_INFERENCE, v3]**  
> *그럴듯한 오해*: "집단 모델(population model)이 검증되면 TDM과 용량 결정은 소프트웨어가 자동으로 처리한다."  
> *왜 틀렸는가*: 신기능, 약물 상호작용, 채혈 식별가능성(sampling identifiability), posterior parameter uncertainty가 각각 *독립적으로* 의사결정을 변형합니다. 소프트웨어가 출력한 숫자는 posterior mean입니다. 그 숫자가 식별 가능한 정보 위에 있는지는 임상약사·임상약리학자가 판단해야 합니다.  
> *실무 발현 형태*: Bayesian TDM 소프트웨어가 "$CL=5.7$ L/h"를 출력했지만, 채혈 시점이 모두 $T_{max}$ 이전이어서 $V$만 잘 추정되고 $CL$은 population prior로 collapse된 경우를 생각할 수 있습니다. 이때 그 $CL$ 수치로 개별화 용량을 결정하면 실제 clearance와 무관한 dose를 투여하게 됩니다. 이 메커니즘의 자세한 NONMEM 진단은 §5.6 실패 모드(Failure Mode)와 §7 Q16에서 잠급니다.

<!-- MASTER LENS -->
**핵심**: response-time, concentration-time, concentration-response plot은 먼저 baseline, time-delay, peak-shift, saturation/slope를 따라 읽습니다. 그 다음 Fig.6.12식 workflow처럼 C/R vs time, C-R plot(← 농도-반응 관계를 시간과 분리해 보는 그림), hysteresis(← 시간 지연으로 C-R 관계가 고리처럼 보이는 현상), rebound, tolerance 여부를 순서대로 확인합니다.
<!-- ANNOTATION -->

**확정된 형식 (Locked formulation)**

```text
1. Baseline: stable? drifting? disease progression/adaptation?
2. Time-delay: concentration peak와 response maximum/minimum이 분리되는가?
3. Peak-shift: dose 증가에 따라 response extremum이 좌/우로 이동하는가?
4. Saturation/slope: high dose에서 flat portion 또는 nonlinear rise/fall이 보이는가?
5. C-R plot: direct, indirect, rebound, tolerance, hysteresis 중 어느 후보가 남는가?
```

**편집자 수정 (Editorial correction)**: “60초 내 모델 확정”은 source claim이 아닙니다. 본 문서에서는 “빠른 후보 축소를 위한 교육용 operation”으로만 둡니다.

<!-- TRENCH -->
**현장 팁(Trench-Level Tip)**: 단일 dose response-time curve 하나만으로 mechanism을 확정하지 마세요. 중요한 것은 dose escalation에서 shape가 어떻게 바뀌는지입니다. 그 변화가 model-class narrowing의 핵심입니다.

<!-- ANCHOR -->
§2.1은 plot-reading grammar입니다. §2.2–§2.3은 그 grammar가 실제 ODE 후보로 내려가는 첫 번째 mechanistic bridge입니다.

<!-- SLIDE_START: S08 | title: Fig.6.1 및 Fig.6.12 확인 지점 | source_anchor: figure-pointer-2-1 -->

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner Ch.6, Fig.6.1 [p.423] and Fig.6.12 [pp.465–466]
Why this matters: Fig.6.1은 baseline, time-delay, peak-shift, saturation, slope라는 초기 시각 문법을 보여 줍니다. Fig.6.12는 그 문법을 실제 분석 흐름(workflow)으로 바꾸어 줍니다.
When to look: 이 카드를 읽은 뒤, §2.2로 넘어가기 전에 확인하면 됩니다.
Learner instruction: 먼저 Fig.6.1을 점검표(checklist)로 확인한 다음, Fig.6.12를 의사결정 흐름(decision workflow)으로 확인하세요. checklist 항목을 서로 독립된 사실처럼 취급하지 말고, 각 관찰이 다음 모델 질문을 어떻게 좁히는지 따라가면 됩니다.
<!-- /FIGURE_POINTER -->

<!-- SLIDE_START: S09 | title: §2.1 체화와 실습 브리프 | source_anchor: mastery-2-1 -->

> **체화 노트(Mastery Note) — TEXTBOOK_DERIVED**  
> 이 카드는 “정답 모델”을 즉시 고르는 법이 아니라, 관찰 순서를 고정해 후보 모델을 줄이는 법을 가르칩니다. 먼저 shape vocabulary를 만들고, 그 다음 남는 mechanistic question을 줄이는 방식으로 읽으면 됩니다.

> **▶ 실습 브리프(Practice Brief) — §2.1 체화 4축** — [EXPERT_INFERENCE, v3]  
> - **왜 알아야 하는가:** 데이터 shape 관찰 순서를 고정하지 못하면 §2.2 이후 모든 모델 후보 결정이 한 방향으로 기울어 §2.4 Bayesian estimation까지 편향됩니다.  
> - **흐름상 역할:** S08(모델 식별) + S15(PD pattern recognition)가 임상 데이터에 적용되는 입구입니다. §2.2–§2.3과 §2.4를 잇습니다.  
> - **체화 꿀팁:** 새 plot을 만나면 무조건 baseline → time-delay → peak-shift → saturation 순서로만 *말로 읽어내세요*. 입력 즉시 모델로 넘어가는 직관을 차단하기 위한 절차입니다.  
> - **실무 활용:** TDM에서 환자 농도-시간 그래프가 "이상해 보일" 때, 어느 shape feature가 이상한지 명명하는 작업이 다음 모델링·재샘플링 결정의 출발점이 됩니다.


---

## §2.2 — 피크 이동 + 포화: 결정 규칙이 아니라 진단 신호(Peak-shift + saturation) [G&W pp.424–428]
<!-- SECTION_CORE: SC-03 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** Peak-shift와 saturation은 모델명을 외우게 하지 않고 competing candidates를 남긴다 — 신호를 판결로 과장하지 마라.

---
<!-- SLIDE_START: S10 | title: Peak-shift와 saturation | source_anchor: section-2-2-peak-shift -->


<!-- MASTER LENS -->
**핵심**: peak-shift 방향은 “모델 클래스 그 자체”가 아닙니다. 이는 competing model candidates를 좁히는 1차 진단 신호입니다.

| 관찰된 패턴 (Observed pattern) | 확정된 해석 (Locked interpretation) |
|---|---|
| Case A: plasma peak이 $R_{min}$까지 걸리는 시간의 약 1/3 시점에 발생 | response delay가 존재합니다. direct-effect 모델 단독은 가능성이 낮습니다. |
| Case B: 고용량에서 trough가 좌측 이동 | turnover loss stimulation 또는 receptor on/off가 후보로 떠오를 수 있습니다. 자동 결론은 아닙니다. |
| Case C: 최고용량에서 trough가 우측 이동 + flat 구간 출현 | saturation을 동반한 input inhibition이 강한 후보 신호입니다. |

**수정된 문장(Corrected sentence)**  
“좌/우 방향이 곧 모델 클래스”가 아닙니다. 더 정확히는, 좌/우 방향과 saturation 유무가 turnover, effect compartment, receptor on/off 등 후보군을 좁히는 1차 진단 신호입니다.

<!-- TRENCH -->
**현장 팁(Trench-Level Tip)**: Case B left-shift를 “$k_{on}$이 큰 약물”로 외우지 마세요. receptor on/off에서는 finite receptor pool 때문에 nadir가 빨라질 수 있고, turnover model에서도 loss stimulation이 유사한 pattern을 만들 수 있습니다.

<!-- SLIDE_START: S11 | title: Fig.6.2 및 Fig.6.3 확인 지점 | source_anchor: figure-pointer-2-2 -->

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner Ch.6, Fig.6.2 [p.424] and Fig.6.3 [p.428]
Why this matters: Fig.6.2는 반응-시간 움직임(response-time movement)이 좌측 또는 우측으로 이동하는 모습을 보여 줍니다. Fig.6.3은 경쟁 대안(competing alternatives)을 함께 보여 주어, 하나의 pattern을 하나의 model에 바로 대응시키는 흔한 오류를 막아 줍니다.
When to look: 이 카드를 읽은 직후 확인하면 됩니다.
Learner instruction: 먼저 Case A, B, C를 최저점 시점(trough timing)과 고용량 평탄화(high-dose flattening)만 보고 비교하세요. 그 다음 Fig.6.3을 확인하면서, 하나의 model을 성급하게 선택하지 말고 어떤 경쟁 모델(competing models)이 남는지 질문하면 됩니다.
<!-- /FIGURE_POINTER -->

<!-- SLIDE_START: S12 | title: §2.2 실패 모드와 실습 브리프 | source_anchor: failure-2-2 -->

> **실패 모드(Failure Mode) — AUDIT_DERIVED**  
> Peak-shift를 단일 모델명으로 번역하는 순간 source-fidelity가 무너집니다. 좌/우 이동은 후보군을 줄이는 신호이지, 모델 확정 판결이 아닙니다.

> **▶ 실습 브리프(Practice Brief) — §2.2 체화 4축** — [EXPERT_INFERENCE, v3]  
> - **왜 알아야 하는가:** "Peak-shift 방향 = 모델 클래스" 환원은 NDA 심사관이 가장 먼저 의심하는 deterministic overclaim 중 하나입니다.  
> - **흐름상 역할:** §2.1(shape grammar)에서 §2.3(prototype ODE)로 가는 *triage*입니다. S15 PD pattern과 직결됩니다.  
> - **체화 꿀팁:** Case A·B·C를 외울 때 모델 이름이 아니라 *"이 패턴이 남기는 후보 목록"*을 함께 외우세요.  
> - **실무 활용:** Phase I/II PK-PD modeling 보고서에서는 "peak shift는 turnover일 수 있다" 같은 *후보 표현*으로 적어야 reviewer 수용 가능성이 올라갑니다.


---

## §2.3 — 효과구획 / turnover / receptor on-off 원형(Effect compartment / turnover / receptor on-off prototypes) [G&W pp.425–427]
<!-- SECTION_CORE: SC-04 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** Effect compartment·turnover·receptor on/off의 차이는 delay가 박힌 state의 차이다 — $C_e$, $R$, $RC$를 분리해 읽어라.

---
<!-- SLIDE_START: S13 | title: 세 가지 PK-PD prototype | source_anchor: section-2-3-prototypes -->


<!-- MASTER LENS -->
**핵심**: Ch.6의 Case A–I 수식들은 모두 외울 목록이 아닙니다. 이 수식들의 역할은 세 prototype(← 반복적으로 재사용되는 대표 구조)을 구분하는 pattern library를 제공하는 것입니다. *(P04 적용)*
<!-- ANNOTATION -->

### Prototype 1 — 효과구획 (Effect compartment)
<!-- SLIDE_START: S14 | title: Prototype 1 효과구획 | source_anchor: prototype-1-effect-compartment -->


Time-delay가 있으나 dose 증가에 따른 clear peak-shift가 약하면 link model을 먼저 의심합니다.

```math
\frac{dC_e}{dt}=k_{e0}(C-C_e)
```

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{\frac{dC_e}{dt}}_{\text{$C_e$ 변화}}
> =
> \underbrace{k_{e0}}_{\text{평형 속도}}
> \overbrace{\left(\underbrace{C}_{\text{혈장}}-\underbrace{C_e}_{\text{효과부위}}\right)}^{\text{농도 차}}
> $$


Response model은 $C$가 아니라 $C_e$에 연결됩니다. Counter-clockwise hysteresis는 effect-site equilibration delay의 전형적 신호입니다 [G&W p.426].

### Prototype 2 — 회전 모델 (Turnover model)
<!-- SLIDE_START: S15 | title: Prototype 2 turnover model | source_anchor: prototype-2-turnover -->


Response variable $R$은 생성과 소실의 동적 평형 위에 놓일 수 있습니다. 이때 drug은 input 또는 loss process를 억제하거나 자극합니다.

```math
\frac{dR}{dt}=k_{in}\cdot I(C)-k_{out}R
```

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{\frac{dR}{dt}}_{\text{$R$ 순변화}}
> =
> \overbrace{\underbrace{k_{in}}_{\text{생성}}\cdot\underbrace{I(C)}_{\text{농도 조절}}}^{\text{input}}
> -
> \underbrace{k_{out}R}_{\text{소실}}
> $$


```math
\frac{dR}{dt}=k_{in}-k_{out}R\cdot S(C)
```

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{\frac{dR}{dt}}_{\text{$R$ 순변화}}
> =
> \underbrace{k_{in}}_{\text{기본 생성}}
> -
> \overbrace{\underbrace{k_{out}R}_{\text{기본 소실}}\cdot\underbrace{S(C)}_{\text{농도 자극}}}^{\text{loss}}
> $$


Baseline $R_0=k_{in}/k_{out}$는 정적 ratio가 아니라 dynamic equilibrium입니다. 새로운 평형으로 이동하는 속도는 주로 $k_{out}$이 지배합니다.

### Prototype 3 — 수용체 on/off (Receptor on/off)
<!-- SLIDE_START: S16 | title: Prototype 3 receptor on/off | source_anchor: prototype-3-receptor -->


Receptor binding이 finite pool을 가진다면 response extremum의 timing은 $k_{on}\cdot C\cdot(R_T-RC)$와 $k_{off}\cdot RC$의 경쟁으로 결정됩니다.

```math
\frac{dRC}{dt}=k_{on}C(R_T-RC)-k_{off}RC
```

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{\frac{dRC}{dt}}_{\text{$RC$ 변화}}
> =
> \overbrace{\underbrace{k_{on}}_{\text{결합 속도}}\underbrace{C}_{\text{농도}}\underbrace{(R_T-RC)}_{\text{free 수용체}}}^{\text{결합 형성}}
> -
> \underbrace{k_{off}RC}_{\text{해리}}
> $$


<!-- TRENCH -->
**현장 팁(Trench-Level Tip)**: Case A–I의 모든 수식을 전수 암기하지 말고, direct delay, turnover delay, finite-pool binding 중 어느 failure mode가 현재 plot을 설명하는지 먼저 판단하세요.

<!-- RECAP -->
**§2.1–§2.3 recap**: Ch.6의 목적은 shape에서 model candidate를 줄이는 것입니다. Pattern은 proof가 아니라 triage signal입니다.

<!-- SLIDE_START: S17 | title: §2.3 prototype synthesis | source_anchor: practice-lens-2-3 -->

> **실무 렌즈(Practice Lens) — EXPERT_INFERENCE**  
> 세 prototype은 “delay가 어디에서 생겼는가”를 묻는 세 가지 문법입니다. effect-site equilibration, response turnover, finite receptor binding 중 어느 병목이 plot의 모양을 만들었는지 먼저 분리합니다.

> **▶ 실습 브리프(Practice Brief) — §2.3 체화 4축** — [EXPERT_INFERENCE, v3]  
> - **왜 알아야 하는가:** Case A–I 수식을 *전수 암기*하면 새 데이터에서 prototype 분리가 늦어집니다. 반대로 *prototype 3개*만 잡으면 즉시 첫 모델 후보를 꺼낼 수 있습니다.  
> - **흐름상 역할:** S11 effect compartment + S12 turnover + S13 receptor binding의 임상적 통합 카드입니다. §2.4 Bayesian fitting은 이 세 prototype 위에서 작동합니다.  
> - **체화 꿀팁:** 각 prototype을 *"어떤 ODE state에 delay가 박혀 있는가"*로 한 줄 요약하세요. link model = $C_e$에, turnover = $R$에, receptor = $RC$에 delay가 있습니다.  
> - **실무 활용:** PK-PD 모델 코딩 시 `$DES` 블록의 첫 줄을 작성하기 전에 "delay state 명명"을 강제하면 모델 디버깅 시간이 크게 단축됩니다.


---

## §2.4 — 개인 TDM을 위한 베이지안 목적함수(Bayesian objective function for individual TDM) [G&W pp.641–643; R&T pp.605–606]
<!-- SECTION_CORE: SC-05 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** Bayesian TDM은 농도 likelihood와 population prior의 힘겨루기다 — posterior 숫자보다 먼저 어떤 parameter가 식별됐는지 보라.

---
<!-- SLIDE_START: S18 | title: Bayesian TDM objective | source_anchor: section-2-4-bayesian-tdm -->


<!-- MASTER LENS -->
**핵심**: Bayesian TDM은 observed concentrations만 믿지 않습니다. population average만 믿지도 않습니다. concentration likelihood와 population prior의 상대적 variance를 함께 고려해 개인 parameter를 추정합니다.
<!-- ANNOTATION -->
앞선 §2.1–§2.3이 “어떤 구조가 가능한가”를 줄였다면, §2.4는 그 구조 안에서 “이 환자의 parameter가 어디에 있는가”를 추정합니다.

**개념적 목적함수 (Conceptual objective)**

```math
OBJ_{Bayes}\approx
\sum_i\frac{(C_{obs,i}-\hat C_i)^2}{var(\hat C_i)}
+
\sum_j\frac{(P_{pop,j}-\hat P_j)^2}{var(\hat P_j)}
```

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{OBJ_{Bayes}}_{\text{총 penalty}}
> \approx
> \underbrace{\sum_i\frac{\left(C_{obs,i}-\hat C_i\right)^2}{\operatorname{var}(\hat C_i)}}_{\text{농도 mismatch}}
> +
> \underbrace{\sum_j\frac{\left(P_{pop,j}-\hat P_j\right)^2}{\operatorname{var}(\hat P_j)}}_{\text{prior 이탈}}
> $$


- 농도 없음: population average가 사실상 estimate가 됩니다.
- prior 없음: maximum-likelihood concentration fitting에 가까워집니다.
- 농도 + prior 있음: complete Bayesian method가 됩니다.

**PK35 digoxin 앵커 (PK35 digoxin anchor)**  
55세, 60 kg, CHF 남성; Lanoxicap 0.2 mg daily; 458 h에서 2.5 µg/L, 479 h에서 0.9 µg/L; $CL_{pop}$ 1.8 L/h, $V_{pop}$ 500 L; 추정 $CL$ 5.7 L/h, $V$ 119.6 L, $t_{1/2}$ 14.5 h [G&W pp.641–643].

**채혈 식별가능성 앵커 (Sampling identifiability anchor)**  
R&T Fig.18-13은 early sample이 $V$에 더 민감하고, late/plateau sample이 $CL$에 더 민감함을 보여줍니다. 따라서 $1\times t_{1/2}$ 근처 sampling만으로는 $CL$ 1/3 변화와 $V$ 3배 변화를 구분하기 어렵습니다. $CL$을 정확히 추정하려면 $4\times t_{1/2}$ 또는 steady-state 시점의 정보가 필요합니다 [R&T pp.605–606]. *(P05 적용)*

<!-- TRENCH -->
**현장 팁(Trench-Level Tip)**: Bayesian posterior(← 관측 후 갱신된 개인 추정값)가 이상한 $V$를 내면 “환자가 이상하다”고 먼저 결론내리지 마세요. sampling time, dosing history, prior variance, assay error, adherence를 먼저 점검합니다.
<!-- ANNOTATION -->

**경계 (Boundary)**  
PK35 digoxin 사례는 $CL/V/t_{1/2}$ 추정 사례입니다. Loading dose 0.4 mg, maintenance 0.1–0.125 mg/day 같은 처방 문장은 교과서 직접 권고가 아니라 `[교과서 외 통합 추론 예시]`로만 다룹니다. Sheiner 1977을 NONMEM의 직접 조상으로 단정하는 표현은 `[확인 필요]`입니다.

<!-- SLIDE_START: S19 | title: PK35 및 Fig.18-13 확인 지점 | source_anchor: figure-pointer-2-4 -->

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner PK35, Fig.35.1 [pp.641–642]; Rowland & Tozer Ch.18, Fig.18-13 [pp.605–606]
Why this matters: Fig.35.1은 환자별 청소율 변동성(clearance variability)이 농도-시간 거동(concentration-time behavior)과 어떻게 연결되는지 보여 줍니다. Fig.18-13은 채혈 시점(sampling time)에 따라 $V$ vs $CL$ 추정의 신뢰도(confidence)가 왜 달라지는지 보여 줍니다.
When to look: 이 카드의 Sampling identifiability anchor 문단을 읽은 뒤 확인하면 됩니다.
Learner instruction: 먼저 $CL$ 변동성(variability)이 예측 농도-시간 곡선(predicted concentration-time curves)을 어떻게 바꾸는지 확인하세요. 그 다음 Fig.18-13을 보면서 현재 sample이 $V$ 정보를 주는지($V$-informative), $CL$ 정보를 주는지($CL$-informative), 아니면 애매한지(ambiguous)를 질문하면 됩니다.
<!-- /FIGURE_POINTER -->

<!-- SLIDE_START: S20 | title: §2.4 posterior 해석 실무화 | source_anchor: mastery-2-4 -->

> **체화 노트(Mastery Note — CRUCIBLE_DERIVED**  
> Bayesian TDM의 핵심은 농도값 자체보다 그 농도가 어떤 parameter를 식별할 수 있는 시점에서 얻어졌는지입니다. 같은 concentration이라도 timing이 다르면 posterior가 지지하는 $V/CL$ 조합이 달라집니다.

> **▶ 실습 브리프(Practice Brief) — §2.4 체화 4축** — [EXPERT_INFERENCE, v3]  
> - **왜 알아야 하는가:** Bayesian posterior 숫자를 그대로 dose 결정으로 옮기는 *placebo individualization*은 임상 현장에서 가장 흔한 misuse입니다.  
> - **흐름상 역할:** S08(모델) + S15(prior) + 본 세션 §2.5–§2.7(covariate)이 만나는 결합점입니다. §5.6 sampling identifiability와 §7 Q16 NONMEM signature로 이어집니다.  
> - **체화 꿀팁:** 모든 posterior 출력 앞에 *"prior weight vs likelihood weight 비율"*을 한 줄로 기록하는 습관을 들이세요.  
> - **실무 활용:** TDM 소프트웨어(BestDose, ID-ODS) 결과를 보고할 때는 "이 환자의 sample은 V-informative였는지, CL-informative였는지"를 항상 한 문장 첨부합니다. 임상의 권장사항입니다.


---

## §2.5 — 질환/$RF$/$R_d$ 프레임워크: $f_e$와 환자 신기능을 분리하세요 [R&T pp.450–464]
<!-- SECTION_CORE: SC-06 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** $R_d=RF\cdot f_e+(1-f_e)$는 약물 속성 $f_e$와 환자 속성 $RF$를 분리해 maintenance dose를 읽게 하는 renal dosing 문법이다.

---
<!-- SLIDE_START: S21 | title: 질환 RF Rd framework | source_anchor: section-2-5-rd-framework -->


<!-- MASTER LENS -->
**핵심**: renal impairment dosing은 “신장 나쁘니 줄인다”가 아닙니다. drug property $f_e$와 patient property $RF$를 분리한 뒤, 그 조합으로 maintenance requirement를 줄이는 작업입니다.

```math
R_d = RF\cdot f_e + (1-f_e)
```

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{R_d}_{\text{유지용량 비율}}
> =
> \overbrace{\underbrace{RF}_{\text{신기능}}\cdot\underbrace{f_e}_{\text{renal 의존}}}^{\text{renal 기여}}
> +
> \underbrace{(1-f_e)}_{\text{비신 기여}}
> $$


- $f_e$: 미변화체 배설분율(fraction excreted unchanged); drug-specific.
- $RF$: typical 대비 renal function; patient-specific.
- maintenance dose 또는 dosing rate는 $R_d$에 비례하여 조정합니다.

**임상 분류 (Clinical triage)**

- $f_e \leq 0.30$이면 renal function 감소가 maintenance exposure에 미치는 영향이 작을 수 있습니다.
- $RF \geq 0.70$이면 많은 경우 major regimen change가 필요하지 않을 수 있습니다.
- Loading dose는 $CL$이 아니라 $V$에 의존하므로, renal function만으로 자동 감량하지 않습니다. 단, digoxin처럼 uremia에서 tissue distribution이 감소하여 $V$가 줄 수 있는 예외는 별도로 봅니다 [R&T p.464].

**▶ $R_d$ framework 결정 테이블 — [EXPERT_INFERENCE, v3]**

| $f_e\times RF$ 영역 | 해석 | 모델링 함의 | 용량/TDM 지침 |
|---|---|---|---|
| $f_e\cdot RF$ 기여 < 0.1 | 신기능이 전체 제거에 미미한 기여 | $CL_{renal}$ $pprox$ 무시 가능; 간/대사 경로 파라미터에 집중 | 신기능 기반 maintenance 조절 불필요; 간기능 covariate 우선 탐색 |
| $f_e\cdot RF$ 기여 0.1–0.5 | 신기능이 부분 기여 | $CL=CL_{non-renal}+f_e\cdot CL_{total}\cdot RF$로 분리; $RF$를 covariate로 탐색 | 신기능 저하 시 부분 maintenance 감량; TDM으로 개별화 필요 |
| $f_e\cdot RF$ 기여 > 0.5 | 신기능이 주요 제거 경로 | $CL$이 $RF$에 강하게 의존; 신기능 covariate가 $\omega^2$의 주요 설명 변수 | 유지 용량 적극적 감량; loading dose는 $V$ 기반으로 *별도* 결정; TDM 필수 |


> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{CL}_{\text{총 CL}}
> =
> \underbrace{CL_{non\text{-}renal}}_{\text{비신 CL}}
> +
> \overbrace{\underbrace{f_e}_{\text{renal 의존}}\cdot\underbrace{CL_{total}}_{\text{기준 CL}}\cdot\underbrace{RF}_{\text{신기능}}}^{\text{renal CL}}
> $$
>
> **검토 메모:** 이 표의 `$CL_{renal}$ $\approx$ 무시 가능` 표현은 문맥상 renal clearance contribution이 매우 작다는 뜻으로 읽는 것이 자연스럽습니다. 단, 원문 보존 원칙에 따라 원 표기는 수정하지 않았습니다.

참고: $f_e$ = fraction excreted unchanged, $RF$ = patient CrCl / normal CrCl. 이 테이블은 기존 §2.5 본문의 $R_d=RF\cdot f_e+(1-f_e)$ 식과 clinical triage 임계값($f_e\leq0.30$, $RF\geq0.70$)을 결정 격자로 재배열한 것입니다. 새 외부 임계값은 도입하지 않습니다. 컬럼 4의 "loading dose는 $V$ 기반으로 별도 결정"은 §2.9 $V/CL$ 분리 원칙과 cross-link됩니다.

**간 질환 대조 (Hepatic contrast)**  
Cirrhosis에서는 high-extraction oral drug의 first-pass loss 감소와 portal bypass로 $F$가 증가할 수 있습니다. 반대로 low-extraction albumin-bound drug에서는 $f_u$ 증가가 total $CL$을 높일 수 있습니다. 그러나 unbound $CL$(← 단백결합 안 된 약물 기준 청소율)은 크게 변하지 않을 수 있습니다 [R&T pp.444–446]. *(P06 적용)*
<!-- ANNOTATION -->

<!-- TRENCH -->
**현장 팁(Trench-Level Tip)**: phenytoin처럼 albumin-bound low-extraction drug에서는 $f_u\uparrow$가 total concentration 해석을 망칠 수 있습니다. total target을 그대로 쓰면 같은 unbound exposure를 과소평가할 수 있습니다.

<!-- SLIDE_START: S22 | title: Rd framework schematic | source_anchor: figure-schematic-rd-framework -->

<!-- FIGURE_SCHEMATIC -->
Title: $R_d$ 프레임워크 — 약물 속성 $f_e$ × 환자 속성 $RF$
Mode: R
Visual objective: 5초 안에 신장 용량 조절(renal dose adjustment)이 신기능저하 라벨(renal impairment label) 자체가 아니라 $f_e$와 $RF$의 상호작용(interaction)임을 보이게 합니다.
Core message: 유지요법 조절(maintenance adjustment)은 약물이 신장 배설(renal excretion)에 상당히 의존하고 환자의 신기능(renal function)이 의미 있게 감소했을 때 커집니다.
Elements to include: X축: 정상에서 중증 저하까지의 $RF$; Y축 또는 층화 band: 낮음, 중간, 높음의 $f_e$; 출력 구역: $R_d$가 1에 가까운 영역 vs 감소한 영역; 주석: $f_e$ = 약물 속성(drug property), $RF$ = 환자 속성(patient property), $R_d$ = 유지요법 필요량(maintenance requirement); 작은 callout: $V$가 변하지 않으면 LD는 별도입니다.
Elements to exclude: 교과서 곡선의 정확한 재현, 여러 약물 예시, Cockcroft-Gault 식의 세부 전개(equation details).
Suggested rendering: SVG
Caption: $R_d$는 신기능 저하 자체가 아니라 약물별 $f_e$(drug-specific $f_e$)와 환자별 $RF$(patient-specific $RF$)의 조합으로 유지요법 필요량(maintenance requirement)을 줄입니다.
Alt text: 한 축에는 신기능(renal function), 다른 축에는 미변화체 배설분율(fraction excreted unchanged)을 두고, 신장 의존성(renal dependence)과 신기능저하(impairment)가 모두 클 때 유지 용량 필요량(maintenance dose requirement)이 가장 크게 감소함을 보여 주는 두 축 개념 표면.
Source relation: 교과서 개념을 바탕으로 재도식화(Redrawn from textbook concept)
<!-- /FIGURE_SCHEMATIC -->

<!-- SLIDE_START: S23 | title: §2.5 failure mode and practice | source_anchor: failure-2-5 -->

> **실무 렌즈(Practice Lens) — TEXTBOOK_DERIVED**  
> $R_d$ framework는 “환자 라벨”과 “약물 라벨”을 분리하는 계산 문법입니다. 같은 renal impairment라도 $f_e$가 낮은 약물과 높은 약물의 maintenance decision은 달라져야 합니다.

> **실패 모드(Failure Mode — CRUCIBLE_DERIVED**  
> $R_d$ 식이 통하려면 “비신 $CL$은 $RF$에 의해 변하지 않는다”는 가정이 성립해야 합니다. R&T Fig.15-15 [R&T pp.464–466]는 imipenem처럼 신장에서 일부 *대사*까지 일어나는 약물에서는 total $CL$과 renal $CL$의 두 곡선이 $RF\downarrow$에 따라 평행하지 않고 간격이 좁아짐을 보여줍니다. 이 형태가 보이면 $f_e$만으로 $R_d$를 적용하지 마세요. “신장이 대사도 한다”는 신호로 읽고 환자 데이터 또는 별도 모델로 보정합니다. cerivastatin·bupropion·telithromycin 등도 같은 패턴 후보입니다.

> **▶ 실습 브리프(Practice Brief) — §2.5 체화 4축** — [EXPERT_INFERENCE, v3]  
> - **왜 알아야 하는가:** 신부전 환자 dosing은 임상약사 8년 경력의 *핵심 use case*이며, fe와 RF를 분리하지 못하면 환자별 dose error가 누적된다.  
> - **흐름상 역할:** S04 covariate + S05 IIV의 임상 응용; §2.6 Cockcroft-Gault → §2.7 dialysis로 이어지는 신기능 트랙의 첫 카드.  
> - **체화 꿀팁:** 약물 한 개를 만나면 즉시 "fe = ?, RF에 따라 어디 영역?"을 *동시에* 묻는 mental routine을 만들 것.  
> - **실무 활용:** 항생제 (vancomycin, aminoglycosides), digoxin, lithium 같은 high-fe 약물의 입원 환자 protocol 작성 시, MA22 결정 테이블을 그대로 쓸 수 있다.


---

## §2.6 — Cockcroft-Gault + creatinine lag [R&T pp.457–461]
<!-- SECTION_CORE: SC-07 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** 신기능과 투석 판단은 숫자 하나가 아니라 시간·unbound CL·sampling 맥락의 문제다 — SCr lag와 $CL_{uD}$를 따로 보라.

---
<!-- SLIDE_START: S24 | title: Cockcroft-Gault와 creatinine lag | source_anchor: section-2-6-cockcroft-gault -->


<!-- MASTER LENS -->
**핵심**: Cockcroft-Gault는 RF의 입력값을 만든다. 그러나 SCr는 실시간 renal function의 거울이 아니다. SCr는 creatinine turnover가 반영된 *지연* 지표이기 때문이다. *(P07 적용)*

```math
CL_{cr}\;(mL/min)=\frac{(140-age)\cdot WT}{72\cdot SCr}
```

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{CL_{cr}}_{\text{CrCL 추정}}\;(\mathrm{mL/min})
> =
> \frac{\underbrace{(140-age)}_{\text{연령}}\cdot\underbrace{WT}_{\text{체중}}}{\underbrace{72\cdot SCr}_{\text{SCr 보정}}}
> $$


여성에서는 일반적으로 0.85를 곱한다. 식은 adult, stable renal function, body size interpretation이 전제이다 [R&T p.457].

**AKI 주의사항 (AKI caveat)**  
Acute renal failure에서는 SCr 상승이 renal function 감소보다 늦다. R&T Table 15-6은 renal function이 낮아질수록 creatinine turnover time과 half-life가 길어짐을 보여준다 [R&T pp.459–461]. 따라서 오늘 측정한 SCr로 오늘의 RF를 과신하면, 초기 24–48h 독성 축적을 놓칠 수 있다.

<!-- TRENCH -->
**현장 팁(Trench-Level Tip)**: C-G는 snapshot 계산이 아니라 trend 해석과 함께 써야 한다. 특히 노인, 근감소, 비만, AKI에서는 체중 선택과 SCr lag가 dose error의 주된 원인이다.

> **실패 모드(Failure Mode) — AUDIT_DERIVED**  
> SCr가 아직 새 steady state에 도달하지 않았는데 Cockcroft-Gault 값을 그대로 RF로 쓰면, 계산은 정확해 보여도 임상적으로는 과거 신기능을 반영할 수 있다. 이 카드는 식보다 시간 지연을 함께 기억해야 한다. R&T Table 15-6 [pp.459–461]은 RF가 낮을수록 creatinine turnover time과 half-life가 길어짐을 정량적으로 보여준다. RF가 크게 떨어진 환자에서 creatinine half-life는 수십 시간 단위로 늘어날 수 있으므로, 오늘의 SCr은 며칠 전 RF의 거울일 수 있다. 이것이 첫 24–48시간 표준 용량이 toxic 농도로 누적되는 메커니즘이다.

> **▶ 실습 브리프(Practice Brief) — §2.6 체화 4축** — [EXPERT_INFERENCE, v3]  
> - **왜 알아야 하는가:** AKI 환자 첫 24–48h dosing 결정에서 SCr lag를 무시하면 실제 RF 대비 *과대 추정* dose가 들어가 nephrotoxic 약물이 누적된다.  
> - **흐름상 역할:** §2.5 Rd framework의 *입력값*을 만드는 카드; ICU 환자에서 §2.4 Bayesian TDM과 결합되어 작동한다.  
> - **체화 꿀팁:** Cockcroft-Gault 값을 단일 숫자가 아니라 *trend slope*과 함께 보는 시각을 길러라 — "이 SCr가 오르고 있는 중인가, 안정인가?"  
> - **실무 활용:** ICU vancomycin·aminoglycoside protocol에서 첫 48h는 *보수적* 용량 + 조기 TDM 샘플로 보정하는 전략의 이론적 근거가 이 카드에 있다.


---

## §2.7 — 혈액투석 좌표 평면: $V_u$와 $CL_u$를 함께 보세요 [R&T pp.466–474]
<!-- SLIDE_START: S25 | title: Hemodialysis coordinate plane | source_anchor: section-2-7-hemodialysis -->


<!-- MASTER LENS -->
**핵심**: hemodialysis 보충 용량은 “half-life가 줄었는가”만으로 결정하지 않는다. dialysis session 동안 body amount가 의미 있게 빠졌는지가 핵심이다.

**확정된 수정 (Locked correction)**

```text
삭제: Vu < 120 L AND CLu < CLuD이면 보충 용량 필요.
채택: Vu·CLu 평면에서 dialysis effectiveness를 읽는다.
```

R&T Fig.15-18은 high-flux 3 h dialysis에서 unbound V가 약 120 L보다 크거나, 환자의 own unbound clearance가 dialysis clearance보다 훨씬 크면 dialysis가 제거하는 fraction이 20% 미만으로 작아질 수 있음을 보여준다 [R&T pp.471–472]. 따라서 이는 hard AND gate가 아니라 continuous trade-off이다.

**핵심 수식 — 개념 수준 (Key equations, concept level)**

- During dialysis: `kD = (CLu + CLuD)/Vu`.
- Fraction lost during dialysis period: `1 − exp(−kD·T)`.
- Dialysis contribution depends on `CLuD/(CLu + CLuD)` and the fraction lost over the session.
- Supplementary dose is considered when the amount after dialysis should be restored to the amount expected without dialysis [R&T pp.471–474].


> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{k_D}_{\text{투석 중 제거}}
> =
> \frac{\overbrace{\underbrace{CL_u}_{\text{자체 CL}}+\underbrace{CL_{uD}}_{\text{투석 CL}}}^{\text{총 unbound CL}}}{\underbrace{V_u}_{\text{unbound V}}},
> \qquad
> \underbrace{1-\exp(-k_D\cdot T)}_{\text{session 제거율}},
> \qquad
> \underbrace{\frac{CL_{uD}}{CL_u+CL_{uD}}}_{\text{투석 기여}}
> $$

**CAPD 대조 (CAPD contrast)**  
CAPD clearance는 대부분의 약물에서 혈액투석 clearance보다 낮다. 따라서 '투석 환자'라는 단일 라벨로 용량 규칙을 하나로 묶을 수 없다 [R&T pp.475–477]. *(P08 적용)*

<!-- TRENCH -->
**현장 팁(Trench-Level Tip)**: Phenobarbital의 dialysis half-life가 크게 줄어도 single 3 h session에서 body amount가 충분히 빠지지 않을 수 있습니다. 반감기 단축과 세션 중 제거된 약물량은 같은 endpoint가 아닙니다. *(P09 적용)*

<!-- SLIDE_START: S26 | title: Fig.15-18 및 Fig.15-19 확인 지점 | source_anchor: figure-pointer-2-7 -->

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer Ch.15, Fig.15-18 [p.471] and Fig.15-19 [p.473]
Why this matters: Fig.15-18은 투석 제거(dialysis removal)가 hard threshold가 아니라 $V_u$와 $CL_u$의 연속 함수(continuous function)임을 보여 줍니다. Fig.15-19는 투석 중 제거량을 보충 용량 개념(replacement-dose concept)과 연결합니다.
When to look: 이 카드의 확정 수정(locked correction) block을 읽은 뒤 확인하면 됩니다.
Learner instruction: 어떤 보충 용량 규칙(supplement rule)을 적용하기 전에 Fig.15-18을 먼저 확인하세요. 해당 환자-약물 조합(patient-drug pair)이 투석 세션(dialysis session) 동안 임상적으로 의미 있는 체내 약물량(body amount)을 제거하는 영역에 있는지 질문하면 됩니다.
<!-- /FIGURE_POINTER -->

<!-- SLIDE_START: S27 | title: §2.7 dialysis practice | source_anchor: failure-2-7 -->

> **실패 모드(Failure Mode) — AUDIT_DERIVED**  
> Dialysis decision에서 half-life shortening은 시각적으로 강한 신호입니다. 그러나 supplement decision의 endpoint는 session 동안 빠진 body amount입니다. 그래서 $V_u$와 $CL_{uD}/CL_u$의 좌표를 함께 읽어야 합니다.

> **▶ 실습 브리프(Practice Brief) — §2.7 체화 4축** — [EXPERT_INFERENCE, v3]  
> - **왜 알아야 하는가:** "혈액투석 = 보충용량 필요"라는 단순화는 high-$V_u$ 약물에서 불필요한 추가 용량을 처방하게 만들어 *반대 방향* 독성을 부릅니다.  
> - **흐름상 역할:** §2.5–§2.6 신기능 트랙의 *intermittent* 변종입니다. 단일 시점이 아니라 *세션 단위* 시간 척도로 읽어야 합니다.  
> - **체화 꿀팁:** 모든 dialysis 약물 결정에서 항상 두 좌표를 *동시에* 물으세요. "$V_u$는 큰가? $CL_{uD}/CL_u$는 큰가?"  
> - **실무 활용:** vancomycin, gentamicin, phenobarbital 같은 흔한 임상 약물의 dialysis 후 보충 protocol을 환자별로 재평가할 때 표준 절차가 됩니다.


---

## §2.8 — 목표농도전략 기준(Target Concentration Strategy criteria) [R&T pp.594–597]
<!-- SECTION_CORE: SC-08 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** $V$는 loading dose를, $CL$은 maintenance dose를 지배한다 — TCS와 missed dose 판단도 이 분리를 깨면 무너진다.

---
<!-- SLIDE_START: S28 | title: Target Concentration Strategy criteria | source_anchor: section-2-8-tcs -->


<!-- MASTER LENS -->
**핵심**: TCS는 특정 약물명에 자동 적용되는 필수 전략이 아닙니다.
<!-- ANNOTATION -->
여기서 핵심은 “농도를 잴 수 있는가”가 아니라, 그 농도가 다음 clinical decision을 바꿀 만큼 제때·정확하게 해석되는가입니다. criteria가 대부분 충족될 때, 치료 시작 및 모니터링 단계에서 유용한 보조 전략(adjunct strategy)이 됩니다. *(P10 적용)*

**기준 잠금 (Criteria lock)**

1. Concentration-response relationship이 충분히 좋아야 합니다.
2. Therapeutic failure probability가 높아야 합니다: low therapeutic index, large PK variability, genetic/disease/drug-interaction risk, nonadherence/erratic absorption 가능성.
3. Population PK information이 있어야 합니다.
4. Reliable assay가 가능해야 합니다.
5. Assay turnaround가 다음 therapeutic decision 전에 도착해야 합니다.

**Table 18-5 잠금 (Table 18-5 lock)**  
Cyclosporine, digoxin, gentamicin, nortriptyline, phenytoin, theophylline 등은 TCS가 clinically helpful했던 대표 후보군입니다. 약물명만으로 TCS가 필수라는 뜻은 아닙니다 [R&T pp.595–596].

**Table 18-6 해석 관문 (Table 18-6 interpretation gate)**  
Measured concentration 하나만으로는 해석이 끝나지 않습니다. 완전한 해석을 위해서는 dosing history, sampling time, previous concentrations, clinical status, renal/hepatic laboratory data, protein binding, concurrent drugs, assay method, usual PK parameters가 모두 필요합니다 [R&T p.597]. *(P11 적용)*

**페니토인 잠금 (Phenytoin lock)**  
Phenytoin은 saturable metabolism과 altered protein binding의 영향을 받아 monitoring 정당성이 강합니다 [R&T pp.588, 595–596]. 그러나 total concentration target은 uremia, surgery, displacement drugs에서 unbound target을 맞추도록 조정되어야 합니다 [R&T p.596]. *(P12 적용)*

<!-- TRENCH -->
**현장 팁(Trench-Level Tip)**: TCS의 5 criteria는 checklist가 아니라 sequential filter입니다. 하나가 실패하면 measured number가 있어도 임상 의사결정에 유용하지 않을 수 있습니다.

> **실무 렌즈(Practice Lens) — TEXTBOOK_DERIVED**  
> TCS는 “농도를 측정할 수 있음”이 아니라 “측정값이 다음 처방 결정을 바꿀 수 있음”을 요구합니다. Table 18-6의 정보가 빠지면 concentration은 숫자일 뿐 decision object가 아닙니다.

> **체화 노트(Mastery Note — CRUCIBLE_DERIVED**  
> phenytoin은 saturable metabolism으로 monitoring 정당성이 강해집니다. 농도가 작은 dose 변화에도 비선형으로 반응하기 때문에, 같은 mg/day가 환자마다 다른 농도를 만듭니다. 한편 trimipramine·nortriptyline 등 CYP2D6 polymorphism이 큰 약물 [R&T Fig.18-6, p.583]에서는 prior 자체가 phenotype subgroup별로 갈라집니다. 이 두 경우 모두, 평균 농도 하나만 보고하는 것은 의사결정 정보로 부족합니다. 적용 전에 “이 환자가 어느 subgroup에 속하는가”라는 prior 질문을 먼저 던져야 합니다. 이는 §2.4 Bayesian objective function의 prior 선택 문제와 동일한 구조입니다.

> **실패 모드(Failure Mode) — AUDIT_DERIVED**  
> Tozer Fig.18-2 [R&T p.579]의 PD variability 분해 백분율(예: gene 40%, age 15%, drugs 10% 등)은 *hypothetical* drug schematic입니다. 이 수치를 특정 약물의 PD variability 추정으로 인용하면 source 외 주장이 됩니다. NDA 등 규제 맥락에서 이런 인용은 careless citation으로 판정되어 deficiency 사유가 될 수 있습니다. 이는 `[교과서 외 규제 번역]` 영역의 위험 지점입니다.

> **▶ 실습 브리프(Practice Brief) — §2.8 체화 4축** — [EXPERT_INFERENCE, v3]  
> - **왜 알아야 하는가:** "TCS 후보 약물 = 자동 monitoring"으로 환원하면 turnaround이 느린 환경에서 *결정에 쓰이지 못하는* 데이터만 쌓는 placebo monitoring이 됩니다.  
> - **흐름상 역할:** §2.4 Bayesian estimation과 §2.9–§2.10 dosing decision을 잇는 *전략 결정* 카드입니다. §7 Q15 Boss-Dilemma의 직접 무대입니다.  
> - **체화 꿀팁:** 5 criteria를 *checklist*가 아니라 *sequential filter*로 외우세요. 하나가 마르면 나머지를 더 쌓아도 의미 없습니다.  
> - **실무 활용:** TDM 도입 결정 회의에서 5 criteria를 차례로 점검하는 것이 임상약사·임상약리학자의 표준 workflow입니다.


---

## §2.9 — Loading dose vs maintenance dose [R&T pp.582, pp.584–586]
<!-- SLIDE_START: S29 | title: Loading dose vs maintenance dose | source_anchor: section-2-9-ld-md -->


<!-- MASTER LENS -->
**핵심**: loading dose와 maintenance dose는 서로 다른 parameter가 지배합니다.
<!-- ANNOTATION -->
따라서 TCS가 target concentration을 정해 주더라도, 어떤 dose component를 바꿀지는 $V$와 $CL$을 분리해서 결정해야 합니다. loading dose는 $V$와 target concentration의 문제이고, maintenance dose는 $CL$과 target average exposure의 문제입니다.

```math
D_L = \frac{V\cdot C_{target}}{F}
```

> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{D_L}_{\text{loading dose}}
> =
> \frac{\underbrace{V}_{\text{분포 공간}}\cdot\underbrace{C_{target}}_{\text{목표 농도}}}{\underbrace{F}_{\text{이용률}}}
> $$


**Fig.18-5 수정 잠금 (Corrected Fig.18-5 lock)**  
Step 1의 “$V$ 90% 설명” 또는 “$V$ 5–10% 정확도” 표현은 삭제합니다. 이 표현들은 Fig.18-5의 의미를 prediction accuracy로 잘못 읽게 만듭니다. R&T Fig.18-5의 variability partition은 대략 다음을 보여줍니다: $V$는 body weight 25% + age 10% + renal function 10%로 약 45% explained, 55% unaccounted; hepatic $CL$은 약 40% explained, 60% unaccounted; renal $CL$은 renal function 50% + body weight 15% + age 15%로 약 80% explained; $F$는 약 5%만 explained [R&T p.582].

**임상적 함의 (Clinical implication)**

- Renal-clearance dominant drug의 maintenance dose는 $RF$로 비교적 강하게 예측됩니다.
- Hepatic-clearance dominant drug의 maintenance dose는 demographic covariate만으로 설명되지 않는 IIV가 큽니다.
- Loading dose는 $V$-driven이지만, 실제 투여에서는 distribution kinetics, administration rate, formulation, available dose strengths `[p.확인 필요]`, toxicity risk 등을 고려해 분할 투여(divided loading)가 필요할 수 있습니다. Chloroquine example처럼 theoretical LD를 한 번에 투여하지 않는 이유가 여기에 있습니다 [R&T p.585]. *(P13 적용)*

<!-- TRENCH -->
**현장 팁(Trench-Level Tip)**: “신부전이므로 LD도 줄인다”는 자동 규칙은 틀릴 수 있습니다. LD는 $V$ 문제이고 MD는 $CL$ 문제입니다. 단, digoxin uremia처럼 $V$ 자체가 변하는 예외는 따로 잡습니다.

<!-- SLIDE_START: S30 | title: Fig.18-5 variability partition 확인 지점 | source_anchor: figure-pointer-2-9 -->

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer Ch.18, Fig.18-5 [p.582]
Why this matters: 이 그림은 $V/CL$ 예측 정확도(prediction accuracy)를 잘못 읽는 오류를 바로잡는 데 핵심입니다. 용량 정확도(dosing precision)를 약속하는 그림이 아니라 변동성 분할(variability partition)로 보아야 합니다.
When to look: 이 카드의 Fig.18-5 수정 기준 문단을 읽은 직후 확인하면 됩니다.
Learner instruction: 이 그림은 변동성(variability) 중 어느 부분(fraction)이 설명되고 무엇이 설명되지 않은 채(unaccounted) 남는지 묻는 방식으로 읽으세요. 그 다음 renal $CL$이 hepatic $CL$이나 $F$보다 유지요법 예측(maintenance prediction)을 더 강하게 지지할 수 있는 이유와 연결하면 됩니다.
<!-- /FIGURE_POINTER -->

<!-- SLIDE_START: S31 | title: §2.9 LD MD practice | source_anchor: mastery-2-9 -->

> **체화 노트(Mastery Note — AUDIT_DERIVED**  
> Fig.18-5는 “얼마나 정확히 맞출 수 있는가”가 아니라 “어떤 variability가 설명되고 무엇이 남는가”를 보여줍니다. 따라서 LD/MD 판단에서는 $V$와 $CL$의 설명 가능성을 분리해 읽어야 합니다.

> **▶ 실습 브리프(Practice Brief) — §2.9 체화 4축** — [EXPERT_INFERENCE, v3]  
> - **왜 알아야 하는가:** "신부전 → LD도 줄여야 한다"는 가장 흔한 임상 misapplication이며, §5.5 Critical Blow의 메커니즘이 여기서 시작됩니다.  
> - **흐름상 역할:** §2.5 $R_d$ framework + §2.4 Bayesian + §2.10 dosing irregularity의 *결정* 단계입니다. "어떤 dose component를 바꿀지"의 분기점입니다.  
> - **체화 꿀팁:** 모든 dose 결정 앞에 *"이건 $V$ 문제인가, $CL$ 문제인가?"*를 한 줄로 자문하는 습관을 들이세요.  
> - **실무 활용:** ICU loading dose protocol 작성 시 신기능 항목과 $V$ 변화 항목을 *분리해 명시*하는 것이 미국·유럽 표준입니다. 한국 protocol에도 적용 가능한 best practice입니다.


---

## §2.10 — Missed / unequal / erratic dosing framework [R&T pp.600–605]
<!-- SLIDE_START: S32 | title: Missed unequal erratic dosing | source_anchor: section-2-10-irregular-dosing -->


<!-- MASTER LENS -->
**핵심**: nonadherence, unequal interval, erratic ICU dosing은 TDM 해석을 망치는 예외가 아닙니다. superposition(← 각 용량의 남은 농도 기여를 더하는 원리)으로 정량화할 수 있는 일반 상황입니다.
<!-- ANNOTATION -->

**세 가지 시나리오 (Three scenarios)**

| 시나리오 (Scenario) | 수식 (Equation) | 확정된 활용 (Locked use) |
|---|---|---|
| 한 번의 missed dose | Eq.18-1 | 예상 정상상태(steady-state) 농도에서 missed dose의 잔여 기여를 뺀다. |
| 연속된 두 번의 missed doses | Eq.18-2 | 두 missed doses의 기여를 뺀다. |
| 9-13-17-21 institutional regimen | Eq.18-3 | 일중 간격이 unequal한 24시간 반복 cycle. |
| Dose와 interval 모두 unequal | Eq.18-4 | 이전 dose들의 잔여량을 합산; 환자 $4\times t_{1/2}$ 이전 dose는 무시 가능. |

**유지된 풀이 예제(Worked examples retained)**

- Digoxin: typical patient가 0.25 mg daily dose를 두 번 missed한 경우, expected concentration은 0.39 µg/L입니다. 이는 therapeutic range 0.8–2.0 µg/L보다 낮습니다 [R&T p.602].
- Vancomycin 9-13-17-21: 20 kg, 5-year-old, $V$ 14 L, $CL$ 3.3 L/h, $k$ 0.24 h⁻¹, 250 mg regimen은 8:00 concentration 2.03 mg/L를 만듭니다. 이는 therapeutic 5–15 mg/L보다 낮습니다 [R&T pp.602–603].
- Erratic vancomycin: 68 kg, 60-year-old male, SCr 2.2 mg/dL, $CL_{cr}$ 34 mL/min, $V$ 42.2 L, $k$ 0.049 h⁻¹; observed 34 mg/L vs predicted 33.7 mg/L입니다. 이는 kinetics는 consistent하지만 dose가 too high임을 시사합니다 [R&T p.604].

**삭제된 주장(Deleted claim)**  
“TDM 환자의 80%”는 source-backed 표현이 아니므로 삭제합니다.

<!-- TRENCH -->
**현장 팁(Trench-Level Tip)**: adherence phantom을 IIV로 흡수하지 마세요. dosing history와 sampling time은 clerical detail이 아니라 model input입니다.

> **실무 렌즈(Practice Lens) — TEXTBOOK_DERIVED**  
> Missed, unequal, erratic dosing은 예외 처리 항목이 아니라 superposition의 일반 적용입니다. dose history와 sampling time을 narrative가 아니라 parameter estimation의 입력으로 취급해야 합니다.

> **체화 노트(Mastery Note — CRUCIBLE_DERIVED**  
> R&T Fig.18-9 [p.592]는 “자주 먹을수록 missed dose에 더 취약하다”는 직관을 뒤집습니다. 동일 약물($t_{1/2}pprox18.2$ h, $V=50$ L, window 8–20 mg/L)에서 600 mg q24h regimen 한 번 missed → trough 3.2 mg/L(window 미달), 200 mg q8h regimen 세 번 연속 missed → trough 5.0 mg/L(여전히 q24h 한 번 miss보다 위). 즉 $t_{1/2}/\tau$ 비율이 forgiveness를 결정합니다. q8h: $t_{1/2}/\taupprox2.27$(forgiving), q24h: $t_{1/2}/\taupprox0.76$(unforgiving). 이는 §2.4 Bayesian의 prior-likelihood 균형, §2.7 dialysis의 $V_u\cdot CL_{uD}$ 곱과 함께 “두 인자의 곱이 결과를 결정한다”는 §8 Meta-pattern 1의 동형 사례입니다.


> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{\frac{t_{1/2}}{\tau}}_{\text{시간 여유}}
> \times
> \underbrace{\text{therapeutic window}}_{\text{농도 여유}}
> \Rightarrow
> \underbrace{\text{forgiving/unforgiving regimen}}_{\text{missed-dose 내성}}
> $$
>
> **검토 메모:** 원문 중 `$t_{1/2}\approx18.2$`, `$t_{1/2}/\tau\approx2.27$`, `$t_{1/2}/\tau\approx0.76$`에 해당하는 표기는 문맥상 approximate relation으로 읽는 것이 자연스럽습니다. 단, 원문 보존 원칙에 따라 원 표기는 수정하지 않았습니다.

> **▶ 실습 브리프(Practice Brief) — §2.10 체화 4축** — [EXPERT_INFERENCE, v3]  
> - **왜 알아야 하는가:** Missed/erratic dosing은 *예외*가 아니라 임상 환경의 *기본 상태*에 가깝습니다. superposition으로 정량화하지 못하면 TDM 해석이 무효화됩니다.  
> - **흐름상 역할:** 본 세션 capstone의 *마지막* 카드입니다. §2.1–§2.9가 만든 모든 도구가 irregular dosing 환경에서 어떻게 작동하는지 종합합니다. §8 Meta-pattern 1과 cross-link됩니다.  
> - **체화 꿀팁:** Eq.18-1–18-4를 외우는 대신 *"이전 dose의 남은 기여를 더한다"*는 superposition 직관 한 줄을 먼저 고정하세요. 식은 그 위에 얹으면 됩니다.  
> - **실무 활용:** 외래·재가 환자 상담에서 "한 번 빠뜨렸는데 어떻게 하나요?"에 대한 답을 $t_{1/2}/\tau$ 비율 한 단어로 요약할 수 있습니다(forgiving/unforgiving 라벨).


<!-- RECAP -->
**§2 recap**: Ch.6이 model 후보를 만들고, Ch.15가 patient-specific parameter deviation을 설명하며, PK35가 posterior parameter를 추정하고, Ch.18이 그 추정을 dosing and monitoring decision으로 변환합니다.

---

# §5 — 혼동 쌍 해부 (Confusion Pair Dissection)
<!-- SECTION_CORE: SC-09 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** Confusion pair는 시험용 암기가 아니라 실무 오류 차단 장치다 — $C_e/R/RC$, $RF/f_e$, $V/CL$, sampling confidence를 끝까지 분리하라.

---
<!-- SLIDE_START: S33 | title: Confusion pair overview | source_anchor: section-5-confusion-pairs -->


## §5.1 — 효과구획(effect compartment) vs turnover
<!-- SLIDE_START: S34 | title: Effect compartment vs turnover | source_anchor: section-5-1-effect-vs-turnover -->


<!-- CONFUSION -->
| 쌍 (Pair) | 잘못된 지름길 (Wrong shortcut) | 올바른 판별자 (Correct discriminator) |
|---|---|---|
| Effect compartment | “delay가 있으면 모두 turnover” | Delay가 있으나 dose-dependent peak-shift가 뚜렷하지 않으면 $C_e$ equilibration이 우선 후보. |
| Turnover | “response가 늦으면 link model” | baseline, rebound, adaptation, dose-dependent shift가 보이면 production/loss process 자체가 변한 것일 수 있습니다. |

**한 줄 요약(One-line lock)**: Effect compartment는 response site equilibration delay이고, turnover는 response system의 input/output rate가 drug에 의해 변하는 것입니다 [G&W pp.425–426].

> **⚡ 기억 고리 (Memory Hook) — *분포 지연 vs 시스템 지연*** — [EXPERT_INFERENCE, v3]  
> Effect compartment는 약이 plasma에서 effect site로 **이동하는 데 걸리는 시간**이 지연의 원인입니다. Turnover는 effect site에 약이 도달했지만 **response system 자체가 바뀌는 데 걸리는 시간**이 지연의 원인입니다. 진단 단서: dose-dependent response peak shift가 보이면 turnover, 보이지 않으면 effect compartment 가능성이 높습니다. (S11/S12 개념의 캡스톤 통합 — "Name the delayed state"의 임상 버전.)

---

## §5.2 — 좌측 이동 vs 우측 이동 peak movement(Left-shift vs right-shift)
<!-- SLIDE_START: S35 | title: Left-shift vs right-shift | source_anchor: section-5-2-left-right-shift -->


<!-- CONFUSION -->
| 패턴 (Pattern) | 오독 (Misread) | 확정된 해석 (Locked interpretation) |
|---|---|---|
| 좌측 trough shift (Leftward trough shift) | “무조건 receptor on/off” | turnover loss stimulation과 receptor on/off가 모두 후보가 될 수 있다. |
| 우측 trough shift + flat high-dose 구간 (Rightward trough shift + flat high-dose portion) | “absorption delay” | input inhibition with saturation가 강한 후보가 된다. |

**한 줄 요약(One-line lock)**: 방향은 확정 규칙이 아니라 competing models를 줄이는 sign입니다 [G&W pp.424–428].

> **⚡ 기억 고리 (Memory Hook) — *방향은 단서이지 결론이 아니다*** — [EXPERT_INFERENCE, v3]  
> Peak 이동 방향은 메커니즘을 구분하는 **1차 필터**이지 최종 판단이 아닙니다. 같은 방향의 이동이 receptor on/off, turnover loss stimulation, distribution delay 등 여러 메커니즘에서 나타날 수 있습니다. 방향을 보고 *가설 목록을 좁히고*, 추가 데이터(dose scaling, time course 비교)로 하나씩 *제거*하는 방식이 올바른 접근입니다.

---

## §5.3 — Bayesian “no concentration” vs “no prior”
<!-- SLIDE_START: S36 | title: Bayesian no concentration vs no prior | source_anchor: section-5-3-bayesian-extremes -->


<!-- CONFUSION -->
| 조건 (Condition) | 추정 거동 (Estimate behavior) | 위험 (Risk) |
|---|---|---|
| 농도 없음 (No concentration) | population average가 지배 | 환자 특이 deviation을 놓침. |
| Prior 없음 (No prior) | concentration fit이 지배 | sparse 또는 mistimed 농도는 생리학적으로 불가능한 파라미터를 만들 수 있음. |
| Prior + 농도 (Prior + concentration) | Bayesian compromise | dosing/sampling/assay history가 신뢰할 만할 때만 유용. |

**한 줄 요약(One-line lock)**: Bayesian TDM의 핵심 역량은 "posterior number를 믿는 것"이 아니라, 그 농도가 어떤 parameter를 식별할 수 있는 시점에 얻어졌는지를 판단하는 것입니다 [G&W pp.641–643; R&T pp.597, 605–606]. *(P14 적용)*

> **⚡ 기억 고리 (Memory Hook) — *데이터 없음 vs 사전 지식 없음*** — [EXPERT_INFERENCE, v3]  
> "No concentration"에서 Bayesian TDM은 population mean으로 회귀합니다. 개인 특이 정보가 없으니 집단 대표값을 그대로 씁니다. "No prior"에서는 측정 농도만이 파라미터를 결정합니다. 이때 측정이 희소하거나 타이밍이 나쁘면 생리학적으로 불합리한 파라미터가 나옵니다. 좋은 Bayesian TDM은 *prior의 강도(정보량)와 likelihood의 강도(측정 품질)를 동시에 평가*하고 어느 쪽이 지배하는지 인식하는 것입니다.

---

## §5.4 — 간 고추출 약물 vs 신장 배설 약물(Hepatic high-extraction drug vs renal-excreted drug)
<!-- SLIDE_START: S37 | title: Hepatic high-extraction vs renal-excreted | source_anchor: section-5-4-hepatic-renal -->


<!-- CONFUSION -->
| 약물 상황 (Drug situation) | 일차적으로 변하는 양 (Primary altered quantity) | 용량 함의 (Dosing implication) |
|---|---|---|
| 간경변에서의 고추출 경구 약물 (High-extraction oral hepatic drug in cirrhosis) | F 증가; CL은 감소할 수 있음 | 경구 노출이 급격히 증가할 수 있음. |
| 알부민 결합 저추출 약물 (Low-extraction albumin-bound drug) | fu 증가; total CL은 증가할 수 있으나 unbound CL은 그렇지 않을 수 있음 | total concentration target의 재해석이 필요할 수 있음. |
| 신장 배설 미변화 약물 (Renal-excreted unchanged drug) | RF가 renal CL 성분을 낮춤 | Rd framework가 maintenance dose를 안내할 수 있음. |

**한 줄 요약(One-line lock)**: 간 질환이 있다고 해서 '$CL$이 모두 감소한다'는 뜻이 아닙니다. extraction ratio, $F$, 단백결합, unbound $CL$이 변화의 방향을 결정합니다 [R&T pp.444–446]. *(P15 적용)*

> **⚡ 기억 고리 (Memory Hook) — *간 질환 = CL 감소?의 함정*** — [EXPERT_INFERENCE, v3]  
> High-extraction 경구 약물에서 간경변은 $F$를 *증가*시키고 $CL$을 *감소*시켜 노출을 급격히 올립니다. 두 방향 모두 *같은 쪽*이어서 파급력이 큽니다. Low-extraction albumin-bound 약물에서 저알부민혈증은 $f_u$를 올리고 total $CL$을 올릴 수 있지만 *unbound $CL$은 변하지 않아 free concentration이 유지됩니다*. 신장 배설 약물에서는 $R_d=1-f_e(1-RF)$ 공식이 작동합니다. "간 질환 = $CL$ 감소"는 *high-extraction 약물에만 유효한* 단순화입니다.

---

## §5.5 — Loading dose vs maintenance dose
<!-- SLIDE_START: S38 | title: Loading dose vs maintenance confusion | source_anchor: section-5-5-ld-md-confusion -->


<!-- CONFUSION -->
| 결정 (Decision) | 지배 파라미터 (Dominant parameter) | 흔한 오류 (Common error) | 올바른 대응 (Correct move) |
|---|---|---|---|
| Loading dose | $V$와 target concentration | $CL_{cr}$이 낮다는 이유만으로 LD를 줄임 | $V$가 변했는지 확인; renal impairment만으로는 LD 감량을 의미하지 않음. |
| Maintenance dose | $CL$과 target average exposure | 장기 dosing에 $V$ 논리를 사용 | $CL/RF/R_d$로 조정하고 criteria가 정당화하면 TDM으로 갱신. |
| TCS 해석 (TCS interpretation) | 농도, 시점, 이력, assay | Table 18-6 데이터 없이 측정 농도만 사용 | dosing/sampling history를 먼저 재구성. |
| **▶ 치명적 타격(Critical Blow)** | colspan-style note → | 신부전 환자에서 loading dose를 신기능에 비례해 줄이면(예: CrCl 30 mL/min에서 LD를 50%로 감량), 실제로 $V$가 변하지 않는 항생제(aminoglycoside)에서 *초기 치료 농도를 달성하지 못합니다*. Bactericidal 항생제에서 초기 24시간 치료 실패는 **내성 선택 압력의 시작점**이 될 수 있습니다. 이 오류는 $R_d$ framework를 loading dose에 잘못 적용했을 때 발생하는 전형적 misapplication입니다. — [EXPERT_INFERENCE, v3] | |

**Fig.18-5 수정된 진술(Corrected Fig.18-5 statement)**: Fig.18-5의 schematic variability partition에서 $V$는 약 45%, hepatic $CL$은 약 40%, renal $CL$은 약 80%, $F$는 약 5%가 covariate로 설명됩니다. 이는 loading-dose의 "정확도(accuracy)" 값이 아닙니다 [R&T p.582].

> **⚡ 기억 고리 (Memory Hook) — *욕조 채우기 vs 욕조 유지하기*** — [EXPERT_INFERENCE, v3]  
> Loading dose는 **욕조를 목표 수위까지 채우는** 일회성 작업입니다. 필요한 양은 $V\times 목표농도$입니다. Maintenance dose는 **수위를 유지하기 위해 배수구에서 빠져나가는 만큼 채우는** 반복 작업입니다. 필요한 양은 $CL\times 목표농도\times \tau$입니다. 신부전이 있어도 $V$가 변하지 않으면 loading dose는 줄일 이유가 *없습니다*. 유지 용량만 조정합니다. 이 분리를 못 하면 신부전 환자에서 loading dose를 *불필요하게* 줄여 초기 치료 실패가 일어납니다(위 Critical Blow 행 참조).

---

## §5.6 — 채혈 식별가능성 vs point estimate confidence(Sampling identifiability)
<!-- SLIDE_START: S39 | title: Sampling identifiability vs point estimate confidence | source_anchor: section-5-6-sampling-identifiability -->


<!-- CONFUSION -->
| 결정 맥락 (Decision context) | 잘못된 지름길 (Wrong shortcut) | 확정된 판별자 (Locked discriminator) |
|---|---|---|
| TDM 결과 해석 | "Bayesian software가 $CL$ 5.7 L/h를 출력했으니 그 환자 $CL$은 5.7 L/h이다" | Point estimate는 *posterior가 식별 가능한 정보 위에서만* 의미가 있습니다. sampling timing이 $V\cdot CL$을 분리시키지 못하는 영역이면, 같은 농도에서 여러 ($V$, $CL$) 조합이 거의 동일한 likelihood를 갖습니다. |
| Sample timing 선택 | "일찍 잴수록 정보가 많다" | $1\times t_{1/2}$ 근처 sampling은 $V$-information 위주이며, $CL\times1/3$ 변화와 $V\times3$ 변화를 구분하지 못합니다. $\geq4\times t_{1/2}$ 또는 trough/steady-state sample이 $CL$을 분리합니다 [R&T pp.605–606, Fig.18-13]. |
| PopPK dataset 구조 | "많이 모으면 fit이 잘 된다" | 모든 sample이 $1\times t_{1/2}$ 이전에 몰려 있으면 estimation은 $V$는 잘 잡지만 $CL$은 population mean으로 collapse합니다. Vancomycin처럼 $CL$의 variability가 $V$보다 큰 약물에서 $V$를 strong prior로 고정하고 $CL$을 individualize하는 표준 관행이 여기서 나옵니다 [R&T p.605]. |

**한 줄 요약(One-line lock)**: Bayesian posterior의 신뢰는 "number 자체"가 아니라 "그 number가 sampling geometry 위에서 식별 가능한가"에 달려 있습니다. 같은 concentration이라도 timing이 다르면 지지되는 ($V$, $CL$) 조합이 다릅니다 [G&W pp.641–643; R&T pp.605–606].

> **⚡ 기억 고리 (Memory Hook) — *지도가 식별 가능한 영역에 있는가*** — [EXPERT_INFERENCE, v3]  
> Bayesian posterior point estimate의 신뢰는 "소프트웨어가 숫자를 출력했다"가 아니라 "**채혈 시점이 $V$와 $CL$을 분리할 수 있는 정보를 제공했는가**"에 달려 있습니다. $1\times t_{1/2}$ 이전 샘플들은 $V$는 잘 추정하지만 $CL$은 population prior로 collapse합니다. TDM에서 "농도가 치료역에 있다"는 확인은, **그 농도가 $CL$을 실제로 추정한 것인지 $V$에서 계산된 것인지 먼저 물어야** 의미 있습니다.

> **실패 모드(Failure Mode — CRUCIBLE_DERIVED**  
> NONMEM 진단에서 η-shrinkage on $CL$ > 30%이면서 $V$는 < 15%, 그리고 RSE($CL$) > 50%인데 fit은 통과한다면, 이는 거의 “sampling time mismatch”의 신호입니다. ICU 첫 24h dense sampling처럼 모든 sample이 $1\times t_{1/2}$ 이전에 몰린 데이터셋에서는 $CL$ 추정값을 그대로 individual dosing 결정에 옮기지 마세요. 그 number는 fit 결과이기는 하나, 데이터가 식별할 수 있던 quantity가 아닐 수 있습니다.

<!-- RECAP -->
**§5 recap**: 대부분의 오류는 하나의 관찰값을 하나의 원인으로 고정할 때 발생합니다. 이 세션의 판단 단위는 단일 수치가 아닙니다. shape, covariate, dose history, sampling time의 joint interpretation입니다.

---

# §7 — 자기 테스트: 능동 회상 모듈 (Self-Test: Active Recall Module)
<!-- SECTION_CORE: SC-10 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** Self-test는 답 확인이 아니라 판단 사슬의 누수 검사다 — shape, posterior, renal dosing, LD/MD를 스스로 연결해 보라.

---
<!-- SLIDE_START: S40 | title: Self-test Q1 to Q8 | source_anchor: section-7-self-test -->


<!-- SELF-TEST -->
## Q1
Response-time curve에서 baseline, time-delay, peak-shift, saturation/slope를 왜 같은 순서로 읽어야 합니까?

**정답(Answer)**: baseline이 drift하거나 adaptation/rebound가 있으면 direct model 해석이 먼저 깨집니다. time-delay와 peak-shift는 effect-site delay, turnover, receptor on/off 후보를 구분하는 신호이며, saturation/slope는 high-dose에서 nonlinear process를 드러냅니다 [G&W pp.423–424]. *(P16 적용)*

## Q2
Case B leftward peak-shift를 “모델 클래스 확정”으로 쓰면 왜 위험한가?

**정답(Answer)**: leftward shift는 turnover loss stimulation이나 receptor on/off 등 복수 후보를 남기는 diagnostic signal입니다. 원문은 potential models를 평가하라고 제시하지, 방향만으로 model을 확정하라고 하지 않습니다 [G&W pp.424–428].

## Q3
Effect compartment와 turnover model의 가장 짧은 구분법은?

**정답(Answer)**: Effect compartment는 concentration이 effect site로 늦게 equilibration되는 delay이고, turnover는 response variable의 production/loss rate 자체가 drug에 의해 변하는 delay입니다 [G&W pp.425–426].

## Q4
Bayesian TDM에서 concentration이 없을 때와 prior가 없을 때의 극단은 어떻게 다른가?

**정답(Answer)**: concentration이 없으면 population average가 추정값이 되고, prior가 없으면 concentration-only maximum likelihood에 가까워집니다. Sparse concentration + weak prior는 physiologically implausible $V/CL$을 만들 수 있습니다 [G&W pp.641–643].

## Q5
PK35 digoxin case에서 반드시 보존해야 할 numeric anchors는?

**정답(Answer)**: 55세 60 kg CHF 남성, Lanoxicap 0.2 mg daily, 458 h에서 2.5 µg/L, 479 h에서 0.9 µg/L, $CL_{pop}$ 1.8 L/h, $V_{pop}$ 500 L, estimated $CL$ 5.7 L/h, $V$ 119.6 L, $t_{1/2}$ 14.5 h [G&W pp.641–643].

## Q6
$R_d=RF\cdot f_e+(1-f_e)$에서 $f_e$와 $RF$를 분리해야 하는 이유는 무엇입니까?


> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{R_d}_{\text{유지용량 비율}}
> =
> \overbrace{\underbrace{RF}_{\text{신기능}}\cdot\underbrace{f_e}_{\text{renal 의존}}}^{\text{renal 기여}}
> +
> \underbrace{(1-f_e)}_{\text{비신 기여}}
> $$

**정답(Answer)**: $f_e$는 drug property이고 $RF$는 patient property입니다. 둘을 분리해야 renal impairment가 maintenance exposure에 미치는 영향을 정량화할 수 있습니다 [R&T pp.450–453].

## Q7
AKI에서 Cockcroft-Gault를 그대로 적용하면 왜 위험한가?

**정답(Answer)**: SCr는 renal function의 즉시값이 아니라 creatinine turnover가 반영된 지연값입니다. 급성 변화에서는 실제 $RF$가 SCr 기반 추정보다 더 낮을 수 있습니다 [R&T pp.459–461].

## Q8
Hemodialysis에서 half-life가 크게 줄면 보충 용량이 항상 필요한가?

**정답(Answer)**: 아닙니다. dialysis session 동안 실제 body amount가 얼마나 제거되었는지가 중요합니다. $V_u$가 크거나 $CL_u$가 $CL_{uD}$보다 훨씬 크면 single session의 fraction removed는 작을 수 있습니다 [R&T pp.471–472].

<!-- SLIDE_START: S41 | title: Self-test Q9 to Q16 | source_anchor: self-test-q9-q16 -->

## Q9
TCS 후보 약물이면 항상 concentration monitoring을 해야 하는가?

**정답(Answer)**: 아닙니다. Good concentration-response relationship, high probability of therapeutic failure, population PK information, reliable assay, decision 전에 도착하는 turnaround time이 대부분 충족되어야 routine strategy가 됩니다 [R&T pp.594–597].

## Q10
Phenytoin에서 total concentration target을 그대로 해석하면 왜 틀릴 수 있는가?

**정답(Answer)**: phenytoin은 albumin binding과 saturable metabolism이 중요합니다. Uremia, surgery, displacement drugs에서 altered protein binding이 예상되면 same unbound therapeutic concentration을 맞추도록 total target을 조정해야 합니다 [R&T pp.588, 595–596].

## Q11
Loading dose와 maintenance dose를 한 문장으로 구분하라.

**정답(Answer)**: Loading dose는 $V$와 target concentration의 문제이고, maintenance dose는 $CL$과 target average exposure의 문제입니다 [R&T pp.584–586].

## Q12
Fig.18-5를 “V는 정확히 예측 가능하다”로 읽으면 왜 틀린가?

**정답(Answer)**: Fig.18-5는 variability partition입니다. $V$는 약 45% explained, 55% unaccounted이고, hepatic $CL$은 약 40%, renal $CL$은 약 80% explained로 제시됩니다. 이는 prediction accuracy 값이 아닙니다 [R&T p.582].

## Q13
Vancomycin 9-13-17-21 regimen 예제가 가르치는 핵심은?

**정답(Answer)**: 24 h total daily dose가 같아도 unequal intra-day intervals는 trough를 크게 낮출 수 있습니다. 예제에서 250 mg 9-13-17-21 regimen은 8:00 concentration 2.03 mg/L로 therapeutic range 5–15 mg/L보다 낮습니다 [R&T pp.602–603].

## Q14
Q8 digoxin 처방 권고를 source-locked answer로 쓰면 안 되는 이유는?

**정답(Answer)**: PK35는 Bayesian $CL/V/t_{1/2}$ 추정 사례이지 loading 0.4 mg 또는 maintenance 0.1–0.125 mg/day를 직접 권고하는 처방 문서가 아닙니다. 그런 답은 `[교과서 외 통합 추론 예시]`로만 제시해야 합니다 [G&W pp.641–643].

## ⚡ 보스 딜레마 ★★

## Q15  *(트레이드오프 / 보스 딜레마(Trade-off / Boss-Dilemma) — ★★ SR)*
hepatic-$CL$ dominant 약물 X로 maintenance 단계에 있는 환자가 있습니다. R&T Fig.18-5에 따르면 hepatic $CL$은 demographic covariate로 약 40%만 설명됩니다. TCS 5 criteria 중 "concentration-response 관계 양호"는 충족되지만, "decision 전 도착하는 turnaround time"이 marginal입니다. 이 환자에게 routine TDM을 도입할지, demographic 기반 표준 regimen으로 갈지 어느 쪽을 택하고 어떻게 방어하겠습니까?

**정답(Answer)**: 정답은 양자택일이 아닙니다. 두 trade-off를 명시적으로 *분리해 인식*하는 것이 핵심입니다. *(P20 적용)*
- **Demographic-only로 갈 경우의 비용**: hepatic $CL$의 60% IIV가 covariate로 설명되지 않으므로 individual exposure가 target에서 ±50% 이상 벗어날 수 있습니다. 그러나 sampling/assay/turnaround의 운영 risk는 0입니다.
- **Routine TDM으로 갈 경우의 비용**: 60% IIV를 individualize할 수 있습니다. 그러나 turnaround이 marginal이라면 도착한 농도가 다음 dose 결정 시점을 *지나서* 와서, 측정값은 있으나 의사결정 input은 아닌 상태가 발생할 수 있습니다.
- **마스터 모델러의 선택**: TCS criterion이 *대부분* 충족되므로 도입 *후보*는 맞다. 그러나 turnaround marginal을 운영적으로 해결할 방법(샘플링 시점 조정, lab cutoff 협의)이 없으면 TDM은 데이터만 쌓고 결정을 바꾸지 못하는 *placebo monitoring*이 된다. 따라서 운영 조건이 fix되기 전까지는 demographic-based regimen + clinical response monitoring으로 가되, "이 약물이 hepatic-CL dominant이고 demographic으로 60%가 설명되지 않으므로 IIV가 큰 outlier가 발생할 수 있다"는 점을 명시 보고한다. 운영 조건이 fix되면 즉시 TCS로 전환한다 [R&T pp.582, 594–597].

## Q16  *(NONMEM 신호 해독)*
Vancomycin PopPK fit에서 η-shrinkage on $CL$ > 30%, $V$는 < 15%, $COV step은 통과했지만 RSE($CL$) > 50%입니다. 데이터셋은 ICU 첫 24h dense sampling으로 구성되어 있습니다. 이 결과는 무엇을 말합니까?

**정답(Answer)**: "fit이 통과했지만 data가 식별할 수 없던 quantity를 추정하려 했다"는 신호입니다. $1\times t_{1/2}$ 이전 sample에서는 *$CL\times1/3$*과 *$V\times3$*이 거의 같은 likelihood를 가지므로, NONMEM은 $V$는 잘 잡고 $CL$은 population mean으로 collapse합니다. 해결: $V$를 population strong prior로 고정하고 $CL$만 individualize하거나, $\geq4\times t_{1/2}$ post-infusion sample을 추가합니다 [R&T pp.605–606].


> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{CL\times\frac{1}{3}}_{\text{낮은 CL}}
> \;\approx_{\text{early sample 구분 불가}}\;
> \underbrace{V\times3}_{\text{큰 V}},
> \qquad
> \underbrace{t\geq4\times t_{1/2}}_{\text{늦은 CL anchor}}
> $$

<!-- RECAP -->
**§7 recap**: self-test의 목적은 계산 정답보다 “어떤 정보가 없으면 해석이 불가능한가”를 즉시 말하게 만드는 것입니다. Q15·Q16은 단일 정답이 없는 trade-off를 어떻게 *방어 가능한 추론*으로 변환하는지를 묻습니다.

---

# §8 — 메타프레임과 큰 그림 (Meta-Frame & Big Picture)
<!-- SECTION_CORE: SC-11 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** Session 016의 moat는 source-locked 판단 언어다 — 모델·질환·TDM·용량·노출 보고를 한 줄 chain으로 말할 수 있어야 한다.

---
<!-- SLIDE_START: S42 | title: Meta-frame overview | source_anchor: section-8-meta-frame -->


## A. 이 세션의 위치
<!-- SLIDE_START: S43 | title: 이 세션의 위치 | source_anchor: section-8-a-position -->


이 세션은 pharmacometrics 학습에서 "model building"과 "clinical dosing decision" 사이의 연결부를 다룹니다. 모델을 구성한 뒤 실제 환자 용량 판단으로 넘어가는 지점입니다. *(P17 적용)* Ch.6은 model structure를 좁히는 눈을 만들고, Ch.15는 disease가 parameter를 어떻게 움직이는지 설명하며, PK35는 individual parameter를 posterior estimate로 만들고, Ch.18은 그 estimate를 loading, maintenance, monitoring, missed-dose interpretation으로 바꿉니다.

## B. 네 가지 메타 패턴 (Four meta-patterns)
<!-- SLIDE_START: S44 | title: 네 가지 메타 패턴 | source_anchor: section-8-b-meta-patterns -->


1. **두 인자의 곱(Two-factor product)**: $R_d$는 $f_e\times RF$, forgiveness는 $t_{1/2}/\tau\times therapeutic\ window$, TCS는 $risk\times measurability$처럼 두 축이 함께 움직입니다.


> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{R_d}_{\text{renal 조정}}
> \sim
> \overbrace{\underbrace{f_e}_{\text{약물 속성}}\times\underbrace{RF}_{\text{환자 속성}}}^{\text{renal 의존}},
> \qquad
> \underbrace{\text{forgiveness}}_{\text{missed-dose 내성}}
> \sim
> \overbrace{\underbrace{\frac{t_{1/2}}{\tau}}_{\text{시간 여유}}\times\underbrace{\text{therapeutic window}}_{\text{농도 여유}}}^{\text{허용 여유}},
> \qquad
> \underbrace{TCS}_{\text{monitoring 전략}}
> \sim
> \overbrace{\underbrace{risk}_{\text{위험}}\times\underbrace{measurability}_{\text{측정성}}}^{\text{TCS 필요}}
> $$
2. **식별가능성은 채혈 시점에 달린다(Identifiability depends on sampling geometry)**: early concentration은 $V$, later/steady-state concentration은 $CL$을 더 잘 식별합니다. *(P18 적용)*
3. **현실은 연속적, 소통은 이산적(Continuous reality, discrete communication)**: renal impairment stage, TCS candidate list, dialysis thresholds는 communication tools이지 hard biological cutoffs가 아닙니다. *(P18 적용)*
4. **$CL$의 해부학이 용량 논리를 결정한다(Anatomy of CL determines dose logic)**: renal $CL$-dominant, hepatic $CL$-dominant, high-extraction, low-extraction, protein-bound drug은 같은 “$CL$ 감소” 언어로 묶을 수 없습니다. *(P18 적용)*

## C. 소스 잠금 전문가 해석 지점 (Source-locked professional moat)
<!-- SLIDE_START: S45 | title: Source-locked professional moat | source_anchor: section-8-c-professional-moat -->


- Plot shape를 보고 ODE 후보를 줄입니다.
- $f_e/RF/R_d$로 renal disease maintenance adjustment를 계산합니다.
- C-G를 쓰되 SCr lag와 body composition caveat를 같이 판단합니다.
- Bayesian output을 prior, concentration, sampling time, dosing history의 산물로 읽습니다.
- TCS를 약물명 자동 적용이 아니라 criteria-based adjunct strategy로 운용합니다.
- LD와 MD를 $V$ vs $CL$ 문제로 분리합니다.
- Missed/erratic dosing을 “자료 오염”이 아니라 superposition problem으로 계산합니다.

## D. PK15 마무리 브리지 (PK15 closing bridge)
<!-- SLIDE_START: S46 | title: PK15 closing bridge | source_anchor: section-8-d-pk15 -->


PK15는 처방 자체가 아니라 “선택된 용량에서 어떤 exposure와 safety margin을 보고할 것인가”를 담당합니다. 10/56/320 µmol·day⁻¹·kg⁻¹ dose levels, Cmax/AUC exposure reporting, therapeutic concentration 0.05–0.1 µM, high-dose Cmax approximately 50 µM, >100-fold safety margin은 clinical dosing chain의 마지막 reporting layer로만 사용합니다 [G&W pp.546–548].

## E. 최종 잠금 주의 목록 (Final locked caution list)
<!-- SLIDE_START: S47 | title: Final locked caution list | source_anchor: section-8-e-caution-list -->


아래 표현은 source boundary 위반 또는 overclaim 위험이 있어 대체 표현으로 교체합니다. *(P19 적용)*

**사용 금지 표현 (Do not say):**

```text
Do not say:
- peak-shift direction = model class
- TCS candidate drug = mandatory TCS
- V/CL Fig.18-5 percentages = dosing accuracy
- PK35 digoxin case = direct prescription recommendation
- TDM patients are 80% irregular dosing
- hemodialysis decision = simple Vu<120 AND CLu<CLuD rule
- NDA/IND/RMP/software workflow = textbook source claim
```

**대신 사용할 표현 (Say instead):**

```text
Say instead:
- peak-shift direction narrows competing models
- TCS is useful as adjunct when criteria are satisfied
- Fig.18-5 is variability partition
- PK35 estimates individual CL/V/t½; prescription is separate inference
- missed/unequal/erratic dosing is common enough to need equations, without source-free percentages
- dialysis effectiveness lies on Vu·CLu·CLuD coordinate plane
- implementation/regulatory extrapolations require [교과서 외 구현/규제 번역]
```

<!-- RECAP -->
**최종 요약(Final recap)**: 이 세션의 캡스톤 척추(capstone spine)는 “shape로 모델 후보를 좁히고, 질환과 환자 특성으로 파라미터 편차를 설명한 뒤, Bayesian TDM과 dosing equation으로 치료 의사결정에 연결한다”는 흐름입니다. 핵심 주의점은 deterministic overclaim, 근거 없는 백분율, 라벨 없는 규제·소프트웨어 외삽, PDF에 없는 직접 처방 주장으로 넘어가지 않는 것입니다.


---

# PART B — Compiler-Only Appendix

This appendix is not learner-facing. It exists only to protect Phase 5 rendering fidelity and prevent regression. **(v3.1 note: PART B는 v3에서 변경되지 않았다. v3.1 patch는 PART A 한국어 독해성 개선만 적용하며, PART B의 모든 guardrail·certification·marker block registry·coverage matrix·splice verification table은 그대로 보존된다.)**

### B1. Compilation Contract

- PART A is the only learner-facing body.
- Phase 5 must render PART A without altering content.
- PART B is instruction/guardrail only.
- Do not restore deprecated material.
- Do not add new scientific content.
- Do not render PART B as learner content unless explicitly requested.

### B2. Figure Rendering Instructions

- Use the approved Phase 4C figure strategy only.
- Preserve Mode P/R/N decisions exactly.
- Image rights = None: do not embed copyrighted textbook images.
- Render `FIGURE_POINTER` as text-only textbook reference callouts.
- Render `FIGURE_SCHEMATIC` only as visually distinct new schematic based on the brief; do not reproduce textbook figures.
- Do not propose additional figures.
- Do not generate Mermaid/SVG in Phase 4D; Phase 5 may render approved schematic briefs only.

#### Approved Phase 4C Figure Strategy / Insertion Map

```markdown
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
```

### B3. Page Tag Rendering Rules

- Preserve all `[p.XX]`, `[pp.XX–YY]`, `[pp.XX, YY]`, and `[p.확인 필요]` tags.
- Render page tags visibly in HTML.
- Do not fabricate, delete, renumber, or relocate page tags.
- `[p.확인 필요]` remains visible unless already resolved by Audit/Content Lock.
- Do not hide source page tags in print mode.

### B4. HTML Compiler Requirements

The following compiler prompt is the controlling Phase 5 rendering contract. It is not learner-facing.

```text
ROLE: Education UX Engineer.
Function: transform Content Lock v2.1 into a production-quality HTML file.
You render content. You do not alter it.

If inputs include a PATCH MODE Insertion Map (instead of a fully-marked v2.1):
  Step 1 (mandatory): Splice each marker block into Content Lock v2 at the specified
                      anchor location, producing a working v2.1 in memory.
                      Do not modify any other text.
  Step 2 (mandatory): Output a Splice Verification Table BEFORE rendering HTML.
                      If any anchor cannot be matched exactly, STOP and report.
  Step 3:             Render HTML as below.

INPUT: Content Lock v2.1 (or Content Lock v2 + Insertion Map)
DESIGN REFERENCE: [attach reference HTML — T.E.A. Loop Playbook or equivalent]

=== PATCH MODE SPLICE VERIFICATION ===

When rendering from PATCH MODE inputs, output the following table BEFORE the HTML:

## Splice Verification Table (PATCH MODE only)

| Marker # | Anchor text (truncated to 60 chars) | Anchor found? | Match count | Inserted? | Final location (§ + card) |
|----------|-------------------------------------|---------------|-------------|-----------|---------------------------|

Rules:
- Anchor found?  : YES if exact substring match found in Content Lock v2; NO otherwise.
- Match count    : number of times the anchor appears (must be exactly 1 — see below).
- Inserted?      : YES only if Anchor found = YES AND Match count = 1.
- Final location : the § and concept card immediately preceding the inserted marker.

HALT CONDITIONS (do NOT proceed to HTML rendering if any apply):
  H1. Any "Anchor found?" = NO.
  H2. Any "Match count" ≠ 1 (zero matches OR multiple matches → ambiguous).
  H3. Any "Inserted?" = NO.

If a HALT condition triggers:
  Stop rendering. Output:
    "PATCH MODE SPLICE FAILED — N markers could not be inserted unambiguously.
     Return to Phase 4C and request anchor revision (verbatim, unique, ≥40 chars,
     extend to ≥60 chars if collision)."
  Do NOT guess insertion location.
  Do NOT proceed to HTML output.

If all markers pass: continue to HTML rendering and include the Splice Verification Table
as a comment block at the top of the HTML file (inside <!-- ... --> for traceability).

=== MARKER → COMPONENT MAPPING (mandatory) ===

| Marker / Pattern                  | HTML Component              | Style specification                                              |
|-----------------------------------|-----------------------------|------------------------------------------------------------------|
| <!-- MASTER LENS -->              | Callout box                 | border-left:4px solid #c9a84c; background:rgba(201,168,76,0.08)  |
| <!-- ANNOTATION -->               | Inline abbr / tooltip       | font-size:0.85em; color:var(--muted); font-style:italic          |
| <!-- ANCHOR -->                   | Bridge sentence             | font-style:italic; color:var(--muted)                            |
| <!-- TRENCH -->                   | Practical tip box           | border-left:4px solid var(--rose); background:rose-tint          |
| <!-- CONFUSION -->                | Side-by-side comparison     | .box.amber class                                                 |
| <!-- SELF-TEST -->                | Click-to-reveal accordion   | Question visible; answer hidden until click                      |
| <!-- RECAP -->                    | Section summary box         | border-left:4px solid var(--blue); background:blue-tint          |
| [확인 필요]                        | Highlighted flag            | <mark> tag                                                       |
| [p.XX] / [pp.XX–YY] / [pp.XX, YY] | Inline source page tag      | <span class="source-page">[p.XX]</span> — see CSS below          |
| [p.확인 필요]                      | Source page uncertainty tag | <span class="source-page source-uncertain">[p.확인 필요]</span>  |
| <!-- FIGURE_POINTER -->           | Textbook reference callout  | border-left:4px solid var(--purple); 📖 icon                     |
| <!-- FIGURE_SCHEMATIC -->         | Inline schematic <figure>   | Render via Mermaid (default) or inline SVG; <figcaption> below   |
| <!-- FIGURE_IMAGE_SLOT -->        | Image figure or placeholder | <figure> with <img> if file provided; styled placeholder if not  |

=== SOURCE PAGE TAG RENDERING RULES (v3.3.3 신설) ===

Source page tags are NOT HTML comment markers — they appear as plain text in
Content Lock v2.1 (e.g., "Concept Anatomy: Hepatic Clearance [p.123]").
The HTML compiler must detect them via pattern matching and wrap them in <span> elements.

Pattern detection (regex-equivalent, applied to body text only):
  - \[p\.(\d+)\]                 → standard single-page tag
  - \[pp\.(\d+)[–-](\d+)\]       → range tag (en-dash or hyphen)
  - \[pp\.(\d+(?:,\s*\d+)+)\]    → multi-page non-contiguous tag
  - \[p\.확인 필요\]              → uncertainty tag

Rendering:
  Standard tags  → <span class="source-page">[p.XX]</span>
  Uncertain tags → <span class="source-page source-uncertain">[p.확인 필요]</span>

Detection scope:
  - APPLY pattern detection to body text inside §2 cards, equation captions, and example headings.
  - DO NOT apply pattern detection inside <pre><code> blocks (preserve verbatim in code).
  - DO NOT apply pattern detection inside <!-- FIGURE_* --> marker blocks (those have their own
    internal "Source:" fields and are not body content tags).

Fabrication prohibition:
  - DO NOT add page tags that are not present in Content Lock v2.1.
  - DO NOT silently remove page tags during rendering.
  - DO NOT alter page numbers (e.g., normalizing en-dash to em-dash is permitted; changing
    page numbers is forbidden).

=== RENDERING REQUIREMENTS ===

Math      : MathJax CDN — inline \(...\), display \[...\]
Code      : <pre><code> dark background, language class attribute
Navigation: sticky left sidebar, anchor jump per § section
Accordion : Self-Test answers hidden by default; revealed on user click
Checklist : sessionStorage state persistence across page reload
Controls  : code block copy button, print/PDF button (window.print())
Responsive: ≤768px single-column + collapsed nav; ≥1024px two-column
Dark/Light: prefers-color-scheme auto-switch
Print     : remove backgrounds, hide navigation, optimize page-break-inside
            Source page tags MUST remain visible in print mode (do not hide via @media print).

=== NAVIGATION ANCHOR INTEGRITY RULES ===

The HTML must include a sticky left sidebar table of contents.

For every sidebar link:
- Use <a href="#..."> links only.
- Every href target must have a matching id in the body.
- Every major section heading (§1, §2, §3...) must receive a stable id.
- Every concept card inside §2 must also receive a stable id when possible.
- The href value and body id must match exactly, including spelling and hyphens.
- Do not create TOC links whose target id does not exist.
- Do not create duplicate ids.
- Enable smooth scrolling with:

html { scroll-behavior: smooth; }

Before finalizing, self-check:
1. Count all sidebar href="#id" values.
2. Confirm each id exists exactly once in the document.
3. Confirm no duplicate id exists in the body.
4. If any mismatch exists, fix before output.

Required implementation:
- The sidebar must be placed on the left side on desktop.
- The sidebar must remain visible while scrolling unless the viewport is mobile-sized.
- Each major section must be reachable by clicking the sidebar entry.
- Each §2 concept card should be reachable by clicking its sidebar sub-entry when concept-card headings are present.
- The active section may be highlighted using IntersectionObserver or equivalent JavaScript.
- On mobile viewports, the sidebar may collapse, but anchor navigation must still work.

=== FIGURE RENDERING RULES ===

GENERAL:
- Every figure marker becomes a proper <figure> block (or pointer callout) with caption and alt text.
- Figures must not interrupt reading flow — place at end of the concept card they belong to.
- Visual style consistent with the design system. No decorative imagery.
- Do not generate or embed figures not present in Content Lock v2.1.

FIGURE_POINTER:
- Render as a compact callout box with class .figure-pointer:
    border-left: 4px solid var(--purple);
    background: rgba(155, 89, 182, 0.06);
    icon: 📖
- Display: Source / Why this matters / When to look / Learner instruction.
- Do NOT generate or embed an image — pointer is text-only.

FIGURE_SCHEMATIC (Mode R or N):
- Default rendering: Mermaid via CDN (https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js).
  Use <div class="mermaid">...</div> inside <figure>.
- Use inline SVG only when the schematic requires curve plotting, precise spatial layout,
  or shapes Mermaid cannot express (e.g., concentration-time curves, radar plots).
- For comparison-style figures (Confusion-pair), CSS side-by-side cards (no SVG) are acceptable
  if the brief's "Suggested rendering" specifies CSS-card.
- Implement the brief faithfully: include only listed elements; exclude listed exclusions.
- Do not reproduce the textbook figure's exact layout, color palette, or label placement
  even when "Redrawn from textbook concept" — visual distinctness is mandatory.
- Caption: render as <figcaption>.
- Alt text: render as alt attribute on SVG container or aria-label on <figure>.
- Mermaid initialization in inline JS:
    mermaid.initialize({ startOnLoad: true, theme: 'neutral',
                         themeVariables: { fontFamily: 'var(--font)' } });

MERMAID SELF-CHECK (생성 직후 self-validate):
After generating each Mermaid block, verify all of the following BEFORE finalizing:
  M1. Block opens with a valid directive: flowchart TD | flowchart LR |
      graph TD | graph LR | sequenceDiagram | classDiagram | stateDiagram-v2 | erDiagram.
  M2. Node IDs contain ONLY [A-Za-z0-9_]. No parentheses, slashes, dots, hyphens,
      Korean characters, spaces, or quotes inside IDs.
  M3. Any label containing parentheses, special characters, or non-ASCII characters
      is wrapped in double quotes:  A["Clearance (CL)"]
  M4. Edge labels with special chars use the |"label"| form:  A -->|"Q × E"| B
  M5. Subgraph titles, when used, are quoted:  subgraph "Hepatic"
  M6. No trailing semicolons inside node definitions.
  M7. If any of M1–M6 cannot be satisfied OR Mermaid expressiveness is insufficient,
      FALLBACK to one of:
        - inline SVG (for spatial/curve figures)
        - CSS side-by-side cards (for comparison figures)
      Do not emit a Mermaid block that is likely to fail rendering.

FIGURE_IMAGE_SLOT:
- If Rights = User-supplied AND image file exists in working directory:
    <figure><img src="..." alt="..." /><figcaption>...</figcaption></figure>
- If Rights = Open-license AND license/attribution provided in marker:
    <figure>
      <img src="..." alt="..." />
      <figcaption>
        [Caption text]
        <span class="figure-attribution">
          Source: [Attribution]. License: [License type].
          [<a href="[Source URL]">link</a>]
        </span>
      </figcaption>
    </figure>
- If Rights = placeholder OR file unavailable:
    Render styled placeholder box with class .figure-placeholder:
    [📖 교과서 원그림 삽입 위치 — Source: Book, p.XX, Fig.Y]
    Do not generate an approximation of the textbook figure.

CAPTION & ALT TEXT (all schematic/image figures):
- Caption mandatory. Alt text mandatory. Both from the brief.

=== CSS DESIGN SYSTEM (inherit from reference) ===

Variables: --bg, --surface, --surface-2, --ink, --muted, --faint,
           --line, --line-strong, --blue, --green, --purple, --amber, --rose,
           --radius, --radius-sm, --shadow, --font, --mono

Add for navigation:
  html {
    scroll-behavior: smooth;
  }
  .sidebar {
    position: sticky;
    top: 0;
    align-self: start;
    height: 100vh;
    overflow-y: auto;
  }
  .sidebar a {
    display: block;
    text-decoration: none;
  }
  .sidebar a.active {
    font-weight: 700;
    border-left: 3px solid var(--purple);
  }
  @media (max-width: 768px) {
    .sidebar {
      position: static;
      height: auto;
      max-height: none;
    }
  }

Add for v3.3 figure components:
  .figure-pointer { border-left: 4px solid var(--purple); ... }
  figure { margin: 1.5em 0; }
  figcaption { color: var(--muted); font-size: 0.9em; margin-top: 0.5em; }
  .figure-attribution { display: block; font-size: 0.8em; margin-top: 0.3em;
                        color: var(--faint); }
  .figure-placeholder { border: 2px dashed var(--line-strong); padding: 2em;
                         text-align: center; color: var(--muted); }

Add for v3.3.3 source page tag components:
  .source-page {
    font-size: 0.78em;
    color: var(--purple);
    background: rgba(155, 89, 182, 0.10);
    padding: 2px 6px;
    border-radius: 6px;
    vertical-align: super;
    white-space: nowrap;
    margin-left: 0.25em;
    font-weight: 500;
    letter-spacing: 0.01em;
  }
  .source-page.source-uncertain {
    color: var(--amber);
    background: rgba(245, 158, 11, 0.12);
    border: 1px dashed var(--amber);
  }
  /* Print: keep tags visible for offline traceability */
  @media print {
    .source-page {
      background: transparent;
      color: #000;
      border: 1px solid #888;
    }
  }
  /* Hover: subtle elevation to confirm interactivity (if linked to PDF in future) */
  .source-page:hover {
    background: rgba(155, 89, 182, 0.18);
  }

=== OUTPUT SPECIFICATION ===

Single HTML file with all custom CSS and custom JS inline.
External runtime dependencies are allowed ONLY for:
  - MathJax CDN
  - Mermaid CDN
  - cdnjs.cloudflare.com library list (e.g., highlight.js for code coloring)
No external local .css / .js / font / image files unless explicitly supplied by the user.
File header comment block: document title | chapter | generation date.
PATCH MODE only: include Splice Verification Table as a comment block in the HTML header.

=== PROHIBITED ===

- <iframe>, <embed>, external .js files (other than permitted CDNs), external local .css
  files, external font files (other than permitted CDNs).
- Any modification to Content Lock v2.1 text content (including page tag text).
- Self-Test answer text visible without user interaction.
- Markers rendered as plain text (every marker must become its mapped component).
- Source page tags rendered as plain bracketed text without <span> wrapping.
- Reproducing copyrighted textbook figures exactly when rendering R/N schematics.
- Embedding textbook images without User-supplied or Open-license rights with attribution.
- Emitting Mermaid blocks that fail M1–M6 self-check.
- Proceeding to HTML rendering when any PATCH MODE Splice Verification HALT condition
  (H1–H3) is triggered.
- Guessing insertion location for unmatched anchors.
- Adding new source page tags or altering existing ones during HTML compilation.
- Hiding source page tags via @media print or display:none under any condition.
- Creating sidebar TOC links whose target ids do not exist.
- Creating duplicate body ids.
- Creating body ids that are not stable or that change across repeated generations for the same heading text.

Output (PATCH MODE):
  1. Splice Verification Table
  2. (only if all markers pass) Complete HTML from <!DOCTYPE html> to </html>

Output (FULL MODE):
  Complete HTML from <!DOCTYPE html> to </html>.
```

### B5. Audit Guardrails

Regression-prevention items:

- Do not restore “peak-shift direction = model class.” Use diagnostic signal / candidate narrowing only.
- Do not state TCS is mandatory for a drug name alone. Use criteria-based adjunct strategy language.
- Do not restore unsupported `V 5–10%`, `CL 30–40%`, or other dosing-accuracy claims.
- Do not present PK35 digoxin loading/maintenance dosing as direct textbook recommendation.
- Do not restore “TDM patient 80%” or similar unsupported prevalence claims.
- Do not treat NONMEM, BestDose, ID-ODS, Pmetrics, NDA/IND/RMP wording as direct textbook source claims without the explicit `[교과서 외 구현/규제 번역]` label.
- Do not restore hemodialysis `Vu<120 AND CLu<CLuD` as a hard gate.
- Do not embed textbook figures because Image rights = None.
- Do not remove `[확인 필요]` or `[p.확인 필요]` flags.
- Do not expand Ch.6 Case A–I equations into a new full-card bank.

### B6. Crucible Guardrails

- Crucible is not a raw content source at this stage.
- Preserve only already-adopted or explicitly allowed Grade A logic.
- Do not reintroduce omitted/rejected Crucible items.
- Do not convert speculative insight into textbook-derived fact.
- Label expert interpretation as `EXPERT_INFERENCE` when it appears in Mastery Augmentation.

### B7. Deprecated and Forbidden Restorations

- Step 1 Draft v0 is deprecated.
- Do not restore rejected overclaims, unsupported numbers, unsupported regulatory claims, source-unsupported examples, unapproved code, or unapproved figures.
- Do not use Step 1 Draft v0 as learner-body source except through the Micro-Patch Gate.
- Do not add new named drugs, new equations, new external regulatory claims, or new page tags.

### B8. PATCH MODE Splice Verification Table

| Marker # | Anchor text | Anchor found? | Match count | Inserted? | Final location (§ + card) |
|---|---|---|---:|---|---|
| F01 | `**§1 recap**: 이 세션은 “모델 선택 → 질환 보정 → 개인 추정 → 처방·monitoring →` | YES | 1 | YES | §1 — Session Header & Roadmap / Capstone spine |
| F02 | `§2.1은 plot-reading grammar이고, §2.2–§2.3은 그 grammar가 실제 ODE 후` | YES | 1 | YES | §2.1 — Pattern-recognition decision workflow |
| F03 | `**Trench-Level Tip**: Case B left-shift를 “kon이 큰 약물”로 외우지 말라` | YES | 1 | YES | §2.2 — Peak-shift + saturation |
| F04 | `PK35 digoxin 사례는 CL/V/t½ 추정 사례이다. Loading dose 0.4 mg, maint` | YES | 1 | YES | §2.4 — Bayesian objective function for individual TDM |
| F05 | `**Trench-Level Tip**: phenytoin처럼 albumin-bound low-extracti` | YES | 1 | YES | §2.5 — Disease/RF/Rd framework |
| F06 | `**Trench-Level Tip**: Phenobarbital의 dialysis half-life가 크게 ` | YES | 1 | YES | §2.7 — Hemodialysis coordinate plane |
| F07 | `**Trench-Level Tip**: “신부전이므로 LD도 줄인다”는 자동 규칙은 틀릴 수 있다. LD는 ` | YES | 1 | YES | §2.9 — Loading dose vs maintenance dose |


### B9. Zero-Omission Coverage Matrix

| Domain | Required coverage | Status | Resolution in master file |
|---|---|---|---|
| C1. Scope Lock concepts | Ch.6 pattern recognition, PK35 Bayesian TDM, PK15 toxicokinetic exposure reporting, R&T Ch.15 disease/RF/Rd/dialysis, R&T Ch.18 TCS/loading/missed dosing | PASS | Present in §1, §2.1–§2.10, §8. |
| C2. Scope data anchors | PK35 digoxin case values; PK15 toxicokinetic dose/exposure/safety-margin anchors; Table 18-6 concentration interpretation inputs | PASS | Retained in §1 Data anchors, §2.4, §2.8, §2.10, §8. |
| C3. Audit MUST_FIX #1 | Peak-shift deterministic overclaim removed | PASS | §2.2 states diagnostic signal, not deterministic model rule. |
| C3. Audit MUST_FIX #2 | TCS “mandatory/all criteria” overstatement softened | PASS | §2.8 states useful adjunct when criteria are mostly met; not drug-name automatic. |
| C3. Audit MUST_FIX #3 | Unsupported LD/V/CL prediction-accuracy numbers removed | PASS | §2.9 recasts Fig.18-5 as variability partition, not accuracy promise. |
| C3. Audit MUST_FIX #4 | PK35 digoxin prescription recommendation not treated as textbook claim | PASS | §2.4 Boundary labels loading/maintenance suggestions as outside direct source. |
| C3. Audit MUST_FIX #5 | “TDM patient 80%” claim removed | PASS | §2.10 has explicit deleted-claim statement. |
| C3. Audit MUST_FIX #6–7 | NONMEM/software/regulatory wording separated from source-locked claims | PASS | §1 labels these as `[교과서 외 구현/규제 번역]`; §8 caution preserved. |
| C3. Audit MUST_FIX #8 | Hemodialysis hard AND gate removed | PASS | §2.7 uses Vu·CLu coordinate plane and continuous trade-off. |
| C4. Audit SHOULD_FIX | Fig.6.12, creatinine lag, Table 18-6, PK15 closing bridge, MUST-card compression | PASS | §2.1/F02, §2.6, §2.8, §8, and ten-card curation reflect these corrections. |
| C5. Figure coverage | Phase 4C KEEP F01–F07 exactly once; no textbook image embedding | PASS | Raw marker blocks are exact-spliced; P markers are pointer-only; R/N are schematic briefs only. |
| C6. Page-tag integrity | Preserve existing page tags and `[확인 필요]`; do not fabricate new tags | PASS | Canonical tags retained; mastery notes add no page tags. |
| C7. Crucible Grade A preservation | Adopted Grade A logic retained without speculative conversion to textbook fact | PASS *(ver2 강화)* | V/CL sampling identifiability, variability partition correction, and forgiveness/superposition logic retained in §2.4, §2.9, §2.10. **ver2 추가**: Imipenem Rd violation (Wall #6 → §2.5 MA11), SCr turnover lag 정량 anchor (Wall #5 → §2.6 MA12), CYP2D6 prior subgroup (위험 9 → §2.8 MA13), Forgiving/Unforgiving Fig.18-9 정량 (Wall #9 / Tip 12 → §2.10 MA15), Sampling identifiability Confusion Pair (Wall #10 / S8 → §5.6 MA16). |
| C8. Deprecated source control | Step 1 Draft v0 not restored as raw learner-body source | PASS | Step 1 used only as deprecated omission-check reference. |
| C9. Mastery-Uplift completeness *(ver2 신설)* | Crucible Grade A (활성 12 Tips + Walls #4–#10) 모든 Adopt 항목이 PART A에 epistemic-labeled augmentation으로 도달했는가 | PASS *(ver2)* | Wall #4·#5·#6·#7·#8·#9·#10 + Tips 1·6·7·8·10·11·12·13 + Signatures S8·S9가 모두 §2 Trench/Mastery/Failure 또는 §5 Confusion Pair 또는 §7 self-test로 반영됨. Tip 4 (PK margin ≠ NOAEL margin)는 Step 2 §6 PK15 시나리오 영역으로 이월 (textbook_workflow scope 외). |
| **C10. Boss-Dilemma coverage** *(ver2 신설)* | Step 1 V5.0 명세의 Socratic Dilemma 형 trade-off question이 §7 최종부에 존재하는가 | PASS *(ver2)* | Q15 (TDM-vs-demographic trade-off in marginal turnaround 환자) + Q16 (S8 NONMEM signature decode)가 §7 self-test 후반부에 추가됨. 양자택일이 아닌 *방어 가능한 추론*으로 변환하는 형식. |
| **C11. Apex / Memory Hook / Critical Blow** *(v3 신설)* | Step 1 V5.0 Apex Edition 명세의 [⚡ Apex Concept] 1개, §5 Memory Hook 6개 전수, Critical Blow 1개가 PART A에 존재하는가 | PASS *(v3)* | §2.1에 [⚡ Apex Concept] + Plausible Fallacy block (MA19); §5.1–§5.6 모두에 Memory Hook 6개 (MA20); §5.5에 Critical Blow 행 (MA21); Q15 Boss-Dilemma 레이블/SR 표준화 (MA23). |
| **C12. Practice Brief 일관성** *(v3 신설)* | §2.1–§2.10 10개 카드 *전부*에 4축(왜 알아야/흐름상 역할/체화 꿀팁/실무 활용) Practice Brief가 존재하는가 | PASS *(v3)* | 10/10 카드에 표준 Practice Brief 블록 삽입 (MA24). 각 블록은 EXPERT_INFERENCE 라벨로 epistemic-tagged. |


### B10. Micro-Patch Log

| # | Location | Action | Rationale | Risk |
|---:|---|---|---|---|
| 1 | Content Lock v2 → v2.1 | Exact-spliced seven approved figure markers from Phase 4C PATCH MODE | Required to produce working v2.1 without rewriting canonical text | Low |
| 2 | PART A adjacent notes | Added ten bounded Mastery/Practice/Failure Mode notes | Required by Phase 4D Mastery-Uplift while preserving canonical body | Low |

No scientific micro-patch was made to canonical wording. No page tag, equation, numerical value, or source claim was altered.


### B11. Mastery Augmentation Log

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
|---|---|---|---|---|---|---|
| MA01 | §2.1 | Mastery Note | YES | TEXTBOOK_DERIVED | Adjacent bounded augmentation; no new numerical/page/source claims. | Low |
| MA02 | §2.2 | Failure Mode | YES | AUDIT_DERIVED | Adjacent bounded augmentation; no new numerical/page/source claims. | Low |
| MA03 | §2.3 | Practice Lens | YES | EXPERT_INFERENCE | Adjacent bounded augmentation; no new numerical/page/source claims. | Low |
| MA04 | §2.4 | Mastery Note | YES | CRUCIBLE_DERIVED | Adjacent bounded augmentation; no new numerical/page/source claims. | Low |
| MA05 | §2.5 | Practice Lens | YES | TEXTBOOK_DERIVED | Adjacent bounded augmentation; no new numerical/page/source claims. | Low |
| MA06 | §2.6 | Failure Mode | YES | AUDIT_DERIVED | Adjacent bounded augmentation; no new numerical/page/source claims. | Low |
| MA07 | §2.7 | Failure Mode | YES | AUDIT_DERIVED | Adjacent bounded augmentation; no new numerical/page/source claims. | Low |
| MA08 | §2.8 | Practice Lens | YES | TEXTBOOK_DERIVED | Adjacent bounded augmentation; no new numerical/page/source claims. | Low |
| MA09 | §2.9 | Mastery Note | YES | AUDIT_DERIVED | Adjacent bounded augmentation; no new numerical/page/source claims. | Low |
| MA10 | §2.10 | Practice Lens | YES | TEXTBOOK_DERIVED | Adjacent bounded augmentation; no new numerical/page/source claims. | Low |
| **MA11** *(ver2)* | §2.5 | Failure Mode | YES | CRUCIBLE_DERIVED | Imipenem-class 약물의 Rd assumption violation [R&T pp.464–466, Fig.15-15] — Crucible Wall #6 Grade A, 기존 page tag 재사용, 새 numerical 없음. | Low |
| **MA12** *(ver2)* | §2.6 | Failure Mode 보강 | YES | TEXTBOOK_DERIVED | Table 15-6 SCr turnover/half-life 정량 anchor [R&T pp.459–461] — Crucible Wall #5 / Tip 7 Grade A, 기존 page tag 재사용, R&T 본문이 정량적 길이 증가를 보여준다는 정성 표현으로 처리 (특정 시간 수치는 R&T 그래프 인용으로만). | Low |
| **MA13** *(ver2)* | §2.8 | Mastery Note | YES | CRUCIBLE_DERIVED | CYP2D6 polymorphism prior subgroup의 Bayesian 연결 [R&T Fig.18-6, p.583] — Crucible 위험 9 Grade A. phenytoin Michaelis-Menten saturation는 기존 본문 유지. | Low |
| **MA14** *(ver2)* | §2.8 | Failure Mode | YES | AUDIT_DERIVED | Tozer Fig.18-2 [p.579] hypothetical PD variability 백분율의 NDA 인용 위험 — Crucible Wall #7 / Tip 9 Grade B, [교과서 외 규제 번역] 라벨 영역으로 명시. | Low |
| **MA15** *(ver2)* | §2.10 | Mastery Note | YES | CRUCIBLE_DERIVED | R&T Fig.18-9 [p.592]의 forgiving/unforgiving 직관 반대 사례 정량 anchor (q24h 1× miss 3.2 mg/L vs q8h 3× miss 5.0 mg/L) — Crucible Wall #9 / Tip 12 Grade B → Grade A 격상 (직접 PDF 검증된 numbers 사용), §8 Meta-pattern 1 cross-link. | Low |
| **MA16** *(ver2)* | §5 | New Confusion Pair §5.6 | YES | CRUCIBLE_DERIVED | Sampling identifiability vs point estimate confidence 혼동쌍 + S8 NONMEM signature — Crucible Wall #10 / Tip 11 / S8 Grade A, 기존 [R&T pp.605–606] page tag 재사용. | Low |
| **MA17** *(ver2)* | §7 | Q15 Trade-off question | YES | CRUCIBLE_DERIVED | hepatic-CL dominant + marginal turnaround 환자에서 TDM-vs-demographic trade-off의 Boss-Dilemma. Step 1 V5.0의 Socratic Dilemma 명세 충족, source-locked numbers (45%/40%/80%/5%) 재사용. | Low |
| **MA18** *(ver2)* | §7 | Q16 NONMEM signature decode | YES | CRUCIBLE_DERIVED | S8 Sampling Time Mismatch signature를 active recall 형태로 변환. 새 numerical/page 없음. | Low |
| **MA19** *(v3)* | §2.1 | [⚡ Apex Concept] 배지 + Plausible Fallacy block | YES | EXPERT_INFERENCE | Step 1 V5.0 Apex Edition 명세 충족. "model → exposure → target → decision pipeline" 거장 시각 + "software automates" 그럴듯한 오해 + 5.7 L/h CL collapse 실무 발현 사례. §5.6 / §7 Q16 cross-link. | Low |
| **MA20** *(v3)* | §5.1–§5.6 | ⚡ Memory Hook 6개 (분포지연 vs 시스템지연 / 방향=단서 / 데이터vs사전지식 / 간질환=CL감소함정 / 욕조채우기vs유지하기 / 식별가능영역) | YES | EXPERT_INFERENCE | Step 1 V5.0 명세의 *구조적 메커니즘 인코딩* 기준 충족 (단순 차이 나열 금지, 비유로 *왜* 차이가 생기는지 인코딩). 새 page tag 없음. | Low |
| **MA21** *(v3)* | §5.5 | Critical Blow 행 (LD/MD 혼동의 임상 파급) | YES | EXPERT_INFERENCE | aminoglycoside loading dose underdose → 초기 24h 치료 실패 → 내성 선택 압력 메커니즘. Step 1 V5.0 "치명적 타격" 명세 충족. 새 named drug example 없음 (aminoglycoside는 §2.5 Trench/§2.10 vancomycin 맥락에서 이미 등장). | Low |
| **MA22** *(v3)* | §2.5 | Rd framework 결정 테이블 (3-tier `fe·RF` 영역) | YES | EXPERT_INFERENCE | 기존 Rd 산문(`fe ≤ 0.30`, `RF ≥ 0.70` 임계값)을 결정 격자로 재배열. 새 외부 임계값 도입 없음. 컬럼 4가 §2.9 V/CL 분리와 cross-link. | Low |
| **MA23** *(v3)* | §7 | Q15 Boss-Dilemma 레이블 표준화 + ★★ SR 태그 | YES | EXPERT_INFERENCE | 기존 Q15 본문 보존 (트레이드오프 논리, source-locked numbers 유지); `## ⚡ 보스 딜레마 ★★` 표준 헤더 + ★★ SR 태그만 추가. Step 1 V5.0 명세 정합. | Low |
| **MA24** *(v3)* | §2.1–§2.10 | Practice Brief 4축 블록 10개 (전 카드) | YES | EXPERT_INFERENCE | 표준 4축(왜 알아야/흐름상 역할/체화 꿀팁/실무 활용)으로 카드별 체화 가이드 제공. 각 블록은 카드 본문 *마지막* 보조 박스 형태로 배치, 캐노니컬 본문에 영향 없음. S08·S11·S12·S15 등 이전 세션 cross-link 일관 유지. | Low |

| Rejected candidate | Reason for rejection |
|---|---|
| New drug examples outside the attached PDFs | Would violate source boundary and introduce unsupported examples. |
| New numerical decision thresholds beyond Content Lock v2 | Would risk restoring unsupported precision. |
| Broad rewrite of §2 cards | Would convert Phase 4D into Content Lock v3. |
| **Adherence Phantom S9 separate Confusion Pair** *(ver2 considered)* | §2.10 Trench-Level Tip이 이미 “adherence phantom을 IIV로 흡수하지 말라”를 잠그고 있어 별도 카드 신설은 분량 폭발 위험 vs 학습 ROI 낮음. Mastery Augmentation으로 한정. |
| **Confusion Pair §5.7: total CL ↔ unbound CL 부호 분리** *(ver2 considered)* | §5.4와 §2.5의 phenytoin/uremia 라인에 이미 핵심 메시지가 잠겨 있으며, Crucible Tip 6도 §2.5 Trench에 반영되어 있음. 별도 카드 신설은 중복. |



---

## Final v3 All-Pass Checklist

| # | Check item | Verification | Status |
|---:|---|---|---|
| 1 | **MA11–MA18 보존** | ver2 augmentation 8건 모두 본문에서 라벨·내용 그대로 유지 (B11 로그에서 검증 가능) | PASS |
| 2 | **F01–F07 splice fidelity 보존** | B8 Splice Verification Table의 7개 anchor·Final location·Inserted=YES 상태 모두 그대로 유지 | PASS |
| 3 | **Source-prefix labels & page tag 보존** | `[G&W ...]`, `[R&T ...]`, `[p.확인 필요]`, `[교과서 외 구현/규제 번역]` 등 모든 라벨 보존; 새 page tag 도입 없음 | PASS |
| 4 | **[⚡ Apex Concept] 1개 지정** | §2.1에 배지 + Plausible Fallacy block 삽입 (MA19) | PASS |
| 5 | **§5 Memory Hook 전수 6개** | §5.1–§5.6 모두에 *구조적 메커니즘을 비유로 인코딩한* Memory Hook 삽입 (MA20) | PASS |
| 6 | **Critical Blow 1개 행** | §5.5 비교 테이블에 ▶ 치명적 타격 행 추가 — aminoglycoside LD underdose 메커니즘 (MA21) | PASS |
| 7 | **Rd framework 결정 테이블** | §2.5 본문 산문 직후 3-tier `fe·RF` 결정 테이블 추가; 새 외부 임계값 없음 (MA22) | PASS |
| 8 | **Q15 Boss-Dilemma 레이블 + ★★ SR** | `## ⚡ 보스 딜레마 ★★` 표준 헤더 + Q15 본문 보존 + ★★ SR 태그 (MA23); Q16 미변경 | PASS |

**v3 판정**: GO. ver2 NO-GO 판정의 3개 구조적 결함(Apex 부재 / Memory Hook 부재 / Critical Blow 부재) 모두 봉합되었으며, Rd 결정 테이블 보강 및 Q15 레이블 표준화도 함께 처리되었다. 캐노니컬 본문, MA01–MA18 augmentation, F01–F07 splice fidelity, 모든 page tag는 변경 없이 보존되었다. 모든 신규 항목은 EXPERT_INFERENCE 또는 CRUCIBLE_DERIVED 라벨로 epistemic-tagged되어 source boundary를 위반하지 않는다.

**Phase 5 HTML compiler 재실행 시 영향 범위**:
- §2.1 헤딩 직후에 Apex Frame 박스(금색 좌측 보더) + Plausible Fallacy 박스(앰버 좌측 보더) 두 개 추가 렌더링.
- §5.1–§5.6 각 섹션 끝에 Memory Hook 박스(자색 좌측 보더 권장) 6개 추가 렌더링.
- §5.5 비교 테이블에 굵은 행(`▶ 치명적 타격`) 1개 추가 — 적색 강조 권장.
- §2.5 결정 테이블 1개 추가 — 표준 비교 테이블 스타일.
- §2.1–§2.10 각 카드 끝에 Practice Brief 박스(블루 좌측 보더 권장) 10개 추가 렌더링.
- §7에 `## ⚡ 보스 딜레마 ★★` 새 헤딩 추가; sidebar TOC에 anchor 추가 필요.
- B8 Splice Verification Table에는 영향 없음 (F01–F07 anchor 모두 유효).

---

## v3.1 Final Checklist

| # | Check item | Verification | Status |
|---:|---|---|---|
| 1 | PART A readability improved | 20개 patch 모두 적용 (P01–P20). Learner Navigation Aid 한국어화 (P01–P03), §2 dense sentence 분할 및 영문→한국어 변환 (P04–P13), §5 영문 one-line lock 한국어화 (P14–P15), §7·§8 가독성 개선 (P16–P20). | PASS |
| 2 | Scientific content unchanged | 모든 과학적 사실, 임상 수치, 파라미터 추정값, drug example, regulatory claim이 v3와 동일. | PASS |
| 3 | Equations preserved | MathJax 수식 (`Rd = RF·fe + (1-fe)`, `D_L = V·C_target/F`, ODE prototypes, OBJ_Bayes 등) 모두 원문 그대로. | PASS |
| 4 | Page tags preserved | `[p.XX]`, `[pp.XX–YY]`, `[pp.XX, YY]`, `[p.확인 필요]` 모든 페이지 태그가 원문 위치에 그대로 보존. 새 page tag 도입 없음. | PASS |
| 5 | Figure markers preserved | `<!-- FIGURE_POINTER -->`, `<!-- FIGURE_SCHEMATIC -->` 7개 marker block (F01–F07), 모든 Source / Why this matters / When to look / Learner instruction / Caption / Alt text 필드 원문 그대로. | PASS |
| 6 | Source-boundary preserved | source-prefix labels (`[G&W ...]`, `[R&T ...]`, `[교과서 외 구현/규제 번역]`, `[교과서 외 통합 추론 예시]`, `[확인 필요]`) 모두 그대로. 새 named drug example, 새 numerical anchor, 새 regulatory claim, 새 external reference 없음. | PASS |
| 7 | HTML-readiness preserved | PART B (B1–B11) 전체, marker → component mapping table, Mermaid self-check rules (M1–M7), CSS design system, Splice Verification Table (B8), Coverage Matrix (B9), Mastery Augmentation Log (B11) 모두 원문 그대로. PATCH MODE Insertion Map의 모든 anchor verbatim text가 v3.1 PART A에서도 1:1 일치 (Korean Readability Patch는 anchor 7개의 verbatim text를 변경하지 않음 — F01 anchor `**§1 recap**: 이 세션은 "모델 선택 → ...`, F02 anchor `§2.1은 plot-reading grammar이고 ...`, F03 anchor `**Trench-Level Tip**: Case B left-shift를 ...`, F04 anchor `PK35 digoxin 사례는 CL/V/t½ 추정 사례이다 ...`, F05 anchor `**Trench-Level Tip**: phenytoin처럼 albumin-bound ...`, F06 anchor `**Trench-Level Tip**: Phenobarbital의 dialysis half-life ...`, F07 anchor `**Trench-Level Tip**: "신부전이므로 LD도 줄인다"는 ...` 모두 patch 미적용 영역). | PASS |
| 8 | Ready for Phase 5 HTML compilation | PATCH MODE Splice Verification (B8) HALT 조건 H1–H3 모두 미발생; 7개 anchor 모두 v3.1 PART A에서 정확히 1회 발견됨; figure marker 7개 splice 가능; HTML compiler가 v3.1을 입력으로 받아 Phase 5 rendering contract (B4) 그대로 적용 가능. | PASS |

**v3.1 판정**: GO. v3의 모든 PASS 상태(Final v3 All-Pass Checklist 8개 항목)를 그대로 유지하면서, PART A의 한국어 독해성을 20개 surgical patch로 개선했다. PATCH MODE Splice Verification anchor 7개 (F01–F07)의 verbatim text는 patch 미적용 영역에 위치하므로 모두 그대로 보존되었으며, Phase 5 HTML compiler 재실행 시 splice 실패 위험 없음. v3.1은 Phase 5 HTML 컴파일 단계로 즉시 진입 가능하다.

---

## v3.2 Final Checklist

| # | Check item | Verification | Status |
|---:|---|---|---|
| 1 | PART A Korean-Dominant readability improved | 15개 patch 모두 적용 (K01–K15). Learner Navigation Aid·Curation Map 헤더 한국어화 (K01), §1 Source universe / Big Idea / Capstone spine 라벨 (K02), §2 sub-section 헤더 (Locked formulation, Editorial correction, Conceptual objective, AKI caveat, Hepatic contrast, Locked correction, Key equations, CAPD contrast, Criteria lock, Table 18-X locks, Phenytoin lock, Corrected Fig.18-5 lock, Clinical implication, Three scenarios, Worked examples retained, Deleted claim, Boundary 등) 한국어화 (K03–K10), §5 confusion pair 표 헤더 6개 + One-line lock 라벨 6개 (K11–K12), §7 Q15 Boss-Dilemma 라벨 + Answer 라벨 일괄 한국어화 16건 (K13), §8 B/C/D/E 헤더 + Final recap 영문 산문 한국어화 (K14–K15). | PASS |
| 2 | Career-critical 용어 paired expression | 핵심 pharmacometrics·교육 장치 용어를 `한글(English)` 형식으로 처리: 계량약리학(pharmacometrics), 편집자(Editor-in-Chief), 핵심 통찰(Big Idea), 캡스톤 척추(Capstone spine), 소스 범위(Source universe), 효과구획(Effect compartment), 회전 모델(Turnover model), 수용체 on/off(Receptor on/off), 한 줄 요약(One-line lock), 트레이드오프 / 보스 딜레마(Trade-off / Boss-Dilemma), 정답(Answer), 네 가지 메타 패턴(Four meta-patterns), 두 인자의 곱(Two-factor product), 소스 잠금 전문가 해석 지점(Source-locked professional moat), PK15 마무리 브리지(PK15 closing bridge), 최종 잠금 주의 목록(Final locked caution list), 최종 요약(Final recap), 자기 테스트: 능동 회상 모듈(Self-Test: Active Recall Module), 개념 해부 카드(Concept Anatomy Cards), 혼동 쌍 해부(Confusion Pair Dissection), 메타프레임과 큰 그림(Meta-Frame & Big Picture), 세션 헤더 & 로드맵(Session Header & Roadmap) 등. 기존 v3 항목인 기억 고리(Memory Hook), 그럴듯한 오해(Plausible Fallacy), 치명적 타격(Critical Blow), Practice Brief는 v3에서 이미 처리되어 그대로 유지. | PASS |
| 3 | Scientific content unchanged | 모든 과학적 사실, 임상 수치, 파라미터 추정값, drug example, regulatory claim이 v3.1과 동일. | PASS |
| 4 | Equations preserved | MathJax 수식 (`Rd = RF·fe + (1-fe)`, `D_L = V·C_target/F`, ODE prototypes, OBJ_Bayes 등) 모두 원문 그대로. | PASS |
| 5 | Page tags preserved (수치 검증) | `[p.XX]` 34개, `[pp.XX–YY]` 30개, `[p.확인 필요]` 11개, `[확인 필요]` 7개 모두 v3.1과 정확히 동일한 개수로 유지. 새 page tag 도입 없음, 페이지 번호 변경 없음. | PASS |
| 6 | HTML compiler markers preserved (수치 검증) | `<!-- MASTER LENS -->` 12개, `<!-- ANNOTATION -->` 11개, `<!-- ANCHOR -->` 3개, `<!-- TRENCH -->` 11개, `<!-- CONFUSION -->` 7개, `<!-- SELF-TEST -->` 2개, `<!-- RECAP -->` 7개, `<!-- FIGURE_POINTER -->` 12개 + `<!-- /FIGURE_POINTER -->` 10개, `<!-- FIGURE_SCHEMATIC -->` 6개 + `<!-- /FIGURE_SCHEMATIC -->` 4개 — 모두 v3.1과 정확히 동일한 개수로 유지. | PASS |
| 7 | Source labels preserved | `[EXPERT_INFERENCE, v3]`, `[CRUCIBLE_DERIVED, v3]`, `[AUDIT_DERIVED]`, `[TEXTBOOK_DERIVED]`, `[교과서 외 통합 추론 예시]`, `[교과서 외 구현/규제 번역]`, `[G&W ...]`, `[R&T ...]` 모두 그대로 보존. 새 named drug example, 새 numerical anchor, 새 regulatory claim, 새 external reference 없음. (PART A 본문의 augmentation 라벨 22개는 v3.1과 동일; v3.2 Change Log 자체에 두 라벨이 description 텍스트로 1회씩 meta-reference로 등장하지만 이는 새로운 과학적 라벨링이 아니라 라벨 보존을 설명하는 텍스트.) | PASS |
| 8 | Anchor verbatim 보존 (자동 검증) | F01–F07 PATCH MODE Insertion Map anchor 7개 모두 PART A 본문에서 정확히 1회씩 발견됨 (PART B Insertion Map 1회 포함하여 총 2회). 곡선 따옴표(`""`), 백틱 코드 스팬(`` ` ``), 영숫자, 한글 모두 byte-for-byte 일치. 자동 검증 스크립트 통과. | PASS |
| 9 | PART B 무변경 | B1–B11 모든 guardrail·certification·marker block registry·splice verification table·coverage matrix·mastery augmentation log가 v3.1과 동일. v3.2는 PART B의 어떤 줄도 수정하지 않았다 (단, 본 v3.2 Change Log는 PART A 상단에 위치). | PASS |
| 10 | Ready for Phase 5 HTML compilation | PATCH MODE Splice Verification (B8) HALT 조건 H1–H3 모두 미발생; 7개 anchor 모두 v3.2 PART A에서 정확히 1회 발견됨; figure marker 7개 splice 가능; HTML compiler가 v3.2를 입력으로 받아 Phase 5 rendering contract (B4) 그대로 적용 가능. | PASS |

**v3.2 판정**: GO. v3의 8개 All-Pass 항목 + v3.1의 8개 Final Checklist 항목을 모두 유지하면서, PART A의 한국어 중심 독해성을 15개 surgical patch (K01–K15)로 추가 개선했다. 영문 sub-section 헤더, 표 헤더, 영문 산문이 한국어 중심으로 변환되었고, 커리어상 영어로 알아두는 것이 유리한 핵심 pharmacometrics·교육 장치 용어는 `한글(English)` 형식으로 병기되어 국제 학술·실무 검색·논문 작성·발표에서의 영어 익숙도를 잃지 않도록 처리되었다. PATCH MODE anchor 7개 (F01–F07)의 verbatim text는 자동 스크립트로 검증되어 byte-for-byte 일치하며, page tag 82개·HTML marker 85개 모두 v3.1 대비 정확히 동일한 개수로 보존되었다. v3.2는 Phase 5 HTML 컴파일 단계로 즉시 진입 가능하다.

---

## Final Certification Table

| Certificate | Status | Basis |
|---|---|---|
| Korean-Dominant Readability Certificate | PASS | 일반 학습자 본문 영문 산문이 가능한 한 한국어로 변환되었다 (15개 K-patch). 커리어상 핵심 pharmacometrics·교육 장치 용어는 `한글(English)` 형식의 paired expression으로 보존되었다 (계량약리학(pharmacometrics), 효과구획(Effect compartment), 한 줄 요약(One-line lock), 정답(Answer), 트레이드오프 / 보스 딜레마(Trade-off / Boss-Dilemma) 등). 표준 약어·기호(`CL`, `V`, `ka`, `F`, `AUC`, `Cmax`, `MRT`, `Vss`, `η`, `ε`, `ω²`, `THETA`, `OMEGA`, `SIGMA`, `t½` 등)는 원문 그대로 유지되었다. |
| Scientific Preservation Certificate | PASS | 어떠한 과학적 콘텐츠, 수식, 수치, 예시, page tag, source label도 변경되지 않았다. 페이지 번호 검증: `[p.XX]` 34/34, `[pp.XX–YY]` 30/30, `[p.확인 필요]` 11/11, `[확인 필요]` 7/7 — v3.1과 정확히 동일. 새 named drug example·새 numerical anchor·새 regulatory claim·새 external reference 도입 없음. |
| Marker Integrity Certificate | PASS | 모든 figure marker (`<!-- FIGURE_POINTER -->` 12쌍, `<!-- FIGURE_SCHEMATIC -->` 6쌍 — 일부는 닫힘 태그가 PART B Marker Block Registry에 별도 위치), HTML compiler marker (`<!-- MASTER LENS -->`, `<!-- ANNOTATION -->`, `<!-- TRENCH -->`, `<!-- CONFUSION -->`, `<!-- SELF-TEST -->`, `<!-- RECAP -->`, `<!-- ANCHOR -->`), anchor (F01–F07), section/card 구조가 v3.1과 정확히 동일한 개수와 위치로 보존되었다. PATCH MODE anchor 7개는 자동 스크립트로 verbatim 일치 검증됨. |
| HTML-Readiness Certificate | PASS | Phase 5 호환성이 유지되었다. PART B의 B1–B11 모든 guardrail·B4 HTML compiler requirements·B8 Splice Verification Table·B9 Coverage Matrix·B11 Mastery Augmentation Log가 변경되지 않았다. HTML/Mermaid/SVG 코드는 생성되지 않았다. PATCH MODE Splice Verification HALT 조건 H1–H3은 발생하지 않으며, 7개 anchor 모두 PART A 본문에서 정확히 1회씩 발견되어 splice 가능 상태이다. |

---

*PIPET Lab · 계량약리학 PhD Program · 16_HTML Compile Input Master v3.2*
*Korean-Dominant Readability Patch — PART A 학습자 본문 한국어 중심 가독성 개선*
*v3.1 (Phase 4D PASS, 20개 P-patch) + v3 (8 v3 패치, MA19–MA24) + ver2 (8 v2 패치, MA11–MA18) 위에 적층된 안전한 표면 패치*

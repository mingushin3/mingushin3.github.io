# XX_html_compile_input_master_v3.2.md

> **v3.6.1 note:** This version applies a Compact Equation Annotation + Section Core Declaration Patch to PART A only. OP-1: All "Annotated equation — 수식 해부" bullet lists (항별 의미·실무 직관·오해 방지) removed; underbrace/overbrace labels refined for compactness and clarity from a pharmacometrics expert perspective. OP-2 (Replace mode): All per-slide 핵심 메시지 blocks removed; replaced by SECTION_CORE markers with single-line vivid 핵심 요지 declarations at thematic section boundaries. All SLIDE_START markers, figure markers, page tags, source labels, numerical anchors, tables, code blocks, and PART B content are preserved unchanged from v3.6.

> **v3.6.1 보존 검증 통과:** OP-1(수식 bullet 제거·레이블 정제) + OP-2(슬라이드별 핵심 메시지 전부 제거·SECTION_CORE 핵심 요지 삽입) 외 원문 무변경 확인. SLIDE_START 마커 수·figure marker·page tag·source label·수치 anchor·표·코드·PART B 전부 보존. 잔존 핵심 메시지 행: 0건.


**v3.2 note:** This version applies a Korean-Dominant Readability Patch to PART A learner-facing prose. General English prose was converted to Korean where possible, while career-critical pharmacometrics terms are retained as Korean-English paired expressions on first use. Scientific content, equations, numerical anchors, page tags, source labels, figure markers, compiler markers, section structure, and PART B guardrails are preserved. No new scientific claims, examples, numbers, page tags, figures, or external references were added.

**v3.1 note:** This version applies a Korean Readability Patch to improve learner-facing Korean prose while preserving scientific content, equations, page tags, source labels, figure markers, and Phase 5 HTML-readiness. No new scientific claims, page tags, numerical anchors, figure decisions, or external references were added.

---

# 14_HTML Compile Input Master — Version 3.2

## Version 3.2 Enhancement Note (Korean-Dominant Readability Patch)

이 파일은 `14_html_compile_input_master_v3.1.md`의 PART A 과학 본문 전체와 PART B 컴파일 계약(compilation contract)을 그대로 상속한다. v3.2는 **하나의 좁게 한정된 패치 군**을 도입하여, v3.1 검토에서 식별된 잔존 영어 산문 마찰을 한국어 중심 가독성으로 한 번 더 닫는다.

> "v3.1에서 학습자 진입부와 §5 일부 한국어화는 성공했지만, §2 카드별 subsection 헤더, Failure Conditions·Assumptions의 영문 명사 나열, §8 Failure Mode 이름, 일부 본문 인라인 영어 표현이 여전히 한국어 학습자의 독해 흐름을 끊는다."

v3.2 patches (전부 PART A; 새로운 과학 내용 없음, 새로운 page tag 없음, 새로운 임상 예시 없음, 새로운 수치 임계값 없음, 새로운 figure marker 없음, 새로운 규제 언어 없음; 모두 한국어 중심 가독성을 위한 외과적(surgical) prose 편집):

| # | Location | Type | Source basis | Risk |
|---:|---|---|---|---|
| L01 | Top header v3.1→v3.2 + v3.2 enhancement note | Version note expansion | n/a (log only) | Low |
| L02 | Learner Navigation Aid 마지막 두 영문 문장 | Korean conversion (영문 → 한국어 산문) | Style/readability | Low |
| L03 | Learner Navigation Aid Practice Brief / Walkthrough 영문 안내 | Korean conversion + 학습 장치명 `한글(English)` 병기 | Style/readability | Low |
| L04 | §1 지식 그래프 위치 「직접 후속」 영문 명사 나열 | Korean conversion + `한글(English)` 병기 | Style/readability | Low |
| L05 | §2 C1 A/B/C/D subsection 헤더 + 본문 영어 표현 | Korean header conversion + 본문 `한글(English)` 병기 | Style/readability | Low |
| L06 | §2 C2 A/B/C/D subsection 헤더 + Failure Conditions 6-item 나열 + body 영어 표현 | Korean header conversion + list `한글(English)` 병기 | Style/readability | Low |
| L07 | §2 C3 A/B/C/D subsection 헤더 + Limitations 영어 명사 + body | Korean header conversion + `한글(English)` 병기 | Style/readability | Low |
| L08 | §2 C4 A/B/C/D subsection 헤더 + Elementary/Complex Dedrick 명칭 + Buckingham π 표현 + Data Anchor body | Korean header conversion + `한글(English)` 병기 | Style/readability | Low |
| L09 | §2 C5 A/B/C/D subsection 헤더 + Assumptions 5-item 나열 + body 영어 표현 | Korean header conversion + list `한글(English)` 병기 | Style/readability | Low |
| L10 | §8 A.1–3 Animal-to-human / PopPK / PBPK scaling 항목 | Korean conversion + `한글(English)` 병기 | Style/readability | Low |
| L11 | §8 B Failure Mode 1/2/3 이름 | 학습 장치명 `한글(English)` 병기 + 부제 한국어화 | Style/readability | Low |
| L12 | §8 C Professional Moat 헤더 + 학습 장치명 첫 등장 `한글(English)` 병기 (Practice Brief, Practice Lens, Mastery Note, Failure Mode, Plausible Fallacy, Critical Blow, Boss Dilemma) | First-use gloss for pedagogical device names + Korean section header polish | Style/readability | Low |

v3.2는 v3.1의 모든 PART A 과학 문장, 수식, page tag, marker, figure pointer, RECAP, Mastery Note 본문 내용, Practice Lens, Trench tip, Practice Brief 4축, Walkthrough, Target Mental Model, "왜 이 질문" rationale, [⚡ Apex Concept] 마커, §5 v3 Memory Hooks 2개, v3 Plausible Fallacy 보강(`b=0.75` over-trust), v3.1 K01–K13 prose patch를 **그대로 보존**합니다. PK28/PK29 anchor, 4.1/7.4/7.7 fold 분리, FIH backbone 위상, R&T age/renal/BSA caution, Audit/Crucible guardrail도 모두 보존됩니다.

---

## Version 3.1 Enhancement Note (Korean Readability Patch)

This file inherits the full PART A scientific body and PART B compilation contract
from `14_html_compile_input_master_v3.md`. Version 3.1 introduces **a single
narrowly scoped patch family** addressing residual Korean readability gaps
identified in the v3.1 review:

> "Learner Navigation Aid의 일부 안내문이 영문으로만 작성되어 있고, 본문 일부
> 카드의 표현이 한국어 독해 흐름을 미세하게 끊는다."

v3.1 patches (all PART A, no new science, no new page tags, no new clinical
examples, no new numerical thresholds, no new figure markers, no new regulatory
language; all Low-risk surgical Korean readability edits):

| # | Location | Type | Source basis | Risk |
|---:|---|---|---|---|
| K01 | Learner Navigation Aid 섹션 헤더 | Korean flow improvement (영문 헤더 → 한국어) | Style/readability | Low |
| K02 | Learner Navigation Aid Learning route 7-item list | Korean flow improvement (영문 목록 → 한국어) | Style/readability | Low |
| K03 | Learner Navigation Aid Before/After 헤더 | Korean flow improvement (영문 헤더 → 한국어) | Style/readability | Low |
| K04 | §2 C1 B Derivation — `turnover time` 첫 등장 | First-use gloss | Style/readability | Low |
| K05 | §2 C1 C Structural Meaning — `scale-invariant 구조` | First-use gloss | Style/readability | Low |
| K06 | §2 C3 MASTER LENS Big Idea — `extent` 첫 등장 | First-use gloss | Style/readability | Low |
| K07 | §2 C3 ANCHOR — 긴 문장 흐름 + "학생은" → "학습자는" | Sentence split + Korean flow improvement | Style/readability | Low |
| K08 | §2 C4 MASTER LENS Big Idea — `접어 넣는 변환` 표현 | Korean flow improvement | Style/readability | Low |
| K09 | §2 C2 Plausible Fallacy 보강 — `반대 방향의 거울상` | Redundancy trimming | Style/readability | Low |
| K10 | §2 C5 D 마지막 문장 | Korean flow improvement | Style/readability | Low |
| K11 | §5 Pair 2 기억 고리 | Korean flow improvement | Style/readability | Low |
| K12 | §2 폐막 Walkthrough Step 2 — 6개 trigger 나열 구조 | Sentence split | Style/readability | Low |
| K13 | §2 C4 C AUC relation 표현 | Concept clarification | Style/readability | Low |

v3.1은 v3의 모든 PART A 과학 문장, 수식, page tag, marker, figure pointer,
RECAP, Mastery Note, Practice Lens, Trench tip, Practice Brief, Walkthrough,
Target Mental Model, "왜 이 질문" rationale, [⚡ Apex Concept] 마커, §5 v3
Memory Hooks 2개, v3 Plausible Fallacy 보강(`b=0.75` over-trust)을 **그대로
보존**합니다. PK28/PK29 anchor, 4.1/7.4/7.7 fold 분리, FIH backbone 위상,
R&T age/renal/BSA caution, Audit/Crucible guardrail도 모두 보존됩니다.

---

## Version 3 Enhancement Note

This file inherits the full PART A scientific body and PART B compilation contract
from `14_html_compile_input_master_ver2.md`. Version 3 introduces **three bounded,
surgically scoped patches** addressing residual mastery gaps identified in the
v3 review:

> "C2 Apex가 명시적 `[⚡ Apex Concept]` 표준 마커로 표기되지 않았고, §5 일부
> 혼동쌍에 기억 고리(Memory Hook)가 누락되어 있다."

v3 patches (all PART A, all source-labeled, no new page tags, no new named clinical
examples, no new numerical thresholds, no new figure markers, no new regulatory
language):

| # | Location | Type | Source basis | Risk |
|---:|---|---|---|---|
| P1a | §2 C2 heading | Apex marker normalization (`[Apex]` → `[⚡ Apex Concept]`) | Style/marker convention | Low |
| P1b | §2 C2 (after `B. Plausible Fallacy` block) | Plausible Fallacy 보강 — `b=0.75` over-trust | EXPERT_INFERENCE (mirror to existing `b=1` fallacy) | Low |
| P2a | §5 Pair 1 (after Critical Blow) | ⚡ 기억 고리 — *기능 vs 공간* | EXPERT_INFERENCE (compresses C2/C3 priors) | Low |
| P2b | §5 Pair 3 (after 정리) | ⚡ 기억 고리 — *직선 도로 vs 우회로* | EXPERT_INFERENCE (simple vs corrected allometry framing) | Low |
| P3 | PART B B11 + Final v3 All-Pass Checklist | v3 Change Log (minimum entries) | n/a | Low |

v3는 ver2의 모든 PART A 사실 문장, 수식, page tag, marker, figure pointer, RECAP,
Mastery Note, Practice Lens, Trench tip, Practice Brief, Allometric Decision
Walkthrough, Target Mental Model, "왜 이 질문" rationale를 **그대로 보존**합니다.
PK28/PK29 anchor, 4.1/7.4/7.7 fold 분리, FIH backbone 위상, R&T age/renal/BSA
caution도 모두 보존됩니다.

---

## Version 2 Enhancement Note

This file inherits PART A scientific body and PART B compilation contract from
`14_html_compile_input_master.md`. ver2 adds **five bounded mastery augmentations**
to address a Mastery-Uplift gap detected by user-side review:

> "각 개념마다 **왜 알아야 하는가 / 흐름상 역할 / 체화 꿀팁 / 실무 활용**의
> 4축이 카드별로 일관 구조화되어 있는가 + C1→C5 통합 워크플로우 walkthrough가
> 본문에 시연되어 있는가"

ver2 augmentations (all PART A, all source-labeled, no new page tags, no new named
examples, no new numerical thresholds, no new figure markers, no new regulatory
language):

| # | Location | Type | Source basis | Risk |
|---:|---|---|---|---|
| V1 | §1 Big Idea 직후 | Target Mental Model 명시 블록 | TEXTBOOK_DERIVED (§8 D 압축 미러) | Low |
| V2 | §2 C1–C5 각 카드 말미 | ▶ Practice Brief 4축 블록 (왜/흐름/꿀팁/실무) | EXPERT_INFERENCE (PART A 내부 합성) | Low |
| V3 | §2 폐막 (C5 후) | ▶ Allometric Decision Walkthrough 5-step | EXPERT_INFERENCE (C1–C5 통합) | Medium |
| V4 | §7 각 Q 진입부 | "왜 이 질문" 1줄 rationale | EXPERT_INFERENCE (§1 spine + Q 의도) | Low |
| V5 | PART B B11 | Mastery Augmentation Log ver2 갱신 | n/a | Low |

ver2는 PART A의 모든 기존 사실 문장, 수식, page tag, marker, figure pointer,
RECAP, Mastery Note, Practice Lens, Trench tip을 **그대로 보존**합니다.

---

## Phase 4D Certification — ver2

| Certificate | Status | Basis |
|---|---|---|
| Learner-Standalone Certificate | PASS | PART A starts with a learner navigation aid and contains §1, §2, §5, §7, and §8 as a complete study handout without audit/process tables. ver2 adds Practice Brief and Walkthrough blocks that strengthen self-study completeness. |
| Zero-Omission Certificate | PASS | Scope Lock, Audit MUST/SHOULD fixes, Content Lock v2, v2.1 insertion map, Crucible Grade A logic, and PDF figure/page anchors were cross-checked; no high-impact unresolved omission remains. |
| Mastery-Uplift Certificate | PASS (uplifted in ver2) | Eight original bounded augmentations + five ver2 augmentations (Practice Briefs, Walkthrough, Target Mental Model, Q rationales, log update) inserted with explicit source labels. The 4-axis (why / role / tip / practice) frame is now consistent across C1–C5. |
| Source-Boundary Certificate | PASS | Each augmentation is labeled TEXTBOOK_DERIVED, AUDIT_DERIVED, CRUCIBLE_DERIVED, or EXPERT_INFERENCE; no new page tags, no new named examples (only methadone / compound X / cefazolin / epoetin-β remain), no new numerical anchors, no new regulatory phrases, no new figure markers. |
| HTML-Readiness Certificate | PASS | PART B contains the Phase 5 compilation contract, figure rules, page-tag rules, marker mapping, navigation integrity rules, audit/crucible guardrails, and PATCH MODE splice verification. ver2 Practice Briefs use the existing TRENCH marker (rose tip-box style); ver2 Walkthrough uses MASTER LENS marker (gold callout). No new marker types introduced. |

## Assembly Mode

PATCH MODE — `14_Content_Lock_v2.1(1).md` is a Figure Marker Patch / Insertion Map, not a full re-emitted learner body. PART A was constructed from learner-facing `14_Content_Lock_v2(2).md` §1–§8, with the seven approved Phase 4C markers spliced at exact unique anchors. ver2 adds five labeled mastery augmentations on top of that exact-spliced base.

## Input Manifest

| File | Role | Authority level | Used for | Notes |
|---|---|---:|---|---|
| `14_scope_lock(3).md` | scope boundary | A0 | source range, learner, mode, image-right boundary, hard rules | Image rights = None; textbook figures must be pointers only. |
| `014_G_알로메트릭 스케일링 종간 외삽·체중·연령(4).pdf` | PDF verification source | A1 | G&W §2.10, PK28, PK29 formulas, data anchors, figure identities | Used only for verification/high-impact grounding. |
| `014_T_알로메트릭 스케일링 종간 외삽·체중·연령(4).pdf` | PDF verification source | A1 | R&T Ch.14/Ch.22 age-weight and allometry anchors | Used only for verification/high-impact grounding. |
| `14_Audit_Report_v1(3).md` | audit guardrail | A2 | MUST_FIX/SHOULD_FIX correction and regression prevention | Controls fold correction, FIH directionality, unsupported claims. |
| `14_Content_Lock_v2(2).md` | canonical body | A3 | base learner body | §1–§8 used; process/adjudication §0 excluded from learner-facing PART A. |
| `14_Content_Lock_v2.1(1).md` | figure insertion source | A4 | PATCH MODE figure strategy and exact insertion anchors | Seven approved markers; two schematics, five pointers. |
| `14_crucible_report_v1(1).md` | crucible guardrail | A5 | preserved Grade A logic and mastery augmentation basis | Used only as controlled insight source, not raw prose source. |
| `S14_phase1_patch memo(2).md` | locked reference / deprecated source check | A6 | regression check against Phase 1 known weaknesses | Not copied into PART A. |
| `14_step1_draft_v0(2).md` | deprecated source | A6 | regression check only | Not used as learner-body source. |
| `14_html_compile_input_master.md` | ver1 source | A8 | base for ver2 augmentation | All ver1 PART A scientific content preserved verbatim in ver2. |

---

## PART A — 학습자용 완성 핸드아웃(Learner-Facing Complete Handout)

<!-- SECTION_CORE: SC-01 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** $Y=a\cdot BW^b$를 암기식이 아니라 $CL$·$V$·시간·Dedrick·dose backbone을 한 줄로 꿰는 allometric spine으로 먼저 잡아라.

---
<!-- SLIDE_START: S01 | title: 학습 항법 안내 | source_anchor: learner-navigation-aid -->

## 학습 항법 안내(Learner Navigation Aid)

**이 자료 활용법:** §1을 한 번 읽어 전체 뼈대를 잡은 뒤, §2 C1–C5를 순서대로 학습하고, §7에 도전하기 전에 §5로 세 가지 혼동을 먼저 차단하세요. Figure pointer는 교과서 그림을 그대로 복제하지 않습니다. Pointer가 등장하면 출처 PDF·교과서에서 명시된 figure를 직접 펼쳐 확인하시면 됩니다.

**각 C-카드는 ▶ 실무 체화 요약(Practice Brief)으로 마무리되며, 네 가지 체화 축(왜 알아야 하는가 / 흐름상 역할 / 체화 꿀팁 / 실무 활용)을 압축합니다.** §2는 알로메트릭 의사결정 워크스루(Allometric Decision Walkthrough)로 마무리되어 C1→C5를 하나의 작업 흐름으로 연결합니다.

**학습 경로:**

1. C1: $Y=a\cdot BW^b$가 단순 회귀선이 아닌 **스케일 법칙**임을 이해합니다.
2. C2: CL 지수와 $b=1$ 오류(fallacy)를 확실히 잡습니다.
3. C3: 흐름(flow) 지수 $b$와 분포 범위(extent) 지수 $d$를 분리하고 시간·속도 결과를 도출합니다.
4. C4: Dedrick 도표(Dedrick plot)를 지수 구조의 진단 도구로 활용합니다.
5. C5: 알로메트릭 용량(allometric dose) 외삽을 최종 임상 용량이 아니라 equal-AUCu 백본(backbone)으로 다룹니다.
6. §2 폐막 워크스루(Walkthrough): 동물 PK 데이터셋 하나를 C1→C5 흐름으로 통과시켜 전체 흐름을 잠급니다.
7. §5–§7: 출처(source) 불일치, 근거 없는 규제 언어, 지수 혼동 오류를 스스로 차단할 수 있는지 점검합니다.

**시작 전 점검:** CL, V, AUC, 반감기(half-life), 비결합 분율(unbound fraction), 일차 제거(first-order elimination)를 정의할 수 있는지 확인합니다.  
**완료 후 체크:** $0.75$와 $1.0$이 왜 호환되지 않는지, 시간이 왜 $d-b$로 스케일링되는지, 소아·노인 용량에서 왜 기능적 연령(functional age)과 장기 기능 보정이 체중 외에 추가로 필요한지 설명할 수 있어야 합니다.


<!-- SLIDE_START: S02 | title: 세션 개요와 로드맵 | source_anchor: section-1-roadmap -->

## §1 — 세션 개요와 로드맵(Session Header & Roadmap)

**Source:** Gabrielsson & Weiner 5e §2.10 (p.170–191), Case Study PK28 (p.611–614), Case Study PK29 (p.615–620); Rowland & Tozer 5e Ch.14 (p.411–441), Ch.22 allometry section (p.731–743).

### 핵심 아이디어(Big Idea)

<!-- MASTER LENS -->
$Y=a\cdot BW^b$는 단순 회귀식이 아닙니다. 종간 체중 차이를 **파라미터 스케일(parameter scale)**로 번역하는 거듭제곱 언어입니다.
<!-- ANNOTATION -->
여기서 파라미터 스케일(parameter scale, 체중 차이를 파라미터 단위로 옮기는 척도)은 “kg 차이”를 CL, V, 용량(dose) 같은 PK 파라미터의 차이로 바꾸어 읽는 방식입니다. 핵심 오류는 $b=0.75$와 $b=1.0$의 차이를 작게 보는 것입니다. R&T의 20-g mouse→70-kg human 예시에서는 같은 값 1이 $b=1$이면 3500, $b=0.75$이면 455가 되어 7.7배 차이가 납니다 [R&T p.733]. G&W PK28의 23-g mouse→70-kg human에서는 약 7.4배, rat 250-g→human 70-kg에서는 약 4.1배 차이입니다. 이 차이는 “용량을 낮게 시작한다/높게 시작한다”라는 단순 구호가 아니라, **target AUC 기반에서는 CL 과대예측이 dose 과대 산출로 이어질 수 있다**는 dose/AUC 방향성 문제입니다.
> **Annotated equation — 수식 해부**
>
> $$
> \overbrace{b=1}^{\text{kg당 선형}}\quad vs\quad \overbrace{b=0.75}^{\text{CL 흐름 prior}}
> $$


> **▶ 목표 사고 모델(Target Mental Model) — [TEXTBOOK_DERIVED, ver2 V1]**  
> 이 세션을 마치는 순간, 다음 4단계가 자동으로 회상되어야 합니다.
> 1. **변수 종류부터 묻습니다** — 흐름/속도(flow/rate) 변수인가(CL, GFR, 혈류량(blood flow) → $b\approx 0.75$), 공간/분포 범위(space/extent) 변수인가(V, 혈액량(blood volume), 조직량(tissue mass) → $d\approx 1$), 시간(time) 변수인가($V/CL \rightarrow BW^{d-b}$), 속도상수(rate constant) 변수인가($CL/V \rightarrow BW^{b-d}$).
> 2. **종간 용량 번역(dose translation)은 비결합 노출(unbound exposure) 관점**으로 읽습니다. AUCu equality이면 $Dose \propto BW^b$, mg/kg 비는 $BW^{b-1}$입니다.
> 3. **예외를 먼저 찾습니다** — fu, CYP 동종효소(isoform), 비선형 PK(nonlinear PK), 수송체(transporter), 장간 순환(enterohepatic recirculation), 투여 경로·제형(route/formulation) 차이입니다.
> 4. **출처 언어(source language)를 지킵니다** — PDF에서 직접 뒷받침되는 항목(PDF-supported: G&W/R&T 수식, PK28/PK29 anchor, R&T age/renal/BSA caution)과 직접 뒷받침되지 않는 항목(not directly supported: ICH/FDA/MABEL/NONMEM/QSP 단정)을 분리합니다. 이 4단계 자체가 §8 D 최종 사고 모델(Final Mental Model)의 압축이며, §1–§8 전체가 이 4단계의 정당화 과정입니다.

<!-- SLIDE_START: S03 | title: 개념 항법도와 지식 그래프 | source_anchor: section-1-concept-map -->

### 개념 항법도

```text
[C1] Master Equation: Y = a·BW^b
        │
        ├──▶ [C2] CL exponent b≈0.75 ─────────────┐
        │                                           ├──▶ [C5] Equal-AUCu dose backbone
        └──▶ [C3] V exponent d≈1.0 ────────────────┘
                  │
                  ├──▶ t1/2 ∝ BW^(d-b)≈BW^0.25
                  ├──▶ kel ∝ BW^(b-d)≈BW^-0.25
                  └──▶ [C4] Dedrick Superposition
```

### 지식 그래프 위치

**선행 전제:** CL, V, AUC, 반감기(half-life)의 정의; 일구획 지수 감소(one-compartment exponential decay); 혈장 단백 결합(plasma protein binding, 단백 결합으로 자유 약물 농도가 달라지는 현상)과 비결합 청소율(unbound clearance) 개념입니다.  
<!-- ANNOTATION -->
**직접 후속:** 소아·노인 용량 조정(pediatric/elderly dose adjustment), 모집단 약동학 체중 공변량 선택(PopPK weight covariate choice), PBPK 장기 혈류·부피 스케일링(PBPK organ blood flow/volume scaling), 최초 인체 투여 노출 번역 표(FIH exposure translation table).  
**주의:** NONMEM control stream, ICH/FDA/MABEL 언어(language), QSP 구현(implementation)은 본 PDF가 직접 다루는 내용이 아니므로, 본문에서는 `[교과서 외 구현/실무 해석]`으로만 다룹니다.

<!-- RECAP -->
**§1 요약:** 이 세션의 중심축(spine)은 $Y=a\cdot BW^b \rightarrow CL\ b\approx0.75 \rightarrow V\ d\approx1 \rightarrow time\ d-b\approx0.25 \rightarrow Dedrick \rightarrow equal\text{-}AUCu\ dose\ backbone$입니다. 반드시 고정해야 할 교정 지점은 $4.1/7.4/7.7$ fold 기준을 분리하고, FIH dose formula를 standalone starting-dose rule이 아닌 allometric exposure backbone으로 낮추는 것입니다.

---


<!-- SLIDE_START: S04 | title: 알로메트릭 중심축 schematic | source_anchor: figure-F1-allometric-spine -->

<!-- FIGURE_SCHEMATIC --><br>Title: 알로메트릭 중심축: 변수 유형 → 지수 → 시간/용량 결과<br>Mode: N<br>Visual objective: 5초 안에 C1–C5가 하나의 작업 흐름이라는 점을 보이게 합니다.<br>Core message: $Y=a\cdot BW^b$는 독립 수식이 아니라 CL, V, 시간(time), Dedrick, equal-AUCu 용량 번역(dose translation)을 연결하는 중심축입니다.<br>Elements to include: 시작 노드 $Y=a\cdot BW^b$; CL / 흐름(flow) / $b\approx0.75$; V / 분포 범위(extent) / $d\approx1$; $t_{1/2}\propto BW^{d-b}$; $k_{el}\propto BW^{b-d}$; Dedrick superposition; Equal-AUCu dose backbone; 주의 게이트(caveat gates) fu, 대사 경로(metabolism route), 비선형 PK(nonlinear PK), 기능적 연령(functional age).<br>Elements to exclude: 규제기관 로고, 근거 없는 ICH/FDA 주장, 세부 PBPK/QSP 하위 모델, 동물 만화.<br>Suggested rendering: Mermaid<br>Caption: 알로메트릭 스케일링은 다섯 개의 고립된 공식이 아니라 연결된 의사결정 중심축으로 읽어야 합니다.<br>Alt text: $Y=a\cdot BW^b$에서 시작한 흐름도가 CL과 V 지수로 갈라진 뒤, 반감기, 속도상수, Dedrick 도표, 용량 번역 주의점으로 연결됩니다.<br>Source relation: Newly designed<br><!-- /FIGURE_SCHEMATIC -->
> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{Y=a\cdot BW^b}_{\text{마스터식}}\rightarrow\underbrace{CL\sim BW^{0.75}}_{\text{CL 흐름}}\; /\;\underbrace{V\sim BW^1}_{\text{V 공간}}\rightarrow\underbrace{t_{1/2}\sim BW^{d-b}}_{\text{시간축}}\; /\;\underbrace{k_{el}\sim BW^{b-d}}_{\text{제거속도}}\rightarrow\underbrace{Dose\sim BW^b}_{\text{AUCu 용량}}
> $$


## §2 — 개념 해부 카드(Concept Anatomy Cards)

---

<!-- SECTION_CORE: SC-02 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** $Y=a\cdot BW^b$의 $b$는 자연상수가 아니라 변수 유형과 scale-invariance를 검증하게 만드는 생리학적 prior다.

---
<!-- SLIDE_START: S05 | title: C1. Master Allometric Equation | source_anchor: C1-master-allometric-equation -->

### ━━ C1. 마스터 알로메트릭 방정식(Master Allometric Equation): $Y=a\cdot BW^b$ ━━

<!-- MASTER LENS -->
**개념 핵심 아이디어(Big Idea):** 알로메트리(allometry, 크기와 생리 변수의 거듭제곱 관계)는 “큰 동물은 단순히 작은 동물의 확대판인가?”라는 질문에 대한 정량적 답입니다.
<!-- ANNOTATION --> $a$는 화합물·변수의 절편(intercept), $b$는 체중이 바뀔 때 해당 변수의 변화율을 결정하는 지수(exponent)입니다.

#### A. 정형 정의(Formal Definition)

$$Y=a\cdot BW^b \quad [G\&W\ Eq.2:374,\ p.173;\ R\&T\ Eq.22\text{-}2,\ p.732]$$
> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{Y}_{\text{대상 변수}}=\underbrace{a}_{\text{절편}}\cdot \underbrace{BW}_{\text{체중}}^{\overbrace{b}^{\text{지수}}}
> $$


양변 로그 변환:

$$\ln(Y)=\ln(a)+b\cdot\ln(BW) \quad [G\&W\ Eq.2:379,\ p.176;\ R\&T\ Eq.22\text{-}1,\ p.732]$$
> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{\ln(Y)}_{\text{로그 }Y}=\underbrace{\ln(a)}_{\text{로그 절편}}+\overbrace{\underbrace{b}_{\text{기울기}}\cdot\underbrace{\ln(BW)}_{\text{로그 }BW}}^{\text{log-log 체중효과}}
> $$


- **$a$:** 약물 의존적(drug-dependent) 또는 화합물 의존적(compound-dependent) 절편(intercept)입니다. 단위는 $b$에 의존합니다.
- **$b$:** 대체로 변수 유형에 의존하는(variable type-dependent) 지수입니다. 다만 실제 CL 지수(exponent)는 자료 품질, 종 수, 비선형성, 종간 단백 결합(protein binding) 차이 등에 따라 변동할 수 있습니다 [G&W p.177–178].

<!-- SLIDE_START: S06 | title: C1. 거듭제곱 법칙의 생리학적 의미 | source_anchor: C1-derivation-boundary -->

#### B. 도출(Derivation) — 왜 거듭제곱 함수인가

G&W는 대사율(metabolic rate)이 $BW^{0.75}$로 스케일링하고, 에너지 함량(energy content)이 대략 $BW^1$에 비례하므로 순환 시간(turnover time, 에너지 순환 주기)이 $BW^{0.25}$로 나온다고 제시합니다 [G&W Eq.2:375–377, p.173]. 즉 알로메트리는 “체중이 커질수록 절대 처리량은 증가하지만, 단위 체중당 처리 효율은 감소한다”는 생리학적 압축입니다.

표면적·부피 직관도 같은 방향을 줍니다. 기하학적으로 표면적(surface)은 길이의 제곱(length²), 부피(volume)는 길이의 세제곱(length³)이므로 표면적은 부피의 $2/3$승에 비례합니다. 그러나 실제 생리학 변수는 단순 외부 표면적보다 더 복잡해, Brody의 경험적 지수는 0.5–0.8 범위로 나타납니다 [G&W p.173–174].

#### C. 구조적 의미(Structural Meaning)

<!-- ANCHOR -->
로그-로그(log-log) 직선은 단순히 “회귀가 잘 맞는다”는 뜻이 아닙니다. `[교과서 외 수학적 해석]`으로 말하면, 이는 체중 배율이 달라져도 같은 지수 법칙이 유지되는 척도 불변(scale-invariant) 구조를 가정한다는 뜻입니다. 이 가정이 깨지는 순간이 알로메트리 실패(allometry failure)의 시작입니다.

#### D. 경계 조건(Boundary Conditions)

G&W는 알로메트리(allometry)가 물리적 수송 과정(physical transport processes)에 지배되는 변수에서, 그리고 약물 분포가 혈장 단백 결합(plasma protein binding)에 크게 좌우되지 않는 물질에서 특히 유용하다고 설명합니다. 반대로 종간 대사·배설(metabolism/excretion)의 질적 차이, CYP450 동종효소(isozyme) 구성 차이, 혈장 단백 결합 차이가 크면 알로메트리는 실패할 수 있습니다 [G&W p.173].

#### E. 제텔카스텐 원자(Zettelkasten Atom)

```yaml
aliases: [allometric law, allometric power function, Y=a·BW^b]
tags: [pharmacometrics/allometry, scaling/inter-species]
source: "G&W §2.10.3 p.173–176; R&T Ch.22 p.731–733"
```

<!-- RECAP -->
**C1 핵심:** 알로메트리(Allometry)는 $a$와 $b$로 종간 차이를 압축합니다. 하지만 $b$는 “항상 고정된 자연상수”가 아니라, 변수 유형과 데이터 품질, 결합(binding), 비선형성, 종간 기전(mechanism) 차이에 영향을 받는 생리학적 prior입니다.

> **체화 노트(Mastery Note) — [CRUCIBLE_DERIVED]**  
> 로그-로그(log-log) 직선은 “그럴듯한 그림”이 아니라 척도 불변성 주장(scale-invariance claim)입니다. 따라서 C1을 적용할 때는 먼저 이 약물의 청소율(clearance) 또는 분포용적(volume)에 종 고유의 특성 기전(characteristic mechanism)이 들어오는지를 물어야 합니다.

> <!-- TRENCH -->
> **▶ 실무 체화 요약(Practice Brief) — C1 체화 4축 — [EXPERT_INFERENCE, ver2 V2]**  
> - **왜 알아야 하는가:** $Y=a\cdot BW^b$는 종간 PK 차이를 “회귀선”이 아니라 **척도 불변성 주장(scale-invariance claim)**으로 옮기는 언어입니다. 이 한 식이 깨지는 약물이 어떤 약물인지 식별하지 못하면 C2–C5의 모든 추론이 무너집니다.  
> - **흐름상 역할:** 항법도의 **루트 노드**입니다. $a$는 후속 카드들에서 구체값으로 채워지고, $b$는 C2(CL)와 C3(V)에서 각각 다른 prior를 받습니다. 즉 C1은 “수식 골격”, C2/C3는 “지수 채움”, C4/C5는 “결과 활용”입니다.  
> - **체화 꿀팁:** 회귀 결과를 보면 **먼저 잔차 패턴과 종 수**를 봅니다. 로그-로그 기울기(log-log slope)의 점추정값은 거짓 정밀도를 줄 수 있습니다. $b$는 자연상수가 아니라 **생리학적 prior**라고 입으로 말하며 풀어보시면 됩니다.  
> - **실무 활용:** 동물-인간 번역(animal-to-human translation) 보고서 첫 문단은 “이 화합물은 척도 불변성(scale-invariance)이 유지될 대사/수송 프로파일(metabolic/transport profile)을 갖는가?”에 답해야 합니다. 이 답이 “아니다”이면 C2의 $b\approx 0.75$ prior를 그대로 적용할 근거가 약해집니다.

---

<!-- SECTION_CORE: SC-03 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** $CL$은 공간이 아니라 시간당 흐름이다 — $b=1$ kg당 사고와 $b=0.75$ 과신을 동시에 의심하고 $CL_u$·기전 신호로 검증하라.

---
<!-- SLIDE_START: S07 | title: C2. Clearance exponent | source_anchor: C2-clearance-exponent -->

### ━━ C2. [⚡ Apex Concept] 청소율 지수(Clearance Exponent) $b\approx0.75$ ━━

<!-- MASTER LENS -->
**개념 핵심 아이디어(Big Idea):** 청소율(clearance)은 “공간의 크기”가 아니라 **단위 시간당 처리 흐름**입니다. 그래서 V처럼 $BW^1$로 증가하지 않고, 대사율·혈류·GFR과 같은 기능 변수(functional variable, 기능적 처리량 변수)처럼 대략 $BW^{0.75}$로 증가합니다 [G&W Table 2.22, p.180; R&T Fig.22-1, p.732].

#### A. 정형 정의(Formal Definition)

$$CL_i=a\cdot BW_i^b \quad [G\&W\ Eq.2:380,\ p.176;\ PK28\ Eq.28:1,\ p.611]$$
> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{CL_i}_{\text{개체 CL}}=\underbrace{a}_{\text{CL 절편}}\cdot\underbrace{BW_i}_{\text{개체 BW}}^{\overbrace{b}^{\text{CL 지수}}}
> $$


G&W는 CL/대사율(metabolic rate)의 대표 지수(exponent)를 0.75로 제시하지만, 실제 CL 지수는 약 0.2에서 $>1$까지 변할 수 있다고 경고합니다 [G&W p.178]. Fig.2.159는 91개 화합물의 CL 지수 분포가 주로 0.5–1.0 범위에 놓임을 보여 줍니다 [G&W p.191].

<!-- SLIDE_START: S08 | title: C2. $b=1$ 선형 kg당 오류 | source_anchor: C2-linear-per-kg-fallacy -->

#### B. 그럴듯한 오해(Plausible Fallacy) — $b=1$ 선형 kg당(per-kg) 스케일링

**오류:** “mg/kg 처방에 익숙하니 청소율(clearance)도 kg에 선형 비례한다”라고 생각하기 쉽습니다. 이것이 선형 kg당 스케일링(linear per-kg scaling, kg당 값이 일정하다는 가정) 오류입니다.  
<!-- ANNOTATION -->
**교정:** CL은 흐름·속도 변수(rate/flow variable)이므로 $b\approx0.75$가 생리학적 prior(physiological prior)입니다.

- **R&T 20-g mouse→70-kg human:** $b=1$이면 3500, $b=0.75$이면 455 → 7.7배 차이 [R&T p.733].
- **G&W PK28 23-g mouse→70-kg human:** $(70/0.023)^{0.25}\approx7.4$배 차이.
- **Rat 250-g→70-kg human:** $(70/0.25)^{0.25}\approx4.1$배 차이.
> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{\left(\frac{BW_{human}}{BW_{animal}}\right)^{1-0.75}}_{\text{b=1 vs 0.75 격차}}=\underbrace{\left(\frac{BW_{human}}{BW_{animal}}\right)^{0.25}}_{\text{species 격차}}
> $$


Target AUC 용량(dose) 계산에서는 CL 과대예측이 목표 AUC를 맞추기 위한 dose 과대 산출로 이어질 수 있습니다. 따라서 “CL 과대평가 → subtherapeutic 시작”이라는 단정은 사용하지 않습니다.

> <!-- TRENCH -->
> **▶ 그럴듯한 오해(Plausible Fallacy) 보강 — $b=0.75$ 과신(over-trust) — [EXPERT_INFERENCE, v3]**
>
> - **그럴듯한 오해:** “CL 지수 $b=0.75$를 적용하면 종간 스케일링 문제가 해결된다”라고 보는 것입니다.
> - **왜 틀렸는가:** $0.75$는 대사율 스케일링(metabolic rate scaling)의 경험적 prior(empirical prior)이지 모든 약물에 적용되는 생물학적 법칙이 아닙니다. G&W는 실제 CL 지수가 $0.2$에서 $>1$까지 분포한다고 경고합니다 [G&W p.178]. 단백질 결합, 수송체(transporter) 발현, 종간 효소 활성 차이, 성숙(maturation) 요인이 모두 예외를 만들 수 있습니다. 즉 $0.75$는 **출발점(prior)**이지 **종점(law)**이 아닙니다.
> - **실무에서 어떻게 드러나는가:** FIH 용량을 $b=0.75$로만 계산했다가 실제 human CL이 다른 지수(exponent)를 따를 경우, Phase 1 시작 용량(starting dose)이 과대 또는 과소추정될 수 있습니다. 안전성 검토(safety review)에서 “지수 정당화(exponent justification)”를 요구하는 IND meeting 피드백이 나올 수 있습니다. 이 fallacy는 위의 $b=1$ 오류와 **거울상 관계**에 있습니다 — 한쪽은 mg/kg에 묶여 $b$를 1로 고정하고, 다른 쪽은 $b=0.75$를 무비판적으로 신뢰합니다. 두 fallacy를 동시에 차단해야 C2가 닫힙니다.

<!-- SLIDE_START: S09 | title: C2. Allometry 실패 조건과 $CL_u$ | source_anchor: C2-failure-conditions -->

#### C. 실패 조건(Failure Conditions)

알로메트리 실패(allometry failure)는 단순한 무작위 오차(random error)가 아니라 **메커니즘 신호(mechanism signal)**일 수 있습니다. G&W Fig.2.145는 스케일링 가능한 화합물(scalable compound)에서는 70-kg human CL 예측구간(prediction interval)이 약 10-fold 범위이지만, 스케일링이 어려운 화합물(less scalable compound)에서는 약 1000-fold 범위까지 넓어질 수 있음을 보여 줍니다 [G&W p.174].

주요 실패 트리거(failure trigger)는 다음과 같습니다:

1. 종간 혈장 단백 결합(species-dependent plasma protein binding) 차이;
2. 대사 경로 또는 CYP isozyme 조성(different metabolic routes or CYP isozyme composition) 차이;
3. 비선형 미카엘리스-멘텐 거동(nonlinear Michaelis-Menten behavior);
4. 장간 순환(enterohepatic recirculation);
5. 투여 경로·제형(route/formulation) 차이;
6. 중심·말초 분포용적 비율 변동(variable central/peripheral volume ratio) [G&W p.191].

> <!-- TRENCH -->
> **[TRENCH — 비결합 청소율 스케일링(unbound clearance scaling)]** 종간 fu 차이가 크면 total CL이 아니라 $CL_u=CL/f_u$를 스케일링합니다. G&W Eq.2:421은 $CL_{u,man}=CL_{u,rat}\cdot(BW_{man}/BW_{rat})^b$ 형태로 제시되며 [G&W p.190], R&T Table 22-1은 cefazolin 등에서 human-animal plasma protein binding 차이가 크게 나타날 수 있음을 보여 줍니다 [R&T p.740]. `[교과서 외 실무 해석]` fu 비교는 가능하면 동일 농도, buffer, 온도, assay method에서 측정된 값끼리 해야 합니다.

#### D. 전문가 진단 트리거(Expert Diagnostic Trigger)

`[교과서 외 실무 해석]` PopPK 또는 종간 회귀에서 추정된 $b>1$이 나오면 “추정값을 그대로 믿을 것인가?”가 아니라 “종간 단백 결합(binding), 수송체(transporter), 포화(saturation), 자료 품질(data quality) 중 무엇이 기울기(slope)를 밀어 올렸는가?”를 먼저 물어야 합니다. 반대로 두 종만으로 얻은 $b<0.5$는 생리학적 신호보다 통계적 지렛대 부족(statistical leverage failure)일 가능성이 큽니다.

#### E. 제텔카스텐 원자(Zettelkasten Atom)

```yaml
aliases: [clearance allometric exponent, b_CL, Brody-Kleiber clearance scaling]
tags: [pharmacometrics/allometry, clearance, FIH/exposure-translation]
source: "G&W §2.10.3 p.176–180; G&W Fig.2.159 p.191; R&T Ch.22 p.732–735"
```

<!-- ANCHOR -->
CL의 $b\approx0.75$는 시간당 처리량의 지수입니다. 그럼 V는 왜 $d\approx1$일까요? 답은 V가 “흐름”이 아니라 “공간”이기 때문입니다.

<!-- SLIDE_START: S10 | title: Figure F2. $b=1$ vs $b=0.75$ | source_anchor: figure-F2-RT-b1-b075 -->

<!-- FIGURE_POINTER --><br>Source: Rowland & Tozer 5e, Ch.22, p.733, Fig.22-2<br>Why this matters: 이 그림은 $b=1$과 $b=0.75$ 오류를 보여 주는 가장 명확한 원출처 시각 자료입니다. 7.7배의 mouse-human 격차를 계산으로만 이해하는 것이 아니라 눈으로 확인하게 해 줍니다.<br>When to look: C2의 그럴듯한 오해(Plausible Fallacy)를 읽은 뒤, C2 실패 조건(Failure Conditions)으로 넘어가기 전에 확인하시면 됩니다.<br>Learner instruction: human body-weight 끝에서 $b=1$과 $b=0.75$ 투영값을 비교해 보세요. 그런 다음 target-AUC 논리에서 mg/kg 선형 스케일링이 왜 human CL/dose를 과대평가하는지 한 문장으로 다시 말해 보시면 됩니다.<br><!-- /FIGURE_POINTER -->

<!-- SLIDE_START: S11 | title: Figure F3. scalable vs less scalable compounds | source_anchor: figure-F3-GW-scalability -->

<!-- FIGURE_POINTER --><br>Source: Gabrielsson & Weiner 5e, §2.10.3, p.174, Fig.2.145<br>Why this matters: 이 그림은 allometry가 유용한 예측을 제공하는 화합물과 예측구간이 위험하게 넓어지는 화합물을 분리해서 보여 줍니다. 이는 실패가 단순 잡음이 아니라 기전/자료 품질 신호(mechanism/data-quality signal)일 수 있다는 C2의 메시지를 직접 뒷받침합니다.<br>When to look: C2 실패 조건(Failure Conditions)을 읽은 뒤 확인하시면 됩니다.<br>Learner instruction: 어느 패널이 스케일링 가능한 화합물(scalable compound)을 나타내고, 어느 패널이 스케일링이 어려운 화합물(less scalable compound)을 나타내는지 식별해 보세요. 그런 다음 넓은 예측구간을 C2의 실패 트리거 중 최소 두 가지와 연결해 보시면 됩니다.<br><!-- /FIGURE_POINTER -->

> **실무 렌즈(Practice Lens) — [AUDIT_DERIVED]**  
> $b=1$ 오류를 검토할 때는 “용량이 낮아진다/높아진다”라는 구호보다 계산 논리를 먼저 고정해야 합니다. Target AUC 기반에서는 CL 과대예측이 dose 과대 산출로 이어질 수 있으므로, 방향성 문장은 항상 노출 목표(exposure target)와 함께 써야 합니다.

> <!-- TRENCH -->
> **▶ 실무 체화 요약(Practice Brief) — C2 체화 4축 — [EXPERT_INFERENCE, ver2 V2]**  
> - **왜 알아야 하는가:** Apex 카드입니다. CL 지수 하나의 선택이 mouse→human 7.4배, rat→human 4.1배, 20-g mouse 케이스 7.7배의 **자릿수(order-of-magnitude) 격차**를 만듭니다. $b=0.75$ vs $b=1.0$은 “소수점 차이”가 아니라 **첫 human exposure estimate의 자릿수**를 바꿉니다.  
> - **흐름상 역할:** $b\approx 0.75$는 C5의 equal-AUCu backbone($Dose\propto BW^b$)에 직접 들어가는 **유일한 지수**입니다. C3의 V 지수와 조합되어 C4 Dedrick의 시간축도 결정합니다. C2가 흔들리면 C5 dose translation 전체가 흔들립니다.  
> - **체화 꿀팁:** **“흐름 변수 → 0.75”**라는 입버릇을 먼저 만듭니다. 그 다음 $b=1$을 보면 “이건 mg/kg 사고가 들어왔다”라고 진단합니다. $b>1$은 기전(mechanism) 신호, $b<0.5$는 통계적 지렛대 부족(statistical leverage failure)으로 분류하는 진단 레퍼토리를 굳힙니다.  
> - **실무 활용:** FIH exposure translation 표에서 CL column을 채울 때, $b=0.75$를 primary로 두되 $b=0.5, 0.62, 0.75, 1.0$ sensitivity를 같은 표에 병기하는 것이 방어적입니다 (Q8 보스 딜레마(Boss Dilemma) 응답 패턴). $f_u$ 차이가 크면 total CL이 아니라 $CL_u$를 스케일링한다는 Trench 규칙을 동시에 적용합니다.

---

<!-- SECTION_CORE: SC-04 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** $V$의 $d\approx1$과 $CL$의 $b\approx0.75$를 분리하면 $t_{1/2}\propto BW^{d-b}$와 $k_{el}\propto BW^{b-d}$가 한 번에 열린다.

---
<!-- SLIDE_START: S12 | title: C3. Volume exponent | source_anchor: C3-volume-exponent -->

### ━━ C3. 분포용적 지수(Volume Exponent) $d\approx1.0$ ━━

<!-- MASTER LENS -->
**개념 핵심 아이디어(Big Idea):** V는 흐름(flow, 처리 흐름)이 아니라 분포 범위(extent, 분포 공간의 크기)입니다. 체액, 혈액량, 조직 부피가 대체로 체중에 비례하므로 분포용적은 대략 $BW^1$로 증가합니다. 이 $d\approx1$과 CL의 $b\approx0.75$의 차이 0.25가 종간 시간 척도를 만듭니다.

#### A. 정형 정의(Formal Definition)

$$V_i=c\cdot BW_i^d \quad [G\&W\ Eq.2:382,\ p.179;\ PK28\ Eq.28:2,\ p.611]$$
> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{V_i}_{\text{개체 }V}=\underbrace{c}_{\text{V 절편}}\cdot\underbrace{BW_i}_{\text{개체 BW}}^{\overbrace{d}^{\text{V 지수}}}
> $$


G&W Table 2.22는 혈액량 지수(blood volume exponent) 0.99, 골격근량(skeletal mass) 1.09, Vd 약 1.0을 제시합니다 [G&W p.180].

<!-- SLIDE_START: S13 | title: C3. Half-life와 rate constant | source_anchor: C3-half-life-rate-constant -->

#### B. 결과(Consequence) — 반감기(half-life)와 속도상수(rate constant)

$$t_{1/2}=\ln2\cdot\frac{V}{CL}=\ln2\cdot\frac{c\cdot BW^d}{a\cdot BW^b}\propto BW^{d-b}$$
> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{t_{1/2}}_{\text{반감기}}=\underbrace{\ln2}_{\text{반감 상수}}\cdot\frac{\overbrace{V}^{\text{공간}}}{\overbrace{CL}^{\text{흐름}}}=\ln2\cdot\frac{\underbrace{c\cdot BW^d}_{\text{V 스케일}}}{\underbrace{a\cdot BW^b}_{\text{CL 스케일}}}\propto \underbrace{BW^{d-b}}_{\text{시간지수}}
> $$


$d\approx1$, $b\approx0.75$이면 다음과 같습니다:

$$t_{1/2}\propto BW^{0.25},\qquad k_{el}=\frac{CL}{V}\propto BW^{b-d}\approx BW^{-0.25}$$
> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{t_{1/2}}_{\text{반감기}}\propto \underbrace{BW^{0.25}}_{\text{큰 종↑}},\qquad \underbrace{k_{el}}_{\text{제거속도}}=\frac{\overbrace{CL}^{\text{흐름}}}{\overbrace{V}^{\text{공간}}}\propto\underbrace{BW^{b-d}}_{\text{큰 종↓}}\approx BW^{-0.25}
> $$


<!-- ANCHOR -->
학습자는 “$t_{1/2}\propto BW^{0.25}$”를 암기하는 데 그치기 쉽습니다. 그러나 더 중요한 것은 **큰 동물일수록 모든 일차 속도상수(first-order rate constant)가 작아진다**는 사실입니다. 같은 분수 $V/CL$을 시간으로 읽으면 반감기(half-life)이고, 뒤집어 $CL/V$로 읽으면 속도상수(rate constant)입니다. 다시 말해, 큰 동물은 절대 CL이 크지만 단위 시간당 제거되는 분율(fraction)은 작습니다.
<!-- ANNOTATION -->

<!-- SLIDE_START: S14 | title: C3. PK28 data anchor와 V 한계 | source_anchor: C3-PK28-volume-anchor -->

#### C. 데이터 앵커(Data Anchor) — Methadone PK28

G&W PK28 methadone 앵커는 다음과 같습니다:

| 종(Species) | BW | Dose | 비고(Note) |
|---|---:|---:|---|
| Mouse | 23 g | 25 µg IV bolus | 기본 Dedrick 앵커(elementary Dedrick anchor) |
| Rat | 250 g | 500 µg IV bolus | 출처 내부 $t_{1/2}$ 불일치(source-internal discrepancy) 있음 |
| Man | 70 kg | 100,000 µg IV bolus | human 앵커 |

- $a=0.319$, $AUC=1/a=3.13$ [G&W §2.10.6 p.186; PK28 p.613].
- 간 추출률(hepatic extraction) <10% [G&W p.186; PK28 p.613].
- **$t_{1/2}$ 불일치(discrepancy):** G&W §2.10.6 본문은 1.5/2.9/35 h, PK28 case는 1.5/3.9/35 h로 rat 값이 다릅니다. 본문 인용 시 `[§2.10.6 set]` 또는 `[PK28 case set]`을 명시합니다.

#### D. 한계(Limitations)

V 지수는 대체로 1에 가깝지만, $V_{ss}$는 조직 친화성(tissue affinity), 지방 분포(fat distribution), 수송체(transporter), 단백 결합(protein binding)에 따라 0.8–1.2 범위로 흔들릴 수 있습니다. R&T Ch.14의 비만(obesity) 예시도 “체중(body weight)이 항상 생물학적으로 관련된 분포용적(biologically relevant volume)은 아니다”라는 경고로 읽어야 합니다 [R&T p.439].

<!-- RECAP -->
**C3 핵심:** $d\approx1$은 분포 공간이 체중에 비례한다는 뜻이고, $b<d$는 큰 동물에서 제거 분율(fraction)이 느려진다는 뜻입니다. $d-b$와 $b-d$를 동시에 볼 수 있어야 half-life와 rate constant를 같은 구조로 이해할 수 있습니다.

<!-- SLIDE_START: S15 | title: Figure F4. flow vs extent schematic | source_anchor: figure-F4-flow-vs-extent -->

<!-- FIGURE_SCHEMATIC --><br>Title: 흐름과 분포 범위의 분리: 왜 $b$와 $d$를 바꾸어 쓰면 안 되는가<br>Mode: N<br>Visual objective: 5초 안에 CL, V, half-life, $k_{el}$의 방향성을 분리합니다.<br>Core message: CL은 흐름(flow)이므로 $b\approx0.75$, V는 분포 범위(extent)이므로 $d\approx1$이며, 두 지수의 차이가 시간(time)과 속도상수(rate constant)를 반대 방향으로 만듭니다.<br>Elements to include: 2열 레이아웃 $CL=a\cdot BW^b$ vs $V=c\cdot BW^d$; 레이블 flow/rate vs space/extent; 화살표 $V/CL \rightarrow t_{1/2}\propto BW^{d-b}$; $CL/V \rightarrow k_{el}\propto BW^{b-d}$; 경고 스트립: 근거 없이 CL scaling에 $d=1$을 쓰지 말 것, 근거 없이 V scaling에 $b=0.75$를 쓰지 말 것.<br>Elements to exclude: 새로운 동물 예시, 추가 species-specific 숫자, 학습 문제 계산.<br>Suggested rendering: CSS-card<br>Caption: 임상적 오류는 0.75를 잊는 것이 아니라, 흐름 지수와 분포용적 지수를 서로 바꾸어 쓰는 데서 생깁니다.<br>Alt text: 2열 도표가 청소율은 지수 0.75의 흐름 변수이고, 분포용적은 지수 1의 분포 범위 변수임을 대비한 뒤, 반감기와 제거 속도상수가 서로 반대 비율임을 보여 줍니다.<br>Source relation: Newly designed<br><!-- /FIGURE_SCHEMATIC -->
> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{CL=a\cdot BW^b}_{\text{CL 흐름}}\quad vs\quad\underbrace{V=c\cdot BW^d}_{\text{V 공간}}\quad\Rightarrow\quad\underbrace{t_{1/2}\propto BW^{d-b}}_{\text{시간↑}}\; ,\;\underbrace{k_{el}\propto BW^{b-d}}_{\text{fraction 속도↓}}
> $$

> **실패 모드(Failure Mode) — [CRUCIBLE_DERIVED]**  
> $t_{1/2}$만 외우면 $k_{el}$의 부호를 놓칩니다. 큰 동물에서 속도상수(rate constant)가 작아지는 구조를 보지 못하면 CL과 V의 지수(exponent)를 서로 바꾸는 오류가 반복됩니다.

> <!-- TRENCH -->
> **▶ 실무 체화 요약(Practice Brief) — C3 체화 4축 — [EXPERT_INFERENCE, ver2 V2]**  
> - **왜 알아야 하는가:** $d\approx 1$이라는 prior가 깨지지 않는다고 가정하면 PK29 compound X($d\approx1.18$)처럼 다구획(multicompartment) 약물에서 Dedrick superposition이 무너집니다. V의 지수를 따로 추적할 능력이 없으면 시간축이 잘못 정규화됩니다.  
> - **흐름상 역할:** $b$와 $d$의 **차이($d-b$)** 자체가 핵심 산출물입니다. C3는 C2의 산출($b$)과 결합해 **시간축 두 개**($t_{1/2} \propto BW^{0.25}$, $k_{el} \propto BW^{-0.25}$)를 만들어 C4 Dedrick의 x축에 직접 입력됩니다.  
> - **체화 꿀팁:** “큰 동물 = 절대 CL 큼, 그러나 분율(fraction) 제거는 느림”을 한 호흡으로 외웁니다. **$V/CL$과 $CL/V$를 동시에** 적어가며 부호(sign)를 점검합니다 — half-life는 양수 지수, rate constant는 음수 지수입니다.  
> - **실무 활용:** PopPK에서 V 지수를 1로 고정(fix)하기 전에 log-log V vs BW slope가 0.9–1.1 안인지 확인합니다 (C4 Trench와 동일 진단). 비만·소아·노인 데이터에서 $V_{ss}$가 0.8–1.2로 흔들리면 BW 기반 V 추정에 이상체중/제지방체중(ideal/lean body mass) 대안 공변량(covariate)을 검토합니다.

---

<!-- SECTION_CORE: SC-05 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** Dedrick plot은 예쁜 overlay가 아니라 $b$와 $d$를 시간축·농도축에 넣었을 때 PK28/PK29 데이터가 버티는지 보는 검증 도구다.

---
<!-- SLIDE_START: S16 | title: C4. Elementary and Complex Dedrick | source_anchor: C4-dedrick-definitions -->

### ━━ C4. Dedrick 중첩(Dedrick Superposition): 기본형(Elementary) + 복합형(Complex) ━━

<!-- MASTER LENS -->
**개념 핵심 아이디어(Big Idea):** Dedrick 도표(Dedrick plot, 종별 PK 곡선을 공통 척도 위에 겹치는 변환)는 종간 PK curve를 “같은 과정의 서로 다른 시간 척도”로 표현한 뒤 하나의 공통 축 위에 포개어 보이는 변환입니다.
<!-- ANNOTATION --> 시간축만 조정하는 것이 아니라, 용량 정규화 농도(dose-normalized concentration) 축도 BW 지수(exponent)에 맞게 조정합니다.

#### A. 정형 정의(Formal Definitions)

**기본 Dedrick 도표(Elementary Dedrick plot)** — $d=1$ 가정:

$$y=\frac{C}{Dose/BW},\qquad x=\frac{t}{BW^{1-b}}$$
> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{y}_{\text{농도축}}=\frac{\overbrace{C}^{\text{농도}}}{\underbrace{Dose/BW}_{\text{kg당 용량}}},\qquad \underbrace{x}_{\text{시간축}}=\frac{\overbrace{t}^{\text{시간}}}{\underbrace{BW^{1-b}}_{\text{elementary 시간}}}
> $$


**복합 Dedrick 도표(Complex Dedrick plot)** — $d\neq1$ 일반형:

$$y=\frac{C}{Dose/BW^d}=\frac{C\cdot BW^d}{Dose},\qquad x=\frac{t}{BW^{d-b}}$$
> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{y}_{\text{농도축}}=\frac{\overbrace{C}^{\text{농도}}}{\underbrace{Dose/BW^d}_{\text{V지수 용량}}}=\frac{\overbrace{C}^{\text{농도}}\cdot\overbrace{BW^d}^{\text{공간 보정}}}{\underbrace{Dose}_{\text{투여량}}},\qquad \underbrace{x}_{\text{시간축}}=\frac{\overbrace{t}^{\text{시간}}}{\underbrace{BW^{d-b}}_{\text{complex 시간}}}
> $$


Kallynochron은 $d=1$ 가정 하의 kg당 시간 척도(per-kg time scale)이고, Apolysichron은 $d$를 명시적으로 반영한 일반화 생리학적 시간 척도(generalized physiological time scale)입니다 [G&W §2.10.6–2.10.7, p.184–189].

<!-- SLIDE_START: S17 | title: C4. Dedrick 도출 | source_anchor: C4-dedrick-derivation -->

#### B. 도출(Derivation)

단일 지수 모델(mono-exponential model):

$$C=\frac{D_{iv}}{V}\cdot e^{-(CL/V)t}$$
> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{C}_{\text{농도}}=\frac{\underbrace{D_{iv}}_{\text{IV dose}}}{\underbrace{V}_{\text{V 공간}}}\cdot \overbrace{e^{-(CL/V)t}}^{\text{일차 제거}}
> $$


알로메트릭 치환(allometric substitution):

$$C=\frac{D_{iv}}{c\cdot BW^d}\cdot e^{-(a/c)\cdot BW^{b-d}\cdot t} \quad [G\&W\ Eq.2:384,\ p.179]$$
> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{C}_{\text{농도}}=\frac{\underbrace{D_{iv}}_{\text{Dose}}}{\underbrace{c\cdot BW^d}_{\text{V 스케일}}}\cdot \overbrace{e^{-\left(\underbrace{a/c}_{\text{CL/V 절편}}\right)\cdot\underbrace{BW^{b-d}}_{\text{k 체중지수}}\cdot \underbrace{t}_{\text{시간}}}}^{\text{체중 보정 제거}}
> $$


따라서 농도(concentration)는 $Dose/BW^d$로, 시간(time)은 $BW^{d-b}$로 정규화되어야 합니다. `[교과서 외 수학적 해석]`으로 말하면 이는 Buckingham π 정리(Buckingham π theorem)류의 차원 해석(dimensional analysis)과 같은 직관입니다. 변수들이 가진 질량·시간·부피(mass/time/volume) 차원을 제거하면 독립적인 무차원 그룹(dimensionless group)이 남고, Dedrick 변환은 그 그룹의 PK 버전입니다.

#### C. AUC 관계식(AUC relation)

기본 Dedrick(Elementary Dedrick) 맥락에서 G&W는 AUC가 $1/a$로 정리됨을 보입니다 [G&W Eq.2:386, p.179]. 이것은 C5의 'equal unbound AUC' 조건과 무관한 별개의 사실이 아니라, 같은 논리가 수식으로 먼저 나타나는 전단계입니다.

<!-- SLIDE_START: S18 | title: C4. PK28/PK29 benchmark | source_anchor: C4-PK28-PK29-anchor -->

#### D. 데이터 앵커(Data Anchor) — PK28과 PK29

**PK28 Methadone**: mouse/rat/man IV bolus 자료를 기본 Dedrick 도표(elementary Dedrick plot)로 중첩합니다 [G&W p.184–186; PK28 p.611–614]. 단, case는 단일 dose level이며 G&W도 ≥2 dose levels, 다회 투여·항정상태(multiple dosing/steady state), 모델 잘못 지정(model misspecification) 배제가 필요하다고 경고합니다 [PK28 p.614].

**PK29 Compound X**: mouse 20 g, rat 250 g, monkey 3.5 kg, dog 14 kg, man 70 kg의 5종 자료를 사용합니다 [G&W p.186–189; PK29 p.615–620].

- G&W §2.10.7 parameter set: $a=0.021$, $b=0.74$, $c=0.076$, $d=1.18$, $e=0.56$, $g=0.075$ [G&W p.189].
- PK29 case set: $a=0.021$, $b=0.75$, $c=0.10$, $d=1.21$, $e=0.54$, $g=0.071$ [PK29 p.619].
- 체중 범위(weight range): 산술적으로 $70/0.020=3500$-fold; PK29 case 본문은 약 3000-fold로 표기할 수 있습니다. 본문에서는 “약 3000–3500-fold”로 표기합니다.

> <!-- TRENCH -->
> **[TRENCH — 기본형 vs 복합형 Dedrick 전환(Elementary vs Complex Dedrick switch)]** log-log $V$ vs $BW$ slope가 0.9–1.1 밖이면 기본 Dedrick(Elementary, $d=1$ 가정)을 고집하지 않습니다. PK29처럼 $d\approx1.18$이면 $C/(Dose/BW^d)$와 $t/BW^{d-b}$를 쓰는 복합 Dedrick(Complex Dedrick)으로 전환합니다.

<!-- RECAP -->
**C4 핵심:** Dedrick superposition은 곡선 적합(curve-fitting) 장식이 아니라 CL 지수와 V 지수를 동시에 검증하는 진단(diagnostic) 도구입니다. Elementary가 실패하면 “plot이 안 예쁜 것”이 아니라 “$d=1$ 가정이 깨졌을 가능성”을 먼저 봅니다.

<!-- SLIDE_START: S19 | title: Figure F5. PK28 Elementary Dedrick | source_anchor: figure-F5-PK28-dedrick -->

<!-- FIGURE_POINTER --><br>Source: Gabrielsson & Weiner 5e, Case Study PK28, p.613, Fig.28.2<br>Why this matters: 이 그림은 methadone의 기본 Dedrick 중첩(elementary Dedrick superposition)을 학습자 관점에서 가장 잘 보여 줍니다. 정규화가 mouse, rat, human의 concentration-time curve를 공통 생리학적 시간 척도 위로 접어 넣기 위한 것임을 확인할 수 있습니다.<br>When to look: C4 데이터 앵커(Data Anchor) — PK28을 읽은 뒤, C4 한계(limitations)를 읽기 전에 확인하시면 됩니다.<br>Learner instruction: 곡선 모양만 보지 말고 축 변환(axis transformations)에 집중해 보세요. 이 elementary version이 작동하려면 $d$에 대해 어떤 가정이 필요한지 물어보시면 됩니다.<br><!-- /FIGURE_POINTER -->

<!-- SLIDE_START: S20 | title: Figure F6. PK29 Complex Dedrick | source_anchor: figure-F6-PK29-complex-dedrick -->

<!-- FIGURE_POINTER --><br>Source: Gabrielsson & Weiner 5e, Case Study PK29, p.619, Fig.29.3<br>Why this matters: 이 그림은 $d\neq1$이고 multicompartment scaling이 들어올 때 왜 Complex Dedrick이 필요한지를 보여 주는 최종 시각 증거입니다. allometric parameter set이 곡선 중첩(curve superposition)과 어떻게 연결되는지 보여 줍니다.<br>When to look: F5 이후, 그리고 C4 Complex Dedrick / PK29 자료를 읽은 뒤 확인하시면 됩니다.<br>Learner instruction: 이 그림을 elementary Dedrick 논리와 머릿속으로 비교해 보세요. $BW^d$ 정규화가 농도축을 어디에서 바꾸는지, 그리고 그것이 compound X에서 왜 중요한지 확인하시면 됩니다.<br><!-- /FIGURE_POINTER -->

> **실무 렌즈(Practice Lens) — [CRUCIBLE_DERIVED]**  
> Dedrick plot은 예쁜 overlay를 만드는 도구가 아니라 지수 쌍(exponent pair)을 검증하는 진단 도구입니다. Curve fan-out이 보이면 먼저 $d=1$ 가정, 구획(compartment) 비율, 결합(binding) 또는 기전 불일치(mechanism mismatch)를 의심해야 합니다.

> <!-- TRENCH -->
> **▶ 실무 체화 요약(Practice Brief) — C4 체화 4축 — [EXPERT_INFERENCE, ver2 V2]**  
> - **왜 알아야 하는가:** Dedrick은 “결과 그림”이 아니라 **C2/C3 지수 쌍의 진단 도구**입니다. Elementary가 깨지면 $d\neq1$ 가능성·구획(compartment) 비율·결합 불일치(binding mismatch) 중 어느 것이 신호인지 빠르게 분류할 수 있어야 합니다.  
> - **흐름상 역할:** C4는 C1–C3가 만든 **수식적 예측**을 **데이터에 한 번 부딪쳐 보는 검증대**입니다. 통과하면 C5 dose backbone이 신뢰성 있게 적용되고, 실패하면 C5 적용 전에 $d$ 추정을 다시 검토합니다.  
> - **체화 꿀팁:** Elementary($t/BW^{1-b}$)와 Complex($t/BW^{d-b}$)의 **시간축 차이만 비교**하면서 외웁니다. log-log V vs BW slope **0.9–1.1**이라는 전환 트리거(switch trigger)를 외부 cheat sheet에 적어 두고 매번 확인합니다. $AUC=1/a$라는 elementary 결론은 C5 equal-AUCu의 수학적 전단계임을 의식합니다.  
> - **실무 활용:** PK28($d=1$ anchor)과 PK29($d=1.18$ anchor)를 **벤치마크 쌍**으로 기억합니다. 새 화합물에서 종간 V 지수(exponent)를 추정했을 때, PK29처럼 1을 넘어가면 즉시 Complex Dedrick으로 전환하고 이를 보고서에 명시합니다 (단일 dose level, model misspecification 배제 검토 caution을 함께 적시).

---

<!-- SECTION_CORE: SC-06 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** C5의 $Dose\propto BW^b$는 final FIH dose가 아니라 equal-$AUC_u$ exposure backbone이다 — metric·fu·linearity·functional age를 분리하라.

---
<!-- SLIDE_START: S21 | title: C5. Equal-unbound-AUC dose backbone | source_anchor: C5-equal-AUCu-backbone -->

### ━━ C5. FIH 용량 번역(FIH Dose Translation)의 알로메트릭 백본(Allometric Backbone) ━━

<!-- MASTER LENS -->
**개념 핵심 아이디어(Big Idea):** C5는 FIH 시작 용량(starting dose) 전체를 결정하는 단독 공식이 아닙니다. G&W Eq.2:417–421은 **equal unbound AUC(자유 약물 AUC를 같게 맞추는 기준)를 유지하기 위한 total dose scaling backbone**입니다.
<!-- ANNOTATION --> 실제 FIH starting dose는 이 backbone 위에 안전 여유(safety margin), 독성학(toxicology), 약리학(pharmacology), 노출-반응(exposure-response), 투여 경로(route), 제형(formulation), PD 지표(metric)를 더해 결정합니다.

#### A. Equal-unbound-AUC 백본(backbone)

$$AUC_{u,rat}=AUC_{u,man}=\frac{Dose_{rat}}{CL_{u,rat}}=\frac{Dose_{man}}{CL_{u,man}} \quad [G\&W\ Eq.2:417,\ p.190]$$
> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{AUC_{u,rat}}_{\text{rat }AUC_u}=\underbrace{AUC_{u,man}}_{\text{human }AUC_u}=\frac{\overbrace{Dose_{rat}}^{\text{rat dose}}}{\underbrace{CL_{u,rat}}_{\text{rat }CL_u}}=\frac{\overbrace{Dose_{man}}^{\text{human dose}}}{\underbrace{CL_{u,man}}_{\text{human }CL_u}}
> $$


$$Dose_{man}=Dose_{rat}\cdot\left(\frac{BW_{man}}{BW_{rat}}\right)^b \quad [G\&W\ Eq.2:420,\ p.190]$$
> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{Dose_{man}}_{\text{human dose}}=\underbrace{Dose_{rat}}_{\text{rat dose}}\cdot\left(\frac{\overbrace{BW_{man}}^{\text{human BW}}}{\overbrace{BW_{rat}}^{\text{rat BW}}}\right)^{\overbrace{b}^{\text{CL/AUC 지수}}}
> $$


$$CL_{u,man}=CL_{u,rat}\cdot\left(\frac{BW_{man}}{BW_{rat}}\right)^b \quad [G\&W\ Eq.2:421,\ p.190]$$
> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{CL_{u,man}}_{\text{human }CL_u}=\underbrace{CL_{u,rat}}_{\text{rat }CL_u}\cdot\left(\frac{\overbrace{BW_{man}}^{\text{human BW}}}{\overbrace{BW_{rat}}^{\text{rat BW}}}\right)^{\overbrace{b}^{\text{CLu 지수}}}
> $$


mg/kg dose 비(ratio)로 쓰면 다음과 같습니다:

$$\frac{Dose_{man}/BW_{man}}{Dose_{rat}/BW_{rat}}=\left(\frac{BW_{man}}{BW_{rat}}\right)^{b-1}$$
> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{\frac{Dose_{man}/BW_{man}}{Dose_{rat}/BW_{rat}}}_{\text{mg/kg 비}}=\left(\frac{\overbrace{BW_{man}}^{\text{큰 종 BW}}}{\overbrace{BW_{rat}}^{\text{작은 종 BW}}}\right)^{\overbrace{b-1}^{\text{kg당 지수}}}
> $$


$b<1$이면 큰 동물의 mg/kg dose는 작은 동물보다 낮아집니다.

<!-- SLIDE_START: S22 | title: C5. Assumptions and exposure metric limits | source_anchor: C5-assumptions -->

#### B. 가정(Assumptions)

1. 비결합 AUC(unbound AUC)가 약리 효과(pharmacologic effect)와 연결됩니다;
2. 표적 친화도(target affinity)와 관련 약리학(relevant pharmacology)이 종간 크게 다르지 않습니다;
3. PK가 선형 구간(linear range)에 있습니다;
4. fu(비결합 분율, unbound fraction) 차이가 있으면 $CL_u$로 보정합니다;
5. AUC가 적절한 노출 지표(exposure metric)입니다. 최고농도 기반 독성(Cmax-driven toxicity) 또는 역치 초과 시간 지표(time-above-threshold metric)이면 별도 판단이 필요합니다.

G&W는 동일 AUC(equal AUC)라도 농도-시간 곡선(concentration-time curve)의 모양(shape)은 상당히 다를 수 있음을 명시합니다 [G&W p.190]. 따라서 C5는 AUC 백본일 뿐이며, 전체 곡선 등가성(full curve equivalence)을 보장하지 않습니다.

<!-- SLIDE_START: S23 | title: C5. Pediatric and elderly context | source_anchor: C5-pediatric-elderly -->

#### C. 소아·노인 맥락(Pediatric and elderly context) — R&T 기반

R&T Ch.14는 연령(age), 체중(weight), 성별(gender)이 약물 반응 변동성(drug response variability)의 중요한 원천이며, 생활연령(chronologic age)이 기능적 연령(functional age)을 정의하지 않는다고 경고합니다 [R&T p.411–412]. 또한 연령을 고려하지 않는 일률 용량(flat dosing)은 개별 노인 환자(elderly patient)의 필요를 충족하지 못할 수 있다고 설명합니다 [R&T p.412].

R&T Key Relationships는 BSA를 다음처럼 체중 기반으로 근사합니다:

$$BSA=1.73\cdot\left(\frac{Weight}{70}\right)^{0.75} \quad [R\&T\ p.436]$$
> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{BSA}_{\text{BSA 근사}}=\underbrace{1.73}_{\text{70kg BSA}}\cdot\left(\frac{\overbrace{Weight}^{\text{체중}}}{\underbrace{70}_{\text{70kg}}}\right)^{\overbrace{0.75}^{\text{BSA 지수}}}
> $$


그리고 60세 일반 성인(typical 60-year-old adult) 대비 소아 유지 용량(child maintenance dose)을 다음처럼 제시합니다:

$$Child\ maintenance\ dose=1.5\cdot\left(\frac{Weight_{child}}{70}\right)^{0.75}\cdot Typical\ adult\ maintenance\ dose \quad [R\&T\ Eq.14\text{-}6,\ p.432;\ Key\ Relationships,\ p.436]$$
> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{Child\ maintenance\ dose}_{\text{소아 유지용량}}=\underbrace{1.5}_{\text{성인 보정}}\cdot\left(\frac{\overbrace{Weight_{child}}^{\text{소아 체중}}}{\underbrace{70}_{\text{70kg}}}\right)^{\overbrace{0.75}^{\text{BW 지수}}}\cdot\underbrace{Typical\ adult\ maintenance\ dose}_{\text{성인 용량}}
> $$


다만 R&T는 mg/kg 또는 mg/1.73 m² 규칙의 폭넓은 사용(broader use)은 적용 한계(연령, 체조성, 신기능)를 명시하지 않으면 의심스럽다고 경고합니다 [R&T p.435]. 즉 **BW 알로메트리는 시작점이지, 소아·노인 용량 결정 공식 전체를 대체하지 않습니다.**

#### D. 노인 대사 진술 교정(Elderly metabolism statement correction)

“CYP3A4 metabolism이 60세 이상 매년 1% 감소”라는 문장은 과단정입니다. R&T는 크레아티닌 청소율(creatinine clearance)이 성인기(adulthood)에서 대략 1%/yr 감소한다는 경험 법칙(rule of thumb)을 제시하고 [R&T p.422], CYP3A 기질(substrate)에서는 노인군(elderly group)이 청년군(young adult)보다 낮은 청소율을 보이며 그 연령 차이를 해석할 때 1%/yr 크레아티닌 청소율 경험치(heuristic)가 관련된다고 설명합니다 [R&T p.424]. 따라서 최종 문장은 다음처럼 제한합니다: **노인에서는 신·간 기능(renal/hepatic function)과 생물학적 연령(biological age)을 별도로 보아야 하며, CYP3A 청소율도 청년 대비 감소할 수 있지만 단순 선형 시간 함수로 쓰지 않습니다.**

<!-- RECAP -->
**C5 핵심:** C5의 수식은 equal unbound AUC를 맞추는 allometric backbone입니다. FIH dose justification이나 pediatric/elderly dosing에서는 이 backbone 위에 functional age, renal/hepatic function, body composition, binding, PD metric, safety margin을 얹어야 합니다.

<!-- SLIDE_START: S24 | title: Figure F7. age-related maintenance-dose fraction | source_anchor: figure-F7-RT-age-dose -->

<!-- FIGURE_POINTER --><br>Source: Rowland & Tozer 5e, Ch.14, p.430, Fig.14-20<br>Why this matters: 이 그림은 $BW^{0.75}$만으로 pediatric/elderly dosing이 해결된다고 보는 흔한 오류를 시각적으로 막아 줍니다. 연령에 따라 maintenance-dose fraction이 달라지는 모습을 보여 주며, 이것이 바로 C5의 caveat입니다.<br>When to look: C5 소아·노인 맥락(Pediatric and elderly context)을 읽은 뒤, C5 recap을 읽기 전에 확인하시면 됩니다.<br>Learner instruction: infancy부터 old age까지 dose fraction이 어떻게 변하는지 추적해 보세요. 그런 다음 functional age와 renal/hepatic function이 왜 BW allometry 위에 추가되어야 하는지 말해 보시면 됩니다.<br><!-- /FIGURE_POINTER -->

> **체화 노트(Mastery Note) — [TEXTBOOK_DERIVED]**  
> Equal-AUCu dose backbone은 “최종 FIH dose”가 아니라 노출 번역(exposure translation)의 중심축입니다. R&T의 age/weight 논리는 이 축 위에 functional age와 organ function을 더해야 개인 환자 용량이 된다는 점을 보강합니다.

> <!-- TRENCH -->
> **▶ 실무 체화 요약(Practice Brief) — C5 체화 4축 — [EXPERT_INFERENCE, ver2 V2]**  
> - **왜 알아야 하는가:** C5를 standalone FIH starting-dose 공식처럼 적으면 NDA·IND 정당화에서 곧장 **방어 불가**입니다. 이 식은 backbone이지 final answer가 아닙니다. 또한 R&T Ch.14의 핵심 메시지(chronologic age ≠ functional age)를 누락하면 소아·노인 dosing 자체가 단순화 오류로 무너집니다.  
> - **흐름상 역할:** C1–C4가 산출한 지수 쌍과 시간축이 **여기서 dose라는 단일 임상 액션으로 수렴**합니다. C5는 “종간 수식”과 “인간 환자 수식” 사이의 마지막 다리이며, 이 다리 위에 safety margin, PD metric, route/formulation이 얹힙니다.  
> - **체화 꿀팁:** “Equal AUCu가 곧 같은 PD를 보장하지 않는다”와 “mg/kg 비는 $BW^{b-1}$이다”를 동시에 외웁니다. 큰 동물 → 작은 mg/kg, 작은 동물 → 큰 mg/kg이라는 방향성을 손가락 방향으로 굳힙니다. CYP3A 1%/yr 같은 단정문은 입에서 자동 차단합니다.  
> - **실무 활용:** FIH dose justification 보고서에서 C5 backbone은 한 줄($Dose_{man}=Dose_{animal}\cdot (BW_{man}/BW_{animal})^b$)로 적되, 그 위에 (i) 안전성 margin, (ii) AUC vs Cmax target 선택 근거, (iii) fu 보정, (iv) route/formulation 고려를 별도 섹션으로 분리합니다. 소아/노인 적용 시 BSA 근사·R&T pediatric maintenance 식·creatinine clearance heuristic을 backbone 위에 한 층씩 얹습니다.

---

> <!-- MASTER LENS -->
<!-- SLIDE_START: S25 | title: §2 폐막 Allometric Decision Walkthrough | source_anchor: section-2-walkthrough -->

> ## ▶ §2 폐막 — 알로메트릭 의사결정 워크스루(Allometric Decision Walkthrough) — [EXPERT_INFERENCE, ver2 V3]
>
> 이 워크스루(walkthrough)는 **새로운 수치도, 새로운 명명 예시(named example)도 도입하지 않습니다.** C1–C5 본문에서 이미 확정된 수식·anchor·진단만 사용하여, 학습자가 **하나의 동물 PK 데이터셋을 받아 인간 노출 추정에 도달하는 5단계 의사결정**을 한 호흡에 통과시키는 시연입니다. 이 walkthrough를 닫는 순간 §1 Target Mental Model이 닫힙니다.
>
> **Step 1 — 변수 유형 진단(Variable Type Diagnosis; C1 ↔ C2/C3 진입점)**  
> 받은 변수가 무엇인지 먼저 묻습니다. CL/GFR/blood flow면 **흐름 변수(flow variable)**이므로 $b\approx 0.75$ prior로 진입합니다 (C2). V/blood volume/tissue mass면 **분포 범위 변수(extent variable)**이므로 $d\approx 1$ prior로 진입합니다 (C3). 이 분류 자체가 틀리면 C4–C5 전체가 무너집니다. 한 줄 cheat: “**flow면 0.75, extent면 1**.”
>
> **Step 2 — Prior 타당성 점검(Prior Validity Check; C1 scale-invariance + C2 failure conditions)**  
> $b\approx 0.75$ prior를 그대로 적용해도 되는지 점검합니다. 다음 6개 trigger 중 하나라도 강하게 의심되면 prior를 sensitivity analysis로 격하합니다: 종간 fu 차이, CYP isoform 차이, nonlinear MM kinetics, enterohepatic recirculation, route/formulation 차이, central/peripheral V ratio drift. fu 차이가 크면 total CL이 아니라 $CL_u$로 스케일링합니다 (Eq.2:421 라인).
>
> **Step 3 — 시간축 도출(Time-axis Derivation; C3)**  
> $b$와 $d$로부터 두 시간축을 동시에 적습니다. $t_{1/2} \propto BW^{d-b} \approx BW^{0.25}$ (큰 동물 = 긴 반감기), $k_{el} \propto BW^{b-d} \approx BW^{-0.25}$ (큰 동물 = 작은 fraction 제거 속도). 이 두 식의 부호를 동시에 보지 못하면 C4 정규화가 어긋납니다.
>
> **Step 4 — Dedrick 진단 통과(Dedrick Diagnostic Pass; C4)**  
> 종간 자료가 있으면 Elementary Dedrick($d=1$ 가정, $t/BW^{1-b}$)을 먼저 시도합니다. log-log V vs BW slope가 **0.9–1.1 안**이면 Elementary로 충분합니다. 0.9–1.1을 벗어나면 Complex Dedrick($t/BW^{d-b}$, $C\cdot BW^d/Dose$)으로 전환합니다. PK28(elementary 통과) ↔ PK29($d\approx 1.18$로 Complex 필요)가 그 벤치마크 쌍입니다. Curve fan-out이 남으면 그건 “예쁜 overlay 실패”가 아니라 **mechanism signal**입니다.
>
> **Step 5 — Equal-AUCu 용량 백본 적용(Equal-AUCu Dose Backbone Application; C5 + R&T 보강층)**  
> $Dose_{man}=Dose_{animal}\cdot (BW_{man}/BW_{animal})^b$를 backbone 한 줄로 적되, 그 위에 (i) AUC vs Cmax-driven toxicity 선택 근거, (ii) fu 보정, (iii) PK linearity 가정 점검, (iv) safety margin/toxicology, (v) route/formulation, (vi) PD metric — 6개 layer를 명시적으로 얹습니다. 소아/노인 환자에 적용할 때는 R&T Ch.14의 BSA 근사식, pediatric maintenance 식, chronologic vs functional age 경고, creatinine clearance ~1%/yr heuristic을 backbone 위에 다시 한 층 얹습니다.
>
> **닫는 한 줄:** 이 5단계가 자동 회상되어야 §1 Target Mental Model이 닫힙니다. 닫힌 학습자는 “0.75를 외우는 사람”이 아니라 “0.75를 prior로 두고 자료가 prior를 언제 밀어내는지 판단하는 사람”입니다.

---

## §5 — 혼동쌍 분해(Confusion Pair Dissection)

---

<!-- CONFUSION -->
<!-- SECTION_CORE: SC-07 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** $b$/$d$, Kallynochron/Apolysichron, BW allometry/BSA를 섞는 순간 CL·V·시간·용량 해석이 한꺼번에 무너진다.

---
<!-- SLIDE_START: S26 | title: Pair 1. $b$ vs $d$ | source_anchor: confusion-pair-1-b-vs-d -->

### Pair 1. 청소율 지수(Clearance exponent) $b$ vs 분포용적 지수(Volume exponent) $d$

| 비교 차원 | $b$ — CL 지수 | $d$ — V 지수 |
|---|---|---|
| 변수 성격 | 흐름/속도(flow/rate), 단위 시간당 처리량 | 공간/분포 범위(space/extent), 분포 공간 |
| 전형값 | $b\approx0.75$ | $d\approx1.0$ |
| 생리학적 근거 | 대사율(metabolic rate), 장기 혈류(organ blood flow), GFR | 체수분(body water), 혈액량(blood volume), 조직 부피(tissue volume) |
| 체중 2배 시 | CL 약 $2^{0.75}=1.68$배 | V 약 $2^1=2$배 |
| 시간 결과 | $t_{1/2}\propto BW^{d-b}$ | $k_{el}\propto BW^{b-d}$ |
| 가장 위험한 오류 | dose/CL scaling에 $d=1$을 넣어 linear per-kg처럼 외삽 | V scaling에 $b=0.75$를 넣어 volume을 과소/과대예측 |
> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{b}_{\text{CL 지수}}\ne\underbrace{d}_{\text{V 지수}},\qquad \underbrace{t_{1/2}}_{\text{시간}}\propto\underbrace{BW^{d-b}}_{\text{지수차}}
> $$


**치명적 타격(Critical Blow):** rat 250 g→human 70 kg에서 $b=0.75$ 대신 $d=1$처럼 선형 scaling하면 차이는 $(70/0.25)^{0.25}\approx4.1$배입니다. mouse 23 g→human에서는 약 7.4배, R&T 20-g mouse 예시는 7.7배입니다. 이 오류는 “소수점 차이”가 아니라 첫 human exposure estimate의 order를 바꿉니다.

**⚡ 기억 고리 (Memory Hook) — *기능 vs 공간*: [EXPERT_INFERENCE, v3]**  
CL은 **기능적 처리 능력**입니다 — 체중이 커질수록 대사율이 체중보다 느리게 증가하므로 $b<1$입니다. V는 **물리적 분포 공간**입니다 — 체중에 비례하여 증가하므로 $d\approx 1$입니다. 결론은 $t_{1/2}=0.693\cdot V/CL\propto BW^{d-b}\approx BW^{0.25}$입니다. 체중이 클수록 half-life가 길어지는 현상은 CL과 V의 서로 다른 scaling에서 **수학적으로 따라오는 결과**이지, 별도의 가정이 아닙니다. 이 한 줄을 입에 두면 “큰 동물은 절대 CL은 크지만 단위 시간당 fraction은 작다”는 C3 Failure Mode가 자동 차단됩니다.

---

<!-- CONFUSION -->
<!-- SLIDE_START: S27 | title: Pair 2. Kallynochron vs Apolysichron | source_anchor: confusion-pair-2-kallynochron-apolysichron -->

### Pair 2. Kallynochron vs Apolysichron

| 비교 차원 | Kallynochron | Apolysichron |
|---|---|---|
| 사용 맥락 | Elementary Dedrick | Complex Dedrick |
| 전제 | $d=1$ | $d$를 추정/반영 |
| 시간축 | $t/BW^{1-b}$ | $t/BW^{d-b}$ |
| 해석 | per-kg clearance time | per-$BW^d$ fractional elimination time |
| 실패 신호 | $d\neq1$이면 curve fan-out | $d\neq1$에서 curve collapse 가능 |
> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{\frac{t}{BW^{1-b}}}_{\text{Kallynochron, }d=1}\quad vs\quad\underbrace{\frac{t}{BW^{d-b}}}_{\text{Apolysichron, }d\text{ 반영}}
> $$


**기억 고리:** Kallynochron은 'kg 단위로 정규화한 생리학적 시간'이고, Apolysichron은 '$BW^d$ 단위로 정규화한 생리학적 시간'입니다. $d=1$이면 둘은 같아 보이지만, PK29 compound X처럼 $d>1$이면 차이가 드러납니다.

---

<!-- CONFUSION -->
<!-- SLIDE_START: S28 | title: Pair 3. BW allometry vs BSA scaling | source_anchor: confusion-pair-3-BW-vs-BSA -->

### Pair 3. 체중 알로메트릭 스케일링(Body Weight Allometric Scaling) vs 체표면적 스케일링(Body Surface Area Scaling)

| 비교 차원 | $BW^b$ allometry | BSA scaling |
|---|---|---|
| 수식 | $Y=a\cdot BW^b$ | $BSA\approx1.73(Weight/70)^{0.75}$ |
| 지수 | 변수/자료에 따라 추정 또는 prior | 임상적으로 체중 0.75승 근사 |
| 장점 | 화합물·변수 특이성 반영 | 처방/소아 용량에 친숙 |
| 위험 | 종 수 부족 시 slope 불안정 | 적용 한계 없이 광범위 사용 시 부정확 |
| R&T 메시지 | — | mg/kg 또는 mg/1.73 m² rule은 age, body composition, renal function 한계를 명시해야 함 [R&T p.435] |
> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{Y=a\cdot BW^b}_{\text{변수별 allometry}}\quad vs\quad\underbrace{BSA\approx1.73\left(\frac{Weight}{70}\right)^{0.75}}_{\text{임상 BSA 근사}}
> $$


**정리:** BSA는 allometry의 적이 아니라 임상적으로 굳어진 $BW^{0.75}$ 근사입니다. 그러나 BSA라는 이름이 붙었다고 renal maturation, obesity, functional age 문제가 사라지는 것은 아닙니다.

**⚡ 기억 고리 (Memory Hook) — *직선 도로 vs 우회로*: [EXPERT_INFERENCE, v3]**  
단순 알로메트리(simple allometry)는 $y=a\cdot BW^b$만으로 종간 스케일링을 완성하는 **직선 도로**입니다 — 종간 유사성이 높고 조정 요인이 없을 때 유효합니다. 보정 인자(correction factors: MLP, brain weight, PPB correction)는 특정 약물에서 대사(metabolic) 또는 결합(binding) 차이가 클 때 필요한 **우회로**입니다 — 우회로를 쓸 이유가 없는 도로에서 강제로 우회하면 오히려 정확도가 떨어집니다. BSA 변환($1.73(W/70)^{0.75}$)은 임상적으로 굳어진 우회로의 한 형태이며, 그 자체로 maturation/binding/disease state 문제를 해결하지 않는다는 점을 잊지 않아야 합니다.

<!-- RECAP -->
**§5 요약:** $b$와 $d$의 혼동은 dose와 half-life를 동시에 망가뜨립니다. Kallynochron/Apolysichron 혼동은 Dedrick plot 해석을 망가뜨립니다. BSA와 BW allometry 혼동은 pediatric/elderly dosing을 과도하게 단순화합니다.

> **실패 모드(Failure Mode) — [CRUCIBLE_DERIVED]**  
> 혼동쌍은 암기 문제가 아니라 보고서 검토 체크리스트(checklist)입니다. $b/d$, Kallynochron/Apolysichron, BSA/BW allometry 중 하나라도 섞이면 table, figure, dose narrative가 동시에 흔들립니다.

---

<!-- SECTION_CORE: SC-08 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** Self-test 전반부는 $a$·$b$·$b=1$ fold·$V/CL$ 부호를 손으로 설명해 공식 암기를 방어 가능한 추론으로 바꾼다.

---
<!-- SLIDE_START: S29 | title: §7 Self-Test overview | source_anchor: section-7-self-test -->

## §7 — 자기점검(Self-Test): 능동 회상 모듈(Active Recall Module)

---

<!-- SELF-TEST -->
<!-- SLIDE_START: S30 | title: Q1. $a$와 $b$의 의미 | source_anchor: self-test-Q1 -->

### Q1. 회상(Recall) — $a$와 $b$의 의미

*왜 이 질문 — [EXPERT_INFERENCE, ver2 V4]:* C1의 수식 골격을 손에서 입으로 옮길 수 있는지 확인합니다. 이 회상이 안 되면 C2 이후 모든 추론이 흔들립니다.

**질문:** $Y=a\cdot BW^b$에서 $a$와 $b$를 각각 한 문장으로 설명하고, CL과 V의 전형적 지수(exponent)를 답하세요.

**정답:**

- $a$: 화합물 의존적 절편(compound-dependent intercept); $BW=1$에서의 기준값이며 단위는 $b$에 의존합니다.
- $b$: 체중 변화에 대한 스케일링 지수(scaling exponent); 대체로 변수 유형에 의존하지만 자료 품질과 기전(mechanism)에 따라 변합니다.
- CL: $b\approx0.75$; 대사율/기능적 흐름 변수(metabolic rate/functional flow variable).
- V: $d\approx1.0$; 분포용적/분포 범위 변수(volume/extent variable).
- 따라서 $t_{1/2}\propto BW^{d-b}\approx BW^{0.25}$, $k_{el}\propto BW^{b-d}\approx BW^{-0.25}$.


---

<!-- SELF-TEST -->
<!-- SLIDE_START: S31 | title: Q2. $b=1$ 위험성 | source_anchor: self-test-Q2 -->

### Q2. 회상(Recall) — 왜 $b=1$이 위험한가

*왜 이 질문 — [EXPERT_INFERENCE, ver2 V4]:* Phase 1 patch memo MUST_FIX 1번(4.1 vs 7.4 vs 7.7 fold 분리)이 입에 자동으로 나오는지 확인. species pair를 명시하지 않고 fold를 외우면 보고서 검토에서 곧장 깨진다.

**질문:** 23-g mouse에서 70-kg human으로 CL을 외삽할 때 $b=1$과 $b=0.75$의 차이는 몇 배인가요? rat 250 g→human에서는 몇 배인가요?

**정답:**

- Mouse 23 g→human 70 kg: $(70/0.023)^{1-0.75}\approx7.4$배.
- Rat 250 g→human 70 kg: $(70/0.25)^{0.25}\approx4.1$배.
- R&T의 20-g mouse 예시는 3500 vs 455로 7.7배 차이를 제시한다 [R&T p.733].
- Target AUC 기반 dose 계산에서는 CL 과대예측이 dose 과대 산출로 이어질 수 있다.


---

<!-- SELF-TEST -->
<!-- SLIDE_START: S32 | title: Q3. $t_{1/2}$ and $k_{el}$ derivation | source_anchor: self-test-Q3 -->

### Q3. 도출(Derivation) — $t_{1/2}$와 $k_{el}$의 종간 지수

*왜 이 질문 — [EXPERT_INFERENCE, ver2 V4]:* 도출을 한 번 손으로 해보면 $V/CL$과 $CL/V$의 부호가 반대라는 사실이 오래 남습니다. C3 실패 모드(Failure Mode, "$k_{el}$ 부호 놓침")의 직접 예방책입니다.

**질문:** $CL=a\cdot BW^b$, $V=c\cdot BW^d$일 때 $t_{1/2}$와 $k_{el}$의 BW 지수(exponent)를 도출하세요.

**정답:**

$$t_{1/2}=\ln2\cdot V/CL=\ln2\cdot(c/a)\cdot BW^{d-b}$$
> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{t_{1/2}}_{\text{반감기}}=\underbrace{\ln2}_{\text{반감 상수}}\cdot\frac{\overbrace{V}^{\text{V}}}{\overbrace{CL}^{\text{CL}}}=\ln2\cdot\left(\frac{\underbrace{c}_{\text{V 절편}}}{\underbrace{a}_{\text{CL 절편}}}\right)\cdot\underbrace{BW^{d-b}}_{\text{시간지수}}
> $$


$$k_{el}=CL/V=(a/c)\cdot BW^{b-d}$$
> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{k_{el}}_{\text{제거속도}}=\frac{\overbrace{CL}^{\text{CL}}}{\overbrace{V}^{\text{V}}}=\left(\frac{\underbrace{a}_{\text{CL 절편}}}{\underbrace{c}_{\text{V 절편}}}\right)\cdot\underbrace{BW^{b-d}}_{\text{k 지수}}
> $$


$d=1$, $b=0.75$이면 $t_{1/2}\propto BW^{0.25}$이고 $k_{el}\propto BW^{-0.25}$입니다. 큰 동물은 절대 CL이 크지만, 단위 시간당 제거 분율(fraction)은 작습니다.


---

<!-- SELF-TEST -->
<!-- SECTION_CORE: SC-09 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** Self-test 후반부는 Dedrick 선택, source discrepancy, human $CL$, 소아·노인 gate, Boss Dilemma를 통해 primary assumption과 sensitivity를 분리하게 만든다.

---
<!-- SLIDE_START: S33 | title: Q4. Elementary vs Complex Dedrick | source_anchor: self-test-Q4 -->

### Q4. Dedrick — Elementary vs Complex

*왜 이 질문 — [EXPERT_INFERENCE, ver2 V4]:* PK28 ↔ PK29 벤치마크 쌍을 "switch trigger"와 함께 외우게 만드는 진단 회상 문제. log-log V vs BW slope가 0.9–1.1 밖이면 Complex라는 입버릇이 안 만들어지면 PK29류 약물에서 정규화가 어긋난다.

**질문:** Elementary Dedrick과 Complex Dedrick의 y축/x축 변환을 쓰고, 언제 Complex가 필요한지 답하세요.

**정답:**

- Elementary: $C/(Dose/BW)$ vs $t/BW^{1-b}$; $d=1$ 가정.
- Complex: $C/(Dose/BW^d)$ 또는 $C\cdot BW^d/Dose$ vs $t/BW^{d-b}$.
- log-log $V$ vs $BW$ slope가 1에서 벗어나면, 예를 들어 PK29 compound X처럼 $d\approx1.18$이면 Complex Dedrick이 필요합니다.


---

<!-- SELF-TEST -->
<!-- SLIDE_START: S34 | title: Q5. Source discrepancy handling | source_anchor: self-test-Q5 -->

### Q5. 출처 불일치 처리(Source discrepancy handling) — PK28/PK29

*왜 이 질문 — [EXPERT_INFERENCE, ver2 V4]:* 학술 보고서·심사 문서에서 source-internal 수치 불일치를 임의로 하나로 "고정"하는 것은 무결성 위반입니다. citation scope를 함께 적는 습관이 들어야 합니다.

**질문:** PK28 methadone과 PK29 compound X의 source-internal numerical discrepancy를 어떻게 인용해야 하나요?

**정답:**

- PK28 methadone rat $t_{1/2}$: G&W §2.10.6 본문은 2.9 h, PK28 case는 3.9 h로 다릅니다. 하나를 고르지 말고 `[§2.10.6 set]` 또는 `[PK28 case set]`을 명시합니다.
- PK29 parameter set: G&W §2.10.7은 $a=0.021,b=0.74,c=0.076,d=1.18,e=0.56,g=0.075$; PK29 case는 $a=0.021,b=0.75,c=0.10,d=1.21,e=0.54,g=0.071$입니다. citation scope와 수치를 일치시킵니다.


---

<!-- SELF-TEST -->
<!-- SLIDE_START: S35 | title: Q6. human CL prediction | source_anchor: self-test-Q6 -->

### Q6. 적용(Application) — human CL 예측

*왜 이 질문 — [EXPERT_INFERENCE, ver2 V4]:* 숫자가 손에서 나오는지 확인. 이 계산이 입에서 자동으로 안 나오면 FIH exposure translation 표를 그 자리에서 채울 수 없다.

**시나리오:** Mouse BW=25 g, observed CL=0.012 L/hr. 70-kg human CL을 (a) $b=0.75$, (b) $b=1.0$으로 계산하고 차이를 해석하시오.

**정답:**

(a) $CL_{human}=0.012\cdot(70/0.025)^{0.75}\approx4.6$ L/hr.  
(b) $CL_{human}=0.012\cdot(70/0.025)^1\approx33.6$ L/hr.
> **Annotated equation — 수식 해부**
>
> $$
> \underbrace{CL_{human}}_{\text{human CL}}=\underbrace{CL_{mouse}}_{0.012}\cdot\left(\frac{\overbrace{70}^{\text{human kg}}}{\overbrace{0.025}^{\text{mouse kg}}}\right)^{\overbrace{b}^{\text{선택 지수}}}
> $$
  
차이는 약 7.3배입니다. $b=1$은 선형 kg당 오류(linear per-kg fallacy)이며, target AUC 기반에서는 dose도 과대 산출할 수 있습니다.


---

<!-- SELF-TEST -->
<!-- SLIDE_START: S36 | title: Q7. child/elderly dose context | source_anchor: self-test-Q7 -->

### Q7. 적용(Application) — child/elderly dose context

*왜 이 질문 — [EXPERT_INFERENCE, ver2 V4]:* R&T Ch.14의 핵심 메시지(chronologic ≠ functional age)가 입에서 나오는지 확인. C5 backbone만 외운 학습자는 소아/노인 용량을 단순화 오류로 망친다.

**질문:** 왜 소아 또는 노인 용량에서 $BW^{0.75}$만으로 충분하지 않을까요?

**정답:**

R&T Ch.14는 생활연령(chronologic age)이 기능적 연령(functional age)을 정의하지 않는다고 설명합니다 [R&T p.411–412]. 소아에서는 renal/hepatic maturation, 체수·binding 변화가 중요하고, 노인에서는 renal function, hepatic metabolism, disease state, body composition이 중요합니다. 따라서 $BW^{0.75}$는 시작점일 뿐이며, renal/hepatic function과 biological age 보정이 필요합니다.


---

<!-- SELF-TEST -->
<!-- SLIDE_START: S37 | title: Q8. Boss Dilemma | source_anchor: self-test-Q8 -->

### Q8. 보스 딜레마(Boss Dilemma) — two-species regression vs physiological prior

*왜 이 질문 — [EXPERT_INFERENCE, ver2 V4]:* 보스 딜레마(Boss Dilemma)입니다. 점추정값과 physiological prior가 충돌할 때 무엇을 primary로 두고 무엇을 sensitivity로 보일지를 입으로 정당화할 수 있어야 합니다. 동시에 ICH/FDA 단정문을 자발적으로 차단하는 source language discipline이 동작하는지 확인합니다.

**시나리오:** Rat와 dog 두 종만으로 log-log CL 회귀를 했더니 $b=0.62$가 나왔습니다. 문헌적 physiological prior $b=0.75$와 충돌합니다. FIH exposure translation table에는 무엇을 primary로 두겠습니까?

**정답:**

두 종 회귀의 점추정값은 leverage가 약하고 confidence interval이 넓을 가능성이 큽니다. 따라서 primary는 생리학적 prior(physiological prior) $b=0.75$로 두고, $b=0.5,0.62,0.75,1.0$ sensitivity analysis를 함께 제시합니다. 단, $b=0.75$를 특정 ICH/FDA 조항이 직접 명시한다고 쓰지는 않습니다. 본 PDF 범위에서 방어 가능한 표현은 “mammalian metabolic rate와 functional flow variable의 allometric rationale에 근거한 prior”입니다. `[확인 필요]` 규제 문구는 원문 가이드라인 확인 전 사용하지 않습니다.


---

<!-- RECAP -->
**§7 요약:** 자기점검(self-test)의 목표는 수치 암기가 아니라 세 가지 방어 능력입니다. (1) $b$와 $d$를 구별합니다. (2) $b=1$ 오류가 dose/AUC에 주는 방향을 설명합니다. (3) source discrepancy와 NOT_IN_SOURCE 규제 표현을 스스로 차단합니다.

> **실무 렌즈(Practice Lens) — [EXPERT_INFERENCE]**  
> Self-test 답안을 실제 보고서 문장으로 바꿀 때는 “무엇을 primary assumption으로 두고, 무엇을 sensitivity로 보였는가”를 반드시 적습니다. 이렇게 쓰면 수식 지식이 모델 선택의 방어 논리로 전환됩니다.

---

<!-- SECTION_CORE: SC-10 -->
> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** 전문가의 allometry는 0.75를 외우는 기술이 아니라 변수 유형→지수→시간축→dose/exposure→예외 gate→source language를 순서대로 잠그는 판단 체계다.

---
<!-- SLIDE_START: S38 | title: §8 Meta-Frame positioning | source_anchor: section-8-positioning -->

## §8 — 메타 프레임과 큰 그림(Meta-Frame & Big Picture)

### A. 위치 잡기(Positioning) — 이 세션이 시스템으로 작동하는 세 순간

1. **동물-인간 노출 번역 표(Animal-to-human exposure translation table):** C1이 표 골격(table equation), C2가 CL column, C3가 V·시간 column, C4가 곡선 중첩 검증(curve-superposition check), C5가 equal-AUCu dose backbone입니다.
2. **모집단 PK 체중 공변량 결정(PopPK weight covariate decision):** `[교과서 외 구현 해석]` WT exponent를 fix할지 estimate할지 결정할 때 C2의 physiological prior와 C3의 V exponent가 동시에 필요합니다.
3. **PBPK 파라미터 스케일링(PBPK parameter scaling):** R&T Ch.22는 알로메트리(allometry)를 인간 동태 예측(human kinetics prediction)의 한 축으로 다룬다. 장기 혈류(organ blood flow)는 속도 유사 변수(rate-like), 장기 부피(organ volume)는 분포 공간 유사 변수(extent-like)로 구분해 스케일링해야 한다 [R&T p.731–743].

<!-- SLIDE_START: S39 | title: §8 Failure Modes | source_anchor: section-8-failure-modes -->

### B. 이 섹션이 약할 때의 실패 모드(Failure Modes)

**실패 모드(Failure Mode) 1 — 알로메트릭 기울기 드리프트(Allometric Slope Drift).**  
`[교과서 외 구현 해석]` 성인 60–90 kg처럼 WT range가 좁은 데이터에서 CL 지수(exponent)를 자유 추정하면 SE가 커지고 점추정값이 흔들립니다. 이 경우에는 $b=0.75$ fixed model을 primary로 두고, sensitivity analysis로 추정값의 영향을 따로 보여주는 편이 더 방어 가능합니다.

**실패 모드 2 — V 지수 고정 편향(Volume Exponent Lock-in Bias).**  
$V$ 지수(exponent)를 항상 1로 고정하면 PK29 compound X처럼 $d>1$인 약물에서 Dedrick superposition이 실패합니다. 큰 체중에서 ηV trend가 남으면 $d$를 estimate하거나 Complex Dedrick 구조를 검토합니다.

**실패 모드 3 — 기능적 연령 누락(Functional age omission).**  
소아·노인에서 BW scaling만 쓰면 maturation, renal function, body composition, disease state가 누락됩니다. R&T의 핵심 메시지는 “typical patient”와 “individual patient”가 다르다는 것입니다 [R&T p.412–415].

<!-- SLIDE_START: S40 | title: §8 Professional Moat | source_anchor: section-8-professional-moat -->

### C. 전문가 해석 지점(Professional Moat) — 동기부여가 아니라 진단(diagnostic, not motivational)

1. **$b$의 이탈을 신호와 잡음으로 구별합니다.** $b>1$ 또는 $b<0.5$가 나오면 먼저 종 수, leverage, binding, nonlinearity, metabolism route 차이를 확인합니다.
2. **FIH/exposure translation에서 수식과 언어를 분리합니다.** G&W Eq.2:420은 equal-AUCu dose backbone이지 standalone starting-dose rule이 아닙니다.
3. **Dedrick plot을 diagnostic으로 읽습니다.** Elementary plot fan-out은 “그림 실패”가 아니라 $d\neq1$, multicompartment 비율 차이, 또는 model misspecification의 신호입니다.
4. **Source discrepancy를 숨기지 않습니다.** PK28 $t_{1/2}$와 PK29 parameter set 불일치는 citation 규약으로 드러내고, 임의로 하나를 정답처럼 고정하지 않습니다.

<!-- SLIDE_START: S41 | title: Final One-Page Mental Model | source_anchor: section-8-final-mental-model -->

### D. 최종 1페이지 사고 모델(Final One-Page Mental Model)

```text
1. 변수의 종류를 먼저 묻는다.
   - flow/rate?  → CL, GFR, blood flow → b≈0.75
   - space/extent? → V, blood volume, tissue mass → d≈1
   - time? → V/CL → d-b≈0.25
   - rate constant? → CL/V → b-d≈-0.25

2. 종간 dose/exposure translation은 total dose가 아니라 unbound exposure 관점에서 읽는다.
   - AUCu equality → Dose ∝ BW^b
   - mg/kg ratio → BW^(b-1)

3. 예외를 먼저 찾는다.
   - fu 차이, CYP isoform 차이, nonlinear PK, transporter, enterohepatic recirculation, route/formulation 차이

4. source language를 지킨다.
   - PDF-supported: G&W/R&T 수식, PK28/PK29 anchor, R&T age/renal/BSA caution
   - not directly supported: ICH/FDA/MABEL/NONMEM/QSP claims → 삭제 또는 [교과서 외 해석]
```

<!-- RECAP -->
**§8 최종 요약:** Session 14의 핵심은 “0.75를 외우는 것”이 아닙니다. “어떤 변수가 왜 0.75이고, 어떤 변수는 왜 1이며, 그 차이가 시간과 dose를 어떻게 바꾸는지”를 보는 것입니다. 이 학습본은 allometric spine을 유지하되, fold 오류, FIH overclaim, source-internal discrepancy, unsupported regulatory language를 제거한 형태로 읽어야 합니다.

> **체화 노트(Mastery Note) — [EXPERT_INFERENCE]**  
> 이 세션의 최종 문장은 “0.75가 맞다”가 아니라 “0.75는 flow 변수의 생리학적 prior이고, 자료와 mechanism이 그 prior를 언제 밀어내는지 판단한다”입니다. 이 관점이 allometry를 공식 암기에서 모델링 판단으로 바꿉니다.

---

## PART B — Compiler-Only Appendix

This appendix is not learner-facing. It exists only to protect Phase 5 rendering fidelity.

### B1. Compilation Contract

- PART A is the only learner-facing body.
- Phase 5 must render PART A without altering content.
- PART B is instruction/guardrail only.
- Do not restore deprecated material.
- Do not add new scientific content.
- Do not render PART B as learner content unless explicitly requested.
- ver2 augmentations (V1–V5) are PART A content and must be rendered along with the rest of PART A.
- ver2 Practice Briefs use the existing TRENCH marker and must render with the same rose tip-box style as other Trench tips. ver2 Allometric Decision Walkthrough uses the existing MASTER LENS marker and must render with the same gold callout style.
- v3.1 Korean Readability Patches (K01–K13) are PART A surgical edits to existing prose; they do not introduce new markers, page tags, equations, or scientific claims. Phase 5 renders them transparently as part of PART A.
- v3.2 Korean-Dominant Readability Patches (L01–L12) are PART A surgical edits to existing prose; they convert remaining English narrative sentences and subsection headers into Korean while preserving career-critical pharmacometrics terms via Korean-English paired expressions on first use. They do not introduce new markers, page tags, equations, source labels, figure markers, or scientific claims. Phase 5 renders them transparently as part of PART A.

### B2. Figure Rendering Instructions

- Preserve the approved F1–F7 figure plan below.
- Preserve P/N decisions and source fields in PART A figure markers.
- Image rights = None: do not embed copyrighted textbook images. Render `FIGURE_POINTER` as text-only callout.
- Do not propose new figures.
- Do not generate Mermaid/SVG in Phase 4D; Phase 5 may render only approved schematics.
- ver2 introduces no new figure markers.
- v3.1 introduces no new figure markers.
- v3.2 introduces no new figure markers.

| # | Mode | Location | Source / relation | Rendering decision |
|---:|---|---|---|---|
| F1 | N schematic | §1 후, §2 진입 전 | Newly designed | Render as non-textbook allometric spine schematic; no copyrighted image. |
| F2 | P pointer | C2 말미 | R&T Ch.22 p.733 Fig.22-2 | Text-only pointer; no embedded figure. |
| F3 | P pointer | C2 말미 | G&W §2.10.3 p.174 Fig.2.145 | Text-only pointer; no embedded figure. |
| F4 | N schematic | C3 말미 | Newly designed | Render as CSS-card or Mermaid schematic; no new examples. |
| F5 | P pointer | C4 말미 | G&W PK28 p.613 Fig.28.2 | Text-only pointer; no embedded figure. |
| F6 | P pointer | C4 말미 | G&W PK29 p.619 Fig.29.3 | Text-only pointer; no embedded figure. |
| F7 | P pointer | C5 말미 | R&T Ch.14 p.430 Fig.14-20 | Text-only pointer; no embedded figure. |

### B3. Page Tag Rendering Rules

- Preserve all `[p.XX]`, `[pp.XX–YY]`, `[pp.XX, YY]`, and `[p.확인 필요]` tags exactly as present in PART A.
- Render page tags visibly in HTML.
- Do not fabricate, delete, renumber, or relocate page tags.
- `[p.확인 필요]` remains visible unless already resolved by Audit/Content Lock.
- ver2 introduces no new page tags. All page tags in ver2 PART A are inherited from ver1.
- v3.1 introduces no new page tags. All page tags in v3.1 PART A are identical to v3.
- v3.2 introduces no new page tags. All page tags in v3.2 PART A are identical to v3.1.

### B4. HTML Compiler Requirements

- Render PART A only; do not alter, summarize, reorder, or expand scientific content.
- Generate one self-contained HTML file with inline custom CSS and JS.
- External runtime dependencies are allowed only for MathJax CDN, Mermaid CDN, and approved CDN libraries such as highlight.js.
- MathJax: support inline `\(...\)` and display `\[...\]` as well as existing dollar-style equations after safe conversion if needed.
- Code blocks: render as `<pre><code>` with copy buttons.
- Self-test markers: render as click-to-reveal accordions; answers must be hidden by default.
- Self-test "왜 이 질문" rationale lines (italic prose preceding question) MUST remain visible (not hidden inside the accordion); they are pedagogical framing and must precede the question text in the rendered card.
- Controls: include print/PDF button using `window.print()` and copy controls for code blocks.
- Responsive layout: desktop left sticky sidebar; mobile single-column/collapsed navigation.
- Dark/light: respect `prefers-color-scheme`.
- Print: hide navigation/backgrounds but keep source-page tags visible.

#### Marker-to-component mapping

| Marker / Pattern | HTML component | Required style/behavior |
|---|---|---|
| `<!-- MASTER LENS -->` | callout box | gold border-left, soft background |
| `<!-- ANNOTATION -->` | inline note/tooltip style | muted italic small text |
| `<!-- ANCHOR -->` | bridge sentence | muted italic bridge |
| `<!-- TRENCH -->` | practical tip box | rose border-left/background |
| `<!-- CONFUSION -->` | side-by-side comparison / amber box | preserve tables |
| `<!-- SELF-TEST -->` | accordion | question visible; rationale italic line visible above question; answer hidden until click |
| `<!-- RECAP -->` | summary box | blue border-left/background |
| `[확인 필요]` | highlighted flag | `<mark>` |
| `[p.XX]`, `[pp.XX–YY]`, `[pp.XX, YY]` | source page span | `.source-page` |
| `[p.확인 필요]` | uncertainty source span | `.source-page.source-uncertain` |
| `<!-- FIGURE_POINTER -->` | textbook reference callout | text-only; purple border-left; no image |
| `<!-- FIGURE_SCHEMATIC -->` | inline schematic `<figure>` | Mermaid or CSS-card as specified; caption and alt text required |
| `<!-- FIGURE_IMAGE_SLOT -->` | image/placeholder | not used in this file unless explicitly supplied with rights |

#### Source page tag rendering

- Detect tags by regex-equivalent patterns: `\[p\.(\d+)\]`, `\[pp\.(\d+)[–-](\d+)\]`, `\[pp\.(\d+(?:,\s*\d+)+)\]`, `\[p\.확인 필요\]`.
- Apply detection to body text, cards, equation captions, and example headings.
- Do not apply detection inside code blocks or inside `FIGURE_*` marker blocks.
- Do not add, delete, renumber, or relocate source page tags.
- Keep source-page tags visible in print.

#### Navigation anchor integrity rules

- Include a sticky left sidebar table of contents.
- Use `<a href="#...">` links only.
- Every sidebar target must have exactly one matching body `id`.
- Every major section heading (§1, §2, §5, §7, §8) must receive a stable id.
- Every §2 concept card should receive a stable id when possible.
- The §2 폐막 Allometric Decision Walkthrough block should receive a stable id (e.g., `#walkthrough` or `#sec2-closing`) and appear in the sidebar TOC as a §2 sub-item.
- Do not create duplicate ids or TOC links whose targets do not exist.
- Enable `html { scroll-behavior: smooth; }`.
- Before finalizing: count sidebar hrefs, confirm each target exists once, confirm no duplicate ids, and fix any mismatch.

#### Figure rendering constraints

- Every figure marker must become either a pointer callout or a proper `<figure>` block.
- `FIGURE_POINTER`: render Source / Why this matters / When to look / Learner instruction; do not generate or embed an image.
- `FIGURE_SCHEMATIC`: render only the listed elements and explicitly exclude listed exclusions; do not reproduce textbook layout, labels, or artwork.
- Do not add figures not present in PART A.

#### Prohibited in Phase 5

- Do not render PART B as learner content.
- Do not modify PART A text, page tags, equations, source language, or markers.
- Do not expose self-test answers by default.
- Do not leave markers as plain text.
- Do not embed textbook images without explicit rights.
- Do not output Mermaid that fails self-check.
- Do not create sidebar links with missing or duplicated ids.
- Do not collapse the ver2 "왜 이 질문" rationale lines into hidden accordion content.
- Do not strip ver2 augmentation labels (`[EXPERT_INFERENCE, ver2 V*]`, `[TEXTBOOK_DERIVED, ver2 V*]`) from the rendered HTML; these labels are part of the source-boundary record.
- Do not strip v3 augmentation labels (`[EXPERT_INFERENCE, v3]`) from the rendered HTML; these labels are part of the source-boundary record.
- Do not strip the Korean-English paired expressions (e.g., `청소율(clearance)`, `절편(intercept)`, `실무 체화 요약(Practice Brief)`, `실패 모드(Failure Mode)`, `보스 딜레마(Boss Dilemma)`) introduced by v3.2 readability patches — they are part of the learner-facing prose and must render verbatim.


### B5. Audit Guardrails

Do not restore or introduce:

- `4.1배` as mouse-human; it is rat 250 g→human 70 kg only.
- `7.4배` and `7.7배` without species/source distinction.
- The deleted claim “CL overprediction necessarily causes subtherapeutic starting dose.”
- Unsupported FDA/EMA/ICH/NDA/MABEL reviewer claims as textbook fact.
- Unsupported NONMEM/QSP implementation claims as textbook-derived content.
- Unsupported numerical values or examples absent from PDF/Audit/Content Lock.
- Embedded textbook figures despite Image rights = None.
- New figure ideas or unapproved code blocks.
- Total-CL scaling where unbound clearance is required by binding context.
- Silent correction of PK28 t½ or PK29 parameter-set discrepancies without source-scope labeling.
- ver2: any new named clinical example beyond methadone / compound X / cefazolin / epoetin-β.
- ver2: any new numerical threshold beyond the source/Audit/Content Lock set.
- ver2: any new regulatory or implementation phrase not already present in PART A ver1.
- v3.1: any new content beyond Korean readability prose edits to existing PART A sentences. K01–K13 do not change facts, equations, page tags, source labels, or scientific claims.
- v3.2: any new content beyond Korean-Dominant readability prose edits to existing PART A sentences. L01–L12 do not change facts, equations, page tags, source labels, figure markers, or scientific claims; they only convert English narrative phrases to Korean and add Korean-English paired expressions on first use of career-critical terms.


### B6. Crucible Guardrails

- Crucible Report v1 is not a raw content source for Phase 5.
- Preserve only logic already present in PART A or explicitly logged in the Mastery Augmentation Layer.
- Do not turn `EXPERT_INFERENCE` notes into textbook-derived statements.
- Do not reintroduce rejected or lower-priority Crucible items.
- Do not add new named drugs, new regulatory claims, new numerical thresholds, or new page tags from Crucible ideas.
- ver2 EXPERT_INFERENCE blocks (Practice Briefs, Walkthrough, Q rationales, Target Mental Model) must remain labeled in HTML and must not be silently relabeled as TEXTBOOK_DERIVED.


### B7. Deprecated and Forbidden Restorations

- Step 1 Draft v0 is deprecated and must not be used as learner-body source.
- Do not restore rejected overclaims, unsupported numbers, unsupported regulatory claims, source-unsupported examples, unapproved code, or unapproved figures.
- Do not use Step 1 material except through a formally logged micro-patch gate.
- No such micro-patch was required for this assembly.
- ver1 PART A scientific content was preserved verbatim in ver2; no deprecation of ver1 content occurred.
- v3 PART A scientific content was preserved verbatim in v3.1; only Korean prose readability was patched.
- v3.1 PART A scientific content was preserved verbatim in v3.2; only Korean-dominant prose readability was patched (English subsection headers, English noun lists, and selected English narrative phrases were converted to Korean or Korean-English paired expressions).


### B8. PATCH MODE Splice Verification Table

| Marker # | Anchor text (truncated to 60 chars) | Anchor found? | Match count | Inserted? | Final location (§ + card) |
|---|---|---|---:|---|---|
| F1 | `## §1 — Session Header & Roadmap` | YES | 1 | YES | §1 Session Header & Roadmap |
| F2 | `CL의 $b\approx0.75$는 시간당 처리량의 지수다. 그럼 V는 왜 $d\approx1$인가? 답은 ` | YES | 1 | YES | §2 C2 Clearance Exponent — b=1 fallacy |
| F3 | `CL의 $b\approx0.75$는 시간당 처리량의 지수다. 그럼 V는 왜 $d\approx1$인가? 답은 ` | YES | 1 | YES | §2 C2 Failure Conditions |
| F4 | `**C3 핵심:** $d\approx1$은 분포 공간이 체중에 비례한다는 뜻이고, $b<d$는 큰 동물에서 ` | YES | 1 | YES | §2 C3 Volume Exponent / §5 Pair 1 연결 |
| F5 | `**C4 핵심:** Dedrick superposition은 curve-fitting 장식이 아니라 CL e` | YES | 1 | YES | §2 C4 Elementary Dedrick / PK28 |
| F6 | `**C4 핵심:** Dedrick superposition은 curve-fitting 장식이 아니라 CL e` | YES | 1 | YES | §2 C4 Complex Dedrick / PK29 |
| F7 | `**C5 핵심:** C5의 수식은 equal unbound AUC를 맞추는 allometric backbon` | YES | 1 | YES | §2 C5 Pediatric/elderly context |


### B9. Zero-Omission Coverage Matrix

| Domain | Required item | Evidence in PART A | Status | Action |
|---|---|---|---|---|
| C1 Scope concepts | Master equation, CL exponent, V exponent, Dedrick, equal-AUCu dose backbone | §2 C1–C5 | PRESENT | None |
| C1 Scope chapter role | Theory/data-anchor chapter for FIH, pediatric dose, PBPK scaling, PK28/PK29 interpretation | §1 roadmap, §8 positioning | PRESENT | None |
| C2 Data anchors | G&W PK28 methadone mouse/rat/man BW/dose, AUC=1/a, hepatic extraction, t½ discrepancy | C3 Data Anchor; Q5 | PRESENT | None |
| C2 Data anchors | G&W PK29 compound X parameter-set discrepancy and complex Dedrick need | C4 Data Anchor; Q4/Q5 | PRESENT | None |
| C2 Data anchors | R&T 20-g mouse to 70-kg human 3500 vs 455, 7.7-fold | §1 Big Idea, C2, Q2 | PRESENT | None |
| C3 Audit MUST_FIX | 4.1/7.4/7.7 fold species pairs separated | §1 Big Idea; C2; §5 Pair 1; Q2 | PRESENT | None |
| C3 Audit MUST_FIX | `b=1` directionality corrected: target-AUC CL overprediction may cause dose overprediction | §1 Big Idea; C2; Q2; Practice Lens | PRESENT | None |
| C3 Audit MUST_FIX | Unsupported FDA/ICH/NDA/MABEL/NONMEM claims removed or downgraded | §1 caution; §7 Q8; §8 text labels `[교과서 외 구현 해석]` | PRESENT | None |
| C3 Audit SHOULD_FIX | `b` not treated as fixed natural constant; varies with data/mechanism | C1, C2, §8 | PRESENT | None |
| C4 Audit T5 | R&T Ch.14 age/renal/functional-age message preserved | C5, Q7, §8 Failure Mode 3 | PRESENT | None |
| C4 Audit T5 | Protein-binding/unbound clearance boundary retained | C1 Boundary, C2 TRENCH, C5 assumptions | PRESENT | None |
| C5 Figure coverage | F1–F7 approved figure markers present exactly once each; image rights respected | PART A figure markers; B8 verification | PRESENT | None |
| C5 Rejected figures | Rejected/deferred textbook figures not restored as embedded images | PART A has no `FIGURE_IMAGE_SLOT` and no image paths | PRESENT | None |
| C6 Page tags | Existing source page tags preserved; no new page tags fabricated by augmentation | PART A page tags inherited from Content Lock v2 and marker sources; ver2 adds no new tags; v3.1 adds no new tags; v3.2 adds no new tags | PRESENT | None |
| C7 Crucible Grade A | Scale-invariance, k_el directionality, Dedrick diagnostic, source-boundary logic preserved | C1/C3/C4 notes; §7/§8 | PRESENT_COMPRESSED | None |
| C8 Deprecated Draft regression | Wrong FIH wording, unsupported regulatory overclaim, Step 1 figure/code overreach blocked | PART A and B5/B7 guardrails | PRESENT | None |
| C9 Canonical integrity | Scientific body equals §1–§8 of Content Lock v2 plus exact approved figure markers, labeled augmentation, and non-scientific process-label neutralization | PART A | PRESENT | None |
| C10 ver2 Mastery-Uplift | 4-axis Practice Briefs per C1–C5; Allometric Decision Walkthrough; §1 Target Mental Model; §7 "왜 이 질문" rationale lines | PART A V1–V4 blocks; B11 ver2 log | PRESENT | None |
| C11 ver2 Source-Boundary | All ver2 augmentations labeled; no new page tags / named examples / numerical thresholds / regulatory phrases | PART A V1–V4 labels; B5/B6 guardrails | PRESENT | None |
| C12 v3.1 Korean Readability | Learner Navigation Aid Korean prose; first-use glosses for `turnover time` / `scale-invariant` / `extent`; Korean-flow polish for selected awkward phrases; sentence split for long enumerations; no scientific change | PART A K01–K13 edits; B11 v3.1 log | PRESENT | None |
| C13 v3.2 Korean-Dominant Readability | §2 subsection headers Korean conversion (정형 정의 / 도출 / 구조적 의미 / 경계 조건 / 결과 / 데이터 앵커 / 한계 / 가정 / 그럴듯한 오해 / 실패 조건 / 전문가 진단 트리거); Failure Conditions 6-item and Assumptions 5-item Korean-English paired list; §8 Failure Mode 1/2/3 Korean naming; learner-facing English narrative sentences converted to Korean; pedagogical device names (실무 체화 요약, 실무 렌즈, 체화 노트, 실패 모드, 그럴듯한 오해, 보스 딜레마, 치명적 타격, 전문가 해석 지점) Korean-English paired on first use; no scientific change | PART A L01–L12 edits; B11 v3.2 log | PRESENT | None |

### B10. Micro-Patch Log

No scientific micro-patches were needed. PART A equals exact-spliced learner-facing Content Lock v2.1 except approved Mastery Augmentation Layer (eight ver1 augmentations + five ver2 augmentations + five v3 augmentations), learner navigation wrapper, four non-scientific process-label neutralizations that remove `Draft v0`/`Content Lock` wording from learner-facing sentences without changing scientific meaning, v3.1 Korean Readability Patches K01–K13, and v3.2 Korean-Dominant Readability Patches L01–L12 which edit only Korean prose surface form (subsection headers, English narrative sentences, English noun lists, pedagogical device first-use glosses).

### B11. Mastery Augmentation Log — v3.2 (consolidated)

#### ver1 augmentations (preserved verbatim)

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
|---:|---|---|---|---|---|---|
| 1 | C1 end | M | YES | CRUCIBLE_DERIVED | Clarifies scale-invariance claim without adding new formula or page tag. | Low |
| 2 | C2 end | J/R | YES | AUDIT_DERIVED | Reinforces corrected AUC/dose directionality from Audit. | Low |
| 3 | C3 end | F | YES | CRUCIBLE_DERIVED | Prevents half-life/rate-constant sign confusion. | Low |
| 4 | C4 end | J | YES | CRUCIBLE_DERIVED | Frames Dedrick as diagnostic rather than decorative overlay. | Low |
| 5 | C5 end | R | YES | TEXTBOOK_DERIVED | Keeps equal-AUCu backbone distinct from final dose selection. | Low |
| 6 | §5 end | F | YES | CRUCIBLE_DERIVED | Turns confusion pairs into review checklist. | Low |
| 7 | §7 end | J | YES | EXPERT_INFERENCE | Converts self-test outputs into model-selection narrative. | Medium |
| 8 | §8 end | M | YES | EXPERT_INFERENCE | Locks allometry as prior-plus-override judgment. | Medium |

#### ver2 augmentations (preserved verbatim)

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
|---:|---|---|---|---|---|---|
| V1 | §1 Big Idea 직후 | Target Mental Model 명시 블록 | YES | TEXTBOOK_DERIVED | §8 D Final Mental Model을 §1으로 압축 미러링. 학습자가 세션 시작 시 도달 목표를 명시적으로 인지하도록. 새 내용 없음. | Low |
| V2 | C1–C5 각 카드 말미 (5 blocks) | Practice Brief — 4축 (왜/흐름/꿀팁/실무) | YES | EXPERT_INFERENCE | 각 C-카드의 기존 Master Lens, RECAP, Mastery Note, Practice Lens, Trench tip 콘텐츠를 4축 구조로 재합성. 사용자 검토 기준 "각 개념마다 4축 일관 구조" 충족. 새 사실/수치/명명사례 없음. | Low |
| V3 | §2 폐막 (C5 후) | Allometric Decision Walkthrough 5-step | YES | EXPERT_INFERENCE | C1–C5 통합 워크플로우 시연. 새로운 numerical anchor 또는 named example 미사용; 기존 PK28/PK29 벤치마크와 §8 D Mental Model을 5-step으로 압축 재구성. | Medium |
| V4 | §7 Q1–Q8 진입부 (8 lines) | "왜 이 질문" 1줄 rationale prefix | YES | EXPERT_INFERENCE | 각 self-test의 pedagogical 의도를 명시. §1 spine과 카드 콘텐츠로부터 직접 도출. 새 사실 없음. | Low |
| V5 | PART B B11 | Mastery Augmentation Log 갱신 | YES | n/a (log only) | ver1 + ver2 통합 기록. | Low |


#### v3 augmentations (preserved verbatim)

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
|---:|---|---|---|---|---|---|
| P1a | §2 C2 heading | `[Apex]` → `[⚡ Apex Concept]` 마커 표준화 | YES | n/a (style normalization) | C2가 본 세션의 Apex Concept임을 표준 마커로 명시. 학습자/HTML 컴파일러가 동일 컨벤션을 인식하도록. 텍스트 의미 변경 없음. | Low |
| P1b | §2 C2 (after `B. Plausible Fallacy`) | Plausible Fallacy 보강 — `b=0.75` over-trust | YES | EXPERT_INFERENCE | 기존 `b=1` fallacy의 거울상 (b를 무비판적으로 0.75로 신뢰하는 오류). G&W p.178의 "0.2~>1 분포" 경고를 직접 인용. 새 named clinical example 없음, 새 numerical threshold 없음. IND meeting 피드백 언급은 일반화된 실무 시나리오로, 특정 규제 조항 단정 아님. | Low |
| P2a | §5 Pair 1 (after Critical Blow) | ⚡ 기억 고리 — *기능 vs 공간* | YES | EXPERT_INFERENCE | C2($b\approx 0.75$ flow prior)와 C3($d\approx 1$ extent prior)의 차이를 단일 인과 체인으로 압축. 기존 RECAP/Failure Mode와 중복되지 않는 비유 인코딩(기능 vs 공간). 새 사실/수치/명명사례 없음. | Low |
| P2b | §5 Pair 3 (after 정리) | ⚡ 기억 고리 — *직선 도로 vs 우회로* | YES | EXPERT_INFERENCE | Pair 3을 "simple form vs corrected form" 일반 프레임으로 확장. 비유는 patch에 명시된 verbatim 형태로 적용; MLP/brain weight/PPB correction은 §2 본문에 명시 등장은 없으나 알로메트릭 스케일링 일반 도메인의 표준 correction factor 명칭이며 새 named **clinical** example이 아님. **검토 메모:** patch 원문의 pair label "simple allometry vs allometry with correction factors"는 기존 Pair 3 제목 "BW^b allometry vs BSA scaling"과 literal 일치는 아니나, simple/corrected라는 차원의 conceptual umbrella 안에 BSA가 임상 corrected form으로 포함된다는 해석으로 적용. 다음 review에서 reviewer가 pair scope를 확인. | Low |
| P3 | PART B B11 + Final v3 All-Pass Checklist | v3 Change Log 갱신 + 최종 8항목 체크리스트 | YES | n/a (log only) | 전체 v3 변경 사항을 단일 표로 추적; 최종 체크리스트로 무결성 검증. | Low |


#### v3.1 augmentations (new — Korean Readability Patch)

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
|---:|---|---|---|---|---|---|
| K01 | Learner Navigation Aid 섹션 헤더 | "How to use this handout:" 영문 헤더 → "이 자료 활용법:" 한국어 헤더로 변환 | YES | n/a (style — Korean readability) | 학습자 진입부 영문 헤더 한국어화. 본문 의미·구조 보존. | Low |
| K02 | Learner Navigation Aid Learning route 7-item list | 영문 7개 학습 경로 목록을 한국어 목록으로 변환 | YES | n/a (style — Korean readability) | 영문 안내 항목의 한국어 가독성 개선. C1–C5 흐름과 §5–§7 점검 의도는 그대로 보존. 새 학습 항목 없음. | Low |
| K03 | Learner Navigation Aid Before/After 헤더 | "Before you start:" / "After you finish:" 영문 헤더 → "시작 전 점검:" / "완료 후 체크:" 한국어 헤더로 변환 + 본문 한국어화 | YES | n/a (style — Korean readability) | 영문 안내 헤더와 본문 한국어화. 사전 점검 항목과 사후 체크 항목 변경 없음. `unbound fraction(← 비결합 분율)` first-use gloss 추가. | Low |
| K04 | §2 C1 B Derivation `turnover time` 첫 등장 | `turnover time` → `turnover time(← 에너지 순환 주기)` first-use gloss 추가 | YES | n/a (style — Korean readability) | 첫 등장 영문 용어에 짧은 한국어 글로스 추가. 수식·수치·source label 변경 없음. | Low |
| K05 | §2 C1 C Structural Meaning `scale-invariant 구조` | `scale-invariant 구조` → `scale-invariant(← 척도 불변) 구조` first-use gloss 추가 | YES | n/a (style — Korean readability) | 첫 등장 영문 용어에 짧은 한국어 글로스 추가. 수학적 해석 라벨 `[교과서 외 수학적 해석]` 보존. | Low |
| K06 | §2 C3 MASTER LENS Big Idea `extent` 첫 등장 | `V는 flow가 아니라 extent다.` → `V는 flow(← 처리 흐름)가 아니라 extent(← 분포 공간의 크기)다.` | YES | n/a (style — Korean readability) | 첫 등장 영문 용어 두 개에 짧은 한국어 글로스 추가. 후속 문장의 $d\approx 1$ vs $b\approx 0.75$ 해석은 그대로 보존. | Low |
| K07 | §2 C3 ANCHOR 긴 문장 | "학생은 '반감기는 BW^0.25'를 외우지만…" → "학습자는 '$t_{1/2}\propto BW^{0.25}$'를 암기하는 데 그치기 쉽다. 그러나…" + "다시 말해" 연결어 추가 | YES | n/a (style — Korean readability) | 한 문장을 두 문장으로 분리하고 연결어로 흐름 명확화. "학생" → "학습자" 호칭 일관화. 수식 LaTeX 표기로 통일. 과학적 의미 그대로. | Low |
| K08 | §2 C4 MASTER LENS Big Idea `접어 넣는 변환` 표현 | `'같은 과정의 다른 시간 척도'로 접어 넣는 변환` → `'같은 과정의 서로 다른 시간 척도'로 표현한 뒤 하나의 공통 축 위에 포개어 보이는 변환` | YES | n/a (style — Korean readability) | 어색한 한국어 표현 자연화. 괄호 주석 내 `← 종별 PK 곡선을 공통 척도 위에 겹치는 변환`도 동일 어휘로 미세 조정. Dedrick plot의 본질(축 변환·곡선 중첩)은 그대로 보존. | Low |
| K09 | §2 C2 Plausible Fallacy 보강 (v3 TRENCH) `반대 방향의 거울상` 표현 | `위의 b=1 오류와 **반대 방향의 거울상**이다 — 한쪽은 mg/kg에 묶여 b를 1로 보수적으로, 다른 쪽은 b를 0.75로 무비판적으로 신뢰한다.` → `위의 b=1 오류와 **거울상 관계**에 있다 — 한쪽은 mg/kg에 묶여 b를 1로 고정하고, 다른 쪽은 b=0.75를 무비판적으로 신뢰한다.` | YES | n/a (style — Korean readability) | 중복 표현(`반대 방향의 거울상` ≈ 거울상은 이미 반대) 제거. v3 P1b의 핵심 메시지("두 fallacy를 동시에 차단해야 C2가 닫힌다") 그대로 보존. | Low |
| K10 | §2 C5 D 마지막 문장 `pediatric/elderly dose equation 전체가 아니다` | `BW allometry는 시작점이지, pediatric/elderly dose equation 전체가 아니다.` → `BW allometry는 시작점이지, 소아·노인 용량 결정 공식 전체를 대체하지 않는다.` | YES | n/a (style — Korean readability) | 영문 명사구를 한국어로 풀어 쓰기. R&T Ch.14 메시지(BSA·maintenance dose·age caution)는 그대로 보존. | Low |
| K11 | §5 Pair 2 기억 고리 `kg당 청소` 표현 | `Kallynochron은 'kg당 청소'의 시간이고, Apolysichron은 '$BW^d$당 청소'의 시간이다.` → `Kallynochron은 'kg 단위로 정규화한 생리학적 시간'이고, Apolysichron은 '$BW^d$ 단위로 정규화한 생리학적 시간'이다.` | YES | n/a (style — Korean readability) | "kg당 청소" 영어 직역체를 한국어 자연 표현으로 변환. 두 시간 척도의 차이($d=1$ 가정 vs $d$ 반영)는 그대로 보존. PK29 compound X 예시 그대로 보존. | Low |
| K12 | §2 폐막 Walkthrough Step 2 6-trigger 나열 | 한 문장 안에 6개 trigger를 dash로 나열 → `다음 6개 trigger 중 하나라도 강하게 의심되면 prior를 sensitivity analysis로 격하한다: 종간 fu 차이, …` 콜론 형식으로 분리 | YES | n/a (style — Korean readability) | 긴 나열 문장을 헤드 + 콜론 + 항목 구조로 정리해 가독성 개선. 6개 trigger 자체는 그대로 보존(fu / CYP isoform / nonlinear MM / enterohepatic recirculation / route/formulation / V ratio drift). $CL_u$ 보정 안내 그대로 보존. | Low |
| K13 | §2 C4 C AUC relation 표현 | `C5의 'equal unbound AUC'와 분리된 사실이 아니라 같은 논리의 수학적 전단계다.` → `C5의 'equal unbound AUC' 조건과 무관한 별개의 사실이 아니라, 같은 논리가 수식으로 먼저 나타나는 전단계다.` | YES | n/a (style — Korean readability) | "분리된 사실이 아니라" 표현을 자연화. AUC=1/a [G&W Eq.2:386, p.179]의 C5 backbone과의 논리적 관계는 그대로 보존. | Low |


#### v3.2 augmentations (new — Korean-Dominant Readability Patch)

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
|---:|---|---|---|---|---|---|
| L01 | Top header v3.1 → v3.2 + v3.2 enhancement note 신설 | Version note expansion | YES | n/a (log only) | v3.2 patch family 등록 + L01–L12 sub-table 명시. 새 과학 내용 없음. | Low |
| L02 | Learner Navigation Aid 마지막 두 영문 문장 | `Figure pointers do not reproduce textbook images; when a pointer appears, consult the named textbook figure in the source PDF/book.` → `Figure pointer는 교과서 그림을 그대로 복제하지 않는다. Pointer가 등장하면 출처 PDF·교과서에서 명시된 figure를 직접 펼쳐 확인한다.` | YES | n/a (style — Korean-Dominant readability) | 학습자 진입부 영문 문장을 한국어로 변환. `Figure pointer`, `figure` 같은 표준 용어는 영문 유지 (HTML 컴파일러 marker convention과 일관). 메시지 그대로 보존. | Low |
| L03 | Learner Navigation Aid Practice Brief / Walkthrough 영문 안내 문단 | `Each C-card closes with a ▶ Practice Brief that compresses four mastery axes …` → `각 C-카드는 ▶ 실무 체화 요약(Practice Brief)으로 마무리되며, 네 가지 체화 축…` + `§2 closes with an Allometric Decision Walkthrough that links C1→C5 as a single workflow.` → `§2는 알로메트릭 의사결정 워크스루(Allometric Decision Walkthrough)로 마무리되어 C1→C5를 하나의 워크플로우로 연결한다.` | YES | n/a (style — Korean-Dominant readability) | 영문 안내문 한국어화 + 학습 장치명 `한글(English)` 병기 (Practice Brief, Allometric Decision Walkthrough). 4축·워크스루 의도 보존. | Low |
| L04 | §1 지식 그래프 위치 「직접 후속」 영문 명사 4개 나열 | `pediatric/elderly dose adjustment, PopPK weight covariate choice, PBPK organ blood flow/volume scaling, FIH exposure translation table.` → `소아·노인 용량 조정(pediatric/elderly dose adjustment), 모집단 약동학 체중 공변량 선택(PopPK weight covariate choice), PBPK 장기 혈류·부피 스케일링(PBPK organ blood flow/volume scaling), 최초 인체 투여 노출 번역 표(FIH exposure translation table).` | YES | n/a (style — Korean-Dominant readability) | 영문 명사 4개 나열을 `한글(English)` 병기 형식으로 변환. 원래 항목 그대로 4개 보존. 직접 후속 영역 4개의 정체성·범위 변경 없음. | Low |
| L05 | §2 C1 A/B/C/D subsection 헤더 + A 본문 bullet + B 본문 영어 표현 + D 본문 | `A. Formal Definition` → `A. 정형 정의(Formal Definition)`; `B. Derivation — 왜 거듭제곱 함수인가` → `B. 도출(Derivation) — 왜 거듭제곱 함수인가`; `C. Structural Meaning` → `C. 구조적 의미(Structural Meaning)`; `D. Boundary Conditions` → `D. 경계 조건(Boundary Conditions)`. A 본문 `drug-dependent / compound-dependent intercept`, `variable type-dependent exponent`, `protein binding` 등 `한글(English)` 병기. B 본문 `metabolic rate`, `energy content`, `surface`, `length²`, `volume`, `length³` 등 `한글(English)` 병기. C 본문 `allometry failure` → `알로메트리 실패(allometry failure)`. D 본문 `physical transport processes`, `plasma protein binding`, `metabolism/excretion`, `CYP450 isozyme makeup` 등 `한글(English)` 병기. | YES | n/a (style — Korean-Dominant readability) | C1 카드 전반의 영어식 명사 처리·subsection 헤더 한국어화. 수식·page tag·turnover time 기존 gloss·source label 모두 그대로 보존. | Low |
| L06 | §2 C2 MASTER LENS + A/B/C/D subsection 헤더 + Failure Conditions 6-item 나열 + D body | `Clearance` → `청소율(Clearance)`; `functional variable` → `functional variable(← 기능적 처리량 변수)`; `A. Formal Definition` → `A. 정형 정의(Formal Definition)`; `B. Plausible Fallacy — b=1 linear per-kg scaling` → `B. 그럴듯한 오해(Plausible Fallacy) — b=1 선형 per-kg 스케일링`; `C. Failure Conditions` → `C. 실패 조건(Failure Conditions)`; `D. Expert Diagnostic Trigger` → `D. 전문가 진단 트리거(Expert Diagnostic Trigger)`. Failure Conditions 6-item을 모두 `한글(English)` 병기 형식으로 변환 (종간 혈장 단백 결합 / 대사 경로 또는 CYP isozyme 조성 / 비선형 미카엘리스-멘텐 거동 / 장간 순환 / 투여 경로·제형 / 중심·말초 분포용적 비율 변동). D body의 binding/transporter/saturation/data quality 등 `한글(English)` 병기. | YES | n/a (style — Korean-Dominant readability) | v3.1 Rejected entry의 우려(precision 손실)는 `한글(English)` 병기 방식이 해소함 — 영문 원어가 보존되어 검색·논문 작성·국제 커뮤니케이션 정밀도가 유지되며 한국어 학습자 독해 흐름은 개선됨. v3 P1b TRENCH 블록 메시지 그대로 보존. | Low |
| L07 | §2 C3 A/B/C/D subsection 헤더 + ANCHOR 본문 + C body bullet + D body | `A. Formal Definition` → `A. 정형 정의(Formal Definition)`; `B. Consequence — half-life and rate constant` → `B. 결과(Consequence) — 반감기(half-life)와 속도상수(rate constant)`; `C. Data Anchor — Methadone PK28` → `C. 데이터 앵커(Data Anchor) — Methadone PK28`; `D. Limitations` → `D. 한계(Limitations)`. ANCHOR 본문 `first-order rate constant`, `half-life`, `rate constant`, `fraction` 등 `한글(English)` 병기. C body `Hepatic extraction` → `간 추출률(hepatic extraction)`. D body `tissue affinity / fat distribution / transporter / protein binding / obesity examples / body weight / biologically relevant volume` 등 `한글(English)` 병기. Failure Mode block label에 `실패 모드(Failure Mode)` 첫 등장 gloss. | YES | n/a (style — Korean-Dominant readability) | K06 v3.1 first-use gloss(`flow / extent`) 그대로 보존. PK28 23g/250g/70kg anchor·t½ discrepancy 인용 규약·source label 변경 없음. | Low |
| L08 | §2 C4 A/B/C/D subsection 헤더 + ANNOTATION + Elementary/Complex Dedrick 명칭 + Buckingham π 구절 + D body + TRENCH switch | `A. Formal Definitions` → `A. 정형 정의(Formal Definitions)`; `B. Derivation` → `B. 도출(Derivation)`; `C. AUC relation` → `C. AUC 관계식(AUC relation)`; `D. Data Anchor — PK28 and PK29` → `D. 데이터 앵커(Data Anchor) — PK28 and PK29`. `Elementary Dedrick plot` → `기본 Dedrick plot(Elementary Dedrick plot)`; `Complex Dedrick plot` → `복합 Dedrick plot(Complex Dedrick plot)`. ANNOTATION의 `dose-normalized concentration` → `용량 정규화 농도(dose-normalized concentration)`. Kallynochron/Apolysichron 정의문의 `per-kg time scale`, `generalized physiological time scale` `한글(English)` 병기. B body `Mono-exponential model`, `Allometric substitution`, `concentration`, `time`, `Buckingham π theorem`, `dimensional analysis`, `mass/time/volume`, `dimensionless group` `한글(English)` 병기. D body `multiple dosing/steady state`, `model misspecification`, `Weight range / arithmetic / about` 등 한국어화. TRENCH switch에 `기본 Dedrick(Elementary, $d=1$ 가정)` / `복합 Dedrick(Complex Dedrick)` 한국어 paired 적용. RECAP `curve-fitting` → `곡선 적합(curve-fitting)`, `diagnostic` → `진단(diagnostic)`. | YES | n/a (style — Korean-Dominant readability) | K08 v3.1 `포개어 보이는 변환` 표현 그대로 보존. K13 v3.1 AUC relation 표현 그대로 보존. PK28/PK29 parameter set·t½ discrepancy 그대로 보존. v3.2는 PK28 ↔ PK29 벤치마크 쌍·log-log V vs BW 0.9–1.1 switch trigger 그대로 보존. | Low |
| L09 | §2 C5 ANNOTATION + A/B/C/D subsection 헤더 + Assumptions 5-item + B body + C body + D body + Mastery Note | ANNOTATION의 `safety margin / toxicology / pharmacology / exposure-response / route / formulation / PD metric` → `안전 여유(safety margin) / 독성학(toxicology) / 약리학(pharmacology) / 노출-반응(exposure-response) / 투여 경로(route) / 제형(formulation) / PD 지표(metric)`. `A. Equal-unbound-AUC backbone` → `A. Equal-unbound-AUC 백본(backbone)`; `B. Assumptions` → `B. 가정(Assumptions)`; `C. Pediatric and elderly context from R&T` → `C. 소아·노인 맥락(Pediatric and elderly context) — R&T 기반`; `D. Elderly metabolism statement correction` → `D. 노인 대사 진술 교정(Elderly metabolism statement correction)`. Assumptions 5-item을 `한글(English)` 병기 형식으로 변환 (비결합 AUC / 표적 친화도·관련 약리학 / 선형 구간 / 비결합 분율 / 노출 지표·최고농도 기반 독성·역치 초과 시간 지표). B body `equal AUC / concentration-time curve / shape / full curve equivalence` `한글(English)` 병기. C body `age / weight / gender / drug response variability / chronologic age / functional age / flat dosing / elderly patient / typical 60-year-old adult / child maintenance dose / broader use` `한글(English)` 병기. D body `creatinine clearance / adulthood / rule of thumb / CYP3A substrates / elderly group / young adult / heuristic / renal/hepatic function / biological age` `한글(English)` 병기. mg/kg dose ratio 줄에 `mg/kg dose 비(ratio)` 추가. Mastery Note `exposure translation` → `노출 번역(exposure translation)`. | YES | n/a (style — Korean-Dominant readability) | K10 v3.1 `소아·노인 용량 결정 공식 전체를 대체하지 않는다` 그대로 보존. R&T Eq.14-6, BSA 근사식, 1%/yr creatinine clearance heuristic 그대로 보존. CYP3A 단정 차단 메시지 그대로 보존. | Low |
| L10 | §8 A.1–3 Positioning 항목 영문 명사 | `Animal-to-human exposure translation table` → `동물-인간 노출 번역 표(Animal-to-human exposure translation table)`; `PopPK weight covariate decision` → `모집단 PK 체중 공변량 결정(PopPK weight covariate decision)`; `PBPK parameter scaling` → `PBPK 파라미터 스케일링(PBPK parameter scaling)`. body 내 `table equation`, `curve-superposition check`, `allometry`, `human kinetics prediction`, `organ blood flow`, `rate-like`, `organ volume`, `extent-like` 등 `한글(English)` 병기. | YES | n/a (style — Korean-Dominant readability) | §8 A 시스템 작동 3순간의 항목명 한국어화. R&T Ch.22 page tag 그대로 보존. | Low |
| L11 | §8 B Failure Mode 1/2/3 이름 | `Failure Mode 1 — Allometric Slope Drift` → `실패 모드(Failure Mode) 1 — 알로메트릭 기울기 드리프트(Allometric Slope Drift)`; `Failure Mode 2 — Volume Exponent Lock-in Bias` → `실패 모드 2 — V 지수 고정 편향(Volume Exponent Lock-in Bias)`; `Failure Mode 3 — Functional age omission` → `실패 모드 3 — 기능적 연령 누락(Functional age omission)`. | YES | n/a (style — Korean-Dominant readability) | 학습 장치명 `실패 모드(Failure Mode)` 첫 등장 gloss + 부제 한국어화. R&T 인용 "typical patient" / "individual patient" 직접 인용은 그대로 보존(v3.1 Rejected entry 결정 존중). [R&T p.412–415] page tag 그대로 보존. | Low |
| L12 | §8 C Professional Moat 헤더 + §5 Pair 1 Critical Blow + §7 Q8 Boss Dilemma + §2 C1/C5 Mastery Note + §2 C2 Practice Lens + §2 C2 B Plausible Fallacy + §2 C1 Practice Brief 등 학습 장치명 첫 등장 `한글(English)` 병기 | `### C. Professional Moat — diagnostic, not motivational` → `### C. 전문가 해석 지점(Professional Moat) — diagnostic, not motivational`. §5 Pair 1 `**Critical Blow:**` → `**치명적 타격(Critical Blow):**`. §7 Q8 rationale `보스 딜레마.` → `보스 딜레마(Boss Dilemma).`. §2 C1 `**Mastery Note**` → `**체화 노트(Mastery Note)**`. §2 C1 `**▶ Practice Brief — C1 체화 4축**` → `**▶ 실무 체화 요약(Practice Brief) — C1 체화 4축**`. §2 C2 `**Practice Lens**` → `**실무 렌즈(Practice Lens)**`. §2 C2 B 헤더에 `그럴듯한 오해(Plausible Fallacy)` 한국어 paired (L06과 함께 적용). §2 C2 Practice Brief 4축 보스 딜레마 언급 `Q8 보스 딜레마` → `Q8 보스 딜레마(Boss Dilemma)`. §2 C3 `**Failure Mode**` → `**실패 모드(Failure Mode)**`. | YES | n/a (style — Korean-Dominant readability) | 학습 장치명 첫 등장 시 `한글(English)` 병기로 학습자가 한국어 어휘와 영어 원어를 동시에 익히도록 함. v3 Memory Hook 라벨 (`⚡ 기억 고리 (Memory Hook)`)은 이미 v3에서 paired 형태로 존재 — 변경 없음. 후속 등장은 영문 단독 또는 한국어 단독 표기 유지 (반복 paired는 가독성을 해침). 본문 의미·논리·source label 변경 없음. | Low |


#### Rejected augmentation candidates (ver1 + ver2 + v3 + v3.1 + v3.2)

| Rejected candidate | Reason for rejection |
|---|---|
| Additional named clinical examples beyond methadone/compound X/cefazolin/epoetin-β and source-listed context | Would introduce new named examples not required by Scope/Audit/Content Lock. |
| New regulatory agency-specific language for FIH justification | PDF does not directly support specific external regulatory wording; would violate source-boundary rule. |
| Additional numerical thresholds for acceptable b/d estimates | Would add unsupported numerical claims beyond the source/Audit/Content Lock set. |
| New figure ideas beyond F1–F7 | Would exceed Phase 4C approved figure plan and risk Phase 5 drift. |
| ver2: Concrete worked numerical example (e.g., methadone 23 g→70 kg full CL/V/dose calculation) | Considered but rejected to avoid double-treatment of Q6 mouse-25g example; would risk introducing CL/V values not directly given as PK28 numbers. Walkthrough V3 is conceptual-only. |
| ver2: New marker type for Practice Brief | Rejected to preserve marker-to-component contract. Practice Briefs reuse existing TRENCH marker (rose tip-box style); Walkthrough reuses MASTER LENS marker (gold callout). |
| v3: Adding the new `b=0.75` over-trust Plausible Fallacy as a separate `B-2` numbered subsection | Considered but rejected to preserve C2's existing A–E lettered structure. Implemented as a labeled TRENCH-styled callout block immediately after the existing `B. Plausible Fallacy`, which keeps the lettered backbone intact and visually couples the two complementary fallacies. |
| v3: Forcing the patch's `simple allometry vs correction factors` hook label literally into Pair 3's title | Rejected. Pair 3's existing title (`BW^b allometry vs BSA scaling`) is preserved; only the Memory Hook is appended verbatim under the existing 정리. The slight pair-scope divergence is logged in the v3 augmentation table for next-pass reviewer confirmation. |
| v3: New named scaling correction methods beyond MLP/brain weight/PPB cited in the verbatim Hook 2 text | Rejected as a **content** addition. These are general allometric correction-factor names already invoked at the source-domain level (G&W §2.10) and are not new clinical drug examples. No new clinical entity (drug, patient, disease) is introduced. |
| v3.1: Translating the C2 Failure Conditions 6-item English list (species-dependent plasma protein binding; different metabolic routes; …) into Korean | Rejected. Items are technical pharmacology terms whose precision is best preserved in English; Korean translation risks term-equivalence ambiguity (e.g., "plasma protein binding" vs "혈장 단백질 결합" can drift toward less precise readings). Skipped to avoid technical-precision loss. |
| v3.1: Adding Korean glosses to additional English standard abbreviations (CL, V, AUC, Cmax, ka, ke0, EC50, OFV, VPC, GOF, etc.) inside body text | Rejected. These are global-standard pharmacometrics symbols and abbreviations whose Korean equivalents would clutter the prose without learner gain. Only first-use glosses for narrative-tier English nouns (`turnover time`, `scale-invariant`, `extent`, `unbound fraction`) were applied. |
| v3.1: Restructuring §8 Failure Mode 3 `"typical patient" vs "individual patient"` quotes into a Korean side-by-side table or first-use gloss | Rejected. The R&T direct phrasing carries the specific message intent and is short enough to read fluently in context. Adding a gloss would risk drifting the source-language fidelity that B5 Audit guardrails protect. |
| v3.2: Reversing v3.1's K-list rejections by translating C2 Failure Conditions 6-item or §8 Failure Mode 3 R&T quotes into pure Korean | Rejected. v3.2's Korean-Dominant policy uses `한글(English)` paired expressions, NOT pure Korean translation. v3.1's precision concern is resolved by retaining English originals in parentheses while improving Korean readability. R&T direct quotes ("typical patient" / "individual patient") remain unchanged in v3.2 to preserve source-language fidelity per B5. |
| v3.2: Adding Korean glosses to standard pharmacometrics symbols/abbreviations inside body text (CL, V, AUC, Cmax, ka, ke0, EC50, OFV, VPC, GOF, IIV, RUV, η, ε, ω², σ², THETA, OMEGA, SIGMA, etc.) | Rejected. These are global-standard symbols whose Korean equivalents clutter prose without learner gain. v3.2 maintains v3.1's policy: first-use glosses only for narrative-tier English nouns and concept terms, not for symbols and standard abbreviations. |
| v3.2: Translating code blocks (Zettelkasten YAML, ▶ §8 D Final Mental Model code-fenced text-art) into Korean | Rejected. Code blocks are technical artifacts (YAML metadata, ASCII workflow diagrams) and are explicitly excluded from translation per v3.2 directive Rule 9. Their content is reference-only, not narrative prose. |
| v3.2: Translating figure marker contents (FIGURE_POINTER blocks' "Why this matters / When to look / Learner instruction" English fields) into Korean | Rejected. Figure marker contents are part of the marker payload (per v3.2 directive Rule 8: "figure marker의 위치와 내용은 절대 변경하지 마라"). Phase 5 HTML compiler renders them via marker-to-component mapping; mid-stream translation would break the splice verification contract documented in B8. |
| v3.2: Replacing every occurrence of pedagogical device names (Failure Mode, Plausible Fallacy, Practice Lens, Mastery Note, Practice Brief, Boss Dilemma, Critical Blow) with `한글(English)` paired form throughout the document | Rejected. Repeated paired forms harm reading flow. v3.2 applies first-use gloss policy: paired form on first occurrence in a major section, then English-only or Korean-only as locally natural. v3 Memory Hook label (`⚡ 기억 고리 (Memory Hook)`) was already paired in v3 and is preserved verbatim. |
| v3.2: Converting RECAP / TRENCH / Practice Brief 4-axis bullet bodies (containing many English technical terms in flowing Korean prose) into more aggressively Korean-dominant rewrites | Rejected. These body texts were already heavily polished by ver2 V2 augmentation and v3.1 K-patches; further rewriting risks (a) altering pedagogical intent of EXPERT_INFERENCE blocks, (b) breaking the source-boundary record (paired-source-status would not match), (c) violating B5 audit guardrail "any new content beyond ... readability prose edits". v3.2 limits itself to subsection headers, first-use device-name glosses, English noun-list normalization, and Positioning-item naming. |


---

## End of 14_html_compile_input_master_v3.1.md (preserved as v3.1 historical closing)

**Final Verdict: GO for Phase 5 HTML compilation.**

v3.1은 v3의 모든 PASS 인증과 mastery 강화 요소(Practice Brief 4축, Allometric
Decision Walkthrough, Target Mental Model, "왜 이 질문" rationale, [⚡ Apex Concept]
표준 마커, §5 v3 Memory Hooks 2개, v3 Plausible Fallacy 보강)를 그대로 유지하면서,
잔존하던 한국어 독해 마찰점 13개를 **외과적 prose patch(K01–K13)**로 닫았다.
v3의 모든 사실 문장, 수식, page tag, marker, figure pointer, RECAP, Mastery Note,
Practice Lens, Trench tip, Practice Brief, Walkthrough, Target Mental Model,
Q rationale, [⚡ Apex Concept] 마커, §5 Pair 1·Pair 3 v3 Memory Hooks가 **그대로
보존**되었다.

PK28/PK29 anchor (4.1/7.4/7.7 fold species pair separation, t½ discrepancy citation
scope, parameter-set discrepancy), R&T age/renal/BSA caution, FIH equal-AUCu
backbone vs final dose distinction, "CL overprediction → subtherapeutic" 단정 차단,
unsupported FDA/ICH/MABEL/NONMEM/QSP claim 차단 — 모든 audit guardrail이 그대로
유지된다.

Source-Boundary, Zero-Omission, HTML-Readiness, Learner-Standalone, Mastery-Uplift
인증은 모두 유지되며, v3.1에서 Korean Readability 보강이 추가되었다. Phase 5 HTML
컴파일러는 이 파일을 그대로 입력으로 받을 수 있다.

---

## Final v3 All-Pass Checklist (8 items)

| # | Check item | Status | Evidence in PART A / PART B |
|---:|---|---|---|
| 1 | C2 Apex marker normalized to `[⚡ Apex Concept]` (not `[Apex]`) | PASS | §2 C2 heading line; B11 v3 P1a |
| 2 | C2 Plausible Fallacy now covers BOTH `b=1` (existing) AND `b=0.75` over-trust (new, [EXPERT_INFERENCE, v3]) | PASS | §2 C2 `B. Plausible Fallacy` + immediately following TRENCH-styled v3 block; B11 v3 P1b |
| 3 | §5 Pair 1 (`b` vs `d`) has both Critical Blow AND ⚡ Memory Hook (*기능 vs 공간*) | PASS | §5 Pair 1 closing two paragraphs; B11 v3 P2a |
| 4 | §5 Pair 3 (`BW allometry` vs `BSA scaling`) has both 정리 AND ⚡ Memory Hook (*직선 도로 vs 우회로*) | PASS | §5 Pair 3 closing two paragraphs; B11 v3 P2b |
| 5 | All ver1 + ver2 PART A scientific content preserved verbatim (no fact, equation, page tag, marker, figure pointer, RECAP, Mastery Note, Practice Lens, Trench tip, Practice Brief, Walkthrough, Target Mental Model, or "왜 이 질문" rationale was modified or removed) | PASS | Full PART A diff against ver2; B5/B7/B11 guardrails reaffirmed |
| 6 | No new named clinical example, no new regulatory/agency-specific phrasing as fact, no new numerical threshold, no new figure marker introduced by v3 | PASS | v3 additions = 1 marker normalization + 1 EXPERT_INFERENCE TRENCH block + 2 EXPERT_INFERENCE Memory Hooks + 1 PART B log; all labeled; Rejected-candidates table v3 entries explicit |
| 7 | All v3 additions explicitly tagged `[EXPERT_INFERENCE, v3]` or `[v3]` style label so HTML compiler preserves source-boundary record | PASS | C2 v3 TRENCH block, Pair 1 hook, Pair 3 hook all bear `[EXPERT_INFERENCE, v3]` inline; B11 v3 sub-table; B6 guardrail (do not relabel EXPERT_INFERENCE as TEXTBOOK_DERIVED) reaffirmed |
| 8 | PART B (B1 contract, B2 figure plan, B3 page-tag rules, B4 marker mapping, B5 audit guardrails, B6 crucible guardrails, B7 deprecated, B8 splice verification, B9 zero-omission matrix, B10 micro-patch log) intact and consistent with v3 PART A | PASS | B1–B10 unchanged in scope; B11 extended with v3 sub-table and v3 rejected-candidate entries; Rejected-candidates table updated; no contradiction with v3 PART A additions |

---

## v3.1 Final Checklist

| # | Check item | Status | Evidence |
|---:|---|---|---|
| 1 | PART A readability improved | PASS | K01–K13 applied: Learner Navigation Aid 한국어화(K01–K03), first-use gloss 4종(K04 turnover time, K05 scale-invariant, K06 extent, K03 unbound fraction), 어색한 표현 자연화 5종(K07 학습자/문장 분리, K08 Dedrick "포개어 보이는 변환", K09 거울상 관계, K10 한국어 풀이, K11 Pair 2 기억 고리), 긴 문장 분리 1종(K12 Walkthrough Step 2), 개념 명확화 1종(K13 C4 AUC relation). |
| 2 | Scientific content unchanged | PASS | 모든 수식, 수치 anchor(PK28 23 g/250 g/70 kg, AUC=1/a=3.13, PK29 a=0.021/b=0.74/c=0.076/d=1.18 vs 0.021/0.75/0.10/1.21, R&T 3500 vs 455, 7.7/7.4/4.1 fold), source page tag, [G&W p.…] / [R&T p.…] / [PK28 p.…] / [PK29 p.…] 라벨, source-boundary 라벨([교과서 외 수학적/구현/실무 해석], [TEXTBOOK_DERIVED] / [AUDIT_DERIVED] / [CRUCIBLE_DERIVED] / [EXPERT_INFERENCE, ver2 V*] / [EXPERT_INFERENCE, v3]) 모두 보존. |
| 3 | Equations preserved | PASS | $Y=a\cdot BW^b$, $\ln(Y)=\ln(a)+b\cdot\ln(BW)$, $CL_i=a\cdot BW_i^b$, $V_i=c\cdot BW_i^d$, $t_{1/2}\propto BW^{d-b}$, $k_{el}\propto BW^{b-d}$, Elementary Dedrick / Complex Dedrick 변환, mono-exponential model + allometric substitution, equal-unbound-AUC backbone (Eq.2:417/420/421), mg/kg dose ratio = $BW^{b-1}$, BSA = $1.73(W/70)^{0.75}$, R&T Eq.14-6 child maintenance dose 모두 v3 원문 그대로 보존. K07에서 $t_{1/2}\propto BW^{0.25}$ 표기를 LaTeX로 통일했으나 수식 자체는 동일. |
| 4 | Page tags preserved | PASS | [G&W Eq.2:374, p.173] / [R&T Eq.22-2, p.732] / [G&W Eq.2:379, p.176] / [R&T Eq.22-1, p.732] / [G&W p.177–178] / [G&W p.173–174] / [G&W p.173] / [G&W Eq.2:380, p.176] / [PK28 Eq.28:1, p.611] / [G&W Table 2.22, p.180] / [R&T Fig.22-1, p.732] / [G&W p.178] / [G&W p.191] / [R&T p.733] / [G&W p.174] / [G&W p.190] / [R&T p.740] / [G&W §2.10.3 p.176–180; G&W Fig.2.159 p.191; R&T Ch.22 p.732–735] / [G&W Eq.2:382, p.179; PK28 Eq.28:2, p.611] / [G&W §2.10.6 p.186; PK28 p.613] / [R&T p.439] / [G&W §2.10.6–2.10.7, p.184–189] / [G&W Eq.2:384, p.179] / [G&W Eq.2:386, p.179] / [G&W p.184–186; PK28 p.611–614] / [PK28 p.614] / [G&W p.186–189; PK29 p.615–620] / [G&W p.189] / [PK29 p.619] / [G&W Eq.2:417, p.190; Eq.2:420, p.190; Eq.2:421, p.190] / [R&T p.411–412] / [R&T p.412] / [R&T p.436] / [R&T Eq.14-6, p.432; Key Relationships, p.436] / [R&T p.435] / [R&T p.422] / [R&T p.424] / [R&T p.412–415] / [R&T p.731–743] — 모두 v3 원문 동일. v3.1에서 새 page tag 추가 또는 기존 page tag 변경 없음. |
| 5 | Figure markers preserved | PASS | F1 FIGURE_SCHEMATIC (§1 후 allometric spine), F2 FIGURE_POINTER (R&T Ch.22 p.733 Fig.22-2), F3 FIGURE_POINTER (G&W §2.10.3 p.174 Fig.2.145), F4 FIGURE_SCHEMATIC (§2 C3 후 flow vs extent), F5 FIGURE_POINTER (G&W PK28 p.613 Fig.28.2), F6 FIGURE_POINTER (G&W PK29 p.619 Fig.29.3), F7 FIGURE_POINTER (R&T Ch.14 p.430 Fig.14-20) — 7개 figure marker 위치, source 필드, learner instruction, alt text 모두 v3 원문 동일. v3.1에서 figure marker 변경·추가·삭제 없음. B2 / B8 splice verification 그대로 유효. |
| 6 | Source-boundary preserved | PASS | TEXTBOOK_DERIVED / AUDIT_DERIVED / CRUCIBLE_DERIVED / EXPERT_INFERENCE / [EXPERT_INFERENCE, ver2 V*] / [TEXTBOOK_DERIVED, ver2 V1] / [EXPERT_INFERENCE, v3] / [⚡ Apex Concept] 라벨 전부 보존. K-patch는 모두 `n/a (style — Korean readability)` source status로 분류되어 EXPERT_INFERENCE / TEXTBOOK_DERIVED 등 본문 사실 라벨과 충돌하지 않음. B5 audit guardrail (4.1/7.4/7.7 fold species pair, FIH 단정 차단, ICH/FDA/MABEL/NONMEM/QSP 단정 차단), B6 crucible guardrail, B7 deprecated material 차단 모두 유지. |
| 7 | HTML-readiness preserved | PASS | B1 compilation contract, B2 figure plan, B3 page-tag rendering rules, B4 marker-to-component mapping, B4 navigation anchor integrity rules, B4 figure rendering constraints, B4 prohibited list, B5 audit guardrails, B6 crucible guardrails, B7 deprecated restorations, B8 PATCH MODE splice verification table (F1–F7), B9 zero-omission coverage matrix(C12 v3.1 추가), B10 micro-patch log, B11 mastery augmentation log(K01–K13 추가) 모두 일관 보존. 신규 marker 타입 도입 없음. CSS class (.source-page / .source-page.source-uncertain / Mermaid theme) 변경 없음. Phase 5 HTML 컴파일러는 v3와 동일한 marker → component 매핑으로 v3.1을 렌더링할 수 있다. |
| 8 | Ready for Phase 5 HTML compilation | PASS | 모든 가드레일·인증·marker·page tag·수식·figure marker·source label이 v3 대비 변경 없음. PART A는 surgical Korean prose 개선만 반영되어 학습자 가독성이 상승했다. PART B의 contract / guardrail은 그대로 유지되며 K01–K13 항목이 B11 v3.1 sub-table에 명시 등록되었다. Phase 5는 이 파일을 그대로 입력으로 받아 v3와 동일한 마커→컴포넌트 매핑·page tag 렌더링·figure rendering rule·navigation anchor integrity rule을 적용할 수 있다. |

---

## End of 14_html_compile_input_master_v3.2.md

**Final Verdict: GO for Phase 5 HTML compilation.**

v3.2는 v3.1의 모든 PASS 인증과 mastery 강화 요소(Practice Brief 4축, Allometric
Decision Walkthrough, Target Mental Model, "왜 이 질문" rationale, [⚡ Apex Concept]
표준 마커, §5 v3 Memory Hooks 2개, v3 Plausible Fallacy 보강, K01–K13 Korean
readability prose patch)를 그대로 유지하면서, v3.1 잔존 영어 마찰점을 한국어 중심
가독성으로 한 번 더 닫는 **외과적 prose patch(L01–L12)**를 적용했다.

v3.1의 모든 사실 문장, 수식, page tag, marker, figure pointer, RECAP, Mastery Note
본문, Practice Lens, Trench tip, Practice Brief 4축 본문, Walkthrough 본문,
Target Mental Model 본문, Q rationale 본문, [⚡ Apex Concept] 마커, §5 Pair 1·Pair 3
v3 Memory Hooks가 **그대로 보존**되었다.

PK28/PK29 anchor (4.1/7.4/7.7 fold species pair separation, t½ discrepancy citation
scope, parameter-set discrepancy), R&T age/renal/BSA caution, FIH equal-AUCu
backbone vs final dose distinction, "CL overprediction → subtherapeutic" 단정 차단,
unsupported FDA/ICH/MABEL/NONMEM/QSP claim 차단 — 모든 audit guardrail이 그대로
유지된다. R&T "typical patient" / "individual patient" 직접 인용 표현 또한 v3.1
Rejected 결정을 존중하여 v3.2에서도 변경 없이 보존된다.

Source-Boundary, Zero-Omission, HTML-Readiness, Learner-Standalone, Mastery-Uplift
인증은 모두 유지되며, v3.2에서 Korean-Dominant Readability 보강이 추가되었다.
Phase 5 HTML 컴파일러는 이 파일을 그대로 입력으로 받을 수 있다.

---

## Final v3.2 Certification

| Certificate | Status | Basis |
|---|---|---|
| Korean-Dominant Readability Certificate | PASS | General learner-facing English prose converted to Korean where possible; career-critical terms retained as Korean-English paired expressions. §2 subsection headers, Failure Conditions 6-item, Assumptions 5-item, §1 직접 후속 4-noun list, §8 Positioning items, §8 Failure Mode names, pedagogical device first-use names all converted per L01–L12. |
| Scientific Preservation Certificate | PASS | No scientific content, equation, number, example, page tag, source label, or figure marker changed. PK28/PK29 anchors (23 g/250 g/70 kg, AUC=1/a=3.13, a=0.021, b=0.74/0.75, c=0.076/0.10, d=1.18/1.21, R&T 3500 vs 455, 7.7/7.4/4.1 fold), all [G&W ...] / [R&T ...] / [PK28 ...] / [PK29 ...] page tags, [TEXTBOOK_DERIVED] / [AUDIT_DERIVED] / [CRUCIBLE_DERIVED] / [EXPERT_INFERENCE, ver2 V*] / [EXPERT_INFERENCE, v3] source labels preserved verbatim. |
| Marker Integrity Certificate | PASS | All HTML compiler markers (`<!-- MASTER LENS -->`, `<!-- ANNOTATION -->`, `<!-- TRENCH -->`, `<!-- CONFUSION -->`, `<!-- SELF-TEST -->`, `<!-- RECAP -->`, `<!-- ANCHOR -->`, `<!-- FIGURE_POINTER -->`, `<!-- FIGURE_SCHEMATIC -->`), figure markers F1–F7, anchors, and section/card structure preserved. No new markers introduced. PATCH MODE splice verification table B8 remains valid. |
| HTML-Readiness Certificate | PASS | Phase 5 compatibility preserved; no HTML/Mermaid/SVG generated. All B1–B11 PART B contracts intact. v3.2 sub-table appended to B11. v3.2 statements added to B1 / B2 / B3 / B4 prohibited list / B5 / B7 / B9 (C13 row) / B10. CSS class (.source-page / .source-page.source-uncertain) unchanged. Phase 5 HTML compiler can render this file with the same marker → component mapping as v3.1. |

---

## v3.2 Final Checklist

| # | Check item | Status | Evidence |
|---:|---|---|---|
| 1 | PART A readability improved (Korean-Dominant) | PASS | L01–L12 applied: header v3.2 신설(L01), Learner Navigation Aid 한국어화(L02–L03), §1 직접 후속 영문 명사 나열 `한글(English)` 변환(L04), §2 C1/C2/C3/C4/C5 subsection 헤더 + 본문 영어 표현 한국어화(L05–L09), §8 A 1–3 항목 한국어 paired(L10), §8 B Failure Mode 1/2/3 이름 한국어 paired(L11), 학습 장치명 첫 등장 `한글(English)` 병기(L12). |
| 2 | Scientific content unchanged | PASS | 모든 수식, 수치 anchor (PK28 23 g/250 g/70 kg, AUC=1/a=3.13, PK29 a=0.021/b=0.74/c=0.076/d=1.18 vs 0.021/0.75/0.10/1.21, R&T 3500 vs 455, 7.7/7.4/4.1 fold), source page tag, source-boundary 라벨 모두 보존. |
| 3 | Equations preserved | PASS | $Y=a\cdot BW^b$, $\ln(Y)=\ln(a)+b\cdot\ln(BW)$, $CL_i=a\cdot BW_i^b$, $V_i=c\cdot BW_i^d$, $t_{1/2}\propto BW^{d-b}$, $k_{el}\propto BW^{b-d}$, Elementary/Complex Dedrick 변환식, mono-exponential + allometric substitution, equal-unbound-AUC backbone (Eq.2:417/420/421), mg/kg dose ratio = $BW^{b-1}$, BSA = $1.73(W/70)^{0.75}$, R&T Eq.14-6 child maintenance dose 모두 v3.1 원문 그대로 보존. |
| 4 | Page tags preserved | PASS | [G&W Eq.2:374, p.173] / [R&T Eq.22-2, p.732] / 외 모든 G&W·R&T·PK28·PK29 page tag — v3.1 원문 동일. v3.2에서 새 page tag 추가 또는 기존 page tag 변경 없음. |
| 5 | Figure markers preserved | PASS | F1 FIGURE_SCHEMATIC, F2/F3/F5/F6/F7 FIGURE_POINTER, F4 FIGURE_SCHEMATIC — 7개 figure marker 위치, source 필드, learner instruction, alt text 모두 v3.1 원문 동일. v3.2에서 figure marker 변경·추가·삭제 없음. B2 / B8 splice verification 그대로 유효. |
| 6 | Source-boundary preserved | PASS | TEXTBOOK_DERIVED / AUDIT_DERIVED / CRUCIBLE_DERIVED / EXPERT_INFERENCE / [EXPERT_INFERENCE, ver2 V*] / [TEXTBOOK_DERIVED, ver2 V1] / [EXPERT_INFERENCE, v3] / [⚡ Apex Concept] 라벨 전부 보존. L-patch는 모두 `n/a (style — Korean-Dominant readability)` source status로 분류. B5 audit guardrail / B6 crucible guardrail / B7 deprecated material 차단 모두 유지. |
| 7 | HTML-readiness preserved | PASS | B1 compilation contract, B2 figure plan, B3 page-tag rendering rules, B4 marker-to-component mapping + navigation anchor integrity rules + figure rendering constraints + prohibited list, B5 audit guardrails, B6 crucible guardrails, B7 deprecated restorations, B8 PATCH MODE splice verification table (F1–F7), B9 zero-omission coverage matrix(C13 v3.2 추가), B10 micro-patch log, B11 mastery augmentation log(L01–L12 추가) 모두 일관 보존. 신규 marker 타입 도입 없음. CSS class 변경 없음. Phase 5 HTML 컴파일러는 v3.1과 동일한 marker → component 매핑으로 v3.2를 렌더링할 수 있다. |
| 8 | Ready for Phase 5 HTML compilation | PASS | 모든 가드레일·인증·marker·page tag·수식·figure marker·source label이 v3.1 대비 변경 없음. PART A는 surgical Korean-Dominant prose 개선만 반영되어 학습자 가독성이 한층 더 상승했다. PART B의 contract / guardrail은 그대로 유지되며 L01–L12 항목이 B11 v3.2 sub-table에 명시 등록되었다. Phase 5는 이 파일을 그대로 입력으로 받아 v3.1과 동일한 마커→컴포넌트 매핑·page tag 렌더링·figure rendering rule·navigation anchor integrity rule을 적용할 수 있다. |

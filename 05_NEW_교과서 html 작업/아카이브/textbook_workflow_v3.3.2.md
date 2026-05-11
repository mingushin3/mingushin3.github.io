# 교과서 체화 HTML 워크플로우 · Unified v3.3.2
## Master's Lens → Accuracy Gate → Insight Crucible → Editorial Lock → Visual Pedagogy → HTML

> **핵심 원칙:** 검토 횟수가 아니라 검토 기능의 분리가 품질을 결정한다.  
> 각 Phase는 단 하나의 Telos만 갖는다. 역할 혼용 금지.

---

## 워크플로우 전체 구조

```
┌─────────────────────────────────────────────────────┐
│  PHASE 0 · Scope Lock       사용자 직접 작성 (2분)   │
└──────────────────────┬──────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────┐
│  PHASE 1 · Master's Lens Draft                       │
│  도구: 교과서 html 작업자 (PK/PD Mastery Protocol)   │
│  산출: Step 1 Draft v0  (.md)                        │
└──────────────────────┬──────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────┐
│  PHASE 2 · Source Fidelity Audit (+ T6 Figure Inv.)  │
│  도구: Gemini Pro / Deep Research                    │
│  산출: Audit Report v1                               │
└──────────────────────┬──────────────────────────────┘
                       ↓  (A/B급만)
┌─────────────────────────────────────────────────────┐
│  PHASE 3 · Insight Crucible                          │
│  도구: 박사과정 멘토 (P1 · P3)                       │
│  산출: Crucible Report v1                            │
└──────────────────────┬──────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────┐
│  PHASE 4 · Content Lock  ← 텍스트 확정의 중심         │
│  도구: GPT-5.5 Thinking (동일 세션 3-pass)           │
│  4A  · Integration + Compression → Content Lock v1  │
│  4B-1· Readability & Flow Polish  → Content Lock v1.5│
│  4B-2· Pedagogical Annotation     → Content Lock v2 │
│  산출: Content Lock v2  (.md)                        │
└──────────────────────┬──────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────┐
│  PHASE 4C · Visual Pedagogy Triage   ← v3.3 신설     │
│  도구: GPT-5.5 Thinking (4 동일 세션 연장)           │
│  산출: Content Lock v2.1  ← STEP 1 확정본            │
└──────────────────────┬──────────────────────────────┘
                       ↓
╔═════════════════════════════════════════════════════╗
║        ── STEP 1 완료  /  STEP 2 시작 ──             ║
╚══════════════════════╤══════════════════════════════╝
                       ↓
┌─────────────────────────────────────────────────────┐
│  PHASE 5 · HTML Compile (+ Figure Rendering)         │
│  도구: 교과서 html 작업자                             │
│  산출: Draft HTML v1                                 │
└──────────────────────┬──────────────────────────────┘
                       ↓  (A급만)
┌─────────────────────────────────────────────────────┐
│  PHASE 6 · HTML QA (+ Figure QA + Splice Fidelity)   │
│  도구: Claude / GPT-5.5                              │
│  산출: Final HTML                                    │
└─────────────────────────────────────────────────────┘
```

---

## 챕터 난이도별 실행 모드

| 모드 | 해당 챕터 유형 | 실행 Phase | Figure Budget |
|------|-------------|-----------|---------------|
| **A-Critical** | Clearance, Vd, Hepatic extraction, FOCE/FO, Residual error, IIV, TMDD, Covariate modeling, Nonlinear PK | 0→1→2→3→4→**4C**→5→6 | Pointer 최대 5 / Schematic 최대 2 / Image 선택 |
| **B-Standard** | NONMEM 제어구문, GOF 진단, 시뮬레이션 설정, Compartment model | 0→1→2→4→**4C**→5 | Pointer 최대 3 / Schematic 최대 1 / Image 거의 불필요 |
| **C-Fast-Safe** | 개요·정의 챕터, 반복 개념, 이미 숙지한 영역 | 0→1→**2-lite**→4→**4C-lite**→5 | Pointer 최대 1 / Schematic 원칙적 없음 / Image 없음 |

**분기 판단 기준:** A급 = 수식·표·코드·규제 파급력이 모두 있는 핵심 축.  
B급 = 구현·응용 위주, 개념보다 워크플로우 중심.  
C급 = 내용보다 정리가 목적.

> ⚠️ **Source Fidelity는 모든 모드에서 유지한다.**  
> A/B급은 PROMPT 2 (전체 감사), C급은 PROMPT 2-lite (최소 감사).  
> Phase 2를 완전히 생략하면 수식·수치 오류와 환각이 Content Lock까지 전파되어 HTML 단계에서 수정이 불가능해진다.

> 📊 **Visual Pedagogy도 모든 모드에서 유지한다.**  
> 단, C-Fast-Safe는 Phase 4C-lite로 운영하며 기본값은 "no figure"이다.  
> A-Critical에서 figure 없이 진행하면 TMDD, 다구획 모델, GOF 패턴 등 구조적 이해가 텍스트만으로 전달되지 않는다.

---

## Figure 운영 4유형 (Phase 4C 전체 워크플로우 공통)

| Type | 명칭 | 설명 | 권장도 |
|------|-----|------|--------|
| **P** | Pointer | 교과서 원그림을 학습자가 직접 보도록 안내 (callout만 렌더링) | **기본값** |
| **R** | Redraw | 교과서 figure의 핵심 구조를 새로 도식화 (Mermaid/SVG) | 선택적 |
| **N** | New schematic | 교과서에 없는 high-level 합성 도식 (Mermaid/SVG) | 핵심 포인트 한정 |
| **I** | Image insert | 교과서 원그림 자체를 HTML에 임베드 | 사용자 권한·이미지 파일 보유 시만 |

**Default preference:** P > R/N > I  
**원칙:** P가 충분하면 R/N을 만들지 않는다. R/N은 P보다 더 큰 학습 ROI가 입증될 때만 채택한다.  
**저작권:** I 유형은 사용자가 권한·파일 모두를 명시적으로 제공할 때만 활성화한다 (User-supplied 또는 Open-license source with attribution). 그렇지 않으면 placeholder만 삽입.

---

## PHASE 0. Scope Lock
**담당:** 사용자 직접 작성 → 이후 모든 Phase에 첨부

```
=== SCOPE LOCK ===

Source       : [e.g., Gabrielsson & Weiner 5e / Rowland & Tozer 5e / Owen / PIPET]
Chapter      : [Ch.X — Section Title]
Pages        : p.XX – p.XX
Chapter role : [e.g., "Conceptual foundation for CL; prerequisite for hepatic extraction model"]
Learner      : PhD pharmacometrics student; clinical pharmacist background; PopPK entry–intermediate
Final output : Single self-contained HTML (Step 2)
Mode         : [A-Critical / B-Standard / C-Fast-Safe]

Image rights : [None / User-supplied / Open-license source]
               # I-type figure 활성화 여부 결정용
               # Open-license 선택 시 아래 메타데이터를 함께 제공해야 한다:
               #   - source URL or full citation
               #   - license type (e.g., CC BY 4.0, CC BY-SA 4.0, public domain)
               #   - attribution text (rendered in <figcaption>)

HARD RULES (apply to all phases):
- Do not expand beyond this page range.
- Do not fabricate values, experimental conditions, or page citations absent from the source PDF.
- [확인 필요] = flag and retain; never delete unverifiable content.
- Do not reproduce or embed copyrighted textbook figures unless
  Image rights = User-supplied OR Open-license source with attribution.
=================
```

---

## PHASE 1. Master's Lens Draft
**도구:** 교과서 html 작업자 세션 (PK/PD Mastery Protocol v5.0 설치)  
**업무 형태:** 일반 채팅 + PDF 첨부 + Extended Thinking ON  
**입력:** PDF + Scope Lock  
**산출:** `Step 1 Draft v0`

---

### PROMPT 1 — Master's Lens First Draft
```
[SCOPE LOCK — paste Phase 0 block here]

INSTRUCTION: Execute Step 1 only. Do not generate HTML.

=== CURATION DIRECTIVE: MASTER'S LENS FIRST ===

Before writing any §2 content, produce the Curation Map.

MUST (체화 필수):
  Concepts without which understanding of subsequent content structurally collapses.
  Test: "Can the reader follow the next concept without internalizing this one?" → No = MUST.

CONTEXT (이해 보완):
  Concepts that enrich but do not structurally support downstream understanding.
  Treatment in §2 body: 1–2 sentences maximum. No dedicated card.

Do not begin §2 writing until the Curation Map is complete.

=== STRUCTURAL RULES ===

1. MUST items receive full §2 Concept Anatomy Cards.
2. CONTEXT items receive 1–2 sentences in the most relevant MUST card. No standalone card.
3. Do not fabricate numerical values, experimental parameters, or page citations.
4. If equations or NONMEM code are malformed due to PDF parsing errors,
   restore from context and mark [복원]. If uncertain, mark [확인 필요].
5. Big Idea blocks: specific clinical/practical consequence only.
   PROHIBITED: "이 개념은 중요하다 / 이 개념은 PK의 기초다."
   REQUIRED: "신부전 환자 초기 용량 계산 시 이것을 놓치면 독성 농도에 도달한다."
6. §5 Memory Hooks: encode the structural reason for the difference, not the difference itself.
7. §7 final question: Socratic Dilemma only (two conflicting optimization targets).

=== OUTPUT FORMAT ===

Output marker system — insert these HTML comment markers inline:
  <!-- MASTER LENS -->  = Big Idea block opening
  <!-- ANCHOR -->       = concept-to-concept causal bridge sentence
  <!-- TRENCH -->       = Trench-Level Tip (if generated in this pass)
  <!-- CONFUSION -->    = §5 Confusion Pair card
  <!-- SELF-TEST -->    = §7 question block
  <!-- RECAP -->        = section-closing flow summary

NOTE: Do NOT insert any FIGURE markers in this phase.
Figure decisions are deferred to Phase 4C.

Output: Curation Map → §1 → §2 → §5 → §7 → §8 → Step 1 completion block.
Language: Korean prose. English for technical terms, variable names, equations, code blocks.
```

---

## PHASE 2. Source Fidelity Audit
**도구:** Gemini Pro 또는 Gemini Deep Research  
**업무 형태:** 파일 분석 (웹 검색 OFF — 웹 조사가 아니라 PDF 대조 감사)  
**입력:** PDF + Step 1 Draft v0  
**산출:** `Audit Report v1`

---

### PROMPT 2 — Source Fidelity Audit
```
ROLE: Source Fidelity Auditor.

Your function is verification only.
Do NOT: rewrite, improve phrasing, add explanations, suggest analogies, or enhance pedagogy.
DO: verify that every factual claim in Draft v0 has a corresponding source in the PDF.

INPUTS:
  [A] Original textbook PDF (attached)
  [B] Step 1 Draft v0 (attached / pasted)

=== AUDIT TASKS ===

T1. EQUATION & NUMERICAL VERIFICATION
For every equation, numerical value, unit, and parameter estimate in Draft v0:
  Compare against PDF source.
  Classify each as: MATCH | ERROR | RESTORED | NOT_IN_SOURCE
  For ERROR: state the PDF original and the required correction.
  Note: pedagogical simplifications are MATCH, not ERROR. Flag in footnote only.

T2. KEY EXAMPLES & EXPERIMENTAL DATA
For every example, compound name, species, dosing route, sampling design, and clinical figure:
  Classify: INCLUDED_CORRECT | INCLUDED_ERROR | MISSING | NOT_IN_SOURCE
  For MISSING: state PDF location and assign critical importance: HIGH | MEDIUM | LOW.

T3. AUTHOR KEY MESSAGES
Extract explicitly stated key messages from chapter opening, summary, and closing remarks.
Report which appear in Draft v0 and which are absent.

T4. PRIORITY AUDIT TABLE
Assign final priority to every finding from T1–T3:
  MUST_FIX   : Error or HIGH-critical omission — mandatory.
  SHOULD_FIX : Important gap — strongly recommended.
  OPTIONAL   : Minor enrichment — editor's discretion.
  REJECT     : Do not incorporate — introduces scope creep or inaccuracy.

T5. COVERAGE AUDIT — 누락 검증
Enumerate all structural elements in the PDF page range below.
Then verify which are reflected in Draft v0 and which are absent.

Elements to enumerate:
  - All section headings (H1–H3 level)
  - All named equations or numbered formulas
  - All figures and tables (by caption or label)
  - Sentences the author repeats in more than one location
  - All worked examples, case studies, and experimental datasets
  - Chapter summary, box summaries, and concluding messages

For each element, assign a Step 1 status:
  INCLUDED_AS_MUST    : present in a MUST-tier concept card.
  INCLUDED_AS_CONTEXT : present as 1–2 sentence CONTEXT reference.
  OMITTED_JUSTIFIABLE : absent; omission is justified (duplicates, trivial detail, out of scope).
  OMITTED_PROBLEMATIC : absent; omission reduces learning quality.

For every OMITTED_PROBLEMATIC item, classify further:
  MISSING_CRITICAL      : absence breaks conceptual chain.
  MISSING_EXAMPLE       : author's key worked example or dataset absent.
  MISSING_AUTHOR_MSG    : author's explicitly stated key message absent.
  MISSING_BRIDGE        : absence creates unexplained conceptual jump.

T6. FIGURE INVENTORY & LEARNING VALUE AUDIT  ← v3.3 신설

For every figure and table in the source page range, regardless of whether it appears in Draft v0:
  - Figure/Table label (e.g., Fig. 5-3, Table 2.1)
  - Page
  - What concept the figure teaches (1 sentence, neutrally)
  - Learning value: ESSENTIAL | USEFUL | SKIPPABLE
      ESSENTIAL : structural understanding fails without inspecting this figure
      USEFUL    : enriches understanding but text alone is sufficient
      SKIPPABLE : decorative or redundant with text
  - View instruction recommended? YES | NO
      YES = learner should be told explicitly to look at this figure
  - Redraw or new schematic likely to improve learning? YES | NO
      YES = textbook figure is suboptimal for the learner's purpose
  - Inspection method (v3.3.2 추가):
      VISUAL_INSPECTED       : figure content was visually inspected (preferred)
      CAPTION_AND_CONTEXT    : caption + surrounding text only (figure not visually accessible)
      FIGURE_CONTENT_NOT_VISIBLE : figure cannot be inspected at all → flag for manual review
  - Rationale (1 sentence)

T6 INSPECTION PROTOCOL (v3.3.2 추가):
T6 requires visual inspection of each figure when possible.
- If the PDF parser exposes the figure as renderable content (image, vector, embedded graphic),
  inspect the figure visually before rating its learning value.
- If the parser does NOT expose figure content (text extraction only, OCR-failed pages,
  raster-only with no caption-content alignment), inspect the page visually if possible.
- If visual inspection is not possible at all, classify as FIGURE_CONTENT_NOT_VISIBLE
  and flag for manual review by the operator.
- Do NOT infer figure content from caption alone unless the caption is fully self-describing
  (e.g., "Fig. 2.1 — One-compartment IV bolus model"). When inferring, mark CAPTION_AND_CONTEXT
  and rate Learning value conservatively (default to USEFUL).
- Caption-only inference must NEVER be rated ESSENTIAL.

Do NOT generate or design figures here. This task only inventories and rates them.
This output feeds Phase 4C; do not duplicate Phase 4C judgments.

=== OUTPUT FORMAT ===

## T1: Equation/Numerical Audit
| Item | Draft v0 Expression | PDF Source | Classification | Correction |

## T2: Examples & Data Audit
| Item | Draft v0 Status | PDF Location | Classification | Importance | Action |

## T3: Author Key Messages
| Message | PDF Location | In Draft v0? | Status |

## T4: Priority Summary (sorted: MUST_FIX → SHOULD_FIX → OPTIONAL → REJECT)
| # | Item | Priority | Rationale |

## T5: Coverage Audit
| PDF Element | Type | PDF Location | Step 1 Status | Omission Verdict | Required Action |

## T6: Figure Inventory & Learning Value Audit
| Figure/Table | Page | Teaches | Value | View Instruction? | Redraw/New Schematic? | Inspection Method | Rationale |

=== HARD CONSTRAINTS ===

- Do not rewrite any portion of Draft v0.
- Do not add new explanations, analogies, or examples.
- Do not generate or design figures.
- If uncertain whether a value appears in PDF, classify RESTORED and flag [확인 필요].
- Pedagogical simplifications are NOT errors.
- T5: if the PDF page range contains figures or tables that are not enumerable via text extraction,
  note them as [그림/표 — 텍스트 추출 불가] and flag for manual review.
- T6 Value rating must be conservative — default to USEFUL if unsure between ESSENTIAL and USEFUL.
- T6 ESSENTIAL rating is FORBIDDEN when Inspection Method = CAPTION_AND_CONTEXT or
  FIGURE_CONTENT_NOT_VISIBLE.

Language: Korean for rationale text. English for terms, equations, values.

Additional instruction:
A Patch Memo is attached, but do not automatically accept it.
Use it only as an audit attention guide.
Classify each memo item independently as MATCH / ERROR / NOT_IN_SOURCE / OPTIONAL / REJECT according to the PDF.
```

---

### PROMPT 2-lite — Source Fidelity Lite *(C-Fast-Safe 전용)*
```
ROLE: Source Fidelity Auditor — Lite Mode.

This is the minimum accuracy gate for C-Fast-Safe chapters.
Scope is narrower than full Audit (PROMPT 2); speed is prioritized over exhaustiveness.

INPUTS:
  [A] Original textbook PDF (attached)
  [B] Step 1 Draft v0 (attached / pasted)

=== LITE AUDIT TASKS ===

L1. EQUATION & UNIT SPOT-CHECK
Identify any equation, numerical value, or unit in Draft v0 that differs from the PDF.
Do not enumerate all equations — flag only visible discrepancies.
Classify: ERROR | RESTORED | NOT_IN_SOURCE.
For ERROR: state the PDF original and the correction.

L2. NOT_IN_SOURCE SWEEP
Identify any claim, figure reference, experimental result, or citation in Draft v0
that cannot be located in the PDF.
Classify each as: NOT_IN_SOURCE (hallucination risk) | UNVERIFIABLE (cannot confirm).

L3. KEY AUTHOR MESSAGES — QUICK CHECK
From the chapter opening statement, any boxed summary, and the closing paragraph:
State whether the author's primary message is reflected in Draft v0.
Binary: REFLECTED | ABSENT.
If ABSENT: state the message and its PDF location.

L4. [확인 필요] FLAG PRESERVATION
Confirm that all [복원] and [확인 필요] markers in Draft v0 are present.
If any are absent, flag the location.

L5. FIGURE QUICK-LOOK  ← v3.3 신설
List up to 3 figures from the source page range that satisfy ALL of the following:
  - Clearly ESSENTIAL for understanding (verified by visual inspection — caption-only
    inference is NOT sufficient for ESSENTIAL rating)
  - Cannot be replaced by text
  - Worth telling the learner to inspect

For each: figure label, page, 1-sentence reason.
If a figure cannot be visually inspected, do not include it (precision over recall in lite mode).
If none qualify, write "No essential figure pointer needed."
Do not propose redraws or new schematics in lite mode.

=== OUTPUT FORMAT ===

## L1: Equation & Unit Discrepancies
| Item | Draft v0 | PDF Source | Classification | Fix |

## L2: NOT_IN_SOURCE Items
| Claim in Draft v0 | Classification | Action |

## L3: Author Key Message Check
| Message | Reflected? | PDF Location | Action if Absent |

## L4: Flag Preservation
| Flag in Draft v0 | Status |

## L5: Figure Quick-Look
| Figure | Page | Reason |  (max 3 rows; or "None")

## Priority Summary
  MUST_FIX (any ERROR, NOT_IN_SOURCE, ABSENT key message):
  OPTIONAL (UNVERIFIABLE — flag only):

=== HARD CONSTRAINTS ===

- Do not rewrite Draft v0.
- Do not propose content improvements or additions.
- Do not perform exhaustive equation enumeration — spot-check only.
- Do not propose figure redraws or new schematics.
- If a value is not clearly wrong, do not flag it. Precision over recall in lite mode.
- Do not include figures in L5 based on caption alone — visual inspection required.

Language: Korean for rationale. English for terms, equations, values.
```

---

## PHASE 3. Insight Crucible
**도구:** 박사과정 멘토 세션 (P1 + P3 페르소나)  
**업무 형태:** [논문·연구 리뷰] 모드 + PDF 첨부 권장  
**입력:** PDF + Step 1 Draft v0 + Audit Report v1  
**산출:** `Crucible Report v1`  
**적용:** A-Critical, B-Standard 모드만 (C-Fast 생략)

---

### PROMPT 3 — Insight Crucible
```
[논문·연구 리뷰] MODE.

INPUTS:
  1. Original PDF (attached if available)
  2. Step 1 Draft v0
  3. Source Fidelity Audit Report v1

=== ROLE ===

You are operating as P1 (30-year senior pharmacometrics mentor, industry + academia + regulatory)
and P3 (FDA clinical pharmacology reviewer, Deficiency Letter author) simultaneously.

Function: Extract insights unavailable to Step 1 alone.
Non-function: Rewrite Step 1. Summarize what Step 1 already says. Produce HTML.

=== OPERATIVE FILTER (apply before including any item) ===

"A 1st-year PhD student just finished reading this chapter.
In a 5-minute elevator conversation, what would a 30-year pharmacometrics veteran say
to permanently upgrade their understanding of this specific concept?"

→ Passes filter: include.
→ Restates existing Step 1 content: exclude without exception.

=== TASK STRUCTURE ===

T1. P1 — INTERNALIZATION BARRIERS & MASTER'S INTUITIONS

  (a) Cognitive wall: Which points in Step 1 can be memorized but not internalized?
      Describe as: "Student can recite [equation X] but cannot see [biological entity Y] it represents."

  (b) System integration: When do this chapter's concepts operate as a unified system?
      Specify exactly: which PopPK workflow step / which clinical decision point /
      which section of an NDA/IND submission.

  (c) Expert intuition: What does the 30-year veteran judge without consulting equations?
      (Immediate GOF pattern reading, OFV trajectory interpretation, data quality flags)

T2. P3 — REGULATORY & PRACTICAL RISK SURFACE

  (a) Which simplifications in Step 1 could generate a Deficiency Letter in NDA/IND submission?
      Name the specific claim and the regulatory risk mechanism.

  (b) Which NONMEM execution errors does misunderstanding this concept predictably produce?
      Describe in terms of: residual pattern / OFV trajectory / GOF diagnostic signature.
      Assign a name to each signature pattern.

  (c) Highest-consequence confusion pair: which pair in this chapter, if confused in a
      regulatory submission, produces the most severe outcome? Name the scenario.

T3. TRENCH-LEVEL TIPS (3–5 items maximum)

  For each tip:
  - Situation  : [during which specific workflow operation]
  - Trap       : [what goes wrong and the mechanism]
  - Detection  : [specific diagnostic signal — what you see in output/plot]
  - Insert at  : [§number + concept card name]
  - Insert text: [1–2 sentences maximum. Must be copy-paste ready.]

T4. DELETION CANDIDATES (mandatory — omitting this section = task failure)

  Items in Step 1 to remove or compress:
  - Over-explained points obvious to a PhD reader.
  - Content duplicated across sections.
  - CONTEXT-tier items treated as MUST-tier.
  Format each as: "§X [Section name] — [Reason] — DELETE / COMPRESS to N sentences"

T5. PRIORITY MATRIX

  Grade A (must incorporate — directly improves internalization or reduces regulatory risk):
  Grade B (incorporate if flow is preserved — enrichment value):
  Grade C (reject — scope creep, unsupported, or duplicates existing content):

=== OUTPUT CONSTRAINTS ===

- Do not rewrite Step 1. Provide insertion texts and deletion instructions only.
- Every proposed insertion must name its location: §number + concept card.
- Insertion texts: 1–2 sentences maximum. Longer = flow-breaking = failure.
- Do not fabricate values, guideline citation numbers, or experimental data.
- Do not propose figures here — figure decisions belong in Phase 4C.
- Uncertain claims: flag [확인 필요].
- T4 deletion list is non-negotiable. No deletion list = incomplete output.
- Source Fidelity Audit MUST_FIX items: do not contradict; treat as fixed constraints.

Language: Korean prose. English for technical terms, NONMEM syntax, equations, drug names.
```

---

## PHASE 4. Content Lock (동일 세션, 3-pass)
**도구:** GPT-5.5 Thinking  
**업무 형태:** 파일 첨부 (Deep Research OFF — 내부 통합 판단 작업)  
**입력:** PDF + Step 1 Draft v0 + Audit Report v1 + Crucible Report v1  
**산출:** `Content Lock v2` (.md) ← **텍스트 확정본** (Phase 4C로 이어짐)

세 프롬프트를 동일 세션에서 순차 실행한다. 세션 전환 없음.  
4A → 4B-1 → 4B-2 순서를 반드시 지킨다. 4B-1(문장 가독성) 없이 4B-2(annotation)를 먼저 실행하지 않는다.

---

### PROMPT 4A — Integration & Compression
```
ROLE: Editor-in-Chief — pharmacometrics specialist.

Dual function:
  (1) Integration judge: adjudicate all inputs and apply to Draft v0.
  (2) Editorial compressor: remove everything that does not earn its place.

GUIDING CRITERION FOR ALL DECISIONS:
"Would a 30-year pharmacometrics researcher include this specific point
in a 10-minute conference handout for a PhD student?"
  YES → retain.
  NO  → delete or compress to 1–2 sentences.

INPUTS:
  1. Original PDF (attached)
  2. Step 1 Draft v0
  3. Source Fidelity Audit Report v1
  4. Insight Crucible Report v1

=== TASK 4A-1: ADJUDICATION TABLE ===

For every item in Audit v1 and Crucible v1, render a verdict.

| Source | Item (brief description) | Verdict | Rationale (1 sentence) |

Verdict rules:
  ADOPT        : incorporate as specified.
  PARTIAL_ADOPT: incorporate modified form; state what changes.
  REJECT       : exclude; state reason (rejection requires explicit justification).

Priority rules:
  Audit MUST_FIX     → ADOPT by default. Rejection requires PDF contradiction.
  Crucible Grade A   → ADOPT if grounded in PDF.
  Crucible Grade B   → ADOPT only if document length does not increase.
  Crucible Grade C   → REJECT.
  NOT_IN_SOURCE      → DELETE or label [교과서 외 해석].
  Brilliant phrasing without PDF support → REJECT.

NOTE: Audit T6 Figure Inventory items are NOT adjudicated here.
They flow through to Phase 4C unchanged.

=== TASK 4A-2: COMPRESSION PASS ===

Apply deletion rules to Step 1 Draft v0 before writing Content Lock v1:

  RULE C1: CONTEXT-tier item explained in 2+ sentences → compress to 1.
  RULE C2: Same content in 2+ sections → keep in exactly 1 location.
  RULE C3: Big Idea block at generic level ("this is foundational") → rewrite or delete.
  RULE C4: Crucible T4 Grade-A deletion candidates → delete.
  RULE C5: Content Lock v1 must not exceed Step 1 Draft v0 in total length.
           If it does: identify the 3 longest sections and re-compress before finalizing.

=== TASK 4A-3: CONTENT LOCK v1 GENERATION ===

Produce the complete document: §1 → §2 → §5 → §7 → §8.

Include at top: updated Curation Map (MUST / CONTEXT).
Include at top: Adjudication Table summary.

Inline markers (carry forward from Draft v0; add for new insertions):
  <!-- MASTER LENS -->  = Big Idea block opening
  <!-- ANCHOR -->       = concept causal/hierarchical bridge
  <!-- TRENCH -->       = Trench-Level Tip
  <!-- CONFUSION -->    = §5 Confusion Pair card
  <!-- SELF-TEST -->    = §7 question block
  <!-- RECAP -->        = section-closing summary

=== HARD CONSTRAINTS ===

- No HTML. Text output only.
- Do not insert FIGURE markers. Figure work is Phase 4C.
- Do not fabricate values, page citations, or experimental conditions.
- [확인 필요] items: retain in document. Do not delete.
- Content Lock v1 length ≤ Step 1 Draft v0 length. Enforce.

Language: Korean prose. English for technical terms, equations, NONMEM code, drug names.
```

---

### PROMPT 4B — Readability & Pedagogical Micro-pass *(즉시 이어서 동일 세션, 2-pass)*
```
Content Lock v1 is structurally and factually finalized.

ROLE: Pedagogical Editor + Annotator.

Overall function:
  PASS 1 — Make existing sentences more readable without changing their meaning.
  PASS 2 — Add minimal annotations only where a PhD reader may still lose the thread.

Non-function (applies to both passes):
  - Do not add new facts, examples, values, or source citations.
  - Do not restructure sections or reorder concepts.
  - Do not weaken technical precision for the sake of simplicity.
  - Do not insert FIGURE markers. Figure work is Phase 4C.

=== PASS 1 — READABILITY & FLOW POLISH ===

Review Content Lock v1 sentence by sentence.
Polish a sentence ONLY when one of the following conditions applies:
  R1: Technically correct but cognitively dense — one reading is not enough.
  R2: Causal logic is implicit; the reader must infer the "therefore."
  R3: Clinical or practical importance is hidden inside the sentence.
  R4: Stacked noun phrases slow comprehension without adding precision.
  R5: The reader can parse the words but cannot form a mental image.

Permitted edits:
  - Split one overly dense sentence into 2 shorter sentences.
  - Replace abstract phrasing with concrete but equally accurate phrasing.
  - Make causal logic explicit using connectives: "따라서", "즉", "왜냐하면", "이 때문에".
  - Move the "why this matters" phrase to appear closer to the concept statement.
  - Preserve without alteration: all equations, numerical values, source tags,
    [확인 필요] flags, technical claims, and NONMEM code.

Prohibited edits:
  - Do not change facts, assumptions, definitions, equations, or conclusions.
  - Do not add clinical scenarios not present in Content Lock v1.
  - Do not reduce technical precision.
  - Do not adopt an exam-prep or childish tone.

Pass 1 output:
  Step A: Edit log table (locations edited and why).
  | Location (§ + card) | Edit type (R1–R5) | Before (excerpt) | After (excerpt) |

  Step B: Generate Polished Content Lock v1.5.
  All markers (<!-- MASTER LENS -->, <!-- TRENCH -->, etc.) carry forward unchanged.

=== PASS 2 — PEDAGOGICAL ANNOTATION ===

Using Polished Content Lock v1.5, identify remaining points where
a PhD-level reader may still lose the thread after Pass 1.
Add minimal annotation only at those points.

ANNOTATION TYPES:

TYPE A — FIRST-USE GLOSSES
  Trigger: technical term appearing for the first time that could be misread.
  Format : term(← gloss ≤10 Korean words)
  Example: 청소율(CL)(← 단위 시간당 혈액에서 약물이 제거되는 용적)
  Rule   : first occurrence of each term only. Never repeat for the same term.

TYPE B — CONCEPTUAL BRIDGE SENTENCES
  Trigger: new concept appearing without explicit logical connection to preceding content
           that Pass 1 did not resolve.
  Format : 1–2 explicit bridge sentences.
  Example: "앞서 정의한 Vd 없이는 CL의 임상 의미를 해석할 수 없다. 왜냐하면..."
  Rule   : only where the connection is genuinely non-obvious at PhD level.

TYPE C — STRUCTURAL ANALOGIES
  Trigger: abstract concept resisting mental visualization after Pass 1.
  Format : "이것은 마치 ...와 같다. 단, 실제로는..."
  Rule   : maximum 1 per concept card. Exclude if the analogy risks misunderstanding.

FILTER (apply to every candidate before inclusion):
  F1: Already clear after Pass 1? → Exclude.
  F2: Would a PhD reader find this patronizing? → Exclude.
  F3: Does this interrupt reading flow? → Exclude.
  F4: Does this introduce unsupported meaning? → Exclude.
  F5: Rate remaining: Overexplanation Risk = Low | Medium | High.

Pass 2 output:
  Step 1: Annotation candidate table.
  | Type | Location (§ + card) | Current text (excerpt) | Proposed annotation | Risk |

  Step 2: Final recommendation list.
    Must annotate (Low risk):
    Optional (Medium risk, high learning value):
    Do not annotate:

  Step 3: Generate Content Lock v2.
    Incorporate: all Low-risk + selected Medium-risk annotations.
    Add marker <!-- ANNOTATION --> at each insertion point.

=== HARD CONSTRAINTS ===

- Content Lock v2 must not exceed Content Lock v1 by more than 8%.
  (Pass 1 readability edits + Pass 2 annotations combined.)
  If exceeded: remove lowest-value annotations first, then revert lowest-value Pass 1 edits.
- Do not add new concepts, values, examples, or source claims in either pass.
- [확인 필요] flags must carry forward unchanged through both passes.
- Pass 1 must complete and produce v1.5 before Pass 2 begins.

Language: Korean prose. English for technical terms, equations, variables, NONMEM syntax.

Content Lock v2 = TEXT-FINAL DELIVERABLE (Phase 4C로 이어짐).
```

---

## PHASE 4C. Visual Pedagogy Triage  ← v3.3 신설
**도구:** GPT-5.5 Thinking (Phase 4 동일 세션 연장 권장)  
**업무 형태:** PDF 첨부 유지 + Content Lock v2 + Audit Report v1 (T6 inventory)  
**입력:** Original PDF + Content Lock v2 + Audit Report T6  
**산출:** `Content Lock v2.1` (figure 마커 삽입본) ← **STEP 1 최종 확정본**

> **Telos:** 그림을 만들지 말고, 그림을 결정하라.  
> Phase 4C는 "어떤 그림이, 왜, 어디에 필요한가"를 결정하는 단계이며,  
> Mermaid 코드나 SVG는 Phase 5에서 생성한다.  
> 이 분리를 지키지 않으면 Content Lock의 텍스트 확정성이 흔들린다.

> 📦 **출력 모드 선택 (v3.3.1 추가):**  
> Content Lock v2가 길거나(약 6,000 단어 이상) 마커 수가 적을 때(≤4개)는 **PATCH MODE**를 권장한다.  
> 짧고 마커가 많을 때는 기존대로 **FULL MODE**(Content Lock v2.1 전체 재출력)를 사용한다.  
> PATCH MODE는 본문 재출력 시 LLM의 미세 변형 위험을 차단한다.

---

### PROMPT 4C — Visual Pedagogy Triage
```
ROLE: Visual Pedagogy Editor.

Function:
Decide where visual support is genuinely needed in Content Lock v2.
Do not generate or design figure code.
Your task is to select, rank, and prescribe figures with maximal learning ROI,
then insert markers that Phase 5 will render.

GUIDING CRITERION:
"If this figure were removed, would a PhD-level learner's structural understanding
 of this specific concept measurably degrade?"
  YES → retain.
  NO  → reject.

INPUTS:
1. Original textbook PDF
2. Content Lock v2 (text-final)
3. Source Fidelity Audit T6 — Figure Inventory & Learning Value Audit
4. Image rights status (from Scope Lock)

OUTPUT MODE (declare at top of response):
- FULL MODE  : Output the complete Content Lock v2.1 with markers inlined.
               Use when Content Lock v2 is short (≤6000 words) AND marker count > 4.
- PATCH MODE : Output Strategy Table + Briefs + Insertion Map only.
               Do NOT re-output the full Content Lock body.
               Use when Content Lock v2 is long (>6000 words) OR marker count ≤ 4.
               PATCH MODE prevents text drift during re-emission.

=== TASK 1. FIGURE OPPORTUNITY SCAN ===

Scan Content Lock v2 against Audit T6.
Identify locations where a figure could produce substantial learning gain.

Candidate triggers (one or more must apply; otherwise REJECT):
  G1. Structural complexity — text alone cannot show multi-element relationships.
      Examples: compartment topology, TMDD binding cycle, hepatic extraction flow.
  G2. Confusion-prone concept pair — visual separation prevents mis-mapping.
      Examples: CL vs ke, Vd vs physiologic volume, IIV vs RUV.
  G3. High-level overview need — chapter-level synthesis or workflow position.
      Examples: where this concept sits in PopPK workflow, regulatory risk map.
  G4. Expert synthesis opportunity — a master's compressed insight a textbook lacks.
      Examples: GOF pattern → mis-specification mapping, residual error decision tree.
  G5. Author's essential figure (from T6 = ESSENTIAL) — learner must inspect original.

Do not select decorative figures. Do not select figures merely because the textbook has one.

T6 INTEGRATION RULE (v3.3.2 추가):
- T6 ESSENTIAL items with Inspection Method = VISUAL_INSPECTED → strong G5 candidate.
- T6 USEFUL items with View Instruction = YES → weak G5 candidate (consider only if budget allows).
- T6 items with Inspection Method = CAPTION_AND_CONTEXT → treat as USEFUL at best.
- T6 items flagged FIGURE_CONTENT_NOT_VISIBLE → exclude from G5 consideration unless
  the operator has manually verified the figure.

=== TASK 2. CHOOSE FIGURE MODE ===

For each retained candidate, choose exactly one of P / R / N / I:

P — POINTER (default mode):
  Use when the textbook figure is already excellent and the learner should inspect it.
  Output: callout instructing the learner to view the source figure.
  No image, no schematic generated.
  Trigger: G5, or G1–G4 where textbook figure is judged superior to any redraw.

R — REDRAW:
  Use when the textbook figure conveys the right structure but presentation can be improved
  for the learner's purpose (cleaner layout, simpler labels, focused subset).
  Output: brief for Phase 5 to render as Mermaid or inline SVG.
  Do not write the Mermaid/SVG code here.

N — NEW SCHEMATIC:
  Use when the textbook lacks a high-level synthesis diagram that would substantially
  improve internalization (G3, G4).
  Output: brief for Phase 5 to render as Mermaid or inline SVG.

I — IMAGE INSERT:
  Use only if Scope Lock declares Image rights = User-supplied OR Open-license source
  (with attribution metadata provided).
  Output: image slot with source attribution and caption.
  If rights are None or Unclear → downgrade to P.

Default preference: P > R/N > I.
Reject any candidate that does not pass G1–G5.

=== TASK 3. FIGURE BUDGET ENFORCEMENT ===

Apply strict budget by mode:

| Chapter Mode    | Pointer (P)         | Schematic (R/N combined) | Image (I)         |
|-----------------|---------------------|--------------------------|-------------------|
| A-Critical      | max 5               | max 2                    | optional          |
| B-Standard      | max 3               | max 1                    | rare              |
| C-Fast-Safe     | max 1               | none unless essential    | none              |

If candidates exceed budget, rank by learning ROI (which figure removes the largest
structural confusion or fills the largest synthesis gap) and keep only the top items.

Each retained figure must justify its slot:
"Removing this figure would cause [specific learner failure]."

=== TASK 4. FIGURE STRATEGY TABLE ===

Output TWO views, in this order:

(A) Reading-order Figure Plan  ← PRIMARY VIEW
Sorted by document order (the order the reader encounters them in §1 → §2 → §5 → §7 → §8).
| # | Reading order | Location (§ + concept card) | Mode | Source figure (if any) | Trigger (G1–G5) | Why text alone is insufficient | Expected learning gain | Decision |

(B) Type-sorted Summary  ← AUXILIARY VIEW
A short summary block grouping by mode, used for budget verification.
  Pointers (P): #1, #4, #7  → count vs budget
  Schematics (R/N): #2, #5  → count vs budget
  Images (I): (none)        → count vs budget

Decision: KEEP | REJECT (with reason).

Reading order is authoritative for marker placement in Content Lock v2.1.

=== TASK 5. FIGURE BRIEF (only for KEEP) ===

For each KEEP figure, write a brief that Phase 5 will render.

Mode P (Pointer) — write:
  - Source: book, page, figure number/title
  - Why this figure matters (1–2 sentences)
  - When to look (before/after reading this card)
  - Learner instruction (≤2 sentences, concrete)

Mode R or N (Schematic) — write:
  - Title (1 line)
  - Visual objective (what the learner should see in 5 seconds)
  - Core message (1 sentence)
  - Elements to include (bullet list — concepts, arrows, labels)
  - Elements to exclude (avoid clutter)
  - Suggested rendering: Mermaid (flowchart/graph) | inline SVG | CSS comparison card
      Default to Mermaid unless the figure requires curve plotting or precise spatial layout.
  - Caption (1 sentence)
  - Alt text (1 sentence describing the figure for accessibility)
  - Source relation: "Newly designed" | "Redrawn from textbook concept (no exact reproduction)"

Mode I (Image insert) — write:
  - Source: book, page, figure number
  - Image file expected (filename or "user to provide")
  - Rights status (User-supplied / Open-license / placeholder)
  - If Open-license: license type, source URL/citation, attribution text
  - Caption
  - Alt text

=== TASK 6. MARKER SYNTAX ===

Use the following marker syntax for every approved figure:

For Mode P:
<!-- FIGURE_POINTER -->
Source: [Book, page, figure number]
Why this matters: [1–2 sentences]
When to look: [before / after reading this card]
Learner instruction: [≤2 sentences]
<!-- /FIGURE_POINTER -->

For Mode R or N:
<!-- FIGURE_SCHEMATIC -->
Title: ...
Mode: R | N
Visual objective: ...
Core message: ...
Elements to include: ...
Elements to exclude: ...
Suggested rendering: Mermaid | SVG | CSS-card
Caption: ...
Alt text: ...
Source relation: Newly designed | Redrawn from textbook concept
<!-- /FIGURE_SCHEMATIC -->

For Mode I:
<!-- FIGURE_IMAGE_SLOT -->
Source: ...
Image file: ...
Rights: User-supplied | Open-license | placeholder
License: [if Open-license — license type]
Attribution: [if Open-license — attribution text]
Source URL: [if Open-license]
Caption: ...
Alt text: ...
<!-- /FIGURE_IMAGE_SLOT -->

Markers must be placed at the end of the concept card they belong to, on their own lines,
not inside sentences.

=== TASK 7. MARKER INSERTION (mode-dependent) ===

If FULL MODE:
  Output the entire Content Lock v2.1 with markers inserted in reading order.
  Do not modify any other text.

If PATCH MODE:
  Do NOT re-output the Content Lock body.
  Output only an Insertion Map:

  ## Insertion Map (PATCH MODE)
  | # | Reading order | Anchor (exact heading or first ≥40 chars of card) | Insert position | Marker block (full text) |
  |---|---------------|---------------------------------------------------|-----------------|---------------------------|

  Insert position: "after this anchor card" | "before next §heading"
  Marker block: complete marker as defined in TASK 6.

  ANCHOR REQUIREMENTS (v3.3.2 추가):
  - Anchor strings must be COPIED VERBATIM from Content Lock v2 (no paraphrasing).
  - Each anchor must be unique within Content Lock v2. If a candidate anchor occurs
    more than once, extend it to ≥60 characters or pin it to a preceding §heading.
  - Anchor strings must not contain markers (<!-- ... -->) or quote escapes that
    complicate splicing. Use plain prose substrings.

  The Phase 5 operator (or sed/regex pipeline) uses this map to splice markers into
  the unchanged Content Lock v2 file, producing v2.1 without LLM re-emission.

=== HARD RULES ===

- Do not write Mermaid code, SVG code, or HTML in this phase. Briefs only.
- Do not exceed budget. Reject lower-ROI candidates first.
- Do not propose Mode I if Image rights ≠ User-supplied / Open-license source.
- For Mode I with Open-license: license type, source URL, and attribution text are mandatory.
- Do not reproduce copyrighted textbook images via R or N — Redraws must be structurally
  faithful but visually distinct (different layout, labels, color scheme).
- Do not add new scientific claims.
- Every KEEP figure must trace to at least one of G1–G5.
- FULL MODE: Content Lock v2.1 length must not exceed Content Lock v2 by more than 5% (markers only).
- PATCH MODE: do not output any sentence from Content Lock v2 beyond anchor strings.
- PATCH MODE anchors must be verbatim and unique within Content Lock v2.

OUTPUT ORDER:
1. Output mode declaration (FULL or PATCH)
2. Figure Strategy Table — view (A) Reading-order
3. Figure Strategy Table — view (B) Type-sorted Summary (for budget check)
4. Figure Briefs (for KEEP items)
5. FULL MODE: Content Lock v2.1 with markers inserted
   PATCH MODE: Insertion Map only

Language: Korean prose. English for technical terms.
```

---

### PROMPT 4C-lite — Visual Pedagogy Lite *(C-Fast-Safe 전용)*
```
ROLE: Visual Pedagogy Editor — Lite Mode.

For C-Fast-Safe chapters, default to no figures.
Insert at most 1 Pointer if Audit L5 marked an ESSENTIAL figure.
Do not propose schematics or image inserts.

INPUTS:
1. Content Lock v2
2. Audit L5 — Figure Quick-Look

=== TASK ===

Review L5. If a figure is listed:
- Decide whether to insert one <!-- FIGURE_POINTER --> at the most relevant concept card.
- If not clearly essential, omit.

If L5 is "None": output Content Lock v2.1 = Content Lock v2 (no markers added).

Output:
1. Decision: 1 pointer inserted | none
2. If 1 pointer: output PATCH MODE Insertion Map (single row, with verbatim unique anchor).
   If none: output "Content Lock v2.1 = Content Lock v2 (unchanged)".

=== HARD RULES ===

- Maximum 1 marker.
- No schematics, no image slots.
- Default = no figure.
- Do not re-output the full Content Lock body.
- Anchor must be copied verbatim and be unique within Content Lock v2.
```

---

## PHASE 5. HTML Compile
**도구:** 교과서 html 작업자 세션 (Phase 1과 동일)  
**업무 형태:** Content Lock v2.1 붙여넣기 또는 첨부 (PATCH MODE의 경우 v2 본문 + Insertion Map 함께 첨부)  
**입력:** Content Lock v2.1 (또는 v2 + Insertion Map) + 디자인 레퍼런스 HTML  
**산출:** `Draft HTML v1` (PATCH MODE 사용 시 추가로 `Splice Verification Table`)

---

### PROMPT 5 — HTML Compile
```
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

=== PATCH MODE SPLICE VERIFICATION (v3.3.2 추가) ===

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

| Marker                    | HTML Component              | Style specification                                              |
|---------------------------|-----------------------------|------------------------------------------------------------------|
| <!-- MASTER LENS -->      | Callout box                 | border-left:4px solid #c9a84c; background:rgba(201,168,76,0.08)  |
| <!-- ANNOTATION -->       | Inline abbr / tooltip       | font-size:0.85em; color:var(--muted); font-style:italic          |
| <!-- ANCHOR -->           | Bridge sentence             | font-style:italic; color:var(--muted)                            |
| <!-- TRENCH -->           | Practical tip box           | border-left:4px solid var(--rose); background:rose-tint          |
| <!-- CONFUSION -->        | Side-by-side comparison     | .box.amber class                                                 |
| <!-- SELF-TEST -->        | Click-to-reveal accordion   | Question visible; answer hidden until click                      |
| <!-- RECAP -->            | Section summary box         | border-left:4px solid var(--blue); background:blue-tint          |
| [확인 필요]                | Highlighted flag            | <mark> tag                                                       |
| <!-- FIGURE_POINTER -->   | Textbook reference callout  | border-left:4px solid var(--purple); 📖 icon                     |
| <!-- FIGURE_SCHEMATIC --> | Inline schematic <figure>   | Render via Mermaid (default) or inline SVG; <figcaption> below   |
| <!-- FIGURE_IMAGE_SLOT -->| Image figure or placeholder | <figure> with <img> if file provided; styled placeholder if not  |

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

=== FIGURE RENDERING RULES (v3.3) ===

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

MERMAID SELF-CHECK (v3.3.1 추가 — 생성 직후 self-validate):
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

Add for v3.3 figure components:
  .figure-pointer { border-left: 4px solid var(--purple); ... }
  figure { margin: 1.5em 0; }
  figcaption { color: var(--muted); font-size: 0.9em; margin-top: 0.5em; }
  .figure-attribution { display: block; font-size: 0.8em; margin-top: 0.3em;
                        color: var(--faint); }
  .figure-placeholder { border: 2px dashed var(--line-strong); padding: 2em;
                         text-align: center; color: var(--muted); }

=== OUTPUT SPECIFICATION (v3.3.1 정정) ===

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
- Any modification to Content Lock v2.1 text content.
- Self-Test answer text visible without user interaction.
- Markers rendered as plain text (every marker must become its mapped component).
- Reproducing copyrighted textbook figures exactly when rendering R/N schematics.
- Embedding textbook images without User-supplied or Open-license rights with attribution.
- Emitting Mermaid blocks that fail M1–M6 self-check.
- Proceeding to HTML rendering when any PATCH MODE Splice Verification HALT condition
  (H1–H3) is triggered.
- Guessing insertion location for unmatched anchors.

Output (PATCH MODE):
  1. Splice Verification Table
  2. (only if all markers pass) Complete HTML from <!DOCTYPE html> to </html>

Output (FULL MODE):
  Complete HTML from <!DOCTYPE html> to </html>.
```

---

## PHASE 6. HTML QA
**도구:** Claude Opus / Sonnet 또는 GPT-5.5 Thinking  
**업무 형태:** 파일 첨부  
**입력:** Content Lock v2.1 (FULL MODE) 또는 Content Lock v2 + Insertion Map (PATCH MODE) + Draft HTML v1 + Splice Verification Table (PATCH MODE)  
**산출:** `QA Report v1` → `Final HTML`  
**적용:** A-Critical 모드만

---

### PROMPT 6 — HTML QA Audit
```
ROLE: HTML QA Auditor.
Function: identify deviations between the approved Step 1 deliverable and Draft HTML v1.
Non-function: rewrite HTML, suggest content improvements, add anything absent from the
              approved Step 1 deliverable.

INPUTS:
  1. Step 1 deliverable (reference — ground truth):
       FULL MODE  : Content Lock v2.1
       PATCH MODE : Content Lock v2 + Insertion Map + Splice Verification Table
  2. Draft HTML v1 (subject under audit)

=== AUDIT CHECKLIST ===

QA-1. CONTENT FIDELITY
  - Sections or items in the reference deliverable absent from Draft HTML v1.
  - Sentences where meaning changed during HTML conversion.
  - PATCH MODE: any text outside marker insertion points that differs from Content Lock v2
    indicates unauthorized modification.

QA-2. MARKER RENDERING
  - Markers (<!-- MASTER LENS -->, <!-- TRENCH -->, etc.) present as plain text.
  - Incorrect component mapping (e.g., TRENCH rendered with ANCHOR style).

QA-3. MATHJAX / LATEX INTEGRITY
  - Equations at risk of rendering failure: unescaped characters, missing delimiters.
  - Incorrect inline vs. display math context.
  - Delimiter conflicts with surrounding HTML syntax.

QA-4. INTERACTIVE ELEMENTS
  - CRITICAL: Self-Test answers visible without user interaction.
  - Accordion open/close malfunction.
  - Navigation anchors pointing to nonexistent IDs.
  - Copy button non-functional.

QA-5. RESPONSIVE & PRINT
  - Table overflow on mobile viewport (≤768px).
  - Navigation not collapsing on mobile.
  - Print mode: backgrounds not suppressed / navigation not hidden.

QA-6. [확인 필요] PRESERVATION
  - [확인 필요] flags in the reference deliverable absent or unformatted (<mark>) in HTML.

QA-7. FIGURE RENDERING  ← v3.3 신설
  - FIGURE_POINTER: source/page/figure number rendered correctly; not embedded as image.
  - FIGURE_SCHEMATIC: matches the brief's elements/exclusions; visually distinct from
    textbook original; <figcaption> present; alt text present.
  - FIGURE_SCHEMATIC: Mermaid blocks pass M1–M6 self-check (valid directive,
    safe node IDs, quoted complex labels); SVG blocks valid.
  - FIGURE_IMAGE_SLOT: image embedded only if Rights ≠ placeholder; otherwise placeholder shown.
  - FIGURE_IMAGE_SLOT (Open-license): attribution text and license info rendered in <figcaption>.
  - No unapproved figures added (every figure traces back to a marker in the reference deliverable).
  - Figure budget not exceeded (P/R/N/I counts match the chapter mode).
  - No reproduction of textbook figure that violates rights status.

QA-8. PATCH MODE SPLICE FIDELITY  ← v3.3.2 신설
  *(Only run when Step 1 deliverable was produced in PATCH MODE; skip otherwise.)*
  - Every marker in the Insertion Map appears exactly once in Draft HTML
    (rendered as its mapped component, not as plain text).
  - Each marker was inserted at the approved anchor location
    (the § + concept card recorded in the Splice Verification Table's "Final location").
  - No surrounding Content Lock v2 text was altered during splicing
    (compare Draft HTML body text against Content Lock v2; only marker-derived components
     should be additions).
  - The Splice Verification Table from Phase 5 is included as a comment block
    in the HTML header.
  - No marker is missing (count of approved markers in Insertion Map = count of
    rendered figure components in HTML).

=== OUTPUT FORMAT ===

## QA Report

| ID | Category | Location in HTML | Severity | Issue description | Fix instruction |
|----|----------|-----------------|----------|------------------|----------------|

Severity: CRITICAL | MAJOR | MINOR
Sort order: CRITICAL first → MAJOR → MINOR.

QA-8 splice failures (missing marker, wrong location, surrounding-text alteration) are
CRITICAL by default — they undermine the integrity guarantee that PATCH MODE was designed to provide.

Append after table:
"Return to HTML workstation session. Paste this report with the following instruction:
'Fix all CRITICAL and MAJOR items from the QA Report below.
Do not introduce new content. Do not modify text content.
Rendering, structure, marker styling, figure rendering, splice fidelity, and interactivity
fixes only.'
[paste QA Report]"

=== HARD CONSTRAINTS ===

- Do not rewrite HTML sections.
- Do not suggest content improvements.
- Do not add content absent from the reference deliverable.
- Do not propose new figures or modify approved figure briefs.
- For PATCH MODE: never resolve splice failures by guessing — escalate to Phase 4C
  for anchor revision.
```

---

## 단계 간 산출물 체계

```
Phase 0    → Scope Lock block (text)
Phase 1    → Step 1 Draft v0.md
Phase 2    → Audit Report v1.md            (T1–T6 포함, T6에 Inspection Method 포함)
Phase 3    → Crucible Report v1.md
Phase 4A   → Content Lock v1.md            (intermediate — integration + compression)
Phase 4B-1 → Content Lock v1.5.md          (intermediate — readability polish)
Phase 4B-2 → Content Lock v2.md            (text-final — pre-figure)
Phase 4C   → Content Lock v2.1.md          ← STEP 1 FINAL
             FULL MODE  : v2 + 마커 inlined된 단일 파일
             PATCH MODE : v2 본체 + Insertion Map (별도 파일)
Phase 5    → Draft HTML v1.html
             PATCH MODE 사용 시: + Splice Verification Table (HTML 헤더에 comment 삽입)
Phase 6    → QA Report v1.md (QA-1 ~ QA-8) + Final HTML
```

---

## Anti-Pattern Reference (위반 감지 체크리스트)

실행 중 아래 상황이 발생하면 해당 Phase를 재실행한다.

| Phase | 위반 신호 | 조치 |
|-------|---------|------|
| 1 | §2 카드 작성 전 Curation Map 없음 | Phase 1 재실행 |
| 1 | Big Idea가 "이 개념은 중요하다" 수준 | Big Idea만 재작성 |
| 1 | Phase 1에서 FIGURE 마커가 삽입됨 | 해당 마커 모두 제거 (Phase 4C 전담) |
| 2 | 새로운 설명이나 비유가 Audit Report에 포함됨 | Gemini에 재지시: "이미 작성한 설명을 모두 삭제하고 감사표만 남겨라" |
| 2 | T5 Coverage Audit에서 OMITTED_PROBLEMATIC 항목이 다수 | Phase 4A에서 ADOPT 여부 재판정 후 반영 |
| 2 | T6에서 Audit이 figure를 직접 설계함 | "inventory only — do not design figures" 재지시 |
| 2 | T6에 Inspection Method 컬럼 누락 | Inspection Method 추가 후 재출력 |
| 2 | T6에서 CAPTION_AND_CONTEXT 또는 FIGURE_CONTENT_NOT_VISIBLE인데 ESSENTIAL로 평가됨 | USEFUL 이하로 다운그레이드 |
| 2-lite | NOT_IN_SOURCE 항목이 발견됨 | Phase 4A에서 해당 항목 DELETE 또는 [교과서 외 해석] 처리 |
| 2-lite | L5에 4개 이상의 figure가 제안됨 | "max 3, ESSENTIAL만" 재지시 |
| 2-lite | L5에 visual inspection 없이 caption만으로 ESSENTIAL 판정된 figure 포함 | 해당 항목 제거 또는 visual inspection 후 재판정 |
| 3 | Crucible Report에 T4 삭제 목록 없음 | Phase 3 재실행 |
| 3 | 삽입 문장이 3문장 이상 | 각 삽입문을 1–2문장으로 재압축 |
| 3 | Crucible이 figure를 제안함 | 해당 항목 무시 (Phase 4C 전담) |
| 4A | Content Lock v1이 Draft v0보다 길다 | Compression Pass 재수행 |
| 4A | Crucible Grade C 항목이 채택됨 | 해당 항목 REJECT 처리 |
| 4A | FIGURE 마커가 Content Lock v1에 삽입됨 | 해당 마커 모두 제거 |
| 4B-1 | 문장의 사실·수식·결론이 바뀜 | 해당 문장만 원문으로 복원 |
| 4B-1 | 새 임상 시나리오나 수치가 추가됨 | 추가 내용 삭제, Pass 1 규칙 재확인 |
| 4B-2 | Content Lock v2가 v1 대비 8% 초과 | 낮은 가치 annotation 제거 후 재점검 |
| 4B-2 | 같은 용어에 gloss가 두 번 이상 달림 | 첫 등장 1회만 남기고 나머지 삭제 |
| 4C | Phase 4C에서 Mermaid/SVG 코드를 직접 작성함 | 모든 코드 제거, brief만 남기고 재실행 (Phase 5 전담) |
| 4C | Figure budget 초과 | 학습 ROI 낮은 figure부터 REJECT |
| 4C | G1–G5 trigger 미충족 figure가 KEEP됨 | 해당 figure REJECT |
| 4C | Image rights = None 인데 Mode I 사용됨 | Mode P로 다운그레이드 |
| 4C | Mode I에 attribution/license 메타데이터 누락 | Open-license 메타데이터 보강 또는 Mode P 다운그레이드 |
| 4C | T6 Inspection Method = CAPTION_AND_CONTEXT 항목을 G5 strong candidate로 채택 | weak candidate로 다운그레이드 또는 visual inspection 보강 |
| 4C | FULL MODE에서 Content Lock v2.1이 v2 대비 5% 초과 | brief 압축 또는 PATCH MODE로 전환 |
| 4C | PATCH MODE인데 본문 문장이 함께 출력됨 | "Insertion Map only" 재지시 |
| 4C | PATCH MODE Insertion Map의 anchor가 Content Lock v2와 verbatim 일치하지 않음 | verbatim 복사 후 재출력 |
| 4C | PATCH MODE anchor가 Content Lock v2 내에서 중복 발생 | anchor를 ≥60자로 확장 또는 §heading에 pin |
| 4C | Strategy Table이 type별로만 정렬되어 reading-order view 누락 | Reading-order view (A) 추가 출력 |
| 5 | 마커가 HTML에 스타일 없이 텍스트로 남음 | 마커별 컴포넌트 매핑 재적용 |
| 5 | Self-Test 정답이 기본 상태에서 노출됨 | JS 아코디언 로직 수정 |
| 5 | [확인 필요]가 HTML에서 사라짐 | `<mark>` 태그 적용 |
| 5 | FIGURE_SCHEMATIC가 교과서 원그림과 시각적으로 동일하게 렌더링됨 | 레이아웃·색상·라벨 재구성 |
| 5 | Mermaid 코드 syntax error로 렌더링 실패 | M1–M6 self-check 재적용; 통과 불가 시 SVG/CSS-card로 fallback |
| 5 | Mermaid 노드 ID에 한글/괄호/슬래시 포함 | 영문/숫자/언더스코어로 교체 후 라벨에 한글 배치 (quoted) |
| 5 | FIGURE_IMAGE_SLOT가 권한 없이 이미지 임베드됨 | placeholder로 교체 |
| 5 | Open-license 이미지인데 attribution 누락 | <figcaption>에 attribution·license·source URL 추가 |
| 5 | PATCH MODE에서 Splice Verification Table 없이 HTML 출력됨 | HTML 폐기, Splice Verification Table 먼저 출력 후 재진행 |
| 5 | PATCH MODE Splice Verification에서 H1–H3 발생인데 HTML 진행됨 | HTML 폐기, Phase 4C로 anchor revision 요청 |
| 5 | PATCH MODE에서 unmatched anchor를 추측으로 삽입 | 해당 markers 제거, Phase 4C로 escalate |
| 6 | QA-7에서 figure budget 초과 발견 | Phase 4C 재실행 후 Phase 5 재컴파일 |
| 6 | QA-8에서 marker 누락 또는 anchor 위치 불일치 | CRITICAL — Phase 5 재실행 (PATCH MODE splice 재수행) |
| 6 | QA-8에서 본문 텍스트 변형 발견 | CRITICAL — Phase 5 splice 로직 점검, 본문 원본 복원 |

---

## 역할 고정표 (전체 워크플로우)

| 도구 | 고정 역할 | 절대 하지 말 것 |
|------|---------|-------------|
| 교과서 html 작업자 | Draft 생성 / HTML 컴파일 / Figure 코드 렌더링 (Phase 5) / Mermaid self-check 적용 / PATCH MODE splice 수행 + Verification Table 출력 | 검증, 리뷰, Figure 선별 판단, anchor 추측 삽입 |
| Gemini Pro | PDF 원문 대조 감사 / Figure inventory (T6, visual inspection 우선) | 설명 개선, 내용 창작, Figure 설계 |
| 박사과정 멘토 | 통찰 추출, 규제 리스크 탐지 | 전체 재작성, HTML 작업, Figure 제안 |
| GPT-5.5 (Phase 4) | 통합 편집 판단, 압축 | 새 리뷰 수행, 내용 창작 |
| GPT-5.5 (Phase 4C) | Figure 선별·예산 적용·brief 작성·PATCH MODE 판정·verbatim unique anchor 작성 | Mermaid/SVG 코드 직접 작성, 텍스트 수정 |
| Claude / GPT-5.5 (Phase 6) | HTML QA / Figure 렌더링 QA / Mermaid syntax 검증 / PATCH MODE splice fidelity 검증 (QA-8) | HTML 재작성, 내용 추가, splice 실패 추측 보정 |

---

*교과서 체화 HTML 워크플로우 Unified v3.3.2*  
*통합 기반: v1.0 Prompt Suite + v2.0 Master's Lens Design + v3.0 Phase Ordering*  
*v3.1 패치: Phase 4B → 4B-1(Readability Polish) + 4B-2(Annotation) 분리 적용*  
*v3.2 패치: Phase 2에 T5 Coverage Audit 추가 / C-Fast → C-Fast-Safe (PROMPT 2-lite 필수 포함)*  
*v3.3 패치: Visual Pedagogy 통합 — Phase 2 T6 Figure Inventory 추가 / Phase 4C Visual Pedagogy Triage 신설 / Phase 5 Figure Rendering Rules 추가 / Phase 6 QA-7 Figure Rendering 추가 / Figure 4유형(P/R/N/I) 및 모드별 budget 정식화*  
*v3.3.1 패치: 5개 minor patch 반영 — (1) Phase 5 OUTPUT SPECIFICATION의 self-contained ↔ CDN 표현 충돌 정정 / (2) Image rights 운영 일관화 (Open-license source 전 단계 동기화 + license·attribution·source URL 메타데이터 정식화) / (3) Phase 4C에 PATCH MODE 옵션 추가 (긴 챕터에서 본문 재출력 회피) / (4) Figure Strategy Table을 reading-order primary view + type-sorted summary 이중 출력으로 변경 / (5) Phase 5에 Mermaid Self-Check (M1–M6 + fallback rule) 추가*  
*v3.3.2 패치: 3개 안정화 minor patch 반영 — (A) Phase 2 T6에 Inspection Method (VISUAL_INSPECTED / CAPTION_AND_CONTEXT / FIGURE_CONTENT_NOT_VISIBLE) 컬럼 추가 + caption-only inference의 ESSENTIAL 등급 금지 + Phase 4C T6 Integration Rule 명문화 / (B) Phase 5 PATCH MODE에 Splice Verification Table (Anchor found / Match count / Inserted / Final location) + HALT 조건 (H1–H3) 추가 / Phase 4C anchor 요건 강화 (verbatim, unique, ≥40자, 충돌 시 ≥60자 또는 §heading pin) / (C) Phase 6에 QA-8 PATCH MODE Splice Fidelity 신설 (marker 누락·위치 불일치·본문 변형 검증 — splice 실패는 CRITICAL 등급)*  
*핵심 설계 원칙: 기능 분리 → Master's Lens First → Accuracy Before Insight → Editorial Lock → Visual Pedagogy Triage → HTML化*  
*Figure 운영 원칙: Pointer 우선 + 선별적 LLM 도식화 + 권한 조건부 Image — 결정은 Step 1, 렌더링은 Step 2 — 그리고 splice는 검증된다*  
*PIPET Lab · Pharmacometrics PhD Program*

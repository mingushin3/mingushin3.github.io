> **v3.5 note:** This version applies an Expression Refinement Patch to PART A only. Scientific content, equations’ meaning, numerical anchors, page tags, source labels, figure marker boundary tags and field keys, compiler markers, section/card structure, code blocks, and PART B guardrails are preserved. The patch normalizes mathematical expressions into MathJax/LaTeX-ready notation, converts remaining general English prose and figure-marker learner-facing descriptions into Korean, applies first-use Korean-English pairing for career-critical terms, and rewrites learner-facing prose in a Korean doctoral-level friendly expert lecture style. No new scientific claims, examples, numbers, page tags, figures, or external references were added.

# XX_html_compile_input_master_v3.2.md
**v3.2 note:** This version applies a **Korean-Dominant Readability Patch** to PART A learner-facing prose. General English prose was converted to Korean where possible, while career-critical pharmacometrics terms are retained as Korean-English paired expressions on first use (e.g., 청소율(clearance), 분포용적(volume of distribution), 그럴듯한 오해(plausible fallacy)). Scientific content, equations, numerical anchors, page tags, source labels, figure markers, compiler markers, section structure, and PART B guardrails are preserved verbatim. No new scientific claims, examples, numbers, page tags, figures, or external references were added. v3.1 note is preserved below for traceability.

**v3.1 note (preserved):** This version applies a Korean Readability Patch to improve learner-facing Korean prose while preserving scientific content, equations, page tags, source labels, figure markers, and Phase 5 HTML-readiness. No new scientific claims, page tags, numerical anchors, figure decisions, or external references were added.

---

# 12_html_compile_input_master_v3.2.md

**세션:** 12 — Effect Compartment · Tolerance/Rebound · Transduction  
**단계(Phase):** 4D Learner-Complete + Mastery-Enriched + HTML-Ready Master Assembler — **V3 Structural-Gap Closure Pass + V3.1 Korean Readability Patch + V3.2 Korean-Dominant Readability Patch**  
**출력 모드:** PATCH MODE with verified figure-marker splicing  
**생성일:** 2026-05-06 (v3 from ver2 base) · 2026-05-07 (v3.1 Korean Readability Patch) · 2026-05-08 (v3.2 Korean-Dominant Readability Patch)  
**Phase 경계:** 이 파일은 Phase 5가 아니다. 이 파일에서 HTML, Mermaid 코드, SVG 코드, 또는 교과서 그림 재현을 생성하지 마라.

**V3.1 change log relative to v3 (Korean Readability Patch):**
1. **Learner Navigation Aid** — All five "How to use this handout" steps, "Before you start" bullets, and "After you finish" bullets translated/rephrased into Korean for learner readability. Headings localized. [READABILITY_PATCH, v3.1]
2. **Card 1 §A** — Sentence ending "steady-state data alone are insufficient" rephrased into Korean to avoid mid-paragraph English drop-off. [READABILITY_PATCH, v3.1]
3. **Card 1 §B** — Noun-stack "표준 simplifying assumption인 ... no partitioning simplification" simplified to verb-centric Korean phrasing. [READABILITY_PATCH, v3.1]
4. **Card 1 §E opening** — "The major pitfall is not PD13. It is..." rephrased into clean Korean opening. [READABILITY_PATCH, v3.1]
5. **Card 1 §E-2** — Line 201 redundancy ("동일하게 ... 동일하게") trimmed. [READABILITY_PATCH, v3.1]
6. **Card 2 §D** — "The decisive question is..." and "Direction-dependent boundary insight from R&T" English-only paragraphs converted to Korean. [READABILITY_PATCH, v3.1]
7. **Card 3 §A, §B, §B-2, §C** — Four English-only paragraphs (tolerance mechanism list, baseline/steady-state derivation, negative-feedback sign rationale, AUC asymmetry explanation) converted to Korean while preserving every equation, value, and page tag. [READABILITY_PATCH, v3.1]
8. **Card 3 §B Eq.3:204 interpretation** — One long Korean sentence split into two for readability. [READABILITY_PATCH, v3.1]
9. **Card 3 §D PD13 reading instruction** — Flow polish for "읽는 방법" sentence. [READABILITY_PATCH, v3.1]
10. **Card 4 §C, §D, §E** — Three English-only sentences (PD35 setup, transit-chain delay logic, equal-τ identifiability) converted to Korean; "identifiability" given a first-use Korean gloss. [READABILITY_PATCH, v3.1]
11. **§5 Pair 1 Critical Blow** — Trailing English clause converted to Korean while preserving the textbook-boundary disclaimer semantics. [READABILITY_PATCH, v3.1]
12. **§6 opener + Signature labels** — Section-opening sentence localized; the four "What you see / Mechanistic meaning / Textbook anchor / Next step" labels of all four signatures dual-labeled (Korean + English in parentheses). Body content of the signatures preserved verbatim. [READABILITY_PATCH, v3.1]
13. **§8 §B heading** — Section heading translated. [READABILITY_PATCH, v3.1]

**V3.1 preservation guarantees (non-negotiable):** All equations, numerical values, page tags, source labels, figure markers (F12-01 through F12-07), HTML compiler markers (`<!-- MASTER LENS -->`, `<!-- ANNOTATION -->`, `<!-- TRENCH -->`, `<!-- CONFUSION -->`, `<!-- SELF-TEST -->`, `<!-- RECAP -->`, `<!-- ANCHOR -->`, `<!-- FIGURE_DECISION ... -->`), Apex Concept tag, Plausible Fallacy block content, Hidden-state echoes, Memory Hooks, Critical Blow, Boss Dilemma, Practice Briefs, all v3 augmentations, and PART B in its entirety preserved unchanged. v3.1 is a *prose-only* Korean readability pass.

**V3 change log relative to ver2:**
1. **Apex standardization** — Card 1 tag changed from `[Apex]` to `[⚡ Apex Concept]`. Apex thesis re-stated explicitly: *observed delay is a diagnostic clue, not a mechanism — the modeler's task is to name the hidden state.* [EXPERT_INFERENCE, v3]
2. **Plausible Fallacy block added to Card 1** — codifies the most seductive Apex-level error: "CCW hysteresis ⇒ effect compartment." Why it fails (same loop generated by 5+ mechanisms), what it produces in practice (dose-scaling failure of $k_{e0}$). [EXPERT_INFERENCE, v3]
3. **Hidden-state naming echoed across all four §2 cards** — each card closes with an explicit one-line declaration: *"Hidden state of this card: [name]"*. This operationalizes the §8 capstone "A delay is not a mechanism. Name the delayed state." across the entire concept body. [EXPERT_INFERENCE, v3]
4. **§5 fully reorganized to 5 pairs with structural Memory Hooks** — every pair now carries a ⚡ 기억 고리 that encodes the *reason* for the distinction (bridge-vs-tank, race-relay, fatigue-vs-recalibration, etc.), not a mere restatement. Critical Blow preserved on Pair 1. Tolerance-vs-Rebound mechanistic content retained in Card 3 §C (AUC asymmetry); §5 now distinguishes tolerance from *adaptation* at the conceptual axis. [EXPERT_INFERENCE, v3]
5. **§7 Boss Dilemma added as Q11** — final Self-Test question becomes a Socratic dilemma between Effect-compartment ($k_{e0}$) and Indirect-response/turnover routes for CCW hysteresis, with the master modeler's trade-off logic (mutual-exclusion defense in regulatory documents) as the answer. The compressed Q8 is retained as a complementary stability-vs-mechanism dilemma. [EXPERT_INFERENCE, v3]
6. **Practice Brief added to each §2 card** — a one-paragraph "if you encounter this situation tomorrow, do exactly this" decision rule, anchored to the textbook diagnostic pattern. [EXPERT_INFERENCE, v3]
7. **§8 capstone strengthened** — "A delay is not a mechanism. Name the delayed state." now explicitly cross-referenced to the four hidden states declared at the end of each §2 card.
8. **PART B updated** — B4 Coverage Matrix, B5 Micro-Patch Register, B6 Mastery Augmentation Register, B8 Phase 5 Compilation Contract, B10 Forbidden-Restoration list, and B11 Certificates all updated to reflect v3 changes. New Final v3 All-Pass Checklist (8 items) appended.

**Ver2 change log preserved (relative to ver1):**
1. Restored full PD13 Model I/II/III parameter comparison table to Card 3 (G&W p.808 Table 13.1).
2. Restored Eq.3:204 governing $t_{1/2,k_{out}}$ as a function of $S(C)$ to Card 3 (G&W p.299).
3. Restored AUC asymmetry note ($AUC_R < AUC_E$) to Card 3 (G&W Fig.3.82).
4. Strengthened Card 3 Big Idea with concrete textbook clinical anchors (nitroglycerin Hat TDS, β-agonist desensitization, opioid tolerance — all G&W §3.11 cited).
5. Restored hysteresis collapse method to Card 2 as the bridge between R&T's diagnostic concept and PD21's $k_{e0}=0.025$ min⁻¹ numerical anchor (R&T pp.245–246; G&W PD21 pp.840–841).
6. Strengthened Wall 3 (moderator sign as homeostasis necessity) with bounded structural-stability commentary in Card 3 (Crucible Grade B, source-bounded).
7. Added §6 Master's Diagnostic Lens with four named GOF signatures (Crucible Grade B catalog, labeled as expert-derived diagnostic mnemonics).
8. Added two restored Self-Test items to §7 — Q9 (acenocoumarol vs phenprocoumon rate-limiting) from R&T Fig.8-11; Q10 (between-patient hysteresis direction variation) from R&T Ch.8 input-rate logic.
9. Updated §8 B failure modes to cross-reference §6 diagnostic catalog.
10. Updated PART B B4/B5/B6/B11 to reflect ver2 restorations.

**Splice verification:** all seven approved figure markers from Content Lock v2.1 remain in their original positions, unchanged. Anchor strings preserved verbatim across both ver2 → v3 → v3.1 transitions.

**Preservation guarantees (non-negotiable):** PD13 Model I/II/III table, hysteresis collapse method (Card 2 §B-2), §6 Master's Diagnostic Lens (4 named signatures), §5 Pair 1 Critical Blow, all G&W and R&T page tags, Eq.3:204, AUC asymmetry note, Card 3 clinical anchors, R&T-anchored Self-Test Q9/Q10. None of these are touched by v3 or v3.1 patches.

---

## PART A — Learner-Facing Complete Handout

## 학습 항법 안내

**이 학습 자료 사용 방법**

1. 먼저 §1을 한 번 훑어 트리아지 지도로 사용하세요. 관찰된 농도-반응(concentration–response) 지연 하나가 서로 다른 세 가지 숨은 상태(hidden state)를 의미할 수 있습니다.
2. §2의 네 장 카드를 순서대로 학습하세요: 링크(Link) → 이력현상 트리아지(hysteresis triage) → 내성/반동(tolerance/rebound) → 신호전달(transduction).
3. 그림 포인터(Figure Pointer)가 나올 때마다 교과서·PDF 원본을 열어 확인하세요. 이 자료는 저작권 보호 교과서 그림을 직접 재현하지 않습니다.
4. §7로 가기 전에 §5를 먼저 보세요. 혼동 쌍(confusion pair)은 자기점검(자기점검(Self-Test)) 전에 가장 흔한 모델 선택 오류를 미리 막기 위해 설계되었습니다.
5. §6은 §5 이후, §7 이전에 보세요. 진단 시그니처(diagnostic-signature) 사전은 혼동 쌍을 정리한 뒤에 가장 유용하며, 자기점검에 필요한 구체적인 진단 어휘를 제공합니다.

**시작하기 전**

- 학습 전 전제: $E_{max}$/Hill 모델, 1구획 기초 PK, 간접반응(indirect response) 모델 용어에 이미 익숙해야 합니다.
- 읽는 내내 이 질문을 눈에 띄는 곳에 두세요: "지연된 숨은 상태(hidden state)는 무엇인가?"

**학습을 마친 뒤**

- $k_{e0}$, $k_{out}$, $k_{tol}$, $k_{off}$를 각각이 지배하는 시계(clock)가 무엇인지로 구분할 수 있어야 합니다.
- 이력현상 방향(hysteresis direction)이 최종 모델 선택 규칙이 아니라 진단 단서인 이유를 설명할 수 있어야 합니다. 또한 *이력현상 접힘 기법(hysteresis collapse method)*이 루프 기하학(loop geometry)을 수치 $k_{e0}$로 바꾸는 원리(PD21)를 설명할 수 있어야 합니다.
- PD13이 내성/반동(tolerance/rebound)에 속하는 이유와 G&W Table 3.10이 링크 모델(Link model) 함정인 이유를 설명할 수 있어야 합니다.
- PD13 Model I/II/III 파라미터 테이블 전체를 읽고, Model II가 단순히 우세하다는 사실을 넘어서 *왜* 우세한지 설명할 수 있어야 합니다.
- PD35가 신호전달 연쇄(transduction chain)를 지지하면서도 $n$이 정확한 생물학적 신호전달 단계 수를 의미하지 않는 이유를 설명할 수 있어야 합니다.
- 네 가지 GOF 진단 시그니처($EC_{50}$ 용량 분기, trough drift, S자형 CWRES 잔차, OFV plateau)와 각각이 함의하는 기계론적 의미를 명명할 수 있어야 합니다.


# §1 — 세션 헤더와 로드맵

**소스(Source):** Gabrielsson & Weiner 5e + Rowland & Tozer 5e  
**챕터 범위:** G&W Ch.3 §3.9/§3.11/§3.13 + PD13/20/21/35; R&T Ch.8  
**핵심 과제:** 농도-반응 사이의 시간 지연을 **분포 지연(distributional delay)**, **시스템 적응(system adaptation)**, 또는 **신호전달 연쇄(transduction cascade)** 중 하나로 분류하는 것입니다.

<!-- MASTER LENS -->
**핵심 통찰:** 혈장(plasma) 농도와 반응(response)은 서로 다른 기전적 이유로 시간상 분리될 수 있습니다. 전문가의 첫 판단은 단순히 "지연 항(delay term)을 하나 붙이는 것"이 아닙니다. 먼저 그 지연이 **약물 분포(drug distribution, $k_{e0}$)**, **시스템 회전/적응(system turnover/adaptation, $k_{out}$/$k_{tol}$)**, 또는 **하류 신호 전파(downstream signal propagation, $n \times \tau$)** 중 어디에 속하는지 정해야 합니다.

### 개념 로드맵

```text
Observed concentration–response time delay
        ↓
Hysteresis direction = first diagnostic clue
        ↓
Mechanism triage
   ├─ Distributional delay       → Effect compartment / Link / ke0
   ├─ System turnover/adaptation → Indirect response / Tolerance / Moderator M
   └─ Signal transduction chain  → Transit compartments / tau / n
        ↓
Discrimination checks
   ├─ linear PK first, then tmax dose-invariance
   ├─ dose-stratified EC50/Emax/n plausibility
   ├─ repeated-dose trough drift / rebound
   └─ onset shape: immediate exponential vs delayed sigmoid
```

<!-- FIGURE_SCHEMATIC -->
Title: F12-01 — PK/PD 시간 지연 뒤의 세 가지 숨은 시계
Visual objective: 관찰된 하나의 농도-반응 지연이 세 가지 지연된 숨은 상태(hidden state)로 분기됨을 보여줍니다: 생체상 농도(biophase concentration) $C_e$, 적응성 반응/조절자 상태(adaptive response/moderator state) $R/M$, 하류 transit 상태 $n \times \tau$.
Core message: 링크(Link), 내성(tolerance), 신호전달(transduction)은 병렬 레이블이 아니라 기전 트리아지(mechanism-triage) 순서로 다루어야 합니다.
Elements to include: 관찰된 농도-반응 시간 지연에서 시작하여 분포 지연(distributional delay) → $C_e$, 시스템 회전/적응(system turnover/adaptation) → $R/M$, 신호전달 연쇄(transduction chain) → $n \times \tau$로 분기되는 흐름.
Elements to exclude: 교과서 그림의 직접 재현, 새 수치, 새 예시, 새 기전 주장.
Caption: 하나의 PK/PD 시간 지연은 효과구획(effect compartment), 조절자/적응 상태, 신호전달 transit chain 중 서로 다른 숨은 시계로 해석될 수 있습니다.
Alt text: 관찰된 농도-반응 지연이 생체상 농도 $C_e$, 조절자 상태 $R/M$, 하류 transit 상태 $n \times \tau$의 세 경로로 분기되는 개념 도식.
<!-- /FIGURE_SCHEMATIC -->

<!-- ANCHOR -->
챕터 순서 자체가 에스컬레이션(escalation) 논리입니다. §3.9는 "분포 지연(distributional delay)인가?"를 묻고, §3.11은 "시스템이 적응하고 있는가?"를 묻습니다. §3.13은 "측정된 반응(measured response)이 하류 cascade 뒤에 나타나는가?"를 묻습니다.

<!-- ANNOTATION --> 따라서 같은 시간 지연(time delay)이라도 숨은 상태(hidden state)가 다르면 모델도 달라집니다. 이 세션의 핵심은 지연의 *크기*가 아니라, **무엇이 지연되는 상태(delayed state)인지**를 명명하는 것입니다.

> **거장의 시각(Mastery Lens) — [EXPERT_INFERENCE | SOURCE-AWARE]**  
> 이 세션에서 "지연(delay)"은 시간 차이 자체가 아니라 *숨은 상태(hidden state)를 찾으라*는 신호입니다. 먼저 지연된 상태의 이름을 붙인 뒤에야 ODE family를 선택할 수 있습니다. 실무 에스컬레이션 순서는 직접반응(direct response) → 효과구획(effect compartment, Link) → 간접반응(indirect response, turnover) → 내성(tolerance, Moderator) → 신호전달(transduction, transit chain)입니다. 이 순서는 §3.7 → §3.9 → §3.11 → §3.13의 G&W 챕터 순서와 동형이며, 새 데이터를 받으면 *어느 단계에서 시작할지*가 첫 5초의 판단이 됩니다.

---

# §2 — 개념 해부 카드

---

## Card 1 — 효과구획 모델(Effect Compartment Model)과 $k_{e0}$ [⚡ Apex Concept]

> **⚡ Apex 명제(thesis) — [EXPERT_INFERENCE, v3]**  
> 관찰된 농도-반응 지연(concentration-response delay)은 진단의 **단서**이지 메커니즘 그 자체가 아닙니다. 모델러의 임무는 그 지연을 만드는 **숨겨진 상태(hidden state)에 이름을 붙이는 것**입니다. Card 1은 그 명명 작업의 첫 후보인 생체상 농도(biophase concentration) $C_e$를 다룹니다. 그러나 동일한 이력현상(hysteresis) 패턴은 이후 카드들의 다른 hidden state로도 만들어질 수 있습니다. 따라서 $C_e$ 가설을 채택하기 전에 반드시 *용량 스케일링(dose-scaling)* 검증과 *루프 접힘(loop-collapse)* 검사를 통과시켜야 합니다.

<!-- MASTER LENS -->
### 핵심 통찰

효과구획 모델(Effect Compartment Model)은 **분포 지연(distributional delay)**을 다루는 표준 링크 모델(link model)입니다. 혈장(plasma) 농도 $C$가 관찰되지 않는 생체상 농도(biophase concentration) $C_e$를 움직이고, $C_e$가 반응(response)을 움직입니다. 실무에서 가장 강한 시그니처는 **용량을 올려도 반응의 $t_{max}$가 동일**하다는 점입니다. 다만 이 판단은 PK가 선형일 때만 유효합니다 [G&W p.264].

### A. 형식적 정의

효과구획(effect compartment)은 혈장(plasma)과 생체상(biophase) 사이의 가상 1차(first-order) 분포 링크입니다 <!-- ANNOTATION -->(← 약물이 작용하는 효과 부위). $C_e$는 직접 측정되지 않습니다. 따라서 반응-시간(response-time) 데이터로부터 역추정해야 합니다. 상승기(rising phase)와 하강기(falling phase) 정보가 모두 필요하므로, 정상상태(steady-state) 데이터만으로는 $k_{e0}$ 추정이 불가능합니다 [G&W p.263].

<!-- FIGURE_POINTER -->
Source: G&W Fig.3.53 (p.263)
Why this matters: F12-02는 $C_e$가 직접 측정되지 않고 반응-시간 데이터로부터 *추론*되는 이유를 시각적으로 이해하도록 돕습니다.
When to use: 효과구획 수식 도출을 읽기 전에, 혈장(plasma) 농도 → 효과구획 농도 $C_e$ → $C_e$ 대비 반응 → 반응-시간으로 이어지는 흐름을 확인할 때 사용하세요.
Learner instruction: 교과서/PDF에서 G&W Fig.3.53 (p.263)을 직접 열고, 각 단계가 관찰 농도인지 추론된 숨은 상태인지 구분하세요. 소스 그림은 본문에 삽입하지 않습니다.
<!-- /FIGURE_POINTER -->

### B. 핵심 방정식

1구획 IV bolus 이후 혈장(plasma) 내 약물량(amount):

$$A_p = D e^{-Kt} \quad \text{[G&W p.264, Eq.3:126]}$$

효과구획 내 약물량:

$$\frac{dA_e}{dt}=k_{1e}A_p-k_{e0}A_e \quad \text{[G&W p.264, Eq.3:127]}$$

적분된 약물량(integrated amount):

$$A_e=\frac{k_{1e}D}{k_{e0}-K}\left(e^{-Kt}-e^{-k_{e0}t}\right) \quad \text{[G&W p.264, Eq.3:128]}$$

표준 단순화 가정인 $k_{1e}=k_{e0}$와 분배 비율 무시($K_p=1$)를 적용하면, 생체상 농도는 다음과 같이 정리됩니다:

$$C_e=\frac{k_{e0}D}{V_c(k_{e0}-K)}\left(e^{-Kt}-e^{-k_{e0}t}\right) \quad \text{[G&W p.265, Eq.3:134]}$$

<!-- ANNOTATION --> 닫힌형(closed-form) 식은 bolus 상황에서 직관을 줍니다. 실제 피팅(fitting)에서는 같은 의미를 더 일반적으로 표현하는 ODE 형태(ODE form)가 중요합니다.

동등한 ODE 형태:

$$\frac{dC_e}{dt}=k_{e0}(C-C_e) \quad \text{[G&W pp.268–269, Eq.3:143]}$$

이 ODE 형태가 유연한 이유는 구동(driving) 역할을 하는 혈장 농도 $C(t)$를 선형 PK, 비선형 PK, 또는 table function으로 넣을 수 있기 때문입니다 [G&W p.269; PD21 pp.840–841].

> **거장의 시각(Mastery Lens) — [EXPERT_INFERENCE | TEXTBOOK_CONSISTENT]**  
> $C_e$는 "관측 농도"가 아니라, 혈장 프로파일(plasma profile)과 반응 곡선(response curve)이 동시에 정합적이도록 강제되는 *숨은 상태(hidden state)*입니다. 따라서 $k_{e0}$ 추정의 품질은 농도 자료만이 아니라 반응(response)의 상승·하강 정보가 얼마나 잘 포착되었는지에 의해 제한됩니다.

### C. 핵심 가정과 경계조건

| 가정 | 유지 | 위반 시 경계 |
|---|---|---|
| $C_e$는 반응-시간(response-time) 데이터로부터 추론됨 | 예 | 상승/하강 반응 데이터가 없으면 → $k_{e0}$와 PD 형상(shape)이 분리되지 않습니다 [G&W p.263]. |
| $t_{max}$ 검사를 위한 선형 PK | 예 | 비선형 PK는 겉보기 peak shift를 만들 수 있습니다. $t_{max}$를 모델 식별자(discriminator)로 쓰기 전에 먼저 노출(exposure) 비례성을 확인하세요 [G&W p.264]. |
| $k_{1e}=k_{e0}$ | 예(수정 적용) | 이는 식별가능성(identifiability) 기반의 단순화 가정이지, 보편적 물리적 등식이 아닙니다 [G&W pp.263, 265]. |
| $K_p=1$ | 단순화 가정으로만 사용 | 분배(partitioning)가 존재하면 정상상태에서도 $C_e$와 $C$가 다를 수 있습니다. 추정된 $EC_{50}$는 혈장 스케일(plasma-scale) 대리(surrogate)값입니다 [G&W pp.263, 265–266]. |
| 반응이 $C_e$를 즉시 추종 | 조건부 | 시스템 회전(system turnover)이나 하류 cascade가 우세하면 간접반응/내성/신호전달(indirect response/tolerance/transduction)로 이동하세요. |

<!-- TRENCH -->
**현장 팁(Trench-Level Tip):** PK 선형성을 먼저 확인하지 않은 상태에서 $t_{max}$ 용량 불변성 검사(dose-invariance test)를 돌리지 마세요. G&W는 same-$t_{max}$ 성질을 "약물 동태가 선형이라는 가정 하에"라고 명시합니다 [G&W p.264].

### D. 보정된 수치 앵커

- **G&W Table 3.9:** 반응 평형 반감기(response equilibration half-lives) — terbutaline FEV-1 7.5 min, theophylline FEV-1 11 min, d-tubocurarine/vecuronium 근이완 4 min, fentanyl spectral edge 6.4 min, QT-quinidine 8 min [G&W p.269].
- **R&T succinylcholine은 별개의 사례입니다:** succinylcholine은 *용량-지속시간(dose-duration)* 예시입니다 — 0.5 mg/kg IV, $T_{50}\approx6$ min, $k\approx0.2\ \text{min}^{-1}$, 그리고 80→20% 반응 감소가 약 22%/min [R&T pp.249–256]. G&W Table 3.9의 $t_{1/2,k_{e0}}=4$ min 사례로 잘못 라벨링하지 마세요.
- **PD20:** 진통제 IV bolus 예시 — $D=45\ \mu\text{g/kg}$, $V=1\ \text{L/kg}$, $K=0.50\ \text{h}^{-1}$, 초기 추정값 $E_{max}\approx3{-}5$, $EC_{50}\approx1.5\ \mu\text{g/L}$, $k_{e0}\approx0.1\ \text{h}^{-1}$. G&W는 데이터셋이 단일 용량만 포함했기 때문에 $EC_{50}$ 정밀도가 낮다고 기술합니다 [G&W pp.836–839].

### E. 그럴듯한 오해 — 회전 데이터에 링크 모델을 끼워 맞추는 경우

여기서 함정은 PD13이 아닙니다. **G&W §3.9.7 Table 3.10**이 진짜 주의 대상입니다. 여기서는 회전으로 생성된 데이터(turnover-generated data)를 효과구획 모델(effect-compartment model)에 끼워 맞춥니다. 그 결과 용량별 피팅(dose-stratified fits)에서 생물학적으로 비현실적인(biologically implausible) $EC_{50}$/$E_{max}$/$n$ 변화가 나타납니다: dose 1 $EC_{50}=0.681$, dose 10 $EC_{50}=4.85$, dose 100 $EC_{50}=0.941$. 약 7배의 $EC_{50}$ 분산은 소스에서 유도된 계산입니다 [G&W p.271]. Fig.3.59는 PD13이 아니라 PD12 데이터를 사용한 것으로 설명됩니다.

**진단명:** *$EC_{50}$ 용량 분기(dose-bifurcation) 패턴*. 용량별 피팅(dose-stratified fit)이 기전적 근거 없이 수용체 민감도(receptor sensitivity)나 용량(capacity)이 용량에 따라 바뀐다는 것을 함의한다면, 링크(Link) 모델이 회전/적응(turnover/adaptation) 오설정(misspecification)을 흡수하고 있을 가능성이 높습니다 [G&W pp.271–272]. 전체 시그니처 사전은 §6 진단 렌즈(Diagnostic Lens)를 참조하세요.

<!-- FIGURE_POINTER -->
Source: G&W Fig.3.59와 Table 3.10 (p.271)
Why this matters: F12-03은 이 함정이 PD13이 아니라 §3.9.7/Table 3.10(PD12 데이터)에 해당함을 정정하고, link 모델 오설정의 시각적·수치적 신호를 확인하기 위함입니다.
When to use: 회전으로 생성된 데이터(turnover-generated data)를 효과구획 모델(effect-compartment model)에 끼워 맞춘 결과를 해석할 때 사용하세요.
Learner instruction: 교과서/PDF에서 G&W Fig.3.59와 Table 3.10 (p.271)을 직접 열고, 동시 피팅(simultaneous fit)과 용량별 피팅(dose-stratified fit)을 비교하면서 용량 의존적 $EC_{50}$/$E_{max}$/$n$ 패턴을 확인하세요. 소스 그림/표는 본문에 삽입하지 않습니다.
<!-- /FIGURE_POINTER -->

> **실패 양식(Failure Mode) — [AUDIT_DERIVED]**  
> 용량별 $EC_{50}$/$E_{max}$/$n$이 크게 흔들릴 때 첫 질문은 "PD가 dose-dependent한가?"가 아닙니다. 먼저 "링크(Link) 모델이 다른 *지연된 시스템 상태(delayed system state)*를 대신 흡수하고 있지는 않은가?"를 물어야 합니다. Table 3.10 함정은 이 질문을 자동화하기 위한 경고 표지입니다.

### E-2. 최상위 수준의 그럴듯한 오해 — "CCW hysteresis ⇒ effect compartment" [EXPERT_INFERENCE, v3]

Section E의 Table 3.10 함정(pitfall)이 *모델을 잘못 끼운 결과*를 보여준다면, 이 E-2는 *모델을 잘못 고른 이유*를 가리킵니다. Apex 수준에서 가장 자주 저질러지는 매혹적인 오류는 다음과 같이 진술됩니다:

> *"반시계방향 이력현상(counterclockwise hysteresis)이 보이면 효과구획(effect compartment) 모델이 답이다. $k_{e0}$를 추가하면 된다."*

**왜 틀렸는가.** 동일한 CCW loop는 최소 다섯 가지 서로 다른 메커니즘에 의해 만들어질 수 있습니다 — (1) 효과구획(effect-compartment) 평형 지연, (2) 회전/간접반응(turnover/indirect-response) 시스템 지연, (3) 조절자 구동 내성(Moderator-driven tolerance)이 아직 발달하기 전 투여 초기 phase, (4) 순차적 신호전달 연쇄(sequential transduction chain)의 상위 단계 지연, (5) 단순한 흡수 율속(absorption rate-limiting), 특히 pro-drug 또는 sustained-release formulation. Loop의 *방향*은 mechanism을 제거하지 않습니다. 모델 family를 좁힐 뿐입니다.

**실무에서 어떻게 드러나는가.** $k_{e0}$를 기계적으로 추가하면 단회투여 데이터(single-dose data)의 표면적 피팅(fit)은 거의 항상 개선됩니다. $k_{e0}$가 추가 자유도이기 때문입니다. 그러나 데이터가 사실은 회전(turnover)이나 신호전달(transduction)이 지배하는 시스템이라면, 다음 세 가지 신호 중 하나가 반드시 나타납니다:

- **용량 스케일링 실패(Dose-scaling failure)**: 용량별로 $k_{e0}$ 추정치가 흔들립니다(예: low dose에서 $0.10\ \text{h}^{-1}$, high dose에서 $0.04\ \text{h}^{-1}$). $k_{e0}$는 분자 수준의 분포 상수이므로 용량에 무관해야 합니다.
- **반복투여 실패(Repeated-dose failure)**: 내성/반동(tolerance/rebound) 패턴(trough drift, second-cycle carry-over)을 $k_{e0}$ 단독으로 설명할 수 없습니다. 조절자(Moderator) $M$ 같은 시스템 메모리(system memory)가 빠져 있기 때문입니다.
- **개시 형상 실패(Onset-shape failure)**: PD35 같은 긴 지연 개시(long delayed-onset) 데이터에서 $k_{e0}$로 피팅하면 초기 phase의 거의 평평한 plateau를 흉내낼 수 없습니다. 1차 링크(first-order link)는 $t=0$에서 즉시 움직이기 시작하기 때문입니다.

**진단 시그니처 이름:** *"용량에 따른 $k_{e0}$ 이동($k_{e0}$ migration under dose)"* (§6 Signature 1과 다른 도메인이지만 같은 가족입니다. 표면적 피팅(fit)이 좋아도 용량별 피팅(dose-stratified fit)이 흔들리면, 모델이 다른 숨은 상태(hidden state)를 흡수하고 있다는 신호입니다.)

> **거장의 시각(Mastery Lens) — [EXPERT_INFERENCE, v3]**  
> CCW hysteresis는 *Card 1을 시작하세요*는 신호이지 *Card 1에서 끝내라*는 신호가 아닙니다. $k_{e0}$ collapse(Card 2 §B-2)가 깨끗하게 일어나고, 용량에 무관한 단일 $k_{e0}$가 회복되며, 반복 투여에서 trough가 reset되어야만 effect compartment 가설이 살아남습니다. 이 세 조건 중 하나라도 깨지면, 다음 카드(turnover, tolerance, transduction)로 escalation해야 합니다.

### F. $k_{e0}$ vs $k_{out}$ vs $k_{off}$

PD21은 *동일한 단위가 동일한 의미를 함의하지 않는 이유*를 보여줍니다. $k_{e0}=0.025$, $k_{out}=0.031$, $k_{off}=0.018\ \text{min}^{-1}$는 수치적으로 유사할 수 있지만, 서로 다른 *시계(clock)*를 가리킵니다: 생체상 평형(biophase equilibration), 시스템 회전(system turnover), 수용체 해리(receptor dissociation) [G&W p.846]. 따라서 단회투여(single-dose) 시간 경과만으로는 여러 메커니즘이 비슷하게 피팅될 수 있습니다. 기전 식별(mechanism discrimination)에는 추가 용량이나 washout 행동 같은 *더 풍부한 실험 설계(richer design)*가 필요합니다 [G&W pp.840–846].

### G. 실무 체화 요약(Practice Brief) — [EXPERT_INFERENCE, v3]

> **상황.** 신약 Phase 1 단회상승용량(single-ascending-dose) study에서 4개 용량(dose; ×1, ×2, ×5, ×10) 모두 CCW hysteresis loop가 관찰되었습니다. 동료 모델러가 "$k_{e0}$ 하나 추가해서 effect compartment로 fit하자"고 제안합니다.
>
> **다음 스프린트 1주 결정 절차.**
> 1. **PK 선형성(PK linearity) 먼저** — 용량 정규화(dose-normalized) $C_{max}$와 $AUC_{0-\infty}$를 4개 용량에 걸쳐 비교하세요. 비례성이 깨지면 hysteresis 진단 자체가 비선형 PK 아티팩트(nonlinear PK artifact)일 수 있습니다 [G&W p.264].
> 2. **$t_{max,response}$ 용량 불변성 검사(dose invariance test)** — 선형 PK가 확인되면, 반응 $t_{max}$가 4개 용량에서 동일한지 검사하세요. 동일하면 effect compartment 가설은 *생존*하고, 용량에 따라 변하면 *기각*됩니다.
> 3. **$k_{e0}$ 루프 접힘(loop-collapse) 시도** — Card 2 §B-2 방법으로 4개 용량의 loop를 단일 농도-반응(concentration-response) 곡선으로 접을 수 있는 $k_{e0}$를 추정하세요. 용량별 $k_{e0}$가 ±20% 안에 들어오면 합격입니다.
> 4. **용량별 $EC_{50}$/$E_{max}$/$n$ 검사** — 동료가 피팅한 모델에서 용량별 PD 파라미터가 흔들리는지 확인하세요. 흔들리면 §3.9.7 Table 3.10 함정(§6 Signature 1)이 발생한 것입니다. Card 3/Card 4로 에스컬레이션하세요.
>
> **금지 사항.** 단일 용량에서 $k_{e0}$가 피팅된다고 채택하지 마세요. 단일 용량 정보는 effect compartment / turnover / transduction을 구분하지 못합니다 [G&W pp.840–846].

> **이 카드의 숨은 상태(Hidden state of this card) — [EXPERT_INFERENCE, v3]:** *효과부위/생체상 농도(effect-site/biophase concentration) $C_e$* — plasma와 effect site 사이의 분포 지연을 표현하는 측정 불가능한 숨은 변수(hidden variable)입니다.



<!-- RECAP -->
효과구획(effect compartment)은 *분포 지연(distributional-delay) 모델*입니다. $C_e$가 $C$ 뒤에 그럴듯하게 지연되고, 선형 PK 하에서 $t_{max}$ 패턴이 일관되며, 용량별 PD 파라미터가 생물학적으로 정합적일 때 사용하세요.

---

## Card 2 — 이력현상(Hysteresis) 방향과 기전 트리아지(Mechanism Triage)

<!-- MASTER LENS -->
### 핵심 통찰

이력현상(hysteresis) 방향은 **첫 진단 단서(first diagnostic clue)**이지 최종 판결이 아닙니다. 반시계방향(counterclockwise) 루프는 대개 반응(response)이 농도보다 늦는다는 뜻입니다. 시계방향(clockwise) 루프는 내성(tolerance), 길항(antagonism), 또는 적응(adaptation)을 시사합니다. 그러나 최종 모델 선택에는 추가 근거가 필요합니다 [R&T pp.234–246; G&W pp.295–296].

### A. 정의

이력현상(hysteresis)이란 농도가 상승할 때와 하강할 때 반응이 서로 다른 경로를 따르는 현상을 말합니다. R&T는 이를 digoxin과 naproxen으로 보여줍니다. Digoxin에서는 IV 투여 후 첫 4시간 동안 혈장(plasma) 농도가 감소하는 *동안* 심장 효과(cardiac effect)는 오히려 증가합니다. Naproxen에서는 경구 500 mg 투여 후 통증 완화(pain relief)에서 반시계방향(counterclockwise) 이력현상이 나타납니다 [R&T pp.234–235].

<!-- FIGURE_POINTER -->
Source: R&T Fig.8-2 (p.235)
Why this matters: F12-04는 이력현상(hysteresis) 방향을 단어 레이블이 아니라 시간순 경로로 시각화하도록 돕습니다.
When to use: 진단 매트릭스를 사용하기 전에, naproxen 루프에서 같은 농도가 서로 다른 반응에 대응하는 지점을 확인할 때 사용하세요.
Learner instruction: 교과서/PDF에서 R&T Fig.8-2 (p.235)를 직접 열고, 루프 위 시간 레이블을 따라가며 농도 상승기와 하강기의 반응 차이를 표시하세요. 소스 그림은 본문에 삽입하지 않습니다.
<!-- /FIGURE_POINTER -->

### B. 진단 매트릭스

| 방향 | 1차 해석 | 검증할 기전 후보 | 필요한 후속 분석 |
|---|---|---|---|
| 반시계방향(Counterclockwise) | 반응이 농도보다 늦음 | 분포 지연, 간접반응(indirect response), 느린 수용체 결합, 동조성 대사체(concordant metabolite) | 용량별 $t_{max}$ 패턴, 상승/하강 반응, 대사체/표적 데이터, 모델 비교 |
| 시계방향(Clockwise) | 반응이 농도보다 일찍 약화 | 내성/탈감작(tolerance/desensitization), 길항성 대사체, 수용체 down-regulation | 반복 투여 패턴, 반동(rebound), 대사체 약리, 회복 동역학 |
| 8자형/혼합 | 경쟁하는 시간 척도 | 분포 지연 + 내성, 희소 샘플링 artifact, 다중 기전 | 모델 확정 전 더 조밀한 샘플링과 기전 기반 실험 설계 |

### B-2. 이력현상 collapse 기법 — 루프 기하학을 수치로 변환하기

R&T는 Card 1과 Card 2를 잇는 강력한 진단 수단을 소개합니다. 시간으로 짝지은 농도-반응 데이터를 효과구획 변환(effect-compartment transformation)하면, 분포 지연이 우세한 기전일 때 반시계방향 루프를 단일 농도-반응 곡선으로 *collapse*시킬 수 있습니다 [R&T pp.245–246, Fig.8-14]. 가장 깨끗한 collapse를 만드는 $k_{e0}$ 값이 곧 분포 지연 추정치입니다.

PD21이 이를 구체화합니다. 길항제 X 실험에서 보고된 $k_{e0}\approx0.025\ \text{min}^{-1}$은 반응 데이터를 $C$ 대신 $C_e$에 투영했을 때 상승부와 하강부 데이터를 하나의 매끄러운 곡선으로 묶어주는 값입니다 [G&W PD21 pp.840–846]. 이는 §2 Card 1 도출에서 나타난 동일한 수치적 시계지만, 여기서는 *그래픽 기반 모델 식별 도구*로 운용됩니다.

> **거장의 시각(Mastery Lens) — [TEXTBOOK_DERIVED | SOURCE-AWARE]**  
> Loop collapse가 깨끗하게 일어나면 분포 지연 가설은 살아남습니다. Collapse가 깔끔하지 않거나 용량마다 서로 다른 $k_{e0}$가 필요하다면, 다른 숨은 상태(turnover 또는 transduction)가 작용 중이라는 신호입니다. 이때 다음 카드(Card 3, Card 4)로 넘어가는 결정이 강제됩니다.

### C. R&T 임상 앵커

- **Digoxin:** IV 투여 후 0–4시간 동안 plasma는 감소하지만 효과는 상승; 심장 조직으로의 분포와 표적 결합이 느리기 때문 [R&T p.234].
- **Naproxen:** 경구 500 mg에서 반시계방향 이력현상; 효과구획 변환으로 루프를 더 명료한 농도-반응 관계로 collapse 가능 [R&T pp.235, 245–246].
- **Warfarin:** 지연된 prothrombin complex 반응은 단순 조직 분포가 아니라 *시스템 회전(system turnover)*을 반영한다 [R&T pp.242–248].
- **Succinylcholine:** 반응 지속 시간이 *용량-지속시간(dose-duration)* 논리를 따른다; 감소/지속 교육에는 유용하나 G&W Table 3.9의 효과구획 반감기와 동일하지 않다 [R&T pp.249–256].

> **범위 마이크로패치(Scope Micro-Patch) — [TEXTBOOK_DERIVED | SCOPE_REQUIRED]**  
> 기전 트리아지를 위해 다음 R&T 지속시간 앵커들은 가시 상태로 유지되어야 한다: naproxen 500 mg 경구는 반시계방향 이력현상과 지연된 peak-response 패턴; warfarin 1.5 mg/kg 경구는 약 48시간 지연된 prothrombin-complex nadir와 1–2일 수준의 시스템 회전; aspirin 650 mg는 짧은 plasma 반감기에도 항혈소판 반응이 수일 지속; succinylcholine 0.5 mg/kg IV는 *용량-지속시간 예시*로 유지되어야 하며 G&W Table 3.9의 4-min $t_{1/2,k_{e0}}$ 사례로 재라벨링하면 안 된다 [Scope Lock; R&T pp.234–256].

<!-- TRENCH -->
**현장 팁(Trench-Level Tip):** 희소 샘플링은 *가짜 8자형*을 만들어낼 수 있습니다. 방향을 해석하기 전에 농도와 반응 모두에서 상승/하강을 포착할 만큼 샘플링 밀도가 충분한지 확인하세요. 그렇지 않으면 루프 기하학은 *기전이 아니라 플롯팅 아티팩트*입니다.

### D. 구조적 해석

시계/반시계 방향은 시간으로 짝지은 농도와 반응의 상평면(phase-plane) 궤적을 기술합니다. 방향은 모델 family를 좁혀주지만, 그것만으로 분포 지연과 회전 지연을 구분하지는 못합니다. 결정적 질문은 이것입니다: **무엇이 지연되고 있는가 — 생체상의 약물 농도($C_e$)인가, 생리학적 반응 시스템($R$)인가, 아니면 하류 cascade의 신호($R_n$)인가?**

R&T가 명시하는 중요한 경계 조건이 있습니다. 약물 주입 속도가 분포 속도나 tolerance 발달 속도를 압도하면 — 예컨대 매우 빠른 IV bolus에서 — 시계방향 루프가 나타날 수 있습니다 [R&T p.236]. 이것은 tolerance가 아니라 *입력 속도 아티팩트(input-rate artifact)*이며, 더 느린 infusion이나 경구 데이터로 재검증하면 사라집니다. 이 아티팩트를 tolerance로 오인하면 불필요한 Moderator 모델 피팅으로 이어집니다.

> **실무 시각(Practice Lens) — [CRUCIBLE_DERIVED]**  
> 이력현상 방향은 모델 family를 줄여주는 *필터*이지 판결문이 아닙니다. *방향 → 선형성/$t_{max}$ → 반복 투여 패턴 → 기전 증거* 순으로 검증해야 루프 기하학을 기전으로 과해석하지 않습니다.

### E. 실무 체화 요약 (Practice Brief) — [EXPERT_INFERENCE, v3]

> **상황.** 새 PK/PD 데이터셋을 받았습니다. 첫 개시 시 plot 한 장은 concentration-response loop입니다. Loop 방향이 무엇이든, *어떤 순서로* 검증을 진행해야 할까요?
>
> **다음 30분 의사결정 트리.**
> 1. **Sampling density 점검** — concentration rise/fall과 response rise/fall이 모두 ≥4 timepoint로 포착됐는지 확인하세요. 그렇지 않으면 figure-eight나 약한 loop는 *artifact 가능성*이 우선입니다.
> 2. **Direction 식별** — CCW면 distribution/turnover/binding 가족, CW면 tolerance/desensitization/antagonist metabolite/input-rate artifact 가족을 후보로 시작합니다.
> 3. **Input-rate artifact 배제(R&T p.236 게이트)** — IV bolus처럼 input rate이 distribution rate을 압도했는지 확인하세요. 그렇다면 CW가 진짜 tolerance를 의미하지 않을 수 있습니다. 더 느린 infusion 또는 oral data로 재검증합니다.
> 4. **$k_{e0}$ loop-collapse 시도 (B-2 방법)** — CCW의 경우, single $k_{e0}$로 loop가 깨끗하게 collapse되는가? 그렇다면 PD21 $k_{e0}=0.025$ $\text{min}^{-1}$ 식으로 numerical estimate 확보. dose에 따라 $k_{e0}$가 흔들리면 다음 카드로 이동.
> 5. **Mechanism evidence 요청** — direction과 collapse만으로는 부족합니다. repeated-dose pattern, metabolite/target data, washout behavior 중 가능한 것을 1건 이상 확보한 뒤 모델 family를 확정하세요.
>
> **금지 사항.** Direction을 보고 즉시 모델 family를 *결정하지 마세요*. Direction은 후보를 줄이는 filter이지 판결문이 아닙니다.

> **이 카드의 숨은 상태(Hidden state of this card) — [EXPERT_INFERENCE, v3]:** *Loop direction이 가리키는 시간 지연의 정체* — 이 카드 자체는 hidden state를 명명하지 않고, *어느 카드의 hidden state가 작동 중인지* 결정하기 위한 진단 게이트입니다. 따라서 Card 2의 결과물은 "biophase $C_e$ / 시스템 response $R$ / Moderator $M$ / transduction transit chain $R_n$" 중 어느 hidden state로 다음 escalation을 할지에 대한 판단입니다.

<!-- RECAP -->
이력현상은 *지도*이지 *목적지*가 아닙니다. 먼저 화살표(루프 방향)를 읽고, $k_{e0}$ collapse를 시도한 뒤, 용량·시간·모델 행동으로 기전을 증명하세요.

---

## Card 3 — 조절자 $M$을 통한 내성·반동(Tolerance/Rebound via Moderator $M$)

<!-- MASTER LENS -->
### 핵심 통찰

내성(tolerance)과 반동(rebound)은 서로 무관한 두 현상이 아닙니다. 조절자 모델(Moderator model)에서 $M$은 반응(response)을 뒤따라 형성되는 지연된 반조절 상태(delayed counter-regulatory state)입니다. 투여(dosing) 중에는 $M$이 response를 줄입니다. 투여가 중단된 뒤에는 $M$이 남아 baseline 너머의 rebound를 만들 수 있습니다 [G&W pp.297–300].

이 추상적 ODE 쌍이 임상에서 나타나는 모습은 매우 구체적입니다. Nitroglycerin 작업자의 "월요일 두통, 일요일 angina" 패턴(G&W Fig.3.71의 hat TDS 일화) — 약물이 반복 노출되면 효과가 줄고(tolerance), 주말 dose holiday에 baseline 너머의 vasoconstrictive rebound가 발생할 수 있다는 임상 신호 — 가 같은 ODE 쌍의 두 phase로 나타납니다 [G&W pp.284–286]. β-agonist의 점진적 desensitization, opioid의 점진적 내성, cocaine의 acute cardiovascular tolerance는 모두 같은 Moderator 구조의 변주입니다 [G&W pp.284–286, 295–296].

### A. 형식적 정의

내성(tolerance)은 노출이 지속되는 동안 반응이 점진적으로 감소하는 현상이고, 반동(rebound)은 약물 투여 중단 후 반응이 기저치를 벗어나 과도하게 움직이는 현상입니다. G&W는 tolerance의 분자 메커니즘으로 수용체 down-regulation/internalization, 신호 전달계 변화, cofactor 고갈, mRNA/단백질 수준 변화, 항체 형성, 효소 유도(enzyme induction)를 열거합니다 [G&W pp.284–286].

### B. 조절자 ODE

핵심 음의 되먹임 모델(core negative-feedback model):

$$\frac{dR}{dt}=k_{in}S(C)-k_{out}M \quad \text{[G&W p.299, Eq.3:193]}$$

$$\frac{dM}{dt}=k_{tol}R-k_{tol}M \quad \text{[G&W p.299, Eq.3:194]}$$

기저 상태(baseline)에서 $S(C)=1$이고 $R_0=k_{in}/k_{out}$이다 [G&W pp.299–300]. 단순형에서 정상 상태(steady state)에 도달하면 $dM/dt=0$이므로 $k_{tol}(R-M)=0$, 즉 $R=M$이 된다 ($k_{tol}\neq0$ 가정 하에).

겉보기 반응 반감기(apparent response half-life)는 자극(stimulus) 의존 표현으로 지배된다 [G&W p.299, Eq.3:204]:

$$t_{1/2,k_{out}} = \frac{\ln 2 \cdot R_0}{k_{in}\cdot S(C)}$$

자극 $S(C)$가 클수록(고용량 또는 강한 약물) response의 *겉보기 반감기*는 짧아진다. 이것이 "왜 고용량에서 tolerance가 더 빠르게 발달하는가"에 대한 수학적 답이다. 단, kinetics 자체가 빨라지는 것이 아니다. 같은 kinetic constant 아래에서 driver인 $S(C)$가 커짐으로써 effective time scale이 단축될 뿐이다.

> **거장의 시각(Mastery Lens) — [CRUCIBLE_DERIVED]**  
> $M$은 약물 구획(drug compartment)이 아니라 *시스템 메모리(system memory)*이다. Rebound가 생기는 이유는 약물이 남아서가 아니라, 약물이 사라진 뒤에도 *반조절 상태(counter-regulatory state)*가 남아 반응 방정식을 계속 밀기 때문이다.

더 일반적인 "조절자 + 반응 수준(moderator + level of response)" 형식은 비선형 $M$ 효과를 도입하고 2차 정상상태 해(second-order steady-state solution)를 만든다 [G&W pp.301–302, Eq.3:205–3:216]. 이 핸드아웃의 핵심 포인트는 대수적 전개 자체가 아니라 그 *결과*다 — 되먹임 강도가 반응 수준과 회복 행동을 바꾼다.

### B-2. 음의 되먹임 부호가 수학적으로 필요한 이유

Eq.3:193에서 moderator $M$은 반응 방정식에 *빼기* 부호로 진입한다 — 자극에 맞서는 방향이다. 만약 부호가 반전되어 $M$이 $S(C)$를 더하는 방향으로 작용했다면, 시스템은 homeostasis로 돌아오는 대신 self-amplify하여 발산했을 것이다. 따라서 음의 부호는 임의의 modeling 선택이 아니라, homeostasis를 만들어야 하는 모든 모델의 *구조적 안정성 요구사항*이다 [G&W pp.297–300; structural commentary, source-bounded].

이 부호 하나가 PD13 Model II의 $AIC=-97.5$ 우위를 만드는 *수학적 정합성*의 출처이다. Model I (no feedback) 또는 Model III (pool/precursor)이 같은 수치적 적합도를 흉내낼 수는 있어도, *반복 dose에서 baseline-traversing rebound와 partial tolerance를 함께* 생성하는 구조적 필연은 음성 피드백 부호로부터만 emerge한다.

### C. AUC 비대칭성 — 내장된 시그니처

Moderator 시스템에서 dosing 중 기저치 상방 반응 면적($AUC_E$)은 일반적으로 투여 중단 후 기저치 하방 rebound 면적($AUC_R$)보다 크다: $AUC_R < AUC_E$ [G&W Fig.3.82, p.298]. 이 비대칭의 구조적 이유는 다음과 같다 — dosing 중에는 drug stimulus와 아직 상승 중인 $M$이 함께 $R$을 밀지만, 투여 중단 후에는 잔류 $M$만이 편차를 만들기 때문이다. 이 비대칭은 진단 체크로 바로 활용된다: 데이터에서 명확한 비대칭이 보이는데 모델이 $AUC_R \approx AUC_E$를 예측한다면, moderator 구조가 잘못 설정된 것이다.

### D. PD13 앵커 — 반복 infusion에서의 내성/반동

PD13은 반복 IV infusion의 정식 사례 연구다. 이 사례는 일반 회전(ordinary turnover), 음의 되먹임 조절자(negative-feedback moderator), pool/precursor 구조를 비교한다 [G&W pp.805–809]. 가장 잘 맞는 것은 Model II, 즉 조절자(moderator) 모델이다. 이는 단순 진술이 아니라 *비교*로 읽어야 한다 — 다음 표가 그 비교다 [G&W p.808, Table 13.1].

| 파라미터 | Model I (no FB) | **Model II (Moderator)** | Model III (pool/precursor) |
|---|---:|---:|---:|
| $k_{in}$ | 21 | **30** | 94 |
| $k_{out}$ | 7.3 | **2.9** | 35 |
| $k_{tol}$ | — | **4.2** | 0.05 |
| $EC_{50}$ / $IC_{50}$ | 390 | **350** | 270 |
| $E_{max}$ / $I_{max}$ | 4.8 | **9.8** | 0.84 |
| n (Hill) | — | **7.4** | — |
| AIC | −39.0 | **−97.5** | −43.5 |
| WRSS | 0.33 | **0.083** | 0.28 |

읽는 방법: AIC/WRSS만 보고 Model II를 채택하면 학습이 절반에 그친다. 핵심 mechanistic 발견은 따로 있다 — *Model II의 $k_{tol}=4.2 > k_{out}=2.9$*, 즉 tolerance 발달(memory build-up) 속도가 response turnover 속도보다 빠르다는 부등식이다 [G&W p.808]. 이 부등식이 단일 infusion 안에서도 tolerance가 가시화되는 이유이고, Model III의 $k_{tol}=0.05$가 임상적으로 비현실적인 이유이다.

핵심 해석은 **trough drift / carry-over**입니다. 반복 infusion에서는 조절자 상태(moderator state)가 완전히 돌아오지 않았기 때문에 두 번째 trough가 첫 번째 trough로 단순히 초기화(reset)되지 않습니다. 이 때문에 내성(tolerance)을 보려면 single-dose 데이터보다 *반복 투여 데이터*가 훨씬 더 정보적입니다 [G&W p.808].

<!-- FIGURE_POINTER -->
Source: G&W Fig.13.1과 Table 13.1 (pp.806–808)
Why this matters: F12-05는 Model II의 우월성을 단순한 AIC/WRSS 수치가 아니라 가시적인 반복 투여 메모리와 연결하기 위함입니다.
When to use: PD13 반복 IV infusion 단락을 읽은 뒤, 두 번째 infusion이 깨끗한 reset인지 또는 숨은 조절자 상태(hidden moderator state)의 carry-over를 보이는지 판단할 때 사용하세요.
Learner instruction: 교과서/PDF에서 G&W Fig.13.1과 Table 13.1 (pp.806–808)을 직접 열고, 반복 infusion 사이의 trough drift와 Model I/II/III 비교 지표를 함께 확인하세요. 소스 그림/표는 본문에 삽입하지 않습니다.
<!-- /FIGURE_POINTER -->

<!-- TRENCH -->
**현장 팁(Trench-Level Tip):** 비슷한 노출(exposure) 하에서 두 번째 trough가 첫 번째 trough와 다르다면, 숨은 조절자 상태(hidden moderator state)를 의심하세요. 직접반응(direct response)이나 순수 link 모델은 그 메모리를 자연스럽게 운반하지 못한다.

### E. 대안적 내성/반동 구조 — 압축 맥락

- **시간 의존 감쇠(Time-dependent attenuation, Colburn–Eldon):** 시간에 따른 potency/capacity의 경험적 평활화; 유용하나 기전성이 약하고 rebound 설명에 취약하다 [G&W pp.291–292].
- **길항성 대사체(Antagonistic metabolite):** 길항(antagonism)은 설명할 수 있으나 추가 구조 없이는 rebound를 다루지 못한다 [G&W pp.292–293].
- **내성 구획 / 반작용 기전(Tolerance compartment / counteracting mechanisms):** 적응 시스템을 위한 대안적 상태변수 형식 [G&W pp.293–295].
- **Pool/precursor 모델 (PD13의 Model III):** 이 데이터셋에서 검증되었으나 조절자 Model II보다 열등하다 [G&W pp.807–808]; 완전 내성만 예측하고 부분 내성은 설명하지 못한다.

### F. 부호가 중요한 이유

조절자 $M$은 $R$을 뒤따르지만, 반응 방정식에서는 *반작용(counteracting) 항*으로 나타난다. 이 음의 되먹임(negative-feedback) 부호 덕분에 시스템은 *자기증폭형(self-amplifying)*이 아니라 *항상성(homeostatic)*으로 작동한다. 여기서 필요한 한 줄짜리 기전 메모리는 다음과 같다: **약이 R을 밀고(drug pushes R), R이 M을 키우고(R builds M), M이 되받아 민다(M pushes back).**

### G. 실무 체화 요약(Practice Brief) — [EXPERT_INFERENCE, v3]

> **상황.** 반복 IV infusion 데이터에서 second-dose trough가 first-dose trough보다 낮다 (약 30% 더 낮음). 동일 dose, 동일 infusion duration. 동료가 "exposure가 누적된 거 아닌가, dose adjustment하자"고 한다.
>
> **다음 1주 결정 절차.**
> 1. **Exposure 누적 배제 먼저** — second-dose의 $C_{trough,plasma}$가 first-dose와 동등한가 (PK가 깨끗한가)? 그렇다면 누적은 PK가 아닌 PD memory의 신호다.
> 2. **AUC asymmetry 검사 (G&W Fig.3.82 게이트)** — second-dose 후 baseline 너머 rebound가 보이는가? Rebound이 dosing 중 response excursion보다 작으면 ($AUC_R < AUC_E$), Moderator 가설 *생존*.
> 3. **Model II vs Model III 비교** — pool/precursor (Model III)는 *complete tolerance*만 만든다. 데이터에 *partial tolerance + rebound*가 같이 나타나면 Model II (Moderator)가 강한 후보. AIC/WRSS 비교 + $k_{tol}/k_{out}$ 부등식 검사.
> 4. **$k_{tol} > k_{out}$ 검사 (PD13 시그니처)** — Model II fit 결과 $k_{tol}=4.2 > k_{out}=2.9$ 같은 부등식이 회복되면, single infusion 안에서도 tolerance가 발달하는 mechanistic 정당성 확보. 그렇지 않으면 Model III 또는 다른 turnover 변형 검토.
> 5. **Sign 검사 (Wall 3 게이트)** — 채택 모델에서 Moderator term이 *반드시 빼는* 부호인지 (Eq.3:193) 확인. 더하기 부호로 fit하면 stability가 깨진다.
>
> **금지 사항.** Trough drift만 보고 즉시 dose adjustment 권고하지 마세요. PK가 깨끗한데 PD trough가 drift하면 *system memory*의 신호이지 *exposure* 문제가 아니다.

> **Hidden state of this card — [EXPERT_INFERENCE, v3]:** *Moderator state $M$* — sustained suppression 또는 stimulation 후 남는 counter-regulatory state. Drug compartment가 아니라 *system memory*; drug가 사라진 뒤에도 남아 rebound를 만든다.

<!-- FIGURE_SCHEMATIC -->
Title: F12-06 — 조절자 메모리 루프 (Moderator Memory Loop)
Visual objective: `Drug stimulus S(C) → Response R → delayed Moderator M ┤ Response R` 구조를 통해 조절자 $M$이 반응 $R$을 뒤따라 형성되고 다시 $R$을 억제하는 지연된 음의 되먹임 루프를 보여줍니다.
Core message: 내성(tolerance)과 반동(rebound)은 별개의 현상이 아니라 동일한 지연된 조절자 메모리 루프의 dosing phase와 withdrawal phase로 이해해야 합니다.
Elements to include: 투여(dosing) phase와 중단(withdrawal) phase 레이블, `Drug stimulus S(C) → Response R → delayed Moderator M ┤ Response R`, 압축 ODE 레이블 `dR/dt = k_in S(C) − k_out M` 및 `dM/dt = k_tol(R − M)`.
Elements to exclude: 새 수치, 새 임상 예시, 교과서 그림의 직접 재현, 조절자 모델 밖의 추가 기전.
Caption: 약물 자극은 반응을 밀고, 반응은 지연된 조절자 $M$을 만들며, 남아 있는 $M$은 투여 중 내성과 중단 후 반동을 생성합니다.
Alt text: 약물 자극 $S(C)$가 반응 $R$을 증가시키고, 반응이 지연된 조절자 $M$을 형성하며, 조절자 $M$이 다시 반응 $R$을 억제하는 음의 되먹임 루프 도식.
<!-- /FIGURE_SCHEMATIC -->

<!-- RECAP -->
내성/반동은 *약력학적 메모리(pharmacodynamic memory) 문제*이다. 시스템이 이전 노출을 기억한다면, 기억을 담을 *상태(state)*를 추가하세요 — 그리고 그 상태의 부호가 발산이 아니라 항상성(homeostasis)을 만들어내는지 확인하세요.

---

## Card 4 — 신호전달 모델 / Transit Chain(Transduction Model / Transit Chain)

<!-- MASTER LENS -->
### 핵심 통찰

신호전달(transduction) 모델은 수용체 활성화(receptor activation)와 관찰된 기능적 반응(observed functional response) 사이의 *연쇄(chain)*를 표현합니다. 반응 개시(onset)가 즉각적인 지수형(immediate exponential)이 아니라 *지연된 시그모이드(delayed sigmoid)*라면, 단일 회전 구획(단일 회전(single turnover) compartment)은 깊이가 부족할 수 있습니다. 이때 *순차적 transit compartments*가 필요합니다 [G&W pp.323–325].

### A. 형식적 정의

신호전달 모델은 수용체-리간드 결합과 관찰된 반응 사이에 *구획 또는 사건의 연쇄*를 사용합니다. 각 transit 단계는 고유한 transit time $\tau$와 그에 대응하는 분획 회전율(fractional turnover rate) $k_{out}=1/\tau$를 갖습니다 [G&W pp.323–325].

<!-- FIGURE_POINTER -->
Source: G&W Fig.3.98과 Fig.3.99 (p.323)
Why this matters: F12-07은 "약물이 부위에 늦게 도달함"과 "측정 반응까지의 신호 전파가 느림"을 구분하도록 돕습니다.
When to use: 신호전달 ODE를 읽기 전에, 수용체-반응(receptor-to-response) 연쇄와 15–20시간 onset 지연 패턴을 확인할 때 사용하세요.
Learner instruction: 교과서/PDF에서 G&W Fig.3.98과 Fig.3.99 (p.323)를 직접 열고, 수용체 활성화에서 관찰 반응까지 이어지는 연쇄와 지연된 onset 형상을 분리해서 표시하세요. 소스 그림은 본문에 삽입하지 않습니다.
<!-- /FIGURE_POINTER -->

### B. 핵심 방정식

수용체-구동 단계(receptor-driving step):

$$\frac{dR_e}{dt}=\frac{1}{\tau}\left(E_0S(C)-R_e\right) \quad \text{[G&W p.911, Eq.35:5]}$$

순차적 transit compartments:

$$\frac{dR_i}{dt}=\frac{1}{\tau}(R_{i-1}-R_i),\quad i=1,2,\ldots,n \quad \text{[G&W p.911, Eq.35:6]}$$

관찰된 반응은 *연쇄의 최종 하류 상태*입니다: $R_{obs}=R_n$.

<!-- ANNOTATION --> 여기서 지연되는 것은 *약물의 이동*이 아니라 *반응 신호(response signal)의 전달*입니다. 따라서 Link 모델의 "약물이 부위에 도달했는가" 질문과 신호전달 모델의 "신호가 측정 지점에 도달했는가" 질문은 *서로 다릅니다*.

### C. PD35 앵커 — onset 지연과 $n$ 선택

PD35는 건강한 남성 지원자에서 3가지 용량 수준(기저 저용량 $C_0=1.05$ nmol/L, 4배, 16배)을 사용한 사례 연구입니다. $K=0.0228\ \text{h}^{-1}$이며 반감기는 약 30시간입니다 [G&W pp.910–914]. 단순한 1-state 간접반응 모델로는 15–20시간의 onset 지연을 재현하기에 역부족이었습니다. 따라서 반응을 설명하려면 *신호전달 연쇄(transduction chain)*가 필요했습니다 [G&W p.323, pp.910–914].

Table 35.1은 모델 비교 시퀀스를 보여줍니다 [G&W p.914]:

| 신호전달 단계 수 | $EC_{50}$ | $E_{max}$ | $\tau$ (h) | $E_0$ | WRSS |
|---:|---:|---:|---:|---:|---:|
| 1 | 0.33 | 7.2 | 20 | 15 | 1319 |
| 2 | 0.34 | 6.0 | 13 | 18 | 789 |
| 3 | 0.35 | 5.4 | 9.8 | 19 | 642 |
| 4 | 0.35 | 5.1 | 7.8 | 20 | 632 |
| 5 | 0.34 | 4.8 | 6.4 | 20 | 682 |

$n=3$은 **기전적 진실(mechanistic truth)**이 아니라 **실용적 충분성(practical sufficiency)**으로 이해해야 합니다. $n=4$는 WRSS를 약간 더 낮추지만, $n=5$에서는 오히려 악화됩니다. 이 패턴은 실제 생물학적 신호전달 단계 수가 아니라 데이터셋의 *정보 수용 한계(information-capacity ceiling)*를 보여줍니다.

또한 $EC_{50}$와 $E_0$가 $n$에 거의 무관(robust)하다는 점, 그리고 $n \times \tau \approx$ 상수라는 trade-off(총 transit time은 거의 일정, 분할 방식만 다름)는 모델 파라미터화에 두 가지 안전감을 동시에 줍니다 [G&W p.914].

> **실무 시각(Practice Lens) — [CRUCIBLE_DERIVED]**  
> PD35의 $n$ 선택은 "진짜 생물학적 단계 수를 맞혔다"는 선언이 아니라, *현재 데이터가 구분 가능한 지연 구조의 해상도를 읽는 작업*입니다. $n=3$ 이후 WRSS 이득이 작고 $n=5$에서 악화되면, 추가 cascade 디테일은 설명력보다 불안정성을 더할 수 있습니다.

<!-- TRENCH -->
**현장 팁(Trench-Level Tip):** "가장 낮은 WRSS"만으로 $n$을 선택하지 마세요. PD35의 $1319\to789\to642\to632\to682$ 시퀀스가 말해주는 것은 분명합니다. 모델은 1단계보다 더 필요하고, $n=3$이면 실용적으로 충분하며, 데이터는 정확한 cascade 깊이를 *해상하지 못합니다*.

### D. 구조적 직관

1개의 1차 지연(first-order delay)은 $t=0$에서 즉시 반응을 시작합니다. Transit chain은 물질이 순차적 상태를 통과해야 하므로 가시적 반응이 나타나기까지의 시간이 지연됩니다. [구조적 비유 — 교과서 외 확장] 수학적으로는 동일한 지수 대기시간(exponential waiting time)들의 합이 *Erlang형 지연*과 닮아 있어, 지연되고 더 가파른 onset 형상을 설명합니다. 이 비유는 학습 보조 수단으로만 유지되며 교과서적 주장이 아닙니다.

### E. 경계 조건

- 각 단계에서 $\tau$를 동일하게 놓는 것은 *식별가능성(identifiability)*을 확보하기 위한 단순화 가정입니다.
- $n$과 $\tau$는 trade-off 관계입니다. 단계 수를 늘리면 단계당 $\tau$를 줄일 수 있고 전체 지연은 비슷하게 유지됩니다.
- 이 연쇄는 *반응 전파(response propagation)*를 기술하지, *약물 분포(drug distribution)*를 기술하지 않습니다. 분포 지연은 상류에 별도로 존재하여 여전히 $C_e$를 요구할 수 있습니다.
- [구현 번역] ODE 소프트웨어에서 이 연쇄는 순차적 1차 ODE로 구현됩니다. 정확한 NONMEM syntax는 이 핸드아웃 범위 밖입니다.

### F. 실무 체화 요약 (Practice Brief) — [EXPERT_INFERENCE, v3]

> **상황.** 새 신호전달 약물의 PD onset이 15–20시간 지연되어 측정됩니다. Plasma kinetics는 $t_{1/2}\approx30$ h입니다. Indirect response($n=1$) fit에서 early phase residual이 *under-then-over-then-under* S-curve를 그립니다.
>
> **다음 2일 결정 절차.**
> 1. **$n=1$ vs $n=2$ vs $n=3$ sequential fit** — 동일한 소프트웨어와 동일한 알고리즘으로 transit chain step 수만 늘리면서 WRSS를 추적하세요. PD35 패턴($1319\to789\to642$)처럼 첫 번째 개선폭이 가장 크면 단일 회전(single turnover)은 *부족*하다는 신호입니다.
> 2. **Plateau 탐지(§6 Signature 4)** — $n=3$, $n=4$, $n=5$까지 escalation하세요. $642\to632\to682$ 같은 plateau-then-worsen 패턴이 나타나면 정보 수용 한계(information-capacity ceiling)에 도달한 것이므로 $n=3$을 채택합니다.
> 3. **$n \times \tau$ 보존 검사** — 채택된 $n$에서 $\tau$가 어떻게 변하는지 확인하세요. PD35처럼 $n \times \tau \approx$ 상수이면 모델은 *총 transit time*을 잡고 있고, 이는 robustness의 신호입니다.
> 4. **$EC_{50}$/$E_{max}$ 강건성(robustness) 검사** — $n$에 따라 $EC_{50}$/$E_{max}$가 흔들리지 않는지 확인하세요. PD35에서 $EC_{50}\approx0.34$, $E_0\approx18{-}20$이 $n$에 거의 무관하다는 점은 transit chain이 *PD parameter를 오염시키지 않고* delay만 흡수했다는 뜻입니다.
> 5. **분포 지연(distribution delay) 동시 가능성 점검** — onset이 매우 길면 transduction과 distribution이 *동시에* 작동할 수 있습니다. Card 1의 $k_{e0}$를 함께 고려하지 않으면 transit chain이 *분포 지연까지 흡수*해버립니다.
>
> **금지 사항.** WRSS 최저값 하나만 보고 $n$을 결정하지 마세요. Parsimony와 plateau가 함께 만족돼야 합니다(PD35: $n=4$가 WRSS 최저지만 $n=3$이 정답).

> **이 카드의 숨은 상태(Hidden state of this card) — [EXPERT_INFERENCE, v3]:** *순차적 transit compartments $R_1, R_2, \ldots, R_n$* — receptor activation에서 measured response까지 신호가 통과하는 중간 단계 pool들입니다. 이 hidden states의 *수와 통과 시간*이 delayed sigmoidal onset shape을 만듭니다.

<!-- RECAP -->
신호전달(transduction)은 Link 모델과 *다른 질문*을 던집니다. "약물이 얼마나 빨리 부위에 도달하는가?"가 아니라, "측정 반응이 나타나기 전에 얼마나 많은 *지연된 생물학적 인계(biological handoffs)*가 일어나는가?"입니다.

---

# §5 — 혼동 쌍 해부

> **V3 재구성 노트 — [EXPERT_INFERENCE, v3]**  
> §5는 *5쌍의 혼동 쌍(confusion pair)*으로 재구성되었으며, 각 쌍은 단순한 재진술이 아니라 *구별이 생기는 이유*를 인코딩하는 구조적 *기억 고리(Memory Hook)*에 앵커됩니다. *치명적 타격(Critical Blow)*은 Pair 1에 유지됩니다. 내성(Tolerance) vs 반동(Rebound) — 동일한 Moderator 방정식의 두 phase — 은 v3에서 *혼동 쌍이 아닙니다*. 그 기전적 관계는 Card 3 §C/§D에 AUC 비대칭 시그니처와 함께 정착됩니다. 대신 v3 §5는 *내성 vs 적응(Tolerance vs Adaptation, Pair 4)*을 묻는데, 이는 더 깊은 개념적 축(시스템 피로 vs 항상성 재보정)을 탐사합니다.

---

<!-- CONFUSION -->
## Pair 1 — $k_{e0}$ vs $k_{out}$ vs $k_{off}$

| 차원 (Dimension) | $k_{e0}$ | $k_{out}$ | $k_{off}$ |
|---|---|---|---|
| 무엇의 시계인가? | Plasma–생체상 평형 | 내인성 반응-시스템 회전 | 수용체-리간드 해리 |
| 대표 모델 | 효과구획(effect compartment) | 간접반응(indirect response)/turnover | 수용체 결합(receptor binding) |
| 단위 | $\text{time}^{-1}$ | $\text{time}^{-1}$ | $\text{time}^{-1}$ |
| 혼동 이유 | 단위가 같고 때로 크기가 비슷 | 유사한 이력현상 형태 | 유사한 single-dose fit |
| PD21 값 | 0.025 $\text{min}^{-1}$ | 0.031 $\text{min}^{-1}$ | 0.018 $\text{min}^{-1}$ [G&W p.846] |
| 식별자(Discriminator) | 선형 PK 하의 $t_{max}$와 loop collapse | 회전/회복 및 반복 투여 행동 | 결합/washout 행동과 표적 정보 |

**⚡ 기억 고리(Memory Hook) — *다리 통행 속도 vs 수조 배수 속도 vs 빗장 풀림 속도*:** [EXPERT_INFERENCE, v3]  
$k_{e0}$는 plasma와 effect site 사이 **다리의 통행 속도**입니다 — 약이 effect site에 도달하는 rate입니다. $k_{out}$은 response pool의 **수조 배수 속도**입니다 — system이 response를 잃는 rate입니다. $k_{off}$는 receptor-ligand의 **빗장 풀림 속도**입니다 — drug-target bond가 해체되는 rate입니다. 세 시계가 같은 단위를 가져도 *대상이 다릅니다* — 다리, 수조, 빗장입니다. PD21에서 세 값이 $0.025/0.031/0.018\ \text{min}^{-1}$로 비슷한 것은 우연이지 동치가 아닙니다. Single-dose data로는 셋을 구분하지 못하므로 dose stratification, repeated dosing, washout 같은 *richer design*이 필요합니다.

**치명적 타격(Critical Blow) — 정정:** G&W §3.9.7은 *회전(turnover) 데이터를 분포/link 모델로 피팅하면 생물학적으로 비현실적인 dose-dependent $EC_{50}$/$E_{max}$/$n$이 생길 수 있다*고 경고합니다 [G&W pp.271–272]. [교과서 외 실무 해석] 모델 정당화 상황에서 이 패턴은 대안 모델 비교와 민감도 분석 요구로 이어집니다. 단, 교과서 자체는 특정 규제 결과를 단언하지 않습니다.

---

<!-- CONFUSION -->
## Pair 2 — 효과구획 모델 vs 회전/간접반응 모델

| 차원 (Dimension) | 효과구획(Effect compartment) | 회전/간접반응(Turnover, indirect response) |
|---|---|---|
| 지연의 출처 | 약물이 effect site로 *느리게 이동* | 약물은 즉시 작용하지만 *반응 변수*가 느리게 변함 |
| 숨은 상태 | 생체상 농도 $C_e$ | $k_{in}/k_{out}$이 지배하는 반응 풀(pool) $R$ |
| 구동 관계식 | $dC_e/dt = k_{e0}(C - C_e)$ | $dR/dt = k_{in}\,S(C) - k_{out}\,R$ |
| 용량 스케일링 검사 | 선형 PK 하 모든 용량에서 동일한 반응 $t_{max}$ [G&W p.264] | $k_{out}$은 고정이고 $S(C)$만 변하므로 반응 $t_{max}$가 용량에 따라 이동 |
| 반복 투여 행동 | 단일 $k_{e0}$로 loop가 collapse됨 | 풀이 reset되지 않으면 메모리 carry-over 가능 |
| 해당 위치 | G&W §3.9, PD20/PD21 | G&W §3.10–3.11, PD13/PD20 |

**⚡ 기억 고리(Memory Hook) — *분포 지연 vs 시스템 지연*:** [EXPERT_INFERENCE, v3]  
Effect compartment는 약이 **distribution 지연** 때문에 effect site에 늦게 도달하는 모델입니다 — plasma와 effect site 사이의 *약물 이동*이 rate-limiting입니다. Turnover는 약이 **생물학적 시스템의 response dynamics** 때문에 효과가 느리게 나타나는 모델입니다 — 약은 즉시 작용하지만 *response pool*이 천천히 바뀝니다. 핵심 진단 질문은 하나입니다: **투여량을 올리면 response peak의 timing이 달라지는가?** 달라지면 effect compartment는 깨집니다(분포 지연은 dose에 무관해야 하기 때문). 달라지지 않으면 turnover의 가능성이 높습니다(turnover는 $S(C)$가 커져도 peak shape 변화가 있지만 *분포 시계*는 영향받지 않음).

---

<!-- CONFUSION -->
## Pair 3 — 반시계방향 vs 시계방향 이력현상

| 차원 (Dimension) | 반시계방향(Counterclockwise) | 시계방향(Clockwise) |
|---|---|---|
| 시각적 의미 | 반응이 농도보다 지연 | 반응이 농도 대비 약화·역전 |
| 같은 농도, 두 방문 | 두 번째(나중) 방문에서 *더 강한* 효과 | 두 번째(나중) 방문에서 *더 약한* 효과 |
| 흔한 기전 | 분포 지연, 시스템 회전, 느린 결합, 동조성 대사체 | 내성, 길항성 대사체, down-regulation, *입력 속도 아티팩트* |
| 예시 | Naproxen/digoxin/warfarin 논리 [R&T pp.234–246] | Cocaine/nitroglycerin 형 내성 논리 [G&W pp.284–296]; 느린 생체상으로의 빠른 IV bolus [R&T p.236] |
| 진단 수순 | 먼저 $k_{e0}$ 기반 loop collapse 시도 | 반복 투여 패턴 확인; 내성 확정 전 입력 속도 아티팩트를 배제 |
| 과독(overread) 시 오류 | 모든 지연을 Link로 처리 | 모든 약화를 단일 내성 기전으로 처리 |
| 올바른 사용 | 첫 진단 단서 | 첫 진단 단서 |

**⚡ 기억 고리(Memory Hook) — *먼저 오는 것이 무엇인가*:** [EXPERT_INFERENCE, v3]  
Counterclockwise hysteresis는 같은 농도에서 **나중 방문에 더 강한 효과**를 보입니다 — 약이 effect site에 늦게 도달하거나(effect compartment), turnover로 response가 누적되기 때문입니다. Clockwise hysteresis는 같은 농도에서 **나중 방문에 더 약한 효과**를 보입니다 — tolerance, acute desensitization, 또는 antagonistic metabolite formation이 후보입니다. 방향은 *"같은 concentration이라는 약속 장소에 두 번 들렀을 때, 두 번째 방문에서 더 환영받는가(CCW) 아니면 덜 환영받는가(CW)"*로 기억하면 됩니다. Loop direction 자체는 mechanism을 결정하지 않습니다. *후보 가족*만 좁힐 뿐입니다.

---

<!-- CONFUSION -->
## Pair 4 — 내성 vs 적응

| 차원 (Dimension) | 내성(Tolerance) | 적응(Adaptation) |
|---|---|---|
| 기저 기전 | 시스템 *피로* — 수용체 down-regulation, 매개체 고갈, cofactor 소진 | 항상성 *재보정* — 생리학적 되먹임이 기저치 회복 |
| 가역성 | 약물 washout 이후에도 지속될 수 있음 (느린 회복) | 약물 노출 종료 시 즉각 역전 |
| 필요한 모델 요소 | 반응에 따라 자라는 숨은 상태 $M$ (조절자, Moderator) | 시스템이 정의한 setpoint를 갖는 음의 되먹임 루프 |
| 시간적 시그니처 | *지속* 노출 동안 점진적 효과 감소 | *지속* 노출 *중*에도 반응이 기저치로 접근 |
| 진단적 분리 | 약물 중단; 느린 역전 또는 반동 관찰 | 약물 중단; 반동 없이 빠른 복귀 관찰 |
| 해당 위치 | G&W §3.11, PD13 (Moderator) [G&W pp.297–300, 805–809] | G&W §3.11 개념적 대비; 다수 생리학적 시스템 |

**⚡ 기억 고리(Memory Hook) — *피로 vs 재보정*:** [EXPERT_INFERENCE, v3]  
Tolerance는 같은 노출에서 시간이 지날수록 효과가 줄어드는 **시스템 피로**입니다 — 약에 대한 반응 capacity가 둔화됩니다. Adaptation은 생리학적 homeostasis로 인해 반응이 기저치로 돌아오려는 **재보정** 과정입니다 — 시스템이 새로운 setpoint로 적응합니다. 두 현상이 겹치는 경우도 있으나, **tolerance는 약 노출이 없어져도 지속될 수 있고, adaptation은 노출 제거 시 바로 역전됩니다**. 이 reversibility 차이가 데이터에서 둘을 구분하는 가장 강한 신호입니다.

---

<!-- CONFUSION -->
## Pair 5 — 단일 효과구획 링크 vs 신호전달 연쇄

| 차원 (Dimension) | 단일 $k_{e0}$ link | Transit chain $n\times\tau$ |
|---|---|---|
| 지연되는 상태 | 생체상의 약물 농도 ($C_e$) | 하류 생물학적 반응 상태들 ($R_1, \ldots, R_n$) |
| ODE 형태 | 1개의 1차 평활화(smoothing) ODE | 순차적 1차 연쇄 ($n$개 방정식) |
| Onset 형상 | 즉각적 평활 접근 ($t=0$에서 최대 기울기) | 지연된 시그모이드형 전파 ($t=0$에서 기울기 0) |
| 핵심 진단 | 선형 PK 하의 동일한 $t_{max}$ | $n=1$이 지연된 onset을 피팅하지 못함; $n=1\to3$에서의 WRSS 급락 |
| 앵커 | G&W §3.9, PD20 | G&W §3.13, PD35 (Table 35.1: $n=1,2,3$에 대해 WRSS $1319\to789\to642$) |

**⚡ 기억 고리(Memory Hook) — *릴레이 경주 vs 단거리 경주*:** [EXPERT_INFERENCE, v3]  
Transduction chain은 신호가 여러 중간 단계(transit compartments)를 거쳐 효과에 도달하는 **릴레이 경주**입니다 — 각 선수(compartment)가 시간을 소모합니다. Single effect compartment는 plasma에서 effect site로 직접 이동하는 **단거리 경주**입니다. 릴레이는 단거리보다 *늦게 시작*하고(첫 선수가 출발선 떠날 때까지 다음 선수는 가만히 있음 — 이것이 zero slope at $t=0$의 정체), relay 선수 수가 많을수록 onset의 sigmoidal sharpness가 커집니다. **Transduction이 필요한 신호는 다음과 같습니다: 용량이 커져도 onset의 *형상*(sigmoidal sharpness)이 유지되며, 단순한 first-order curve로 fit하면 early phase residual이 S-curve로 누적됩니다(§6 Signature 3).**

---

# §6 — 거장의 진단 렌즈(GOF 시그니처 사전)

> **소스 경계 주의(Source-boundary note) — [EXPERT_INFERENCE | TEXTBOOK_DERIVED]**  
> 아래 네 가지 명명된 시그니처는 교과서 앵커와 Crucible-Grade-B 전문가 리뷰에서 도출된 *교육용 기억술(mnemonic)*이다. *패턴*은 교과서 데이터(G&W §3.9.7, PD13, PD35)와 표준 NONMEM 진단 플롯에서 관찰 가능하나, *이름*은 교육적이며 교과서의 직접 명명이 아니다. NONMEM 특정 구현 언어는 의도적으로 최소화되었다.

피팅이 수렴했지만 뭔가 맞지 않는 느낌이 들 때, re-parameterization 전에 데이터를 다음 네 가지 진단 렌즈에 통과시켜라. 각 렌즈의 메시지는 단 하나다: "이 패턴이 보이면, 모델 트리아지의 다음 escalation은 X다."

### Signature 1 — $EC_{50}$ 용량 분기 패턴($EC_{50}$ dose-bifurcation pattern)

- **관찰 패턴:** 모델을 용량별로(individual fits) 피팅하면 $EC_{50}$, $E_{max}$, $n$ 값이 용량군 간에 *기전적 정당화가 없는* 방향이나 크기로 크게 변동한다.
- **기계론적 의미:** Link 모델이 회전/적응(turnover/adaptation) 효과를 강제로 흡수하고 있습니다. 모델링되지 않은 동역학을 보상하기 위해 $EC_{50}$이 *이동(migrate)*합니다.
- **교과서 근거:** G&W §3.9.7 Table 3.10 — dose-stratified $EC_{50}$가 0.681, 4.85, 0.941(약 7배 분산); simultaneous fit에서 체계적 편차가 나타납니다 [G&W p.271].
- **다음 단계:** Link → 간접반응(turnover)으로 이동하세요. *단일 $EC_{50}$이 회복되는지* 검증하면 됩니다.

### Signature 2 — Trough drift / carry-over 패턴

- **관찰 패턴:** 반복 투여 데이터에서, 노출(AUC)이 비슷한데도 *2번째 cycle 종료 시 trough가 1번째 cycle 종료 시 trough와 다릅니다*. 연속된 trough들이 같은 방향으로 깊어지거나 이동합니다.
- **기계론적 의미:** 숨은 상태(hidden state)가 cycle 간에 *메모리를 운반*하고 있습니다. 내성/반동 시스템에서는 다음 투여가 도착하기 전에 조절자 $M$이 완전히 washout되지 않습니다.
- **교과서 근거:** G&W p.808은 PD13의 2번째 투여 trough가 첫 번째와 같지 않음을 명시하며, 이것이 조절자 활성화의 시그니처임을 진술한다 [G&W pp.805–809].
- **다음 단계:** 간접반응 → 조절자(Moderator, Model II)로 이동; AIC/WRSS를 비교하고 $k_{tol}/k_{out}$ 비율을 확인하세요.

### Signature 3 — 지연된 onset / S자형 onset 잔차 패턴

- **관찰 패턴:** 긴 onset 지연을 가진 데이터에 단일 회전(single-turnover, $n=1$) 간접반응 모델을 피팅합니다. 모델은 반응이 *너무 일찍* 상승한다고 예측하지만, 데이터는 더 늦게, 더 급격히 상승합니다. 시간에 따른 잔차가 onset 부근에서 *under-then-over-then-under* 패턴을 형성합니다.
- **기계론적 의미:** 단일 1차 지연으로는 평탄한 초기 phase 뒤에 급격한 상승을 만들어낼 수 없습니다. *순차적 transit compartments*가 필요합니다.
- **교과서 근거:** PD35 Table 35.1 — WRSS가 1319 ($n=1$) → 789 ($n=2$) → 642 ($n=3$)로 감소합니다. $n=1$ vs $n=3$은 약 2배 개선이며, 이는 onset 형상이 단일-회전이 아니라 *cascade에 의해* 생성된다는 신호입니다 [G&W p.914].
- **다음 단계:** 간접반응 → transit chain으로 이동하세요. 절약 원칙(parsimony)에 따라 데이터가 지지하는 $n$을 선택하세요.

### Signature 4 — OFV / WRSS plateau 패턴

- **관찰 패턴:** 구조적 시퀀스를 따라 모델 복잡도를 에스컬레이션하면(예: $n=1,2,3,4,5$ transit compartments; 또는 single → moderator → moderator+M50), OFV 또는 WRSS가 개선된 뒤 *plateau*에 도달하고, 이후 *소폭 악화*를 보입니다.
- **기계론적 의미:** 데이터가 해당 기전에 대해 *정보 수용 한계(information-capacity ceiling)*에 도달했습니다. 추가 파라미터는 더 이상 구조를 포착하지 못하고 *잡음을 흡수*하기 시작합니다.
- **교과서 근거:** PD35 시퀀스 1319 → 789 → 642 → 632 → 682 ($n=1\to5$). 642→632 단계는 작고, 632→682는 *악화*이며, 이는 $n=3$ 또는 $n=4$를 넘는 *과적합(over-parameterization)*을 시사합니다 [G&W p.914].
- **다음 단계:** 에스컬레이션을 *멈추세요*. 절약 원칙이 지지하는 모델을 선택하세요. *데이터가 더 미세한 구조를 해상하지 못한다*는 사실을 문서화하면 됩니다.

> **거장의 시각(Mastery Lens) — [EXPERT_INFERENCE | SOURCE-AWARE]**  
> 네 시그니처는 모델 오설정(misspecification)의 *서로 다른 위치*를 가리킵니다 — Signature 1은 *모델 패밀리 선택*의 오류, Signature 2는 *반복 노출 메모리*의 누락, Signature 3은 *cascade 깊이*의 부족, Signature 4는 *데이터 해상도* 한계입니다. 이 네 패턴을 구분하지 못하면, 잘못된 한 개 패치(예: 재모수화, re-parameterization)로 다른 시그니처를 덮으려 하다가 모델이 오히려 손상됩니다.

---

# §7 — 자기점검: 능동 회상 모듈

<!-- SELF-TEST -->
## Q1 — 회상
효과구획 ODE를 쓰고, $k_{1e}=k_{e0}$이 사용되는 이유를 서술하세요.

**정답:** $dC_e/dt=k_{e0}(C-C_e)$ [G&W pp.268–269]. 이 등식은 보편적 물리 법칙이 아니라 *식별가능성(identifiability) 기반의 표준 단순화*입니다 [G&W pp.263, 265].

---

<!-- SELF-TEST -->
## Q2 — 적용
3개 용량 연구에서 모든 용량의 반응 $t_{max}$가 동일하게 관찰되었다. 즉시 Link 모델을 선택해도 되는가?

**정답:** 아니오. 먼저 *선형 PK*를 검증하세요. Same-$t_{max}$ 성질은 선형 약물 동태 가정 하에서만 진술됩니다 [G&W p.264]. 그 다음 dose-stratified PD 파라미터의 정합성과 모델 적합을 확인하세요.

---

<!-- SELF-TEST -->
## Q3 — 오류 탐지
어떤 초안에 "PD13 Table 3.10이 Link 오설정 하의 $EC_{50}$ 용량 분기를 보여준다"고 적혀 있습니다. 이를 정정하세요.

**정답:** "G&W §3.9.7 Table 3.10 link-model pitfall; Fig.3.59는 PD12 데이터이다"로 정정해야 합니다. PD13은 *반복 IV infusion 내성/반동 모델 비교 사례*입니다 [G&W pp.271, 805–809].

---

<!-- SELF-TEST -->
## Q4 — 기전 트리아지
농도-반응 플롯이 반시계방향입니다. 가능한 기전 3가지와 각각에 대한 *추가 식별자(discriminator)* 1개씩을 나열하세요.

**정답:** 분포 지연 → 선형 PK 하 $t_{max}$ 용량 불변성 검사 + $k_{e0}$ 기반 loop collapse 시도; 회전 지연 → peak shift와 시스템 회복 시간 확인; 느린 결합 → 표적/결합 또는 washout 행동 검사입니다. 대사체 기여는 대사체 농도/약리 데이터가 필요합니다.

---

<!-- SELF-TEST -->
## Q5 — PD13 추론
PD13에서 Model II는 $k_{in}=30$, $k_{out}=2.9$, $k_{tol}=4.2$, $EC_{50}=350$, $E_{max}=9.8$, $n=7.4$, $AIC=-97.5$, $WRSS=0.083$를 보고하며, Model I(되먹임 없음, $AIC=-39.0$)과 Model III(pool, $AIC=-43.5$)보다 우수합니다. AIC를 넘어서, *Model II를 기전적으로 옳은 답으로 만드는 단 하나의 파라미터 관계*는 무엇입니까?

**정답:** $k_{tol}=4.2 > k_{out}=2.9$, 즉 *조절자 발달이 반응 회전보다 빠르다*는 점입니다. 이 부등식은 단일 infusion *내에서도* 내성이 가시화됨을 예측하며, 2번째 cycle에서 carry-over/trough-drift가 관찰되도록 만드는 핵심입니다 [G&W p.808]. Model III의 $k_{tol}=0.05$는 관찰된 패턴에 대해 *생물학적으로 비현실적*입니다.

---

<!-- SELF-TEST -->
## Q6 — PD21 추론
$k_{e0}$, $k_{out}$, $k_{off}$가 모두 $\text{min}^{-1}$ 단위에 비슷한 크기라는 이유만으로 *동일한 의미*라고 결론짓는 것이 안전하지 않은 이유는?

**정답:** 셋은 *서로 다른 물리적/생물학적 시계*를 가리킵니다 — 생체상 평형, 시스템 회전, 수용체 해리. PD21은 유사한 값(0.025, 0.031, 0.018 $\text{min}^{-1}$)을 보고하지만 *서로 다른 기전 모델*을 비교합니다 [G&W p.846].

---

<!-- SELF-TEST -->
## Q7 — PD35 추론
PD35 Table 35.1은 $n=1\to5$에 대해 WRSS $1319\to789\to642\to632\to682$를 보여 줍니다. WRSS가 가장 낮다는 이유만으로 단순히 $n=4$를 선택하면 안 되는 이유는 무엇입니까?

**정답:** $n=4$는 $n=3$ 대비 미미한 개선(642→632)에 그치며, $n=5$에서는 *악화*(632→682)됩니다. 이 패턴은 $n=3$ 부근에서 *실용적 충분성*과 *정보 수용 한계*에 도달했음을 시사합니다. $n=3$은 절약 원칙이 지지하는 선택이며, $n=4$가 "더 좋은" 모델이라고 선언하는 것은 *데이터가 해상하는 것 이상을 주장*하는 것입니다 [G&W p.914].

---

<!-- SELF-TEST -->
## Q8 — 보스 딜레마, 압축형
모델 A는 안정적인 Link 모델이지만 dose-dependent EC50을 만들어낸다. 모델 B는 계산적으로 덜 안정하지만 *생물학적으로 정합적인 단일 EC50*를 유지하고 내성도 포착한다. 어떤 원칙이 선택을 지도하는가?

**정답:** *기전적 타당성(mechanistic validity)이 통계적 편의성에 우선한다*. 기전 없이 dose-dependent 수용체 민감도를 함의하는 모델은 G&W §3.9.7 함정(§6 Signature 1 참조)을 반복한다. 계산적 불안정성은 *기술적 문제*지만, 생물학적으로 비현실적인 파라미터 행동은 *모델 타당성 문제*다.

---

<!-- SELF-TEST -->
## Q9 — 율속 단계 비교 (R&T 앵커)
Acenocoumarol(plasma $t_{1/2} \approx 15$ h)과 phenprocoumon(plasma $t_{1/2} \approx 5$ days)은 동일 표적(응고 인자 합성 억제)에 작용하지만, *기저치 회복 시간*은 약 한 자리수 차이가 납니다. 각 약물의 회복을 율속(rate-limit)하는 단계는 무엇입니까?

**정답:** 회복은 (i) 약물 제거(kinetics)와 (ii) 응고 인자 회전(dynamics) 중 *더 느린 과정*에 의해 율속됩니다 [R&T Ch.8, Fig.8-11]. Acenocoumarol에서는 약물 청소(clearance)가 빠르고 응고 인자 회전($t_{1/2} \approx 1{-}2$ days)이 율속이 되어 회복 시간이 *동역학(dynamics)에 의해 제한*됩니다. Phenprocoumon에서는 약물 청소 자체가 가장 느린 단계($t_{1/2} \approx 5$ days)이므로 회복 시간이 *동태(kinetics)에 의해 제한*됩니다. Warfarin($t_{1/2} \approx 1.5$ days)은 경계에 위치하며, 이는 warfarin 용량 적정이 임상적으로 *민감한* 구조적 이유 중 하나입니다.

---

<!-- SELF-TEST -->
## Q10 — 환자 간 이력현상 변이
동일 약물을 투여받은 두 환자에서 이력현상 루프가 관찰된다. 환자 A의 루프는 반시계방향, 환자 B의 루프는 시계방향이다. 이 세션의 프레임워크에 근거한 두 가지 그럴듯한 설명을 나열하세요.

**정답:** (1) **두 가지 기전이 서로 다른 상대적 우세도로 동시에 작동.** 분포 지연과 내성이 모두 기여할 때, 관찰 가능한 방향은 *관찰 창(observation window) 동안 어느 쪽이 우세한가*에 달려 있다 — 환자 A는 주로 분포 지연 phase에서, 환자 B는 주로 내성 phase에서 샘플링되었을 수 있고, 더 긴 관찰은 양쪽 모두에서 *8자형*을 드러낼 수 있다. (2) **입력 속도 vs 분포 속도 불일치.** R&T는 *약물 입력 속도가 분포 또는 내성 발달 속도보다 빠를 때*에도 시계방향 루프가 나타날 수 있음을 명시한다 [R&T p.236]; 환자 간 경구 흡수 속도, infusion 속도, 또는 first-pass 동태 차이는 *기저 기전이 다르지 않아도* 겉보기 방향을 뒤집을 수 있다.

---

<!-- SELF-TEST -->
## ⚡ Q11 — 보스 딜레마(보스 딜레마(Boss Dilemma)) ★★ [EXPERT_INFERENCE, v3]

반시계방향 이력현상(counterclockwise hysteresis)이 PD 데이터에서 명확히 관찰되었습니다. PK는 선형(linear)이고, 샘플링(sampling)은 충분하며, 3개 용량 수준(dose levels)에서 일관된 CCW direction이 나타났습니다. 이제 두 가지 모델링 경로 사이에서 결정해야 합니다.

- **선택지 A — 효과구획(effect compartment) 모델($k_{e0}$ 추가).** 즉시 구현할 수 있고, 파라미터 집합(parameter set)이 간결합니다($k_{e0}$ 하나 추가). Card 2 §B-2의 hysteresis collapse method가 깨끗하게 작동하면 수치 $k_{e0}$를 확보할 수 있습니다. 단점은 $k_{e0}$가 용량 의존적으로 변하면 모델 정당성이 흔들리고, 반복투여 내성/반동(repeated-dose tolerance/rebound)을 *전혀* 설명하지 못한다는 점입니다.
- **선택지 B — Indirect response / turnover 모델 ($k_{in}, k_{out}, S(C)$).** Mechanism이 production/loss pathway 변화로 정당화되면 생물학적으로 더 의미 있다. Repeated-dose에서 trough drift나 carry-over가 있으면 Moderator로 자연스럽게 확장 가능. 단점: parameter 추정에 *더 넓은* 데이터가 필요 — single-dose만으로는 $k_{in}/k_{out}$이 $C_{baseline}=k_{in}/k_{out}$ 비율로만 결정되어 individually identifiable하지 않다.

**질문:** 각 선택을 *규제 문서*에서 어떻게 방어하는가?

<details>
<summary>정답 공개 — 거장의 Trade-off 논리</summary>

**핵심 통찰: 어느 쪽을 선택하든, 답변의 70%는 "다른 쪽을 *왜 배제했는지*"이다.** 모델 선택은 *증명*이 아니라 *경쟁 가설의 체계적 기각*이다.

**선택지 A (Effect compartment)를 방어하는 경우:**
- (i) Hysteresis collapse method가 3개 용량 수준 모두에서 단일 $k_{e0}$ ±20%로 작동했다는 수치 근거(numerical evidence)를 제시합니다.
- (ii) 반복투여 데이터(repeated-dose data, 가능하면 ≥2 cycles)에서 *no trough drift*, *no rebound*를 보여 turnover/Moderator 가설을 기각합니다.
- (iii) PD13(G&W p.808) 같은 turnover-data 사례와의 *비교 피팅(comparison fit)*을 첨부합니다. 같은 데이터에 turnover 모델을 fit했을 때 $EC_{50}$ 용량 분기(§6 Signature 1) 또는 trough drift(§6 Signature 2)가 나타나지 *않음*을 보여 distribution 가설을 강화합니다.
- (iv) 기전(mechanism)이 그럴듯한지(plausible)를 확인합니다. 약물의 logP, 표적 조직 분배(target tissue partitioning), 관류(perfusion)가 distributional delay 가설과 *일관*되는지에 대한 생물학적 논거(biological argument)를 추가합니다.

**선택지 B (Indirect response)를 방어하는 경우:**
- (i) 약물의 알려진 mechanism이 receptor-mediated production/loss라는 *사전 생물학적 근거(prior biological evidence)*를 제시합니다(literature, in-vitro data, target identity).
- (ii) Effect compartment 모델을 *동일 데이터에* fit한 결과를 첨부하고, dose-stratified $k_{e0}$나 $EC_{50}$/$E_{max}$/$n$ migration(§6 Signature 1) 같은 misspecification 신호를 보여 distribution 가설을 기각합니다.
- (iii) Turnover model의 $k_{in}/k_{out}/S(C)$ identifiability를 위한 *experimental design*을 동반합니다(multiple doses, ideally washout phase 또는 endogenous baseline 측정).
- (iv) Repeated-dose data가 있으면 trough drift 또는 rebound asymmetry($AUC_R<AUC_E$) 관찰을 *명시적 양성 근거(explicit positive evidence)*로 첨부합니다.

**규제 reviewer가 둘 중 어느 하나를 *반드시 묻는* 질문:**  
> "왜 다른 모델이 아닌가?"

준비된 답이 없으면, 어느 모델이든 불충분한 정당화(inadequate justification)로 평가됩니다. 따라서 master modeler의 작업 흐름은 *처음부터 두 모델을 같이 fit하고*, *어느 하나가 명확히 우세한 evidence*를 만든 뒤 *그 evidence를 문서화*하는 것입니다. Fit 결과만 첨부하는 것으로는 충분하지 않습니다.

**현장 단서(Trench-level 단서):** 실제 Phase 1 환경에서 단회투여(single dose)만 있는 경우, A를 *잠정* 선택하되 Phase 1b/2 protocol에서 반복투여 확장(repeated-dose extension)을 미리 *계획*하세요. 그래야 향후 Moderator 가설로 escalate할 수 있는 evidence를 능동적으로 수집할 수 있습니다. 단회투여 effect compartment 모델은 그 자체로 unfalsifiable하기 때문입니다.

</details>
---

<!-- SELF-TEST -->
## Q12 — 제한된 샘플링에서의 메커니즘 판별 ★★ [EXPERT_INFERENCE, v3.4]

> **출처 경계 라벨:** [EXPERT_INFERENCE — mechanism discrimination patch; File 11의 discrimination crisis와 File 12의 hysteresis triage를 연결하기 위한 자기점검 보강]

**시나리오 (시나리오)**

신규 후보 약물의 단회투여(single dose) 임상시험 데이터를 받았습니다. 샘플링 설계는 비용·침습성 제약 때문에 *제한된 샘플링(limited sampling)*만 허용했고, 혈장 농도(plasma concentration)와 효과 표지(effect marker)를 각각 5개 시간점에서만 측정했습니다. 관찰 결과는 다음과 같습니다:

- 혈장 농도는 빠르게 peak에 도달한 뒤 단조 감소한다.
- 효과는 농도 peak보다 *늦게* peak를 보이며, 농도–효과 평면에서 명확한 *반시계방향 이력현상 고리(counterclockwise hysteresis loop)*가 관찰됩니다.
- 두 후보 모델을 동일 데이터에 적합시켰을 때 GOF(goodness-of-fit) 지표가 사실상 동등하다:
  1. **효과구획 모델(effect compartment model)** — $k_{e0}$로 생체상 지연(biophase delay)을 설명합니다.
  2. **간접반응 / 턴오버 모델(indirect response / turnover model)** — $k_{in}/k_{out}$ 또는 반응 풀 턴오버(response pool turnover)로 지연을 설명합니다.

**질문 (질문)**

이 상황에서 단순히 GOF가 비슷하다는 이유로 효과구획 모델을 잠정 선택하면 안 되는 *구조적 이유*는 무엇인가? 그리고 제한된 샘플링(limited sampling) 환경에서 두 메커니즘을 *판별*하기 위해 다음 연구·분석 설계에서 어떤 정보를 추가로 확보해야 하는가?

<details>
<summary>정답 공개 — 메커니즘 판별 논리</summary>

**1. 반시계방향 고리(counterclockwise loop)는 단서이지 결정증거가 아니다.**  
CCW loop는 "효과가 농도보다 늦게 변한다"는 *현상*만을 보여줄 뿐, 그 지연이 *어디에서 오는지*를 결정하지 못합니다. Card 1 §E-2의 그럴듯한 오해(Plausible Fallacy)와 §6 진단 시그니처 사전(Master's Diagnostic Lens)이 가르치는 핵심은 동일합니다. 동일한 CCW 패턴은 효과구획·간접반응·신호전달연쇄(transduction chain) 등 5가지 이상 서로 다른 메커니즘에서 동일하게 생성됩니다.

**2. 효과구획 모델은 주로 *분포·생체상 지연(distributional / biophase delay)*을 설명한다.**  
즉 약물이 측정 가능한 혈장 구획(plasma compartment)에서 작용 부위(effect site)로 도달하는 데 걸리는 시간입니다. 이때 시계는 *약물 시계(drug clock)*이며, $k_{e0}$가 그 속도를 지배합니다(Card 1 hidden state: $C_e$).

**3. 간접반응·턴오버 모델은 *반응 시스템 자체의 생성·소실 속도* 때문에 지연이 생긴다.**  
약물은 plasma에서 즉시 작용하지만, 약물이 변화시키는 것은 내인성 반응 풀의 $k_{in}$ 또는 $k_{out}$입니다. 풀이 새로운 항정상태로 재평형하는 데 걸리는 시간이 *시스템 시계(system clock)*를 만듭니다. 이 경우 $t_{1/2,k_{out}}$이 지연의 본질입니다(Card 3 §B, Eq.3:204 [G&W p.299]).

**4. 제한된 샘플링에서는 모델 식별성(model identifiability)이 구조적으로 약하다.**  
단회투여 + 5개 시간점이라는 데이터 정보량은 두 모델을 *수치적으로* 분리할 만한 자유도를 주지 못합니다. 두 모델 모두 CCW loop와 단조 감소하는 농도 곡선을 *비슷한 RSS·OFV로 재현*할 수 있습니다. GOF만으로 잠그면 사실상 *데이터 식별성이 아니라 prior assumption*에 의해 모델이 결정됩니다. 이는 규제 검토에서 reviewer가 즉시 지적하는 결함입니다.

**5. 판별을 위해 다음 중 일부를 추가로 확보해야 한다.**

- **더 이른 시간점의 효과 샘플링(effect sampling)** — 농도 peak 이전에 효과가 *얼마나 빨리 움직이기 시작하는지*가 두 모델을 분리합니다. 효과구획 모델은 즉각적 출발 후 부드러운 ramp-up을, 턴오버 모델은 *느린 출발(lag-like onset)*을 예측합니다.
- **효과 peak 전후의 촘촘한 샘플링(dense sampling around effect peak)** — peak 시각 자체와 그 형상(둥근 vs 뾰족한)이 hidden state의 차수와 수를 시사합니다.
- **반복용량(repeated dose) 또는 다른 용량 수준(dose level)에서의 $t_{max}$, effect onset, recovery pattern 비교** — 효과구획 모델은 용량 변화에도 onset이 *변하지 않으며*, $k_{e0}$가 dose-independent해야 합니다. 턴오버 모델은 §6 Signature 1($EC_{50}$ 용량 분기), Signature 2(trough drift) 같은 진단 시그니처를 자연스럽게 만듭니다.
- **기저선 회복(baseline recovery)과 반동·내성(rebound / tolerance) 검사** — 효과구획 모델은 *비대칭 회복*을 설명하지 못합니다. $AUC_R < AUC_E$ 같은 비대칭(Card 3 §C, [G&W Fig.3.82])이 보이면 즉시 turnover/Moderator 쪽으로 escalation해야 합니다.
- **독립적 생리학적 지식(independent physiological knowledge)** — 표지 분자(biomarker)의 고유 턴오버 반감기, 생성·소실 속도, receptor 동태 같은 외부 정보입니다. 이 prior가 없으면 데이터만으로 hidden state를 명명할 수 없습니다.

**6. 결론 (결론 원칙)**  
> **Delay는 단순한 시간 지연항이 아니라 숨은 상태(hidden state)를 가리키는 신호이며, 그 숨은 상태가 biophase인지 response turnover인지 구분하는 것이 File 12의 핵심입니다.**

이 원칙은 §8 capstone "지연은 메커니즘이 아닙니다. 지연되는 상태에 이름을 붙이세요(A delay is not a mechanism. Name the delayed state.)"의 직접적 운영 형태입니다. File 11의 discrimination crisis(서로 다른 모델이 동일 데이터를 동등하게 설명하는 위기)와 File 12의 hysteresis triage(loop 방향만으로 잠그는 함정)를 잇는 자기점검입니다.

</details>

**좋은 답안의 최소 구조 (좋은 답안의 최소 구조)**

1. **Loop 방향 → 후보 메커니즘 나열** (CCW = 효과구획 OR 턴오버 OR 신호전달연쇄; 방향만으로는 결정 불가).
2. **GOF만으로 잠금 금지** (제한된 샘플링에서 두 모델은 모델 식별성(identifiability)이 약하므로 RSS·OFV 비교로 잠그면 prior에 의한 결정에 가깝다).
3. **추가 sampling/design으로 판별** (이른 시간점, peak 전후 dense sampling, 반복투여 또는 dose escalation, baseline recovery·rebound 검사, 독립적 생리학적 지식).

---

# §8 — 메타 프레임과 큰 그림

<!-- MASTER LENS -->
## A. PK/PD 지식 그래프에서의 위치

이 세션은 기본 $E_{max}$/Hill/간접반응 모델과 TMDD, PBPK-PD coupling, QSP 같은 고급 통합 PK/PD 시스템 *사이*에 위치합니다. 세 가지 *시계(clock)*의 구분을 가르칩니다:

1. **약물 시계(Drug clock):** 농도가 생체상에 도달하는 속도 — $k_{e0}$.
2. **시스템 시계(System clock):** 생리학적 반응이 생성·소실·적응하는 속도 — $k_{out}$/$k_{tol}$.
3. **신호 시계(Signal clock):** 측정 반응이 나타나기까지의 하류 단계 수 — $n \times \tau$.

## B. 이 세션을 피상적으로 학습했을 때 발생하는 실패 모드

1. **링크 과사용(Link overuse, Signature 1):** turnover가 원인일 때에도 모든 counterclockwise loop를 Link model로 처리합니다. 결과는 G&W Table 3.10처럼 용량 의존적 $EC_{50}$/$E_{max}$/$n$입니다 [G&W p.271].
2. **내성 맹점(Tolerance blindness, Signature 2):** 반복투여 반응을 시스템 메모리가 없는 것처럼 시뮬레이션합니다. 결과적으로 trough drift와 rebound를 놓칩니다 [G&W pp.297–300, 805–809].
3. **연쇄 과소적합(Cascade underfitting, Signature 3):** 지연된 시그모이드형 onset을 단일 turnover state에 강제로 넣습니다. 결과적으로 PD35가 보여주듯 early/late residual pattern과 onset-time misprediction이 발생합니다 [G&W pp.323–325, 910–914].
4. **과모수화(Over-parameterization, Signature 4):** 모델 복잡도를 데이터의 정보 수용 한계(information-capacity ceiling)를 넘어 에스컬레이션하고, 이를 데이터가 실제로 해상하지 못하는 기전의 근거로 오인합니다 [G&W p.914].
5. **단위 수준 혼동(Unit-level confusion):** $k_{e0}$, $k_{out}$, $k_{off}$가 모두 $\text{time}^{-1}$ 단위라는 이유로 같은 종류의 파라미터로 오인됩니다 [G&W p.846].

(교차 참조: §6 거장의 진단 렌즈(Master's Diagnostic Lens)는 이 네 가지 시그니처를 명시적으로 명명합니다.)

## C. 전문가 해석 지점

지속적인 기술은 ODE를 외우는 것이 아닙니다. 핵심은 *피팅 전에* 데이터가 어떤 *숨은 상태(hidden state)*를 요구하는지 *보는 것*입니다: 숨은 **생체상 농도**, 숨은 **적응성 조절자(adaptive moderator)**, 또는 숨은 **신호전달 상태들(transduction states)**. 이 구분이 *수학적으로 수렴했지만 생물학적으로 비현실적인* PK/PD 모델을 막습니다.

> **거장의 시각(Mastery Lens) — [EXPERT_INFERENCE | SOURCE-AWARE]**  
> 세 모델군의 공통점은 모두 "시간 지연"을 설명한다는 점이고, 차이는 *지연되는 상태(delayed state)*의 정체입니다. 좋은 모델러는 rate constant의 *단위*를 먼저 보지 않고, 그 rate constant가 *무엇의 시계인지*를 먼저 묻습니다. 그리고 fit 결과에서 자기 모델이 §6의 네 시그니처 중 어느 하나를 만들어내고 있지는 않은지 — *수렴 이전에* — 검사합니다.

<!-- RECAP -->
Session 12의 최종 원칙: **지연은 메커니즘이 아닙니다. 지연되는 상태에 이름을 붙이세요.** (A delay is not a mechanism. Name the delayed state.)

> **V3 capstone echo — [EXPERT_INFERENCE, v3]**  
> 각 §2 카드의 마지막 줄은 그 카드의 hidden state를 명시한다:
> - **Card 1:** 효과부위/생체상 농도(effect-site/biophase concentration) $C_e$
> - **Card 2:** loop direction이 가리키는 시간 지연의 정체(어느 hidden state로 escalation할지에 대한 진단 게이트)
> - **Card 3:** 조절자 상태(Moderator state) $M$(system memory; drug compartment 아님)
> - **Card 4:** 순차적 transit compartments $R_1, \ldots, R_n$
>
> 새 PK/PD 데이터를 받으면 이 네 hidden states 중 *어느 것이 작동 중인지*를 **수식 쓰기 전에** 결정합니다. ODE 선택은 *결과*이지 *시작*이 아닙니다.

---

---

## PART B — Compiler-Only Appendix

This section is not learner-facing. It exists only to protect Phase 5 rendering fidelity and prevent regression.

### B1. Input Manifest

| File | Role | Authority level | Used for | Notes |
|---|---|---|---|---|
| 12_scope_lock(3).md | scope boundary / locked reference | A0 | Source range, learner, mode, hard exclusions, required numeric anchors, image-rights boundary | Applied; required R&T duration anchors micro-patched into Part A. |
| 012_G_Effect Compartment 내성·Transduction(4).pdf | PDF verification source | A1 | G&W source-page/page-figure verification for §3.9/§3.11/§3.13 and PD13/20/21/35 | Used as verification source only; no textbook image embedded. |
| 012_T_Effect Compartment 내성·Transduction(4).pdf | PDF verification source | A1 | R&T Ch.8 response/time-delay/hysteresis/duration anchors | Used as verification source only; no textbook image embedded. |
| 12_Audit_Report_v1(2).md | audit guardrail | A2 | MUST_FIX/SHOULD_FIX corrections and regression prevention | All mandatory corrections preserved; rejected material not restored. |
| 12_Content Lock v2(4).md | canonical body | A3 | Primary locked text before figure insertion | §1–§8 used as learner-facing body; process curation/adjudication sections moved to Part B. |
| 12_Content Lock v2.1(2).md | figure insertion source | A4 | PATCH MODE figure strategy, figure briefs, insertion map | Seven approved markers spliced exactly once; positions unchanged from ver1. |
| 12_Crucible_Report_v1(1).md | crucible guardrail | A5 | Grade A/approved insight preservation and deletion constraints | Grade A restorations applied; Grade B catalog now in §6 with bounded labeling. |
| 붙여넣은 마크다운(2)(61).md | compiler instruction | A7 | Step 2 HTML Compiler prompt, rendering, navigation, source-page tag, figure rules | Incorporated in B6–B10. |
| 붙여넣은 텍스트 (1)(82).txt | Phase 4D assembly instruction | Controller | Phase 4D output structure, zero-omission gate, augmentation limits | Applied to this master file. |
| 12_step1_draft_v0(2).md | deprecated source | A6 | Regression check; ver2 uses it as restoration-source for textbook-anchored items only | Restorations limited to: PD13 Model I/II/III table, Eq.3:204, AUC asymmetry, Card 3 clinical anchors, hysteresis collapse method, R&T-anchored Self-Test items. |
| S12_phase1_patch memo(2).md | patch memo / locked reference | Auxiliary | Independent classification of Phase 1 issues | Used only for consistency check with Audit. |
| 12_Content Lock v1(2).md | locked reference | Auxiliary | Pre-v2 comparison | Not used as source body; v2 supersedes it. |

### B2. Construction Mode

- Mode detected: **PATCH MODE**.
- Base body: `12_Content Lock v2(4).md`, learner-facing scientific sections §1–§8, plus ver2 textbook-anchored restorations.
- Figure marker source: `12_Content Lock v2.1(2).md` PATCH MODE insertion map. Marker count and positions unchanged from ver1.
- Non-learner process sections from Content Lock v2 (`0. Updated Source Detection`, `0A. Curation Map`, `0B. Adjudication Table`) are not rendered in PART A; their function is preserved here in PART B.
- No HTML, Mermaid code, SVG code, or generated figures are produced in this file.

### B3. Splice Verification Table

| Marker # | Anchor text | Anchor found? | Match count | Inserted? | Final location (§ + card) |
|---|---|---:|---:|---|---|
| F12-01 |    └─ onset shape: immediate exponential vs delayed sigmoid ``` | YES | 1 | YES | §1 Session Header & Roadmap — after Concept roadmap block |
| F12-02 | steady-state data alone are insufficient [G&W p.263]. | YES | 1 | YES | §2 Card 1 — after A. Formal definition |
| F12-03 | the Link model is likely absorbing turnover/adaptation misspecification [G&W pp.271–272]. | YES | 1 | YES | §2 Card 1 — after E. Plausible fallacy paragraph |
| F12-04 | counterclockwise hysteresis가 나타난다 [R&T pp.234–235]. | YES | 1 | YES | §2 Card 2 — after A. Definition |
| F12-05 | 이 때문에 tolerance를 보려면 single-dose data보다 repeated-dose data가 훨씬 더 정보적이다 [G&W p.808]. | YES | 1 | YES | §2 Card 3 — after D. PD13 anchor paragraph |
| F12-06 | **drug pushes R, R builds M, M pushes back**. | YES | 1 | YES | §2 Card 3 — after F. Why the sign matters |
| F12-07 | 각 transit step은 characteristic transit time $\tau$와 corresponding fractional turnover rate | YES | 1 | YES | §2 Card 4 — after A. Formal definition |

**Splice verdict:** PASS. All seven approved markers are present exactly once in PART A. Anchor strings preserved verbatim relative to ver1.

**Note on F12-05 and F12-06 location labels:** in ver2, Card 3 was reorganized so that PD13 anchor moved to subsection D and "Why the sign matters" moved to subsection F. The marker anchor strings themselves are unchanged; only the subsection letter labels differ. Anchor-based splicing remains correct.

**Note on v3.1 Korean Readability Patch:** v3.1 prose-only edits do not touch any of the seven anchor strings. Splice verdict remains PASS unchanged from v3.

### B4. Zero-Omission Coverage Matrix (v3)

| Domain | Required item | Evidence in PART A | Status | Action |
|---|---|---|---|---|
| C1 Scope concepts | Effect Compartment, Hysteresis triage, Tolerance/Rebound, Transduction | §1 roadmap and four §2 cards | PRESENT | No action. |
| C2 G&W required anchors | PD20, PD21, PD13, PD35, Table 3.9 | Card 1 D/F, Card 3 D, Card 4 C | PRESENT | No action. |
| C2 R&T required anchors | digoxin, naproxen, warfarin, aspirin, succinylcholine | Card 2 C plus Scope Micro-Patch | REPAIRED_BY_MICRO_PATCH | Added one bounded scope-required R&T anchor patch. |
| C3 Audit MUST_FIX | PD13/Table 3.10 label correction, k1e=ke0 identifiability, succinylcholine separation, hysteresis non-determinism, implementation/regulatory labeling, transduction analogy control | Cards 1–4 and §5 | PRESENT | No rejected content restored. |
| C4 Audit T5 high-impact omissions | Link pitfall, PD20/PD21/PD35, correct case identity, model-selection caveats | Cards 1, 3, 4, §5, §7 | PRESENT | No unresolved high-impact omission detected. |
| C4-2 Crucible Grade A items | Wall 1, Wall 2, Wall 4, Sparse-sampling figure-eight, T4 deletions | Cards 1–4, §5, §6, §8 | PRESENT | All Grade A items present. |
| C4-3 Crucible Grade B catalog | GOF signature catalog (4 patterns) | §6 Master's Diagnostic Lens | PRESENT_VER2 | Bounded catalog with labeled epistemic status. Preserved unchanged in v3. |
| C4-4 Card 3 PD13 Model I/II/III comparison | Full parameter table with kin, kout, ktol, EC50, Emax, n, AIC, WRSS | Card 3 D | PRESENT_VER2 | Preserved unchanged in v3. |
| C4-5 Card 3 Eq.3:204 governing $t_{1/2,k_{out}}$ | Stimulus-dependent half-life formula | Card 3 B | PRESENT_VER2 | Preserved unchanged in v3. |
| C4-6 Card 3 AUC asymmetry | $AUC_R < AUC_E$ | Card 3 C; (also retained as mechanistic context for absent §5 Tolerance vs Rebound pair) | PRESENT_VER2 | Preserved unchanged in v3. |
| C4-7 Hysteresis collapse method | $k_{e0}$-based loop collapse as PD21 application | Card 2 B-2 | PRESENT_VER2 | Preserved unchanged in v3. |
| C4-8 Card 3 clinical Big Idea anchors | Nitroglycerin Hat TDS, β-agonist desensitization, opioid tolerance | Card 3 Big Idea | PRESENT_VER2 | Preserved unchanged in v3. |
| C4-9 R&T rate-limiting Self-Test | Acenocoumarol vs phenprocoumon | §7 Q9 | PRESENT_VER2 | Preserved unchanged in v3. |
| C4-10 Between-patient hysteresis Self-Test | Direction variation across patients | §7 Q10 | PRESENT_VER2 | Preserved unchanged in v3. |
| C4-11 Wall 3 strengthening | Negative-feedback sign as homeostasis necessity | Card 3 B-2 | PRESENT_VER2 | Preserved unchanged in v3. |
| **C4-12 (v3) Apex standardization** | Card 1 carries [⚡ Apex Concept] tag and explicit Apex thesis | Card 1 header + Apex thesis block | RESTORED_V3 | [Apex] → [⚡ Apex Concept]; thesis re-stated as "delay is a clue, name the hidden state". |
| **C4-13 (v3) Plausible Fallacy block** | "CCW hysteresis ⇒ effect compartment" misconception, why it fails, three diagnostic failure modes | Card 1 §E-2 | RESTORED_V3 | [EXPERT_INFERENCE, v3] tagged; pre-existing §3.9.7 Table 3.10 pitfall (Card 1 §E) preserved separately. |
| **C4-14 (v3) Hidden-state echo across §2 cards** | One-line declaration at end of each card naming the hidden state | Card 1 G, Card 2 E, Card 3 G, Card 4 F | RESTORED_V3 | Cross-referenced from §8 capstone block. |
| **C4-15 (v3) §5 5-pair restructure with Memory Hooks** | Five confusion pairs each with structural Memory Hook (bridge/race/fatigue metaphors); Critical Blow preserved on Pair 1 | §5 Pairs 1–5 | RESTORED_V3 | Tolerance vs Rebound (v2 Pair 3) folded back into Card 3 §C/§D mechanistic context; new Pair 4 (Tolerance vs Adaptation) added; Pair 2 (Effect compartment vs Turnover model, mechanism-level) added. |
| **C4-16 (v3) Boss Dilemma Q11** | Final Self-Test question as Socratic dilemma (Effect compartment vs Indirect response) with regulatory defense logic | §7 Q11 | RESTORED_V3 | Q8 (compressed dilemma) preserved as complementary stability-vs-mechanism question. |
| **C4-17 (v3) Practice Brief in each §2 card** | "Next sprint" decision rule anchored to textbook diagnostic patterns | Card 1 G, Card 2 E, Card 3 G, Card 4 F | RESTORED_V3 | All briefs cite specific page anchors and link to §6 Diagnostic Lens. |
| C5 Figure coverage | F12-01 through F12-07 KEEP markers | All seven markers inserted once | PRESENT | Textbook figures pointer-only; N-mode schematics deferred to Phase 5. Marker positions unchanged across ver1/ver2/v3/v3.1. |
| C6 Page/source tag integrity | Existing source page tags preserved; no [p.확인 필요] deleted | Canonical text preserved; no page-number changes | PRESENT | No fabricated page tags. New v3 content reuses only previously-verified page anchors or carries [EXPERT_INFERENCE, v3] without page tags. v3.1 readability patch did not touch any page tag. |
| C7 Crucible Grade A preservation | Different referents for equal-unit clocks; linear PK before tmax; moderator sign intuition; PD35 information ceiling; sparse sampling warning | Cards 1–4, §5, §8 and mastery notes | PRESENT_EXPANDED | Augmentations visibly labeled. |
| C8 Deprecated draft regression | No unsupported NDA narrative, NONMEM syntax expansion, added case studies, §3.10/§3.12/§3.14 creep | Part A and guardrails | PRESENT | Rejected material remains excluded. |
| C9 Canonical integrity | Content Lock v2 §1–§8 retained with approved markers/micro-patch/augmentations only | Part A | PRESENT | V3 additions are surgical and visibly tagged; locked text not rewritten. v3.1 prose-only edits preserve all locked claims, equations, and tags. |

**Zero-Omission Certificate (v3):** PASS. All ver2-resolved omissions remain resolved (C4-3 through C4-11). All v3 audit-flagged structural gaps closed (C4-12 through C4-17). v3.1 Korean Readability Patch does not affect any C-row status.

### B5. Controlled Micro-Patch Register

| ID | Location | Reason | Patch | Epistemic status |
|---|---|---|---|---|
| MP-01 | Card 2 C R&T clinical anchors | Scope-required R&T anchors not fully explicit in Content Lock v2 | Added one labeled Scope Micro-Patch containing naproxen/warfarin/aspirin/succinylcholine duration anchors | TEXTBOOK_DERIVED / SCOPE_REQUIRED |
| MP-02 (ver2) | Card 3 D — PD13 anchor | Single-line Model II values prevented learner from seeing the comparative basis for Model II's superiority | Restored full PD13 Model I/II/III parameter comparison table from Audit-verified Step 1 Draft v0 anchor (G&W p.808 Table 13.1) | TEXTBOOK_DERIVED |
| MP-03 (ver2) | Card 3 B — moderator ODEs | Stimulus-dependent response half-life relationship missing; learner cannot derive why high-dose tolerance accelerates | Inserted Eq.3:204 $t_{1/2,k_{out}} = \ln 2 \cdot R_0 / (k_{in}\cdot S(C))$ with one-sentence interpretation (G&W p.299 anchor) | TEXTBOOK_DERIVED |
| MP-04 (ver2) | Card 3 C — new subsection | $AUC_R < AUC_E$ asymmetry and its structural reason missing | Added "AUC asymmetry — a built-in signature" paragraph anchored to G&W Fig.3.82 (p.298) | TEXTBOOK_DERIVED |
| MP-05 (ver2) | Card 2 — new subsection B-2 | Hysteresis collapse method (the R&T diagnostic move that yields a numerical $k_{e0}$ via PD21) was unstated, breaking the Card 1 ↔ Card 2 numerical bridge | Added "Hysteresis collapse method" paragraph linking R&T pp.245–246 (Fig.8-14 logic) with G&W PD21 $k_{e0}=0.025$ min⁻¹ | TEXTBOOK_DERIVED |
| MP-06 (ver2) | Card 3 Big Idea | Big Idea was abstract; no concrete clinical hook made the moderator system memorable | Added textbook-cited clinical anchor sentence (nitroglycerin Hat TDS / β-agonist desensitization / opioid tolerance / cocaine acute tolerance) all from G&W §3.11 pp.284–286 and Fig.3.71 | TEXTBOOK_DERIVED |
| MP-07 (ver2) | §7 — new Q9 | R&T Fig.8-11 rate-limiting kinetics-vs-dynamics distinction (acenocoumarol vs phenprocoumon vs warfarin) was lost during compression | Restored as Self-Test Q9 with full R&T-anchored answer | TEXTBOOK_DERIVED |
| MP-08 (ver2) | §7 — new Q10 | R&T Ch.8 input-rate-vs-distribution-rate explanation of clockwise hysteresis was lost; between-patient direction variation has no Self-Test home | Restored as Self-Test Q10 with two textbook-grounded explanations | TEXTBOOK_DERIVED |
| **MP-09 (v3)** | Card 1 header + Apex thesis | `[Apex]` tag was non-standard; Apex thesis was implicit | Replaced `[Apex]` with `[⚡ Apex Concept]`; added explicit Apex thesis block stating "delay is a clue, not a mechanism — name the hidden state" | EXPERT_INFERENCE, v3 |
| **MP-10 (v3)** | Card 1 §E-2 (new) | Apex-level Plausible Fallacy missing; learner could mistake CCW hysteresis for automatic effect-compartment indication | Added "CCW hysteresis ⇒ effect compartment" plausible fallacy block with five alternative mechanisms and three diagnostic failure signatures | EXPERT_INFERENCE, v3 |
| **MP-11 (v3)** | Cards 1–4 final section | Hidden-state naming directive from §8 capstone was not echoed within concept body | Each card closes with explicit "Hidden state of this card: [name]" line | EXPERT_INFERENCE, v3 |
| **MP-12 (v3)** | §5 entire restructure | Memory Hooks were absent (Pair 1) or weak one-liners (Pairs 2/3/4); Tolerance vs Rebound was a *phase* pair, not a *mechanism-confusion* pair | Restructured to 5 pairs each with structural Memory Hook (bridge/race/fatigue/relay/clock metaphors); Critical Blow preserved on Pair 1; Tolerance vs Rebound mechanistic content retained in Card 3 §C/§D | EXPERT_INFERENCE, v3 |
| **MP-13 (v3)** | §7 Q11 (new) | Boss Dilemma as Socratic dilemma was missing; Q8 was compressed but did not echo the master compiler's required Boss Dilemma format with regulatory defense logic | Added Q11 as final §7 question — Effect compartment vs Indirect response model selection with full mutual-exclusion regulatory defense | EXPERT_INFERENCE, v3 |
| **MP-14 (v3)** | Cards 1–4 §G/§E/§G/§F | Practice Briefs (concrete "next sprint" decision rules) were absent | One Practice Brief added per card, each with stepped decision procedure anchored to textbook patterns and §6 Diagnostic Lens | EXPERT_INFERENCE, v3 |
| **MP-15 (v3)** | §8 capstone block | Capstone "A delay is not a mechanism. Name the delayed state." had no explicit cross-reference to the four hidden states declared at card-end | Added capstone echo block listing all four hidden states with their card locations | EXPERT_INFERENCE, v3 |

### B6. Mastery Augmentation Register

| ID | Location | Purpose | Epistemic status |
|---|---|---|---|
| AUG-01 | §1 after hidden-state annotation | Delay means hidden-state triage | EXPERT_INFERENCE | SOURCE-AWARE |
| AUG-02 | Card 1 after ODE form | Ce as inferred hidden state, not measured concentration | EXPERT_INFERENCE | TEXTBOOK_CONSISTENT |
| AUG-03 | Card 1 after F12-03 | Dose-stratified parameter drift as misspecification warning | AUDIT_DERIVED |
| AUG-04 | Card 2 after structural interpretation | Direction filters, but does not decide, mechanism | CRUCIBLE_DERIVED |
| AUG-05 | Card 3 after moderator ODEs | M as system memory rather than drug compartment | CRUCIBLE_DERIVED |
| AUG-06 | Card 4 after PD35 n interpretation | n selection as information-capacity ceiling | CRUCIBLE_DERIVED |
| AUG-07 | §8 after professional skill sentence | Rate constants as different clocks with different referents | EXPERT_INFERENCE | SOURCE-AWARE |
| AUG-08 (ver2) | §1 escalation cascade addition | Direct → link → turnover → tolerance → transduction as ordered model triage; Crucible T1-(b) System Integration | CRUCIBLE_DERIVED |
| AUG-09 (ver2) | Card 2 D input-rate-artifact note | Clockwise loop from rapid input is not tolerance; R&T-grounded boundary insight | TEXTBOOK_DERIVED |
| AUG-10 (ver2) | Card 3 B-2 negative-feedback sign as stability requirement | Crucible Grade B Wall 3, source-bounded; explains why Model II's structural choice has mathematical necessity | CRUCIBLE_DERIVED / SOURCE-BOUNDED |
| AUG-11 (ver2) | §6 entire section — Master's Diagnostic Lens | Crucible Grade B GOF signature catalog (4 named patterns), labeled as expert mnemonics with textbook anchors | CRUCIBLE_DERIVED / EXPERT_INFERENCE |
| AUG-12 (ver2) | §8 B failure-mode list cross-reference to §6 | Failure modes given pattern names so the diagnostic dictionary in §6 connects back to the meta-frame | EXPERT_INFERENCE |
| **AUG-13 (v3)** | Card 1 Apex thesis block | Explicit declaration that hidden-state naming is the modeler's task; CCW hysteresis is *Card 1's starting signal*, not Card 1's verdict | EXPERT_INFERENCE, v3 |
| **AUG-14 (v3)** | Card 1 §E-2 Plausible Fallacy + diagnostic signature naming "$k_{e0}$ migration under dose" | Closes the most seductive Apex-level error before it reaches model-justification documents | EXPERT_INFERENCE, v3 |
| **AUG-15 (v3)** | Cards 1–4 hidden-state echo lines (one per card) | Operationalizes §8 capstone within concept body; gives learner an explicit hook for "what hidden state am I declaring?" | EXPERT_INFERENCE, v3 |
| **AUG-16 (v3)** | §5 five Memory Hooks (bridge/race/fatigue/relay/two-visits) | Encodes the *reason* for each distinction in a structural metaphor; differs from v2's weak one-liners | EXPERT_INFERENCE, v3 |
| **AUG-17 (v3)** | §5 Pair 4 Tolerance vs Adaptation (new pair) | Provides conceptual axis (system fatigue vs homeostatic recalibration) absent in v2 §5; complements Card 3's tolerance/rebound mechanistic content | EXPERT_INFERENCE, v3 |
| **AUG-18 (v3)** | §5 Pair 2 Effect-compartment vs Turnover model (new pair) | Mechanism-level confusion pair not present in v2 §5; explicitly contrasts distribution-delay vs system-delay mental models | EXPERT_INFERENCE, v3 |
| **AUG-19 (v3)** | §7 Q11 Boss Dilemma | Socratic dilemma format with master modeler's regulatory-defense trade-off logic; teaches *mutual-exclusion defense* as the work product, not just model choice | EXPERT_INFERENCE, v3 |
| **AUG-20 (v3)** | Cards 1–4 Practice Briefs | Bridges concept body to next-day workbench decisions with stepped procedures anchored to textbook diagnostics and §6 Signature catalog | EXPERT_INFERENCE, v3 |

**Mastery-Uplift Certificate (v3):** PASS. v3 augmentations are bounded, visibly tagged [EXPERT_INFERENCE, v3], do not introduce new numerical values or new named examples outside Scope/Audit/Crucible, and explicitly preserve all v2 textbook-anchored content. The Plausible Fallacy in §E-2 names a pedagogical signature ("$k_{e0}$ migration under dose") which is family-related to but distinct from §6 Signature 1 (EC50 dose-bifurcation); both are labeled as expert-derived mnemonics. v3.1 Korean Readability Patch does not affect this certificate — no augmentation content was changed; only Korean prose was polished.

### B7. Figure Rendering Queue

| Figure ID | Mode | Phase 5 action | Rendering constraint |
|---|---|---|---|
| F12-01 | N | Generate new Mermaid flowchart | Do not reproduce textbook figures; use only abstract nodes/arrows from Content Lock logic. |
| F12-02 | P | Convert to styled pointer callout | No image; include source page/figure instruction only. |
| F12-03 | P | Convert to styled pointer callout | No image; emphasize "not PD13." |
| F12-04 | P | Convert to styled pointer callout | No image; learner must inspect source loop direction. |
| F12-05 | P | Convert to styled pointer callout | No image; pair Fig.13.1 with Table 13.1. |
| F12-06 | N | Generate new Mermaid or inline SVG feedback loop | Must show negative feedback clearly; avoid stability/Jacobian math. |
| F12-07 | P | Convert to styled pointer callout | No image; pair Fig.3.98 with Fig.3.99. |

### B8. Phase 5 Compilation Contract

- PART A is the only learner-facing body.
- Phase 5 must render PART A without altering scientific content.
- PART B is instruction/guardrail only.
- Do not restore deprecated Step 1 Draft v0 material **except** the items already restored in this ver2 file under MP-02 through MP-08; those restorations have explicit Audit-verified or textbook-anchored basis and are therefore part of PART A.
- Do not add new scientific content, new examples, new source page tags, or new figures beyond what is already present in PART A.
- Do not render PART B as learner content unless explicitly requested.
- If Image rights = None, do not embed copyrighted textbook images. Render pointer figures as text-only callouts.
- §6 Master's Diagnostic Lens must be rendered as a learner-facing section with the source-boundary note prominently visible (the labeled callout at the top of §6).
- Self-Test §7 now contains **11 questions (Q1–Q11)** in v3. All 11 must be rendered as click-to-reveal accordions with answers hidden by default. Q11 (Boss Dilemma) is the **final** question by master compiler convention and must be visually marked with the ⚡ icon and ★★ SR-tag.
- §5 contains **5 confusion pairs** in v3, each carrying a ⚡ 기억 고리 (Memory Hook) block. Pair 1 additionally carries a Critical Blow row. Memory Hooks must render with distinct visual emphasis (recommend the .box.amber class with an inner gold-bordered callout).
- Each §2 card must render its closing **Hidden state** declaration as a visually anchored summary (recommend a small bordered footer card or a decorated final paragraph with a key icon).
- Each §2 card must render its **Practice Brief** as a numbered procedural callout (recommend the .figure-pointer class adapted with a clipboard icon, or a distinct .practice-brief class).
- Card 1 carries the **[⚡ Apex Concept]** tag — render with prominent emphasis (gold/amber border-left, larger font for the ⚡ symbol).
- v3.1 Korean Readability Patch dual labels in §6 (e.g., "관찰 패턴 (What you see):") render as a single bold inline label — preserve both Korean and parenthetical English; do not strip either.

### B9. Marker-to-Component and Rendering Rules

The following compiler prompt is binding for Phase 5. It is reproduced verbatim from the attached Step 2 HTML Compiler prompt, with this file's PART A as the input body.

~~~~text
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
Navigation: sticky left sidebar, anchor jump per § section (now including §6)
Accordion : Self-Test answers hidden by default; revealed on user click — applies to all 10 Q&A
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
- Every major section heading (§1, §2, §3...) must receive a stable id, including the new §6.
- Every concept card inside §2 must also receive a stable id when possible.
- Each of the four §6 GOF signatures should also receive a sub-id for navigation.
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
- §6 Diagnostic Lens with its four signatures should be reachable individually.
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

Add for §6 GOF signature dictionary:
  .signature-card {
    border-left: 4px solid var(--amber);
    background: rgba(245, 158, 11, 0.04);
    padding: 1em 1.2em;
    margin: 1em 0;
    border-radius: var(--radius-sm);
  }
  .signature-card h3 {
    color: var(--amber);
    margin-top: 0;
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
~~~~

### B10. Forbidden-Restoration Guardrails

Do **not** restore any of the following into the learner-facing HTML:

- §3.10 Dose-Response-Time Models, §3.12 Receptor Occupancy Theory, or §3.14 Synergistic Effects as expanded content.
- "Hysteresis direction determines the model" as a deterministic rule.
- "$k_{1e}=k_{e0}$ is physically mandatory" or mass-conservation overclaims.
- The error that G&W Table 3.10 / Fig.3.59 is PD13.
- The error that succinylcholine is the G&W Table 3.9 4-min $t_{1/2,k_{e0}}$ example.
- NDA Deficiency Letter, FDA reviewer, ICH E9(R1), NONMEM SAEM/bootstrap/SIR/MU-referencing, BIC/AIC/ΔOFV implementation expansion unless explicitly labeled as non-textbook implementation commentary and separately requested. (Note: textbook-anchored AIC/WRSS values reported in case studies — e.g., PD13 AIC=−97.5, WRSS=0.083, PD35 WRSS sequence — are *data*, not implementation expansion, and remain present.)
- Erlang/Bode/RC/do-loop engineering analogies as canonical textbook facts.
- New case studies beyond PD13, PD20, PD21, and PD35.
- Textbook image embedding or exact figure reproduction.
- Mock NDA submission language or hypothetical regulatory letter text.
- Q10 boss-dilemma 7–8 paragraph regulatory narrative from Step 1 Draft v0 is replaced by compressed Q8 *and* the v3-added Q11 Socratic Dilemma. The v3 Q11 is **shorter and structurally distinct** (Effect-compartment vs Indirect-response mutual-exclusion defense, ~600 words including the answer panel) — it does not restore the forbidden 7–8 paragraph format.

### B11. Source-Boundary and HTML-Readiness Certificates (v3)

| Certificate | Status | Basis |
|---|---|---|
| Required files present | PASS | Scope Lock, PDFs, Audit, Crucible, Content Lock v2, v2.1 patch, compiler prompt, Step 1, patch memo all present. |
| PDF use boundary | PASS | PDFs used only as verification/source-boundary anchors; no image reproduction. |
| Figure rights | PASS | Image rights = None; pointer-only for textbook figures. |
| PART A standalone learner body | PASS_EXPANDED_V3 | Learner Navigation Aid + full scientific §§1–§8 + §6 Diagnostic Lens + figure markers + micro-patches + mastery notes + v3 Apex thesis + v3 Plausible Fallacy + v3 Hidden-state echoes + v3 §5 5-pair restructure + v3 Q11 Boss Dilemma + v3 Practice Briefs (4). v3.1 Korean Readability Patch applied to learner-facing prose only — no scientific or structural change. |
| Compiler readiness | PASS_V3 | Marker mapping, source-page tag rules, navigation anchor rules, CSS/JS constraints, figure rules, prohibited items included. §6 sub-id navigation specified. §7 now 11 Q&A accordions. §5 now 5 pair components. Apex tag rendering specified. v3.1 dual-label rendering note added (B8). |
| Navigation anchor integrity requirement | PASS for instruction | Phase 5 must implement sticky left sidebar, stable ids, no duplicate ids, and href/id self-check before output. |
| Zero-Omission gate (v3) | PASS | All ver1 unresolved high-impact omissions remain resolved (C4-3 through C4-11). All v3 audit-flagged structural gaps closed (C4-12 through C4-17). v3.1 prose-only edits do not affect this gate. |
| Mastery-Uplift gate (v3) | PASS | Wall 1, Wall 2, Wall 3, Wall 4 all explicit; §6 GOF signature dictionary names 4 patterns; escalation cascade explicit in §1; Apex thesis explicit in Card 1; Plausible Fallacy explicit in Card 1 §E-2; 5 §5 Memory Hooks structurally encoded; Boss Dilemma explicit in §7 Q11; Hidden-state echoes explicit at end of each §2 card. v3.1 prose-only edits do not affect this gate. |
| Source-Boundary gate (v3) | PASS | All textbook-derived items use verified anchors. All non-textbook items labeled [교과서 외 실무 해석] / [구조적 비유 — 교과서 외 확장] / [구현 번역] / EXPERT_INFERENCE / CRUCIBLE_DERIVED / [EXPERT_INFERENCE, v3]. §6's source-boundary note opens the section. v3 additions carry no fabricated page tags. v3.1 readability patch did not add or alter any source-boundary label, page tag, or numerical anchor. |
| Splice Verification (v3) | PASS | All seven figure markers present exactly once; positions and anchor strings unchanged from ver1 → ver2 → v3 → v3.1. v3 patches and v3.1 readability edits did not touch any figure marker location or anchor string. |
| Apex Concept standardization (v3) | PASS | Card 1 carries `[⚡ Apex Concept]` tag with explicit Apex thesis block. |
| Plausible Fallacy presence (v3) | PASS | Card 1 §E-2 codifies the "CCW hysteresis ⇒ effect compartment" misconception with mechanism enumeration and three diagnostic failure modes. |
| Memory Hook coverage (v3) | PASS | All 5 §5 pairs carry structural Memory Hooks; Critical Blow preserved on Pair 1. |
| Boss Dilemma presence (v3) | PASS | §7 Q11 added with Socratic format, ★★ SR-tag, and master-modeler trade-off logic in answer panel. |
| Hidden-state echo coverage (v3) | PASS | All 4 §2 cards close with explicit hidden-state declaration; §8 capstone cross-references all four. |
| Practice Brief coverage (v3) | PASS | All 4 §2 cards carry one Practice Brief with stepped decision procedure. |
| **Korean Readability gate (v3.1)** | **PASS** | Learner Navigation Aid localized; four English-only paragraphs in Card 3 and two in Card 4 converted to Korean; Card 2 §D bridge sentence and last paragraph localized; §6 opener and Signature labels dual-labeled (Korean + parenthetical English); §8 §B heading translated; one first-use gloss added (identifiability(식별가능성)); two sentence splits applied for cognitive density. All equations, page tags, source labels, figure markers, and HTML compiler markers preserved verbatim. |
| **Korean-Dominant Readability gate (v3.2)** | **PASS** | PART A learner-facing prose converted to Korean-dominant style. Card 1 §A–§G headers and lead-ins, Card 2 §A–§E (incl. diagnostic matrix table headers/cells), Card 3 §A–§G (incl. ODE leads, alternative structures bullets, Why-the-sign matters), Card 4 §A–§F (incl. core equations, transit chain interpretation, boundary conditions) localized. §1 Big Idea + Concept roadmap header localized. §5 all five Pair tables (Pairs 1–5) had column headers and dimension cells converted to Korean; English-only Critical Blow sentence localized. §6 source-boundary note + all four Signature bodies (관찰 패턴/기계론적 의미/교과서 근거/다음 단계 fields) converted to Korean prose. §7 all 11 Q&A questions and answers converted to Korean. §8 §A position description + §C Professional moat localized; capstone RECAP dual-labeled. All career-critical pharmacometrics terms (clearance, volume of distribution, identifiability, plausible fallacy, Memory Hook, Boss Dilemma, Critical Blow, Practice Brief, biophase concentration, moderator, transduction, etc.) rendered as `한글(English)` on first use. PART B (B1–B11), all equations, all page tags ([G&W p.XXX], [R&T pp.XXX–YYY]), all source labels ([EXPERT_INFERENCE], [TEXTBOOK_DERIVED], [CRUCIBLE_DERIVED], [AUDIT_DERIVED], etc.), all 7 figure markers (F12-01 through F12-07) and their anchor strings, all HTML compiler markers (`<!-- MASTER LENS -->`, `<!-- ANNOTATION -->`, `<!-- ANCHOR -->`, `<!-- TRENCH -->`, `<!-- CONFUSION -->`, `<!-- SELF-TEST -->`, `<!-- RECAP -->`, `<!-- FIGURE_DECISION ... -->`), all numerical anchors (PD21 0.025/0.031/0.018, PD13 AIC=−97.5/WRSS=0.083, PD35 1319→789→642→632→682), all Apex/Plausible Fallacy/Memory Hook/Boss Dilemma blocks, and section/card structures preserved verbatim. No new scientific claims, examples, numbers, page tags, figures, or external references added. |

**Final Go-Decision Verdict (v3.2):** GO. Master file is ready for Phase 5 HTML compilation. All v3 audit-flagged structural gaps (Apex tag standardization, §5 Memory Hooks, Boss Dilemma) closed. All preservation guarantees (PD13 table, hysteresis collapse, diagnostic lens, Critical Blow, page tags) verified intact. v3.1 Korean Readability Patch and v3.2 Korean-Dominant Readability Patch improve learner-facing Korean prose without altering scientific content, equations, page tags, source labels, figure markers, or compiler markers.

---

## Final v3 All-Pass Checklist

This checklist is the v3-specific gate. Phase 5 compiler should fail-fast if any item shows ❌.

| # | Item | Required evidence | Status |
|---:|---|---|:---:|
| 1 | **Apex Concept tag standardized** | Card 1 header reads `[⚡ Apex Concept]` (not `[Apex]`); Apex thesis block immediately follows the header | ✅ |
| 2 | **Plausible Fallacy block in Card 1** | §E-2 names the "CCW hysteresis ⇒ effect compartment" misconception; lists ≥3 alternative mechanisms; describes ≥3 diagnostic failure signatures (dose-scaling, repeated-dose, onset-shape) | ✅ |
| 3 | **Hidden-state echo in all 4 §2 cards** | Each card closes with one-line "Hidden state of this card: [name]" declaration tagged [EXPERT_INFERENCE, v3] | ✅ |
| 4 | **§5 contains 5 pairs each with structural Memory Hook** | Pairs 1–5 each carry a ⚡ 기억 고리 block encoding the *reason* for the distinction (bridge/tank/lock; distribution-vs-system; two-visits; fatigue-vs-recalibration; relay-vs-sprint) | ✅ |
| 5 | **Critical Blow preserved on §5 Pair 1** | Pair 1 ($k_{e0}$ vs $k_{out}$ vs $k_{off}$) retains the §3.9.7 dose-dependent EC50/Emax/n warning with [G&W pp.271–272] anchor | ✅ |
| 6 | **Boss Dilemma as final §7 question** | Q11 is the last Self-Test question, marked ⚡ + ★★, formatted as Socratic dilemma with master-modeler trade-off logic in a `<details>` panel covering both A and B regulatory defenses | ✅ |
| 7 | **All v2 preservation items intact** | PD13 Model I/II/III table (Card 3 §D), Eq.3:204 (Card 3 §B), AUC asymmetry (Card 3 §C), hysteresis collapse method (Card 2 §B-2), §6 Master's Diagnostic Lens (4 signatures), all G&W and R&T page tags, F12-01 through F12-07 figure markers in original positions | ✅ |
| 8 | **All v3 additions tagged [EXPERT_INFERENCE, v3]** | Apex thesis, Plausible Fallacy E-2, hidden-state echoes (×4), §5 Memory Hooks (×5) and pair-restructure note, Q11 Boss Dilemma, Practice Briefs (×4), capstone echo block — all visibly tagged for traceability | ✅ |

**v3 verdict:** **ALL-PASS — GO for Phase 5 HTML compilation.**

---

## v3.1 Final Checklist

This checklist is the v3.1-specific Korean Readability Patch gate. Phase 5 compiler should fail-fast if any item shows ❌.

| # | Item | Status |
|---:|---|:---:|
| 1 | PART A readability improved | ✅ PASS |
| 2 | Scientific content unchanged | ✅ PASS |
| 3 | Equations preserved | ✅ PASS |
| 4 | Page tags preserved | ✅ PASS |
| 5 | Figure markers preserved | ✅ PASS |
| 6 | Source-boundary preserved | ✅ PASS |
| 7 | HTML-readiness preserved | ✅ PASS |
| 8 | Ready for Phase 5 HTML compilation | ✅ PASS |

**Patch coverage summary:**
- 25 patches applied (P-01 through P-25), all Risk = Low.
- 2 patches deferred (P-26 §7 Q-label restructure, P-27 §6 Signature body wholesale Korean conversion) — flagged High Risk in v3.1 patch table; not applied.
- All seven figure-marker anchor strings (F12-01 through F12-07) verified verbatim against v3; no changes.
- All HTML compiler markers (`<!-- MASTER LENS -->`, `<!-- ANNOTATION -->`, `<!-- ANCHOR -->`, `<!-- TRENCH -->`, `<!-- CONFUSION -->`, `<!-- SELF-TEST -->`, `<!-- RECAP -->`, `<!-- FIGURE_DECISION ... -->`) preserved at original positions.
- All MathJax equations (`$...$`, `$$...$$`) preserved verbatim.
- All page tags (`[G&W p.XXX]`, `[R&T pp.XXX–YYY]`) preserved verbatim.
- All v3 augmentation labels ([EXPERT_INFERENCE, v3], [CRUCIBLE_DERIVED], etc.) preserved verbatim.

**v3.1 verdict:** **ALL-PASS — GO for Phase 5 HTML compilation.**

---

## v3.2 Final Checklist

이 체크리스트는 v3.2 Korean-Dominant Readability Patch 게이트다. Phase 5 컴파일러는 ❌가 하나라도 있으면 fail-fast 해야 한다.

| # | 항목 | 상태 |
|---:|---|:---:|
| 1 | PART A 학습자 산문이 한국어 중심으로 변환됨 | ✅ PASS |
| 2 | 핵심 학습 장치명(Memory Hook, Plausible Fallacy, Boss Dilemma, Critical Blow, Practice Brief)이 `한글(English)`로 병기됨 | ✅ PASS |
| 3 | Career-critical pharmacometrics 용어(clearance, volume of distribution, identifiability 등)가 첫 등장 시 `한글(English)`로 병기됨 | ✅ PASS |
| 4 | 모든 수식, MathJax delimiter ($...$, $$...$$) 보존 | ✅ PASS |
| 5 | 모든 page tag ([G&W p.XXX], [R&T pp.XXX–YYY]) 보존 | ✅ PASS |
| 6 | 모든 source label ([EXPERT_INFERENCE], [TEXTBOOK_DERIVED], [CRUCIBLE_DERIVED], [AUDIT_DERIVED] 등) 보존 | ✅ PASS |
| 7 | 모든 figure marker (F12-01 ~ F12-07) 및 anchor 문자열 보존 | ✅ PASS |
| 8 | 모든 HTML compiler marker (MASTER LENS, ANNOTATION, ANCHOR, TRENCH, CONFUSION, SELF-TEST, RECAP, FIGURE_DECISION) 보존 | ✅ PASS |
| 9 | PART B 가드레일이 비파괴적으로 유지됨 (B11에 v3.2 인증 한 줄만 추가) | ✅ PASS |
| 10 | 새 과학적 주장·예시·수치·page tag·figure·외부 참조 없음 | ✅ PASS |
| 11 | section/card 구조와 anchor 변경 없음 | ✅ PASS |
| 12 | code block 내부 미번역 (코드 무결성 유지) | ✅ PASS |
| 13 | Phase 5 HTML compilation 준비 완료 | ✅ PASS |

**최종 인증표 (v3.2):**

| Certificate | Status | Basis |
|---|---|---|
| Korean-Dominant Readability Certificate | PASS | General learner-facing English prose converted to Korean where possible; career-critical terms retained as Korean-English paired expressions on first use. |
| Scientific Preservation Certificate | PASS | No scientific content, equation, number, example, page tag, or source label changed. |
| Marker Integrity Certificate | PASS | All figure markers (F12-01 ~ F12-07), HTML compiler markers, anchors, and section/card structures preserved verbatim. |
| HTML-Readiness Certificate | PASS | Phase 5 compatibility preserved; no HTML/Mermaid/SVG generated in this file. |

**v3.2 verdict:** **ALL-PASS — GO for Phase 5 HTML compilation.**

---

*End of 12_html_compile_input_master_v3.2.md*

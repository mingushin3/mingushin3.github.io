# 15_html_compile_input_master_v3.2.md

**v3.2 note:** This version applies a Korean-Dominant Readability Patch to PART A learner-facing prose. General English prose was converted to Korean where possible, while career-critical pharmacometrics terms are retained as Korean-English paired expressions on first use. Scientific content, equations, numerical anchors, page tags, source labels, figure markers, compiler markers, section structure, and PART B guardrails are preserved. No new scientific claims, examples, numbers, page tags, figures, or external references were added.

**v3.1 note (preserved):** This version applies a Korean Readability Patch to improve learner-facing Korean prose while preserving scientific content, equations, page tags, source labels, figure markers, and Phase 5 HTML-readiness. No new scientific claims, page tags, numerical anchors, figure decisions, or external references were added.

---

# 15_HTML Compile Input Master — v3.2

**Target file**: `15_html_compile_input_master_v3.2.md`  
**Assembly date**: 2026-05-08 (v3.2 Korean-Dominant Readability Patch date; v3.1 patch base preserved)  
**Assembly mode**: PATCH MODE  
**Phase**: 4E + v3 Surgical Patch + v3.1 Korean Readability Patch + v3.2 Korean-Dominant Readability Patch

**ver2 변경 요약** (Phase 4E 진입): Phase 4D PASS 결과 위에 학습자 체화·거장 시각 차원의 bounded 보완을 추가함.
- §1 Recap 직후 "거장의 한 줄(Master's One-liner)" 캡스톤 추가  [CRUCIBLE_DERIVED]
- 각 MUST 카드 Recap 직후 "체화 꿀팁(Embodiment Tip)" 1–2문장 추가 (×6)  [CRUCIBLE_DERIVED]
- 혼동쌍 #1에 Critical Blow 행 추가 (regulatory fabrication 없이; PROMPT 1 §5 명시 요구사항 회복)  [CRUCIBLE_DERIVED]
- 혼동쌍 #2 Memory Hook 강화 (dynamic range 메커니즘 인코딩)  [CRUCIBLE_DERIVED]
- 모든 추가 항목: source page tag 신규 생성 없음, 새 수식·새 임상 예시·새 USD/규제 표현 없음, audit guardrail 위반 없음.
- PART B Mastery Augmentation Log·Splice Verification Table 보존, 신규 항목 #8–#15는 별도 Embodiment Augmentation Log에 기록.

**ver3 변경 요약** (Surgical Patch — Independent Reviewer v3):
- [PATCH 1] §5 Critical Blow 단일화 확인: 혼동쌍 #1에만 1개 존재 확인, 추가 조치 불필요. PART B B4에 단일성 명시 보강.  [EXPERT_INFERENCE, v3]
- [PATCH 2] §2 MUST 1–6 Practice Brief 점검: 전 카드 체화 꿀팁(다축 실천 정보 포함) 이미 보유, MUST 5 Practice Lens 별도 존재 — 신규 추가 불필요.  [EXPERT_INFERENCE, v3]
- [PATCH 3] PART B v3 Change Log 신설 (B12) + 말미 Final v3 All-Pass Checklist (8항목) 추가.  [EXPERT_INFERENCE, v3]
- 과학적 내용, 수식, 소스 페이지 태그, Embodiment Tips, Master's One-liner, Critical Blow, Memory Hooks, 모델-빌딩 워크플로우 전면 보존.
- 신규 [EXPERT_INFERENCE, v3] 항목 이외 어떠한 새 내용·수식·규제 주장도 추가되지 않음.

**v3.1 변경 요약** (Korean Readability Patch — v3 → v3.1):
- PART A 학습자-facing 본문에 한국어 독해성 개선 패치 20개 적용 (P-01 ~ P-20, 전부 Risk = Low).
- 적용 영역: Learner Navigation 영어 산문 → 한국어 변환(P-01 ~ P-11), MUST 카드 핵심 개념의 첫 등장 글로스(P-12 ~ P-15, P-18, P-19), 영어 관용구의 자연스러운 한국어화(P-17, P-20), 미시적 연결어 정제(P-16).
- 보류 처리: P-21 (MUST 4 체화 꿀팁 괄호 분리, Risk = Medium) — 의미 보존 추가 검증 필요로 v3.1에서는 미적용.
- **불변 영역**: 과학 내용, 수식, 페이지 태그([p.XX], [pp.XX–YY], [확인 필요]), source label([CRUCIBLE_DERIVED], [TEXTBOOK_DERIVED], [교과서 외 *]), figure marker(`<!-- FIGURE_POINTER -->`, `<!-- FIGURE_SCHEMATIC -->`), HTML compiler marker(`<!-- MASTER LENS -->`, `<!-- TRENCH -->`, `<!-- CONFUSION -->`, `<!-- SELF-TEST -->`, `<!-- RECAP -->`, `<!-- ANCHOR -->`, `<!-- ANNOTATION -->`), NONMEM 코드, 표준 약어(CL, V, AUC, IIV, OFV 등), Mastery Augmentation Layer 위치·내용, Phase 5 splice anchor 모두 보존.
- 새 과학 주장·새 수치·새 임상 예시·새 페이지 태그·새 reference·새 figure marker 추가 없음.
- PART B 내용 무변경(이 Version Note와 B12 Change Log의 v3.1 항목 추가만 예외).
- HTML readiness 영향 없음. Phase 5 PATCH MODE Splice Verification Table 유효성 유지.

**v3.2 변경 요약** (Korean-Dominant Readability Patch — v3.1 → v3.2):
- PART A 학습자-facing 본문에 한국어 독해성 추가 정제 패치 5개 적용 (Q-01 ~ Q-05, 전부 Risk = Low).
- 적용 영역: §1 후행 지식의 영어 명사구에 한국어 병기 추가(Q-01), §5 혼동쌍 표의 영어 라벨에 한국어 병기 추가(Q-02 ~ Q-04), §7 Self-Test Q1 정답의 영어 단어 나열에 한국어 병기 추가(Q-05).
- 적용 원칙: career-critical pharmacometrics 용어는 `한글(English)` 병기 형태 유지. 기존 한국어화 패턴과 일관성 유지. 수식·페이지 태그·source label·figure marker·HTML compiler marker·표준 약어·NONMEM 코드는 일체 보존.
- v3.1 불변 영역 모두 유지 + v3.2 추가 불변 영역: 모든 Phase 5 splice anchor (각 MUST card Recap의 verbatim opening sentence), 모든 Mastery Augmentation Layer entries, 모든 §2 MUST card 본문 핵심 산문(v3.2 패치 영역과 분리됨), 모든 §1 Big Idea/Roadmap 본문(Q-01 후행 지식 항목만 패치), 모든 §8 Meta-Frame 본문, FIGURE_POINTER/FIGURE_SCHEMATIC marker 내부 영문 brief 일체 보존.
- 새 과학 주장·새 수치·새 임상 예시·새 페이지 태그·새 reference·새 figure marker·새 source label 추가 없음.
- PART B 내용 무변경(이 Version Note, B1의 v3.2 contract clause, Phase 4E Certification 표의 v3.2 row, B10 Micro-Patch Log의 v3.2 entry, B12-B Change Log 신설, 파일 말미 v3.2 Final Checklist 추가만 예외).
- HTML readiness 영향 없음. Phase 5 PATCH MODE Splice Verification Table 유효성 유지.

## Phase 4E Certification

| Certificate | Status | Basis |
| --- | --- | --- |
| Learner-Standalone Certificate | PASS | PART A contains learner navigation, source metadata, §1–§8 learner body, approved figure markers, embodiment tips, master's capstone, and no audit/process tables. |
| Zero-Omission Certificate | PASS | High-impact Scope/Audit/Crucible/PDF-required items are present, repaired earlier in Content Lock v2, or justifiably omitted; no HOLD_UNRESOLVED rows remain. |
| Mastery-Uplift Certificate | PASS | PART A includes seven Phase 4D mastery augmentations plus eight Phase 4E embodiment augmentations (master's one-liner, six per-card embodiment tips, one Critical Blow row, one strengthened memory hook), all bounded, adjacent, and source-labeled. |
| Source-Boundary Certificate | PASS | All Phase 4D and Phase 4E augmentations are labeled TEXTBOOK_DERIVED or CRUCIBLE_DERIVED and add no new page tags, no new equations, no new clinical scenarios, no new regulatory/business claims, no new modern-tool names beyond what was already in Content Lock v2 with [교과서 외 *] labels. |
| HTML-Readiness Certificate | PASS | PART B contains Phase 5 rendering rules, figure/page-tag rules, navigation integrity rules, audit guardrails, splice table, and logs. New embodiment-tip blocks render under existing CONFUSION/TRENCH/RECAP-adjacent style or new dedicated Embodiment Tip style; rendering note added in PART B B4. |
| Embodiment-Coverage Certificate (ver2 신설) | PASS | Each MUST card now carries an explicit "체화 꿀팁" line answering "이 카드의 핵심을 머릿속에 어떻게 박는가." §1 carries the master's one-liner. §5 혼동쌍 #1 has the protocol-mandated Critical Blow row. |
| v3 Surgical Patch Certificate | PASS | Critical Blow 단일화 확인(혼동쌍 #1 전용 1개), Practice Brief 전 카드 충족 확인, B12 Change Log 신설, Final v3 All-Pass Checklist 부착. 과학 내용·수식·페이지 태그 전면 보존.  [EXPERT_INFERENCE, v3] |
| v3.1 Korean Readability Certificate (신설) | PASS | PART A 학습자 진입 영역(Learner Navigation, Figure-use note)의 영어 산문이 한국어로 정제되었고, MUST 1–6 핵심 개념(domain-informed prior, objective function surface, basin, run, dartboard, likelihood surface, pre-fitting stress test)의 첫 등장 글로스가 추가되었다. 모든 패치 Risk = Low. 과학 내용·수식·페이지 태그·figure marker·source label 미변경. Phase 5 PATCH MODE 호환성 유지. |
| v3.2 Korean-Dominant Readability Certificate (신설) | PASS | v3.1 위에 PART A 추가 한국어 정제 패치 5개(Q-01 ~ Q-05, 전부 Risk = Low) 적용. §1 후행 지식 영어 명사구 한영 병기, §5 혼동쌍 #1·#2·#4 표 영어 라벨 한영 병기, §7 Q1 정답 영어 단어 나열 한영 병기. career-critical 용어는 `한글(English)` 형식으로 처리. 과학 내용·수식·페이지 태그·figure marker·source label·HTML compiler marker·NONMEM 코드·표준 약어·Mastery Augmentation Layer 위치·내용·Phase 5 splice anchor 일체 보존. Phase 5 PATCH MODE 호환성 유지. |

## Assembly Mode

**PATCH MODE** — `15_Content Lock v2.1(2).md` is a Figure Marker Insertion Patch, not a full re-emitted learner body. The canonical learner-facing body was constructed from `15_Content Lock v2(3).md` §1–§8, with the seven approved Phase 4C marker blocks inserted after exact unique anchors. No scientific text was rewritten during splicing.

## Input Manifest

| File | Role | Authority level | Used for | Notes |
| --- | --- | --- | --- | --- |
| 15_scope_lock(3).md | Scope Lock | A0 | source boundary; learner; page range; image rights; hard rules | Used to constrain scope and figure rights. |
| 015_G_모델 구축의 기술 초기값·GOF·실험설계(4).pdf | Original textbook PDF | A1 | PDF verification source | Rendered to PNG for figure/table inspection; used only for source/page/figure verification and high-impact omission checks. |
| 15_Audit_Report_v1(5).md | Source Fidelity Audit | A2 | audit guardrail | MUST_FIX/SHOULD_FIX and forbidden-restoration guardrails applied. |
| 15_Content Lock v2(3).md | Content Lock v2 | A3 | canonical body | Primary text-final body; learner-facing §1–§8 used as canonical body. |
| 15_Content Lock v2.1(2).md | Phase 4C Figure Marker Insertion Patch | A4 | figure insertion source | PATCH MODE insertion map and marker blocks #1–#7 spliced into Content Lock v2. |
| 15_crucible_report_v1(1).md | Insight Crucible Report v1 | A5 | crucible guardrail | Used only for accepted high-value insight preservation and labeled mastery notes. |
| 붙여넣은 텍스트 (1)(89).txt | Phase 4D assembler prompt | A7 / process instruction | master assembly contract | Controls PART A/PART B structure, micro-patch gate, augmentation gate, and certification. |
| 붙여넣은 마크다운(2)(64).md | Step 2 HTML Compiler prompt / Prompt 5 | A7 | compiler instruction | Rendering, marker mapping, page-tag, navigation, and output constraints summarized in PART B. |
| 15_step1_draft_v0(3).md | Step 1 Draft v0 | A6 | deprecated source | Not used as learner-body source; only regression-prevention reference. |
| 15_Content Lock v1(2).md | Content Lock v1 | locked reference | reference only | Not used as canonical body because v2 supersedes it. |
| S15_phase1_patch memo(2).md | Phase 1 Patch Memo | audit support / locked reference | reference only | Already adjudicated through Audit/Content Lock; not used as raw learner content. |

## PART A — Learner-Facing Complete Handout

# Session 15 — 모델 구축의 기술: 초기값 · GOF · 모델 판별 · 실험 설계

**Source**: Gabrielsson & Weiner 5e, *Pharmacokinetic and Pharmacodynamic Data Analysis: Concepts and Applications*  
**Scope**: Ch.4 §4.4, §4.7–4.10 + Ch.5 §5.2.3–5.2.4, §5.3.3  
**Verified page range**: p.352–364 / p.368–392 / p.399–405 / p.412–414  
**Missing uploaded pages**: pp.365–367 (§4.5 Minimization, §4.6 Weighting) and pp.406–411 are not included in the uploaded PDF. Any dependence on these pages remains `[확인 필요]`.  
**Mode**: A-Critical  
**Learner-facing status**: Phase 4D learner-complete handout with approved figure markers and bounded mastery augmentation.

## Learner Navigation Aid

### How to use this handout

§1을 먼저 읽어 modeling carousel의 논리 구조를 확정하라. 이후 MUST 카드 여섯 장을 순서대로 공부하라: 초기값 → 잔차 진단 → F-test/AIC/SC 타당성 → 정밀도·상관 → 편미분 샘플링 → 민감도 분석. 학습을 마친 뒤에는 §5로 혼동쌍을 해소하고, §7로 능동 회상을 점검하며, §8로 세션 전체를 하나의 워크플로우 문장으로 압축하라.

### Learning route

| 학습 단계 | 집중 포인트 | 이 단계 이후 할 수 있어야 하는 것 |
|---:|---|---|
| 1 | §1 Roadmap | 이 세션이 여섯 개의 독립 기술이 아니라 하나의 닫힌 모델링 루프인 이유를 설명할 수 있다. |
| 2 | MUST 1 | 그래프·NCA anchor에서 초기값을 도출하고, 초기값이 나쁠 때 fitting이 왜 잘못된 결과로 이어지는지 설명할 수 있다. |
| 3 | MUST 2 | 잔차 형태(banana, fan shape, leverage point)를 구조적 문제·분산/weighting 문제·데이터/설계 문제에 각각 연결할 수 있다. |
| 4 | MUST 3 | F-test, AIC, SC를 적용할 수 있는 조건과 적용할 수 없는 조건을 판단할 수 있다. |
| 5 | MUST 4 | 좋은 curve fit과 parameter 식별가능성(identifiability)이 서로 다른 개념임을 구분할 수 있다. |
| 6 | MUST 5 | 편미분 극값(derivative peak)을 실제 sampling 위치로 변환할 수 있다. |
| 7 | MUST 6 | 민감도 분석을 사용해 예측이나 독성동태 해석이 무너질 수 있는 위치를 특정할 수 있다. |
| 8 | §5/§7/§8 | 혼동쌍을 해소하고, 본문을 보지 않고 자기 테스트에 답할 수 있다. |

### Figure-use note

이 자료는 저작권이 있는 교과서 그림을 직접 재현하지 않는다. `FIGURE_POINTER` 블록은 HTML 컴파일러에게 학습자를 원본 교과서 그림·표로 안내하는 텍스트 전용 callout을 렌더링하도록 지시한다. `FIGURE_SCHEMATIC` 블록은 Phase 5에서 새로 그릴 교육용 도식의 명세를 담고 있으며, 현 단계는 HTML, Mermaid, SVG, 이미지 파일을 직접 생성하지 않는다.

---

## §1 — Session Header & Roadmap

### 이 세션의 정확한 위치

본 세션은 p.352 Fig.4.16의 **modeling carousel**(← 모델링 한 사이클의 반복 구조) 중 Step 4 Explore data, Step 5 Fit model(s), Step 6 Analyze output를 다룬다. <!-- ANNOTATION --> 그 결과를 다음 실험의 Design으로 되돌리므로, 초기값 획득에서 시작해 GOF 판독, 경쟁 모델 선택, outlier 판단, 편미분 기반 sampling design, sensitivity analysis까지 이어지는 한 사이클의 실행 척추다. [p.352]

<!-- MASTER LENS -->
### Big Idea

이 범위의 핵심은 "좋은 통계량을 계산하는 법"이 아니라 **통계량을 적용해도 되는 조건을 아는 법**이다. F-test, AIC/SC, correlation coefficient, WRSS, partial derivatives는 각각 강력하다. 그러나 nested 조건, weighting 조건, residual randomness, parameter identifiability, sampling sensitivity를 벗어나면 이 숫자들은 오히려 잘못된 모델 확신을 만든다. [pp.369–391, pp.399–405]

### 개념 항법도

```text
[초기값 획득] → [잔차 진단] → [F-test/AIC/SC 모델 판별]
      ↑              ↓                  ↓
[민감도 분석] ← [편미분 sampling design] ← [정밀도·상관·설계]
```

<!-- ANCHOR -->
위 흐름은 닫힌 고리다. 초기값이 나쁘면 회귀가 잘못된 minimum으로 간다. 잔차가 무작위가 아니면 모델 또는 weighting이 틀린다. 모델 비교 조건을 어기면 통계 검정이 무의미하다. 그리고 파라미터가 상관되면 다음 실험의 sampling design을 바꿔야 한다. [p.353, pp.369–389, pp.399–405]

### 지식 그래프 위치

**선행 지식**: 1구획/다구획 모델, noncompartmental analysis, nonlinear regression, error model. Ch.4 §4.5 Minimization과 §4.6 Weighting은 pp.365–367 업로드 부재로 `[확인 필요 — pp.365–367 업로드 부재]`를 유지한다.

**후행 지식**: `[교과서 외 구현 번역]` 현대 PopPK에서는 이 세션의 잔차 진단(residual diagnostics), 파라미터 정밀도(parameter precision), −2·log likelihood 비교, 설계 피드백(design feedback)이 NONMEM/PsN/xpose류 workflow로 번역된다. 단, 이 도구명들은 업로드 PDF의 직접 내용이 아니라 구현 환경의 번역이다.

<!-- RECAP -->
**§1 Recap**: 이 세션의 목적은 모델링 결과를 "좋아 보인다"가 아니라 "조건을 만족하므로 비교·해석 가능하다"로 바꾸는 것이다. 즉, 판단의 언어를 인상에서 조건으로 옮기는 것이다.

> **거장의 한 줄 — [CRUCIBLE_DERIVED]**  
> 이 한 문장만 머릿속에 박고 §2로 진입하라: **"좋은 fit은 가설이고, 잔차·정밀도·비교 조건이 그것을 통과시키는 검열이다."** 6개 MUST 카드는 각각 다른 도구처럼 보이지만, 모두 이 한 문장의 검열 절차를 구성한다. 카드를 6개의 독립 기술로 외우면 사이클이 닫히지 않는다. 같은 문장의 6개 검열 통과 조건으로 읽어야 modeling carousel이 회전한다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.352, Fig.4.16, "From tentative model to plot of data."
Why this matters: This figure is the source's organizing spine for the session. It shows that EDA and initial estimates feed fitting, output analysis, and the next experiment rather than ending the process.
When to look: after reading §1 Recap, before entering MUST cards.
Learner instruction: Trace the arrow from Explore data to Fit model(s) to Analyze output, then back to Design. Read every MUST card as one part of this loop, not as an isolated technique.
<!-- /FIGURE_POINTER -->

> **Practice Lens — [CRUCIBLE_DERIVED]**  
> 이 세션은 "모델을 한 번 잘 맞추기"가 아니라, output을 다음 design으로 되돌리는 폐루프 사고를 훈련한다. 각 MUST 카드는 독립 기술이 아니라 다음 실험을 더 정보성 있게 만들기 위한 판단 장치로 읽어야 한다.

---

## §2 — Concept Anatomy Cards

### ▣ MUST 1 — 초기값 획득의 실전 기술 (Initial Estimate Acquisition)

<!-- MASTER LENS -->
**Big Idea**: 초기값은 회귀 알고리즘의 출발점이 아니라, 모델러가 EDA에서 추출해 알고리즘에 넘겨주는 **domain-informed prior**(← 도메인 지식에 근거한 사전 추정값)다. 즉, 알고리즘이 어디서 탐색을 시작할지 정하는 모델러의 첫 판단이다. Gabrielsson은 초기값이 나쁘면 wrong final values, unwanted local minima, physiologically impossible parameter values로 수렴할 수 있다고 경고한다. [p.353]

#### A. Formal Definition

Initial estimate acquisition은 nonlinear regression을 시작하기 전에 그래프, linear regression, NCA, prior compound knowledge로 starting parameter vector를 구성하는 절차다. 이 단계는 fit 이전에 끝나야 한다. 왜냐하면 nonlinear regression은 starting vector가 주어진 뒤에야 objective function surface(← 파라미터 조합에 따라 잔차 제곱합 값이 분포하는 지형)를 탐색하기 때문이다. 이는 modeling carousel의 Explore data 단계에 속한다. [pp.352–353]

#### B. Source-locked derivation anchors

**B-1. IV bolus one-compartment example**: 두 피험자에게 동일한 10 mg IV bolus를 투여한 뒤 semi-log concentration–time plot에서 slope를 읽는다. 이 slope가 elimination rate constant $K$의 초기 anchor가 된다. [pp.353–354]

$$\text{slope}=\frac{\ln(800)-\ln(400)}{23-87}=-0.01\ \text{min}^{-1}=-K \quad [\text{Eq.4:16},\ p.354]$$

이로부터 다음 초기값이 이어진다. [p.354]

$$t_{1/2}=\frac{\ln2}{K}=\frac{0.693}{0.01}\approx65\ \text{min} \quad [\text{Eq.4:17}]$$

$$AUC=\frac{C^0}{K}=100{,}000\ \mu g\cdot L^{-1}\cdot\text{min} \quad [\text{Eq.4:18}]$$

$$Cl=0.1\ L\cdot\text{min}^{-1},\qquad V=10\ L \quad [\text{Eq.4:19–4:20}]$$

**B-2. Bi-exponential curve stripping**: [p.354]

$$C=Ae^{-\alpha t}+Be^{-\beta t}\quad [\text{Eq.4:21},\ p.354]$$

Terminal phase에서 $B$와 $\beta$를 먼저 읽고, back-extrapolated terminal line을 초기 phase에서 빼서 $A$와 $\alpha$를 얻는다. Fig.4.18의 anchor values는 $A=1.0\ \mu g\cdot L^{-1}$, $B=0.8\ \mu g\cdot L^{-1}$, $\alpha=0.05\ \text{min}^{-1}$, $\beta=0.003\ \text{min}^{-1}$이다. [p.355]

**B-3. Dynamic equilibrium response**: Response–concentration 관계에서는 lin-lin plot과 semi-log plot이 서로 다른 정보를 준다. Semi-log plot은 IC50 이하 구간을 확장해 IC50 initial estimate를 더 쉽게 읽게 한다. [pp.355–356]

**B-4. Dynamic non-steady-state turnover**: Warfarin이 prothrombin complex synthesis를 차단하면 downswing slope가 $-k_{out}$를 준다. [pp.356–357]

$$\text{slope}=\frac{\ln(124)-\ln(56.77)}{24-0}\approx -0.03\ h^{-1}\quad [\text{Eq.4:22},\ p.356]$$

이 식은 PDF에 표시된 형태를 보존한다. 다만 산술 부호에는 source-internal inconsistency가 있다. 수학적으로 재작성하려면 $[\ln(56.77)-\ln(124)]/(24-0)$ 또는 $[\ln(124)-\ln(56.77)]/(0-24)$가 된다. 따라서 이는 Draft source mismatch가 아니라 원문 내부 부호 문제다. Baseline 120 sec와 $k_{out}\approx0.03\ h^{-1}$로 $k_{in}=3.6\ \text{sec}\cdot h^{-1}$를 얻는다. [p.357]

**B-5. Indirect response model-choice example**: Eq.4:23–4:33은 baseline, steady state, $E_{max}$, $k_{out}$, $k_{in}$, exponent $n$를 그래프에서 순차 도출하는 예다. Table 4.3은 Model 1과 Model 4의 final estimates와 initial estimates를 비교하며, WRSS/AIC가 Model 1에서 7.3/83, Model 4에서 12/102로 제시된다. 이 예시는 "초기값 계산"이 곧 "모델 선택"의 전 단계임을 보여준다. [pp.358–360]

**B-6. Repeated-dose anxiolytic example**: Eq.4:34의 oral PK input은 $K_a=1.1\ h^{-1}$, $K=0.128\ h^{-1}$, $V/F=5.0\ L\cdot kg^{-1}$로 고정해 response model에 넣는다. PD turnover는 $dR/dt=k_{in}I(C)-k_{out}R$이고, $k_{out}\approx0.06\ h^{-1}$, $k_{in}=4.8$ units, $IC_{50}\approx0.25\ \mu g\cdot L^{-1}$가 initial anchor로 사용된다. [pp.361–363]

**B-7. When all else fails — boundary scaling**: 초기값을 직접 얻기 어렵다면 lower/upper boundary를 이용해 parameter를 0–1 범위로 scaling한다. [p.364]

$$\frac{IE-LB}{UB-LB}\quad [\text{Eq.4:44},\ p.364]$$

원문은 일반적으로 $0.1\cdot IE$부터 $10\cdot IE$까지의 relative range를 권한다. 그러나 Table 4.4처럼 source-specific boundary가 예외를 만들 수 있으므로, 이 규칙을 기계적으로 적용하면 안 된다. [p.364]

<!-- TRENCH -->
**Trench-Level Tip**: `[교과서 외 구현 번역]` Boundary scaling을 현대 nonlinear estimation에서 사용할 때 final estimate가 LB 또는 UB에 붙으면 model이 정보를 준 것이 아니라 boundary가 estimate를 만든 것일 수 있다. Table 4.4의 $\beta=0.05$와 UB=0.05는 그대로 모방할 prescription이 아니라 boundary dependence를 의심하게 하는 teaching example로 읽어야 한다. [p.364]

#### C. Structural Necessity

Bi-exponential curve stripping이 가능한 이유는 $\alpha \gg \beta$일 때 terminal phase에서 $Ae^{-\alpha t}$가 사라지고 $Be^{-\beta t}$만 남기 때문이다. 즉, semi-log plot은 시간 스케일 분리를 눈으로 확인하게 해주는 장치이며, 두 slope가 충분히 분리되지 않으면 curve stripping은 불안정하다. [pp.354–355]

#### D. Assumptions & Boundaries

초기값은 "정확한 값"일 필요는 없다. 그러나 physiologically plausible해야 하고, objective function surface에서 잘못된 basin(← 수렴 가능한 극솟값 영역)으로 들어가지 않을 정도로는 근접해야 한다. 또한 compound knowledge base를 일찍 만들고 regression objective를 명확히 해야 한다. 그렇지 않으면 modeling은 끝없는 journey가 된다. [p.353]

<!-- RECAP -->
**MUST 1 Recap**: 초기값은 계산 전의 사전 판단이다. Graph → slope/intercept/plateau → initial estimates → regression이라는 순서를 바꾸면 알고리즘이 모델러의 눈을 대신할 수 없다.

> **체화 꿀팁 — [CRUCIBLE_DERIVED]**  
> Fit 버튼을 누르기 전에 종이에 (1) 각 parameter의 예상값과 (2) 그 근거(graph slope, NCA, 선행 화합물)를 적어두라. 결과가 그 예상과 크게 어긋나면 모델 결함이 아니라 초기값이 잘못된 basin에 들어갔을 가능성을 먼저 의심한다. 이 한 단계가 fit 결과의 1차 sanity check가 된다.

<!-- FIGURE_SCHEMATIC -->
Title: Bi-exponential curve stripping: terminal-first logic
Mode: R
Visual objective: In 5 seconds, the learner should see that terminal slope is isolated first, then subtracted to reveal the initial slope.
Core message: Curve stripping works only when the fast and slow time scales are visually separable.
Elements to include: semi-log concentration–time axes; observed bi-exponential curve as a generic trajectory; terminal line labeled "read B and beta first"; back-extrapolated terminal line; residual initial line labeled "subtract terminal component → read A and alpha"; warning label "unstable if alpha ≈ beta."
Elements to exclude: exact textbook visual style; dense tick marks or exact point replication; additional PK equations already present in the text.
Suggested rendering: SVG
Caption: A simplified redraw of the curve-stripping logic: terminal-phase information is extracted first, then removed to expose the initial phase.
Alt text: Semi-log concentration–time schematic showing a total bi-exponential curve, a terminal back-extrapolated line, and a residual initial line.
Source relation: Redrawn from textbook concept
<!-- /FIGURE_SCHEMATIC -->

> **Failure Mode — [TEXTBOOK_DERIVED]**  
> 초기값이 "대충 맞는 숫자"처럼 보여도 objective function의 잘못된 basin으로 들어가면 회귀는 그 오류를 스스로 고치지 못한다. 따라서 fit 전에 그래프, compound knowledge, regression objective를 먼저 명시하는 것이 초기값 계산의 일부다.

---

### ▣ MUST 2 — 잔차 기반 모델 진단 (Residual-Based Diagnostics)

<!-- MASTER LENS -->
**Big Idea**: Observed vs predicted curve만 보면 systematic error가 숨어 보인다. Residual plot은 이 숨은 오차를 부호와 순서로 다시 펼쳐준다. 따라서 모델이 놓친 구조, 시간 스케일, 또는 error model을 노출하는 최소 진단 도구다. [pp.368–370]

#### A. Formal Definition

Residual(← 관측값과 예측값의 차이)은 observed value와 calculated/predicted value 사이의 vertical distance다. <!-- ANNOTATION --> [p.369]

$$\epsilon=N(0,\sigma^2)\quad [\text{Eq.4:46},\ p.369]$$

$$residual_i=C_{obs,i}-\hat C_{calc,i}\quad [\text{Fig.4.41},\ p.369]$$

Weighted residual sum of squares는 다음과 같다. [p.371]

$$WRSS=\sum W_i(C_i-\hat C_i)^2\quad [\text{Eq.4:47},\ p.371]$$

$$\sigma=\sqrt{\frac{WRSS}{N_{obs}-N_{par}}}\quad [\text{Eq.4:48},\ p.371]$$

#### B. Diagnostic pattern catalogue

Residual은 random scatter가 되어야 한다. 따라서 consecutive positive/negative residuals가 run(← 같은 부호 잔차가 연속으로 이어지는 패턴)으로 나타나거나 cluster가 생기면, 단순 noise가 아니라 model inadequacy를 의심해야 한다. [pp.369–372]

- Residual vs time에서 banana/U-shape가 보이면 missing exponential term 또는 wrong structural time scale을 의심한다. [pp.372–376]
- Residual amplitude가 concentration과 함께 커지는 fan shape이면 constant variance assumption 또는 weighting이 틀렸을 수 있다. [pp.373–374]
- Ordinary Emax와 sigmoid Emax 비교에서는 predicted curve만으로 애매한 차이가 residual plot에서는 systematic deviation으로 드러난다. [pp.372–373]
- Weighting power/exponent는 source text에서 0, −1, −2, −n으로 설명되며, Eq.4:49는 $C_i^{-\lambda_z}$ 또는 $\hat C_i^{-\lambda_z}$ 형태를 쓴다. 즉, "$\lambda_z=-1$"처럼 부호를 단정하지 말고 **weighting power/exponent**로 표기해야 한다. [pp.373–374]

<!-- ANCHOR -->
잔차 패턴은 단순한 그림 모양이 아니다. 이것은 "모델이 설명하지 못한 시간 스케일 또는 분산 구조"가 밖으로 드러난 형태다. Banana pattern은 빠른 phase가 빠졌다는 신호일 수 있고, fan pattern은 구조보다 error variance model의 문제일 수 있다. [pp.372–376]

#### C. Pure error vs lack-of-fit

Replicate measurement가 있는 in vitro dataset에서는 residual error를 pure error와 lack-of-fit으로 분해할 수 있다. Table 4.7의 예에서 residual SS 92.67, pure error SS 23.61, lack-of-fit SS 69.06이고, Eq.4:51의 $F_{LOF}=15.35$는 $F_{crit}=2.76$보다 커서 lack-of-fit를 지지한다. [pp.377–379]

$$F_{LOF}=\frac{(92.67-23.61)/(25-21)}{23.61/21}=15.35\quad [\text{Eq.4:51},\ p.379]$$

<!-- TRENCH -->
**Trench-Level Tip**: §4.7.3의 LOF F-test는 같은 x값에서 반복 측정이 있어 pure error를 계산할 수 있을 때만 가능하다. 환자별 sparse clinical PK처럼 같은 시점 반복이 없는 데이터에서는 LOF F-test를 억지로 만들지 말고 residual pattern과 model plausibility를 본다.

<!-- TRENCH -->
**Trench-Level Tip**: Residual vs time과 residual vs predicted/concentration을 함께 본다. 한 축에서 random scatter처럼 보여도 다른 축에서 fan shape나 structural run이 나타날 수 있다.

#### D. Structural Necessity

Model misspecification은 observed curve overlay보다 residual plot에서 먼저 보인다. Overlay는 curve와 data의 절대 위치를 보여준다. 반면 residual plot은 오차의 부호와 순서를 보존하므로 systematic deviation을 더 선명하게 드러낸다. [pp.369–376]

<!-- RECAP -->
**MUST 2 Recap**: GOF는 "curve가 지나가는가"가 아니라 "residual이 무작위인가"다. Residual pattern이 있으면 model, weighting, sampling design 중 하나가 정보를 잘못 처리하고 있다.

> **체화 꿀팁 — [CRUCIBLE_DERIVED]**  
> 잔차는 항상 두 축에 동시에 plot한다 — residual vs time과 residual vs predicted/concentration. 한 plot에서 random scatter처럼 보여도 다른 plot에서는 systematic 패턴이 노출되는 일이 흔하다. 두 plot이 모두 random일 때만 잔차가 random이라고 판정한다. 이 두 축 동시 점검을 무의식 단계까지 끌어내리면 GOF 진단의 절반이 자동화된다.

<!-- FIGURE_SCHEMATIC -->
Title: Residual pattern triage: shape → likely failure → next action
Mode: N
Visual objective: In 5 seconds, the learner should map each residual pattern to the correct diagnostic branch.
Core message: Residual shape determines whether the next action should target structure, weighting, or data/design.
Elements to include: four pattern boxes — random scatter, systematic run/banana, fan shape, isolated leverage point; diagnostic labels — acceptable randomness, structural time-scale error, variance/weighting error, outlier/leverage concern; action arrows — keep/check precision, revise structural model, revise error/weighting model, inspect source data and leverage; small warning "do not swap treatments: fan ≠ compartment problem; banana ≠ weighting-only problem."
Elements to exclude: exact textbook residual plots; numerical thresholds; software-specific diagnostics not in Content Lock v2.
Suggested rendering: Mermaid flowchart or CSS-card
Caption: A diagnostic triage map linking residual shape to the most plausible modeling failure and next action.
Alt text: Flowchart connecting residual scatter, banana runs, fan-shaped spread, and leverage points to different modeling responses.
Source relation: Newly designed
<!-- /FIGURE_SCHEMATIC -->

> **Mastery Note — [CRUCIBLE_DERIVED]**  
> 잔차의 시간 패턴은 모델이 놓친 시간 스케일이 밖으로 드러난 흔적이다. Banana/run을 weighting 문제 하나로 덮거나, fan shape를 구조 모델 추가로 해결하려 하면 원인과 처방이 어긋난다.

---

### ▣ MUST 3 — F 검정 적용 조건 (F-Test Validity Conditions) ⚡ Apex Concept

<!-- MASTER LENS -->
**Big Idea**: F-test는 "더 복잡한 모델이 WRSS(← weighted residual sum of squares)를 줄였는가"를 묻는 도구가 아니다. <!-- ANNOTATION --> **Full model과 reduced model이 hierarchical/nested이고, 같은 weighting scheme으로 fit되었을 때만** 추가 parameter의 의미를 검정하는 도구다. [pp.387–388]

#### A. Formal Definition

Nested model(← full model의 제한 형태)이란 full model에서 특정 parameter를 고정하면 reduced model로 collapse되는 관계다. <!-- ANNOTATION --> Sigmoid Emax model은 exponent $n=1$로 고정하면 ordinary Emax model이 되므로 nested 관계다. [p.388]

F statistic은 다음 구조를 갖는다. [p.387]

$$F^*=\frac{(WRSS_{reduced}-WRSS_{full})/(df_{reduced}-df_{full})}{WRSS_{full}/df_{full}}\quad [\text{Eq.4:54},\ p.387]$$

$$df=N_{obs}-N_{par}\quad [\text{Eq.4:55},\ p.387]$$

#### B. Valid vs invalid examples

- **Valid**: ordinary Emax vs sigmoid Emax. Full sigmoid model에서 $n=1$을 고정하면 ordinary Emax로 줄어든다. [p.388]
- **Invalid**: ordinary Emax vs linear response. $C\ll EC_{50}$라는 제한 상황에서만 근사적으로 연결될 뿐, 일반적으로 nested comparison이 아니다. [p.388]
- **Conditionally valid**: hepatic distributed model과 parallel-tube model은 reduced relation이 성립하는 경우 F-test를 사용할 수 있다. [pp.388–389]
- **Invalid with double violation**: Table 4.8의 Michaelis–Menten weighted fit과 first-order unweighted fit은 non-nested이고 weighting도 달라 F-test도 AIC도 사용할 수 없다. [p.389]

#### C. Structural Necessity

<!-- ANCHOR -->
Nested 조건은 parameter 개수 차이가 아니라 **한 모델이 다른 모델의 제한된 형태인가**의 문제다. `[교과서 외 해석]` 기하학적으로 말하면 reduced model은 full model parameter space 안의 제한된 부분공간이어야 한다. 그래야 WRSS 감소량이 "추가 parameter가 설명한 개선"으로 해석된다.

#### C-2. Plausible Fallacy

**Fallacy**: "WRSS가 더 낮고 parameter가 하나 더 많으니 F-test를 쓰면 된다."  
**Correction**: WRSS 감소량은 같은 error/weighting model과 nested 구조 안에서만 F 분포와 연결된다. Non-nested 구조에서는 두 WRSS가 같은 검정 좌표계 위에 있지 않다. [pp.387–389]

#### D. AIC/SC boundary

AIC와 SC는 nested model을 요구하지 않지만, equal weighting은 요구한다. [p.389]

$$AIC=N_{obs}\ln(WRSS)+2N_{par}\quad [\text{Eq.4:56},\ p.389]$$

$$SC=N_{obs}\ln(WRSS)+N_{par}\ln(N_{obs})\quad [\text{Eq.4:57},\ p.389]$$

AIC/SC의 lowest value가 자동으로 adequate model을 뜻하지 않는다. GOF(← model adequacy의 종합 진단)는 residuals, parameter precision, accuracy, correlation matrix, condition number, F-test, AIC/SC를 함께 보는 복합 진단 도구군(battery of tools)이다. <!-- ANNOTATION --> [pp.387–391]

#### E. WRSS vs −2·log likelihood

원문은 historical WRSS 기반 프로그램과 modern −2·log likelihood 기반 프로그램을 구분하되, 비교 원리는 동일하게 model adequacy criteria와 연결된다고 설명한다. [p.386] `[교과서 외 구현 번역]` NONMEM의 OFV 비교로 번역할 수는 있지만, ΔOFV threshold나 SCM rule은 이 PDF의 직접 내용이 아니다.

<!-- RECAP -->
**MUST 3 Recap**: F-test는 nested + equal weighting일 때만 쓴다. AIC/SC는 nested를 요구하지 않지만 equal weighting을 요구하며, 어느 경우든 residual과 biology를 대체하지 못한다.

> **체화 꿀팁 — [CRUCIBLE_DERIVED]**  
> 두 모델의 통계량을 비교하기 전에 두 질문을 먼저 적어라: **(1) 한 모델이 다른 모델의 부분집합인가(nested)? (2) 두 모델이 같은 weighting으로 fit되었는가?** 둘 다 YES면 F-test가 작동한다. weighting만 같으면 AIC/SC만 작동한다. 둘 다 NO면 통계 검정 없이 잔차·메커니즘·외부 데이터로 triangulate한다. 이 두 질문을 비교 전 routine으로 만들면 Table 4.8 같은 더블 위반은 자동으로 차단된다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.389, Table 4.8, Michaelis–Menten weighted fit vs first-order unweighted fit comparison.
Why this matters: Table 4.8 is the compact source example showing why F-test and AIC can both become invalid when model structure and weighting differ. It operationalizes the Apex rule.
When to look: after reading MUST 3 Recap.
Learner instruction: Identify the two violations separately: non-nested model structure and different weighting. Do not collapse them into a vague statement that "models are different."
<!-- /FIGURE_POINTER -->

> **Judgment Lens — [CRUCIBLE_DERIVED]**  
> Nested 조건은 단순히 parameter 수가 다른 관계가 아니라, 두 모델이 같은 비교 좌표계 위에 놓여 있다는 조건이다. 이 조건이 없으면 WRSS 감소량은 "추가 parameter의 기여"가 아니라 서로 다른 문제에서 나온 두 숫자의 차이가 된다.

---

### ▣ MUST 4 — 파라미터 정밀도와 상관 (Parameter Precision & Correlation)

<!-- MASTER LENS -->
**Big Idea**: 좋은 fit은 좋은 parameter를 보장하지 않는다. Parameter precision과 correlation은 모델 자체보다 **sampling design이 parameter를 서로 분리해 보여주었는가**에 좌우된다. 즉, 같은 식이라도 잘못 찍은 시간점에서는 parameter들이 서로 구별되지 않는다. [pp.380–385]

#### A. Accuracy, precision, and CV%

Accuracy는 bias와 관련되고, precision은 estimate의 uncertainty와 관련된다. 즉, 평균적으로 맞는가와 반복하면 얼마나 좁게 모이는가는 다른 질문이다. 원문은 다트 과녁(dartboard) 비유를 통해 accurate/inaccurate와 precise/imprecise를 구분한다. [pp.379–380]

$$CV\%=\frac{SE(\hat p)}{\hat p}\cdot100\quad [\text{Eq.4:52},\ p.380]$$

$p=0.01\pm0.005\ h^{-1}$의 CV 50% 예시는 "높은 uncertainty"를 보여주는 예시일 뿐, PDF-defined rejection threshold가 아니다. [p.380]

#### B. Correlation coefficient r is not GOF

PDF는 correlation coefficient가 가장 많이 오용되는 GOF 기준 중 하나라고 설명한다. Eq.4:53은 원문 표기를 보존한다. [p.381]

$$r=1-\frac{\sum(C_i-\hat C_i)^2}{\sum(C_i-\bar C)^2}\quad [\text{Eq.4:53 source form},\ p.381]$$

Fig.4.53에서 OLS fit은 $r=0.96$이지만 마지막 세 관측치를 systematic하게 underestimate하고, IRLS fit은 $r=0.94$이지만 전체적으로 더 나은 fit을 보인다. 따라서 높은 r은 좋은 fit의 충분조건이 아니다. [p.382]

<!-- CONFUSION -->
`[교과서 외 해석]` Dynamic range가 넓은 concentration–time data에서는 r이 모델의 잔차 구조보다 전체 값의 범위에 강하게 끌릴 수 있다. 그래서 r은 residual plot과 함께 읽어야지 단독 GOF 판정 기준으로 쓰면 안 된다.

#### C. Parameter correlation and ridge geometry

Parameter correlation matrix는 parameter들이 독립적으로 estimate되는지, 또는 서로 trade-off하는지를 보여준다. 원문은 high correlation이 fewer parameters 또는 more data 필요성을 시사한다고 설명한다. [pp.382–383]

<!-- ANCHOR -->
Fig.4.55–4.57의 핵심은 **ridge minimum**(← 길게 늘어진 최솟값 영역)이다. <!-- ANNOTATION --> 두 parameter가 ridge 위에서 같이 움직이면 OFV/WRSS가 거의 변하지 않는다. 이 때문에 univariate estimate는 그럴듯해도 joint uncertainty는 크다. Design A/B 비교는 같은 모델도 sampling design에 따라 Cl/V 또는 IC50/Imax correlation이 크게 달라짐을 보여준다. [pp.383–385]

#### D. Fixing one parameter

Fig.4.55는 한 parameter를 고정하면 다른 parameter의 confidence interval이 작아질 수 있음을 보여준다. [pp.383–384] 그러나 `[교과서 외 실무 해석]` fix 전략은 정당화 부담을 통계에서 biology/literature/prior study로 옮긴다. 따라서 fix value의 출처와 적용 가능성을 설명하지 못하면, precision이 좋아진 것이 아니라 uncertainty를 숨긴 것이다.

#### E. Limitations

High correlation에 대한 universal cutoff는 PDF에 없다. $|r|>0.95$ 같은 hard threshold 대신, correlation matrix, confidence ellipse, residual pattern, design adequacy를 함께 읽는다. `[교과서 외 구현 번역]` Condition number나 covariance-step warning은 현대 구현에서 유용한 신호지만, 이 PDF의 직접 teaching point는 "correlation은 design의 결과"라는 점이다.

<!-- RECAP -->
**MUST 4 Recap**: Fit이 좋아 보여도 parameter가 식별되지 않을 수 있다. Precision은 모델이 아니라 설계가 만든다.

> **체화 꿀팁 — [CRUCIBLE_DERIVED]**  
> Fit이 끝나면 항상 두 가지를 동시에 본다 — observed/predicted overlay와 parameter correlation matrix. Overlay가 좋아 보여도 두 parameter가 강하게 짝지어 움직이면(소스는 보편적 cutoff을 정의하지 않는다는 점에 유의) 그 둘은 사실상 하나의 변형으로 작동한다. 이때 처방은 모델 단순화가 아니라 다음 cohort의 sampling design 변경이다. "fit이 좋다 → parameter가 좋다"라는 자동 연결을 의식적으로 끊는 것이 이 카드의 체화 핵심이다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.382, Fig.4.53; pp.383–385, Fig.4.55–4.57.
Why this matters: Fig.4.53 demonstrates that a higher r can still hide systematic terminal bias. Fig.4.55–4.57 then show that even a plausible fit can have poorly identified correlated parameters.
When to look: after reading MUST 4 Recap, before §5 confusion pairs.
Learner instruction: First compare r=0.96 versus r=0.94 and ask which fit is structurally better. Then inspect the confidence ellipses/design comparison and ask whether the parameter pair is truly identifiable.
<!-- /FIGURE_POINTER -->

> **Mastery Note — [CRUCIBLE_DERIVED]**  
> Ridge minimum을 떠올리면 parameter correlation의 의미가 분명해진다. 능선 위 여러 지점이 거의 같은 WRSS를 주기 때문에, estimate 하나가 그럴듯해도 joint uncertainty는 크게 남을 수 있다.

---

### ▣ MUST 5 — 편미분 기반 최적 샘플링 (Partial-Derivative Optimal Sampling)

<!-- MASTER LENS -->
**Big Idea**: Partial derivative plot(← 파라미터 변화에 대한 예측 변화율 그림)은 "어디서 sample하면 어떤 parameter가 가장 잘 보이는가"를 말해준다. <!-- ANNOTATION --> 예측값이 parameter 변화에 민감한 시간·농도 영역이 그 parameter를 estimate하는 정보의 중심이다. [pp.399–403]

#### A. Bi-exponential derivative design

원문은 bi-exponential model을 예로 든다. [p.399]

$$C=Ae^{-\alpha t}+Be^{-\beta t}\quad [\text{Eq.5:7},\ p.399]$$

$A$와 $B$에 대한 derivatives는 intercept 영역에서, $\alpha$와 $\beta$에 대한 derivatives는 각각 $t=1/\alpha$, $t=1/\beta$에서 극값을 갖는다. [pp.399–400]

$$t=\frac{1}{\alpha},\qquad t=\frac{1}{\beta}\quad [\text{Eq.5:11},\ p.400]$$

예시 parameter가 $\alpha=0.69\ h^{-1}$, $\beta=0.069\ h^{-1}$이면 optimal time은 약 1.4 h와 14 h다. Fig.5.4의 plotted example에서는 $\alpha$와 $\beta$ 정보가 각각 약 20 min, 300 min 부근에 모인다. [p.400]

#### B. Sigmoid Imax / Emax design

Sigmoid Imax model의 derivatives는 $IC_{50}$ 정보가 half-maximal effect 부근에, sigmoidicity factor $n$ 정보가 20%와 80% effect level 부근에 집중됨을 보여준다. Fig.5.6은 $E_0$, $n$, $EC_{50}$, $n$, $E_{max}$에 대한 다섯 design points를 제시한다. [pp.400–402]

#### C. Turnover model design

Turnover response model에서는 $k_{out}$ sensitivity가 25 h와 약 100 h post-dose에서 크고, early time에서는 $k_{out}$가 $IC_{50}$ 또는 $n$보다 민감하다. 따라서 early sampling은 $k_{out}$ initial estimate를 직접 강화한다. [pp.402–404]

#### D. Structural Necessity

<!-- ANCHOR -->
편미분이 큰 위치는 prediction이 해당 parameter 변화에 크게 흔들리는 위치다. `[교과서 외 해석]` 이를 likelihood surface(← 파라미터 공간에서 OFV 값이 분포하는 지형) 언어로 바꾸면, 그 위치의 관측치는 해당 parameter 방향의 surface curvature를 키워 minimum을 더 좁고 깊게 만든다.

<!-- TRENCH -->
**Trench-Level Tip**: `[교과서 외 구현 번역]` Parameter 단위가 다르면 raw $\partial C/\partial\theta$ 크기 비교가 왜곡될 수 있다. 실무에서는 $\theta_i(\partial C/\partial\theta_i)/C$ 같은 normalized sensitivity를 함께 보아 parameter 간 비교를 안정화한다.

#### E. Boundary Conditions

True parameter values를 사전에 알 수 없으므로, derivative maxima에만 sample을 몰아넣으면 안 된다. 전체 concentration range에도 추가 samples를 두어야 한다. 원문은 pooled data를 무비판적으로 design decision에 쓰는 위험도 경고한다. [p.402]

<!-- RECAP -->
**MUST 5 Recap**: 최적 샘플링은 촘촘히 많이 찍는 것이 아니라, 각 parameter가 가장 크게 보이는 곳을 의도적으로 찍는 것이다.

> **체화 꿀팁 — [CRUCIBLE_DERIVED]**  
> 다음 cohort sampling을 정할 때, 각 parameter에 대해 partial derivative plot을 그리고 peak 위치를 시간점으로 옮긴다. 그 시간점들이 design의 anchor가 된다. 그러나 anchor에만 sample을 몰아넣지 말고, 전체 concentration range에 보완 sampling을 함께 둔다 — true parameter는 아직 모르므로 peak 추정은 이동할 수 있다. **"information이 모인 곳에 anchor + 전체 range에 보험"**의 두 층이 이 카드의 체화 골격이다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, pp.400–402, Fig.5.4–5.6; p.403, Fig.5.8.
Why this matters: These figures are the core visual evidence that derivative peaks define informative sampling regions. Without the plots, the rule "sample where sensitivity is high" remains too abstract.
When to look: after reading MUST 5 Recap.
Learner instruction: For each derivative curve, point to the time or concentration region where the curve is largest in magnitude. Translate that region into a sampling design point.
<!-- /FIGURE_POINTER -->

> **Practice Lens — [CRUCIBLE_DERIVED]**  
> 편미분 peak는 "그 parameter가 보이는 시간 또는 농도 영역"을 표시한다. 다만 true parameter가 아직 불확실하므로, peak 주변만 찍는 설계가 아니라 전체 range를 보존하는 보완 sampling이 함께 필요하다.

---

### ▣ MUST 6 — 민감도 분석 (Sensitivity Analysis)

<!-- MASTER LENS -->
**Big Idea**: Sensitivity analysis(← parameter perturbation의 예측 영향 점검)는 fitting 후 해석이 아니다. <!-- ANNOTATION --> 다음 실험을 설계하기 전 "어떤 parameter uncertainty가 prediction을 얼마나 흔드는가"를 보는 사전 점검 절차(pre-fitting stress test)다. [pp.403–405]

#### A. Formal Definition

Sensitivity analysis는 특정 parameter를 일정 비율로 변화시켜 concentration–time 또는 response–time prediction이 어떻게 달라지는지 보는 절차다. 즉, parameter uncertainty가 실제 prediction uncertainty로 얼마나 번역되는지를 본다. 원문의 예시는 parameter를 +100% 또는 −50%로 변화시켜 model output 변화를 비교한다. [pp.404–405]

#### B. PK sensitivity example

Michaelis–Menten pharmacokinetic model에서 $V_{max}$, $K_M$, $V_c$, $V_t$를 변화시키면 concentration–time profile의 어느 구간이 어떤 parameter에 민감한지 드러난다. Fig.5.9는 이것을 future sampling location 결정에 연결한다. [p.405]

#### C. PD sensitivity example

Warfarin-PCA model에서는 $IC_{50}$, $k_{in}$, $k_{out}$, $t_{lag}$의 변화가 response-time profile에 미치는 영향을 비교한다. Fig.5.10의 목적은 "어떤 parameter를 더 잘 estimate하려면 어느 구간을 보강해야 하는가"를 읽는 것이다. [p.405]

#### D. Toxicokinetic design context

Toxicokinetic design에서 chronic studies는 보통 exposure 확인을 위해 Cmax sampling만으로 충분한 경우가 있으나, 예외가 있으며 investigator judgment가 필요하다. Table 5.6은 PK/DRF/chronic study type별로 profile 또는 Cmax 중심 sampling package를 구분한다. [p.413]

Nonlinear elimination에서는 concentration이 first-order linear kinetics 또는 negligible level에 도달할 때까지 sampling하지 않으면 true extrapolated AUC to infinity를 얻을 수 없다. [p.414]

Capacity-dependent kinetics와 time-dependent kinetics가 동시에 존재하면 Day 1 AUC와 steady-state AUC 비교가 상쇄될 수 있다. 이 경우 interpretation은 흐려진다. Fig.5.20의 핵심은 exposure가 변하지 않는 것처럼 보여도 capacity와 induction이 동시에 작동할 수 있다는 점이다. [p.414]

<!-- TRENCH -->
**Trench-Level Tip**: Sensitivity analysis는 parameter를 "잘 추정했는지"보다 먼저 "잘못 추정하면 어떤 결론이 흔들리는지"를 묻는다. 흔들리는 결론이 dose, safety margin, sampling schedule이면 다음 실험 설계를 바꿔야 한다.

<!-- RECAP -->
**MUST 6 Recap**: Partial derivative가 "어디서 정보가 생기는가"를 말한다면, sensitivity analysis는 "정보가 부족하면 결론이 어디서 무너지는가"를 말한다.

> **체화 꿀팁 — [CRUCIBLE_DERIVED]**  
> 해석을 시작하기 전 — 즉 결과로부터 dose, safety margin, sampling schedule을 제안하기 전 — 각 parameter를 ±50% 흔들어 그 결론들이 어떻게 변하는지 본다. 결론이 거의 같으면 그 parameter의 정밀도는 충분하다. 결론이 흔들리면 다음 실험에서 그 영역을 보강한다. **"흔들어도 살아남는 결론만 보고하라"**가 이 카드의 체화 원칙이다. Toxicokinetic 영역에서는 capacity-dependent와 time-dependent 과정이 동시에 작동하면 exposure summary가 비슷해 보여도 흔들기에서 두 효과의 역방향 상쇄가 노출되므로, 흔들기는 단일 결론을 검증하는 동시에 가설을 분리하는 도구가 된다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.405, Fig.5.10; p.414, Fig.5.20.
Why this matters: Fig.5.10 shows how parameter perturbations alter response-time profiles. Fig.5.20 shows the toxicokinetic trap where capacity-dependent and time-dependent processes can mask each other in exposure interpretation.
When to look: after reading MUST 6 Recap, before moving to §5 confusion pairs.
Learner instruction: In Fig.5.10, identify which profile region moves when each parameter is perturbed. In Fig.5.20, focus on why similar-looking exposure summaries can hide two simultaneous kinetic processes.
<!-- /FIGURE_POINTER -->

> **Failure Mode — [TEXTBOOK_DERIVED]**  
> Toxicokinetic design에서 exposure summary가 비슷해 보여도 capacity-dependent process와 time-dependent process가 서로 상쇄될 수 있다. 따라서 sensitivity analysis는 수치가 변했는지보다 어떤 결론이 가려질 수 있는지를 묻는 단계다.

---

## §5 — Confusion Pair Dissection

### ▣ 혼동쌍 #1 — Nested + equal weighting vs non-nested 또는 different weighting

<!-- CONFUSION -->
| 항목 | 올바른 판정 |
|---|---|
| 흔한 오해 | "더 복잡한 모델이 WRSS를 줄이면 F-test를 쓴다." |
| 원전 교정(Source correction) | F-test는 hierarchical/nested model에서만 가능하고, equal weighting이 필요하다. [pp.387–388] |
| AIC/SC 적용 경계(AIC/SC boundary) | AIC/SC는 nested를 요구하지 않지만 equal weighting은 요구한다. [p.389] |
| 결정적 예(Critical example) | Table 4.8의 Michaelis–Menten weighted model vs first-order unweighted model은 F-test도 AIC도 사용할 수 없다. [p.389] |
| 변화 방향 | 통계 검정 하나로 결론 내리지 말고 residual pattern, mechanism plausibility, external evidence, visual prediction을 triangulate한다. |
| **치명적 타격(Critical Blow)** *— [교과서 외 실무 해석]* | 이 비교 조건 위반은 그 한 검정의 무효화에서 끝나지 않는다. 잘못된 모델 위에 쌓이는 후속 dose simulation, safety margin 계산, 다음 cohort sampling 권고가 모두 같은 오류를 상속하므로, 한 차례의 부주의가 modeling carousel 전체 사이클을 오염시킨다. PDF는 이 워크플로우 전파를 명시하지 않으므로 거장의 실무 해석으로 라벨링한다. |

<!-- TRENCH -->
Weighting 선택은 관행이 아니라 residual pattern으로 정당화한다. Fan shape이면 relative error weighting을 의심한다. 반대로 잔차 폭이 균질하면 constant absolute error가 더 자연스럽다. [pp.373–374]

**기억 고리**: F-test는 "nested + same weighting"이라는 잠금장치가 맞아야 열린다. 하나라도 맞지 않으면 낮은 WRSS는 검정 통계량이 아니라 단순한 숫자다.

---

### ▣ 혼동쌍 #2 — Correlation coefficient r vs 진정한 GOF

<!-- CONFUSION -->
| 항목 | 올바른 판정 |
|---|---|
| 흔한 오해 | "r이 높으면 fit이 좋다." |
| 원전 교정(Source correction) | Fig.4.53에서 OLS는 r=0.96이지만 terminal observations를 underestimate하고, IRLS는 r=0.94이지만 더 나은 pattern을 보인다. [p.382] |
| 왜 위험한가 | r은 residual sign/run, variance pattern, terminal bias를 직접 보여주지 못한다. [pp.381–382] |
| 필요한 증거 | observed/predicted overlay + residual vs time + residual vs prediction/concentration + parameter precision. |

`[교과서 외 해석]` PK data처럼 y-range가 넓으면 r은 dynamic range의 영향을 크게 받을 수 있다. 따라서 r은 "전체 설명력"의 보조 숫자일 뿐, GOF 판정의 주연이 아니다.

**기억 고리 — [CRUCIBLE_DERIVED]**: r은 데이터의 농도 폭이 클수록 자동으로 1에 가까워진다. 즉 r=0.95라는 숫자는 모델의 적합도라기보다 데이터의 dynamic range가 만들어낸 그림자다. 모델이 어디서 거짓말하는지는 r이 아니라 **잔차의 부호와 순서**에서 보인다. r은 큰 방향을 보고, 잔차는 모델의 거짓말을 본다.

---

### ▣ 혼동쌍 #3 — Structural model error vs variance/weighting model error

<!-- CONFUSION -->
| 항목 | Structural model error | Variance/weighting model error |
|---|---|---|
| 전형적 residual | Banana, U-shape, systematic runs | Fan shape, concentration-dependent spread |
| 원인 | 빠진 compartment, wrong Emax shape, lag-time omission | constant variance 가정 오류, weighting mismatch |
| 처방 | 구조 모델 수정, phase/time-scale 추가 | error model 또는 weighting 재검토 |
| 원전 anchor 위치(Source anchor) | Residual pattern examples and common residual plots [pp.372–376] | Weighting and error distribution examples [pp.373–374] |

<!-- TRENCH -->
두 종류의 오류를 바꿔 처방하면 모델이 더 복잡해지기만 한다. 예를 들어 fan shape에 compartment를 추가하거나 banana pattern에 weighting만 바꾸면, 문제의 원인은 그대로 남는다.

**기억 고리**: 모양이 휘면 구조를 의심하고, 폭이 벌어지면 variance를 의심한다.

---

### ▣ 혼동쌍 #4 — Outlier A vs Outlier B

<!-- CONFUSION -->
| 항목 | Outlier A | Outlier B |
|---|---|---|
| 원전 서술(Source description) | Vertical deviation from true curve | Time-axis deviation with high leverage |
| 영향 | Precision 감소 | Bias를 만들면서 precision이 좋아 보일 수 있음 |
| 위험 | noisy point로 보임 | 잘못된 curve를 강하게 끌고 감 |
| 원전 anchor 위치(Source anchor) | Fig.4.59 [p.390] | Fig.4.59 [p.390] |

원문은 table만 보면 A와 B의 deviating points를 거의 알아보기 어렵다고 강조한다. 따라서 outlier 판단에서는 graphical presentation이 매우 중요하다. [p.390]

`[교과서 외 통계 도구]` Cook's distance나 hat matrix는 현대 회귀 진단에서 유용하지만, 이 PDF의 핵심은 먼저 plot에서 leverage와 vertical deviation을 구분하는 것이다.

**기억 고리**: A는 위아래로 튄 점이고, B는 시간을 잘못 말하는 점이다. B가 더 위험한 이유는 curve의 방향을 바꾸기 때문이다.

---

## §7 — Self-Test: Active Recall Module

### Q1. [회상 ★★]

<!-- SELF-TEST -->
**문제**: 초기값이 부실할 때 Gabrielsson이 명시한 세 가지 위험은 무엇인가? [p.353]

**정답**: 잘못된 최종 추정값(wrong final values), 원치 않는 국소 최솟값(unwanted local minima), 생리학적으로 불가능한 parameter 값(physiologically impossible parameter values). 초기값은 nonlinear regression에서 단순한 편의값이 아니라 algorithm이 어떤 basin으로 들어갈지 결정하는 EDA 산출물이다.

---

### Q2. [계산 ★★]

<!-- SELF-TEST -->
**문제**: 10 mg IV bolus 예시에서 semi-log slope가 −0.01 min⁻¹일 때 $t_{1/2}$, AUC, Cl, V의 source anchor 값을 쓰라. [p.354]

**정답**: $t_{1/2}\approx65$ min, $AUC=100{,}000\ \mu g\cdot L^{-1}\cdot min$, $Cl=0.1\ L\cdot min^{-1}$, $V=10\ L$. [Eq.4:17–4:20]

---

### Q3. [회상 ★]

<!-- SELF-TEST -->
**문제**: Bi-exponential curve stripping에서 terminal phase를 먼저 읽는 이유는 무엇인가? [pp.354–355]

**정답**: terminal phase에서는 빠른 exponential term $Ae^{-\alpha t}$가 거의 사라지고 $Be^{-\beta t}$가 지배하므로, $B$와 $\beta$를 먼저 얻은 뒤 이를 back-extrapolate하여 초기 phase에서 빼면 $A$와 $\alpha$를 얻을 수 있다.

---

### Q4. [진단 ★★]

<!-- SELF-TEST -->
**문제**: Residual plot에서 banana pattern과 fan shape가 각각 시사하는 문제는 무엇인가? [pp.372–376]

**정답**: Banana/U-shape는 structural time-scale 문제, 예를 들어 빠진 exponential term이나 wrong model shape를 의심하게 한다. Fan shape는 concentration-dependent variance 또는 weighting mismatch를 의심하게 한다.

---

### Q5. [Apex 적용 ★★]

<!-- SELF-TEST -->
**문제**: Ordinary Emax model과 sigmoid Emax model 비교에는 F-test를 쓸 수 있는가? Linear response model과 ordinary Emax model 비교에는 어떤가? [p.388]

**정답**: Ordinary Emax vs sigmoid Emax는 sigmoid model에서 $n=1$로 고정하면 ordinary Emax가 되므로 nested이고 F-test 가능하다. Linear response vs ordinary Emax는 일반적으로 nested가 아니므로 F-test를 쓰면 안 된다.

---

### Q6. [판정 ★★]

<!-- SELF-TEST -->
**문제**: Michaelis–Menten weighted fit과 first-order unweighted fit에서 AIC가 더 낮은 모델을 선택해도 되는가? [p.389]

**정답**: 안 된다. Table 4.8은 두 모델이 non-nested이고 weighting도 다르므로 F-test도 AIC도 쓸 수 없음을 보여준다. AIC/SC는 nested를 요구하지 않지만 equal weighting은 요구한다.

---

### Q7. [계산/개념 ★★]

<!-- SELF-TEST -->
**문제**: Table 4.7의 residual SS 92.67, pure error SS 23.61, df 25와 21로 계산한 $F_{LOF}$는 무엇이며 어떤 결론인가? [pp.378–379]

**정답**: $F_{LOF}=[(92.67-23.61)/(25-21)]/(23.61/21)=15.35$이고, $F_{crit}=2.76$보다 커서 lack-of-fit가 있다. 단, 이 검정은 replicate measurement가 있어 pure error를 분리할 수 있을 때만 가능하다.

---

### Q8. [설계 ★★]

<!-- SELF-TEST -->
**문제**: Fig.4.55–4.57에서 design A와 design B가 가르치는 핵심은 무엇인가? [pp.383–385]

**정답**: Parameter correlation과 confidence ellipse는 model equation만의 문제가 아니라 sampling design의 결과다. 좋은 design은 두 parameter가 서로 trade-off하지 않도록 정보 영역을 분리해 confidence interval과 correlation을 줄인다.

---

### Q9. [Boss Dilemma ★★]

<!-- SELF-TEST -->
**문제**: 두 competing model이 있다. 하나는 lower WRSS를 보이지만 다른 weighting을 사용했고, 다른 하나는 mechanistically plausible하지만 AIC 차이가 작다. 어떤 결정을 내려야 하는가?

**정답**: 먼저 같은 weighting으로 재적합해 비교 가능성을 확보한다. 그래도 F-test/AIC가 단독 결론을 주지 못하면 residual pattern, mechanism plausibility, external data, visual prediction을 함께 triangulate한다. PDF는 AIC difference threshold를 정의하지 않는다. 따라서 낮은 AIC 하나만으로 mechanistic plausibility를 이길 수 없다. [p.389, p.391]

---

## §8 — Meta-Frame & Big Picture

### A. Positioning

<!-- MASTER LENS -->
이 세션은 PK/PD 모델링에서 "모델을 세우는 기술"보다 "모델을 버리거나 다시 설계하는 기술"에 가깝다. Initial estimates는 fit의 출발점을 정한다. Residuals는 모델 결함을 드러낸다. F-test/AIC/SC는 비교 조건을 제한한다. Precision/correlation은 설계의 약점을 노출한다. 그리고 partial derivatives와 sensitivity analysis는 다음 실험의 sampling을 바꾼다. [p.353, pp.369–391, pp.399–405]

`[교과서 외 구현 번역]` 현대 PopPK workflow에서 이 한 사이클의 실무 단위는 단일 run이 아니라 **model/control file 한 버전 + GOF diagnostic plot set + 다음 cohort sampling recommendation**이다. 세 가지가 함께 닫혀야 modeling carousel이 완주된다.

### B. Dependency chain

1. 초기값이 틀리면 convergence가 틀릴 수 있다. [p.353]  
2. Residual이 systematic하면 GOF가 성립하지 않는다. [pp.369–376]  
3. Non-nested 또는 different weighting comparison이면 F-test/AIC가 무력화된다. [pp.387–389]  
4. Parameter correlation이 높으면 next design이 필요하다. [pp.382–385]  
5. Partial derivatives와 sensitivity analysis가 그 next design의 위치를 정한다. [pp.399–405]

### C. Professional moat

경험 많은 모델러는 "어느 모델의 AIC가 낮은가"만 보지 않는다. 두 모델이 비슷한 WRSS/AIC를 보이는데 residual pattern과 mechanism이 모두 애매하면, 어느 한쪽을 고르기 전에 **둘 다 wrong mechanism일 가능성**을 의심한다. 이 역방향 추론이 model selection을 parameter-count game이 아니라 mechanistic hypothesis revision으로 바꾼다.

### D. GOF checklist locked from Table 4.9

<!-- RECAP -->
모델 적합성은 최소한 다음 다섯 질문으로 닫아야 한다. [p.391]

| Checklist question | Locked interpretation |
|---|---|
| Does the model have biological relevance? | Mechanistic plausibility가 없는 낮은 AIC는 취약하다. |
| Does the fitted curve mimic trends in the data? | Curve overlay는 첫 관문이다. |
| Are the parameters estimated with adequate precision? | CV%, SE, confidence intervals를 본다. |
| Do the residuals show lack of systematic deviation? | Run, banana, fan, lag-time pattern을 본다. |
| Do residual plots display random scatter? | 잔차가 무작위가 아니면 모델 또는 weighting을 다시 본다. |

### E. Final locked summary

<!-- RECAP -->
이 세션의 압축 명제는 다음과 같다.

> **초기값은 알고리즘의 출발점을 정하고, residual은 모델의 거짓말을 드러내며, F-test/AIC는 비교 가능한 모델에서만 의미가 있고, precision/correlation은 설계의 품질을 말하며, partial derivative와 sensitivity analysis는 다음 실험을 어디서 다시 해야 하는지 알려준다.**

이 문장을 체화하면 p.352의 modeling carousel은 단순한 그림이 아니라 실제 workflow가 된다: Explore data에서 initial estimates를 만들고, Fit model 후 Analyze output에서 residual/precision/comparison을 검토하며, 그 결과로 다음 Design을 수정한다. [p.352, p.392, pp.399–405]


## PART B — Compiler-Only Appendix

This appendix is not learner-facing. It exists only to protect Phase 5 rendering fidelity and prevent regression. Phase 5 must render PART A only unless explicitly instructed otherwise.

### B1. Compilation Contract

- PART A is the only learner-facing body.
- Phase 5 must render PART A without altering scientific content, equations, source page tags, or markers.
- PART B is instruction/guardrail only and must not be rendered as learner content.
- Do not restore deprecated material from Step 1 Draft v0.
- Do not add new scientific content, new equations, new page tags, new examples, or new figures.
- Do not generate HTML from PART B tables except as internal compiler guidance if explicitly requested.
- **ver2 추가**: Embodiment Tip blocks (체화 꿀팁), Master's One-liner block (거장의 한 줄), 그리고 혼동쌍 #1의 Critical Blow row, 혼동쌍 #2의 강화된 Memory Hook은 모두 PART A의 일부로서 그대로 렌더링한다. 이들은 **새 사실·새 수치·새 그림 마커가 아니라 학습자 체화를 강화하는 거장 시각의 박스 또는 행 추가**이며, 모두 [CRUCIBLE_DERIVED] 또는 [교과서 외 실무 해석] 라벨로 source-boundary 안에 격리되어 있다.
- **v3 추가**: v3 패치는 PART B에만 영향을 주며 PART A 내용을 변경하지 않는다. B12 Change Log와 파일 말미 Final v3 All-Pass Checklist는 compiler-only 메타데이터로, Phase 5 렌더링 대상이 아니다.
- **v3.1 추가**: v3.1 Korean Readability Patch는 PART A 학습자-facing 산문의 한국어 독해성만 개선한다. 모든 수식, 페이지 태그, source label, figure marker, HTML compiler marker, NONMEM/R 코드, 표준 약어, Mastery Augmentation Layer 위치·내용, Phase 5 splice anchor는 그대로 보존된다. PART B는 본 항목과 B12의 v3.1 entry 추가를 제외하면 무변경이다.
- **v3.2 추가**: v3.2 Korean-Dominant Readability Patch는 v3.1 위에서 PART A 학습자-facing 산문의 추가 한국어 정제만 수행한다. career-critical pharmacometrics 용어는 `한글(English)` 병기 형태를 유지한다. v3.1과 동일한 불변 영역(수식, 페이지 태그, source label, figure marker, HTML compiler marker, NONMEM/R 코드, 표준 약어, Mastery Augmentation Layer 위치·내용, Phase 5 splice anchor)은 그대로 보존된다. PART B는 본 항목, Phase 4E Certification 표의 v3.2 row, B10 Micro-Patch Log의 v3.2 entry, B12-B Change Log 신설, 파일 말미 v3.2 Final Checklist 추가를 제외하면 무변경이다.

### B2. Figure Rendering Instructions

**Image rights**: None. Do not embed copyrighted textbook images. Render `FIGURE_POINTER` as text-only callouts. Render `FIGURE_SCHEMATIC` as newly created, visually distinct teaching schematics according to the marker brief. Do not propose or add figures beyond the approved KEEP list.

#### Approved Figure Inventory

| # | Mode | Source figure/table | Location | Phase 5 rendering decision |
| --- | --- | --- | --- | --- |
| 1 | P | Fig.4.16 p.352 | §1 after Recap | Render as text-only pointer callout; no textbook image. |
| 2 | R | Fig.4.18 p.355 concept | MUST 1 after Recap | Render as distinct schematic; do not reproduce textbook figure. |
| 3 | N | Synthesis from residual figures pp.372–376 | MUST 2 after Recap | Render as new diagnostic triage schematic. |
| 4 | P | Table 4.8 p.389 | MUST 3 after Recap | Render as text-only pointer callout; no table image. |
| 5 | P | Fig.4.53 p.382; Fig.4.55–4.57 pp.383–385 | MUST 4 after Recap | Render as text-only pointer callout. |
| 6 | P | Fig.5.4–5.6 pp.400–402; Fig.5.8 p.403 | MUST 5 after Recap | Render as text-only pointer callout. |
| 7 | P | Fig.5.10 p.405; Fig.5.20 p.414 | MUST 6 after Recap | Render as text-only pointer callout. |

#### Rejected Figure Inventory — Do Not Restore

| # | Source | Decision | Reason |
| --- | --- | --- | --- |
| 8 | Fig.4.21 p.357; Table 4.3 p.360 | REJECT | Budget; lower ROI than Fig.4.18; content already preserved in MUST 1. |
| 9 | Fig.4.59 p.390 | REJECT | Budget; outlier distinction already stated in confusion pair. |
| 10 | Table 4.9 p.391 | REJECT | Redundant with §8 checklist. |

### B3. Page Tag Rendering Rules

- Preserve all `[p.XX]`, `[pp.XX–YY]`, `[pp.XX, YY]`, `[p.확인 필요]`, and `[확인 필요]` tags exactly as present in PART A.
- Render page tags visibly in HTML, preferably as `<span class="source-page">...</span>`.
- Render uncertainty tags with a visible uncertain style.
- Do not fabricate, delete, renumber, or relocate source page tags.
- Do not apply source-page detection inside code blocks or inside raw `FIGURE_*` marker blocks.
- Source page tags must remain visible in print mode.

### B4. HTML Compiler Requirements

#### Core rendering rule

Render content; do not alter it. Produce a single self-contained HTML file with custom CSS and JS inline. External runtime dependencies are allowed only for MathJax CDN, Mermaid CDN, and permitted CDN libraries for code highlighting.

#### Marker-to-component mapping

| Marker / Pattern | HTML component | Mandatory rendering note |
|---|---|---|
| `<!-- MASTER LENS -->` | Callout box | border-left gold; lightly tinted background |
| `<!-- ANNOTATION -->` | Inline abbr/tooltip or small italic annotation | preserve in text flow |
| `<!-- ANCHOR -->` | Bridge sentence | italic muted bridge style |
| `<!-- TRENCH -->` | Practical tip box | rose left border / practical warning |
| `<!-- CONFUSION -->` | Comparison component | side-by-side or table/card with amber styling |
| `<!-- SELF-TEST -->` | Click-to-reveal accordion | answer hidden by default |
| `<!-- RECAP -->` | Section summary box | blue left border |
| `[p.XX]`, `[pp.XX–YY]`, `[pp.XX, YY]` | Source page tag span | visible inline and in print |
| `[p.확인 필요]` / `[확인 필요]` | Uncertainty highlight | retain visibly; do not resolve unless verified |
| `<!-- FIGURE_POINTER -->` | Textbook reference callout | text-only; no image embedding |
| `<!-- FIGURE_SCHEMATIC -->` | Inline schematic figure | render from brief using distinct Mermaid/SVG/CSS, not textbook reproduction |
| `<!-- FIGURE_IMAGE_SLOT -->` | Image/placeholder figure | not used in this session because image rights are None |
| **블록쿼트 `> **거장의 한 줄 — [CRUCIBLE_DERIVED]**`** *(ver2)* | Master's capstone callout | gold-tinted callout, slightly larger type, immediately after §1 Recap; semantically distinct from MASTER LENS Big Idea |
| **블록쿼트 `> **체화 꿀팁 — [CRUCIBLE_DERIVED]**`** *(ver2)* | Embodiment tip callout | teal/green left border or distinct visual treatment from TRENCH; positioned directly after each MUST card's Recap and before the FIGURE marker; consistent styling across MUST 1–6 |
| **혼동쌍 표 행 `**치명적 타격(Critical Blow)** *— [교과서 외 실무 해석]*`** *(ver2, v3 단일화 확인)* | Highlighted row inside CONFUSION table | distinct row background (e.g., subtle red/amber tint) within the existing 혼동쌍 #1 table; not a separate table. *(v3 확인: §5 전체 스캔 결과 혼동쌍 #1 전용 단일 행으로 확인됨 — 혼동쌍 #2, #3, #4에는 Critical Blow 없음. Phase 5는 이 행을 혼동쌍 #1 테이블 안의 단일 강조 행으로만 렌더링한다.)* |
| **블록쿼트 `> **Mastery Note / Failure Mode / Practice Lens / Judgment Lens — [CRUCIBLE_DERIVED\|TEXTBOOK_DERIVED]**`** | Phase 4D mastery augmentation callout | preserve as-is from Phase 4D; existing styling (no change in ver2 or v3) |


#### Math, code, interaction, and layout

- MathJax: support inline `\(...\)` and display `\[...\]`, plus existing `$$...$$` blocks if present.
- Code: render `<pre><code>` with copy button; preserve code verbatim.
- Navigation: sticky left sidebar table of contents on desktop; collapsed/single-column behavior on mobile.
- Accordion: Self-Test answers must be hidden by default and revealed only on user click.
- Checklist state: if implemented, persist using `sessionStorage` only.
- Controls: include print/PDF button using `window.print()`.
- Responsive: ≤768px single-column; ≥1024px readable two-column or sidebar layout.
- Dark/light: support `prefers-color-scheme`.
- Print: remove unnecessary backgrounds, hide navigation, optimize page breaks, and keep source-page tags visible.

#### Navigation anchor integrity rules

- Use `<a href="#...">` links only in the sidebar.
- Every sidebar target must have a matching body `id`.
- Every major section heading (§1, §2, §5, §7, §8) must receive a stable id.
- Every §2 concept card should receive a stable id when possible.
- `href` values and body ids must match exactly.
- Do not create duplicate ids.
- Enable `html { scroll-behavior: smooth; }`.
- Before finalizing HTML, count sidebar hrefs, confirm each id exists exactly once, and fix all mismatches before output.

#### Figure rendering self-check

- Every `FIGURE_POINTER` becomes a text-only pointer callout with source, why it matters, when to look, and learner instruction.
- Every `FIGURE_SCHEMATIC` becomes a `<figure>` with caption and alt text.
- Do not reproduce the textbook figure's exact layout, color palette, or label placement.
- For Mermaid blocks, use valid directives and safe node IDs only; if the diagram cannot satisfy Mermaid syntax rules, use inline SVG or CSS cards instead.
- Do not emit a Mermaid block likely to fail rendering.

#### Prohibited in Phase 5

- Modifying PART A text, equations, or source page tags.
- Rendering markers as plain text.
- Showing Self-Test answers without interaction.
- Embedding textbook images or exact figure reproductions.
- Adding external local CSS/JS/font/image files not supplied by the user.
- Using `<iframe>` or `<embed>`.
- Creating sidebar links whose targets do not exist or duplicate ids.

### B5. Audit Guardrails

Do not restore the following rejected or unsupported material:

- Deficiency Letter, Major Deficiency, 6-month review extension, NDA Module 5, specific FDA/EMA reviewer quotes, or FDA Guidance claims as if textbook-derived.
- Unsupported cost, market-value, business-delay, or USD claims.
- Unsupported broad claim that "80% of modeling failures" come from these tool misuses.
- Modern implementation details as source facts: NONMEM, CWRES, NPDE, Pirana/xpose, SCM, ΔOFV thresholds, Bayesian TDM, Fisher information matrix, D-optimal/ED-optimal, PFIM, PopED, Sobol, mrgsolve. These may appear only as clearly labeled `[교과서 외 구현 번역]` or `[교과서 외 해석]` if already in PART A.
- Hard cutoffs such as `CV% > 50%` or `|r| > 0.95` as PDF-defined rejection thresholds.
- Incorrect continuous Ch.5 source range `p.399–414`; use the verified split range `p.399–405 / p.412–414` and retain missing pp.406–411.
- Any correction that treats Eq.4:22 or Eq.4:53 as a Draft-vs-PDF mismatch rather than a source-form/source-internal note.
- Unapproved code blocks, unapproved figure embedding, or unapproved figure generation.

### B6. Crucible Guardrails

- Crucible v1 is not a raw prose source at Phase 5.
- Preserve only insights already present in PART A or explicitly inserted as labeled Mastery Augmentation.
- Do not convert `[CRUCIBLE_DERIVED]` or `[EXPERT_INFERENCE]` notes into textbook-derived claims.
- Do not introduce omitted or rejected Crucible expansions such as VPC/PPC/NPDE expansion, additional cards, or new external optimal-design frameworks.

### B7. Deprecated and Forbidden Restorations

- Step 1 Draft v0 is deprecated.
- Do not restore rejected overclaims, unsupported numerical values, unsupported regulatory claims, source-unsupported examples, unapproved code, or unapproved figures.
- Do not use Step 1 Draft v0 as learner-body source except through a future Micro-Patch Gate.
- Do not broaden the source range beyond the uploaded PDF pages.

### B8. PATCH MODE Splice Verification Table

| Marker # | Anchor text | Anchor found? | Match count | Inserted? | Final location (§ + card) |
| --- | --- | --- | --- | --- | --- |
| 1 | **§1 Recap**: 이 세션의 목적은 모델링 결과를 "좋아 보인다"가 아니라 "조건을 만족하므로 비교·해석 가능하다"로 바꾸는 것이다. 즉, 판단의 언어를 … | YES | 1 | YES | §1 → before §2 |
| 2 | **MUST 1 Recap**: 초기값은 계산 전의 사전 판단이다. Graph → slope/intercept/plateau → initial estimates … | YES | 1 | YES | §2 MUST 1 — Initial Estimate Acquisition |
| 3 | **MUST 2 Recap**: GOF는 "curve가 지나가는가"가 아니라 "residual이 무작위인가"다. Residual pattern이 있으면 model… | YES | 1 | YES | §2 MUST 2 — Residual-Based Diagnostics |
| 4 | **MUST 3 Recap**: F-test는 nested + equal weighting일 때만 쓴다. AIC/SC는 nested를 요구하지 않지만 equal … | YES | 1 | YES | §2 MUST 3 — F-Test Validity Conditions |
| 5 | **MUST 4 Recap**: Fit이 좋아 보여도 parameter가 식별되지 않을 수 있다. Precision은 모델이 아니라 설계가 만든다. | YES | 1 | YES | §2 MUST 4 — Parameter Precision & Correlation |
| 6 | **MUST 5 Recap**: 최적 샘플링은 촘촘히 많이 찍는 것이 아니라, 각 parameter가 가장 크게 보이는 곳을 의도적으로 찍는 것이다. | YES | 1 | YES | §2 MUST 5 — Partial-Derivative Optimal Sampling |
| 7 | **MUST 6 Recap**: Partial derivative가 "어디서 정보가 생기는가"를 말한다면, sensitivity analysis는 "정보가 부족하… | YES | 1 | YES | §2 MUST 6 — Sensitivity Analysis |

**v3.1 splice integrity note**: PATCH MODE Splice Verification Table은 v3.1 Korean Readability Patch 적용 후에도 유효하다. 모든 anchor (각 MUST card Recap의 verbatim opening sentence)는 v3.1에서 변경되지 않았다. v3.1 패치 영역(Learner Navigation, MUST 카드의 first-use gloss, 영어 관용구 한국어화)은 splice anchor와 분리되어 있다.

**v3.2 splice integrity note**: PATCH MODE Splice Verification Table은 v3.2 Korean-Dominant Readability Patch 적용 후에도 유효하다. 모든 anchor (각 MUST card Recap의 verbatim opening sentence)는 v3.2에서 변경되지 않았다. v3.2 패치 영역(§1 후행 지식 영어 명사구 한영 병기, §5 혼동쌍 #1·#2·#3·#4 표 영어 라벨 한영 병기, §7 Q1 정답 영어 단어 나열 한영 병기)은 splice anchor와 분리되어 있다. §5 혼동쌍 표 라벨 변경은 표 내부 셀에 국한되며 §2 MUST card Recap의 anchor 텍스트에 영향을 주지 않는다.

### B9. Zero-Omission Coverage Matrix

| Domain | Required item | Evidence in PART A | Status | Action |
| --- | --- | --- | --- | --- |
| C1 Scope Lock concepts | Initial estimates, GOF/residuals, F-test/AIC/SC, precision/correlation, derivative sampling, sensitivity/toxicokinetic design | §1 roadmap; §2 MUST 1–6; §5 confusion pairs; §8 dependency chain | PRESENT | No action |
| C1 Scope page boundaries | p.352–364 / p.368–392 / p.399–405 / p.412–414; pp.365–367 and pp.406–411 not uploaded | PART A metadata and §1 선행 지식 note | PRESENT | No action |
| C2 Required data anchors | 10 mg IV bolus; K, half-life, AUC, Cl, V; bi-exponential A/B/alpha/beta; warfarin PCA; Table 4.3; repeated-dose anxiolytic; Table 4.4; LOF F-test; Table 4.8; derivative design; toxicokinetic Fig.5.20 | MUST 1 B-1–B-7; MUST 2 C; MUST 3 B/D; MUST 5 A–C; MUST 6 D | PRESENT | No action |
| C3 Audit MUST_FIX | Unsupported regulatory/financial/tool claims removed or labeled; page range corrected; weighting sign convention controlled | §1 후행 지식; MUST 2 B; MUST 3 E; PART B audit guardrails | PRESENT | No action |
| C3 Audit SHOULD_FIX | Eq.4:23–4:33/Table 4.3 restored; Fig.4.19 restored; regression objective/endless journey restored; hard thresholds removed | MUST 1 B-3/B-5/D; MUST 4 A/E | PRESENT | No action |
| C4 Audit T5 coverage | Dynamic non-steady-state, pure error/LOF, accuracy vs precision, WRSS vs −2LL, GOF checklist, toxicokinetic design | MUST 1, MUST 2, MUST 3, MUST 4, MUST 6, §8 D | PRESENT | No action |
| C5 Figure coverage KEEP | Approved Figure #1–#7 markers | PART A contains seven spliced markers after the approved recap anchors | PRESENT | No action |
| C5 Figure rejections | Dynamic non-steady-state pointer, Outlier A/B pointer, Table 4.9 pointer not restored | PART B figure inventory lists rejected items as non-renderable | PRESENT | No action |
| C6 Page tag integrity | Existing page tags preserved; no new tags created by augmentations | PART A body preserves [p.xx]/[pp.xx–yy]; augmentations have no page tags | PRESENT | No action |
| C7 Crucible Grade A preservation | Nested geometry, r misuse, derivative/information link, ridge geometry, residual pattern as time-scale exposure | MUST 2–5 canonical text and Mastery Notes #3–#6 | PRESENT_COMPRESSED | No action |
| C8 Deprecated Draft regression | No unsupported Deficiency Letter, review extension, USD, ΔOFV threshold, or unapproved software workflow restored as textbook content | PART A + PART B guardrails | PRESENT | No action |
| C9 Canonical body integrity | Content Lock v2 §1–§8 preserved; only approved 4C markers and labeled mastery notes inserted | Splice verification table; Mastery Augmentation Log | PRESENT | No action |
| C10 Embodiment coverage (ver2) | 각 MUST 카드별 체화 꿀팁, §1 거장의 한 줄 캡스톤, 혼동쌍 #1 Critical Blow 행, 혼동쌍 #2 강화된 Memory Hook | PART A의 8개 신규 ver2 augmentation; Phase 4E entries #8–#16 in B11 | PRESENT | No action |
| C11 Protocol-mandated structural elements (ver2) | PROMPT 1 §5 Critical Blow 행 (가장 파급력 큰 혼동쌍 1개) | 혼동쌍 #1 Critical Blow row, [교과서 외 실무 해석] labeled | PRESENT | No action |
| C12 v3 Surgical Patch (신설) | Critical Blow 단일화, Practice Brief 전 카드 충족, B12 Change Log, Final Checklist | B4 Critical Blow 단일성 명시 보강; B10 v3 패치 기록; B12 신설; 말미 Checklist | PRESENT | No action |
| C13 v3.1 Korean Readability Patch (신설) | Learner Navigation 한국어화, MUST 1–6 first-use gloss, 영어 관용구 한국어 정제 | Learner Navigation §A; MUST 1 Big Idea/A/D; MUST 2 B; MUST 3 D; MUST 4 A; MUST 5 D; MUST 6 Big Idea | PRESENT | No action |
| C14 v3.2 Korean-Dominant Readability Patch (신설) | §1 후행 지식 영어 명사구 한영 병기, §5 혼동쌍 #1·#2·#3·#4 표 영어 라벨 한영 병기, §7 Q1 정답 영어 단어 나열 한영 병기 | §1 후행 지식 단락; §5 혼동쌍 #1 표 헤더 3개; 혼동쌍 #2 표 헤더 1개; 혼동쌍 #3 표 헤더 1개; 혼동쌍 #4 표 헤더 2개; §7 Q1 정답 첫 문장 | PRESENT | No action |

### B10. Micro-Patch Log

**Phase 4D**: No micro-patches needed. PART A equals spliced learner-facing Content Lock v2 §1–§8 except approved Figure 4C markers and the bounded Mastery Augmentation Layer.

**Phase 4E (ver2)**: Eight bounded enrichment patches applied directly to PART A:
- 1× Master's One-liner capstone block (§1 after Recap)
- 6× Embodiment Tip blocks (one after each MUST 1–6 Recap)
- 1× Critical Blow row appended to 혼동쌍 #1 CONFUSION table (within existing table, not a new table)
- 1× Memory Hook strengthening (replacement of 혼동쌍 #2 hook; single line replacement, no new factual content beyond CRUCIBLE-derived dynamic-range mechanism)

All Phase 4E patches:
- preserve all existing source page tags ([p.XX], [pp.XX–YY], [pp.XX, YY], [확인 필요], [p.확인 필요])
- add no new page tags
- add no new equations
- add no new clinical scenarios, drug names, or dosing values
- add no new regulatory/business/USD claims
- add no new modern-tool names beyond what PART A already contains under [교과서 외 *] labels
- carry [CRUCIBLE_DERIVED] or compound-labeled provenance markers
- pass Audit Guardrail set B5 unchanged
- do not affect the PATCH MODE Splice Verification Table (which remains valid for the 7 Phase 4C figure markers)
- can be cleanly removed (rollback to Phase 4D state) if Phase 5 detects any rendering issue, by deleting the 8 inserted blocks/rows and reverting 혼동쌍 #2 hook

**Phase 4F / v3 (Surgical Patch)**: PART A 내용 무변경. PART B 메타데이터·가이드라인만 갱신.  [EXPERT_INFERENCE, v3]
- [PATCH 1] §5 Critical Blow 전수 스캔: `치명적 타격` 레이블이 붙은 행은 혼동쌍 #1에만 1개 존재. 혼동쌍 #2, #3, #4에는 해당 레이블 없음. 추가 레이블 변경 불필요. B4 마커 테이블에 단일성 확인 주석 추가.
- [PATCH 2] §2 MUST 1–6 Practice Brief 전수 점검: MUST 1–6 전 카드가 체화 꿀팁(다축 실천 정보 포함)을 보유하고 있어 신규 Practice Brief 추가 불필요. MUST 5는 체화 꿀팁 외 Practice Lens 블록도 별도 보유. 모든 카드 Pass.
- [PATCH 3-A] B12 v3 Change Log 신설.
- [PATCH 3-B] 파일 말미 Final v3 All-Pass Checklist (8항목) 추가.
- 모든 v3 패치: 신규 페이지 태그·수식·임상 예시·규제 주장 없음.

**v3.1 (Korean Readability Patch)**: 20개 Low-risk 패치 PART A에 적용. PART B는 본 항목과 B12 v3.1 entry 추가, B1 v3.1 contract clause, Phase 4E Certification 표의 v3.1 Certificate row, B8 splice integrity note, B9 C13 row 추가만 변경됨. 그 외 PART B 메타데이터 무변경.

v3.1 적용 패치 분류:
- **Learner Navigation 한국어화 (P-01 ~ P-11, 11개)**: How to use this handout 단락, Learning route 테이블 헤더 3개·8개 행 설명, Figure-use note 단락의 영어 산문을 한국어로 변환. 표준 약어, MUST/§ 번호 표기, FIGURE_POINTER/FIGURE_SCHEMATIC 마커명, technical 변수명 등 글로벌 표준은 영어 보존.
- **First-use gloss 추가 (P-12 ~ P-15, P-18, P-19, 6개)**: domain-informed prior(MUST 1 Big Idea), objective function surface(MUST 1 A), basin(MUST 1 D), run(MUST 2 B), dartboard(MUST 4 A), likelihood surface(MUST 5 D)에 각 1회 한국어 괄호 글로스 추가. 기존 글로스(modeling carousel, residual, ridge minimum 등)와 동일 형식.
- **영어 관용구 한국어화 (P-17, P-20, 2개)**: "battery of tools" → "복합 진단 도구군(battery of tools)" (MUST 3 D), "pre-fitting stress test" → "사전 점검 절차(pre-fitting stress test)" (MUST 6 Big Idea). 영어 원어 괄호 보존.
- **미시 연결어 정제 (P-16, 1개)**: MUST 2 B의 weighting power/exponent 표기 문장에서 "따라서"를 "즉,"으로 교체하여 인과 vs 동치 관계를 정확히 표현.

v3.1 미적용 패치:
- P-21 (Risk = Medium): MUST 4 체화 꿀팁의 괄호 분리 patch는 의미 보존 추가 검증이 필요하여 v3.1에서 보류. 차후 별도 검토 후 적용 여부 결정.

v3.1 무변경 영역:
- 모든 수식 ($CL$, $V$, $AUC$, $WRSS$, $F^*$, $r$, $C=Ae^{-\alpha t}+Be^{-\beta t}$ 등)
- 모든 페이지 태그 ([p.352], [pp.369–391], [pp.399–405], [확인 필요], [p.확인 필요] 등)
- 모든 source label ([CRUCIBLE_DERIVED], [TEXTBOOK_DERIVED], [EXPERT_INFERENCE, v3], [교과서 외 구현 번역], [교과서 외 해석], [교과서 외 실무 해석], [교과서 외 통계 도구])
- 모든 figure marker (`<!-- FIGURE_POINTER -->`, `<!-- FIGURE_SCHEMATIC -->`, `<!-- /FIGURE_POINTER -->`, `<!-- /FIGURE_SCHEMATIC -->`)
- 모든 HTML compiler marker (`<!-- MASTER LENS -->`, `<!-- TRENCH -->`, `<!-- CONFUSION -->`, `<!-- SELF-TEST -->`, `<!-- RECAP -->`, `<!-- ANCHOR -->`, `<!-- ANNOTATION -->`)
- 표준 약어 (CL, V, Vd, AUC, Cmax, Tmax, ka, ke0, EC50, IC50, Emax, Imax, IIV, BSV, RUV, OMEGA, SIGMA, ETA, EPS, OFV, VPC, GOF, CWRES, NONMEM, NCA, WRSS, AIC, SC, MM, PCA, PK, PD, IRLS, OLS, LOF, df, SE, CV%)
- Mastery Augmentation Layer 8개 항목의 위치·내용·라벨
- 거장의 한 줄 (§1 Master's One-liner) 본문
- 혼동쌍 #1 Critical Blow row 본문
- 혼동쌍 #2 강화된 Memory Hook 본문
- §7 Self-Test 9개 문제·정답·SR 태그
- §8 Final locked summary 압축 명제
- PATCH MODE Splice Verification Table의 모든 anchor (각 MUST Recap의 verbatim opening sentence)

**v3.2 (Korean-Dominant Readability Patch)**: 5개 Low-risk 패치 PART A에 적용. PART B는 본 항목과 B12-B v3.2 Change Log 신설, B1 v3.2 contract clause, Phase 4E Certification 표의 v3.2 Certificate row, B8 v3.2 splice integrity note, B9 C14 row 추가만 변경됨. 그 외 PART B 메타데이터 무변경.

v3.2 적용 패치 분류:
- **§1 후행 지식 영어 명사구 한영 병기 (Q-01, 1개)**: residual diagnostics, parameter precision, design feedback에 한국어 병기 추가. −2·log likelihood 비교는 표준 표기로 보존. NONMEM/PsN/xpose 도구명은 영어 보존.
- **§5 혼동쌍 표 영어 라벨 한영 병기 (Q-02 ~ Q-04, 3개 패치 / 7개 라벨)**: 혼동쌍 #1 표의 "Source correction", "AIC/SC boundary", "Critical example"; 혼동쌍 #2 표의 "Source correction"; 혼동쌍 #3 표의 "Source anchor"; 혼동쌍 #4 표의 "Source description", "Source anchor"에 한국어 병기 추가. 표 본문(설명 셀)은 무변경.
- **§7 Self-Test Q1 정답 영어 단어 나열 한영 병기 (Q-05, 1개)**: "wrong final values, unwanted local minima, physiologically impossible parameter values"에 각각 한국어 번역을 괄호로 병기. 영어 원어는 보존되어 PDF 원전 표현 추적성 유지.

v3.2 무변경 영역:
- v3.1 무변경 영역 전체 (수식, 페이지 태그, source label, figure marker, HTML compiler marker, 표준 약어, Mastery Augmentation Layer, 거장의 한 줄, Critical Blow row 본문, Memory Hooks, Self-Test 문제 본문 및 정답의 핵심 산문, §8 Final locked summary, PATCH MODE Splice Verification Table anchor)
- 추가 v3.2 무변경 영역:
  - PART A 헤더 metadata (Source, Scope, Verified page range, Missing uploaded pages, Mode, Learner-facing status 라벨 — metadata 성격으로 영어 유지)
  - Assembly Mode, Input Manifest 영문 본문 (compiler-only metadata)
  - §1 Big Idea, §1 개념 항법도 ASCII art, §1 Recap, 거장의 한 줄 (모두 v3.2 패치 영역과 분리)
  - §2 MUST 1–6 카드 본문 (Big Idea, A. Formal Definition, B. derivation, C. Structural Necessity, D. Assumptions, E. Limitations, Recap, 체화 꿀팁, Mastery Augmentation block 본문 모두 무변경)
  - §5 혼동쌍 #1, #2, #3, #4 표 본문 셀 (라벨 외 모든 설명 셀 무변경)
  - §5 모든 기억 고리(Memory Hook), TRENCH 블록 본문
  - §7 Q2–Q9 정답 (Q1만 패치)
  - §8 A. Positioning, B. Dependency chain, C. Professional moat, D. GOF checklist, E. Final locked summary 본문 무변경
  - 모든 FIGURE_POINTER / FIGURE_SCHEMATIC marker 내부 영문 brief (v3.2 prompt 명시 규칙: "figure marker의 위치와 내용은 절대 변경하지 마라")
  - 모든 NONMEM/R/Python 코드 블록 (없음, 본 세션은 코드 블록 부재)
  - PATCH MODE Splice Verification Table의 7개 anchor 전부 (각 MUST Recap 첫 문장)

### B11. Mastery Augmentation Log

#### Phase 4D entries (preserved from original master)

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | §1 after Figure #1 | W / workflow consequence | YES | CRUCIBLE_DERIVED | Frames the six cards as a closed modeling loop rather than isolated techniques. | Low |
| 2 | MUST 1 after Figure #2 | F / failure mode | YES | TEXTBOOK_DERIVED | Reinforces bad initial estimates entering the wrong objective-function basin. | Low |
| 3 | MUST 2 after Figure #3 | M / macro insight | YES | CRUCIBLE_DERIVED | Links residual time pattern to missing time scale and prevents treatment swapping. | Low |
| 4 | MUST 3 after Figure #4 | J / judgment lens | YES | CRUCIBLE_DERIVED | Explains nestedness as same-comparison-coordinate condition. | Low |
| 5 | MUST 4 after Figure #5 | M / macro insight | YES | CRUCIBLE_DERIVED | Turns parameter correlation into ridge-minimum geometry. | Low |
| 6 | MUST 5 after Figure #6 | W / workflow consequence | YES | CRUCIBLE_DERIVED | Connects derivative peaks to visible parameter regions while preserving boundary conditions. | Low |
| 7 | MUST 6 after Figure #7 | F / failure mode | YES | TEXTBOOK_DERIVED | Highlights toxicokinetic masking without adding new values or examples. | Low |

#### Phase 4E entries (ver2 — new)

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
| --- | --- | --- | --- | --- | --- | --- |
| 8 | §1 after Recap, before Figure #1 | C / capstone (Master's One-liner) | YES | CRUCIBLE_DERIVED | Provides a single quotable sentence that compresses the session into one master's frame; resolves the "거장 메타 통찰 캡스톤 부재" gap identified in ver1 review. | Low |
| 9 | MUST 1 after Recap | E / embodiment tip | YES | CRUCIBLE_DERIVED | Adds explicit embodiment instruction ("종이에 예상 parameter와 근거 적기") for Initial Estimate card, addressing "체화 꿀팁 부재" gap. | Low |
| 10 | MUST 2 after Recap | E / embodiment tip | YES | CRUCIBLE_DERIVED | Promotes "two-axis residual plot" routine to the level of card-default practice; complements the existing TRENCH on the same point. | Low |
| 11 | MUST 3 after Recap | E / embodiment tip | YES | CRUCIBLE_DERIVED | Converts the F-test/AIC validity rules into a two-question pre-comparison routine; addresses MUST 3 TRENCH absence. | Low |
| 12 | MUST 4 after Recap | E / embodiment tip | YES | CRUCIBLE_DERIVED | Forces the learner to break the automatic "good fit → good parameters" inference; addresses MUST 4 TRENCH absence; carefully avoids introducing new hard thresholds. | Low |
| 13 | MUST 5 after Recap | E / embodiment tip | YES | CRUCIBLE_DERIVED | Makes the "anchor + range" two-layer sampling design explicit as a card practice. | Low |
| 14 | MUST 6 after Recap | E / embodiment tip | YES | CRUCIBLE_DERIVED | Translates sensitivity analysis into a pre-interpretation perturbation routine; ties toxicokinetic masking back to the core practice. | Low |
| 15 | §5 혼동쌍 #1 — Critical Blow row | B / boss-impact row | YES | CRUCIBLE_DERIVED with [교과서 외 실무 해석] label | Restores PROMPT 1 §5 protocol mandate that was previously removed due to Audit MUST_FIX on Deficiency Letter framing; reframes consequence as workflow contamination without fabricating regulatory letters or USD claims. | Low–Medium (label-dependent) |
| 16 | §5 혼동쌍 #2 — Memory Hook | H / memory-hook strengthening | YES | CRUCIBLE_DERIVED | Encodes the dynamic-range mechanism behind r inflation directly into the hook, satisfying the PROMPT 1 §5 requirement that hooks encode structural reasons rather than restate differences. Replaces (not adds to) the previous thinner hook. | Low |

#### Rejected or Deferred Augmentation Candidates (ver1 + ver2)

| Rejected candidate | Reason for rejection |
| --- | --- |
| Additional r/dynamic-range note in §5 | Rejected because canonical body already contains the same bounded interpretation. |
| Outlier A/B new figure or expanded leverage diagnostics | Rejected because Phase 4C rejected the figure and extra statistics would expand beyond the locked body. |
| External NONMEM/ΔOFV/PFIM/PopED implementation details | Rejected because Audit explicitly limits modern tools to labeled implementation translation and forbids unsupported thresholds. |
| Per-card "실무 활용 시나리오" section with full case study | Deferred — would require new clinical scenarios not in source PDF; out of scope. Embodiment tips (Phase 4E) cover the "how to use this in practice" function without introducing new cases. |
| Boss Dilemma Q9 expanded answer with explicit "둘 다 잘못된 모델" branch | Deferred — already covered in §8 Professional Moat; duplication risk. |
| §8 final master's seal beyond existing E. Final locked summary | Deferred — Final locked summary already serves capstone function for §8; ver2 adds master's one-liner at §1 entry which is the higher-leverage location. |
| New page tags on Phase 4E embodiment tips | REJECTED — Phase 1 Rule 8 closed page tagging at Phase 4A; embodiment tips are CRUCIBLE_DERIVED interpretations, not direct PDF citations, and therefore do not carry [p.XX]. |
| P-21 (MUST 4 체화 꿀팁 괄호 분리) | DEFERRED in v3.1 — Risk = Medium. 의미 보존 검증 필요. 차후 별도 검토 시 재평가. |
| Q-XX 후보: PART A 헤더 metadata 라벨(Source/Scope/Verified page range/Missing uploaded pages/Mode/Learner-facing status) 한영 병기 | DEFERRED in v3.2 — metadata 성격으로 영어 보존이 일관성·국제 실무 호환성에 더 적합. v3.2 prompt가 강조하는 "learner-facing 산문" 범위 외부로 판단. 차후 별도 정책 결정 후 재평가. |
| Q-XX 후보: §2 MUST 1 A "Initial estimate acquisition은 nonlinear regression을 시작하기 전에..." 정의 문장의 영어 명사구 추가 한영 병기 | DEFERRED in v3.2 — 이미 v3.1에서 핵심 용어(domain-informed prior, objective function surface, basin)에 first-use gloss 적용 완료. 동일 문장에 추가 병기 시 가독성이 오히려 저하될 수 있음. 현 정제 수준이 적절. |
| Q-XX 후보: §7 Q2–Q9 정답의 영어 명사구 추가 한영 병기 | DEFERRED in v3.2 — Q2–Q9 정답은 이미 한국어 위주로 작성되어 있고 영어 명사구는 표준 약어·기호·고유명사(NCA, IRLS, OLS, F-test, AIC, Emax, sigmoid Emax, weighted/unweighted fit 등)로 한정됨. career-critical 용어 보존 정책에 부합. |
| Q-XX 후보: FIGURE_POINTER / FIGURE_SCHEMATIC marker 내부 영문 brief 한국어화 | REJECTED in v3.2 — v3.2 prompt 명시 규칙 ("figure marker의 위치와 내용은 절대 변경하지 마라") 위반. Phase 5 HTML compiler가 marker 내부를 directive-aware하게 파싱하므로 영문 보존 필수. |

---

### B12. v3 Change Log  [EXPERT_INFERENCE, v3]

*(이 섹션은 compiler-only. Phase 5 렌더링 대상 아님.)*

| Patch ID | 적용 위치 | 수행 내용 | 근거 | 결과 |
| --- | --- | --- | --- | --- |
| P1-SCAN | §5 전체 (혼동쌍 #1–#4) | `치명적 타격` / Critical Blow 레이블 전수 스캔 | 프로토콜: 가장 파급력 높은 혼동쌍 1개에만 허용 | 혼동쌍 #1에만 1개 존재 확인; 혼동쌍 #2–#4 해당 없음. 추가 레이블 변경 불필요. |
| P1-B4 | PART B B4 마커 테이블 | Critical Blow 단일성 확인 주석 추가 ("v3 확인: 혼동쌍 #1 전용 단일 행") | Phase 5 compiler에게 단일 행 조건 명시 전달 | B4 테이블 해당 셀에 주석 삽입 완료 |
| P2-AUDIT | §2 MUST 1–6 전체 | Practice Brief / 4축 실천 블록 존재 여부 점검 | 4축 실천 정보 부재 카드에만 추가 지시 | MUST 1–6 전 카드 체화 꿀팁 보유 확인; MUST 5 Practice Lens 추가 보유; 신규 추가 없음 |
| P3-B9 | PART B B9 Zero-Omission Matrix | C12 행 신설 (v3 Surgical Patch 커버리지) | 패치 추적 완결성 | C12 행 추가 완료 |
| P3-B10 | PART B B10 Micro-Patch Log | Phase 4F/v3 패치 항목 추가 | 변경 이력 기록 | v3 3개 패치 항목 기록 완료 |
| P3-B12 | PART B 말미 | B12 v3 Change Log 신설 (이 표) | 패치 추적 및 감사 가능성 | 신설 완료 |
| P3-CHKLIST | 파일 최말미 | Final v3 All-Pass Checklist (8항목) 추가 | 품질 보증 최종 확인 | 추가 완료 |

**v3 패치 범위 제한 선언**: PART A 과학 내용·수식·페이지 태그·Embodiment Tips·Critical Blow·Memory Hooks·거장의 한 줄·모델-빌딩 워크플로우 일체 무변경. 모든 v3 추가는 PART B 메타데이터 및 파일 말미 Checklist에 국한됨.

---

### B12-A. v3.1 Korean Readability Patch — Change Log

*(이 섹션은 compiler-only. Phase 5 렌더링 대상 아님.)*

| Patch ID | 적용 위치 | 수행 내용 | Change type | Risk |
| --- | --- | --- | --- | --- |
| P-01 | Learner Navigation §A "How to use this handout" 단락 | 영어 산문 → 한국어 번역. 학습 진입 동선·MUST 카드 순서·§5/§7/§8 활용법을 한국어 명령형 문장으로 재구성. | Korean flow improvement | Low |
| P-02 | Learner Navigation §A Learning route 테이블 헤더 3개 | "Route step / Focus / What you should be able to do before moving on" → "학습 단계 / 집중 포인트 / 이 단계 이후 할 수 있어야 하는 것" | Korean flow improvement | Low |
| P-03 | Learning route Row 1 설명 | 영문 → 한국어 ("이 세션이 여섯 개의 독립 기술이 아니라 하나의 닫힌 모델링 루프인 이유를 설명할 수 있다") | Korean flow improvement | Low |
| P-04 | Learning route Row 2 설명 | 영문 → 한국어 (NCA anchor·초기값 도출·fitting 잘못된 결과 연결 설명) | Korean flow improvement | Low |
| P-05 | Learning route Row 3 설명 | 영문 → 한국어 (잔차 형태 → 구조/분산/설계 문제 매핑) | Korean flow improvement | Low |
| P-06 | Learning route Row 4 설명 | 영문 → 한국어 (F-test/AIC/SC 적용 가능 조건 판단) | Korean flow improvement | Low |
| P-07 | Learning route Row 5 설명 | 영문 → 한국어 + identifiability 글로스 | Korean flow improvement + First-use gloss | Low |
| P-08 | Learning route Row 6 설명 | 영문 → 한국어 (편미분 극값 → sampling 위치 변환) | Korean flow improvement | Low |
| P-09 | Learning route Row 7 설명 | 영문 → 한국어 (민감도 분석 → 실패 영역 특정) | Korean flow improvement | Low |
| P-10 | Learning route Row 8 설명 | 영문 → 한국어 (혼동쌍 해소·자기 테스트 답변) | Korean flow improvement | Low |
| P-11 | Learner Navigation §A "Figure-use note" 단락 | 영어 산문 → 한국어 번역. FIGURE_POINTER / FIGURE_SCHEMATIC 마커명·역할 설명을 한국어로 재구성. 마커명 자체는 영어 보존. | Korean flow improvement | Low |
| P-12 | MUST 1 — Big Idea (line 142 region) | "domain-informed prior" 첫 등장에 글로스 "(← 도메인 지식에 근거한 사전 추정값)" 추가 | First-use gloss | Low |
| P-13 | MUST 1 — A. Formal Definition | "objective function surface" 첫 등장에 글로스 "(← 파라미터 조합에 따라 잔차 제곱합 값이 분포하는 지형)" 추가 | First-use gloss | Low |
| P-14 | MUST 1 — D. Assumptions & Boundaries | "basin" 첫 등장에 글로스 "(← 수렴 가능한 극솟값 영역)" 추가 | First-use gloss | Low |
| P-15 | MUST 2 — B. Diagnostic pattern catalogue | "run" 첫 등장에 글로스 "(← 같은 부호 잔차가 연속으로 이어지는 패턴)" 추가 | First-use gloss | Low |
| P-16 | MUST 2 — B. Weighting power/exponent 문장 | 인과 접속 "따라서" → 동치 표현 "즉," 으로 교체. Weighting power/exponent 표기 권고 의미 명료화. | Concept clarification | Low |
| P-17 | MUST 3 — D. AIC/SC boundary | "battery of tools다" → "복합 진단 도구군(battery of tools)이다". 영어 관용구를 한국어 명사구로 풀고 영어 원어 괄호 보존. | Korean flow improvement | Low |
| P-18 | MUST 4 — A. Accuracy, precision, and CV% | "원문은 dartboard를 통해" → "원문은 다트 과녁(dartboard) 비유를 통해". 비유 대상 명시. | First-use gloss | Low |
| P-19 | MUST 5 — D. Structural Necessity | "likelihood surface" 첫 등장에 글로스 "(← 파라미터 공간에서 OFV 값이 분포하는 지형)" 추가 | First-use gloss | Low |
| P-20 | MUST 6 — Big Idea | "pre-fitting stress test다" → "사전 점검 절차(pre-fitting stress test)다". 영어 표현을 한국어 명사구로 풀고 영어 원어 괄호 보존. | Korean flow improvement | Low |

**v3.1 패치 범위 제한 선언**: PART A의 과학 내용·수식·페이지 태그·source label·figure marker·HTML compiler marker·NONMEM/R 코드·표준 약어·Mastery Augmentation Layer 위치 및 본문·Phase 5 splice anchor 일체 무변경. 모든 v3.1 추가는 (a) PART A의 학습자-facing 산문 한국어화 20개 패치(P-01 ~ P-20)와, (b) PART B의 본 Change Log 신설·B1 contract clause·Phase 4E Certification v3.1 row·B8 splice integrity note·B9 C13 row·B10 v3.1 micro-patch entry에 국한됨.

---

### B12-B. v3.2 Korean-Dominant Readability Patch — Change Log

*(이 섹션은 compiler-only. Phase 5 렌더링 대상 아님.)*

| Patch ID | 적용 위치 | 수행 내용 | Change type | Risk |
| --- | --- | --- | --- | --- |
| Q-01 | §1 — 지식 그래프 위치 / 후행 지식 단락 | "residual diagnostics, parameter precision, design feedback" 영어 명사구 3개에 한국어 병기 추가 → "잔차 진단(residual diagnostics)", "파라미터 정밀도(parameter precision)", "설계 피드백(design feedback)". "−2·log likelihood 비교"는 표준 표기로 보존. NONMEM/PsN/xpose 도구명은 영어 보존. | Korean-dominant flow improvement | Low |
| Q-02 | §5 혼동쌍 #1 표 — 라벨 셀 3개 | "Source correction" → "원전 교정(Source correction)". "AIC/SC boundary" → "AIC/SC 적용 경계(AIC/SC boundary)". "Critical example" → "결정적 예(Critical example)". 본문 셀 무변경. | Korean-dominant flow improvement (label-only) | Low |
| Q-03 | §5 혼동쌍 #2 표 — 라벨 셀 1개 | "Source correction" → "원전 교정(Source correction)". 본문 셀 무변경. | Korean-dominant flow improvement (label-only) | Low |
| Q-04 | §5 혼동쌍 #3·#4 표 — 라벨 셀 3개 | 혼동쌍 #3 "Source anchor" → "원전 anchor 위치(Source anchor)". 혼동쌍 #4 "Source description" → "원전 서술(Source description)". 혼동쌍 #4 "Source anchor" → "원전 anchor 위치(Source anchor)". 본문 셀 무변경. | Korean-dominant flow improvement (label-only) | Low |
| Q-05 | §7 Self-Test Q1 정답 첫 문장 | "wrong final values, unwanted local minima, physiologically impossible parameter values" 영어 단어 나열 3개에 한국어 병기 추가 → "잘못된 최종 추정값(wrong final values), 원치 않는 국소 최솟값(unwanted local minima), 생리학적으로 불가능한 parameter 값(physiologically impossible parameter values)". 영어 원어 보존으로 PDF 원전 표현 추적성 유지. 정답 두 번째 문장 무변경. | Korean-dominant flow improvement (term-pair) | Low |

**v3.2 패치 범위 제한 선언**: PART A의 과학 내용·수식·페이지 태그·source label·figure marker·HTML compiler marker·NONMEM/R 코드·표준 약어·Mastery Augmentation Layer 위치 및 본문·Phase 5 splice anchor 일체 무변경. 모든 v3.2 추가는 (a) PART A의 학습자-facing 산문 한국어 정제 5개 패치(Q-01 ~ Q-05)와, (b) PART B의 본 Change Log 신설·B1 v3.2 contract clause·Phase 4E Certification v3.2 row·B8 v3.2 splice integrity note·B9 C14 row·B10 v3.2 micro-patch entry·B11 deferred candidates 추가에 국한됨.

**v3.2 적용 원칙**:
1. **Career-critical 용어 보존**: 영어 원어를 한국어 병기 형식 `한글(English)`로 처리하여 학습자가 한국어로 즉시 이해하면서도 국제 학술·실무 환경에서 영어 용어를 알 수 있도록 함.
2. **Career-critical 용어 보존 (영어 단독 유지)**: 표준 약어·기호·수식 변수·고유명사·코드 변수명·NONMEM/R 구문은 영어 단독 유지 (예: CL, V, AUC, IIV, OFV, NONMEM, MathJax, $r$, $F^*$ 등).
3. **PDF 원전 표현 보존**: §7 Q1 정답의 영어 단어 나열은 PDF 원전 직접 인용 가능성이 있으므로 영어 원어를 괄호 안에 보존.
4. **Splice anchor 무변경**: PATCH MODE Splice Verification Table의 7개 anchor (각 MUST Recap의 verbatim opening sentence)는 일체 손대지 않음.
5. **Marker 내부 무변경**: FIGURE_POINTER / FIGURE_SCHEMATIC marker 내부 영문 brief는 v3.2 prompt 명시 규칙에 따라 보존.

---

## Final v3 All-Pass Checklist  [EXPERT_INFERENCE, v3]

*(이 섹션은 compiler-only. Phase 5 렌더링 대상 아님.)*

| # | 검증 항목 | 결과 |
|---|---|---|
| 1 | §5 Critical Blow 단일화: `**치명적 타격(Critical Blow)**` 레이블이 혼동쌍 #1에만 1개 존재하는가? 나머지 혼동쌍(#2, #3, #4)에는 없는가? | ✅ PASS — 혼동쌍 #1 전용 단일 행 확인, #2–#4 없음 |
| 2 | §2 MUST 1–6 전체: 각 카드에 체화 꿀팁 또는 동등한 다축 실천 블록이 있는가? | ✅ PASS — 6개 카드 전원 체화 꿀팁 보유; MUST 5는 Practice Lens 추가 보유 |
| 3 | 기존 Memory Hooks, Embodiment Tips, Critical Blow, 거장의 한 줄, 모델-빌딩 워크플로우, Apex Concept 전면 보존되었는가? | ✅ PASS — PART A 내용 무변경 |
| 4 | [EXPERT_INFERENCE, v3] 이외 새 도구명·소프트웨어 임계값·규제 주장이 추가되지 않았는가? | ✅ PASS |
| 5 | 소스 페이지 태그 ([p.XX], [pp.XX–YY], [확인 필요]) 추가·삭제·이동 없음이 확인되는가? | ✅ PASS |
| 6 | PART A 과학 내용·수식·임상 예시가 변경되지 않았는가? | ✅ PASS — PART A 무변경 |
| 7 | PART B Audit Guardrails (B5), Crucible Guardrails (B6), 금지 복원 목록 (B7)을 위반하지 않았는가? | ✅ PASS |
| 8 | v3 Change Log (B12) 및 본 Checklist 첨부가 완료되었는가? | ✅ PASS |

> **v3 Surgical Patch — All 8 checks PASS.**  
> 과학 내용 무변경. Critical Blow 단일화 확인. Practice Brief 전 카드 충족. PART B 메타데이터·로그·체크리스트 only 갱신.

---

## v3.1 Final Checklist

*(이 섹션은 compiler-only. Phase 5 렌더링 대상 아님.)*

| # | 검증 항목 | 결과 |
|---|---|---|
| 1 | PART A readability improved (Learner Navigation 한국어화 + MUST 카드 first-use gloss 6개 + 영어 관용구 한국어 정제 2개) | ✅ PASS |
| 2 | Scientific content unchanged (모든 정의·도출·결론·임상 예시·실험 데이터 anchor 보존) | ✅ PASS |
| 3 | Equations preserved (MathJax inline·display 수식 모두 verbatim 보존; Eq.4:16 ~ Eq.5:11, Eq.4:46 ~ Eq.4:57, AIC/SC, $F^*$, $F_{LOF}$, CV%, $r$ 등) | ✅ PASS |
| 4 | Page tags preserved ([p.352], [pp.352–353], [pp.354–355], [pp.369–391], [pp.399–405], [p.확인 필요], [확인 필요 — pp.365–367 업로드 부재] 등 모든 형식 보존; 신규 태그 0건) | ✅ PASS |
| 5 | Figure markers preserved (`<!-- FIGURE_POINTER -->` 5개, `<!-- FIGURE_SCHEMATIC -->` 2개, 모든 marker brief 본문 verbatim 보존) | ✅ PASS |
| 6 | Source-boundary preserved ([CRUCIBLE_DERIVED], [TEXTBOOK_DERIVED], [EXPERT_INFERENCE, v3], [교과서 외 *] 라벨 모두 위치·표기 보존; B5 Audit Guardrails·B6 Crucible Guardrails·B7 Forbidden Restorations 일체 위반 없음) | ✅ PASS |
| 7 | HTML-readiness preserved (모든 HTML compiler marker `<!-- MASTER LENS -->`·`<!-- TRENCH -->`·`<!-- CONFUSION -->`·`<!-- SELF-TEST -->`·`<!-- RECAP -->`·`<!-- ANCHOR -->`·`<!-- ANNOTATION -->` 위치·구문 보존; PATCH MODE Splice Verification Table의 7개 anchor 모두 verbatim 일치) | ✅ PASS |
| 8 | Ready for Phase 5 HTML compilation (B1 Compilation Contract·B2 Figure Rendering·B3 Page Tag Rules·B4 Marker Mapping·B5–B7 Guardrails 모두 충족; v3.1 패치는 산문 가독성 개선에 국한되어 Phase 5 렌더링 파이프라인에 영향 없음) | ✅ PASS |

> **v3.1 Korean Readability Patch — All 8 checks PASS.**  
> PART A 한국어 독해성 개선 완료. 과학 내용·수식·페이지 태그·figure marker·source-boundary·HTML readiness 일체 보존. Phase 5 HTML compilation 진입 준비 완료.

---

## v3.2 Final Checklist

*(이 섹션은 compiler-only. Phase 5 렌더링 대상 아님.)*

| # | 검증 항목 | 결과 |
|---|---|---|
| 1 | PART A learner-facing readability further improved (§1 후행 지식 한영 병기, §5 혼동쌍 표 영어 라벨 한영 병기 7개, §7 Q1 정답 영어 단어 나열 한영 병기) | ✅ PASS |
| 2 | Career-critical pharmacometrics terms 처리 일관성 (`한글(English)` 병기 형태 유지) | ✅ PASS — 적용된 모든 용어가 한영 병기 형식 준수 (잔차 진단, 파라미터 정밀도, 설계 피드백, 원전 교정, AIC/SC 적용 경계, 결정적 예, 원전 서술, 원전 anchor 위치, 잘못된 최종 추정값, 원치 않는 국소 최솟값, 생리학적으로 불가능한 parameter 값) |
| 3 | Scientific content unchanged (모든 정의·도출·결론·임상 예시·실험 데이터 anchor·수치 보존) | ✅ PASS |
| 4 | Equations preserved (MathJax inline·display 수식 모두 verbatim 보존; Eq.4:16 ~ Eq.5:11, Eq.4:46 ~ Eq.4:57, AIC/SC, $F^*$, $F_{LOF}$, CV%, $r$ 등) | ✅ PASS |
| 5 | Page tags preserved (모든 [p.XX], [pp.XX–YY], [pp.XX, YY], [확인 필요], [p.확인 필요] 형식 보존; 신규 태그 0건; 기존 태그 위치 0건 이동) | ✅ PASS |
| 6 | Source labels preserved ([CRUCIBLE_DERIVED], [TEXTBOOK_DERIVED], [EXPERT_INFERENCE, v3], [교과서 외 *] 라벨 모두 위치·표기 보존) | ✅ PASS |
| 7 | Figure markers preserved (`<!-- FIGURE_POINTER -->` 5개, `<!-- FIGURE_SCHEMATIC -->` 2개, 모든 marker 내부 영문 brief 일체 verbatim 보존 — v3.2 prompt 명시 규칙 준수) | ✅ PASS |
| 8 | HTML compiler markers preserved (모든 `<!-- MASTER LENS -->`·`<!-- TRENCH -->`·`<!-- CONFUSION -->`·`<!-- SELF-TEST -->`·`<!-- RECAP -->`·`<!-- ANCHOR -->`·`<!-- ANNOTATION -->` 위치·구문 보존) | ✅ PASS |
| 9 | Standard abbreviations preserved (CL, V, Vd, AUC, Cmax, Tmax, ka, ke0, EC50, IC50, Emax, Imax, IIV, BSV, RUV, OMEGA, SIGMA, ETA, EPS, OFV, VPC, GOF, CWRES, NONMEM, NCA, WRSS, AIC, SC, MM, PCA, PK, PD, IRLS, OLS, LOF, df, SE, CV%, F-test 영어 단독 유지) | ✅ PASS |
| 10 | Mastery Augmentation Layer 위치·본문 보존 (Phase 4D 7개 entries + Phase 4E 8개 entries — 거장의 한 줄, 체화 꿀팁 6개, Critical Blow row, 강화된 Memory Hook 모두 v3.2에서 무변경) | ✅ PASS |
| 11 | PATCH MODE Splice Verification Table의 7개 anchor 모두 verbatim 일치 (각 MUST Recap의 첫 문장이 v3.2에서 변경되지 않음) | ✅ PASS |
| 12 | Section/card structure unchanged (§1, §2 MUST 1–6, §5 혼동쌍 #1–#4, §7 Q1–Q9, §8 A–E 구조 무변경) | ✅ PASS |
| 13 | No new scientific claims, no new numbers, no new examples, no new page tags, no new figures, no new source labels added | ✅ PASS |
| 14 | Code blocks not translated (본 세션 PART A에는 NONMEM/R/Python 코드 블록 없음 — 해당 없음으로 자동 PASS) | ✅ PASS |
| 15 | PART B guardrails (B5 Audit Guardrails, B6 Crucible Guardrails, B7 Forbidden Restorations) 일체 위반 없음 | ✅ PASS |
| 16 | PART B 변경은 v3.2 metadata에 국한 (B1 contract clause, Phase 4E Certification row, B8 splice integrity note, B9 C14 row, B10 micro-patch entry, B11 deferred candidates, B12-B Change Log, 본 Final Checklist만 추가/수정) | ✅ PASS |
| 17 | HTML-readiness preserved (Phase 5 PATCH MODE Splice Verification Table 유효성 유지; v3.2 패치 영역과 splice anchor 분리 확인됨) | ✅ PASS |
| 18 | Ready for Phase 5 HTML compilation (v3.2 패치는 산문 가독성 개선에 국한되어 Phase 5 렌더링 파이프라인에 영향 없음) | ✅ PASS |

> **v3.2 Korean-Dominant Readability Patch — All 18 checks PASS.**  
> PART A 한국어 중심 독해성 추가 정제 완료. 과학 내용·수식·페이지 태그·figure marker·source label·HTML compiler marker·표준 약어·Mastery Augmentation Layer·Phase 5 splice anchor 일체 보존. Phase 5 HTML compilation 진입 준비 완료.

---

## Final Certification Summary (v3.2)

| Certificate | Status | Basis |
|---|---|---|
| Korean-Dominant Readability Certificate | PASS | General learner-facing English prose converted to Korean where possible; career-critical terms retained as Korean-English paired expressions. |
| Scientific Preservation Certificate | PASS | No scientific content, equation, number, example, page tag, or source label changed. |
| Marker Integrity Certificate | PASS | All figure markers, compiler markers, anchors, and section/card structures preserved. |
| HTML-Readiness Certificate | PASS | Phase 5 compatibility preserved; no HTML/Mermaid/SVG generated. |

---

*`15_html_compile_input_master_v3.2.md` — Korean-Dominant Readability Patch Editor, 2026-05-08*  
*v3.1 base: Independent Pharmacometrics Master Reviewer & Korean Readability Patch Editor, 2026-05-07*  
*v3 base: Independent Pharmacometrics Master Reviewer & Surgical Patch Editor, 2026-05-07*

# XX_html_compile_input_master_v3.1.md

**v3.1 note:** This version applies a Korean Readability Patch to improve learner-facing Korean prose while preserving scientific content, equations, page tags, source labels, figure markers, and Phase 5 HTML-readiness. No new scientific claims, page tags, numerical anchors, figure decisions, or external references were added.

---

# 00_HTML Compile Input Master — v3.1

**Output file**: `00_html_compile_input_master_v3.1.md`
**Assembly date**: 2026-05-07
**Assembly mode**: PATCH MODE
**Phase**: 4D — Learner-Complete + Mastery-Enriched + HTML-Ready Master Assembly
**Revision basis**: v3 was GO. v3.1 applies 13 surgical Korean Readability Patches to PART A only (sentence-level readability and first-use glosses). No scientific content, equation, page tag, figure marker, or PART B guardrail is altered.
**Important**: This is not HTML. Do not generate HTML, Mermaid, SVG, or image embeds from this file until Phase 5.

## ver1 → ver2 Change Log (assembly-only edits; no scientific content changed)

| # | Change | Location | Type | Source-boundary impact |
|---|---|---|---|---|
| Δ1 | Moved `§8.D Compression Compliance Note` from PART A to PART B as new section `B0. Compression Lineage Note` | PART A → PART B | Structural relocation only — text identical | None — process/audit content is now Compiler-Only as B1 contract requires |
| Δ2 | Reformatted three `FIGURE_POINTER` blocks from inline `<br>`-separated single line to multi-line block (one field per line) | §2 M1, M2, M3 figure markers | Whitespace-only re-formatting; identical fields (Source / Why / When / Learner instruction); identical anchors | None — Phase 4C splice content semantically unchanged; Phase 5 parser more robust |
| Δ3 | Added structural memory hook to §5 Pair 1 (PK vs PD), keeping the existing source-grounded `Lock` line and adding one `Memory Hook` line that encodes the structural reason for the difference | §5 Pair 1 | One added line, ≤2 sentences, derived from existing PDF-grounded statements (T p.5) — no new numbers, examples, or page tags | None — paraphrases existing source statements; no new claim |
| Δ4 | Added one Apex visual cue in §1 Roadmap to align with the M1 card heading's existing `⚡ Apex Concept` badge | §1 Roadmap | Single inline marker added next to "M1. Modeling Carousel" | None — visual consistency only |
| Δ5 | Updated `Phase 4D Certification` table, `B10 Micro-Patch Log`, `B11 Mastery Augmentation Log`, `B9 Zero-Omission Coverage Matrix`, and `Final Checklist` to reflect ver2 state | Certification / Logs / Checklist | Metadata accounting | None |

All ver1 anchors remain verbatim; the PATCH MODE Splice Verification Table in §B8 is unchanged because anchor strings (`## Card M1 …`, `## Card M2 …`, `## Card M3 …`) are not altered.

## ver2 → v3 Change Log (surgical patches; no scientific content changed)

| # | Change | Location | Type | Source-boundary impact |
|---|---|---|---|---|
| Δ6 | Added `### C-2. Plausible Fallacy` block to Card M1 (Apex Concept): 그럴싸한 오해 "좋은 fit = 옳은 모델", 기계론적 반박, 실무 시그니처 (VPC 없이 GOF만 제출 → deficiency letter) | §2 Card M1, between §C and §D | Content addition — labeled `[EXPERT_INFERENCE, v3]`; no new page tags, equations, or examples | None — paraphrases existing Carousel step logic; no external claim |
| Δ7 | Standardized memory hook label in §5 Pair 1 from `**⚡ 기억 고리**:` to `**⚡ 기억 고리 (Memory Hook)**:` | §5 Pair 1 | Label-only formatting change; content identical | None |
| Δ8 | Expanded §8.C Professional Lock from single sentence to 4-bullet structured block labeled `[EXPERT_INFERENCE, v3]` | §8.C | Content addition; no new page tags or equations | None — derived from existing M1–M4 concepts already in PART A |
| Δ9 | Added `▶ Practice Brief — M[N] 체화 4축` block at end of each M1–M4 card (after RECAP, before `---`) | §2 Cards M1, M2, M3, M4 | Content addition — labeled `[EXPERT_INFERENCE, v3]`; 4 lines each | None — derived from existing card content |
| Δ10 | Updated PART B: v3 Change Log; Mastery Augmentation Log v3 entries; Coverage Matrix v3 items; Final Checklist v3 state | PART B (B10, B11, B9, Final Checklist) | Metadata accounting | None |

All ver2 anchors remain verbatim. Card heading anchor strings unchanged.

## v3 → v3.1 Change Log (Korean Readability Patch; no scientific content changed)

| # | Change | Location | Type | Source-boundary impact |
|---|---|---|---|---|
| Δ11 | Applied 13 Low-risk Korean Readability Patches (P-001 ~ P-013) to PART A learner-facing prose: 2 first-use glosses (WRSS, parameter-space basin), 2 tone smoothing edits (process-language → learner-language), 7 Korean flow improvements (sentence connectors, more natural phrasing, parallel-structure clarification), 1 first-use gloss + flow improvement (steep/threshold-like), 1 concept clarification (즉, connector). All scientific content, numerical anchors, page tags, equations, figure markers, and section/card structure preserved verbatim. | §2 Cards M1–M4, §2 Recap, §5 Pair 1 | Sentence-level prose readability only | None — no new claims, no new page tags, no new examples, no new figure decisions, no equation changes, no PART B alteration except adding Δ11 to B10 Micro-Patch Log |

All v3 anchors remain verbatim. Card heading anchor strings unchanged. PATCH MODE Splice Verification Table in §B8 is unchanged.

---

## Phase 4D Certification (v3.1)

| Certificate | Status | Basis |
|---|---|---|
| Learner-Standalone Certificate | **PASS** | PART A contains only learner-facing content. v3.1 patches improve Korean readability of existing learner content; no compiler-only material was added. |
| Zero-Omission Certificate | PASS | All v3 MUST concepts, data anchors, Audit MUST/SHOULD corrections, Crucible-adopted insights, and 3 approved Figure Pointers are preserved verbatim. v3.1 adds no new scope items. |
| Mastery-Uplift Certificate | PASS | All v3 augmentations (Plausible Fallacy, Practice Briefs, §8C 4-bullet, Memory Hook label) preserved. v3.1 does not add new mastery content; it only improves Korean prose readability of existing content. |
| Source-Boundary Certificate | PASS | v3.1 patches introduce zero new page tags, equations, numerical values, drug examples, or external claims. All edits are sentence-level prose readability only. |
| HTML-Readiness Certificate | PASS | PART B rendering contracts and anchor integrity rules unchanged. v3.1 patches use existing prose patterns; no new marker types introduced; gloss patches use the established `(← Korean term)` convention already present in §1 Curation Map. |
| Korean Readability Certificate (v3.1) | **PASS** | 13 Low-risk patches applied: WRSS gloss, parameter-space basin gloss, "이 Content Lock" → "이 카드", "dose가" sentence connector, "T Fig.1-3" flow, "이 통계가 시사하는 바는", "steep/threshold-like" gloss, "즉," connector, "Entry rule" → "판단 기준", "원문에서 잠글 것은" → "이 카드에서 체화할 것은", "각각 보여 준다", "권리가" → "근거가", "치료적으로 유용한 예측은". |

## Assembly Mode

**PATCH MODE** — `00_Content Lock v2.1.md` is a Figure Marker Patch / Insertion Map, not a full body. The learner body was assembled from `00_Content Lock v2.md` with the three approved Phase 4C `FIGURE_POINTER` blocks inserted at verified card boundaries.

## Input Manifest

| File | Role | Authority level | Used for | Notes |
|---|---|---|---|---|
| `00_scope_lock.md` | scope boundary | A0 | source range, learner, mode, image-rights, hard boundaries, required anchors | G p.1–7 + T p.3–49 locked. |
| Gabrielsson Pre-Sprint PDF | PDF verification source | A1 | Gabrielsson Ch.1 source verification | Used only for source/page/figure identity and omission checks. |
| Rowland & Tozer Pre-Sprint PDF | PDF verification source | A1 | Rowland & Tozer Ch.1–2 source verification | Used only for source/page/figure identity and omission checks. |
| `00_Audit_Report_v1.md` | audit guardrail | A2 | correction/regression prevention | MUST/SHOULD fixes and forbidden restorations enforced. |
| `00_Content Lock v2.md` | canonical body | A3 | base learner body | Processing record and adjudication process table excluded from PART A; learner body preserved. |
| `00_Content Lock v2.1.md` | figure insertion source | A4 | PATCH MODE figure strategy and insertion map | Three approved FIGURE_POINTER blocks spliced. |
| `00_crucible_report_v1.md` | crucible guardrail | A5 | accepted high-value insight preservation | Used only for adopted/allowed interpretive logic and mastery notes. |
| Workflow v3.3.3 spec | compiler instruction | A7 | Phase 5 HTML rendering requirements | Marker mapping, page-tag rendering, navigation integrity, figure rules. |
| `00_step1_draft_v0.md` | deprecated source | A6 | regression check only | Not used as raw body source. |
| `S00_phase1_patch memo.md` | locked reference / audit attention guide | A6-adjacent | source fidelity caution | Not used as independent source. |
| `00_Content Lock v1.md` | locked reference | lower than v2 | lineage check | Not used as body source. |

---

## PART A — Learner-Facing Complete Handout

## Learner Navigation Aid

**How to use this handout**: 먼저 §1 Roadmap으로 네 개의 MUST 개념을 잡고, §2의 M1→M4 카드를 순서대로 읽는다. 그다음 §5 Confusion Pair와 §7 Self-Test로 "개념을 설명할 수 있는지"를 확인한다.

**Recommended learning route**:
1. M1 — Modeling Carousel: fitting보다 앞선 사고 순서 확인.
2. M2 — PK/PD Linkage: dose regimen을 exposure와 response로 번역.
3. M3 — Emax/C50/Hill γ: 농도-반응 곡선의 ceiling, potency, steepness 분리.
4. M4 — Turnover: concentration peak와 effect peak가 분리될 때의 delay 사고.
5. §5와 §7 — 혼동쌍과 active recall로 마무리.

**Figure note**: `FIGURE_POINTER`는 교과서 그림을 직접 삽입하지 않는다. Image rights = None이므로 Phase 5에서는 텍스트형 참고 callout으로만 렌더링하고, 학습자는 해당 교과서 페이지의 원그림을 따로 확인한다.

**Before you finish**: 아래 네 문장을 스스로 말할 수 있어야 한다.
- 왜 fitting은 Modeling Carousel의 시작점이 아닌가?
- 왜 PK-only 또는 PD-only로는 dosing decision이 불완전한가?
- 왜 γ는 단순 exponent가 아니라 response sensitivity의 언어인가?
- 왜 turnover에서는 "얼마나 많이"와 "얼마나 빠르게"를 분리해야 하는가?

---

# 00_Content Lock v2 — Pre-Sprint: 모델링 철학·용어

**Source**: Gabrielsson & Weiner 5e Ch.1, p.1–7 + Rowland & Tozer 5e Ch.1–2, p.3–49
**Mode**: B-Standard
**Image rights**: None
**Phase**: 4B-2 — Readability Polish + Pedagogical Annotation
**Output type**: Phase 4D learner-facing markdown body with approved FIGURE_POINTER markers spliced; no HTML

---

# Updated Curation Map

이 세션은 두 권의 교과서가 서로 다른 질문에 답하는 진입점이다. Gabrielsson & Weiner는 **어떤 사고 순서로 모델링할 것인가**를 정한다. Rowland & Tozer는 **그 모델링 언어를 임상 용량 결정으로 어떻게 번역할 것인가**를 정한다. 후속 PopPK 세션에서 control stream, GOF, parameter interpretation, TDM 판단을 다루기 전에 잠가야 할 기반은 네 개다.

## MUST tier

| # | 개념 | Source | Lock 판정 |
|---|---|---|---|
| M1 | Modeling Carousel & 5대 dysfunction | Gabrielsson Ch.1 | 모델링은 fitting이 아니라 질문→설계→실험→EDA(← 그래프 중심 탐색적 데이터 분석) <!-- ANNOTATION -->→fitting→진단의 순환이라는 사고 순서를 고정한다. |
| M2 | PK/PD Linkage & Therapeutic Window | Rowland & Tozer Ch.1 | dose regimen을 exposure-time profile과 response-time profile로 번역하는 임상 정량화의 출발점이다. |
| M3 | Emax / C50(← 최대효과 절반 농도) <!-- ANNOTATION --> / Hill γ(← 곡선 가파름 계수) <!-- ANNOTATION --> | Rowland & Tozer Ch.2 | 농도-반응 관계를 Emax, potency, steepness로 분해하는 direct-effect PD 모델의 골격이다. |
| M4 | Turnover(← 체내 물질의 생성·소실 순환) <!-- ANNOTATION --> | Rowland & Tozer Ch.2 | response delay와 endogenous system의 dynamic equilibrium을 이해하는 indirect-response 모델의 선행 개념이다. |

## CONTEXT tier — 압축 흡수

| CONTEXT 개념 | 흡수 위치 | v2 처리 |
|---|---|---|
| constant / parameter / variable; primary vs secondary parameter | M1 | primary vs secondary parameter만 1문장으로 유지 |
| NCA vs compartmental modeling | M1 | "질문이 단순하면 NCA, 예측·비선형·PK/PD 정량화에는 모델"로 압축 |
| ADME, disposition, first-pass loss, bioavailability, enterohepatic cycling | M2 | PK phase가 exposure를 만드는 physiological chain이라는 1문장으로 압축 |
| route, dosage form, adherence, variability | M2 | therapeutic window를 흔드는 real-world input factors로 압축 |
| plasma/serum/whole blood, unbound concentration | M3 | response를 연결할 때 measurement matrix와 unbound concentration 조건으로 압축 |
| active metabolite / prodrug / stereoisomer | M3 | "측정한 농도 ≠ 활성 분자일 수 있음"으로 압축 |
| disease progression, placebo, biomarker/surrogate | M3/M4 | measured response 해석의 배경으로 압축 |

---

# §1 — Session Header & Roadmap

**Session title**: Pre-Sprint — 모델링 철학·용어
**Core question**: 모델링은 왜, 언제, 어떤 순서로 해야 하며, 그 결과를 어떻게 임상 용량 결정 언어로 번역할 것인가?

<!-- MASTER LENS -->
**Big Idea**: 모델링은 수식 fitting이 아니라 **임상 질문 → 설계 → 실험 → EDA → fitting → 진단**의 순환 사고다. PK/PD는 그 순환 안에서 **dose regimen을 exposure-time profile과 response-time profile로 번역하는 언어**다.
<!-- /MASTER LENS -->

## Roadmap

```text
M1. Modeling Carousel  ⚡ Apex Concept
    ├─ 왜 fitting부터 시작하면 안 되는가
    ├─ EDA가 initial estimate와 model structure를 만든다
    └─ 5대 dysfunction: EDA 경시, formula slavery, software overtrust,
       improper weighting, lack of holistic view

M2. PK/PD Linkage & Therapeutic Window
    ├─ dose regimen → exposure → desired/adverse effects
    ├─ empirical regimen design vs rational PK/PD approach
    └─ therapeutic window: efficacy와 harm 사이의 operating range

M3. Emax / C50 / Hill γ
    ├─ Emax: maximum response
    ├─ C50: potency
    └─ γ: steepness; titration-friendly vs threshold-like response

M4. Turnover
    ├─ steady state는 static state가 아니라 dynamic equilibrium
    ├─ Rt, Ass, kt, tt
    └─ concentration peak와 effect peak가 분리될 때 indirect response를 의심한다
```

**후속 개방**: M1은 GOF와 model selection, M2는 compartmental PK와 TDM, M3는 direct-effect PD, M4는 indirect-response/disease progression/TMDD downstream 모델로 이어진다.

---

# §2 — Concept Anatomy Cards

---

## Card M1 ⚡ Apex Concept — Modeling Carousel & 5대 Dysfunction [G pp.1–7]

<!-- MASTER LENS -->
### [개념 Big Idea: 거장의 시각]

**왜 결정적인가**: nonlinear model fitting은 parameter initial estimate를 요구한다. EDA 없이 fitting을 시작하면 model structure와 initial estimate가 데이터에서 나오지 않는다. 대신 사용자의 추측이나 software default가 출발점이 되고, 이때 local minimum에 수렴할 위험이 커진다. 핵심은 "fitting이 시작점이 아니다"라는 것이다.

**체화해야 할 단 하나의 직관**: Modeling Carousel에서 fitting은 6단계 중 5번째다. 앞의 네 단계 — tentative model, design, experiment, EDA — 가 먼저 model structure와 initial estimate의 근거를 만든다. 따라서 fitting 결과의 해석 가능성은 fitting 전에 상당 부분 결정된다.
<!-- /MASTER LENS -->

> **Mastery Note — [CRUCIBLE_DERIVED]**
> EDA의 역할은 "plot을 한 번 보는 단계"가 아니라 nonlinear fitting이 출발할 parameter-space basin(← 파라미터 탐색 공간)을 데이터 기반으로 좁히는 일이다. 따라서 Carousel의 앞 단계는 형식적 절차가 아니라 fitting을 해석 가능하게 만드는 사전 정보 생산이다.


### A. Formal Definition

**Modeling Carousel**은 성공적 모델링을 위한 순환 workflow다 [G p.4].

1. **Tentative model** — 실험 전 사전 가설과 tentative system model.
2. **Design** — dose, sampling time, response measurement, population, simulation/CATD.
3. **Run experiment** — 데이터 수집.
4. **Explore data (EDA)** — concentration-time, response-time, response-concentration plot으로 구조와 비선형성을 탐색.
5. **Fit model(s)** — 보통 nonlinear regression으로 parameter와 precision을 추정.
6. **Analyze output & model discrimination** — GOF, residual, parameter precision, validation, competing model 비교.

G Ch.1의 simple model은 dose $D$를 constant, $V$와 $Cl$을 primary parameter, $\hat C$와 $t$를 variable로 둔다. $K=Cl/V$, $AUC=D/Cl$, $t_{1/2}=\ln(2)/K$는 primary parameter에서 도출되는 secondary parameter다 [G pp.1–2].

**Equation block — one-compartment prediction / observation error [G pp.1–2]**

$$
\hat C = \frac{D}{V}\exp\left(-\frac{Cl}{V}t\right)
$$

$$
C = \hat C + \varepsilon
$$

### B. Why Model at All?

G Ch.1의 핵심은 "모델링을 많이 하라"가 아니라 **필요할 때만 하라**다. 질문이 bioavailability나 total clearance 같은 exposure summary라면 NCA가 충분할 수 있다. 반대로 single-dose에서 multiple-dose를 예측하거나, nonlinear kinetics를 다루거나, PK/PD 관계를 정량화해야 한다면 compartmental/PBPK-type model이 필요하다 [G p.4].

<!-- ANCHOR -->
즉, 모델은 지식 과시가 아니라 질문에 맞는 압축 장치다. "가장 복잡한 모델"이 아니라 "질문을 답하는 데 필요한 만큼만 복잡한 모델"이 원칙이다 [G pp.3–4].
<!-- /ANCHOR -->

### C. Structural Necessity

Step 4 EDA는 예쁜 그림을 만드는 단계가 아니다. Step 5 fitting에 들어갈 model structure와 initial estimate를 생산하는 단계다. G p.5–6은 EDA가 model structure와 initial estimates를 제안해야 하며, nonlinear fitting algorithm은 initial estimate를 필요로 한다고 설명한다.

G Fig.1.2는 clearance와 volume의 parameter space에서 objective function WRSS(← 가중 잔차 제곱합)가 여러 hollow를 가질 수 있음을 보여 준다. Yellow point는 possible initial estimate이고 red point는 final estimate다. 출발점이 나쁘면 local minimum으로 갈 수 있고, 좋은 initial estimate는 global minimum으로 가는 길을 열 수 있다 [G p.6].

<!-- TRENCH -->
**Trench-level tip [실무 추론]**: EDA의 산출물은 plot 자체가 아니라 "initial estimate 후보 1표 + nonlinearity yes/no 1줄"이다. Dose-normalized plot이 nonlinearity를 시사하면, 결론 전에 dataset의 dose/time/event coding 오류 가능성부터 배제한다.
<!-- /TRENCH -->

### C-2. Plausible Fallacy — [EXPERT_INFERENCE, v3]

**그럴싸한 오해**: "GOF가 좋게 나왔으니 모델이 옳다."

**왜 틀렸는가**: Fitting(Step 5)은 **가설 생성** 단계이고, simulation과 decision이 Carousel의 목적이다. Step 6 "Analyze output & model discrimination"은 fitting 이후에 반드시 따른다. VPC 없이 GOF만으로 diagnosis 단계를 건너뛰면, fitting이 만든 가설이 검증 없이 의사결정으로 직행한다. GOF plot은 fitted value가 observed value에 가깝다는 것만 보여 줄 뿐 — predictive validity는 별도로 평가해야 한다.

**실무에서 어떻게 드러나는가 (GOF-Only Submission Trap)**: VPC 없이 GOF만으로 규제 제출을 강행하면, 심사관이 model의 predictive performance를 확인할 수 없다는 이유로 deficiency letter를 발행하는 패턴으로 이어진다. Carousel의 diagnosis 단계(Step 6) 생략이 만드는 가장 흔한 규제 실패 모드다.

### D. Assumptions & Boundary Conditions

Modeling Carousel은 rich dataset과 실험 설계를 전제로 한 사고 순서다. Sparse data나 real-world data에서는 EDA의 해상도가 떨어질 수 있다. 이 경우 "모델이 설명한다"와 "데이터가 구분해 준다"를 분리해서 말해야 한다.

**Five common dysfunctions** [G p.4]

| Dysfunction | 압축 해석 |
|---|---|
| failure to appreciate EDA before fitting | fitting부터 돌리면 model structure와 initial estimate가 빈약해진다. |
| slavery to formulas | 수식을 외워도 biology와 data가 요구하는 구조를 보지 못한다. |
| too much trust in software | 수렴 메시지는 과학적 타당성 보증서가 아니다. |
| improper use of weighting | residual/error model을 잘못 두면 structural 판단도 흐려진다. |
| lack of holistic view | design, assay, biology, response timing을 함께 보지 못한다. |

### E. Limitations

이 장은 NONMEM convergence diagnostics나 covariance step 해석을 가르치는 장이 아니다. 따라서 "몇 개 initial estimate를 써야 하는가", "OFV 차이가 얼마면 충분한가" 같은 운영 기준은 이 카드에서 다루지 않는다. 원문 수준에서 잠글 메시지는 **different initial estimates로 rerun하여 local minimum 여부를 확인하라**는 원칙이다 [G p.6].

### F. Cognitive Lock

- **Formal**: model은 response variable이 predictor에 어떻게 의존하는지 표현한다.
- **Graphical**: concentration-time, response-time, response-concentration plot이 구조를 먼저 말한다.
- **Algorithmic**: nonlinear fitting은 initial estimate와 objective surface의 basin에 민감하다.
- **Biological**: model은 biology와 collected data가 drive해야 한다.
- **Practical**: fitting 전에 "질문, design, EDA, initial estimate"가 문서화되어야 한다.

**Diagnostic signature [실무 추론]**: **Premature Convergence Mirage** — EDA 없이 fitting부터 시작해 수렴은 했지만, model structure와 initial estimate의 근거가 빈약한 상태.

### G. Zettelkasten Atom

```yaml
aliases: [Modeling Carousel, EDA-first modeling, local minimum]
tags: [pharmacometrics/modeling, EDA, model-selection]
source: Gabrielsson & Weiner 5e Ch.1 pp.1-7
lock: Fitting is Step 5, not Step 1. EDA produces model structure and initial estimates.
```

<!-- RECAP -->
**M1 Recap**: 모델링의 첫 원칙은 software 실행이 아니라 질문과 데이터 구조를 먼저 보는 것이다. EDA를 건너뛴 fitting은 수렴할 수는 있어도, 왜 그 model이어야 하는지 설명하지 못한다.
<!-- /RECAP -->

> **▶ Practice Brief — M1 체화 4축 — [EXPERT_INFERENCE, v3]**
> - **왜 알아야 하는가**: Modeling Carousel 없이는 fitting 결과가 왜 그 형태인지 설명하지 못하고, model selection이 근거 없는 주관적 선택이 된다.
> - **흐름상 역할**: 이 카드는 후속 GOF, model selection, VPC 해석 세션의 사고 순서를 미리 잠그는 관문이다.
> - **체화 꿀팁**: "왜 EDA가 없으면 initial estimate를 만들 수 없는가"를 nonlinear fitting algorithm의 수학적 요구에서 스스로 도출할 수 있을 때 M1이 내재화된 것이다 — 암기가 아니라 구조적 필연에서 이유를 끌어내라.
> - **실무 활용**: 새 dataset을 받을 때 가장 먼저 dose-normalized concentration-time plot을 그리는 EDA 루틴이 곧 M1이 실무로 출력되는 형태다; 이 plot 없이 control stream부터 여는 것이 M1이 경고한 dysfunction이다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.6, Figure 1.2
Why this matters: This figure makes the local-minimum problem visible. It shows why EDA-derived initial estimates are not cosmetic; they determine which region of parameter space the fitting algorithm enters.
When to look: after reading Card M1, especially §C Structural Necessity
Learner instruction: Focus on the yellow starting points and the red final estimates. Ask which starting point would send the program to the wrong hollow and why EDA is the safeguard.
<!-- /FIGURE_POINTER -->

---

## Card M2 — PK/PD Linkage & Therapeutic Window [T pp.3–17]

<!-- MASTER LENS -->
### [개념 Big Idea: 거장의 시각]

**왜 결정적인가**: 임상 처방 질문은 "얼마나, 얼마나 자주, 얼마나 오래, 어떤 route와 dosage form으로 줄 것인가"다. 이 질문의 답은 dose 숫자 자체에 있지 않다. 대신, dose가 만든 exposure-time profile, 그리고 그 exposure가 만든 desired/adverse response-time profile로 답해야 한다 [T p.3].

**체화해야 할 단 하나의 직관**: PK와 PD는 두 개의 독립 과목이 아니라 하나의 causal chain이다. **Dosage regimen → exposure within body → desired/adverse effects**가 연결되어야 한다. 그래야 regimen을 왜 바꾸는지 설명할 수 있다.
<!-- /MASTER LENS -->

> **Practice Lens — [TEXTBOOK_DERIVED]**
> 용량 질문을 받을 때 먼저 dose 숫자를 고정하지 말고 exposure-time profile과 response-time profile을 분리해서 생각하라. 같은 regimen이라도 input, variability, adherence가 exposure를 바꾸면 therapeutic window 안에 머무는 시간도 달라진다.


### A. Formal Definition

**Pharmacokinetics**: dose, dosage form, dosing frequency, route 같은 input이 시간에 따른 concentration/exposure를 어떻게 만드는가.
**Pharmacodynamics**: concentration이 desired effect와 adverse effect를 시간에 따라 어떻게 만드는가 [T pp.4–5].

T Fig.1-3이 보여 주는 핵심은, conc-vs-time과 conc-vs-effect가 결합되어야 비로소 effect-vs-time이 만들어진다는 것이다. PK만으로는 "몸 안 농도가 어떻게 변하는가"만 알 수 있다. PD만으로는 "농도가 주어졌을 때 반응이 어떻게 변하는가"만 알 수 있다. 치료에는 둘의 link가 필요하다 [T p.5].

**PK phase context**: ADME, disposition, first-pass loss, bioavailability, enterohepatic cycling은 dose가 systemic exposure로 바뀌는 physiological chain의 component다 [T pp.26–33].

### B. Therapeutic Window

Therapeutic window는 exposure가 너무 낮으면 ineffective therapy가 되고, 너무 높으면 adverse effects가 증가한다는 전제 위에 놓인 operating range다 [T p.6].

<!-- ANCHOR -->
[해석/교육용 formalization] 실무적으로는 therapeutic window를 "therapeutic response probability가 충분하고 adverse-event probability가 지나치지 않은 exposure range"로 읽으면 된다. 단, 이 확률 집합 표기는 원문 수식이 아니라 교육용 formalization이다.
<!-- /ANCHOR -->

### C. Structural Necessity

T Ch.1은 empirical trial-and-error regimen design을 rational PK/PD approach와 대비한다. 예전에는 dose와 interval을 조정하고 desired/adverse effects를 관찰하면서 regimen을 개선했다. 그러나 이 방식만으로는 digoxin과 morphine regimen 차이의 원리를 설명하지 못한다 [T p.4].

Digoxin은 0.125–0.25 mg once daily로 쓰이는 반면, morphine sulfate는 10–50 mg을 하루 최대 6회까지 투여할 수 있다. 두 약물 모두 therapeutic window가 비교적 좁지만, morphine은 빠르게 제거되어 자주 투여가 필요하고, digoxin은 천천히 제거되어 once-daily가 가능하다 [T pp.4, 7].

**Key example — digoxin accumulation/digitalizing dose [T p.7]**
Digoxin을 낮은 daily dose로 주면 처음에는 ineffective할 수 있고, 높은 rate로 유지하면 나중에 toxic해질 수 있다. 그래서 초기에는 여러 small dose로 빠르게 therapeutic concentration에 도달시키고 이후 small daily dose로 유지하는 digitalizing dose 논리가 나온다.

### D. Why It Matters Clinically

Rowland & Tozer는 inappropriate drug use 때문에 병원 입원 환자의 약 5%가 입원한다는 예를 든다 [T p.4]. 이 통계가 시사하는 바는 단순한 약동학 지식의 유용성이 아니다. 핵심 메시지는 **regimen design의 안전성**이다.

PK/PD는 drug design, drug selection, dosage regimen design, protocol design, data interpretation, drug product performance 평가, individualized therapy initiation에도 쓰인다 [T p.20].

### E. Limitations & Real-World Distortions

- **Measured site problem**: site of action 농도는 대개 직접 측정하기 어렵고 plasma가 대리 site로 쓰인다 [T p.6].
- **Adherence problem**: prescribed regimen이 실제 exposure로 그대로 이어지지 않는다. Once-daily antihypertensive cohort에서 1년 말 처방약을 지속한 비율은 약 50%였다 [T p.12].
- **Variability problem**: phenytoin concentration variability, warfarin S-warfarin variability, G6PD/primaquine, debrisoquine/CYP2D6, terfenadine/ketoconazole 예시는 같은 regimen이 같은 exposure/response를 보장하지 않음을 보여 준다 [T pp.10–12].
- **Warfarin genetics correction**: 이 PDF 범위에서는 CYP2C9/CYP2C19 polymorphisms와 vitamin K epoxide reductase 기전이 언급된다. VKORC1 label은 이 범위의 원문 표현이 아니므로 사용하지 않는다 [T p.10].

<!-- TRENCH -->
**Trench-level tip [실무 추론]**: adherence monitoring이 약하면 apparent PK variability가 실제 missed dose의 artifact일 수 있다. 이때 model은 환자 생리 차이가 아니라 input history 오류를 variability로 흡수할 수 있다.
<!-- /TRENCH -->

### F. Zettelkasten Atom

```yaml
aliases: [PK/PD linkage, therapeutic window, input-response phases]
tags: [clinical-pharmacology/dosing, pharmacometrics/pkpd]
source: Rowland & Tozer 5e Ch.1 pp.3-17; Table 2-1 p.20
lock: Dose regimen is useful only after it is translated into exposure-time and response-time profiles.
```

<!-- RECAP -->
**M2 Recap**: PK/PD linkage의 핵심은 "dose가 아니라 concentration at the site of action이 response를 drive한다"는 점이다. Therapeutic window는 이 linkage가 임상적으로 작동해야 하는 안전 범위다.
<!-- /RECAP -->

> **▶ Practice Brief — M2 체화 4축 — [EXPERT_INFERENCE, v3]**
> - **왜 알아야 하는가**: PK/PD linkage를 놓치면 PK 파라미터를 추정하고도 dosing decision을 내릴 논리적 근거가 빠져 있게 된다 — 숫자만 있고 해석이 없는 상태다.
> - **흐름상 역할**: 이 카드는 compartmental PK, TDM, exposure-response 세션이 공유하는 dose→exposure→response 번역 문법을 선행 잠금한다.
> - **체화 꿀팁**: 어떤 처방을 볼 때 "이 dose가 만드는 exposure-time profile은 무엇이고, 그 profile이 therapeutic window 안에 머무는 시간은 얼마나 되는가"를 자동으로 묻게 되면 M2가 내재화된 신호다.
> - **실무 활용**: 규제 보고서에서 PK 섹션과 PD 섹션을 완전히 분리하지 않고 PK/PD linkage 섹션으로 연결하는 것이 M2가 실무 문서에서 나타나는 형태다.

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.5, Figure 1-3
Why this matters: This figure prevents the common mis-mapping of PK and PD as separate disciplines. It shows that therapeutically useful prediction requires the two relationships to be linked into an effect-time profile.
When to look: after reading Card M2, especially §A Formal Definition
Learner instruction: Trace the path from concentration vs time to concentration vs effect and then to effect vs time. Do not leave the figure until you can explain why either puzzle piece alone is insufficient for dosing.
<!-- /FIGURE_POINTER -->

---

## Card M3 — Emax / C50 / Hill γ [T pp.35–43]

<!-- MASTER LENS -->
### [개념 Big Idea: 거장의 시각]

**왜 결정적인가**: 농도-반응 관계를 말할 때 "효과가 증가한다"만으로는 부족하다. Emax는 ceiling을, C50은 potency를, γ는 curve steepness를 따로 보여 준다. 이 세 가지를 분리하지 못하면 dose titration, endpoint selection, safety margin 해석이 흐려진다.

**체화해야 할 단 하나의 직관**: C50이 낮다고 항상 좋은 약이 아니다. 같은 potency라도 Emax가 낮으면 충분한 clinical response에 도달하지 못할 수 있다. 또한 γ가 너무 크면 작은 농도 변화가 response threshold를 급격히 넘게 만든다 [T pp.40–43].
<!-- /MASTER LENS -->

> **Practice Lens — [CRUCIBLE_DERIVED]**
> γ는 curve-fitting parameter에 그치지 않는다. γ가 클수록 같은 C50 주변에서도 작은 concentration 변화가 response 판단을 더 크게 바꾸므로, titration-friendly response인지 threshold-like response인지 먼저 구분해야 한다.


### A. Formal Definition

**Graded response**는 concentration이 변할 때 response intensity가 연속적으로 변하는 반응이다. Ketamine 예시에서 S(+)-ketamine은 R(−)-ketamine보다 더 낮은 C50와 더 높은 maximum response를 보인다: S(+) C50 ≈ 0.7 mg/L, R(−) C50 ≈ 1.8 mg/L [T p.40].

**Equation block — Hill/Emax equation [T p.40]**

$$
E = \frac{E_{\max}\,C^{\gamma}}{C_{50}^{\gamma}+C^{\gamma}}
$$

- $E_{\max}$: maximum response.
- $C_{50}$: 50% of $E_{\max}$를 만드는 concentration.
- $\gamma$: steepness factor.

**Exposure-time anchor [T pp.21–22]**: single oral dose profile에서 $C_{\max}$는 maximum systemic exposure, $t_{\max}$는 그 시간, AUC는 total systemic exposure다. Fig.2-1의 예시는 $C_{\max}=96\,\mu g/L$, $t_{\max}=3.0$ hr이다.

### B. What γ Really Changes

T p.40은 $\gamma=1$이면 20%→80% response에 필요한 concentration 범위가 $0.25C_{50}$에서 $4C_{50}$, 즉 16-fold라고 설명한다. $\gamma=2$이면 $0.5C_{50}$에서 $2C_{50}$, 즉 4-fold로 압축된다.

$$
\gamma=1: C_{20}=0.25C_{50},\; C_{80}=4C_{50}
$$

$$
\gamma=2: C_{20}=0.5C_{50},\; C_{80}=2C_{50}
$$

일반적으로 $\gamma$는 1–3 사이에 있다. 그러나 매우 크면 minimal response와 maximal response 사이의 concentration range가 좁아진다. 그 결과 response가 all-or-none처럼 보일 수 있다 [T pp.40–41].

<!-- ANCHOR -->
$\gamma$는 단순한 곡선 모양이 아니라 처방 사고를 바꾼다. $\gamma \approx 1$이면 symptom-based titration이 상대적으로 자연스럽다. 반대로 반응이 가파르거나(steep) 역치형(threshold-like)이면 작은 농도 변화가 clinical event를 바꿀 수 있다.
<!-- /ANCHOR -->

### C. Real Data Anchors

**Key example — propranolol [T p.42]**
Exercise-induced tachycardia 감소율과 unbound propranolol concentration의 관계는 Hill equation에 잘 맞고, $\gamma \approx 1$, $E_{\max}\approx 40\%$, $C_{50}=5.3\,\mu g/L$로 제시된다.

**Key example — alfentanil quantal response [T pp.42–43]**
Alfentanil은 nitrous oxide anesthesia 중 satisfactory response의 cumulative frequency로 평가된다. C50는 breast 0.27 mg/L, lower abdomen 0.31 mg/L, upper abdomen 0.42 mg/L 순으로 증가한다. 이 예시는 γ를 추정한 graded curve가 아니다. 즉, quantal endpoint에서 response probability가 concentration과 어떻게 연결되는지 보여 주는 예시다.

### D. Measurement & Assay Boundaries

Total plasma/serum concentration에는 bound와 unbound drug가 모두 포함된다. 그러나 distribution, elimination, PD response는 unbound concentration에 의존한다. 다만 fraction unbound가 일정하면 total concentration으로도 충분할 수 있다. 반대로 saturable binding, displacement interaction, renal/hepatic disease, surgery, severe burns, pregnancy처럼 binding이 변하는 조건에서는 unbound concentration 측정이 중요해진다 [T p.21].

**Chemical entity boundary**: racemate, stereoisomer, active metabolite, prodrug에서는 "측정한 total parent concentration"이 실제 active moiety를 대표하지 못할 수 있다. Acenocoumarol, methylphenidate, aspirin/salicylic acid 예시는 assay specificity가 PK/PD link를 좌우한다 [T pp.23–25].

<!-- TRENCH -->
**Trench-level tip [실무 추론]**: dose range가 C50 주변에만 몰려 있고 plateau 정보가 없으면 γ를 자유롭게 estimate하기보다 parsimonious assumption을 먼저 검토한다. "γ를 estimate했다"는 사실보다 "데이터가 γ를 식별할 수 있는가"가 먼저다.
<!-- /TRENCH -->

### E. Limitations

Clinical $E_{\max}$는 pharmacological maximum보다 낮을 수 있다. 예를 들어 heart rate를 올리는 약물에서는 cardiovascular system이 먼저 악화될 수 있다. 그러면 pharmacological maximum에 도달하기 전에 안전성 한계가 온다. 따라서 agonist의 $E_{\max}$는 antagonist보다 임상적으로 정의하기 어렵다 [T p.41].

Fig.2-19의 메시지는 exposure metric 선택에도 적용된다. Chronic therapy에서는 duration above a minimum concentration이 중요할 수 있고, headache relief처럼 빠른 효과가 목적이면 $C_{\max}$와 $t_{\max}$가 더 중요할 수 있으며, 어떤 경우에는 total AUC가 더 관련 있을 수 있다 [T p.44].

### F. Diagnostic Lock

- **Graded response**: concentration 변화가 response intensity의 연속 변화로 이어진다.
- **Quantal response**: individual-level endpoint는 all-or-none이며, population-level cumulative frequency로 concentration-response를 본다.
- **Endpoint trap**: pharmacologic response는 graded인데 clinical endpoint가 threshold로 절단되어 quantal처럼 분석될 수 있다 [T p.43].
- **Diagnostic signature [실무 추론]**: **Hill γ Identifiability Collapse** — data range가 plateau와 low-response region을 충분히 포함하지 못해 γ 추정이 model보다 noise를 따라가는 상태.

### G. Zettelkasten Atom

```yaml
aliases: [Emax, C50, Hill equation, graded response, quantal response]
tags: [pharmacometrics/pd, exposure-response]
source: Rowland & Tozer 5e Ch.2 pp.35-43
lock: Emax is ceiling, C50 is potency, gamma is steepness; endpoint type decides how response should be modeled.
```

<!-- RECAP -->
**M3 Recap**: Hill equation은 농도-반응의 "현재 순간"을 정량화한다. 하지만 measured concentration, active moiety, endpoint type, γ 식별 가능성을 함께 보지 않으면 정확한 수식도 잘못된 dose 해석으로 이어진다.
<!-- /RECAP -->

> **▶ Practice Brief — M3 체화 4축 — [EXPERT_INFERENCE, v3]**
> - **왜 알아야 하는가**: Emax/C50/γ를 한 덩어리로 암기하면 endpoint type이 바뀔 때 모델 선택이 흔들리고, γ identifiability 문제를 인식하지 못한 채 noise를 parameter로 추정한다.
> - **흐름상 역할**: 이 카드는 direct-effect PD, exposure-response analysis, dose titration 설계 세션의 "천장-효능-가파름" 3축 언어를 선행 잠금한다.
> - **체화 꿀팁**: propranolol 예시($\gamma\approx1$, $C_{50}=5.3\,\mu g/L$)를 기준으로 γ 값을 2, 3으로 올리면 20%–80% response range가 어떻게 압축되는지 손으로 계산해 보면 — γ가 단순 exponent가 아니라 titration logic을 바꾼다는 것이 체감된다.
> - **실무 활용**: exposure-response 보고서에서 C50 하나만 보고하지 않고 Emax, γ, endpoint type(graded vs quantal)을 함께 명시하고 γ identifiability를 언급하는 것이 M3가 규제 문서에서 요구하는 수준이다.

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.41, Figure 2-16
Why this matters: This figure turns γ from an abstract exponent into a visible change in response sensitivity. It shows why the same C50 can behave very differently when steepness changes.
When to look: after reading Card M3, especially §B What γ Really Changes
Learner instruction: Compare the curves around C50, not only at the plateau. Then compare the 20–80% region to see why γ changes titration logic.
<!-- /FIGURE_POINTER -->

---

## Card M4 — Turnover: Pool Size · Rate · Fractional Rate · Time [T pp.44–46]

<!-- MASTER LENS -->
### [개념 Big Idea: 거장의 시각]

**왜 결정적인가**: 어떤 response는 drug concentration이 peak를 찍은 뒤 훨씬 늦게 나타난다. 이 지연은 단순 distribution delay일 수도 있고, endogenous system의 turnover 때문일 수도 있다. 둘을 구분하지 못하면 direct-effect Hill model로 설명할 수 없는 시간을 억지로 fitting하게 된다.

**체화해야 할 단 하나의 직관**: steady state는 움직이지 않는 상태가 아니다. **input rate와 output rate가 같아 pool size가 일정하게 보이는 dynamic equilibrium**이다 [T p.45]. 따라서 약물이 input을 바꾸는지 output을 바꾸는지에 따라 response time course가 달라진다.
<!-- /MASTER LENS -->

> **Judgment Lens — [CRUCIBLE_DERIVED]**
> 관찰 데이터에서 concentration peak와 effect peak가 분리되면, 단순 direct-effect 모델만으로 끝내기 전에 turnover/delay 사고를 켜야 한다. 이 판단은 모델을 복잡하게 만들기 위한 것이 아니라 response가 어느 system pool을 통해 나타나는지 묻는 출발점이다.


### A. Formal Definition

Turnover는 endogenous substance/system이 steady state에 있으면서 계속 renewal되고 elimination되는 현상이다. Oral anticoagulants, antihyperlipidemics, uricosuric agents, epoetin alfa는 모두 endogenous compound/system의 formation 또는 elimination을 바꿔 delayed response를 만들 수 있다 [T p.45].

**Equation block — turnover relationships [T p.45]**

$$
k_t = \frac{R_t}{A_{ss}}
$$

$$
t_t = \frac{A_{ss}}{R_t}
$$

$$
t_t = \frac{1}{k_t}
$$

- $A_{ss}$: pool size at steady state.
- $R_t$: turnover rate.
- $k_t$: fractional turnover rate.
- $t_t$: turnover time.

### B. Key Examples

**Key example — warfarin [T p.8]**
Warfarin sodium 1.5 mg/kg single oral dose를 5명의 male volunteers에게 투여했을 때, plasma warfarin concentration은 빠르게 올라가지만 prothrombin complex activity response는 느리게 변한다. 이 분리는 concentration-time profile만으로 response-time profile을 설명할 수 없음을 보여 준다.

**Key example — paclitaxel [T pp.8–9]**
Paclitaxel은 body에서 약 2일 내 제거되지만 leukocyte count 변화는 매우 느리며, nadir는 1주 이후에 나타나고 baseline 회복은 약 3주가 걸릴 수 있다. 이것이 turnover-driven response의 전형적 시그니처다.

**Key example — total body water [T pp.45–46]**
Total body water는 약 42 L이고, 평균 turnover rate는 2.5 L/day, fractional turnover rate는 0.06 day⁻¹, turnover time은 17 days다. Desert-like condition에서는 pool size가 거의 일정해도 turnover rate가 21 L/day까지 증가할 수 있고, 이때 fractional turnover rate는 0.5 day⁻¹, turnover time은 2 days가 된다.

### C. Structural Necessity

M3는 concentration과 response의 즉시적 또는 quasi-steady relationship을 다루지만, M4는 measured response가 endogenous pool의 변화를 반영할 때 필요하다. 판단 기준은 단순하다. **effect peak time이 concentration peak time과 분리되어 있으면 direct-effect Hill만으로 충분한지 의심한다**.

<!-- ANCHOR -->
Turnover modeling에서 더 중요한 질문은 "Rt, kt, tt 중 무엇을 외웠는가"가 아니다. 핵심 질문은 "이 system에서는 pool size가 보존되는가, fractional turnover가 보존되는가, 아니면 turnover rate 자체가 바뀌는가"다. Water 예시는 pool size가 feedback으로 유지될 수 있음을, cholesterol/WBC 예시는 pool size 자체가 변할 수 있음을 각각 보여 준다 [T p.46].
<!-- /ANCHOR -->

### D. Boundaries

이 장은 indirect response ODE coding을 제공하지 않는다. 이 카드에서 체화할 것은 equation template이 아니라 turnover parameter 간 관계와 delayed response의 원인이다. ODE, KIN/KOUT, baseline parameterization은 후속 PD modeling 세션으로 이연한다.

<!-- TRENCH -->
**Trench-level tip [실무 추론]**: sparse response-time data에서 input과 output을 동시에 자유롭게 추정하면 parameter가 서로 보상할 수 있다. 먼저 baseline, peak timing, recovery timing을 보고 어떤 turnover component가 데이터로 식별 가능한지 판단한다.
<!-- /TRENCH -->

### E. Diagnostic Lock

- **Turnover rate**가 크다고 process가 빠른 것은 아니다. pool size가 크면 큰 양이 오가도 fractional turnover는 느릴 수 있다.
- **Fractional turnover rate**와 **turnover time**이 process speed를 더 직접적으로 말한다.
- **Diagnostic signature [실무 추론]**: **Turnover-PD Mis-attribution** — delayed response를 PK distribution delay나 Hill γ 문제로만 설명하려는 상태.

### F. Zettelkasten Atom

```yaml
aliases: [Turnover, pool size, fractional turnover rate, turnover time]
tags: [pharmacometrics/indirect-response, physiology/dynamic-equilibrium]
source: Rowland & Tozer 5e Ch.2 pp.44-46
lock: Steady state is dynamic equilibrium; delayed response often means the measured system is turning over.
```

<!-- RECAP -->
**M4 Recap**: Turnover는 "반응이 늦다"를 수학적으로 다루기 전, 무엇이 천천히 바뀌고 있는지 묻는 생리학적 언어다. Concentration peak와 effect peak가 분리되면 M4 사고가 켜져야 한다.
<!-- /RECAP -->

> **▶ Practice Brief — M4 체화 4축 — [EXPERT_INFERENCE, v3]**
> - **왜 알아야 하는가**: turnover 개념 없이는 delayed response를 poor fit 또는 data 오류로 오해하고, indirect-response model이 필요한 시점을 놓친다.
> - **흐름상 역할**: 이 카드는 indirect-response model, disease progression model, TMDD downstream 세션이 공유하는 "effect peak delay의 원인 분류" 판단 기준을 선행 잠금한다.
> - **체화 꿀팁**: water turnover 예시의 수치($A_{ss}=42\,L$, $R_t=2.5\,L/day$ → $k_t=0.06\,day^{-1}$, $t_t=17\,days$)를 desert 조건($R_t=21\,L/day$ → $t_t=2\,days$)과 비교하며 pool size가 고정돼도 $k_t$와 $t_t$가 얼마나 크게 달라지는지 직접 손으로 계산하면 rate/fractional rate/time의 차이가 내재화된다.
> - **실무 활용**: PD 모델링 보고서에서 concentration peak와 effect peak의 시간 차이를 먼저 데이터로 기술하고, 그 차이가 turnover 구조 채택의 근거임을 명시하는 것이 M4가 실무 문서에서 나타나는 형태다.

---

## §2 Recap — 30-Second Diagnostic Grid

<!-- RECAP -->
새 PK/PD dataset을 처음 받은 30초에는 네 개 lens를 동시에 켜야 한다.

| Lens | 먼저 볼 것 | 즉시 판단할 것 |
|---|---|---|
| M1 | dose levels, sampling density, concentration-time plot | EDA가 model structure와 initial estimate를 줄 수 있는가? |
| M2 | regimen, route, adherence, measurement site | dose→exposure→response chain에서 빠진 link가 있는가? |
| M3 | plateau, C50 주변 coverage, endpoint type | Emax/C50/γ를 식별할 수 있는가, endpoint가 graded인가 quantal인가? |
| M4 | concentration peak vs effect peak timing | direct-effect model로 충분한가, turnover/delay 구조가 필요한가? |

이 grid의 목적은 control stream을 바로 쓰게 만드는 것이 아니다. 어떤 모델을 선택할 근거가 데이터에 있는지 먼저 묻는 것이다.
<!-- /RECAP -->

---

# §5 — Confusion Pair Dissection

## Pair 1 — Pharmacokinetics vs Pharmacodynamics

<!-- CONFUSION -->
| 구분 | Pharmacokinetics | Pharmacodynamics |
|---|---|---|
| 질문 | body가 drug에 무엇을 하는가? | drug가 body에 무엇을 하는가? |
| 축 | input → concentration-time | concentration → effect-time |
| 데이터 | plasma/serum/whole blood concentration, AUC, Cmax, tmax | desired/adverse response, biomarker, clinical endpoint |
| 실패 모드 | exposure를 dose와 동일시 | response를 concentration 없이 직접 dose와 연결 |

**Lock**: PK와 PD는 반대말이 아니다. 치료적으로 유용한 예측은 둘이 link될 때 비로소 가능하다 [T p.5].

**⚡ 기억 고리 (Memory Hook)**: PK는 *input → concentration* 의 화살표이고 PD는 *concentration → effect* 의 화살표다. 두 화살표는 **같은 선상의 앞뒤 화살표**이지 좌우의 반대 화살표가 아니다. 따라서 한쪽 화살표만 그리면 dose-to-effect 사슬이 끊겨 임상 의사결정이 멈춘다 [T p.5].
<!-- /CONFUSION -->

## Pair 2 ⚡ Critical Blow Applied — Graded Response vs Quantal Response

<!-- CONFUSION -->
| 구분 | Graded response | Quantal response |
|---|---|---|
| response 형태 | intensity가 연속적으로 변함 | individual endpoint가 all-or-none |
| 모델 감각 | Hill/Emax로 continuous response를 설명 | cumulative frequency/probability로 event를 설명 |
| 예시 | ketamine response, propranolol heart-rate reduction | alfentanil satisfactory anesthesia response |
| C50 의미 | 50% of Emax를 주는 concentration | population 50%에서 predetermined response가 나타나는 concentration |

**Critical Blow [교육용 가상 시나리오]**: Protocol의 primary endpoint가 "24시간 내 ≥50% pain reduction: Y/N" 같은 quantal endpoint인데, modeler가 continuous VAS score를 graded Hill model로만 분석하면, statistician의 binary endpoint 분석과 modeler의 exposure-response 분석이 서로 다른 dose를 지지할 수 있다. 문제는 Hill equation 자체가 아니다. 문제는 **endpoint scale과 modeling framework의 불일치**다.

> **Failure Mode — [CRUCIBLE_DERIVED]**
> quantal 자료를 개인별 graded curve처럼 읽으면 Hill equation의 문제가 아니라 endpoint 정의의 문제가 된다. 먼저 개체 수준 반응 크기인지, 집단 수준 발생확률인지 분리해야 한다.

<!-- /CONFUSION -->

## Pair 3 — Turnover Rate vs Fractional Turnover Rate

<!-- CONFUSION -->
| 구분 | Turnover rate $R_t$ | Fractional turnover rate $k_t$ |
|---|---|---|
| 정의 | 단위 시간당 input/output amount | pool size 대비 fractional replacement speed |
| 단위 | amount/time | time⁻¹ |
| 직관 | 얼마나 많이 바뀌는가 | 얼마나 빠르게 바뀌는가 |
| water 예시 | 2.5 L/day는 커 보임 | 0.06 day⁻¹, turnover time 17 days는 느린 process임을 보여 줌 |

**Lock**: $R_t$만 보면 큰 pool의 느린 turnover를 빠른 process로 오해할 수 있다. Speed는 $k_t$와 $t_t$가 더 잘 말한다 [T pp.45–46].
<!-- /CONFUSION -->

---

# §7 — Self-Test: Active Recall Module

<!-- SELF-TEST -->
## Q1. Modeling Carousel에서 fitting은 몇 번째 단계이며, 왜 그 앞 단계가 중요한가?

**Expected answer**: fitting은 Step 5다. Step 4 EDA가 model structure와 initial estimate를 제안하고, nonlinear fitting algorithm은 initial estimate에 민감하기 때문이다 [G pp.5–6].

## Q2. NCA가 충분한 질문과 compartmental model이 필요한 질문을 하나씩 들어라.

**Expected answer**: bioavailability 또는 total clearance summary가 목적이면 NCA가 충분할 수 있다. single-dose data로 multiple-dose 결과를 예측하거나 nonlinear kinetics 또는 PK/PD 관계를 정량화하려면 model이 필요하다 [G p.4].

## Q3. Therapeutic window를 dose가 아니라 exposure 관점에서 설명하라.

**Expected answer**: 너무 낮은 exposure는 ineffective therapy로, 너무 높은 exposure는 adverse effects 증가로 이어지며, 둘 사이에서 therapeutic response를 얻고 undue adverse effect를 피하는 exposure range가 therapeutic window다 [T p.6].

## Q4. Digoxin과 morphine regimen 차이를 "dose frequency 차이"가 아니라 PK/PD 원리로 설명하라.

**Expected answer**: 두 약물 모두 narrow window를 가질 수 있지만 morphine은 빠르게 제거되어 자주 투여가 필요하고, digoxin은 천천히 제거되어 once-daily가 가능하다. Digoxin은 빠른 도달과 유지가 분리되어 digitalizing dose + maintenance dose 논리가 나온다 [T pp.4, 7].

## Q5. $\gamma=1$과 $\gamma=2$에서 20–80% response concentration range는 어떻게 다른가?

**Expected answer**: $\gamma=1$이면 $0.25C_{50}$에서 $4C_{50}$까지 16-fold, $\gamma=2$이면 $0.5C_{50}$에서 $2C_{50}$까지 4-fold다 [T p.40].

## Q6. Propranolol과 alfentanil 예시가 각각 가르치는 것은 무엇인가?

**Expected answer**: Propranolol은 unbound concentration과 graded response가 Hill equation으로 설명되는 예시이며 $\gamma\approx1$, $E_{\max}\approx40\%$, $C_{50}=5.3\,\mu g/L$다. Alfentanil은 quantal response에서 C50가 population event probability의 기준이 됨을 보여 준다 [T pp.42–43].

## Q7. Concentration peak와 effect peak가 분리되어 있을 때, 어떤 사고가 켜져야 하는가?

**Expected answer**: direct-effect Hill만으로 충분한지 의심하고 turnover/delay 구조를 고려해야 한다. Warfarin과 paclitaxel은 concentration-time과 response-time이 분리되는 예시다 [T pp.8–9].

## Q8. $R_t=2.5$ L/day인 total body water turnover가 왜 "빠른 process"라고 단정할 수 없는가?

**Expected answer**: pool size가 42 L이므로 fractional turnover rate는 0.06 day⁻¹이고 turnover time은 17 days다. Amount/time이 커도 pool 대비 fraction이 작으면 process는 느리다 [T pp.45–46].

## Q9. Fig.2-19의 두 scenario가 exposure metric 선택에 주는 메시지는 무엇인가?

**Expected answer**: 같은 Cmax/tmax라도 decline 속도가 다르면 AUC와 duration이 달라질 수 있고, 같은 AUC라도 input 속도가 다르면 Cmax와 tmax가 달라진다. 어떤 metric이 중요한지는 clinical objective와 exposure-response relationship에 따라 달라진다 [T p.44].
<!-- /SELF-TEST -->

---

# §8 — Meta-Frame & Big Picture

## A. Positioning

<!-- MASTER LENS -->
이 세션의 목표는 "PK/PD 용어 암기"가 아니라 **후속 모델링 판단의 언어를 잠그는 것**이다. M1은 사고 순서를 정한다. M2는 임상 목적 함수를 정한다. M3는 농도-반응 형태를 정하고, M4는 시간 지연과 endogenous system을 해석한다.
<!-- /MASTER LENS -->

## B. Dependencies

- M1 없이 후속 GOF/diagnostic 세션으로 가면, software output을 model validity로 오해한다.
- M2 없이 compartmental PK로 가면, concentration-time curve를 임상 response와 분리해서 보게 된다.
- M3 없이 PD modeling으로 가면, potency, ceiling, steepness, endpoint type을 한 덩어리로 오해한다.
- M4 없이 indirect response로 가면, delayed response를 단순 distribution delay나 poor fit으로만 오해한다.

## C. Professional Lock — [EXPERT_INFERENCE, v3]

<!-- RECAP -->
이 세션의 원리를 구조적으로 내재화한 pharmacometrician이 새 dataset 앞에서 갖는 것은 다음 네 개다.

- **Modeling은 question-driven workflow다**: 질문 없이 시작하는 fitting은 답 없는 수식이다. 데이터를 받는 순간 "무엇을 결정하기 위한 모델인가"를 먼저 쓸 수 있어야 한다. 이 한 줄이 없으면 EDA, fitting, diagnosis의 모든 단계가 목적지 없는 출력이 된다.
- **PK/PD의 핵심 번역 좌표**: dose → exposure → response. 이 세 좌표 사이 어디에서 개체간 변이가 생기는지 식별하는 것이 거장의 첫 진단이다. PK variability인지 PD variability인지 구분하지 못하면 covariate 탐색을 엉뚱한 layer에서 하게 된다.
- **Emax/Hill은 "천장-효능-가파름"의 3축 문법이다**: 이 셋을 분리하지 못하면 exposure-response 해석이 무너진다. C50만 보고하는 보고서는 ceiling과 steepness 정보를 버린 것이다. γ의 identifiability 문제를 모르면 noise를 parameter로 오인한다.
- **Turnover는 "지연된 상태"의 첫 번째 문법이다**: 반응이 늦는 이유가 distribution lag인지 endogenous system dynamics인지를 구분하는 관문이다. 이 구분이 없으면 indirect-response model 채택의 근거를 설명할 수 없고, delayed response를 poor fit이나 outlier로 오해하게 된다.
<!-- /RECAP -->

---

## PART B — Compiler-Only Appendix

This appendix is not learner-facing. It exists only to protect Phase 5 rendering fidelity and prevent regression.

### B0. Compression Lineage Note (relocated from PART A §8.D in ver1)

Content Lock v2는 Content Lock v1의 구조와 사실관계를 유지하면서 가독성과 최소 annotation만 보강했다. 4A 압축 단계에서 다음 항목은 이미 삭제 또는 압축되었다. 이 표는 Phase 5가 본문에서 우연히 다시 부활시키는 일을 막기 위한 회귀 방지 가드레일이다 (학습자에게 노출하지 않는다).

| 삭제/압축 항목 | 처리 |
|---|---|
| local minimum·regulatory overclaim | 위험 수준으로 완화; unsupported 정량 삭제 |
| AUC 30–50%, OFV>5, 4 initial estimates, COV/Hessian | 삭제 |
| CYP2C9·VKORC1 | CYP2C9/CYP2C19 + vitamin K epoxide reductase로 정정 |
| ADME/route/assay/stereoisomer context | 1–2문장으로 압축 |
| Hill code / NONMEM `$DES` template | 삭제; 후속 implementation 세션으로 이연 |
| Hb-O2, Michaelis-Menten/Langmuir, AI/regulatory meta-claims | PDF 범위 외이므로 삭제 |
| self-test의 unsupported hypothetical quantitative claims | 삭제 또는 source-grounded question으로 교체 |

### B1. Compilation Contract

- PART A is the only learner-facing body.
- Phase 5 must render PART A without altering scientific content, source page tags, equations, figure marker content, or mastery-note labels.
- PART B is instruction/guardrail only.
- Do not restore deprecated material.
- Do not add new scientific content.
- Do not render PART B as learner content unless explicitly requested.
- The `00_Content Lock v2` processing record, `Adjudication Table Summary`, and the original PART A `§8.D Compression Compliance Note` (now relocated as B0) are excluded from PART A because PART A must not contain process/audit tables; their regression-prevention function is preserved here in PART B.

### B2. Figure Rendering Instructions

| # | Mode | Source | Phase 5 rendering |
|---|---|---|---|
| 1 | P / FIGURE_POINTER | Gabrielsson & Weiner 5e, p.6, Figure 1.2 | Text-only pointer callout; do not embed or redraw textbook image. |
| 2 | P / FIGURE_POINTER | Rowland & Tozer 5e, p.5, Figure 1-3 | Text-only pointer callout; do not embed or redraw textbook image. |
| 3 | P / FIGURE_POINTER | Rowland & Tozer 5e, p.41, Figure 2-16 | Text-only pointer callout; do not embed or redraw textbook image. |
| R1–R4 | Rejected | G Fig.1.1; T Fig.1-4; T Fig.2-11; T Fig.1-6/Fig.2-20 | Do not restore unless Phase 4C is formally reopened. |

Global figure rules:
- Image rights = None.
- Do not embed copyrighted textbook images.
- Render every `FIGURE_POINTER` as a compact text-only callout with Source / Why this matters / When to look / Learner instruction.
- ver2 reformatting note: each FIGURE_POINTER block now uses one field per line (no inline `<br>` tags). The Phase 5 parser should detect the `FIGURE_POINTER` open/close markers and read the four fields by label prefix (`Source:`, `Why this matters:`, `When to look:`, `Learner instruction:`).
- Do not propose new figures.
- Do not generate Mermaid/SVG in Phase 4D.
- Phase 5 must not create a new figure from rejected candidates unless Phase 4C is formally reopened.

### B3. Page Tag Rendering Rules

- Preserve all `[p.XX]`, `[pp.XX–YY]`, `[pp.XX, YY]`, and `[p.확인 필요]` tags exactly as present in PART A.
- Render standard source tags as `<span class="source-page">[p.XX]</span>`.
- Render uncertain source tags as `<span class="source-page source-uncertain">[p.확인 필요]</span>`.
- Do not fabricate, delete, renumber, or relocate page tags.
- Do not apply page-tag detection inside code blocks or inside `FIGURE_POINTER` marker blocks.
- Source page tags must remain visible in print mode.

### B4. HTML Compiler Requirements

#### B4-1. Marker → Component Mapping

| Marker / Pattern | HTML Component | Requirement |
|---|---|---|
| `<!-- MASTER LENS -->` | Callout box | gold left border, subtle gold background |
| `<!-- ANNOTATION -->` | Inline abbr/tooltip style | muted italic text |
| `<!-- ANCHOR -->` | Bridge sentence | italic muted text |
| `<!-- TRENCH -->` | Practical tip box | rose left border/background tint |
| `<!-- CONFUSION -->` | Side-by-side comparison | amber comparison styling |
| `<!-- SELF-TEST -->` | Click-to-reveal accordion | question visible, answer hidden by default |
| `<!-- RECAP -->` | Section summary box | blue left border/background tint |
| `[확인 필요]` | Highlight flag | `<mark>` |
| `[p.XX]`, `[pp.XX–YY]`, `[pp.XX, YY]` | Source page tag | `<span class="source-page">...</span>` |
| `[p.확인 필요]` | Uncertain page tag | `<span class="source-page source-uncertain">...</span>` |
| `<!-- FIGURE_POINTER -->` | Textbook reference callout | text-only pointer with Source / Why / When / Learner instruction (parse by line, label-prefixed) |

#### B4-2. Navigation Anchor Integrity Rules

- HTML must include a sticky left sidebar table of contents.
- Use only `<a href="#...">` links.
- Every sidebar target must have exactly one matching body `id`.
- Every major section heading (§1, §2, §5, §7, §8) must receive a stable id.
- Every §2 concept card should receive a stable id when possible.
- Do not create duplicate ids.
- Enable `html { scroll-behavior: smooth; }`.
- Before finalizing Phase 5 HTML, count all sidebar href targets, confirm each exists exactly once, and fix any mismatch before output.
- Desktop: left sticky sidebar; mobile: sidebar may collapse but anchor navigation must still work.

#### B4-3. General Rendering Requirements

- Render content; do not alter PART A scientific text or page-tag text.
- Output a single self-contained HTML file with inline custom CSS and JS.
- Permitted external runtime dependencies only: MathJax CDN, Mermaid CDN, and cdnjs.cloudflare.com libraries such as highlight.js.
- MathJax must support inline `\(...\)` and display `\[...\]` / `$$...$$` math as needed.
- Code blocks: dark background, language classes where available, copy button.
- Self-test answers: hidden by default and revealed only on user interaction.
- Checklist state may persist with sessionStorage.
- Include print/PDF button using `window.print()`.
- Responsive: ≤768px single-column/collapsed nav; ≥1024px two-column layout.
- Dark/light: use `prefers-color-scheme`.
- Print: remove decorative backgrounds and hide navigation, but source page tags must remain visible.
- Do not generate Mermaid/SVG for this Phase 4D file; Phase 5 may render only approved markers and must not create new figures.

#### B4-4. Prohibited in Phase 5

- Do not embed copyrighted textbook images.
- Do not reproduce textbook figures exactly.
- Do not add, delete, renumber, or relocate page tags.
- Do not render markers as plain text.
- Do not expose self-test answers by default.
- Do not use `<iframe>` or `<embed>`.
- Do not use external local `.css`, `.js`, font, or image files unless explicitly supplied.
- Do not create sidebar TOC links whose target ids do not exist.
- Do not create duplicate body ids.
- Do not proceed if PATCH MODE splice verification fails.
- Do not restore material rejected by Audit/Content Lock/Phase 4C.
- Do not render the B0 Compression Lineage Note as learner content.

### B5. Audit Guardrails

Known forbidden restorations:
- "EDA 누락이 가장 빈번" as a ranked claim; retain only as one of five common dysfunctions.
- "반드시 local minimum" or deterministic failure claims; retain risk-level language.
- Unsupported FIH dose recommendation or FDA/EMA reviewer overclaims.
- Unsupported numerical values: AUC 30–50%, OFV>5, 4+ initial estimates, 6–12 month delay, large financial estimates.
- Misreading G Fig.1.2: A/B/C are possible initial estimates; D/E are final estimates; E is not a possible initial estimate.
- Recasting G Fig.1.2 as NONMEM OFV with thresholds; source-fidelity wording is WRSS/objective function.
- Digoxin/morphine "50-fold" frequency claim; retain only that dosing amount/frequency differs greatly.
- Unsupported CYP2C9/VKORC1 wording for this PDF range; use the corrected wording already locked in Content Lock.
- Hb-O2 γ≈2.7, Michaelis-Menten/Langmuir isomorphism, unapproved NONMEM/nlmixr2 code blocks, turnover ODE template.
- Any unapproved figure embedding or new figure proposal.

### B6. Crucible Guardrails

- Crucible is a guardrail and insight-preservation source, not raw prose for uncontrolled expansion.
- Preserve only adopted or explicitly allowed Grade A logic.
- Keep expert intuition short, labeled, and adjacent to existing concepts.
- Do not convert speculative or reviewer-style insight into textbook fact.
- Do not reintroduce rejected diagnostic thresholds, long dialogic scenarios, or external workflow details.

### B7. Deprecated and Forbidden Restorations

- `00_step1_draft_v0.md` is deprecated.
- Do not use Step 1 Draft v0 as learner-body source except through the Micro-Patch Gate.
- Do not restore rejected overclaims, unsupported numbers, unsupported regulatory claims, source-unsupported examples, unapproved code, or unapproved figures.
- Do not treat Patch Memo as an independent source; it is only an audit-attention guide.
- Do not broaden this Pre-Sprint beyond G p.1–7 and T p.3–49.

### B8. PATCH MODE Splice Verification Table

ver2 anchors are unchanged from ver1 because the three card title strings were not modified. v3.1 Korean Readability Patches do not alter anchor strings.

| Marker # | Anchor text | Anchor found? | Match count | Inserted? | Final location (§ + card) |
|---|---|---|---|---|---|
| 1 | `## Card M1 ⚡ Apex Concept — Modeling Carousel & 5대 Dysfuncti` | YES | 1 | YES | §2 → Card M1 |
| 2 | `## Card M2 — PK/PD Linkage & Therapeutic Window [T pp.3–17]` | YES | 1 | YES | §2 → Card M2 |
| 3 | `## Card M3 — Emax / C50 / Hill γ [T pp.35–43]` | YES | 1 | YES | §2 → Card M3 |

### B9. Zero-Omission Coverage Matrix (v3.1 re-verified)

| Domain | Required item | Evidence in PART A | Status | Action |
|---|---|---|---|---|
| C1 Scope concepts | M1 Modeling Carousel & 5대 dysfunction | §2 Card M1 | PRESENT | None |
| C1 Scope concepts | M2 PK/PD Linkage & Therapeutic Window | §2 Card M2 | PRESENT | None |
| C1 Scope concepts | M3 Emax / C50 / Hill γ | §2 Card M3 | PRESENT | None |
| C1 Scope concepts | M4 Turnover | §2 Card M4 | PRESENT | None |
| C1 Chapter role | Pre-Sprint epistemic foundation for later PopPK sessions | §1 Roadmap, §8 Meta-Frame | PRESENT | None |
| C2 Required data anchors | warfarin 1.5 mg/kg, propranolol C50=5.3 µg/L, alfentanil 0.27/0.31/0.42 mg/L, total body water 2.5 L/day / 0.06 day⁻¹ / 17 days | §2 M3/M4 and §7 questions retain these anchors | PRESENT | None |
| C2 Additional anchors | digoxin/morphine regimen contrast; Cmax=96 µg/L and tmax=3.0 hr; Fig.2-19 exposure-metric bridge | §2 M2/M3 and §7 | PRESENT_COMPRESSED | None |
| C3 Audit corrections | Overclaims softened; unsupported numerical thresholds and external claims not restored; G Fig.1.2 interpreted as WRSS/objective surface with initial/final estimates | §2 M1, PART B Audit Guardrails | PRESENT | None |
| C4 Audit T5 findings | NCA vs model need, empirical vs rational regimen design, digitalizing dose logic, Table 2-1 applications, Cmax/tmax/AUC bridge, graded/quantal distinction | §2 M1–M3, §5 Pair 2, §7 | PRESENT_COMPRESSED | None |
| C5 Figure coverage | Approved KEEP figures #1–#3 present exactly once as FIGURE_POINTER (ver2 reformatted to one-field-per-line); rejected R1–R4 not restored | PART A figure markers; PART B figure table | PRESENT | None |
| C6 Page tag integrity | Existing [p.XX]/[pp.XX–YY] tags preserved; no new page tags created by mastery notes, ver2 changes, v3 patches, or v3.1 Korean Readability Patches | PART A body | PRESENT | None |
| C7 Crucible Grade A preservation | Carousel as nonlinear-fitting necessity, M3 vs M4 entry rule, γ as response sensitivity, endpoint-scale warning | Mastery notes and §2/§5/§8 body | PRESENT_COMPRESSED | None |
| C8 Deprecated draft regression | Unsupported FIH/FDA claims, AUC 30–50%, OFV>5, 4-starting-value rule, CYP2C9/VKORC1 unsupported wording, unapproved code blocks not restored | PART B forbidden restoration list | PRESENT | None |
| C9 Canonical integrity | Content Lock v2 learner body preserved except approved figure pointer splices, the bounded Mastery Augmentation Layer, ver2 assembly edits, v3 labeled augmentations (Plausible Fallacy, Practice Briefs, §8C expansion, Memory Hook label), and v3.1 Korean Readability Patches | PART A; logs below | PRESENT | None |
| C10 Learner-Standalone (v3) | PART A contains no audit/process/compiler appendix text; all v3 additions are learner-facing augmentations in PART A; v3.1 patches improve Korean prose readability of existing learner content only | PART A inspection | PRESENT | None |
| C11 v3 Apex standardization | `[⚡ Apex Concept]` label is on M1 heading (existing) and C-2 Plausible Fallacy block is present | §2 Card M1 | PRESENT | None |
| C12 v3 Memory Hook label | `**⚡ 기억 고리 (Memory Hook)**` standardized in §5 Pair 1 | §5 Pair 1 | PRESENT | None |
| C13 v3 Professional Moat | §8.C expanded to 4 structural competency bullets, labeled [EXPERT_INFERENCE, v3] | §8.C | PRESENT | None |
| C14 v3 Practice Briefs | Practice Brief 4축 block present in each M1–M4 card, labeled [EXPERT_INFERENCE, v3] | §2 Cards M1–M4 | PRESENT | None |
| C15 v3.1 Korean Readability Patches | 13 Low-risk prose patches applied (P-001 ~ P-013): WRSS gloss, parameter-space basin gloss, "이 Content Lock" → "이 카드", "dose가" sentence connector, "T Fig.1-3" flow, "이 통계가 시사하는 바는", steep/threshold-like gloss, "즉," connector, "Entry rule" → "판단 기준", "원문에서 잠글 것은" → "이 카드에서 체화할 것은", "각각 보여 준다", "권리가" → "근거가", "치료적으로 유용한 예측은" | §2 Cards M1–M4, §2 Recap, §5 Pair 1 | PRESENT | None |

### B10. Micro-Patch Log

ver1 had no scientific micro-patches. ver2 also introduces no scientific micro-patches; the changes below are assembly-only. v3 introduces labeled interpretive augmentations (no scientific content change). v3.1 introduces Korean Readability Patches only (no scientific content change).

| Δ | Type | Description | Source-boundary impact |
|---|---|---|---|
| Δ1 | Relocation | §8.D Compression Compliance Note moved from PART A to PART B as B0 | None — text identical, location only |
| Δ2 | Re-formatting | Three FIGURE_POINTER blocks reformatted: inline `<br>` separators replaced with newlines (one field per line) | None — fields and content identical |
| Δ3 | Bounded addition | One memory-hook line added to §5 Pair 1 paraphrasing the existing T p.5 Lock statement (PK and PD as forward-chained arrows) | None — no new number, page tag, example, or external claim; paraphrases existing PDF-grounded statement |
| Δ4 | Visual cue | "⚡ Apex Concept" tag added next to "M1. Modeling Carousel" in the §1 Roadmap, matching the existing M1 card heading | None — visual consistency with existing card heading |
| Δ5 | Metadata | Certification table, Coverage Matrix, Mastery Augmentation Log, and Final Checklist updated to reflect ver2 state | None |
| Δ6 | Interpretive addition | `### C-2. Plausible Fallacy` block added to Card M1 between §C and §D: overt mis-assumption, mechanistic rebuttal, GOF-Only Submission Trap diagnostic signature. Labeled [EXPERT_INFERENCE, v3]. | None — paraphrases existing Carousel step-6 logic; no new page tag, equation, drug example, or external claim |
| Δ7 | Label standardization | §5 Pair 1 memory hook label changed from `**⚡ 기억 고리**:` to `**⚡ 기억 고리 (Memory Hook)**:` — content unchanged | None |
| Δ8 | Interpretive expansion | §8.C Professional Lock expanded from single sentence to 4-bullet block. Labeled [EXPERT_INFERENCE, v3]. | None — derived entirely from existing M1–M4 concepts in PART A; no new page tags or equations |
| Δ9 | Interpretive addition | `▶ Practice Brief — M[N] 체화 4축` block added at end of each M1–M4 card (after RECAP, before `---`). Labeled [EXPERT_INFERENCE, v3]. 4 lines each. | None — derived from existing card content; no new page tags, equations, or drug examples |
| Δ10 | Metadata | v3 Change Log, Certification table, Coverage Matrix, Mastery Augmentation Log, and Final Checklist updated to reflect v3 state | None |
| Δ11 | Korean Readability Patch | 13 Low-risk PART A prose patches (P-001 ~ P-013) applied: P-001 WRSS first-use gloss (M1 §C); P-002 parameter-space basin first-use gloss (M1 Mastery Note); P-003 "이 Content Lock" → "이 카드" tone smoothing (M1 §E); P-004 "dose가" → "대신, dose가" sentence connector (M2 Big Idea); P-005 "T Fig.1-3의 핵심은" flow improvement (M2 §A); P-006 "이 숫자가 말하는 것은" → "이 통계가 시사하는 바는" (M2 §D); P-007 "steep/threshold-like response이면" → Korean gloss (M3 §B ANCHOR); P-008 "즉," concept-clarification connector (M3 §C); P-009 "Entry rule은 단순하다" → "판단 기준은 단순하다" (M4 §C); P-010 "원문에서 잠글 것은" → "이 카드에서 체화할 것은" tone smoothing (M4 §D); P-011 "각각 보여 준다" parallel-structure clarification (M4 §C ANCHOR); P-012 "권리가" → "근거가" (§2 Recap); P-013 "치료적으로 유용해지는 지점은" → "치료적으로 유용한 예측은 ... 비로소 가능하다" (§5 Pair 1 Lock). | None — sentence-level Korean prose only; no new page tag, equation, numerical value, drug example, figure decision, or external claim. All anchor strings unchanged. PATCH MODE Splice Verification Table (B8) unaffected. |

No page tags were created, deleted, or corrected in v3.1. No equations were modified. No figures were added, removed, or altered. No examples or numerical anchors were added or removed.

### B11. Mastery Augmentation Log

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
|---|---|---|---|---|---|---|
| 1 | §2 Card M1 | Type M / W | YES | CRUCIBLE_DERIVED | Converts EDA from a procedural step into a parameter-space/optimization mental model. | Low |
| 2 | §2 Card M2 | Type J | YES | TEXTBOOK_DERIVED | Reinforces dose→exposure→response translation without adding examples or numbers. | Low |
| 3 | §2 Card M3 | Type J | YES | CRUCIBLE_DERIVED | Connects γ to titration vs threshold-like response judgment. | Low |
| 4 | §2 Card M4 | Type J | YES | CRUCIBLE_DERIVED | Makes concentration/effect peak separation the entry cue for turnover/delay thinking. | Low |
| 5 | §5 Pair 2 | Type F | YES | CRUCIBLE_DERIVED | Prevents endpoint-scale mismatch between graded and quantal response. | Low |
| 6 (ver2) | §5 Pair 1 | Memory-hook structural encoder | YES | TEXTBOOK_DERIVED (paraphrased from T p.5) | Encodes the structural reason PK and PD must be linked: they are forward-chained arrows on the same axis, not opposing arrows on different axes. | Low — uses existing PDF-grounded statement; no new number, example, or page tag |
| 7 (v3) | §2 Card M1, §C–D boundary | Plausible Fallacy block | YES | EXPERT_INFERENCE, v3 | Inoculates against the most common modeling over-confidence: conflating GOF with predictive validity; names GOF-Only Submission Trap as diagnostic signature. | Low — paraphrases existing Carousel step logic; no new page tags or equations |
| 8 (v3) | §5 Pair 1 | Label standardization | YES | EXPERT_INFERENCE, v3 | Standardizes memory hook label to `**⚡ 기억 고리 (Memory Hook)**` for V5.0 compliance. Content unchanged. | Minimal |
| 9 (v3) | §8.C | Professional Moat 4-bullet expansion | YES | EXPERT_INFERENCE, v3 | Converts single-sentence lock into 4 structurally distinct competency bullets covering question-driven workflow, translation axes, Hill grammar, and turnover gate. | Low — all derived from M1–M4 existing content |
| 10 (v3) | §2 Cards M1–M4 | Practice Brief 4-axis blocks (×4) | YES | EXPERT_INFERENCE, v3 | Adds "왜-흐름-꿀팁-실무" axis to each card for deeper active engagement and concrete activation route. | Low — derived entirely from existing card content |
| 11 (v3.1) | §2 Cards M1–M4, §2 Recap, §5 Pair 1 | Korean Readability Patches (13 Low-risk) | YES | KOREAN_PROSE_POLISH, v3.1 | Improves learner-facing Korean prose readability via first-use glosses, sentence connectors, parallel-structure clarification, and tone smoothing. No mastery content added. | Low — sentence-level prose only; all 13 patches independently audited; no scientific content, page tag, equation, figure marker, or anchor string altered |

#### Rejected or deferred augmentation candidates

| Rejected candidate | Reason for rejection |
|---|---|
| Add explicit OFV/RSE/condition-number thresholds | Rejected: unsupported numerical or diagnostic thresholds outside PDF/Audit-allowed content. |
| Add new clinical or regulatory examples | Rejected: would introduce external examples and source-boundary risk. |
| Add a fourth figure pointer for M4 | Rejected: Phase 4C budget exceeded; R4 was explicitly rejected. |
| Add Mermaid/SVG schematic at Phase 4D | Rejected: Phase 4D is not Phase 5 and image rights are None. |
| Add a §7 Q10 boss dilemma (Socratic) | Deferred: ver1 Self-Test (Q1–Q9) was finalized through Phase 4B-2 and not flagged by Audit/Crucible. Adding a new question now would risk creating new content; out of scope for ver2 assembly fix and v3.1 readability patch. |

## Final Checklist (v3.1)

| Check | Status |
|---|---|
| PART A alone is learner-facing and complete | PASS — all v3.1 patches refine learner-facing PART A prose; PART B is compiler-only |
| PART A contains no audit/process/compiler appendix text | PASS — P-003 and P-010 specifically removed residual process-language phrases ("이 Content Lock에서", "원문에서 잠글 것은") that had leaked from process to learner context |
| Approved figure markers are present exactly once | PASS — 3 markers, one-field-per-line format, content unchanged by v3.1 |
| No unapproved figure markers were added | PASS |
| Source page tags were preserved; no new page tags were fabricated | PASS — v3.1 patches added zero new page tags; all [G p.X], [T p.X], [T pp.X–Y] tags preserved verbatim |
| Audit/Crucible were not used as uncontrolled raw prose sources | PASS |
| Deprecated Step 1 Draft v0 material was not restored | PASS |
| Mastery augmentations are labeled and within B-Standard budget | PASS — 6 ver1/ver2 augmentations + 4 v3 augmentations + 1 v3.1 patch group; all properly labeled |
| No unsupported numerical values, new examples, equations, or page tags were introduced | PASS |
| PART B contains Phase 5 rendering requirements and navigation anchor integrity rules | PASS |
| No HTML, Mermaid, SVG, or image embed generated in Phase 4D | PASS |
| v3.1 changes are Korean prose readability patches only and do not alter scientific content, equations, or page tags | PASS |
| §5 Pair 1 has a structural memory hook with standardized label `**⚡ 기억 고리 (Memory Hook)**` (v3) | PASS |
| §1 Roadmap shows Apex visual cue consistent with M1 card heading | PASS |
| FIGURE_POINTER blocks parseable line-by-line by Phase 5 | PASS |
| Card M1 has `[⚡ Apex Concept]` in heading AND `C-2 Plausible Fallacy` block (v3) | PASS |
| §8.C Professional Lock expanded to 4-bullet block labeled [EXPERT_INFERENCE, v3] (v3) | PASS |
| Cards M1–M4 each have Practice Brief 4축 block labeled [EXPERT_INFERENCE, v3] (v3) | PASS |
| 13 v3.1 Korean Readability Patches applied surgically; all anchors unchanged (v3.1) | PASS |

---

## v3.1 Final Checklist

| # | Criterion | Status | 근거 |
|---|---|---|---|
| 1 | **PART A readability improved** | **PASS** | 13 Low-risk patches applied (P-001 ~ P-013) covering 2 first-use glosses, 2 tone smoothing edits, 7 Korean flow improvements, 1 first-use gloss with flow improvement, 1 concept-clarification connector. Coverage spans M1 (3 patches), M2 (3 patches), M3 (2 patches), M4 (3 patches), §2 Recap (1 patch), §5 Pair 1 (1 patch). Korean readability is improved without altering meaning, register, or technical precision. |
| 2 | **Scientific content unchanged** | **PASS** | All scientific claims, drug examples (warfarin, paclitaxel, propranolol, alfentanil, ketamine, digoxin, morphine, total body water), numerical anchors ($C_{50}=5.3\,\mu g/L$, $C_{\max}=96\,\mu g/L$, 1.5 mg/kg, 0.27/0.31/0.42 mg/L, 42 L, 2.5 L/day, 0.06 day⁻¹, 17 days, etc.), parameter relationships, and conceptual definitions are preserved verbatim. v3.1 patches operate at sentence-level Korean prose only. |
| 3 | **Equations preserved** | **PASS** | All MathJax equations preserved exactly: one-compartment prediction $\hat C = \frac{D}{V}\exp(-\frac{Cl}{V}t)$, observation error $C = \hat C + \varepsilon$, Hill/Emax $E = \frac{E_{\max}\,C^{\gamma}}{C_{50}^{\gamma}+C^{\gamma}}$, γ=1/γ=2 range expressions, turnover relations $k_t = R_t/A_{ss}$, $t_t = A_{ss}/R_t$, $t_t = 1/k_t$. Inline math ($\gamma$, $C_{50}$, $E_{\max}$, $R_t$, $A_{ss}$, $k_t$, $t_t$) preserved. |
| 4 | **Page tags preserved** | **PASS** | All page tags preserved verbatim and at original locations: [G pp.1–7], [G pp.1–2], [G pp.3–4], [G p.4], [G p.6], [T p.3], [T p.4], [T p.5], [T p.6], [T p.7], [T pp.4, 7], [T p.8], [T pp.8–9], [T pp.10–12], [T p.10], [T p.12], [T p.20], [T p.21], [T pp.21–22], [T pp.23–25], [T pp.26–33], [T p.40], [T pp.40–41], [T pp.40–43], [T p.41], [T p.42], [T pp.42–43], [T p.43], [T p.44], [T p.45], [T pp.45–46], [T p.46]. v3.1 patches added zero new page tags. |
| 5 | **Figure markers preserved** | **PASS** | All three FIGURE_POINTER blocks preserved verbatim with Source / Why this matters / When to look / Learner instruction fields intact: G Fig.1.2 (Card M1), T Fig.1-3 (Card M2), T Fig.2-16 (Card M3). One-field-per-line ver2 format preserved. PART B B2 Figure Rendering Instructions table unchanged. |
| 6 | **Source-boundary preserved** | **PASS** | No new scientific claims, no new examples, no new numerical anchors, no new external references, no new regulatory claims. PART B B5 Audit Guardrails forbidden-restoration list still binding and unaffected. v3.1 patches do not reintroduce any deprecated material from `00_step1_draft_v0.md` or rejected restoration list. |
| 7 | **HTML-readiness preserved** | **PASS** | All marker conventions intact: `<!-- MASTER LENS -->`, `<!-- ANNOTATION -->`, `<!-- ANCHOR -->`, `<!-- TRENCH -->`, `<!-- CONFUSION -->`, `<!-- SELF-TEST -->`, `<!-- RECAP -->`, `<!-- FIGURE_POINTER -->`. Marker → Component Mapping (B4-1) unaffected. Navigation anchor integrity rules (B4-2) unaffected. PATCH MODE Splice Verification Table (B8) unchanged because card heading anchor strings (`## Card M1 ⚡ Apex Concept — Modeling Carousel & 5대 Dysfuncti`, `## Card M2 — PK/PD Linkage & Therapeutic Window [T pp.3–17]`, `## Card M3 — Emax / C50 / Hill γ [T pp.35–43]`) remain verbatim. v3.1 first-use glosses use the established `(← Korean term)` convention already present in §1 Curation Map and require no new HTML component. |
| 8 | **Ready for Phase 5 HTML compilation** | **PASS** | All Phase 4D certificates pass. PART A is learner-standalone. PART B compilation contract intact. Three FIGURE_POINTER markers ready for splice. Page tag rendering rules (B3) ready. Self-test accordion mapping ready. v3.1 introduces no new rendering requirements. **GO for Phase 5 HTML Compile.** |

---

C-260507-160230-K1P

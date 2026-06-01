# XX_html_compile_input_master_v3.2.md

**v3.2 note:** This version applies a Korean-Dominant Readability Patch to PART A learner-facing prose. General English prose was converted to Korean where possible, while career-critical pharmacometrics terms are retained as Korean-English paired expressions on first use. Scientific content, equations, numerical anchors, page tags, source labels, figure markers, compiler markers, section structure, and PART B guardrails are preserved. No new scientific claims, examples, numbers, page tags, figures, or external references were added.

| Certificate | Status | Basis |
|---|---|---|
| Korean-Dominant Readability Certificate | PASS | General learner-facing English prose converted to Korean where possible; career-critical terms retained as Korean-English paired expressions. |
| Scientific Preservation Certificate | PASS | No scientific content, equation, number, example, page tag, or source label changed. |
| Marker Integrity Certificate | PASS | All figure markers, compiler markers, anchors, and section/card structures preserved. |
| HTML-Readiness Certificate | PASS | Phase 5 compatibility preserved; no HTML/Mermaid/SVG generated. |

---

# 00_HTML Compile Input Master — v3.2

**Output file**: `00_html_compile_input_master_v3.2.md`
**Assembly date**: 2026-05-07
**Assembly mode**: PATCH MODE
**Phase**: 4D — Learner-Complete + Mastery-Enriched + HTML-Ready Master Assembly
**Revision basis**: v3.1 was GO. v3.2 applies a Korean-Dominant Readability Patch to PART A only. All English learner-facing prose is converted to Korean where possible; career-critical pharmacometrics terms are retained as Korean-English paired expressions on first use. No scientific content, equation, page tag, figure marker, or PART B guardrail is altered.
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

## v3.1 → v3.2 Change Log (Korean-Dominant Readability Patch; no scientific content changed)

| # | Change | Location | Type | Source-boundary impact |
|---|---|---|---|---|
| Δ12 | Applied Korean-Dominant Readability Patch to entire PART A learner-facing prose: (1) all English section headers converted to Korean or Korean(English) paired form, (2) English explanatory labels converted to Korean, (3) remaining English sentences in learner-facing prose converted to Korean where possible, (4) career-critical terms retained as Korean-English paired expressions on first use. Scientific content, equations, page tags, source labels, figure markers (including all English fields inside FIGURE_POINTER blocks), compiler markers, section/card structure, anchor strings, code blocks, and PART B guardrails preserved verbatim. | PART A — all §1–§8 learner-facing sections | Korean-dominant prose conversion; sentence-level and label-level only | None — no new scientific claims, no new page tags, no new equations, no new numerical values, no new drug examples, no new figure decisions, no new external references. All anchor strings unchanged. PATCH MODE Splice Verification Table (B8) unaffected. |

All v3.1 anchors remain verbatim. Card heading anchor strings unchanged. PATCH MODE Splice Verification Table in §B8 is unchanged.

---

## Phase 4D Certification (v3.2)

| Certificate | Status | Basis |
|---|---|---|
| Learner-Standalone Certificate | **PASS** | PART A contains only learner-facing content. v3.2 patches convert English prose to Korean-dominant form; no compiler-only material was added. |
| Zero-Omission Certificate | PASS | All v3.1 MUST concepts, data anchors, Audit MUST/SHOULD corrections, Crucible-adopted insights, and 3 approved Figure Pointers are preserved verbatim. v3.2 adds no new scope items. |
| Mastery-Uplift Certificate | PASS | All v3.1 augmentations preserved. v3.2 does not add new mastery content; it only converts English prose to Korean-dominant form. |
| Source-Boundary Certificate | PASS | v3.2 patches introduce zero new page tags, equations, numerical values, drug examples, or external claims. All edits are prose-language conversion only. |
| HTML-Readiness Certificate | PASS | PART B rendering contracts and anchor integrity rules unchanged. v3.2 patches use existing prose patterns; no new marker types introduced. |
| Korean-Dominant Readability Certificate (v3.2) | **PASS** | All learner-facing English prose converted to Korean where possible. Career-critical pharmacometrics terms retained as Korean(English) paired expressions on first use. Section headers, labels, explanatory text fully Korean-dominant. |

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

## PART A — 학습자 본문(Learner-Facing Complete Handout)

## 학습자 안내

**이 핸드아웃 사용법**: 먼저 §1 로드맵으로 네 개의 MUST 개념을 잡고, §2의 M1→M4 카드를 순서대로 읽는다. 그다음 §5 혼동쌍 해부(Confusion Pair)와 §7 자기 테스트(Self-Test)로 "개념을 설명할 수 있는지"를 확인한다.

**권장 학습 경로**:
1. M1 — 모델링 회전목마(Modeling Carousel): fitting보다 앞선 사고 순서 확인.
2. M2 — PK/PD 연결(Linkage): 투여 요법(dose regimen)을 노출(exposure)과 반응(response)으로 번역.
3. M3 — Emax/C50/Hill γ: 농도-반응 곡선의 천장(ceiling), 효능(potency), 가파름(steepness) 분리.
4. M4 — 전환(Turnover): 농도 최고점과 효과 최고점이 분리될 때의 지연(delay) 사고.
5. §5와 §7 — 혼동쌍과 능동 회상(active recall)으로 마무리.

**그림 참고 사항**: `FIGURE_POINTER`는 교과서 그림을 직접 삽입하지 않는다. Image rights = None이므로 Phase 5에서는 텍스트형 참고 callout으로만 렌더링하고, 학습자는 해당 교과서 페이지의 원그림을 따로 확인한다.

**학습 마무리 전 확인**: 아래 네 문장을 스스로 말할 수 있어야 한다.
- 왜 fitting은 모델링 회전목마(Modeling Carousel)의 시작점이 아닌가?
- 왜 PK 단독 또는 PD 단독으로는 용량 결정(dosing decision)이 불완전한가?
- 왜 γ는 단순 지수(exponent)가 아니라 반응 민감도(response sensitivity)의 언어인가?
- 왜 전환(turnover)에서는 "얼마나 많이"와 "얼마나 빠르게"를 분리해야 하는가?

---

# 00_Content Lock v2 — Pre-Sprint: 모델링 철학·용어

**Source**: Gabrielsson & Weiner 5e Ch.1, p.1–7 + Rowland & Tozer 5e Ch.1–2, p.3–49
**Mode**: B-Standard
**Image rights**: None
**Phase**: 4B-2 — Readability Polish + Pedagogical Annotation
**Output type**: Phase 4D learner-facing markdown body with approved FIGURE_POINTER markers spliced; no HTML

---

# 최신 큐레이션 맵(Updated Curation Map)

이 세션은 두 권의 교과서가 서로 다른 질문에 답하는 진입점이다. Gabrielsson & Weiner는 **어떤 사고 순서로 모델링할 것인가**를 정한다. Rowland & Tozer는 **그 모델링 언어를 임상 용량 결정으로 어떻게 번역할 것인가**를 정한다. 후속 PopPK 세션에서 제어구문(control stream), GOF, 파라미터 해석(parameter interpretation), TDM 판단을 다루기 전에 잠가야 할 기반은 네 개다.

## MUST 계층(MUST tier)

| # | 개념 | 출처(Source) | 잠금 판정(Lock) |
|---|---|---|---|
| M1 | 모델링 회전목마(Modeling Carousel) & 5대 기능 장애(dysfunction) | Gabrielsson Ch.1 | 모델링은 fitting이 아니라 질문→설계→실험→EDA(← 그래프 중심 탐색적 데이터 분석) <!-- ANNOTATION -->→fitting→진단의 순환이라는 사고 순서를 고정한다. |
| M2 | PK/PD 연결(Linkage) & 치료역(Therapeutic Window) | Rowland & Tozer Ch.1 | 투여 요법(dose regimen)을 노출-시간 프로파일(exposure-time profile)과 반응-시간 프로파일(response-time profile)로 번역하는 임상 정량화의 출발점이다. |
| M3 | Emax / C50(← 최대효과 절반 농도) <!-- ANNOTATION --> / Hill γ(← 곡선 가파름 계수) <!-- ANNOTATION --> | Rowland & Tozer Ch.2 | 농도-반응 관계를 Emax, 효능(potency), 가파름(steepness)으로 분해하는 직접 효과(direct-effect) PD 모델의 골격이다. |
| M4 | 전환(Turnover)(← 체내 물질의 생성·소실 순환) <!-- ANNOTATION --> | Rowland & Tozer Ch.2 | 반응 지연(response delay)과 내인성 시스템의 동적 평형(dynamic equilibrium)을 이해하는 간접 반응(indirect-response) 모델의 선행 개념이다. |

## CONTEXT 계층 — 압축 흡수

| CONTEXT 개념 | 흡수 위치 | v2 처리 |
|---|---|---|
| constant / parameter / variable; primary vs secondary parameter | M1 | primary vs secondary parameter만 1문장으로 유지 |
| NCA vs 구획 모델링(compartmental modeling) | M1 | "질문이 단순하면 NCA, 예측·비선형·PK/PD 정량화에는 모델"로 압축 |
| ADME, 체내 배치(disposition), 초회 통과 손실(first-pass loss), 생체이용률(bioavailability), 장간순환(enterohepatic cycling) | M2 | PK 단계가 노출(exposure)을 만드는 생리학적 연쇄(physiological chain)라는 1문장으로 압축 |
| 투여 경로(route), 제형(dosage form), 순응도(adherence), 변이(variability) | M2 | 치료역(therapeutic window)을 흔드는 현실 세계 입력 요인으로 압축 |
| 혈장/혈청/전혈(plasma/serum/whole blood), 비결합 농도(unbound concentration) | M3 | 반응(response)을 연결할 때 측정 매트릭스(measurement matrix)와 비결합 농도 조건으로 압축 |
| 활성 대사체(active metabolite) / 전구약물(prodrug) / 입체이성질체(stereoisomer) | M3 | "측정한 농도 ≠ 활성 분자일 수 있음"으로 압축 |
| 질병 진행(disease progression), 위약(placebo), 바이오마커/대리 지표(biomarker/surrogate) | M3/M4 | 측정된 반응 해석의 배경으로 압축 |

---

# §1 — 세션 헤더 & 로드맵(Session Header & Roadmap)

**세션 제목**: Pre-Sprint — 모델링 철학·용어
**핵심 질문**: 모델링은 왜, 언제, 어떤 순서로 해야 하며, 그 결과를 어떻게 임상 용량 결정 언어로 번역할 것인가?

<!-- MASTER LENS -->
**핵심 통찰(Big Idea)**: 모델링은 수식 fitting이 아니라 **임상 질문 → 설계 → 실험 → EDA → fitting → 진단**의 순환 사고다. PK/PD는 그 순환 안에서 **투여 요법(dose regimen)을 노출-시간 프로파일(exposure-time profile)과 반응-시간 프로파일(response-time profile)로 번역하는 언어**다.
<!-- /MASTER LENS -->

## 로드맵(Roadmap)

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

**후속 개방**: M1은 GOF와 모델 선별(model selection), M2는 구획 PK(compartmental PK)와 TDM, M3는 직접 효과 PD(direct-effect PD), M4는 간접 반응(indirect-response)/질병 진행(disease progression)/TMDD 하류 모델로 이어진다.

---

# §2 — 개념 해부 카드(Concept Anatomy Cards)

---

## Card M1 ⚡ Apex Concept — Modeling Carousel & 5대 Dysfunction [G pp.1–7]

<!-- MASTER LENS -->
### [개념 Big Idea: 거장의 시각]

**왜 결정적인가**: 비선형 모델 적합(nonlinear model fitting)은 파라미터 초기 추정치(parameter initial estimate)를 요구한다. EDA 없이 fitting을 시작하면 모델 구조(model structure)와 초기 추정치가 데이터에서 나오지 않는다. 대신 사용자의 추측이나 소프트웨어 기본값이 출발점이 되고, 이때 국소 최솟값(local minimum)에 수렴할 위험이 커진다. 핵심은 "fitting이 시작점이 아니다"라는 것이다.

**체화해야 할 단 하나의 직관**: 모델링 회전목마(Modeling Carousel)에서 fitting은 6단계 중 5번째다. 앞의 네 단계 — 잠정 모델(tentative model), 설계(design), 실험(experiment), EDA — 가 먼저 모델 구조와 초기 추정치의 근거를 만든다. 따라서 fitting 결과의 해석 가능성은 fitting 전에 상당 부분 결정된다.
<!-- /MASTER LENS -->

> **숙달 메모(Mastery Note) — [CRUCIBLE_DERIVED]**
> EDA의 역할은 "plot을 한 번 보는 단계"가 아니라 비선형 fitting이 출발할 파라미터 탐색 공간(parameter-space basin)을 데이터 기반으로 좁히는 일이다. 따라서 회전목마의 앞 단계는 형식적 절차가 아니라 fitting을 해석 가능하게 만드는 사전 정보 생산이다.


### A. 정의(Formal Definition)

**모델링 회전목마(Modeling Carousel)**는 성공적 모델링을 위한 순환 워크플로(workflow)다 [G p.4].

1. **잠정 모델(Tentative model)** — 실험 전 사전 가설과 잠정적 시스템 모델.
2. **설계(Design)** — 용량(dose), 채혈 시점(sampling time), 반응 측정(response measurement), 대상 집단(population), 시뮬레이션/CATD.
3. **실험 수행(Run experiment)** — 데이터 수집.
4. **데이터 탐색(Explore data, EDA)** — 농도-시간, 반응-시간, 반응-농도 도표(plot)로 구조와 비선형성을 탐색.
5. **모델 적합(Fit model(s))** — 보통 비선형 회귀(nonlinear regression)로 파라미터와 정밀도(precision)를 추정.
6. **결과 분석 및 모델 판별(Analyze output & model discrimination)** — GOF, 잔차(residual), 파라미터 정밀도, 검증(validation), 경쟁 모델 비교.

G Ch.1의 단순 모델은 용량(dose) $D$를 상수(constant), $V$와 $Cl$을 일차 파라미터(primary parameter), $\hat C$와 $t$를 변수(variable)로 둔다. $K=Cl/V$, $AUC=D/Cl$, $t_{1/2}=\ln(2)/K$는 일차 파라미터에서 도출되는 이차 파라미터(secondary parameter)다 [G pp.1–2].

**수식 블록 — 1구획 예측 / 관측 오차(Equation block — one-compartment prediction / observation error) [G pp.1–2]**

$$
\hat C = \frac{D}{V}\exp\left(-\frac{Cl}{V}t\right)
$$

$$
C = \hat C + \varepsilon
$$

### B. 왜 모델링하는가?

G Ch.1의 핵심은 "모델링을 많이 하라"가 아니라 **필요할 때만 하라**다. 질문이 생체이용률(bioavailability)이나 총 청소율(total clearance) 같은 노출 요약(exposure summary)이라면 NCA가 충분할 수 있다. 반대로 단회 투여(single-dose)에서 반복 투여(multiple-dose)를 예측하거나, 비선형 약동학(nonlinear kinetics)을 다루거나, PK/PD 관계를 정량화해야 한다면 구획/PBPK형 모델이 필요하다 [G p.4].

<!-- ANCHOR -->
즉, 모델은 지식 과시가 아니라 질문에 맞는 압축 장치다. "가장 복잡한 모델"이 아니라 "질문을 답하는 데 필요한 만큼만 복잡한 모델"이 원칙이다 [G pp.3–4].
<!-- /ANCHOR -->

### C. 구조적 필연성(Structural Necessity)

4단계 EDA는 예쁜 그림을 만드는 단계가 아니다. 5단계 fitting에 들어갈 모델 구조와 초기 추정치를 생산하는 단계다. G p.5–6은 EDA가 모델 구조와 초기 추정치를 제안해야 하며, 비선형 fitting 알고리즘은 초기 추정치를 필요로 한다고 설명한다.

G Fig.1.2는 청소율(clearance)과 분포용적(volume)의 파라미터 공간에서 목적 함수 WRSS(← 가중 잔차 제곱합, weighted residual sum of squares)가 여러 홈(hollow)을 가질 수 있음을 보여 준다. 노란 점(yellow point)은 가능한 초기 추정치이고 빨간 점(red point)은 최종 추정치다. 출발점이 나쁘면 국소 최솟값(local minimum)으로 갈 수 있고, 좋은 초기 추정치는 전역 최솟값(global minimum)으로 가는 길을 열 수 있다 [G p.6].

<!-- TRENCH -->
**실무 꿀팁(Trench-level tip) [실무 추론]**: EDA의 산출물은 도표(plot) 자체가 아니라 "초기 추정치 후보 1표 + 비선형성 유무 1줄"이다. 용량 보정 도표(dose-normalized plot)가 비선형성을 시사하면, 결론 전에 데이터셋의 용량/시간/사건 코딩 오류 가능성부터 배제한다.
<!-- /TRENCH -->

### C-2. 그럴싸한 오해(Plausible Fallacy) — [EXPERT_INFERENCE, v3]

**그럴싸한 오해**: "GOF가 좋게 나왔으니 모델이 옳다."

**왜 틀렸는가**: Fitting(5단계)은 **가설 생성** 단계이고, 시뮬레이션과 의사결정이 회전목마의 목적이다. 6단계 "결과 분석 및 모델 판별"은 fitting 이후에 반드시 따른다. VPC 없이 GOF만으로 진단 단계를 건너뛰면, fitting이 만든 가설이 검증 없이 의사결정으로 직행한다. GOF 도표는 적합값(fitted value)이 관측값(observed value)에 가깝다는 것만 보여 줄 뿐 — 예측 타당성(predictive validity)은 별도로 평가해야 한다.

**실무에서 어떻게 드러나는가 (GOF-Only Submission Trap)**: VPC 없이 GOF만으로 규제 제출을 강행하면, 심사관이 모델의 예측 성능(predictive performance)을 확인할 수 없다는 이유로 결함 통지서(deficiency letter)를 발행하는 패턴으로 이어진다. 회전목마의 진단 단계(6단계) 생략이 만드는 가장 흔한 규제 실패 양식이다.

### D. 가정과 경계 조건(Assumptions & Boundary Conditions)

모델링 회전목마는 풍부한 데이터셋(rich dataset)과 실험 설계를 전제로 한 사고 순서다. 희소 데이터(sparse data)나 실세계 데이터(real-world data)에서는 EDA의 해상도가 떨어질 수 있다. 이 경우 "모델이 설명한다"와 "데이터가 구분해 준다"를 분리해서 말해야 한다.

**5대 기능 장애(Five common dysfunctions)** [G p.4]

| 기능 장애(Dysfunction) | 압축 해석 |
|---|---|
| fitting 전 EDA 경시 | fitting부터 돌리면 모델 구조와 초기 추정치가 빈약해진다. |
| 수식 맹종(slavery to formulas) | 수식을 외워도 생물학과 데이터가 요구하는 구조를 보지 못한다. |
| 소프트웨어 과신(too much trust in software) | 수렴 메시지는 과학적 타당성 보증서가 아니다. |
| 가중치 오용(improper use of weighting) | 잔차/오차 모델(residual/error model)을 잘못 두면 구조적 판단도 흐려진다. |
| 총체적 시야 부재(lack of holistic view) | 설계, 분석법, 생물학, 반응 시점을 함께 보지 못한다. |

### E. 한계(Limitations)

이 장은 NONMEM 수렴 진단(convergence diagnostics)이나 공분산 단계(covariance step) 해석을 가르치는 장이 아니다. 따라서 "몇 개 초기 추정치를 써야 하는가", "OFV 차이가 얼마면 충분한가" 같은 운영 기준은 이 카드에서 다루지 않는다. 이 카드에서 체화할 메시지는 **서로 다른 초기 추정치(different initial estimates)로 재실행하여 국소 최솟값 여부를 확인하라**는 원칙이다 [G p.6].

### F. 인지 잠금(Cognitive Lock)

- **형식적(Formal)**: 모델은 반응 변수(response variable)가 예측 변수(predictor)에 어떻게 의존하는지 표현한다.
- **그래프적(Graphical)**: 농도-시간, 반응-시간, 반응-농도 도표가 구조를 먼저 말한다.
- **알고리즘적(Algorithmic)**: 비선형 fitting은 초기 추정치와 목적 함수 곡면(objective surface)의 분지(basin)에 민감하다.
- **생물학적(Biological)**: 모델은 생물학과 수집된 데이터가 이끌어야(drive) 한다.
- **실무적(Practical)**: fitting 전에 "질문, 설계, EDA, 초기 추정치"가 문서화되어야 한다.

**진단 시그니처(Diagnostic signature) [실무 추론]**: **조기 수렴 착각(Premature Convergence Mirage)** — EDA 없이 fitting부터 시작해 수렴은 했지만, 모델 구조와 초기 추정치의 근거가 빈약한 상태.

### G. 제텔카스텐 원자(Zettelkasten Atom)

```yaml
aliases: [Modeling Carousel, EDA-first modeling, local minimum]
tags: [pharmacometrics/modeling, EDA, model-selection]
source: Gabrielsson & Weiner 5e Ch.1 pp.1-7
lock: Fitting is Step 5, not Step 1. EDA produces model structure and initial estimates.
```

<!-- RECAP -->
**M1 요약(Recap)**: 모델링의 첫 원칙은 소프트웨어 실행이 아니라 질문과 데이터 구조를 먼저 보는 것이다. EDA를 건너뛴 fitting은 수렴할 수는 있어도, 왜 그 모델이어야 하는지 설명하지 못한다.
<!-- /RECAP -->

> **▶ 실무 체화 요약(Practice Brief) — M1 체화 4축 — [EXPERT_INFERENCE, v3]**
> - **왜 알아야 하는가**: 모델링 회전목마 없이는 fitting 결과가 왜 그 형태인지 설명하지 못하고, 모델 선별(model selection)이 근거 없는 주관적 선택이 된다.
> - **흐름상 역할**: 이 카드는 후속 GOF, 모델 선별, VPC 해석 세션의 사고 순서를 미리 잠그는 관문이다.
> - **체화 꿀팁**: "왜 EDA가 없으면 초기 추정치를 만들 수 없는가"를 비선형 fitting 알고리즘의 수학적 요구에서 스스로 도출할 수 있을 때 M1이 내재화된 것이다 — 암기가 아니라 구조적 필연에서 이유를 끌어내라.
> - **실무 활용**: 새 데이터셋을 받을 때 가장 먼저 용량 보정 농도-시간 도표(dose-normalized concentration-time plot)를 그리는 EDA 루틴이 곧 M1이 실무로 출력되는 형태다; 이 도표 없이 제어구문(control stream)부터 여는 것이 M1이 경고한 기능 장애다.

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

**왜 결정적인가**: 임상 처방 질문은 "얼마나, 얼마나 자주, 얼마나 오래, 어떤 투여 경로(route)와 제형(dosage form)으로 줄 것인가"다. 이 질문의 답은 용량(dose) 숫자 자체에 있지 않다. 대신, dose가 만든 노출-시간 프로파일(exposure-time profile), 그리고 그 노출이 만든 원하는/원치 않는 반응-시간 프로파일(desired/adverse response-time profile)로 답해야 한다 [T p.3].

**체화해야 할 단 하나의 직관**: PK와 PD는 두 개의 독립 과목이 아니라 하나의 인과 사슬(causal chain)이다. **투여 요법(dosage regimen) → 체내 노출(exposure within body) → 원하는/원치 않는 효과(desired/adverse effects)**가 연결되어야 한다. 그래야 요법을 왜 바꾸는지 설명할 수 있다.
<!-- /MASTER LENS -->

> **실무 렌즈(Practice Lens) — [TEXTBOOK_DERIVED]**
> 용량 질문을 받을 때 먼저 용량 숫자를 고정하지 말고 노출-시간 프로파일과 반응-시간 프로파일을 분리해서 생각하라. 같은 요법이라도 입력(input), 변이(variability), 순응도(adherence)가 노출을 바꾸면 치료역(therapeutic window) 안에 머무는 시간도 달라진다.


### A. 정의(Formal Definition)

**약동학(Pharmacokinetics)**: 용량, 제형, 투여 빈도, 투여 경로 같은 입력이 시간에 따른 농도/노출을 어떻게 만드는가.
**약력학(Pharmacodynamics)**: 농도가 원하는 효과(desired effect)와 이상 반응(adverse effect)을 시간에 따라 어떻게 만드는가 [T pp.4–5].

T Fig.1-3이 보여 주는 핵심은, 농도 대 시간(conc-vs-time)과 농도 대 효과(conc-vs-effect)가 결합되어야 비로소 효과 대 시간(effect-vs-time)이 만들어진다는 것이다. PK만으로는 "몸 안 농도가 어떻게 변하는가"만 알 수 있다. PD만으로는 "농도가 주어졌을 때 반응이 어떻게 변하는가"만 알 수 있다. 치료에는 둘의 연결(link)이 필요하다 [T p.5].

**PK 단계 맥락**: ADME, 체내 배치(disposition), 초회 통과 손실(first-pass loss), 생체이용률(bioavailability), 장간순환(enterohepatic cycling)은 용량이 전신 노출(systemic exposure)로 바뀌는 생리학적 연쇄의 구성 요소다 [T pp.26–33].

### B. 치료역(Therapeutic Window)

치료역(therapeutic window)은 노출이 너무 낮으면 무효 치료(ineffective therapy)가 되고, 너무 높으면 이상 반응(adverse effects)이 증가한다는 전제 위에 놓인 작동 범위(operating range)다 [T p.6].

<!-- ANCHOR -->
[해석/교육용 형식화] 실무적으로는 치료역을 "치료 반응 확률이 충분하고 이상 사건 확률이 지나치지 않은 노출 범위"로 읽으면 된다. 단, 이 확률 집합 표기는 원문 수식이 아니라 교육용 형식화(formalization)이다.
<!-- /ANCHOR -->

### C. 구조적 필연성(Structural Necessity)

T Ch.1은 경험적 시행착오 요법 설계(empirical trial-and-error regimen design)를 합리적 PK/PD 접근법(rational PK/PD approach)과 대비한다. 예전에는 용량과 투여 간격을 조정하고 원하는/원치 않는 효과를 관찰하면서 요법을 개선했다. 그러나 이 방식만으로는 digoxin과 morphine 요법 차이의 원리를 설명하지 못한다 [T p.4].

Digoxin은 0.125–0.25 mg 1일 1회로 쓰이는 반면, morphine sulfate는 10–50 mg을 하루 최대 6회까지 투여할 수 있다. 두 약물 모두 치료역이 비교적 좁지만, morphine은 빠르게 제거되어 자주 투여가 필요하고, digoxin은 천천히 제거되어 1일 1회가 가능하다 [T pp.4, 7].

**핵심 예시 — digoxin 축적/디지탈화 용량(Key example — digoxin accumulation/digitalizing dose) [T p.7]**
Digoxin을 낮은 1일 용량으로 주면 처음에는 무효할 수 있고, 높은 투여 속도로 유지하면 나중에 독성이 나타날 수 있다. 그래서 초기에는 여러 소량 투여로 빠르게 치료 농도에 도달시키고 이후 소량 유지 용량으로 유지하는 디지탈화 용량(digitalizing dose) 논리가 나온다.

### D. 임상적 중요성(Why It Matters Clinically)

Rowland & Tozer는 부적절한 약물 사용(inappropriate drug use) 때문에 병원 입원 환자의 약 5%가 입원한다는 예를 든다 [T p.4]. 이 통계가 시사하는 바는 단순한 약동학 지식의 유용성이 아니다. 핵심 메시지는 **요법 설계의 안전성**이다.

PK/PD는 약물 설계(drug design), 약물 선택(drug selection), 투여 요법 설계, 임상시험 프로토콜 설계, 데이터 해석, 약물 제품 성능 평가, 개인 맞춤 치료(individualized therapy) 개시에도 쓰인다 [T p.20].

### E. 한계와 현실 세계의 왜곡(Limitations & Real-World Distortions)

- **측정 부위 문제(Measured site problem)**: 작용 부위(site of action) 농도는 대개 직접 측정하기 어렵고 혈장이 대리 부위(surrogate site)로 쓰인다 [T p.6].
- **순응도 문제(Adherence problem)**: 처방된 요법이 실제 노출로 그대로 이어지지 않는다. 1일 1회 항고혈압제 코호트에서 1년 말 처방약을 지속한 비율은 약 50%였다 [T p.12].
- **변이 문제(Variability problem)**: phenytoin 농도 변이, warfarin S-warfarin 변이, G6PD/primaquine, debrisoquine/CYP2D6, terfenadine/ketoconazole 예시는 같은 요법이 같은 노출/반응을 보장하지 않음을 보여 준다 [T pp.10–12].
- **Warfarin 유전학 교정**: 이 PDF 범위에서는 CYP2C9/CYP2C19 다형성(polymorphisms)과 vitamin K epoxide reductase 기전이 언급된다. VKORC1 표기는 이 범위의 원문 표현이 아니므로 사용하지 않는다 [T p.10].

<!-- TRENCH -->
**실무 꿀팁(Trench-level tip) [실무 추론]**: 순응도 모니터링이 약하면 겉보기 PK 변이(apparent PK variability)가 실제 누락 투여(missed dose)의 가공물(artifact)일 수 있다. 이때 모델은 환자 생리 차이가 아니라 입력 이력 오류를 변이로 흡수할 수 있다.
<!-- /TRENCH -->

### F. 제텔카스텐 원자(Zettelkasten Atom)

```yaml
aliases: [PK/PD linkage, therapeutic window, input-response phases]
tags: [clinical-pharmacology/dosing, pharmacometrics/pkpd]
source: Rowland & Tozer 5e Ch.1 pp.3-17; Table 2-1 p.20
lock: Dose regimen is useful only after it is translated into exposure-time and response-time profiles.
```

<!-- RECAP -->
**M2 요약(Recap)**: PK/PD 연결의 핵심은 "용량이 아니라 작용 부위 농도(concentration at the site of action)가 반응을 구동(drive)한다"는 점이다. 치료역은 이 연결이 임상적으로 작동해야 하는 안전 범위다.
<!-- /RECAP -->

> **▶ 실무 체화 요약(Practice Brief) — M2 체화 4축 — [EXPERT_INFERENCE, v3]**
> - **왜 알아야 하는가**: PK/PD 연결을 놓치면 PK 파라미터를 추정하고도 용량 결정(dosing decision)을 내릴 논리적 근거가 빠져 있게 된다 — 숫자만 있고 해석이 없는 상태다.
> - **흐름상 역할**: 이 카드는 구획 PK, TDM, 노출-반응(exposure-response) 세션이 공유하는 용량→노출→반응 번역 문법을 선행 잠금한다.
> - **체화 꿀팁**: 어떤 처방을 볼 때 "이 용량이 만드는 노출-시간 프로파일은 무엇이고, 그 프로파일이 치료역 안에 머무는 시간은 얼마나 되는가"를 자동으로 묻게 되면 M2가 내재화된 신호다.
> - **실무 활용**: 규제 보고서에서 PK 섹션과 PD 섹션을 완전히 분리하지 않고 PK/PD 연결 섹션으로 연결하는 것이 M2가 실무 문서에서 나타나는 형태다.

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

**왜 결정적인가**: 농도-반응 관계를 말할 때 "효과가 증가한다"만으로는 부족하다. Emax는 천장(ceiling)을, C50은 효능(potency)을, γ는 곡선 가파름(steepness)을 따로 보여 준다. 이 세 가지를 분리하지 못하면 용량 적정(dose titration), 평가변수 선택(endpoint selection), 안전역 해석(safety margin interpretation)이 흐려진다.

**체화해야 할 단 하나의 직관**: C50이 낮다고 항상 좋은 약이 아니다. 같은 효능이라도 Emax가 낮으면 충분한 임상 반응(clinical response)에 도달하지 못할 수 있다. 또한 γ가 너무 크면 작은 농도 변화가 반응 역치(response threshold)를 급격히 넘게 만든다 [T pp.40–43].
<!-- /MASTER LENS -->

> **실무 렌즈(Practice Lens) — [CRUCIBLE_DERIVED]**
> γ는 곡선 적합 파라미터(curve-fitting parameter)에 그치지 않는다. γ가 클수록 같은 C50 주변에서도 작은 농도 변화가 반응 판단을 더 크게 바꾸므로, 적정 친화적 반응(titration-friendly response)인지 역치형 반응(threshold-like response)인지 먼저 구분해야 한다.


### A. 정의(Formal Definition)

**등급 반응(Graded response)**은 농도가 변할 때 반응 강도(response intensity)가 연속적으로 변하는 반응이다. Ketamine 예시에서 S(+)-ketamine은 R(−)-ketamine보다 더 낮은 C50와 더 높은 최대 반응(maximum response)을 보인다: S(+) C50 ≈ 0.7 mg/L, R(−) C50 ≈ 1.8 mg/L [T p.40].

**수식 블록 — Hill/Emax 방정식(Equation block — Hill/Emax equation) [T p.40]**

$$
E = \frac{E_{\max}\,C^{\gamma}}{C_{50}^{\gamma}+C^{\gamma}}
$$

- $E_{\max}$: 최대 반응(maximum response).
- $C_{50}$: $E_{\max}$의 50%를 만드는 농도.
- $\gamma$: 가파름 인자(steepness factor).

**노출-시간 앵커(Exposure-time anchor) [T pp.21–22]**: 경구 단회 투여 프로파일(single oral dose profile)에서 $C_{\max}$는 최대 전신 노출(maximum systemic exposure), $t_{\max}$는 그 시간, AUC는 총 전신 노출(total systemic exposure)이다. Fig.2-1의 예시는 $C_{\max}=96\,\mu g/L$, $t_{\max}=3.0$ hr이다.

### B. γ가 실제로 바꾸는 것(What γ Really Changes)

T p.40은 $\gamma=1$이면 20%→80% 반응에 필요한 농도 범위가 $0.25C_{50}$에서 $4C_{50}$, 즉 16배(16-fold)라고 설명한다. $\gamma=2$이면 $0.5C_{50}$에서 $2C_{50}$, 즉 4배(4-fold)로 압축된다.

$$
\gamma=1: C_{20}=0.25C_{50},\; C_{80}=4C_{50}
$$

$$
\gamma=2: C_{20}=0.5C_{50},\; C_{80}=2C_{50}
$$

일반적으로 $\gamma$는 1–3 사이에 있다. 그러나 매우 크면 최소 반응과 최대 반응 사이의 농도 범위가 좁아진다. 그 결과 반응이 전부 아니면 전무(all-or-none)처럼 보일 수 있다 [T pp.40–41].

<!-- ANCHOR -->
$\gamma$는 단순한 곡선 모양이 아니라 처방 사고를 바꾼다. $\gamma \approx 1$이면 증상 기반 적정(symptom-based titration)이 상대적으로 자연스럽다. 반대로 반응이 가파르거나(steep) 역치형(threshold-like)이면 작은 농도 변화가 임상 사건(clinical event)을 바꿀 수 있다.
<!-- /ANCHOR -->

### C. 실제 데이터 앵커(Real Data Anchors)

**핵심 예시 — propranolol [T p.42]**
운동 유발 빈맥(exercise-induced tachycardia) 감소율과 비결합 propranolol 농도의 관계는 Hill 방정식에 잘 맞고, $\gamma \approx 1$, $E_{\max}\approx 40\%$, $C_{50}=5.3\,\mu g/L$로 제시된다.

**핵심 예시 — alfentanil 이분형 반응(quantal response) [T pp.42–43]**
Alfentanil은 nitrous oxide 마취 중 만족스러운 반응의 누적 빈도(cumulative frequency)로 평가된다. C50는 유방(breast) 0.27 mg/L, 하복부(lower abdomen) 0.31 mg/L, 상복부(upper abdomen) 0.42 mg/L 순으로 증가한다. 이 예시는 γ를 추정한 등급 곡선이 아니다. 즉, 이분형 평가변수(quantal endpoint)에서 반응 확률이 농도와 어떻게 연결되는지 보여 주는 예시다.

### D. 측정과 분석 경계(Measurement & Assay Boundaries)

총 혈장/혈청 농도(total plasma/serum concentration)에는 결합형과 비결합형 약물이 모두 포함된다. 그러나 분포, 소실, PD 반응은 비결합 농도(unbound concentration)에 의존한다. 다만 비결합 분율(fraction unbound)이 일정하면 총 농도로도 충분할 수 있다. 반대로 포화성 결합(saturable binding), 약물 상호작용에 의한 전위(displacement interaction), 신장/간 질환, 수술, 중증 화상, 임신처럼 결합이 변하는 조건에서는 비결합 농도 측정이 중요해진다 [T p.21].

**화학적 물질 경계(Chemical entity boundary)**: 라세미체(racemate), 입체이성질체(stereoisomer), 활성 대사체(active metabolite), 전구약물(prodrug)에서는 "측정한 총 모체 농도(total parent concentration)"가 실제 활성 물질(active moiety)을 대표하지 못할 수 있다. Acenocoumarol, methylphenidate, aspirin/salicylic acid 예시는 분석 특이성(assay specificity)이 PK/PD 연결을 좌우한다 [T pp.23–25].

<!-- TRENCH -->
**실무 꿀팁(Trench-level tip) [실무 추론]**: 용량 범위가 C50 주변에만 몰려 있고 고원(plateau) 정보가 없으면 γ를 자유롭게 추정하기보다 절약적 가정(parsimonious assumption)을 먼저 검토한다. "γ를 추정했다"는 사실보다 "데이터가 γ를 식별(identify)할 수 있는가"가 먼저다.
<!-- /TRENCH -->

### E. 한계(Limitations)

임상적 $E_{\max}$는 약리학적 최대치(pharmacological maximum)보다 낮을 수 있다. 예를 들어 심박수를 올리는 약물에서는 심혈관계가 먼저 악화될 수 있다. 그러면 약리학적 최대치에 도달하기 전에 안전성 한계가 온다. 따라서 작용제(agonist)의 $E_{\max}$는 길항제(antagonist)보다 임상적으로 정의하기 어렵다 [T p.41].

Fig.2-19의 메시지는 노출 지표(exposure metric) 선택에도 적용된다. 만성 치료(chronic therapy)에서는 최소 농도 이상 유지 기간(duration above a minimum concentration)이 중요할 수 있고, 두통 완화처럼 빠른 효과가 목적이면 $C_{\max}$와 $t_{\max}$가 더 중요할 수 있으며, 어떤 경우에는 총 AUC가 더 관련 있을 수 있다 [T p.44].

### F. 진단 잠금(Diagnostic Lock)

- **등급 반응(Graded response)**: 농도 변화가 반응 강도의 연속 변화로 이어진다.
- **이분형 반응(Quantal response)**: 개체 수준 평가변수는 전부 아니면 전무(all-or-none)이며, 집단 수준 누적 빈도로 농도-반응을 본다.
- **평가변수 함정(Endpoint trap)**: 약리적 반응은 등급형인데 임상 평가변수가 역치로 절단되어 이분형처럼 분석될 수 있다 [T p.43].
- **진단 시그니처(Diagnostic signature) [실무 추론]**: **Hill γ 식별 가능성 붕괴(Hill γ Identifiability Collapse)** — 데이터 범위가 고원과 저반응 영역을 충분히 포함하지 못해 γ 추정이 모델보다 잡음(noise)을 따라가는 상태.

### G. 제텔카스텐 원자(Zettelkasten Atom)

```yaml
aliases: [Emax, C50, Hill equation, graded response, quantal response]
tags: [pharmacometrics/pd, exposure-response]
source: Rowland & Tozer 5e Ch.2 pp.35-43
lock: Emax is ceiling, C50 is potency, gamma is steepness; endpoint type decides how response should be modeled.
```

<!-- RECAP -->
**M3 요약(Recap)**: Hill 방정식은 농도-반응의 "현재 순간"을 정량화한다. 하지만 측정 농도, 활성 물질, 평가변수 유형, γ 식별 가능성(identifiability)을 함께 보지 않으면 정확한 수식도 잘못된 용량 해석으로 이어진다.
<!-- /RECAP -->

> **▶ 실무 체화 요약(Practice Brief) — M3 체화 4축 — [EXPERT_INFERENCE, v3]**
> - **왜 알아야 하는가**: Emax/C50/γ를 한 덩어리로 암기하면 평가변수 유형이 바뀔 때 모델 선택이 흔들리고, γ 식별 가능성 문제를 인식하지 못한 채 잡음을 파라미터로 추정한다.
> - **흐름상 역할**: 이 카드는 직접 효과 PD, 노출-반응 분석(exposure-response analysis), 용량 적정 설계 세션의 "천장-효능-가파름" 3축 언어를 선행 잠금한다.
> - **체화 꿀팁**: propranolol 예시($\gamma\approx1$, $C_{50}=5.3\,\mu g/L$)를 기준으로 γ 값을 2, 3으로 올리면 20%–80% 반응 범위가 어떻게 압축되는지 손으로 계산해 보면 — γ가 단순 지수가 아니라 적정 논리를 바꾼다는 것이 체감된다.
> - **실무 활용**: 노출-반응 보고서에서 C50 하나만 보고하지 않고 Emax, γ, 평가변수 유형(등급형 vs 이분형)을 함께 명시하고 γ 식별 가능성을 언급하는 것이 M3가 규제 문서에서 요구하는 수준이다.

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

**왜 결정적인가**: 어떤 반응은 약물 농도가 최고점을 찍은 뒤 훨씬 늦게 나타난다. 이 지연은 단순 분포 지연(distribution delay)일 수도 있고, 내인성 시스템의 전환(turnover) 때문일 수도 있다. 둘을 구분하지 못하면 직접 효과 Hill 모델로 설명할 수 없는 시간을 억지로 fitting하게 된다.

**체화해야 할 단 하나의 직관**: 정상 상태(steady state)는 움직이지 않는 상태가 아니다. **입력 속도(input rate)와 출력 속도(output rate)가 같아 풀 크기(pool size)가 일정하게 보이는 동적 평형(dynamic equilibrium)**이다 [T p.45]. 따라서 약물이 입력을 바꾸는지 출력을 바꾸는지에 따라 반응 시간 경과(response time course)가 달라진다.
<!-- /MASTER LENS -->

> **판단 렌즈(Judgment Lens) — [CRUCIBLE_DERIVED]**
> 관찰 데이터에서 농도 최고점과 효과 최고점이 분리되면, 단순 직접 효과 모델만으로 끝내기 전에 전환/지연 사고를 켜야 한다. 이 판단은 모델을 복잡하게 만들기 위한 것이 아니라 반응이 어느 시스템 풀(system pool)을 통해 나타나는지 묻는 출발점이다.


### A. 정의(Formal Definition)

전환(turnover)은 내인성 물질/시스템이 정상 상태에 있으면서 계속 갱신(renewal)되고 소실(elimination)되는 현상이다. 경구 항응고제(oral anticoagulants), 항고지혈증제(antihyperlipidemics), 요산 배설 촉진제(uricosuric agents), epoetin alfa는 모두 내인성 화합물/시스템의 생성(formation) 또는 소실을 바꿔 지연 반응을 만들 수 있다 [T p.45].

**수식 블록 — 전환 관계식(Equation block — turnover relationships) [T p.45]**

$$
k_t = \frac{R_t}{A_{ss}}
$$

$$
t_t = \frac{A_{ss}}{R_t}
$$

$$
t_t = \frac{1}{k_t}
$$

- $A_{ss}$: 정상 상태 풀 크기(pool size at steady state).
- $R_t$: 전환 속도(turnover rate).
- $k_t$: 분획 전환 속도(fractional turnover rate).
- $t_t$: 전환 시간(turnover time).

### B. 핵심 예시(Key Examples)

**핵심 예시 — warfarin [T p.8]**
Warfarin sodium 1.5 mg/kg 단회 경구 투여를 5명의 남성 지원자에게 투여했을 때, 혈장 warfarin 농도는 빠르게 올라가지만 prothrombin complex activity 반응은 느리게 변한다. 이 분리는 농도-시간 프로파일만으로 반응-시간 프로파일을 설명할 수 없음을 보여 준다.

**핵심 예시 — paclitaxel [T pp.8–9]**
Paclitaxel은 체내에서 약 2일 내 제거되지만 백혈구 수(leukocyte count) 변화는 매우 느리며, 최저점(nadir)은 1주 이후에 나타나고 기저선 회복(baseline recovery)은 약 3주가 걸릴 수 있다. 이것이 전환 구동 반응(turnover-driven response)의 전형적 시그니처다.

**핵심 예시 — 총 체수분(total body water) [T pp.45–46]**
총 체수분은 약 42 L이고, 평균 전환 속도는 2.5 L/day, 분획 전환 속도는 0.06 day⁻¹, 전환 시간은 17 days다. 사막 환경(desert-like condition)에서는 풀 크기가 거의 일정해도 전환 속도가 21 L/day까지 증가할 수 있고, 이때 분획 전환 속도는 0.5 day⁻¹, 전환 시간은 2 days가 된다.

### C. 구조적 필연성(Structural Necessity)

M3는 농도와 반응의 즉시적 또는 준정상(quasi-steady) 관계를 다루지만, M4는 측정된 반응이 내인성 풀의 변화를 반영할 때 필요하다. 판단 기준은 단순하다. **효과 최고점 시간이 농도 최고점 시간과 분리되어 있으면 직접 효과 Hill만으로 충분한지 의심한다**.

<!-- ANCHOR -->
전환 모델링에서 더 중요한 질문은 "$R_t$, $k_t$, $t_t$ 중 무엇을 외웠는가"가 아니다. 핵심 질문은 "이 시스템에서는 풀 크기가 보존되는가, 분획 전환이 보존되는가, 아니면 전환 속도 자체가 바뀌는가"다. 체수분 예시는 풀 크기가 피드백으로 유지될 수 있음을, 콜레스테롤/백혈구 예시는 풀 크기 자체가 변할 수 있음을 각각 보여 준다 [T p.46].
<!-- /ANCHOR -->

### D. 경계와 범위(Boundaries)

이 장은 간접 반응 ODE 코딩(indirect response ODE coding)을 제공하지 않는다. 이 카드에서 체화할 것은 수식 템플릿이 아니라 전환 파라미터 간 관계와 지연 반응의 원인이다. ODE, KIN/KOUT, 기저선 파라미터화(baseline parameterization)는 후속 PD 모델링 세션으로 이연한다.

<!-- TRENCH -->
**실무 꿀팁(Trench-level tip) [실무 추론]**: 희소 반응-시간 데이터(sparse response-time data)에서 입력과 출력을 동시에 자유롭게 추정하면 파라미터가 서로 보상할 수 있다. 먼저 기저선(baseline), 최고점 시점(peak timing), 회복 시점(recovery timing)을 보고 어떤 전환 구성 요소가 데이터로 식별 가능한지 판단한다.
<!-- /TRENCH -->

### E. 진단 잠금(Diagnostic Lock)

- **전환 속도(turnover rate)**가 크다고 과정이 빠른 것은 아니다. 풀 크기가 크면 큰 양이 오가도 분획 전환은 느릴 수 있다.
- **분획 전환 속도(fractional turnover rate)**와 **전환 시간(turnover time)**이 과정 속도를 더 직접적으로 말한다.
- **진단 시그니처(Diagnostic signature) [실무 추론]**: **전환-PD 오귀인(Turnover-PD Mis-attribution)** — 지연 반응을 PK 분포 지연이나 Hill γ 문제로만 설명하려는 상태.

### F. 제텔카스텐 원자(Zettelkasten Atom)

```yaml
aliases: [Turnover, pool size, fractional turnover rate, turnover time]
tags: [pharmacometrics/indirect-response, physiology/dynamic-equilibrium]
source: Rowland & Tozer 5e Ch.2 pp.44-46
lock: Steady state is dynamic equilibrium; delayed response often means the measured system is turning over.
```

<!-- RECAP -->
**M4 요약(Recap)**: 전환은 "반응이 늦다"를 수학적으로 다루기 전, 무엇이 천천히 바뀌고 있는지 묻는 생리학적 언어다. 농도 최고점과 효과 최고점이 분리되면 M4 사고가 켜져야 한다.
<!-- /RECAP -->

> **▶ 실무 체화 요약(Practice Brief) — M4 체화 4축 — [EXPERT_INFERENCE, v3]**
> - **왜 알아야 하는가**: 전환 개념 없이는 지연 반응을 부적합(poor fit) 또는 데이터 오류로 오해하고, 간접 반응 모델이 필요한 시점을 놓친다.
> - **흐름상 역할**: 이 카드는 간접 반응 모델, 질병 진행 모델, TMDD 하류 세션이 공유하는 "효과 최고점 지연의 원인 분류" 판단 기준을 선행 잠금한다.
> - **체화 꿀팁**: 체수분 전환 예시의 수치($A_{ss}=42\,L$, $R_t=2.5\,L/day$ → $k_t=0.06\,day^{-1}$, $t_t=17\,days$)를 사막 조건($R_t=21\,L/day$ → $t_t=2\,days$)과 비교하며 풀 크기가 고정돼도 $k_t$와 $t_t$가 얼마나 크게 달라지는지 직접 손으로 계산하면 속도/분획 속도/시간의 차이가 내재화된다.
> - **실무 활용**: PD 모델링 보고서에서 농도 최고점과 효과 최고점의 시간 차이를 먼저 데이터로 기술하고, 그 차이가 전환 구조 채택의 근거임을 명시하는 것이 M4가 실무 문서에서 나타나는 형태다.

---

## §2 요약 — 30초 진단 격자(30-Second Diagnostic Grid)

<!-- RECAP -->
새 PK/PD 데이터셋을 처음 받은 30초에는 네 개 렌즈를 동시에 켜야 한다.

| 렌즈(Lens) | 먼저 볼 것 | 즉시 판단할 것 |
|---|---|---|
| M1 | 용량 수준, 채혈 밀도, 농도-시간 도표 | EDA가 모델 구조와 초기 추정치를 줄 수 있는가? |
| M2 | 요법, 투여 경로, 순응도, 측정 부위 | 용량→노출→반응 사슬에서 빠진 연결이 있는가? |
| M3 | 고원, C50 주변 범위 포함 여부, 평가변수 유형 | Emax/C50/γ를 식별할 수 있는가, 평가변수가 등급형인가 이분형인가? |
| M4 | 농도 최고점 vs 효과 최고점 시점 | 직접 효과 모델로 충분한가, 전환/지연 구조가 필요한가? |

이 격자의 목적은 제어구문(control stream)을 바로 쓰게 만드는 것이 아니다. 어떤 모델을 선택할 근거가 데이터에 있는지 먼저 묻는 것이다.
<!-- /RECAP -->

---

# §5 — 혼동쌍 해부(Confusion Pair Dissection)

## 혼동쌍 1 — 약동학(Pharmacokinetics) vs 약력학(Pharmacodynamics)

<!-- CONFUSION -->
| 구분 | 약동학(Pharmacokinetics) | 약력학(Pharmacodynamics) |
|---|---|---|
| 질문 | 몸(body)이 약물(drug)에 무엇을 하는가? | 약물이 몸에 무엇을 하는가? |
| 축 | 입력 → 농도-시간 | 농도 → 효과-시간 |
| 데이터 | 혈장/혈청/전혈 농도, AUC, Cmax, tmax | 원하는/원치 않는 반응, 바이오마커, 임상 평가변수 |
| 실패 양식 | 노출(exposure)을 용량(dose)과 동일시 | 반응을 농도 없이 직접 용량과 연결 |

**잠금(Lock)**: PK와 PD는 반대말이 아니다. 치료적으로 유용한 예측은 둘이 연결(link)될 때 비로소 가능하다 [T p.5].

**⚡ 기억 고리 (Memory Hook)**: PK는 *입력 → 농도* 의 화살표이고 PD는 *농도 → 효과* 의 화살표다. 두 화살표는 **같은 선상의 앞뒤 화살표**이지 좌우의 반대 화살표가 아니다. 따라서 한쪽 화살표만 그리면 용량-효과 사슬이 끊겨 임상 의사결정이 멈춘다 [T p.5].
<!-- /CONFUSION -->

## 혼동쌍 2 ⚡ 치명적 타격(Critical Blow) 적용 — 등급 반응(Graded Response) vs 이분형 반응(Quantal Response)

<!-- CONFUSION -->
| 구분 | 등급 반응(Graded response) | 이분형 반응(Quantal response) |
|---|---|---|
| 반응 형태 | 강도가 연속적으로 변함 | 개체 평가변수가 전부 아니면 전무(all-or-none) |
| 모델 감각 | Hill/Emax로 연속 반응을 설명 | 누적 빈도/확률로 사건을 설명 |
| 예시 | ketamine 반응, propranolol 심박수 감소 | alfentanil 만족스러운 마취 반응 |
| C50 의미 | Emax의 50%를 주는 농도 | 집단의 50%에서 사전 결정된 반응이 나타나는 농도 |

**치명적 타격(Critical Blow) [교육용 가상 시나리오]**: 임상시험 프로토콜의 일차 평가변수(primary endpoint)가 "24시간 내 ≥50% 통증 감소: 예/아니오" 같은 이분형 평가변수인데, 모델러가 연속 VAS 점수를 등급형 Hill 모델로만 분석하면, 통계학자의 이진 평가변수 분석과 모델러의 노출-반응 분석이 서로 다른 용량을 지지할 수 있다. 문제는 Hill 방정식 자체가 아니다. 문제는 **평가변수 척도(endpoint scale)와 모델링 프레임워크의 불일치**다.

> **실패 양식(Failure Mode) — [CRUCIBLE_DERIVED]**
> 이분형 자료를 개체별 등급 곡선처럼 읽으면 Hill 방정식의 문제가 아니라 평가변수 정의의 문제가 된다. 먼저 개체 수준 반응 크기인지, 집단 수준 발생 확률인지 분리해야 한다.

<!-- /CONFUSION -->

## 혼동쌍 3 — 전환 속도(Turnover Rate) vs 분획 전환 속도(Fractional Turnover Rate)

<!-- CONFUSION -->
| 구분 | 전환 속도 $R_t$ | 분획 전환 속도 $k_t$ |
|---|---|---|
| 정의 | 단위 시간당 입출력 양 | 풀 크기 대비 분획 교체 속도 |
| 단위 | amount/time | time⁻¹ |
| 직관 | 얼마나 많이 바뀌는가 | 얼마나 빠르게 바뀌는가 |
| 체수분 예시 | 2.5 L/day는 커 보임 | 0.06 day⁻¹, 전환 시간 17 days는 느린 과정임을 보여 줌 |

**잠금(Lock)**: $R_t$만 보면 큰 풀의 느린 전환을 빠른 과정으로 오해할 수 있다. 속도는 $k_t$와 $t_t$가 더 잘 말한다 [T pp.45–46].
<!-- /CONFUSION -->

---

# §7 — 자기 테스트: 능동 회상 모듈(Self-Test: Active Recall Module)

<!-- SELF-TEST -->
## Q1. 모델링 회전목마에서 fitting은 몇 번째 단계이며, 왜 그 앞 단계가 중요한가?

**기대 답안(Expected answer)**: fitting은 5단계다. 4단계 EDA가 모델 구조와 초기 추정치를 제안하고, 비선형 fitting 알고리즘은 초기 추정치에 민감하기 때문이다 [G pp.5–6].

## Q2. NCA가 충분한 질문과 구획 모델(compartmental model)이 필요한 질문을 하나씩 들어라.

**기대 답안(Expected answer)**: 생체이용률 또는 총 청소율 요약이 목적이면 NCA가 충분할 수 있다. 단회 투여 데이터로 반복 투여 결과를 예측하거나 비선형 약동학 또는 PK/PD 관계를 정량화하려면 모델이 필요하다 [G p.4].

## Q3. 치료역(therapeutic window)을 용량이 아니라 노출 관점에서 설명하라.

**기대 답안(Expected answer)**: 너무 낮은 노출은 무효 치료로, 너무 높은 노출은 이상 반응 증가로 이어지며, 둘 사이에서 치료 반응을 얻고 과도한 이상 반응을 피하는 노출 범위가 치료역이다 [T p.6].

## Q4. Digoxin과 morphine 요법 차이를 "투여 빈도 차이"가 아니라 PK/PD 원리로 설명하라.

**기대 답안(Expected answer)**: 두 약물 모두 좁은 치료역을 가질 수 있지만 morphine은 빠르게 제거되어 자주 투여가 필요하고, digoxin은 천천히 제거되어 1일 1회가 가능하다. Digoxin은 빠른 도달과 유지가 분리되어 디지탈화 용량 + 유지 용량(maintenance dose) 논리가 나온다 [T pp.4, 7].

## Q5. $\gamma=1$과 $\gamma=2$에서 20–80% 반응 농도 범위는 어떻게 다른가?

**기대 답안(Expected answer)**: $\gamma=1$이면 $0.25C_{50}$에서 $4C_{50}$까지 16배, $\gamma=2$이면 $0.5C_{50}$에서 $2C_{50}$까지 4배다 [T p.40].

## Q6. Propranolol과 alfentanil 예시가 각각 가르치는 것은 무엇인가?

**기대 답안(Expected answer)**: Propranolol은 비결합 농도와 등급 반응이 Hill 방정식으로 설명되는 예시이며 $\gamma\approx1$, $E_{\max}\approx40\%$, $C_{50}=5.3\,\mu g/L$다. Alfentanil은 이분형 반응에서 C50가 집단 사건 확률(population event probability)의 기준이 됨을 보여 준다 [T pp.42–43].

## Q7. 농도 최고점과 효과 최고점이 분리되어 있을 때, 어떤 사고가 켜져야 하는가?

**기대 답안(Expected answer)**: 직접 효과 Hill만으로 충분한지 의심하고 전환/지연 구조를 고려해야 한다. Warfarin과 paclitaxel은 농도-시간과 반응-시간이 분리되는 예시다 [T pp.8–9].

## Q8. $R_t=2.5$ L/day인 총 체수분 전환이 왜 "빠른 과정"이라고 단정할 수 없는가?

**기대 답안(Expected answer)**: 풀 크기가 42 L이므로 분획 전환 속도는 0.06 day⁻¹이고 전환 시간은 17 days다. 양/시간이 커도 풀 대비 분획이 작으면 과정은 느리다 [T pp.45–46].

## Q9. Fig.2-19의 두 시나리오가 노출 지표 선택에 주는 메시지는 무엇인가?

**기대 답안(Expected answer)**: 같은 Cmax/tmax라도 감소 속도가 다르면 AUC와 유지 기간이 달라질 수 있고, 같은 AUC라도 입력 속도가 다르면 Cmax와 tmax가 달라진다. 어떤 지표가 중요한지는 임상 목표와 노출-반응 관계에 따라 달라진다 [T p.44].
<!-- /SELF-TEST -->

---

# §8 — 메타프레임 & 큰 그림(Meta-Frame & Big Picture)

## A. 위치(Positioning)

<!-- MASTER LENS -->
이 세션의 목표는 "PK/PD 용어 암기"가 아니라 **후속 모델링 판단의 언어를 잠그는 것**이다. M1은 사고 순서를 정한다. M2는 임상 목적 함수를 정한다. M3는 농도-반응 형태를 정하고, M4는 시간 지연과 내인성 시스템을 해석한다.
<!-- /MASTER LENS -->

## B. 의존 관계(Dependencies)

- M1 없이 후속 GOF/진단 세션으로 가면, 소프트웨어 출력을 모델 타당성(model validity)으로 오해한다.
- M2 없이 구획 PK로 가면, 농도-시간 곡선을 임상 반응과 분리해서 보게 된다.
- M3 없이 PD 모델링으로 가면, 효능, 천장, 가파름, 평가변수 유형을 한 덩어리로 오해한다.
- M4 없이 간접 반응으로 가면, 지연 반응을 단순 분포 지연이나 부적합으로만 오해한다.

## C. 전문가 해석 지점(Professional Lock) — [EXPERT_INFERENCE, v3]

<!-- RECAP -->
이 세션의 원리를 구조적으로 내재화한 계량약리학자(pharmacometrician)가 새 데이터셋 앞에서 갖는 것은 다음 네 개다.

- **모델링은 질문 기반 워크플로(question-driven workflow)다**: 질문 없이 시작하는 fitting은 답 없는 수식이다. 데이터를 받는 순간 "무엇을 결정하기 위한 모델인가"를 먼저 쓸 수 있어야 한다. 이 한 줄이 없으면 EDA, fitting, 진단의 모든 단계가 목적지 없는 출력이 된다.
- **PK/PD의 핵심 번역 좌표**: 용량 → 노출 → 반응. 이 세 좌표 사이 어디에서 개체간 변이(IIV)가 생기는지 식별하는 것이 거장의 첫 진단이다. PK 변이인지 PD 변이인지 구분하지 못하면 공변량 탐색(covariate search)을 엉뚱한 층(layer)에서 하게 된다.
- **Emax/Hill은 "천장-효능-가파름"의 3축 문법이다**: 이 셋을 분리하지 못하면 노출-반응 해석이 무너진다. C50만 보고하는 보고서는 천장과 가파름 정보를 버린 것이다. γ의 식별 가능성 문제를 모르면 잡음을 파라미터로 오인한다.
- **전환은 "지연된 상태"의 첫 번째 문법이다**: 반응이 늦는 이유가 분포 지연(distribution lag)인지 내인성 시스템 역학(endogenous system dynamics)인지를 구분하는 관문이다. 이 구분이 없으면 간접 반응 모델 채택의 근거를 설명할 수 없고, 지연 반응을 부적합이나 이상치(outlier)로 오해하게 된다.
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

ver2 anchors are unchanged from ver1 because the three card title strings were not modified. v3.2 Korean-Dominant Readability Patches do not alter anchor strings.

| Marker # | Anchor text | Anchor found? | Match count | Inserted? | Final location (§ + card) |
|---|---|---|---|---|---|
| 1 | `## Card M1 ⚡ Apex Concept — Modeling Carousel & 5대 Dysfuncti` | YES | 1 | YES | §2 → Card M1 |
| 2 | `## Card M2 — PK/PD Linkage & Therapeutic Window [T pp.3–17]` | YES | 1 | YES | §2 → Card M2 |
| 3 | `## Card M3 — Emax / C50 / Hill γ [T pp.35–43]` | YES | 1 | YES | §2 → Card M3 |

### B9. Zero-Omission Coverage Matrix (v3.2 re-verified)

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
| C6 Page tag integrity | Existing [p.XX]/[pp.XX–YY] tags preserved; no new page tags created by mastery notes, ver2 changes, v3 patches, v3.1 Korean Readability Patches, or v3.2 Korean-Dominant Readability Patch | PART A body | PRESENT | None |
| C7 Crucible Grade A preservation | Carousel as nonlinear-fitting necessity, M3 vs M4 entry rule, γ as response sensitivity, endpoint-scale warning | Mastery notes and §2/§5/§8 body | PRESENT_COMPRESSED | None |
| C8 Deprecated draft regression | Unsupported FIH/FDA claims, AUC 30–50%, OFV>5, 4-starting-value rule, CYP2C9/VKORC1 unsupported wording, unapproved code blocks not restored | PART B forbidden restoration list | PRESENT | None |
| C9 Canonical integrity | Content Lock v2 learner body preserved except approved figure pointer splices, the bounded Mastery Augmentation Layer, ver2 assembly edits, v3 labeled augmentations, v3.1 Korean Readability Patches, and v3.2 Korean-Dominant Readability Patch | PART A; logs below | PRESENT | None |
| C10 Learner-Standalone (v3) | PART A contains no audit/process/compiler appendix text; all v3 additions are learner-facing augmentations in PART A; v3.1/v3.2 patches improve Korean prose readability of existing learner content only | PART A inspection | PRESENT | None |
| C11 v3 Apex standardization | `[⚡ Apex Concept]` label is on M1 heading (existing) and C-2 Plausible Fallacy block is present | §2 Card M1 | PRESENT | None |
| C12 v3 Memory Hook label | `**⚡ 기억 고리 (Memory Hook)**` standardized in §5 Pair 1 | §5 Pair 1 | PRESENT | None |
| C13 v3 Professional Moat | §8.C expanded to 4 structural competency bullets, labeled [EXPERT_INFERENCE, v3] | §8.C | PRESENT | None |
| C14 v3 Practice Briefs | Practice Brief 4축 block present in each M1–M4 card, labeled [EXPERT_INFERENCE, v3] | §2 Cards M1–M4 | PRESENT | None |
| C15 v3.1 Korean Readability Patches | 13 Low-risk prose patches applied (P-001 ~ P-013) | §2 Cards M1–M4, §2 Recap, §5 Pair 1 | PRESENT | None |
| C16 v3.2 Korean-Dominant Readability Patch | All learner-facing English prose converted to Korean-dominant form; career-critical terms retained as Korean(English) paired expressions; all section headers, labels, explanatory text Korean-dominant | PART A — all §1–§8 | PRESENT | None |

### B10. Micro-Patch Log

ver1 had no scientific micro-patches. ver2 also introduces no scientific micro-patches; the changes below are assembly-only. v3 introduces labeled interpretive augmentations (no scientific content change). v3.1 introduces Korean Readability Patches only (no scientific content change). v3.2 introduces Korean-Dominant Readability Patches only (no scientific content change).

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
| Δ11 | Korean Readability Patch | 13 Low-risk PART A prose patches (P-001 ~ P-013) applied. | None — sentence-level Korean prose only; no new page tag, equation, numerical value, drug example, figure decision, or external claim. All anchor strings unchanged. |
| Δ12 | Korean-Dominant Readability Patch | All learner-facing English prose in PART A converted to Korean-dominant form: section headers → Korean(English) paired; English labels → Korean(English); remaining English explanatory sentences → Korean; career-critical terms → Korean(English) on first use. FIGURE_POINTER internal English fields preserved verbatim. PART B unchanged except metadata updates. | None — prose-language conversion only; no new scientific claims, page tags, equations, numerical values, drug examples, figure decisions, or external references. All anchor strings unchanged. PATCH MODE Splice Verification Table (B8) unaffected. |

No page tags were created, deleted, or corrected in v3.2. No equations were modified. No figures were added, removed, or altered. No examples or numerical anchors were added or removed.

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
| 11 (v3.1) | §2 Cards M1–M4, §2 Recap, §5 Pair 1 | Korean Readability Patches (13 Low-risk) | YES | KOREAN_PROSE_POLISH, v3.1 | Improves learner-facing Korean prose readability via first-use glosses, sentence connectors, parallel-structure clarification, and tone smoothing. No mastery content added. | Low — sentence-level prose only |
| 12 (v3.2) | PART A — all §1–§8 | Korean-Dominant Readability Patch | YES | KOREAN_DOMINANT_PROSE_PATCH, v3.2 | Converts all remaining learner-facing English prose to Korean-dominant form: section headers, labels, explanatory text. Career-critical terms retained as Korean(English) paired expressions on first use. No mastery content added. | Low — prose-language conversion only; no scientific content, page tag, equation, figure marker, or anchor string altered |

#### Rejected or deferred augmentation candidates

| Rejected candidate | Reason for rejection |
|---|---|
| Add explicit OFV/RSE/condition-number thresholds | Rejected: unsupported numerical or diagnostic thresholds outside PDF/Audit-allowed content. |
| Add new clinical or regulatory examples | Rejected: would introduce external examples and source-boundary risk. |
| Add a fourth figure pointer for M4 | Rejected: Phase 4C budget exceeded; R4 was explicitly rejected. |
| Add Mermaid/SVG schematic at Phase 4D | Rejected: Phase 4D is not Phase 5 and image rights are None. |
| Add a §7 Q10 boss dilemma (Socratic) | Deferred: ver1 Self-Test (Q1–Q9) was finalized through Phase 4B-2 and not flagged by Audit/Crucible. Adding a new question now would risk creating new content; out of scope for ver2 assembly fix and v3.2 readability patch. |

## Final Checklist (v3.2)

| Check | Status |
|---|---|
| PART A alone is learner-facing and complete | PASS — v3.2 patches convert English prose to Korean-dominant form; PART B is compiler-only |
| PART A contains no audit/process/compiler appendix text | PASS |
| Approved figure markers are present exactly once | PASS — 3 markers, one-field-per-line format, content unchanged by v3.2 |
| No unapproved figure markers were added | PASS |
| Source page tags were preserved; no new page tags were fabricated | PASS — v3.2 patches added zero new page tags; all [G p.X], [T p.X], [T pp.X–Y] tags preserved verbatim |
| Audit/Crucible were not used as uncontrolled raw prose sources | PASS |
| Deprecated Step 1 Draft v0 material was not restored | PASS |
| Mastery augmentations are labeled and within B-Standard budget | PASS — 6 ver1/ver2 augmentations + 4 v3 augmentations + 1 v3.1 patch group + 1 v3.2 patch; all properly labeled |
| No unsupported numerical values, new examples, equations, or page tags were introduced | PASS |
| PART B contains Phase 5 rendering requirements and navigation anchor integrity rules | PASS |
| No HTML, Mermaid, SVG, or image embed generated in Phase 4D | PASS |
| v3.2 changes are Korean-dominant prose conversion only and do not alter scientific content, equations, or page tags | PASS |
| §5 Pair 1 has a structural memory hook with standardized label `**⚡ 기억 고리 (Memory Hook)**` (v3) | PASS |
| §1 Roadmap shows Apex visual cue consistent with M1 card heading | PASS |
| FIGURE_POINTER blocks parseable line-by-line by Phase 5 | PASS |
| Card M1 has `[⚡ Apex Concept]` in heading AND `C-2 Plausible Fallacy` block (v3) | PASS |
| §8.C Professional Lock expanded to 4-bullet block labeled [EXPERT_INFERENCE, v3] (v3) | PASS |
| Cards M1–M4 each have Practice Brief 4축 block labeled [EXPERT_INFERENCE, v3] (v3) | PASS |
| 13 v3.1 Korean Readability Patches applied surgically; all anchors unchanged (v3.1) | PASS |
| v3.2 Korean-Dominant Readability Patch applied; all learner-facing English prose Korean-dominant; all anchors unchanged (v3.2) | PASS |

---

## v3.2 Final Checklist

| # | Criterion | Status | 근거 |
|---|---|---|---|
| 1 | **PART A가 한국어 중심으로 바뀌었는가** | **PASS** | 모든 학습자 대면 영어 산문이 한국어로 변환됨. 섹션 헤더는 한국어(English) 병기. 레이블(Mastery Note, Practice Lens, Judgment Lens, Practice Brief, Trench-level tip, Formal Definition, Structural Necessity, Limitations, Diagnostic Lock, Zettelkasten Atom, Key example, Equation block, Cognitive Lock, Critical Blow, Memory Hook, Recap, Big Idea, Expected answer 등)이 한국어(English) 형식으로 변환됨. 일반 설명문이 한국어로 전환됨. |
| 2 | **과학적 내용 보존** | **PASS** | 모든 과학적 주장, 약물 예시(warfarin, paclitaxel, propranolol, alfentanil, ketamine, digoxin, morphine, total body water), 수치 앵커($C_{50}=5.3\,\mu g/L$, $C_{\max}=96\,\mu g/L$, 1.5 mg/kg, 0.27/0.31/0.42 mg/L, 42 L, 2.5 L/day, 0.06 day⁻¹, 17 days 등), 파라미터 관계, 개념 정의 원문 보존. |
| 3 | **수식 보존** | **PASS** | 모든 MathJax 수식 그대로 보존: 1구획 예측, 관측 오차, Hill/Emax, γ=1/γ=2 범위 표현, 전환 관계식. 인라인 수학 보존. |
| 4 | **Page tag 보존** | **PASS** | 모든 page tag 원위치·원문 보존: [G pp.1–7], [G pp.1–2], [G pp.3–4], [G p.4], [G p.6], [T p.3], [T p.4], [T p.5], [T p.6], [T p.7], [T pp.4, 7], [T p.8], [T pp.8–9], [T pp.10–12], [T p.10], [T p.12], [T p.20], [T p.21], [T pp.21–22], [T pp.23–25], [T pp.26–33], [T p.40], [T pp.40–41], [T pp.40–43], [T p.41], [T p.42], [T pp.42–43], [T p.43], [T p.44], [T p.45], [T pp.45–46], [T p.46]. v3.2 패치에서 새 page tag 없음. |
| 5 | **Figure marker 보존** | **PASS** | 세 FIGURE_POINTER 블록 원문 보존 (Source / Why this matters / When to look / Learner instruction 영문 필드 포함). B2 Figure Rendering Instructions 테이블 미변경. |
| 6 | **소스 경계 보존** | **PASS** | 새 과학적 주장, 새 예시, 새 수치 앵커, 새 외부 참조, 새 규제 주장 없음. PART B B5 Audit Guardrails 금지 복원 목록 유효. |
| 7 | **HTML 준비 상태 보존** | **PASS** | 모든 마커 규약 유지. B4-1 마커→컴포넌트 매핑 미변경. B4-2 네비게이션 앵커 무결성 규칙 미변경. PATCH MODE Splice Verification Table (B8) 미변경 — 카드 제목 앵커 문자열 원문 유지. |
| 8 | **Phase 5 HTML 컴파일 준비 완료** | **PASS** | 모든 Phase 4D 인증 통과. PART A 학습자 독립 완결. PART B 컴파일 계약 유지. FIGURE_POINTER 3개 splice 준비 완료. Page tag 렌더링 규칙(B3) 준비 완료. Self-test 아코디언 매핑 준비 완료. **GO for Phase 5 HTML Compile.** |

---

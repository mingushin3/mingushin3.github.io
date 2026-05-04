# 13_Crucible Report v1

**Session 13 — 개체 간 변이 (IIV/BSV) 와 공변량 모델링**
**Mode**: [논문·연구 리뷰] · **Personas**: P1 (30-year senior mentor) + P3 (FDA reviewer)
**Inputs cross-checked**: 013_G PDF (G&W Ch.4 p.333-352 + PK50 p.704-710), 013_T PDF (R&T Ch.12-13 p.361-410), 13_step1_draft_v0.md, 13_Audit_Report_v1.md, 13_scope_lock.md, S13_phase1_patch_memo.md
**Operative filter**: "30년 베테랑이 5분 안에 후배 1년차 박사과정생에게 이 챕터를 영구적으로 한 단계 끌어올리려면 무엇을 더 말할 것인가?"
**Non-mandate**: Step 1을 다시 쓰지 않는다 / 요약하지 않는다 / HTML을 만들지 않는다 / Audit MUST_FIX를 건드리지 않는다.

---

## T1. P1 — Internalization Barriers & Master's Intuitions

### (a) Cognitive Walls — 외울 수는 있으나 보이지 않는 것

**Wall 1 — ω²/σ² 보존 법칙 (Variance conservation)**
박사과정생은 "η는 between-subject, ε는 within-subject"를 정확히 암송할 수 있다. 그러나 *고정된 데이터셋 안에서 ω²과 σ²이 동일한 총 변이를 두고 zero-sum으로 경쟁한다*는 사실을 보지 못한다. 잔차 모델 오설정이 ω²으로 새는 메커니즘은 신비가 아니라 보존 법칙의 결과다 — ε가 흡수하지 못한 분산은 반드시 η가 가져가고, 그 역도 같다. Step 1의 C1·C2가 별개의 카드로 배치되어 있어 *둘이 보존 관계의 두 면*이라는 직관이 약하다.

**Wall 2 — fu의 정체 (PK50 reparameterization vs covariate)**
박사과정생은 "fu가 covariate로 도입되어 ω²을 깎는다"는 문장을 외울 수 있다. 그러나 PK50에서 일어나는 일은 NONMEM covariate model의 적용이 *아니라* unbound 좌표계로의 deterministic reparameterization (`CL = fu·CL_u`)이다. Total Cl CV 28%와 unbound Cl_u CV 9%는 *같은 12명 환자, 같은 데이터*의 두 표현일 뿐 — 분산은 사라진 게 아니라 fu 측정값으로 옮겨갔다. Audit가 정정한 표현(`PK50 reports total Cl CV 28% and unbound Clu CV 9%`)이 통계적으로 옳은 만큼이나 인지적으로도 옳다는 사실을 학습자가 *직관적으로* 받아들이도록 하나의 짧은 brick이 필요.

**Wall 3 — Categorical covariate의 빈 셀 (Empty cell trap)**
박사과정생은 PM/IM/EM/UM 4-level IF-THEN 구조를 코딩할 수 있다. 그러나 PM(n=3)의 THETA factor가 ETA(1)에 흡수되어 *시각적으로 사라지는* 메커니즘 — 즉 phenotype 효과를 잡지 못하면 그 자리를 within-phenotype η가 메우고 ω²이 인공적으로 inflate되는 conservation 결과 — 을 즉각 보지 못한다. C4의 IF-THEN 코드가 그대로 학습되면, "코드는 돌지만 모델은 무력화"되는 NDA 시나리오를 직접 만들어낸다.

### (b) System Integration — 이 세션의 개념들이 단일 시스템으로 작동하는 지점

이 챕터의 4-card는 추상적으로 연결된 것이 아니라, 실무에서 다음 *세 지점*에서 단일 메커니즘으로 동시에 작동한다:

**Integration 1 — Phase 1 → Phase 2 transition (model maturation cascade)**
Phase 1에서 RUV 구조(C2)가 잘못 잡히면, Phase 2 covariate selection(C3) 단계에서 진짜 covariate가 reject되거나 가짜 covariate가 detect되는 *cascade*가 발생한다. 즉 C1·C2의 정확성은 C3·C4의 모든 결론을 *조건적으로* 지배한다 — 이 의존성이 Step 1 §8 B (Dependencies)에 numerically 5개로 나열되어 있으나, *Phase boundary*가 그 cascade의 trigger라는 시간적 구조는 명시되어 있지 않다.

**Integration 2 — Bayesian TDM 알고리즘 (clinical translation point)**
ω²/σ² *비율*이 single-sample TDM에서 prior(인구 평균)와 posterior(개인 측정)의 가중치를 결정한다. ω² >> σ²이면 single sample이 prior를 압도해 EBE가 측정값을 따라가고, ω² ≈ σ²이면 prior가 EBE를 강하게 끌어당겨 1-2 sample TDM이 무력화된다. 이 비율이 Session 13의 추상이 임상 알고리즘으로 번역되는 *바로 그 지점*이며, Step 1은 §8 Dependencies에서 1줄 언급에 그쳤다.

**Integration 3 — NDA Section 5.2 PopPK report (regulatory deliverable)**
ω², σ², shrinkage, η_EBE distribution, residual structure는 reviewer가 *순차적으로 읽는* line items이며, reviewer가 실제로 감사하는 것은 *이들 사이의 상호 일관성*이다 — 예를 들어 σ²(prop)으로 보고된 CV가 bioanalytical assay validation 보고서의 CV와 일치하지 않으면, 모델 전체의 prior justification이 흔들린다.

### (c) Master's Intuition — 30년 베테랑이 방정식 없이 즉각 판독하는 것

**Intuition 1 — "낮은 shrinkage = 좋은 모델"이 아닌 경우**
"ω²(CL) = 0.06, η-shrinkage = 5%, η-EBE histogram 정규성"이라는 보고서를 받으면, 베테랑은 안심하지 않고 *데이터 sparsity를 먼저 묻는다*. 환자당 sample 수가 < 2이면 낮은 shrinkage는 정보 부족(추정 자체가 prior로 끌려간 결과)의 시그니처이지 model fit의 증거가 아니다. Rich data와 결합되었을 때만 의미를 가진다. (※ shrinkage 자체는 audit T1에서 [교과서 외 후속 구현 지식]으로 격하되었으므로, 본 직관은 C2의 limitations 항목에 그 forward pointer 형태로만 등장해야 한다.)

**Intuition 2 — "효과 없음"이 아닌 "효과 흡수됨"의 즉각 식별**
"CYP2D6 PM 5명 모두 ETA(1) ≈ 0"이라는 결과를 받으면, 베테랑은 즉각 *RUV 오설정 또는 prior에의 흡수*를 의심한다. 진짜 효과가 있는데 모델이 못 잡는 가장 흔한 시그니처가 바로 이것이며, "phenotype 효과 없음"으로 결론짓는 것이 가장 위험한 false negative.

**Intuition 3 — PK50 EC50 paradox의 한 줄 판독**
PK50의 EC50이 total 1.8 µg/L (CV 40%)에서 unbound 0.029 µg/L (CV 60%)로 변환되어 *변이가 증가했다*는 것을 보면, 베테랑은 "fu는 PK 좌표계 변환에는 작동하지만 PD 변이의 진짜 source는 다른 곳(receptor density)에 있다 — fu 보정이 그것을 가렸을 뿐"을 즉각 데이터에서 직접 읽어낸다. G&W p.708-709가 이 결론을 명시적으로 적고 있으며, "all subjects with maximum response less than one response unit also lacked full expression of the target"이 그 직접 증거.

**Intuition 4 — `$OMEGA` block 구조를 `$THETA`보다 먼저 보기**
NONMEM control stream을 받으면 베테랑은 `$THETA` 줄보다 `$OMEGA` block 구조를 먼저 본다. Block diagonal vs full block 결정이 Cl-V correlation 같은 mechanism-level 가정을 *코드 한 줄로* 인코딩하기 때문이다. Diagonal로 시작해 수렴 안 되면 block으로 전환하는 것은 역순서이며, mechanism-level prior에서 출발하는 것이 정도다.

---

## T2. P3 — Regulatory & Practical Risk Surface

### (a) Step 1을 통과한 이후에도 남는 NDA-level Risk

Audit의 MUST_FIX(deficiency letter / 21 CFR / 비용·기간 문장 삭제)가 적용된다는 가정 하에서, 다음 simplification들이 *여전히* Section 5.2 review에서 risk signal로 작동한다:

**Risk 1 — Variance propagation의 "reasonable agreement" 무마**
Step 1 §7 Q2의 정답은 $0.28^2 - 0.31^2$이 음수가 되는 결과를 "두 변량이 약한 음의 상관"으로 해석한다. Audit T1이 이 propagation 자체를 ERROR로 분류했으나, 더 근본적인 P3 risk는 *분포 가정이 명시되지 않은 채로* 분산 합산을 시도했다는 것이다. Reviewer는 "fu와 Cl_u의 결합 분포가 어떤 형태로 가정되었는가, 독립성 검증은 어떻게 했는가"를 묻는다. → 권장 조치: Audit가 지시한 대로 propagation 주장 자체를 삭제하고, "PK50의 표 50.1 수치가 그 자체로 fu의 변이가 total 변이의 일부를 설명한다는 강한 데이터 anchor이다"로 *기술 기반*에서만 멈춘다.

**Risk 2 — Phenotype frequency의 인구 reference 미명시**
C4의 PM 5-10%, IM ~30%, EM ~50%, UM 1-3% 표는 audit T1에서 ERROR로 분류되었다(IM/EM/UM은 R&T Table 13-1에 직접 수치 없음). 그러나 PhD-level deliverable에서 더 깊은 리스크는 *frequency가 제시될 때 인구 reference가 명시되지 않으면 라벨의 generalizability가 즉시 의심받는다*는 것 — Asian, African American, Caucasian 사이의 frequency 차이가 표 13-1에서 직접 보이는데도 단일 숫자로 표기하면 reviewer는 "어느 인구의 라벨인가"를 첫 질문으로 던진다.

**Risk 3 — Apex Concept C2의 "Phase 2/3 default" 단정**
S13_phase1_patch_memo가 이미 지적했듯, "Mixed RUV는 Phase 2/3 default" 표현은 *왜 이 데이터에서 mixed가 옳은가*에 대한 a priori justification(assay characteristic, sampling design, LLOQ proximity)을 결여한 채로는 post-hoc model selection의 우려를 생성한다. Audit의 MUST_FIX와 일치하지만, 추가로 P3 관점에서 *모델 선택 근거의 시간적 순서*가 보고서에 명시되어야 한다는 점을 강조한다.

### (b) 이 세션의 개념을 잘못 이해할 때 NONMEM이 만드는 진단 시그니처

다음 셋은 §6 (Phase 4C 실용 시나리오)에 1줄씩 anchor로만 등장해야 한다 — 본 보고서에서 그 *카탈로그*만 제공:

**Signature 1 — "ω²-σ² Leakage Funnel"**
Proportional-only RUV + LLOQ-rich data에서 ω²(CL)이 비현실적으로 inflate (예: PK50 scale 데이터에서 ω²(CL) > 0.5에 해당하는 추정치). 시각적 시그니처: CWRES vs PRED plot에서 LLOQ 근처 funnel + η-shrinkage spike. 처방: Mixed RUV로 전환 후 재추정.

**Signature 2 — "Empty Phenotype Cell"**
Categorical covariate를 4-level full stratification으로 정의했으나 PM(n=3) THETA factor의 RSE가 80%를 넘고 `$COV step`이 "non-positive definite" 메시지로 실패. 처방: 인접 phenotype 통합("reduced function" 단일 카테고리) 또는 informative prior 도입.

**Signature 3 — "Vanishing Covariate Cascade"**
진짜 covariate(CrCl)가 모델에 없으면 η_CL이 그것을 흡수하고, 후속 stepwise selection에서 *상관 covariate*(weight, BSA)가 가짜로 detect된다. 시그니처: η_EBE vs CrCl scatter는 평탄하지만 Cl_obs vs CrCl는 명확한 기울기. 처방: domain knowledge 기반 candidate covariate를 a priori 정의 후 stepwise.

### (c) 가장 파급력 큰 Confusion Pair — Critical Blow의 재배치

Step 1은 Critical Blow를 Pair 1 (ω² vs σ²)에 적용했고, 그 시나리오는 Audit T1에서 NDA-cost 주장이 NOT_IN_SOURCE로 분류되어 무력화되었다. P3 관점에서 *audit 제약 안에서도 살아남는* 가장 높은 파급력의 pair는 **Pair 2 (Total Cl vs Unbound Cl_u)** 이다.

이유: PK50의 G&W p.705는 "total plasma concentrations above 50 µg·L⁻¹ should be avoided"라고 *total 좌표계*에서 safety threshold를 설정한다. 그러나 unbound parameter를 사용해 dose individualization 알고리즘을 만들면, 라벨의 권고가 Phase 1 safety 근거와 *서로 다른 좌표계*에서 표현되며, reviewer는 "어느 좌표계가 라벨의 권위를 가지는가"를 묻는다. 답이 명확하지 않으면 라벨의 dose recommendation 자체가 reissue 대상. 이 risk는 audit가 삭제한 외부 NDA 비용 주장에 의존하지 않으며, *G&W 본문 안에서 직접 도출되는* 좌표계 일관성 문제이므로 source-locked 콘텐츠로 살아남는다.

---

## T3. Trench-Level Tips (4 items)

### Tip 1 — `$OMEGA` block 구조 결정의 정도(正道)
- **Situation**: 2-구획 모델에 IIV를 부여하기 시작할 때
- **Trap**: Diagonal `$OMEGA`로 시작 후 "수렴 안 되면 block으로 전환"하는 역순서 결정. Cl-V가 같은 organ size에 의해 함께 변동하는 mechanism-level 사실을 무시.
- **Detection**: OFV가 떨어졌음에도 η_Cl-η_V scatter에서 명백한 직선 추세가 보이고, IIV에 적합한 lognormal 가정이 실제 데이터의 ellipsoidal 분포를 못 잡음
- **Insert at**: §2 C1, F. Five Cognitive Layers, L2 (Vol II) cell
- **Insert text**: "`$OMEGA` block 구조는 mechanism-level prior에서 출발하라 — Cl과 V가 같은 organ size에 의해 함께 변할 것으로 예상되면 `$OMEGA BLOCK(2)`로 시작하고, diagonal은 *증거가 있을 때만* 후퇴 옵션으로 둔다."

### Tip 2 — fu를 covariate로 입력할 때 ETA의 정확한 위치
- **Situation**: PK50 형태의 multi-subject dataset에서 fu를 활용해 unbound 좌표계로 전환할 때
- **Trap**: Total parameter (CL_total)에 ETA를 붙인 채 fu를 simultaneously data column으로 입력. 변환의 일부가 ETA에 흡수되어 ω²이 데이터-모델 사이에서 oscillate.
- **Detection**: 같은 데이터에 두 가지 parameterization을 적용했을 때 ω²(CL)의 추정치가 일치하지 않음 (보존 법칙 위반의 시그니처)
- **Insert at**: §2 C3, B. Derivation/Code Structure, NONMEM 코드 블록 직후 (audit가 [교과서 외 구현 번역] 라벨링한 그 블록 안)
- **Insert text**: "ETA는 unbound 파라미터 (`CL_u`, `V_u`)에 부여하고 fu는 data column으로 입력 — total 좌표계로의 변환은 *deterministic mapping*이지 random effect가 위치할 자리가 아니다."

### Tip 3 — Phenotype categorical level의 데이터 비례 통합
- **Situation**: CYP2D6 또는 CYP2C9 phenotype을 NONMEM 모델에 도입할 때
- **Trap**: PM/IM/EM/UM 4-level full stratification을 처음부터 펼침. 작은 n의 cell (특히 PM, UM)의 THETA factor RSE가 폭증.
- **Detection**: `$COV step` 실패 메시지 ("covariance matrix is non-positive definite") + 작은 n 카테고리의 RSE > 80%
- **Insert at**: §2 C4, B. Derivation/Code Structure, NONMEM 코드 블록 직후 (audit가 [교과서 외 구현 번역] 라벨링한 그 블록 안)
- **Insert text**: "Phenotype level은 데이터 size에 비례해 통합하라 — 작은 n의 cell은 인접 phenotype과 합치거나(예: PM+IM = `reduced function`) informative prior로 안정화한다; 4-level full stratification은 데이터가 명확히 허용할 때만."

### Tip 4 — Sparsity 정보 없는 shrinkage 보고의 위험
- **Situation**: η-shrinkage 진단을 보고서에 기재할 때 (audit가 본 내용을 [교과서 외 후속 구현 지식]으로 격하한 후에도 forward pointer로 등장 가능)
- **Trap**: shrinkage 단일 수치로 모델 품질을 판단. Sparse data에서의 낮은 shrinkage는 정보 부족(prior 흡수)의 시그니처일 수 있음.
- **Detection**: 환자당 sample 수 분포와 shrinkage를 *함께* 보지 않고는 진단이 불가능 — n_sample/patient < 2 cohort에서의 낮은 shrinkage는 model fit의 증거가 아니다
- **Insert at**: §2 C2, E. Limitations 마지막 항목
- **Insert text**: "η-shrinkage 진단은 환자당 sample 수 분포와 *반드시 함께* 보고하라 — sparse cohort에서의 낮은 shrinkage는 정보 부족의 시그니처이며 모델 품질의 증거가 아니다."

---

## T4. Deletion Candidates (Mandatory)

Audit MUST_FIX와 *별도로*, PhD 1-2년차 독자에게 분량 대비 한계 가치를 가지거나 중복인 항목들. 본 list는 비협상.

| 위치 | 사유 | 처분 |
|---|---|---|
| **§2 C1, C. Structural Necessity, item 3 ("Why two-stage")** | STS vs NLME 비교는 PhD 독자에게 Session 11-12 단계에서 이미 처리된 기초 | COMPRESS to 1 sentence: "STS는 sparse 환자에서 적합 실패 시 그 환자를 잃지만, NLME는 인구 정보를 빌려 EBE를 추정한다." |
| **§2 C1, F. Five Cognitive Layers, L3 row ("Bayesian hierarchical isomorphism")** | Bayesian-NLME 동형성은 후속 세션(Bayesian TDM)의 Apex 영역 — 본 세션에서 별도 row 차지가 비대 | COMPRESS to L1 또는 L4의 inline pointer (별도 row 제거) |
| **§2 C2, A. Formal Definition, "Exponential" row** | Additive/Proportional/Mixed 3개 contrast가 핵심; Exponential은 LTBS 논의에서 자연 등장 | DELETE row, LTBS 한 줄 노트로 흡수 |
| **§2 C3, D. Assumptions table, "Covariate가 시간에 따라 일정 또는 모델링됨" row** | 시간 가변 covariate는 별도 세션 주제 | DELETE row, §8 Dependencies로 forward pointer 1줄만 이동 |
| **§2 C4, F. Five Cognitive Layers, L5 row ("FDA Pharmacogenomic Biomarker label > 200 drugs")** | Audit T1에서 NOT_IN_SOURCE; Five Cognitive Layers 비대화의 추가 사유로 재확인 | DELETE row entirely |
| **§5 Pair 4 (NAD vs NPD vs Population)** | 이는 confusion pair가 아니라 *역사적 method 진화* — 별도 table 형식이 학습 부담만 증가 | COMPRESS to 3 sentences in §2 C1의 ANCHOR 직후 한 문단 |
| **§7 Q6의 정답 본문 마지막 단락 (mixture model 등 mini-essay)** | Audit가 ω²/shrinkage 정규성 핵심 통찰은 살림; mini-essay 분량은 PhD 독자에게 과잉 | COMPRESS to 2 sentences (sparsity dependence + bimodality 가능성만) |
| **§7 Q8 보스 딜레마의 "FDA 응답 prepared statement 예시"** | Audit MUST_FIX (deficiency letter 문장 삭제)와 일치; 추가로 prepared statement는 본 세션 학습 목표를 넘어선 *규제 작문* 영역 | DELETE entirely (Q8 본문은 trade-off 판단까지만 남김) |

---

## T5. Priority Matrix

### Grade A — 반드시 반영 (내면화 직접 개선 또는 규제 위험 직접 감소)

**A1.** §2 C1, C. Structural Necessity 직후에 Wall 1(보존 법칙) 1문장 삽입:
> "ω²과 σ²은 같은 데이터의 총 변이를 두고 경쟁하는 두 그릇이다 — 잔차 모델이 잘못 잡히면 사라진 분산이 ω²으로 새고, 그 반대도 같은 메커니즘으로 작동한다."

**A2.** §2 C3, B. Derivation/Code Structure NONMEM 코드 블록 직후에 Tip 2 (ETA 위치) 1문장 삽입.

**A3.** §2 C4, B. Derivation/Code Structure NONMEM 코드 블록 직후에 Tip 3 (phenotype level 통합) 1문장 삽입.

**A4.** §5 Pair 2 (Total Cl vs Unbound Cl_u) 행에 *Critical Blow 행 추가* — 또는 Pair 1의 Critical Blow를 Pair 2로 *이동* (Audit 제약 하에서 Pair 1 Critical Blow는 NDA-cost 주장 의존이라 무력화됨):
> "라벨의 dose recommendation이 total 좌표계와 unbound 좌표계 사이에서 일관성을 잃으면, Phase 1 safety 근거(total plasma C < 50 µg/L, G&W p.705)와 PopPK individualization(unbound)의 좌표계 정합 문제가 라벨 reissue 직접 사유가 된다."

**A5.** §2 C2, E. Limitations 마지막에 Tip 4 (sparse + shrinkage 동시 보고) 1문장 삽입.

**A6.** T4 deletion list 8개 항목 *전체 적용*. 이 deletion 없이 §2 C2/C3 카드의 무게중심이 audit MUST_FIX 적용 후에도 "Mixed RUV default"·"shrinkage threshold"의 외부 지식 쪽으로 기울어 있음.

### Grade B — 흐름 보존되면 반영 (enrichment value)

**B1.** §2 C1, F. Five Cognitive Layers, L1 row 끝에 Wall 2(fu reparameterization) 1문장 삽입:
> "PK50에서 fu는 NONMEM이 적용하는 covariate가 아니라 unbound 좌표계로의 deterministic reparameterization — 변이는 사라진 것이 아니라 fu 측정값으로 *재배분*된다."

**B2.** §7 Q5 정답 끝에 Master's Intuition 3 (PD 변이의 진짜 source) 1문장 추가:
> "fu의 PK 좌표계 변환은 unbound clearance 변이를 *드러내지만* PD 변이의 진짜 source(receptor density 등)는 가린다 — covariate 하나가 모든 변이를 설명한다는 가정 자체가 모델의 한계."

**B3.** §6 실용 시나리오 (Phase 4C 영역)에 Three GOF Signatures (Signature 1·2·3) 각 1줄 anchor.

**B4.** §8 Dependencies (B)에 System Integration Moment 3 (NDA Section 5.2 line-item consistency) 1문장 삽입:
> "NDA Section 5.2 PopPK report에서 ω², σ², shrinkage는 reviewer가 *순차적으로* 읽으며 *상호 일관성*을 감사한다 — 예를 들어 σ²이 bioanalytical assay validation 보고서의 CV와 일치하지 않으면 모델 전체의 prior justification이 흔들린다."

### Grade C — 거부 (scope creep, unsupported, 또는 기존 콘텐츠와 중복)

**C1.** Figure pointer 추가 — Phase 4C 영역; 본 Phase 3 Crucible 범위 밖.

**C2.** Mixture model `$MIX` 블록 상세 — §7 Q6 정답에서 이미 1회 언급; 별도 카드 추가는 분량 폭증.

**C3.** Bayesian TDM의 prior/posterior 가중치 수식 — Session 17 (Bayesian TDM) 영역; §8 forward pointer 1줄로 충분.

**C4.** PK50 individual fu 값 (G&W Table 50.3) 카드 본문 통합 — Audit T2에서 USEFUL but not required로 분류; 학습 부담 대비 marginal value.

**C5.** CYP2D6 phenotype 측정 방법론 (probe drug, genotyping platform 등) — 본 세션의 변이 분해 축에서 분기; pharmacogenomics 별도 세션 영역.

**C6.** G&W §4.6-4.7 Euler integration / Lineweaver-Burke / Scatchard — Step 1 Curation Map에서 이미 정확히 제외; 재검토 불필요.

---

## Cross-reference 안전 매트릭스

본 Crucible Report v1의 모든 권고는 다음 제약과 충돌하지 않는다 — 마지막으로 명시:

| 제약 원천 | 점검 결과 |
|---|---|
| Audit T1 NOT_IN_SOURCE 항목 | 본 Crucible에서 NDA cost·CFR·month 수치 등 외부 주장 *추가하지 않음* |
| Audit T1 ERROR 항목 | Variance propagation 주장은 Q2 정답에서 *제거 권고*만 (T2-a Risk 1) |
| Patch memo MUST_FIX 1-6 | 모두 audit와 일치, 본 Crucible은 이를 fixed constraint로 받음 |
| Scope Lock — page range | R&T p.361-410, G&W p.333-352·p.704-710 외 인용 *추가하지 않음* |
| Image rights = None | 본 Crucible에서 figure 새로 제안 *없음* (Phase 4C 영역) |
| 저작권 한계 | 본 보고서 안에 PDF 직접 인용은 G&W p.705 1구절(<15 단어)만 사용 |

---

## 종결 — Phase 3 Verdict

`Crucible Report v1 GO to Phase 4 (Step 2 HTML Compile preparation) — provided Grade A items A1~A6 are merged into Step 1 v1, and T4 deletions are applied.`

Step 1 v0의 4-card 골격, PK50 anchor의 강도, Boss Dilemma의 trade-off 논리는 PhD-level deliverable로서 우수한 수준. Audit MUST_FIX 적용과 본 Crucible의 Grade A 6개 적용 후, Step 1 v1은 Source Fidelity와 Master's Intuition의 두 축 모두에서 Phase 4 진입 가능 상태에 도달한다.

---

## PIPET-Vault Filing Metadata

- **저장 위치**: `02_LITERATURE/024_Gabrielson-Textbook/` (또는 `05_MEETINGS_AND_LOGS/Lectures/Session-13/`)
- **파일명**: `2026-05-04_Session13_Crucible-Report_v1_논문리뷰.md`
- **태그**: `#PopPK` `#IIV-RUV-decomposition` `#PK50-CpD` `#covariate-modeling` `#pharmacogenetics` `#P1_Action` `#P3_Audit`
- **링크 제안**:
  - `[[2026-05-04_Session13_Step1-Draft_v0]]` (선행 산출)
  - `[[2026-05-04_Session13_Audit-Report_v1]]` (병렬 제약)
  - `[[Bayesian-TDM-prior-posterior-weight]]` (후속 Session 17 forward pointer)
  - `[[NDA-Section-5.2-PopPK-report-template]]` (P3 deliverable forward)

---

*ID: C-260504-064218-K7Q*

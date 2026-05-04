# 04_Content Lock v1 — 청소율 · 간 · 신장 · 대사체

**Phase**: 4A Content Lock v1  
**Input set**: Original PDFs + `04_step1_draft_v0` + `04_Audit_Report_v1` + `04_Crucible_Report_v1`  
**Language**: Korean prose; English retained for technical terms, equations, drug names, NONMEM terms.  
**Output constraint**: Text only. No HTML. No figure markers. Textbook figure work is deferred to Phase 4C.  
**Source tag rule**: MUST cards, equations, and key examples retain page tags. Unresolved `[확인 필요]` items are retained rather than silently deleted.

---

## 0. Updated Curation Map

### 0.1 최종 MUST 항목 — 20개 초안을 14개 atom으로 압축

| ID | Final MUST atom | Source pages | Verdict logic |
|---|---|---:|---|
| **M1** | Clearance proportionality + AUC integration + half-life is derived | G pp.49, 77–79; T5 pp.124–128, 148–150 | ADOPT; half-life card는 독립 카드에서 M1로 흡수. |
| **M2** | Renal clearance decomposition: `CL_R`, `f_e`, filtration/secretion/reabsorption, additivity | G pp.48–56; T5 pp.138–148 | ADOPT; biliary/EHC와 clearance additivity는 CONTEXT로 압축 흡수. |
| **M3** | ARE plot vs excretion-rate plot + urine collection caveat | G pp.50–52, 497; T5 p.145 | ADOPT; Audit SHOULD_FIX인 “negligible urinary concentration까지 수집” 1문장 삽입. |
| **M4** | Well-stirred hepatic clearance derivation + Table 2.9 conceptual comparison | G pp.79–94; T5 pp.130–135; TE pp.777–778 | PARTIAL_ADOPT; Table 2.9 상세 수식은 `[확인 필요]`로 잠금. |
| **M5** | High/low extraction + route × extraction × `f_u` matrix | G pp.83–85; T5 pp.130–163 | ADOPT; IV/oral, total/unbound 해석을 하나의 matrix로 압축. |
| **M6** | IVIVE pitfalls: single-point, MMP, data condensation | G pp.85–90 | ADOPT; 외부 실무 claim은 삭제 또는 `[교과서 외 해석]`로 격하. |
| **M7** | PK5 simultaneous plasma+urine fitting; analytic vs ODE equivalence | G pp.494–499 | ADOPT; 초기값과 최종값을 분리. |
| **M8** | Plasma-to-blood ratio mechanism and blood clearance | T5 pp.124–128; TD pp.775–776 | ADOPT; extraction ratio는 blood 기준임을 명시. |
| **M9** | Permeability-rate-limited hepatic uptake: App.E `ρ` | T5 pp.136–138; TE pp.778–779 | ADOPT with correction; passive diffusion이 충분히 클 때 well-stirred로 환원. |
| **M10** | Extended clearance concept: transporter–enzyme architecture | T5 pp.136–138; TE pp.778–780 | ADOPT; M9와 겹치는 부분은 1개 bridge로 압축. |
| **M11** | Rate-limiting step in metabolite disposition | T20 pp.659–662 | ADOPT; renal impairment shortcut 삭제. |
| **M12** | `AUC(m)/AUC` decomposition: `f_m × CL/CL(m)` | T20 pp.662–665 | ADOPT with correction; `AUC(m)/AUC < 1`만으로 `CL(m) ≥ CL/f_m` 추론 금지. |
| **M13** | First-pass metabolite contribution + steady-state/multiple-dose metabolite | T20 pp.665–673 | PARTIAL_ADOPT; “oral이 항상 더 빠르고 강하다”는 보편화 삭제. |
| **M14** | Renal impairment active-metabolite scenario + interconversion | T20 pp.673–679 | ADOPT; parent `f_e`만으로 dose 조절하지 않는 원칙을 핵심으로 유지. |

### 0.2 CONTEXT 항목 — 전용 카드 없이 흡수

| Context | Final location | Compression decision |
|---|---|---|
| Nephron anatomy, GFR 110–130 mL/min, urine pH 4.5–8 | M2 | 1문단으로 압축. |
| Eq 2:107–2:108, Eq 2:115 urinary bioavailability | M7/M2 | 식만 보존, 별도 카드 없음. |
| Biliary excretion, enterohepatic cycling, pulmonary exception | M2 | clearance additivity의 예외·확장으로 2문장. |
| Half-life as secondary parameter | M1 | `t1/2 = 0.693·V/CL`로 통합. |
| Table 2.9 four hepatic clearance models | M4 | concept-level 비교만 보존; detailed formula `[확인 필요]`. |
| App.D Study Problem 1 | M8 | full numeric solution 삭제; formula 사용법만 보존. |
| App.E oral equations E-19/E-20 | M9/M13 | oral first-pass AUC bridge로 압축. |
| Carbamazepine autoinduction, halazepam plateau | M13 | exact visual values는 쓰지 않고 `[확인 필요]`로 처리. |
| Procainamide/NAPA, clofibric acid | M14 | mechanism만 유지; figure-derived 수치 anchor는 `[확인 필요]`. |

---

## 0A. Adjudication Table Summary

### 0A-1. Audit v1 priority items

| Source | Item | Verdict | Rationale |
|---|---|---|---|
| Audit T1/T4 | M15 passive diffusion / extended clearance inequality | **ADOPT** | `PSpd` 또는 effective passive diffusion이 `CLint`에 비해 충분히 클 때 well-stirred로 환원되도록 수정. |
| Audit T1/T4 | M16 `AUC(m)/AUC < 1` 해석 오류 | **ADOPT** | 최종본은 `AUC(m)/AUC = f_m·CL/CL(m)`만 잠그고, `f_m` 미상 시 상대 clearance 단정 금지. |
| Audit T1/T4 | M18 propranolol oral dose | **ADOPT** | `80 mg` 삭제, source의 single `20-mg oral dose`로 정정 [T20 p.666]. |
| Audit T1/T4 | M18 morphine/M6G route-dose framing | **ADOPT** | `10 mg dose-equivalent` 삭제, oral `11.7 mg` vs i.v. `5 mg`로 정정 [T20 p.668]. |
| Audit T1/T4 | M17 renal impairment shortcut | **ADOPT** | “parent CL 보정이면 metabolite도 자동 보정” 삭제; metabolite CL과 율속단계 별도 평가로 수정. |
| Audit T1/T4 | Table 2.9 formula transcription risk | **PARTIAL_ADOPT** | 4-model 명칭·개념은 보존하되 상세 수식은 `[확인 필요]`로 잠금. |
| Audit T1/T4 | Unsupported external/practice claims | **ADOPT** | source 없는 `SLCO1B1*5`, exposure fold-change, AIMS standard, toxicity threshold는 삭제 또는 `[교과서 외 해석]`. |
| Audit T1/T4 | Internal title `01_step1_draft_v0` | **ADOPT** | 본 파일명과 metadata를 Session 04로 정정. |
| Audit T3/T4 | T20 “action, toxicity, inhibition, induction, displacement” | **ADOPT** | M11 도입에 1문장으로 삽입. |
| Audit T3/T4 | Metabolite concentration caveat | **ADOPT** | “대사체가 존재해도 충분한 농도 없으면 therapeutic concern 아님”을 M11에 삽입. |
| Audit T3/T4 | Urine collection until negligible | **ADOPT** | M3에 1문장으로 삽입 [G p.51]. |
| Audit T4 | Chain example “fastest k” wording | **ADOPT** | downstream substances는 slowest step의 terminal decline을 따른다고 수정. |
| Audit T4 | Oral effect faster/stronger phrasing | **ADOPT** | conditional prodrug/active metabolite 상황으로 제한. |
| Audit T4 | Halazepam/carboxy? and carbamazepine exact visual values | **PARTIAL_ADOPT** | exact day/dose range 대신 qualitative trend; 필요 시 `[확인 필요]`. |
| Audit T4 | T5 integration tables/figures | **PARTIAL_ADOPT** | table/figure 자체는 Phase 4C로 넘기고, M5/M8/M9에 핵심 해석만 반영. |
| Audit T4 | Figure-view inventory | **DEFER** | T6 Figure Inventory는 본 adjudication 대상이 아니므로 Phase 4C로 이관. |
| Audit T4 | Aminoglycoside renal example | **REJECT** | 도입 예시로는 유용하나 10분 handout 핵심 atom 아님. |
| Audit T4 | Inulin GFR marker | **PARTIAL_ADOPT** | nephron physiology 문장 안에만 간단히 흡수. |
| Audit T4 | Full Table 2.3 urinary dataset | **REJECT** | plot logic만 필요; full table은 Phase 4C/appendix 후보. |
| Audit T4 | CYP abundance details | **REJECT** | DDI context로는 유용하나 clearance atom 흐름에서는 과밀. |
| Audit T4 | App.D/E study problem full solution | **REJECT** | formula-level first principles만 필요. |
| Audit T4 | External facts without source tags | **REJECT** | PDF fidelity 범위 위반. |
| Audit T4 | Universal oral-route rule | **REJECT** | source examples are conditional. |
| Audit T4 | Invented examples replacing PDF examples | **REJECT** | source lock 위반. |

### 0A-2. Crucible v1 items

| Source | Item | Verdict | Rationale |
|---|---|---|---|
| Crucible | 14 MUST card architecture | **ADOPT** | Draft v0의 20 MUST를 14 atom으로 압축하는 최적 구조. |
| Crucible | Grade A: M4, M5, M11, M12, M14 | **ADOPT** | handout의 spine으로 유지. |
| Crucible | Grade B: M2, M8, M9, M10, M13 | **PARTIAL_ADOPT** | 문서 길이 증가 없이 기존 카드 안으로 압축. |
| Crucible | Grade C: distributed/dispersion formula detail, long sequence demonstration, isoproterenol detail | **REJECT** | 세부 수식/사례는 10분 handout의 핵심 부담을 증가. |
| Crucible | Deletion candidates: App.D/E separate card 삭제 | **ADOPT** | M8/M4/M9 내부 first-principles 보강으로 유지. |
| Crucible | Deletion candidates: Biliary/EHC, half-life, steady-state metabolite compression | **ADOPT** | M2/M1/M13으로 흡수. |
| Crucible | Confusion Pair 1 IIV vs RUV | **REJECT** | 중요하지만 본 교과서 source 직접 흐름 밖; NONMEM 일반론으로 별도 세션 대상. |
| Crucible | Confusion Pair 2–3 fu/fub and CL/CLb | **ADOPT** | App.D/T5와 직접 연결. |
| Crucible | Confusion Pair 4 CYP abundance vs contribution | **PARTIAL_ADOPT** | Ch.5 context로 1문장만 허용; 핵심 pair에서는 제외. |
| Crucible | Confusion Pair 5 permeability vs metabolism | **ADOPT** | App.E `ρ`의 핵심. |
| Crucible | Confusion Pair 6 phenytoin uremia | **ADOPT** | T5 integration 사례로 유지. |
| Crucible | Confusion Pair 7 formation vs elimination RL | **ADOPT** | T20 핵심. |
| Crucible | Confusion Pair 8 `AUC(m)/AUC` vs `f_m` | **ADOPT** | Audit MUST_FIX와 직접 연결. |
| Crucible | Confusion Pair 9 sequential vs interconversion | **ADOPT** | T20 interconversion 함정. |
| Crucible | Confusion Pair 10 membrane-limited vs flow-limited | **ADOPT** | App.E Model II의 핵심. |
| Crucible | NDA Deficiency Letters DL-1~DL-10 | **REJECT** | PDF 직접 근거보다 규제 확장 claim 비중이 커 본 Content Lock에서는 제외. |
| Crucible | NONMEM Diagnostic Signatures | **PARTIAL_ADOPT** | §8에 `[교과서 외 해석]` bridge로만 압축. |
| Crucible | Trench-Level Tips 15개 | **PARTIAL_ADOPT** | source-grounded 6개만 각 카드에 1문장으로 분산. |
| Crucible | Self-test 8 + Boss Dilemma | **PARTIAL_ADOPT** | source-grounded 8문항 + 1 종합문항으로 재작성; FDA/ICH 외부 claim 삭제. |
| Crucible | Professional Moat / AIMS-specific framing | **REJECT** | 교과서 source fidelity 기준에서는 외부 해석. |

---

## §1 Why This Chapter Matters

<!-- MASTER LENS -->
**Big Idea**: Clearance는 `Dose/AUC`로 끝나는 숫자가 아니라, **혈류(`Q`), 단백결합(`f_u`, `f_{ub}`), intrinsic clearance(`CL_int`), permeability/transporter, renal filtration/secretion/reabsorption, metabolite formation/elimination**이 한 식 안에서 충돌한 결과다. 이 장의 목표는 `CL`을 외우는 것이 아니라, 관찰된 `CL`, `t1/2`, `AUC(m)/AUC`, `C/C_b` 변화가 어느 생리학적 병목에서 왔는지 역추적하는 것이다.

<!-- ANCHOR -->
학습 흐름은 네 단계다. 먼저 `Rate = CL·C`로 clearance의 비례관계를 세운다. 둘째, 신장에서는 `CL_R = f_e·CL`과 filtration/secretion/reabsorption으로 분해한다. 셋째, 간에서는 well-stirred 식으로 `Q_H`, `f_{ub}`, `CL_int`, permeability를 분리한다. 넷째, parent–metabolite 시스템에서는 `f_m`, `CL(m)`, rate-limiting step, renal impairment를 별도 축으로 추가한다.

<!-- RECAP -->
이 문서에서 버릴 수 없는 한 문장은 다음이다: **“어떤 clearance인가?”라는 질문은 항상 “어느 농도 기준인가, 어느 장기인가, 어느 율속단계인가, parent인가 metabolite인가?”로 풀어야 한다.**

---

## §2 Concept Anatomy Cards

### M1. Clearance proportionality + half-life is derived

<!-- MASTER LENS -->
**Big Idea**: Clearance는 제거 속도 자체가 아니라 **농도로 normalize한 제거능**이다. 따라서 `CL`은 first-order 조건에서 시간에 대해 한 숫자로 유지될 수 있고, `AUC`는 그 제거능을 전체 시간에 걸쳐 적분한 관찰량이다.

**Core equations** [G p.49 Eq 2:83–2:86; G pp.77–79 Eq 2:180–2:185; T5 pp.124–128 Eq 5-1–5-8]

$$rac{dX}{dt}=-CL\cdot C$$

$$CL=\frac{Dose_{iv}}{AUC_{0-\infty}}, \qquad \frac{CL}{F}=\frac{D_{po}}{AUC_{po}}$$

$$CL=f_u\cdot CL_u$$

**Half-life는 원인이 아니라 결과** [T5 pp.148–150 Eq 5-24–5-27]

$$k=\frac{CL}{V}, \qquad t_{1/2}=\frac{0.693\cdot V}{CL}$$

`t1/2`가 변했다는 말은 `CL` 또는 `V`가 변했다는 결과 신호다. `t1/2` 자체가 `CL`을 결정하지 않는다.

<!-- TRENCH -->
**Trench-level tip**: 신부전, 간부전, 단백결합 변화에서 “half-life가 늘었다/줄었다”로 시작하지 말고 `CL`과 `V`를 먼저 분리한다. 같은 `t1/2`라도 `CL↑ + V↑`가 동시에 생긴 경우와 둘 다 변하지 않은 경우는 완전히 다르다.

<!-- ANCHOR -->
M1의 `CL`을 신장에 적용하면 M2의 `CL_R`; 간에 적용하면 M4의 `CL_H`; 대사체에 적용하면 M12의 `CL_f`와 `CL(m)`이 된다.

---

### M2. Renal clearance decomposition: `CL_R`, `f_e`, filtration/secretion/reabsorption

<!-- MASTER LENS -->
**Big Idea**: `CL_R = f_e·CL`은 단순 비례식이 아니라, **혈장 AUC와 소변 누적 배설량을 연결하는 measurement bridge**다. 혈장만 보면 total `CL`만 보이고, 소변을 같이 봐야 renal route의 지분 `f_e`와 `CL_R`가 열린다.

**Renal physiology compressed** [G p.48; T5 pp.138–145]

Nephron은 Bowman’s capsule, proximal tubule, loop of Henle, distal tubule, collecting duct로 구성된다. GFR은 Gabrielsson에서 110–130 mL/min, Tozer에서는 reference로 약 120 mL/min이며, urine pH는 4.5–8 범위로 변할 수 있다 [G p.48; T5 pp.119–120, pp.138–145]. Inulin은 GFR marker로 언급되지만 본 handout에서는 physiology context로만 유지한다.

**Core renal equations** [G pp.49–50 Eq 2:87–2:89; T5 pp.139–142 Eq 5-17–5-23]

$$\frac{dX_u}{dt}=CL_R\cdot C$$

$$X_{u,0-\infty}=CL_R\cdot AUC_{0-\infty}$$

$$CL_R=\frac{X_u(t_1,t_2)}{AUC(t_1,t_2)}$$

$$f_e=\frac{CL_R}{CL}$$

$$CL_R=(1-F_R)\cdot(CL_f+CL_S), \qquad CL_f=f_u\cdot GFR$$

`CL_R > f_u·GFR`이면 secretion이 필요하고, `CL_R < f_u·GFR`이면 reabsorption 또는 측정 조건을 의심한다.

**Clearance additivity** [T5 pp.127–128 Eq 5-9]

$$CL=CL_R+CL_H+CL_{other}$$

Biliary excretion과 enterohepatic cycling은 elimination profile을 바꿀 수 있지만, 본 문서에서는 M2의 route decomposition 안에 압축한다 [T5 pp.137–138]. Pulmonary clearance는 organ additivity 해석에서 특수 예외로만 기억한다 [T5 p.128].

<!-- CONFUSION -->
**Confusion**: `f_e`가 작으면 renal impairment 영향이 작다고 단정하기 쉽다. Parent 기준으로는 대체로 맞을 수 있지만, active metabolite가 renal elimination을 받으면 M14의 결론이 완전히 달라진다.

<!-- ANCHOR -->
M2는 M7의 simultaneous plasma+urine fitting과 M14의 renal impairment metabolite scenario로 연결된다.

---

### M3. ARE plot vs Excretion Rate plot

<!-- MASTER LENS -->
**Big Idea**: ARE plot과 excretion-rate plot은 같은 urinary data에서 `K`를 추정하지만, noise와 시간 정보를 다르게 왜곡한다. Rate plot은 renal clearance의 시간 변동을 잘 드러내고, ARE plot은 누적량 기반이라 변동을 평활한다.

**Rate plot** [G pp.50–51 Eq 2:90–2:92]

$$\ln\left(\frac{dX_u}{dt}\right)=\ln\left(CL_R\cdot\frac{D_{iv}}{V}\right)-K\cdot t$$

**ARE plot** [G pp.50–52 Eq 2:93–2:98]

$$\ln(X_{u,0-\infty}-X_u)=\ln(X_{u,0-\infty})-K\cdot t$$

| 판단 축 | Excretion-rate plot | ARE plot |
|---|---|---|
| Collection interval이 half-life보다 길 때 | 취약 | 상대적으로 안정 |
| Incomplete bladder emptying | 취약 | 누적 bias 가능 |
| `X_{u,0-∞}` 필요성 | 낮음 | 높음 |
| pH/urine flow에 따른 `CL_R` 시간 변동 | 잘 보임 | 평활되어 덜 보임 |

**Audit SHOULD_FIX 반영**: 정확한 urinary result를 위해서는 drug urinary concentration이 negligible level로 돌아올 때까지 urine sample을 수집하는 것이 좋다 [G p.51].

**Key example**: PK5에서 urine collection interval은 0.5–12 h로 다양하고, rate plot/ARE plot에서 half-life가 약 6–6.3 h로 figure-derived 추정된다 [G p.497; 확인 필요: figure-derived value]. Methamphetamine은 urine pH에 따라 urinary recovery가 acidic urine에서 70–80%, alkaline urine에서 1–2%로 크게 달라지는 예로 제시된다 [T5 p.145].

<!-- TRENCH -->
**Trench-level tip**: urinary data를 보면 먼저 ARE와 rate plot을 둘 다 그린다. 두 plot이 같은 `K`를 주지 않으면 먼저 collection interval, bladder emptying, pH/flow 변동을 의심하고, 곧바로 compartment 수를 늘리지 않는다.

---

### M4. Well-stirred hepatic clearance + 4-model compression

<!-- MASTER LENS -->
**Big Idea**: Well-stirred model은 hepatic clearance를 세 입력값으로 압축한다: blood flow `Q_H`, blood unbound fraction `f_{ub}`, intrinsic clearance `CL_int`. 분모의 어느 항이 큰지가 high/low extraction 분류와 임상 해석을 결정한다.

**Core equation** [G pp.79–82 Eq 2:188–2:195; T5 pp.130–135 Eq 5-14–5-15; TE pp.777–778 Eq E-1–E-8]

$$CL_{H,b}=Q_H\cdot E_H=\frac{Q_H\cdot f_{ub}\cdot CL_{int}}{Q_H+f_{ub}\cdot CL_{int}}$$

$$E_H=\frac{CL_{H,b}}{Q_H}=\frac{f_{ub}\cdot CL_{int}}{Q_H+f_{ub}\cdot CL_{int}}$$

`Q_H`는 Tozer reference에서 약 1.35 L/min (=81 L/h)로 제시된다 [T5 p.125].

**Limiting cases** [T5 pp.130–135]

| Condition | Approximation | Interpretation |
|---|---|---|
| `f_{ub}·CL_int >> Q_H` | `CL_H,b ≈ Q_H` | flow-limited, high extraction |
| `f_{ub}·CL_int << Q_H` | `CL_H,b ≈ f_{ub}·CL_int` | capacity/binding-limited, low extraction |

**Four hepatic clearance models** [G pp.90–94 Table 2.9]

Well-stirred, parallel-tube, distributed, dispersion model은 모두 hepatic extraction을 설명하지만, mixing assumption과 concentration gradient 처리 방식이 다르다. 본 Content Lock에서는 conceptual difference만 보존하고, distributed/dispersion 상세 수식은 source-fidelity risk 때문에 `[p.94; 확인 필요: formula-level 1:1 재검산 전까지 잠금]`으로 둔다.

<!-- CONFUSION -->
**Confusion**: “간청소율 식”을 plasma `C` 기준으로 쓰면 extraction ratio가 틀어진다. Organ extraction은 blood concentration 기준이며, plasma에서 측정한 값은 M8의 `C/C_b` 변환을 거쳐야 한다.

---

### M5. High/low extraction + route × extraction × `f_u` matrix

<!-- MASTER LENS -->
**Big Idea**: 단백결합 변화의 해석은 `route × extraction × total/unbound concentration`의 3축 문제다. “High extraction이면 `f_u` 무관”은 **IV total concentration**에 한정되는 위험한 반쪽 문장이다.

**Route matrix** [G pp.83–85; T5 pp.150–163]

| Scenario | Total concentration / AUC | Unbound concentration |
|---|---|---|
| IV + High extraction | `CL≈Q_H`, total `C`는 `f_u`에 둔감 | `C_u=f_u·C`, `f_u` 증가 시 unbound 증가 가능 |
| IV + Low extraction | `CL≈f_u·CL_int`, total `C` 감소 | `C_u`는 대체로 `CL_int`에 의해 보존 |
| Oral + High extraction | first-pass 때문에 total AUC가 `f_u·CL_int`에 민감 | unbound AUC는 `CL_int` 중심으로 해석 |
| Oral + Low extraction | total AUC가 `f_u·CL_int`에 민감 | unbound AUC는 `CL_int` 중심으로 해석 |

**Tozer integration examples** [T5 pp.152–163]

- Alfentanil + rifampin: low extraction enzyme induction → clearance 증가, AUC 감소 [T5 p.152].
- Alprenolol + pentobarbital: high extraction IV에서 enzyme induction 효과가 작고, oral bioavailability는 감소 [T5 p.153].
- Fentanyl + itraconazole vs ritonavir: itraconazole은 i.v. fentanyl PK에 큰 영향이 없지만, ritonavir는 clearance를 0.94 → 0.32 L/h/kg로 낮춰 high-to-low extraction 전환을 일으킨다 [T5 pp.154–155].
- Phenytoin in uremia: `f_u` 증가로 total concentration은 낮아질 수 있으나 unbound 관점 해석이 필요하다 [T5 pp.159–160].
- Clofibric acid in nephrotic syndrome: 작은 `V`에서 `f_u` 증가가 `CL` 변화로 half-life 단축을 만들 수 있다 [T5 pp.161–162].

<!-- TRENCH -->
**Trench-level tip**: high extraction drug에서 IV DDI가 음성이라고 oral DDI도 안전하다고 결론 내리지 않는다. Route가 바뀌면 first-pass와 `f_u·CL_int` 민감도가 바뀐다.

---

### M6. IVIVE pitfalls: single-point, MMP, data condensation

<!-- MASTER LENS -->
**Big Idea**: IVIVE는 `Vmax`, `Km`, microsomal protein scaling을 넣는 계산 문제가 아니라, **어떤 정보를 버렸는지**를 점검하는 문제다. 한 점에서 얻은 `CL_int`, 잘못된 MMP 보정, 과도한 data condensation은 모두 in vivo clearance를 왜곡한다.

**Core flow** [G pp.85–90]

$$CL_{int,in\ vitro}\rightarrow CL_{int,scaled}\rightarrow CL_H=\frac{Q_H\cdot f_u\cdot CL_{int}}{Q_H+f_u\cdot CL_{int}}$$

**Three traps**

1. **Single-point trap**: 한 농도에서 얻은 rate를 `Vmax/Km`처럼 쓰면 nonlinearity와 saturation을 놓친다 [G pp.85–89].
2. **MMP scaling trap**: microsomal protein per gram liver 보정은 평균값 하나가 아니라 variability와 ratio 처리 방식에 민감하다 [G p.87].
3. **Data condensation trap**: raw concentration–rate relation을 하나의 `CL_int`로 압축하면 curvature와 outlier 구조가 사라진다 [G pp.88–89].

<!-- TRENCH -->
**Trench-level tip**: IVIVE report를 검토할 때 첫 질문은 “well-stirred 식이 맞는가?”가 아니라 “in vitro rate 정보가 single point로 collapse되었는가?”다. Collapse된 입력은 정교한 hepatic model로도 복구되지 않는다.

---

### M7. PK5 simultaneous plasma+urine fitting

<!-- MASTER LENS -->
**Big Idea**: PK5는 urinary data를 별도 계산표로 처리하지 않고, **plasma concentration과 cumulative urine amount를 한 모델에서 동시에 fitting**하는 예다. 이 구조가 NONMEM에서 plasma+urine, IV+oral, parent+metabolite를 함께 fitting하는 사고방식의 출발점이다.

**Problem anchor** [G pp.494–499]

- Dose: 250 mg i.v. bolus [G p.494].
- Initial estimates: `V≈7 L`, `CL≈2 L/h`, `f_e≈0.3` [G p.497].
- Final estimates: `CL≈1.2 L/h`, `f_e≈35%`, `CL_R≈0.42 L/h`; parameter CVs <5%; plasma/urine CV estimates 2.84% and 8.96% [G p.498].

**Analytic vs ODE equivalence** [G pp.497–499]

Analytic solution and differential-equation system give almost identical final parameter estimates and precision.

**Model skeleton** [G pp.497–499]

$$C(t)=\frac{D_{iv}}{V}\exp\left(-\frac{CL}{V}t\right)$$

$$X_u(t)=f_e\cdot D_{iv}\left[1-\exp\left(-\frac{CL}{V}t\right)\right]$$

<!-- TRENCH -->
**Trench-level tip — NONMEM [교과서 외 해석]**: plasma and urine endpoints should not be forced into one residual error scale. Use separate `DVID` and endpoint-specific residual error, because PK5 itself shows plasma and urine CVs differ.

---

### M8. Plasma-to-blood ratio and blood clearance

<!-- MASTER LENS -->
**Big Idea**: Organ extraction ratio는 blood flow와 비교하므로 **blood concentration 기준 clearance**가 필요하다. 그런데 실제 측정은 대부분 plasma concentration이다. `C/C_b` 변환을 하지 않으면 extraction ratio 분류가 systematic하게 틀어진다.

**Clearance relation** [T5 pp.124–128 Eq 5-4–5-6]

Let `R = C/C_b`.

$$CL_b=CL\cdot\frac{C}{C_b}=CL\cdot R$$

$$CL=CL_b\cdot\frac{C_b}{C}=\frac{CL_b}{R}$$

**App.D mass-balance** [TD pp.775–776 Eq D-1–D-8]

$$\frac{C}{C_b}=\frac{1}{1+H(f_uK_{PBC}-1)}$$

where `H` is hematocrit, `f_u` is unbound fraction in plasma, and `K_{PBC}` is the blood-cell-to-unbound-plasma partition coefficient.

**Implication**

- If `R<1`, plasma concentration is lower than blood concentration; plasma CL can look smaller/larger depending on ratio usage.
- Hepatic extraction must use `E_H=CL_{H,b}/Q_H`, not plasma `CL_H/Q_H`.
- `f_u` and `f_{ub}` are not interchangeable. `f_{ub}=f_u·(C/C_b)`.

<!-- CONFUSION -->
**Confusion**: `CL=60 L/h`, `Q_H=81 L/h`이면 moderate extraction처럼 보일 수 있다. 그러나 `R=C/C_b=0.5`이면 `CL_b=30 L/h`이고 `E_H=0.37`이다. 분류가 바뀐다.

---

### M9. Permeability-rate-limited hepatic uptake: App.E `ρ`

<!-- MASTER LENS -->
**Big Idea**: Basic well-stirred model은 liver cell 안팎의 unbound concentration이 빠르게 평형이라고 가정한다. 그러나 hepatic uptake permeability가 느리면 hepatocyte 내부 unbound concentration이 blood unbound concentration보다 낮아지고, `CL_int`만으로는 hepatic clearance를 설명할 수 없다.

**App.E Model II** [TE pp.778–779 Eq E-9–E-15]

$$\rho=\frac{P_{in}\cdot SA}{P_{out}\cdot SA+CL_{int}}$$

$$CL_{H,b}=\frac{Q_H\cdot f_{ub}\cdot \rho\cdot CL_{int}}{Q_H+f_{ub}\cdot \rho\cdot CL_{int}}$$

**Audit correction**

Passive diffusion / permeability가 충분히 커서 intracellular and extracellular unbound concentrations가 빠르게 평형에 가까워지면 `ρ→1`이고 basic well-stirred model로 환원된다. 반대로 uptake permeability가 작으면 `ρ<1`이고 clearance는 permeability-limited가 된다 [TE pp.778–779].

**Oral bridge** [TE pp.779–780 Eq E-19–E-20]

For a drug entirely cleared by hepatic extraction under the stated assumptions:

$$AUC_{po}=\frac{Dose}{f_{ub}\cdot\rho\cdot CL_{int}}$$

<!-- TRENCH -->
**Trench-level tip**: transporter substrate에서 `f_u`와 `CL_int`만으로 IVIVE를 강행하면 permeability bottleneck을 `CL_int` 부족으로 오해할 수 있다.

---

### M10. Extended clearance: transporter–enzyme architecture

<!-- MASTER LENS -->
**Big Idea**: Extended clearance는 hepatic elimination을 “enzyme 하나”가 아니라 **sinusoidal uptake, canalicular efflux, basolateral efflux, intracellular metabolism**의 네 흐름으로 본다. Basic well-stirred는 이 네 흐름 중 membrane step이 충분히 빠른 특수한 경우다.

**Core source** [T5 pp.136–138 Eq 5-35–5-36]

T5는 hepatic elimination이 perfusion, plasma protein binding, hepatocellular activity만으로 끝나지 않고 membrane permeability와 transporter에 의해 달라질 수 있음을 명시한다. App.E는 이 점을 `ρ`로 first-principles화한다 [TE pp.778–779].

**Minimal interpretation**

- Uptake-limited: plasma/blood에서 hepatocyte로 들어가는 step이 병목.
- Metabolism-limited: cell 내부 도달은 충분하고 enzyme capacity가 병목.
- Efflux-limited: bile 또는 blood 방향 efflux가 병목.

<!-- ANCHOR -->
M10은 M6의 IVIVE trap과 M9의 `ρ`를 연결한다. 즉, poor IVIVE가 항상 enzyme assay 문제는 아니며, transporter/permeability term 누락일 수 있다.

---

### M11. Rate-limiting step in metabolite disposition

<!-- MASTER LENS -->
**Big Idea**: 대사체 농도-시간 곡선의 terminal slope는 대사체 자체의 half-life가 아닐 수 있다. Formation이 느리면 대사체는 parent의 “그림자”처럼 parent half-life로 감소한다. Elimination이 느리면 대사체 자체 half-life가 terminal phase를 지배한다.

**Why metabolites matter** [T20 pp.658–659]

Metabolites matter for five reasons: **action, toxicity, inhibition, induction, displacement**. 그러나 metabolite가 그런 성질을 가져도 충분한 concentration에 도달하지 않으면 therapeutic concern은 작다 [T20 p.659].

**Mass balance** [T20 pp.659–662 Eq 20-1–20-3]

$$\frac{dA(m)}{dt}=k_fA-k(m)A(m)$$

| Case | Condition | Observed pattern | Interpretation |
|---|---|---|---|
| Formation rate-limited | `k << k(m)` | metabolite declines parallel to parent | observed metabolite terminal `t1/2` is parent’s half-life |
| Elimination rate-limited | `k(m) << k` | metabolite peaks later and declines slower | terminal `t1/2` is metabolite’s own half-life |

**Audit correction**

Sequential chain에서는 “fastest k가 결정한다”가 아니라, downstream substance의 terminal decline은 **가장 느린 step**에 의해 지배된다 [T20 p.661]. Renal impairment에서는 parent CL 보정이 metabolite exposure를 자동 보정하지 않는다; metabolite CL과 rate-limiting step을 별도로 평가해야 한다 [T20 pp.673–675].

<!-- CONFUSION -->
**Confusion**: parent와 metabolite가 parallel decline이면 metabolite half-life를 parent와 같다고 보고하기 쉽다. 정확히는 “observed terminal half-life after parent dosing”이 parent의 half-life를 반영할 뿐이다.

---

### M12. `AUC(m)/AUC` decomposition: `f_m × CL/CL(m)`

<!-- MASTER LENS -->
**Big Idea**: `AUC(m)/AUC`는 `f_m` 그 자체가 아니다. 이 비는 metabolite formation fraction과 metabolite clearance가 함께 들어간 compound quantity다.

**Core equations** [T20 pp.662–665 Eq 20-4–20-7]

$$\frac{dA(m)}{dt}=CL_f\cdot C-CL(m)\cdot C(m)$$

Integrated over time:

$$\frac{AUC(m)}{AUC}=\frac{CL_f}{CL(m)}$$

with:

$$CL_f=f_m\cdot CL$$

Therefore:

$$\boxed{\frac{AUC(m)}{AUC}=f_m\cdot\frac{CL}{CL(m)}}$$

**Audit correction**

If `AUC(m)/AUC < 1` and `f_m` is unknown, one cannot infer `CL(m) ≥ CL/f_m`. Only the source-consistent inequality `CL(m)>f_m·CL` follows. The same AUC ratio can arise from low `f_m`, high `CL(m)`, or both.

**Examples retained** [T20 pp.662–665]

Methylprednisolone hemisuccinate → methylprednisolone, tolbutamide → hydroxytolbutamide, and propranolol → naphthoxylactic acid illustrate how metabolite curves distinguish rate-limiting steps and relative clearance. Detailed figure numeric readings are not expanded here.

<!-- TRENCH -->
**Trench-level tip**: active metabolite PopPK에서 `AUC(m)/AUC`가 작다는 이유로 metabolite를 무시하지 않는다. `f_m`이 작아도 `CL(m)`이 renal impairment에서 크게 줄면 M14의 문제가 된다.

---

### M13. First-pass metabolite contribution + steady-state metabolite

<!-- MASTER LENS -->
**Big Idea**: Oral parent dosing can create metabolite from two sources: first-pass formation during absorption and post-absorption formation from systemic parent. This is not a universal “oral is stronger” rule; it matters when parent has high first-pass extraction and the metabolite is active or otherwise clinically relevant.

**First-pass dual-source model** [T20 pp.665–669]

Observed metabolite after oral parent dosing is the sum of:

1. metabolite formed during absorption/first pass, and
2. metabolite formed later from absorbed systemic parent.

**Corrected examples**

- Propranolol: source example is a single **20-mg oral dose**, not 80 mg. Naphthoxylactic acid peaks at about the same time as propranolol, consistent with first-pass metabolite input [T20 p.666].
- Morphine/M6G: source compares oral **11.7 mg** and i.v. **5 mg** morphine, not a 10 mg dose-equivalent framing. Morphine oral bioavailability is low, but M6G exposure/amount can be similar because first-pass formation contributes [T20 pp.667–668].
- Isoproterenol: route-dependent urinary recovery pattern supports gut-wall/extrahepatic metabolism in that example [T20 p.669].

**Steady-state metabolite** [T20 pp.669–673 Eq 20-11–20-15]

For constant-rate input:

$$C(m)_{ss}=\frac{f_m\cdot R_{inf}}{CL(m)}$$

For multiple oral dosing by superposition:

$$C(m)_{av,ss}=\frac{AUC(m)_{single}}{\tau}$$

Time to plateau is governed by the slower of parent elimination and metabolite elimination, depending on the rate-limiting pattern [T20 pp.670–673]. N-desalkylhalazepam shows slower metabolite accumulation/decline than parent; exact visual timing is not locked here `[T20 p.672; 확인 필요: figure-derived value]`. Carbamazepine autoinduction is retained as a qualitative trend—dose-normalized parent falls and metabolite relationship changes—without locking exact dose range `[T20 p.676; 확인 필요]`.

<!-- TRENCH -->
**Trench-level tip**: oral parent data alone cannot always separate low parent bioavailability from large first-pass metabolite formation. Route comparison is a diagnostic tool, not just a bioavailability calculation.

---

### M14. Renal impairment active-metabolite scenario + interconversion

<!-- MASTER LENS -->
**Big Idea**: Parent `f_e` alone is not enough for renal impairment dosing when active metabolite exists. The highest-risk case is not always “parent mostly renal”; it can be “parent partly metabolized to an active metabolite that is itself renally cleared.”

**Tozer worked scenario** [T20 pp.673–675; Fig 20-10; Table 20-4]

Normal example:

| Parameter | Parent drug | Active metabolite |
|---|---:|---:|
| Total CL | 30 L/h | 10 L/h |
| Renal CL | 15 L/h | 8.5 L/h |
| Parent oral F / formation fraction | `F=0.8` | `f_m=0.3` |

At 10 mg/h oral dosing, normal total active concentration is parent 0.27 mg/L + metabolite 0.24 mg/L = 0.51 mg/L [T20 pp.673–674]. In anuric condition, parent increases about 2-fold, but metabolite can increase about 13-fold; dose ratio to match normal total activity is about 0.14 [T20 p.674].

**Scenario rule** [T20 p.675]

1. If metabolite formation is the major parent elimination pathway and metabolite is active, dosing may need to follow metabolite clearance.
2. If parent renal excretion is major and metabolite formation is minor, parent exposure may dominate.
3. If metabolite formation is minor but metabolite elimination is almost exclusively renal and the metabolite is active, renal impairment can make the metabolite dominate total activity.

**Interconversion** [T20 pp.676–679]

Interconversion means parent and metabolite can regenerate each other. In that case, renal impairment affecting the metabolite can indirectly reduce apparent parent elimination. Clofibric acid is retained as a qualitative example; figure-derived numeric anchors are not locked `[T20 p.679; 확인 필요]`.

<!-- CONFUSION -->
**Confusion**: “minor metabolite pathway” is not the same as “minor safety concern.” If metabolite `CL(m)` collapses in renal impairment, a small `f_m` can still become the main exposure driver.

---

## §5 Confusion Pairs — 반드시 분리해야 하는 개념 쌍

### Pair 1. `CL`, `CL_R`, `f_e`

<!-- CONFUSION -->
`CL` is total systemic clearance. `CL_R` is renal clearance. `f_e=CL_R/CL` is a fraction. 신부전 covariate를 total `CL`에 바로 곱하면 nonrenal clearance까지 같이 줄이는 오류가 생긴다.

### Pair 2. ARE plot vs Excretion-rate plot

<!-- CONFUSION -->
ARE는 cumulative residual amount를 쓰고, rate plot은 interval excretion rate를 midpoint에 둔다. pH/flow에 따른 `CL_R` 변동은 rate plot에 더 잘 보인다 [G p.51].

### Pair 3. Plasma `CL` vs Blood `CL_b`

<!-- CONFUSION -->
Plasma `CL`은 measured concentration 기준이고, `CL_b`는 organ blood flow와 비교 가능한 값이다. Extraction ratio는 `E=CL_b/Q`, not `CL/Q` [T5 pp.124–128; TD pp.775–776].

### Pair 4. `f_u` vs `f_{ub}`

<!-- CONFUSION -->
`f_u` is unbound fraction in plasma. `f_{ub}` is unbound fraction in blood. `f_{ub}=f_u·C/C_b`; App.D를 통과하지 않으면 well-stirred input이 틀어진다 [TD pp.775–776].

### Pair 5. High extraction IV vs High extraction oral

<!-- CONFUSION -->
High extraction IV에서는 total `CL≈Q_H`라 enzyme induction/inhibition이 잘 안 보일 수 있다. 그러나 oral에서는 first-pass availability와 metabolite formation이 달라져 전혀 다른 결과가 가능하다 [G pp.83–85; T20 pp.665–669].

### Pair 6. Well-stirred vs extended/permeability-limited model

<!-- CONFUSION -->
Well-stirred는 rapid equilibration 가정이다. Uptake permeability가 병목이면 `ρ<1`이 되고, `CL_int`가 충분해도 hepatic clearance가 낮게 보인다 [TE pp.778–779].

### Pair 7. Single-point `CL_int` vs Michaelis–Menten information

<!-- CONFUSION -->
Single-point rate는 curvature를 버린다. `Vmax/Km`을 쓰려면 concentration range가 충분하고, free concentration과 scaling assumptions가 맞아야 한다 [G pp.85–89].

### Pair 8. Formation-rate-limited vs elimination-rate-limited metabolite

<!-- CONFUSION -->
Parent와 metabolite가 parallel decline하면 metabolite terminal slope는 parent elimination을 반영할 수 있다. Metabolite own `t1/2`는 separate metabolite dosing 또는 model-based inference 없이는 단정하기 어렵다 [T20 pp.659–662].

### Pair 9. `AUC(m)/AUC` vs `f_m`

<!-- CONFUSION -->
`AUC(m)/AUC=f_m·CL/CL(m)`. AUC ratio가 작다는 것은 `f_m`이 작다는 뜻일 수도, `CL(m)`이 큰 뜻일 수도 있다 [T20 pp.662–665].

### Pair 10. Sequential metabolism vs interconversion

<!-- CONFUSION -->
Sequential metabolism은 downstream 방향으로 진행된다. Interconversion은 metabolite가 parent로 되돌아올 수 있어, metabolite clearance 변화가 parent apparent clearance까지 바꾼다 [T20 pp.676–679].

<!-- RECAP -->
Confusion pairs의 공통 메시지: **같아 보이는 두 숫자가 실제로는 서로 다른 denominator, route, compartment, or rate-limiting step을 갖는다.**

---

## §7 Self-Test — Socratic Dilemma

### Q1. Clearance definition

`CL = Dose/AUC`가 compartment model 없이도 성립하는 이유를 `Rate=CL·C`의 시간 적분으로 설명하라.  
**Answer direction**: total eliminated amount = dose, `∫Rate dt = CL·∫Cdt`.

### Q2. Renal decomposition

정상 `CL=10 L/h`, `f_e=0.6`인 약물에서 renal function이 25%로 떨어지고 nonrenal CL은 보존된다. 새 total CL은?  
**Answer direction**: renal CL=6→1.5, nonrenal=4, total=5.5 L/h.

### Q3. Urinary plots

Rate plot과 ARE plot의 slope가 다르고, rate plot에서 시간별 변동이 크다. 어떤 artifact 또는 physiology를 먼저 의심할 것인가?  
**Answer direction**: collection interval, bladder emptying, pH/urine flow variation, `X_u∞` bias.

### Q4. Well-stirred limiting case

`Q_H=81 L/h`, `f_{ub}·CL_int=20 L/h`이면 high/low/intermediate 중 어디에 가까운가? `f_{ub}`가 4배 증가하면?  
**Answer direction**: initial low-ish `E=20/(81+20)=0.20`; after 80, `E≈0.50`, intermediate.

### Q5. Plasma vs blood CL

Plasma `CL=60 L/h`, `C/C_b=0.5`, `Q_H=81 L/h`. `CL_b`와 extraction ratio는? Plasma CL만 쓰면 어떤 오류가 생기는가?  
**Answer direction**: `CL_b=30 L/h`, `E=0.37`; plasma 기준으로 비교하면 false higher extraction.

### Q6. IVIVE trap

한 substrate concentration에서 얻은 in vitro rate로 `CL_int`를 만들고 MMP 평균값 하나로 scaling했다. Phase 1에서 in vivo CL이 예측의 1/5이다. 어떤 세 가지 원인을 우선 점검할 것인가?  
**Answer direction**: single-point nonlinearity, binding/free concentration, MMP/scaling variability, transporter/permeability omission.

### Q7. Metabolite rate-limiting

Parent dosing 후 parent와 metabolite가 parallel terminal decline을 보인다. 별도 metabolite dosing에서는 metabolite half-life가 더 짧다. 어떤 case인가?  
**Answer direction**: formation rate-limited; observed metabolite slope after parent dosing is parent-controlled.

### Q8. AUC ratio

`AUC(m)/AUC=0.5`이다. 이 값만으로 `f_m=0.5`라고 말할 수 있는가?  
**Answer direction**: No. Need `CL(m)/CL`; equation is `AUC(m)/AUC=f_m·CL/CL(m)`.

### Q9. Boss Dilemma — renal impairment + active metabolite

Parent drug has normal `CL=30 L/h`, renal CL=15 L/h, oral `F=0.8`. Active metabolite has `CL(m)=10 L/h`, renal CL(m)=8.5 L/h, and formation fraction `f_m=0.3`. In anuric condition, parent renal CL and metabolite renal CL go to zero. Why is parent-only dose adjustment unsafe?  
**Answer direction**: parent exposure rises about 2-fold, but metabolite CL collapses from 10 to 1.5 L/h and formation fraction can increase in the Tozer scenario; metabolite exposure can dominate total activity, with source example showing about 13-fold metabolite increase and dose ratio about 0.14 [T20 pp.673–675].

---

## §8 Recap & NONMEM/PopPK Bridge

<!-- RECAP -->
**One-page recap**

1. `CL` is concentration-normalized elimination capacity, not elimination rate itself [G p.49; T5 pp.124–128].
2. `t1/2` is derived from `V/CL`; do not interpret it before decomposing `CL` and `V` [T5 pp.148–150].
3. `CL_R=f_e·CL`, but renal clearance itself is filtration + secretion − reabsorption, modified by urine pH and flow [G pp.48–56; T5 pp.138–148].
4. Well-stirred hepatic clearance is governed by `Q_H`, `f_{ub}`, and `CL_int`; high/low extraction are limiting cases, not drug labels fixed forever [G pp.79–85; T5 pp.130–135].
5. Plasma concentration must be converted to blood concentration for organ extraction; App.D gives the mass-balance bridge [TD pp.775–776].
6. IVIVE fails when the in vitro input has already lost information: single-point `CL_int`, poor scaling, or omitted permeability/transporter terms [G pp.85–90; T5 pp.136–138; TE pp.778–779].
7. Parent–metabolite systems need `f_m`, `CL(m)`, and rate-limiting step; `AUC(m)/AUC` is not `f_m` [T20 pp.659–665].
8. Renal impairment dose adjustment must evaluate active metabolite clearance, not just parent `f_e` [T20 pp.673–679].

### NONMEM/PopPK bridge `[교과서 외 해석 — source equations 기반]`

| Source concept | PopPK implementation implication |
|---|---|
| `CL = CL_R + CL_H + CL_other` | renal covariate를 total `CL`에 무차별 적용하지 말고 route-specific component에 적용. |
| `CL_R=f_e·CL` | urinary data 또는 external `f_e`가 없으면 renal fraction을 과해석하지 않음. |
| PK5 plasma+urine simultaneous fit | `DVID`/endpoint-specific residual error로 plasma and urine data를 동시에 fit. |
| `CL_b=CL·C/C_b` | hepatic extraction 또는 PBPK input에는 blood-based clearance를 사용. |
| well-stirred + App.E `ρ` | transporter substrate에서는 `CL_int` covariate보다 uptake/permeability covariate 가능성을 먼저 점검. |
| `AUC(m)/AUC=f_m·CL/CL(m)` | metabolite model에서 `f_m`, `CL(m)`, `V(m)` 식별성을 route/dose/metabolite data로 확인. |
| rate-limiting step | metabolite terminal slope를 곧바로 metabolite own `t1/2`로 쓰지 않음. |
| renal impairment active metabolite | parent and metabolite combined exposure를 label/dose scenario sensitivity로 계산. |

### Final Content Lock decisions

- Draft v0의 20 MUST는 14 MUST atom으로 압축했다.
- Audit MUST_FIX 8개는 모두 반영했다.
- Audit SHOULD_FIX 중 figure triage는 Phase 4C로 이관하고, source-grounded text corrections는 본문에 삽입했다.
- Crucible Grade A는 채택, Grade B는 길이 증가 없이 흡수, Grade C와 unsupported regulatory/practice embellishment는 삭제했다.
- T6 Figure Inventory는 본 단계에서 adjudication하지 않았고 Phase 4C로 그대로 넘긴다.
- `[확인 필요]`가 필요한 figure-derived numeric anchors는 삭제하지 않고 tag를 남겼다.

**END — 04_Content Lock v1**

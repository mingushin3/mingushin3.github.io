# 04_HTML Compile Input Master

**Target filename**: `04_html_compile_input_master.md`  
**Assembly date**: 2026-05-06  
**Assembly mode**: PATCH MODE — `04_Content Lock v2.1` is a figure-marker patch/insertion map, not a full body.  
**Phase boundary**: This is Phase 4D. No HTML, Mermaid code, SVG code, or textbook image embedding is generated here.

## Phase 4D Certification

| Certificate | Status | Basis |
|---|---|---|
| Learner-Standalone Certificate | PASS | PART A begins with a learner navigation aid and contains the complete learner-facing body, approved figure markers, micro-patches, and bounded mastery notes; compiler/process material is kept in PART B. |
| Zero-Omission Certificate | PASS | Scope/Audit/Crucible/PDF-required high-impact concepts are present, compressed by Content Lock, or repaired by logged micro-patches. |
| Mastery-Uplift Certificate | PASS | PART A includes source-labeled, adjacent, short augmentation notes without broad rewriting. |
| Source-Boundary Certificate | PASS | All augmentations are labeled by epistemic status; no expert inference is presented as textbook fact. |
| HTML-Readiness Certificate | PASS | PART B contains figure, page-tag, compiler, audit/crucible, patch-mode, and navigation guardrails. |

## Assembly Mode

PATCH MODE. `04_Content Lock v2(4).md` was used as the canonical scientific body. Approved marker blocks from `04_Content Lock v2.1(2).md` were spliced by exact anchors. Three high-impact micro-patches were added because the Scope Lock explicitly required anchors/equations that were compressed out of the learner-facing Content Lock body. Mastery augmentations were added only as visibly labeled adjacent notes.

## Input Manifest

| File | Role | Authority level | Used for | Notes |
|---|---|---:|---|---|
| `04_scope_lock(4).md` | Scope Lock | A0 | scope boundary; hard rules; learner and image-rights constraints | Used to check page ranges, key equations, and no-image policy |
| `04_G_청소율 간·신장·대사체(5).pdf` | Original textbook PDF — Gabrielsson | A1 | PDF verification source | Used to verify high-impact Gabrielsson scope, equations, PK5 anchors, and figure identities |
| `04_T_청소율 간·신장·대사체_01(5).pdf` | Original textbook PDF — Tozer Ch.5 | A1 | PDF verification source | Used to verify Ch.5 clearance, organ blood flow, extraction, renal physiology, and figure identities |
| `04_T_청소율 간·신장·대사체_02(5).pdf` | Original textbook PDF — Tozer Ch.20 | A1 | PDF verification source | Used to verify metabolite equations, scenarios, and figure identities |
| `04_T_청소율 간·신장·대사체_03(5).pdf` | Original textbook PDF — Tozer App.D/E | A1 | PDF verification source | Used to verify plasma-to-blood and well-stirred appendix equations |
| `04_Audit_Report_v1(4).md` | Audit Report v1 | A2 | audit guardrail | Used for MUST_FIX/SHOULD_FIX coverage and regression prevention |
| `04_Content Lock v2(4).md` | Content Lock v2 | A3 | canonical body | Primary learner body before figure-marker splicing |
| `04_Content Lock v2.1(2).md` | Content Lock v2.1 PATCH | A4 | figure insertion source | Used for approved figure markers and insertion map |
| `04_Crucible_Report_v1(1).md` | Crucible Report v1 | A5 | crucible guardrail | Used only for already-adopted or explicitly preserved high-value logic |
| `04_step1_draft_v0(3).md` | Step 1 Draft v0 | A6 | deprecated source | Used only as regression check; not copied into learner body |
| `붙여넣은 마크다운(2)(53).md` | Prompt 5 / HTML Compiler prompt | A7 | compiler instruction | Essential rendering, marker, page-tag, navigation, and HTML safety rules summarized/preserved in PART B |
| `S04_phase1_patch memo(2).md` | Patch Memo | attention guide | locked reference | Used only to understand known Phase 1 weaknesses; not a raw source |
| `04_Content Lock v1(2).md` | Content Lock v1 | locked reference | not used for body | Earlier lock version; superseded by Content Lock v2 |
| `붙여넣은 텍스트 (1)(76).txt` | Phase 4D assembly prompt | process instruction | assembly specification | Defines current master-file requirements; output filename adapted to user request: 04_html_compile_input_master.md |


## PART A — Learner-Facing Complete Handout

## Learner Navigation Aid

**How to use this handout**: Study PART A in four passes. First read §1 for the governing question, then read §2 M1-M14 as concept cards, then use §5 to separate look-alike concepts, and finally answer §7 before reviewing §8.

**Learning route**: `M1 clearance definition → M2-M3 renal measurement → M4-M6 hepatic/extraction/IVIVE logic → M7 implementation bridge → M8-M10 blood-basis and extended clearance → M11-M14 metabolite and renal-impairment decisions`.

**Figure-use rule**: Figure pointers identify where to consult the textbook object. Because image rights are locked as `None`, textbook figures are not reproduced in this markdown file and must not be embedded during HTML compilation.

## §1 Why This Chapter Matters

<!-- MASTER LENS -->
<!-- ANNOTATION -->
**Big Idea**: Clearance(← 농도 대비 제거능)는 `Dose/AUC`로 끝나는 숫자가 아니다. **혈류(`Q`), 단백결합(`f_u`, `f_{ub}`), intrinsic clearance(`CL_int`), permeability/transporter, renal filtration/secretion/reabsorption, metabolite formation/elimination**이 한 식 안에서 충돌한 결과다. 이 장의 목표는 `CL`을 외우는 것이 아니라, 관찰된 `CL`, `t1/2`, `AUC(m)/AUC`, `C/C_b` 변화가 어느 생리학적 병목에서 왔는지 역추적하는 것이다.

<!-- ANCHOR -->
<!-- ANNOTATION -->
학습 흐름은 네 단계다. 먼저 `Rate = CL·C`로 clearance의 비례관계를 세운다. 둘째, 신장에서는 `CL_R = f_e·CL`과 filtration/secretion/reabsorption으로 분해한다. 셋째, 간에서는 well-stirred 식으로 `Q_H`, `f_{ub}`, `CL_int`, permeability를 분리한다. 넷째, parent–metabolite 시스템에서는 `f_m`, `CL(m)`, rate-limiting step(← 전체 속도를 정하는 느린 단계), renal impairment를 별도 축으로 추가한다.

<!-- RECAP -->
이 문서에서 버릴 수 없는 한 문장은 다음이다: **“어떤 clearance인가?”라는 질문은 항상 “어느 농도 기준인가, 어느 장기인가, 어느 율속단계인가, parent인가 metabolite인가?”로 풀어야 한다.**

---

<!-- FIGURE_SCHEMATIC -->
Title: Clearance universe decision map: organ, route, concentration basis, and metabolite axis
Mode: N
Visual objective: 5초 안에 `CL` 해석이 total number가 아니라 네 가지 질문으로 분해됨을 보이게 한다.
Core message: `CL` 해석은 “어느 농도 기준인가, 어느 장기인가, 어느 route인가, parent인가 metabolite인가?”를 순서대로 묻는 구조적 문제다.
Elements to include: center node observed `CL`/`t1/2`/`AUC`/`AUC(m)/AUC`; branch concentration basis with plasma `CL` vs blood `CL_b`; branch organ route with renal `CL_R`, hepatic `CL_H`, other; branch hepatic determinants with `Q_H`, `f_{ub}`, `CL_int`, permeability/transporter; branch metabolite axis with `f_m`, `CL(m)`, rate-limiting step, renal impairment; final decision node dose/label/model interpretation.
Elements to exclude: numerical examples; full equations beyond variable labels; regulatory claims not already in Content Lock v2.
Suggested rendering: Mermaid
Caption: Clearance interpretation begins by splitting one observed number into concentration basis, organ route, route/extraction behavior, and metabolite-specific clearance.
Alt text: A flowchart starts from observed clearance-related metrics and branches to plasma versus blood basis, renal/hepatic routes, hepatic determinants, and metabolite-specific axes.
Source relation: Newly designed
<!-- /FIGURE_SCHEMATIC -->

## §2 Concept Anatomy Cards

### M1. Clearance proportionality + half-life is derived

<!-- MASTER LENS -->
**Big Idea**: Clearance는 제거 속도 자체가 아니라 **농도로 normalize한 제거능**이다. 따라서 `CL`은 first-order 조건에서 시간마다 새로 바뀌는 숫자가 아니라, 관찰 구간 전체를 설명하는 하나의 비례상수로 취급된다. `AUC`는 그 제거능이 시간 전체에 남긴 관찰량이다.

**Core equations** [G p.49 Eq 2:83–2:86; G pp.77–79 Eq 2:180–2:185; T5 pp.124–128 Eq 5-1–5-8]

$$\frac{dX}{dt}=-CL\cdot C$$

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

> **Practice Lens — [EXPERT_INFERENCE]**  
> In modeling work, treat half-life as a diagnostic summary, not as the primary covariate target. A covariate explanation should usually be framed on `CL` and/or `V` first, then translated back into `t_{1/2}` only after the mechanism is clear.

### M2. Renal clearance decomposition: `CL_R`, `f_e`, filtration/secretion/reabsorption

<!-- MASTER LENS -->
**Big Idea**: `CL_R = f_e·CL`은 단순 비례식이 아니다. **혈장 AUC와 소변 누적 배설량을 연결하는 measurement bridge**다. 혈장은 몸 안 노출을 보여주고, 소변은 renal route로 빠져나간 양을 보여준다. 둘을 함께 보아야 renal route의 지분 `f_e`와 `CL_R`가 열린다.

**Renal physiology compressed** [G p.48; T5 pp.138–145]

Nephron은 Bowman’s capsule, proximal tubule, loop of Henle, distal tubule, collecting duct로 구성된다. GFR은 Gabrielsson에서 110–130 mL/min, Tozer에서는 reference로 약 120 mL/min이다. Urine pH는 4.5–8 범위로 변할 수 있다 [G p.48; T5 pp.119–120, pp.138–145]. Inulin은 GFR marker로 언급되지만 본 handout에서는 physiology context로만 유지한다.

Tozer also gives average renal blood flow as approximately `1.1 L/min`; this is the renal blood-flow ceiling for renal organ extraction, whereas GFR is the filtered subset of renal plasma water [T5 pp.127, 140].

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

> **Failure Mode — [EXPERT_INFERENCE]**  
> Scaling total `CL` by renal function silently assumes the renal pathway is the whole clearance pathway. When `f_e` is credible, split renal and nonrenal components before applying a renal-function covariate.

### M3. ARE plot vs Excretion Rate plot

<!-- MASTER LENS -->
**Big Idea**: ARE plot과 excretion-rate plot은 같은 urinary data에서 `K`를 추정한다. 그러나 한쪽은 interval excretion rate를 보고, 다른 한쪽은 남은 누적 배설량을 본다. 그래서 noise와 시간 정보가 다르게 보인다. Rate plot은 renal clearance의 시간 변동을 잘 드러내고, ARE plot은 누적량 기반이라 변동을 평활한다.

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

<!-- FIGURE_POINTER -->
Source: [Gabrielsson & Weiner, p.50, Fig 2.35]
Why this matters: M3의 핵심 혼동은 두 plot의 slope가 모두 `K`를 주더라도 시간 배치와 noise 민감도가 다르다는 점이다. 원 figure는 ARE의 actual time과 rate plot의 midpoint convention을 직접 보여준다.
When to look: after reading this card
Learner instruction: 두 panel에서 x-axis time이 무엇을 의미하는지 먼저 확인하라. 그 다음 `X_{u,0-∞}` 의존성과 midpoint averaging이 각각 어느 plot에 들어가는지 표시하라.
<!-- /FIGURE_POINTER -->

> **Practice Lens — [AUDIT_DERIVED]**  
> A disagreement between ARE and excretion-rate plots is a data-process signal before it is a structural-model signal. Check collection intervals, midpoint assignment, bladder emptying, and urine pH/flow before adding compartments.

### M4. Well-stirred hepatic clearance + 4-model compression

<!-- MASTER LENS -->
<!-- ANNOTATION -->
**Big Idea**: Well-stirred model(← 간을 즉시 섞인 장기로 보는 모델)은 hepatic clearance를 세 입력값으로 압축한다: blood flow `Q_H`, blood unbound fraction `f_{ub}`, intrinsic clearance `CL_int`. 분모에서 `Q_H`가 큰지, `f_{ub}·CL_int`가 큰지에 따라 high/low extraction 분류와 임상 해석이 갈린다.

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

Well-stirred, parallel-tube, distributed, dispersion model은 모두 hepatic extraction을 설명한다. 차이는 간 안에서 blood와 hepatocyte가 얼마나 섞이는지, 그리고 concentration gradient를 어떻게 처리하는지에 있다. 본 Content Lock에서는 conceptual difference만 보존하고, distributed/dispersion 상세 수식은 source-fidelity risk 때문에 `[p.94; 확인 필요: formula-level 1:1 재검산 전까지 잠금]`으로 둔다.

<!-- CONFUSION -->
**Confusion**: “간청소율 식”을 plasma `C` 기준으로 쓰면 extraction ratio가 틀어진다. Organ extraction은 blood concentration 기준이며, plasma에서 측정한 값은 M8의 `C/C_b` 변환을 거쳐야 한다.

---

<!-- FIGURE_POINTER -->
Source: [Gabrielsson & Weiner, p.79, Fig 2.58; optional companion: Rowland & Tozer, p.131, Fig 5-7]
Why this matters: Well-stirred equation은 organ input-output 구조에서 출발한다. 그림을 보지 않으면 `Q_H`가 단순 covariate가 아니라 organ에 들어오는 blood flow ceiling이라는 점이 약해진다.
When to look: before reading this card
Learner instruction: 먼저 inlet concentration, outlet concentration, blood flow, extracted fraction을 하나의 organ balance로 읽어라. 그런 다음 `f_{ub}·CL_int >> Q_H`와 `f_{ub}·CL_int << Q_H`가 각각 어느 병목을 뜻하는지 대응시켜라.
<!-- /FIGURE_POINTER -->

> **Mastery Note — [TEXTBOOK_DERIVED]**  
> `Q_H` is not just another covariate; it is the blood-flow ceiling for hepatic blood clearance. The low-extraction limit is the opposite regime, where `f_{ub}·CL_int` rather than flow is the bottleneck.

### M5. High/low extraction + route × extraction × `f_u` matrix

<!-- MASTER LENS -->
**Big Idea**: 단백결합 변화의 해석은 `route × extraction × total/unbound concentration`의 3축 문제다. 즉, 같은 `f_u` 변화라도 IV인지 oral인지, high extraction인지 low extraction인지, total을 보는지 unbound를 보는지에 따라 결론이 달라진다. “High extraction이면 `f_u` 무관”은 **IV total concentration**에 한정되는 위험한 반쪽 문장이다.

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

<!-- FIGURE_SCHEMATIC -->
Title: Route × extraction × protein binding interpretation matrix
Mode: N
Visual objective: 5초 안에 IV/oral과 high/low extraction이 `f_u` 변화 해석을 바꾸는 4사분면임을 보이게 한다.
Core message: Protein binding effect는 drug label 하나로 결정되지 않고 route, extraction class, total/unbound endpoint에 따라 바뀐다.
Elements to include: 2×2 matrix with rows IV/oral and columns high extraction/low extraction; in each cell, total concentration/AUC response and unbound concentration/AUC response; side label “Do not transfer IV DDI conclusion to oral route without first-pass check”; small legend for total `C` vs unbound `C_u`.
Elements to exclude: drug-specific mini profiles; numeric fold changes; detailed Table 2.9 formula variants.
Suggested rendering: CSS-card
Caption: The same protein-binding change can have different clinical meaning depending on route, extraction ratio, and whether total or unbound concentration is interpreted.
Alt text: A two-by-two matrix compares IV and oral dosing against high and low extraction, with separate notes for total and unbound concentration interpretation.
Source relation: Newly designed
<!-- /FIGURE_SCHEMATIC -->

> **Failure Mode — [EXPERT_INFERENCE]**  
> A protein-binding conclusion is incomplete unless the report states route, extraction class, and whether total or unbound exposure is being interpreted. The common error is transferring an IV conclusion directly to oral dosing without checking first-pass behavior.

### M6. IVIVE pitfalls: single-point, MMP, data condensation

<!-- MASTER LENS -->
**Big Idea**: IVIVE는 `Vmax`, `Km`, microsomal protein scaling을 넣는 계산 문제가 아니다. 먼저 **어떤 정보를 버렸는지**를 점검해야 한다. 한 점에서 얻은 `CL_int`, 잘못된 MMP 보정, 과도한 data condensation은 모두 in vivo clearance를 왜곡한다.

**Core flow** [G pp.85–90]

$$CL_{int,in\ vitro}\rightarrow CL_{int,scaled}\rightarrow CL_H=\frac{Q_H\cdot f_u\cdot CL_{int}}{Q_H+f_u\cdot CL_{int}}$$

**Three traps**

1. **Single-point trap**: 한 농도에서 얻은 rate를 `Vmax/Km`처럼 쓰면 nonlinearity와 saturation을 놓친다 [G pp.85–89].
2. **MMP scaling trap**: microsomal protein per gram liver 보정은 평균값 하나가 아니라 variability와 ratio 처리 방식에 민감하다 [G p.87].
3. **Data condensation trap**: raw concentration–rate relation을 하나의 `CL_int`로 압축하면 curvature와 outlier 구조가 사라진다 [G pp.88–89].

<!-- TRENCH -->
**Trench-level tip**: IVIVE report를 검토할 때 첫 질문은 “well-stirred 식이 맞는가?”가 아니라 “in vitro rate 정보가 single point로 collapse되었는가?”다. Collapse된 입력은 정교한 hepatic model로도 복구되지 않는다.

---

> **Workflow Consequence — [TEXTBOOK_DERIVED]**  
> An IVIVE review starts upstream of the hepatic equation. Once the in vitro concentration–rate relation has been collapsed into one fragile `CL_int`, a more elaborate liver model cannot recover the lost curvature.

### M7. PK5 simultaneous plasma+urine fitting

<!-- MASTER LENS -->
**Big Idea**: PK5는 urinary data를 별도 계산표로 처리하지 않는다. **Plasma concentration과 cumulative urine amount를 한 모델에서 동시에 fitting**한다. 이 구조가 NONMEM에서 plasma+urine, IV+oral, parent+metabolite를 함께 fitting하는 사고방식의 출발점이다.

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
<!-- ANNOTATION -->
**Big Idea**: Organ extraction ratio(← 장기 통과 중 제거된 비율)는 blood flow와 비교하므로 **blood concentration 기준 clearance**가 필요하다. 그런데 실제 측정은 대부분 plasma concentration이다. `C/C_b` 변환을 하지 않으면 denominator가 달라진다. 그 결과 extraction ratio 분류가 systematic하게 틀어진다.

**Clearance relation** [T5 pp.124–128 Eq 5-4–5-6]

Let `R = C/C_b`.

$$CL_b=CL\cdot\frac{C}{C_b}=CL\cdot R$$

$$CL=CL_b\cdot\frac{C_b}{C}=\frac{CL_b}{R}$$

**App.D mass-balance** [TD pp.775–776 Eq D-1–D-8]

$$\frac{C}{C_b}=\frac{1}{1+H(f_uK_{PBC}-1)}$$

where `H` is hematocrit, `f_u` is unbound fraction in plasma, and `K_{PBC}` is the blood-cell-to-unbound-plasma partition coefficient.

**Micro-patch — required App.D inversion** [TD pp.775–776 Eq D-8]

$$K_{PBC}=\frac{H-1+(C_b/C)}{f_u\cdot H}$$

**Implication**

- If `R<1`, plasma concentration is lower than blood concentration; plasma CL can look smaller/larger depending on ratio usage.
- Hepatic extraction must use `E_H=CL_{H,b}/Q_H`, not plasma `CL_H/Q_H`.
- `f_u` and `f_{ub}` are not interchangeable. `f_{ub}=f_u·(C/C_b)`.

<!-- CONFUSION -->
**Confusion**: `CL=60 L/h`, `Q_H=81 L/h`이면 moderate extraction처럼 보일 수 있다. 그러나 `R=C/C_b=0.5`이면 `CL_b=30 L/h`이고 `E_H=0.37`이다. 분류가 바뀐다.

---

> **Judgment Lens — [TEXTBOOK_DERIVED]**  
> Plasma clearance can be adequate for exposure summary, but organ extraction classification requires a blood-basis denominator. Before calling a drug high or low extraction, confirm whether `CL_b`, not plasma `CL`, was compared with organ blood flow.

### M9. Permeability-rate-limited hepatic uptake: App.E `ρ`

<!-- MASTER LENS -->
**Big Idea**: Basic well-stirred model은 liver cell 안팎의 unbound concentration이 빠르게 평형이라고 가정한다. 그러나 hepatic uptake permeability가 느리면 hepatocyte 내부 unbound concentration이 blood unbound concentration보다 낮아진다. 이 경우 `CL_int`만으로는 hepatic clearance를 설명할 수 없다.

**App.E Model II** [TE pp.778–779 Eq E-9–E-15]

<!-- ANNOTATION -->
`ρ`(← 세포 안팎 unbound 비율)는 hepatocyte 내부 unbound concentration이 혈액 쪽 unbound concentration을 얼마나 따라가는지 나타낸다.

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
**Big Idea**: Extended clearance는 hepatic elimination을 “enzyme 하나”로 보지 않는다. **Sinusoidal uptake, canalicular efflux, basolateral efflux, intracellular metabolism**의 네 흐름으로 본다. Basic well-stirred는 이 네 흐름 중 membrane step이 충분히 빠른 특수한 경우다.

**Core source** [T5 pp.136–138 Eq 5-35–5-36]

T5는 hepatic elimination이 perfusion, plasma protein binding, hepatocellular activity만으로 끝나지 않고 membrane permeability와 transporter에 의해 달라질 수 있음을 명시한다. App.E는 이 점을 `ρ`로 first-principles화한다 [TE pp.778–779].

**Minimal interpretation**

- Uptake-limited: plasma/blood에서 hepatocyte로 들어가는 step이 병목.
- Metabolism-limited: cell 내부 도달은 충분하고 enzyme capacity가 병목.
- Efflux-limited: bile 또는 blood 방향 efflux가 병목.

<!-- ANCHOR -->
M10은 M6의 IVIVE trap과 M9의 `ρ`를 연결한다. 즉, poor IVIVE가 항상 enzyme assay 문제는 아니며, transporter/permeability term 누락일 수 있다.

---

<!-- FIGURE_POINTER -->
Source: [Rowland & Tozer, p.136, Fig 5-11; companion equations: Tozer App.E pp.778–779, Eq E-9–E-15]
Why this matters: M10은 cell membrane을 사이에 둔 uptake, metabolism, efflux의 위치 관계가 핵심이다. 이 위치 관계를 보지 않으면 permeability-limited clearance를 단순 low `CL_int`로 오해하기 쉽다.
When to look: before reading this card
Learner instruction: Sinusoidal uptake, intracellular metabolism, canalicular efflux, basolateral efflux를 서로 다른 arrow로 구분하라. 그 다음 `ρ<1`이 어느 membrane step의 병목을 뜻하는지 찾아라.
<!-- /FIGURE_POINTER -->

> **Failure Mode — [EXPERT_INFERENCE]**  
> A transporter or permeability bottleneck can masquerade as poor enzyme `CL_int` prediction. Before solving the discrepancy with an empirical scalar, check whether the well-stirred rapid-equilibration assumption is the weak link.

### M11. Rate-limiting step in metabolite disposition

<!-- MASTER LENS -->
<!-- ANNOTATION -->
**Big Idea**: 대사체 농도-시간 곡선의 terminal slope(← 말단 감소 구간의 기울기)는 대사체 자체의 half-life가 아닐 수 있다. Formation이 느리면 대사체는 parent의 “그림자”처럼 parent half-life로 감소한다. Elimination이 느리면 대사체 자체 half-life가 terminal phase를 지배한다.

**Why metabolites matter** [T20 pp.658–659]

Metabolites matter for five reasons: **action, toxicity, inhibition, induction, displacement**. 그러나 metabolite가 그런 성질을 가져도 충분한 concentration에 도달하지 않으면 therapeutic concern은 작다 [T20 p.659]. 즉, “active metabolite가 있다”와 “임상적으로 중요하다”는 같은 말이 아니다.

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

<!-- FIGURE_POINTER -->
Source: [Rowland & Tozer, p.660, Fig 20-1]
Why this matters: Metabolite terminal slope는 formation과 elimination 중 더 느린 step에 의해 결정된다. 원 figure는 parent → metabolite → eliminated metabolite 흐름에서 `k_f`, `k(m)`, other elimination을 동시에 보여준다.
When to look: before reading this card
Learner instruction: `k_f`와 `k(m)` 중 작은 rate constant가 terminal behavior를 지배한다는 점을 그림 위에 표시하라. Parallel decline을 보면 metabolite own half-life라고 쓰기 전에 formation-limited 가능성을 먼저 점검하라.
<!-- /FIGURE_POINTER -->

> **Mastery Note — [TEXTBOOK_DERIVED]**  
> The terminal slope after parent dosing is a system-level terminal slope. Calling it the metabolite’s own half-life requires separate evidence that metabolite elimination, not formation, is the slow step.

### M12. `AUC(m)/AUC` decomposition: `f_m × CL/CL(m)`

<!-- MASTER LENS -->
**Big Idea**: `AUC(m)/AUC`는 `f_m` 그 자체가 아니다. 이 비는 metabolite formation fraction과 metabolite clearance가 함께 들어간 compound quantity다. 따라서 AUC ratio 하나만 보고 formation 쪽 문제인지 elimination 쪽 문제인지 분리할 수 없다.

**Core equations** [T20 pp.662–665 Eq 20-4–20-7]

$$\frac{dA(m)}{dt}=CL_f\cdot C-CL(m)\cdot C(m)$$

Integrated over time:

$$\frac{AUC(m)}{AUC}=\frac{CL_f}{CL(m)}$$

with:

$$CL_f=f_m\cdot CL$$

Therefore:

$$\boxed{\frac{AUC(m)}{AUC}=f_m\cdot\frac{CL}{CL(m)}}$$

**Micro-patch — required Eq.20-7** [T20 p.664 Eq 20-7]

$$\frac{k(m)}{k}=\frac{CL(m)/CL}{V(m)/V}$$

**Audit correction**

If `AUC(m)/AUC < 1` and `f_m` is unknown, one cannot infer `CL(m) ≥ CL/f_m`. Only the source-consistent inequality `CL(m)>f_m·CL` follows. The same AUC ratio can arise from low `f_m`, high `CL(m)`, or both.

**Examples retained** [T20 pp.662–665]

Methylprednisolone hemisuccinate → methylprednisolone, tolbutamide → hydroxytolbutamide, and propranolol → naphthoxylactic acid illustrate how metabolite curves distinguish rate-limiting steps and relative clearance. Detailed figure numeric readings are not expanded here.

<!-- TRENCH -->
**Trench-level tip**: active metabolite PopPK에서 `AUC(m)/AUC`가 작다는 이유로 metabolite를 무시하지 않는다. `f_m`이 작아도 `CL(m)`이 renal impairment에서 크게 줄면 M14의 문제가 된다.

---

### M13. First-pass metabolite contribution + steady-state metabolite

<!-- MASTER LENS -->
**Big Idea**: Oral parent dosing 후 metabolite는 두 경로에서 생길 수 있다: absorption 중 first-pass formation, 그리고 흡수된 systemic parent에서 생기는 post-absorption formation. 이것은 “oral이 항상 더 강하다”는 규칙이 아니다. Parent가 high first-pass extraction을 보이고 metabolite가 active 또는 clinically relevant할 때 문제가 된다.

**First-pass dual-source model** [T20 pp.665–669]

Observed metabolite after oral parent dosing is the sum of two inputs:

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
**Big Idea**: Parent `f_e` alone is not enough for renal impairment dosing when active metabolite exists. The highest-risk case is not always “parent mostly renal.” It can be “parent partly metabolized to an active metabolite that is itself renally cleared.”

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

Interconversion means parent and metabolite can regenerate each other. 따라서 metabolite 쪽 renal impairment가 parent의 apparent elimination까지 늦출 수 있다. Clofibric acid is retained as a qualitative example; figure-derived numeric anchors are not locked `[T20 p.679; 확인 필요]`.

<!-- CONFUSION -->
**Confusion**: “minor metabolite pathway” is not the same as “minor safety concern.” If metabolite `CL(m)` collapses in renal impairment, a small `f_m` can still become the main exposure driver.

---

<!-- FIGURE_POINTER -->
Source: [Rowland & Tozer, p.674, Fig 20-10 and Table 20-4]
Why this matters: M14의 위험은 parent exposure 상승보다 active metabolite exposure 상승이 훨씬 클 수 있다는 비대칭성이다. Fig 20-10/Table 20-4는 parent-only dose adjustment가 왜 실패하는지 보여주는 핵심 evidence object다.
When to look: after reading this card
Learner instruction: 정상 상태와 anuric condition에서 parent와 metabolite contribution을 따로 비교하라. 최종 dose ratio를 보기 전에 metabolite `CL(m)`이 얼마나 무너지는지 먼저 확인하라.
<!-- /FIGURE_POINTER -->

> **Practice Lens — [EXPERT_INFERENCE]**  
> A defensible renal-impairment argument should present parent and active-metabolite exposure together. Parent-only adjustment can be numerically clean but clinically incomplete when metabolite clearance is the collapsing pathway.

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

## PART B — Compiler-Only Appendix

This appendix is not learner-facing. It exists only to protect Phase 5 rendering fidelity and prevent regression.

### B1. Compilation Contract

- PART A is the only learner-facing body.
- Phase 5 must render PART A without altering content.
- PART B is instruction/guardrail only.
- Do not restore deprecated material.
- Do not add new scientific content.
- Do not render PART B as learner content unless explicitly requested.
- Do not convert this markdown into HTML during Phase 4D.

### B2. Figure Rendering Instructions

- Preserve the approved Figure Strategy and Insertion Map below.
- Preserve P/N decisions and all `Source:` fields inside figure markers.
- Image rights = `None`: do not embed copyrighted textbook images. Render `FIGURE_POINTER` as a text-only callout.
- Do not propose or generate new figures.
- Do not generate Mermaid/SVG in Phase 4D. Phase 5 may render approved schematics only from these briefs.
- Approved KEEP markers: #1-#7. Rejected lower-priority candidates R1-R5 must not be restored.

## 1. Figure Strategy Table — View A. Reading-order Figure Plan

| # | Reading order | Location (§ + concept card) | Mode | Source figure / source object | Trigger | Why text alone is insufficient | Expected learning gain | Decision |
|---:|---|---|---|---|---|---|---|---|
| 1 | §1 | Why This Chapter Matters | N | None — source-synthesized overview | G3, G4 | 본문은 M1–M14를 순서대로 설명하지만, `CL`, organ extraction, route, parent–metabolite, renal impairment가 하나의 decision space에서 어떻게 연결되는지는 한눈에 보이지 않는다. | 학습자가 “어떤 clearance인가?”를 네 축 질문으로 분해하는 전체 항법도를 먼저 얻는다. | KEEP |
| 2 | §2 | M3. ARE plot vs Excretion Rate plot | P | Gabrielsson p.50, Fig 2.35 | G2, G5 | ARE plot의 actual time과 rate plot의 midpoint convention은 텍스트 표만으로는 머릿속에서 쉽게 섞인다. | urinary plot을 “같은 slope를 추정하지만 시간 정보가 다른 두 도구”로 분리한다. | KEEP |
| 3 | §2 | M4. Well-stirred hepatic clearance + 4-model compression | P | Gabrielsson p.79, Fig 2.58; optional companion: Tozer p.131, Fig 5-7 | G1, G5 | well-stirred 식은 `Q_H`, `f_{ub}`, `CL_int`가 하나의 분수식에 들어가므로, organ input-output 구조를 보지 않으면 분모의 의미가 추상화된다. | hepatic extraction을 “혈류가 들어오고, 일부가 제거되고, 나머지가 나가는 organ balance”로 고정한다. | KEEP |
| 4 | §2 | M5. High/low extraction + route × extraction × `f_u` matrix | N | Newly designed from source equations/cases | G1, G2, G4 | high/low extraction, IV/oral route, total/unbound concentration이 동시에 바뀌므로 문장형 설명은 4사분면 오개념을 막기 어렵다. | “High extraction이면 `f_u` 무관”이라는 반쪽 문장을 route와 concentration 기준으로 교정한다. | KEEP |
| 5 | §2 | M10. Extended clearance: transporter–enzyme architecture | P | Tozer p.136, Fig 5-11; companion equations: Tozer App.E pp.778–779, Eq E-9–E-15 | G1, G5 | uptake, metabolism, efflux, permeability가 cell membrane을 사이에 두고 배열되는 구조는 수식만으로는 위치 관계가 흐려진다. | well-stirred model이 transporter/permeability step이 빠른 특수한 경우임을 시각적으로 분리한다. | KEEP |
| 6 | §2 | M11. Rate-limiting step in metabolite disposition | P | Tozer p.660, Fig 20-1 | G1, G2, G5 | formation-limited와 elimination-limited의 차이는 terminal slope가 parent를 따르는지 metabolite를 따르는지의 시간 패턴 문제다. | “metabolite terminal half-life = metabolite own half-life”라는 자동 해석을 차단한다. | KEEP |
| 7 | §2 | M14. Renal impairment active-metabolite scenario + interconversion | P | Tozer p.674, Fig 20-10 and Table 20-4 | G1, G2, G5 | parent와 active metabolite가 renal impairment에서 서로 다른 폭으로 상승하는 위험은 숫자표와 profile을 함께 봐야 구조가 잡힌다. | parent-only dose adjustment가 왜 active metabolite accumulation을 놓치는지 한 번에 확인한다. | KEEP |
| R1 | §2 | M2. Renal clearance decomposition | P/R candidate | Tozer p.140, Fig 5-14 | G1, G5 | filtration/secretion/reabsorption은 시각적으로 유용하다. | M2 식 이해 보조. | REJECT — budget 초과 시 M3 urinary-plot confusion이 더 큰 learner failure를 제거함. |
| R2 | §2 | M6. IVIVE pitfalls | P/R candidate | Gabrielsson pp.88–89, Fig 2.63–2.65 | G2, G5 | single-point, MMP, data condensation의 위험을 그림으로 볼 수 있다. | IVIVE audit mindset 강화. | REJECT — 본문에 3 trap이 이미 명시되어 있고, schematic budget은 §1 overview와 M5 matrix에 배정. |
| R3 | §2 | M7. PK5 simultaneous plasma+urine fitting | P candidate | Gabrielsson pp.495–497, PK5 Fig 5.1 and Fig 5.3 | G1, G5 | simultaneous fitting 구조는 중요하다. | plasma+urine fitting implementation 강화. | REJECT — implementation evidence figure로는 가치가 높지만, 본 v2.1의 core conceptual budget에서는 M10/M11/M14보다 낮음. |
| R4 | §2 | M8. Plasma-to-blood ratio and blood clearance | P candidate | Tozer App.D pp.775–776, Eq D-1–D-8 | G1, G5 | mass-balance derivation은 시각적 보조가 가능하다. | `C/C_b`, `f_u`, hematocrit 연결 강화. | REJECT — M8 본문 equation block이 충분하고, organ extraction failure는 M4/M5 marker로 더 직접 해결됨. |
| R5 | §2 | M13. First-pass metabolite contribution + steady-state metabolite | P candidate | Tozer pp.666–668, Fig 20-5–20-7; p.671 Fig 20-8 | G1, G5 | oral first-pass metabolite input과 accumulation profile은 figure 가치가 있다. | route-dependent metabolite exposure 강화. | REJECT — M14 active-metabolite renal impairment가 더 큰 safety/decision failure를 제거함. |

---

## 2. Figure Strategy Table — View B. Type-sorted Summary

- **Pointers (P)**: #2, #3, #5, #6, #7 → **5 / max 5** for A-Critical budget.
- **Schematics (R/N combined)**: #1, #4 → **2 / max 2** for A-Critical budget.
- **Images (I)**: none → Image rights = None; no direct textbook image insertion.
- **Rejected due to budget / lower marginal ROI**: R1–R5.

**Budget verdict**: PASS. No Mode I proposed. No textbook image reproduction proposed.

---

## 3. Figure Briefs — KEEP Items Only

### Figure #1 — New schematic

- **Title**: Clearance universe decision map: organ, route, concentration basis, and metabolite axis
- **Visual objective**: 5초 안에 `CL` 해석이 total number가 아니라 네 가지 질문으로 분해됨을 보이게 한다.
- **Core message**: `CL` 해석은 “어느 농도 기준인가, 어느 장기인가, 어느 route인가, parent인가 metabolite인가?”를 순서대로 묻는 구조적 문제다.
- **Elements to include**:
  - Center node: observed `CL`, `t1/2`, `AUC`, `AUC(m)/AUC`
  - Branch 1: concentration basis → plasma `CL` vs blood `CL_b`
  - Branch 2: organ route → renal `CL_R`, hepatic `CL_H`, other
  - Branch 3: hepatic determinants → `Q_H`, `f_{ub}`, `CL_int`, permeability/transporter
  - Branch 4: metabolite axis → `f_m`, `CL(m)`, rate-limiting step, renal impairment
  - Final decision node: dose/label/model interpretation
- **Elements to exclude**:
  - Numerical examples
  - Full equations beyond variable labels
  - Regulatory claims not already in Content Lock v2
- **Suggested rendering**: Mermaid flowchart
- **Caption**: Clearance interpretation begins by splitting one observed number into concentration basis, organ route, route/extraction behavior, and metabolite-specific clearance.
- **Alt text**: A flowchart starts from observed clearance-related metrics and branches to plasma versus blood basis, renal/hepatic routes, hepatic determinants, and metabolite-specific axes.
- **Source relation**: Newly designed

### Figure #2 — Pointer

- **Source**: Gabrielsson & Weiner, p.50, Fig 2.35 — ARE plot and excretion-rate plot schematic.
- **Why this figure matters**: M3의 핵심 혼동은 두 plot의 slope가 모두 `K`를 주더라도 시간 배치와 noise 민감도가 다르다는 점이다. 원 figure는 ARE의 actual time과 rate plot의 midpoint convention을 직접 보여준다.
- **When to look**: After reading M3.
- **Learner instruction**: 두 panel에서 x-axis time이 무엇을 의미하는지 먼저 확인하라. 그 다음 `X_{u,0-∞}` 의존성과 midpoint averaging이 각각 어느 plot에 들어가는지 표시하라.

### Figure #3 — Pointer

- **Source**: Gabrielsson & Weiner, p.79, Fig 2.58 — extraction across eliminating organ; optional companion: Rowland & Tozer, p.131, Fig 5-7 — perfusion effect on hepatic clearance/extraction.
- **Why this figure matters**: well-stirred equation은 organ input-output 구조에서 출발한다. 그림을 보지 않으면 `Q_H`가 단순 covariate가 아니라 organ에 들어오는 blood flow ceiling이라는 점이 약해진다.
- **When to look**: Before reading the limiting-case table in M4.
- **Learner instruction**: 먼저 inlet concentration, outlet concentration, blood flow, extracted fraction을 하나의 organ balance로 읽어라. 그런 다음 `f_{ub}·CL_int >> Q_H`와 `f_{ub}·CL_int << Q_H`가 각각 어느 병목을 뜻하는지 대응시켜라.

### Figure #4 — New schematic

- **Title**: Route × extraction × protein binding interpretation matrix
- **Visual objective**: 5초 안에 IV/oral과 high/low extraction이 `f_u` 변화 해석을 바꾸는 4사분면임을 보이게 한다.
- **Core message**: Protein binding effect는 drug label 하나로 결정되지 않고 route, extraction class, total/unbound endpoint에 따라 바뀐다.
- **Elements to include**:
  - 2×2 matrix: rows = IV / oral; columns = high extraction / low extraction
  - Each cell: total concentration/AUC response and unbound concentration/AUC response
  - Side label: “Do not transfer IV DDI conclusion to oral route without first-pass check”
  - Small legend: total `C` vs unbound `C_u`
- **Elements to exclude**:
  - Drug-specific mini profiles
  - Numeric fold changes
  - Detailed Table 2.9 formula variants
- **Suggested rendering**: CSS-card
- **Caption**: The same protein-binding change can have different clinical meaning depending on route, extraction ratio, and whether total or unbound concentration is interpreted.
- **Alt text**: A two-by-two matrix compares IV and oral dosing against high and low extraction, with separate notes for total and unbound concentration interpretation.
- **Source relation**: Newly designed

### Figure #5 — Pointer

- **Source**: Rowland & Tozer, p.136, Fig 5-11 — hepatocyte transporter/enzyme location and extended clearance; companion: Tozer App.E pp.778–779, Eq E-9–E-15 for `ρ`.
- **Why this figure matters**: M10은 cell membrane을 사이에 둔 uptake, metabolism, efflux의 위치 관계가 핵심이다. 이 위치 관계를 보지 않으면 permeability-limited clearance를 단순 low `CL_int`로 오해하기 쉽다.
- **When to look**: After reading M9 and before reading M10.
- **Learner instruction**: Sinusoidal uptake, intracellular metabolism, canalicular efflux, basolateral efflux를 서로 다른 arrow로 구분하라. 그 다음 `ρ<1`이 어느 membrane step의 병목을 뜻하는지 찾아라.

### Figure #6 — Pointer

- **Source**: Rowland & Tozer, p.660, Fig 20-1 — rate-limiting step in metabolite disposition.
- **Why this figure matters**: metabolite terminal slope는 formation과 elimination 중 더 느린 step에 의해 결정된다. 원 figure는 parent → metabolite → eliminated metabolite 흐름에서 `k_f`, `k(m)`, other elimination을 동시에 보여준다.
- **When to look**: Before reading the Case table in M11.
- **Learner instruction**: `k_f`와 `k(m)` 중 작은 rate constant가 terminal behavior를 지배한다는 점을 그림 위에 표시하라. Parallel decline을 보면 metabolite own half-life라고 쓰기 전에 formation-limited 가능성을 먼저 점검하라.

### Figure #7 — Pointer

- **Source**: Rowland & Tozer, p.674, Fig 20-10 and Table 20-4 — active metabolite accumulation in renal insufficiency.
- **Why this figure matters**: M14의 위험은 parent exposure 상승보다 active metabolite exposure 상승이 훨씬 클 수 있다는 비대칭성이다. Fig 20-10/Table 20-4는 parent-only dose adjustment가 왜 실패하는지 보여주는 핵심 evidence object다.
- **When to look**: After reading the Tozer worked scenario in M14.
- **Learner instruction**: 정상 상태와 anuric condition에서 parent와 metabolite contribution을 따로 비교하라. 최종 dose ratio를 보기 전에 metabolite `CL(m)`이 얼마나 무너지는지 먼저 확인하라.

---

## 4. Insertion Map (PATCH MODE)

| # | Reading order | Anchor copied verbatim from Content Lock v2 | Insert position | Marker block ID |
|---:|---|---|---|---|
| 1 | §1 | `## §1 Why This Chapter Matters` | before next §heading | Marker block #1 |
| 2 | §2 / M3 | `### M3. ARE plot vs Excretion Rate plot` | after this anchor card | Marker block #2 |
| 3 | §2 / M4 | `### M4. Well-stirred hepatic clearance + 4-model compression` | after this anchor card | Marker block #3 |
| 4 | §2 / M5 | `### M5. High/low extraction + route × extraction × \`f_u\` matrix` | after this anchor card | Marker block #4 |
| 5 | §2 / M10 | `### M10. Extended clearance: transporter–enzyme architecture` | after this anchor card | Marker block #5 |
| 6 | §2 / M11 | `### M11. Rate-limiting step in metabolite disposition` | after this anchor card | Marker block #6 |
| 7 | §2 / M14 | `### M14. Renal impairment active-metabolite scenario + interconversion` | after this anchor card | Marker block #7 |

### Marker block #1

```text
<!-- FIGURE_SCHEMATIC -->
Title: Clearance universe decision map: organ, route, concentration basis, and metabolite axis
Mode: N
Visual objective: 5초 안에 `CL` 해석이 total number가 아니라 네 가지 질문으로 분해됨을 보이게 한다.
Core message: `CL` 해석은 “어느 농도 기준인가, 어느 장기인가, 어느 route인가, parent인가 metabolite인가?”를 순서대로 묻는 구조적 문제다.
Elements to include: center node observed `CL`/`t1/2`/`AUC`/`AUC(m)/AUC`; branch concentration basis with plasma `CL` vs blood `CL_b`; branch organ route with renal `CL_R`, hepatic `CL_H`, other; branch hepatic determinants with `Q_H`, `f_{ub}`, `CL_int`, permeability/transporter; branch metabolite axis with `f_m`, `CL(m)`, rate-limiting step, renal impairment; final decision node dose/label/model interpretation.
Elements to exclude: numerical examples; full equations beyond variable labels; regulatory claims not already in Content Lock v2.
Suggested rendering: Mermaid
Caption: Clearance interpretation begins by splitting one observed number into concentration basis, organ route, route/extraction behavior, and metabolite-specific clearance.
Alt text: A flowchart starts from observed clearance-related metrics and branches to plasma versus blood basis, renal/hepatic routes, hepatic determinants, and metabolite-specific axes.
Source relation: Newly designed
<!-- /FIGURE_SCHEMATIC -->
```

### Marker block #2

```text
<!-- FIGURE_POINTER -->
Source: [Gabrielsson & Weiner, p.50, Fig 2.35]
Why this matters: M3의 핵심 혼동은 두 plot의 slope가 모두 `K`를 주더라도 시간 배치와 noise 민감도가 다르다는 점이다. 원 figure는 ARE의 actual time과 rate plot의 midpoint convention을 직접 보여준다.
When to look: after reading this card
Learner instruction: 두 panel에서 x-axis time이 무엇을 의미하는지 먼저 확인하라. 그 다음 `X_{u,0-∞}` 의존성과 midpoint averaging이 각각 어느 plot에 들어가는지 표시하라.
<!-- /FIGURE_POINTER -->
```

### Marker block #3

```text
<!-- FIGURE_POINTER -->
Source: [Gabrielsson & Weiner, p.79, Fig 2.58; optional companion: Rowland & Tozer, p.131, Fig 5-7]
Why this matters: Well-stirred equation은 organ input-output 구조에서 출발한다. 그림을 보지 않으면 `Q_H`가 단순 covariate가 아니라 organ에 들어오는 blood flow ceiling이라는 점이 약해진다.
When to look: before reading this card
Learner instruction: 먼저 inlet concentration, outlet concentration, blood flow, extracted fraction을 하나의 organ balance로 읽어라. 그런 다음 `f_{ub}·CL_int >> Q_H`와 `f_{ub}·CL_int << Q_H`가 각각 어느 병목을 뜻하는지 대응시켜라.
<!-- /FIGURE_POINTER -->
```

### Marker block #4

```text
<!-- FIGURE_SCHEMATIC -->
Title: Route × extraction × protein binding interpretation matrix
Mode: N
Visual objective: 5초 안에 IV/oral과 high/low extraction이 `f_u` 변화 해석을 바꾸는 4사분면임을 보이게 한다.
Core message: Protein binding effect는 drug label 하나로 결정되지 않고 route, extraction class, total/unbound endpoint에 따라 바뀐다.
Elements to include: 2×2 matrix with rows IV/oral and columns high extraction/low extraction; in each cell, total concentration/AUC response and unbound concentration/AUC response; side label “Do not transfer IV DDI conclusion to oral route without first-pass check”; small legend for total `C` vs unbound `C_u`.
Elements to exclude: drug-specific mini profiles; numeric fold changes; detailed Table 2.9 formula variants.
Suggested rendering: CSS-card
Caption: The same protein-binding change can have different clinical meaning depending on route, extraction ratio, and whether total or unbound concentration is interpreted.
Alt text: A two-by-two matrix compares IV and oral dosing against high and low extraction, with separate notes for total and unbound concentration interpretation.
Source relation: Newly designed
<!-- /FIGURE_SCHEMATIC -->
```

### Marker block #5

```text
<!-- FIGURE_POINTER -->
Source: [Rowland & Tozer, p.136, Fig 5-11; companion equations: Tozer App.E pp.778–779, Eq E-9–E-15]
Why this matters: M10은 cell membrane을 사이에 둔 uptake, metabolism, efflux의 위치 관계가 핵심이다. 이 위치 관계를 보지 않으면 permeability-limited clearance를 단순 low `CL_int`로 오해하기 쉽다.
When to look: before reading this card
Learner instruction: Sinusoidal uptake, intracellular metabolism, canalicular efflux, basolateral efflux를 서로 다른 arrow로 구분하라. 그 다음 `ρ<1`이 어느 membrane step의 병목을 뜻하는지 찾아라.
<!-- /FIGURE_POINTER -->
```

### Marker block #6

```text
<!-- FIGURE_POINTER -->
Source: [Rowland & Tozer, p.660, Fig 20-1]
Why this matters: Metabolite terminal slope는 formation과 elimination 중 더 느린 step에 의해 결정된다. 원 figure는 parent → metabolite → eliminated metabolite 흐름에서 `k_f`, `k(m)`, other elimination을 동시에 보여준다.
When to look: before reading this card
Learner instruction: `k_f`와 `k(m)` 중 작은 rate constant가 terminal behavior를 지배한다는 점을 그림 위에 표시하라. Parallel decline을 보면 metabolite own half-life라고 쓰기 전에 formation-limited 가능성을 먼저 점검하라.
<!-- /FIGURE_POINTER -->
```

### Marker block #7

```text
<!-- FIGURE_POINTER -->
Source: [Rowland & Tozer, p.674, Fig 20-10 and Table 20-4]
Why this matters: M14의 위험은 parent exposure 상승보다 active metabolite exposure 상승이 훨씬 클 수 있다는 비대칭성이다. Fig 20-10/Table 20-4는 parent-only dose adjustment가 왜 실패하는지 보여주는 핵심 evidence object다.
When to look: after reading this card
Learner instruction: 정상 상태와 anuric condition에서 parent와 metabolite contribution을 따로 비교하라. 최종 dose ratio를 보기 전에 metabolite `CL(m)`이 얼마나 무너지는지 먼저 확인하라.
<!-- /FIGURE_POINTER -->
```

---

### B3. Page Tag Rendering Rules

- Preserve all `[p.XX]`, `[pp.XX-YY]`, `[pp.XX–YY]`, `[pp.XX, YY]`, and `[p.확인 필요]` tags.
- Render source page tags visibly in HTML.
- Do not fabricate, delete, renumber, or relocate page tags.
- `[p.확인 필요]` remains visible unless already resolved by Audit/Content Lock.
- Do not apply page-tag regex inside code blocks or inside `FIGURE_*` marker blocks.
- Source page tags must remain visible in print mode.

### B4. HTML Compiler Requirements

- Render content; do not alter learner-facing text.
- Produce a single self-contained HTML file with inline CSS/JS.
- Use MathJax for equations and preserve display/inline math integrity.
- Convert all semantic markers to their mapped HTML components; never leave marker comments visible as plain text.
- Detect source page tags such as `[p.XX]`, `[pp.XX-YY]`, `[pp.XX, YY]`, and `[p.확인 필요]` and wrap them visibly in source-page spans.
- Include sticky left sidebar navigation with stable anchors, smooth scrolling, no duplicate ids, and verified matching `href="#id"` targets.
- Render `FIGURE_POINTER` as text-only textbook-reference callouts.
- Render `FIGURE_SCHEMATIC` only from approved briefs; do not reproduce textbook figures or add unapproved figures.
- Preserve self-test answer hiding through click-to-reveal accordions.
- Include print/PDF controls and ensure source page tags remain visible in print.
- Do not embed copyrighted textbook images; Image rights are `None`.


#### B4-full. Prompt 5 rendering contract preserved for Phase 5

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

Audit Report v1 is a regression-prevention source at this stage, not raw prose for new learner content. Preserve the following boundaries:

- Unsupported overclaims from Step 1 Draft v0.
- Unsupported numerical values or figure-derived values not preserved with `[확인 필요]`.
- Unsupported OFV thresholds or unapproved NONMEM code blocks.
- Unsupported FDA/EMA/ICH reviewer claims not grounded in the locked body.
- Digoxin/morphine 50-fold type errors or any route/dose misframing rejected by Audit.
- G Fig.1.2 E or any unrelated figure misinterpretation.
- Unsupported CYP2C9/VKORC1 wording, if encountered from deprecated drafts.
- Any NOT_IN_SOURCE item rejected by Audit or Content Lock.
- Any unapproved figure embedding or direct textbook-image reproduction.


Specific locked corrections already represented in PART A include:

- `AUC(m)/AUC` is not `f_m`; use `AUC(m)/AUC = f_m·CL/CL(m)`.
- If `AUC(m)/AUC < 1` and `f_m` is unknown, do not infer `CL(m) ≥ CL/f_m`; only `CL(m) > f_m·CL` follows under the stated source-consistent relation.
- Sequential metabolism is not controlled by the fastest rate constant; downstream terminal behavior follows the slow step.
- Passive diffusion/permeability large enough for rapid equilibration yields `ρ→1`; low permeability yields `ρ<1` and permeability-limited hepatic clearance.
- Figure-derived values marked `[확인 필요]` must remain visibly uncertain.

### B6. Crucible Guardrails

- Crucible Report v1 is not a raw content source at Phase 4D.
- Preserve only already-adopted or explicitly allowed Grade A logic.
- Do not reintroduce omitted/rejected Crucible items.
- Do not convert speculative insight into textbook-derived fact.
- Mastery augmentations derived from expert interpretation must remain labeled as `EXPERT_INFERENCE`.

### B7. Deprecated and Forbidden Restorations

- Step 1 Draft v0 is deprecated.
- Do not restore rejected overclaims, unsupported numbers, unsupported regulatory claims, source-unsupported examples, unapproved code, or unapproved figures.
- Do not use Step 1 Draft v0 as learner-body source except through the Micro-Patch Gate.
- Do not reopen Phase 4 decisions unless a HOLD condition is triggered by explicit source conflict.

### B8. PATCH MODE Splice Verification Table

| Marker # | Anchor text | Anchor found? | Match count | Inserted? | Final location (§ + card) |
|---:|---|---:|---:|---:|---|
| 1 | `## §1 Why This Chapter Matters` | YES | 1 | YES | §1 Why This Chapter Matters |
| 2 | `### M3. ARE plot vs Excretion Rate plot` | YES | 1 | YES | §2 / M3. ARE plot vs Excretion Rate plot |
| 3 | `### M4. Well-stirred hepatic clearance + 4-model compression` | YES | 1 | YES | §2 / M4. Well-stirred hepatic clearance + 4-model compression |
| 4 | `### M5. High/low extraction + route × extraction × `f_u` matrix` | YES | 1 | YES | §2 / M5. High/low extraction + route × extraction × f_u matrix |
| 5 | `### M10. Extended clearance: transporter–enzyme architecture` | YES | 1 | YES | §2 / M10. Extended clearance: transporter–enzyme architecture |
| 6 | `### M11. Rate-limiting step in metabolite disposition` | YES | 1 | YES | §2 / M11. Rate-limiting step in metabolite disposition |
| 7 | `### M14. Renal impairment active-metabolite scenario + interconversion` | YES | 1 | YES | §2 / M14. Renal impairment active-metabolite scenario + interconversion |


### B9. Zero-Omission Coverage Matrix

| Domain | Required item | Evidence in PART A | Status | Action |
|---|---|---|---|---|
| C1 Scope Lock | Gabrielsson §2.3 renal clearance, ARE/rate plots, simultaneous plasma+urine logic | PART A M2, M3, M7 | PRESENT | None |
| C1 Scope Lock | Gabrielsson §2.5 clearance concepts, well-stirred, route/extraction, IVIVE | PART A M4-M6 | PRESENT | None |
| C1 Scope Lock | PK5 practical implementation anchor | PART A M7 | PRESENT | None |
| C1 Scope Lock | Tozer Ch.5 elimination, extraction ratio, hepatic/renal physiology, blood clearance | PART A M1-M5, M8-M10 | PRESENT | None |
| C1 Scope Lock | Tozer Ch.20 metabolite rate-limiting, AUC ratio, first-pass, steady state, renal impairment/interconversion | PART A M11-M14 | PRESENT | None |
| C1 Scope Lock | Appendix D plasma-to-blood derivation and D-8 inversion | PART A M8 plus Micro-patch #2 | REPAIRED_BY_MICRO_PATCH | D-8 equation restored from Scope/Audit/PDF |
| C1 Scope Lock | Appendix E well-stirred and permeability-limited equations including oral AUC bridge | PART A M4 and M9 | PRESENT | None |
| C2 Data anchors | Hepatic blood flow QH = 1.35 L/min (=81 L/h) | PART A M4 | PRESENT | None |
| C2 Data anchors | Renal blood flow QR ≈ 1.1 L/min | PART A M2 plus Micro-patch #1 | REPAIRED_BY_MICRO_PATCH | Added as physiologic anchor |
| C2 Data anchors | GFR 110-130 mL/min / ~120 mL/min and urine pH 4.5-8 | PART A M2 | PRESENT | None |
| C2 Data anchors | PK5 dose and final estimates | PART A M7 | PRESENT | None |
| C2 Data anchors | Tozer active-metabolite renal-impairment scenario numeric anchors | PART A M14 | PRESENT | None |
| C3 Audit MUST_FIX/SHOULD_FIX | MUST_FIX items from equation/numerical audit | Content Lock v2 body retained; M8/M12 micro-patches added for Scope key equations | PRESENT | None |
| C3 Audit MUST_FIX/SHOULD_FIX | Urinary concentration negligible-level sampling caveat | PART A M3 | PRESENT | None |
| C3 Audit MUST_FIX/SHOULD_FIX | AUC(m)/AUC correction and inequality guardrail | PART A M12 | PRESENT | None |
| C4 Audit T5 coverage | OMITTED_PROBLEMATIC / MISSING_CRITICAL / MISSING_BRIDGE high-impact issues | PART A M1-M14; Part B audit guardrails | PRESENT_COMPRESSED | No HOLD_UNRESOLVED items identified |
| C5 Figure coverage | Approved KEEP figure markers #1-#7 | PART A has 5 FIGURE_POINTER and 2 FIGURE_SCHEMATIC markers | PRESENT | All approved markers present exactly once |
| C5 Figure coverage | Rejected figures R1-R5 not restored | PART B B2 lists rejected figures; PART A includes no R1-R5 markers | PRESENT | None |
| C5 Figure coverage | Image rights = None | PART A figure-use rule; PART B B2 | PRESENT | No textbook image embedded |
| C6 Page tags | Preserve source page tags and uncertainty tags | PART A body retains existing tags; micro-patches use verified tags only | PRESENT | None |
| C7 Crucible Grade A | High-value adopted logic retained | PART A §1, M cards, §5, §7, §8 | PRESENT_COMPRESSED | Crucible not used as raw prose source |
| C8 Deprecated draft regression | Rejected/unsupported Step 1 claims not restored | PART B B5-B7 | PRESENT | Step 1 not used as body source |
| C9 Canonical integrity | Scientific body remains Content Lock v2 plus approved markers, micro-patches, and labeled augmentation | PART A | PRESENT | Allowed additions logged |


### B10. Micro-Patch Log

| Patch # | Location | Source trigger | Inserted text | PDF/Audit basis | Why allowed | Page tag handling |
|---:|---|---|---|---|---|---|
| 1 | M2. Renal physiology compressed | Scope Lock / Tozer Ch.5 average renal blood flow anchor | Tozer also gives average renal blood flow as approximately `1.1 L/min`; this is the renal blood-flow ceiling for renal organ extraction, whereas GFR is the filtered subset of renal plasma water [T5 pp.127, 140]. | T5 pp.127, 140; Crucible physiologic anchor catalog | High-impact Scope key-equation/data-anchor coverage; 1-3 sentence/equation patch; no rejected material restored | Verified existing source range; no fabricated page tag |
| 2 | M8. App.D mass-balance | Scope Lock key equation Eq.D-8; Audit T1/M10 KPBC inverse | **Micro-patch — required App.D inversion** [TD pp.775–776 Eq D-8]<br><br>$$K_{PBC}=\frac{H-1+(C_b/C)}{f_u\cdot H}$$ | TD pp.775–776 Eq D-8; Audit Report T1 | High-impact Scope key-equation/data-anchor coverage; 1-3 sentence/equation patch; no rejected material restored | Verified existing source range; no fabricated page tag |
| 3 | M12. Core equations | Scope Lock key equation Eq.20-7 | **Micro-patch — required Eq.20-7** [T20 p.664 Eq 20-7]<br><br>$$\frac{k(m)}{k}=\frac{CL(m)/CL}{V(m)/V}$$ | T20 p.664 Eq 20-7; Scope Lock | High-impact Scope key-equation/data-anchor coverage; 1-3 sentence/equation patch; no rejected material restored | Verified existing source range; no fabricated page tag |


### B11. Mastery Augmentation Log

#### Candidate scan table

| Location | Type | Proposed augmentation | Source status | Risk | Decision |
|---|---|---|---|---|---|
| M1. Clearance proportionality + half-life is derived | W | In modeling work, treat half-life as a diagnostic summary, not as the primary covariate target. A covariate explanation should usually be framed on `CL` and/or `V` first, then translated back into `t_{1/2}` only after the mechanism is clear. | EXPERT_INFERENCE | Low | ADOPT |
| M2. Renal clearance decomposition: `CL_R`, `f_e`, filtration/secretion/reabsorption | F | Scaling total `CL` by renal function silently assumes the renal pathway is the whole clearance pathway. When `f_e` is credible, split renal and nonrenal components before applying a renal-function covariate. | EXPERT_INFERENCE | Low | ADOPT |
| M3. ARE plot vs Excretion Rate plot | J | A disagreement between ARE and excretion-rate plots is a data-process signal before it is a structural-model signal. Check collection intervals, midpoint assignment, bladder emptying, and urine pH/flow before adding compartments. | AUDIT_DERIVED | Low | ADOPT |
| M4. Well-stirred hepatic clearance + 4-model compression | M | `Q_H` is not just another covariate; it is the blood-flow ceiling for hepatic blood clearance. The low-extraction limit is the opposite regime, where `f_{ub}·CL_int` rather than flow is the bottleneck. | TEXTBOOK_DERIVED | Low | ADOPT |
| M5. High/low extraction + route × extraction × `f_u` matrix | F | A protein-binding conclusion is incomplete unless the report states route, extraction class, and whether total or unbound exposure is being interpreted. The common error is transferring an IV conclusion directly to oral dosing without checking first-pass behavior. | EXPERT_INFERENCE | Low | ADOPT |
| M6. IVIVE pitfalls: single-point, MMP, data condensation | W | An IVIVE review starts upstream of the hepatic equation. Once the in vitro concentration–rate relation has been collapsed into one fragile `CL_int`, a more elaborate liver model cannot recover the lost curvature. | TEXTBOOK_DERIVED | Low | ADOPT |
| M8. Plasma-to-blood ratio and blood clearance | J | Plasma clearance can be adequate for exposure summary, but organ extraction classification requires a blood-basis denominator. Before calling a drug high or low extraction, confirm whether `CL_b`, not plasma `CL`, was compared with organ blood flow. | TEXTBOOK_DERIVED | Low | ADOPT |
| M10. Extended clearance: transporter–enzyme architecture | F | A transporter or permeability bottleneck can masquerade as poor enzyme `CL_int` prediction. Before solving the discrepancy with an empirical scalar, check whether the well-stirred rapid-equilibration assumption is the weak link. | EXPERT_INFERENCE | Low | ADOPT |
| M11. Rate-limiting step in metabolite disposition | M | The terminal slope after parent dosing is a system-level terminal slope. Calling it the metabolite’s own half-life requires separate evidence that metabolite elimination, not formation, is the slow step. | TEXTBOOK_DERIVED | Low | ADOPT |
| M14. Renal impairment active-metabolite scenario + interconversion | R | A defensible renal-impairment argument should present parent and active-metabolite exposure together. Parent-only adjustment can be numerically clean but clinically incomplete when metabolite clearance is the collapsing pathway. | EXPERT_INFERENCE | Medium | ADOPT |


#### Inserted augmentation log

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
|---:|---|---|---|---|---|---|
| 1 | M1. Clearance proportionality + half-life is derived | W | YES | EXPERT_INFERENCE | Improves learner internalization / model judgment adjacent to the concept without adding new numeric or named external examples | Low |
| 2 | M2. Renal clearance decomposition: `CL_R`, `f_e`, filtration/secretion/reabsorption | F | YES | EXPERT_INFERENCE | Improves learner internalization / model judgment adjacent to the concept without adding new numeric or named external examples | Low |
| 3 | M3. ARE plot vs Excretion Rate plot | J | YES | AUDIT_DERIVED | Improves learner internalization / model judgment adjacent to the concept without adding new numeric or named external examples | Low |
| 4 | M4. Well-stirred hepatic clearance + 4-model compression | M | YES | TEXTBOOK_DERIVED | Improves learner internalization / model judgment adjacent to the concept without adding new numeric or named external examples | Low |
| 5 | M5. High/low extraction + route × extraction × `f_u` matrix | F | YES | EXPERT_INFERENCE | Improves learner internalization / model judgment adjacent to the concept without adding new numeric or named external examples | Low |
| 6 | M6. IVIVE pitfalls: single-point, MMP, data condensation | W | YES | TEXTBOOK_DERIVED | Improves learner internalization / model judgment adjacent to the concept without adding new numeric or named external examples | Low |
| 7 | M8. Plasma-to-blood ratio and blood clearance | J | YES | TEXTBOOK_DERIVED | Improves learner internalization / model judgment adjacent to the concept without adding new numeric or named external examples | Low |
| 8 | M10. Extended clearance: transporter–enzyme architecture | F | YES | EXPERT_INFERENCE | Improves learner internalization / model judgment adjacent to the concept without adding new numeric or named external examples | Low |
| 9 | M11. Rate-limiting step in metabolite disposition | M | YES | TEXTBOOK_DERIVED | Improves learner internalization / model judgment adjacent to the concept without adding new numeric or named external examples | Low |
| 10 | M14. Renal impairment active-metabolite scenario + interconversion | R | YES | EXPERT_INFERENCE | Improves learner internalization / model judgment adjacent to the concept without adding new numeric or named external examples | Medium |


#### Rejected candidate summary

| Rejected candidate | Reason for rejection |
|---|---|
| Additional numerical worked examples | Would introduce new numeric claims beyond Content Lock / PDF-verified anchors. |
| New named drug examples beyond those already present | Would require source verification and risk scope expansion. |
| Broad regulatory-reviewer narrative | Would compete with the canonical body and risk unsupported external claims. |
| Extra schematic ideas beyond approved 4C markers | Would violate Phase 4C figure budget and Phase 5 figure-control rules. |

### B12. Final Safety Checklist

- PART A alone is learner-facing and complete.
- PART A includes the spliced canonical body, approved figure markers, micro-patches, and bounded augmentations.
- Approved figure markers are present exactly once.
- No unapproved figure markers were added.
- Source page tags are preserved and micro-patch tags are PDF/Audit-verified.
- Audit and Crucible were not used as raw prose sources.
- Step 1 Draft v0 was not used as a learner-body source except through the Micro-Patch Gate.
- Rejected material was not restored.
- No HTML, Mermaid code, SVG code, or textbook image was generated in Phase 4D.

**END — 04_html_compile_input_master.md**

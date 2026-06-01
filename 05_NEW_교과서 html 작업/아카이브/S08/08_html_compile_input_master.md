# 08_HTML Compile Input Master

## Phase 4D Certification

| Certificate | Status | Basis |
| --- | --- | --- |
| Learner-Standalone Certificate | PASS | PART A starts with a learner navigation aid and contains the spliced learner body without audit tables or compiler-only appendix text |
| Zero-Omission Certificate | PASS | High-impact Scope/Audit/Crucible/PDF-required items are present, compressed by Content Lock, or protected by guardrails |
| Mastery-Uplift Certificate | PASS | Six bounded, source-labeled adjacent notes were inserted; no broad rewrite or new numerical/example content |
| Source-Boundary Certificate | PASS | All augmentations are labeled by epistemic status and do not masquerade as textbook claims |
| HTML-Readiness Certificate | PASS | PART B includes marker, figure, page-tag, navigation, MathJax, accordion, and regression-prevention requirements |

## Assembly Mode

**PATCH MODE.** `08_Content Lock v2.1.md` is a Figure Marker Patch Plan, so `08_Content Lock v2(1).md` was used as the base body and approved 4C markers were spliced by exact anchors. The requested output filename was adapted to `08_html_compile_input_master.md`.

## Input Manifest

| File | Role | Authority level | Used for | Notes |
| --- | --- | --- | --- | --- |
| 08_scope_lock(3).md | scope boundary | A0 | source ranges, learner, image rights, hard boundaries, required anchors | Used to constrain PART A and PART B |
| 08_G_비선형 PK MM·DDI 기전(4).pdf | PDF verification source | A1 | Gabrielsson mechanism pages and case-study grounding | Image rights=None; figures pointer-only |
| 08_T_비선형 PK MM·DDI 기전_01(4).pdf | PDF verification source | A1 | R&T Ch.16 nonlinearities verification | Image rights=None; figures pointer-only |
| 08_T_비선형 PK MM·DDI 기전_02(4).pdf | PDF verification source | A1 | R&T Ch.17 DDI verification | Image rights=None; figures pointer-only |
| 08_Audit_Report_v1(4).md | audit guardrail | A2 | MUST_FIX/SHOULD_FIX and regression prevention | Used as guardrail, not prose source |
| 08_Content Lock v2(1).md | canonical body | A3 | base learner body before figure-marker splice | §1 onward used; process logs excluded from PART A |
| 08_Content Lock v2.1.md | figure insertion source | A4 | approved Figure Strategy and PATCH MODE marker blocks | All KEEP markers spliced exactly once |
| 08_crucible_report_v1(1).md | crucible guardrail | A5 | preserved Grade A logic and mastery augmentation source | Used only after Audit/Content Lock constraints |
| 붙여넣은 마크다운(2)(57).md | compiler instruction | A7 | Phase 5 HTML rendering requirements | Essential requirements summarized in PART B |
| 08_step1_draft_v0(3).md | deprecated source | A6 | regression check only | Not copied into PART A |
| 08_Content_Lock_v1(4).md | locked reference | A3/Audit trail | historical Phase 4A reference | Not used as primary body |
| S08_phase1_patch memo(2).md | locked reference | A6/Audit trail | compression/readiness context | Not used as learner prose source |
| 붙여넣은 텍스트 (1)(86).txt | assembly instruction | A7/Task spec | Phase 4D output contract | Filename adapted from 05 to 08 by user request |

## PART A — Learner-Facing Complete Handout

## Learner Navigation Aid

**How to use this handout:** PART A is the learner-facing study body. Read §1 once for the mechanism triage map, then study C1–C6 in order, use the figure pointers as textbook look-up instructions, and finish with §5 confusion pairs plus §7 self-test.

**Learning route:**
1. Diagnose nonlinearity with superposition and dose-normalized exposure patterns.
2. Assign the likely mechanism: capacity, time, binding, DDI/transporter, or PD interaction.
3. Translate the mechanism into modeling, TDM, or DDI interpretation.
4. Check yourself with confusion pairs and the Boss Dilemma.

**Figure rights note:** textbook figures are not reproduced in this file. `FIGURE_POINTER` blocks are text-only instructions to consult the cited source figure; `FIGURE_SCHEMATIC` blocks are newly designed schematic briefs for Phase 5 rendering.

---

# §1. Session Header & Roadmap

<!-- MASTER LENS -->
이번 session의 한 문장 핵심은 다음이다. **비선형 PK는 “선형 superposition이 깨지는 현상”에 머무르지 않는다. capacity·time·flow·binding·interaction 중 어느 물리적 병목이 농도, 시간, route, 환자 genotype과 결합했는지를 식별하는 문제다.**

<!-- ANNOTATION -->
superposition(← dose-normalized profile이 겹치는 성질)은 여기서 진단 출발점일 뿐이다. Gabrielsson은 이 문제를 mechanism과 ODE로 보여주고, Rowland & Tozer Ch.16은 phenytoin·alcohol·ascorbic acid 같은 임상 dose-response 비대칭으로 보여준다. Ch.17은 그 비대칭이 drug interaction의 AUC ratio, induction time course, PM risk, route effect로 확장되는 방식을 보여준다. [G pp.112–114], [T16 pp.491–492], [T17 pp.531–532]

<!-- ANCHOR -->
읽는 순서는 진단 → capacity → time → binding → DDI → PD interaction이다. 먼저 dose-normalized plot으로 “선형이 아닌지”를 확인한다. 그 다음 $V_{max}/K_m$, enzyme turnover, $f_u$, $f_m$, route/extraction을 순서대로 점검한다.

<!-- ANNOTATION -->
$f_m$(← 해당 경로가 담당하는 제거 비율)은 DDI 예측에서 “막힌 경로가 전체 제거에서 얼마나 큰가”를 묻는 변수다. 이 순서를 어기면 nonlinear model을 fitting할 수는 있어도, 왜 parameter가 흔들리는지는 설명하지 못한다. [G p.113], [T16 p.492], [T17 pp.532–533]

## 1.1 지식 그래프 위치

| Layer | 질문 | 대표 mechanism | 실패 시그널 |
|---|---|---|---|
| Diagnostics | 농도/노출이 dose에 비례하는가? | superposition, AUC/Dose vs Dose | dose-normalized curve가 겹치지 않음 |
| Capacity | 병목이 capacity인가? | MM metabolism/transport, saturable first-pass | 작은 dose change가 큰 Css change를 만듦 |
| Time | parameter가 시간에 따라 바뀌는가? | enzyme turnover, induction, MBI | trough envelope drift, delayed toxicity/recovery |
| Binding | total concentration이 misleading한가? | saturable protein/tissue/target binding | total vs unbound profile이 서로 다른 결론 |
| DDI | 다른 약물이 CL/F/V/PD를 바꾸는가? | inhibition, induction, transporter, PD interaction | AUC ratio, route difference, PM amplification |

<!-- RECAP -->
**Recap:** 이 session은 “nonlinear PK = dose-proportionality failure”에서 멈추지 않는다. 최종 목표는 nonlinearity의 원인을 source mechanism으로 분해하고, 실험 설계·TDM 해석·PopPK model diagnosis·DDI risk prediction으로 번역하는 것이다.

---

<!-- FIGURE_SCHEMATIC -->
Title: Session 08 mechanism triage map
Mode: N
Visual objective: In 5 seconds, the learner should see that the session is a decision path, not a list of nonlinear PK facts.
Core message: Start with superposition failure, then triage the mechanism as capacity, time, binding, or DDI/PD interaction before translating it into PopPK/TDM/DDI decisions.
Elements to include: diagnostic entry node; dose-normalized plot trigger; mechanism branches for capacity, time, binding, and DDI/PD; downstream outputs for model diagnosis, TDM interpretation, and DDI prediction; sequence arrows.
Elements to exclude: textbook figure panels; numerical case values; source-page citations inside the schematic; regulatory label wording.
Suggested rendering: Mermaid
Caption: Session 08 is organized as a mechanism-triage workflow from superposition failure to pharmacometrics decisions.
Alt text: A flowchart starts with superposition failure and branches to capacity, time, binding, and interaction mechanisms, which then feed modeling, TDM, and DDI interpretation.
Source relation: Newly designed
<!-- /FIGURE_SCHEMATIC -->

# §2. Concept Anatomy Cards

## C1. Nonlinearity Diagnostics — superposition이 깨지는 순간부터 시작한다

<!-- MASTER LENS -->
**Big Idea:** 비선형성의 첫 진단은 “모델을 무엇으로 짤까?”가 아니다. 같은 route·formulation·method에서 dose-normalized concentration-time profile, AUC vs Dose, AUC/Dose vs Dose가 superimpose 되는지 확인하는 것이다. 선형이면 dose-normalized 관측값이 겹친다. 비선형이면 clearance, bioavailability, distribution, binding 중 적어도 하나가 dose 또는 time의 함수가 된다. [G pp.112–114], [T16 p.492]

### Core anatomy

- **Superposition principle:** linear PK에서는 dose를 두 배로 하면 concentration과 AUC도 두 배가 된다. [G pp.113–115], [T16 p.492]
- **Dose-normalized AUC pattern:** AUC/Dose가 dose와 함께 증가하면 CL 감소 또는 F 증가를 의심하고, 감소하면 CL 증가 또는 F 감소를 의심한다. [G p.113]
- **Time-dependent kinetics의 정의:** concentration이 변해서 parameter가 달라 보이는 것만으로는 time-dependence가 아니다. 실제 enzyme amount, transporter activity, perfusion 같은 physiological/biochemical state가 시간에 따라 변해야 한다. [G p.112], [T16 p.492]

### Practical reading rule

<!-- TRENCH -->
**Trench tip:** nonlinear PK 검토에서 첫 그림은 spaghetti concentration-time plot이 아니라 **dose-normalized concentration-time plot + AUC/Dose vs Dose**다. 이 두 그림 없이 바로 $V_{max}$/$K_m$를 fitting하면 안 된다. capacity limitation인지 F 변화인지, time-dependence인지, binding artifact인지 구분하지 못하기 때문이다. [G p.113]

### What changed from Draft v0

- M1의 도입부와 Table 2.15 재생산은 삭제했다.
- “carrier saturation 하나로 모든 비선형 PK를 설명한다”는 표현은 제거했다.
- Flow, binding, time, capacity는 “같은 비선형성”이 아니라 **서로 다른 원인으로 superposition failure를 만드는 네 축**으로 정렬했다. [G pp.112–114]

<!-- RECAP -->
**Recap:** C1의 목적은 비선형성을 선언하는 것이 아니라, 다음 질문을 강제하는 것이다. “AUC/Dose가 올라갔는가, 내려갔는가, 시간이 지나며 변했는가, total과 unbound가 다른 말을 하는가?”

---

> **Practice Lens — [CRUCIBLE_DERIVED]**  
> C1은 mechanism naming 전에 수행하는 triage 단계다. AUC/Dose 방향만으로 원인을 확정하지 말고, CL·F·distribution·time-dependence 중 어떤 parameter가 상수가 아니게 되었는지를 다음 카드에서 분리해 검증한다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner, p.113, Fig.2.85 and Fig.2.86
Why this matters: These figures are the fastest way to learn the visual grammar of nonlinearity diagnostics. Removing them would make AUC/Dose pattern recognition depend on memory rather than visual classification.
When to look: Before reading C1, then once again after C1 Recap.
Learner instruction: First inspect the direction of AUC/Dose change. Then map that direction to possible CL, F, or distribution changes before naming a mechanistic model.
<!-- /FIGURE_POINTER -->

## C2. Capacity-limited Michaelis–Menten Kinetics — $V_{max}$/$K_m$가 dose 조정의 비대칭성을 만든다

<!-- MASTER LENS -->
**Big Idea:** Michaelis–Menten capacity limitation은 clearance가 상수가 아니라 concentration의 함수가 되는 상황이다. 즉, 같은 drug라도 농도 영역이 바뀌면 apparent clearance와 t½ 해석이 달라진다. Gabrielsson의 MM clearance는 Eq.2:266–2:274 영역에 속한다. Eq.2:264는 linear superposition 식이므로 MM ODE의 citation으로 쓰지 않는다. [G pp.114–119]

### Core equations and source tags

$$Cl(C)=\frac{V_{max}}{K_m+C}$$  
[Equation family: G Eq.2:266; source tag: G p.115]

$$Rate=\frac{V_{max}\cdot C}{K_m+C}$$  
[G pp.115–116], [T16 p.494]

Bolus ODE는 $V_{max}$가 concentration/time 단위로 parameterized되면 $dC/dt=-V_{max}C/(K_m+C)$처럼 쓸 수 있지만, $V_{max}$가 amount/time 단위이면 volume scaling이 필요하다. 따라서 본문에서는 shorthand로만 사용하고, primary source tag는 Eq.2:266–2:274로 유지한다. [G pp.115–118]

### Two limiting cases

- **Low concentration:** $C\ll K_m$이면 $Cl\approx V_{max}/K_m$이고 first-order처럼 보인다. [G pp.115–117]
- **High concentration:** $C\gg K_m$이면 elimination rate가 $V_{max}$에 접근하고 apparent clearance는 감소한다. 이 영역에서는 small dose increase가 disproportionate AUC/Css increase를 만든다. [G pp.115–119], [T16 pp.500–506]

### Clinical anchors

1. **Phenytoin:** 300 mg/day에서 4 mg/L이던 환자가 500 mg/day로 증량 후 36 mg/L가 되었고, 67% dose increase가 9× concentration increase를 만들었다. 이는 phenytoin의 dose-dependent metabolism 때문이다. [T16 p.491]
2. **Phenytoin steady-state equation:**

$$C_{u,ss}=\frac{K_m\cdot R_0}{V_m-R_0}$$  
[T16 Eq.16-7; source tag: T16 p.503]

이 식의 핵심은 $R_0$가 $V_m$에 가까워질수록 denominator가 작아진다는 점이다. 따라서 $C_{u,ss}$는 선형적으로가 아니라 급격히 상승한다. $K_m$은 unbound concentration 기준이고, total concentration으로 작업할 때의 $K_m'$와 구분해야 한다. [T16 pp.503–506]

3. **Alcohol:** ethanol은 approximate $V_m\approx10$ g/hr, $K_m\approx100$ mg/L scale에서 zero-order plateau intuition을 제공한다. 같은 ethanol 사례는 capacity뿐 아니라 absorption/flow/time factor가 겹치므로 단일 MM 사례처럼 과단순화하지 않는다. [T16 pp.500–502], [G pp.139–141], [G pp.556–562]
4. **Ascorbic acid:** 75 mg/day에서 9 mg/L, 10,000 mg/day에서 약 19 mg/L로, 133-fold dose increase가 약 2-fold concentration increase만 만든다. 이유는 concentration 상승과 함께 renal clearance가 크게 증가하기 때문이다. [T16 p.492]

### Design and fitting implications

<!-- TRENCH -->
**Trench tip:** $V_{max}$와 $K_m$를 따로 추정하려면 농도 범위가 curvature를 지나야 한다. 특히 $K_m$ 주변 또는 그 이하의 관측값이 필요하다. high-concentration plateau만 있으면 $V_{max}$와 $K_m$가 ridge처럼 같이 움직인다. [G p.117]

<!-- TRENCH -->
**Trench tip:** PK18처럼 nonlinear fit을 시작하기 전에는 graphical method로 $V_{max}/K_m$, $V_c$, distribution terms의 initial estimate를 손산출해야 한다. nonlinear fitting은 initial estimate에 민감하므로, 손산출 30분이 model debugging을 크게 줄인다. [G pp.556–562]

### Critical caution

AUC 기반 bioavailability 계산은 clearance가 constant일 때만 안전하다. CL이 concentration-dependent이면 AUC 변화가 F 변화인지 CL 변화인지 분리되지 않으므로, “AUC가 늘었다 = F가 늘었다”로 결론 내리면 안 된다. [G p.116]

<!-- ANCHOR -->
C2는 Stage 3 DDI의 수학적 원형이다. $K_m+C$의 분모 구조를 이해해야 한다. 그렇지 않으면 inhibitor가 등장해 $1+C_{u,I}/K_I$ factor를 만드는 Eq.17-9–17-11도 새 식처럼 외우게 된다. [G pp.115–118], [T17 pp.550–552]

<!-- RECAP -->
**Recap:** MM kinetics의 핵심은 “포화되면 zero-order”가 아니다. 핵심은 **CL이 농도의 함수가 되어 dose 조정, AUC 해석, t½, steady-state 도달 시간이 모두 비선형화된다**는 점이다.

---

> **Failure Mode — [TEXTBOOK_DERIVED]**  
> MM kinetics를 “포화되면 zero-order”로만 기억하면 dose adjustment 판단이 무너진다. 실무 위험은 $R_0$ 또는 concentration이 capacity 근처로 접근할 때 small dose change가 large exposure change로 바뀌는 비대칭성이다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner, p.115, Fig.2.88; Rowland & Tozer, p.503, Fig.16-9; Rowland & Tozer, p.505, Fig.16-10
Why this matters: C2 depends on seeing the same denominator intuition in three forms: clearance decreases, rate plateaus, and clinical steady state becomes sharply sensitive near capacity.
When to look: After reading the C2 equations and before the C2 clinical anchors.
Learner instruction: Track what happens as concentration or dosing rate approaches capacity. Do not read the curves as simple proportional dose-response plots.
<!-- /FIGURE_POINTER -->

## C3. Time-dependent Turnover and Mechanism-Based Inhibition — 농도 시계와 enzyme 시계를 분리한다

<!-- MASTER LENS -->
**Big Idea:** Time-dependent kinetics는 concentration이 달라져서 clearance가 달라 보이는 현상이 아니다. enzyme/transporter/physiology 자체가 시간에 따라 변하는 현상이다. 따라서 약물 concentration time course와 enzyme turnover time course라는 두 개의 시계를 분리해서 읽어야 한다. [G p.112], [G pp.119–129], [T16 pp.516–519]

### Core turnover equation

$$\frac{dE}{dt}=R_{in}-k_{out}E$$  
$$E_{ss}=\frac{R_{in}}{k_{out}}$$  
[G Eq.2:275–2:278; source tag: G pp.120–121]

Enzyme level이 변하면 $Cl(t)$가 변한다. Induction은 enzyme amount 증가로 $V_{max}$ 또는 intrinsic clearance capacity를 올리고, de-induction이나 mechanism-based inhibition은 enzyme activity recovery를 $k_{out}$ clock에 묶는다. [G pp.120–128], [T17 pp.557–561]

### Autoinduction and heteroinduction anchors

- **PK22 autoinduction:** multiple-dose profile에서 $Vc$, $Vt$, $a$, $k_{12}$, $k_{21}$, $k_{out}$, $E_0$ 같은 parameter가 연결되며, trough sampling이 enzyme turnover 식별에 중요하다. [G pp.580–585]
- **Carbamazepine:** Tozer Ch.16의 autoinduction example은 반복투여 중 clearance가 시간에 따라 변하는 임상 anchor다. [T16 p.518]
- **Phenobarbital–dicumarol:** induction onset/offset이 즉시 일어나지 않고 수주 scale로 보이는 이유는 inducer/enzyme turnover clock 때문이다. [T17 pp.560–561]

### Mechanism-based inhibition as turnover destruction

MBI(mechanism-based inhibition)는 reversible inhibition과 달리 enzyme을 기능적으로 제거한다.

<!-- ANNOTATION -->
여기서 “제거”는 enzyme amount가 사라진다는 뜻만이 아니라, enzyme activity가 회복 전까지 유효하지 않다는 뜻이다. 회복은 inhibitor concentration이 사라지는 속도만이 아니라 enzyme resynthesis/degradation clock에 의해 제한된다. Clarithromycin example에서 $k_{inact}$, $k_E$, $C_{u,I}/K_I$가 결합해 reversible inhibition보다 훨씬 큰 effect를 만들 수 있으며, CYP3A4 회복에는 2주 또는 그 이상이 필요할 수 있다고 설명된다. [T16 p.519], [T17 pp.557–558]

<!-- ANCHOR -->
Eq.17-13/17-14의 MBI term은 C3 turnover ODE의 정상상태 사고방식을 DDI prediction에 붙인 것이다. Reversible inhibition은 “분모에 inhibitor competition을 더하는 문제”다. 반면 MBI는 “enzyme pool 자체를 줄인 뒤 회복 clock까지 계산하는 문제”다. [T17 p.558]

### Diagnostic signatures

- **Trough Envelope Drift:** 같은 dose인데 trough가 일정 방향으로 이동하면 IIV보다 time-varying CL을 먼저 의심한다. [G pp.126–129], [G pp.580–585]
- **Single-dose fit trap:** single-dose data만 잘 맞는 model이 multiple-dose에서 systematic over/underprediction을 보이면 autoinduction 또는 time-dependent inhibition을 의심한다. [G pp.580–585], [T16 pp.516–519]
- **Washout trap:** MBI에서는 perpetrator 중단 후 substrate exposure가 즉시 정상화된다고 가정하면 안 된다. [T17 pp.557–558]

<!-- TRENCH -->
**Trench tip:** Autoinduction study에서 dense single-dose sampling만 늘리는 것은 $k_{out}$ 식별에 충분하지 않을 수 있다. multiple-dose trough envelope가 enzyme clock을 더 직접적으로 보여준다. [G pp.580–585]

<!-- RECAP -->
**Recap:** C3의 핵심 질문은 “약물 농도가 낮아졌는가?”가 아니라 “enzyme pool이 회복되었는가?”다. 이 질문이 induction, autoinduction, MBI, withdrawal trap을 하나로 묶는다.

---

> **Mastery Note — [EXPERT_INFERENCE]**  
> C3를 읽을 때는 관측값이 concentration clock을 따라 회복되는지, enzyme pool clock을 따라 늦게 회복되는지를 먼저 묻는다. 이 한 질문이 reversible inhibition, induction, MBI, withdrawal trap을 구분하는 가장 빠른 mental check다.

<!-- FIGURE_SCHEMATIC -->
Title: Two clocks in nonlinear PK: concentration clock vs enzyme turnover clock
Mode: N
Visual objective: In 5 seconds, the learner should distinguish concentration-driven apparent CL change from true time-dependent enzyme-pool change.
Core message: Reversible inhibition mainly follows the perpetrator concentration clock, whereas induction and MBI require an enzyme turnover/recovery clock.
Elements to include: left lane for drug/perpetrator concentration clock; right lane for enzyme pool clock; nodes for reversible inhibition, induction, MBI, and recovery; arrows to observed signatures such as trough drift and delayed recovery.
Elements to exclude: numerical rate constants; case-specific parameter estimates; exact reproduction of textbook turnover diagrams.
Suggested rendering: Mermaid
Caption: Time-dependent kinetics requires a second clock: the enzyme or transporter pool changes more slowly than the plasma concentration profile.
Alt text: A two-lane diagram contrasts a drug concentration clock with an enzyme turnover clock and shows how reversible inhibition, induction, and MBI map to different recovery patterns.
Source relation: Newly designed
<!-- /FIGURE_SCHEMATIC -->

## C4. Binding, TMDD, and Displacement-only DDI — total concentration을 그대로 믿지 않는다

<!-- MASTER LENS -->
**Big Idea:** Nonlinear binding은 total concentration과 unbound concentration의 관계를 비선형화한다. 따라서 total concentration만으로 exposure나 effect를 판단하기 어렵다. 특히 open in vivo system과 closed in vitro binding experiment를 혼동하면, protein binding displacement를 실제 unbound exposure 변화로 과대해석하게 된다. [G pp.129–134], [T17 pp.538–544]

### Core binding equation

$$C_b=\frac{n\cdot P_t\cdot C_u}{K_d+C_u}$$  
[G Eq.2:294; source tag: G p.129]

Binding site가 saturable이면 total concentration이 크게 변해도 unbound concentration의 해석은 별도로 해야 한다. Low-extraction drug의 steady state에서는 unbound concentration이 input rate와 unbound clearance에 의해 지배되므로, displacement-only는 total concentration을 낮출 수 있어도 unbound steady-state exposure를 지속적으로 올리지 않는 경우가 많다. [G pp.129–134], [T17 pp.538–544]

### Open vs closed system

- **Closed in vitro system:** total amount가 고정되어 displacement가 곧 unbound fraction 증가처럼 보인다. [G pp.131–132]
- **Open in vivo system:** input, clearance, distribution이 함께 작동하므로 total concentration 변화가 곧 pharmacologic effect 변화는 아니다. [G pp.132–134]

<!-- ANNOTATION -->
closed/open의 차이는 “시험관 안의 총량 고정”과 “몸 안의 지속적 제거·재분포”의 차이다.

### TMDD and tissue/target binding

Target-mediated drug disposition은 high-affinity, low-capacity target/tissue binding이 disposition을 바꾸는 경우다. Tozer Ch.16은 small molecule에서도 bosentan, imirestat, trandolaprilat, draflazine, mitoxantrone 같은 prototype을 제시하지만, 본 단계에서는 TMDD full mechanistic code나 Mager–Jusko implementation으로 확장하지 않는다. [T16 pp.511–516]

### Displacement-only DDI downrank

Phenytoin–valproate는 total phenytoin이 낮아져도 unbound phenytoin은 상대적으로 유지되는 displacement-only prototype으로 제시된다. 이 사례의 가치는 “dose를 줄이라”가 아니라 “total concentration만 보고 toxicity/efficacy를 판단하지 말라”는 데 있다. [T17 p.543]

Warfarin–phenylbutazone은 단순 displacement만이 아니라 inhibition까지 겹친 multifaceted example로 다루어야 한다. [T17 p.563]

<!-- TRENCH -->
**Trench tip:** Protein binding nonlinearity가 의심되는 Phase 1/PopPK package에서는 total concentration만 모으지 말고 dose level별 $f_u$를 측정하라. total-only dataset은 binding nonlinearity와 clearance nonlinearity를 서로 구분하기 어렵게 만든다. [G pp.129–134], [T16 pp.511–516]

<!-- RECAP -->
**Recap:** C4는 “protein binding이 변하면 위험하다”가 아니라, **total과 unbound가 서로 다른 질문에 답한다**는 원칙을 고정한다.

---

> **Practice Lens — [TEXTBOOK_DERIVED]**  
> Binding 문제에서는 total concentration 변화가 곧 pharmacologic exposure 변화라는 가정을 보류한다. 먼저 unbound concentration, system boundary(open vs closed), 그리고 unbound clearance가 함께 변했는지를 확인한다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner, p.132, Fig.2.104; Gabrielsson & Weiner, p.133, Fig.2.105
Why this matters: The C4 confusion hinges on system boundaries. Removing these figures would let the learner transfer closed-system binding intuition into open-system in vivo interpretation.
When to look: After reading the C4 Open vs closed system subsection.
Learner instruction: Compare which quantities are fixed and which can leave the system. Then re-read the displacement-only warning with those boundaries in mind.
<!-- /FIGURE_POINTER -->

## C5. Quantitative DDI Prediction — $f_m$, inhibitor strength, route가 AUC ratio를 만든다

<!-- MASTER LENS -->
**Big Idea:** Ch.17의 DDI 정량 framework는 “상호작용이 있다/없다”를 묻지 않는다. affected drug의 clearance 중 얼마가 inhibited pathway에 의존하는지($f_m$), inhibitor exposure가 $K_I$에 비해 얼마나 큰지, route/first-pass가 얼마나 관여하는지를 묻는다. [T17 pp.531–532], [T17 pp.546–552]

### Reversible competitive inhibition spine

Eq.17-9–17-12는 inhibited pathway의 clearance 감소와 whole-body AUC ratio를 연결한다. 즉, 한 pathway의 억제가 전체 exposure를 얼마나 바꾸는지 계산하는 spine이다. 핵심 직관은 다음이다. [T17 pp.550–552]

$$\text{AUC ratio}\approx\frac{1}{\frac{f_m}{1+C_{u,I}/K_I}+(1-f_m)}$$

이 식은 textbook source로 유지하되, “FDA DDI Guidance 핵심식”이라고 직접 부르지 않는다. FDA guidance 연결은 첨부 source에 없으므로 본 문서에서는 삭제한다. [T17 pp.550–552]

### Clinical anchors

- **Theophylline–enoxacin:** t½가 8.8→22 h, Css가 4→9 mg/L로 증가하며, graded inhibition의 primary clinical example로 쓰인다. [T17 pp.546–547]
- **Desipramine–quinidine/fluoxetine:** CYP2D6 pathway 의존성이 클수록 inhibitor impact가 커진다. [T17 pp.549–552]
- **Diltiazem–lovastatin / fluconazole–midazolam:** oral interaction이 IV interaction보다 클 수 있다. gut wall/first-pass component가 있으면 route별 AUC ratio가 달라진다. [T17 pp.553–554]

### PM × inhibitor amplification

Eq.17-18은 polymorphic pathway와 nonpolymorphic residual pathway가 동시에 고려될 때 maximum exposure ratio가 커질 수 있음을 보여준다. PM 환자에서 남은 nonpolymorphic pathway까지 strong inhibitor가 막으면 exposure ratio가 크게 뛸 수 있다. [T17 pp.558–559]

Fig.17-15의 omeprazole–clarithromycin example은 high ratio 사례로 유지하되, Draft v0의 “33×”는 exact printed number가 아니라 시각 추정/확인필요로 취급한다. 따라서 본문에서는 “매우 큰 exposure ratio example”로만 사용한다. [T17 p.559]

### Sequence and withdrawal

Interaction은 all-or-none이 아니라 concentration, timing, sequence, initiation/withdrawal에 따라 graded하게 나타난다. 따라서 inhibitor를 추가할 때와 제거할 때의 위험은 대칭이 아니다. induction/MBI에서는 특히 회복 지연이 critical하다. [T17 pp.532–534], [T17 pp.557–561]

<!-- TRENCH -->
**Trench tip:** DDI 예측표에는 최소한 $f_m$ uncertainty band를 붙여라. $f_m$가 0.5인지 0.8인지에 따라 같은 inhibitor라도 AUC ratio 해석이 완전히 달라진다. [T17 pp.550–552]

<!-- RECAP -->
**Recap:** C5의 핵심은 inhibitor 이름이 아니라 **affected drug의 pathway dependence**다. $C_{u,I}/K_I$가 커도 $f_m$가 작으면 whole-body AUC ratio는 제한되고, $f_m$가 크면 작은 inhibitor effect도 임상적으로 커진다.

---

> **Judgment Lens — [CRUCIBLE_DERIVED]**  
> DDI prediction에서 $f_m$은 “inhibitor strength가 임상적으로 증폭될 수 있는 구조적 취약성”이다. 같은 inhibitor라도 victim drug이 해당 pathway에 얼마나 의존하는지에 따라 AUC ratio의 의미가 달라진다.

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer, p.550, Fig.17-8
Why this matters: The AUC-ratio equation is easy to copy but hard to feel. This figure shows why fm controls whether a given inhibitor produces a small or large exposure change.
When to look: Immediately after the C5 reversible competitive inhibition equation.
Learner instruction: Read the figure by holding inhibitor strength constant and moving fm. Then hold fm constant and vary inhibitor strength.
<!-- /FIGURE_POINTER -->

## C6. Multifaceted/Transporter and PD Interactions — 하나의 perpetrator가 하나의 mechanism만 갖는다고 가정하지 않는다

<!-- MASTER LENS -->
**Big Idea:** 실제 DDI는 metabolic inhibition 하나로 끝나지 않는다. Transporter inhibition, altered distribution, gut/hepatic first-pass, induction, PD additivity/synergy/antagonism이 겹칠 수 있다. 이 때문에 같은 drug라도 acute/chronic, oral/IV 조건에서 반대 방향 effect를 보일 수 있다. [T17 pp.563–567]

### Core multifaceted anchors

1. **Digoxin–quinidine:** quinidine은 digoxin의 clearance, volume/distribution, bioavailability에 복합적으로 영향을 주는 example로 제시된다. [T17 p.564]
2. **Atorvastatin–rifampin acute IV:** acute rifampin은 OATP1B1 inhibition 성격으로 atorvastatin Cmax 10×, AUC 7×, t½ 8→3 h 같은 pattern을 보인다. Draft v0의 $V_d/F$ 17×, $CL/F$ 9×는 직접 source 수치처럼 쓰지 않는다. [T17 p.565]
3. **Fluconazole–midazolam / Diltiazem–lovastatin:** oral vs IV 차이는 gut wall/first-pass contribution을 분리하는 실험적 단서다. [T17 pp.553–554]

### Acute/chronic × oral/IV diagnostic matrix

Rifampin 같은 perpetrator는 acute transporter inhibition과 chronic enzyme induction이 서로 반대 방향 effect를 만들 수 있다. 따라서 실무적으로는 acute IV, acute oral, chronic IV, chronic oral을 구분해 mechanism을 생각해야 한다. 이 문장은 label language가 아니다. 교과서 사례에서 도출한 diagnostic framework다. [T17 pp.560–565]

### PD interaction layer

Gabrielsson Ch.3.6은 competitive antagonism, noncompetitive antagonism, empirical two-drug model, enantiomer interaction을 receptor/response model로 다룬다. Tozer Ch.17은 두 full agonist가 같은 receptor에서 ceiling effect를 보일 수 있고, isobologram으로 additivity/synergy/antagonism을 구분할 수 있음을 보여준다. [G pp.224–227], [T17 pp.567–570]

Greco Eq.17-22는 advanced response surface reference로만 유지하고, 본 session의 master card로 독립 확장하지 않는다. [T17 p.569]

<!-- TRENCH -->
**Trench tip:** DDI case를 검토할 때 “AUC가 증가했다”로 끝내지 말고, 함께 움직인 Cmax, t½, V/F, oral/IV ratio를 보라. 예를 들어 AUC↑와 t½↓가 같이 나오면 단순 metabolic inhibition만으로 설명하기 어렵다. distribution/transporter mechanism을 의심해야 한다. [T17 pp.563–565]

<!-- RECAP -->
**Recap:** C6는 단일 mechanism model의 과신을 막는다. 같은 DDI pair라도 route, timing, chronicity에 따라 전혀 다른 mechanism signature가 나타난다.

---

> **Failure Mode — [TEXTBOOK_DERIVED]**  
> Multifaceted DDI를 한 mechanism으로 축약하면 AUC, Cmax, t½가 서로 다른 방향으로 움직이는 signature를 놓친다. C6에서는 단일 지표가 아니라 지표들의 조합과 투여 timing을 함께 읽는다.

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer, p.565, Fig.17-19
Why this matters: This source plot shows the signature that text alone tends to flatten: AUC and Cmax can rise while half-life falls. Removing it would encourage overcalling the case as simple metabolic inhibition.
When to look: After reading the C6 core multifaceted anchors.
Learner instruction: Inspect AUC, Cmax, and half-life together. The key lesson is the joint pattern, not any single metric.
<!-- /FIGURE_POINTER -->

# §5. Confusion Pair Dissection

## CP1. Dose-dependent capacity vs true time-dependent kinetics

<!-- CONFUSION -->
- **Wrong shortcut:** “CL이 시간에 따라 변했으니 time-dependent kinetics다.”
- **Correction:** MM kinetics에서는 concentration이 시간에 따라 떨어지므로 apparent CL도 함께 변한다. 그러나 enzyme amount나 physiology가 실제로 변하지 않으면 true time-dependence가 아니다. [G p.112], [G pp.115–119]
- **Test:** 같은 concentration에서 시간이 달라도 CL이 달라지는가? 그렇다면 time-dependent mechanism을 의심한다.

## CP2. Autoinduction vs ordinary multiple-dose accumulation

<!-- CONFUSION -->
- **Wrong shortcut:** 반복투여 중 trough가 변하면 accumulation 때문이다.
- **Correction:** accumulation은 linear parameter로도 예측 가능하지만, autoinduction은 enzyme turnover 때문에 trough envelope가 시간이 지나며 구조적으로 이동한다. [G pp.126–129], [G pp.580–585]
- **Test:** single-dose fit이 multiple-dose trough를 systematic하게 벗어나면 $k_{out}$-linked enzyme compartment를 고려한다.

## CP3. Capacity-limited elimination vs flow/first-pass effect

<!-- CONFUSION -->
- **Wrong shortcut:** AUC/Dose가 증가하면 무조건 hepatic enzyme saturation이다.
- **Correction:** AUC/Dose 증가는 CL 감소 또는 F 증가 모두에서 발생한다. First-pass saturation, solubility limitation, flow effect도 같은 방향의 AUC pattern을 만들 수 있다. [G p.113], [T16 pp.496–500]
- **Test:** IV/oral crossover 또는 bioavailability 변화 evidence를 확인한다.

## CP4. Open in vivo binding vs closed in vitro binding

<!-- CONFUSION -->
- **Wrong shortcut:** displacement가 있으면 unbound concentration이 지속적으로 오른다.
- **Correction:** open system에서는 input과 unbound clearance가 unbound steady state를 결정한다. total concentration 변화만으로 dose adjustment를 결정하지 않는다. [G pp.129–134], [T17 pp.538–544]
- **Test:** total과 unbound concentration을 같이 보고, low/high extraction context를 분리한다.

## CP5. Displacement-only DDI vs inhibition DDI

<!-- CONFUSION -->
- **Wrong shortcut:** phenytoin total concentration이 내려가면 efficacy가 낮아졌다.
- **Correction:** valproate displacement example에서는 total phenytoin이 낮아져도 unbound concentration은 유지될 수 있다. 반대로 warfarin–phenylbutazone은 displacement와 inhibition이 겹쳐 단순 displacement로 설명하면 안 된다. [T17 p.543], [T17 p.563]
- **Test:** unbound concentration과 clearance/time-course를 함께 확인한다.

## CP6. Reversible inhibition vs MBI

<!-- CONFUSION -->
- **Wrong shortcut:** inhibitor를 중단하면 interaction은 inhibitor half-life만큼 사라진다.
- **Correction:** reversible inhibition은 inhibitor concentration이 줄면 빠르게 회복될 수 있지만, MBI는 enzyme pool recovery가 필요하다. Clarithromycin-like MBI는 회복 시간이 enzyme resynthesis에 묶인다. [T17 pp.557–558]
- **Test:** single-dose vs multiple-dose perpetrator exposure에서 affected drug PK 변화가 질적으로 달라지는지 본다.

## CP7. Inhibition vs induction, and rifampin acute vs chronic switch

<!-- CONFUSION -->
- **Wrong shortcut:** rifampin은 inducer이므로 substrate exposure를 낮춘다.
- **Correction:** chronic rifampin induction은 exposure를 낮출 수 있지만, acute rifampin은 transporter inhibition으로 exposure를 올릴 수 있다. Timing과 route를 분리해야 한다. [T17 pp.560–565]
- **Test:** acute/chronic × oral/IV matrix로 예상 방향을 따로 적는다.

## CP8. PK DDI vs PD DDI

<!-- CONFUSION -->
- **Wrong shortcut:** response가 변하면 concentration이 변했을 것이다.
- **Correction:** PD interaction은 concentration-time profile이 크게 변하지 않아도 response가 additive, synergistic, antagonistic하게 변할 수 있다. [G pp.224–227], [T17 pp.567–570]
- **Test:** unbound concentration-response relationship을 같이 확인한다.

<!-- RECAP -->
**Recap:** Confusion pair의 공통 원인은 “관측값 하나로 mechanism 하나를 단정하는 습관”이다. total concentration, AUC, t½, route, timing, response를 함께 읽어야 한다.

---

# §7. Self-Test: Active Recall Module

## Q1. [회상]
<!-- SELF-TEST -->
비선형성 진단에서 dose-normalized concentration-time plot과 AUC/Dose vs Dose plot을 먼저 그리는 이유는 무엇인가?  
**Answer:** 선형이면 dose-normalized 관측값이 superimpose된다. 겹치지 않으면 CL, F, V/distribution, binding, time-dependent process 중 하나가 dose/time의 함수라는 신호다. 즉, 이 그림은 “어떤 parameter가 상수가 아니게 되었는가?”를 묻는 첫 필터다. [G pp.112–114], [T16 p.492]

## Q2. [적용]
<!-- SELF-TEST -->
AUC/Dose가 dose와 함께 증가한다. 가능한 두 가지 mechanism은?  
**Answer:** clearance 감소 또는 bioavailability 증가. capacity-limited elimination뿐 아니라 first-pass saturation도 가능하므로 IV/oral evidence가 필요하다. [G p.113], [T16 pp.499–506]

## Q3. [회상]
<!-- SELF-TEST -->
왜 Eq.2:264를 MM ODE citation으로 쓰면 안 되는가?  
**Answer:** Eq.2:264는 linear superposition 식이다. MM clearance/rate/bolus/infusion/input 식은 Eq.2:266–2:274 영역에 있다. [G pp.114–118]

## Q4. [적용]
<!-- SELF-TEST -->
Phenytoin 300 mg/day에서 4 mg/L, 500 mg/day에서 36 mg/L가 된 이유를 Eq.16-7의 denominator 관점에서 설명하라.  
**Answer:** $C_{u,ss}=K_mR_0/(V_m-R_0)$에서 dosing rate $R_0$가 $V_m$에 가까워질수록 denominator가 작아져 concentration이 비선형적으로 증가한다. [T16 pp.491, 503]

## Q5. [적용]
<!-- SELF-TEST -->
Ascorbic acid는 133-fold dose increase에도 concentration이 약 2-fold만 증가했다. phenytoin과 반대 방향의 비선형성이 생긴 이유는?  
**Answer:** 농도 상승과 함께 renal clearance가 증가하는 saturable reabsorption/renal escape-valve 성격 때문이다. [T16 p.492], [T16 pp.507–510]

## Q6. [회상]
<!-- SELF-TEST -->
MM model에서 $V_{max}$와 $K_m$를 따로 추정하려면 어떤 concentration range가 필요한가?  
**Answer:** curvature를 포함하고, 특히 $K_m$ 주변 또는 그 이하의 concentration이 필요하다. high concentration plateau만으로는 $V_{max}$/$K_m$ ridge가 생긴다. [G p.117]

## Q7. [적용]
<!-- SELF-TEST -->
반복투여 중 trough가 계속 낮아지고 single-dose model은 잘 맞는다. 어떤 mechanism을 먼저 의심해야 하는가?  
**Answer:** autoinduction 또는 time-dependent increase in clearance. enzyme turnover compartment와 $k_{out}$ 식별 가능성을 확인한다. [G pp.126–129], [G pp.580–585]

## Q8. [적용]
<!-- SELF-TEST -->
Clarithromycin 병용 후 midazolam exposure가 multiple dosing에서 더 커지고 회복도 느리다. reversible inhibition과 어떻게 다른가?  
**Answer:** mechanism-based inhibition은 enzyme activity를 제거하므로, 회복은 inhibitor 농도 소실뿐 아니라 enzyme resynthesis/degradation clock에 묶인다. [T17 pp.557–558]

## Q9. [적용]
<!-- SELF-TEST -->
Valproate 병용 후 total phenytoin은 낮아졌지만 unbound phenytoin은 유지된다. dose를 줄여야 하는가?  
**Answer:** displacement-only에서는 total concentration이 misleading할 수 있다. unbound concentration과 clinical response를 기준으로 판단해야 하며, total 감소만으로 dose 감량하면 안 된다. [T17 p.543]

## Q10. [계산 직관]
<!-- SELF-TEST -->
Affected drug의 $f_m$가 0.8이고 inhibitor가 해당 pathway를 강하게 억제한다. 왜 $f_m$가 0.3인 drug보다 AUC ratio가 훨씬 커지는가?  
**Answer:** Eq.17-11에서 inhibited pathway term $f_m/(1+C_{u,I}/K_I)$가 작아져도 residual $(1-f_m)$가 exposure ratio의 바닥을 정한다. $f_m=0.8$이면 남은 pathway가 0.2뿐이라 ratio가 크게 뛴다. [T17 pp.550–552]

## Q11. [적용]
<!-- SELF-TEST -->
Oral midazolam interaction이 IV midazolam interaction보다 크다. 어떤 mechanism을 시사하는가?  
**Answer:** gut wall/first-pass metabolism component가 크다는 뜻이다. route별 AUC ratio 차이는 hepatic clearance만으로 설명하면 안 된다. [T17 pp.553–554]

## Q12. [회상]
<!-- SELF-TEST -->
Eq.17-18의 PM × inhibitor risk가 큰 이유는?  
**Answer:** polymorphic pathway가 이미 결손된 PM에서 남은 nonpolymorphic pathway가 inhibitor에 의해 막히면 residual clearance가 매우 작아질 수 있기 때문이다. [T17 pp.558–559]

## Q13. [적용]
<!-- SELF-TEST -->
Rifampin 병용에서 acute IV study는 AUC 증가, chronic oral 병용은 AUC 감소를 보일 수 있다. 왜 모순이 아닌가?  
**Answer:** acute rifampin은 transporter inhibition, chronic rifampin은 enzyme induction이 지배할 수 있다. timing과 route가 mechanism을 바꾼다. [T17 pp.560–565]

## Q14. [적용]
<!-- SELF-TEST -->
Response는 크게 변했지만 unbound concentration-time profile은 거의 변하지 않았다. 무엇을 의심해야 하는가?  
**Answer:** PK DDI보다 PD interaction을 의심한다. receptor-level additivity, synergy, antagonism 또는 Emax ceiling을 검토한다. [G pp.224–227], [T17 pp.567–570]

## Q15. [Boss Dilemma]
<!-- SELF-TEST -->
Sponsor가 “inhibitor 병용 시 AUC가 증가하니 label에 일괄 dose reduction을 쓰자”고 한다. 10분 안에 mechanism-based 검토 순서를 말하라.  
**Answer:** (1) affected drug의 $f_m$와 inhibited pathway 확인, (2) $C_{u,I}/K_I$와 reversible vs MBI 구분, (3) oral/IV route effect 확인, (4) PM 또는 residual pathway risk 확인, (5) acute/chronic perpetrator effect와 withdrawal sequence 확인, (6) transporter/multifaceted signature 확인. 단, 본 문서에서는 label language가 아니라 textbook-based mechanism checklist로만 둔다. [T17 pp.546–565]

<!-- RECAP -->
**Recap:** Self-test는 식 암기가 아니라 mechanism triage를 묻는다. 각 답은 “어떤 parameter가 상수가 아니게 되었는가?”로 되돌아가야 한다.

---

# §8. Meta-Frame & Big Picture

## 8.1 One-page memory model

<!-- MASTER LENS -->
Session 08의 기억 모델은 다음 여섯 문장으로 고정한다. 이 여섯 문장은 세부식을 외우기 전, mechanism triage 순서를 유지하기 위한 압축본이다.

1. **Nonlinearity는 superposition failure로 발견한다.** [G pp.112–114], [T16 p.492]
2. **Capacity limitation은 $CL(C)$를 만들고, $R_0\to V_m$에서 steady-state가 발산한다.** [G pp.115–119], [T16 pp.500–506]
3. **Time-dependence는 enzyme/transporter/physiology의 clock이 drug concentration clock과 분리될 때 생긴다.** [G pp.119–129], [T16 pp.516–519]
4. **Binding은 total concentration을 속이고, open system에서는 unbound exposure가 mass balance를 따른다.** [G pp.129–134], [T17 pp.538–544]
5. **DDI prediction은 $f_m$, inhibitor strength, route, PM/residual pathway, induction/MBI recovery를 함께 본다.** [T17 pp.546–561]
6. **Multifaceted DDI와 PD interaction은 “AUC 하나”로 mechanism을 단정하지 못하게 만든다.** [T17 pp.563–570]

## 8.2 Dependencies for later pharmacometrics work

- **PopPK model building:** nonlinear CL, time-varying CL, binding nonlinearity, transporter DDI를 구분하지 못하면 parameter variability가 mechanism error를 가린다.
- **TDM:** phenytoin-like capacity limitation에서는 small dose change가 큰 concentration change를 만들고, total-only monitoring은 displacement/binding 상황에서 misleading하다. [T16 pp.491–506], [T17 p.543]
- **DDI study interpretation:** reversible inhibition, MBI, induction, transporter effect, route effect를 분리하지 못하면 initiation/withdrawal recommendation이 잘못된다. [T17 pp.546–565]
- **Drug–metabolite modeling:** parent-metabolite 동시 관측만으로 metabolite disposition이 충분히 식별된다고 가정하지 않는다. 이 항목은 source-backed identifiability caution으로만 유지하며, regulatory deficiency language는 쓰지 않는다. [G pp.135–139]

## 8.3 Deleted or quarantined material

| Material | Final action |
|---|---|
| FDA DDI Guidance direct claim | 삭제. Textbook Eq.17-11/17-18로만 표기. |
| NDA Section 12.3 dose reduction wording | 삭제. 필요 시 후속 규제 source가 있을 때 별도 audit. |
| CPIC/ethnicity PM frequency | 삭제. 첨부 source 없음. |
| Mager–Jusko/TMDD NONMEM code | 삭제. Conceptual TMDD만 유지. |
| Full NONMEM code blocks | 삭제. equation-to-model implication sentence만 유지. |
| Greco Eq.17-22 full expansion | 1줄 reference로 축소. |
| Exercise-only study problem tables | 삭제. |

## 8.4 Compression check

Step 1 Draft v0의 20개 이상 full card 구조를 6개 Master Card, 8개 Confusion Pair, 15개 Self-Test로 압축했다. Source page tags는 MUST cards, equations, key examples에서 유지했고, 병합된 항목에는 범위형 page tag를 부여했다. [p.확인 필요]가 필요한 항목은 삭제하지 않고 “시각 추정/확인필요”로 처리했다.

<!-- RECAP -->
**Final recap:** 이 Content Lock v2의 최종 spine은 “diagnose nonlinearity → identify capacity/time/binding mechanism → translate to DDI prediction → avoid route/timing/unbound/PM traps”이다. 이 spine만 PhD 1년차가 확실히 체화하면, 비선형 PK와 DDI chapter의 대부분은 암기가 아니라 mechanism triage로 회수된다.


## PART B — Compiler-Only Appendix

This appendix is not learner-facing. It exists only to protect Phase 5 rendering fidelity.

### B1. Compilation Contract

- PART A is the only learner-facing body.
- Phase 5 must render PART A without altering content.
- PART B is instruction/guardrail only and must not be rendered as learner content unless explicitly requested.
- Do not restore deprecated material, add new scientific content, add new page tags, or modify equations/source tags.
- Do not generate HTML in Phase 4D; Phase 5 alone generates the single self-contained HTML.

### B2. Figure Rendering Instructions

- Preserve approved Figure Strategy decisions from `08_Content Lock v2.1.md`.
- Approved KEEP markers in PART A: #1, #2, #4, #6, #8, #10, #12.
- Rejected figures are not restored.
- Image rights = None. Do not embed copyrighted textbook images.
- Render `FIGURE_POINTER` as a text-only textbook-reference callout showing Source, Why this matters, When to look, and Learner instruction.
- Render `FIGURE_SCHEMATIC` as a newly designed schematic based only on the marker brief. Do not reproduce textbook layout, palette, or label placement.
- Do not propose or add new figures in Phase 5.

### B3. Page Tag Rendering Rules

- Preserve all existing source tags and page tags, including `[p.XX]`, `[pp.XX–YY]`, `[pp.XX, YY]`, and `[p.확인 필요]` if present.
- Render visible source page tags in HTML using `<span class="source-page">...</span>`.
- Render `[p.확인 필요]` as `<span class="source-page source-uncertain">[p.확인 필요]</span>`.
- Do not fabricate, delete, renumber, or relocate page tags.
- Do not apply page-tag regex inside code blocks or inside `FIGURE_*` marker blocks.
- Source page tags must remain visible in print mode.

### B4. HTML Compiler Requirements

- Render content; do not alter it.
- Output one self-contained HTML file with inline custom CSS and JS.
- Permitted external runtime dependencies only: MathJax CDN, Mermaid CDN, and permitted CDN libraries such as highlight.js.
- MathJax: support inline `\(...\)` and display `\[...\]` math while preserving existing dollar-delimited equations if the compiler normalizes them safely.
- Code blocks: dark `<pre><code>` style with copy buttons.
- Self-test blocks: render `<!-- SELF-TEST -->` as click-to-reveal accordions; answers hidden by default.
- Controls: print/PDF button via `window.print()` and checklist/session state persistence if checklists are rendered.
- Responsive: mobile single-column/collapsed navigation; desktop two-column with sticky left sidebar.
- Dark/light: respect `prefers-color-scheme`.
- Print: hide navigation, avoid broken cards, and keep source page tags visible.

#### Marker-to-component mapping

| Marker / Pattern | HTML Component | Rendering rule |
|---|---|---|
| `<!-- MASTER LENS -->` | Callout box | border-left gold; subtle background |
| `<!-- ANNOTATION -->` | Annotation/tooltip-style note | muted italic style |
| `<!-- ANCHOR -->` | Bridge sentence | muted italic style |
| `<!-- TRENCH -->` | Practical tip box | rose-accented practical callout |
| `<!-- CONFUSION -->` | Confusion comparison | amber comparison box |
| `<!-- SELF-TEST -->` | Accordion | question visible, answer hidden until click |
| `<!-- RECAP -->` | Section recap | blue-accented summary box |
| `<!-- FIGURE_POINTER -->` | Textbook pointer callout | text-only; no image embedding |
| `<!-- FIGURE_SCHEMATIC -->` | Schematic figure | Mermaid/inline SVG/CSS only as appropriate |
| `[확인 필요]` | Highlight flag | visible mark/highlight |

#### Navigation anchor integrity rules

- HTML must include a sticky left sidebar table of contents.
- Use `<a href="#...">` links only.
- Every sidebar target must have exactly one matching body id.
- Every major section heading (§1, §2, §5, §7, §8) must receive a stable id.
- Every §2 concept card heading must receive a stable id.
- Do not create duplicate ids or TOC links whose target id does not exist.
- Enable smooth scrolling with `html { scroll-behavior: smooth; }`.
- Before finalizing HTML, count all sidebar `href="#id"` values, confirm each id exists exactly once, and fix any mismatch.

#### Mermaid/schematic self-check

- Mermaid blocks must start with a valid directive such as `flowchart TD`, `flowchart LR`, `graph TD`, or `graph LR`.
- Node IDs must use only `[A-Za-z0-9_]`.
- Labels with Korean text, parentheses, slashes, symbols, or spaces must be quoted.
- Edge labels with special characters must use quoted edge-label syntax.
- If Mermaid cannot be made robust, use inline SVG or CSS cards.
- Do not emit a Mermaid block likely to fail rendering.

### B5. Audit Guardrails

Regression-prevention items:

- Do not restore the unsupported direct claim that textbook Eq.17-11/Eq.17-18 are FDA Guidance equations unless an external guidance source is separately supplied and audited.
- Do not restore NDA Section 12.3, contraindication, or dose-reduction label wording as source-backed textbook content.
- Do not restore CPIC, ethnicity, Korean/Asian/White poor-metabolizer frequency claims.
- Do not restore Mager-Jusko TMDD code, quasi-equilibrium TMDD implementation, or full NONMEM code blocks.
- Do not reduce all nonlinear PK to a single “carrier saturation” geometry.
- Do not restore unsupported exact values such as omeprazole-clarithromycin observed maximum ratio = 33 unless separately verified and labeled.
- Do not restore unapproved figure embedding or any copyrighted textbook image.
- Keep Eq.2:264 as linear superposition, not MM ODE; MM belongs to Eq.2:266–2:274 family.

### B6. Crucible Guardrails

- Crucible is not a raw content source at this stage.
- Preserve only already-adopted or explicitly allowed Grade A logic.
- Do not reintroduce omitted or rejected Crucible items.
- Do not convert expert interpretation into textbook-derived fact.
- Expert additions must remain labeled as `EXPERT_INFERENCE` if not directly textbook-derived.

### B7. Deprecated and Forbidden Restorations

- Step 1 Draft v0 is deprecated.
- Do not copy Step 1 prose into the learner body except through a formally logged micro-patch.
- Do not restore rejected overclaims, unsupported numerical values, unsupported regulatory claims, source-unsupported examples, unapproved code, or unapproved figures.
- Do not use Audit/Crucible as broad rewrite sources.

### B8. PATCH MODE Splice Verification Table

| Marker # | Anchor text | Anchor found? | Match count | Inserted? | Final location (§ + card) |
| --- | --- | --- | --- | --- | --- |
| 1 | `## 1.1 지식 그래프 위치` | YES | 1 | YES | §1.1 지식 그래프 위치 |
| 2 | `## C1. Nonlinearity Diagnostics — superposition이 깨지는 순간부터 시작한다` | YES | 1 | YES | §2 C1. Nonlinearity Diagnostics |
| 4 | `## C2. Capacity-limited Michaelis–Menten Kinetics — $V_{max}$/$K_m$가 dose 조정의 비대칭성을 만든다` | YES | 1 | YES | §2 C2. Capacity-limited Michaelis–Menten Kinetics |
| 6 | `## C3. Time-dependent Turnover and Mechanism-Based Inhibition — 농도 시계와 enzyme 시계를 분리한다` | YES | 1 | YES | §2 C3. Time-dependent Turnover and MBI |
| 8 | `## C4. Binding, TMDD, and Displacement-only DDI — total concentration을 그대로 믿지 않는다` | YES | 1 | YES | §2 C4. Binding, TMDD, and Displacement-only DDI |
| 10 | `## C5. Quantitative DDI Prediction — $f_m$, inhibitor strength, route가 AUC ratio를 만든다` | YES | 1 | YES | §2 C5. Quantitative DDI Prediction |
| 12 | `## C6. Multifaceted/Transporter and PD Interactions — 하나의 perpetrator가 하나의 mechanism만 갖는다고 가정하지 않는다` | YES | 1 | YES | §2 C6. Multifaceted/Transporter and PD Interactions |

### B9. Zero-Omission Coverage Matrix

| Domain | Required item | Evidence in PART A | Status | Action |
| --- | --- | --- | --- | --- |
| C1 Scope concepts | Nonlinearity diagnostics, superposition, AUC/Dose vs Dose | §2 C1 and §7 Q1–Q3 | PRESENT | No action |
| C1 Scope concepts | Capacity-limited MM, CL(C), two limits, phenytoin/alcohol/ascorbic acid anchors | §2 C2 and §7 Q4–Q6 | PRESENT | No action |
| C1 Scope concepts | Time-dependent turnover, auto/heteroinduction, MBI, recovery clock | §2 C3 and §5 CP1–CP2/CP6–CP7 | PRESENT | No action |
| C1 Scope concepts | Binding, TMDD, open vs closed system, displacement-only DDI caution | §2 C4 and §5 CP4–CP5 | PRESENT | No action |
| C1 Scope concepts | Quantitative DDI prediction: reversible inhibition, fm, route, PM amplification, induction/withdrawal | §2 C5 and §7 Q10–Q12/Q15 | PRESENT | No action |
| C1 Scope concepts | Multifaceted/transporter and PD interactions | §2 C6, §5 CP7–CP8, §7 Q13–Q14 | PRESENT | No action |
| C1 Scope concepts | Flow-dependent kinetics, ethanol integrated case, nonlinear parent-metabolite model | §2 C2 clinical anchors; §8.2 Dependencies | PRESENT_COMPRESSED | Compressed by Content Lock; no micro-patch needed |
| C2 Required data anchors | Phenytoin 67% dose increase → 9× concentration; Eq.16-7; alcohol and ascorbic acid anchors | §2 C2 Clinical anchors | PRESENT | No action |
| C2 Required data anchors | Theophylline-enoxacin, desipramine-quinidine/fluoxetine, MBI, diltiazem-lovastatin, fluconazole-midazolam, rifampin, digoxin-quinidine and related Ch.17 anchors | §2 C5–C6; §7 Q10–Q15; §8.1 | PRESENT_COMPRESSED | Kept only at locked handout density |
| C3 Audit MUST_FIX/SHOULD_FIX | Wrong Eq.2:264 MM citation correction | §2 C2 and §7 Q3 | PRESENT | No action |
| C3 Audit MUST_FIX/SHOULD_FIX | Remove unsupported FDA Guidance/NDA/CPIC/code/TMDD overclaims | §8.3 plus PART B B5–B7 | PRESENT | Forbidden restoration guardrails included |
| C4 Audit T5 findings | High-impact omissions and examples checked against compressed Content Lock structure | §2 C1–C6, §5, §7, §8 | PRESENT_COMPRESSED | No unresolved HIGH item identified in Phase 4D assembly |
| C5 Figure coverage | Approved KEEP markers #1/#2/#4/#6/#8/#10/#12 | PART A figure marker blocks | PRESENT | All markers spliced exactly once; rejected figures not restored |
| C6 Page/source tags | Existing source tags and [확인 필요] policy preserved; no fabricated new page tags | PART A source tags; PART B B3 | PRESENT | No page-tag micro-patch made |
| C7 Crucible Grade A preservation | Mechanism-triad, two clocks, fm vulnerability, reviewer-style mechanism checklist | §1, §2 C3/C5, §7 Q15, augmentation notes | PRESENT | Labeled augmentations used only where bounded |
| C8 Deprecated draft regression | Unsupported overclaims, external examples, code blocks, unapproved figures not restored | §8.3 and PART B B5–B7 | PRESENT | Regression guardrails preserved |
| C9 Canonical body integrity | Content Lock v2 §1 onward preserved with approved markers plus labeled augmentations | PART A | PRESENT | No canonical scientific rewrite performed |

### B10. Micro-Patch Log

No micro-patches needed. PART A equals exact-spliced Content Lock v2.1 except the Learner Navigation Aid and approved Mastery Augmentation Layer.

### B11. Mastery Augmentation Log

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | §2 C1 | J/W | YES | CRUCIBLE_DERIVED | Converts diagnostic plot reading into mechanism-triage workflow | Low |
| 2 | §2 C2 | F | YES | TEXTBOOK_DERIVED | Prevents reduction of MM to zero-order slogan and emphasizes dose-adjustment asymmetry | Low |
| 3 | §2 C3 | M/J | YES | EXPERT_INFERENCE | Short mental check for concentration clock vs enzyme pool clock | Medium; labeled |
| 4 | §2 C4 | J | YES | TEXTBOOK_DERIVED | Prevents total-only exposure interpretation in binding/displacement contexts | Low |
| 5 | §2 C5 | J/R | YES | CRUCIBLE_DERIVED | Frames fm as DDI vulnerability without adding external thresholds | Low |
| 6 | §2 C6 | F | YES | TEXTBOOK_DERIVED | Prevents single-mechanism overcall when PK metrics move discordantly | Low |

#### Rejected augmentation candidates

| Rejected candidate | Reason for rejection |
| --- | --- |
| New regulatory label wording for DDI dose adjustment | Rejected: would restore NDA/FDA-style external claim without attached regulatory source |
| New named examples beyond PDFs | Rejected: would violate source-boundary and no-new-example rule |
| Additional numerical thresholds for strong/moderate inhibitors beyond locked content | Rejected: would require external verification or broader rewrite |


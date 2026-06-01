# 12_Content Lock v2
## Session 12 · Effect Compartment · Tolerance/Rebound · Transduction

**Output status:** Content Lock v2 — Phase 4B 문장 가독성 polish + 최소 annotation 통합본  
**Language rule:** Korean prose; English for technical terms, equations, NONMEM/general implementation labels, drug names  
**Figure rule:** Phase 4C로 이월. 본 문서에는 FIGURE marker를 삽입하지 않음.

---

## 0. Updated Source Detection & Scope Lock

- **Primary source:** Gabrielsson & Weiner 5e, Ch.3 §3.9 Effect Compartment Models [G&W pp.261–272], §3.11 Tolerance and Rebound Models [G&W pp.284–302], §3.13 Transduction Models [G&W pp.323–325], Case Studies PD13/PD20/PD21/PD35 [G&W pp.805–809, 836–848, 910–914].
- **Secondary source:** Rowland & Tozer 5e, Ch.8 Response [R&T pp.233–264].
- **Scope exclusion retained:** §3.10 Dose-Response-Time Models, §3.12 Receptor Occupancy Theory, §3.14 Synergistic Effects. These remain out of scope.
- **Phase 4A correction basis:** Audit MUST_FIX items are treated as binding. Crucible Grade A items are adopted if source-grounded and compressed.

---

## 0A. Updated Curation Map

### MUST

| # | Concept | Why it earns space |
|---|---|---|
| 1 | **Effect Compartment / Link Model / $k_{e0}$** | Core model for distributional delay <!-- ANNOTATION -->(← plasma와 biophase 사이 지연) between plasma and biophase; requires rise-and-fall response data because $C_e$ is inferred, not measured [G&W pp.262–265]. |
| 2 | **Hysteresis direction <!-- ANNOTATION -->(← 상승·하강 경로가 달라지는 현상) and mechanism triage** | Clockwise/counterclockwise loops are the first diagnostic clue for time delay, but not a stand-alone model-selection rule [R&T pp.234–246; G&W pp.262, 296]. |
| 3 | **Tolerance/Rebound via Moderator <!-- ANNOTATION -->(← 지연된 반조절 상태변수) $M$** | Negative feedback ODEs explain overshoot, tolerance, rebound, and PD13 repeated-infusion carry-over [G&W pp.297–300, 805–809]. |
| 4 | **Transduction <!-- ANNOTATION -->(← 신호가 관찰반응으로 전달되는 과정) / Transit Chain** | Sequential response compartments explain long sigmoidal onset delays that ordinary indirect response cannot mimic, as in PD35 [G&W pp.323–325, 910–914]. |

### CONTEXT — absorbed into MUST cards

- **Table 3.10 link-model pitfall** → Card 1 and Confusion Pair 1. This is **not PD13**; it is G&W §3.9.7 Table 3.10, with Fig.3.59 described as PD12 data [G&W p.271].
- **PD20** → numeric anchor for effect-compartment fitting and single-dose precision limitation [G&W pp.836–839].
- **PD21** → comparison anchor for $k_{e0}$, $k_{out}$, and $k_{off}$, which share units but not meaning [G&W pp.840–846].
- **Colburn-Eldon attenuation, antagonistic metabolite, tolerance compartment, pool/precursor** → one-sentence alternatives under Card 3 [G&W pp.287–295, 807–808].
- **R&T clinical examples** → digoxin/naproxen/warfarin/succinylcholine used only as diagnostic anchors, not as separate expanded mini-chapters [R&T pp.234–256].

---

## 0B. Adjudication Table Summary

| Source | Item | Verdict | Rationale |
|---|---|---|---|
| Audit | Scope: G&W §3.9/§3.11/§3.13 + PD13/20/21/35; R&T Ch.8 | ADOPT | Scope matches session role and prevents §3.10/§3.12/§3.14 creep. |
| Audit | Effect compartment definition, $C_e$ not measured, rise/fall data required | ADOPT | Directly grounded in G&W pp.262–263 and central to Card 1. |
| Audit | Same $t_{max}$ with increasing doses | PARTIAL_ADOPT | Retain as useful discriminatory tool, but only under **linear PK** and not as a deterministic rule [G&W p.264]. |
| Audit | One-compartment equations Eq.3:126–3:134 | ADOPT | Core derivation retained with page tags [G&W pp.264–265]. |
| Audit | $k_{1e}=k_{e0}$ as physical/mandatory equality | ADOPT as correction | Rewrite as identifiability-based simplifying assumption; remove mass-conservation overclaim [G&W pp.263, 265]. |
| Audit | $K_p=1$ and partitioning caveat | ADOPT | Needed to prevent overinterpreting plasma-scale EC50 as true biophase affinity [G&W pp.263, 265–266]. |
| Audit | Table 3.9 values | ADOPT | Keep correct values and separate examples [G&W p.269]. |
| Audit | Succinylcholine vs d-tubocurarine/vecuronium mix | ADOPT as correction | G&W 4-min $t_{1/2,k_{e0}}$ belongs to d-tubocurarine/vecuronium; succinylcholine remains R&T dose-duration example [R&T pp.249–256]. |
| Audit | G&W §3.9.7 Table 3.10 mislabeled as PD13 | ADOPT as correction | Replace all “PD13 EC50 분기” references with “G&W §3.9.7 Table 3.10 link-model pitfall / PD12 data” [G&W p.271]. |
| Audit | NDA/FDA/ICH/Deficiency Letter narrative | PARTIAL_ADOPT | Remove specific outcome narrative; retain only labeled [교과서 외 실무 해석] where useful. |
| Audit | NONMEM SAEM/bootstrap/SIR/MU-referencing details | REJECT | Implementation detail is not source-grounded and not needed for 10-minute handout. |
| Audit | Hysteresis direction determines model | ADOPT as correction | Direction is the first diagnostic clue; final model choice requires $t_{max}$, repeated-dose pattern, metabolite/target information, and model comparison. |
| Audit | PD13 Model II superiority | ADOPT | PD13 is retained only for repeated IV infusion tolerance/rebound model comparison [G&W pp.805–809]. |
| Audit | PD35 n=3 “optimal” wording | PARTIAL_ADOPT | State n=3 as practical sufficiency; n=4 has slightly lower WRSS, n=5 worsens [G&W p.914]. |
| Audit | Transduction Bode/PFR/RC/do-loop analogies | PARTIAL_ADOPT | Compress to one labeled structural analogy; avoid treating engineering metaphors as textbook content. |
| Audit | §3.10/§3.12/§3.14 insertion | REJECT | Scope creep; excluded by Scope Lock. |
| Crucible | Wall 1: $k_{e0}$/$k_{out}$/$k_{off}$ same units but different referents | ADOPT | High-yield PD21 insight and directly useful for confusion prevention [G&W p.846]. |
| Crucible | Wall 2: $t_{max}$ test requires linear PK | ADOPT | Critical missing assumption explicitly stated in G&W p.264. |
| Crucible | Wall 3: negative-feedback sign intuition | PARTIAL_ADOPT | Retain as qualitative homeostasis logic; omit Jacobian/trace/determinant details. |
| Crucible | Wall 4: PD35 n selection as information-capacity ceiling | ADOPT | Converts Table 35.1 from rote model selection into epistemic boundary [G&W p.914]. |
| Crucible | Escalation cascade: direct → link → turnover → tolerance → transduction | PARTIAL_ADOPT | Keep as model-triage roadmap, without NDA workflow expansion. |
| Crucible | GOF signature catalog | PARTIAL_ADOPT | Keep four named diagnostic patterns as learning aids; label implementation layer where relevant. |
| Crucible | Sparse sampling fake figure-eight tip | ADOPT | Useful trench-level warning for hysteresis interpretation. |
| Crucible | PD21 identifiability warning | ADOPT | Strong support from model-comparison case [G&W pp.840–846]. |
| Crucible | Q10 regulatory scenario expansion | REJECT | Overlong and outside textbook; compress to mechanism-validity principle only. |
| Crucible | Grade C items: scope creep, added case studies, NONMEM syntax expansion | REJECT | They fail the 10-minute PhD handout criterion. |

---

# §1 — Session Header & Roadmap

**Source:** Gabrielsson & Weiner 5e + Rowland & Tozer 5e  
**Chapter range:** G&W Ch.3 §3.9/§3.11/§3.13 + PD13/20/21/35; R&T Ch.8  
**Core task:** classify time delay between concentration and response into distributional delay, system adaptation, or transduction cascade.

<!-- MASTER LENS -->
**Big Idea:** Plasma concentration and response can separate in time for different mechanistic reasons. 전문가의 첫 판단은 단순히 “delay term을 하나 붙이는 것”이 아니다. 먼저 그 지연이 **drug distribution** ($k_{e0}$), **system turnover/adaptation** ($k_{out}$/$k_{tol}$), 또는 **downstream signal propagation** ($n \times \tau$) 중 어디에 속하는지 정해야 한다.

### Concept roadmap

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

<!-- ANCHOR -->
The chapter sequence itself is the escalation logic. §3.9는 “distributional delay인가?”를 묻고, §3.11은 “system이 적응하고 있는가?”를 묻는다. §3.13은 “measured response가 downstream cascade 뒤에 나타나는가?”를 묻는다.

<!-- ANNOTATION --> 따라서 같은 time delay라도 숨은 state가 다르면 모델도 달라진다. 이 세션의 핵심은 delay의 크기가 아니라 **무엇이 delayed state인지**를 명명하는 것이다.

---

# §2 — Concept Anatomy Cards

---

## Card 1 — Effect Compartment Model & $k_{e0}$ [Apex]

<!-- MASTER LENS -->
### Big Idea

Effect Compartment Model은 **distributional delay**를 다루는 표준 link model이다. Plasma concentration $C$가 관찰되지 않는 biophase concentration $C_e$를 움직이고, $C_e$가 response를 움직인다. 가장 강한 실무적 시그니처는 **same response $t_{max}$ across increasing doses**이지만, 이 판단은 PK가 linear일 때만 유효하다 [G&W p.264].

### A. Formal definition

The effect compartment is a hypothetical first-order distribution link between plasma and biophase <!-- ANNOTATION -->(← 약물이 작용하는 효과 부위). $C_e$는 직접 측정되지 않는다. 따라서 response-time data로부터 역추정해야 하며, rising phase와 falling phase 정보가 모두 필요하므로 steady-state data alone are insufficient [G&W p.263].

### B. Core equations

Plasma amount after one-compartment IV bolus:

$$A_p = D e^{-Kt} \quad \text{[G&W p.264, Eq.3:126]}$$

Effect-compartment amount:

$$\frac{dA_e}{dt}=k_{1e}A_p-k_{e0}A_e \quad \text{[G&W p.264, Eq.3:127]}$$

Integrated amount:

$$A_e=\frac{k_{1e}D}{k_{e0}-K}\left(e^{-Kt}-e^{-k_{e0}t}\right) \quad \text{[G&W p.264, Eq.3:128]}$$

표준 simplifying assumption인 $k_{1e}=k_{e0}$와 no partitioning simplification ($K_p=1$)을 적용하면, biophase concentration은 다음과 같이 정리된다:

$$C_e=\frac{k_{e0}D}{V_c(k_{e0}-K)}\left(e^{-Kt}-e^{-k_{e0}t}\right) \quad \text{[G&W p.265, Eq.3:134]}$$

<!-- ANNOTATION --> 닫힌형 식은 bolus 상황에서 직관을 준다. 실제 fitting에서는 같은 의미를 더 일반적으로 표현하는 ODE form이 중요하다.

Equivalent ODE form:

$$\frac{dC_e}{dt}=k_{e0}(C-C_e) \quad \text{[G&W pp.268–269, Eq.3:143]}$$

이 ODE form은 flexible하다. 왜냐하면 driving plasma concentration $C(t)$를 linear PK, nonlinear PK, 또는 table function으로 넣을 수 있기 때문이다 [G&W p.269; PD21 pp.840–841].

### C. Critical assumptions and boundaries

| Assumption | Keep | Boundary if violated |
|---|---|---|
| $C_e$ is inferred from response-time data | Yes | No rise/fall response data → $k_{e0}$ and PD shape cannot be separated [G&W p.263]. |
| Linear PK for $t_{max}$ test | Yes | Nonlinear PK can create apparent peak shift; first confirm exposure proportionality before using $t_{max}$ as model discriminator [G&W p.264]. |
| $k_{1e}=k_{e0}$ | Yes, corrected | This is an identifiability-based simplifying assumption, not a universal physical equality [G&W pp.263, 265]. |
| $K_p=1$ | Use only as simplification | If partitioning exists, $C_e$ and $C$ may differ even at steady state; estimated EC50 is a plasma-scale surrogate [G&W pp.263, 265–266]. |
| Response tracks $C_e$ instantaneously | Conditional | If system turnover or downstream cascade dominates, move to indirect response/tolerance/transduction. |

<!-- TRENCH -->
**Trench-Level Tip:** Do not run the $t_{max}$ dose-invariance test before checking PK linearity. G&W states the same-$t_{max}$ property under the condition “assuming the drug kinetics is linear” [G&W p.264].

### D. Corrected numeric anchors

- **G&W Table 3.9:** response equilibration half-lives include terbutaline FEV-1 7.5 min, theophylline FEV-1 11 min, d-tubocurarine/vecuronium muscle paralysis 4 min, fentanyl spectral edge 6.4 min, and QT-quinidine 8 min [G&W p.269].
- **R&T succinylcholine is separate:** succinylcholine is a dose-duration example: 0.5 mg/kg IV, $T_{50}\approx6$ min, $k\approx0.2\ \text{min}^{-1}$, and 80–20% response decline at about 22%/min [R&T pp.249–256]. It should not be labeled as G&W Table 3.9 $t_{1/2,k_{e0}}=4$ min.
- **PD20:** analgesic IV bolus example uses D=45 µg/kg, V=1 L/kg, K=0.50 h⁻¹, with initial estimates Emax≈3–5, EC50≈1.5 µg/L, $k_{e0}\approx0.1$ h⁻¹; G&W notes low EC50 precision because the dataset contained only one dose [G&W pp.836–839].

### E. Plausible fallacy — Link model fitted to turnover data

The major pitfall is not PD13. It is **G&W §3.9.7 Table 3.10**이다. 여기서는 turnover-generated data를 effect-compartment model로 fit한다. 그 결과 dose-stratified fits가 biologically implausible한 EC50/Emax/n 변화를 만든다: dose 1 EC50=0.681, dose 10 EC50=4.85, dose 100 EC50=0.941; the approximately sevenfold EC50 spread is a source-derived calculation [G&W p.271]. Fig.3.59 is described as using PD12 data, not PD13.

**Diagnostic name:** EC50 dose-bifurcation pattern. If dose-stratified fits imply that receptor sensitivity or capacity changes by dose without a mechanistic reason, the Link model is likely absorbing turnover/adaptation misspecification [G&W pp.271–272].

### F. $k_{e0}$ vs $k_{out}$ vs $k_{off}$

PD21 shows why equal units do not imply equal meaning. $k_{e0}=0.025$, $k_{out}=0.031$, and $k_{off}=0.018\ \text{min}^{-1}$ can be numerically similar, yet they refer to different clocks: biophase equilibration, system turnover, and receptor dissociation [G&W p.846]. 따라서 single-dose time course만으로는 여러 mechanism이 비슷하게 fit될 수 있다. Mechanism discrimination에는 additional doses나 washout behavior 같은 richer design이 필요하다 [G&W pp.840–846].

<!-- RECAP -->
Effect compartment is a distributional-delay model. Use it when $C_e$ plausibly lags behind $C$, the $t_{max}$ pattern is compatible under linear PK, and dose-stratified PD parameters remain biologically coherent.

---

## Card 2 — Hysteresis Direction and Mechanism Triage

<!-- MASTER LENS -->
### Big Idea

Hysteresis direction은 **first diagnostic clue**이지 final verdict가 아니다. Counterclockwise loops는 대개 response가 concentration보다 늦는다는 뜻이다. Clockwise loops는 tolerance, antagonism, 또는 adaptation을 시사한다. 그러나 final model choice에는 추가 근거가 필요하다 [R&T pp.234–246; G&W pp.295–296].

### A. Definition

Hysteresis means that response follows a different path when concentration rises than when concentration falls. R&T는 이를 digoxin과 naproxen으로 보여준다. Digoxin에서는 IV dosing 후 첫 4시간 동안 plasma concentration이 감소하는 동안 cardiac effect가 증가한다. Naproxen에서는 oral 500 mg 투여 후 pain relief에서 counterclockwise hysteresis가 나타난다 [R&T pp.234–235].

### B. Diagnostic matrix

| Direction | First interpretation | Mechanisms to test | Required follow-up |
|---|---|---|---|
| Counterclockwise | Response lags concentration | Distributional delay, indirect response, slow receptor binding, concordant metabolite | $t_{max}$ dose pattern, rise/fall response, metabolite/target data, model comparison |
| Clockwise | Response weakens earlier than concentration | Tolerance/desensitization, antagonistic metabolite, receptor down-regulation | repeated-dose pattern, rebound, metabolite pharmacology, recovery kinetics |
| Figure-eight / mixed | Competing time scales | Distribution delay + tolerance, sparse sampling artifact, multiple mechanisms | denser sampling and mechanism-informed design before committing to one model |

### C. R&T clinical anchors

- **Digoxin:** effect rises while plasma falls during 0–4 h after IV dose; distribution to cardiac tissue and target binding are slow [R&T p.234].
- **Naproxen:** oral 500 mg produces counterclockwise hysteresis; effect-compartment transformation can collapse the loop into a clearer concentration-response relationship [R&T pp.235, 245–246].
- **Warfarin:** delayed prothrombin complex response reflects system turnover rather than simple tissue distribution [R&T pp.242–248].
- **Succinylcholine:** response duration follows dose-duration logic; useful for decline/duration teaching but not the same as G&W Table 3.9 effect-compartment half-life [R&T pp.249–256].

<!-- TRENCH -->
**Trench-Level Tip:** Sparse sampling can manufacture a fake figure-eight. Before interpreting direction, confirm that sampling density captures both concentration rise/fall and response rise/fall; otherwise the loop geometry is a plotting artifact, not a mechanism.

### D. Structural interpretation

Clockwise/counterclockwise direction describes the phase-plane trajectory of time-paired concentration and response. The direction narrows the model family, but it does not distinguish distribution delay from turnover delay by itself. The decisive question is: **what state variable is delayed — drug at the biophase, the physiological response system, or a downstream cascade?**

<!-- RECAP -->
Hysteresis is the map, not the destination. Read the arrow first, then prove the mechanism with dose, timing, and model behavior.

---

## Card 3 — Tolerance/Rebound via Moderator $M$

<!-- MASTER LENS -->
### Big Idea

Tolerance와 rebound는 서로 무관한 두 현상이 아니다. Moderator model에서 $M$은 response를 뒤따라 형성되는 delayed counter-regulatory state이다. Dosing 중에는 $M$이 response를 줄인다. Dosing이 중단된 뒤에는 $M$이 남아 baseline 너머의 rebound를 만들 수 있다 [G&W pp.297–300].

### A. Formal definition

Tolerance is progressive response reduction during exposure; rebound is response excursion after withdrawal. G&W lists multiple tolerance mechanisms, including receptor down-regulation/internalization, transduction changes, cofactor depletion, mRNA/protein effects, antibodies, and enzyme induction [G&W pp.284–286].

### B. Moderator ODEs

Core negative-feedback model:

$$\frac{dR}{dt}=k_{in}S(C)-k_{out}M \quad \text{[G&W p.299, Eq.3:193]}$$

$$\frac{dM}{dt}=k_{tol}R-k_{tol}M \quad \text{[G&W p.299, Eq.3:194]}$$

At baseline, $S(C)=1$ and $R_0=k_{in}/k_{out}$ [G&W pp.299–300]. At steady state for the simple form, $R=M$ because $dM/dt=0$ implies $k_{tol}(R-M)=0$ when $k_{tol}\neq0$.

The more general “moderator + level of response” form introduces a nonlinear $M$ effect and produces a second-order steady-state solution [G&W pp.301–302, Eq.3:205–3:216]. The key handout point is not the algebraic expansion but the consequence: feedback strength changes the response level and recovery behavior.

### C. PD13 anchor — repeated infusion tolerance/rebound

PD13 is the proper repeated IV infusion case study. 이 사례는 ordinary turnover, negative-feedback moderator, and pool/precursor structures를 비교한다 [G&W pp.805–809]. 가장 잘 맞는 것은 Model II, 즉 moderator model이다: kin=30, kout=2.9, ktol=4.2, EC50=350, n=7.4, AIC=−97.5, WRSS=0.083 [G&W p.808].

The key interpretation is **trough drift/carry-over**이다. Repeated infusion에서는 moderator state가 완전히 돌아오지 않았기 때문에 second trough가 first trough로 단순히 reset되지 않는다. 이 때문에 tolerance를 보려면 single-dose data보다 repeated-dose data가 훨씬 더 정보적이다 [G&W p.808].

<!-- TRENCH -->
**Trench-Level Tip:** If the second-dose trough differs from the first-dose trough under similar exposure, suspect a hidden moderator state. Direct response or pure link models do not naturally carry that memory.

### D. Alternative tolerance/rebound structures — compressed context

- **Time-dependent attenuation:** empirical smoothing of potency/capacity over time; useful but weakly mechanistic and poor for rebound [G&W pp.291–292].
- **Antagonistic metabolite:** can explain antagonism but does not by itself cover rebound without added structure [G&W pp.292–293].
- **Tolerance compartment / counteracting mechanisms:** alternative state-variable formulations for adaptive systems [G&W pp.293–295].
- **Pool/precursor model:** tested in PD13 but inferior to moderator Model II for this dataset [G&W pp.807–808].

### E. Why the sign matters

Moderator $M$은 $R$을 따라가지만, response equation에서는 counteracting term으로 나타난다. 이 negative-feedback sign 때문에 system은 self-amplifying이 아니라 homeostatic하게 작동한다. 여기서 필요한 mechanistic memory는 한 줄이다: **drug pushes R, R builds M, M pushes back**.

<!-- RECAP -->
Tolerance/rebound is the pharmacodynamic memory problem. If the system remembers prior exposure, add a state that remembers.

---

## Card 4 — Transduction Model / Transit Chain

<!-- MASTER LENS -->
### Big Idea

Transduction models는 receptor activation과 observed functional response 사이의 chain을 표현한다. Response onset이 immediate exponential이 아니라 delayed sigmoid이면, single turnover compartment는 너무 얕을 수 있다. 이때 sequential transit compartments가 필요하다 [G&W pp.323–325].

### A. Formal definition

A transduction model uses a chain of compartments or events between receptor-ligand coupling and observed response. 각 transit step은 characteristic transit time $\tau$와 corresponding fractional turnover rate $k_{out}=1/\tau$를 가진다 [G&W pp.323–325].

### B. Core equations

Receptor-driving step:

$$\frac{dR_e}{dt}=\frac{1}{\tau}\left(E_0S(C)-R_e\right) \quad \text{[G&W p.911, Eq.35:5]}$$

Sequential transit compartments:

$$\frac{dR_i}{dt}=\frac{1}{\tau}(R_{i-1}-R_i),\quad i=1,2,\ldots,n \quad \text{[G&W p.911, Eq.35:6]}$$

Observed response is the final downstream state, $R_{obs}=R_n$.

<!-- ANNOTATION --> 여기서 지연되는 것은 약물의 이동이 아니라 response signal의 전달이다. 따라서 Link model의 “drug reaches site” 질문과 Transduction model의 “signal reaches measurement” 질문은 다르다.

### C. PD35 anchor — onset delay and n selection

PD35 involves a human male volunteer and three dose levels: baseline low dose C0=1.05 nmol/L, then 4× and 16× dose levels. K=0.0228 h⁻¹, corresponding to a half-life of about 30 h [G&W pp.910–914]. Ordinary indirect response could not adequately mimic the 15–20 h onset delay. 따라서 response를 설명하려면 transduction chain이 필요했다 [G&W p.323, pp.910–914].

Table 35.1 gives the model-comparison sequence [G&W p.914]:

| Transduction steps | EC50 | Emax | $\tau$ (h) | E0 | WRSS |
|---:|---:|---:|---:|---:|---:|
| 1 | 0.33 | 7.2 | 20 | 15 | 1319 |
| 2 | 0.34 | 6.0 | 13 | 18 | 789 |
| 3 | 0.35 | 5.4 | 9.8 | 19 | 642 |
| 4 | 0.35 | 5.1 | 7.8 | 20 | 632 |
| 5 | 0.34 | 4.8 | 6.4 | 20 | 682 |

n=3은 **mechanistic truth**가 아니라 **practical sufficiency**로 이해해야 한다. n=4는 WRSS를 약간 더 낮추지만, n=5에서는 오히려 악화된다. 이 패턴은 실제 biological signaling step 수가 아니라 dataset의 information-capacity ceiling을 보여준다.

<!-- TRENCH -->
**Trench-Level Tip:** Do not choose n by “lowest WRSS” alone. In PD35, 1319→789→642→632→682 says: the model needs more than one step, n=3 is practically enough, and the data cannot resolve exact cascade depth.

### D. Structural intuition

A single first-order delay begins moving immediately. A transit chain delays visible response because material must pass through sequential states. [구조적 비유 — 교과서 외 확장] Mathematically, the sum of identical exponential waiting times resembles an Erlang-type delay, which explains the delayed, sharper onset shape. This analogy is retained only as a learning aid, not as a textbook claim.

### E. Boundary conditions

- Equal $\tau$ across steps is a simplifying assumption that protects identifiability.
- n and $\tau$ trade off: more steps can reduce each step’s $\tau$ while preserving a similar overall delay.
- The chain describes response propagation, not drug distribution; distribution delay can be upstream and may still require $C_e$.
- [구현 번역] In ODE software, the chain is implemented as sequential first-order ODEs; exact NONMEM syntax is outside this handout.

<!-- RECAP -->
Transduction asks a different question from Link: not “how fast does drug reach the site?” but “how many delayed biological handoffs occur before the measured response appears?”

---

# §5 — Confusion Pair Dissection

---

<!-- CONFUSION -->
## Pair 1 — $k_{e0}$ vs $k_{out}$ vs $k_{off}$

| Dimension | $k_{e0}$ | $k_{out}$ | $k_{off}$ |
|---|---|---|---|
| What clock? | Plasma–biophase equilibration | Endogenous response-system turnover | Receptor-ligand dissociation |
| Typical model | Effect compartment | Indirect response / turnover | Receptor binding |
| Unit | time⁻¹ | time⁻¹ | time⁻¹ |
| Why confused? | Similar units and sometimes similar magnitude | Similar hysteresis shape | Similar single-dose fit |
| PD21 values | 0.025 min⁻¹ | 0.031 min⁻¹ | 0.018 min⁻¹ [G&W p.846] |
| Discriminator | $t_{max}$ and loop collapse under linear PK | turnover/recovery and repeated-dose behavior | binding/washout behavior and target information |

**Critical Blow — corrected:** G&W §3.9.7 warns that fitting turnover data with a distribution/link model can create biologically implausible dose-dependent EC50/Emax/n [G&W pp.271–272]. [교과서 외 실무 해석] In a model-justification setting, this would trigger a demand for alternative model comparison and sensitivity analysis; specific regulatory outcomes are not asserted by the textbook.

---

<!-- CONFUSION -->
## Pair 2 — Counterclockwise vs Clockwise Hysteresis

| Dimension | Counterclockwise | Clockwise |
|---|---|---|
| Visual meaning | Response lags concentration | Response attenuates or reverses relative to concentration |
| Common mechanisms | Distribution delay, system turnover, slow binding, concordant metabolite | Tolerance, antagonistic metabolite, down-regulation |
| Examples | Naproxen/digoxin/warfarin logic [R&T pp.234–246] | Cocaine/nitroglycerin-style tolerance logic [G&W pp.284–296] |
| Error if overread | Treating every lag as Link | Treating every attenuation as a single tolerance mechanism |
| Correct use | First diagnostic clue | First diagnostic clue |

**Memory hook:** direction says which way time bends; it does not name the mechanism by itself.

---

<!-- CONFUSION -->
## Pair 3 — Tolerance vs Rebound

| Dimension | Tolerance | Rebound |
|---|---|---|
| Time phase | During exposure | After withdrawal |
| Moderator state | $M$ catches up and suppresses R | $M$ remains after drug stimulus disappears |
| Same model? | Yes | Yes |
| Core ODE origin | $dR/dt=k_{in}S(C)-k_{out}M$ | same ODE pair [G&W p.299] |
| Study anchor | PD13 repeated infusion | PD13 repeated infusion and G&W feedback/rebound figures [G&W pp.297–300, 805–809] |

**Memory hook:** tolerance is the shadow growing under the drug; rebound is the shadow left after the drug leaves.

---

<!-- CONFUSION -->
## Pair 4 — Single Link Delay vs Transit Cascade

| Dimension | Single $k_{e0}$ link | Transit chain $n\times\tau$ |
|---|---|---|
| Delayed state | Drug concentration at biophase | Downstream biological response states |
| ODE shape | one first-order smoothing ODE | sequential first-order chain |
| Onset shape | immediate smooth approach | delayed sigmoidal propagation |
| Key diagnostic | same $t_{max}$ under linear PK | inability of n=1 to fit delayed onset |
| Anchor | G&W §3.9, PD20 | G&W §3.13, PD35 |

**Memory hook:** Link is one bridge. Transduction is a queue of handoffs.

---

# §7 — Self-Test: Active Recall Module

<!-- SELF-TEST -->
## Q1 — Recall
Write the effect-compartment ODE and state why $k_{1e}=k_{e0}$ is used.

**Answer:** $dC_e/dt=k_{e0}(C-C_e)$ [G&W pp.268–269]. The equality is a standard identifiability-based simplification, not a universal physical law [G&W pp.263, 265].

---

<!-- SELF-TEST -->
## Q2 — Application
A three-dose study shows the same response $t_{max}$ at every dose. Can you immediately choose Link model?

**Answer:** No. First verify linear PK; the same-$t_{max}$ property is stated under linear drug kinetics [G&W p.264]. Then check dose-stratified PD parameter coherence and model fit.

---

<!-- SELF-TEST -->
## Q3 — Error detection
A draft says “PD13 Table 3.10 shows EC50 dose-bifurcation under Link misspecification.” Correct it.

**Answer:** It should say “G&W §3.9.7 Table 3.10 link-model pitfall; Fig.3.59 is PD12 data.” PD13 is the repeated IV infusion tolerance/rebound model-comparison case [G&W pp.271, 805–809].

---

<!-- SELF-TEST -->
## Q4 — Mechanism triage
A concentration-response plot is counterclockwise. List three possible mechanisms and one additional discriminator for each.

**Answer:** Distributional delay → test $t_{max}$ dose invariance under linear PK; turnover delay → look for peak shift and system recovery time; slow binding → examine target/binding or washout behavior. Metabolite contribution requires metabolite concentration/pharmacology.

---

<!-- SELF-TEST -->
## Q5 — PD13 reasoning
In PD13, Model II has $k_{tol}=4.2$ and $k_{out}=2.9$ with AIC=−97.5 and WRSS=0.083. What should you expect in repeated-dose troughs?

**Answer:** Carry-over/trough drift. The moderator state does not instantly reset; repeated infusion reveals tolerance/rebound information that a single-dose study may hide [G&W p.808].

---

<!-- SELF-TEST -->
## Q6 — PD21 reasoning
Why is it unsafe to conclude that $k_{e0}$, $k_{out}$, and $k_{off}$ mean the same thing just because all are min⁻¹ and similar in magnitude?

**Answer:** They refer to different physical/biological clocks: biophase equilibration, system turnover, and receptor dissociation. PD21 reports similar values but compares different mechanistic models [G&W p.846].

---

<!-- SELF-TEST -->
## Q7 — PD35 reasoning
PD35 Table 35.1 shows WRSS 1319→789→642→632→682 for n=1→5. Why not simply choose n=4 because WRSS is lowest?

**Answer:** n=4 improves only slightly over n=3, while n=5 worsens. The pattern indicates practical sufficiency around n=3/4 and limited information capacity for exact step count [G&W p.914].

---

<!-- SELF-TEST -->
## Q8 — Boss dilemma, compressed
Model A is a stable Link model but produces dose-dependent EC50. Model B is less stable computationally but keeps a single biologically coherent EC50 and captures tolerance. Which principle guides selection?

**Answer:** Mechanistic validity outweighs statistical convenience. A model that implies dose-dependent receptor sensitivity without mechanism repeats the G&W §3.9.7 pitfall. Computational instability is a technical problem; biologically implausible parameter behavior is a model-validity problem.

---

# §8 — Meta-Frame & Big Picture

<!-- MASTER LENS -->
## A. Position in the PK/PD knowledge graph

This session sits between basic Emax/Hill/indirect response models and advanced integrated PK/PD systems such as TMDD, PBPK-PD coupling, and QSP. It teaches the distinction between three clocks:

1. **Drug clock:** how fast concentration reaches the biophase — $k_{e0}$.
2. **System clock:** how fast the physiological response is produced, lost, or adapted — $k_{out}$/$k_{tol}$.
3. **Signal clock:** how many downstream steps occur before the measured response appears — $n\times\tau$.

## B. Failure modes if this session is learned shallowly

1. **Link overuse:** every counterclockwise loop becomes a Link model, even when turnover is responsible. Result: dose-dependent EC50/Emax/n like G&W Table 3.10 [G&W p.271].
2. **Tolerance blindness:** repeated-dose response is simulated as if the system has no memory. Result: trough drift and rebound are missed [G&W pp.297–300, 805–809].
3. **Cascade underfitting:** delayed sigmoidal onset is forced into a single turnover state. Result: early/late residual patterns and onset-time misprediction, as PD35 demonstrates [G&W pp.323–325, 910–914].
4. **Unit-level confusion:** $k_{e0}$, $k_{out}$, and $k_{off}$ are mistaken as the same kind of parameter because all are time⁻¹ [G&W p.846].

## C. Professional moat

The durable skill is not memorizing ODEs. Fitting 전에 data가 어떤 hidden state를 요구하는지 보는 것이다: hidden **biophase concentration**, hidden **adaptive moderator**, 또는 hidden **transduction states**. 이 구분이 mathematically converged but biologically implausible PK/PD model을 막는다.

<!-- RECAP -->
Session 12’s final rule: **A delay is not a mechanism. Name the delayed state.**

---

## Content Lock v2 Completion Note

- Pass 1 readability polish applied without changing technical meaning.
- Pass 2 low-risk annotations inserted with `<!-- ANNOTATION -->` markers.
- No new facts, values, examples, equations, or page tags added.
- Existing source page tags, unresolved confirmation flags, and section order retained.
- Final v2 remains within the +8% length constraint relative to Content Lock v1.

# 12_html_compile_input_master_ver2.md

**Session:** 12 — Effect Compartment · Tolerance/Rebound · Transduction  
**Phase:** 4D Learner-Complete + Mastery-Enriched + HTML-Ready Master Assembler — **VER2 Restoration Pass**  
**Output mode:** PATCH MODE with verified figure-marker splicing  
**Generated:** 2026-05-06 (ver2 restoration)  
**Phase boundary:** This is not Phase 5. Do not generate HTML, Mermaid code, SVG code, or textbook image reproductions from this file.

**Ver2 change log relative to ver1:**
1. Restored full PD13 Model I/II/III parameter comparison table to Card 3 (textbook-anchored, G&W p.808 Table 13.1).
2. Restored Eq.3:204 governing $t_{1/2,k_{out}}$ as a function of $S(C)$ to Card 3 (G&W p.299).
3. Restored AUC asymmetry note ($AUC_R < AUC_E$) to Card 3 (G&W Fig.3.82).
4. Strengthened Card 3 Big Idea with concrete textbook clinical anchors (nitroglycerin Hat TDS, β-agonist desensitization, opioid tolerance — all G&W §3.11 cited).
5. Restored hysteresis collapse method to Card 2 as the bridge between R&T's diagnostic concept and PD21's $k_{e0}=0.025$ min⁻¹ numerical anchor (R&T pp.245–246; G&W PD21 pp.840–841).
6. Strengthened Wall 3 (moderator sign as homeostasis necessity) with bounded structural-stability commentary in Card 3 (Crucible Grade B, source-bounded).
7. Added §6 Master's Diagnostic Lens with four named GOF signatures (Crucible Grade B catalog, labeled as expert-derived diagnostic mnemonics).
8. Added two restored Self-Test items to §7 — Q9 (acenocoumarol vs phenprocoumon rate-limiting) from R&T Fig.8-11; Q10 (between-patient hysteresis direction variation) from R&T Ch.8 input-rate logic.
9. Updated §8 B failure modes to cross-reference §6 diagnostic catalog.
10. Updated PART B B4/B5/B6/B11 to reflect ver2 restorations.

**Splice verification:** all seven approved figure markers from Content Lock v2.1 remain in their original positions, unchanged. Anchor strings preserved verbatim.

---

## PART A — Learner-Facing Complete Handout

## Learner Navigation Aid

**How to use this handout**

1. Read §1 once as a triage map: one observed concentration–response delay can mean three different delayed states.
2. Study the four §2 cards in order: Link → Hysteresis triage → Tolerance/Rebound → Transduction.
3. At every Figure Pointer, open the original textbook/PDF figure; this handout does not reproduce copyrighted textbook images.
4. Use §5 before §7. The confusion pairs are designed to prevent the most common model-selection errors before self-testing.
5. Use §6 *after* §5 and *before* §7. The diagnostic-signature dictionary is most useful once the confusion pairs are clear, and it gives the self-test questions concrete diagnostic vocabulary.

**Before you start**

- You should already be comfortable with Emax/Hill models, basic one-compartment PK, and indirect response model vocabulary.
- Keep this question visible while reading: "What is the delayed hidden state?"

**After you finish**

- You should be able to distinguish $k_{e0}$, $k_{out}$, $k_{tol}$, and $k_{off}$ by what each clock governs.
- You should be able to explain why hysteresis direction is a diagnostic clue rather than a final model-selection rule, and how the *hysteresis collapse method* turns the loop geometry into a numerical $k_{e0}$ estimate (PD21).
- You should be able to explain why PD13 belongs to tolerance/rebound, and why G&W Table 3.10 is the Link-model pitfall.
- You should be able to read the full PD13 Model I/II/III parameter table and explain *why* Model II wins, not merely *that* it wins.
- You should be able to explain why PD35 supports a transduction chain without claiming that n equals the exact biological number of signaling steps.
- You should be able to name at least four GOF diagnostic signatures (EC50 dose-bifurcation, trough drift, S-curve CWRES residual, OFV plateau) and what each implies mechanistically.


# §1 — Session Header & Roadmap

**Source:** Gabrielsson & Weiner 5e + Rowland & Tozer 5e  
**Chapter range:** G&W Ch.3 §3.9/§3.11/§3.13 + PD13/20/21/35; R&T Ch.8  
**Core task:** classify time delay between concentration and response into distributional delay, system adaptation, or transduction cascade.

<!-- MASTER LENS -->
**Big Idea:** Plasma concentration and response can separate in time for different mechanistic reasons. 전문가의 첫 판단은 단순히 "delay term을 하나 붙이는 것"이 아니다. 먼저 그 지연이 **drug distribution** ($k_{e0}$), **system turnover/adaptation** ($k_{out}$/$k_{tol}$), 또는 **downstream signal propagation** ($n \times \tau$) 중 어디에 속하는지 정해야 한다.

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

<!-- FIGURE_DECISION: F12-01 | MODE=N | PHASE5_RENDER=Mermaid flowchart -->
**Figure Marker F12-01 — Three Hidden Clocks Behind PK/PD Time Delay**  
Phase 5 should render a new schematic showing that one observed concentration–response delay branches into three delayed hidden states: biophase concentration $C_e$, adaptive response/moderator state $R/M$, and downstream transit states $n \times \tau$.  
**Purpose:** prevent the reader from treating Link, Tolerance, and Transduction as parallel labels rather than a mechanism-triage sequence.  
**Do not render in Phase 4C.**

<!-- ANCHOR -->
The chapter sequence itself is the escalation logic. §3.9는 "distributional delay인가?"를 묻고, §3.11은 "system이 적응하고 있는가?"를 묻는다. §3.13은 "measured response가 downstream cascade 뒤에 나타나는가?"를 묻는다.

<!-- ANNOTATION --> 따라서 같은 time delay라도 숨은 state가 다르면 모델도 달라진다. 이 세션의 핵심은 delay의 크기가 아니라 **무엇이 delayed state인지**를 명명하는 것이다.

> **Mastery Lens — [EXPERT_INFERENCE | SOURCE-AWARE]**  
> 이 세션에서 "delay"는 시간 차이 자체가 아니라 hidden state를 찾으라는 신호다. 먼저 delayed state의 이름을 붙인 뒤에야 ODE family를 선택한다. 실무 escalation 순서: direct response → effect compartment(Link) → indirect response(turnover) → tolerance(Moderator) → transduction(transit chain). 이 순서는 §3.7→§3.9→§3.11→§3.13의 G&W 챕터 순서와 동형이며, 새 데이터를 받으면 *어느 단계에서 시작해야 하는지*가 첫 5초의 판단이 된다.

---

# §2 — Concept Anatomy Cards

---

## Card 1 — Effect Compartment Model & $k_{e0}$ [Apex]

<!-- MASTER LENS -->
### Big Idea

Effect Compartment Model은 **distributional delay**를 다루는 표준 link model이다. Plasma concentration $C$가 관찰되지 않는 biophase concentration $C_e$를 움직이고, $C_e$가 response를 움직인다. 가장 강한 실무적 시그니처는 **same response $t_{max}$ across increasing doses**이지만, 이 판단은 PK가 linear일 때만 유효하다 [G&W p.264].

### A. Formal definition

The effect compartment is a hypothetical first-order distribution link between plasma and biophase <!-- ANNOTATION -->(← 약물이 작용하는 효과 부위). $C_e$는 직접 측정되지 않는다. 따라서 response-time data로부터 역추정해야 하며, rising phase와 falling phase 정보가 모두 필요하므로 steady-state data alone are insufficient [G&W p.263].

<!-- FIGURE_DECISION: F12-02 | MODE=P | POINTER_ONLY -->
**Figure Pointer F12-02 — Effect-compartment inference sequence**  
Inspect **G&W Fig.3.53 (p.263)** before reading the derivation. Follow the source figure from plasma concentration to effect-compartment concentration $C_e$, then to response vs $C_e$ and response-time.  
**Purpose:** show why $C_e$ is inferred from response-time data rather than directly measured.  
**No image insertion; source figure must be viewed in the textbook/PDF.**

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

> **Mastery Lens — [EXPERT_INFERENCE | TEXTBOOK_CONSISTENT]**  
> $C_e$는 "관측 농도"가 아니라, plasma profile과 response curve가 동시에 말이 되도록 강제되는 hidden state이다. 따라서 $k_{e0}$ 추정의 품질은 농도자료만이 아니라 response의 상승·하강 정보가 얼마나 잘 포착되었는지에 의해 제한된다.

### C. Critical assumptions and boundaries

| Assumption | Keep | Boundary if violated |
|---|---|---|
| $C_e$ is inferred from response-time data | Yes | No rise/fall response data → $k_{e0}$ and PD shape cannot be separated [G&W p.263]. |
| Linear PK for $t_{max}$ test | Yes | Nonlinear PK can create apparent peak shift; first confirm exposure proportionality before using $t_{max}$ as model discriminator [G&W p.264]. |
| $k_{1e}=k_{e0}$ | Yes, corrected | This is an identifiability-based simplifying assumption, not a universal physical equality [G&W pp.263, 265]. |
| $K_p=1$ | Use only as simplification | If partitioning exists, $C_e$ and $C$ may differ even at steady state; estimated EC50 is a plasma-scale surrogate [G&W pp.263, 265–266]. |
| Response tracks $C_e$ instantaneously | Conditional | If system turnover or downstream cascade dominates, move to indirect response/tolerance/transduction. |

<!-- TRENCH -->
**Trench-Level Tip:** Do not run the $t_{max}$ dose-invariance test before checking PK linearity. G&W states the same-$t_{max}$ property under the condition "assuming the drug kinetics is linear" [G&W p.264].

### D. Corrected numeric anchors

- **G&W Table 3.9:** response equilibration half-lives include terbutaline FEV-1 7.5 min, theophylline FEV-1 11 min, d-tubocurarine/vecuronium muscle paralysis 4 min, fentanyl spectral edge 6.4 min, and QT-quinidine 8 min [G&W p.269].
- **R&T succinylcholine is separate:** succinylcholine is a dose-duration example: 0.5 mg/kg IV, $T_{50}\approx6$ min, $k\approx0.2\ \text{min}^{-1}$, and 80–20% response decline at about 22%/min [R&T pp.249–256]. It should not be labeled as G&W Table 3.9 $t_{1/2,k_{e0}}=4$ min.
- **PD20:** analgesic IV bolus example uses D=45 µg/kg, V=1 L/kg, K=0.50 h⁻¹, with initial estimates Emax≈3–5, EC50≈1.5 µg/L, $k_{e0}\approx0.1$ h⁻¹; G&W notes low EC50 precision because the dataset contained only one dose [G&W pp.836–839].

### E. Plausible fallacy — Link model fitted to turnover data

The major pitfall is not PD13. It is **G&W §3.9.7 Table 3.10**이다. 여기서는 turnover-generated data를 effect-compartment model로 fit한다. 그 결과 dose-stratified fits가 biologically implausible한 EC50/Emax/n 변화를 만든다: dose 1 EC50=0.681, dose 10 EC50=4.85, dose 100 EC50=0.941; the approximately sevenfold EC50 spread is a source-derived calculation [G&W p.271]. Fig.3.59 is described as using PD12 data, not PD13.

**Diagnostic name:** EC50 dose-bifurcation pattern. If dose-stratified fits imply that receptor sensitivity or capacity changes by dose without a mechanistic reason, the Link model is likely absorbing turnover/adaptation misspecification [G&W pp.271–272]. (See §6 Diagnostic Lens for the full signature dictionary.)

<!-- FIGURE_DECISION: F12-03 | MODE=P | POINTER_ONLY -->
**Figure Pointer F12-03 — Link-model pitfall is Table 3.10, not PD13**  
Inspect **G&W Fig.3.59 and Table 3.10 (p.271)** after this pitfall paragraph. Compare simultaneous and dose-stratified fits, focusing on the implausible dose-dependent EC50/Emax/n pattern.  
**Purpose:** anchor the corrected case identity: this is §3.9.7/Table 3.10 with PD12 data, not PD13.  
**No image insertion; source figure/table must be viewed in the textbook/PDF.**

> **Failure Mode — [AUDIT_DERIVED]**  
> Dose-stratified EC50/Emax/n이 크게 흔들릴 때 첫 질문은 "PD가 dose-dependent인가?"가 아니라 "Link model이 다른 delayed system state를 대신 흡수하고 있지 않은가?"이다. Table 3.10 pitfall은 이 질문을 자동화하기 위한 경고 표지다.

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

<!-- FIGURE_DECISION: F12-04 | MODE=P | POINTER_ONLY -->
**Figure Pointer F12-04 — Counterclockwise hysteresis as chronological loop**  
Inspect **R&T Fig.8-2 (p.235)** before using the diagnostic matrix. Trace the time labels around the naproxen loop and identify where the same concentration corresponds to different responses.  
**Purpose:** make hysteresis direction a visible time-ordered path, not a verbal label.  
**No image insertion; source figure must be viewed in the textbook/PDF.**

### B. Diagnostic matrix

| Direction | First interpretation | Mechanisms to test | Required follow-up |
|---|---|---|---|
| Counterclockwise | Response lags concentration | Distributional delay, indirect response, slow receptor binding, concordant metabolite | $t_{max}$ dose pattern, rise/fall response, metabolite/target data, model comparison |
| Clockwise | Response weakens earlier than concentration | Tolerance/desensitization, antagonistic metabolite, receptor down-regulation | repeated-dose pattern, rebound, metabolite pharmacology, recovery kinetics |
| Figure-eight / mixed | Competing time scales | Distribution delay + tolerance, sparse sampling artifact, multiple mechanisms | denser sampling and mechanism-informed design before committing to one model |

### B-2. Hysteresis collapse method — turning loop geometry into a number

R&T introduces a powerful diagnostic move that bridges Card 1 and Card 2: an effect-compartment transformation of the time-paired concentration–response data can *collapse* the counterclockwise loop into a single concentration–response curve when distributional delay is the dominant mechanism [R&T pp.245–246, Fig.8-14]. The $k_{e0}$ value that produces the cleanest collapse is itself the distributional-delay estimate.

PD21 makes this concrete. The reported $k_{e0}\approx0.025$ min⁻¹ for the antagonist X experiment is the value that brings the rising-limb and falling-limb response data into one smooth curve when projected onto $C_e$ rather than $C$ [G&W PD21 pp.840–846]. This is the same numerical clock that appears in the §2 Card 1 derivation; here it is *operationalized* as a graphical model-discrimination tool.

> **Mastery Lens — [TEXTBOOK_DERIVED | SOURCE-AWARE]**  
> Loop collapse가 깨끗하게 일어나면 분포 지연 가설은 산다. 깨끗하게 collapse되지 않거나 dose에 따라 다른 $k_{e0}$가 필요하면, 다른 hidden state(turnover 또는 transduction)가 작용 중이라는 신호다. 이때 다음 카드(Card 3, Card 4)로 넘어가는 결정이 강제된다.

### C. R&T clinical anchors

- **Digoxin:** effect rises while plasma falls during 0–4 h after IV dose; distribution to cardiac tissue and target binding are slow [R&T p.234].
- **Naproxen:** oral 500 mg produces counterclockwise hysteresis; effect-compartment transformation can collapse the loop into a clearer concentration-response relationship [R&T pp.235, 245–246].
- **Warfarin:** delayed prothrombin complex response reflects system turnover rather than simple tissue distribution [R&T pp.242–248].
- **Succinylcholine:** response duration follows dose-duration logic; useful for decline/duration teaching but not the same as G&W Table 3.9 effect-compartment half-life [R&T pp.249–256].

> **Scope Micro-Patch — [TEXTBOOK_DERIVED | SCOPE_REQUIRED]**  
> R&T duration anchors should remain visible for mechanism triage: naproxen 500 mg oral shows counterclockwise hysteresis and a delayed peak-response pattern; warfarin 1.5 mg/kg oral has a delayed prothrombin-complex nadir around 48 h with system turnover on the order of 1–2 days; aspirin 650 mg has a short plasma half-life but antiplatelet response persisting for days; succinylcholine 0.5 mg/kg IV remains the dose-duration example and must not be relabeled as the G&W Table 3.9 4-min $t_{1/2,k_{e0}}$ case [Scope Lock; R&T pp.234–256].

<!-- TRENCH -->
**Trench-Level Tip:** Sparse sampling can manufacture a fake figure-eight. Before interpreting direction, confirm that sampling density captures both concentration rise/fall and response rise/fall; otherwise the loop geometry is a plotting artifact, not a mechanism.

### D. Structural interpretation

Clockwise/counterclockwise direction describes the phase-plane trajectory of time-paired concentration and response. The direction narrows the model family, but it does not distinguish distribution delay from turnover delay by itself. The decisive question is: **what state variable is delayed — drug at the biophase, the physiological response system, or a downstream cascade?**

Direction-dependent boundary insight from R&T: a clockwise loop can also appear when the *rate of drug input* exceeds the rate of distribution or tolerance development — i.e., very rapid IV bolus into a slow biophase [R&T p.236]. This is *not* tolerance; it is a kinetic-input artifact that disappears with slower infusion. Mistaking this artifact for tolerance triggers wasted Moderator-model fitting.

> **Practice Lens — [CRUCIBLE_DERIVED]**  
> Hysteresis direction은 model family를 줄여주는 filter이지 판결문이 아니다. Direction → linearity/tmax → repeated-dose pattern → mechanism evidence 순서로 검증해야 loop geometry를 mechanism으로 과해석하지 않는다.

<!-- RECAP -->
Hysteresis is the map, not the destination. Read the arrow first, attempt a $k_{e0}$ collapse, then prove the mechanism with dose, timing, and model behavior.

---

## Card 3 — Tolerance/Rebound via Moderator $M$

<!-- MASTER LENS -->
### Big Idea

Tolerance와 rebound는 서로 무관한 두 현상이 아니다. Moderator model에서 $M$은 response를 뒤따라 형성되는 delayed counter-regulatory state이다. Dosing 중에는 $M$이 response를 줄인다. Dosing이 중단된 뒤에는 $M$이 남아 baseline 너머의 rebound를 만들 수 있다 [G&W pp.297–300].

이 추상적 ODE 쌍이 임상에서 부딪히는 모습은 매우 구체적이다. Nitroglycerin 작업자의 "월요일 두통, 일요일 angina" 패턴(G&W Fig.3.71의 hat TDS 일화) — 약물이 반복 노출되면 효과가 줄고(tolerance), 주말 dose holiday에 baseline 너머의 vasoconstrictive rebound가 발생할 수 있다는 임상 신호 — 가 같은 ODE 쌍의 두 phase로 emerge한다 [G&W pp.284–286]. β-agonist의 점진적 desensitization, opioid의 점진적 내성, cocaine의 acute cardiovascular tolerance — 모두 같은 Moderator 구조의 변주다 [G&W pp.284–286, 295–296].

### A. Formal definition

Tolerance is progressive response reduction during exposure; rebound is response excursion after withdrawal. G&W lists multiple tolerance mechanisms, including receptor down-regulation/internalization, transduction changes, cofactor depletion, mRNA/protein effects, antibodies, and enzyme induction [G&W pp.284–286].

### B. Moderator ODEs

Core negative-feedback model:

$$\frac{dR}{dt}=k_{in}S(C)-k_{out}M \quad \text{[G&W p.299, Eq.3:193]}$$

$$\frac{dM}{dt}=k_{tol}R-k_{tol}M \quad \text{[G&W p.299, Eq.3:194]}$$

At baseline, $S(C)=1$ and $R_0=k_{in}/k_{out}$ [G&W pp.299–300]. At steady state for the simple form, $R=M$ because $dM/dt=0$ implies $k_{tol}(R-M)=0$ when $k_{tol}\neq0$.

The apparent response half-life is governed by the stimulus-dependent expression [G&W p.299, Eq.3:204]:

$$t_{1/2,k_{out}} = \frac{\ln 2 \cdot R_0}{k_{in}\cdot S(C)}$$

자극 $S(C)$가 클수록(고용량 또는 강한 약물) response의 *겉보기 반감기*는 짧아진다. 이 한 줄이 "왜 고용량에서 tolerance가 더 빠르게 발달하는가"의 수학적 근거다 — kinetics가 빨라지는 게 아니라, 같은 kinetic constant에서 driver $S(C)$가 커져 effective time scale이 단축된다.

> **Mastery Lens — [CRUCIBLE_DERIVED]**  
> $M$은 drug compartment가 아니라 system memory이다. Rebound가 생기는 이유는 drug가 남아서가 아니라, drug가 사라진 뒤에도 counter-regulatory state가 남아 response equation을 계속 밀기 때문이다.

The more general "moderator + level of response" form introduces a nonlinear $M$ effect and produces a second-order steady-state solution [G&W pp.301–302, Eq.3:205–3:216]. The key handout point is not the algebraic expansion but the consequence: feedback strength changes the response level and recovery behavior.

### B-2. Why the negative-feedback sign is mathematically required

In Eq.3:193 the moderator $M$ enters the response equation with a *subtraction*: it opposes the stimulus. If the sign were reversed — if $M$ added to $S(C)$ rather than subtracting from $k_{out}M$ — the system would self-amplify and diverge instead of returning to baseline. The negative sign is therefore not an arbitrary modeling choice but a structural-stability requirement for any model that must produce homeostasis [G&W pp.297–300; structural commentary, source-bounded].

이 부호 하나가 PD13 Model II의 AIC=−97.5 우위를 만드는 *수학적 정합성*의 출처이다. Model I (no feedback) 또는 Model III (pool/precursor)이 같은 수치적 적합도를 흉내낼 수는 있어도, *반복 dose에서 baseline-traversing rebound와 partial tolerance를 함께* 생성하는 구조적 필연은 음성 피드백 부호로부터만 emerge한다.

### C. AUC asymmetry — a built-in signature

For the moderator system, the response excursion above baseline during dosing ($AUC_E$) is generally larger than the rebound excursion below baseline after withdrawal ($AUC_R$): $AUC_R < AUC_E$ [G&W Fig.3.82, p.298]. The reason is structural — during dosing the drug stimulus and the still-rising $M$ both push $R$, but during withdrawal only the residual $M$ drives the deviation. This asymmetry is a free diagnostic check: if a model predicts $AUC_R \approx AUC_E$ where the data show clear asymmetry, the moderator structure is mis-specified.

### D. PD13 anchor — repeated infusion tolerance/rebound

PD13 is the proper repeated IV infusion case study. 이 사례는 ordinary turnover, negative-feedback moderator, and pool/precursor structures를 비교한다 [G&W pp.805–809]. 가장 잘 맞는 것은 Model II, 즉 moderator model이다. 단순 진술이 아니라 *비교*로 읽어야 한다 — 다음 표가 그 비교다 [G&W p.808, Table 13.1].

| 파라미터 | Model I (no FB) | **Model II (Moderator)** | Model III (pool/precursor) |
|---|---:|---:|---:|
| $k_{in}$ | 21 | **30** | 94 |
| $k_{out}$ | 7.3 | **2.9** | 35 |
| $k_{tol}$ | — | **4.2** | 0.05 |
| EC50 / IC50 | 390 | **350** | 270 |
| Emax / Imax | 4.8 | **9.8** | 0.84 |
| n (Hill) | — | **7.4** | — |
| AIC | −39.0 | **−97.5** | −43.5 |
| WRSS | 0.33 | **0.083** | 0.28 |

읽는 방법: AIC/WRSS만 보고 Model II를 채택해서는 학습이 끝난 것이 아니다. *Model II에서 $k_{tol}=4.2 > k_{out}=2.9$* 라는 사실 — 즉 tolerance development(memory build-up)이 response turnover보다 빠르다는 사실 — 이 카드의 핵심 mechanistic 발견이다 [G&W p.808]. 이 부등식이 단일 infusion 안에서도 tolerance가 가시화되는 이유이고, Model III의 $k_{tol}=0.05$가 임상적으로 비현실적인 이유이다.

The key interpretation is **trough drift/carry-over**이다. Repeated infusion에서는 moderator state가 완전히 돌아오지 않았기 때문에 second trough가 first trough로 단순히 reset되지 않는다. 이 때문에 tolerance를 보려면 single-dose data보다 repeated-dose data가 훨씬 더 정보적이다 [G&W p.808].

<!-- FIGURE_DECISION: F12-05 | MODE=P | POINTER_ONLY -->
**Figure Pointer F12-05 — PD13 repeated-infusion memory pattern**  
Inspect **G&W Fig.13.1 and Table 13.1 (pp.806–808)** after the PD13 paragraph. Focus on whether the second infusion behaves like a clean reset or shows carry-over from the hidden moderator state.  
**Purpose:** connect Model II superiority to visible repeated-dose memory, not only to AIC/WRSS values.  
**No image insertion; source figure/table must be viewed in the textbook/PDF.**

<!-- TRENCH -->
**Trench-Level Tip:** If the second-dose trough differs from the first-dose trough under similar exposure, suspect a hidden moderator state. Direct response or pure link models do not naturally carry that memory.

### E. Alternative tolerance/rebound structures — compressed context

- **Time-dependent attenuation (Colburn–Eldon):** empirical smoothing of potency/capacity over time; useful but weakly mechanistic and poor for rebound [G&W pp.291–292].
- **Antagonistic metabolite:** can explain antagonism but does not by itself cover rebound without added structure [G&W pp.292–293].
- **Tolerance compartment / counteracting mechanisms:** alternative state-variable formulations for adaptive systems [G&W pp.293–295].
- **Pool/precursor model (Model III in PD13):** tested and inferior to moderator Model II for this dataset [G&W pp.807–808]; predicts complete tolerance only, fails partial tolerance.

### F. Why the sign matters

Moderator $M$은 $R$을 따라가지만, response equation에서는 counteracting term으로 나타난다. 이 negative-feedback sign 때문에 system은 self-amplifying이 아니라 homeostatic하게 작동한다. 여기서 필요한 mechanistic memory는 한 줄이다: **drug pushes R, R builds M, M pushes back**.

<!-- FIGURE_DECISION: F12-06 | MODE=N | PHASE5_RENDER=Mermaid flowchart or inline SVG -->
**Figure Marker F12-06 — Moderator Memory Loop**  
Phase 5 should render a new schematic: `Drug stimulus S(C) → Response R → delayed Moderator M ┤ Response R`, with phase labels for dosing and withdrawal. Include the compact ODE labels `dR/dt = k_in S(C) − k_out M` and `dM/dt = k_tol(R − M)`.  
**Purpose:** show tolerance and rebound as two phases of one delayed negative-feedback loop.  
**Do not render in Phase 4C.**

<!-- RECAP -->
Tolerance/rebound is the pharmacodynamic memory problem. If the system remembers prior exposure, add a state that remembers — and check that its sign produces homeostasis, not divergence.

---

## Card 4 — Transduction Model / Transit Chain

<!-- MASTER LENS -->
### Big Idea

Transduction models는 receptor activation과 observed functional response 사이의 chain을 표현한다. Response onset이 immediate exponential이 아니라 delayed sigmoid이면, single turnover compartment는 너무 얕을 수 있다. 이때 sequential transit compartments가 필요하다 [G&W pp.323–325].

### A. Formal definition

A transduction model uses a chain of compartments or events between receptor-ligand coupling and observed response. 각 transit step은 characteristic transit time $\tau$와 corresponding fractional turnover rate $k_{out}=1/\tau$를 가진다 [G&W pp.323–325].

<!-- FIGURE_DECISION: F12-07 | MODE=P | POINTER_ONLY -->
**Figure Pointer F12-07 — Transduction chain and delayed onset**  
Inspect **G&W Fig.3.98 and Fig.3.99 (p.323)** before reading the transduction ODEs. First identify the receptor-to-response chain, then inspect the 15–20 h onset-delay pattern.  
**Purpose:** separate "drug reaches the site slowly" from "signal propagation to the measured response is slow."  
**No image insertion; source figures must be viewed in the textbook/PDF.**

### B. Core equations

Receptor-driving step:

$$\frac{dR_e}{dt}=\frac{1}{\tau}\left(E_0S(C)-R_e\right) \quad \text{[G&W p.911, Eq.35:5]}$$

Sequential transit compartments:

$$\frac{dR_i}{dt}=\frac{1}{\tau}(R_{i-1}-R_i),\quad i=1,2,\ldots,n \quad \text{[G&W p.911, Eq.35:6]}$$

Observed response is the final downstream state, $R_{obs}=R_n$.

<!-- ANNOTATION --> 여기서 지연되는 것은 약물의 이동이 아니라 response signal의 전달이다. 따라서 Link model의 "drug reaches site" 질문과 Transduction model의 "signal reaches measurement" 질문은 다르다.

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

또한 EC50와 E0가 n에 거의 무관(robust)하다는 점, 그리고 $n\times\tau \approx$ const라는 trade-off (총 transit time은 거의 일정, 분할 방식만 다름)는 model parameterization에 대한 두 가지 안전감을 동시에 준다 [G&W p.914].

> **Practice Lens — [CRUCIBLE_DERIVED]**  
> PD35의 n 선택은 "진짜 생물학적 step 수를 맞혔다"는 선언이 아니라, 현재 데이터가 구분 가능한 지연 구조의 해상도를 읽는 작업이다. n=3 이후 WRSS 이득이 작고 n=5에서 악화되면, 추가 cascade detail은 설명력보다 불안정성을 더할 수 있다.

<!-- TRENCH -->
**Trench-Level Tip:** Do not choose n by "lowest WRSS" alone. In PD35, 1319→789→642→632→682 says: the model needs more than one step, n=3 is practically enough, and the data cannot resolve exact cascade depth.

### D. Structural intuition

A single first-order delay begins moving immediately. A transit chain delays visible response because material must pass through sequential states. [구조적 비유 — 교과서 외 확장] Mathematically, the sum of identical exponential waiting times resembles an Erlang-type delay, which explains the delayed, sharper onset shape. This analogy is retained only as a learning aid, not as a textbook claim.

### E. Boundary conditions

- Equal $\tau$ across steps is a simplifying assumption that protects identifiability.
- n and $\tau$ trade off: more steps can reduce each step's $\tau$ while preserving a similar overall delay.
- The chain describes response propagation, not drug distribution; distribution delay can be upstream and may still require $C_e$.
- [구현 번역] In ODE software, the chain is implemented as sequential first-order ODEs; exact NONMEM syntax is outside this handout.

<!-- RECAP -->
Transduction asks a different question from Link: not "how fast does drug reach the site?" but "how many delayed biological handoffs occur before the measured response appears?"

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
| Diagnostic move | Try $k_{e0}$-based loop collapse first | Check repeated-dose pattern; check input rate vs distribution rate |
| Error if overread | Treating every lag as Link | Treating every attenuation as a single tolerance mechanism (input-rate artifacts can mimic) |
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
| AUC signature | $AUC_E$ above baseline | $AUC_R < AUC_E$ below baseline [G&W Fig.3.82] |
| Study anchor | PD13 repeated infusion | PD13 repeated infusion and G&W feedback/rebound figures [G&W pp.297–300, 805–809] |

**Memory hook:** tolerance is the shadow growing under the drug; rebound is the shadow left after the drug leaves.

---

<!-- CONFUSION -->
## Pair 4 — Single Link Delay vs Transit Cascade

| Dimension | Single $k_{e0}$ link | Transit chain $n\times\tau$ |
|---|---|---|
| Delayed state | Drug concentration at biophase | Downstream biological response states |
| ODE shape | one first-order smoothing ODE | sequential first-order chain |
| Onset shape | immediate smooth approach (max slope at t=0) | delayed sigmoidal propagation (zero slope at t=0) |
| Key diagnostic | same $t_{max}$ under linear PK | inability of n=1 to fit delayed onset |
| Anchor | G&W §3.9, PD20 | G&W §3.13, PD35 |

**Memory hook:** Link is one bridge. Transduction is a queue of handoffs.

---

# §6 — Master's Diagnostic Lens (GOF Signature Dictionary)

> **Source-boundary note — [EXPERT_INFERENCE | TEXTBOOK_DERIVED]**  
> The four named signatures below are pedagogical mnemonics derived from textbook anchors and Crucible-Grade-B expert review. The *patterns* are observable in textbook data (G&W §3.9.7, PD13, PD35) and in standard NONMEM diagnostic plots; the *names* are pedagogical and not direct textbook nomenclature. NONMEM-specific implementation language is intentionally minimized.

When a fit converges but feels wrong, run the data through these four diagnostic lenses before re-parameterizing. Each lens says: "If you see this pattern, the next escalation step in the model triage is X."

### Signature 1 — EC50 dose-bifurcation pattern

- **What you see:** Fitting the model dose-by-dose (individual fits) yields EC50, Emax, or n values that vary substantially across dose groups, in directions or magnitudes that have no mechanistic justification.
- **Mechanistic meaning:** A Link model is being forced to absorb a turnover/adaptation effect. EC50 is migrating to compensate for unmodeled dynamics.
- **Textbook anchor:** G&W §3.9.7 Table 3.10 — dose-stratified EC50 at 0.681, 4.85, 0.941 (≈ sevenfold spread); simultaneous fit shows systematic deviation [G&W p.271].
- **Next step:** Move from Link → indirect response (turnover); test whether a single EC50 is recovered.

### Signature 2 — Trough drift / carry-over pattern

- **What you see:** In repeated-dose data, the trough at the end of cycle 2 is not the same as the trough at the end of cycle 1, even when exposure (AUC) is comparable. Successive troughs deepen or shift in the same direction.
- **Mechanistic meaning:** A hidden state is carrying memory from cycle to cycle. In tolerance/rebound systems, the moderator $M$ has not fully washed out before the next dose arrives.
- **Textbook anchor:** G&W p.808 explicitly notes that the second-dose trough in PD13 is not the same as the first, and that this is the signature of moderator activation [G&W pp.805–809].
- **Next step:** Move from indirect response → moderator (Model II); compare AIC/WRSS and check $k_{tol}/k_{out}$ ratio.

### Signature 3 — Delayed-onset / S-shaped onset residual pattern

- **What you see:** A single-turnover (n=1) indirect response model is fitted to data with a long delayed onset. The fit predicts response rising too early, the data rises later and more sharply. Residuals over time form an under-then-over-then-under pattern around the onset region.
- **Mechanistic meaning:** A single first-order delay cannot produce a near-flat early phase followed by a sharp rise. Sequential transit compartments are required.
- **Textbook anchor:** PD35 Table 35.1 — WRSS drops from 1319 (n=1) to 789 (n=2) to 642 (n=3); the n=1 vs n=3 comparison is roughly twofold improvement, indicating that the onset shape is genuinely cascade-driven, not single-turnover-driven [G&W p.914].
- **Next step:** Move from indirect response → transit chain; let the data choose n by parsimony.

### Signature 4 — OFV / WRSS plateau pattern

- **What you see:** As you escalate model complexity along a structural sequence (e.g., n=1, n=2, n=3, n=4, n=5 transit compartments; or single → moderator → moderator+M50), OFV or WRSS improves and then plateaus, with a small subsequent worsening.
- **Mechanistic meaning:** The data has reached its information-capacity ceiling for that mechanism. Additional parameters do not capture additional structure; they begin to absorb noise.
- **Textbook anchor:** PD35 sequence 1319 → 789 → 642 → 632 → 682 (n=1→5). The 642→632 step is small; 632→682 is a worsening, indicating over-parameterization beyond n=3 or n=4 [G&W p.914].
- **Next step:** Stop escalating. Choose the parsimony-supported model. Document that the data cannot resolve finer structure.

> **Mastery Lens — [EXPERT_INFERENCE | SOURCE-AWARE]**  
> 네 시그니처는 모델 misspecification의 *서로 다른* 위치를 가리킨다 — Signature 1은 *모델 패밀리 선택*의 오류, Signature 2는 *반복 노출 메모리*의 누락, Signature 3은 *cascade depth*의 부족, Signature 4는 *데이터 해상도* 한계. 이 네 패턴을 구분하지 못하면, 잘못된 한 개 패치(예: re-parameterization)로 다른 시그니처를 덮으려 하다가 모델이 오히려 손상된다.

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
A draft says "PD13 Table 3.10 shows EC50 dose-bifurcation under Link misspecification." Correct it.

**Answer:** It should say "G&W §3.9.7 Table 3.10 link-model pitfall; Fig.3.59 is PD12 data." PD13 is the repeated IV infusion tolerance/rebound model-comparison case [G&W pp.271, 805–809].

---

<!-- SELF-TEST -->
## Q4 — Mechanism triage
A concentration-response plot is counterclockwise. List three possible mechanisms and one additional discriminator for each.

**Answer:** Distributional delay → test $t_{max}$ dose invariance under linear PK, and try a $k_{e0}$-based loop collapse; turnover delay → look for peak shift and system recovery time; slow binding → examine target/binding or washout behavior. Metabolite contribution requires metabolite concentration/pharmacology.

---

<!-- SELF-TEST -->
## Q5 — PD13 reasoning
In PD13, Model II reports $k_{in}=30$, $k_{out}=2.9$, $k_{tol}=4.2$, EC50=350, Emax=9.8, n=7.4, AIC=−97.5, WRSS=0.083 — superior to Model I (no feedback, AIC=−39.0) and Model III (pool, AIC=−43.5). Beyond AIC, what one parameter relationship makes Model II the mechanistically right answer?

**Answer:** $k_{tol}=4.2 > k_{out}=2.9$, i.e. moderator development is faster than response turnover. This inequality predicts that tolerance is visible *within* a single infusion, and it is what makes carry-over/trough-drift observable in the second cycle [G&W p.808]. Model III's $k_{tol}=0.05$ is biologically implausible for the observed pattern.

---

<!-- SELF-TEST -->
## Q6 — PD21 reasoning
Why is it unsafe to conclude that $k_{e0}$, $k_{out}$, and $k_{off}$ mean the same thing just because all are min⁻¹ and similar in magnitude?

**Answer:** They refer to different physical/biological clocks: biophase equilibration, system turnover, and receptor dissociation. PD21 reports similar values (0.025, 0.031, 0.018 min⁻¹) but compares different mechanistic models [G&W p.846].

---

<!-- SELF-TEST -->
## Q7 — PD35 reasoning
PD35 Table 35.1 shows WRSS 1319→789→642→632→682 for n=1→5. Why not simply choose n=4 because WRSS is lowest?

**Answer:** n=4 improves only slightly over n=3 (642→632), while n=5 worsens (632→682). The pattern indicates practical sufficiency around n=3, with information-capacity ceiling reached. n=3 is parsimony-supported; declaring n=4 a "better" model claims more than the data resolves [G&W p.914].

---

<!-- SELF-TEST -->
## Q8 — Boss dilemma, compressed
Model A is a stable Link model but produces dose-dependent EC50. Model B is less stable computationally but keeps a single biologically coherent EC50 and captures tolerance. Which principle guides selection?

**Answer:** Mechanistic validity outweighs statistical convenience. A model that implies dose-dependent receptor sensitivity without mechanism repeats the G&W §3.9.7 pitfall (see §6 Signature 1). Computational instability is a technical problem; biologically implausible parameter behavior is a model-validity problem.

---

<!-- SELF-TEST -->
## Q9 — Rate-limiting comparison (R&T anchor)
Acenocoumarol (plasma $t_{1/2} \approx 15$ h) and phenprocoumon (plasma $t_{1/2} \approx 5$ days) act on the same target (clotting-factor synthesis inhibition), but their *baseline-recovery times* differ by roughly an order of magnitude. What rate-limits each drug's recovery?

**Answer:** Recovery is rate-limited by *whichever process is slower* among (i) drug elimination (kinetics) and (ii) clotting-factor turnover (dynamics) [R&T Ch.8, Fig.8-11]. For acenocoumarol, drug clearance is fast and clotting-factor turnover ($t_{1/2} \approx 1{-}2$ days) becomes the rate-limit; recovery time is dynamics-limited. For phenprocoumon, drug clearance itself is the slowest step ($t_{1/2} \approx 5$ days); recovery time is kinetics-limited. Warfarin ($t_{1/2} \approx 1.5$ days) sits at the boundary, which is one structural reason warfarin dose titration is clinically delicate.

---

<!-- SELF-TEST -->
## Q10 — Between-patient hysteresis variation
You observe a hysteresis loop in two patients given the same drug. Patient A's loop is counterclockwise; patient B's loop is clockwise. List two plausible explanations grounded in this session's framework.

**Answer:** (1) **Two mechanisms operating simultaneously with different relative dominance.** When distributional delay and tolerance both contribute, the visible direction depends on which is dominant during the observation window — patient A may be sampled mostly in the distribution-delay phase, patient B mostly in the tolerance phase, and longer observation could reveal a figure-eight in either. (2) **Input-rate vs distribution-rate disparity.** R&T notes that a clockwise loop can also appear when the rate of drug input is more rapid than the rate of distribution or tolerance development [R&T p.236]; differences in oral absorption rate, infusion rate, or first-pass kinetics across patients can therefore flip the apparent direction without different underlying mechanisms.

---

# §8 — Meta-Frame & Big Picture

<!-- MASTER LENS -->
## A. Position in the PK/PD knowledge graph

This session sits between basic Emax/Hill/indirect response models and advanced integrated PK/PD systems such as TMDD, PBPK-PD coupling, and QSP. It teaches the distinction between three clocks:

1. **Drug clock:** how fast concentration reaches the biophase — $k_{e0}$.
2. **System clock:** how fast the physiological response is produced, lost, or adapted — $k_{out}$/$k_{tol}$.
3. **Signal clock:** how many downstream steps occur before the measured response appears — $n\times\tau$.

## B. Failure modes if this session is learned shallowly

1. **Link overuse (Signature 1):** every counterclockwise loop becomes a Link model, even when turnover is responsible. Result: dose-dependent EC50/Emax/n like G&W Table 3.10 [G&W p.271].
2. **Tolerance blindness (Signature 2):** repeated-dose response is simulated as if the system has no memory. Result: trough drift and rebound are missed [G&W pp.297–300, 805–809].
3. **Cascade underfitting (Signature 3):** delayed sigmoidal onset is forced into a single turnover state. Result: early/late residual patterns and onset-time misprediction, as PD35 demonstrates [G&W pp.323–325, 910–914].
4. **Over-parameterization (Signature 4):** model complexity is escalated past the data's information-capacity ceiling, taken as evidence of a mechanism that the data does not actually resolve [G&W p.914].
5. **Unit-level confusion:** $k_{e0}$, $k_{out}$, and $k_{off}$ are mistaken as the same kind of parameter because all are time⁻¹ [G&W p.846].

(Cross-reference: §6 Master's Diagnostic Lens names these four signatures explicitly.)

## C. Professional moat

The durable skill is not memorizing ODEs. Fitting 전에 data가 어떤 hidden state를 요구하는지 보는 것이다: hidden **biophase concentration**, hidden **adaptive moderator**, 또는 hidden **transduction states**. 이 구분이 mathematically converged but biologically implausible PK/PD model을 막는다.

> **Mastery Lens — [EXPERT_INFERENCE | SOURCE-AWARE]**  
> 세 모델군의 공통점은 모두 "시간 지연"을 설명한다는 점이고, 차이는 delayed state의 정체다. 좋은 모델러는 rate constant의 단위를 먼저 보지 않고, 그 rate constant가 무엇의 clock인지 먼저 묻는다. 그리고 fit 결과에서 자기 모델이 §6의 네 시그니처 중 어느 하나를 만들고 있지 않은지 — *수렴 이전에* — 검사한다.

<!-- RECAP -->
Session 12's final rule: **A delay is not a mechanism. Name the delayed state.**

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

### B4. Zero-Omission Coverage Matrix (ver2)

| Domain | Required item | Evidence in PART A | Status | Action |
|---|---|---|---|---|
| C1 Scope concepts | Effect Compartment, Hysteresis triage, Tolerance/Rebound, Transduction | §1 roadmap and four §2 cards | PRESENT | No action. |
| C2 G&W required anchors | PD20, PD21, PD13, PD35, Table 3.9 | Card 1 D/F, Card 3 D, Card 4 C | PRESENT | No action. |
| C2 R&T required anchors | digoxin, naproxen, warfarin, aspirin, succinylcholine | Card 2 C plus Scope Micro-Patch | REPAIRED_BY_MICRO_PATCH | Added one bounded scope-required R&T anchor patch. |
| C3 Audit MUST_FIX | PD13/Table 3.10 label correction, k1e=ke0 identifiability, succinylcholine separation, hysteresis non-determinism, implementation/regulatory labeling, transduction analogy control | Cards 1–4 and §5 | PRESENT | No rejected content restored. |
| C4 Audit T5 high-impact omissions | Link pitfall, PD20/PD21/PD35, correct case identity, model-selection caveats | Cards 1, 3, 4, §5, §7 | PRESENT | No unresolved high-impact omission detected. |
| C4-2 Crucible Grade A items | Wall 1, Wall 2, Wall 4, Sparse-sampling figure-eight, T4 deletions | Cards 1–4, §5, §6, §8 | PRESENT | All Grade A items present. |
| C4-3 Crucible Grade B catalog | GOF signature catalog (4 patterns) | §6 Master's Diagnostic Lens | RESTORED_VER2 | Bounded catalog with labeled epistemic status. |
| C4-4 Card 3 PD13 Model I/II/III comparison | Full parameter table with kin, kout, ktol, EC50, Emax, n, AIC, WRSS | Card 3 D | RESTORED_VER2 | Restored from textbook (G&W p.808 Table 13.1) and Step 1 Draft v0 verified by Audit T1. |
| C4-5 Card 3 Eq.3:204 governing $t_{1/2,k_{out}}$ | Stimulus-dependent half-life formula | Card 3 B | RESTORED_VER2 | Direct G&W p.299 anchor; explains high-dose tolerance acceleration. |
| C4-6 Card 3 AUC asymmetry | $AUC_R < AUC_E$ | Card 3 C; §5 Pair 3 | RESTORED_VER2 | Direct G&W Fig.3.82 anchor. |
| C4-7 Hysteresis collapse method | $k_{e0}$-based loop collapse as PD21 application | Card 2 B-2 | RESTORED_VER2 | R&T pp.245–246 + G&W PD21 pp.840–846. Bridges R&T diagnostic concept and G&W numerical anchor. |
| C4-8 Card 3 clinical Big Idea anchors | Nitroglycerin Hat TDS, β-agonist desensitization, opioid tolerance | Card 3 Big Idea | RESTORED_VER2 | All G&W §3.11 textbook-cited (pp.284–286, Fig.3.71). |
| C4-9 R&T rate-limiting Self-Test | Acenocoumarol vs phenprocoumon | §7 Q9 | RESTORED_VER2 | Direct R&T Fig.8-11 anchor. |
| C4-10 Between-patient hysteresis Self-Test | Direction variation across patients | §7 Q10 | RESTORED_VER2 | R&T Ch.8 input-rate logic. |
| C4-11 Wall 3 strengthening | Negative-feedback sign as homeostasis necessity | Card 3 B-2 | RESTORED_VER2 | Bounded structural-stability commentary; textbook-aligned. |
| C5 Figure coverage | F12-01 through F12-07 KEEP markers | All seven markers inserted once | PRESENT | Textbook figures pointer-only; N-mode schematics deferred to Phase 5. Marker positions unchanged from ver1. |
| C6 Page/source tag integrity | Existing source page tags preserved; no [p.확인 필요] deleted | Canonical text preserved; no page-number changes | PRESENT | No fabricated page tags. New ver2 content uses only previously-verified page anchors. |
| C7 Crucible Grade A preservation | Different referents for equal-unit clocks; linear PK before tmax; moderator sign intuition; PD35 information ceiling; sparse sampling warning | Cards 1–4, §5, §8 and mastery notes | PRESENT_EXPANDED | Augmentations visibly labeled. |
| C8 Deprecated draft regression | No unsupported NDA narrative, NONMEM syntax expansion, added case studies, §3.10/§3.12/§3.14 creep | Part A and guardrails | PRESENT | Rejected material remains excluded. |
| C9 Canonical integrity | Content Lock v2 §1–§8 retained with approved markers/micro-patch/augmentations only | Part A | PRESENT | Ver2 restorations applied without rewriting locked text; restored items use textbook-verified anchors. |

**Zero-Omission Certificate (ver2):** PASS. All ver1 unresolved high-impact omissions resolved by C4-3 through C4-11.

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

**Mastery-Uplift Certificate (ver2):** PASS. Augmentations are bounded, visibly labeled, source-aware, and do not create new numerical values or new named examples outside Scope/Audit/Crucible. The §6 diagnostic catalog uses only patterns whose existence is supported by textbook data (G&W §3.9.7 / PD13 / PD35) and assigns *names* to those patterns as pedagogical mnemonics, with the source-boundary caveat stated in §6 itself.

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
- Self-Test §7 now contains 10 questions (Q1–Q10). All ten must be rendered as click-to-reveal accordions with answers hidden by default.

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
- Q10 boss-dilemma 7–8 paragraph regulatory narrative from Step 1 Draft v0 (replaced by compressed Q8 in §7).

### B11. Source-Boundary and HTML-Readiness Certificates (ver2)

| Certificate | Status | Basis |
|---|---|---|
| Required files present | PASS | Scope Lock, PDFs, Audit, Crucible, Content Lock v2, v2.1 patch, compiler prompt, Step 1, patch memo all present. |
| PDF use boundary | PASS | PDFs used only as verification/source-boundary anchors; no image reproduction. |
| Figure rights | PASS | Image rights = None; pointer-only for textbook figures. |
| PART A standalone learner body | PASS_EXPANDED | Learner Navigation Aid + full scientific §§1–§8 + new §6 Diagnostic Lens + figure markers + micro-patch + mastery notes. |
| Compiler readiness | PASS | Marker mapping, source-page tag rules, navigation anchor rules, CSS/JS constraints, figure rules, prohibited items included. §6 sub-id navigation specified. |
| Navigation anchor integrity requirement | PASS for instruction | Phase 5 must implement sticky left sidebar, stable ids, no duplicate ids, and href/id self-check before output. |
| Zero-Omission gate (ver2) | PASS | All ver1 unresolved high-impact omissions (PD13 Model I/II/III table, Eq.3:204, AUC asymmetry, hysteresis collapse method, Card 3 clinical anchors, R&T-anchored Self-Test items, GOF catalog) are restored or added as bounded labeled augmentations. |
| Mastery-Uplift gate (ver2) | PASS | Wall 1, Wall 2, Wall 3 (now strengthened), Wall 4 all explicit; GOF signature dictionary in §6 names four diagnostic patterns; escalation cascade explicit in §1. |
| Source-Boundary gate (ver2) | PASS | All textbook-derived items use verified anchors. All non-textbook items labeled [교과서 외 실무 해석] / [구조적 비유 — 교과서 외 확장] / [구현 번역] / EXPERT_INFERENCE / CRUCIBLE_DERIVED. §6's source-boundary note opens the section. |
| Splice Verification (ver2) | PASS | All seven figure markers present exactly once; positions and anchor strings unchanged from ver1. |

**Final Go-Decision Verdict (ver2):** GO. Master file is ready for Phase 5 HTML compilation.

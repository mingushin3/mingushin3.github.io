# 02_HTML Compile Input Master

## Phase 4D Certification

| Certificate | Status | Basis |
|---|---|---|
| Learner-Standalone Certificate | PASS | PART A contains navigation aid plus §1-§8 learner body only; audit/compiler/process material is isolated in PART B. |
| Zero-Omission Certificate | PASS | Scope MUST concepts, Audit MUST_FIX/SHOULD_FIX, retained figure pointers, page tags, and adopted Crucible Grade A logic are present or justifiably compressed. |
| Mastery-Uplift Certificate | PASS | PART A contains 8 bounded, adjacent, source-labeled augmentation blocks for this A-Critical chapter. |
| Source-Boundary Certificate | PASS | Augmentations are labeled TEXTBOOK_DERIVED, AUDIT_DERIVED, CRUCIBLE_DERIVED, or EXPERT_INFERENCE and add no new page tags or unsupported numerical claims. |
| HTML-Readiness Certificate | PASS | PART B contains Phase 5 rendering contract, marker mapping, page-tag rules, figure rules, audit/crucible guardrails, and navigation integrity rules. |

## Assembly Mode

**FULL MODE** — `02_Content Lock v2.1(1).md` is complete and already contains the retained Phase 4C figure markers. No PATCH MODE splicing was required.

## Input Manifest

| File | Role | Authority level | Used for | Notes |
|---|---|---|---|---|
| 붙여넣은 텍스트 (1)(75).txt | Phase 4D assembly prompt | A7 | compiler/master assembly instruction | Renamed target from 05 to 02 to match user request. |
| 붙여넣은 마크다운(2)(51).md | Step 2 HTML Compiler prompt / Prompt 5 | A7 | HTML rendering requirements and guardrails | Used in PART B only. |
| 02_scope_lock(4).md | Scope Lock | A0 | scope boundary, learner, mode, source range, hard limits | Defines A-Critical session and PDF ranges. |
| 02_T_분포의 생물학 Vd·막투과·단백결합(5).pdf | Original R&T textbook PDF | A1 | PDF verification source | R&T Ch.4 p.77-118; App.B/C/D. |
| 02_G_분포의 생물학 Vd·막투과·단백결합(5).pdf | Original G&W textbook PDF | A1 | PDF verification source | G&W §2.9.3-2.9.5 and PK47. |
| 02_Audit_Report_v1(3).md | Audit Report v1 | A2 | audit guardrail and correction checklist | Controls MUST_FIX/SHOULD_FIX and rejected material. |
| 02_Content Lock v2(3).md | Content Lock v2 | A3 | locked reference / fallback canonical body | Used as regression reference; v2.1 available. |
| 02_Content Lock v2.1(1).md | Content Lock v2.1 | A4 | canonical learner body and figure markers | FULL MODE source for PART A. |
| 02_crucible_report_v1(2).md | Crucible Report v1 | A5 | crucible guardrail and accepted insight source | Used only for adopted Grade A logic / augmentation source labels. |
| 02_step1_draft_v0(3).md | Step 1 Draft v0 | A6 | deprecated source / regression check | Not copied into PART A except through locked Content Lock material. |
| 02_Content_Lock_v1(2).md | Content Lock v1 | locked reference | historical adjudication reference | Used for consistency check only. |
| S02_phase1_patch memo(3).md | Phase 1 Patch Memo | audit support | patch attention / guardrail source | Used to confirm known risks were resolved. |

## PART A — Learner-Facing Complete Handout

## Learner Navigation Aid

### How to Use This Handout

1. Read §1 to fix the single governing question: which concentration species and which binding compartment are being interpreted?
2. Study §2 in order. M1 explains whether drug can cross membranes, M2 explains how fast distribution proceeds, M3 explains what V means, M4 and M5 explain plasma/tissue binding, and M6 explains which exposure metric is defensible.
3. Use the `FIGURE_POINTER` blocks as textbook-look-up prompts. They do not reproduce copyrighted textbook figures.
4. Finish with §5 and §7. These sections are designed to expose the common failure modes before HTML rendering.

### Learning Route

M1 membrane permeability → M2 distribution rate limitation → M3 apparent V structure → M4 plasma protein binding and concentration-dependent fu → M5 tissue binding/Kp/transporter → M6 total vs unbound exposure → §5 Critical Blow → §7 self-test → §8 professional synthesis.

### Before You Start Checklist

- I can distinguish total concentration `C` from unbound concentration `Cu`.
- I know that apparent volume is not a physical organ volume.
- I will treat textbook figure markers as pointers, not as embedded images.

### After You Finish Checklist

- I can explain why `Cu`, not total `C`, drives passive membrane diffusion.
- I can separate distribution extent from distribution rate.
- I can use `Vp + tissue term`, `Kp`, and `fu/fuT` as interchangeable lenses only when their assumptions are satisfied.
- I can state when `AUCu = AUC × fu` is safe and when it is not.
- I can defend a total vs unbound exposure metric choice without restoring unsupported regulatory claims.


---

## §1 — Session Header & Roadmap

### Big Idea

<!-- MASTER LENS -->
분포용적은 실제 장기 부피가 아니다. **Amount in body를 concentration으로 나누기 위해 도입한 apparent proportionality constant<!-- ANNOTATION --> (← 실제 부피가 아닌 계산상 비례상수)**이다. 따라서 이 상수는 대체로 `plasma binding(fu)`가 약물을 혈장 쪽에 붙잡는 힘과 `tissue binding(fuT/Kp)`이 조직 쪽으로 끌어당기는 힘의 균형으로 결정된다. [R&T pp.102–111]

> **Mastery Note — EXPERT_INFERENCE**  
> 이 handout을 읽을 때는 모든 concentration 기호 앞에 “which species?”를 붙여서 해석한다. 같은 데이터라도 total scale, unbound scale, blood scale, tissue scale 중 무엇을 보고 있는지 바뀌면 V, CL, exposure-response 판단이 달라진다.

### Concept Navigation

```text
M1 막투과 결정인자
  → M2 분포 율속: perfusion-limited인가 permeability-limited인가?
  → M3 Vd의 수학 구조 [Apex]
  → M4 plasma binding과 fu 농도의존성
  → M5 tissue binding, Kp, transporter
  → M6 total vs unbound exposure 선택
  → §5 Critical Blow: C vs Cu
```

### Knowledge Graph Position

- 이전 세션의 `C(t) = (Dose/V)·e^{-kt}`에서 $V$가 무엇인지 해부하는 장이다.
- 다음 elimination 세션에서는 $f_u$가 well-stirred hepatic clearance 식의 분자로 들어간다.
- PopPK에서는 albumin, α1-AGP, renal/liver disease covariate가 `V`, `CL`, 또는 `fu`에 어떤 방향으로 연결되는지 판단하는 기반이 된다.

---

## §2 — Concept Anatomy Cards

---

### M1 · 막투과의 결정인자

<!-- MASTER LENS -->
**핵심 직관**: 막투과는 “lipophilic이면 통과한다”로 끝나지 않는다. 실제 permeability는 **size × lipophilicity × charge × transporter**가 함께 만든다. Eq.4-1의 $P$는 이 네 축과 막 구조가 한 숫자로 접힌 macroscale permeability이다. [R&T pp.80–84, 85–90]

#### A. Formal Definition

막 양쪽 수성구획의 unbound concentration<!-- ANNOTATION --> (← 단백질에 결합하지 않은 농도)이 각각 $Cu_1$, $Cu_2$일 때 net transport rate는 다음과 같다.

$$\text{Net rate of transport}=P\cdot SA\cdot(Cu_1-Cu_2)$$

[출처: R&T Eq.4-1, p.80]

Bound drug은 일반적으로 막을 통과하지 못한다. 따라서 막투과의 driving force는 total concentration $C$가 아니라 unbound concentration $Cu$이다. [R&T p.80]

#### B. Source-Anchored Details

- **Size**: 같은 lipophilicity에서 MW 400 → 800 g/mol로 증가하면 skin permeability는 약 300-fold 낮아진다. [R&T Fig.4-3, p.81–82] Atenolol 246 g/mol은 GI absorption이 가능하지만, oxytocin 1007 g/mol은 GI membrane을 거의 통과하지 못하고, calcitonin-salmon 3432 g/mol은 nasal absorption도 약 3% 수준이다. [R&T p.81]
- **Lipophilicity**: BBB permeability는 대체로 n-octanol/water partition coefficient가 증가할수록 증가한다. 단, vinblastine·vincristine은 lipophilicity만으로 기대되는 값보다 낮은 permeability를 보이는데, 원문은 P-glycoprotein efflux substrate임을 주요 이유로 든다. [R&T Fig.4-4, p.82] “100배” 같은 배수는 시각 추정 [확인 필요]로만 취급한다.
- **Charge / pH partition**: 약산·약염기에서는 un-ionized form이 lipoidal membrane을 주로 통과한다. 평형에서 un-ionized 농도는 같아질 수 있지만, pH와 pKa에 따라 total concentration은 달라진다. [R&T p.83; App.B pp.763–765]
- **Transporter**: passive facilitated transporter는 equilibrium 도달 속도를 바꾸고, active transporter는 steady-state unbound ratio 자체를 바꿀 수 있다. Active transport가 있을 때:

$$\frac{Cu_T}{Cu}=\frac{P_{uptake}}{P_{efflux}}$$

[출처: R&T Eq.4-26, p.110]

<!-- TRENCH -->
**Trench-Level Tip**: logP와 MW가 좋아도 P-gp/BCRP efflux substrate이면 BBB 또는 gut wall에서 effective permeability가 크게 낮아질 수 있다. 단, Caco-2/PAMPA, Lipinski rule은 이 source 범위 밖이므로 본 handout에서는 삭제한다.

> **Failure Mode — AUDIT_DERIVED**  
> logP 하나로 BBB 또는 tissue permeability를 예측하려고 하면, size·ionization·efflux transporter가 만드는 예외를 놓친다. 특히 이 세션에서는 “lipophilicity = permeability”가 아니라 “effective permeability = physicochemistry + membrane + transporter”로 읽어야 한다.

<!-- ANCHOR -->
막을 통과하는 성질이 정해지면, 다음 질문은 “조직으로 가는 속도가 blood flow에 의해 제한되는가, membrane 자체에 의해 제한되는가?”이다.

<!-- FIGURE_POINTER -->
Source: R&T 5e, p.82, Fig.4-4
Why this matters: BBB permeability가 logP만으로 결정되지 않고 size/efflux 예외를 갖는다는 점을 실제 좌표로 보여준다.
When to look: after reading this card
Learner instruction: caffeine, lomustine, vinblastine/vincristine의 위치를 비교하라.
<!-- /FIGURE_POINTER -->

---

### M2 · 분포의 율속 단계

<!-- MASTER LENS -->
**핵심 직관**: 조직 분포에서는 “얼마나 많이 가는가”와 “얼마나 빨리 가는가”를 분리해야 한다. Tissue affinity가 커지면 equilibrium extent는 커진다. 그러나 채워야 할 tissue amount도 커지므로 equilibrium time은 오히려 길어질 수 있다. [R&T pp.94–100]

#### A. Formal Definition

Perfusion-rate limited distribution<!-- ANNOTATION --> (← 혈류 공급이 속도 제한)에서는 membrane crossing이 충분히 빠르다. 이때 조직으로 들어가는 공급 속도는 blood flow가 결정하고, tissue concentration의 접근은 mono-exponential 형태를 따른다.

$$k_T=\frac{Q/V_T}{K_{pb}}$$

$$t_{1/2,distribution}=\frac{0.693\cdot K_{pb}}{Q/V_T}$$

$$C_T(t)=K_{pb}\cdot C_A\cdot(1-e^{-k_Tt})$$

[출처: R&T Eq.4-5~4-7, p.97]

#### B. Source-Anchored Details

| Tissue | Perfusion rate, mL/min/g | 해석 |
|---|---:|---|
| Lung | 10.0 | 매우 빠른 equilibrium 가능 |
| Kidney | 4.0 | flow-rich organ |
| Brain | 0.5 | flow는 높지만 BBB permeability가 별도 제한 가능 |
| Adipose | 0.025 | 매우 낮은 flow → high Kp 약물에서 늦은 equilibration |
| Inactive muscle | 0.025 | 큰 tissue mass + 낮은 perfusion |

[출처: R&T Table4-4, p.96]

- **Thiopental dog 25 mg/kg IV bolus**: brain은 빠르게 오르고 빠르게 빠지는 반면, fat은 low perfusion/high affinity 때문에 after 3 h에도 상당량이 남는다. exact “3.5 h equilibrium”은 author-stated value가 아니므로 삭제한다. [R&T Fig.4-13, p.94]
- **Macromolecule/lymphatic extreme**: large molecule은 혈관 벽 passage가 제한되며 lymphatic drainage가 중요한데, 원문 caption은 lymph flow를 `1–10 mL/min per 70 kg`로 제시한다. [R&T Fig.4-14, p.95] MW >5000 g/mol에서는 permeability limitation과 lymphatic return이 분포 속도를 크게 늦출 수 있다. [R&T Table4-1, p.84; Fig.4-14, p.95]
- **Ribitol and penicillin G**: small polar compound도 조직별 permeability에 따라 mixed limitation을 보이고, penicillin G는 muscle과 달리 brain/CSF에서 permeability limitation이 두드러진다. [R&T Fig.4-17 p.99; Fig.4-18 p.100]

#### C. Boundary Conditions

- Eq.4-5~4-7은 **perfusion-rate limited** 가정에서만 안전하다.
- permeability-rate limited tissue에서는 $Q$를 올려도 distribution rate가 비례해서 증가하지 않는다.
- High $K_{pb}$는 “많이 간다”와 동시에 “평형 도달이 늦다”를 의미할 수 있다.

> **Practice Lens — CRUCIBLE_DERIVED**  
> 분포 문제를 볼 때는 먼저 extent와 rate를 분리한다. V 또는 Kp는 “얼마나 많이”를 말하고, Q/VT와 permeability는 “얼마나 빨리”를 말하므로, onset 또는 sampling-time 문제를 equilibrium parameter만으로 설명하지 않는다.

<!-- RECAP -->
**M2 recap**: distribution half-life는 blood flow, tissue size, tissue affinity의 함수이다. 큰 $K_{pb}$와 낮은 $Q/V_T$가 만나면 distribution은 느려진다.

<!-- FIGURE_POINTER -->
Source: R&T 5e, p.94, Fig.4-13
Why this matters: thiopental에서 brain과 fat의 time-course 차이가 perfusion과 affinity의 결합 효과임을 보여준다.
When to look: after reading this card
Learner instruction: brain peak와 fat 잔류를 비교하라.
<!-- /FIGURE_POINTER -->

---

### M3 · 분포용적의 수학 구조 **[Apex Concept]**

<!-- MASTER LENS -->
**핵심 직관**: $V$는 실제 부피가 아니라 `Amount/C`이다. 작은 Vd의 albumin-bound 산성 약물에서는 albumin이 ferry처럼 약물을 plasma와 extravascular albumin space로 운반한다. $f_u\to0$이면 약물은 그 ferry에서 거의 내리지 않는다. 이 때문에 apparent V는 albumin distribution volume인 약 7.5 L 근처에서 floor를 갖는다. [R&T pp.111–113; App.C pp.767–773]

#### A. Formal Definition

$$V=\frac{\text{Amount in body}}{C}=\frac{A}{C}$$

[출처: R&T Eq.4-8, p.102]

Tissue/plasma equilibrium ratio $K_p$를 쓰면:

$$A=V_p\cdot C+V_T\cdot K_p\cdot C$$

$$V=V_p+V_T\cdot K_p$$

$$V=V_p+\sum_i V_{T,i}\cdot K_{p,i}$$

[출처: R&T Eq.4-11~4-13, pp.103–104]

측정 matrix가 바뀌면 apparent volume도 달라진다.

$$V_u=\frac{A}{C_u},\qquad V_b=\frac{A}{C_b}$$

[출처: R&T Eq.4-14~4-15, p.104]

#### B. Binding-Based Structure

Plasma/tissue unbound fraction으로 쓰면:

$$V=V_p+V_{TW}\cdot\frac{f_u}{f_{uT}}$$

[출처: R&T Eq.4-25, p.109]

<!-- ANNOTATION --> 여기서 $K_p$를 $f_u/f_{uT}$로 바꾸어 쓰는 이유는, 같은 amount라도 plasma에 남는 비율과 tissue에 붙는 비율이 서로 다르기 때문이다. 이 전환이 “V가 왜 binding의 함수인가”를 보여준다.

Transporter가 tissue distribution을 지배하면:

$$V=V_p+V_{TW}\cdot\frac{f_u}{f_{uT}}\cdot\frac{P_{uptake}}{P_{efflux}}$$

[출처: R&T Eq.4-29, p.111]

Small-Vd albumin-bound drug model에서는:

$$V=7.5+\left(7.5+\frac{V_R}{f_{uR}}\right)\cdot f_u$$

[출처: R&T Eq.4-30, p.112; App.C Eq.C-13, pp.767–773]

#### C. Source-Anchored Data Anchors

- Plasma 3 L, extracellular water 16 L, total body water 42 L는 V 해석의 physiologic anchor다. [R&T p.111]
- Albumin apparent distribution volume은 약 7.5 L이며, cephalosporin Fig.4-25에서 $f_u\to0$ extrapolation intercept가 약 7 L로 보인다. [R&T Table4-5 p.101; Fig.4-25 pp.112–113]
- 같은 cephalosporin series에서 $V$는 $f_u$와 함께 증가하지만, $V_u$는 $f_u$가 증가할수록 감소한다. 이 paired message가 “total concentration 기준 V”와 “unbound concentration 기준 V”가 같은 생리적 의미가 아님을 보여준다. [R&T Fig.4-25~4-26, p.113]
- Warfarin nephrotic syndrome 예시: albumin 43→12.5 g/L, V 9.4→13.7 L, CL 0.20→0.58 L/hr, t1/2 36→18 hr. [R&T Table4-12, p.118]
- Adalimumab 같은 high MW antibody는 V가 약 5–6 L로 작고, caffeine/alcohol처럼 small freely permeating molecule은 V가 total body water에 접근한다. [R&T p.111]

#### D. Apex Fallacy

“$f_u$가 증가하면 unbound concentration이 증가하므로 loading dose를 올려야 한다”는 직관은 small-Vd albumin-bound drug에서 틀릴 수 있다. 같은 amount에서 $f_u$가 증가하면 total $C$는 낮아지고 $V$는 증가한다. 그러나 $C_u$는 반드시 같은 방향으로 증가하지 않는다. R&T의 cephalosporin/warfarin 논리는 이 함정을 정면으로 다룬다. [R&T pp.112–118]

<!-- TRENCH -->
**[교과서 외 실무 해석] Albumin covariate asymmetry**: large-Vd drug에서 albumin을 `V` covariate로만 넣고 `CL` 쪽을 보지 않으면 total concentration 기준 CL 변화가 누락될 수 있다. ETA-CL vs albumin 관계가 ETA-V vs albumin보다 강하면 CL covariate도 검토한다.

**[교과서 외 실무 경고] Vss vs Vβ**: multi-compartment model에서 loading dose는 Vss 기반, terminal half-life 해석은 Vβ 기반이라는 구분을 유지한다.

> **Mastery Note — CRUCIBLE_DERIVED**  
> Albumin 변화가 보이면 바로 “dose를 바꿀까?”로 가지 말고, total C, Cu, V, CL 중 어느 관찰값이 움직였는지 먼저 분해한다. 이 순서를 지키면 hypoalbuminemia 상황에서 total concentration 변화와 active exposure 변화를 혼동하지 않는다.

<!-- RECAP -->
**M3 recap**: $V$는 `Vp + tissue term`이며, tissue term은 $K_p$ 또는 $f_u/f_{uT}$로 읽을 수 있다. Small-Vd albumin-bound drug에서는 albumin distribution volume이 floor를 만든다.

<!-- FIGURE_POINTER -->
Source: R&T 5e, p.113, Fig.4-25 and Fig.4-26
Why this matters: 같은 cephalosporin series에서 V와 Vu가 fu에 대해 반대 방향으로 읽힐 수 있음을 보여준다.
When to look: after reading this card
Learner instruction: V-fu와 Vu-fu 축을 나란히 비교하라.
<!-- /FIGURE_POINTER -->

---

### M4 · 혈장단백결합과 fu의 농도의존성

<!-- MASTER LENS -->
**핵심 직관**: $f_u$는 고정 상수가 아니다. Protein concentration, binding affinity, binding site 수, unbound concentration의 함수다. 따라서 “total concentration ↔ unbound concentration” 변환은 $f_u$가 일정하다는 검증 위에서만 안전하다. [R&T pp.105–108; G&W pp.690–693]

#### A. Formal Definition

$$f_u=\frac{C_u}{C}$$

[출처: R&T Eq.4-17, p.105]

Single binding site에서 association constant는:

$$K_a=\frac{C_{b,t}}{C_u\cdot P}$$

[출처: R&T Eq.4-18, p.105]

R&T의 mass-law relationship은 protein concentration과 binding site occupancy가 $f_u$를 바꾼다는 점을 보여준다.

$$f_u=\frac{1}{1+K_a\cdot f_{up}\cdot P_t}$$

[출처: R&T Eq.4-19, p.105]

#### B. PK47 Source-Anchored Data

G&W PK47은 $f_u$를 $C_u$, total protein concentration $[P_T]$, site number $n$, affinity $K_a$의 함수로 모델링한다.

$$f_u=1-\frac{1}{1+\frac{C_u}{n[P_T]}+\frac{1}{K_a\cdot n[P_T]}}$$

[출처: G&W Eq.47:1, p.691]

Low-$C_u$ approximation:

$$f_u\approx\frac{1}{1+K_a\cdot n[P_T]}$$

[출처: G&W Eq.47:3, p.692]

G&W는 Compound 1에서 $[P_T]=50$과 0.3, Compound 2에서 $[P_T]=10$과 0.1 조건을 사용하고, $n$은 대략 1–4 범위, $K_a$는 Eq.47:4 초기 추정으로 약 6 concentration units 수준을 제시한다. [G&W Table47.1 p.692; Eq.47:4 p.693]

#### C. Boundary Conditions

- Eq.47:1은 single binding-site class 모델이다. multiple site class가 있으면 residual pattern이 systematic하게 남을 수 있다.
- $AUCu=AUC\times f_u$는 $f_u$가 시간·농도에 대해 충분히 일정할 때만 안전하다. [G&W p.167]
- G&W는 `fub > 1`이 가능하다고 명시한다; 이는 bound/free ratio이므로 fraction bound와 혼동하면 안 된다. [G&W p.168]

<!-- TRENCH -->
**[교과서 외 실무 해석] Protein covariate choice**: acidic drug는 albumin, basic drug는 α1-AGP 변화에 먼저 주목한다. R&T Table4-9는 albumin과 α1-AGP가 disease state에 따라 달라질 수 있음을 보여준다. [R&T Table4-9, p.114]

**[교과서 외 실무 경고] PPB method bias**: equilibrium dialysis와 ultrafiltration은 method bias가 다를 수 있다. 이 문장은 PDF 원문이 아니라 실험 데이터 수령 단계의 실무 주의로만 사용한다.

> **Practice Lens — TEXTBOOK_DERIVED**  
> Total AUC에 단일 fu를 곱하기 전에는, 그 fu가 의사결정에 쓰는 농도 범위에서 유지되는 값인지 확인한다. PK47의 핵심은 binding parameter fit 자체보다 “conversion shortcut의 안전 조건”을 드러내는 데 있다.

<!-- RECAP -->
**M4 recap**: $f_u$는 protein concentration과 binding site saturation에 따라 변할 수 있다. total-to-unbound conversion은 $f_u$ constant assumption이 무너지면 함께 무너진다.

<!-- FIGURE_POINTER -->
Source: G&W 5e, p.691, Fig.47.1
Why this matters: fu가 Cu와 protein concentration에 따라 변하는 비선형 binding curve를 직접 보여준다.
When to look: after reading this card
Learner instruction: low/high protein curves가 n과 Ka 추정에 주는 정보를 확인하라.
<!-- /FIGURE_POINTER -->

---

### M5 · 조직결합과 Kp의 결정인자

<!-- MASTER LENS -->
**핵심 직관**: 큰 Vd는 “plasma에서 많이 풀려 있다”는 뜻이 아닐 수 있다. 오히려 “tissue에서 더 강하게 붙잡힌다”는 신호인 경우가 많다. Basic drug의 큰 Vd는 plasma binding보다 tissue binding, 특히 acidic phospholipid affinity로 설명되는 경우가 많다. [R&T pp.108–111]

#### A. Formal Definition

Tissue-to-plasma equilibrium distribution ratio $K_p$<!-- ANNOTATION --> (← 조직/혈장 평형 농도비)는 tissue concentration과 plasma concentration의 평형 비율이다. R&T는 Eq.4-25와 Eq.4-12를 비교해 $K_p\sim f_u/f_{uT}$로 해석할 수 있음을 설명한다. [R&T pp.104, 109–110]

#### B. Source-Anchored Details

- Furosemide와 amiodarone은 plasma $f_u$가 비슷한 범위일 수 있으나 V는 크게 다르다. 차이는 basic drug의 높은 tissue binding, 즉 낮은 $f_{uT}$에서 온다. [R&T p.110]
- Propranolol은 6 controls + 15 chronic hepatic disease patients에서 40 mg IV bolus 후 $V$와 $f_u$의 관계가 제시된다. 이는 plasma binding 변화가 $V$ 변동을 설명할 수 있음을 보여준다. [R&T Fig.4-23, p.110]
- Metoprolol tissue $K_p$는 tissue acidic phospholipid concentration과 강한 positive relationship을 보인다. Exact `r>0.85`는 원문에 없으므로 삭제한다. [R&T Fig.4-24, p.110]
- Indinavir 800 mg q8h HIV adults 8명에서 CSF unbound concentration은 plasma unbound보다 낮고 지연되며 fluctuation이 작다. Exact “1/10”은 approximate visual estimate로만 취급한다. [R&T Fig.4-10, p.91]
- Brain은 whole-body mass의 약 2%이므로 local transporter effect가 whole-body V를 크게 바꾸지 않을 수 있다. [R&T pp.109, 111]

#### C. Plasma-to-Blood Context

Appendix D의 핵심은 blood/plasma concentration ratio가 hematocrit, plasma fu, red cell binding에 의해 달라진다는 점이다.

$$\frac{C_b}{C}=1+H\left(f_u\cdot K_{PBC}-1\right)$$

[출처: R&T App.D, pp.775–776]

#### D. Boundary Condition

Transporter가 지배적이면 tissue unbound concentration과 plasma unbound concentration이 자유롭게 평형을 이룬다는 단순 $f_{uT}$ 해석이 깨질 수 있다. BBB의 efflux transporter가 대표적인 예다. [R&T pp.90–91, 110–111]

> **Failure Mode — CRUCIBLE_DERIVED**  
> Eq.4-29에서 binding term과 transporter term을 같은 종류의 원인으로 합쳐 해석하면 안 된다. fuT는 tissue binding을, Puptake/Pefflux는 active distribution imbalance를 나타내므로, 둘은 같은 V 변화를 만들 수 있어도 실험적 확인 방법과 모델링 의미가 다르다.

<!-- RECAP -->
**M5 recap**: $K_p$는 tissue affinity의 숫자 표현이고, $f_{uT}$는 tissue binding의 inverse signal이다. Transporter가 있으면 $K_p$는 binding뿐 아니라 uptake/efflux imbalance까지 반영한다.

---

### M6 · 노출 지표 선택: total vs unbound

<!-- MASTER LENS -->
**핵심 직관**: exposure metric은 “하나의 AUC 숫자”가 아니다. 어떤 concentration species가 어떤 시간 패턴으로 pharmacology를 만든다는 주장이다. Total concentration이 protein binding 차이에 confounded되면 unbound concentration이 active comparator가 된다. [G&W pp.163–169]

#### A. Formal Definition

Total and unbound concentration 관계:

$$C=\frac{C_u}{f_u}$$

$f_u$가 일정하면:

$$AUC_u=AUC\times f_u$$

[출처: G&W Eq.2:373, p.167]

#### B. Source-Anchored Details

<!-- ANNOTATION --> 따라서 M6의 질문은 “AUC를 쓸 것인가?”가 아니라 “어떤 species의 AUC 또는 시간 패턴을 쓸 것인가?”이다.

- G&W Fig.2.134는 dose-response, total concentration-response, unbound concentration-response가 서로 다른 결론을 낼 수 있음을 보여준다. Total concentration 관계는 plasma protein binding 차이에 confounded되고, unbound concentration 기준에서는 potency order가 뒤집힌다. [G&W p.163]
- G&W Fig.2.136은 같은 AUC라도 peak, duration above threshold, toxicity implication이 다를 수 있음을 경고한다. “equal AUC = equal effect”는 process shape을 잃는 단일 scalar shortcut이다. [G&W p.164]
- G&W Fig.2.140은 $f_u$를 total concentration보다 $C_u$에 대해 그릴 때 더 명확한 관계를 보일 수 있음을 제시한다. [G&W p.167]
- G&W Fig.2.141은 dog/rat/mouse total concentration-response curve는 다르게 보이나 unbound ECu50가 약 2 nM 부근으로 정렬될 수 있음을 보여준다. Total potency fold는 visual/inferred estimate로만 다룬다. [G&W p.168]
- G&W Table2.21은 exposure metric을 `Cmax`, `AUC`, `td`, treatment period 등으로 나누고, 각 metric의 적용 상황을 구분한다. [G&W p.169]
- G&W는 456 drugs 검토를 인용하며 protein binding change가 PK parameters에는 영향을 줄 수 있으나 clinical outcome에는 대개 큰 영향을 주지 않고, 예외는 IV high-extraction drug with narrow therapeutic window라고 정리한다. [G&W p.168]
- G&W 결론: IND 단계에서는 여러 concentration과 species(including human)에서 ex vivo plasma protein binding을 측정하고, NDA 단계에서는 selected clinical studies에서 unbound와 total concentration을 함께 얻는 것이 권장된다. Routine “good to have” 측정은 지양한다. [G&W p.169]

#### C. Boundary Conditions

- $f_u$가 dose-, time-, concentration-dependent이면 $AUC_u=AUC\times f_u$ shortcut은 무효가 될 수 있다.
- Total AUC가 같아도 peak-driven toxicity 또는 duration-above-threshold effect는 다를 수 있다. [G&W Fig.2.136, p.164]
- “unbound를 항상 측정하라”가 아니라 “의사결정이 unbound species에 민감한 상황에서 측정하라”가 G&W의 결론이다. [G&W p.169]

> **Practice Lens — TEXTBOOK_DERIVED**  
> Exposure metric은 보고서의 숫자 선택이 아니라 causal claim의 선택이다. AUC, Cmax, td 중 무엇을 전면에 둘지는 “효과를 만든 시간 패턴이 무엇인가”와 “total과 unbound 중 어떤 species가 비교 가능한가”를 함께 답해야 정당화된다.

<!-- RECAP -->
**M6 recap**: total concentration은 assay-friendly metric이고, unbound concentration은 active species에 가까운 metric이다. 어느 쪽을 쓸지는 binding 차이, species extrapolation, exposure shape, decision risk가 결정한다.

<!-- FIGURE_POINTER -->
Source: G&W 5e, p.163, Fig.2.134
Why this matters: dose, total concentration, unbound concentration이 서로 다른 potency 결론을 만들 수 있음을 보여준다.
When to look: after reading this card
Learner instruction: total-response와 unbound-response에서 potency order가 어떻게 바뀌는지 확인하라.
<!-- /FIGURE_POINTER -->

---

## §5 — Confusion Pair Dissection

### Confusion Pair 1 — C vs Cu **[Critical Blow]**

<!-- CONFUSION -->
| 구분 | C, total concentration | Cu, unbound concentration |
|---|---|---|
| 정의 | bound + unbound | unbound only |
| 막투과 driving force | 부적합 | 적합 [R&T p.80] |
| Exposure-response | PPB 차이에 confounded 가능 | active species 비교에 유리 [G&W pp.163, 167–168] |
| Shortcut | assay가 쉬움 | fu 측정 또는 모델 필요 |
| 실패 모드 | species/compound potency order가 왜곡됨 | fu가 time-dependent이면 계산 오류 가능 |

<!-- MASTER LENS -->
Critical Blow는 “C와 Cu 중 무엇이 참인가?”가 아니다. 핵심 질문은 **지금 의사결정의 causal species가 무엇인가?**이다. 막투과, receptor interaction, species extrapolation이 문제이면 $Cu$가 더 직접적이다. 하지만 $f_u$가 안정적이고 decision이 total assay 기반으로 검증되어 있다면 $C$도 유용하다.

> **Practice Lens — EXPERT_INFERENCE**  
> C vs Cu 판단은 네 단계로 고정한다: causal species → assay scale → conversion validity → decision risk. 이 순서가 없으면 “unbound가 더 맞다”와 “total도 충분하다”가 둘 다 근거 없는 주장으로 변한다.

### Confusion Pair 2 — Perfusion-rate vs Permeability-rate limitation

<!-- CONFUSION -->
Perfusion-rate limitation에서는 blood flow가 속도를 정하고 Eq.4-5~4-7이 안전하다. Permeability-rate limitation에서는 membrane passage가 bottleneck이며, brain penicillin G나 macromolecule lymphatic distribution처럼 blood flow만으로 설명되지 않는다. [R&T pp.94–100]

### Confusion Pair 3 — fu vs fuT

<!-- CONFUSION -->
$f_u$는 plasma에서 unbound fraction이고, $f_{uT}$는 tissue에서 unbound fraction이다. $V=V_p+V_{TW}(f_u/f_{uT})$이므로 $f_u$가 커지면 V는 커질 수 있고, $f_{uT}$가 작아지면 V는 크게 커진다. [R&T Eq.4-25, p.109]

### Confusion Pair 4 — Small Vd vs Large Vd response to protein binding

<!-- CONFUSION -->
Small-Vd albumin-bound drugs에서는 albumin distribution model과 7.5 L floor가 필요하다. Large-Vd basic drugs에서는 tissue binding이 지배적이므로 plasma protein binding 변화만으로 V와 Cu를 해석하면 위험하다. [R&T pp.111–118]

---

## §7 — Self-Test: Active Recall Module

### Q1
<!-- SELF-TEST -->
Eq.4-1에서 concentration difference가 $C_1-C_2$가 아니라 $Cu_1-Cu_2$인 이유는?

**Answer**: bound drug은 일반적으로 막을 통과하지 못하고, unbound drug만 diffusion driving force가 되기 때문이다. [R&T p.80]

### Q2
<!-- SELF-TEST -->
MW 400→800 g/mol 증가와 logP 증가가 permeability에 미치는 방향을 각각 말하라.

**Answer**: MW 증가는 permeability를 크게 낮추고, logP 증가는 대체로 permeability를 높인다. 단 transporter substrate이면 logP 예측이 깨질 수 있다. [R&T Fig.4-3~4-4, pp.81–82]

### Q3
<!-- SELF-TEST -->
Perfusion-rate limited tissue에서 $K_{pb}$가 커지면 distribution half-life는 어떻게 변하는가?

**Answer**: $t_{1/2,distribution}=0.693K_{pb}/(Q/V_T)$이므로 커진다. 친화도가 크면 채워야 할 tissue amount가 많아져 equilibrium 도달이 늦어진다. [R&T p.97]

### Q4
<!-- SELF-TEST -->
Small-Vd albumin-bound drug에서 $f_u\to0$일 때 V가 0 L이 아니라 약 7.5 L 근처 floor를 갖는 이유는?

**Answer**: 약물이 albumin에 붙어 plasma와 extravascular albumin space에 분포하기 때문이다. Albumin distribution volume이 약 7.5 L floor를 만든다. [R&T p.111–113; App.C pp.767–773]

### Q5
<!-- SELF-TEST -->
Warfarin nephrotic syndrome에서 albumin 감소가 V, CL, t1/2에 어떤 방향 변화를 보였는가?

**Answer**: albumin 43→12.5 g/L에서 V 9.4→13.7 L, CL 0.20→0.58 L/hr, t1/2 36→18 hr로 변했다. [R&T Table4-12, p.118]

### Q6
<!-- SELF-TEST -->
G&W Eq.2:373의 $AUC_u=AUC\times f_u$를 쓰기 위한 핵심 조건은?

**Answer**: $f_u$가 시간·농도·dose에 대해 충분히 일정해야 한다. 그렇지 않으면 total AUC에 하나의 fu를 곱하는 shortcut이 깨진다. [G&W p.167]

### Q7
<!-- SELF-TEST -->
Equal AUC인데 toxicity가 다를 수 있는 이유는?

**Answer**: 같은 area라도 peak concentration, threshold 초과 시간($t_d$), concentration-time shape이 다를 수 있기 때문이다. [G&W Fig.2.136, p.164]

### Q8
<!-- SELF-TEST -->
PK47에서 low/high protein concentration을 동시에 fit하는 이유는?

**Answer**: $n$과 $K_a$의 correlation을 줄이고 precision을 높이기 위해서다. [G&W p.693]

### Q9 — Boss Dilemma
<!-- SELF-TEST -->
신약 후보에서 total AUC는 종간 차이가 큰데 unbound ECu50는 종간 정렬된다. 어느 exposure metric을 safety margin 논의의 중심에 놓을 것인가?

**Answer**: unbound exposure를 중심 metric으로 두되, total exposure와 $f_u$ 측정 방법을 함께 제시한다. G&W는 total concentration-response가 PPB 차이에 confounded될 수 있고, unbound concentration이 species extrapolation에서 더 적절할 수 있음을 보여준다. [G&W pp.163, 167–169]

### Q10 — [교육용 가상 사례]
<!-- SELF-TEST -->
Phase 1 SAD에서 dose-normalized AUC가 dose 증가와 함께 감소한다. Saturable clearance와 saturable PPB를 어떻게 구분할 것인가?

**Answer**: dose별 ex vivo $f_u$를 확인한다. $f_u$가 dose/Cu에 따라 증가하면 saturable PPB가 원인일 수 있고, $f_u$가 일정하면 clearance nonlinearity를 우선 의심한다. 이 문항은 교과서 수식의 실무 적용이며, 특정 PDF case는 아니다.

---

## §8 — Meta-Frame & Big Picture

### A. Positioning

<!-- MASTER LENS -->
이 세션은 **distribution을 physiology로 읽는 법**을 세운다. 이후 clearance, multiple dosing, TDM, PBPK, PopPK covariate modeling은 모두 여기서 정의된 $Cu$, $f_u$, $f_{uT}$, $K_p$, $V$ 위에 쌓인다.

### B. Dependencies

이 섹션을 약하게 이해하면 다음 오류가 발생한다.

1. **Loading dose 오류**: $V$가 apparent proportionality constant임을 잊고 physiologic volume처럼 해석한다.
2. **Covariate 오류**: albumin 변화가 total CL, total V, unbound exposure에 미치는 방향을 구분하지 못한다.
3. **Exposure metric 오류**: equal AUC를 equal effect로 가정하고 peak/duration 정보를 잃는다.
4. **Species extrapolation 오류**: total concentration-response의 potency order를 active unbound species의 potency order로 착각한다.
5. **Protein binding 오류**: $f_u$를 상수로 가정하고 saturable binding 또는 protein concentration change를 놓친다.

### C. Professional Moat

박사과정생이 이 세션에서 가져가야 할 한 문장은 다음이다.

<!-- RECAP -->
**분포는 “약물이 어디에 있는가”가 아니다. Plasma와 tissue 사이의 binding·permeability·flow가 만든 equilibrium and time-course problem이다.** Total concentration은 관찰값이고, unbound concentration은 많은 경우 causal species에 더 가깝다. $V$는 그 둘을 amount와 연결하는 apparent constant이다.

### D. System Integration Points

- **Clinical pharmacology summary**: dose-exposure linearity를 쓸 때 absorption/permeability(M1), V/dose dependence(M3), saturable PPB(M4), exposure metric(M6)이 한 문단 안에서 연결된다.
- **TDM**: hypoalbuminemia, renal failure, α1-AGP change가 동시 발생하면 total concentration만으로는 active exposure를 놓칠 수 있다.
- **NONMEM**: albumin/α1-AGP covariate는 `V`에만 기계적으로 붙이는 것이 아니라, total vs unbound scale과 CL 해석까지 함께 결정해야 한다.

---

---

## PART B — Compiler-Only Appendix

This appendix is not learner-facing. It exists only to protect Phase 5 rendering fidelity and prevent regression.

### B1. Compilation Contract

- PART A is the only learner-facing body.
- Phase 5 must render PART A without altering content.
- PART B is instruction/guardrail only.
- Do not restore deprecated material.
- Do not add new scientific content.
- Do not render PART B as learner content unless explicitly requested.
- Assembly mode for this file: **FULL MODE**. `02_Content Lock v2.1(1).md` contains the full learner body with retained Phase 4C figure markers already inserted.

### B2. Figure Rendering Instructions

- Preserve all retained figure pointer markers listed below.
- Render every `FIGURE_POINTER` as a text-only textbook reference callout.
- Because `Image rights = None`, do not embed copyrighted textbook images.
- Do not propose new figures.
- Do not generate Mermaid/SVG in Phase 4D.
- In Phase 5, figures must not interrupt reading flow; place callouts at the end of the concept card where the marker appears.

#### Approved Figure Pointer Inventory

| # | Marker | Source | Why this matters | When to look | Learner instruction |
|---:|---|---|---|---|---|
| 1 | FIGURE_POINTER | R&T 5e, p.82, Fig.4-4 | BBB permeability가 logP만으로 결정되지 않고 size/efflux 예외를 갖는다는 점을 실제 좌표로 보여준다. | after reading this card | caffeine, lomustine, vinblastine/vincristine의 위치를 비교하라. |
| 2 | FIGURE_POINTER | R&T 5e, p.94, Fig.4-13 | thiopental에서 brain과 fat의 time-course 차이가 perfusion과 affinity의 결합 효과임을 보여준다. | after reading this card | brain peak와 fat 잔류를 비교하라. |
| 3 | FIGURE_POINTER | R&T 5e, p.113, Fig.4-25 and Fig.4-26 | 같은 cephalosporin series에서 V와 Vu가 fu에 대해 반대 방향으로 읽힐 수 있음을 보여준다. | after reading this card | V-fu와 Vu-fu 축을 나란히 비교하라. |
| 4 | FIGURE_POINTER | G&W 5e, p.691, Fig.47.1 | fu가 Cu와 protein concentration에 따라 변하는 비선형 binding curve를 직접 보여준다. | after reading this card | low/high protein curves가 n과 Ka 추정에 주는 정보를 확인하라. |
| 5 | FIGURE_POINTER | G&W 5e, p.163, Fig.2.134 | dose, total concentration, unbound concentration이 서로 다른 potency 결론을 만들 수 있음을 보여준다. | after reading this card | total-response와 unbound-response에서 potency order가 어떻게 바뀌는지 확인하라. |

### B3. Page Tag Rendering Rules

- Preserve all `[p.XX]`, `[pp.XX-YY]`, `[pp.XX, YY]`, and `[p.확인 필요]` tags.
- Render page tags visibly in HTML using `span.source-page` or `span.source-page.source-uncertain`.
- Do not fabricate, delete, renumber, or relocate page tags.
- `[p.확인 필요]` remains visible unless already resolved by Audit/Content Lock.
- Do not apply source-tag regex conversion inside code blocks or inside `FIGURE_*` marker blocks.

### B4. HTML Compiler Requirements

**Core contract**

- Render PART A only. Do not render PART B as learner content unless explicitly requested.
- Render content; do not alter scientific wording, equations, page tags, or figure marker intent.
- Output one self-contained HTML document in Phase 5.
- Do not generate HTML, Mermaid, or SVG during Phase 4D.

**Marker → component mapping**

| Marker / Pattern | HTML Component | Style / behavior |
|---|---|---|
| `<!-- MASTER LENS -->` | Callout box | `border-left:4px solid #c9a84c; background:rgba(201,168,76,0.08)` |
| `<!-- ANNOTATION -->` | Inline annotation / tooltip | `font-size:0.85em; color:var(--muted); font-style:italic` |
| `<!-- ANCHOR -->` | Bridge sentence | italic, muted |
| `<!-- TRENCH -->` | Practical tip box | rose left border / rose tint |
| `<!-- CONFUSION -->` | Side-by-side comparison | `.box.amber` class or equivalent comparison styling |
| `<!-- SELF-TEST -->` | Click-to-reveal accordion | question visible; answer hidden until click |
| `<!-- RECAP -->` | Section summary box | blue left border / blue tint |
| `[확인 필요]` | Highlighted flag | `<mark>` |
| `[p.XX]`, `[pp.XX-YY]`, `[pp.XX, YY]` | Source page tag | `<span class="source-page">...</span>` |
| `[p.확인 필요]` | Source uncertainty tag | `<span class="source-page source-uncertain">...</span>` |
| `<!-- FIGURE_POINTER -->` | Textbook reference callout | text-only pointer with source / why / when / learner instruction |
| `<!-- FIGURE_SCHEMATIC -->` | Inline schematic figure | Mermaid by default or inline SVG if needed; not used in PART A currently |
| `<!-- FIGURE_IMAGE_SLOT -->` | Image or placeholder | placeholder if no permitted image file; not used in PART A currently |

**Source page tag rendering rules**

Detect and wrap source tags in body text, but not inside code blocks or inside `FIGURE_*` marker blocks.

- `\[p\.(\d+)\]` → standard single-page tag.
- `\[pp\.(\d+)[–-](\d+)\]` → range tag.
- `\[pp\.(\d+(?:,\s*\d+)+)\]` → multi-page non-contiguous tag.
- `\[p\.확인 필요\]` → uncertainty tag.

Do not fabricate, delete, renumber, or relocate page tags. Source page tags must remain visible in print mode.

**Navigation anchor integrity rules**

- Use a sticky left sidebar table of contents on desktop.
- Use `<a href="#...">` links only.
- Every `href` target must have one matching body `id`.
- Every major section heading (§1, §2, §5, §7, §8) must receive a stable id.
- Every §2 concept card heading should receive a stable id.
- Do not create duplicate ids.
- Enable `html { scroll-behavior: smooth; }`.
- Before finalizing, count all sidebar `href="#id"` values and verify each id exists exactly once.

**Rendering requirements**

- Math: MathJax CDN for inline `\(...\)` and display `\[...\]` / `$$...$$` equations.
- Code: `<pre><code>` with dark background, language class, and copy button.
- Accordion: self-test answers hidden by default, revealed on click.
- Checklist: sessionStorage state persistence if interactive checklist is rendered.
- Controls: code block copy button and print/PDF button using `window.print()`.
- Responsive: single-column/collapsed nav at `≤768px`; two-column layout at `≥1024px`.
- Theme: respect `prefers-color-scheme` for dark/light auto-switch.
- Print: remove decorative backgrounds, hide navigation, preserve source page tags, optimize page breaks.

**Figure rendering rules**

- Every figure marker becomes a proper text pointer callout or figure block.
- Do not embed copyrighted textbook images because image rights are None.
- `FIGURE_POINTER` must render as a compact text-only callout with source, why, when, and learner instruction.
- Do not generate or embed figures not present in PART A.
- For any future `FIGURE_SCHEMATIC`, use Mermaid only after validating node ids and labels; otherwise fall back to SVG or CSS cards.
- For any future `FIGURE_IMAGE_SLOT`, render a placeholder unless a permitted user-supplied or open-license image file is provided.

**CSS design system minimum**

Use variables for `--bg`, `--surface`, `--surface-2`, `--ink`, `--muted`, `--faint`, `--line`, `--line-strong`, `--blue`, `--green`, `--purple`, `--amber`, `--rose`, `--radius`, `--radius-sm`, `--shadow`, `--font`, `--mono`. Include `.sidebar`, `.source-page`, `.source-uncertain`, `.figure-pointer`, `figure`, `figcaption`, `.figure-placeholder`, and accordion styles.


### B5. Audit Guardrails

Known forbidden restorations for Session 02:

- Do not restore the wrong PK47 `fu` Curation Map expression from Step 1.
- Do not restore caffeine as a logP≈2 example; caffeine should not be used that way.
- Do not restore unsupported Caco-2/PAMPA, Lipinski rule-of-5, phase 1 screening, or “annual dozens of phase 1 failures” claims.
- Do not restore FDA Guidance, FDA reviewer deficiency-letter, or submission-template language not supported by the attached PDFs.
- Do not restore Rodgers-Rowland depth, `80% variance`, `one-digit Vd prediction`, or exact `r>0.85` claims.
- Do not restore exact visual-estimate values such as thiopental fat equilibrium 3.5 h or indinavir CSF/plasma 1/10 as author-stated facts.
- Do not restore albumin site I/II, SGLT2 inhibitor, activated charcoal, fexofenadine-grapefruit juice, or toxicokinetics expansions into the learner body.
- Do not embed unapproved textbook figures or unapproved code blocks.
- Treat `[교과서 외 실무 해석]` and `EXPERT_INFERENCE` as interpretive notes, not textbook facts.

### B6. Crucible Guardrails

- Crucible Report v1 is not a raw content source at Phase 4D.
- Preserve only already-adopted or explicitly allowed Grade A logic.
- Do not reintroduce omitted/rejected Crucible items.
- Do not convert speculative insight into textbook-derived fact.
- Accepted Crucible-derived logic retained in PART A includes: albumin ferry intuition, rate/extent separation, fuT vs transporter boundary, protein-binding conversion safety, and C vs Cu decision logic.

### B7. Deprecated and Forbidden Restorations

- Step 1 Draft v0 is deprecated.
- Do not use Step 1 Draft v0 as learner-body source except through the Micro-Patch Gate.
- Do not restore rejected overclaims, unsupported numbers, unsupported regulatory claims, source-unsupported examples, unapproved code, or unapproved figures.
- Content Lock v1/v2 are locked references only; v2.1 is the canonical body for this FULL MODE assembly.

### B8. PATCH MODE Splice Verification Table

Not applicable. FULL MODE was used because `02_Content Lock v2.1(1).md` contains the full canonical body with Phase 4C figure markers already inserted.

### B9. Zero-Omission Coverage Matrix

| Domain | Required item | Evidence in PART A | Status | Action |
|---|---|---|---|---|
| C1 Scope MUST | M1 membrane permeability determinants | §2 M1: size, lipophilicity, charge, transporter; Eq.4-1 | PRESENT | None |
| C1 Scope MUST | M2 perfusion- vs permeability-rate limitation | §2 M2: Eq.4-5~4-7, tissue perfusion table, thiopental/macromolecule examples | PRESENT | None |
| C1 Scope MUST | M3 Vd mathematical structure / Apex | §2 M3: Eq.4-8, 4-11~4-16, 4-25, 4-29, 4-30/App.C | PRESENT | None |
| C1 Scope MUST | M4 plasma protein binding and concentration-dependent fu | §2 M4: Eq.4-17~4-19 and G&W Eq.47:1/47:3/47:4 context | PRESENT | None |
| C1 Scope MUST | M5 tissue binding, Kp, transporter, blood/plasma ratio | §2 M5: Kp/fuT, acidic phospholipid, indinavir, App.D equation | PRESENT | None |
| C1 Scope MUST | M6 total vs unbound exposure metric choice | §2 M6 and §5 Critical Blow: Eq.2:373, Fig.2.134/2.136/2.140/2.141, Table2.21 | PRESENT | None |
| C2 Data anchors | R&T physiologic anchors: plasma, extracellular water, total body water, albumin V | §2 M3 Source-Anchored Data Anchors | PRESENT | None |
| C2 Data anchors | Cephalosporin V-fu and Vu-fu paired message | §2 M3 figure pointer and bullet on Fig.4-25~4-26 | PRESENT | None |
| C2 Data anchors | Warfarin nephrotic syndrome values | §2 M3 and §7 Q5 | PRESENT | None |
| C2 Data anchors | G&W PK47 protein concentrations, n, Ka estimate context | §2 M4 PK47 Source-Anchored Data and §7 Q8 | PRESENT | None |
| C2 Data anchors | G&W 456 drugs and IND/NDA recommendation | §2 M6 Source-Anchored Details | PRESENT | None |
| C3 Audit MUST_FIX | PK47 fu formula corrected and wrong Curation Map expression not restored | §2 M4 uses G&W Eq.47:1; PART B guardrail forbids old expression | PRESENT | None |
| C3 Audit MUST_FIX | Caffeine logP error removed | §2 M1 uses caffeine only in figure pointer comparison, not as logP≈2 claim | PRESENT | None |
| C3 Audit MUST_FIX | Unsupported regulatory wording removed | §2 M6 uses G&W author recommendation only; PART B forbids deficiency-letter/FDA guidance restoration | PRESENT | None |
| C3 Audit SHOULD_FIX | Thiopental exact 3.5 h not used | §2 M2 uses after 3 h remains; exact 3.5 h deleted | PRESENT | None |
| C3 Audit SHOULD_FIX | Lymph flow corrected | §2 M2 uses 1-10 mL/min per 70 kg | PRESENT | None |
| C3 Audit SHOULD_FIX | Rodgers-Rowland / one-digit Vd / 80% variance removed | §2 M5 does not use these claims; PART B forbids restoration | PRESENT | None |
| C4 Audit T5 | OMITTED_PROBLEMATIC / MISSING_CRITICAL resolved | Key additions from Audit are in M1-M6; optional scope-creep items remain excluded | PRESENT_COMPRESSED | No content micro-patch needed; rendering syntax patch logged in B10 |
| C5 Figure coverage | All retained Phase 4C figure markers | 5 FIGURE_POINTER blocks present exactly once in PART A (10 start/end marker tokens) | PRESENT | None |
| C5 Rights | Image rights = None respected | PART A uses text-only pointers; PART B instructs no textbook image embedding | PRESENT | None |
| C6 Page tags | Source page tags preserved | PART A retains [p.] and [pp.] tags from Content Lock v2.1; no new page tags added | PRESENT | None |
| C7 Crucible Grade A | Albumin ferry / Eq.C-13 intuition | §2 M3 Master Lens and M3 mastery note | PRESENT | None |
| C7 Crucible Grade A | Kp high affinity can slow equilibrium | §2 M2 Master Lens and practice lens | PRESENT | None |
| C7 Crucible Grade A | fuT vs transporter boundary | §2 M5 Boundary Condition and failure mode | PRESENT | None |
| C8 Draft regression | Rejected external/unsupported claims not restored | PART B B5/B7 list; PART A avoids unsupported numbers/regulatory claims | PRESENT | None |
| C9 Canonical integrity | Content Lock v2.1 learner sections preserved | PART A uses §1-§8 from v2.1 with adjacent labeled augmentations plus one rendering-only LaTeX micro-patch | PRESENT | None |

### B10. Micro-Patch Log

| Patch # | Location | Source trigger | Inserted text | PDF/Audit basis | Why allowed | Page tag handling |
|---:|---|---|---|---|---|---|
| 1 | §2 M1 Formal Definition, Eq.4-1 display math | HTML/MathJax rendering integrity check | Replaced a tab-corrupted `ext{Net rate of transport}` with `\text{Net rate of transport}` | R&T Eq.4-1 is already cited in Content Lock; this patch only restores LaTeX syntax | Scientific meaning unchanged; required for Phase 5 math rendering | No page tags added or altered |

### B11. Mastery Augmentation Log

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
|---:|---|---|---|---|---|---|
| 1 | §1 Big Idea | M | YES | EXPERT_INFERENCE | Frames all later cards around concentration species without adding factual claims. | Low |
| 2 | M1 · 막투과의 결정인자 | F | YES | AUDIT_DERIVED | Prevents the exact Audit-identified overreading of logP as sufficient. | Low |
| 3 | M2 · 분포의 율속 단계 | J | YES | CRUCIBLE_DERIVED | Reinforces Crucible rate/extent separation that is central to tissue time-course interpretation. | Low |
| 4 | M3 · 분포용적의 수학 구조 | J | YES | CRUCIBLE_DERIVED | Converts albumin-fu changes into a practical sequence for total vs unbound interpretation. | Low |
| 5 | M4 · 혈장단백결합과 fu의 농도의존성 | W | YES | TEXTBOOK_DERIVED | Connects PK47 to the safety condition for AUCu conversion. | Low |
| 6 | M5 · 조직결합과 Kp의 결정인자 | F | YES | CRUCIBLE_DERIVED | Keeps tissue binding and transporter imbalance separate in Eq.4-29 interpretation. | Low |
| 7 | M6 · 노출 지표 선택 | R | YES | TEXTBOOK_DERIVED | Clarifies that exposure metric selection is a causal-species/time-pattern claim. | Low |
| 8 | §5 Critical Blow | J | YES | EXPERT_INFERENCE | Provides a compact decision sequence for C vs Cu without introducing external claims. | Medium |


#### Rejected or Deferred Augmentation Candidates

| Rejected candidate | Reason for rejection |
|---|---|
| New named clinical examples beyond R&T/G&W examples | Would require external literature or new source tags. |
| New regulatory-deficiency wording | Audit explicitly rejected unsupported FDA/guidance/deficiency-letter language. |
| New numeric heuristics for BBB, PPB, or PBPK predictivity | Would add unsupported numerical claims. |
| Expanded Rodgers-Rowland/PBPK discussion | Rejected as scope creep for Session 02. |


# 09_HTML Compile Input Master

## Phase 4D Certification

| Certificate | Status | Basis |
|---|---|---|
| Learner-Standalone Certificate | PASS | PART A contains learner navigation plus the complete cleaned learner body; audit/process/compiler tables are kept out of PART A. |
| Zero-Omission Certificate | PASS | Scope, Audit T5, Phase 4C KEEP markers, Crucible preservation, and PDF-required high-impact data anchors were checked; 3 source-bounded micro-patches resolve missing hard anchors. |
| Mastery-Uplift Certificate | PASS | PART A includes 8 bounded, adjacent, source-status-labeled mastery augmentations without broad rewrite. |
| Source-Boundary Certificate | PASS | Augmentations are labeled as AUDIT_DERIVED, CRUCIBLE_DERIVED, or EXPERT_INFERENCE; micro-patches use verified PDF/Audit basis and page tags. |
| HTML-Readiness Certificate | PASS | PART B preserves Phase 5 rendering rules, figure/page-tag rules, audit/crucible guardrails, and splice verification. |

## Assembly Mode

PATCH MODE. `09_Content Lock v2.1(1).md` is a Figure Marker Patch / Insertion Map, not a full re-emitted learner body. The base learner body is therefore the cleaned learner-facing portion of `09_Content Lock v2(4).md`, with approved Marker Blocks #1–#7 inserted at the ends of their specified concept cards. The requested filename is adapted to `09_html_compile_input_master.md`.

## Input Manifest

| File | Role | Authority level | Used for | Notes |
|---|---|---|---|---|
| 09_scope_lock(3).md | Scope boundary | A0 | Defines source ranges, learner, A-Critical mode, image rights, required anchors | Used |
| 09_G_TMDD·항체 PK 거대분자 비선형(4).pdf | PDF verification source | A1 | Verifies G&W pp.94–111, PK26 pp.599–601, PK27 pp.602–610 | Used for page/source/figure and micro-patch verification |
| 09_T_TMDD·항체 PK 거대분자 비선형(4).pdf | PDF verification source | A1 | Verifies R&T Ch.21 pp.687–730 | Used for figure/page/source guardrails |
| 09_Audit_Report_v1(3).md | Audit guardrail | A2 | Controls MUST_FIX, SHOULD_FIX, T5/T6/T7 regression prevention | Used |
| 09_Content Lock v2(4).md | Canonical body | A3 | Base learner body before figure marker insertion | Used; process/adjudication sections excluded from learner body |
| 09_Content Lock v2.1(1).md | Figure insertion source | A4 | PATCH MODE figure strategy and marker blocks | Used; 7 approved markers spliced |
| 09_crucible_report_v1(1).md | Crucible guardrail | A5 | Controls accepted high-value internalization logic | Used only for bounded augmentation logic |
| 붙여넣은 텍스트 (1)(79).txt | Phase 4D assembler instruction | A7 | Defines master-file assembly, gates, certificates, Part A/B split | Used; filename adapted from 05 to 09 per user request |
| 붙여넣은 마크다운(2)(58).md | HTML compiler instruction / Prompt 5 | A7 | Defines Phase 5 rendering rules, marker mapping, page tags, navigation integrity | Used in Part B |
| 09_step1_draft_v0(2).md | Deprecated source | A6 | Regression check only | Not copied into PART A |
| S09_phase1_patch memo(2).md | Locked reference / patch memo | A6 | Confirms Phase 1 was audit-ready, not HTML-ready | Used as context only |
| 09_Content_Lock_v1(4).md | Locked reference | A6 | Prior content lock state | Not used as learner-body source |

## PART A — Learner-Facing Complete Handout

## Learner Navigation Aid

**How to use this handout**

1. Read the five MUST cards in order: M1 turnover → M2 protein/antibody PK → M3 TMDD curve phases → M4 Full TMDD → M5 MM boundary.
2. When a `FIGURE_POINTER` appears, consult the cited textbook figure; the image itself is not reproduced because image rights are not available.
3. Use §5 to remove common confusions, §7 to test active recall, and §8 to lock the professional synthesis.

**Learning route**

```text
M1 kin/kout baseline → M2 biologics ADME gates → M3 concentration-regime curve reading → M4 mechanistic ODE topology → M5 reduced-model boundary → §5 confusion pairs → §7 self-test → §8 professional synthesis
```

**Before you start**

- You should already know one-/two-compartment linear PK, basic Michaelis-Menten notation, and the idea of ODE state variables.
- Keep one question active throughout: “What data actually teach this parameter?”

**After you finish**

- You should be able to explain why `kin`, `kout`, `kon`, `koff`, `ke(RL)`, `Kd`, and `Km` are not interchangeable.
- You should be able to defend when Full TMDD is needed and when MM approximation is only an interpolation tool.
- You should be able to identify why high-dose fit quality does not automatically justify low-dose or low-concentration extrapolation.

---

# Updated Curation Map

<!-- MASTER LENS -->

<!-- ANNOTATION -->
본 세션의 핵심은 “항체 PK” 자체가 아니다. 핵심은 **turnover 수학이 target-mediated disposition(← 표적 결합이 약물 배치를 바꾸는 현상)으로 확장되는 순간, 어떤 자료가 어떤 파라미터를 가르치는가**를 체화하는 것이다. 10분 handout 기준으로 남길 spine은 5개뿐이다.

## MUST

| # | Concept | Locked rationale |
|---|---|---|
| M1 | **Turnover Paradigm (`kin`/`kout`)** | TMDD의 target compartment(`R`)는 endogenous turnover pool이다. 따라서 `kin/kout` 없이는 target baseline, recovery, `R0`, `kout` 식별을 설명할 수 없다. [G pp.95–97] |
| M2 | **Protein/Antibody Distinctive PK** | 큰 분자량, 제한적 Vd, lymphatic absorption, renal cutoff, FcRn salvage가 mAb PK의 “느림”과 비선형성의 생리학적 전제다. [G pp.97–102; R&T pp.701–724] |
| M3 | **TMDD 4-Phase Profile** | 곡선 모양을 Phase A–D로 읽어야 Full TMDD와 MM approximation 중 무엇을 선택할지 데이터 기반으로 판단할 수 있다. [G pp.603–610; R&T pp.711–712] |
| M4 | **Full TMDD Model** ⚡ **Apex Concept** | ligand, target, complex, sink가 하나의 ODE system으로 결합되는 지점이며, PD와 PK가 같은 수식으로 묶인다. [G pp.603–609; R&T pp.711–712] |
| M5 | **Michaelis-Menten Approximation Boundary** | MM은 limited dose range에서는 쓸 수 있다. 그러나 low-concentration extrapolation과 occupancy(← 표적 중 ligand가 결합한 비율) 판단에서는 구조적 bias를 만들 수 있다. [G p.609; R&T p.712] |

## CONTEXT

| Context item | Locked placement |
|---|---|
| Bucket/water turnover example | M1 직관 보조 1문장 [G p.96] |
| IgX sc 40 µg·kg⁻¹ and immunoglobulin turnover | M1 clinical anchor [G pp.100–102] |
| Estradiol turnover in postmenopausal women | M1 endogenous turnover extension [G pp.102–104] |
| Baseline scenarios / circadian and feedback examples | M1 assumption boundary; independent MUST로 승격하지 않음 [G pp.104–111] |
| Protein Vd, renal sieving, hepatic uptake, FcγR/FcRn | M2 ADME mechanism [R&T pp.701–709] |
| Somatropin sc absorption-rate-limited example | M2 absorption context 1문장 [R&T p.721] |
| Anakinra renal disease example | M2 renal disease context 1문장 [R&T p.724] |
| Efalizumab PK26 reduced model | M5 “MM이 제한적으로 통하는 사례” anchor [G pp.599–601; R&T p.710] |

---

---

# §1 Session Header & Roadmap

<!-- MASTER LENS -->

**Source**: [혼합]

- Gabrielsson & Weiner 5e, Ch.2 §2.6 Turnover [G pp.94–111]
- Gabrielsson & Weiner 5e, Case Study PK26 Efalizumab [G pp.599–601]
- Gabrielsson & Weiner 5e, Case Study PK27 Target Mediated Drug Disposition [G pp.602–610]
- Rowland & Tozer 5e, Ch.21 Protein Drugs [R&T pp.687–730]

**Mode**: A-Critical  
**Image rights**: None; figure work is deferred to Phase 4C.

## Big Idea

> **항체의 비선형 PK는 “큰 약물이 천천히 빠진다”가 아니다. ligand가 endogenous target turnover system에 결합하면서 생기는 concentration-dependent clearance(← 농도에 따라 달라지는 제거)다. Full TMDD를 MM으로 줄이면 제한된 dose range에서는 맞아 보일 수 있다. 그러나 PK27에서는 `Km`이 0.03에서 3.7로 약 123배 over-predicted되어 low-concentration extrapolation이 구조적으로 틀어졌다.** [G p.609]

<!-- ANCHOR -->

## Roadmap

```text
M1. Turnover Paradigm
       ↓
M2. Protein/Antibody ADME 특수성
       ↓
M3. TMDD 4-phase curve reading
       ↓
M4. Full TMDD Model: ligand + target + complex + sink
       ↓
M5. Michaelis-Menten Approximation: 언제 허용되고 언제 무너지는가
```

## Knowledge position

이 세션은 one-/two-compartment PK, Michaelis-Menten kinetics, ODE 기본, NONMEM `$DES` 구조를 전제로 한다. 후속으로는 mAb PopPK, TMDD/QSP, target occupancy simulation, FcRn engineering, biologics clinical pharmacology report 작성이 열린다. 단, 본 Content Lock에서는 교과서 범위를 넘어가는 specific regulatory timeline, cost, company-risk narrative는 삭제한다.

<!-- RECAP -->

**Section recap**: 이 세션의 판단 기준은 “curve가 예쁘게 fit되는가?”가 아니라 “이 데이터가 target turnover, binding, complex sink를 분리해서 가르치는가?”이다.

---

# §2 Concept Anatomy Cards

---

## ▌ Card M1 — Turnover Paradigm (`kin`/`kout`)

<!-- MASTER LENS -->

### [개념 Big Idea]

<!-- ANNOTATION -->
Turnover는 endogenous compound(← 체내에서 원래 생성되는 물질)의 baseline이 고정된 숫자가 아니라 **zero-order input `kin`과 first-order loss `kout·A`가 유지하는 동적 평형**임을 말한다. TMDD의 target `R`도 이 구조를 따른다. 따라서 mAb가 target에 결합한다는 것은 외부 ligand가 endogenous turnover pool에 개입한다는 뜻이다. [G pp.95–96]

### A. Formal definition

$$\frac{dA}{dt}=k_{in}-k_{out}\cdot A \qquad \text{Eq.2:237}$$

정상상태에서는 다음 관계가 성립한다. [G pp.95–96]

| Relation | Meaning | Source |
|---|---|---|
| $k_{in}=k_{out}\cdot A_0$ | input = output | Eq.2:239 [G p.96] |
| $k_{out}=k_{in}/A_0$ | fractional turnover rate | Eq.2:240 [G p.96] |
| $A_0=k_{in}/k_{out}$ | baseline amount | Eq.2:241 [G p.96] |
| $t_t=A_0/k_{in}=1/k_{out}$ | turnover time | Eq.2:242 [G p.96] |
| $t_t=V_{ss}/Cl=MRT$ | turnover time links to PK MRT | Eq.2:243 [G p.96] |
| $t_{1/2}=\ln(2)/k_{out}=\ln(2)\cdot t_t$ | half-life relationship | Eq.2:244 [G p.96] |

`kin`은 mass/time, `kout`은 time⁻¹이다. 이 단위 구분을 놓치면 target synthesis와 binding on-rate를 혼동하게 된다.

<!-- ANCHOR -->

### B. Intuition: faucet vs drain

10 L 욕조에 1 L·min⁻¹로 물이 들어오면 turnover time은 10분이다. 사람 몸의 물 42 L와 하루 intake 2.5 L를 쓰면 water turnover time은 약 17일이다. 즉, “얼마나 많이 있는가”보다 “현재 pool 전체가 얼마나 빨리 교체되는가”가 핵심이다. 이 단순한 예가 endogenous IgG, target receptor, hormone turnover와 같은 수학이다. [G p.96]

Fig.2.70의 핵심은 비대칭성이다. `kin`을 바꾸면 steady-state level만 바뀌고 time-to-steady-state는 linear kinetics 조건에서 유지된다. `kout`을 바꾸면 level과 time-to-steady-state가 함께 바뀐다. [G p.97]

### C. Clinical anchors

**IgX sc example**: Growth hormone-like IgX 40 µg·kg⁻¹ sc 투여에서 predose baseline은 32 µg·L⁻¹였고, 추정값은 `Cl/F=0.03 L·h⁻¹·kg⁻¹`, `V/F=0.10 L·kg⁻¹`, `kin=0.78 µg·h⁻¹·kg⁻¹`, `tt=2.7 h`, `MIT=1.8 h`, `t1/2=2.5 h`, `kout=0.27 h⁻¹`, pool size 2.3 µg·kg⁻¹였다. [G pp.100–101]

**Immunoglobulin turnover**: endogenous IgG는 Table 2.11에서 `t1/2=23 days`, fractional catabolic rate 6.7% plasma pool·day⁻¹, turnover 33 mg·kg⁻¹·day⁻¹로 제시된다. 이는 R&T의 therapeutic mAb half-life “approximately 21 days”와 비슷하지만, 두 문장을 같은 사실로 합치면 안 된다. [G p.102; R&T p.708]

**Estradiol turnover**: postmenopausal women 15명에서 estradiol은 평균 `kin=19 µg·24h⁻¹`, `Cl=1.6 L·min⁻¹`, `Vss=50 L`, `t1/2=26 min`, `MRT=18 min`로 보고되며, 낮은 E2 level은 clearance 증가보다 turnover 감소로 설명된다. [G pp.102–104]

### D. Assumptions and boundary conditions

Turnover는 baseline이 의미 있게 정의될 때 강력하다. 그러나 Fig.2.77은 baseline이 constant, oscillating, feedback-governed, Zeitgeber-driven일 수 있음을 보여준다. 따라서 PD endpoint를 처리할 때 첫 질문은 “predose concentration을 baseline으로 빼도 되는가?”가 아니라 “이 endpoint는 Fig.2.77 중 어떤 baseline scenario인가?”여야 한다. [G p.104]

<!-- TRENCH -->

**Trench-level tip**: predose target measurement가 있으면 단순히 `R0=THETA`로 추정하지 말고, 가능하면 baseline DV record로 모델에 들어가도록 설계해야 `R0` variability가 residual error로 흡수되는 것을 줄일 수 있다. 이 구현 팁은 교과서 수식의 NONMEM translation이며, 원문 control stream은 아니다.

### E. Limitations

Turnover 관계식은 linear first-order loss를 전제로 한다. 높은 농도에서 saturable metabolism이 개입하면 Michaelis-Menten 또는 더 복잡한 feedback model이 필요하다. Hyaluronan, body temperature, feedback examples는 이 boundary를 보여주는 context이지, 본 세션의 독립 MUST는 아니다. [G pp.95, 105–111]

### F. Five cognitive layers

| Layer | What to retain |
|---|---|
| L1 | `kin`은 input, `kout`은 fractional loss다. |
| L2 | baseline은 `kin/kout`의 결과이지 그냥 “0시간 값”이 아니다. |
| L3 | `kout` 변화는 level과 time scale을 동시에 바꾼다. |
| L4 | target `R` turnover가 TMDD의 backbone이다. |
| L5 | baseline model이 틀리면 target occupancy와 PD interpretation이 함께 틀어진다. |

### G. Zettelkasten atom

```text
Turnover = dynamic baseline.
A0 = kin/kout, tt = 1/kout = Vss/Cl = MRT.
TMDD target R is an endogenous turnover pool perturbed by ligand binding.
```

<!-- RECAP -->

**M1 recap**: Turnover를 모르면 `R0`, `kout`, baseline correction, target recovery를 모두 “피팅 파라미터”로만 보게 된다. Turnover를 이해하면 TMDD가 endogenous biology 위에 얹힌 PK model로 보인다.

---

> **Mastery Note — CRUCIBLE_DERIVED**  
> Treat baseline as a model assumption, not as a data-cleaning convention. In TMDD work, the first professional question is whether the observed baseline behaves like a turnover pool that can recover after perturbation.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.97, Fig.2.70
Why this matters: This figure fixes the asymmetric logic of turnover: changing `kin` changes steady-state level, whereas changing `kout` changes both level and time-to-steady-state. Without seeing both panels, learners often treat both as generic “rate changes.”
When to look: after reading Card M1.
Learner instruction: Compare the left and right panels. Ask which manipulation changes only the new level and which also changes the approach time.
<!-- /FIGURE_POINTER -->


## ▌ Card M2 — Protein/Antibody Distinctive PK

<!-- MASTER LENS -->

### [개념 Big Idea]

<!-- ANNOTATION -->
Protein drugs와 mAbs는 small molecules와 달리 “잘 녹고 전신으로 퍼진 뒤 간/신장으로 빠지는” 물질이 아니다. 큰 분자량, 제한된 capillary permeability, lymphatic input, proteolysis, receptor-mediated uptake(← 수용체 결합 후 세포 내 유입), FcRn salvage(← IgG를 분해에서 회수하는 기전)가 ADME의 기본 문법이다. [G pp.97–100; R&T pp.701–724]

### A. Formal definition

Protein/antibody PK의 distinctive features는 다음 네 가지 gate로 압축된다.

| Gate | Meaning | Source |
|---|---|---|
| Distribution gate | Vd가 작고 plasma/interstitial space 중심으로 제한된다. | Table 21-6 [R&T pp.701–702] |
| Absorption gate | sc/im 후 큰 단백질은 주로 lymphatic route로 천천히 systemic circulation에 들어간다. | Table 21-13 [R&T p.718] |
| Elimination gate | 작은 protein은 renal handling이 중요하고, 큰 mAb는 proteolysis/receptor-mediated pathways가 중심이다. | [G pp.98–99; R&T pp.704–708] |
| Rescue gate | FcRn은 IgG/mAbs를 acidic endosome에서 binding 후 recycling하여 lysosomal degradation을 피하게 한다. | Fig.21-5 [R&T p.709] |

### B. Key mechanisms

**Distribution**: R&T Table 21-6은 protein drugs의 `Vss`가 대체로 0.04–0.23 L·kg⁻¹ 범위임을 보여준다. 이는 large biologics가 body water 전체가 아니라 plasma/interstitial space에 제한된다는 해석을 뒷받침한다. [R&T pp.701–702]

**G&W protein/antibody data anchors**: G&W also uses an experimental antibody in cynomolgus monkey after five consecutive ascending infusions (0.77–771 µmol·kg⁻¹) to warn against naïve central-only antibody disposition, and r-hSOD in normal/nephrectomized rats to show renal clearance loss and low `Vd` in a large-protein context. [G pp.99–100]

**Lymphatic absorption**: G&W는 sc 투여된 proteins/peptides의 absorption이 low, erratic, delayed라고 설명하고, lymph flow를 about 2 L/day로 제시한다. R&T Table 21-13은 larger molecules `>15,000–20,000 g/mol`가 primarily lymphatics를 통해 systemic circulation에 들어간다고 정리한다. [G p.97; R&T p.718]

**Directionality, not extrapolated formula**: R&T Fig.21-16은 sheep에서 0.246–19 kDa 범위의 water-soluble compounds가 molecular weight 증가와 함께 lymph recovery가 증가하는 방향성을 보여준다. 이것은 150 kDa mAb의 recovery를 선형식으로 정량 예측하는 근거가 아니다. [R&T p.720]

**Absorption-rate limitation**: Somatropin은 i.v. half-life가 약 2.1 h인데 sc 후 plasma concentration이 길게 지속되어, 큰 단백질의 terminal profile이 elimination이 아니라 slow input에 의해 rate-limited될 수 있음을 보여준다. [R&T p.721]

**Renal disease**: anakinra(17,258 g/mol)는 renal function 감소에 따라 clearance가 감소하고 exposure가 증가하는 예시다. 반대로 full-size antibodies와 매우 큰 proteins는 glomerular filtration을 거의 받지 않아 renal disease 영향이 일반적으로 작다. [R&T p.724]

### C. FcRn and FcγR

FcRn은 endogenous IgG와 therapeutic mAbs의 long half-life를 설명하는 핵심 salvage mechanism이다. R&T는 mAb half-life가 IgG에 가까워 approximately 21 days인 경우가 많다고 설명하지만, 이는 모든 mAb의 고정 half-life가 아니다. FcRn binding, target-mediated clearance, immunogenicity, dose level에 따라 apparent half-life는 달라진다. [R&T pp.708–710]

FcγR-mediated clearance도 무시할 수 없다. R&T는 methotrexate가 rheumatoid arthritis patients에서 adalimumab clearance를 29–44% 감소시킬 수 있음을 제시한다. 따라서 “FcγR은 peripheral detail”이 아니라, 특정 질환/병용약물 맥락에서는 clearance covariate가 될 수 있다. [R&T p.706]

<!-- ANCHOR -->

### D. Why this matters for TMDD

mAb의 slow absorption과 small Vd를 모르면 TMDD curve를 잘못 읽는다. 왜냐하면 sc 투여에서는 Phase A의 rapid binding signature가 absorption phase와 confound될 수 있기 때문이다. 또한 FcRn rescue가 있는 mAb에서는 “terminal slope = simple elimination half-life”라는 해석이 위험해진다.

### E. Assumptions and limitations

- “mAb half-life ≈ 21 days”는 useful prior일 수 있지만, molecule-specific FcRn binding evidence와 target-mediated clearance를 확인해야 한다. [R&T p.708]
- ADA/immunogenicity는 PK를 변화시킬 수 있으므로, unexplained clearance increase가 나타나면 target biology뿐 아니라 ADA도 점검해야 한다. [R&T p.725]
- sc mAb `Tmax`는 Table 21-15에서 보통 며칠 단위이며, adalimumab F=0.64, `Tmax=5.5 days`, `t1/2=30 days`; omalizumab F=0.62, `Tmax=7.5 days`, `t1/2=26 days`; efalizumab F=0.50, `t1/2=17 days`로 제시된다. [R&T p.723]

### F. Five cognitive layers

| Layer | What to retain |
|---|---|
| L1 | 큰 protein은 capillary diffusion이 느리고 lymphatic route가 중요하다. |
| L2 | Vd가 작다는 것은 “약한 분포”가 아니라 physiology-constrained distribution이다. |
| L3 | FcRn은 mAb half-life를 늘리지만 half-life를 고정값으로 만들지는 않는다. |
| L4 | renal disease effect는 molecular size와 renal handling에 따라 달라진다. |
| L5 | sc mAb profile의 terminal slope는 elimination이 아니라 absorption-rate limitation일 수 있다. |

### G. Zettelkasten atom

```text
Antibody PK = restricted distribution + lymphatic input + proteolytic/receptor-mediated elimination + FcRn salvage.
Do not read mAb half-life as a single molecule property when TMDD or slow input is active.
```

<!-- RECAP -->

**M2 recap**: mAb PK의 느림은 단일 half-life 숫자가 아니라, tissue access, lymphatic transit, FcRn recycling, target/receptor-mediated sink가 합쳐진 결과다.

---

> **Failure Mode — CRUCIBLE_DERIVED**  
> A single reported mAb half-life can be a misleading mental shortcut when slow input, FcRn salvage, target-mediated clearance, or ADA are active. Read half-life as a regime-dependent summary unless the concentration range and mechanism are clear.

<!-- FIGURE_SCHEMATIC -->
Title: Protein/Antibody PK Four-Gate Map
Mode: N
Visual objective: Show in 5 seconds that mAb PK is controlled by four physiological gates, not by “large molecule = slow elimination” alone.
Core message: Protein/antibody PK emerges from restricted distribution, lymphatic input, size-dependent elimination, and FcRn rescue.
Elements to include: central `mAb / protein drug`; Distribution gate (`Vss` small, plasma/interstitial restriction); Absorption gate (sc/im to lymphatic route, delayed input); Elimination gate (renal cutoff for small proteins, proteolysis/RME for larger proteins); Rescue gate (FcRn salvage, degradation avoidance, longer apparent half-life); downstream cautions for terminal slope, renal disease, and TMDD curve reading.
Elements to exclude: full numerical tables; long drug lists; 150 kDa lymph recovery percentage extrapolation; decorative antibody anatomy.
Suggested rendering: Mermaid
Caption: Protein/antibody PK should be read as a set of physiological gates before interpreting terminal slope or nonlinear clearance.
Alt text: A central mAb node branches into distribution, absorption, elimination, and FcRn rescue gates, each leading to a specific PK interpretation caution.
Source relation: Newly designed
<!-- /FIGURE_SCHEMATIC -->

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.709, Fig.21-5
Why this matters: FcRn salvage is a recycling mechanism, not just a long half-life label. The figure shows how IgG/mAbs avoid degradation and return to circulation.
When to look: after reading Card M2.
Learner instruction: Trace the endosomal route. Identify which path leads to degradation and which path returns IgG/mAb to the systemic circulation.
<!-- /FIGURE_POINTER -->


## ▌ Card M3 — TMDD 4-Phase Concentration-Time Profile

<!-- MASTER LENS -->

### [개념 Big Idea]

TMDD curve는 “비선형 곡선”이 아니다. **ligand concentration이 target concentration, `Kd`, `Km`, saturation boundary를 지나갈 때 dominant clearance route가 바뀌는 기록**이다. 따라서 Phase A–D는 단순 시간 구간이 아니라 concentration hierarchy다. [G pp.604–610; R&T pp.711–712]

### A. Formal definition

PK27과 R&T는 characteristic TMDD profile을 네 phase로 설명한다. [G p.610; R&T p.712]

**PK27 dose anchor**: PK27’s full-TMDD demonstration uses rapid intravenous injections of a monoclonal antibody at 1.5, 5, 15, and 45 mg·kg⁻¹; this is why dose-stratified curve reading is central rather than decorative. [G pp.602–603]

| Phase | Dominant process | Interpretation |
|---|---|---|
| A | rapid second-order binding | ligand and target equilibrate rapidly |
| B | slow first-order disposition | target route saturated; nonspecific route dominates |
| C | mixed-order disposition | target partly saturated; linear and target-mediated routes coexist |
| D | `koff` and `ke(RL)`-driven terminal phase | very low ligand; target-specific elimination becomes visible |

<!-- ANCHOR -->

### B. Concentration hierarchy, not just time sequence

A beginner reads Phase A→B→C→D as a time sequence. A modeler reads the same curve as ligand concentration crossing `R0`, `Km`, and `Kd`. In PK27, `R0≈12 mg·L⁻¹`, `Km≈0.03 mg·L⁻¹`, and `Kd` is defined by `koff/kon`. These thresholds explain why low-dose curves reveal slopes that high-dose curves can hide. [G pp.603–610]

### C. What the curve teaches

- If only high-dose data are observed, target-mediated route may look saturated and linear.
- If low-dose data are missing because assay sensitivity is poor, Phase A/D may be invisible.
- If sc absorption is slow, early rapid binding can be masked by input kinetics.
- If target and complex data are absent, ligand-only fitting may look acceptable while `kon`, `koff`, `ke(RL)` remain imprecise. [G pp.603–609]

### D. Practical reading rule

A TMDD plot should be inspected dose-stratified. If low-dose residuals drift systematically while high-dose profiles fit well, the model may have phantom linearity: apparent success in central profiles but biased low-concentration extrapolation. This is a diagnostic interpretation derived from PK27’s MM failure, not a textbook-provided NONMEM rule. [G p.609]

### E. Limitations

The four phases are clearest in rich, high-quality, multi-dose, IV-like datasets. Sparse clinical sampling, sc absorption, total-vs-free assay ambiguity, or membrane-bound targets can obscure phase boundaries. [G pp.604–605]

### F. Five cognitive layers

| Layer | What to retain |
|---|---|
| L1 | TMDD is linear at very low and very high ligand concentrations, nonlinear in between. |
| L2 | Saturation changes apparent clearance. |
| L3 | Four phases map to dominant ODE terms. |
| L4 | Missing low-dose or target data hides the most important phase information. |
| L5 | Curve reading precedes model selection. |

### G. Zettelkasten atom

```text
TMDD phases are concentration-regime signatures.
Do not choose MM or Full TMDD before asking which phases the dataset actually observes.
```

<!-- RECAP -->

**M3 recap**: Phase A–D는 그림 설명이 아니라 model-selection checklist다. 보이는 phase가 곧 식별 가능한 mechanism이다.

---

> **Mastery Note — CRUCIBLE_DERIVED**  
> Phase A–D should be memorized less as a time order and more as a concentration-regime map. This is the move that turns a curve shape into a model-selection argument.

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.712, Fig.21-9; cross-check Gabrielsson & Weiner 5e, p.610, Fig.27.7
Why this matters: This figure prevents the common mistake of memorizing TMDD Phase A–D as mere time segments. The phases should be read as concentration-regime signatures linked to target saturation and `Km`/`Kd` boundaries.
When to look: after reading Card M3, before reading Card M5.
Learner instruction: Follow Phase A–D while asking what concentration regime the ligand is in. Then map the phase transition to the MM boundary discussion.
<!-- /FIGURE_POINTER -->


## ▌ Card M4 — Full TMDD Model ⚡ Apex Concept

<!-- MASTER LENS -->

### [⚡ Apex Big Idea]

<!-- ANNOTATION -->
Full TMDD는 ligand disposition, target turnover, ligand-target binding, complex loss를 하나의 mechanistic system으로 묶는다. 즉, 하나의 ODE system(← 시간에 따른 상태변화 방정식 묶음)이 PK와 target biology를 동시에 추적한다. PK27은 이를 “eight-parameter full TMDD model”로 부르지만, `Vc=0.05 L·kg⁻¹`를 fixed한 상태에서 Table 27.2가 8 estimated parameters를 보고한다. fixed `Vc`까지 structural quantity로 세면 ligand central, ligand tissue, target, complex의 4 state와 9 structural quantities가 존재한다. [G pp.603, 608–609]

### A. Formal structure

Full TMDD의 state variables는 다음 4개다. [G pp.604–607; R&T p.711]

| State | Meaning |
|---|---|
| `L_c` | ligand in central compartment |
| `L_t` | ligand in tissue/peripheral compartment |
| `R` | free target/receptor |
| `RL` | ligand-target complex |

PK27 Table 27.2의 8 estimated/reported parameters는 `Cl`, `Kon`, `Koff`, `Vt`, `Cld`, `Kout`, `R0`, `Ke(RL)`이다. `Vc`는 0.05 L·kg⁻¹로 fixed되었다. [G pp.608–609]

<!-- ANCHOR -->

### B. Mechanistic equations

Conceptually, the model contains:

```text
Ligand central/tissue distribution:
  nonspecific Cl(L), Cld, Vc, Vt

Target turnover:
  dR/dt = kin - kout·R - kon·L·R + koff·RL

Complex dynamics:
  dRL/dt = kon·L·R - koff·RL - ke(RL)·RL
```

The binding term is `kon·L·R`, not `kin·L·R`. `kin` belongs to target synthesis; `kon` is the second-order on-rate for ligand-target binding. 이 구분은 단순 표기 문제가 아니라, turnover process와 binding process를 분리하는 핵심이다. [G p.604; G pp.606–607]

### C. Identifiability: what data teach which term

PK27 uses three datasets: I = ligand only, II = ligand + target, III = ligand + target + complex. The precision of `kon`, `koff`, and `ke(RL)` improves as target and complex time courses are added. Table 27.2 shows `kon` CV% improving 17→2→1, `koff` 27→13→3, and `ke(RL)` 27→23→2 across datasets I→II→III. [G pp.603, 608–609]

The expert reading is simple: ligand data teach nonspecific disposition and visible phase structure; target data teach target recovery and saturation boundaries; complex data teach sink behavior. Data richness is not cosmetic—it determines which ODE terms become estimable.

### D. Plausible fallacy: fit quality without mechanism

A reduced model can fit the three highest ligand profiles reasonably while failing the lowest profile. In PK27, the MM model produced `Km=3.7` whereas the TMDD model implied `Km=0.03`, a 123× over-prediction. This bias can propagate through trough prediction, target occupancy estimation, and subgroup extrapolation; the quantitative impact must be evaluated molecule-by-molecule, not asserted generically. [G p.609]

### E. NONMEM-style implementation note

[교과서 외 구현 번역 예시] The following is not a textbook control stream. It is a NONMEM-style educational skeleton translated from the PK27/R&T ODE structure.

```text
; conceptual only
CLIG = A(1)/VC
CTIS = A(2)/VT
R    = A(3)/VR_OR_SCALE
RL   = A(4)/VC

BIND = KON * CLIG * R * VC     ; amount/time scale requires volume conversion
DISS = KOFF * A(4)
SINK = KERL * A(4)

DADT(1) = INPUT - CL*CLIG - Q*(CLIG-CTIS) - BIND + DISS
DADT(2) =  Q*(CLIG-CTIS)
DADT(3) =  KIN - KOUT*A(3) - BIND + DISS
DADT(4) =  BIND - DISS - SINK
```

<!-- TRENCH -->

**Trench-level tip**: `BIND` must have amount/time units before entering `DADT`. If `kon·C_L·R` is written without the required amount scale conversion, the model may silently violate mass balance.

### F. Assumptions and boundary conditions

- `Vc=0.05 L·kg⁻¹` fixing is a high-resolution rapid-IV/high-MW approximation in PK27; it is not a universal clinical constant. [G p.608]
- Free target, total target, and complex assays must be aligned with the model’s state variables. If the assay reports partial total target while the model assumes free `R`, `R0` and `kout` interpretation changes.
- Full TMDD can be over-parameterized if only sparse ligand data exist. PK26 failed to fit a full TMDD model because target/complex and `kon/koff/kd` information were not available. [G p.601]

### G. Five cognitive layers

| Layer | What to retain |
|---|---|
| L1 | Full TMDD has 4 state variables. |
| L2 | Target turnover and binding are separate processes. |
| L3 | `Kd` and `Km` are not interchangeable. |
| L4 | Target/complex measurements improve parameter precision because they isolate ODE terms. |
| L5 | Good ligand fit alone does not prove mechanistic validity. |

### H. Zettelkasten atom

```text
Full TMDD = 4-state mechanistic system:
ligand central + ligand tissue + free target + complex.
PK27 reports 8 estimated parameters because Vc is fixed at 0.05 L·kg⁻¹.
```

<!-- RECAP -->

**M4 recap**: Full TMDD의 핵심은 “파라미터가 많다”가 아니라, ligand curve 안에 숨어 있는 target turnover, binding, complex sink를 분리하는 것이다.

---

> **Practice Lens — CRUCIBLE_DERIVED**  
> Before adding complexity to Full TMDD, name which observed species teaches which hidden ODE term. If the dataset only observes ligand, many mechanistic parameters may be numerically fitted but not biologically learned.

> **Failure Mode — AUDIT_DERIVED**  
> The `kin`/`kon` distinction is a structural sanity check. When a control stream or derivation uses target synthesis notation for binding, it is not a typo to ignore; it changes the process being modeled.

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.711, Fig.21-8; cross-check Gabrielsson & Weiner 5e, p.604, Fig.27.2
Why this matters: Full TMDD is a topology problem before it is a parameter-count problem. The figure shows how ligand, target, complex, binding, dissociation, and sink are connected.
When to look: after reading Card M4.
Learner instruction: Locate ligand, free target, and complex first. Then map `kon`, `koff`, and `ke(RL)` to arrows, and keep `kin` separate as target turnover input.
<!-- /FIGURE_POINTER -->

<!-- FIGURE_SCHEMATIC -->
Title: Data Richness → ODE Term Identifiability Map
Mode: N
Visual objective: Show in 5 seconds why ligand-only, ligand+target, and ligand+target+complex datasets identify different TMDD mechanisms.
Core message: Target and complex assays are not decorative; they isolate hidden ODE terms.
Elements to include: Dataset I = ligand only → nonspecific disposition + gross phase structure; Dataset II = ligand + target → target recovery/saturation boundary → improved `kon`/`koff`; Dataset III = ligand + target + complex → complex sink trajectory → improved `ke(RL)`; summary CV% improvement signal: `kon` 17→2→1, `koff` 27→13→3, `ke(RL)` 27→23→2; bottom message “Observed species determine estimable mechanism.”
Elements to exclude: full Table 27.2 reproduction; non-key parameters; estimation software settings; NONMEM control stream details.
Suggested rendering: Mermaid
Caption: Adding target and complex observations converts hidden TMDD mechanisms into estimable ODE terms.
Alt text: Three dataset rows show ligand-only, ligand-plus-target, and ligand-plus-target-plus-complex data progressively improving identifiability of binding and complex-loss parameters.
Source relation: Newly designed
<!-- /FIGURE_SCHEMATIC -->


## ▌ Card M5 — Michaelis-Menten Approximation Boundary

<!-- MASTER LENS -->

### [개념 Big Idea]

Michaelis-Menten approximation은 Full TMDD의 target/complex subsystem을 `Vmax`와 `Km`로 줄이는 것이다. 즉, `R`과 `RL`을 직접 추적하지 않고 target-mediated route를 하나의 saturable clearance term으로 접는다. 문제는 fit이 아니라 **어느 concentration/occupancy range에서 이 reduction이 구조적으로 허용되는가**이다. [G p.609; R&T p.712]

### A. Formal definition

Reduced model은 target-mediated route를 다음 형태로 압축한다. 여기서 압축은 단순화이지, biology가 사라졌다는 뜻이 아니다.

$$Cl_{MM}=\frac{V_{max}}{K_m+C}$$

Full TMDD에서 relevant constants are:

$$K_d=\frac{k_{off}}{k_{on}}$$

$$K_m=\frac{k_{off}+k_{e(RL)}}{k_{on}}$$

`Kd`는 binding affinity에 가까운 thermodynamic dissociation constant이고, `Km`은 complex loss까지 포함한 apparent kinetic constant다. [G pp.603–609; R&T pp.711–712]

### B. When MM can work

MM can be adequate when:

- ligand concentration significantly exceeds target concentration;
- target occupancy is close to complete saturation;
- the observed dose range is limited;
- the purpose is interpolation within observed profiles, not low-concentration extrapolation. [G p.609; R&T p.712]

PK26 Efalizumab is a useful reduced-model anchor: a two-compartment model with parallel linear/MM elimination was used because full TMDD failed without target/complex and `kon/koff/kd` information. Reported estimates included `Vt=0.061`, `Vmax=0.039`, `Km=0.161`, `CLd=0.031`, `CLL=0.007`. [G pp.599–601]

**PK26 dose anchor**: The reduced Efalizumab model was fitted to five intravenous time-courses from single-dose i.v. bolus data, so it should be read as a limited-data reduced-model anchor, not as proof that MM is universally mechanistic. [G pp.599–601]

### C. When MM breaks

In PK27, MM fitted the three highest concentration profiles relatively well but showed severe systematic deviation at the lowest concentration profile. The estimated `Km=3.7` was dramatically over-predicted versus `0.03` from the TMDD model. [G p.609]

The clinical lesson is not “never use MM.” The lesson is narrower and more useful: **do not use MM outside the concentration/occupancy domain in which target saturation is demonstrated**.

### D. Occupancy verification

If greater than approximately 90–95% occupancy is needed, simplification may be acceptable; if occupancy is below `Kd` or below biomarker potency, MM may not suffice. [G p.609]

Practical Content Lock rule: any report that uses MM for a mAb with plausible TMDD should specify the observed concentration range, target concentration range, and minimum predicted target occupancy over the dosing interval. This is an implementation interpretation of the source boundary, not a quoted regulatory requirement.

### E. Limitations

- MM loses explicit `R0`, `kout`, `kon`, `koff`, and `ke(RL)` interpretation.
- It can hide low-concentration bias if only high-dose or central profiles are weighted.
- It cannot answer target recovery or complex sink questions without additional assumptions.
- QSS/QE approximations are related but are not expanded here; that is a follow-up modeling session.

### F. Five cognitive layers

| Layer | What to retain |
|---|---|
| L1 | MM is a reduction of TMDD, not a competing biology. |
| L2 | `Km` is not the same as binding `Kd`. |
| L3 | MM can interpolate but may fail extrapolation. |
| L4 | Occupancy range is the validity boundary. |
| L5 | If target/complex dynamics matter clinically, Full TMDD or richer data are needed. |

### G. Zettelkasten atom

```text
MM approximation is acceptable only inside a demonstrated saturation/occupancy domain.
PK27 shows why good high-dose fit can coexist with low-dose structural bias.
```

<!-- RECAP -->

**M5 recap**: MM은 빠른 실무 도구일 수 있지만, “fit이 잘 됨”과 “target biology를 올바르게 외삽함”은 같은 말이 아니다.

---

> **Practice Lens — AUDIT_DERIVED / CRUCIBLE_DERIVED**  
> MM is defensible when the question stays inside the observed saturation domain. It becomes fragile when the decision depends on recovery, low-concentration extrapolation, or target occupancy below the fitted range.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.609, Fig.27.6
Why this matters: Fig.27.6 is the critical blow against unqualified MM extrapolation: high-dose fit can look acceptable while the lowest-dose profile shows systematic deviation and `Km` is over-predicted. Without seeing this, learners may equate fit quality with mechanistic validity.
When to look: after reading Card M5.
Learner instruction: Compare the three higher profiles against the lowest profile. Treat the mismatch as a model-boundary signal, not as a cosmetic fit issue.
<!-- /FIGURE_POINTER -->


# §5 Confusion Pair Dissection

## ▌ Pair 1 — Turnover Rate (`kin`) vs Fractional Turnover Rate (`kout`)

<!-- CONFUSION -->

| Confusion | Correction |
|---|---|
| `kin`과 `kout`을 둘 다 “rate”로만 기억한다. | `kin`은 mass/time인 input이고, `kout`은 time⁻¹인 fractional loss다. |
| `kin` 증가와 `kout` 감소가 둘 다 concentration 증가라서 같다고 생각한다. | `kin` 변화는 level만, `kout` 변화는 level과 time scale을 함께 바꾼다. [G p.97] |

**Locked sentence**: `kin`은 수도꼭지이고 `kout`은 배수구다. 수위만 볼 것이 아니라 새 수위에 도달하는 시간까지 함께 보라.

---

## ▌ Pair 2 — Full TMDD vs Michaelis-Menten Approximation

<!-- CONFUSION -->

| Confusion | Correction |
|---|---|
| Full TMDD는 복잡하고 MM은 단순한 대체 모델이다. | MM은 Full TMDD target/complex subsystem의 reduction이다. |
| 고용량 fit이 좋으면 MM이 충분하다. | PK27에서는 high-dose profiles fit이 좋아도 low-dose profile에서 systematic deviation과 `Km` 123× bias가 발생했다. [G p.609] |
| target/complex assay는 있으면 좋은 부가자료다. | target/complex data는 `kon`, `koff`, `ke(RL)` precision을 개선하는 식별 자료다. [G p.609] |

**Locked sentence**: MM은 “작은 TMDD”가 아니라 “target biology를 `Vmax/Km`으로 접은 모델”이다. 접어도 되는지는 occupancy range가 결정한다.

---

## ▌ Pair 3 — `Kd` vs `Km` in TMDD

<!-- CONFUSION -->

| Term | Definition | What it means |
|---|---|---|
| `Kd` | `koff/kon` | ligand-target binding/dissociation equilibrium |
| `Km` | `(koff + ke(RL))/kon` | binding plus complex loss/internalization effect |

`Kd` and `Km` can differ because `Km` contains `ke(RL)`. In documentation, in vitro thermodynamic `Kd` and in vivo model-derived apparent `Km` must be separated. Calling both “affinity” is a common source of internal confusion and reviewer-facing inconsistency. [G pp.603–609; R&T pp.711–712]

**Locked sentence**: `Kd`는 결합의 언어이고, `Km`은 결합 이후 sink까지 포함한 disposition의 언어다.

---

## ▌ Pair 4 — Linear PK at Low Concentration vs Linear PK at High Concentration

<!-- CONFUSION -->

| Regime | Why it looks linear | Risk |
|---|---|---|
| Very low ligand | target route not saturated; nonspecific + target-specific first-order routes coexist | assay sensitivity가 낮으면 이 구간을 놓친다. |
| Very high ligand | target route saturated; nonspecific clearance dominates | high-dose fit만 보고 MM/linear model을 과신한다. |
| Middle range | target saturation changes with concentration | nonlinear clearance가 가장 뚜렷하다. |

**Locked sentence**: TMDD는 “선형 또는 비선형”이 아니라, concentration에 따라 두 종류의 linearity와 한 구간의 nonlinearity가 이어지는 system이다. [G pp.604–605]

<!-- RECAP -->

**§5 recap**: 이 세션의 가장 위험한 혼동은 `fit`, `affinity`, `linearity`, `half-life` 같은 친숙한 단어가 TMDD에서는 모두 조건부 의미를 갖는다는 점이다.

---

> **Mastery Note — EXPERT_INFERENCE**  
> In this chapter, familiar terms such as fit, affinity, linearity, and half-life are safe only when their concentration regime is stated. A robust report defines the regime before defending the parameter.


# §7 Self-Test: Active Recall Module

<!-- SELF-TEST -->

## Q1 (회상)

`A0 = kin/kout`에서 `kin`과 `kout`의 단위는 각각 무엇인가?

**Answer**: `kin`은 mass/time, `kout`은 time⁻¹이다. `A0`는 두 값의 ratio로 정의되는 baseline amount다. [G p.96]

---

## Q2 (회상)

왜 `kout` 변화는 steady-state level과 time-to-steady-state를 동시에 바꾸는가?

**Answer**: `kout`은 fractional loss rate이므로 baseline `A0=kin/kout`와 time scale `tt=1/kout`에 동시에 들어간다. [G pp.96–97]

---

## Q3 (회상)

Full TMDD의 4 state variables는 무엇인가?

**Answer**: ligand central, ligand tissue/peripheral, free target `R`, ligand-target complex `RL`이다. [G pp.604–607]

---

## Q4 (적용)

mAb ligand-only data에서 high-dose profiles는 잘 맞지만 lowest dose에서 systematic under/over-prediction이 보인다. 어떤 판단을 해야 하는가?

**Answer**: MM 또는 reduced model이 observed high-dose range에서는 interpolation을 하고 있지만, low-concentration TMDD phase를 제대로 설명하지 못할 가능성이 높다. 이 판단은 측정된 dose/concentration 범위에 한정되며, 외삽 영역은 target occupancy와 sensitivity analysis가 필요하다. [G p.609]

---

## Q5 (적용)

`Km`과 `Kd`가 다를 수밖에 없는 mechanistic 이유는 무엇인가?

**Answer**: `Kd=koff/kon`은 결합/해리 equilibrium이고, `Km=(koff+ke(RL))/kon`은 complex irreversible loss를 포함한다. 따라서 complex sink가 있으면 `Km`은 thermodynamic affinity가 아니라 apparent kinetic constant가 된다. [G p.609; R&T p.712]

---

## Q6 (적용)

sc mAb의 terminal slope를 보고 곧바로 elimination half-life라고 해석하면 왜 위험한가?

**Answer**: 큰 protein은 sc/im 후 lymphatic absorption이 느리고 absorption-rate-limited profile을 보일 수 있다. Somatropin처럼 i.v. half-life는 짧아도 sc profile은 길게 지속될 수 있다. [R&T pp.718–721]

---

## Q7 (회상)

PK27에서 `Vc=0.05 L·kg⁻¹`는 어떻게 처리되었는가?

**Answer**: `Vc`는 fixed assumption으로 사용되었고, Table 27.2는 그 외 8 estimated/reported parameters를 제시한다. fixed `Vc`까지 structural quantity로 세면 9개를 언급할 수 있으나, “8 estimated parameters”와 구분해야 한다. [G pp.603, 608–609]

---

## Q8 (적용)

target and complex data가 추가되면 왜 `kon`, `koff`, `ke(RL)` precision이 좋아지는가?

**Answer**: ligand-only data는 여러 ODE term의 합성 결과만 보여준다. target data는 saturation/recovery를, complex data는 sink behavior를 직접 가르치므로 해당 파라미터의 CV%가 개선된다. PK27 Table 27.2에서 `kon` 17→2→1, `koff` 27→13→3, `ke(RL)` 27→23→2로 개선된다. [G p.609]

---

## Q9 (회상)

R&T Fig.21-16에서 얻을 수 있는 올바른 결론과 얻으면 안 되는 결론은 무엇인가?

**Answer**: 올바른 결론은 molecular weight 증가에 따라 lymphatic recovery가 증가하는 방향성이다. 얻으면 안 되는 결론은 0.246–19 kDa sheep data를 150 kDa mAb에 선형 외삽해 구체 recovery percentage를 계산하는 것이다. [R&T p.720]

---

## Q10 (보스 딜레마)

팀이 “MM model로 OFV도 낮고 VPC도 괜찮으니 first-in-human low-dose extrapolation에 쓰자”고 주장한다. 30초 답변은?

**Answer**: “MM은 observed dose range 안에서는 쓸 수 있지만, low-dose extrapolation은 target occupancy가 충분히 높게 유지되는지 확인해야 합니다. PK27에서는 high-dose fit이 양호해도 lowest-dose profile에서 systematic deviation이 있었고 `Km`이 0.03에서 3.7로 123× over-predicted되었습니다. 최소한 dose-stratified residual, predicted occupancy, low-concentration sensitivity analysis를 보고 결정해야 합니다.” [G p.609]

<!-- RECAP -->

**§7 recap**: 답을 외우는 것보다 중요한 것은 “이 데이터가 어떤 phase와 어떤 ODE term을 실제로 가르치는가?”를 즉시 묻는 것이다.

---

> **Practice Lens — EXPERT_INFERENCE**  
> For every self-test answer, add one extra sentence: “Which observable taught this?” This habit prevents treating unobserved target biology as if it had been measured.


# §8 Meta-Frame & Big Picture

## A. Positioning

<!-- MASTER LENS -->

이 세션은 biologics pharmacometrics의 입구다. Small molecule PK에서는 clearance와 Vd를 중심으로 설명할 수 있었다. 그러나 mAb에서는 target biology, binding kinetics, complex sink, FcRn salvage, lymphatic input이 함께 PK 곡선의 형태를 만든다.

선행 지식:

```text
linear PK → Michaelis-Menten → turnover → TMDD
```

후속 지식:

```text
mAb PopPK → target occupancy simulation → QSP/PBPK → clinical pharmacology narrative
```

## B. Dependencies and failure modes

| If skipped | Concrete failure |
|---|---|
| Turnover | target baseline을 predose DV로만 처리하고 `R0/kout` interpretation을 잃는다. |
| Protein ADME | sc mAb terminal slope를 elimination으로 오해한다. |
| 4-phase TMDD | high-dose fit만 보고 low-dose extrapolation bias를 놓친다. |
| Full TMDD | target/complex data의 value를 “nice-to-have”로 오판한다. |
| MM boundary | observed range interpolation을 clinical extrapolation으로 착각한다. |

## C. Professional moat

이 세션을 제대로 체화하면 두 가지 능력이 생긴다.

1. **Mechanistic model narrative justification**: “왜 Full TMDD인가 / 왜 MM이어도 되는가 / 왜 target assay가 필요한가”를 수식, physiology, observed concentration range로 설명할 수 있다.
2. **Diagnostic GOF reading**: 전체 VPC가 아니라 dose-stratified residual, low-dose profile, target/complex coverage를 먼저 보고 structural misspecification을 의심할 수 있다.

<!-- TRENCH -->

**Trench-level diagnostic rule**: mAb TMDD dataset을 처음 받으면 전체 fit plot보다 먼저 dose-stratified plot을 만든다. 고용량은 맞고 저용량만 systematic하게 틀리면, “variability problem”보다 “reduced model boundary problem”을 먼저 의심한다.

## D. Final locked synthesis

<!-- RECAP -->

mAb 비선형 PK의 본질은 “항체가 크다”가 아니라, **큰 ligand가 제한된 tissue space와 lymphatic input을 거쳐 endogenous target turnover system에 들어가고, binding/complex/sink가 concentration-dependent clearance를 만든다**는 점이다. Full TMDD는 이 과정을 분해하고, MM은 일부 조건에서만 이를 압축한다. 모델 선택의 기준은 편의성이 아니라 dataset이 관찰한 phase와 임상 의사결정이 요구하는 extrapolation 범위다.

## PART B — Compiler-Only Appendix

This appendix is not learner-facing. It exists only to protect Phase 5 rendering fidelity.

### B1. Compilation Contract

- PART A is the only learner-facing body.
- Phase 5 must render PART A without altering scientific content.
- PART B is instruction/guardrail only; do not render it as learner content unless explicitly requested.
- Do not restore deprecated Step 1 material.
- Do not add new scientific content, page tags, examples, equations, figures, or regulatory claims.
- Do not generate HTML, Mermaid, SVG, or image assets from this Phase 4D file itself.

### B2. Figure Rendering Instructions

Approved figure plan from Phase 4C:

| # | Mode | Location | Source / Title | Rendering decision |
|---:|---|---|---|---|
| 1 | P | Card M1 | G&W p.97, Fig.2.70 | Text-only textbook pointer callout |
| 2 | N | Card M2 | Protein/Antibody PK Four-Gate Map | New schematic to be rendered in Phase 5 |
| 3 | P | Card M2 | R&T p.709, Fig.21-5 | Text-only textbook pointer callout |
| 4 | P | Card M3 | R&T p.712, Fig.21-9; G&W p.610, Fig.27.7 | Text-only textbook pointer callout |
| 5 | P | Card M4 | R&T p.711, Fig.21-8; G&W p.604, Fig.27.2 | Text-only textbook pointer callout |
| 6 | N | Card M4 | Data Richness → ODE Term Identifiability Map | New schematic to be rendered in Phase 5 |
| 7 | P | Card M5 | G&W p.609, Fig.27.6 | Text-only textbook pointer callout |

Rules:
- Image rights = None. Do not embed copyrighted textbook images.
- `FIGURE_POINTER` must become a text-only callout that displays Source, Why this matters, When to look, and Learner instruction.
- `FIGURE_SCHEMATIC` may be rendered as a newly designed Mermaid/inline SVG/CSS figure in Phase 5, using only the listed elements and exclusions.
- Do not propose additional figures or restore rejected candidates: lymphatic-route pointer, lymph-recovery pointer, Fig.27.3 pointer, Kd/Km visual card, diagnostic GOF workflow figure.
- Do not reproduce the textbook figure layout, color palette, or image content.

### B3. Page Tag Rendering Rules

- Preserve all source page tags, including generic tags (`[p.XX]`, `[pp.XX–YY]`, `[pp.XX, YY]`, `[p.확인 필요]`) and book-prefixed tags used in PART A (`[G p.XX]`, `[G pp.XX–YY]`, `[R&T p.XX]`, `[R&T pp.XX–YY]`).
- Render page tags visibly in HTML, including print output.
- Do not fabricate, delete, renumber, or relocate page tags.
- Do not apply page-tag regex conversion inside code blocks or inside `FIGURE_*` marker blocks.
- New tags introduced by micro-patches are verified: `[G pp.99–100]`, `[G pp.602–603]`, and existing `[G pp.599–601]` reuse.

### B4. HTML Compiler Requirements

- Render content; do not alter it.
- Produce one self-contained HTML file for PART A only.
- Use MathJax for inline and display mathematics.
- Render code blocks with copy buttons and preserve code verbatim.
- Build sticky left sidebar navigation on desktop and mobile-safe collapsed navigation on small screens.
- Every sidebar `href="#id"` must have exactly one matching body `id`; do not create duplicate ids.
- Major section headings (§1, §2, §5, §7, §8) require stable ids; concept cards in §2 should also receive stable ids.
- Enable smooth scrolling and active-section highlighting if implemented.
- Render `SELF-TEST` answers as click-to-reveal accordions; answers hidden by default.
- Add print/PDF button using browser print.
- Support responsive layout, dark/light color scheme, and print styles that keep source page tags visible.
- Marker mapping: `MASTER LENS` callout, `ANNOTATION` tooltip/inline note, `ANCHOR` bridge sentence, `TRENCH` practical tip, `CONFUSION` comparison block, `SELF-TEST` accordion, `RECAP` summary box, `FIGURE_POINTER` textbook pointer, `FIGURE_SCHEMATIC` newly rendered schematic.
- For Mermaid generation in Phase 5, use valid Mermaid syntax only; node ids must be ASCII alphanumeric/underscore, labels with special characters must be quoted, and invalid diagrams must fall back to inline SVG or CSS cards.
- Do not render PART B as learner content.

### B5. Audit Guardrails

Forbidden restorations and regression risks:

- Do not restore unsupported NDA Deficiency Letter, 6–18 month delay, $2M, 30% risk, or $60M+ claims.
- Do not restore `lymph recovery ≈ 3.2% per kDa` or 150 kDa mAb percentage extrapolation.
- Do not state that more than 90% of mAb candidates lack target/complex assays.
- Do not present NONMEM `$DES` skeleton as textbook source code.
- Do not restore ADVAN/TOL/OMEGA/minimization details as universal rules.
- Do not change `kon·L·R` back to any `kin` binding term.
- Do not count fixed `Vc=0.05 L·kg⁻¹` as one of eight estimated parameters without qualification.
- Do not reduce Full TMDD to three ODEs; preserve four-state topology.
- Do not embed textbook figures.
- Do not use Step 1 Draft v0 as a prose source.

### B6. Crucible Guardrails

- Crucible is not a raw content source at Phase 4D.
- Preserve only adopted or explicitly allowed Grade A logic already consistent with Content Lock: baseline-classifier thinking, half-life regime dependence, concentration hierarchy, data richness/identifiability, occupancy boundary, and dose-stratified diagnostics.
- Do not convert expert inference into textbook fact.
- Do not reintroduce speculative GOF signatures or regulatory reviewer statements that were rejected or compressed by Content Lock.

### B7. Deprecated and Forbidden Restorations

- Step 1 Draft v0 is deprecated.
- Restore no unsupported overclaims, unsupported numerical values, unsupported regulatory claims, source-unsupported examples, unapproved code, or unapproved figures.
- Use Step 1 only as a regression-check source through the Micro-Patch Gate.
- Process-only notes from Content Lock v2, including the Phase 4C/HTML workflow footer and adjudication tables, must remain outside PART A.

### B8. PATCH MODE Splice Verification Table

| Marker # | Anchor text | Anchor found? | Match count | Inserted? | Final location (§ + card) |
|---:|---|---|---:|---|---|
| 1 | `## ▌ Card M1 — Turnover Paradigm (`kin`/`kout`)` | YES | 1 | YES | §2 / Card M1 |
| 2 | `## ▌ Card M2 — Protein/Antibody Distinctive PK` | YES | 1 | YES | §2 / Card M2 |
| 3 | `## ▌ Card M2 — Protein/Antibody Distinctive PK` | YES | 1 | YES | §2 / Card M2 |
| 4 | `## ▌ Card M3 — TMDD 4-Phase Concentration-Time Profile` | YES | 1 | YES | §2 / Card M3 |
| 5 | `## ▌ Card M4 — Full TMDD Model ⚡ Apex Concept` | YES | 1 | YES | §2 / Card M4 |
| 6 | `## ▌ Card M4 — Full TMDD Model ⚡ Apex Concept` | YES | 1 | YES | §2 / Card M4 |
| 7 | `## ▌ Card M5 — Michaelis-Menten Approximation Boundary` | YES | 1 | YES | §2 / Card M5 |

### B9. Zero-Omission Coverage Matrix

| Domain | Required item | Evidence in PART A | Status | Action |
|---|---|---|---|---|
| C1 Scope Lock MUST concepts | M1 Turnover, M2 Protein/Antibody PK, M3 TMDD 4-phase, M4 Full TMDD, M5 MM boundary | Updated Curation Map + §2 cards M1–M5 | PRESENT | None |
| C1 Chapter role | Turnover and TMDD integrated as biologics nonlinear PK spine | §1 Big Idea, §2 M1→M5, §8 synthesis | PRESENT | None |
| C2 Required data anchors | IgX sc 40 µg·kg⁻¹ and immunoglobulin turnover | §2 M1 Clinical anchors | PRESENT | None |
| C2 Required data anchors | Estradiol turnover in 15 postmenopausal women | §2 M1 Clinical anchors | PRESENT | None |
| C2 Required data anchors | Experimental antibody monkey + r-hSOD normal/nephrectomized rats | §2 M2 G&W protein/antibody data anchors | REPAIRED_BY_MICRO_PATCH | MP-1 inserted |
| C2 Required data anchors | PK27 monoclonal antibody 1.5/5/15/45 mg·kg⁻¹ | §2 M3 PK27 dose anchor | REPAIRED_BY_MICRO_PATCH | MP-2 inserted |
| C2 Required data anchors | PK26 Efalizumab five intravenous time-courses and parameter estimates | §2 M5 B + PK26 dose anchor | REPAIRED_BY_MICRO_PATCH | MP-3 inserted |
| C2 R&T biologics anchors | Vd range, lymphatic route, FcRn, FcγR, somatropin, anakinra, ADA | §2 M2 | PRESENT | None |
| C3 Audit MUST_FIX | 8-parameter vs fixed Vc distinction | §2 M4 Apex Big Idea + Q7 | PRESENT | None |
| C3 Audit MUST_FIX | `kon·L·R` binding term; no `kin` binding typo | §2 M4 Mechanistic equations | PRESENT | None |
| C3 Audit MUST_FIX | 4-state ODE structure | §2 M4 Formal structure + Zettelkasten | PRESENT | None |
| C3 Audit MUST_FIX | Unsupported regulatory/cost claims removed | No NDA cost/time/risk scenario in PART A | PRESENT | None |
| C3 Audit MUST_FIX | Lymphatic recovery extrapolation blocked | §2 M2 Directionality, not extrapolated formula; Q9 | PRESENT | None |
| C3 Audit MUST_FIX | NONMEM code labeled as educational implementation translation | §2 M4 E | PRESENT | None |
| C4 Audit T5 problematic omissions | Somatropin absorption-rate limitation | §2 M2 B + Q6 | PRESENT | None |
| C4 Audit T5 problematic omissions | Anakinra renal disease example | §2 M2 B | PRESENT | None |
| C4 Audit T5 justifiable omissions | PD figures/tables, future section, study problems | PART B guardrails identify as omitted justifiably | JUSTIFIABLY_OMITTED | Do not restore in Phase 5 |
| C5 Phase 4C figures | 7 KEEP markers, P=5 and N=2 | PART A figure marker counts: 5 pointers, 2 schematics | PRESENT | None |
| C5 Figure rights | Image rights None; no textbook images embedded | Learner Navigation Aid + PART B B2 | PRESENT | None |
| C6 Page tags | Existing page tags preserved; new verified tags only in micro-patches | PART A + Micro-Patch Log | PRESENT | None |
| C7 Crucible Grade A | Baseline scenario, half-life regime, concentration hierarchy, data richness, occupancy boundary | M1, M2, M3, M4, M5 + mastery notes | PRESENT_COMPRESSED | None |
| C8 Deprecated Draft regression | Unsupported NDA/cost, 150 kDa percentage, unapproved code/figures not restored | PART A and B5/B7 | PRESENT | None |
| C9 Canonical integrity | Content Lock v2 learner body preserved except 7 figure insertions, 3 micro-patches, 8 labeled augmentations | Assembly logs | PRESENT | None |

### B10. Micro-Patch Log

| Patch # | Location | Source trigger | Inserted text | PDF/Audit basis | Why allowed | Page tag handling |
|---|---|---|---|---|---|---|
| MP-1 | §2 / Card M2 / B. Key mechanisms | Scope Lock required actual data anchors + Audit T5 Fig.2.71–2.73 context | G&W protein/antibody data anchors sentence | G&W pp.99–100; Audit T5 Fig.2.71–2.73 | 1-sentence context patch; already in source range and Audit-supported | Added verified [G pp.99–100] |
| MP-2 | §2 / Card M3 / A. Formal definition | Scope Lock required PK27 dose anchor + Audit T5 PK27 objectives/Fig.27.1 | PK27 dose anchor sentence | G&W pp.602–603; Audit T5 PK27/Fig.27.1 | 1-sentence data-anchor patch; does not alter model interpretation | Added verified [G pp.602–603] |
| MP-3 | §2 / Card M5 / B. When MM can work | Scope Lock required Efalizumab 5-dose anchor + Audit T5 Fig.26.1 | PK26 dose anchor sentence | G&W pp.599–601; Audit T5 PK26/Fig.26.1 | 1-sentence data-anchor patch; reinforces existing MM boundary | Used existing [G pp.599–601] tag |

### B11. Mastery Augmentation Log

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
|---|---|---|---|---|---|---|
| AUG-1 | §2 Card M1 | M / Failure-prevention | YES | CRUCIBLE_DERIVED | Baseline as model assumption improves turnover→TMDD internalization | Low |
| AUG-2 | §2 Card M2 | F | YES | CRUCIBLE_DERIVED | Prevents half-life-as-fixed-property error | Low |
| AUG-3 | §2 Card M3 | M | YES | CRUCIBLE_DERIVED | Converts Phase A–D from time sequence to concentration-regime map | Low |
| AUG-4 | §2 Card M4 | J / W | YES | CRUCIBLE_DERIVED | Connects observed species to ODE term identifiability | Low |
| AUG-5 | §2 Card M4 | F | YES | AUDIT_DERIVED | Prevents `kin`/`kon` process confusion | Low |
| AUG-6 | §2 Card M5 | J / R | YES | AUDIT_DERIVED / CRUCIBLE_DERIVED | Clarifies MM defensibility boundary without new regulatory claim | Low |
| AUG-7 | §5 Confusion Pair Dissection | M | YES | EXPERT_INFERENCE | Frames terminology as regime-dependent; no new factual claim | Medium |
| AUG-8 | §7 Self-Test | W | YES | EXPERT_INFERENCE | Adds workflow habit: link answer to observable; no new factual claim | Medium |

| Rejected candidate | Reason for rejection |
|---|---|
| Additional named regulatory scenario with NDA deficiency timing/cost | Rejected because Audit classified these numerical claims as not supported by PDF. |
| New FcRn engineering examples beyond source range | Rejected as scope expansion requiring external literature. |
| Additional Mermaid/SVG draft diagrams in Phase 4D | Rejected because Phase 4D decides figure intent only; Phase 5 renders. |

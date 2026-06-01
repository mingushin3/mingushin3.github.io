# 09_Content Lock v1

**Role**: Editor-in-Chief — pharmacometrics specialist  
**Mode**: Content Lock / Source-fidelity patched / Editorial compression applied  
**Sources**: Gabrielsson & Weiner 5e Ch.2 §2.6 + PK26 + PK27; Rowland & Tozer 5e Ch.21  
**Input integration**: Step 1 Draft v0 + Source Fidelity Audit Report v1 + Insight Crucible Report v1  
**Output scope**: §1 → §2 → §5 → §7 → §8  
**Hard constraints applied**: No HTML; no figure markers; source page tags preserved/inserted; unsupported regulatory/cost scenarios deleted or explicitly labeled; Content Lock v1 compressed relative to Step 1 Draft v0.

---

# Updated Curation Map

<!-- MASTER LENS -->

본 세션의 핵심은 “항체 PK” 자체가 아니라, **turnover 수학이 target-mediated disposition으로 확장되는 순간 어떤 자료가 어떤 파라미터를 가르치는가**를 체화하는 것이다. 10분 handout 기준으로 남길 spine은 5개뿐이다.

## MUST

| # | Concept | Locked rationale |
|---|---|---|
| M1 | **Turnover Paradigm (`kin`/`kout`)** | TMDD의 target compartment(`R`)는 endogenous turnover pool이므로, `kin/kout` 없이는 target baseline, recovery, `R0`, `kout` 식별을 설명할 수 없다. [G pp.95–97] |
| M2 | **Protein/Antibody Distinctive PK** | 큰 분자량, 제한적 Vd, lymphatic absorption, renal cutoff, FcRn salvage가 mAb PK의 “느림”과 비선형성의 생리학적 전제다. [G pp.97–102; R&T pp.701–724] |
| M3 | **TMDD 4-Phase Profile** | 곡선 모양을 Phase A–D로 읽어야 Full TMDD와 MM approximation 중 무엇을 선택할지 데이터 기반으로 판단할 수 있다. [G pp.603–610; R&T pp.711–712] |
| M4 | **Full TMDD Model** ⚡ **Apex Concept** | ligand, target, complex, sink가 하나의 ODE system으로 결합되는 지점이며, PD와 PK가 같은 수식으로 묶인다. [G pp.603–609; R&T pp.711–712] |
| M5 | **Michaelis-Menten Approximation Boundary** | MM은 limited dose range에서는 쓸 수 있으나, low-concentration extrapolation과 occupancy 판단에서 구조적 bias를 만든다. [G p.609; R&T p.712] |

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

# Adjudication Table Summary

## A. Source Fidelity Audit v1

| Source | Item | Verdict | Rationale |
|---|---|---|---|
| Audit T1 | Turnover equations Eq.2:237–2:244 | ADOPT | 모든 핵심 turnover 식과 단위가 G&W pp.95–96와 일치하므로 보존한다. |
| Audit T1 | Bucket 10 L / 1 L·min⁻¹ and water 42 L / 2.5 L·day⁻¹ | ADOPT | 직관 보조로 적합하고 p.96에 직접 근거가 있다. |
| Audit T1 | Fig.2.70 message: `kin` vs `kout` manipulation | ADOPT | turnover의 비대칭성을 설명하는 핵심 메시지이므로 M1에 유지한다. |
| Audit T1 | Protein absorption: low, erratic, delayed after extravascular routes | ADOPT | G&W와 R&T 양쪽에서 지지되며 M2의 출발점이다. |
| Audit T1 | Lymph flow about 2 L/day and plasma protein return | ADOPT | mAb sc absorption 직관에 유용하되 정량 과잉 외삽은 삭제한다. |
| Audit T1 | MW threshold `>16 kDa`, R&T `>15,000–20,000 g/mol` | ADOPT | lymphatic absorption gate 설명에 보존한다. |
| Audit T1 | Protein Vd range `Vss ≈ 0.04–0.23 L·kg⁻¹` | ADOPT | 항체가 small molecule처럼 넓게 퍼지지 않는다는 핵심 근거다. |
| Audit T1 | Antibody monkey, r-hSOD, IgX examples | PARTIAL_ADOPT | 핵심 anchor인 IgX는 유지하고, monkey/r-hSOD는 M2 context로 압축한다. |
| Audit T1 | IgG `t1/2=23 days` and mAb approx. 21 days | PARTIAL_ADOPT | endogenous IgG 23일과 therapeutic mAb approx. 21일을 혼용하지 않도록 분리 표기한다. |
| Audit T1 | Estradiol, body temperature, feedback examples | PARTIAL_ADOPT | independent card로 확장하지 않고 turnover boundary/context로 압축한다. |
| Audit T1 | PK26 Efalizumab reduced MM model | ADOPT | MM approximation이 제한된 범위에서 작동할 수 있음을 보여주는 필수 anchor다. |
| Audit T1 | PK27 doses and dataset richness I–III | ADOPT | Full TMDD identifiability의 중심 근거이므로 M3/M4에 유지한다. |
| Audit T1 | “8-parameter full TMDD” wording | PARTIAL_ADOPT | “8 estimated parameters + fixed `Vc=0.05 L·kg⁻¹`; fixed `Vc`까지 세면 9 structural quantities”로 수정한다. |
| Audit T1 | Draft recap list counting 9 quantities as 8 | ADOPT | 오류이므로 수정한다. |
| Audit T1 | Zettelkasten “세 ODE” | ADOPT | ligand central/peripheral + target + complex의 4-state ODE로 수정한다. |
| Audit T1 | `kin·C_L·R` binding term typo | ADOPT | mass-action binding term은 `kon·C_L·R`이므로 즉시 교정한다. |
| Audit T1 | `Kd=koff/kon`, `Km=(koff+ke(RL))/kon` | ADOPT | M3/M5 구분의 핵심 식으로 유지한다. |
| Audit T1 | Table 27.2 CV% hierarchy | ADOPT | 데이터 richness가 parameter precision을 어떻게 개선하는지 보여주는 핵심 근거다. |
| Audit T1 | MM `Km` 3.7 vs 0.03 | ADOPT | “100배 규모” 대신 PK27의 123× over-prediction으로 구체화한다. |
| Audit T1 | MM validity: 90–95% occupancy, `C >> R0` | ADOPT | M5의 boundary condition으로 유지한다. |
| Audit T1 | NONMEM `$DES` code | PARTIAL_ADOPT | 교과서 원문 코드가 아니므로 `[교과서 외 구현 번역 예시]` 라벨을 붙인다. |
| Audit T1 | ADVAN13, `$COV`, `$OMEGA`, minimization failure details | PARTIAL_ADOPT | 교과서 외 실무 구현 주의로 짧게 라벨링하고 과잉 진단 narrative는 압축한다. |
| Audit T1 | NDA Deficiency Letter, 6–18개월, $2M, 30%, $60M+ | REJECT | PDF source가 없고 구체 수치가 사실처럼 보이므로 삭제한다. |
| Audit T1 | `lymph recovery ≈ 3.2% per kDa`, 150 kDa mAb >80% | REJECT | R&T Fig.21-16 범위 밖의 선형 외삽이므로 정량 문장을 삭제하고 방향성만 남긴다. |
| Audit T1 | “90% 이상의 mAb 후보 target/complex assay 없음” | REJECT | PDF source가 없으므로 삭제한다. |
| Audit T1 | “16 ODE bispecific” extension | PARTIAL_ADOPT | scope creep이므로 M4 limitation에 1문장 `[교과서 외 확장]`로만 남긴다. |
| Audit T2 | Basic turnover, IgX, Table 2.11, baseline scenarios | ADOPT | M1의 필수 수식·임상 anchor·assumption boundary를 구성한다. |
| Audit T2 | Protein absorption, Vd, renal/hepatic handling | ADOPT | M2의 필수 ADME mechanism이다. |
| Audit T2 | Somatropin Fig.21-17 | ADOPT | sc absorption-rate-limited kinetics를 설명하는 1문장 context로 추가한다. |
| Audit T2 | Anakinra Fig.21-18/Table 21-16 | ADOPT | renal disease가 kidney-eliminated protein drug에 미치는 영향을 1문장으로 유지한다. |
| Audit T4 #1 | Full TMDD parameter count | ADOPT | Apex Concept 신뢰도에 직접 영향이 있으므로 교정한다. |
| Audit T4 #2 | Binding term typo | ADOPT | `kin`/`kon` 혼동은 수식 오류이므로 교정한다. |
| Audit T4 #3 | ODE count | ADOPT | 4-state ODE로 수정한다. |
| Audit T4 #4 | Unsupported regulatory/cost scenario | ADOPT | 삭제 또는 명시 라벨이 필요하며 본 Content Lock에서는 삭제를 기본으로 한다. |
| Audit T4 #5 | Unsupported lymphatic extrapolation | ADOPT | directionality만 유지한다. |
| Audit T4 #6 | NONMEM code label | ADOPT | 교과서 외 구현 번역으로 명시한다. |
| Audit T4 #7 | “Step 2 HTML” completion block | ADOPT | 현재 산출물은 Content Lock이므로 HTML 직행 문구를 삭제한다. |
| Audit T4 #8 | Fig.27.6 + Peletier & Gabrielsson interpretation | PARTIAL_ADOPT | 교재 안에서 언급된 figure 사실은 유지하되 추가 문헌 해석은 확장하지 않는다. |
| Audit T4 #9–10 | Assay availability / NDA section details | REJECT | PDF source가 없으므로 삭제한다. |
| Audit T4 #11–13 | Somatropin, Anakinra, Table 21-13 | ADOPT | M2 context로 압축 삽입한다. |
| Audit T4 #14–16 | Body temperature, nomenclature, therapeutic-use long tables | PARTIAL_ADOPT | context로만 유지하고 세부 암기 항목은 삭제한다. |
| Audit PATCH 1–9 | Minimal Patch List | ADOPT | 본문에 모두 반영한다. |
| Audit T6 | Figure inventory | NOT_ADJUDICATED | 지시대로 Phase 4C로 unchanged flow; 본 산출물에는 figure marker를 넣지 않는다. |

## B. Insight Crucible Report v1

| Source | Item | Verdict | Rationale |
|---|---|---|---|
| Crucible T1(a-1) | Fig.2.77 as baseline-subtraction decision classifier | ADOPT | “baseline=predose” 자동 코딩을 막는 핵심 internalization이다. |
| Crucible T1(a-2) | “이 mAb의 half-life는?” 질문 자체의 부정확성 | ADOPT | TMDD-active dose 영역에서는 half-life가 dose/concentration dependent임을 M2/M3에 반영한다. |
| Crucible T1(a-3) | 4 phases as concentration hierarchy, not merely time sequence | ADOPT | Phase A–D를 `Kd`, `Km`, `R0`와 연결하는 고급 직관이다. |
| Crucible T1(a-4) | Data source isolates ODE terms | PARTIAL_ADOPT | M4 identifiability paragraph로 압축해 삽입한다. |
| Crucible T1(b) | Three decision nodes: `$PK/$DES`, sampling, NDA narrative | PARTIAL_ADOPT | §8에 두 가지 capability로 압축하고 구체 NDA wording은 삭제한다. |
| Crucible T1(c) | Veteran GOF reading patterns | PARTIAL_ADOPT | §8 Professional Moat에 “dose-stratified residual” 중심으로 1문장 반영한다. |
| Crucible T2(a-1) | FcRn evidence question | PARTIAL_ADOPT | source-supported mechanism 수준으로 반영하고 specific reviewer wording은 삭제한다. |
| Crucible T2(a-2) | Occupancy verification for MM approximation | ADOPT | M5 boundary condition에 per-subject minimum occupancy 확인 절차로 삽입한다. |
| Crucible T2(a-3) | MTX–FcγR clearance impact | PARTIAL_ADOPT | R&T의 adalimumab clearance 29–44% 감소 사실만 M2 limitation에 유지한다. |
| Crucible T2(b-1) | Inverted Phase A | REJECT | 교과서 외 NONMEM failure signature로 과잉 확장되어 본문에서는 삭제한다. |
| Crucible T2(b-2) | Dose-stratified OMEGA inflation | PARTIAL_ADOPT | §8 diagnostic GOF capability에 일반 원리로만 반영한다. |
| Crucible T2(b-3) | Phantom Linearity / Low-Concentration CWRES Drift | PARTIAL_ADOPT | unsupported simulation narrative는 제거하고 저농도 residual drift라는 진단 직관만 남긴다. |
| Crucible T2(c) | Apparent affinity vs true affinity | ADOPT | §5 Pair 3 하단에 `Km`과 thermodynamic `Kd`의 문서 분리를 추가한다. |
| Crucible T3 Tip 1 | `$DES` BIND term needs `Vc` multiplication | ADOPT | `[교과서 외 구현 번역 예시]` 아래 trench tip으로 삽입한다. |
| Crucible T3 Tip 2 | ADVAN13 TOL | REJECT | 실행환경별 권장값이 교과서 source 밖이며 본 handout에 과하다. |
| Crucible T3 Tip 3 | Free vs total target assay | PARTIAL_ADOPT | M4 assumptions에 “assay species 확인”으로 압축 삽입한다. |
| Crucible T3 Tip 4 | `R0` baseline record | PARTIAL_ADOPT | M1/M4 identifiability note로 압축한다. |
| Crucible T3 Tip 5 | `Vc` fixing sensitivity | PARTIAL_ADOPT | fixed `Vc`의 한계로 M4 assumptions에 반영한다. |
| Crucible T4 deletion | “100배 규모” → PK27 123× | ADOPT | §1 Big Idea와 M5에 반영한다. |
| Crucible T4 deletion | Card M4 C-2 clinical scenarios | ADOPT | 세 시나리오를 1문장 mechanistic statement로 압축한다. |
| Crucible T4 deletion | M5 B-2 duplicate memo | ADOPT | 반복 설명 삭제, numeric anchor만 유지한다. |
| Crucible T4 deletion | M2 sc bioavailability table compression | ADOPT | representative entries 중심으로 압축한다. |
| Crucible T4 deletion | §7 Q4 caveat compression | ADOPT | 정답 + 1문장 caveat로 압축한다. |
| Crucible T4 deletion | §8 Professional Moat 4 → 2 capabilities | ADOPT | narrative justification과 diagnostic GOF reading으로 압축한다. |
| Crucible Grade A A1–A7 | Must incorporate items | ADOPT | 모두 본문에 반영한다. |
| Crucible Grade B B1 | Data-phase mapping | ADOPT | M4 identifiability에 반영한다. |
| Crucible Grade B B2 | GOF reading | PARTIAL_ADOPT | §8에 1문장으로 반영한다. |
| Crucible Grade B B3–B4 | FcRn/MTX risk | PARTIAL_ADOPT | M2 limitation에 source-supported 범위로 반영한다. |
| Crucible Grade B B5 | NONMEM signatures | PARTIAL_ADOPT | full signature list는 삭제하고 §8 diagnostic capability로 압축한다. |
| Crucible Grade B B6 | Apparent vs true affinity | ADOPT | §5 Pair 3에 반영한다. |
| Crucible Grade B B7 | Tips 2–5 | PARTIAL_ADOPT | 교과서 외 값·권장치 삭제, assay/`R0`/`Vc` sensitivity만 반영한다. |
| Crucible Grade C C1–C6 | Scope creep / unsupported / duplicates | REJECT | Content Lock 목적상 모두 제외한다. |

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

> **항체의 비선형 PK는 “큰 약물이 천천히 빠진다”가 아니라, ligand가 endogenous target turnover system에 결합하면서 생기는 concentration-dependent clearance다. Full TMDD를 MM으로 줄이면 제한된 dose range에서는 맞아 보일 수 있지만, PK27에서는 `Km`이 0.03에서 3.7로 약 123배 over-predicted되어 low-concentration extrapolation이 구조적으로 틀어졌다.** [G p.609]

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

Turnover는 endogenous compound의 baseline이 고정된 숫자가 아니라 **zero-order input `kin`과 first-order loss `kout·A`가 유지하는 동적 평형**임을 말한다. TMDD의 target `R`도 이 구조를 따른다. 따라서 mAb가 target에 결합한다는 것은 외부 ligand가 endogenous turnover pool에 개입한다는 뜻이다. [G pp.95–96]

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

10 L 욕조에 1 L·min⁻¹로 물이 들어오면 turnover time은 10분이다. 사람 몸의 물 42 L와 하루 intake 2.5 L를 쓰면 water turnover time은 약 17일이다. 이 단순한 예가 endogenous IgG, target receptor, hormone turnover와 같은 수학이다. [G p.96]

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

## ▌ Card M2 — Protein/Antibody Distinctive PK

<!-- MASTER LENS -->

### [개념 Big Idea]

Protein drugs와 mAbs는 small molecules와 달리 “잘 녹고 전신으로 퍼진 뒤 간/신장으로 빠지는” 물질이 아니다. 큰 분자량, 제한된 capillary permeability, lymphatic input, proteolysis, receptor-mediated uptake, FcRn salvage가 ADME의 기본 문법이다. [G pp.97–100; R&T pp.701–724]

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

**Lymphatic absorption**: G&W는 sc 투여된 proteins/peptides의 absorption이 low, erratic, delayed라고 설명하고, lymph flow를 about 2 L/day로 제시한다. R&T Table 21-13은 larger molecules `>15,000–20,000 g/mol`가 primarily lymphatics를 통해 systemic circulation에 들어간다고 정리한다. [G p.97; R&T p.718]

**Directionality, not extrapolated formula**: R&T Fig.21-16은 sheep에서 0.246–19 kDa 범위의 water-soluble compounds가 molecular weight 증가와 함께 lymph recovery가 증가하는 방향성을 보여준다. 이것은 150 kDa mAb의 recovery를 선형식으로 정량 예측하는 근거가 아니다. [R&T p.720]

**Absorption-rate limitation**: Somatropin은 i.v. half-life가 약 2.1 h인데 sc 후 plasma concentration이 길게 지속되어, 큰 단백질의 terminal profile이 elimination이 아니라 slow input에 의해 rate-limited될 수 있음을 보여준다. [R&T p.721]

**Renal disease**: anakinra(17,258 g/mol)는 renal function 감소에 따라 clearance가 감소하고 exposure가 증가하는 예시다. 반대로 full-size antibodies와 매우 큰 proteins는 glomerular filtration을 거의 받지 않아 renal disease 영향이 일반적으로 작다. [R&T p.724]

### C. FcRn and FcγR

FcRn은 endogenous IgG와 therapeutic mAbs의 long half-life를 설명하는 핵심 salvage mechanism이다. R&T는 mAb half-life가 IgG에 가까워 approximately 21 days인 경우가 많다고 설명하지만, 이는 모든 mAb의 고정 half-life가 아니다. FcRn binding, target-mediated clearance, immunogenicity, dose level에 따라 apparent half-life는 달라진다. [R&T pp.708–710]

FcγR-mediated clearance도 무시할 수 없다. R&T는 methotrexate가 rheumatoid arthritis patients에서 adalimumab clearance를 29–44% 감소시킬 수 있음을 제시한다. 따라서 “FcγR은 peripheral detail”이 아니라, 특정 질환/병용약물 맥락에서는 clearance covariate가 될 수 있다. [R&T p.706]

<!-- ANCHOR -->

### D. Why this matters for TMDD

mAb의 slow absorption과 small Vd를 모르면 TMDD curve를 잘못 읽는다. sc 투여에서는 Phase A의 rapid binding signature가 absorption phase와 confound될 수 있고, FcRn rescue가 있는 mAb에서는 “terminal slope = simple elimination half-life”라는 해석이 위험해진다.

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

## ▌ Card M3 — TMDD 4-Phase Concentration-Time Profile

<!-- MASTER LENS -->

### [개념 Big Idea]

TMDD curve는 “비선형 곡선”이 아니라 **ligand concentration이 target concentration, `Kd`, `Km`, saturation boundary를 지나가며 dominant clearance route가 바뀌는 기록**이다. 따라서 Phase A–D는 단순 시간 구간이 아니라 concentration hierarchy다. [G pp.604–610; R&T pp.711–712]

### A. Formal definition

PK27과 R&T는 characteristic TMDD profile을 네 phase로 설명한다. [G p.610; R&T p.712]

| Phase | Dominant process | Interpretation |
|---|---|---|
| A | rapid second-order binding | ligand and target equilibrate rapidly |
| B | slow first-order disposition | target route saturated; nonspecific route dominates |
| C | mixed-order disposition | target partly saturated; linear and target-mediated routes coexist |
| D | `koff` and `ke(RL)`-driven terminal phase | very low ligand; target-specific elimination becomes visible |

<!-- ANCHOR -->

### B. Concentration hierarchy, not just time sequence

A beginner reads Phase A→B→C→D as a time sequence. A modeler reads the same curve as ligand concentration crossing `R0`, `Km`, and `Kd`. In PK27, `R0≈12 mg·L⁻¹`, `Km≈0.03 mg·L⁻¹`, and `Kd` is defined by `koff/kon`; these thresholds explain why low-dose curves reveal different slopes than high-dose curves. [G pp.603–610]

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

## ▌ Card M4 — Full TMDD Model ⚡ Apex Concept

<!-- MASTER LENS -->

### [⚡ Apex Big Idea]

Full TMDD는 ligand disposition, target turnover, ligand-target binding, complex loss를 하나의 mechanistic system으로 묶는다. PK27은 이를 “eight-parameter full TMDD model”로 부르지만, `Vc=0.05 L·kg⁻¹`를 fixed한 상태에서 Table 27.2가 8 estimated parameters를 보고한다. fixed `Vc`까지 structural quantity로 세면 ligand central, ligand tissue, target, complex의 4 state와 9 structural quantities가 존재한다. [G pp.603, 608–609]

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

The binding term is `kon·L·R`, not `kin·L·R`. `kin` belongs to target synthesis; `kon` is the second-order on-rate for ligand-target binding. [G p.604; G pp.606–607]

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

## ▌ Card M5 — Michaelis-Menten Approximation Boundary

<!-- MASTER LENS -->

### [개념 Big Idea]

Michaelis-Menten approximation은 Full TMDD의 target/complex subsystem을 `Vmax`와 `Km`로 줄이는 것이다. 문제는 fit이 아니라 **어느 concentration/occupancy range에서 이 reduction이 구조적으로 허용되는가**이다. [G p.609; R&T p.712]

### A. Formal definition

Reduced model은 target-mediated route를 다음 형태로 압축한다.

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

### C. When MM breaks

In PK27, MM fitted the three highest concentration profiles relatively well but showed severe systematic deviation at the lowest concentration profile. The estimated `Km=3.7` was dramatically over-predicted versus `0.03` from the TMDD model. [G p.609]

The clinical lesson is not “never use MM.” The lesson is: **do not use MM outside the concentration/occupancy domain in which target saturation is demonstrated**.

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

# §8 Meta-Frame & Big Picture

## A. Positioning

<!-- MASTER LENS -->

이 세션은 biologics pharmacometrics의 입구다. Small molecule PK에서는 clearance와 Vd를 중심으로 설명할 수 있었지만, mAb에서는 target biology, binding kinetics, complex sink, FcRn salvage, lymphatic input이 PK 곡선의 형태를 만든다.

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

## Next workflow note

Next: Phase 4C Visual Pedagogy Triage, then HTML compile. 본 Content Lock v1은 텍스트 확정본이며, figure markers는 의도적으로 삽입하지 않았다.


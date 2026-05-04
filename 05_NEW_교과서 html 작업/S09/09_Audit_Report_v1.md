# 09_Audit Report v1

**업무 형태:** 파일 분석 / 웹 검색 OFF / PDF 대조 감사  
**입력:** `09_G_TMDD·항체 PK 거대분자 비선형.pdf` + `09_T_TMDD·항체 PK 거대분자 비선형.pdf` + `09_step1_draft_v0.md` + `S09_phase1_patch memo.md` + 감사 프롬프트  
**산출:** Source Fidelity Audit v1  
**역할:** Source Fidelity Auditor — 검증 전용. 문장 개선·교육적 강화·비유 추가는 수행하지 않음.

---

## 0. Executive Verdict

```text
Phase 1 재실행: 불필요
Phase 2 Source Fidelity Audit: 필요했고, 본 보고서가 그 역할을 수행
HTML 직행: 금지
치명적 붕괴: 없음
MUST_FIX: 있음
최종 판정: Draft v0는 구조적으로 성공했으나, 출처 미지원 실무 확장과 일부 파라미터 카운팅/표기 오류를 Phase 4A에서 반드시 패치해야 함
```

### 핵심 감사 판정

| 항목 | 판정 |
|---|---:|
| Scope / curation 구조 | 양호 |
| MUST 5개 선정 | 양호 |
| G&W §2.6 + PK26/PK27 반영 | 양호 |
| R&T Ch.21 반영 | 양호 |
| 수식·수치 source fidelity | 중간 이상, 단 MUST_FIX 존재 |
| 실무·규제 확장 source fidelity | 취약 |
| Figure/Table coverage | 핵심 도해는 대체로 반영, 일부는 Phase 4C에서 view instruction 필요 |

### 최우선 MUST_FIX

1. **Full TMDD “8-parameter” 표현 정리 필요.** 원문 PK27은 “eight-parameter full TMDD model”이라고 부르지만, `Vc`는 `0.05 L·kg⁻¹`로 fixed된 초기 가정이다. Draft는 `Cl_L, Vc, Cl_d, Vt, kon, koff, ke(RL), R0, kout`처럼 9개 structural quantity를 한꺼번에 “8 parameter”로 부르고 있어 혼선이 발생한다.
2. **M4 B-1의 binding term 오기:** `kin·C_L·R`는 **ERROR**. Source 및 Draft 수식 본문상 `kon·C_L·R`가 맞다.
3. **Zettelkasten의 “세 ODE(L, R, RL)” 표현 오류:** Full TMDD는 ligand central/peripheral + target + complex의 4-state ODE 구조이다. “3 ODE”는 오류다.
4. **NDA Deficiency Letter, 6–18개월, 200만 달러, 30% risk, $60M+ 등은 PDF source에 없음.** 모두 `[교과서 외 실무 가상 시나리오]`로 라벨링하거나 삭제해야 한다.
5. **lymph recovery ≈ 3.2% per kDa 및 150 kDa mAb >80% 외삽은 PDF source 직접값이 아님.** R&T Fig.21-16은 0.246–19 kDa 범위의 sheep lymph recovery 방향성을 보여줄 뿐, 150 kDa mAb 정량 예측을 지지하지 않는다.
6. **NONMEM `$DES` control stream은 원문 수록 코드가 아님.** PK27 ODE의 교육용 구현 번역으로 라벨링해야 한다.
7. **Draft 말미의 “계속 → Step 2 HTML” 흐름은 현재 워크플로우와 충돌.** Source Fidelity Audit 후 Phase 4A 패치를 거쳐야 한다.

---

## T1: Equation/Numerical Audit

| Item | Draft v0 Expression | PDF Source | Classification | Correction |
|---|---|---|---|---|
| Turnover ODE | `dA/dt = kin − kout·A` | G&W p.95, Eq.2:237 | MATCH | 없음 |
| Baseline steady state | `dA/dt = kin − kout·A = 0` | G&W p.95, Eq.2:238 | MATCH | 없음 |
| Input-output relation | `kin = kout·A0` | G&W p.96, Eq.2:239 | MATCH | 없음 |
| Fractional turnover | `kout = kin/A0` | G&W p.96, Eq.2:240 | MATCH | 없음 |
| Baseline amount | `A0 = kin/kout` | G&W p.96, Eq.2:241 | MATCH | 없음 |
| Turnover time | `tt = A0/kin = 1/kout` | G&W p.96, Eq.2:242 | MATCH | 없음 |
| `tt = Vss/Cl = MRT` | `tt = C0·Vss/(C0·Cl) = Vss/Cl = MRT` | G&W p.96, Eq.2:243 | MATCH | 없음 |
| Half-life-turnover time | `t1/2 = ln(2)/kout = ln(2)·tt` | G&W p.96, Eq.2:244 | MATCH | 없음 |
| Bucket analogy | 10 L bucket / 1 L·min⁻¹ → 10 min | G&W p.96 | MATCH | 없음 |
| Human body water turnover | 42 L / 2.5 L·day⁻¹ → ~17 days | G&W p.96 | MATCH | 없음 |
| Fractional turnover example | `0.1 h⁻¹ = 10% per hour` | G&W p.96 | MATCH | 없음 |
| Fig.2.70 message | `kin` 변화 = SS level만 변화, Tss 불변; `kout` 변화 = SS level과 Tss 모두 변화 | G&W p.97, Fig.2.70 | MATCH | 없음 |
| Protein absorption | proteins/peptides: low, erratic, delayed after extravascular routes | G&W p.97; R&T pp.718–721 | MATCH | 없음 |
| Lymph flow | about `2 L/day` | G&W p.97 | MATCH | 없음 |
| Plasma protein return | ~50% of total plasma protein pool returned daily | G&W p.98 | MATCH | 없음 |
| Lymphatic MW threshold | `>16 kDa` lymphatic distribution/absorption, `<1 kDa` not absorbed by lymphatics | G&W p.98 | MATCH | 없음 |
| R&T parenteral threshold | `>15,000–20,000 g/mol` primarily via lymphatics | R&T p.718, Table 21-13 | MATCH | 없음 |
| Protein Vd range | `Vss ≈ 0.04–0.23 L·kg⁻¹` | R&T p.701, Table 21-6 context | MATCH | 없음 |
| G&W Table 2.10 values | EPO ~49/50 mL·kg⁻¹, albumin 100, IL-3 320 | G&W p.98, Table 2.10 | MATCH | 없음 |
| Renal elimination MW ranges | `<500`, `500–1000`, `1000–50,000`, `50,000–200,000` mechanisms | G&W pp.98–99 | MATCH | 없음 |
| Antibody monkey model | cynomolgus, five consecutive ascending infusions, `0.77–771 µmol·kg⁻¹`, `CL 6 mL·h⁻¹·kg⁻¹`, `Vss 4 L·kg⁻¹` | G&W p.99, Fig.2.71 | MATCH | 없음, 단 `Vss=4 L·kg⁻¹`는 원문 경고와 함께만 사용 |
| r-hSOD rat model | normal/nephrectomized rats; 20 mg during 15 s; CL 3.0 vs 0.22 mL·h⁻¹; Vss 45 vs 30 mL | G&W pp.99–100, Figs.2.72–2.73 | MATCH | 없음 |
| IgX dose | `40 µg·kg⁻¹ sc`, healthy volunteer, baseline `32 µg·L⁻¹` | G&W pp.100–101, Fig.2.74 | MATCH | 없음 |
| IgX PK estimates | `Cl/F=0.03 L·h⁻¹·kg⁻¹`, `V/F=0.10 L·kg⁻¹`, `kin=0.78 µg·h⁻¹·kg⁻¹`, `tt=2.7 h`, `MIT=1.8 h`, `t1/2=2.5 h`, `kout=0.27 h⁻¹`, pool `2.3 µg·kg⁻¹` | G&W p.101 | MATCH | 없음 |
| Ig Table 2.11 | IgG `t1/2=23 days`, fractional catabolic `6.7% plasma pool·day⁻¹`, turnover `33 mg·kg⁻¹·day⁻¹` | G&W p.102, Table 2.11 | MATCH | 없음 |
| FcRn half-life claim | mAb t1/2 typically close to IgG, approx. `21 days` | R&T p.708 | MATCH | 없음. G&W Table 2.11의 endogenous IgG 23일과 R&T의 approx. 21일을 혼용하지 않도록 주석 권장 |
| Estradiol data | 15 postmenopausal women; mean `kin=19 µg·24h⁻¹`, `Cl=1.6 L·min⁻¹`, `Vss=50 L`, `t1/2=26 min`, `MRT=18 min` | G&W p.103, Table 2.12 | MATCH | 없음 |
| Estradiol conclusion | lowered E2 levels due to reduced turnover rather than increased clearance | G&W p.104 | MATCH | 없음 |
| Body temperature doses | rats, sc `0, 30, 125, 500, 2000 µg` 8-OH-DPAT | G&W p.106 | MATCH | 없음 |
| Body temperature Dmax | `3°C (Imax/kout)` | G&W p.107 | MATCH | 없음 |
| Peletier baseline model | Eq.2:256–2:258; `Tref 37.5 ± 0.5°C`, amplitude `3%` | G&W pp.108–109 | MATCH | 없음 |
| Table 2.14 | `α=0.026 min⁻¹`, `b=0.0037 min⁻¹`, `Dark=0.053`, `Tref=37.3°C`, `Amplitude=0.033` | G&W p.109, Table 2.14 | MATCH | 없음 |
| IgG negative feedback | IgG half-life shortens to limit ~11 days at serum `30 mg·mL⁻¹` | G&W p.111, Fig.2.84 | MATCH | 없음 |
| PK26 doses | Draft says `5 i.v. doses 0.1–10 mg·kg⁻¹` | G&W PK26 Fig.26.1; R&T Fig.21-7 | MATCH | 없음 |
| PK26 estimates | `Vt=0.061`, `Vmax=0.039`, `Km=0.161`, `CLd=0.031`, `CLL=0.007`; CV% 13/12/44/23/10 | G&W p.601, Table 26.1 | MATCH | 없음 |
| PK26 Full TMDD failure | Full TMDD failed due to lack of target/complex and no kon/koff/kd information | G&W p.601 | MATCH | 없음 |
| PK27 doses | `1.5, 5, 15, 45 mg·kg⁻¹` rapid IV injections | G&W pp.602–603, Figs.27.1/27.4/27.5 | MATCH | 없음 |
| PK27 dataset richness | I=L only, II=L+R, III=L+R+RL | G&W p.603 | MATCH | 없음 |
| `Vc=0.05 L·kg⁻¹` fixed | Draft states Vc fixed at 0.05 L/kg | G&W p.603 and p.608 | MATCH | 없음 |
| “8-parameter full TMDD” | Draft repeatedly says 8-parameter ODE system | G&W p.603 says purpose is fitting eight-parameter full TMDD; Table 27.2 reports 8 estimates with Vc fixed | MATCH_WITH_WARNING | 반드시 “8 estimated parameters + fixed Vc”로 정리 |
| “8 parameters” list | Draft recap lists `Cl_L, Vc, Cl_d, Vt, k_on, k_off, k_e(RL), R_0, k_out` as 8 parameters | G&W Fig.27.2/Table 27.2 | ERROR | `Vc`를 포함하면 9 structural quantities. Table 27.2의 8 estimated/reported parameters는 `Cl, Kon, Koff, Vt, Cld, Kout, R0, Ke(RL)`이며 `Vc=0.05 L·kg⁻¹` fixed |
| Full TMDD ODE count | Draft main text says 4 ODE, but Zettelkasten says “세 ODE(L, R, RL)” | G&W Eq.27:1–27:3; R&T Eq.21-1–21-4 | ERROR | ligand central + ligand tissue + target + complex의 4 state로 정리 |
| Binding term label | Draft M4 B-1 says `kin·C_L·R` term | G&W/R&T TMDD equations | ERROR | `kon·C_L·R`로 수정. `kin`은 target synthesis/turnover input이므로 binding on-rate가 아님 |
| Kd definition | `Kd = koff/kon` | G&W Fig.27.1/27.4/27.5; R&T p.711/Fig.21-9 | MATCH | 없음 |
| Km definition | `Km = (koff + ke(RL))/kon` | G&W Fig.27.1/27.4/27.5; R&T p.711/Fig.21-9 | MATCH | 없음 |
| Table 27.2 CV% hierarchy | kon 17→2→1; koff 27→13→3; ke(RL) 27→23→2 | G&W p.609, Table 27.2 | MATCH | 없음 |
| MM Km bias | `3.7 vs 0.03`, approx. 123× over-prediction | G&W p.609 and Fig.27.6 | MATCH | 없음 |
| “100배 규모” wording | “100배 규모의 체계적 바이어스” | G&W p.609: 3.7 vs 0.03 | MATCH | 정확히는 123배; “100배 규모”는 허용 가능 |
| PK27 four phases | A rapid second-order, B slow first-order saturated, C mixed-order, D koff/ke(RL)-driven | G&W p.610 Fig.27.7; R&T p.712 Fig.21-9 | MATCH | 없음 |
| Molar units note | Molar units preferable, mg acceptable in PK27 because synthetic known binding setup | G&W p.610 | MATCH | 없음 |
| MM validity conditions | `90–95% occupancy`; if occupancy < Kd or biomarker potency, MM may not suffice | G&W p.609; R&T p.712 says MM adequate when drug concentrations significantly exceed target or occupancy close to 100% | MATCH | 없음 |
| `C >> R0` as validity condition | Draft states `C >> R0` | R&T p.712: drug concentrations significantly exceed target concentrations | MATCH | 없음 |
| R&T QE condition | internalization rate much smaller than dissociation rate | R&T p.712 | MATCH | 없음 |
| NONMEM `$DES` code | Full control-stream-like skeleton | PDF source has ODEs, not NONMEM code | NOT_IN_SOURCE | `[교과서 외 구현 번역 예시]`로 라벨링 |
| NONMEM ADVAN13 | Draft says ADVAN13/general nonlinear use required | PDF source does not provide NONMEM ADVAN13 | NOT_IN_SOURCE | 출처 태그 필요 또는 제거 |
| NONMEM failure / `$COV` / `$OMEGA` | Draft mentions minimization failure, omega fixes | PDF source 없음 | NOT_IN_SOURCE | 실무 해석으로 라벨링 |
| NDA Deficiency Letter | multiple instances | PDF source 없음 | NOT_IN_SOURCE | 삭제 또는 `[교과서 외 실무 가상 시나리오]` |
| 6–18개월, $2M, 30% risk, $60M+ | Draft boss dilemma | PDF source 없음 | NOT_IN_SOURCE | 삭제 또는 명시적 가상 시나리오 라벨 |
| lymph recovery `3.2% per kDa` | Draft regression from Fig.21-16 | R&T Fig.21-16 gives points and trend, no regression equation | NOT_IN_SOURCE | 계산값으로 라벨. 150 kDa 외삽은 정량 예측으로 사용 금지 |
| `mAb 150 kDa lymph recovery >80%` | Draft extrapolation | R&T Fig.21-16 data only to 19 kDa | ERROR/NOT_IN_SOURCE | “MW 증가에 따라 lymph recovery 증가”로 제한. 150 kDa 정량 외삽 삭제/격하 |
| “90% 이상의 mAb 후보 target/complex assay 없음” | Draft M5 Big Idea | PDF source 없음 | NOT_IN_SOURCE | 실무 추정 라벨 필요 |
| “16 ODE bispecific” | Draft limitation | PDF source 없음 | NOT_IN_SOURCE | out-of-source extension 라벨 필요 |
| “sample당 $X”, “D-optimal design”, “비용 절반” | Draft §8 | PDF source 없음 | NOT_IN_SOURCE | 실무 확장/가상 시나리오 라벨 필요 |

**T1 footnote:** Draft의 수식 대부분은 교재 수식 또는 교재 수식의 교육적 재표현으로 확인된다. 오류는 주로 (i) `kon`/`kin` 오기, (ii) 8 estimated parameters와 fixed `Vc`를 혼합한 parameter count, (iii) 교재 외 규제·NONMEM·비용 시나리오의 source tag 부재에서 발생한다.

---

## T2: Examples & Data Audit

| Item | Draft v0 Status | PDF Location | Classification | Importance | Action |
|---|---|---|---|---:|---|
| Basic turnover model | M1 MUST | G&W §2.6.1 pp.94–97, Figs.2.69–2.70 | INCLUDED_CORRECT | HIGH | 유지 |
| Bucket/water example | M1 context | G&W p.96 | INCLUDED_CORRECT | MEDIUM | 유지 |
| Metabolic saturation/hyaluronan | M1 limitations/context | G&W p.95; §2.6.5 p.105 | INCLUDED_CORRECT | MEDIUM | “별도 케이스”로 충분 |
| Proteins/peptides/antibodies introduction | M2 MUST | G&W §2.6.2 pp.97–100 | INCLUDED_CORRECT | HIGH | 유지 |
| Lymphatic absorption after sc dosing | M2 MUST | G&W p.97–98; R&T pp.718–721, Figs.21-13–21-16 | INCLUDED_CORRECT_WITH_WARNING | HIGH | 150 kDa 정량 외삽만 수정 |
| Protein volume of distribution | M2 MUST | G&W Table 2.10; R&T Table 21-6 | INCLUDED_CORRECT | HIGH | 유지 |
| Protein renal/elimination mechanisms | M2 MUST | G&W pp.98–99; R&T Tables 21-9–21-10 | INCLUDED_CORRECT | HIGH | 유지 |
| Antibody after five ascending infusions in cynomolgus monkey | M2 context/self-test | G&W p.99, Fig.2.71 | INCLUDED_CORRECT | MEDIUM | 원문 경고와 함께 유지 |
| r-hSOD normal vs nephrectomized rats | M2 context | G&W pp.99–100, Figs.2.72–2.73 | INCLUDED_CORRECT | MEDIUM | 유지 |
| IgX sc 40 µg/kg healthy volunteer | M1 anchor | G&W §2.6.3 pp.100–101, Fig.2.74 | INCLUDED_CORRECT | HIGH | 유지 |
| Immunoglobulin turnover Table 2.11 | M1 anchor | G&W p.102 | INCLUDED_CORRECT | HIGH | 유지 |
| Estradiol postmenopausal women | M1 context | G&W §2.6.4 pp.102–104, Fig.2.76, Table 2.12 | INCLUDED_CORRECT | MEDIUM | 유지 |
| Baseline subtraction scenarios | M1 assumptions/context | G&W §2.6.5 p.104, Fig.2.77 | INCLUDED_CORRECT | HIGH | 유지; Phase 4C에서 view 권장 |
| Comparison of clearance/turnover/response models | M1 context | G&W Table 2.13 p.105 | INCLUDED_CORRECT | MEDIUM | 유지 |
| 8-OH-DPAT body temperature | context only | G&W §2.6.6 pp.106–109, Figs.2.78–2.82 | INCLUDED_CORRECT | LOW-MEDIUM | 독립 MUST로 승격 불필요 |
| Feedback/Ackerman/IgG half-life concentration dependence | context only | G&W §2.6.7 pp.110–111, Figs.2.83–2.84 | INCLUDED_CORRECT | MEDIUM | 유지 |
| PK26 Efalizumab | M4/M5 anchor | G&W PK26 pp.599–601; R&T Fig.21-7 | INCLUDED_CORRECT | HIGH | 유지 |
| PK27 synthetic/semisynthetic TMDD data | M3–M5 MUST | G&W PK27 pp.602–610 | INCLUDED_CORRECT | HIGH | 유지 |
| PK27 ligand/target/complex dataset richness | M4 MUST | G&W pp.603–609, Table 27.2 | INCLUDED_CORRECT | HIGH | 유지 |
| PK27 MM reduced model failure at low dose | M4/M5 MUST | G&W p.609, Fig.27.6 | INCLUDED_CORRECT | HIGH | 유지 |
| PK27 four-phase profile | M3 MUST | G&W p.610 Fig.27.7; R&T p.712 Fig.21-9 | INCLUDED_CORRECT | HIGH | 유지; view instruction 필수 |
| FDA-approved therapeutic proteins/mAbs 2011–2016 | M2 context | R&T p.692 Fig.21-1 | INCLUDED_CORRECT | LOW | 유지 가능 |
| IgG structure/Fab/Fc | M2 context | R&T p.692 Fig.21-2 | INCLUDED_CORRECT | MEDIUM | 유지 가능 |
| mAb nomenclature and therapeutic use tables | context | R&T Tables 21-2–21-4 | INCLUDED_AS_CONTEXT | LOW | 자세한 표는 생략 정당 |
| FcRn salvage | M2 MUST | R&T pp.707–709 Fig.21-5 | INCLUDED_CORRECT | HIGH | 유지 |
| Nonlinear G-CSF/nartograstim | R&T example | R&T p.710 Fig.21-6 | MISSING | LOW | 굳이 추가 필요 없음; efalizumab/TMDD가 더 핵심 |
| R&T efalizumab curves | M4/M5 anchor | R&T p.710 Fig.21-7 | INCLUDED_CORRECT | HIGH | 유지 |
| Mager-Jusko TMDD conceptual model | M4 MUST | R&T p.711 Fig.21-8, Eq.21-1–21-6 | INCLUDED_CORRECT | HIGH | 유지 |
| R&T Fig.21-9 TMDD 4-phase | M3 MUST | R&T p.712 | INCLUDED_CORRECT | HIGH | 유지 |
| UK-279,276 PD example | omitted | R&T p.713 Fig.21-10 | MISSING | LOW | 생략 정당. 세션 핵심은 TMDD/antibody PK |
| Epoetin PD rate-limited examples | omitted/context minor | R&T Figs.21-11–21-12 | MISSING | LOW | 생략 정당 |
| Somatropin sc vs iv | context maybe absent | R&T p.721 Fig.21-17 | MISSING | MEDIUM | M2의 absorption-rate-limited 설명에 1문장 추가 가능 |
| Anakinra renal disease | context to Step 2 | R&T p.723–724 Fig.21-18, Table 21-16 | INCLUDED_AS_CONTEXT | MEDIUM | Step 2 이연 가능. M2에서 renal impairment 예시 1문장 있으면 좋음 |
| Immunogenicity | context | R&T p.725 Fig.21-19 | INCLUDED_AS_CONTEXT | MEDIUM | 유지 |
| Study problems 21-17–21-21 | omitted | R&T pp.726–730 | OMITTED_JUSTIFIABLE | LOW | 학습 문제이므로 Step 1 핵심 큐레이션에서 제외 가능 |

---

## T3: Author Key Messages

| Message | PDF Location | In Draft v0? | Status |
|---|---|---|---|
| Turnover concepts explain equilibrium between production/synthesis and loss/catabolism for endogenous compounds. | G&W p.94–95 | Yes, M1 | INCLUDED |
| Turnover implies steady state; two of `Rin`, `kout`, and `A` are needed to characterize turnover. | G&W p.95 | Yes, M1 formal definition | INCLUDED |
| Changing `kin` changes steady-state level but not time to new steady state; changing `kout` changes both level and time. | G&W p.97 Fig.2.70 | Yes, M1 central intuition | INCLUDED |
| Proteins/peptides generally have low, erratic, delayed extravascular absorption; lymphatics are important after sc dosing. | G&W p.97; R&T pp.718–721 | Yes, M2 | INCLUDED |
| Protein Vd is generally low; as MW increases, Vss, capillary permeability, and GFR tend to decrease. | G&W p.98; R&T p.701–704 | Yes, M2 | INCLUDED |
| Traditional mammillary model with central elimination can give inappropriate antibody Vd if tissue catabolism/peripheral elimination matters. | G&W p.99 | Yes, M2/self-test | INCLUDED |
| Baseline subtraction is appropriate only when baseline is constant or over a very short timeframe; constant baseline is exception rather than rule. | G&W p.104 Fig.2.77 | Partly, M1 assumptions | INCLUDED |
| Lowered estradiol levels in postmenopausal women are due to reduced turnover, not increased clearance. | G&W p.104 | Yes, context | INCLUDED |
| Body temperature simple turnover model is limited to 60 min because of negative feedback and circadian regulation. | G&W p.107 | Yes, context | INCLUDED |
| Full TMDD fitting precision improves when target and complex time courses are added. | G&W pp.603–609, Table 27.2 | Yes, M4 | INCLUDED |
| Reduced MM model can fit high concentration profiles but fails at lowest concentration with systematic deviation and inflated Km. | G&W p.609 Fig.27.6 | Yes, M4/M5 | INCLUDED |
| A true 5-parameter target/complex disposition model cannot always be replaced by 2-parameter MM across full concentration/time range. | G&W p.603, p.609 | Yes, M5 | INCLUDED |
| TMDD has four phases A–D with different dominant processes. | G&W p.610; R&T p.712 | Yes, M3 | INCLUDED |
| Molar units are preferably used for fitting/regression, though mg units were acceptable in PK27 synthetic data. | G&W p.610 | Yes, M3/M4 context | INCLUDED |
| Protein drugs generally require parenteral administration; absorption, distribution, excretion, metabolism differ from small molecules. | R&T objectives p.687 | Yes, M2 | INCLUDED |
| mAbs are IgG-like, FcRn recycling extends half-life; mAb half-life typically ~21 days. | R&T p.708–709 | Yes, M2 | INCLUDED |
| Nonlinearity is common to protein drugs; clearance and half-life must be viewed cautiously because values can be dose/condition specific. | R&T p.709 | Yes, M2/M5 | INCLUDED |
| TMDD occurs when high-affinity target binding affects PK; simpler approximations are often used because full parameter estimation is difficult. | R&T pp.709–712 | Yes, M4/M5 | INCLUDED |
| QE adequate when internalization is much slower than dissociation; MM adequate when drug concentrations exceed target or occupancy close to 100%. | R&T p.712 | Yes, M5 | INCLUDED |
| Renal disease affects protein drugs below about 30,000 g/mol; renal elimination for proteins usually means metabolism. | R&T p.723–724 | Partly, M2 context | PARTIAL |
| Immunogenic responses can increase or decrease mAb exposure through clearance changes and immune complex effects. | R&T p.712 and p.725 | Yes, M2 limitation | INCLUDED |
| The future of protein drugs includes modified molecules and complex delivery/engineering strategies. | R&T p.725–726 | No | OMITTED_JUSTIFIABLE |

---

## T4: Priority Summary (MUST_FIX → SHOULD_FIX → OPTIONAL → REJECT)

| # | Item | Priority | Rationale |
|---:|---|---|---|
| 1 | Full TMDD “8-parameter” vs fixed `Vc` 포함 9 structural quantities | MUST_FIX | Apex Concept 신뢰도에 직접 영향. 원문은 8 estimated parameters + fixed Vc 구조 |
| 2 | `kin·C_L·R` binding term 오기 | MUST_FIX | `kin`과 `kon` 혼동은 수식적 오류. TMDD mass-action 구조를 훼손 |
| 3 | Zettelkasten “세 ODE(L,R,RL)” 표현 | MUST_FIX | Full TMDD state count 오류. ligand peripheral state 누락 |
| 4 | NDA Deficiency Letter / FDA reviewer / 6–18개월 / $2M / 30% / $60M+ | MUST_FIX | PDF source 없음. 구체 수치가 출처 있는 사실처럼 보임 |
| 5 | `lymph recovery ≈ 3.2% per kDa`, mAb 150 kDa >80% | MUST_FIX | Fig.21-16 범위를 훨씬 벗어난 선형 외삽. 정량 예측처럼 쓰면 오류 |
| 6 | NONMEM `$DES` 코드의 source 라벨 | MUST_FIX | PDF에는 control stream 없음. 구현 번역 예시로 라벨링 필요 |
| 7 | Draft 말미 “계속 → Step 2 HTML” | MUST_FIX | 현재 workflow는 Phase 2 audit/Phase 4A patch 선행 |
| 8 | `Fig.27.6 + Peletier & Gabrielsson 2012` 인용 | SHOULD_FIX | PDF에는 Peletier & Gabrielsson이 cited source로 언급되지만 Draft의 추가 해석은 교재 기반/문헌 기반을 구분해야 함 |
| 9 | “90% 이상의 mAb 후보 target/complex assay 없음” | SHOULD_FIX | PDF source 없음. 실무 경험치라면 라벨 필요 |
| 10 | “NDA Section 5.3.2”, pediatric/elderly reviewer 요청 등 | SHOULD_FIX | plausible but not in source. 실무 확장으로 명시 |
| 11 | Somatropin absorption-rate-limited example | SHOULD_FIX | R&T Fig.21-17은 protein absorption 메시지를 강화하는 좋은 예시. M2에 1문장 context로 추가 가능 |
| 12 | Anakinra renal disease example | SHOULD_FIX | R&T objectives의 renal disease 메시지를 반영하려면 M2/§6에 유지 필요 |
| 13 | Table 21-13 small molecules vs protein absorption | SHOULD_FIX | M2에서 protein absorption 특수성 설명에 유용 |
| 14 | Body temperature/feedback section | OPTIONAL | 이미 context로 충분. 독립 MUST 불필요 |
| 15 | mAb nomenclature Table 21-2 | OPTIONAL | 임상 컨텍스트로만 필요. TMDD core에는 과잉 |
| 16 | Therapeutic use long tables 21-1/21-3/21-4/21-12 | OPTIONAL | 범위감 제공용. 상세 암기 불필요 |
| 17 | Study problem tables 21-17–21-21 | REJECT | Step 1 core curation에 넣으면 scope creep |
| 18 | UK-279,276 PD detailed model | REJECT | TMDD/항체 PK 세션의 주 spine에서 벗어남. 후속 PD 세션으로 이연 |

### Patch Memo Independent Verification

| Patch memo item | Audit classification | Decision |
|---|---|---|
| “8-parameter” vs “Vc 포함 9 structural quantities” | ERROR/MATCH_WITH_WARNING | 채택. MUST_FIX |
| NDA Deficiency Letter/6–18개월/200만 달러 | NOT_IN_SOURCE | 채택. MUST_FIX |
| lymph recovery >80% 외삽 | NOT_IN_SOURCE / ERROR if used as fact | 채택. MUST_FIX |
| NONMEM `$DES` code label | NOT_IN_SOURCE as source claim; useful as implementation | 채택. MUST_FIX label |
| Step 2 HTML 직행 금지 | WORKFLOW_MATCH | 채택. MUST_FIX |
| Phase 1 재실행 불필요 | AUDIT JUDGMENT MATCH | 채택 |

---

## T5: Coverage Audit

| PDF Element | Type | PDF Location | Step 1 Status | Omission Verdict | Required Action |
|---|---|---|---|---|---|
| 2.6 Turnover | Heading | G&W p.94 | INCLUDED_AS_MUST | - | 유지 |
| 2.6.1 Background | Heading | G&W pp.94–97 | INCLUDED_AS_MUST | - | 유지 |
| Fig.2.69 Basic turnover model | Figure | G&W p.95 | INCLUDED_AS_MUST | - | Phase 4C view or redraw 권장 |
| Eq.2:237–2:244 | Equations | G&W pp.95–96 | INCLUDED_AS_MUST | - | 유지 |
| Fig.2.70 kin vs kout manipulation | Figure | G&W p.97 | INCLUDED_AS_MUST | - | view instruction YES |
| 2.6.2 Introduction to proteins, peptides, antibodies | Heading | G&W pp.97–100 | INCLUDED_AS_MUST | - | 유지 |
| Table 2.10 Vd large MW compounds | Table | G&W p.98 | INCLUDED_AS_CONTEXT | - | M2에서 유지 |
| Fig.2.71 antibody cynomolgus monkey | Figure | G&W p.99 | INCLUDED_AS_CONTEXT | - | Vss warning과 함께 유지 |
| Fig.2.72 r-hSOD normal/nephrectomized rats | Figure | G&W p.100 | INCLUDED_AS_CONTEXT | - | optional/context |
| Fig.2.73 nephrectomization schematic | Figure | G&W p.100 | INCLUDED_AS_CONTEXT | - | optional/context |
| 2.6.3 Turnover of immunoglobulins | Heading | G&W pp.100–102 | INCLUDED_AS_MUST | - | 유지 |
| Eq.2:245–2:246 IgX sc model | Equations | G&W p.101 | INCLUDED_AS_CONTEXT | - | 유지 |
| Fig.2.74 IgX sc concentration-time | Figure | G&W p.101 | INCLUDED_AS_MUST | - | view instruction optional |
| Table 2.11 immunoglobulin turnover | Table | G&W p.102 | INCLUDED_AS_MUST | - | 유지 |
| 2.6.4 Turnover of hormones - Estradiol | Heading | G&W pp.102–104 | INCLUDED_AS_CONTEXT | - | 유지 |
| Eq.2:247–2:251 estradiol turnover/PK relations | Equations | G&W pp.102–103 | INCLUDED_AS_CONTEXT | - | current level sufficient |
| Fig.2.75 estradiol model schematic | Figure | G&W p.102 | INCLUDED_AS_CONTEXT | - | optional |
| Fig.2.76 estradiol time course | Figure | G&W p.103 | INCLUDED_AS_CONTEXT | - | optional |
| Table 2.12 estradiol mean kinetics | Table | G&W p.103 | INCLUDED_AS_CONTEXT | - | 유지 |
| 2.6.5 Comparison of models | Heading | G&W pp.104–105 | INCLUDED_AS_CONTEXT | - | 유지 |
| Fig.2.77 baseline scenarios | Figure | G&W p.104 | INCLUDED_AS_CONTEXT | MISSING_BRIDGE if absent; present | Phase 4C view instruction 권장 |
| Table 2.13 clearance/turnover/response comparison | Table | G&W p.105 | INCLUDED_AS_CONTEXT | - | 유지 |
| 2.6.6 Turnover of body temperature | Heading | G&W pp.106–109 | INCLUDED_AS_CONTEXT | - | 독립 MUST 금지 |
| Eq.2:252–2:258 | Equations | G&W pp.106–108 | INCLUDED_AS_CONTEXT/OMITTED_PARTLY | OMITTED_JUSTIFIABLE | 세부식 암기 불필요 |
| Figs.2.78–2.82 body temperature/circadian | Figures | G&W pp.106–109 | INCLUDED_AS_CONTEXT/OMITTED_PARTLY | OMITTED_JUSTIFIABLE | 후속 PD 세션으로 이연 가능 |
| Table 2.14 circadian parameters | Table | G&W p.109 | OMITTED_JUSTIFIABLE | - | 추가 불필요 |
| 2.6.7 Feedback | Heading | G&W pp.110–111 | INCLUDED_AS_CONTEXT | - | 유지 |
| Eq.2:259–2:263 | Equations | G&W pp.110–111 | INCLUDED_AS_CONTEXT/OMITTED_PARTLY | OMITTED_JUSTIFIABLE | 세부식은 PD/feedback 세션 이연 |
| Fig.2.83 Ackerman model | Figure | G&W p.110 | INCLUDED_AS_CONTEXT | - | optional |
| Fig.2.84 IgG half-life vs concentration | Figure | G&W p.111 | INCLUDED_AS_CONTEXT | - | M2/FcRn과 연결 유지 |
| PK26 objectives/problem specification | Case Study | G&W pp.599–600 | INCLUDED_AS_MUST | - | 유지 |
| Fig.26.1 efalizumab 5-dose curves | Figure | G&W p.600 | INCLUDED_AS_MUST | - | view instruction YES |
| Eq.26:1–26:2 parallel linear/MM | Equations | G&W p.600 | INCLUDED_AS_MUST | - | 유지 |
| Table 26.1 final estimates | Table | G&W p.601 | INCLUDED_AS_MUST | - | 유지 |
| PK26 interpretation | Author conclusion | G&W p.601 | INCLUDED_AS_MUST | - | 유지 |
| PK27 objectives/problem specification | Case Study | G&W pp.602–603 | INCLUDED_AS_MUST | - | 유지 |
| Fig.27.1 ligand profiles | Figure | G&W p.603 | INCLUDED_AS_MUST | - | view instruction YES |
| Fig.27.2 full TMDD schematic | Figure | G&W p.604 | INCLUDED_AS_MUST | - | view/redraw YES |
| Fig.27.3 ligand time course and clearance vs concentration | Figure | G&W p.604 | INCLUDED_AS_MUST | - | view instruction YES |
| Fig.27.4 ligand+target profiles | Figure | G&W p.605 | INCLUDED_AS_CONTEXT | - | 유지 |
| Fig.27.5 ligand+target+complex profiles | Figure | G&W p.606 | INCLUDED_AS_CONTEXT | - | 유지 |
| Eq.27:1–27:3 full TMDD | Equations | G&W pp.606–607 | INCLUDED_AS_MUST | - | `kon` typo patch |
| Eq.27:4–27:5 MM reduced model | Equations | G&W p.607 | INCLUDED_AS_MUST | - | 유지 |
| Eq.27:6–27:7 initial parameter estimates | Equations | G&W p.608 | INCLUDED_AS_CONTEXT | - | 유지 |
| Table 27.2 parameter precision | Table | G&W p.609 | INCLUDED_AS_MUST | - | view/table instruction YES |
| Fig.27.6 MM fit deviation | Figure | G&W p.609 | INCLUDED_AS_MUST | - | view instruction YES |
| Fig.27.7 4-phase TMDD | Figure | G&W p.610 | INCLUDED_AS_MUST | - | view/redraw YES |
| R&T Ch.21 objectives | Objectives | R&T p.687 | INCLUDED_AS_CONTEXT | - | renal disease objective partly 보강 가능 |
| Peptide/polypeptide/protein drugs | Heading | R&T pp.687–693 | INCLUDED_AS_CONTEXT | - | 유지 |
| Table 21-1 nonantibody agents | Table | R&T pp.688–691 | INCLUDED_AS_CONTEXT | - | 상세 생략 정당 |
| Figs.21-1–21-2 FDA approvals/IgG structure | Figures | R&T p.692 | INCLUDED_AS_CONTEXT | - | optional |
| Tables 21-2–21-4 nomenclature/mAb/polyclonal | Tables | R&T pp.693–700 | INCLUDED_AS_CONTEXT | - | 상세 생략 정당 |
| Comparison of PK protein vs conventional drugs | Heading | R&T pp.693–724 | INCLUDED_AS_MUST | - | 유지 |
| Distribution / Table 21-6 Vd | Heading/Table | R&T pp.701–702 | INCLUDED_AS_MUST | - | 유지 |
| Table 21-7 binding proteins | Table | R&T p.703 | INCLUDED_AS_CONTEXT | - | optional |
| Excretion and metabolism / Table 21-9 sieving | Heading/Table | R&T pp.703–705 | INCLUDED_AS_MUST | - | 유지 |
| Figs.21-3–21-4 glomerular sieving/kidney elimination | Figures | R&T p.705 | INCLUDED_AS_CONTEXT | - | view optional |
| Table 21-10 hepatic uptake | Table | R&T pp.706–707 | INCLUDED_AS_CONTEXT | - | 유지 |
| Table 21-11 Fcγ receptors | Table | R&T p.708 | INCLUDED_AS_CONTEXT | - | optional |
| FcRn-mediated clearance / Fig.21-5 | Heading/Figure | R&T pp.707–709 | INCLUDED_AS_MUST | - | view instruction YES |
| Nonlinearities / Figs.21-6–21-7 | Heading/Figures | R&T pp.709–710 | INCLUDED_AS_MUST/PARTIAL | - | Fig.21-7 유지; Fig.21-6 optional |
| Target-mediated drug disposition / Fig.21-8 / Eq.21-1–21-6 | Heading/Figure/Equations | R&T pp.709–711 | INCLUDED_AS_MUST | - | 유지 |
| Fig.21-9 4-phase TMDD | Figure | R&T p.712 | INCLUDED_AS_MUST | - | view/redraw YES |
| Immunogenicity-mediated clearance | Heading | R&T p.712 | INCLUDED_AS_CONTEXT | - | 유지 |
| Pharmacodynamics / Figs.21-10–21-12 / Table 21-12 | Heading/Figures/Table | R&T pp.713–717 | OMITTED_JUSTIFIABLE | - | TMDD/PK core와 분리 |
| Intravenous administration | Heading | R&T p.717 | OMITTED_JUSTIFIABLE | - | core 아님 |
| Subcutaneous and intramuscular administration | Heading | R&T pp.718–723 | INCLUDED_AS_MUST | - | 유지 |
| Table 21-13 absorption comparison | Table | R&T p.718 | INCLUDED_AS_CONTEXT/PARTIAL | MISSING_BRIDGE minor | M2에 1문장/table pointer 권장 |
| Figs.21-13–21-16 lymph/capillary/MW | Figures | R&T pp.718–720 | INCLUDED_AS_MUST | - | 150 kDa 외삽 patch |
| Fig.21-17 somatropin sc vs iv | Figure | R&T p.721 | OMITTED_PROBLEMATIC | MISSING_EXAMPLE | absorption-rate-limited example 1문장 추가 권장 |
| Tables 21-14–21-15 bioavailability | Tables | R&T pp.722–723 | INCLUDED_AS_CONTEXT | - | 유지 |
| Concurrent disease states / renal disease / Fig.21-18 / Table 21-16 | Heading/Figure/Table | R&T pp.723–724 | INCLUDED_AS_CONTEXT | - | Step 2 이연 허용, M2에 1문장 권장 |
| Immunogenic responses / Fig.21-19 | Heading/Figure | R&T p.725 | INCLUDED_AS_CONTEXT | - | 유지 |
| Future of the area | Heading | R&T p.725–726 | OMITTED_JUSTIFIABLE | - | scope 밖 |
| Study problems / Tables 21-17–21-21 / Fig.21-20 | Problems/Tables/Figure | R&T pp.726–730 | OMITTED_JUSTIFIABLE | - | Step 1에서 제외 정당 |
| Repeated author sentence: protein drugs need parenteral routes / lymphatics important | Repeated message | R&T objectives + pp.718–721 | INCLUDED_AS_MUST | - | 유지 |
| Repeated author sentence: nonlinearity makes CL and half-life guarded | Repeated message | R&T p.709 + examples | INCLUDED_AS_MUST | - | 유지 |
| Repeated author sentence: target/complex data needed for precise TMDD parameters | Repeated message | G&W PK27 pp.603–609; R&T p.712 | INCLUDED_AS_MUST | - | 유지 |

---

## T6: Figure Inventory & Learning Value Audit

**Inspection note:** PDF pages were rendered as contact sheets and visually inspected. Ratings are conservative. `ESSENTIAL` is used only when the visual structure materially affects learning of the core session.

### T6A. Gabrielsson & Weiner source range

| Figure/Table | Page | Teaches | Value | View Instruction? | Redraw/New Schematic? | Inspection Method | Rationale |
|---|---:|---|---|---|---|---|---|
| Table 2.9 | G p.94 | hepatic clearance model comparison from previous section | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Source range overlap artifact; not Session 09 core |
| Fig.2.69 | G p.95 | Basic turnover input-output model | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M1 skeleton을 도식적으로 고정함 |
| Fig.2.70 | G p.97 | `Rin/kin` vs `kout` manipulation effects on level and Tss | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M1 핵심 직관의 가장 중요한 그림 |
| Table 2.10 | G p.98 | Vd of large molecular weight compounds | USEFUL | YES | NO | VISUAL_INSPECTED | M2의 low Vd 메시지 근거 |
| Fig.2.71 | G p.99 | Antibody concentration-time after ascending infusions in cynomolgus monkey | USEFUL | NO | NO | VISUAL_INSPECTED | antibody Vss warning의 배경 |
| Fig.2.72 | G p.100 | r-hSOD normal vs nephrectomized rats | USEFUL | NO | NO | VISUAL_INSPECTED | renal contribution example |
| Fig.2.73 | G p.100 | Nephrectomization effect schematic | USEFUL | NO | NO | VISUAL_INSPECTED | Fig.2.72 해석 보조 |
| Fig.2.74 | G p.101 | IgX sc + endogenous turnover baseline | USEFUL | YES | NO | VISUAL_INSPECTED | turnover model의 applied example |
| Table 2.11 | G p.102 | Immunoglobulin turnover characteristics | ESSENTIAL | YES | NO | VISUAL_INSPECTED | IgG half-life/FcRn 논리의 수치 anchor |
| Fig.2.75 | G p.102 | Estradiol endogenous/exogenous turnover model | USEFUL | NO | NO | VISUAL_INSPECTED | M1 확장 예시 |
| Fig.2.76 | G p.103 | Estradiol time course after rapid infusion | USEFUL | NO | NO | VISUAL_INSPECTED | estradiol turnover conclusion support |
| Table 2.12 | G p.103 | Estradiol mean kinetic data | USEFUL | NO | NO | VISUAL_INSPECTED | context 수치 anchor |
| Fig.2.77 | G p.104 | Constant, diurnal, feedback, Zeitgeber baseline scenarios | ESSENTIAL | YES | YES | VISUAL_INSPECTED | baseline subtraction 오류 방지에 중요 |
| Table 2.13 | G p.105 | Clearance/turnover/response model analogy | USEFUL | YES | NO | VISUAL_INSPECTED | turnover-PD bridge support |
| Fig.2.78 | G p.106 | 8-OH-DPAT body temperature response-time | USEFUL | NO | NO | VISUAL_INSPECTED | PD extension example |
| Fig.2.79 | G p.107 | Simulated dose-response curve for body temperature | SKIPPABLE | NO | NO | VISUAL_INSPECTED | core TMDD learning에는 주변부 |
| Fig.2.80 | G p.108 | Intrinsic biorhythm model with Zeitgeber | USEFUL | NO | YES | VISUAL_INSPECTED | feedback/circadian extension; redraw may clarify |
| Table 2.14 | G p.109 | Circadian body temperature model parameters | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Step 1 core에는 과함 |
| Fig.2.81 | G p.109 | Circadian rhythm in untreated rats | SKIPPABLE | NO | NO | VISUAL_INSPECTED | context only |
| Fig.2.82 | G p.109 | Free-running vs entrained oscillations | SKIPPABLE | NO | NO | VISUAL_INSPECTED | context only |
| Fig.2.83 | G p.110 | Ackerman hormone-glucose feedback adaptation | USEFUL | NO | YES | VISUAL_INSPECTED | feedback extension; not TMDD core |
| Fig.2.84 | G p.111 | IgG half-life vs concentration / feedback-governed elimination | USEFUL | YES | NO | VISUAL_INSPECTED | FcRn/IgG nonlinear feedback bridge |
| Fig.26.1 | G p.600 | Efalizumab nonlinear antibody kinetics and reduced MM model | ESSENTIAL | YES | NO | VISUAL_INSPECTED | PK26 anchor for MM use case |
| Table 26.1 | G p.601 | PK26 parameter estimates/CV% | ESSENTIAL | YES | NO | VISUAL_INSPECTED | M5 numeric anchor |
| Fig.27.1 | G p.603 | Ligand profiles at four doses; early phase dose-dependence; R0/Km/Kd | ESSENTIAL | YES | YES | VISUAL_INSPECTED | TMDD curve-reading core |
| Fig.27.2 | G p.604 | Full TMDD schematic with ligand-target-complex sink | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Apex model structure |
| Fig.27.3 | G p.604 | Four concentration regimes and clearance-vs-concentration | ESSENTIAL | YES | YES | VISUAL_INSPECTED | MM boundary intuition |
| Fig.27.4 | G p.605 | Ligand+target simultaneous data | USEFUL | YES | NO | VISUAL_INSPECTED | dataset richness concept |
| Fig.27.5 | G p.606 | Ligand+target+complex data | USEFUL | YES | NO | VISUAL_INSPECTED | Table 27.2 precision improvement support |
| Table 27.1 | G pp.603/606 | A priori/simulated parameter set context | USEFUL | NO | NO | VISUAL_INSPECTED | background; Draft does not rely heavily |
| Table 27.2 | G p.609 | Parameter estimate precision across datasets I–III | ESSENTIAL | YES | NO | VISUAL_INSPECTED | identifiability core |
| Fig.27.6 | G p.609 | MM fit deviation, Km 3.7 vs 0.03 | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Critical Blow source |
| Fig.27.7 | G p.610 | Characteristic four-phase TMDD profile | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M3 central figure |

### T6B. Rowland & Tozer source range

| Figure/Table | Page | Teaches | Value | View Instruction? | Redraw/New Schematic? | Inspection Method | Rationale |
|---|---:|---|---|---|---|---|---|
| Table 21-1 | R&T pp.688–691 | Breadth of nonantibody protein drugs | USEFUL | NO | NO | VISUAL_INSPECTED | category breadth; not TMDD core |
| Fig.21-1 | R&T p.692 | FDA-approved therapeutic proteins 2011–2016 and mAb share | USEFUL | NO | NO | VISUAL_INSPECTED | context/importance only |
| Fig.21-2 | R&T p.692 | IgG heavy/light chain, Fab/Fc structure | USEFUL | YES | NO | VISUAL_INSPECTED | FcRn/Fc 이해 보조 |
| Table 21-2 | R&T p.693 | mAb nomenclature infixes | SKIPPABLE | NO | NO | VISUAL_INSPECTED | scope peripheral |
| Table 21-3 | R&T pp.694–700 | mAbs therapeutic use, half-life, route, dosing interval | USEFUL | NO | NO | VISUAL_INSPECTED | clinical breadth; 상세 암기 불필요 |
| Table 21-4 | R&T p.700 | FDA-approved polyclonal immune globulins/fragments | SKIPPABLE | NO | NO | VISUAL_INSPECTED | scope peripheral |
| Table 21-5 | R&T p.701 | Less conventional administration sites/methods | SKIPPABLE | NO | NO | VISUAL_INSPECTED | delivery context only |
| Table 21-6 | R&T pp.701–702 | Vd of proteins/antibodies/fragments | ESSENTIAL | YES | NO | VISUAL_INSPECTED | M2 Vd 제한의 핵심 근거 |
| Table 21-7 | R&T p.703 | protein drugs binding to carrier proteins | USEFUL | NO | NO | VISUAL_INSPECTED | binding proteins context |
| Table 21-8 | R&T p.703 | h-GH in rat tissue/distribution example | SKIPPABLE | NO | NO | VISUAL_INSPECTED | source peripheral |
| Table 21-9 | R&T p.704 | Glomerular sieving coefficients by MW/charge | ESSENTIAL | YES | NO | VISUAL_INSPECTED | M2 renal gate core |
| Fig.21-3 | R&T p.705 | Sieving coefficient vs molecular size/charge | USEFUL | YES | NO | VISUAL_INSPECTED | Table 21-9 visualizes trend |
| Fig.21-4 | R&T p.705 | Kidney protein elimination pathways | USEFUL | NO | YES | VISUAL_INSPECTED | complex kidney pathways; redraw can help |
| Table 21-10 | R&T pp.706–707 | Hepatic uptake mechanisms/receptors | USEFUL | NO | NO | VISUAL_INSPECTED | proteolysis/RME context |
| Table 21-11 | R&T p.708 | Fcγ receptor distribution/function | USEFUL | NO | NO | VISUAL_INSPECTED | FcγR vs FcRn distinction |
| Fig.21-5 | R&T p.709 | FcRn recycling protects IgG/mAbs from degradation | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M2 core mechanism |
| Fig.21-6 | R&T p.710 | Nonlinear G-CSF concentration-time profiles | USEFUL | NO | NO | VISUAL_INSPECTED | protein nonlinearity example |
| Fig.21-7 | R&T p.710 | Efalizumab dose-dependent half-life/nonlinearity | ESSENTIAL | YES | NO | VISUAL_INSPECTED | links R&T to PK26 |
| Fig.21-8 | R&T p.711 | Mager-Jusko general TMDD model | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Apex model source |
| Fig.21-9 | R&T p.712 | Four-phase TMDD profile with Km/Kd | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M3 and M5 central figure |
| Fig.21-10 | R&T p.713 | Mechanistic PD model for UK-279,276 | SKIPPABLE | NO | NO | VISUAL_INSPECTED | PD peripheral for Session 09 |
| Fig.21-11 | R&T pp.714/716 | Drug/target/effect relationship for abciximab | USEFUL | NO | NO | VISUAL_INSPECTED | protein PD example; not mAb PK core |
| Table 21-12 | R&T pp.714–715 | Antibody therapeutic uses | USEFUL | NO | NO | VISUAL_INSPECTED | clinical context |
| Fig.21-12 | R&T p.717 | Delayed PD effects despite short PK half-life | USEFUL | NO | NO | VISUAL_INSPECTED | PD extension |
| Table 21-13 | R&T p.718 | Small molecules vs protein systemic absorption after sc/im | ESSENTIAL | YES | NO | VISUAL_INSPECTED | M2 absorption mechanism core |
| Fig.21-13 | R&T p.718 | Blood capillary vs lymphatic absorption route | ESSENTIAL | YES | YES | VISUAL_INSPECTED | lymphatic route core |
| Fig.21-14 | R&T p.719 | Capillary permeability decreases with MW | ESSENTIAL | YES | NO | VISUAL_INSPECTED | explains lymphatic predominance |
| Fig.21-15 | R&T p.720 | Lymphatic system sketch | USEFUL | NO | NO | VISUAL_INSPECTED | anatomical support |
| Fig.21-16 | R&T p.720 | MW vs lymph recovery in sheep | ESSENTIAL | YES | NO | VISUAL_INSPECTED | M2 lymph recovery trend; avoid 150 kDa over-extrapolation |
| Fig.21-17 | R&T p.721 | Somatropin iv vs sc absorption-rate-limited profile | USEFUL | YES | NO | VISUAL_INSPECTED | Missing example worth adding as 1 sentence |
| Table 21-14 | R&T p.722 | nonantibody protein sc bioavailability/Tmax | USEFUL | NO | NO | VISUAL_INSPECTED | context only |
| Table 21-15 | R&T p.723 | mAb sc/im bioavailability/Tmax/t1/2 | ESSENTIAL | YES | NO | VISUAL_INSPECTED | M2 mAb absorption anchor |
| Fig.21-18 | R&T p.724 | Anakinra renal function vs exposure | USEFUL | YES | NO | VISUAL_INSPECTED | renal disease objective support |
| Table 21-16 | R&T p.724 | anakinra AUC/Cmax/t1/2 by renal function | USEFUL | YES | NO | VISUAL_INSPECTED | renal disease quantitative support |
| Fig.21-19 | R&T p.725 | ADA/immunogenicity effects on PK | USEFUL | YES | YES | VISUAL_INSPECTED | M2 limitation/ADA bridge |
| Table 21-17 | R&T p.726 | erythropoietin AUC/Cmax/t1/2 in ESRD | SKIPPABLE | NO | NO | VISUAL_INSPECTED | study problem data |
| Table 21-18 | R&T p.727 | growth hormone sc thigh/abdomen concentrations | SKIPPABLE | NO | NO | VISUAL_INSPECTED | study problem data |
| Table 21-19 | R&T p.727 | hirudin half-life/fraction excreted | SKIPPABLE | NO | NO | VISUAL_INSPECTED | study problem data |
| Table 21-20 | R&T p.728 | GnRH clearance/half-life in renal/hepatic disease | SKIPPABLE | NO | NO | VISUAL_INSPECTED | study problem data |
| Fig.21-20 | R&T p.729 | anakinra iv healthy vs ESRD | SKIPPABLE | NO | NO | VISUAL_INSPECTED | study problem figure |
| Table 21-21 | R&T p.729 | anakinra iv AUC/t1/2/Vi normal vs hemodialysis | SKIPPABLE | NO | NO | VISUAL_INSPECTED | study problem table |

---

## Minimal Patch List for Phase 4A

```text
[PATCH 1] Full TMDD parameter count
- Replace ambiguous “8-parameter ODE system” where it enumerates Vc.
- Use: “Full TMDD has 4 state variables and 9 structural quantities if fixed Vc is counted. In PK27, Vc was fixed at 0.05 L·kg⁻¹, so Table 27.2 reports 8 estimated parameters.”

[PATCH 2] Correct binding term typo
- Replace `kin·C_L·R` with `kon·C_L·R` in M4 B-1.

[PATCH 3] Correct ODE count in Zettelkasten
- Replace “세 ODE(L, R, RL)” with “4 ODE / 4 state variables (L central, L tissue, R, RL).”

[PATCH 4] Label NONMEM code
- Add: “[교과서 외 구현 번역 예시] The following code is a NONMEM-style educational skeleton translated from the PK27/R&T ODEs; it is not a control stream printed in the textbook.”

[PATCH 5] Remove or label regulatory/cost scenarios
- NDA Deficiency Letter, FDA reviewer wording, 30%, 6–18 months, $2M, $60M+, Section 5.3.2 should be deleted or marked as `[교과서 외 실무 가상 시나리오]`.

[PATCH 6] Lymphatic recovery extrapolation
- Replace “lymph recovery ≈ 3.2% per kDa; mAb 150 kDa >80%” with: “R&T Fig.21-16 shows increasing lymphatic recovery across 0.246–19 kDa in sheep; this supports directionality, not quantitative extrapolation to 150 kDa mAbs.”

[PATCH 7] Add one missing protein absorption example
- Add one sentence from R&T Fig.21-17: somatropin has ~2.1 h i.v. half-life but prolonged plasma concentrations after sc dosing, illustrating absorption-rate-limited kinetics.

[PATCH 8] Keep Anakinra as context
- Retain or add one sentence: renal disease reduces clearance of kidney-eliminated protein drugs, illustrated by anakinra in R&T Fig.21-18/Table 21-16.

[PATCH 9] Update completion block
- Replace “계속 → Step 2 HTML” with “Next: Phase 4A official patching based on Source Fidelity Audit, then Phase 4C, then HTML compile.”
```

---

## Final Audit Judgment

Draft v0 is **not a failed Phase 1 output**. The core conceptual spine is strong:

```text
Turnover skeleton → protein/antibody PK gates → TMDD 4-phase profile → Full TMDD model → MM approximation boundary
```

The main weakness is not coverage; it is **source boundary control**. The draft often moves from textbook facts into high-value practical extrapolation without labeling the transition. This is acceptable in a later “Master Lens / Practice Lens” layer, but it is not acceptable inside a Source Fidelity-locked Step 1 unless clearly tagged.

```text
Go to Phase 4A patching: YES
Go directly to HTML: NO
Need full Phase 1 redo: NO
```

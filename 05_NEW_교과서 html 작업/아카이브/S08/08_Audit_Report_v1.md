# 08_Audit Report v1 — Source Fidelity Audit

**업무 형태:** 파일 분석 / PDF 대조 감사 / 웹 검색 OFF  
**입력:** `08_G_비선형 PK MM·DDI 기전(1).pdf`, `08_T_비선형 PK MM·DDI 기전_01(1).pdf`, `08_T_비선형 PK MM·DDI 기전_02(1).pdf`, `08_step1_draft_v0(1).md`, `S08_phase1_patch memo.md`, audit prompt  
**산출:** `08_Audit Report v1`  
**역할:** Source Fidelity Auditor — 검증 전용. 재작성, 문장 개선, 새 비유·설명 생성은 수행하지 않음.  
**Inspection note:** T6는 PDF 페이지 렌더링 contact sheet를 육안 확인한 뒤 평가했다. 본 감사는 웹 검색을 사용하지 않았다.

---

## Executive Verdict

**판정:** `CONDITIONAL PASS — Source coverage는 높지만, Phase 4A/HTML 직행 전 MUST_FIX 필요.`

Draft v0는 비선형 PK, Michaelis-Menten capacity limitation, time-dependent enzyme turnover, nonlinear binding, drug-metabolite nonlinear model, ethanol 복합 사례, DDI 정량 framework를 매우 넓게 포착한다. 그러나 source fidelity 관점에서는 다음 문제가 있다.

### MUST_FIX 핵심 12건

1. **MUST 카드 과밀:** Draft는 M1–M9 + EXT/T1–T10까지 20개 이상을 사실상 핵심 카드로 유지한다. 이는 source fidelity 오류는 아니지만 Step 1의 MUST/CONTEXT 구분 실패다.
2. **Stage 1 “별도 산출물 참조” 의존:** 핵심 mechanism 정본을 별도 파일에 맡긴 구조는 single self-contained Step 1/HTML 요구와 충돌한다.
3. **M2 Eq 번호 오인:** Draft M2는 `dC/dt = -Vm·C/(Km+C)`를 `Eq 2:264`로 연결하지만, G Eq.2:264는 linear superposition 식이고 MM 관련식은 Eq.2:266–2:274 영역이다.
4. **FDA DDI Guidance 직접 주장:** Draft는 Eq.17-11/17-18을 “FDA DDI Guidance 핵심식”으로 서술하지만, 첨부 PDF는 R&T textbook이며 FDA guidance 문헌은 첨부되어 있지 않다. 식 자체는 R&T에 있으나 FDA guidance 연결은 NOT_IN_SOURCE다.
5. **NDA reviewer / NDA Section 12.3 / contraindication / dose reduction 언어:** PDF 직접 근거가 아니라 실무 추론 또는 가상 label drafting이다. Source-backed statement처럼 두면 안 된다.
6. **CPIC·한국/아시아 PM 빈도·백인 빈도:** 첨부 PDF에 없다. 웹 검색 OFF 조건에서 NOT_IN_SOURCE다.
7. **Mager-Jusko 2001 / quasi-equilibrium TMDD code / NONMEM code blocks:** PDF 범위는 small-molecule TMDD prototype 언급에 머문다. 구현 코드는 source 범위 밖이다.
8. **“carrier saturation이라는 단일 기하학” 과도 일반화:** source는 saturability/capacity/time/flow/binding을 다루지만 모든 비선형 PK를 carrier saturation 하나로 환원하지 않는다.
9. **Displacement-only DDI 독립 MUST card 유지:** 원문상 중요하지만 Ch.17의 핵심 정량 축은 altered clearance, inhibition, induction, route/extraction effect다. 독립 full card보다는 confusion/context가 적합하다.
10. **Omeprazole-clarithromycin observed max ratio = 33:** Fig.17-15의 최고점/예시로 추정 가능하나 정확 숫자로 본문 산출된 값은 아니다. RESTORED/확인필요 처리해야 한다.
11. **Atorvastatin-rifampin `Vd/F 17×↓`, `CL/F 9×↓`:** source는 AUC, Cmax, t1/2 변화와 mechanism 해석을 제공하지만 Draft의 배수 계산 일부는 직접 출처가 불명확하다. RESTORED 또는 계산식 표시 필요.
12. **Patch Memo의 “압축” 권고는 편집 판단이지 source fidelity 판정 자체가 아님:** Audit에서는 coverage와 오류를 분리해야 한다.

---

# T1: Equation/Numerical Audit

| Item | Draft v0 Expression | PDF Source | Classification | Correction |
|---|---|---|---|---|
| Source scope | G Ch.2.7 pp.112–141 + Ch.3.6 pp.224–227 + PK17/18/22; T Ch.16 pp.491–529; T Ch.17 pp.531–576 | Uploaded PDFs match these page ranges | MATCH | Keep. |
| Stage 3 regulatory framing | `FDA DDI Guidance Eq.17-11 / Eq.17-18` | R&T Ch.17 contains Eq.17-11 and Eq.17-18; no FDA guidance source attached | NOT_IN_SOURCE | Do not label as FDA guidance unless external source is separately supplied/verified. |
| Big Idea | `carrier saturation` as a single geometry behind capacity/time/flow/binding | G p.112–114 describes capacity, time, flow, binding; R&T Ch.16 describes saturability mechanisms | RESTORED | Use only as interpretive synthesis, not as author-stated fact. |
| M1 diagnostic | Dose-normalized AUC vs Dose; superposition violation | G Fig.2.85–2.86; T Ch.16 definition of nonlinearity | MATCH | Keep. |
| M2 formula citation | `$Cl = Vm/(Km+C)$`, Eq.2:264–2:274 | G Eq.2:266 gives concentration-dependent CL; Eq.2:264 is linear superposition, not MM | ERROR | Correct Eq.2:264 citation. Link MM CL/rate/bolus/input to Eq.2:266–2:274. |
| M2 ODE | `dC/dt = -Vm*C/(Km+C)` | G Eq.2:270 and surrounding MM bolus model; R&T Eq.16-4/16-5 | RESTORED | Accept as shorthand only if dimensional context/V term is clarified; do not cite Eq.2:264. |
| M2 high/low limits | `C<<Km: CL≈Vm/Km`; `C>>Km: zero-order` | G p.115–119; R&T Eq.16-1/16-2 | MATCH | Keep. |
| M2 AUC/single dose | Stage 1 references Eq.2:271 | G Eq.2:271 AUC for one-compartment IV MM | MATCH | Keep if single-dose context is explicit. |
| M2 C0/Vd 영역별 거동 | `C0/Vd` region behavior | G Eq.2:270–2:272 discuss C0=Dose/V and concentration-dependent half-life | MATCH | Keep with source context. |
| M3 turnover | `dE/dt = Rin − kout·E`; `Ess=Rin/kout` | G Eq.2:275 and subsequent turnover derivation | MATCH | Keep. |
| M3 `Cl(t)` time function | Clearance as function of enzyme level | G Eq.2:279–2:287 | MATCH | Keep. |
| M4 PK22 parameters | `Vc/Vt/a/k12/k21/kout/E0`; Table 22.2 | G PK22 pp.580–585; Table 22.2 | MATCH | Keep. |
| PK22 numeric anchors | `a=0.041`, `kout=0.023 h^-1` | G Table 22.2 shows initial/final estimates including `a`, `kout` | MATCH | Keep; units should be checked against table display. |
| M5 binding | `$Cb = n·Pt·Cu/(Kd+Cu)$` | G Eq.2:294 | MATCH | Keep. |
| M5 open vs closed system | Open system unbound concentration determined by input/unbound CL; in vitro closed systems can mislead | G Figs.2.104–2.105 and text | MATCH | Keep. |
| M6 drug-metabolite model | Two-compartment drug + one-compartment metabolite + MM | G §2.7.6, Eq.2:304–2:308, Tables 2.18–2.20 | MATCH | Keep. |
| M6 “Flip-flop을 분포 kinetics로 오독” | Draft card consequence | G §2.7.6 does not frame it as flip-flop | RESTORED | Treat as interpretive warning, not direct author wording. |
| M7 ethanol three dependencies | Capacity + Time + Flow | G §2.7.7; PK18; Fig.2.110–2.112; Eq.18:13 | MATCH | Keep. |
| M7 ethanol values in card | `Vmax≈10 g/hr`, `Km≈100 mg/L` | R&T Ch.16 alcohol section gives approximate Vm/Km; G PK18 gives Vmax/Km in g/min, g/L forms | MATCH | Keep with unit consistency. |
| M8 competitive PD | Eq.3:49, EC50 shift | G §3.6.1, Fig.3.24 | MATCH | Keep. |
| M8 statement | `Competitive antagonists do not alter Emax nor EC50, but shift inflection by [1+A/EA50]·EC50` | G p.225 | MATCH | Keep. |
| M9 noncompetitive PD | Eq.3:50, Emax reduction | G §3.6.2, Fig.3.25 | MATCH | Keep. |
| M9 empirical/enantiomer | Eq.3:51–3:53; Table 3.2; ketamine enantiomers | G §3.6.3–3.6.4; Fig.3.26; Table 3.2 | MATCH | Keep. |
| M2-EXT phenytoin clinical scenario | 300 mg/day → 4 mg/L; 500 mg/day → 36 mg/L; 67% dose increase → 9× concentration; toxicity signs | R&T Ch.16 opening p.491 | MATCH | Keep. |
| M2-EXT phenytoin typical values | `Vm≈500 mg/day`, `Km=0.4 mg/L`, `fu≈0.1`, `Km'=4 mg/L` | R&T p.503 | MATCH | Keep. |
| M2-EXT therapeutic range | `10–20 mg/L` | R&T p.503 | MATCH | Keep. |
| M2-EXT equation | `Cu,ss = Km·R0/(Vm−R0)` Eq.16-7 | R&T p.503 Eq.16-7 | MATCH | Keep. |
| M2-EXT bioavailability switch | Patient `Km'=3`, `Vm=425`, `200 mg q12h`, `F 0.85→0.95`, `Css 12→25 mg/L` | R&T p.503–504 example | MATCH | Keep. |
| M2-EXT t90 | Eq.16-10, `Km'=4`, `Vm=500`, `V=50`; plateau 300/350/400/425 mg/day → 6/9.3/16/22.7 mg/L | R&T Fig.16-10 | MATCH | Keep. |
| M2-EXT Vm sensitivity | `20% decrease in Vm doubles Css; 20% increase reduces by 33%` | R&T p.506 | MATCH | Keep. |
| M2-EXT mixed pathway | Eq.16-11; effect material if fm ≥0.5 | R&T p.506 | MATCH | Keep. |
| Alcohol values | `Vm≈10 g/hr`, `Km≈100 mg/L`, `Vd≈42 L/70 kg`; `200 mg/L` effect, `5000 mg/L` potentially lethal | R&T alcohol section pp.500–502 | MATCH | Keep. |
| Alcohol hourly drink example | 1 drink = 14 g; 4 drinks/hr = 56 g/hr; 0.5 drink/hr = 7 g/hr; Css = 233 mg/L | R&T p.501–502 | MATCH | Keep if fully sourced in card body. |
| Ascorbic acid opening | `75 mg/day→9 mg/L`; `10,000 mg/day→19 mg/L`; 133-fold dose increase, ~2-fold concentration | R&T p.492 | MATCH | Keep. |
| Ascorbic acid renal clearance | `<0.5 mL/min at 9 mg/L`; `21 mL/min at 19 mg/L`; >42-fold clearance increase | R&T p.492 | MATCH | Keep. |
| T1 transport formula | `Rate = Tm·Cu/(KT+Cu)` Eq.16-3 | R&T p.495 Eq.16-3 | MATCH | Keep. |
| Dicloxacillin | `1 g CLR=104`, `2 g CLR=63 mL/min`; `fu=0.04` | R&T p.507 and Fig.16-13/table discussion | MATCH | Keep. |
| Ascorbic acid reabsorption | CLR increases with concentration due to saturable active reabsorption | R&T Fig.16-15 and text | MATCH | Keep. |
| Glucose renal threshold | Study problem/Table 16-10 | R&T pp.527–528 | MATCH as exercise/context | Keep as context only. |
| T2 nicardipine | `F=19→22→28→36%` across 10–40 mg q8h | R&T Table 16-2 | MATCH | Keep. |
| T2 methylphenidate | Enantiomer exposure difference, Fig.16-6 | R&T Fig.16-6 | MATCH | Keep. |
| T3 TMDD examples | Bosentan, imirestat, trandolaprilat, draflazine, mitoxantrone | R&T target-mediated disposition section and Figs.16-20–16-23 | MATCH | Keep. |
| T3 Bosentan | `Vss 0.67→0.16 L/kg` | R&T Fig.16-20 and associated text | RESTORED | Value appears in figure/table context; retain with [확인 필요] unless exact figure values are manually read. |
| T3 quasi-equilibrium TMDD code | `Mager-Jusko 2001`, NONMEM implementation | Not in attached PDFs | NOT_IN_SOURCE | Remove from source-backed Step 1 or tag as 후속 세션/실무 확장. |
| T4 clarithromycin MBI mechanism | Half-life longer after multiple dosing, mechanism-based inhibition | R&T Fig.16-26 and Ch.17 Fig.17-13/17-14 | MATCH | Keep. |
| Clarithromycin numeric | `kinact=0.07 min^-1`, `kE≈0.23 day^-1`, enzyme t1/2≈3d | R&T Ch.17 p.558 | MATCH | Keep. |
| T4-EXT MBI ratio | `kinact/kE=438`, `CuI/KI=0.025`, `11-fold CL reduction`, `1.025-fold reversible` | R&T p.558 | MATCH | Keep. |
| MBI recovery | `2 weeks, perhaps longer, for CYP3A4` | R&T p.558 | MATCH | Keep. |
| T5 displacement equation | `V=Vp+Vt·fu/fuT` Eq.17-1 | R&T altered distribution section | MATCH | Keep if T5 remains. |
| T5 phenytoin-valproate | `N=25/11/9`, total phenytoin decreased, unbound unchanged | R&T Fig.17-3 | MATCH | Keep. |
| T5 conclusion | `Displacement-only is not dose-adjustment reason` | R&T Ch.17 explicitly says plasma binding displacement is unlikely to produce clinically significant interaction | MATCH | Keep, but as context/confusion pair. |
| Warfarin-phenylbutazone | Displacement + inhibition | R&T Fig.17-18 and surrounding discussion | MATCH | Keep. |
| T6 theophylline-enoxacin | `t1/2 8.8→22h`, `average interdose 4→9 mg/L`, `CLinh/CLnormal=0.44`, `fm=0.67` | R&T Fig.17-6/17-7 and text pp.546–550 | MATCH | Keep. |
| T6 Eq.17-9–17-12 | Reversible competitive inhibition and AUC/CL ratio framework | R&T pp.550–552 | MATCH | Keep. |
| T6 “FDA 핵심식” | Eq.17-11 as FDA guidance | No FDA source attached | NOT_IN_SOURCE | Tag as external regulatory linkage, not textbook source. |
| Desipramine-quinidine | CYP2D6, fm≈0.75, 4-fold CL decrease | R&T p.549–550 | MATCH | Keep. |
| Desipramine-fluoxetine | `AUC 284→2110`, `t1/2 16.1→63.8h`, `CL/F 289→27.1 L/hr` | R&T Table 17-11 | MATCH | Keep. |
| Strong/moderate/weak inhibitor classification | Table 17-5; strong ≥5-fold AUC ratio or >80% CL reduction | R&T Table 17-5 | MATCH | Keep. |
| Table 17-6 substrates | ≥4-fold AUC increase substrates | R&T Table 17-6 | MATCH | Keep. |
| Diltiazem-lovastatin | `AUC ratio 1.27 IV vs 3.57 oral` | R&T Table 17-7 | MATCH | Keep. |
| Fluconazole-midazolam | `5.6× oral vs 2× IV`; `FH 0.42→0.72`, `FG 0.57→0.88` | R&T Fig.17-10 and text | MATCH | Keep. |
| Rosuvastatin-cyclosporine | `11-fold Cmax`, `7-fold AUC` | R&T Fig.17-11 and text | MATCH | Keep. |
| Imipenem-cilastatin | Fig.17-12 renal dehydropeptidase inhibition | R&T Fig.17-12; Table 17-2 | MATCH | Keep as beneficial DDI context. |
| T7 Eq.17-18 | `Maximum exposure ratio = 1/(1−fmPOLY−fmNP)` | R&T Eq.17-18 | MATCH | Keep. |
| Omeprazole-clarithromycin | `observed max ratio ~33`; `fmPOLY≈0.92` | R&T Fig.17-15 lists omeprazole-clarithromycin as high fmPOLY example; exact 33 not printed in text | RESTORED [확인 필요] | Present as approximate visual estimate only, not exact source number. |
| Korean/Asian PM frequency | `한국·아시아 15%, 백인 3%` | Not in PDFs | NOT_IN_SOURCE | Remove or external-source tag. |
| T8 phenobarbital-dicumarol | `3–4 weeks plateau`; `phenobarbital t1/2=4 days` | R&T Fig.17-17 and induction section | MATCH | Keep. |
| T9 digoxin-quinidine | `CL 140→72`, `CLR 101→51`, `Vd 500→240`, `F 0.75→0.85` | R&T Table 17-8 and text | MATCH | Keep. |
| T9 atorvastatin-rifampin | `Cmax 10×`, `AUC 7×`, `t1/2 8→3h`; OATP1B1 inhibition | R&T Fig.17-19 and text | MATCH for Cmax/AUC/t1/2/mechanism | `Vd/F 17×↓`, `CL/F 9×↓` should be marked derived/restored unless formula shown. |
| T10 Eq.17-21 | Two full agonists same receptor; Emax ceiling | R&T Eq.17-19–17-21 and Fig.17-20 | MATCH | Keep. |
| T10 isobologram | Fig.17-21 additive/less-than-additive/greater-than-additive | R&T Fig.17-21 | MATCH | Keep. |
| Greco Eq.17-22 | Universal response surface | R&T Eq.17-22 | MATCH | Keep. |
| Midazolam-propofol synergy | R&T PD interaction examples | MATCH | Keep if exact source location preserved. |
| Isoproterenol-propranolol antagonism | R&T p.569 | MATCH | Keep. |
| CPIC guidelines | Mentioned as future integration | Not in PDFs | NOT_IN_SOURCE | Tag as 후속 지식 only. |
| NDA Section 12.3 dose labels | `75% reduction`, `2-week washout`, `contraindicated unless TDM`, etc. | Not in PDFs; some elements inferable from AUC ratios but not author-stated recommendations | NOT_IN_SOURCE | Remove from source-backed audit body or tag as hypothetical exercise. |
| TDM/post-marketing plan | Draft recommendation | Not directly in PDFs | NOT_IN_SOURCE | Mark as 실무 추론, not textbook fact. |

---

# T2: Examples & Data Audit

| Item | Draft v0 Status | PDF Location | Classification | Importance | Action |
|---|---|---|---|---|---|
| G nonlinear diagnostic EDA | Included M1 | G §2.7.1, Fig.2.85–2.86 | INCLUDED_CORRECT | HIGH | Keep. |
| G Table 2.15 causes of nonlinearities | Partly included | G p.114 | INCLUDED_CORRECT | HIGH | Keep; useful overview. |
| G capacity-limited bolus/infusion/oral models | Included in M2 | G §2.7.2.1–2.7.2.3 | INCLUDED_CORRECT with Eq citation issue | HIGH | Fix Eq.2:264 mis-citation. |
| G Fig.2.89 25/100 unit IV bolus two-subject example | Not prominent | G p.116 | MISSING | MEDIUM | Add as optional case anchor if teaching superposition failure. |
| G Fig.2.90 ethanol parenteral/oral model | Included through M7 | G p.118 | INCLUDED_CORRECT | MEDIUM | Keep. |
| G time-dependence/induction concepts | Included M3/M4 | G §2.7.3 | INCLUDED_CORRECT | HIGH | Keep self-contained. |
| G heteroinduction pentobarbital-nortriptyline | Included mostly as context | G §2.7.3.3 Figs.2.94–2.98 | INCLUDED_CORRECT | MEDIUM | Keep as context. |
| G PK22 autoinduction compound X | Included M4 | G PK22 pp.580–585 | INCLUDED_CORRECT | HIGH | Keep; verify units/table values. |
| G flow-dependent ethanol | Included M7 | G §2.7.4, Fig.2.110 | INCLUDED_CORRECT | HIGH | Keep. |
| G nonlinear binding open/closed system | Included M5 | G §2.7.5, Figs.2.101–2.105 | INCLUDED_CORRECT | HIGH | Keep. |
| G drug-metabolite nonlinear model | Included M6 | G §2.7.6, Figs.2.106–2.109, Tables2.18–2.20 | INCLUDED_CORRECT | HIGH | Keep but do not use flip-flop phrasing as source claim. |
| G ethanol oral bioavailability concentration dependence | Included M7 | G §2.7.7, Eq.18:13, Fig.18.3 | INCLUDED_CORRECT | HIGH | Keep. |
| G PK17 capacity I | Included in data anchors | G PK17 pp.553–555, Table17.1 | INCLUDED_CORRECT | MEDIUM | Keep as data anchor. |
| G PK18 ethanol IV infusion | Included | G PK18 pp.556–562 | INCLUDED_CORRECT | HIGH | Keep. |
| G PD competitive/noncompetitive/enantiomer models | Included M8/M9 | G §3.6.1–3.6.4 | INCLUDED_CORRECT | HIGH | Keep. |
| R&T phenytoin opening case | Included M2-EXT | T16 p.491, p.503–506 | INCLUDED_CORRECT | HIGH | Keep. |
| R&T ascorbic acid opening case | Included | T16 p.492, Fig.16-15/Table16-4 | INCLUDED_CORRECT | HIGH | Keep. |
| R&T griseofulvin solubility-limited absorption | Included context | T16 Fig.16-4 | INCLUDED_CORRECT | MEDIUM | Keep as context. |
| R&T amoxicillin saturable peptide transport | Included context | T16 Fig.16-5 | INCLUDED_CORRECT | MEDIUM | Keep as context. |
| R&T methylphenidate enantiomer first-pass | Included T2 | T16 Fig.16-6 | INCLUDED_CORRECT | MEDIUM | Keep. |
| R&T nicardipine saturable first-pass | Included T2 | T16 Table16-2 | INCLUDED_CORRECT | HIGH | Keep. |
| R&T alcohol nonlinear absorption/AUC | Included | T16 Figs.16-7–16-8 | INCLUDED_CORRECT | HIGH | Keep. |
| R&T phenytoin dose plateau/time-to-plateau | Included | T16 Figs.16-9–16-11 | INCLUDED_CORRECT | HIGH | Keep. |
| R&T dicloxacillin saturable secretion | Included T1 | T16 Fig.16-13 | INCLUDED_CORRECT | HIGH | Keep. |
| R&T ascorbic acid/disopyramide reabsorption | Included T1/M5-EXT | T16 Figs.16-15–16-16 | INCLUDED_CORRECT | MEDIUM | Keep. |
| R&T protein/tissue binding prototypes | Included M5-EXT/T3 | T16 Figs.16-17–16-23 | INCLUDED_CORRECT | HIGH | Keep but compress. |
| R&T verapamil chronopharmacokinetics | Included context | T16 Fig.16-24 | INCLUDED_CORRECT | LOW/MEDIUM | Keep as context only. |
| R&T carbamazepine autoinduction | Included M3-EXT | T16 Fig.16-25 | INCLUDED_CORRECT | HIGH | Keep. |
| R&T clarithromycin MBI | Included T4 | T16 Fig.16-26; T17 Fig.17-13/17-14 | INCLUDED_CORRECT | HIGH | Keep. |
| R&T salicylic acid opposing nonlinearities | Included M5-EXT | T16 Figs.16-27–16-29 | INCLUDED_CORRECT | HIGH | Keep. |
| R&T ethchlorvynol overdose/dialysis | Context | T16 Fig.16-30 | INCLUDED_CORRECT | LOW | Optional. |
| R&T polypharmacy/graded interactions | Partly included | T17 pp.531–532 | INCLUDED_CORRECT | HIGH | Keep. |
| R&T Table17-1 interactions to avoid | Weakly included | T17 p.533 | MISSING/WEAK | MEDIUM | Add if Ch.17 introduction needs coverage. |
| R&T Table17-2 beneficial combination products | Included context | T17 p.534 | INCLUDED_CORRECT | MEDIUM | Keep as context. |
| R&T transporter-mediated DDI table | Included T9 context | T17 Table17-3 | INCLUDED_CORRECT | HIGH | Keep but compress. |
| R&T altered absorption schematic | Not prominent | T17 Fig.17-1 | MISSING | LOW/MEDIUM | Optional. |
| R&T displacement simulations/cases | Included T5 | T17 Figs.17-2–17-4 | INCLUDED_CORRECT | MEDIUM | Down-rank from full card. |
| R&T theophylline-enoxacin | Included T6 | T17 Figs.17-6–17-7 | INCLUDED_CORRECT | HIGH | Keep. |
| R&T fm/AUC ratio simulations | Included T6 | T17 Fig.17-8 | INCLUDED_CORRECT | HIGH | Keep. |
| R&T inhibition time course | Included T6 | T17 Fig.17-9 | INCLUDED_CORRECT | HIGH | Keep. |
| R&T fluconazole-midazolam route effect | Included T9 | T17 Fig.17-10 | INCLUDED_CORRECT | HIGH | Keep. |
| R&T rosuvastatin-cyclosporine | Included T9 | T17 Fig.17-11 | INCLUDED_CORRECT | HIGH | Keep. |
| R&T imipenem-cilastatin | Included context | T17 Fig.17-12 | INCLUDED_CORRECT | MEDIUM | Keep as beneficial DDI context. |
| R&T midazolam-clarithromycin MBI | Included T4-EXT | T17 Fig.17-13 | INCLUDED_CORRECT | HIGH | Keep. |
| R&T MBI mechanism scheme | Included | T17 Fig.17-14 | INCLUDED_CORRECT | HIGH | Keep. |
| R&T PM + inhibitor max exposure | Included T7 | T17 Fig.17-15 | INCLUDED_CORRECT except exact 33 | HIGH | Keep; exact 33 should be approximate. |
| R&T induction withdrawal trap | Included T8 | T17 Fig.17-16 | INCLUDED_CORRECT | HIGH | Keep. |
| R&T phenobarbital-dicumarol | Included T8 | T17 Fig.17-17 | INCLUDED_CORRECT | HIGH | Keep. |
| R&T warfarin-phenylbutazone | Included T5 | T17 Fig.17-18 | INCLUDED_CORRECT | MEDIUM | Keep as multifaceted caution. |
| R&T atorvastatin-rifampin | Included T9 | T17 Fig.17-19 | INCLUDED_CORRECT with derived-value caution | HIGH | Mark derived ratios. |
| R&T PD agonist/isobole | Included T10 | T17 Figs.17-20–17-21 | INCLUDED_CORRECT | HIGH | Keep. |
| R&T study problem figures/tables 17-22–17-24 / 17-13 | Mostly absent | T17 pp.570–576 | MISSING | LOW | Omission justifiable unless exercise appendix desired. |

---

# T3: Author Key Messages

| Message | PDF Location | In Draft v0? | Status |
|---|---|---|---|
| Nonlinear kinetics occurs with capacity, time, flow, and binding; multiple causes may occur simultaneously. | G §2.7.1 | Yes | INCLUDED |
| Start nonlinear assessment with linear, semilog, dose-normalized C-time plots, then AUC vs Dose and AUC/Dose vs Dose. | G p.113 | Yes | INCLUDED |
| If clearance decreases or bioavailability increases, AUC/Dose rises with dose; opposite for CL increase/F decrease. | G Fig.2.85 | Yes | INCLUDED |
| Linear systems obey superposition; nonlinear systems violate it. | G Fig.2.87; T16 definition | Yes | INCLUDED |
| In MM kinetics, clearance is concentration-dependent and is of limited utility; Vmax, Km, Vss are more useful. | G p.116, p.118–119 | Yes | INCLUDED; Eq citation patch needed |
| AUC-based bioavailability is not appropriate when clearance is not constant. | G p.116 | Partly | SHOULD_FIX |
| To estimate Vmax and Km separately, data must cover the curvature and include concentrations around/below Km. | G p.117 | Partly | SHOULD_FIX |
| Enzyme induction changes Vmax, not Km, when Km is based on unbound concentration. | G p.118–119 | Yes | INCLUDED |
| Half-life in nonlinear systems is concentration-dependent and instantaneous, not a fixed time to eliminate half the body amount. | G p.117; T16 Ch.16 | Yes | INCLUDED |
| Time dependence requires actual physiological/biochemical change, not just parameter values changing with concentration. | G p.112 Levy quote; T16 definition | Yes | INCLUDED |
| In open in vivo systems, protein binding displacement alone often does not change unbound steady-state concentration for low-extraction drugs. | G §2.7.5; T17 displacement section | Yes | INCLUDED |
| Ethanol forward prediction is hampered by combined capacity, time, flow, absorption variability. | G §2.7.7 | Yes | INCLUDED |
| Nonlinearities are clinically important because small dose or bioavailability changes can cause large exposure changes near capacity. | T16 phenytoin case | Yes | INCLUDED |
| Ascorbic acid shows the opposite direction: massive dose increase with small concentration increase due to renal clearance increase. | T16 p.492 | Yes | INCLUDED |
| Interactions are graded, not all-or-none; many are not clinically important but some are severe. | T17 p.532 | Yes | INCLUDED |
| Drug interactions alter PK, PD, or both; food/herbal constituents may do the same but are not the focus. | T17 p.532 | Partly | SHOULD_FIX |
| Displacement of plasma protein binding is unlikely to produce a clinically significant interaction by itself. | T17 objectives + displacement text | Yes | INCLUDED |
| Oral interactions are often greater than parenteral interactions for drugs subject to high oral first-pass loss. | T17 objectives + midazolam/diltiazem examples | Yes | INCLUDED |
| PM patients can have much greater inhibition risk when a nonpolymorphic compensatory pathway is inhibited. | T17 Eq.17-18/Fig.17-15 | Yes | INCLUDED |
| Interaction detection depends strongly on sequence of administration and withdrawal. | T17 p.534 | Partly | SHOULD_FIX |
| PD interactions can be additive, synergistic, or antagonistic; same-receptor full agonist combinations may have Emax ceiling. | T17 PD section/Fig.17-20–17-21 | Yes | INCLUDED |

---

# T4: Priority Summary

| # | Item | Priority | Rationale |
|---|---|---|---|
| 1 | Correct M2 Eq.2:264 mis-citation | MUST_FIX | Direct source error: Eq.2:264 is linear superposition, not MM ODE. |
| 2 | Separate textbook Eq.17-11/17-18 from FDA DDI Guidance claim | MUST_FIX | FDA guidance is not attached; source fidelity fails if stated as direct source. |
| 3 | Remove/source-tag NDA reviewer, NDA Section 12.3, contraindication, and dose-reduction language | MUST_FIX | Not in PDFs; can remain only as hypothetical/external practical inference. |
| 4 | Remove/source-tag CPIC and ethnicity PM frequency claims | MUST_FIX | Not in attached source and web search is OFF. |
| 5 | Remove/source-tag Mager-Jusko/TMDD code/NONMEM code blocks | MUST_FIX | Not in PDFs; G/R&T provide concepts, not these implementations. |
| 6 | Make Stage 1 mechanism self-contained | MUST_FIX | Draft’s “별도 산출물 참조” creates downstream source gap. |
| 7 | Mark omeprazole-clarithromycin `~33` as approximate/restored | MUST_FIX | Source figure supports high ratio; exact value not printed as draft number. |
| 8 | Mark atorvastatin-rifampin `Vd/F 17×`, `CL/F 9×` as derived/restored | MUST_FIX | Source supports major PK changes and mechanism; those ratios need formula provenance. |
| 9 | Reduce displacement-only from full MUST card or justify as confusion card | SHOULD_FIX | Source-important but not central top-level DDI equation framework. |
| 10 | Add G warning that AUC-based F is inappropriate when CL is not constant | SHOULD_FIX | Author explicitly states this; important for nonlinear PK. |
| 11 | Add explicit Vmax/Km design requirement | SHOULD_FIX | G p.117 says concentration coverage around Km is required. |
| 12 | Keep phenytoin/asccorbic acid/alcohol anchors | MUST_KEEP | All are source-backed, high-yield examples. |
| 13 | Keep Eq.17-9–17-14 and Eq.17-18 | MUST_KEEP | Source-backed core of Ch.17 DDI quantification. |
| 14 | Keep T17 sequence-of-administration message | SHOULD_FIX | Author explicitly emphasizes initiation/withdrawal sequence. |
| 15 | Patch Memo compression recommendation | OPTIONAL | Valid editorial concern, but not an equation/source error. |
| 16 | Patch Memo “Figure budget” | OPTIONAL | Phase 4C editorial triage; source fidelity does not require it. |
| 17 | Claims of AI/ML/NONMEM professional moat | REJECT for source-backed report | Not textbook content; may be retained only as external commentary. |

---

# T5: Coverage Audit

## T5-A. Section / Structural Elements

| PDF Element | Type | PDF Location | Step 1 Status | Omission Verdict | Required Action |
|---|---|---|---|---|---|
| G §2.7 Nonlinear Systems – Capacity, Time, Flow and Binding | H1 | G p.112 | INCLUDED_AS_MUST | — | Keep. |
| G §2.7.1 What causes nonlinearity and how is it assessed? | H2 | G pp.112–114 | INCLUDED_AS_MUST | — | Keep. |
| G §2.7.2 Nonlinear kinetics – Capacity | H2 | G pp.114–119 | INCLUDED_AS_MUST | — | Fix Eq citation. |
| G §2.7.2.1 Bolus input - Capacity limited elimination | H3 | G p.117 | INCLUDED_AS_MUST | — | Keep. |
| G §2.7.2.2 Constant rate input - Capacity limited elimination | H3 | G p.118 | INCLUDED_AS_CONTEXT | — | Keep. |
| G §2.7.2.3 First order input - Capacity limited elimination | H3 | G p.118 | INCLUDED_AS_CONTEXT | — | Keep. |
| G §2.7.2.4 Conclusions for capacity limited elimination | H3 | G pp.118–119 | PARTIAL | MISSING_AUTHOR_MSG | Add CL/AUC/F caution and Vmax/Km/Vss message. |
| G §2.7.3 Nonlinear kinetics - Time | H2 | G pp.119–129 | INCLUDED_AS_MUST | — | Keep self-contained. |
| G §2.7.3.1 Background | H3 | G p.120 | INCLUDED_AS_CONTEXT | — | Keep. |
| G §2.7.3.2 Turnover of induction | H3 | G pp.120–125 | INCLUDED_AS_MUST | — | Keep. |
| G §2.7.3.3 Heteroinduction | H3 | G pp.124–126 | INCLUDED_AS_CONTEXT | — | Keep context. |
| G §2.7.3.4 Autoinduction | H3 | G pp.126–129 | INCLUDED_AS_MUST | — | Keep. |
| G §2.7.4 Nonlinear kinetics - Flow | H2 | G p.129 | INCLUDED_AS_CONTEXT | — | Keep mainly through ethanol. |
| G §2.7.5 Nonlinear kinetics - Binding | H2 | G pp.129–134 | INCLUDED_AS_MUST | — | Keep. |
| G §2.7.6 Nonlinear drug and metabolite models | H2 | G pp.135–139 | INCLUDED_AS_MUST | — | Keep but avoid non-source flip-flop language. |
| G §2.7.7 Ethanol combines capacity, time and flow dependencies | H2 | G pp.139–141 | INCLUDED_AS_MUST | — | Keep. |
| G §3.5.7 Multiple binding site model | H3 | G p.224 | INCLUDED_AS_CONTEXT | — | Keep if M9 references multiple binding. |
| G §3.6 Interaction Models | H2 | G pp.224–227 | INCLUDED_AS_MUST | — | Keep. |
| G §3.6.1 Competitive antagonism | H3 | G p.225 | INCLUDED_AS_MUST | — | Keep. |
| G §3.6.2 Noncompetitive antagonism | H3 | G pp.225–226 | INCLUDED_AS_MUST | — | Keep. |
| G §3.6.3 General empirical dynamic model for two drugs | H3 | G p.226 | INCLUDED_AS_CONTEXT | — | Keep as context. |
| G §3.6.4 Enantiomer interaction models | H3 | G p.227 | INCLUDED_AS_CONTEXT/MUST | — | Keep if M9 remains. |
| G PK17 Nonlinear kinetics - Capacity I | Case study | G pp.553–555 | INCLUDED_AS_CONTEXT | — | Keep as data anchor. |
| G PK18 Capacity II – Ethanol kinetics | Case study | G pp.556–562 | INCLUDED_AS_MUST | — | Keep. |
| G PK22 Nonlinear kinetics - Autoinduction | Case study | G pp.580–585 | INCLUDED_AS_MUST | — | Keep. |
| T16 Chapter objectives | Opening | T16 p.491 | PARTIAL | MISSING_AUTHOR_MSG | Include dose/time dependence and recognition objectives in compressed header. |
| T16 Definition of nonlinear kinetic behavior | H2 | T16 p.492 | INCLUDED_AS_MUST | — | Keep. |
| T16 Causes of nonlinearity | H2 | T16 pp.492–493 | INCLUDED_AS_MUST | — | Keep. |
| T16 Saturable processes | H2 | T16 pp.493–497 | INCLUDED_AS_MUST | — | Keep. |
| T16 Saturable metabolism | H3 | T16 pp.493–495 | INCLUDED_AS_MUST | — | Keep. |
| T16 Saturable transport | H3 | T16 p.495 | INCLUDED_AS_CONTEXT/MUST | — | Keep T1. |
| T16 Saturable plasma protein binding | H3 | T16 p.495–496 | INCLUDED_AS_MUST | — | Keep M5-EXT. |
| T16 Target-mediated drug disposition | H3 | T16 p.496 | INCLUDED_AS_MUST | — | Keep but no code. |
| T16 Nonlinear absorption | H2 | T16 pp.496–499 | INCLUDED_AS_CONTEXT | — | Keep examples. |
| T16 Saturable first-pass metabolism | H2 | T16 pp.499–500 | INCLUDED_AS_MUST | — | Keep T2. |
| T16 Capacity-limited metabolism | H2 | T16 pp.500–506 | INCLUDED_AS_MUST | — | Keep M2-EXT. |
| T16 Concentration-dependent renal excretion | H2 | T16 pp.506–510 | INCLUDED_AS_MUST | — | Keep T1. |
| T16 Saturability of plasma protein and tissue binding | H2 | T16 pp.511–516 | INCLUDED_AS_MUST | — | Keep but compress. |
| T16 Time-dependent kinetics | H2 | T16 pp.516–523 | INCLUDED_AS_MUST | — | Keep. |
| T16 Therapeutic consequences of nonlinearities | H2 | T16 p.524 | PARTIAL | MISSING_AUTHOR_MSG | Add if final summary needs author conclusion. |
| T16 Study problems | Exercises | T16 pp.525–529 | OMITTED_JUSTIFIABLE | Exercises not core | No action. |
| T17 Chapter objectives | Opening | T17 p.531 | PARTIAL | MISSING_AUTHOR_MSG | Include graded nature, displacement unlikely, oral>IV, PM risk. |
| T17 Intro/polypharmacy/definition | Opening text | T17 pp.532–533 | INCLUDED_AS_CONTEXT | — | Keep. |
| T17 Combination products | Table + text | T17 pp.533–534 | INCLUDED_AS_CONTEXT | — | Keep. |
| T17 Transporter comments | Intro text + Table17-3 | T17 pp.535–536 | INCLUDED_AS_CONTEXT/MUST | — | Keep T9 but compress. |
| T17 Altered absorption | H2 | T17 pp.537–538 | INCLUDED_AS_CONTEXT | — | Optional. |
| T17 Altered distribution | H2 | T17 pp.538–544 | INCLUDED_AS_CONTEXT/MUST | — | Downrank displacement. |
| T17 Altered clearance | H2 | T17 pp.544–560 | INCLUDED_AS_MUST | — | Keep T6/T4-EXT/T7/T8. |
| T17 Substrates/Inhibitors/Inducers tables | Tables | T17 pp.545–552 | INCLUDED_AS_MUST | — | Keep selectively. |
| T17 Multifaceted interactions | H2 | T17 pp.563–567 | INCLUDED_AS_MUST | — | Keep T9. |
| T17 Pharmacodynamic interactions | H2 | T17 pp.567–570 | INCLUDED_AS_MUST | — | Keep T10. |
| T17 Study problems | Exercises | T17 pp.570–576 | OMITTED_JUSTIFIABLE | Exercises not core | No action. |

## T5-B. Numbered Equation / Formula Inventory

| PDF Element | Type | PDF Location | Step 1 Status | Omission Verdict | Required Action |
|---|---|---|---|---|---|
| G Eq.2:264–2:265 | Linear model/superposition and proportional dC/dt | G p.114 | INCLUDED_AS_MUST but mis-cited | MISSING_BRIDGE/ERROR | Correct M2 citation. |
| G Eq.2:266–2:267 | CL(C) and elimination rate under MM | G pp.115–116 | INCLUDED_AS_MUST | — | Keep. |
| G Eq.2:268–2:269 | High/low concentration limits | G pp.116–117 | INCLUDED_AS_MUST | — | Keep. |
| G Eq.2:270–2:272 | Bolus MM, AUC, concentration-dependent t1/2 | G p.117 | INCLUDED_AS_MUST | — | Keep. |
| G Eq.2:273 | Constant-rate input + MM | G p.118 | INCLUDED_AS_CONTEXT | — | Keep. |
| G Eq.2:274 | First-order input + MM | G p.118 | INCLUDED_AS_CONTEXT | — | Keep. |
| G Eq.2:275–2:287 | Turnover induction equations | G pp.120–123 | INCLUDED_AS_MUST | — | Keep. |
| G Eq.2:288–2:293 | Autoinduction equations | G pp.126–128 | INCLUDED_AS_MUST | — | Keep. |
| G Eq.2:294–2:303 | Nonlinear binding equations | G pp.129–134 | INCLUDED_AS_MUST | — | Keep. |
| G Eq.2:304–2:308 | Drug-metabolite model ODEs | G pp.136–137 | INCLUDED_AS_MUST | — | Keep. |
| G Eq.2:309 | Concentration-dependent half-life/clearance relation | G p.138 | INCLUDED_AS_CONTEXT/MUST | — | Keep if M6 uses t1/2. |
| G Eq.3:48 | Multiple binding sites | G p.224 | INCLUDED_AS_CONTEXT | — | Keep as context. |
| G Eq.3:49 | Competitive antagonism | G p.225 | INCLUDED_AS_MUST | — | Keep. |
| G Eq.3:50 | Noncompetitive antagonism | G pp.225–226 | INCLUDED_AS_MUST | — | Keep. |
| G Eq.3:51 | General empirical two-drug model | G p.226 | INCLUDED_AS_CONTEXT | — | Keep if M9 remains. |
| G Eq.3:52–3:53 | Enantiomer interaction | G p.227 | INCLUDED_AS_CONTEXT/MUST | — | Keep. |
| G Eq.17:1–17:3 | PK17 case equations | G PK17 | INCLUDED_AS_CONTEXT | — | Keep data anchor. |
| G Eq.18:1–18:13 | PK18 ethanol model and F function | G PK18 | INCLUDED_AS_MUST | — | Keep. |
| G Eq.22:1–22:13 | PK22 autoinduction model | G PK22 | INCLUDED_AS_MUST | — | Keep. |
| T16 Eq.16-1–16-2 | MM metabolism rate / intrinsic clearance | T16 p.494 | INCLUDED_AS_MUST | — | Keep. |
| T16 Eq.16-3 | Saturable transport | T16 p.495 | INCLUDED_AS_MUST | — | Keep. |
| T16 Eq.16-4–16-7 | Capacity-limited metabolism steady-state | T16 pp.500–503 | INCLUDED_AS_MUST | — | Keep. |
| T16 Eq.16-8–16-10 | Phenytoin t90 / plateau approach | T16 p.505 | INCLUDED_AS_MUST | — | Keep. |
| T16 Eq.16-11 | Mixed linear + nonlinear clearance | T16 p.506 | INCLUDED_AS_MUST | — | Keep. |
| T16 Eq.16-12–16-14 | Renal excretion/transport relationships | T16 pp.507–510 | INCLUDED_AS_CONTEXT/MUST | — | Keep. |
| T16 Eq.16-15–16-30 | Study problem equations | T16 pp.525–529 | OMITTED_JUSTIFIABLE | Exercises | No action. |
| T17 Eq.17-1–17-4 | Displacement/distribution relations | T17 pp.539–544 | INCLUDED_AS_CONTEXT/MUST | — | Downrank if overexpanded. |
| T17 Eq.17-5–17-8 | Clearance/half-life/AUC under inhibition | T17 pp.546–549 | INCLUDED_AS_MUST | — | Keep. |
| T17 Eq.17-9–17-12 | Competitive inhibition quantitative framework | T17 pp.550–552 | INCLUDED_AS_MUST | — | Keep; no FDA label unless sourced. |
| T17 Eq.17-13–17-14 | MBI quantitative framework | T17 p.558 | INCLUDED_AS_MUST | — | Keep. |
| T17 Eq.17-15–17-18 | PM/inhibition maximum exposure ratio | T17 pp.558–559 | INCLUDED_AS_MUST | — | Keep; exact 33 caution. |
| T17 Eq.17-19–17-21 | Two full agonists/same receptor effect | T17 pp.567–568 | INCLUDED_AS_MUST | — | Keep. |
| T17 Eq.17-22 | Greco response surface | T17 p.569 | INCLUDED_AS_MUST | — | Keep. |
| T17 Eq.17-23–17-24 | Study problem dose equations | T17 pp.570–571 | OMITTED_JUSTIFIABLE | Exercises | No action. |

---

# T6: Figure Inventory & Learning Value Audit

**Inspection method note:** 아래 항목은 PDF page render/contact sheet를 육안 확인했으므로 기본값은 `VISUAL_INSPECTED`이다. 일부 study-problem figure/table은 학습 본문이 아닌 연습문제 보조자료라 `SKIPPABLE`로 분류했다.

## T6-A. Gabrielsson & Weiner figures/tables

| Figure/Table | Page | Teaches | Value | View Instruction? | Redraw/New Schematic? | Inspection Method | Rationale |
|---|---:|---|---|---|---|---|---|
| Fig.2.85 | G p.113 | Linear vs nonlinear AUC and dose-normalized AUC patterns | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Nonlinearity diagnostic의 출발 도식이다. |
| Fig.2.86 | G p.113 | Linear, feedback, MM, parallel linear+MM elimination profiles | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M1/M2 구조 차이를 한 장에 보여준다. |
| Table 2.15 | G p.114 | Sources of nonlinearities and affected PK parameters | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Scope 전체의 index table이다. |
| Fig.2.87 | G p.115 | Superposition vs lack of superposition; product inhibition | ESSENTIAL | YES | YES | VISUAL_INSPECTED | 선형/비선형의 operational 차이를 보여준다. |
| Fig.2.88 | G p.115 | Concentration-dependent CL and elimination rate | ESSENTIAL | YES | NO | VISUAL_INSPECTED | MM clearance 직관의 핵심 그림이다. |
| Fig.2.89 | G p.116 | Dose-normalized nonlinear IV bolus profiles | USEFUL | YES | NO | VISUAL_INSPECTED | 실제 곡선의 superposition failure를 보강한다. |
| Fig.2.90 | G p.118 | Ethanol parenteral vs oral MM models | USEFUL | NO | YES | VISUAL_INSPECTED | M7 ethanol 연결에는 유용하지만 핵심은 텍스트로도 가능하다. |
| Fig.2.91 | G p.120 | Causes of enzyme level change | USEFUL | NO | YES | VISUAL_INSPECTED | Time-dependence mechanism 분류 보조. |
| Fig.2.92 | G p.120 | Induced vs non-induced CL and concentration-time course | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Time-dependent clearance의 curve effect를 보여준다. |
| Fig.2.93 | G p.121 | Rat/dog repeated dosing simulation | USEFUL | NO | NO | VISUAL_INSPECTED | 종간 scaling/time dependence 사례 보강. |
| Table 2.16 | G p.121 | Drug examples and enzyme turnover half-lives | USEFUL | NO | NO | VISUAL_INSPECTED | Induction time scale examples. |
| Fig.2.94 | G p.124 | Pentobarbital induction turnover model | USEFUL | YES | YES | VISUAL_INSPECTED | Heteroinduction model structure. |
| Fig.2.95 | G p.125 | Nortriptyline before/during/after induction | USEFUL | NO | NO | VISUAL_INSPECTED | Heteroinduction data anchor. |
| Fig.2.96 | G p.125 | Nortriptyline dosing interval profiles | USEFUL | NO | NO | VISUAL_INSPECTED | Fig.2.95 보조. |
| Fig.2.97 | G p.126 | Semi-log decline pre/peri/post induction | USEFUL | NO | NO | VISUAL_INSPECTED | Slopes/MRT 변화 보조. |
| Fig.2.98 | G p.126 | Design points for induction kinetics | USEFUL | NO | YES | VISUAL_INSPECTED | Sampling design concept 보강. |
| Fig.2.99 | G p.127 | Drug model linked to enzyme model | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M3/M4 구조 연결에 핵심. |
| Fig.2.100 | G p.128 | Autoinduction model prediction vs data | USEFUL | YES | NO | VISUAL_INSPECTED | Autoinduction curve anchor. |
| Fig.2.101 | G p.129 | Plasma/tissue unbound-bound equilibrium and modifiers | USEFUL | NO | YES | VISUAL_INSPECTED | Binding system overview. |
| Fig.2.102 | G p.130 | Cu vs C and fu log-log relationship | USEFUL | NO | NO | VISUAL_INSPECTED | Binding equation visual aid. |
| Fig.2.103 | G p.130 | Species differences in free fraction | USEFUL | NO | NO | VISUAL_INSPECTED | Cross-species binding variability. |
| Fig.2.104 | G p.132 | Three in vitro binding systems | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Closed-system conclusion을 보여준다. |
| Fig.2.105 | G p.133 | Three in vivo open binding systems | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Open-system 결론에 핵심이다. |
| Fig.2.106 | G p.136 | Drug/metabolite dose profiles | USEFUL | YES | NO | VISUAL_INSPECTED | M6 data anchor. |
| Fig.2.107 | G p.136 | Drug-metabolite disposition model | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M6 ODE 구조 이해에 필요. |
| Table 2.18 | G p.137 | Drug-metabolite parameter estimates | USEFUL | NO | NO | VISUAL_INSPECTED | M6 numeric anchor. |
| Table 2.19 | G p.138 | Predicted CL/t1/2/MRT using parent/metabolite data | USEFUL | NO | NO | VISUAL_INSPECTED | M6 inference 보조. |
| Table 2.20 | G p.138 | Final parameter estimates | USEFUL | NO | NO | VISUAL_INSPECTED | M6 numeric confirmation. |
| Fig.2.108 | G p.138 | CL and half-life vs concentration | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Nonlinear t1/2 message에 핵심. |
| Fig.2.109 | G p.139 | Observed/predicted plasma concentrations at three doses | USEFUL | NO | NO | VISUAL_INSPECTED | M6 outcome plot. |
| Fig.2.110 | G p.139 | Ethanol clearance vs concentration and hepatic blood flow | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Capacity/flow 결합 시각화. |
| Fig.2.111 | G p.139 | Linear vs nonlinear dose variability | USEFUL | YES | NO | VISUAL_INSPECTED | Ethanol nonlinearity 보강. |
| Fig.2.112 | G p.140 | Ethanol concentration-time variability under fasting/meal/aspirin+meal | USEFUL | YES | NO | VISUAL_INSPECTED | Forensic variability message. |
| Fig.3.23 | G p.224 | Multiple binding site response peak/decline | USEFUL | NO | NO | VISUAL_INSPECTED | M9 multiple binding context. |
| Fig.3.24 | G p.225 | Competitive antagonism curve shift | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Eq.3:49 interpretation에 핵심. |
| Fig.3.25 | G p.226 | Noncompetitive antagonism Emax reduction | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Eq.3:50 interpretation에 핵심. |
| Table 3.2 | G p.226 | General empirical dynamic model cases | USEFUL | NO | NO | VISUAL_INSPECTED | M9 model taxonomy. |
| Fig.3.26 | G p.227 | Ketamine enantiomer concentration-response | USEFUL | NO | NO | VISUAL_INSPECTED | Enantiomer interaction example. |
| Fig.17.1 | G p.554–555 | PK17 observed/fitted linear vs MM model | USEFUL | YES | NO | VISUAL_INSPECTED | Case-study support. |
| Table 17.1 | G p.555 | First-order vs MM parameter estimates | USEFUL | YES | NO | VISUAL_INSPECTED | PK17 numeric anchor. |
| Fig.18.1 | G p.557 | Ethanol IV infusion fit | USEFUL | YES | NO | VISUAL_INSPECTED | PK18 data anchor. |
| Fig.18.2 | G p.558 | Ethanol initial estimate plots | USEFUL | NO | NO | VISUAL_INSPECTED | Parameter estimation support. |
| Fig.18.3 | G p.561 | Ethanol F vs concentration/Vmax/Km/QH | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Ethanol oral F nonlinearity 핵심. |
| Fig.18.4 | G p.562 | Ethanol CLH 3D surface | USEFUL | YES | YES | VISUAL_INSPECTED | Flow-capacity integration. |
| Table 18.1 | G p.562 | Ethanol parameter comparisons | USEFUL | NO | NO | VISUAL_INSPECTED | Numeric support. |
| Fig.22.1 | G p.581 | Compound X repeated infusion autoinduction data | ESSENTIAL | YES | NO | VISUAL_INSPECTED | PK22 observed pattern. |
| Fig.22.2 | G p.581 | Proposed autoinduction model | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M4 model structure. |
| Table 22.1 | G p.582 | Compound X concentration-time data | USEFUL | NO | NO | VISUAL_INSPECTED | Case dataset. |
| Fig.22.3 | G p.584 | Causes of enzyme level change | USEFUL | NO | YES | VISUAL_INSPECTED | Turnover design support. |
| Table 22.2 | G p.585 | Initial/final PK22 parameter estimates | ESSENTIAL | YES | NO | VISUAL_INSPECTED | M4 numeric anchor. |

## T6-B. Rowland & Tozer Ch.16 figures/tables

| Figure/Table | Page | Teaches | Value | View Instruction? | Redraw/New Schematic? | Inspection Method | Rationale |
|---|---:|---|---|---|---|---|---|
| Fig.16-1 | T16 p.493 | Four saturable processes: dissolution, metabolism, transport, binding | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Ch.16 전체 map이다. |
| Fig.16-2 | T16 p.494 | MM metabolism rate and intrinsic clearance | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Eq.16-1/16-2 이해에 핵심. |
| Fig.16-3 | T16 p.497 | Response C50 vs metabolism Km comparison | USEFUL | NO | NO | VISUAL_INSPECTED | Nonlinearity frequency 비교 보조. |
| Table 16-1 | T16 p.496 | Processes/mechanisms showing saturability | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Example inventory. |
| Fig.16-4 | T16 p.498 | Griseofulvin solubility-limited absorption | USEFUL | NO | NO | VISUAL_INSPECTED | Absorption context. |
| Fig.16-5 | T16 p.498 | Amoxicillin saturable absorption | USEFUL | NO | NO | VISUAL_INSPECTED | Transport context. |
| Fig.16-6 | T16 p.499 | Methylphenidate enantiomer first-pass | USEFUL | NO | NO | VISUAL_INSPECTED | First-pass example. |
| Table 16-2 | T16 p.499 | Nicardipine F by dose | ESSENTIAL | YES | NO | VISUAL_INSPECTED | T2 core numeric anchor. |
| Fig.16-7 | T16 p.501 | Alcohol absorption rate and AUC/peak changes | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Alcohol nonlinear interpretation. |
| Fig.16-8 | T16 p.502 | Zero-order elimination after bolus/infusion | USEFUL | YES | YES | VISUAL_INSPECTED | Alcohol/capacity intuition. |
| Fig.16-9 | T16 p.503 | Phenytoin Css vs dosing rate | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M2-EXT apex visual. |
| Fig.16-10 | T16 p.505 | Phenytoin time-to-plateau vs dosing rate | ESSENTIAL | YES | NO | VISUAL_INSPECTED | t90 발산 핵심. |
| Fig.16-11 | T16 p.505 | Phenytoin pseudosteady-state after dose reduction | USEFUL | YES | NO | VISUAL_INSPECTED | Clinical time-course support. |
| Fig.16-12 | T16 p.507 | Saturable renal secretion rate vs filtration | USEFUL | NO | YES | VISUAL_INSPECTED | T1 concept. |
| Fig.16-13 | T16 p.508 | Dicloxacillin saturable secretion | ESSENTIAL | YES | NO | VISUAL_INSPECTED | T1 clinical data anchor. |
| Fig.16-14 | T16 p.509 | Renal secretion vs reabsorption direction | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Secretion/reabsorption 분기 핵심. |
| Fig.16-15 | T16 p.509 | Ascorbic acid saturable reabsorption | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Ascorbic acid anchor. |
| Fig.16-16 | T16 p.510 | Disopyramide total vs unbound renal CL | USEFUL | NO | NO | VISUAL_INSPECTED | Binding/renal context. |
| Fig.16-17 | T16 p.512 | Naproxen nonlinear AUC/Cmax | USEFUL | NO | NO | VISUAL_INSPECTED | Protein binding prototype. |
| Fig.16-18 | T16 p.513 | Cefonicid total/unbound profiles and binding | USEFUL | NO | NO | VISUAL_INSPECTED | Protein binding prototype. |
| Fig.16-19 | T16 p.514 | Trandolaprilat nonlinear kinetics/binding | USEFUL | NO | NO | VISUAL_INSPECTED | Target/binding prototype. |
| Fig.16-20 | T16 p.515 | Bosentan Vss decreases with dose | ESSENTIAL | YES | NO | VISUAL_INSPECTED | TMDD/saturable tissue binding prototype. |
| Fig.16-21 | T16 p.515 | Imirestat dose-normalized profile reversal | USEFUL | NO | NO | VISUAL_INSPECTED | TMDD prototype. |
| Fig.16-22 | T16 p.516 | Draflazine plasma/blood profiles | USEFUL | NO | NO | VISUAL_INSPECTED | Transport/binding prototype. |
| Fig.16-23 | T16 p.516 | Draflazine blood/plasma concentration relation | USEFUL | NO | NO | VISUAL_INSPECTED | Fig.16-22 support. |
| Fig.16-24 | T16 p.517 | Verapamil time-of-administration profiles | USEFUL | NO | NO | VISUAL_INSPECTED | Chronopharm context. |
| Fig.16-25 | T16 p.518 | Carbamazepine autoinduction | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Time-dependent kinetics anchor. |
| Fig.16-26 | T16 p.519 | Clarithromycin single/multiple dose time course | ESSENTIAL | YES | NO | VISUAL_INSPECTED | MBI clue. |
| Fig.16-27 | T16 p.520 | Salicylic acid single-dose diagnostic steps | USEFUL | NO | NO | VISUAL_INSPECTED | Opposing nonlinearities setup. |
| Fig.16-28 | T16 p.522 | Salicylic acid fu and unbound CL opposing changes | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Opposing nonlinearities 핵심. |
| Fig.16-29 | T16 p.522 | Salicylic acid unbound concentration vs dosing rate | USEFUL | NO | NO | VISUAL_INSPECTED | Fig.16-28 clinical consequence. |
| Fig.16-30 | T16 p.524 | Ethchlorvynol intoxication/dialysis | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Interesting but peripheral. |
| Tables 16-3–16-13 | T16 pp.525–529 | Study-problem datasets | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Exercise material; not required for Step 1 concept chain. |

## T6-C. Rowland & Tozer Ch.17 figures/tables

| Figure/Table | Page | Teaches | Value | View Instruction? | Redraw/New Schematic? | Inspection Method | Rationale |
|---|---:|---|---|---|---|---|---|
| Table 17-1 | T17 p.533 | Interactions to avoid by PK/PD parameter | USEFUL | NO | NO | VISUAL_INSPECTED | Intro classification. |
| Table 17-2 | T17 p.534 | Pharmacokinetically driven combination products | USEFUL | NO | NO | VISUAL_INSPECTED | Beneficial DDI context. |
| Table 17-3 | T17 p.535 | Transporter-mediated clinical DDIs | ESSENTIAL | YES | NO | VISUAL_INSPECTED | T9 case pool. |
| Fig.17-1 | T17 p.537 | Altered absorption initiation/withdrawal scenarios | USEFUL | NO | YES | VISUAL_INSPECTED | Sequence effect support. |
| Fig.17-2 | T17 p.538 | Displacement at plateau by extraction/route | ESSENTIAL for T5 | YES | YES | VISUAL_INSPECTED | Displacement mechanism visual. |
| Fig.17-3 | T17 p.543 | Valproate-phenytoin displacement-only case | USEFUL | YES | NO | VISUAL_INSPECTED | T5 data anchor. |
| Fig.17-4 | T17 p.544 | Displacer infusion/withdrawal simulation | USEFUL | NO | NO | VISUAL_INSPECTED | T5 support. |
| Fig.17-5 | T17 p.545 | CYP enzymes/substrates/inhibitors/inducers | USEFUL | NO | NO | VISUAL_INSPECTED | DDI overview. |
| Table 17-4 | T17 p.545 | Selected CYP substrates/inhibitors/inducers | USEFUL | NO | NO | VISUAL_INSPECTED | Supporting list. |
| Fig.17-6 | T17 p.546 | Theophylline-enoxacin clinical time course | ESSENTIAL | YES | NO | VISUAL_INSPECTED | T6 primary case. |
| Fig.17-7 | T17 p.547 | Graded enoxacin inhibition by dose | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Inhibition graded nature. |
| Fig.17-8 | T17 p.550 | AUC ratio by Cu/KI and fm | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Eq.17-11 intuition. |
| Fig.17-9 | T17 p.552 | Insidious concentration rise under inhibition | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Time-course safety message. |
| Table 17-5 | T17 p.549 | Strong/moderate/weak inhibitor classification | ESSENTIAL | YES | NO | VISUAL_INSPECTED | DDI classification anchor. |
| Table 17-6 | T17 p.551 | Substrates with ≥4-fold AUC increase | USEFUL | NO | NO | VISUAL_INSPECTED | Example list. |
| Table 17-7 | T17 p.553 | Diltiazem-lovastatin route effect | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Oral vs IV DDI message. |
| Fig.17-10 | T17 p.554 | Fluconazole-midazolam oral vs IV effect | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Route/extraction message. |
| Fig.17-11 | T17 p.555 | Rosuvastatin-cyclosporine transporter DDI | USEFUL | YES | NO | VISUAL_INSPECTED | T9 case anchor. |
| Fig.17-12 | T17 p.556 | Imipenem-cilastatin beneficial inhibition | USEFUL | NO | NO | VISUAL_INSPECTED | Combination-product example. |
| Fig.17-13 | T17 p.557 | Midazolam-clarithromycin MBI effect | ESSENTIAL | YES | NO | VISUAL_INSPECTED | MBI primary case. |
| Fig.17-14 | T17 p.558 | MBI mechanism scheme | ESSENTIAL | YES | YES | VISUAL_INSPECTED | T4-EXT structure. |
| Fig.17-15 | T17 p.559 | PM + nonpolymorphic pathway inhibitor max exposure | ESSENTIAL | YES | YES | VISUAL_INSPECTED | T7 core visual. |
| Fig.17-16 | T17 p.560 | Induction initiation/withdrawal dose trap | ESSENTIAL | YES | YES | VISUAL_INSPECTED | T8 clinical trap. |
| Fig.17-17 | T17 p.561 | Phenobarbital-dicumarol induction | ESSENTIAL | YES | NO | VISUAL_INSPECTED | T8 data anchor. |
| Fig.17-18 | T17 p.563 | Warfarin-phenylbutazone multifaceted interaction | USEFUL | YES | NO | VISUAL_INSPECTED | T5/T9 caution. |
| Table 17-8 | T17 p.564 | Digoxin-quinidine PK parameter changes | ESSENTIAL | YES | NO | VISUAL_INSPECTED | T9 primary numeric anchor. |
| Fig.17-19 | T17 p.565 | Atorvastatin-rifampin acute transporter DDI | ESSENTIAL | YES | NO | VISUAL_INSPECTED | T9 mechanism-diagnosis anchor. |
| Fig.17-20 | T17 p.567 | Two full agonists same receptor ceiling effect | ESSENTIAL | YES | YES | VISUAL_INSPECTED | T10 core. |
| Fig.17-21 | T17 p.568 | Isobologram: additive/synergy/antagonism | ESSENTIAL | YES | YES | VISUAL_INSPECTED | T10 core. |
| Fig.17-22 | T17 p.570 | Study problem simulation profiles | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Exercise-only. |
| Fig.17-23 | T17 p.573 | Study problem concentration-response/interaction graph | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Exercise-only. |
| Fig.17-24 | T17 p.576 | Study problem semilog plot | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Exercise-only. |
| Tables 17-9–17-13 | T17 pp.570–576 | Study-problem datasets and parameter scenarios | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Exercise-only; omission justified. |

---

# Patch Memo Independent Classification

| Patch Memo Item | Classification | Source-Fidelity Judgment |
|---|---|---|
| Source coverage is high | MATCH | Draft does cover all three PDFs broadly. |
| HTML 직행 금지 / Phase 2 필요 | OPTIONAL/MATCH | Workflow judgment is reasonable; not a source claim. |
| MUST too many / compress to 5–6 master cards | OPTIONAL | Valid editing recommendation; not source fidelity error. |
| Stage 1 별도 산출물 참조 is risky | MATCH | Draft is not self-contained in M1–M9; source chain could break. |
| FDA/NDA/CPIC/Mager-Jusko/NONMEM code as scope creep | MATCH | These are not in attached PDFs, except textbook equations underlying some DDI logic. |
| Displacement-only should be context | MATCH/OPTIONAL | Source supports displacement importance but top-level priority can be reduced. |
| Figure budget concern | OPTIONAL | Phase 4C editorial issue; T6 identifies essential figures. |
| Eq.17-9~17-14 / Eq.17-18 must be verified | MATCH | These are central R&T Ch.17 equations and are correctly prioritized. |
| Eq.16-7~16-10 must be verified | MATCH | These are central phenytoin MM steady-state equations. |
| PK17/PK18/PK22 anchors must be verified | MATCH | These case studies are central G data anchors. |

---

# Final Source-Fidelity Decision

**Final status:** `CONDITIONAL PASS`  
**HTML readiness:** `NO — Phase 4A compression and source-tag cleanup required.`  
**Rewrite requirement:** `No full rewrite required, but MUST_FIX patches are mandatory.`

**Most important source-backed spine to preserve:**

1. `Nonlinearity diagnostics`: dose-normalized plots + superposition failure.
2. `Capacity-limited MM`: Vmax/Km, concentration-dependent CL/t1/2, phenytoin/alcohol/ascorbic acid anchors.
3. `Time-dependent turnover`: enzyme turnover, induction/autoinduction/MBI.
4. `Binding/TMDD/displacement`: open vs closed binding, tissue/target binding, displacement-only DDI caution.
5. `DDI quantitative prediction`: reversible inhibition, MBI, induction, route/extraction, PM×inhibitor risk, transporter/multifaceted cases.
6. `PD interactions`: competitive/noncompetitive receptor models, two agonists, isobologram.

**Mandatory source-tag rule for next phase:**  
`PDF 직접 근거`와 `[실무 추론]`, `[후속 규제 연결]`, `[후속 세션]`, `[가상 Boss Dilemma]`를 반드시 분리해야 한다. The equations can remain, but regulatory/labeling claims cannot be presented as PDF-derived facts unless an external regulatory source is later supplied and audited.

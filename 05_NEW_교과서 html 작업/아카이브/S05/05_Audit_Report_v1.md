# 05_Audit Report v1
## Source Fidelity Audit — Session 05 Step 1 Draft v0

**업무 형태:** 파일 분석 / PDF 대조 감사 / 웹 검색 OFF  
**감사 입력:**
- `05_G_2구획 모델 α:β·재파라미터화(2).pdf` — G&W 5e Ch.2 §2.4.1–2.4.6 + PK7/PK8
- `05_T_2구획 모델 α:β·재파라미터화(2).pdf` — Rowland & Tozer 5e Ch.19
- `05_step1_draft_v0.md`
- `S05_phase1_patch memo(1).md` — audit attention guide only, 자동 채택하지 않음

**최종 판정:**  
Step 1 Draft v0는 구조와 큐레이션은 양호하나, source fidelity 기준에서는 **HTML 직행 불가**입니다. 핵심 수식 골격과 주요 사례 배치는 대체로 맞습니다. 그러나 **condition number 범위 오류**, **aspirin clearance 왜곡 방향 오류**, **규제/NONMEM 확장 문구의 source tag 미분리**, **R&T/G&W가 명시한 모델 비식별성·terminal half-life 경고의 일부 과장 표현**은 Phase 4A 전에 반드시 패치해야 합니다.

---

## T1: Equation/Numerical Audit

| Item | Draft v0 Expression | PDF Source | Classification | Correction |
|---|---|---|---|---|
| Bi-exponential IV bolus | `C(t)=A·e^{-αt}+B·e^{-βt}, α>β>0` | G&W Eq.2:117; R&T Eq.19-2 | MATCH | 유지. G&W는 `b`/`β` 혼용. 표기 통일만 필요. |
| Half-lives | `t1/2,α=ln2/α`, `t1/2,β=ln2/β` | G&W Eq.2:118–2:119 | MATCH | 유지. |
| Residual method | terminal phase back-extrapolation 후 subtraction | G&W p.60 Fig.2.43 설명; R&T aspirin residual procedure | MATCH | 유지. |
| G&W Fig.2.43 values | `A≈70`, `B=28`, `α=ln(70/10)/130=0.0150 min^-1`, `β=ln(28/10)/450=0.00229 min^-1` | G&W Fig.2.43 caption | MATCH | 유지. 단, source figure는 y-axis `µg/L`, caption은 `mg/L`처럼 보이는 단위 혼재가 있어 최종본에서는 `source unit as printed` 또는 `[단위 확인 필요]` 각주 권장. |
| `C0=A+B` | Draft uses as validation | G&W p.60, R&T Eq.19-3 context | MATCH | 유지. |
| `AUC=A/α+B/β` | G&W Eq.2:130; R&T Eq.19-8 | MATCH | 유지. |
| `AUMC=A/α²+B/β²` | G&W Eq.2:136; R&T Eq.19-22 | MATCH | 유지. |
| Fractional areas | `f1=(A/α)/AUC`, `f2=(B/β)/AUC` | G&W Eq.2:133–2:134; R&T Eq.19-12 | MATCH | 유지. |
| “fractional area determines elimination phase” | Draft M1/M5 | G&W p.63 Table 2.4/Fig.2.45; R&T p.622 | MATCH | 유지. 매우 핵심. |
| 2-compartment ODE amount equations | `dA1/dt=-(k12+k10)A1+k21A2`, `dA2/dt=k12A1-k21A2` | R&T Eq.19-4–19-5; G&W equivalent ODE concentration form Eq.2:159–2:160 | MATCH | 유지. Source에서는 prose/formula로 제시됨. |
| Eigenvalue explanation | `α,β are eigenvalues of system matrix` | Not explicitly taught in G&W/R&T; mathematically implied by Eq.2:124–2:125/Table 19-1 | NOT_IN_SOURCE | 삭제 불필요. `[수학적 해석]` 또는 `[derived interpretation]` tag 필수. |
| `α+β=k12+k21+k10`, `αβ=k21k10` | implied by G&W Eq.2:124–2:125 and R&T Table 19-1 | MATCH | 유지. |
| Macro→Micro formulas | `A`, `B`, `Vc`, `k21`, `k10`, `k12` formulas | G&W Eq.2:121–2:129 | MATCH | 유지. |
| `Cld=k12·Vc=k21·Vt` | G&W Eq.2:120; Eq.2:158a,b | MATCH | 유지. R&T Eq number citation should be removed or changed to Table 19-1/compartment model discussion; R&T does not label this as Eq.2:158. |
| `CL=k10·Vc` | R&T p.618; Table 19-1; G&W physiological model | MATCH | 유지. |
| NONMEM ADVAN3/TRANS4 code | `CL,V1,Q,V2; K=CL/V1; K12=Q/V1; K21=Q/V2` | Not in G&W/R&T PDFs; external NONMEM manual knowledge | NOT_IN_SOURCE | 본문 source claim처럼 두지 말고 `[실무 확장: NONMEM implementation]`으로 분리. |
| TRANS3 vs TRANS4 covariance claim | TRANS3 lower correlation, TRANS4 fallback etc. | Not in supplied PDFs | NOT_IN_SOURCE | 유지하려면 `[실무 확장/확인 필요]`; PDF 대조 감사 기준으로는 source unsupported. |
| “2-compartment has 4 degrees of freedom: Vc,Vt,k10,k12(or k21)” | Draft M2 | G&W Table 2.6 says micro: `Vc,k10,k12,k21`; physiological: `Vc,Cl,Cld,Vt` | ERROR | `Vc,k10,k12,k21` 또는 `Vc,CL,Cld,Vt`로 수정. `Vc,Vt,k10,k12(or k21)`는 혼합 좌표계라 부정확. |
| “Three 2-comp models are structurally non-identifiable from plasma data alone” | Draft M1/M2 | G&W Fig.2.46/p.65; R&T p.618–619 | MATCH | 유지. |
| `V1=Dose/(A+B)=Div/C0` | R&T Eq.19-3; G&W Eq.2:129 for Vc | MATCH | 유지. |
| `Vβ=CL/β=Dose/(AUC·β)` | R&T Eq.19-11; G&W Vz discussion PK8 | MATCH | 유지. |
| `Vss=MRT·CL=Dose·AUMC/AUC²` | G&W Eq.2:140/2:164; R&T Eq.19-23 | MATCH | 유지. |
| `Vss=V1(1+k12/k21)` | G&W Eq.2:141; R&T Table 19-1 | MATCH | 유지, 단 central elimination only / standard two-compartment assumption 명시. |
| Formal table `Vss = (V1·k12 + Vt·k21)/... = V1(1+k12/k21)` | Draft M3 table | No exact source expression; ellipsis formula is not auditable | ERROR | 중간의 `...` 식 삭제. `Vss=MRT·CL`, `Vss=V1(1+k12/k21)`, 또는 `Vss=V1+V2`만 사용. |
| `V1≤Vss≤Vβ` | R&T p.629–630 says Vss lies between V1 and V | MATCH | 유지하되 “under standard source assumptions” 범위 표시. |
| Aspirin biexponential | `C=67e^-0.23t+33e^-0.050t` | R&T p.616 | MATCH | 유지. |
| Aspirin one-compartment values | `k=0.050 min^-1`, `t1/2=14 min`, `C0=33 mg/L`, `V=20 L`, `CL=0.98 L/min` | R&T p.615 | MATCH | Draft의 `985 mL/min`은 source의 `0.98 L/min`과 실질적으로 근접하나 최종본은 `0.98 L/min` 또는 `980 mL/min` 권장. |
| Aspirin two-compartment CL | `CL=683 mL/min` | R&T p.620 | MATCH | 유지. |
| Aspirin “clearance 30% off” | Draft says 1-comp CL vs 2-comp CL differs ~30% | R&T p.620: 0.98 L/min vs 683 mL/min | RESTORED | 방향과 기준을 명확히 해야 함. 2-comp true CL은 1-comp estimate보다 약 30% 낮고, 1-comp estimate는 true CL을 약 44% overestimate. |
| Aspirin “all subsequent dosing calculations underestimated by 30%” | Draft M1 | R&T says one-comp CL is overestimate | ERROR | `유지용량은 과소평가가 아니라 과대평가될 위험`; 또는 `exposure for a fixed dose is underpredicted`로 수정. |
| Aspirin V values | `V1=6.5L`, `Vss=10.4L`, `Vβ=13.7L`, `f1=0.31`, `f2=0.69`, `t1/2,e=10.5min` | R&T p.617, p.622, p.629–630; derived from equations | MATCH | 유지. |
| Salicylic acid values | `V=10.5L`, `Vss=10.2L`, `V1=5.3L` | R&T p.629–630 | MATCH | 유지. |
| Gentamicin values | `V=345L`, `Vss=56L`, `V1=14L`; terminal `87hr`, initial `~4hr`; `f2≈0` | R&T p.630, p.635–636, p.632 | MATCH | 유지. |
| Gentamicin accumulation index | `1/(1-e^{-βτ})≈16` for τ=8hr, t1/2=87hr | R&T Fig.19-14 narrative supports 16-fold terminal/tissue accumulation | MATCH | 유지. |
| “gentamicin Vβ-based dose adjustment causes nephrotoxicity/inefficacy simultaneously” | Draft M3 | Source discusses renal impairment, tissue accumulation, and dosing rate adjustment, but not this causal claim | NOT_IN_SOURCE | `[실무 추론]`으로 낮추거나 삭제. |
| `Amount in slowly equilibrating tissue = (Vss−V1)Css` | R&T Eq.19-30 | MATCH | 유지. |
| Nicardipine terminal t1/2 12hr; 50% Css 1hr; 90% ~15hr | R&T Fig.19-10/p.631 | MATCH | 유지. |
| Eq.19-26 plateau equation | Draft uses `C/Css=f1(1-e^-αt)+f2(1-e^-βt)` | R&T Eq.19-26/19-27 | MATCH | 유지. |
| “terminal half-life = 5×t1/2 to plateau” | Draft phrase | R&T uses 1 half-life for 50%, 3.3 terminal half-lives for 90%; general 5× is not source here | NOT_IN_SOURCE | 표현을 source-aligned하게 `1 t1/2 for 50%, 3.3 t1/2 for 90%`로 수정. |
| “항상 빗나간다” | Draft M5 | R&T says terminal half-life ceases to have simple application; also notes many drugs have f2>0.8 | ERROR | `f2와 dosing context를 확인하지 않으면 빗나갈 수 있다`로 완화. |
| Effective half-life `ln2·MRT` | G&W Eq.2:139 | MATCH | 유지. |
| “effective half-life is true elimination-oriented half-life” | Draft M5 | Interpretive, not directly R&T/G&W wording | OPTIONAL | `[해석]` tag 권장. |
| G&W PK8 condition numbers in table | `Macro 125.2; Takada 3186; Colburn 2243; Reparam 2306; ODE 29.69` | G&W PK8 Table 8.1 | MATCH | 유지. |
| Condition number range in curation | `29.69–4,104` | 4,104 belongs to PK7 tri-exponential Table 7.1, not PK8 Table 8.1 | ERROR | `29.69–3,186`로 수정. |
| “200배 진폭” | Draft M4 | 3186/29.69≈107; 4104/29.69≈138 | ERROR | `약 100배 이상` 또는 `약 107배`로 수정. |
| `condition number >1000 threshold` | Draft M4 | Not in supplied PDFs | NOT_IN_SOURCE | `[실무 기준/외부 지식]` tag 필요. |
| “NDA Deficiency Letter direct trigger” | Draft M3/M4/§8 | Not in supplied PDFs | NOT_IN_SOURCE | `[실무 추론] regulatory risk`로 낮추기. |
| “FDA Population PK Guidance recommends physiological parameterization” | Draft Q9/M3 | Not in supplied PDFs | NOT_IN_SOURCE | PDF 대조 기준에서는 삭제 또는 `[외부 근거 필요]`. |
| Takada model equation | `C=Div/(Vc+Vt)e^-βt`, `Vt=Vmax·t/(Kd+t)` | G&W Eq.2:150–2:151 / PK8 Eq.8:2–8:3 | MATCH | 유지. |
| Colburn model equation | `C=Div/(Vc+Vt)e^-βt`, `Vt=Vmax(1-e^-Kvt)` | G&W Eq.2:152–2:153 / PK8 Eq.8:4–8:5 | MATCH | 유지. |
| Reparameterized CL model | `A=α(Div/CL−B/β)`; substituted equation | G&W Eq.2:148–2:149 / PK8 Eq.8:6–8:8 | MATCH | 유지. |
| PK7 condition values | Mono 4778, Bi 446, Tri 4104 | G&W PK7 Table 7.1 | DRAFT_MISSING_CONTEXT | If 4104 is used anywhere, explicitly label it PK7 tri-exponential, not PK8. |
| PK8 final conclusion | Takada lowest WRSS; ODE lowest condition number; if initial phase hardly discernible, NCA proposed | G&W PK8 p.516–517 | PARTIAL | Add missing NCA fallback sentence in M4 Limitations. |

---

## T2: Examples & Data Audit

| Item | Draft v0 Status | PDF Location | Classification | Importance | Action |
|---|---|---|---|---|---|
| G&W Fig.2.39 mono-/bi-/multi-exponential decline | Mentioned conceptually | G&W p.57 | INCLUDED_CORRECT | MEDIUM | 유지. view instruction optional. |
| Catenary vs mammillary systems | Context only | G&W p.58 Fig.2.40–2.41 | INCLUDED_CORRECT | LOW | 유지. catenary=EHC 예시는 source 없음. |
| Central/peripheral/urine time profiles | Mentioned via Fig.2.42 | G&W p.59 | INCLUDED_CORRECT | MEDIUM | 유지. Fig.2.42 view instruction useful. |
| Fig.2.43 bi-exponential residual method | Core M1 | G&W p.60 | INCLUDED_CORRECT | HIGH | 유지. ESSENTIAL figure. |
| Fig.2.45/Table 2.4 initial vs terminal “elimination phase” | Reflected in fractional area discussion | G&W p.63 | INCLUDED_CORRECT | HIGH | 유지. Final HTML에서 Fig.2.45 view instruction 권장. |
| Fig.2.46 three structurally different 2-comp models | Included | G&W p.65 | INCLUDED_CORRECT | HIGH | 유지. structural non-identifiability source anchor. |
| SHAM Table 2.5 | Mostly omitted | G&W p.66 | MISSING | LOW | Omitted justifiable; NCA/SHAM separate. |
| Reparameterization section 2.4.3 | Included in M4 | G&W p.66–71 | INCLUDED_CORRECT | HIGH | 유지. |
| Fig.2.47 time-dependent volume | Included in M4 | G&W p.67 | INCLUDED_CORRECT | MEDIUM | 유지. |
| Fig.2.48/2.49 physiological ODE model | Included in M2/M4 | G&W p.68 | INCLUDED_CORRECT | HIGH | 유지. |
| Fig.2.50 partition/central-peripheral equality at SS | Lightly omitted | G&W p.70 | MISSING | MEDIUM | Add 1 sentence caveat: if central/peripheral concentrations are not equal at SS, partitioning may require two Cld terms and tissue data. |
| Constant-rate infusion Eq.2:166–2:168 | Context only | G&W p.72–73 | INCLUDED_AS_CONTEXT | MEDIUM | 유지. Detailed derivation can remain out of Step 1. |
| Extravascular administration Eq.2:169–2:174 | Context only | G&W p.74–75 | INCLUDED_AS_CONTEXT | LOW | 유지. |
| Plasma + urine data Eq.2:175–2:179 | Context only | G&W p.76–77 | INCLUDED_AS_CONTEXT | LOW | 유지. |
| G&W PK7 100 µg IV bolus Part I | Briefly not anchored in main cards | G&W p.505–509 | MISSING | MEDIUM | Add one context note: PK7 supports bi- vs tri-exponential discrimination and residual/AIC/precision trade-off. |
| G&W PK7 Part II AIC/F-test | Only §8 future mention | G&W p.509–512 | MISSING | MEDIUM | Add “F-test not sufficient; simplest adequate model + residuals + precision” context. |
| G&W PK8 Compound X 100 µg IV bolus | Core M4 | G&W p.513–517 | INCLUDED_CORRECT | HIGH | 유지. Correct condition number range. |
| G&W PK8 NCA fallback when initial phase hardly discernible | Missing | G&W p.517 | MISSING | HIGH | Add to M4 limitations: if initial phase is hardly discernible but cannot be excluded, G&W propose NCA. |
| R&T Thiopental dog 25 mg/kg IV | Included in M1 L4 | R&T p.614–615 Fig.19-1 | INCLUDED_CORRECT | HIGH | 유지. 핵심 direct evidence. |
| Thiopental adipose-to-plasma partition coefficient 10; fat ~40% of Vd; <20% eliminated by 3hr | Mostly omitted | R&T p.614–615 | MISSING | MEDIUM | Optional enrichment in M1 L4 if space. |
| Zoledronic acid and azithromycin redistribution examples | Omitted | R&T p.615 | MISSING | LOW | Omission justifiable. |
| Aspirin 650 mg IV bolus | Core M1/M3/self-test | R&T p.615–622 | INCLUDED_ERROR | HIGH | Numerical values OK; dose-calculation direction must fix. |
| Aspirin V1/V/Vss comparison | Core M3 | R&T p.617, p.621–630 | INCLUDED_CORRECT | HIGH | 유지. |
| Digoxin oral distribution nose | Context in M5 | R&T p.624–625 Fig.19-5–19-6 | INCLUDED_CORRECT | MEDIUM | 유지 as context. |
| Midazolam-like short infusion Cmax reduction | Context in M1 | R&T p.624–625 Fig.19-7 | INCLUDED_CORRECT | MEDIUM | 유지; clarify source says “drug with kinetics similar to midazolam,” not direct midazolam dataset. |
| Long-term infusion stop/propofol-like schematic | Mostly omitted | R&T p.626–627 Fig.19-8 | MISSING | LOW | Omission justifiable. |
| V1/V/Vss explanatory Fig.19-9 | Core M3 | R&T p.628 | INCLUDED_CORRECT | HIGH | 유지. ESSENTIAL figure. |
| Endogenous tracer example | Omitted | R&T p.630 | MISSING | LOW | Omission justifiable. |
| Nicardipine 0.5 mg/hr infusion, 37 patients, terminal 12hr, 50% Css 1hr, 90% 15hr | Core M5 | R&T p.631 Fig.19-10 | INCLUDED_CORRECT | HIGH | 유지. |
| Fig.19-11 f2 spectrum | Core M5 | R&T p.632 | INCLUDED_CORRECT | HIGH | 유지. ESSENTIAL figure. |
| Fig.19-12 plasma vs slowly equilibrating tissue | Included in M5 limitation | R&T p.633–634 | INCLUDED_CORRECT | HIGH | 유지. |
| Eptifibatide bolus+infusion, 180 µg/kg supplemental bolus | Context | R&T p.634–635 Fig.19-13 | INCLUDED_CORRECT | MEDIUM | 유지. |
| Gentamicin 8-hourly IM regimen | Core M5 | R&T p.635–636 Fig.19-14 | INCLUDED_CORRECT | HIGH | 유지. |
| Oral dosing regimen design when effect wears off | Mostly omitted | R&T p.637–638 Fig.19-15 | MISSING | MEDIUM | Step 1 omission acceptable if PD/oral regimen out-of-scope; can add context line only. |
| Volume term utility during multiple dosing | Partially included | R&T p.638–639 Fig.19-16 | PARTIAL | HIGH | Add one explicit sentence: Vss only applies when fluctuation is small/near true SS; V applies late in interval after distribution equilibrium; neither works well for gentamicin-like cases. |
| Tobramycin renal impairment Fig.19-17 | Contextualized with gentamicin renal impairment | R&T p.640 | INCLUDED_CORRECT | MEDIUM | 유지. |
| Renal function simulation Fig.19-18; <7% normal threshold | Partially included | R&T p.640–641 | PARTIAL | MEDIUM | Add if discussing renal impairment; otherwise optional. |
| Drug redistribution/hemodialysis rebound/lithium | Excluded | R&T p.641–643 Fig.19-19 | MISSING | LOW | Exclusion justifiable. |
| Pharmacodynamic response sections and examples | Excluded | R&T p.644–656 Fig.19-20–19-32/Tables 19-2–19-5 | MISSING | LOW–MEDIUM | Exclusion mostly justifiable under draft scope, but source range includes them; document as out-of-scope rather than silently omit. |

---

## T3: Author Key Messages

| Message | PDF Location | In Draft v0? | Status |
|---|---|---|---|
| One-compartment representation is useful for fundamentals but inaccurate when distribution takes time. | R&T p.613–614 | Yes | MATCH |
| Error from ignoring distribution kinetics becomes unacceptable when observations are misinterpreted or dosage calculations differ substantially. | R&T p.614 | Partial | SHOULD_FIX — currently present via examples but overstates some directions. |
| Evidence of distribution kinetics: early rapid plasma decline when little drug eliminated and early effect changes. | R&T p.614 | Yes | MATCH |
| Tissue perfusion, membrane permeability, and partitioning determine distribution time. | R&T p.613–615 | Partial | OPTIONAL — M1 L4 mentions perfusion but not all determinants. |
| A two-compartment model is defined by data and degrees of freedom; number of exponential terms equals number of pools needed. | R&T p.618 | Yes | MATCH |
| Compartmental model chosen is often not unique; plasma data alone cannot distinguish several structures. | R&T p.618–619; G&W Fig.2.46 | Yes | MATCH |
| Rate constants rarely have direct physical/physiologic meaning. | R&T p.619 | Partial | SHOULD_FIX — draft says k’s are unphysical but should be tied to author warning. |
| Elimination occurs at all times, not just terminal phase; CL is Dose/AUC. | R&T p.620 | Yes | MATCH |
| Terminal phase is often called elimination phase, but this is not always true; fractional area determines dominant elimination phase. | G&W p.63; R&T p.622 | Yes | MATCH |
| V1, V, and Vss are distinct; Vss is the closest estimate of purely distributional volume. | R&T p.617, p.621–630 | Yes | MATCH |
| Vss lies between V1 and V; V/Vss difference grows when much drug is eliminated before distribution equilibrium. | R&T p.629–630 | Yes | MATCH |
| For most drugs f2>0.8 and terminal half-life primarily controls plateau, but not for nicardipine/gentamicin-like cases. | R&T p.632 | Partial | MUST_FIX — draft says “항상 빗나간다,” which conflicts with this nuance. |
| Plasma plateau and tissue plateau may be controlled by different time scales. | R&T p.631–634 Fig.19-11/12 | Yes | MATCH |
| Vss applicability during multiple dosing depends on departure from true steady state; neither V nor Vss may be useful in gentamicin-like intervals. | R&T p.638–639 Fig.19-16 | Partial | SHOULD_FIX |
| In renal impairment for gentamicin/tobramycin-like drugs, terminal half-life may be virtually unaffected until renal function is very low; initial phase is altered. | R&T p.639–641 Fig.19-17/18 | Yes | MATCH |
| Terminal half-life, or any half-life, ceases to have simple application under distribution kinetics; all model parameters matter. | R&T p.641 | Yes | MATCH |
| G&W: pharmacokinetics has moved away from micro-constant elimination parameterization; clearance is preferred. | G&W p.67 | Partial | SHOULD_FIX — draft has physiological parameterization but overextends to NONMEM/regulatory without source tag. |
| G&W PK7: model choice should use residuals, AIC/F-test, precision/correlation; simplest adequate model rule. | G&W p.508–512 | Partial | SHOULD_FIX |
| G&W PK8: Takada lowest WRSS, ODE lowest condition number; fits similar but precision differs. | G&W p.516 | Yes | MATCH, except wrong range in curation. |
| G&W PK8: if initial phase is hardly discernible but cannot be excluded, NCA may be proposed. | G&W p.517 | No | SHOULD_FIX |

---

## T4: Priority Summary

| # | Item | Priority | Rationale |
|---|---|---|---|
| 1 | `condition number 29.69–4,104` under PK8 | MUST_FIX | 4,104 is PK7 tri-exponential condition number, not PK8. PK8 maximum is 3,186. |
| 2 | `200배 진폭` | MUST_FIX | Correct ratio is ~107× using PK8 Table 8.1. |
| 3 | Aspirin “용량 계산 30% 과소평가” | MUST_FIX | Source says one-compartment CL is overestimate. Maintenance dose risk direction is overestimation/overdosing; fixed-dose exposure is underpredicted. |
| 4 | Formal `Vss` table with ellipsis formula | MUST_FIX | Non-auditable expression; replace with source formulas. |
| 5 | `항상 빗나간다` terminal half-life statement | MUST_FIX | R&T says many drugs have f2>0.8; terminal half-life often works but loses simple generality. |
| 6 | “NDA Deficiency Letter 직접 사유/발화점” | MUST_FIX | Not in source. Convert to `[실무 추론] regulatory review risk`. |
| 7 | NONMEM/FDA/PIPET claims used as source-like statements | MUST_FIX | Not in supplied PDFs. Keep only as external implementation notes with explicit tag, or remove. |
| 8 | `2-compartment has 4 DOF: Vc,Vt,k10,k12(or k21)` | MUST_FIX | Use source parameter sets: macro, micro, physiological. |
| 9 | G&W PK8 NCA fallback omitted | SHOULD_FIX | Important author conclusion for sparse/indistinct initial phase. |
| 10 | R&T Fig.19-16 volume-term applicability under multiple dosing underdeveloped | SHOULD_FIX | Important bridge between Vss/Vβ concept and dosing regimen interpretation. |
| 11 | PK7 model discrimination message underdeveloped | SHOULD_FIX | Important for preventing overfit: residuals/precision/AIC/F-test/simple adequate model. |
| 12 | Eigenvalue explanation | OPTIONAL | Correct but not explicitly source; keep with `[수학적 해석]`. |
| 13 | catenary=enterohepatic recirculation example | OPTIONAL/REJECT | Not in source. Delete if strict source fidelity; keep only if clearly external analogy. |
| 14 | Thiopental numeric details omitted | OPTIONAL | Can enrich M1 but not required. |
| 15 | PD response sections omitted | REJECT for Step 1 core | Source range includes them, but current session scope excludes PD; do not absorb into MUST cards. Document as out-of-scope. |

---

## Patch Memo Independent Audit

| Patch Memo Item | Audit Classification | PDF-based Decision |
|---|---|---|
| Condition number max should be 3,186 not 4,104 | ERROR confirmed | Adopt. 4,104 belongs to PK7 tri-exponential table. |
| Aspirin “30% 과소평가” direction risky | ERROR confirmed | Adopt. Correct direction. |
| NDA Deficiency Letter wording is not textbook source | NOT_IN_SOURCE confirmed | Adopt. Convert to 실무 추론. |
| Eigenvalue explanation useful but not textbook source | NOT_IN_SOURCE but mathematically valid | Adopt tag separation, not deletion. |
| NONMEM ADVAN3/4/11/12 should remain future/implementation link | NOT_IN_SOURCE confirmed | Adopt. |
| “항상 빗나간다” should be softened | ERROR/OVERSTATEMENT confirmed | Adopt. |

---

## T5: Coverage Audit

### T5-A. Section Headings

| PDF Element | Type | PDF Location | Step 1 Status | Omission Verdict | Required Action |
|---|---|---|---|---|---|
| 2.4 Multi-Compartment Models | Heading | G&W p.57 | INCLUDED_AS_MUST | — | 유지 |
| 2.4.1 Catenary and mammillary models | Heading | G&W p.57–58 | INCLUDED_AS_CONTEXT | — | 유지 |
| 2.4.2 Intravenous bolus administration | Heading | G&W p.59–66 | INCLUDED_AS_MUST | — | 유지 |
| 2.4.3 Reparameterization of the two-compartment model | Heading | G&W p.66–71 | INCLUDED_AS_MUST | — | 유지 |
| 2.4.4 Constant rate infusion | Heading | G&W p.72–74 | INCLUDED_AS_CONTEXT | OMITTED_JUSTIFIABLE | 핵심식 Eq.2:168만 M5와 연결 유지 |
| 2.4.5 Extravascular administration | Heading | G&W p.74–75 | INCLUDED_AS_CONTEXT | OMITTED_JUSTIFIABLE | 상세 도출 제외 가능 |
| 2.4.6 Plasma and urine data | Heading | G&W p.76 | INCLUDED_AS_CONTEXT | OMITTED_JUSTIFIABLE | 상세 도출 제외 가능 |
| 2.5/2.5.1 Clearance Concepts/Derivation of clearance | Heading | G&W p.77 | OMITTED_JUSTIFIABLE | Scope edge | CL definition already covered via R&T/G&W |
| PK7 Two-compartment intravenous bolus dosing | Case Study | G&W p.505–512 | INCLUDED_AS_CONTEXT only | MISSING_BRIDGE | Add 1–2 sentence on model discrimination and simplest adequate model. |
| PK8 Two-compartment distribution models | Case Study | G&W p.513–517 | INCLUDED_AS_MUST | — | Correct condition number. |
| R&T Objectives | Chapter opener | R&T p.613 | INCLUDED_AS_MUST/CONTEXT | — | 유지 |
| Evidence of Distribution Kinetics | Heading | R&T p.614–615 | INCLUDED_AS_MUST | — | 유지 |
| Intravenous Bolus Dose → Presentation → Sum of Exponential Terms | Heading | R&T p.615–617 | INCLUDED_AS_MUST | — | 유지 |
| A Compartmental Model | Heading | R&T p.617–619 | INCLUDED_AS_MUST | — | 유지 |
| Pharmacokinetic Parameters: Clearance/Volume/Distribution Kinetics and Elimination | Heading | R&T p.620–623 | INCLUDED_AS_MUST | — | 유지 |
| A Mathematical Aid | Heading | R&T p.623 | INCLUDED_AS_MUST | — | 유지 |
| Constant-Rate Infusion: Short-/Long-Term | Heading | R&T p.624–628 | INCLUDED_AS_CONTEXT | OMITTED_JUSTIFIABLE | M5 context enough. |
| Distribution Volumes / Events at Plateau | Heading | R&T p.628–630 | INCLUDED_AS_MUST | — | 유지 |
| Time to Reach Plateau / Events in Plasma / Peripheral Tissue | Heading | R&T p.631–634 | INCLUDED_AS_MUST | — | 유지 |
| Bolus plus Infusion | Heading | R&T p.634–635 | INCLUDED_AS_CONTEXT | — | 유지 |
| Multiple Dosing and Regimen Design | Heading | R&T p.635–639 | PARTIAL | MISSING_BRIDGE | Add Fig.19-16 volume term applicability. |
| Altered Clearance | Heading | R&T p.639–641 | INCLUDED_AS_MUST | — | 유지 |
| Drug Redistribution | Heading | R&T p.641–643 | OMITTED_JUSTIFIABLE | Out of current core | Keep excluded unless clinical PK session. |
| Pharmacodynamic Considerations and Response sections | Heading group | R&T p.643–656 | OMITTED_JUSTIFIABLE | Out of current core | Do not absorb into MUST cards. |

### T5-B. Named/Numbered Formula Coverage

| PDF Element | Type | PDF Location | Step 1 Status | Omission Verdict | Required Action |
|---|---|---|---|---|---|
| G&W Eq.2:117–2:134 | Bi-exponential, half-life, macro/micro, AUC/fractional area | G&W p.59–63 | INCLUDED_AS_MUST | — | 유지 |
| G&W Eq.2:135–2:145 | CL, AUMC, MRT, effective t1/2, Vss, model variants | G&W p.63–65 | INCLUDED_AS_MUST/PARTIAL | MISSING_BRIDGE for Eq.2:145 | Keep Eq.2:145 only as structural non-identifiability context. |
| G&W Eq.2:146–2:153 | CL reparameterized, Takada, Colburn | G&W p.66–67 | INCLUDED_AS_MUST | — | 유지 |
| G&W Eq.2:154–2:165 | Cld initial estimates, ODE, SS equality, MRT/MTT/MST | G&W p.69–71 | PARTIAL | OMITTED_JUSTIFIABLE except partition caveat | Add one caveat from Fig.2.50/SS equality. |
| G&W Eq.2:166–2:168 | Infusion intercepts and plateau time | G&W p.72–73 | INCLUDED_AS_CONTEXT | — | 유지. |
| G&W Eq.2:169–2:174 | Extravascular first-order input | G&W p.75 | INCLUDED_AS_CONTEXT | — | 유지. |
| G&W Eq.2:175–2:180 | Plasma/urine/CL derivation | G&W p.76–77 | INCLUDED_AS_CONTEXT/PARTIAL | OMITTED_JUSTIFIABLE | 상세 제외 가능. |
| G&W PK7 Eq.7:1–7:11 | NCA, curve stripping, mono/bi/tri, AIC/F-test | G&W p.506–511 | PARTIAL | MISSING_BRIDGE | Add model-discrimination context. |
| G&W PK8 Eq.8:1–8:10 | Five parameterizations + ODE | G&W p.514–515 | INCLUDED_AS_MUST | — | 유지. |
| R&T Eq.19-1–19-13 | Sum exponentials, V1, ODE, CL/AUC, V, f2, mathematical aid | R&T p.615–623 | INCLUDED_AS_MUST | — | 유지. |
| R&T Eq.19-14–19-25 | Infusion/Vss/MRT formulas | R&T p.627–630 | PARTIAL | MISSING_BRIDGE | Eq.19-23/25 Vss included; details can remain context. |
| R&T Eq.19-26–19-30 | Plateau, tissue events, gentamicin tissue amount | R&T p.633–641 | INCLUDED_AS_MUST/PARTIAL | — | Maintain Eq.19-30 if renal/tissue accumulation discussed. |
| R&T later PD equations/examples | R&T p.643–656 | OMITTED_JUSTIFIABLE | Out of core | Do not include. |

### T5-C. Figures/Tables Coverage Summary

| PDF Element | Type | PDF Location | Step 1 Status | Omission Verdict | Required Action |
|---|---|---|---|---|---|
| G&W Fig.2.39–2.44 | Figures | G&W p.57–61 | INCLUDED_AS_MUST/CONTEXT | — | Fig.2.43 essential. |
| G&W Table 2.4/Fig.2.45 | Table/Figure | G&W p.63 | INCLUDED_AS_MUST | — | View instruction recommended. |
| G&W Fig.2.46/Table 2.5 | Figure/Table | G&W p.65–66 | Fig included; Table omitted | Table omission justifiable | Fig.2.46 essential. |
| G&W Fig.2.47–2.50/Table 2.6 | Figures/Table | G&W p.67–71 | INCLUDED_AS_MUST/PARTIAL | — | Add Fig.2.50 caveat optional. |
| G&W Fig.2.51–2.57 | Figures | G&W p.72–77 | CONTEXT/OMITTED | Mostly justifiable | Keep as route/input variants. |
| G&W Fig.7.1/Table 7.1/Fig.7.2/F table | Case figures/tables | G&W p.505–511 | PARTIAL | MISSING_BRIDGE | Add PK7 context. |
| G&W Fig.8.1/Table 8.1 | Case figure/table | G&W p.514–516 | INCLUDED_AS_MUST | — | Fix range. |
| R&T Fig.19-1–19-4/Table 19-1 | Core figures/table | R&T p.614–621 | INCLUDED_AS_MUST | — | 유지. |
| R&T Fig.19-5–19-8 | Input/infusion figures | R&T p.624–627 | INCLUDED_AS_CONTEXT/PARTIAL | Justifiable | Maintain context. |
| R&T Fig.19-9–19-16 | V terms/plateau/multiple dosing | R&T p.628–639 | INCLUDED_AS_MUST/PARTIAL | Fig.19-16 missing bridge | Add Fig.19-16 one-sentence rule. |
| R&T Fig.19-17–19-18 | Altered clearance | R&T p.640 | INCLUDED_AS_MUST/PARTIAL | — | 유지. |
| R&T Fig.19-19–19-32/Tables 19-2–19-5 | Redistribution/PD/response/examples | R&T p.642–656 | OMITTED_JUSTIFIABLE | Out of Step 1 scope | Document exclusion. |

---

## T6: Figure Inventory & Learning Value Audit

**Inspection note:** pages were rendered and visually inspected as page images/contact sheets; key source pages with dense formulas/figures were additionally inspected individually. Value ratings are conservative.

### T6-A. G&W Figure/Table Inventory

| Figure/Table | Page | Teaches | Value | View Instruction? | Redraw/New Schematic? | Inspection Method | Rationale |
|---|---:|---|---|---|---|---|---|
| Fig.2.39 | G&W 57 | Mono-, bi-, and multi-exponential decline comparison | USEFUL | YES | YES | VISUAL_INSPECTED | 세션 시작 intuition용. |
| Fig.2.40 | G&W 58 | Catenary chain compartment structure | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Context only. |
| Fig.2.41 | G&W 58 | Mammillary central-peripheral structure | USEFUL | YES | YES | VISUAL_INSPECTED | 2-compartment mainstream 구조 이해에 도움. |
| Fig.2.42 | G&W 59 | Central vs peripheral vs urine time profiles after bolus | USEFUL | YES | YES | VISUAL_INSPECTED | Plasma만 보면 tissue/urine profiles를 알 수 없다는 bridge. |
| Fig.2.43 | G&W 60 | Residual method and bi-exponential decomposition | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M1 이해의 핵심 figure. |
| Fig.2.44 | G&W 61 | Physiological vs micro-constant parameterization | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M2 좌표계 변환 핵심. |
| Table 2.4 | G&W 63 | Initial/terminal phase contribution to AUC and effective half-life | ESSENTIAL | YES | YES | VISUAL_INSPECTED | terminal phase≠elimination phase 메시지의 수치 근거. |
| Fig.2.45 | G&W 63 | Which phase is elimination phase depending on fractional AUC | ESSENTIAL | YES | YES | VISUAL_INSPECTED | fractional area intuition 강화. |
| Fig.2.46 | G&W 65 | Three non-identifiable 2-compartment mammillary variants | ESSENTIAL | YES | YES | VISUAL_INSPECTED | structural non-identifiability 핵심. |
| Table 2.5 | G&W 66 | SHAM/NCA summary variables | USEFUL | NO | NO | VISUAL_INSPECTED | 세션 core보다는 NCA reference. |
| Fig.2.47 | G&W 67 | Volume of distribution as function of time; Vc→Vss/Vz | USEFUL | YES | YES | VISUAL_INSPECTED | Vss/Vz intuition 보조. |
| Fig.2.48 | G&W 68 | Physiological two-compartment model | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M2/M4 ODE parameterization anchor. |
| Fig.2.49 | G&W 68 | Early vs terminal flux direction, redistribution | USEFUL | YES | YES | VISUAL_INSPECTED | redistribution concept visual. |
| Fig.2.50 | G&W 70 | Central/peripheral concentrations approach equilibrium | USEFUL | YES | YES | VISUAL_INSPECTED | partitioning caveat bridge. |
| Table 2.6 | G&W 71 | Five parameterization families | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M4 map의 source table. |
| Fig.2.51 | G&W 72 | Bolus vs infusion initial-phase reduction | USEFUL | NO | YES | VISUAL_INSPECTED | M5 route/input context. |
| Fig.2.52 | G&W 73 | Intercepts after infusion and multi-exponential post-infusion decline | USEFUL | NO | YES | VISUAL_INSPECTED | detailed derivation, not core. |
| Fig.2.53 | G&W 73 | Three-compartment model after infusion | SKIPPABLE | NO | NO | VISUAL_INSPECTED | follow-up topic. |
| Fig.2.54 | G&W 74 | Bolus data, one- vs two-compartment fits, MRT | USEFUL | NO | NO | VISUAL_INSPECTED | effective half-life/MRT support. |
| Fig.2.55 | G&W 74 | Oral dosing concentration-time data | USEFUL | NO | NO | VISUAL_INSPECTED | input-function variant. |
| Fig.2.56 | G&W 77 | Amount remaining to excrete/rate vs time | SKIPPABLE | NO | NO | VISUAL_INSPECTED | urine-data extension. |
| Fig.2.57 | G&W 77 | Elimination rate vs concentration slope=CL | USEFUL | NO | NO | VISUAL_INSPECTED | CL concept but outside core. |
| Fig.7.1 | G&W 505 | Mono/bi/tri-exponential model fit comparison | USEFUL | YES | YES | VISUAL_INSPECTED | PK7 model discrimination. |
| Table 7.1 parameter estimates | G&W 508 | Mono/bi/tri precision, condition number, WRSS, AIC | USEFUL | YES | YES | VISUAL_INSPECTED | 4,104 source; avoid PK8 confusion. |
| Fig.7.2 | G&W 510 | Bi vs tri residual patterns | USEFUL | NO | NO | VISUAL_INSPECTED | model-discrimination context. |
| Table 7.1 F table | G&W 511 | F-test threshold lookup | SKIPPABLE | NO | NO | VISUAL_INSPECTED | method detail. |
| Fig.8.1 | G&W 514 | Compound X observed/predicted, model diagram, volume over time | ESSENTIAL | YES | YES | VISUAL_INSPECTED | PK8 core visual. |
| Table 8.1 | G&W 516 | WRSS/condition number across 5 parameterizations | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M4 central quantitative anchor. |

### T6-B. R&T Figure/Table Inventory

| Figure/Table | Page | Teaches | Value | View Instruction? | Redraw/New Schematic? | Inspection Method | Rationale |
|---|---:|---|---|---|---|---|---|
| Fig.19-1 | R&T 614 | Thiopental tissue/plasma distribution kinetics | ESSENTIAL | YES | YES | VISUAL_INSPECTED | direct evidence of distribution kinetics. |
| Fig.19-2 | R&T 616 | Aspirin bi-exponential curve stripping | ESSENTIAL | YES | YES | VISUAL_INSPECTED | aspirin residual method source. |
| Fig.19-3 | R&T 617 | Two-compartment model with k12/k21/k10 | ESSENTIAL | YES | YES | VISUAL_INSPECTED | compartment model source anchor. |
| Table 19-1 | R&T 619 | Equivalent relationships between sum exponentials and 2-comp model | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M2/M3 source table. |
| Fig.19-4 | R&T 621 | Effective volume A/C increases from V1 to V | ESSENTIAL | YES | YES | VISUAL_INSPECTED | V1/V/Vss intuition. |
| Fig.19-5 | R&T 624 | Digoxin oral vs IV distribution nose | USEFUL | NO | YES | VISUAL_INSPECTED | input/absorption bridge. |
| Fig.19-6 | R&T 625 | Absorption speed affects digoxin distribution nose | USEFUL | NO | YES | VISUAL_INSPECTED | extravascular context. |
| Fig.19-7 | R&T 625 | Short infusion lowers Cmax for midazolam-like kinetics | USEFUL | NO | YES | VISUAL_INSPECTED | dosing safety context. |
| Fig.19-8 | R&T 626 | Stopping infusion at different times during approach to plateau | USEFUL | NO | YES | VISUAL_INSPECTED | long-infusion context. |
| Fig.19-9 | R&T 628 | Elimination affects V and Vss distinction | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M3 central figure. |
| Fig.19-10 | R&T 631 | Nicardipine reaches 50% plateau much earlier than terminal t1/2 | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M5 central example. |
| Fig.19-11 | R&T 632 | f2 controls plasma approach to plateau | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M5 equation-to-visual bridge. |
| Fig.19-12 | R&T 634 | Plasma vs slowly equilibrating tissue plateau times | ESSENTIAL | YES | YES | VISUAL_INSPECTED | tissue accumulation distinction. |
| Fig.19-13 | R&T 635 | Eptifibatide bolus plus infusion and supplemental bolus | USEFUL | YES | YES | VISUAL_INSPECTED | practical dosing context. |
| Fig.19-14 | R&T 636 | Gentamicin plasma/tissue multiple dosing accumulation | ESSENTIAL | YES | YES | VISUAL_INSPECTED | aminoglycoside terminal half-life trap. |
| Fig.19-15 | R&T 637 | Input-rate effects on multiple-dose fluctuation | USEFUL | NO | YES | VISUAL_INSPECTED | regimen design context. |
| Fig.19-16 | R&T 639 | When V or Vss can estimate amount during dosing interval | ESSENTIAL | YES | YES | VISUAL_INSPECTED | missing bridge for M3/M5. |
| Fig.19-17 | R&T 640 | Tobramycin renal impairment affects first phase more than terminal slope | USEFUL | YES | YES | VISUAL_INSPECTED | altered clearance context. |
| Fig.19-18 | R&T 640 | Simulated renal function effects in gentamicin-like drug | USEFUL | YES | YES | VISUAL_INSPECTED | renal impairment boundary condition. |
| Fig.19-19 | R&T 642 | Lithium postdialysis rebound | USEFUL | NO | NO | VISUAL_INSPECTED | separate redistribution topic. |
| Fig.19-20 | R&T 644 | Duration of effect vs infusion strategy | SKIPPABLE | NO | NO | VISUAL_INSPECTED | PD-focused, out of core. |
| Fig.19-21 | R&T 645 | Response/intensity-distribution relationship | SKIPPABLE | NO | NO | VISUAL_INSPECTED | PD-focused. |
| Fig.19-22 | R&T 646 | Mean concentration/effect during/after infusion | SKIPPABLE | NO | NO | VISUAL_INSPECTED | PD-focused. |
| Fig.19-23 | R&T 647 | Hysteresis/effect compartment relationship | SKIPPABLE | NO | NO | VISUAL_INSPECTED | PD-focused. |
| Fig.19-24 | R&T 648 | Slow target-site distribution and fixed dosing | SKIPPABLE | NO | NO | VISUAL_INSPECTED | PD/regimen topic. |
| Fig.19-25 | R&T 649 | One-compartment simplification for response | SKIPPABLE | NO | NO | VISUAL_INSPECTED | PD-focused. |
| Fig.19-26 | R&T 650 | Repeated dosing when response wears off | SKIPPABLE | NO | NO | VISUAL_INSPECTED | PD-focused. |
| Fig.19-27 | R&T 651 | Thiopental acute tolerance/response | SKIPPABLE | NO | NO | VISUAL_INSPECTED | PD-focused. |
| Table 19-2 | R&T 652 | Irbesartan plasma concentration dataset | SKIPPABLE | NO | NO | VISUAL_INSPECTED | worked problem, outside current 2-comp core. |
| Fig.19-28 | R&T 652 | Irbesartan concentration-time plot | SKIPPABLE | NO | NO | VISUAL_INSPECTED | worked problem. |
| Table 19-3 | R&T 653 | Amrinone slow/fast acetylator concentrations | SKIPPABLE | NO | NO | VISUAL_INSPECTED | worked problem. |
| Fig.19-29 | R&T 654 | Renal impairment effect on drug disposition | USEFUL | NO | NO | VISUAL_INSPECTED | altered clearance reinforcement, but not core. |
| Fig.19-30 | R&T 655 | Propofol/diazepam/midazolam concentration-time comparison | SKIPPABLE | NO | NO | VISUAL_INSPECTED | anesthetic PD context. |
| Fig.19-31 | R&T 655 | Drug concentration fall in label/reference context | SKIPPABLE | NO | NO | VISUAL_INSPECTED | out of core. |
| Table 19-4 | R&T 655 | IV anesthetic disposition parameters | SKIPPABLE | NO | NO | VISUAL_INSPECTED | out of core. |
| Table 19-5 | R&T 656 | Pancuronium effect of successive doses | SKIPPABLE | NO | NO | VISUAL_INSPECTED | PD-focused. |
| Fig.19-32 | R&T 656 | Testosterone concentration with time | SKIPPABLE | NO | NO | VISUAL_INSPECTED | worked problem/out of core. |

---

## Final Audit Decision

### Pass/Fail by task

| Domain | Result |
|---|---|
| Core concept selection | PASS |
| M1 bi-exponential / residual method | PASS with minor source-tag caveats |
| M2 macro/micro/physiological conversion | PASS with one DOF correction and NONMEM source-tag separation |
| M3 V1/Vss/Vβ apex | PASS conceptually, but several regulatory/clinical overclaims need downgrade |
| M4 reparameterization + condition number | FAIL until numeric range fixed |
| M5 terminal half-life trap | PASS after wording softening |
| Example fidelity | PASS with aspirin direction correction |
| Figure inventory readiness | PASS |
| HTML compile readiness | NOT READY |

### Minimum patch set before Phase 4C/HTML

1. Replace all PK8 `29.69–4,104` with `29.69–3,186`.
2. Replace `200배` with `약 107배` or `약 100배 이상`.
3. Correct aspirin direction: terminal-only one-compartment interpretation **overestimates CL**; maintenance-dose risk is overdose/overprediction, not dose underestimation.
4. Remove or tag as `[실무 확장]` all NONMEM/FDA/NDA/PIPET claims not present in the PDFs.
5. Replace “항상 빗나간다” with source-consistent wording.
6. Fix the malformed `Vss` formula row.
7. Add G&W PK8 NCA fallback sentence.
8. Add R&T Fig.19-16 one-sentence rule about when Vss/V are usable during multiple dosing.
9. Add PK7 one-sentence warning: F-test/AIC alone do not prove adequacy; residuals, precision, correlations, and simplest adequate model rule matter.

**Recommended route:**  
`Draft v0 보존 → Patch Memo 확정 → Phase 4A official patch → Phase 4C figure/view instruction integration → HTML compile`.


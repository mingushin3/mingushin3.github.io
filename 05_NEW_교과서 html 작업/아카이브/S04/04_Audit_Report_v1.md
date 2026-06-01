# 04_Audit Report v1 — Source Fidelity Audit

**업무 형태**: 파일 분석 · PDF 대조 감사 · 웹 검색 OFF  
**대상 Draft**: `04_step1_draft_v0(1).md`  
**Source PDFs**:  
- **G** = Gabrielsson & Weiner, *Pharmacokinetic and Pharmacodynamic Data Analysis*, 5e: §2.3, §2.5, PK5
- **T5** = Rowland & Tozer, *Clinical Pharmacokinetics and Pharmacodynamics*, 5e: Ch.5 Elimination
- **T20** = Rowland & Tozer, Ch.20 Metabolites and Drug Response
- **TD/TE** = Rowland & Tozer, App.D Plasma-to-Blood Concentration Ratio / App.E Well-Stirred Model of Hepatic Clearance
- **Patch Memo** = `S04_phase1_patch memo.md` — 자동 채택하지 않고 attention guide로만 독립 검증

**감사 범위**: Draft v0의 사실 주장, 수식, 수치, 예시, 그림·표 반영 여부를 PDF 원문과 대조. 문장 개선·재작성·교육적 보강은 수행하지 않음.

**핵심 판정**: `조건부 PASS — Source Fidelity Patch 필요`. Draft v0는 원문 범위 포착력은 높으나, 일부 수식 조건·AUC ratio 해석·임상 예시 dose·실무 확장 claim에서 PDF 근거 초과 또는 오류가 있어 HTML 전환 전 수정이 필요함.

---

## T1: Equation/Numerical Audit

| Item | Draft v0 Expression | PDF Source | Classification | Correction |
|---|---|---|---|---|
| M1 clearance definition | `dX/dt = Cl · C`; `V·dC/dt = -Cl·C` | G Eq 2:83; T5 Eq 5-1 | MATCH | 없음 |
| M1 AUC clearance | `CL = Dose/AUC`; `CL/F = Dpo/AUCpo` | G Eq 2:86; T5 Eq 5-2/5-3 | MATCH | 없음 |
| M1 blood/plasma relation | `CL = CLb · (Cb/C)` 또는 `CLb = CL · (C/Cb)` 취지 | T5 Eq 5-4, 5-5; TD Eq D-6/D-7 | MATCH | blood clearance 해석은 blood concentration 기준임을 유지 |
| M1 unbound clearance | `CL = fu · CLu` | T5 Eq 5-8 | MATCH | 없음 |
| C1 GFR | `GFR 110–130 mL·min⁻¹` | G §2.3.1 | MATCH | 없음 |
| C1 GFR Tozer anchor | `GFR ≈ 120 mL/min` | T5 objective/renal physiology section | MATCH | 없음 |
| C1 filtered water/urine output | `~180 L/day filtered`, `1–2 L/day urine`, `>95% reabsorbed` | G §2.3.1 | MATCH | 없음 |
| C1 urine pH | `pH 4.5–8` | G §2.3.1 | MATCH | 없음 |
| M2 renal excretion rate | `dXu/dt = CLR · C` | G Eq 2:87 | MATCH | 없음 |
| M2 cumulative urine amount | `Xu,0–∞ = CLR · AUC` | G Eq 2:88 | MATCH | 없음 |
| M2 interval renal clearance | `CLR = Xu(t1–t2)/AUC(t1–t2)` | G Eq 2:89 | MATCH | 없음 |
| M2 fraction excreted | `fe = ku/(ku+km)`; `ku=K·fe`, `km=K·fm` | G Fig 2.33 context | MATCH | 없음 |
| M2 `fe = CLR/CL` | `fe = CLR/(CLR+CLm)=CLR/CL` | G one-compartment partial urinary excretion model; T5 clearance additivity | MATCH | 없음 |
| M2 renal filtration | `CLf = fu · GFR` | T5 renal clearance section Eq 5-18/5-19 context | MATCH | 없음 |
| M2 renal composite | `Rate excretion = (1-FR)(Filtration + Secretion)`; `CLR=(1-FR)(CLf+CLS)` | T5 Eq 5-20/5-21 | MATCH | 없음 |
| M2 bioavailability from urine | `F = AUCpo·Div/(AUCiv·Dpo) = CLiv/CLpo` 취지 | G Eq 2:115 | MATCH | 없음 |
| M2 simultaneous regression equations | `C = Div/V·exp(-CL/V·t)`; `Xu = fe·Div·(1-exp(-CL/V·t))` | G Eq 2:99–2:101 | MATCH | 없음 |
| M2 statement on simultaneous fit robustness | simultaneous plasma+urine regression avoids ARE total-excreted dependency and excretion-rate midpoint/bladder-emptying weakness | G §2.3.4 + PK5 discussion | MATCH | 없음 |
| M2 fe failure threshold | `fe < 0.1`일 때 urinary data 기반 F/CL 추정 취약 | G §2.3.4 | MATCH | 없음 |
| M3 ARE plot | `ln[Xu(0–∞)-Xu] = ln Xu(0–∞) - Kt` | G Eq 2:98 / Fig 2.35 | MATCH | 없음 |
| M3 excretion rate plot | `ln(dXu/dt)=ln(ClR·Div/V)-K·t` | G Eq 2:92 / Fig 2.35 | MATCH | 없음 |
| M3 ARE/rate plot slope | both slopes estimate `K` | G Fig 2.35 | MATCH | 없음 |
| M3 excretion-rate limitation | short half-life relative to collection interval; incomplete bladder emptying | G §2.3.3 | MATCH | 없음 |
| M3 ARE limitation | requires accurate `Xu,0–∞`; cumulative assay/collection errors bias | G §2.3.3 | MATCH | 없음 |
| M3 PK16 half-life | Draft references urinary-derived half-life around `6–6.3 h` | G Fig 2.36/Table 2.3 | RESTORED | [확인 필요] figure/table visual 기반 anchor로 보이나, 최종본에서는 exact source label 또는 range로 표시 권장 |
| M3 methamphetamine urine pH recovery | `acidic urine 70–80%`, `alkaline urine 1–2%` | T5 renal reabsorption / Fig 5-16 context | MATCH | 없음 |
| M4 well-stirred hepatic clearance | `CLH,b = QH · fub·CLint / (QH + fub·CLint)` | G Eq 2:188–2:195; T5 Eq 5-14; TE Eq E-8 | MATCH | 없음 |
| M4 extraction ratio | `EH = CLH,b/QH = fub·CLint/(QH+fub·CLint)` | G/T5 well-stirred derivation | MATCH | 없음 |
| M4 hepatic blood flow | `QH ≈ 1.35 L/min` | T5 reference physiology values | MATCH | 없음 |
| M5 high extraction limit | `fub·CLint >> QH` → `CLH,b ≈ QH` | T5 hepatic clearance | MATCH | 없음 |
| M5 low extraction limit | `fub·CLint << QH` → `CLH,b ≈ fub·CLint` | T5 hepatic clearance | MATCH | 없음 |
| M5 extraction ratio classification | `E > 0.7 high`, `E < 0.3 low`, intermediate between | T5 extraction ratio section | MATCH | 없음 |
| M5 propranolol / lidocaine / verapamil high extraction classification | high extraction examples | T5 examples/tables | MATCH | 없음 |
| M5 tolbutamide / phenytoin / diazepam low extraction classification | low extraction examples | T5 examples/tables | MATCH | 없음 |
| M6 route × extraction × fu quadrant | IV vs oral and high vs low extraction effects of fu | G §2.5.3; T5 integration examples | MATCH | 없음 |
| M6 phenytoin/clofibric acid binding examples | increased `fu` can increase `CL`, reduce total concentration while unbound exposure may remain relevant | T5 integration cases | MATCH | 없음 |
| M7 IVIVE single-point warning | single-point in vitro `CLint` extrapolation can be misleading | G §2.5.4 | MATCH | 없음 |
| M7 `MMP` warning | mean of ratios vs ratio of means / poor handling of variability | G §2.5.4 context | MATCH | 없음 |
| M7 condensation warning | excessive data condensation can hide information | G §2.5.4 | MATCH | 없음 |
| M8 four hepatic models | Well-stirred / Parallel tube / Distributed / Dispersion | G Table 2.9 | RESTORED | Table 2.9 수식은 source fidelity risk가 높은 항목. HTML 전 최종 수식 1:1 대조 필요 |
| M8 distributed/dispersion equations | Draft includes detailed formula variants | G Table 2.9 | RESTORED | [확인 필요] 지수항·무차원수 표기 오류 가능성이 높아 MUST_FIX로 재검산 필요 |
| M9 PK5 dose | `250 mg i.v.` | G PK5 problem specification | MATCH | 없음 |
| M9 PK5 initial V/CL | `V ≈ 7 L`, `CL ≈ 2 L/h`, `fe ≈ 0.3` | G PK5 initial estimates | MATCH | 없음 |
| M9 PK5 final CL/fe/CLR | `CL ≈ 1.2 L/h`, `fe ≈ 0.35`, `CLR ≈ 0.42 L/h` | G PK5 results | MATCH | 없음 |
| M9 PK5 residual CV | plasma CV `2.84%`, urine CV `8.96%` | G PK5 output | MATCH | 없음 |
| M9 PK5 parameter CV | parameter CV `<5%` | G PK5 output | MATCH | 없음 |
| M9 integrated vs ODE equivalence | integrated solution and ODE model give essentially same fitted result | G PK5 Eq 5:1–5:4/Fig 5.3 | MATCH | 없음 |
| M10 App.D mass balance | `Cb·VB = C·Vp + CBC·VBC` | TD Eq D-1 | MATCH | 없음 |
| M10 cell partition | `CBC = KPBC·fu·C` | TD Eq D-2 | MATCH | 없음 |
| M10 hematocrit volumes | `VBC=H·VB`, `Vp=(1-H)VB` | TD Eq D-3/D-4 | MATCH | 없음 |
| M10 plasma-to-blood ratio | `C/Cb = 1/{1+H[fu·KPBC−1]}` | TD Eq D-6 | MATCH | 없음 |
| M10 blood-to-plasma ratio | `Cb/C = 1+H[fu·KPBC−1]` | TD Eq D-7 | MATCH | 없음 |
| M10 KPBC inverse | `KPBC = {H−1+(Cb/C)}/(fu·H)` | TD Eq D-8 | MATCH | 없음 |
| M10 study problem anchor | `C/Cb≈0.425`, `H=0.45`, `fu=0.1` | TD Study Problem 1 | MATCH | 없음 |
| M11 clearance additivity | `CL = CLR + CLH` | T5 Eq 5-9 context | MATCH | 없음 |
| M11 pulmonary exception | pulmonary clearance is not simply additive in the same way because lung is in series with systemic circulation | T5 clearance additivity discussion | MATCH | 없음 |
| M12 biliary clearance | `CLbile = bile flow · Cbile / Cplasma` | T5 Eq 5-16 | MATCH | 없음 |
| M12 bile flow | `0.5–0.8 mL/min` | T5 biliary section | MATCH | 없음 |
| M12 bile-to-plasma ratio | values can be very high; draft uses `up to ~1000` | T5 biliary examples | MATCH | 없음 |
| M12 EHC as distribution component | EHC affects profile/secondary peaks and distribution-like persistence | T5 biliary/EHC section | MATCH | 없음 |
| M13 weak acid/base pH rule | urinary pH alters ionization and passive reabsorption | G §2.3.1; T5 renal reabsorption | MATCH | 없음 |
| M13 urine flow rule | urine flow can alter reabsorption-sensitive renal clearance | T5 Eq 5-22/5-23 context | MATCH | 없음 |
| M14 half-life equation | `t1/2 = 0.693·V/CL` | T5 Eq 5-24/5-25 | MATCH | 없음 |
| M14 “half-life depends on CL and V, not vice versa” | stated as author message | T5 objective + half-life section | MATCH | 없음 |
| M14 CL/V ranges | `CL 0.01–100 L/h`, `V 3–7000 L` | T5 half-life discussion / Fig 5-19 | MATCH | 없음 |
| M15 extended clearance | transporter/permeability-inclusive hepatic clearance expression | T5 Eq 5-35/5-36; TE Model II | MATCH | 없음 |
| M15 passive diffusion reduction condition | Draft states passive diffusion condition with `PS_efflux+PS_pd << CLint` in one reduction statement | T5 Eq 5-36 explanatory text; TE Eq E-14/E-15 | ERROR | Correct condition: when active transport is negligible and passive diffusion is large relative to intrinsic metabolic/biliary clearance, the extended model reduces to well-stirred. Replace `<<` with the source-consistent large-diffusion condition (`PSpd` or effective passive terms `>> CLint`). |
| M15 App.E `ρ` | `ρ = Pin·SA/(Pout·SA+CLint)` | TE Eq E-13 | MATCH | 없음 |
| M15 permeability limit | `ρ→1` when passive diffusion is not limiting; `CLb,H=fub·Pin` when influx permeability is limiting | TE Eq E-14/E-15 | MATCH | 없음 |
| M16 metabolite ODE | `dA(m)/dt = kf·A − k(m)·A(m)` | T20 Eq 20-1 | MATCH | 없음 |
| M16 clearance-form metabolite ODE | `dA(m)/dt = CLf·C − CL(m)·C(m)` | T20 Eq 20-4 | MATCH | 없음 |
| M16 AUC ratio | `AUC(m)/AUC = CLf/CL(m) = fm·CL/CL(m)` | T20 Eq 20-5/20-6 | MATCH | 없음 |
| M16 AUC ratio interpretation | Draft: `AUC(m)/AUC < 1 → CL(m) ≥ CL/fm` 또는 metabolite clearance faster inference | T20 AUC ratio discussion | ERROR | Correct: `AUC(m)/AUC = fm·CL/CL(m)`. If ratio < 1 and `fm` is unknown, `CL(m)/CL` cannot be assessed; only `CL(m) > fm·CL` follows. Do not infer `CL(m) ≥ CL/fm`. |
| M16 tolbutamide IV dose | `1 g i.v. bolus` | T20 Fig 20-3/text | MATCH | 없음 |
| M16 tolbutamide half-life | `t1/2 ≈ 4 h`; hydroxytolbutamide terminal decline parallel | T20 Fig 20-3/text | MATCH | 없음 |
| M16 propranolol IV dose | `3.7 mg i.v.` | T20 Fig 20-4/text | MATCH | 없음 |
| M16 propranolol CL/V/t1/2 | `CL≈1.1 L/min`, `V≈380 L`, `t1/2≈4 h` | T20 Fig 20-4/text | MATCH | 없음 |
| M16 methylprednisolone hemisuccinate | `80 mg i.v.`, ester `t1/2≈0.25 h`, methylprednisolone `t1/2≈2.7 h`; AUCs `2.1` and `3.9 mg·h/L` | T20 Fig 20-2/text | MATCH | 없음 |
| M17 chain example rate constants | `kG=0.05 h⁻¹`, `t1/2≈13.9 h`; A/B/E controlled by sum `0.03+0.2+0.3=0.53 h⁻¹`, `t1/2≈1.31 h` | T20 Fig 20-1/text | MATCH with wording caveat | Draft의 “fastest k” 표현은 오해 소지가 있음. Correct wording: A elimination rate-limits B/E terminal decline. |
| M17 renal impairment shortcut | Draft: Case A에서 parent CL correction으로 metabolite exposure도 자동 조정 가능하다는 취지 | T20 renal insufficiency scenarios | ERROR | Source는 renal impairment에서 metabolite CL change와 active metabolite accumulation을 별도로 판단하도록 함. 이 문장은 삭제하거나 “rate-limiting step and metabolite clearance must be reassessed”로 source-consistent하게 제한. |
| M18 propranolol oral dose | Draft: `propranolol 80 mg oral` | T20 Fig 20-5 | ERROR | Correct source: single `20-mg oral dose` of propranolol. |
| M18 propranolol first-pass fraction | `~21%` of oral dose filters past liver as parent; majority enters body as metabolites | T20 Fig 20-5/text | MATCH | dose만 오류 |
| M18 morphine route/dose | Draft: `10 mg dose-equivalent` framing | T20 Fig 20-7 | ERROR | Correct source: oral `11.7 mg` and i.v. `5 mg` morphine were compared; oral bioavailability ~21%; M6G exposure/amount can be similar because first-pass formation compensates. |
| M18 isoproterenol Table 20-3 | IV: parent 62.2, sulfate 0, glucuronide 13.0, deaminated 24.8%; oral: parent 6.3, sulfate 62.0, glucuronide 5.6, deaminated 1.3% | T20 Table 20-3 | MATCH | 없음 |
| M18 `AUCpo = Dose/(fub·ρ·CLint)` | oral first-principles expression | TE Eq E-19/E-20 | MATCH | 없음 |
| M19 infusion plateau | `Css(m)=fm·Rinf/CL(m)`; example `fm=0.5`, `Rinf=5 mg/h`, `k(m)=0.1 h⁻¹`, `CL(m)=1 L/h`, `V(m)=10 L` → `A(m)ss=25 mg`, `Css(m)=2.5 mg/L` | T20 constant infusion example | MATCH | 없음 |
| M19 time to plateau | 50% in 1 metabolite half-life, 90% in 3.3 metabolite half-lives | T20 constant infusion section | MATCH | 없음 |
| M19 multiple-dose average plateau | `Cav,ss(m)=AUC(m)/τ` | T20 Eq 20-12 | MATCH | 없음 |
| M19 Halazepam regimen | `10 mg q8h for 13 days` | T20 Fig 20-9/text | MATCH | 없음 |
| M19 Halazepam plateau timing | Draft visual estimate `5–10 days` | T20 Fig 20-9 | RESTORED | [확인 필요] 원문 수치문장보다는 figure visual estimate. 수치로 잠그지 말고 “slower accumulation/decline than parent”로 유지 권장 |
| M19 carbamazepine dose range | Draft cites dose escalation range | T20 Fig 20-11 | RESTORED | [확인 필요] figure-derived exact range. 핵심 메시지는 dose-normalized parent falls and metabolite ratio rises. |
| M20 renal impairment example | normal `C=0.27`, `C(m)=0.24`; anuric `C=0.53`, `C(m)=3.2`; active totals `0.51` vs `3.73`; dose ratio `0.14`; metabolite ~13-fold | T20 Table 20-4 / renal insufficiency example | MATCH | 없음 |
| M20 dose-rate recommendation | normal `10 mg/hr`, renal failure `1.4 mg/hr` equivalent activity target | T20 renal insufficiency example | MATCH | 없음 |
| M20 procainamide/NAPA | NAPA accumulates in renal impairment; active metabolite can dominate response/toxicity | T20 Fig 20-14 / study problem | MATCH with numeric caution | `5–6` ratio 등 exact numeric은 figure-derived면 [확인 필요] 태그 권장 |
| M20 clofibric acid | renal impairment and protein binding changes affect unbound clearance/exposure | T20 Fig 20-13 | MATCH with numeric caution | Draft의 `~250→~30 mL/min` 등 수치 anchor는 figure visual 기반이면 RESTORED [확인 필요] 처리 |
| M20 apparent fraction interconversion | AUC-based apparent fraction estimation using separate IV doses | T20 Eq 20-21–20-24 | MATCH | 없음 |
| Non-PDF practice claim | `SLCO1B1*5 frequency`, `2–3x exposure`, `AIMS BioScience standard`, `rhabdomyolysis threshold`, `DDI under-conservative` 등 PDF 밖 실무 claim | Not in supplied PDFs | NOT_IN_SOURCE | PDF fidelity 목적에서는 삭제, 별도 외부근거 태그, 또는 `[실무 추론/외부근거 필요]`로 격하 필요 |
| File/session title | Draft header says `01_step1_draft_v0.md` while session is 04 | Draft metadata, not PDF | ERROR | `04_step1_draft_v0`로 정정 필요 |

**T1 footnote**: 일부 pedagogical simplification은 수식 원문과 완전 동일하지 않아도 원문 개념을 왜곡하지 않으면 MATCH로 처리했다. 단, 수학적 부등호 방향·dose·route·AUC ratio 해석은 simplification이 아니라 source fidelity 오류로 보았다.

---

## T2: Examples & Data Audit

| Item | Draft v0 Status | PDF Location | Classification | Importance | Action |
|---|---|---|---|---|---|
| Aminoglycosides as renal-elimination example | 거의 미반영 | G §2.3.1 p48 | MISSING | LOW | M2 context로 1문장 추가 가능하나 필수 아님 |
| Nephron anatomy: Bowman’s capsule, proximal tubule, loop of Henle, distal tubule, collecting duct | 반영 | G §2.3.1; T5 renal section | INCLUDED_CORRECT | MEDIUM | 없음 |
| Inulin as GFR marker | 부분/미반영 | G §2.3.1 | MISSING | LOW | GFR 설명 보강용으로만 optional |
| Weak acid/base urinary pH | 반영 | G §2.3.1; T5 renal pH | INCLUDED_CORRECT | HIGH | 없음 |
| Table 2.3 urinary excretion dataset | 개념만 반영, full table 미반영 | G Table 2.3 p51 | MISSING | MEDIUM | M3에서 full table은 생략 가능. 단 Fig 2.36 해석 근거로 label 필요 |
| Fig 2.36 ARE/rate plot example | 반영 | G Fig 2.36 p51 | INCLUDED_CORRECT | MEDIUM | 수치 half-life는 [확인 필요] 또는 figure-derived 표시 |
| PK16 bioavailability from urine | 일부 context | G Fig 2.37–2.38 p53–54 | MISSING | LOW | Step 1 핵심은 아니므로 optional |
| Table 2.7 interspecies characteristics | context 처리 | G Table 2.7 p87 | INCLUDED_CORRECT | LOW | 없음 |
| Table 2.8 species in vivo/in vitro ratio | context 처리 | G Table 2.8 p87 | INCLUDED_CORRECT | LOW | 없음 |
| Fig 2.63–2.65 IVIVE single-point/condensation examples | 반영 | G p88–89 | INCLUDED_CORRECT | HIGH | 없음 |
| Table 2.9 four hepatic clearance models | 반영하나 수식 검증 미잠금 | G Table 2.9 p94 | INCLUDED_ERROR | HIGH | Table 2.9 수식·symbols 재검산 후 확정 |
| PK5 plasma+urine case | 반영 | G PK5 p494–499 | INCLUDED_CORRECT | HIGH | 없음 |
| PK5 integrated vs ODE equivalence | 반영 | G PK5 Fig 5.3 | INCLUDED_CORRECT | HIGH | 없음 |
| Fig 5-1 route/mechanism top 200 drugs | context 처리 | T5 Fig 5-1 p120 | INCLUDED_CORRECT | LOW | 없음 |
| Table 5-1 metabolism examples | context 처리 | T5 Table 5-1 p121 | INCLUDED_CORRECT | MEDIUM | Active/inactive metabolite examples may be retained as context |
| CYP abundance/contribution examples | context 처리 | T5 Fig 5-2–5-4 p122–124 | INCLUDED_CORRECT | LOW | Not central; no full expansion needed |
| Tolbutamide low extraction example | 반영 | T5 integration cases and T20 Fig 20-3 | INCLUDED_CORRECT | HIGH | 없음 |
| Phenytoin protein binding/uremia example | 반영 | T5 integration cases | INCLUDED_CORRECT | HIGH | 없음 |
| Clofibric acid nephrotic/renal impairment example | 반영 with numeric caution | T5/T20 Fig 20-13 context | INCLUDED_CORRECT | HIGH | Numeric anchors [확인 필요] 처리 |
| Propranolol high extraction example | 반영 with dose error in T20 oral example | T5 high extraction; T20 Fig 20-5 | INCLUDED_ERROR | HIGH | Oral propranolol dose `80 mg` → `20 mg` correction |
| Rifampin/alfentanil induction example | 반영 여부 불명/부분 | T5 integration figures | MISSING | MEDIUM | If Draft uses induction/DDI general claims, exact figure source should be anchored or removed |
| Ritonavir/fentanyl/itraconazole examples | 부분/미반영 | T5 integration figures | MISSING | MEDIUM | DDI source examples are useful but not mandatory if not central |
| Digoxin/ritonavir transporter example | 부분/미반영 | T5 integration figures | MISSING | MEDIUM | M15 transporter section에 1문장 context 가능 |
| Biliary secretion / EHC examples | 반영 | T5 biliary/EHC | INCLUDED_CORRECT | HIGH | 없음 |
| Methamphetamine urine pH example | 반영 | T5 Fig 5-16 | INCLUDED_CORRECT | HIGH | 없음 |
| Top 200 prescribed drugs elimination mechanism | context only | T5 Fig 5-1 | INCLUDED_CORRECT | LOW | 없음 |
| T20 Table 20-1 therapeutically important metabolites | 반영 | T20 Table 20-1 p658 | INCLUDED_CORRECT | HIGH | 없음 |
| Clopidogrel sequential metabolism | 반영 | T20 p659 | INCLUDED_CORRECT | MEDIUM | 없음 |
| Methylprednisolone hemisuccinate | 반영 | T20 Fig 20-2 p662 | INCLUDED_CORRECT | HIGH | 없음 |
| Tolbutamide/hydroxytolbutamide | 반영 | T20 Fig 20-3 p663 | INCLUDED_CORRECT | HIGH | 없음 |
| Propranolol/naphthoxylactic acid IV | 반영 | T20 Fig 20-4 p665 | INCLUDED_CORRECT | HIGH | 없음 |
| Propranolol oral first-pass | 반영하나 dose 오류 | T20 Fig 20-5 p666 | INCLUDED_ERROR | HIGH | `80 mg oral` → `20 mg oral` |
| Morphine/M6G oral vs IV | 반영하나 route/dose framing 오류 | T20 Fig 20-7 p668 | INCLUDED_ERROR | HIGH | `oral 11.7 mg` and `i.v. 5 mg`; “10 mg dose-equivalent” 삭제/정정 |
| Isoproterenol route-dependent metabolite fractions | 반영 | T20 Table 20-3 p669 | INCLUDED_CORRECT | HIGH | 없음 |
| Halazepam/N-desalkylhalazepam multiple dose | 반영 | T20 Fig 20-9 p672 | INCLUDED_CORRECT | MEDIUM | visual-estimate 수치는 source label 필요 |
| Active metabolite renal failure hypothetical example | 반영 | T20 Fig 20-10/Table 20-4 p674 | INCLUDED_CORRECT | HIGH | 없음 |
| Carbamazepine autoinduction | 반영 | T20 Fig 20-11 p676 | INCLUDED_CORRECT | MEDIUM | exact dose range [확인 필요] |
| Prednisone/prednisolone interconversion | 반영 | T20 Fig 20-12/Table 20-5 p677–678 | INCLUDED_CORRECT | MEDIUM | 없음 |
| Procainamide/NAPA | 반영 | T20 Fig 20-14 p683 | INCLUDED_CORRECT | HIGH | exact numeric ratio는 figure-derived caution |
| App.D Study Problem 1 | 반영 | TD p776 | INCLUDED_CORRECT | LOW | Context 이상 확장하지 않는 것이 적절 |
| App.E Study Problems | 대부분 미반영 | TE p780 | MISSING | LOW | Omitted justifiable; 본 세션 core 아님 |

---

## T3: Author Key Messages

| Message | PDF Location | In Draft v0? | Status |
|---|---|---:|---|
| Clearance is the proportionality factor relating elimination rate to concentration. | G Eq 2:83; T5 Ch.5 opening | Yes | INCLUDED_CORRECT |
| Renal clearance can be estimated by combining urinary excretion and plasma concentration/AUC data. | G Eq 2:87–2:89 | Yes | INCLUDED_CORRECT |
| Urinary excretion rate plot and ARE plot have different assumptions and limitations. | G §2.3.3/Fig 2.35 | Yes | INCLUDED_CORRECT |
| For accurate urinary results, collect urine until urinary concentration returns to negligible levels. | G §2.3.3 | Partial/No | SHOULD_FIX: small but important practical message absent |
| Simultaneous nonlinear regression of plasma and urine data is robust and avoids weaknesses of linearized plots. | G §2.3.4/PK5 | Yes | INCLUDED_CORRECT |
| Clearance can be viewed physiologically by organ, process, and site of measurement; blood concentration is required for extraction ratio. | T5 Ch.5 clearance sections; TD | Yes | INCLUDED_CORRECT |
| Extraction ratio determines whether organ clearance is sensitive to perfusion vs binding/cellular activity. | T5 hepatic clearance objectives/sections | Yes | INCLUDED_CORRECT |
| High-extraction clearance is perfusion-limited; low-extraction clearance is binding/intrinsic-clearance-sensitive. | T5 hepatic clearance | Yes | INCLUDED_CORRECT |
| Half-life and elimination rate constant depend on clearance and volume of distribution, not vice versa. | T5 objective and half-life section | Yes | INCLUDED_CORRECT |
| Biliary secretion and enterohepatic cycling can strongly shape drug disposition profiles. | T5 biliary/EHC | Yes | INCLUDED_CORRECT |
| Renal clearance is governed by glomerular filtration, tubular secretion, tubular reabsorption, urine pH and flow. | T5 renal clearance | Yes | INCLUDED_CORRECT |
| Extended hepatic clearance requires permeability/transporter terms when passive diffusion is not sufficient. | T5 Eq 5-35/5-36; TE Model II | Yes | INCLUDED_WITH_ERROR: one reduction inequality condition must be fixed |
| Metabolites matter for five reasons: action, toxicity, inhibition, induction, displacement. | T20 opening | Partial | SHOULD_FIX: message should appear explicitly; currently metabolite rationale is broader but less source-anchored |
| A metabolite is therapeutically important only if sufficient concentration exists to exert its property. | T20 opening p659 | Partial/No | SHOULD_FIX: important author caveat absent or under-emphasized |
| Metabolite disposition may be formation-rate-limited or metabolite-elimination-rate-limited. | T20 Rate-Limiting Step | Yes | INCLUDED_CORRECT |
| AUC ratio can help infer relative clearance, but inference depends on `fm`. | T20 Eq 20-5/20-6 | Yes | INCLUDED_WITH_ERROR: ratio interpretation must be corrected |
| Hepatic first-pass extraction can make oral parent administration a parent+metabolite input scenario. | T20 Impact of Hepatic Extraction | Yes | INCLUDED_WITH_ERROR: propranolol and morphine route/dose details must be corrected |
| Metabolite accumulation under infusion/multiple dosing depends on the metabolite half-life or the slowest step. | T20 infusion/multiple-dose sections | Yes | INCLUDED_CORRECT |
| Renal impairment dose adjustment cannot rely only on parent renal excretion; active metabolites can accumulate disproportionately. | T20 Renal Insufficiency | Yes | INCLUDED_CORRECT overall, but M17 shortcut conflicts and must be removed |
| Plasma-to-blood ratio depends on hematocrit, plasma protein binding, and blood-cell partitioning. | TD App.D | Yes | INCLUDED_CORRECT |
| App.E independently derives the well-stirred model and shows permeability-limited deviations. | TE App.E | Yes | INCLUDED_CORRECT with M15 inequality correction |

---

## T4: Priority Summary (sorted: MUST_FIX → SHOULD_FIX → OPTIONAL → REJECT)

| # | Item | Priority | Rationale |
|---:|---|---|---|
| 1 | M15 passive diffusion / extended clearance reduction condition uses wrong inequality direction in one statement. | MUST_FIX | 부등호 오류는 permeability-limited vs well-stirred recovery 판단을 반대로 만들 수 있음. |
| 2 | M16 AUC(m)/AUC `<1` interpretation is mathematically wrong. | MUST_FIX | Source states `fm` is needed; Draft inference `CL(m) ≥ CL/fm` is incorrect. |
| 3 | M18 propranolol oral dose is wrong. | MUST_FIX | Source Fig 20-5 is single `20-mg oral dose`, not `80 mg`. |
| 4 | M18 morphine/M6G route-dose framing is wrong. | MUST_FIX | Source compares oral `11.7 mg` and i.v. `5 mg`; “10 mg dose-equivalent” is not source-supported. |
| 5 | M17 renal impairment “Case A parent CL correction automatically corrects metabolite exposure” shortcut. | MUST_FIX | Conflicts with T20 renal impairment message that metabolite CL and rate-limiting step must be separately evaluated. |
| 6 | Table 2.9 four hepatic clearance models formula transcription. | MUST_FIX | Draft correctly identifies the table but detailed formulas are high-risk; Table 2.9 must be checked 1:1 before HTML. |
| 7 | Unsupported external/practice claims not in PDF. | MUST_FIX | `SLCO1B1*5`, exposure fold-change, AIMS standards, toxicity thresholds, regulatory/consulting claims require external source or explicit non-PDF label. |
| 8 | Internal title says `01_step1_draft_v0.md`. | MUST_FIX | Session 04 deliverable metadata mismatch. |
| 9 | T20 metabolite key message “action, toxicity, inhibition, induction, displacement” absent as explicit author message. | SHOULD_FIX | Important opening message; 1 sentence enough. |
| 10 | T20 caveat: metabolite matters only if concentration is sufficient. | SHOULD_FIX | Prevents over-claiming all metabolites as clinically important. |
| 11 | G urinary-data practical message: collect urine until concentration negligible. | SHOULD_FIX | Minor but operationally relevant condition for urinary excretion analysis. |
| 12 | M17 chain example wording “fastest k” may mislead. | SHOULD_FIX | Should say A/drug elimination rate-limits terminal decline of downstream B/E in the example. |
| 13 | M18 “oral effect faster/stronger” phrasing. | SHOULD_FIX | Source supports conditional cases, not universal route rule. |
| 14 | Halazepam plateau timing and carbamazepine dose range as exact values. | SHOULD_FIX | Visual estimates should be tagged [확인 필요] or softened. |
| 15 | T5 integration tables/figures not fully reflected. | SHOULD_FIX | Table 5-9 and related integration figures are useful for route/extraction/fu reasoning. |
| 16 | Figure-view instruction inventory should explicitly mark essential visual checks. | SHOULD_FIX | Phase 4C depends on figure learning-value triage. |
| 17 | Aminoglycoside renal-elimination example. | OPTIONAL | Opening example; not necessary for core conceptual chain. |
| 18 | Inulin GFR marker. | OPTIONAL | Useful physiology note, not critical for Step 1. |
| 19 | Full Table 2.3 urinary dataset. | OPTIONAL | Figure/plot logic is more important than full data table in learner-facing Step 1. |
| 20 | CYP abundance details from Fig 5-2–5-4. | OPTIONAL | Contextual pharmacology, not central to clearance derivations. |
| 21 | App.D/E study problem full numeric solution. | OPTIONAL | Can be appendix note; should not dominate MUST cards. |
| 22 | Add external facts to “strengthen” practice implications without source tags. | REJECT | Violates PDF fidelity audit scope. |
| 23 | Treat morphine/codeine/propranolol examples as a universal oral-route rule. | REJECT | Source examples are conditional and mechanism-specific. |
| 24 | Replace PDF examples with invented examples. | REJECT | Not permitted in source fidelity audit / Phase 1 patch context. |

---

## T5: Coverage Audit

| PDF Element | Type | PDF Location | Step 1 Status | Omission Verdict | Required Action |
|---|---|---|---|---|---|
| 2.3 Plasma and Urine Data | H2 | G p48 | INCLUDED_AS_MUST | — | 없음 |
| 2.3.1 Basic renal physiology | H3 | G p48 | INCLUDED_AS_CONTEXT | — | 없음 |
| Nephron components | Worked physiology | G p48 | INCLUDED_AS_CONTEXT | — | 없음 |
| GFR 110–130 mL/min; 180 L/day filtered; urine 1–2 L/day; pH 4.5–8 | Numerical physiology | G p48 | INCLUDED_AS_CONTEXT | — | 없음 |
| 2.3.2 Derivation of equations | H3 | G p48–50 | INCLUDED_AS_MUST | — | 없음 |
| Eq 2:83 clearance proportionality | Equation | G p49 | INCLUDED_AS_MUST | — | 없음 |
| Eq 2:84–2:86 AUC/dose clearance derivation | Equation | G p49 | INCLUDED_AS_MUST | — | 없음 |
| Eq 2:87 renal excretion rate | Equation | G p49 | INCLUDED_AS_MUST | — | 없음 |
| Eq 2:88 cumulative urinary excretion | Equation | G p50 | INCLUDED_AS_MUST | — | 없음 |
| Eq 2:89 interval urinary excretion/AUC | Equation | G p50 | INCLUDED_AS_MUST | — | 없음 |
| 2.3.3 Analysis of urinary excretion data | H3 | G p50–52 | INCLUDED_AS_MUST | — | 없음 |
| ARE plot | Worked method | G Fig 2.35/2.36 | INCLUDED_AS_MUST | — | 없음 |
| Excretion rate plot | Worked method | G Fig 2.35/2.36 | INCLUDED_AS_MUST | — | 없음 |
| Limitations of ARE/rate plots | Author method caveat | G p51 | INCLUDED_AS_MUST | — | 없음 |
| Collect urine until negligible concentration | Author practical message | G p51 | OMITTED_PROBLEMATIC | MISSING_AUTHOR_MSG | Add 1 sentence under M3 limitations |
| Table 2.3 urinary dataset | Table/data | G p51 | OMITTED_JUSTIFIABLE | — | Full table not needed; cite if using numeric plot anchors |
| 2.3.4 Estimation of bioavailability from urinary data | H3 | G p52–56 | INCLUDED_AS_CONTEXT | — | 없음 |
| Eq 2:99–2:101 simultaneous plasma+urine model | Equation | G p52 | INCLUDED_AS_MUST | — | 없음 |
| Eq 2:102–2:104 extravascular/urine model | Equation | G p53 | INCLUDED_AS_CONTEXT | — | 없음 |
| Eq 2:107–2:108 first-order absorption + urine | Equation | G p54 | INCLUDED_AS_CONTEXT | — | 없음 |
| Eq 2:115 bioavailability from urinary data | Equation | G p56 | INCLUDED_AS_CONTEXT | — | 없음 |
| Fig 2.37–2.38 PK16 urinary bioavailability figures | Figures/case | G p53–54 | OMITTED_JUSTIFIABLE | — | Optional only |
| 2.5 Clearance Concepts | H2 | G p77 | INCLUDED_AS_MUST | — | 없음 |
| 2.5.1 Derivation of clearance | H3 | G p77–79 | INCLUDED_AS_MUST | — | 없음 |
| Eq 2:180 clearance definition | Equation | G p77 | INCLUDED_AS_MUST | — | 없음 |
| 2.5.2 Extraction | H3 | G p79–82 | INCLUDED_AS_MUST | — | 없음 |
| Eq 2:188–2:195 well-stirred derivation | Equations | G p79–82 | INCLUDED_AS_MUST | — | 없음 |
| 2.5.3 Impact of route of administration | H3 | G p83–85 | INCLUDED_AS_MUST | — | 없음 |
| Route × extraction × fu implications | Concept/author message | G p83–85 | INCLUDED_AS_MUST | — | 없음 |
| 2.5.4 In vitro/in vivo comparisons of clearance | H3 | G p85–89 | INCLUDED_AS_MUST | — | 없음 |
| Single-point/MMP/condensation warnings | Author method caveats | G p85–89 | INCLUDED_AS_MUST | — | 없음 |
| Table 2.7 interspecies characteristics | Table | G p87 | INCLUDED_AS_CONTEXT | — | 없음 |
| Table 2.8 ratio of in vivo/in vitro clearances | Table | G p87 | INCLUDED_AS_CONTEXT | — | 없음 |
| 2.5.5 Hepatic clearance models | H3 | G p90–94 | INCLUDED_AS_MUST | — | 없음 |
| Table 2.9 four hepatic models | Table/equation inventory | G p94 | INCLUDED_AS_MUST | OMITTED_PROBLEMATIC | MISSING_CRITICAL: formula-level verification required |
| 2.5.6 Additional readings | H3 | G p94 | OMITTED_JUSTIFIABLE | — | No action |
| PK5 One-compartment intravenous plasma/urine I | Case study | G p494–499 | INCLUDED_AS_MUST | — | 없음 |
| PK5 Objectives/keywords/problem specification | Case setup | G p494 | INCLUDED_AS_MUST | — | 없음 |
| PK5 initial parameter estimates | Case workflow | G p495 | INCLUDED_AS_MUST | — | 없음 |
| PK5 integrated vs ODE fit equivalence | Case conclusion | G p497–499 | INCLUDED_AS_MUST | — | 없음 |
| T5 Objectives | Chapter objectives | T5 p119–120 | INCLUDED_AS_CONTEXT | — | 없음 |
| Processes of Elimination | H2 | T5 p120 | INCLUDED_AS_MUST | — | 없음 |
| Fig 5-1 top 200 route/mechanism | Figure | T5 p120 | INCLUDED_AS_CONTEXT | — | 없음 |
| Table 5-1 biotransformation patterns | Table | T5 p121 | INCLUDED_AS_CONTEXT | — | 없음 |
| CYP figures and primary/secondary pathways | Figures/concepts | T5 p122–124 | INCLUDED_AS_CONTEXT | — | 없음 |
| Clearance in General / physiologic meaning | H2 | T5 p124–128 | INCLUDED_AS_MUST | — | 없음 |
| Blood clearance and extraction ratio | Concept/equations | T5 p124–128 | INCLUDED_AS_MUST | — | 없음 |
| Clearance additivity | Concept/equations | T5 p127–128 | INCLUDED_AS_MUST | — | 없음 |
| Hepatic Clearance: perfusion, binding, hepatocellular activity | H2/H3 | T5 p128–135 | INCLUDED_AS_MUST | — | 없음 |
| Well-stirred model Eq 5-14/5-15 | Equations | T5 p130–131 | INCLUDED_AS_MUST | — | 없음 |
| High vs low extraction memory aid | Author teaching message | T5 p134–135 | INCLUDED_AS_MUST | — | 없음 |
| Permeability / transporter complexity | H3 | T5 p136–138 | INCLUDED_AS_MUST | — | M15 inequality correction required |
| Eq 5-35/5-36 extended clearance | Equations | T5 p136–137 | INCLUDED_AS_MUST | INCLUDED_WITH_ERROR | Correct reduction condition |
| Biliary excretion and EHC | H3 | T5 p137–138 | INCLUDED_AS_MUST | — | 없음 |
| Renal Clearance | H2 | T5 p138–148 | INCLUDED_AS_MUST | — | 없음 |
| Glomerular filtration, secretion, reabsorption | H3 concepts | T5 p138–145 | INCLUDED_AS_MUST | — | 없음 |
| Urine flow and urine pH | H3 concepts | T5 p145–148 | INCLUDED_AS_MUST | — | 없음 |
| Half-life dependence | H2/H3 | T5 p148–150 | INCLUDED_AS_MUST | — | 없음 |
| Integration cases after IV bolus | H2 | T5 p150–163 | INCLUDED_AS_MUST | — | Key figures/tables can be view-instructed; no full expansion needed |
| Study Problems Ch.5 | Chapter exercises | T5 p164–168 | OMITTED_JUSTIFIABLE | — | No action in Step 1 |
| T20 Objectives | Chapter objectives | T20 p657–658 | INCLUDED_AS_CONTEXT | — | 없음 |
| Contribution of Metabolites to Drug Response | H2 | T20 p658–659 | INCLUDED_AS_MUST | OMITTED_PROBLEMATIC | MISSING_AUTHOR_MSG: five-word rationale and concentration caveat explicitness needed |
| Table 20-1 therapeutically important metabolites | Table | T20 p658 | INCLUDED_AS_CONTEXT | — | 없음 |
| Single Dose of Drug | H2 | T20 p659 | INCLUDED_AS_MUST | — | 없음 |
| Rate-Limiting Step | H3 | T20 p659–662 | INCLUDED_AS_MUST | — | M17 wording correction |
| Eq 20-1 | Equation | T20 p659 | INCLUDED_AS_MUST | — | 없음 |
| Sequential metabolism/clopidogrel | Example | T20 p659 | INCLUDED_AS_CONTEXT | — | 없음 |
| Plasma concentration/AUC ratio | H3/equations | T20 p662–665 | INCLUDED_AS_MUST | INCLUDED_WITH_ERROR | Correct AUC ratio inference |
| Methylprednisolone hemisuccinate | Example/figure | T20 Fig 20-2 | INCLUDED_AS_MUST | — | 없음 |
| Tolbutamide/hydroxytolbutamide | Example/figure | T20 Fig 20-3 | INCLUDED_AS_MUST | — | 없음 |
| Propranolol/naphthoxylactic acid | Example/figure | T20 Fig 20-4 | INCLUDED_AS_MUST | — | 없음 |
| Impact of Hepatic Extraction | H3 | T20 p665–669 | INCLUDED_AS_MUST | INCLUDED_WITH_ERROR | Correct propranolol/morphine source details |
| Propranolol oral first pass | Example/figure | T20 Fig 20-5 | INCLUDED_AS_MUST | INCLUDED_WITH_ERROR | Dose correction |
| Morphine/M6G route comparison | Example/figure | T20 Fig 20-7 | INCLUDED_AS_MUST | INCLUDED_WITH_ERROR | Route-dose correction |
| Isoproterenol metabolite distribution | Example/table | T20 Table 20-3 | INCLUDED_AS_CONTEXT | — | 없음 |
| Constant-Rate Drug Infusion | H2 | T20 p669–671 | INCLUDED_AS_MUST | — | 없음 |
| Multiple-Dose Drug Regimen | H2 | T20 p671–673 | INCLUDED_AS_MUST | — | 없음 |
| Renal Insufficiency | H2 | T20 p673–675 | INCLUDED_AS_MUST | — | Remove conflicting M17 shortcut |
| Nonlinear Metabolite Formation or Elimination | H2 | T20 p675–676 | INCLUDED_AS_CONTEXT | — | 없음 |
| Interconversion | H2 | T20 p676–679 | INCLUDED_AS_MUST | — | 없음 |
| Estimation of Metabolite Clearance | H2 | T20 p679–686 | INCLUDED_AS_CONTEXT | — | 없음 |
| T20 Study Problems | Chapter exercises | T20 p680–686 | OMITTED_JUSTIFIABLE | — | No action unless used for worked example |
| App.D Plasma-to-Blood Concentration Ratio | Appendix heading | TD p775–776 | INCLUDED_AS_CONTEXT | — | 없음 |
| Eq D-1–D-8 | Equations | TD p775–776 | INCLUDED_AS_CONTEXT | — | 없음 |
| App.D Study Problem 1 | Study problem | TD p776 | INCLUDED_AS_CONTEXT | — | Keep as appendix note only |
| App.E Well-Stirred Model of Hepatic Clearance | Appendix heading | TE p777–780 | INCLUDED_AS_CONTEXT | — | 없음 |
| App.E Model I Eq E-1–E-8 | Derivation | TE p777–778 | INCLUDED_AS_CONTEXT | — | 없음 |
| App.E Model II Eq E-9–E-15 | Derivation | TE p778–779 | INCLUDED_AS_CONTEXT | INCLUDED_WITH_ERROR | M15 inequality correction |
| App.E Events after oral dose Eq E-19–E-20 | Derivation | TE p779–780 | INCLUDED_AS_CONTEXT | — | 없음 |
| Repeated author message: clearance/extraction must be blood-based for organ extraction | Repeated bridge | T5 + TD | INCLUDED_AS_MUST | — | 없음 |
| Repeated author message: half-life is derived from CL and V | Repeated bridge | T5 objectives + half-life | INCLUDED_AS_MUST | — | 없음 |
| Repeated author message: metabolites require kinetic concentration context, not mere existence | Repeated bridge | T20 opening + examples | OMITTED_PROBLEMATIC | MISSING_AUTHOR_MSG | Add explicit 1 sentence |

---

## T6: Figure Inventory & Learning Value Audit

**Inspection note**: PDF text and rendered page images were available for major figures/tables. Items rated `VISUAL_INSPECTED` were inspected from rendered page/caption context. Items rated `CAPTION_AND_CONTEXT` are retained conservatively where formula/table details were not fully legible from extraction. No textbook figure is to be embedded directly in later phases.

| Figure/Table | Page | Teaches | Value | View Instruction? | Redraw/New Schematic? | Inspection Method | Rationale |
|---|---:|---|---|---|---|---|---|
| G Fig 2.33 | 48 | One-compartment model with partial urinary excretion and `fe/fm/ku/km`. | USEFUL | YES | YES | VISUAL_INSPECTED | M2 구조를 한눈에 잡는 schematic. |
| G Fig 2.34 | 49 | Excretion rate vs plasma concentration; slope = `CLR`. | USEFUL | YES | YES | VISUAL_INSPECTED | `dXu/dt=CLR·C`의 그래프 해석에 유용. |
| G Fig 2.35 | 50 | ARE plot vs excretion-rate plot and their time conventions. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M3의 두 plot 차이는 그림 없이 혼동되기 쉬움. |
| G Table 2.3 | 51 | Time, plasma concentration, urinary amount, ARE, midpoint, excretion rate dataset. | USEFUL | NO | NO | VISUAL_INSPECTED | Worked data source이나 full table은 Step 1 핵심 아님. |
| G Fig 2.36 | 51 | Real ARE and excretion-rate plots from Table 2.3. | USEFUL | YES | YES | VISUAL_INSPECTED | Plot slopes/limitations 설명에 유용. |
| G Fig 2.37 | 53 | Plasma concentration and accumulated urine amount after IV/oral dosing. | USEFUL | NO | YES | VISUAL_INSPECTED | Bioavailability from urinary data context. |
| G Fig 2.38 | 54 | Simultaneous modeling of plasma and urine for F estimation. | USEFUL | NO | YES | VISUAL_INSPECTED | M2 말미 context로 충분. |
| G Fig 2.56 | 77 | Drug input-output and clearance concept schematic. | USEFUL | YES | YES | VISUAL_INSPECTED | Clearance as proportionality concept에 도움. |
| G Fig 2.57 | 77 | Clearance units/concept as volume cleared per time. | USEFUL | YES | YES | VISUAL_INSPECTED | M1 직관 강화용. |
| G Fig 2.58 | 79 | Mass-balance/extraction setup across eliminating organ. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Well-stirred derivation의 구조적 출발점. |
| G Fig 2.59 | 80 | Organ extraction/perfusion flow relationship. | USEFUL | YES | YES | VISUAL_INSPECTED | High/low extraction transition 설명에 유용. |
| G Fig 2.60 | 80 | Parallel organ/extraction conceptualization. | USEFUL | NO | YES | VISUAL_INSPECTED | Text alone으로 대체 가능. |
| G Fig 2.61 | 85 | Route × extraction × protein binding effect on exposure. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M6 4사분면 판단의 핵심 figure. |
| G Fig 2.62 | 86 | In vitro vs in vivo clearance relationship schematic. | USEFUL | YES | YES | VISUAL_INSPECTED | IVIVE risk framing에 유용. |
| G Table 2.7 | 87 | Inter-species physiological characteristics. | USEFUL | NO | NO | VISUAL_INSPECTED | IVIVE context but not 핵심 chain. |
| G Table 2.8 | 87 | Ratio of in vivo to in vitro clearance by species/drug. | USEFUL | YES | NO | VISUAL_INSPECTED | IVIVE over/under-prediction context. |
| G Fig 2.63 | 88 | Single-point IVIVE comparison risk. | USEFUL | YES | YES | VISUAL_INSPECTED | M7 single-point warning에 직접 연결. |
| G Fig 2.64 | 88 | Mean of ratios vs ratio of means / variability issue. | USEFUL | YES | YES | VISUAL_INSPECTED | MMP warning을 시각화. |
| G Fig 2.65 | 89 | Data condensation can hide scatter/structure. | USEFUL | YES | YES | VISUAL_INSPECTED | IVIVE audit mindset에 유용. |
| G Fig 2.66 | 91 | Hepatic clearance model geometry/perfusion structure. | USEFUL | YES | YES | VISUAL_INSPECTED | Four model comparison 배경. |
| G Fig 2.67 | 91 | Dispersion/distributed model conceptual setup. | USEFUL | YES | YES | VISUAL_INSPECTED | Table 2.9 이해 보조. |
| G Fig 2.68 | 92 | Relation among extraction/perfusion/intrinsic activity across models. | USEFUL | YES | YES | VISUAL_INSPECTED | Model differences를 직관화. |
| G Table 2.9 | 94 | Four hepatic clearance models and formula comparison. | ESSENTIAL | YES | YES | CAPTION_AND_CONTEXT | 수식 세부가 핵심이므로 별도 manual formula check 필요. |
| G PK5 Fig 5.1 | 495 | Plasma+urine one-compartment model for case study. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | NONMEM ADVAN1/ODE equivalent model 구조. |
| G PK5 Table 5.1 | 496 | Plasma and urine observations for PK5. | USEFUL | NO | NO | VISUAL_INSPECTED | Full dataset은 optional. |
| G PK5 Fig 5.2 | 496 | Initial visual fit / parameter estimate support. | USEFUL | YES | YES | VISUAL_INSPECTED | Initial estimate reasoning에 유용. |
| G PK5 Fig 5.3 | 497 | Final plasma+urine fit and ODE equivalence. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M9의 핵심 evidence. |
| T5 Fig 5-1 | 120 | Relative importance of elimination route/mechanism in top 200 drugs. | USEFUL | NO | NO | VISUAL_INSPECTED | Context figure. |
| T5 Table 5-1 | 121 | Representative biotransformation patterns and active/inactive metabolites. | USEFUL | NO | NO | VISUAL_INSPECTED | Ch5→Ch20 bridge에 유용. |
| T5 Fig 5-2 | 122 | CYP abundance vs contribution to drug clearance. | USEFUL | NO | NO | VISUAL_INSPECTED | CYP context only. |
| T5 Fig 5-3 | 123 | Weighted mean abundance of CYP enzymes. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Detailed enzyme abundance is not Step 1 core. |
| T5 Fig 5-4 | 124 | Examples of substrates for CYP enzymes. | USEFUL | NO | NO | VISUAL_INSPECTED | DDI/metabolism context. |
| T5 Fig 5-5 | 126 | Organ clearance/extraction relationship. | USEFUL | YES | YES | VISUAL_INSPECTED | Blood clearance/extraction definition support. |
| T5 Fig 5-6 | 129 | Hepatic acinus/sinusoid perfusion structure. | USEFUL | YES | YES | VISUAL_INSPECTED | Well-stirred biological anatomy context. |
| T5 Table 5-2 | 130 | Hepatic blood flow/extraction/clearance examples. | USEFUL | YES | NO | VISUAL_INSPECTED | High/low extraction classification. |
| T5 Fig 5-7 | 131 | Effect of perfusion on hepatic clearance/extraction. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M5 perfusion-limited logic. |
| T5 Fig 5-8 | 132 | Effect of protein binding on hepatic clearance. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M6 fu effects. |
| T5 Fig 5-9 | 134 | Effect of hepatocellular activity on hepatic clearance. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Intrinsic clearance sensitivity. |
| T5 Fig 5-10 | 135 | Memory aid for high/low extraction behavior. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Learner-facing diagram should be remade. |
| T5 Fig 5-11 | 136 | Hepatocyte transporter/enzyme location and extended clearance. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M15 transporter/permeability logic. |
| T5 Fig 5-12 | 138 | Enterohepatic cycling schematic/profile. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | EHC as distribution/recycling concept needs visual. |
| T5 Fig 5-13 | 139 | Nephron anatomy and filtration/secretion/reabsorption sites. | USEFUL | YES | YES | VISUAL_INSPECTED | M13 renal mechanism support. |
| T5 Fig 5-14 | 140 | Renal clearance components schematic. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Filtration/secretion/reabsorption equation chain. |
| T5 Fig 5-15 | 141 | Renal extraction/clearance vs flow concept. | USEFUL | YES | YES | VISUAL_INSPECTED | Renal clearance interpretation. |
| T5 Table 5-3 | 143 | Renal clearance examples relative to filtration/protein binding. | USEFUL | YES | NO | VISUAL_INSPECTED | Reabsorption vs secretion classification. |
| T5 Table 5-4 | 144 | Transporters/secretion examples. | USEFUL | NO | NO | VISUAL_INSPECTED | Context. |
| T5 Fig 5-16 | 145 | Urine pH effect on methamphetamine excretion/reabsorption. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M13 clinical anchor. |
| T5 Table 5-5 | 146 | Drugs affected by urine pH/flow. | USEFUL | NO | NO | VISUAL_INSPECTED | Context list. |
| T5 Fig 5-17 | 146–147 | Urine flow effect on renal clearance/reabsorption. | USEFUL | YES | YES | CAPTION_AND_CONTEXT | Figure label/context sufficient; not central enough to be essential. |
| T5 Fig 5-18 | 147–148 | Renal clearance as rate process / dynamic process. | USEFUL | NO | YES | CAPTION_AND_CONTEXT | Context only. |
| T5 Fig 5-19 | 149 | Half-life depends jointly on CL and V across large ranges. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M14 “t½ is derived” core visual. |
| T5 Table 5-6 | 151 | Equations for interpreting changes after IV bolus. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Integration logic central. |
| T5 Fig 5-20 | 152 | Effect of altered clearance/volume on concentration-time course. | USEFUL | YES | YES | VISUAL_INSPECTED | Integration case support. |
| T5 Fig 5-21 | 153 | Perfusion/protein binding/cellular activity scenario. | USEFUL | YES | YES | VISUAL_INSPECTED | M5/M6 support. |
| T5 Fig 5-22 | 154 | Low extraction protein binding scenario. | USEFUL | YES | YES | VISUAL_INSPECTED | M6 support. |
| T5 Fig 5-23 | 155 | High extraction protein binding scenario. | USEFUL | YES | YES | VISUAL_INSPECTED | M6 support. |
| T5 Fig 5-24 | 156 | Change in renal/hepatic function example. | USEFUL | YES | YES | VISUAL_INSPECTED | M11/M13 support. |
| T5 Table 5-7 | 156 | Summary of parameter changes under altered physiology. | USEFUL | YES | NO | VISUAL_INSPECTED | Helpful integration table. |
| T5 Fig 5-25 | 157 | Phenytoin/uremia binding and concentration-time effects. | USEFUL | YES | YES | VISUAL_INSPECTED | M6 clinical example. |
| T5 Fig 5-26 | 158 | Clofibric acid/nephrotic syndrome or altered binding example. | USEFUL | YES | YES | VISUAL_INSPECTED | M6 clinical example. |
| T5 Fig 5-27 | 159 | DDI/perfusion/intrinsic clearance integration example. | USEFUL | YES | YES | VISUAL_INSPECTED | Integration context. |
| T5 Fig 5-28 | 160 | Hepatic extraction/binding/intrinsic scenario. | USEFUL | YES | YES | VISUAL_INSPECTED | Integration context. |
| T5 Table 5-8 | 161 | Integrated case parameter table. | USEFUL | NO | NO | VISUAL_INSPECTED | Not essential for learner-facing core. |
| T5 Fig 5-29 | 162 | Summary relationship among extraction, perfusion, binding, activity. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Best candidate for Phase 4C redraw. |
| T5 Tables 5-9–5-15 | 163–168 | Study problems and scenario tables. | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Exercises; not core but useful for exam-style validation. |
| T20 Table 20-1 | 658 | Therapeutically important metabolites. | USEFUL | YES | NO | VISUAL_INSPECTED | M16/M20 examples anchor. |
| T20 Fig 20-1 | 660 | Rate-limiting step chain example. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M17 needs this visual logic. |
| T20 Fig 20-2 | 662 | Methylprednisolone hemisuccinate parent-limited vs metabolite profile. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Case B rate-limiting example. |
| T20 Fig 20-3 | 663 | Tolbutamide/hydroxytolbutamide AUC ratio case. | USEFUL | YES | YES | VISUAL_INSPECTED | M16 ratio interpretation support. |
| T20 Fig 20-4 | 665 | Propranolol/naphthoxylactic acid IV disposition. | USEFUL | YES | YES | VISUAL_INSPECTED | M16 example. |
| T20 Table 20-2 | 665 | Metabolite/drug AUC ratio and inference conditions. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | M16 오류 방지 핵심 table. |
| T20 Fig 20-5 | 666 | Oral propranolol first-pass parent/metabolite contribution. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M18 dose error 발생 지점. |
| T20 Fig 20-6 | 667 | Hepatic extraction effect on oral metabolite exposure. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M18 route/extraction mechanism. |
| T20 Fig 20-7 | 668 | Morphine/M6G oral vs IV route comparison. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M18 dose/route correction required. |
| T20 Table 20-3 | 669 | Isoproterenol route-dependent metabolite distribution. | USEFUL | YES | NO | VISUAL_INSPECTED | M18 worked data anchor. |
| T20 Fig 20-8 | 671 | Metabolite accumulation during constant-rate infusion. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M19 time-to-plateau logic. |
| T20 Fig 20-9 | 672 | Halazepam/N-desalkylhalazepam multiple-dose accumulation. | USEFUL | YES | YES | VISUAL_INSPECTED | M19 clinical profile. |
| T20 Fig 20-10 | 674 | Active metabolite renal insufficiency example. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M20 dose-adjustment dilemma core. |
| T20 Table 20-4 | 674 | Normal vs anuric active concentration/dose calculation. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | M20 numerical anchor. |
| T20 Fig 20-11 | 676 | Carbamazepine nonlinear metabolite formation/autoinduction. | USEFUL | YES | YES | VISUAL_INSPECTED | M19 nonlinear extension. |
| T20 Table 20-5 | 677 | Interconversion model parameters/example. | USEFUL | NO | NO | VISUAL_INSPECTED | Context. |
| T20 Fig 20-12 | 678 | Prednisone/prednisolone interconversion profiles. | USEFUL | YES | YES | VISUAL_INSPECTED | M20 interconversion bridge. |
| T20 Fig 20-13 | 679 | Clofibric acid renal impairment/interconversion effect. | USEFUL | YES | YES | VISUAL_INSPECTED | M20 clinical extension. |
| T20 Table 20-6 | 680 | Apparent fraction/metabolite clearance calculation context. | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Study-problem level. |
| T20 Fig 20-14 | 683 | Procainamide/NAPA renal impairment profiles. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M20 active metabolite trap. |
| T20 Table 20-7 | 684 | Procainamide/NAPA related numerical table. | USEFUL | YES | NO | CAPTION_AND_CONTEXT | Numeric confirmation table; use if exact ratios cited. |
| T20 Fig 20-15 | 685 | Competitive agonist parent/metabolite response contribution. | USEFUL | YES | YES | VISUAL_INSPECTED | PD response extension. |
| T20 Table 20-8 | 686 | Response/concentration calculation table. | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Advanced exercise; optional. |
| TD App.D equations D-1–D-8 | 775–776 | Plasma/blood ratio mass-balance and KPBC inversion. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M10 first-principles derivation. |
| TD App.D Study Problem 1 | 776 | Numerical plasma/blood ratio scenario. | USEFUL | NO | NO | VISUAL_INSPECTED | Appendix note only. |
| TE App.E Eq E-1–E-8 | 777–778 | Alternative derivation of well-stirred hepatic clearance. | USEFUL | YES | YES | CAPTION_AND_CONTEXT | Cross-validation for G/T5. |
| TE App.E Eq E-9–E-15 | 778–779 | Permeability-limited Model II and `ρ`. | ESSENTIAL | YES | YES | CAPTION_AND_CONTEXT | M15 inequality correction depends on it. |
| TE App.E Eq E-19–E-20 | 779–780 | Oral AUC first-principles under hepatic extraction. | USEFUL | YES | YES | CAPTION_AND_CONTEXT | M18 support. |

---

## Final Auditor Verdict

**Final status**: `조건부 Go → Patch required before HTML`.  
Draft v0는 핵심 범위를 넓게 포착했으며, 청소율·간/신장·대사체 세션의 major conceptual chain은 대부분 살아 있다. 그러나 아래 항목은 HTML 전 반드시 수정해야 한다.

1. **M15 extended clearance reduction inequality**: 부등호 방향 오류 가능성이 아니라 실제 개념 반전 오류.
2. **M16 AUC ratio inference**: `AUC(m)/AUC < 1` 해석이 원문과 수학식에 반함.
3. **M18 propranolol dose**: `80 mg` → source `20 mg`.
4. **M18 morphine route/dose**: `10 mg dose-equivalent` 삭제/정정; source는 oral `11.7 mg`, IV `5 mg`.
5. **M17 renal impairment shortcut**: T20 renal impairment 메시지와 충돌하므로 삭제/수정.
6. **Table 2.9 formula-level verification**: 모든 model formula를 원문과 1:1 재대조 후 확정.
7. **PDF 밖 실무 claim**: source tag 없이 원문 근거처럼 쓰지 말 것.
8. **Session metadata**: `01_step1_draft_v0.md` → `04_step1_draft_v0`.

**Patch Memo 판정**: Patch Memo의 “과밀·source fidelity 위험·Table 2.9 검증 필요·외부 claim 주의” 지적은 대체로 타당하다. 단, 본 감사에서는 Memo를 자동 채택하지 않고 PDF 근거와 독립 대조하여 위 MUST/SHOULD 항목으로 재분류했다.

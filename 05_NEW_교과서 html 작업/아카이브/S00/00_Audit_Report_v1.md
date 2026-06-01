# 00_Audit Report v1 — Source Fidelity Audit

**업무 형태**: 파일 분석 / PDF 대조 감사  
**웹 검색**: OFF  
**입력**: Original textbook PDFs + Step 1 Draft v0 + Patch Memo  
**역할**: Source Fidelity Auditor  
**판정**: **조건부 PASS — 구조는 유지 가능하나, MUST_FIX 패치 후 Phase 3/HTML 진행 권장**

---

## Executive Verdict

Step 1 Draft v0의 **MUST 4개 구성(M1 Modeling Carousel, M2 PK/PD Linkage & Therapeutic Window, M3 Hill/Emax, M4 Turnover)**은 PDF 범위의 핵심을 대체로 잘 포착했다. 특히 실제 수치 anchor인 warfarin 1.5 mg/kg, propranolol C50=5.3 µg/L, alfentanil 0.27/0.31/0.42 mg/L, total body water turnover 값은 대부분 원문과 일치한다.

다만 Draft v0에는 **원문 직접 근거가 없는 실무 확장·규제 과장·교육용 가상 시나리오**가 섞여 있다. 특히 다음 유형은 HTML 전환 전 반드시 패치해야 한다.

1. **원문보다 강한 단정**: “반드시 local minimum”, “FDA/EMA reviewer가 이의 제기 못 함”.
2. **PDF에 없는 정량값**: “AUC 30–50% 잘못 예측”, “OFV 5 이상”, “4개 이상의 초기추정치”, “6–12개월 지연”, “수백억 원”.
3. **원문 수치 오독**: digoxin vs morphine “dosing frequency 50배 차이”는 원문과 불일치.
4. **Figure 해석 오류**: G Fig.1.2에서 E는 possible initial estimate가 아니라 final estimate 위치다.
5. **유전형 오류**: Draft의 “CYP2C9·VKORC1”은 해당 PDF 범위에서는 “CYP2C9 and CYP2C19 genetic polymorphisms”와 vitamin K epoxide reductase 기전으로 제시된다.

Patch Memo의 핵심 지적은 대체로 타당하다. 단, Patch Memo도 독립 source가 아니라 audit attention guide로만 사용하였다.

---

## T1: Equation/Numerical Audit

| Item | Draft v0 Expression | PDF Source | Classification | Correction |
|---|---|---|---|---|
| Source page range | G Ch.1 p.1–7 + T Ch.1–2 p.3–49 | 첨부 PDF 범위와 일치 | MATCH | 없음 |
| Course scale | “28세션 PopPK 커리큘럼” | PDF에는 없음 | NOT_IN_SOURCE | 커리큘럼 내부 메타데이터로 태그 필요 |
| Modeling Carousel steps | Tentative model → Design → Run experiment → EDA → Fit → Analyze output | G Fig.1.1, p.4 | MATCH | 없음 |
| “fitting은 6단계 중 5번째” | Step 5 = Fit model(s) | G Fig.1.1 | MATCH | 없음 |
| “fitting의 정확도는 앞 단계가 결정” | EDA와 design이 model structure/initial estimates를 제공한다는 취지는 원문과 일치 | G p.5–6 | MATCH(교육적 단순화) | 과한 단정만 완화 |
| Constant/parameter/variable | Dose D constant; V, CL parameters; Ĉ, t variables | G p.1–2 | MATCH | 없음 |
| Primary/secondary parameter | K=CL/V; AUC=D/CL; t1/2=ln(2)/K | G p.2 | MATCH | 없음 |
| Observed-predicted relation | C = Ĉ + ε | G Eq.1:2, p.2 | MATCH | 없음 |
| One-compartment prediction equation | Draft는 G Eq.52:1/1:1에 해당하는 Ĉ=(D/V)e^{-(CL/V)t}를 본문에 반영하지 않음 | G p.1 | MISSING | T5에서 SHOULD_FIX |
| Five dysfunctions | EDA failure, slavery to formulas, trust in software, improper weighting, lack of holistic view | G p.4 | MATCH | 없음 |
| “EDA 누락이 가장 빈번” | Draft: “가장 빈번” | G p.4는 five most common dysfunctions만 제시, 순위 없음 | ERROR | “5대 common dysfunction 중 하나”로 낮출 것 |
| CATD 포함 | Computer Assisted Trial Design and prior simulation | G p.5 | MATCH | 없음 |
| EDA plots | concentration-time, response-time, response-concentration | G p.5 | MATCH | 없음 |
| Dose-normalized curve/AUC vs dose | 비선형성 탐색 절차 | G p.5 | MATCH | 없음 |
| Initial estimates/local minimum | nonlinear fitting requires initial estimates; to avoid local minimum | G p.6 | MATCH | “위험 증가” 수준 유지 |
| “반드시 local minimum” | Draft M1 Big Idea | PDF 직접 근거 없음 | ERROR | “local minimum에 수렴할 위험이 커진다”로 수정 |
| “wrong FIH dose recommendation” | Draft M1 Big Idea | PDF 직접 근거 없음 | NOT_IN_SOURCE | [실무 추론] 또는 삭제 |
| G Fig.1.2 A/B/C/E 해석 | “A·B·C·E 후보 시작점” | G Fig.1.2 caption: yellow = possible initial estimates; red = final estimates. E는 final estimate | ERROR | A/B/C는 possible initial estimate, D/E는 final estimate로 정정 |
| OFV landscape | Draft: OFV landscape | G Fig.1.2는 objective function WRSS | ERROR/RESTORED | PDF fidelity에서는 WRSS/objective function로 표기; NONMEM 확장은 [실무 추론] |
| AUC 30–50% wrong prediction | Draft Plausible Fallacy | PDF에 없음 | NOT_IN_SOURCE | 삭제 또는 [교육용 가상 시나리오: 수치 임의] 표시 |
| $COV step 통과 가능/Hessian 양정치 | Draft Plausible Fallacy | PDF에 없음 | NOT_IN_SOURCE | 삭제 또는 [실무 추론] 표시 |
| GOF plot 무난해 보임 | Draft Plausible Fallacy | PDF에 없음 | NOT_IN_SOURCE | 삭제 또는 [실무 추론] 표시 |
| “4개 이상의 initial estimates” | Draft Local Minimum Mirage | G p.6는 different initial estimates 권고만 있음 | NOT_IN_SOURCE | “different initial estimates”로 수정 |
| “OFV 5 단위 이상” | Draft Local Minimum Mirage | PDF에 없음 | NOT_IN_SOURCE | 삭제 |
| NCA usually suffice | bioavailability/total clearance 목적에는 NCA suffice | G p.4 | MATCH | 없음 |
| Model 필요 상황 | single→multiple dose 예측, nonlinear kinetics, PK-PD quantification | G p.4 | MATCH | 없음 |
| Multiple dose levels/repeated dosing/routes | multiple dose levels, repeated dosing, multiple input rates/routes often needed | G p.7 | MATCH | 없음 |
| Digoxin dose | 0.125–0.25 mg once daily | T Ch.1 p.4 | MATCH | 없음 |
| Morphine sulfate dose | 10–50 mg up to 6 times/day | T Ch.1 p.4 | MATCH | 없음 |
| “dosing frequency가 50배 차이” | Draft M2 Big Idea | 원문 frequency는 once daily vs up to 6 times/day; 50배 아님 | ERROR | “투여량 범위와 투여빈도가 크게 다르다” 또는 “up to 6 times/day” |
| 5% hospital admission | Draft에는 없음 | T Ch.1 p.4 | MISSING | T2/T3에서 SHOULD_FIX 후보 |
| PK definition | dose/dosage form/frequency/route → concentration-time | T Fig.1-2/p.4–5 | MATCH | 없음 |
| PD definition | concentration → desired/adverse effect | T Fig.1-2/p.4–5 | MATCH | 없음 |
| PK/PD linkage | PK + PD integration predicts effect-time | T Fig.1-3/p.5 | MATCH | 없음 |
| Therapeutic window | adequate response without undue adverse effects | T Fig.1-4/p.6 | MATCH | 없음 |
| Therapeutic window set notation | Draft uses probability threshold set | PDF에는 없음 | NOT_IN_SOURCE | [해석/교육용 formalization] 태그 필요 |
| Warfarin dose | single oral 1.5 mg/kg sodium warfarin | T Fig.1-6/p.8 | MATCH | 없음 |
| Warfarin sampling/data | averages from five male volunteers | T Fig.1-6 caption | MATCH | 없음 |
| Warfarin response delay | peak effect approx. 2–4 days; first 2 days response increases | T p.8 | MATCH | 없음 |
| Paclitaxel route | single intravenous dose | T Fig.1-7/p.8 | MATCH | 없음 |
| Paclitaxel kinetics/response | eliminated within 2 days; WBC nadir >1 week; return baseline 3 weeks | T p.9 | MATCH | 없음 |
| Phenytoin variability | chronic dosing concentration varies widely | T Fig.1-8/p.10 | MATCH/CONTEXT | 없음 |
| Warfarin variability | S-warfarin concentration range for similar anticoagulation | T Fig.1-9/p.10 | MATCH/CONTEXT | 없음 |
| CYP2C9·VKORC1 | Draft M2 variability | PDF text states CYP2C9 and CYP2C19 polymorphisms; vitamin K epoxide reductase mechanism, not VKORC1 label | ERROR | “CYP2C9/CYP2C19 polymorphisms; vitamin K epoxide reductase mechanism”로 정정 |
| G6PD | >400 million variants/carriers context; primaquine hemolysis | T p.11 | MATCH | 없음 |
| Debrisoquine/CYP2D6 | metabolism variability example | T p.11–12 | MATCH | 없음 |
| Terfenadine + ketoconazole | CYP inhibition → torsade de pointes/withdrawal | T p.12 | MATCH | 없음 |
| Adherence ~50% | by end of first year only 50% continue prescribed medication | T Fig.1-10/p.12 | MATCH | 없음 |
| Adherence chain | prescribed regimen → adherence pattern → exposure → effects | T Fig.1-11/p.13 | MATCH | 없음 |
| Digital medicine aripiprazole | IEM/patch/app/web portal | T Fig.1-12/p.14 | MISSING | T2 OPTIONAL |
| Table 2-1 applications | PK/PD applications in therapy | T Table 2-1/p.20 | MISSING | T5 SHOULD/OPTIONAL |
| Plasma/serum/whole blood | definitions and differences | T Table 2-2/p.21 | MATCH | 없음 |
| Unbound concentration | unbound drives distribution/elimination/PD response | T p.21 | MATCH | 없음 |
| Cmax/tmax/AUC definitions | Cmax, tmax, AUC | T Fig.2-1/p.22 | MATCH | 없음 |
| Fig.2-1 numeric example | Cmax=96 µg/L; tmax=3.0 hr | T p.22 | MISSING | SHOULD_FIX as concrete anchor |
| Acenocoumarol | oral 20 mg 50/50 racemate | T Fig.2-2A/p.23 | MATCH | 없음 |
| Methylphenidate | oral 30 mg racemate | T Fig.2-2B/p.23 | MATCH | 없음 |
| S-naproxen/tamsulosin | single stereoisomer examples | T p.24 | MATCH | 없음 |
| Aspirin/salicylic acid | oral 650 mg aspirin; metabolite profile | T Fig.2-3/p.25 | MATCH | 없음 |
| PK mass balance Eq.2-1 | Dose = absorption site + body + excreted + metabolized | T p.28 | MATCH | 없음 |
| PK rate Eq.2-2 | dA_body/dt = R_abs - (R_excretion + R_metabolism) | T p.29 | MATCH | 없음 |
| ADME/disposition | disposition = distribution + elimination | T Fig.2-8/p.31 | MATCH | 없음 |
| Bioavailability definition | Draft says extent only in book definition | T p.31–32 | MATCH | 없음 |
| Enterohepatic cycle | component of distribution | T Fig.2-10/p.33 | MATCH | 없음 |
| Agonist/antagonist/partial | receptor functional response definitions | T p.33 | MATCH | 없음 |
| Estrogens agonist/antagonist by concentration range | T p.33 | MATCH | 없음 |
| Graded/quantal definitions | T p.35 | MATCH | 없음 |
| Busulfan irreversible binding | alkylating anticancer drugs such as busulfan covalently bind DNA | T p.35 | MATCH | 없음 |
| Measured response Eq.2-3 | drug response + placebo response + baseline | T p.36 | MATCH | 없음 |
| Montelukast | 10 mg oral vs placebo, FEV1, 24 hr | T Fig.2-12/p.37 | MATCH | 없음 |
| Prednisone Duchenne | placebo, 0.3/0.75 mg/kg daily, 6 months; 1 vs 3 month improvement | T Fig.2-13/p.38 | MATCH | 없음 |
| Natural progression | around 1% per year beyond ~20 years | T p.38 | MATCH | 없음 |
| Moxifloxacin | 400 mg q24h, resistant clones day 18, 100% day 28 | T Fig.2-15/p.39 | MATCH | 없음 |
| Hill equation Eq.2-4 | E=Emax·C^γ/(C50^γ+C^γ) | T Eq.2-4/p.40 | MATCH | 없음 |
| Ketamine values | S(+) C50=0.7 mg/L, R(-) C50=1.8 mg/L; Emax differs | T p.40/Fig.2-11 | MATCH | 없음 |
| γ 20–80% ratio | γ=1: 0.25→4 C50 = 16-fold; γ=2: 0.5→2 C50 = 4-fold | T p.40 | MATCH | 없음 |
| γ generally 1–3 | Source states generally γ lies between 1 and 3 | T p.40 | MISSING | OPTIONAL/SHOULD depending depth |
| Propranolol | γ close to 1; Emax 40%; C50 5.3 µg/L | T Fig.2-17/p.42 | MATCH | 없음 |
| Alfentanil | C50 order breast 0.27 < lower abdomen 0.31 < upper abdomen 0.42 mg/L | T Fig.2-18/p.42 | MATCH | 없음 |
| “opioid anesthetics γ very large” | Draft M3 Big Idea | Alfentanil figure is quantal cumulative frequency; source does not estimate γ for opioid anesthetic | NOT_IN_SOURCE | “quantal response can resemble very steep all-or-none relationship”로 분리 |
| Hb-O2 γ≈2.7 | Draft L4 | PDF 범위에 없음 | NOT_IN_SOURCE | 삭제 또는 external source 표시 금지 |
| Michaelis-Menten/Langmuir structural isomorphism | Draft L3 | 해당 PDF 범위에 직접 없음 | NOT_IN_SOURCE | [해석] 태그 필요 |
| NONMEM/nlmixr2 code | Draft M3/M4 code blocks | PDF 범위에 없음 | NOT_IN_SOURCE | [실무 구현 예시]로 분리하거나 Source Fidelity output에서는 제외 |
| Dose-time-response Fig.2-19 | Draft에는 거의 없음 | T Fig.2-19/p.44 | MISSING | SHOULD_FIX; Cmax/tmax/AUC의 임상 의미 연결 |
| Turnover Eq.2-5 | kt=Rt/Ass | T p.45 | MATCH | 없음 |
| Turnover Eq.2-6 | tt=Ass/Rt | T p.45 | MATCH | 없음 |
| Turnover Eq.2-7 | tt=1/kt | T p.45 | MATCH | 없음 |
| Turnover ODE | dA/dt=Rin−kt·A | PDF에 직접 없음 | RESTORED/NOT_IN_SOURCE | [해석/후속 모델링 bridge] 태그 필요 |
| Total body water normal | Ass=42 L; Rt=2.5 L/day; kt=0.06 day−1; tt=17 days | T Fig.2-20/p.45–46 | MATCH | 없음 |
| Desert environment | Rt=21 L/day; kt=0.5 day−1; tt=2 days; pool constant | T p.46 | MATCH | 없음 |
| Ezetimibe/simvastatin/filgrastim | examples of altered turnover | T p.46 | MATCH | 없음 |
| Warfarin clotting factor tt=6h~3d | Draft L5 | 해당 PDF 범위에 없음 | NOT_IN_SOURCE | 삭제 또는 별도 출처 필요 |
| Albumin 350 g/16 days | Study Problem 10 | T p.49 | MATCH | self-test source로는 가능 |
| Q7 severe burn 2× Rt, IV replacement | Draft self-test | PDF에 없음 | NOT_IN_SOURCE | [교육용 가상 문제] 태그 필요 |
| Q8 hypothetical R/S isomer Emax values | Draft self-test | PDF에 없음 | NOT_IN_SOURCE | [교육용 가상 문제] 태그 필요 |
| Q9 280명/4 dose/18시간/Phase 2b | Draft boss dilemma | PDF에 없음 | NOT_IN_SOURCE | [교육용 가상 시나리오] 태그 필요 |
| Regulatory deficiency, FDA/EMA, launch 6–12 months | Draft §5/§7/§8 | PDF에 없음 | NOT_IN_SOURCE | 삭제 또는 [실무 추론] 명시; Source Fidelity 기준에서는 MUST_FIX |
| “AI가 구조적으로 못 한다” | Draft §8 | PDF에 없음 | NOT_IN_SOURCE | Source-based Step 1 본문에서는 제외 권장 |

---

## T2: Examples & Data Audit

| Item | Draft v0 Status | PDF Location | Classification | Importance | Action |
|---|---|---|---|---|---|
| Aspirin dose-response/toxicity: 25 mg, 300–600 mg, 10 g fatal | Omitted | T Ch.1 p.3 | MISSING | MEDIUM | Therapeutic dose intuition context로 1문장 반영 권장 |
| Paracelsus “dose makes poison” | Omitted | T Ch.1 p.3 | MISSING | LOW | 선택 반영 |
| 5% hospital admissions due to inappropriate drug use | Omitted | T Ch.1 p.4 | MISSING | MEDIUM | “why this matters clinically” anchor로 반영 권장 |
| Empirical trial-and-error regimen design | Omitted/weak | T Fig.1-1 p.4 | MISSING | MEDIUM | M2 context에 1문장 반영 |
| Digoxin 0.125–0.25 mg qd | Included | T p.4 | INCLUDED_CORRECT | HIGH | 유지 |
| Morphine sulfate 10–50 mg up to 6/day | Included | T p.4 | INCLUDED_CORRECT | HIGH | “50배” 표현만 정정 |
| PK/PD rational input-response | Included | T Fig.1-2/1-3 p.5 | INCLUDED_CORRECT | HIGH | 유지 |
| Therapeutic window | Included | T Fig.1-4 p.6 | INCLUDED_CORRECT | HIGH | 유지 |
| Digoxin accumulation/digitalizing dose | Partly included | T Fig.1-5 p.7 | MISSING/WEAK | MEDIUM | rapid achievement + maintenance logic 1문장 보강 권장 |
| Warfarin 1.5 mg/kg oral, 5 male volunteers | Included | T Fig.1-6 p.8 | INCLUDED_CORRECT | HIGH | 유지 |
| Paclitaxel single i.v. dose/leukopenia | Included | T Fig.1-7 p.8–9 | INCLUDED_CORRECT | HIGH | 유지 |
| Clonidine hypotensive/hypertensive by concentration | Included as limitation | T p.9 | INCLUDED_CORRECT | MEDIUM | 유지 |
| Phenytoin dose-concentration variability | Included/brief | T Fig.1-8 p.10 | INCLUDED_CORRECT | MEDIUM | 유지 |
| Warfarin S-warfarin variability; 97 patients | Included/brief | T Fig.1-9 p.10 | INCLUDED_ERROR | MEDIUM | CYP2C9/VKORC1 부분 정정 |
| G6PD/primaquine hemolysis | Included/brief | T p.11 | INCLUDED_CORRECT | MEDIUM | 유지 |
| Debrisoquine metabolism variability | Included/brief | T p.11–12 | INCLUDED_CORRECT | MEDIUM | 유지 |
| Terfenadine + ketoconazole | Included | T p.12 | INCLUDED_CORRECT | MEDIUM | 유지 |
| Adherence/Vrijens 2008 once-daily antihypertensive | Included | T Fig.1-10 p.12 | INCLUDED_CORRECT | HIGH | 유지 |
| Digital medicine aripiprazole monitoring | Omitted | T Fig.1-12 p.14 | MISSING | LOW | Optional; scope상 생략 가능 |
| Industrial development process | Omitted | T Fig.1-13 p.15 | MISSING | LOW | Optional; Pre-Sprint에는 생략 가능 |
| Table 2-1 PK/PD applications | Omitted | T p.20 | MISSING | MEDIUM | M2 purpose/context 1문장 반영 권장 |
| Plasma/serum/whole blood | Included | T Table 2-2 p.21 | INCLUDED_CORRECT | MEDIUM | 유지 |
| Unbound concentration conditions | Included | T p.21 | INCLUDED_CORRECT | HIGH | 유지 |
| Exposure-time Cmax/tmax/AUC example 96 µg/L/3.0 hr | Omitted | T Fig.2-1 p.22 | MISSING | MEDIUM | M3/M2 context에 수치 anchor로 추가 권장 |
| Acenocoumarol R/S, oral 20 mg racemate | Included | T Fig.2-2 p.23 | INCLUDED_CORRECT | MEDIUM | 유지 |
| Methylphenidate (+)/(−), oral 30 mg racemate | Included | T Fig.2-2 p.23 | INCLUDED_CORRECT | MEDIUM | 유지 |
| Aspirin/salicylic acid, oral 650 mg | Included | T Fig.2-3 p.25 | INCLUDED_CORRECT | MEDIUM | 유지 |
| ADME/anatomic route/first-pass loss | Included | T Fig.2-4/2-8/2-9 p.26–32 | INCLUDED_CORRECT | MEDIUM | 내용 길이는 별도 편집 이슈 |
| Enterohepatic cycle | Included | T Fig.2-10 p.33 | INCLUDED_CORRECT | MEDIUM | 유지 |
| Ketamine i.v. graded response | Included | T Fig.2-11 p.35 | INCLUDED_CORRECT | HIGH | 유지 |
| Montelukast 10 mg/placebo FEV1 | Included | T Fig.2-12 p.37 | INCLUDED_CORRECT | MEDIUM | 유지 |
| Prednisone in Duchenne dystrophy 0.3/0.75 mg/kg | Included | T Fig.2-13 p.38 | INCLUDED_CORRECT | MEDIUM | 유지 |
| Disease progression schema | Included | T Fig.2-14 p.39 | INCLUDED_CORRECT | MEDIUM | 유지 |
| Moxifloxacin resistance | Included | T Fig.2-15 p.39 | INCLUDED_CORRECT | MEDIUM | 유지 |
| Propranolol unbound concentration/Hill fit | Included | T Fig.2-17 p.42 | INCLUDED_CORRECT | HIGH | 유지 |
| Alfentanil quantal response | Included | T Fig.2-18 p.42 | INCLUDED_CORRECT | HIGH | 유지 |
| Dose-time-response scenarios | Omitted | T Fig.2-19 p.44 | MISSING | HIGH | Cmax/tmax/AUC가 임상 목표에 따라 달라진다는 bridge 필요 |
| Total body water turnover | Included | T Fig.2-20 p.45–46 | INCLUDED_CORRECT | HIGH | 유지 |
| AF-DX116 study problem | Omitted | T Fig.2-21 p.48 | MISSING | LOW | Optional; self-test로는 활용 가능 |
| Hepatic toxicity vs AUC study problem | Omitted | T Fig.2-22 p.48–49 | MISSING | LOW/MEDIUM | Optional; exposure metric selection 예시로는 유용 |

---

## T3: Author Key Messages

| Message | PDF Location | In Draft v0? | Status |
|---|---|---|---|
| Book aims to help readers critically and accurately analyze PK/PD data using theory and real-life case studies. | G p.1 | Partly | SHOULD_FIX: “real-life case studies” orientation weak |
| Model only when needed; NCA suffices for simple exposure/CL questions. | G p.3–4 | Yes | INCLUDED |
| The model should be only as complex as needed to answer the question. | G p.3–4 | Partly | SHOULD_FIX: explicit phrase absent |
| Good analysts let biology and collected data drive the analysis. | G p.3 | Yes/implicit | INCLUDED_AS_CONTEXT |
| Take time to understand data/results; do not make everything merely numerical. | G p.3 | Partly | SHOULD_FIX: Barbara McClintock message absent |
| Five common dysfunctions and Modeling Carousel are the core “art of successful modeling.” | G p.4 | Yes | INCLUDED |
| Dose regimen questions are how much, how often, how long, which route, which dosage form. | T Ch.1 p.3 | Partly | SHOULD_FIX: clinical questions not explicit enough |
| Concentration at site of action, not dose administered, drives response. | T p.4–5 | Yes | INCLUDED |
| PK and PD are insufficient separately; only linked/integrated PK/PD is therapeutically useful. | T Fig.1-3 p.5 | Yes | INCLUDED |
| Therapeutic window balances therapeutic and adverse effects. | T Fig.1-4 p.6 | Yes | INCLUDED |
| Temporal events after administration are necessary for meaningful optimal-use decisions. | T p.7 | Yes | INCLUDED |
| Drug response variability invalidates one-dose-for-all for intermediate/narrow window drugs. | T p.9–10 | Yes | INCLUDED |
| Adherence is a major source of variability and must be incorporated between prescribed regimen and exposure. | T p.12–13 | Yes | INCLUDED |
| PK/PD is useful across development: design, selection, dose escalation, toxicity, special populations, postmarketing. | T Fig.1-13/Table 2-1 | Weak | OPTIONAL/SHOULD depending curriculum scope |
| Ch.2 defines input-exposure and exposure-response terminology. | T p.19 | Yes | INCLUDED |
| Chemical specificity matters: distinguish parent, metabolite, stereoisomers. | T p.23–25 | Yes | INCLUDED |
| Mass balance applies under all circumstances regardless of absorption/elimination nature. | T p.29 | Yes | INCLUDED |
| Assessing true drug effect requires separating drug response, placebo response, and baseline. | T Eq.2-3/p.36 | Yes | INCLUDED |
| The relative importance of Cmax, tmax, and AUC depends on clinical application and exposure-response relationship. | T Fig.2-19/p.44 | Weak/Omitted | MUST/SHOULD_FIX: important bridge absent |
| Turnover rate alone does not fully convey process speed; fractional rate and turnover time often characterize turnover better. | T p.45–46 | Yes | INCLUDED |

---

## T4: Priority Summary

| # | Item | Priority | Rationale |
|---|---|---|---|
| 1 | “반드시 local minimum”, “잘못된 FIH 용량 추천” | MUST_FIX | Source보다 강한 단정; PDF는 risk/avoidance 수준 |
| 2 | “AUC 30–50% 잘못 예측” | MUST_FIX | PDF에 없는 정량값 |
| 3 | G Fig.1.2 A/B/C/E 시작점 해석 | MUST_FIX | E는 initial estimate가 아니라 final global estimate 위치 |
| 4 | “OFV landscape/OFV 5 이상/4개 이상의 초기추정치” | MUST_FIX | PDF는 WRSS objective function과 different initial estimates만 제시 |
| 5 | “EDA failure가 가장 빈번” | MUST_FIX | PDF는 five most common dysfunctions; rank 없음 |
| 6 | “digoxin vs morphine dosing frequency 50배” | MUST_FIX | frequency는 once daily vs up to 6/day; 50배 아님 |
| 7 | “CYP2C9·VKORC1” | MUST_FIX | 해당 PDF 범위는 CYP2C9/CYP2C19 polymorphisms 및 vitamin K epoxide reductase 기전 |
| 8 | Regulatory overclaims: “FDA/EMA reviewer 이의 제기 못 함”, “deficiency letter”, “6–12개월 지연”, “수백억 원” | MUST_FIX | 원문에 없는 실무 확장. 삭제 또는 명확히 [실무 추론]/[교육용 가상 시나리오] 태그 필요 |
| 9 | G one-compartment prediction equation omitted | SHOULD_FIX | 기본 개념 섹션의 named formula가 빠짐 |
| 10 | Fig.2-1 Cmax=96 µg/L, tmax=3.0 hr omitted | SHOULD_FIX | Cmax/tmax/AUC 정의에 좋은 실제 수치 anchor |
| 11 | Fig.2-19 dose-time-response scenarios omitted | SHOULD_FIX | exposure-time profile의 임상 의미 bridge가 비어 있음 |
| 12 | “model only as complex as needed” explicit message | SHOULD_FIX | G Ch.1 핵심 author message |
| 13 | Clinical dosing questions: how much/how often/how long/route/dosage form | SHOULD_FIX | T Ch.1 opening의 임상 질문 프레임 |
| 14 | Table 2-1 applications | OPTIONAL/SHOULD_FIX | 목적론 보강에는 유용하나 MUST 카드 핵심은 아님 |
| 15 | Digital medicine/aripiprazole Fig.1-12 | OPTIONAL | Adherence modern example; Pre-Sprint core에는 부차적 |
| 16 | Industrial perspective Fig.1-13 | OPTIONAL | Book organization/development context; scope상 생략 가능 |
| 17 | AF-DX116 and hepatic toxicity study problems | OPTIONAL | Self-test 확장 소재로 유용하지만 핵심 개념 chain은 아님 |
| 18 | Hb-O2 γ≈2.7, Michaelis-Menten/Langmuir, PDCA/OODA, AI/Regulatory meta-claims | REJECT unless separately tagged | PDF source fidelity 산출물에는 넣으면 안 됨; 외부/해석/실무 확장으로 분리 필요 |
| 19 | Patch Memo: overclaim removal | MATCH | 독립 감사 결과와 일치 |
| 20 | Patch Memo: CONTEXT compression | OPTIONAL | Source fidelity 문제라기보다 편집/워크플로우 준수 문제 |
| 21 | Patch Memo: Source vs inference tags | MATCH | 본 audit에서 MUST_FIX로 확인됨 |
| 22 | Patch Memo: Phase 2 before HTML | MATCH | Draft 자체도 Phase 2 필요성을 언급 |

---

## T5: Coverage Audit

| PDF Element | Type | PDF Location | Step 1 Status | Omission Verdict | Required Action |
|---|---|---|---|---|---|
| Objectives | Heading/objectives | G p.1 | OMITTED_JUSTIFIABLE | Low | 필요 없음 |
| 1.1 Introduction | H2 | G p.1 | INCLUDED_AS_CONTEXT | - | 유지 |
| 1.2 Basic Concepts | H2 | G p.1–2 | INCLUDED_AS_CONTEXT | - | G prediction equation만 보강 |
| G Eq.52:1/1:1 predicted concentration | Numbered formula | G p.1 | OMITTED_PROBLEMATIC | MISSING_BRIDGE | SHOULD_FIX |
| G Eq.1:2 C=Ĉ+ε | Numbered formula | G p.2 | INCLUDED_AS_CONTEXT | - | 유지 |
| Primary/secondary parameters | Concept | G p.2 | INCLUDED_AS_CONTEXT | - | 유지 |
| 1.3 Why Model the Data? | H2 | G p.2–4 | INCLUDED_AS_MUST | - | 유지 |
| “model only as complex as needed” | Repeated/key message | G p.3–4 | INCLUDED_AS_CONTEXT weak | MISSING_AUTHOR_MSG | SHOULD_FIX |
| NCA vs model need | Key message | G p.4 | INCLUDED_AS_CONTEXT | - | 유지 |
| 1.4 The Art of Successful Modeling | H2 | G p.4–7 | INCLUDED_AS_MUST | - | 유지 |
| Fig.1.1 Modeling carousel | Figure | G p.4 | INCLUDED_AS_MUST | - | 유지/view pointer 필요 |
| CATD/simulation quotation | Key message | G p.5 | INCLUDED_AS_CONTEXT | - | 유지 |
| EDA plots and dose-normalization | Method | G p.5 | INCLUDED_AS_MUST | - | 유지 |
| Fig.1.2 local/global minimum | Figure | G p.6 | INCLUDED_AS_MUST but error | MISSING_CRITICAL/ERROR | MUST_FIX figure interpretation |
| Step 6 diagnostics/model validation | Method | G p.6–7 | INCLUDED_AS_CONTEXT | - | 유지 |
| 1.5 How to Use This Book | H2 | G p.7 | OMITTED_JUSTIFIABLE | Low | 필요 없음 |
| Clinical Setting | H1/H2 | T p.3–4 | INCLUDED_AS_CONTEXT weak | MISSING_AUTHOR_MSG | SHOULD_FIX clinical questions |
| Fig.1-1 empirical approach | Figure | T p.4 | OMITTED_PROBLEMATIC | MISSING_BRIDGE | empirical vs rational contrast 1문장 |
| Input-Response Phases | H2 | T p.4–5 | INCLUDED_AS_MUST | - | 유지 |
| Fig.1-2 rational approach | Figure | T p.5 | INCLUDED_AS_MUST | - | 유지 |
| Fig.1-3 PK/PD linked integrated | Figure | T p.5 | INCLUDED_AS_MUST | - | View pointer ESSENTIAL |
| Fig.1-4 therapeutic window | Figure | T p.6 | INCLUDED_AS_MUST | - | View pointer ESSENTIAL |
| Fig.1-5 accumulation/digitalizing dose | Figure/example | T p.7 | INCLUDED_AS_CONTEXT weak | MISSING_EXAMPLE | SHOULD_FIX 1문장 |
| Fig.1-6 warfarin delay | Figure/dataset | T p.8 | INCLUDED_AS_MUST | - | 유지 |
| Fig.1-7 paclitaxel leukopenia | Figure/dataset | T p.8–9 | INCLUDED_AS_MUST/CONTEXT | - | 유지 |
| Clonidine dual effect | Worked example | T p.9 | INCLUDED_AS_CONTEXT | - | 유지 |
| Variability in Drug Response | H2 | T p.9–12 | INCLUDED_AS_CONTEXT | - | 유지 |
| Fig.1-8 phenytoin | Figure/dataset | T p.10 | INCLUDED_AS_CONTEXT | - | 유지 |
| Fig.1-9 warfarin variability | Figure/dataset | T p.10 | INCLUDED_AS_CONTEXT but typo | ERROR | CYP/VKORC correction |
| G6PD/primaquine/debrisoquine/terfenadine | Examples | T p.11–12 | INCLUDED_AS_CONTEXT | - | 유지 |
| Adherence | H2 | T p.12–14 | INCLUDED_AS_CONTEXT | - | 유지 |
| Fig.1-10 adherence | Figure/dataset | T p.12 | INCLUDED_AS_CONTEXT | - | 유지 |
| Fig.1-11 adherence chain | Figure | T p.13 | INCLUDED_AS_CONTEXT | - | 유지 |
| Fig.1-12 digital medicine | Figure | T p.14 | OMITTED_JUSTIFIABLE | Low | Optional |
| Industrial Perspective | H2 | T p.14–15 | OMITTED_JUSTIFIABLE | Low | Optional |
| Fig.1-13 development process | Figure | T p.15 | OMITTED_JUSTIFIABLE | Low | Optional |
| Organization of the Book | H2 | T p.16–17 | OMITTED_JUSTIFIABLE | Low | 필요 없음 |
| Chapter 2 Objectives | Objectives | T p.19 | INCLUDED_AS_CONTEXT | - | 유지 |
| Table 2-1 applications | Table | T p.20 | OMITTED_PROBLEMATIC | MISSING_AUTHOR_MSG | OPTIONAL/SHOULD |
| Pharmacokinetics/Systemic Exposure | H1/H2 | T p.20 | INCLUDED_AS_CONTEXT | - | 유지 |
| Sites of Measurement | H2 | T p.20–21 | INCLUDED_AS_CONTEXT | - | 유지 |
| Table 2-2 plasma/serum/whole blood | Table | T p.21 | INCLUDED_AS_CONTEXT | - | 유지 |
| Unbound Drug Concentration | H2 | T p.21 | INCLUDED_AS_CONTEXT | - | 유지 |
| Exposure-Time Profile | H2 | T p.21–22 | INCLUDED_AS_CONTEXT weak | MISSING_EXAMPLE | Add 96 µg/L, 3.0 hr |
| Fig.2-1 Cmax/tmax/AUC | Figure | T p.22 | INCLUDED_AS_CONTEXT weak | MISSING_EXAMPLE | SHOULD_FIX |
| Period of Observation | H2 | T p.22 | OMITTED_JUSTIFIABLE | Low | 필요 없음 |
| Chemical Purity and Analytic Specificity | H2 | T p.23–24 | INCLUDED_AS_CONTEXT | - | 유지 |
| Fig.2-2 stereoisomers | Figure/dataset | T p.23 | INCLUDED_AS_CONTEXT | - | 유지 |
| Active Metabolites and Prodrugs | H2 | T p.24–25 | INCLUDED_AS_CONTEXT | - | 유지 |
| Fig.2-3 aspirin/salicylic acid | Figure/dataset | T p.25 | INCLUDED_AS_CONTEXT | - | 유지 |
| Anatomic and Physiologic Considerations | H2 | T p.26 | INCLUDED_AS_CONTEXT | - | 유지 |
| Sites of Administration | H2/table | T p.26–27 | INCLUDED_AS_CONTEXT | - | 유지 |
| Fig.2-4 anatomy/first pass | Figure | T p.26 | INCLUDED_AS_CONTEXT | - | 유지 |
| Table 2-3 extravascular routes | Table | T p.27 | INCLUDED_AS_CONTEXT | - | 유지 |
| Events after Entering Systemically | H2 | T p.28 | INCLUDED_AS_CONTEXT | - | 유지 |
| Models for Drug Absorption and Disposition | H2 | T p.28–30 | INCLUDED_AS_CONTEXT weak | MISSING_BRIDGE | Fig.2-5/2-6/2-7 view optional |
| Fig.2-5 mass balance model | Figure | T p.28 | INCLUDED_AS_MUST via Eq.2-1 | - | 유지 |
| Fig.2-6 mass balance time course | Figure | T p.29 | OMITTED_JUSTIFIABLE | Low | Optional |
| Fig.2-7 model types | Figure | T p.30 | OMITTED_PROBLEMATIC | MISSING_BRIDGE | Optional/SHOULD for model vocabulary |
| Definitions of PK Terms/ADME | H2 | T p.29–33 | INCLUDED_AS_CONTEXT | - | 유지 |
| Fig.2-8 ADME | Figure | T p.31 | INCLUDED_AS_CONTEXT | - | 유지 |
| Fig.2-9 systemic absorption barriers | Figure | T p.31–32 | INCLUDED_AS_CONTEXT | - | 유지 |
| Bioavailability | Concept | T p.31–32 | INCLUDED_AS_CONTEXT | - | 유지 |
| Fig.2-10 enterohepatic cycle | Figure | T p.33 | INCLUDED_AS_CONTEXT | - | 유지 |
| Pharmacodynamics | H1 | T p.33–35 | INCLUDED_AS_MUST | - | 유지 |
| Classification of Response | H2 | T p.34–35 | INCLUDED_AS_CONTEXT | - | 유지 |
| Fig.2-11 ketamine | Figure/dataset | T p.35 | INCLUDED_AS_MUST | - | View pointer ESSENTIAL |
| Assessment of Drug Response | H2 | T p.36–39 | INCLUDED_AS_CONTEXT | - | 유지 |
| Eq.2-3 measured response | Formula | T p.36 | INCLUDED_AS_CONTEXT | - | 유지 |
| Fig.2-12 montelukast/placebo | Figure/dataset | T p.37 | INCLUDED_AS_CONTEXT | - | 유지 |
| Fig.2-13 prednisone/Duchenne | Figure/dataset | T p.38 | INCLUDED_AS_CONTEXT | - | 유지 |
| Fig.2-14 disease progression | Figure | T p.39 | INCLUDED_AS_CONTEXT | - | 유지 |
| Fig.2-15 moxifloxacin resistance | Figure/dataset | T p.39 | INCLUDED_AS_CONTEXT | - | 유지 |
| Relating Response to Exposure | H2 | T p.40 | INCLUDED_AS_MUST | - | 유지 |
| Graded Response | H3 | T p.40–42 | INCLUDED_AS_MUST | - | 유지 |
| Eq.2-4 Hill | Formula | T p.40 | INCLUDED_AS_MUST | - | 유지 |
| Fig.2-16 gamma curves | Figure | T p.41 | INCLUDED_AS_MUST | - | View pointer ESSENTIAL |
| Fig.2-17 propranolol | Figure/dataset | T p.42 | INCLUDED_AS_MUST | - | 유지 |
| Quantal Response | H3 | T p.41–43 | INCLUDED_AS_CONTEXT | - | 유지 |
| Fig.2-18 alfentanil | Figure/dataset | T p.42 | INCLUDED_AS_MUST | - | 유지 |
| Desirable Characteristics | H3 | T p.43 | INCLUDED_AS_CONTEXT weak | MISSING_BRIDGE | potency/Emax/specificity balance 1문장 |
| Dose-Time-Response Relationships | H2 | T p.43–44 | OMITTED_PROBLEMATIC | MISSING_BRIDGE | SHOULD_FIX |
| Fig.2-19 exposure profile scenarios | Figure | T p.44 | OMITTED_PROBLEMATIC | MISSING_EXAMPLE | SHOULD_FIX |
| Turnover Concepts in Drug Response | H2 | T p.44–46 | INCLUDED_AS_MUST | - | 유지 |
| Eq.2-5/2-6/2-7 turnover formulas | Formulas | T p.45 | INCLUDED_AS_MUST | - | 유지 |
| Fig.2-20 total body water | Figure/dataset | T p.45 | INCLUDED_AS_MUST | - | 유지 |
| Closing transition to next section | Concluding message | T p.46 | OMITTED_JUSTIFIABLE | Low | 필요 없음 |
| Key Relationships | Box summary | T p.47 | INCLUDED_AS_CONTEXT mostly | MISSING_BRIDGE minor | Eq.52:1/Fig2-19만 보강 |
| Study Problems | Exercises | T p.47–49 | PARTLY via Q7 | OMITTED_JUSTIFIABLE | Optional |
| Fig.2-21 AF-DX116 | Study problem figure | T p.48 | OMITTED_JUSTIFIABLE | Low | Optional |
| Fig.2-22 hepatic toxicity vs AUC | Study problem figure | T p.48–49 | OMITTED_JUSTIFIABLE | Low/Medium | Optional |

---

## T6: Figure Inventory & Learning Value Audit

| Figure/Table | Page | Teaches | Value | View Instruction? | Redraw/New Schematic? | Inspection Method | Rationale |
|---|---:|---|---|---|---|---|---|
| G Fig.1.1 | G p.4 | Modeling Carousel의 6단계 순환 구조 | ESSENTIAL | YES | YES | VISUAL_INSPECTED | 세션 Apex 구조 자체이므로 learner가 시각적으로 확인해야 함 |
| G Fig.1.2 | G p.6 | initial estimate와 local/global minimum의 관계 | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Draft의 주요 오류가 이 figure 해석에서 발생하므로 직접 보기 필요 |
| T Fig.1-1 | T p.4 | empirical dose regimen feedback | USEFUL | YES | NO | VISUAL_INSPECTED | rational PK/PD 접근과 대비되는 출발점 |
| T Fig.1-2 | T p.5 | dosage regimen→exposure→effect의 rational approach | ESSENTIAL | YES | YES | VISUAL_INSPECTED | PK/PD chain의 기본 구조 |
| T Fig.1-3 | T p.5 | conc-time + conc-effect가 effect-time을 만든다는 linkage | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M2의 핵심 시각 자료 |
| T Fig.1-4 | T p.6 | therapeutic response/adverse effects 사이의 window | ESSENTIAL | YES | YES | VISUAL_INSPECTED | therapeutic window 개념의 직접 그림 |
| T Fig.1-5 | T p.7 | repeated dosing accumulation and plateau | USEFUL | YES | YES | VISUAL_INSPECTED | digoxin loading/maintenance 논리를 보강 |
| T Fig.1-6 | T p.8 | warfarin concentration-response time delay | ESSENTIAL | YES | NO | VISUAL_INSPECTED | M4 turnover/response delay의 핵심 dataset |
| T Fig.1-7 | T p.8 | paclitaxel leukopenia delayed nadir/recovery | USEFUL | YES | NO | VISUAL_INSPECTED | indirect response 예시로 유용 |
| T Fig.1-8 | T p.10 | phenytoin dose vs concentration variability | USEFUL | YES | NO | VISUAL_INSPECTED | narrow-window variability 설명에 도움 |
| T Fig.1-9 | T p.10 | warfarin maintenance variability vs S-warfarin | USEFUL | YES | NO | VISUAL_INSPECTED | variability/covariate 논의 보강 |
| T Fig.1-10 | T p.12 | adherence decline over 1 year | ESSENTIAL | YES | NO | VISUAL_INSPECTED | adherence가 exposure 이전 단계라는 메시지 강화 |
| T Fig.1-11 | T p.13 | prescribed regimen→adherence→exposure→effects | USEFUL | YES | YES | VISUAL_INSPECTED | Fig.1-2의 real-world 확장 |
| T Fig.1-12 | T p.14 | digital medicine system for adherence monitoring | USEFUL | NO | NO | VISUAL_INSPECTED | 현대 사례이나 핵심 chain은 텍스트로 충분 |
| T Fig.1-13 | T p.15 | drug development process and PK/PD roles | USEFUL | NO | NO | VISUAL_INSPECTED | industrial perspective 보강용 |
| T Table 2-1 | T p.20 | PK/PD applications in drug therapy | USEFUL | NO | NO | VISUAL_INSPECTED | 목적론 요약표 |
| T Table 2-2 | T p.21 | plasma/serum/whole-blood differences | USEFUL | YES | NO | VISUAL_INSPECTED | measurement matrix 이해에 도움 |
| T Fig.2-1 | T p.22 | exposure-time profile, Cmax, tmax | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Cmax/tmax/AUC 정의의 기본 figure |
| T Fig.2-2 | T p.23 | stereoisomer exposure differences | USEFUL | YES | NO | VISUAL_INSPECTED | assay specificity/PK-PD relation 왜곡 설명 |
| T Fig.2-3 | T p.25 | parent-metabolite exposure profiles | USEFUL | YES | NO | VISUAL_INSPECTED | active metabolite/prodrug 맥락 강화 |
| T Fig.2-4 | T p.26 | systemic absorption barriers and sites of loss | USEFUL | YES | YES | VISUAL_INSPECTED | first-pass/systemic absorption 이해에 도움 |
| T Table 2-3 | T p.27 | extravascular routes of administration | USEFUL | NO | NO | VISUAL_INSPECTED | route terminology 보조표 |
| T Fig.2-5 | T p.28 | mass balance model compartments | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Eq.2-1의 구조적 배경 |
| T Fig.2-6 | T p.29 | time course of mass balance compartments | USEFUL | YES | NO | VISUAL_INSPECTED | Eq.2-2의 동적 직관 제공 |
| T Fig.2-7 | T p.30 | equation/physiologic/compartmental model types | USEFUL | YES | YES | VISUAL_INSPECTED | 모델 유형 vocabulary bridge |
| T Fig.2-8 | T p.31 | ADME and disposition definitions | ESSENTIAL | YES | YES | VISUAL_INSPECTED | PK terminology skeleton |
| T Fig.2-9 | T p.31–32 | oral route barriers/systemic absorption | USEFUL | YES | YES | VISUAL_INSPECTED | first-pass loss 설명에 유용 |
| T Fig.2-10 | T p.33 | enterohepatic cycle | USEFUL | YES | NO | VISUAL_INSPECTED | enterohepatic cycling의 anatomy |
| T Fig.2-11 | T p.35 | ketamine graded concentration-response | ESSENTIAL | YES | NO | VISUAL_INSPECTED | M3 Hill/Emax anchor |
| T Fig.2-12 | T p.37 | montelukast/placebo/baseline response | USEFUL | YES | NO | VISUAL_INSPECTED | Eq.2-3 이해에 도움 |
| T Fig.2-13 | T p.38 | prednisone and Duchenne disease progression | USEFUL | YES | NO | VISUAL_INSPECTED | symptomatic relief vs disease modification |
| T Fig.2-14 | T p.39 | cure/stabilization/symptomatic relief schema | USEFUL | YES | YES | VISUAL_INSPECTED | disease progression taxonomy |
| T Fig.2-15 | T p.39 | moxifloxacin resistance emergence | USEFUL | YES | NO | VISUAL_INSPECTED | response deterioration over time |
| T Fig.2-16 | T p.41 | Hill γ effect on curve steepness | ESSENTIAL | YES | YES | VISUAL_INSPECTED | γ의 의미를 시각적으로 이해하는 핵심 figure |
| T Fig.2-17 | T p.42 | propranolol Hill fit using unbound concentration | ESSENTIAL | YES | NO | VISUAL_INSPECTED | real data anchor for Eq.2-4 |
| T Fig.2-18 | T p.42 | alfentanil quantal response by surgery group | ESSENTIAL | YES | NO | VISUAL_INSPECTED | graded vs quantal 구분의 핵심 figure |
| T Fig.2-19 | T p.44 | Cmax/tmax/AUC importance depends on clinical objective | USEFUL | YES | YES | VISUAL_INSPECTED | Draft에서 빠진 중요한 bridge figure |
| T Fig.2-20 | T p.45 | total body water turnover | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M4 turnover 수치 anchor |
| T Fig.2-21 | T p.48 | AF-DX116 concentration-response exercise | USEFUL | NO | NO | VISUAL_INSPECTED | Study problem; optional self-test source |
| T Fig.2-22 | T p.48 | hepatic toxicity incidence vs AUC | USEFUL | NO | NO | VISUAL_INSPECTED | Study problem; exposure metric selection 예시 |

---

## Patch Memo Cross-check

| Patch Memo Item | Independent Audit Classification | Decision |
|---|---|---|
| Phase 1 v0는 구조적으로 좋지만 최적본은 아님 | MATCH | 본 audit와 동일 |
| MUST 4개 선정은 적절 | MATCH | 유지 |
| 실제 수치 anchor 대체로 충실 | MATCH | 일부 오류만 패치 |
| “반드시 local minimum”, “AUC 30–50%” 과장 | MATCH | MUST_FIX |
| CONTEXT 일부가 1–2문장보다 길다 | OPTIONAL | Source fidelity 오류는 아니나 워크플로우 규칙상 편집 필요 |
| Regulatory/NDA 표현은 source와 inference 분리 필요 | MATCH | MUST_FIX |
| Figure direct embedding 금지/Phase 4C 주의 | MATCH | T6 결과와 호환 |
| Step 2 HTML 전 Phase 2 필요 | MATCH | 본 audit 수행 완료 후 패치 권장 |

---

## Final Action Gate

**Go to Phase 3/HTML?**  
아직 **No-Go for HTML direct compile**.  
**Go after patch**가 적절하다.

**필수 패치 최소 세트**:

1. M1 overclaim 문장 완화: local minimum “위험”으로 표현.
2. AUC 30–50%, OFV>5, 4개 initial estimates, COV/Hessian, launch delay/수백억/FDA-EMA 단정 삭제 또는 태그 분리.
3. G Fig.1.2 설명 정정: yellow initial estimates vs red final estimates; WRSS/objective function.
4. M2 digoxin/morphine “50배” 삭제.
5. CYP2C9·VKORC1 오류 정정.
6. G Eq. predicted concentration, T Fig.2-1 numeric anchor, T Fig.2-19 bridge 추가.
7. Source / interpretation / practical inference / educational scenario 태그 분리.

**최종 판정**: **조건부 PASS, Source Fidelity 7.2/10. 패치 후 8.5/10 이상 가능.**

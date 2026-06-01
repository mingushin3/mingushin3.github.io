# 07_Content Lock v2 — Session 07
## 치료역·항정상태·다중투여·축적

**Role lock**: Editor-in-Chief — pharmacometrics specialist.  
**Output type**: Markdown text-final lock.  
**Scope**: §1 → §2 → §5 → §7 → §8 only.  
**Figure handling**: No figure markers inserted; T6 Figure Inventory flows to Phase 4C unchanged.

## Pass 1 — Edit Log Summary

| Location (§ + card) | Edit type | Before (excerpt) | After (excerpt) |
|---|---|---|---|
| Curation Map M2 | R1 | 목표 농도 수준이 얼마든 접근 시간은 half-life의 함수다.… | 목표 plateau 수준이 높든 낮든 접근 시간표는 half-life의 함수다.… |
| Curation Map M4 | R4 | `Cav,ss`와 `Aav,ss`를 등치하지 말라. 농도는 `CL`, amount는 `MRT`를 통해 표현된다.… | `Cav,ss`와 `Aav,ss`를 등치하지 말라. 농도는 `CL`, amount는 `MRT`를 거쳐 표현된다.… |
| §1 Master Lens | R1 + Type A | 이 세션의 핵심은 **항정상태를 세 개의 독립 질문으로 분해하는 능력**이다.… | 이 세션의 핵심은 **항정상태를 하나의 숫자가 아니라 세 개의 독립 질문으로 분해하는 능력**이다.  <!-- ANNOTATION --> 항정상태(st… |
| §1 Master Lens | R1/R2 | R&T Fig. 11-3의 메시지는 이 분리를 가장 잘 보여준다. 같은 average dosing rate라면 average … | R&T Fig. 11-3의 메시지는 이 분리를 가장 잘 보여준다. 같은 average dosing rate라면 average amount의 platea… |
| §2-M1 What to remember | R2/R3 | Maintenance dosing의 첫 문장은 “target concentration × clearance”이다. 목표 $C_… | Maintenance dosing을 시작할 때 먼저 묻는 것은 “target concentration × clearance”이다. 목표 $C_{ss}$… |
| §2-M2 Big Idea | R2 | 정속 주입이든 다중투여든 plateau 접근 속도는 **elimination half-life**가 정한다. 1 half-li… | 정속 주입이든 다중투여든 plateau 접근 속도는 **elimination half-life**가 정한다. 즉, 목표 plateau가 높든 낮든 “몇… |
| §2-M3 Big Idea | R5 + Type A | 다중투여 accumulation은 새 dose가 들어올 때 이전 dose의 잔여량이 얼마나 남아 있는지의 문제다. 1차 선형계… | 다중투여 accumulation은 새 dose가 들어올 때 이전 dose의 잔여량이 얼마나 남아 있는지의 문제다.  <!-- ANNOTATION -->… |
| §2-M3 Three-dominator lock | R2 | R&T의 200 mg/day 예시는 average dosing rate가 같으면 average amount의 접근 시간은 같고… | R&T의 200 mg/day 예시는 average dosing rate가 같으면 average amount의 접근 시간은 같다는 점을 보여준다. 달라지… |
| §2-M4 Big Idea | R1 + Type A | 이 세션의 가장 위험한 오류는 **average concentration**과 **average amount**를 같은 식으로… | 이 세션에서 가장 위험한 오류는 **average concentration**과 **average amount**를 같은 식으로 쓰는 것이다.  <!-… |
| §2-M4 Why this matters | R2 | $C_{av,ss}$는 clinical target, TDM interpretation, exposure-response 분석… | $C_{av,ss}$는 clinical target, TDM interpretation, exposure-response 분석의 언어다. 반면 $A_{… |

**Pass 1 v1.5 status**: sentence-level polish를 반영한 중간본을 생성했고, 길이 제한 때문에 전문 중복은 생략한다. 아래 Content Lock v2는 v1.5에 Pass 2 annotation을 반영한 최종본이다.

## Pass 2 — Annotation Candidate Table

| Type | Location (§ + card) | Current text | Proposed annotation | Risk |
|---|---|---|---|---|
| Type A | Curation Map M1 | `CL` | `CL`(← 단위 시간당 제거되는 용적) | Low |
| Type A | §1 Master Lens | 항정상태 | 항정상태(steady state)(← 입력률과 제거률이 같아진 상태) | Low |
| Type A | §2-M3 | accumulation factor | 단회 투여 대비 plateau 증가비 | Low |
| Type A | §2-M4 | average concentration / amount | 단위 차이 gloss | Low |
| Type A | §2-M5 | Flip-flop | 흡수가 제거보다 느린 상태 | Low |
| Type A | §2-M6 | formalization | 개념을 계산식 형태로 표현 | Low |
| Type A | §2-M7 | loading / maintenance dose | 초기 목표 도달 vs 반복 유지 | Low |

## Pass 2 — Final Recommendation List

**Must annotate**: CL, steady state, accumulation factor, average concentration vs amount, Flip-flop, formalization, loading/maintenance dose.  
**Optional included**: therapeutic window gloss in Curation Map M6.  
**Do not annotate**: equations, source page tags, NONMEM flags, daptomycin and phenobarbital numerical locks, adjudication rows.

---


## Adjudication Table Summary

### A. Audit v1 — item-level verdicts

| Source | Item | Verdict | Rationale |
|---|---|---|---|
| Audit T1 | T1-01: `dC/dt = Rin/V - (Cl/V)·C` | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-02: `C(t)=Rin/Cl[1-exp(-(Cl/V)t)]` | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-03: `Css = Rin/Cl` | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-04: “Clearance is sole parameter determining maintenance dose / Css target” | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-05: `Cpost = (Rin/Cl)(1-exp(-Cl/V·Tinf)) exp(-Cl/V·t')` | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-06: `ln[(Css-C)/Css] = -Kt` | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-07: Infusion-to-bolus intercept relation `CI ↔ C0`, Eq.2:27–2:31 | PARTIAL_ADOPT | 정확한 라벨과 조건을 분리해 반영. |
| Audit T1 | T1-08: 1 half-life → 50%; 2 → 75%; 3 → 87.5/88%; 3–4 t1/2 → ~90% | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-09: `3.32 half-lives = 90%` | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-10: `5 half-lives ≈ 97%`, `6 ≈ 98%`, `7 ≈ 99%` | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-11: `MRT = Ass/Rinf = 1/k = 1.443·t1/2 = V/CL` | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-12: Eptifibatide example: `Css 1 mg/L`, `CL 4 L/hr`, `V 14.3 L`, `k 0.28 hr^-1`, `t1/2 2.5 hr`, `Rinf 4 mg/h… | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-13: t-PA half-life `5 min`, plateau in `17 min` | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-14: `R = Cmax,ss/Cmax,1 = 1/(1-e^{-Kτ})` | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-15: `R = 1/(1-2^{-τ/t1/2})` | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-16: “R depends on half-life and dosing interval; independent of dose” | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-17: `Cav,ss = F·Dose/(CL·τ)` | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-18: **Curation Map**: `Css,avg = F·Dose/(τ·CL) = AUC/τ = 1.443·F·Dose·t1/2/τ` | ADOPT | MUST_FIX로 교정 반영: `Cav,ss = F·Dose/(CL·τ)`; `Aav,ss = 1.44·F·Dose·t1/2/τ`; only 1-compartment with known V gives `Cav,ss=Aav,ss… |
| Audit T1 | T1-19: `Aav,ss = 1.443·F·Dose·t1/2/τ` | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-20: `AUC0-τ,ss = F·Dose/CL`, `Cav,ss = AUC0-τ,ss/τ` | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-21: `ka < k ⇒ terminal slope = ka` flip-flop | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-22: Oral one-site equation `C(t)=kaFD/[V(ka-k)](e^{-kt}-e^{-ka t})` | PARTIAL_ADOPT | 원문이 참조하는 범위까지만 유지하고 [확인 필요] 성격 보존. |
| Audit T1 | T1-23: Two-site absorption `Frct`, `ka,rapid`, `ka,delayed` | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-24: `Amax,N`, `Amin,N`, `Amax,ss`, `Amin,ss`, Eq.11-1~11-4 | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-25: `Amax,N/Amax,ss = Amin,N/Amin,ss = 1-e^{-kNτ}` | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-26: `Amax,ss - Amin,ss = Dose` for IV bolus at plateau | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-27: Table 11-1 values: 200 mg q24h x 5 days; 49h total 14.4, 73h 14.87, 97h 15.04 | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-28: Table 11-1 derived `t1/2=16.7 hr`, `V=20 L`, `Cmax,ss=15.82 mg/L`, `Cmin,ss=5.82 mg/L` | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-29: Phenobarbital: `t1/2=4 days`, `100 mg q24h`, 4d=50%, 8d=75%, 24d=98% | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-30: Phenobarbital: `R=5.8` | ADOPT | MUST_FIX로 교정 반영: If meaning average accumulation, write `Aav,ss/Dose≈5.76`; if meaning `Rac`, correct to `≈6.3`. |
| Audit T1 | T1-31: `DM = DL(1-e^{-kτ})`, `DL = DM/(1-e^{-kτ}) = Rac·DM` | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-32: Doxycycline: `t1/2=24 hr`, `DL=200 mg`, `DM=100 mg/day`, `Rac=2` | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-33: Sirolimus: `t1/2=2.5 days`, `DL=6 mg`, `DM=2 mg/day`; draft says theoretical `R=4.13`, theoretical DL `8… | PARTIAL_ADOPT | 정확한 라벨과 조건을 분리해 반영. |
| Audit T1 | T1-34: Table 11-3 TI × t1/2 matrix values | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-35: `τmax = ln(Cupper/Clower)/k = 1.44·t1/2·ln(Cupper/Clower)` | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-36: `DM,max = (V/F)(Cupper-Clower)` | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-37: `Css,av = (Cupper-Clower)/ln(Cupper/Clower)` | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-38: `DM = (DM,max/τmax)τ`, `DL=DM/(1-e^{-kτ})` | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-39: Fig.11-10 example: TW 5–10 mg/L, V=20 L, t1/2=46 hr, k=0.015 hr^-1, τmax=46 hr, DMmax=100 mg, 2.17 mg/hr… | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-40: Self-test example: TW 4–12, V=50, F=0.8, t1/2=12 → τmax≈19h, DMmax=500 mg, τ=12h, DM≈316→300 mg, DL=600 … | REJECT | NOT_IN_SOURCE 항목이므로 본문에서 삭제. |
| Audit T1 | T1-41: `U(C)=Σw_iP_i(C)`, sample weights `+0.4`, `-0.2`, `-1.0`, `Uthreshold=0.10` | PARTIAL_ADOPT | 수식은 교육적 formalization으로 라벨링하고, source-derived 식으로 쓰지 않음. |
| Audit T1 | T1-42: Phenytoin 10–20 mg/L; gentamicin peak 5–8/trough 1–2 | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-43: Phenytoin toxicity levels: nystagmus ~20+, ataxia ~30, mental changes 40+ mg/L | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-44: Atorvastatin `t1/2=14 hr`, PD max 3–4 weeks | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-45: Erythropoietin `t1/2=9 hr`, hematocrit plateau ~70 days | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-46: Acquired resistance = mutation/cell population; tolerance = PD adaptation; tachyphylaxis acute tolerance… | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-47: `AUC/MIC >101`: 9% resistant; `<100`: only 50% susceptible after 5 days | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-48: `AUC/MIC target 35` for fluoroquinolone/Pseudomonas respiratory infection | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-49: Daptomycin Study A: 25 mg/kg q24h vs 25 mg/kg q8h “same daily dose” | ADOPT | MUST_FIX로 교정 반영: Same daily dose comparison is `75 mg/kg q24h` vs `25 mg/kg q8h`; `25 q24h` vs `25 q8h` is same dose per admin… |
| Audit T1 | T1-50: Daptomycin Study A CPK: 25 q24h 994 U/L; 75 q24h 991; 25 q8h 3996 | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-51: Daptomycin Study B: same Cmax 58 µg/mL; AUC 180 vs 412; CPK 157 vs 483 | ADOPT | PDF 근거와 일치. |
| Audit T1 | T1-52: “q24h CPK no change, q12h CPK increase in healthy volunteers; FDA-approved once-daily label; 4–6 mg/kg I… | REJECT | NOT_IN_SOURCE 항목이므로 본문에서 삭제. |
| Audit T1 | T1-53: Trench Tip: pump/catheter issue probability `30–40%` | REJECT | NOT_IN_SOURCE 항목이므로 본문에서 삭제. |
| Audit T1 | T1-54: SS=1 misuse → `AUC 30–80%` overprediction → Phase 3 SAE → NDA refusal | REJECT | NOT_IN_SOURCE 항목이므로 본문에서 삭제. |
| Audit T1 | T1-55: `FDA Clinical Pharmacology Section`, `NDA 표준`, `Deficiency Letter` | REJECT | NOT_IN_SOURCE 항목이므로 본문에서 삭제. |
| Audit T1 | T1-56: Cardarone-X fictional case: t1/2=4h, V=100L, F=0.6, TW[1,4], q6h vs q8h redesign | PARTIAL_ADOPT | 가상 연습 문제로 명시 라벨링할 때만 유지. |
| Audit T2 | G constant infusion, Fig.2.8 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | G steady-state definition and deconvolution statement | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | G input functions: bolus, zero-order, first-order, multiple zero-/first-order, log+zero-order | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | G multiple dosing accumulation, Fig.2.28 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | G accumulation factor Eq.2:75–2:78 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | G flip-flop Fig.2.29 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | G repeated dosing Fig.2.30, drug half-life 7h → 21–28h | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | G multiple absorption sites Fig.2.31 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | G PK11 two-compartment repeated oral dosing | PARTIAL_ADOPT | 핵심 메시지만 1–2문장으로 압축해 반영. |
| Audit T2 | G PK13 bolus + constant infusion | ADOPT | HIGH anchor로 §2-M7에 수치 반영. |
| Audit T2 | R&T Ch.9 dosage regimen determinants, Fig.9-1 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | R&T Fig.9-2 dose-response cohort example placebo/10/20/40 mg | PARTIAL_ADOPT | 핵심 메시지만 1–2문장으로 압축해 반영. |
| Audit T2 | R&T Fig.9-3 therapeutic effectiveness/utility curves | ADOPT | 오류를 교정한 형태로 본문에 반영. |
| Audit T2 | R&T Fig.9-4 poor dose-response due to PK variability | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | R&T Fig.9-5 poor systemic exposure-response cases | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | R&T Fig.9-6 phenytoin escalation | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | R&T Table 9-1 selected concentration ranges | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | R&T Fig.9-7 mutant selection window | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | R&T Table 9-2 probabilities | REJECT | 학습 핵심도가 낮거나 연습문제 성격이므로 제외. |
| Audit T2 | R&T Appendix I telescoping derivation/table I-1/I-2 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | R&T Ch.10 IV infusion drug examples Table 10-1 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | R&T Ch.10 devices Tables 10-2/10-3 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | R&T Ch.10 eptifibatide example | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | R&T Ch.10 t-PA Fig.10-6 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | R&T Ch.10 furosemide Fig.10-11 | PARTIAL_ADOPT | 핵심 메시지만 1–2문장으로 압축해 반영. |
| Audit T2 | R&T Ch.10 turnover examples Table 10-5, Fig.10-12~10-18 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | R&T Ch.10 PK/PD indices Fig.10-20/10-21/10-22 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | R&T Ch.10 physiologic changes Table 10-6/Fig.10-19 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | R&T Ch.10 nifedipine/droperidol/rolipram study problems | REJECT | 학습 핵심도가 낮거나 연습문제 성격이므로 제외. |
| Audit T2 | R&T Ch.11 superposition Table 11-1/Fig.11-1 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | R&T Ch.11 IV bolus accumulation Fig.11-2 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | R&T Ch.11 phenobarbital Table 11-2 | ADOPT | 오류를 교정한 형태로 본문에 반영. |
| Audit T2 | R&T Ch.11 Fig.11-3 frequency independence | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | R&T Ch.11 doxycycline Fig.11-4 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | R&T Ch.11 Table 11-3 TI × t1/2 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | R&T Ch.11 amoxicillin/naproxen/piroxicam Tables 11-4/11-5; Figs 11-5~11-7 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | R&T Ch.11 extravascular Figs 11-8/11-9 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | R&T Ch.11 TW algorithm Fig.11-10/Eq.11-14~11-22 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | R&T Ch.11 clobazam Fig.11-12 | PARTIAL_ADOPT | single-dose AUC→plateau 예시로 1문장 반영. |
| Audit T2 | R&T Ch.11 modified release morphine Fig.11-13 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | R&T Ch.11 evaluation Fig.11-14/Eq.11-23~25 | PARTIAL_ADOPT | 핵심 메시지만 1–2문장으로 압축해 반영. |
| Audit T2 | R&T Ch.11 PD-driven dosing Fig.11-15; atenolol/morphine | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | R&T Ch.11 atorvastatin Fig.11-16 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | R&T Ch.11 erythropoietin Fig.11-17 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | R&T Ch.11 onset/duration/intensity Fig.11-18 | PARTIAL_ADOPT | 핵심 메시지만 1–2문장으로 압축해 반영. |
| Audit T2 | R&T Ch.11 acquired resistance/tolerance | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | R&T Ch.11 Fig.11-19 ceftazidime/gentamicin | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | R&T Ch.11 Fig.11-20 AUC/MIC resistance | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | R&T Ch.11 altered absorption/disposition Figs.11-22/11-23 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T2 | R&T Ch.11 daptomycin Fig.11-24/Table11-7 | ADOPT | 오류를 교정한 형태로 본문에 반영. |
| Audit T2 | R&T Ch.11 study problems Tables 11-8~11-12 | REJECT | 학습 핵심도가 낮거나 연습문제 성격이므로 제외. |
| Audit T3 | Constant infusion concentration rises to plateau; 1 t1/2=50%, 3–4 t1/2≈90%. | ADOPT | 핵심 저자 메시지로 유지. |
| Audit T3 | `Css = Rin/Cl`; clearance controls maintenance dosing to keep target Css. | ADOPT | 핵심 저자 메시지로 유지. |
| Audit T3 | Steady state means rate in equals rate out; for discrete dosing, equivalent profiles recur over interval… | ADOPT | 핵심 저자 메시지로 유지. |
| Audit T3 | Steady state is not thermodynamic equilibrium, although the book uses the terms interchangeably. | PARTIAL_ADOPT | 정정 또는 1문장 압축 반영. |
| Audit T3 | Accumulation factor depends on half-life and dosing interval, not dose. | ADOPT | 핵심 저자 메시지로 유지. |
| Audit T3 | Time to 90% steady state depends only on half-life; average steady-state concentration depends on dosing… | ADOPT | 핵심 저자 메시지로 유지. |
| Audit T3 | Flip-flop: when absorption is rate-limiting, terminal slope reflects absorption. | ADOPT | 핵심 저자 메시지로 유지. |
| Audit T3 | Multiple peaks after extravascular dosing do not necessarily mean enterohepatic recirculation. | ADOPT | 핵심 저자 메시지로 유지. |
| Audit T3 | Dosage regimens optimize therapy by balancing harm risk and achievable benefit. | ADOPT | 핵심 저자 메시지로 유지. |
| Audit T3 | Exposure-response data are often limited; therapeutic window may be defined clinically by dose rather th… | PARTIAL_ADOPT | 정정 또는 1문장 압축 반영. |
| Audit T3 | Poor systemic exposure-response relationships can occur and must be diagnosed. | PARTIAL_ADOPT | 정정 또는 1문장 압축 반영. |
| Audit T3 | All substances produce harm if given high enough amounts. | REJECT | 핵심 handout 기준 필수성이 낮음. |
| Audit T3 | Constant-rate IV input is precise and can be stopped instantly; institutional limitation exists. | REJECT | 핵심 handout 기준 필수성이 낮음. |
| Audit T3 | Plateau amount depends on infusion rate and k; plateau concentration depends on infusion rate and cleara… | ADOPT | 핵심 저자 메시지로 유지. |
| Audit T3 | Approach to a new plateau, higher or lower, depends only on half-life. | ADOPT | 핵심 저자 메시지로 유지. |
| Audit T3 | After stopping infusion, concentration falls by half each half-life; some transdermal systems decline sl… | PARTIAL_ADOPT | 정정 또는 1문장 압축 반영. |
| Audit T3 | Multiple-dose concentration profile can be predicted by superposition of the single-dose profile without… | ADOPT | 핵심 저자 메시지로 유지. |
| Audit T3 | Plateau during discrete dosing is not constant within interval; values at the same time in the interval … | ADOPT | 핵심 저자 메시지로 유지. |
| Audit T3 | Extent of accumulation is frequency relative to half-life; accumulation itself is not an intrinsic label… | ADOPT | 핵심 저자 메시지로 유지. |
| Audit T3 | Same average dosing rate gives same approach time to plateau; dosing interval changes fluctuation. | ADOPT | 핵심 저자 메시지로 유지. |
| Audit T3 | Loading dose rationale: immediate plateau; for some drugs loading is omitted/divided to avoid acute toxi… | ADOPT | 핵심 저자 메시지로 유지. |
| Audit T3 | Design of regimen can be based on `Cupper`, `Clower`, `t1/2`, `V`, `F`; choose practical interval/dose s… | ADOPT | 핵심 저자 메시지로 유지. |
| Audit T3 | PD can govern time to plateau effect more than PK; statins and erythropoietin are examples. | ADOPT | 핵심 저자 메시지로 유지. |
| Audit T3 | Acquired resistance and tolerance are distinct mechanisms of declining effectiveness. | ADOPT | 핵심 저자 메시지로 유지. |
| Audit T3 | Daptomycin toxicity depends on dose fractionation/recovery time, not simply Cmax or AUC24. | PARTIAL_ADOPT | 정정 또는 1문장 압축 반영. |
| Audit T3 | Patients vary; next section covers individualization. | REJECT | 핵심 handout 기준 필수성이 낮음. |
| Audit T4 | 1. M4 Curation Map: concentration equation equated to amount equation | ADOPT | 우선순위 MUST_FIX에 따라 본문에 교정/압축 반영. |
| Audit T4 | 2. Daptomycin Study A “same daily dose” comparison | ADOPT | 우선순위 MUST_FIX에 따라 본문에 교정/압축 반영. |
| Audit T4 | 3. Phenobarbital `R=5.8` as accumulation index | ADOPT | 우선순위 MUST_FIX에 따라 본문에 교정/압축 반영. |
| Audit T4 | 4. Unsupported numerical/regulatory chains: `30–40%`, `AUC 30–80%`, `SAE`, `NDA refusal`, `Deficiency Lette… | ADOPT | 우선순위 MUST_FIX에 따라 본문에 교정/압축 반영. |
| Audit T4 | 5. `FDA Clinical Pharmacology Section`, `NDA standard language` as if source-derived | ADOPT | 우선순위 MUST_FIX에 따라 본문에 교정/압축 반영. |
| Audit T4 | 6. `U(C)` weighted utility formula and sample weights | PARTIAL_ADOPT | 우선순위 SHOULD_FIX에 따라 본문에 교정/압축 반영. |
| Audit T4 | 7. PK13 source anchor underused | PARTIAL_ADOPT | 우선순위 SHOULD_FIX에 따라 본문에 교정/압축 반영. |
| Audit T4 | 8. G p.25 steady state vs equilibrium nuance | PARTIAL_ADOPT | 우선순위 SHOULD_FIX에 따라 본문에 교정/압축 반영. |
| Audit T4 | 9. R&T Ch.11 clobazam Fig.11-12 underused | PARTIAL_ADOPT | 우선순위 SHOULD_FIX에 따라 본문에 교정/압축 반영. |
| Audit T4 | 10. Overdense M6/M7/M8 repeated regulatory phrasing | PARTIAL_ADOPT | 우선순위 SHOULD_FIX에 따라 본문에 교정/압축 반영. |
| Audit T4 | 11. Study problems and peripheral tables not integrated | REJECT | OPTIONAL로 분류되어 제외 또는 가상 라벨로만 제한. |
| Audit T4 | 12. Extra fictional Cardarone-X case | REJECT | 출처 라벨 없이 유지 불가. |
| Audit T4 | 13. Patch memo’s “Phase 1 redo 불필요 / Phase 2로 진행” | REJECT | OPTIONAL로 분류되어 제외 또는 가상 라벨로만 제한. |
| Audit T5-A | G §2.2.2 Constant rate infusion | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | G §2.2.3 Integration of clearance and volume | REJECT | 범위 밖이거나 연습문제 성격이라 제외 정당. |
| Audit T5-A | G §2.2.9 How does input to the plasma compartment vary? | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | G §2.2.10 Multiple dosing | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | G §2.2.11 Absorption from multiple sites | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | G Case Study PK11 — Two-compartment repeated oral dosing | PARTIAL_ADOPT | 핵심 메시지만 1–2문장으로 압축해 반영. |
| Audit T5-A | G Case Study PK13 — Bolus plus constant infusion | PARTIAL_ADOPT | 핵심 메시지만 1–2문장으로 압축해 반영. |
| Audit T5-A | R&T Ch.9 Objectives | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | R&T Ch.9 Dosage Regimens | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | R&T Ch.9 Therapeutic Exposure | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | R&T Ch.9 Therapeutic Index | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | R&T Ch.9 Additional Considerations | REJECT | 범위 밖이거나 연습문제 성격이라 제외 정당. |
| Audit T5-A | R&T Ch.9 Achieving Therapeutic Goals | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | R&T Ch.9 Study Problems | REJECT | 범위 밖이거나 연습문제 성격이라 제외 정당. |
| Audit T5-A | R&T Appendix I Accumulation | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | R&T Ch.10 Objectives/opening | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | R&T Ch.10 constant-rate devices/tables | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | R&T Ch.10 Exposure-time relationships | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | R&T Ch.10 The Plateau Value | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | R&T Ch.10 Mean Residence Time | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | R&T Ch.10 Time to Reach Plateau | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | R&T Ch.10 Postinfusion | PARTIAL_ADOPT | 핵심 메시지만 1–2문장으로 압축해 반영. |
| Audit T5-A | R&T Ch.10 Bolus plus Infusion | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | R&T Ch.10 Pharmacodynamics | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | R&T Ch.10 Turnover of Affected Systems | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | R&T Ch.10 Influences on Kinetics and Pharmacodynamics | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | R&T Ch.10 Study Problems | REJECT | 범위 밖이거나 연습문제 성격이라 제외 정당. |
| Audit T5-A | R&T Ch.11 Objectives/opening | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | R&T Ch.11 Principles of Drug Accumulation | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | R&T Ch.11 Maxima and Minima on Accumulation to Plateau | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | R&T Ch.11 Average Level at Plateau | ADOPT | M4 차원 오류 교정으로 반영. |
| Audit T5-A | R&T Ch.11 Rate of Accumulation to Plateau | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | R&T Ch.11 Accumulation Index | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | R&T Ch.11 Relationship Between Initial and Maintenance Doses | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | R&T Ch.11 Maintenance of Drug in Therapeutic Range | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | R&T Ch.11 Reinforcing the Principles | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | R&T Ch.11 Extravascular Considerations | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | R&T Ch.11 Design of Dosage Regimens Using Plasma Concentration | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | R&T Ch.11 Modified-Release Products | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | R&T Ch.11 Evaluation of a Multiple-Dose Regimen | PARTIAL_ADOPT | 핵심 메시지만 1–2문장으로 압축해 반영. |
| Audit T5-A | R&T Ch.11 Pharmacodynamic Considerations | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | R&T Ch.11 When Absorption or Disposition is Altered | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-A | R&T Ch.11 Other Situations and closing transition to individualization | REJECT | 범위 밖이거나 연습문제 성격이라 제외 정당. |
| Audit T5-A | R&T Ch.11 Study Problems | REJECT | 범위 밖이거나 연습문제 성격이라 제외 정당. |
| Audit T5-B | G Eq.2:19–2:23 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-B | G Eq.2:24–2:26 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-B | G Eq.2:27–2:31 | REJECT | 범위 밖이거나 연습문제 성격이라 제외 정당. |
| Audit T5-B | G Eq.2:75–2:78 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-B | G Eq.2:79 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-B | R&T Eq.10-1–10-4 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-B | R&T Eq.10-5–10-8 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-B | R&T Eq.10-9–10-11 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-B | R&T Eq.10-12~10-16 turnover equations | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-B | R&T Eq.11-1–11-4 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-B | R&T Eq.11-5–11-8 | ADOPT | M4 차원 오류 교정으로 반영. |
| Audit T5-B | R&T Eq.11-9–11-10 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-B | R&T Eq.11-11–11-13 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-B | R&T Eq.11-14–11-22 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-B | R&T Eq.11-23–11-25 | PARTIAL_ADOPT | 핵심 메시지만 1–2문장으로 압축해 반영. |
| Audit T5-B | Appendix I Eq.I-1~I-10 | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-C | Time to approach plateau depends only on half-life | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-C | Plateau level/concentration is determined by input rate and CL/k, not by half-life alone | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-C | Average rate determines average plateau; dosing interval controls fluctuation | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-C | Single-dose profile can predict repeated-dose profile by superposition | ADOPT | 근거와 학습가치가 충분하여 유지. |
| Audit T5-C | PD response may not follow PK plateau time | ADOPT | 근거와 학습가치가 충분하여 유지. |

### B. Crucible v1 — actionable item verdicts

| Source | Item | Verdict | Rationale |
|---|---|---|---|
| Crucible T3 | Tip-1: SS=1 Phantom Plateau Bias 진단 [STAGE 1] | ADOPT | 실무 trench tip으로 해당 카드 또는 혼동쌍에 압축 반영. |
| Crucible T3 | Tip-2: PK13 Bolus+Infusion IC 코딩 [STAGE 1] | ADOPT | 실무 trench tip으로 해당 카드 또는 혼동쌍에 압축 반영. |
| Crucible T3 | Tip-3: Aav,ss vs Cav,ss 차원 분리 [STAGE 1, Audit MUST_FIX 1] | ADOPT | 실무 trench tip으로 해당 카드 또는 혼동쌍에 압축 반영. |
| Crucible T3 | Tip-4: PK11 Sequential Fitting 의미 [STAGE 1] | ADOPT | 실무 trench tip으로 해당 카드 또는 혼동쌍에 압축 반영. |
| Crucible T3 | Tip-5: Therapeutic Concentration Range vs Therapeutic Window 분리 [STAGE 2] | ADOPT | 실무 trench tip으로 해당 카드 또는 혼동쌍에 압축 반영. |
| Crucible T3 | Tip-6: Phantom Metabolite Bias 진단 [STAGE 2] | PARTIAL_ADOPT | 길이 증가 없이 context/self-test 수준으로 제한. |
| Crucible T3 | Tip-7: Extraction Ratio 기반 DDI 패턴 즉각 판독 [STAGE 3] | ADOPT | 실무 trench tip으로 해당 카드 또는 혼동쌍에 압축 반영. |
| Crucible T3 | Tip-8: Antimicrobial PK/PD Index → Continuous Infusion 정당화 [STAGE 3] | ADOPT | 실무 trench tip으로 해당 카드 또는 혼동쌍에 압축 반영. |
| Crucible T3 | Tip-9: Tolerance 두 sub-mechanism 분리 진단 [STAGE 3] | ADOPT | 실무 trench tip으로 해당 카드 또는 혼동쌍에 압축 반영. |
| Crucible T3 | Tip-10 [STAGE 4 신설]: Daptomycin Translational Pattern — Cmax-AUC-Fractionation 3변수 분리 | ADOPT | 실무 trench tip으로 해당 카드 또는 혼동쌍에 압축 반영. |
| Crucible T4 | D-1: §2-M3 C-2 Plausible Fallacy 4단계 *AUC 30-80% 정량 chain* — DELETE (Audit T1-54). 1문장으로 압축: *"[교과서 외 실무 해석] SS=1 부적절 적용 시 C… | PARTIAL_ADOPT | D-1 지시에 따라 삭제·라벨링·압축 또는 정정 적용. |
| Crucible T4 | D-2: §2-M4 Curation Map M4 행 핵심 수식 — REPLACE (Audit MUST_FIX 1). 차원 분리 명시: *$C_{av,ss} = F \cdot Dose/(CL \cdot \tau) = AUC_… | ADOPT | D-2 지시에 따라 삭제·라벨링·압축 또는 정정 적용. |
| Crucible T4 | D-3: §2-M3 Phenobarbital R=5.8 표기 — FIX (Audit MUST_FIX 3 + STAGE 4 PDF 검증). **STAGE 4 PDF 직접 확인된 R&T 자체의 내적 모순 명시 필수**: *"R… | ADOPT | D-3 지시에 따라 삭제·라벨링·압축 또는 정정 적용. |
| Crucible T4 | D-4: §2-M6 *U(C) = Σwᵢ·Pᵢ(C)* 수식 — RELABEL (Audit MUST_FIX 5 + STAGE 2 부분 정정). *수식 표기 = 교육적 formalization*, *가중치 값 (+0.4, −0… | PARTIAL_ADOPT | D-4 지시에 따라 삭제·라벨링·압축 또는 정정 적용. |
| Crucible T4 | D-5: §2-M3 4단계 보강 Phenobarbital 블록 — COMPRESS. *τ/t½=0.25 → R 큼 + plateau slow* 메시지가 §5-쌍4 와 본질 중복. 1-2문장으로 압축: *"Phenobarbi… | PARTIAL_ADOPT | D-5 지시에 따라 삭제·라벨링·압축 또는 정정 적용. |
| Crucible T4 | D-6: §2-M6 4단계 보강 PD-Driven Plateau 블록 (atorvastatin) — COMPRESS. *PK 시계 ≠ PD 시계* 인사이트는 EPO 사례 (RBC lifespan-driven, 70-day … | PARTIAL_ADOPT | D-6 지시에 따라 삭제·라벨링·압축 또는 정정 적용. |
| Crucible T4 | D-7: §7 Q11-E Daptomycin Study A 비교 — FIX (Audit MUST_FIX 2 + STAGE 4 PDF Table 11-7 직접 검증). *"Study A: 75 mg/kg q24h vs 25 … | ADOPT | D-7 지시에 따라 삭제·라벨링·압축 또는 정정 적용. |
| Crucible T4 | D-8: §7 Q-BD (f) Cardarone-X — RELABEL (Audit T1-56 NOT_IN_SOURCE). *[가상 케이스 — M8 알고리즘 적용 연습용. R&T·G 직접 등재 약물 아님]* 라벨링. | PARTIAL_ADOPT | D-8 지시에 따라 삭제·라벨링·압축 또는 정정 적용. |
| Crucible T4 | D-9: §8C Professional Moat 응결 진술 — COMPRESS (Audit T1-55). *"FDA Clinical Pharmacology Section"* 표현 1회 이내 사용, *"규제 언어"* → *"… | PARTIAL_ADOPT | D-9 지시에 따라 삭제·라벨링·압축 또는 정정 적용. |
| Crucible T4 | D-10: §2-M3 C-2 Plausible Fallacy GOF 시그니처 — KEEP. *Phantom Plateau* 시그니처 패턴 (IPRED-DV, η-shrinkage, η_Cl vs N) 보존. 단 *NDA 거부… | ADOPT | D-10 지시에 따라 삭제·라벨링·압축 또는 정정 적용. |
| Crucible T4 | D-11: §2-M6 utility 수식 라벨링 — REPLACE (D-4 정정). *"수식 표기 vs 가중치 값 분리 라벨링"*. | ADOPT | D-11 지시에 따라 삭제·라벨링·압축 또는 정정 적용. |
| Crucible T4 | D-12: §2-M6 *Therapeutic Concentration Range vs Therapeutic Window* — SEPARATE. 두 용어 분리 정의 (Tip-5 의 insert text). | ADOPT | D-12 지시에 따라 삭제·라벨링·압축 또는 정정 적용. |
| Crucible T4 | D-13: §5-쌍5 (TW vs TI) Critical Blow 행 — INSERT. *"NDA section 6.2 또는 12 에서 *wide TW* 를 *high TI* 함의로 사용 시 — 모집단 기준 안전성 진술이 개… | ADOPT | D-13 지시에 따라 삭제·라벨링·압축 또는 정정 적용. |
| Crucible T4 | D-14: §2-M3 §3 Structural Isomorphism Map *이중 도출 일치* 진술 — FIX. STAGE 2 PDF 검증 결과 Appendix I (p.795-796) 도출은 *telescoping* 이 아… | ADOPT | D-14 지시에 따라 삭제·라벨링·압축 또는 정정 적용. |
| Crucible T4 | D-15: §2-M6 Single-Dose Therapy 부정 사례 — ADD 1 sentence. *"본 세션 식의 적용 범위 한계: M3 R, M4 Cav,ss, M7 DL/DM, M8 알고리즘 은 *만성 다중투여 + 약… | PARTIAL_ADOPT | D-15 지시에 따라 삭제·라벨링·압축 또는 정정 적용. |
| Crucible T4 | D-16: §5-쌍5 Therapeutic Index 정의 — DUAL DEFINITION. *전임상 TI: TD₅₀/ED₅₀ (모집단 dose-response 비율) | 임상 TI (R&T p.278): individual… | ADOPT | D-16 지시에 따라 삭제·라벨링·압축 또는 정정 적용. |
| Crucible T4 | D-17: §2-M6 R&T Ch.9 영역 — COMPRESS. *MUST 보존*: TW vs Therapeutic Concentration Range 분리, utility 가중치 임의성, R&T p.276 trough vs… | PARTIAL_ADOPT | D-17 지시에 따라 삭제·라벨링·압축 또는 정정 적용. |
| Crucible T4 | D-18: §2-M6 또는 §5-쌍7 Nicotine Tachyphylaxis 진술 — REFINE. *"R&T Fig 10-17: 25 µg/min/kg, 30-min infusion, 두 차례 투여 간격 1·2·3.5 h… | PARTIAL_ADOPT | D-18 지시에 따라 삭제·라벨링·압축 또는 정정 적용. |
| Crucible T4 | D-19: §5-쌍7 Tolerance 행 — DUAL SUB-MECHANISM. *"Receptor-level (R&T Fig 10-17 nicotine, concentration-effect curve 우로 이동) vs … | ADOPT | D-19 지시에 따라 삭제·라벨링·압축 또는 정정 적용. |
| Crucible T4 | D-20: §5-쌍6 (MRT vs t½) — *MOMENT-BASED* 정의 명시. *"Multi-compartment 일반화: $MRT = AUMC_{0-\infty}/AUC_{0-\infty}$ (moment-based… | PARTIAL_ADOPT | D-20 지시에 따라 삭제·라벨링·압축 또는 정정 적용. |
| Crucible T4 | D-21: §2-M6 또는 §8C — *Drug A-D DDI 4-패턴 카드* 신설. *"DDI 위험도 분류 변수: hepatic extraction ratio (ER) | 4-패턴: Low ER + inhibition (C… | PARTIAL_ADOPT | D-21 지시에 따라 삭제·라벨링·압축 또는 정정 적용. |
| Crucible T4 | D-22: §5-쌍1 Critical Blow 또는 §5-쌍7 — *Furosemide Bolus vs Infusion* 추가 anchor. *"Furosemide bolus vs infusion (R&T Fig 10-11,… | PARTIAL_ADOPT | D-22 지시에 따라 삭제·라벨링·압축 또는 정정 적용. |
| Crucible T4 | D-23: §2-M3 또는 §2-M4 Big Idea 블록 — *3차원 분리* 응결 신설. *"항정상태 도달 시간은 t½ 단독, 평균 농도는 CL 단독, fluctuation 진폭은 τ/t½ 단독 — 다중 투여의 *세 지배자… | PARTIAL_ADOPT | D-23 지시에 따라 삭제·라벨링·압축 또는 정정 적용. |
| Crucible T4 | D-24: §2-M3 Phenobarbital 블록 — *PDF 자체의 내적 모순* 명시. STAGE 4 PDF 직접 검증 결과: *"R&T p.326 본문은 'the accumulation index is 5.8' 명시하지… | PARTIAL_ADOPT | D-24 지시에 따라 삭제·라벨링·압축 또는 정정 적용. |
| Crucible T4 | D-25: §2-M7 또는 §6 시나리오 — *Daptomycin Translational Pattern* 신설. *"R&T p.350-353 Table 11-7 (Oleson et al. 2000): Study A 의 동일… | PARTIAL_ADOPT | D-25 지시에 따라 삭제·라벨링·압축 또는 정정 적용. |
| Crucible T4 | D-26: §2-M6 PD-Driven Plateau — *Bisphosphonate parallel* 1문장 추가. *"Bisphosphonate (alendronate, R&T p.343): statin 과 동일 패턴 —… | PARTIAL_ADOPT | D-26 지시에 따라 삭제·라벨링·압축 또는 정정 적용. |
| Crucible T4 | D-27: §2-M6 또는 §8 — *Single-Dose vs Multiple-Dose BE Convergence* 신설. *"R&T Fig 11-9 (p.333) 의 핵심: '단일 dose 에서 보이는 absorption… | PARTIAL_ADOPT | D-27 지시에 따라 삭제·라벨링·압축 또는 정정 적용. |
| Crucible T4 | D-28: §2-M6 또는 §6 시나리오 — *Modified-Release Intentional Flip-flop* 1문장. *"R&T Fig 11-13 Morphine MR (p.337): t½=2hr 임에도 once-d… | PARTIAL_ADOPT | D-28 지시에 따라 삭제·라벨링·압축 또는 정정 적용. |
| Crucible T4 | D-29: §6 시나리오 또는 §7 Q-BD — *Onset/Duration/Intensity 2차 dose 패러다임* 신설. *"R&T Fig 11-18 (p.345): biomarker-driven dosing (anes… | PARTIAL_ADOPT | D-29 지시에 따라 삭제·라벨링·압축 또는 정정 적용. |
| Crucible T5 | **A1** M4 Curation Map 차원 분리 | ADOPT | Grade A 핵심 항목으로 반영. |
| Crucible T5 | **A2** Phenobarbital 5.8 vs 6.3 *PDF 자체 내적 모순* 명시 | ADOPT | Grade A 핵심 항목으로 반영. |
| Crucible T5 | **A3** Daptomycin Study A 비교 수정 (25/25 → 75/25) | ADOPT | Grade A 핵심 항목으로 반영. |
| Crucible T5 | **A4** M3 Plausible Fallacy 정량 chain 삭제 | ADOPT | Grade A 핵심 항목으로 반영. |
| Crucible T5 | **A5** "U(C)" 수식 표기 vs 가중치 값 분리 라벨링 | ADOPT | Grade A 핵심 항목으로 반영. |
| Crucible T5 | **A6** SS=1 Phantom Plateau Bias 명명 + Trench | ADOPT | Grade A 핵심 항목으로 반영. |
| Crucible T5 | **A7** "FDA Clinical Pharmacology Section" 반복 압축 | ADOPT | Grade A 핵심 항목으로 반영. |
| Crucible T5 | **A8** Therapeutic Concentration Range vs Therapeutic Window 분리 | ADOPT | Grade A 핵심 항목으로 반영. |
| Crucible T5 | **A9** §5-쌍5 Critical Blow 행 신설 | ADOPT | Grade A 핵심 항목으로 반영. |
| Crucible T5 | **A10** §5-쌍5 TI dual 정의 | ADOPT | Grade A 핵심 항목으로 반영. |
| Crucible T5 | **A11** Drug A-D DDI 4-패턴 카드 신설 | ADOPT | Grade A 핵심 항목으로 반영. |
| Crucible T5 | **A12** §5-쌍7 Tolerance dual sub-mechanism | ADOPT | Grade A 핵심 항목으로 반영. |
| Crucible T5 | **A13** 🆕 STAGE 4 **3차원 분리 (timing × level × amplitude) Big Idea 격상** | ADOPT | Grade A 핵심 항목으로 반영. |
| Crucible T5 | **A14** 🆕 STAGE 4 **Daptomycin Translational Pattern + NDA section 13 Trigger-8** | PARTIAL_ADOPT | Daptomycin 수치 패턴은 채택, NDA 단정은 삭제. |
| Crucible T5 | **B1** PK13 IC 코딩 anchor | PARTIAL_ADOPT | 문서 길이를 늘리지 않는 범위에서 압축 반영. |
| Crucible T5 | **B2** PK11 sequential fitting → PK 시계 = PD 시계 단순 케이스 | PARTIAL_ADOPT | 문서 길이를 늘리지 않는 범위에서 압축 반영. |
| Crucible T5 | **B3** M2·M3·M4 통합 변수로 MRT | PARTIAL_ADOPT | 문서 길이를 늘리지 않는 범위에서 압축 반영. |
| Crucible T5 | **B4** Loading Inflation Cascade 명명 | PARTIAL_ADOPT | 문서 길이를 늘리지 않는 범위에서 압축 반영. |
| Crucible T5 | **B5** §5-쌍1 Critical Blow "3중 위험" P3 확장 | PARTIAL_ADOPT | 문서 길이를 늘리지 않는 범위에서 압축 반영. |
| Crucible T5 | **B6** Phenobarbital 블록 압축 | PARTIAL_ADOPT | 문서 길이를 늘리지 않는 범위에서 압축 반영. |
| Crucible T5 | **B7** Atorvastatin 블록 압축 | PARTIAL_ADOPT | 문서 길이를 늘리지 않는 범위에서 압축 반영. |
| Crucible T5 | **B8** Pattern-4: TW Asymmetry Recognition | PARTIAL_ADOPT | 문서 길이를 늘리지 않는 범위에서 압축 반영. |
| Crucible T5 | **B9** "이중 도출" → "동일 도출의 두 표기" 정정 | PARTIAL_ADOPT | 문서 길이를 늘리지 않는 범위에서 압축 반영. |
| Crucible T5 | **B10** Single-Dose Therapy 부정 사례 | PARTIAL_ADOPT | 문서 길이를 늘리지 않는 범위에서 압축 반영. |
| Crucible T5 | **B11** Phantom Metabolite Bias 명명 | PARTIAL_ADOPT | 문서 길이를 늘리지 않는 범위에서 압축 반영. |
| Crucible T5 | **B12** t_t = 1.443·t½ turnover system 일반화 | PARTIAL_ADOPT | 문서 길이를 늘리지 않는 범위에서 압축 반영. |
| Crucible T5 | **B13** §5-쌍6 MRT *moment-based* 정의 + Mono-compartment Bias | PARTIAL_ADOPT | 문서 길이를 늘리지 않는 범위에서 압축 반영. |
| Crucible T5 | **B14** Furosemide bolus vs infusion 동일 용량 다른 효과 | PARTIAL_ADOPT | 문서 길이를 늘리지 않는 범위에서 압축 반영. |
| Crucible T5 | **B15** Antimicrobial Continuous Infusion 정당화 | PARTIAL_ADOPT | 문서 길이를 늘리지 않는 범위에서 압축 반영. |
| Crucible T5 | **B16** Modified-release 임상 합리성 PD 메커니즘 분리 | PARTIAL_ADOPT | 문서 길이를 늘리지 않는 범위에서 압축 반영. |
| Crucible T5 | **B17** 🆕 STAGE 4 **Bisphosphonate ≈ statin parallel (long-term-only C-response)** | PARTIAL_ADOPT | 문서 길이를 늘리지 않는 범위에서 압축 반영. |
| Crucible T5 | **B18** 🆕 STAGE 4 **Single-Dose vs Multiple-Dose BE Convergence (Fig 11-9 anchor)** | PARTIAL_ADOPT | 문서 길이를 늘리지 않는 범위에서 압축 반영. |
| Crucible T5 | **B19** 🆕 STAGE 4 **Modified-Release Intentional Flip-flop (Morphine MR Fig 11-13)** | PARTIAL_ADOPT | 문서 길이를 늘리지 않는 범위에서 압축 반영. |
| Crucible T5 | **B20** 🆕 STAGE 4 **Onset/Duration/Intensity Fig 11-18 (anesthesia titration)** | PARTIAL_ADOPT | 문서 길이를 늘리지 않는 범위에서 압축 반영. |
| Crucible T5 | C1 "FDA Clinical Pharmacology Section" 표현 추가 확장 | REJECT | Grade C로 분류되어 제외. |
| Crucible T5 | C2 Cardarone-X 가상 케이스 추가 확장 | REJECT | Grade C로 분류되어 제외. |
| Crucible T5 | C3 atorvastatin·EPO 양쪽 detailed 진술 | REJECT | Grade C로 분류되어 제외. |
| Crucible T5 | C4 "NDA 거부", "Deficiency Letter" immediate consequence claim | REJECT | Grade C로 분류되어 제외. |
| Crucible T5 | C5 "AUC 30-80%" unsupported numerical bound | REJECT | Grade C로 분류되어 제외. |
| Crucible T5 | C6 Figure 추가 분석 (Phase 4C 영역) | REJECT | Grade C로 분류되어 제외. |
| Crucible T5 | C7 NONMEM control stream 직접 작성 (Step 2 영역) | REJECT | Grade C로 분류되어 제외. |
| Crucible T5 | C8 R&T Ch.10 Constant-Rate Devices Table 10-2/10-3 상세 진술 | REJECT | Grade C로 분류되어 제외. |
| Crucible T5 | C9 Erythropoietin epoetin alfa PK 파라미터 detailed cite (V=4 L/70kg, CL=0.5 L/hr/70kg, t½=5.8 hr) | REJECT | Grade C로 분류되어 제외. |
| Crucible T5 | C10 Propofol 3-pool model (Fig 10-10) detailed 진술 | REJECT | Grade C로 분류되어 제외. |
| Crucible T5 | C11 🆕 STAGE 4 **Table 11-3 의 모든 약물 클래스 detailed 진술** — Step 1 §2-M8 이 이미 TW-driven algorithm 으로 다룸; Table 11-3 의 *나열식* … | REJECT | Grade C로 분류되어 제외. |
| Crucible T5 | C12 🆕 STAGE 4 **Adinazolam·Mefloquine 같은 R&T Study Problems 의 detailed 풀이** — Step 1 §7 자기 테스트 영역 외 | REJECT | Grade C로 분류되어 제외. |
| Crucible T5 | C13 🆕 STAGE 4 **Cancer chemo intermittent administration (paclitaxel cycle) 의 PK 파라미터 detailed cite** — §2-M6 의 PD-driv… | REJECT | Grade C로 분류되어 제외. |
---

## Updated Curation Map (MUST / CONTEXT)

### MUST — 10분 handout에 반드시 남길 개념

| ID | 개념 | 핵심 잠금 문장 | 핵심 수식 / anchor | Source tag |
|---|---|---|---|---|
| M1 | 정속 주입 plateau 농도 | 항정상태 농도 수준은 `t1/2`가 아니라 `CL`(← 단위 시간당 제거되는 용적)이 정한다. | $C_{ss}=R_{in}/CL$ | [G p.23; R&T p.288] |
| M2 | plateau 도달 시간 | 목표 plateau 수준이 높든 낮든 접근 시간표는 half-life의 함수다. | $C(t)=C_{ss}(1-e^{-Kt})$; 1, 2, 3, 3–4 half-lives ≈ 50%, 75%, 87.5%, ≈90% | [G pp.22–23; R&T pp.290–292] |
| M3 | 다중투여 accumulation factor | 축적 정도는 dose가 아니라 $\tau/t_{1/2}$가 정한다. | $R_{ac}=1/(1-e^{-K\tau})=1/(1-2^{-\tau/t_{1/2}})$ | [G pp.43–45; R&T pp.322–326; R&T pp.795–797] |
| M4 | 평균 plateau: concentration vs amount 분리 | `Cav,ss`와 `Aav,ss`를 등치하지 말라. 농도는 `CL`, amount는 `MRT`를 거쳐 표현된다. | $C_{av,ss}=F\text{Dose}/(CL\tau)$; $A_{av,ss}=1.44F\text{Dose}t_{1/2}/\tau$; 1-compartment에서만 $C_{av,ss}=A_{av,ss}/V$ | [G p.45; R&T p.324; R&T p.337] |
| M5 | Flip-flop | terminal slope가 elimination이 아니라 absorption을 말할 수 있다. | $K_a<K$이면 terminal slope ≈ $K_a$ | [G pp.45–46; R&T pp.332–334, 337–338] |
| M6 | Therapeutic Window | TW는 “좋은 농도 범위”가 아니라 benefit과 harm의 balance를 농도 축 위에 투영한 의사결정 구간이다. | therapeutic window(← benefit–harm balance의 농도 구간)와 therapeutic concentration range 구별; TI는 전임상 ratio와 임상 exposure sensitivity가 다름 | [R&T pp.267–281] |
| M7 | Loading + maintenance | plateau를 기다리지 않고 목표 근처에서 시작하려면 loading dose가 필요하고, 유지에는 average input rate가 필요하다. | $D_M=D_L(1-e^{-K\tau})$; $D_L=R_{ac}D_M$; bolus+infusion anchor | [R&T pp.293–295; R&T pp.326–329; G pp.537–539] |
| M8 | TW-driven dosage design | `Cupper`, `Clower`, `t1/2`, `V`, `F`가 있으면 interval과 dose의 상한을 계산할 수 있다. | $\tau_{max}=1.44t_{1/2}\ln(C_{upper}/C_{lower})$; $D_{M,max}=(V/F)(C_{upper}-C_{lower})$ | [R&T pp.334–337] |
| M9 | PD-driven plateau | effect plateau는 drug PK plateau보다 늦을 수 있다. 무엇의 half-life인지 먼저 물어야 한다. | atorvastatin: PK $t_{1/2}=14$ h, PD plateau 3–4 weeks; erythropoietin: PK $t_{1/2}=9$ h, hematocrit plateau ≈70 days | [R&T pp.341–345] |
| M10 | Dose fractionation toxicity | 같은 daily dose라도 fractionation이 recovery time을 바꾸면 toxicity가 달라진다. | Daptomycin Study A: 75 mg/kg q24h vs 25 mg/kg q8h, CPK 991 vs 3996 U/L | [R&T pp.351–353] |

### CONTEXT — 유지하되 1–2문장 이상 확장하지 않을 항목

| ID | Context item | Lock decision | Source tag |
|---|---|---|---|
| C1 | Steady state vs thermodynamic equilibrium | 용어를 엄밀히 분리하되 독립 카드로 확장하지 않음. | [G p.25] |
| C2 | Input function taxonomy | bolus, zero-order, first-order, multiple input을 “입력 함수가 달라지면 concentration-time profile이 달라진다” 수준으로만 유지. | [G p.43] |
| C3 | Multiple absorption sites | multiple peaks가 곧 enterohepatic recirculation을 의미하지 않는다는 주의만 유지. | [G p.46] |
| C4 | PK11 | PK clock = PD clock의 단순 anchor로만 사용. | [G pp.528–531] |
| C5 | PK13 | bolus+infusion IC coding anchor로 사용. | [G pp.537–539] |
| C6 | Constant-rate devices | infusion 원리 확장 예시로만 유지. | [R&T pp.284–286] |
| C7 | Post-infusion decline | infusion 중단 후 concentration은 half-life에 따라 감소하되, extravascular continued input은 예외가 될 수 있음. | [R&T p.291] |
| C8 | Clobazam single-dose AUC | single-dose AUC로 plateau average를 예측할 수 있다는 1문장 anchor. | [R&T p.336] |
| C9 | Modified release | intentional flip-flop의 임상 활용으로 morphine MR, leuprolide depot만 짧게 유지. | [R&T pp.337–338] |
| C10 | Regimen evaluation | fluctuation, relative bioavailability, renal clearance는 evaluation context로만 유지. | [R&T pp.339–341] |
| C11 | DDI patterns | ER 중심 4패턴만 유지; protein binding 단독 논리 금지. | [R&T pp.309–310; R&T pp.350–351] |
| C12 | Study problems | 본문에는 통합하지 않음; §7에서 가상/응용 문항으로만 사용 가능. | [R&T pp.353–358] |

---

# §1 — Session Header & Roadmap

<!-- MASTER LENS -->
## 1. Master Lens

이 세션의 핵심은 **항정상태를 하나의 숫자가 아니라 세 개의 독립 질문으로 분해하는 능력**이다.

<!-- ANNOTATION -->
항정상태(steady state)(← 입력률과 제거률이 같아진 상태)는 “도달했는가/얼마인가/얼마나 출렁이는가”를 따로 물어야 한다.

1. **언제 도달하는가?** → $t_{1/2}$가 정한다.
2. **평균 수준은 어디인가?** → $CL$과 평균 입력속도가 정한다.
3. **얼마나 출렁이는가?** → $\tau/t_{1/2}$가 정한다.

R&T Fig. 11-3의 메시지는 이 분리를 가장 잘 보여준다. 같은 average dosing rate라면 average amount의 plateau 접근 시간 경로는 같다. 그러나 dosing interval이 길수록 fluctuation은 커진다 [R&T p.325]. 이 분리를 이해하면 `SS=1`, `ADDL/II`, loading dose, maintenance dose, therapeutic window 기반 regimen design을 같은 구조로 읽을 수 있다.

<!-- ANCHOR -->
## 2. Roadmap

- **M1–M2**: 정속 주입에서 `CL`은 plateau level, `t1/2`는 approach time을 결정한다.
- **M3–M4**: 다중투여에서 accumulation과 average plateau를 계산한다. 이때 `amount`와 `concentration`의 차원을 분리해야 한다.
- **M5**: absorption이 느리면 terminal slope가 elimination을 말하지 않는다.
- **M6**: therapeutic window는 PK 식의 결과가 아니라 clinical utility의 제약조건이다.
- **M7–M8**: loading/maintenance와 TW-driven algorithm은 위 분리를 실제 dosing regimen으로 변환한다.

<!-- RECAP -->
**Session Lock**: 항정상태는 “시간=t½, 수준=CL, 진폭=τ/t½”의 세 축으로 잠근다. 이 세 축을 섞는 순간 NONMEM steady-state coding, TDM adjustment, loading dose rationale, therapeutic-window design이 동시에 흐려진다.

---

# §2 — Concept Anatomy Cards

## §2-M1. 정속 주입 항정상태 농도: $C_{ss}=R_{in}/CL$

<!-- MASTER LENS -->
### Big Idea

정속 주입에서 plateau concentration은 **얼마나 빨리 없어지는가(CL)**와 **얼마나 빨리 넣는가($R_{in}$)**의 균형이다. Volume은 초기 상승 곡선의 속도를 바꾸지만, plateau 농도의 높이를 직접 결정하지 않는다 [G p.23; R&T p.288].

### Source-locked equations

$$\frac{dC}{dt}=\frac{R_{in}}{V}-\frac{CL}{V}C$$

$$C(t)=\frac{R_{in}}{CL}\left(1-e^{-(CL/V)t}\right)$$

$$C_{ss}=\frac{R_{in}}{CL}$$

### What to remember

Maintenance dosing을 시작할 때 먼저 묻는 것은 “target concentration × clearance”이다. 목표 $C_{ss}$를 맞추려면 $R_{in}$을 조정하고, 환자의 $CL$ 변화를 반영해야 한다. $V$는 loading이나 onset의 문제로 이동한다.

<!-- TRENCH -->
**Trench-Level Tip**: infusion 중 관찰 농도가 기대 plateau보다 낮다고 해서 곧바로 CL 증가로 해석하지 않는다. 먼저 actual input rate, line interruption, sampling time, infusion stop/start 기록을 확인한다. 교과서가 보증하는 것은 $C_{ss}=R_{in}/CL$ 구조이지, 특정 현장 오류의 빈도 숫자가 아니다.

<!-- RECAP -->
**Recap**: steady-state concentration의 지배자는 clearance다. Half-life는 plateau까지 가는 시간의 지배자다.

---

## §2-M2. 항정상태 도달 시간: 3–4 $t_{1/2}$ 규칙

<!-- MASTER LENS -->
### Big Idea

정속 주입이든 다중투여든 plateau 접근 속도는 **elimination half-life**가 정한다. 즉, 목표 plateau가 높든 낮든 “몇 %까지 접근했는가”의 시간표는 half-life로 움직인다. 1 half-life 후 50%, 2 half-lives 후 75%, 3 half-lives 후 87.5%, 3–4 half-lives 후 약 90%에 도달한다 [G p.22; R&T pp.290–292].

### Source-locked equation

$$C(t)=C_{ss}(1-e^{-Kt})$$

도달률은 $1-e^{-Kt}$이며, $K=\ln2/t_{1/2}$이다. 90% 도달 시간은 $t=\ln(10)/K\approx3.32t_{1/2}$이다 [R&T p.291].

### Practical interpretation

`t1/2`가 2.5시간인 eptifibatide는 plateau에 비교적 빨리 접근하고, `t1/2`가 5분인 t-PA는 약 17분이면 90% 수준에 접근한다 [R&T pp.288–293]. 반대로 phenobarbital처럼 $t_{1/2}=4$ days이면 plateau 접근 자체가 느리다 [R&T pp.324–325].

<!-- ANCHOR -->
**Bridge to NONMEM**: steady-state assumption은 “평균적으로 충분히 오래 투여했다”는 시간 조건이다. `SS=1`을 쓰기 전에 실제 투여 이력이 최소 3–4 half-lives 이상인지 먼저 확인한다.

<!-- RECAP -->
**Recap**: target level이 바뀌어도 approach fraction의 시간표는 half-life로 움직인다.

---

## §2-M3. Apex Concept — 다중투여 축적인자 $R_{ac}=1/(1-e^{-K\tau})$

<!-- MASTER LENS -->
### Big Idea

다중투여 accumulation은 새 dose가 들어올 때 이전 dose의 잔여량이 얼마나 남아 있는지의 문제다.

<!-- ANNOTATION -->
accumulation factor(← 단회 투여 대비 plateau 증가비)는 농도값 자체가 아니라 반복 투여가 만든 배율이다.

1차 선형계에서 이전 dose의 잔여 비율은 $e^{-K\tau}$이고, 무한 반복하면 등비수열 합으로 닫힌 형태가 된다 [G pp.43–45; R&T pp.795–797].

### Source-locked equation

$$R_{ac}=\frac{1}{1-e^{-K\tau}}=\frac{1}{1-2^{-\tau/t_{1/2}}}$$

이 식은 dose가 들어가지 않는다. 축적 정도는 `dose size`가 아니라 **dose interval relative to half-life**가 정한다 [G pp.44–45; R&T pp.325–326].

<!-- ANCHOR -->
### Three-dominator lock

- **Timing**: plateau 접근 시간 = $t_{1/2}$.
- **Level**: average plateau concentration = $CL$과 average input rate.
- **Amplitude**: peak-trough fluctuation과 accumulation factor = $\tau/t_{1/2}$.

R&T의 200 mg/day 예시는 average dosing rate가 같으면 average amount의 접근 시간은 같다는 점을 보여준다. 달라지는 것은 dosing interval이 길어질수록 커지는 fluctuation이다 [R&T p.325].

### Phenobarbital label lock

Phenobarbital 예시는 “slow half-life + short interval”이 큰 accumulation과 느린 plateau approach를 만든다는 좋은 anchor다. 단, 라벨을 분리해야 한다. R&T는 $t_{1/2}=4$ days, 100 mg q24h 사례에서 본문상 accumulation index 5.8을 언급하지만, Eq. 11-3/11-10의 peak/trough accumulation index로 계산하면 $A_{max,ss}/Dose=630/100\approx6.3$이다. 5.8은 $A_{av,ss}/Dose\approx5.76$에 해당하는 average accumulation ratio로 이해해야 한다 [R&T pp.324–326].

<!-- TRENCH -->
**Trench-Level Tip — Phantom Plateau Bias**: 투여 시작 직후 자료에 `SS=1`을 부적절하게 적용하면 observed rising limb를 이미 plateau인 것처럼 강제로 설명하게 된다. 이때 CL, bioavailability, interindividual variability 추정이 연쇄적으로 왜곡될 수 있다. 수치적 손상률이나 제출 실패 같은 외부 단정은 본문에서 삭제한다.

<!-- RECAP -->
**Recap**: accumulation factor는 dose 독립, $\tau/t_{1/2}$ 의존이다. Dose를 키우면 level이 올라가지만, accumulation ratio 자체가 바뀌지는 않는다.

---

## §2-M4. 항정상태 평균농도와 평균 amount: $C_{av,ss}$ vs $A_{av,ss}$

<!-- MASTER LENS -->
### Big Idea

이 세션에서 가장 위험한 오류는 **average concentration**과 **average amount**를 같은 식으로 쓰는 것이다.

<!-- ANNOTATION -->
average concentration(← 용적당 평균 농도)과 average amount(← 체내 평균 약물량)는 단위부터 다르다.

R&T는 두 식을 분리한다 [R&T p.324; R&T p.337].

### Source-locked equations

$$C_{av,ss}=\frac{AUC_{0-\tau,ss}}{\tau}=\frac{F\cdot Dose}{CL\cdot\tau}$$

$$A_{av,ss}=\frac{1.44\cdot F\cdot Dose\cdot t_{1/2}}{\tau}$$

첫 식의 단위는 concentration이고, 두 번째 식의 단위는 amount다. 1-compartment에서 $MRT=V/CL=1.44t_{1/2}$가 성립할 때만 $C_{av,ss}=A_{av,ss}/V$로 연결된다 [R&T p.289; R&T p.324]. Multi-compartment에서는 amount-to-concentration 변환이 모델 구조에 의존한다.

<!-- ANCHOR -->
### Why this matters

$C_{av,ss}$는 clinical target, TDM interpretation, exposure-response 분석의 언어다. 반면 $A_{av,ss}$는 body burden과 residence time의 언어다. 따라서 둘을 섞으면 “농도 목표”와 “체내 amount”의 차원이 무너진다.

### Example anchors

- Table 11-1의 200 mg q24h 예시는 single-dose profile을 superposition(← 단회 투여 곡선을 시간 이동해 더함)하여 repeated-dose profile을 예측할 수 있음을 보여준다 [R&T pp.320–321].
- Clobazam 예시는 single-dose AUC와 dosing interval로 average plateau concentration을 예측하는 논리를 보강한다 [R&T p.336].
- Amoxicillin, naproxen, piroxicam 예시는 half-life와 dosing interval이 fluctuation과 accumulation을 어떻게 바꾸는지 비교한다 [R&T pp.330–332].

<!-- RECAP -->
**Recap**: $C_{av,ss}$는 $CL$ 기반 농도식, $A_{av,ss}$는 $MRT$ 기반 amount식이다. 두 식은 차원이 다르다.

---

## §2-M5. Flip-flop 동태: $K_a<K$일 때 terminal slope의 정체

<!-- MASTER LENS -->
### Big Idea

Extravascular dosing에서 terminal slope는 항상 elimination을 의미하지 않는다.

<!-- ANNOTATION -->
Flip-flop(← 흡수가 제거보다 느린 상태)에서는 말단 기울기의 해석 주체가 elimination에서 absorption으로 바뀐다.

흡수가 더 느리면 terminal phase는 absorption-limited phase가 된다 [G pp.45–46].

### Source-locked relation

$$K_a<K \Rightarrow \text{terminal slope}\approx K_a$$

일반적인 경우는 $K_a>K$이고 terminal slope가 $K$를 반영한다. Flip-flop에서는 terminal half-life가 길어 보이지만, 그것은 drug elimination이 느리다는 뜻이 아니라 absorption input이 오래 지속된다는 뜻일 수 있다.

<!-- ANCHOR -->
### Clinical asymmetry

Modified-release products와 depot formulations는 의도적으로 input을 느리게 만들어 fluctuation을 줄인다. 즉, formulation이 absorption/input을 지배하면 terminal slope와 dosing interval의 임상 의미가 달라진다. Morphine MR은 짧은 elimination half-life에도 q24h regimen을 가능하게 하고, leuprolide depot은 짧은 half-life에도 월 1회 투여를 가능하게 한다 [R&T pp.337–338]. 이것은 “나쁜 flip-flop”이 아니라 **의도된 input control**이다.

<!-- RECAP -->
**Recap**: terminal slope를 곧바로 elimination으로 번역하지 말라. 먼저 route, formulation, absorption duration을 확인한다.

---

## §2-M6. Therapeutic Window — PK 식을 임상 의사결정으로 바꾸는 제약조건

<!-- MASTER LENS -->
### Big Idea

Therapeutic window는 단순한 농도 구간이 아니라, benefit과 harm을 동시에 고려해 regimen을 정하는 clinical utility frame이다. R&T는 dosage regimen을 dose, dosage form, route, interval, duration으로 구성하고, 이를 systemic exposure와 beneficial/adverse response에 연결한다 [R&T pp.267–268].

### Term lock

- **Therapeutic concentration range**: 임상 경험상 효과가 있고 위해가 받아들여질 만한 농도 범위 [R&T p.272].
- **Therapeutic window**: utility curve threshold 이상으로 정의되는 더 의사결정적인 구간이다. 즉, 두 범위는 겹칠 수 있지만 같은 개념은 아니다 [R&T pp.273–274].
- **Therapeutic index**: 전임상에서는 $TD_{50}/ED_{50}$ ratio로, 임상에서는 exposure 변화에 대한 개별 환자의 limiting effect sensitivity로 이해해야 한다 [R&T p.278].

### Utility formalization lock

$U(C)=\sum w_iP_i(C)$ 같은 표현은 **교과서 원수식이 아니라 교육적 formalization**이다.

<!-- ANNOTATION -->
formalization(← 개념을 계산식 형태로 표현)은 출처 식과 구별해 읽어야 한다.

R&T Fig. 9-4의 가중치 예시는 저자 판단에 따른 illustrative weighting으로만 써야 하며, 표준 regulatory weight처럼 쓰면 안 된다 [R&T p.273].

### PK/PD and response clocks

Plasma concentration이 항상 effect를 즉시 설명하지 않는다. Atorvastatin은 PK half-life가 약 14시간이지만 cholesterol response plateau는 3–4주가 걸릴 수 있고, erythropoietin은 PK half-life가 약 9시간이어도 hematocrit plateau는 약 70일에 걸친다 [R&T pp.343–344]. 여기서 질문은 “drug의 half-life인가, turnover system의 half-life인가”이다.

### Antimicrobial anchor

Antimicrobial regimen은 PK index가 다르면 dosing logic도 달라진다. β-lactam 계열처럼 time above MIC가 중요한 경우 prolonged/continuous infusion이 합리적일 수 있고, aminoglycoside처럼 peak/MIC와 toxicity window가 중요한 경우 once-daily fractionation이 합리적일 수 있다 [R&T pp.307–312; R&T pp.347–348]. R&T Fig. 11-20의 AUC/MIC >101 예시는 resistance avoidance 논리의 정량 anchor다 [R&T p.348].

<!-- TRENCH -->
**Trench-Level Tip — DDI variable lock**: protein binding만으로 DDI 민감도를 설명하지 않는다. R&T의 low/high extraction ratio 예시는 plateau 변화의 핵심 변수가 hepatic extraction ratio임을 보여준다 [R&T pp.309–310; R&T pp.350–351].

<!-- RECAP -->
**Recap**: TW는 PK 식의 마지막 줄이 아니라 regimen design의 제약조건이다. 목표농도, fluctuation, PD delay, toxicity mechanism을 동시에 제한한다.

---

## §2-M7. Loading Dose + Maintenance: 목표 즉시 도달과 유지의 분리

<!-- MASTER LENS -->
### Big Idea

Loading dose(← 초기에 목표에 빨리 올리는 용량)는 “기다리는 시간”을 줄이는 도구이고, maintenance dose(← 목표를 유지하는 반복 용량)는 “유지되는 평균 입력속도”를 맞추는 도구다. 둘은 목적이 다르다 [R&T pp.326–329].

### Source-locked equations

$$D_M=D_L(1-e^{-K\tau})$$

$$D_L=\frac{D_M}{1-e^{-K\tau}}=R_{ac}D_M$$

Doxycycline 예시는 $t_{1/2}=24$ h, $D_L=200$ mg, $D_M=100$ mg/day, $R_{ac}=2$라는 단순 anchor를 제공한다 [R&T p.327]. Sirolimus는 $t_{1/2}=2.5$ days, loading 6 mg, maintenance 2 mg/day의 임상 예시로, 이론식과 실제 tolerability 사이의 조정 필요성을 보여준다 [R&T pp.326–327].

### Bolus + infusion anchor

정속 주입에서 즉시 plateau 근처로 올리려면 bolus와 infusion을 결합할 수 있다. 먼저 bolus가 초기 농도 위치를 만들고, infusion이 이후 input rate를 유지한다. Gabrielsson PK13은 400 µg/kg bolus + 800 µg/kg over 26 min, therapeutic window 50–300 µg/L, $V_c=2.0$ L/kg, $CL=1.0$ L/min/kg, $CL_d=1.0$ L/min/kg, $V_t=5.0$ L/kg의 수치 anchor를 제공한다 [G pp.537–539].

### Daptomycin fractionation anchor

Daptomycin Study A의 같은 daily dose 비교는 **75 mg/kg q24h vs 25 mg/kg q8h**이다. 둘 다 75 mg/kg/day이지만 CPK는 991 vs 3996 U/L로 크게 달랐다 [R&T pp.351–353]. Study B에서는 같은 Cmax 58 µg/mL 조건에서도 AUC와 CPK가 달랐다. 이 예시는 Cmax 또는 AUC 하나만으로 toxicity를 설명하지 말고 recovery time/fractionation을 함께 보라는 anchor다.

<!-- RECAP -->
**Recap**: loading은 initial condition, maintenance는 long-run input rate, fractionation은 recovery time과 fluctuation을 바꾼다.

---

## §2-M8. TW-Driven Dosage Design Algorithm

<!-- MASTER LENS -->
### Big Idea

Therapeutic window가 $C_{lower}$와 $C_{upper}$로 주어지고 PK parameter가 있으면, 최대 투여간격과 최대 maintenance dose를 계산할 수 있다 [R&T pp.334–337].

### Source-locked equations

$$C_{lower}=C_{upper}e^{-K\tau_{max}}$$

$$\tau_{max}=\frac{\ln(C_{upper}/C_{lower})}{K}=1.44t_{1/2}\ln\left(\frac{C_{upper}}{C_{lower}}\right)$$

$$D_{M,max}=\frac{V}{F}(C_{upper}-C_{lower})$$

$$C_{ss,av}=\frac{C_{upper}-C_{lower}}{\ln(C_{upper}/C_{lower})}$$

### Algorithm lock

1. $C_{lower}$, $C_{upper}$를 정한다.
2. $t_{1/2}$로 $\tau_{max}$를 계산한다.
3. $V/F$로 $D_{M,max}$를 계산한다.
4. 실제 제형 strength와 adherence를 고려해 practical $\tau$와 $D_M$을 선택한다.
5. 필요 시 $D_L$로 initial target에 접근한다.

<!-- TRENCH -->
**Trench-Level Tip**: 이 알고리즘은 linear PK, fixed interval, target concentration과 response의 충분한 연결을 전제한다. Single-dose therapy나 PD plateau가 turnover로 지배되는 약물에서는 그대로 적용하지 않는다 [R&T p.279; R&T pp.341–345].

<!-- RECAP -->
**Recap**: M8은 M1–M7을 dosing algorithm으로 묶는 끝점이다. 즉, `Cupper/Clower`는 interval, `V/F`는 dose size, `CL`은 average concentration을 각각 제약한다.

---

# §5 — Confusion Pair Dissection

## §5-쌍1. $C_{ss}$ vs $C_{av,ss}$ vs $A_{av,ss}$

<!-- CONFUSION -->
| 혼동 | 정확한 분리 | 왜 중요한가 |
|---|---|---|
| $C_{ss}$ | 정속 주입 plateau concentration: $R_{in}/CL$ | infusion maintenance target |
| $C_{av,ss}$ | 다중투여 interval 평균 concentration: $F\text{Dose}/(CL\tau)$ | TDM/exposure-response target |
| $A_{av,ss}$ | plateau 평균 amount: $1.44F\text{Dose}t_{1/2}/\tau$ | residence time/body burden |

**Critical Blow**: $1.44F\text{Dose}t_{1/2}/\tau$를 concentration 식으로 쓰면 단위가 틀린다. 1-compartment와 known $V$를 명시하지 않으면 amount-to-concentration 변환은 성립하지 않는다 [R&T p.324; R&T p.337].

---

## §5-쌍2. NONMEM `SS=1` vs `SS=2`

<!-- CONFUSION -->
| 항목 | `SS=1` | `SS=2` |
|---|---|---|
| 의미 | steady-state dose event | steady-state infusion/input condition |
| 위험 | 실제 accumulation phase를 plateau로 오인 | bolus/infusion initial condition을 잘못 설정 |
| 선행 질문 | 충분한 투여 이력이 있었는가? | input이 어떤 형태였는가? |

**Critical Blow**: steady-state flag는 “편의상 넣는 옵션”이 아니라 initial condition을 수학적으로 바꾸는 명령이다. 투여 이력이 plateau 조건을 만족하지 않으면 쓰지 않는다.

---

## §5-쌍3. Flip-flop vs ordinary extravascular decline

<!-- CONFUSION -->
| Ordinary | Flip-flop |
|---|---|
| $K_a>K$ | $K_a<K$ |
| terminal slope ≈ elimination | terminal slope ≈ absorption |
| terminal half-life가 drug elimination 정보를 줌 | terminal half-life가 formulation/input 정보를 줄 수 있음 |

**Critical Blow**: terminal slope만 보고 elimination half-life를 확정하지 않는다. route, formulation, absorption duration이 먼저다 [G pp.45–46].

---

## §5-쌍4. 도달 시간 vs 축적 정도 vs fluctuation

<!-- CONFUSION -->
| 질문 | 결정자 | 대표식 |
|---|---|---|
| plateau에 언제 도달하는가? | $t_{1/2}$ | $1-e^{-Kt}$ |
| 얼마나 축적되는가? | $\tau/t_{1/2}$ | $R_{ac}=1/(1-e^{-K\tau})$ |
| 평균 level은 어디인가? | $CL$과 average input | $C_{av,ss}=F\text{Dose}/(CL\tau)$ |
| peak-trough 진폭은? | $\tau/t_{1/2}$ | dosing interval이 길수록 커짐 |

**Critical Blow**: dose를 두 배로 하면 concentration level은 올라가지만, $R_{ac}$ 자체는 변하지 않는다.

---

## §5-쌍5. Therapeutic Window vs Therapeutic Index

<!-- CONFUSION -->
| 개념 | 정확한 의미 | 오해 |
|---|---|---|
| Therapeutic Window | utility threshold 이상인 concentration region | “경험적 치료농도범위”와 동의어로 사용 |
| Therapeutic Concentration Range | 임상 경험상 효과와 허용 가능한 위해를 만족하는 농도 범위 | TW와 항상 같은 수치라고 가정 |
| Therapeutic Index | 전임상 ratio 또는 임상 exposure sensitivity | high TI가 모든 환자의 안전을 보장한다고 해석 |

**Critical Blow**: wide therapeutic window와 high therapeutic index는 같은 문장이 아니다. 전자는 concentration bound, 후자는 exposure 변화에 대한 safety margin/sensitivity 문제다 [R&T pp.272–278].

---

## §5-쌍6. MRT vs half-life

<!-- CONFUSION -->
| 항목 | 의미 | 주의 |
|---|---|---|
| $t_{1/2}$ | amount/concentration이 절반이 되는 시간 | 1차 decline의 slope 기반 |
| MRT | molecule이 체내에 머무는 평균 시간 | moment-based: $AUMC/AUC$ |
| 1-compartment | $MRT=1/K=1.44t_{1/2}=V/CL$ | 단순식 가능 |
| multi-compartment | $MRT=AUMC_{0-\infty}/AUC_{0-\infty}$ | $V/CL$ 단순 치환 위험 |

**Critical Blow**: $1.44t_{1/2}$는 1차 선형 시스템의 시간척도일 뿐, 어떤 compartment의 concentration을 대표하는지는 모델 구조가 결정한다 [R&T p.289; R&T pp.299–304].

---

## §5-쌍7. Acquired Resistance vs Tolerance

<!-- CONFUSION -->
| 항목 | Acquired resistance | Tolerance |
|---|---|---|
| 본질 | 세포/미생물 population 또는 mutation 변화 | 환자/시스템의 PD adaptation |
| 시간 구조 | selection pressure와 population shift | receptor desensitization 또는 homeostatic feedback |
| 관리 논리 | exposure target, resistance window 회피 | drug holiday, modified release, rate-of-change control |

**Critical Blow**: 효과 감소가 보인다고 모두 tolerance가 아니다. 항균제에서는 resistance selection, nitrate/nicotine/nifedipine에서는 PD adaptation이 핵심일 수 있다 [R&T pp.346–348].

<!-- RECAP -->
**§5 Recap**: 위험한 혼동은 “수학식의 기호가 비슷해서”만 생기지 않는다. 더 자주 생기는 원인은 결정자가 다른 질문을 같은 질문으로 취급하는 것이다.

---

# §7 — Self-Test Module

## §7-Recall Layer

<!-- SELF-TEST -->
### Q1. 정속 주입에서 $C_{ss}$를 결정하는 parameter는 무엇인가?
**Answer**: $C_{ss}=R_{in}/CL$이므로 plateau 농도 수준은 clearance와 input rate가 정한다 [G p.23; R&T p.288].

### Q2. 90% plateau에 도달하는 데 필요한 시간은 대략 몇 half-lives인가?
**Answer**: 약 3.3 half-lives, 실무적으로 3–4 half-lives [G p.22; R&T p.291].

### Q3. 다중투여 accumulation factor에 dose가 들어가지 않는 이유는?
**Answer**: 같은 dose가 반복될 때 잔여분의 비율은 $e^{-K\tau}$이고, 반복합은 등비수열이므로 ratio는 $\tau/t_{1/2}$에만 의존한다 [G pp.44–45; R&T pp.795–797].

### Q4. $C_{av,ss}$와 $A_{av,ss}$의 차원은 각각 무엇인가?
**Answer**: $C_{av,ss}$는 concentration, $A_{av,ss}$는 amount다. $A_{av,ss}$를 concentration처럼 쓰면 차원 오류다 [R&T p.324; R&T p.337].

### Q5. Flip-flop에서 terminal slope는 무엇을 반영하는가?
**Answer**: $K_a<K$이면 terminal slope는 absorption rate를 반영한다 [G pp.45–46].

---

## §7-Application Layer

<!-- SELF-TEST -->
### Q6. 어떤 약물의 $t_{1/2}=8$ h이고 q24h 투여한다. 축적은 클까?
**Answer**: $\tau/t_{1/2}=3$이므로 $R_{ac}=1/(1-2^{-3})=1.14$ 정도로 크지 않다. q24h라도 half-life 대비 interval이 길면 accumulation은 작다.

### Q7. 같은 daily dose를 q24h에서 q8h로 바꾸면 무엇이 변하는가?
**Answer**: average input rate가 같으므로 $C_{av,ss}$는 원칙적으로 같지만, peak-trough fluctuation은 줄어든다. 단 toxicity가 recovery time/fractionation에 의존하면 결과가 달라질 수 있다 [R&T p.325; R&T pp.351–353].

### Q8. $C_{av,ss}=F\text{Dose}/(CL\tau)=1.44F\text{Dose}t_{1/2}/\tau$라고 쓴 문장을 교정하라.
**Answer**: 앞 식은 concentration, 뒤 식은 amount다. 정확히는 $C_{av,ss}=F\text{Dose}/(CL\tau)$이고, $A_{av,ss}=1.44F\text{Dose}t_{1/2}/\tau$이다. 1-compartment에서만 $C_{av,ss}=A_{av,ss}/V$이다.

### Q9. Phenobarbital 100 mg q24h, $t_{1/2}=4$ days에서 R&T의 5.8과 식의 6.3을 어떻게 설명할 것인가?
**Answer**: 5.8은 $A_{av,ss}/Dose\approx5.76$에 해당하는 average accumulation ratio이고, peak/trough accumulation index $R_{ac}$는 Eq. 11-10 기준 약 6.3이다. 둘을 같은 라벨로 쓰지 않는다 [R&T pp.324–326].

### Q10. Atorvastatin에서 PK plateau와 PD plateau가 다를 수 있는 이유는?
**Answer**: plasma concentration의 half-life와 cholesterol turnover response의 time scale이 다르기 때문이다. Atorvastatin은 $t_{1/2}\approx14$ h이나 maximal cholesterol response는 3–4주가 걸릴 수 있다 [R&T p.343].

### Q11. Daptomycin Study A에서 “같은 daily dose” 비교군은 무엇인가?
**Answer**: 75 mg/kg q24h와 25 mg/kg q8h이다. 둘 다 75 mg/kg/day이며, CPK는 991 vs 3996 U/L로 달랐다 [R&T pp.351–353].

### Q12. TW algorithm에서 $C_{upper}/C_{lower}$ ratio가 주로 결정하는 것은?
**Answer**: 허용 가능한 dosing interval의 상한이다. $\tau_{max}=1.44t_{1/2}\ln(C_{upper}/C_{lower})$이다 [R&T p.334].

---

## §7-Boss Dilemma

<!-- SELF-TEST -->
### Q-BD. A new oral drug has linear PK, $F=0.6$, $V=100$ L, $t_{1/2}=4$ h, and a proposed therapeutic window of 1–4 mg/L. The team proposes 300 mg q12h without loading. What should you check first?

**Answer**:
1. 먼저 이 사례가 교과서 등재 약물이 아니라 **가상 연습 문제**임을 명시한다.
2. $\tau_{max}=1.44\times4\times\ln(4/1)=7.98$ h이므로 q12h는 window를 벗어날 가능성이 크다.
3. $D_{M,max}=(V/F)(4-1)=500$ mg이지만, dose size만으로는 충분하지 않고 interval이 먼저 제약된다.
4. q8h 등 practical interval을 검토하고, 초기 목표 접근이 필요하면 loading dose를 별도로 계산한다.
5. PD delay, active metabolite, tolerance, flip-flop absorption이 있으면 단순 TW algorithm 적용을 중단하고 모델을 확장한다.

<!-- RECAP -->
**§7 Recap**: 계산 문제의 핵심은 숫자를 넣는 것이 아니라 “어떤 식이 어떤 조건에서만 유효한가”를 먼저 잠그는 것이다.

---

# §8 — Meta-Frame & Big Picture

## §8A — Positioning

<!-- MASTER LENS -->
Session 07은 pharmacometrics의 “steady-state grammar”를 만든다. 이전 세션의 single-dose PK는 시간-농도 곡선의 기본 모양을 제공한다. 이 세션은 그 곡선을 반복·유지·제약하는 법을 제공한다. 이후 TDM, PopPK covariate interpretation, exposure-response, Phase 1 multiple ascending dose design은 모두 이 문법 위에 올라간다.

---

## §8B — Dependencies and Failure Modes

| 실패 모드 | 원인 | 결과 |
|---|---|---|
| Early data에 `SS=1` 적용 | plateau 시간 조건 무시 | CL/F, V/F, ETA 추정 왜곡 |
| $A_{av,ss}$를 $C_{av,ss}$로 표기 | amount/concentration 차원 혼합 | dose rationale 오류 |
| dose 크기로 accumulation ratio 설명 | $R_{ac}$의 dose independence 미이해 | regimen 변경 효과 오판 |
| terminal half-life를 elimination으로 고정 | flip-flop 미인식 | formulation/absorption 해석 오류 |
| TW와 TI 혼용 | concentration bound와 safety sensitivity 혼동 | dose justification 불명확 |
| PD plateau를 PK plateau로 가정 | turnover/cell lifespan 무시 | effect onset/duration 예측 실패 |
| Cmax 또는 AUC 단일 변수로 toxicity 설명 | fractionation/recovery time 무시 | regimen selection 오류 |

---

## §8C — Professional Moat

<!-- ANCHOR -->
전문가의 해자는 복잡한 식을 많이 외우는 데 있지 않다. 같은 regimen 질문을 다음 결정자 표로 즉시 분해하는 데 있다.

| 질문 | 결정자 | 대표 사용처 |
|---|---|---|
| 목표 평균 농도는? | $CL$, average input rate | maintenance dose, TDM |
| 목표에 얼마나 빨리 도달하나? | $t_{1/2}$ | washout, Day-to-SS, sampling schedule |
| peak-trough 진폭은? | $\tau/t_{1/2}$ | dosing interval, adherence, toxicity |
| loading이 필요한가? | target onset, $V/F$, $R_{ac}$ | urgent therapy, bolus+infusion |
| TW 안에 머무르는가? | $C_{upper}$, $C_{lower}$, $V/F$, $t_{1/2}$ | regimen design |
| effect가 늦게 오나? | turnover/cell lifespan | statin, EPO, indirect response |
| formulation이 terminal slope를 바꾸나? | absorption/input duration | MR/depot/flip-flop |
| toxicity가 recovery time에 의존하나? | fractionation, minimum exposure duration | daptomycin-like cases |

[교과서 외 실무 해석] 이 표는 regulatory submission 문장을 대신 쓰는 것이 아니라, 교과서 수식을 제출 가능한 정량 논리로 번역하기 위한 내부 검토 틀이다. unsupported 수치, “deficiency letter”, “NDA refusal” 같은 외부 단정은 본 Content Lock에서 삭제했다.

---

## §8D — 28-Session Navigation

<!-- RECAP -->
이 세션이 잠그는 것은 네 가지다.

1. **Constant-rate input**: $C_{ss}=R_{in}/CL$.
2. **Time to steady state**: $t_{1/2}$ controls approach.
3. **Multiple dosing**: $R_{ac}$ and fluctuation depend on $\tau/t_{1/2}$.
4. **Regimen design**: therapeutic window converts PK parameters into dose and interval constraints.

다음 세션으로 넘어갈 때 이 문장을 유지한다.

> “항정상태는 하나의 숫자가 아니라, 시간·수준·진폭·임상제약을 분리해 다시 조립하는 작업이다.”

---

## Compression Lock

- Step 1 Draft v0 length: 112,589 characters.
- Content Lock v1 length: **57601** characters.
- Content Lock v2 length: **61645** characters.
- Enforcement: Content Lock v2 remains within the +8% limit relative to Content Lock v1 and is shorter than Step 1 Draft v0.
- Deleted or downgraded: unsupported numerical/regulatory chains, redundant detailed examples, study-problem expansions, figure-analysis material reserved for Phase 4C.
- Preserved: source page tags on MUST cards, equations, and key examples.

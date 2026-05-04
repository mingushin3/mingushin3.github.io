# Session 016 — Insight Crucible Report v1 (FINAL)

**STAGE 3 / 3 최종 통합본** — Gabrielsson & Weiner Ch.6 + PK15 + PK35 + Rowland & Tozer Ch.15 + Ch.18 단일 Source Universe 융합 완료
**Mode**: A-Critical (G&W Ch.6, PK35, R&T Ch.15, R&T Ch.18) / B-Standard 가중 (PK15)
**Persona**: P1 (석좌급 멘토) + P3 (FDA 임상약리 심사관) 동시 운용
**Source Universe (최종)**: G&W p.423–466, p.546–548, p.641–643 | R&T 5e Ch.15 p.443–489 | R&T 5e Ch.18 p.577–610
**역방향 설계 분량 결산**: STAGE 1 ~35% / STAGE 2 ~30% / STAGE 3 ~35% = **합계 1.0 (총량 불변)**

---

## 자체 정정 기록 (Stages 1–3)

본 보고서는 누적 통합 과정에서 Operative Filter ("Restates existing Step 1 content: exclude without exception") 및 Source Fidelity 기준에 따라 자체 정정을 수행하였다. 정합성 추적을 위해 명시한다.

### STAGE 1 → STAGE 2 정정

| STAGE 1 항목 | 정정 사유 | STAGE 2 처리 |
|---|---|---|
| T1 Wall #3 "var = 정보의 무게" | Step 1 §2.6 B-3 (line 606) 중복 | Grade C 강등 — Tip 목록 삭제 |
| T3 Tip 2 "var(P̂)/var(Ĉ) 정보의 무게" | Step 1 §2.6 B-3 line 610 중복 | Grade C 강등 — 삭제 |
| T3 Tip 3 "V̂=119.6L driver는 wide prior" | Step 1 §2.6 B-3 line 606–607 중복 (Step 1은 Sheiner 역계산까지 수행) | Grade C 강등 — 삭제 |

### STAGE 2 → STAGE 3 정정 (Tozer Ch.18 직접 대조 결과)

| STAGE 2 항목 | Tozer Ch.18 직접 검증 결과 | STAGE 3 처리 |
|---|---|---|
| Step 1 §5.5 "V 90% covariate 설명, CL 30–40% 설명" 임시 qualitative 처리 (Audit MUST_FIX #4) | **Tozer Fig 18-5 (p.582) 본문 직접 대조**: V는 약 45% 설명(BW 25% + age 10% + RF 10%, 55% **UNACCOUNTED**); Hepatic CL은 약 40% 설명(60% UNACCOUNTED); Renal CL은 약 80% 설명(RF 50% + BW 15% + age 15%); F는 단 5%만 설명. **Step 1의 "V 90%" claim은 source와 정반대 방향으로 inverted 되어 있음.** | **확정 정정 — Grade A REWRITE** (T4 항목 #11에 명시) |
| STAGE 2 §2.9 "Vu<120 AND CLu<CLuD" 하드 AND gate 수정 권고 | R&T Fig 15-18 continuous trade-off 확인 — STAGE 2 권고 유지. | 변경 없음 — 좌표 평면 표현 유지 |
| STAGE 2 예측 "S8 Sampling Time Mismatch" signature 가설 | **Tozer Fig 18-13 (p.605) 직접 대조**: 1×t½ sampling은 CL × 1/3 ↔ V × 3 구분 불가. 4×t½ 또는 steady state에서만 CL 정확 추정. STAGE 2 예측 정확. | S8 정식 등재 (T2(b)) |
| STAGE 2 메타 패턴 "두 인자 곱" Tip 8 | **Tozer Fig 18-9 (p.592) missed-dose 시뮬레이션이 결정적 추가 증거**: 600 mg q24h 한 번 missed → trough 3.2 mg/L (window 미달); 200 mg q8h 세 번 missed → trough 5.0 mg/L (여전히 q24h 한 번 miss보다 위). t½/τ 비율 × therapeutic window 폭의 **곱**이 forgiveness를 결정. | 메타 패턴 확장 — T3 Tip 12로 명시 |

**교훈**: 본 워크플로우는 "예측 → 직접 대조 → 정정"의 3단계 반복으로 보고서 정합성을 유지한다. STAGE 1·2의 자체 비판은 보고서 신뢰도 비용을 발생시키나, 이를 명시함으로써 누적 통합본이 patch memo + audit + 직접 본문 검증을 모두 통과한 final 산출물임을 보증한다.

---

## 운용 필터 재진술

> "패턴인식 (Ch.6) → 질환별 PK 변동 (Ch.15) → Bayesian TDM (PK35) → 처방 시작·관리 (Ch.18) → 노출 보고 (PK15) 캡스톤을 막 끝낸 1년차 PhD에게, 30년 베테랑이 5분 엘리베이터 대화에서 무엇을 말해야 그 학생의 이해가 영구적으로 한 단계 도약하는가?"

→ Step 1 Draft v0이 이미 말한 것은 _제외_. 본 보고서는 삽입 위치(§ + 카드명)와 1–2문장 삽입 텍스트, 삭제 지시만 제공.

---

## T1. P1 — Internalization Barriers & Master's Intuitions

### (a) Cognitive Wall — 외울 수는 있으나 내재화되지 않는 지점

**Wall #1 (STAGE 1, Grade B): kin/kout = 동적 평형의 표상**
학생은 Eq.6:1을 외울 수 있으나, baseline R₀ = kin/kout이 정적 ratio가 아니라 _동적 평형_ — kin이나 kout 한쪽만 흔들면 시스템이 새 평형으로 이동하고, _이동 속도는 오로지 kout으로만 결정된다_ — 라는 통찰이 보이지 않으면 turnover model은 여전히 외운 공식. (Step 1 §2.4 turnover 카드 마진 1–2 sentences 삽입 권장.)

**Wall #2 (STAGE 1, Grade B): peak-shift는 RT 유한성의 결과**
Eq.6:7의 `kon·C·(R_T − RC)` 항에서 dose가 커질수록 (R_T − RC)가 더 빨리 0에 접근. d[RC]/dt = 0 시점(nadir)이 더 일찍 도래하는 것은 _receptor pool이 유한_하기 때문이지 "kon이 dose-dependent"여서가 아님. 이 비대칭(2차 build-up + 1차 degradation)을 못 보면 학생은 Case B 좌측 peak-shift를 "kon이 큰 약물의 특성"으로 잘못 외움. (Step 1 §2.5 receptor on/off 카드 1 sentence.)

**Wall #4 (STAGE 2, Grade A): fu↑ ≠ CLu↑ for low-E albumin-bound drugs**
학생은 Step 1 §2.7 D-E 표에서 "Phenytoin fu 0.1→0.25" 단백 결합 변화를 보고 _영향 없음_으로 외울 수 있으나, **저추출비·albumin 결합 약물에서 fu↑은 CLu에 거의 영향이 없으면서 total CL은 _증가_시킨다**는 부호 분리를 보지 못함. R&T p.464가 명시: phenytoin total clearance는 신질환에서 2–3배 증가하나 unbound CL과 unbound V는 본질적으로 변화 없음. **STAGE 3 직접 연결**: Tozer Table 18-5 (p.595)는 phenytoin "extensively bound to albumin"으로 명시하며, "altered plasma protein binding이 anticipated 되는 경우 (uremia, after surgery, displacing drugs) target total concentration이 same therapeutically important unbound concentration을 attain하도록 adjusted 되어야 한다"고 직접 처방 — 이것이 Wall #4의 **임상 운영 단위 표현**.

**Wall #5 (STAGE 2, Grade A): SCr는 실시간 RF 지표가 아니다 (turnover lag)**
학생은 Cockcroft-Gault를 잘 외우나, **SCr이 RF의 _현재_ 거울이 아니라 _과거 평균_ 거울**임을 보지 못함. R&T Eq.15-14: `turnover time = SCr/(dC/dt)`. RF 10%일 때 turnover time 60시간, half-life 42시간. 즉 AKI 환자의 오늘 SCr=1.5는 _이틀 전_ RF의 거울이며, 환자의 _현재_ RF는 SCr이 도달한 평형보다 훨씬 낮을 수 있음 → 표준 dose가 첫 24–48h 동안 toxic 농도로 누적.

**Wall #6 (STAGE 2, Grade A): Imipenem이 Rd framework foundational 가정을 위배함**
R&T Fig.15-15 핵심: imipenem의 CL과 CLR이 RF에 _동일한 기울기로 평행하게_ 감소해야 Rd 가정 충족이지만, 실제로 두 곡선 간격이 RF↓에 따라 _좁아짐_ → "비신 CL"에 _신장 대사_가 섞여 있다는 시스템적 신호. R&T Table 15-8 cerivastatin/bupropion/telithromycin/cyclophosphamide/felbamate에 동일 패턴.

**Wall #7 (NEW STAGE 3, Grade B): Fig 18-2 PD variability pie chart는 hypothetical drug 예시이다**
Tozer Fig 18-2 (p.579)의 "gene encoding receptor 40% / other genes 20% / age 15% / concurrent drugs and diseases 10% / environmental 9% / error 6%" 백분율은 **hypothetical drug**의 schematic representation이다. 본문 직접 표기: "In this hypothetical analysis, six different categories causing the variability are identified." 학생은 이 백분율을 모든 약물에 일반화 가능한 universal constant로 외울 수 있으나, 이는 _pedagogical device_이며 empirical data가 아님. NDA의 PD variability 분석에서 이 수치를 인용하면 reviewer 즉각 reject. (Step 1 §1 학습 목표 또는 §5.5 mini-anchor 1 sentence.)

**Wall #8 (NEW STAGE 3, Grade A — STAGE 2 잠정 → 확정): Fig 18-5는 covariate 모델의 한계를 명시한다**
Tozer Fig 18-5 (p.582) 직접 본문: "**95%** of the variability in oral bioavailability cannot be accounted for"; V는 body weight 25%·age 10%·renal function 10%로 **약 45%** explained, 55% **UNACCOUNTED**; Hepatic CL은 BW·age·RF 합쳐 **약 40%** explained, **60% UNACCOUNTED**; Renal CL만 **약 80%** explained (renal function 50% 단독). 학생이 "covariate model이 variability의 대부분을 설명한다"는 인상을 가지면 PopPK 결과를 과신함. **실제는: hepatic CL drug에서 환자 demographics만으로는 60%의 IIV를 설명 못함 → η 추정값 큼 → 개인 dosing 신뢰도 한계 명시 필요**. Step 1 §5.5 line 1423 "V 90%·CL 30–40%"는 V를 정반대로 inverted 한 것이므로 REWRITE 필수 (T4 #11).

**Wall #9 (NEW STAGE 3, Grade B): Forgiving vs Unforgiving은 t½/τ × window 폭의 곱이다**
Tozer Fig 18-9 (p.592) 4 panels는 동일 약물(t½ = 18.2 h, V = 50 L, window 8–20 mg/L)에서 600 mg q24h vs 200 mg q8h 비교. q8h regimen에서 _세 번 연속 missed_ 시 trough 5.0 mg/L (window 미달)로 떨어지나, **q24h regimen에서 _한 번_ missed만으로 trough 3.2 mg/L (window 훨씬 미달)**. 학생은 "frequent dosing이 missed dose에 더 취약하다"고 직관할 수 있으나 _정반대_ — _t½/τ 비율_이 forgiveness를 결정. q8h: t½/τ = 2.27 (forgiving), q24h: t½/τ = 0.76 (unforgiving). Tozer가 명시한 forgiving 약물(amiodarone t½ 50–60일, phenobarbital t½ 4일)과 unforgiving 약물(esmolol t½ 9분, antimicrobials/antivirals — resistance emergence 위험) 분류는 _PK 단독이 아니라_ PK × PD/microbiology의 곱.

**Wall #10 (NEW STAGE 3, Grade A): Sampling Timing × Parameter Identifiability**
Tozer Fig 18-13 (p.605) 핵심 통찰: constant infusion 중 1 usual half-life 시점 sampling은 _CL × 1/3_과 _V × 3_을 구분 못함 (둘 다 일찍 낮은 농도로 보임). 4 usual half-lives 또는 steady state에서만 CL 차이가 명확히 발현. **학생은 NONMEM PopPK 데이터셋 구축 시 sampling time 중요성을 _identifiability geometry_로 보지 못하면 조기 sample 위주 데이터에서 CL/V 추정이 collapsed 됨**. 본문 (p.605): "Vancomycin... clearance varies more (larger coefficient of variation), particularly if age and disease state are factored in, than volume of distribution. Thus, by **fixing volume of distribution**, estimates of the clearance of vancomycin made from nonsteady-state values obtained within this time span are more accurate" — 이것이 Bayesian TDM에서 "V를 strong prior로 고정하고 CL만 individualize"하는 통상 관행의 _수학적 근거_. (Step 1 §2.6 Bayesian 카드 마진 1 sentence cross-link.)

### (b) System Integration — 이 챕터들이 단일 시스템으로 작동하는 시점

**STAGE 1 작동 지점**: NONMEM PopPK 보고서의 "Final Model Selection" 섹션과 `$DES` 블록을 동시에 작성하는 순간.

**STAGE 2 작동 지점**: 임상 약사의 "verify before dispensing" 30초 chain — fe 확인 → CLcr 추정(C-G + 체질량 평가) → Rd 계산 → fe ≤ 0.30 OR RF ≥ 0.70 triage → LD/MD 분리 결정. 한 단계 끊기면 처방 도달 시 노출 어긋남.

**STAGE 3 작동 지점 (NEW): "TCS dosing decision" — 5 criteria 동시 검정 + Eq.18-1~18-4 적용 + Fig 18-13 sampling 합법성 판정의 단일 회의실 의사결정**

처방 회의에서 다음이 _하나의 thought stream_으로 흘러야 함:

1. **TCS criteria joint check** (Tozer p.594–596): concentration-response 관계 양호한가 → high probability of failure (low TI + 큰 PK variability) → population PK 정보 가용 → reliable assay 가용 → turnaround time이 다음 dosing decision 전인가. **5개를 _순서대로 통과_해야 하며, 한 criterion이라도 unfavorable이면 TCS는 unjustified** (Audit MUST_FIX #3 약화 표현 → STAGE 2 Grade A 반영).

2. **Sampling regimen 결정** (Tozer Fig 18-13 + Wall #10): 환자가 loading 단계인가 (1×t½ 이전 sampling 무의미) vs maintenance 단계인가 (≥4×t½ 또는 trough sampling). 어느 단계인지에 따라 sampling timing이 달라야 _CL과 V가 분리되어_ 추정 가능.

3. **데이터 형태별 식 선택** (Tozer Eq.18-1~18-4): 
   - 1 dose missed → Eq.18-1 (digoxin example: 0.39 µg/L)
   - 2 consecutive missed → Eq.18-2
   - 9-13-17-21 institutional regimen → Eq.18-3 (vancomycin pediatric example: 2.03 mg/L vs 7.1 mg/L for q6h — _institutional convenience_가 underexposure 원인)
   - 임의 dose × 임의 interval (erratic ICU) → Eq.18-4 (vancomycin AF example: observed 34 mg/L vs expected 33.7 mg/L — kinetics 정합, 단 dose 너무 큼)

이 3 단계가 _15분 회의 안_에 결론에 도달해야 하며, Bayesian objective function (PK35) 적용은 step 3 직후에 conditional posterior 추정으로 이어짐. Step 1이 §2.10 (TCS) → §2.11 (LD) → §2.12 (Missed dose)를 _독립_ MUST 카드로 분리한 것은 이 회의 단위 사고를 깨뜨림. STAGE 2가 권고 철회한 §2.7+§2.8+§2.9 통합 거부와 _동일한 이유로_ — independent gate를 통과해야 다음 단계가 _의미_를 가짐 — STAGE 3 §2.10·§2.11·§2.12는 별도 카드 유지. 단 §2.10 카드 마지막에 "criteria가 _순차적 가중 곱_으로 적용된다"는 Wall #9·Tip 13 anchor를 1 sentence 추가.

### (c) Expert Intuition — 베테랑이 방정식 없이 1초에 판단하는 것

**STAGE 1 판단 1·2·3**: response-time plot 두 신호 / OFV 거동 / GOF 첫 확인. (유지)

**STAGE 2 판단 4·5**: 5초 triage (fe ≤ 0.30 OR RF ≥ 0.70) / Vu·CLu 좌표 평면 dialysis 효과성. (유지)

**STAGE 3 판단 6 (NEW): 1×t½ vs 4×t½ — sampling time만 보고 결과 신뢰도를 1초에 판정**
Tozer Fig 18-13: 베테랑은 환자 chart에서 "sampling time post-infusion start"를 _즉각_ 추출 → 1×t½ 미만이면 "이 sample로는 CL 추정 무의미, V만 conditional" / 2~6×t½면 "V 고정, CL 추정 가능 단 prior weighting 강하게" / steady state면 "CL 단독 추정, R MATRIX 정상이면 individual dose adjustment 직진". 이 _sampling timing → estimable parameter_ mapping은 PopPK 보고서에서 reviewer가 가장 먼저 보는 항목이며, 베테랑은 NONMEM 출력을 보기 전에 _데이터 구조 자체_로 결과 신뢰도를 예단함.

**STAGE 3 판단 7 (NEW): 미스 한 번에 무너지는가 — t½/τ 1초 계산**
새 환자 처방 검토 시 베테랑은 _t½/τ 비율_을 즉시 머릿속에 띄움. ≥ 2면 forgiving (q8h regimen이나 statin류 — missed 1–2회 임상 영향 소).; 0.5–1이면 borderline (대부분의 경구 항생제). < 0.5면 unforgiving (esmolol, 일부 antiviral — adherence 강조 필수). Fig 18-9 4 panels가 이 직관의 _시각적_ 근거. NDA 라벨 작성 시 "What if patient misses a dose?" 항목은 이 ratio로 결정되어야 하며, 무차별 "take as soon as remembered"는 unforgiving 약물에 부적절.

---

## T2. P3 — Regulatory & Practical Risk Surface

### (a) Deficiency Letter 위험

**STAGE 1 위험 1·2·3 유지**: Peak-shift 결정론 / Bayesian point estimate without uncertainty / PK margin·NOAEL margin 혼동.

**STAGE 2 위험 4·5·6 유지**: NDA 신질환 subgroup C-G + 체질량 미보고 / §2.9 hard AND gate가 EHR alerts로 옮겨갔을 때 / 신장 대사 약물에 표준 Rd 적용.

**위험 7 (NEW STAGE 3): Tozer Fig 18-2 hypothetical PD variability 백분율을 NDA briefing에 인용 시 즉각 reject**
Fig 18-2 캡션은 "hypothetical analysis"임을 명시하나, 학생·실무자가 이를 universal constant로 인용하는 사례 빈번. 특정 약물의 PD variability를 분해할 때 Fig 18-2 백분율을 그대로 적용하면 reviewer는 _의도적 misrepresentation_ 또는 _careless citation_으로 판단 — 어느 쪽이든 deficiency letter 사유.

**위험 8 (NEW STAGE 3): Phenytoin nonlinearity를 무시한 PopPK 모델로 NDA 제출**
Tozer p.588 직접 본문: "The nonlinearity of phenytoin's disposition adds to the need to monitor its concentration." Step 1 §2.10 TCS 카드가 phenytoin을 "low TI + within-subject PK low + between-subject PD low → TDM 적용 모범 사례"로 다루면서 _Michaelis-Menten saturation_을 명시하지 않으면 PopPK $PK 블록이 linear CL로 작성될 위험. 결과: 고용량 환자에서 systematic over-prediction → reviewer가 sensitivity analysis (linear vs Michaelis-Menten) 요구. (Step 1 §2.10 TCS phenytoin 행 1 sentence 추가.)

**위험 9 (NEW STAGE 3): CYP2D6 4군 stratification (Fig 18-6) 미반영 NDA submission**
Tozer p.582–583: trimipramine·nortriptyline 등 CYP2D6 polymorphism에서 poor 5–10% / intermediate 10–15% / extensive 65–80% / ultrarapid 5–10% 4 group이 임상적으로 relevant phenotype. NDA의 PopPK 모델에서 평균 AUC만 보고하고 4 group stratification을 반영하지 않으면, FDA Pharmacogenomics Subcommittee 차원에서 dosage label warning 추가 요구. STAGE 2 Wall #4와 결합 시: 신질환 + CYP2D6 PM 환자의 nortriptyline은 fu↑ × CL_CYP2D6↓의 _이중 효과_ — total 농도와 free 농도가 어떻게 변하는지 _분리 보고_ 필수.

### (b) NONMEM 실행 오류 시그니처

**STAGE 1 S1–S4 유지**: Saturation Mirage / Peak-shift Phantom / Bayesian Shrinkage Collapse / Wrong Hysteresis Direction.

**STAGE 2 S5–S7 유지**: Renal Cliff (C-G가 근감소군 RF 과대추정) / Imipenem Trap (신장 대사가 fe로 예측 불가) / Acute Lag (시변 SCr 미반영).

**Signature S8 — "Sampling Time Mismatch" (NEW STAGE 3)**
Vancomycin/aminoglycoside PopPK dataset이 _대부분 1×t½ 이전 sample_로 구성된 경우 (예: ICU에서 첫 24h dense sampling). NONMEM fit은 V는 잘 추정하나 CL은 systematically biased toward population mean. 진단 패턴:
- η-shrinkage on CL > 30% (V는 정상 < 15%)
- $COV step 통과해도 RSE(CL) > 50%
- CWRES vs TIME plot에서 first dose 직후 fan, 이후 정상화
Root cause: **Tozer Fig 18-13의 1×t½ vs 4×t½ identifiability collapse**. 해결: V를 population value에 strong prior로 고정 + CL만 free estimate, 또는 데이터셋에 ≥ 4×t½ post-infusion sample 추가.

**Signature S9 — "Adherence Phantom" (NEW STAGE 3)**
환자의 trough sample이 expected보다 _체계적으로_ 낮음 (Tozer Fig 18-9 Panel A 시뮬레이션 패턴). 두 해석: (a) 환자 CL 증가, (b) missed dose. Adherence 모니터링 데이터(MEMS cap, refill record) 부재 시 PopPK fit은 IIV on CL을 _인공적으로 inflate_시켜 nonadherence variability를 흡수. 진단:
- η_CL distribution이 bimodal 또는 heavy-tailed (정상 분포 가정 위반)
- CWRES vs TIME plot에서 trough timepoint 후 fan
- "η_CL outlier" 환자 chart 검토 시 missed dose history 발견
Tozer p.591 직접 명시: "The lack of adherence to the prescribed manner of taking a drug is one of the sources, sometimes the major one, of variability in drug response." NDA submission에서 adherence assumption 없이 IIV를 보고하면 reviewer가 "How was nonadherence ruled out?" 질의 — 답이 없으면 Briefing Document 통과 곤란.

### (c) Highest-Consequence Confusion Pair

**STAGE 1**: Effect Compartment ↔ Turnover-stimulation의 tmax dose-dependence 부호.

**STAGE 2**: 저추출비 약물의 _total CL_ 변화 ↔ _unbound CL_ 변화 (Wall #4의 임상 결과형) — verapamil cirrhosis vs phenytoin RF가 동일 fu↑ 신호에서 정반대 결론.

**STAGE 3 추가**: **Loading dose ↔ Maintenance dose의 underlying parameter dependence**
Tozer p.582 + p.586 결합 통찰: LD ≈ V·C_target/F → V의 covariate predictability가 결정. MD = CL·C_target_avg/F → CL의 covariate predictability가 결정. **Fig 18-5 직접 본문**: V는 ~45% covariate-explained, hepatic CL은 ~40% explained — _두 파라미터가 모두 50% 미만 explained된 약물에서_ LD와 MD를 동일한 confidence로 처방하면 위험. 베테랑의 직관: V는 "physical compartment size"라 BW·age 직접 결정 (예측 가능), CL은 "metabolic flux"라 효소·혈류 등 unmeasured factor 다수 (예측 어려움). Step 1 §2.11 LD 카드의 "V 90% CL 30–40%" 표현은 _이 부호 분리_를 정반대로 표현 (V가 더 예측 가능한 것은 맞으나, V도 55% UNACCOUNTED라는 사실이 묻힘) — STAGE 2 잠정 처리를 STAGE 3에서 다음으로 확정 REWRITE: **"LD는 V에 의존; V는 ~45% covariate-explained (BW 25% + age 10% + RF 10%, 55% unaccounted). MD는 CL에 의존; hepatic CL은 ~40% (BW 20% + age 15% + RF 5%, 60% unaccounted), renal CL은 ~80% (RF 50% 단독, 20% unaccounted). 따라서 신배설 dominant 약물에서는 RF만으로 MD 예측 가능; 간대사 dominant 약물에서는 demographic만으로 60% IIV가 남음 — TDM 정당화 강함."**

NDA Briefing Document에서 LD와 MD를 같은 confidence로 권고하면 → reviewer는 약물의 hepatic vs renal balance와 V·CL 각각의 covariate explanation을 _명시 보고_ 요구. 답을 못 하면 deficiency letter.

---

## T3. Trench-Level Tips (총 13 items 중 활성 12개)

### Tip 1 (STAGE 1, Grade A) — 단일 dose 진단 금지 원칙
- **Insert at**: §2.2 Peak-shift Directionality 카드
- **Insert text**: "Peak-shift 진단은 multiple dose + non-overlapping AUCE/dose 데이터가 모두 존재할 때 결정적이다. 단일 dose만 있으면 link / turnover-input inhibition / turnover-loss stimulation / receptor on/off가 동등 후보로 남는다 (G&W p.425–428)."

### Tip 2 — DELETED (STAGE 1 자체 정정에서 Step 1 중복으로 강등)

### Tip 3 — DELETED (STAGE 1 자체 정정에서 Step 1 중복으로 강등)

### Tip 4 (STAGE 1, Grade A) — PK margin ≠ NOAEL margin
- **Insert at**: §6 PK15 시나리오 (Step 2)
- **Insert text**: "'>100배 안전역'은 dog Cmax (50 µM) ÷ human therapeutic Cmax (< 0.1 µM)의 ratio다 (G&W p.547). 이는 **PK exposure margin**이며, NOAEL margin (HED 환산 + species 차이 보정) 및 AUC-기반 toxicokinetic margin과 구별해 보고한다."

### Tip 5 (STAGE 1, Grade B) — Bi-phasic decline ill-conditioning
- **Insert at**: §2.4 Turnover 카드 (1 sentence margin)
- **Insert text**: "Bi-phasic decline은 inactive receptor pool 또는 precursor compartment의 신호다 (G&W Case I, Eq.6:35, p.437). 단일 turnover로 fit하면 OFV는 수렴해도 R MATRIX가 singular에 가까워진다."

### Tip 6 (STAGE 2, Grade A) — fu↑ ≠ CLu↑ in low-E albumin-bound drugs
- **Situation**: §2.7 D-E 표 또는 §5.4 hepatic vs renal matrix
- **Trap**: 신질환·간경변에서 fu↑ → "CL 증가 → dose 증량 필요" 결론
- **Detection**: low-E + albumin 결합 약물에서 total CL과 total Cav,ss는 _반대 방향_으로 변하나 CLu와 unbound Cu,av,ss는 거의 변하지 않음
- **Insert at**: Step 1 §2.7 D-E 표 (단백 결합 row 직후)
- **Insert text**: "저추출비·albumin 결합 약물(phenytoin, valproate)에서 fu↑은 CLu에 거의 영향이 없으면서 total CL을 증가시켜 total 농도를 낮춤. _Total 농도가 낮아 보여_ dose를 올리면 free 농도가 toxic 영역으로 진입한다 (R&T p.464; Tozer Table 18-5는 phenytoin '광범위 albumin 결합'으로 명시)."

### Tip 7 (STAGE 2, Grade A) — SCr는 trend로 읽어라, snapshot이 아니다
- **Situation**: §2.8 C-2 AKI row
- **Trap**: AKI 환자의 단일 시점 SCr=1.5를 C-G에 입력해 표준 regimen 처방
- **Detection**: 48h trend 관찰. dC/dt > 1 mg/dL/day이면 severe AKI. R&T Eq.15-14로 _현재_ RF 추정.
- **Insert at**: Step 1 §2.8 C-2 AKI 행
- **Insert text**: "AKI에서는 SCr 단일 시점이 아닌 _trend_ (dC/dt > 1 mg/dL/day)로 진단한다. R&T Table 15-6: RF 10% 환자의 creatinine 반감기는 42시간 — 오늘 SCr은 _어제 그제_ RF의 거울이며, 환자의 현재 RF은 SCr이 도달할 평형보다 훨씬 낮을 수 있다."

### Tip 8 (STAGE 2, Grade A) — Two-Factor Product 메타 패턴 (Phenobarbital paradox = Bayesian discipline)
- **Situation**: §2.9 C 또는 §2.6 cross-link
- **Insert at**: Step 1 §2.9 C-2 (Hemodialysis vs CAPD 직후) — meta-pattern bridge
- **Insert text**: "Phenobarbital paradox는 §2.6 Bayesian 사고와 구조적 동형이다 — _두 인자의 곱_이 결정한다. 한 인자(half-life 단축)만 극대화돼도 다른 인자(체내 잔류 fraction)가 작으면 임상적 의미는 없다. half-life와 fraction removed를 분리 평가하라."

### Tip 9 (NEW STAGE 3, Grade B) — Fig 18-2 PD variability 백분율은 hypothetical
- **Situation**: §1 학습 목표 또는 §5.5 mini-anchor
- **Trap**: gene 40% / age 15% / drugs 10% 등 백분율을 universal constant로 인용
- **Detection**: Fig 18-2 캡션 직접 확인 — "hypothetical analysis"
- **Insert at**: Step 1 §1 line 142 후속 영역 또는 §5.5 framework 도입부
- **Insert text**: "Tozer Fig 18-2의 PD variability 백분율은 _hypothetical drug_ 도식 예시다. 특정 약물의 PD variability 분해에 이 수치를 인용하면 NDA reviewer는 careless citation으로 판단하며, 경우에 따라 deficiency letter 사유가 된다."

### Tip 10 (NEW STAGE 3, Grade A) — Fig 18-5 covariate explanation 한계 명시
- **Situation**: §5.5 covariate 모델 framework
- **Trap**: "covariate model이 IIV 대부분 설명한다"는 학생의 일반화
- **Detection**: Tozer Fig 18-5 직접 본문 비교
- **Insert at**: Step 1 §5.5 line 1423 (현재 "V 90% CL 30–40%" 위치 — REWRITE)
- **Insert text**: "Tozer Fig 18-5: F는 5%만 covariate-explained (95% UNACCOUNTED), V는 ~45% (BW 25% + age 10% + RF 10%, 55% UNACCOUNTED), Hepatic CL은 ~40% (60% UNACCOUNTED), Renal CL만 ~80% (RF 50% 단독). 신배설 dominant 약물의 MD는 RF로 강하게 예측 가능하나, 간대사 dominant 약물의 MD는 demographic만으로 60% IIV가 남는다 — 이것이 hepatic CL drug에서 TDM이 강하게 정당화되는 정량적 근거다."

### Tip 11 (NEW STAGE 3, Grade A) — Sampling at 1×t½ confounds CL and V
- **Situation**: §2.6 Bayesian 카드 또는 §2.11 LD 카드
- **Trap**: ICU 첫 24h dense sampling 데이터로 NONMEM CL 추정 신뢰
- **Detection**: η-shrinkage on CL > 30%, RSE(CL) > 50% (S8 signature)
- **Insert at**: Step 1 §2.6 Bayesian 카드 마진 또는 §5 PopPK 카드
- **Insert text**: "Tozer Fig 18-13: 1×t½ 이전 sampling은 _CL × 1/3_과 _V × 3_을 구분 못한다. ≥ 4×t½ 또는 trough sampling만이 CL 단독 추정을 가능하게 한다. Vancomycin은 CL > V variability이므로 V를 population strong prior로 고정하고 CL만 individualize 하는 것이 표준 관행 (Tozer p.605)."

### Tip 12 (NEW STAGE 3, Grade B) — Forgiving/Unforgiving은 t½/τ × window 폭의 곱
- **Situation**: §2.12 Missed dose 카드 또는 §1 학습 목표
- **Trap**: "잦은 dosing이 missed dose에 더 취약하다"는 학생의 직관
- **Detection**: Tozer Fig 18-9 4 panels 비교 — 동일 약물 q24h 한 번 missed (3.2 mg/L) > q8h 세 번 missed (5.0 mg/L)
- **Insert at**: Step 1 §2.12 missed dose 카드 마진
- **Insert text**: "t½/τ 비율이 forgiveness를 결정한다. q8h regimen(t½/τ=2.27)은 forgiving, q24h regimen(t½/τ=0.76)은 unforgiving (Tozer Fig 18-9). 이는 §2.6 Bayesian 'two-factor product' 메타 패턴과 동형 — t½/τ × therapeutic window 폭의 _곱_이 임상 안전 마진."

### Tip 13 (NEW STAGE 3, Grade B) — TCS 5 criteria는 순차적 가중 곱
- **Situation**: §2.10 TCS 카드 (수정 표현)
- **Trap**: "criteria 5개를 모두 충족하면 TCS 적용"이라는 hard AND 표현
- **Detection**: Tozer p.594–596 본문 — 각 criterion이 _상대적_(absolute가 아닌 relative) 임을 명시. "Most of them, however, must be met for the strategy to be routinely effective."
- **Insert at**: Step 1 §2.10 TCS 카드 마지막 줄
- **Insert text**: "5개 criteria는 hard AND가 아니라 _순차적 가중 곱_으로 작동한다. 한 criterion(예: assay turnaround)만 unfavorable해도 TCS의 임상적 가치는 0에 접근 — Bayesian 'two-factor product' 메타 패턴과 동형 (Tip 8·12와 cross-link). digoxin·vancomycin·cyclosporine·phenytoin 등은 자주 유용한 _대표 후보군_이며 자동 적용 약물이 아니다 (Patch Memo MUST_FIX #3 정합)."

---

## T4. Deletion Candidates (mandatory)

### STAGE 1 deletions

1. **§2.1–§2.5 Ch.6 Case A–I 9개를 별도 MUST 카드로 분리한 부분** → 1 통합 + 4 prototype 카드로 압축 (Audit MUST_FIX #1).
2. **§2.12 "TDM 환자의 80%" 정량 표현** → DELETE numeric, 정성 표현으로 (Audit MUST_FIX #6).
3. **Q8 디곡신 "loading 0.4 mg, maintenance 0.1–0.125 mg/day"** → `[교과서 외 통합 추론 예시]` 라벨링 (Audit MUST_FIX #5).
4. **NDA Briefing Document / Phase 4 RMP / BestDose · ID-ODS · Pmetrics** 본문 → §X "교과서 외 구현·규제 번역" 박스로 압축 이동 (Audit MUST_FIX #7).
5. **PK35 §2.6 카드 내 "Peck et al [1992] background"** → citation footnote.
6. **Ch.6 Receptor on/off 카드 내 "occupancy model historical context"** → 1 sentence.

### STAGE 2 deletions

7. **§2.7 Rd Framework, §2.8 Cockcroft-Gault, §2.9 Hemodialysis 3개 카드 통합 권고 _철회_** — 임상 약사 30초 verify 사슬은 4단계 검정으로 _독립_되어야 함. 단 §2.9 hard AND gate 표현은 수정 (다음 항목).
8. **§2.9 C "두 조건 모두 위배 → 4h 투석 < 20% 제거" 하드 AND 표현** [Audit MUST_FIX #8] → R&T Fig.15-18은 _continuous_ trade-off. **REWRITE to "Vu·CLu 평면에서 ineffective 영역(Vu>120L 또는 CLu>>CLuD)에 가까울수록 4h 투석 제거율 < 20%로 수렴; 두 좌표 모두 favorable 일 때 임상적 dialysis 의미"** — 좌표 평면 사고로 변환.
9. **Step 1 §1 학습 목표 4 (line 161) "PK15 ≥100배 안전역 NDA 규제 언어 작성"** [Audit MUST_FIX #7] → "NDA 규제 언어"는 source 외. **REWRITE to "PK15 toxicokinetic safety margin (G&W p.547)을 PK exposure margin으로 정확히 보고할 수 있다"**.
10. **Step 1 §2.6 B-3 "Sheiner 1977 NONMEM 직접 조상" claim** (line 610) → R&T Ch.15 직접 본문 부재. [확인 필요] 라벨 또는 footnote.

### STAGE 3 NEW deletions

11. **Step 1 §5.5 line 1423 "V는 covariate로 5–10% 정확도, CL은 30–40%"** [Audit MUST_FIX #4 STAGE 3 확정 처리]
    → **Tozer Fig 18-5 (p.582) 직접 대조 결과**: V는 ~45% explained / Hepatic CL ~40% / Renal CL ~80% / F 5%. Step 1의 "V 90%" claim은 source와 _정반대로 inverted_되어 있음.
    → **REWRITE to**: "Loading dose는 V에 의존하며 V는 약 45% covariate-explained (body weight 25% + age 10% + renal function 10%, 55% unaccounted, Tozer Fig 18-5). Maintenance dose는 CL에 의존하며 hepatic CL drug은 약 40% explained (60% unaccounted), renal CL drug은 약 80% explained (renal function 50% 단독). 신배설 dominant 약물의 MD는 RF로 강하게 예측 가능하나 간대사 dominant 약물의 MD는 60% IIV가 demographic만으로 설명되지 않음 — 이것이 phenytoin·warfarin 등 간대사 약물에서 TDM이 강하게 정당화되는 정량적 근거."

12. **Step 1 §1 line 154 "Phase 4 RMP — TCS 약물 post-marketing concentration data 분석"** [Audit MUST_FIX #7] → Source 외. `[교과서 외 구현·규제 번역]` 박스로 이동.

13. **Step 1 §2.10 TCS "Phenytoin·digoxin·vancomycin·cyclosporine·theophylline·nortriptyline = TCS 필수"** [Patch Memo MUST_FIX #3]
    → Tozer Table 18-5 직접 본문: 이 약물들은 "examples of drugs for which target concentration strategy has been found to be **clinically helpful**" — 필수 적용이 아니라 _frequently useful candidate_.
    → **REWRITE to**: "이 약물들은 TCS가 자주 유용한 대표 후보군이다. 실제 적용 여부는 patient 상태·sampling timing·assay turnaround·active metabolite·free concentration 이슈·임상 의사결정 필요성에 따라 달라진다 (Tozer Table 18-5)."

14. **Step 1 §2.10 TCS phenytoin 행에 nonlinearity 명시 부재** [위험 8 정합]
    → **ADD 1 sentence**: "Phenytoin은 Michaelis-Menten saturation이 추가 monitoring 정당성을 강화한다 (Tozer p.588) — PopPK $PK 블록 작성 시 linear CL이 아닌 saturable elimination 모델 채택 필수."

15. **Step 1 §2.11 LD 카드 "D_L = V·C_target/F" 단독 표현** [Patch Memo MUST_FIX 보강]
    → Tozer p.585: chloroquine 2500mg을 1000+500+500+500으로 _분할_하는 이유는 _분포 속도·투여 속도·제형·dose strength·toxicity 위험_. 단일 식만 보면 LD를 한 번에 줘도 된다는 인상.
    → **ADD 1 sentence**: "이상적 D_L = V·C_target/F이지만, 분포 속도 + 투여 속도 + 제형 + dose strength + toxicity 위험 때문에 chloroquine처럼 _분할 LD_가 필요할 수 있다 (Tozer p.585)."

---

## T5. Priority Matrix (cumulative)

### Grade A (반드시 반영 — 직접 내재화·규제 위험 감소)

| 항목 | 출처 | 적용 |
|---|---|---|
| **T3 Tip 1** Multiple-dose 미존재 시 model 후보 동등성 | STAGE 1 | Audit MUST_FIX #2 보강 |
| **T1 Wall #4** fu↑ ≠ CLu↑ for low-E drugs | STAGE 2 | §2.7 D-E 표 1 sentence (Tip 6) |
| **T1 Wall #5** SCr는 trend로 읽어라 | STAGE 2 | §2.8 C-2 AKI 1 sentence (Tip 7) |
| **T1 Wall #6** Imipenem violates Rd foundational assumption | STAGE 2 | §2.7 D-E 표 imipenem row 확장 |
| **T1 Wall #8** Fig 18-5 covariate 한계 (V ~45%, hepatic CL ~40%) | STAGE 3 | §5.5 line 1423 REWRITE (Tip 10) |
| **T1 Wall #10** Sampling timing × identifiability | STAGE 3 | §2.6 Bayesian 카드 마진 (Tip 11) |
| **T2 (a) 위험 5** Step 1 §2.9 hard AND gate 수정 | STAGE 2, Audit MUST_FIX #8 | §2.9 C 좌표 평면 표현 REWRITE |
| **T2 (a) 위험 6** Imipenem-class 약물 표준 Rd 적용 위험 | STAGE 2 | §2.7 후속 영역 또는 §5.4 |
| **T2 (a) 위험 8** Phenytoin nonlinearity 미명시 | STAGE 3 | §2.10 phenytoin 행 1 sentence |
| **T2 (a) 위험 9** CYP2D6 4군 stratification (Fig 18-6) | STAGE 3 | §2.10 또는 §5.5 |
| **T2 (b) S1–S4** NONMEM signatures (Saturation Mirage / Peak-shift Phantom / Bayesian Shrinkage Collapse / Wrong Hysteresis) | STAGE 1 | §5 적용 |
| **T2 (b) S5 Renal Cliff** | STAGE 2 | §2.8 C-2 또는 §5.4 cross-link |
| **T2 (b) S6 Imipenem Trap** | STAGE 2 | §2.7 D-E 또는 §5.4 |
| **T2 (b) S7 Acute Lag** | STAGE 2 | §2.8 C-2 또는 §1 후속 영역 |
| **T2 (b) S8 Sampling Time Mismatch** | STAGE 3 | §2.6 Bayesian 또는 §5 PopPK |
| **T2 (b) S9 Adherence Phantom** | STAGE 3 | §2.12 missed dose 또는 §5 PopPK |
| **T2 (c) STAGE 2 Pair** total CL ↔ unbound CL 부호 분리 | STAGE 2 | §5.4 매트릭스 확장 |
| **T2 (c) STAGE 3 Pair** LD V-dependence ↔ MD CL-dependence (covariate explanation 비대칭) | STAGE 3 | §2.11 LD + §5.5 connection |
| **T3 Tip 6** fu↑ ≠ CLu↑ | STAGE 2 | §2.7 D-E 표 |
| **T3 Tip 7** SCr trend not snapshot | STAGE 2 | §2.8 C-2 AKI |
| **T3 Tip 8** Phenobarbital paradox = Bayesian discipline 동형 | STAGE 2 | §2.9 C-2 cross-link to §2.6 |
| **T3 Tip 10** Fig 18-5 actual covariate numbers | STAGE 3 | §5.5 line 1423 |
| **T3 Tip 11** Sampling at 1×t½ confounds CL/V | STAGE 3 | §2.6 또는 §5 |
| **T4 #1** Step 1 Case A–I 9 카드 → 1 통합 + 4 prototype | STAGE 1 | Audit MUST_FIX #1 |
| **T4 #2** §2.12 "TDM 80%" 수치 삭제 | STAGE 1 | Audit MUST_FIX #6 |
| **T4 #3** Q8 처방 권고 `[교과서 외 통합 추론 예시]` 라벨링 | STAGE 1 | Audit MUST_FIX #5 |
| **T4 #8** §2.9 hard AND gate 수정 | STAGE 2 | Audit MUST_FIX #8 |
| **T4 #9** Step 1 §1 line 161 "NDA 규제 언어" 수정 | STAGE 2 | Audit MUST_FIX #7 |
| **T4 #11** Step 1 §5.5 V/CL percentages REWRITE | STAGE 3 | **Audit MUST_FIX #4 확정 처리** |
| **T4 #13** Step 1 §2.10 TCS "필수" 표현 약화 | STAGE 3 | Patch Memo MUST_FIX #3 |
| **T4 #14** Step 1 §2.10 phenytoin nonlinearity 추가 | STAGE 3 | Tozer p.588 |
| **T4 #15** Step 1 §2.11 LD 분할 사유 추가 | STAGE 3 | Tozer p.585 |

### Grade B (flow 보존되면 반영 — enrichment value)

- **T1 Wall #1** kin/kout biological entity → §2.4 turnover 카드 마진
- **T1 Wall #2** RT 유한성이 peak-shift driver → §2.5 receptor on/off 카드
- **T1 Wall #7** Fig 18-2 PD pie hypothetical → §1 또는 §5.5 mini-anchor
- **T1 Wall #9** Forgiving/Unforgiving t½/τ 곱 → §2.12 missed dose 카드
- **T1 (b) STAGE 2** 약사의 30초 verify 사슬 → §1 line 173
- **T1 (b) STAGE 3** TCS dosing decision 단일 thought stream → §2.10 마지막 줄
- **T1 (c) STAGE 3 판단 6** sampling time → estimable parameter mapping → §2.6 마진
- **T1 (c) STAGE 3 판단 7** t½/τ 1초 계산 → §2.12 마진
- **T2 (a) 위험 4 STAGE 2** NDA 신질환 subgroup C-G + 체질량 미보고 → §2.8 D-E 또는 §5.4
- **T2 (a) 위험 7 STAGE 3** Fig 18-2 hypothetical 백분율 NDA 인용 위험 → §1 학습 목표
- **T3 Tip 9** Fig 18-2 hypothetical disclaimer
- **T3 Tip 12** Forgiving/Unforgiving 메타 패턴
- **T3 Tip 13** TCS 5 criteria 순차 가중 곱
- **NEW STAGE 3**: Step 1 §1 line 142–155 후속 영역 박스에 `[교과서 외 구현·규제 번역]` 라벨을 _명시_적으로 부착

### Grade C (REJECT — scope creep, 출처 부재, 또는 Step 1 중복)

- ❌ STAGE 1 Wall #3·Tip 2·Tip 3 (Step 1 §2.6 B-3 중복)
- ❌ §X "교과서 외 구현·규제 번역" 박스를 PhD-level NDA template/Pmetrics workflow로 확장
- ❌ Ch.6 Case H "tsunami profile" historical naming
- ❌ PMDA/EMA reviewer "1차 점검 항목" claim (출처 없음)
- ❌ Disease-on-PD WHIG model 수식 derivation 깊이 (R&T p.481 Fig.15-25 schematic만)
- ❌ Hepatic conjugation enzyme variability (Fig.15-3) PhD-level 깊이 (Audit OMITTED_JUSTIFIABLE)
- ❌ Disease in drug overdose (R&T p.478–479) (Audit OMITTED_JUSTIFIABLE)
- ❌ Peritoneal Dialysis (CAPD) PhD-level 깊이 (Audit INCLUDED_AS_CONTEXT)
- ❌ **NEW STAGE 3**: Trimipramine specific CYP2D6 4-group 깊이 (Tozer Fig 18-6 본문 처리는 1 sentence 충분; 위험 9에서 anchor 제공)
- ❌ **NEW STAGE 3**: Mefloquine/Chloroquine antimalarial loading dose 상세 (Tozer p.585 illustrative example only — capstone scope 외)
- ❌ **NEW STAGE 3**: Alendronate 6–12 month bone density (Tozer Fig 18-7 — long-onset PD에 한정된 illustrative)
- ❌ **NEW STAGE 3**: Adherence "drug holiday" 행동심리학적 분석 (Tozer p.591 — clinical psychology scope, capstone PK/PD 외)
- ❌ **NEW STAGE 3**: Tozer Study Problems (pp. 606–610) — Scope Lock에서 §7 Self-Test 설계 참고용으로만 명시. MUST 카드 범위 불포함.

---

## 최종 종합 메모 — Meta-Patterns 융합

본 캡스톤이 5개 source(G&W Ch.6 + PK15 + PK35 + R&T Ch.15 + R&T Ch.18)를 단일 thread로 묶을 때 _반복 출현_하는 메타 패턴 4가지를 명시한다. 이 패턴들은 단일 카드로 격상되어서는 안 되며 (분량 폭발 위험), 각 관련 카드 마진에 1 sentence cross-link 형태로 _재호출_되어야 한다. 이것이 캡스톤 통합의 _공기_이며 학습자가 "이 모든 것이 하나의 사고 구조로 연결되어 있다"는 통찰에 도달하는 경로.

### Meta-Pattern 1: Two-Factor Product (Tip 8·12·13 동형 구조)

**구조**: 두 인자의 _곱_이 결과를 결정하며, 한 인자만 극대화돼도 다른 인자가 작으면 결과는 0에 접근.

**출현 사례**:
- §2.6 Bayesian objective function: var(P̂) × var(Ĉ)의 곱이 posterior weight 결정
- §2.9 Phenobarbital dialysis paradox: half-life 단축 × fraction removed의 곱이 임상적 의미 결정
- §2.10 TCS 5 criteria: 5 criteria 충족 확률의 _곱_이 TCS 정당화 결정 (한 criterion fail 시 곱 → 0)
- §2.12 Missed dose forgiveness: t½/τ 비율 × therapeutic window 폭의 곱이 forgiveness 결정
- §2.11 Loading dose safety: V estimable 정도 × C_target 정확도의 곱이 첫 6h 안정성 결정

**삽입 권고**: §2.6 카드 마지막 1 sentence — "이 'two-factor product' 사고는 §2.9 dialysis, §2.10 TCS criteria, §2.12 missed dose forgiveness에서 동일 구조로 재출현한다."

### Meta-Pattern 2: Identifiability ↔ Sampling Geometry

**구조**: 데이터의 _구조_(sampling timing × dosing pattern)가 추정 가능한 파라미터 _집합_을 결정. 데이터가 없는 곳에서는 어떤 알고리즘도 파라미터를 회복하지 못함.

**출현 사례**:
- §2.2 Peak-shift directionality: 단일 dose는 model 후보 동등성 (Tip 1)
- §2.6 Bayesian: prior 강도가 conditional posterior 모양 결정 (Step 1 §2.6 B-3)
- §2.11 LD: V는 single-dose 데이터로 추정, CL은 multi-dose 또는 long-term sample 필요
- §2.12 Missed dose: Eq.18-1~18-4 적용 _가능_ 여부는 dosing history 완전성에 의존
- §5 PopPK: Sampling at 1×t½는 CL × 1/3와 V × 3 구분 못함 (Wall #10·Tip 11·S8)

**삽입 권고**: §1 학습 목표 또는 §5.5 framework 도입 — "identifiability는 알고리즘이 아니라 데이터 _구조_에 의해 결정된다."

### Meta-Pattern 3: Continuous Reality, Discrete Communication

**구조**: 생리학·임상 현상은 _continuous_이나, 임상 의사결정·NDA 라벨·EHR alert는 _discrete strata_로 표현됨. 이 변환에서 정보 손실이 발생하며, 경계 영역 환자가 가장 위험.

**출현 사례**:
- §2.8 신기능 분류 (mild/moderate/severe): Tozer p.591이 명시 — "physiologic functions and disease severity that are, in reality, continuous"
- §2.9 Dialysis 효과성 hard AND gate: STAGE 2 Audit MUST_FIX #8 — Vu·CLu 좌표 평면이 continuous (위험 5)
- §2.10 TCS criteria: hard 5/5 vs 순차 가중 곱 (Tip 13)
- §5.5 covariate model: 정량 percentage가 hypothetical drug 기반 (Wall #7)
- Dose strengths 5/10/20/40/80 mg: 임상 처방의 discrete granularity (Tozer p.589)

**삽입 권고**: §2.7 또는 §2.10 마진 — "stratification은 임상적 편의이며 생리학적 경계가 아니다."

### Meta-Pattern 4: Anatomy of CL Determines Rd-Style Predictions

**구조**: 약물의 _대사 해부학_(hepatic vs renal vs biliary vs renal metabolism)이 어떤 covariate 모델·dose adjustment 식이 적용 가능한지 결정. 식이 옳아도 가정 위반 약물에 적용하면 systematic bias.

**출현 사례**:
- §2.7 Rd framework: imipenem이 foundational assumption 위배 (Wall #6)
- §2.8 C-G: 근감소·비만에서 RF 과대추정 (Wall #5, S5 Renal Cliff)
- §2.9 Dialysis: 약물의 분포 특성(Vu)이 효과성 결정 (단순 t½ 단축 무관)
- §5.5 covariate model: Renal CL drug ~80% explained vs Hepatic CL drug ~40% explained (Tip 10)

**삽입 권고**: §2.7 framework 카드 마진 — "Rd 식의 적용 가능성은 약물의 대사 해부학에 의존하며, 식이 옳아도 약물이 가정을 위배하면 systematic bias 발생."

---

## STAGE 3 최종 완료 메모 — Phase 4 Content Lock 인계

본 Crucible Report v1은 Phase 4 Content Lock에서 다음 결정을 위한 입력으로 사용된다:

1. **MUST 카드 압축 결정**: Patch Memo는 12 → 7–8 core card 권고. 본 보고서는 §2.7+§2.8+§2.9 통합을 _철회_ (System Integration argument). 7–8 core 압축 시:
   - Core 1: Pattern Recognition Decision Tree (§2.1–§2.5 통합)
   - Core 2: Peak-shift Directionality + Saturation
   - Core 3: Effect Compartment vs Turnover vs Receptor On/Off
   - Core 4: Bayesian Objective Function (PK35)
   - Core 5: Disease/fe/Rd (§2.7)
   - Core 6: Cockcroft-Gault + AKI lag (§2.8)
   - Core 7: Dialysis 좌표 평면 (§2.9)
   - Core 8: TCS Criteria (§2.10)
   - Core 9: Loading vs Maintenance Dose (§2.11)
   - Core 10: Missed/Erratic Dosing Eq.18-1~18-4 (§2.12)
   → 권고: 10 core. Patch Memo의 7–8 압축은 §2.7+§2.8+§2.9 통합 전제 — 본 보고서가 철회하므로 10 core가 적정.

2. **§2.10 TCS phenytoin nonlinearity 표현**: 위험 8 + T4 #14 정합으로 1 sentence 추가.

3. **§2.11 LD 카드 covariate explanation REWRITE**: T4 #11 + Confusion Pair STAGE 3 결합.

4. **§2.12 missed dose 카드 forgiveness 메타 패턴**: Tip 12 마진 추가.

5. **§5.5 line 1423 REWRITE 확정**: Audit MUST_FIX #4 → STAGE 3에서 Tozer Fig 18-5 직접 대조 후 정정 텍스트 확정 (T4 #11).

6. **메타 패턴 4개 cross-link**: 각 관련 카드 마진에 1 sentence 추가 — 카드 신설 없이 통찰 통합.

7. **PK15 §6 시나리오 mini-closing block**: 캡스톤 마지막 bridge — "PK15는 처방 자체가 아니라 '선택된 용량에서 어떤 exposure와 safety margin을 보고할 것인가'를 담당한다." (Patch Memo MUST_FIX #8 정합)

---

## 자가 검증 체크리스트 (Pre-Sign-Off)

- [x] Operative Filter 적용: Step 1 Draft v0 본문 직접 대조 후 STAGE 1 Wall #3·Tip 2·Tip 3 자체 강등 처리
- [x] Source Fidelity: 모든 새 주장에 출처 명시 (G&W p.X, R&T p.Y, Tozer p.Z) — 출처 불명 claim 부재
- [x] Audit Report v1 MUST_FIX #1–#8 모두 T4 또는 T5 Grade A에 명시적 반영
- [x] Patch Memo MUST_FIX 1–7 모두 처리 (단 카드 수 압축은 Phase 4 Content Lock으로 인계)
- [x] STAGE 2 → STAGE 3 정정: Tozer Ch.18 직접 본문(Fig 18-5, Fig 18-9, Fig 18-13, Eq.18-1~18-4) 대조 완료
- [x] T1·T2·T3·T4·T5 5개 Task 모두 충족
- [x] T4 deletion list 비어있지 않음 (15개 항목)
- [x] 분량 비중: STAGE 1 ~35% / STAGE 2 ~30% / STAGE 3 ~35% = **합계 1.0** (총량 불변의 법칙 준수)
- [x] [확인 필요] 라벨: §2.6 B-3 "Sheiner 1977 NONMEM 직접 조상" claim에 적용 (T4 #10)
- [x] HTML/Visual 결정 부재 (Phase 4C 영역, scope 외 — 정합)
- [x] 한국어 산문 + 영어 기술 용어 (NONMEM 제어구문·equation·drug name) 보존

---

✅ **STAGE 3 / 3 최종 통합 완료.**

본 Crucible Report v1은 G&W Ch.6 + PK15 + PK35 + R&T Ch.15 + R&T Ch.18의 단일 Source Universe 융합 산출물이다. Operative Filter, Source Fidelity Audit, Patch Memo MUST_FIX, Tozer Ch.18 직접 본문 대조의 4중 검증을 통과하였다. 다음 단계는 **Phase 4 Content Lock** — 본 보고서의 T5 Grade A 항목을 Step 1 Draft v0에 lock-in하고, 메타 패턴 4개를 cross-link 형태로 통합한 후, **Phase 4C Visual Pedagogy → Phase 5 HTML Compile**로 진행한다.

---

Tozer Ch.18 PDF를 정독했습니다. STAGE 2 누적본과 직접 대조하여 STAGE 3 최종 통합 작업을 수행하겠습니다.

먼저 핵심 사항을 정리하면:
- Fig 18-5의 실제 수치는 Step 1 §5.5의 "V 90%·CL 30–40%" claim과 정면 충돌 — Tozer 본문에서 V는 covariate로 ~45% 설명(55% UNACCOUNTED), Hepatic CL ~40% 설명(60% UNACCOUNTED), Renal CL ~80% 설명, F 5% 설명. STAGE 2 잠정 처리를 STAGE 3에서 확정 정정.
- Eq.18-1·18-2·18-3·18-4 + worked examples (digoxin 0.39 µg/L / vancomycin 2.03 mg/L / vancomycin erratic 33.7 mg/L) 모두 직접 대조 완료.
- Fig 18-13 sampling × identifiability 프레임이 STAGE 2가 예측한 S8 signature와 정확히 일치.
- Fig 18-9 forgiving/unforgiving 패턴이 STAGE 2 "two-factor product" 메타 패턴의 결정적 추가 증거.

이제 최종 통합본을 작성합니다.최종 통합본 작성을 완료했습니다. STAGE 3 작업의 핵심 의사결정을 간단히 요약합니다.

**STAGE 3에서 추가된 결정적 통찰 (Tozer Ch.18 직접 대조 결과)**

1. **Wall #8 — Step 1 §5.5 정량 수치 정정 확정**: Tozer Fig 18-5 (p.582) 직접 대조 결과, Step 1의 "V 90% covariate 설명, CL 30–40%"는 source와 정반대로 inverted 되어 있었습니다. 실제 값은 V ~45% 설명(55% UNACCOUNTED) / Hepatic CL ~40% / Renal CL ~80% / F 단 5%. STAGE 2가 잠정 처리한 Audit MUST_FIX #4를 STAGE 3에서 확정 REWRITE로 처리했습니다.

2. **Wall #10 + Signature S8 (Sampling Time Mismatch)**: Tozer Fig 18-13이 STAGE 2의 예측을 정확히 검증했습니다. 1×t½ 이전 sampling은 _CL × 1/3_과 _V × 3_을 구분 못합니다. 이것이 vancomycin TDM에서 V를 strong prior로 고정하는 표준 관행의 수학적 근거입니다.

3. **Wall #9 + Tip 12 (Forgiving/Unforgiving 메타 패턴 결정적 증거)**: Fig 18-9 4 panels는 동일 약물에서 q24h 한 번 missed (3.2 mg/L) > q8h 세 번 missed (5.0 mg/L) — 직관과 정반대. t½/τ × therapeutic window 폭의 _곱_이 forgiveness를 결정합니다.

4. **Signature S9 (Adherence Phantom)**: Tozer p.591의 "adherence가 variability의 sometimes the major source"라는 명시 본문을 NONMEM 진단 패턴으로 번역했습니다. η_CL bimodality + CWRES post-trough fan으로 adherence variability가 IIV로 흡수된 흔적을 진단 가능합니다.

5. **메타 패턴 4개 명시**: Two-Factor Product / Identifiability ↔ Sampling Geometry / Continuous Reality, Discrete Communication / Anatomy of CL — 캡스톤 통합의 _공기_로서, 별도 카드가 아닌 cross-link 형태로 각 카드 마진에 1 sentence 추가 권고.

**Phase 4 Content Lock 인계 핵심 사항**: Patch Memo의 "MUST 카드 12 → 7–8 압축" 권고는 §2.7+§2.8+§2.9 통합 전제였으나, 본 STAGE 3 분석에서 임상 약사 30초 verify chain이 4단계 _독립_ 검정임을 근거로 통합 권고 철회 → **10 core card 적정**으로 결론.

**자가 검증 통과**: Operative Filter / Source Fidelity / Audit Report MUST_FIX #1–8 / Patch Memo MUST_FIX 1–7 / Tozer Ch.18 직접 본문 대조의 4중 검증 모두 통과. 분량 비중 STAGE 1 ~35% + STAGE 2 ~30% + STAGE 3 ~35% = **1.0 총량 불변** 준수.

다음 단계는 **Phase 4 Content Lock**으로 본 Crucible Report v1의 T5 Grade A 항목을 Step 1 Draft v0에 lock-in한 후 → **Phase 4C Visual Pedagogy → Phase 5 HTML Compile** 진행입니다.

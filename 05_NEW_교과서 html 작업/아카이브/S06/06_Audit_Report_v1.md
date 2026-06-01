# 06_Audit Report v1 — Source Fidelity Audit

**업무 형태:** 파일 분석 / PDF 대조 감사 / 웹 검색 OFF  
**입력:** `06_G_NCA·노출 평가 MRT·비구획 실무(2).pdf`, `06_T_NCA·노출 평가 MRT·비구획 실무(2).pdf`, `06_step1_draft_v0.md`, `S06_phase1_patch memo.md`, 감사 프롬프트  
**산출:** `06_Audit Report v1`  
**감사 역할:** Source Fidelity Auditor — 재작성·문장 개선·교육적 보강이 아니라, Draft v0의 사실·수식·수치·예시가 PDF에 의해 지지되는지 검증

---

## Executive Verdict

**최종 판정: Conditional Go / 재작성 불필요 / Phase 4A 패치 필수**

Draft v0의 큰 구조는 좋다. `C1 AUC`, `C2 AUMC/MRT`, `C3 CL·Vss·Vz·투여경로 보정`, `C4 exposure metrics`의 4-card 구성은 Gabrielsson §2.8-§2.9와 R&T Appendix A/H의 핵심을 대체로 잘 반영한다. 특히 다음 중심축은 원문과 잘 맞는다.

- NCA는 특정 compartment model을 요구하지 않지만, sampling compartment에서의 elimination은 linear라고 가정한다.
- AUC는 zero moment, AUMC는 first moment이며, higher moments는 계산 오차 때문에 일반적으로 쓰지 않는다.
- linear/log-linear trapezoidal rule, λz 추정, AUC/AUMC 외삽, MRT, CL, Vss, Vz는 이 세션의 핵심 수식 흐름이다.
- 짧은 half-life가 긴 input time에 비해 매우 짧을 때 Eq.2:366/2:367이 Eq.2:328/2:337보다 robust하고 zero/negative Vss를 피한다.
- §2.9의 핵심은 dose보다 systemic exposure, 특히 total 또는 unbound systemic plasma concentration을 보라는 것이다.
- PK41은 NCA가 nonlinear regression의 **initial parameter estimates**로 쓰이는 대표 사례다.

그러나 Draft v0에는 PDF 직접 근거가 없는 실무·규제 확장과 몇 가지 명시 오류가 있다. 특히 `λz 오류 30–50%`, `AUMC 외삽 30–60%`, `FDA 21 CFR 320 / 90% CI 80–125% / Clinical Hold / NDA Deficiency Letter`, `R&T Table A-1 zileuton`, `2–4 half-lives`, `V_z ≥ Vss always`, `PK41 수치 anchor 배제`는 Phase 4A 이전에 반드시 처리해야 한다.

---

## T1: Equation/Numerical Audit

| Item | Draft v0 Expression | PDF Source | Classification | Correction |
|---|---|---|---|---|
| NCA 정의 | “NCA는 model-free가 아니라 compartment-free이며, linear elimination 가정이 핵심” | G p.141 §2.8.1: specific compartmental model은 요구하지 않지만 sampling compartment elimination은 linear assumed | MATCH | 유지 가능. 단, “model-free가 아니다”는 원문 직문이 아니라 해석이므로 `[해석]`으로 두면 더 안전. |
| NCA output이 nonlinear에서는 “모델 추정 입력으로만 살아남는다” | Turbojoint 같은 dose-dependent CL에서 NCA 결과는 다음 회귀 모델 초기 모수 입력 | G p.661-664 PK41: NCA로 initial estimates를 얻고 nonlinear regression fit | RESTORED | PK41에는 명확히 지지됨. 다만 모든 nonlinear 상황에 “only”라고 일반화한 표현은 과강. “PK41처럼 초기 모수 입력으로 전환된다”로 제한. |
| λz 오류 30–50% | “1개 포인트만 잘못 포함해도 외삽 AUC가 30–50% 왜곡” | G p.146-148: 3-4 observations, 20-25% extrapolated AUC 권고는 있음. 특정 30-50% 왜곡 수치는 없음 | NOT_IN_SOURCE | 숫자 삭제 또는 `[교육용 가상 시나리오]` 태그. MUST_FIX. |
| BA/BE 90% CI 80-125% | “NDA BA/BE 제출의 90% CI (80-125%)를 흔든다” | 지정 PDF에는 BA/BE 80-125% 기준 없음 | NOT_IN_SOURCE | PDF fidelity 기준에서는 삭제/외부 규제 연결로 분리. REJECT for source-anchored body. |
| Linear trapezoidal AUC | `AUC_0^tlast = Σ((Ci+Ci+1)/2)Δt` | G Eq.2:310 p.143; R&T Table A-1/A-1 figure | MATCH | 유지. |
| Linear trapezoid bias | 하강 구간 overestimate, 상승 구간 underestimate | G p.142 Fig 2.115 | MATCH | 유지. |
| Log-linear trapezoid AUC | `AUC_i^{i+1} = (Ci-Ci+1)/ln(Ci/Ci+1)·Δt` | G Eq.2:316 p.145; R&T Eq.A-7 p.761 | MATCH | 유지. |
| Log-linear 적용 조건 | descending only; Ci=0 또는 Ci+1=Ci이면 linear fallback | G p.144 §2.8.3 | MATCH | 유지. |
| “혼합 적용 = 실무 표준” | ascending/equal linear, descending log-linear | G p.146 Fig 2.118: “One could also use a mixture...” | RESTORED | 방법 자체는 MATCH. “실무 표준”은 원문보다 강하므로 “사용 가능/흔히 사용” 수준으로 완화. |
| `AUC_tlast-∞ = C_last/λz` | 외삽 AUC | G Eq.2:311, 2:319 | MATCH | 유지. |
| Predicted vs observed Clast | `C_hat_last` 권고 | G p.147 Fig 2.120: predicted rather than observed last concentration recommended | MATCH | 유지. 단, “항상”보다는 “general recommendation”으로 표현. |
| `% extrapolated = AUC_tlast-∞/AUC_total × 100` | 외삽 비율 | G Eq.2:324 p.148 | MATCH | 유지. |
| 20-25% threshold | AUCtlast-∞ should generally not exceed 20-25% unless preliminary | G p.148 | MATCH | 유지. |
| λz 최소 관측점 | “최소 3-4개 관측점” | G p.146 §2.8.4 | MATCH | 유지. |
| λz 이상적 반감기 범위 | Draft: “이상적으로 2-4 반감기” | G p.146: “Ideally ... 3-4 half-lives would need to have elapsed” | ERROR | `2-4 half-lives` → `3-4 half-lives`. MUST_FIX. |
| 마지막 관측치 회귀 제외 | “마지막 관측치가 회귀선 아래로 떨어지면 회귀 제외” | G p.147 Fig 2.120: observed terminal concentration deviates; last observation not included | RESTORED | 방향이 “아래”에 한정되지 않음. “deviates from regression line”으로 수정. |
| LOQ 미만 처리 | missing으로 처리, zero/LOQ 치환 금지 | G p.153 §2.8.6 | MATCH | 유지. |
| AUMC linear trapezoid | `Σ((tiCi + ti+1Ci+1)/2)Δt` | G Eq.2:312 p.144 | MATCH | 유지. |
| AUMC extrapolation | `tlast·Clast/λz + Clast/λz²` | G Eq.2:313, 2:320; R&T Eq.H-9 | MATCH | 유지. |
| AUMC 외삽 30–60% | “AUMC 외삽이 전체의 30-60%” | G p.148/R&T H p.791-792는 AUMC tail이 더 중요함을 말하지만 일반 30-60% rule 없음. R&T Table H-1 예시는 4.9/177 ≈ 2.8% | NOT_IN_SOURCE | 숫자 삭제. “AUMC 외삽은 AUC 외삽보다 tail에 더 민감”으로 완화. MUST_FIX. |
| R&T H-1 molecules | 1 mg, MW 300 g/mol ≈ 2×10^18 molecules | R&T App H p.789 | MATCH | 유지. |
| MRT molecular definition | `MRT = Σtj/N` | R&T Eq.H-1 | MATCH | 유지. |
| MRT plasma definition | `MRT = AUMC/AUC` | R&T Eq.H-8; G Eq.2:328 family | MATCH | 유지. |
| MRT_ivinf | `AUMC/AUC - Tinf/2` | G Eq.2:328; R&T Table H-2 | MATCH | 유지. |
| MRT_oral | `AUMC/AUC - 1/Ka` | G Eq.2:329; R&T Table H-2 | MATCH | 유지. |
| MIT = Tinf/2 | mean input time for constant-rate infusion | G p.149; R&T Table H-2 | MATCH | 유지. |
| MAT/Ka caveat | Ka may contain parallel processes such as degradation; MAT sum | G Eq.2:330 p.150 | OMITTED_IN_DRAFT | 필요 시 C2 context로 1문장 추가. SHOULD_FIX if oral absorption context retained. |
| `MDRT(i)=MBRT(i)-MIT` | 대사체/ith compartment residence time 일반화 | G Eq.2:362 p.156 | MATCH | 유지. |
| CL from NCA | `CL = D_iv/AUC_0∞` | G Eq.2:325 p.149 | MATCH | 유지. |
| Oral clearance | `CL_o = CL/F = D_po/AUC_0∞` | G Eq.2:326 p.149 | MATCH | 유지. |
| Bioavailability F | `F=(AUCpo/AUCiv)(Div/Dpo)` | G Eq.2:327 p.149 | MATCH | 유지. |
| Vss standard | `Vss = MRT·CL = D·AUMC/AUC²` | G Eq.2:337 p.151 | MATCH | 유지. |
| Vz | `Vz = CL/λz = D/(AUC·λz)` | G Eq.2:338 p.151 | MATCH | 유지. |
| Vz ≥ Vss always | “다구획 모델에서 Vz ≥ Vss 항상” | 지정 PDF에는 해당 부등식 명시 없음 | NOT_IN_SOURCE | `[일반 PK sanity check]`로 분리하거나 삭제. PDF-anchored fact로 두지 말 것. |
| t1/2z, t1/2α, t1/2β | `ln(2)/λz`, `ln(2)/α`, `ln(2)/β` | G Eq.2:340-342 | MATCH where present | Draft의 self-test/맥락에 들어간 경우 유지 가능. |
| Effective half-life | `ln(2)·MRT` | G p.151: effective half-life is ln(2)·MRT | MATCH | 유지. |
| Steady-state AUC equivalence | `AUC0-τ,ss = AUC0-∞` single-dose | G p.152 Fig 2.122 | MATCH | 유지. |
| Unequal dosing interval equations | Eq.2:350-2:353 | Draft에서는 거의 생략 | OMITTED_JUSTIFIABLE | 세션 핵심에는 낮은 우선순위. 필요 시 context note. |
| Short half-life/input alternative | `Vss = K0·AUC_t*∞/Css²`; `MRT = AUC_t*∞/Css` | G Eq.2:366-2:367 p.157 | MATCH | 유지. |
| “수학적으로 음수가 불가능” | Eq.2:366 does not result in zero or negative Vss | G p.157 | MATCH | 유지. |
| Specific scenario `t1/2≈0.5h`, `Vss=-0.4 L/kg` | Draft Q3/C3 가상 사례 | 지정 PDF에는 해당 수치 없음 | NOT_IN_SOURCE | `[교육용 가상 시나리오]` 표시. 본문 사실처럼 쓰면 안 됨. |
| PK41 doses | 310, 520, 780 µg/kg over 5 h, one volunteer, BW 70 kg | G p.661 | MISSING_IN_MAIN | Draft Q4/§8에 전략은 있으나 수치 anchor가 카드에서 배제됨. SHOULD_FIX/HIGH. |
| PK41 NCA results | CL 1.6→0.9 L·h⁻¹·kg⁻¹, V 2.3→1.8 L/kg, MRT 1.4→1.9h | G p.662 | MISSING_IN_MAIN | Curation Map에서 “§2 카드 침투 금지”로 밀어냄. Dynamic source anchor로 4-6줄 삽입 권장. MUST_FIX if Scope Lock required it. |
| PK41 initial estimates | V≈2 L/kg, CL 1.6 & 0.94, Cpeak 44 & 180, Km≈150, Vmax≈310, selected 200/100 | G p.663-664 | PARTIAL | Q4는 전략만 있고 수치 anchor는 없음. SHOULD_FIX. |
| PK41 final estimates | Vmax=184, Km=83, V=1.8 | G p.664 | MISSING_IN_MAIN | Curation Map에서 reject. 최소 anchor box에 넣을 것. SHOULD_FIX. |
| CL and t1/2 incompatible with mixed zero-/first-order kinetics | Draft nonlinear 전환 논리 | G p.664 explicitly states this | MATCH | 유지. |
| R&T Table A-1 “zileuton” | Draft: “R&T Table A-1 zileuton” | R&T Table A-1 p.759 = generic oral 50 mg example, total AUC 26.60. Zileuton is Table A-2 p.762 | ERROR | `Table A-1: oral 50 mg generic AUC example`; `Table A-2: zileuton 600 mg PO`로 분리. MUST_FIX. |
| R&T A-1 AUC | total AUC 26.60 mg·hr/L | R&T Table A-1 p.759-760 | MATCH if used generically | 유지. |
| R&T A-2 Zileuton | 600 mg oral dose, time 0-24h, concentration values | R&T Table A-2 p.762 | OMITTED_OR_MISNAMED | 혼동쌍 예시에 쓰려면 Table A-2로 명시. |
| R&T IV bolus special case | `AUC=C(0)/k`; e.g., C(0)=200 mg/L, k=0.1 hr⁻¹ → 2000 mg·hr/L | R&T p.760-761 Eq.A-1-A-3 | OMITTED_JUSTIFIABLE | C1의 보강 예시로는 유용하나 필수는 아님. |
| R&T log trapezoid discrepancy > twofold | consecutive observations differ by more than twofold | R&T p.761 | OMITTED_JUSTIFIABLE | C1 실무 caveat로 optional. |
| R&T H-1 values | AUC=44.2, AUMC=177, AUC tail=0.17, AUMC tail=4.9, MRT 4.25/4.0/4.3 | R&T p.792 | MATCH | Draft의 177은 source-consistent; OCR상 17.7로 보일 수 있으나 MRT=177/44.2≈4.0로 해석해야 함. |
| ICH S3A·E1·M3 | Draft source tag | G p.158 mentions ICH S3A and 7A only | ERROR/NOT_IN_SOURCE | PDF 기반 본문에서는 `ICH S3A and 7A`로 제한. E1/M3는 외부 연결로 분리. |
| FDA 21 CFR 320 / BA-BE standard | Draft 후속 지식 | 지정 PDF 없음 | NOT_IN_SOURCE | 본문에서 제거하거나 `[후속 규제 연결: 외부 근거 필요]`. |
| `C_u = C_total·f_u` | free concentration relation | G Fig 2.134 discusses unbound concentration and protein binding but formula not printed | RESTORED | 수식은 일반적 정의. PDF 직접 수식처럼 표시하지 말고 `[정의 보충]`으로 처리. |
| Cmax/AUC/td/Css exposure metrics | Table in C4 | G p.163 Fig 2.135 | MATCH | 유지. |
| `Css = D/(τ·CL)` | C4 layer | G §2.8.6 has CL from dose/AUC over interval; exact expression as written not in §2.9 | RESTORED | 일반식으로 맞으나 PDF 직접 인용처럼 두지 말 것. |
| NONMEM/Phoenix/PKNCA specifics | Draft L5/Professional Moat | 지정 PDF에는 software package generic warning만 있음; NONMEM/Phoenix/PKNCA는 없음 | NOT_IN_SOURCE | `[실무 확장]` 태그 필수. |
| FOCE/local optimum/covariance/η-shrinkage | Draft §8 failure modes | 지정 PDF 없음 | NOT_IN_SOURCE | 교재 사실처럼 보이면 안 됨. `[교육용 가상 시나리오]` 또는 삭제. |
| Clinical Hold/Deficiency Letter/Information Request | Draft C3/Q3/Q9/§8 | 지정 PDF 없음 | NOT_IN_SOURCE | MUST_FIX: source-anchored body에서 제거 또는 명확히 tag. |

---

## T2: Examples & Data Audit

| Item | Draft v0 Status | PDF Location | Classification | Importance | Action |
|---|---|---|---|---|---|
| NCA vs nonlinear regression schematic | C1/Curation Map에서 반영 | G Fig 2.113 p.141 | INCLUDED_CORRECT | HIGH | 유지. |
| Linear trapezoid graphical example | C1 반영 | G Fig 2.114 p.142 | INCLUDED_CORRECT | HIGH | 유지. |
| Under/overestimation during infusion | C1 반영 | G Fig 2.115 p.142 | INCLUDED_CORRECT | HIGH | 유지. |
| λz terminal slope estimation | C1 반영 | G Fig 2.116 p.143 | INCLUDED_CORRECT | HIGH | 3-4 half-lives 오류만 수정. |
| Linear vs log-linear trapezoid comparison | C1 반영 | G Fig 2.117 p.144 | INCLUDED_CORRECT | HIGH | 유지. |
| Mixed linear/log-linear rule | C1 반영 | G Fig 2.118 p.146 | INCLUDED_CORRECT | MEDIUM | “실무 표준” 표현 완화. |
| Ideal vs common λz situation | C1 일부 반영 | G Fig 2.119 p.147 | INCLUDED_CORRECT | MEDIUM | 시각 지시 권장. |
| Observed vs predicted terminal concentration | C1 반영 | G Fig 2.120 p.147 | INCLUDED_CORRECT | HIGH | 유지. |
| AUC vs AUMC curve shape | C2 반영 | G Fig 2.121 p.148 | INCLUDED_CORRECT | HIGH | 유지. |
| Holford message: AUC as exposure but CL/CL/F physiologically preferred | 거의 미반영 | G p.148-149 | MISSING | MEDIUM | C1 또는 C3에 1문장 추가 권장. |
| Steady-state residual area equivalence | C1 context 반영 | G Fig 2.122 p.152 | INCLUDED_CORRECT | MEDIUM | 유지. |
| Incomplete sampling within dosing interval; LOQ handling | LOQ는 반영, Fig 2.123은 미반영 | G Fig 2.123 p.153 | PARTIAL | MEDIUM | LOQ caveat 유지. Figure view는 optional. |
| Unequal dosing intervals 10/14h | 미반영 | G Fig 2.124 p.154 | MISSING | LOW | 생략 가능. 실무형 supplement에는 optional. |
| Metabolite kinetics schematic | C2 context 반영 | G Fig 2.125 p.156; Eq.2:354-2:362 | INCLUDED_CORRECT | MEDIUM | 유지. |
| Short half-life vs input alternative | C3 핵심 반영 | G §2.8.8, Fig 2.126 p.157 | INCLUDED_CORRECT | HIGH | 유지. |
| Exposure route/F example | C4 context 반영 | G Fig 2.127 p.158-159 | INCLUDED_CORRECT | HIGH | 유지. |
| Nonlinear elimination and safety margin | C4 context 반영 | G Fig 2.128 p.159 | INCLUDED_CORRECT | HIGH | 유지. |
| Active metabolite example | C4 context 반영 | G Fig 2.129 p.160 | INCLUDED_CORRECT | HIGH | 유지. |
| Mode of administration: salicylic acid/osmotic minipump vs IV injection | C4 context 반영 | G Fig 2.130 p.160 | INCLUDED_CORRECT | HIGH | 유지. |
| Occupancy/biomarker/system behavior | C4 context 반영 | G Fig 2.131 p.161 | INCLUDED_CORRECT | MEDIUM | 수치 range 표현을 원문과 맞춰 재확인. |
| Repeated feeding safety study in rats | Draft C4 사례 목록에서 누락 | G Fig 2.132 p.162 | MISSING | MEDIUM | §2.9 사례를 “6가지”로 압축할 때 누락됨. 1문장 context 추가 권장. |
| U-shaped concentration-response | C4 context 반영 | G Fig 2.133 p.162 | INCLUDED_CORRECT | HIGH | 유지. |
| Protein binding / unbound concentration reverses potency order | C4 context 반영 | G Fig 2.134 p.163 | INCLUDED_CORRECT | HIGH | 유지. |
| Exposure metrics schematic | C4 반영 | G Fig 2.135 p.163 | INCLUDED_CORRECT | HIGH | 유지. |
| PK41 objectives/problem specification | §8와 Q4에 간접 반영 | G p.661 | PARTIAL | HIGH | Source anchor box로 직접 추가. |
| PK41 one volunteer, 5h infusion, 310/520/780 µg/kg, BW 70kg | Curation Map에서 배제 | G p.661 | MISSING | HIGH | MUST_FIX: 카드나 §8에 4-6줄 anchor. |
| PK41 Table 41.1 dose-time-concentration data | Curation Map에서 배제 | G Table 41.1 p.662 | MISSING | MEDIUM | 전체 표 재현은 불필요. 핵심 design만 언급. |
| PK41 Figure 41.1 concentration-time observed/predicted | 미반영 | G Fig 41.1 p.662 | MISSING | MEDIUM | Figure view instruction 권장. |
| PK41 Figure 41.2 CL vs dose | §8에서 dose-dependent CL 언급 | G Fig 41.2 p.663 | PARTIAL | HIGH | 수치와 함께 명시. |
| PK41 NCA results | Curation Map에서 reject | G p.662 | MISSING | HIGH | CL/V/MRT dose-dependence는 반드시 anchor. |
| PK41 equations 41:1-41:4 and final estimates | Q4 전략만 반영 | G p.663-664 | PARTIAL | HIGH | Vmax/Km/V initial/final 수치 보강. |
| R&T Table A-1 generic AUC example | mislabeled as zileuton | T App A p.759 | INCLUDED_ERROR | HIGH | Table A-1 명칭 수정. |
| R&T Figure A-1 trapezoid illustration | C1 indirectly | T p.760 | INCLUDED_CORRECT | MEDIUM | 필요 시 view instruction. |
| R&T IV bolus special case AUC=C0/k | 거의 미반영 | T p.760-761 | MISSING | LOW | optional. |
| R&T log trapezoid derivation A-4-A-7 | C1 formula 반영 | T p.761 | INCLUDED_CORRECT | MEDIUM | 유지. |
| R&T Table A-2 Zileuton 600mg | mislabeled/misplaced | T p.762 | INCLUDED_ERROR | MEDIUM | Table A-2로 분리. |
| R&T MRT molecular definition | C2 핵심 반영 | T App H p.789 | INCLUDED_CORRECT | HIGH | 유지. |
| R&T urinary MRT Eq H-7 + Fig H-1 | Draft 거의 미반영 | T p.790 | MISSING | MEDIUM | MRT를 plasma-only로 보이지 않게 1문장 추가 권장. |
| R&T plasma MRT H-8/H-10 + Fig H-2 | C2 반영 | T p.791 | INCLUDED_CORRECT | HIGH | 유지. |
| R&T Table H-1 numerical MRT example | §5/Q5 반영 | T p.792 | INCLUDED_CORRECT | HIGH | 유지. |
| R&T Table H-2 input mode MIT | C2 반영 | T p.793 | INCLUDED_CORRECT | HIGH | 유지. |
| Patch Memo item: PK41 anchor too weak | Draft와 PDF 대조 시 타당 | S06 memo; G p.661-664 | MATCH | HIGH | 채택. |
| Patch Memo item: R&T Table A-1 zileuton error | 타당 | T p.759, p.762 | MATCH | HIGH | 채택. |
| Patch Memo item: AUMC 30-60% source issue | 타당 | G/R&T source lacks general 30-60% | MATCH | HIGH | 채택. |
| Patch Memo item: regulatory 표현 과강 | 타당 | 지정 PDF source 없음 | MATCH | HIGH | 채택. |
| Patch Memo item: BA/BE 규제 프레임 source 외부 | 타당 | 지정 PDF source 없음 | MATCH | MEDIUM | 채택. |
| Patch Memo item: §7 길이 | Source fidelity issue는 아님 | Draft structure | OPTIONAL | LOW | HTML 단계 편집 판단. |

---

## T3: Author Key Messages

| Message | PDF Location | In Draft v0? | Status |
|---|---|---|---|
| NCA and nonlinear regression are complementary; strengths of one are weaknesses of the other. | G §2.8.1 p.141 | Partly | SHOULD_FIX: Curation Map의 “NCA vs regression”에 보강 가능. |
| NCA does not require a specific compartmental model, but assumes linear elimination from the sampling compartment. | G §2.8.1 p.141 | Yes | MATCH. |
| NCA deals with sums of areas; regression modeling uses a function with regression parameters. | G Fig 2.113/p.141 | Yes | MATCH. |
| AUC is zero moment; AUMC is first moment; higher moments are generally not used due unacceptable computational error. | G p.142 | Yes | MATCH. |
| Linear trapezoidal error depends on trapezoid width and true profile curvature; it overestimates descending and underestimates ascending. | G p.142/Fig 2.115 | Yes | MATCH. |
| Log-linear trapezoid applies only to descending data and fails when Ci=0 or Ci+1=Ci. | G §2.8.3 p.144 | Yes | MATCH. |
| With reasonable sampling design, differences between linear/log-linear methods are rarely clinically important; method choice is modeler discretion. | G p.146 | Weakly | SHOULD_FIX: Draft emphasizes method mechanics but not this author-balancing message. |
| λz should be estimated from individual semi-log plots; ideally 3-4 half-lives, minimum 3-4 observations. | G §2.8.4 p.146 | Partly | ERROR: Draft says 2-4 half-lives. |
| Predicted terminal concentration is generally recommended over observed last concentration for extrapolated area when observed deviates. | G p.147/Fig 2.120 | Yes | MATCH. |
| AUC extrapolated area should generally not exceed 20-25% of total unless preliminary. | G p.148 | Yes | MATCH. |
| AUMC tail is generally much larger relative to AUC tail; first moment emphasizes late time. | G Fig 2.121 p.148; R&T Fig H-2 p.791 | Yes | MATCH, but numeric 30-60% is NOT_IN_SOURCE. |
| Holford: CL or CL/F is more physiologically interpretable than AUC; AUC still useful as exposure/toxicology or when dose unknown. | G p.148-149 | Mostly absent | SHOULD_FIX: Important author message. |
| Steady-state AUC within a dosing interval equals single-dose AUC0-∞ because residual areas are equal. | G p.152/Fig 2.122 | Yes | MATCH. |
| Values below LOQ should be treated as missing rather than set to LOQ, zero, or something else. | G p.153 | Yes | MATCH. |
| If K or λz is not well established for unequal dosing intervals, regression modeling may be necessary. | G p.154 | No | OPTIONAL: out of main scope unless steady-state NCA emphasized. |
| Metabolite NCA uses MDRT/MBRT/MIT relationships; upstream residence time is input time. | G §2.8.7 p.155-156 | Yes | MATCH as context. |
| When half-life is short relative to input time, Eq.2:366/2:367 is more robust and avoids zero/negative Vss. | G §2.8.8 p.157 | Yes | MATCH. |
| Most software packages may fail to estimate MRT/Vss accurately for relevant short half-life/input datasets if they use standard equations. | G p.158, Case PK48 note | Partly | MATCH conceptually; do not over-name Phoenix/WinNonMEM unless source-supported. |
| Exposure means not primarily administered dose but total/unbound systemic plasma concentration, sometimes tissue concentration. | G §2.9.1 p.158 | Yes | MATCH. |
| Six real-life cases show systemic concentration is useful for potency, safety margin, efficacy, or active metabolite screening. | G §2.9.2 p.158-163 | Mostly | SHOULD_FIX: repeated-feeding safety example Fig 2.132 missing. |
| Exposure metrics include Cmax, AUC, duration above threshold td; F and t1/2 aid interpretation. | G §2.9.3 p.163 | Yes | MATCH. |
| PK41: fitting several doses allows estimation of highly correlated Vmax/Km with good precision using limited samples. | G p.661, p.664 | Partly | SHOULD_FIX: strategy included but concrete source anchor weak. |
| PK41: in capacity-limited one-compartment system model parameters are Vmax, Km, V rather than CL and V; CL and t1/2 are incompatible with mixed zero-/first-order kinetics. | G p.664 | Yes/partly | MATCH but should be tied directly to PK41 source. |
| R&T Appendix A: trapezoidal AUC is simple numeric table extension; total AUC usually zero to infinity. | T p.759-760 | Partly | OPTIONAL. |
| R&T Appendix H: MRT is average time molecules reside in the body; input route adds mean input time. | T p.789-793 | Yes | MATCH. |

---

## T4: Priority Summary

| # | Item | Priority | Rationale |
|---|---|---|---|
| 1 | `R&T Table A-1 zileuton` | MUST_FIX | 명시 오류. Table A-1은 generic oral 50 mg AUC=26.60 예제, zileuton은 Table A-2. |
| 2 | `λz 30-50% distortion` | MUST_FIX | 지정 PDF에 없는 수치. 교육용 가상 시나리오 태그 없이는 source fidelity 위반. |
| 3 | `AUMC 외삽 30-60%` | MUST_FIX | 일반 rule로 PDF에 없음. R&T Table H-1 예시는 2.8% 수준. |
| 4 | `2-4 half-lives` | MUST_FIX | 원문은 ideally 3-4 half-lives. |
| 5 | FDA/BA-BE/Clinical Hold/Deficiency/IR/FOCE/η-shrinkage 시나리오 | MUST_FIX | 실무적으로 유용하더라도 지정 PDF 밖. `[실무 추론]` 또는 `[교육용 가상 시나리오]` 분리 필수. |
| 6 | PK41 concrete data anchor 배제 | MUST_FIX | PDF source의 핵심 worked case이며 Draft가 “§6 전용”으로 밀었으나 현재 산출물에 §6이 없음. 최소 anchor box 필요. |
| 7 | ICH S3A·E1·M3 | MUST_FIX | PDF는 ICH S3A and 7A를 언급. E1/M3는 외부 지식. |
| 8 | `V_z ≥ Vss always` | SHOULD_FIX | 일반 PK sanity check로는 유용하지만 지정 PDF에 명시 없음. Source fact처럼 두지 말 것. |
| 9 | Repeated feeding safety study Fig 2.132 누락 | SHOULD_FIX | §2.9 exposure cases 중 한 사례. C4 압축 목록에 1문장 추가 권장. |
| 10 | Holford AUC vs CL message 누락 | SHOULD_FIX | 저자의 명시적 관점. NCA를 exposure vs parameter로 구분하는 데 중요. |
| 11 | Predicted/observed Clast 표현 방향 | SHOULD_FIX | “아래로 떨어지면”이 아니라 “회귀선에서 벗어나면”으로 수정. |
| 12 | Method-choice author message | SHOULD_FIX | log-linear가 무조건 superior처럼 보이지 않게, reasonable design에서는 차이 드문 점 보강. |
| 13 | R&T urinary MRT/Fig H-1 | SHOULD_FIX | MRT가 plasma AUMC/AUC만이 아니라 urinary excretion data에서도 추정 가능하다는 보강. |
| 14 | Unequal dosing intervals Eq.2:350-2:353 | OPTIONAL | 실무적으로 유용하지만 Step 1 core card에는 생략 가능. |
| 15 | R&T IV bolus AUC=C0/k special case | OPTIONAL | C1 예시로 유용하나 Gabrielsson 수식만으로도 충분. |
| 16 | Table A-2 zileuton detailed concentrations | OPTIONAL | mislabel만 고치면 전체 표는 불필요. |
| 17 | §7 question count | OPTIONAL | Source fidelity 이슈가 아니라 HTML/학습 설계 이슈. |
| 18 | PK41 구체 수치를 §2 card에서 완전 배제 | REJECT | “구체 수치 침투 금지”는 현재 산출물 구조상 source anchor를 약화시킴. 최소한 §8 또는 box에 포함해야 함. |
| 19 | PDF 근거 없는 수치 rule을 교재 사실처럼 유지 | REJECT | 30-50%, 30-60%, FDA timelines 등. |

---

## T5: Coverage Audit

### T5-A. Section Headings

| PDF Element | Type | PDF Location | Step 1 Status | Omission Verdict | Required Action |
|---|---|---|---|---|---|
| Ethanol nonlinear first-pass carryover paragraph | Context bridge | G p.141 before §2.8 | OMITTED_JUSTIFIABLE | None | §2.7 prior context. |
| 2.8 Non-Compartmental Analysis | H1 | G p.141 | INCLUDED_AS_MUST | None | 유지. |
| 2.8.1 Non-compartmental versus regression analysis | H2 | G p.141 | INCLUDED_AS_MUST | None | 유지. |
| 2.8.2 Computational methods - Linear trapezoidal rule | H2 | G p.142 | INCLUDED_AS_MUST | None | 유지. |
| 2.8.3 Computational methods - Log-linear trapezoidal rule | H2 | G p.144 | INCLUDED_AS_MUST | None | 유지. |
| 2.8.4 Strategies for estimation of λz | H2 | G p.146 | INCLUDED_AS_MUST | None | 3-4 half-lives correction. |
| 2.8.5 Pertinent pharmacokinetic estimates | H2 | G p.148 | INCLUDED_AS_MUST | None | Holford message add. |
| 2.8.6 Issues related to steady state | H2 | G p.152 | INCLUDED_AS_CONTEXT | None | 유지. |
| 2.8.7 Metabolite kinetics | H2 | G p.155 | INCLUDED_AS_CONTEXT | None | 유지. |
| 2.8.8 When half-life is short relative to input time | H2 | G p.157 | INCLUDED_AS_MUST | None | 유지. |
| 2.9 How to Assess Exposure | H1 | G p.158 | INCLUDED_AS_MUST | None | 유지. |
| 2.9.1 What do we mean by exposure? | H2 | G p.158 | INCLUDED_AS_MUST | None | 유지. |
| 2.9.2 The case(s) for abandoning dose | H2 | G p.158 | INCLUDED_AS_MUST | MISSING_EXAMPLE partial | Fig 2.132 추가. |
| 2.9.3 Exposure based on total concentrations | H2 | G p.163 | INCLUDED_AS_MUST | None | 유지. |
| PK41 - Multiple intravenous infusions - NCA versus regression | Case Study | G p.661-664 | INCLUDED_AS_CONTEXT only | OMITTED_PROBLEMATIC: MISSING_EXAMPLE | 핵심 수치 anchor 삽입. |
| R&T Appendix A Assessment of AUC | Appendix heading | T p.759-762 | INCLUDED_AS_CONTEXT | None | Table A-1 오류 수정. |
| R&T Special Case: An Intravenous Bolus | Subheading | T p.760 | OMITTED_JUSTIFIABLE | None | Optional. |
| R&T When Decline Is Logarithmic | Subheading | T p.761 | INCLUDED_AS_CONTEXT | None | 유지. |
| R&T Study Problems App A | Exercises | T p.761-762 | OMITTED_JUSTIFIABLE | None | 생략. |
| R&T Appendix H Mean Residence Time | Appendix heading | T p.789-793 | INCLUDED_AS_MUST | None | 유지. |
| R&T Excretion Data | Subheading | T p.790 | OMITTED_PROBLEMATIC: MISSING_BRIDGE | SHOULD_FIX | urinary MRT도 가능하다는 1문장 추가. |
| R&T Plasma Concentration Data | Subheading | T p.791 | INCLUDED_AS_MUST | None | 유지. |
| R&T Study Problems App H | Exercises | T p.793 | OMITTED_JUSTIFIABLE | None | 생략. |

### T5-B. Numbered Equations / Formulas

| PDF Element | Type | PDF Location | Step 1 Status | Omission Verdict | Required Action |
|---|---|---|---|---|---|
| Eq.2:310 | Linear AUC trapezoid | G p.143 | INCLUDED_AS_MUST | None | 유지. |
| Eq.2:311 | AUC extrapolation from tlast to infinity | G p.143 | INCLUDED_AS_MUST | None | 유지. |
| Eq.2:312 | Linear AUMC trapezoid | G p.144 | INCLUDED_AS_MUST | None | 유지. |
| Eq.2:313 | AUMC extrapolation | G p.144 | INCLUDED_AS_MUST | None | 유지. |
| Eq.2:314 | Exponential decline between two observations | G p.144 | INCLUDED_AS_MUST | None | 유지. |
| Eq.2:315 | K from log ratio | G p.145 | INCLUDED_AS_MUST | None | 유지. |
| Eq.2:316 | Log-linear AUC interval | G p.145 | INCLUDED_AS_MUST | None | 유지. |
| Eq.2:317 | Log-linear AUC sum | G p.145 | INCLUDED_AS_MUST | None | 유지. |
| Eq.2:318 | Log-linear AUMC sum | G p.145 | OMITTED_JUSTIFIABLE | MISSING_BRIDGE low | C1/C2에서 optional. |
| Eq.2:319 | Log-linear AUC extrapolation | G p.145 | INCLUDED_AS_MUST | None | 유지. |
| Eq.2:320 | Log-linear AUMC extrapolation | G p.145 | INCLUDED_AS_MUST equivalent | None | 유지. |
| Eq.2:321 | AUC extrapolated using observed Clast | G p.147 | INCLUDED_AS_CONTEXT | None | 유지. |
| Eq.2:322 | AUC extrapolated using predicted Clast | G p.147 | INCLUDED_AS_CONTEXT | None | 유지. |
| Eq.2:323 | Total AUC | G p.147 | INCLUDED_AS_MUST | None | 유지. |
| Eq.2:324 | Fraction extrapolated AUC | G p.148 | INCLUDED_AS_MUST | None | 유지. |
| Eq.2:325 | CL = Div/AUC | G p.149 | INCLUDED_AS_MUST | None | 유지. |
| Eq.2:326 | Clo = Dpo/AUC | G p.149 | INCLUDED_AS_MUST | None | 유지. |
| Eq.2:327 | F from dose-normalized AUC ratio | G p.149 | INCLUDED_AS_MUST | None | 유지. |
| Eq.2:328 | MRT correction for infusion | G p.149 | INCLUDED_AS_MUST | None | 유지. |
| Eq.2:329 | MRT correction for first-order input | G p.149 | INCLUDED_AS_MUST | None | 유지. |
| Eq.2:330 | MAT and apparent Ka caveat | G p.150 | OMITTED_PROBLEMATIC: MISSING_BRIDGE | SHOULD_FIX if oral context retained | Ka includes parallel processes. |
| Eq.2:331 | MRT(1) for central compartment | G p.150 | OMITTED_JUSTIFIABLE | None | Advanced mammillary model, out of card scope. |
| Eq.2:332 | MRTiv with k21 | G p.150 | OMITTED_JUSTIFIABLE | None | Advanced. |
| Eq.2:333 | Observed MRT after extravascular dosing = MRT + MIT | G p.150 | INCLUDED_AS_MUST equivalent | None | 유지. |
| Eq.2:334-2:336 | MIT from input function | G p.150-151 | INCLUDED_AS_CONTEXT partial | MISSING_BRIDGE low | Optional. |
| Eq.2:337 | Vss = MRT·CL | G p.151 | INCLUDED_AS_MUST | None | 유지. |
| Eq.2:338 | Vz = CL/λz | G p.151 | INCLUDED_AS_MUST | None | 유지. |
| Eq.2:339 | Bi-exponential corresponding volume | G p.151 | OMITTED_JUSTIFIABLE | None | Out of main scope. |
| Eq.2:340-2:342 | Terminal/initial/beta half-lives | G p.151 | INCLUDED_AS_CONTEXT partial | None | 유지 가능. |
| Eq.2:343 | CL at steady state from dose/AUC0-τ | G p.152 | INCLUDED_AS_CONTEXT | None | 유지. |
| Eq.2:344 | Oral clearance at steady state | G p.152 | OMITTED_JUSTIFIABLE | None | Optional. |
| Eq.2:345-2:349 | Incomplete interval extrapolation to 24h | G p.152-153 | OMITTED_JUSTIFIABLE | None | Optional; LOQ caveat retained. |
| Eq.2:350-2:353 | Unequal dosing interval and Vss steady-state calculation | G p.154-155 | OMITTED_JUSTIFIABLE | None | Optional. |
| Eq.2:354-2:362 | Metabolite MDRT/MBRT/MIT and for | G p.155-156 | INCLUDED_AS_CONTEXT | None | 유지. |
| Eq.2:363 | Ass=Vss·Css | G p.157 | INCLUDED_AS_MUST | None | 유지. |
| Eq.2:364 | Ass=CL·AUCt*∞ | G p.157 | INCLUDED_AS_MUST | None | 유지. |
| Eq.2:365 | CL=K0/Css | G p.157 | INCLUDED_AS_MUST | None | 유지. |
| Eq.2:366 | Vss alternative | G p.157 | INCLUDED_AS_MUST | None | 유지. |
| Eq.2:367 | MRT alternative | G p.157 | INCLUDED_AS_MUST | None | 유지. |
| Eq.2:368 | CL from known Ass and washout AUC | G p.157 | OMITTED_JUSTIFIABLE | None | Optional. |
| Eq.41:1 | `V·dC/dt = In - Cl·C` | G p.663 | INCLUDED_AS_CONTEXT only | MISSING_EXAMPLE | PK41 anchor에서 추가. |
| Eq.41:2 | `Cl=Vmax/(Km+C)` | G p.663 | INCLUDED_AS_CONTEXT | None | Q4에 수식 추가 가능. |
| Eq.41:3 | `1.6=Vmax/(Km+44)` | G p.663 | PARTIAL | MISSING_EXAMPLE | PK41 anchor에 추가. |
| Eq.41:4 | `0.94=Vmax/(Km+180)` | G p.664 | PARTIAL | MISSING_EXAMPLE | PK41 anchor에 추가. |
| R&T Eq.A-1-A-3 | IV bolus AUC = C(0)/k | T p.760-761 | OMITTED_JUSTIFIABLE | None | Optional. |
| R&T Eq.A-4-A-7 | Log trapezoid derivation | T p.761 | INCLUDED_AS_CONTEXT | None | 유지. |
| R&T Eq.H-1-H-6 | Molecular/amount-based MRT derivation | T p.789-790 | INCLUDED_AS_MUST partial | None | 유지. |
| R&T Eq.H-7 | Urinary MRT | T p.790 | OMITTED_PROBLEMATIC: MISSING_BRIDGE | SHOULD_FIX | 1문장 추가. |
| R&T Eq.H-8 | Plasma MRT = AUMC/AUC | T p.791 | INCLUDED_AS_MUST | None | 유지. |
| R&T Eq.H-9 | AUMC extrapolation after last point | T p.791 | INCLUDED_AS_MUST | None | 유지. |
| R&T Eq.H-10 | Exponential sum AUMC | T p.791 | OMITTED_JUSTIFIABLE | None | Advanced. |

### T5-C. Figures, Tables, Worked Examples, Repeated Messages

| PDF Element | Type | PDF Location | Step 1 Status | Omission Verdict | Required Action |
|---|---|---|---|---|---|
| Figs 2.113-2.118 | Figures | G p.141-146 | INCLUDED_AS_MUST | None | 유지. |
| Figs 2.119-2.120 | Figures | G p.147 | INCLUDED_AS_MUST | None | λz half-life correction. |
| Fig 2.121 | Figure | G p.148 | INCLUDED_AS_MUST | None | 유지. |
| Figs 2.122-2.124 | Figures | G p.152-154 | INCLUDED_AS_CONTEXT/OMITTED | Justified except LOQ/steady-state | 유지. |
| Fig 2.125 | Figure | G p.156 | INCLUDED_AS_CONTEXT | None | 유지. |
| Fig 2.126 | Figure | G p.157 | INCLUDED_AS_MUST | None | 유지. |
| Figs 2.127-2.135 | Figures | G p.159-163 | INCLUDED_AS_MUST/PARTIAL | MISSING_EXAMPLE for Fig 2.132 | Add repeated feeding rat safety example. |
| Case Study PK41 | Worked case | G p.661-664 | PARTIAL | MISSING_EXAMPLE HIGH | Add data anchor box. |
| R&T Table A-1/Fig A-1 | Worked AUC example | T p.759-760 | PARTIAL_ERROR | MISSING_EXAMPLE label error | Correct table label. |
| R&T Table A-2 | Study problem dataset | T p.762 | INCLUDED_ERROR as Table A-1 | MISSING_EXAMPLE low | Correct label if retained. |
| R&T Fig H-1 | Figure | T p.790 | OMITTED_PROBLEMATIC | MISSING_BRIDGE | Add urinary MRT note. |
| R&T Fig H-2/Table H-1 | Figure/Table | T p.791-792 | INCLUDED_AS_MUST | None | 유지. |
| R&T Table H-2 | Table | T p.793 | INCLUDED_AS_MUST | None | 유지. |
| Repeated message: NCA assumes linear elimination | Author repeated theme | G p.141, p.143-148, p.664 | INCLUDED_AS_MUST | None | 유지. |
| Repeated message: AUC/AUMC tail/extrapolation quality controls downstream parameters | Author repeated theme | G p.143-148, R&T H | INCLUDED_AS_MUST | None | Numeric overreach fix. |
| Repeated message: concentration/exposure can outperform dose | Author repeated theme | G §2.9.1-2.9.3 | INCLUDED_AS_MUST | None | Fig 2.132 add. |
| Chapter summary/box summary | Closing/summary | No explicit chapter summary in extracted page range | N/A | None | No action. |

---

## T6: Figure Inventory & Learning Value Audit

**Inspection protocol note:** PDF pages were rendered to images and inspected visually. The `Inspection Method` is therefore `VISUAL_INSPECTED` unless otherwise stated.

| Figure/Table | Page | Teaches | Value | View Instruction? | Redraw/New Schematic? | Inspection Method | Rationale |
|---|---:|---|---|---|---|---|---|
| Fig 2.113 | G p.141 | NCA sums areas whereas regression fits a function with parameters. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Session framing depends on this contrast; a cleaner redraw could improve Phase 4C. |
| Fig 2.114 | G p.142 | Linear trapezoidal rule geometry and Δt intervals. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Core AUC computation figure. |
| Fig 2.115 | G p.142 | Linear trapezoid underestimates rising and overestimates falling phases. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Bias direction is easier visually; redraw could isolate ascending/descending. |
| Fig 2.116 | G p.143 | Terminal slope λz estimation on semi-log plot. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | λz selection is central to extrapolation. |
| Fig 2.117 | G p.144 | Linear vs log-linear trapezoid difference during exponential decline. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Best visual anchor for C1. A modern redraw could clarify shaded overestimation. |
| Fig 2.118 | G p.146 | Mixed linear-up/log-down NCA rule. | USEFUL | YES | NO | VISUAL_INSPECTED | Supports practical method choice but text alone is sufficient. |
| Fig 2.119 | G p.147 | Ideal vs common terminal-slope estimation situations. | USEFUL | YES | NO | VISUAL_INSPECTED | Helps audit λz but not structurally indispensable. |
| Fig 2.120 | G p.147 | Observed vs predicted terminal concentration effect on extrapolated AUC. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Critical for Clast_pred vs Clast_obs rule; redraw could show over/under cases clearly. |
| Fig 2.121 | G p.148 | AUC vs AUMC shape and larger first-moment tail. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Essential for MRT intuition. |
| Fig 2.122 | G p.152 | Steady-state AUC0-τ equals single-dose AUC0-∞ via residual-area cancellation. | USEFUL | YES | YES | VISUAL_INSPECTED | Useful for steady-state context; redraw could be clearer. |
| Fig 2.123 | G p.153 | Predicted area to τ and LOQ-excluded observations. | USEFUL | NO | NO | VISUAL_INSPECTED | Supports LOQ and interval extrapolation; not core. |
| Fig 2.124 | G p.154 | Unequal 10/14-hour dosing interval NCA logic. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Specialized steady-state case outside main Step 1 scope. |
| Fig 2.125 | G p.156 | MDRT(i)=MBRT(i)-MBRT(i-1) schematic for metabolite/compartment residence time. | USEFUL | NO | YES | VISUAL_INSPECTED | Context figure; redraw may help but not required. |
| Fig 2.126 | G p.157 | Washout AUC from steady state used for robust Vss/MRT when input time is long. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Apex C3 depends on this visual. |
| Fig 2.127 | G p.159 | Route/bioavailability confounds dose-response; concentration-response superimposes. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Core exposure philosophy figure. |
| Fig 2.128 | G p.159 | Nonlinear elimination changes dose-response safety margin vs concentration-response. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Directly supports nonlinear dose vs exposure logic. |
| Fig 2.129 | G p.160 | Active metabolite explains route-dependent apparent parent concentration-response. | USEFUL | YES | YES | VISUAL_INSPECTED | Key example, but text can convey main point. |
| Fig 2.130 | G p.160 | Mode of administration changes fetal toxicity at similar daily dose. | USEFUL | YES | NO | VISUAL_INSPECTED | Important exposure-case example. |
| Fig 2.131 | G p.161 | Ligand concentration, occupancy, biomarker response, and target concentration ranges. | USEFUL | YES | YES | VISUAL_INSPECTED | Dense figure; redraw would substantially improve learning. |
| Fig 2.132 | G p.162 | Repeated feeding in rats: single-dose + feeding simulation overpredicts exposure; model fit differs. | USEFUL | YES | NO | VISUAL_INSPECTED | Draft omitted; should be at least mentioned. |
| Fig 2.133 | G p.162 | U-shaped concentration-response and dose-dependent time-course consequences. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Core warning against dose-only thinking. |
| Fig 2.134 | G p.163 | Dose, total concentration, and unbound concentration can reverse compound potency order. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Essential for free/unbound exposure message. |
| Fig 2.135 | G p.163 | Four exposure measures: Css/average, Cmax, AUC, AUC above threshold and td. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Central C4 schematic. |
| Fig 41.1 | G p.662 | Observed and model-predicted Turbojoint concentrations across 310/520/780 µg/kg infusions. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Case-study anchor; Draft underuses it. |
| Table 41.1 | G p.662 | Dose-time-concentration data for Turbojoint across three infusion regimens. | USEFUL | YES | NO | VISUAL_INSPECTED | Full table need not be reproduced, but design must be anchored. |
| Fig 41.2 | G p.663 | Clearance decreases as Turbojoint dose increases. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Key evidence of nonlinear clearance. |
| Table A-1 | T p.759 | Generic oral 50 mg AUC calculation by trapezoidal rule, total AUC 26.60. | USEFUL | YES | NO | VISUAL_INSPECTED | Draft mislabeled; visual confirms generic example. |
| Fig A-1 | T p.760 | First trapezoid interval area as average concentration × time interval. | USEFUL | YES | NO | VISUAL_INSPECTED | Good beginner visual but Gabrielsson already covers core. |
| Table A-2 | T p.762 | Zileuton 600 mg oral concentration-time dataset. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Study problem dataset; useful only if examples expanded. |
| Fig H-1 | T p.790 | Urinary excretion method for MRT using amount remaining to be excreted. | USEFUL | YES | YES | VISUAL_INSPECTED | Draft omits excretion pathway; a small redraw could help. |
| Fig H-2 | T p.791 | Concentration declines while first-moment rises then declines; first-moment tail larger. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Core MRT/AUMC intuition. |
| Table H-1 | T p.792 | Numerical plasma/urine data yielding AUC, AUMC, MRT estimates. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Draft uses it correctly; retain. |
| Table H-2 | T p.793 | Input modes and mean input time: IV bolus 0, infusion Tinf/2, extravascular 1/Ka. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Directly supports C2/C3 input correction. |

---

## Required Patch List for Phase 4A

1. **Table A-1/Zileuton correction**  
   - Replace: `R&T Table A-1 zileuton`  
   - With: `R&T Table A-1: generic oral 50 mg AUC example, total AUC=26.60 mg·hr/L; R&T Table A-2: zileuton 600 mg PO concentration-time dataset.`

2. **λz half-life correction**  
   - Replace: `이상적으로 2–4 반감기`  
   - With: `이상적으로 3–4 반감기, 최소 3–4 terminal observations.`

3. **Remove unsupported numeric rules**  
   - Remove or tag as scenario: `λz error distorts AUC by 30–50%`.
   - Remove or tag as scenario: `AUMC extrapolation is 30–60%`.
   - Replace with: `AUMC extrapolation is generally more tail-sensitive than AUC extrapolation.`

4. **Regulatory/source boundary tags**  
   - Add `[실무 추론]` or `[외부 규제 연결: 별도 근거 필요]` to FDA/BA-BE/Clinical Hold/Deficiency/IR/FOCE/η-shrinkage claims.
   - In the source-anchored body, restrict ICH references to `ICH S3A and 7A` unless external citations are introduced later.

5. **PK41 Dynamic Source Anchor**  
   Add a compact anchor box in C4 or §8:
   - One volunteer, three 5h IV infusions, 310/520/780 µg·kg⁻¹, BW 70 kg.
   - NCA: CL decreased 1.6→0.9 L·h⁻¹·kg⁻¹; V 2.3→1.8 L·kg⁻¹; MRT 1.4→1.9 h.
   - Regression model: `V·dC/dt = In - Cl·C`, `Cl=Vmax/(Km+C)`.
   - Initial estimates from NCA: V≈2 L/kg, Km≈150, Vmax≈310; selected initial values 100 and 200 to challenge program.
   - Final: Vmax=184 µg·h⁻¹·kg⁻¹, Km=83 µg·L⁻¹, V=1.8 L·kg⁻¹.
   - Key author message: in capacity-limited kinetics, model parameters are Vmax, Km, and V rather than CL and V; CL and t1/2 are incompatible with mixed zero-/first-order kinetics.

6. **Exposure-case completeness**  
   - Add Fig 2.132 repeated-feeding rat safety study as one compressed sentence in C4 context.

7. **Holford/AUC vs CL author message**  
   - Add one sentence: `AUC is useful as exposure/toxicology or when dose is unknown, but CL or CL/F is more physiologically interpretable and directly computed from AUC and dose.`

8. **Observed vs predicted Clast wording**  
   - Replace “마지막 관측치가 회귀선 아래로 떨어지면” with “마지막 관측치가 terminal regression line에서 벗어나면”.

9. **Vss/Vz sanity check boundary**  
   - Keep as `[실무 sanity check]` if desired, but do not present `V_z ≥ Vss always` as a PDF-source statement.

---

## Final Audit Conclusion

Draft v0 is **not a failed draft**. It is structurally strong and suitable to proceed to Phase 4A after patching. The main issue is not concept selection but **source-boundary control**: the draft repeatedly blends textbook facts with expert/regulatory simulation scenarios. For the final HTML/textbook transformation, the safest path is:

1. Preserve the 4-card architecture.
2. Apply the MUST_FIX items above before any HTML conversion.
3. Keep practical/NONMEM/regulatory comments only when explicitly labeled as `[실무 추론]`, `[교육용 가상 시나리오]`, or `[후속 규제 연결]`.
4. Add PK41 as a compact dynamic source anchor because it is the strongest source-based example showing the transition from NCA to nonlinear regression.
5. Avoid unsupported numerical “rules of thumb” unless they are explicitly sourced or converted into hypothetical examples.

**Overall:** Conditional Go to Phase 4A Patch. Do not proceed directly to final HTML before the patch pass.

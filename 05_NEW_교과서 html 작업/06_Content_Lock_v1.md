# 06_Content Lock v1 — NCA·노출 평가·MRT·비구획 실무

**Source scope**: Gabrielsson & Weiner 5e Ch.2 §2.8–§2.9, PK41; Rowland & Tozer 5e Appendix A·H.  
**Primary pages**: Gabrielsson pp.141–164, pp.661–664; Rowland & Tozer pp.759–762, pp.789–793.  
**Output status**: Content Lock v1 / Markdown / Figure markers 없음.  
**Compression guard**: Step 1 Draft v0의 4-card 구조는 유지하되, 출처 없는 수치·규제 시나리오·중복 비유를 삭제하여 전체 길이를 v0보다 짧게 압축했다.

---

## Updated Curation Map

### MUST-tier

| Card | 개념 | 최종 판정 | Source tags |
|---|---|---|---|
| **C1** | AUC 계산: linear/log-linear trapezoidal rule, λz, extrapolation | **MUST** — 모든 NCA 파라미터의 분모가 되는 $AUC_0^\infty$의 신뢰도를 결정한다. | [G pp.141–148; T pp.759–762] |
| **C2** | AUMC와 MRT: first moment, residence time, input-time correction | **MUST** — $MRT=AUMC/AUC$와 MIT 보정이 $V_{ss}$ 해석으로 이어진다. | [G pp.142–151; T pp.789–793] |
| **C3** | CL, $V_{ss}$, $V_z$와 투여 경로 보정 | **MUST / Apex** — $V_{ss}=MRT\cdot CL$은 단순하지만, infusion/oral input 보정 누락 시 생리학적으로 불가능한 값까지 만들 수 있다. | [G pp.149–157; T p.793] |
| **C4** | Exposure metrics: $C_{max}$, AUC, $t_d$, $C_{ss}$, total/unbound concentration | **MUST** — §2.9의 핵심은 dose가 아니라 systemic exposure를 보는 것이다. | [G pp.158–164] |

### CONTEXT-tier

| 항목 | 통합 위치 | 압축 방식 |
|---|---|---|
| 정상상태 NCA: $AUC_{0-\tau,ss}=AUC_{0-\infty}$ | C1 | 1문장 context. [G p.152] |
| LOQ 미만 처리 | C1 | missing 처리 원칙으로 1문장. [G p.153] |
| Metabolite residence time: MDRT/MBRT/MIT | C2 | 시간 가산성의 일반화로 1문장. [G pp.155–156] |
| §2.9.1–§2.9.2 exposure 사례 | C4 | 여섯 사례를 한 압축 표로 통합. [G pp.158–163] |
| PK41 Turbojoint | C4/§8/Q4 | NCA→MM regression 전환 anchor로 삽입. [G pp.661–664] |
| R&T Table A-1, Table H-1, Table H-2 | C1/C2/§5/§7 | 계산 anchor로 유지. [T pp.759–760, pp.792–793] |

### REJECT / Deferred

- FDA 21 CFR 320, BA/BE 90% CI 80–125%, Clinical Hold, NDA Deficiency Letter, Information Request: **출처 범위 밖**. 본문에서는 삭제하거나 `[외부 규제 연결: 별도 근거 필요]` 수준으로만 남긴다.
- NONMEM code block, TMDD/PBPK, concentration-dependent vs time-dependent killing: **후속 세션 영역**.
- $V_z \ge V_{ss}$ “always” 단언: **PDF 직접 근거 없음**. 일반 sanity check로도 본 Lock에서는 핵심이 아니므로 삭제.
- Figure Inventory: Audit T6 항목은 Phase 4C로 그대로 이관하며 여기서 adjudication하지 않는다.

---

## Adjudication Table Summary

| Source | Item | Verdict | Rationale |
|---|---|---|---|
| Audit | 4-card architecture: C1–C4 | ADOPT | Gabrielsson §2.8–§2.9와 R&T Appendix A/H의 핵심 흐름을 가장 짧게 보존한다. |
| Audit | “NCA는 model-free가 아니라 compartment-free” | PARTIAL_ADOPT | 원문 직문은 아니므로 `[해석]`을 붙여 linear elimination 가정과 함께 사용한다. |
| Audit | nonlinear kinetics에서 NCA는 모델 추정 입력 | PARTIAL_ADOPT | PK41처럼 dose-dependent CL이 보이면 NCA는 final parameter가 아니라 initial estimate anchor로 제한한다. |
| Audit | λz 오류가 AUC를 30–50% 왜곡 | REJECT | PDF에 특정 30–50% 수치가 없으므로 삭제하고 정성적 민감성으로 교체한다. |
| Audit | BA/BE 90% CI 80–125%, FDA 21 CFR 320 | REJECT | 지정 PDF 밖의 규제 기준이므로 source-anchored body에서 삭제한다. |
| Audit | Linear trapezoidal AUC equation | ADOPT | Gabrielsson Eq.2:310과 R&T Table A-1에 의해 직접 지지된다. |
| Audit | Linear trapezoid bias: 상승 과소·하강 과대 | ADOPT | Fig 2.115의 핵심 교육 메시지다. |
| Audit | Log-linear trapezoid equation | ADOPT | Gabrielsson Eq.2:316 및 R&T Eq.A-7과 일치한다. |
| Audit | Log-linear rule 조건: descending only, zero/equal fallback | ADOPT | §2.8.3의 boundary condition으로 반드시 유지한다. |
| Audit | 혼합 linear-up/log-down을 “실무 표준”으로 단언 | PARTIAL_ADOPT | “사용 가능/흔히 사용”으로 완화하여 원문보다 강한 표현을 피한다. |
| Audit | $AUC_{tlast\to\infty}=C_{last}/\lambda_z$ | ADOPT | Eq.2:311/2:319의 핵심 외삽식이다. |
| Audit | predicted $\hat C_{last}$ 권고 | PARTIAL_ADOPT | “항상”이 아니라 관측치가 terminal regression에서 벗어날 때 일반 권고로 표현한다. |
| Audit | % extrapolated area | ADOPT | Eq.2:324 및 20–25% 권고와 연결된다. |
| Audit | Extrapolated AUC 20–25% threshold | ADOPT | Gabrielsson p.148의 실무 경계로 유지한다. |
| Audit | λz 최소 3–4 observations | ADOPT | terminal slope 신뢰도의 최소 요건이다. |
| Audit | λz ideal 2–4 half-lives | ADOPT | 오류이므로 `3–4 half-lives`로 수정한다. |
| Audit | 마지막 관측치가 “아래”로 떨어지면 제외 | PARTIAL_ADOPT | 방향 한정 없이 terminal regression line에서 벗어나는 경우로 수정한다. |
| Audit | LOQ 미만 zero/LOQ 치환 금지 | ADOPT | §2.8.6의 데이터 처리 원칙으로 유지한다. |
| Audit | AUMC linear trapezoid | ADOPT | Eq.2:312와 일치한다. |
| Audit | AUMC extrapolation formula | ADOPT | Eq.2:313/2:320 및 R&T Eq.H-9와 일치한다. |
| Audit | AUMC tail 30–60% rule | REJECT | 일반 수치 규칙은 PDF에 없으므로 삭제한다. |
| Audit | R&T molecule-counting MRT intuition | ADOPT | Appendix H의 핵심 직관으로 C2에 유지한다. |
| Audit | $MRT=\sum t_j/N$ | ADOPT | R&T Eq.H-1의 분자 수준 정의다. |
| Audit | $MRT=AUMC/AUC$ | ADOPT | R&T Eq.H-8 및 Gabrielsson MRT 식과 일치한다. |
| Audit | Infusion/oral MIT correction | ADOPT | $T_{inf}/2$, $1/K_a$ 보정은 C2–C3 연결의 핵심이다. |
| Audit | MAT/$K_a$ caveat | PARTIAL_ADOPT | oral absorption 맥락에서 1문장으로만 통합한다. |
| Audit | MDRT/MBRT/MIT metabolite NCA | PARTIAL_ADOPT | 본문을 늘리지 않도록 C2 context 1문장으로 제한한다. |
| Audit | CL, CL/F, F equations | ADOPT | Eq.2:325–2:327의 핵심 파라미터다. |
| Audit | $V_{ss}$ and $V_z$ equations | ADOPT | Eq.2:337–2:338을 C3의 formal core로 유지한다. |
| Audit | $V_z\ge V_{ss}$ always | REJECT | 지정 PDF에 직접 근거가 없어 삭제한다. |
| Audit | Effective half-life $=\ln(2)\cdot MRT$ | ADOPT | MRT vs half-life 혼동쌍에 필요한 최소 수식으로 유지한다. |
| Audit | Steady-state AUC equivalence | PARTIAL_ADOPT | C1 context 1문장으로 압축한다. |
| Audit | Unequal dosing interval equations | REJECT | 세션 10분 handout 기준으로 우선순위가 낮아 삭제한다. |
| Audit | Short half-life/input alternative equations | ADOPT | §2.8.8의 핵심 경고이므로 C3에 유지한다. |
| Audit | Eq.2:366 avoids zero/negative $V_{ss}$ | ADOPT | Apex 카드의 실무적 이유를 설명한다. |
| Audit | 특정 가상 수치 $t_{1/2}\approx0.5h$, $V_{ss}=-0.4$ | PARTIAL_ADOPT | 본문 사실처럼 쓰지 않고 `[교육용 가상 시나리오]`로 축소한다. |
| Audit | PK41 doses/design | ADOPT | Scope Lock의 required source anchor이므로 C4와 Q4에 삽입한다. |
| Audit | PK41 NCA CL/V/MRT dose-dependence | ADOPT | nonlinear transition의 가장 강한 실제 anchor다. |
| Audit | PK41 initial/final MM estimates | ADOPT | NCA→regression workflow의 완결성을 위해 Q4와 C4에 유지한다. |
| Audit | CL and $t_{1/2}$ incompatible with mixed zero-/first-order kinetics | ADOPT | PK41 결론의 핵심 문장이다. |
| Audit | R&T Table A-1 “zileuton” | ADOPT | 오류 수정: Table A-1은 generic oral 50 mg AUC=26.60; zileuton은 Table A-2다. |
| Audit | R&T IV bolus AUC special case | REJECT | 유용하지만 MUST 흐름에 필요하지 않아 삭제한다. |
| Audit | R&T log-trapezoid twofold discrepancy note | REJECT | C1이 이미 충분하므로 압축 기준에서 삭제한다. |
| Audit | R&T Table H-1 values | ADOPT | AUC/AUMC/MRT 수치 검증 예시로 유지한다. |
| Audit | ICH E1/M3 | REJECT | 원문 범위에서는 ICH S3A/7A만 확인되며, 본 Lock에서는 규제 문헌 확장을 하지 않는다. |
| Audit | $C_u=C_{total}\cdot f_u$ | PARTIAL_ADOPT | 일반 정의 보충으로만 사용하고 PDF 직접 수식처럼 표시하지 않는다. |
| Audit | $C_{ss}=D/(\tau\cdot CL)$ | PARTIAL_ADOPT | exposure metric 설명 수준으로만 유지한다. |
| Audit | Software-specific claims: Phoenix/PKNCA/NONMEM | PARTIAL_ADOPT | 제품명은 삭제하고 자동 λz 선택 수동 검증 원칙만 `[실무 확장]`으로 남긴다. |
| Audit | FOCE/local optimum/η-shrinkage chain | PARTIAL_ADOPT | NCA-IIV warning은 `[실무 추론]`으로 압축하고 세부 수치는 삭제한다. |
| Audit | Clinical Hold/Deficiency/IR scenarios | REJECT | PDF에 근거가 없으므로 삭제하거나 가상 시나리오로만 제한한다. |
| Audit | Exposure Fig 2.132 repeated-feeding example omitted | ADOPT | C4 exposure-case 표에 1문장으로 추가한다. |
| Audit | R&T urinary MRT path omitted | PARTIAL_ADOPT | plasma-only 오해를 막기 위해 C2에 1문장 추가한다. |
| Crucible A1 | flip-flop kinetics silent failure | PARTIAL_ADOPT | $V_z\ge V_{ss}$ 단언은 삭제하고 “정상 단위·양수 출력이 오히려 위험”으로 반영한다. |
| Crucible A2 | AUMC tail의 $\lambda_z$ 2차 의존성 | ADOPT | MRT 불안정성의 핵심 직관으로 C2에 삽입한다. |
| Crucible A3 | Holford: CL/F primary, AUC exposure metric | PARTIAL_ADOPT | NDA 표현은 줄이고 “생리학적 해석성” 메시지만 §8에 반영한다. |
| Crucible A4 | 두 $V_{ss}$ 공식의 불일치가 적용 영역 진단 | ADOPT | §5 Pair 3와 Q9에 반영한다. |
| Crucible A5 | NCA-IIV는 PopPK $\omega^2$의 상한 | PARTIAL_ADOPT | `[실무 추론]`으로 §8 failure mode에 압축한다. |
| Crucible B1 | PK41에서 NCA-CL 보고 위험 | PARTIAL_ADOPT | “CL/$t_{1/2}$는 혼합 zero-/first-order kinetics와 incompatible”로 source-boundary 안에서 반영한다. |
| Crucible B2 | NDA exposure priority justification | REJECT | 문헌 범위 밖 reviewer framing이므로 삭제한다. |
| Crucible B3 | 자동 λz 선택 검증 | PARTIAL_ADOPT | 제품명 없이 시각적 terminal slope 검증 원칙으로 축소한다. |
| Crucible B4 | 4개 카드의 직렬 EDA workflow | ADOPT | §1 concept navigation에 반영한다. |
| Crucible B5 | Dose escalation NCA-CL pattern | PARTIAL_ADOPT | PK41 anchor의 해석 문장으로만 유지한다. |
| Crucible C1–C6 | NONMEM code, TMDD/PBPK, BA/BE numeric rule, PK/PD killing, ICH E1/M3, $V_z\ge V_{ss}$ always | REJECT | scope creep 또는 source 미지원 항목이다. |
| Crucible T4 | deletion/compression candidates | ADOPT | unsupported 수치, 규제 시나리오, 과잉 비유는 모두 삭제·압축한다. |

---

# §1 — Session Header & Roadmap

**Session Title**: 비구획 분석(NCA) — AUC, AUMC, MRT, $V_{ss}$와 노출 평가의 실무 경계  
**Source**: Gabrielsson & Weiner 5e Ch.2 §2.8–§2.9, PK41; Rowland & Tozer 5e Appendix A·H. [G pp.141–164, pp.661–664; T pp.759–762, pp.789–793]

<!-- MASTER LENS -->
**Big Idea**: NCA는 `[해석]` *model-free*라기보다 *compartment-free*에 가깝다. 특정 compartment model을 세우지 않아도 되지만, sampling compartment에서의 **linear elimination** 가정은 여전히 필요하며, PK41처럼 capacity-limited kinetics가 보이면 NCA 결과는 최종 해석값이 아니라 nonlinear regression의 **initial parameter anchor**로 내려와야 한다. [G p.141; G pp.661–664]

<!-- ANCHOR -->
**개념 항법도**: 이 세션의 네 카드는 병렬 암기 목록이 아니라 Phase 1 SAD/MAD EDA에서 순서대로 작동하는 직렬 workflow다.

| Step | 판단 질문 | Card | 오류 전파 |
|---|---|---|---|
| 1 | 면적이 믿을 만한가? | C1 AUC/λz/extrapolation | AUC 오류 → CL, V, exposure 모두 왜곡 |
| 2 | 시간 모멘트가 안정적인가? | C2 AUMC/MRT | AUMC tail 오류 → MRT와 $V_{ss}$ 왜곡 |
| 3 | 분포·청소 파라미터가 경로 보정됐는가? | C3 CL/$V_{ss}$/$V_z$ | MIT 누락 → $V_{ss}$ 해석 오류 |
| 4 | 어떤 노출 지표로 PD/safety를 볼 것인가? | C4 exposure metrics | dose-only 해석 → exposure-response 판단 오류 |

**선행 지식**: CL/V 정의, 1-·2-compartment model, Michaelis-Menten kinetics, $t_{1/2}=\ln(2)/k$.  
**후속 연결**: PopPK 초기 모수 설정, nonlinear PK regression, BA/BE·clinical pharmacology 보고서의 exposure table 구성. 단, 구체적 외부 규제 기준은 본 source scope 밖이다.

<!-- RECAP -->
**§1 Recap**: NCA의 강점은 단순함이고, 약점도 같은 지점에서 온다. 모델을 덜 세우는 대신, terminal slope·input correction·linear elimination 가정이 무너지면 오류가 조용히 후속 분석으로 전파된다.

---

# §2 — Concept Anatomy Cards

## C1. AUC 계산 — linear/log-linear trapezoidal rule, λz, extrapolation

<!-- MASTER LENS -->
### Big Idea

AUC는 “관측된 곡선 아래 면적” 하나가 아니라 **관측 구간의 사다리꼴 합 + terminal slope로 외삽한 미래 면적**이다. 따라서 NCA 신뢰도의 첫 질문은 “AUC가 얼마인가?”가 아니라 “관측 면적과 외삽 면적의 비율, 그리고 $\lambda_z$ 선택이 방어 가능한가?”이다. [G pp.142–148]

### A. Formal definition

- **AUC (zero moment area)**: concentration-time curve 아래 면적. [G p.142]
- **AUC$_{0-tlast}$**: 관측 자료로 계산한 면적.
- **AUC$_{tlast\to\infty}$**: 마지막 측정 시점 이후를 mono-exponential decline으로 가정해 외삽한 면적.
- **Total AUC**: $AUC_{0-tlast}+AUC_{tlast\to\infty}$.

### B. Equations and source-locked rules

**Linear trapezoidal rule** [G p.143, Eq.2:310; T pp.759–760]

$$
AUC_0^{t_{last}}=\sum_i \frac{C_i+C_{i+1}}{2}\cdot \Delta t
$$

R&T Table A-1의 generic oral 50 mg 예시는 이 계산으로 total AUC=26.60 mg·hr/L을 얻는다. 이 예시는 **zileuton이 아니다**. Zileuton은 R&T Table A-2의 600 mg oral dataset이다. [T pp.759–762]

**Bias direction**: linear trapezoid는 상승 구간에서 underestimate, 하강 구간에서 overestimate한다. 이 편향은 sampling interval이 half-life에 비해 클수록 커진다. [G p.142]

**Log-linear trapezoidal rule** [G pp.144–145, Eq.2:316; T p.761]

$$
AUC_i^{i+1}=\frac{C_i-C_{i+1}}{\ln(C_i/C_{i+1})}\cdot \Delta t
$$

적용 조건은 **descending data**다. $C_i=0$ 또는 $C_{i+1}=C_i$이면 log-linear rule은 실패하므로 linear fallback을 쓴다. [G p.144]

**Mixed approach**: increasing/equal 구간은 linear, decreasing 구간은 log-linear로 처리할 수 있다. 단, “항상 표준”이라고 단언하지 말고, 합리적 sampling design에서는 두 방법 차이가 대개 임상적으로 작다는 저자 균형도 함께 기억한다. [G p.146]

**Terminal extrapolation** [G pp.143–145, Eq.2:311/2:319]

$$
AUC_{t_{last}\to\infty}=\frac{C_{last}}{\lambda_z}
$$

관측 $C_{last}$가 terminal regression line에서 벗어나면, 관측값 대신 regression 기반 예측값 $\hat C_{last}$ 사용이 일반적으로 권고된다. [G p.147]

**Percent extrapolated area** [G p.148, Eq.2:324]

$$
\%Extrapolated=\frac{AUC_{t_{last}\to\infty}}{AUC_{total}}\times 100
$$

저자 권고는 extrapolated area가 일반적으로 total AUC의 20–25%를 넘지 않는 것이다. 넘으면 preliminary estimate로 다뤄야 한다. [G p.148]

### C. λz selection

Terminal slope는 semi-log plot에서 individual profile을 보고 정한다. 최소 3–4 observations가 필요하고, 이상적으로 terminal phase에서 **3–4 half-lives**가 경과해야 한다. [G p.146]

<!-- TRENCH -->
**Trench-Level Tip**: 자동 NCA output의 $\lambda_z$ 구간은 그대로 믿지 말고 semi-log plot에서 terminal phase인지 직접 확인한다. 높은 adjusted $R^2$만으로 분포기 점이 terminal slope에 섞이면 AUC tail뿐 아니라 CL, $V_z$, $V_{ss}$까지 연쇄적으로 흔들린다. `[실무 확장]`

### D. Context notes

- 정상상태에서는 한 dosing interval의 $AUC_{0-\tau,ss}$가 single-dose $AUC_{0-\infty}$와 동등하게 취급될 수 있다. 이전 투여의 잔류 면적과 다음 투여의 외삽 면적이 상쇄되기 때문이다. [G p.152]
- LOQ 미만 값은 zero나 LOQ로 대체하지 않고 missing으로 처리하는 원칙이 제시된다. [G p.153]

### E. Boundary conditions

| 조건 | 깨지면 생기는 문제 |
|---|---|
| Linear elimination | $\lambda_z$와 extrapolated AUC의 의미가 약해진다. |
| Terminal phase가 실제 terminal phase | absorption/distribution phase를 terminal로 착각하면 tail이 왜곡된다. |
| Extrapolated fraction ≤20–25% | 초과 시 NCA 결과는 preliminary 성격이 강해진다. |
| 관측 $C_{last}$가 regression line과 일치 | 벗어나면 $\hat C_{last}$ 사용을 검토한다. |

### F. Zettelkasten atom

> **NCA-AUC atom**: AUC는 사다리꼴 합이 아니라 “사다리꼴 합 + $\lambda_z$ 기반 tail”이다. 그래서 AUC 검토의 핵심은 값 자체가 아니라 terminal slope 선택, $\hat C_{last}$ 사용 여부, %extrapolated area다. [G pp.143–148]

<!-- RECAP -->
**C1 Recap**: AUC가 흔들리면 CL, $V_z$, $V_{ss}$, exposure comparison이 모두 흔들린다. NCA audit은 항상 $\lambda_z$ plot과 %extrapolated area에서 시작한다.

---

## C2. AUMC와 MRT — first moment와 평균 체류시간

<!-- MASTER LENS -->
### Big Idea

AUMC는 concentration에 time을 곱한 first moment이고, MRT는 그 first moment를 AUC로 나눈 평균 체류시간이다. AUC보다 AUMC가 더 불안정한 이유는 단순히 “tail이 크다”가 아니라, AUMC tail에 $1/\lambda_z$와 $1/\lambda_z^2$ 항이 동시에 들어가 terminal slope 오류가 더 강하게 반영되기 때문이다. [G pp.142–148; T pp.789–792]

### A. Formal definition

- **AUMC**: $t\cdot C(t)$ 대 time curve 아래 면적, 즉 first moment area. [G p.142]
- **MRT**: body 또는 sampling system 안에 molecule이 머무는 평균 시간. [T p.789]

R&T Appendix H는 1 mg, molecular weight 300 g/mol 약물에 약 $2\times10^{18}$ molecules가 들어 있다는 직관에서 시작해, 각 molecule의 residence time 평균을 MRT로 정의한다. [T p.789]

### B. Equations

**AUMC by linear trapezoid** [G p.144, Eq.2:312]

$$
AUMC_0^{t_{last}}=\sum_i \frac{t_iC_i+t_{i+1}C_{i+1}}{2}\cdot\Delta t
$$

**AUMC tail** [G pp.144–145, Eq.2:313/2:320]

$$
AUMC_{t_{last}\to\infty}=\frac{t_{last}C_{last}}{\lambda_z}+\frac{C_{last}}{\lambda_z^2}
$$

**Molecular definition** [T p.789, Eq.H-1]

$$
MRT=\frac{\sum_j t_j}{N}
$$

**Plasma definition** [T p.791, Eq.H-8]

$$
MRT=\frac{AUMC_0^\infty}{AUC_0^\infty}
$$

R&T Table H-1의 numerical example은 AUC=44.2 mg·hr/L, AUMC=177 mg·hr²/L, plasma MRT≈4.0 hr, urinary MRT≈4.25 hr, simulated MRT≈4.3 hr로 서로 일관된다. [T p.792]

### C. Input-time correction

Observed MRT에는 drug이 systemic circulation에 들어오기까지 걸리는 input time이 섞인다. 따라서 해석하려는 residence time에 맞게 mean input time (MIT)을 빼야 한다. [G pp.149–151; T p.793]

| Input mode | MIT | Corrected MRT |
|---|---:|---|
| IV bolus | 0 | $MRT=AUMC/AUC$ |
| Constant IV infusion | $T_{inf}/2$ | $MRT=AUMC/AUC-T_{inf}/2$ |
| First-order extravascular input | $1/K_a$ | $MRT=AUMC/AUC-1/K_a$ |

Oral absorption에서 $K_a$는 단순 흡수만이 아니라 degradation 등 병렬 과정을 포함할 수 있으므로, $1/K_a$를 “순수 흡수시간”으로 과해석하지 않는다. [G p.150]

### D. Context extension

Metabolite 또는 downstream compartment에서는 $MBRT$에서 upstream input residence time을 빼는 방식으로 $MDRT$를 정의한다. 핵심은 residence time이 “공간별 고유 시간 + input time”으로 누적된다는 점이다. [G pp.155–156]

R&T는 urinary excretion data에서도 MRT를 계산할 수 있음을 보이지만, 이 세션에서는 plasma MRT가 주축이다. 이 1문장만으로 plasma-only 오해를 방지한다. [T pp.790–792]

### E. Boundary conditions

| 조건 | 깨지면 생기는 문제 |
|---|---|
| Tail sampling 충분 | AUMC는 late time에 더 민감하므로 tail 부족이 MRT를 크게 흔든다. |
| $\lambda_z$ 신뢰 가능 | $1/\lambda_z^2$ 항 때문에 AUMC tail 민감도가 커진다. |
| Input mode 정확 | MIT 보정 누락 시 MRT와 $V_{ss}$가 함께 왜곡된다. |
| Linear elimination | MRT 해석이 compartment-free residence time으로 유지된다. |

### F. Zettelkasten atom

> **NCA-MRT atom**: MRT는 half-life가 아니다. MRT는 “분자가 system 안에서 보낸 시간의 평균”이고, 계산상으로는 $AUMC/AUC$이며, 투여 경로에 따라 MIT를 빼야 해석 가능한 residence time이 된다. [G pp.149–151; T pp.789–793]

<!-- RECAP -->
**C2 Recap**: AUMC는 time-weighted exposure다. 그래서 tail과 input correction을 놓치면 MRT는 안정적인 평균이 아니라 terminal slope 오류를 증폭한 숫자가 된다.

---

## C3. Apex — CL, $V_{ss}$, $V_z$와 투여 경로 보정

<!-- MASTER LENS -->
### Big Idea

$CL$, $V_{ss}$, $V_z$는 NCA output 표에 나란히 나오지만 같은 종류의 숫자가 아니다. $CL$은 제거 능력, $V_{ss}$는 steady-state 분포 크기, $V_z$는 terminal slope와 결합된 apparent volume이다. 특히 $V_{ss}=MRT\cdot CL$은 input correction이 빠지면 매우 그럴듯하지만 잘못된 분포 부피가 된다. [G pp.149–157]

### A. Core equations

**Clearance** [G p.149, Eq.2:325]

$$
CL=\frac{D_{iv}}{AUC_0^\infty}
$$

**Oral apparent clearance** [G p.149, Eq.2:326]

$$
CL_o=\frac{CL}{F}=\frac{D_{po}}{AUC_0^\infty}
$$

**Bioavailability** [G p.149, Eq.2:327]

$$
F=\frac{AUC_{po}}{AUC_{iv}}\cdot\frac{D_{iv}}{D_{po}}
$$

**Steady-state volume of distribution** [G p.151, Eq.2:337]

$$
V_{ss}=MRT\cdot CL=\frac{D_{iv}\cdot AUMC_0^\infty}{(AUC_0^\infty)^2}
$$

**Terminal volume** [G p.151, Eq.2:338]

$$
V_z=\frac{CL}{\lambda_z}=\frac{D_{iv}}{AUC_0^\infty\cdot\lambda_z}
$$

**Effective half-life** [G p.151]

$$
t_{1/2,eff}=\ln(2)\cdot MRT
$$

### B. Why C3 is the Apex

<!-- ANCHOR -->
C1이 AUC를 만들고, C2가 MRT를 만들고, C3가 이 둘을 CL과 volume으로 변환한다. 따라서 C3의 오류는 독립 오류가 아니라 **앞선 두 카드의 오류가 임상 파라미터 이름을 달고 나타나는 최종 형태**다.

| Parameter | Depends on | Main failure |
|---|---|---|
| $CL$ | Dose, AUC | AUC tail 오류가 clearance 오류로 변한다. |
| $V_{ss}$ | CL, MRT | input correction 누락과 AUMC tail 오류가 함께 들어온다. |
| $V_z$ | CL, $\lambda_z$ | terminal slope 선택에 직접 묶인다. |

### C. §2.8.8 special case — half-life short relative to input time

Half-life가 input time에 비해 짧으면 standard MRT/$V_{ss}$ 계산이 불안정해질 수 있다. Gabrielsson은 이 경우 washout AUC from steady state를 이용한 대안식이 더 robust하며 zero 또는 negative $V_{ss}$를 피한다고 설명한다. [G pp.157–158]

$$
V_{ss}=\frac{K_0\cdot AUC_{t^*\to\infty}}{C_{ss}^2}
$$

$$
MRT=\frac{AUC_{t^*\to\infty}}{C_{ss}}
$$

위 식은 $T_{inf}$가 긴 상황에서 표준식만 붙잡으면 생기는 문제를 줄이기 위한 대안이다. [G p.157, Eq.2:366/2:367]

<!-- TRENCH -->
**Trench-Level Tip**: 표준 $V_{ss}$ 식(Eq.2:337)과 §2.8.8 대안식(Eq.2:366)을 함께 계산했을 때 값이 잘 맞으면 정상 적용 영역에 가깝고, 크게 벌어지면 input time과 half-life의 비율 자체가 문제라는 신호다. [G pp.151, 157]

### D. Limitations

- **Flip-flop kinetics**: oral NCA에서 terminal slope가 elimination이 아니라 absorption을 반영할 수 있다. 위험한 이유는 값이 음수처럼 “비명을 지르는” 것이 아니라, 양수·정상 단위의 그럴듯한 output으로 나타날 수 있기 때문이다. `[실무 해석]`
- **Nonlinear elimination**: capacity-limited kinetics에서는 CL과 $t_{1/2}$가 first-order parameter이므로 mixed zero-/first-order kinetics와 양립하지 않는다. PK41이 대표 anchor다. [G p.664]
- **NCA-IIV**: NCA의 개체간 분산은 IIV와 residual/error contribution을 함께 포함하므로 PopPK $\omega^2$의 직접 추정값이 아니라 상한으로 보는 것이 안전하다. `[실무 추론]`

### E. Zettelkasten atom

> **NCA-volume atom**: $V_{ss}$는 “분포 부피 하나”가 아니라 $AUC$, $AUMC$, CL, input correction이 모두 통과한 최종 요약값이다. 따라서 $V_{ss}$를 볼 때는 항상 “어떤 MRT를 썼는가?”와 “input time을 뺐는가?”를 같이 봐야 한다. [G pp.149–157]

<!-- RECAP -->
**C3 Recap**: C3는 Apex다. AUC와 AUMC의 작은 불확실성은 여기서 CL과 volume이라는 임상적 이름을 얻고, 그 순간부터 훨씬 설득력 있어 보이기 때문이다.

---

## C4. Exposure metrics — dose가 아니라 concentration을 본다

<!-- MASTER LENS -->
### Big Idea

§2.9의 핵심은 “투여량(dose)”보다 **systemic exposure**, 특히 total 또는 unbound systemic plasma concentration을 보라는 것이다. 같은 dose라도 route, first-pass, nonlinear elimination, active metabolite, protein binding, 투여 방식에 따라 실제 target exposure는 달라진다. [G pp.158–164]

### A. Exposure measures

| Metric | 의미 | 사용 직관 | Source |
|---|---|---|---|
| $C_{max}$ | peak exposure | acute toxicity, peak-driven effect | [G p.163] |
| AUC | total exposure | cumulative exposure, extent comparison | [G p.163] |
| $t_d$ | threshold 이상 지속시간 | time-above-threshold type 판단 | [G p.163] |
| $C_{ss}$ / average concentration | steady-state intensity | chronic dosing exposure | [G p.163] |
| unbound concentration | pharmacologically available fraction | protein binding 차이 비교 | [G p.163] |

$C_u=C_{total}\cdot f_u$는 일반 정의 보충이며, PDF의 직접 수식 인용으로 취급하지 않는다. [G p.163; 정의 보충]

### B. §2.9 cases compressed

| Case | 핵심 교훈 | Source |
|---|---|---|
| Route/bioavailability | dose-response가 route 차이로 흔들려도 concentration-response는 정렬될 수 있다. | [G p.159] |
| Nonlinear elimination | dose 증가는 exposure와 safety margin을 비선형적으로 바꾼다. | [G p.159] |
| Active metabolite | parent concentration만 보면 route-dependent response를 오해할 수 있다. | [G p.160] |
| Mode of administration | 같은 daily dose라도 infusion/feeding pattern이 toxicity를 바꿀 수 있다. | [G p.160] |
| Occupancy/biomarker | ligand concentration, receptor occupancy, biomarker response는 같은 축이 아니다. | [G p.161] |
| Repeated feeding | single-dose + feeding simulation이 반복급여 노출을 과대예측할 수 있다. | [G p.162] |
| U-shaped response | exposure-response가 단조가 아니면 dose만으로 효과를 예측할 수 없다. | [G p.162] |
| Protein binding | total concentration과 unbound concentration은 potency ranking을 뒤집을 수 있다. | [G p.163] |

### C. PK41 dynamic source anchor — NCA에서 nonlinear regression으로

Turbojoint® PK41은 한 지원자에게 310, 520, 780 µg·kg⁻¹을 각각 5시간 IV infusion한 사례다. NCA에서 dose가 증가할수록 CL은 1.6→0.9 L·h⁻¹·kg⁻¹로 감소했고, V는 2.3→1.8 L·kg⁻¹, MRT는 1.4→1.9 h로 변했다. [G pp.661–662]

이 패턴은 “dose escalation에서 NCA-CL이 단조 감소하면 capacity-limited elimination을 의심하라”는 source-anchored signal이다. 이후 모델은

$$
V\cdot\frac{dC}{dt}=In-CL\cdot C,\qquad CL=\frac{V_{max}}{K_m+C}
$$

로 전환되며, NCA 결과는 $V\approx2$ L/kg, $K_m\approx150$ µg/L, $V_{max}\approx310$ µg·h⁻¹·kg⁻¹ 등의 initial estimate를 제공한다. 최종 추정값은 $V_{max}=184$ µg·h⁻¹·kg⁻¹, $K_m=83$ µg/L, $V=1.8$ L/kg이었다. 저자의 결론은 명확하다: capacity-limited one-compartment system의 parameters는 CL과 V가 아니라 $V_{max}$, $K_m$, V이며, CL과 $t_{1/2}$는 mixed zero-/first-order kinetics와 incompatible하다. [G pp.663–664]

### D. Zettelkasten atom

> **Exposure atom**: dose는 투입량이고 exposure는 body 또는 target이 실제로 본 concentration-time burden이다. §2.9의 모든 사례는 “dose가 같아도 exposure가 다르면 response가 달라진다”는 한 문장으로 수렴한다. [G pp.158–164]

<!-- RECAP -->
**C4 Recap**: C4는 계산 카드가 아니라 해석 카드다. NCA가 AUC와 concentration metrics를 만든 뒤, 어떤 metric을 efficacy/safety argument의 중심에 둘지 결정하는 단계다.

---

# §5 — Confusion Pair Dissection

<!-- CONFUSION -->
## Pair 1. AUC vs AUMC — zero moment vs first moment

| 구분 | AUC | AUMC |
|---|---|---|
| 정의 | $C(t)$ 아래 면적 | $t\cdot C(t)$ 아래 면적 |
| 의미 | 총 노출량 | 시간이 가중된 노출량 |
| tail | $C_{last}/\lambda_z$ | $t_{last}C_{last}/\lambda_z+C_{last}/\lambda_z^2$ |
| downstream | CL, exposure comparison | MRT, $V_{ss}$ |

**Critical distinction**: AUMC는 late concentration을 time으로 다시 가중하므로, 같은 terminal slope 오류라도 MRT와 $V_{ss}$에 더 민감하게 전달된다. [G pp.142–148]

<!-- CONFUSION -->
## Pair 2. MRT vs $t_{1/2}$ — 평균 체류시간 vs 50% 감소시간

| 구분 | MRT | $t_{1/2}$ |
|---|---|---|
| 질문 | molecule이 평균적으로 얼마나 오래 머무는가? | 농도가 절반으로 줄어드는 시간은? |
| 계산 | $AUMC/AUC$ 또는 MIT 보정 후 값 | $\ln(2)/\lambda_z$ |
| 성격 | system residence 평균 | terminal decline descriptor |
| 함정 | input time 포함 가능 | multi-phase profile에서 단일 반감기 과해석 |

**Critical distinction**: MRT는 분포와 제거를 통합한 평균 시간이고, $t_{1/2}$는 terminal slope의 시간 척도다. 둘은 한-compartment monoexponential 상황에서 가까워질 수 있지만 같은 개념이 아니다. [G p.151; T pp.789–793]

<!-- CONFUSION -->
## Pair 3. $V_{ss}$ vs $V_z$ — steady-state distribution vs terminal-slope volume

| 구분 | $V_{ss}$ | $V_z$ |
|---|---|---|
| 계산 | $MRT\cdot CL$ | $CL/\lambda_z$ |
| 지배 요소 | AUC + AUMC + input correction | AUC + terminal slope |
| 해석 | steady-state distribution size | terminal phase 기반 apparent volume |
| 주된 함정 | MIT 누락, AUMC tail 오류 | 잘못된 $\lambda_z$ 선택 |

**Critical blow**: 같은 $V_{ss}$라도 표준 Eq.2:337과 §2.8.8 대안 Eq.2:366이 크게 다르면, “어느 공식이 맞나?”보다 먼저 “현재 데이터가 표준식 적용 영역인가?”를 물어야 한다. [G pp.151, 157]

<!-- RECAP -->
**§5 Recap**: 이 세션의 혼동쌍은 모두 “같아 보이는 요약 숫자” 문제다. AUC/AUMC, MRT/half-life, $V_{ss}/V_z$는 output table에서 가까이 있지만 서로 다른 질문에 답한다.

---

# §7 — Self-Test: Active Recall Module

<!-- SELF-TEST -->
## Q1. Linear trapezoidal AUC와 log-linear trapezoidal AUC의 수식을 쓰고, 각각의 적용 조건을 말하라.

**Answer**: Linear rule은 $\sum [(C_i+C_{i+1})/2]\Delta t$이며 상승·평탄·하강 모두 계산 가능하지만 하강 구간에서 overestimate한다. Log-linear rule은 $(C_i-C_{i+1})/\ln(C_i/C_{i+1})\cdot\Delta t$이며 descending data에서만 유효하고 $C_i=0$ 또는 $C_{i+1}=C_i$에서는 linear fallback이 필요하다. [G pp.143–145]

<!-- SELF-TEST -->
## Q2. $\lambda_z$ 추정의 최소 조건과 이상 조건은?

**Answer**: 최소 3–4 terminal observations가 필요하고, 이상적으로 terminal phase에서 3–4 half-lives가 경과해야 한다. 관측 마지막 농도가 terminal regression line에서 벗어나면 $\hat C_{last}$를 검토한다. [G pp.146–147]

<!-- SELF-TEST -->
## Q3. Extrapolated AUC가 total AUC의 30%라면 어떻게 보고할 것인가?

**Answer**: Gabrielsson의 일반 권고 20–25%를 넘으므로, 최종적인 신뢰 파라미터처럼 쓰기보다 preliminary estimate 성격을 명시한다. 추가 sampling 또는 terminal phase 재검토가 필요하다. [G p.148]

<!-- SELF-TEST -->
## Q4. PK41에서 NCA 결과가 nonlinear regression의 initial estimate로 전환되는 흐름을 설명하라.

**Answer**: Turbojoint®에서 310/520/780 µg·kg⁻¹ 5h IV infusion 후 dose 증가에 따라 NCA-CL이 1.6→0.9 L·h⁻¹·kg⁻¹로 감소했다. 이는 capacity-limited elimination signal이며, NCA는 final CL 보고가 아니라 $V_{max}$, $K_m$, V를 갖는 Michaelis-Menten regression의 initial estimate anchor가 된다. 최종 추정값은 $V_{max}=184$ µg·h⁻¹·kg⁻¹, $K_m=83$ µg/L, V=1.8 L/kg이었다. [G pp.661–664]

<!-- SELF-TEST -->
## Q5. R&T Table H-1에서 AUC=44.2, AUMC=177이면 plasma MRT는 얼마인가?

**Answer**: $MRT=AUMC/AUC=177/44.2\approx4.0$ hr이다. 같은 예시에서 urinary MRT≈4.25 hr, simulated MRT≈4.3 hr로 일관된다. [T p.792]

<!-- SELF-TEST -->
## Q6. IV bolus에서 CL은 어떻게 계산하며, oral 투여에서는 무엇이 달라지는가?

**Answer**: IV bolus/IV 투여에서는 $CL=D_{iv}/AUC_0^\infty$다. Oral에서는 bioavailability가 섞이므로 $CL/F=D_{po}/AUC_0^\infty$로 apparent clearance를 계산한다. [G p.149]

<!-- SELF-TEST -->
## Q7. Acute toxicity, cumulative exposure, threshold-driven effect에 각각 어떤 exposure metric을 우선 볼 것인가?

**Answer**: Acute toxicity는 $C_{max}$, cumulative exposure는 AUC, threshold-driven effect는 $t_d$ 또는 AUC above threshold를 우선 본다. 실제 선택은 drug mechanism과 response time course에 맞춰 정당화해야 한다. [G p.163]

<!-- SELF-TEST -->
## Q8. Total concentration 기준 potency ranking과 unbound concentration 기준 ranking이 달라질 수 있는 이유는?

**Answer**: 단백 결합이 다르면 total concentration이 같아도 pharmacologically available unbound concentration이 달라진다. §2.9의 메시지는 total concentration보다 unbound systemic exposure가 더 직접적인 비교 기준이 될 수 있다는 것이다. [G p.163]

<!-- SELF-TEST -->
## Q9. Boss Dilemma: 회사 SOP는 표준 Eq.2:337만 허용하지만, half-life가 input time에 비해 매우 짧아 §2.8.8 대안식이 더 타당해 보인다. 어떻게 처리할 것인가?

**Answer**: 표준식과 §2.8.8 대안식을 모두 계산해 차이를 제시하고, 차이의 원인이 $T_{inf}/t_{1/2}$ 비율에 있음을 설명한다. SOP deviation은 “더 예쁜 결과”가 아니라 zero/negative $V_{ss}$를 피하는 source-based mathematical justification으로 문서화한다. [G pp.151, 157]

<!-- RECAP -->
**§7 Recap**: Q1–Q3은 AUC 신뢰도, Q4는 nonlinear 전환, Q5–Q6은 NCA 계산, Q7–Q8은 exposure 해석, Q9는 C3 Apex의 적용 경계다.

---

# §8 — Meta-Frame & Big Picture

## A. Positioning

NCA는 PopPK의 대체물이 아니라 전후방 도구다. 모델 선택 전에는 EDA와 initial estimate를 만들고, 모델 추정 후에는 population prediction이 관측 exposure의 규모와 일관되는지 확인하는 기준점이 된다. 단, NCA가 linear elimination을 가정한다는 점을 잊으면 “단순해서 강한 방법”이 “단순해서 틀린 방법”으로 바뀐다. [G p.141]

## B. Failure modes to track

1. **Terminal slope contamination**: distribution phase point가 $\lambda_z$에 포함되면 AUC tail, CL, $V_z$가 함께 흔들린다. [G pp.146–148]
2. **Input correction omission**: infusion/oral input time을 빼지 않으면 MRT와 $V_{ss}$가 실제 residence/distribution보다 길거나 짧게 해석될 수 있다. [G pp.149–151; T p.793]
3. **Nonlinear CL masquerading as NCA CL**: dose 증가에 따라 CL이 단조 감소하면, CL을 dose별 final parameter처럼 해석하지 말고 capacity-limited model로 전환해야 한다. [G pp.661–664]
4. **NCA-IIV overuse**: NCA-derived variability는 PopPK IIV의 직접 추정값이 아니라 residual variability까지 섞인 상한으로 다루는 것이 안전하다. `[실무 추론]`

## C. Professional moat

- **보고서 검토의 시작점**: AUC table보다 먼저 $\lambda_z$ selection plot, %extrapolated, $C_{last}$ 처리 기준을 본다.
- **MRT/$V_{ss}$ 검토의 시작점**: $AUMC$ tail과 MIT correction을 확인한다.
- **비선형 전환의 시작점**: dose escalation NCA-CL이 dose와 함께 변하는지 본다. PK41은 CL 감소가 Michaelis-Menten regression으로 이어지는 textbook anchor다. [G pp.661–664]
- **Exposure 해석의 시작점**: dose가 아니라 systemic/unbound concentration, AUC, $C_{max}$, $t_d$ 중 어느 metric이 response mechanism에 맞는지 먼저 정한다. [G pp.158–164]

## D. Final compressed doctrine

<!-- MASTER LENS -->
NCA의 본질은 “모델을 쓰지 않는다”가 아니라 “최소한의 선형 소실 가정으로 면적과 시간 모멘트를 요약한다”이다. AUC는 exposure의 출발점, AUMC는 residence time의 출발점, MRT는 $V_{ss}$의 출발점, PK41은 이 모든 것이 nonlinear kinetics 앞에서 initial estimate로 격하되는 순간을 보여준다.

<!-- RECAP -->
**§8 Recap**: 30년 pharmacometrics 연구자가 10분 handout에 남길 메시지는 하나다. NCA output table을 믿기 전에 terminal slope, extrapolated fraction, input correction, dose-dependence, exposure metric 선택을 순서대로 점검하라.

---

## Content Lock v1 적용 로그

- Unsupported numeric rules 삭제: `λz 오류 30–50%`, `AUMC tail 30–60%`, `6–12개월 지연`.
- Source-outside regulatory claims 삭제/경계 처리: FDA 21 CFR 320, 90% CI 80–125%, Clinical Hold, Deficiency Letter, IR.
- R&T Table A-1/Zileuton 오류 수정: Table A-1은 generic oral 50 mg AUC=26.60, Zileuton은 Table A-2.
- λz half-life 조건 수정: 2–4 → 3–4 half-lives.
- Terminal $C_{last}$ wording 수정: “아래로 떨어지면” → “terminal regression line에서 벗어나면”.
- PK41 dynamic source anchor 삽입: design, NCA results, initial estimates, final MM estimates, author conclusion.
- Crucible Grade A 통합: flip-flop silent failure, AUMC $\lambda_z$ sensitivity, Holford/CL interpretability, dual $V_{ss}$ check, NCA-IIV upper-bound warning.
- Crucible Grade C 거부: NONMEM code, TMDD/PBPK, BA/BE numeric rule, PK/PD killing 확장, ICH E1/M3, $V_z\ge V_{ss}$ always.

# 06_Content Lock v1 — NCA·노출 평가·MRT·비구획 실무

**산출 단계**: Phase 4A — Editorial Adjudication + Compression Pass  
**입력**: Original PDFs + Step 1 Draft v0 + Source Fidelity Audit Report v1 + Insight Crucible Report v1  
**출력 범위**: §1 → §2 → §5 → §7 → §8  
**언어 원칙**: Korean prose; English for technical terms, equations, NONMEM/software terms, drug names.  
**Figure note**: Audit T6 Figure Inventory는 본 단계에서 판정하지 않고 Phase 4C로 이월.

---

## 0. Updated Curation Map

### MUST-tier

| Card | Concept | Verdict after 4A | Why it stays |
|---|---|---|---|
| **C1** | AUC 계산: linear/log-linear trapezoidal rule, $\lambda_z$, extrapolation | **MUST 유지** | 모든 NCA-derived parameter의 분모가 $AUC_0^\infty$이며, $\lambda_z$ 선택 오류가 CL, MRT, $V_{ss}$, $V_z$로 전파된다. [G pp.141–148; T pp.759–762] |
| **C2** | AUMC + MRT: first moment, residence time, input correction | **MUST 유지** | MRT는 단순 half-life가 아니라 molecule residence의 평균이며, $AUMC/AUC$와 mean input time 보정이 핵심이다. [G pp.144–151; T pp.789–793] |
| **C3** | CL, $V_{ss}$, $V_z$, 투여경로 보정, 짧은 half-life/input-time 대안 공식 | **Apex 유지** | 표준 공식과 §2.8.8 대안 공식의 적용 영역을 구분하지 못하면 0 또는 음수 $V_{ss}$가 발생한다. [G pp.149–157] |
| **C4** | Exposure metrics: $C_{ss}$, $C_{max}$, AUC, $t_d$ | **MUST 유지** | §2.9의 핵심은 dose가 아니라 systemic exposure, 특히 total/unbound concentration을 보는 것이다. [G pp.158–164] |
| **PK41 anchor** | Turbojoint NCA → nonlinear regression transition | **MUST로 승격** | Draft v0에서 §6로 밀렸으나 현재 산출물에 §6이 없으므로, 본문 안에 compact source anchor로 포함해야 한다. [G pp.661–664] |

### CONTEXT-tier

| Context item | Final placement |
|---|---|
| NCA vs nonlinear regression의 상보성 | §1 master lens + C1 opening에 1문장 통합. [G p.141] |
| Steady-state NCA: $AUC_{0-\tau,ss}=AUC_{0-\infty}$ | C1 boundary note로 압축. [G p.152] |
| BLQ/LOQ 처리 | C1 assumptions에 1문장 유지. [G p.153] |
| Metabolite residence time: $MDRT(i)=MBRT(i)-MIT$ | C2 context note로 압축. [G pp.155–156] |
| R&T Table A-1 / Table A-2 | Table A-1은 generic oral 50 mg AUC=26.60 예시, Table A-2는 zileuton 600 mg PO dataset으로 정정. [T pp.759–762] |
| R&T urinary MRT | MRT가 plasma-only 개념으로 보이지 않도록 C2에 1문장 추가. [T p.790] |
| Exposure case examples | C4에 압축; repeated-feeding rat safety case도 1문장 포함. [G pp.159–163] |
| Software/NONMEM implications | §8에만 `[실무 확장]` 또는 `[교과서 외 해석]`으로 제한. |

### DELETE / DOWNGRADE

| Item | Final action |
|---|---|
| $\lambda_z$ 오류가 AUC를 “30–50%” 왜곡한다는 수치 | **삭제**; PDF 근거 없음. 정성 표현으로 대체. |
| AUMC 외삽 “30–60%” 일반 규칙 | **삭제**; tail-sensitive로 완화. |
| BA/BE 90% CI 80–125%, FDA 21 CFR 320, Clinical Hold, Deficiency Letter, IR | **source-anchored 본문에서 삭제**; 필요 시 후속 외부 규제 연결로만 표기. |
| ICH E1/M3 | **삭제**; PDF 내 언급은 ICH S3A and 7A. |
| $V_z \ge V_{ss}$ “always” | **삭제 또는 `[일반 PK sanity check]`로만 제한**; 본문 source fact로 사용하지 않음. |
| PK/PD concentration-dependent vs time-dependent killing 확장 | **삭제**; 후속 PK/PD 세션 범위. |
| 물리학·경제학·환경독성학 비유 | **삭제**; 10분 handout에서 핵심 학습 기여 낮음. |

---

## 0.1 Adjudication Table Summary

| Source | Item | Verdict | Rationale |
|---|---|---|---|
| Audit T1 | “NCA는 model-free가 아니라 compartment-free” | **PARTIAL_ADOPT** | 원문은 specific compartmental model 불필요 + linear elimination 가정이므로, “model-free가 아니다”는 `[해석]`으로 유지. |
| Audit T1 | Nonlinear PK에서 NCA output은 초기 모수 입력으로 전환 | **PARTIAL_ADOPT** | PK41에 근거가 있으나 모든 nonlinear situation으로 일반화하지 않고 “PK41처럼”으로 제한. |
| Audit T1 | $\lambda_z$ 오류 30–50% | **REJECT** | PDF 직접 근거 없는 수치. |
| Audit T1 | BA/BE 90% CI 80–125% | **REJECT** | 지정 PDF 밖의 규제 기준. |
| Audit T1 | Linear trapezoidal AUC Eq.2:310 | **ADOPT** | 핵심 수식. |
| Audit T1 | Linear trapezoid bias | **ADOPT** | Fig 2.115와 일치. |
| Audit T1 | Log-linear trapezoid Eq.2:316 | **ADOPT** | Gabrielsson/R&T 모두 근거. |
| Audit T1 | Log-linear 조건 및 fallback | **ADOPT** | descending only, zero/equal 농도에서는 linear fallback. |
| Audit T1 | “혼합 적용 = 실무 표준” | **PARTIAL_ADOPT** | 원문 강도에 맞춰 “사용 가능/흔히 사용”으로 완화. |
| Audit T1 | $AUC_{tlast\to\infty}=C_{last}/\lambda_z$ | **ADOPT** | 핵심 외삽 수식. |
| Audit T1 | predicted vs observed $C_{last}$ | **ADOPT** | “항상” 대신 “일반적으로 권장”으로 완화. |
| Audit T1 | % extrapolated와 20–25% 기준 | **ADOPT** | Gabrielsson 권고와 일치. |
| Audit T1 | $\lambda_z$ 최소 관측점 3–4개 | **ADOPT** | 유지. |
| Audit T1 | “2–4 half-lives” | **ADOPT correction** | “3–4 half-lives”로 정정. |
| Audit T1 | 마지막 관측치가 회귀선 “아래”이면 제외 | **ADOPT correction** | 방향 제한 삭제; terminal regression line에서 벗어나는 경우로 수정. |
| Audit T1 | BLQ/LOQ 처리 | **ADOPT** | missing 처리로 유지. |
| Audit T1 | AUMC trapezoid/extrapolation | **ADOPT** | Eq.2:312/2:313/2:320 및 R&T H와 일치. |
| Audit T1 | AUMC 외삽 30–60% | **REJECT** | PDF 근거 없는 일반 수치. |
| Audit T1 | R&T H-1 molecule/MRT intuition | **ADOPT** | 1 mg, MW 300 g/mol, 약 $2\times10^{18}$ molecules 직관 유지. |
| Audit T1 | MRT plasma/infusion/oral correction | **ADOPT** | Eq.H-8, Eq.2:328/329와 일치. |
| Audit T1 | MAT/$K_a$ caveat | **PARTIAL_ADOPT** | oral absorption 맥락에서 1문장만 추가. |
| Audit T1 | Metabolite MDRT/MBRT/MIT | **ADOPT compressed** | C2 context로 압축. |
| Audit T1 | CL, $CL_o$, F, $V_{ss}$, $V_z$ 수식 | **ADOPT** | 핵심 NCA-derived parameter. |
| Audit T1 | $V_z\ge V_{ss}$ always | **REJECT as source fact** | PDF 직접 근거 없음; 보편 단언 삭제. |
| Audit T1 | Effective half-life $=\ln(2)\cdot MRT$ | **ADOPT** | C2/C3에 context로 유지. |
| Audit T1 | Steady-state AUC equivalence | **ADOPT compressed** | C1에 1문장 유지. |
| Audit T1 | §2.8.8 대안 공식 Eq.2:366/367 | **ADOPT** | Apex card의 핵심. |
| Audit T1 | 가상 $t_{1/2}\approx0.5h$, $V_{ss}=-0.4$ | **PARTIAL_ADOPT** | 교육용 가상 시나리오로만 표기하거나 본문에서 삭제. |
| Audit T1 | PK41 design/NCA/final estimates | **ADOPT** | compact source anchor로 본문 삽입. |
| Audit T1 | R&T Table A-1 “zileuton” | **ADOPT correction** | Table A-1 generic 50 mg, Table A-2 zileuton 600 mg으로 분리. |
| Audit T1 | R&T IV bolus $AUC=C(0)/k$ | **REJECT for body** | 유용하나 10분 handout에서는 optional. |
| Audit T1 | ICH S3A·E1·M3 | **ADOPT correction** | PDF 기준 ICH S3A and 7A로 제한. |
| Audit T1 | $C_u=C_{total}\cdot f_u$ | **PARTIAL_ADOPT** | PDF 수식으로 제시하지 않고 `[정의 보충]`으로 유지. |
| Audit T1 | NONMEM/Phoenix/PKNCA/FOCE/η-shrinkage | **PARTIAL_ADOPT** | §8 `[실무 확장]`으로만 유지; 교과서 사실처럼 쓰지 않음. |
| Audit T2/T5 | Fig 2.132 repeated-feeding rat safety case 누락 | **ADOPT compressed** | C4 context에 1문장 삽입. |
| Audit T3 | Holford: AUC vs CL/CL/F 메시지 | **ADOPT** | 보고 순서와 해석성에 핵심. |
| Audit T4 | Required Patch List 1–9 | **ADOPT** | 전부 본문에 반영. |
| Crucible T1 벽 1 | flip-flop kinetics 함정 | **PARTIAL_ADOPT** | 교과서 직접 예시는 아니므로 C3 limitation에 `[실무 해석]` 1문장으로 압축. |
| Crucible T1 벽 2 | AUMC tail의 $\lambda_z$ 민감도 | **ADOPT** | 수식 구조로 grounded; C2에 통합. |
| Crucible T1 벽 3 | Holford 메시지의 보고 함의 | **ADOPT** | Audit SHOULD_FIX와 일치. |
| Crucible T1-b | 4 cards as Phase 1 EDA serial workflow | **ADOPT** | §1 roadmap와 §8 meta-frame에 반영. |
| Crucible T1-c1 | Dose escalation CL pattern | **PARTIAL_ADOPT** | PK41 기반 “단조 감소 → nonlinear elimination 의심”까지만 채택; autoinduction 등은 `[실무 확장]`. |
| Crucible T1-c2 | 두 $V_{ss}$ 공식 동시 비교 | **ADOPT** | §5 Pair 3 및 C3 trench tip에 통합. |
| Crucible T1-c3 | NCA-IIV not direct PopPK $\omega^2$ | **PARTIAL_ADOPT** | 교과서 외 실무 확장으로 §8에만 배치. |
| Crucible T2-a 위험 1 | PK41 type에서 CL/t1/2 reporting caveat | **ADOPT** | Gabrielsson p.664와 일치하므로 PK41 anchor에 통합. |
| Crucible T2-a 위험 2 | exposure metric 선정 정당화 | **PARTIAL_ADOPT** | reviewer 언급은 줄이고 C4에 “주 지표 선정 근거를 문서화”로 압축. |
| Crucible T2-b | NCA-IIV Inflation | **PARTIAL_ADOPT** | §8 `[실무 확장]`으로 유지; 수치 30–60%, 30–50%는 삭제. |
| Crucible T2-c | $V_{ss}$ 표준 vs 대안 공식의 혼동쌍 | **ADOPT** | §5 Pair 3 내부 분기로 명시. |
| Crucible T3 Tip A | Holford reporting order | **ADOPT** | C1/C4와 §8에 1문장 반영. |
| Crucible T3 Tip B | 두 $V_{ss}$ 공식 sanity check | **ADOPT** | C3 trench tip. |
| Crucible T3 Tip C | automated $\lambda_z$ validation | **PARTIAL_ADOPT** | software 이름 최소화, 시각 검증 원칙만 C1에 반영. |
| Crucible T3 Tip D | NCA-IIV upper bound | **PARTIAL_ADOPT** | §8 practical extension. |
| Crucible T4 | 14 deletion/compression candidates | **ADOPT** | 전부 삭제 또는 1문장 압축. |
| Crucible Grade C | NONMEM code, TMDD/PBPK, BA/BE 80–125, ICH E1/M3, $V_z\ge V_{ss}$ always | **REJECT** | scope creep 또는 PDF 근거 부족. |

---

# §1 — Session Header & Roadmap

**Source**: Gabrielsson & Weiner 5e, Ch.2 §2.8 Non-Compartmental Analysis [G pp.141–157], §2.9 How to Assess Exposure [G pp.158–164], Case Study PK41 [G pp.661–664]. Supplementary: Rowland & Tozer 5e Appendix A [T pp.759–762], Appendix H [T pp.789–793].

**Session title**: 비구획 분석(NCA) — AUC, AUMC, MRT, $V_{ss}$, 노출 지표, 그리고 nonlinear regression으로 넘어가는 순간

<!-- MASTER LENS -->
**Big Idea**: NCA는 특정 compartment model을 요구하지 않는 **compartment-free** 접근이지만, sampling compartment에서의 elimination이 linear라는 가정은 여전히 필요하다. 따라서 PK41 Turbojoint처럼 dose가 증가할수록 NCA-CL이 감소하는 순간, NCA 결과는 최종 해석값이 아니라 nonlinear regression의 **initial parameter estimate**로 역할이 바뀐다. [G p.141; G pp.661–664]

<!-- ANCHOR -->
**Roadmap**: 이 세션은 병렬 암기 목록이 아니라 Phase 1 SAD/MAD EDA의 직렬 workflow다. C1에서 $AUC$와 $\lambda_z$를 정하고, C2에서 $AUMC/MRT$를 계산하며, C3에서 $CL$, $V_{ss}$, $V_z$와 투여경로 보정을 점검하고, C4에서 어떤 exposure metric을 PD·safety endpoint와 연결할지 결정한다.

| Step | Question | Output |
|---|---|---|
| 1 | 면적을 어떻게 계산하고 어디까지 믿을 것인가? | $AUC_0^{\infty}$, $\lambda_z$, % extrapolated |
| 2 | 분자가 평균적으로 얼마나 머무는가? | $AUMC$, MRT, MIT correction |
| 3 | CL·분포 부피가 생리적으로 가능한가? | $CL$, $V_{ss}$, $V_z$, Eq.2:337 vs Eq.2:366 |
| 4 | dose 대신 무엇을 exposure로 삼을 것인가? | $C_{ss}$, $C_{max}$, AUC, $t_d$ |
| 5 | 선형 가정이 깨졌는가? | NCA → nonlinear regression transition, PK41 anchor |

<!-- RECAP -->
**Section recap**: NCA의 힘은 “모델을 안 쓴다”가 아니라 “모델을 정하기 전에도 면적과 시간 모멘트로 데이터의 방향을 볼 수 있다”는 점이다. 그러나 선형 소실, terminal slope, 투여경로 보정이 무너지면 NCA output은 자동 보고값이 아니라 진단 신호다.

---

# §2 — Concept Anatomy Cards

## C1. AUC 계산 — trapezoidal rule, $\lambda_z$, extrapolation

<!-- MASTER LENS -->
**Big Idea**: AUC는 관측 곡선 아래 면적이 아니라 **관측 구간의 numerical area + terminal slope로 외삽한 미래 면적**이다. 따라서 AUC의 신뢰도는 사다리꼴 계산보다 $\lambda_z$ 선택과 extrapolated fraction에서 더 크게 흔들릴 수 있다. [G pp.143–148]

### A. Formal definition

$AUC$는 plasma concentration–time curve의 zero moment area다. $AUC_0^{t_{last}}$는 관측값으로 계산하고, $AUC_{t_{last}\to\infty}$는 terminal phase가 mono-exponential로 감소한다는 가정으로 외삽한다. [G pp.142–143]

$$
AUC_{total}=AUC_0^{t_{last}}+AUC_{t_{last}\to\infty}
$$

### B. Core equations

Linear trapezoidal rule: [G p.143, Eq.2:310]

$$
AUC_0^{t_{last}}=\sum_i \frac{C_i+C_{i+1}}{2}\Delta t
$$

Log-linear trapezoidal rule for descending concentrations: [G p.145, Eq.2:316; T p.761, Eq.A-7]

$$
AUC_i=\frac{C_i-C_{i+1}}{\ln(C_i/C_{i+1})}\Delta t
$$

Terminal extrapolation: [G pp.143,145, Eq.2:311/2:319]

$$
AUC_{t_{last}\to\infty}=\frac{C_{last}}{\lambda_z}
$$

Fraction extrapolated: [G p.148, Eq.2:324]

$$
\%AUC_{extrapolated}=\frac{AUC_{t_{last}\to\infty}}{AUC_{total}}\times100
$$

Gabrielsson의 practical boundary는 $AUC_{t_{last}\to\infty}$가 일반적으로 total AUC의 20–25%를 넘지 않는 것이다. 초과하면 refined study 전의 preliminary estimate로만 다루는 것이 안전하다. [G p.148]

### C. Structural intuition

Linear trapezoid는 상승 구간에서 area를 underestimate하고, first-order decline 구간에서 area를 overestimate한다. Log-linear trapezoid는 하강 구간의 exponential decay를 더 잘 반영하지만, $C_i=0$ 또는 $C_{i+1}=C_i$이면 적용할 수 없으므로 linear fallback이 필요하다. Reasonable sampling design에서는 두 방법의 평균 AUC 차이가 임상적으로 크지 않을 수 있으므로, 방법 선택보다 sampling과 $\lambda_z$ 검증이 더 중요하다. [G pp.142–146]

### D. $\lambda_z$ selection rule

Terminal slope는 individual semi-log plot에서 육안으로 먼저 확인하고, 이상적으로 3–4 half-lives가 지나며 최소 3–4 terminal observations가 있어야 한다. 마지막 관측치가 terminal regression line에서 벗어나면 observed $C_{last}$ 대신 predicted $\hat C_{last}$를 사용하는 것이 일반적으로 권장된다. [G pp.146–147]

<!-- TRENCH -->
**Trench-Level Tip**: automated NCA output을 그대로 믿지 말고, $\lambda_z$ 회귀 구간과 % extrapolated를 먼저 본다. 특히 terminal phase에 distribution-phase point가 섞이면 AUC, CL, $V_z$, MRT가 모두 같은 방향으로 오염된다.

### E. Boundary notes

- BLQ/LOQ 이하 값은 zero나 LOQ로 치환하지 말고 missing으로 취급하는 것이 원문 권고다. [G p.153]
- 정상상태에서는 한 dosing interval의 $AUC_{0-\tau,ss}$가 단회투여 $AUC_0^\infty$와 동등해지는 조건이 있다. [G p.152]
- R&T Table A-1은 **zileuton이 아니라** oral 50 mg generic example이며 total AUC는 26.60 mg·hr/L이다. Zileuton 600 mg PO dataset은 Table A-2다. [T pp.759–762]

---

## C2. AUMC와 MRT — first moment와 평균 체류시간

<!-- MASTER LENS -->
**Big Idea**: MRT는 terminal half-life의 다른 이름이 아니다. MRT는 분자들이 체내에 머무른 시간의 평균이며, plasma data에서는 $AUMC/AUC$로 계산된다. AUMC는 time을 곱한 curve이므로 late tail에 더 민감하다. [G pp.142,144–145; T pp.789–792]

### A. Formal definition

AUC는 zero moment area이고 AUMC는 $C\times t$ curve의 first moment area다. Higher moments는 computational error가 커 일반적으로 PK analysis에서 사용하지 않는다. [G p.142]

R&T의 분자 직관: 1 mg, molecular weight 300 g/mol인 약물은 약 $2\times10^{18}$ molecules에 해당하며, MRT는 이 molecules의 residence time 평균으로 볼 수 있다. [T p.789]

### B. Core equations

Linear AUMC: [G p.144, Eq.2:312]

$$
AUMC_0^{t_{last}}=\sum_i \frac{t_iC_i+t_{i+1}C_{i+1}}{2}\Delta t
$$

AUMC tail: [G pp.144–145, Eq.2:313/2:320; T p.791, Eq.H-9]

$$
AUMC_{t_{last}\to\infty}=\frac{t_{last}C_{last}}{\lambda_z}+\frac{C_{last}}{\lambda_z^2}
$$

Plasma MRT: [T p.791, Eq.H-8]

$$
MRT=\frac{AUMC_0^\infty}{AUC_0^\infty}
$$

### C. Why AUMC is more fragile

<!-- ANCHOR -->
AUC tail has one dominant term, $C_{last}/\lambda_z$. AUMC tail has two terms, $t_{last}C_{last}/\lambda_z$ and $C_{last}/\lambda_z^2$. The second term makes MRT more sensitive to terminal-slope selection than AUC; this is the mathematical reason “MRT is unstable when the tail is poorly defined.” [G pp.144–145; T p.791]

### D. Input correction: observed residence vs disposition residence

For IV infusion: [G p.149, Eq.2:328]

$$
MRT_{iv}=\frac{AUMC_0^\infty}{AUC_0^\infty}-\frac{T_{inf}}{2}
$$

For first-order extravascular input: [G p.149, Eq.2:329]

$$
MRT_{ev}=\frac{AUMC_0^\infty}{AUC_0^\infty}-\frac{1}{K_a}
$$

Mean absorption/input time is not always a pure absorption constant; apparent $K_a$ can include parallel processes such as degradation, so oral MRT correction must be interpreted cautiously. [G p.150, Eq.2:330]

### E. Context extensions

- Urinary excretion data can also be used for MRT estimation, so MRT is not intrinsically plasma-only; plasma $AUMC/AUC$ is the most common implementation. [T p.790]
- Metabolite or downstream-compartment residence time can be expressed as a difference between body residence times, e.g., $MDRT(i)=MBRT(i)-MIT$. [G pp.155–156]
- Effective half-life can be expressed as $\ln(2)\cdot MRT$, but this does not mean MRT and terminal $t_{1/2}$ are interchangeable in multicompartment systems. [G p.151]

<!-- RECAP -->
**C2 recap**: AUC asks “how much exposure?”, AUMC asks “how late was that exposure?”, and MRT normalizes that late-weighted area by total exposure.

---

## C3. CL, $V_{ss}$, $V_z$, and input-time correction — Apex Card

<!-- MASTER LENS -->
**Big Idea**: $CL$, $V_{ss}$, and $V_z$ look like simple algebraic outputs, but they are only as valid as AUC, AUMC, $\lambda_z$, and input-time correction. The fatal error is treating $AUMC/AUC$ as disposition MRT when the observed curve still contains input time. [G pp.149–157]

### A. Core equations

Clearance after IV dosing: [G p.149, Eq.2:325]

$$
CL=\frac{D_{iv}}{AUC_0^\infty}
$$

Oral apparent clearance: [G p.149, Eq.2:326]

$$
CL_o=\frac{CL}{F}=\frac{D_{po}}{AUC_0^\infty}
$$

Bioavailability: [G p.149, Eq.2:327]

$$
F=\frac{AUC_{po}}{AUC_{iv}}\cdot\frac{D_{iv}}{D_{po}}
$$

Steady-state volume: [G p.151, Eq.2:337]

$$
V_{ss}=MRT\cdot CL=\frac{D_{iv}\cdot AUMC_0^\infty}{(AUC_0^\infty)^2}
$$

Terminal volume: [G p.151, Eq.2:338]

$$
V_z=\frac{CL}{\lambda_z}=\frac{D_{iv}}{AUC_0^\infty\lambda_z}
$$

### B. Structural meaning

$V_{ss}$ is governed by total body amount at steady state relative to steady-state concentration; it is an equilibrium distribution parameter. $V_z$ is governed by the terminal slope and is therefore a terminal-phase parameter. Confusing the two is a category error: one summarizes steady-state distribution, the other summarizes the apparent volume implied by the final log-linear decline. [G p.151]

### C. Short half-life relative to input time: §2.8.8 alternative

When half-life is short relative to input time, the standard equations can yield zero or negative $V_{ss}$ because the input-time subtraction dominates the observed $AUMC/AUC$. Gabrielsson provides a more robust washout-based formulation. [G p.157]

Starting identities: [G p.157, Eq.2:363–2:365]

$$
A_{ss}=V_{ss}C_{ss}, \qquad A_{ss}=CL\cdot AUC_{t^*\to\infty}, \qquad CL=\frac{K^0}{C_{ss}}
$$

Alternative steady-state volume: [G p.157, Eq.2:366]

$$
V_{ss}=\frac{K^0\cdot AUC_{t^*\to\infty}}{C_{ss}^2}
$$

Alternative MRT: [G p.157, Eq.2:367]

$$
MRT=\frac{AUC_{t^*\to\infty}}{C_{ss}}
$$

<!-- TRENCH -->
**Trench-Level Tip**: 표준 공식 Eq.2:337과 §2.8.8 대안 Eq.2:366을 함께 계산해 본다. 두 값이 크게 다르면 그것은 단순 계산 차이가 아니라 $T_{inf}/t_{1/2}$ 영역 문제를 알려주는 적용-영역 진단 신호다.

### D. Limitations

- $V_{ss}$ is not directly estimable after oral dosing unless bioavailability and input-time issues are resolved; otherwise the output is apparent and input-confounded.
- $V_z$ must not be used to describe distribution during the distribution phase.
- In capacity-limited kinetics, $CL$ and $t_{1/2}$ are first-order parameters and become incompatible with mixed zero-/first-order behavior; PK41 is the worked example. [G p.664]
- `[실무 해석]` Flip-flop kinetics can be dangerous because the NCA output may look numerically plausible while absorption, not elimination, is driving the terminal slope.

---

## C4. Exposure metrics — from dose to concentration

<!-- MASTER LENS -->
**Big Idea**: Exposure assessment asks what concentration-time feature best explains efficacy or toxicity. Dose is only the administered input; systemic exposure is the concentration history that the body or target sees. [G pp.158–163]

### A. Exposure concepts

Gabrielsson frames exposure in terms of total or unbound systemic plasma concentration, and sometimes tissue concentration, rather than administered dose alone. [G p.158]

| Metric | Definition | Typical use |
|---|---|---|
| $C_{ss}$ | steady-state average concentration | chronic dosing, TDM, maintenance exposure |
| $C_{max}$ | highest observed concentration | peak-related toxicity or rapid response |
| AUC or $n\cdot AUC$ | cumulative exposure | cumulative toxicity, carcinogenicity, broad systemic burden |
| $t_d$ or AUC above threshold | time or area above a target threshold | threshold-driven efficacy/toxicity |

### B. Total vs unbound exposure

`[정의 보충]`

$$
C_u=C_{total}\cdot f_u
$$

If protein binding differs across compounds or conditions, total concentration can misrank potency, while unbound concentration may better align with pharmacologic effect. [G p.163]

### C. Exposure case compression

§2.9 examples show why concentration can outperform dose: route and bioavailability can distort dose-response, nonlinear elimination can distort safety margins, active metabolites can drive apparent effects, dosing mode can alter toxicity despite similar total daily dose, repeated-feeding safety studies can require simulation rather than naive single-dose extrapolation, and U-shaped concentration-response can make “more dose” an invalid intuition. [G pp.159–163]

### D. Metric selection principle

Choose the primary exposure metric by the endpoint’s causal time scale: peak-driven effects use $C_{max}$, cumulative burden uses AUC, threshold effects use $t_d$ or AUC above threshold, and chronic steady-state response uses $C_{ss}$. The choice should be documented as a scientific rationale, not left as a software-default table order. [G p.163]

<!-- TRENCH -->
**Trench-Level Tip**: Holford’s message is a reporting-order rule: $CL$ or $CL/F$ carries physiologic interpretability and covariate meaning, while AUC is most useful as an exposure/toxicology metric or when dose is unknown. [G pp.148–149]

---

## PK41 Dynamic Source Anchor — NCA가 regression 입력으로 바뀌는 순간

<!-- ANCHOR -->
**Case**: One volunteer received three randomized 5 h IV infusions of Turbojoint: 310, 520, and 780 µg·kg⁻¹, assuming body weight 70 kg. [G p.661]

**NCA signal**: As dose increased from 310 to 780 µg·kg⁻¹, NCA clearance decreased from 1.6 to 0.9 L·h⁻¹·kg⁻¹, volume decreased from 2.3 to 1.8 L·kg⁻¹, and MRT increased from 1.4 to 1.9 h. This is the practical alarm: clearance is dose-dependent. [G p.662]

**Regression model**: [G p.663, Eq.41:1–2]

$$
V\frac{dC}{dt}=In-Cl\cdot C, \qquad Cl=\frac{V_{max}}{K_m+C}
$$

**Initial estimates**: NCA gave $V\approx2$ L·kg⁻¹; using NCA clearance values and peak concentrations gave $K_m\approx150$ µg·L⁻¹ and $V_{max}\approx310$ µg·h⁻¹·kg⁻¹. The fitted model used initial values $V_{max}=200$ µg·h⁻¹·kg⁻¹ and $K_m=100$ µg·L⁻¹ to challenge the program. [G pp.663–664]

**Final estimates**: $V_{max}=184$ µg·h⁻¹·kg⁻¹, $K_m=83$ µg·L⁻¹, $V=1.8$ L·kg⁻¹. The author’s key message is that capacity-limited one-compartment kinetics are parameterized by $V_{max}$, $K_m$, and $V$, not by fixed $CL$ and $t_{1/2}$. [G p.664]

<!-- RECAP -->
**§2 recap**: C1–C4 are not four independent topics. AUC quality controls CL; AUMC controls MRT; MRT and CL control $V_{ss}$; and exposure metrics decide how the PK output becomes an efficacy or safety argument. PK41 shows the boundary where NCA stops being the answer and becomes the starting point for regression.

---

# §5 — Confusion Pair Dissection

<!-- CONFUSION -->
## Pair 1. Linear vs log-linear trapezoidal rule

| Dimension | Linear trapezoid | Log-linear trapezoid |
|---|---|---|
| Assumption | concentration changes linearly between two observations | concentration declines exponentially between two observations |
| Best use | rising/equal concentrations; zero-order decline | descending first-order region |
| Failure mode | descending first-order phase overestimation | cannot handle $C_i=0$ or $C_{i+1}=C_i$ |
| Memory hook | “straight line between concentrations” | “straight line after log transform” |

**Critical distinction**: The choice is not about which method is universally superior. With reasonable sampling design, differences may be small; the larger risk is using an unsupported $\lambda_z$ for the terminal extrapolation. [G pp.144–146]

---

<!-- CONFUSION -->
## Pair 2. MRT vs terminal half-life

| Dimension | MRT | Terminal $t_{1/2,z}$ |
|---|---|---|
| Definition | $AUMC/AUC$ after input correction | $\ln(2)/\lambda_z$ |
| What it summarizes | average residence time of molecules | time for terminal phase concentration to halve |
| Sensitive to | AUMC tail, input route, distribution history | terminal slope only |
| Misuse | using observed $AUMC/AUC$ as disposition MRT without MIT correction | using terminal half-life as if it captured full distribution history |

**Critical distinction**: In a one-compartment exponential decline, MRT and half-life are tightly related; in multicompartment or input-confounded data, MRT absorbs more of the time history while terminal half-life only sees the final slope. [G pp.149–151; T pp.789–793]

---

<!-- CONFUSION -->
## Pair 3. $V_{ss}$ vs $V_z$ — and the two $V_{ss}$ formulas

| Dimension | $V_{ss}$ | $V_z$ |
|---|---|---|
| Main equation | $V_{ss}=MRT\cdot CL$ | $V_z=CL/\lambda_z$ |
| Core meaning | steady-state distribution volume | terminal-slope-implied apparent volume |
| Main risk | input-time correction missing → impossible or misleading $V_{ss}$ | terminal slope misidentified → misleading $V_z$ |
| Source anchor | Eq.2:337 / Eq.2:366 | Eq.2:338 |

**Internal sub-pair**: $V_{ss}$ by standard Eq.2:337 and $V_{ss}$ by §2.8.8 Eq.2:366 have the same name but different valid-use territory. When $t_{1/2}$ is short relative to infusion/input time, Eq.2:366 is the safer formula because it uses steady-state washout area and avoids zero/negative $V_{ss}$. [G p.157]

---

<!-- CONFUSION -->
## Pair 4. Dose vs exposure

Dose is what is administered; exposure is what the organism or target experiences over time. §2.9 shows repeated cases where dose-response is misleading and concentration-response clarifies the mechanism. The practical question is therefore not “what dose was given?” but “which concentration-time summary is causally linked to the endpoint?” [G pp.158–163]

<!-- RECAP -->
**§5 recap**: Most NCA mistakes are not arithmetic errors. They are category errors: linear vs exponential interpolation, residence time vs half-life, steady-state volume vs terminal volume, and dose vs exposure.

---

# §7 — Self-Test

<!-- SELF-TEST -->
## Q1. Linear/log-linear rule

A profile rises to $C_{max}$ and then declines mono-exponentially. Which rule should be used for increasing/equal segments and which for decreasing segments?

**Answer**: Increasing/equal segments: linear trapezoid. Decreasing segments: log-linear trapezoid, unless zero/equal concentrations make log-linear invalid. [G pp.144–146]

---

<!-- SELF-TEST -->
## Q2. $\lambda_z$ validity

A terminal regression uses only two points, and the extrapolated AUC fraction is 35%. Is this final-report ready?

**Answer**: No. Gabrielsson recommends individual semi-log inspection, ideally 3–4 half-lives with minimum 3–4 terminal observations; extrapolated area should generally not exceed 20–25% unless preliminary. [G pp.146–148]

---

<!-- SELF-TEST -->
## Q3. AUMC tail

Why can MRT be more unstable than AUC when the terminal slope is uncertain?

**Answer**: AUC tail is $C_{last}/\lambda_z$, whereas AUMC tail includes $t_{last}C_{last}/\lambda_z + C_{last}/\lambda_z^2$. The first moment weights late time, so terminal-slope uncertainty is amplified. [G pp.144–145; T p.791]

---

<!-- SELF-TEST -->
## Q4. Infusion MRT correction

For constant-rate IV infusion, why is $T_{inf}/2$ subtracted from $AUMC/AUC$?

**Answer**: Observed $AUMC/AUC$ includes both input time and disposition residence time. For constant-rate infusion, mean input time is $T_{inf}/2$, so disposition MRT is $AUMC/AUC-T_{inf}/2$. [G p.149]

---

<!-- SELF-TEST -->
## Q5. Negative or zero $V_{ss}$

When can the standard $V_{ss}=MRT\cdot CL$ formula produce zero or negative values, and what is the source-based remedy?

**Answer**: When half-life is short relative to input time, the input-time correction can dominate the observed $AUMC/AUC$. Gabrielsson §2.8.8 uses washout-based equations: $V_{ss}=K^0AUC_{t^*\to\infty}/C_{ss}^2$ and $MRT=AUC_{t^*\to\infty}/C_{ss}$. [G p.157]

---

<!-- SELF-TEST -->
## Q6. PK41 transition

In PK41, dose increased from 310 to 780 µg·kg⁻¹ and NCA-CL decreased from 1.6 to 0.9 L·h⁻¹·kg⁻¹. What should the analyst do next?

**Answer**: Treat NCA as the source of initial parameter estimates, not as the final linear-CL interpretation. PK41 moves to a capacity-limited model with $V_{max}$, $K_m$, and $V$. [G pp.661–664]

---

<!-- SELF-TEST -->
## Q7. Exposure metric selection

Match the metric to the causal question: chronic steady-state response, peak toxicity, cumulative toxicity, threshold-driven antimicrobial activity.

**Answer**: chronic steady-state response → $C_{ss}$; peak toxicity → $C_{max}$; cumulative toxicity → AUC or $n\cdot AUC$; threshold-driven effect → $t_d$ or AUC above threshold. [G p.163]

---

<!-- SELF-TEST -->
## Q8. Table A-1 vs zileuton

Which R&T table gives total AUC=26.60 mg·hr/L after oral 50 mg, and which table contains the zileuton 600 mg PO dataset?

**Answer**: Table A-1 is the generic oral 50 mg AUC example with total AUC=26.60 mg·hr/L. Table A-2 is the zileuton 600 mg PO concentration-time dataset. [T pp.759–762]

<!-- RECAP -->
**§7 recap**: A correct NCA answer must state not only the equation, but also the validity conditions: interpolation rule, terminal slope quality, extrapolated fraction, input correction, and whether linear clearance is still meaningful.

---

# §8 — Meta-Frame & Big Picture

<!-- MASTER LENS -->
## 8.1 The chapter in one workflow

NCA is the first-pass diagnostic layer before model-based analysis and the sanity-check layer after model fitting. It begins with areas, converts areas into exposure and residence summaries, and then asks whether the implied CL and volumes are still compatible with the assumptions. If not, as in PK41, NCA hands the analysis over to regression modeling. [G p.141; G pp.661–664]

## 8.2 Failure modes that survive compression

### Failure Mode 1 — terminal slope contamination

Distribution-phase points are included in terminal regression → $\lambda_z$ is biased → AUC tail, AUMC tail, $CL$, $V_z$, MRT, and $V_{ss}$ all shift. The fix is not a more decorative table; it is individual semi-log inspection and explicit reporting of terminal points and % extrapolated. [G pp.146–148]

### Failure Mode 2 — input time mistaken for residence time

Observed $AUMC/AUC$ is reported as MRT after infusion or oral dosing without subtracting mean input time. This can distort $V_{ss}$ and, in short half-life/input-time settings, can produce zero or negative values under the standard formula. [G pp.149–157]

### Failure Mode 3 — NCA-CL reported as if linear when clearance is dose-dependent

PK41 shows the source-based transition rule: dose-dependent NCA-CL is a signal for nonlinear elimination. In that setting, fixed $CL$ and $t_{1/2}$ are incompatible with mixed zero-/first-order kinetics; model parameters become $V_{max}$, $K_m$, and $V$. [G p.664]

### Failure Mode 4 — exposure metric chosen by software order

If $C_{max}$, AUC, $C_{ss}$, and $t_d$ are reported without endpoint rationale, the analysis loses its causal connection. Metric selection must follow the biology of the endpoint: peak, cumulative, steady-state, or threshold. [G p.163]

### Failure Mode 5 — NCA variability treated as PopPK IIV

`[교과서 외 실무 확장]` NCA between-subject variability includes true IIV plus residual and design noise. Use it as a rough upper bound or diagnostic starting point, not as a literal NONMEM $\omega^2$ estimate. This is a practical modeling caution, not a Gabrielsson/R&T source claim.

## 8.3 Professional Moat

A junior analyst reports the NCA table. A mature pharmacometrician asks five additional questions before believing it:

1. Was $\lambda_z$ visually selected from a credible terminal phase?
2. How much of AUC and AUMC is extrapolated?
3. Did the observed residence time include input time?
4. Do standard and §2.8.8 $V_{ss}$ formulas agree in the relevant setting?
5. Does dose escalation show clearance changing with dose?

<!-- RECAP -->
**Final recap**: The operational mastery of NCA is not memorizing $AUC$, $AUMC$, MRT, $CL$, $V_{ss}$, and $V_z$ equations. It is knowing when those equations still describe linear disposition, when they merely provide preliminary estimates, and when they are signaling that a nonlinear regression model is now mandatory.

---

## 8.4 Phase 4A compression log

| Compression rule | Applied action |
|---|---|
| C1: CONTEXT item in 2+ sentences → 1 sentence | steady-state NCA, metabolite NCA, urinary MRT, exposure examples compressed. |
| C2: duplicate content | AUC/extrapolation material kept in C1 only; PK41 details centralized in one anchor. |
| C3: generic Big Idea | replaced with source-bound “compartment-free but linear-elimination-assuming” framing. |
| C4: Grade-A deletion candidates | unsupported numeric rules and external regulatory claims removed. |
| C5: length ≤ Draft v0 | Content Lock v1 is compressed relative to the Draft v0 structure. |
| C6: page tags preserved | MUST equations, examples, PK41 anchor, and R&T examples retain page tags. |


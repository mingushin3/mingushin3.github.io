# 06_HTML Compile Input Master

## Phase 4D Certification

| Certificate | Status | Basis |
|---|---|---|
| Learner-Standalone Certificate | PASS | PART A는 Learner Navigation Aid와 §1–§8 학습 본문만 포함하며, compiler/audit/process log는 PART B로 분리했다. |
| Zero-Omission Certificate | PASS | Scope Lock의 C1–C4, PK41, R&T A/H anchors, Audit MUST/SHOULD corrections, 4C KEEP markers를 모두 반영했다. |
| Mastery-Uplift Certificate | PASS | 8개 이하의 bounded augmentation을 관련 concept 옆에 source-status label과 함께 삽입했다. |
| Source-Boundary Certificate | PASS | 모든 augmentation은 TEXTBOOK_DERIVED/AUDIT_DERIVED/CRUCIBLE_DERIVED/EXPERT_INFERENCE로 표기했고, 새 수치·새 page tag·새 named example을 추가하지 않았다. |
| HTML-Readiness Certificate | PASS | PART B에 marker mapping, figure/page-tag/navigation/MathJax/self-test/rendering/guardrail 규칙을 포함했다. |

## Assembly Mode

PATCH MODE — `06_Content Lock v2.1(3).md` is a Figure Marker Patch Plan / Insertion Map, not a full re-emitted learner body. PART A was constructed from `06_Content Lock v2(6).md` §1–§8 by exact insertion of approved 4C figure markers, followed by bounded Mastery Augmentation Layer additions.

## Input Manifest

| File | Role | Authority level | Used for | Notes |
|---|---|---|---|---|
| `06_scope_lock(6).md` | scope boundary | A0 | source range, learner, mode, required anchors, image rights | Image rights=None; A-Critical. |
| `06_G_NCA·노출 평가 MRT·비구획 실무(7).pdf` | PDF verification source | A1 | Gabrielsson Ch.2 §2.8–§2.9, PK41 page/figure/data verification | Used only for high-impact fidelity checks and source identity. |
| `06_T_NCA·노출 평가 MRT·비구획 실무(7).pdf` | PDF verification source | A1 | Rowland & Tozer Appendix A/H numerical anchor verification | Used only for AUC/MRT source checks. |
| `06_Audit_Report_v1(5).md` | audit guardrail | A2 | MUST_FIX/SHOULD_FIX, forbidden restoration, page/figure/data correction | Controls regression prevention. |
| `06_Content Lock v2(6).md` | canonical body | A3 | base learner body from §1–§8 | Process logs excluded from PART A and summarized in PART B. |
| `06_Content Lock v2.1(3).md` | figure insertion source | A4 | PATCH MODE figure strategy, insertion anchors, marker blocks | All KEEP markers spliced exactly once. |
| `06_crucible_report_v1(3).md` | crucible guardrail | A5 | adopted/allowed Grade A logic, mastery note candidates | Not used as raw learner prose except labeled augmentation logic. |
| `S06_phase1_patch memo(3).md` | locked reference / deprecated draft guard | A6 adjunct | identifies Phase 1 risks and patch expectations | Used only to confirm already-resolved concerns. |
| `06_step1_draft_v0(3).md` | deprecated source | A6 | regression check only | Not copied into learner body. |
| `06_Content_Lock_v1(4).md` | locked reference | A3 predecessor | historical comparison only | Not used as learner-body source. |
| `붙여넣은 마크다운(2)(55).md` | compiler instruction | A7 | Phase 5 rendering, marker mapping, navigation anchor rules | Summarized in PART B. |
| `붙여넣은 텍스트 (1)(84).txt` | Phase 4D assembly instruction | task instruction | output structure, gates, certificates | Adapted to Session 06 filename. |

## PART A — Learner-Facing Complete Handout

## Learner Navigation Aid

**How to use this handout**: PART A만 읽어도 학습용 handout으로 사용할 수 있다. 먼저 §1의 직렬 workflow를 잡고, §2의 C1→C4를 순서대로 읽은 뒤, §5 혼동쌍과 §7 self-test로 회수한다.

**Learning route**: `C1 AUC/λz → C2 AUMC/MRT → C3 CL·Vss·Vz/Input correction → C4 Exposure metric selection → §5 Confusion pairs → §7 Active recall → §8 Professional lock`.

**Before you start**: CL/V 개념, 1·2 compartment model, Michaelis-Menten kinetics, $t_{1/2}=\ln(2)/k$를 떠올린다.

**After you finish**: NCA table을 볼 때 `terminal slope → %extrapolated → AUMC/MRT → input correction → CL/V → dose-dependence → exposure metric` 순서로 검토할 수 있어야 한다.

**Figure note**: `FIGURE_POINTER`는 저작권 있는 교과서 그림을 삽입하지 않고, 해당 원문 figure를 언제·왜 확인할지 알려주는 텍스트 callout이다. `FIGURE_SCHEMATIC`은 교과서 그림의 exact copy가 아니라 구조적으로 다른 redraw brief로만 사용한다.

# §1 — Session Header & Roadmap

**Session Title**: 비구획 분석(NCA) — AUC, AUMC, MRT, $V_{ss}$와 노출 평가의 실무 경계  
**Source**: Gabrielsson & Weiner 5e Ch.2 §2.8–§2.9, PK41; Rowland & Tozer 5e Appendix A·H. [G pp.141–164, pp.661–664; T pp.759–762, pp.789–793]

<!-- MASTER LENS -->
**Big Idea**: <!-- ANNOTATION --> NCA(← 특정 compartment model 없이 면적을 요약하는 분석)는 `[해석]` *model-free*라기보다 *compartment-free*에 가깝다. 특정 compartment model을 세우지 않아도 되지만, sampling compartment에서는 **linear elimination**(← 농도에 비례해 제거되는 소실) 가정이 여전히 필요하다. 따라서 PK41처럼 capacity-limited kinetics가 보이면 NCA 결과는 최종 해석값이 아니라 nonlinear regression의 **initial parameter anchor**로 내려와야 한다. [G p.141; G pp.661–664]

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

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.141, Fig 2.113
Why this matters: NCA가 area sums를 다루고 regression이 parameterized function을 fitting한다는 대비는 이 세션 전체의 프레임이다. 이 그림이 없으면 PK41에서 NCA가 왜 final answer가 아니라 regression 초기값으로 내려가는지 구조적 전환이 약해진다.
When to look: §1 Recap 직후, C1로 들어가기 전
Learner instruction: 왼쪽 panel에서 NCA가 각 구간 면적을 더하는 방식을 먼저 보라. 오른쪽 panel에서는 model parameters가 curve shape를 설명한다는 점만 확인하고, 아직 수식 세부로 들어가지 않는다.
<!-- /FIGURE_POINTER -->

> **Practice Lens — [EXPERT_INFERENCE]**  
> NCA output을 읽을 때는 표의 행 순서가 아니라 가정의 감사 순서로 읽는다. 즉, 먼저 terminal slope와 외삽 비율을 보고, 그 다음 MRT/input correction을 본 뒤, 마지막에 CL·volume·exposure metric을 해석한다.

---

# §2 — Concept Anatomy Cards

## C1. AUC 계산 — linear/log-linear trapezoidal rule, λz, extrapolation

<!-- MASTER LENS -->
### Big Idea

<!-- ANNOTATION -->
AUC는 “관측된 곡선 아래 면적” 하나가 아니다. **관측 구간의 사다리꼴 합 + terminal slope(← 말단 로그농도-시간 직선의 기울기)로 외삽한 미래 면적**이다. 따라서 NCA 신뢰도의 첫 질문은 “AUC가 얼마인가?”가 아니라 “관측 면적과 외삽 면적의 비율, 그리고 $\lambda_z$ 선택이 방어 가능한가?”이다. [G pp.142–148]

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

<!-- FIGURE_SCHEMATIC -->
Title: C1 AUC Audit Chain — trapezoid, method choice, λz, tail, downstream parameters
Mode: R
Visual objective: 5초 안에 “AUC 계산은 단일 공식이 아니라 quality-control chain”임을 보게 한다.
Core message: AUC 신뢰도는 사다리꼴 계산보다 terminal slope와 extrapolated tail 검증에서 결정되며, 그 오류는 CL/$V_z$/$V_{ss}$로 전파된다.
Elements to include: observed concentration-time points; linear trapezoid segment; descending segment with log-linear alternative; terminal semi-log slope labeled $\lambda_z$; $C_{last}^{obs}$ vs $\hat C_{last}$ decision point; extrapolated tail fraction checkpoint; downstream arrows to CL, $V_z$, $V_{ss}$, exposure comparison
Elements to exclude: exact textbook layout or shaded regions copied from source figures; numerical example values; software-specific λz algorithm; BA/BE regulatory thresholds
Suggested rendering: SVG
Caption: AUC audit는 `observed area + terminal extrapolation`의 chain이며, 각 단계의 오류가 downstream NCA parameters로 전파된다.
Alt text: 관측 농도-시간 점에서 사다리꼴 면적, terminal slope, 외삽 tail, downstream 파라미터로 이어지는 흐름도.
Source relation: Redrawn from textbook concept
<!-- /FIGURE_SCHEMATIC -->

> **Failure Mode — [AUDIT_DERIVED]**  
> 이 세션의 source-anchored 본문에서는 특정 외부 규제 cut-off나 unsupported distortion percentage를 AUC 품질 기준처럼 쓰지 않는다. C1의 방어 가능성은 여기서는 $\lambda_z$ 선택, $\hat C_{last}$ 사용 여부, %extrapolated area, sampling adequacy로 세운다.

---

## C2. AUMC와 MRT — first moment와 평균 체류시간

<!-- MASTER LENS -->
### Big Idea

<!-- ANNOTATION -->
AUMC(← 시간으로 가중한 농도-시간 면적)는 concentration에 time을 곱한 first moment이고, MRT(← 분자 평균 체류시간)는 그 first moment를 AUC로 나눈 평균 체류시간이다. AUC보다 AUMC가 더 불안정한 이유는 단순히 “tail이 크다”가 아니다. AUMC tail에는 $1/\lambda_z$와 $1/\lambda_z^2$ 항이 동시에 들어가므로, terminal slope 오류가 더 강하게 반영된다. [G pp.142–148; T pp.789–792]

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

<!-- ANNOTATION -->
Observed MRT에는 drug이 systemic circulation에 들어오기까지 걸리는 input time이 섞인다. 이 때문에 투여 과정이 만든 지연시간을 residence time으로 착각할 수 있다. 따라서 해석하려는 residence time에 맞게 mean input time (MIT)(← 투여 input이 만든 평균 지연시간)을 빼야 한다. [G pp.149–151; T p.793]

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

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.148, Fig 2.121; Rowland & Tozer 5e, p.791, Fig H-2
Why this matters: C2의 핵심은 AUMC가 time-weighted exposure라는 점이다. AUMC tail의 영향은 수식만으로는 늦게 체화되므로, concentration curve와 first-moment curve를 눈으로 비교해야 한다.
When to look: C2 Recap 직후, C3로 넘어가기 전
Learner instruction: concentration curve와 $t\cdot C(t)$ curve의 late-time 영역을 비교하라. AUMC에서는 늦은 시간이 다시 가중되므로 tail sampling이 MRT에 더 크게 들어간다는 점만 확인한다.
<!-- /FIGURE_POINTER -->

> **Mastery Note — [CRUCIBLE_DERIVED]**  
> MRT는 “평균”이라는 이름 때문에 안정적으로 보이지만, 계산상으로는 AUMC tail의 민감도를 그대로 받는다. 따라서 MRT를 검토한다는 것은 평균값 하나를 보는 일이 아니라 tail sampling과 MIT 보정이 동시에 방어 가능한지 확인하는 일이다.

---

## C3. Apex — CL, $V_{ss}$, $V_z$와 투여 경로 보정

<!-- MASTER LENS -->
### Big Idea

$CL$, $V_{ss}$, $V_z$는 NCA output 표에 나란히 나오지만 같은 종류의 숫자가 아니다. 서로 다른 질문에 답한다. $CL$은 제거 능력, $V_{ss}$는 steady-state 분포 크기, $V_z$는 terminal slope와 결합된 apparent volume이다. 특히 $V_{ss}=MRT\cdot CL$은 input correction이 빠지면 매우 그럴듯해 보이지만, 실제로는 잘못된 분포 부피가 된다. [G pp.149–157]

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

Half-life가 input time에 비해 짧으면 standard MRT/$V_{ss}$ 계산이 불안정해질 수 있다.

<!-- ANNOTATION -->
여기서 핵심은 표준식이 “틀렸다”는 뜻이 아니다. Input duration이 residence time 계산에 너무 크게 들어와 표준식의 적용 영역이 좁아졌다는 뜻이다. Gabrielsson은 이 경우 washout AUC from steady state를 이용한 대안식이 더 robust하며 zero 또는 negative $V_{ss}$를 피한다고 설명한다. [G pp.157–158]

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

- <!-- ANNOTATION --> **Flip-flop kinetics(← 흡수가 제거보다 느려 말단기울기를 지배)**: oral NCA에서 terminal slope가 elimination이 아니라 absorption을 반영할 수 있다. 위험한 이유는 값이 음수처럼 “비명을 지르는” 것이 아니라, 양수·정상 단위의 그럴듯한 output으로 나타날 수 있기 때문이다. `[실무 해석]`

> **Failure Mode — [CRUCIBLE_DERIVED]**  
> Flip-flop 상황의 위험은 숫자가 이상해지는 것이 아니라 숫자가 그럴듯하게 보이는 데 있다. 따라서 oral NCA에서 terminal slope를 elimination으로 해석하려면 IV/reference 정보 또는 absorption-limited 가능성에 대한 명시적 caveat가 필요하다.
- **Nonlinear elimination**: capacity-limited kinetics에서는 CL과 $t_{1/2}$가 first-order parameter이므로 mixed zero-/first-order kinetics와 양립하지 않는다. PK41이 대표 anchor다. [G p.664]
- **NCA-IIV**: NCA의 개체간 분산은 IIV와 residual/error contribution을 함께 포함하므로 PopPK $\omega^2$의 직접 추정값이 아니라 상한으로 보는 것이 안전하다. `[실무 추론]`

### E. Zettelkasten atom

> **NCA-volume atom**: $V_{ss}$는 “분포 부피 하나”가 아니라 $AUC$, $AUMC$, CL, input correction이 모두 통과한 최종 요약값이다. 따라서 $V_{ss}$를 볼 때는 항상 “어떤 MRT를 썼는가?”와 “input time을 뺐는가?”를 같이 봐야 한다. [G pp.149–157]

<!-- RECAP -->
**C3 Recap**: C3는 Apex다. AUC와 AUMC의 작은 불확실성은 여기서 CL과 volume이라는 임상적 이름을 얻고, 그 순간부터 훨씬 설득력 있어 보이기 때문이다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.157, Fig 2.126
Why this matters: C3 Apex에서 §2.8.8 대안식은 단순한 공식 대체가 아니라 적용 영역의 변경이다. washout AUC를 직접 보아야 input-time-dominant 상황에서 표준식이 왜 불안정해지는지 이해된다.
When to look: C3 Recap 직후, C4로 넘어가기 전
Learner instruction: steady-state plateau 이후 washout curve에서 어떤 AUC가 쓰이는지 먼저 확인하라. 그 다음 Eq.2:366/2:367이 왜 zero/negative $V_{ss}$를 피하는지 본문 수식으로 돌아가 검토한다.
<!-- /FIGURE_POINTER -->

> **Practice Lens — [TEXTBOOK_DERIVED]**  
> 표준식과 §2.8.8 대안식의 불일치는 결과를 고르는 문제가 아니라 적용 영역을 진단하는 문제다. 특히 input duration이 residence time을 지배할 때는 표준 $V_{ss}$ 값이 생리학적 이름을 달고 나와도 해석을 보류해야 한다.

---

## C4. Exposure metrics — dose가 아니라 concentration을 본다

<!-- MASTER LENS -->
### Big Idea

§2.9의 핵심은 “투여량(dose)”보다 **systemic exposure**, 특히 total 또는 unbound systemic plasma concentration을 보라는 것이다.

<!-- ANNOTATION -->
앞선 C1–C3가 exposure를 계산하고 파라미터로 변환하는 카드라면, C4는 그 exposure 중 무엇을 PD/safety와 연결할지 고르는 카드다. 같은 dose라도 route, first-pass, nonlinear elimination, active metabolite, protein binding, 투여 방식에 따라 실제 target exposure는 달라진다. [G pp.158–164]

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

이 패턴은 “dose escalation에서 NCA-CL이 단조 감소하면 capacity-limited elimination을 의심하라”는 source-anchored signal이다.

<!-- ANNOTATION -->
즉, 여기서 CL 감소는 단순한 reporting finding이 아니라 모델 전환 신호다. 이후 모델은

$$
V\cdot\frac{dC}{dt}=In-CL\cdot C,\qquad CL=\frac{V_{max}}{K_m+C}
$$

로 전환되며, NCA 결과는 $V\approx2$ L/kg, $K_m\approx150$ µg/L, $V_{max}\approx310$ µg·h⁻¹·kg⁻¹ 등의 initial estimate를 제공한다. 최종 추정값은 $V_{max}=184$ µg·h⁻¹·kg⁻¹, $K_m=83$ µg/L, $V=1.8$ L/kg이었다. 저자의 결론은 명확하다: capacity-limited one-compartment system의 parameters는 CL과 V가 아니라 $V_{max}$, $K_m$, V이며, CL과 $t_{1/2}$는 mixed zero-/first-order kinetics와 incompatible하다. [G pp.663–664]

### D. Zettelkasten atom

> **Exposure atom**: dose는 투입량이고 exposure는 body 또는 target이 실제로 본 concentration-time burden이다. §2.9의 모든 사례는 “dose가 같아도 exposure가 다르면 response가 달라진다”는 한 문장으로 수렴한다. [G pp.158–164]

<!-- RECAP -->
**C4 Recap**: C4는 계산 카드가 아니라 해석 카드다. NCA가 AUC와 concentration metrics를 만든 뒤, 어떤 metric을 efficacy/safety argument의 중심에 둘지 결정하는 단계다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.163, Fig 2.135
Why this matters: C4의 exposure metrics는 단순 목록이 아니다. 그림을 통해 $C_{ss}$/average concentration, $C_{max}$, AUC, threshold-above exposure/$t_d$가 서로 다른 pharmacologic question에 답하는 요약값임을 분리할 수 있다.
When to look: C4 Recap 직후, §5 Confusion Pair로 넘어가기 전
Learner instruction: 각 metric이 concentration-time profile의 어느 부분을 요약하는지 표시 위치를 확인하라. 이후 어떤 PD/safety endpoint가 peak, cumulative burden, duration 중 무엇에 가까운지 생각한다.
<!-- /FIGURE_POINTER -->

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.663, Fig 41.2
Why this matters: PK41의 핵심은 CL 감소가 숫자 한 줄이 아니라 model transition signal이라는 점이다. 이 figure가 없으면 learner가 NCA-CL을 dose별 descriptive table로만 읽고 nonlinear regression 전환의 필연성을 약하게 느낄 수 있다.
When to look: C4 Recap 직후 또는 Q4 self-test 전에
Learner instruction: dose가 증가할수록 CL이 감소하는 방향성만 확인하라. 그 다음 C4의 Michaelis-Menten regression 전환 문장으로 돌아가 “왜 CL/$t_{1/2}$가 final parameter가 아닌가”를 연결한다.
<!-- /FIGURE_POINTER -->

> **Judgment Lens — [TEXTBOOK_DERIVED]**  
> PK41의 핵심 판단은 dose별 CL 값을 더 정교하게 설명하는 것이 아니라, parameter language 자체를 바꾸는 것이다. 용량 의존적 CL 패턴이 보이면 질문은 ‘CL이 얼마인가’에서 ‘$V_{max}$, $K_m$, V로 설명되는가’로 이동한다.

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

> **Mastery Note — [EXPERT_INFERENCE]**  
> 혼동쌍은 용어 암기 문제가 아니라 질문-파라미터 불일치 문제다. 같은 output table 안의 값이라도 ‘무엇을 묻는 숫자인가’를 바꾸면 해석 대상이 완전히 달라진다.

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

NCA는 PopPK의 대체물이 아니라 전후방 도구다. 모델 선택 전에는 EDA와 initial estimate를 만들고, 모델 추정 후에는 population prediction이 관측 exposure의 규모와 일관되는지 확인하는 기준점이 된다. 그러나 NCA는 linear elimination을 가정한다. 이 점을 잊으면 “단순해서 강한 방법”이 “단순해서 틀린 방법”으로 바뀐다. [G p.141]

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

> **Practice Lens — [EXPERT_INFERENCE]**  
> 완성된 NCA 보고서는 숫자 표가 아니라 assumption audit trail이어야 한다. 독자가 terminal slope, tail fraction, input correction, dose-dependence, exposure metric 선택을 따라갈 수 있으면 이후 PopPK 모델링의 출발점으로도 방어 가능해진다.

---

## PART B — Compiler-Only Appendix

This appendix is not learner-facing. It exists only to protect Phase 5 rendering fidelity.

### B1. Compilation Contract

- PART A is the only learner-facing body.
- Phase 5 must render PART A without altering content.
- PART B is instruction/guardrail only and must not be rendered as learner content unless explicitly requested.
- Do not restore deprecated material from Step 1 Draft v0.
- Do not add new scientific content, equations, numerical thresholds, external examples, page tags, or unapproved figures.

### B2. Figure Rendering Instructions

- Preserve Image rights = `None`: do not embed copyrighted textbook images.
- Render every `FIGURE_POINTER` as text-only textbook-reference callout.
- Render `FIGURE_SCHEMATIC` #2 as a visually distinct redraw brief; do not copy textbook layout, shading, labels, color scheme, or exact figure composition.
- Do not add new figures; do not restore rejected figures.
- Approved KEEP plan:

| # | Location | Mode | Source | Decision |
|---:|---|---|---|---|
| 1 | §1 after roadmap | P | Gabrielsson Fig 2.113, p.141 | KEEP |
| 2 | §2 C1 after card | R | Gabrielsson Figs 2.114–2.120, pp.142–147; R&T Fig A-1, p.760 | KEEP |
| 3 | §2 C2 after card | P | Gabrielsson Fig 2.121, p.148; R&T Fig H-2, p.791 | KEEP |
| 4 | §2 C3 after card | P | Gabrielsson Fig 2.126, p.157 | KEEP |
| 5 | §2 C4 after card | P | Gabrielsson Fig 2.135, p.163 | KEEP |
| 6 | §2 C4 after card / Q4 before self-test | P | Gabrielsson Fig 41.2, p.663 | KEEP |

Rejected/merged figures remain rejected: C1 separate textbook figures merged into #2; mixed linear-up/log-down separate pointer rejected; §2.9 catalogue figures beyond #5 rejected; R&T worked tables rejected as standalone figures.

### B3. Page Tag Rendering Rules

- Preserve all existing `[p.XX]`, `[pp.XX–YY]`, `[pp.XX, YY]`, `[p.확인 필요]`, and existing `[G ...]` / `[T ...]` source tags in PART A.
- Render source page tags visibly in HTML where pattern-matching applies.
- Do not fabricate, delete, renumber, or relocate page tags.
- Do not apply page-tag conversion inside code blocks or inside `FIGURE_*` marker blocks.
- Source page tags must remain visible in print mode.

### B4. HTML Compiler Requirements

Phase 5 must render content and must not alter it.

**Marker → component mapping**

| Marker / Pattern | HTML Component | Required rendering |
|---|---|---|
| `<!-- MASTER LENS -->` | Callout box | border-left gold; subtle tinted background |
| `<!-- ANNOTATION -->` | Inline annotation/tooltip style | small muted italic text |
| `<!-- ANCHOR -->` | Bridge sentence | italic muted bridge |
| `<!-- TRENCH -->` | Practical tip box | rose left border / tinted background |
| `<!-- CONFUSION -->` | Side-by-side comparison | amber comparison box/card |
| `<!-- SELF-TEST -->` | Click-to-reveal accordion | answer hidden by default |
| `<!-- RECAP -->` | Section summary box | blue left border / tinted background |
| `[확인 필요]` | Highlighted flag | `<mark>` |
| `[p.XX]`, `[pp.XX–YY]`, `[pp.XX, YY]` | Source page tag | `<span class="source-page">...</span>` |
| `[p.확인 필요]` | Uncertain source tag | `<span class="source-page source-uncertain">...</span>` |
| `<!-- FIGURE_POINTER -->` | Textbook reference callout | text-only callout with Source / Why / When / Learner instruction |
| `<!-- FIGURE_SCHEMATIC -->` | Inline schematic figure | Mermaid or inline SVG; caption and alt/aria label mandatory |
| `<!-- FIGURE_IMAGE_SLOT -->` | Image/placeholder figure | only if rights permit; otherwise placeholder |

**Rendering requirements**

- Single self-contained HTML with custom CSS/JS inline.
- MathJax CDN for inline/display math; preserve all equations.
- Self-test answers hidden by default and revealed by click.
- SessionStorage may persist checklist state.
- Code blocks, if any, receive copy buttons and dark `<pre><code>` styling.
- Provide print/PDF button using `window.print()`.
- Responsive layout: ≤768px single-column/collapsed nav; ≥1024px two-column.
- Dark/light mode follows `prefers-color-scheme`.
- Print CSS hides navigation/backgrounds but keeps source page tags visible.
- External dependencies allowed only for MathJax, Mermaid, and permitted CDN utility libraries; no external local CSS/JS/font/image files unless user-supplied.

**Navigation anchor integrity**

- HTML must include a sticky left sidebar table of contents.
- Use only `<a href="#...">` links.
- Every sidebar href target must have exactly one matching body `id`.
- Every major section heading (§1, §2, §5, §7, §8) must receive a stable id.
- Every §2 concept card should receive a stable id.
- Do not create duplicate ids or broken TOC links.
- Enable `html { scroll-behavior: smooth; }`.
- Before finalizing HTML, count all sidebar href values, confirm each target exists exactly once, and fix any mismatch.
- Sidebar is sticky on desktop, collapsible/static on mobile, and active section highlighting may use IntersectionObserver.

**Figure rendering rules**

- `FIGURE_POINTER`: compact text callout only; no image embedding.
- `FIGURE_SCHEMATIC`: implement the brief faithfully; include only listed elements and exclude listed exclusions. Use inline SVG if Mermaid cannot express the curve/spatial layout reliably.
- For Mermaid, validate syntax before finalizing: valid directive, ASCII-only node IDs, quoted labels with special/non-ASCII characters, quoted edge labels, no invalid semicolons. Fall back to SVG/CSS cards if validation fails.
- Caption and alt/aria text are mandatory for schematic/image figures.

**Prohibited in Phase 5**

- Do not modify PART A text content, equations, page tags, or marker text.
- Do not render markers as plain text.
- Do not render source page tags as plain bracketed text.
- Do not reveal self-test answers by default.
- Do not embed or reproduce copyrighted textbook figures.
- Do not add new source page tags, figures, scientific claims, or external examples.
- Do not create broken sidebar links or duplicate body ids.

### B5. Audit Guardrails

Do not restore the following rejected or unsupported items:

- unsupported `λz 오류 30–50%` distortion claim;
- unsupported `AUMC 외삽 30–60%` claim;
- unsupported FDA 21 CFR 320 / 90% CI 80–125% / Clinical Hold / NDA Deficiency Letter / Information Request claims;
- `R&T Table A-1 = zileuton` mislabel;
- `2–4 half-lives` terminal slope ideal condition;
- `$V_z \ge V_{ss}$ always` as PDF-anchored statement;
- NONMEM code block, TMDD/PBPK expansion, concentration-dependent vs time-dependent killing expansion;
- any unapproved code block, unapproved figure embedding, or NOT_IN_SOURCE material rejected by Audit/Content Lock.

### B6. Crucible Guardrails

- Crucible is not a raw content source at this stage.
- Preserve only already-adopted or explicitly allowed Grade A logic.
- Do not reintroduce omitted/rejected Crucible items.
- Do not convert speculative insight into textbook-derived fact.
- All Crucible-derived additions in PART A must remain labeled `CRUCIBLE_DERIVED`.

### B7. Deprecated and Forbidden Restorations

- Step 1 Draft v0 is deprecated.
- Do not restore rejected overclaims, unsupported numbers, unsupported regulatory claims, source-unsupported examples, unapproved code, or unapproved figures.
- Do not use Step 1 Draft v0 as learner-body source except through a logged Micro-Patch Gate.
- Do not use Content Lock v1 to override Content Lock v2.

### B8. PATCH MODE Splice Verification Table

| Marker # | Anchor text | Anchor found? | Match count | Inserted? | Final location (§ + card) |
|---|---|---:|---:|---|---|
| 1 | `**§1 Recap**: NCA의 강점은 단순함이고, 약점도 같은 지점에서 온다. 모델을 덜 세우는 대신, terminal slope·input correction·linear elimination 가정이 무너...` | YES | 1 | YES | §1 — Session Header & Roadmap |
| 2 | `**C1 Recap**: AUC가 흔들리면 CL, $V_z$, $V_{ss}$, exposure comparison이 모두 흔들린다. NCA audit은 항상 $\lambda_z$ plot과 %extrapola...` | YES | 1 | YES | §2 / C1 |
| 3 | `**C2 Recap**: AUMC는 time-weighted exposure다. 그래서 tail과 input correction을 놓치면 MRT는 안정적인 평균이 아니라 terminal slope 오류를 증폭한...` | YES | 1 | YES | §2 / C2 |
| 4 | `**C3 Recap**: C3는 Apex다. AUC와 AUMC의 작은 불확실성은 여기서 CL과 volume이라는 임상적 이름을 얻고, 그 순간부터 훨씬 설득력 있어 보이기 때문이다.` | YES | 1 | YES | §2 / C3 |
| 5–6 | `**C4 Recap**: C4는 계산 카드가 아니라 해석 카드다. NCA가 AUC와 concentration metrics를 만든 뒤, 어떤 metric을 efficacy/safety argument의 중심에 ...` | YES | 1 | YES | §2 / C4 |

### B9. Zero-Omission Coverage Matrix

| Domain | Required item | Evidence in PART A | Status | Action |
|---|---|---|---|---|
| C1 Scope Lock required concepts | AUC, AUMC/MRT, CL/Vss/Vz, exposure metrics | §2 C1–C4 | PRESENT | None |
| C2 Scope Lock data anchors | PK41 310/520/780 µg·kg⁻¹, CL 1.6→0.9, V 2.3→1.8, MRT 1.4→1.9, final Vmax/Km/V | C4 PK41 dynamic source anchor; Q4 | PRESENT | None |
| C2 Scope Lock data anchors | R&T Table A-1 generic oral 50 mg AUC=26.60; Table H-1 AUC/AUMC/MRT values | C1 equations; C2 equations; Q5 | PRESENT | None |
| C3 Audit MUST_FIX | Remove unsupported λz 30–50%, AUMC 30–60%, external BA/BE threshold overclaims | C1/C2 corrected qualitative language; PART B forbidden restoration | PRESENT | None |
| C3 Audit MUST_FIX | 3–4 half-lives, not 2–4; Table A-1 not zileuton | C1 λz selection; C1 R&T note | PRESENT | None |
| C3 Audit SHOULD_FIX | PK41 numerical anchor and final MM estimates | C4 PK41 anchor; Q4 | PRESENT | None |
| C4 Audit T5 | No unresolved high-impact omission in C1–C4 / PK41 / R&T anchors | §2 and §7 | PRESENT | None |
| C5 Audit T6 / Phase 4C | KEEP figures #1–#6 present exactly once; rejected figures not restored | FIG-P01, FIG-R02, FIG-P03, FIG-P04, FIG-P05, FIG-P06 | PRESENT | None |
| C6 Page tag integrity | Existing [G]/[T] source page tags preserved; no new page tags fabricated in augmentation | PART A body | PRESENT | None |
| C7 Crucible Grade A preservation | flip-flop silent risk, AUMC tail sensitivity, NCA→model transition judgment | C2, C3 Limitations, C4 PK41, mastery notes | PRESENT_COMPRESSED | None |
| C8 Deprecated Draft regression | unsupported regulatory claims, unsupported numeric distortion, NONMEM code, TMDD/PBPK, killing extensions not restored | PART A and B guardrails | PRESENT | None |
| C9 Canonical body integrity | Scientific body from Content Lock v2 §1–§8 retained; figure markers and labeled augmentation only added | PART A | PRESENT | None |

### B10. Micro-Patch Log

No micro-patches needed. PART A equals the learner-facing Content Lock v2 body from §1–§8 with approved Phase 4C marker splices and approved Mastery Augmentation Layer. Initial process tables/logs from Content Lock v2 were not learner-facing scientific body and were moved out of PART A by construction.

### B11. Mastery Augmentation Log

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
|---|---|---|---|---|---|---|
| M1 | §1 after FIG-P01 | Practice Lens | YES | EXPERT_INFERENCE | Turns output-table reading into assumption-audit workflow. | Medium |
| M2 | C1 after FIG-R02 | Failure Mode | YES | AUDIT_DERIVED | Prevents restoration of unsupported numeric/regulatory overclaims while preserving source-grounded AUC QC. | Low |
| M3 | C2 after FIG-P03 | Mastery Note | YES | CRUCIBLE_DERIVED | Clarifies why MRT must be audited through tail and MIT, not accepted as a stable average. | Low |
| M4 | C3 after FIG-P04 | Practice Lens | YES | TEXTBOOK_DERIVED | Frames formula disagreement as applicability diagnosis. | Low |
| M5 | C3 Limitations after flip-flop bullet | Failure Mode | YES | CRUCIBLE_DERIVED | Preserves crucible insight on silent flip-flop failure without adding new example or numbers. | Low |
| M6 | C4 after FIG-P06 | Judgment Lens | YES | TEXTBOOK_DERIVED | Reinforces PK41 as parameter-language transition, not descriptive-table finding. | Low |
| M7 | §5 after recap | Mastery Note | YES | EXPERT_INFERENCE | Transforms confusion pairs into parameter-question matching. | Medium |
| M8 | §8 after recap | Practice Lens | YES | EXPERT_INFERENCE | Connects the final doctrine to report defensibility and later PopPK use. | Medium |

| Rejected candidate | Reason for rejection |
|---|---|
| New external BA/BE acceptance threshold note | Rejected: outside source scope and previously rejected by Audit/Content Lock. |
| New drug/mechanism examples beyond PK41 and R&T examples | Rejected: would introduce new named examples not present in approved sources. |

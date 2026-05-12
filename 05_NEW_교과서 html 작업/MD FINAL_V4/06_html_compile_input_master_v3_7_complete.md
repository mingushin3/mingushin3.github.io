# 비구획 분석(NCA) — AUC, AUMC, MRT, $V_{ss}$와 노출 평가의 실무 경계 — v3.7

<!-- 기호 통일: 신규 변경 없음 — 원본 첫 등장 표기 유지 ($V_{max}$, $K_m$, $V_{ss}$, $V_z$, $\lambda_z$) -->

Turbojoint® PK41에서는 310/520/780 µg·kg⁻¹을 각각 5시간 IV 주입한 뒤 투여량이 증가할수록 NCA-CL이 1.6→0.9 L·h⁻¹·kg⁻¹로 감소했습니다. 같은 표 안에서 V는 2.3→1.8 L·kg⁻¹, MRT는 1.4→1.9 h로 움직였습니다. 이 장면에서 NCA 표는 “최종 답”이 아니라 $V_{max}$, $K_m$, V를 갖는 Michaelis-Menten 회귀로 넘어가기 위한 출발점입니다. [G pp.661–664]

## 학습 안내(Learner Navigation Aid)

**이 핸드아웃 사용법**: PART A만 읽어도 학습용 핸드아웃으로 사용할 수 있습니다. 먼저 §1에서 직렬 작업흐름(workflow)을 잡고, §2의 C1→C4를 순서대로 읽으면 됩니다. 그 뒤 §5 혼동쌍과 §7 자기 테스트(self-test)로 점검합니다.

**학습 경로(Learning Route)**: C1 $AUC/\lambda_z$ → C2 $AUMC/MRT$ → C3 $CL$·$V_{ss}$·$V_z$/투여 경로 보정(input correction) → C4 노출 지표 선택(exposure metric selection) → §5 혼동쌍(confusion pairs) → §7 능동 회상(active recall) → §8 전문가 잠금(professional lock).

**시작 전 점검**: $CL/V$ 개념, 1·2 구획 모델(compartment model), Michaelis-Menten kinetics, $t_{1/2}=\ln(2)/k$를 떠올리면 됩니다.

**완료 후 확인**: NCA 표를 볼 때 말단 기울기(terminal slope) → 외삽 비율(%extrapolated) → $AUMC/MRT$ → 투여 경로 보정(input correction) → $CL/V$ → 용량 의존성(dose-dependence) → 노출 지표(exposure metric) 순서로 검토할 수 있어야 합니다.

**그림 안내**: 교과서 원문 그림은 직접 삽입하지 않고, 해당 그림을 언제·왜 확인해야 하는지 텍스트 참조로만 제시합니다. 새 도식은 원문 그림의 복제가 아니라, 구조를 다시 설명하기 위한 HTML 렌더링용 개념 도식으로만 사용합니다.

<!-- SLIDE_START: §1 | title: 세션 헤더와 로드맵 -->

# §1 — 세션 헤더와 로드맵(Session Header & Roadmap)

**세션 제목**: 비구획 분석(NCA) — AUC, AUMC, MRT, $V_{ss}$와 노출 평가의 실무 경계  
**출처**: Gabrielsson & Weiner 5e Ch.2 §2.8–§2.9, PK41; Rowland & Tozer 5e Appendix A·H. [G pp.141–164, pp.661–664; T pp.759–762, pp.789–793]

**핵심 통찰(Big Idea)**: NCA(← 특정 구획 모델(compartment model) 없이 면적을 요약하는 분석)는 `[해석]` *model-free*라기보다 *compartment-free*에 가깝습니다. 특정 구획 모델을 세우지 않아도 되지만, 관측 구획(sampling compartment)에서는 **선형 소실(linear elimination)**(← 농도에 비례해 제거되는 소실) 가정이 여전히 필요합니다. 따라서 PK41처럼 용량 제한 동력학(capacity-limited kinetics)이 보이면 NCA 결과는 최종 해석값이 아니라 비선형 회귀(nonlinear regression)의 **초기 파라미터 앵커(initial parameter anchor)**로 내려와야 합니다. [G p.141; G pp.661–664]

```text
Layer 1 — 무엇인가
  NCA → AUC → AUMC → MRT → CL/Vss/Vz → exposure metric

Layer 2 — 어떻게 계산되는가
  trapezoid + log-trapezoid → λz extrapolation → AUMC tail → MRT=AUMC/AUC → Vss=MRT·CL

Layer 3 — 언제, 왜 중요한가
  λz 방어 → 외삽률 방어 → MIT 보정 → 비선형 신호 감지 → endpoint별 exposure 선택
```

🧭 **읽는 순서:**  
카드 1 (C1): AUC 숫자를 보기 전에 어떤 꼬리와 어떤 $\lambda_z$를 믿어야 하는가?  
카드 2 (C2): 평균 체류시간이라는 값이 왜 AUC보다 꼬리에 더 민감한가?  
카드 3 (C3): AUC와 AUMC의 작은 오류가 어떻게 CL, $V_{ss}$, $V_z$라는 임상 파라미터로 굳어지는가?  
카드 4 (C4): 계산된 노출 중 어느 지표를 PD/safety 논증의 중심에 놓아야 하는가?

**지식 그래프 위치:**  
`[선행 세션: CL/V, 1·2 구획, Michaelis-Menten, t1/2] → [이 세션: NCA 면적·모멘트·노출 감사] → [후속 세션: PopPK 초기 모수, 비선형 PK 회귀, BA/BE·clinical pharmacology 보고서]`

**개념 항법도**: 이 세션의 네 카드는 병렬 암기 목록이 아닙니다. Phase 1 SAD/MAD EDA에서 순서대로 작동하는 직렬 작업흐름(workflow)으로 이해하면 됩니다.

| 단계 | 판단 질문 | 카드 | 오류 전파 |
|---|---|---|---|
| 1 | 면적이 믿을 만한가? | C1 $AUC/\lambda_z$/외삽(extrapolation) | AUC 오류 → CL, V, 노출(exposure) 모두 왜곡 |
| 2 | 시간 모멘트가 안정적인가? | C2 AUMC/MRT | AUMC 꼬리(tail) 오류 → MRT와 $V_{ss}$ 왜곡 |
| 3 | 분포·청소 파라미터가 경로 보정됐는가? | C3 CL/$V_{ss}$/$V_z$ | MIT 누락 → $V_{ss}$ 해석 오류 |
| 4 | 어떤 노출 지표로 PD/safety를 볼 것인가? | C4 노출 지표(exposure metrics) | 투여량만 보는 해석(dose-only 해석) → 노출-반응(exposure-response) 판단 오류 |

**선행 지식**: $CL/V$ 정의, 1·2 구획 모델(compartment model), Michaelis-Menten kinetics, $t_{1/2}=\ln(2)/k$입니다.  
**후속 연결**: PopPK 초기 모수 설정, 비선형 PK 회귀(nonlinear PK regression), BA/BE·clinical pharmacology 보고서의 노출 표(exposure table) 구성입니다. 단, 구체적 외부 규제 기준은 본 출처 범위(source scope) 밖입니다.

**§1 요약(Recap)**: NCA의 강점은 단순함이고, 약점도 같은 지점에서 옵니다. 모델을 덜 세우는 대신, 말단 기울기(terminal slope)·투여 경로 보정(input correction)·선형 소실(linear elimination) 가정이 무너지면 오류가 조용히 후속 분석으로 전파됩니다.

> 📖 **교과서 그림 참조:** Gabrielsson & Weiner 5e, p.141, Fig 2.113  
> NCA가 면적 합(area sums)을 다루고, 회귀(regression)가 파라미터화된 함수(parameterized function)를 적합(fitting)한다는 대비는 이 세션 전체의 프레임입니다. 이 그림이 없으면 PK41에서 NCA가 왜 최종 답(final answer)이 아니라 회귀 초기값으로 내려가는지 보여 주는 구조적 전환이 약해집니다.  
> 확인 시점: §1 요약(Recap) 직후, C1로 들어가기 전에 확인하면 됩니다.

> 💼 **실무 인사이트 — [EXPERT_INFERENCE]**  
> NCA 출력(output)을 읽을 때는 표에 나온 행 순서대로 읽지 않습니다. 가정을 점검하는 순서로 읽어야 합니다. 즉, 먼저 말단 기울기(terminal slope)와 외삽 비율을 보고, 그 다음 MRT/투여 경로 보정(input correction)을 본 뒤, 마지막에 CL·분포용적(volume)·노출 지표(exposure metric)를 해석합니다.

<!-- SLIDE_START: §2 | title: 개념 해부 카드 -->

# §2 — 개념 해부 카드(Concept Anatomy Cards)

<!-- SLIDE_START: C1 | title: AUC 계산 — 선형/로그-선형 사다리꼴법, λz, 외삽 -->

## C1. AUC 계산 — 선형/로그-선형 사다리꼴법(linear/log-linear trapezoidal rule), $\lambda_z$, 외삽(extrapolation) [⚡ Apex Concept]

> **거장의 시각**  
> 💢 **흔한 오해:** NCA는 구획 모델을 세우지 않으니 계산된 AUC가 데이터의 객관적 면적이라고 생각하기 쉽습니다.  
> ✅ **실제는:** AUC는 관측 사다리꼴 합과 $\lambda_z$ 기반 외삽 꼬리의 합이므로, 말단기와 외삽률 방어가 무너지면 CL·$V_z$·$V_{ss}$가 함께 무너집니다.  
> 🎯 **체화할 단 하나의 직관:** AUC 감사는 값이 아니라 `말단 기울기 선택 → $C_{last}$ 처리 → 외삽 분율`의 감사 기록입니다.

### A. 형식적 정의(Formal Definition)

- **AUC(영차 모멘트 면적, zero moment area)**: 농도-시간 곡선(concentration-time curve) 아래 면적입니다. [G p.142]
- **$AUC_{0-t_{last}}$**: 관측 자료로 계산한 면적입니다.
- **$AUC_{t_{last}\to\infty}$**: 마지막 측정 시점 이후를 단일지수적 감소(mono-exponential decline)로 가정해 외삽한 면적입니다.
- **총 AUC(Total AUC)**: $AUC_{0-t_{last}}+AUC_{t_{last}\to\infty}$입니다.

**선형 사다리꼴법(Linear Trapezoidal Rule)** [G p.143, Eq.2:310; T pp.759–760]

$$
\underbrace{AUC_0^{t_{last}}}_{\text{관측 AUC}}
=\sum_i \underbrace{\frac{C_i+C_{i+1}}{2}}_{\text{평균농도}}\cdot\underbrace{\Delta t}_{\text{시간폭}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $AUC_0^{t_{last}}$ | 농도×시간 | 관측 노출량 | 표본추출 시간, 농도 측정값 |
| $C_i$, $C_{i+1}$ | 농도 | 인접 시점 혈장 농도 | 흡수·분포·소실, 측정오차 |
| $\Delta t$ | 시간 | 구간 폭 | sampling design |
| $\lambda_z$ | 1/시간 | 말단 로그농도-시간 직선의 기울기 | 말단기 선택, 분포기 오염, 비선형 소실 |
| $C_{last}$ 또는 $\hat C_{last}$ | 농도 | 마지막 농도 또는 회귀선 기반 마지막 농도 | BLQ 처리, 회귀선 이탈 |
| $AUC_{total}$ | 농도×시간 | 관측+외삽 총 노출 | 관측 면적, 말단 외삽 |

R&T Table A-1의 일반 경구(generic oral) 50 mg 예시는 이 계산으로 총 AUC(total AUC) = 26.60 mg·hr/L을 얻습니다. 이 예시는 **zileuton이 아닙니다**. Zileuton은 R&T Table A-2의 600 mg 경구 자료셋(oral dataset)입니다. [T pp.759–762]

💡 **사다리꼴은 면적계가 아니라 감사 체인** — 선형 사다리꼴 값은 농도 점과 간격의 곱이므로, 숫자가 맞아도 말단 꼬리가 틀리면 전체 AUC 해석이 틀릴 수 있습니다.  
⚠️ **헷갈림 방지:** 선형 사다리꼴법(linear trapezoid)은 상승 구간에서 과소추정(underestimate), 하강 구간에서 과대추정(overestimate)합니다. 이 편향은 표본추출 간격(sampling interval)이 반감기(half-life)에 비해 클수록 커집니다. [G p.142]  
🔑 **AUC 보고 규칙:** AUC 값만 보고하지 말고 $\lambda_z$, $C_{last}^{obs}$ vs $\hat C_{last}$, %extrapolated를 함께 둡니다.

### B. 수식 및 출처 고정 규칙

**로그-선형 사다리꼴법(Log-Linear Trapezoidal Rule)** [G pp.144–145, Eq.2:316; T p.761]

$$
\underbrace{AUC_i^{i+1}}_{\text{구간 AUC}}
=\underbrace{\frac{C_i-C_{i+1}}{\ln(C_i/C_{i+1})}}_{\text{로그평균농도}}\cdot\underbrace{\Delta t}_{\text{시간폭}}
$$

💡 **비유:** 하강 구간의 로그-선형 평균은 내리막 곡선을 직선 판자로 덮지 않고, 곡선의 기울기에 맞춘 얇은 천으로 덮는 방식에 가깝습니다. 간격이 길수록 판자식 선형 근사보다 곡률을 더 존중합니다.

적용 조건은 **하강 구간(descending data)**입니다. $C_i=0$ 또는 $C_{i+1}=C_i$이면 로그-선형 규칙(log-linear rule)은 실패하므로 선형 방식으로 대체(linear fallback)합니다. [G p.144]

**혼합 방식(Mixed Approach)**: 증가/동일(increasing/equal) 구간은 선형(linear), 감소(decreasing) 구간은 로그-선형(log-linear)으로 처리할 수 있습니다. 단, 이를 “항상 표준”이라고 단언하지는 않아야 합니다. 합리적인 표본추출 설계(sampling design)에서는 두 방법의 차이가 대개 임상적으로 작다는 저자의 균형도 함께 기억하면 됩니다. [G p.146]

**말단 외삽(Terminal Extrapolation)** [G pp.143–145, Eq.2:311/2:319]

$$
\underbrace{AUC_{t_{last}\to\infty}}_{\text{꼬리 AUC}}
=\frac{\underbrace{C_{last}\ \text{or}\ \hat C_{last}}_{\text{말단농도}}}{\underbrace{\lambda_z}_{\text{말단기울기}}}
$$

관측 $C_{last}$가 말단 회귀선(terminal regression line)에서 벗어나면, 관측값 대신 회귀 기반 예측값 $\hat C_{last}$ 사용이 일반적으로 권고됩니다. [G p.147]

**외삽 면적 비율(Percent Extrapolated Area)** [G p.148, Eq.2:324]

$$
\underbrace{\%Extrapolated}_{\text{외삽률}}
=\frac{\underbrace{AUC_{t_{last}\to\infty}}_{\text{꼬리 AUC}}}{\underbrace{AUC_{total}}_{\text{총 AUC}}}\times 100
$$

저자 권고는 외삽 면적(extrapolated area)이 일반적으로 총 AUC(total AUC)의 20–25%를 넘지 않는 것입니다. 이를 넘으면 예비 추정값(preliminary estimate)으로 다뤄야 합니다. [G p.148]

### C. $\lambda_z$ 선정과 맥락 보충

말단 기울기(terminal slope)는 반로그 도표(semi-log plot)에서 개별 프로파일(individual profile)을 보고 정합니다. 최소 3–4개 관측값(observations)이 필요하고, 이상적으로는 말단기(terminal phase)에서 **3–4 반감기(half-lives)**가 경과해야 합니다. [G p.146]

> 💼 **실무 인사이트:** 자동 NCA 출력(output)의 $\lambda_z$ 구간은 그대로 믿지 말고, 반로그 도표(semi-log plot)에서 말단기(terminal phase)인지 직접 확인해야 합니다. 높은 보정 $R^2$(adjusted $R^2$)만으로 분포기 점이 말단 기울기(terminal slope)에 섞이면 AUC 꼬리(tail)뿐 아니라 CL, $V_z$, $V_{ss}$까지 연쇄적으로 흔들립니다.

| 상황 | 파라미터 변화 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| 정상상태 투여 간격 | $AUC_{0-\tau,ss}$가 단회 $AUC_{0-\infty}$와 동등 취급 가능 | → | 반복투여 노출 비교 가능 | 잔류 면적과 다음 투여 외삽 면적의 상쇄를 설명 [G p.152] |
| LOQ 미만 값 | 0 또는 LOQ 대체 시 AUC 왜곡 | → | 말단기·외삽률 왜곡 | 결측(missing) 처리 원칙 적용 [G p.153] |
| AUC 단독 보고 | CL 생리학 연결 약화 | → | 공변량 회귀와 보고서 해석성 저하 | $CL$ 또는 $CL/F$를 1차 파라미터로 보고 [G p.148] |

### D. 경계 조건과 원자 노트

| 이 카드에서 다루는 것 | → | 후속 세션으로 이월 | 이유 |
|---|---|---|---|
| 선형 소실(linear elimination) | → | 비선형 PK 회귀 | 깨지면 $\lambda_z$와 외삽 AUC의 의미가 약해집니다. |
| 실제 terminal phase | → | PopPK 초기값 | 흡수/분포기를 말단기로 착각하면 꼬리(tail)가 왜곡됩니다. |
| 외삽 분율 $\leq 20$–$25\%$ | → | BA/BE·임상약리 보고 | 초과 시 NCA 결과는 예비적(preliminary) 성격이 강해집니다. |
| 관측 $C_{last}$와 회귀선 일치 | → | CL/$V_z$ 계산 | 벗어나면 $\hat C_{last}$ 사용을 검토합니다. |

> **NCA-AUC 원자 노트(atom)**: AUC는 사다리꼴 합이 아니라 “사다리꼴 합 + $\lambda_z$ 기반 꼬리(tail)”입니다. 그래서 AUC 검토의 핵심은 값 자체가 아니라 말단 기울기(terminal slope) 선택, $\hat C_{last}$ 사용 여부, 외삽 면적 비율(%extrapolated area)입니다. [G pp.143–148]

> 📖 **교과서 그림 참조:** Gabrielsson & Weiner 5e, p.141, Fig 2.113  
> NCA가 면적 합(area sums)을 다루고, 회귀(regression)가 파라미터화된 함수(parameterized function)를 적합(fitting)한다는 대비는 이 세션 전체의 프레임입니다.  
> 확인 시점: §1 요약(Recap) 직후, C1로 들어가기 전에 확인하면 됩니다.

> 📊 **개념 도식 (HTML에서 렌더링):** C1 AUC 감사 체인 — AUC 신뢰도는 사다리꼴 계산보다 말단 기울기(terminal slope)와 외삽 꼬리(extrapolated tail) 검증에서 결정되며, 그 오류는 CL/$V_z$/$V_{ss}$로 전파됩니다.

### M. Plausible Fallacy — 나비효과 연쇄

**오류:** NCA는 구획 모델(compartment model)을 세우지 않으므로 어떤 데이터에도 객관적인 면적 답을 준다고 판단한다.  
**왜 그럴싸한가:** 결과가 사다리꼴 합과 모멘트 계산처럼 보이기 때문에 모델-기반 오류에서 자유로운 산술 요약처럼 보입니다.  
**나비효과:** $\lambda_z$ 선택 방어 실패 또는 $\%AUC_{extrap}>20$–$25\%$ → AUC 꼬리(tail)가 관측 영역만큼 결과를 좌우 → [임상] CL·$V_z$·$V_{ss}$ 기반 용량·노출 해석 왜곡 → [모델링/규제] PopPK 초기 추정값(initial estimate) 편향, NONMEM 수렴 경로와 공변량(covariate) 신호 강도 왜곡, 외삽 분율과 $\lambda_z$ 선택 근거에 대한 재분석 요구.

> **C1 체화 핵심**  
> ① `AUC가 믿을 만한가?` → $\lambda_z$, $C_{last}$ 처리, 외삽률이 결정  
> ② `관측 면적 vs. 외삽 면적 혼동` → 총 AUC가 아니라 꼬리 AUC가 신뢰도를 지배  
> ⚡ `NCA는 assumption-free` → 선형 소실·말단기·표본추출 충분성 가정 누락 → CL/$V_z$/$V_{ss}$와 PopPK 초기값까지 오류 전파

<!-- SLIDE_START: C2 | title: AUMC와 MRT — 일차 모멘트와 평균 체류시간 -->

## C2. AUMC와 MRT — 일차 모멘트(first moment)와 평균 체류시간

> **앞 카드에서 이 카드로:** C1이 “얼마나 노출되었는가”를 감사했다면, C2는 그 노출이 “언제 발생했는가”를 시간 가중으로 다시 묻습니다.

> **거장의 시각**  
> MRT를 안정적인 평균값처럼 읽으면 AUMC 꼬리의 $1/\lambda_z^2$ 민감도를 놓칩니다.  
> AUMC를 시간가중 노출로 보면, 꼬리 표본추출과 MIT 보정이 MRT의 신뢰도를 즉시 결정한다는 점이 보입니다.

### A. 형식적 정의(Formal Definition)

- **AUMC**: $t\cdot C(t)$ 대 시간 곡선(time curve) 아래 면적, 즉 일차 모멘트 면적(first moment area)입니다. [G p.142]
- **MRT**: 몸(body) 또는 표본추출계(sampling system) 안에 분자(molecule)가 머무는 평균 시간입니다. [T p.789]

R&T Appendix H는 분자량(molecular weight) 300 g/mol인 약물 1 mg에 약 $2\times10^{18}$개의 분자(molecules)가 들어 있다는 직관에서 시작해, 각 분자의 체류시간(residence time) 평균을 MRT로 정의합니다. [T p.789]

**AUMC 선형 사다리꼴 계산** [G p.144, Eq.2:312]

$$
\underbrace{AUMC_0^{t_{last}}}_{\text{관측 AUMC}}
=\sum_i \underbrace{\frac{t_iC_i+t_{i+1}C_{i+1}}{2}}_{\text{시간가중 평균}}\cdot\underbrace{\Delta t}_{\text{시간폭}}
$$

**AUMC 꼬리(tail) 외삽** [G pp.144–145, Eq.2:313/2:320]

$$
\underbrace{AUMC_{t_{last}\to\infty}}_{\text{꼬리 AUMC}}
=\underbrace{\frac{t_{last}C_{last}}{\lambda_z}}_{\text{시점가중 꼬리}}
+\underbrace{\frac{C_{last}}{\lambda_z^2}}_{\text{기울기 민감도}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $AUMC$ | 농도×시간² | 시간으로 가중한 노출 | 늦은 시점 농도, 꼬리 표본추출 |
| $MRT$ | 시간 | 분자 평균 체류시간 | AUMC/AUC, 입력시간 보정 |
| $t_{last}$ | 시간 | 마지막 관측 시점 | sampling design |
| $\lambda_z$ | 1/시간 | 말단기울기 | 말단기 선택, 분포기 오염 |
| $MIT$ | 시간 | 평균 입력 지연시간 | IV bolus, infusion, extravascular input |

💡 **AUMC는 늦은 시간에 더 큰 무게를 얹는다** — 같은 농도라도 늦게 남아 있으면 시간 가중치가 붙어 MRT와 $V_{ss}$를 더 크게 흔듭니다.  
⚠️ **헷갈림 방지:** “평균”이라는 단어 때문에 MRT가 안정적으로 보이지만, 계산상으로는 AUMC 꼬리와 $\lambda_z$ 오류를 그대로 상속합니다.  
🔑 **MRT 보고 규칙:** MRT 값 옆에는 AUMC 외삽, MIT 보정, 입력 방식(input mode)을 함께 적습니다.

💡 **비유:** AUC가 하루 동안 받은 햇빛의 총량이라면, AUMC는 늦은 오후 햇빛에 더 무거운 추를 매단 저울입니다. 해가 질 무렵의 작은 오차도 평균 체류시간을 크게 밀어냅니다.

### B. MRT 정의와 수치 앵커

**분자 정의(Molecular Definition)** [T p.789, Eq.H-1]

$$
\underbrace{MRT}_{\text{평균체류}}
=\frac{\underbrace{\sum_j t_j}_{\text{체류시간 합}}}{\underbrace{N}_{\text{분자수}}}
$$

**혈장 정의(Plasma Definition)** [T p.791, Eq.H-8]

$$
\underbrace{MRT}_{\text{혈장 MRT}}
=\frac{\underbrace{AUMC_0^\infty}_{\text{시간가중 노출}}}{\underbrace{AUC_0^\infty}_{\text{총 노출}}}
$$

R&T Table H-1의 수치 예시(numerical example)는 $AUC=44.2$ mg·hr/L, $AUMC=177$ mg·hr²/L, 혈장 MRT(plasma MRT) $\approx 4.0$ hr, 소변 MRT(urinary MRT) $\approx 4.25$ hr, simulated MRT $\approx 4.3$ hr로 서로 일관됩니다. [T p.792]

### C. 투여시간 보정(Input-Time Correction)

관측 MRT(observed MRT)에는 약물(drug)이 전신순환(systemic circulation)에 들어오기까지 걸리는 입력 시간(input time)이 섞입니다. 이 때문에 투여 과정이 만든 지연시간을 체류시간(residence time)으로 착각할 수 있습니다. 따라서 해석하려는 체류시간에 맞게 평균 입력 시간(MIT, mean input time)(← 투여 입력(input)이 만든 평균 지연시간)을 빼야 합니다. [G pp.149–151; T p.793]

| 입력 방식(Input mode) | MIT | 보정 MRT(Corrected MRT) |
|---|---:|---|
| IV bolus | 0 | $MRT=AUMC/AUC$ |
| 일정 IV 주입(Constant IV infusion) | $T_{inf}/2$ | $MRT=AUMC/AUC-T_{inf}/2$ |
| 1차 혈관외 입력(First-order extravascular input) | $1/K_a$ | $MRT=AUMC/AUC-1/K_a$ |

$$
\underbrace{MRT_{\text{corrected}}}_{\text{보정 MRT}}
=\underbrace{\frac{AUMC}{AUC}}_{\text{관측 MRT}}-\underbrace{MIT}_{\text{입력 평균시간}},\qquad
MIT\in\{\underbrace{0}_{\text{IV bolus}},\underbrace{T_{inf}/2}_{\text{주입중간}},\underbrace{1/K_a}_{\text{흡수평균}}\}
$$

경구 흡수(oral absorption)에서 $K_a$는 단순 흡수만이 아니라 분해(degradation) 등 병렬 과정을 포함할 수 있습니다. 따라서 $1/K_a$를 “순수 흡수시간”으로 과해석하지 않습니다. [G p.150]

### D. 맥락 확장과 경계 조건

대사체(metabolite) 또는 하류 구획(downstream compartment)에서는 $MBRT$에서 상류 입력 체류시간(upstream input residence time)을 빼는 방식으로 $MDRT$를 정의합니다. 핵심은 체류시간(residence time)이 “공간별 고유 시간 + 입력 시간(input time)”으로 누적된다는 점입니다. [G pp.155–156]

R&T는 소변 배설 자료(urinary excretion data)에서도 MRT를 계산할 수 있음을 보입니다. 다만 이 세션에서는 혈장 MRT(plasma MRT)가 주축입니다. 이 한 문장만으로 혈장만 가능하다는 오해(plasma-only 오해)를 방지합니다. [T pp.790–792]

| 이 카드에서 다루는 것 | → | 후속 세션으로 이월 | 이유 |
|---|---|---|---|
| 꼬리 표본추출(tail sampling) | → | $V_{ss}$ 계산 | AUMC는 늦은 시간에 더 민감하므로 꼬리 부족이 MRT를 크게 흔듭니다. |
| $\lambda_z$ 신뢰 가능성 | → | CL/$V_z$ 해석 | $1/\lambda_z^2$ 항 때문에 AUMC 꼬리 민감도가 커집니다. |
| 입력 방식(input mode) | → | MIT 보정 | MIT 보정 누락 시 MRT와 $V_{ss}$가 함께 왜곡됩니다. |
| 선형 소실(linear elimination) | → | compartment-free 체류시간 해석 | 선형 소실이 깨지면 MRT 해석이 흔들립니다. |

> **NCA-MRT 원자 노트(atom)**: MRT는 반감기(half-life)가 아닙니다. MRT는 “분자가 계(system) 안에서 보낸 시간의 평균”이고, 계산상으로는 $AUMC/AUC$이며, 투여 경로에 따라 MIT를 빼야 해석 가능한 체류시간(residence time)이 됩니다. [G pp.149–151; T pp.789–793]

> 📖 **교과서 그림 참조:** Gabrielsson & Weiner 5e, p.148, Fig 2.121; Rowland & Tozer 5e, p.791, Fig H-2  
> C2의 핵심은 AUMC가 시간 가중 노출(time-weighted exposure)이라는 점입니다. AUMC 꼬리(tail)의 영향은 수식만으로는 늦게 체화되므로, 농도 곡선(concentration curve)과 일차 모멘트 곡선(first-moment curve)을 눈으로 비교해야 합니다.  
> 확인 시점: C2 요약(Recap) 직후, C3로 넘어가기 전에 확인하면 됩니다.

> **C2 체화 핵심**  
> ① `평균 체류시간을 보고할 때` → AUMC 꼬리와 MIT 보정이 결정  
> ② `MRT vs. 반감기 혼동` → MRT는 분자 체류 평균, 반감기는 말단 감소 시간척도  
> ⚡ `MRT는 안정적인 평균값` → $1/\lambda_z^2$ 꼬리 오류와 입력 지연 흡수 → $V_{ss}$ 왜곡

<!-- SLIDE_START: C3 | title: Apex — CL, Vss, Vz와 투여 경로 보정 -->

## C3. Apex — CL, $V_{ss}$, $V_z$와 투여 경로 보정 [⚡ Apex Concept]

> **앞 카드에서 이 카드로:** C1의 AUC와 C2의 AUMC/MRT는 C3에서 CL과 분포용적이라는 임상 언어로 이름을 바꿉니다.

> **거장의 시각**  
> 💢 **흔한 오해:** NCA 표에 $CL$, $V_{ss}$, $V_z$가 나란히 있으면 같은 신뢰도의 파라미터처럼 읽기 쉽습니다.  
> ✅ **실제는:** $CL$은 AUC, $V_{ss}$는 AUC+AUMC+MIT, $V_z$는 AUC+$\lambda_z$의 오류를 서로 다른 방식으로 상속합니다.  
> 🎯 **체화할 단 하나의 직관:** C3의 숫자는 독립 계산값이 아니라 C1·C2 가정 오류가 임상 파라미터 이름으로 응결된 최종 형태입니다.

### A. 핵심 수식(Core Equations)

**청소율(Clearance)** [G p.149, Eq.2:325]

$$
\underbrace{CL}_{\text{정화부피/시간}}
=\frac{\underbrace{D_{iv}}_{\text{IV 용량}}}{\underbrace{AUC_0^\infty}_{\text{총 노출}}}
$$

**경구 겉보기 청소율(Oral Apparent Clearance)** [G p.149, Eq.2:326]

$$
\underbrace{CL_o}_{\text{CL/F}}
=\frac{\underbrace{CL}_{\text{실제 CL}}}{\underbrace{F}_{\text{흡수분율}}}
=\frac{\underbrace{D_{po}}_{\text{경구용량}}}{\underbrace{AUC_0^\infty}_{\text{총 노출}}}
$$

**생체이용률(Bioavailability)** [G p.149, Eq.2:327]

$$
\underbrace{F}_{\text{도달분율}}
=\overbrace{\frac{AUC_{po}}{AUC_{iv}}}^{\text{노출비}}
\cdot\overbrace{\frac{D_{iv}}{D_{po}}}^{\text{용량보정}}
$$

**정상상태 분포용적(Steady-State Volume of Distribution)** [G p.151, Eq.2:337]

$$
\underbrace{V_{ss}}_{\text{정상상태 V}}
=\overbrace{\underbrace{MRT}_{\text{보정 MRT}}\cdot\underbrace{CL}_{\text{정화}}}^{\text{체류×정화}}
=\frac{\underbrace{D_{iv}}_{\text{IV 용량}}\cdot\underbrace{AUMC_0^\infty}_{\text{시간가중 노출}}}{\underbrace{(AUC_0^\infty)^2}_{\text{노출제곱}}}
$$

**말단 분포용적(Terminal Volume)** [G p.151, Eq.2:338]

$$
\underbrace{V_z}_{\text{말단 V}}
=\frac{\underbrace{CL}_{\text{정화}}}{\underbrace{\lambda_z}_{\text{말단기울기}}}
=\frac{\underbrace{D_{iv}}_{\text{IV 용량}}}{\underbrace{AUC_0^\infty}_{\text{총 노출}}\cdot\underbrace{\lambda_z}_{\text{말단기울기}}}
$$

**유효 반감기(Effective Half-Life)** [G p.151]

$$
\underbrace{t_{1/2,eff}}_{\text{유효반감기}}
=\underbrace{\ln(2)}_{\text{50\% 변환}}\cdot\underbrace{MRT}_{\text{평균체류}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $CL$ | 부피/시간 | 약물을 제거하는 생리학적 능력 | AUC, 투여량, 신·간 기능 |
| $CL_o$ 또는 $CL/F$ | 부피/시간 | 생체이용률이 섞인 겉보기 청소율 | $F$, 경구 흡수, 초회통과 |
| $F$ | 무차원 | 투여량 중 전신순환 도달 분율 | 투여 경로, 흡수, 초회통과 |
| $V_{ss}$ | 부피 | 정상상태 분포 크기 | CL, MRT, AUMC 꼬리, MIT 보정 |
| $V_z$ | 부피 | 말단 기울기 기반 겉보기 부피 | CL, $\lambda_z$ 선택 |
| $t_{1/2,eff}$ | 시간 | 반복투여 축적 관점의 유효 반감기 | MRT |

💡 **V는 하나가 아니다** — $V_{ss}$는 체류시간과 정화능의 곱이고, $V_z$는 말단기울기와 정화능의 비입니다. 이름은 모두 volume이지만 질문이 다릅니다.  
⚠️ **헷갈림 방지:** $V_{ss}=MRT\cdot CL$에 쓰는 MRT가 입력 보정 전 값이면, 식은 맞아도 해석은 틀립니다.  
🔑 **Apex 규칙:** $CL$, $V_{ss}$, $V_z$를 읽기 전에 AUC 꼬리, AUMC 꼬리, MIT 보정, $\lambda_z$를 역추적합니다.

### B. C3가 Apex인 이유

C1이 AUC를 만들고, C2가 MRT를 만들고, C3가 이 둘을 CL과 분포용적(volume)으로 변환합니다. 따라서 C3의 오류는 독립 오류가 아닙니다. **앞선 두 카드의 오류가 임상 파라미터 이름을 달고 나타나는 최종 형태**입니다.

| 파라미터(Parameter) | 의존 항목(Depends on) | 주요 실패(Main failure) |
|---|---|---|
| $CL$ | 투여량(Dose), AUC | AUC 꼬리(tail) 오류가 청소율(clearance) 오류로 변합니다. |
| $V_{ss}$ | CL, MRT | 투여 경로 보정(input correction) 누락과 AUMC 꼬리(tail) 오류가 함께 들어옵니다. |
| $V_z$ | CL, $\lambda_z$ | 말단 기울기(terminal slope) 선택에 직접 묶입니다. |

### C. §2.8.8 특수 사례 — 반감기가 투여시간에 비해 짧은 경우

반감기(half-life)가 입력 시간(input time)에 비해 짧으면 표준(standard) MRT/$V_{ss}$ 계산이 불안정해질 수 있습니다. 여기서 핵심은 표준식이 “틀렸다”는 뜻이 아닙니다. 입력 기간(input duration)이 체류시간(residence time) 계산을 지배할 정도로 커지면서, 표준식이 유효하게 적용될 수 있는 조건을 벗어났다는 뜻입니다. Gabrielsson은 이 경우 정상상태 이후 washout AUC(washout AUC from steady state)를 이용한 대안식이 더 견고하며(robust), 0 또는 음수 $V_{ss}$를 피한다고 설명합니다. [G pp.157–158]

$$
\underbrace{V_{ss}}_{\text{대안 Vss}}
=\frac{\underbrace{K_0}_{\text{주입속도}}\cdot\underbrace{AUC_{t^*\to\infty}}_{\text{washout AUC}}}{\underbrace{C_{ss}^2}_{\text{농도제곱}}}
$$

$$
\underbrace{MRT}_{\text{washout MRT}}
=\frac{\underbrace{AUC_{t^*\to\infty}}_{\text{washout AUC}}}{\underbrace{C_{ss}}_{\text{정상상태 농도}}}
$$

위 식은 $T_{inf}$가 긴 상황에서 표준식만 붙잡으면 생기는 문제를 줄이기 위한 대안입니다. [G p.157, Eq.2:366/2:367]

💡 **비유:** 표준 $V_{ss}$ 식은 “입구가 짧고 몸 안 체류가 충분히 긴” 물탱크에서 수위를 재는 방식입니다. 주입 시간이 체류시간만큼 길어지면, 수위계는 탱크 크기보다 수도꼭지 개방 시간을 더 크게 읽게 됩니다.

> 💼 **실무 인사이트:** 표준 $V_{ss}$ 식(Eq.2:337)과 §2.8.8 대안식(Eq.2:366)을 함께 계산했을 때 값이 잘 맞으면 정상 적용 영역에 가깝습니다. 크게 벌어지면 입력 시간(input time)과 반감기(half-life)의 비율 자체가 문제라는 신호입니다. [G pp.151, 157]

### D. 한계(Limitations)

| 상황 | 파라미터 변화 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| Flip-flop kinetics(← 흡수가 제거보다 느려 말단기울기를 지배) | 경구 $\lambda_z$가 제거가 아니라 흡수를 반영 | → | $V_z$와 $V_{ss}$가 그럴듯한 양수로 잘못 출력 | IV/reference 정보 또는 흡수 제한 caveat 명시 |
| 비선형 소실(Nonlinear elimination) | CL과 $t_{1/2}$가 용량 의존적으로 변함 | → | 1차 파라미터 해석 실패 | capacity-limited model로 전환 [G p.664] |
| NCA-IIV | 잔차/오차 기여까지 IIV에 섞임 | → | PopPK $\omega^2$ 초기값 과대 | NCA 분산을 상한으로 보고 보수적 초기값 설정 |

> **NCA-volume 원자 노트(atom)**: $V_{ss}$는 “분포 부피 하나”가 아니라 $AUC$, $AUMC$, CL, 투여 경로 보정(input correction)이 모두 통과한 최종 요약값입니다. 따라서 $V_{ss}$를 볼 때는 항상 “어떤 MRT를 썼는가?”와 “입력 시간(input time)을 뺐는가?”를 같이 봐야 합니다. [G pp.149–157]

> 📖 **교과서 그림 참조:** Gabrielsson & Weiner 5e, p.157, Fig 2.126  
> C3 Apex에서 §2.8.8 대안식은 단순한 공식 대체가 아니라 적용 영역의 변경입니다. Washout AUC를 직접 보아야 입력 시간 지배(input-time-dominant) 상황에서 표준식이 왜 불안정해지는지 이해할 수 있습니다.  
> 확인 시점: C3 요약(Recap) 직후, C4로 넘어가기 전에 확인하면 됩니다.

### M. Plausible Fallacy — 나비효과 연쇄

**오류:** $V_{ss}$와 $V_z$가 양수·정상 단위로 출력되면 둘 중 더 그럴듯한 값을 분포용적으로 써도 된다고 판단한다.  
**왜 그럴싸한가:** 두 값 모두 NCA 표에서 volume 단위로 제시되고, 입력 보정이나 $\lambda_z$ 오염이 있어도 숫자 자체는 정상적인 형태로 보일 수 있습니다.  
**나비효과:** MIT 누락 또는 flip-flop $\lambda_z$ 오해 → $V_{ss}$/$V_z$ 해석 혼동 → [임상] 부하용량(loading dose) 또는 유지용량(maintenance dose) 정당화 오류, 협역 치료역 약물(digoxin, aminoglycoside)에서 초기 독성 가능성 → [모델링/규제] 표준 Eq.2:337과 §2.8.8 Eq.2:366 정합성 대조 누락, NDA submission의 loading dose 정당화 하자, 적용 영역 이탈에 대한 재분석 요구.

> **C3 체화 핵심**  
> ① `CL을 해석할 때` → AUC 꼬리와 투여량이 결정  
> ② `$V_{ss}$ vs. $V_z$ 혼동` → $V_{ss}$는 MRT/MIT, $V_z$는 $\lambda_z$가 지배  
> ⚡ `정상 단위의 volume이면 신뢰 가능` → 입력 보정·말단기 오류 은폐 → 부하용량·모델 초기값·규제 방어 실패

<!-- SLIDE_START: C4 | title: 노출 지표 — 투여량이 아니라 농도를 봅니다 -->

## C4. 노출 지표(Exposure metrics) — 투여량이 아니라 농도를 봅니다

> **앞 카드에서 이 카드로:** C3가 노출을 CL과 분포용적으로 번역했다면, C4는 그중 어떤 노출 지표가 PD/safety 질문에 맞는지 고릅니다.

> **거장의 시각**  
> 투여량(dose)을 반응의 중심에 두면 route, first-pass, 비선형 소실, 대사체, 단백결합이 만든 노출 차이를 놓칩니다.  
> Endpoint가 peak·cumulative·threshold·unbound 중 무엇을 묻는지 먼저 정하면 $C_{max}$, AUC, $C_{ss}$, $t_d$, $C_u$ 선택이 자연스럽게 정렬됩니다.

### A. 노출 지표(Exposure Measures)

§2.9의 핵심은 “투여량(dose)”보다 **전신 노출(systemic exposure)**, 특히 총 또는 비결합 전신 혈장 농도(total or unbound systemic plasma concentration)를 보라는 것입니다. 앞선 C1–C3가 노출(exposure)을 계산하고 파라미터로 변환하는 카드라면, C4는 그 노출 중 무엇을 PD/safety와 연결할지 고르는 카드입니다. 같은 투여량(dose)이라도 투여 경로(route), 초회통과(first-pass), 비선형 소실(nonlinear elimination), 활성 대사체(active metabolite), 단백 결합(protein binding), 투여 방식에 따라 실제 표적 노출(target exposure)은 달라집니다. [G pp.158–164]

| 지표(Metric) | 의미 | 사용 직관 | 출처(Source) |
|---|---|---|---|
| $C_{max}$ | 최고 노출(peak exposure) | 급성 독성(acute toxicity), peak-driven effect | [G p.163] |
| AUC | 총 노출(total exposure) | 누적 노출(cumulative exposure), extent 비교 | [G p.163] |
| $t_d$ | 역치(threshold) 이상 지속시간 | time-above-threshold 유형 판단 | [G p.163] |
| $C_{ss}$ / 평균 농도(average concentration) | 정상상태 강도(steady-state intensity) | 만성 투여 노출(chronic dosing exposure) | [G p.163] |
| 비결합 농도(unbound concentration) | 약리학적으로 사용 가능한 분율(pharmacologically available fraction) | 단백 결합(protein binding) 차이 비교 | [G p.163] |

$C_u=C_{total}\cdot f_u$는 일반 정의 보충이며, PDF의 직접 수식 인용으로 취급하지 않습니다. [G p.163; 정의 보충]

$$
\underbrace{C_u}_{\text{비결합농도}}
=\underbrace{C_{total}}_{\text{총농도}}\cdot\underbrace{f_u}_{\text{비결합률}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $C_{max}$ | 농도 | peak exposure | 흡수속도, 투여 방식, 분포 |
| AUC | 농도×시간 | total exposure | CL, F, 투여량 |
| $t_d$ | 시간 | threshold 이상 지속시간 | 농도-시간 곡선, threshold 설정 |
| $C_{ss}$ | 농도 | steady-state intensity | 투여간격, CL, 축적 |
| $C_u$ | 농도 | pharmacologically available concentration | $C_{total}$, 단백 결합률 $f_u$ |

💡 **노출 지표는 endpoint의 언어다** — 독성이 peak-driven이면 $C_{max}$, 누적 부담이면 AUC, threshold라면 $t_d$가 먼저 질문에 답합니다.  
⚠️ **헷갈림 방지:** 같은 총 농도라도 단백 결합이 다르면 비결합 농도 기준 효능 순위가 뒤집힐 수 있습니다. [G p.163]  
🔑 **선택 규칙:** dose를 먼저 보지 말고, endpoint mechanism을 먼저 정한 뒤 노출 지표를 고릅니다.

### B. §2.9 사례 압축

| 사례(Case) | 핵심 교훈 | 출처(Source) |
|---|---|---|
| 투여 경로/생체이용률(Route/bioavailability) | 용량-반응(dose-response)이 투여 경로(route) 차이로 흔들려도 농도-반응(concentration-response)은 정렬될 수 있습니다. | [G p.159] |
| 비선형 소실(Nonlinear elimination) | 투여량(dose) 증가는 노출(exposure)과 안전역(safety margin)을 비선형적으로 바꿉니다. | [G p.159] |
| 활성 대사체(Active metabolite) | 모약물 농도(parent concentration)만 보면 투여 경로 의존 반응(route-dependent response)을 오해할 수 있습니다. | [G p.160] |
| 투여 방식(Mode of administration) | 같은 일일 투여량(daily dose)이라도 주입/섭식 패턴(infusion/feeding pattern)이 독성(toxicity)을 바꿀 수 있습니다. | [G p.160] |
| 점유율/바이오마커(Occupancy/biomarker) | 리간드 농도(ligand concentration), 수용체 점유율(receptor occupancy), 바이오마커 반응(biomarker response)은 같은 축이 아닙니다. | [G p.161] |
| 반복 섭식(Repeated feeding) | 단회 투여(single-dose) + 섭식 시뮬레이션(feeding simulation)이 반복급여 노출을 과대예측할 수 있습니다. | [G p.162] |
| U자형 반응(U-shaped response) | 노출-반응(exposure-response)이 단조가 아니면 투여량(dose)만으로 효과를 예측할 수 없습니다. | [G p.162] |
| 단백 결합(Protein binding) | 총 농도(total concentration)와 비결합 농도(unbound concentration)는 효능 순위(potency ranking)를 뒤집을 수 있습니다. | [G p.163] |

### C. PK41 동적 출처 앵커(Dynamic Source Anchor) — NCA에서 비선형 회귀(nonlinear regression)로

Turbojoint® PK41은 한 지원자에게 310, 520, 780 µg·kg⁻¹을 각각 5시간 IV 주입(infusion)한 사례입니다. NCA에서 투여량(dose)이 증가할수록 CL은 1.6→0.9 L·h⁻¹·kg⁻¹로 감소했고, V는 2.3→1.8 L·kg⁻¹, MRT는 1.4→1.9 h로 변했습니다. [G pp.661–662]

이 패턴은 “용량 증량(dose escalation)에서 NCA-CL이 단조 감소하면 용량 제한 소실(capacity-limited elimination)을 의심하라”는 출처 고정 신호(source-anchored signal)입니다. 즉, 여기서 CL 감소는 단순히 표로 나열된 수치 하나가 아니라 모델 전환 신호입니다. 이후 모델은 다음과 같이 전환됩니다.

$$
\underbrace{V\cdot\frac{dC}{dt}}_{\text{체내변화}}
=\underbrace{In}_{\text{입력}}-\underbrace{CL\cdot C}_{\text{제거}},\qquad
\underbrace{CL}_{\text{농도의존 CL}}
=\frac{\underbrace{V_{max}}_{\text{최대제거}}}{\underbrace{K_m+C}_{\text{포화경계}}}
$$

💡 **비유:** 선형 CL은 배수구 지름이 일정한 욕조처럼 보이지만, Michaelis-Menten CL은 배수구가 포화되면서 물이 차오를수록 빠져나가는 비율이 달라지는 배수 시스템입니다. 용량이 커질수록 같은 “CL” 이름으로는 더 이상 배수 능력을 설명할 수 없습니다.

NCA 결과는 $V\approx2$ L/kg, $K_m\approx150$ µg/L, $V_{max}\approx310$ µg·h⁻¹·kg⁻¹ 등의 초기 추정값(initial estimate)을 제공합니다. 최종 추정값은 $V_{max}=184$ µg·h⁻¹·kg⁻¹, $K_m=83$ µg/L, $V=1.8$ L/kg이었습니다. 저자의 결론은 명확합니다. 용량 제한 1구획 시스템(capacity-limited one-compartment system)의 파라미터(parameters)는 CL과 V가 아니라 $V_{max}$, $K_m$, V이며, CL과 $t_{1/2}$는 혼합 0차/1차 동력학(mixed zero-/first-order kinetics)과 양립할 수 없습니다(incompatible). [G pp.663–664]

### D. 원자 노트와 그림 참조

> **노출 원자 노트(Exposure atom)**: 투여량(dose)은 투입량이고, 노출(exposure)은 몸(body) 또는 표적(target)이 실제로 본 농도-시간 부담(concentration-time burden)입니다. §2.9의 모든 사례는 “투여량이 같아도 노출이 다르면 반응(response)이 달라진다”는 한 문장으로 수렴합니다. [G pp.158–164]

> 📖 **교과서 그림 참조:** Gabrielsson & Weiner 5e, p.163, Fig 2.135  
> C4의 노출 지표(exposure metrics)는 단순 목록이 아닙니다. 그림을 통해 $C_{ss}$/평균 농도(average concentration), $C_{max}$, AUC, 역치 초과 노출(threshold-above exposure)/$t_d$가 서로 다른 약리학적 질문(pharmacologic question)에 답하는 요약값임을 분리할 수 있습니다.  
> 확인 시점: C4 요약(Recap) 직후, §5 혼동쌍(Confusion Pair)으로 넘어가기 전에 확인하면 됩니다.

> 📖 **교과서 그림 참조:** Gabrielsson & Weiner 5e, p.663, Fig 41.2  
> PK41의 핵심은 CL 감소가 숫자 한 줄이 아니라 모델 전환 신호(model transition signal)라는 점입니다. 이 그림(figure)이 없으면 학습자(learner)가 NCA-CL을 용량별 기술 표(dose별 descriptive table)로만 읽고, 비선형 회귀(nonlinear regression) 전환의 필연성을 약하게 느낄 수 있습니다.  
> 확인 시점: C4 요약(Recap) 직후 또는 Q4 자기 테스트(self-test) 전에 확인하면 됩니다.

> **C4 체화 핵심**  
> ① `endpoint가 peak-driven일 때` → $C_{max}$가 우선 지표  
> ② `총 농도 vs. 비결합 농도 혼동` → $C_u=C_{total}\cdot f_u$가 지배  
> ⚡ `dose가 같으면 response도 같다` → route·first-pass·비선형 소실·단백결합 차이를 무시 → exposure-response 정당화 실패

<!-- SLIDE_START: §5 | title: 혼동 쌍 해부 -->

# §5 — 혼동 쌍 해부(Confusion Pair Dissection)

## 쌍 1. AUC vs AUMC — 영차 모멘트 vs 일차 모멘트

| 비교 기준 | AUC | AUMC |
|---|---|---|
| 단위 / 차원 | 농도×시간 | 농도×시간² |
| 수식 내 위치 (분자/분모/지수) | 꼬리: $C_{last}/\lambda_z$ | 꼬리: $t_{last}C_{last}/\lambda_z+C_{last}/\lambda_z^2$ |
| 변화 원인 (생물학적/병적) | 농도 크기, CL, 표본추출 | 늦은 시간 농도, 꼬리 표본추출, $\lambda_z$ 오류 |
| 혼동 시 임상 결과 | 총 노출 비교와 CL 해석 왜곡 | MRT와 $V_{ss}$ 오류 증폭 |

**⚡ 기억 고리 (Memory Hook)**: AUC 꼬리(tail)는 $\lambda_z$의 1차 항 하나뿐이지만, AUMC 꼬리는 $1/\lambda_z$와 $1/\lambda_z^2$ 두 항이 동시에 들어갑니다. **시간이 한 번 더 가중되는 순간 후방 꼬리가 지배적이 됩니다** — 그래서 같은 말단 기울기(terminal slope) 오류라도 MRT와 $V_{ss}$로 흘러갈 때 더 강하게 증폭됩니다. [G pp.144–145]

**핵심 구분**: AUMC는 늦은 농도(late concentration)를 시간(time)으로 다시 가중하므로, 같은 말단 기울기(terminal slope) 오류라도 MRT와 $V_{ss}$에 더 민감하게 전달됩니다. [G pp.142–148]

$$
\overbrace{AUC_{tail}=\frac{C_{last}}{\lambda_z}}^{\text{1차 꼬리}}\qquad\text{vs}\qquad
\overbrace{AUMC_{tail}=\frac{t_{last}C_{last}}{\lambda_z}+\frac{C_{last}}{\lambda_z^2}}^{\text{시간가중 꼬리 + 민감도 증폭}}
$$

## 쌍 2. MRT vs $t_{1/2}$ — 평균 체류시간 vs 50% 감소시간

| 비교 기준 | MRT | $t_{1/2}$ |
|---|---|---|
| 단위 / 차원 | 시간 | 시간 |
| 수식 내 위치 (분자/분모/지수) | $AUMC/AUC$ 또는 MIT 보정 후 값 | $\ln(2)/\lambda_z$ |
| 변화 원인 (생물학적/병적) | 분포, 제거, 입력 시간 | 말단기울기, 제거 또는 흡수 지배 |
| 혼동 시 임상 결과 | 체류시간과 입력 지연을 반감기로 오해 | 다상 프로파일에서 단일 반감기 과해석 |

**⚡ 기억 고리 (Memory Hook)**: MRT는 *분자가 머문 시간의 평균*, $t_{1/2}$는 *농도가 절반이 되는 시간*입니다. 1구획 단일지수(monoexponential)에서는 $MRT=1/\lambda_z$, $t_{1/2}=\ln(2)/\lambda_z$로 단순한 비율 관계($1/\ln 2\approx 1.443$)이지만, 다구획에서는 **MRT가 분포기 정보까지 흡수하는 반면 $t_{1/2}$는 말단 기울기(terminal slope)만 기술합니다**. 이 때문에 유효 반감기(effective half-life)는 $\ln(2)\cdot MRT$로 다시 정의됩니다. [G p.151; T pp.789–793]

**핵심 구분**: MRT는 분포와 제거를 통합한 평균 시간이고, $t_{1/2}$는 말단 기울기(terminal slope)의 시간 척도입니다. 둘은 1구획 단일지수(one-compartment monoexponential) 상황에서 가까워질 수 있지만 같은 개념은 아닙니다. [G p.151; T pp.789–793]

$$
\underbrace{MRT}_{\text{체류시간 평균}}=\frac{\underbrace{AUMC}_{\text{시간가중 노출}}}{\underbrace{AUC}_{\text{총 노출}}},\qquad
\underbrace{t_{1/2}}_{\text{반감기}}=\frac{\underbrace{\ln(2)}_{\text{50\% 변환}}}{\underbrace{\lambda_z}_{\text{말단기울기}}}
$$

## 쌍 3. $V_{ss}$ vs $V_z$ — 정상상태 분포용적 vs 말단기울기 부피

| 비교 기준 | $V_{ss}$ | $V_z$ |
|---|---|---|
| 단위 / 차원 | 부피 | 부피 |
| 수식 내 위치 (분자/분모/지수) | $MRT\cdot CL$ 또는 $D_{iv}\cdot AUMC/(AUC)^2$ | $CL/\lambda_z$ 또는 $D_{iv}/(AUC\cdot\lambda_z)$ |
| 변화 원인 (생물학적/병적) | AUC, AUMC, CL, 투여 경로 보정 | AUC, CL, 말단 기울기 선택 |
| 혼동 시 임상 결과 | MIT 누락·AUMC tail 오류가 loading dose 논증으로 전파 | 잘못된 $\lambda_z$가 말단 부피를 부풀림 |

**⚡ 기억 고리 (Memory Hook)**: $V_{ss}$의 분모에는 $AUMC$와 투여 경로 보정(input correction)이 모두 들어오고, $V_z$의 분모에는 $AUC$와 $\lambda_z$만 들어갑니다. 따라서 **두 부피가 어긋나는 방향 자체가 어디서 가정이 흔들렸는지의 단서가 됩니다** — 표준 $V_{ss}$만 비정상적으로 부풀거나 음수에 가까워지면 투여 경로 보정 영역의 문제, $V_z$만 부풀면 말단 기울기(terminal slope) 영역의 문제입니다. [G pp.151, 157]

**치명적 타격(Critical Blow)**: $V_z$를 $V_{ss}$로 혼동하여 부하용량(loading dose)을 계산하면 실제 약물 분포 용량을 과대추정합니다. 다구획 약물에서 이 오류는 초기 독성 농도를 유발할 수 있으며, 특히 협역 치료역 약물(digoxin, aminoglycoside)에서 NDA submission의 loading dose 정당화에 결정적 하자가 됩니다. [EXPERT_INFERENCE, v3]

$$
\underbrace{V_{ss}}_{\text{정상상태 V}}=\underbrace{MRT}_{\text{체류시간}}\cdot\underbrace{CL}_{\text{정화}},\qquad
\underbrace{V_z}_{\text{말단 V}}=\frac{\underbrace{CL}_{\text{정화}}}{\underbrace{\lambda_z}_{\text{말단기울기}}}
$$

**§5 요약(Recap)**: 이 세션의 혼동쌍은 모두 “같아 보이는 요약 숫자” 문제입니다. AUC/AUMC, MRT/반감기(half-life), $V_{ss}/V_z$는 출력 표(output table)에서 가까이 있지만 서로 다른 질문에 답합니다.

> **숙련 해석 — [EXPERT_INFERENCE]**  
> 혼동쌍은 용어 암기 문제가 아니라 질문-파라미터 불일치 문제입니다. 같은 출력 표(output table) 안의 값이라도 ‘무엇을 묻는 숫자인가’를 바꾸면 해석 대상이 완전히 달라집니다.

<!-- SLIDE_START: §7 | title: 자기 테스트: 능동 회상 모듈 -->

# §7 — 자기 테스트: 능동 회상 모듈(Active Recall Module)

## Q1. 선형 사다리꼴 AUC와 로그-선형 사다리꼴 AUC의 수식을 쓰고, 각각의 적용 조건을 말해 보세요.

**정답**: 선형 규칙(linear rule)은 $\sum [(C_i+C_{i+1})/2]\Delta t$이며, 상승·평탄·하강 구간 모두 계산할 수 있지만 하강 구간에서 과대추정(overestimate)합니다. 로그-선형 규칙(log-linear rule)은 $(C_i-C_{i+1})/\ln(C_i/C_{i+1})\cdot\Delta t$이며, 하강 자료(descending data)에서만 유효합니다. $C_i=0$ 또는 $C_{i+1}=C_i$에서는 선형 대체(linear fallback)가 필요합니다. [G pp.143–145]

## Q2. $\lambda_z$ 추정의 최소 조건과 이상 조건은 무엇인가요?

**정답**: 최소 3–4개 말단 관측값(terminal observations)이 필요하고, 이상적으로는 말단기(terminal phase)에서 3–4 반감기(half-lives)가 경과해야 합니다. 관측 마지막 농도가 말단 회귀선(terminal regression line)에서 벗어나면 $\hat C_{last}$를 검토합니다. [G pp.146–147]

## Q3. 외삽 AUC(extrapolated AUC)가 총 AUC(total AUC)의 30%라면 어떻게 보고해야 하나요?

**정답**: Gabrielsson의 일반 권고 20–25%를 넘으므로, 최종적인 신뢰 파라미터처럼 쓰기보다 예비 추정값(preliminary estimate) 성격을 명시합니다. 추가 표본추출(sampling) 또는 말단기(terminal phase) 재검토가 필요합니다. [G p.148]

## Q4. PK41에서 NCA 결과가 비선형 회귀(nonlinear regression)의 초기 추정값(initial estimate)으로 전환되는 흐름을 설명해 보세요.

**정답**: Turbojoint®에서 310/520/780 µg·kg⁻¹ 5h IV 주입(infusion) 후 투여량(dose) 증가에 따라 NCA-CL이 1.6→0.9 L·h⁻¹·kg⁻¹로 감소했습니다. 이는 용량 제한 소실 신호(capacity-limited elimination signal)이며, NCA는 최종 CL 보고가 아니라 $V_{max}$, $K_m$, V를 갖는 Michaelis-Menten 회귀(regression)의 초기 추정값 앵커(initial estimate anchor)가 됩니다. 최종 추정값은 $V_{max}=184$ µg·h⁻¹·kg⁻¹, $K_m=83$ µg/L, $V=1.8$ L/kg이었습니다. [G pp.661–664]

> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** Q5–Q9는 MRT 단위, $CL/F$, endpoint별 노출, 비결합 농도, 대안식 판단을 통해 NCA 결과의 적용 경계를 묻는다.

---

## Q5. R&T Table H-1에서 $AUC=44.2$, $AUMC=177$이면 혈장 MRT(plasma MRT)는 얼마인가요?

**정답**: $MRT=AUMC/AUC=177/44.2\approx4.0$ hr입니다. 같은 예시에서 소변 MRT(urinary MRT) $\approx4.25$ hr, simulated MRT $\approx4.3$ hr로 일관됩니다. [T p.792]

## Q6. IV bolus에서 CL은 어떻게 계산하며, 경구(oral) 투여에서는 무엇이 달라지나요?

**정답**: IV bolus/IV 투여에서는 $CL=D_{iv}/AUC_0^\infty$입니다. 경구(oral)에서는 생체이용률(bioavailability)이 섞이므로 $CL/F=D_{po}/AUC_0^\infty$로 겉보기 청소율(apparent clearance)을 계산합니다. [G p.149]

## Q7. 급성 독성(acute toxicity), 누적 노출(cumulative exposure), 역치 기반 효과(threshold-driven effect)에는 각각 어떤 노출 지표(exposure metric)를 우선 볼까요?

**정답**: 급성 독성(acute toxicity)은 $C_{max}$, 누적 노출(cumulative exposure)은 AUC, 역치 기반 효과(threshold-driven effect)는 $t_d$ 또는 역치 초과 AUC(AUC above threshold)를 우선 봅니다. 실제 선택은 약물 기전(drug mechanism)과 반응 시간경과(response time course)에 맞춰 정당화해야 합니다. [G p.163]

## Q8. 총 농도(total concentration) 기준 효능 순위(potency ranking)와 비결합 농도(unbound concentration) 기준 순위가 달라질 수 있는 이유는 무엇인가요?

**정답**: 단백 결합이 다르면 총 농도(total concentration)가 같아도 약리학적으로 사용 가능한 비결합 농도(pharmacologically available unbound concentration)가 달라집니다. §2.9의 메시지는 총 농도보다 비결합 전신 노출(unbound systemic exposure)이 더 직접적인 비교 기준이 될 수 있다는 것입니다. [G p.163]

## Q9. 보스 딜레마(Boss Dilemma): 회사 SOP는 표준 Eq.2:337만 허용하지만, 반감기(half-life)가 입력 시간(input time)에 비해 매우 짧아 §2.8.8 대안식이 더 타당해 보입니다. 어떻게 처리해야 하나요?

**정답**: 표준식과 §2.8.8 대안식을 모두 계산해 차이를 제시하고, 차이의 원인이 $T_{inf}/t_{1/2}$ 비율에 있음을 설명합니다. SOP deviation은 “더 예쁜 결과”가 아니라 0 또는 음수 $V_{ss}$를 피하는 출처 기반 수학적 정당화(source-based mathematical justification)로 문서화합니다. [G pp.151, 157]

**§7 요약(Recap)**: Q1–Q3은 AUC 신뢰도, Q4는 비선형 전환, Q5–Q6은 NCA 계산, Q7–Q8은 노출(exposure) 해석, Q9는 C3 Apex의 적용 경계입니다.

---

> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** 전문가의 NCA 보고서는 숫자표가 아니라 $\lambda_z$에서 노출 지표까지 이어지는 가정 감사 추적 기록이다.

---

<!-- SLIDE_START: §8 | title: 메타프레임과 거시 구조 -->

# §8 — 메타프레임과 거시 구조(Meta-Frame & Big Picture)

## A. 위치 설정(Positioning)

NCA는 PopPK를 대체하는 분석이 아니라 모델링 전후에 활용하는 도구입니다. 모델 선택 전에는 EDA와 초기 추정값(initial estimate)을 만들고, 모델 추정 후에는 population prediction이 관측 노출(exposure)의 규모와 일관되는지 확인하는 기준점이 됩니다. 그러나 NCA는 선형 소실(linear elimination)을 가정합니다. 이 점을 잊으면 “단순해서 강한 방법”이 “단순해서 틀린 방법”으로 바뀝니다. [G p.141]

## B. 추적해야 할 실패 모드

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| 말단 기울기 오염(Terminal slope contamination) | $\lambda_z$ | → | AUC 꼬리, CL, $V_z$ 동시 왜곡 | selection plot, %extrapolated, $C_{last}$ 처리 기준 확인 [G pp.146–148] |
| 투여 경로 보정 누락(Input correction omission) | MIT, MRT | → | MRT와 $V_{ss}$가 실제 체류/분포보다 길거나 짧게 해석 | infusion/oral input time 보정 [G pp.149–151; T p.793] |
| NCA CL처럼 보이는 비선형 CL | CL | → | 용량별 최종 파라미터처럼 오해 | capacity-limited model 전환 [G pp.661–664] |
| NCA-IIV 과사용 | NCA-derived variability | → | PopPK $\omega^2$ inflation cascade, 공변량 회귀 신호 약화 | NCA 분산은 상한으로 보고 보수적 초기값 사용 |

> 💼 **실무 인사이트:** NCA 유래 변동성(NCA-derived variability)은 PopPK IIV의 직접 추정값이 아니라 잔차 변동성(residual variability)까지 섞인 상한입니다. 이 상한을 PopPK $\omega^2$의 초기값으로 그대로 입력하면 IIV가 RUV를 흡수하면서 후속 공변량 회귀(covariate regression)가 묻혀버릴 수 있습니다.

## C. 전문가 해석 지점(Professional Moat)

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| 보고서 검토 시작 | $\lambda_z$, %extrapolated, $C_{last}$ | → | AUC 표의 방어 가능성 결정 | AUC 표보다 먼저 선택 도표와 처리 기준 확인 |
| MRT/$V_{ss}$ 검토 | AUMC tail, MIT | → | 체류시간과 분포용적 해석 결정 | AUMC 꼬리와 MIT 보정 확인 |
| 비선형 전환 | NCA-CL vs dose | → | 용량 제한 소실 가능성 | PK41처럼 Michaelis-Menten 회귀 전환 검토 [G pp.661–664] |
| 노출 해석 | systemic/unbound concentration, AUC, $C_{max}$, $t_d$ | → | endpoint별 exposure-response 정당화 | 반응 기전에 맞는 metric 선정 [G pp.158–164] |
| 이중 $V_{ss}$ 공식 정합성 | Eq.2:337 vs Eq.2:366 | → | 표준식 적용 영역 진단 | 두 결과 일치 여부를 sanity check로 보고 [G pp.151, 157] |

## D. 후속 세션 연결 지식 그래프

| 후속 세션 | 이 세션에서 열리는 개념 | 이 세션 없으면 실패하는 것 |
|---|---|---|
| PopPK 초기 모수 설정 | NCA-derived CL, V, exposure anchor | 외삽 편향값을 NONMEM 초기값으로 투입 |
| 비선형 PK 회귀 | PK41의 capacity-limited signal | CL과 $t_{1/2}$를 1차 파라미터처럼 과해석 |
| BA/BE·clinical pharmacology 보고서 | $\lambda_z$, %extrapolated, exposure metric audit trail | 숫자표만 있고 가정 방어가 없는 보고서 |
| Exposure-response 분석 | endpoint별 $C_{max}$/AUC/$t_d$/$C_u$ 선택 | dose-only 해석으로 PD/safety 논증 실패 |

## E. 최종 압축 원칙(Final Compressed Doctrine)

NCA의 본질은 “모델을 쓰지 않는다”가 아니라 “최소한의 선형 소실 가정으로 면적과 시간 모멘트를 요약한다”입니다. AUC는 노출(exposure)의 출발점, AUMC는 체류시간(residence time)의 출발점, MRT는 $V_{ss}$의 출발점입니다. PK41은 이 모든 것이 비선형 동력학(nonlinear kinetics) 앞에서 초기 추정값(initial estimate)으로 격하되는 순간을 보여줍니다.

**§8 요약(Recap)**: 30년 pharmacometrics 연구자가 10분 핸드아웃에 남길 메시지는 하나입니다. NCA 출력 표(output table)를 믿기 전에 말단 기울기(terminal slope), 외삽 분율(extrapolated fraction), 투여 경로 보정(input correction), 용량 의존성(dose-dependence), 노출 지표(exposure metric) 선택을 순서대로 점검해야 합니다.

> 💼 **실무 인사이트 — [EXPERT_INFERENCE]**  
> 완성된 NCA 보고서는 숫자 표가 아니라 가정 감사 추적 기록(assumption audit trail)이어야 합니다. 독자가 말단 기울기(terminal slope), 꼬리 분율(tail fraction), 투여 경로 보정(input correction), 용량 의존성(dose-dependence), 노출 지표(exposure metric) 선택을 따라갈 수 있으면 이후 PopPK 모델링의 출발점으로도 방어 가능해집니다.

> **숙련 해석 — [CRUCIBLE_DERIVED]**  
> NCA 보고서의 1차 파라미터 자리에는 $AUC$가 아니라 $CL$ 또는 $CL/F$를 두고, $AUC$는 *노출 지표(exposure metric)*로 보고하는 것이 생리학적 해석성과 공변량(covariate) 회귀 가능성을 동시에 보존합니다. 보고 순서가 바뀌면 공변량 분석(covariate analysis)이 자연스럽게 이어지지 않아, 이후 PopPK 모델링에서 신·간 기능 공변량 신호가 약하게 나타날 수 있습니다.

# 출력 후 자가검증 체크리스트

| 항목 | 기준 | 결과 |
|---|---|---|
| SLIDE_START 개수 | §섹션수 + 카드수 합산 | 9 개 |
| 카드당 callout 합계 ≤ 6 | 전체 카드 | ✓ |
| [E] 박스 존재 | 모든 §2 카드 | ✓ |
| [D] 거장의 시각 존재 | 모든 §2 카드 | ✓ |
| [L] 파라미터 표 존재 | Apex 카드 + 정의 수식 카드 | ✓ |
| §5 혼동 쌍 표 행 순서 고정 (4행) | §5 전체 | ✓ |
| 기호 일관성 | 첫 등장 기준 통일 | ✓ |
| PART B 흔적 없음 | 전체 | ✓ |
| 수치 anchor 보존 | Compound A 등 원본 수치 | ✓ |
| [M] 나비효과 이중 종착점 | Apex 카드 전체 | ✓ |

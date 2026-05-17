# 비구획 분석(NCA) — AUC, AUMC, MRT, $V_{ss}$와 노출 평가의 실무 경계 — 보강본 v4.1

Turbojoint® PK41 사례부터 하나 짚고 갑니다. 한 지원자한테 **310 / 520 / 780 µg·kg⁻¹**을 각각 5시간 IV 주입했더니, 투여량을 올릴수록 **NCA로 계산한 청소율이 1.6 → 0.9 L·h⁻¹·kg⁻¹로 줄었어요.** 같은 표 안에서 V는 2.3 → 1.8 L·kg⁻¹, MRT는 1.4 → 1.9 h로 함께 움직였습니다. 이 장면 한 컷이 NCA 챕터 전체의 입장을 보여줘요 — **NCA 표는 최종 답이 아니라, $V_{max}$·$K_m$·V를 갖는 Michaelis-Menten 회귀로 넘어가기 위한 출발점입니다.** [G&W pp.661–664]

선행으로 알고 와야 할 건 $CL/V$ 정의, 1·2 구획 모델, Michaelis-Menten kinetics, $t_{1/2}=\ln(2)/k$ — 이 정도예요.

<!-- SLIDE_START: §1 | title: 세션 헤더와 로드맵 -->
<!-- SECTION_CORE: SC-01 -->

# §1 — 세션 헤더와 로드맵(Session Header & Roadmap)

**세션 제목**: 비구획 분석(NCA) — AUC, AUMC, MRT, $V_{ss}$와 노출 평가의 실무 경계
**출처**: Gabrielsson & Weiner 5e Ch.2 §2.8–§2.9, PK41; Rowland & Tozer 5e Appendix A·H, Ch.6 §BE, Ch.11 §Fluctuation, Ch.19 §Distribution Kinetics. [G&W pp.141–164, G&W pp.661–664; R&T pp.759–762, R&T pp.789–793; R&T pp.182–195(BE); R&T pp.276, 325, 340(다중투여·PTF); R&T pp.626, 632–636(gentamicin·$V_1$)]

### 핵심 통찰(Big Idea)

NCA를 흔히 "model-free"라고 하는데, 사실 더 정확한 표현은 **"compartment-free"**예요. 특정 구획 모델을 안 세워도 되긴 하지만, **채혈 구획에서 농도에 비례해 약물이 빠진다는 가정 — 선형 소실 — 은 그대로 필요합니다.** 그래서 PK41처럼 용량을 올릴수록 NCA-CL이 떨어지는 신호가 보이면, NCA 결과는 최종 해석값으로 굳어지면 안 되고 **비선형 회귀의 초기 추정값(initial parameter anchor)으로 내려와야 합니다.** [G&W p.141; G&W pp.661–664]

### 이 세션의 3층 구조

```text
Layer 1 — 무엇인가
  NCA → AUC → AUMC → MRT → CL/Vss/Vz → exposure metric

Layer 2 — 어떻게 계산되는가
  trapezoid + log-trapezoid → λz extrapolation → AUMC tail → MRT=AUMC/AUC → Vss=MRT·CL

Layer 3 — 언제, 왜 중요한가
  λz 방어 → 외삽률 방어 → MIT 보정 → 비선형 신호 감지 → endpoint별 exposure 선택
```

### 네 카드는 병렬이 아니라 직렬입니다

이 부분이 핵심이에요. C1·C2·C3·C4는 외울 항목 네 개가 아니라, **Phase 1 SAD/MAD EDA에서 실제로 작동하는 작업흐름의 네 단계**입니다. 각 단계의 오류는 다음 단계로 그대로 전파돼요.

| 단계 | 판단 질문 | 카드 | 오류 전파 |
|---|---|---|---|
| 1 | 면적이 믿을 만한가? | C1 $AUC/\lambda_z$/외삽 | AUC 오류 → CL, V, 노출 모두 왜곡 |
| 2 | 시간 모멘트가 안정적인가? | C2 AUMC/MRT | AUMC 꼬리 오류 → MRT와 $V_{ss}$ 왜곡 |
| 3 | 분포·청소 파라미터가 경로 보정됐는가? | C3 CL/$V_{ss}$/$V_z$ | MIT 누락 → $V_{ss}$ 해석 오류 |
| 4 | 어떤 노출 지표로 PD/safety를 볼 것인가? | C4 노출 지표 | dose-only 해석 → 노출-반응 판단 오류 |

🧭 **읽는 순서를 한 줄씩 풀면 이렇습니다:**
C1은 — AUC 숫자를 보기 전에 어떤 꼬리와 어떤 $\lambda_z$를 믿어야 할지 묻습니다. C2는 — 평균 체류시간이 왜 AUC보다 꼬리에 훨씬 민감한지 다룹니다. C3는 — AUC와 AUMC의 작은 오류가 어떻게 CL, $V_{ss}$, $V_z$라는 임상 파라미터로 굳어지는지 보여줍니다. C4는 — 이렇게 계산된 노출 중 어느 지표를 PD/safety 논증의 중심에 놓을지 정합니다.

**지식 그래프 위치:** `[선행: CL/V, 1·2 구획, Michaelis-Menten, t1/2] → [이 세션: NCA 면적·모멘트·노출 감사] → [후속: PopPK 초기 모수, 비선형 PK 회귀, BA/BE·clinical pharmacology 보고서]`

📖 **G&W p.141, Fig 2.113:** NCA(면적 합)와 회귀(파라미터화된 함수의 적합)가 같은 자료에 어떻게 다르게 작동하는지를 한 화면에 나란히 보여줍니다. PK41에서 NCA가 왜 "최종 답"이 아니라 회귀의 초기값으로 내려가야 하는지, 이 그림 한 장으로 정당화됩니다.

> 💼 **실무 인사이트** — NCA 출력 표는 위에서 한 줄씩 읽는 게 아니에요. **가정을 점검하는 순서**로 읽습니다: ① 말단 기울기와 외삽 비율을 먼저 보고 → ② MRT/투여 경로 보정을 확인하고 → ③ 그다음 CL·분포용적·노출 지표 해석으로 내려갑니다.

**§1 요약(Recap)**: NCA의 강점은 단순함이고, 약점도 같은 지점에서 나옵니다. 모델을 덜 세우는 대신 — 말단 기울기, 투여 경로 보정, 선형 소실 — 이 세 가정 중 하나만 무너져도 오류가 조용히 후속 분석으로 전파됩니다.

<!-- SLIDE_START: §2 | title: 개념 해부 카드 -->
<!-- SECTION_CORE: SC-02 -->

# §2 — 개념 해부 카드(Concept Anatomy Cards)

<!-- SLIDE_START: C1 | title: AUC 계산 — 선형/로그-선형 사다리꼴법, λz, 외삽 -->
<!-- SECTION_CORE: SC-03 -->

## C1. AUC 계산 — 선형/로그-선형 사다리꼴법(linear/log-linear trapezoidal rule), $\lambda_z$, 외삽(extrapolation) [⚡ Apex Concept]

NCA가 "model-free"라는 말 때문에, AUC를 데이터의 객관적인 면적값처럼 읽기 쉬워요. 그런데 실제로는 **AUC = 관측 사다리꼴 합 + $\lambda_z$ 기반 외삽 꼬리**, 두 덩어리예요. 말단기 선택을 잘못하거나 외삽률 방어가 무너지면, AUC 한 값만 흔들리는 게 아니라 CL · $V_z$ · $V_{ss}$가 같이 무너집니다. 그래서 AUC를 감사한다는 건 숫자값을 확인하는 일이 아니라, **말단 기울기 선택 → $C_{last}$ 처리 → 외삽 분율**이라는 세 단계의 처리 기록을 확인하는 일이에요.

### A. 형식적 정의(Formal Definition)

- **AUC(영차 모멘트 면적, zero moment area)**: 농도-시간 곡선 아래 면적. [G&W p.142]
- **$AUC_{0-t_{last}}$**: 관측 자료로 계산한 면적.
- **$AUC_{t_{last}\to\infty}$**: 마지막 측정 시점 이후를 단일지수 감소로 가정해 외삽한 꼬리 면적.
- **총 AUC(Total AUC)** = $AUC_{0-t_{last}}+AUC_{t_{last}\to\infty}$.

**선형 사다리꼴법(Linear Trapezoidal Rule)** [G&W p.143, Eq.2:310; R&T pp.759–760]

$$
\underbrace{AUC_0^{t_{last}}}_{\text{관측 AUC}}
=\sum_i \underbrace{\frac{C_i+C_{i+1}}{2}}_{\text{평균농도}}\cdot\underbrace{\Delta t}_{\text{시간폭}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $AUC_0^{t_{last}}$ | 농도×시간 | 관측 노출량 | 표본추출 시간, 농도 측정값 |
| $C_i$, $C_{i+1}$ | 농도 | 인접 시점 혈장 농도 | 흡수·분포·소실, 측정오차 |
| $\Delta t$ | 시간 | 구간 폭 | sampling design |
| $\lambda_z$ | 1/시간 | 말단 로그농도-시간 직선의 기울기 | 말단기 선택, 분포기 점 섞임, 비선형 소실 |
| $C_{last}$ 또는 $\hat C_{last}$ | 농도 | 마지막 관측 또는 회귀 기반 마지막 농도 | BLQ 처리, 회귀선 이탈 |
| $AUC_{total}$ | 농도×시간 | 관측+외삽 총 노출 | 관측 면적, 말단 외삽 |

R&T Table A-1의 일반 경구(generic oral) 50 mg 예시는 이 계산으로 **총 AUC = 26.60 mg·hr/L**이 나옵니다. ⚠️ 이 예시는 **zileuton이 아닙니다.** Zileuton은 R&T Table A-2의 600 mg 경구 자료셋이에요 — 두 표를 헷갈리지 않게 한 번 못 박고 갑니다. [R&T pp.759–762]

> 💡 사다리꼴 값은 농도와 간격의 곱일 뿐이라, 숫자가 깔끔하게 떨어져도 **말단 꼬리가 틀리면 전체 AUC 해석이 틀립니다.** 그리고 선형 방식은 본질적으로 **상승 구간에서 과소추정, 하강 구간에서 과대추정**해요. 이 편향은 표본추출 간격이 반감기에 비해 클수록 더 커집니다. [G&W p.142]

🔑 **AUC 보고 규칙:** AUC 값 하나만 쓰지 않습니다. $\lambda_z$, $C_{last}^{obs}$ vs $\hat C_{last}$, %extrapolated를 같이 둡니다.

### B. 수식 및 출처 고정 규칙

**로그-선형 사다리꼴법(Log-Linear Trapezoidal Rule)** [G&W pp.144–145, Eq.2:316; R&T p.761]

$$
\underbrace{AUC_i^{i+1}}_{\text{구간 AUC}}
=\underbrace{\frac{C_i-C_{i+1}}{\ln(C_i/C_{i+1})}}_{\text{로그평균농도}}\cdot\underbrace{\Delta t}_{\text{시간폭}}
$$

💡 **비유:** 하강 구간을 직선 판자로 덮어 면적을 재면 곡률을 무시하게 되는데, 로그-선형 평균은 곡선 기울기에 맞춘 얇은 천으로 덮는 방식이에요. 표본 간격이 길수록 곡률을 더 존중하게 됩니다.

적용 조건은 **하강 구간(descending data)**입니다. $C_i=0$ 또는 $C_{i+1}=C_i$인 구간에서는 로그-선형이 정의되지 않으니까, 그 구간만 선형으로 대체(linear fallback)합니다. [G&W p.144]

**혼합 방식(Mixed Approach)**: 증가/동일 구간은 선형, 감소 구간은 로그-선형으로 처리할 수 있어요. 다만 "항상 표준"이라고 단언하지는 않습니다 — 합리적으로 설계된 sampling에서는 두 방법의 차이가 임상적으로 작다는 저자의 균형도 같이 기억하면 됩니다. [G&W p.146]

**말단 외삽(Terminal Extrapolation)** [G&W pp.143–145, Eq.2:311/2:319]

$$
\underbrace{AUC_{t_{last}\to\infty}}_{\text{꼬리 AUC}}
=\frac{\underbrace{C_{last}\ \text{or}\ \hat C_{last}}_{\text{말단농도}}}{\underbrace{\lambda_z}_{\text{말단기울기}}}
$$

관측 $C_{last}$가 말단 회귀선에서 벗어나면, 관측값 대신 회귀 기반 예측값 $\hat C_{last}$를 쓰는 게 일반적인 권고예요. [G&W p.147]

**외삽 면적 비율(Percent Extrapolated Area)** [G&W p.148, Eq.2:324]

$$
\underbrace{\%Extrapolated}_{\text{외삽률}}
=\frac{\underbrace{AUC_{t_{last}\to\infty}}_{\text{꼬리 AUC}}}{\underbrace{AUC_{total}}_{\text{총 AUC}}}\times 100
$$

Gabrielsson 권고는 외삽 면적이 일반적으로 **총 AUC의 20–25%를 넘지 않는 것**입니다. 이를 넘기면 최종값이 아니라 **예비 추정값(preliminary estimate) 성격**으로 보고합니다. [G&W p.148]

### C. $\lambda_z$ 선정과 맥락 보충

말단 기울기는 반로그 도표에서 개별 프로파일을 보고 정해요. 최소 3–4개 관측값이 필요하고, 이상적으로는 말단기에서 **3–4 반감기**가 경과해야 합니다. [G&W p.146]

> 💼 **실무 인사이트:** 자동 NCA 출력의 $\lambda_z$ 구간은 그대로 믿지 말고 반로그 도표에서 직접 확인합니다. **adjusted $R^2$가 높다고 안심하면 안 돼요** — 분포기 점이 말단 기울기에 섞이면, AUC 꼬리뿐 아니라 CL · $V_z$ · $V_{ss}$까지 연쇄적으로 흔들립니다.

| 상황 | 파라미터 변화 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| 정상상태 투여 간격 | $AUC_{0-\tau,ss}$가 단회 $AUC_{0-\infty}$와 동등 취급 가능 | → | 반복투여 노출 비교 가능 | 잔류 면적과 다음 투여 외삽 면적의 상쇄를 설명 [G&W p.152] |
| LOQ 미만 값 | 0 또는 LOQ 대체 시 AUC 왜곡 | → | 말단기·외삽률 왜곡 | 결측(missing) 처리 원칙 적용 [G&W p.153] |
| AUC 단독 보고 | CL 생리학 연결 약화 | → | 공변량 회귀와 보고서 해석성 저하 | $CL$ 또는 $CL/F$를 1차 파라미터로 보고 [G&W p.148] |

### C-2. BLQ(정량 한계 미만) 처리 규칙 — 위치별 분기

LOQ 미만 처리는 단순히 "결측 처리"라는 한 줄로는 부족해요. 농도 곡선의 **어느 위치에서 발생한 BLQ인가**에 따라 처리 규칙이 분기됩니다. Gabrielsson 권고는 분명합니다 — **"회귀 관점에서, 특히 지수 모델에서는 LOQ 미만 농도를 0 등의 값으로 절대 대체해서는 안 되고, missing values로 처리하는 것이 LOQ나 0으로 대체하는 것보다 낫다."** [G&W p.153]

| BLQ 위치 | 통상 처리 규칙 | 처리 근거 | AUC/AUMC 영향 |
|---|---|---|---|
| **첫 정량 가능 시점 이전(pre-first quantifiable)** | 0으로 처리 (IV) 또는 결측(extravascular) | IV에서는 dose 직전 t=0 농도가 정의됨; 경구에서는 흡수 lag을 강제 0으로 가정하면 초기 AUC 왜곡 | 초기 AUC 약간 과소~정상 |
| **중간 BLQ(intervening)** | 선형 보간(linear interpolation) 또는 결측 | 0으로 두면 사다리꼴이 양쪽 관측값을 인공적으로 끌어내려 AUC 과소추정; 결측은 해당 구간을 trapezoid에서 제외 | 0 대체 시 AUC 과소 |
| **말단 BLQ(terminal)** | 결측 처리 권장 (또는 0) | 말단기 회귀에 BLQ가 포함되면 $\lambda_z$ 평탄화로 외삽 꼬리 과대; 0 대체는 지수 회귀에서 $\ln 0 = -\infty$로 수렴 불능 | 0 대체 시 $\lambda_z$ 왜곡 → 외삽률·CL·$V_z$ 연쇄 오류 |

$$
\underbrace{C_{BLQ}}_{\text{관측 BLQ}}\ \rightarrow\
\begin{cases}
\overbrace{0}^{\text{pre-first BLQ, IV}}\\[2pt]
\overbrace{\text{missing}}^{\text{intervening, terminal}}\\[2pt]
\overbrace{\text{linear interp.}}^{\text{intervening 대안}}
\end{cases}
$$

> 💼 **실무 인사이트:** BLQ 처리 규칙은 SOP나 SAP(Statistical Analysis Plan)에 **미리 명문화**해야 합니다. 분석 후에 규칙을 바꾸면 결과 데이터 마이닝(data dredging)으로 간주될 수 있어요. 특히 말단 BLQ를 어떻게 처리할지가 $\lambda_z$와 외삽 꼬리에 직접 들어오니까, BLQ 처리 규칙 → 말단기 점 선정 → $\lambda_z$ → AUC 꼬리 → CL/$V_z$로 오류가 연쇄 전파됩니다. **BLQ 처리 기록 없는 NCA 보고서는 그 자체로 감사 부적격**이에요.

🔑 **BLQ 보고 규칙:** NCA 표 옆에 BLQ 처리 알고리즘(pre-first/intervening/terminal 각각)을 명시합니다. 단순히 "LOQ 미만은 결측 처리"라고만 적으면 위치별 처리 분기가 검증되지 않습니다.

### D. 경계 조건

| 이 카드에서 다루는 것 | → | 후속 세션으로 이월 | 이유 |
|---|---|---|---|
| 선형 소실 | → | 비선형 PK 회귀 | 깨지면 $\lambda_z$와 외삽 AUC의 의미가 약해집니다. |
| 실제 terminal phase | → | PopPK 초기값 | 흡수/분포기를 말단기로 착각하면 꼬리가 왜곡됩니다. |
| 외삽 분율 ≤ 20–25% | → | BA/BE·임상약리 보고 | 초과 시 NCA 결과는 예비적 성격이 강해집니다. |
| 관측 $C_{last}$와 회귀선 일치 | → | CL/$V_z$ 계산 | 벗어나면 $\hat C_{last}$ 사용을 검토합니다. |

이 카드 핵심내용을 한 줄로 정리하면 — **AUC는 사다리꼴 합이 아니라 "사다리꼴 합 + $\lambda_z$ 기반 꼬리"입니다.** 그래서 AUC 검토는 값 자체가 아니라 **말단 기울기 선택, $\hat C_{last}$ 사용 여부, 외삽 면적 비율** 세 가지를 봅니다. [G&W pp.143–148]

📊 **개념 도식:** C1 AUC 감사 체인 — AUC 신뢰도는 사다리꼴 계산보다 말단 기울기와 외삽 꼬리 검증에서 결정되고, 그 오류는 CL/$V_z$/$V_{ss$로 그대로 전파됩니다.

NCA는 구획 모델을 안 세우니까 어떤 데이터에도 객관적인 면적 답을 준다 — 이 말이 그럴싸한 이유는, 결과가 사다리꼴 합과 모멘트 계산처럼 산술 요약으로 보이거든요. 모델 기반 오류에서 자유로워 보입니다. 하지만 $\lambda_z$ 선택 방어가 무너지거나 $\%AUC_{extrap}$이 20–25%를 넘는 순간, 외삽 꼬리가 관측 영역만큼이나 결과를 좌우합니다. 그러면 임상적으로는 CL·$V_z$·$V_{ss}$ 기반 용량·노출 해석이 왜곡되고, 모델링·규제 쪽으로는 PopPK 초기값에 편향이 들어가서 NONMEM 수렴 경로와 공변량 신호 강도가 흔들립니다. 결국 외삽 분율과 $\lambda_z$ 선택 근거에 대한 재분석 요구가 돌아옵니다.

<!-- SLIDE_START: C2 | title: AUMC와 MRT — 일차 모멘트와 평균 체류시간 -->
<!-- SECTION_CORE: SC-04 -->

## C2. AUMC와 MRT — 일차 모멘트(first moment)와 평균 체류시간

C1에서 "얼마나 노출되었는가"를 점검했다면, 이번엔 그 노출이 **"언제 일어났는가"**를 시간 가중으로 다시 묻습니다.

MRT를 안정된 평균값처럼 읽고 넘어가면 AUMC 꼬리의 $1/\lambda_z^2$ 민감도를 놓쳐요. AUMC를 **시간으로 가중한 노출**로 보면, 꼬리 표본추출과 MIT 보정이 MRT의 신뢰도를 곧바로 결정한다는 게 보입니다.

### A. 형식적 정의(Formal Definition)

- **AUMC**: $t\cdot C(t)$ 대 시간 곡선 아래 면적 — 즉 **일차 모멘트 면적**. [G&W p.142]
- **MRT**: 몸 또는 표본추출계 안에서 분자가 머무는 **평균 시간**. [R&T p.789]

R&T Appendix H는 분자량 300 g/mol인 약물 1 mg 안에 약 $2\times10^{18}$개의 분자가 있다는 직관에서 출발해서, **각 분자의 체류시간을 평균낸 값**을 MRT로 정의합니다. [R&T p.789]

**AUMC 선형 사다리꼴 계산** [G&W p.144, Eq.2:312]

$$
\underbrace{AUMC_0^{t_{last}}}_{\text{관측 AUMC}}
=\sum_i \underbrace{\frac{t_iC_i+t_{i+1}C_{i+1}}{2}}_{\text{시간가중 평균}}\cdot\underbrace{\Delta t}_{\text{시간폭}}
$$

**AUMC 꼬리(tail) 외삽** [G&W pp.144–145, Eq.2:313/2:320]

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
| $\lambda_z$ | 1/시간 | 말단기울기 | 말단기 선택, 분포기 점 섞임 |
| $MIT$ | 시간 | 평균 입력 지연시간 | IV bolus, infusion, extravascular input |

💡 **AUMC는 늦은 시간에 더 큰 무게를 얹는 값이에요.** 같은 농도라도 늦게 남아 있으면 시간 가중치가 붙어서 MRT와 $V_{ss}$를 더 크게 흔듭니다. "평균"이라는 단어 때문에 MRT가 안정적으로 보이지만, 계산상 **AUMC 꼬리와 $\lambda_z$ 오류를 그대로 상속**합니다.

🔑 **MRT 보고 규칙:** MRT 값 옆에 AUMC 외삽, MIT 보정, 입력 방식(input mode)을 같이 적습니다.

💡 **비유:** AUC가 하루 동안 받은 햇빛 총량이라면, **AUMC는 늦은 오후 햇빛에 더 무거운 추를 매단 저울**이에요. 해 질 무렵의 작은 측정 오차가 평균 체류시간을 크게 밀어냅니다.

### B. MRT 정의와 수치 앵커

**분자 정의(Molecular Definition)** [R&T p.789, Eq.H-1]

$$
\underbrace{MRT}_{\text{평균체류}}
=\frac{\underbrace{\sum_j t_j}_{\text{체류시간 합}}}{\underbrace{N}_{\text{분자수}}}
$$

**혈장 정의(Plasma Definition)** [R&T p.791, Eq.H-8]

$$
\underbrace{MRT}_{\text{혈장 MRT}}
=\frac{\underbrace{AUMC_0^\infty}_{\text{시간가중 노출}}}{\underbrace{AUC_0^\infty}_{\text{총 노출}}}
$$

R&T Table H-1의 수치 예시를 보면 $AUC=44.2$ mg·hr/L, $AUMC=177$ mg·hr²/L, 혈장 MRT $\approx 4.0$ hr, 소변 MRT $\approx 4.25$ hr, simulated MRT $\approx 4.3$ hr — **세 경로의 값이 서로 일관**됩니다. 이 일관성이 중요해요. 분자 수준 정의와 혈장/소변 계산 결과가 같은 곳에 수렴하니까 MRT가 단순한 비율 계산이 아니라 진짜 물리적 평균이라는 게 보입니다. [R&T p.792]

### C. 투여시간 보정(Input-Time Correction)

관측 MRT에는 약물이 전신순환에 들어오기까지 걸리는 **입력 시간**이 섞여 있어요. 이걸 그대로 두면 투여 과정이 만든 지연을 진짜 체류시간으로 착각하게 됩니다. 그래서 평균 입력 시간(MIT, mean input time — 투여가 만든 평균 지연시간)을 빼야 합니다. [G&W pp.149–151; R&T p.793]

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

경구 흡수에서 $K_a$는 단순 흡수만이 아니라 분해(degradation) 같은 병렬 과정을 포함할 수 있어요. 그래서 $1/K_a$를 "순수 흡수 시간"으로 과해석하면 안 됩니다. [G&W p.150]

### D. 맥락 확장과 경계 조건

대사체나 하류 구획에서는 $MBRT$에서 상류 입력 체류시간을 빼는 방식으로 $MDRT$를 정의합니다. 핵심은 체류시간이 **"공간별 고유 시간 + 입력 시간"으로 누적된다**는 점이에요. [G&W pp.155–156]

R&T는 소변 배설 자료에서도 MRT를 계산할 수 있다는 걸 보입니다. 다만 이 세션의 주축은 혈장 MRT예요 — "MRT는 혈장에서만 정의된다"는 오해를 막기 위해 이 한 줄을 둡니다. [R&T pp.790–792]

| 이 카드에서 다루는 것 | → | 후속 세션으로 이월 | 이유 |
|---|---|---|---|
| 꼬리 표본추출 | → | $V_{ss}$ 계산 | AUMC는 늦은 시간에 더 민감하므로 꼬리 부족이 MRT를 크게 흔듭니다. |
| $\lambda_z$ 신뢰 가능성 | → | CL/$V_z$ 해석 | $1/\lambda_z^2$ 항 때문에 AUMC 꼬리 민감도가 커집니다. |
| 입력 방식 | → | MIT 보정 | MIT 보정 누락 시 MRT와 $V_{ss}$가 함께 왜곡됩니다. |
| 선형 소실 | → | compartment-free 체류시간 해석 | 깨지면 MRT 해석이 흔들립니다. |

이 카드 핵심내용은 한 줄로 — **MRT는 반감기가 아니에요.** MRT는 "분자가 계 안에서 보낸 시간의 평균"이고, 계산상으로는 $AUMC/AUC$이며, 투여 경로에 따라 MIT를 빼야 비로소 해석 가능한 체류시간이 됩니다. [G&W pp.149–151; R&T pp.789–793]

📖 **G&W p.148, Fig 2.121 + R&T p.791, Fig H-2:** 농도 곡선과 일차 모멘트 곡선을 나란히 그려놓은 그림이에요. AUMC 꼬리의 영향은 수식만 봐서는 늦게 체화되니까, **곡선 두 개를 눈으로 비교**해야 "왜 늦은 시간 농도가 MRT를 그렇게 흔드는지"가 직관으로 자리 잡습니다.

MRT가 안정적인 평균값처럼 보이는 게 가장 흔한 함정이에요 — 평균이라는 단어가 주는 인상 때문이죠. 하지만 계산상으로는 $1/\lambda_z^2$ 꼬리 오류와 입력 지연을 그대로 흡수해버려서, MRT가 흔들리면 $V_{ss}$도 같이 무너집니다.

<!-- SLIDE_START: C3 | title: Apex — CL, Vss, Vz와 투여 경로 보정 -->
<!-- SECTION_CORE: SC-05 -->

## C3. Apex — CL, $V_{ss}$, $V_z$와 투여 경로 보정 [⚡ Apex Concept]

C1에서 만든 AUC와 C2에서 만든 AUMC/MRT는, C3에서 **CL과 분포용적이라는 임상 언어로 이름을 바꿉니다.** 그래서 C3는 독립 카드가 아니에요 — 앞 두 카드의 오류가 임상 파라미터 이름을 달고 나타나는 최종 형태예요.

NCA 표에 $CL$, $V_{ss}$, $V_z$가 나란히 출력되니까 셋 다 같은 신뢰도의 파라미터로 읽기 쉬워요. 그런데 셋이 상속하는 오류가 다 달라요 — **$CL$은 AUC 오류, $V_{ss}$는 AUC+AUMC+MIT 오류, $V_z$는 AUC+$\lambda_z$ 오류.** Vss가 가장 많은 가정 위에 얹혀 있다는 뜻이고, 그래서 제일 깨지기 쉽습니다.

### A. 핵심 수식(Core Equations)

**청소율(Clearance)** [G&W p.149, Eq.2:325]

$$
\underbrace{CL}_{\text{정화부피/시간}}
=\frac{\underbrace{D_{iv}}_{\text{IV 용량}}}{\underbrace{AUC_0^\infty}_{\text{총 노출}}}
$$

**경구 겉보기 청소율(Oral Apparent Clearance)** [G&W p.149, Eq.2:326]

$$
\underbrace{CL_o}_{\text{CL/F}}
=\frac{\underbrace{CL}_{\text{실제 CL}}}{\underbrace{F}_{\text{흡수분율}}}
=\frac{\underbrace{D_{po}}_{\text{경구용량}}}{\underbrace{AUC_0^\infty}_{\text{총 노출}}}
$$

**생체이용률(Bioavailability)** [G&W p.149, Eq.2:327]

$$
\underbrace{F}_{\text{도달분율}}
=\overbrace{\frac{AUC_{po}}{AUC_{iv}}}^{\text{노출비}}
\cdot\overbrace{\frac{D_{iv}}{D_{po}}}^{\text{용량보정}}
$$

**정상상태 분포용적(Steady-State Volume of Distribution)** [G&W p.151, Eq.2:337]

$$
\underbrace{V_{ss}}_{\text{정상상태 V}}
=\overbrace{\underbrace{MRT}_{\text{보정 MRT}}\cdot\underbrace{CL}_{\text{정화}}}^{\text{체류×정화}}
=\frac{\underbrace{D_{iv}}_{\text{IV 용량}}\cdot\underbrace{AUMC_0^\infty}_{\text{시간가중 노출}}}{\underbrace{(AUC_0^\infty)^2}_{\text{노출제곱}}}
$$

**말단 분포용적(Terminal Volume)** [G&W p.151, Eq.2:338]

$$
\underbrace{V_z}_{\text{말단 V}}
=\frac{\underbrace{CL}_{\text{정화}}}{\underbrace{\lambda_z}_{\text{말단기울기}}}
=\frac{\underbrace{D_{iv}}_{\text{IV 용량}}}{\underbrace{AUC_0^\infty}_{\text{총 노출}}\cdot\underbrace{\lambda_z}_{\text{말단기울기}}}
$$

**유효 반감기(Effective Half-Life)** [G&W p.151]

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

💡 **V는 하나가 아닙니다.** $V_{ss}$는 **체류시간 × 정화능**이고, $V_z$는 **정화능 ÷ 말단기울기**예요. 이름은 둘 다 volume인데 답하는 질문이 달라요. 그리고 $V_{ss}=MRT\cdot CL$에 쓰는 MRT가 **입력 보정 전 값이면 식은 맞아도 해석이 틀립니다.**

🔑 **Apex 규칙:** $CL$, $V_{ss}$, $V_z$를 읽기 전에 AUC 꼬리, AUMC 꼬리, MIT 보정, $\lambda_z$를 역추적합니다.

### B. C3가 Apex인 이유

C1이 AUC를 만들고, C2가 MRT를 만들고, C3가 이 둘을 **CL과 분포용적으로 변환**합니다. 그래서 C3의 숫자는 독립 계산값이 아니라, **앞선 두 카드의 가정 오류가 임상 파라미터 이름을 달고 굳어지는 최종 형태**예요.

| 파라미터 | 의존 항목 | 주요 실패 |
|---|---|---|
| $CL$ | 투여량, AUC | AUC 꼬리 오류가 청소율 오류로 변합니다. |
| $V_{ss}$ | CL, MRT | 투여 경로 보정 누락과 AUMC 꼬리 오류가 함께 들어옵니다. |
| $V_z$ | CL, $\lambda_z$ | 말단 기울기 선택에 직접 묶입니다. |

### C. §2.8.8 특수 사례 — 입력 시간이 반감기에 비해 매우 길 때

**입력 시간(T_inf)이 반감기($t_{1/2}$)에 비해 매우 길어지면** — 즉, infusion이 elimination을 우세하게 만들면 — 표준 MRT/$V_{ss}$ 계산이 불안정해질 수 있어요. 흔히 직관적으로 "반감기가 짧을 때"라고 표현되지만, 실제 식이 무너지는 **방향**은 **$T_{inf}/t_{1/2}$ 비율이 커질 때**예요. 입력 기간이 체류시간 계산을 지배할 만큼 커지면서 **표준식이 유효하게 작동하는 영역을 벗어났다**는 뜻이에요. 표준식이 **"틀렸다"**는 뜻이 아닙니다.

$$
\underbrace{\frac{T_{inf}}{t_{1/2}}}_{\text{입력/반감기 비율}}\uparrow\ \Rightarrow\
\underbrace{\frac{AUMC}{AUC}-\frac{T_{inf}}{2}}_{\text{표준 MRT 식, Eq.2:328}}\ \to\ 0\ \text{또는 음수}
$$

Gabrielsson은 이 경우 정상상태 이후 washout AUC를 이용한 대안식이 더 견고하고, **0이나 음수 $V_{ss}$를 피한다**고 설명합니다. [G&W pp.157–158]

$$
\underbrace{V_{ss}}_{\text{대안 Vss}}
=\frac{\underbrace{K_0}_{\text{주입속도}}\cdot\underbrace{AUC_{t^*\to\infty}}_{\text{washout AUC}}}{\underbrace{C_{ss}^2}_{\text{농도제곱}}}
$$

$$
\underbrace{MRT}_{\text{washout MRT}}
=\frac{\underbrace{AUC_{t^*\to\infty}}_{\text{washout AUC}}}{\underbrace{C_{ss}}_{\text{정상상태 농도}}}
$$

이 식들은 $T_{inf}$가 긴 상황에서 표준식만 붙잡으면 생기는 문제를 줄이는 대안이에요. [G&W p.157, Eq.2:366/2:367]

💡 **비유:** 표준 $V_{ss}$ 식은 "입구가 짧고 몸 안 체류가 충분히 긴 물탱크"의 수위를 재는 방식이에요. 주입 시간이 체류시간만큼 길어지면, 수위계는 탱크 크기보다 **수도꼭지를 얼마나 오래 열어뒀는지**를 더 크게 읽어버립니다.

> 💼 **실무 인사이트:** 표준 $V_{ss}$ 식(Eq.2:337)과 §2.8.8 대안식(Eq.2:366)을 함께 계산해서 **두 값이 잘 맞으면** 정상 적용 영역에 가까운 거예요. 크게 벌어지면 입력 시간과 반감기의 비율 자체가 문제라는 신호입니다. **벌어지는 방향은 한쪽 — $T_{inf}/t_{1/2}$ 비율이 커지는 쪽에서 표준식이 0 또는 음수 $V_{ss}$로 무너집니다.** [G&W pp.151, 157]

### D. 한계(Limitations)

| 상황 | 파라미터 변화 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| Flip-flop kinetics(흡수가 제거보다 느려 말단기울기를 지배) | 경구 $\lambda_z$가 제거가 아니라 흡수를 반영 | → | $V_z$와 $V_{ss}$가 그럴듯한 양수로 잘못 출력 | IV/reference 정보 또는 흡수 제한 caveat 명시 |
| 비선형 소실 | CL과 $t_{1/2}$가 용량 의존적으로 변함 | → | 1차 파라미터 해석 실패 | capacity-limited model로 전환 [G&W p.664] |
| NCA-IIV | 잔차/오차 기여까지 IIV에 섞임 | → | PopPK $\omega^2$ 초기값 과대 | NCA 분산을 상한으로 보고 보수적 초기값 설정 |

이 카드 핵심내용을 한 줄로 — **$V_{ss}$는 "분포 부피 하나"가 아니라, $AUC$·$AUMC$·CL·투여 경로 보정이 모두 통과한 최종 요약값입니다.** 그래서 $V_{ss}$를 볼 때마다 "어떤 MRT를 썼는가? 입력 시간을 뺐는가?"를 반드시 같이 봐야 합니다. [G&W pp.149–157]

📖 **G&W p.157, Fig 2.126:** washout AUC를 그림으로 직접 보여줘요. **§2.8.8 대안식은 단순한 공식 대체가 아니라 적용 영역의 변경**이라는 점은 이 그림이 없으면 잘 와닿지 않습니다 — 입력 시간이 지배적인 상황에서 표준식이 왜 불안정해지는지가 한 장에 담겨 있어요.

$V_{ss}$와 $V_z$가 둘 다 양수로 정상 단위에 출력되면, 더 그럴듯한 값을 분포용적으로 써도 된다고 생각하기 쉬워요. 두 값 모두 volume 단위로 같은 표에 나오니까, 입력 보정을 빼먹었거나 $\lambda_z$가 오염됐어도 숫자 모양은 멀쩡해 보입니다. 그런데 MIT 누락이나 flip-flop $\lambda_z$ 오해가 $V_{ss}$/$V_z$ 해석 혼동으로 이어지면, 임상에서는 부하용량이나 유지용량 정당화가 무너져요. 특히 **digoxin**(협역 치료역의 강심배당체로, 부정맥 치료에 쓰는 약 — 혈중 농도 폭이 매우 좁아서 조금만 높아도 독성, 조금만 낮으면 무효)이나 **aminoglycoside**(gentamicin·amikacin 같은 광범위 항생제 — 신독성과 이독성 때문에 협역 치료역에 들어가요) 같은 약물에서는 **초기 독성 농도**를 일으킬 수 있습니다. → 그래서 **분포용적 두 종류를 같은 신뢰도로 읽으면 안 된다**는 사실이 임상 안전성으로 직결되는 거예요. 모델링·규제 쪽으로는 표준 Eq.2:337과 §2.8.8 Eq.2:366 정합성 대조를 안 했다는 점이 잡혀서, NDA submission의 loading dose 정당화에 결정적 하자로 남고 적용 영역 이탈에 대한 재분석 요구로 돌아옵니다.

<!-- SLIDE_START: C4 | title: 노출 지표 — 투여량이 아니라 농도를 봅니다 -->
<!-- SECTION_CORE: SC-06 -->

## C4. 노출 지표(Exposure metrics) — 투여량이 아니라 농도를 봅니다

C3가 노출을 CL과 분포용적으로 번역했다면, C4는 그중 **어떤 노출 지표가 PD/safety 질문에 맞는지** 고르는 단계예요.

투여량(dose)을 반응의 중심에 두면 route, first-pass, 비선형 소실, 활성 대사체, 단백결합이 만든 노출 차이를 놓칩니다. **Endpoint가 peak·cumulative·threshold·unbound 중 무엇을 묻는지** 먼저 정하면, $C_{max}$, AUC, $C_{ss}$, $t_d$, $C_u$ 선택이 자연스럽게 정렬돼요.

### A. 노출 지표(Exposure Measures)

§2.9의 핵심은 "투여량(dose)"보다 **전신 노출(systemic exposure)**, 특히 **총 또는 비결합 전신 혈장 농도**를 보라는 거예요. C1–C3가 노출을 계산해 파라미터로 변환하는 카드라면, C4는 그 노출 중 무엇을 PD/safety와 연결할지 고르는 카드입니다. 같은 투여량이라도 투여 경로, 초회통과, 비선형 소실, 활성 대사체, 단백 결합, 투여 방식에 따라 **실제 표적 노출이 달라집니다.** [G&W pp.158–164]

| 지표(Metric) | 의미 | 사용 직관 | 출처 |
|---|---|---|---|
| $C_{max}$ | 최고 노출(peak exposure) | 급성 독성, peak-driven effect | [G&W p.163] |
| AUC | 총 노출(total exposure) | 누적 노출, extent 비교 | [G&W p.163] |
| $t_d$ | 역치 이상 지속시간 | time-above-threshold 유형 판단 | [G&W p.163] |
| $C_{ss}$ / 평균 농도 | 정상상태 강도 | 만성 투여 노출 | [G&W p.163] |
| 비결합 농도 $C_u$ | 약리학적으로 사용 가능한 분율 | 단백 결합 차이 비교 | [G&W p.163] |

$C_u=C_{total}\cdot f_u$는 일반 정의 보충이고, PDF의 직접 수식 인용은 아닙니다. [G&W p.163; 정의 보충]

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

💡 **노출 지표는 endpoint의 언어예요.** 독성이 peak-driven이면 $C_{max}$, 누적 부담이면 AUC, threshold라면 $t_d$가 먼저 질문에 답합니다. 그리고 **같은 총 농도라도 단백 결합이 다르면 비결합 농도 기준 효능 순위가 뒤집힐 수 있어요.** [G&W p.163]

🔑 **선택 규칙:** dose를 먼저 보지 말고, **endpoint mechanism**을 먼저 정한 뒤 노출 지표를 고릅니다.

### B. §2.9 사례 압축

| 사례 | 핵심 교훈 | 출처 |
|---|---|---|
| 투여 경로/생체이용률 | 용량-반응이 투여 경로 차이로 흔들려도 농도-반응은 정렬될 수 있습니다. | [G&W p.159] |
| 비선형 소실 | 투여량 증가는 노출과 안전역을 **비선형적으로** 바꿉니다. | [G&W p.159] |
| 활성 대사체 | 모약물 농도만 보면 투여 경로 의존 반응을 오해할 수 있습니다. | [G&W p.160] |
| 투여 방식 | 같은 일일 투여량이라도 주입/섭식 패턴이 독성을 바꿀 수 있습니다. | [G&W p.160] |
| 점유율/바이오마커 | 리간드 농도, 수용체 점유율, 바이오마커 반응은 **같은 축이 아닙니다.** | [G&W p.161] |
| 반복 섭식 | 단회 투여 + 섭식 시뮬레이션이 반복급여 노출을 과대예측할 수 있습니다. | [G&W p.162] |
| U자형 반응 | 노출-반응이 단조가 아니면 투여량만으로 효과를 예측할 수 없습니다. | [G&W p.162] |
| 단백 결합 | 총 농도와 비결합 농도는 효능 순위를 **뒤집을 수** 있습니다. | [G&W p.163] |

### B-2. 정상상태 NCA 노출 지표 — $AUC_{0-\tau,ss}$와 변동지수(fluctuation index)

§2.9의 단회투여 노출 지표들은 반복투여 정상상태에서 **dosing interval 내의 비교 가능한 지표**로 다시 정의돼야 해요. C1에서 잠깐 짚었듯이 정상상태에서는 **$AUC_{0-\tau,ss}$가 단회 $AUC_{0-\infty}$와 동등**합니다 — 이전 투여로 남은 잔류 면적과 현재 투여의 외삽 꼬리가 정확히 상쇄되거든요 [G&W p.152, Fig.2.122]. 그 위에 정상상태 특유의 정량 지표가 얹힙니다.

| 정상상태 지표 | 정의 | 임상적 질문 | 출처 |
|---|---|---|---|
| $AUC_{0-\tau,ss}$ | $\int_0^\tau C_{ss}(t)\,dt$ | dosing interval 내 누적 노출 (단회 $AUC_{0-\infty}$와 동등) | [G&W p.152] |
| $C_{av,ss}$ | $AUC_{0-\tau,ss}/\tau$ | 정상상태 평균 농도 (rate-equivalent intensity) | [R&T p.340] |
| $C_{max,ss}$, $C_{min,ss}$ | dosing interval 내 최고·최저 | peak/trough 안전성·효능 경계 | [R&T pp.276, 340] |
| **PTF% (Peak-Trough Fluctuation)** | $\dfrac{C_{max,ss}-C_{min,ss}}{C_{av,ss}}\times 100$ | 같은 평균에서 분할 횟수가 만든 농도 변동폭 | [R&T p.340, Fig.11-14] |
| 누적지수 $R_{ac}$ | $AUC_{ss}/AUC_{0-\tau,\text{single}}$ ≈ $1/(1-e^{-k\tau})$ | 단회 대비 정상상태에서 얼마나 축적되었나 | [R&T p.325, Eq.11-10] |

$$
\overbrace{\underbrace{PTF\%}_{\text{변동지수}}=\frac{\underbrace{C_{max,ss}-C_{min,ss}}_{\text{진폭}}}{\underbrace{C_{av,ss}}_{\text{평균}}}\times 100}^{\text{R\&T Eq. (Fig.11-14)}}
$$

PTF%의 핵심은 **같은 $C_{av,ss}$를 가진 두 regimen이라도 PTF%가 다르면 임상 결과가 다를 수 있다**는 거예요. 일일 용량이 같아도 q24h와 q8h는 PTF%가 크게 다르고, peak-driven 독성(예: aminoglycoside의 이독성·신독성)이나 trough-driven 효능(예: vancomycin의 AUC₂₄/MIC) 모두 이 차이에서 갈립니다. [R&T pp.276, 340]

> 💼 **실무 인사이트:** 정상상태 NCA 보고서에서 $C_{av,ss}$ 한 값만 보고하면 **PTF가 숨겨집니다.** "같은 평균 농도 = 같은 노출"이라는 단순화가 PTF% 차이를 가려요. PopPK 모델 검증에서도 simulation의 PTF가 관측 PTF를 재현하지 못하면, 흡수 모델(Ka)이나 분포 모델($V_c$/$Q$)이 underfit된 신호로 봅니다.

🔑 **정상상태 보고 규칙:** $AUC_{0-\tau,ss}$, $C_{av,ss}$, $C_{max,ss}$, $C_{min,ss}$, **PTF%**, $R_{ac}$를 한 세트로 보고합니다. 평균만 보고하면 분할 횟수가 만든 임상 차이가 사라져요.

### B-3. Partial AUC — modified-release vs immediate-release 비교의 정량 anchor

특정 시간 구간의 부분 면적($AUC_{0-t_1}$, $AUC_{t_1-t_2}$)이 전체 $AUC_{0-\infty}$와 별도로 보고되는 경우가 있어요. 가장 흔한 자리는 **modified-release(MR) vs immediate-release(IR) 비교**예요. 두 제형이 같은 $AUC_{0-\infty}$를 만들어도 **농도-시간 곡선의 모양**이 다르면 효과가 다를 수 있고, 이때 전체 면적은 같지만 **초기 노출(early exposure, $AUC_{0-t_{max,IR}}$)** 또는 **후기 노출(late exposure)**의 비교가 임상적으로 더 의미가 큽니다.

$$
\underbrace{AUC_{0-t_1}}_{\text{partial AUC}}
=\underbrace{\int_0^{t_1}C(t)\,dt}_{\text{구간 적분}}\
\overbrace{\neq}^{\text{일반적으로}}\
\underbrace{\frac{t_1}{\tau}\cdot AUC_{0-\infty}}_{\text{비례 가정}}
$$

§2.9의 "투여 방식(dosing pattern)" 사례 — 같은 일일 용량이라도 주입/섭식 패턴이 독성을 바꿀 수 있다는 메시지가 여기서 정량적으로 회수됩니다 [G&W p.160]. EMA의 modified-release BE 가이던스에서는 **early partial AUC**(예: $AUC_{0-t_{max,reference}}$)와 **late partial AUC**(예: $AUC_{t_{max,reference}-\tau}$)를 각각 90% CI 0.80–1.25 기준으로 검증하라고 합니다 — 전체 AUC만으로는 농도 곡선 모양 차이를 포착할 수 없으니까요.

| 비교 상황 | Partial AUC 선택 | 임상 함의 |
|---|---|---|
| MR vs IR (단회) | $AUC_{0-t_{max,IR}}$ (early) | 초기 노출 동등성 — onset of action |
| MR vs IR (단회) | $AUC_{t_{max,IR}-\tau}$ (late) | 후기 노출 동등성 — duration of action |
| Food effect | $AUC_{0-2h}$ 또는 $AUC_{0-4h}$ | 흡수 지연/촉진 정량 |
| Drug-drug interaction | onset 구간 partial AUC | 빠른 흡수 약물의 DDI 초기 노출 변화 |

> 💼 **실무 인사이트:** Partial AUC 보고가 누락된 MR vs IR 비교는 EMA 규제 심사에서 자주 보충 요구가 나옵니다. 같은 $AUC_{0-\infty}$로 BE를 통과해도 농도 곡선 모양이 다르면 임상 동등성이 보장되지 않으니까요. 그리고 partial AUC는 **dose-normalize한 비교**보다 **$t_{max,reference}$ 기준의 절대 시간 구간**으로 비교하는 게 표준입니다.

### C. PK41 동적 출처 앵커(Dynamic Source Anchor) — NCA에서 비선형 회귀로

Turbojoint® PK41은 **한 지원자에게 310, 520, 780 µg·kg⁻¹을 각각 5시간 IV 주입**한 사례입니다. NCA에서 투여량이 늘수록 CL은 1.6 → 0.9 L·h⁻¹·kg⁻¹로 줄었고, V는 2.3 → 1.8 L·kg⁻¹, MRT는 1.4 → 1.9 h로 변했어요. [G&W pp.661–662]

이 패턴이 알려주는 건 분명해요 — **"용량 증량에서 NCA-CL이 단조 감소하면 용량 제한 소실(capacity-limited elimination)을 의심하라"**는 출처 고정 신호예요. CL 감소는 표에 한 줄 더 적힌 숫자가 아니라 **모델을 바꿔야 한다는 신호**입니다. 모델은 이렇게 갈아끼웁니다:

$$
\underbrace{V\cdot\frac{dC}{dt}}_{\text{체내변화}}
=\underbrace{In}_{\text{입력}}-\underbrace{CL\cdot C}_{\text{제거}},\qquad
\underbrace{CL}_{\text{농도의존 CL}}
=\frac{\underbrace{V_{max}}_{\text{최대제거}}}{\underbrace{K_m+C}_{\text{포화경계}}}
$$

💡 **비유:** 선형 CL은 **배수구 지름이 일정한 욕조**처럼 작동합니다. 그런데 Michaelis-Menten CL은 **배수구가 포화되면서 물이 차오를수록 빠져나가는 비율이 떨어지는 배수 시스템**이에요. 용량이 커질수록 같은 "CL"이라는 이름으로는 더 이상 배수 능력을 설명할 수 없어요.

NCA 결과는 초기 추정값으로 $V\approx 2$ L/kg, $K_m\approx 150$ µg/L, $V_{max}\approx 310$ µg·h⁻¹·kg⁻¹ 등을 제공합니다. **최종 추정값은 $V_{max}=184$ µg·h⁻¹·kg⁻¹, $K_m=83$ µg/L, $V=1.8$ L/kg**이었어요. 저자의 결론은 분명합니다 — 용량 제한 1구획 시스템의 파라미터는 CL과 V가 아니라 $V_{max}$, $K_m$, V이며, **CL과 $t_{1/2}$는 혼합 0차/1차 동력학과 양립할 수 없습니다(incompatible).** [G&W pp.663–664]

### D. 정리와 그림 참조

투여량은 **투입량**이고, 노출은 **몸이나 표적이 실제로 본 농도-시간 부담**입니다. §2.9의 모든 사례는 한 문장으로 수렴해요 — **"투여량이 같아도 노출이 다르면 반응이 달라진다."** [G&W pp.158–164]

📖 **G&W p.163, Fig 2.135:** $C_{ss}$/평균 농도, $C_{max}$, AUC, 역치 초과 노출/$t_d$가 **서로 다른 약리학적 질문에 답하는 요약값**이라는 걸 한 화면에서 분리해서 보여줍니다. 노출 지표가 단순 목록이 아니라 endpoint별로 다른 도구라는 점이 이 그림에서 자리 잡힙니다.

📖 **G&W p.663, Fig 41.2:** PK41의 CL 감소가 **숫자 한 줄이 아니라 모델 전환 신호**라는 걸 시각적으로 못 박아주는 그림이에요. 이 그림이 없으면 학습자가 NCA-CL을 "용량별 기술 표"로만 읽고, 비선형 회귀로 전환해야 한다는 필연성을 약하게 느낍니다.

이 카드 핵심내용을 한 줄로 — **dose가 같아도 response가 같다는 보장은 없습니다.** route·first-pass·비선형 소실·단백결합·활성 대사체 — 이 다섯 가지가 dose와 effective exposure 사이에 끼어들어요. exposure-response를 정당화하려면 endpoint가 peak-driven인지, 누적인지, threshold인지, unbound인지부터 정해야 합니다.

<!-- SLIDE_START: §5 | title: 혼동 쌍 해부 -->
<!-- SECTION_CORE: SC-07 -->

# §5 — 혼동 쌍 해부(Confusion Pair Dissection)

지금까지 본 개념들 중에 출력 표에서 가까이 붙어 있어서 같은 종류처럼 보이지만 **사실은 다른 질문에 답하는 쌍들**을 마지막으로 짚고 갑니다.

## 쌍 1. AUC vs AUMC — 영차 모멘트 vs 일차 모멘트

| 비교 기준 | AUC | AUMC |
|---|---|---|
| 단위 / 차원 | 농도×시간 | 농도×시간² |
| 수식 내 위치 (분자/분모/지수) | 꼬리: $C_{last}/\lambda_z$ | 꼬리: $t_{last}C_{last}/\lambda_z+C_{last}/\lambda_z^2$ |
| 변화 원인 (생물학적/병적) | 농도 크기, CL, 표본추출 | 늦은 시간 농도, 꼬리 표본추출, $\lambda_z$ 오류 |
| 혼동 시 임상 결과 | 총 노출 비교와 CL 해석 왜곡 | MRT와 $V_{ss}$ 오류 증폭 |

**⚡ 기억 고리 (Memory Hook):** AUC 꼬리는 $\lambda_z$의 1차 항 하나뿐이지만, AUMC 꼬리는 **$1/\lambda_z$와 $1/\lambda_z^2$ 두 항이 동시에** 들어갑니다. 시간이 한 번 더 가중되는 순간 후방 꼬리가 지배적이 돼요 — 그래서 같은 말단 기울기 오류라도 **MRT와 $V_{ss}$로 흘러갈 때 더 강하게 증폭**됩니다. [G&W pp.144–145]

**핵심 구분:** AUMC는 늦은 농도를 시간으로 다시 가중하니까, 같은 말단 기울기 오류라도 MRT와 $V_{ss}$에 더 민감하게 전달됩니다. [G&W pp.142–148]

$$
\overbrace{AUC_{tail}=\frac{C_{last}}{\lambda_z}}^{\text{1차 꼬리}}\qquad\text{vs}\qquad
\overbrace{AUMC_{tail}=\frac{t_{last}C_{last}}{\lambda_z}+\frac{C_{last}}{\lambda_z^2}}^{\text{AUMC tail}}
$$

## 쌍 2. MRT vs $t_{1/2}$ — 평균 체류시간 vs 50% 감소시간

| 비교 기준 | MRT | $t_{1/2}$ |
|---|---|---|
| 단위 / 차원 | 시간 | 시간 |
| 수식 내 위치 (분자/분모/지수) | $AUMC/AUC$ 또는 MIT 보정 후 값 | $\ln(2)/\lambda_z$ |
| 변화 원인 (생물학적/병적) | 분포, 제거, 입력 시간 | 말단기울기, 제거 또는 흡수 지배 |
| 혼동 시 임상 결과 | 체류시간과 입력 지연을 반감기로 오해 | 다상 프로파일에서 단일 반감기 과해석 |

**⚡ 기억 고리 (Memory Hook):** MRT는 **분자가 머문 시간의 평균**, $t_{1/2}$는 **농도가 절반이 되는 시간**이에요. 1구획 단일지수(monoexponential)에서는 $MRT=1/\lambda_z$, $t_{1/2}=\ln(2)/\lambda_z$로 단순한 비율 관계($1/\ln 2\approx 1.443$)지만, 다구획에서는 **MRT가 분포기 정보까지 흡수하는 반면 $t_{1/2}$는 말단 기울기만 기술합니다.** 그래서 유효 반감기는 $\ln(2)\cdot MRT$로 다시 정의돼요. [G&W p.151; R&T pp.789–793]

**핵심 구분:** MRT는 분포와 제거를 통합한 평균 시간이고, $t_{1/2}$는 말단 기울기의 시간 척도예요. 1구획 단일지수 상황에서는 두 값이 가까워질 수 있지만 같은 개념은 아닙니다. [G&W p.151; R&T pp.789–793]

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

**⚡ 기억 고리 (Memory Hook):** $V_{ss}$의 분모에는 $AUMC$와 투여 경로 보정이 둘 다 들어오고, $V_z$의 분모에는 $AUC$와 $\lambda_z$만 들어가요. 그래서 **두 부피가 어긋나는 방향 자체가 어디서 가정이 흔들렸는지 알려주는 단서**가 됩니다 — 표준 $V_{ss}$만 비정상적으로 부풀거나 음수에 가까워지면 **투여 경로 보정 영역**의 문제, $V_z$만 부풀면 **말단 기울기 영역**의 문제예요. [G&W pp.151, 157]

**치명적 타격(Critical Blow):** $V_z$를 $V_{ss}$로 혼동해서 부하용량을 계산하면 실제 약물 분포 용량을 과대추정합니다. 다구획 약물에서 이 오류는 **초기 독성 농도**를 일으킬 수 있고, 특히 협역 치료역 약물 — 앞서 본 **digoxin**(강심배당체)이나 **aminoglycoside**(gentamicin·amikacin) — 에서는 **NDA submission의 loading dose 정당화에 결정적 하자**가 됩니다. → 그래서 NCA 표에서 $V$ 두 종류를 같은 신뢰도로 읽으면 안 된다는 원칙이 규제 방어로 직결되는 거예요.

⚠️ **임상 부하용량의 실제 기준은 $V_{ss}$가 아니라 $V_c$(혹은 $V_1$, initial dilution volume)입니다.** Gentamicin 같은 다구획 약물에서 부하용량을 $V_{ss}$로 산정하면 — $V_{ss}=V_c+V_t$이니까 — 초기 분포가 일어나기 전 **중앙구획 농도($C_0$)가 표적 농도를 크게 초과**해 일시적 peak 독성을 일으킬 수 있어요. R&T Chapter 19는 신부전 환자의 gentamicin 용량 조정에서 **terminal phase를 무시하고 V_1 기반으로 계산**하는 임상 관행을 명시합니다 [R&T pp.626, 632–636]. 정리하면:

$$
\underbrace{LD}_{\text{loading dose}}=
\overbrace{\underbrace{V_c}_{\text{중앙구획}}\cdot\underbrace{C_{target}}^{\text{표적 농도}}}^{\text{임상 표준 (협역, 다구획)}}
\ \leq\ \overbrace{V_{ss}\cdot C_{target}}^{\text{전신 분포 기준}}
\ \leq\ \overbrace{V_z\cdot C_{target}}^{\text{과대추정 위험}}
$$

따라서 **"$V_z$ vs $V_{ss}$" 비교만으로는 절반의 이야기**이고, 실제 협역 치료역 임상에서는 **세 부피의 위계($V_c \leq V_{ss} \leq V_z$)를 모두 의식**하면서 부하용량은 $V_c$ 기준, 유지용량은 $CL$ 기준, $V_{ss}$는 분포 평형 후 농도 해석 기준으로 분리해야 합니다 — 이 분리가 깨지면 디지털 환자의 안전성이 깨집니다. [G&W pp.66, 151; R&T pp.626, 632–636]

$$
\underbrace{V_{ss}}_{\text{정상상태 V}}=\underbrace{MRT}_{\text{체류시간}}\cdot\underbrace{CL}_{\text{정화}},\qquad
\underbrace{V_z}_{\text{말단 V}}=\frac{\underbrace{CL}_{\text{정화}}}{\underbrace{\lambda_z}_{\text{말단기울기}}}
$$

**§5 요약(Recap)**: 이 세션의 혼동쌍은 모두 **"같아 보이는 요약 숫자"** 문제예요. AUC/AUMC, MRT/반감기, $V_{ss}/V_z$는 출력 표에서 가까이 붙어 있지만 **서로 다른 질문에 답합니다.** 같은 표 안의 값이라도 "무엇을 묻는 숫자인가"를 바꾸면 해석 대상이 완전히 달라집니다.

<!-- SLIDE_START: §7 | title: 자기 테스트: 능동 회상 모듈 -->
<!-- SECTION_CORE: SC-08 -->

# §7 — 자기 테스트: 능동 회상 모듈(Active Recall Module)

## Q1. 선형 사다리꼴 AUC와 로그-선형 사다리꼴 AUC의 수식을 쓰고, 각각의 적용 조건을 말해 보세요.

**정답:** 선형 규칙은 $\sum [(C_i+C_{i+1})/2]\Delta t$이고, 상승·평탄·하강 구간 모두 계산할 수 있지만 하강 구간에서 과대추정합니다. 로그-선형 규칙은 $(C_i-C_{i+1})/\ln(C_i/C_{i+1})\cdot\Delta t$이고, 하강 자료에서만 유효합니다. $C_i=0$ 또는 $C_{i+1}=C_i$에서는 선형 대체가 필요합니다. [G&W pp.143–145]

## Q2. $\lambda_z$ 추정의 최소 조건과 이상 조건은 무엇인가요?

**정답:** 최소 3–4개 말단 관측값이 필요하고, 이상적으로는 말단기에서 3–4 반감기가 경과해야 합니다. 관측 마지막 농도가 말단 회귀선에서 벗어나면 $\hat C_{last}$를 검토합니다. [G&W pp.146–147]

## Q3. 외삽 AUC가 총 AUC의 30%라면 어떻게 보고해야 하나요?

**정답:** Gabrielsson의 일반 권고 20–25%를 넘으니까, 최종 신뢰 파라미터처럼 쓰지 말고 **예비 추정값** 성격을 명시합니다. 추가 표본추출 또는 말단기 재검토가 필요합니다. [G&W p.148]

## Q4. PK41에서 NCA 결과가 비선형 회귀의 초기 추정값으로 전환되는 흐름을 설명해 보세요.

**정답:** Turbojoint®에서 310/520/780 µg·kg⁻¹ 5h IV 주입 후 투여량 증가에 따라 NCA-CL이 1.6 → 0.9 L·h⁻¹·kg⁻¹로 감소했습니다. 이는 용량 제한 소실 신호이고, NCA는 최종 CL 보고가 아니라 $V_{max}$, $K_m$, V를 갖는 Michaelis-Menten 회귀의 **초기 추정값 앵커**가 됩니다. 최종 추정값은 $V_{max}=184$ µg·h⁻¹·kg⁻¹, $K_m=83$ µg/L, $V=1.8$ L/kg이었습니다. [G&W pp.661–664]

## Q5. R&T Table H-1에서 $AUC=44.2$, $AUMC=177$이면 혈장 MRT는 얼마인가요?

**정답:** $MRT=AUMC/AUC=177/44.2\approx 4.0$ hr입니다. 같은 예시에서 소변 MRT $\approx 4.25$ hr, simulated MRT $\approx 4.3$ hr로 일관됩니다. [R&T p.792]

## Q6. IV bolus에서 CL은 어떻게 계산하며, 경구 투여에서는 무엇이 달라지나요?

**정답:** IV bolus/IV 투여에서는 $CL=D_{iv}/AUC_0^\infty$입니다. 경구에서는 생체이용률(F)이 섞이니까 $CL/F=D_{po}/AUC_0^\infty$로 **겉보기 청소율(apparent clearance)**을 계산합니다. [G&W p.149]

## Q7. 급성 독성, 누적 노출, 역치 기반 효과에는 각각 어떤 노출 지표를 우선 볼까요?

**정답:** 급성 독성은 $C_{max}$, 누적 노출은 AUC, 역치 기반 효과는 $t_d$ 또는 역치 초과 AUC를 우선 봅니다. 실제 선택은 약물 기전과 반응 시간경과에 맞춰 정당화해야 합니다. [G&W p.163]

## Q8. 총 농도 기준 효능 순위와 비결합 농도 기준 순위가 달라질 수 있는 이유는 무엇인가요?

**정답:** 단백 결합이 다르면 총 농도가 같아도 **약리학적으로 사용 가능한 비결합 농도**가 달라집니다. §2.9의 메시지는 총 농도보다 **비결합 전신 노출**이 더 직접적인 비교 기준이 될 수 있다는 거예요. [G&W p.163]

## Q9. 보스 딜레마(Boss Dilemma): 회사 SOP는 표준 Eq.2:337만 허용하지만, **입력 시간($T_{inf}$)이 반감기에 비해 매우 길어** §2.8.8 대안식이 더 타당해 보입니다. 어떻게 처리해야 하나요?

**정답:** 표준식과 §2.8.8 대안식을 **둘 다 계산해서 차이를 같이 제시**하고, 차이의 원인이 $T_{inf}/t_{1/2}$ 비율에 있다는 걸 설명합니다. **방향을 명확히 — 비율이 커지는 쪽($T_{inf}\gg t_{1/2}$, infusion이 elimination을 우세하게 만드는 영역)에서 표준 MRT 식이 0이나 음수 $V_{ss}$로 무너집니다.** SOP deviation은 "더 예쁜 결과"가 아니라 **0이나 음수 $V_{ss}$를 피하는 출처 기반 수학적 정당화**로 문서화해요 — 보고서 안에 두 식의 출력 차이, $T_{inf}/t_{1/2}$ 비율, Eq.2:337 적용 영역 이탈 근거, 대안식 채택 사유를 한 박스에 넣어두면 감독관도 그대로 따라갈 수 있습니다. [G&W pp.151, 157]

## Q10. BLQ 값이 농도 곡선의 (a) 첫 정량 가능 시점 이전, (b) 중간 구간, (c) 말단에서 각각 나타날 때 어떻게 처리해야 하나요?

**정답:** (a) IV에서는 0 처리(t=0 시점이 정의됨), 경구에서는 흡수 lag을 강제 0으로 두면 초기 AUC가 왜곡되니까 결측 또는 보간 검토. (b) 중간 BLQ는 선형 보간 또는 결측 처리 — 0 대체는 양쪽 관측값을 인공적으로 끌어내려 AUC를 과소추정합니다. (c) 말단 BLQ는 결측 처리가 권장 — 0 대체는 $\ln 0 = -\infty$로 지수 회귀가 수렴하지 않고, BLQ를 말단 회귀에 포함시키면 $\lambda_z$가 평탄해져 외삽 꼬리가 과대됩니다. **Gabrielsson의 일반 원칙: "특히 지수 모델에서는 LOQ 미만 농도를 0 등의 값으로 절대 대체하지 말고 missing values로 처리"**입니다. [G&W p.153]

## Q11. 같은 일일 용량($D_{daily}$)을 q24h와 q8h로 나눠 줄 때, 평균 농도 $C_{av,ss}$는 같지만 임상 결과가 다를 수 있는 이유를 NCA 노출 지표로 설명해 보세요.

**정답:** $C_{av,ss}=D_{daily}/(CL\cdot 24h)$이므로 dosing interval과 무관해서 두 regimen에서 같습니다. 그런데 **PTF%(peak-trough fluctuation = $(C_{max,ss}-C_{min,ss})/C_{av,ss}\times 100$)**는 q24h에서 훨씬 큽니다 — interval이 길수록 peak는 높아지고 trough는 낮아지니까요. Peak-driven 독성(예: aminoglycoside 이독성·신독성)이나 trough-driven 효능(예: vancomycin AUC₂₄/MIC)은 PTF 차이에서 갈리고, 평균 한 값만 보고하면 이 정보가 사라집니다. [R&T p.340, Fig.11-14; pp.276, 325]

## Q12. 두 제형의 BE 검정에서 test/reference의 AUC 비율 90% CI가 0.88–1.18로 나왔습니다. 이 결과를 어떻게 해석하나요?

**정답:** **0.80–1.25 acceptance criterion 안에 90% CI가 완전히 들어가므로 bioequivalent로 선언**할 수 있습니다. 90% CI를 쓰는 이유는 BE가 TOST(two one-sided tests) 구조로 검정되기 때문이고, 각 측 α=0.05의 양측 합산이 90% CI에 대응합니다. 95% CI(0.85–1.21처럼 더 좁아진 경우라도 마찬가지로 0.80–1.25 안)는 BA 비교나 학술 보고에 쓰이고, BE 규제 판정의 기준은 90% CI입니다. 고변동성 약물(intra-subject CV>30%)에서는 reference-scaled framework로 acceptance bound가 확장될 수 있어요. [R&T pp.182–195]

**§7 요약(Recap)**: Q1–Q3은 AUC 신뢰도, Q4는 비선형 전환, Q5–Q6은 NCA 계산, Q7–Q8은 노출 해석, Q9는 C3 Apex의 적용 경계예요. Q10은 BLQ 처리 분기, Q11은 정상상태 PTF 차이, Q12는 BE 통계 판정 — 세 항목은 NCA가 PopPK/임상약리 실무로 넘어가는 접점입니다.

<!-- SLIDE_START: §8 | title: 메타프레임과 거시 구조 -->
<!-- SECTION_CORE: SC-09 -->

# §8 — 메타프레임과 거시 구조(Meta-Frame & Big Picture)

## A. 위치 설정(Positioning)

NCA는 PopPK를 **대체**하는 분석이 아니라 **모델링 전후에 활용하는 도구**예요. 모델 선택 전에는 EDA와 초기 추정값을 만들고, 모델 추정 후에는 population prediction이 관측 노출의 규모와 일관되는지 확인하는 기준점이 됩니다. 다만 NCA는 선형 소실을 가정합니다 — 이걸 잊는 순간 **"단순해서 강한 방법"이 "단순해서 틀린 방법"**으로 바뀝니다. [G&W p.141]

## B. 추적해야 할 실패 모드

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| 말단 기울기 오염 | $\lambda_z$ | → | AUC 꼬리, CL, $V_z$ 동시 왜곡 | selection plot, %extrapolated, $C_{last}$ 처리 기준 확인 [G&W pp.146–148] |
| 투여 경로 보정 누락 | MIT, MRT | → | MRT와 $V_{ss}$가 실제 체류/분포보다 길거나 짧게 해석 | infusion/oral input time 보정 [G&W pp.149–151; R&T p.793] |
| NCA CL처럼 보이는 비선형 CL | CL | → | 용량별 최종 파라미터처럼 오해 | capacity-limited model 전환 [G&W pp.661–664] |
| NCA-IIV 과사용 | NCA-derived variability | → | PopPK $\omega^2$ inflation cascade, 공변량 회귀 신호 약화 | NCA 분산은 상한으로 보고 보수적 초기값 사용 |

> 💼 **실무 인사이트:** NCA 유래 변동성은 PopPK IIV의 직접 추정값이 아니라 **잔차 변동성까지 섞인 상한**이에요. 이 상한을 PopPK $\omega^2$ 초기값으로 그대로 입력하면 **IIV가 RUV를 흡수하면서 후속 공변량 회귀가 묻혀버릴 수 있습니다.**

## C. 전문가 해석 지점(Professional Moat)

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| 보고서 검토 시작 | $\lambda_z$, %extrapolated, $C_{last}$ | → | AUC 표의 방어 가능성 결정 | AUC 표보다 먼저 선택 도표와 처리 기준 확인 |
| MRT/$V_{ss}$ 검토 | AUMC tail, MIT | → | 체류시간과 분포용적 해석 결정 | AUMC 꼬리와 MIT 보정 확인 |
| 비선형 전환 | NCA-CL vs dose | → | 용량 제한 소실 가능성 | PK41처럼 Michaelis-Menten 회귀 전환 검토 [G&W pp.661–664] |
| 노출 해석 | systemic/unbound concentration, AUC, $C_{max}$, $t_d$ | → | endpoint별 exposure-response 정당화 | 반응 기전에 맞는 metric 선정 [G&W pp.158–164] |
| 이중 $V_{ss}$ 공식 정합성 | Eq.2:337 vs Eq.2:366 | → | 표준식 적용 영역 진단 | 두 결과 일치 여부를 sanity check로 보고 [G&W pp.151, 157] |

## D. 후속 세션 연결 지식 그래프

| 후속 세션 | 이 세션에서 열리는 개념 | 이 세션 없으면 실패하는 것 |
|---|---|---|
| PopPK 초기 모수 설정 | NCA-derived CL, V, exposure anchor | 외삽 편향값을 NONMEM 초기값으로 투입 |
| 비선형 PK 회귀 | PK41의 capacity-limited signal | CL과 $t_{1/2}$를 1차 파라미터처럼 과해석 |
| BA/BE·clinical pharmacology 보고서 | $\lambda_z$, %extrapolated, exposure metric audit trail | 숫자표만 있고 가정 방어가 없는 보고서 |
| **BE 통계 검정** | $AUC_{0-\infty}$·$C_{max}$·partial AUC 산정 | **90% CI of geometric mean ratio가 0.80–1.25 acceptance criterion 내에 들어가는지** 검정 못함 [R&T pp.182–195] |
| Exposure-response 분석 | endpoint별 $C_{max}$/AUC/$t_d$/$C_u$ 선택 | dose-only 해석으로 PD/safety 논증 실패 |
| **PopPK 모델 검증(model validation chain)** | NCA 노출 anchor (관측 AUC/Cmax) | **VPC, CWRES, NPDE, Bayesian MAP** 진단에서 NCA observed exposure가 reference로 쓰이는데, NCA 외삽 편향이 들어가면 model misspecification 판정이 왜곡됨 |

📖 **BE 검정 보충 [R&T pp.182–184, Fig.6-13; Table 6-7 p.195]:** Test/Reference 비율의 **90% confidence interval**(log-transformed AUC와 $C_{max}$)이 **0.80–1.25 구간 안에** 들어가야 bioequivalent로 선언됩니다. 95% CI가 아니라 90% CI를 쓰는 이유는 양측 단측 검정(two one-sided tests, TOST)의 통계적 구조 때문이에요 — TOST에서 95% 신뢰성을 확보하려면 각 측에서 α=0.05 검정이 필요하고, 이게 양측 합쳐서 90% CI에 대응합니다. 고변동성 약물(highly variable drugs, intra-subject CV>30%)에서는 **reference-scaled average bioequivalence (RSABE)** framework이 적용돼 acceptance bound가 확장됩니다.

📖 **Model validation chain 보충:** NCA의 observed AUC/$C_{max}$는 PopPK 모델 적합성 검정의 **외부 reference**로 들어옵니다. **Visual Predictive Check(VPC)**의 관측 분포가 예측 분위수 안에 들어오는지, **Conditional Weighted Residuals(CWRES)**가 시간/예측에 대해 무작위 분포하는지, **Normalized Prediction Distribution Errors(NPDE)**의 분포가 N(0,1)을 따르는지 — 이 모든 진단에서 "관측 노출"의 reference가 NCA에서 옵니다. 그래서 **NCA 외삽 분율과 BLQ 처리 기록이 부실하면 PopPK 모델의 misspecification 판정 자체가 왜곡**됩니다. TDM 영역에서는 sparse data 상황에서 **Bayesian Maximum A Posteriori(MAP) estimation**이 개체 추정의 표준 도구이고, prior로 들어가는 population parameter의 신뢰도가 NCA-anchored 초기값에서 시작합니다.

## E. 최종 압축 원칙(Final Compressed Doctrine)

NCA의 본질은 **"모델을 쓰지 않는다"가 아니라 "최소한의 선형 소실 가정으로 면적과 시간 모멘트를 요약한다"**예요. AUC는 노출의 출발점, AUMC는 체류시간의 출발점, MRT는 $V_{ss}$의 출발점입니다. **PK41은 이 모든 것이 비선형 동력학 앞에서 초기 추정값으로 격하되는 순간**을 보여줍니다.

**§8 요약(Recap)**: 30년 pharmacometrics 연구자가 10분 핸드아웃에 남길 메시지는 하나예요 — NCA 출력 표를 믿기 전에 **말단 기울기 → 외삽 분율 → 투여 경로 보정 → 용량 의존성 → 노출 지표 선택**을 순서대로 점검합니다.

> 💼 **실무 인사이트:** 완성된 NCA 보고서는 **숫자 표가 아니라 가정 점검 기록**이어야 해요. 독자가 말단 기울기, 꼬리 분율, 투여 경로 보정, 용량 의존성, 노출 지표 선택을 따라갈 수 있으면, 이후 PopPK 모델링의 출발점으로도 방어 가능해집니다. 그리고 NCA 보고서의 1차 파라미터 자리에는 $AUC$가 아니라 **$CL$ 또는 $CL/F$**를 두고 $AUC$는 노출 지표로 보고하는 편이, **생리학적 해석성과 공변량 회귀 가능성을 동시에 보존**합니다 — 보고 순서가 바뀌면 이후 PopPK에서 신·간 기능 공변량 신호가 약하게 나타날 수 있어요.

<!--
# 출력 후 자가검증 체크리스트 (보강본 v4.1)

| 항목 | 기준 | 결과 |
|---|---|---|
| SLIDE_START 개수 | §섹션수 + 카드수 합산 | 9 개 (v4.0 동일) |
| 카드당 callout 합계 ≤ 6 | 전체 카드 | ✓ |
| 거장의 시각 산문 흡수 | 모든 §2 카드 | ✓ |
| 파라미터 표 존재 | Apex 카드 + 정의 수식 카드 | ✓ |
| §5 혼동 쌍 표 행 순서 고정 (4행) | §5 전체 | ✓ |
| 기호 일관성 | 첫 등장 기준 통일 | ✓ |
| 메타-언어 헤더 제거 | 전체 | ✓ |
| 수치 anchor 보존 | Turbojoint PK41 등 원본 수치 | ✓ |
| Plausible Fallacy 산문 통합 | Apex 카드 전체 | ✓ |
| 약물 3-step 즉맥락 | digoxin, aminoglycoside | ✓ |
| BLQ 처리 카드 (C1 §C-2) | 위치별 분기, G&W p.153 인용 | ✓ 신규 |
| §2.8.8 방향 명확화 (C3 §C) | T_inf↑ 방향 명시 | ✓ 수정 |
| V_c(V_1) 기준 loading dose (§5 쌍3) | R&T pp.626, 632–636 출처 | ✓ 신규 |
| 정상상태 노출 지표 (C4 §B-2) | AUC_τss, PTF%, R_ac 정의 | ✓ 신규 |
| Partial AUC (C4 §B-3) | MR vs IR 비교 | ✓ 신규 |
| BE 통계 + Model validation (§8 D) | 90% CI 0.80-1.25, VPC/CWRES/NPDE/MAP | ✓ 신규 |
| Q10–Q12 (자기 테스트) | BLQ, PTF, BE | ✓ 신규 |
| 모든 추가 수식 overbrace/underbrace 사용 | 보강 영역 전체 | ✓ |
| 보강 영역 외 원본 보존 | diff 검증 | ✓ |
-->

<!-- v3.9 → v4.0 변환 노트
- Voice rewrite: Park 교수 페르소나 적용, "~합니다/돼요/거든요" 호흡으로 강의체 통일
- 보존 감사:
  * SLIDE_START 마커: 9개 (§1, §2, C1-C4, §5, §7, §8)
  * 수식 블록($$): 22개 = v3.9 일치
  * 출처 anchor: [G&W p.xxx]/[R&T p.xxx] 모두 인라인 보존
  * 약물명·수치: Turbojoint PK41 (310/520/780 µg·kg⁻¹, CL 1.6→0.9, V 2.3→1.8, MRT 1.4→1.9, Vmax=184, Km=83, V=1.8), R&T Table A-1 (50 mg, total AUC 26.60), zileuton A-2 (600 mg), R&T Table H-1 (AUC=44.2, AUMC=177, MRT 4.0/4.25/4.3), digoxin·aminoglycoside 보존
- 주요 변환:
  * "거장의 시각" 💢/✅/🎯 정형 박스 → Park 교수 산문으로 흡수 (C1, C2, C3, C4)
  * "Plausible Fallacy — 나비효과 연쇄" 메타 헤더 → 산문 한 단락으로 통합 (C1, C3)
  * "Cn 체화 핵심" 박스 → "이 카드 핵심내용을 한 줄로" 산문 결론으로 흡수
  * "원자 노트(atom)" 콜아웃 → 카드 마지막 결론 문장으로 흡수
  * "빠른 읽기 경로" PART A 메타 안내 → 삭제
  * 약물명(digoxin, aminoglycoside) 첫 등장 시 §5 3-step 즉맥락 적용 + "→ 그래서 ~의 사례입니다" 닫음
  * Q9 보스 딜레마에 SOP deviation 문서화 절차 한 줄 보강
-->

<!-- v4.0 → 보강본 v4.1 변환 노트 (계량약리학 교수 검토 의견 반영)
교수 검토 의견(33개 항목 중 파일 06 관련) 알맞은 위치에 삽입, 나머지 원본 보존.

[I. 사실/논리 정밀화]
1) C3 §C — §2.8.8 적용 영역의 **방향** 명확화
   기존: "반감기가 입력 시간에 비해 매우 짧으면" → 보강: "T_inf가 t_{1/2}에 비해 매우 길어지면 (T_inf/t_{1/2} 비율이 커지는 쪽)에서 표준식이 0/음수 Vss로 무너진다" 명시
   출처: G&W pp.151, 157
2) §5 쌍 3 (Vss vs Vz) — V_z를 V_ss로 혼동 시 V_c(V_1) 기준 임상 부하용량 보강
   추가: "임상 부하용량 산정의 실제 기준은 V_c(V_1, initial dilution volume)이며 gentamicin 같은 협역 다구획 약물은 V_1 기반"
   수식: LD = V_c · C_target (overbrace로 단계별 위계 표기)
   출처: G&W pp.66, 151; R&T pp.626, 632–636

[III. 빠진 중요 내용 보강]
3) C1 §C-2 — BLQ 처리 규칙 (위치별 분기)
   pre-first quantifiable / intervening / terminal BLQ 처리 분기표 + Gabrielsson 권고문 직접 인용
   출처: G&W p.153
4) C4 §B-2 — 정상상태 NCA 노출 지표 정량 anchor
   AUC_{0-τ,ss}, C_av,ss, C_max,ss, C_min,ss, PTF%, R_ac 표 + PTF% 정의 수식 (overbrace)
   출처: G&W p.152 (AUC_τss); R&T p.340, Fig.11-14 (PTF); R&T p.325, Eq.11-10 (R_ac)
5) C4 §B-3 — Partial AUC와 MR vs IR 비교
   early/late partial AUC 정의 + EMA 가이던스 0.80-1.25 framework 언급
   수식: partial AUC ≠ 비례 (overbrace로 강조)
6) §8 D — BE 통계 검정 행 + Model validation chain(VPC, CWRES, NPDE, MAP) 행 추가
   출처: R&T pp.182–195

[IV. 자기 테스트 확장]
7) §7 Q10 (BLQ 위치별 처리), Q11 (PTF 차이), Q12 (BE 90% CI 판정) 추가
8) §7 요약(Recap) 업데이트

[기타]
9) §1 헤더 — 출처 박스에 R&T Ch.6/Ch.11/Ch.19 page span 추가
10) Q9 정답 — 방향(T_inf 길어질 때) 명시 강조

[수식 표기 규칙]
- 모든 추가 수식은 overbrace/underbrace 사용해 annotation
- 단위·생리학적 의미를 식 위/아래에 동시 표시

[보존 감사]
- v4.0 모든 §, 카드, 표, 수식, 출처 anchor 그대로 유지
- 보강 영역 외 문자열 변경 없음
- Turbojoint PK41 수치, R&T Table A-1/A-2/H-1 수치, digoxin·aminoglycoside 맥락 보존
- SLIDE_START 마커 9개 그대로 유지 (구조 변경 없이 §C-2, §B-2, §B-3 하위 단락으로 보강)
-->

---

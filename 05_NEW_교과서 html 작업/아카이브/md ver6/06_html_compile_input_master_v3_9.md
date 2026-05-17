# 비구획 분석(NCA) — AUC, AUMC, MRT, $V_{ss}$와 노출 평가의 실무 경계 — v3.8

Turbojoint® PK41 사례에서는 한 지원자에게 **310 / 520 / 780 µg·kg⁻¹**을 각각 5시간 IV 주입했더니, 투여량이 늘수록 **NCA-CL이 1.6 → 0.9 L·h⁻¹·kg⁻¹로 줄었습니다.** 같은 표 안에서 V는 2.3 → 1.8 L·kg⁻¹, MRT는 1.4 → 1.9 h로 움직였습니다. 이 장면이 알려주는 건 하나입니다 — NCA 표는 "최종 답"이 아니라, $V_{max}$·$K_m$·V를 갖는 Michaelis-Menten 회귀로 넘어가기 위한 **출발점**입니다. [G&W pp.661–664]

## 빠른 읽기 경로

PART A만 읽어도 핸드아웃으로 충분합니다. 시간이 부족하면 **C1 → C2 → C3 → C4 → §5 → §7** 순서로 읽으면 됩니다. 더 짧게는 **C1 → C3 → C4** 세 카드만 골라도 NCA 표를 감사하는 체계는 작동합니다.

| 카드 | 이 경로에서의 역할 |
|---|---|
| **C1** | AUC와 $\lambda_z$ — 면적이 믿을 만한지 |
| **C2** | AUMC와 MRT — 시간 모멘트가 안정적인지 |
| **C3** ⚡ | CL · $V_{ss}$ · $V_z$ — 분포·청소 파라미터가 경로 보정됐는지 |
| **C4** | 노출 지표 — 어떤 농도 요약으로 PD/safety를 볼지 |

**선행 지식**: $CL/V$ 정의, 1·2 구획 모델, Michaelis-Menten kinetics, $t_{1/2}=\ln(2)/k$.

<!-- SLIDE_START: §1 | title: 세션 헤더와 로드맵 -->
<!-- SECTION_CORE: SC-01 -->

# §1 — 세션 헤더와 로드맵(Session Header & Roadmap)

**세션 제목**: 비구획 분석(NCA) — AUC, AUMC, MRT, $V_{ss}$와 노출 평가의 실무 경계
**출처**: Gabrielsson & Weiner 5e Ch.2 §2.8–§2.9, PK41; Rowland & Tozer 5e Appendix A·H. [G&W pp.141–164, G&W pp.661–664; R&T pp.759–762, R&T pp.789–793]

### 핵심 통찰(Big Idea)

NCA는 흔히 "model-free"라고 부르지만, 더 정확하게는 **"compartment-free"**입니다. 특정 구획 모델을 안 세워도 되지만, **채혈 구획에서 농도에 비례해 빠진다는 가정(선형 소실)은 여전히 필요합니다.** 그래서 PK41처럼 용량을 올릴수록 NCA-CL이 떨어지는 신호가 보이면, NCA 결과는 최종 해석값이 아니라 **비선형 회귀의 초기 추정값(initial parameter anchor)**으로 내려와야 합니다. [G&W p.141; G&W pp.661–664]

### 이 세션의 3층 구조

```text
Layer 1 — 무엇인가
  NCA → AUC → AUMC → MRT → CL/Vss/Vz → exposure metric

Layer 2 — 어떻게 계산되는가
  trapezoid + log-trapezoid → λz extrapolation → AUMC tail → MRT=AUMC/AUC → Vss=MRT·CL

Layer 3 — 언제, 왜 중요한가
  λz 방어 → 외삽률 방어 → MIT 보정 → 비선형 신호 감지 → endpoint별 exposure 선택
```

### 개념 항법도 — 네 카드는 직렬 작업흐름입니다

Phase 1 SAD/MAD EDA에서 이 순서대로 작동합니다. 병렬 암기 목록이 아닙니다.

| 단계 | 판단 질문 | 카드 | 오류 전파 |
|---|---|---|---|
| 1 | 면적이 믿을 만한가? | C1 $AUC/\lambda_z$/외삽 | AUC 오류 → CL, V, 노출 모두 왜곡 |
| 2 | 시간 모멘트가 안정적인가? | C2 AUMC/MRT | AUMC 꼬리 오류 → MRT와 $V_{ss}$ 왜곡 |
| 3 | 분포·청소 파라미터가 경로 보정됐는가? | C3 CL/$V_{ss}$/$V_z$ | MIT 누락 → $V_{ss}$ 해석 오류 |
| 4 | 어떤 노출 지표로 PD/safety를 볼 것인가? | C4 노출 지표 | dose-only 해석 → 노출-반응 판단 오류 |

🧭 **읽는 순서:**
카드 1 (C1): AUC 숫자를 보기 전에 어떤 꼬리와 어떤 $\lambda_z$를 믿어야 하는가?
카드 2 (C2): 평균 체류시간이라는 값이 왜 AUC보다 꼬리에 더 민감한가?
카드 3 (C3): AUC와 AUMC의 작은 오류가 어떻게 CL, $V_{ss}$, $V_z$라는 임상 파라미터로 굳어지는가?
카드 4 (C4): 계산된 노출 중 어느 지표를 PD/safety 논증의 중심에 놓아야 하는가?

**지식 그래프 위치:**
`[선행: CL/V, 1·2 구획, Michaelis-Menten, t1/2] → [이 세션: NCA 면적·모멘트·노출 감사] → [후속: PopPK 초기 모수, 비선형 PK 회귀, BA/BE·clinical pharmacology 보고서]`

📖 **Gabrielsson & Weiner 5e, p.141, Fig 2.113**: 이 그림은 NCA(면적 합)와 회귀(파라미터화된 함수의 적합)를 나란히 놓아 둘의 본질적 차이를 보여줍니다. PK41에서 NCA가 왜 "최종 답"이 아니라 회귀의 초기값으로 내려가야 하는지, 이 그림 한 장으로 정당화됩니다.

> 💼 **실무 인사이트** — NCA 출력 표는 표 위에서부터 한 줄씩 읽는 게 아닙니다. **가정을 점검하는 순서**로 읽습니다: ① 말단 기울기와 외삽 비율 → ② MRT/투여 경로 보정 → ③ CL·분포용적·노출 지표 해석.

**§1 요약(Recap)**: NCA의 강점은 단순함이고, 약점도 같은 지점에서 나옵니다. 모델을 덜 세우는 대신 — 말단 기울기, 투여 경로 보정, 선형 소실 — 이 세 가정 중 하나라도 무너지면 오류가 조용히 후속 분석으로 전파됩니다.

<!-- SLIDE_START: §2 | title: 개념 해부 카드 -->
<!-- SECTION_CORE: SC-02 -->

# §2 — 개념 해부 카드(Concept Anatomy Cards)

<!-- SLIDE_START: C1 | title: AUC 계산 — 선형/로그-선형 사다리꼴법, λz, 외삽 -->
<!-- SECTION_CORE: SC-03 -->

## C1. AUC 계산 — 선형/로그-선형 사다리꼴법(linear/log-linear trapezoidal rule), $\lambda_z$, 외삽(extrapolation) [⚡ Apex Concept]

> **거장의 시각**
> 💢 **흔한 오해:** NCA는 모델을 안 세우니까 AUC는 데이터의 "객관적 면적"이라고 생각하기 쉽습니다.
> ✅ **실제는:** AUC = **관측 사다리꼴 합 + $\lambda_z$ 기반 외삽 꼬리**입니다. 말단기 선택과 외삽률 방어가 무너지면 CL · $V_z$ · $V_{ss}$가 같이 무너집니다.
> 🎯 **체화할 한 줄:** AUC 감사는 숫자값이 아니라 **`말단 기울기 선택 → $C_{last}$ 처리 → 외삽 분율`이라는 감사 기록**입니다.

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

R&T Table A-1의 일반 경구(generic oral) 50 mg 예시는 이 계산으로 **총 AUC = 26.60 mg·hr/L**을 얻습니다. ⚠️ 이 예시는 **zileuton이 아닙니다**. Zileuton은 R&T Table A-2의 600 mg 경구 자료셋입니다 — 두 표를 헷갈리지 않도록 주의합니다. [R&T pp.759–762]

> 💡 **사다리꼴은 면적계가 아니라 감사 체인** — 선형 사다리꼴 값은 농도와 간격의 곱일 뿐이라, 숫자가 깔끔해 보여도 말단 꼬리가 틀리면 전체 AUC 해석이 틀립니다. 그리고 선형 방식은 **상승 구간에서 과소추정, 하강 구간에서 과대추정**합니다. 이 편향은 표본추출 간격이 반감기에 비해 클수록 커집니다. [G&W p.142]

🔑 **AUC 보고 규칙:** AUC 값만 쓰지 말고 $\lambda_z$, $C_{last}^{obs}$ vs $\hat C_{last}$, %extrapolated를 함께 둡니다.

### B. 수식 및 출처 고정 규칙

**로그-선형 사다리꼴법(Log-Linear Trapezoidal Rule)** [G&W pp.144–145, Eq.2:316; R&T p.761]

$$
\underbrace{AUC_i^{i+1}}_{\text{구간 AUC}}
=\underbrace{\frac{C_i-C_{i+1}}{\ln(C_i/C_{i+1})}}_{\text{로그평균농도}}\cdot\underbrace{\Delta t}_{\text{시간폭}}
$$

💡 **비유:** 하강 구간의 로그-선형 평균은 내리막 곡선을 직선 판자로 덮는 게 아니라, 곡선 기울기에 맞춘 얇은 천으로 덮는 방식입니다. 간격이 길수록 곡률을 더 존중합니다.

적용 조건은 **하강 구간(descending data)**입니다. $C_i=0$ 또는 $C_{i+1}=C_i$이면 로그-선형은 정의되지 않으므로 그 구간만 선형으로 대체(linear fallback)합니다. [G&W p.144]

**혼합 방식(Mixed Approach)**: 증가/동일 구간은 선형, 감소 구간은 로그-선형으로 처리할 수 있습니다. 단 "항상 표준"이라고 단언하지는 않습니다 — 합리적으로 설계된 sampling에서는 두 방법의 차이가 임상적으로 작다는 저자의 균형도 같이 기억하면 됩니다. [G&W p.146]

**말단 외삽(Terminal Extrapolation)** [G&W pp.143–145, Eq.2:311/2:319]

$$
\underbrace{AUC_{t_{last}\to\infty}}_{\text{꼬리 AUC}}
=\frac{\underbrace{C_{last}\ \text{or}\ \hat C_{last}}_{\text{말단농도}}}{\underbrace{\lambda_z}_{\text{말단기울기}}}
$$

관측 $C_{last}$가 말단 회귀선에서 벗어나면, 관측값 대신 회귀 기반 예측값 $\hat C_{last}$를 쓰는 게 일반적으로 권고됩니다. [G&W p.147]

**외삽 면적 비율(Percent Extrapolated Area)** [G&W p.148, Eq.2:324]

$$
\underbrace{\%Extrapolated}_{\text{외삽률}}
=\frac{\underbrace{AUC_{t_{last}\to\infty}}_{\text{꼬리 AUC}}}{\underbrace{AUC_{total}}_{\text{총 AUC}}}\times 100
$$

저자 권고는 외삽 면적이 일반적으로 **총 AUC의 20–25%를 넘지 않는 것**입니다. 이를 넘으면 예비 추정값(preliminary estimate) 성격으로 보고합니다. [G&W p.148]

### C. $\lambda_z$ 선정과 맥락 보충

말단 기울기는 반로그 도표에서 개별 프로파일을 보고 정합니다. 최소 3–4개 관측값이 필요하고, 이상적으로는 말단기에서 **3–4 반감기**가 경과해야 합니다. [G&W p.146]

> 💼 **실무 인사이트:** 자동 NCA 출력의 $\lambda_z$ 구간은 그대로 믿지 말고 반로그 도표에서 직접 확인해야 합니다. **adjusted $R^2$가 높다고 안심하면 안 됩니다** — 분포기 점이 말단 기울기에 섞이면 AUC 꼬리뿐 아니라 CL · $V_z$ · $V_{ss}$까지 연쇄적으로 흔들립니다.

| 상황 | 파라미터 변화 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| 정상상태 투여 간격 | $AUC_{0-\tau,ss}$가 단회 $AUC_{0-\infty}$와 동등 취급 가능 | → | 반복투여 노출 비교 가능 | 잔류 면적과 다음 투여 외삽 면적의 상쇄를 설명 [G&W p.152] |
| LOQ 미만 값 | 0 또는 LOQ 대체 시 AUC 왜곡 | → | 말단기·외삽률 왜곡 | 결측(missing) 처리 원칙 적용 [G&W p.153] |
| AUC 단독 보고 | CL 생리학 연결 약화 | → | 공변량 회귀와 보고서 해석성 저하 | $CL$ 또는 $CL/F$를 1차 파라미터로 보고 [G&W p.148] |

### D. 경계 조건과 원자 노트

| 이 카드에서 다루는 것 | → | 후속 세션으로 이월 | 이유 |
|---|---|---|---|
| 선형 소실 | → | 비선형 PK 회귀 | 깨지면 $\lambda_z$와 외삽 AUC의 의미가 약해집니다. |
| 실제 terminal phase | → | PopPK 초기값 | 흡수/분포기를 말단기로 착각하면 꼬리가 왜곡됩니다. |
| 외삽 분율 ≤ 20–25% | → | BA/BE·임상약리 보고 | 초과 시 NCA 결과는 예비적 성격이 강해집니다. |
| 관측 $C_{last}$와 회귀선 일치 | → | CL/$V_z$ 계산 | 벗어나면 $\hat C_{last}$ 사용을 검토합니다. |

> **NCA-AUC 원자 노트(atom)**: AUC는 사다리꼴 합이 아니라 **"사다리꼴 합 + $\lambda_z$ 기반 꼬리"**입니다. 그래서 AUC 검토의 핵심은 값 자체가 아니라 **말단 기울기 선택, $\hat C_{last}$ 사용 여부, 외삽 면적 비율**입니다. [G&W pp.143–148]

> 📊 **개념 도식 (HTML에서 렌더링):** C1 AUC 감사 체인 — AUC 신뢰도는 사다리꼴 계산보다 말단 기울기와 외삽 꼬리 검증에서 결정되며, 그 오류는 CL/$V_z$/$V_{ss}$로 전파됩니다.

### M. Plausible Fallacy — 나비효과 연쇄

**오류:** NCA는 구획 모델을 안 세우니까 어떤 데이터에도 "객관적인 면적 답"을 준다고 생각한다.
**왜 그럴싸한가:** 결과가 사다리꼴 합과 모멘트 계산처럼 보이니까, 모델 기반 오류에서 자유로운 산술 요약처럼 보입니다.
**나비효과:** $\lambda_z$ 선택 방어 실패 또는 $\%AUC_{extrap}>20$–$25\%$ → 외삽 꼬리가 관측 영역만큼 결과를 좌우 → **[임상]** CL·$V_z$·$V_{ss}$ 기반 용량·노출 해석 왜곡 → **[모델링/규제]** PopPK 초기값 편향, NONMEM 수렴 경로와 공변량 신호 강도 왜곡, 외삽 분율과 $\lambda_z$ 선택 근거에 대한 재분석 요구.

> **C1 체화 핵심**
> ① `AUC가 믿을 만한가?` → $\lambda_z$, $C_{last}$ 처리, 외삽률이 결정
> ② `관측 면적 vs. 외삽 면적 혼동` → 총 AUC가 아니라 꼬리 AUC가 신뢰도를 지배
> ⚡ `NCA는 assumption-free` → 선형 소실·말단기·표본추출 충분성 가정 누락 → CL/$V_z$/$V_{ss}$와 PopPK 초기값까지 오류 전파

<!-- SLIDE_START: C2 | title: AUMC와 MRT — 일차 모멘트와 평균 체류시간 -->
<!-- SECTION_CORE: SC-04 -->

## C2. AUMC와 MRT — 일차 모멘트(first moment)와 평균 체류시간

> **앞 카드에서 이 카드로:** C1이 "얼마나 노출되었는가"를 감사했다면, C2는 그 노출이 **"언제 발생했는가"**를 시간 가중으로 다시 묻습니다.

> **거장의 시각**
> MRT를 "안정된 평균값"처럼 읽으면 AUMC 꼬리의 $1/\lambda_z^2$ 민감도를 놓칩니다. AUMC를 **시간 가중 노출**로 보면, 꼬리 표본추출과 MIT 보정이 MRT의 신뢰도를 곧바로 결정한다는 점이 보입니다.

### A. 형식적 정의(Formal Definition)

- **AUMC**: $t\cdot C(t)$ 대 시간 곡선 아래 면적 — 즉 **일차 모멘트 면적**. [G&W p.142]
- **MRT**: 몸 또는 표본추출계 안에서 분자가 머무는 **평균 시간**. [R&T p.789]

R&T Appendix H는 분자량 300 g/mol인 약물 1 mg 안에 약 $2\times10^{18}$개의 분자가 있다는 직관에서 시작해, **각 분자의 체류시간을 평균낸 값**을 MRT로 정의합니다. [R&T p.789]

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

> 💡 **AUMC는 늦은 시간에 더 큰 무게를 얹습니다** — 같은 농도라도 늦게 남아 있으면 시간 가중치가 붙어 MRT와 $V_{ss}$를 더 크게 흔듭니다. "평균"이라는 단어 때문에 MRT가 안정적으로 보이지만, **계산상으로는 AUMC 꼬리와 $\lambda_z$ 오류를 그대로 상속**합니다.

🔑 **MRT 보고 규칙:** MRT 값 옆에는 AUMC 외삽, MIT 보정, 입력 방식(input mode)을 함께 적습니다.

💡 **비유:** AUC가 하루 동안 받은 햇빛의 총량이라면, **AUMC는 늦은 오후 햇빛에 더 무거운 추를 매단 저울**입니다. 해 질 무렵의 작은 오차도 평균 체류시간을 크게 밀어냅니다.

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

R&T Table H-1의 수치 예시는 $AUC=44.2$ mg·hr/L, $AUMC=177$ mg·hr²/L, 혈장 MRT $\approx 4.0$ hr, 소변 MRT $\approx 4.25$ hr, simulated MRT $\approx 4.3$ hr로 **세 경로의 값이 서로 일관**됩니다. [R&T p.792]

### C. 투여시간 보정(Input-Time Correction)

관측 MRT에는 약물이 전신순환에 들어오기까지 걸리는 **입력 시간**이 섞여 있습니다. 이대로 두면 투여 과정이 만든 지연을 진짜 체류시간으로 착각하게 됩니다. 그래서 평균 입력 시간(MIT, mean input time; 투여가 만든 평균 지연시간)을 빼야 합니다. [G&W pp.149–151; R&T p.793]

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

경구 흡수에서 $K_a$는 단순 흡수만이 아니라 분해(degradation) 같은 병렬 과정을 포함할 수 있습니다. 그래서 $1/K_a$를 "순수 흡수 시간"으로 과해석하지 않습니다. [G&W p.150]

### D. 맥락 확장과 경계 조건

대사체나 하류 구획에서는 $MBRT$에서 상류 입력 체류시간을 빼는 방식으로 $MDRT$를 정의합니다. 핵심은 체류시간이 **"공간별 고유 시간 + 입력 시간"으로 누적된다**는 점입니다. [G&W pp.155–156]

R&T는 소변 배설 자료에서도 MRT를 계산할 수 있음을 보입니다. 다만 이 세션의 주축은 혈장 MRT입니다 — "MRT는 혈장에서만 정의된다"는 오해를 막기 위해 이 한 줄을 둡니다. [R&T pp.790–792]

| 이 카드에서 다루는 것 | → | 후속 세션으로 이월 | 이유 |
|---|---|---|---|
| 꼬리 표본추출 | → | $V_{ss}$ 계산 | AUMC는 늦은 시간에 더 민감하므로 꼬리 부족이 MRT를 크게 흔듭니다. |
| $\lambda_z$ 신뢰 가능성 | → | CL/$V_z$ 해석 | $1/\lambda_z^2$ 항 때문에 AUMC 꼬리 민감도가 커집니다. |
| 입력 방식 | → | MIT 보정 | MIT 보정 누락 시 MRT와 $V_{ss}$가 함께 왜곡됩니다. |
| 선형 소실 | → | compartment-free 체류시간 해석 | 깨지면 MRT 해석이 흔들립니다. |

> **NCA-MRT 원자 노트(atom)**: MRT는 반감기가 아닙니다. MRT는 **"분자가 계 안에서 보낸 시간의 평균"**이고, 계산상으로는 $AUMC/AUC$이며, 투여 경로에 따라 MIT를 빼야 해석 가능한 체류시간이 됩니다. [G&W pp.149–151; R&T pp.789–793]

📖 **Gabrielsson p.148, Fig 2.121 + R&T p.791, Fig H-2**: 두 그림은 농도 곡선과 일차 모멘트 곡선을 나란히 보여줍니다. AUMC 꼬리의 영향은 수식만으로는 늦게 체화되니까, **곡선 두 개를 눈으로 비교**해야 "왜 늦은 시간 농도가 MRT를 그렇게 흔드는지"가 직관으로 자리 잡습니다.

> **C2 체화 핵심**
> ① `평균 체류시간을 보고할 때` → AUMC 꼬리와 MIT 보정이 결정
> ② `MRT vs. 반감기 혼동` → MRT는 분자 체류 평균, 반감기는 말단 감소 시간척도
> ⚡ `MRT는 안정적인 평균값` → $1/\lambda_z^2$ 꼬리 오류와 입력 지연 흡수 → $V_{ss}$ 왜곡

<!-- SLIDE_START: C3 | title: Apex — CL, Vss, Vz와 투여 경로 보정 -->
<!-- SECTION_CORE: SC-05 -->

## C3. Apex — CL, $V_{ss}$, $V_z$와 투여 경로 보정 [⚡ Apex Concept]

> **앞 카드에서 이 카드로:** C1의 AUC와 C2의 AUMC/MRT는 C3에서 **CL과 분포용적이라는 임상 언어로 이름을 바꿉니다.**

> **거장의 시각**
> 💢 **흔한 오해:** NCA 표에 $CL$, $V_{ss}$, $V_z$가 나란히 있으면 셋 다 같은 신뢰도의 파라미터처럼 읽기 쉽습니다.
> ✅ **실제는:** 셋은 서로 다른 오류를 상속합니다 — $CL$은 AUC 오류, $V_{ss}$는 AUC+AUMC+MIT 오류, $V_z$는 AUC+$\lambda_z$ 오류.
> 🎯 **체화할 한 줄:** C3의 숫자는 독립 계산값이 아니라 **C1·C2 가정 오류가 임상 파라미터 이름으로 응결된 최종 형태**입니다.

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

> 💡 **V는 하나가 아닙니다** — $V_{ss}$는 **체류시간 × 정화능**이고, $V_z$는 **정화능 ÷ 말단기울기**입니다. 이름은 둘 다 volume이지만 답하는 질문이 다릅니다. $V_{ss}=MRT\cdot CL$에 쓰는 MRT가 **입력 보정 전 값이면 식은 맞아도 해석이 틀립니다.**

🔑 **Apex 규칙:** $CL$, $V_{ss}$, $V_z$를 읽기 전에 AUC 꼬리, AUMC 꼬리, MIT 보정, $\lambda_z$를 역추적합니다.

### B. C3가 Apex인 이유

C1이 AUC를 만들고, C2가 MRT를 만들고, C3가 이 둘을 **CL과 분포용적으로 변환**합니다. 그래서 C3의 오류는 독립 오류가 아닙니다 — **앞선 두 카드의 오류가 임상 파라미터 이름을 달고 나타나는 최종 형태**입니다.

| 파라미터 | 의존 항목 | 주요 실패 |
|---|---|---|
| $CL$ | 투여량, AUC | AUC 꼬리 오류가 청소율 오류로 변합니다. |
| $V_{ss}$ | CL, MRT | 투여 경로 보정 누락과 AUMC 꼬리 오류가 함께 들어옵니다. |
| $V_z$ | CL, $\lambda_z$ | 말단 기울기 선택에 직접 묶입니다. |

### C. §2.8.8 특수 사례 — 반감기가 투여시간에 비해 짧은 경우

반감기가 입력 시간에 비해 짧으면 표준 MRT/$V_{ss}$ 계산이 불안정해질 수 있습니다. 여기서 핵심은 표준식이 **"틀렸다"**는 뜻이 아닙니다. 입력 기간이 체류시간 계산을 지배할 만큼 커지면서 **표준식이 유효하게 적용될 수 있는 영역을 벗어났다**는 뜻입니다. Gabrielsson은 이 경우 정상상태 이후 washout AUC를 이용한 대안식이 더 견고하고, **0이나 음수 $V_{ss}$를 피한다**고 설명합니다. [G&W pp.157–158]

$$
\underbrace{V_{ss}}_{\text{대안 Vss}}
=\frac{\underbrace{K_0}_{\text{주입속도}}\cdot\underbrace{AUC_{t^*\to\infty}}_{\text{washout AUC}}}{\underbrace{C_{ss}^2}_{\text{농도제곱}}}
$$

$$
\underbrace{MRT}_{\text{washout MRT}}
=\frac{\underbrace{AUC_{t^*\to\infty}}_{\text{washout AUC}}}{\underbrace{C_{ss}}_{\text{정상상태 농도}}}
$$

위 식은 $T_{inf}$가 긴 상황에서 표준식만 붙잡으면 생기는 문제를 줄이기 위한 대안입니다. [G&W p.157, Eq.2:366/2:367]

💡 **비유:** 표준 $V_{ss}$ 식은 **"입구가 짧고 몸 안 체류가 충분히 긴" 물탱크**의 수위를 재는 방식입니다. 주입 시간이 체류시간만큼 길어지면, 수위계는 탱크 크기보다 **수도꼭지 개방 시간**을 더 크게 읽습니다.

> 💼 **실무 인사이트:** 표준 $V_{ss}$ 식(Eq.2:337)과 §2.8.8 대안식(Eq.2:366)을 함께 계산해 **두 값이 잘 맞으면** 정상 적용 영역에 가깝습니다. 크게 벌어지면 입력 시간과 반감기의 비율 자체가 문제라는 신호입니다. [G&W pp.151, 157]

### D. 한계(Limitations)

| 상황 | 파라미터 변화 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| Flip-flop kinetics(흡수가 제거보다 느려 말단기울기를 지배) | 경구 $\lambda_z$가 제거가 아니라 흡수를 반영 | → | $V_z$와 $V_{ss}$가 그럴듯한 양수로 잘못 출력 | IV/reference 정보 또는 흡수 제한 caveat 명시 |
| 비선형 소실 | CL과 $t_{1/2}$가 용량 의존적으로 변함 | → | 1차 파라미터 해석 실패 | capacity-limited model로 전환 [G&W p.664] |
| NCA-IIV | 잔차/오차 기여까지 IIV에 섞임 | → | PopPK $\omega^2$ 초기값 과대 | NCA 분산을 상한으로 보고 보수적 초기값 설정 |

> **NCA-volume 원자 노트(atom)**: $V_{ss}$는 "분포 부피 하나"가 아니라 **$AUC$, $AUMC$, CL, 투여 경로 보정이 모두 통과한 최종 요약값**입니다. 그래서 $V_{ss}$를 볼 때는 항상 "**어떤 MRT를 썼는가? 입력 시간을 뺐는가?**"를 같이 봐야 합니다. [G&W pp.149–157]

📖 **Gabrielsson p.157, Fig 2.126**: 이 그림은 washout AUC를 직접 보여줍니다. **§2.8.8 대안식은 단순한 공식 대체가 아니라 적용 영역의 변경**이라는 점은 이 그림이 없으면 잘 와닿지 않습니다 — 입력 시간이 지배적인 상황에서 표준식이 왜 불안정해지는지가 그림 하나에 담겨 있습니다.

### M. Plausible Fallacy — 나비효과 연쇄

**오류:** $V_{ss}$와 $V_z$가 둘 다 양수에 정상 단위로 출력되면, 더 그럴듯한 값을 분포용적으로 써도 된다고 생각한다.
**왜 그럴싸한가:** 두 값 모두 volume 단위로 같은 표에 나오니까, 입력 보정 누락이나 $\lambda_z$ 오염이 있어도 숫자 모양은 정상적으로 보일 수 있습니다.
**나비효과:** MIT 누락 또는 flip-flop $\lambda_z$ 오해 → $V_{ss}$/$V_z$ 해석 혼동 → **[임상]** 부하용량(loading dose) 또는 유지용량 정당화 오류, **digoxin·aminoglycoside 같은 협역 치료역 약물에서 초기 독성 가능성** → **[모델링/규제]** 표준 Eq.2:337과 §2.8.8 Eq.2:366 정합성 대조 누락, NDA submission의 loading dose 정당화 하자, 적용 영역 이탈에 대한 재분석 요구.

> **C3 체화 핵심**
> ① `CL을 해석할 때` → AUC 꼬리와 투여량이 결정
> ② `$V_{ss}$ vs. $V_z$ 혼동` → $V_{ss}$는 MRT/MIT, $V_z$는 $\lambda_z$가 지배
> ⚡ `정상 단위의 volume이면 신뢰 가능` → 입력 보정·말단기 오류 은폐 → 부하용량·모델 초기값·규제 방어 실패

<!-- SLIDE_START: C4 | title: 노출 지표 — 투여량이 아니라 농도를 봅니다 -->
<!-- SECTION_CORE: SC-06 -->

## C4. 노출 지표(Exposure metrics) — 투여량이 아니라 농도를 봅니다

> **앞 카드에서 이 카드로:** C3가 노출을 CL과 분포용적으로 번역했다면, C4는 그중 **어떤 노출 지표가 PD/safety 질문에 맞는지** 고릅니다.

> **거장의 시각**
> 투여량(dose)을 반응의 중심에 두면 route, first-pass, 비선형 소실, 활성 대사체, 단백결합이 만든 노출 차이를 놓칩니다. **Endpoint가 peak·cumulative·threshold·unbound 중 무엇을 묻는지** 먼저 정하면 $C_{max}$, AUC, $C_{ss}$, $t_d$, $C_u$ 선택이 자연스럽게 정렬됩니다.

### A. 노출 지표(Exposure Measures)

§2.9의 핵심은 "투여량(dose)"보다 **전신 노출(systemic exposure)**, 특히 **총 또는 비결합 전신 혈장 농도**를 보라는 것입니다. C1–C3가 노출을 계산해 파라미터로 변환하는 카드라면, C4는 그 노출 중 무엇을 PD/safety와 연결할지 고르는 카드입니다. 같은 투여량이라도 투여 경로, 초회통과, 비선형 소실, 활성 대사체, 단백 결합, 투여 방식에 따라 **실제 표적 노출이 달라집니다.** [G&W pp.158–164]

| 지표(Metric) | 의미 | 사용 직관 | 출처 |
|---|---|---|---|
| $C_{max}$ | 최고 노출(peak exposure) | 급성 독성, peak-driven effect | [G&W p.163] |
| AUC | 총 노출(total exposure) | 누적 노출, extent 비교 | [G&W p.163] |
| $t_d$ | 역치 이상 지속시간 | time-above-threshold 유형 판단 | [G&W p.163] |
| $C_{ss}$ / 평균 농도 | 정상상태 강도 | 만성 투여 노출 | [G&W p.163] |
| 비결합 농도 $C_u$ | 약리학적으로 사용 가능한 분율 | 단백 결합 차이 비교 | [G&W p.163] |

$C_u=C_{total}\cdot f_u$는 일반 정의 보충이며, PDF의 직접 수식 인용으로 취급하지 않습니다. [G&W p.163; 정의 보충]

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

> 💡 **노출 지표는 endpoint의 언어입니다** — 독성이 peak-driven이면 $C_{max}$, 누적 부담이면 AUC, threshold라면 $t_d$가 먼저 질문에 답합니다. 그리고 **같은 총 농도라도 단백 결합이 다르면 비결합 농도 기준 효능 순위가 뒤집힐 수 있습니다.** [G&W p.163]

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

### C. PK41 동적 출처 앵커(Dynamic Source Anchor) — NCA에서 비선형 회귀로

Turbojoint® PK41은 **한 지원자에게 310, 520, 780 µg·kg⁻¹을 각각 5시간 IV 주입**한 사례입니다. NCA에서 투여량이 늘수록 CL은 1.6 → 0.9 L·h⁻¹·kg⁻¹로 줄었고, V는 2.3 → 1.8 L·kg⁻¹, MRT는 1.4 → 1.9 h로 변했습니다. [G&W pp.661–662]

이 패턴이 알려주는 건 분명합니다 — **"용량 증량에서 NCA-CL이 단조 감소하면 용량 제한 소실(capacity-limited elimination)을 의심하라"**는 출처 고정 신호입니다. CL 감소는 표에 한 줄 더 나열된 숫자가 아니라 **모델 전환 신호**입니다. 모델은 이렇게 바뀝니다:

$$
\underbrace{V\cdot\frac{dC}{dt}}_{\text{체내변화}}
=\underbrace{In}_{\text{입력}}-\underbrace{CL\cdot C}_{\text{제거}},\qquad
\underbrace{CL}_{\text{농도의존 CL}}
=\frac{\underbrace{V_{max}}_{\text{최대제거}}}{\underbrace{K_m+C}_{\text{포화경계}}}
$$

💡 **비유:** 선형 CL은 **배수구 지름이 일정한 욕조**처럼 보입니다. 그런데 Michaelis-Menten CL은 **배수구가 포화되면서 물이 차오를수록 빠져나가는 비율이 달라지는 배수 시스템**입니다. 용량이 커질수록 같은 "CL" 이름으로는 더 이상 배수 능력을 설명할 수 없습니다.

NCA 결과는 초기 추정값으로 $V\approx 2$ L/kg, $K_m\approx 150$ µg/L, $V_{max}\approx 310$ µg·h⁻¹·kg⁻¹ 등을 제공합니다. **최종 추정값은 $V_{max}=184$ µg·h⁻¹·kg⁻¹, $K_m=83$ µg/L, $V=1.8$ L/kg**이었습니다. 저자의 결론은 분명합니다 — 용량 제한 1구획 시스템의 파라미터는 CL과 V가 아니라 $V_{max}$, $K_m$, V이며, **CL과 $t_{1/2}$는 혼합 0차/1차 동력학과 양립할 수 없습니다(incompatible).** [G&W pp.663–664]

### D. 원자 노트와 그림 참조

> **노출 원자 노트(Exposure atom)**: 투여량은 **투입량**이고, 노출은 **몸이나 표적이 실제로 본 농도-시간 부담**입니다. §2.9의 모든 사례는 한 문장으로 수렴합니다 — **"투여량이 같아도 노출이 다르면 반응이 달라진다."** [G&W pp.158–164]

📖 **Gabrielsson p.163, Fig 2.135**: 이 그림은 $C_{ss}$/평균 농도, $C_{max}$, AUC, 역치 초과 노출/$t_d$가 **서로 다른 약리학적 질문에 답하는 요약값**임을 한 화면에서 분리해 보여줍니다. 노출 지표가 단순 목록이 아니라 endpoint별로 다른 도구라는 게 이 그림에서 자리 잡힙니다.

📖 **Gabrielsson p.663, Fig 41.2**: PK41의 CL 감소가 **숫자 한 줄이 아니라 모델 전환 신호**라는 점을 시각적으로 못 박는 그림입니다. 이 그림이 없으면 학습자가 NCA-CL을 "용량별 기술 표"로만 읽고, 비선형 회귀로 전환해야 한다는 필연성을 약하게 느낍니다.

> **C4 체화 핵심**
> ① `endpoint가 peak-driven일 때` → $C_{max}$가 우선 지표
> ② `총 농도 vs. 비결합 농도 혼동` → $C_u=C_{total}\cdot f_u$가 지배
> ⚡ `dose가 같으면 response도 같다` → route·first-pass·비선형 소실·단백결합 차이를 무시 → exposure-response 정당화 실패

<!-- SLIDE_START: §5 | title: 혼동 쌍 해부 -->
<!-- SECTION_CORE: SC-07 -->

# §5 — 혼동 쌍 해부(Confusion Pair Dissection)

## 쌍 1. AUC vs AUMC — 영차 모멘트 vs 일차 모멘트

| 비교 기준 | AUC | AUMC |
|---|---|---|
| 단위 / 차원 | 농도×시간 | 농도×시간² |
| 수식 내 위치 (분자/분모/지수) | 꼬리: $C_{last}/\lambda_z$ | 꼬리: $t_{last}C_{last}/\lambda_z+C_{last}/\lambda_z^2$ |
| 변화 원인 (생물학적/병적) | 농도 크기, CL, 표본추출 | 늦은 시간 농도, 꼬리 표본추출, $\lambda_z$ 오류 |
| 혼동 시 임상 결과 | 총 노출 비교와 CL 해석 왜곡 | MRT와 $V_{ss}$ 오류 증폭 |

**⚡ 기억 고리 (Memory Hook)**: AUC 꼬리는 $\lambda_z$의 1차 항 하나뿐이지만, AUMC 꼬리는 **$1/\lambda_z$와 $1/\lambda_z^2$ 두 항이 동시에** 들어갑니다. 시간이 한 번 더 가중되는 순간 후방 꼬리가 지배적이 됩니다 — 그래서 같은 말단 기울기 오류라도 **MRT와 $V_{ss}$로 흘러갈 때 더 강하게 증폭**됩니다. [G&W pp.144–145]

**핵심 구분**: AUMC는 늦은 농도를 시간으로 다시 가중하므로, 같은 말단 기울기 오류라도 MRT와 $V_{ss}$에 더 민감하게 전달됩니다. [G&W pp.142–148]

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

**⚡ 기억 고리 (Memory Hook)**: MRT는 **분자가 머문 시간의 평균**, $t_{1/2}$는 **농도가 절반이 되는 시간**입니다. 1구획 단일지수(monoexponential)에서는 $MRT=1/\lambda_z$, $t_{1/2}=\ln(2)/\lambda_z$로 단순한 비율 관계($1/\ln 2\approx 1.443$)지만, 다구획에서는 **MRT가 분포기 정보까지 흡수하는 반면 $t_{1/2}$는 말단 기울기만 기술**합니다. 그래서 유효 반감기는 $\ln(2)\cdot MRT$로 다시 정의됩니다. [G&W p.151; R&T pp.789–793]

**핵심 구분**: MRT는 분포와 제거를 통합한 평균 시간이고, $t_{1/2}$는 말단 기울기의 시간 척도입니다. 1구획 단일지수 상황에서는 가까워질 수 있지만 같은 개념은 아닙니다. [G&W p.151; R&T pp.789–793]

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

**⚡ 기억 고리 (Memory Hook)**: $V_{ss}$의 분모에는 $AUMC$와 투여 경로 보정이 둘 다 들어오고, $V_z$의 분모에는 $AUC$와 $\lambda_z$만 들어갑니다. 그래서 **두 부피가 어긋나는 방향 자체가 어디서 가정이 흔들렸는지 알려주는 단서**가 됩니다 — 표준 $V_{ss}$만 비정상적으로 부풀거나 음수에 가까워지면 **투여 경로 보정 영역**의 문제, $V_z$만 부풀면 **말단 기울기 영역**의 문제입니다. [G&W pp.151, 157]

**치명적 타격(Critical Blow)**: $V_z$를 $V_{ss}$로 혼동해 부하용량을 계산하면 실제 약물 분포 용량을 과대추정합니다. 다구획 약물에서 이 오류는 **초기 독성 농도**를 일으킬 수 있고, 특히 협역 치료역 약물(**digoxin, aminoglycoside**)에서는 **NDA submission의 loading dose 정당화에 결정적 하자**가 됩니다.

$$
\underbrace{V_{ss}}_{\text{정상상태 V}}=\underbrace{MRT}_{\text{체류시간}}\cdot\underbrace{CL}_{\text{정화}},\qquad
\underbrace{V_z}_{\text{말단 V}}=\frac{\underbrace{CL}_{\text{정화}}}{\underbrace{\lambda_z}_{\text{말단기울기}}}
$$

**§5 요약(Recap)**: 이 세션의 혼동쌍은 모두 **"같아 보이는 요약 숫자"** 문제입니다. AUC/AUMC, MRT/반감기, $V_{ss}/V_z$는 출력 표에서 가까이 붙어 있지만 **서로 다른 질문에 답합니다.** 같은 표 안의 값이라도 "무엇을 묻는 숫자인가"를 바꾸면 해석 대상이 완전히 달라집니다.

<!-- SLIDE_START: §7 | title: 자기 테스트: 능동 회상 모듈 -->
<!-- SECTION_CORE: SC-08 -->

# §7 — 자기 테스트: 능동 회상 모듈(Active Recall Module)

## Q1. 선형 사다리꼴 AUC와 로그-선형 사다리꼴 AUC의 수식을 쓰고, 각각의 적용 조건을 말해 보세요.

**정답**: 선형 규칙은 $\sum [(C_i+C_{i+1})/2]\Delta t$이며, 상승·평탄·하강 구간 모두 계산할 수 있지만 하강 구간에서 과대추정합니다. 로그-선형 규칙은 $(C_i-C_{i+1})/\ln(C_i/C_{i+1})\cdot\Delta t$이며, 하강 자료에서만 유효합니다. $C_i=0$ 또는 $C_{i+1}=C_i$에서는 선형 대체가 필요합니다. [G&W pp.143–145]

## Q2. $\lambda_z$ 추정의 최소 조건과 이상 조건은 무엇인가요?

**정답**: 최소 3–4개 말단 관측값이 필요하고, 이상적으로는 말단기에서 3–4 반감기가 경과해야 합니다. 관측 마지막 농도가 말단 회귀선에서 벗어나면 $\hat C_{last}$를 검토합니다. [G&W pp.146–147]

## Q3. 외삽 AUC가 총 AUC의 30%라면 어떻게 보고해야 하나요?

**정답**: Gabrielsson의 일반 권고 20–25%를 넘으므로, 최종 신뢰 파라미터처럼 쓰기보다 **예비 추정값** 성격을 명시합니다. 추가 표본추출 또는 말단기 재검토가 필요합니다. [G&W p.148]

## Q4. PK41에서 NCA 결과가 비선형 회귀의 초기 추정값으로 전환되는 흐름을 설명해 보세요.

**정답**: Turbojoint®에서 310/520/780 µg·kg⁻¹ 5h IV 주입 후 투여량 증가에 따라 NCA-CL이 1.6 → 0.9 L·h⁻¹·kg⁻¹로 감소했습니다. 이는 용량 제한 소실 신호이며, NCA는 최종 CL 보고가 아니라 $V_{max}$, $K_m$, V를 갖는 Michaelis-Menten 회귀의 **초기 추정값 앵커**가 됩니다. 최종 추정값은 $V_{max}=184$ µg·h⁻¹·kg⁻¹, $K_m=83$ µg/L, $V=1.8$ L/kg이었습니다. [G&W pp.661–664]

## Q5. R&T Table H-1에서 $AUC=44.2$, $AUMC=177$이면 혈장 MRT는 얼마인가요?

**정답**: $MRT=AUMC/AUC=177/44.2\approx 4.0$ hr입니다. 같은 예시에서 소변 MRT $\approx 4.25$ hr, simulated MRT $\approx 4.3$ hr로 일관됩니다. [R&T p.792]

## Q6. IV bolus에서 CL은 어떻게 계산하며, 경구 투여에서는 무엇이 달라지나요?

**정답**: IV bolus/IV 투여에서는 $CL=D_{iv}/AUC_0^\infty$입니다. 경구에서는 생체이용률(F)이 섞이므로 $CL/F=D_{po}/AUC_0^\infty$로 **겉보기 청소율(apparent clearance)**을 계산합니다. [G&W p.149]

## Q7. 급성 독성, 누적 노출, 역치 기반 효과에는 각각 어떤 노출 지표를 우선 볼까요?

**정답**: 급성 독성은 $C_{max}$, 누적 노출은 AUC, 역치 기반 효과는 $t_d$ 또는 역치 초과 AUC를 우선 봅니다. 실제 선택은 약물 기전과 반응 시간경과에 맞춰 정당화해야 합니다. [G&W p.163]

## Q8. 총 농도 기준 효능 순위와 비결합 농도 기준 순위가 달라질 수 있는 이유는 무엇인가요?

**정답**: 단백 결합이 다르면 총 농도가 같아도 **약리학적으로 사용 가능한 비결합 농도**가 달라집니다. §2.9의 메시지는 총 농도보다 **비결합 전신 노출**이 더 직접적인 비교 기준이 될 수 있다는 것입니다. [G&W p.163]

## Q9. 보스 딜레마(Boss Dilemma): 회사 SOP는 표준 Eq.2:337만 허용하지만, 반감기가 입력 시간에 비해 매우 짧아 §2.8.8 대안식이 더 타당해 보입니다. 어떻게 처리해야 하나요?

**정답**: 표준식과 §2.8.8 대안식을 **둘 다 계산해 차이를 제시**하고, 차이의 원인이 $T_{inf}/t_{1/2}$ 비율에 있음을 설명합니다. SOP deviation은 "더 예쁜 결과"가 아니라 **0 또는 음수 $V_{ss}$를 피하는 출처 기반 수학적 정당화**로 문서화합니다. [G&W pp.151, 157]

**§7 요약(Recap)**: Q1–Q3은 AUC 신뢰도, Q4는 비선형 전환, Q5–Q6은 NCA 계산, Q7–Q8은 노출 해석, Q9는 C3 Apex의 적용 경계입니다.

<!-- SLIDE_START: §8 | title: 메타프레임과 거시 구조 -->
<!-- SECTION_CORE: SC-09 -->

# §8 — 메타프레임과 거시 구조(Meta-Frame & Big Picture)

## A. 위치 설정(Positioning)

NCA는 PopPK를 **대체**하는 분석이 아니라 **모델링 전후에 활용하는 도구**입니다. 모델 선택 전에는 EDA와 초기 추정값을 만들고, 모델 추정 후에는 population prediction이 관측 노출의 규모와 일관되는지 확인하는 기준점이 됩니다. 다만 NCA는 선형 소실을 가정합니다 — 이 점을 잊으면 **"단순해서 강한 방법"이 "단순해서 틀린 방법"**으로 바뀝니다. [G&W p.141]

## B. 추적해야 할 실패 모드

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| 말단 기울기 오염 | $\lambda_z$ | → | AUC 꼬리, CL, $V_z$ 동시 왜곡 | selection plot, %extrapolated, $C_{last}$ 처리 기준 확인 [G&W pp.146–148] |
| 투여 경로 보정 누락 | MIT, MRT | → | MRT와 $V_{ss}$가 실제 체류/분포보다 길거나 짧게 해석 | infusion/oral input time 보정 [G&W pp.149–151; R&T p.793] |
| NCA CL처럼 보이는 비선형 CL | CL | → | 용량별 최종 파라미터처럼 오해 | capacity-limited model 전환 [G&W pp.661–664] |
| NCA-IIV 과사용 | NCA-derived variability | → | PopPK $\omega^2$ inflation cascade, 공변량 회귀 신호 약화 | NCA 분산은 상한으로 보고 보수적 초기값 사용 |

> 💼 **실무 인사이트:** NCA 유래 변동성은 PopPK IIV의 직접 추정값이 아니라 **잔차 변동성까지 섞인 상한**입니다. 이 상한을 PopPK $\omega^2$ 초기값으로 그대로 입력하면 **IIV가 RUV를 흡수하면서 후속 공변량 회귀가 묻혀버릴 수 있습니다.**

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
| Exposure-response 분석 | endpoint별 $C_{max}$/AUC/$t_d$/$C_u$ 선택 | dose-only 해석으로 PD/safety 논증 실패 |

## E. 최종 압축 원칙(Final Compressed Doctrine)

NCA의 본질은 **"모델을 쓰지 않는다"가 아니라 "최소한의 선형 소실 가정으로 면적과 시간 모멘트를 요약한다"**입니다. AUC는 노출의 출발점, AUMC는 체류시간의 출발점, MRT는 $V_{ss}$의 출발점입니다. **PK41은 이 모든 것이 비선형 동력학 앞에서 초기 추정값으로 격하되는 순간**을 보여줍니다.

**§8 요약(Recap)**: 30년 pharmacometrics 연구자가 10분 핸드아웃에 남길 메시지는 하나입니다 — NCA 출력 표를 믿기 전에 **말단 기울기 → 외삽 분율 → 투여 경로 보정 → 용량 의존성 → 노출 지표 선택**을 순서대로 점검합니다.

> 💼 **실무 인사이트:** 완성된 NCA 보고서는 **숫자 표가 아니라 가정 감사 추적 기록(assumption audit trail)**이어야 합니다. 독자가 말단 기울기, 꼬리 분율, 투여 경로 보정, 용량 의존성, 노출 지표 선택을 따라갈 수 있으면 이후 PopPK 모델링의 출발점으로도 방어 가능해집니다. 그리고 NCA 보고서의 1차 파라미터 자리에는 $AUC$가 아니라 **$CL$ 또는 $CL/F$**를 두고 $AUC$는 노출 지표로 보고하는 편이, **생리학적 해석성과 공변량 회귀 가능성을 동시에 보존**합니다 — 보고 순서가 바뀌면 이후 PopPK에서 신·간 기능 공변량 신호가 약하게 나타날 수 있습니다.

<!--
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
-->
<!-- v3.8 변환 노트
- 활자량 감축: v3.7 683행 → v3.8 (감축률은 본문 산문 기준 ≈ 45–50%; 수식·표·인용은 byte-level 보존)
- 보존 감사:
  * SLIDE_START 마커: 9개 = v3.7 일치
  * 수식 블록($$): 22개 = v3.7 일치
  * 출처 anchor: [G p.xxx]/[T p.xxx] 모두 보존
  * 약물명·수치: Turbojoint PK41 (310/520/780 µg·kg⁻¹, CL 1.6→0.9, V 2.3→1.8, MRT 1.4→1.9, Vmax=184, Km=83, V=1.8), R&T Table A-1 (50 mg, total AUC 26.60), zileuton A-2 (600 mg), R&T Table H-1 (AUC=44.2, AUMC=177, MRT 4.0/4.25/4.3), GFR/QH 등 모두 보존, digoxin·aminoglycoside 보존
- 주요 변환:
  * §1 학습 안내 verbose 블록 → "빠른 읽기 경로" 박스 1개로 축약
  * §1과 C1의 중복된 Fig 2.113 참조 → §1 한 곳으로 통합
  * 카드별 💡⚠️🔑 다중 콜아웃 → 단일 💡 통합 (카드당 ≤6 유지)
  * "Mn의 결론이 ~한다" 형태 자기참조 → 그 자리에서 한 문장으로 결론 풀고 포인터만 괄호로
  * §8의 [EXPERT_INFERENCE] / [CRUCIBLE_DERIVED] 태그 제거(내용은 보존), 마지막 두 실무 인사이트 박스를 하나로 통합
  * 약어 첫 등장 시 한국어 풀이 인라인 (MIT, NDA, IIV 등)
  * "확인 시점:" 패턴 제거 → 그림이 보여주는 것을 직접 한 문장으로 기술
-->

---

C-260514-094312-K7M

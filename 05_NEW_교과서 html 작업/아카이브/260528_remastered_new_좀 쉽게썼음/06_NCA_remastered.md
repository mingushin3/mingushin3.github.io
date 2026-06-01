# 비구획 분석(NCA) — 면적·모멘트·노출의 감사 동선 (Remastered)

> *"NCA 출력 표는 답이 아니라 진술서임. 그리고 진술서는 한 줄씩 읽는 게 아니라 가정 순서로 읽는 것임."*

---

## 0. 들어가기 — 한 컷이 모든 것을 말해줌

Turbojoint® PK41 한 컷부터 보고 시작함.

한 명의 지원자에게 **310 / 520 / 780 µg·kg⁻¹**을 각각 5시간 IV 주입했음. 그런데 투여량을 올릴수록 NCA 표가 이렇게 출력됨:

| 용량(µg·kg⁻¹) | NCA-CL (L·h⁻¹·kg⁻¹) | V (L·kg⁻¹) | MRT (h) |
|---:|---:|---:|---:|
| 310 | 1.6 | 2.3 | 1.4 |
| 520 | 1.2 | 2.0 | 1.6 |
| 780 | 0.9 | 1.8 | 1.9 |

용량을 2.5배 올렸더니 CL이 반토막남. 표만 보면 "어 이 약 청소율이 떨어졌네"라고 적고 다음 줄로 넘어가기 쉬움. 그런데 이 한 컷이 NCA 전체의 정체를 드러내는 결정적 장면임 — **NCA가 출력한 CL은 "그 용량에서의 진짜 청소율"이 아니라 "선형 소실을 가정했을 때 면적이 보여준 평균 청소율"이기 때문임.** 가정이 무너지면 출력값의 이름도 바뀜. [G&W pp.661–664]

그래서 이 자료의 한 줄 명제는 이거임:

> **NCA 출력은 최종 답이 아니라, 다음 모델(비선형 회귀, PopPK)로 넘어가는 anchor임. NCA 표를 읽는 일은 숫자를 읽는 일이 아니라 가정 점검 기록을 읽는 일임.**

이걸 머리에 박고 본문으로 들어감.

---

## 1. NCA의 정체성 — "model-free"가 아니라 "assumption-dependent"

### 1.1 흔한 오해 한 줄로 정리

NCA를 "model-free"라고 부르는 관습이 있음. 그런데 정확한 표현은 **"compartment-free"**임. 1구획·2구획·3구획 같은 특정 구획 모델은 안 세우지만, 그 대신 **세 가지 가정**이 표 전체를 떠받치고 있음. [G&W p.141]

```
가정 ①  선형 소실      → 채혈 구획에서 농도에 비례해 약물이 빠진다
가정 ②  진짜 terminal   → 말단기 회귀에 들어간 점들이 실제 elimination phase다
가정 ③  입력 시간 보정  → MIT를 빼면 순수 체류시간이 남는다
```

이 세 가정 중 **하나만 무너져도 표의 어떤 칸 하나만 흔들리는 게 아니라 표 전체가 연쇄적으로 흔들림**. 그게 NCA의 위험이자 매력임. 단순한 만큼 가정에 정직해야 함.

### 1.2 그래서 NCA를 어떻게 읽어야 하는가 — 감사 동선

NCA 보고서를 위에서부터 한 줄씩 읽는 사람은 초보임. 실무자는 **가정 점검 순서대로 표를 재배열해서 읽음**. 이 순서가 이번 자료의 척추임:

```
[면적이 믿을 만한가?] → [시간 모멘트가 안정적인가?] → [임상 파라미터로 굳어졌을 때 어떤 가정이 어디 박혔나?] → [어떤 노출 지표를 PD/safety의 중심에 둘 것인가?]
       C1                       C2                                  C3                                              C4
```

🔑 **이 네 단계는 병렬이 아니라 직렬임**. C1의 오류는 C2로, C2의 오류는 C3로, C3의 해석 실패는 C4의 endpoint 정당화 실패로 전파됨. 이 직렬성을 잊으면 NCA 보고서 검토가 "체크리스트 채우기"로 전락함.

| 단계 | 질문 | 카드 | 다음 카드로 전파되는 오류 |
|---|---|---|---|
| 1 | 면적이 믿을 만한가? | C1 (AUC / λz / 외삽 / BLQ) | AUC 오류 → CL·V·노출 모두 왜곡 |
| 2 | 시간 모멘트가 안정적인가? | C2 (AUMC / MRT / MIT) | AUMC 꼬리 오류 → MRT·V_ss 왜곡 |
| 3 | 분포·청소가 경로 보정됐는가? | C3 (CL / V_ss / V_z) | MIT 누락 → V_ss 해석 오류 |
| 4 | 어떤 노출 지표로 PD/safety? | C4 (C_max / AUC / t_d / C_u / PTF) | dose-only 해석 → 노출-반응 판단 실패 |

> 💼 **현장 감각** — 컨퍼런스에서 NCA 보고서를 처음 받으면, 1차 파라미터 표 위쪽에 적힌 **λz 선정 구간, %extrapolated, BLQ 처리 규칙, MIT 보정 여부** 네 줄을 먼저 봄. 이 네 줄이 멀쩡하면 그 아래 CL·V·노출은 그제서야 진지하게 읽을 가치가 있음. 거꾸로 이 네 줄이 부실하면 아래 숫자가 아무리 예뻐도 회의실에서 깨질 자료임.

**출처:** Gabrielsson & Weiner 5e Ch.2 §2.8–§2.9, PK41; Rowland & Tozer 5e Appendix A·H, Ch.6 §BE, Ch.11 §Fluctuation, Ch.19 §Distribution Kinetics. [G&W pp.141–164, pp.661–664; R&T pp.759–762, pp.789–793, pp.182–195, pp.276/325/340, pp.626/632–636]

---

## 2. C1 — 면적이 믿을 만한가: AUC, λz, 외삽, BLQ

### 2.1 AUC라는 "객관적 면적"의 정체

AUC를 "데이터 위로 사다리꼴을 깐 객관적 면적값"으로 읽으면 절반만 본 것임. 실제 AUC는 두 덩어리로 이루어져 있음:

$$
\underbrace{AUC_{total}}_{\text{총 노출}}
=\underbrace{AUC_{0 \to t_{last}}}_{\text{관측 사다리꼴 합}}
+\underbrace{AUC_{t_{last} \to \infty}}_{\lambda_z\text{ 외삽 꼬리}}
$$

**관측 부분은 산수**임. 사다리꼴 면적 더하기. 하지만 **꼬리 부분은 "말단 기울기를 어떻게 정했느냐"에 전적으로 의존하는 추정치**임. AUC 한 값을 흔드는 진짜 변수는 거의 항상 이 꼬리에 숨어 있음.

### 2.2 사다리꼴 두 종류 — 언제 무엇을 쓰는가

**선형 사다리꼴(linear trapezoidal):** [G&W p.143, Eq.2:310; R&T pp.759–760]

$$
\underbrace{AUC_0^{t_{last}}}_{\text{관측 AUC}}
=\sum_i \underbrace{\frac{C_i+C_{i+1}}{2}}_{\text{평균농도}}\cdot\underbrace{\Delta t}_{\text{시간폭}}
$$

이게 표준 default임. 그런데 본질적인 편향이 있음 — **상승 구간에서 과소추정, 하강 구간에서 과대추정**. 표본 간격이 반감기 대비 클수록 더 커짐. 직선 판자로 곡선을 덮으니까 곡률을 무시하는 셈임.

**로그-선형 사다리꼴(log-linear):** [G&W pp.144–145, Eq.2:316; R&T p.761]

$$
\underbrace{AUC_i^{i+1}}_{\text{구간 AUC}}
=\underbrace{\frac{C_i-C_{i+1}}{\ln(C_i/C_{i+1})}}_{\text{로그평균농도}}\cdot\underbrace{\Delta t}_{\text{시간폭}}
$$

하강 구간에만 유효함. C_i = 0 또는 C_{i+1} = C_i면 정의되지 않으니까 그 구간만 선형으로 fallback함.

💡 **비유 한 줄로** — 하강 구간을 직선 판자로 덮으면 면적을 과대추정함. 로그-선형은 곡선 기울기에 맞춘 얇은 천으로 덮는 방식임. 표본 간격이 길수록 곡률을 더 존중함.

**혼합 방식(mixed):** 증가/평탄 구간은 선형, 감소 구간은 로그-선형. 합리적으로 설계된 sparse design에서는 두 방법 차이가 임상적으로 작다는 게 G&W의 균형임 — 그러니까 "항상 mixed가 표준"이라고 외우지는 말 것. 보고서에 어느 방식을 썼는지 명시하면 됨. [G&W p.146]

### 2.3 말단 외삽 — AUC를 흔드는 진짜 변수

$$
\underbrace{AUC_{t_{last}\to\infty}}_{\text{꼬리 AUC}}
=\frac{\underbrace{C_{last}\ \text{or}\ \hat C_{last}}_{\text{말단 농도}}}{\underbrace{\lambda_z}_{\text{말단 기울기}}}
$$

관측 마지막 농도 $C_{last}$가 말단 회귀선에서 벗어나 있으면, 관측값을 그대로 쓰지 말고 **회귀선이 예측하는 $\hat C_{last}$를 씀**. 이게 일반적인 권고임. [G&W p.147]

그리고 가장 중요한 수치 — **외삽 면적 비율**:

$$
\underbrace{\%Extrapolated}_{\text{외삽률}}
=\frac{AUC_{t_{last}\to\infty}}{AUC_{total}}\times 100
$$

G&W 권고는 **외삽 면적이 총 AUC의 20–25%를 넘지 않을 것**임. 이걸 넘기면 그 AUC는 "최종 신뢰값"이 아니라 **예비 추정값(preliminary estimate)**으로 보고함. [G&W p.148]

> 💼 **현장 감각** — NCA 자동 출력의 λz 구간을 그대로 믿으면 안 됨. **반로그(semi-log) 도표에서 직접 확인**하는 게 표준 절차임. adjusted R²가 0.99여도, 분포기(distribution phase) 점이 말단 회귀에 섞이면 λz가 평탄해지고 AUC 꼬리가 부풀음. 그리고 이게 무서운 이유는 — **CL, V_z, V_ss가 동시에 다 흔들림**. λz 한 개의 오류가 표의 네 칸으로 동시에 흘러감.

🔑 **AUC 보고 규칙** — AUC 한 값만 적지 말 것. **λz, $C_{last}^{obs}$ vs $\hat C_{last}$, %extrapolated**를 같이 적어야 보고서가 감사 가능해짐.

### 2.4 BLQ 처리 — 위치가 모든 것을 결정함

LOQ 미만 값(Below Limit of Quantification)을 어떻게 처리할지는 "그냥 결측 처리"라는 한 줄로는 절대 부족함. **BLQ가 농도 곡선의 어디에서 발생했느냐**에 따라 처리 규칙이 분기됨.

Gabrielsson의 원칙은 분명함 — **"회귀 관점, 특히 지수 모델에서는 LOQ 미만 농도를 0이나 다른 값으로 절대 대체하지 말 것. missing values로 처리하는 것이 LOQ나 0으로 대체하는 것보다 낫다."** [G&W p.153]

| BLQ 위치 | 통상 처리 | 처리 근거 | AUC/AUMC 영향 |
|---|---|---|---|
| **첫 정량 가능 시점 이전** | IV: 0 처리 / 경구: 결측 또는 보간 | IV는 t=0이 정의됨. 경구에서 흡수 lag을 강제 0으로 두면 초기 AUC 왜곡 | 초기 AUC 약간 과소~정상 |
| **중간(intervening) BLQ** | 선형 보간 또는 결측 | 0으로 두면 양쪽 관측을 인공적으로 끌어내려 AUC 과소 | 0 대체 시 AUC 과소 |
| **말단(terminal) BLQ** | 결측 처리 권장 | 0 대체 시 $\ln 0=-\infty$로 지수 회귀 수렴 불능. 말단 회귀에 BLQ 포함 시 λz 평탄화 | 0 대체 시 λz → 외삽 꼬리 → CL·V_z 연쇄 왜곡 |

$$
\underbrace{C_{BLQ}}_{\text{관측 BLQ}}\ \rightarrow\
\begin{cases}
\overbrace{0}^{\text{pre-first, IV}}\\[2pt]
\overbrace{\text{missing}}^{\text{intervening, terminal}}\\[2pt]
\overbrace{\text{linear interp.}}^{\text{intervening 대안}}
\end{cases}
$$

> 💼 **현장 감각** — BLQ 처리 규칙은 **반드시 SOP나 SAP(Statistical Analysis Plan)에 사전 명문화**해야 함. 분석 끝난 뒤에 규칙을 바꾸면 그 자체로 data dredging으로 간주됨. 특히 말단 BLQ 처리 방식이 λz에 직접 들어오니까, **BLQ 규칙 → 말단점 선정 → λz → AUC 꼬리 → CL·V_z**로 오류가 연쇄 전파됨. BLQ 처리 기록 없는 NCA 보고서는 그 자체로 감사 부적격 자료임.

🌉 **PopPK로 가는 다리 — NCA의 missing ≠ PopPK의 missing**

이게 NCA→PopPK 전환에서 가장 많이 놓치는 부분임. NCA의 BLQ 처리는 **point exclusion 패러다임** — 한 점을 결측으로 두거나 양 옆 값으로 보간함. NONMEM 같은 PopPK 도구에서는 이걸 **likelihood-based** 처리로 격상시킴.

Beal (2001) 분류에서 **M3 방법**은 "BLQ 관측값이 LOQ보다 작을 likelihood가 모델 적합도에 기여한다"는 censoring framework임. M5는 LOQ/2 substitution, M6는 첫 BLQ만 LOQ/2 처리 후 나머지 결측, M7은 BLQ를 0 처리 — 모두 M3의 단순화 변종임. **NCA에서 결측 처리한 BLQ도 PopPK 단계에서는 M3로 다시 들어와 추정 정밀도를 회복할 수 있음.**

$$
\underbrace{\text{NCA}}_{\text{point exclusion}}:\ C_{BLQ}\to\text{missing}
\quad\Longrightarrow\quad
\underbrace{\text{PopPK (M3)}}_{\text{likelihood-based}}:\ \overbrace{P(C_{obs}<LOQ\mid\theta)}^{\text{censored likelihood}}\ \text{기여}
$$

두 영역에서 "missing"이라는 같은 단어가 가리키는 처리는 다름. NCA 보고서의 BLQ 처리 규칙(SOP/SAP)과 PopPK의 BLQ likelihood 옵션이 일관되게 정렬되어 있는지 — 이게 보고서 검토의 숨은 1번 항목임.

### 2.5 C1 마무리 — 다음 카드로 무엇이 전파되는가

C1의 한 줄 결론은 이거임:

> **AUC는 "사다리꼴 합"이 아니라 "사다리꼴 합 + λz 기반 꼬리"임. AUC 검토는 값 자체가 아니라 (말단 기울기 선택, $\hat C_{last}$ 사용 여부, 외삽 비율, BLQ 처리 분기) 네 항목의 처리 기록 검토임.**

→ **C2로 전파되는 것:** λz가 흔들리면 AUC 꼬리뿐 아니라 **AUMC 꼬리가 1/λz²로 더 강하게 흔들림**. C1의 λz 오류는 C2에서 두 배로 증폭되어 등장함.

---

## 3. C2 — 시간 모멘트가 안정적인가: AUMC, MRT, MIT

### 3.1 AUC와 AUMC — 같은 자료를 두 번 묻는 것

C1에서 "얼마나 노출되었는가"를 물었다면, C2는 **"그 노출이 언제 일어났는가"**를 시간 가중으로 다시 묻는 단계임. 두 면적의 차이는 차원과 민감도에 그대로 드러남:

| | AUC (영차 모멘트) | AUMC (일차 모멘트) |
|---|---|---|
| 차원 | 농도 × 시간 | 농도 × 시간² |
| 가중 | 시간 가중 없음 | 시간으로 한 번 더 가중 |
| 꼬리 항 | $C_{last}/\lambda_z$ | $t_{last}C_{last}/\lambda_z + C_{last}/\lambda_z^2$ |
| λz 오류 민감도 | 1차 | **2차** (1/λz² 항 때문) |

$$
\overbrace{AUC_{tail}=\frac{C_{last}}{\lambda_z}}^{\text{1차 꼬리}}
\qquad\text{vs}\qquad
\overbrace{AUMC_{tail}=\frac{t_{last}C_{last}}{\lambda_z}+\frac{C_{last}}{\lambda_z^2}}^{\text{AUMC 꼬리}}
$$

💡 **비유 한 줄로** — AUC가 하루 동안 받은 햇빛 총량이라면, **AUMC는 늦은 오후 햇빛에 더 무거운 추를 매단 저울**임. 해 질 무렵의 작은 측정 오차가 평균 체류시간을 크게 밀어냄. 같은 말단기 오염이라도 AUMC를 통해 **MRT와 V_ss로 더 강하게 증폭**됨.

**AUMC 계산 — 선형 사다리꼴:** [G&W p.144, Eq.2:312]

$$
\underbrace{AUMC_0^{t_{last}}}_{\text{관측 AUMC}}
=\sum_i \underbrace{\frac{t_iC_i+t_{i+1}C_{i+1}}{2}}_{\text{시간가중 평균}}\cdot\underbrace{\Delta t}_{\text{시간폭}}
$$

**꼬리 외삽:** [G&W pp.144–145, Eq.2:313/2:320]

$$
\underbrace{AUMC_{t_{last}\to\infty}}_{\text{꼬리 AUMC}}
=\underbrace{\frac{t_{last}C_{last}}{\lambda_z}}_{\text{시점 가중 항}}
+\underbrace{\frac{C_{last}}{\lambda_z^2}}_{\text{기울기 민감도 항}}
$$

🔑 **C1의 λz 오류가 C2에서 두 배로 증폭되는 지점이 여기임** — AUMC 꼬리에 $1/\lambda_z^2$ 항이 박혀 있음. λz를 5% 잘못 추정하면 AUC 꼬리는 약 5% 흔들리지만, AUMC 꼬리의 후방항은 약 10% 흔들림.

### 3.2 MRT — "평균"이라는 단어의 함정

MRT(Mean Residence Time)를 "안정된 평균값"으로 읽고 넘어가는 게 NCA 학습자가 가장 많이 빠지는 함정임. "평균"이라는 단어가 주는 인상 때문임. 실제로는 AUMC 꼬리의 민감도와 입력 시간 보정 두 가지를 모두 흡수하는, **꽤 불안정한 요약값**임.

**분자 정의:** [R&T p.789, Eq.H-1]

$$
\underbrace{MRT}_{\text{평균 체류시간}}
=\frac{\sum_j t_j}{N}
\quad\text{(분자가 계 안에서 보낸 시간의 평균)}
$$

R&T Appendix H는 직관적인 출발을 줌 — 분자량 300 g/mol인 약물 1 mg 안에 약 $2\times10^{18}$개의 분자가 있는데, 그 각각이 몸 안에서 보낸 시간을 평균낸 값이 MRT임.

**혈장 정의:** [R&T p.791, Eq.H-8]

$$
\underbrace{MRT}_{\text{혈장 MRT}}
=\frac{\underbrace{AUMC_0^\infty}_{\text{시간가중 노출}}}{\underbrace{AUC_0^\infty}_{\text{총 노출}}}
$$

R&T Table H-1 수치 검증 — $AUC=44.2$ mg·hr/L, $AUMC=177$ mg·hr²/L일 때:

- 혈장 MRT ≈ 4.0 hr
- 소변 MRT ≈ 4.25 hr
- simulated MRT ≈ 4.3 hr

**세 경로가 모두 같은 곳에 수렴**함. 이게 중요함 — 분자 수준 정의와 혈장/소변 계산이 일관되니까 MRT가 "단순한 비율 계산"이 아니라 **진짜 물리적 평균 체류시간**이라는 게 확인됨. [R&T p.792]

### 3.3 MRT ≠ t½ — 같은 시간 단위라도 다른 것을 측정함

이 두 값을 헷갈리는 게 NCA 학습의 두 번째 함정임. 둘 다 단위가 "시간"이고 둘 다 elimination 관련 지표지만, **답하는 질문이 완전히 다름**:

| | MRT | t½ |
|---|---|---|
| 정의 | 분자가 계 안에서 보낸 시간의 평균 | 농도가 절반으로 감소하는 시간 |
| 계산 | $AUMC/AUC$ - MIT | $\ln(2)/\lambda_z$ |
| 1구획 단일지수 상황 | $MRT = 1/\lambda_z$ | $t_{1/2} = \ln(2)/\lambda_z$ |
| 다구획 상황 | 분포기까지 포함한 통합 평균 | 말단 기울기만 기술 |

$$
\underbrace{MRT}_{\text{체류시간 평균}}=\frac{AUMC}{AUC}
\qquad\text{vs}\qquad
\underbrace{t_{1/2}}_{\text{반감기}}=\frac{\ln(2)}{\lambda_z}
$$

1구획 단일지수 상황에서는 두 값이 단순 비율($1/\ln 2 \approx 1.443$)로 연결됨. 그런데 **다구획에서는 MRT가 분포기 정보까지 흡수하는 반면 t½는 말단 기울기만 기술**함. 그래서 다구획 약물에서 두 값을 같은 의미로 쓰면 안 됨.

대신 정의되는 게 **유효 반감기(effective half-life)**임:

$$
\underbrace{t_{1/2,eff}}_{\text{유효 반감기}}
=\underbrace{\ln(2)}_{\text{50\% 변환}}\cdot\underbrace{MRT}_{\text{평균 체류}}
$$

이게 반복투여 축적 관점에서 진짜 의미 있는 반감기임. [G&W p.151; R&T pp.789–793]

### 3.4 MIT — 입력 시간을 빼야 진짜 체류시간이 나옴

관측된 $AUMC/AUC$에는 약물이 전신순환에 들어오기까지 걸린 시간이 섞여 있음. 이걸 그대로 두면 **투여 과정이 만든 지연을 진짜 체류시간으로 착각**하게 됨. 그래서 평균 입력 시간(Mean Input Time, MIT)을 빼야 함:

$$
\underbrace{MRT_{\text{corrected}}}_{\text{보정 MRT}}
=\underbrace{\frac{AUMC}{AUC}}_{\text{관측 MRT}}-\underbrace{MIT}_{\text{입력 평균시간}}
$$

투여 경로별 MIT는 이렇게 분기됨:

| 투여 방식 | MIT | 보정 MRT |
|---|---:|---|
| IV bolus | 0 | $AUMC/AUC$ |
| 일정 IV infusion ($T_{inf}$) | $T_{inf}/2$ | $AUMC/AUC - T_{inf}/2$ |
| 1차 혈관외 흡수 ($K_a$) | $1/K_a$ | $AUMC/AUC - 1/K_a$ |

$$
MIT\in\Bigl\{\underbrace{0}_{\text{IV bolus}},\ \underbrace{T_{inf}/2}_{\text{주입 중간점}},\ \underbrace{1/K_a}_{\text{흡수 평균}}\Bigr\}
$$

⚠️ **주의 한 줄** — 경구에서 $1/K_a$를 "순수 흡수 시간"으로 과해석하면 안 됨. $K_a$는 흡수만이 아니라 **분해(degradation) 같은 병렬 과정**까지 포함할 수 있음. [G&W p.150]

### 3.5 C2 마무리

> **MRT는 반감기가 아님. MRT는 "분자가 계 안에서 보낸 시간의 평균"이고, 계산상으로는 $AUMC/AUC$이며, 투여 경로에 따라 MIT를 빼야 비로소 해석 가능한 체류시간이 됨.**

→ **C3로 전파되는 것:** AUMC 꼬리 오류와 MIT 누락은 둘 다 MRT를 거쳐서 V_ss로 흘러감. 그리고 C3에서는 이 오류가 **"분포용적"이라는 임상 이름표**를 달고 등장함 — 그 이름표가 오류를 가려버림.

---

## 4. C3 — 임상 파라미터로 굳어졌을 때: CL, V_ss, V_z [⚡ Apex Concept]

### 4.1 C3가 왜 Apex인가

C1이 AUC를 만들고, C2가 MRT를 만들었다면, **C3는 이 둘을 임상 언어인 "청소율(CL)"과 "분포용적(V)"으로 번역하는 단계**임. 그래서 C3의 숫자는 독립적으로 계산된 값이 아니라, **앞 두 카드의 가정 오류가 임상 파라미터 이름표를 달고 굳어진 최종 형태**임.

문제는 이 이름표가 오류를 가린다는 것임. NCA 표에 CL, V_ss, V_z가 같은 단위로 나란히 출력되니까 셋 다 같은 신뢰도로 읽기 쉬움. 그런데 셋이 상속하는 오류는 다 다름:

| 파라미터 | 의존 항목 | 어떤 가정이 깨지면 흔들리는가 |
|---|---|---|
| **CL** | 투여량, $AUC_0^\infty$ | C1의 AUC 꼬리 오류 |
| **V_ss** | CL, MRT, AUMC | C1 + C2 + MIT 보정 (의존성 가장 큼) |
| **V_z** | CL, λz | C1의 λz 선택 |

V_ss가 가장 많은 가정 위에 얹혀 있음. 그래서 셋 중 **가장 깨지기 쉬운 파라미터**임. 그런데 표에서는 그게 안 보임.

### 4.2 핵심 수식 — 단위 분해부터

**청소율(IV):** [G&W p.149, Eq.2:325]

$$
\underbrace{CL}_{\text{정화부피/시간}}
=\frac{\underbrace{D_{iv}}_{\text{IV 용량}}}{\underbrace{AUC_0^\infty}_{\text{총 노출}}}
$$

**경구 겉보기 청소율:** [G&W p.149, Eq.2:326]

$$
\underbrace{CL/F}_{\text{겉보기 CL}}
=\frac{\underbrace{D_{po}}_{\text{경구 용량}}}{\underbrace{AUC_0^\infty}_{\text{총 노출}}}
$$

**생체이용률:** [G&W p.149, Eq.2:327]

$$
\underbrace{F}_{\text{도달 분율}}
=\overbrace{\frac{AUC_{po}}{AUC_{iv}}}^{\text{노출비}}
\cdot\overbrace{\frac{D_{iv}}{D_{po}}}^{\text{용량 보정}}
$$

**정상상태 분포용적:** [G&W p.151, Eq.2:337]

$$
\underbrace{V_{ss}}_{\text{정상상태 V}}
=\overbrace{\underbrace{MRT}_{\text{보정 MRT}}\cdot\underbrace{CL}_{\text{정화}}}^{\text{체류 × 정화}}
=\frac{\underbrace{D_{iv}}_{\text{IV 용량}}\cdot\underbrace{AUMC_0^\infty}_{\text{시간가중 노출}}}{\underbrace{(AUC_0^\infty)^2}_{\text{노출 제곱}}}
$$

**말단 분포용적:** [G&W p.151, Eq.2:338]

$$
\underbrace{V_z}_{\text{말단 V}}
=\frac{\underbrace{CL}_{\text{정화}}}{\underbrace{\lambda_z}_{\text{말단 기울기}}}
=\frac{\underbrace{D_{iv}}_{\text{IV 용량}}}{\underbrace{AUC_0^\infty}_{\text{총 노출}}\cdot\underbrace{\lambda_z}_{\text{말단 기울기}}}
$$

### 4.3 V_ss vs V_z — 같은 단위, 완전히 다른 질문

이게 NCA 학습의 **세 번째이자 가장 위험한 함정**임. 두 값 모두 volume 단위로 같은 표에 출력되고, 둘 다 양수로 정상 범위에 들어오면 "분포 부피니까 어느 쪽이든 비슷한 의미겠지"라고 읽기 쉬움. 실제로는 답하는 질문이 다름:

| | V_ss | V_z |
|---|---|---|
| 정의식 | $MRT \cdot CL$ | $CL/\lambda_z$ |
| 답하는 질문 | 정상상태에서 약물이 차지하는 평균 분포 크기는? | 말단 기울기가 보여주는 겉보기 부피는? |
| 의존 가정 | AUC + AUMC + MIT 보정 (의존성 최대) | AUC + λz (의존성 중간) |
| 흔들리는 방향 | MIT 누락·AUMC 꼬리 오류로 ↑↓ | λz 선택 오류로 ↑ |

💡 **단서 한 줄로** — **두 부피가 어긋나는 방향이 곧 어디서 가정이 깨졌는지의 단서**임. V_ss만 비정상이면 → MIT 또는 AUMC 꼬리 문제. V_z만 비정상이면 → λz 선택 문제. 두 부피의 차이는 "오류 진단 게이지"로 읽음.

### 4.4 협역 치료역의 진짜 함정 — V_c(V₁) 기준 부하용량

이게 임상 안전성 직결 항목임. 부하용량(loading dose, LD)을 산정할 때 흔히 "V_ss × C_target"으로 계산하는데, **협역 치료역 다구획 약물에서는 이게 위험함**.

이유는 단순함 — IV bolus 직후 약물은 일시적으로 **중앙구획에만 분포**함. 분포 평형이 일어나기 전 짧은 시간 동안 $C_0 = LD/V_c$가 됨. 그러니까 부하용량의 진짜 기준은 V_ss나 V_z가 아니라 **V_c (중앙구획 부피, $V_1$)**임.

$$
\underbrace{LD_{\text{임상 표준}}}_{V_c\ \text{기준}}
=\overbrace{V_c\cdot C_{target}}^{\text{중앙구획 dilution}}
\ \leq\ \overbrace{V_{ss}\cdot C_{target}}^{\text{전신 분포 기준 (과대 위험)}}
\ \leq\ \overbrace{V_z\cdot C_{target}}^{\text{과대추정 (위험)}}
$$

**구체 예시:** 어떤 다구획 약물에서 $V_c=4$ L, $V_{ss}=12$ L, $V_z=20$ L, $C_{target}=2$ mg/L라고 하면:

| 부하용량 산정 기준 | LD | 초기 농도 $C_0=LD/V_c$ | 결과 |
|---|---:|---:|---|
| $V_c$ (4 L) — 임상 표준 | 8 mg | **2 mg/L** | 표적 도달, OK |
| $V_{ss}$ (12 L) — 잘못된 선택 | 24 mg | **6 mg/L** | 표적의 **3배** → peak toxicity |
| $V_z$ (20 L) — 더 잘못된 선택 | 40 mg | **10 mg/L** | 표적의 **5배** → severe |

협역 치료역 약물 예시로 **digoxin**(강심배당체로 부정맥에 쓰임 — 혈중 농도 폭이 좁아서 조금만 높아도 독성, 조금만 낮으면 무효)이나 **aminoglycoside**(gentamicin·amikacin 같은 광범위 항생제 — 신독성·이독성 때문에 협역 치료역에 들어감)를 생각하면, V_ss 기반 LD는 즉시 peak toxicity를 일으킴.

R&T Chapter 19가 신부전 환자의 gentamicin 용량 조정에서 **terminal phase를 무시하고 $V_1$ 기반으로 LD를 계산**하는 임상 관행을 명시하는 이유가 정확히 이거임. [R&T pp.626, 632–636]

🔑 **세 부피의 역할 분리** — 협역 치료역에서 다음 분리가 깨지면 환자 안전이 깨짐:

- **부하용량(LD)** → $V_c$ 기준
- **유지용량(MD)** → $CL$ 기준
- **분포 평형 후 농도 해석** → $V_{ss}$ 기준
- **V_z**는 진단용 — 단독으로 임상 의사결정에 쓰지 않음

[G&W pp.66, 151; R&T pp.626, 632–636]

### 4.5 표준식이 무너지는 영역 — §2.8.8 적용 영역

표준 V_ss 식(Eq.2:337)에는 적용 영역이 있음. **입력 시간($T_{inf}$)이 반감기($t_{1/2}$)에 비해 매우 길어질 때**, 즉 infusion이 elimination을 우세하게 만들 때 표준식이 무너짐.

G&W §2.8.8 원문은 영역을 직접 명시함 — *"the duration of infusion is much greater than $t_{1/2}$"* [G&W p.157]. 분기는 **$T_{inf}/t_{1/2}$ 비율 하나**에서 갈림.

$$
\underbrace{\frac{T_{inf}}{t_{1/2}}}_{\text{판정 비율}}\uparrow
\ \Rightarrow\
\underbrace{\frac{AUMC}{AUC}-\frac{T_{inf}}{2}}_{\text{표준 MRT 식}}\ \to\ 0\ \text{또는 음수}
$$

표준식이 0이나 음수 V_ss를 출력하기 시작하면 그건 "값이 틀린" 게 아니라 **적용 영역을 벗어났다는 신호**임. 이때 G&W는 정상상태 이후 washout AUC를 이용한 대안식을 제시함:

$$
\underbrace{V_{ss}}_{\text{대안 V_ss}}
=\frac{\underbrace{K_0}_{\text{주입 속도}}\cdot\underbrace{AUC_{t^*\to\infty}}_{\text{washout AUC}}}{\underbrace{C_{ss}^2}_{\text{농도 제곱}}}
$$

$$
\underbrace{MRT}_{\text{washout MRT}}
=\frac{AUC_{t^*\to\infty}}{C_{ss}}
$$

**두 식의 적용 영역을 한 표로 압축:** [G&W pp.151, 157]

| | Eq.2:337 (표준식, §2.8.7) | Eq.2:366 (대안식, §2.8.8) |
|---|---|---|
| $T_{inf}/t_{1/2}$ | 작거나 중간 | 큼 ($T_{inf} \gg t_{1/2}$) |
| 필요 데이터 | $AUMC_0^\infty$, $AUC_0^\infty$, MIT | $C_{ss}$, washout $AUC_{t^*\to\infty}$, $K_0$ |
| 핵심 수식 | $V_{ss}=D_{iv}\cdot AUMC/(AUC)^2$ | $V_{ss}=K_0\cdot AUC_{t^*\to\infty}/C_{ss}^2$ |
| 수치 거동 | 적용 영역 내 안정 양수 | 표준식 무너지는 영역에서 양수 보존 |
| Sanity check | 두 식 결과가 잘 맞으면 → 표준식 영역 OK | 두 식 결과가 크게 벌어지면 → 적용 영역 이탈 신호 |

$$
\underbrace{\frac{T_{inf}}{t_{1/2}}}_{\text{판정 비율}}\
\begin{cases}
\overbrace{\text{작거나 중간}}^{\text{Eq.2:337 영역}}\ \Rightarrow\ V_{ss}\text{ 양수, 안정}\\[4pt]
\overbrace{\gg 1}^{\text{Eq.2:366 영역}}\ \Rightarrow\ \text{Eq.2:337 → 0 또는 음수, Eq.2:366 채택}
\end{cases}
$$

💡 **비유 한 줄로** — 표준 V_ss 식은 "입구가 짧고 몸 안 체류가 충분히 긴 물탱크"의 수위를 재는 방식임. 주입 시간이 체류시간만큼 길어지면, 수위계는 탱크 크기가 아니라 **수도꼭지를 얼마나 오래 열어뒀는지**를 더 크게 읽어버림.

> 💼 **현장 감각** — SOP가 표준 Eq.2:337만 허용하는 회사에서 §2.8.8 대안식이 더 타당한 케이스를 만났다면, **두 식을 모두 계산해서 차이를 같이 제시**함. SOP deviation은 "더 예쁜 결과"가 아니라 **0이나 음수 V_ss를 피하는 출처 기반 수학적 정당화**로 문서화됨. 보고서 안에 두 식의 출력 차이, $T_{inf}/t_{1/2}$ 비율, Eq.2:337 적용 영역 이탈 근거, 대안식 채택 사유를 한 박스에 정리하면 감독관도 그대로 따라옴.

### 4.6 비선형 PK가 NCA를 죽이는 순간 — 한계(Limitations)

| 상황 | 무엇이 흔들리는가 | 임상 결과 | 조치 |
|---|---|---|---|
| Flip-flop kinetics (흡수가 제거보다 느림) | 경구 λz가 제거가 아니라 흡수를 반영 | V_z·V_ss가 그럴듯한 양수로 잘못 출력 | IV 기준 정보 또는 흡수 제한 caveat 명시 |
| 비선형 소실 | CL과 t½가 용량 의존적 | 1차 파라미터 해석 실패 | capacity-limited model 전환 [G&W p.664] |
| NCA-derived IIV의 과사용 | 잔차/오차까지 IIV에 섞임 | PopPK $\omega^2$ inflation | NCA 분산은 상한값으로만 사용 |

> 💼 **현장 감각** — NCA 유래 변동성은 PopPK IIV의 직접 추정값이 아니라 **잔차 변동성까지 섞인 상한값**임. 이 상한을 PopPK $\omega^2$ 초기값으로 그대로 입력하면 **IIV가 RUV를 흡수하면서 후속 공변량 회귀가 묻혀버림**. 이건 보고서 검토 단계에서 잘 안 잡히고 PopPK 모델링 단계에서 한참 후에 발견됨. 처음부터 보수적으로 잡는 게 답임.

### 4.7 C3 마무리

> **V_ss는 "분포 부피 하나"가 아니라, AUC·AUMC·CL·투여 경로 보정이 모두 통과한 최종 요약값임. V_ss를 볼 때마다 "어떤 MRT를 썼는가? 입력 시간을 뺐는가? 표준식 영역에 있는가?"를 같이 봐야 함.**

→ **C4로 전파되는 것:** CL과 V가 정해지면 이제 **어떤 노출 지표로 PD/safety를 논증할 것인가**의 단계임. 같은 CL이라도 endpoint가 peak-driven인지 누적인지에 따라 보고해야 할 노출 지표가 달라짐.

---

## 5. C4 — 어떤 노출 지표로 PD/safety를 볼 것인가

### 5.1 "dose가 같으면 response도 같다" — 이 명제가 깨지는 다섯 가지 길

C4의 출발점은 단순함 — **dose는 투입량이고 노출은 몸이나 표적이 실제로 본 농도-시간 부담**임. 둘이 같으리라는 보장은 없음. dose와 effective exposure 사이에 끼어드는 게 다섯 가지나 있음:

1. **투여 경로(route)** — 같은 dose라도 IV/PO/IM/SC에서 노출이 다름
2. **초회통과(first-pass)** — 경구의 F < 1
3. **비선형 소실** — 용량 증가에 비례하지 않는 노출 증가
4. **활성 대사체** — 모약물만 보면 반응을 오해
5. **단백 결합 차이** — 총 농도가 같아도 unbound가 다름

그러니까 **노출 지표를 dose 대신 보는 게 아니라, endpoint가 무엇을 묻는지에 맞춰 노출 지표를 선택**하는 게 진짜 작업임.

### 5.2 노출 지표 — endpoint의 언어

| 지표 | 의미 | 사용 직관 | 출처 |
|---|---|---|---|
| $C_{max}$ | 최고 노출 | 급성 독성, peak-driven effect | [G&W p.163] |
| AUC | 총 노출 | 누적 노출, extent 비교 | [G&W p.163] |
| $t_d$ | 역치 이상 지속시간 | time-above-threshold 효과 | [G&W p.163] |
| $C_{ss}$ / $C_{av}$ | 정상상태 강도 | 만성 투여 노출 | [G&W p.163] |
| $C_u$ (비결합) | 약리학적으로 사용 가능한 분율 | 단백 결합 차이 비교 | [G&W p.163] |

비결합 농도 정의:

$$
\underbrace{C_u}_{\text{비결합농도}}
=\underbrace{C_{total}}_{\text{총농도}}\cdot\underbrace{f_u}_{\text{비결합률}}
$$

💡 **선택 규칙 한 줄로** — dose부터 보지 말고, **endpoint mechanism**을 먼저 정하고 노출 지표를 고름. 독성이 peak-driven이면 $C_{max}$, 누적 부담이면 AUC, threshold라면 $t_d$, 단백 결합이 변하는 상황이면 $C_u$ — 이 mapping이 깨지면 노출-반응 정당화가 깨짐.

### 5.3 §2.9 사례 압축 — "dose 같은데 response 다른" 일곱 시나리오

| 사례 | 핵심 교훈 | 출처 |
|---|---|---|
| 투여 경로/생체이용률 | 용량-반응이 경로 차이로 흔들려도 농도-반응은 정렬될 수 있음 | [G&W p.159] |
| 비선형 소실 | 용량 증가가 노출과 안전역을 **비선형으로** 바꿈 | [G&W p.159] |
| 활성 대사체 | 모약물 농도만 보면 경로 의존 반응을 오해함 | [G&W p.160] |
| 투여 방식 | 같은 일일 용량이라도 주입/섭식 패턴이 독성을 바꿈 | [G&W p.160] |
| 점유율/바이오마커 | 리간드 농도·수용체 점유율·바이오마커 반응은 **같은 축이 아님** | [G&W p.161] |
| 반복 섭식 | 단회 + 섭식 시뮬레이션이 반복급여 노출을 과대예측할 수 있음 | [G&W p.162] |
| U자형 반응 | 노출-반응이 단조가 아니면 용량만으로 효과 예측 불가 | [G&W p.162] |
| 단백 결합 | 총 농도와 비결합 농도가 **효능 순위를 뒤집을 수 있음** | [G&W p.163] |

### 5.4 정상상태 노출 — 평균만 보면 안 되는 이유

반복투여 정상상태에서는 단회 노출 지표들이 **dosing interval 내 비교 가능한 지표**로 재정의됨. 핵심부터:

**$AUC_{0-\tau,ss}$는 단회 $AUC_{0-\infty}$와 동등**함. 이전 투여로 남은 잔류 면적과 현재 투여의 외삽 꼬리가 정확히 상쇄되기 때문임. [G&W p.152, Fig.2.122]

그 위에 정상상태 특유의 정량 지표들이 얹힘:

| 정상상태 지표 | 정의 | 임상적 질문 |
|---|---|---|
| $AUC_{0-\tau,ss}$ | $\int_0^\tau C_{ss}(t)\,dt$ | dosing interval 내 누적 노출 |
| $C_{av,ss}$ | $AUC_{0-\tau,ss}/\tau$ | 정상상태 평균 농도 |
| $C_{max,ss}$, $C_{min,ss}$ | interval 내 최고·최저 | peak/trough 안전성·효능 경계 |
| **PTF%** | $(C_{max,ss}-C_{min,ss})/C_{av,ss} \times 100$ | 같은 평균에서 분할 횟수가 만든 변동폭 |
| $R_{ac}$ (누적지수) | $AUC_{ss}/AUC_{single} \approx 1/(1-e^{-k\tau})$ | 단회 대비 정상상태 축적도 |

$$
\overbrace{\underbrace{PTF\%}_{\text{변동지수}}
=\frac{\underbrace{C_{max,ss}-C_{min,ss}}_{\text{진폭}}}{\underbrace{C_{av,ss}}_{\text{평균}}}\times 100}^{\text{R\&T Eq.\ Fig.11-14}}
$$

**구체 예시 — q24h vs q8h:** 같은 일일 용량 1200 mg을 1200 mg q24h로 줄 때와 400 mg q8h로 줄 때를 비교함. 정상상태 평균 농도($C_{av,ss}=D_{daily}/(CL\cdot 24h)$)는 **두 경우 모두 같음**. 그런데 PTF%는 q24h가 q8h보다 훨씬 큼 — interval이 길수록 peak는 높아지고 trough는 낮아지니까.

이게 임상에서 결정적인 이유:

- **Peak-driven 독성** (예: aminoglycoside의 이독성·신독성) → q24h에서 더 위험할 수도, 안전할 수도 있음 (drug-specific)
- **Trough-driven 효능** (예: vancomycin의 $AUC_{24}/MIC$) → trough 노출 정량에 직접 의존
- **Time-above-MIC 항생제** (예: β-lactams) → trough가 MIC 위로 유지되는 시간이 결정적

> 💼 **현장 감각** — 정상상태 NCA 보고서에 $C_{av,ss}$ 한 값만 적으면 PTF가 숨음. "같은 평균 = 같은 노출"이라는 단순화가 임상적 차이를 가림. PopPK 검증에서도 simulation의 PTF가 관측 PTF를 재현하지 못하면 **흡수 모델(Ka)이나 분포 모델($V_c$/Q)이 underfit된 신호**로 봄.

🔑 **정상상태 보고 규칙** — $AUC_{0-\tau,ss}$, $C_{av,ss}$, $C_{max,ss}$, $C_{min,ss}$, **PTF%**, $R_{ac}$를 한 세트로 보고함. 평균만 보고하면 분할 횟수가 만든 임상 차이가 사라짐.

### 5.5 Partial AUC — modified-release vs immediate-release의 정량 anchor

특정 시간 구간의 부분 면적($AUC_{0-t_1}$ 등)이 전체 $AUC_{0-\infty}$와 별도로 보고되는 가장 흔한 자리가 **MR vs IR 비교**임. 두 제형이 같은 $AUC_{0-\infty}$를 만들어도 **농도-시간 곡선의 모양**이 다르면 효과가 다를 수 있음. 전체 면적은 같은데 초기 노출이 다르거나 후기 노출이 다르면, 그게 임상적으로 더 중요함.

$$
\underbrace{AUC_{0-t_1}}_{\text{partial AUC}}
=\underbrace{\int_0^{t_1}C(t)\,dt}_{\text{구간 적분}}
\overbrace{\neq}^{\text{일반적으로}}
\underbrace{\frac{t_1}{\tau}\cdot AUC_{0-\infty}}_{\text{비례 가정}}
$$

§2.9의 "투여 방식" 사례 — 같은 일일 용량이라도 주입/섭식 패턴이 독성을 바꾼다는 메시지가 여기서 **정량적으로 회수**됨. [G&W p.160]

EMA의 modified-release BE 가이던스는 다음을 요구함:

- **Early partial AUC** ($AUC_{0-t_{max,reference}}$) — onset of action 동등성 검정, 90% CI 0.80–1.25
- **Late partial AUC** ($AUC_{t_{max,reference}-\tau}$) — duration of action 동등성 검정, 90% CI 0.80–1.25

전체 AUC 하나만으로는 농도 곡선 **모양** 차이를 못 잡으니까.

| 상황 | Partial AUC 선택 | 임상 함의 |
|---|---|---|
| MR vs IR (단회) | $AUC_{0-t_{max,IR}}$ | 초기 노출 동등성 — onset |
| MR vs IR (단회) | $AUC_{t_{max,IR}-\tau}$ | 후기 노출 동등성 — duration |
| Food effect | $AUC_{0-2h}$ 또는 $AUC_{0-4h}$ | 흡수 지연/촉진 정량 |
| DDI | onset 구간 partial AUC | 빠른 흡수 약물의 DDI 초기 영향 |

> 💼 **현장 감각** — Partial AUC 누락된 MR vs IR 비교는 EMA 심사에서 보충 요구가 자주 옴. 같은 $AUC_{0-\infty}$로 BE 통과해도 농도 곡선 모양이 다르면 임상 동등성이 보장되지 않음. Partial AUC는 dose-normalize 비교보다 **$t_{max,reference}$ 기준 절대 시간 구간**으로 비교하는 게 표준임.

### 5.6 C4 마무리

> **dose가 같아도 response가 같다는 보장은 없음. route·first-pass·비선형 소실·단백결합·활성 대사체 — 이 다섯 길이 dose와 effective exposure 사이에 끼어듦. exposure-response를 정당화하려면 endpoint가 peak-driven인지, 누적인지, threshold인지, unbound인지부터 정해야 함.**

---

## 6. PK41 회수 — NCA에서 비선형 회귀로

이제 도입부의 PK41을 회수함. C1–C4를 다 거쳐온 시점이라 같은 표가 완전히 다르게 읽힘.

### 6.1 다시 보는 PK41 표

| 용량 (µg·kg⁻¹) | NCA-CL (L·h⁻¹·kg⁻¹) | V (L·kg⁻¹) | MRT (h) |
|---:|---:|---:|---:|
| 310 | 1.6 | 2.3 | 1.4 |
| 520 | 1.2 | 2.0 | 1.6 |
| 780 | 0.9 | 1.8 | 1.9 |

처음 봤을 때와 다르게, 이제 우리는 이 표를 이렇게 읽음:

1. **CL 단조 감소** — C1이 가르쳐준 것: AUC가 용량에 비선형적으로 증가하고 있다는 신호. 그런데 이건 단순한 "AUC 측정 오류"가 아님. 모든 용량에서 일관되게 같은 방향으로 움직임.
2. **V 단조 감소 + MRT 단조 증가** — C2·C3가 가르쳐준 것: 단순히 분포 부피가 줄어든 게 아니라, **분자가 더 오래 머무르고 있음**. 같은 분량이 더 천천히 빠져나가는 상황임.
3. **세 변화가 일관됨** — C4가 가르쳐준 것: 이건 "한 칸이 흔들린 보고서"가 아니라, **시스템 전체가 다른 동력학으로 넘어갔다는 신호**임.

### 6.2 모델 전환 — 선형 CL에서 Michaelis-Menten으로

CL이 용량 의존적으로 감소하면, "CL은 더 이상 농도와 무관한 상수가 아니다"라는 뜻임. 즉, 모델 자체를 바꿔야 함:

$$
\underbrace{V\cdot\frac{dC}{dt}}_{\text{체내 변화율}}
=\underbrace{In}_{\text{입력}}-\underbrace{CL\cdot C}_{\text{제거}},
\qquad
\underbrace{CL}_{\text{농도의존 CL}}
=\frac{\underbrace{V_{max}}_{\text{최대 제거}}}{\underbrace{K_m+C}_{\text{포화 경계}}}
$$

💡 **비유 한 줄로** — 선형 CL은 **배수구 지름이 일정한 욕조**임. 물이 많든 적든 같은 비율로 빠짐. Michaelis-Menten CL은 **배수구가 포화되는 욕조** — 물이 차오를수록 단위 시간당 빠지는 비율이 떨어짐. "용량이 커질수록 같은 'CL'이라는 이름으로는 더 이상 배수 능력을 설명할 수 없다"는 게 PK41이 폭로한 사실임.

### 6.3 NCA 결과가 비선형 회귀의 anchor가 되는 동선

NCA 결과를 그대로 초기값으로 투입함:

- V (NCA) ≈ 2 L/kg → 초기 V ≈ 2 L/kg
- 가장 낮은 용량의 CL ≈ 1.6 L·h⁻¹·kg⁻¹ → $V_{max}/K_m \approx 1.6$ 추정
- 농도 절반인 지점에서 CL 감소 시작 → 초기 $K_m \approx 150$ µg/L
- 최대 CL ≈ $V_{max}/(K_m+C)$의 plateau → 초기 $V_{max} \approx 310$ µg·h⁻¹·kg⁻¹

NONMEM에서 회귀 후 **최종 추정값**: $V_{max}=184$ µg·h⁻¹·kg⁻¹, $K_m=83$ µg/L, $V=1.8$ L/kg.

G&W 저자의 결론이 결정적임 — **용량 제한 1구획 시스템의 파라미터는 CL과 V가 아니라 $V_{max}$, $K_m$, V임. CL과 $t_{1/2}$는 혼합 0차/1차 동력학과 양립할 수 없음(incompatible).** [G&W pp.663–664]

이게 NCA→비선형 회귀 전환의 한 줄 명제임:

> **NCA가 출력한 "CL"은 비선형 시스템에서는 더 이상 의미 있는 파라미터가 아님. NCA 결과는 회귀의 출발점일 뿐, 도착점이 아님.**

이 자료의 첫 줄에서 던졌던 thesis가 PK41을 통해 증명됨. NCA 표는 진술서이고, 진술서는 다음 모델(Michaelis-Menten 또는 PopPK)을 향한 anchor임.

---

## 7. 혼동쌍 압축 — §5 재방문

이미 본문에서 다뤘지만, 한 번 더 압축 정리. 표 한 장으로 끝냄.

### 쌍 1. AUC vs AUMC (C2에서 다뤘음)

| | AUC | AUMC |
|---|---|---|
| 차원 | 농도 × 시간 | 농도 × 시간² |
| 꼬리 | $C_{last}/\lambda_z$ | $t_{last}C_{last}/\lambda_z + C_{last}/\lambda_z^2$ |
| λz 오류 민감도 | 1차 | **2차 (1/λz² 항)** |
| 혼동의 임상 결과 | 총 노출과 CL 왜곡 | MRT와 V_ss 증폭 왜곡 |

**⚡ 기억 고리:** AUMC 꼬리는 $1/\lambda_z^2$ 항이 박혀 있어서 **같은 λz 오류라도 두 배로 증폭됨**.

### 쌍 2. MRT vs t½ (C2에서 다뤘음)

| | MRT | t½ |
|---|---|---|
| 정의 | 분자 평균 체류시간 | 농도 50% 감소 시간 |
| 계산 | $AUMC/AUC$ - MIT | $\ln(2)/\lambda_z$ |
| 다구획 거동 | 분포기 정보 흡수 | 말단 기울기만 기술 |
| 혼동의 결과 | 입력 지연을 반감기로 오해 | 다상 프로파일에서 단일 반감기 과해석 |

**⚡ 기억 고리:** 1구획 단일지수에서만 두 값이 단순 비율($1/\ln 2$)로 연결됨. 다구획에서는 다른 것을 측정함. 그래서 **유효 반감기는 $\ln(2)\cdot MRT$**로 재정의됨.

### 쌍 3. V_ss vs V_z (C3에서 다뤘음)

| | V_ss | V_z |
|---|---|---|
| 정의 | $MRT \cdot CL$ | $CL/\lambda_z$ |
| 의존 가정 | AUC + AUMC + MIT (최대) | AUC + λz (중간) |
| 흔들리는 방향 | MIT 누락·AUMC 꼬리로 ↑↓ | λz 선택 오류로 ↑ |
| **치명적 혼동** | $V_z$를 $V_{ss}$로 혼동하면 다구획 약물 LD 과대 → **초기 독성 농도** | |

**⚡ 기억 고리:** **두 부피가 어긋나는 방향이 곧 어디서 가정이 깨졌는지의 단서**임. 그리고 **협역 치료역 임상 LD의 진짜 기준은 $V_c$(중앙구획) — V_ss도 V_z도 아님**.

$$
\underbrace{LD}_{\text{loading dose}}=
\overbrace{V_c\cdot C_{target}}^{\text{협역 임상 표준}}
\ \leq\ V_{ss}\cdot C_{target}
\ \leq\ V_z\cdot C_{target}
$$

---

## 8. 자기 테스트 — 능동 회상 모듈

### Q1. 선형 사다리꼴과 로그-선형 사다리꼴의 차이는?
선형은 모든 구간에 적용 가능하지만 하강 구간에서 과대추정함. 로그-선형은 하강에서만 유효하고 $C_i=0$이면 정의 불가. 혼합 방식이 자주 쓰이지만 합리적 sampling에서는 두 방법 차이가 임상적으로 작음. [G&W pp.143–146]

### Q2. λz 추정의 최소·이상 조건은?
최소 3–4 관측점, 이상적으로 말단기에서 3–4 반감기 경과. 자동 출력을 그대로 믿지 말고 반로그 도표에서 직접 확인. R²가 높아도 분포기 점이 섞이면 λz 평탄화로 AUC 꼬리·CL·V_z 동시 왜곡. [G&W pp.146–147]

### Q3. 외삽 AUC가 30%면?
G&W 권고(20–25%)를 넘으니까 **예비 추정값**으로 보고. 추가 표본추출 또는 말단기 재검토 필요. [G&W p.148]

### Q4. BLQ 값이 (a) 첫 정량 가능 시점 이전 (b) 중간 (c) 말단에 있을 때 처리는?
(a) IV는 0, 경구는 결측/보간 검토. (b) 선형 보간 또는 결측 — 0 대체는 AUC 과소. (c) 결측 처리 권장 — 0 대체는 $\ln 0$로 회귀 불능, BLQ를 말단 회귀 포함 시 λz 평탄화. **Gabrielsson 원칙: "지수 모델에서는 LOQ 미만 값을 0이나 LOQ로 절대 대체하지 말고 missing으로 처리"**. [G&W p.153]

### Q5. R&T Table H-1에서 $AUC=44.2$, $AUMC=177$이면 혈장 MRT는?
$MRT = AUMC/AUC = 177/44.2 \approx 4.0$ hr. 같은 예시에서 소변 MRT ≈ 4.25, simulated MRT ≈ 4.3 — 세 경로 일관. [R&T p.792]

### Q6. IV bolus와 경구에서 CL 계산의 차이?
IV: $CL = D_{iv}/AUC_0^\infty$. 경구: $CL/F = D_{po}/AUC_0^\infty$ (겉보기 CL). F가 분리되지 않음. [G&W p.149]

### Q7. 급성 독성·누적 노출·역치 효과에 어떤 노출 지표를 우선?
급성 독성 → $C_{max}$. 누적 노출 → AUC. 역치 효과 → $t_d$ 또는 역치 초과 AUC. 약물 기전과 반응 시간경과에 맞춰 정당화. [G&W p.163]

### Q8. 총 농도와 비결합 농도 기준 효능 순위가 뒤집힐 수 있는 이유?
단백 결합이 다르면 같은 총 농도에서도 약리학적으로 사용 가능한 unbound 농도가 다름. §2.9 메시지는 총 농도보다 **비결합 전신 노출**이 더 직접적인 비교 기준이 될 수 있다는 것. [G&W p.163]

### Q9. **보스 딜레마** — SOP는 표준 Eq.2:337만 허용하는데 $T_{inf}$가 반감기에 비해 매우 길어 §2.8.8 대안식이 더 타당해 보임. 어떻게?
표준식과 §2.8.8 대안식을 **둘 다 계산해서 차이를 같이 제시**. 차이 원인이 $T_{inf}/t_{1/2}$ 비율에 있다는 걸 설명. **방향 명확화: 비율이 커지는 쪽($T_{inf} \gg t_{1/2}$, infusion이 elimination을 우세하게 만드는 영역)에서 표준식이 0이나 음수 V_ss로 무너짐.** SOP deviation은 "더 예쁜 결과"가 아니라 **0/음수 V_ss를 피하는 수학적 정당화**로 문서화 — 두 식 출력 차이, $T_{inf}/t_{1/2}$ 비율, Eq.2:337 적용 영역 이탈 근거, 대안식 채택 사유를 한 박스에 정리. [G&W pp.151, 157]

### Q10. q24h와 q8h가 같은 일일 용량인데 임상 결과가 다를 수 있는 이유는?
$C_{av,ss} = D_{daily}/(CL \cdot 24h)$이라 dosing interval과 무관해서 두 regimen에서 같음. 그런데 **PTF%**는 q24h가 훨씬 큼 — interval 길수록 peak↑·trough↓. Peak-driven 독성(예: aminoglycoside)이나 trough-driven 효능(예: vancomycin AUC₂₄/MIC)은 PTF에서 갈리고, 평균만 보고하면 이 정보 사라짐. [R&T p.340, Fig.11-14; pp.276, 325]

### Q11. 두 제형 BE 검정에서 test/reference의 AUC 비율 90% CI가 0.88–1.18이면?
**0.80–1.25 acceptance criterion 안에 90% CI가 완전히 들어가므로 bioequivalent로 선언 가능**. 90% CI를 쓰는 이유는 BE가 TOST(two one-sided tests) 구조로 검정되기 때문 — 각 측 α=0.05 양측 합산이 90% CI에 대응. 95% CI는 BA 비교나 학술 보고용이고, BE 규제 판정 기준은 90% CI. 고변동성 약물(intra-subject CV>30%)에서는 reference-scaled framework로 acceptance bound 확장. [R&T pp.182–195]

### Q12. **결정적 시나리오** — 협역 치료역 다구획 약물의 NCA 보고서에서 $V_c=4$ L, $V_{ss}=12$ L, $V_z=20$ L. 표적 농도 $C_{target}=2$ mg/L에 도달하기 위한 LD 산정에 어느 부피를?
**$V_c$ 기준** — $V_{ss}$가 아님. IV bolus 직후 약물은 일시적으로 중앙구획에만 분포. 분포 평형 전 $C_0 = LD/V_c$.

$$
\underbrace{LD_{\text{임상 표준}}}_{V_c\ \text{기준}}=\overbrace{V_c\cdot C_{target}}^{4\times 2}=\underbrace{8\ \text{mg}}_{\text{표적 도달}}
$$

$V_{ss}$로 계산하면 LD=24 mg → $C_0=6$ mg/L (표적의 **3배**, peak toxicity). $V_z$로 계산하면 LD=40 mg → $C_0=10$ mg/L (표적의 **5배**, severe).

$$
\underbrace{C_0=\frac{LD}{V_c}}_{\text{초기 농도}}\quad
\begin{cases}
\overbrace{V_c=4\Rightarrow C_0=2\ \text{mg/L}}^{\text{표적 도달, OK}}\\[4pt]
\overbrace{V_{ss}=12\Rightarrow C_0=6\ \text{mg/L}}^{\text{표적의 3배, peak toxicity}}\\[4pt]
\overbrace{V_z=20\Rightarrow C_0=10\ \text{mg/L}}^{\text{표적의 5배, severe}}
\end{cases}
$$

R&T Chapter 19가 신부전 환자의 gentamicin 용량 조정에서 **terminal phase 무시하고 $V_1$ 기반 LD 계산** 임상 관행을 명시하는 이유가 정확히 이거임. 정리: **부하용량은 $V_c$, 유지용량은 $CL$, $V_{ss}$는 분포 평형 후 농도 해석 기준** — 세 부피의 역할 분리가 임상 안전성의 기초. [G&W pp.66, 151; R&T pp.626, 632–636]

### Q13. PK41에서 NCA 결과가 비선형 회귀의 anchor가 되는 흐름은?
용량 증가에 따라 NCA-CL이 1.6 → 0.9로 단조 감소. 이는 용량 제한 소실(capacity-limited elimination) 신호. NCA는 최종 CL 보고가 아니라 $V_{max}$, $K_m$, V를 갖는 Michaelis-Menten 회귀의 **초기 추정값 anchor**가 됨. 최종 추정: $V_{max}=184$ µg·h⁻¹·kg⁻¹, $K_m=83$ µg/L, V=1.8 L/kg. **CL과 $t_{1/2}$는 혼합 0차/1차 동력학과 양립 불가**. [G&W pp.661–664]

---

## 9. 메타프레임 — 30년 연구자가 10분에 남기는 한 페이지

### 9.1 한 줄 명제 (다시)

> **NCA는 PopPK를 대체하는 분석이 아니라 모델링 전후에 활용하는 도구임. 모델 선택 전에는 EDA와 초기값을 만들고, 모델 추정 후에는 population prediction이 관측 노출의 규모와 일관되는지 확인하는 reference가 됨. NCA는 선형 소실을 가정 — 이걸 잊는 순간 "단순해서 강한 방법"이 "단순해서 틀린 방법"으로 바뀜.** [G&W p.141]

### 9.2 보고서 1페이지 체크리스트 (실무 동선)

이 자료 전체를 한 페이지로 압축하면 이거임. NCA 보고서가 도착했을 때 위에서부터 순서대로 확인:

| 단계 | 확인 항목 | 기준 | 깨질 때 신호 |
|---|---|---|---|
| ① | λz 선정 구간 | 반로그 도표에서 직접, 최소 3–4점, 3–4 t½ 경과 | 분포기 섞이면 평탄화 |
| ② | $C_{last}$ 처리 | 관측값이 회귀선 이탈 시 $\hat C_{last}$ 사용 | 외삽 꼬리 왜곡 |
| ③ | %extrapolated | 20–25% 이하 | 초과 시 "예비 추정" 표기 |
| ④ | BLQ 처리 규칙 (위치별) | SOP/SAP에 사전 명문화 | 사후 변경 = data dredging |
| ⑤ | MIT 보정 | 투여 경로별로 $0/T_{inf}/2/1/K_a$ | 누락 시 MRT·V_ss 왜곡 |
| ⑥ | V_ss vs V_z 정합성 | 어긋남 방향이 진단 단서 | 한쪽만 흔들리면 가정 위치 식별 |
| ⑦ | $T_{inf}/t_{1/2}$ 비율 | Eq.2:337 vs Eq.2:366 sanity check | 0/음수 V_ss는 적용 영역 이탈 |
| ⑧ | 용량별 CL 단조성 | 일정해야 선형 가정 유지 | 단조 감소/증가는 비선형 신호 |
| ⑨ | 노출 지표 선정 정당화 | endpoint mechanism 명시 | dose-only 해석은 부적격 |
| ⑩ | 1차 파라미터로 CL 또는 CL/F | AUC는 노출, CL은 생리학 anchor | 보고 순서 바뀌면 공변량 회귀 약화 |

### 9.3 후속 세션 연결 — 지식 그래프 위치

| 후속 세션 | 이 세션에서 열리는 개념 | 이 세션 없으면 실패하는 것 |
|---|---|---|
| **PopPK 초기 모수 설정** | NCA-derived CL, V, exposure anchor | 외삽 편향값을 NONMEM 초기값으로 투입 |
| **비선형 PK 회귀** | PK41의 capacity-limited signal | CL과 t½를 1차 파라미터처럼 과해석 |
| **BA/BE 보고서** | λz, %extrapolated, exposure metric audit trail | 가정 방어 없는 숫자표 |
| **BE 통계 검정** | $AUC_{0-\infty}$·$C_{max}$·partial AUC | 90% CI 0.80–1.25 검정 [R&T pp.182–195] |
| **Exposure-response 분석** | endpoint별 $C_{max}$/AUC/$t_d$/$C_u$ 선택 | dose-only PD/safety 정당화 실패 |
| **PopPK 모델 검증** | NCA 노출 anchor (관측 AUC/$C_{max}$) | VPC/CWRES/NPDE/MAP 진단의 reference 왜곡 |
| **PopPK BLQ likelihood (Beal M3)** | NCA BLQ 위치별 규칙 (SOP/SAP) | NCA의 missing과 PopPK의 censored likelihood 정렬 깨지면 $\omega^2$/$\sigma^2$ 분리 실패 |

📖 **BE 검정 보충** [R&T pp.182–184, Fig.6-13; Table 6-7 p.195]: Test/Reference 비율의 **90% CI**(log-transformed AUC와 $C_{max}$)가 **0.80–1.25 안에** 들어가야 bioequivalent로 선언. 95% CI가 아니라 90% CI를 쓰는 이유는 TOST의 통계 구조 — 양측 단측 검정에서 95% 신뢰성 확보하려면 각 측 α=0.05 검정이 양측 합쳐서 90% CI에 대응. 고변동성 약물(intra-subject CV>30%)은 **reference-scaled average bioequivalence (RSABE)** framework로 acceptance bound 확장.

📖 **Model validation chain 보충:** NCA observed AUC/$C_{max}$는 PopPK 모델 적합성의 **외부 reference**임. **VPC**의 관측 분포가 예측 분위수 안에 들어오는지, **CWRES**가 시간/예측에 대해 무작위 분포하는지, **NPDE** 분포가 N(0,1)을 따르는지 — 모든 진단에서 "관측 노출"의 reference가 NCA에서 옴. NCA 외삽 분율과 BLQ 처리 기록이 부실하면 PopPK 모델의 misspecification 판정이 왜곡됨. TDM 영역의 **Bayesian MAP estimation**도 prior로 들어가는 population parameter 신뢰도가 NCA-anchored 초기값에서 시작함.

📖 **NCA BLQ ↔ PopPK Beal M3 정렬 보충:** Beal (2001) **M3**는 BLQ를 censored likelihood로 처리, **M5**는 LOQ/2 substitution, **M6**는 첫 BLQ만 LOQ/2 후 결측, **M7**은 BLQ를 0 처리 — 모두 M3의 단순화 변종. **NCA에서 결측 처리한 BLQ도 PopPK 단계에서 M3로 들어와야 추정 정밀도 회복**. 두 영역 BLQ 규칙이 정렬 안 되면 BLQ 가까운 농도 구간의 IIV·RUV 분리 실패 — terminal phase의 $\omega^2$가 RUV로 흡수되거나 그 반대. NCA 보고서의 BLQ 처리 기록은 PopPK 모델 specification의 기초 자료임.

### 9.4 최종 압축 — 한 문단으로

NCA의 본질은 "모델을 쓰지 않는다"가 아니라 **"최소한의 선형 소실 가정으로 면적과 시간 모멘트를 요약한다"**임. AUC는 노출의 출발점, AUMC는 체류시간의 출발점, MRT는 V_ss의 출발점. PK41은 이 모든 것이 비선형 동력학 앞에서 **초기 추정값으로 격하되는 순간**을 보여줌. 그래서 30년 pharmacometrics 연구자가 10분 핸드아웃에 남길 메시지는 한 줄임 — **NCA 출력 표를 믿기 전에 (말단 기울기 → 외삽 분율 → BLQ 처리 → 투여 경로 보정 → 용량 의존성 → 노출 지표 선택)을 순서대로 점검**. 완성된 NCA 보고서는 **숫자 표가 아니라 가정 점검 기록**이어야 함.

> 💼 **현장 감각 마무리** — NCA 보고서의 1차 파라미터 자리에는 $AUC$가 아니라 **$CL$ 또는 $CL/F$**를 두고, $AUC$는 노출 지표로 보고하는 편이 **생리학적 해석성과 공변량 회귀 가능성을 동시에 보존**함. 보고 순서가 바뀌면 이후 PopPK에서 신·간 기능 공변량 신호가 약하게 나타날 수 있음. 작은 차이 같지만 6개월 뒤 모델링 단계에서 결과가 갈림.

---

## 부록: 출처 anchor 정리

- **Gabrielsson & Weiner 5e**
  - Ch.2 §2.8 NCA: pp.141–157 (정의·수식·MIT·§2.8.8 대안식)
  - Ch.2 §2.9 노출 지표: pp.158–164
  - Ch.41 PK41 (Turbojoint®): pp.661–664
  - §2.8.5 BLQ 처리: p.153
  - §2.8.6 정상상태 AUC equivalence: p.152
  - §2.8.8 washout 대안식: p.157, Eq.2:366/2:367
- **Rowland & Tozer 5e**
  - Appendix A (사다리꼴 예시, Table A-1·A-2): pp.759–762
  - Appendix H (MRT 분자 정의·Table H-1): pp.789–793
  - Ch.6 §BE (90% CI, TOST): pp.182–195, Fig.6-13, Table 6-7
  - Ch.11 §Fluctuation (PTF, $R_{ac}$): pp.276, 325, 340, Fig.11-14, Eq.11-10
  - Ch.19 §Distribution Kinetics (gentamicin, $V_1$ 기반 LD): pp.626, 632–636

---

*"표를 한 줄씩 읽으면 초보, 가정 순서로 읽으면 실무자, 모델 전환 신호로 읽으면 연구자."*

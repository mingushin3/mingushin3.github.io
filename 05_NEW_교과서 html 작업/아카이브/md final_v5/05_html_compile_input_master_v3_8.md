# 세션 05 · 2구획 모델 — 이중지수 분해 / α·β 재파라미터화 / $V_1$·$V_{ss}$·$V_\beta$ 체계 — v3.8

> **Source:** Gabrielsson & Weiner 5e Ch.2 §2.4.1–2.4.6 + Case Studies PK7/PK8 [G&W pp.57–77, 505–517] + Rowland & Tozer 5e Ch.19 [R&T pp.613–656]  
> **출처 노트:** 본 장은 2구획 약동학의 핵심 언어인 α/β phase, 중심·말초구획, $V_1$/$V_{ss}$/$V_\beta$, micro-rate constant, reparameterization을 학습자 관점에서 연결합니다.

<!-- SLIDE_START: §1 | title: 세션 헤더와 로드맵 -->

## §1 — 세션 헤더와 로드맵

**임상 장면 두 가지** — 이 세션이 왜 필요한지 보여주는 사례입니다.

- **Aspirin**(저용량 항혈소판제, 고용량 NSAID) **650 mg IV bolus**: early sampling을 놓치면 1구획 해석으로 $CL = 0.98$ L/min이 나오지만, 이중지수 해석에서는 $CL = 683$ mL/min입니다. 차이는 **44%** — 유지 용량(maintenance dose)이 그만큼 과대 산정됩니다. [R&T pp.615–620]
- **Gentamicin**(아미노글리코사이드 항생제; 좁은 치료범위, 신독성·이독성)**-like 약물**: $V_\beta = 345$ L, $V_{ss} = 56$ L. 어느 volume을 loading dose에 쓰느냐로 **첫 용량이 약 6배 흔들립니다.** [R&T pp.630, 635–641]

**핵심 아이디어:** 2구획 모델은 "곡선이 두 번 꺾인다"는 관찰을 $A,\alpha,B,\beta$라는 macro-constant(곡선의 절편·기울기)로 분해한 뒤, 이를 $CL,Q,V_1,V_2$ 같은 해석 가능한 좌표계로 다시 옮기는 작업입니다. **좌표계 선택은 표기 문제가 아닙니다** — clearance 추정, volume의 임상 해석, covariance 안정성, multiple-dosing 결과가 모두 이 선택에 따라 달라집니다. [G&W pp.59–71; R&T pp.615–641]

**3-Layer 개념 지도:**

```text
Layer 1 (정의/용어):  plasma curve ─ α/β phase ─ central/peripheral ─ A,α,B,β / V1,Vss,Vβ
Layer 2 (수식):       C(t)=Ae^{-αt}+Be^{-βt} ─ AUC=A/α+B/β ─ CL=k10·V1 ─ Vss=MRT·CL
Layer 3 (의사결정):   sampling 적정성 → parameterization → volume 선택 → dosing → 규제 방어
```

🧭 **읽는 순서**

- 카드 1 (M1): 왜 하나의 plasma curve가 두 지수항으로 분해되는가?
- 카드 2 (M2): 같은 curve를 macro, micro, physiological 좌표계로 바꾸면 무엇이 달라지는가?
- 카드 3 (M3): $V_1$, $V_{ss}$, $V_\beta$ 중 어떤 volume을 어떤 임상 질문에 써야 하는가?
- 카드 4 (M4): 같은 fit인데 왜 어떤 parameterization은 covariance가 무너지는가?
- 카드 5 (M5): terminal half-life 하나로 plateau와 multiple dosing을 말하면 왜 위험한가?

**지식 그래프 위치:**

```text
[선행: 1구획 IV bolus, AUC=Dose/CL, MRT/AUMC]
   → [이 세션: 2구획 phase 분해 · 좌표계 · volume 선택]
   → [후속: NONMEM ADVAN3/4/11/12, sparse design, 3구획, tissue/target-site PK]
```

**카드 간 연결:** M1(이중지수+잔차법) → M2(좌표계 3중 변환) → M3($V_1/V_{ss}/V_\beta$) → M4(재파라미터화+condition number) → M5(분포속도론+terminal half-life 함정).

**실무 흐름 기준점(Workflow Anchor):** PopPK 공변량 모델의 forward inclusion 단계에서 다섯 카드가 동시에 작동합니다.

| 결정 사항 | 어떤 카드가 답하는가 |
|---|---|
| 신기능 변화가 어느 phase를 흔드는가? | $f_2$ (M1/M5) |
| Covariate를 $CL$에 붙일지 $\beta$에 붙일지 | 좌표계 (M2) |
| 체중·조직 amount 해석 | $V_{ss}$/$V_\beta$ 구분 (M3) |
| 그 covariate model을 유지할 수 있는가? | condition number / RSE (M4) |

[실무 통합]

**선행 지식:** 1구획 IV bolus, $AUC=Dose/CL$, $V_d=CL/k$, MRT/AUMC, linear ODE.  
**후속 지식:** NONMEM ADVAN3/4/11/12, sparse sampling, $\eta$-shrinkage(ETA 정보 부족 지표) 해석, 3구획, tissue/target-site PK.

> 📍 **이 세션의 한 줄 회수**  
> 2구획 모델의 본질은 "두 지수항 외우기"가 아닙니다. **곡선 분해 → 좌표계 변환 → volume 선택 → dosing 해석**, 이 네 단계를 한 흐름으로 연결하는 것입니다.

---

<!-- SLIDE_START: §2 | title: 개념 해부 카드 -->

## §2 — 개념 해부 카드(Concept Anatomy Cards)

<!-- SLIDE_START: M1 | title: 이중지수 방정식과 잔차법 -->

### 카드 M1 — 이중지수 방정식과 잔차법(Method of Residuals)

> **거장의 시각**  
> 두 지수항을 "두 제거 경로"로 읽는 순간, phase slope가 ODE eigen-component라는 핵심을 놓칩니다. $f_1/f_2$와 AUC/AUMC 기여를 함께 보면 terminal phase를 elimination으로 해석해도 되는지 그 자리에서 판정할 수 있습니다.

**핵심 아이디어:** IV bolus 후 plasma curve가 반로그 도표(semilog plot; 농도축만 로그인 그래프)에서 하나의 직선이 아니라 **두 직선의 합**으로 보이면 다음처럼 씁니다. $A,B$는 zero-time intercept($t=0$ 외삽 절편), $\alpha,\beta$는 phase slope의 절댓값입니다. [G&W pp.59–60; R&T pp.615–617]

$$
\underbrace{C(t)}_{\text{혈장농도}}
=
\overbrace{\underbrace{A}_{\text{α절편}}e^{-\underbrace{\alpha}_{\text{빠른 slope}}t}}^{\text{α상 기여}}
+
\overbrace{\underbrace{B}_{\text{β절편}}e^{-\underbrace{\beta}_{\text{느린 slope}}t}}^{\text{β상 기여}},
\qquad \alpha>\beta>0
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $C(t)$ | 농도 | 시간 $t$의 혈장농도 | 투여량, 분포, 제거의 합성 |
| $A$ | 농도 | 빠른 α phase의 $t=0$ 외삽 절편 | 초기 분포상 크기, early sampling 민감 |
| $B$ | 농도 | 느린 β phase의 $t=0$ 외삽 절편 | 말단상 크기, terminal sampling 민감 |
| $\alpha$ | time$^{-1}$ | 빠른 phase slope | 분포속도, 일부 제거 영향 |
| $\beta$ | time$^{-1}$ | 느린 phase slope | 제거와 재분포가 결합 |

> 💡 **핵심 구분**: 두 지수항은 두 사람이 따로 문을 나가는 그림이 아니라, **한 방의 물이 빠지면서 옆방과 계속 섞이는 모습을 두 그림자로 나눈 것**입니다. 그래서 $\alpha,\beta$는 제거경로명이 아니라 관측 곡선을 만드는 phase slope입니다.

**잔차법(Method of Residuals) 절차:** terminal β phase를 log-linear 회귀로 외삽하여 $Be^{-\beta t}$를 얻고, 초기 관측치에서 이를 빼서 residual $C_{resid}(t)=C_{obs}(t)-Be^{-\beta t}$를 만듭니다. 이 residual이 반로그 도표에서 직선이면 그 기울기가 $-\alpha$, 절편이 $A$입니다. [G&W p.60; R&T p.616]

| 단계 | 가정 | 수식 |
|---|---|---|
| 1 | 말단부가 log-linear | $C_\beta(t)=Be^{-\beta t}$ |
| 2 | 초기 관측치에서 말단 외삽값 제거 | $C_{resid}(t)=C_{obs}(t)-Be^{-\beta t}$ |
| 3 | residual을 semilog로 재배치 | slope $=-\alpha$, intercept $=A$ |

> ⚠️ 잔차법은 NONMEM 실용 알고리즘이 아닙니다. 손으로 curve-stripping을 해 보는 이유는 simultaneous nonlinear regression에 넣을 **초기 추정치(initial estimate)의 감각**을 기르기 위해서입니다. [실무 확장]

**G&W Fig.2.43 기준점:** $A\approx70$, $B=28$, $\alpha=\ln(70/10)/130=0.0150$ min$^{-1}$, $\beta=\ln(28/10)/450=0.00229$ min$^{-1}$. 원본 그림의 단위 표기가 혼재되어 있으므로 최종 시각화 단계에서는 `[단위 확인 필요]`를 유지합니다. [G&W p.60]

$$
\underbrace{\alpha}_{\text{빠른 slope}}
=\frac{\overbrace{\ln(70/10)}^{\text{농도비 로그}}}{\underbrace{130}_{\text{시간간격}}},
\qquad
\underbrace{\beta}_{\text{느린 slope}}
=\frac{\overbrace{\ln(28/10)}^{\text{농도비 로그}}}{\underbrace{450}_{\text{시간간격}}}
$$

**2차 파라미터(Secondary Parameters):** AUC는 두 phase가 남긴 "총 물자국"이고, AUMC는 늦게 남은 물자국에 더 큰 가중치를 주는 기록입니다.

$$
\begin{aligned}
\underbrace{AUC_0^\infty}_{\text{총노출}}
&=\overbrace{\frac{\underbrace{A}_{\text{α절편}}}{\underbrace{\alpha}_{\text{α감소}}}}^{\text{빠른 상 면적}}
+\overbrace{\frac{\underbrace{B}_{\text{β절편}}}{\underbrace{\beta}_{\text{β감소}}}}^{\text{느린 상 면적}},\\[2mm]
\underbrace{AUMC_0^\infty}_{\text{시간가중노출}}
&=\overbrace{\frac{A}{\alpha^2}}^{\text{빠른 시간가중}}
+\overbrace{\frac{B}{\beta^2}}^{\text{느린 시간가중}}
\end{aligned}
$$

$$
\underbrace{t_{1/2,\alpha}}_{\text{빠른 반감기}}=\frac{\overbrace{\ln2}^{\text{반감상수}}}{\underbrace{\alpha}_{\text{빠른 slope}}},
\qquad
\underbrace{t_{1/2,\beta}}_{\text{느린 반감기}}=\frac{\overbrace{\ln2}^{\text{반감상수}}}{\underbrace{\beta}_{\text{느린 slope}}}
$$

$$
\underbrace{f_1}_{\text{α상 AUC분율}}=\frac{\overbrace{A/\alpha}^{\text{α상 AUC}}}{\underbrace{AUC}_{\text{총노출}}},
\qquad
\underbrace{f_2}_{\text{β상 AUC분율}}=\frac{\overbrace{B/\beta}^{\text{β상 AUC}}}{\underbrace{AUC}_{\text{총노출}}},
\qquad f_1+f_2=1
$$

$f_2$가 크면 terminal phase는 elimination 해석에 가깝습니다. **$f_2$가 작으면** terminal slope는 elimination보다 **재분포를 더 많이 반영**할 수 있습니다. [G&W p.63; R&T pp.622–623]

> 🔑 **Terminal 해석 규칙:** $f_2$를 보지 않고 terminal slope를 "elimination phase"라고 부르면 half-life와 dosing interval 해석이 함께 흔들립니다.

**구조적 필연(Structural Necessity):** 2구획 central/peripheral amount ODE는 다음과 같습니다.

$$
\underbrace{\frac{dA_1}{dt}}_{\text{중앙 변화율}}
=-\overbrace{\underbrace{(k_{12}+k_{10})}_{\text{말초+제거}}\underbrace{A_1}_{\text{중앙량}}}^{\text{중앙 유출}}
+\overbrace{\underbrace{k_{21}}_{\text{말초→중앙}}\underbrace{A_2}_{\text{말초량}}}^{\text{중앙 회귀}}
$$

$$
\underbrace{\frac{dA_2}{dt}}_{\text{말초 변화율}}
=\overbrace{\underbrace{k_{12}}_{\text{중앙→말초}}\underbrace{A_1}_{\text{중앙량}}}^{\text{말초 유입}}
-\overbrace{\underbrace{k_{21}}_{\text{말초→중앙}}\underbrace{A_2}_{\text{말초량}}}^{\text{중앙 회귀}}
$$

선형 상수계수 $2\times 2$ ODE의 해가 두 지수항의 합이기 때문에 $\alpha,\beta$는 이 system matrix에서 유래합니다. 따라서 다음 두 관계가 생깁니다 — **macro 4개는 서로 독립적인 숫자가 아니라 micro-parameter 공간의 수학적 제약을 받는 값들**입니다. [G&W pp.61–62; R&T pp.618–619]

$$
\underbrace{\alpha+\beta}_{\text{고유값 합}}
=\underbrace{k_{12}}_{\text{중앙→말초}}+
\underbrace{k_{21}}_{\text{말초→중앙}}+
\underbrace{k_{10}}_{\text{중앙 제거}},
\qquad
\underbrace{\alpha\beta}_{\text{고유값 곱}}
=\underbrace{k_{21}k_{10}}_{\text{회귀×제거}}
$$

💡 **비유:** $\alpha,\beta$는 엔진 부품 하나하나가 아니라, 여러 기어가 맞물린 뒤 바퀴에서 관찰되는 두 회전 속도입니다.

**그래프 3초 점검표:** ① 꺾임점(knee)이 어디인가($\alpha/\beta$의 비), ② 두 phase의 면적 비율이 어느 쪽으로 기우는가($f_1/f_2$), ③ terminal 직선이 정말 직선인가(3구획 가능성). [G&W p.63; R&T p.632]

**Aspirin 경고(Aspirin Warning):** R&T의 aspirin 650 mg IV bolus 예시는 early sampling을 놓치면 terminal-only 1구획 해석으로 $CL=0.98$ L/min을 얻지만, 이중지수 해석에서는 $CL=683$ mL/min임을 보여줍니다. **1구획 해석이 $CL$을 약 44% 과대추정**하므로 그대로 유지 용량을 계산하면 유지 용량도 과대 산정됩니다. → 이것이 "분포상을 놓치면 곡선이 같아 보여도 결론이 통째로 달라진다"는 사례입니다. [R&T pp.615–620]

| 상황 | 파라미터 변화 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| early sampling 누락 | $A,\alpha$ 정보 약화 | → | terminal-only $CL$ 과대추정 | 분포상 표본 확보 |
| terminal line만 사용 | $CL=0.98$ L/min로 계산 | → | 유지용량 과대 산정 위험 | biexponential 가능성 점검 |
| terminal 직선 휘어짐 | 2구획 부족 가능 | → | half-life 해석 불안정 | 3구획 또는 NCA 고려 |

**경계 조건(Boundary Conditions):** 선형 약동학, 중앙구획 내 빠른 혼합(mixing), 분포상 관측, mammillary 배열(중앙구획이 허브인 방사형 다구획 구조), 중앙구획 제거 가정이 필요합니다. 이 조건이 깨지면 bi-exponential fit은 가능해도 생리학적 해석이 흔들립니다. [G&W pp.57–65; R&T pp.617–619]

> 📖 **G&W p.60, Fig.2.43**: 정맥 일시주입(IV bolus) 후 이중지수 감소를 보여주는 반로그 도표. **관측 곡선이 하나의 말단선이 아니라 두 개의 외삽된 phase line의 합으로 보인다**는 잔차법의 핵심 시각 자료입니다.

> **M1 체화 핵심**  
> ① early sampling이 있는 IV bolus curve → $A,\alpha,B,\beta$와 $f_1/f_2$가 terminal 해석 가능성을 결정  
> ② terminal-only 1구획 해석 → $CL$ 과대추정과 maintenance dose 과대 산정 위험이 지배  
> ⚡ "두 지수항 = 두 제거경로"로 읽음 → central elimination 가정과 ODE 구조를 오독해 phase 해석 실패

---

<!-- SLIDE_START: M2 | title: Macro Micro Physiological 3중 좌표계 -->

### 카드 M2 — Macro ↔ Micro ↔ Physiological 3중 좌표계 변환

> **앞 카드에서 이 카드로**  
> M1이 curve를 $A,\alpha,B,\beta$ 네 숫자로 분해했다면, M2는 그 네 숫자를 임상적으로 보고할 수 있는 $CL,Q,V_1,V_2$ 언어로 옮깁니다.

> **거장의 시각**  
> 좌표계를 섞으면 자유도·가정·임상 해석이 한 문장 안에서 뒤엉킵니다. **fit은 macro로 이해하고, ODE는 micro로 점검하며, 보고와 covariate 해석은 physiological parameter로 마무리**하면 reviewer 질문이 깨끗하게 정리됩니다.

**핵심 아이디어:** 같은 2구획 curve가 세 가지 좌표계로 표현됩니다 — Macro는 곡선의 언어, Micro는 ODE 전이의 언어, Physiological은 clearance와 volume의 언어입니다. 실무에서는 대개 physiological 좌표계를 쓰지만, **왜 같은 곡선을 그 좌표계로 설명할 수 있는지는 macro/micro 변환을 이해할 때만 보입니다.** [G&W pp.60–71; R&T pp.618–619]

| 좌표계 | 파라미터 집합 | 역할 |
|---|---|---|
| Macro | $A,\alpha,B,\beta$ | 관측 plasma 곡선의 두 지수항 표현 |
| Micro | $V_1,k_{10},k_{12},k_{21}$ | 구획 ODE의 분율 속도 상수(fractional rate constant) |
| Physiological | $V_1,CL,Cld,V_t$ | 청소율, 분포 청소율, 중앙/말초 용적의 언어 |

좌표계라는 말은 같은 곡선을 서로 다른 질문에 맞춰 다시 쓰는 방식이라는 뜻입니다. **곡선을 잘 기술하는 좌표와 임상적으로 해석하기 좋은 좌표가 반드시 같지는 않습니다.**

**핵심 변환식(Core Conversions):**

$$
\underbrace{CL}_{\text{전신 CL}}=
\underbrace{k_{10}}_{\text{중앙 제거율}}
\underbrace{V_1}_{\text{중앙 V}}
$$

$$
\underbrace{Cld}_{\text{분포 CL}}=
\underbrace{k_{12}}_{\text{중앙→말초}}
\underbrace{V_1}_{\text{중앙 V}}
=
\underbrace{k_{21}}_{\text{말초→중앙}}
\underbrace{V_t}_{\text{말초 V}}
$$

$$
\underbrace{V_1}_{\text{중앙 V}}=
\frac{\underbrace{D_{iv}}_{\text{IV 용량}}}{\underbrace{A+B}_{\text{초기 }C_0}}
$$

$$
\underbrace{k_{21}}_{\text{말초→중앙}}
=
\frac{\overbrace{\underbrace{A}_{\text{α절편}}\underbrace{\beta}_{\text{느린 slope}}+\underbrace{B}_{\text{β절편}}\underbrace{\alpha}_{\text{빠른 slope}}}^{\text{절편가중 slope}}}{\underbrace{A+B}_{C_0}}
$$

$$
\underbrace{k_{10}}_{\text{중앙 제거율}}
=\frac{\overbrace{\alpha\beta}^{\text{고유값 곱}}}{\underbrace{k_{21}}_{\text{말초→중앙}}},
\qquad
\underbrace{k_{12}}_{\text{중앙→말초}}
=\overbrace{\alpha+\beta}^{\text{slope 합}}
-\underbrace{k_{21}}_{\text{말초→중앙}}
-\underbrace{k_{10}}_{\text{중앙 제거}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $CL$ | volume/time | 체내에서 완전히 제거되는 순 배출 능력 | 간·신장 제거능, 단백결합, 질병 상태 |
| $Cld$ 또는 $Q$ | volume/time | 중앙↔말초 사이 왕복 분포 흐름 | 관류, 조직 투과성, 분배 특성 |
| $V_1$ | volume | bolus 직후 중앙 희석 공간 | 혈장량, 빠른 평형 조직 |
| $V_t$ | volume | 말초구획 겉보기 공간 | 조직 결합, 지방/수분 분포 |
| $k_{10},k_{12},k_{21}$ | time$^{-1}$ | amount 기준 분율 전이 속도 | 각 clearance를 해당 volume으로 나눈 값 |

> 💡 **좌표계 비유:** Macro는 사진의 픽셀 좌표, Micro는 카메라 내부 렌즈 배치, Physiological은 의사가 읽는 판독문입니다. 같은 사진이라도 어떤 좌표로 말하느냐에 따라 책임지는 질문이 달라집니다.

**왜 자유도가 4개인가:** M1에서 본 두 지수항은 곡선을 설명하는 4개 자유도입니다. 출처가 지원하는 4-파라미터 집합은 micro $(V_1,k_{10},k_{12},k_{21})$ 또는 physiological $(V_1,CL,Cld,V_t)$입니다. **혼합 표현 $(V_1,V_t,k_{10},k_{12})$를 독립 자유도처럼 쓰면 안 됩니다.** [G&W pp.60–62, 71]

**비식별성(Non-identifiability)의 핵심:** plasma 이중지수 곡선만으로는 중앙구획 단독 제거, 말초구획 단독 제거, 양 구획 제거를 **구별할 수 없습니다.** 통상 중앙구획 단독 제거 모델을 쓰는 이유는 생리적으로 그럴듯하기 때문입니다 — plasma data가 그것을 증명한 것이 아닙니다. [G&W p.65; R&T pp.618–619]

> ⚠️ plasma curve가 같다고 elimination site까지 식별되는 것은 아닙니다. **제거 위치는 자료가 증명한 사실이 아니라 모델 가정으로 보충되는 부분**입니다.

**보고 시 주의(Reporting Caveat):** 보고서에서는 "중앙구획에서만 제거"와 "말초구획 단순 통합" 가정을 명시해야 합니다. 조직 PK, 거대 단백 약물, 표적 매개 제거(target-mediated)가 의심되는 경우는 이 가정에 대한 기전적 근거를 함께 제시해야 합니다. [R&T pp.618–619; 실무 추론]

> 💼 **NONMEM 연결**: ADVAN3/TRANS4의 표준 표현은 $CL,V_1,Q,V_2$이며, $K=CL/V_1$, $K_{12}=Q/V_1$, $K_{21}=Q/V_2$로 ODE 전이를 만듭니다.

**분배 주의사항(Partition Caveat):** 생리학적 ODE에서 중앙/말초 농도가 정상상태에서 같아진다는 표현은 **분배(partitioning)가 없다는 가정** 위에 있습니다. 실제 조직 농도가 plasma와 다르면 서로 다른 분포 청소율 또는 분배 계수가 필요한데, 두 구획 모두의 data 없이는 두 파라미터를 따로 추정할 수 없습니다. [G&W p.70]

> 📖 **G&W p.65, Fig.2.46**: 동일한 plasma 이중지수 곡선에 적합되는 **세 가지 2구획 모델**(중앙 제거, 말초 제거, 양 구획 제거). 같은 plasma curve가 elimination site를 식별해 준다는 잘못된 추론을 막아 줍니다.

> **M2 체화 핵심**  
> ① covariate를 어디에 붙일지 결정할 때 → $CL,Q,V_1,V_2$ physiological 좌표계가 결정  
> ② plasma curve로 제거 위치를 말하고 싶을 때 → structural non-identifiability가 지배  
> ⚡ macro=micro=physiological을 같은 언어로 취급 → 가정과 식별성을 혼동해 보고서 방어 실패

---

<!-- SLIDE_START: M3 | title: V1 Vss Vbeta 3중 분포용적 체계 -->

### 카드 M3 — $V_1$ / $V_{ss}$ / $V_\beta$ 3중 분포용적 체계 [⚡ Apex Concept]

> **앞 카드에서 이 카드로**  
> M2가 좌표계 셋을 분리했다면, M3는 그중 **가장 자주 임상 판단을 망가뜨리는 volume 좌표**의 혼동을 끊습니다.

> **거장의 시각**  
> 💢 **흔한 오해:** terminal half-life가 길면 그 약은 단순히 넓게 분포한다고 생각하기 쉽습니다.  
> ✅ **실제:** $V_\beta$는 terminal slope geometry와 $CL$이 만든 apparent volume이며, **$V_{ss}$나 $V_1$과 같은 임상 질문에 답하지 않습니다.**  
> 🎯 **체화할 단 하나의 직관:** volume을 묻는 순간 먼저 "**bolus 직후인가, steady state인가, terminal extrapolation인가**"를 물어야 합니다.

**핵심 아이디어:** 2구획에서 "volume of distribution"은 **하나가 아닙니다.** $V_1$은 bolus 직후 중앙 희석(central dilution), $V_{ss}$는 distribution equilibrium에서 $amount/C$, $V_\beta$는 terminal slope와 $CL$로 계산되는 apparent terminal volume입니다. 이 셋을 섞으면 amount in body, loading dose, tissue accumulation 해석이 모두 흔들립니다. [R&T pp.617, 628–630; G&W pp.63–65]

| 용적(Volume) | 공식 | 의미 | 주의 |
|---|---|---|---|
| $V_1$ | $V_1=Dose/(A+B)$ | 초기 희석/중앙구획 용적 | bolus 직후 중앙구획 + 매우 빠르게 평형에 도달하는 조직 |
| $V_{ss}$ | $V_{ss}=MRT\cdot CL=Dose\cdot AUMC/AUC^2$ | 정상상태 체내량 대비 plasma 비율 | 표준 중앙 제거 가정에서 $V_{ss}=V_1(1+k_{12}/k_{21})$ |
| $V_\beta$ | $V_\beta=CL/\beta=Dose/(AUC\cdot\beta)$ | 말단 기울기 기반 겉보기 용적 | 말단 기울기가 재분포에 지배되면 크게 부풀 수 있음 |

$$
\underbrace{V_1}_{\text{초기희석}}
=\frac{\underbrace{Dose}_{\text{용량}}}{\underbrace{A+B}_{C_0}},
\qquad
\underbrace{V_{ss}}_{\text{SS 체내량/C}}
=\underbrace{MRT}_{\text{평균체류시간}}\cdot\underbrace{CL}_{\text{정화능}}
=\frac{\underbrace{Dose}_{\text{용량}}\underbrace{AUMC}_{\text{시간가중노출}}}{\underbrace{AUC^2}_{\text{노출제곱}}},
\qquad
\underbrace{V_\beta}_{\text{말단 V}}
=\frac{\underbrace{CL}_{\text{정화능}}}{\underbrace{\beta}_{\text{β slope}}}
=\frac{\underbrace{Dose}_{\text{용량}}}{\underbrace{AUC}_{\text{노출}}\underbrace{\beta}_{\text{β slope}}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $V_1$ | L | 초기 central dilution | 혈장량, 빠른 평형 조직, bolus 직후 sampling |
| $V_{ss}$ | L | 정상상태 체내량/plasma concentration | 조직 분배, $MRT$, $CL$ |
| $V_\beta$ | L | terminal slope에서 역산한 겉보기 공간 | $CL$, $\beta$, 느린 재분포 |
| $MRT$ | time | 평균 체류시간 | AUMC/AUC, 분포·제거 시간 구조 |
| $AUMC$ | concentration·time$^2$ | 시간가중 노출 | 늦게 남는 농도 기여 |

> 💡 **세 volume의 비유:** $V_1$은 문을 열자마자 물이 찬 **첫 방**, $V_{ss}$는 모든 방의 수위가 안정된 뒤의 **집 전체**, $V_\beta$는 마지막 배수 그림자를 보고 거꾸로 추정한 **집 크기**입니다. "volume이 얼마입니까?"라는 질문 자체가 불완전합니다 — bolus 직후인지, steady state인지, terminal extrapolation인지부터 물어야 합니다.

**순서 관계(Ordering):** 표준 중앙구획 제거 2구획 가정에서는 $V_1\le V_{ss}\le V_\beta$로 생각할 수 있습니다. 단 이 부등식은 보편 법칙이 아니라 모델 가정 안에서의 실무 규칙입니다. [R&T pp.629–630]

$$
\underbrace{V_1}_{\text{초기희석}}\le
\underbrace{V_{ss}}_{\text{분포평형}}\le
\underbrace{V_\beta}_{\text{말단 V}}
$$

> 🔑 **Volume 선택 규칙:** loading dose와 steady-state amount에는 $V_{ss}$, bolus 직후 peak에는 $V_1$, terminal extrapolation에는 $V_\beta$를 연결합니다.

**Aspirin 기준점:** $V_1=6.5$ L, $V_{ss}=10.4$ L, $V_\beta=13.7$ L. 세 값에 차이는 있지만 치명적으로 벌어지지는 않습니다. [R&T pp.617, 629–630]

**Gentamicin 기준점:** $V_1=14$ L, $V_{ss}=56$ L, **$V_\beta=345$ L** — $V_\beta$가 $V_{ss}$보다 약 **6배** 큽니다. terminal half-life 87 hr는 plasma elimination half-life처럼 행동하지 않으며, **초기 phase half-life 약 4 hr**가 therapeutic plasma concentration 조절에 더 중요해집니다. → 그래서 같은 약물이라도 어느 volume을 쓰느냐로 첫 용량 판단이 6배 흔들린다는 사례입니다. [R&T pp.630, 635–641]

| 상황 | 파라미터 변화 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| Aspirin-like | $V_\beta/V_{ss}\approx 1.3$ | → | terminal volume 오용 위험 제한적 | 그래도 volume 정의 명시 |
| Gentamicin-like | $V_\beta/V_{ss}\approx 6.2$ | → | loading dose 과대 산정·peak 독성 위험 | $V_{ss}$ 중심으로 판단 |
| 느린 재분포 | $\beta$ 감소, $V_\beta$ 증가 | → | terminal half-life가 plasma 조절 시간과 분리 | 초기 phase와 $f_2$ 확인 |

**Thiopental 직관(Intuition):** R&T의 **thiopental**(지용성 barbiturate; 정맥 마취유도제) dog example에서는 지방으로의 분배(fat partitioning)가 크고 adipose tissue가 total apparent $V_d$의 큰 몫을 차지합니다. → 따라서 친유성·관류·분배 정보는 새 약물의 $V_{ss}/V_1$과 $V_\beta$ 부풀림을 **사전에 의심하게 해 주는 단서**입니다. [R&T pp.614–615]

**그럴듯한 오류(Plausible Fallacy):**

- **오류:** terminal half-life가 길면 2구획 모델에서 분포가 넓다고 판단한다.
- **왜 그럴싸한가:** $t_{1/2,\beta}=0.693/\beta$이고 $V_\beta=CL/\beta$이므로, 작은 $\beta$가 큰 volume처럼 보입니다.
- **나비효과:** terminal half-life를 "넓은 분포"로 직역 → $V_\beta$를 body amount/loading dose용 volume으로 사용 → **gentamicin-like 약물에서 첫 dose가 약 6배 과대 산정**되어 nephrotoxicity/ototoxicity 임계 농도를 첫 60분 내 초과할 위험 → 규제 측에서는 dosing rationale의 volume 정의 불일치로 **FDA Deficiency Letter** 또는 재분석 요구. [R&T pp.628–630, 638–639]

$$
\underbrace{t_{1/2,\beta}}_{\text{말단 반감기}}
=\frac{\overbrace{0.693}^{\ln2}}{\underbrace{\beta}_{\text{β slope}}},
\qquad
\underbrace{V_\beta}_{\text{말단 V}}
=\frac{\underbrace{CL}_{\text{정화능}}}{\underbrace{\beta}_{\text{β slope}}}
$$

💡 **느린 재분포의 정체:** 느린 재분포는 멀리 있는 창고에서 물건이 늦게 돌아오는 현상입니다. **창고가 거대해서가 아니라 왕복 도로가 좁아서** 마지막 움직임이 길게 보일 수 있습니다.

**임상 사용 규칙:** loading dose나 amount-at-steady-state 추정에는 **$V_{ss}$가 더 적절**하고, terminal phase extrapolation에는 $V_\beta$가 쓰입니다. 다회투여 interval 내에서는 fluctuation이 작고 true steady state에 가까울 때 $V_{ss}$가 쓸 만하며, interval 말기 distribution equilibrium에 가까워진 뒤에는 $V_\beta$가 approximate amount estimate에 쓰일 수 있습니다. **Gentamicin-like case처럼 interval 내 distribution disequilibrium이 크면 둘 다 단순 적용하기 어렵습니다.** [R&T pp.638–639]

> 📖 **R&T p.628, Fig.19-9**: 분포용적 용어와 제거가 $V$ 및 $V_{ss}$에 미치는 영향. **$V_1$, $V_{ss}$, $V_\beta$가 서로 바꾸어 쓸 수 없는 이유**를 가장 잘 보여주는 그림입니다.

> 📊 **다회투여 중 volume 선택**: 분포용적 항은 보편 계산기가 아닙니다. 사용 가능성은 투여 간격, fluctuation, distribution equilibrium에 따라 달라집니다.

> **M3 체화 핵심**  
> ① loading dose 또는 steady-state amount 계산 → $V_{ss}$가 지배  
> ② bolus 직후 peak 또는 terminal extrapolation → 각각 $V_1$과 $V_\beta$가 지배  
> ③ gentamicin-like ($V_\beta/V_{ss}$ 큰 약물) → 느린 재분포와 plasma dosing을 분리  
> ⚡ "terminal half-life가 길다 = 분포가 넓다" → $V_\beta$ 오용 → 독성 peak·규제 재분석 위험

---

<!-- SLIDE_START: M4 | title: 재파라미터화 5종과 condition number -->

### 카드 M4 — 재파라미터화 5종과 condition number

> **앞 카드에서 이 카드로**  
> M3가 어떤 volume을 쓸지 결정했다면, M4는 같은 curve를 어떤 parameterization으로 적합해야 **추정 geometry가 무너지지 않는지** 점검합니다.

> **거장의 시각**  
> 가장 낮은 WRSS를 고르는 습관은 fit residual만 보고 covariance geometry를 못 보는 실수입니다. **condition number, RSE, 상관성까지 함께 보면** "맞아 보이는 모델"과 "제출 가능한 모델"이 분리됩니다.

**핵심 아이디어:** 같은 biexponential data를 5개 parameterization으로 fit하면, **WRSS**(weighted residual sum of squares; fit 잔차 크기 지표)는 비슷해도 **parameter precision과 condition number**(추정 불안정성의 수치 지표)는 크게 달라질 수 있습니다. 즉 model form이 같아도 **좌표계가 estimation geometry를 바꿉니다.** [G&W pp.513–517]

**PK8 기준점:** **Compound X**(G&W PK8의 가상 화합물) 100 µg IV bolus data에서 G&W는 5가지 parameterization을 비교합니다. Table 8.1의 condition number는 **ODE model 29.69, Macro model 125.2, Colburn 2243, Reparameterized model 2306, Takada 3186**. 따라서 PK8 범위는 **29.69–3,186**이고, 최대/최소 비율은 약 **107배**입니다. [G&W pp.513–517]

| 모델 계열 | 핵심 파라미터화 | 판단 |
|---|---|---|
| Macro | $A,\alpha,B,\beta$ | 곡선 기술에는 직관적이나 절편/기울기 상관 가능성 큼 |
| Takada | 시간 의존적 $V(t)$ | WRSS가 낮아도 condition number가 큼 |
| Colburn | $V(t)$의 지수적 접근 | 시간 의존적 용적 직관 제공 |
| 재파라미터화 CL 모델 | $D_{iv},CL$ 포함 | 청소율 언어로 연결 |
| ODE 생리학적 모델 | $CL,V_1,Cld,V_t$ | **PK8에서 최저 condition number** |

> 💡 **추정 기하 핵심 + 비유:** Reparameterization은 표기 치장이 아니라 estimation geometry를 바꾸는 preconditioning입니다. 같은 지도를 접는 방법만 바꿔도 주머니에 잘 들어가거나 찢어질 수 있는 것처럼, 추정 과정에서 접히는 방향이 달라집니다.

**핵심 교훈:** 가장 낮은 WRSS가 실용 모델(production model)의 충분조건은 아닙니다. **Takada model**은 WRSS가 낮아도 condition number가 높고, **ODE model**은 condition number가 가장 낮습니다. [G&W p.516]

| 상황 | 파라미터 변화 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| WRSS만 최저 | residual fit만 개선 | → | 불안정한 모델 채택 위험 | condition number/RSE 병행 |
| condition number 폭증 | 정보 행렬 불안정 | → | covariate 추가 시 결과 비재현 | 초기치·로그 파라미터화·좌표계 순서 점검 |
| ODE 좌표 안정 | $CL,V_1,Cld,V_t$ 해석 가능 | → | reviewer 방어 용이 | production 후보 우선 고려 |

> 💼 **실무 인사이트:** condition number가 폭증하면 좌표계부터 바꾸기 전에 **THETA 초기치를 먼저 확인**합니다. 초기치가 자릿수부터 틀리면 좌표계와 무관하게 정보 행렬이 나빠질 수 있습니다. **디버깅 순서: 초기 추정치 → 로그 영역 파라미터화 → 재파라미터화.** [실무 디버깅 순서]

**RSE 주의:** condition number는 파라미터 간 정보 직교성을 봅니다. **RSE**(relative standard error; 각 추정치의 상대표준오차, %)는 각 파라미터 자체의 추정 신뢰성을 봅니다. PK8 Table 8.1에는 RSE가 없으므로 **그 표만으로 실용 모델 결정을 끝내지 않습니다.** [실무 확장]

**PK7 모델 판별 연결:** G&W PK7은 mono/bi/tri-exponential 판별에서 AIC/F-test, 정밀도, 상관성, 잔차, 최소 적절 모델 규칙을 함께 보게 합니다. 특히 — **weighting scheme이 다른 두 모델을 단순 F-test로 비교해서는 안 됩니다.** 두 모델의 likelihood가 서로 다른 측정오차 가정 위에 서 있기 때문입니다. NDA 제출의 모델 정당화 논리는 이 단순 사실 위에 서 있습니다. [G&W pp.505–512]

> ⚠️ WRSS와 condition number는 서로를 대체하지 않습니다. 하나는 "얼마나 잘 맞았는가", 다른 하나는 "그 맞음이 안정적으로 추정되는가"를 봅니다.

**NCA 대안 판단:** G&W PK8은 initial phase가 거의 보이지 않지만 배제할 수 없을 때 NCA가 제안될 수 있음을 언급합니다. **"2구획 fit을 무조건 강행"하라는 세션이 아닙니다** — data가 phase를 식별할 때만 parametric 2구획 해석을 신뢰하라는 경고입니다. [G&W p.517]

> 📊 **PK8 모델 선택**: WRSS 축 vs condition-number 축 — 비슷한 적합 품질이 비슷한 추정 안정성을 의미하지는 않습니다.

> **M4 체화 핵심**  
> ① 비슷한 fit의 후보 모델이 여러 개일 때 → condition number/RSE/상관성이 결정  
> ② WRSS가 가장 낮지만 condition number가 큰 모델 → production model 보류 판단이 지배  
> ⚡ "lowest WRSS = best model" → covariance instability를 숨겨 NDA 모델 정당화 실패

---

<!-- SLIDE_START: M5 | title: 분포속도론과 terminal half-life의 함정 -->

### 카드 M5 — 분포속도론의 임상 파급과 terminal half-life의 함정

> **앞 카드에서 이 카드로**  
> M4가 제출 가능한 parameterization을 고르는 문제였다면, M5는 그 모델에서 나온 **terminal half-life를 dosing 시간 척도로 써도 되는지** 검증합니다.

> **거장의 시각**  
> half-life 숫자 하나를 듣자마자 dosing interval로 번역하면 terminal, effective, plasma, tissue가 한 단어 안에서 뒤섞입니다. **$f_1/f_2$, input pattern, volume term을 함께 보면** terminal half-life가 유용한 경우와 위험한 경우가 갈립니다.

**핵심 아이디어:** terminal half-life는 자주 유용합니다. 단, distribution kinetics가 강할 때는 "약물이 사라지는 속도"보다 **"slow tissue(서서히 평형에 도달하는 조직)에서 plasma로 돌아오는 속도"를 더 많이 반영**할 수 있습니다. 그래서 plateau 도달, tissue accumulation, renal impairment dosing은 $f_1/f_2$와 투여 방식까지 함께 봐야 합니다. [R&T pp.631–641]

**정상상태 접근 방정식(Plateau Equation):**

$$
\underbrace{\frac{C(t)}{C_{ss}}}_{\text{SS 접근률}}
=
\overbrace{\underbrace{f_1}_{\text{α상 기여}}(1-e^{-\underbrace{\alpha}_{\text{빠른 slope}}t})}^{\text{빠른 접근}}
+
\overbrace{\underbrace{f_2}_{\text{β상 기여}}(1-e^{-\underbrace{\beta}_{\text{느린 slope}}t})}^{\text{느린 접근}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $C(t)/C_{ss}$ | fraction | 정상상태 농도에 대한 접근률 | phase별 접근률과 $f_1/f_2$ |
| $f_1$ | fraction | 빠른 phase의 AUC 기여 | early distribution 비중 |
| $f_2$ | fraction | 느린 phase의 AUC 기여 | terminal contribution, 재분포/제거 |
| $\alpha$ | time$^{-1}$ | 빠른 접근 속도 | 분포속도, 일부 제거 |
| $\beta$ | time$^{-1}$ | 느린 접근 속도 | terminal slope, 느린 조직 회귀 |

> 💡 **plateau 접근 비유:** 두 개의 수도꼭지가 동시에 차오르는 욕조입니다. **빠른 수도꼭지의 물량이 대부분이면** 마지막 한 방울이 늦어도 욕조 수위는 이미 거의 올라와 있습니다.

이 식은 두 phase가 $C_{ss}$로 접근하는 정도를 $f_1/f_2$로 가중합합니다. **그래서 half-life 하나가 아니라 phase별 AUC 기여도가 plateau 해석을 결정합니다.** $f_2$가 크면 terminal half-life가 plateau 도달을 대체로 설명하지만, **$f_2$가 작으면 terminal half-life가 길어도 plasma plateau는 훨씬 빨리 접근**합니다. [R&T pp.631–633]

> 🔑 **Half-life 분류 규칙:** half-life를 들으면 계산 전에 "**terminal? effective? plasma? tissue?**"를 먼저 물어야 합니다.

**Nicardipine 기준점:** **Nicardipine**(디하이드로피리딘 calcium channel blocker; IV 혈압강하제)은 말단 반감기가 약 **12 hr**로 길지만, plasma 농도는 **1 hr 안에 약 50% $C_{ss}$**에 도달하고 약 15 hr에 90% $C_{ss}$에 도달합니다. → 말단 반감기만 보고 loading dose 필요성을 판단하면 **초기 과량 투여 위험**이 생기는 사례입니다. [R&T p.631]

**Gentamicin 기준점:** 말단 반감기가 **87 hr**이어도 plasma 치료적 거동은 **약 4 hr 초기상**에 의해 좌우됩니다. 말단항 기반 축적 지수(accumulation index)는 16배가 될 수 있지만, 이는 plasma 최고/최저 농도 축적과 동일하지 않고 **서서히 평형에 도달하는 조직의 축적**을 말합니다. [R&T pp.635–641]

| 상황 | 파라미터 변화 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| Nicardipine-style | terminal $t_{1/2}\approx 12$ hr, 1 hr에 50% $C_{ss}$ | → | loading dose 필요성 과대판단 위험 | plateau equation으로 effective time scale 확인 |
| Gentamicin-like | terminal $t_{1/2}=87$ hr, 초기상 약 4 hr | → | terminal accumulation과 plasma fluctuation 혼동 | plasma와 tissue accumulation 분리 |
| $f_2 > 0.8$ | terminal contribution 큼 | → | terminal half-life가 time-course 대표 가능 | 그래도 phase/조직 구분 명시 |

**조직 vs plasma 정상상태:** plasma가 정상상태에 빨리 접근해도 **서서히 평형에 도달하는 조직은 훨씬 늦게 접근**할 수 있습니다. 따라서 반응 부위(response site)가 말초/조직 쪽이면 plasma 반감기만으로 작용 개시(onset)와 지속(duration)을 해석하면 안 됩니다. [R&T pp.633–634]

**Multiple dosing volume rule:** fluctuation이 작고 true steady state에 가까울 때는 $V_{ss}$가 amount estimate에 유용합니다. interval 말기 distribution equilibrium에 가까우면 $V_\beta$도 approximation으로 쓰일 수 있습니다. **단, gentamicin-like 경우처럼 interval 전체가 distribution disequilibrium이면 어느 volume도 단순 amount calculator가 되지 않습니다.** [R&T pp.638–639]

**완화된 경고:** "terminal half-life는 항상 틀린다"는 뜻이 아닙니다. R&T는 **많은 약물에서 $f_2>0.8$이면 terminal phase가 plateau/time-course를 잘 설명한다**고 말합니다. 핵심은 "terminal인지 effective인지, plasma인지 tissue인지, $f_2$가 얼마인지"를 확인하는 것입니다. [R&T pp.631–641]

> 💼 **실무 인사이트:** 누군가 "이 약물의 half-life는 X시간"이라고 말하면 바로 물어야 합니다 — **"terminal? effective? plasma? tissue?"** 이 구분이 달라지면 multiple-dosing simulation 결과가 통째로 달라집니다. [실무 확장]

> 📖 **R&T p.631, Fig.19-10**: 긴 말단 반감기에도 불구하고 plateau에 접근하는 Nicardipine 사례. 반감기 하나만으로 투여를 판단하지 말라는 경고를 직접 뒷받침합니다.

> 📖 **R&T p.636, Fig.19-14**: Gentamicin의 plasma/tissue 다회투여 축적. **말단항 축적과 치료적 plasma 변동을 분리해서** 보여줍니다.

> **M5 체화 핵심**  
> ① plateau 도달과 multiple dosing 판단 → $f_1/f_2$-가중 plateau equation이 결정  
> ② terminal half-life가 길지만 plasma가 빨리 오르는 경우 → effective/plasma time scale이 지배  
> ⚡ half-life 하나로 dosing interval 결정 → tissue accumulation과 plasma fluctuation을 혼동해 dosing simulation 실패

---

<!-- SLIDE_START: §5 | title: 혼동 쌍 해부와 치명적 타격 -->

## §5 — 혼동 쌍 해부(Confusion Pairs) & 치명적 타격(Critical Blow)

### Pair 1 — Bi-exponential curve vs "two elimination processes"

| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | Bi-exponential phase: $A e^{-\alpha t}+B e^{-\beta t}$, 농도 | "two elimination processes": 독립 제거 경로처럼 오해 |
| 수식 내 위치 | $\alpha,\beta$는 지수부 slope | 제거경로라면 별도 clearance 항이어야 하나 본 수식에는 없음 |
| 변화 원인 | distribution과 elimination이 합성된 ODE eigen-component | 제거 장기 2개가 따로 작동한다는 과잉 해석 |
| 혼동 시 임상 결과 | $f_2$가 작으면 terminal phase를 elimination phase라 부르면 위험 | central elimination 가정과 sampling adequacy 판단 실패 [G&W p.63; R&T pp.622–623] |

**⚡ 기억 고리 — *이사 vs 청소*:**  
α phase는 약이 혈장에서 조직으로 **이사 가는** 분포 단계, β phase는 주로 **청소**(제거)가 지배하는 단계입니다. 단 두 단계가 완전히 분리된 것이 아니라 **항상 동시에** 일어납니다 — α 단계에도 제거가 있고, β 단계에도 분포 평형 조정이 있습니다. **"α = 분포, β = 제거"는 근사 레이블이지 기계적 분리가 아닙니다.** 이 레이블을 두 개의 elimination pathway로 곡해하는 순간 central elimination 가정이 무너집니다.

### Pair 2 — $V_1$ vs $V_{ss}$ vs $V_\beta$ [Critical Blow]

| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | $V_1$/$V_{ss}$: bolus 직후 또는 steady-state amount용 volume | $V_\beta$: terminal slope 기반 apparent volume |
| 수식 내 위치 | $V_1=Dose/(A+B)$, $V_{ss}=MRT\cdot CL$ | $V_\beta=CL/\beta=Dose/(AUC\cdot\beta)$ |
| 변화 원인 | 중앙 희석, 분포 평형, 조직 분배 | 작은 $\beta$, 느린 재분포, terminal geometry |
| 혼동 시 임상 결과 | loading dose와 amount-at-steady-state에 연결 가능 | Gentamicin: $V_\beta=345$ L, $V_{ss}=56$ L, $V_1=14$ L. $V_\beta$를 "진짜 body volume"처럼 쓰면 tissue redistribution과 plasma dosing을 혼동합니다. [R&T pp.630, 635–641] |

**치명적 타격:** NDA/IND 제출 또는 critical care 상황의 loading dose 결정에서 $V_\beta$를 $V_{ss}$ 대신 사용하면 gentamicin-like 약물의 첫 dose가 **약 6배 과대 산정**됩니다. 결과적으로 (1) 심사관이 dosing rationale의 volume 정의 일관성 결여를 **Deficiency Letter** 사유로 지적하거나, (2) 환자에게 nephrotoxicity/ototoxicity 임계 농도를 **첫 60분 내 초과하는 plasma peak**이 발생할 위험이 있습니다.

$$
\underbrace{\frac{V_\beta}{V_{ss}}}_{\text{말단V 오용}}
\approx
\frac{\underbrace{345}_{\text{GM }V_\beta}}{\underbrace{56}_{\text{GM }V_{ss}}}
\approx 6.2
$$

**⚡ 기억 고리 — *현재 vs 균형 vs 제거 그림자*:**  
$V_1$은 투여 직후 약이 도달한 **즉각적 분포 공간**(혈장 + 빠른 조직), $V_{ss}$는 분포와 제거가 독립인 **평형 상태의 겉보기 부피**, $V_\beta$는 terminal slope에서 역산한 **제거 편향이 혼합된 겉보기 부피**입니다. $V_1 < V_{ss} \le V_\beta$는 2구획 시스템의 수학적 필연입니다. **Loading dose는 $V_{ss}$, AUC 정규화는 $CL$, terminal half-life는 $V_\beta/CL$에 의존합니다 — 세 부피를 혼용하면 세 계산이 모두 틀립니다.**

### Pair 3 — Macro vs Micro vs Physiological parameterization

| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | Macro: $A,\alpha,B,\beta$; 농도와 time$^{-1}$ | Physiological: $CL,Q,V_1,V_2$; volume/time과 volume |
| 수식 내 위치 | $A,B$는 지수항 계수, $\alpha,\beta$는 지수 slope | $CL,V_1,Q,V_2$는 ODE와 보고용 parameter |
| 변화 원인 | 관측 curve geometry와 sampling | 제거능, 분포 흐름, 중앙/말초 용적 |
| 혼동 시 임상 결과 | curve description만 남음 | covariate 보고와 dosing 해석 가능. 둘을 별개로 생각하면 condition number와 interpretability 판단 실패 [G&W pp.60–71; R&T pp.618–619] |

**⚡ 기억 고리 — *내부 고속도로 vs 나가는 출구*:**  
좌표계 전환에서 가장 자주 혼동되는 핵심 쌍은 **$Q$ vs $CL$**입니다. $Q$(intercompartmental clearance)는 중앙구획과 말초구획 사이를 오가는 **내부 순환량**(고속도로 통행량), $CL$(systemic clearance)은 체내에서 완전히 빠져나가는 **순 배출량**(출구)입니다. $Q$가 크면 두 구획이 빠르게 균형을 잡고(짧은 α phase), $CL$이 크면 전체 약물이 빠르게 제거됩니다. **$Q \gg CL$이면 2구획 성격이 약해져 1구획처럼 보일 수 있다** — 이것이 macro(α, β) ↔ physiological($Q$, $CL$) 좌표계 변환에서 비로소 보이는 시스템 진단 단서입니다.

### Pair 4 — Terminal half-life vs Effective/clinical half-life [치명적 구분]

| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | Terminal half-life: 시간 | Effective/clinical half-life: 임상 농도 접근 시간 척도 |
| 수식 내 위치 | $t_{1/2,\beta}=0.693/\beta$ | $C(t)/C_{ss}=f_1(1-e^{-\alpha t})+f_2(1-e^{-\beta t})$ |
| 변화 원인 | terminal slope, 느린 재분포 | $f_1/f_2$, input pattern, plasma/tissue site |
| 혼동 시 임상 결과 | 논문 half-life 12 hr를 plateau에도 적용 | Nicardipine-style case: terminal $t_{1/2}\approx 12$ hr이지만 50% $C_{ss}$는 약 1 hr. terminal half-life만 보고 loading dose를 권하면 초기 과량 투여 판단이 나옵니다. [R&T p.631] |

**⚡ 기억 고리 — *마지막 페이지 vs 전체 이야기*:**  
Terminal $t_{1/2}$은 log-concentration 곡선의 마지막 직선 구간에서만 읽히는 **마지막 페이지** — 이미 재분포가 완료되고 제거만 남은 단순화된 단계입니다. 그 앞에는 α phase의 빠른 분포와 초기 제거가 있었습니다. **Terminal $t_{1/2}$만으로 투여 간격이나 체내 잔류를 판단하면 앞 페이지의 높은 초기 농도와 분포 지연 효과를 놓칩니다.** Effective $t_{1/2}$은 $f_1/f_2$-가중 plateau equation으로 읽어야 보이는 "전체 이야기"의 시간 척도입니다.

### Pair 5 — Better WRSS vs better model

| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | WRSS: residual fit 품질 지표 | deployable model: fit + 안정성 + 해석 가능성 |
| 수식 내 위치 | 목적함수/잔차 축 | condition number, RSE, correlation, biological plausibility와 병렬 판단 |
| 변화 원인 | 측정오차 가정, weighting, residual 크기 | parameterization, 정보 행렬, covariance geometry |
| 혼동 시 임상 결과 | WRSS가 가장 낮은 parameterization을 무조건 채택 | G&W PK8에서 ODE model은 lowest condition number이고, Takada는 낮은 WRSS에도 high condition number입니다. [G&W pp.513–517] |

**혼동 회수(Confusion recap):** 이 세션의 치명적 혼동은 모두 **"curve geometry를 physiological truth로 바로 읽는 것"**에서 생깁니다. curve는 evidence이고, interpretation은 assumption과 좌표계를 거쳐서 얻어집니다.

---

<!-- SLIDE_START: §7 | title: 자기 테스트 -->

## §7 — 자기 테스트(Self-Test)

### Q1. 잔차법 재구성

G&W Fig.2.43에서 말단상을 외삽하여 $B=28$, $\beta=\ln(28/10)/450$를 얻었습니다. 초기 관측치에서 무엇을 빼야 α 상을 얻습니까?

**정답:** 각 초기 관측치 $C_{obs}(t_i)$에서 $Be^{-\beta t_i}$를 뺍니다. 잔차를 반로그 도표에 다시 놓고 기울기/절편을 구하면 α와 $A$가 나옵니다. [G&W p.60]

### Q2. Aspirin CL 방향 판단

Aspirin 650 mg IV bolus에서 말단상 전용 1구획 해석은 $CL=0.98$ L/min, 이중지수 해석은 $CL=683$ mL/min입니다. 말단상 전용 해석은 실제 $CL$을 과소평가합니까, 과대평가합니까?

**정답:** **과대평가합니다.** $0.98$ L/min은 683 mL/min보다 약 **44% 높습니다.** 따라서 유지 용량 계산이 과대평가될 위험이 있습니다. [R&T pp.615–620]

### Q3. 용적 비율 적용

Aspirin과 gentamicin 중 $V_\beta/V_{ss}$ 비율이 더 큰 약물은 무엇이며, 그것이 왜 중요합니까?

**정답:** **Gentamicin입니다.** Aspirin은 $13.7/10.4 \approx 1.3$이지만 gentamicin은 $345/56 \approx 6.2$입니다. 큰 비율은 **말단 기울기 유래 용적을 정상상태 체내량 용적처럼 쓰면 안 된다**는 경고입니다. [R&T pp.629–641]

$$
\underbrace{\left(\frac{V_\beta}{V_{ss}}\right)_{aspirin}}_{\text{ASA 말단부풀림}}
\approx\frac{13.7}{10.4}\approx 1.3,
\qquad
\underbrace{\left(\frac{V_\beta}{V_{ss}}\right)_{gentamicin}}_{\text{GM 말단부풀림}}
\approx\frac{345}{56}\approx 6.2
$$

### Q4. 구조적 비식별성

동일한 이중지수 plasma 곡선을 중앙구획 제거, 말초구획 제거, 양 구획 제거 모델이 모두 설명할 수 있습니다. plasma data만으로 무엇을 결론낼 수 없습니까?

**정답:** **제거 부위(elimination site)를 식별할 수 없습니다.** 중앙구획 단독 제거는 보통 생리학적 타당성 때문에 선택되는 실무 가정이며, 조직 data나 기전적 근거 없이 plasma 곡선만으로 증명되는 것이 아닙니다. [G&W p.65; R&T pp.618–619]

### Q5. 말단 반감기의 함정

Nicardipine처럼 말단 반감기가 12 hr인데 1 hr에 50% $C_{ss}$에 도달하는 사례에서 말단 반감기만으로 loading dose를 권하면 왜 위험합니까?

**정답:** plateau 접근이 terminal term만으로 결정되지 않고 **$f_1/f_2$ 가중합으로 결정**되기 때문입니다. plasma는 이미 빠르게 올라가는데 terminal half-life만 보면 "너무 늦게 도달한다"고 오판하여 **과도한 loading을 권할 수 있습니다.** [R&T pp.631–633]

$$
\underbrace{\text{plateau 접근}}_{C(t)/C_{ss}}
\neq
\underbrace{\text{말단반감기 단독}}_{\beta\text{만 보는 해석}},
\qquad
\underbrace{C(t)/C_{ss}}_{\text{접근률}}
=\underbrace{f_1}_{\text{α 기여}}(1-e^{-\alpha t})
+\underbrace{f_2}_{\text{β 기여}}(1-e^{-\beta t})
$$

### Q6. PK8 모델 선택

PK8에서 Takada 모델은 WRSS가 낮고 ODE 모델은 condition number가 낮습니다. 어느 하나만 보고 결정하면 안 되는 이유는?

**정답:** WRSS는 fit residual의 크기, condition number는 parameter estimation geometry를 봅니다. **둘 중 하나만 좋다고 deployable model이 되는 것은 아닙니다.** PK8의 핵심은 "동일 데이터/비슷한 fit에서도 좌표계가 condition number를 크게 바꾼다"는 것입니다. [G&W pp.513–517]

### Q7. 희소 설계 진단

첫 표본이 분포상 이후에만 존재하는 sparse design에서 ADVAN3 TRANS4 적합 후 $V_2$ RSE >100%, ETA(V2) shrinkage >80%, 초기 CWRES 양의 경향이 보입니다. 가장 먼저 의심할 것은?

**정답:** "약물의 $V_2$가 진짜 작다"가 아니라 **distribution phase가 data에 없어 $V_2$가 식별되지 않는 Phantom V2** 상황을 의심합니다. [실무 확장]

### Q8. 반감기 실무 규칙

회의에서 누군가 "half-life가 87 hr이므로 8시간 간격 투여하면 plasma가 16배 축적된다"고 말합니다. 무엇을 되물어야 합니까?

**정답:** **terminal half-life인지 effective/plasma half-life인지, $f_2$가 얼마인지, 그리고 축적이 plasma 구획인지 서서히 평형에 도달하는 조직인지** 물어야 합니다. Gentamicin-like case에서는 terminal term accumulation과 plasma therapeutic fluctuation을 구분해야 합니다. [R&T pp.635–641]

### Q9. 보스 딜레마 — PK8 모델 채택 결정 (★★ Socratic Dilemma)

당신은 NDA submission 마감 1주일 전입니다. PK8 데이터로 PopPK 모델 후보가 둘로 좁혀졌습니다.

- **Model A (Takada parameterization):** WRSS가 5개 parameterization 중 가장 낮음. 그러나 condition number 3,186, $V_t(t)$ time-dependent 표현이 reviewer가 익숙하지 않을 가능성이 큼.
- **Model B (ODE physiological parameterization):** condition number 29.69로 압도적으로 안정적. WRSS는 Takada보다 약간 높지만 fit 자체는 visually 충분히 양호. $CL,V_1,Cld,V_t$로 reviewer가 즉시 해석 가능.

어느 모델을 실용 모델(deployable model)로 채택하고, 그 결정을 reviewer에게 어떻게 방어합니까?

**정답 (Trade-off 논리):**

**채택: Model B (ODE 생리학적 모델).** 단, 정답은 모델 선택 자체보다 **방어 논리의 구조**에 있습니다.

1. **WRSS는 fit residual의 크기, condition number는 추정 geometry의 안정성**입니다. 두 축은 서로 대체할 수 없습니다. 단일 축으로 결정할 수 없는 상황은 NDA에서 흔합니다.
2. **실용 모델의 첫째 조건은 재현성** — 다른 시드, 다른 초기치, 다른 공변량 추가에서도 동일한 결론이 나오는가. condition number 3,186은 covariance step instability와 covariate inclusion 시 결과 비예측성을 의미합니다.
3. **Reviewer Defense 한 줄:** "Takada는 lowest WRSS이지만 (a) covariance geometry가 100배 이상 불안정하고 (b) 시간 의존적 용적 표현은 공변량-용적 관계 해석에 추가 해석 부담을 만듭니다. ODE 생리학적 모델은 적합이 거의 동등하면서 (a) 정밀도/상관성이 안정적이고 (b) 청소율/용적 좌표계로 일반적 PopPK 보고 관행에 부합합니다." [실무 추론: regulatory defense]
4. **적합 차이가 임상적으로 유의미한 수준 (예: AUC 차이 >10%)이면** 두 모델 모두를 민감도 분석(sensitivity analysis)으로 보고하고 최종 dosing 권고는 두 모델 간 robust 영역에서 도출합니다. PK8 자체는 그 정도 차이를 보이지 않습니다.
5. **함정:** "WRSS가 더 낮으니 Takada가 진짜 모델에 가깝다"는 추론은 **부적절한 weighting scheme 비교**일 수 있습니다 (Q6 + PK7 bridge). 무가중 RSS와 가중 RSS는 직접 비교 대상이 아닙니다. [G&W pp.508–517; R&T 일반 PopPK practice; 실무 추론]

**다음 깊이 질문:** Model B를 채택했는데 reviewer가 "그렇다면 Takada가 보여준 lower WRSS는 어떤 정보를 담고 있나"라고 묻는다면? — **"lower WRSS는 시간 의존적 $V$ 가정이 적합 잔차를 약간 감소시킨다는 신호이지, 그 가정이 기전적으로 검증되었다는 의미는 아닙니다. 기전적 검증 없이는 실용 모델로 채택할 수 없습니다"**가 표준 답변입니다. [실무 추론]

**자기 테스트 회수:** 9개 질문(8 회상·적용 + 1 Socratic Dilemma)을 모두 통과하면, 2구획 모델을 "공식"이 아니라 **모델 선택·volume 해석·dosing simulation·규제 방어 논리의 사고 도구**로 사용할 준비가 된 것입니다.

---

<!-- SLIDE_START: §8 | title: 지식 그래프 실패 모드 전문가 해석 지점 -->

## §8 — 지식 그래프(Knowledge Graph), 실패 모드(Failure Modes), 전문가 해석 지점(Professional Moat)

### A. 이번 세션 직후 연결되는 지식

| 후속 세션 | 이 세션에서 열리는 개념 | 이 세션 없으면 실패하는 것 |
|---|---|---|
| NONMEM ADVAN3/4/11/12 | $CL,V_1,Q,V_2$ 좌표계와 macro/micro 연결 | ADVAN parameter를 curve slope와 분리해 외움 |
| Sparse sampling design | distribution phase sample 없이는 $V_2$, $Q$, α 식별이 약해진다 | Phantom V2를 실제 작은 $V_2$로 오판 |
| Covariate model building | covariate는 보통 $CL,V,Q$ 같은 physiological parameter에 붙인다 | covariate를 β나 terminal half-life에 직접 붙여 해석 불능 |
| Multiple-dosing simulation | terminal half-life 하나가 아니라 $f_1/f_2$, input duration, $V_{ss}/V_\beta$를 같이 본다 | plateau와 tissue accumulation을 같은 시간 척도로 처리 |
| 3구획 모델 | 이중지수 잔차에서 다시 곡선이 휘면 삼중지수 또는 더 깊은 조직 구획을 의심 | 2구획으로 설명되지 않는 terminal curvature를 노이즈로 처리 |

### B. 실패 모드(Failure Modes)

| 실패 모드 | 진단 시그니처 | 예방 규칙 |
|---|---|---|
| **말단상 전용 CL 오류** | 초기 표본 누락, 1구획 CL 과대추정 | 분포상 표본을 확보하고 이중지수 가능성 확인 |
| **Vβ-as-Vss error** | $V_\beta/V_{ss}$가 큰데 loading/amount 계산에 $V_\beta$ 사용 | amount/steady-state에는 $V_{ss}$ 우선, terminal extrapolation에는 $V_\beta$ |
| **Phantom V2** | sparse design, $V_2$ RSE >100%, ETA(V2)(V2의 random effect; 개체 간 변동) shrinkage >80% | "작은 $V_2$" 결론 전 distribution-phase identifiability 확인 |
| **Pseudo-Stable V across renal function** | gentamicin-like 약물에서 $V_\beta$ vs CrCl plot이 거의 평탄하지만 multiple-dose plasma trough VPC(visual predictive check; 모델-관측치 시각 진단)는 신부전군에서 systematic underprediction. 신부전 시 $CL$과 β가 함께 감소하면 $V_\beta=CL/\beta$의 비율이 안정해 보이는 착시가 생깁니다. | covariate를 $V_\beta$가 아닌 $V_{ss}/V_1$에 attach하고, plasma trough VPC와 tissue accumulation 예측을 분리 검증 [실무 추론] |
| **Macro Drift** | $A/B$ high correlation, covariance instability | production에는 physiological parameterization 우선 |
| **초기 추정치 함정** | condition number 폭증, 초기치 변경만으로 결과 급변 | 초기 추정치 → 로그 영역 → 재파라미터화 순서로 디버깅 |
| **WRSS 단독 선택** | 최저 WRSS 모델이 높은 condition number | 잔차/정밀도/condition number/생물학적 타당성 동시 판단 |
| **F-test 오용** | weighting scheme이 다른 모델을 단순 F-test 비교 | PK7 규칙: 잔차/정밀도/상관성/최소 적절 모델을 함께 사용 |

### C. 전문가 해석 지점(Professional Moat) — 30년차 모델러가 1분 안에 보는 것

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| Semilog 곡선의 꺾임점과 말단 직선성이 보임 | $\alpha/\beta$ 구조 | → | 2구획/3구획 가능성 판단 | terminal curvature 확인 |
| $f_2$가 작거나 큼 | $f_2$ | → | terminal 반감기가 임상 시간 척도를 대표할지 결정 | plateau equation과 함께 해석 |
| $V_\beta/V_{ss}$ 비율 상승 | $V_\beta$, $V_{ss}$ | → | terminal volume 오용 위험 | loading/amount에는 $V_{ss}$ 우선 |
| WRSS는 낮지만 condition number/RSE/상관성이 나쁨 | condition number, RSE | → | production model 불안정 | 모델 보류 또는 좌표계 재검토 |
| CWRES vs TIME이 초기 양의 값 또는 S자 패턴 | CWRES(conditional weighted residuals; FOCE 기반 가중잔차) | → | 구조적 오설정 또는 분포상 누락 | sampling·구획 수 재점검 |
| η-shrinkage가 높음 | η-shrinkage | → | covariate effect 해석 가능성 낮음 | covariate 결론 보수화 |
| forward inclusion에서 공변량 추가 | $CL,Q,V_{ss},V_\beta$, condition number | → | covariate를 어디에 붙일지 결정 | M1–M5 동시 점검 [실무 통합 — §1 Workflow anchor의 §8 재호출] |

### D. 최소 실무 알고리즘(Minimal Practical Algorithm)

```text
1. Plot semilog C-time curve.
2. Early sampling이 distribution phase를 포착했는지 확인.
3. Bi-exponential 가능성이 있으면 A, α, B, β를 rough estimate.
4. AUC, f1, f2, V1, Vss, Vβ를 계산.
5. Vβ/Vss와 f2를 보고 terminal half-life 해석 가능성을 평가.
6. Physiological parameterization으로 CL, Q/Cld, V1, V2를 설정.
7. Fit 후 residual, RSE, correlation, condition number를 함께 확인.
8. Sparse design 또는 high shrinkage이면 V2/Q/covariate 해석을 보류.
9. Multiple dosing은 terminal half-life 하나가 아니라 f1/f2-weighted plateau equation으로 점검.
```

**최종 회수:** 2구획 모델의 mastery는 $C=Ae^{-\alpha t}+Be^{-\beta t}$를 외우는 것이 아닙니다. 좋은 모델러는 그 식을 보는 순간 **sampling adequacy, CL bias direction, volume choice, condition number risk, half-life misuse**를 함께 읽습니다.

---

## 출력 후 자가검증 체크리스트

| 항목 | 기준 | 결과 |
|---|---|---|
| SLIDE_START 개수 | §섹션수 + 카드수 합산 | 10 개 |
| 카드당 callout 합계 ≤ 6 | 전체 카드 | ✓ |
| [E] 박스 존재 | 모든 §2 카드 | ✓ |
| [D] 거장의 시각 존재 | 모든 §2 카드 | ✓ |
| [L] 파라미터 표 존재 | Apex 카드 + 정의 수식 카드 | ✓ |
| §5 혼동 쌍 표 행 순서 고정 (4행) | §5 전체 | ✓ |
| 기호 일관성 | 첫 등장 기준 통일 | ✓ |
| PART B 흔적 없음 | 전체 | ✓ |
| 수치 anchor 보존 | Compound X 100 µg, aspirin/gentamicin/nicardipine/PK8 수치 | ✓ |
| [M] 나비효과 이중 종착점 | Apex 카드 전체 | ✓ |

<!-- v3.8 변환 노트
- 라인/바이트: v3.7 778줄 / 66,966 B → v3.8 738줄 / 60,701 B (라인 -5.1%, 바이트 -9.4%)
  - 추가 압축 여지는 §3 HARD PRESERVE(약물명·수치·정의·임상 장면·진단 시그니처·자가검증 12항목)에 의해 차단됨. 의미 단위 readability는 §7·§10 기준으로 단일 패스 통과.
- 보존 감사:
  - SLIDE_START 마커: v3.7=10 / v3.8=10 (1:1)
  - 수식 블록($$..$$): v3.7=20 / v3.8=20 (전수 unique, 중복 0건)
  - 출처 anchor 총량: v3.7=65 → v3.8=61 (차이 4건은 §4 METACONTENT 규칙에 따라 본문에서 제거된 [EXPERT_INFERENCE, v3] 태그 4건; 의미 보존)
  - [실무 추론/확장/통합/디버깅 순서] 10건 1:1 보존
- 약물명 빈도 차이: aspirin 14→12, gentamicin 23→19, nicardipine 7→7, thiopental 2→2, Compound X 2→2, PK8 15→16.
  - aspirin/gentamicin 감소분은 §4 메타 문구("확인 시점", 카드 연결 안내, "정성적 예시로 보존" 등)에서 약물명이 보조적으로 재호출되던 부분을 정리한 결과로, 본 학습 사례 사용 횟수와 임상 시나리오는 모두 보존됨.
- 주요 변환:
  - §4 METACONTENT 제거: §1.5 정독 경로 분기, "확인 시점/학습 지시", 컴파일러 주석, [EXPERT_INFERENCE]/[v3] 태그
  - §5 금지 표현 일괄 치환: 닫는다→다룬다, 분기된다→달라진다, 평활한다→평탄해진다, 식별성이 무너진다→두 파라미터를 따로 추정할 수 없게 된다, 비대칭성이다→비대칭적이다, 시사한다→보여준다/신호다 등
  - §6 자기참조 즉해: "Mn의 결론이 ~한다" 형태 모두 결론 직접 진술 + 포인터 괄호
  - §7 약물 즉맥락: aspirin/gentamicin/nicardipine/thiopental/PK8 첫 등장에 분류 인라인 및 "→ 그래서 ~의 사례" 패턴 적용
  - §8 콜아웃 단일화: 한 블록 💡+⚠️ 중복 통합, 카드당 콜아웃 ≤6 유지
  - §9 시각화 우선: Workflow Anchor 등 분류성 줄글을 표/박스로 전환
  - §11 카드 구조 보존: SLIDE_START · 카드 ID · 카드 제목 · 수식 LaTeX · 출처 anchor 1:1 유지, 문장 톤만 §3–§10 규칙으로 재작성
-->

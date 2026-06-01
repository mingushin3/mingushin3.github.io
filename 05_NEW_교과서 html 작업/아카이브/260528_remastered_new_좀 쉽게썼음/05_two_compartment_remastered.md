# 세션 05 (Remastered) · 2구획 모델 — 하나의 곡선이 만드는 4개의 분기점

> **Source:** Gabrielsson & Weiner 5e Ch.2 §2.4.1–2.4.6 + Case Studies PK7/PK8 [G&W pp.57–77, 505–517] + Rowland & Tozer 5e Ch.19 [R&T pp.613–656]
>
> **재구성 원칙:** 원본 v4.0 보강본_final의 모든 콘텐츠·수식·출처·사례를 보존하되, 학습 동선을 "**하나의 plasma 곡선 → 4개 의사결정 분기점 → 각 분기점에서 잘못된 선택의 정량적 손해**" 구조로 한 줄에 꿰었음. M1~M5 카드 구조는 분기점 흐름에 녹여 재배치했고, 혼동쌍·자기테스트·확장 framework는 본문 동선에 따라 자연스럽게 노출되도록 옮겼음. 어미는 음슴체.

---

<!-- SLIDE_START: §0 | title: 이 세션이 진짜로 하려는 한 문장 -->
<!-- SECTION_CORE: SC-00 -->

## §0 — 이 세션이 진짜로 하려는 한 문장

먼저 두 숫자만 보고 시작함.

**44%** — Aspirin(저용량은 항혈소판제, 고용량은 NSAID로 쓰이는 약물) 650 mg IV bolus에서 early sampling을 놓치고 1구획으로 해석하면 $CL = 0.98$ L/min이 나옴. 이중지수로 다시 풀면 $CL = 683$ mL/min임. 그대로 유지 용량을 계산하면 **유지 용량도 44% 부풀어 나감** [R&T pp.615–620].

**6배** — Gentamicin(아미노글리코사이드 항생제로 치료범위가 좁고 신독성·이독성이 따라붙는 약물)에서 $V_\beta = 345$ L, $V_{ss} = 56$ L임. 어느 volume을 loading dose 계산에 넣느냐로 **첫 용량이 약 6배 흔들림** [R&T pp.630, 635–641].

이 두 숫자가 같은 함정의 두 얼굴임. 같은 plasma 곡선, 같은 환자, 같은 데이터인데 — **곡선을 어떻게 분해하고, 어떤 좌표계로 옮기고, 어떤 volume을 고르고, 어떤 half-life로 dosing을 결정하느냐**에 따라 임상 결론이 통째로 갈림.

이 세션의 본질을 한 문장으로 정리하면 이거임:

> **하나의 IV bolus plasma 곡선은 4개의 의사결정 분기점을 만들고, 각 분기점에서 잘못 가면 임상에서 정량화 가능한 손해가 나옴.**

**4개 분기점 미리보기:**

```text
[Plasma curve C(t)]
     │
     ├─ 분기점 1: Sampling adequacy ────────→ 잘못 가면 CL 44% 부풀음 (Aspirin)
     │
     ├─ 분기점 2: Volume choice (V1/Vss/Vβ) ─→ 잘못 가면 loading dose 6배 (Gentamicin) ⚡ Apex
     │
     ├─ 분기점 3: Parameterization stability ─→ 잘못 가면 condition number 100배 (PK8)
     │
     └─ 분기점 4: Half-life interpretation ──→ 잘못 가면 multiple dosing 통째로 (Nicardipine + GM)
```

원본의 M1~M5 카드는 사실 이 4개 분기점을 지나가는 데 필요한 도구들임. 본 핸드아웃은 분기점을 따라 도구를 꺼내쓰는 순서로 다시 배열했음.

**왜 이게 PopPK forward inclusion 단계에서 동시에 작동하는지** — 한 표로 미리 박아둠.

| 임상 결정 사항 | 어느 분기점이 답하나 |
|---|---|
| 신기능 변화가 어느 phase를 흔드는가? | 분기점 1 ($f_2$) + 분기점 4 |
| Covariate를 $CL$에 붙일까 $\beta$에 붙일까? | 분기점 2 (좌표계) |
| 체중·조직 amount는 어떻게 해석? | 분기점 2 ($V_{ss}/V_\beta$ 구분) |
| 그 covariate model이 제출 가능한가? | 분기점 3 (condition number / RSE) |

**선행 지식:** 1구획 IV bolus, $AUC=Dose/CL$, $V_d=CL/k$, MRT/AUMC, 선형 ODE.
**후속 연결:** NONMEM ADVAN3/4/11/12, sparse sampling, η-shrinkage(ETA에 정보가 부족할 때 커지는 진단 지표), 3구획, tissue/target-site PK.

---

<!-- SLIDE_START: §1 | title: 곡선이 왜 두 개로 갈라지는가 -->
<!-- SECTION_CORE: SC-01 -->

## §1 — 곡선이 왜 두 개로 갈라지는가 (ODE 구조에서 출발)

분기점으로 들어가기 전에, **"왜 한 곡선이 두 직선으로 갈라지는가"**를 ODE 구조로 한 번에 정리하고 가자. 이걸 ODE 관점에서 안 잡고 가면 4개 분기점이 다 흔들림.

> **거장의 시각**
> 두 지수항을 "두 개의 제거 경로"로 읽는 순간 핵심을 놓침. **phase slope는 ODE eigenvalue임** — 두 사람이 따로 문 나가는 그림이 아니라, **하나의 시스템에서 관찰되는 두 회전 속도**임.

### 1.1 ODE 구조 — 왜 eigenvalue가 2개이고, 그래서 곡선이 2개 phase로 갈라지는가

중앙·말초구획 ODE는 이렇게 생김.

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

선형 상수계수 $2\times 2$ ODE의 해는 두 지수항의 합임. 그래서 $\alpha, \beta$는 system matrix의 두 eigenvalue로 결정되고, 다음 두 관계가 **자동으로** 따라옴 [G&W pp.61–62; R&T pp.618–619].

$$
\underbrace{\alpha+\beta}_{\text{고유값 합}}
=\underbrace{k_{12}}_{\text{중앙→말초}}+
\underbrace{k_{21}}_{\text{말초→중앙}}+
\underbrace{k_{10}}_{\text{중앙 제거}},
\qquad
\underbrace{\alpha\beta}_{\text{고유값 곱}}
=\underbrace{k_{21}k_{10}}_{\text{회귀×제거}}
$$

> 💡 한 줄로: $\alpha, \beta$는 엔진 부품 하나하나가 아니라 **여러 기어가 맞물린 뒤 바퀴에서 관찰되는 두 회전 속도**임. 그래서 macro 4개 숫자($A, \alpha, B, \beta$)는 독립이 아니라 micro-parameter 공간의 수학적 제약을 받는 값들임.

### 1.2 이중지수식과 잔차법 — 곡선을 4개 숫자로 압축하는 단계

IV bolus 후 plasma curve를 반로그 도표(농도축만 로그인 그래프)에 그렸을 때 직선 하나가 아니라 **두 직선의 합**으로 보이면 이렇게 적음 [G&W pp.59–60; R&T pp.615–617].

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
| $A$ | 농도 | 빠른 α phase의 $t=0$ 외삽 절편 | 초기 분포상 크기, early sampling에 민감 |
| $B$ | 농도 | 느린 β phase의 $t=0$ 외삽 절편 | 말단상 크기, terminal sampling에 민감 |
| $\alpha$ | time$^{-1}$ | 빠른 phase slope | 분포속도, 일부 제거 영향 |
| $\beta$ | time$^{-1}$ | 느린 phase slope | 제거와 재분포가 결합 |

**잔차법(Method of Residuals).** terminal β phase를 log-linear 회귀로 외삽해서 $Be^{-\beta t}$를 만들어두고, 초기 관측치에서 빼면 잔차 $C_{resid}(t)=C_{obs}(t)-Be^{-\beta t}$가 나옴. 이 잔차를 다시 반로그 도표에 놓고 직선이면 기울기가 $-\alpha$, 절편이 $A$임 [G&W p.60; R&T p.616].

| 단계 | 가정 | 수식 |
|---|---|---|
| 1 | 말단부가 log-linear | $C_\beta(t)=Be^{-\beta t}$ |
| 2 | 초기 관측치에서 말단 외삽값 제거 | $C_{resid}(t)=C_{obs}(t)-Be^{-\beta t}$ |
| 3 | 잔차를 semilog로 재배치 | slope $=-\alpha$, intercept $=A$ |

> 💼 **실무 인사이트.** 잔차법은 NONMEM 실용 알고리즘이 아님. 손으로 curve-stripping을 해 보는 이유는 simultaneous nonlinear regression에 넣을 **초기 추정치의 감각**을 기르기 위해서임. 초기치가 자릿수부터 틀어지면 좌표계가 아무리 좋아도 condition number가 폭증함 (분기점 3에서 다시 나옴).

### 1.3 단위 일관성 — G&W Fig.2.43 직접 읽기

G&W p.60 Fig.2.43 caption은 단위를 명시적으로 정함: **$A\approx 70~\text{mg·L}^{-1}$, $B=28~\text{mg·L}^{-1}$, $\alpha,\beta$ 모두 $\text{min}^{-1}$** [G&W p.60 Fig.2.43 caption 직접 인용].

$$
\underbrace{\alpha}_{[\text{min}^{-1}]}
=\frac{\overbrace{\ln(70/10)}^{\text{무차원}}}{\underbrace{130~[\text{min}]}_{\text{시간간격}}}
\approx 0.0150~[\text{min}^{-1}],
\qquad
\underbrace{\beta}_{[\text{min}^{-1}]}
=\frac{\overbrace{\ln(28/10)}^{\text{무차원}}}{\underbrace{450~[\text{min}]}_{\text{시간간격}}}
\approx 0.00229~[\text{min}^{-1}]
$$

이걸 한 번 명시해두면 downstream 모든 식의 단위가 일관적으로 흐름. $AUC$ 단위는 $[\text{mg·min·L}^{-1}]$, $AUMC$ 단위는 $[\text{mg·min}^2\text{·L}^{-1}]$, $t_{1/2,\alpha}=0.693/\alpha\approx 46.2$ min, $t_{1/2,\beta}=0.693/\beta\approx 302.6$ min임. **단위 audit 1단계 — 이게 안 맞으면 그 뒤 모든 계산이 통째로 의심받음** [G&W p.60; 실무 추론].

### 1.4 2차 파라미터 — AUC, AUMC, $f_1/f_2$

곡선을 분해했으니 이제 거기서 임상이 쓰는 2차 파라미터를 뽑음.

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

**$f_2$의 임상적 의미가 핵심임.** $f_2$가 크면(보통 >0.8) terminal phase를 elimination 해석으로 끌고 가도 됨. **$f_2$가 작으면** terminal slope는 elimination보다 **재분포를 더 많이 반영**하고 있음 [G&W p.63; R&T pp.622–623].

> 🔑 **Terminal 해석 규칙:** $f_2$를 보지 않고 terminal slope를 "elimination phase"라고 부르는 순간, 반감기와 dosing interval 해석이 동시에 흔들림. 이게 분기점 4에서 다시 폭발함.

### 1.5 ⚡ 메타포 정리 — "이사 vs 청소"는 근사 레이블임

α phase는 약이 혈장에서 조직으로 **이사 가는** 분포 단계, β phase는 주로 **청소(제거)**가 지배하는 단계로 부르는 게 보통임. 단, 두 단계가 분리된 게 아니라 **항상 동시에** 일어남 — α 단계에도 제거가 있고, β 단계에도 분포 평형 조정이 있음. **"α = 분포, β = 제거"는 근사 레이블이지 기계적 분리가 아님.** 이 레이블을 두 개의 elimination pathway로 곡해하는 순간 central elimination 가정이 무너짐.

> 📖 **G&W p.60, Fig.2.43:** IV bolus 후 이중지수 감소를 보여주는 반로그 도표. 관측 곡선이 하나의 말단선이 아니라 두 개의 외삽된 phase line의 합으로 보임. → 잔차법이 왜 한 그림을 두 직선으로 분리해서 보는지가 한 장에 다 들어있음.

### 1.6 경계 조건 — 이 모든 게 깔리는 가정

선형 약동학, 중앙구획 내 빠른 혼합, 분포상 관측 확보, mammillary 배열(중앙구획을 허브로 두는 방사형 다구획 구조), 중앙구획 제거 가정 — 이 다섯이 받쳐줄 때만 위 모든 식이 성립함. 하나라도 깨지면 bi-exponential fit은 여전히 가능해도 생리학적 해석이 흔들림 [G&W pp.57–65; R&T pp.617–619].

이제 곡선 분해는 끝났음. 진짜 의사결정 분기점으로 들어감.

---

<!-- SLIDE_START: §2 | title: 분기점 1 — Sampling adequacy, Aspirin Warning -->
<!-- SECTION_CORE: SC-02 -->

## §2 — 분기점 1: Sampling Adequacy — Aspirin Warning

> **거장의 시각**
> Early sampling을 놓치는 순간 곡선이 1구획처럼 보임. 1구획으로 fitting 하면 분포상의 빠른 감소가 다 elimination으로 흡수돼서 **CL이 시스템적으로 과대 추정됨.** 이건 데이터 양의 문제가 아니라 **데이터가 phase를 식별해 주는가**의 문제임.

### 2.1 무슨 일이 벌어지는가 — 숫자로 못 박기

Aspirin 650 mg IV bolus에서:
- **말단상 전용 1구획 해석:** $CL = 0.98$ L/min
- **이중지수 해석:** $CL = 683$ mL/min

차이 약 **44%**. 1구획 해석이 $CL$을 **과대 추정**함. 유지 용량 공식이 $\text{Maintenance rate} = CL \cdot C_{ss,\text{target}}$이니까, **유지 용량도 그대로 44% 부풀어 나감** [R&T pp.615–620].

| 상황 | 파라미터 변화 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| early sampling 누락 | $A, \alpha$ 정보 약화 | → | terminal-only $CL$ 과대 추정 | 분포상 표본 확보 |
| terminal line만 사용 | $CL=0.98$ L/min로 계산 | → | 유지용량 과대 산정 위험 | biexponential 가능성 점검 |
| terminal 직선이 휘어짐 | 2구획 부족 가능 | → | half-life 해석 불안정 | 3구획 또는 NCA 고려 |

### 2.2 왜 1구획 해석이 CL을 과대 추정하는가 — 직관

1구획 가정에서는 $C(t) = C_0 e^{-kt}$로 놓고 $CL = k \cdot V$로 계산함. 그런데 진짜 곡선은 두 phase의 합이라서, 초기 농도가 빠르게 떨어지는 분포상이 있음. **이걸 1구획에 우겨 넣으면 $k$가 실제 elimination보다 크게 추정되고**, 그 결과 $CL = k \cdot V$도 같이 부풀어 나옴.

> 💡 한 줄로: 분포상에서 약이 조직으로 빠지는 걸 "제거로 사라지는 것"으로 잘못 셈하는 게 1구획의 함정임.

### 2.3 그래프 3초 점검표

곡선을 처음 보는 순간 다음 셋만 확인하면 됨 [G&W p.63; R&T p.632]:

1. **꺾임점(knee)이 어디인가?** → $\alpha/\beta$ 비
2. **두 phase의 면적 비율이 어느 쪽으로 기우는가?** → $f_1/f_2$
3. **terminal 직선이 정말 직선인가?** → 3구획 가능성

### 2.4 첫 번째 분기점의 함정 — 혼동쌍

이 자리에서 가장 자주 깨지는 함정은 **"bi-exponential curve vs two elimination processes"**임.

| 비교 기준 | Bi-exponential phase | "Two elimination processes" |
|---|---|---|
| 의미 | $Ae^{-\alpha t}+Be^{-\beta t}$ — 한 시스템의 두 eigenvalue | 독립 제거 경로 2개가 따로 작동? |
| 수식 위치 | $\alpha, \beta$는 지수부 slope | 제거경로라면 별도 clearance 항 필요 |
| 변화 원인 | distribution + elimination 합성된 ODE eigen-component | 제거 장기 2개 작동? (잘못된 직관) |
| 혼동 시 결과 | $f_2$가 작은데 terminal을 "elimination phase"로 부르면 위험 | central elimination 가정과 sampling adequacy 판단이 한꺼번에 실패 [G&W p.63; R&T pp.622–623] |

### 2.5 자기 점검 1

**Q.** Aspirin 650 mg IV bolus에서 말단상 전용 1구획 해석은 $CL=0.98$ L/min, 이중지수 해석은 $CL=683$ mL/min임. 말단상 전용 해석은 실제 $CL$을 과소평가함, 과대평가함?

**A.** **과대평가함.** $0.98$ L/min은 683 mL/min보다 약 **44% 높음.** 유지 용량 계산이 그대로 따라 부풀어 나갈 위험이 있음 [R&T pp.615–620].

---

<!-- SLIDE_START: §3 | title: 같은 곡선, 세 개의 좌표계 -->
<!-- SECTION_CORE: SC-03 -->

## §3 — 같은 곡선, 세 개의 좌표계 (분기점 2 진입)

분기점 1을 통과해서 $A, \alpha, B, \beta$를 잡았음. 이제 이 4개 숫자를 **어떤 좌표계로 옮길지** 결정해야 함. 좌표계 선택이 분기점 2(volume choice)로 직결되기 때문에 먼저 좌표계 지형도를 그려놓고 가야 함.

> **거장의 시각**
> 좌표계를 섞으면 자유도·가정·임상 해석이 한 문장 안에서 뒤엉킴. **fit은 macro로 이해하고, ODE는 micro로 점검하며, 보고와 covariate 해석은 physiological parameter로 마무리**하면 reviewer 질문이 깨끗하게 정리됨.

### 3.1 세 좌표계 한눈에

같은 2구획 곡선이 세 가지 좌표계로 표현됨 [G&W pp.60–71; R&T pp.618–619].

| 좌표계 | 파라미터 집합 | 역할 |
|---|---|---|
| **Macro** | $A,\alpha,B,\beta$ | 관측 plasma 곡선의 두 지수항 표현 |
| **Micro** | $V_1,k_{10},k_{12},k_{21}$ | 구획 ODE의 분율 속도 상수(fractional rate constant) |
| **Physiological** | $V_1,CL,Cld,V_t$ | 청소율, 분포 청소율, 중앙/말초 용적 |

> 💡 **메타포:** Macro는 사진의 픽셀 좌표, Micro는 카메라 내부 렌즈 배치, Physiological은 의사가 읽는 판독문임. 같은 사진이라도 어떤 좌표로 말하느냐에 따라 책임지는 질문이 달라짐.

### 3.2 변환식 — 좌표계 간 다리

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

### 3.3 자유도가 왜 4개인가 — 그리고 혼합 표현의 함정

M1에서 본 두 지수항은 곡선을 설명하는 **4개 자유도**임. 출처가 지원하는 4-파라미터 집합은:
- micro $(V_1, k_{10}, k_{12}, k_{21})$, 또는
- physiological $(V_1, CL, Cld, V_t)$

둘 중 하나임. **혼합 표현 $(V_1, V_t, k_{10}, k_{12})$를 독립 자유도처럼 쓰는 건 안 됨** — 종속 관계가 깨짐 [G&W pp.60–62, 71].

### 3.4 ⚠️ 비식별성(Non-identifiability) — plasma 데이터의 근본 한계

plasma 이중지수 곡선만 보고 있으면 **중앙구획 단독 제거, 말초구획 단독 제거, 양 구획 제거**를 구별할 수 없음. 통상 중앙구획 단독 제거 모델을 쓰는 이유는 **생리적으로 그럴듯하기 때문**이지, plasma 데이터가 그걸 증명했기 때문이 아님 [G&W p.65; R&T pp.618–619].

> ⚠️ plasma curve가 같다고 elimination site까지 식별되는 건 아님. **제거 위치는 자료가 증명한 사실이 아니라 모델 가정으로 보충되는 부분.**

**보고할 때 명시할 것.** "중앙구획에서만 제거"라는 가정과 "말초구획 단순 통합" 가정을 보고서에 명시해야 함. 조직 PK, 거대 단백 약물, 표적 매개 제거(target-mediated)가 의심되면 이 가정에 대한 기전적 근거를 함께 제시해야 함 [R&T pp.618–619; 실무 추론].

> 📖 **G&W p.65, Fig.2.46:** 동일한 plasma 이중지수 곡선에 적합되는 세 가지 2구획 모델(중앙 제거, 말초 제거, 양 구획 제거)을 한 그림에 겹쳐 놓음. → 같은 plasma curve가 elimination site를 식별해 준다는 잘못된 추론을 한 장으로 차단해 줌.

### 3.5 NONMEM 연결 — ADVAN3 / TRANS4

> 💼 **실무 인사이트.** ADVAN3 / TRANS4의 표준 표현이 바로 $CL, V_1, Q, V_2$임. 내부에서는 $K=CL/V_1$, $K_{12}=Q/V_1$, $K_{21}=Q/V_2$로 ODE 전이를 만듦. **보고서 좌표와 추정 좌표가 같으니 reviewer가 즉시 읽을 수 있음.** 이게 분기점 3(parameterization stability)에서 ODE 좌표계가 압승하는 첫 번째 이유임.

### 3.6 좌표계 혼동 쌍

| 비교 기준 | Macro | Physiological |
|---|---|---|
| 단위 | $A,\alpha,B,\beta$ — 농도 + time$^{-1}$ | $CL, Q, V_1, V_2$ — volume/time + volume |
| 수식 위치 | 지수항 계수와 slope | ODE 전이 + 보고용 |
| 변화 원인 | 관측 curve geometry, sampling | 제거능, 분포 흐름, 중앙·말초 용적 |
| 혼동 시 결과 | curve description만 남음 | covariate 보고와 dosing 해석 가능. 둘을 별개로 처리하면 condition number와 interpretability 판단이 한꺼번에 실패 |

> ⚡ **메타포 — 내부 고속도로 vs 나가는 출구.** 좌표계 전환에서 가장 자주 헷갈리는 핵심 쌍은 **$Q$ vs $CL$**임. $Q$(intercompartmental clearance)는 중앙·말초 사이를 오가는 **내부 순환량**(고속도로 통행량), $CL$(systemic clearance)은 체내에서 완전히 빠져나가는 **순 배출량**(출구)임. $Q$가 크면 두 구획이 빠르게 균형을 잡아서 α phase가 짧아지고, $CL$이 크면 전체 약물이 빠르게 제거됨. **$Q \gg CL$이면 2구획 성격이 약해져서 1구획처럼 보일 수 있음** — 이게 macro($\alpha, \beta$) ↔ physiological($Q$, $CL$) 좌표계 변환에서 비로소 보이는 시스템 진단 단서임.

좌표계 지형도가 깔렸으니, 이제 진짜 분기점 2 — **Volume choice** — 로 들어감.

---

<!-- SLIDE_START: §4 | title: 분기점 2 — Volume choice, Gentamicin Disaster -->
<!-- SECTION_CORE: SC-04 -->

## §4 — 분기점 2: Volume Choice — Gentamicin Disaster [⚡ Apex Concept]

여기가 학생들이 **가장 많이 다치는 자리**임. 이번 챕터의 본체임.

> **거장의 시각**
> 💢 흔한 오해: terminal half-life가 길면 그 약은 넓게 분포한다고 생각하기 쉬움. 이게 왜 위험하냐면 — $V_\beta$는 terminal slope geometry와 $CL$이 만든 **겉보기** volume이라서, $V_{ss}$나 $V_1$이 답해주는 임상 질문엔 답을 못 함.
>
> **체화할 단 하나의 직관:** volume을 묻는 순간 먼저 **"bolus 직후인가, steady state인가, terminal extrapolation인가"**를 되물어야 함.

### 4.1 세 개의 volume — 무엇이 다른가

2구획에서 "volume of distribution"은 **하나가 아님.** 세 개임 [R&T pp.617, 628–630; G&W pp.63–65].

| Volume | 공식 | 의미 | 임상 질문 |
|---|---|---|---|
| $V_1$ | $V_1=Dose/(A+B)$ | 초기 희석 / 중앙구획 용적 | bolus 직후 peak은? |
| $V_{ss}$ | $V_{ss}=MRT\cdot CL=Dose\cdot AUMC/AUC^2$ | 정상상태 체내량 / plasma 비율 | loading dose는? 정상상태 amount는? |
| $V_\beta$ | $V_\beta=CL/\beta=Dose/(AUC\cdot\beta)$ | 말단 기울기 기반 겉보기 용적 | terminal extrapolation 시? |

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

> 💡 **3단 메타포:** $V_1$은 문을 열자마자 물이 찬 **첫 방**, $V_{ss}$는 모든 방의 수위가 안정된 뒤의 **집 전체**, $V_\beta$는 마지막 배수 속도를 보고 거꾸로 추정한 **집 크기**임. "volume이 얼마입니까?"라는 질문 자체가 **불완전한 질문**임 — bolus 직후인지, steady state인지, terminal extrapolation인지부터 되물어야 함.

### 4.2 순서 관계 — $V_1 \le V_{ss} \le V_\beta$

표준 중앙구획 제거 2구획 가정에서 [R&T pp.629–630]:

$$
\underbrace{V_1}_{\text{초기희석}}\le
\underbrace{V_{ss}}_{\text{분포평형}}\le
\underbrace{V_\beta}_{\text{말단 V}}
$$

이 부등식은 **모델 가정 안에서의 실무 규칙**이지 보편 법칙은 아님. 그런데 왜 $V_\beta \ge V_{ss}$인가? 이게 학생들이 가장 자주 묻는 자리니까 기전을 명확히 해두자.

### 4.3 ⭐ 왜 $V_\beta \ge V_{ss}$인가 — 기전적 직관

R&T p.628 Fig.19-9가 답을 직접 줌:

> "the **faster a drug is eliminated relative to distribution**, the greater is the ratio of drug in slowly equilibrating tissues to that in plasma during the terminal phase, and correspondingly, the **larger is the apparent volume of distribution**" [R&T p.628].

풀어서 한 줄로 정리하면:

- **이상적인 정상상태**($CL=0$인 가상의 평형)에서는 조직과 혈장의 농도비가 진짜 분배계수 $K_p$에 정확히 일치함. 이때 $V = V_B + K_p \cdot V_T$ (혈장 + 조직). 이게 $V_{ss}$의 개념적 기준임.
- **실제 elimination이 작동하는 terminal phase**에서는 혈장 농도가 elimination에 의해 계속 떨어지는데, **slowly equilibrating tissue는 그 하락을 따라잡지 못함(lag)**. 그래서 terminal phase 중에는 "조직/혈장 농도비"가 진짜 $K_p$보다 큰 **겉보기 $K_{p,\text{app}}$**가 됨.
- $V_\beta = V_B + K_{p,\text{app}} \cdot V_T$이고 $K_{p,\text{app}} > K_p$이므로 **$V_\beta > V_{ss}$** 가 따라옴.

$$
\underbrace{V_{ss}}_{\text{진짜 평형 V}}
=\underbrace{V_B}_{\text{혈장}}+\underbrace{K_p}_{\text{진짜 분배}}\cdot\underbrace{V_T}_{\text{조직}}
\;<\;
\underbrace{V_\beta}_{\text{말단 겉보기 V}}
=\underbrace{V_B}_{\text{혈장}}+\overbrace{\underbrace{K_{p,\text{app}}}_{\text{lag로 부풀린 분배}}}^{\;>K_p\;}\cdot\underbrace{V_T}_{\text{조직}}
$$

> 💡 **재분포 지연을 elimination 부족으로 흡수해 더 큰 부피처럼 보이는 게 $V_\beta$임.** 한 줄로 — $V_\beta$는 terminal slope만 보고 역산하니까, 조직에서 혈장으로 돌아오는 속도가 느릴수록 (재분포 지연이 클수록) 그 지연을 "혈장이 천천히 빠진다"고 잘못 읽어 더 큰 부피로 환산함. **Elimination이 distribution보다 빠를수록 $V_\beta/V_{ss}$ 비율이 커짐** [R&T p.628 Fig.19-9 직접 인용].

### 4.4 사례 두 개 — Aspirin (안전) vs Gentamicin (위험)

이 차이가 임상에서 얼마나 폭발하는지 보자.

**Aspirin (안전한 사례):** $V_1=6.5$ L, $V_{ss}=10.4$ L, $V_\beta=13.7$ L. 세 값에 차이는 있지만 치명적이지 않음 [R&T pp.617, 629–630].

$$
\underbrace{\left(\frac{V_\beta}{V_{ss}}\right)_{aspirin}}_{\text{ASA 말단부풀림}}
\approx\frac{13.7}{10.4}\approx 1.3
$$

**Gentamicin (위험한 사례):** $V_1=14$ L, $V_{ss}=56$ L, **$V_\beta=345$ L** — $V_\beta$가 $V_{ss}$보다 약 **6배** 큼 [R&T pp.630, 635–641].

$$
\underbrace{\left(\frac{V_\beta}{V_{ss}}\right)_{gentamicin}}_{\text{GM 말단부풀림}}
\approx\frac{345}{56}\approx 6.2
$$

**왜 gentamicin에서 이렇게 폭발하는가?** Gentamicin은 distribution이 permeability-limited라서 distribution이 느림 ($k_{21}$이 작음). 그런데 elimination ($k_{10}$)은 신장으로 빠르게 돌아감. 결과: elimination이 distribution보다 훨씬 빠름 → $K_{p,\text{app}}$가 진짜 $K_p$보다 크게 부풀음 [R&T pp.628, 630, 635–641].

| 상황 | 파라미터 변화 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| Aspirin-like | $V_\beta/V_{ss}\approx 1.3$ | → | terminal volume 오용 위험 제한적 | 그래도 volume 정의는 명시 |
| Gentamicin-like | $V_\beta/V_{ss}\approx 6.2$ | → | loading dose 과대 산정·peak 독성 위험 | $V_{ss}$ 중심으로 판단 |
| 느린 재분포 | $\beta$ 감소, $V_\beta$ 증가 | → | terminal half-life가 plasma 조절 시간과 분리 | 초기 phase와 $f_2$ 확인 |

### 4.5 ⚠️ 치명적 타격 — Loading dose 6배 차이의 임상 결과

NDA/IND 제출이나 critical care 상황의 loading dose 결정에서 **$V_\beta$를 $V_{ss}$ 대신 쓰면** gentamicin-like 약물의 첫 dose가 **약 6배 과대 산정됨.** 결과:

1. 심사관이 dosing rationale의 volume 정의 일관성 결여를 **FDA Deficiency Letter** 사유로 지적함, 또는
2. 환자에게 nephrotoxicity/ototoxicity 임계 농도를 **첫 60분 안에 plasma peak이 넘는** 사건이 발생함.

$$
\underbrace{\frac{V_\beta}{V_{ss}}}_{\text{말단V 오용}}
\approx
\frac{\underbrace{345}_{\text{GM }V_\beta}}{\underbrace{56}_{\text{GM }V_{ss}}}
\approx 6.2
$$

> 🔑 **Volume 선택 규칙:** loading dose와 steady-state amount에는 **$V_{ss}$**, bolus 직후 peak에는 **$V_1$**, terminal extrapolation에는 **$V_\beta$**.

### 4.6 가장 위험한 함정 — "Terminal half-life가 길다 = 분포가 넓다"

이건 정말 자주 들리는 잘못된 직관임. 그럴듯한 이유가 있음 — $t_{1/2,\beta}=0.693/\beta$이고 $V_\beta=CL/\beta$이니까, 작은 $\beta$가 큰 volume처럼 보임. 하지만 이걸 그대로 두면 도미노가 시작됨:

```
terminal half-life 길다고 인식
  → "넓은 분포"로 직역
  → $V_\beta$를 body amount나 loading dose에 사용
  → gentamicin-like 약물에서 첫 dose 6배 과대 산정
  → 첫 60분 안에 plasma peak이 nephrotoxicity 임계 돌파
  → 규제 측에서 Deficiency Letter 또는 재분석 요구
```

$$
\underbrace{t_{1/2,\beta}}_{\text{말단 반감기}}
=\frac{\overbrace{0.693}^{\ln2}}{\underbrace{\beta}_{\text{β slope}}},
\qquad
\underbrace{V_\beta}_{\text{말단 V}}
=\frac{\underbrace{CL}_{\text{정화능}}}{\underbrace{\beta}_{\text{β slope}}}
$$

> 💡 느린 재분포는 **멀리 있는 창고에서 물건이 늦게 돌아오는 현상**임. **창고가 거대해서가 아니라 왕복 도로가 좁아서** 마지막 움직임이 길게 보일 수 있음.

### 4.7 Thiopental 직관 — 친유성 약물의 사전 경고 신호

**Thiopental**(지용성 barbiturate, 정맥 마취유도제로 쓰이는 약물)에 대한 R&T의 개 실험 예시에서는 지방으로의 분배가 크고 adipose tissue가 total apparent $V_d$의 큰 몫을 차지함. 친유성·관류·분배 정보는 새 약물의 $V_{ss}/V_1$과 $V_\beta$ 부풀림을 **사전에 의심하게 해 주는 단서**임 [R&T pp.614–615].

### 4.8 다회투여 volume 규칙

- fluctuation이 작고 true steady state에 가까울 때: **$V_{ss}$**가 amount estimate에 유용함.
- interval 말기 distribution equilibrium에 가까울 때: **$V_\beta$**도 approximation으로 쓸 수 있음.
- **Gentamicin-like 약물처럼 interval 내 distribution disequilibrium이 크면 어느 volume도 단순 적용하기 어려움** [R&T pp.638–639].

### 4.9 Volume 혼동 쌍 — Critical Blow

| 비교 기준 | $V_1, V_{ss}$ | $V_\beta$ |
|---|---|---|
| 용도 | bolus 직후 또는 steady-state amount용 | terminal slope 기반 apparent volume |
| 수식 | $V_1=Dose/(A+B)$, $V_{ss}=MRT\cdot CL$ | $V_\beta=CL/\beta$ |
| 변화 원인 | 중앙 희석, 분포 평형, 조직 분배 | 작은 $\beta$, 느린 재분포 |
| 혼동 시 결과 | loading dose, amount-at-steady-state 직결 | Gentamicin: $V_\beta=345$, $V_{ss}=56$, $V_1=14$. $V_\beta$를 "진짜 body volume"처럼 쓰면 tissue redistribution과 plasma dosing이 한 숫자에 섞임 |

> ⚡ **메타포 — 지금 vs 균형 vs 마지막 기울기.** $V_1$은 투여 직후 약이 도달한 **즉각적 분포 공간**, $V_{ss}$는 분포와 제거가 균형 잡힌 뒤의 **평형 상태 겉보기 부피**, $V_\beta$는 terminal slope에서 역산한 **제거 편향이 섞인 겉보기 부피**임. **Loading dose는 $V_{ss}$, AUC 정규화는 $CL$, terminal half-life는 $V_\beta/CL$에 연결됨 — 세 부피를 섞으면 세 계산이 다 틀림.**

### 4.10 자기 점검 2

**Q.** Aspirin과 gentamicin 중 $V_\beta/V_{ss}$ 비율이 더 큰 약물은? 그게 왜 중요한가?

**A.** **Gentamicin.** Aspirin은 $13.7/10.4 \approx 1.3$이지만 gentamicin은 $345/56 \approx 6.2$임. 큰 비율은 **말단 기울기에서 나온 용적을 정상상태 체내량 용적처럼 쓰면 안 된다**는 경고임 [R&T pp.629–641].

> 📖 **R&T p.628, Fig.19-9:** 분포용적 용어와 제거가 $V$ 및 $V_{ss}$에 미치는 영향을 정리한 그림. **$V_1$, $V_{ss}$, $V_\beta$가 왜 서로 바꿔 쓸 수 없는지** — 그리고 elimination이 distribution보다 빠를수록 $K_{p,\text{app}}$가 진짜 $K_p$보다 부풀어 $V_\beta$가 커지는 정확한 기전 — 을 한 장으로 가장 잘 보여줌.

분기점 2를 마무리하면서 분기점 3으로 이어주는 한 줄: **volume을 옳게 골랐다고 끝이 아니라, 그 volume이 들어간 좌표계에서 추정이 안정한가 — 이게 분기점 3임.**

---

<!-- SLIDE_START: §5 | title: 분기점 3 — Parameterization stability, PK8 -->
<!-- SECTION_CORE: SC-05 -->

## §5 — 분기점 3: Parameterization Stability — PK8

올바른 volume을 골라서 좌표계를 구성했음. 이제 그 좌표계로 데이터에 fit 했을 때 **추정 geometry가 무너지지 않는가**를 점검함. 이게 NDA 제출 모델을 결정짓는 마지막 통과 조건임.

> **거장의 시각**
> 가장 낮은 WRSS를 고르는 습관이 문제임 — fit residual만 보고 covariance geometry는 못 보고 있는 것임. **condition number, RSE, 상관성까지 같이 봐야** "맞아 보이는 모델"과 "제출 가능한 모델"이 분리됨.

### 5.1 PK8 사례 — 같은 데이터, 5개 parameterization, condition number 100배 차이

**Compound X**(G&W PK8의 가상 화합물) 100 µg IV bolus 데이터에서 G&W는 5가지 parameterization을 비교함. Table 8.1의 condition number는:

| 모델 계열 | Condition Number | 핵심 파라미터화 | 판단 |
|---|---:|---|---|
| **ODE 생리학적** | **29.69** | $CL, V_1, Cld, V_t$ | **최저, 가장 안정** |
| Macro | 125.2 | $A, \alpha, B, \beta$ | 절편/기울기 상관 가능성 큼 |
| Colburn | 2,243 | $V(t)$의 지수적 접근 | 시간 의존적 용적 |
| 재파라미터화 CL | 2,306 | $D_{iv}, CL$ 포함 | 청소율 언어 연결 |
| Takada | 3,186 | 시간 의존적 $V(t)$ | **WRSS는 낮지만 condition number 폭증** |

**최대/최소 비율 약 107배** [G&W pp.513–517].

> 💡 **핵심 한 줄:** 같은 데이터, 비슷한 fit이어도 좌표계 하나로 covariance geometry가 **100배 단위로 흔들림.** Reparameterization은 표기를 치장하는 게 아니라 **estimation geometry를 바꾸는 preconditioning**임. 같은 지도라도 접는 방향만 바꾸면 주머니에 잘 들어가거나 찢어질 수 있는 것처럼.

### 5.2 핵심 교훈 — WRSS와 Condition Number는 다른 질문에 답함

| 지표 | 무엇을 묻나 | 단독으로 보면? |
|---|---|---|
| **WRSS** | "얼마나 잘 맞았나" (residual fit 크기) | fit 품질 |
| **Condition Number** | "그 맞음이 안정적으로 추정되나" (정보 행렬 안정성) | covariance geometry |
| **RSE** | "각 파라미터 자체의 신뢰성" (relative standard error) | 개별 추정의 정밀도 |

PK8의 핵심 메시지: **Takada model**은 WRSS가 낮아도 condition number가 크고, **ODE model**은 condition number가 가장 낮음. 따라서 **lowest WRSS = best model**이 아님 [G&W p.516].

| 상황 | 파라미터 변화 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| WRSS만 최저 | residual fit만 개선 | → | 불안정한 모델 채택 위험 | condition number/RSE 병행 |
| condition number 폭증 | 정보 행렬 불안정 | → | covariate 추가 시 결과 비재현 | 초기치·로그 파라미터화·좌표계 순서 점검 |
| ODE 좌표 안정 | $CL, V_1, Cld, V_t$ 해석 가능 | → | reviewer 방어 용이 | production 후보 우선 고려 |

### 5.3 디버깅 순서 — Condition Number가 폭증할 때

> 💼 **실무 인사이트.** condition number가 폭증하면 **좌표계부터 바꾸기 전에 THETA 초기치를 먼저 확인**해야 함. 초기치가 자릿수부터 틀어져 있으면 좌표계와 무관하게 정보 행렬이 나빠질 수 있음.

**디버깅 순서 — 위에서 아래로:**

1. **초기 추정치(THETA initial)** 점검 → 자릿수가 맞나?
2. **로그 영역 파라미터화** → 양수 제약을 자연스럽게 풀어줌
3. **재파라미터화** → 좌표계 자체를 바꿔봄

### 5.4 PK7 모델 판별 — F-test 오용 경고

G&W PK7은 mono/bi/tri-exponential 판별에서 AIC/F-test, 정밀도, 상관성, 잔차, 최소 적절 모델 규칙을 같이 봄. 그중 **가장 자주 잘못 쓰이는 게 F-test**임 — **weighting scheme이 다른 두 모델을 단순 F-test로 비교하면 안 됨.** 두 모델의 likelihood가 서로 다른 측정오차 가정 위에 서 있기 때문임. NDA 제출의 모델 정당화 논리는 결국 이 단순 사실 위에 서 있음 [G&W pp.505–512].

> ⚠️ WRSS와 condition number는 서로 대체 못 함. 하나는 "얼마나 잘 맞았나"를 묻고, 다른 하나는 "그 맞음이 안정적으로 추정되나"를 묻음.

### 5.5 NCA를 선택해야 할 때

G&W PK8은 **initial phase가 거의 안 보이지만 그렇다고 배제할 수도 없을 때 NCA가 제안될 수 있다**고 말함. **2구획 fit을 무조건 강행하라는 세션이 아니라**, 데이터가 phase를 식별해 줄 때만 parametric 2구획 해석을 신뢰하라는 경고임 [G&W p.517].

### 5.6 Parameterization 혼동 쌍

| 비교 기준 | Better WRSS | Better deployable model |
|---|---|---|
| 무엇을 보나 | residual fit 품질 지표 | fit + 안정성 + 해석 가능성 |
| 위치 | 목적함수/잔차 축 | condition number, RSE, correlation, biological plausibility 병렬 |
| 변화 원인 | 측정오차, weighting, residual 크기 | parameterization, 정보 행렬, covariance geometry |
| 혼동 시 결과 | WRSS 최저 parameterization 무조건 채택 | PK8 ODE는 condition number 최저, Takada는 낮은 WRSS에 high condition number |

### 5.7 자기 점검 3 — Socratic Dilemma

**Q.** NDA submission 마감이 1주일 남았음. PK8 데이터로 PopPK 모델 후보가 둘로 좁혀짐.

- **Model A (Takada parameterization):** WRSS 5개 parameterization 중 최저. 단, condition number 3,186, $V_t(t)$ time-dependent 표현이 reviewer에게 익숙하지 않을 가능성 큼.
- **Model B (ODE physiological parameterization):** condition number 29.69로 압도적으로 안정적. WRSS는 Takada보다 약간 높지만 fit 자체는 시각적으로 충분히 양호. $CL, V_1, Cld, V_t$로 reviewer가 즉시 해석 가능.

어느 모델을 채택하고, 그 결정을 reviewer에게 어떻게 방어할 것인가?

**A. 채택: Model B (ODE 생리학적 모델).** 정답은 모델 선택 자체보다 **방어 논리의 구조**에 있음:

1. **WRSS는 fit residual 크기, condition number는 추정 geometry 안정성** — 두 축은 서로 대체 못 함.
2. **실용 모델의 첫째 조건은 재현성** — 다른 시드, 다른 초기치, 다른 공변량 추가에서도 같은 결론. condition number 3,186은 covariance step instability와 covariate inclusion 시 결과 비예측성을 뜻함.
3. **Reviewer Defense 한 줄:** "Takada는 lowest WRSS이지만 (a) covariance geometry가 100배 이상 불안정하고 (b) 시간 의존적 용적 표현은 공변량-용적 관계 해석에 추가 부담을 만듦. ODE 생리학적 모델은 적합이 거의 동등하면서 (a) 정밀도/상관성이 안정적이고 (b) 청소율/용적 좌표계로 일반적 PopPK 보고 관행에 부합함."
4. **적합 차이가 임상적으로 유의미(AUC 차이 >10%)하면** 두 모델 모두를 sensitivity analysis로 보고하고 최종 dosing은 robust 영역에서 도출함.
5. **함정:** "WRSS가 더 낮으니 Takada가 진짜 모델에 가깝다"는 추론은 **weighting scheme이 부적절한 두 모델을 직접 비교하는 실수**일 수 있음. 무가중 RSS와 가중 RSS는 직접 비교 대상이 아님 [G&W pp.508–517; 실무 추론: regulatory defense].

**다음 깊이 질문:** Model B를 채택했는데 reviewer가 "그렇다면 Takada가 보여준 lower WRSS는 어떤 정보를 담고 있나"라고 묻는다면? → **"lower WRSS는 시간 의존적 $V$ 가정이 적합 잔차를 약간 감소시킨다는 신호이지, 그 가정이 기전적으로 검증되었다는 의미는 아님. 기전적 검증 없이는 실용 모델로 채택할 수 없음."** [실무 추론]

분기점 3을 마무리하고 마지막 분기점 4로 넘어감.

---

<!-- SLIDE_START: §6 | title: 분기점 4 — Half-life trap, Multiple dosing -->
<!-- SECTION_CORE: SC-06 -->

## §6 — 분기점 4: Half-Life Trap — Nicardipine & Gentamicin Multiple Dosing

제출 가능한 parameterization을 골랐음. 그래도 끝이 아님. 그 모델에서 나온 **terminal half-life를 dosing 시간 척도로 그대로 써도 되는가** — 이게 마지막 검증임.

> **거장의 시각**
> half-life 숫자 하나를 듣자마자 dosing interval로 번역하면 terminal, effective, plasma, tissue가 한 단어 안에서 뒤섞임. **$f_1/f_2$, input pattern, volume term을 같이 봐야** terminal half-life가 유용한 경우와 위험한 경우가 갈림.

### 6.1 정상상태 접근 방정식 — 진짜 답은 plateau equation

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

이 식의 핵심은 **두 phase가 $C_{ss}$로 접근하는 정도를 $f_1/f_2$로 가중합한 것**임. 따라서 **half-life 하나가 아니라 phase별 AUC 기여도가 plateau 해석을 결정**함.

> 💡 **메타포:** 두 개의 수도꼭지가 동시에 차오르는 욕조를 떠올려 보자. **빠른 수도꼭지의 물량이 대부분이면** 마지막 한 방울이 늦더라도 욕조 수위는 이미 거의 올라와 있음.

- $f_2 > 0.8$이면 terminal half-life로 plateau 도달을 대체로 설명할 수 있음.
- **$f_2$가 작으면 terminal half-life가 길어도 plasma plateau는 훨씬 빨리 접근함** [R&T pp.631–633].

> 🔑 **Half-life 분류 규칙.** half-life라는 말을 들으면 계산에 들어가기 전에 **"terminal? effective? plasma? tissue?"** 부터 물어야 함.

### 6.2 Nicardipine 사례 — "Terminal 길다 = loading 필요"의 함정

**Nicardipine**(디하이드로피리딘 계열 calcium channel blocker로, IV로 쓰면 빠르게 혈압을 떨어뜨리는 약물):
- 말단 반감기 약 **12 hr** (길어 보임)
- 그런데 plasma 농도는 **1 hr 안에 약 50% $C_{ss}$**, 약 15 hr에 90% $C_{ss}$ 도달

말단 반감기만 보고 loading dose 필요성을 판단하면 **초기 과량 투여 위험**이 생김. 실제로는 $f_1$이 커서 $C_{ss}$ 접근이 빠른 약물임 [R&T p.631].

### 6.3 Gentamicin 사례 — Terminal Accumulation vs Plasma Fluctuation

말단 반감기가 **87 hr**여도 plasma 치료적 거동은 **초기상 약 4 hr**가 좌우함. 말단항 기반 축적 지수(accumulation index)는 16배가 될 수 있지만, 이건 plasma 최고/최저 농도 축적과 같은 게 아니라 **서서히 평형에 도달하는 조직의 축적**임.

→ **terminal accumulation과 plasma fluctuation은 같은 시간 척도가 아님** [R&T pp.635–641].

| 상황 | 파라미터 변화 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| Nicardipine-style | terminal $t_{1/2}\approx 12$ hr, 1 hr에 50% $C_{ss}$ | → | loading dose 필요성 과대판단 위험 | plateau equation으로 effective time scale 확인 |
| Gentamicin-like | terminal $t_{1/2}=87$ hr, 초기상 약 4 hr | → | terminal accumulation과 plasma fluctuation 혼동 | plasma와 tissue accumulation 분리 |
| $f_2 > 0.8$ | terminal contribution 큼 | → | terminal half-life가 time-course 대표 가능 | 그래도 phase/조직 구분은 명시 |

### 6.4 조직 vs Plasma — 두 시간 척도가 분리되는 자리

plasma가 정상상태에 빨리 들어가도 **서서히 평형에 도달하는 조직은 훨씬 늦게 들어옴**. 반응 부위(response site)가 말초·조직 쪽이면 plasma 반감기만으로 작용 개시와 지속을 해석하면 안 됨 [R&T pp.633–634].

### 6.5 다회투여 volume 규칙 — 분기점 2와 만나는 자리

- fluctuation이 작고 true steady state에 가까울 때: **$V_{ss}$**가 amount estimate에 유용함.
- interval 말기 distribution equilibrium에 가까울 때: **$V_\beta$**도 approximation으로 쓸 수 있음.
- **Gentamicin-like처럼 interval 전체가 distribution disequilibrium이면 어느 volume도 단순 amount calculator가 되지 않음** [R&T pp.638–639].

### 6.6 완화된 경고 — Terminal half-life가 항상 틀린 건 아님

"terminal half-life는 항상 틀린다"는 게 아님. R&T는 **많은 약물에서 $f_2>0.8$이면 terminal phase가 plateau/time-course를 잘 설명한다**고 말함. 핵심은 "terminal인지 effective인지, plasma인지 tissue인지, $f_2$가 얼마인지"를 묻는 습관임 [R&T pp.631–641].

### 6.7 회의실 실무 룰

> 💼 **실무 인사이트.** 회의에서 누가 "이 약물 half-life가 X시간"이라고 말하면 바로 되물어야 함 — **"terminal인가요? effective인가요? plasma인가요? tissue인가요?"** 이 네 글자가 달라지면 multiple-dosing simulation 결과가 통째로 달라짐.

### 6.8 Half-life 혼동 쌍

| 비교 기준 | Terminal half-life | Effective/clinical half-life |
|---|---|---|
| 단위 | 시간 | 임상 농도 접근 시간 척도 |
| 수식 위치 | $t_{1/2,\beta}=0.693/\beta$ | $C(t)/C_{ss}=f_1(1-e^{-\alpha t})+f_2(1-e^{-\beta t})$ |
| 변화 원인 | terminal slope, 느린 재분포 | $f_1/f_2$, input pattern, plasma/tissue site |
| 혼동 시 결과 | 논문 half-life 12 hr를 plateau에도 그대로 적용 | Nicardipine: terminal 12 hr인데 1 hr에 50% $C_{ss}$ → loading dose 권하면 과량 투여 |

> ⚡ **메타포 — 마지막 페이지 vs 전체 이야기.** Terminal $t_{1/2}$은 log-concentration 곡선의 마지막 직선 구간에서만 읽히는 **마지막 페이지** — 재분포가 이미 끝나고 제거만 남은 단순화된 단계임. 그 앞에는 α phase의 빠른 분포와 초기 제거가 있었음. **Terminal $t_{1/2}$만으로 투여 간격이나 체내 잔류를 판단하면 앞 페이지의 높은 초기 농도와 분포 지연 효과를 놓침.** Effective $t_{1/2}$은 $f_1/f_2$-가중 plateau equation으로 읽어야 비로소 보이는 "전체 이야기"의 시간 척도임.

### 6.9 자기 점검 4

**Q.** Nicardipine처럼 말단 반감기가 12 hr인데 1 hr에 50% $C_{ss}$에 도달하는 사례에서, 말단 반감기만으로 loading dose를 권하면 왜 위험한가?

**A.** plateau 접근이 terminal term만으로 결정되지 않고 **$f_1/f_2$ 가중합으로 결정**되기 때문임. plasma는 이미 빠르게 올라가고 있는데 terminal half-life만 보면 "너무 늦게 도달한다"고 오판해서 **과도한 loading을 권하게 됨** [R&T pp.631–633].

$$
\underbrace{\text{plateau 접근}}_{C(t)/C_{ss}}
\neq
\underbrace{\text{말단반감기 단독}}_{\beta\text{만 보는 해석}}
$$

> 📖 **R&T p.631, Fig.19-10:** 긴 말단 반감기에도 불구하고 plateau에 빠르게 접근하는 Nicardipine 사례. → 반감기 하나만 보고 투여를 판단하지 말라는 경고를 한 장으로 받쳐 줌.

> 📖 **R&T p.636, Fig.19-14:** Gentamicin의 plasma/tissue 다회투여 축적을 한 그림에. → **말단항 축적과 치료적 plasma 변동을 분리해서** 봐야 한다는 메시지를 시각적으로 못 박아 줌.

4개 분기점을 다 통과했음. 이제 확장 framework로 들어감.

---

<!-- SLIDE_START: §7 | title: 확장 framework — 3구획, 1/k optimal, non-stationary -->
<!-- SECTION_CORE: SC-07 -->

## §7 — 확장 Framework: 3구획 진단, 1/k Optimal Sampling, Non-stationary 경계

4개 분기점 너머에 있는 세 개의 정밀화 framework임. 본문 동선이 자연스럽게 연결되는 곳에 배치.

### 7.1 3구획 모델로 넘어가야 하는 진단 신호

2구획 fit을 끝내고 잔차를 봤는데 **terminal phase가 또 휘면** 3구획 가능성을 의심함. G&W p.73 Fig.2.52는 IV bolus 후 **세 개의 지수항(α, β, γ phase)**으로 감소하는 plasma curve를 보여주고, Fig.2.53은 그에 대응하는 6-parameter 3구획 모델($V_c, V_{t1}, V_{t2}, Cld_1, Cld_2, Cl$)을 정의함 [G&W p.73].

$$
\underbrace{C(t)}_{\text{혈장농도}}
=
\overbrace{\underbrace{A}_{\text{α절편}}e^{-\alpha t}}^{\text{α상}}
+
\overbrace{\underbrace{B}_{\text{β절편}}e^{-\beta t}}^{\text{β상(shallow tissue 회귀)}}
+
\overbrace{\underbrace{C_\gamma}_{\text{γ절편}}e^{-\gamma t}}^{\text{γ상(deep tissue 회귀)}}
$$

핵심은 두 말초구획의 기전적 분리임:
- **Shallow compartment** — 빠르게 평형에 도달하는 조직 (예: renal, hepatic tissue)
- **Deep compartment** — 느리게 평형에 도달하는 조직 (예: adipose tissue, bone marrow)

| 진단 신호 | 어떻게 보이나 | 의심할 것 |
|---|---|---|
| 2구획 fit 잔차의 terminal 영역에 S자 또는 다시 휘는 패턴 | CWRES vs TIME plot이 말단에서 양의 systematic bias | 3구획 또는 deep-tissue 구획 |
| Terminal slope를 한참 늦게까지 잡아도 직선이 안 됨 | semilog plot이 두 번 꺾임 | shallow + deep 분리 |
| 친유성 약물(예: thiopental, amiodarone) | 지방·골수 분배가 큼 | adipose deep compartment |
| 단클론 항체(mAb)와 일부 펩타이드 | FcRn-mediated recycling, slow lymphatic | deep compartment 또는 TMDD |

> 💡 **3구획 직관:** 두 개의 말초 창고가 있고 그 둘이 회귀 속도가 다름. 빠른 창고(shallow)는 신장·간 같은 잘 관류되는 조직, 느린 창고(deep)는 지방·골수처럼 관류는 적은데 분배가 큰 조직. 이중지수가 안 맞으면 창고 개수를 늘려야 하는지(모델 차수 ↑), 아니면 다른 비선형성인지를 먼저 분리해야 함 [G&W p.73; 실무 추론].

> ⚠️ **단, 데이터가 phase를 식별해 줄 때만 3구획으로 감.** PK8의 교훈("initial phase가 안 보이면 NCA가 더 안전")이 그대로 확장됨 [G&W pp.512, 517].

### 7.2 Optimal Sampling Design — D-optimality의 1/k 원칙

sparse design에서 어디에 표본을 두면 $V_2/Q/\alpha$ 같은 분포상 파라미터가 식별 가능할까? G&W p.512가 **답을 한 줄로 줌:**

> "place a sample at 1/(rate constant). According to experimental design theory, 1/(rate constant) is the optimal time point with respect to that particular parameter" [G&W p.512].

풀어 말하면 — 어떤 파라미터의 식별성을 최대로 끌어올리려면 **그 파라미터에 대한 농도의 국소 민감도(local sensitivity)가 가장 큰 시점**에 표본을 두라는 것. 1차 지수 감소 시스템에서 그 시점이 정확히 $1/k$임.

$$
\underbrace{t_{\text{optimal}}}_{\text{최적 sampling}}
=
\frac{\overbrace{1}^{\text{1 time-unit}}}{\underbrace{k_{\text{parameter}}}_{\text{관심 rate constant}}},
\qquad
\text{e.g., }
\underbrace{t_\alpha^*}_{\text{α상 최적}}\approx\frac{1}{\alpha},\quad
\underbrace{t_\beta^*}_{\text{β상 최적}}\approx\frac{1}{\beta},\quad
\underbrace{t_{k_{21}}^*}_{V_2\text{ 식별}}\approx\frac{1}{k_{21}}
$$

| 식별 대상 | 최적 sampling 시점 | 실무 의미 |
|---|---|---|
| α phase($V_1$, $k_{12}$) | $t\approx 1/\alpha$ (분포상 중간) | IV bolus 5–30 min 영역 |
| β phase($CL$, terminal slope) | $t\approx 1/\beta$ (말단상 중간) | terminal half-life 1배 시점 근처 |
| $V_2/Q$ 식별 | α와 β 사이 전이 구간 | 잘못 잡으면 Phantom V2 |
| AUC 추정 | 전 구간 균형 + tail 1점 | NCA quality check |

> 💼 **실무 인사이트.** D-optimality 정식 알고리즘(PFIM, PopED 같은 toolkit)을 매번 돌릴 필요는 없음. **1/k 원칙**만 머리에 두면 sparse design에서 "여기 표본 하나 더 있어야 함"을 정량적으로 방어할 수 있음. 특히 PopPK protocol design에서 분포상 표본을 빼자는 압력이 있을 때, "1/α 근처 한 점이 없으면 $V_2$가 식별 불가능하고, 그러면 covariate 모델에서 신기능을 $V_2$에 붙일 수가 없음"이라는 정량 방어가 가능함.

### 7.3 ⭐ 2구획 다중-파라미터의 Two-stage Cluster Sampling

위의 1/k 원칙은 **단일 파라미터에 대한 local D-optimum**임. G&W p.512가 정확히 그렇게 적음:

> "1/(rate constant) is the optimal time point **with respect to that particular parameter**" [G&W p.512, 강조 추가].

풀어 말하면 — 1/k 원칙은 본질적으로 **single-compartment 또는 단일 시간상수 가정 하의 D-optimal design**임. 그런데 2구획 시스템은 두 개의 고유값 $\lambda_1=\alpha$와 $\lambda_2=\beta$를 **동시에** 식별해야 하니까, single-compartment의 1/k 원칙을 그대로 가져오면 한쪽 phase가 비어 식별성이 무너짐.

PopPK 설계의 표준 관행은 **two-stage cluster sampling** — $1/\lambda_1$ 근방과 $1/\lambda_2$ 근방에 각각 **표본을 군집(cluster)으로 배치**하는 방식임.

$$
\underbrace{\text{2-comp sampling design}}_{\text{두 phase 동시 식별}}
=
\overbrace{\underbrace{\{t : t\approx 1/\lambda_1=1/\alpha\}}_{\text{α phase cluster}}}^{V_1,\,k_{12},\,k_{21}\text{ 식별}}
\;\cup\;
\overbrace{\underbrace{\{t : t\approx 1/\lambda_2=1/\beta\}}_{\text{β phase cluster}}}^{CL,\,\beta,\,AUC\text{ tail 식별}}
$$

| 단계 | 시점 cluster | 정보 식별 | 표본 권장 |
|---|---|---|---|
| Stage 1 — α cluster | $t\approx 1/\alpha$ 주변 (분포상 중간) | $V_1$, $k_{12}$, $k_{21}$ (재분포 동력학) | 3–5 표본을 가까운 시점에 (IV bolus 5–30 min) |
| Stage 2 — β cluster | $t\approx 1/\beta$ 주변 (말단상 중간) | $CL$, $\beta$, $AUC$ tail | 3–5 표본을 1–3 terminal half-life 영역 |
| Bridge | α와 β cluster 사이 전이 영역 | $Q/V_2$ 식별 보강 | 1–2 표본을 $1/\alpha$와 $1/\beta$ 사이 |

$$
\underbrace{n_\alpha}_{\text{α cluster 표본 수}}
+
\underbrace{n_{\text{bridge}}}_{\text{전이 표본 수}}
+
\underbrace{n_\beta}_{\text{β cluster 표본 수}}
\;\overset{\text{D-criterion}}{=}\;
\arg\max\overbrace{\det\bigl(\underbrace{\boldsymbol{M}(\boldsymbol{\theta})}_{\text{Fisher 정보행렬}}\bigr)}^{\text{정보량 최대화}}
$$

> 💡 **단일 cluster의 함정.** β phase cluster만 있으면 $CL$과 terminal $\beta$는 잘 식별되지만 $V_1$, $k_{12}$, $k_{21}$이 **Phantom V2** 위험에 빠짐. α phase cluster만 있으면 분포상 파라미터는 잡히지만 $CL$ 정밀도가 무너짐. **두 cluster가 모두 있어야 2구획 좌표계가 완전히 식별 가능함** — 이게 single-compartment 1/k 원칙과 2-compartment 설계가 갈라지는 정확한 자리임 [실무 추론: 1/k 원칙의 multi-parameter 확장].

> ⚠️ **두 cluster의 비율도 결정해야 함.** "α cluster에 몇 점, β cluster에 몇 점?"은 $f_1/f_2$ AUC 분율과 covariate model 우선순위에 따라 달라짐. covariate를 $CL$에 붙이는 게 1차 목표라면 β cluster를 더 두텁게, **distribution disequilibrium이 임상 핵심인 약물**(예: gentamicin)이면 **α cluster를 더 두텁게**. 비율은 D-criterion 또는 ED-optimality로 정량 결정하는 게 표준 마무리임.

> 💼 **PK7과의 연결.** PK7에서 "관측치를 10–20–30%씩 줄여 가며 정밀도와 상관성을 보라"는 G&W의 권유는 사실 이 two-stage cluster 원리의 **inverse exercise**임 — 어느 cluster의 어느 표본이 정보 행렬에 가장 큰 기여를 하는지 확인하는 작업임. PK7 reduced-design exercise를 **두 cluster의 표본을 따로 빼 가며** 해 보면, single-compartment 1/k 원칙과 multi-compartment two-stage 원리가 같은 데이터에서 어떻게 다른 결론을 내는지 직접 보임.

### 7.4 Non-stationary Kinetics — 시간 의존적 V의 경계

분기점 3에서 Takada model이 $V(t)$를 시간 의존적으로 두는 표기였음. G&W p.513은 이 표기의 기원과 한계를 같이 적음 — Takada-Asada(1981)와 Colburn(1983)의 V(t)는 **2구획 시스템에서 시간에 따라 분포가 확장되는 현상을 한 변수에 흡수한 수학적 reparameterization**이지, 진짜로 분포 공간이 시간에 따라 변한다는 기전적 주장은 아님 [G&W p.513].

$$
\underbrace{V(t)}_{\text{시간의존 겉보기 V}}
:\overbrace{\underbrace{V_1}_{t=0^+}}^{\text{초기 중앙}}
\;\xrightarrow{\text{재분포 진행}}\;
\overbrace{\underbrace{V_{ss}}_{\text{진짜 평형}}}^{\text{distribution eq.}}
\;\xrightarrow{\text{terminal phase 안}}\;
\overbrace{\underbrace{V_z\equiv V_\beta}_{\text{말단 V}}}^{\text{Vβ 부풀림 흡수}}
$$

**진짜 non-stationary kinetics**는 이것과 다름 — 시간에 따라 시스템 자체의 파라미터($V$, $CL$, $Q$, $k$)가 변하는 경우임.

| 분류 | 의미 | 처리 |
|---|---|---|
| **표기상 시간 의존성** (Takada/Colburn V(t)) | 2구획의 정상적 재분포를 한 변수로 흡수한 reparameterization. 시스템 파라미터는 시간 불변 | 표준 2구획 fit과 동등하지만 covariance geometry가 나빠질 수 있음 |
| **기전적 시간 의존성** (true non-stationary) | input rate가 시간에 따라 변하는 depot 제형, 또는 시스템 파라미터가 시간 함수 | 별도 input function 또는 time-varying model |

**임상에서 진짜 non-stationary가 생기는 자리.** Depot 제형(예: leuprolide microsphere, medroxyprogesterone acetate(DMPA) depot)에서는 약물 방출 속도 $k_a(t)$ 자체가 시간 의존적임. 이런 경우는 2구획 disposition + 시간 의존적 absorption input으로 구조를 분리해야 하지, $V(t)$로 흡수하면 안 됨 — 두 시간 의존성이 한 변수에 합쳐지면 식별 불가능해짐 [실무 확장; G&W p.513].

> 💡 **경계 정리:** $V_1 \to V_{ss} \to V_\beta$로 시간에 따라 "겉보기 V가 확장"되는 현상은 **2구획 disposition의 정상적 모습**이지 진짜 시스템 변화가 아님. depot 제형이나 enzyme induction/inhibition으로 **시스템 파라미터 자체가 시간에 따라 변할 때만 진짜 non-stationary**임. 두 개를 같은 단어로 부르면 모델 구조 결정이 흔들림.

> ⚠️ PK8 Takada 모델이 reviewer에게 익숙하지 않다는 분기점 3의 문장과 직접 연결됨. Time-dependent V 표기는 covariate 해석을 어렵게 만듦 — "신기능이 어떤 시점의 V에 붙는가?"를 답하기가 어려워짐. 그래서 **진짜 non-stationary가 아닌 경우라면 ODE 생리학적 좌표계가 covariate 모델링에 훨씬 안전함** [G&W p.513; 분기점 3 PK8 ODE model의 condition number 최저 이유].

---

<!-- SLIDE_START: §8 | title: 실패 모드와 전문가 해석 지점 -->
<!-- SECTION_CORE: SC-08 -->

## §8 — 실패 모드(Failure Modes)와 전문가 해석 지점(Professional Moat)

### 8.1 실패 모드 — 분기점별 정리

| 실패 모드 | 분기점 | 어떻게 알아보나 | 예방 규칙 |
|---|---|---|---|
| **말단상 전용 CL 오류** | 1 | 초기 표본 누락, 1구획 CL 과대 추정 | 분포상 표본 확보 + 이중지수 가능성 점검 |
| **Vβ-as-Vss error** | 2 | $V_\beta/V_{ss}$가 큰데 loading/amount 계산에 $V_\beta$ 사용 | amount·SS에는 $V_{ss}$ 우선, terminal에만 $V_\beta$ |
| **Phantom V2** | 2 / 7.3 | sparse design, $V_2$ RSE >100%, ETA(V2) shrinkage >80% | "작은 $V_2$" 결론 전 distribution-phase identifiability 확인 |
| **Pseudo-Stable V across renal function** | 2 / 4 | gentamicin-like에서 $V_\beta$ vs CrCl plot이 평탄해 보이는데, multiple-dose plasma trough VPC가 신부전군 underprediction. 신부전 시 $CL$과 β가 같이 떨어지면 $V_\beta=CL/\beta$의 비율이 안정해 보이는 착시 | covariate를 $V_\beta$가 아니라 $V_{ss}/V_1$에 붙이고, plasma trough VPC와 tissue accumulation 예측을 분리 검증 [실무 추론] |
| **Macro Drift** | 3 | $A/B$ 사이 상관이 높고 covariance가 불안정 | production에는 physiological parameterization 우선 |
| **초기 추정치 함정** | 3 | condition number 폭증, 초기치만 바꿔도 결과 급변 | 초기 추정치 → 로그 영역 → 재파라미터화 순서 |
| **WRSS 단독 선택** | 3 | 최저 WRSS 모델이 높은 condition number | 잔차·정밀도·condition number·생물학적 타당성 병행 |
| **F-test 오용** | 3 | weighting scheme이 다른 모델을 단순 F-test로 비교 | PK7 규칙: 잔차·정밀도·상관성·최소 적절 모델 함께 적용 |
| **Half-life 단어 혼용** | 4 | "half-life 87 hr이니 plasma 16배 축적" 같은 단언 | "terminal? effective? plasma? tissue?" 되묻기 |

### 8.2 전문가 해석 지점 — 30년차 모델러가 1분 안에 보는 것

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| Semilog 꺾임점과 말단 직선성 | $\alpha/\beta$ 구조 | → | 2구획·3구획 가능성 판단 | terminal curvature 확인 |
| $f_2$가 작거나 큼 | $f_2$ | → | terminal 반감기가 임상 시간 척도 대표 가능 여부 | plateau equation과 함께 해석 |
| $V_\beta/V_{ss}$ 비율 상승 | $V_\beta$, $V_{ss}$ | → | terminal volume 오용 위험 | loading·amount에는 $V_{ss}$ 우선 |
| WRSS 낮지만 condition number/RSE 나쁨 | condition number, RSE | → | production model 불안정 | 모델 보류 또는 좌표계 재검토 |
| CWRES vs TIME이 초기 양 또는 S자 | CWRES | → | 구조적 오설정 또는 분포상 누락 | sampling·구획 수 재점검 |
| η-shrinkage 높음 | η-shrinkage | → | covariate effect 해석 가능성 낮음 | covariate 결론 보수화 |
| forward inclusion에서 공변량 추가 | $CL, Q, V_{ss}, V_\beta$, condition number | → | covariate를 어디에 붙일지 결정 | 4개 분기점 동시 점검 |

### 8.3 후속 세션 연결

| 후속 세션 | 이 세션에서 열리는 개념 | 이 세션 없으면 실패하는 것 |
|---|---|---|
| NONMEM ADVAN3/4/11/12 | $CL,V_1,Q,V_2$ 좌표계와 macro/micro 연결 | ADVAN parameter를 curve slope와 분리해 외우게 됨 |
| Sparse sampling design | distribution phase sample 없으면 $V_2$, $Q$, α 식별 약화 | Phantom V2를 실제 작은 $V_2$로 오판 |
| Covariate model building | covariate는 보통 $CL,V,Q$ physiological parameter에 붙음 | covariate를 β나 terminal half-life에 직접 붙여 해석 불능 |
| Multiple-dosing simulation | terminal half-life 하나가 아니라 $f_1/f_2$, input duration, $V_{ss}/V_\beta$ 같이 봄 | plateau와 tissue accumulation을 같은 시간 척도로 처리 |
| 3구획 모델 | 이중지수 잔차에서 다시 곡선이 휘면 삼중지수 또는 deep tissue 의심 | 2구획 미설명 terminal curvature를 노이즈로 처리 |

---

<!-- SLIDE_START: §9 | title: 최소 실무 알고리즘과 자기 테스트 -->
<!-- SECTION_CORE: SC-09 -->

## §9 — 최소 실무 알고리즘 & 자기 테스트

### 9.1 9단계 실무 알고리즘

```text
1. Plot semilog C-time curve.
2. Early sampling이 distribution phase를 잡았는지 확인.
3. Bi-exponential 가능성이 있으면 A, α, B, β를 rough estimate.
4. AUC, f1, f2, V1, Vss, Vβ를 계산.
5. Vβ/Vss와 f2를 보고 terminal half-life 해석 가능성을 평가.
6. Physiological parameterization으로 CL, Q/Cld, V1, V2를 설정.
7. Fit 후 residual, RSE, correlation, condition number를 함께 확인.
8. Sparse design 또는 high shrinkage이면 V2/Q/covariate 해석을 보류.
9. Multiple dosing은 terminal half-life 하나가 아니라 f1/f2-weighted plateau equation으로 점검.
```

### 9.2 자기 테스트 — 통합 9문항

**Q1 (분기점 1, 잔차법 재구성).** G&W Fig.2.43에서 말단상을 외삽해 $B=28$, $\beta=\ln(28/10)/450$을 얻음. 초기 관측치에서 무엇을 빼야 α 상이 나오나?

> **A.** 각 초기 관측치 $C_{obs}(t_i)$에서 $Be^{-\beta t_i}$를 뺌. 잔차를 반로그 도표에 다시 놓고 기울기/절편을 구하면 α와 $A$ [G&W p.60].

**Q2 (분기점 1, Aspirin CL 방향).** Aspirin 650 mg IV bolus, 말단 전용 1구획 = 0.98 L/min, 이중지수 = 683 mL/min. 말단 전용은 과소? 과대?

> **A.** **과대(약 44%).** 유지 용량 계산이 그대로 부풀음 [R&T pp.615–620].

**Q3 (분기점 2, Volume 비율).** Aspirin과 gentamicin 중 $V_\beta/V_{ss}$ 비율이 더 큰 약물은? 중요한 이유?

> **A.** **Gentamicin.** Aspirin $\approx 1.3$, gentamicin $\approx 6.2$. 큰 비율은 **말단 기울기에서 나온 용적을 정상상태 체내량 용적처럼 쓰면 안 된다**는 경고 [R&T pp.629–641].

**Q4 (분기점 2, 비식별성).** 같은 이중지수 plasma 곡선을 중앙 제거, 말초 제거, 양 구획 제거 모델이 모두 설명함. plasma data만으로 무엇을 결론낼 수 없나?

> **A.** **제거 부위(elimination site)를 식별할 수 없음.** 중앙구획 단독 제거는 보통 생리학적 타당성으로 선택되는 실무 가정이지, plasma 곡선만으로 증명되는 게 아님 [G&W p.65; R&T pp.618–619].

**Q5 (분기점 4, Half-life 함정).** Nicardipine처럼 말단 반감기 12 hr인데 1 hr에 50% $C_{ss}$ 도달하는 사례에서, 말단 반감기만으로 loading을 권하면 왜 위험한가?

> **A.** plateau 접근이 terminal term만으로 결정되지 않고 **$f_1/f_2$ 가중합**으로 결정되기 때문임. plasma가 이미 빠르게 올라가는데 terminal만 보면 "너무 늦는다"고 오판해서 **과도한 loading**을 권함 [R&T pp.631–633].

**Q6 (분기점 3, PK8 모델 선택).** PK8에서 Takada는 WRSS 최저, ODE는 condition number 최저. 어느 하나만 보고 결정하면 안 되는 이유?

> **A.** WRSS는 fit residual 크기, condition number는 parameter estimation geometry. **둘 중 하나만 좋다고 deployable model이 되는 게 아님.** 같은 데이터, 비슷한 fit이어도 좌표계가 condition number를 크게 바꿈 [G&W pp.513–517].

**Q7 (분기점 7.3, Phantom V2).** 첫 표본이 분포상 이후에만 있는 sparse design에서 ADVAN3 TRANS4 적합 후 $V_2$ RSE >100%, ETA(V2) shrinkage >80%, 초기 CWRES 양의 경향. 가장 먼저 의심할 것은?

> **A.** "약물의 $V_2$가 진짜 작다"가 아니라 **distribution phase가 data에 없어서 $V_2$가 식별되지 않는 Phantom V2** 상황 [실무 확장].

**Q8 (분기점 4, 회의실 실무).** 누가 "half-life가 87 hr이니까 8시간 간격 투여하면 plasma가 16배 축적된다"고 함. 무엇을 되물어야 하나?

> **A.** **terminal half-life인지 effective/plasma half-life인지, $f_2$는 얼마인지, 축적이 plasma 구획인지 서서히 평형에 도달하는 조직인지** 물어야 함. Gentamicin-like에서는 terminal accumulation과 plasma fluctuation 분리 필수 [R&T pp.635–641].

**Q9 (Socratic Dilemma — PK8 모델 채택).** §5.7에서 다룬 NDA 마감 1주 남은 PK8 의사결정. Model B(ODE) 채택의 reviewer defense 논리는?

> **A.** §5.7의 5단계 논리: (1) WRSS ≠ condition number, (2) 재현성이 1순위, (3) reviewer-friendly 좌표계, (4) sensitivity analysis 병행, (5) F-test 오용 함정 [G&W pp.508–517].

> 통과 기준: 9개 질문 모두 답할 수 있으면 2구획 모델을 "공식"이 아니라 **모델 선택·volume 해석·dosing simulation·규제 방어 논리의 사고 도구**로 쓸 준비가 된 것임.

---

<!-- SLIDE_START: §10 | title: 한 줄 회수와 다음 세션 연결 -->
<!-- SECTION_CORE: SC-10 -->

## §10 — 한 줄 회수와 다음 세션 연결

이 세션의 본질을 다시 한 줄로:

> **하나의 IV bolus plasma 곡선은 4개의 의사결정 분기점을 만들고, 각 분기점에서 잘못 가면 임상에서 정량화 가능한 손해가 나옴.**

4개 분기점 회수:

| 분기점 | 핵심 함정 | 잘못 가면 | 옳게 가는 도구 |
|---|---|---|---|
| 1. Sampling adequacy | early sampling 누락 | CL 44% 부풀음 (Aspirin) | $f_2$ 점검, 이중지수 가능성 확인 |
| 2. Volume choice ⚡ | "terminal 길다 = 분포 넓다" 직역 | loading dose 6배 (Gentamicin) | $V_1/V_{ss}/V_\beta$ 분리 + $K_{p,\text{app}}$ 기전 |
| 3. Parameterization | lowest WRSS만 추종 | condition number 100배 (PK8) | WRSS + condition number + RSE 병행 |
| 4. Half-life interpretation | terminal half-life 단독 사용 | multiple dosing 통째로 (Nicardipine, GM) | plateau equation + $f_1/f_2$ 가중 |

**최종 회수:** 2구획 모델의 mastery는 $C=Ae^{-\alpha t}+Be^{-\beta t}$를 외우는 게 아님. 좋은 모델러는 이 식을 보는 순간 **sampling adequacy, CL bias 방향, volume choice, condition number risk, half-life 오용 가능성**을 동시에 읽음. 그리고 본 세션의 확장 framework(3구획 진단 신호, 1/k optimal sampling, two-stage cluster, non-stationary 경계)까지 갖춰지면, **"2구획으로 충분한가, 더 가야 하는가"**를 데이터 앞에서 빠르게 분리할 수 있음.

**다음 세션 연결:** NONMEM ADVAN3/4/11/12로 들어가면 이 세션의 좌표계가 그대로 ADVAN parameter로 옮겨가고, sparse sampling design에서는 7.3의 two-stage cluster가 protocol 결정 도구가 되며, covariate model building에서는 4개 분기점이 동시에 작동함. 이 세션을 한 줄로 꿴 다음에야 후속 세션이 평면이 아닌 입체로 보이기 시작함.

---

<!-- 재구성 노트 (v4.0 보강본_final → Remastered)
- 원본의 모든 콘텐츠, 수식 underbrace/overbrace, 출처 anchor [G&W p.XX]/[R&T p.XX], 사례(Aspirin/Gentamicin/Nicardipine/Thiopental/PK7/PK8/Compound X), 보강본 5건(M1 단위 명시, M3 Kp_app 기전, E-1 3구획, E-2 1/k, E-2-bis cluster sampling, E-3 non-stationary)을 모두 보존.
- 동선 재구성: M1~M5 평면 카드 구조를 "4개 의사결정 분기점" 동선으로 재배치. 분기점 1(sampling/Aspirin), 분기점 2(volume/Gentamicin), 분기점 3(parameterization/PK8), 분기점 4(half-life/Nicardipine+GM). 각 분기점에 원본 카드 콘텐츠를 자연스럽게 녹여 넣음.
- 혼동쌍 5개: 원본은 §5에 몰아넣었으나 재구성은 각 분기점 끝에 배치 (2.4 bi-exp/two elim, 3.6 macro/physio, 4.9 V1/Vss/Vβ, 5.6 WRSS/deployable, 6.8 terminal/effective).
- 자기 테스트 9문항: 원본 §7의 Q1~Q9를 분기점 동선에 맞춰 재라벨링하면서 동일 문제 보존 (Q1→Q1, Q2→Q2, Q3→Q3, Q4→Q4, Q5→Q5, Q6→Q6, Q7→Q7, Q8→Q8, Q9→Q9 Socratic Dilemma).
- 확장 framework: §8.E-1/E-2/E-2-bis/E-3 전체를 §7에 한 흐름으로 배치. 7.2의 1/k 원칙과 7.3의 cluster sampling이 자연스럽게 이어지도록 단락 순서 조정.
- 음슴체 적용: "~함/~것임/~음/~임" 일관 사용. 기존 "~예요/~입니다" 어조는 모두 변환.
- SLIDE_START 마커 재배치: §0~§10에 SC-00 ~ SC-10으로 새 카드 구조 부여.
- v4.0 보강본_final의 모든 수식 블록(27개) 보존하면서 신규 한 줄 회수 요약/도미노 다이어그램만 본문 흐름에 추가.
- "한 바느질" 효과: §0의 4개 분기점 미리보기 → 각 §에서 동일 분기점을 도구와 함께 깊이 다룸 → §10에서 4개 분기점 한 표로 회수.
-->

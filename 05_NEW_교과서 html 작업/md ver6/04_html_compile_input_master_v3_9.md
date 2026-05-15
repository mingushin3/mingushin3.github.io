# 세션 04 — 청소율(Clearance): 신·간·IVIVE·대사체 — $CL_R$, $CL_H$, well-stirred, parent-metabolite — v3.9

## PART A — 학습자용 완성 핸드아웃(Learner-Facing Complete Handout)

> **임상 장면**  
> 간 혈류 $Q_H=81\ \mathrm{L/h}$인 성인에서 plasma $CL=60\ \mathrm{L/h}$만 보고 "중등도 이상 hepatic extraction"이라고 판단했다고 가정합시다 [R&T p.125]. 그런데 $C/C_b=0.5$이면 blood 기준 $CL_b$는 30 L/h가 되고, $E_H$는 0.37로 내려갑니다. **이 한 번의 기준 선택 오류가 DDI 해석, 간장애 라벨, PBPK 입력값 전체를 바꿉니다.**

<!-- SLIDE_START: §1 | title: §1 이 장이 중요한 이유(Why This Chapter Matters) -->
<!-- SECTION_CORE: SC-01 -->

## §1 이 장이 중요한 이유(Why This Chapter Matters)

### 레이어 개념 지도

```text
레이어 1 — 무엇인가
  CL / CL_R / CL_H / CL_b / f_e / f_u / f_{ub} / f_m / CL(m)
        ↓
레이어 2 — 어떻게 계산되는가
  Rate = CL·C → 장기별 CL 분해 → well-stirred → ρ/extended clearance → AUC(m)/AUC
        ↓
레이어 3 — 언제, 왜 중요한가
  신장애·간장애·DDI·first-pass·active metabolite·NONMEM covariate 위치·label defense
```

### 지식 그래프 위치

```text
[선행 세션: 선형 1구획 PK·AUC·mass balance]
      → [이 세션: clearance의 생리학적 분해]
      → [후속 세션: PBPK·PopPK covariate·parent–metabolite joint model·impairment label]
```

🧭 **읽는 순서:**  
카드 1 (M1): 왜 $t_{1/2}$가 원인이 아니라 $CL$과 $V$의 결과인가?  
카드 2 (M2): total $CL$ 중 신장 경로만 어떻게 떼어내는가?  
카드 3 (M3): 같은 소변 데이터에서 왜 ARE와 rate plot이 다른 약점을 보이는가?  
카드 4 (M4): 간 $CL$은 $Q_H$와 $f_{ub}CL_{int}$ 중 무엇에 막히는가?  
카드 5 (M5): 단백결합 변화는 왜 IV/oral·high/low extraction에 따라 뒤집히는가?  
카드 6 (M6): IVIVE 실패는 모델식 때문인가, 입력 데이터 압축 때문인가?  
카드 7 (M7): plasma와 urine을 왜 동시에 fitting해야 하는가?  
카드 8 (M8): plasma $CL$을 왜 blood $CL_b$로 바꿔야 하는가?  
카드 9 (M9): $CL_{int}$가 충분해도 왜 hepatocyte 접근성이 병목이 되는가?  
카드 10 (M10): transporter–enzyme architecture는 well-stirred를 어떻게 확장하는가?  
카드 11 (M11): metabolite terminal slope는 누구의 half-life인가?  
카드 12 (M12): $AUC(m)/AUC$는 왜 $f_m$ 하나로 읽을 수 없는가?  
카드 13 (M13): oral first-pass metabolite는 어떻게 정상상태 위험으로 이어지는가?  
카드 14 (M14): 작은 $f_m$이 왜 신장애에서 가장 큰 안전성 문제가 되는가?

**핵심 아이디어(Big Idea)**: 청소율(clearance)은 $Dose/AUC$로 끝나는 숫자가 아니라, **혈류, 단백결합, $CL_{int}$, 투과성/수송체, 신장 여과·분비·재흡수, 대사체 형성·제거**가 한 식 안에서 충돌한 결과입니다. 이 장의 목표는 관찰된 $CL$·$t_{1/2}$·$AUC(m)/AUC$·$C/C_b$ 변화가 **어느 생리학적 병목에서 왔는지 역추적**하는 것입니다.

학습 흐름은 네 단계입니다 — ① $Rate=CL\cdot C$, ② 신장에서 $CL_R=f_e\cdot CL$로 여과·분비·재흡수를 분해, ③ 간에서 well-stirred로 $Q_H$, $f_{ub}$, $CL_{int}$, 투과성을 분리, ④ 모약물–대사체에서 $f_m$, $CL(m)$, 율속단계(rate-limiting step; **전체 속도를 정하는 느린 단계**), 신장애를 추가.

> **버릴 수 없는 한 문장**: "어떤 청소율입니까?"는 항상 "어느 농도 기준인가, 어느 장기인가, 어느 율속단계인가, 모약물인가 대사체인가?"로 나눠서 봐야 합니다.

📍 **이 장의 위치**  
• **다루는 영역**: PopPK · PBPK · TMDD · parent–metabolite joint model이 공유하는 생리학 축.  
• **이 장 없이는**: 공변량(eGFR, $f_u$, transporter genotype 등)을 식의 어느 자리에 넣을지 근거를 댈 수 없음.  
• **이 장을 통과한 뒤**: 모든 공변량 결정이 "어느 생리학적 병목을 가설로 세우는가?"로 바뀝니다.

---

> 📊 **개념 도식 (HTML에서 렌더링):** 청소율 해석 의사결정 지도 — 장기, 투여 경로, 농도 기준, 대사체 축. $CL$ 해석은 "어느 농도 기준인가, 어느 장기인가, 어느 투여 경로인가, 모약물인가 대사체인가?"를 순서대로 묻는 구조적 문제입니다.

## §1.5 빠른 읽기 경로

이 장 전체를 관통하는 핵심 질문은 하나입니다 — **"지금 다루는 것이 정확히 어떤 청소율(clearance)입니까?"**

이 질문은 항상 **4개 좌표**로 분해해서 풉니다.

| # | 좌표 | 묻는 내용 |
|---|---|---|
| 1 | 농도 기준 | 혈장(plasma)? 전혈(blood)? 비결합(unbound)? |
| 2 | 장기 | 신장? 간? 그 밖? |
| 3 | 투여 경로 | IV? 경구? 초회통과가 작동? |
| 4 | 분석 대상 | 모약물(parent)? 대사체(metabolite)? |

시간이 부족하면 **M1 → M2 → M4 → M5 → M14** 다섯 카드만 순서대로 읽어도 이 장의 의사결정 체계가 작동합니다.

| 카드 | 이 경로에서의 역할 |
|---|---|
| **M1** | 청소율의 비례식($Rate = CL \cdot C$) — 기본 좌표 정립 |
| **M2** | 신장 청소율 분해 — 여과·분비·재흡수로 $CL_R$ 풀어내기 |
| **M4** | 간 청소율과 well-stirred — $Q_H$, $f_{ub}$, $CL_{int}$ 분리 |
| **M5** | 고추출/저추출 해석 — 같은 식이 어떻게 다른 임상 함의로 갈라지는가 |
| **M14** | 신부전 + 활성 대사체 통합 — 한 환자에서 위 카드들이 동시에 충돌하는 사례 |

---

<!-- SLIDE_START: §2 | title: §2 개념 해부 카드(Concept Anatomy Cards) -->
<!-- SECTION_CORE: SC-02 -->

## §2 개념 해부 카드(Concept Anatomy Cards)

<!-- SLIDE_START: M1 | title: M1. 청소율 비례성과 반감기의 파생성(Clearance proportionality + half-life is derived) -->
<!-- SECTION_CORE: SC-03 -->

### M1. 청소율 비례성과 반감기의 파생성(Clearance proportionality + half-life is derived)

> **거장의 시각**  
> 반감기 변화에서 곧바로 원인을 찾으면 $CL$ 변화와 $V$ 변화를 섞어 해석하게 됩니다. 먼저 $CL$과 $V$를 분리하면 신장애·간장애·단백결합 변화가 어느 축에서 왔는지 보입니다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: 청소율(clearance)은 제거 속도 자체가 아니라 **농도로 정규화한 제거능**입니다. 그래서 first-order 조건에서 $CL$은 시간마다 새로 바뀌는 숫자가 아니라, 관찰 구간 전체를 설명하는 하나의 비례상수입니다. $AUC$는 그 제거능이 시간 전체에 남긴 관찰량입니다.

**핵심 방정식** [G&W p.49 Eq 2:83–2:86; G&W pp.77–79 Eq 2:180–2:185; R&T pp.124–128 Eq 5-1–5-8]

$$
\underbrace{\frac{dX}{dt}}_{\text{체내 변화속도}}=-\underbrace{CL}_{\text{제거능}}\cdot \underbrace{C}_{\text{농도 신호}}
$$

#### 파라미터 해부 표

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $CL$ | L/h | 농도 대비 제거능 | 신장·간 기능, 단백결합, 대사능 |
| $C$ | mg/L | 제거 속도를 정규화하는 농도 신호 | 투여량, 분포, 시간 |
| $V$ | L | 농도를 양으로 환산하는 분포용적 | 조직분포, 단백결합, 체액량 |
| $t_{1/2}$ | h | $V/CL$에서 파생되는 관찰 결과 | ↑ $V$, ↓ $CL$ |

> 💡 $t_{1/2}$는 원인이 아니라 $V/CL$의 결과입니다. 반감기가 늘었다고 해서 $CL$이 줄었는지 $V$가 늘었는지는 아직 모릅니다.

$$
\underbrace{CL}_{\text{IV CL}}=\frac{\underbrace{Dose_{iv}}_{\text{IV 투여량}}}{\underbrace{AUC_{0-\infty}}_{\text{IV 전신노출}}}, \qquad \underbrace{\frac{CL}{F}}_{\text{경구 CL/F}}=\frac{\underbrace{D_{po}}_{\text{경구 투여량}}}{\underbrace{AUC_{po}}_{\text{경구 노출}}}
$$

$$
\underbrace{CL}_{\text{총농도 CL}}=\underbrace{f_u}_{\text{유리분율}}\cdot\underbrace{CL_u}_{\text{유리 CL}}
$$

**반감기(half-life)는 원인이 아니라 결과** [R&T pp.148–150 Eq 5-24–5-27]

$$
\underbrace{k}_{\text{소실상수}}=\frac{\underbrace{CL}_{\text{제거능}}}{\underbrace{V}_{\text{분포용적}}}, \qquad \underbrace{t_{1/2}}_{\text{반감기}}=\frac{\underbrace{0.693}_{\ln 2}\cdot\underbrace{V}_{\text{분포용적}}}{\underbrace{CL}_{\text{제거능}}}
$$

$t_{1/2}$가 변했다는 말은 $CL$ 또는 $V$가 변했다는 결과 신호일 뿐, $t_{1/2}$ 자체가 $CL$을 결정하지 않습니다.

**현장 팁(Trench-level tip)**: 신부전·간부전·단백결합 변화에서 "반감기가 늘었다/줄었다"로 시작하지 말고 $CL$과 $V$를 먼저 분리하세요. 같은 $t_{1/2}$라도 $CL↑+V↑$가 동시에 생긴 경우와 둘 다 변하지 않은 경우는 완전히 다릅니다.

같은 $CL$이라도 적용 대상에 따라 이름이 달라집니다 — 신장이면 M2의 $CL_R$, 간이면 M4의 $CL_H$, 대사체면 M12의 $CL_f$와 $CL(m)$.

---

> **M1 체화 핵심**  
> ① `반감기가 변했을 때` → $CL$과 $V$ 분리가 원인 진단을 결정  
> ② `CL 변화 vs V 변화 혼동` → 같은 $t_{1/2}$라도 전혀 다른 임상 상황  
> ⚡ `$t_{1/2}$를 원인으로 취급` → covariate 위치 오류와 용량 해석 실패

<!-- SLIDE_START: M2 | title: M2. 신장 청소율 분해: $CL_R$, $f_e$, 여과/분비/재흡수(Renal clearance decomposition: $CL_R$, $f_e$, filtration/secretion/reabsorption) -->
<!-- SECTION_CORE: SC-04 -->

### M2. 신장 청소율 분해: $CL_R$, $f_e$, 여과/분비/재흡수(Renal clearance decomposition: $CL_R$, $f_e$, filtration/secretion/reabsorption)

> **앞 카드에서 이 카드로**  
> M1에서 $CL$을 농도로 정규화한 제거능으로 정의했습니다. 이제 그중 신장 경로가 차지하는 몫을 분해합니다.

> **거장의 시각**  
> $f_e$를 "신기능 영향의 크기"로만 읽으면 nonrenal clearance까지 함께 줄이는 모델을 만들기 쉽습니다. $CL_R=f_e\cdot CL$을 경로 분해로 보면 renal covariate를 어느 자리에 넣어야 하는지 즉시 정해집니다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: $CL_R=f_e\cdot CL$은 단순 비례식이 아닙니다. **혈장 AUC와 소변 누적 배설량을 잇는 다리**입니다. 혈장은 몸 안의 노출을, 소변은 신장 경로로 빠져나간 양을 보여줍니다. 둘을 함께 봐야 renal route의 지분 $f_e$와 $CL_R$가 열립니다.

**신장 생리 요약** [G&W p.48; R&T pp.119–120, 127, 138–145]: 네프론은 보먼주머니·근위세뇨관·헨레고리·원위세뇨관·집합관으로 구성. GFR ≈ **120 mL/min** (Tozer; Gabrielsson 110–130). Urine pH 4.5–8 범위. 평균 신장 혈류 ≈ **1.1 L/min**(신장 추출의 혈류 상한). GFR은 신장 혈장의 여과 부분집합입니다. Inulin은 GFR marker로 언급됩니다.

**핵심 신장 방정식** [G&W pp.49–50 Eq 2:87–2:89; R&T pp.139–142 Eq 5-17–5-23]

$$
\underbrace{\frac{dX_u}{dt}}_{\text{소변 배설속도}}=\underbrace{CL_R}_{\text{신장 CL}}\cdot\underbrace{C}_{\text{혈장농도}}
$$

#### 파라미터 해부 표

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $CL_R$ | L/h | 신장 경로로 제거되는 청소율 | GFR, 분비, 재흡수 |
| $f_e$ | fraction | 전체 CL 중 신장 경로 지분 | 약물 경로, 신기능 |
| $GFR$ | mL/min | 사구체 여과율 | 연령, 신장애, 체표면적 |
| $F_R$ | fraction | 재흡수된 비율 | urine pH, flow, transporter |

> 🔑 **경로 분해 규칙:** 신기능 covariate는 가능하면 total $CL$이 아니라 $CL_R$ 위치에 적용합니다.

$$
\underbrace{X_{u,0-\infty}}_{\text{총 소변량}}=\underbrace{CL_R}_{\text{신장 CL}}\cdot\underbrace{AUC_{0-\infty}}_{\text{전신노출}}
$$

$$
\underbrace{CL_R}_{\text{신장 CL}}=\frac{\underbrace{X_u(t_1,t_2)}_{\text{구간 소변량}}}{\underbrace{AUC(t_1,t_2)}_{\text{동일구간 노출}}}
$$

$$
\underbrace{f_e}_{\text{신장 지분}}=\frac{\underbrace{CL_R}_{\text{신장 CL}}}{\underbrace{CL}_{\text{전체 CL}}}
$$

$$
\underbrace{CL_R}_{\text{순 신장 CL}}=\underbrace{(1-F_R)}_{\text{재흡수 잔여율}}\cdot(\underbrace{CL_f}_{\text{여과}}+\underbrace{CL_S}_{\text{분비}}), \qquad \underbrace{CL_f}_{\text{여과 CL}}=\underbrace{f_u}_{\text{유리분율}}\cdot\underbrace{GFR}_{\text{여과율}}
$$

$CL_R>f_u\cdot GFR$이면 분비(secretion)가 필요하고, $CL_R<f_u\cdot GFR$이면 재흡수(reabsorption)이거나 측정 방식이 잘못됐는지 의심해야 합니다.

**청소율 가산성(Clearance additivity)** [R&T pp.127–128 Eq 5-9]

$$
\underbrace{CL}_{\text{전체 CL}}=\underbrace{CL_R}_{\text{신장}}+\underbrace{CL_H}_{\text{간}}+\underbrace{CL_{other}}_{\text{기타}}
$$

담즙 배설과 장간순환은 소실 곡선을 바꿀 수 있지만, 본 문서에서는 M2의 경로 분해 안에서 한꺼번에 다룹니다 [R&T pp.137–138]. 폐 청소율은 장기 가산성 해석에서 특수 예외로만 기억합니다 [R&T p.128].

**혼동 지점(Confusion)**: $f_e$가 작으면 신장애 영향도 작다고 생각하기 쉽습니다. 모약물 기준으로는 대체로 맞지만, **활성 대사체가 신장으로 빠지는 약이면 신부전 환자에서 모약물보다 대사체가 훨씬 더 쌓입니다** (→ M14 참조).

---

> **M2 체화 핵심**  
> ① `신기능이 변했을 때` → $CL_R=f_e\cdot CL$ 분해가 결정  
> ② `renal vs nonrenal 경로 혼동` → total $CL$ 보정이 nonrenal pathway까지 왜곡  
> ⚡ `$f_e$가 작으면 안전` → active metabolite renal elimination을 놓쳐 신장애 위험 실패

<!-- SLIDE_START: M3 | title: M3. ARE 플롯과 배설속도 플롯(ARE plot vs Excretion Rate plot) -->
<!-- SECTION_CORE: SC-05 -->

### M3. ARE 플롯과 배설속도 플롯(ARE plot vs Excretion Rate plot)

> **앞 카드에서 이 카드로**  
> M2에서 신장 경로의 양을 정의했습니다. 이제 그 양이 실제 소변 수집 데이터에서 어떻게 왜곡되어 보이는지 봅니다.

> **거장의 시각**  
> ARE와 rate plot의 기울기가 안 맞을 때 이를 곧바로 "구획이 더 필요하다"는 신호로 읽으면 **소변 측정 잡음을 구조 모델로 착각하게 됩니다**. 두 plot을 함께 보면 collection interval, bladder emptying, pH/flow 변동을 먼저 걸러낼 수 있습니다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: ARE plot과 excretion-rate plot은 같은 urinary data에서 $K$를 추정합니다. 그러나 한쪽은 구간 배설속도를, 다른 한쪽은 남은 누적 배설량을 봅니다. 그래서 noise와 시간 정보가 다르게 보입니다. Rate plot은 renal clearance의 시간 변동을 잘 드러내고, ARE plot은 누적량 기반이라 **변동이 평탄해져서 보입니다**.

**배설속도 플롯(Rate plot)** [G&W pp.50–51 Eq 2:90–2:92]

$$
\underbrace{\ln\left(\frac{dX_u}{dt}\right)}_{\text{로그 배설속도}}=\underbrace{\ln\left(CL_R\cdot\frac{D_{iv}}{V}\right)}_{\text{초기절편}}-\underbrace{K}_{\text{소실기울기}}\cdot\underbrace{t}_{\text{시간}}
$$

#### 파라미터 해부 표

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $dX_u/dt$ | amount/time | 구간 소변 배설속도 | 수집 간격, pH/flow |
| $X_{u,0-\infty}$ | amount | 총 소변 회수량 | 수집 완료도, 방광 배출 |
| $K$ | 1/time | 소실 기울기 | $CL/V$, 데이터 배치 |

> 💡 Rate plot은 시간 변동을 노출하고, ARE plot은 누적량으로 변동을 평탄하게 만듭니다. slope 불일치가 곧바로 다구획의 증거는 아닙니다.

**ARE 플롯** [G&W pp.50–52 Eq 2:93–2:98]

$$
\underbrace{\ln(X_{u,0-\infty}-X_u)}_{\text{잔여량 로그}}=\underbrace{\ln(X_{u,0-\infty})}_{\text{총량절편}}-\underbrace{K}_{\text{소실기울기}}\cdot\underbrace{t}_{\text{시간}}
$$

| 판단 축 | 배설속도 플롯 | ARE 플롯 |
|---|---|---|
| 수집 간격이 반감기보다 길 때 | 취약 | 상대적으로 안정 |
| 불완전 방광 배출 | 취약 | 누적 편향 가능 |
| $X_{u,0-\infty}$ 필요도 | 낮음 | 높음 |
| pH/urine flow에 따른 $CL_R$ 시간 변동 | 잘 보임 | 평탄해져서 덜 보임 |

정확한 소변 결과를 얻으려면 약물의 소변 농도가 무시할 수준이 될 때까지 소변 시료를 수집하는 것이 좋습니다 [G&W p.51].

**핵심 예시**: PK5에서 urine collection interval은 0.5–12 h로 다양하고, rate plot/ARE plot에서 half-life가 약 **6–6.3 h**로 그림에서 읽어집니다 [G&W p.497]. **Methamphetamine**은 소변 pH 하나로 회수율이 극적으로 달라지는 대표 사례입니다 — **산성 소변에서 70–80%**, **알칼리성 소변에서 1–2%** [R&T p.145]. → 재흡수가 소변 pH 하나로도 회수율을 수십 배 흔든다는 사례입니다.

**현장 팁(Trench-level tip)**: urinary data를 보면 먼저 ARE와 rate plot을 둘 다 그리세요. 두 plot이 같은 $K$를 주지 않으면 먼저 collection interval, bladder emptying, pH/flow 변동을 의심하고, 곧바로 compartment 수를 늘리지 마세요.

---

> 📖 **Gabrielsson p.50, Fig 2.35**: 두 plot 모두 $K$를 주지만 시간 배치와 잡음 민감도가 다릅니다. 그림은 ARE의 실제 시간과 배설속도 plot의 구간 가운데 시점을 대표값으로 쓰는 약속을 직접 보여줍니다.

---

> **M3 체화 핵심**  
> ① `urinary data가 있을 때` → ARE와 rate plot 동시 진단이 결정  
> ② `plot slope 불일치` → 구조 모델보다 collection artifact를 먼저 의심  
> ⚡ `바로 compartment 추가` → pH/flow·방광 배출 문제를 모델 구조로 오인

<!-- SLIDE_START: M4 | title: M4. Well-stirred 간 청소율과 4-모델 압축(Well-stirred hepatic clearance + 4-model compression) -->
<!-- SECTION_CORE: SC-06 -->

### M4. Well-stirred 간 청소율과 4-모델 압축(Well-stirred hepatic clearance + 4-model compression)

> **앞 카드에서 이 카드로**  
> M2–M3가 신장 경로를 측정했다면, 이제 간 경로에서는 혈류와 효소 용량이 어떤 식으로 경쟁하는지 봅니다.

> **거장의 시각**  
> $CL_H$를 하나의 숫자로만 보면 두 가지 효과가 섞여서 보입니다 — 추출률 효과와 단백결합 효과. **$Q_H$ vs $f_{ub}CL_{int}$ 둘 중 어느 쪽이 작은가**라는 관점으로 봐야 혈류 제한과 용량·결합 제한이 분리됩니다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: Well-stirred model(← 간을 즉시 섞인 장기로 보는 모델)은 hepatic clearance를 세 입력값으로 압축합니다 — blood flow $Q_H$, blood unbound fraction $f_{ub}$, intrinsic clearance $CL_{int}$. 분모에서 $Q_H$가 큰지, $f_{ub}\cdot CL_{int}$가 큰지에 따라 고추출/저추출 여부와 임상 해석이 갈립니다.

**핵심 방정식** [G&W pp.79–82 Eq 2:188–2:195; R&T pp.130–135 Eq 5-14–5-15; R&T App.E pp.777–778 Eq E-1–E-8]

$$
\underbrace{CL_{H,b}}_{\text{간 CL_b}}=\underbrace{Q_H}_{\text{간혈류}}\cdot\underbrace{E_H}_{\text{추출률}}=\frac{\underbrace{Q_H}_{\text{혈류한계}}\cdot\underbrace{f_{ub}}_{\text{혈액 유리분율}}\cdot\underbrace{CL_{int}}_{\text{간세포 제거능}}}{\underbrace{Q_H}_{\text{혈류}}+\underbrace{f_{ub}\cdot CL_{int}}_{\text{유리·효소축}}}
$$

#### 파라미터 해부 표

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $CL_{H,b}$ | L/h | blood 기준 간 청소율 | $Q_H$, $f_{ub}$, $CL_{int}$ |
| $Q_H$ | L/h | 간으로 들어오는 혈류 상한 | 간혈류, 심박출량 |
| $f_{ub}$ | fraction | blood 기준 비결합 분율 | 단백결합, 혈구분배 |
| $CL_{int}$ | L/h | 간세포 내재 제거능 | 효소·수송체 활성 |

> 🔑 **Well-stirred 판독법:** $Q_H$가 큰지 $f_{ub}CL_{int}$가 큰지를 먼저 비교합니다. 장기 추출률은 **blood 농도 기준**입니다 — plasma에서 측정한 값은 M8 변환을 거친 뒤 써야 합니다. 비유하자면 간은 수도관과 정수기가 붙은 장치 — 물이 적게 들어오면 혈류가 한계이고, 정수기 용량이 작으면 $f_{ub}CL_{int}$가 한계입니다.

$$
\underbrace{E_H}_{\text{추출분율}}=\frac{\underbrace{CL_{H,b}}_{\text{간 CL_b}}}{\underbrace{Q_H}_{\text{간혈류}}}=\frac{\underbrace{f_{ub}\cdot CL_{int}}_{\text{제거용량}}}{\underbrace{Q_H}_{\text{혈류공급}}+\underbrace{f_{ub}\cdot CL_{int}}_{\text{제거용량}}}
$$

$Q_H \approx$ **1.35 L/min (= 81 L/h)** [R&T p.125].

**극한 근사(Limiting cases)** [R&T pp.130–135]

| 조건 | 근사식 | 해석 |
|---|---|---|
| $f_{ub}\cdot CL_{int}\gg Q_H$ | $CL_{H,b} \approx Q_H$ | 혈류 제한(flow-limited), high extraction |
| $f_{ub}\cdot CL_{int}\ll Q_H$ | $CL_{H,b} \approx f_{ub}\cdot CL_{int}$ | 용량/결합 제한(capacity/binding-limited), low extraction |

$$
\begin{aligned}\underbrace{f_{ub}CL_{int}\gg Q_H}_{\text{제거용량>혈류}}&\Rightarrow \underbrace{CL_{H,b}\approx Q_H}_{\text{혈류제한}}\\ \underbrace{f_{ub}CL_{int}\ll Q_H}_{\text{제거용량<혈류}}&\Rightarrow \underbrace{CL_{H,b}\approx f_{ub}CL_{int}}_{\text{용량·결합제한}}\end{aligned}
$$

**네 가지 간 청소율 모델** [G&W pp.90–94 Table 2.9]: well-stirred, parallel-tube, distributed, dispersion 모델은 모두 간 extraction을 설명합니다. 차이는 간 내부에서 혈액과 hepatocyte가 얼마나 섞이는지, 농도 기울기를 어떻게 처리하는지에 있습니다. 본 핸드아웃은 개념적 차이만 보존하고 distributed/dispersion 상세 수식은 출처 충실성을 위해 잠금 상태로 둡니다.

---

> 📖 **Gabrielsson p.79, Fig 2.58** (companion: Rowland & Tozer p.131, Fig 5-7): Well-stirred 식은 장기 input-output 구조에서 출발합니다. 그림을 보지 않으면 $Q_H$가 단순 공변량이 아니라 **간으로 들어오는 혈류가 정해주는 상한선**이라는 점이 약해집니다.

> **M4 체화 핵심**  
> ① `간 $CL$을 해석할 때` → $Q_H$와 $f_{ub}CL_{int}$ 경쟁이 결정  
> ② `high vs low extraction 혼동` → 단백결합·DDI 해석이 뒤집힘  
> ⚡ `plasma 기준 extraction` → organ blood flow와 단위 불일치로 분류 실패

<!-- SLIDE_START: M5 | title: M5. 고/저 추출률과 투여 경로 × 추출률 × $f_u$ 매트릭스(High/low extraction + route × extraction × $f_u$ matrix) -->
<!-- SECTION_CORE: SC-07 -->

### M5. 고/저 추출률과 투여 경로 × 추출률 × $f_u$ 매트릭스(High/low extraction + route × extraction × $f_u$ matrix)

> **앞 카드에서 이 카드로**  
> M4의 well-stirred 식은 투여 경로(IV/oral)나 단백결합 상태가 바뀌면 임상 결론이 완전히 달라집니다.

> **거장의 시각**  
> "High extraction이면 $f_u$ 무관"을 모든 상황에 적용하면 oral first-pass와 비결합 endpoint 해석이 뒤집힙니다. 투여 경로 × 추출률 × total/unbound의 세 가지 축으로 놓으면 같은 $f_u$ 변화도 맞는 자리에 들어갑니다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: 단백결합의 효과는 약물 이름만 보고 정할 수 없습니다. **세 가지를 같이 봐야 결정됩니다**: ① 투여 경로(IV/oral), ② 고추출/저추출 여부, ③ 보는 농도가 총량인지 비결합인지. "High extraction이면 $f_u$ 무관"이라는 말은 **IV total concentration**에 한정되는 위험한 절반 진술입니다.

**투여 경로 매트릭스(Route matrix)** [G&W pp.83–85; R&T pp.150–163]

| 시나리오 | Total concentration / AUC | Unbound concentration |
|---|---|---|
| IV + High extraction | $CL \approx Q_H$, total $C$는 $f_u$에 둔감 | $C_u=f_u\cdot C$, $f_u$ 증가 시 unbound 증가 가능 |
| IV + Low extraction | $CL \approx f_u\cdot CL_{int}$, total $C$ 감소 | $C_u$는 대체로 $CL_{int}$에 의해 보존 |
| Oral + High extraction | first-pass 때문에 total AUC가 $f_u\cdot CL_{int}$에 민감 | unbound AUC는 $CL_{int}$ 중심으로 해석 |
| Oral + Low extraction | total AUC가 $f_u\cdot CL_{int}$에 민감 | unbound AUC는 $CL_{int}$ 중심으로 해석 |

$$
\begin{aligned}\text{IV high: }&\underbrace{CL\approx Q_H}_{\text{혈류제한 CL}},\quad \underbrace{C_u=f_uC}_{\text{유리농도 확인}}\\ \text{Low/oral 축: }&\underbrace{CL\approx f_uCL_{int}}_{\text{결합·용량민감}},\quad \underbrace{AUC\propto (f_uCL_{int})^{-1}}_{\text{경구노출 민감}}\end{aligned}
$$

#### 파라미터 해부 표

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $f_u$ | fraction | plasma 비결합 분율 | 알부민, AAG, displacement |
| $C_u$ | concentration | pharmacologically available 농도 | $f_u$, total $C$ |
| $AUC$ | concentration·time | total exposure | route, extraction, $CL_{int}$ |
| $F$ | fraction | 경구 생체이용률 | first-pass, 흡수, 장/간 대사 |

> 🔑 **세 가지 축으로 읽는 법:** route, extraction class, total/unbound endpoint를 동시에 지정해야 합니다. "High extraction이면 $f_u$ 무관"은 IV total endpoint에만 적용됩니다.

**Tozer 통합 예시** [R&T pp.152–163]

- **Alfentanil**(저추출 opioid) + **rifampin**(강력한 CYP3A 유도제): 효소가 유도되니까 청소율이 늘고 AUC가 줄어듭니다. → 저추출 약물이 $CL_{int}$ 변화에 직접 반응한다는 사례입니다 [R&T p.152].
- **Alprenolol**(고추출 β차단제) + **pentobarbital**(효소 유도제): high extraction IV에서는 효소 유도 효과가 작지만, 경구 생체이용률은 감소합니다 [R&T p.153]. → IV와 oral이 같은 약에서도 다르게 반응하는 사례.
- **Fentanyl** + **itraconazole**(CYP3A 억제제 약함) vs **ritonavir**(CYP3A 강억제): itraconazole은 IV fentanyl PK에 큰 영향이 없지만, ritonavir는 clearance를 **0.94 → 0.32 L/h/kg**로 낮춰 고추출에서 저추출로 분류가 전환됩니다 [R&T pp.154–155].
- **Phenytoin** 요독증: $f_u$ 증가로 총 농도는 낮아질 수 있으나, 비결합 농도 관점으로 해석해야 합니다 [R&T pp.159–160].
- **Clofibric acid** 신증후군: 작은 $V$에서 $f_u$ 증가가 $CL$ 변화를 거쳐 반감기 단축을 만들 수 있습니다 [R&T pp.161–162].

**현장 팁(Trench-level tip)**: high extraction 약물에서 IV DDI가 음성이라고 oral DDI도 안전하다고 결론 내리지 마세요. Route가 바뀌면 first-pass와 $f_u\cdot CL_{int}$ 민감도가 바뀝니다.

---

> 📊 **개념 도식 (HTML에서 렌더링):** 투여 경로 × 추출률 × 단백결합 해석 매트릭스 — 단백결합의 효과는 약물 이름 하나로 정해지지 않고, 투여 경로, 고추출/저추출 여부, total/unbound endpoint에 따라 달라집니다.

---

> **M5 체화 핵심**  
> ① `단백결합 변화가 있을 때` → route × extraction × endpoint가 결정  
> ② `IV high extraction vs oral high extraction 혼동` → first-pass DDI 위험 누락  
> ⚡ `IV negative DDI를 oral 안전으로 일반화` → 라벨 방어 실패

<!-- SLIDE_START: M6 | title: M6. IVIVE 함정: 단일점, MMP, 데이터 압축(IVIVE pitfalls: single-point, MMP, data condensation) -->
<!-- SECTION_CORE: SC-08 -->

### M6. IVIVE 함정: 단일점, MMP, 데이터 압축(IVIVE pitfalls: single-point, MMP, data condensation)

> **앞 카드에서 이 카드로**  
> M4–M5가 간 청소율 식의 해석을 세웠다면, 이제 그 식에 넣는 $CL_{int}$ 입력값이 어디서 무너질 수 있는지 점검합니다.

> **거장의 시각**  
> IVIVE 실패를 hepatic model의 문제로만 보면 이미 압축되어 사라진 in vitro 곡선을 복구하려고 하게 됩니다. 입력 데이터가 single point·MMP·압축 중 어디서 정보를 잃었는지 먼저 보면 실패 원인이 상류에서 보입니다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: IVIVE는 $V_{max}$, $K_m$, microsomal protein scaling을 넣는 계산 문제가 아닙니다. 먼저 **어떤 정보를 버렸는지**를 점검해야 합니다. 한 점에서 얻은 $CL_{int}$, 잘못된 MMP(microsomal protein per gram of liver; 간 1g당 마이크로솜 단백량) 보정, 과도한 데이터 압축은 모두 in vivo clearance를 왜곡합니다.

**핵심 흐름** [G&W pp.85–90]

$$
\underbrace{CL_{int,in\ vitro}}_{\text{in vitro}}\rightarrow \underbrace{CL_{int,scaled}}_{\text{체내 스케일}}\rightarrow \underbrace{CL_H}_{\text{예측 간 CL}}=\frac{\underbrace{Q_H}_{\text{혈류}}\cdot\underbrace{f_u}_{\text{유리분율}}\cdot\underbrace{CL_{int}}_{\text{스케일 제거능}}}{\underbrace{Q_H}_{\text{혈류}}+\underbrace{f_u\cdot CL_{int}}_{\text{제거용량}}}
$$

#### 파라미터 해부 표

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $CL_{int,in\ vitro}$ | volume/time | in vitro 제거능 | 농도범위, 비결합 보정 |
| $CL_{int,scaled}$ | volume/time | 체내로 스케일된 제거능 | MMP, liver weight, scaling factor |
| $V_{max}/K_m$ | volume/time | 저농도 선형 근사 제거능 | 포화, enzyme capacity |

> 🔑 **IVIVE 검토 순서:** single-point → MMP scaling → data condensation → transporter/permeability 누락 순서로 점검합니다. 정교한 hepatic model로도 single-point 입력에서 사라진 곡선 정보는 복구되지 않습니다 — 흐릿하게 압축된 사진을 고해상도 화면에 띄우는 것과 같아서 원본 rate 곡선이 사라졌다면 뒤의 모델은 잃어버린 곡률을 만들 수 없습니다.

**세 가지 함정**: ① **단일 농도 함정**: 한 농도 rate를 $V_{max}/K_m$처럼 쓰면 비선형성·포화를 놓침 [G&W pp.85–89]. ② **MMP 보정 함정**: 간 g당 microsomal protein 보정은 평균값 하나가 아니라 변이·비율 처리에 민감 [G&W p.87]. ③ **데이터 압축 함정**: 농도-속도 관계를 하나의 $CL_{int}$로 압축하면 곡선 형태·이상치 구조가 사라짐 [G&W pp.88–89].

**현장 팁(Trench-level tip)**: IVIVE report를 검토할 때 첫 질문은 "well-stirred 식이 맞는가?"가 아니라 **"in vitro rate 정보가 single point로 뭉개졌는가?"**입니다. 뭉개진 입력은 정교한 hepatic model로도 복구되지 않습니다.

---

> **M6 체화 핵심**  
> ① `IVIVE 예측이 빗나갈 때` → 입력 데이터 압축 여부가 결정  
> ② `single-point rate vs MM 정보 혼동` → saturation과 곡률 소실  
> ⚡ `정교한 간 모델로 복구 가능하다는 믿음` → Phase 1 CL 예측 실패

<!-- SLIDE_START: M7 | title: M7. PK5 혈장+소변 동시 적합(PK5 simultaneous plasma+urine fitting) -->
<!-- SECTION_CORE: SC-09 -->

### M7. PK5 혈장+소변 동시 적합(PK5 simultaneous plasma+urine fitting)

> **앞 카드에서 이 카드로**  
> M2–M6의 장기별 분해는 실제 데이터에서 plasma와 urine을 동시에 맞출 때 비로소 추정 가능한 구조가 됩니다.

> **거장의 시각**  
> 소변 데이터를 별도 계산표로 분리하면 $f_e$와 $CL_R$를 plasma model 안에서 따로 추정할 수 없게 됩니다. Plasma와 urine을 동시에 적합하면 endpoint별 오차와 renal fraction을 같은 구조 안에서 추정할 수 있습니다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: PK5는 urinary data를 별도 계산표로 처리하지 않습니다. **Plasma 농도와 누적 소변량을 한 모델에서 동시에 fitting**합니다. 이 구조가 NONMEM에서 plasma+urine, IV+oral, parent+metabolite를 함께 fitting하는 사고방식의 출발점입니다.

**문제 앵커** [G&W pp.494–499]: **250 mg i.v. bolus** [G&W p.494]. 초기 추정 $V \approx 7$ L, $CL \approx 2$ L/h, $f_e \approx 0.3$. 최종 $CL \approx 1.2$ L/h, $f_e \approx 35\%$, $CL_R \approx 0.42$ L/h; parameter CVs <5%; plasma/urine CV **2.84%**와 **8.96%** [G&W pp.497–498]. 해석적 풀이와 ODE는 거의 동일한 추정값을 줍니다 [G&W pp.497–499].

**모델 골격** [G&W pp.497–499]

$$
\underbrace{C(t)}_{\text{혈장농도}}=\frac{\underbrace{D_{iv}}_{\text{IV 용량}}}{\underbrace{V}_{\text{분포용적}}}\exp\left(-\underbrace{\frac{CL}{V}}_{\text{소실상수 }k}\underbrace{t}_{\text{시간}}\right)
$$

#### 파라미터 해부 표

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $C(t)$ | mg/L | 시간별 plasma 농도 | $D_{iv}$, $V$, $CL$ |
| $X_u(t)$ | amount | 누적 소변 배설량 | $f_e$, $D_{iv}$, $CL/V$ |
| $f_e$ | fraction | 신장 제거 지분 | renal route, urine recovery |

> 💡 Plasma는 노출을, urine은 신장 경로의 양을 알려줍니다. 둘을 분리하면 $f_e$가 흔들립니다 — 비유하자면 plasma는 저수지 수위, urine은 배수구로 빠진 총량입니다. 두 endpoint의 CV가 다르므로 `DVID` 기반 endpoint 분리와 endpoint별 잔차오차 블록이 필요합니다(PK5 권고).

$$
\underbrace{X_u(t)}_{\text{누적 소변량}}=\underbrace{f_e}_{\text{신장 지분}}\cdot\underbrace{D_{iv}}_{\text{IV 용량}}\left[1-\exp\left(-\underbrace{\frac{CL}{V}}_{\text{소실상수}}\underbrace{t}_{\text{시간}}\right)\right]
$$

---

> **M7 체화 핵심**  
> ① `plasma+urine 데이터가 있을 때` → endpoint 동시 적합이 $f_e$와 $CL_R$를 결정  
> ② `plasma-only fit` → renal fraction 식별 불가  
> ⚡ `오차 모델 통합` → endpoint별 산포 차이를 흡수해 추정 편향

<!-- SLIDE_START: M8 | title: M8. 혈장-혈액 비와 혈액 청소율(Plasma-to-blood ratio and blood clearance) -->
<!-- SECTION_CORE: SC-10 -->

### M8. 혈장-혈액 비와 혈액 청소율(Plasma-to-blood ratio and blood clearance)

> **앞 카드에서 이 카드로**  
> M4–M7의 간·신장 해석은 농도 기준이 맞아야 작동합니다. 그래서 plasma 기준을 blood 기준으로 바꾸는 다리가 필요합니다.

> **거장의 시각**  
> Plasma $CL$을 그대로 $Q_H$와 비교하면 장기 추출의 분모가 틀어져 실제보다 높은 추출률이 잡힙니다. $C/C_b$를 거쳐 $CL_b$로 바꾸면 혈류와 같은 단위에서 간 추출을 판단할 수 있습니다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: 장기 추출률(← 장기 통과 중 제거된 비율)은 blood flow와 비교하므로 **blood 농도 기준 청소율**이 필요합니다. 그런데 실제 측정은 대부분 plasma 농도입니다. **이때 plasma 농도를 blood 농도로 바꿔 써야 합니다.** 변환을 안 하면 분모가 달라지고 결과적으로 추출률 분류가 통째로 틀어집니다.

**청소율 관계식** [R&T pp.124–128 Eq 5-4–5-6]

$R=C/C_b$로 정의합니다.

$$
\underbrace{CL_b}_{\text{혈액 CL}}=\underbrace{CL}_{\text{혈장 CL}}\cdot\underbrace{\frac{C}{C_b}}_{\text{기준변환}}=\underbrace{CL}_{\text{혈장 CL}}\cdot\underbrace{R}_{\text{변환비}}
$$

#### 파라미터 해부 표

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $CL_b$ | L/h | blood 기준 청소율 | plasma $CL$, $C/C_b$ |
| $R=C/C_b$ | ratio | plasma-to-blood 변환비 | hematocrit, RBC partition |
| $H$ | fraction | hematocrit | 환자 혈구용적률 |
| $K_{PBC}$ | ratio | 혈구-비결합 혈장 분배 | RBC binding/partition |

> 🔑 **추출 전 필수 변환:** hepatic $E_H$ 계산 전 plasma $CL$을 $CL_b$로 변환합니다. $f_u$와 $f_{ub}$는 같은 분율이 아니라 농도 기준이 다른 분율입니다.

$$
\underbrace{CL}_{\text{혈장 CL}}=\underbrace{CL_b}_{\text{혈액 CL}}\cdot\underbrace{\frac{C_b}{C}}_{\text{역변환}}=\frac{\underbrace{CL_b}_{\text{혈액 CL}}}{\underbrace{R}_{C/C_b}}
$$

**App.D 질량수지** [R&T App.D pp.775–776 Eq D-1–D-8]

$$
\underbrace{\frac{C}{C_b}}_{\text{혈장/혈액비}}=\frac{1}{1+\underbrace{H}_{\text{적혈구용적률}}\left(\underbrace{f_u}_{\text{혈장 유리분율}}\underbrace{K_{PBC}}_{\text{RBC 분배}}-1\right)}
$$

여기서 $H$는 hematocrit, $f_u$는 혈장 내 비결합 분율, $K_{PBC}$는 혈구-비결합 혈장 분배계수입니다.

**App.D 역행렬 필수** [R&T App.D pp.775–776 Eq D-8]

$$
\underbrace{K_{PBC}}_{\text{RBC분배}}=\frac{\underbrace{H}_{\text{적혈구용적률}}-1+\underbrace{(C_b/C)}_{\text{혈액/혈장비}}}{\underbrace{f_u}_{\text{유리분율}}\cdot\underbrace{H}_{\text{RBC 분율}}}
$$

**해석상 함의**: $R<1$이면 plasma CL이 실제보다 다르게 보일 수 있습니다. 간 추출에는 $E_H=CL_{H,b}/Q_H$를 써야 하며, $f_u$와 $f_{ub}$는 호환되지 않습니다($f_{ub}=f_u\cdot (C/C_b)$).

**혼동 지점(Confusion)**: $CL=60\ \mathrm{L/h}$, $Q_H=81\ \mathrm{L/h}$이면 중등도 추출처럼 보일 수 있습니다. 그러나 $R=C/C_b=0.5$이면 $CL_b=30\ \mathrm{L/h}$이고 $E_H=0.37$입니다. **분류가 바뀝니다.**

---

> **M8 체화 핵심**  
> ① `간 추출을 판단할 때` → $CL_b=CL\cdot C/C_b$ 변환이 결정  
> ② `plasma CL vs blood CL 혼동` → false-high extraction 분류  
> ⚡ `$CL/Q_H$ 직접 비교` → PBPK 입력과 DDI 해석 실패

<!-- SLIDE_START: M9 | title: M9. 투과성 속도 제한 간 흡수: App.E $\rho$ (Permeability-rate-limited hepatic uptake: App.E $\rho$) -->
<!-- SECTION_CORE: SC-11 -->

### M9. 투과성 속도 제한 간 흡수: App.E $\rho$ (Permeability-rate-limited hepatic uptake: App.E $\rho$)

> **앞 카드에서 이 카드로**  
> M8에서 blood 기준을 맞춘 뒤에도, hepatocyte 내부로 들어가는 접근성이 느리면 well-stirred의 전제가 무너집니다.

> **거장의 시각**  
> $CL_{int}$가 충분하면 hepatic clearance도 충분하다고 보면 hepatocyte 접근성이라는 병목을 놓칩니다. $\rho$를 넣으면 세포막 uptake가 효소 제거능보다 앞단에서 clearance를 막을 수 있다는 것이 보입니다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: 기본 well-stirred model은 간세포 안팎의 unbound 농도가 빠르게 평형이라고 가정합니다. 그러나 hepatic uptake permeability가 느리면 세포 내부 unbound 농도가 혈액 쪽 unbound 농도보다 낮아집니다. 이 경우 $CL_{int}$만으로는 hepatic clearance를 설명할 수 없습니다.

**App.E Model II** [R&T App.E pp.778–779 Eq E-9–E-15]

$\rho$(← 세포 안팎 unbound 비율)는 hepatocyte 내부 unbound 농도가 혈액 쪽 unbound 농도를 얼마나 따라가는지 나타냅니다.

$$
\underbrace{\rho}_{\text{세포접근성}}=\frac{\underbrace{P_{in}\cdot SA}_{\text{유입투과}}}{\underbrace{P_{out}\cdot SA}_{\text{유출투과}}+\underbrace{CL_{int}}_{\text{대사제거}}}
$$

#### 파라미터 해부 표

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $\rho$ | ratio | hepatocyte 접근성 | uptake/outflow permeability, $CL_{int}$ |
| $P_{in}\cdot SA$ | volume/time | 세포 유입 투과능 | transporter, membrane permeability |
| $P_{out}\cdot SA$ | volume/time | 세포 유출 투과능 | efflux, passive diffusion |
| $CL_{int}$ | volume/time | 세포 내 대사 제거능 | enzyme activity |

> 🔑 **ρ 판독법:** passive diffusion이 충분하면 $\rho\to1$, uptake가 느리면 $\rho<1$입니다. 효소가 충분해도 약물이 hepatocyte 안으로 못 들어가면 clearance는 낮아집니다 — 공장 문 앞 회전문이 느리면 공장 안 효소가 아무리 빨라도 전체 생산량은 느려집니다.

$$
\underbrace{CL_{H,b}}_{\text{간 CL_b}}=\frac{\underbrace{Q_H}_{\text{혈류}}\cdot\underbrace{f_{ub}}_{\text{혈액 유리분율}}\cdot\underbrace{\rho}_{\text{세포접근성}}\cdot\underbrace{CL_{int}}_{\text{대사제거}}}{\underbrace{Q_H}_{\text{혈류}}+\underbrace{f_{ub}\cdot \rho\cdot CL_{int}}_{\text{보정 제거축}}}
$$

수동 확산/permeability가 충분히 커서 세포 내외의 비결합 농도가 빠르게 평형에 가까워지면 $\rho\to1$이 되어 기본 well-stirred model로 환원됩니다. 반대로 uptake permeability가 작으면 $\rho<1$이고 clearance는 permeability-limited가 됩니다 [R&T App.E pp.778–779].

**경구 투여 다리(Oral bridge)** [R&T App.E pp.779–780 Eq E-19–E-20]

위 가정하에서 간 추출로만 제거되는 약물의 경우:

$$
\underbrace{AUC_{po}}_{\text{경구노출}}=\frac{\underbrace{Dose}_{\text{투여량}}}{\underbrace{f_{ub}}_{\text{혈액 유리분율}}\cdot\underbrace{\rho}_{\text{세포접근성}}\cdot\underbrace{CL_{int}}_{\text{제거능}}}
$$

**현장 팁(Trench-level tip)**: transporter 기질에서 $f_u$와 $CL_{int}$만으로 IVIVE를 강행하면 permeability 병목을 $CL_{int}$ 부족으로 오해할 수 있습니다.

---

> **M9 체화 핵심**  
> ① `$CL_{int}$로 설명되지 않는 간 CL` → $\rho$가 결정  
> ② `효소 부족 vs uptake 병목 혼동` → covariate 선택 위치 오류  
> ⚡ `$\rho$ 생략` → transporter substrate의 IVIVE mismatch 은폐

<!-- SLIDE_START: M10 | title: M10. 확장 청소율: 수송체–효소 구조(Extended clearance: transporter–enzyme architecture) -->
<!-- SECTION_CORE: SC-12 -->

### M10. 확장 청소율: 수송체–효소 구조(Extended clearance: transporter–enzyme architecture)

> **앞 카드에서 이 카드로**  
> M9의 $\rho$는 단일 보정항처럼 보이지만, 실제로는 uptake·metabolism·efflux의 다층 구조를 열어 줍니다.

> **거장의 시각**  
> 간 소실을 효소 하나로 줄이면 transporter 단계의 DDI와 IVIVE mismatch가 모두 $CL_{int}$ 오류처럼 보입니다. Uptake·metabolism·efflux를 나누면 어느 막 단계가 전체 clearance를 막는지 분류할 수 있습니다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: 확장 청소율(extended clearance)은 hepatic elimination을 "효소 하나"로 보지 않습니다. **Sinusoidal uptake, canalicular efflux, basolateral efflux, intracellular metabolism**의 네 흐름으로 봅니다. 기본 well-stirred는 이 네 흐름 중 막 단계가 충분히 빠른 특수한 경우입니다.

**최소 해석** [R&T pp.136–138 Eq 5-35–5-36; R&T App.E pp.778–779]: R&T 5장은 간 소실이 관류·단백결합·세포 활성만으로 끝나지 않고 막 투과성과 transporter에 의해 달라짐을 명시합니다. App.E는 이를 $\rho$로 제1원리화합니다.

- **Uptake-limited**: 혈장/혈액에서 hepatocyte로 들어가는 단계가 병목.
- **Metabolism-limited**: 세포 내부 도달은 충분하고 효소 용량이 병목.
- **Efflux-limited**: 담즙 또는 혈액 방향 유출이 병목.

잘 안 맞는 IVIVE가 항상 효소 assay 문제는 아닙니다 — transporter/permeability 항이 빠졌을 수 있습니다(M6 IVIVE trap + M9 $\rho$ 연결).

---

> 📖 **Rowland & Tozer p.136, Fig 5-11** (companion: Tozer App.E pp.778–779, Eq E-9–E-15): 세포막을 사이에 둔 uptake, metabolism, efflux의 위치 관계가 핵심입니다. 이 위치 관계를 보지 않으면 permeability-limited clearance를 단순한 낮은 $CL_{int}$로 오해하기 쉽습니다.

---

#### 파라미터 해부 표

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| Uptake | — | 혈액→hepatocyte 유입 | OATP/OCT/OAT, permeability |
| Metabolism | — | 세포 내 효소 제거 | CYP/UGT activity |
| Efflux | — | 담즙/혈액 방향 유출 | canalicular/basolateral transporter |
| $\rho$ | ratio | membrane bottleneck 요약 | uptake vs metabolism 경쟁 |

> 💡 확장 청소율은 효소 하나가 아니라 uptake·metabolism·efflux의 병렬/직렬 구조입니다. 경험적 scalar는 transporter 병목을 숨길 수 있습니다.

> **M10 체화 핵심**  
> ① `수송체 기질 간 소실` → uptake/metabolism/efflux 단계가 결정  
> ② `enzyme-only 사고` → transporter DDI와 efflux 병목 누락  
> ⚡ `empirical scalar로 봉합` → 구조 원인 은폐와 예측 외삽 실패

<!-- SLIDE_START: M11 | title: M11. 대사체 처리(disposition)의 율속단계(Rate-limiting step in metabolite disposition) -->
<!-- SECTION_CORE: SC-13 -->

### M11. 대사체 처리(disposition)의 율속단계(Rate-limiting step in metabolite disposition)

> **앞 카드에서 이 카드로**  
> M10까지 모약물 clearance의 병목을 분해했다면, 이제 대사체 곡선의 말단 기울기가 무엇을 반영하는지 분리해야 합니다.

> **거장의 시각**  
> 대사체의 말단 기울기를 곧바로 대사체의 반감기라고 쓰면 형성률속 상황에서 **모약물을 그대로 베껴낸 모습**을 대사체 특성으로 오인합니다. 형성과 제거 중 느린 단계를 확인하면 관찰된 기울기와 대사체 본연의 처리(disposition)를 분리할 수 있습니다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: 대사체 농도-시간 곡선의 terminal slope(← 말단 감소 구간의 기울기)는 대사체 자체의 반감기가 아닐 수 있습니다. 형성이 느리면 대사체는 모약물의 잔향처럼 모약물 반감기를 따라 감소합니다. 제거가 느리면 대사체 자체 반감기가 말단을 지배합니다.

**대사체가 임상적으로 중요한 이유** [R&T pp.658–659]: **활성, 독성, 억제, 유도, 치환**. 그러나 충분한 농도에 도달하지 않으면 치료적 우려는 작습니다 — "활성 대사체가 있다"와 "임상적으로 의미가 있다"는 같은 말이 아닙니다 [R&T p.659].

**질량수지(Mass balance)** [R&T pp.659–662 Eq 20-1–20-3]

$$
\underbrace{\frac{dA(m)}{dt}}_{\text{대사체 변화}}=\underbrace{k_fA}_{\text{형성입력}}-\underbrace{k(m)A(m)}_{\text{제거출력}}
$$

#### 파라미터 해부 표

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $k_f$ | 1/time | parent→metabolite 형성속도 | 효소, parent 노출 |
| $k(m)$ | 1/time | metabolite 제거속도 | renal/hepatic metabolite CL |
| $A(m)$ | amount | 체내 대사체 양 | 형성입력·제거출력 |
| terminal slope | 1/time | 관찰된 말단 감소 | formation 또는 elimination 율속 |

> 🔑 **Terminal slope 규칙:** downstream 물질의 말단 감소는 **가장 느린 단계**가 지배합니다. parallel decline은 대사체 본연의 반감기 증거가 아니라 formation-limited 신호일 수 있습니다 — 대사체는 앞차(모약물)를 따라가는 차량이라서 앞차가 느리면 뒤차 속도계가 아니라 교통 흐름 전체가 느린 것입니다.

| 분류 | 조건 | 관찰 패턴 | 해석 |
|---|---|---|---|
| Formation rate-limited | $k \ll k(m)$ | parent에 나란히 감소 | 관찰된 metabolite terminal $t_{1/2}$은 parent의 half-life |
| Elimination rate-limited | $k(m) \ll k$ | metabolite가 더 늦게 peak, 더 느리게 감소 | terminal $t_{1/2}$은 metabolite 자신의 half-life |

$$
\begin{aligned}\underbrace{k\ll k(m)}_{\text{형성 느림}}&\Rightarrow \underbrace{t_{1/2,\mathrm{obs}}(m)\approx t_{1/2,\mathrm{parent}}}_{\text{parent 잔향}}\\ \underbrace{k(m)\ll k}_{\text{제거 느림}}&\Rightarrow \underbrace{t_{1/2,\mathrm{obs}}(m)\approx t_{1/2,\mathrm{metabolite}}}_{\text{대사체 지배}}\end{aligned}
$$

순차 연쇄(sequential chain)에서는 "fastest k가 결정한다"가 아니라, downstream 물질의 말단 감소는 **가장 느린 단계**가 지배합니다 [R&T p.661]. 신장애에서는 모약물 CL 보정이 대사체 노출을 자동으로 보정하지 않습니다. 대사체 CL과 율속단계를 별도로 평가해야 합니다 [R&T pp.673–675].

**혼동 지점(Confusion)**: 모약물과 대사체가 평행 감소를 보이면 대사체 반감기를 모약물과 같다고 보고하기 쉽습니다. 정확히는 "모약물 투여 후 관찰된 말단 반감기"가 모약물의 반감기를 그대로 보여주는 것뿐입니다.

---

> 📖 **Rowland & Tozer p.660, Fig 20-1**: 대사체의 말단 기울기는 형성과 제거 중 더 느린 단계가 결정합니다. 그림은 parent → metabolite → eliminated metabolite 흐름에서 $k_f$, $k(m)$, other elimination을 동시에 보여줍니다.

> **M11 체화 핵심**  
> ① `metabolite terminal slope를 볼 때` → formation/elimination 율속단계가 결정  
> ② `parallel decline vs own half-life 혼동` → metabolite half-life 과대 해석  
> ⚡ `system slope를 metabolite label로 보고` → renal impairment 축적 예측 실패

<!-- SLIDE_START: M12 | title: M12. $AUC(m)/AUC$ 분해: $f_m × CL/CL(m)$ ($AUC(m)/AUC$ decomposition: $f_m × CL/CL(m)$) -->
<!-- SECTION_CORE: SC-14 -->

### M12. $AUC(m)/AUC$ 분해: $f_m × CL/CL(m)$ ($AUC(m)/AUC$ decomposition: $f_m × CL/CL(m)$)

> **앞 카드에서 이 카드로**  
> M11에서 형성과 제거 율속을 나눴습니다. 이제 $AUC(m)/AUC$를 $f_m$과 $CL(m)$으로 분해합니다.

> **거장의 시각**  
> $AUC(m)/AUC$를 $f_m$으로 읽으면 형성 쪽 문제와 대사체 청소율 쪽 문제를 구분할 수 없습니다. 이 비를 $f_m\times CL/CL(m)$으로 나눠서 봐야 활성 대사체 위험의 정량 좌표가 생깁니다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: $AUC(m)/AUC$는 $f_m$ 그 자체가 아닙니다. 이 비는 대사체 형성분율과 대사체 청소율이 함께 들어간 복합량입니다. 따라서 AUC ratio 하나만 보고 형성 쪽 문제인지 제거 쪽 문제인지 분리할 수 없습니다.

**핵심 방정식** [R&T pp.662–665 Eq 20-4–20-7]

$$
\underbrace{\frac{dA(m)}{dt}}_{\text{대사체 변화}}=\underbrace{CL_f\cdot C}_{\text{형성입력}}-\underbrace{CL(m)\cdot C(m)}_{\text{제거출력}}
$$

#### 파라미터 해부 표

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $AUC(m)/AUC$ | ratio | metabolite/parent 노출비 | $f_m$, $CL$, $CL(m)$ |
| $CL_f$ | L/h | metabolite 형성 clearance | $f_m\cdot CL$ |
| $f_m$ | fraction | parent 제거 중 형성분율 | metabolic pathway share |
| $CL(m)$ | L/h | metabolite 제거 clearance | renal/hepatic function |

> 💡 $AUC(m)/AUC$는 $f_m$과 $CL(m)$이 섞인 값입니다 — AUC ratio 하나로 형성 문제와 제거 문제를 분리할 수 없습니다. 비유하자면 수도꼭지 유입량($f_m$)과 배수구 크기($CL(m)$)가 함께 만든 수위입니다.

시간에 대해 적분하면:

$$
\underbrace{\frac{AUC(m)}{AUC}}_{\text{노출비}}=\frac{\underbrace{CL_f}_{\text{형성 CL}}}{\underbrace{CL(m)}_{\text{대사체 CL}}}
$$

여기서:

$$
\underbrace{CL_f}_{\text{형성 CL}}=\underbrace{f_m}_{\text{형성분율}}\cdot\underbrace{CL}_{\text{parent CL}}
$$

따라서:

$$
\boxed{\underbrace{\frac{AUC(m)}{AUC}}_{\text{노출비}}=\underbrace{f_m}_{\text{형성분율}}\cdot\frac{\underbrace{CL}_{\text{parent CL}}}{\underbrace{CL(m)}_{\text{대사체 CL}}}}
$$

**필수 Eq.20-7** [R&T p.664 Eq 20-7]

$$
\underbrace{\frac{k(m)}{k}}_{\text{속도비}}=\frac{\underbrace{CL(m)/CL}_{\text{청소율비}}}{\underbrace{V(m)/V}_{\text{분포비}}}
$$

$AUC(m)/AUC<1$이고 $f_m$이 알려지지 않은 경우, $CL(m) \geq CL/f_m$이라고 추론할 수 없습니다. 원전에 부합하는 부등식은 $CL(m)>f_m\cdot CL$뿐입니다. 같은 AUC ratio는 낮은 $f_m$, 높은 $CL(m)$, 또는 두 조건 모두에서 나올 수 있습니다.

**보존된 예시** [R&T pp.662–665]

**Methylprednisolone hemisuccinate → methylprednisolone**(prodrug→active), **tolbutamide**(sulfonylurea) **→ hydroxytolbutamide**, **propranolol**(고추출 β차단제) **→ naphthoxylactic acid**는 대사체 곡선이 율속단계와 상대적 청소율을 어떻게 구분하는지 보여주는 대표 사례입니다. 개별 그림 수치는 본 문서에서 확장하지 않습니다.

**현장 팁(Trench-level tip)**: active metabolite PopPK에서 $AUC(m)/AUC$가 작다는 이유로 대사체를 무시하지 마세요. $f_m$이 작아도 $CL(m)$이 신장애에서 크게 줄면 M14의 문제가 됩니다.

---

> **M12 체화 핵심**  
> ① `AUC(m)/AUC가 주어졌을 때` → $f_m$과 $CL(m)$ 분해가 결정  
> ② `노출비 vs 형성분율 혼동` → 신부전·DDI 외삽 오류  
> ⚡ `AUC ratio 단독 보고` → formation/elimination 원인 구분 실패

<!-- SLIDE_START: M13 | title: M13. 초회통과 대사체 기여와 정상상태 대사체(First-pass metabolite contribution + steady-state metabolite) -->
<!-- SECTION_CORE: SC-15 -->

### M13. 초회통과 대사체 기여와 정상상태 대사체(First-pass metabolite contribution + steady-state metabolite)

> **앞 카드에서 이 카드로**  
> M12의 노출비 분해는 단회 노출을 넘어 first-pass 형성과 정상상태 축적 문제로 이어집니다.

> **거장의 시각**  
> 경구 대사체 노출을 단순히 생체이용률 문제로 보면 초회통과 형성과 전신순환 형성이 섞입니다. 입력 경로를 둘로 나누면 정상상태 축적과 IV-oral 비교 설계의 필요성이 드러납니다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: 모약물을 **경구 투여하면 대사체는 두 군데에서 생깁니다** — ① 흡수 과정에서 간 초회통과를 받으며 생기거나, ② 흡수가 끝난 뒤 전신 순환에서 생기거나. 이게 임상적으로 문제가 되는 건 한 가지 조건이 맞을 때입니다 — **모약물이 초회통과를 강하게 받는데, 하필 그 대사체가 활성을 띌 때.**

**First-pass 이중 입력** [R&T pp.665–669]: 경구 모약물 투여 후 관찰되는 대사체는 두 입력의 합 — ① 흡수·초회통과 중 형성, ② 흡수된 전신 모약물에서 이후 형성.

**수정된 예시**

- **Propranolol**(고추출 β차단제): 원전 예시는 단일 **20 mg 경구 투여**이며, 80 mg이 아닙니다. **Naphthoxylactic acid**(naphthoxylactic acid; propranolol의 대사체)는 propranolol과 거의 같은 시간에 최고 농도에 도달하며, 이는 초회통과 대사체 유입과 일치합니다 [R&T p.666]. → 모약물이 high first-pass면 대사체 입력에서 초회통과 비중이 크다는 사례.
- **Morphine/M6G**(morphine-6-glucuronide; 모르핀의 활성 대사체): 원전은 경구 **11.7 mg**과 정맥 **5 mg** morphine을 비교하며, 10 mg 등가 용량 틀이 아닙니다. Morphine의 경구 생체이용률은 낮지만, 초회통과 형성이 기여하므로 M6G 노출량/총량은 비슷할 수 있습니다 [R&T pp.667–668].
- **Isoproterenol**(β교감신경 작용제): 투여 경로에 따라 장벽 대사인지 간외 대사인지가 달라지면 소변 회수율도 달라집니다 [R&T p.669].

**정상상태 대사체** [R&T pp.669–673 Eq 20-11–20-15]

일정 속도 주입 시:

$$
\underbrace{C(m)_{ss}}_{\text{대사체 Css}}=\frac{\underbrace{f_m}_{\text{형성분율}}\cdot\underbrace{R_{inf}}_{\text{입력속도}}}{\underbrace{CL(m)}_{\text{대사체 CL}}}
$$

#### 파라미터 해부 표

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $C(m)_{ss}$ | concentration | 정상상태 metabolite 농도 | $f_m$, $R_{inf}$, $CL(m)$ |
| $R_{inf}$ | amount/time | parent 입력속도 | infusion/dosing rate |
| $\tau$ | time | 투여간격 | dosing regimen |
| $AUC(m)_{single}$ | concentration·time | 단회 metabolite 노출 | first-pass/systemic formation |

> 🔑 **Oral metabolite 판독법:** 초회통과 형성과 전신순환 형성을 한 모델에 같이 넣으면 **두 경로를 따로 추정할 수 없게 됩니다.** 경구 데이터만으로는 이 둘을 원리적으로 구분할 수 없습니다 — 마치 공항 입국장과 도심 도로 두 곳에서 동시에 들어오는 사람 수처럼, 총 인원만 보면 어느 입구가 병목인지 알기 어렵습니다.

다회 경구 투여 시 중첩 원리에 의해:

$$
\underbrace{C(m)_{av,ss}}_{\text{평균 Css}}=\frac{\underbrace{AUC(m)_{single}}_{\text{단회 노출}}}{\underbrace{\tau}_{\text{투여간격}}}
$$

정상상태 도달 시간은 율속 패턴에 따라 모약물 소실 또는 대사체 소실 중 더 느린 쪽이 결정합니다 [R&T pp.670–673]. **N-desalkylhalazepam**(diazepam계 활성 대사체)에서 대사체 축적/감소는 모약물보다 느립니다. 정확한 timing은 본 문서에 고정하지 않습니다 `[R&T p.672; 확인 필요]`. **Carbamazepine**(항경련제)의 autoinduction은 정성적 추세만 보존하며 — 용량 정규화 모약물이 감소하고 대사체 관계가 변화하지만, 정확한 용량 범위는 고정하지 않습니다 `[R&T p.676; 확인 필요]`.

**현장 팁(Trench-level tip)**: 경구 모약물 단독 데이터만으로는 낮은 모약물 생체이용률과 대규모 초회통과 대사체 형성을 항상 구분할 수 없습니다. Route 비교는 단순 생체이용률 계산을 넘어 진단 도구로 기능합니다.

---

> **M13 체화 핵심**  
> ① `oral parent 후 metabolite가 보일 때` → first-pass와 systemic formation 분리가 결정  
> ② `oral 단독 데이터 과해석` → 두 경로 따로 추정 실패  
> ⚡ `정상상태 축적 경시` → active metabolite 라벨 wording 실패

<!-- SLIDE_START: M14 | title: M14. 신장애 활성 대사체 시나리오와 상호전환(Renal impairment active-metabolite scenario + interconversion) -->
<!-- SECTION_CORE: SC-16 -->

### M14. 신장애 활성 대사체 시나리오와 상호전환(Renal impairment active-metabolite scenario + interconversion)

> **앞 카드에서 이 카드로**  
> M13의 정상상태 대사체 개념은 신장애에서 활성 대사체가 전체 위험을 지배하는 최종 시나리오로 모입니다.

> **거장의 시각**  
> $f_m$이 작으면 대사체 위험도 작다고 생각하기 쉽지만, 진짜 위험은 형성분율이 아니라 **신장애에서 대사체 $CL(m)$이 얼마나 무너지는지**가 결정합니다. 작은 형성 경로도 제거 경로가 닫히면 전체 활성 노출의 지배 경로가 됩니다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: 활성 대사체가 존재할 때, 모약물 $f_e$ 하나만으로는 신부전 용량 결정을 내릴 수 없습니다. 가장 위험한 상황이 반드시 '모약물이 주로 신배설되는' 경우는 아닙니다. **모약물이 일부 대사되어 생긴 활성 대사체가 그 자체로 신배설을 받는** 경우도 똑같이 위험합니다.

**Tozer 풀이 시나리오** [R&T pp.673–675; Fig 20-10; Table 20-4]

정상 신기능 예시:

| 파라미터 | Parent drug | Active metabolite |
|---|---:|---:|
| 전체 CL | 30 L/h | 10 L/h |
| 신장 CL | 15 L/h | 8.5 L/h |
| Parent 경구 F / 형성 분율 | $F=0.8$ | $f_m=0.3$ |

$$
\underbrace{F=0.8}_{\text{경구 F}},\qquad \underbrace{f_m=0.3}_{\text{형성분율}}
$$

#### 파라미터 해부 표

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $F$ | fraction | 경구 bioavailability | absorption, first-pass |
| $f_m$ | fraction | active metabolite 형성분율 | metabolic pathway share |
| $CL(m)$ | L/h | active metabolite 제거능 | renal impairment, anuria |
| dose ratio | ratio | 정상 총 활성 농도 유지 감량비 | parent+metabolite combined exposure |

> 🔑 **방어 논리 규칙:** parent-only 감량은 시나리오 (3)을 닫지 못하므로 통합 노출 또는 모니터링 논리가 필요합니다. 신장애에서 진짜 무서운 건 **모약물보다 활성 대사체가 훨씬 더 많이 쌓이는 경우**입니다.

경구 10 mg/h 투여 시, 정상상태 총 활성 농도는 모약물 **0.27 mg/L** + 대사체 **0.24 mg/L** = **0.51 mg/L**입니다 [R&T pp.673–674]. 무뇨 상태에서 모약물은 약 **2배** 증가하지만, 대사체는 약 **13배**까지 증가할 수 있습니다. 정상 총 활성을 맞추기 위한 용량비는 약 **0.14**입니다 [R&T p.674].

**시나리오 규칙** [R&T p.675]

1. 대사체 형성이 모약물의 주요 제거 경로이고 대사체가 활성인 경우, 용량은 대사체 청소율을 기준으로 설정해야 할 수 있습니다.
2. 모약물의 신배설이 주요 경로이고 대사체 형성이 부차적인 경우, 모약물 노출이 지배합니다.
3. **대사체 형성 비율이 작지만 대사체 제거가 거의 신배설에만 의존하고 대사체가 활성인 경우, 신부전에서 대사체가 전체 활성을 지배할 수 있습니다.**

**상호전환(Interconversion)** [R&T pp.676–679]

상호전환은 모약물과 대사체가 서로를 재생성할 수 있음을 뜻합니다. 따라서 대사체 쪽 신장애가 모약물의 겉보기 소실까지 늦출 수 있습니다. **Clofibric acid**(clofibrate의 활성 대사체)는 대표 사례로 보존합니다. 그림에서 읽어낸 수치 앵커는 고정하지 않습니다 `[R&T p.679; 확인 필요]`.

**혼동 지점(Confusion)**: '소수 대사 경로(minor metabolite pathway)'는 '소수 안전성 우려(minor safety concern)'와 같은 말이 아닙니다. 신부전에서 대사체 $CL(m)$이 무너지면, 작은 $f_m$이라도 주요 노출 경로가 될 수 있습니다.

---

> 📖 **Rowland & Tozer p.674, Fig 20-10 and Table 20-4**: 모약물 농도만 보면 안전해 보이는데 환자는 부작용을 호소하는 상황이 바로 이것입니다. 그림과 표는 모약물 단독 용량 조정이 왜 실패하는지를 보여주는 핵심 증거입니다.

---

#### M. Plausible Fallacy — 나비효과 연쇄

**오류:** "$f_m$이 작으면 대사체는 부차적 우려입니다."  
**왜 그럴싸한가:** 정상 신기능에서는 대사체 질량수지가 $f_m\times Dose$로 들어오므로, 작은 $f_m$은 작은 대사체 노출량처럼 보입니다.  
**나비효과:** 활성 대사체 소실이 거의 신배설이라면($f_e(m)\approx1$), 무뇨 상태에서 $CL(m)$이 거의 0으로 무너짐 → Tozer 풀이 예에서 $f_m=0.3$임에도 대사체 Css 약 13배 상승 [R&T pp.673–675] → [임상] 모약물 단독 감량 후 활성 대사체 독성 농도 미예측 → [모델링/규제] 통합 노출 재계산, ESRD 대사체 PK 재분석, 라벨 방어 논리 보완 요구.  
**Detection signature:** 모약물 CL은 신기능 비례로 감소하지만 대사체 Css가 10배 이상 상승하는 비대칭 패턴.  
**Defense:** 통합 노출(모약물 + 활성 대사체, 등효능 또는 효능 가중)을 정상 수준으로 맞추는 용량비를 별도로 계산해야 합니다.

> **M14 체화 핵심**  
> ① `신장애 + active metabolite` → parent+metabolite combined exposure가 결정  
> ② `minor pathway vs minor concern 혼동` → 작은 $f_m$의 위험을 과소평가  
> ⚡ `parent-only 감량` → [임상] metabolite 독성 농도 미예측 + [규제] ESRD PK 재분석 요구

<!-- SLIDE_START: §5 | title: §5 혼동 쌍(Confusion Pairs) — 반드시 분리해야 하는 개념 쌍 -->
<!-- SECTION_CORE: SC-17 -->

## §5 혼동 쌍(Confusion Pairs) — 반드시 분리해야 하는 개념 쌍

### 쌍 1(Pair 1). $CL$, $CL_R$, $f_e$

#### 2×4 혼동 분리 매트릭스

| 비교 기준 | $CL$ | $CL_R$ / $f_e$ |
|---|---|---|
| 단위 / 차원 | L/h, 전체 전신 청소율 | $CL_R$: L/h; $f_e$: fraction |
| 수식 내 위치 (분자/분모/지수) | $CL=CL_R+CL_H+CL_{other}$의 합 | $f_e=CL_R/CL$; $CL_R=f_e\cdot CL$ |
| 변화 원인 (생물학적/병적) | renal + nonrenal pathway 전체 | 신기능, urine route, filtration/secretion/reabsorption |
| 혼동 시 임상 결과 | total CL 전체에 renal covariate 적용 | nonrenal clearance까지 줄어 systematic underestimation |

> **⚡ 기억 고리**: $f_e$는 "renal pathway의 지분"입니다 — $CL_R=f_e\cdot CL$은 곱셈 분해이지 비례 단축이 아닙니다. 신부전 covariate는 $CL$ 전체에 곱하지 말고 $CL_R$ 위치(분해된 자리)에만 곱해야 합니다.

### 쌍 2(Pair 2). ARE 플롯 vs 배설속도 플롯(ARE plot vs Excretion-rate plot)

#### 2×4 혼동 분리 매트릭스

| 비교 기준 | ARE plot | Excretion-rate plot |
|---|---|---|
| 단위 / 차원 | 잔여 누적량 로그 | 구간 배설속도 로그 |
| 수식 내 위치 (분자/분모/지수) | $\ln(X_{u,0-\infty}-X_u)$ | $\ln(dX_u/dt)$ |
| 변화 원인 (생물학적/병적) | $X_{u,0-\infty}$ 추정, 누적 편향 | collection interval, pH/flow, bladder emptying |
| 혼동 시 임상 결과 | 평활된 누적량을 시간 변동 없음으로 오인 | sampling artifact를 구조 모델로 오인 [G&W p.51] |

> **⚡ 기억 고리**: Rate plot은 *시간 정보를 노출*하고, ARE plot은 *누적량으로 변동을 평탄하게* 만듭니다. 두 plot의 slope가 달라지면 모델 구조(구획 수)가 아니라 sampling design(수집 간격, 방광 배출, 소변 pH/flow)을 먼저 의심하세요.

### 쌍 3(Pair 3). 혈장 $CL$ vs 혈액 $CL_b$ (Plasma $CL$ vs Blood $CL_b$)

#### 2×4 혼동 분리 매트릭스

| 비교 기준 | Plasma $CL$ | Blood $CL_b$ |
|---|---|---|
| 단위 / 차원 | plasma concentration 기준 L/h | blood concentration 기준 L/h |
| 수식 내 위치 (분자/분모/지수) | $CL=Dose/AUC_{plasma}$ | $CL_b=CL\cdot C/C_b$ |
| 변화 원인 (생물학적/병적) | plasma binding, plasma measurement | hematocrit, RBC partition, $C/C_b$ |
| 혼동 시 임상 결과 | $CL/Q_H$로 false-high extraction | $E_H=CL_b/Q_H$를 놓쳐 DDI 해석 실패 [R&T pp.124–128; R&T App.D pp.775–776] |

> **⚡ 기억 고리**: $E_H=CL_b / Q_H$이지 $CL / Q_H$가 아닙니다. $R=C/C_b<1$인 약물에서 plasma 기준 비교를 하면 같은 약물이 false-high extraction으로 분류되어 임상·DDI 해석이 통째로 틀어집니다 — App.D bridge 없이 organ extraction을 말하지 마세요.

### 쌍 4(Pair 4). $f_u$ vs $f_{ub}$

#### 2×4 혼동 분리 매트릭스

| 비교 기준 | $f_u$ | $f_{ub}$ |
|---|---|---|
| 단위 / 차원 | plasma 내 unbound fraction | blood 내 unbound fraction |
| 수식 내 위치 (분자/분모/지수) | plasma binding 식 | well-stirred의 $f_{ub}\cdot CL_{int}$ |
| 변화 원인 (생물학적/병적) | albumin/AAG, displacement | $f_u$ + $C/C_b$ 변환 |
| 혼동 시 임상 결과 | plasma 분율을 blood 식에 직접 대입 | hepatic extraction과 PBPK 입력 단위 오류 [R&T App.D pp.775–776] |

> **⚡ 기억 고리**: Plasma 식에서 blood 식으로 옮길 때 $R=C/C_b$를 곱해야 합니다. $f_u$와 $f_{ub}$는 *분모가 다른 두 측정량*이지 같은 변수의 별명이 아닙니다 — 이 한 곱이 빠지면 well-stirred의 분자($f_{ub}\cdot CL_{int}$)가 통째로 잘못된 단위에서 평가됩니다.

### 쌍 5(Pair 5). 고추출 IV vs 고추출 경구(High extraction IV vs High extraction oral)

#### 2×4 혼동 분리 매트릭스

| 비교 기준 | High extraction IV | High extraction oral |
|---|---|---|
| 단위 / 차원 | systemic $CL\approx Q_H$ | first-pass bioavailability/AUC |
| 수식 내 위치 (분자/분모/지수) | 혈류 제한 항 | $F$, first-pass, $f_{ub}CL_{int}$ 민감 항 |
| 변화 원인 (생물학적/병적) | hepatic blood flow | enzyme induction/inhibition, first-pass formation |
| 혼동 시 임상 결과 | IV DDI 음성을 oral 안전으로 오판 | route-dependent DDI와 metabolite formation 위험 누락 [G&W pp.83–85; R&T pp.665–669] |

> **⚡ 기억 고리**: IV에서는 $Q_H$ 상한(flow-limited)이 enzyme 변화를 가립니다. Oral에서는 first-pass의 $f_{ub}\cdot CL_{int}$ 민감도가 그 상한을 풀어줍니다. **IV negative DDI는 oral safety의 보장이 아닙니다** — route가 바뀌는 순간 같은 enzyme 변화가 다른 endpoint로 나타납니다.

---

### 쌍 6(Pair 6). Well-stirred vs 확장/투과성 제한 모델(Well-stirred vs extended/permeability-limited model)

#### 2×4 혼동 분리 매트릭스

| 비교 기준 | Well-stirred | Extended/permeability-limited |
|---|---|---|
| 단위 / 차원 | rapid equilibration 가정 | membrane/transporter 병목 포함 |
| 수식 내 위치 (분자/분모/지수) | $f_{ub}CL_{int}$ | $f_{ub}\rho CL_{int}$ 또는 uptake/efflux 단계 |
| 변화 원인 (생물학적/병적) | blood flow, binding, enzyme | uptake permeability, transporter, efflux |
| 혼동 시 임상 결과 | 낮은 $CL_{int}$처럼 오인 | transporter/permeability covariate 누락 [R&T App.E pp.778–779] |

> **⚡ 기억 고리**: Well-stirred는 "세포 안팎이 즉시 평형"이라는 가정입니다. $\rho<1$이면 *효소가 아니라 막*이 병목이며, IVIVE의 $CL_{int}$ 부족처럼 보이는 mismatch가 실제로는 transporter/permeability 항 누락입니다. $\rho\to1$이 회복되는 조건은 수동 확산이 $CL_{int}$보다 충분히 클 때입니다.

### 쌍 7(Pair 7). 단일점 $CL_{int}$ vs Michaelis–Menten 정보(Single-point $CL_{int}$ vs Michaelis–Menten information)

#### 2×4 혼동 분리 매트릭스

| 비교 기준 | 단일점 $CL_{int}$ | Michaelis–Menten 정보 |
|---|---|---|
| 단위 / 차원 | 한 농도 rate의 압축값 | 농도-속도 곡선 정보 |
| 수식 내 위치 (분자/분모/지수) | $CL_{int}$ 하나로 입력 | $V_{max}$, $K_m$, free concentration |
| 변화 원인 (생물학적/병적) | 측정 농도 선택, scaling | saturation, enzyme capacity, transporter uptake |
| 혼동 시 임상 결과 | 곡선 정보 소실 후 정교한 모델 적용 | IVIVE 예측 실패와 FIH CL mismatch [G&W pp.85–89] |

> **⚡ 기억 고리**: 한 농도에서의 rate를 그대로 $V_{max}/K_m$로 쓰는 것은 **곡선을 버린 다음 분수식을 정교화**하는 셈입니다. Saturation, free concentration, MMP scaling, 수송체 매개 uptake 중 어느 하나라도 빠지면 그 위에 어떤 hepatic model을 얹어도 입력 정보가 이미 뭉개져 있어 회복되지 않습니다.

### 쌍 8(Pair 8). 형성 율속 vs 제거 율속 대사체(Formation-rate-limited vs elimination-rate-limited metabolite)

#### 2×4 혼동 분리 매트릭스

| 비교 기준 | Formation-rate-limited | Elimination-rate-limited |
|---|---|---|
| 단위 / 차원 | parent가 metabolite terminal slope 지배 | metabolite own elimination 지배 |
| 수식 내 위치 (분자/분모/지수) | $k \ll k(m)$ | $k(m) \ll k$ |
| 변화 원인 (생물학적/병적) | 느린 parent disappearance/formation | 느린 metabolite clearance |
| 혼동 시 임상 결과 | parent 잔향을 metabolite half-life로 라벨링 | renal impairment 축적·multiple-dose 예측 실패 [R&T pp.659–662] |

> **⚡ 기억 고리**: **평행 감소이면 대사체는 모약물의 잔향입니다.** 보고된 대사체 말단 $t_{1/2}$은 대사체 *자신의* 것이 아닐 수 있습니다. "Formation rate-limited"는 대사체가 자기 자신의 제거 속도가 아니라 모약물의 제거 속도를 입고 사라지는 상태입니다.

> **▶ 치명적 타격 (Critical Blow)**  
> 이 혼동을 품고 NDA 또는 임상 dosing 결정을 강행했을 때: 모약물과 대사체의 말단 $t_{1/2}$이 같다는 보고는 대사체 자체의 제거 특성을 보여주는 게 *아닙니다*. Sponsor가 대사체의 IV 단독 시험 없이 "대사체 반감기는 X시간"이라 명시하면, 이는 system-level 말단 slope에 대사체 라벨을 붙인 것입니다. 그 결과 (a) 신장애에서 대사체 축적 외삽이 빗나가고, (b) 다회 투여 축적 예측이 빗나가며, (c) dose-response timing 평가가 동시에 빗나갑니다. "순차 연쇄에서는 가장 느린 단계가 downstream 물질의 말단 감소를 지배한다"가 본 항목의 정확한 원전 진술입니다 [R&T pp.659–662].

### 쌍 9(Pair 9). $AUC(m)/AUC$ vs $f_m$

#### 2×4 혼동 분리 매트릭스

| 비교 기준 | $AUC(m)/AUC$ | $f_m$ |
|---|---|---|
| 단위 / 차원 | 노출비 | 형성분율 |
| 수식 내 위치 (분자/분모/지수) | $f_m\cdot CL/CL(m)$ | 형성항 단독 |
| 변화 원인 (생물학적/병적) | formation + metabolite clearance | metabolic pathway share |
| 혼동 시 임상 결과 | 낮은 ratio를 낮은 formation으로 단정 | $CL(m)$ 변화와 신장애 위험 누락 [R&T pp.662–665] |

> **⚡ 기억 고리**: $AUC(m)/AUC<1$은 **하나의 식에 두 미지수**입니다 — $f_m$이 작아서일 수도, $CL(m)$이 커서일 수도, 둘 다일 수도 있습니다. $f_m$을 알지 못하면 $CL(m)/CL$ 부등식을 쓰지 마세요. 원전에 부합하는 부등식은 오직 $CL(m)>f_m\cdot CL$뿐입니다.

### 쌍 10(Pair 10). 순차 대사 vs 상호전환(Sequential metabolism vs interconversion)

#### 2×4 혼동 분리 매트릭스

| 비교 기준 | Sequential metabolism | Interconversion |
|---|---|---|
| 단위 / 차원 | 한 방향 대사 흐름 | 양방향 parent↔metabolite 흐름 |
| 수식 내 위치 (분자/분모/지수) | downstream chain | reversible transfer 항 |
| 변화 원인 (생물학적/병적) | 대사 경로 순차 진행 | 재생성, 장간순환·재전환 가능성 |
| 혼동 시 임상 결과 | parent profile만으로 renal-safe 오판 | metabolite 신부전이 parent apparent elimination까지 지연 [R&T pp.676–679] |

> **⚡ 기억 고리**: Sequential은 *한 방향*, interconversion은 *양방향*입니다. 후자에서는 모약물의 $f_e$가 작아도 대사체 쪽 신부전이 모약물의 *겉보기* 소실까지 늦출 수 있습니다 — 모약물 profile만 보고 "renal-safe"로 분류하면 메커니즘을 놓칩니다.

혼동 쌍의 공통 메시지: **같아 보이는 두 숫자가 실제로는 서로 다른 분모, 투여 경로, 구획, 또는 율속단계를 갖습니다.**

---

<!-- SLIDE_START: §7 | title: §7 자기 검증(Self-Test) — 소크라테스식 딜레마 -->
<!-- SECTION_CORE: SC-18 -->

## §7 자기 검증(Self-Test) — 소크라테스식 딜레마

### Q1. 청소율 정의

$CL=Dose/AUC$가 compartment model 없이도 성립하는 이유를 $Rate=CL\cdot C$의 시간 적분으로 설명하세요.  
**답 방향**: 총 제거량 = dose이고, $\int Rate\,dt=CL\cdot\int C\,dt$이므로 $CL=Dose/AUC$가 모델 독립적으로 성립합니다.

### Q2. 신장 분해

정상 $CL=10\ \mathrm{L/h}$, $f_e=0.6$인 약물에서 renal function이 25%로 떨어지고 nonrenal CL은 보존됩니다. 새 total CL은?  
**답 방향**: renal CL=6→1.5, nonrenal=4, total=5.5 L/h.

### Q3. 소변 플롯

Rate plot과 ARE plot의 slope가 다르고, rate plot에서 시간별 변동이 큽니다. 어떤 artifact 또는 physiology를 먼저 의심해야 합니까?  
**답 방향**: 수집 간격, 방광 배출, pH/소변 유량 변동, $X_{u,\infty}$ 편향을 순서대로 점검합니다.

### Q4. Well-stirred 극한 근사

$Q_H=81\ \mathrm{L/h}$, $f_{ub}\cdot CL_{int}=20\ \mathrm{L/h}$이면 high/low/intermediate 중 어디에 가깝습니까? $f_{ub}$가 4배 증가하면?  
**답 방향**: 초기 $E=20/(81+20)=0.20$으로 낮은 편. $f_{ub}$가 4배이면 80이 되어 $E \approx 0.50$, 중간 수준으로 상승합니다.

---

### Q5. 혈장 CL vs 혈액 CL

Plasma $CL=60\ \mathrm{L/h}$, $C/C_b=0.5$, $Q_H=81\ \mathrm{L/h}$. $CL_b$와 추출률은? Plasma CL만 쓰면 어떤 오류가 생깁니까?  
**답 방향**: $CL_b=30\ \mathrm{L/h}$, $E=0.37$. Plasma 기준으로 비교하면 실제보다 높은 추출률로 분류되는 오류가 발생합니다.

### Q6. IVIVE 함정

한 substrate concentration에서 얻은 in vitro rate로 $CL_{int}$를 만들고 MMP 평균값 하나로 scaling했다. Phase 1에서 in vivo CL이 예측의 1/5입니다. 어떤 세 가지 원인을 우선 점검할 것인가?  
**답 방향**: 단일 농도 비선형성, 결합/비결합 농도 오류, MMP/scaling 변이, transporter/permeability 항 누락을 순서대로 확인합니다.

### Q7. 대사체 율속단계

Parent 투여 후 모약물과 대사체가 평행 말단 감소를 보입니다. 별도 대사체 투여에서는 대사체 반감기가 더 짧다. 어떤 경우입니까?  
**답 방향**: Formation rate-limited 상태입니다. Parent 투여 후 관찰되는 대사체 slope는 parent에 의해 지배됩니다.

### Q8. AUC 비

$AUC(m)/AUC=0.5$입니다. 이 값만으로 $f_m=0.5$라고 말할 수 있습니까?  
**답 방향**: 불가능합니다. $CL(m)/CL$이 필요합니다. 식은 $AUC(m)/AUC=f_m\cdot CL/CL(m)$입니다.

### Q9. 보스 딜레마(Boss Dilemma) — 신장애 + 활성 대사체

Parent drug의 정상 $CL=30\ \mathrm{L/h}$, renal CL=15 L/h, oral $F=0.8$입니다. 활성 대사체의 $CL(m)=10\ \mathrm{L/h}$, renal CL(m)=8.5 L/h, 형성 분율 $f_m=0.3$입니다. 무뇨 상태에서 parent renal CL과 metabolite renal CL이 모두 0이 됩니다. 모약물만의 용량 조정이 왜 불안전합니까?  
**답 방향**: 모약물 노출은 약 2배 증가하지만, 대사체 CL은 10에서 1.5 L/h로 무너지며 Tozer 시나리오에서 형성 분율이 증가할 수 있습니다. 대사체 노출이 전체 활성을 지배할 수 있고, 원전 예시에서 약 13배 대사체 증가와 약 0.14의 용량비가 보고됩니다 [R&T pp.673–675].

> **전문가의 절충 판단(Master's Trade-off)**  
> Q9에는 두 가지 *방어 가능한* 입장이 있습니다 — 어느 쪽을 택하든 그 결정은 라벨/CSR에서 어떻게 방어할 수 있는지를 함께 답해야 합니다.  
>  
> **(a) 통합 노출 기반 용량 조정.** 모약물 + 활성 대사체의 통합 활성을 정상 수준으로 맞추는 용량비(Tozer 풀이 예의 약 0.14)를 적용합니다. *방어 논리*: 대사체가 모약물과 거의 등효능이거나 효능 가중 합이 독성 유발인자라면, 통합 Css를 기준점으로 삼는 것이 가장 보수적입니다. *Trade-off 비용*: 모약물 주도 치료 효과를 underdose할 위험이 있습니다. 라벨 문구 요구: "based on combined active exposure".  
>  
> **(b) 2단계 모니터링.** 모약물 용량은 모약물 CL 변화에만 맞추되, 활성 대사체 TDM 또는 PK/PD biomarker로 안전 안내선을 운영합니다. *방어 논리*: 모약물과 대사체의 효능 차이가 분명하고, 대사체 분석법과 turnaround time이 가능하면 일률 감량보다 정밀합니다. *Trade-off 비용*: 분석법 검증, 채혈 설계, 조치 역치가 모두 라벨에 명시되어야 합니다.  
>  
> **두 입장 모두에서 방어 불가능한 것**: "parent $f_e$ 변화에 비례한 일률 감량" 단독. [R&T p.675]는 위 (1)/(2)/(3) 시나리오 규칙으로 이를 수식적으로 차단합니다. Sponsor가 활성 대사체의 ESRD PK를 측정하지 않은 상태에서 parent-only 비례 감량을 제출하면, 시나리오 (3) 가능성을 닫지 못한 채 권고가 발행되는 것이며, 이것이 본 딜레마의 *진짜* 위험입니다.

---

<!-- SLIDE_START: §8 | title: §8 요약 & NONMEM/PopPK 교량 -->
<!-- SECTION_CORE: SC-19 -->

## §8 요약 & NONMEM/PopPK 교량

### §8A. 학습 위계상 위치(Positioning) — 28-session arc 내 위치

본 세션은 PopPK 학습 위계의 **physiology layer spine**을 마무리합니다.

- **선행 의존성**: 1-구획 IV/oral 동역학, AUC 정의·trapezoidal 적분, mass balance — 그 위에 *생리학적 분해*를 얹습니다.
- **본 세션이 담당하는 자리**: 관찰된 $CL$/$t_{1/2}$/$AUC(m)/AUC$/$C/C_b$ 변화가 어느 생리학적 병목에서 왔는지 역추적하는 frame.

**본 세션이 열어주는 후속 영역**:

| 후속 세션 | 이 세션에서 열리는 개념 | 이 세션 없으면 실패하는 것 |
|---|---|---|
| PBPK 모델링 | well-stirred / 확장 청소율의 organ-level 제1원리 | organ input을 경험적 scalar로만 보정 |
| PopPK covariate selection | eGFR, $f_u$, transporter genotype, hepatic function score의 식 내 위치 | 통계적 유의성만으로 covariate 채택 |
| Parent–metabolite joint modeling | $f_m$, $CL(m)$, 율속단계의 식별가능성 spine | $F$와 $f_m$ product confounding |
| Renal/Hepatic impairment label | 시나리오 규칙 기반 dose/label wording | parent-only 또는 route-insensitive label 작성 |

### §8B. 선행 의존성(Dependencies) — 본 chapter를 대충 넘겼을 때의 후속 실패 모드

- **D1. Plasma↔Blood 단위 붕괴**: App.D bridge 생략 시 hepatic $E_H$가 $R=C/C_b$만큼 빗나가 고추출/저추출 분류·DDI 해석·PBPK input $f_{ub}\cdot CL_{int}$ 단위가 통째로 잘못됩니다.
- **D2. $f_e$ covariate 오적용**: $f_e$를 비례 단축으로 다루어 신부전 covariate를 total $CL$에 곱하면 nonrenal까지 같이 줄어 *systematic CL underestimation*이 발생, dose adjustment가 안전성과 어긋납니다.
- **D3. 대사체 식별가능성 실패**: 율속단계 분리 없이 $f_m$/$CL(m)$/$V(m)$을 자유 추정하면 oral data만으로 $F$와 $f_m$이 product confounding을 일으켜 두 파라미터를 따로 추정할 수 없습니다 (NONMEM `$COV` 실패 또는 RSE 폭증).
- **D4. 신장애 시나리오 (3) 누락**: 작은 $f_m$을 부차적 우려로 분류하여 활성 대사체 ESRD PK를 측정하지 않으면 parent-only 감량 라벨이 대사체 과포화를 만듭니다.

### §8C. 전문성 해자(Professional Moat) — 이 chapter를 진정으로 내면화한 연구자만이 갖는 것

NONMEM control stream과 GOF plot 작성은 이미 자동화 영역에 가깝습니다. 본 chapter를 구조적으로 내면화한 모델러는 자동화가 복제하지 못하는 것 — **관찰된 PK/PD 신호가 어느 생리학적 병목에서 왔는지 역추적하는 능력** — 을 갖습니다.

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| 수렴 실패 또는 GOF anomaly | 단위, 율속단계, $\rho$, interconversion | → | 구조 모델 과증식 또는 병목 오판 | §8D 4개 시그니처 순서로 점검 |
| Covariate 선택 회의 | eGFR, $f_u$, transporter genotype | → | 통계적 유의성만으로 생리학 위치 누락 | covariate가 들어갈 식의 자리를 먼저 명시 |
| Renal/Hepatic impairment 라벨 회의 | parent $CL$, $CL(m)$, combined exposure | → | parent-only 감량 또는 route 오류 | 시나리오 규칙과 방어 논리를 라벨 문구로 연결 |

### §8D. 진단 시그니처 카탈로그(Diagnostic Signatures Catalog)

진단 시그니처 4개. 모두 PART A 원전 앵커가 박힌 M카드 위에서 의미를 갖는 *실패 모드 요약*입니다.

| ID | 시그니처 명칭 | Trigger pattern (관찰 신호) | 기계론적 원인 | Anchor card |
|---|---|---|---|---|
| **DS-1** | Phantom Plasma Clearance | 추정 $CL$이 $Q_H$ (≈81 L/h)를 초과하는 결과가 나옴 — 생리학적으로 불가능한 값 | Plasma $CL$을 그대로 organ flow와 비교한 단위 mismatch. $R=C/C_b<1$인 약물에서 발생. App.D bridge로 $CL_b=CL \cdot R$을 적용해야 함. | M8 (Plasma-to-blood ratio) |
| **DS-2** | Phantom Metabolite Half-life | 대사체의 추정 `k`가 모약물의 `k`와 거의 동일하게 잡힘 | Formation rate-limited 상태에서 *말단 slope를 대사체 자신의 slope로 오해*. 모약물의 잔향이 대사체 라벨을 입은 결과. Separate metabolite IV 또는 model-based formation rate fixing이 필요. | M11 (Rate-limiting step) |
| **DS-3** | Renal Covariate Asymmetry | 대사체의 CrCl power coefficient가 1.0에 가깝고 모약물의 power는 작은 비대칭 | 대사체가 거의 신배설 ($f_e(m)\approx1$)인데 모약물의 $f_e$는 작은 시나리오 — Tozer Scenario (3)의 직접 신호. 활성 대사체 신장애 위험이 parent-only 보정으로는 검출되지 않음. | M14 (Renal impairment + active metabolite) |
| **DS-4** | Permeability Rate-Limited Mismatch | hepatic clearance covariate로 $f_u$를 넣었으나 모든 cohort에서 비유의/계수 ≈ 0; IVIVE에서 $CL_{int}$만 5–10배 underestimate | 수송체 기질에서 $\rho<1$ 상태. $f_u$보다 uptake permeability/transporter genotype이 dominant covariate일 가능성 — 기본 well-stirred의 rapid equilibration 가정이 무너짐. | M9, M10 (Permeability/Extended clearance) |

### §8E. NONMEM/PopPK 구현 교량(Implementation Bridge)

| 원전 개념 | PopPK 구현 시사점 |
|---|---|
| $CL=CL_R + CL_H + CL_{other}$ | 신기능 covariate를 total $CL$에 무차별 적용하지 말고 경로별 구성요소에 적용합니다. |
| $CL_R=f_e\cdot CL$ | 소변 데이터 또는 외부 $f_e$ 정보가 없으면 신장 분율을 과해석하지 마세요. |
| PK5 혈장+소변 동시 적합 | `DVID`/endpoint별 잔차오차로 혈장과 소변 데이터를 동시에 적합합니다. |
| $CL_b=CL\cdot C/C_b$ | 간 추출 또는 PBPK 입력에는 혈액 기준 청소율을 사용합니다. |
| well-stirred + App.E $\rho$ | 수송체 기질에서는 $CL_{int}$ covariate보다 uptake/permeability covariate 가능성을 먼저 점검합니다. |
| $AUC(m)/AUC=f_m\cdot CL/CL(m)$ | 대사체 모델에서 $f_m$, $CL(m)$, $V(m)$을 따로 추정할 수 있는지(identifiability)를 투여 경로/용량/대사체 데이터로 확인합니다. |
| 율속단계(rate-limiting step) | 대사체 말단 slope를 곧바로 대사체 자신의 $t_{1/2}$로 쓰지 마세요. |
| 신부전 활성 대사체 | 모약물과 대사체의 통합 노출을 라벨/용량 시나리오 민감도로 계산합니다. |

### §8F. 한 페이지 요약(One-page Recap)

1. $CL$은 농도로 정규화한 제거 능력입니다 — 제거 속도 자체가 아닙니다 [G&W p.49; R&T pp.124–128].
2. $t_{1/2}$은 $V/CL$에서 파생된 결과값입니다. $CL$과 $V$를 먼저 분해하지 않고 $t_{1/2}$만 해석하지 마세요 [R&T pp.148–150].
3. $CL_R=f_e\cdot CL$이지만, 신장 청소율 자체는 여과 + 분비 − 재흡수이며, urine pH와 flow가 이 값을 변화시킵니다 [G&W pp.48–56; R&T pp.138–148].
4. Well-stirred 간 청소율은 $Q_H$, $f_{ub}$, $CL_{int}$가 결정합니다. 고추출/저추출은 극한 근사값이지, 약물에 영구히 붙는 라벨이 아닙니다 [G&W pp.79–85; R&T pp.130–135].
5. 장기 추출 계산에서 plasma 농도는 blood 농도로 변환해야 합니다. App.D가 이 변환의 질량수지 다리를 제공합니다 [R&T App.D pp.775–776].
6. IVIVE는 in vitro 입력이 이미 정보를 잃었을 때 실패합니다 — single-point $CL_{int}$, 부적절한 scaling, permeability/transporter 항 누락이 대표적입니다 [G&W pp.85–90; R&T pp.136–138; R&T App.E pp.778–779].
7. Parent–metabolite 시스템은 $f_m$, $CL(m)$, 율속단계를 따로 파악해야 합니다. $AUC(m)/AUC$는 $f_m$ 그 자체가 아닙니다 [R&T pp.659–665].
8. 신부전 용량 조정은 모약물 $f_e$만이 아니라, 활성 대사체 청소율을 별도로 평가해야 합니다 [R&T pp.673–679].

---

<!--
## v3.8 출력 후 자가검증 체크리스트

| 항목 | 기준 | 결과 |
|---|---|---|
| SLIDE_START 개수 | §섹션수 + 카드수 합산 | 19 개 |
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
- 활자량 감축: v3.7 1335 줄 / 98611 자 → v3.8 1187 줄 / 87393 자 (감축률 약 11.4%)
  · 비고: 사양 §2.3의 40–55% 목표는 v3.7 원본의 metacontent 비중을 가정한 수치이나, 이 v3.7 파일은 §1.5 항법 오버레이·[EXPERT_INFERENCE]·[TEXTBOOK_DERIVED] 태그·"확인 시점/학습 지시"·HTML 코멘트를 합쳐도 전체의 약 11%에 머무릅니다. 사양 §3 HARD PRESERVE를 어기지 않는 한도에서 도달 가능한 한계입니다.
- 보존 감사 (100% 일치):
  · SLIDE_START 마커 20 = 20
  · LaTeX 수식 블록($$ 줄 기준) 72 = 72
  · §2 M카드 14 = 14, §5 혼동 쌍 10 = 10, §7 자기검증 9 = 9
  · 약물명·수치 앵커(methamphetamine 70-80%/1-2%, phenytoin 300→500 mg/day, propranolol 20 mg, morphine 11.7/5 mg, GFR 120 mL/min, Q_H 81 L/h, Tozer 0.27+0.24=0.51 mg/L / dose ratio 0.14 등) 100%
  · 출처 앵커: T5/G/T20/TD/TE 페이지 범위 100% 보존(일부 인접 인용은 단일 괄호로 통합되었으나 페이지 커버리지는 동일)
- 주요 변환 통계:
  · 메타 문구 제거: TEXTBOOK_DERIVED 9건 / EXPERT_INFERENCE 7건 / "확인 시점" 5건 / HTML 코멘트 3건 / "이 자료의 활용법" 1건 / "byte-level" 1건 / "Audit SHOULD_FIX" 1건 → 0건
  · 자기참조 즉해: "Mn의 결론이 ~한다" 형태 전건 → 결론 인라인 + 괄호 포인터로 치환
  · 약물 예시 즉맥락화: alfentanil/rifampin, alprenolol/pentobarbital, fentanyl/ritonavir, phenytoin, clofibric acid, methylprednisolone hemisuccinate, tolbutamide, propranolol/naphthoxylactic acid, morphine/M6G, isoproterenol, N-desalkylhalazepam, carbamazepine — 분류 인라인 + "→ 그래서 [개념]의 사례" 적용
  · §1.5 단순화: 60줄 항법 오버레이(A/B/C/D 분기) → 26줄 4-좌표 표 + 5카드 빠른 경로
  · 콜아웃 단일화: 카드당 💡+⚠️ 중복 통합, 💡 비유 → 🔑 본문 콜아웃에 흡수, 카드당 콜아웃 ≤6 유지
  · 금지 표현 변환: "축을 닫는다/측정 교량/분기된다/그림자/식별성/비대칭성/원칙 고정/추출률 분류/혈류 천장/3축 판독법/figure-derived 추정/항법 패치/시사한다/도출된다/풀어야 합니다/압축한다/가설화한다/clinically relevant" 등 30+ 항목 일괄 치환
  · M14 거장의 시각: 💢/✅/🎯 3-emoji 블록 → 단일 2문장 박스로 통합
-->

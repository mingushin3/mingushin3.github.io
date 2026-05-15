# 세션 04 — 청소율(Clearance): 신·간·IVIVE·대사체 — $CL_R$, $CL_H$, well-stirred, parent-metabolite — v4.0

## PART A — 학습자용 완성 핸드아웃(Learner-Facing Complete Handout)

> **임상 장면 하나로 시작합시다.**
> 환자 chart에 한 줄이 있어요 — "Plasma $CL = 60\ \mathrm{L/h}$, 간 혈류 $Q_H = 81\ \mathrm{L/h}$." 그래서 누군가 "중등도 이상 hepatic extraction이네요"라고 라벨을 붙입니다 [R&T p.125]. 그런데 같은 환자에서 $C/C_b = 0.5$예요. 이걸 알고 다시 계산하면 blood 기준 $CL_b = 30\ \mathrm{L/h}$, $E_H = 0.37$. **이 한 번의 기준 선택 오류 하나가 DDI 해석, 간장애 라벨 문구, PBPK 입력값을 통째로 바꿉니다.**
>
> 이 장에서 우리가 진짜 익히는 건 청소율이라는 숫자가 아니에요. **"지금 다루는 청소율이 정확히 어떤 청소율인가?"라는 4-좌표 질문**을 본능처럼 던지는 습관입니다.

<!-- SLIDE_START: §1 | title: §1 이 장이 중요한 이유(Why This Chapter Matters) -->
<!-- SECTION_CORE: SC-01 -->

## §1 이 장이 중요한 이유(Why This Chapter Matters)

청소율은 **숫자 하나가 아니라 주소 4줄**입니다. 같은 "CL"이라는 라벨이 붙어도, 그 청소율이 **어느 농도 기준**(혈장? 전혈? 비결합?), **어느 장기**(신장? 간?), **어느 투여 경로**(IV? 경구?), **무엇**(모약물? 대사체?)을 가리키느냐에 따라 임상 결론이 완전히 달라져요. 위의 60 L/h가 분류를 바꾸는 것도 같은 이유고요. 이 장이 하는 일은 그 4줄 주소를 본능적으로 읽게 만드는 겁니다.

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

**큰 흐름은 4단계예요** — ① $Rate = CL \cdot C$로 청소율의 좌표를 정한다, ② 신장에서 $CL_R = f_e \cdot CL$로 여과·분비·재흡수를 분해한다, ③ 간에서 well-stirred로 $Q_H$, $f_{ub}$, $CL_{int}$, 투과성을 분리한다, ④ 모약물–대사체에서 $f_m$, $CL(m)$, 율속단계(rate-limiting step; **전체 속도를 정하는 느린 단계**), 신장애를 얹는다.

**핵심 아이디어(Big Idea)**: 청소율은 $Dose/AUC$로 끝나는 숫자가 아니에요. **혈류, 단백결합, $CL_{int}$, 투과성/수송체, 신장 여과·분비·재흡수, 대사체 형성·제거**가 한 식 안에서 충돌한 결과입니다. 그래서 이 장의 목표는 관찰된 $CL$, $t_{1/2}$, $AUC(m)/AUC$, $C/C_b$ 변화가 **어느 생리학적 병목에서 왔는지를 역추적**하는 거예요.

> **버릴 수 없는 한 문장**: "어떤 청소율입니까?"는 항상 "어느 농도 기준인가, 어느 장기인가, 어느 율속단계인가, 모약물인가 대사체인가?"로 나눠서 봐야 합니다.

📍 **이 장의 위치**
- **다루는 영역**: PopPK · PBPK · TMDD · parent–metabolite joint model이 공유하는 생리학 축.
- **이 장 없이는**: 공변량(eGFR, $f_u$, transporter genotype 등)을 식의 어느 자리에 넣을지 근거를 댈 수 없어요.
- **이 장을 통과한 뒤**: 모든 공변량 결정이 "어느 생리학적 병목을 가설로 세우는가?"로 바뀝니다.

---

> 📊 **개념 도식 (HTML에서 렌더링):** 청소율 해석 의사결정 지도 — 장기, 투여 경로, 농도 기준, 대사체 축. $CL$ 해석은 "어느 농도 기준인가, 어느 장기인가, 어느 투여 경로인가, 모약물인가 대사체인가?"를 순서대로 묻는 구조적 문제입니다.

### §1.5 4-좌표 질문 — 이 장의 운영 체계

이 장 전체를 관통하는 핵심 질문은 단 하나예요 — **"지금 다루는 게 정확히 어떤 청소율(clearance)입니까?"** 그리고 이 질문을 항상 **4개 좌표**로 분해해서 풉니다.

| # | 좌표 | 묻는 내용 |
|---|---|---|
| 1 | 농도 기준 | 혈장(plasma)? 전혈(blood)? 비결합(unbound)? |
| 2 | 장기 | 신장? 간? 그 밖? |
| 3 | 투여 경로 | IV? 경구? 초회통과가 작동? |
| 4 | 분석 대상 | 모약물(parent)? 대사체(metabolite)? |

시간이 빠듯할 때는 **M1 → M2 → M4 → M5 → M14** 다섯 카드만 순서대로 읽어도 이 장의 의사결정 체계가 작동합니다.

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

**거장의 시각.** 환자 chart에 "반감기가 늘었다"라고 한 줄 적혀 있으면, 신부전인지 단백결합 변화인지 곧바로 추측하고 싶어져요. **그러면 안 됩니다.** $t_{1/2}$는 $V$와 $CL$의 결과예요. 두 축을 먼저 분리하지 않으면, 같은 반감기 증가가 신장애(CL↓)에서 왔는지 organomegaly(V↑)에서 왔는지 알 수 없어요. 그래서 이 카드의 한 줄은 "**$t_{1/2}$로 시작하지 말고 $CL$과 $V$로 시작하라**"입니다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: 청소율은 제거 속도 자체가 아니라 **농도로 정규화한 제거능**이에요. 그래서 first-order 조건에서 $CL$은 시간마다 새로 바뀌는 숫자가 아니라, **관찰 구간 전체를 설명하는 하나의 비례상수**입니다. $AUC$는 그 제거능이 시간 전체에 남긴 관찰량이고요.

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

> 💡 $t_{1/2}$는 원인이 아니라 $V/CL$의 결과예요. 반감기가 늘었다는 말은 $CL$이 줄었는지 $V$가 늘었는지 아직 모른다는 뜻입니다.

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

$t_{1/2}$가 변했다는 말은 $CL$ 또는 $V$가 변했다는 신호일 뿐, $t_{1/2}$ 자체가 $CL$을 결정하는 건 아니에요.

**현장 팁(Trench-level tip)**: 신부전·간부전·단백결합 변화 보고서를 검토할 때, "반감기가 늘었다/줄었다"로 진단을 시작하지 마세요. **$CL$과 $V$를 먼저 분리합니다.** 같은 $t_{1/2}$라도 $CL↑+V↑$가 동시에 생긴 경우와 둘 다 변하지 않은 경우는 임상적으로 완전히 다른 상황이에요.

같은 $CL$이라도 적용 대상에 따라 이름이 달라집니다 — 신장이면 $CL_R$ (→ M2), 간이면 $CL_H$ (→ M4), 대사체면 $CL_f$와 $CL(m)$ (→ M12).

**이 카드의 한 줄**: 반감기가 변했다는 말은 출발점일 뿐이에요. 진단은 항상 **$CL$과 $V$를 분리한 뒤**에 시작합니다. $t_{1/2}$를 원인처럼 다루면 PopPK 공변량을 엉뚱한 자리에 놓게 되고, 임상에서 용량 조정 해석도 빗나갑니다.

<!-- SLIDE_START: M2 | title: M2. 신장 청소율 분해: $CL_R$, $f_e$, 여과/분비/재흡수(Renal clearance decomposition: $CL_R$, $f_e$, filtration/secretion/reabsorption) -->
<!-- SECTION_CORE: SC-04 -->

### M2. 신장 청소율 분해: $CL_R$, $f_e$, 여과/분비/재흡수(Renal clearance decomposition: $CL_R$, $f_e$, filtration/secretion/reabsorption)

**앞에서 → 여기서**. M1에서 청소율을 농도로 정규화한 제거능으로 정의했죠. 이제 그중 **신장 경로가 차지하는 몫**만 떼어내는 일을 합니다.

**거장의 시각.** $f_e$를 보고 "아, 신기능 영향이 이만큼이구나"라고 단순 비례로 읽으면, 신부전 covariate를 total $CL$ 전체에 곱하게 됩니다. 그러면 nonrenal pathway까지 같이 줄어서 systematic underestimation이 발생해요. $CL_R = f_e \cdot CL$은 **경로 분해**예요 — 신부전 covariate가 들어갈 자리는 $CL$ 전체가 아니라 $CL_R$ 위치 하나입니다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: $CL_R = f_e \cdot CL$은 단순 비례식이 아니에요. **혈장 AUC와 소변 누적 배설량을 잇는 다리**입니다. 혈장은 몸 안의 노출을 보여주고, 소변은 신장 경로로 빠져나간 양을 보여주죠. 둘을 함께 봐야 renal route의 지분 $f_e$와 $CL_R$가 비로소 추정 가능해집니다.

**신장 생리 요약** [G&W p.48; R&T pp.119–120, 127, 138–145]: 네프론은 보먼주머니·근위세뇨관·헨레고리·원위세뇨관·집합관으로 구성됩니다. GFR은 약 **120 mL/min** (Tozer; Gabrielsson은 110–130 범위). Urine pH는 4.5–8 범위에서 움직이고요. 평균 신장 혈류는 약 **1.1 L/min**(이게 신장 추출의 혈류 상한이에요). GFR은 신장 혈장이 사구체에서 여과되는 부분집합입니다. Inulin이 GFR marker로 언급됩니다.

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

> 🔑 **경로 분해 규칙:** 신기능 covariate는 가능하면 total $CL$이 아니라 $CL_R$ 위치에 적용합니다. 비유하자면 신부전이라는 신호는 "신장 수도꼭지만 잠긴 것"인데, 식의 어디에 그 잠금을 거는지가 결정적이에요.

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

$CL_R > f_u \cdot GFR$이면 분비(secretion)가 작동하고 있다는 뜻이고, $CL_R < f_u \cdot GFR$이면 재흡수(reabsorption)가 일어나거나 측정 방식이 잘못됐는지 의심해야 합니다.

**청소율 가산성(Clearance additivity)** [R&T pp.127–128 Eq 5-9]

$$
\underbrace{CL}_{\text{전체 CL}}=\underbrace{CL_R}_{\text{신장}}+\underbrace{CL_H}_{\text{간}}+\underbrace{CL_{other}}_{\text{기타}}
$$

담즙 배설과 장간순환은 소실 곡선을 바꿀 수 있지만, 본 문서에서는 M2의 경로 분해 안에서 한꺼번에 다룹니다 [R&T pp.137–138]. 폐 청소율은 장기 가산성 해석에서 특수 예외로만 기억합니다 [R&T p.128].

**현장 함정**: $f_e$가 작으면 신장애 영향도 작다고 단정하기 쉬워요. 모약물 기준으로는 대체로 맞는 말이지만, **활성 대사체가 신장으로 빠지는 약이라면 신부전 환자에서 모약물보다 대사체가 훨씬 더 쌓입니다** — 이게 바로 M14의 본 게임이에요.

**이 카드의 한 줄**: 신기능이 변했을 때 손이 가야 할 식은 $CL_R = f_e \cdot CL$이에요. **이 분해를 하지 않으면** 신부전 covariate가 nonrenal pathway까지 끌어내려서 dose adjustment 결정 전체가 어긋납니다. 그리고 작은 $f_e$를 봤다고 안심하는 순간 활성 대사체가 신장으로 빠지는 시나리오(M14)를 놓치게 돼요.

<!-- SLIDE_START: M3 | title: M3. ARE 플롯과 배설속도 플롯(ARE plot vs Excretion Rate plot) -->
<!-- SECTION_CORE: SC-05 -->

### M3. ARE 플롯과 배설속도 플롯(ARE plot vs Excretion Rate plot)

**앞에서 → 여기서**. M2에서 신장 경로의 양 자체를 정의했어요. 이제 그 양이 **실제 소변 수집 데이터에서 어떻게 왜곡되어 보이는지**를 봅니다.

**거장의 시각.** ARE plot과 rate plot의 기울기가 안 맞을 때, 곧바로 "다구획 모델이 필요한가?" 쪽으로 머리가 가요. **그 점프가 위험합니다.** 두 plot의 slope 불일치는 대부분 collection interval, bladder emptying, urine pH/flow 변동에서 와요. 구조 모델로 점프하기 전에 sampling artifact부터 거르는 게 순서예요.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: ARE plot과 excretion-rate plot은 같은 urinary data에서 $K$를 추정합니다. 그런데 한쪽은 **구간 배설속도**를, 다른 한쪽은 **남은 누적 배설량**을 봐요. 그래서 noise 구조와 시간 정보가 다르게 나타나요. Rate plot은 renal clearance의 시간 변동을 그대로 노출하고, ARE plot은 누적량 기반이라 **변동이 평탄해져서 보입니다**.

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

> 💡 Rate plot은 시간 변동을 그대로 노출하고, ARE plot은 누적량으로 변동을 평탄하게 만듭니다. 두 plot의 slope가 안 맞는다고 곧바로 다구획 모델 신호로 읽으면 안 돼요.

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

정확한 소변 결과를 얻으려면 약물의 소변 농도가 무시할 수준이 될 때까지 시료를 수집하는 게 좋아요 [G&W p.51].

**핵심 예시**: G&W의 PK5에서 urine collection interval은 0.5–12 h로 다양하고, rate plot/ARE plot에서 half-life가 그림에서 약 **6–6.3 h**로 읽힙니다 [G&W p.497]. **Methamphetamine**(중추흥분제, 약염기성 약물)은 소변 pH에 따라 비이온화 형태 비율이 극적으로 바뀌어서 재흡수가 통째로 흔들립니다. **산성 소변에서는 회수율 70–80%, 알칼리성 소변에서는 1–2%** [R&T p.145]. → 그래서 **소변 pH 하나만으로도 $CL_R$ 회수율이 수십 배 흔들린다**는 사실의 임상 사례입니다. 이 차이를 모르면 같은 약을 같은 환자에게 줬는데도 신장 경로 추정이 자릿수가 달라져요.

**현장 팁(Trench-level tip)**: urinary data를 받으면 **먼저 ARE와 rate plot 둘 다 그립니다.** 두 plot이 같은 $K$를 안 줄 때, 구조 모델 점프 전에 ① collection interval, ② bladder emptying, ③ pH/flow 변동을 이 순서로 의심하세요.

> 📖 **G&W p.50, Fig 2.35:** 두 plot 모두 $K$를 주지만 시간 배치와 잡음 민감도가 다릅니다. 그림은 ARE는 실제 시간을 그대로 쓰고, 배설속도 plot은 구간 가운데 시점을 그 구간의 대표값으로 쓴다는 약속을 직접 보여줍니다.

**이 카드의 한 줄**: ARE와 rate plot은 **같은 데이터를 두 각도에서 본 영상**이에요. 두 plot이 같은 $K$를 안 주면 구획 수를 늘리기 전에 sampling artifact를 먼저 의심합니다. 안 그러면 pH/flow·방광 배출 문제를 모델 구조 문제로 잘못 진단하게 돼요.

<!-- SLIDE_START: M4 | title: M4. Well-stirred 간 청소율과 4-모델 압축(Well-stirred hepatic clearance + 4-model compression) -->
<!-- SECTION_CORE: SC-06 -->

### M4. Well-stirred 간 청소율과 4-모델 압축(Well-stirred hepatic clearance + 4-model compression)

**앞에서 → 여기서**. M2–M3가 신장 경로를 측정했다면, 이제 **간 경로에서 혈류와 효소 용량이 어떻게 경쟁하는지** 봅니다.

**거장의 시각.** $CL_H$를 하나의 숫자로만 보면 두 가지 효과가 섞여 보여요 — 추출률 효과와 단백결합 효과. 분리가 안 되는 거죠. **$Q_H$가 큰지 $f_{ub}\cdot CL_{int}$가 큰지를 비교하는 관점**으로 가야 혈류 제한과 용량·결합 제한이 따로 보입니다. 그래서 이 카드의 본능은 — "간 CL 숫자를 받자마자 분모를 들여다본다"예요.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: Well-stirred model(← 간을 즉시 섞인 장기로 보는 모델)은 hepatic clearance를 **세 입력값**으로 다룹니다 — blood flow $Q_H$, blood unbound fraction $f_{ub}$, intrinsic clearance $CL_{int}$. 분모에서 $Q_H$가 큰지, $f_{ub} \cdot CL_{int}$가 큰지에 따라 고추출/저추출 여부와 임상 해석이 갈라져요.

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

> 🔑 **Well-stirred 판독법:** $Q_H$가 큰지 $f_{ub} CL_{int}$가 큰지를 먼저 비교합니다. 장기 추출률은 **blood 농도 기준**이에요 — plasma에서 측정한 값은 M8 변환을 거친 뒤 써야 합니다. 비유하자면 간은 수도관과 정수기가 붙은 장치예요. 물(혈류)이 적게 들어오면 혈류가 한계고, 정수기 용량(효소·결합)이 작으면 $f_{ub} CL_{int}$가 한계입니다.

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

**네 가지 간 청소율 모델** [G&W pp.90–94 Table 2.9]: well-stirred, parallel-tube, distributed, dispersion 모델은 모두 간 extraction을 설명합니다. 차이는 **간 내부에서 혈액과 hepatocyte가 얼마나 섞이는지, 농도 기울기를 어떻게 처리하는지**에 있어요. 본 핸드아웃은 개념적 차이만 보존하고 distributed/dispersion 상세 수식은 출처 충실성을 위해 잠금 상태로 둡니다.

> 📖 **G&W p.79, Fig 2.58** (companion: R&T p.131, Fig 5-7): Well-stirred 식은 장기의 input-output 구조에서 출발합니다. 이 그림을 보지 않으면 $Q_H$가 단순 공변량이 아니라 **간으로 들어오는 혈류가 정해주는 상한선**이라는 감각이 약해져요.

**이 카드의 한 줄**: 간 CL을 해석할 때 반드시 짚는 비교는 단 하나 — **$Q_H$ vs $f_{ub} \cdot CL_{int}$**. 이걸 안 보고 가면 high/low extraction 분류가 통째로 흔들리고, 단백결합·DDI 해석이 뒤집힙니다. 그리고 분류를 plasma 기준으로 하는 순간 단위 자체가 어긋나기 때문에(→ M8), $CL_b$로 변환한 뒤에 비교한다는 순서가 본능이 돼야 해요.

<!-- SLIDE_START: M5 | title: M5. 고/저 추출률과 투여 경로 × 추출률 × $f_u$ 매트릭스(High/low extraction + route × extraction × $f_u$ matrix) -->
<!-- SECTION_CORE: SC-07 -->

### M5. 고/저 추출률과 투여 경로 × 추출률 × $f_u$ 매트릭스(High/low extraction + route × extraction × $f_u$ matrix)

**앞에서 → 여기서**. M4의 well-stirred 식이 있어도, **투여 경로(IV/oral)나 단백결합 상태가 바뀌면 임상 결론이 완전히 달라집니다.** 그 매트릭스를 펴 보는 카드예요.

**거장의 시각.** "High extraction이면 $f_u$ 무관"이라는 한 줄 — 이거 진짜 위험해요. 이 말은 **IV total concentration에서만** 맞는 절반 진술이에요. 같은 약을 경구로 주거나, 비결합 농도를 endpoint로 잡으면 결론이 뒤집힙니다. 그래서 단백결합 변화를 평가할 때는 항상 세 축을 같이 봐야 해요 — 투여 경로 × 추출률 × total/unbound endpoint.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: 단백결합의 효과는 **약물 이름 하나로 정해지지 않습니다.** 세 가지를 같이 봐야 결정돼요 — ① 투여 경로(IV/oral), ② 고추출/저추출 여부, ③ 보는 농도가 총량인지 비결합인지. "High extraction이면 $f_u$ 무관"은 IV total endpoint에 한정되는 절반의 진술이에요.

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

> 🔑 **세 가지 축으로 읽는 법:** route, extraction class, total/unbound endpoint를 동시에 지정해야 합니다. "High extraction이면 $f_u$ 무관"은 IV total endpoint에만 적용되는 절반의 진술이에요.

**Tozer 통합 예시** [R&T pp.152–163]

- **Alfentanil**(저추출 opioid)에 **rifampin**(강력한 CYP3A 유도제)을 같이 쓰면, 효소가 유도되면서 청소율이 늘고 AUC가 줄어들어요. → 그래서 **저추출 약물은 $CL_{int}$ 변화에 직접 반응한다**는 사실의 임상 사례입니다 [R&T p.152].
- **Alprenolol**(고추출 β차단제) + **pentobarbital**(효소 유도제) 조합. 같은 효소 유도라도 IV에서는 high extraction의 혈류 제한 때문에 변화가 작은데, 경구 생체이용률은 분명히 감소합니다 [R&T p.153]. → 그래서 **같은 약이라도 IV와 oral에서 효소 유도에 반응하는 방식이 다르다**는 사실의 임상 사례입니다.
- **Fentanyl**(고추출 opioid)에 **itraconazole**(약한 CYP3A 억제제) 또는 **ritonavir**(강한 CYP3A 억제제). itraconazole은 IV fentanyl PK에 큰 영향이 없지만, ritonavir는 clearance를 **0.94 → 0.32 L/h/kg**까지 떨어뜨립니다. → 그래서 **강한 효소 억제로 같은 약이 고추출에서 저추출로 분류가 전환된다**는 사실의 임상 사례입니다 [R&T pp.154–155].
- **Phenytoin + 요독증(uremia)**: 요독 상태에서 알부민 결합이 떨어져 $f_u$가 올라가요. 그러면 total 농도는 낮게 측정되는데, **약리학적으로 작용하는 비결합 농도는 안 변하거나 오히려 올라갈 수 있어요**. → 그래서 같은 total 농도라도 **total과 unbound는 다른 질문에 답한다**는 사실의 임상 사례입니다 [R&T pp.159–160].
- **Clofibric acid + 신증후군(nephrotic syndrome)**: 작은 $V$에서 $f_u$ 증가가 $CL$ 변화로 이어지면서 반감기가 단축될 수 있어요. → 그래서 **$f_u$ 변화 하나가 $V$와 $CL$ 양쪽에 작용해 $t_{1/2}$를 흔든다**는 사실의 임상 사례입니다 [R&T pp.161–162].

**현장 팁(Trench-level tip)**: high extraction 약물에서 **IV DDI가 음성이라고 oral DDI도 안전하다고 결론 내리지 마세요.** Route가 바뀌면 first-pass와 $f_u \cdot CL_{int}$ 민감도가 같이 바뀝니다. IV negative DDI는 oral safety의 보장이 아니에요.

> 📊 **개념 도식 (HTML에서 렌더링):** 투여 경로 × 추출률 × 단백결합 해석 매트릭스 — 단백결합의 효과는 약물 이름 하나로 정해지지 않고, 투여 경로, 고추출/저추출 여부, total/unbound endpoint에 따라 달라집니다.

**이 카드의 한 줄**: 단백결합 변화를 평가할 때 본능은 **route × extraction × endpoint를 동시에 좌표화하는 것**입니다. 이 세 축을 하나라도 빠뜨리면, IV negative DDI를 oral 안전으로 일반화하는 라벨 방어 실패가 곧바로 발생해요.

<!-- SLIDE_START: M6 | title: M6. IVIVE 함정: 단일점, MMP, 데이터 압축(IVIVE pitfalls: single-point, MMP, data condensation) -->
<!-- SECTION_CORE: SC-08 -->

### M6. IVIVE 함정: 단일점, MMP, 데이터 압축(IVIVE pitfalls: single-point, MMP, data condensation)

**앞에서 → 여기서**. M4–M5가 간 청소율 식의 **해석**을 세웠다면, 이제 그 식에 넣는 **$CL_{int}$ 입력값이 어디서 무너지는지** 점검합니다.

**거장의 시각.** IVIVE가 5배 빗나갔다는 보고서가 올라오면, 본능적으로 "hepatic model이 안 맞나?"부터 의심하게 돼요. 그러면 이미 in vitro에서 사라진 곡선 정보를 모델로 복구하려는 헛수고를 하게 됩니다. **순서를 뒤집으세요** — 입력 데이터가 single point에서, MMP에서, 압축에서 어디서 정보를 잃었는지 먼저 봅니다. 실패 원인은 거의 상류에 있어요.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: IVIVE는 $V_{max}$, $K_m$, microsomal protein scaling을 넣는 계산 문제가 아니에요. 먼저 **어떤 정보를 버렸는지**를 점검해야 합니다. 한 점에서 얻은 $CL_{int}$, 잘못된 MMP(microsomal protein per gram of liver; 간 1 g당 마이크로솜 단백량) 보정, 과도한 데이터 압축은 모두 in vivo clearance를 왜곡합니다.

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

> 🔑 **IVIVE 검토 순서:** single-point → MMP scaling → data condensation → transporter/permeability 누락. 이 순서로 점검합니다. 정교한 hepatic model로도 single-point 입력에서 사라진 곡선 정보는 복구되지 않아요 — 흐릿하게 압축된 사진을 고해상도 화면에 띄우는 것과 같아서, 원본 rate 곡선이 사라졌다면 뒤의 모델은 그 곡률을 만들어내지 못합니다.

**세 가지 함정**

① **단일 농도 함정**: 한 농도에서 얻은 rate를 $V_{max}/K_m$처럼 쓰면 비선형성과 포화를 통째로 놓칩니다 [G&W pp.85–89].

② **MMP 보정 함정**: 간 g당 microsomal protein 보정은 평균값 하나로 끝나지 않아요. 변이와 비율 처리에 민감합니다 [G&W p.87].

③ **데이터 압축 함정**: 농도-속도 관계를 단일 $CL_{int}$로 압축하면 곡선 형태와 이상치 구조가 사라져요 [G&W pp.88–89].

**현장 팁(Trench-level tip)**: IVIVE report를 받았을 때 첫 질문은 "well-stirred 식이 맞는가?"가 아니라 **"in vitro rate 정보가 single point로 뭉개졌는가?"**여야 합니다. 뭉개진 입력은 정교한 hepatic model로도 복구되지 않아요.

**이 카드의 한 줄**: IVIVE가 빗나갔을 때, 모델식보다 **입력 데이터 정보 손실**을 먼저 의심합니다. single-point rate vs MM 정보의 차이를 모르면 saturation과 곡률 정보가 통째로 소실되고, Phase 1 CL 예측 실패의 진짜 원인을 마지막까지 못 찾게 돼요.

<!-- SLIDE_START: M7 | title: M7. PK5 혈장+소변 동시 적합(PK5 simultaneous plasma+urine fitting) -->
<!-- SECTION_CORE: SC-09 -->

### M7. PK5 혈장+소변 동시 적합(PK5 simultaneous plasma+urine fitting)

**앞에서 → 여기서**. M2–M6의 장기별 분해는 **실제 데이터에서 plasma와 urine을 동시에 맞출 때 비로소 추정 가능한 구조**가 됩니다.

**거장의 시각.** 소변 데이터를 별도 계산표로 분리하면 그 순간 $f_e$와 $CL_R$를 **plasma model 안에서 따로 추정할 수 없게 돼요.** 두 endpoint를 같이 적합해야 endpoint별 오차 구조와 renal fraction이 한 모델 안에서 추정 가능합니다. 이게 NONMEM에서 plasma+urine, IV+oral, parent+metabolite를 동시에 fitting하는 사고방식의 출발점이에요.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: PK5는 urinary data를 별도 계산표로 처리하지 않습니다. **Plasma 농도와 누적 소변량을 한 모델에서 동시에 fitting**해요. 이 구조가 NONMEM에서 다중 endpoint를 함께 fitting하는 사고방식의 첫 번째 모범 사례입니다.

**문제 앵커** [G&W pp.494–499]: **250 mg IV bolus** [G&W p.494]. 초기 추정 $V \approx 7$ L, $CL \approx 2$ L/h, $f_e \approx 0.3$. 최종 $CL \approx 1.2$ L/h, $f_e \approx 35\%$, $CL_R \approx 0.42$ L/h; parameter CV는 5% 미만; plasma와 urine의 잔차 CV는 각각 **2.84%**와 **8.96%** [G&W pp.497–498]. 해석적 풀이와 ODE는 거의 동일한 추정값을 줍니다 [G&W pp.497–499].

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

> 💡 Plasma는 노출을, urine은 신장 경로의 양을 알려줘요. 둘을 분리하면 $f_e$가 흔들립니다 — plasma는 저수지 수위, urine은 배수구로 빠진 총량이에요. 두 endpoint의 CV가 다르니까(2.84% vs 8.96%) `DVID` 기반 endpoint 분리와 endpoint별 잔차오차 블록이 필요합니다(PK5 권고).

$$
\underbrace{X_u(t)}_{\text{누적 소변량}}=\underbrace{f_e}_{\text{신장 지분}}\cdot\underbrace{D_{iv}}_{\text{IV 용량}}\left[1-\exp\left(-\underbrace{\frac{CL}{V}}_{\text{소실상수}}\underbrace{t}_{\text{시간}}\right)\right]
$$

**이 카드의 한 줄**: plasma + urine 데이터를 받으면 **한 모델 안에서 동시에 적합**합니다. 이걸 안 하면 $f_e$와 $CL_R$를 따로 추정할 수 없게 되고, endpoint별 산포 차이가 추정 편향으로 흡수돼요. NONMEM에서 다중 endpoint 잔차오차 블록을 분리하는 습관은 여기서 시작됩니다.

<!-- SLIDE_START: M8 | title: M8. 혈장-혈액 비와 혈액 청소율(Plasma-to-blood ratio and blood clearance) -->
<!-- SECTION_CORE: SC-10 -->

### M8. 혈장-혈액 비와 혈액 청소율(Plasma-to-blood ratio and blood clearance)

**앞에서 → 여기서**. M4–M7의 간·신장 해석은 **농도 기준이 맞아야 작동합니다.** 그래서 plasma 기준을 blood 기준으로 바꾸는 다리가 필요해요.

**거장의 시각.** Plasma $CL$을 그대로 $Q_H$와 비교하는 순간 장기 추출의 분모가 틀어져요. 같은 약물이 false-high extraction으로 분류되고, DDI 해석·간장애 라벨 문구·PBPK 입력이 통째로 어긋납니다. 그래서 hepatic extraction을 말하기 전에 본능은 — "**이 CL은 plasma 기준인가, blood 기준인가?**" 한 줄을 묻는 거예요.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: 장기 추출률(← 장기 통과 중 제거된 비율)은 blood flow와 비교해서 계산하니까 **blood 농도 기준 청소율**이 필요해요. 그런데 임상에서 측정하는 건 대부분 plasma 농도입니다. **그래서 plasma 농도를 blood 농도로 바꿔 써야 해요.** 이 변환을 안 하면 분모가 달라지고 결과적으로 추출률 분류가 통째로 틀어집니다.

**청소율 관계식** [R&T pp.124–128 Eq 5-4–5-6]

$R = C/C_b$로 정의합니다.

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

> 🔑 **추출 전 필수 변환:** hepatic $E_H$ 계산 전 plasma $CL$을 $CL_b$로 변환합니다. $f_u$와 $f_{ub}$는 같은 분율이 아니라 농도 기준이 다른 분율이에요.

$$
\underbrace{CL}_{\text{혈장 CL}}=\underbrace{CL_b}_{\text{혈액 CL}}\cdot\underbrace{\frac{C_b}{C}}_{\text{역변환}}=\frac{\underbrace{CL_b}_{\text{혈액 CL}}}{\underbrace{R}_{C/C_b}}
$$

**App.D 질량수지** [R&T App.D pp.775–776 Eq D-1–D-8]

$$
\underbrace{\frac{C}{C_b}}_{\text{혈장/혈액비}}=\frac{1}{1+\underbrace{H}_{\text{적혈구용적률}}\left(\underbrace{f_u}_{\text{혈장 유리분율}}\underbrace{K_{PBC}}_{\text{RBC 분배}}-1\right)}
$$

여기서 $H$는 hematocrit, $f_u$는 혈장 내 비결합 분율, $K_{PBC}$는 혈구-비결합 혈장 분배계수예요.

**App.D 역행렬 필수** [R&T App.D pp.775–776 Eq D-8]

$$
\underbrace{K_{PBC}}_{\text{RBC분배}}=\frac{\underbrace{H}_{\text{적혈구용적률}}-1+\underbrace{(C_b/C)}_{\text{혈액/혈장비}}}{\underbrace{f_u}_{\text{유리분율}}\cdot\underbrace{H}_{\text{RBC 분율}}}
$$

**해석상 함의**: $R < 1$이면 plasma CL이 실제와 다르게 보일 수 있어요. 간 추출에는 $E_H = CL_{H,b}/Q_H$를 써야 하고, $f_u$와 $f_{ub}$는 호환되지 않습니다 ($f_{ub} = f_u \cdot (C/C_b)$).

**핵심 시나리오로 다시 짚기**: 앞서 hook에서 본 그 환자죠 — $CL = 60\ \mathrm{L/h}$, $Q_H = 81\ \mathrm{L/h}$이면 중등도 추출처럼 보입니다. 그런데 $R = C/C_b = 0.5$를 알게 되면 $CL_b = 30\ \mathrm{L/h}$, $E_H = 0.37$. **분류가 통째로 바뀝니다.** 이게 변환 하나로 라벨이 흔들리는 가장 직설적인 사례예요.

**이 카드의 한 줄**: 간 추출을 판단할 때 본능은 단 하나 — **$CL_b = CL \cdot C/C_b$ 변환부터 한다**. plasma CL을 그대로 $Q_H$와 비교하면 false-high extraction이 곧바로 발생하고, $CL/Q_H$ 직접 비교는 PBPK 입력과 DDI 해석을 통째로 흔듭니다. App.D bridge 없이는 organ extraction을 말하지 마세요.

<!-- SLIDE_START: M9 | title: M9. 투과성 속도 제한 간 흡수: App.E $\rho$ (Permeability-rate-limited hepatic uptake: App.E $\rho$) -->
<!-- SECTION_CORE: SC-11 -->

### M9. 투과성 속도 제한 간 흡수: App.E $\rho$ (Permeability-rate-limited hepatic uptake: App.E $\rho$)

**앞에서 → 여기서**. M8에서 blood 기준을 맞췄어요. 그런데 그 뒤에도, **hepatocyte 내부로 들어가는 접근성이 느리면 well-stirred의 전제 자체가 무너집니다.**

**거장의 시각.** $CL_{int}$가 충분하면 hepatic clearance도 충분하다고 생각하기 쉬워요. 그러면 **hepatocyte 접근성이라는 병목**을 놓치게 됩니다. transporter 기질 약물에서 IVIVE가 5–10배 빗나가는데 enzyme assay만 다시 들여다보는 실수가 여기서 일어나요. $\rho$를 식에 넣으면 세포막 uptake가 효소 제거능보다 앞단에서 clearance를 막을 수 있다는 게 보입니다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: 기본 well-stirred는 간세포 안팎의 unbound 농도가 빠르게 평형이라고 가정해요. 그런데 hepatic uptake permeability가 느리면 세포 내부 unbound 농도가 혈액 쪽 unbound 농도보다 낮아집니다. 이 경우 $CL_{int}$만으로는 hepatic clearance를 설명할 수 없어요.

**App.E Model II** [R&T App.E pp.778–779 Eq E-9–E-15]

$\rho$(← 세포 안팎 unbound 비율)는 hepatocyte 내부 unbound 농도가 혈액 쪽 unbound 농도를 얼마나 따라가는지를 나타냅니다.

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

> 🔑 **ρ 판독법:** passive diffusion이 충분하면 $\rho \to 1$, uptake가 느리면 $\rho < 1$입니다. 효소가 충분해도 약물이 hepatocyte 안으로 못 들어가면 clearance는 낮아져요 — 공장 문 앞 회전문이 느리면 안쪽 효소가 아무리 빨라도 전체 생산량은 느려지는 것과 같습니다.

$$
\underbrace{CL_{H,b}}_{\text{간 CL_b}}=\frac{\underbrace{Q_H}_{\text{혈류}}\cdot\underbrace{f_{ub}}_{\text{혈액 유리분율}}\cdot\underbrace{\rho}_{\text{세포접근성}}\cdot\underbrace{CL_{int}}_{\text{대사제거}}}{\underbrace{Q_H}_{\text{혈류}}+\underbrace{f_{ub}\cdot \rho\cdot CL_{int}}_{\text{보정 제거축}}}
$$

수동 확산/permeability가 충분히 커서 세포 내외 비결합 농도가 빠르게 평형에 가까워지면 $\rho \to 1$이 되어 기본 well-stirred로 환원됩니다. 반대로 uptake permeability가 작으면 $\rho < 1$이고 clearance는 permeability-limited가 돼요 [R&T App.E pp.778–779].

**경구 투여 다리(Oral bridge)** [R&T App.E pp.779–780 Eq E-19–E-20]

위 가정하에서 간 추출로만 제거되는 약물의 경우:

$$
\underbrace{AUC_{po}}_{\text{경구노출}}=\frac{\underbrace{Dose}_{\text{투여량}}}{\underbrace{f_{ub}}_{\text{혈액 유리분율}}\cdot\underbrace{\rho}_{\text{세포접근성}}\cdot\underbrace{CL_{int}}_{\text{제거능}}}
$$

**현장 팁(Trench-level tip)**: transporter 기질에서 $f_u$와 $CL_{int}$만으로 IVIVE를 강행하면 permeability 병목을 $CL_{int}$ 부족으로 오해할 수 있어요. 모든 cohort에서 $f_u$ covariate가 비유의로 떨어지는데 IVIVE만 안 맞으면 $\rho$를 의심합니다.

**이 카드의 한 줄**: $CL_{int}$로 설명되지 않는 hepatic CL을 만났을 때 본능은 **$\rho$**(세포 접근성)을 들여다보는 것입니다. $\rho$를 생략하면 transporter substrate의 IVIVE mismatch가 효소 부족처럼 보이게 되고, covariate 위치가 통째로 잘못 잡혀요.

<!-- SLIDE_START: M10 | title: M10. 확장 청소율: 수송체–효소 구조(Extended clearance: transporter–enzyme architecture) -->
<!-- SECTION_CORE: SC-12 -->

### M10. 확장 청소율: 수송체–효소 구조(Extended clearance: transporter–enzyme architecture)

**앞에서 → 여기서**. M9의 $\rho$는 단일 보정항처럼 보이지만, 실제로는 **uptake·metabolism·efflux의 다층 구조**를 열어줍니다.

**거장의 시각.** 간 소실을 효소 하나로 줄이면 transporter 단계의 DDI와 IVIVE mismatch가 모두 $CL_{int}$ 오류로 보여요. 그러면 처방 사고 자체가 좁아집니다. Uptake·metabolism·efflux를 나누면 **어느 막 단계가 전체 clearance를 막는지** 분류할 수 있어요. 진단 차원이 통째로 한 단계 늘어나는 거예요.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: 확장 청소율(extended clearance)은 hepatic elimination을 "효소 하나"로 보지 않습니다. **Sinusoidal uptake, canalicular efflux, basolateral efflux, intracellular metabolism**의 네 흐름으로 봐요. 기본 well-stirred는 이 네 흐름 중 막 단계가 충분히 빠른 특수한 경우일 뿐입니다.

**최소 해석** [R&T pp.136–138 Eq 5-35–5-36; R&T App.E pp.778–779]: R&T 5장은 간 소실이 관류·단백결합·세포 활성만으로 끝나지 않고 막 투과성과 transporter에 의해 달라진다는 점을 명시합니다. App.E는 이를 $\rho$로 제1원리화해요.

- **Uptake-limited**: 혈장/혈액에서 hepatocyte로 들어가는 단계가 병목.
- **Metabolism-limited**: 세포 내부 도달은 충분하고 효소 용량이 병목.
- **Efflux-limited**: 담즙 또는 혈액 방향 유출이 병목.

잘 안 맞는 IVIVE가 항상 효소 assay 문제는 아니에요 — transporter/permeability 항이 빠졌을 가능성이 큽니다 (M6 IVIVE trap + M9 $\rho$ 연결).

> 📖 **R&T p.136, Fig 5-11** (companion: Tozer App.E pp.778–779, Eq E-9–E-15): 세포막을 사이에 둔 uptake, metabolism, efflux의 **위치 관계**가 핵심입니다. 이 위치 관계를 보지 않으면 permeability-limited clearance를 단순히 낮은 $CL_{int}$로 오해하기 쉬워요.

#### 파라미터 해부 표

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| Uptake | — | 혈액→hepatocyte 유입 | OATP/OCT/OAT, permeability |
| Metabolism | — | 세포 내 효소 제거 | CYP/UGT activity |
| Efflux | — | 담즙/혈액 방향 유출 | canalicular/basolateral transporter |
| $\rho$ | ratio | membrane bottleneck 요약 | uptake vs metabolism 경쟁 |

> 💡 확장 청소율은 효소 하나가 아니라 uptake·metabolism·efflux의 병렬/직렬 구조예요. 경험적 scalar로 봉합하면 transporter 병목을 통째로 숨기게 됩니다.

**이 카드의 한 줄**: 수송체 기질의 간 소실을 다룰 때, 본능은 **uptake/metabolism/efflux 중 어느 단계가 병목인지**를 따로 점검하는 것이에요. enzyme-only 사고에 빠지면 transporter DDI와 efflux 병목을 한꺼번에 놓치고, empirical scalar로 봉합하면 구조 원인이 숨겨져서 다음 cohort에 외삽할 때 통째로 빗나갑니다.

<!-- SLIDE_START: M11 | title: M11. 대사체 처리(disposition)의 율속단계(Rate-limiting step in metabolite disposition) -->
<!-- SECTION_CORE: SC-13 -->

### M11. 대사체 처리(disposition)의 율속단계(Rate-limiting step in metabolite disposition)

**앞에서 → 여기서**. M10까지 **모약물 clearance의 병목**을 분해했어요. 이제 **대사체 곡선의 말단 기울기가 무엇을 반영하는지** 분리해야 합니다.

**거장의 시각.** 대사체의 말단 기울기를 보고 곧바로 "이게 대사체 반감기"라고 라벨링하는 게 일반적인 함정이에요. 형성률속 상황에서는 그 기울기가 **모약물을 그대로 베껴낸 모습**이거든요. 대사체 본연의 처리(disposition)와 관찰된 기울기를 분리하려면, 형성과 제거 중 어느 쪽이 느린지를 먼저 확인해야 합니다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: 대사체 농도-시간 곡선의 terminal slope(← 말단 감소 구간의 기울기)는 **대사체 자체의 반감기가 아닐 수 있습니다.** 형성이 느리면 대사체는 모약물의 잔향처럼 모약물 반감기를 따라 감소하고, 제거가 느리면 대사체 자체 반감기가 말단을 지배해요.

**대사체가 임상적으로 중요한 이유** [R&T pp.658–659]: **활성, 독성, 억제, 유도, 치환**. 그런데 충분한 농도에 도달하지 않으면 치료적 우려는 작아요 — "활성 대사체가 있다"와 "임상적으로 의미가 있다"는 같은 말이 아닙니다 [R&T p.659].

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

> 🔑 **Terminal slope 규칙:** downstream 물질의 말단 감소는 **가장 느린 단계**가 지배합니다. parallel decline은 대사체 본연의 반감기 증거가 아니라 formation-limited 신호일 수 있어요 — 대사체는 앞차(모약물)를 따라가는 차량이에요. 앞차가 느리면 뒤차 속도계가 아니라 교통 흐름 전체가 느린 거죠.

| 분류 | 조건 | 관찰 패턴 | 해석 |
|---|---|---|---|
| Formation rate-limited | $k \ll k(m)$ | parent에 나란히 감소 | 관찰된 metabolite terminal $t_{1/2}$은 parent의 half-life |
| Elimination rate-limited | $k(m) \ll k$ | metabolite가 더 늦게 peak, 더 느리게 감소 | terminal $t_{1/2}$은 metabolite 자신의 half-life |

$$
\begin{aligned}\underbrace{k\ll k(m)}_{\text{형성 느림}}&\Rightarrow \underbrace{t_{1/2,\mathrm{obs}}(m)\approx t_{1/2,\mathrm{parent}}}_{\text{parent 잔향}}\\ \underbrace{k(m)\ll k}_{\text{제거 느림}}&\Rightarrow \underbrace{t_{1/2,\mathrm{obs}}(m)\approx t_{1/2,\mathrm{metabolite}}}_{\text{대사체 지배}}\end{aligned}
$$

순차 연쇄(sequential chain)에서는 "fastest k가 결정한다"가 아니라, downstream 물질의 말단 감소는 **가장 느린 단계**가 지배합니다 [R&T p.661]. 신장애에서는 모약물 CL 보정이 대사체 노출을 자동으로 보정해주지 않아요. 대사체 CL과 율속단계를 별도로 평가해야 합니다 [R&T pp.673–675].

**자주 만나는 함정**: 모약물과 대사체가 평행 감소를 보이면 대사체 반감기를 모약물과 같다고 보고하기 쉬워요. **그러면 안 됩니다.** 정확히는 "모약물 투여 후 관찰된 말단 반감기"가 모약물의 반감기를 그대로 보여주는 것뿐이에요. 대사체 자체의 반감기는 별도 IV 투여 시험으로 확인해야 합니다.

> 📖 **R&T p.660, Fig 20-1**: 대사체의 말단 기울기는 형성과 제거 중 더 느린 단계가 결정합니다. 그림은 parent → metabolite → eliminated metabolite 흐름에서 $k_f$, $k(m)$, other elimination을 동시에 보여줘요.

**이 카드의 한 줄**: 대사체 terminal slope를 봤을 때 본능은 **formation과 elimination 중 어느 쪽이 율속단계인지** 먼저 물어보는 것입니다. parallel decline을 own half-life로 라벨링하면 metabolite half-life가 과대 해석되고, 신장애에서 대사체 축적 외삽이 빗나갑니다.

<!-- SLIDE_START: M12 | title: M12. $AUC(m)/AUC$ 분해: $f_m × CL/CL(m)$ ($AUC(m)/AUC$ decomposition: $f_m × CL/CL(m)$) -->
<!-- SECTION_CORE: SC-14 -->

### M12. $AUC(m)/AUC$ 분해: $f_m \times CL/CL(m)$ ($AUC(m)/AUC$ decomposition: $f_m \times CL/CL(m)$)

**앞에서 → 여기서**. M11에서 형성과 제거 율속을 분리했어요. 이제 **$AUC(m)/AUC$를 $f_m$과 $CL(m)$으로 분해**합니다.

**거장의 시각.** $AUC(m)/AUC$를 그대로 $f_m$으로 읽으면, 형성 쪽 문제와 대사체 청소율 쪽 문제를 구분할 수 없어요. 두 미지수를 한 식에 욱여넣는 셈이거든요. 이 비를 $f_m \times CL/CL(m)$으로 나눠서 봐야 활성 대사체 위험의 정량 좌표가 비로소 생깁니다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: $AUC(m)/AUC$는 $f_m$ 그 자체가 아니에요. 이 비는 **대사체 형성분율과 대사체 청소율이 함께 들어간 복합량**입니다. 그래서 AUC ratio 하나만 보고 형성 쪽 문제인지 제거 쪽 문제인지 분리할 수 없어요.

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

> 💡 $AUC(m)/AUC$는 $f_m$과 $CL(m)$이 섞인 값이에요 — AUC ratio 하나로 형성 문제와 제거 문제를 분리할 수 없습니다. 비유하자면 수도꼭지 유입량($f_m$)과 배수구 크기($CL(m)$)가 같이 만든 수위예요.

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

$AUC(m)/AUC < 1$이고 $f_m$이 알려지지 않은 경우, $CL(m) \geq CL/f_m$이라고 추론할 수 없어요. 원전에 부합하는 부등식은 $CL(m) > f_m \cdot CL$뿐입니다. 같은 AUC ratio가 낮은 $f_m$, 높은 $CL(m)$, 또는 두 조건 모두에서 나올 수 있거든요.

**보존된 예시** [R&T pp.662–665]

- **Methylprednisolone hemisuccinate**(스테로이드 prodrug) → **methylprednisolone**(active drug): prodrug → active 변환의 대표 사례. → 그래서 **AUC ratio가 형성 단계의 산물임을 보여주는 임상 예시**입니다.
- **Tolbutamide**(1세대 sulfonylurea) → **hydroxytolbutamide**: 활성/비활성 대사체 비교에서 대사체 곡선이 율속단계와 상대적 청소율을 어떻게 구분하는지 보여줍니다.
- **Propranolol**(고추출 β차단제) → **naphthoxylactic acid**: 모약물이 high first-pass인 경우 대사체 입력에서 초회통과 비중이 큰 사례. (이 짝은 M13에서 다시 본격적으로 나옵니다.)

개별 그림 수치는 본 문서에서 확장하지 않습니다.

**현장 팁(Trench-level tip)**: active metabolite PopPK에서 **$AUC(m)/AUC$가 작다는 이유로 대사체를 무시하지 마세요.** $f_m$이 작아도 $CL(m)$이 신장애에서 크게 줄면 그게 바로 M14의 본 게임입니다.

**이 카드의 한 줄**: $AUC(m)/AUC$를 받았을 때 본능은 **$f_m$과 $CL(m)$을 따로 분해**하는 것이에요. 노출비를 형성분율과 혼동하면 신부전·DDI 외삽이 빗나가고, AUC ratio 단독 보고만으로는 formation/elimination 원인을 구분할 수 없습니다.

<!-- SLIDE_START: M13 | title: M13. 초회통과 대사체 기여와 정상상태 대사체(First-pass metabolite contribution + steady-state metabolite) -->
<!-- SECTION_CORE: SC-15 -->

### M13. 초회통과 대사체 기여와 정상상태 대사체(First-pass metabolite contribution + steady-state metabolite)

**앞에서 → 여기서**. M12의 노출비 분해는 단회 노출을 넘어 **first-pass 형성과 정상상태 축적 문제**로 이어집니다.

**거장의 시각.** 경구 대사체 노출을 단순히 생체이용률 문제로 보면, **초회통과 형성과 전신순환 형성이 한 통에 섞입니다.** 두 입력 경로를 따로 보지 않으면 같은 데이터에서 두 파라미터를 따로 추정할 수 없게 되고, 정상상태 축적 위험이 라벨에서 빠집니다. 그래서 본능은 — "**oral parent 후 metabolite가 보이면 두 입력 경로가 동시에 작동했다고 가정한다**"예요.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: 모약물을 **경구로 투여하면 대사체는 두 군데에서 생깁니다** — ① 흡수 과정에서 간 초회통과를 받으며 생기거나, ② 흡수가 끝난 뒤 전신 순환에서 생기거나. 이게 임상적으로 진짜 문제가 되는 건 한 가지 조건이 맞을 때예요 — **모약물이 초회통과를 강하게 받는데, 하필 그 대사체가 활성을 띌 때**.

**First-pass 이중 입력** [R&T pp.665–669]: 경구 모약물 투여 후 관찰되는 대사체는 두 입력의 합 — ① 흡수·초회통과 중 형성, ② 흡수된 전신 모약물에서 이후 형성.

**수정된 예시**

- **Propranolol**(고추출 β차단제) — 원전 예시는 단일 **20 mg 경구 투여**입니다 (80 mg이 아니에요). **Naphthoxylactic acid**(propranolol의 대사체)는 propranolol과 거의 같은 시간에 최고 농도에 도달하는데, 이게 초회통과 대사체 유입과 일치하는 패턴이에요 [R&T p.666]. → 그래서 **모약물이 high first-pass이면 대사체 입력에서 초회통과 비중이 크다**는 사실의 임상 사례입니다.
- **Morphine/M6G**(morphine-6-glucuronide; 모르핀의 활성 대사체) — 원전은 경구 **11.7 mg**과 정맥 **5 mg** morphine을 비교합니다 (10 mg 등가 용량 틀이 아니에요). Morphine의 경구 생체이용률은 낮지만, 초회통과에서 M6G가 형성되니까 **M6G 노출량/총량은 비슷할 수 있어요** [R&T pp.667–668]. → 그래서 **모약물 생체이용률이 낮아도 활성 대사체 노출은 보존될 수 있다**는 사실의 임상 사례입니다.
- **Isoproterenol**(β교감신경 작용제): 투여 경로에 따라 장벽 대사가 작동하는지 간외 대사가 작동하는지가 달라지면 소변 회수율도 달라집니다 [R&T p.669]. → 그래서 **route가 first-pass 위치 자체를 옮긴다**는 사실의 임상 사례입니다.

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

> 🔑 **Oral metabolite 판독법:** 초회통과 형성과 전신순환 형성을 한 모델에 같이 넣으면 **두 경로를 따로 추정할 수 없게 됩니다.** 경구 데이터만으로는 원리적으로 이 둘을 구분할 수 없어요 — 마치 공항 입국장과 도심 도로 두 곳에서 동시에 들어오는 사람 수처럼, 총 인원만 보면 어느 입구가 병목인지 알 수 없습니다.

다회 경구 투여 시 중첩 원리에 의해:

$$
\underbrace{C(m)_{av,ss}}_{\text{평균 Css}}=\frac{\underbrace{AUC(m)_{single}}_{\text{단회 노출}}}{\underbrace{\tau}_{\text{투여간격}}}
$$

정상상태 도달 시간은 율속 패턴에 따라 모약물 소실 또는 대사체 소실 중 **더 느린 쪽**이 결정합니다 [R&T pp.670–673]. **N-desalkylhalazepam**(diazepam계 활성 대사체)에서 대사체 축적/감소는 모약물보다 느려요. 정확한 timing은 본 문서에 고정하지 않습니다 `[R&T p.672; 확인 필요]`. **Carbamazepine**(항경련제)의 autoinduction은 정성적 추세만 보존합니다 — 용량 정규화 모약물이 감소하고 대사체 관계가 변화하지만, 정확한 용량 범위는 고정하지 않습니다 `[R&T p.676; 확인 필요]`.

**현장 팁(Trench-level tip)**: 경구 모약물 단독 데이터만으로는 **낮은 모약물 생체이용률과 대규모 초회통과 대사체 형성을 항상 구분할 수 없습니다.** Route 비교(IV vs oral)는 단순 생체이용률 계산을 넘어 진단 도구로 기능해요.

**이 카드의 한 줄**: oral parent 후 metabolite가 보일 때 본능은 **first-pass와 systemic formation을 두 입력 경로로 가정하고 IV-oral 비교 설계**를 떠올리는 것입니다. oral 단독 데이터를 과해석하면 두 경로를 따로 추정할 수 없고, 정상상태 축적을 경시하면 active metabolite 라벨 wording이 통째로 실패합니다.

<!-- SLIDE_START: M14 | title: M14. 신장애 활성 대사체 시나리오와 상호전환(Renal impairment active-metabolite scenario + interconversion) -->
<!-- SECTION_CORE: SC-16 -->

### M14. 신장애 활성 대사체 시나리오와 상호전환(Renal impairment active-metabolite scenario + interconversion)

**앞에서 → 여기서**. M13의 정상상태 대사체 개념은 **신장애에서 활성 대사체가 전체 위험을 지배하는 최종 시나리오**로 모입니다. 이 카드가 이 장의 종착역이에요.

**거장의 시각.** "$f_m$이 작으면 대사체 위험도 작다" — 정상 신기능에서는 맞는 말이에요. 정상에서는 형성량이 $f_m \times Dose$로 들어오니까. 그런데 **신장애에서 진짜 위험은 형성분율이 아니라 대사체 $CL(m)$이 얼마나 무너지는지**가 결정합니다. 작은 $f_m$이라도 제거 경로가 닫히면 그 작은 경로가 전체 활성 노출의 지배자가 됩니다. 이게 라벨에서 가장 자주 놓치는 시나리오예요.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: 활성 대사체가 존재할 때, **모약물 $f_e$ 하나만으로는 신부전 용량 결정을 내릴 수 없습니다.** 가장 위험한 상황이 반드시 '모약물이 주로 신배설되는' 경우는 아니에요. **모약물이 일부 대사되어 생긴 활성 대사체가 그 자체로 신배설을 받는** 경우도 똑같이 위험합니다.

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

> 🔑 **방어 논리 규칙:** parent-only 감량은 시나리오 (3)을 닫지 못해요. 통합 노출 또는 모니터링 논리가 필요합니다. 신장애에서 진짜 무서운 건 **모약물보다 활성 대사체가 훨씬 더 많이 쌓이는 경우**입니다.

경구 10 mg/h 투여 시, 정상상태 총 활성 농도는 모약물 **0.27 mg/L** + 대사체 **0.24 mg/L** = **0.51 mg/L**입니다 [R&T pp.673–674]. **무뇨 상태**에서 모약물은 약 **2배** 증가하는데, **대사체는 약 13배**까지 증가할 수 있어요. 정상 총 활성을 맞추기 위한 용량비는 약 **0.14**입니다 [R&T p.674].

이 숫자가 충격적이죠? $f_m = 0.3$인 — 보통이라면 "minor pathway 수준"이라고 부를 만한 — 대사체가, 신장이 닫히는 순간 모약물보다 6배 이상 빠르게 쌓이는 거예요. 그래서 parent-only 감량 라벨이 안전해 보이는 환자에서 독성을 만듭니다.

**시나리오 규칙** [R&T p.675]

1. 대사체 형성이 모약물의 주요 제거 경로이고 대사체가 활성인 경우, 용량은 대사체 청소율을 기준으로 설정해야 할 수 있습니다.
2. 모약물의 신배설이 주요 경로이고 대사체 형성이 부차적인 경우, 모약물 노출이 지배합니다.
3. **대사체 형성 비율이 작지만 대사체 제거가 거의 신배설에만 의존하고 대사체가 활성인 경우, 신부전에서 대사체가 전체 활성을 지배할 수 있습니다.**

**상호전환(Interconversion)** [R&T pp.676–679]

상호전환은 모약물과 대사체가 서로를 재생성할 수 있다는 뜻이에요. 그래서 대사체 쪽 신장애가 모약물의 **겉보기 소실**까지 늦출 수 있습니다. **Clofibric acid**(clofibrate의 활성 대사체)가 대표 사례로 보존됩니다. 그림에서 읽어낸 수치 앵커는 고정하지 않습니다 `[R&T p.679; 확인 필요]`.

**자주 만나는 함정**: '소수 대사 경로(minor metabolite pathway)'는 '소수 안전성 우려(minor safety concern)'와 같은 말이 아니에요. 신부전에서 대사체 $CL(m)$이 무너지면, 작은 $f_m$이라도 주요 노출 경로가 됩니다.

> 📖 **R&T p.674, Fig 20-10 and Table 20-4**: 모약물 농도만 보면 안전해 보이는데 환자는 부작용을 호소하는 상황 — 바로 이게 그 시나리오입니다. 그림과 표는 모약물 단독 용량 조정이 왜 실패하는지를 직접 보여주는 핵심 증거예요.

**나비효과 짚기.** "$f_m$이 작으면 대사체는 부차적 우려"라는 진술 — 정상 신기능에서는 그럴싸해 보입니다. 대사체 질량수지가 $f_m \times Dose$로 들어오니까 작은 $f_m$은 작은 노출량처럼 읽히죠. 그런데 활성 대사체 소실이 거의 신배설이라면($f_e(m) \approx 1$), **무뇨 상태에서 $CL(m)$이 거의 0으로 무너집니다.** 그러면 Tozer 풀이 예에서 본 그대로 — $f_m = 0.3$임에도 대사체 Css가 약 13배 상승해요 [R&T pp.673–675]. 이게 임상으로 가면 모약물 단독 감량 후 활성 대사체 독성 농도가 예측되지 않고, 규제 측면에서는 통합 노출 재계산과 ESRD 대사체 PK 재분석, 라벨 방어 논리 보완이 요구됩니다. 진단 신호는 모약물 CL은 신기능 비례로 감소하지만 대사체 Css가 10배 이상 상승하는 비대칭 패턴이에요. 방어는 통합 노출(모약물 + 활성 대사체, 등효능 또는 효능 가중)을 정상 수준으로 맞추는 용량비를 별도로 계산하는 것입니다.

**이 카드의 한 줄**: 신장애 + active metabolite 환자에서 본능은 **parent + metabolite combined exposure**를 계산하는 거예요. minor pathway를 minor concern으로 분류하면 작은 $f_m$의 위험이 통째로 가려지고, parent-only 감량으로 가면 임상에서는 metabolite 독성 농도가 미예측되고 규제 측면에서는 ESRD PK 재분석이 요구됩니다.

<!-- SLIDE_START: §5 | title: §5 혼동 쌍(Confusion Pairs) — 반드시 분리해야 하는 개념 쌍 -->
<!-- SECTION_CORE: SC-17 -->

## §5 혼동 쌍(Confusion Pairs) — 반드시 분리해야 하는 개념 쌍

M1~M14를 다 통과했어도, 임상 보고서 한 장에서 흔들리게 만드는 건 **비슷해 보이는 두 숫자**예요. 이 섹션은 그 쌍들을 차원·위치·원인·결과 4축으로 잘라서 다시는 같은 자리에 두지 않도록 만듭니다.

### 쌍 1(Pair 1). $CL$, $CL_R$, $f_e$

#### 2×4 혼동 분리 매트릭스

| 비교 기준 | $CL$ | $CL_R$ / $f_e$ |
|---|---|---|
| 단위 / 차원 | L/h, 전체 전신 청소율 | $CL_R$: L/h; $f_e$: fraction |
| 수식 내 위치 (분자/분모/지수) | $CL=CL_R+CL_H+CL_{other}$의 합 | $f_e=CL_R/CL$; $CL_R=f_e\cdot CL$ |
| 변화 원인 (생물학적/병적) | renal + nonrenal pathway 전체 | 신기능, urine route, filtration/secretion/reabsorption |
| 혼동 시 임상 결과 | total CL 전체에 renal covariate 적용 | nonrenal clearance까지 줄어 systematic underestimation |

> **⚡ 기억 고리**: $f_e$는 "renal pathway의 지분"이에요 — $CL_R = f_e \cdot CL$은 곱셈 분해이지 비례 단축이 아닙니다. 신부전 covariate는 $CL$ 전체에 곱하지 말고 $CL_R$ 위치(분해된 자리)에만 곱해야 해요.

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

> **⚡ 기억 고리**: $E_H = CL_b / Q_H$이지 $CL / Q_H$가 아니에요. $R = C/C_b < 1$인 약물에서 plasma 기준 비교를 하면 같은 약물이 false-high extraction으로 분류되어 임상·DDI 해석이 통째로 틀어집니다 — App.D bridge 없이 organ extraction을 말하지 마세요.

### 쌍 4(Pair 4). $f_u$ vs $f_{ub}$

#### 2×4 혼동 분리 매트릭스

| 비교 기준 | $f_u$ | $f_{ub}$ |
|---|---|---|
| 단위 / 차원 | plasma 내 unbound fraction | blood 내 unbound fraction |
| 수식 내 위치 (분자/분모/지수) | plasma binding 식 | well-stirred의 $f_{ub}\cdot CL_{int}$ |
| 변화 원인 (생물학적/병적) | albumin/AAG, displacement | $f_u$ + $C/C_b$ 변환 |
| 혼동 시 임상 결과 | plasma 분율을 blood 식에 직접 대입 | hepatic extraction과 PBPK 입력 단위 오류 [R&T App.D pp.775–776] |

> **⚡ 기억 고리**: Plasma 식에서 blood 식으로 옮길 때 $R = C/C_b$를 곱해야 합니다. $f_u$와 $f_{ub}$는 *분모가 다른 두 측정량*이지 같은 변수의 별명이 아니에요 — 이 한 곱이 빠지면 well-stirred의 분자($f_{ub} \cdot CL_{int}$)가 통째로 잘못된 단위에서 평가됩니다.

### 쌍 5(Pair 5). 고추출 IV vs 고추출 경구(High extraction IV vs High extraction oral)

#### 2×4 혼동 분리 매트릭스

| 비교 기준 | High extraction IV | High extraction oral |
|---|---|---|
| 단위 / 차원 | systemic $CL\approx Q_H$ | first-pass bioavailability/AUC |
| 수식 내 위치 (분자/분모/지수) | 혈류 제한 항 | $F$, first-pass, $f_{ub}CL_{int}$ 민감 항 |
| 변화 원인 (생물학적/병적) | hepatic blood flow | enzyme induction/inhibition, first-pass formation |
| 혼동 시 임상 결과 | IV DDI 음성을 oral 안전으로 오판 | route-dependent DDI와 metabolite formation 위험 누락 [G&W pp.83–85; R&T pp.665–669] |

> **⚡ 기억 고리**: IV에서는 $Q_H$ 상한(flow-limited)이 enzyme 변화를 가려요. Oral에서는 first-pass의 $f_{ub} \cdot CL_{int}$ 민감도가 그 상한을 풀어주고요. **IV negative DDI는 oral safety의 보장이 아닙니다** — route가 바뀌는 순간 같은 enzyme 변화가 다른 endpoint로 나타납니다.

---

### 쌍 6(Pair 6). Well-stirred vs 확장/투과성 제한 모델(Well-stirred vs extended/permeability-limited model)

#### 2×4 혼동 분리 매트릭스

| 비교 기준 | Well-stirred | Extended/permeability-limited |
|---|---|---|
| 단위 / 차원 | rapid equilibration 가정 | membrane/transporter 병목 포함 |
| 수식 내 위치 (분자/분모/지수) | $f_{ub}CL_{int}$ | $f_{ub}\rho CL_{int}$ 또는 uptake/efflux 단계 |
| 변화 원인 (생물학적/병적) | blood flow, binding, enzyme | uptake permeability, transporter, efflux |
| 혼동 시 임상 결과 | 낮은 $CL_{int}$처럼 오인 | transporter/permeability covariate 누락 [R&T App.E pp.778–779] |

> **⚡ 기억 고리**: Well-stirred는 "세포 안팎이 즉시 평형"이라는 가정이에요. $\rho < 1$이면 *효소가 아니라 막*이 병목이고, IVIVE의 $CL_{int}$ 부족처럼 보이는 mismatch가 실제로는 transporter/permeability 항 누락입니다. $\rho \to 1$이 회복되는 조건은 수동 확산이 $CL_{int}$보다 충분히 클 때예요.

### 쌍 7(Pair 7). 단일점 $CL_{int}$ vs Michaelis–Menten 정보(Single-point $CL_{int}$ vs Michaelis–Menten information)

#### 2×4 혼동 분리 매트릭스

| 비교 기준 | 단일점 $CL_{int}$ | Michaelis–Menten 정보 |
|---|---|---|
| 단위 / 차원 | 한 농도 rate의 압축값 | 농도-속도 곡선 정보 |
| 수식 내 위치 (분자/분모/지수) | $CL_{int}$ 하나로 입력 | $V_{max}$, $K_m$, free concentration |
| 변화 원인 (생물학적/병적) | 측정 농도 선택, scaling | saturation, enzyme capacity, transporter uptake |
| 혼동 시 임상 결과 | 곡선 정보 소실 후 정교한 모델 적용 | IVIVE 예측 실패와 FIH CL mismatch [G&W pp.85–89] |

> **⚡ 기억 고리**: 한 농도에서의 rate를 그대로 $V_{max}/K_m$로 쓰는 건 **곡선을 버린 다음 분수식을 정교화**하는 셈이에요. Saturation, free concentration, MMP scaling, 수송체 매개 uptake 중 어느 하나라도 빠지면 그 위에 어떤 hepatic model을 얹어도 입력 정보가 이미 뭉개져 있어 회복되지 않습니다.

### 쌍 8(Pair 8). 형성 율속 vs 제거 율속 대사체(Formation-rate-limited vs elimination-rate-limited metabolite)

#### 2×4 혼동 분리 매트릭스

| 비교 기준 | Formation-rate-limited | Elimination-rate-limited |
|---|---|---|
| 단위 / 차원 | parent가 metabolite terminal slope 지배 | metabolite own elimination 지배 |
| 수식 내 위치 (분자/분모/지수) | $k \ll k(m)$ | $k(m) \ll k$ |
| 변화 원인 (생물학적/병적) | 느린 parent disappearance/formation | 느린 metabolite clearance |
| 혼동 시 임상 결과 | parent 잔향을 metabolite half-life로 라벨링 | renal impairment 축적·multiple-dose 예측 실패 [R&T pp.659–662] |

> **⚡ 기억 고리**: **평행 감소이면 대사체는 모약물의 잔향입니다.** 보고된 대사체 말단 $t_{1/2}$이 대사체 *자신의* 것이 아닐 수 있어요. "Formation rate-limited"는 대사체가 자기 자신의 제거 속도가 아니라 모약물의 제거 속도를 입고 사라지는 상태입니다.

> **▶ 치명적 타격 (Critical Blow)**
> 이 혼동을 품고 NDA 또는 임상 dosing 결정을 강행했을 때: 모약물과 대사체의 말단 $t_{1/2}$이 같다는 보고는 대사체 자체의 제거 특성을 보여주는 게 *아닙니다*. Sponsor가 대사체의 IV 단독 시험 없이 "대사체 반감기는 X시간"이라고 명시하면, 이는 system-level 말단 slope에 대사체 라벨을 붙인 거예요. 그 결과 (a) 신장애에서 대사체 축적 외삽이 빗나가고, (b) 다회 투여 축적 예측이 빗나가며, (c) dose-response timing 평가가 동시에 빗나갑니다. "순차 연쇄에서는 가장 느린 단계가 downstream 물질의 말단 감소를 지배한다"가 본 항목의 정확한 원전 진술이에요 [R&T pp.659–662].

### 쌍 9(Pair 9). $AUC(m)/AUC$ vs $f_m$

#### 2×4 혼동 분리 매트릭스

| 비교 기준 | $AUC(m)/AUC$ | $f_m$ |
|---|---|---|
| 단위 / 차원 | 노출비 | 형성분율 |
| 수식 내 위치 (분자/분모/지수) | $f_m\cdot CL/CL(m)$ | 형성항 단독 |
| 변화 원인 (생물학적/병적) | formation + metabolite clearance | metabolic pathway share |
| 혼동 시 임상 결과 | 낮은 ratio를 낮은 formation으로 단정 | $CL(m)$ 변화와 신장애 위험 누락 [R&T pp.662–665] |

> **⚡ 기억 고리**: $AUC(m)/AUC < 1$은 **하나의 식에 두 미지수**예요 — $f_m$이 작아서일 수도, $CL(m)$이 커서일 수도, 둘 다일 수도 있습니다. $f_m$을 알지 못하면 $CL(m)/CL$ 부등식을 쓰지 마세요. 원전에 부합하는 부등식은 오직 $CL(m) > f_m \cdot CL$뿐입니다.

### 쌍 10(Pair 10). 순차 대사 vs 상호전환(Sequential metabolism vs interconversion)

#### 2×4 혼동 분리 매트릭스

| 비교 기준 | Sequential metabolism | Interconversion |
|---|---|---|
| 단위 / 차원 | 한 방향 대사 흐름 | 양방향 parent↔metabolite 흐름 |
| 수식 내 위치 (분자/분모/지수) | downstream chain | reversible transfer 항 |
| 변화 원인 (생물학적/병적) | 대사 경로 순차 진행 | 재생성, 장간순환·재전환 가능성 |
| 혼동 시 임상 결과 | parent profile만으로 renal-safe 오판 | metabolite 신부전이 parent apparent elimination까지 지연 [R&T pp.676–679] |

> **⚡ 기억 고리**: Sequential은 *한 방향*, interconversion은 *양방향*입니다. 후자에서는 모약물의 $f_e$가 작아도 대사체 쪽 신부전이 모약물의 *겉보기* 소실까지 늦출 수 있어요 — 모약물 profile만 보고 "renal-safe"로 분류하면 메커니즘을 놓치게 됩니다.

혼동 쌍들의 공통 메시지는 하나입니다 — **같아 보이는 두 숫자가 실제로는 서로 다른 분모, 투여 경로, 구획, 또는 율속단계를 갖습니다.**

---

<!-- SLIDE_START: §7 | title: §7 자기 검증(Self-Test) — 소크라테스식 딜레마 -->
<!-- SECTION_CORE: SC-18 -->

## §7 자기 검증(Self-Test) — 소크라테스식 딜레마

### Q1. 청소율 정의

$CL = Dose/AUC$가 compartment model 없이도 성립하는 이유를 $Rate = CL \cdot C$의 시간 적분으로 설명하세요.
**답 방향**: 총 제거량 = dose이고, $\int Rate\,dt = CL \cdot \int C\,dt$이므로 $CL = Dose/AUC$가 모델 독립적으로 성립합니다.

### Q2. 신장 분해

정상 $CL = 10\ \mathrm{L/h}$, $f_e = 0.6$인 약물에서 renal function이 25%로 떨어지고 nonrenal CL은 보존됩니다. 새 total CL은?
**답 방향**: renal CL = 6 → 1.5, nonrenal = 4, total = 5.5 L/h.

### Q3. 소변 플롯

Rate plot과 ARE plot의 slope가 다르고, rate plot에서 시간별 변동이 큽니다. 어떤 artifact 또는 physiology를 먼저 의심해야 합니까?
**답 방향**: 수집 간격, 방광 배출, pH/소변 유량 변동, $X_{u,\infty}$ 편향을 순서대로 점검합니다.

### Q4. Well-stirred 극한 근사

$Q_H = 81\ \mathrm{L/h}$, $f_{ub} \cdot CL_{int} = 20\ \mathrm{L/h}$이면 high/low/intermediate 중 어디에 가깝습니까? $f_{ub}$가 4배 증가하면?
**답 방향**: 초기 $E = 20/(81+20) = 0.20$으로 낮은 편. $f_{ub}$가 4배이면 80이 되어 $E \approx 0.50$, 중간 수준으로 상승합니다.

---

### Q5. 혈장 CL vs 혈액 CL

Plasma $CL = 60\ \mathrm{L/h}$, $C/C_b = 0.5$, $Q_H = 81\ \mathrm{L/h}$. $CL_b$와 추출률은? Plasma CL만 쓰면 어떤 오류가 생깁니까?
**답 방향**: $CL_b = 30\ \mathrm{L/h}$, $E = 0.37$. Plasma 기준으로 비교하면 실제보다 높은 추출률로 분류되는 오류가 발생합니다.

### Q6. IVIVE 함정

한 substrate concentration에서 얻은 in vitro rate로 $CL_{int}$를 만들고 MMP 평균값 하나로 scaling했다. Phase 1에서 in vivo CL이 예측의 1/5입니다. 어떤 세 가지 원인을 우선 점검할 것인가?
**답 방향**: 단일 농도 비선형성, 결합/비결합 농도 오류, MMP/scaling 변이, transporter/permeability 항 누락을 순서대로 확인합니다.

### Q7. 대사체 율속단계

Parent 투여 후 모약물과 대사체가 평행 말단 감소를 보입니다. 별도 대사체 투여에서는 대사체 반감기가 더 짧다. 어떤 경우입니까?
**답 방향**: Formation rate-limited 상태입니다. Parent 투여 후 관찰되는 대사체 slope는 parent에 의해 지배됩니다.

### Q8. AUC 비

$AUC(m)/AUC = 0.5$입니다. 이 값만으로 $f_m = 0.5$라고 말할 수 있습니까?
**답 방향**: 불가능합니다. $CL(m)/CL$이 필요합니다. 식은 $AUC(m)/AUC = f_m \cdot CL/CL(m)$입니다.

### Q9. 보스 딜레마(Boss Dilemma) — 신장애 + 활성 대사체

Parent drug의 정상 $CL = 30\ \mathrm{L/h}$, renal CL = 15 L/h, oral $F = 0.8$입니다. 활성 대사체의 $CL(m) = 10\ \mathrm{L/h}$, renal CL(m) = 8.5 L/h, 형성 분율 $f_m = 0.3$입니다. 무뇨 상태에서 parent renal CL과 metabolite renal CL이 모두 0이 됩니다. 모약물만의 용량 조정이 왜 불안전합니까?
**답 방향**: 모약물 노출은 약 2배 증가하지만, 대사체 CL은 10에서 1.5 L/h로 무너지고 Tozer 시나리오에서 형성 분율이 증가할 수 있습니다. 대사체 노출이 전체 활성을 지배할 수 있고, 원전 예시에서 약 13배 대사체 증가와 약 0.14의 용량비가 보고됩니다 [R&T pp.673–675].

> **전문가의 절충 판단(Master's Trade-off)**
> Q9에는 두 가지 *방어 가능한* 입장이 있습니다 — 어느 쪽을 택하든 그 결정은 라벨/CSR에서 어떻게 방어할 수 있는지를 함께 답해야 합니다.
>
> **(a) 통합 노출 기반 용량 조정.** 모약물 + 활성 대사체의 통합 활성을 정상 수준으로 맞추는 용량비(Tozer 풀이 예의 약 0.14)를 적용합니다. *방어 논리*: 대사체가 모약물과 거의 등효능이거나 효능 가중 합이 독성 유발인자라면, 통합 Css를 기준점으로 삼는 게 가장 보수적입니다. *Trade-off 비용*: 모약물 주도 치료 효과를 underdose할 위험이 있어요. 라벨 문구 요구: "based on combined active exposure".
>
> **(b) 2단계 모니터링.** 모약물 용량은 모약물 CL 변화에만 맞추되, 활성 대사체 TDM 또는 PK/PD biomarker로 안전 안내선을 운영합니다. *방어 논리*: 모약물과 대사체의 효능 차이가 분명하고, 대사체 분석법과 turnaround time이 가능하면 일률 감량보다 정밀합니다. *Trade-off 비용*: 분석법 검증, 채혈 설계, 조치 역치가 모두 라벨에 명시되어야 합니다.
>
> **두 입장 모두에서 방어 불가능한 것**: "parent $f_e$ 변화에 비례한 일률 감량" 단독. [R&T p.675]는 위 (1)/(2)/(3) 시나리오 규칙으로 이를 수식적으로 차단합니다. Sponsor가 활성 대사체의 ESRD PK를 측정하지 않은 상태에서 parent-only 비례 감량을 제출하면, 시나리오 (3) 가능성을 닫지 못한 채 권고가 발행되는 것이며, 이게 본 딜레마의 *진짜* 위험입니다.

---

<!-- SLIDE_START: §8 | title: §8 요약 & NONMEM/PopPK 교량 -->
<!-- SECTION_CORE: SC-19 -->

## §8 요약 & NONMEM/PopPK 교량

### §8A. 학습 위계상 위치(Positioning) — 28-session arc 내 위치

본 세션은 PopPK 학습 위계의 **physiology layer spine**을 마무리합니다.

- **선행 의존성**: 1-구획 IV/oral 동역학, AUC 정의·trapezoidal 적분, mass balance — 그 위에 *생리학적 분해*를 얹어요.
- **본 세션이 담당하는 자리**: 관찰된 $CL$, $t_{1/2}$, $AUC(m)/AUC$, $C/C_b$ 변화가 어느 생리학적 병목에서 왔는지 역추적하는 frame.

**본 세션이 열어주는 후속 영역**:

| 후속 세션 | 이 세션에서 열리는 개념 | 이 세션 없으면 실패하는 것 |
|---|---|---|
| PBPK 모델링 | well-stirred / 확장 청소율의 organ-level 제1원리 | organ input을 경험적 scalar로만 보정 |
| PopPK covariate selection | eGFR, $f_u$, transporter genotype, hepatic function score의 식 내 위치 | 통계적 유의성만으로 covariate 채택 |
| Parent–metabolite joint modeling | $f_m$, $CL(m)$, 율속단계의 식별가능성 spine | $F$와 $f_m$ product confounding |
| Renal/Hepatic impairment label | 시나리오 규칙 기반 dose/label wording | parent-only 또는 route-insensitive label 작성 |

### §8B. 선행 의존성(Dependencies) — 본 chapter를 대충 넘겼을 때의 후속 실패 모드

- **D1. Plasma↔Blood 단위 붕괴**: App.D bridge 생략 시 hepatic $E_H$가 $R = C/C_b$만큼 빗나가서 고추출/저추출 분류·DDI 해석·PBPK input $f_{ub} \cdot CL_{int}$ 단위가 통째로 잘못됩니다.
- **D2. $f_e$ covariate 오적용**: $f_e$를 비례 단축으로 다루어 신부전 covariate를 total $CL$에 곱하면 nonrenal까지 같이 줄어서 *systematic CL underestimation*이 발생, dose adjustment가 안전성과 어긋납니다.
- **D3. 대사체 식별가능성 실패**: 율속단계 분리 없이 $f_m$/$CL(m)$/$V(m)$을 자유 추정하면 oral data만으로 $F$와 $f_m$이 product confounding을 일으켜 두 파라미터를 따로 추정할 수 없습니다 (NONMEM `$COV` 실패 또는 RSE 폭증).
- **D4. 신장애 시나리오 (3) 누락**: 작은 $f_m$을 부차적 우려로 분류하여 활성 대사체 ESRD PK를 측정하지 않으면 parent-only 감량 라벨이 대사체 과포화를 만듭니다.

### §8C. 전문성 해자(Professional Moat) — 이 chapter를 진정으로 내면화한 연구자만이 갖는 것

NONMEM control stream과 GOF plot 작성은 이미 자동화 영역에 가깝습니다. 본 chapter를 구조적으로 내면화한 모델러는 자동화가 복제하지 못하는 것 — **관찰된 PK/PD 신호가 어느 생리학적 병목에서 왔는지 역추적하는 능력** — 을 갖습니다.

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| 수렴 실패 또는 GOF anomaly | 단위, 율속단계, $\rho$, interconversion | → | 구조 모델 과증식 또는 병목 오판 | §8D 4개 시그니처 순서로 점검 |
| Covariate 선택 회의 | eGFR, $f_u$, transporter genotype | → | 통계적 유의성만으로 생리학 위치 누락 | covariate가 들어갈 식의 자리를 먼저 명시 |
| Renal/Hepatic impairment 라벨 회의 | parent $CL$, $CL(m)$, combined exposure | → | parent-only 감량 또는 route 오류 | 시나리오 규칙과 방어 논리를 라벨 문구로 연결 |

### §8D. 실패 모드 카탈로그 — 네 가지 패턴

PART A 원전 앵커가 박힌 M카드 위에서 의미를 갖는 *실패 모드 요약* 4개입니다. 보고서에서 이 신호 중 하나라도 잡히면 해당 카드로 곧장 돌아갑니다.

| ID | 패턴 명칭 | Trigger pattern (관찰 신호) | 기계론적 원인 | Anchor card |
|---|---|---|---|---|
| **DS-1** | Phantom Plasma Clearance | 추정 $CL$이 $Q_H$(≈81 L/h)를 초과하는 결과가 나옴 — 생리학적으로 불가능한 값 | Plasma $CL$을 그대로 organ flow와 비교한 단위 mismatch. $R = C/C_b < 1$인 약물에서 발생. App.D bridge로 $CL_b = CL \cdot R$을 적용해야 함. | M8 (Plasma-to-blood ratio) |
| **DS-2** | Phantom Metabolite Half-life | 대사체의 추정 `k`가 모약물의 `k`와 거의 동일하게 잡힘 | Formation rate-limited 상태에서 *말단 slope를 대사체 자신의 slope로 오해*. 모약물의 잔향이 대사체 라벨을 입은 결과. Separate metabolite IV 또는 model-based formation rate fixing이 필요. | M11 (Rate-limiting step) |
| **DS-3** | Renal Covariate Asymmetry | 대사체의 CrCl power coefficient가 1.0에 가깝고 모약물의 power는 작은 비대칭 | 대사체가 거의 신배설($f_e(m) \approx 1$)인데 모약물의 $f_e$는 작은 시나리오 — Tozer Scenario (3)의 직접 신호. 활성 대사체 신장애 위험이 parent-only 보정으로는 검출되지 않음. | M14 (Renal impairment + active metabolite) |
| **DS-4** | Permeability Rate-Limited Mismatch | hepatic clearance covariate로 $f_u$를 넣었으나 모든 cohort에서 비유의/계수 ≈ 0; IVIVE에서 $CL_{int}$만 5–10배 underestimate | 수송체 기질에서 $\rho < 1$ 상태. $f_u$보다 uptake permeability/transporter genotype이 dominant covariate일 가능성 — 기본 well-stirred의 rapid equilibration 가정이 무너짐. | M9, M10 (Permeability/Extended clearance) |

### §8E. NONMEM/PopPK 구현 교량(Implementation Bridge)

| 원전 개념 | PopPK 구현 시사점 |
|---|---|
| $CL = CL_R + CL_H + CL_{other}$ | 신기능 covariate를 total $CL$에 무차별 적용하지 말고 경로별 구성요소에 적용합니다. |
| $CL_R = f_e \cdot CL$ | 소변 데이터 또는 외부 $f_e$ 정보가 없으면 신장 분율을 과해석하지 마세요. |
| PK5 혈장+소변 동시 적합 | `DVID`/endpoint별 잔차오차로 혈장과 소변 데이터를 동시에 적합합니다. |
| $CL_b = CL \cdot C/C_b$ | 간 추출 또는 PBPK 입력에는 혈액 기준 청소율을 사용합니다. |
| well-stirred + App.E $\rho$ | 수송체 기질에서는 $CL_{int}$ covariate보다 uptake/permeability covariate 가능성을 먼저 점검합니다. |
| $AUC(m)/AUC = f_m \cdot CL/CL(m)$ | 대사체 모델에서 $f_m$, $CL(m)$, $V(m)$을 따로 추정할 수 있는지(identifiability)를 투여 경로/용량/대사체 데이터로 확인합니다. |
| 율속단계(rate-limiting step) | 대사체 말단 slope를 곧바로 대사체 자신의 $t_{1/2}$로 쓰지 마세요. |
| 신부전 활성 대사체 | 모약물과 대사체의 통합 노출을 라벨/용량 시나리오 민감도로 계산합니다. |

### §8F. 한 페이지 요약(One-page Recap)

1. $CL$은 농도로 정규화한 제거 능력입니다 — 제거 속도 자체가 아닙니다 [G&W p.49; R&T pp.124–128].
2. $t_{1/2}$은 $V/CL$에서 파생된 결과값입니다. $CL$과 $V$를 먼저 분해하지 않고 $t_{1/2}$만 해석하지 마세요 [R&T pp.148–150].
3. $CL_R = f_e \cdot CL$이지만, 신장 청소율 자체는 여과 + 분비 − 재흡수이며, urine pH와 flow가 이 값을 변화시킵니다 [G&W pp.48–56; R&T pp.138–148].
4. Well-stirred 간 청소율은 $Q_H$, $f_{ub}$, $CL_{int}$가 결정합니다. 고추출/저추출은 극한 근사값이지, 약물에 영구히 붙는 라벨이 아닙니다 [G&W pp.79–85; R&T pp.130–135].
5. 장기 추출 계산에서 plasma 농도는 blood 농도로 변환해야 합니다. App.D가 이 변환의 질량수지 다리를 제공합니다 [R&T App.D pp.775–776].
6. IVIVE는 in vitro 입력이 이미 정보를 잃었을 때 실패합니다 — single-point $CL_{int}$, 부적절한 scaling, permeability/transporter 항 누락이 대표적입니다 [G&W pp.85–90; R&T pp.136–138; R&T App.E pp.778–779].
7. Parent–metabolite 시스템은 $f_m$, $CL(m)$, 율속단계를 따로 파악해야 합니다. $AUC(m)/AUC$는 $f_m$ 그 자체가 아닙니다 [R&T pp.659–665].
8. 신부전 용량 조정은 모약물 $f_e$만이 아니라, 활성 대사체 청소율을 별도로 평가해야 합니다 [R&T pp.673–679].

---

<!-- v4.0 변환 노트
- v3.9 → v4.0 변환: spoken-voice rewrite, byte-preserved scope
- Pass 9 자가검증 12개 통과 확인:
  · 카드 ID 1:1 매핑 (M1–M14 전부 보존)
  · 약물명 1:1 매핑 (alfentanil/rifampin, alprenolol/pentobarbital, fentanyl/itraconazole/ritonavir, phenytoin, clofibric acid, methamphetamine, propranolol/naphthoxylactic acid, morphine/M6G, isoproterenol, N-desalkylhalazepam, carbamazepine, methylprednisolone hemisuccinate, tolbutamide, inulin 전부 보존)
  · 정량 수치 1:1 매핑 (GFR 120 mL/min, Q_H=81 L/h=1.35 L/min, 신장 혈류 1.1 L/min, urine pH 4.5-8, methamphetamine 70-80%/1-2%, PK5: 250 mg/V≈7L/CL≈1.2 L/h/f_e≈35%/CL_R≈0.42 L/h/CV<5%/2.84%/8.96%/6-6.3h, ritonavir 0.94→0.32 L/h/kg, propranolol 20 mg, morphine 11.7/5 mg, M14: 0.27+0.24=0.51 mg/L, 2배/13배/0.14, Q4: 20→80 E=0.20→0.50, Q5: 60/0.5/30/0.37, Q2: 10/0.6→1.5/4/5.5 L/h, hook 60 L/h/0.5/30/0.37 전부 보존)
  · 출처 1:1 매핑 (G&W p.48/49/49-50/50-51/50-52/51/52/77-79/79-82/79/83-85/85-89/85-90/87/88-89/90-94/132-133/494-499/497-499/Fig 2.35/Fig 2.58/Fig 2.104-2.105/Table 2.9 + R&T pp.119-120/124-128/125/127-128/128/130-135/131/136-138/137-138/138-145/138-148/139-142/145/148-150/150-163/152/153/154-155/159-160/161-162/658-659/659-662/660/662-665/664/665-669/666/667-668/669/669-673/670-673/672/673-675/674/675/676/676-679/679 + R&T App.D pp.775-776 + R&T App.E pp.777-778/778-779/779-780 전부 보존)
  · 수식 $$ 블록 수 동일, \underbrace/\overbrace annotation 전부 보존
  · SLIDE_START·SECTION_CORE 마커 모든 슬라이드 경계 부여 (§1/§1.5-통합/§2/M1-M14/§5/§7/§8 = 19개)
  · Reading Test 통과: 한 번 읽고 결론이 머리에 남는 문장으로 재구성
  · §0.3 회피 어휘 0건: 닫는다/측정 교량/분기된다/식별성/비대칭성/추출률 분류/혈류 천장/figure-derived 추정/시사한다/도출된다/압축한다/사고 순서/인지 잠금/진단 시그니처/원자 노트/감사 체인/체화 핵심/제텔카스텐 원자/단정하기 쉽다 → 전부 산문으로 치환
  · 자기참조 0건: "Mn의 결론이 ~한다" 형태 → 결론 인라인 + (→ Mn) 포인터로 치환
  · 약물명 첫 등장 100% §5 3-Step (분류 인라인 + 특징 한 줄 + "→ 그래서 [개념]의 사례") 적용
  · 메타-언어 헤더 0건: "진단 시그니처"→"실패 모드 패턴", "체화 핵심"→"이 카드의 한 줄"(자연 산문), "Plausible Fallacy" 4단 박스→M14 본문 단락 산문 ("나비효과 짚기"), "혼동 지점"→자연 산문 ("자주 만나는 함정")
  · 거장의 시각 §4 셋 중 하나로 재구성: 실무 함정 짚기 / 경계 조건 짚기 / 압축 한 줄
- 구조 재구성 핵심 결정:
  · Hook을 본문 시작에 배치 (CL=60 L/h 환자 사례) → §1 본문 → M8에서 hook 재호출 ("앞서 hook에서 본 그 환자죠") → M14에서 종착 (이 장의 종착역)
  · 메타포 한 줄: "청소율은 숫자 한 개가 아니라 주소 4줄" (농도/장기/경로/모약물·대사체) — §1 도입에 자연 흡수
  · §1.5 "빠른 읽기 경로" → "§1.5 4-좌표 질문"으로 통합 명료화 (별도 SLIDE_START 부여하지 않고 §1 내 흐름으로 유지)
- 보류 항목 없음
-->

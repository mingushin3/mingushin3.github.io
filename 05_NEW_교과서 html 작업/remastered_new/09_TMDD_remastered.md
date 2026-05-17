# 세션 09 — TMDD 한 바느질로 꿰기: PK27의 123배 사건이 가르치는 것들 (Remastered)

> 이 자료는 Gabrielsson & Weiner 5e의 turnover, PK26 Efalizumab, PK27 TMDD 사례와 Rowland & Tozer 5e Ch.21 Protein Drugs를 한 흐름으로 재구성한 학습자용 정리본임. 다루는 범위는 단백질 약물 PK, mAb 배치, FcRn, TMDD, Michaelis-Menten 근사, 자료 풍부도(data richness), assay 식별성임.

---

## 들어가며 — 이 세션을 한 컷으로 요약하면

> **임상 장면 한 컷**
> 한 단클론 항체를 **1.5, 5, 15, 45 mg·kg⁻¹** 네 용량으로 급속 정맥 주사함. 고용량 곡선 세 개는 모델이 그럴듯하게 맞춰주는데, 가장 낮은 용량 곡선 하나만 따로 놂. 그래서 모델을 두 가지로 돌려봤음 — MM 모델의 $K_m$은 **3.7**, Full TMDD 모델의 $K_m$은 **0.03**. **약 123배 차이임.** [G&W pp.602–603; G&W p.609]

이게 무슨 뜻인지 임상 현장 언어로 옮기면 이렇게 됨 — first-in-human 들어가서 저용량 trough 노출을 MM 모델로 예측했는데, 실제로는 100배 이상 어긋날 수 있다는 얘기임. dose-escalation 결정이 통째로 잘못된 경로로 갈 수 있고, target occupancy 판단도 망가지고, sub-population 외삽도 망가짐. "피팅이 살짝 안 됐다" 수준이 아니라 **임상 의사결정의 출발 좌표가 틀어진 사건**임.

이 세션 전체는 결국 한 질문에 답하는 것임 — **"이 데이터가 실제로 어떤 파라미터를 가르치고 있는가?"** 곡선이 예쁘게 맞춰지냐가 아니라, 이 질문이 모든 결정의 기준임.

그래서 이 세션을 한 바느질로 꿰면 이렇게 됨:

| 카드 | 한 줄 |
|---|---|
| **M1** | Target은 "살아있는 욕조"임 — baseline은 결과값이지 입력값이 아님 |
| **M2** | mAb는 작은 약물처럼 안 빠짐 — 4개의 관문(분포·림프·proteolysis·FcRn)이 따로 작동함 |
| **M3** | TMDD 곡선의 4 phase는 시간 순서가 아니라 **농도 영역의 지도**임 |
| **M4** | Full TMDD는 ligand·target·complex·sink를 분리하는 ODE임 — 자료가 있어야 풀림 |
| **M4½** | 임상에서 실제로 쓰는 건 Full도 MM도 아니라 그 사이의 **QSS 근사**임 |
| **M5** | MM은 "포화 영역 안에서만 쓰는 압축 도구"임 — 그 밖으로 외삽하면 PK27 사건이 일어남 |

이 카드들은 평행한 주제가 아니라 **의존 사슬**임. M1이 무너지면 M2가 흔들리고, M3 없이 M4를 보면 phase가 뭘 가르치는지 모르고, M4 없이 M4½/M5를 보면 어디서 어떤 가정으로 근사가 가능한지 판단할 도구가 없음. 그래서 거꾸로 말하면, PK27의 123배 사건은 **이 사슬의 어느 한 마디를 건너뛴 결과**임.

선행: 1구획·2구획 선형 PK + Michaelis-Menten + ODE 기본.
후속: mAb PopPK → target occupancy 시뮬레이션 → QSP/PBPK → biologics 임상약리 narrative.

**Source**:
- Gabrielsson J, Weiner D. *Pharmacokinetic and Pharmacodynamic Data Analysis: Concepts and Applications*, 5th Edition. Apotekarsocieteten, Stockholm, 2016. — Ch.2 §2.6 Turnover [G&W pp.94–111]
- 위 문헌 — Case Study PK26 Efalizumab [G&W pp.599–601]
- 위 문헌 — Case Study PK27 TMDD [G&W pp.602–610]
- Rowland M, Tozer TN. *Clinical Pharmacokinetics and Pharmacodynamics*, 5th Edition. Wolters Kluwer, Philadelphia, 2019. — Ch.21 Protein Drugs [R&T pp.687–730]
- Mager DE, Jusko WJ. *J Pharmacokinet Pharmacodyn* 2001;28:507–532. — R&T Fig.21-8 원전
- Peletier LA, Gabrielsson J. *J Pharmacokinet Pharmacodyn* 2012;39:429–451. — R&T Fig.21-9 원전

---

## M1 — Turnover: Target은 "살아있는 욕조"임

PK27의 123배 사건이 일어난 첫 번째 이유는 단순함. 사람들이 **target $R$을 고정값으로 처리**하기 때문임. 그런데 target은 약물이 들어오기 전부터 이미 몸 안에서 계속 만들어지고 계속 분해되는 **dynamic system**임. 그래서 약물이 target에 결합한다는 건, 외부 ligand가 **이미 돌아가고 있는 turnover 시스템 안으로 들어가서 그 균형을 흔든다**는 의미임. 이걸 못 박지 않으면 $R_0$, $k_{out}$, recovery time이 전부 "잔차"나 "임의 파라미터"로 보이게 됨.

### 욕조 그림 한 컷이면 됨

10 L 욕조에 분당 1 L의 물이 들어오고 분당 1 L의 물이 빠져나가면 turnover time은 10분임. 사람 몸의 물 42 L와 하루 섭취량 2.5 L를 넣으면 water turnover time은 **약 17일**임. 핵심은 "얼마나 많이 있는가"가 아니라 **"지금 pool 전체가 얼마나 빨리 교체되는가"**임 [G&W p.96].

이 단순한 욕조 수학이 내인성 IgG에도, target receptor에도, hormone turnover에도, **글자 그대로 똑같이** 적용됨.

| 파라미터 | 단위 | 의미 |
|---|---|---|
| $A$ | mass | 욕조 안의 물(pool 양) |
| $k_{in}$ | mass/time | 수도꼭지 — 0차 입력 |
| $k_{out}$ | time⁻¹ | 배수구 — 1차 분획 소실 |
| $A_0$ | mass | 정상상태 수위(baseline) |
| $t_t$ | time | 욕조 전체가 교체되는 시간 |

$$
\overbrace{\frac{dA}{dt}}^{\text{pool 변화}}
=
\underbrace{k_{in}}_{\text{0차 입력 (수도꼭지)}}
-
\underbrace{k_{out}\cdot A}_{\text{1차 소실 (배수구)}}
\qquad \text{Eq.2:237}
$$

정상상태(수도꼭지 = 배수구)에서는 줄줄이 관계식이 나옴 [G&W pp.95–96]:

$$
\begin{aligned}
\underbrace{A_0}_{\text{baseline 수위}} &= \underbrace{\frac{k_{in}}{k_{out}}}_{\text{입력÷소실}} \\
\underbrace{t_t}_{\text{교체 시간}} &= \underbrace{\frac{1}{k_{out}}}_{\text{소실 역수}} = \underbrace{\frac{V_{ss}}{Cl}}_{\text{PK 체류시간}} = \underbrace{MRT}_{\text{평균 체류}} \\
\underbrace{t_{1/2}}_{\text{반감기}} &= \underbrace{\frac{\ln(2)}{k_{out}}}_{\text{1차 반감}}
\end{aligned}
$$

### 여기서 절대 놓치면 안 되는 비대칭

이게 임상 해석에서 진짜 중요한 부분임. **$k_{in}$을 바꿀 때와 $k_{out}$을 바꿀 때 결과가 다름.**

- $k_{in}$ 변화 → **수위만** 바뀜. 새 수위 도달 시간은 그대로
- $k_{out}$ 변화 → **수위와 도달 시간이 같이** 바뀜 [G&W p.97]

$$
\underbrace{k_{in}\uparrow}_{\text{입력 증가}}
\Rightarrow
\underbrace{A_0\uparrow}_{\text{level만 상승}},
\qquad
\underbrace{k_{out}\uparrow}_{\text{분획 소실 증가}}
\Rightarrow
\underbrace{A_0\downarrow}_{\text{level 하강}}+\underbrace{t_t\downarrow}_{\text{시간도 단축}}
$$

왜 이게 임상적으로 중요하냐 — 예를 들어 어떤 PD endpoint가 회복이 느려졌음. 합성이 줄어든 건지($k_{in}\downarrow$), 분해가 느려진 건지($k_{out}\downarrow$)에 따라 처치 방향이 완전히 갈림. **level 하나만 봐서는 원인을 못 잡음.**

> 💡 **단위가 핵심임.** $k_{in}$은 mass/time, $k_{out}$은 time⁻¹임. 이거 안 구분하면 곧 **target 합성($k_{in}$)과 ligand-target 결합 on-rate($k_{on}$)을 같은 양으로 섞어버림** — M4에서 이 함정이 다시 나옴. 미리 못 박아둬야 안전함.

### 임상 앵커 3개 — "같은 수식, 다른 맥락"

**IgX**(내인성 성장호르몬 유사 펩타이드): predose baseline 32 µg·L⁻¹, $k_{in}=0.78$ µg·h⁻¹·kg⁻¹, $t_t=2.7$ h, $t_{1/2}=2.5$ h, $k_{out}=0.27$ h⁻¹. → **endogenous baseline 위에 외부 ligand가 얹히는** 전형적인 사례임 [G&W pp.100–101].

**내인성 IgG**: $t_{1/2}=$ **23 days**, FCR 6.7% plasma pool·day⁻¹, turnover 33 mg·kg⁻¹·day⁻¹ [G&W p.102]. R&T가 "치료용 mAb 반감기 ≈ 21일"이라고 하는 숫자와 비슷한 영역인데, **두 문장을 하나로 합치면 안 됨**. 내인성 IgG는 단일 분자종이고, 치료용 mAb는 후보별로 FcRn 친화도가 다 다름. → **숫자가 비슷하다고 같은 사실이 아님** [R&T p.708].

**Estradiol** (폐경 후 여성): $k_{in}=19$ µg·24h⁻¹, $Cl=1.6$ L·min⁻¹, $V_{ss}=50$ L, $t_{1/2}=26$ min, $MRT=18$ min. 임상 포인트는 — 폐경 후 낮은 E2 level은 **청소율이 늘어서가 아니라 $k_{in}$이 줄어서** 만들어짐. → **level 하나만 봐서는 합성 쪽인지 분해 쪽인지 모름** [G&W pp.102–104].

### 실무에서 자주 망하는 지점

predose target 값을 그냥 `R0=THETA`로만 추정하면 $R_0$의 individual variability가 residual error로 흡수돼서 사라짐. baseline DV record로 모델에 직접 넣어야 함. 이건 교과서 control stream이 아니라 NONMEM 쪽 구현 해석임.

**M1 한 줄**: target을 고정값으로 보면 TMDD는 출발부터 망함. $R$은 $k_{in}/k_{out}$이 만들어내는 **균형의 결과값**이고, 외부 ligand는 이 균형을 흔드는 침입자임. baseline과 회복 시간을 같이 설명할 때는 $k_{in}/k_{out}$ 구조가 결정함.

---

## M2 — mAb는 작은 약물처럼 안 빠짐: 4개의 관문

M1에서 target이 살아있는 욕조라는 걸 잡았음. 이제 그 욕조에 들어가는 ligand 자체를 봐야 함. mAb라면 small molecule과 전혀 다른 ADME를 거침. 이걸 단일 "반감기 21일" 같은 숫자 하나로 압축하면 어떻게 되냐 — slow input, FcRn salvage, target-mediated sink가 전부 terminal slope에 뭉뚱그려져서 **어떤 데이터가 어떤 mechanism을 가르치는지 분리할 수 없게 됨** [G&W pp.97–100; R&T pp.701–724].

그래서 4개 관문으로 분리해서 봐야 함:

| 관문 | 무슨 일이 일어나는가 | 출처 |
|---|---|---|
| **① Distribution** | $V_d$가 작음 — plasma/interstitial space로 분포 제한됨 | Table 21-6 [R&T pp.701–702] |
| **② Absorption (lymphatic)** | sc/im 후 큰 단백질은 주로 림프관으로 느리게 전신 유입 | Table 21-13 [R&T p.718] |
| **③ Elimination** | 작은 단백질은 신장이 핵심, 큰 mAb는 proteolysis와 RME가 중심 | [G&W pp.98–99; R&T pp.704–708] |
| **④ Rescue (FcRn)** | IgG/mAb를 acidic endosome에서 회수해 순환으로 돌려보냄 | Fig.21-5 [R&T p.709] |

### 관문 ① — 분포: "혈관 안에 갇힌 큰 덩어리"

R&T Table 21-6은 단백질 약물의 $V_{ss}$가 대체로 **0.04–0.23 L·kg⁻¹** 범위라고 보여줌. body water 전체(약 0.6 L·kg⁻¹)에 비하면 작은 숫자임. 큰 biologic은 body water 전반이 아니라 plasma/interstitial space에만 갇혀 있다는 뜻임 [R&T pp.701–702].

$$
\underbrace{V_{ss}}_{\text{SS 분포용적}}
\approx
\underbrace{0.04\text{--}0.23\ \mathrm{L\cdot kg^{-1}}}_{\text{제한 분포}}
$$

### 관문 ② — 림프 흡수: "혈관 아니라 림프관 타고 들어옴"

sc 단백질·펩타이드 흡수는 낮고 erratic하고 지연됨. 림프 흐름은 대략 2 L/day임 [G&W p.97]. R&T Table 21-13의 분자량 기준이 핵심임 — **15,000–20,000 g/mol을 넘으면 주로 림프관 경로**임 [R&T p.718]:

$$
\underbrace{MW}_{\text{분자량}}
>
\underbrace{15{,}000\text{--}20{,}000\ \mathrm{g/mol}}_{\text{림프 경로 역치}}
\Rightarrow
\underbrace{\mathrm{lymphatic\ input}}_{\text{느린 전신 유입}}
$$

**주의 한 줄** — R&T Fig.21-16에서 양(sheep)의 0.246–19 kDa 데이터로 "분자량 클수록 림프 회수율 증가"라는 **방향성**만 봐야 함. 이 데이터를 150 kDa mAb에 직선 외삽해서 회수율 퍼센트를 계산하면 안 됨 [R&T p.720].

**Absorption-rate limitation 사례 — somatropin** (재조합 성장호르몬, 22 kDa): iv 반감기 **2.1시간**, 그런데 sc로 주면 농도가 훨씬 더 길게 지속됨. → **terminal profile이 elimination이 아니라 slow input에 의해 rate-limited될 수 있다**는 사례임 [R&T p.721].

### 관문 ③ — 제거: "크기에 따라 갈림"

**Renal disease 사례 — anakinra** (재조합 IL-1 수용체 길항제, 17,258 g/mol): 신기능 떨어지면 청소율도 같이 떨어짐. 반면 full-size mAb는 사구체 여과를 거의 안 받아서 신질환 영향이 작음. → **"단백질이면 신장이 중요하다"가 아니라 크기에 따라 갈림** [R&T p.724].

### 관문 ④ — FcRn salvage: "분해 직전에서 구조됨"

FcRn은 내인성 IgG와 치료용 mAb의 긴 반감기를 설명하는 핵심 salvage 기전임. R&T는 mAb 반감기가 IgG에 가까운 **약 21일**인 경우가 많다고 함. 그런데 이건 모든 mAb에 통하는 고정 숫자가 아님. FcRn 친화도, target-mediated clearance, immunogenicity, dose level에 따라 apparent 반감기가 달라짐 [R&T pp.708–710].

$$
\underbrace{t_{1/2,\mathrm{mAb}}}_{\text{mAb 겉보기 t½}}
\approx
\underbrace{21\ \mathrm{days}}_{\text{IgG식 prior}}
\quad \text{(prior일 뿐, 분자별 확인 필요)}
$$

**FcγR 매개 청소율 사례 — adalimumab + MTX**: 류마티스 관절염 환자에서 **methotrexate** 병용 시 **adalimumab**의 청소율이 **29–44% 감소**할 수 있음. → **FcγR은 변두리 디테일이 아니라 특정 질환·병용약물 맥락에서 clearance covariate가 됨** [R&T p.706].

### sc mAb 예시 — "Tmax가 며칠 단위"

Table 21-15 예시 [R&T p.723]:

| mAb | $F$ | $T_{max}$ | $t_{1/2}$ |
|---|---|---|---|
| **adalimumab** (anti-TNFα) | 0.64 | 5.5 days | 30 days |
| **omalizumab** (anti-IgE) | 0.62 | 7.5 days | 26 days |
| **efalizumab** (anti-CD11a) | 0.50 | — | 17 days |

$T_{max}$가 며칠 단위라는 것 자체가 **sc 입력이 느리다**는 뜻임. terminal slope를 그대로 "elimination 반감기"로 읽으면 absorption-rate limitation을 놓침.

> 💡 **mAb 곡선의 "느림"은 단일 원인이 아님.** 4개 관문이 합쳐진 결과임. 그래서 sc 투여 terminal slope를 그대로 elimination 반감기로 읽으면 위험함. terminal phase를 해석하기 전, **4개 관문 중 어느 쪽이 지배하는지 먼저 적어보는 습관**이 필요함.

**ADA(anti-drug antibody)와 immunogenicity** — 설명되지 않는 청소율 증가가 보이면 target biology뿐 아니라 ADA도 같이 점검해야 함. ADA가 TMDD signature 자체를 시점에 따라 어떻게 변형시키는지는 M4에서 따로 다룸 [R&T p.725].

**M2 한 줄**: mAb의 느림은 반감기 숫자가 아니라 **tissue access + lymphatic transit + FcRn recycling + target sink**가 합쳐진 결과임. 이 4관문을 분리해 두면 다음 M3에서 phase A~D가 무엇을 가르치는지 분리해서 읽을 수 있음.

---

## M3 — TMDD 곡선의 4 phase: 시간이 아니라 농도 영역의 지도

M2의 4 관문을 통과한 곡선이라도 **target 결합이 개입하는 순간 곡선은 더 이상 시간표가 아님**. 농도 영역의 지도가 됨. 이게 무슨 뜻이냐 — Phase A→B→C→D를 "시간 순서"로 외우면 임상에서 망함. 농도 위계로 읽어야 함.

### PK27 데이터셋 한 번 더

이 세션의 척추가 되는 PK27을 다시 꺼냄. 단클론 항체를 **1.5, 5, 15, 45 mg·kg⁻¹** 네 용량으로 급속 정맥 주사한 데이터임 [G&W pp.602–603]. 곡선을 용량별로 층화해서 봐야 하는 이유는 단순함 — **곡선이 어떤 phase를 실제로 관찰했는지가 용량마다 다름**.

PK27에서 $R_0 \approx 12$ mg·L⁻¹, $K_m \approx 0.03$ mg·L⁻¹임. ligand 농도 $C_L$이 이 역치들을 통과하면서 phase가 갈림:

$$
\underbrace{C_L}_{\text{ligand 농도}}
\quad\text{통과}\quad
\overbrace{\underbrace{R_0}_{\text{target 기준}},\ \underbrace{K_m}_{\text{겉보기 경계}},\ \underbrace{K_d}_{\text{결합 경계}}}^{\text{phase 전환점}}
$$

### 4 phase의 정체

| 단계 | 지배 과정 | 농도 위치 | 해석 |
|---|---|---|---|
| **A** | 빠른 2차 결합 | dosing 직후 최고 농도 | ligand와 target이 빠르게 평형 |
| **B** | **1차 nonspecific clearance** | target 포화 영역 | target 경로 포화 → 비특이적 linear clearance가 지배 |
| **C** | 혼합차수 배치 | target 부분 포화 | 선형과 target-mediated 경로 공존 |
| **D** | $k_{off}$와 $k_{e(RL)}$ 주도 | 매우 낮은 ligand | target-specific 제거가 가시화 |

> ⚠️ **Phase B의 "느린"은 함정임.** 표준 TMDD 문헌(Mager & Jusko 2001; Peletier & Gabrielsson 2012)과 R&T 본문은 Phase B를 "drug is mainly eliminated directly by a first-order process"로 기술함 [R&T p.712]. 즉 Phase B는 **target 결합 경로가 포화돼서 nonspecific linear clearance가 지배하는 영역**이고, 절대적 청소율 척도로는 **Phase D보다 빠름**. 저농도 Phase D에서는 $k_{off}$·$k_{e(RL)}$ 주도의 매우 느린 말기 기울기가 나옴. "느린"이라는 단어 때문에 phase 순서를 "A→B→C→D = 빨라짐→느려짐"으로 단조 해석하면 안 됨. **농도 위계가 시간 위계와 반드시 일치하는 게 아님.**

### 시간 순서가 아니라 농도 위계인 이유 — 한방 직관

생각해봐야 할 것은 이거임. 고용량(45 mg/kg)을 주면 ligand가 target을 완전 압도해서 곡선은 nonspecific clearance 쪽만 보임 — Phase B만 길게 깔리고, 정말 마지막 trace level에서야 Phase D가 살짝 보임. **저용량(1.5 mg/kg)을 주면 ligand가 target에 비해 충분히 많지 않으니 target-specific 경로가 처음부터 끝까지 계속 작동함** — Phase C, D가 훨씬 일찍, 훨씬 뚜렷하게 보임.

그래서 phase는 시간 좌표가 아님. **dose가 결정하는 농도 영역의 지문**임.

### 곡선이 가르치는 것, 가르치지 않는 것

곡선의 한계를 한 줄씩 짚으면 [G&W pp.603–609]:

- 고용량 데이터만 봤다면 target-mediated 경로는 이미 포화 상태라 **선형처럼 보임** → MM 모델로도 잘 맞는 것처럼 보임
- assay 민감도가 낮아서 저용량 데이터가 빠지면 Phase A와 D를 못 봄
- sc 흡수가 느리면 초기의 rapid binding(Phase A)이 input kinetics 뒤에 가려짐
- target과 complex 데이터가 없으면 ligand-only 적합이 좋아 보여도 $k_{on}$, $k_{off}$, $k_{e(RL)}$의 정밀도는 그대로 낮음

### 실무 판독 규칙 한 줄

TMDD plot은 **용량별로 층화**해서 점검하는 게 첫걸음임. 고용량 곡선은 잘 맞는데 저용량 잔차가 체계적으로 한쪽으로 편향돼 있다면 — **이게 phantom linearity의 신호**임. 중심에서는 겉보기 성공인데 저농도 외삽에서는 편향이 숨어 있는 상태임. PK27의 123배 사건이 정확히 이 패턴이었음 [G&W p.609].

> 💡 **Phase 라벨은 시간이 아니라 농도 영역의 지문임.** 고용량 곡선만 가지고 있으면 target-mediated 경로가 포화돼서 **곡선이 선형처럼 보일 수 있음.** Full TMDD와 MM 중 무엇을 쓸지 결정하기 전에, 용량별 층화 곡선에서 **실제로 관찰된 phase가 무엇인지 먼저 표시**해 둬야 함.

**M3 한 줄**: 보이는 phase가 곧 식별 가능한 mechanism임. 고용량 적합만 평가하는 함정을 피해야 phantom linearity에 안 속음.

---

## M4 — Full TMDD: 4-state ODE의 정체 [⚡ Apex Concept]

M3에서 4 phase가 농도 영역의 지문이라는 걸 잡았으면, 이제 그 지문을 만들어내는 ODE 자체를 분해해야 함. 이게 Full TMDD임.

### Full TMDD는 "복잡한 MM"이 아님

먼저 가장 자주 하는 오해부터 깨야 함. Full TMDD는 "MM에 target·complex라는 이름표를 붙인 복잡한 saturable clearance 모델"이 아님. **ligand disposition, target turnover, binding, complex sink를 서로 다른 state와 ODE 항으로 분리하는 모델**임.

여기서 한 마디로 못 박을 수 있음 — **관찰 species가 없는 mechanism은 추정값이 아니라 가정임.**

### 4개의 상태변수

PK27은 이걸 "8-parameter full TMDD model"이라고 부름. $V_c=0.05$ L·kg⁻¹를 fixed해 둔 상태에서 Table 27.2가 보고하는 8개의 추정 파라미터를 말함. fixed $V_c$까지 structural quantity로 세면 **4 state + 9 structural quantities**임 [G&W pp.603, 608–609]:

| 상태변수 | 의미 |
|---|---|
| $L_c$ | central 구획의 ligand |
| $L_t$ | tissue/peripheral 구획의 ligand |
| $R$ | free target/수용체 |
| $RL$ | ligand-target complex |

$$
\underbrace{\mathbf{x}(t)}_{\text{TMDD 상태벡터}}
=
\left(
\underbrace{L_c}_{\text{central ligand}},
\underbrace{L_t}_{\text{tissue ligand}},
\underbrace{R}_{\text{free target}},
\underbrace{RL}_{\text{LT complex}}
\right)
$$

PK27 Table 27.2의 8개 보고 파라미터는 $Cl$, $k_{on}$, $k_{off}$, $V_t$, $Cl_d$, $k_{out}$, $R_0$, $k_{e(RL)}$임. $V_c$는 $0.05$ L·kg⁻¹로 fixed.

### 핵심 ODE — Target과 Complex 식

ligand 식은 일반적인 2구획 + binding sink 형태이고, 진짜 핵심은 **target과 complex 식**임:

$$
\begin{aligned}
\overbrace{\frac{dR}{dt}}^{\text{free target 변화}}
&=
\underbrace{k_{in}}_{\text{target 생성}}
-\underbrace{k_{out}R}_{\text{target 자연 소실}}
-\underbrace{k_{on}LR}_{\text{LT 결합}}
+\underbrace{k_{off}RL}_{\text{complex 해리}} \\
\overbrace{\frac{dRL}{dt}}^{\text{complex 변화율}}
&=
\underbrace{k_{on}LR}_{\text{complex 형성}}
-\underbrace{k_{off}RL}_{\text{해리}}
-\underbrace{k_{e(RL)}RL}_{\text{complex sink}}
\end{aligned}
$$

여기서 **절대 헷갈리면 안 되는 한 줄** — 결합 속도항은 $k_{on}\cdot L\cdot R$임. $k_{in}\cdot L\cdot R$이 아님. $k_{in}$은 **target 합성** 쪽이고, $k_{on}$은 ligand-target 결합의 **2차 on-rate**임. 표기 차이가 아니라 **turnover process와 binding process를 분리**하는 핵심 갈림길임 [G&W p.604; G&W pp.606–607]:

$$
\underbrace{\mathrm{BIND}}_{\text{complex 형성속도}}
=
\underbrace{k_{on}}_{\text{2차 on-rate}}
\cdot
\underbrace{L}_{\text{ligand}}
\cdot
\underbrace{R}_{\text{free target}}
\quad \ne \quad
\underbrace{k_{in}\cdot L\cdot R}_{\text{process 혼합 (오류)}}
$$

### 자료 풍부도 — 이 세션의 진짜 결론

여기가 이 카드, 그리고 이 세션 전체의 결론에 가까운 부분임. PK27은 세 데이터셋을 비교함:

- **Dataset I**: ligand 단독
- **Dataset II**: ligand + target
- **Dataset III**: ligand + target + complex

target과 complex 시간경과 데이터가 추가될수록 핵심 파라미터의 정밀도가 줄줄이 좋아짐. Table 27.2의 CV% 변화:

$$
\begin{aligned}
\underbrace{CV\%(k_{on})}_{\text{kon 정밀도}} &: \underbrace{17\to2\to1}_{\text{자료 풍부도}},\\
\underbrace{CV\%(k_{off})}_{\text{koff 정밀도}} &: \underbrace{27\to13\to3}_{\text{target/complex 추가}},\\
\underbrace{CV\%(k_{e(RL)})}_{\text{sink 정밀도}} &: \underbrace{27\to23\to2}_{\text{complex 측정 효과}}
\end{aligned}
$$

한 줄로 정리하면 — **ligand 데이터는 nonspecific disposition과 가시적 phase 구조를 가르치고, target 데이터는 recovery와 saturation 경계를 가르치고, complex 데이터는 sink 거동을 가르침.** 자료 풍부도는 장식이 아니라 **어떤 ODE 항이 추정 가능해지는지를 결정하는 변수**임 [G&W pp.603, 608–609].

> 💡 **식별성의 분업표**:
> - **ligand 데이터** → disposition을 가르침
> - **target 데이터** → recovery와 saturation 경계를 가르침
> - **complex 데이터** → sink를 가르침
>
> 측정 안 한 species의 파라미터는 "추정값"이 아니라 "가정"임.

### 적합 품질 ≠ 기전 타당성 — PK27의 123배 사건

여기가 이 세션 hook의 정체임. PK27에서:

$$
\underbrace{\frac{K_{m,\mathrm{MM}}}{K_{m,\mathrm{TMDD}}}}_{\text{MM bias}}
=
\underbrace{\frac{3.7}{0.03}}_{\text{PK27 비교}}
\approx
\underbrace{123}_{\text{123배 과대}}
$$

reduced model은 가장 높은 세 ligand 곡선은 상당히 잘 맞춤. 그런데 **가장 낮은 곡선에서는 실패**함. 그 결과로 MM 모델의 $K_m$이 Full TMDD의 $K_m$ 대비 123배 과대추정됨. 이 편향은 trough 예측, target occupancy 추정, subgroup 외삽으로 그대로 전파됨 [G&W p.609].

왜 이런 일이 일어났냐 — 풀어 보면 이렇게 됨. MM 근사는 **drug $\gg$ target** 조건(즉 $L \gg R$ 또는 $L \gg K_d$에서 binding이 빠르게 quasi-equilibrium에 도달하고 target 경로가 지속 포화되는 상태)에서만 Full TMDD로부터 구조적으로 유도됨. 근사 조건이 깨지는 농도 영역 — **ligand 농도가 $K_d$ 또는 $K_m$ 부근(target saturation 전환점)으로 떨어지는 구간**, 그리고 **매우 낮은 농도의 linear regime** — 에서 MM 근사는 PK 거동을 구조적으로 잘못 예측함. PK27의 $K_m$ 0.03 vs 3.7이 바로 이 경계 위반의 정량 흔적임.

**임상 실무에서 이게 어떻게 드러나냐** — 저용량 Phase 1 데이터에서 MM 모델이 OFV·VPC 기준으로 잘 맞은 것처럼 보일 수 있음. 그런데 중간 용량 범위의 비선형 전환점(Phase B↔C↔D 전이)을 mechanistic하게 예측 못 해서 **Phase 2 dose selection이 어긋남**. 또는 고용량 데이터셋만으로 적합된 MM이 sub-population(저체중, 고 target burden, 초기 dose interval) 외삽에서 trough 노출을 체계적으로 잘못 예측해서 후속 임상 의사결정의 출발점이 흔들림.

### NONMEM 스타일 구현 — 단위 정합성 한 번에 정리

다음은 교과서 control stream이 아니라 **PK27/R&T ODE 구조를 NONMEM 스타일로 교육 목적 번역**한 골격임. 단위 정합성을 학습자가 직접 확인할 수 있도록 **두 가지 표기 선택지**를 명시함.

**(a) 모든 상태변수를 농도로 두는 경우** — R&T Eq.21-1~21-4 표기와 일치 [R&T p.711]:

```text
; (a) concentration-based: A(i)는 농도로 직접 처리
CLIG = A(1)        ; ligand concentration in central
CTIS = A(2)        ; ligand concentration in tissue
R    = A(3)        ; free target concentration
RL   = A(4)        ; complex concentration

BIND = KON * CLIG * R          ; conc/time, no volume factor
DISS = KOFF * RL
SINK = KERL * RL

DCDT(1) = INPUT/VC - (CL/VC)*CLIG - (Q/VC)*(CLIG-CTIS) - BIND + DISS
DCDT(2) = (Q/VT)*(CLIG-CTIS)
DCDT(3) = KIN - KOUT*R - BIND + DISS
DCDT(4) = BIND - DISS - SINK
```

**(b) 모든 상태변수를 amount로 두고 명시적 volume 변환을 박는 경우** — NONMEM의 표준 DADT 표기와 일치:

```text
; (b) amount-based: A(i)는 amount, binding 전에 농도로 변환
CLIG = A(1)/VC      ; central concentration
CTIS = A(2)/VT      ; tissue concentration
RC   = A(3)/VR      ; free target concentration (plasma target이면 VR=VC)
RLC  = A(4)/VR      ; complex concentration

BIND = KON * CLIG * RC * VR    ; amount/time — 명시적 volume 변환
DISS = KOFF * A(4)
SINK = KERL * A(4)

DADT(1) = INPUT - CL*CLIG - Q*(CLIG-CTIS) - BIND + DISS
DADT(2) =  Q*(CLIG-CTIS)
DADT(3) =  KIN*VR - KOUT*A(3) - BIND + DISS    ; KIN as conc/time → multiply by VR
DADT(4) =  BIND - DISS - SINK
```

> ⚠️ **두 표기를 절대 섞으면 안 됨.** 흔한 함정 — `BIND = KON * CLIG * R * VC`라고 쓰는 경우가 있는데, 이 식은 **R이 농도일 때만** 옳음. R이 amount이면 추가 volume 변환이 필요해서 mass balance가 조용히 깨짐. PK27 원전(G&W Eq.27:1~27:3)의 mass-balance는 둘 중 하나로 **일관되게** 잡혀야 함 — concentration-based(DCDT)이거나 amount-based(DADT, 모든 binding 항에 명시적 volume 변환)이거나. R&T Eq.21-1~21-4도 농도 기반 표기를 일관되게 사용함 [G&W pp.606–607; R&T p.711].

**실무 디버깅 한 줄**: 두 표기를 혼용하면 정상상태에서 $R_0 = k_{in}/k_{out}$ 관계가 미묘하게 어긋나서, 모델은 적합되지만 baseline drift가 **자료가 아닌 표기 오류 때문에** 만들어짐. 가장 안전한 디버깅은 dose=0 simulation에서 $R$이 정확히 $R_0$로 수렴하는지를 먼저 확인하는 것임.

### Soluble target vs Membrane-bound target — 임상 분기점

PK27이 다루는 데이터는 **soluble target**임 [G&W p.602]. 그런데 임상 mAb 분석에서는 target이 soluble이냐 membrane-bound이냐가 **TMDD signature의 phase 구조 자체를 바꾸는 분기점**임. G&W도 PK27 본문에서 "membrane bound targets could have very different impact on the ligand disposition"이라고 명시적으로 경고함 [G&W p.605].

| 비교 기준 | Soluble target (VEGF, TNF-α, IgE) | Membrane-bound (HER2, CD20, CD11a) |
|---|---|---|
| Complex의 운명 | drug-target complex가 **혈장 같이 순환** | complex가 세포 안으로 **internalize**되어 곧장 sink |
| Target turnover | 혈장에서 $k_{in}/k_{out}$ 측정 가능 | 세포 표면 발현·shedding·internalization이 얽힘 |
| Phase A 신호 | rapid binding이 혈장 곡선에 잘 보임 | internalize가 빠르면 Phase A가 흡수돼서 안 보일 수 있음 |
| Total assay 해석 | total = free + complex (둘 다 혈장) | total이 shed antigen만 잡고 막결합 target은 못 잡음 |
| 대표 mAb | bevacizumab, adalimumab, omalizumab | trastuzumab, rituximab, efalizumab |

수식으로 보면 두 시나리오 차이는 complex의 운명에 직접 들어감:

$$
\overbrace{\frac{dRL}{dt}}^{\text{complex 변화}}
=
\underbrace{k_{on}LR}_{\text{형성}}
-\underbrace{k_{off}RL}_{\text{해리}}
-\overbrace{\underbrace{k_{e(RL)}RL}_{\text{soluble: 혈장 청소}}\ \text{vs}\ \underbrace{k_{int}\cdot RL}_{\text{membrane: internalize 직행}}}^{\text{이 항의 의미가 갈리는 지점}}
$$

수학 형태는 같은 1차 소실 항인데, **물리적 해석이 다름**. soluble에서는 $k_{e(RL)}$이 ligand의 nonspecific clearance와 같은 capillary/RES 경로일 가능성이 높고, membrane-bound에서는 $k_{int}$가 receptor internalization·lysosomal degradation의 결합 속도임.

**실무 한 줄**: 새 mAb 후보의 TMDD 모델링 시작할 때 가장 먼저 적어야 하는 한 줄은 "이 target은 soluble인가, membrane-bound인가, 아니면 shed antigen이 둘 다 만들어지는가?"임. PK27의 4-state Full TMDD 골격은 soluble target에 가장 직접 적용되고, membrane-bound나 shed-antigen 시나리오에서는 추가 state(membrane R, shed R, 두 종류의 complex)가 필요해질 수 있음 [R&T p.751, Fig.22-20].

### ADA — TMDD signature의 시간 의존 변형

soluble vs membrane-bound가 **target 쪽 분기**라면, ADA는 **숙주 면역계 쪽 분기**임. PK27의 single-dose 데이터에서는 ADA가 안 보이지만, **임상 mAb의 repeated-dose 데이터에서는 ADA 형성이 TMDD signature를 시점에 따라 변형**시킴 [R&T p.712].

기전 — anti-drug antibody가 형성되면 mAb-ADA 면역복합체가 phagocytic cell의 uptake와 lysosomal degradation을 자극해서 mAb 청소율을 끌어올림.

| TMDD signature 변형 | 임상·모델링 신호 |
|---|---|
| **Phase B(linear) 청소율 급증** | nonspecific linear CL이 target turnover 변화 없이 시간에 따라 증가 |
| **BSV 폭발** | 일부 환자만 trough가 sub-therapeutic으로 떨어지고 나머지는 그대로 — bimodal |
| **시점 의존 PK** | 같은 환자 PK가 dose 초기와 후반에서 다름 — IOV 또는 dose-time interaction |

ADA 시간 척도 — R&T Fig.21-19(cynomolgus monkey의 anti-tetanus toxoid ADA)가 보여줌. **ADA titer가 약 200시간(약 8~9일)에서 검출 시작, 약 400~500시간(약 17~21일)에 정점** [R&T p.725]. 이 정도 시간 척도면 multiple-dose mAb PK 데이터의 두 번째·세 번째 dose 구간부터 covariate-naive linear CL 가정이 깨질 수 있음.

수식으로 보면 Full TMDD ligand 항에 시간 의존 1차 sink 항이 추가되는 형태임:

$$
\overbrace{\frac{dL}{dt}}^{\text{ligand 변화율}}
=
\underbrace{(\text{기존 TMDD 항})}_{\text{nonspecific CL + TMDD 경로}}
-\overbrace{\underbrace{k_{ADA}(t)\cdot L}_{\text{면역복합체 매개 sink}}}^{\text{시간 의존 1차 추가 항}}
$$

ADA 위험 인자 [R&T p.725]:
- 투여 경로: **s.c. > i.m. > i.v.**
- 분자 응집 정도: 응집 ↑ → 면역원성 ↑
- 단백질 인간 유사도: murine > chimeric > humanized > human

> ⚠️ **모델링 함정** — ADA-매개 청소율 증가를 단순 "target turnover 변화"로 잡으면 $k_{in}$이나 $R_0$를 잘못 추정함. 두 신호는 **시간 위계가 다름** — target turnover 변화는 보통 baseline 시점부터 차이가 있는 반면, ADA-매개 변형은 **dose 후 약 200h 이후부터 켜지는 시간 지연 신호**임. ADA가 의심되는 데이터에서는 **dose-elapsed-time covariate**나 occasion-based IOV 구조로 두 신호를 분리할 수 있는지 먼저 살펴봐야 함.

**실무 한 줄**: ADA 형성 이후의 TMDD signature는 single-dose 4-phase에서 벗어나서 **"시점에 따라 다른 phase 구조"**를 보임. multiple-dose mAb 데이터 분석 시 **(i) ADA assay 결과 가용성, (ii) dosing occasion별 IOV 구조, (iii) Phase B 영역의 시간 의존 CL drift** — 이 세 가지를 ADA 가능성 점검표로 갖고 가야 함.

**M4 한 줄**: Full TMDD의 핵심은 "파라미터가 많다"가 아니라 **ligand 곡선 안에 숨어 있는 target turnover·binding·complex sink를 분리하는 것**임. target과 complex 데이터가 같이 있어야 $k_{on}$, $k_{off}$, $k_{e(RL)}$의 식별성이 개선됨. ligand-only 적합이 좋아 보일 때는 "biologically learned"가 아니라 "fitted but not learned"일 수 있다는 걸 기억해야 함.

---

## M4½ — QSS: Full과 MM 사이의 실무 표준

M4의 Full TMDD와 M5의 MM 사이에는 **중간 근사 단계가 사슬처럼 있음**. 임상 mAb 분석에서 실제로 가장 많이 쓰이는 건 Full도 MM도 아니라 그 사이의 **준정상상태(QSS) 근사**임. R&T 본문이 PK27 4-phase 그림 바로 다음 문단에서 *"Alternatively, quasi-steady state or quasi-equilibrium approximations can be used"*라고 명시함 [R&T p.712].

여기서 핵심 — **QSS를 "MM의 별명"으로 외우면 안 됨.** QSS는 complex의 동역학에 대한 명시적 가정을 두고 **ligand·target 수준에서 식별성을 회복**시키는 단계임. MM은 그 위에 "drug $\gg$ target"이라는 한 가지 가정을 더 얹어서 한 항으로 접은 형태임. 그래서 QSS는 보통 MM보다 **더 넓은 농도 영역에서 방어 가능**하고, biologics PopPK 실무의 출발점이 됨.

### 근사 위계 — 한 표로 정리

| 근사 단계 | 핵심 가정 | 식별 가능한 양 | 주된 사용처 |
|---|---|---|---|
| **Full TMDD** | 가정 없음 | $R_0, k_{out}, k_{on}, k_{off}, k_{e(RL)}$ | target·complex 자료 풍부할 때 |
| **Rapid Binding (RB) / Quasi-Equilibrium (QE)** | $k_{on}, k_{off} \gg k_{e(RL)}$ | $K_d = k_{off}/k_{on}$ 중심 | 매우 강한 결합 [R&T p.712] |
| **Quasi-Steady-State (QSS)** ▶ **실무 표준** | $d[RL]/dt \approx 0$ | $K_{ss} = (k_{off}+k_{e(RL)})/k_{on}, R_0, k_{out}$ | 대부분의 biologics PopPK 출발점 |
| **Michaelis-Menten (MM)** | $L \gg R$ 또는 occupancy ≈ 100% | $V_{max}, K_m$ (target/complex 식별 불가) | 자료 한정, 고용량 내삽 위주 |

### QSS 도출 — 한 줄로 이해하기

Full TMDD의 complex 식 (R&T Eq.21-4)에서 출발:

$$
\overbrace{\frac{d[RL]}{dt}}^{\text{complex 변화율}}
=
\underbrace{k_{on}\,L\,R}_{\text{형성}}
-\underbrace{(k_{off}+k_{e(RL)})\,RL}_{\text{해리+sink}}
$$

QSS 가정 — complex가 ligand·target보다 훨씬 빠른 time scale로 평형 도달. 우변 ≈ 0:

$$
\underbrace{k_{on}\,L\,R}_{\text{형성}}
\approx
\underbrace{(k_{off}+k_{e(RL)})\,RL}_{\text{해리+sink}}
\quad\Longrightarrow\quad
\overbrace{\underbrace{K_{ss}}_{\text{QSS 상수}}
=
\frac{\underbrace{k_{off}+k_{e(RL)}}_{\text{소실 합}}}{\underbrace{k_{on}}_{\text{결합}}}}^{\text{Mager-Krzyzanski식 정의}}
$$

여기서 **$K_{ss}$는 수식적으로 $K_m$과 동일한 형태**임. 그런데 의미는 다름:
- $K_m$ = "겉보기 saturation 경계" (MM에서)
- $K_{ss}$ = **complex의 quasi-steady-state로부터 명시적으로 유도된 ligand·target 평형 상수** (QSS에서)

같은 분수식, 다른 가정, 다른 해석임.

QSS 가정 아래 total target $R_{tot} = R + RL$ 관계에서 free $R$과 complex $RL$이 풀려나옴:

$$
\underbrace{R}_{\text{free target}}
=
\frac{\overbrace{R_{tot}\cdot K_{ss}}^{\text{총 target × QSS 상수}}}{\underbrace{K_{ss}+L}_{\text{ligand 농도 의존}}}
,\qquad
\underbrace{RL}_{\text{complex}}
=
\frac{\overbrace{R_{tot}\cdot L}^{\text{총 target × ligand}}}{\underbrace{K_{ss}+L}_{\text{포화 분모}}}
$$

이 두 식이 가르치는 게 뭐냐 — **complex 데이터를 명시적으로 추적하지 않아도, ligand와 total target만으로 $K_{ss}$를 식별할 수 있음.** Full TMDD가 요구하던 "complex assay 풍부도"를 우회함. 이게 biologics PopPK 실무에서 QSS가 거의 표준이 된 이유임.

### MM과의 관계 — "한 가정 더 얹으면 MM"

QSS에 추가로 **$L \gg R$** (target occupancy ≈ 100%) 가정을 얹으면 MM이 나옴:

$$
\underbrace{K_{ss}}_{\text{QSS}} \xrightarrow{\,L\gg R\text{ 가정 추가}\,} \underbrace{K_{m}}_{\text{MM}}
,\qquad
\underbrace{V_{max}}_{\text{MM}} \approx \underbrace{k_{e(RL)}\cdot R_{tot}}_{\text{포화 시 sink 처리능}}
$$

여기서 결정적 차이 — MM에서는 **$R_{tot}$ 자체가 보이지 않게 잠긴 형태**임. 그래서 MM은 target turnover ($k_{in}, k_{out}$)와 complex sink ($k_{e(RL)}$)를 분리해서 추정할 수 없고, $V_{max}/K_m$이라는 두 macro-parameter만 남음. **PK27에서 $K_m$이 0.03 → 3.7로 123배 부풀려졌던 이유 중 하나가 정확히 이거임** — MM은 $R_{tot}$의 변동을 추적할 도구를 잃기 때문에, 저용량(target이 포화되지 않은 영역)에서 구조 편향이 누적됨 [G&W p.609].

### 임상 mAb에서 QSS가 표준인 이유

R&T가 이 자리에서 강조하는 핵심 — **임상 자료만으로 $k_{on}$과 $k_{e(RL)}$를 분리하는 건 free target 또는 complex 측정 없이는 거의 불가능함** [R&T p.712]. QSS는 이 식별성 한계를 정면으로 다룸. 두 micro-parameter를 분리하는 대신, **두 값의 합으로 정의되는 macro-parameter $K_{ss}$**를 식별함.

실무 시나리오별 권고:

| 시나리오 | 권고 모델 | 이유 |
|---|---|---|
| Preclinical, target·complex 풍부 | **Full TMDD** | 모든 micro-parameter 식별 가능 |
| Clinical Phase 1, ligand·total target 측정 | **QSS** | $K_{ss}, R_0, k_{out}$ 식별; complex 측정 불필요 |
| Clinical PopPK, ligand만 측정 | **Parallel linear + MM** 또는 **QSS with prior** | 자료 한정, QSS는 prior로 보강 가능 |
| Phase 1 SAD, occupancy ≥ 95% 유지 | **MM (제한적)** | 좁은 농도 범위 내삽만 |

### 세 K 상수 한 자리에

> 💡 **세 가지 K 상수를 절대 같은 단어로 부르면 안 됨.**
>
> $$
> \overbrace{K_d}^{\text{thermodynamic}} = \frac{k_{off}}{k_{on}}
> \quad<\quad
> \overbrace{K_{ss}}^{\text{QSS 가정 하}} = \frac{k_{off}+k_{e(RL)}}{k_{on}}
> \quad=\quad
> \overbrace{K_{m}}^{\text{MM 가정 하}} = \frac{k_{off}+k_{e(RL)}}{k_{on}}
> $$
>
> $K_{ss}$와 $K_m$은 **분수식이 같지만 도출 가정이 다름.** $K_{ss}$는 "complex의 QSS"라는 한 가지 가정만 두고 ligand·total target 수준에서 식별되는 반면, $K_m$은 추가로 "$L \gg R$"을 가정해서 $R_{tot}$가 사라진 형태임. $K_d$는 $k_{e(RL)}$이 포함되지 않는다는 점에서 두 동역학 상수와 본질적으로 다름. 리포트에서 셋을 같은 단어로 부르면 reviewer가 반드시 reconciliation을 요구함.

### QSS의 한계

QSS는 만능이 아님:
- **complex 동역학이 ligand·target 동역학과 같은 time scale**이면 QSS 가정이 깨짐 (예: internalize가 매우 느린 membrane-bound target)
- QSS는 $k_{on}$과 $k_{e(RL)}$를 **개별 식별 못함**. 두 값의 합비 $K_{ss}$만 식별. "target receptor occupancy를 micro-parameter 수준에서 mechanistic하게 시뮬레이션" 같은 요구가 있으면 Full TMDD 필요
- **soluble target에서 가장 깔끔하게 작동**. membrane-bound나 shed antigen 시나리오는 추가 state 필요

**M4½ 한 줄**: Full TMDD와 MM은 같은 사슬의 양 끝이고, 그 사이에 **QSS와 QE라는 명시적 가정 단계**가 있음. 임상 mAb 분석의 실무 표준은 보통 QSS임. MM은 그 위에 "$L \gg R$" 가정을 더 얹은 더 좁은 도구임. $K_{ss}$와 $K_m$이 같은 분수식을 갖는 이유는 우연이 아니라 **MM이 QSS의 한 가지 추가 가정 하 특수 경우**이기 때문임.

---

## M5 — Michaelis-Menten의 경계: PK27 사건의 정량 흔적

M4½에서 QSS가 Full과 MM 사이의 다리라는 걸 잡았으면, 이제 결정해야 함 — **어떤 조건에서 이 사슬의 끝(MM) 한 줄로 접어도 되는가?**

### MM은 "단순한 대체 모델"이 아님

MM 근사는 Full TMDD의 target과 complex 하부 시스템을 $V_{max}$와 $K_m$로 줄이는 거임. $R$과 $RL$을 직접 추적하지 않고 target-mediated 경로를 하나의 saturable clearance 항으로 접음. 진짜 문제는 적합이 아니라 — **어느 농도·occupancy 영역에서 이 접기가 구조적으로 허용되는가**임 [G&W p.609; R&T p.712]:

$$
\overbrace{Cl_{MM}}^{\text{포화 TMDD CL}}
=
\frac{\underbrace{V_{max}}_{\text{최대 처리능}}}{\underbrace{K_m}_{\text{반포화 경계}}+\underbrace{C}_{\text{ligand 농도}}}
$$

Full TMDD 안에서 두 상수의 정의를 같이 보면 차이가 명확함:

$$
\overbrace{K_d}^{\text{결합 해리상수}}
=
\frac{\underbrace{k_{off}}_{\text{해리 속도}}}{\underbrace{k_{on}}_{\text{결합 속도}}},
\qquad
\overbrace{K_m}^{\text{겉보기 동역학상수}}
=
\frac{\overbrace{k_{off}+k_{e(RL)}}^{\text{해리+sink}}}{\underbrace{k_{on}}_{\text{결합 속도}}}
$$

$K_d$는 binding affinity에 가까운 **thermodynamic 해리상수**이고, $K_m$은 complex loss($k_{e(RL)}$)까지 포함한 **apparent kinetic 상수**임 [G&W pp.603–609; R&T pp.711–712].

> 💡 **MM은 접힌 모델임.** $V_{max}/K_m$은 target biology를 제거한 게 아니라 관찰 가능한 saturable 항으로 압축한 거임. 그래서 $K_m$은 $K_d$가 아님 — $K_m$에는 complex sink $k_{e(RL)}$가 들어감. 관찰된 saturation·occupancy 영역 밖에서는 고용량 적합이 아무리 좋아도 MM 외삽을 정당화할 수 없음.

### MM이 통할 수 있는 4가지 조건

[G&W p.609; R&T p.712]:

- ligand 농도가 target 농도를 크게 초과할 때
- target occupancy가 거의 완전 포화일 때
- 관찰된 용량 범위가 제한적일 때
- 목적이 저농도 외삽이 아니라 **관찰 프로파일 내 내삽**일 때

### PK26 Efalizumab — "reduced model이 정당화된 앵커"

**Efalizumab**(anti-CD11a IgG1 mAb, 건선 치료제) 사례인 **PK26**이 좋은 reduced-model 앵커임. 2구획 모델에 parallel linear/MM 제거가 사용됨. target/complex 데이터와 $k_{on}/k_{off}/K_d$ 정보가 없어서 full TMDD 적합 자체가 불가능했기 때문임. 보고된 추정값:

$$
\overbrace{\{V_t,V_{max},K_m,CL_d,CL_L\}}^{\text{PK26 reduced set}}
=
\underbrace{\{0.061,0.039,0.161,0.031,0.007\}}_{\text{보고 추정값}}
$$

이 reduced model은 single-dose iv bolus 데이터의 5개 정맥주사 시간경과에 적합됨. → **"제한된 데이터에서 reduced model이 정당화된 앵커"로 읽어야 함**. "MM이 보편적으로 mechanistic이다"라는 증거가 아님 [G&W pp.599–601].

### PK27 — MM이 무너지는 정량 흔적

PK27에서 MM은 가장 높은 세 농도 곡선은 비교적 잘 맞춤. 그런데 **가장 낮은 농도 곡선에서는 곡선이 따로 놀았고, 추정된 $K_m$이 3.7로 잡혀서 Full TMDD의 0.03보다 약 123배 부풀려짐** [G&W p.609].

임상 교훈은 "MM을 쓰지 마라"가 아님. 더 좁고 실용적임 — **target saturation이 실증된 농도·occupancy 영역 밖에서는 MM을 쓰지 마라.**

### Occupancy 검증 — 실무 결정 기준

대략 **90–95% 이상의 occupancy**가 유지되는 영역에서는 단순화가 허용될 수 있음. occupancy가 $K_d$ 또는 biomarker 역가 이하로 떨어지면 MM이 충분하지 않음 [G&W p.609]:

$$
\underbrace{\mathrm{Occupancy}}_{\text{target 결합비율}}
\gtrsim
\underbrace{90\text{--}95\%}_{\text{고포화 영역}}
$$

**실무 준칙**: TMDD 가능성이 있는 mAb에 MM을 쓰는 리포트라면, **관찰된 농도 범위, target 농도 범위, 투여 간격 동안의 최소 예측 target occupancy**를 명시해야 함. 이건 소스 경계의 구현 해석이지 규제기관이 직접 인용한 요건은 아님.

### MM이 잃어버리는 것

MM은 $R_0$, $k_{out}$, $k_{on}$, $k_{off}$, $k_{e(RL)}$의 명시적 해석을 잃음. 고용량이나 중심 곡선에 가중치가 쏠리면 저농도 편향이 가려지고, 추가 가정 없이는 target recovery나 complex sink 질문에 답할 수 없음. **이때 한 단계 덜 압축된 도구가 M4½에서 다룬 QSS 근사**임 — complex만 quasi-steady-state로 두고 $R_0$, $k_{out}$, $K_{ss}$를 그대로 식별할 수 있어서 임상 mAb PopPK 실무의 출발점이 됨 [R&T p.712].

**M5 한 줄**: MM은 빠르고 편한 실무 도구일 수 있는데, **"적합이 잘 됨"과 "target biology를 올바르게 외삽함"은 같은 말이 아님.** 관찰된 포화 영역 안에서 내삽할 때는 MM이 실무적으로 방어 가능한데, 저농도 trough·recovery·occupancy 외삽에서는 Full TMDD나 추가 데이터가 지배해야 함. 고용량 적합이 좋다고 MM이면 충분하다고 결론지으면 **PK27처럼 $K_m$ 과대예측과 저용량 구조 편향이 그대로 임상 결정에 들어감**.

---

## §5 자주 혼동되는 4 쌍 — 단어 하나가 리포트를 흔드는 자리들

다섯 카드를 다 통과해도 실무에서 흔들리는 단어들이 있음. `fit`, `affinity`, `linearity`, `half-life` — 친숙해서 안 묻고 넘어가는데, TMDD에서는 전부 **조건부 의미**를 가짐. 이 네 쌍을 분리해 두면 리포트 한 문장의 무게가 달라짐.

### ▌ Pair 1 — $k_{in}$ vs $k_{out}$

| 비교 기준 | $k_{in}$ | $k_{out}$ |
|---|---|---|
| 단위 | mass/time | time⁻¹ |
| 수식 위치 | $A_0=k_{in}/k_{out}$의 분자 | $A_0$ 분모, $t_t=1/k_{out}$의 분모 |
| 변화 원인 | 합성·입력 증가/감소 | catabolism 속도 변화 |
| 혼동 시 결과 | level만 보고 시간 척도 변화로 오해 | level과 회복 시간 변화 모두 놓침 |

$$
\underbrace{k_{in}}_{\text{mass/time 입력}}
\quad\ne\quad
\underbrace{k_{out}}_{\text{시간}^{-1}\text{분획 소실}},
\qquad
\underbrace{A_0}_{\text{level}}
=
\frac{\underbrace{k_{in}}_{\text{level 상승}}}{\underbrace{k_{out}}_{\text{level↓/시간↓}}}
$$

**한 줄로 박아두기**: $k_{in}$은 수도꼭지, $k_{out}$은 배수구임. **수위만 보지 말고 새 수위에 도달하는 시간까지 같이 봐야 함.**

### ▌ Pair 2 — Full TMDD vs MM 근사 ▶ **Critical Blow**

| 비교 기준 | Full TMDD | MM 근사 |
|---|---|---|
| 차원 | ligand·target·complex state ODE system | 하나의 saturable clearance 항 |
| 수식 위치 | $k_{on}LR, k_{off}RL, k_{e(RL)}RL$로 분리 | $Cl_{MM}=V_{max}/(K_m+C)$로 압축 |
| 변화 원인 | binding, turnover, complex sink, nonspecific CL | 관찰 포화 범위와 apparent $V_{max}/K_m$ |
| 혼동 시 결과 | data-rich mechanism 식별 가능 | 저용량 trough·occupancy·subgroup 외삽 편향 |

흔한 혼동과 교정:

| 흔한 혼동 | 교정 |
|---|---|
| Full TMDD는 복잡하고 MM은 단순한 대체 모델임 | MM은 Full TMDD의 target/complex 하부 시스템을 reduction한 것임 |
| 고용량 적합이 좋으면 MM이 충분함 | PK27에서 고용량 곡선 적합이 좋아도 저용량 곡선이 따로 놀고 $K_m$이 123배 부풀려짐 |
| target/complex assay는 있으면 좋은 부가자료임 | target/complex는 $k_{on}, k_{off}, k_{e(RL)}$의 정밀도를 결정하는 **식별 자료**임 |

**기억 고리** — 완전 지도 vs 단순화 지도. Full TMDD는 binding on/off, complex internalization, target 생성·분해를 다 명시한 **완전 지도**임. MM 근사는 특정 농도 영역($L \gg R$ 또는 $L \gg K_d$의 quasi-equilibrium)에서 이 복잡성을 **하나의 포화곡선으로 압축한 단순화 지도**임. 단순화 지도는 그려진 스케일을 벗어나면 틀린 경로를 알려줌. drug 농도가 $K_d$ 또는 $K_m$ 부근으로 떨어지면 MM은 TMDD 거동을 재현 못함. **PK27의 $K_m$ 0.03 → 3.7 과대예측이 바로 이 "지도 밖 영역"의 정량 흔적임.**

> **▶ Critical Blow**: 이 혼동을 안고 first-in-human 저용량 외삽이나 sub-population 외삽으로 임상 의사결정을 강행하면 세 경로의 실패가 옴 — **(i) 저농도 trough 과대평가로 sub-therapeutic 노출 환자군 누락, (ii) dosing interval 동안 target occupancy가 적합 범위 밖으로 떨어져도 검출 안 됨, (iii) sub-population 외삽이 실증된 saturation 영역 밖에서 이뤄짐.**

### ▌ Pair 3 — TMDD에서 $K_d$ vs $K_m$

| 비교 기준 | $K_d$ | $K_m$ |
|---|---|---|
| 단위 | concentration | concentration |
| 수식 위치 | $K_d=k_{off}/k_{on}$ | $K_m=(k_{off}+k_{e(RL)})/k_{on}$ |
| 변화 원인 | binding 친화도 | binding + complex 손실/internalization |
| 혼동 시 결과 | in vitro 친화도를 in vivo 경계로 오독 | occupancy·sink 영향 오해석 |

$$
\underbrace{K_d}_{\text{결합 친화도}}
=
\frac{\underbrace{k_{off}}_{\text{해리}}}{\underbrace{k_{on}}_{\text{결합}}},
\qquad
\underbrace{K_m}_{\text{disposition}}
=
\frac{\underbrace{k_{off}}_{\text{해리}}+\underbrace{k_{e(RL)}}_{\text{complex sink}}}{\underbrace{k_{on}}_{\text{결합}}}
$$

$K_d$와 $K_m$이 다른 이유는 단순함 — $K_m$에 $k_{e(RL)}$이 들어가기 때문임. **리포트 쓸 때 in vitro thermodynamic $K_d$**와 **in vivo 모델에서 나온 apparent $K_m$**을 반드시 분리해야 함. 둘 다 "affinity"라고 부르면 내부에서도 혼동이 생기고, reviewer가 반드시 reconciliation을 요구함.

**기억 고리** — 친화력 vs 처리 속도. $K_d$는 ligand와 target의 **결합 친화력**, 얼마나 단단히 붙는가의 척도임. $K_m$은 결합 친화력에 complex의 **처리 속도(internalization)**까지 더한 apparent kinetic 상수임. 이 둘과 다른 차원에 있는 게 target turnover ($k_{in}/k_{out}$) — target 자체가 **얼마나 빨리 새로 만들어지고 분해되는가**라는 시스템 capacity임. **세 파라미터가 서로 독립**이라서 **in vitro $K_d$ 하나만으로 in vivo TMDD의 임상적 중요성을 판단할 수 없음.**

**한 줄로 박아두기**: $K_d$는 **결합의 언어**, $K_m$은 **결합 이후 sink까지 포함한 disposition의 언어**임.

### ▌ Pair 4 — 저농도 Linear PK vs 고농도 Linear PK

| 농도 영역 | 선형으로 보이는 이유 | 위험 |
|---|---|---|
| **Very low ligand** | target 경로가 포화되지 않아 비특이적·target-specific 1차 경로가 공존 | assay 민감도 낮으면 이 구간 놓침 |
| **Very high ligand** | target 경로 포화로 비특이적 청소율 지배 | 고용량 적합만 보고 MM/linear 모델을 과신 |
| **Middle range** | target saturation이 농도에 따라 변동 | nonlinear clearance가 가장 뚜렷 |

**기억 고리** — 고속도로 vs 병목 도로. 고용량에서 mAb PK가 선형으로 보이는 이유는, target이 이미 포화돼서 TMDD 경로가 더 이상 약물을 추가로 빨아들이지 못하고 비특이적 제거 경로(FcRn salvage가 작동하는 IgG-like clearance)가 지배하기 때문임 — **고속도로**임. 저용량에서 PK가 선형처럼 보이는 이유는 다름. target이 포화되지 않은 상태에서 1차 target-mediated 경로와 nonspecific 경로가 함께 작동하는데, **두 1차 경로의 합이므로 여전히 선형**임. 그러나 이 구간의 target 경로는 **병목 도로**여서, 농도가 조금만 변해도 지배 경로가 바뀜.

**두 linear regime 사이의 nonlinear transition이 임상 용량 범위 안에 걸쳐 있을 때 TMDD 모델링이 필수가 됨.** 고용량 데이터만 보고 "linear PK"라고 결론 내리면 저용량의 병목 도로 거동을 놓침.

**한 줄로 박아두기**: TMDD는 "선형 또는 비선형"이 아님. **농도에 따라 두 종류의 linearity와 한 구간의 nonlinearity가 이어지는 시스템**임 [G&W pp.604–605].

---

## §7 능동 회상 — "이 데이터가 어떤 항을 가르치는가"

답을 외우는 것보다 중요한 건 **"이 데이터가 어떤 phase와 어떤 ODE 항을 실제로 가르치는가?"**를 매번 그 자리에서 묻는 습관임. 아래 열 문제는 그 습관을 굳히는 용도임.

### Q1 ★ — Turnover 단위

$A_0 = k_{in}/k_{out}$에서 $k_{in}$과 $k_{out}$의 단위는?

**답**: $k_{in}$은 mass/time, $k_{out}$은 time⁻¹임. $A_0$는 두 값의 비율로 정의되는 baseline 양임 [G&W p.96].

$$
\underbrace{A_0}_{\text{baseline 양}}
=
\frac{\underbrace{k_{in}}_{\text{mass/time}}}{\underbrace{k_{out}}_{\text{시간}^{-1}}}
$$

**다음 깊이 질문**: 그렇다면 turnover time $t_t = 1/k_{out}$은 임상 PK에서 어떤 측정 가능한 양과 같은가? (M1 Eq.2:243이 단서)

### Q2 ★★ — Turnover 비대칭

왜 $k_{out}$ 변화는 정상상태 level과 도달 시간을 동시에 바꾸는가?

**답**: $k_{out}$은 분획 소실률이라서 baseline $A_0=k_{in}/k_{out}$과 time scale $t_t=1/k_{out}$에 **둘 다 동시에** 들어가기 때문임 [G&W pp.96–97].

$$
\underbrace{A_0}_{\text{SS level}}
=
\frac{k_{in}}{\underbrace{k_{out}}_{\text{level/시간 동시}}},
\qquad
\underbrace{t_t}_{\text{교체 시간}}
=
\frac{1}{\underbrace{k_{out}}_{\text{분획 소실}}}
$$

**다음 깊이 질문**: 이 비대칭이 linear kinetics 가정에 의존한다면, 높은 농도에서 $k_{out}$이 사실상 saturable이 되는 경우 $k_{in}$ 변화와 $k_{out}$ 변화는 어떻게 구별이 어려워지는가?

### Q3 ★★ — Full TMDD 상태변수

Full TMDD의 4개 상태변수는?

**답**: ligand central, ligand tissue/peripheral, free target $R$, ligand-target complex $RL$임 [G&W pp.604–607].

**다음 깊이 질문**: 이 4개 state 중 임상에서 직접 측정이 가장 어려운 것은? 그 측정 결손이 PK27 Table 27.2의 식별 위계($k_{on}$/$k_{off}$/$k_{e(RL)}$ 정밀도)에 어떤 구조 영향을 주는가?

### Q4 ★★ — 저용량 잔차의 진단

mAb ligand-only 데이터에서 고용량 곡선은 잘 맞는데 가장 낮은 용량에서 체계적인 under/over-prediction이 보임. 무엇을 의심해야 함?

**답**: MM 또는 reduced model이 관찰된 고용량 범위에서는 내삽을 잘 하지만, **저농도 TMDD phase를 제대로 설명하지 못할 가능성이 높음.** 이 판단은 측정된 용량·농도 범위에 한정되고, 외삽 영역에서는 target occupancy와 sensitivity analysis가 필요함 [G&W p.609].

**다음 깊이 질문**: 저용량 외삽을 모델 구조 변경 없이 정당화하려면 — target/complex assay 추가가 즉시 불가능한 상황에서 — 어떤 sensitivity analysis 절차를 어떤 순서로 수행해야 함?

### Q5 ★★ — $K_d$ vs $K_m$

$K_m$과 $K_d$가 다를 수밖에 없는 기전 이유는?

**답**: $K_d=k_{off}/k_{on}$은 결합/해리 평형이고, $K_m=(k_{off}+k_{e(RL)})/k_{on}$은 complex의 비가역적 소실($k_{e(RL)}$)까지 포함함. complex sink가 있으면 **$K_m$은 thermodynamic 친화도가 아니라 apparent kinetic 상수**가 됨 [G&W p.609; R&T p.712].

$$
\underbrace{K_d}_{\text{결합 평형}}
=
\frac{k_{off}}{k_{on}},
\qquad
\underbrace{K_m}_{\text{결합+소실}}
=
\frac{k_{off}+k_{e(RL)}}{k_{on}}
$$

**다음 깊이 질문**: in vitro SPR/BLI로 측정한 thermodynamic $K_d$와 in vivo PK fitting으로 추출한 apparent $K_m$을 같은 후보 mAb에 대해 internal report나 NDA narrative에서 어떻게 명시적으로 분리해야 reviewer가 reconciliation 요청을 안 함?

### Q6 ★ — sc mAb terminal slope

sc mAb의 terminal slope를 곧바로 elimination 반감기로 해석하면 왜 위험한가?

**답**: 큰 단백질은 sc/im 후 림프관 흡수가 느려 **absorption-rate-limited** 프로파일을 보일 수 있음. somatropin처럼 iv 반감기는 짧아도 sc 프로파일은 길게 지속될 수 있음 [R&T pp.718–721].

**다음 깊이 질문**: sc mAb의 terminal phase가 absorption-rate-limited인지 elimination-rate-limited인지 어떻게 구분함? 어떤 추가 실험 설계나 데이터 비교가 결정적 신호를 줌?

### Q7 ★★ — PK27의 $V_c$

PK27에서 $V_c=0.05$ L·kg⁻¹는 어떻게 처리됐는가?

**답**: $V_c$는 fixed assumption으로 사용됐고, Table 27.2는 그 외 **8개의 추정·보고 파라미터**를 제시함. fixed $V_c$까지 structural quantity로 세면 9개를 언급할 수 있는데, "8 estimated parameters"와는 구분해야 함 [G&W pp.603, 608–609].

$$
\underbrace{V_c}_{\text{central volume}}
=
\underbrace{0.05\ \mathrm{L\cdot kg^{-1}}}_{\text{fixed}},
\qquad
\overbrace{8}^{\text{추정/보고}}
\ne
\overbrace{9}^{\text{fixed }V_c\text{ 포함}}
$$

**다음 깊이 질문**: PK27의 $V_c=0.05$ L·kg⁻¹는 healthy adult 가정에 가까움. edema, severe burn, ascites, pediatric subgroup처럼 plasma volume이 의미 있게 다른 sub-population에 같은 fixed $V_c$를 적용하면, sensitivity analysis는 어떻게 설계해야 다른 파라미터(특히 $k_{on}$)의 robustness를 검증할 수 있음?

### Q8 ★ — 자료 풍부도와 식별성

target과 complex 데이터가 추가되면 왜 $k_{on}$, $k_{off}$, $k_{e(RL)}$의 정밀도가 좋아짐?

**답**: ligand-only 데이터는 여러 ODE 항의 합성 결과만 보여줌. target 데이터는 saturation·recovery를, complex 데이터는 sink 거동을 직접 가르치니까 해당 파라미터의 CV%가 개선됨. PK27 Table 27.2에서 $k_{on}$은 **17→2→1**, $k_{off}$는 **27→13→3**, $k_{e(RL)}$는 **27→23→2**로 좋아짐 [G&W p.609].

**다음 깊이 질문**: target/complex assay가 임상에서 가용하지 않을 때 — 예를 들어 PK26 Efalizumab처럼 — 동등한 식별성을 확보할 차선 전략이 있음? 어떤 조건이 충족되면 reduced model이 정당화됨?

### Q9 ○ — Fig.21-16 해석

R&T Fig.21-16에서 얻을 수 있는 올바른 결론과 얻으면 안 되는 결론은?

**답**: **얻어도 되는 결론**은 분자량이 커질수록 림프 회수율이 증가한다는 **방향성**임. **얻으면 안 되는 결론**은 0.246–19 kDa sheep 데이터를 150 kDa mAb에 선형 외삽해서 구체적 회수율 퍼센트를 계산하는 거임 [R&T p.720].

**다음 깊이 질문**: 150 kDa mAb의 sc 림프 회수율을 정량 예측할 수 없다면, 임상 protocol 설계에서 sc 흡수 프로파일의 불확실성을 어떻게 다루는 것이 안전함?

### Q10 ★★ — 보스 딜레마

팀이 "MM 모델로 OFV도 낮고 VPC도 괜찮으니 first-in-human 저용량 외삽에 쓰자"고 주장함. 30초 답변은?

**답**: "MM은 관찰된 용량 범위 안에서는 쓸 수 있음. 그런데 저용량 외삽은 **target occupancy가 충분히 높게 유지되는지 확인**해야 함. PK27에서는 고용량 적합이 양호해도 가장 낮은 용량 곡선이 따로 놀았고 $K_m$이 0.03에서 3.7로 **123배 부풀려졌음**. 최소한 dose-stratified 잔차, 예측 occupancy, 저농도 sensitivity analysis를 보고 결정해야 함." [G&W p.609]

$$
\underbrace{K_{m,\mathrm{MM}}}_{\text{reduced model}}
=
\underbrace{3.7}_{\text{PK27 MM}},
\qquad
\underbrace{K_{m,\mathrm{TMDD}}}_{\text{full model}}
=
\underbrace{0.03}_{\text{PK27 TMDD}},
\qquad
\frac{K_{m,\mathrm{MM}}}{K_{m,\mathrm{TMDD}}}\approx123
$$

**다음 깊이 질문**: 위 sensitivity analysis 결과 예측 occupancy가 dosing interval의 일부 구간에서 80% 미만으로 떨어지는 sub-group이 발견됐다고 가정해 보면, 이 sub-group을 위해 reduced MM을 그대로 유지할 건가, Full TMDD로 전환할 건가, 아니면 별도 covariate model로 분리할 건가? 어떤 기준으로 결정하고, 내부 PK report나 NDA narrative에서 그 결정을 어떻게 정당화할 건가?

---

## §8 메타 프레임 — Professional Moat

### 이 세션이 놓인 위치

이 세션은 **biologics pharmacometrics의 입구**임. Small molecule PK에서는 청소율과 $V_d$ 중심으로 설명할 수 있었지만, mAb에서는 **target biology, binding kinetics, complex sink, FcRn salvage, lymphatic input**이 함께 PK 곡선의 형태를 만듦.

- 선행 흐름: linear PK → Michaelis-Menten → turnover → TMDD
- 후속 흐름: mAb PopPK → target occupancy 시뮬레이션 → QSP/PBPK → biologics 임상약리 narrative

### 한 카드를 건너뛰면 어떤 실패가 옴

| 건너뛰면 | 구체 실패 |
|---|---|
| **M1 (Turnover)** | target baseline을 predose DV로만 처리하고 $R_0/k_{out}$ 해석을 잃음 |
| **M2 (단백질 ADME)** | sc mAb terminal slope를 elimination으로 오해함 |
| **M3 (4-Phase)** | 고용량 적합만 보고 저용량 외삽 편향을 놓침 |
| **M4 (Full TMDD)** | target과 complex 데이터의 가치를 "nice-to-have"로 잘못 판단함 |
| **M4½ (QSS)** | 임상 mAb PopPK 실무의 출발점을 모르고 Full ↔ MM 두 극단 사이에서 길을 잃음 |
| **M5 (MM 경계)** | 관찰 범위 내 내삽을 임상 외삽으로 착각함 |

### 실무 해석 지점 — Professional Moat

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| target turnover 변화 | $k_{in}$/$k_{out}$ | → | baseline·recovery·occupancy 해석 변화 | baseline scenario와 target 데이터 확인 |
| FcRn/slow input 개입 | $F$, $T_{max}$, apparent $t_{1/2}$ | → | terminal slope 오독 | iv 비교 또는 dose-stratified 프로파일 확인 |
| 저용량 TMDD 경계 진입 | $K_m$, $K_d$, occupancy | → | trough·subgroup 외삽 편향 | sensitivity analysis와 Full TMDD 필요성 검토 |
| complex sink 관찰 부족 | $k_{e(RL)}$ | → | mechanism fitted but not learned | target/complex assay 또는 informative prior 검토 |
| **ADA-매개 면역복합체** | **apparent Phase B CL, IOV, $k_{ADA}(t)$** | → | **시점 의존 청소율 증가, BSV 폭발, sub-therapeutic trough** | **ADA assay + dose-occasion IOV 점검, time-varying covariate 검토** [R&T p.712] |

### 이 세션을 체화하면 두 가지 능력이 생김

**첫째, mechanistic 모델 narrative 정당화** — "왜 Full TMDD인가 / 왜 QSS이어도 되는가 / 왜 MM이어도 되는가 / 왜 target assay가 필요한가"를 **수식·생리학·관찰된 농도 범위**로 설명할 수 있음.

**둘째, 진단 GOF 읽기** — 전체 VPC가 아니라 **dose-stratified 잔차, 저용량 프로파일, target/complex coverage**를 먼저 보고 구조 misspecification을 의심할 수 있음.

### 실무 한 줄 정리

mAb TMDD 데이터셋을 처음 받으면 전체 적합 plot보다 먼저 **dose-stratified plot**을 만들어야 함. 고용량은 맞는데 저용량만 체계적으로 틀리면, "variability problem"보다 **"reduced model 경계 문제"**를 먼저 의심해야 함.

### 최종 통합

| 후속 세션 | 이 세션에서 열리는 개념 | 이 세션 없으면 실패하는 것 |
|---|---|---|
| mAb PopPK | 제한 분포, FcRn, target-mediated CL, QSS as 실무 출발점 | terminal slope와 covariate effect 해석 |
| TMDD/QSP | ligand-target-complex ODE topology, 근사 위계 (Full ↔ QSS ↔ MM) | target biology와 PK coupling 설명 |
| Target occupancy 시뮬레이션 | $K_d, K_{ss}, K_m$, occupancy 경계 | dosing interval 동안의 pharmacologic coverage 판단 |
| Biologics 임상약리 리포트 | 모델 경계와 외삽 방어, soluble vs membrane-bound 분기, ADA-매개 time-varying CL | MM/QSS/Full TMDD 선택 근거 방어 |

---

## 마지막 한 줄

mAb 비선형 PK의 본질은 "항체가 크다"가 아님. **큰 ligand가 제한된 tissue space와 림프관 입력을 거쳐 endogenous target turnover system에 들어가고, binding·complex·sink가 농도의존적 청소율을 만든다**는 것임. Full TMDD는 이 과정을 분해하고, QSS는 임상 자료 한계 안에서 식별성을 회복시키고, MM은 일부 조건에서만 이를 한 항으로 압축함.

그래서 모델 선택의 기준은 편의성이 아니라 **데이터셋이 관찰한 phase, 그리고 임상 의사결정이 요구하는 외삽 범위**임. 세션 첫머리의 PK27 그림 — 고용량 곡선은 잘 맞는데 가장 낮은 용량 곡선만 따로 놀았던 그 그림, $K_m$이 0.03 vs 3.7로 123배 어긋난 그 사건 — 이 사실 이 세션 전체의 한 컷짜리 요약임.

질문은 처음과 같음 — **"이 데이터가 실제로 어떤 파라미터를 가르치고 있는가?"** 이 질문을 매번 자기 자신에게 던지는 것이 이 세션을 통과한 사람과 통과하지 못한 사람의 차이임.

---

C-260517-114853-9XR

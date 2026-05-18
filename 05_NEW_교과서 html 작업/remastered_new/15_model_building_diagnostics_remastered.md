# 세션 15 (Remastered) — 모델 진단을 한 가닥으로 꿰기: 좋은 fit이 어떻게 임상에서 무너지는가

> **출처 노트**
> 본 챕터의 1차 출처는 **Gabrielsson J & Weiner D. *Pharmacokinetic and Pharmacodynamic Data Analysis*, 5th ed. Apotekarsocieteten, Stockholm, 2016 (G&W 5e)** Ch.4 §4.4, §4.7–4.10 / Ch.5 §5.2.3–5.2.4, §5.3.3. 검증 페이지: **p.352–364 / p.368–392 / p.399–405 / p.412–414**. 누락 페이지(pp.365–367, pp.406–411) 기반 내용은 `[확인 필요]`로 둠.
> 보조 출처(임상 맥락)는 **Rowland M & Tozer TN. *Clinical Pharmacokinetics and Pharmacodynamics*, 5th ed. Wolters Kluwer, 2020 (R&T 5e)**. G&W 5e·R&T 5e 외 인용(Holford 2005; Bergstrand et al. 2011; Brendel et al. 2006; Dosne et al. 2016; Wählby et al. 2002; Lindbom et al. 2005; Wilks 1938 등)은 본문 해당 위치에 명시.

---

## 0. 이 강의 1분 압축 — 왜 다시 짰는가

원본 핸드아웃은 M1~M6 여섯 개 카드를 평행하게 나열하는 구조였음. 그러면 학습자가 카드 하나하나는 이해해도 **"왜 이 6개가 같은 사건의 6단계인가"**를 잡기 어려웠음. 그래서 이번 리마스터는 **하나의 수사극**으로 꿰겠음.

> **사건 — 좋은 fit으로 임상시험을 망친 가상 사례**
> 너가 어느 신약의 PopPK 모델을 NONMEM으로 fit함. AIC가 떨어졌고, 곡선이 예쁘게 깔렸고, COV step도 통과했음. 그 모델로 dose simulation을 돌려서 Phase 2 용량을 정함. 그런데 임상에서 예상치 못한 농도 분포가 나옴. FDA reviewer가 묻음 — "이 covariate, 어떤 test로 채택했습니까?", "이 IIV가 boundary에 닿아 있는데 SE 신뢰합니까?", "Day 1과 정상상태 AUC 비교 어떻게 했습니까?"
> 너는 답을 못 함. 왜? **각 진단 단계가 독립된 체크박스라고 생각했기 때문**임. 실제로는 한 단계의 실패가 다음 모든 단계의 결론을 오염시키는 사슬임.

그래서 이 세션이 다루는 6명의 형사는 다음과 같이 캐스팅됨:

| 형사 | 담당 검문 | 이걸 놓치면 임상에서 정확히 무엇이 무너지는가 |
|---|---|---|
| **M1** | 출발 좌표 (초기값) | local minimum에 갇혀서 모델이 잘못된 골짜기로 수렴 — 이후 모든 진단이 잘못된 모델 위에서 돌아감 |
| **M2** | 잔차 패턴 | 구조 misspecification을 IIV로 흡수해서 가짜 covariate signal 생성 |
| **M3** | 비교 자격 | F-test/AIC가 부적격 모델을 채택 → 잘못된 모델로 dose simulation |
| **M4** | parameter 정밀도 | ridge 위의 unidentifiable parameter로 covariate effect를 잘못 귀속 |
| **M5** | 다음 sampling 위치 | 정보가 없는 시간점에서 반복 측정 → precision 개선 실패 |
| **M6** | 임상 결론 stress test | parameter 불확실성이 안전역·용량 결론을 흔든다는 사실을 모른 채 제출 |

그리고 이 6단계를 모두 통과해도 **마지막 검문 두 개**가 남음 — **VPC/pcVPC/NPDE**(모델이 데이터를 *생성*할 수 있는가), **Bootstrap/SIR**(asymptotic SE가 거짓말일 때 진짜 불확실성). 이건 별도 카드가 아니라 M3·M4에 자연스럽게 환승됨.

> 🎯 **한 줄 압축** — 초기값은 출발 골짜기를 정하고, 잔차는 모델의 거짓말을 드러내며, F-test/AIC는 같은 운동장에서만 의미가 있고, 정밀도/상관은 sampling design의 품질을 말하며, 편미분/민감도는 다음 실험을 재설계하고, VPC와 Bootstrap/SIR이 마지막 검문을 통과시킴.

---

## 1. 형사 M1 — 출발 좌표를 박지 않으면 알고리즘은 길을 잃음

### 1.1. 왜 이게 첫 번째 검문인가

비선형 회귀는 출발 vector가 주어진 뒤에야 **목적함수 표면**(parameter 조합이 만드는 잔차 제곱합 지형)을 탐색함. 즉 fit이 시작되는 순간 알고리즘은 이미 어느 골짜기 입구에 서 있는 것임. 그 입구가 틀리면 **세 가지 사고**가 정해진 운명처럼 따라옴 [G&W 5e p.353]:

1. **잘못된 final estimate**로 수렴
2. **local minimum**에 갇혀서 더 좋은 해를 못 봄
3. **생리학적으로 불가능한 parameter** ($V$가 음수, $K_a < K$ 같은 것)로 수렴

핵심은 — 이 세 사고는 **fit이 끝난 뒤에 잔차 도표로 판별할 수 없음**. 잔차는 "현재 골짜기 안에서 모델이 데이터를 얼마나 설명하는가"만 보여줌. 다른 골짜기가 더 좋았는지는 안 알려줌. 그래서 출발 좌표는 fit 이전에 **그래프·NCA·선행 화합물 지식**으로 박아둬야 함.

### 1.2. 가장 단순한 anchor — IV bolus 1구획

10 mg IV bolus 후 반로그 plot에서 자로 기울기를 읽음 [G&W 5e pp.353–354]:

$$
\overbrace{\text{slope}}^{\text{반로그 기울기}}=\frac{\overbrace{\ln(800)-\ln(400)}^{\text{log 농도차}}}{\underbrace{23-87}_{\text{시간차}}}=\underbrace{-0.01\ \text{min}^{-1}}_{\text{음의 slope}}=-\underbrace{K}_{\text{제거속도}} \quad [\text{G\&W 5e Eq.4:16},\ p.354]
$$

이 한 숫자에서 나머지 anchor가 도미노처럼 따라 나옴:

$$
\overbrace{t_{1/2}}^{\text{반감기}}=\frac{\overbrace{\ln2}^{\text{절반 감소}}}{\underbrace{K}_{\text{제거속도}}}=\frac{0.693}{0.01}\approx\underbrace{65\ \text{min}}_{\text{반감기 anchor}} \quad [\text{G\&W 5e Eq.4:17}]
$$

$$
\overbrace{AUC}^{\text{전신노출}}=\frac{\overbrace{C^0}^{\text{초기농도}}}{\underbrace{K}_{\text{제거속도}}}=\underbrace{100{,}000\ \mu g\cdot L^{-1}\cdot\text{min}}_{\text{노출 anchor}} \quad [\text{G\&W 5e Eq.4:18}]
$$

$$
\overbrace{Cl}^{\text{정화 부피/시간}}=\underbrace{0.1\ L\cdot\text{min}^{-1}}_{\text{Dose/AUC}},\qquad \overbrace{V}^{\text{겉보기 공간}}=\underbrace{10\ L}_{\text{Dose/}C^0} \quad [\text{G\&W 5e Eq.4:19–4:20}]
$$

> 💡 **직관 — 등산로 입구 비유**: 같은 산이라도 입구를 잘못 잡으면 지도가 아무리 맞아도 전혀 다른 능선으로 올라감. 초기값은 등산 첫 입구임. 회귀는 그 입구에서 가장 가까운 정상으로 향함 — 더 높은 정상이 옆 능선에 있어도 안 감.

### 1.3. 두 phase가 섞여 있을 때 — curve stripping

이중지수 곡선은 두 phase를 그래프에서 직접 떼어냄 [G&W 5e p.354]:

$$
\overbrace{C}^{\text{총농도}}=\overbrace{\underbrace{A}_{\text{초기 절편}}e^{-\underbrace{\alpha}_{\text{빠른 slope}}t}}^{\text{분포상}}+\overbrace{\underbrace{B}_{\text{말단 절편}}e^{-\underbrace{\beta}_{\text{느린 slope}}t}}^{\text{말단상}} \quad [\text{G\&W 5e Eq.4:21},\ p.354]
$$

**왜 말단상부터 읽나?** $\alpha \gg \beta$일 때 말단에서는 $Ae^{-\alpha t}$가 사실상 사라지고 $Be^{-\beta t}$만 남음. 즉 말단 시간대는 자연이 만들어준 "한 phase 분리 구간"임. 거기서 $B$와 $\beta$를 자로 읽고, 그 line을 초기 시간대로 후방 외삽해서 원곡선에서 빼면 $Ae^{-\alpha t}$만 남음. Fig.4.18 예시 anchor: $A=1.0\ \mu g\cdot L^{-1}$, $B=0.8\ \mu g\cdot L^{-1}$, $\alpha=0.05\ \text{min}^{-1}$, $\beta=0.003\ \text{min}^{-1}$ [G&W 5e p.355].

> ⚠️ **stripping이 깨지는 자리** — 두 slope가 충분히 안 떨어지면(예: $\alpha/\beta < 5$) 말단상에 빠른 phase의 잔여가 섞여 있어서 $\beta$를 과소 추정함. 이건 그래프로는 잘 안 보이고, 나중에 다구획 모델에서 V_p/Q가 이상하게 추정되는 형태로 드러남.

### 1.4. Turnover 모델 — warfarin 사례

**Warfarin**(경구 항응고제, vitamin K epoxide reductase 억제로 작용)을 주면 prothrombin complex 합성이 차단됨. PCA 반응이 하강하기 시작하는데, **그 하강 기울기가 그대로 $-k_{out}$ anchor**가 됨 [G&W 5e pp.356–357]:

$$
\overbrace{\text{slope}}^{\text{하강 slope}}=\frac{\overbrace{\ln(124)-\ln(56.77)}^{\text{log 반응차}}}{\underbrace{24-0}_{\text{시간차}}}\approx\underbrace{-0.03\ h^{-1}}_{\text{원문 }-k_{out}} \quad [\text{G\&W 5e Eq.4:22},\ p.356]
$$

*원문에 부호 표기 불일치가 있음. 하강 기울기를 $-k_{out}$ anchor로 읽되, 수학적으로는 $[\ln(56.77)-\ln(124)]/(24-0)$ 또는 $[\ln(124)-\ln(56.77)]/(0-24)$가 맞음.*

Baseline 120 sec와 $k_{out}\approx0.03\ h^{-1}$에서 $k_{in}=3.6\ \text{sec}\cdot h^{-1}$가 따라 나옴 [G&W 5e p.357]. 이 사례가 보여주는 핵심 — **turnover 모델 같은 비정상상태 PD에서도 그래프에서 직접 anchor를 읽는 것이 가능함**. fit 시작 전에 이미 $k_{in}$, $k_{out}$의 자릿수가 정해져 있어야 안전함.

### 1.5. 간접반응 모델의 다단계 anchor 추출

G&W 5e Eq.4:23–4:33은 간접반응 모델(baseline, steady state, $E_{max}$, $k_{out}$, $k_{in}$, exponent $n$)을 그래프에서 **순차적**으로 읽어내는 사례임. 그리고 Table 4.3에서 Model 1 vs Model 4의 final/initial estimate를 비교하는데, **WRSS/AIC가 Model 1에서 7.3/83, Model 4에서 12/102** [G&W 5e pp.358–360]. 이게 가르치는 메시지 — **초기값 추출 작업이 곧 모델 선택의 전 단계**임. anchor를 못 박는 모델은 fit 자체가 안 됨.

반복투여 항불안제 예시도 같은 논리임 [G&W 5e pp.361–363]. PK input ($K_a=1.1\ h^{-1}$, $K=0.128\ h^{-1}$, $V/F=5.0\ L\cdot kg^{-1}$)을 fix한 뒤 PD turnover 식에 anchor 값을 박음:

$$
\overbrace{\frac{dR}{dt}}^{\text{반응 변화}}=\overbrace{\underbrace{k_{in}}_{\text{생성}}\underbrace{I(C)}_{\text{농도 억제}}}^{\text{입력}}-\overbrace{\underbrace{k_{out}}_{\text{소실}}\underbrace{R}_{\text{현재 반응}}}^{\text{출력}}
$$

$k_{out}\approx0.06\ h^{-1}$, $k_{in}=4.8$ units, $IC_{50}\approx0.25\ \mu g\cdot L^{-1}$가 시작 vector가 됨.

### 1.6. 다른 방법이 다 막힐 때 — 경계값 스케일링과 그 함정

anchor를 못 읽으면 LB/UB(하한/상한)로 0–1 범위 scale을 만듦 [G&W 5e p.364]:

$$
\overbrace{\frac{\overbrace{IE-LB}^{\text{하한 초과분}}}{\underbrace{UB-LB}_{\text{경계 폭}}}}^{\text{0--1 위치}} \quad [\text{G\&W 5e Eq.4:44},\ p.364]
$$

흔히 $0.1\cdot IE$부터 $10\cdot IE$ relative range를 권함. **하지만 Table 4.4의 $\beta=0.05$가 UB=0.05에 딱 붙어 있는 케이스**가 보여주는 함정 — final estimate가 경계에 닿아 있으면 모델이 정보를 준 게 아니라 **경계가 추정값을 만들어낸 것**임. 이건 boundary parameter 문제로 직결되고, M4의 asymptotic SE가 무너지는 자리(→ bootstrap/SIR 필요)와 연결됨 [G&W 5e p.364].

### 1.7. M1 한 줄 정리

> **출발 vector는 fit 이전의 EDA 산출물임. anchor 없이 NONMEM을 돌리면 NONMEM도 어디서 시작할지 모름. 그리고 잘못된 골짜기에서 수렴한 모델은 잔차도 좋아 보일 수 있음 — 그래서 M2가 잡지 못함.**

---

## 2. 형사 M2 — 잔차는 곡선이 못 말하는 것을 말함

### 2.1. 왜 이게 두 번째 검문인가

곡선 overlay만 보면 모델이 데이터 위에 예쁘게 깔린 것처럼 보일 수 있음. 하지만 잔차는 **부호와 순서**를 보존함. 그 부호와 순서에 구조적 흔적이 남아 있으면, overlay가 아무리 예뻐도 모델이 어딘가에서 거짓말을 하고 있음.

### 2.2. 잔차의 형식적 정의

$$
\overbrace{\epsilon}^{\text{잔차오차}}=\underbrace{N(0,\sigma^2)}_{\text{평균 0·분산 }\sigma^2} \quad [\text{G\&W 5e Eq.4:46},\ p.369]
$$

$$
\overbrace{residual_i}^{\text{i번째 잔차}}=\underbrace{C_{obs,i}}_{\text{관측농도}}-\underbrace{\hat C_{calc,i}}_{\text{예측농도}} \quad [\text{G\&W 5e Fig.4.41},\ p.369]
$$

가중잔차제곱합과 잔차 SD:

$$
\overbrace{WRSS}^{\text{가중잔차합}}=\sum \underbrace{W_i}_{\text{가중치}}\underbrace{(C_i-\hat C_i)^2}_{\text{잔차제곱}} \quad [\text{G\&W 5e Eq.4:47},\ p.371]
$$

$$
\overbrace{\sigma}^{\text{잔차 SD}}=\sqrt{\frac{\overbrace{WRSS}^{\text{남은 불일치}}}{\underbrace{N_{obs}-N_{par}}_{\text{잔차 자유도}}}} \quad [\text{G\&W 5e Eq.4:48},\ p.371]
$$

### 2.3. 잔차가 말해주는 두 종류의 거짓말

잔차는 무작위 산포여야 함. 같은 부호가 연속(run)으로 나오거나 군집(cluster)이 보이면 둘 중 하나임 — **구조 오류** 또는 **분산/가중치 오류**. 이 둘은 처방이 완전히 다르므로 구분이 핵심임.

**거짓말 #1 — Banana / U-shape (잔차 vs 시간)** → 구조 오류
- 빠진 exponential term, 잘못된 compartment 수, lag-time omission, 잘못된 시간 스케일
- 처방: **모델 구조 자체를 바꿔야 함** [G&W 5e pp.372–376]

**거짓말 #2 — Fan shape (잔차 진폭이 농도와 함께 변함)** → 분산/가중치 오류
- 농도의존 분산, 등분산 가정 위반, 잘못된 weighting 선택
- 처방: **weighting scheme을 바꿔야 함** (구조는 그대로) [G&W 5e pp.373–374]

> ⚠️ **가장 흔한 실수** — fan shape에 compartment를 추가하는 것. 구조는 멀쩡한데 분산 모델만 틀린 상황에서 compartment를 추가하면 새 parameter가 약간의 잔차를 더 흡수해서 WRSS가 떨어짐 → "improvement"처럼 보임 → 하지만 분산 문제는 그대로 남고 모델만 더 복잡해짐. 그리고 추가된 compartment의 parameter는 boundary에 닿거나 정밀도가 무너짐(M4의 함정).

가중치 표기는 원문에서 $C_i^{-\lambda_z}$ 또는 $\hat C_i^{-\lambda_z}$ 형태로 일반화됨. 부호를 "$\lambda_z=-1$"처럼 단정해 쓰지 말고 **가중치 지수(weighting power)**로 표기:

$$
\overbrace{C_i^{-\lambda_z}\ \text{ 또는 }\ \hat C_i^{-\lambda_z}}^{\text{농도 기반 가중치}}
$$

### 2.4. 두 축을 모두 봐야 하는 이유

- **잔차 vs 시간**: 시간 스케일/구조 문제를 잡음
- **잔차 vs 예측값 또는 농도**: 분산/가중치 문제를 잡음

한 축에서 무작위로 보여도 다른 축에서 fan이나 run이 보일 수 있음. NONMEM workflow에서 xpose의 표준 GOF 4분할 plot(DV vs PRED, DV vs IPRED, CWRES vs TIME, CWRES vs PRED)이 정확히 이 두 축을 강제로 다 보게 만드는 장치임.

### 2.5. Ordinary Emax vs Sigmoid Emax — 잔차가 모델 선택을 결정함

예측 곡선만 보면 두 모델 차이가 애매한 데이터가 많음. 그런데 잔차 도표로 가면 한쪽에서 **계통적 이탈**이 명확하게 드러남 [G&W 5e pp.372–373]. 이게 잔차 진단의 결정적 가치 — overlay가 모호하게 만드는 모델 선택을 잔차가 단정해줌.

### 2.6. 순수오차(pure error) vs 적합결여(lack-of-fit) — 반복 측정이 있을 때

같은 시간점에 반복 측정이 있는 in vitro dataset에서는 잔차오차를 **순수오차(반복 측정의 본래 분산)**와 **적합결여(모델이 못 잡는 부분)**로 분해할 수 있음 [G&W 5e pp.377–379]:

$$
\overbrace{F_{LOF}}^{\text{LOF F값}}=\frac{\overbrace{(92.67-23.61)/(25-21)}^{\text{LOF 평균제곱}}}{\underbrace{23.61/21}_{\text{pure MS}}}=\underbrace{15.35}_{\text{F 비교값}} \quad [\text{G\&W 5e Eq.4:51},\ p.379]
$$

$F_{crit}=2.76$ 대비 $F_{LOF}=15.35$이므로 lack-of-fit 있음.

> ⚠️ **임상 PK에는 적용 불가한 검정** — 환자별 sparse sampling에서는 같은 시간점에 반복 측정이 없어서 pure error를 분리할 수 없음. 이때 LOF F-test를 억지로 만들지 말고, **잔차 패턴 + 기전 타당성 + VPC**의 삼각 검증으로 가야 함(→ 섹션 7).

### 2.7. M2 한 줄 정리

> **잔차 vs 시간에서 banana는 구조를 의심하고, 잔차 vs 예측값에서 fan은 분산을 의심함. 두 처방은 절대 섞으면 안 됨. 그리고 잔차가 noise처럼 흩어졌다는 사실은 모델이 데이터를 *설명*한다는 증거지, *생성*한다는 증거는 아님(→ VPC 검문은 섹션 7에서 따로 작동함).**

---

## 3. 형사 M3 — 두 모델이 같은 운동장에 있을 때만 심판을 부를 수 있음

### 3.1. 가장 흔한 미신 — "WRSS 더 낮고 parameter 더 많으면 F-test"

이 한 줄이 모델 선택 사고의 절반을 일으킴. F-test는 두 모델이 **같은 운동장**에 서 있을 때만 작동하는 심판임. 그 운동장 조건이 두 개임 — **중첩(nested) 관계**와 **동일 가중치(equal weighting)**.

### 3.2. F 통계량과 그 전제

$$
\overbrace{F^*}^{\text{중첩 F값}}=\frac{\overbrace{(WRSS_{reduced}-WRSS_{full})/(df_{reduced}-df_{full})}^{\text{개선량 (1 자유도당 SS 감소)}}}{\underbrace{WRSS_{full}/df_{full}}_{\text{full MS = 잔차 분산}}} \quad [\text{G\&W 5e Eq.4:54},\ p.387]
$$

$$
\overbrace{df}^{\text{잔차 자유도}}=\underbrace{N_{obs}}_{\text{관측수}}-\underbrace{N_{par}}_{\text{parameter 수}} \quad [\text{G\&W 5e Eq.4:55},\ p.387]
$$

### 3.3. 중첩 조건 — 기하학적 의미

중첩이란 단순히 "parameter 개수가 다름"이 아님. **reduced model이 full model parameter space의 제한된 부분공간**이어야 함. 즉 한 모델이 다른 모델의 **특수 사례(special case)**가 되어야 함.

| 비교 | nested? | 이유 |
|---|---|---|
| Ordinary Emax vs Sigmoid Emax | **Yes** | sigmoid에서 $n=1$ fix하면 ordinary가 됨 [G&W 5e p.388] |
| Linear response vs Ordinary Emax | **No** | $C\ll EC_{50}$ 극한에서만 근사적으로 비슷, 일반 nested 아님 [G&W 5e p.388] |
| Hepatic distributed vs Parallel-tube | **조건부** | 축소 관계가 성립하는 특정 조건에서만 [G&W 5e pp.388–389] |
| MM weighted vs first-order unweighted | **No, 게다가 weighting까지 다름** | F-test도 AIC도 둘 다 불가 [G&W 5e p.389] |

$$
\text{Nested 예시: }\overbrace{n}^{\text{sigmoidicity}}=\underbrace{1}_{\text{Emax 제한}}
$$

$$
\text{비교 불가 극한: }\overbrace{C}^{\text{농도}}\ll\underbrace{EC_{50}}_{\text{반최대 농도}}
$$

### 3.4. 동일 가중치 조건 — 좌표가 같아야 비교가 됨

WRSS는 weighting에 따라 다른 좌표계에서 측정되는 숫자임. 두 모델이 서로 다른 weighting을 쓰면, 그 WRSS 차이는 "모델 우열"이 아니라 "좌표계 차이"를 측정한 것에 불과함. 이 함정이 Table 4.8 (MM weighted vs first-order unweighted)이 보여주는 핵심임 [G&W 5e p.389].

### 3.5. AIC/SC — nested는 안 요구하지만 equal weighting은 요구함

$$
\overbrace{AIC}^{\text{Akaike 기준 (reduced form)}}=\underbrace{N_{obs}\ln(WRSS)}_{\text{불일치}}+\underbrace{2N_{par}}_{\text{복잡도 벌점}} \quad [\text{G\&W 5e Eq.4:56},\ p.389]
$$

$$
\overbrace{SC}^{\text{Schwarz 기준 (reduced form)}}=\underbrace{N_{obs}\ln(WRSS)}_{\text{불일치}}+\underbrace{N_{par}\ln(N_{obs})}_{\text{표본수 벌점}} \quad [\text{G\&W 5e Eq.4:57},\ p.389]
$$

### 3.6. 함정 — WRSS-form AIC와 likelihood-form OFV는 같은 숫자가 아님

이게 학습자가 가장 자주 부딪히는 cross-platform 함정임. WinNonlin/Phoenix는 WRSS 기반 AIC를 보고하고, NONMEM은 $-2\log L$ 기반 OFV를 보고함. **둘은 결국 같은 해로 수렴하지만 절대 scale은 다름** [G&W 5e p.386]:

$$
\overbrace{AIC_{full}}^{\text{절대 likelihood scale}}
=\overbrace{N_{obs}\ln(WRSS)}^{\text{비교에 남는 항}}+\overbrace{2N_{par}}^{\text{복잡도 벌점}}
\underbrace{+\,N_{obs}\!\left[\ln(2\pi)+1\right]-N_{obs}\ln(N_{obs})}_{\text{같은 데이터 내 두 모델에 공통 — 비교 시 상쇄}}
$$

| 환경 | 비교 좌표 | 절대 scale |
|---|---|---|
| WinNonlin/Phoenix (WRSS 기반) | $N_{obs}\ln(WRSS)+2N_{par}$ | reduced form |
| NONMEM OFV ($-2\log L$) | $\Delta\text{OFV}=\chi^2_{df}$로 nested 비교 | full likelihood scale (상수항 포함) |

같은 모델을 WinNonlin에서 AIC=83, NONMEM에서 OFV=120으로 보고했다면 **두 숫자는 서로 환산되지 않음**. 한 환경 내부에서만 비교가 의미를 가짐.

### 3.7. NONMEM 환승 — ΔOFV의 통계적 정당성

현대 PopPK에서는 같은 비교를 ΔOFV로 함. 중첩 모델 간 ΔOFV는 자유도 차이 $\Delta df$에 대해 **카이제곱 분포**를 따름 [Wilks SS. *Ann Math Stat* 1938;9(1):60-2]:

$$
\overbrace{\Delta\text{OFV} = \text{OFV}_{reduced} - \text{OFV}_{full}}^{\text{음의 log-likelihood 비}}
\;\overset{H_0}{\sim}\;
\overbrace{\chi^2_{\Delta df}}^{\Delta df = N_{par,full} - N_{par,reduced}}
$$

이걸 covariate 채택 결정에 자동화한 것이 **Stepwise Covariate Modeling (SCM)** — PsN의 `scm` 명령으로 구현됨:

| 단계 | $\alpha$ | $\Delta df=1$ ΔOFV 임계 | 의미 |
|---|---|---|---|
| Forward inclusion | 0.05 | $\chi^2_{1, 0.95} \approx 3.84$ | "추가 parameter가 모델을 개선하는가" 1차 검문 |
| Backward elimination | 0.01 | $\chi^2_{1, 0.99} \approx 6.63$ | 다중 비교 보정·robustness 확보 |

[Wählby U et al. *J Pharmacokinet Pharmacodyn* 2002;29(3):231-52; Lindbom L et al. *Comput Methods Programs Biomed* 2005;79(3):241-57]

> ⚠️ **카이제곱 근사가 깨지는 곳** — boundary parameter(예: OMEGA를 0으로 fix하느냐 푸느냐)에 대한 검정은 **mixture distribution**($\chi^2$의 mixture)을 따르고, 단순 3.84 임계를 쓰면 보수적이 됨 [Stram DO & Lee JW. *Biometrics* 1994;50(4):1171-7]. OMEGA/SIGMA 구조 결정에서 가장 자주 놓치는 함정임.

### 3.8. 임상으로의 전파 — 비교 자격 위반의 나비효과

비교 조건을 어긴 모델 선택은 다음과 같이 임상에서 무너짐:

1. 잘못된 모델로 dose simulation → 추천 용량 자체가 오염됨
2. 안전역(safety margin) 계산이 다른 모델 기준에서 나옴 → 임상시험에서 예상치 못한 농도 분포
3. 규제 reviewer가 "비교 조건 위반" 지적 → 재분석 + 모델 선택 근거 재제출 요구

그래서 M3는 통계 카드가 아니라 **임상 결정의 정합성 검문**임.

### 3.9. M3 한 줄 정리

> **F-test는 nested + 동일 weighting일 때만 작동함. AIC/SC는 nested는 안 요구하지만 동일 weighting은 요구함. NONMEM ΔOFV는 카이제곱 근사로 환승되지만 boundary parameter에서는 깨짐. 그리고 WRSS-AIC와 likelihood-OFV는 서로 환산되지 않는 별개의 좌표임.**

---

## 4. 형사 M4 — 좋은 fit ≠ 식별 가능한 parameter

### 4.1. M3까지 통과한 모델에도 남은 함정

M1로 좋은 출발점 박았고, M2로 잔차가 무작위인 걸 확인했고, M3로 비교 자격까지 갖춤. 그런데도 — 한 모델 안에서 **parameter 자체가 식별 불가능**할 수 있음. 이게 M4가 잡는 거임.

### 4.2. 정확도 vs 정밀도 — 다트 과녁 비유

- **Accuracy (정확도)** — 평균적으로 참값에 가까운가? 편향 문제임
- **Precision (정밀도)** — 반복하면 얼마나 좁게 모이는가? 불확실성 문제임

둘이 분리됨. 화살이 과녁 중심 부근에 모여 있어도(정확) 탄착군이 길게 늘어져 있으면(정밀도 낮음) "실력이 같다"고 못 함 [G&W 5e pp.379–380].

$$
\overbrace{CV\%}^{\text{상대 SE}}=\frac{\overbrace{SE(\hat p)}^{\text{추정 SE}}}{\underbrace{\hat p}_{\text{parameter 값}}}\cdot100 \quad [\text{G\&W 5e Eq.4:52},\ p.380]
$$

예: $p=0.01\pm0.005\ h^{-1}$이면 **CV 50%** — 추정 불확실성이 큰 신호. G&W는 단일 임계값을 정하지 않음. 통상 실무에서 fixed effect CV가 30% 넘으면 의심하고 50% 넘으면 식별성 재검토함(이건 관습이지 절대 기준 아님).

### 4.3. 상관계수 $r$은 GOF 보조량일 뿐임

G&W가 명시적으로 경고하는 함정 — $r$은 GOF로 가장 많이 오용되는 숫자임 [G&W 5e p.381]:

$$
\overbrace{r}^{\text{GOF 지표}}=1-\frac{\overbrace{\sum(C_i-\hat C_i)^2}^{\text{잔차제곱합}}}{\underbrace{\sum(C_i-\bar C)^2}_{\text{총변동}}} \quad [\text{G\&W 5e Eq.4:53 source form},\ p.381]
$$

*원문 표기 $r$은 잔차제곱합/총변동 비율 기반 보조 지표임.*

Fig.4.53의 핵심 — OLS fit이 $r=0.96$인데 **마지막 세 관측치를 계통적으로 과소예측**함. IRLS fit은 $r=0.94$로 숫자는 낮은데 전체적으로 더 좋은 fit임 [G&W 5e p.382]. 즉 **높은 $r$이 좋은 fit의 충분조건이 아님**.

**왜 PK 데이터에서 $r$이 거의 항상 0.95+ 나오나?** PK는 동적 범위가 넓음(예: 1000 ng/mL → 1 ng/mL). $\sum(C_i-\bar C)^2$가 거대하니까 분모가 압도적이고, 잔차 제곱합이 어지간히 크지 않은 한 $r$은 1에 가깝게 나옴. 즉 **$r$은 모델 적합도가 아니라 dynamic range를 측정**하는 것에 가까움.

### 4.4. 능선 기하(ridge geometry) — 좋은 fit 뒤에 숨는 결합 불확실성

여기가 M4의 가장 깊은 부분임. parameter correlation matrix는 "두 parameter가 독립적으로 추정되는가, 아니면 서로 trade-off하면서 움직이는가"를 보여줌.

**Ridge minimum 직관** — likelihood surface가 길게 늘어진 골짜기 모양일 때, 두 parameter가 능선을 따라 같이 움직여도 OFV가 거의 변하지 않음. 즉:

- 각 parameter 단변량 SE는 좁아 보일 수 있음
- 그런데 **결합 불확실성**은 거대함 — 능선 위 어디든 비슷한 OFV임
- $\hat\theta_1$과 $\hat\theta_2$가 동시에 어디 있는지는 사실상 결정되지 않음

> 💡 **로프로 묶인 두 등산가 비유** — 둘이 능선 위에 서 있음. 능선을 따라 같이 동쪽으로 100m 움직여도 둘 다 같은 고도임(같은 OFV). 각자의 동서 위치 SE는 측정할 수 있지만, "둘이 어디에 있는가"는 사실상 결정되지 않음. correlation matrix에서 $r \approx 0.99$로 나타남.

Fig.4.55–4.57의 핵심 — **같은 모델이라도 sampling design (A vs B)에 따라 $Cl/V$ 또는 $IC_{50}/I_{max}$ 상관이 크게 달라짐** [G&W 5e pp.383–385]. 그래서 parameter 상관은 **모델의 본질**이 아니라 **sampling design의 결과**임. 이게 자동으로 M5(다음 sampling을 어디서 보강할 것인가)로 환승되는 이유임.

### 4.5. parameter를 fix하는 결정 — 통계에서 생물학으로 부담 이동

Fig.4.55가 보여주는 또 다른 사실 — 한 parameter를 fix하면 다른 parameter의 신뢰구간이 줄어들 수 있음 [G&W 5e pp.383–384]. 하지만 이건 공짜가 아님.

**fix은 정밀도를 만드는 것이 아니라 불확실성을 다른 곳에 떠넘기는 행위**임. 정당화 부담이 통계(데이터로부터 추정)에서 생물학·문헌·선행 연구로 이동함. 그 고정값의 출처와 적용 가능성을 설명 못 하면, 정밀도가 좋아진 게 아니라 **불확실성을 덮어 숨긴 것**이 됨.

### 4.6. asymptotic SE가 거짓말일 때 — Bootstrap과 SIR 환승

NONMEM의 $COV$ step이 만드는 SE와 95% CI는 likelihood surface가 최솟값 근방에서 **정규분포 형태의 곡률**을 가진다는 가정 위에 서 있음:

$$
\overbrace{\widehat{\text{Var}}(\hat\theta)}^{\text{asymptotic 분산행렬}}
\approx
\overbrace{\left[-\nabla^2 \ell(\hat\theta)\right]^{-1}}^{\text{Fisher information 역행렬}}
\quad [\text{표준 likelihood 근사}]
$$

이 가정이 깨지는 자리가 실무에서 흔함:

| 상황 | 표준 asymptotic SE | Bootstrap/SIR 필요성 |
|---|---|---|
| 풍부한 데이터 + 잘 정의된 모델 + 낮은 상관 | 충분 | 추가 이득 적음 |
| boundary parameter ($I_{max}\to 1$, $\omega\to 0$) | **깨짐** | **필수** |
| 높은 parameter 상관 (ridge geometry) | SE 좁아 보여도 결합 불확실성 큼 | 권장 |
| 작은 표본 (소아·희귀질환 코호트) | 정규 근사 약함 | 권장 |
| $COV$ step 실패 또는 R/S matrix 비정상 | **사용 불가** | **대안으로 필요** |

**Bootstrap — 데이터 재표집으로 불확실성 재구성** [Efron 1979; Ette EI. *J Pharm Sci* 1997;86(2):260-5]:

$$
\overbrace{\text{원본 dataset}}^{N \text{ 개체}}
\xrightarrow{\text{with-replacement 재표집}}
\overbrace{\text{bootstrap dataset}^{(b)}}^{b=1,\ldots,B}
\xrightarrow{\text{각각 fit}}
\overbrace{\{\hat\theta^{(b)}\}_{b=1}^{B}}^{\text{parameter 분포}}
$$

각 bootstrap replicate의 $\hat\theta^{(b)}$ 분포가 **parameter sampling distribution의 비모수 근사**가 됨. 95% percentile CI는 $[\hat\theta^{(2.5\%)},\hat\theta^{(97.5\%)}]$로 직접 읽음. 비용 큼 — 보통 B=500~1000회 fit, NONMEM에서 non-convergence 누적 이슈 있음. PsN의 `bootstrap` 명령으로 구현됨.

**SIR — Sampling Importance Resampling** [Dosne A-G et al. *J Pharmacokinet Pharmacodyn* 2016;43(6):583-96]:

$$
\overbrace{\theta_m \sim q(\theta)}^{\text{1단계 proposal}}
\;\longrightarrow\;
\overbrace{w_m = \frac{L(\theta_m)}{q(\theta_m)}}^{\text{2단계 importance weight}}
\;\longrightarrow\;
\overbrace{\{\theta^*_k\}_{k=1}^K \sim \text{weighted resample}}^{\text{3단계 posterior 근사}}
$$

1. Proposal $\mathcal{N}(\hat\theta, \widehat{\text{Var}}(\hat\theta))$에서 수천 개 parameter vector sampling
2. 각 $\theta_m$에 대해 importance weight $w_m$ 계산 (likelihood ratio)
3. weight에 비례해서 $K \ll M$개 resampling → **true posterior 근사**

장점 — bootstrap만큼 robust한데 비용이 훨씬 적음(fit 1회 + likelihood 평가). 단점 — proposal이 true posterior와 너무 멀면 effective sample size 무너짐 → iterative SIR로 보완.

### 4.7. M4 한 줄 정리

> **CV%, correlation matrix, ridge geometry는 fit의 부산물이 아니라 sampling design의 진단 신호임. asymptotic SE가 좁다고 안심하면 안 됨 — boundary나 ridge에서는 거짓말함. 그때는 bootstrap/SIR로 결합 불확실성의 진짜 모양을 재구성해야 함. 그리고 parameter fix는 불확실성을 통계에서 생물학으로 떠넘기는 결정임.**

---

## 5. 형사 M5 — 다음 sampling을 어디서 해야 정보가 가장 크게 생기는가

### 5.1. M4와의 직접 연결

M4에서 parameter 상관이 높다고 진단된 순간, 자연스러운 다음 질문 — "그 상관을 깨려면 어느 시간점에 sample을 추가해야 하는가?" 이게 M5가 답하는 질문임.

### 5.2. 손전등 메타포 — partial derivative peak

$\partial C/\partial \theta_i$는 "$\theta_i$를 조금 흔들었을 때 그 시점의 농도가 얼마나 변하는가"를 나타냄. 즉 **모델 예측이 해당 parameter에 가장 민감한 시점**에서 derivative가 최대가 됨. 그 시점이 바로 **$\theta_i$에 대한 정보가 가장 크게 발생하는 자리**임.

> 💡 **어두운 방의 손전등 비유** — 각 parameter는 어두운 방의 한 가구. 손전등(편미분)이 그 가구를 가장 밝게 비추는 위치가 있음. 그 자리에 sample을 두면 그 parameter의 윤곽이 선명해짐. 다른 자리에 sample을 두면? 그 parameter는 어두운 채로 남음.

### 5.3. 이중지수 모델의 design point

$$
\overbrace{C}^{\text{총농도}}=\overbrace{\underbrace{A}_{\text{빠른 절편}}e^{-\underbrace{\alpha}_{\text{빠른 slope}}t}}^{\text{초기 정보}}+\overbrace{\underbrace{B}_{\text{느린 절편}}e^{-\underbrace{\beta}_{\text{느린 slope}}t}}^{\text{말단 정보}} \quad [\text{G\&W 5e Eq.5:7},\ p.399]
$$

- $A$, $B$에 대한 정보는 **절편 영역**(초기·말단 시간)에 집중됨
- $\alpha$, $\beta$ 정보는 각각 $t=1/\alpha$, $t=1/\beta$에서 peak [G&W 5e pp.399–400]

$$
\overbrace{t}^{\text{민감도 peak}}=\frac{1}{\underbrace{\alpha}_{\text{빠른 slope}}},\qquad \overbrace{t}^{\text{민감도 peak}}=\frac{1}{\underbrace{\beta}_{\text{느린 slope}}} \quad [\text{G\&W 5e Eq.5:11},\ p.400]
$$

수치 예시 — $\alpha=0.69\ h^{-1}$, $\beta=0.069\ h^{-1}$이면 design peak는 약 **1.4 h와 14 h**. Fig.5.4에서 $\alpha$와 $\beta$ 정보가 각각 약 **20 min과 300 min** 부근에 모이는 게 보임 [G&W 5e p.400].

**임상 번역** — 이 두 시간점은 **fix해야 할 sampling slot**임. 나머지 sample은 그 다음 우선순위로 배분됨. PopPK design 도구(PFIM, PopED 등)가 이 derivative 정보를 자동화해서 D-optimal design을 출력하는 것의 이론적 기반이 정확히 이것임.

### 5.4. Sigmoid Imax / Emax — parameter별로 다른 effect level이 정보를 줌

[G&W 5e pp.400–402]
- **$IC_{50}$ 정보** → half-maximal effect 부근에 집중
- **Sigmoidicity factor $n$ 정보** → 20% 및 80% effect level 부근에 집중

이게 가르치는 메시지 — **"모든 parameter는 같은 시간점에서 잘 보이지 않음"**. 어떤 parameter는 mid-effect에서, 어떤 parameter는 양쪽 끝에서 정보를 줌. Fig.5.6는 $E_0$, $n$, $EC_{50}$, $E_{max}$ 다섯 parameter의 design point를 한 그림에 보여줌.

### 5.5. Turnover model — $k_{out}$ 정보의 시간대

Turnover response model에서 $k_{out}$ 민감도가 **25 h와 약 100 h post-dose**에서 큼. 초기 시간대에서는 $k_{out}$이 $IC_{50}$이나 $n$보다 더 민감함 — 즉 **초기 sampling은 $k_{out}$ 초기 추정을 직접 강화**함 [G&W 5e pp.402–404].

### 5.6. 정규화 민감도 — parameter 단위가 다를 때

원자료 $\partial C/\partial \theta_i$ 크기를 그대로 비교하면 단위 차이로 왜곡됨. 실무에서는 정규화 민감도를 같이 봄:

$$
\overbrace{\frac{\theta_i\,(\partial C/\partial\theta_i)}{C}}^{\text{정규화 민감도 (normalized sensitivity)}}
$$

이 형태는 단위에서 자유롭고 parameter 간 비교가 안정화됨.

### 5.7. 경계 조건 — derivative peak에만 몰빵하면 안 됨

참 parameter 값을 미리 정확히 알 수는 없음. derivative 극값 시점은 추정값 기준이라 추정값이 틀리면 peak 위치도 틀림. 그래서:

- derivative peak에 우선 sample 배치
- **전체 농도 범위에도 추가 sample** 분산 배치
- pooled data를 무비판적으로 설계 결정에 쓰지 말 것 [G&W 5e p.402]

### 5.8. M5 한 줄 정리

> **partial derivative peak는 "정보가 가장 크게 발생하는 시점"임. parameter마다 peak가 다르므로 균등 sampling은 비효율적임. 그러나 추정값 기반 peak이므로 전체 농도 범위에 보조 sample을 둬야 robust해짐. NONMEM ecosystem에서 PFIM/PopED 같은 optimal design 도구가 이 논리를 자동화함.**

---

## 6. 형사 M6 — parameter 불확실성이 임상 결론을 어디까지 흔드는가

### 6.1. M5와의 연결 — 정보를 어디서 얻을지가 아니라, 잘못된 정보가 어디까지 번지는지

M5가 "정보를 어디서 얻을 것인가"라면 M6는 "정보가 부족하면 어디서 무너지는가"를 묻는 마지막 stress test임. parameter SE/CV가 좋아 보여도, 그 불확실성이 **임상 결론**(용량 결정, 안전역, sampling 일정)을 흔들면 다음 실험 설계 자체를 바꿔야 함.

### 6.2. 형식적 방법 — parameter perturbation

특정 parameter를 일정 비율로 흔들고(예: +100%, −50%) 농도-시간 또는 반응-시간 예측이 얼마나 변하는지 봄. 이건 parameter 불확실성을 **예측 불확실성으로 번역**하는 작업임 [G&W 5e pp.404–405].

### 6.3. PK 민감도 예시 — Michaelis-Menten

$V_{max}$, $K_M$, $V_c$, $V_t$를 각각 흔들었을 때 농도-시간 프로파일의 어느 구간이 어떤 parameter에 민감한지 드러남. Fig.5.9는 이 결과를 향후 sampling 위치로 직접 연결함 [G&W 5e p.405].

### 6.4. PD 민감도 예시 — Warfarin-PCA

Warfarin-PCA 모델에서 $IC_{50}$, $k_{in}$, $k_{out}$, $t_{lag}$를 흔들어서 반응-시간 프로파일에 미치는 영향을 비교함. Fig.5.10이 답하는 질문 — **"어떤 parameter를 더 잘 추정하려면 반응-시간 곡선의 어느 구간을 sampling으로 보강해야 하는가?"** [G&W 5e p.405]

### 6.5. 독성동태(TK) 설계 맥락 — profile 중심 vs $C_{max}$ 중심

만성시험은 보통 **노출 확인 목적으로 $C_{max}$ sampling만으로 충분**한 경우가 있음. 다만 예외는 연구자 판단. Table 5.6은 PK/DRF/chronic study type별 sampling package 차이를 정리함 [G&W 5e p.413].

비선형 제거가 있는 약물에서는 농도가 **first-order linear kinetics 영역**으로 떨어지거나 무시 가능한 수준까지 sampling을 이어가야 함. 안 그러면 **진정한 무한대 외삽 AUC**를 얻을 수 없음 [G&W 5e p.414].

### 6.6. Day 1 AUC vs SS AUC — 가장 함정인 시나리오

용량의존 동태(saturable elimination)와 시간의존 동태(autoinduction)가 **동시에** 존재하면:

$$
\overbrace{\text{noise-free Day 1 vs SS AUC 비교}}^{\text{겉보기에 변화 없음}}
=\underbrace{\text{capacity 효과}}_{\text{AUC 증가 방향}} + \underbrace{\text{induction 효과}}_{\text{AUC 감소 방향}}
$$

두 효과가 서로 상쇄되어 **노출이 변하지 않은 것처럼 보임**. 그런데 기전은 둘 다 작동 중임. Fig.5.20의 핵심 메시지 — "AUC 같음 = 기전 같음"이라는 가정은 함정이며, capacity와 induction이 동시에 작동하면 AUC만으로는 둘을 구분 못 함 [G&W 5e p.414].

### 6.7. 임상으로의 전파 — M6를 안 돌리면 무엇이 무너지는가

| 빠뜨린 stress test | 임상에서 나타나는 결과 |
|---|---|
| $V_{max}$/$K_M$ perturbation | 고용량에서 예측보다 높은 농도 → 안전성 문제 |
| $IC_{50}$ perturbation | PD 효과의 용량-반응 관계 misspecification |
| 비선형 제거 영역 sampling 부족 | AUC 외삽이 무한대로 발산하거나 과대평가 |
| Day 1 vs SS 분리 안 함 | 정상상태 노출 예측 실패 → Phase 2 용량 오류 |

### 6.8. M6 한 줄 정리

> **민감도 분석은 "parameter를 잘 추정했는가"보다 먼저 "잘못 추정하면 어떤 결론이 흔들리는가"를 물음. 흔들리는 결론이 용량·안전역·sampling 일정이라면 다음 실험 설계 자체를 다시 짜야 함.**

---

## 7. 마지막 검문 — fit이 좋아도 generative fit은 다른 얘기 (VPC/pcVPC/NPDE)

### 7.1. 왜 M2의 잔차 진단으로 부족한가

M2의 잔차가 random scatter임을 확인했다고 끝이 아님. 결정적 차이 한 가지:

$$
\underbrace{\text{GOF 잔차/precision/AIC}}_{\text{model-fit-based: 추정값이 데이터를 얼마나 잘 \emph{설명}?}}
\quad\longrightarrow\quad
\underbrace{\text{VPC/pcVPC/NPDE}}_{\text{simulation-based: 모델이 데이터를 얼마나 잘 \emph{생성}?}}
$$

GOF는 **fitted curve가 데이터에 얼마나 가까운가**를 봄. 그런데 fitted curve는 정의상 fit 과정에서 잔차를 최소화하도록 끌려간 좌표임. 즉 잔차가 random인 건 거의 보장된 결과임. 이건 "모델이 데이터를 설명할 수 있다"는 증거지, "모델이 같은 종류의 데이터를 생성할 수 있다"는 증거는 아님.

VPC가 채우는 빈자리가 정확히 이거임 — 추정된 모델 + 추정된 random effect 구조로부터 **새 dataset을 수백 번 simulation**해서, 그 simulation의 percentile band와 관측 데이터의 동일 percentile을 겹쳐 봄. 모델이 관측의 central tendency뿐 아니라 **variability envelope까지** 재현하면 비로소 "생성 모델로서도 신뢰할 만한" 상태가 됨 [Holford NHG. *PAGE* 2005; Karlsson MO & Holford NHG. *PAGE* 2008].

### 7.2. pcVPC가 정확히 보정하는 것 — prediction correction

단순 VPC가 잘 작동하려면 simulation된 관측치들이 **같은 비교 자리에 모여 있어야** 함. dose가 다른 그룹, BW가 크게 다른 코호트, 강한 covariate 효과가 있으면 같은 시간점이라도 typical prediction이 다른 scale을 만듦. 그러면 simulation 분포가 두 모드로 갈라지거나 envelope이 섞여서, "모델 실패"인지 "design 차이"인지 구분이 안 됨.

pcVPC는 각 관측치를 해당 조건의 모집단 예측값으로 정규화함:

$$
\overbrace{Y_{ij}^{pc}}^{\text{prediction-corrected 관측}}
=\overbrace{Y_{ij}}^{\text{원관측}}\cdot
\frac{\overbrace{\widetilde{\text{PRED}}_{bin}}^{\text{bin 내 median typical prediction}}}{\underbrace{\text{PRED}_{ij}}_{\text{개체별 typical prediction}}}
\quad [\text{Bergstrand M et al. } AAPS\ J\ 2011;13(2):143-51]
$$

이 한 줄이 보정하는 건 정확히 **"design/dose/covariate 차이로 생긴 typical prediction scale 차"**임. 모델이 실제로 못 맞춘 부분은 남고, 좌표 차이만 사라짐. pcVPC가 통과 안 하면 "모델이 trend는 따라가는데 variability 구조를 못 잡았다"는 진단이 됨.

### 7.3. NPDE — 분포 위치의 수치 검정

VPC는 percentile band 시각 비교라서 직관은 좋지만 수치적 통계 검정이 어려움. NPDE는 각 관측치가 simulation 분포 안에서 차지하는 위치를 **probability integral transform** 후 정규분포로 변환해서 표준정규 N(0,1)에 대한 검정으로 환원함 [Brendel K et al. *Pharm Res* 2006;23(9):2036-49]:

$$
\overbrace{pde_{ij}}^{\text{distribution error}}
=\underbrace{F_{sim}(Y_{ij})}_{\text{simulation CDF에서 관측의 위치}}
\quad\longrightarrow\quad
\overbrace{npde_{ij}}^{\text{정규화 PDE}}
=\Phi^{-1}\!\left(\underbrace{pde_{ij}}_{\text{0--1 위치}}\right)
$$

| NPDE 결과 | 해석 |
|---|---|
| N(0,1) 따름 | 모델 적합 |
| mean ≠ 0 | bias |
| variance ≠ 1 | variability misspecification |
| Shapiro–Wilk 깨짐 | 분포 형태 오류 |

### 7.4. M2~M4 시그니처와 VPC/NPDE 신호의 환승

| 단계 진단 신호 | VPC/NPDE에서의 대응 |
|---|---|
| M2 banana/U-shape (구조 오류) | VPC median band가 관측 median을 시간축에서 계통적으로 빗나감 |
| M2 fan shape (분산 모델 오류) | VPC의 5–95% band 폭이 관측 spread를 못 따라감 |
| M3 F/AIC가 모델 우월을 못 가림 | VPC envelope 적합도 비교가 결정 권한을 가져옴 |
| M4 높은 parameter 상관 | pcVPC가 ridge 위 동일 fit 두 모델을 구분 못함 → bootstrap/SIR로 추가 환승 |

### 7.5. 한 줄 정리

> **VPC는 GOF의 대체가 아니라 다음 검문임. GOF가 "모델이 데이터를 설명할 수 있는가"라면 VPC는 "모델이 같은 종류의 데이터를 생성할 수 있는가"를 물음. pcVPC는 design/covariate 차이로 생긴 좌표 차를 제거하고, NPDE는 시각 검토에 수치 검정을 더함.**

---

## 8. 실무에서 헷갈리는 4쌍 — 혼동쌍 정리

### 쌍 1: 중첩 + 동일 가중치 vs 비중첩 또는 다른 가중치

| 비교 기준 | A (F-test/AIC 사용 가능) | B (사용 불가) |
|---|---|---|
| 조건 | nested + equal weighting | non-nested 또는 다른 weighting |
| WRSS 비교 의미 | parameter 추가 효과 | 좌표계 차이가 섞여 해석 불가 |
| 대표 사례 | Ordinary Emax vs Sigmoid Emax | MM weighted vs first-order unweighted |
| 임상 결과 | 적절한 추가 parameter 검정 | 잘못된 모델 → dose simulation 오염 [G&W 5e pp.387–389] |

> **기억 고리** — F-test는 "**중첩 + 같은 가중치**" 자물쇠가 둘 다 맞아야 열림.

### 쌍 2: 상관계수 $r$ vs 진정한 GOF

| 비교 기준 | A ($r$) | B (진정한 GOF) |
|---|---|---|
| 본질 | dynamic range가 끌어올리는 보조 숫자 | 잔차·precision·correlation의 복합 판정 |
| PK 데이터에서 | 거의 항상 0.95+ | model-by-model 다양함 |
| 단독 사용 시 위험 | terminal bias 못 봄 | (해당 없음) |
| 사례 | OLS $r=0.96$인데 terminal 과소예측 | IRLS $r=0.94$인데 더 좋은 fit [G&W 5e pp.381–382] |

> **기억 고리** — **$r$은 큰 방향만 보고, 잔차는 모델의 거짓말을 봄.**

### 쌍 3: 구조 모델 오류 vs 분산/가중치 모델 오류

| 비교 기준 | A (구조 오류) | B (분산 오류) |
|---|---|---|
| 진단 시그니처 | banana, U-shape, run | fan shape, 농도의존 spread |
| 처방 | 모델 구조 변경 (compartment 추가, lag-time, exp term) | weighting scheme 변경 |
| 잘못 처방 시 | weighting만 바꿔서 구조 오류 가림 | compartment 추가로 분산 문제 복잡화 [G&W 5e pp.372–376] |

> **기억 고리** — **모양이 휘면 구조를 의심, 폭이 벌어지면 분산을 의심.**

### 쌍 4: 이상치 A (수직 이탈) vs 이상치 B (시간축 이탈, high leverage)

| 비교 기준 | A | B |
|---|---|---|
| 본질 | 참 곡선에서 수직 이탈 | sampling time/reporting error, high leverage |
| 효과 | residual 크기 증가 → precision ↓ | curve 방향 자체를 끌어 bias |
| 위험도 | 잡음으로 처리 가능 | 잘못된 curve가 정밀해 보이는 편향 [G&W 5e p.390] |

원문 핵심 메시지 — **table만 봐서는 A와 B를 구분하기 어려움. graphical presentation이 결정적**임.

> **기억 고리** — **A는 위아래로 튄 점, B는 시간을 잘못 말하는 점. B가 더 위험함 — 곡선 방향 자체를 바꿈.**

---

## 9. 자기 점검 — 능동 회상

### Q1. [회상 ★★]
초기값이 부실할 때 G&W가 명시한 세 가지 위험은?

**답** — 잘못된 final estimate, local minimum 갇힘, 생리학적으로 불가능한 parameter [G&W 5e p.353].

### Q2. [계산 ★★]
10 mg IV bolus에서 slope $-0.01\ \text{min}^{-1}$일 때 $t_{1/2}$, AUC, Cl, V의 anchor는?

**답** — $t_{1/2}\approx65\ \text{min}$, $AUC=100{,}000\ \mu g\cdot L^{-1}\cdot\text{min}$, $Cl=0.1\ L\cdot\text{min}^{-1}$, $V=10\ L$ [G&W 5e Eq.4:17–4:20].

### Q3. [회상 ★]
이중지수 curve stripping에서 말단상을 먼저 읽는 이유는?

**답** — $\alpha \gg \beta$이면 말단에서 $Ae^{-\alpha t}$가 사실상 사라지고 $Be^{-\beta t}$만 남기 때문임. 자연이 만들어준 "한 phase 분리 구간"임 [G&W 5e pp.354–355].

### Q4. [진단 ★★]
잔차 도표의 banana와 fan은 각각 무엇을 의심하게 하는가?

**답** — Banana/U-shape는 **구조적 시간 스케일 문제**(빠진 exp term, 잘못된 구조). Fan은 **농도의존 분산 또는 weighting 불일치**. 처방이 완전히 다름 [G&W 5e pp.372–376].

### Q5. [핵심 적용 ★★]
Ordinary Emax vs Sigmoid Emax에 F-test? Linear vs Ordinary Emax에 F-test?

**답** — 앞은 nested이므로 가능($n=1$ fix). 뒤는 일반 nested 아니므로 불가 [G&W 5e p.388].

### Q6. [판정 ★★]
MM weighted vs first-order unweighted에서 AIC 낮은 쪽을 그냥 골라도 되는가?

**답** — 안 됨. **non-nested + 다른 weighting**이라 F-test도 AIC도 둘 다 불가 [G&W 5e p.389].

### Q7. [계산 ★★]
Residual SS = 92.67, pure error SS = 23.61, df = 25, 21일 때 $F_{LOF}$? 결론?

**답** — $F_{LOF}=[(92.67-23.61)/(25-21)]/(23.61/21)=15.35$. $F_{crit}=2.76$보다 훨씬 크므로 lack-of-fit 있음. 단, 반복 측정으로 pure error 분리 가능할 때만 적용 [G&W 5e pp.378–379].

### Q8. [설계 ★★]
Fig.4.55–4.57의 design A vs B가 가르치는 핵심은?

**답** — parameter 상관·신뢰 타원은 모델 방정식만의 문제가 아니라 **sampling design의 결과**임. 좋은 설계는 두 parameter의 정보 영역을 분리해서 상관과 신뢰구간을 낮춤 [G&W 5e pp.383–385].

### Q9. [통계 ★★]
NONMEM에서 covariate 추가했더니 $\Delta\text{OFV}=5.2$. forward inclusion ($\alpha=0.05$)에서 채택? backward elimination ($\alpha=0.01$)에서 살아남나?

**답** — Forward 임계 $\chi^2_{1,0.95}\approx3.84$이므로 $5.2>3.84$ → **채택**. Backward 임계 $\chi^2_{1,0.99}\approx6.63$이므로 $5.2<6.63$ → **탈락**. 두 단계 임계가 다른 이유는 다중 비교 보정·robustness [Wilks 1938; Wählby et al. 2002].

### Q10. [개념 ★★]
NONMEM $COV$ step이 실패함. 두 가지 대안과 작동 원리는?

**답** — **Bootstrap**: 데이터를 with-replacement 재표집해 각 dataset에 모델을 다시 fit → $\hat\theta^{(b)}$의 경험적 분포에서 percentile CI. asymptotic 가정 불요지만 비용 큼. **SIR**: proposal 분포에서 parameter vector sampling → likelihood ratio로 importance weight → weighted resample로 posterior 근사. fit 1회면 충분해서 비용 적음 [Efron 1979; Dosne et al. 2016].

### Q11. [개념 ★★]
M2/M3/M4 모두 통과한 모델이 VPC에서 실패함. 무엇이 잘못된 건가?

**답** — GOF/잔차/AIC는 **model-fit-based** — fitted curve는 정의상 데이터로 끌려가니 잔차 random이 보장되기 쉬움. 모델이 데이터를 "설명"한다는 증거만 줌. VPC는 **simulation-based** — 추정 모델 + random effect 구조로 새 dataset을 수백 번 생성해 percentile band가 관측 envelope을 재현하는지 봄. VPC 실패 = variability 구조(IIV/RUV 모델) misspecification. pcVPC 실패 = design/covariate 차이를 변동성으로 흡수. NPDE가 N(0,1) 벗어남 = 분포 형태 오류 [Holford 2005; Bergstrand et al. 2011; Brendel et al. 2006].

### Q12. [Boss Dilemma ★★]
한 모델은 WRSS 더 낮은데 다른 weighting을 썼고, 다른 모델은 기전적으로 더 타당한데 AIC 차이가 작음. 어느 모델로 가는가?

**답** — 먼저 **같은 weighting으로 다시 fit해서 비교 가능성 확보**. 그래도 F-test/AIC가 단독 결론을 안 주면 **잔차 패턴 + 기전 타당성 + 외부 데이터 + VPC/pcVPC**의 삼각 검증. G&W는 AIC 차이 cutoff를 정의하지 않으므로 낮은 AIC 하나가 기전 타당성을 못 이김 [G&W 5e p.389, p.391].

---

## 10. 메타 프레임 — 한 줄로 압축한 모든 것

### 10.1. 사슬 한 번에 보기

```text
[M1] 출발 좌표 anchor (그래프/NCA)
       ↓ (틀리면 local minimum → 이하 전부 무의미)
[M2] 잔차 진단: banana vs fan
       ↓ (구조 오류와 분산 오류 처방 분리)
[M3] 비교 자격: nested + equal weighting
       ↓ (NONMEM ΔOFV/SCM 3.84/6.63 카이제곱)
[M4] precision/correlation/ridge
       ↓ (asymptotic 깨지면 bootstrap/SIR)
[M5] derivative peak로 다음 sampling 위치 결정
       ↓
[M6] sensitivity perturbation으로 임상 결론 stress test
       ↓
[VPC/pcVPC/NPDE] 생성 모델로서의 마지막 검문
       ↓
[Carousel] 다음 cohort design으로 환승
```

### 10.2. 의존성 사슬 — 어디가 무너지면 무엇이 무너지나

| 변화 상황 | 1차 영향 | 임상 결과 | 조치 |
|---|---|---|---|
| 초기값 틀림 | starting vector | 잘못된 수렴/local min | EDA/NCA/graph anchor 재설정 [G&W 5e p.353] |
| 잔차 계통적 | residual pattern | GOF 성립 불가 | 구조 또는 weighting 재검토 [G&W 5e pp.369–376] |
| 비중첩/다른 weighting | WRSS/AIC 좌표 | F-test/AIC 무력화 | 기전·잔차·외부근거 삼각검증 [G&W 5e pp.387–389] |
| parameter 상관 높음 | precision/correlation | 식별성 취약 | 다음 sampling design 보강 [G&W 5e pp.382–385] |
| asymptotic SE 가정 깨짐 | boundary/소표본 | 표준 CI 신뢰 불가 | bootstrap/SIR로 재구성 [Dosne et al. 2016] |
| Generative fit 미확인 | model-fit only | predictive performance 미확립 | VPC/pcVPC/NPDE [Bergstrand et al. 2011] |
| 정보 위치 불명확 | partial derivative | 예측 결론 흔들림 | derivative peak + sensitivity 기반 설계 [G&W 5e pp.399–405] |

### 10.3. Table 4.9 기반 GOF 체크리스트 (압축)

[G&W 5e p.391]
1. **생물학적 관련성** — 기전 타당성 없는 낮은 AIC는 취약함
2. **fitted curve가 데이터 경향을 재현** — overlay가 1차 관문
3. **parameter precision 충분** — CV%, SE, 신뢰구간 (필요 시 bootstrap/SIR 보강)
4. **잔차 계통적 이탈 없음** — run, banana, fan, lag pattern 체크
5. **잔차 도표가 무작위 산포** — 무작위 아니면 모델 또는 weighting 재검토

### 10.4. 후속 세션 연결

| 후속 세션 | 이번 세션에서 열리는 개념 | 이번 세션 없으면 실패하는 것 |
|---|---|---|
| NONMEM estimation method module | FO/FOCE/FOCEI/Laplacian/SAEM을 **판단 조건**으로 읽기 | OFV·precision·shrinkage 차이를 단순 옵션으로 잘못 읽음 |
| Model qualification module | GOF → VPC/pcVPC/NPDE → bootstrap/SIR 흐름 | 곡선 적합을 predictive performance로 과잉해석 |
| Stepwise covariate modeling module | ΔOFV 카이제곱 임계(3.84/6.63)의 통계적 정당성 | covariate 선택을 임의 임계로 자동화 |
| Adaptive sampling/design module | derivative peak·sensitivity를 다음 설계로 번역 | 정보 없는 시간점에서 반복 sampling |

### 10.5. 압축 한 문장

> **초기값은 알고리즘의 출발 골짜기를 정하고, 잔차는 모델의 거짓말을 드러내며, F-test/AIC는 같은 운동장에서만 의미가 있고, 정밀도와 상관은 sampling design의 품질을 말하며, 편미분 peak는 다음 sample 위치를 정하고, 민감도 분석은 임상 결론의 stress test이며, VPC/pcVPC/NPDE는 모델이 데이터를 *설명*만 하는지 *생성*도 할 수 있는지 마지막으로 묻고, Bootstrap/SIR은 asymptotic SE가 거짓말일 때 결합 불확실성의 진짜 모양을 재구성함.**

이 한 문장이 머리에 박혀 있으면 G&W 5e p.352의 modeling carousel은 그림이 아니라 손에 잡히는 워크플로우가 됨 — **Explore data에서 초기값 만들고, Fit model 후 Analyze output에서 잔차/precision/비교 검토, simulation-based qualification으로 generative fit 확인, 결과를 다음 Design 단계로 환승**.

### 10.6. 거장이 만든 해자 — 왜 경험자는 빨리 결정하는가

경험 많은 모델러는 두 모델이 비슷한 WRSS/AIC를 보일 때 어느 한쪽을 고르기 전에 **둘 다 잘못된 기전일 가능성**을 의심함. 이 역방향 추론이 모델 선택을 **parameter 개수 게임에서 기전 가설 수정으로** 바꿈. 그게 이 세션 전체가 노리는 사고 전환임 — 진단은 체크박스가 아니라 사건 추적임.

---

*— End of Session 15 (Remastered)*

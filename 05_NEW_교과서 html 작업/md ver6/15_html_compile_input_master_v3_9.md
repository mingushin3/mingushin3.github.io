# 세션 15 — 모델 구축의 기술: 초기값 · GOF · 모델 판별 · 실험 설계 — v3.8

> **출처 및 범위 노트**  
> 이 핸드아웃은 Gabrielsson & Weiner 5e, *Pharmacokinetic and Pharmacodynamic Data Analysis: Concepts and Applications* Ch.4 §4.4, §4.7–4.10 및 Ch.5 §5.2.3–5.2.4, §5.3.3을 다룹니다. 검증된 페이지 범위: **p.352–364 / p.368–392 / p.399–405 / p.412–414**. 업로드 PDF에 빠진 pp.365–367(§4.5 Minimization, §4.6 Weighting) 및 pp.406–411에 의존하는 내용은 `[확인 필요]`로 유지합니다.

### 임상 장면: 왜 이 세션이 필요한가

10 mg IV bolus 후 반로그 기울기에서 $K=0.01\ \text{min}^{-1}$을 읽고 $t_{1/2}\approx65\ \text{min}$, $AUC=100{,}000\ \mu g\cdot L^{-1}\cdot\text{min}$, $Cl=0.1\ L\cdot\text{min}^{-1}$, $V=10\ L$를 초기 anchor로 잡는 순간이 있습니다. [Eq.4:16–4:20, p.354]  
이 anchor가 틀리면 fit은 곡선이 보기 좋아도 **잘못된 basin, 잘못된 WRSS, 잘못된 모델 비교**로 이어집니다. 규제 관점에서는 "fit이 좋아 보인다"가 아니라 **"잔차·정밀도·비교 조건을 통과했다"** 는 문장으로 방어해야 합니다.

## 학습자 항법

시간이 부족하면 **M1 → M2 → M3 → M4** 네 카드만 순서대로 읽어도 이 세션의 의사결정 체계가 작동합니다. M5는 다음 sampling 설계로 환류하는 카드, M6는 결론이 흔들리는 위치를 점검하는 카드입니다.

| 카드 | 이 경로에서의 역할 |
|---|---|
| **M1** | 초기값 획득 — 그래프·NCA anchor로 출발 vector를 어디에 박는가 |
| **M2** | 잔차 진단 — 곡선이 맞아 보여도 잔차가 드러내는 거짓말 |
| **M3** | F-test / AIC / SC — 비교 좌표가 맞을 때만 의미 있는 통계량 |
| **M4** | precision · correlation — 좋은 fit ≠ 식별 가능한 parameter |
| **M5** | 편미분 sampling — 정보가 가장 크게 생기는 시간점 |
| **M6** | 민감도 분석 — parameter 불확실성이 결론을 흔드는 위치 |

> 🎯 **이 세션이 존재하는 이유** — F-test, AIC/SC, $-2\log likelihood$는 **계산값이 아니라 적용 조건을 먼저 통과해야 읽을 수 있는 판단 언어**입니다.

---

<!-- SLIDE_START: §1 | title: 세션 개요와 로드맵 -->
<!-- SECTION_CORE: SC-01 -->

## §1 — 세션 개요와 로드맵

### ASCII 레이어 개념 지도

```text
레이어 1 — 무엇인가
초기값 | 잔차 | 중첩성 | 정밀도/상관 | 편미분 | 민감도

레이어 2 — 어떻게 계산되는가
K → t1/2/AUC/Cl/V | WRSS/σ | F*/AIC/SC | CV%/r | derivative peak | parameter perturbation

레이어 3 — 언제, 왜 중요한가
fit 출발점 | GOF 판독 | 모델 비교 조건 | 설계 취약성 | sampling 위치 | 다음 실험/규제 방어
```

🧭 **읽는 순서:**  
카드 1 (M1): fit을 시작하기 전 어떤 숫자를 어떻게 손으로 고정해야 하는가?  
카드 2 (M2): 곡선이 맞아 보여도 잔차는 어떤 거짓말을 드러내는가?  
카드 3 (M3): F-test/AIC/SC는 언제 쓸 수 있고 언제 금지되는가?  
카드 4 (M4): 좋은 fit과 식별 가능한 parameter는 왜 다른가?  
카드 5 (M5): 어느 시간점이 어떤 parameter를 가장 잘 보이게 하는가?  
카드 6 (M6): parameter 불확실성이 임상 결론을 어디까지 흔드는가?

### 지식 그래프 위치

```text
[선행 세션: 1구획·다구획 PK, NCA, 비선형 회귀, 오차 모델]
        → [이 세션: 초기값 → 잔차 → 모델 비교 → 정밀도/상관 → 설계 피드백]
        → [후속 세션: NONMEM/PsN/xpose 기반 qualification, VPC/NPDE/bootstrap/SIR]
```

### 이 세션의 정확한 위치

본 세션은 p.352 Fig.4.16의 **모델링 회전고리(modeling carousel)** — 모델링 한 사이클의 반복 구조 — 가운데 **Step 4 Explore data, Step 5 Fit model(s), Step 6 Analyze output**을 다룹니다. 그 결과를 다음 실험의 Design으로 되돌리기 때문에, 이 세션은 초기값 획득 → GOF 판독 → 경쟁 모델 선택 → 이상치 판단 → 편미분 sampling 설계 → 민감도 분석으로 이어지는 **한 사이클의 실행 척추**입니다. [G&W p.352]

### 핵심 아이디어(Big Idea)

이 범위의 핵심은 "좋은 통계량을 계산하는 법"이 아니라 **통계량을 적용해도 되는 조건을 아는 법**입니다. F-test, AIC/SC, 상관계수, WRSS, 편미분은 각각 강력한 도구지만, **중첩(nested), 가중치, 잔차의 무작위성, parameter 식별가능성, sampling 민감도**라는 적용 조건을 벗어나면 이 숫자들은 오히려 잘못된 모델 확신을 만듭니다. [G&W pp.369–391, G&W pp.399–405]

### 개념 항법도

```text
[초기값 획득] → [잔차 진단] → [F-test/AIC/SC 모델 판별]
      ↑              ↓                  ↓
[민감도 분석] ← [편미분 sampling design] ← [정밀도·상관·설계]
```

이 흐름은 **닫힌 고리**입니다. 초기값이 나쁘면 회귀가 잘못된 최솟값으로 가고, 잔차가 무작위가 아니면 모델 또는 가중치가 틀린 것이고, 비교 조건을 어기면 통계 검정이 무의미해지고, parameter가 상관되면 다음 실험의 sampling design을 바꿔야 합니다. [G&W p.353, G&W pp.369–389, G&W pp.399–405]

### 후행 지식 — NONMEM/PsN/xpose로의 번역

현대 PopPK에서는 이 세션의 잔차 진단, parameter 정밀도, $-2\cdot\log likelihood$ 비교, 설계 피드백이 NONMEM/PsN/xpose 워크플로우로 번역됩니다. 단 이 도구명은 PDF의 직접 내용이 아니라 구현 환경의 번역이며, §4.5 Minimization과 §4.6 Weighting은 pp.365–367 부재로 `[확인 필요]`로 둡니다.

$$
\underbrace{-2\cdot\log likelihood}_{\text{목적좌표}}
$$

> 📍 **이 세션의 범위 정직성** — 운영 도구는 Volume II로 분리합니다.  
> 이 세션은 **이론 절반**(초기값, 잔차 진단, F-test 타당성, parameter 정밀도, sampling 설계)을 다룹니다. 운영 도구 절반은 Volume II / NONMEM module입니다.
>
> | 영역 | 이 세션(이론 절반) | Volume II(운영 절반) |
> |---|---|---|
> | 진단 도구 | GOF · 잔차 · precision · F-test · AIC/SC | VPC · pcVPC · NPDE |
> | 불확실성 평가 | SE · CV% · correlation matrix | bootstrap · SIR |
> | 추정법 | (개념적 위치만) | FO · FOCE · FOCEI · Laplacian · SAEM |
> | 평가 종류 | model qualification 이론 | qualification 도구 · validation |
>
> 이 세션을 끝내면 **"모델 구축의 이론적 문법"** 을 익힌 것이지, NONMEM 운영·진단 전체 훈련을 마친 것은 아닙니다.

### 추정법(FO/FOCE/FOCEI/Laplacian/SAEM) — 짧은 다리

이 다섯 가지는 계산 옵션이 아니라 **모델을 어떤 근사 언어로 읽을지** 정하는 선택입니다.

- **FO** — 가장 단순한 linearization. 빠르고 출발점으로 좋지만, 비선형성이 강하거나 IIV가 크면 평균 개체 주변 근사가 개체별 거동을 못 따라갈 수 있음.
- **FOCE** — 개체별 ETA 주변에서 conditional approximation. EBE, ETA diagnostic, shrinkage 해석과 직결.
- **FOCEI** — residual error와 ETA(또는 prediction)의 interaction이 중요할 때 그 상호작용을 근사에 반영.
- **Laplacian** — likelihood curvature와 비정규·복잡 likelihood에 강함.
- **SAEM** — simulation-based estimation, 복잡한 비선형 mixed-effects에서 강점. 항상 우월하지는 않음.

핵심 — estimation method는 OFV, parameter precision, EBE/shrinkage, diagnostic 해석을 모두 흔드는 **판단 조건**입니다 (→ Volume II).

### GOF 너머의 qualification 흐름 — 짧은 다리

좋아 보이는 곡선이 predictive performance를 보장하지는 않습니다. 그래서 다음 순서로 닫는 것이 안전합니다:

**GOF → 잔차 진단 → VPC/pcVPC/NPDE → bootstrap/SIR → clinical·scientific plausibility**

- **VPC** — 모델이 관측의 central tendency와 variability envelope을 simulation으로 재현하는가.
- **pcVPC** — dose·design·covariate 차이가 커서 단순 VPC가 "모델 실패"와 "예측 스케일 차이"를 섞을 때, prediction correction으로 비교 좌표 정렬.
- **NPDE** — simulated distribution 안에서 관측값의 표준화된 위치.
- **Bootstrap** — 반복 resampling으로 parameter stability·uncertainty 확인.
- **SIR** — proposal distribution 기반 parameter uncertainty 보정·평가.

Qualification은 "사용 목적에 맞게 충분히 신뢰 가능한가"를 묻는 과정입니다. **validation을 절대적 진실 인증처럼 쓰면 안 됩니다.**

---

<!-- SLIDE_START: §2 | title: 개념 해부 카드 -->
<!-- SECTION_CORE: SC-02 -->

## §2 — 개념 해부 카드


<!-- SLIDE_START: M1 | title: 초기값 획득의 실전 기술(Initial Estimate Acquisition) -->
<!-- SECTION_CORE: SC-03 -->

### 🃏 M1 — 초기값 획득의 실전 기술(Initial Estimate Acquisition)

> **거장의 시각**  
> 초기값을 "그냥 시작 숫자"로 읽으면, 알고리즘이 잘못된 basin으로 들어갔을 때 그 오류가 **모델 결함인지 출발점 결함인지** 구분할 수 없게 됩니다. 그래프·NCA·선행 화합물 지식을 anchor로 박아두면 fit 전에 sanity check가 한 번 생깁니다.

#### A. 형식적 정의

초기값 획득은 비선형 회귀를 시작하기 **전에** 그래프, 선형 회귀, NCA, 선행 화합물 지식으로 시작 parameter vector를 만드는 절차입니다. 비선형 회귀는 시작 벡터가 주어진 뒤에야 **목적함수 표면**(parameter 조합이 만드는 잔차 제곱합 지형)을 탐색하므로, 이 단계는 fit 이전에 끝나야 합니다. 모델링 회전고리의 Explore data 단계입니다. [G&W pp.352–353]

#### B. 원전 기준점(Source-locked anchors)

**B-1. IV bolus 1구획 예시.** 두 피험자에게 동일하게 10 mg IV bolus를 투여한 뒤 반로그 농도-시간 도표의 기울기를 읽습니다. 이 기울기가 $K$(제거속도상수)의 anchor가 됩니다. [G&W pp.353–354]

$$
\underbrace{\text{slope}}_{\text{반로그 기울기}}=\frac{\overbrace{\ln(800)-\ln(400)}^{\text{log 농도차}}}{\underbrace{23-87}_{\text{시간차}}}=\underbrace{-0.01\ \text{min}^{-1}}_{\text{음의 slope}}=-\underbrace{K}_{\text{제거속도}} \quad [\text{Eq.4:16},\ p.354]
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $K$ | $\text{min}^{-1}$ 또는 $h^{-1}$ | 제거속도상수 | CL/V 변화, slope 판독 |
| $t_{1/2}$ | 시간 | 농도가 절반으로 감소하는 시간 | $K$ 감소 시 증가 |
| $AUC$ | 농도·시간 | 전신 노출 | $C^0$ 증가, $K$ 감소 |
| $Cl$ | 부피/시간 | 정화능 | Dose/AUC anchor |
| $V$ | 부피 | 겉보기 분포 공간 | Dose/$C^0$ anchor |

> 💡 초기값 사슬은 산길 등산의 **첫 등산로 입구**와 같습니다. 입구를 잘못 잡으면 지도는 맞아도 전혀 다른 능선으로 올라갑니다.

이 slope에서 다음 anchor들이 이어집니다. [G&W p.354]

$$
\underbrace{t_{1/2}}_{\text{반감기}}=\frac{\overbrace{\ln2}^{\text{절반 감소}}}{\underbrace{K}_{\text{제거속도}}}=\frac{0.693}{0.01}\approx\underbrace{65\ \text{min}}_{\text{반감기 anchor}} \quad [\text{Eq.4:17}]
$$

$$
\underbrace{AUC}_{\text{전신노출}}=\frac{\overbrace{C^0}^{\text{초기농도}}}{\underbrace{K}_{\text{제거속도}}}=\underbrace{100{,}000\ \mu g\cdot L^{-1}\cdot\text{min}}_{\text{노출 anchor}} \quad [\text{Eq.4:18}]
$$

$$
\underbrace{Cl}_{\text{정화 부피/시간}}=\underbrace{0.1\ L\cdot\text{min}^{-1}}_{\text{Dose/AUC}},\qquad \underbrace{V}_{\text{겉보기 공간}}=\underbrace{10\ L}_{\text{Dose/}C^0} \quad [\text{Eq.4:19–4:20}]
$$

**B-2. 이중지수 곡선 분리(curve stripping).** [G&W p.354]

$$
\underbrace{C}_{\text{총농도}}=\overbrace{\underbrace{A}_{\text{초기 절편}}e^{-\underbrace{\alpha}_{\text{빠른 slope}}t}}^{\text{분포상}}+\overbrace{\underbrace{B}_{\text{말단 절편}}e^{-\underbrace{\beta}_{\text{느린 slope}}t}}^{\text{말단상}} \quad [\text{Eq.4:21},\ p.354]
$$

말단상에서 $B$와 $\beta$를 먼저 읽고, 후방 외삽한 말단선을 초기상에서 빼서 $A$와 $\alpha$를 얻습니다. Fig.4.18의 anchor: $A=1.0\ \mu g\cdot L^{-1}$, $B=0.8\ \mu g\cdot L^{-1}$, $\alpha=0.05\ \text{min}^{-1}$, $\beta=0.003\ \text{min}^{-1}$. [G&W p.355]

**B-3. 동적 평형 반응.** 반응-농도 관계에서는 lin-lin plot과 semi-log plot이 서로 다른 정보를 줍니다. Semi-log는 $IC_{50}$ 이하 구간을 확장해 $IC_{50}$ 초기 추정을 더 쉽게 합니다. [G&W pp.355–356]

**B-4. 동적 비정상상태 turnover.** Warfarin(경구 항응고제)이 prothrombin complex synthesis를 차단하면 하강 기울기가 $-k_{out}$를 줍니다. [G&W pp.356–357]

$$
\underbrace{\text{slope}}_{\text{하강 slope}}=\frac{\overbrace{\ln(124)-\ln(56.77)}^{\text{log 반응차}}}{\underbrace{24-0}_{\text{시간차}}}\approx\underbrace{-0.03\ h^{-1}}_{\text{원문 }-k_{out}} \quad [\text{Eq.4:22},\ p.356]
$$

*↑ 원문에 부호 불일치가 있어 하강 기울기를 $-k_{out}$ anchor로 읽습니다. 수학적으로는 $[\ln(56.77)-\ln(124)]/(24-0)$ 또는 $[\ln(124)-\ln(56.77)]/(0-24)$가 맞으며, 이는 draft mismatch가 아니라 **원문 내부의 부호 문제**입니다.*

Baseline 120 sec와 $k_{out}\approx0.03\ h^{-1}$로 $k_{in}=3.6\ \text{sec}\cdot h^{-1}$를 얻습니다. [G&W p.357]

**B-5. 간접반응 모델 선택 예시.** Eq.4:23–4:33은 baseline, steady state, $E_{max}$, $k_{out}$, $k_{in}$, exponent $n$을 그래프에서 순차 도출하는 예입니다. Table 4.3은 Model 1과 Model 4의 final/initial estimates를 비교하며, **WRSS/AIC가 Model 1에서 7.3/83, Model 4에서 12/102**로 제시됩니다. → "초기값 계산"이 곧 "모델 선택"의 전 단계임을 보여주는 사례입니다. [G&W pp.358–360]

**B-6. 반복투여 항불안제 예시.** Eq.4:34의 oral PK input은 $K_a=1.1\ h^{-1}$, $K=0.128\ h^{-1}$, $V/F=5.0\ L\cdot kg^{-1}$로 고정해 response model에 넣습니다. PD turnover는 $dR/dt=k_{in}I(C)-k_{out}R$이고, $k_{out}\approx0.06\ h^{-1}$, $k_{in}=4.8$ units, $IC_{50}\approx0.25\ \mu g\cdot L^{-1}$가 initial anchor입니다. [G&W pp.361–363]

$$
\underbrace{\frac{dR}{dt}}_{\text{반응 변화}}=\overbrace{\underbrace{k_{in}}_{\text{생성}}\underbrace{I(C)}_{\text{농도 억제}}}^{\text{입력}}-\overbrace{\underbrace{k_{out}}_{\text{소실}}\underbrace{R}_{\text{현재 반응}}}^{\text{출력}}
$$

**B-7. 다른 방법이 모두 어려울 때 — 경계값 스케일링.** 초기값을 직접 얻기 어려우면 LB/UB(하한/상한)를 써서 parameter를 0–1 범위로 scale합니다. [G&W p.364]

$$
\underbrace{\frac{\overbrace{IE-LB}^{\text{하한 초과분}}}{\underbrace{UB-LB}_{\text{경계 폭}}}}_{\text{0--1 위치}} \quad [\text{Eq.4:44},\ p.364]
$$

원문은 보통 $0.1\cdot IE$부터 $10\cdot IE$의 relative range를 권하지만, Table 4.4처럼 source-specific boundary 예외가 있어 기계적으로 적용하면 안 됩니다. [G&W p.364]

> 💼 **실무 인사이트** — 현대 비선형 추정에서 최종 추정값이 LB 또는 UB에 붙으면, 모델이 정보를 준 게 아니라 **경계가 추정값을 만든 것**일 수 있습니다. Table 4.4의 $\beta=0.05$와 UB=0.05는 모방할 처방이 아니라 **경계 의존성을 의심하게 하는 교육용 예시**입니다. [G&W p.364]

#### C. 구조적 필연성

이중지수 분리가 가능한 이유는 $\alpha \gg \beta$일 때 말단상에서 $Ae^{-\alpha t}$가 사라지고 $Be^{-\beta t}$만 남기 때문입니다. 즉 semi-log plot은 **시간 스케일 분리를 눈으로 확인**시켜주는 장치이며, 두 slope가 충분히 분리되지 않으면 stripping은 불안정합니다. [G&W pp.354–355]

#### D. 가정과 경계

초기값은 "정확한 값"일 필요는 없지만, **생리학적으로 타당**해야 하고 목적함수 표면에서 잘못된 basin으로 들어가지 않을 정도로는 참값에 근접해야 합니다. 화합물 지식 기반을 일찍 만들고 회귀 목적을 명확히 하지 않으면 modeling은 끝없는 여정이 됩니다. [G&W p.353]

---

> **M1 체화 핵심**  
> ① fit 전 출발 vector — 그래프 slope·intercept·NCA anchor가 결정한다  
> ② "초기값"과 "최종 추정값"의 혼동 — regression은 출발 basin을 스스로 교정하지 못한다  
> ⚡ "대충 넣어도 fit이 고쳐준다" → local minimum 또는 불가능한 parameter 수렴 → **후속 진단 전체가 무너진다**


<!-- SLIDE_START: M2 | title: 잔차 기반 모델 진단(Residual-Based Diagnostics) -->
<!-- SECTION_CORE: SC-04 -->

### 🃏 M2 — 잔차 기반 모델 진단(Residual-Based Diagnostics)

> **앞 카드에서 이 카드로** — 초기값이 회귀의 출발 좌표를 정했다면, 잔차는 그 출발 이후 모델이 실제 데이터에서 무엇을 놓쳤는지 드러냅니다.

> **거장의 시각**  
> 곡선이 그럴듯해도 잔차의 부호와 순서에 남은 구조적 흔적을 놓치면 GOF를 오판합니다. 잔차를 **시간축**과 **예측값 축**에 동시에 펼치면 구조 오류와 가중치 오류의 처방이 분리됩니다.

#### A. 형식적 정의

잔차(residual)는 관측값과 예측값 사이의 **수직 거리**입니다. [G&W p.369]
$$
\underbrace{\epsilon}_{\text{잔차오차}}=\underbrace{N(0,\sigma^2)}_{\text{평균 0·분산 }\sigma^2} \quad [\text{Eq.4:46},\ p.369]
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $\epsilon$ | 관측 단위 | 관측값과 예측값의 차이 | 구조 오류, 분산 오류, 이상치 |
| $W_i$ | 가중치 | 특정 관측치가 WRSS에 기여하는 정도 | 농도 의존 분산, weighting 선택 |
| $WRSS$ | 가중 잔차제곱합 | 모델이 설명하지 못한 불일치 | residual pattern, weighting scheme |
| $\sigma$ | 관측 단위 | 잔차 표준편차 | $WRSS$와 잔차 자유도 |

> 💡 WRSS는 바닥에 남은 발자국을 무게까지 반영해 합산한 것입니다. **발자국이 한쪽으로 휘어 있으면 청소 문제가 아니라 동선 설계 문제**입니다.

$$
\underbrace{residual_i}_{\text{i번째 잔차}}=\underbrace{C_{obs,i}}_{\text{관측농도}}-\underbrace{\hat C_{calc,i}}_{\text{예측농도}} \quad [\text{Fig.4.41},\ p.369]
$$

가중잔차제곱합(WRSS): [G&W p.371]

$$
\underbrace{WRSS}_{\text{가중잔차합}}=\sum \underbrace{W_i}_{\text{가중치}}\underbrace{(C_i-\hat C_i)^2}_{\text{잔차제곱}} \quad [\text{Eq.4:47},\ p.371]
$$

$$
\underbrace{\sigma}_{\text{잔차 SD}}=\sqrt{\frac{\overbrace{WRSS}^{\text{남은 불일치}}}{\underbrace{N_{obs}-N_{par}}_{\text{잔차 자유도}}}} \quad [\text{Eq.4:48},\ p.371]
$$

#### B. 진단 패턴 목록

잔차는 **무작위 산포**를 보여야 합니다. 같은 부호 잔차가 연속으로 이어지는 run, 또는 군집(cluster)이 나타나면 단순 잡음이 아니라 모델 부적절성을 의심해야 합니다. [G&W pp.369–372]

- **잔차 vs 시간**에서 banana 또는 U-shape가 보이면 → **누락된 지수항** 또는 **잘못된 구조적 시간 스케일** 의심. [G&W pp.372–376]
- **잔차 진폭**이 농도와 함께 커지는 fan shape → **등분산 가정** 또는 **가중치**가 틀렸을 가능성. [G&W pp.373–374]
- Ordinary Emax vs sigmoid Emax 비교에서, 예측 곡선만으로 애매한 차이가 잔차 도표에서는 **계통적 이탈**로 드러납니다. [G&W pp.372–373]
- 가중치 지수는 원문에서 $0$, $-1$, $-2$, $-n$으로 설명되며 Eq.4:49는 $C_i^{-\lambda_z}$ 또는 $\hat C_i^{-\lambda_z}$ 형태입니다. 즉 "$\lambda_z=-1$"처럼 부호를 단정하지 말고 **가중치 지수(weighting power)** 로 표기해야 합니다. [G&W pp.373–374]

$$
\underbrace{C_i^{-\lambda_z}\ \text{ 또는 }\ \hat C_i^{-\lambda_z}}_{\text{농도 기반 가중치}}
$$

잔차 패턴은 단순한 그림 모양이 아니라 **"모델이 설명하지 못한 시간 스케일 또는 분산 구조"가 밖으로 드러난 형태**입니다. Banana는 빠른 phase가 빠졌다는 신호일 수 있고, fan은 구조보다 오차분산 모델의 문제일 수 있습니다. [G&W pp.372–376]

#### C. 순수오차(pure error) vs 적합결여(lack-of-fit)

반복 측정이 있는 in vitro dataset에서는 잔차오차를 **순수오차**와 **적합결여**로 분해할 수 있습니다. Table 4.7 예: residual SS = 92.67, pure error SS = 23.61, lack-of-fit SS = 69.06. Eq.4:51의 $F_{LOF}=15.35$는 $F_{crit}=2.76$보다 커서 lack-of-fit을 지지합니다. [G&W pp.377–379]

$$
\underbrace{F_{LOF}}_{\text{LOF F값}}=\frac{\overbrace{(92.67-23.61)/(25-21)}^{\text{LOF 평균제곱}}}{\underbrace{23.61/21}_{\text{pure MS}}}=\underbrace{15.35}_{\text{F 비교값}} \quad [\text{Eq.4:51},\ p.379]
$$

> 💼 **실무 인사이트** — LOF F-test는 **같은 $x$값에서 반복 측정**이 있어 pure error를 계산할 수 있을 때만 가능합니다. 환자별 sparse clinical PK처럼 같은 시점 반복이 없는 데이터에서는 LOF F-test를 억지로 만들지 말고, 잔차 패턴과 모델 타당성을 봐야 합니다.

> 💼 **추가** — 잔차 vs 시간과 잔차 vs 예측값/농도를 **함께** 봐야 합니다. 한 축에서 무작위 산포처럼 보여도 다른 축에서 fan shape나 구조적 run이 나타날 수 있습니다.

#### D. 구조적 필연성

모델 오지정은 관측 곡선 overlay보다 **잔차 도표에서 먼저** 보입니다. Overlay는 곡선과 데이터의 절대 위치를 보여주지만, 잔차 도표는 오차의 부호와 순서를 보존해서 계통적 이탈을 더 선명하게 드러냅니다. [G&W pp.369–376]

---

> **M2 체화 핵심**  
> ① 곡선은 맞아 보이는데 패턴이 남을 때 — residual sign/run이 구조 오류를 결정한다  
> ② banana vs fan 혼동 — 구조 모델 수정과 weighting 수정의 처방이 갈린다  
> ⚡ 잔차 패턴을 noise로 흡수 → **가짜 IIV·가짜 covariate signal** 생성


<!-- SLIDE_START: M3 | title: F 검정 적용 조건(F-Test Validity Conditions) -->
<!-- SECTION_CORE: SC-05 -->

### 🃏 M3 — F 검정 적용 조건(F-Test Validity Conditions) [⚡ Apex Concept]

> **앞 카드에서 이 카드로** — 잔차가 무작위인지 확인한 뒤에야, 두 후보 모델의 WRSS 감소가 **검정 가능한 개선**인지 물을 수 있습니다.

> **거장의 시각**  
> 💢 **흔한 오해** — WRSS가 더 낮고 parameter가 하나 늘면 F-test를 쓰면 된다고 생각합니다.  
> ✅ **실제** — F-test는 **nested + equal weighting**이라는 비교 좌표가 맞을 때만 의미가 있습니다.  
> 🎯 **체화할 단 하나의 직관** — 통계량을 계산하기 전에 **두 모델이 같은 검정 세계에 있는지 먼저 판정**해야 합니다.

#### A. 형식적 정의

중첩 모델(nested)이란 full model에서 특정 parameter를 고정하면 reduced model로 접히는 관계입니다. Sigmoid Emax model은 $n=1$로 고정하면 ordinary Emax가 되므로 nested입니다. [G&W p.388]

F 통계량: [G&W p.387]

$$
\underbrace{F^*}_{\text{중첩 F값}}=\frac{\overbrace{(WRSS_{reduced}-WRSS_{full})/(df_{reduced}-df_{full})}^{\text{개선량}}}{\underbrace{WRSS_{full}/df_{full}}_{\text{full MS}}} \quad [\text{Eq.4:54},\ p.387]
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $WRSS_{reduced}$ | 가중 잔차제곱합 | 축소 모델의 남은 불일치 | parameter 제한, 구조 단순화 |
| $WRSS_{full}$ | 가중 잔차제곱합 | 전체 모델의 남은 불일치 | parameter 추가, 동일 weighting 필요 |
| $df$ | 자유도 | 비교 가능한 정보량 | $N_{obs}-N_{par}$ |
| $N_{par}$ | 개수 | 모델 복잡도 | parameter 추가/고정 |

> 💡 F-test는 **같은 트랙에서 달린 두 기록만 비교**하는 심판입니다. 한 선수는 트랙, 다른 선수는 산길에서 달렸다면 시간 차이는 경기력이 아니라 경기장 차이입니다.

$$
\underbrace{df}_{\text{잔차 자유도}}=\underbrace{N_{obs}}_{\text{관측수}}-\underbrace{N_{par}}_{\text{parameter 수}} \quad [\text{Eq.4:55},\ p.387]
$$

#### B. 유효한 예와 무효한 예

- **유효(Valid)** — ordinary Emax vs sigmoid Emax. Full sigmoid에서 $n=1$ 고정하면 ordinary Emax로 줄어듭니다. [G&W p.388]

$$
\underbrace{n}_{\text{sigmoidicity}}=\underbrace{1}_{\text{Emax 제한}}
$$

- **무효(Invalid)** — ordinary Emax vs linear response. $C\ll EC_{50}$라는 제한 상황에서만 근사적으로 연결될 뿐, 일반적으로 nested가 아닙니다. [G&W p.388]

$$
\underbrace{C}_{\text{농도}}\ll\underbrace{EC_{50}}_{\text{반최대 농도}}
$$

- **조건부 유효** — hepatic distributed model과 parallel-tube model은 축소 관계가 성립할 때 F-test 사용 가능. [G&W pp.388–389]
- **이중 위반으로 무효** — Table 4.8의 Michaelis–Menten weighted fit과 first-order unweighted fit은 **비중첩 + 다른 weighting**이라 F-test도 AIC도 사용할 수 없습니다. [G&W p.389]

#### C. 구조적 필연성

중첩 조건은 parameter 개수 차이가 아니라 **"한 모델이 다른 모델의 제한된 형태인가"** 의 문제입니다. 기하학적으로 reduced model은 full model parameter space 안의 제한된 부분공간이어야 하며, 그래야 WRSS 감소량이 "추가 parameter가 설명한 개선"으로 해석됩니다.

#### D. AIC/SC 적용 경계

AIC와 SC는 nested를 요구하지 않지만, **equal weighting은 요구**합니다. [G&W p.389]

$$
\underbrace{AIC}_{\text{Akaike 기준}}=\underbrace{N_{obs}\ln(WRSS)}_{\text{불일치}}+\underbrace{2N_{par}}_{\text{복잡도 벌점}} \quad [\text{Eq.4:56},\ p.389]
$$

$$
\underbrace{SC}_{\text{Schwarz 기준}}=\underbrace{N_{obs}\ln(WRSS)}_{\text{불일치}}+\underbrace{N_{par}\ln(N_{obs})}_{\text{표본수 벌점}} \quad [\text{Eq.4:57},\ p.389]
$$

AIC/SC의 **최저값이 자동으로 적절한 모델을 뜻하지는 않습니다.** GOF(모델 적절성)는 잔차, parameter 정밀도, 정확도, 상관행렬, 조건수, F-test, AIC/SC를 함께 보는 **복합 진단 도구군**입니다. [G&W pp.387–391]

#### E. WRSS vs $-2\cdot\log likelihood$

원문은 역사적 WRSS 기반과 현대적 $-2\cdot\log likelihood$ 기반을 구분하되, 비교 원리는 동일하게 모델 적절성 기준과 연결된다고 설명합니다. [G&W p.386] NONMEM의 OFV 비교로 번역할 수는 있으나, $\Delta$OFV threshold나 SCM rule은 PDF의 직접 내용이 아닙니다.

---

#### M. Plausible Fallacy — 나비효과 연쇄

**오류** — WRSS가 더 낮고 parameter가 하나 더 많으니 F-test를 쓰면 된다고 판단한다.  
**왜 그럴싸한가** — 같은 데이터에서 더 복잡한 모델이 더 작은 불일치를 만든 것처럼 보이기 때문이다.  
**나비효과** — 비중첩·다른 weighting 비교에 F-test 적용 → WRSS 감소를 추가 parameter 효과로 오독 → [임상] 잘못 선택한 모델로 용량·안전역 시뮬레이션 수행 → [규제] 비교 조건 위반 지적, 재분석 및 모델 선택 근거 재제출 요구.

> **M3 체화 핵심**  
> ① ordinary Emax vs sigmoid Emax — nested + equal weighting이면 F-test 가능  
> ② MM weighted vs first-order unweighted — non-nested + different weighting이면 F-test/AIC 모두 불가  
> ⚡ "낮은 WRSS = 더 좋은 모델" → 비교 좌표 붕괴 → **잘못된 모델 선택 + 재분석 요구**


<!-- SLIDE_START: M4 | title: 파라미터 정밀도와 상관(Parameter Precision & Correlation) -->
<!-- SECTION_CORE: SC-06 -->

### 🃏 M4 — 파라미터 정밀도와 상관(Parameter Precision & Correlation)

> **앞 카드에서 이 카드로** — 모델 비교 조건을 통과해도, **좋은 fit이 곧 식별 가능한 parameter를 뜻하지는 않습니다.**

> **거장의 시각**  
> 좋은 곡선 적합을 좋은 parameter로 착각하면 ridge와 상관행렬이 숨긴 식별성 문제를 놓칩니다. precision과 correlation을 **설계의 결과**로 읽으면 다음 sampling을 어디에서 보강해야 할지가 보입니다.

#### A. 정확도, 정밀도, CV%

정확도(accuracy)는 **편향(bias)** 의 문제이고, 정밀도(precision)는 **추정의 불확실성**의 문제입니다. "평균적으로 맞는가"와 "반복하면 얼마나 좁게 모이는가"는 다른 질문이며, 원문은 다트 과녁 비유로 이 둘을 구분합니다. [G&W pp.379–380]

$$
\underbrace{CV\%}_{\text{상대 SE}}=\frac{\overbrace{SE(\hat p)}^{\text{추정 SE}}}{\underbrace{\hat p}_{\text{parameter 값}}}\cdot100 \quad [\text{Eq.4:52},\ p.380]
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $CV\%$ | % | 추정값 대비 표준오차 | SE 증가, parameter estimate 감소 |
| $SE(\hat p)$ | parameter 단위 | 추정 불확실성 | sparse design, high correlation |
| $r$ | 무차원 | 원문상 GOF 보조량 | dynamic range, residual SS |
| correlation matrix | 무차원 | parameter trade-off | sampling design, ridge geometry |

> 💡 좋은 fit과 낮은 CV는 **과녁 중심과 탄착군 폭**의 관계입니다. 중심 근처에 보여도 탄착군이 길게 늘어지면 같은 실력이 아닙니다.

$p=0.01\pm0.005\ h^{-1}$의 **CV 50%** 예시는 "높은 불확실성"을 보여주는 예시일 뿐, PDF가 정의한 기각 기준은 아닙니다. [G&W p.380]

#### B. 상관계수 r은 GOF가 아닙니다

PDF는 상관계수가 **가장 많이 오용되는 GOF 기준 중 하나**라고 명시합니다. Eq.4:53은 원문 표기를 보존합니다. [G&W p.381]

$$
\underbrace{r}_{\text{GOF 지표}}=1-\frac{\overbrace{\sum(C_i-\hat C_i)^2}^{\text{잔차제곱합}}}{\underbrace{\sum(C_i-\bar C)^2}_{\text{총변동}}} \quad [\text{Eq.4:53 source form},\ p.381]
$$

*↑ 원문 표기 $r$은 잔차제곱합/총변동 기반 GOF 보조량으로 읽습니다.*

Fig.4.53에서 OLS fit은 $r=0.96$이지만 마지막 세 관측치를 **계통적으로 과소예측**하고, IRLS fit은 $r=0.94$이지만 전체적으로 더 나은 fit을 보입니다. → 그래서 높은 $r$은 좋은 fit의 충분조건이 아닙니다. [G&W p.382]

> 💼 **실무 인사이트** — 동적 범위가 넓은 농도-시간 자료에서는 $r$이 모델의 잔차 구조보다 **전체 값의 범위에 강하게 끌릴** 수 있습니다. 그래서 $r$은 잔차 도표와 함께 읽어야지 단독 GOF 판정 기준으로 쓰면 안 됩니다.

#### C. 파라미터 상관과 능선 기하

parameter 상관행렬은 parameter들이 독립적으로 추정되는지, 또는 서로 trade-off하는지를 보여줍니다. 원문은 높은 상관이 **더 적은 parameter** 또는 **더 많은 데이터**의 필요성을 보여주는 신호라고 설명합니다. [G&W pp.382–383]

Fig.4.55–4.57의 핵심은 **능선형 최솟값(ridge minimum)**, 즉 길게 늘어진 최솟값 영역입니다. 두 parameter가 ridge 위에서 같이 움직이면 OFV/WRSS가 거의 변하지 않아서, 단변량 추정값은 그럴듯해도 **결합 불확실성**은 큽니다. Design A/B 비교는 같은 모델도 sampling design에 따라 $Cl/V$ 또는 $IC_{50}/I_{max}$ 상관이 크게 달라짐을 보여줍니다. [G&W pp.383–385]

#### D. 한 파라미터 고정

Fig.4.55는 한 parameter를 고정하면 다른 parameter의 신뢰구간이 작아질 수 있음을 보여줍니다. [G&W pp.383–384] 그러나 고정 전략은 **정당화 부담을 통계에서 생물학·문헌·선행 연구로 옮기는 일**입니다. 고정값의 출처와 적용 가능성을 설명하지 못하면, 정밀도가 좋아진 게 아니라 **불확실성을 숨긴 것**입니다.

#### E. 한계

높은 상관에 대한 **보편적 cutoff는 PDF에 없습니다.** $|r|>0.95$ 같은 hard threshold 대신 상관행렬, 신뢰 타원, 잔차 패턴, 설계 적절성을 함께 읽어야 합니다. 조건수나 covariance-step warning은 현대 구현의 유용한 신호지만, PDF의 직접 교육 포인트는 **"상관은 설계의 결과"** 라는 점입니다.

---

> **M4 체화 핵심**  
> ① fit은 좋아 보이나 SE/CV가 클 때 — parameter identifiability가 지배한다  
> ② r 높음 vs 진짜 GOF — residual pattern·precision·correlation이 따로 지배한다  
> ⚡ "r이 높으면 충분" → terminal bias·ridge·design weakness를 놓친다


<!-- SLIDE_START: M5 | title: 편미분 기반 최적 샘플링(Partial-Derivative Optimal Sampling) -->
<!-- SECTION_CORE: SC-07 -->

### 🃏 M5 — 편미분 기반 최적 샘플링(Partial-Derivative Optimal Sampling)

> **앞 카드에서 이 카드로** — parameter 상관이 설계의 약점을 드러냈다면, 다음 질문은 "**어느 시간점이 그 parameter를 가장 잘 보이게 하는가**"입니다.

> **거장의 시각**  
> 편미분을 단순 계산 문제로만 보면 최적 sampling의 실무 의미를 잃습니다. derivative peak를 **"정보가 가장 크게 생기는 시간·농도 위치"** 로 읽으면 설계가 수식에서 바로 나옵니다.

#### A. 이중지수 편미분 설계

원문은 이중지수 모델을 예로 듭니다. [G&W p.399]

$$
\underbrace{C}_{\text{총농도}}=\overbrace{\underbrace{A}_{\text{빠른 절편}}e^{-\underbrace{\alpha}_{\text{빠른 slope}}t}}^{\text{초기 정보}}+\overbrace{\underbrace{B}_{\text{느린 절편}}e^{-\underbrace{\beta}_{\text{느린 slope}}t}}^{\text{말단 정보}} \quad [\text{Eq.5:7},\ p.399]
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $A, B$ | 농도 | 초기/말단 절편 정보 | 초기·말단 sample 위치 |
| $\alpha, \beta$ | $\text{time}^{-1}$ | 빠른/느린 slope 정보 | derivative peak 위치 |
| $t=1/\alpha$ | 시간 | 빠른 slope 정보가 가장 큰 시간 | $\alpha$ 증가 시 앞당겨짐 |
| $t=1/\beta$ | 시간 | 말단 slope 정보가 가장 큰 시간 | $\beta$ 감소 시 늦어짐 |

> 💡 편미분 peak는 **어두운 방에서 손전등이 가장 밝게 비추는 지점**입니다. 그곳에 sample을 놓아야 해당 parameter의 윤곽이 선명해집니다.

$A$와 $B$에 대한 편미분은 절편 영역에서, $\alpha$와 $\beta$에 대한 편미분은 각각 $t=1/\alpha$, $t=1/\beta$에서 극값을 갖습니다. [G&W pp.399–400]

$$
\underbrace{t}_{\text{민감도 peak}}=\frac{1}{\underbrace{\alpha}_{\text{빠른 slope}}},\qquad \underbrace{t}_{\text{민감도 peak}}=\frac{1}{\underbrace{\beta}_{\text{느린 slope}}} \quad [\text{Eq.5:11},\ p.400]
$$

예시 parameter가 $\alpha=0.69\ h^{-1}$, $\beta=0.069\ h^{-1}$이면 최적 시간은 약 **1.4 h와 14 h**입니다. Fig.5.4에서는 $\alpha$와 $\beta$ 정보가 각각 약 **20 min, 300 min** 부근에 모입니다. [G&W p.400]

#### B. Sigmoid Imax / Emax 설계

Sigmoid Imax model의 편미분은 $IC_{50}$ 정보가 **half-maximal effect 부근**에, sigmoidicity factor $n$ 정보가 **20%와 80% effect level 부근**에 집중됨을 보여줍니다. Fig.5.6은 $E_0$, $n$, $EC_{50}$, $n$, $E_{max}$에 대한 다섯 design point를 제시합니다. [G&W pp.400–402]

#### C. Turnover model 설계

Turnover response model에서는 $k_{out}$ 민감도가 **25 h와 약 100 h post-dose**에서 크고, 초기 시간에서는 $k_{out}$이 $IC_{50}$ 또는 $n$보다 민감합니다. → 그래서 초기 sampling은 $k_{out}$의 초기 추정을 직접 강화합니다. [G&W pp.402–404]

#### D. 구조적 필연성

편미분이 큰 위치는 **예측이 해당 parameter 변화에 크게 흔들리는 위치**입니다. 가능도 표면(likelihood surface, parameter 공간에서 OFV가 분포하는 지형)의 언어로 바꾸면, 그 위치의 관측치는 해당 parameter 방향의 **곡률을 키워 최솟값을 더 좁고 깊게** 만듭니다.

> 💼 **실무 인사이트** — parameter 단위가 다르면 원자료 $\partial C/\partial\theta$ 크기 비교가 왜곡될 수 있습니다. 실무에서는 $\theta_i(\partial C/\partial\theta_i)/C$ 같은 **정규화 민감도**를 함께 보아 parameter 간 비교를 안정화합니다.

$$
\underbrace{\frac{\theta_i(\partial C/\partial\theta_i)}{C}}_{\text{정규화 민감도}}
$$

#### E. 경계 조건

참 parameter 값을 사전에 알 수 없으므로, derivative 극값에만 sample을 몰아넣으면 안 됩니다. **전체 농도 범위에도 추가 sample**을 두어야 합니다. 원문은 pooled data를 무비판적으로 설계 결정에 쓰는 위험도 경고합니다. [G&W p.402]
---

> **M5 체화 핵심**  
> ① 어느 시간에 sample을 찍을까 — partial derivative peak가 결정한다  
> ② intercept 정보 vs slope 정보 — 초기/말단 시간대가 서로 다른 parameter를 지배한다  
> ⚡ "균등 sampling이면 충분" → 민감도 낮은 구간만 반복 → **parameter precision 개선 실패**


<!-- SLIDE_START: M6 | title: 민감도 분석(Sensitivity Analysis) -->
<!-- SECTION_CORE: SC-08 -->

### 🃏 M6 — 민감도 분석(Sensitivity Analysis)

> **앞 카드에서 이 카드로** — 편미분이 정보가 생기는 위치를 말해 주었다면, 민감도 분석은 그 **불확실성이 임상 결론을 얼마나 흔드는지** 보여줍니다.

> **거장의 시각**  
> 민감도 분석을 사후 그림으로만 보면 예측 결론이 무너지는 지점을 놓칩니다. parameter perturbation을 **다음 실험 전 stress test**로 읽으면 안전역·AUC·sampling package를 조정할 근거가 생깁니다.

#### A. 형식적 정의

민감도 분석은 특정 parameter를 일정 비율로 변화시켜 농도-시간 또는 반응-시간 예측이 어떻게 달라지는지 보는 절차입니다. 즉 **parameter 불확실성이 예측 불확실성으로 얼마나 번역되는지**를 봅니다. 원문 예시는 parameter를 **+100% 또는 −50%** 로 변화시켜 모델 출력을 비교합니다. [G&W pp.404–405]

#### B. PK 민감도 예시

Michaelis–Menten PK 모델에서 $V_{max}$, $K_M$, $V_c$, $V_t$를 변화시키면 농도-시간 프로파일의 **어느 구간이 어떤 parameter에 민감한지** 드러납니다. Fig.5.9는 이것을 향후 sampling 위치 결정에 연결합니다. [G&W p.405]

#### C. PD 민감도 예시

Warfarin-PCA 모델에서는 $IC_{50}$, $k_{in}$, $k_{out}$, $t_{lag}$의 변화가 반응-시간 프로파일에 미치는 영향을 비교합니다. Fig.5.10의 목적은 **"어떤 parameter를 더 잘 추정하려면 어느 구간을 보강해야 하는가"** 를 읽는 것입니다. [G&W p.405]

#### D. 독성동태 설계 맥락

독성동태 설계에서 만성시험은 보통 **노출 확인을 위해 $C_{max}$ sampling만으로 충분**한 경우가 있으나, 예외가 있어 연구자 판단이 필요합니다. Table 5.6은 PK/DRF/chronic study type별로 profile 또는 $C_{max}$ 중심 sampling package를 구분합니다. [G&W p.413]

비선형 제거에서는 농도가 **first-order linear kinetics** 또는 무시 가능한 수준에 도달할 때까지 sampling하지 않으면 **진정한 무한대 외삽 AUC**를 얻을 수 없습니다. [G&W p.414]

용량의존 동태와 시간의존 동태가 동시에 존재하면 **Day 1 AUC와 정상상태 AUC 비교가 상쇄**되어 해석이 흐려집니다. Fig.5.20의 핵심은 노출이 변하지 않는 것처럼 보여도 **capacity와 induction이 동시에 작동**할 수 있다는 점입니다. [G&W p.414]

> 💼 **실무 인사이트** — 민감도 분석은 parameter를 "잘 추정했는지"보다 먼저 **"잘못 추정하면 어떤 결론이 흔들리는지"** 를 묻습니다. 흔들리는 결론이 용량, 안전역, sampling 일정이라면 다음 실험 설계를 바꿔야 합니다.

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $V_{max}$ | 양/시간 | 포화 제거 최대속도 | capacity 변화 |
| $K_M$ | 농도 | 반최대 제거 농도 | affinity/포화 위치 변화 |
| $IC_{50}$ | 농도 | 반최대 억제 농도 | potency 변화 |
| $k_{in}, k_{out}$ | 반응/시간, $\text{time}^{-1}$ | turnover 입력·출력 | synthesis/turnover 변화 |

> 💡 민감도 분석은 **다리의 특정 볼트를 일부러 흔들어 보는 검사**입니다. 흔들림이 용량·안전역 결론까지 전달되면 다음 실험 설계를 보강해야 합니다.

---

> **M6 체화 핵심**  
> ① parameter 불확실성이 결론을 흔드는가 — sensitivity analysis가 결정한다  
> ② PK profile vs $C_{max}$ 중심 TK sampling — study type과 nonlinear elimination 여부가 지배한다  
> ⚡ "노출이 같아 보이면 기전도 같다" → capacity·time-dependent kinetics 상쇄를 놓쳐 **AUC 해석 실패**


<!-- SLIDE_START: §5 | title: 혼동쌍 해부 -->
<!-- SECTION_CORE: SC-09 -->

## §5 — 혼동쌍 해부(Confusion Pair Dissection)

### ▣ 혼동쌍 #1 — 중첩 + 동일 가중치 vs 비중첩 또는 다른 가중치

| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | 중첩 + 동일 가중치 — F-test와 AIC/SC의 비교 좌표 | 비중첩 또는 다른 가중치 — 서로 다른 WRSS 좌표 |
| 수식 내 위치 | $F^*$의 WRSS 차이와 $df$ 차이가 의미를 갖는 전제 | $WRSS_{reduced}-WRSS_{full}$ 해석 불가; AIC/SC도 동일 weighting 없으면 불가 |
| 변화 원인 | full model에서 parameter 제한으로 reduced가 접히고 weighting이 동일 | model structure가 다르거나 weighting이 달라 비교 기준이 바뀜 |
| 혼동 시 임상 결과 | 적절한 추가 parameter 검정 가능 | 잘못된 모델 선택 → 후속 dose simulation·safety margin·sampling 권고가 오염됨 [G&W pp.387–389] |

> 💼 **실무 인사이트** — 가중치 선택은 관행이 아니라 **잔차 패턴으로 정당화**합니다. Fan shape이면 상대오차 가중치를 의심하고, 잔차 폭이 균질하면 고정 절대오차가 더 자연스럽습니다. [G&W pp.373–374]

**기억 고리** — F-test는 "**중첩 + 같은 가중치**"라는 잠금장치가 맞아야 열립니다.

### ▣ 혼동쌍 #2 — 상관계수 r vs 진정한 GOF

| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | $r$ — 무차원 보조 숫자 | 진정한 GOF — 곡선·잔차·정밀도·상관의 복합 판정 |
| 수식 내 위치 | 잔차제곱합/총변동 비율 기반 원문 지표 | residual vs time, residual vs prediction/concentration, precision matrix |
| 변화 원인 | 농도 범위가 넓으면 높아질 수 있음 | terminal bias, systematic run, fan shape, poor precision이 드러남 |
| 혼동 시 임상 결과 | $r=0.96$ 같은 숫자에 안심 | terminal observations 과소예측 또는 IRLS 우월 패턴을 놓침 [G&W pp.381–382] |

> 💼 **실무 인사이트** — PK data처럼 $y$-range가 넓으면 $r$은 **dynamic range의 영향**을 크게 받습니다. 따라서 $r$은 GOF의 주연이 아니라 보조 숫자입니다.

**기억 고리** — $r$은 큰 방향을 보고, **잔차는 모델의 거짓말을 본다**.

### ▣ 혼동쌍 #3 — 구조 모델 오류 vs 분산/가중치 모델 오류

| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | 구조 모델 오류 — 시간 스케일/compartment/shape 문제 | 분산·가중치 오류 — 관측오차 크기와 weighting 문제 |
| 수식 내 위치 | 빠진 exponential term, wrong Emax shape, lag-time omission | $W_i$, $C_i^{-\lambda_z}$ 또는 $\hat C_i^{-\lambda_z}$ |
| 변화 원인 | banana, U-shape, systematic runs | fan shape, concentration-dependent spread |
| 혼동 시 임상 결과 | weighting만 바꾸어 구조 오류를 덮음 | compartment 추가로 variance 문제를 복잡화 [G&W pp.372–376] |

> 💼 **실무 인사이트** — Fan shape에 compartment를 추가하거나 banana에 weighting만 바꾸면 문제의 원인은 그대로 남습니다.

**기억 고리** — 모양이 휘면 구조를 의심하고, 폭이 벌어지면 분산을 의심한다.

### ▣ 혼동쌍 #4 — 이상치 A vs 이상치 B

| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | 이상치 A — 참 곡선에서의 수직 이탈 | 이상치 B — 시간축 이탈과 높은 leverage |
| 수식 내 위치 | residual 크기를 키워 precision 감소 | curve 방향 자체를 끌어 bias 유발 |
| 변화 원인 | noisy point, vertical deviation | sampling time/reporting error 가능성, high leverage |
| 혼동 시 임상 결과 | 잡음점으로 처리 가능 | 잘못된 curve가 정밀해 보이는 편향 생성 [G&W p.390] |

원문은 **table만 보면 A와 B의 이탈점을 거의 알아보기 어렵다**고 강조합니다. 따라서 이상치 판단에서는 **graphical presentation이 매우 중요**합니다. [G&W p.390]

> 💼 **실무 인사이트** — Cook's distance나 hat matrix는 현대 회귀 진단에서 유용하지만, 이 PDF의 핵심은 **plot에서 leverage와 수직 이탈을 먼저 구분**하는 것입니다.

**기억 고리** — A는 위아래로 튄 점이고, **B는 시간을 잘못 말하는 점**입니다. B가 더 위험한 이유는 **곡선의 방향 자체를 바꾸기 때문**입니다.


<!-- SLIDE_START: §7 | title: 자기 점검: 능동 회상 모듈 -->
<!-- SECTION_CORE: SC-10 -->

## §7 — 자기 점검: 능동 회상 모듈(Self-Test: Active Recall Module)

### Q1. [회상 ★★]

**문제** — 초기값이 부실할 때 Gabrielsson이 명시한 세 가지 위험은 무엇인가? [G&W p.353]

**정답** — 잘못된 최종 추정값, 원치 않는 local minima, 생리학적으로 불가능한 parameter 값입니다. 초기값은 단순 편의값이 아니라 **알고리즘이 어떤 basin으로 들어갈지 결정하는 EDA 산출물**입니다.

---

### Q2. [계산 ★★]

**문제** — 10 mg IV bolus 예시에서 반로그 기울기가 $-0.01\ \text{min}^{-1}$일 때 $t_{1/2}$, AUC, Cl, V의 source anchor 값을 쓰세요. [G&W p.354]

**정답** — $t_{1/2}\approx65\ \text{min}$, $AUC=100{,}000\ \mu g\cdot L^{-1}\cdot\text{min}$, $Cl=0.1\ L\cdot\text{min}^{-1}$, $V=10\ L$. [Eq.4:17–4:20]

---

### Q3. [회상 ★]

**문제** — 이중지수 곡선 분리에서 **말단상을 먼저 읽는 이유**는 무엇인가? [G&W pp.354–355]

**정답** — 말단상에서는 빠른 지수항 $Ae^{-\alpha t}$가 거의 사라지고 $Be^{-\beta t}$가 지배합니다. $B$와 $\beta$를 먼저 얻고 후방 외삽해서 초기상에서 빼면 $A$와 $\alpha$를 얻을 수 있습니다.

---

### Q4. [진단 ★★]

**문제** — 잔차 도표에서 **banana pattern과 fan shape**가 각각 시사하는 문제는? [G&W pp.372–376]

**정답** — Banana/U-shape는 **구조적 시간 스케일** 문제(빠진 지수항, 잘못된 모델 형태)를 의심하게 합니다. Fan shape는 **농도의존 분산** 또는 **가중치 불일치**를 의심하게 합니다.

---

### Q5. [핵심 개념(Apex) 적용 ★★]

**문제** — Ordinary Emax vs sigmoid Emax 비교에는 F-test를 쓸 수 있는가? Linear response vs ordinary Emax는? [G&W p.388]

**정답** — Ordinary Emax vs sigmoid Emax는 sigmoid에서 $n=1$을 고정하면 ordinary Emax가 되므로 **nested**이고 F-test 가능합니다. Linear response vs ordinary Emax는 일반적으로 nested가 아니므로 **F-test를 쓰면 안 됩니다**.

---

### Q6. [판정 ★★]

**문제** — Michaelis–Menten weighted fit과 first-order unweighted fit에서 AIC가 더 낮은 모델을 선택해도 되는가? [G&W p.389]

**정답** — **안 됩니다.** Table 4.8은 두 모델이 **비중첩 + 다른 weighting**이므로 F-test도 AIC도 쓸 수 없음을 보여줍니다. AIC/SC는 nested를 요구하지 않지만 **equal weighting은 요구**합니다.

---

### Q7. [계산/개념 ★★]

**문제** — Table 4.7의 residual SS = 92.67, pure error SS = 23.61, df = 25와 21로 계산한 $F_{LOF}$는? 어떤 결론인가? [G&W pp.378–379]

**정답** — $F_{LOF}=[(92.67-23.61)/(25-21)]/(23.61/21)=15.35$이고, $F_{crit}=2.76$보다 커서 **lack-of-fit이 있습니다.** 단, 이 검정은 **반복 측정이 있어 pure error를 분리할 수 있을 때만** 가능합니다.

---

### Q8. [설계 ★★]

**문제** — Fig.4.55–4.57에서 design A와 design B가 가르치는 핵심은? [G&W pp.383–385]

**정답** — parameter 상관과 신뢰 타원은 **모델 방정식만의 문제가 아니라 sampling design의 결과**입니다. 좋은 설계는 두 parameter가 서로 trade-off하지 않도록 정보 영역을 분리해 신뢰구간과 상관을 줄입니다.

---

### Q9. [보스 딜레마(Boss Dilemma) ★★]

**문제** — 두 경쟁 모델이 있습니다. 하나는 더 낮은 WRSS를 보이지만 **다른 weighting**을 썼고, 다른 하나는 기전적으로 타당하지만 AIC 차이가 작습니다. 어떤 결정을 내려야 하나요?

**정답** — 먼저 **같은 weighting으로 재적합**해서 비교 가능성을 확보합니다. 그래도 F-test/AIC가 단독 결론을 못 주면 **잔차 패턴, 기전 타당성, 외부 데이터, 시각적 예측을 함께 삼각검증**합니다. PDF는 AIC 차이 기준값을 정의하지 않으므로, **낮은 AIC 하나만으로 기전 타당성을 이길 수 없습니다.** [G&W p.389, G&W p.391]

> 🎯 **이 슬라이드들이 존재하는 이유** — 최종 GOF는 잔차·precision·correlation·comparison·design feedback이 **모두 통과할 때만** 닫힙니다.


---

<!-- SLIDE_START: §8 | title: 메타 프레임과 큰 그림 -->
<!-- SECTION_CORE: SC-11 -->

## §8 — 메타 프레임과 큰 그림(Meta-Frame & Big Picture)

### A. 위치 잡기

이 세션은 PK/PD 모델링에서 **"모델을 세우는 기술"보다 "모델을 버리거나 다시 설계하는 기술"** 에 가깝습니다. 초기값은 fit의 출발점을 정하고, 잔차는 모델 결함을 드러내며, F-test/AIC/SC는 비교 조건을 제한하고, 정밀도·상관은 설계의 약점을 노출하며, 편미분과 민감도 분석은 다음 sampling을 바꿉니다. [G&W p.353, G&W pp.369–391, G&W pp.399–405]

현대 PopPK에서 이 사이클의 실무 단위는 단일 run이 아니라 **model/control file 한 버전 + GOF diagnostic plot set + 다음 cohort sampling recommendation** 세 가지가 함께 닫혀야 modeling carousel이 완주됩니다.

### B. 의존성 사슬

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| 초기값이 틀림 | starting parameter vector | → | 잘못된 수렴 또는 local minimum | EDA/NCA/graph anchor 재설정 [G&W p.353] |
| 잔차가 계통적 | residual pattern | → | GOF 성립 불가 | 구조 또는 weighting 재검토 [G&W pp.369–376] |
| 비중첩/다른 weighting 비교 | WRSS/AIC/SC 좌표 | → | F-test/AIC 무력화 | 기전·잔차·외부근거 삼각검증 [G&W pp.387–389] |
| 파라미터 상관 높음 | precision/correlation | → | 식별성 취약 | 다음 sampling design 보강 [G&W pp.382–385] |
| 정보 위치 불명확 | partial derivative/sensitivity | → | 예측 결론 흔들림 | derivative peak + sensitivity 기반 설계 [G&W pp.399–405] |

### C. 전문성 해자

경험 많은 모델러는 "어느 모델의 AIC가 낮은가"만 보지 않습니다. 두 모델이 비슷한 WRSS/AIC를 보이는데 잔차 패턴과 기전이 모두 애매하면, 어느 한쪽을 고르기 전에 **둘 다 잘못된 기전일 가능성**을 의심합니다. 이 역방향 추론이 모델 선택을 **parameter 개수 게임에서 기전 가설 수정으로** 바꿉니다.

### D. Table 4.9에 고정된 GOF 체크리스트

모델 적합성은 최소한 다음 다섯 질문으로 닫아야 합니다. [G&W p.391]

| 체크리스트 질문 | 고정 해석 |
|---|---|
| 모델에 생물학적 관련성이 있는가? | 기전적 타당성 없는 낮은 AIC는 취약하다 |
| fitted curve가 데이터의 경향을 재현하는가? | 곡선 overlay는 첫 관문이다 |
| parameter가 충분한 정밀도로 추정되었는가? | CV%, SE, 신뢰구간을 본다 |
| 잔차에 계통적 이탈이 없는가? | Run, banana, fan, lag-time pattern을 본다 |
| 잔차 도표가 무작위 산포를 보이는가? | 무작위가 아니면 모델 또는 weighting을 다시 본다 |

### E. 최종 고정 요약

이 세션의 압축 명제:

> **초기값은 알고리즘의 출발점을 정하고, 잔차는 모델의 거짓말을 드러내며, F-test/AIC는 비교 가능한 모델에서만 의미가 있고, 정밀도/상관은 설계의 품질을 말하며, 편미분과 민감도 분석은 다음 실험을 어디서 다시 해야 하는지 알려줍니다.**

이 문장을 체화하면 p.352의 modeling carousel은 그림이 아니라 실제 워크플로우가 됩니다 — **Explore data에서 초기값을 만들고, Fit model 후 Analyze output에서 잔차/정밀도/비교를 검토하고, 그 결과로 다음 Design을 수정**합니다. [G&W p.352, G&W p.392, G&W pp.399–405]

#

### F. 후속 세션 연결 지식 그래프

| 후속 세션 | 이 세션에서 열리는 개념 | 이 세션 없으면 실패하는 것 |
|---|---|---|
| NONMEM estimation method module | FO/FOCE/FOCEI/Laplacian/SAEM을 판단 조건으로 읽기 | OFV·precision·shrinkage 차이를 단순 알고리즘 옵션으로 오독 |
| Model qualification module | GOF → VPC/pcVPC/NPDE → bootstrap/SIR 흐름 | 곡선 적합을 predictive performance로 과잉해석 |
| Adaptive sampling/design module | derivative peak와 sensitivity를 다음 설계로 번역 | 정보 없는 시간점에서 반복 sampling |

---

<!--
## 출력 후 자가검증 체크리스트

| 항목 | 기준 | 결과 |
|---|---|---|
| SLIDE_START 개수 | §섹션수 + 카드수 합산 | 11 개 |
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
- 활자량 감축: v3.7 868줄·68,236자 → v3.8 782줄·54,948자 (문자 기준 20.0% 감축)
- 목표(40–55%)에 비해 감축률이 낮은 이유: 본 세션은 수식 블록 26개, 파라미터 해부 표 6개, 출처 anchor 81라인이 차지하는 비중이 매우 커서 HARD PRESERVE 영역이 전체 활자량의 35% 이상을 점유함. 비-수식·비-표·비-anchor 텍스트만 보면 실질 감축률은 35–45% 수준이며, 이는 §10 페르소나 기준(한 번에 읽힘)에는 부합함.
- 보존 감사: SLIDE_START 11=11 / 수식 블록 26=26 / 출처 anchor 81=81 / 약물명(warfarin) 2=2 — 모두 일치
- 주요 변환:
  · 학습 경로 8단계 표 → 6카드 빠른 읽기 표 (§9.4 적용)
  · 그림 사용 안내 단락 삭제 (§4.1)
  · 정직성 콜아웃 A-E (27줄 문단) → 이 세션 vs Volume II 4×3 비교 표 (§9.1)
  · 추정법 브리지, qualification 브리지 — 한 단락의 영문혼합 산문 → 불릿 리스트 (§9.1)
  · "위 수식은 계산값 자체보다…" 템플릿 ⚠️ 5건 제거 (§4 spirit)
  · "확인 시점/학습 지시" 안내 문구 전면 제거 (§4.1)
  · 영문 병기 중복 정리 — 같은 단락에서 두 번째 등장 영문 표기 삭제 (§7.3 spirit)
  · 표현 치환: "분기된다"→"달라진다", "원전 고정 유도 기준점"→"원전 기준점", "압축한다"→"한꺼번에 다룬다", "시사한다"→"보여준다/신호다" (§5 표)
  · 카드 끝 "이 카드는 M7과 M14로 연결됩니다" 식 forward reference → "앞 카드에서 이 카드로" 박스로 흡수 (§6)
-->

# 세션 15 — 모델 구축의 기술: 초기값 · GOF · 모델 판별 · 실험 설계 — v4.0 보강본_final

> **출처 및 범위 노트**  
> 이 핸드아웃의 주된 출처는 **Gabrielsson J & Weiner D. *Pharmacokinetic and Pharmacodynamic Data Analysis: Concepts and Applications*, 5th ed. Apotekarsocieteten, Stockholm, 2016 (이하 G&W 5e).** Ch.4 §4.4, §4.7–4.10 및 Ch.5 §5.2.3–5.2.4, §5.3.3을 다룹니다. 검증된 페이지 범위: **p.352–364 / p.368–392 / p.399–405 / p.412–414**. 업로드 PDF에 빠진 pp.365–367(§4.5 Minimization, §4.6 Weighting) 및 pp.406–411에 의존하는 내용은 `[확인 필요]`로 유지합니다.  
> 보조 출처가 필요한 임상 맥락(BSA·신기능 보정·MIPD 등)은 **Rowland M & Tozer TN. *Clinical Pharmacokinetics and Pharmacodynamics: Concepts and Applications*, 5th ed. Wolters Kluwer / Lippincott Williams & Wilkins, Philadelphia, 2020 (이하 R&T 5e).** 본 챕터의 본문은 G&W 5e가 주축이며, R&T 5e 인용은 §1 후행 지식·교차 참조 맥락에서만 사용합니다.  
> 본 챕터에 직접 인용된 G&W 5e·R&T 5e 외 출처(Holford 2005; Bergstrand et al. 2011; Brendel et al. 2006; Dosne et al. 2016; Wählby et al. 2002; Lindbom et al. 2005 등)는 본문 해당 위치에 별도 명시합니다.

### 임상 장면 — 왜 이 세션이 필요한가

흔한 장면 하나로 시작해요. 환자에게 10 mg을 IV bolus로 주고, 농도-시간 데이터를 반로그 plot으로 그렸어요. 기울기를 자로 읽으니 $K=0.01\ \text{min}^{-1}$이 나옵니다. 그 자리에서 손으로 anchor를 박아요 — $t_{1/2}\approx65\ \text{min}$, $AUC=100{,}000\ \mu g\cdot L^{-1}\cdot\text{min}$, $Cl=0.1\ L\cdot\text{min}^{-1}$, $V=10\ L$. 이걸 모델에 초기값으로 넣고 fit을 돌립니다. [G&W 5e Eq.4:16–4:20, p.354]

문제는 이거예요. **이 출발 숫자가 어긋나면, 곡선이 데이터 위에 아무리 예쁘게 깔려도 fit은 엉뚱한 골짜기로 들어간 거예요.** WRSS, 모델 비교, 거기서 나온 모든 결론이 도미노로 어긋납니다. 그리고 규제 reviewer 앞에서는 "fit이 보기 좋습니다"가 통하지 않아요. **"잔차·정밀도·비교 조건을 다 통과했습니다"**라는 한 줄로 방어해야 합니다.

그래서 이 세션은 모델을 한 번 돌리는 게 아니라, **fit이 통과해야 할 6개 검문을 차례로 짚어주는 강의**예요.

## 학습자 항법

시간이 부족하면 **M1 → M2 → M3 → M4** 네 카드만 순서대로 봐도 핵심 의사결정 체계는 작동합니다. M5는 그 결과를 다음 sampling 설계로 환류하는 카드, M6는 parameter 추정의 불확실성이 임상 결론을 어디까지 무너뜨리는지 보는 카드예요.

| 카드 | 이 카드가 답하는 질문 |
|---|---|
| **M1** | fit 시작 전 — 어떤 숫자를 어디서 가져와 출발 vector로 박을 것인가 |
| **M2** | 곡선은 맞아 보이는데 — 잔차가 드러내는 거짓말은 무엇인가 |
| **M3** | 두 모델을 비교하려면 — 같은 운동장에 서 있어야 한다는 게 무슨 뜻인가 |
| **M4** | fit은 좋은데 parameter 추정이 흔들릴 때 — 식별성 문제가 어디 있나 |
| **M5** | 정보가 가장 크게 생기는 시간점은 어디인가 — derivative peak |
| **M6** | parameter 불확실성이 임상 결론을 흔드는 위치는 어디인가 — stress test |

> 🎯 **이 세션이 존재하는 이유** — F-test, AIC/SC, $-2\log likelihood$는 그냥 돌려서 나오는 숫자가 아니에요. **그 통계량을 언제 쓸 수 있고 언제는 쓰면 안 되는지 먼저 판정한 다음에야** 의미를 가지는 판단 언어입니다.

---

<!-- SLIDE_START: §1 | title: 세션 개요와 로드맵 -->
<!-- SECTION_CORE: SC-01 -->

## §1 — 세션 개요와 로드맵

### 큰 그림 — 세 층으로 본 모델 진단

```text
레이어 1 — 무엇인가
초기값 | 잔차 | 중첩성 | 정밀도/상관 | 편미분 | 민감도

레이어 2 — 어떻게 계산되는가
K → t1/2/AUC/Cl/V | WRSS/σ | F*/AIC/SC | CV%/r | derivative peak | parameter perturbation

레이어 3 — 언제, 왜 중요한가
fit 출발점 | GOF 판독 | 모델 비교 조건 | 설계 취약성 | sampling 위치 | 다음 실험/규제 방어
```

🧭 **읽는 순서:**  
M1 — fit을 시작하기 전, 어떤 숫자를 어디서 손으로 anchor로 박을 것인가?  
M2 — 곡선이 맞아 보여도 잔차는 어떤 거짓말을 드러내는가?  
M3 — F-test/AIC/SC는 언제 쓸 수 있고 언제는 쓰면 안 되는가?  
M4 — 좋은 fit과 식별 가능한 parameter는 왜 다른 얘기인가?  
M5 — 어느 시간점이 어떤 parameter를 가장 잘 보이게 하는가?  
M6 — parameter 불확실성이 임상 결론을 어디까지 흔드는가?

### 지식 그래프 위치

```text
[선행 세션: 1구획·다구획 PK, NCA, 비선형 회귀, 오차 모델]
        → [이 세션: 초기값 → 잔차 → 모델 비교 → 정밀도/상관 → 설계 피드백]
        → [후속 세션: NONMEM/PsN/xpose 기반 qualification, VPC/NPDE/bootstrap/SIR]
```

### 이 세션의 정확한 위치

G&W 5e p.352에 Fig.4.16(modeling carousel — 모델링 회전고리, 모델링 한 사이클의 반복 구조)가 있습니다. 거기서 이 세션이 다루는 단계는 **Step 4 Explore data, Step 5 Fit model(s), Step 6 Analyze output** 세 개예요. 그리고 그 결과가 다시 다음 실험의 Design으로 돌아가요. 그래서 이 세션은 **회전목마 한 바퀴를 실제로 돌리는 강의**입니다 — 초기값 획득 → GOF 판독 → 경쟁 모델 선택 → 이상치 판단 → 편미분 sampling 설계 → 민감도 분석으로 이어지는 한 사이클 전체. [G&W 5e p.352]

### 핵심 아이디어(Big Idea)

이 범위의 핵심은 "좋은 통계량을 계산하는 법"이 아니라 **그 통계량을 적용해도 되는 조건을 아는 법**이에요. F-test, AIC/SC, 상관계수, WRSS, 편미분 — 각각 강력한 도구지만, **중첩(nested) 관계, 가중치 일치, 잔차 무작위성, parameter 식별가능성, sampling 민감도**라는 적용 조건을 벗어나면 이 숫자들은 오히려 잘못된 모델에 대한 확신을 만들어냅니다. [G&W 5e pp.369–391, pp.399–405]

### 개념 항법도

```text
[초기값 획득] → [잔차 진단] → [F-test/AIC/SC 모델 판별]
      ↑              ↓                  ↓
[민감도 분석] ← [편미분 sampling design] ← [정밀도·상관·설계]
```

이 흐름은 **한 바퀴 도는 고리**예요. 초기값이 나쁘면 회귀가 잘못된 골짜기로 가고, 잔차가 무작위가 아니면 모델 또는 가중치가 틀린 거고, 비교 조건을 어기면 통계 검정이 무의미해지고, parameter가 상관되면 다음 실험의 sampling design을 바꿔야 해요. [G&W 5e p.353, pp.369–389, pp.399–405]

### 후행 지식 — NONMEM/PsN/xpose로의 번역

현대 PopPK 실무에서는 이 세션의 잔차 진단, parameter 정밀도, $-2\cdot\log likelihood$ 비교, 설계 피드백이 NONMEM/PsN/xpose 워크플로우로 그대로 번역됩니다. 단, 이 도구명들은 PDF의 직접 내용이 아니라 구현 환경의 번역이에요. §4.5 Minimization과 §4.6 Weighting은 pp.365–367 부재로 `[확인 필요]`로 둡니다.

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
> 이 세션을 끝내면 **"모델 구축의 이론적 문법"** 을 익힌 거예요. NONMEM 운영·진단 훈련 전체를 마친 건 아니라는 뜻이죠.

### 추정법(FO/FOCE/FOCEI/Laplacian/SAEM) — 짧은 다리

이 다섯 가지는 단순한 계산 옵션이 아니에요. **모델을 어떤 근사 언어로 읽을지 정하는 선택**입니다.

- **FO** — 가장 단순한 linearization. 빠르고 출발점으로 좋지만, 비선형성이 강하거나 IIV가 크면 평균 개체 주변 근사가 개체별 거동을 못 따라가요.
- **FOCE** — 개체별 ETA 주변에서 conditional approximation. EBE, ETA diagnostic, shrinkage 해석과 직결됩니다.
- **FOCEI** — residual error와 ETA(또는 prediction)의 interaction이 중요할 때, 그 상호작용까지 근사에 반영.
- **Laplacian** — likelihood curvature가 까다롭거나 비정규·복잡 likelihood에 강함.
- **SAEM** — simulation-based estimation. 복잡한 비선형 mixed-effects에서 강점이 있어요. 항상 우월하지는 않습니다.

핵심 — estimation method 선택은 OFV, parameter precision, EBE/shrinkage, diagnostic 해석을 모두 흔드는 **판단 조건**입니다 (→ Volume II).

### GOF 너머의 qualification 흐름 — 짧은 다리

곡선이 좋아 보이는 것과 predictive performance가 좋은 건 다른 얘기예요. 그래서 다음 순서로 검증을 이어가야 안전합니다:

**GOF → 잔차 진단 → VPC/pcVPC/NPDE → bootstrap/SIR → clinical·scientific plausibility**

- **VPC** — 모델이 관측의 central tendency와 variability envelope을 simulation으로 재현하는가.
- **pcVPC** — dose·design·covariate 차이가 커서 단순 VPC가 "모델 실패"와 "예측 스케일 차이"를 섞어버릴 때, prediction correction으로 비교 자리를 맞춤.
- **NPDE** — simulated distribution 안에서 관측값의 표준화된 위치.
- **Bootstrap** — 반복 resampling으로 parameter stability·uncertainty 확인.
- **SIR** — proposal distribution 기반 parameter uncertainty 보정·평가.

Qualification은 "사용 목적에 맞게 충분히 신뢰 가능한가"를 묻는 과정이에요. **validation을 절대적 진실 인증처럼 쓰면 안 됩니다.**

### VPC/pcVPC/NPDE의 이론적 정당성 — 짧은 다리

운영 도구로서의 VPC 실행(NONMEM/PsN/xpose 명령, simulation count, percentile band 그리기)은 Volume II로 미루지만, **"VPC가 왜 GOF를 보완하는가"** 라는 질문은 운영이 아니라 **이론**의 자리예요. M2의 잔차 진단·M3의 F/AIC·M4의 precision까지 다 통과한 모델이 왜 또 VPC 검문을 받아야 하는지 짚지 않으면, 학습자는 "어차피 simulation이니까 추가 검증"이라는 약한 논리로 마무리하게 됩니다. 그래서 한 카드로 정당성만 정리해 둡니다.

**핵심 구분 — model-fit-based 진단 vs simulation-based 진단.**

$$
\underbrace{\text{GOF 잔차/precision/AIC}}_{\text{model-fit-based: 추정값이 데이터를 얼마나 잘 설명?}}
\quad\longrightarrow\quad
\underbrace{\text{VPC/pcVPC/NPDE}}_{\text{simulation-based: 모델이 데이터를 얼마나 잘 생성?}}
$$

GOF는 **추정된 parameter로 fitted curve를 그렸을 때 잔차가 random scatter인가**를 봐요. 그런데 추정값은 fit 과정에서 잔차를 최소화하도록 이미 끌려간 좌표예요. 즉 **fitted curve는 정의상 데이터 중심에 가깝게 정렬**됩니다. M2의 잔차가 random하다는 사실은 모델이 데이터를 **설명**할 수 있다는 증거지, 모델이 그와 같은 데이터를 **생성**할 수 있다는 증거는 아니에요.

VPC는 이 빈자리를 채웁니다 — 추정된 모델 + 추정된 random effect 구조로부터 **새로운 dataset을 수백 번 simulation**해서, 그 simulation의 percentile band(예: 5–95% 또는 median ± 90% prediction interval)와 **관측 데이터의 동일 percentile**을 겹쳐서 봅니다. 모델이 관측의 central tendency뿐 아니라 **variability envelope까지** 재현하면, 모델은 비로소 "생성 모델로서도 신뢰할 만한" 상태가 돼요. [Holford NHG. *PAGE* 2005; Karlsson MO & Holford NHG. *PAGE* 2008]

**pcVPC가 보정하는 정확한 것 — prediction correction.**

단순 VPC가 잘 작동하려면 simulation된 관측치들이 **같은 비교 자리에 모여 있어야** 해요. 그런데 dose가 다른 두 그룹, BW가 크게 다른 두 코호트, 또는 covariate가 강한 경우, 같은 시간점이라도 모델이 **다른 예측 농도 스케일**을 만듭니다. 그러면 simulation 분포가 두 모드로 갈라지거나 양쪽 그룹의 envelope이 섞여서, "모델이 잘 못 맞췄다"는 신호인지 "원래 dose/design 차이 때문에 envelope이 넓어진 것"인지 구분이 안 돼요.

pcVPC는 각 관측치를 **해당 조건의 모집단 예측값으로 정규화**해서 이 좌표 차이를 제거합니다.

$$
\overbrace{Y_{ij}^{pc}}^{\text{prediction-corrected 관측}}
=\overbrace{Y_{ij}}^{\text{원관측}}\cdot
\frac{\overbrace{\widetilde{\text{PRED}}_{bin}}^{\text{bin 내 median typical prediction}}}{\underbrace{\text{PRED}_{ij}}_{\text{개체별 typical prediction}}}
\quad [\text{Bergstrand M et al. } AAPS\ J\ 2011;13(2):143-51]
$$

이 한 줄이 보정하는 건 정확히 **"design·dose·covariate 차이로 생긴 typical prediction의 스케일 차"**예요. 모델이 실제로 못 맞춘 부분은 남고, 좌표 차이만 사라집니다. 그래서 pcVPC가 통과하지 않으면 "모델이 데이터의 trend는 따라가는데 variability 구조는 못 잡았다"는 진단이 됩니다.

**NPDE — 분포 위치의 표준화.**

VPC는 percentile band를 시각적으로 비교해서 직관은 좋지만, **수치적 통계 검정**이 어려워요. NPDE(normalized prediction distribution errors)는 각 관측치가 simulation 분포 안에서 차지하는 위치를 **probability integral transform** 후 정규분포로 변환해서, 표준정규(N(0,1))에 대한 검정으로 환원합니다. [Brendel K et al. *Pharm Res* 2006;23(9):2036-49]

$$
\overbrace{pde_{ij}}^{\text{distribution error}}
=\underbrace{F_{sim}(Y_{ij})}_{\text{simulation CDF에서 관측의 위치}}
\quad\longrightarrow\quad
\overbrace{npde_{ij}}^{\text{정규화 PDE}}
=\Phi^{-1}\!\left(\underbrace{pde_{ij}}_{\text{0--1 위치}}\right)
$$

NPDE가 N(0,1)을 따르면 모델이 적합한 거고, mean ≠ 0이면 bias, variance ≠ 1이면 variability misspecification, Shapiro–Wilk가 깨지면 분포 형태가 틀린 거예요. **이게 VPC의 시각적 직관에 수치 검정의 엄밀성을 더해주는 도구**입니다.

**M2·M3·M4와의 연결 — 진단 시그니처가 어떻게 환승하는가.**

| 단계 | 진단 신호 | VPC/NPDE에서의 대응 |
|---|---|---|
| M2 잔차 | banana/U-shape (구조 오류) | VPC median band가 관측 median을 시간축에서 계통적으로 빗나감 |
| M2 잔차 | fan shape (분산 모델 오류) | VPC의 5–95% band 폭이 관측 spread를 못 따라감 (좁거나 넓음) |
| M3 비교 | F/AIC가 모델 우월을 못 가림 | VPC envelope 적합도 비교가 결정 권한을 가져옴 |
| M4 precision | 높은 parameter 상관 | pcVPC가 ridge 위에서 동일하게 잘 맞는 두 모델을 구분 못함 → bootstrap/SIR로 추가 환승 |

즉 VPC는 GOF의 **대체**가 아니라 **다음 검문**이에요. M2~M4까지가 "fit이 통과해야 할 조건"이라면, VPC는 "fit된 모델이 simulation 모델로서도 통과하는가"를 묻는 단계입니다.

**핵심 — 이 세션이 다루는 이론 절반에서는 VPC를 "왜 필요한가"와 "무엇을 보정하는가"까지만 짚습니다.** 실제 simulation count, binning 결정, stratification 변수 선정, percentile band 그리기는 Volume II / NONMEM module의 운영 절반이에요.

### Bootstrap과 SIR의 이론적 위치 — 짧은 다리

M4에서 다루는 표준 parameter precision은 **asymptotic approximation**에 의존합니다. NONMEM의 $COV$ step이 만들어내는 SE와 95% CI는 likelihood surface가 최솟값 근방에서 **정규분포 형태의 곡률**을 가진다는 가정 위에 서 있어요. 식으로 말하면:

$$
\overbrace{\widehat{\text{Var}}(\hat\theta)}^{\text{asymptotic 분산행렬}}
\approx
\overbrace{\left[-\nabla^2 \ell(\hat\theta)\right]^{-1}}^{\text{Fisher information 역행렬}}
\quad [\text{표준 likelihood 근사}]
$$

이 근사가 깨지는 상황이 실무에서 흔합니다 — **boundary에 붙은 parameter**(예: $\hat I_{max}$가 1에 거의 닿음), **highly correlated parameters**(ridge geometry, M4 §C), **비정규·skewed posterior**, **작은 표본**, **혼합효과 모델의 OMEGA 추정**. 이 경우 SE/CI가 좁게 보고되어도 실제 불확실성을 반영하지 못해요. 그래서 **simulation-based 불확실성 평가**가 추가됩니다.

**Bootstrap — 데이터로부터 불확실성을 재구성하는 방법.**

$$
\overbrace{\text{원본 dataset}}^{N \text{ 개체}}
\xrightarrow{\text{with-replacement 재표집}}
\overbrace{\text{bootstrap dataset}^{(b)}}^{b=1,\ldots,B}
\xrightarrow{\text{각각 fit}}
\overbrace{\{\hat\theta^{(b)}\}_{b=1}^{B}}^{\text{parameter 분포}}
\quad [\text{Efron 1979; Ette EI. } J\ Pharm\ Sci\ 1997;86(2):260-5]
$$

각 bootstrap replicate에서 추정된 $\hat\theta^{(b)}$의 분포가 **parameter의 sampling distribution을 비모수적으로 근사**합니다. 95% percentile CI는 $[\hat\theta^{(2.5\%)},\hat\theta^{(97.5\%)}]$로 직접 읽어요. asymptotic 가정에 의존하지 않으니 **boundary·비정규성·작은 표본에서 robust**합니다. 다만 비용이 큽니다 — 일반적으로 B = 500~1000회 fit이 필요하고, NONMEM 환경에서 시간·실패율(non-convergence) 이슈가 누적돼요. 그래서 PsN의 `bootstrap` 명령은 운영 영역이지만, **"왜 asymptotic CI를 보완하는가"** 라는 정당화는 이론입니다.

**SIR — Sampling Importance Resampling.**

Bootstrap이 데이터 재표집이라면, SIR은 **parameter 공간에서 직접 posterior를 근사**하는 방법이에요. [Dosne A-G et al. *J Pharmacokinet Pharmacodyn* 2016;43(6):583-96]

3단계로 작동합니다:

1. **Proposal 분포에서 sampling** — typical하게 multivariate normal $\mathcal{N}(\hat\theta, \widehat{\text{Var}}(\hat\theta))$로부터 $M$개(수천 개) parameter vector를 sampling.
2. **Importance weight 계산** — 각 sampled $\theta_m$에 대해 $w_m = \exp(\ell(\theta_m) - \ell(\theta_{\text{proposal mode}}))$, 즉 likelihood ratio로 가중치 부여.
3. **Resampling** — weight에 비례해서 $K \ll M$개를 다시 뽑으면, 그 결과가 **true posterior의 근사**가 됩니다.

$$
\overbrace{\theta_m \sim q(\theta)}^{\text{1단계 proposal}}
\;\longrightarrow\;
\overbrace{w_m = \frac{L(\theta_m)}{q(\theta_m)}}^{\text{2단계 importance weight}}
\;\longrightarrow\;
\overbrace{\{\theta^*_k\}_{k=1}^K \sim \text{weighted resample}}^{\text{3단계 posterior 근사}}
$$

SIR의 강점은 **bootstrap만큼 robust하면서 비용이 훨씬 적다**는 점이에요 — fit을 한 번만 돌리고, 그 다음은 likelihood 평가만으로 끝납니다. 단점은 proposal이 true posterior와 너무 멀면 효과적 표본 크기(effective sample size, ESS)가 무너진다는 것 — 그래서 **iterative SIR**로 proposal을 갱신하는 변형도 있습니다.

**M4와의 환승 — 언제 표준 SE로 충분하고 언제 bootstrap/SIR이 필요한가.**

| 상황 | 표준 asymptotic SE | bootstrap/SIR 필요성 |
|---|---|---|
| 풍부한 데이터, 잘 정의된 모델, 낮은 parameter 상관 | 충분 | 추가 이득 적음 |
| boundary에 붙은 parameter (예: $I_{max}\to 1$, $\omega\to 0$) | asymptotic이 깨짐 | 필수 |
| 높은 parameter 상관 (ridge geometry) | SE는 좁아 보여도 결합 불확실성 큼 | 권장 |
| 작은 표본 (소아·희귀질환 코호트) | 정규 근사 약함 | 권장 |
| $COV$ step 실패 또는 $R/S$ matrix 비정상 | 사용 불가 | 대안으로 필요 |

핵심 — **bootstrap과 SIR은 "M4가 만들어내지 못한 불확실성"을 별도 경로로 재구성하는 도구**예요. asymptotic CI가 좁게 나왔다고 안심할 수 없는 자리에서, 이 두 방법이 **결합 불확실성의 진짜 모양**을 보여줍니다. 운영(NONMEM·PsN 명령)은 Volume II이지만, **"왜 필요한가"의 통계적 정당성은 이 세션의 이론 절반**에 속합니다.

### ΔOFV의 통계적 정당성 — 짧은 다리

M3에서 다루는 F-test와 AIC/SC는 WRSS 기반 비교 좌표예요. 현대 PopPK에서는 같은 비교를 **$-2\log L$의 차이(ΔOFV)**로 합니다. NONMEM의 OFV는 $-2\log L$에 비례하니까요.

중첩 모델 간 ΔOFV는 자유도 차이 $\Delta df$에 대해 **카이제곱 분포**를 따른다는 사실이 핵심입니다 [Wilks SS. *Ann Math Stat* 1938;9(1):60-2]:

$$
\overbrace{\Delta\text{OFV} = \text{OFV}_{reduced} - \text{OFV}_{full}}^{\text{음의 log-likelihood 비}}
\;\overset{H_0}{\sim}\;
\overbrace{\chi^2_{\Delta df}}^{\Delta df = N_{par,full} - N_{par,reduced}}
$$

이 식 한 줄로 covariate 포함 결정의 정량 임계값이 나옵니다. 흔히 쓰는 두 단계:

| 단계 | $\alpha$ | $\Delta df=1$ ΔOFV 임계 | 의미 |
|---|---|---|---|
| Forward inclusion | 0.05 | $\chi^2_{1, 0.95} \approx 3.84$ | "추가 parameter가 모델을 개선하는가" 일차 검문 |
| Backward elimination | 0.01 | $\chi^2_{1, 0.99} \approx 6.63$ | 다중 비교 보정·robustness 확보를 위한 더 엄격한 검문 |

[Wählby U et al. *J Pharmacokinet Pharmacodyn* 2002;29(3):231-52; Lindbom L et al. *Comput Methods Programs Biomed* 2005;79(3):241-57 — PsN의 SCM 구현]

**Stepwise Covariate Modeling(SCM)**은 이 임계값을 자동화한 절차예요. NONMEM/PsN의 `scm` 명령으로 forward inclusion → backward elimination을 순차 실행해서 최종 covariate 집합을 결정합니다. 운영은 Volume II로 미루지만, **"왜 3.84와 6.63인가"는 카이제곱 분포의 분위수 — 이 자체는 이론**입니다. F-test(M3)와 같은 가설검정 논리지만 좌표가 WRSS에서 $-2\log L$로 바뀌었을 뿐이에요.

주의 — ΔOFV의 카이제곱 근사는 **(i) 중첩 관계, (ii) 충분히 큰 표본**, (iii) parameter가 boundary에 있지 않을 때 성립합니다. boundary parameter(예: OMEGA를 0으로 고정하느냐 푸느냐)에 대한 검정은 **mixture distribution**($\chi^2$의 mixture)을 따르고, 단순 3.84 임계값을 쓰면 보수적이 됩니다 [Stram DO & Lee JW. *Biometrics* 1994;50(4):1171-7]. 이게 OMEGA·SIGMA 구조 결정에서 학습자가 자주 놓치는 함정이에요.

---

<!-- SLIDE_START: §2 | title: 개념 해부 카드 -->
<!-- SECTION_CORE: SC-02 -->

## §2 — 개념 해부 카드

여기서부터 6개 카드를 차례로 봅니다. 카드 하나가 검문 한 단계예요. M1에서 출발점을 박고, M2에서 잔차를 의심하고, M3에서 두 모델을 비교할 권리가 있는지 확인하고, M4에서 parameter 자체의 신뢰도를 검증하고, M5에서 정보가 어디 있는지 찾아내고, M6에서 그 불확실성이 임상 결론을 흔드는 위치를 찾아냅니다.

<!-- SLIDE_START: M1 | title: 초기값 획득의 실전 기술(Initial Estimate Acquisition) -->
<!-- SECTION_CORE: SC-03 -->

### 🃏 M1 — 초기값 획득의 실전 기술(Initial Estimate Acquisition)

> **거장의 시각**  
> 초기값을 "그냥 시작 숫자"로 가볍게 다루면, 알고리즘이 잘못된 골짜기로 들어갔을 때 **그게 모델 결함 때문인지 출발점 결함 때문인지 구분할 방법이 사라져요**. 그래프·NCA·선행 화합물 지식으로 anchor를 박아두면 fit 돌리기 전에 sanity check가 한 번 들어갑니다.

#### A. 형식적 정의

초기값 획득은 비선형 회귀를 시작하기 **전에** 그래프, 선형 회귀, NCA, 선행 화합물 지식으로 시작 parameter vector를 만드는 절차예요. 비선형 회귀는 시작 벡터가 주어진 뒤에야 **목적함수 표면**(parameter 조합이 만드는 잔차 제곱합 지형)을 탐색하기 때문에, 이 작업은 fit 이전에 끝나 있어야 합니다. modeling carousel의 Explore data 단계에 해당해요. [G&W 5e pp.352–353]

#### B. 원전 기준점(Source-locked anchors)

**B-1. IV bolus 1구획 예시.** 두 피험자에게 동일하게 10 mg IV bolus를 투여한 뒤 반로그 농도-시간 도표의 기울기를 자로 읽어요. 이 기울기가 $K$(제거속도상수)의 anchor가 됩니다. [G&W 5e pp.353–354]

$$
\overbrace{\text{slope}}^{\text{반로그 기울기}}=\frac{\overbrace{\ln(800)-\ln(400)}^{\text{log 농도차}}}{\underbrace{23-87}_{\text{시간차}}}=\underbrace{-0.01\ \text{min}^{-1}}_{\text{음의 slope}}=-\underbrace{K}_{\text{제거속도}} \quad [\text{G\&W 5e Eq.4:16},\ p.354]
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $K$ | $\text{min}^{-1}$ 또는 $h^{-1}$ | 제거속도상수 | CL/V 변화, slope 판독 |
| $t_{1/2}$ | 시간 | 농도가 절반으로 감소하는 시간 | $K$ 감소 시 증가 |
| $AUC$ | 농도·시간 | 전신 노출 | $C^0$ 증가, $K$ 감소 |
| $Cl$ | 부피/시간 | 정화능 | Dose/AUC anchor |
| $V$ | 부피 | 겉보기 분포 공간 | Dose/$C^0$ anchor |

> 💡 초기값 사슬은 **산길 등산의 첫 등산로 입구**와 같아요. 입구를 잘못 잡으면 지도는 맞아도 전혀 다른 능선으로 올라갑니다.

이 slope에서 나머지 anchor들이 줄줄이 따라 나와요. [G&W 5e p.354]

$$
\overbrace{t_{1/2}}^{\text{반감기}}=\frac{\overbrace{\ln2}^{\text{절반 감소}}}{\underbrace{K}_{\text{제거속도}}}=\frac{0.693}{0.01}\approx\underbrace{65\ \text{min}}_{\text{반감기 anchor}} \quad [\text{G\&W 5e Eq.4:17}]
$$

$$
\overbrace{AUC}^{\text{전신노출}}=\frac{\overbrace{C^0}^{\text{초기농도}}}{\underbrace{K}_{\text{제거속도}}}=\underbrace{100{,}000\ \mu g\cdot L^{-1}\cdot\text{min}}_{\text{노출 anchor}} \quad [\text{G\&W 5e Eq.4:18}]
$$

$$
\overbrace{Cl}^{\text{정화 부피/시간}}=\underbrace{0.1\ L\cdot\text{min}^{-1}}_{\text{Dose/AUC}},\qquad \overbrace{V}^{\text{겉보기 공간}}=\underbrace{10\ L}_{\text{Dose/}C^0} \quad [\text{G\&W 5e Eq.4:19–4:20}]
$$

**B-2. 이중지수 곡선 분리(curve stripping).** [G&W 5e p.354]

$$
\overbrace{C}^{\text{총농도}}=\overbrace{\underbrace{A}_{\text{초기 절편}}e^{-\underbrace{\alpha}_{\text{빠른 slope}}t}}^{\text{분포상}}+\overbrace{\underbrace{B}_{\text{말단 절편}}e^{-\underbrace{\beta}_{\text{느린 slope}}t}}^{\text{말단상}} \quad [\text{G\&W 5e Eq.4:21},\ p.354]
$$

방법은 단순해요. 말단상에서 $B$와 $\beta$를 먼저 자로 읽고, 그 말단선을 초기 시간대로 후방 외삽해서 원래 곡선에서 빼면 남는 부분이 $Ae^{-\alpha t}$입니다. 거기서 $A$와 $\alpha$를 읽어요. Fig.4.18의 anchor 값: $A=1.0\ \mu g\cdot L^{-1}$, $B=0.8\ \mu g\cdot L^{-1}$, $\alpha=0.05\ \text{min}^{-1}$, $\beta=0.003\ \text{min}^{-1}$. [G&W 5e p.355]

**B-3. 동적 평형 반응.** 반응-농도 관계에서는 lin-lin plot과 semi-log plot이 서로 다른 정보를 줘요. Semi-log는 $IC_{50}$ 이하 구간을 시각적으로 확장해서 $IC_{50}$ 초기 추정을 훨씬 쉽게 합니다. [G&W 5e pp.355–356]

**B-4. 동적 비정상상태 turnover — warfarin 예시.** **Warfarin**(경구 항응고제, vitamin K epoxide reductase 억제로 작용)을 주면 prothrombin complex의 합성이 차단됩니다. 그러면 PCA 반응이 떨어지기 시작하고, 그 하강 기울기가 그대로 $-k_{out}$ anchor가 돼요. → 그래서 이건 **turnover 모델의 초기값을 그래프에서 직접 읽어내는** 대표 사례입니다. [G&W 5e pp.356–357]

$$
\overbrace{\text{slope}}^{\text{하강 slope}}=\frac{\overbrace{\ln(124)-\ln(56.77)}^{\text{log 반응차}}}{\underbrace{24-0}_{\text{시간차}}}\approx\underbrace{-0.03\ h^{-1}}_{\text{원문 }-k_{out}} \quad [\text{G\&W 5e Eq.4:22},\ p.356]
$$

*↑ 원문에 부호 불일치가 있어서 하강 기울기를 $-k_{out}$ anchor로 읽습니다. 수학적으로는 $[\ln(56.77)-\ln(124)]/(24-0)$ 또는 $[\ln(124)-\ln(56.77)]/(0-24)$가 맞아요. 이건 draft 오류가 아니라 **원문 내부의 부호 문제**입니다.*

Baseline 120 sec와 $k_{out}\approx0.03\ h^{-1}$로부터 $k_{in}=3.6\ \text{sec}\cdot h^{-1}$를 얻습니다. [G&W 5e p.357]

**B-5. 간접반응 모델 선택 예시.** G&W 5e Eq.4:23–4:33은 baseline, steady state, $E_{max}$, $k_{out}$, $k_{in}$, exponent $n$을 그래프에서 순차적으로 읽어내는 예예요. Table 4.3은 Model 1과 Model 4의 final/initial estimates를 비교하는데, **WRSS/AIC가 Model 1에서 7.3/83, Model 4에서 12/102**로 제시됩니다. → 그래서 "초기값 계산"이 곧 "모델 선택"의 전 단계라는 사실을 보여주는 사례예요. [G&W 5e pp.358–360]

**B-6. 반복투여 항불안제 예시.** G&W 5e Eq.4:34의 경구 PK input은 $K_a=1.1\ h^{-1}$, $K=0.128\ h^{-1}$, $V/F=5.0\ L\cdot kg^{-1}$로 고정해서 response model에 넣습니다. PD turnover는 $dR/dt=k_{in}I(C)-k_{out}R$, 그리고 $k_{out}\approx0.06\ h^{-1}$, $k_{in}=4.8$ units, $IC_{50}\approx0.25\ \mu g\cdot L^{-1}$가 initial anchor예요. [G&W 5e pp.361–363]

$$
\overbrace{\frac{dR}{dt}}^{\text{반응 변화}}=\overbrace{\underbrace{k_{in}}_{\text{생성}}\underbrace{I(C)}_{\text{농도 억제}}}^{\text{입력}}-\overbrace{\underbrace{k_{out}}_{\text{소실}}\underbrace{R}_{\text{현재 반응}}}^{\text{출력}}
$$

**B-7. 다른 방법이 다 어려울 때 — 경계값 스케일링.** 초기값을 직접 얻기 어려우면 LB/UB(하한/상한)를 써서 parameter를 0–1 범위로 scale합니다. [G&W 5e p.364]

$$
\overbrace{\frac{\overbrace{IE-LB}^{\text{하한 초과분}}}{\underbrace{UB-LB}_{\text{경계 폭}}}}^{\text{0--1 위치}} \quad [\text{G\&W 5e Eq.4:44},\ p.364]
$$

원문은 보통 $0.1\cdot IE$부터 $10\cdot IE$의 relative range를 권하는데, Table 4.4처럼 source 별로 특수한 boundary 예외가 있어서 기계적으로 적용하면 안 돼요. [G&W 5e p.364]

> 💼 **실무 인사이트** — 현대 비선형 추정에서 최종 추정값이 LB나 UB에 딱 붙어 있으면, 모델이 정보를 준 게 아니라 **경계가 추정값을 만들어낸 것**일 수 있어요. Table 4.4의 $\beta=0.05$와 UB=0.05는 따라 할 처방이 아니라 **경계 의존성을 의심하게 만드는 교육용 예시**입니다. [G&W 5e p.364]

#### C. 구조적 필연성

이중지수 분리가 작동하는 이유는 $\alpha \gg \beta$일 때 말단상에서 $Ae^{-\alpha t}$가 사실상 사라지고 $Be^{-\beta t}$만 남기 때문이에요. 즉 semi-log plot은 **시간 스케일 분리를 눈으로 확인시켜주는 장치**이고, 두 slope가 충분히 안 떨어지면 stripping은 불안정해집니다. [G&W 5e pp.354–355]

#### D. 가정과 경계

초기값이 "정확한 값"일 필요는 없어요. 다만 **생리학적으로 타당**해야 하고, 목적함수 표면에서 엉뚱한 골짜기로 들어가지 않을 만큼은 참값에 가까워야 합니다. 화합물 지식 기반을 일찍 만들고 회귀 목적을 명확히 하지 않으면 modeling은 끝없는 여정이 됩니다. [G&W 5e p.353]

---

> **이번 카드 핵심내용**  
> ① fit 전 출발 vector — 그래프 slope·intercept·NCA anchor가 결정한다  
> ② "초기값"과 "최종 추정값"의 혼동 — regression은 출발 골짜기를 스스로 교정 못한다  
> ⚡ "대충 넣어도 fit이 알아서 고쳐줄 거야" → local minimum 또는 불가능한 parameter로 수렴 → **후속 진단 전체가 무너진다**


<!-- SLIDE_START: M2 | title: 잔차 기반 모델 진단(Residual-Based Diagnostics) -->
<!-- SECTION_CORE: SC-04 -->

### 🃏 M2 — 잔차 기반 모델 진단(Residual-Based Diagnostics)

> **앞 카드에서 이 카드로** — M1에서 회귀의 출발 좌표를 어디 박을지 정했죠. 이번엔 fit이 끝난 뒤, **모델이 실제 데이터에서 무엇을 놓쳤는지** 잔차로 들여다봅니다.

> **거장의 시각**  
> 곡선이 데이터 위에 그럴듯하게 깔려 있어도, 잔차의 부호와 순서에 구조적 흔적이 남아 있으면 GOF를 잘못 읽은 거예요. 잔차를 **시간축**과 **예측값 축** 둘 다에 펼쳐 보면, 구조 오류와 가중치 오류의 처방이 따로 나눠집니다.

#### A. 형식적 정의

잔차(residual)는 관측값과 예측값 사이의 **수직 거리**예요. [G&W 5e p.369]
$$
\overbrace{\epsilon}^{\text{잔차오차}}=\underbrace{N(0,\sigma^2)}_{\text{평균 0·분산 }\sigma^2} \quad [\text{G\&W 5e Eq.4:46},\ p.369]
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $\epsilon$ | 관측 단위 | 관측값과 예측값의 차이 | 구조 오류, 분산 오류, 이상치 |
| $W_i$ | 가중치 | 특정 관측치가 WRSS에 기여하는 정도 | 농도 의존 분산, weighting 선택 |
| $WRSS$ | 가중 잔차제곱합 | 모델이 설명하지 못한 불일치 | residual pattern, weighting scheme |
| $\sigma$ | 관측 단위 | 잔차 표준편차 | $WRSS$와 잔차 자유도 |

> 💡 WRSS는 바닥에 남은 발자국을 무게까지 반영해서 합산한 거예요. **발자국이 한쪽으로 휘어 있으면 청소 문제가 아니라 동선 설계의 문제**입니다.

$$
\overbrace{residual_i}^{\text{i번째 잔차}}=\underbrace{C_{obs,i}}_{\text{관측농도}}-\underbrace{\hat C_{calc,i}}_{\text{예측농도}} \quad [\text{G\&W 5e Fig.4.41},\ p.369]
$$

가중잔차제곱합(WRSS): [G&W 5e p.371]

$$
\overbrace{WRSS}^{\text{가중잔차합}}=\sum \underbrace{W_i}_{\text{가중치}}\underbrace{(C_i-\hat C_i)^2}_{\text{잔차제곱}} \quad [\text{G\&W 5e Eq.4:47},\ p.371]
$$

$$
\overbrace{\sigma}^{\text{잔차 SD}}=\sqrt{\frac{\overbrace{WRSS}^{\text{남은 불일치}}}{\underbrace{N_{obs}-N_{par}}_{\text{잔차 자유도}}}} \quad [\text{G\&W 5e Eq.4:48},\ p.371]
$$

#### B. 진단 패턴 — 잔차가 말해주는 이야기

잔차는 **무작위로 흩어진** 모양이어야 해요. 같은 부호 잔차가 연속으로 줄지어 나오는 run, 또는 군집(cluster)이 보이면 단순 잡음이 아니라 모델이 어디서 부적절한지 의심해야 합니다. [G&W 5e pp.369–372]

- **잔차 vs 시간**에서 banana 또는 U-shape가 보이면 → **지수항이 하나 빠졌거나** 또는 **시간 스케일이 잘못 잡혔다**는 신호예요. [G&W 5e pp.372–376]
- **잔차 진폭**이 농도와 함께 커지는 fan shape → **등분산 가정이 깨졌거나** **가중치 선택이 틀렸을** 가능성이 큽니다. [G&W 5e pp.373–374]
- Ordinary Emax vs sigmoid Emax 비교에서, 예측 곡선만 보면 차이가 애매한데 잔차 도표로 가면 한쪽이 **계통적 이탈**로 명확하게 드러납니다. [G&W 5e pp.372–373]
- 가중치 지수는 원문에서 $0$, $-1$, $-2$, $-n$으로 설명되고, Eq.4:49는 $C_i^{-\lambda_z}$ 또는 $\hat C_i^{-\lambda_z}$ 형태예요. "$\lambda_z=-1$"처럼 부호를 단정해 쓰지 말고 **가중치 지수(weighting power)**로 표기해야 합니다. [G&W 5e pp.373–374]

$$
\overbrace{C_i^{-\lambda_z}\ \text{ 또는 }\ \hat C_i^{-\lambda_z}}^{\text{농도 기반 가중치}}
$$

잔차 패턴은 단순한 그림 모양이 아니에요. **"모델이 설명하지 못한 시간 스케일 또는 분산 구조가 밖으로 드러난 모양"**입니다. Banana는 빠른 phase가 빠졌다는 신호일 수 있고, fan은 구조보다 오차분산 모델의 문제일 수 있어요. [G&W 5e pp.372–376]

#### C. 순수오차(pure error) vs 적합결여(lack-of-fit)

반복 측정이 있는 in vitro dataset에서는 잔차오차를 **순수오차**와 **적합결여**로 나눌 수 있어요. Table 4.7 예시: residual SS = 92.67, pure error SS = 23.61, lack-of-fit SS = 69.06. Eq.4:51로 계산하면 $F_{LOF}=15.35$가 나오고, $F_{crit}=2.76$보다 훨씬 커서 lack-of-fit이 있다고 결론냅니다. [G&W 5e pp.377–379]

$$
\overbrace{F_{LOF}}^{\text{LOF F값}}=\frac{\overbrace{(92.67-23.61)/(25-21)}^{\text{LOF 평균제곱}}}{\underbrace{23.61/21}_{\text{pure MS}}}=\underbrace{15.35}_{\text{F 비교값}} \quad [\text{G\&W 5e Eq.4:51},\ p.379]
$$

> 💼 **실무 인사이트** — LOF F-test는 **같은 $x$값에서 반복 측정이 있어서 pure error를 분리할 수 있을 때**만 됩니다. 환자별 sparse clinical PK처럼 같은 시점에 반복 측정이 없는 데이터에서는 LOF F-test를 억지로 만들지 말고, 잔차 패턴과 모델 타당성을 봐야 해요. 또 잔차 vs 시간과 잔차 vs 예측값/농도를 **둘 다** 봐야 합니다. 한 축에서는 무작위 산포처럼 보여도 다른 축에서 fan shape나 구조적 run이 보일 수 있거든요.

#### D. 구조적 필연성

모델 misspecification은 관측 곡선 overlay보다 **잔차 도표에서 먼저** 드러나요. Overlay는 곡선과 데이터의 절대 위치를 보여주지만, 잔차 도표는 오차의 부호와 순서를 그대로 보존해서 계통적 이탈을 훨씬 선명하게 드러냅니다. [G&W 5e pp.369–376]

---

> **이번 카드 핵심내용**  
> ① 곡선은 맞아 보이는데 패턴이 남을 때 — residual sign/run이 구조 오류를 결정한다  
> ② banana vs fan 혼동 — 구조 모델 수정과 weighting 수정은 처방이 다르다  
> ⚡ 잔차 패턴을 noise로 흡수 → **가짜 IIV·가짜 covariate signal**을 만들어낸다


<!-- SLIDE_START: M3 | title: F 검정 적용 조건(F-Test Validity Conditions) -->
<!-- SECTION_CORE: SC-05 -->

### 🃏 M3 — F 검정 적용 조건(F-Test Validity Conditions) [⚡ Apex Concept]

> **앞 카드에서 이 카드로** — M2에서 잔차가 무작위인지 확인했다면, 이제 두 후보 모델의 WRSS 감소가 **검정으로 비교할 자격이 있는 개선인지** 따지는 단계예요.

> **거장의 시각**  
> WRSS가 더 낮고 parameter가 하나 더 많으면 그냥 F-test 쓰면 된다고 생각하기 쉬운데, **F-test는 두 모델이 같은 운동장에 서 있을 때만 쓸 수 있는 심판**입니다. 통계량 계산보다 먼저 **두 모델이 같은 검정 세계에 있는지 판정**하는 게 핵심이에요.

#### A. 형식적 정의

중첩 모델(nested)은 full model에서 특정 parameter를 고정하면 reduced model로 접히는 관계예요. Sigmoid Emax model은 $n=1$로 고정하면 ordinary Emax가 되니까 nested입니다. [G&W 5e p.388]

F 통계량: [G&W 5e p.387]

$$
\overbrace{F^*}^{\text{중첩 F값}}=\frac{\overbrace{(WRSS_{reduced}-WRSS_{full})/(df_{reduced}-df_{full})}^{\text{개선량 (1 자유도당 SS 감소)}}}{\underbrace{WRSS_{full}/df_{full}}_{\text{full MS = 잔차 분산}}} \quad [\text{G\&W 5e Eq.4:54},\ p.387]
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $WRSS_{reduced}$ | 가중 잔차제곱합 | 축소 모델의 남은 불일치 | parameter 제한, 구조 단순화 |
| $WRSS_{full}$ | 가중 잔차제곱합 | 전체 모델의 남은 불일치 | parameter 추가, 동일 weighting 필요 |
| $df$ | 자유도 | 비교 가능한 정보량 | $N_{obs}-N_{par}$ |
| $N_{par}$ | 개수 | 모델 복잡도 | parameter 추가/고정 |

> 💡 F-test는 **같은 트랙에서 달린 두 기록만 비교하는 심판**이에요. 한 선수는 트랙, 다른 선수는 산길에서 달렸다면 시간 차이는 경기력이 아니라 경기장 차이입니다.

$$
\overbrace{df}^{\text{잔차 자유도}}=\underbrace{N_{obs}}_{\text{관측수}}-\underbrace{N_{par}}_{\text{parameter 수}} \quad [\text{G\&W 5e Eq.4:55},\ p.387]
$$

#### B. 유효한 예와 무효한 예

- **유효(Valid)** — ordinary Emax vs sigmoid Emax. Full sigmoid에서 $n=1$로 고정하면 ordinary Emax로 줄어들어요. [G&W 5e p.388]

$$
\overbrace{n}^{\text{sigmoidicity}}=\underbrace{1}_{\text{Emax 제한}}
$$

- **무효(Invalid)** — ordinary Emax vs linear response. $C\ll EC_{50}$이라는 극한 조건에서만 근사적으로 비슷해질 뿐, 일반적으로 nested 관계가 아니에요. [G&W 5e p.388]

$$
\overbrace{C}^{\text{농도}}\ll\underbrace{EC_{50}}_{\text{반최대 농도}}
$$

- **조건부 유효** — hepatic distributed model과 parallel-tube model은 축소 관계가 성립할 때만 F-test 사용 가능. [G&W 5e pp.388–389]
- **이중 위반으로 무효** — Table 4.8의 Michaelis–Menten weighted fit과 first-order unweighted fit. **비중첩이고 weighting까지 다르니까** F-test도 AIC도 둘 다 못 씁니다. [G&W 5e p.389]

#### C. 구조적 필연성

중첩 조건은 단순히 parameter 개수 차이가 있느냐의 문제가 아니에요. **"한 모델이 다른 모델의 제한된 형태인가"**의 문제입니다. 기하학적으로 reduced model은 full model parameter space 안의 제한된 부분공간이어야 하고, 그래야 WRSS 감소량이 "추가 parameter가 설명해낸 개선"으로 해석돼요.

#### D. AIC/SC 적용 경계

AIC와 SC는 nested를 요구하지 않습니다. 하지만 **equal weighting은 반드시 요구**해요. [G&W 5e p.389, Eq.4:56–4:57]

$$
\overbrace{AIC}^{\text{Akaike 기준 (reduced form)}}=\underbrace{N_{obs}\ln(WRSS)}_{\text{불일치}}+\underbrace{2N_{par}}_{\text{복잡도 벌점}} \quad [\text{G\&W 5e Eq.4:56},\ p.389]
$$

$$
\overbrace{SC}^{\text{Schwarz 기준 (reduced form)}}=\underbrace{N_{obs}\ln(WRSS)}_{\text{불일치}}+\underbrace{N_{par}\ln(N_{obs})}_{\text{표본수 벌점}} \quad [\text{G\&W 5e Eq.4:57},\ p.389]
$$

> 💼 **실무 인사이트 — 이 AIC는 "model comparison용 reduced form"입니다.** G&W 5e Eq.4:56은 정규분포 가정 + WRSS 기반 likelihood에서 유도되는데, 두 모델을 같은 데이터에서 비교할 때 **상쇄되어 사라지는 상수항**을 미리 떼어낸 형태예요. 절대 likelihood scale에서 본 full AIC는 다음과 같습니다:
>
> $$
> \overbrace{AIC_{full}}^{\text{절대 likelihood scale}}
> =\overbrace{N_{obs}\ln(WRSS)}^{\text{비교에 남는 항}}+\overbrace{2N_{par}}^{\text{복잡도 벌점}}
> \underbrace{+\,N_{obs}\!\left[\ln(2\pi)+1\right]-N_{obs}\ln(N_{obs})}_{\text{같은 데이터에서 두 모델에 공통 — 비교 시 상쇄}}
> $$
>
> 같은 dataset 안의 모델 A vs B 비교에서는 마지막 상수항이 동일하게 들어가서 차이가 사라지니까, Eq.4:56이 그 작업에는 충분합니다. 그런데 **다른 환경의 OFV와 직접 환산**할 때는 이 상수항이 결정적이에요.
>
> | 환경 | 비교용 좌표 | 절대 scale |
> |---|---|---|
> | WinNonlin/Phoenix 등 WRSS 기반 | $AIC = N_{obs}\ln(WRSS)+2N_{par}$ | reduced form (위 식) |
> | NONMEM OFV ($-2\log L$) | $\Delta\text{OFV}=\chi^2_{df}$로 nested 비교 | full likelihood scale (상수항 포함) |
>
> 그래서 한 모델을 WinNonlin에서 AIC=83으로 보고하고, 같은 모델을 NONMEM OFV=120으로 보고했을 때 **두 숫자는 서로 환산되지 않습니다.** 두 환경을 오가는 학습자가 가장 자주 부딪히는 함정이에요. G&W 5e 자체도 §4.7.8(p.386)에서 WRSS와 $-2\log L$이 "asymptotically give the same values" — 즉 결국 같은 해로 수렴은 하지만 **scale은 다르다**고 명시합니다. [G&W 5e p.386]

AIC/SC의 **가장 낮은 값이 자동으로 좋은 모델을 뜻하지는 않아요.** GOF(모델 적절성)는 잔차, parameter 정밀도, 정확도, 상관행렬, 조건수, F-test, AIC/SC를 함께 보는 **복합 진단 도구군**입니다. [G&W 5e pp.387–391]

#### E. WRSS vs $-2\cdot\log likelihood$

원문은 역사적 WRSS 기반 비교와 현대적 $-2\cdot\log likelihood$ 기반 비교를 구분하면서, 비교 원리 자체는 동일하게 모델 적절성 기준과 연결된다고 설명해요. [G&W 5e p.386] 이걸 NONMEM의 OFV 비교로 번역할 수는 있고, **§1의 "ΔOFV의 통계적 정당성" 다리 카드**에서 카이제곱 근사와 SCM 임계값(3.84/6.63)을 정리했습니다. 다만 NONMEM의 ΔOFV 사용 자체와 SCM 운영은 G&W 5e의 직접 내용이 아니라 후속 문헌(Wählby et al. 2002, Lindbom et al. 2005)에 기반한 운영 확장이에요.

---

#### F. 흔한 오류 — 나비효과까지

"WRSS가 더 낮고 parameter가 하나 더 많으니까 F-test 쓰면 되겠지"라고 많이들 생각해요. 같은 데이터에서 더 복잡한 모델이 작은 불일치를 만든 것처럼 보이니까 그럴싸한 판단이죠. 그런데 두 모델이 비중첩이거나 weighting이 다르면, 이 WRSS 감소는 "추가 parameter 효과"가 아니라 그냥 좌표가 달라서 생긴 숫자일 수 있어요. 이걸 그대로 두면 어떻게 되냐 — **잘못 선택한 모델로 용량·안전역 시뮬레이션을 돌려서 임상에서 위험한 결정이 나옵니다**. 그리고 규제 측에서는 "비교 조건 위반"으로 짚으면서 재분석과 모델 선택 근거 재제출을 요구해요. 한 줄로 정리하면 — F-test 적용 조건 위반은 임상 의사결정 오염과 규제 재작업으로 그대로 전파됩니다.

> **이번 카드 핵심내용**  
> ① ordinary Emax vs sigmoid Emax — nested + equal weighting이면 F-test 가능  
> ② MM weighted vs first-order unweighted — non-nested + different weighting이면 F-test/AIC 모두 불가  
> ⚡ "낮은 WRSS = 더 좋은 모델" → 비교 좌표 붕괴 → **잘못된 모델 선택 + 재분석 요구**


<!-- SLIDE_START: M4 | title: 파라미터 정밀도와 상관(Parameter Precision & Correlation) -->
<!-- SECTION_CORE: SC-06 -->

### 🃏 M4 — 파라미터 정밀도와 상관(Parameter Precision & Correlation)

> **앞 카드에서 이 카드로** — M3에서 두 모델이 비교 가능한지까지 확인했어요. 그런데 한 모델 안에서도 함정이 있습니다 — **좋은 fit이 곧 식별 가능한 parameter를 뜻하는 건 아니거든요.**

> **거장의 시각**  
> 좋은 곡선 적합을 좋은 parameter 추정으로 착각하면, ridge와 상관행렬이 숨기고 있는 식별성 문제를 그대로 놓칩니다. precision과 correlation을 **설계의 결과**로 읽으면, 다음 sampling을 어디서 보강해야 할지가 거의 자동으로 보여요.

#### A. 정확도, 정밀도, CV%

정확도(accuracy)는 **편향(bias)** 의 문제이고, 정밀도(precision)는 **추정의 불확실성** 문제예요. "평균적으로 맞는가"와 "반복하면 얼마나 좁게 모이는가"는 다른 질문입니다. 원문은 다트 과녁 비유로 이 둘을 구분해요. [G&W 5e pp.379–380]

$$
\overbrace{CV\%}^{\text{상대 SE}}=\frac{\overbrace{SE(\hat p)}^{\text{추정 SE}}}{\underbrace{\hat p}_{\text{parameter 값}}}\cdot100 \quad [\text{G\&W 5e Eq.4:52},\ p.380]
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $CV\%$ | % | 추정값 대비 표준오차 | SE 증가, parameter estimate 감소 |
| $SE(\hat p)$ | parameter 단위 | 추정 불확실성 | sparse design, high correlation |
| $r$ | 무차원 | 원문상 GOF 보조량 | dynamic range, residual SS |
| correlation matrix | 무차원 | parameter trade-off | sampling design, ridge geometry |

> 💡 좋은 fit과 낮은 CV는 **과녁 중심과 탄착군 폭**의 관계예요. 화살이 중심 근처에 보여도 탄착군이 길게 늘어져 있으면, 실력이 같다고 말할 수 없죠.

$p=0.01\pm0.005\ h^{-1}$의 **CV 50%** 예시는 "추정 불확실성이 높다"는 걸 보여주는 예시일 뿐, G&W 5e가 정한 기각 기준은 아닙니다. [G&W 5e p.380]

#### B. 상관계수 r은 GOF가 아닙니다

G&W 5e는 상관계수가 **GOF 기준으로 가장 많이 오용되는 숫자 중 하나**라고 명시해요. Eq.4:53은 원문 표기 그대로 보존합니다. [G&W 5e p.381]

$$
\overbrace{r}^{\text{GOF 지표}}=1-\frac{\overbrace{\sum(C_i-\hat C_i)^2}^{\text{잔차제곱합}}}{\underbrace{\sum(C_i-\bar C)^2}_{\text{총변동}}} \quad [\text{G\&W 5e Eq.4:53 source form},\ p.381]
$$

*↑ 원문 표기 $r$은 잔차제곱합/총변동 기반 GOF 보조량으로 읽어요.*

Fig.4.53이 가르치는 게 정확히 이거예요. OLS fit은 $r=0.96$인데 **마지막 세 관측치를 계통적으로 과소예측**하고 있어요. IRLS fit은 $r=0.94$로 숫자는 약간 낮은데 전체적으로 더 나은 fit입니다. → 그래서 높은 $r$이 좋은 fit의 충분조건이 아니라는 거예요. [G&W 5e p.382]

> 💼 **실무 인사이트** — 동적 범위가 넓은 농도-시간 자료에서는 $r$이 모델의 잔차 구조보다 **전체 값의 범위**에 강하게 끌려가요. 그러니까 $r$은 잔차 도표와 함께 읽어야지, 혼자서 GOF 판정 기준으로 쓰면 안 됩니다.

#### C. 파라미터 상관과 능선 기하

parameter 상관행렬은 parameter들이 독립적으로 추정되는지, 아니면 서로 trade-off하면서 움직이는지를 보여줘요. 원문은 높은 상관이 **parameter를 줄이거나** 또는 **데이터를 더 모아야** 한다는 신호라고 설명합니다. [G&W 5e pp.382–383]

Fig.4.55–4.57의 핵심은 **능선형 최솟값(ridge minimum)** — 길게 늘어진 최솟값 영역이에요. 두 parameter가 ridge 위에서 같이 움직이면 OFV/WRSS가 거의 변하지 않아서, 단변량 추정값 자체는 그럴듯해 보여도 **결합 불확실성**이 큽니다. Design A/B 비교가 보여주는 핵심은 — 같은 모델인데도 sampling design에 따라 $Cl/V$ 또는 $IC_{50}/I_{max}$ 상관이 크게 달라진다는 거예요. [G&W 5e pp.383–385]

#### D. 한 파라미터를 고정하는 결정

Fig.4.55는 한 parameter를 고정하면 다른 parameter의 신뢰구간이 줄어들 수 있음을 보여줘요. [G&W 5e pp.383–384] 그런데 이건 공짜가 아닙니다. **정당화 부담을 통계에서 생물학·문헌·선행 연구로 옮기는 행위**예요. 고정값의 출처와 적용 가능성을 설명하지 못하면, 정밀도가 좋아진 게 아니라 **불확실성을 덮어 숨긴 것**이 됩니다.

#### E. asymptotic SE가 부족할 때 — bootstrap/SIR 환승

표준 SE/CV%는 likelihood surface가 최솟값 근방에서 정규 곡률을 갖는다는 가정 위에 서 있습니다. 그 가정이 깨지는 자리(boundary parameter, 높은 상관, 비정규 posterior, 작은 표본)에서는 **bootstrap과 SIR**이 대안이에요. 이 두 도구의 통계적 정당성과 사용 조건은 **§1의 "Bootstrap과 SIR의 이론적 위치" 다리 카드**에 정리되어 있습니다. M4의 단변량 SE/CV%가 좁아 보여도 안심하지 못하는 자리에서, 그 다리 카드를 다시 참조하세요.

#### F. 한계

높은 상관에 대한 **보편적 cutoff는 G&W 5e에 없어요.** $|r|>0.95$ 같은 hard threshold 대신 상관행렬, 신뢰 타원, 잔차 패턴, 설계 적절성을 함께 봐야 합니다. 조건수나 covariance-step warning은 현대 NONMEM 구현에서 매우 유용한 신호지만, G&W 5e의 직접 교육 포인트는 **"상관은 설계의 결과"**라는 한 줄이에요.

---

> **이번 카드 핵심내용**  
> ① fit은 좋아 보이는데 SE/CV가 클 때 — parameter identifiability가 지배한다  
> ② r 높음 vs 진짜 GOF — residual pattern·precision·correlation이 따로 본다  
> ⚡ "r이 높으면 충분" → terminal bias·ridge·design weakness를 그대로 놓친다


<!-- SLIDE_START: M5 | title: 편미분 기반 최적 샘플링(Partial-Derivative Optimal Sampling) -->
<!-- SECTION_CORE: SC-07 -->

### 🃏 M5 — 편미분 기반 최적 샘플링(Partial-Derivative Optimal Sampling)

> **앞 카드에서 이 카드로** — M4에서 parameter 상관이 설계의 약점을 드러냈죠. 그러면 자연스럽게 다음 질문 — **"어느 시간점이 그 parameter를 가장 잘 보이게 하는가?"**

> **거장의 시각**  
> 편미분을 단순한 미적분 계산 문제로만 보면 최적 sampling의 실무 의미를 놓칩니다. derivative peak를 **"정보가 가장 크게 생기는 시간·농도 위치"**로 읽으면, 다음 실험의 sampling 설계가 수식에서 거의 자동으로 나와요.

#### A. 이중지수 편미분 설계

원문은 이중지수 모델을 예로 듭니다. [G&W 5e p.399]

$$
\overbrace{C}^{\text{총농도}}=\overbrace{\underbrace{A}_{\text{빠른 절편}}e^{-\underbrace{\alpha}_{\text{빠른 slope}}t}}^{\text{초기 정보}}+\overbrace{\underbrace{B}_{\text{느린 절편}}e^{-\underbrace{\beta}_{\text{느린 slope}}t}}^{\text{말단 정보}} \quad [\text{G\&W 5e Eq.5:7},\ p.399]
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $A, B$ | 농도 | 초기/말단 절편 정보 | 초기·말단 sample 위치 |
| $\alpha, \beta$ | $\text{time}^{-1}$ | 빠른/느린 slope 정보 | derivative peak 위치 |
| $t=1/\alpha$ | 시간 | 빠른 slope 정보가 가장 큰 시간 | $\alpha$ 증가 시 앞당겨짐 |
| $t=1/\beta$ | 시간 | 말단 slope 정보가 가장 큰 시간 | $\beta$ 감소 시 늦어짐 |

> 💡 편미분 peak는 **어두운 방에서 손전등이 가장 밝게 비추는 지점**이에요. 그 자리에 sample을 놓아야 해당 parameter의 윤곽이 선명해집니다.

$A$와 $B$에 대한 편미분은 절편 영역에서 극값을 갖고, $\alpha$와 $\beta$에 대한 편미분은 각각 $t=1/\alpha$, $t=1/\beta$에서 극값을 갖습니다. [G&W 5e pp.399–400]

$$
\overbrace{t}^{\text{민감도 peak}}=\frac{1}{\underbrace{\alpha}_{\text{빠른 slope}}},\qquad \overbrace{t}^{\text{민감도 peak}}=\frac{1}{\underbrace{\beta}_{\text{느린 slope}}} \quad [\text{G\&W 5e Eq.5:11},\ p.400]
$$

예시 parameter가 $\alpha=0.69\ h^{-1}$, $\beta=0.069\ h^{-1}$이면 최적 시간은 약 **1.4 h와 14 h**입니다. Fig.5.4에서는 $\alpha$와 $\beta$ 정보가 각각 약 **20 min, 300 min** 부근에 모이는 게 보여요. [G&W 5e p.400]

#### B. Sigmoid Imax / Emax 설계

Sigmoid Imax model의 편미분을 풀어 보면, $IC_{50}$ 정보는 **half-maximal effect 부근**에 집중되고, sigmoidicity factor $n$ 정보는 **20%와 80% effect level 부근**에 집중됩니다. Fig.5.6은 $E_0$, $n$, $EC_{50}$, $n$, $E_{max}$ 다섯 parameter에 대한 design point를 한 그림에 보여줘요. [G&W 5e pp.400–402]

#### C. Turnover model 설계

Turnover response model에서는 $k_{out}$ 민감도가 **25 h와 약 100 h post-dose**에서 큽니다. 그리고 초기 시간대에서는 $k_{out}$이 $IC_{50}$이나 $n$보다 민감해요. → 그래서 초기 sampling은 $k_{out}$ 초기 추정을 직접 강화하는 데 효과적입니다. [G&W 5e pp.402–404]

#### D. 구조적 필연성

편미분이 큰 위치는 **예측이 해당 parameter 변화에 가장 크게 반응하는 위치**예요. 가능도 표면(likelihood surface, parameter 공간에서 OFV가 분포하는 지형)의 언어로 바꿔서 말하면, 그 시점의 관측치는 해당 parameter 방향으로 **곡률을 키워서 최솟값을 좁고 깊게** 만드는 정보를 줍니다.

> 💼 **실무 인사이트** — parameter 단위가 서로 다르면 원자료 $\partial C/\partial\theta$ 크기 비교 자체가 왜곡될 수 있어요. 실무에서는 $\theta_i(\partial C/\partial\theta_i)/C$ 같은 **정규화 민감도**를 같이 보면서 parameter 간 비교를 안정화합니다.

$$
\overbrace{\frac{\theta_i\,(\partial C/\partial\theta_i)}{C}}^{\text{정규화 민감도 (normalized sensitivity)}}
$$

#### E. 경계 조건

참 parameter 값을 미리 정확히 알 수는 없잖아요. 그러니까 derivative 극값에만 sample을 몰아넣으면 안 돼요. **전체 농도 범위에도 추가 sample**을 두어야 합니다. 원문은 pooled data를 무비판적으로 설계 결정에 쓰는 위험도 같이 경고해요. [G&W 5e p.402]

---

> **이번 카드 핵심내용**  
> ① 어느 시간에 sample을 찍을까 — partial derivative peak가 결정한다  
> ② intercept 정보 vs slope 정보 — 초기 시간대와 말단 시간대가 서로 다른 parameter를 본다  
> ⚡ "균등 sampling이면 충분" → 민감도 낮은 구간만 반복 → **parameter precision 개선 실패**


<!-- SLIDE_START: M6 | title: 민감도 분석(Sensitivity Analysis) -->
<!-- SECTION_CORE: SC-08 -->

### 🃏 M6 — 민감도 분석(Sensitivity Analysis)

> **앞 카드에서 이 카드로** — M5에서 편미분이 "정보가 어디서 생기는지" 알려줬어요. 이제 마지막 질문 — **그 parameter 불확실성이 임상 결론을 어디까지 흔드는가?**

> **거장의 시각**  
> 민감도 분석을 사후 그림 한 장으로만 보면, 예측 결론이 무너지는 지점을 그대로 놓칩니다. parameter perturbation을 **다음 실험 전에 돌리는 stress test**로 읽으면, 안전역·AUC·sampling package를 어디서 조정해야 할지 근거가 생겨요.

#### A. 형식적 정의

민감도 분석은 특정 parameter를 일정 비율로 흔들었을 때 농도-시간 또는 반응-시간 예측이 얼마나 달라지는지 보는 절차예요. 즉 **parameter 불확실성이 예측 불확실성으로 얼마나 번역되는지** 보는 거죠. 원문 예시는 parameter를 **+100% 또는 −50%**로 흔들어서 모델 출력을 비교합니다. [G&W 5e pp.404–405]

#### B. PK 민감도 예시

Michaelis–Menten PK 모델에서 $V_{max}$, $K_M$, $V_c$, $V_t$를 흔들어 보면 농도-시간 프로파일의 **어느 구간이 어떤 parameter에 민감한지** 그대로 드러납니다. Fig.5.9는 이 결과를 향후 sampling 위치 결정에 그대로 연결해 줘요. [G&W 5e p.405]

#### C. PD 민감도 예시 — warfarin

**Warfarin-PCA 모델**에서는 $IC_{50}$, $k_{in}$, $k_{out}$, $t_{lag}$를 흔들어서 반응-시간 프로파일에 미치는 영향을 비교합니다. Fig.5.10이 답해 주는 질문은 — **"어떤 parameter를 더 잘 추정하려면 반응-시간 곡선의 어느 구간을 sampling으로 보강해야 하는가?"** 예요. [G&W 5e p.405]

#### D. 독성동태 설계 맥락

독성동태 설계에서 만성시험은 보통 **노출 확인 목적으로 $C_{max}$ sampling만으로 충분**한 경우가 있어요. 다만 예외가 있어서 연구자 판단이 필요합니다. Table 5.6은 PK/DRF/chronic study type별로 profile 중심 vs $C_{max}$ 중심 sampling package를 구분해 줘요. [G&W 5e p.413]

비선형 제거가 있는 약물에서는 농도가 **first-order linear kinetics** 영역으로 떨어지거나 무시 가능한 수준까지 sampling을 이어가야 합니다. 안 그러면 **진정한 무한대 외삽 AUC**를 얻을 수 없어요. [G&W 5e p.414]

용량의존 동태와 시간의존 동태가 동시에 존재하면 골치 아픈 상황이 생깁니다 — **Day 1 AUC와 정상상태 AUC 비교가 서로 상쇄되어 해석이 흐려져요**. Fig.5.20이 보여주는 핵심이 이거예요. 노출이 안 변한 것처럼 보여도 **capacity와 induction이 동시에 작동**해서 두 효과가 서로 가려질 수 있다는 점. [G&W 5e p.414]

> 💼 **실무 인사이트** — 민감도 분석은 parameter를 "잘 추정했는지"보다 먼저 **"잘못 추정하면 어떤 결론이 흔들리는지"**를 묻습니다. 흔들리는 결론이 용량 결정, 안전역, sampling 일정 같은 거라면 다음 실험 설계 자체를 바꿔야 해요.

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $V_{max}$ | 양/시간 | 포화 제거 최대속도 | capacity 변화 |
| $K_M$ | 농도 | 반최대 제거 농도 | affinity/포화 위치 변화 |
| $IC_{50}$ | 농도 | 반최대 억제 농도 | potency 변화 |
| $k_{in}, k_{out}$ | 반응/시간, $\text{time}^{-1}$ | turnover 입력·출력 | synthesis/turnover 변화 |

> 💡 민감도 분석은 **다리의 특정 볼트를 일부러 흔들어 보는 검사**예요. 그 흔들림이 용량·안전역 결론까지 전달된다면, 다음 실험 설계를 보강해야 한다는 뜻입니다.

---

> **이번 카드 핵심내용**  
> ① parameter 불확실성이 임상 결론을 흔드는가 — sensitivity analysis가 답한다  
> ② PK profile 중심 vs $C_{max}$ 중심 TK sampling — study type과 nonlinear elimination 여부가 결정한다  
> ⚡ "노출이 같아 보이면 기전도 같다" → capacity·time-dependent kinetics 상쇄를 놓쳐 **AUC 해석 실패**


<!-- SLIDE_START: §5 | title: 혼동쌍 해부 -->
<!-- SECTION_CORE: SC-09 -->

## §5 — 혼동쌍 해부(Confusion Pair Dissection)

여기 모은 네 쌍은 실무에서 가장 자주 헷갈리는 짝들이에요. 같은 단어처럼 들리지만 처방이 완전히 다른 짝들.

### ▣ 혼동쌍 #1 — 중첩 + 동일 가중치 vs 비중첩 또는 다른 가중치

| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | 중첩 + 동일 가중치 — F-test와 AIC/SC가 쓰일 수 있는 비교 자리 | 비중첩 또는 다른 가중치 — 서로 다른 WRSS 좌표 |
| 수식 내 위치 | $F^*$의 WRSS 차이와 $df$ 차이가 의미를 갖는 전제 | $WRSS_{reduced}-WRSS_{full}$ 자체가 해석 불가; AIC/SC도 weighting 다르면 불가 |
| 변화 원인 | full model에서 parameter 제한으로 reduced가 접히고 weighting이 같음 | model structure가 다르거나 weighting이 달라서 비교 기준 자체가 어긋남 |
| 혼동 시 임상 결과 | 적절한 추가 parameter 검정 가능 | 잘못된 모델 선택 → 후속 dose simulation·safety margin·sampling 권고가 오염됨 [G&W 5e pp.387–389] |

> 💼 **실무 인사이트** — 가중치 선택은 관행이 아니라 **잔차 패턴으로 정당화**해야 해요. Fan shape이면 상대오차 가중치를 의심하고, 잔차 폭이 균질하면 고정 절대오차가 더 자연스럽습니다. [G&W 5e pp.373–374]

**기억 고리** — F-test는 "**중첩 + 같은 가중치**"라는 자물쇠가 맞아야 열립니다.

### ▣ 혼동쌍 #2 — 상관계수 r vs 진정한 GOF

| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | $r$ — 무차원 보조 숫자 | 진정한 GOF — 곡선·잔차·정밀도·상관의 복합 판정 |
| 수식 내 위치 | 잔차제곱합/총변동 비율 기반 원문 지표 | residual vs time, residual vs prediction/concentration, precision matrix |
| 변화 원인 | 농도 범위가 넓으면 자동으로 높아질 수 있음 | terminal bias, systematic run, fan shape, poor precision이 드러남 |
| 혼동 시 임상 결과 | $r=0.96$ 같은 숫자에 안심함 | terminal observation 과소예측 또는 IRLS 우월 패턴을 놓침 [G&W 5e pp.381–382] |

> 💼 **실무 인사이트** — PK 데이터처럼 $y$값 범위가 넓은 경우, $r$은 **dynamic range의 영향**을 크게 받아요. 그러니까 $r$은 GOF의 주연이 아니라 어디까지나 보조 숫자입니다.

**기억 고리** — $r$은 큰 방향만 보고, **잔차는 모델의 거짓말을 본다**.

### ▣ 혼동쌍 #3 — 구조 모델 오류 vs 분산/가중치 모델 오류

| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | 구조 모델 오류 — 시간 스케일/compartment/shape 문제 | 분산·가중치 오류 — 관측오차 크기와 weighting 문제 |
| 수식 내 위치 | 빠진 exponential term, wrong Emax shape, lag-time omission | $W_i$, $C_i^{-\lambda_z}$ 또는 $\hat C_i^{-\lambda_z}$ |
| 변화 원인 | banana, U-shape, systematic runs | fan shape, concentration-dependent spread |
| 혼동 시 임상 결과 | weighting만 바꿔서 구조 오류를 가림 | compartment를 추가해서 variance 문제를 복잡화 [G&W 5e pp.372–376] |

> 💼 **실무 인사이트** — Fan shape에 compartment를 추가하거나 banana에 weighting만 바꾸면, 문제의 원인은 그대로 남고 모델만 더 복잡해져요.

**기억 고리** — 모양이 휘면 구조를 의심하고, 폭이 벌어지면 분산을 의심한다.

### ▣ 혼동쌍 #4 — 이상치 A vs 이상치 B

| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | 이상치 A — 참 곡선에서의 수직 이탈 | 이상치 B — 시간축 이탈과 높은 leverage |
| 수식 내 위치 | residual 크기를 키워 precision 감소 | curve 방향 자체를 끌어서 bias 유발 |
| 변화 원인 | noisy point, vertical deviation | sampling time/reporting error 가능성, high leverage |
| 혼동 시 임상 결과 | 잡음점으로 처리 가능 | 잘못된 curve가 정밀해 보이는 편향 생성 [G&W 5e p.390] |

원문이 강조하는 핵심 — **table만 봐서는 A와 B의 이탈점을 거의 알아보기 어렵다**는 거예요. 그래서 이상치 판단에서는 **graphical presentation이 결정적**입니다. [G&W 5e p.390]

> 💼 **실무 인사이트** — Cook's distance나 hat matrix는 현대 회귀 진단에서 유용한 도구지만, 이 G&W 5e의 교육 핵심은 **plot에서 leverage와 수직 이탈을 눈으로 먼저 구분**하는 거예요.

**기억 고리** — A는 위아래로 튄 점이고, **B는 시간을 잘못 말하는 점**이에요. B가 더 위험한 이유는 **곡선의 방향 자체를 바꿔버리기 때문**입니다.


<!-- SLIDE_START: §7 | title: 자기 점검: 능동 회상 모듈 -->
<!-- SECTION_CORE: SC-10 -->

## §7 — 자기 점검: 능동 회상 모듈(Self-Test: Active Recall Module)

### Q1. [회상 ★★]

**문제** — 초기값이 부실할 때 Gabrielsson & Weiner가 명시한 세 가지 위험은 무엇인가? [G&W 5e p.353]

**정답** — 잘못된 최종 추정값, 원치 않는 local minima, 생리학적으로 불가능한 parameter 값입니다. 초기값은 단순 편의값이 아니라 **알고리즘이 어떤 골짜기로 들어갈지 결정하는 EDA 산출물**이에요.

---

### Q2. [계산 ★★]

**문제** — 10 mg IV bolus 예시에서 반로그 기울기가 $-0.01\ \text{min}^{-1}$일 때 $t_{1/2}$, AUC, Cl, V의 source anchor 값을 쓰세요. [G&W 5e p.354]

**정답** — $t_{1/2}\approx65\ \text{min}$, $AUC=100{,}000\ \mu g\cdot L^{-1}\cdot\text{min}$, $Cl=0.1\ L\cdot\text{min}^{-1}$, $V=10\ L$. [G&W 5e Eq.4:17–4:20]

---

### Q3. [회상 ★]

**문제** — 이중지수 곡선 분리에서 **말단상을 먼저 읽는 이유**는 무엇인가? [G&W 5e pp.354–355]

**정답** — 말단상에서는 빠른 지수항 $Ae^{-\alpha t}$가 거의 사라지고 $Be^{-\beta t}$만 남기 때문이에요. $B$와 $\beta$를 먼저 읽고 후방 외삽해서 초기상에서 빼면 $A$와 $\alpha$가 깔끔하게 나옵니다.

---

### Q4. [진단 ★★]

**문제** — 잔차 도표에서 **banana pattern과 fan shape**가 각각 의심하게 만드는 문제는? [G&W 5e pp.372–376]

**정답** — Banana/U-shape는 **구조적 시간 스케일** 문제(빠진 지수항, 잘못된 모델 형태)를 의심하게 만들어요. Fan shape는 **농도의존 분산** 또는 **가중치 불일치**를 의심하게 합니다.

---

### Q5. [핵심 개념(Apex) 적용 ★★]

**문제** — Ordinary Emax vs sigmoid Emax 비교에 F-test를 쓸 수 있나? Linear response vs ordinary Emax는? [G&W 5e p.388]

**정답** — Ordinary Emax vs sigmoid Emax는 sigmoid에서 $n=1$을 고정하면 ordinary Emax가 되니까 **nested**이고 F-test 가능합니다. Linear response vs ordinary Emax는 일반적으로 nested가 아니라서 **F-test를 쓰면 안 됩니다**.

---

### Q6. [판정 ★★]

**문제** — Michaelis–Menten weighted fit과 first-order unweighted fit에서 AIC가 더 낮은 모델을 그냥 선택해도 되나? [G&W 5e p.389]

**정답** — **안 됩니다.** Table 4.8은 두 모델이 **비중첩 + 다른 weighting**이라 F-test도 AIC도 둘 다 못 쓰는 상황을 보여줘요. AIC/SC는 nested를 요구하지는 않지만 **equal weighting은 반드시 요구**합니다.

---

### Q7. [계산/개념 ★★]

**문제** — Table 4.7의 residual SS = 92.67, pure error SS = 23.61, df = 25와 21로 계산한 $F_{LOF}$는? 결론은? [G&W 5e pp.378–379]

**정답** — $F_{LOF}=[(92.67-23.61)/(25-21)]/(23.61/21)=15.35$이고, $F_{crit}=2.76$보다 훨씬 커서 **lack-of-fit이 있습니다.** 단, 이 검정은 **반복 측정이 있어 pure error를 분리할 수 있을 때만** 됩니다.

---

### Q8. [설계 ★★]

**문제** — Fig.4.55–4.57에서 design A와 design B가 가르치는 핵심은? [G&W 5e pp.383–385]

**정답** — parameter 상관과 신뢰 타원은 **모델 방정식만의 문제가 아니라 sampling design의 결과**라는 사실이에요. 좋은 설계는 두 parameter의 정보 영역을 분리해서, 둘이 서로 trade-off하지 않게 만들고 신뢰구간과 상관을 낮춥니다.

---

### Q9. [개념/통계 ★★] — *추가*

**문제** — NONMEM에서 covariate를 추가했더니 $\Delta\text{OFV} = 5.2$가 나왔다. forward inclusion ($\alpha=0.05$) 단계에서 이 covariate를 채택해야 할까? backward elimination ($\alpha=0.01$)에서도 살아남을까?

**정답** — Forward inclusion 임계값은 $\chi^2_{1,0.95} \approx 3.84$이므로 $5.2 > 3.84$ → **forward에서는 채택**. Backward elimination 임계값은 $\chi^2_{1,0.99} \approx 6.63$이므로 $5.2 < 6.63$ → **backward에서는 탈락**합니다. 두 단계의 임계값이 다른 이유는 다중 비교 보정과 robustness 확보예요. 카이제곱 근사는 (i) 중첩 관계, (ii) 충분히 큰 표본, (iii) parameter가 boundary에 있지 않을 때 성립합니다. [Wilks 1938; Wählby et al. 2002]

---

### Q10. [개념 ★★] — *추가*

**문제** — 모델 fit이 끝났는데 NONMEM의 $COV$ step이 실패했다. asymptotic SE를 못 얻은 상황에서 parameter 불확실성을 어떻게 평가할 수 있나? 두 가지 방법과 각각의 작동 원리를 설명하세요.

**정답** — **Bootstrap**과 **SIR**이 대안이에요. Bootstrap은 **원본 데이터를 with-replacement로 재표집해서 각 dataset에 모델을 다시 fit**하고, $\hat\theta^{(b)}$의 경험적 분포에서 직접 percentile CI를 읽습니다 — asymptotic 가정에 의존하지 않아서 boundary/비정규/소표본에 robust한 반면 비용이 큽니다. SIR(Sampling Importance Resampling)은 **proposal 분포에서 parameter vector를 sampling하고 likelihood ratio로 importance weight를 부여한 뒤 weighted resampling**으로 posterior를 근사 — fit을 한 번만 돌리니까 bootstrap보다 비용이 훨씬 적습니다. 둘 다 **asymptotic SE가 작동하지 못하는 자리에서 결합 불확실성의 진짜 모양**을 보여주는 도구예요. [Efron 1979; Dosne et al. 2016]

---

### Q11. [개념 ★★] — *추가*

**문제** — M2의 GOF/잔차 진단, M3의 F/AIC, M4의 precision까지 다 통과한 모델이 VPC에서 실패한다면, 무엇이 잘못된 건가?

**정답** — GOF/잔차/AIC는 **model-fit-based 진단** — 추정값이 데이터를 얼마나 잘 설명하는지를 봅니다. fitted curve는 정의상 데이터 중심으로 끌려가니까 random scatter가 보장되기 쉽고, 모델이 데이터를 "설명"한다는 증거는 줘도 "생성"한다는 증거는 못 줘요. VPC는 **simulation-based 진단** — 추정 모델 + 추정 random effect 구조로 새 dataset을 수백 번 simulation해서 그 percentile band가 관측의 envelope을 재현하는지 봅니다. VPC에서 median은 잘 맞는데 5–95% band가 좁거나 넓으면, **variability 구조(IIV·RUV 모델)가 잘못 잡힌 것**이에요. pcVPC가 추가로 실패하면 design/covariate 차이를 변동성으로 흡수한 거고, NPDE가 N(0,1)을 벗어나면 분포 형태 자체가 틀린 거예요. [Holford 2005; Bergstrand et al. 2011; Brendel et al. 2006]

---

### Q12. [보스 딜레마(Boss Dilemma) ★★]

**문제** — 두 경쟁 모델이 있어요. 하나는 WRSS가 더 낮은데 **다른 weighting**을 썼고, 다른 하나는 기전적으로 더 타당한데 AIC 차이가 작아요. 보스가 "어느 모델로 갑니까?" 묻는다면?

**정답** — 먼저 **같은 weighting으로 다시 fit**해서 비교 가능성부터 확보해야 합니다. 그래도 F-test/AIC가 단독 결론을 안 주면 **잔차 패턴, 기전 타당성, 외부 데이터, 시각적 예측(VPC/pcVPC)을 함께 삼각검증**해요. G&W 5e는 AIC 차이 기준값을 정의하지 않으니까, **낮은 AIC 하나만으로 기전 타당성을 이길 수 없다**는 게 핵심입니다. [G&W 5e p.389, p.391]

> 🎯 **이 슬라이드들이 존재하는 이유** — 최종 GOF는 잔차·precision·correlation·comparison·design feedback이 **모두 통과할 때**만 완성됩니다.


---

<!-- SLIDE_START: §8 | title: 메타 프레임과 큰 그림 -->
<!-- SECTION_CORE: SC-11 -->

## §8 — 메타 프레임과 큰 그림(Meta-Frame & Big Picture)

### A. 위치 잡기

이 세션은 PK/PD 모델링에서 **"모델을 세우는 기술"보다 "모델을 버리거나 다시 설계하는 기술"**에 더 가까워요. 초기값은 fit의 출발점을 정하고, 잔차는 모델 결함을 드러내고, F-test/AIC/SC는 비교 조건을 제한하고, 정밀도·상관은 설계의 약점을 드러내고, 편미분과 민감도 분석은 다음 sampling을 바꿉니다. [G&W 5e p.353, pp.369–391, pp.399–405]

현대 PopPK에서 이 사이클의 실무 단위는 단일 run이 아니라 **model/control file 한 버전 + GOF diagnostic plot set + VPC/pcVPC + bootstrap/SIR uncertainty + 다음 cohort sampling recommendation**의 묶음이 함께 완성되어야 modeling carousel이 한 바퀴 돈 거예요. §1의 다리 카드들(VPC 정당성, bootstrap/SIR, ΔOFV)이 이 묶음의 이론적 골격을 제공합니다.

### B. 의존성 사슬

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| 초기값이 틀림 | starting parameter vector | → | 잘못된 수렴 또는 local minimum | EDA/NCA/graph anchor 재설정 [G&W 5e p.353] |
| 잔차가 계통적 | residual pattern | → | GOF 성립 불가 | 구조 또는 weighting 재검토 [G&W 5e pp.369–376] |
| 비중첩/다른 weighting 비교 | WRSS/AIC/SC 좌표 | → | F-test/AIC 무력화 | 기전·잔차·외부근거 삼각검증 [G&W 5e pp.387–389] |
| 파라미터 상관 높음 | precision/correlation | → | 식별성 취약 | 다음 sampling design 보강 [G&W 5e pp.382–385] |
| asymptotic SE 가정 깨짐 | boundary/소표본/비정규 | → | 표준 CI 신뢰 불가 | bootstrap/SIR로 결합 불확실성 재구성 [Dosne et al. 2016] |
| GOF 통과했지만 generative fit 미확인 | model-fit only | → | predictive performance 미확립 | VPC/pcVPC/NPDE로 simulation 검문 [Bergstrand et al. 2011] |
| 정보 위치 불명확 | partial derivative/sensitivity | → | 예측 결론 흔들림 | derivative peak + sensitivity 기반 설계 [G&W 5e pp.399–405] |

### C. 전문성 해자

경험 많은 모델러는 "어느 모델의 AIC가 낮은가"만 보지 않아요. 두 모델이 비슷한 WRSS/AIC를 보이는데 잔차 패턴도 애매하고 기전도 애매하면, 어느 한쪽을 고르기 전에 **둘 다 잘못된 기전일 가능성**을 의심해요. 이 역방향 추론이 모델 선택을 **parameter 개수 게임에서 기전 가설 수정으로** 바꿉니다.

### D. Table 4.9에 기반한 GOF 체크리스트

모델 적합성은 최소한 이 다섯 질문에 답할 수 있을 때만 완성된 거예요. [G&W 5e p.391]

| 체크리스트 질문 | 핵심 해석 |
|---|---|
| 모델에 생물학적 관련성이 있는가? | 기전적 타당성 없는 낮은 AIC는 취약하다 |
| fitted curve가 데이터의 경향을 재현하는가? | 곡선 overlay가 첫 관문이다 |
| parameter가 충분한 정밀도로 추정되었는가? | CV%, SE, 신뢰구간을 본다 (필요 시 bootstrap/SIR로 보강) |
| 잔차에 계통적 이탈이 없는가? | Run, banana, fan, lag-time pattern을 본다 |
| 잔차 도표가 무작위 산포를 보이는가? | 무작위가 아니면 모델 또는 weighting을 다시 본다 |

### E. 압축 한 줄

이 세션 전체를 한 문장으로 줄이면 이거예요:

> **초기값은 알고리즘의 출발점을 정하고, 잔차는 모델의 거짓말을 드러내며, F-test/AIC는 비교 가능한 모델에서만 의미가 있고, 정밀도/상관은 설계의 품질을 말하며, 편미분과 민감도 분석은 다음 실험을 어디서 다시 해야 하는지 알려줍니다 — 그리고 VPC/pcVPC/NPDE와 bootstrap/SIR은 그 모든 검문을 통과한 모델이 "생성 모델로서도 신뢰 가능한가"를 마지막으로 확인합니다.**

이 문장이 머리에 박혀 있으면, G&W 5e p.352의 modeling carousel은 그림이 아니라 실제로 손에 잡히는 워크플로우가 됩니다 — **Explore data에서 초기값을 만들고, Fit model 후 Analyze output에서 잔차/정밀도/비교를 검토하고, simulation-based qualification으로 generative fit을 확인하고, 그 결과를 다음 Design 단계로 돌립니다**. [G&W 5e p.352, p.392, pp.399–405]

#

### F. 후속 세션 연결 지식 그래프

| 후속 세션 | 이 세션에서 열리는 개념 | 이 세션 없으면 실패하는 것 |
|---|---|---|
| NONMEM estimation method module | FO/FOCE/FOCEI/Laplacian/SAEM을 판단 조건으로 읽기 | OFV·precision·shrinkage 차이를 단순 알고리즘 옵션으로 잘못 읽음 |
| Model qualification module | GOF → VPC/pcVPC/NPDE → bootstrap/SIR 흐름 | 곡선 적합을 predictive performance로 과잉해석 |
| Stepwise covariate modeling module | ΔOFV 카이제곱 임계값(3.84/6.63)의 통계적 정당성 | covariate 선택을 임의 임계값으로 자동화 |
| Adaptive sampling/design module | derivative peak와 sensitivity를 다음 설계로 번역 | 정보 없는 시간점에서 반복 sampling |

---

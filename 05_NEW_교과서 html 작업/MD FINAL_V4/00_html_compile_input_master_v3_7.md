# Pre-Sprint — 모델링 철학·용어 — v3.7

> **기호 통일 메타:** 원본 첫 등장 기준에 따라 $Cl$, $V$, $K$, $AUC$, $E_{\max}$, $C_{50}$, $\gamma$, $A_{ss}$, $R_t$, $k_t$, $t_t$ 표기를 유지했습니다. 일반 prose의 Emax/C50는 수식에서는 $E_{\max}$/$C_{50}$로 통일했습니다.

## 임상 장면 — 왜 이 세션이 필요한가

Digoxin은 0.125–0.25 mg 1일 1회로 쓰일 수 있지만, morphine sulfate는 10–50 mg을 하루 최대 6회까지 투여할 수 있습니다 [T pp.4, 7]. 두 약물 모두 치료역이 좁을 수 있다는 표면적 공통점만 보면 “둘 다 조심해서 쓰면 된다”로 끝납니다. 그러나 실제 처방 판단은 용량 숫자가 아니라 **노출-시간 프로파일과 반응-시간 프로파일이 어떻게 어긋나는가**를 읽는 데서 시작됩니다.

## 학습자 안내

**이 핸드아웃 사용법**: 먼저 §1 로드맵으로 네 개의 MUST 개념을 잡고, §2의 M1→M4 카드를 순서대로 읽으면 됩니다. 그다음 §5 혼동쌍 해부(Confusion Pair)와 §7 자기 테스트(Self-Test)로 “개념을 설명할 수 있는지”를 확인하면 됩니다.

**권장 학습 경로**:
1. M1 — 모델링 회전목마(Modeling Carousel): fitting보다 앞선 사고 순서를 확인합니다.
2. M2 — PK/PD 연결(Linkage): 투여 요법(dose regimen)을 노출(exposure)과 반응(response)으로 번역합니다.
3. M3 — $E_{\max}$/$C_{50}$/Hill $\gamma$: 농도-반응 곡선의 천장(ceiling), 효능(potency), 가파름(steepness)을 분리합니다.
4. M4 — 전환(Turnover): 농도 최고점과 효과 최고점이 분리될 때의 지연(delay) 사고를 확인합니다.
5. §5와 §7 — 혼동쌍과 능동 회상(active recall)으로 마무리하면 됩니다.

**그림 참고 사항**: 교과서 그림은 직접 삽입하지 않습니다. 저작권상 원그림 대신 텍스트형 참고 callout으로만 안내합니다. 학습자는 해당 교과서 페이지의 원그림을 따로 확인하면 됩니다.

**학습 마무리 전 확인**: 아래 네 문장을 스스로 말할 수 있어야 합니다.
- 왜 fitting은 모델링 회전목마(Modeling Carousel)의 시작점이 아닌가요?
- 왜 PK 단독 또는 PD 단독으로는 용량 결정(dosing decision)이 불완전한가요?
- 왜 $\gamma$는 단순 지수(exponent)가 아니라 반응 민감도(response sensitivity)의 언어인가요?
- 왜 전환(turnover)에서는 “얼마나 많이”와 “얼마나 빠르게”를 분리해야 하나요?

# Pre-Sprint — 모델링 철학·용어

> **출처 및 범위 노트:** 이 장은 Gabrielsson & Weiner 5e Ch.1, p.1–7과 Rowland & Tozer 5e Ch.1–2, p.3–49를 바탕으로, 모델링의 기본 언어와 전체 workflow를 학습자 관점에서 정리한 입문 장입니다. 세부 수식·page tag·source label은 본문 내 기존 표기를 따릅니다.

# 최신 큐레이션 맵(Updated Curation Map)

이 세션은 두 권의 교과서가 서로 다른 질문에 답하는 진입점입니다. Gabrielsson & Weiner는 **어떤 사고 순서로 모델링할 것인가**를 정합니다. Rowland & Tozer는 **그 모델링 언어를 임상 용량 결정으로 어떻게 번역할 것인가**를 정합니다. 후속 PopPK 세션에서 제어구문(control stream), GOF, 파라미터 해석(parameter interpretation), TDM 판단을 다루기 전에 잠가야 할 기반은 네 개입니다.

## MUST 계층(MUST tier)

| # | 개념 | 출처(Source) | 잠금 판정(Lock) |
|---|---|---|---|
| M1 | 모델링 회전목마(Modeling Carousel) & 5대 기능 장애(dysfunction) | Gabrielsson Ch.1 | 모델링은 fitting이 아니라 질문→설계→실험→EDA(그래프 중심 탐색적 데이터 분석)→fitting→진단의 순환이라는 사고 순서를 고정합니다. |
| M2 | PK/PD 연결(Linkage) & 치료역(Therapeutic Window) | Rowland & Tozer Ch.1 | 투여 요법(dose regimen)을 노출-시간 프로파일(exposure-time profile)과 반응-시간 프로파일(response-time profile)로 번역하는 임상 정량화의 출발점입니다. |
| M3 | $E_{\max}$ / $C_{50}$(최대효과 절반 농도) / Hill $\gamma$(곡선 가파름 계수) | Rowland & Tozer Ch.2 | 농도-반응 관계를 $E_{\max}$, 효능(potency), 가파름(steepness)으로 분해하는 직접 효과(direct-effect) PD 모델의 골격입니다. |
| M4 | 전환(Turnover)(체내 물질의 생성·소실 순환) | Rowland & Tozer Ch.2 | 반응 지연(response delay)과 내인성 시스템의 동적 평형(dynamic equilibrium)을 이해하는 간접 반응(indirect-response) 모델의 선행 개념입니다. |

## CONTEXT 계층 — 압축 흡수

| CONTEXT 개념 | 흡수 위치 | v3.7 처리 |
|---|---|---|
| constant / parameter / variable; primary vs secondary parameter | M1 | primary vs secondary parameter만 1문장으로 유지 |
| NCA vs 구획 모델링(compartmental modeling) | M1 | “질문이 단순하면 NCA, 예측·비선형·PK/PD 정량화에는 모델”로 압축 |
| ADME, 체내 배치(disposition), 초회 통과 손실(first-pass loss), 생체이용률(bioavailability), 장간순환(enterohepatic cycling) | M2 | PK 단계가 노출(exposure)을 만드는 생리학적 연쇄(physiological chain)라는 1문장으로 압축 |
| 투여 경로(route), 제형(dosage form), 순응도(adherence), 변이(variability) | M2 | 치료역(therapeutic window)을 흔드는 현실 세계 입력 요인으로 압축 |
| 혈장/혈청/전혈(plasma/serum/whole blood), 비결합 농도(unbound concentration) | M3 | 반응(response)을 연결할 때 측정 매트릭스(measurement matrix)와 비결합 농도 조건으로 압축 |
| 활성 대사체(active metabolite) / 전구약물(prodrug) / 입체이성질체(stereoisomer) | M3 | “측정한 농도 ≠ 활성 분자일 수 있음”으로 압축 |
| 질병 진행(disease progression), 위약(placebo), 바이오마커/대리 지표(biomarker/surrogate) | M3/M4 | 측정된 반응 해석의 배경으로 압축 |

<!-- SLIDE_START: §1 | title: 세션 헤더와 로드맵 -->

# §1 — 세션 헤더 & 로드맵(Session Header & Roadmap)

**세션 제목**: Pre-Sprint — 모델링 철학·용어  
**핵심 질문**: 모델링은 왜, 언제, 어떤 순서로 해야 하며, 그 결과를 어떻게 임상 용량 결정 언어로 번역해야 하나요?

**핵심 통찰(Big Idea)**: 모델링은 수식 fitting이 아니라 **임상 질문 → 설계 → 실험 → EDA → fitting → 진단**의 순환 사고입니다. PK/PD는 그 순환 안에서 **투여 요법(dose regimen)을 노출-시간 프로파일(exposure-time profile)과 반응-시간 프로파일(response-time profile)로 번역하는 언어**입니다.

## ASCII 레이어 개념 지도

```text
Layer 1 — 무엇인가: 용어와 진단 개념
  Modeling Carousel | PK vs PD | Therapeutic Window | Graded/Quantal Response | Turnover

Layer 2 — 어떻게 계산되는가: 핵심 수식과 관계
  K = Cl/V | AUC = D/Cl | Hill/Emax | kt = Rt/Ass | tt = Ass/Rt = 1/kt

Layer 3 — 언제, 왜 중요한가: 의사결정 연결
  EDA → initial estimates | dose → exposure → response | gamma → titration logic | delay → turnover model
```

🧭 **읽는 순서:**
카드 1 (M1): 왜 fitting부터 시작하면 모델 구조와 초기값이 취약해지는가?  
카드 2 (M2): 용량 숫자는 어떻게 노출-시간과 반응-시간으로 번역되는가?  
카드 3 (M3): 농도-반응 곡선에서 천장, 효능, 가파름은 어떻게 분리되는가?  
카드 4 (M4): 농도 최고점과 효과 최고점이 어긋날 때 무엇을 먼저 의심해야 하는가?

## 지식 그래프 위치

```text
[기초 PK/NCA·선형 1구획] → [이 세션: Modeling Carousel + PK/PD 언어] → [GOF/VPC·구획 PK·TDM·직접/간접 PD·TMDD 하류 모델]
```

## 로드맵(Roadmap)

```text
M1. Modeling Carousel  ⚡ Apex Concept
    ├─ 왜 fitting부터 시작하면 안 되는가
    ├─ EDA가 initial estimate와 model structure를 만든다
    └─ 5대 dysfunction: EDA 경시, formula slavery, software overtrust,
       improper weighting, lack of holistic view

M2. PK/PD Linkage & Therapeutic Window
    ├─ dose regimen → exposure → desired/adverse effects
    ├─ empirical regimen design vs rational PK/PD approach
    └─ therapeutic window: efficacy와 harm 사이의 operating range

M3. Emax / C50 / Hill γ
    ├─ Emax: maximum response
    ├─ C50: potency
    └─ γ: steepness; titration-friendly vs threshold-like response

M4. Turnover
    ├─ steady state는 static state가 아니라 dynamic equilibrium
    ├─ Rt, Ass, kt, tt
    └─ concentration peak와 effect peak가 분리될 때 indirect response를 의심한다
```

**후속 개방**: M1은 GOF와 모델 선별(model selection), M2는 구획 PK(compartmental PK)와 TDM, M3는 직접 효과 PD(direct-effect PD), M4는 간접 반응(indirect-response)/질병 진행(disease progression)/TMDD 하류 모델로 이어집니다.

<!-- SLIDE_START: §2 | title: 개념 해부 카드 -->

# §2 — 개념 해부 카드(Concept Anatomy Cards)

<!-- SLIDE_START: M1 | title: Modeling Carousel & 5대 Dysfunction -->

## Card M1 ⚡ Apex Concept — Modeling Carousel & 5대 Dysfunction [G pp.1–7]

> **거장의 시각**
> 💢 **흔한 오해:** 좋은 fit과 수렴 메시지가 있으면 모델링은 이미 성공했다고 생각합니다.
> ✅ **실제는:** fitting은 6단계 중 5번째이며, 앞의 질문·설계·실험·EDA가 모델 구조와 초기 추정치의 근거를 먼저 만들어야 합니다.
> 🎯 **체화할 단 하나의 직관:** EDA 없는 fitting은 데이터 기반 모델링이 아니라 소프트웨어 기본값과 사용자의 추측으로 출발하는 탐색입니다.

### A. 형식적 정의 + 수식

**모델링 회전목마(Modeling Carousel)**는 성공적 모델링을 위한 순환 워크플로(workflow)다 [G p.4].

| 단계 | 근거/가정 | 산출물 |
|---|---|---|
| 1. 잠정 모델(Tentative model) | 실험 전 사전 가설과 잠정적 시스템 모델 | 무엇을 설명할지에 대한 초기 구조 |
| 2. 설계(Design) | 용량, 채혈 시점, 반응 측정, 대상 집단, 시뮬레이션/CATD | 식별 가능한 데이터를 만들기 위한 계획 |
| 3. 실험 수행(Run experiment) | 설계에 따른 데이터 수집 | 농도·반응·시간 자료 |
| 4. 데이터 탐색(Explore data, EDA) | 농도-시간, 반응-시간, 반응-농도 도표 | 구조, 비선형성, 초기 추정치 후보 |
| 5. 모델 적합(Fit model(s)) | 비선형 회귀로 파라미터와 정밀도 추정 | 추정값, 정밀도, 목적함수 |
| 6. 결과 분석 및 모델 판별(Analyze output & model discrimination) | GOF, 잔차, 파라미터 정밀도, 검증, 경쟁 모델 비교 | 모델 채택·기각 근거 |

G Ch.1의 단순 모델은 용량(dose) $D$를 상수(constant), $V$와 $Cl$을 일차 파라미터(primary parameter), $\hat C$와 $t$를 변수(variable)로 둡니다. $K=Cl/V$, $AUC=D/Cl$, $t_{1/2}=\ln(2)/K$는 일차 파라미터에서 도출되는 이차 파라미터(secondary parameter)입니다 [G pp.1–2].

$$
\underbrace{K}_{\text{소실속도}}=\frac{\underbrace{Cl}_{\text{정화능}}}{\underbrace{V}_{\text{분포공간}}},\quad
\underbrace{AUC}_{\text{총노출}}=\frac{\underbrace{D}_{\text{투여량}}}{\underbrace{Cl}_{\text{정화능}}},\quad
\underbrace{t_{1/2}}_{\text{반감기}}=\frac{\ln(2)}{\underbrace{K}_{\text{소실속도}}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $D$ | amount | 투여된 입력량 | 처방 용량, 투여 오류 |
| $Cl$ | volume/time | 단위 시간당 제거 가능한 가상 부피 | 장기 기능, 효소/수송체 활성, 질병 상태 |
| $V$ | volume | 농도와 체내 양을 연결하는 분포 공간 | 조직 분포, 결합, 체성분 |
| $K$ | time⁻¹ | 1구획에서 농도 감소를 지배하는 소실 속도 | $Cl$ 증가 또는 $V$ 감소 시 증가 |
| $AUC$ | concentration·time | 총 전신 노출 | $D$ 증가 시 증가, $Cl$ 증가 시 감소 |
| $t_{1/2}$ | time | 농도가 절반으로 줄어드는 시간 | $K$ 증가 시 감소 |

**수식 블록 — 1구획 예측 / 관측 오차(Equation block — one-compartment prediction / observation error) [G pp.1–2]**

$$
\underbrace{\hat C}_{\text{예측농도}} =
\overbrace{\frac{\underbrace{D}_{\text{투여량}}}{\underbrace{V}_{\text{분포공간}}}}^{\text{초기스케일}}
\;\overbrace{\exp\left(-\underbrace{\frac{Cl}{V}}_{\text{소실속도}}t\right)}^{\text{시간감소}}
$$

💡 **비유:** $D/V$는 물감 한 방울을 처음 얼마나 큰 물통에 떨어뜨렸는지를 정하고, $\exp(-Kt)$는 시간이 지나며 색이 얼마나 빠르게 옅어지는지를 정합니다.

$$
\underbrace{C}_{\text{관측농도}} = \underbrace{\hat C}_{\text{모델예측}} + \underbrace{\varepsilon}_{\text{잔차}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $\hat C$ | concentration | 모델이 구조와 파라미터로 예측한 농도 | $D$, $V$, $Cl$, $t$에 의해 결정 |
| $C$ | concentration | 실제 관측 농도 | 예측값 + 분석/잔차 변동 |
| $\varepsilon$ | concentration | 관측값과 예측값 사이의 잔차 | 분석 오차, 표본 처리, 모델 미설명 변동 |

> 💡 **EDA가 fitting보다 앞서는 이유** — 비선형 fitting은 초기 추정치와 목적함수 표면의 분지(basin)에 민감하므로, EDA가 초기값의 근거를 만들어야 합니다.
> ⚠️ **헷갈림 방지:** 수렴 메시지는 과학적 타당성 보증서가 아닙니다. 수렴은 알고리즘이 멈췄다는 말이지, 임상 질문에 답했다는 말이 아닙니다.
> 🔑 **최소 복잡도 규칙:** “가장 복잡한 모델”이 아니라 “질문을 답하는 데 필요한 만큼만 복잡한 모델”이 원칙입니다 [G pp.3–4].

### B. 왜 모델링하는가?

G Ch.1의 핵심은 “모델링을 많이 하라”가 아니라 **필요할 때만 하라**입니다. 질문이 생체이용률(bioavailability)이나 총 청소율(total clearance) 같은 노출 요약(exposure summary)이라면 NCA가 충분할 수 있습니다. 반대로 단회 투여(single-dose)에서 반복 투여(multiple-dose)를 예측하거나, 비선형 약동학(nonlinear kinetics)을 다루거나, PK/PD 관계를 정량화해야 한다면 구획/PBPK형 모델이 필요합니다 [G p.4].

| 이 카드에서 다루는 것 | → | 후속 세션으로 이월 | 이유 |
|---|---|---|---|
| 질문에 맞는 모델 복잡도 | → | NONMEM 제어구문, 모델 선별 | 운영 기준과 OFV 판단은 별도 세션 필요 |
| EDA 기반 초기 추정치 | → | GOF/VPC, bootstrap, sensitivity run | fitting 이후 예측 성능은 별도 진단 필요 |
| NCA와 모델링의 경계 | → | 구획 PK와 반복투여 예측 | 단순 요약과 예측 모델의 목적이 다름 |

### C. 구조적 필연성(Structural Necessity)

4단계 EDA는 예쁜 그림을 만드는 단계가 아닙니다. 5단계 fitting에 들어갈 모델 구조와 초기 추정치를 생산하는 단계입니다. G p.5–6은 EDA가 모델 구조와 초기 추정치를 제안해야 하며, 비선형 fitting 알고리즘은 초기 추정치를 필요로 한다고 설명합니다.

G Fig.1.2는 청소율(clearance)과 분포용적(volume)의 파라미터 공간에서 목적 함수 WRSS(가중 잔차 제곱합, weighted residual sum of squares)가 여러 홈(hollow)을 가질 수 있음을 보여 줍니다. 노란 점(yellow point)은 가능한 초기 추정치이고 빨간 점(red point)은 최종 추정치입니다. 출발점이 나쁘면 국소 최솟값(local minimum)으로 갈 수 있고, 좋은 초기 추정치는 전역 최솟값(global minimum)으로 가는 길을 열 수 있습니다 [G p.6].

> 💼 **실무 인사이트:** EDA의 산출물은 도표(plot) 자체가 아니라 “초기 추정치 후보 1표 + 비선형성 유무 1줄”입니다. 용량 보정 도표(dose-normalized plot)가 비선형성을 시사하면, 결론 전에 데이터셋의 용량/시간/사건 코딩 오류 가능성부터 배제합니다.

> 📖 **교과서 그림 참조:** Gabrielsson & Weiner 5e, p.6, Figure 1.2  
> 이 그림은 국소 최솟값(local minimum) 문제를 눈에 보이게 해 줍니다. EDA에서 얻은 초기 추정치(initial estimates)가 장식적 절차가 아니라, fitting 알고리즘이 파라미터 공간(parameter space)의 어느 영역으로 들어갈지를 결정한다는 점을 보여 줍니다.  
> 확인 시점: Card M1, 특히 §C 구조적 필연성(Structural Necessity)을 읽은 뒤 확인하면 됩니다.

### D. 가정과 경계 조건(Assumptions & Boundary Conditions)

모델링 회전목마는 풍부한 데이터셋(rich dataset)과 실험 설계를 전제로 한 사고 순서입니다. 희소 데이터(sparse data)나 실세계 데이터(real-world data)에서는 EDA의 해상도가 떨어질 수 있습니다. 이 경우 “모델이 설명한다”와 “데이터가 구분해 준다”를 분리해서 말해야 합니다.

**5대 기능 장애(Five common dysfunctions)** [G p.4]

| 기능 장애(Dysfunction) | 압축 해석 |
|---|---|
| fitting 전 EDA 경시 | fitting부터 돌리면 모델 구조와 초기 추정치가 빈약해집니다. |
| 수식 맹종(slavery to formulas) | 수식을 외워도 생물학과 데이터가 요구하는 구조를 보지 못합니다. |
| 소프트웨어 과신(too much trust in software) | 수렴 메시지는 과학적 타당성 보증서가 아닙니다. |
| 가중치 오용(improper use of weighting) | 잔차/오차 모델(residual/error model)을 잘못 두면 구조적 판단도 흐려집니다. |
| 총체적 시야 부재(lack of holistic view) | 설계, 분석법, 생물학, 반응 시점을 함께 보지 못합니다. |

### E. 한계(Limitations)와 인지 잠금(Cognitive Lock)

이 장은 NONMEM 수렴 진단(convergence diagnostics)이나 공분산 단계(covariance step) 해석을 가르치는 장이 아닙니다. 따라서 “몇 개 초기 추정치를 써야 하는가”, “OFV 차이가 얼마면 충분한가” 같은 운영 기준은 이 카드에서 다루지 않습니다. 이 카드에서 체화할 메시지는 **서로 다른 초기 추정치(different initial estimates)로 재실행하여 국소 최솟값 여부를 확인해야 한다**는 원칙입니다 [G p.6].

| 인지 층위 | 잠금 문장 |
|---|---|
| 형식적(Formal) | 모델은 반응 변수(response variable)가 예측 변수(predictor)에 어떻게 의존하는지 표현합니다. |
| 그래프적(Graphical) | 농도-시간, 반응-시간, 반응-농도 도표가 구조를 먼저 말합니다. |
| 알고리즘적(Algorithmic) | 비선형 fitting은 초기 추정치와 목적 함수 곡면(objective surface)의 분지(basin)에 민감합니다. |
| 생물학적(Biological) | 모델은 생물학과 수집된 데이터가 이끌어야(drive) 합니다. |
| 실무적(Practical) | fitting 전에 “질문, 설계, EDA, 초기 추정치”가 문서화되어야 합니다. |

**진단 시그니처(Diagnostic signature) [실무 추론]**: **조기 수렴 착각(Premature Convergence Mirage)** — EDA 없이 fitting부터 시작해 수렴은 했지만, 모델 구조와 초기 추정치의 근거가 빈약한 상태.

### F. 제텔카스텐 원자(Zettelkasten Atom)

```yaml
aliases: [Modeling Carousel, EDA-first modeling, local minimum]
tags: [pharmacometrics/modeling, EDA, model-selection]
source: Gabrielsson & Weiner 5e Ch.1 pp.1-7
lock: Fitting is Step 5, not Step 1. EDA produces model structure and initial estimates.
```

### G. Plausible Fallacy — 나비효과 연쇄 [EXPERT_INFERENCE, v3]

**오류:** GOF가 좋게 나왔으니 모델이 옳다고 판단한다.  
**왜 그럴싸한가:** GOF 도표는 적합값(fitted value)이 관측값(observed value)에 가깝다는 사실을 시각적으로 보여 주기 때문에, 검증까지 끝난 것처럼 보입니다.  
**나비효과:** GOF-only 모델 채택 → VPC/예측 성능 진단 생략 → [임상] 검증되지 않은 노출 예측으로 용량 결정 → 치료 실패 또는 독성 위험 증가 → [모델링/규제] 예측 타당성(predictive validity) 부재 지적, deficiency letter, 재분석 요구.

### H. 핵심 요약 박스

> **M1 체화 핵심**
> ① `새 데이터셋을 받았을 때` → 질문·설계·EDA가 모델 구조와 초기 추정치를 결정
> ② `수렴 결과 vs 예측 타당성` → GOF가 아니라 진단·검증 단계가 지배
> ⚡ `좋은 fit = 옳은 모델` → VPC 없이 의사결정으로 직행하면 임상 예측 실패와 규제 재분석으로 이어짐

<!-- SLIDE_START: M2 | title: PK/PD Linkage & Therapeutic Window -->

## Card M2 — PK/PD Linkage & Therapeutic Window [T pp.3–17]

> **앞 카드에서 이 카드로:** M1이 “모델링을 어떤 순서로 할 것인가”를 잠갔다면, M2는 그 모델이 답해야 할 임상 질문을 용량→노출→반응 사슬로 바꿉니다.

> **거장의 시각**
> 용량 숫자만 보고 처방을 판단하면 같은 dose regimen이 왜 다른 효과와 위험을 만드는지 설명하지 못합니다.
> PK/PD 연결로 보면 투여 요법은 노출-시간 프로파일과 반응-시간 프로파일을 만드는 입력 함수로 읽힙니다.

### A. 형식적 정의 + 수식

**약동학(Pharmacokinetics)**: 용량, 제형, 투여 빈도, 투여 경로 같은 입력이 시간에 따른 농도/노출을 어떻게 만드는가.  
**약력학(Pharmacodynamics)**: 농도가 원하는 효과(desired effect)와 이상 반응(adverse effect)을 시간에 따라 어떻게 만드는가 [T pp.4–5].

T Fig.1-3이 보여 주는 핵심은, 농도 대 시간(conc-vs-time)과 농도 대 효과(conc-vs-effect)가 결합되어야 비로소 효과 대 시간(effect-vs-time)이 만들어진다는 것입니다. PK만으로는 “몸 안 농도가 어떻게 변하는가”만 알 수 있습니다. PD만으로는 “농도가 주어졌을 때 반응이 어떻게 변하는가”만 알 수 있습니다. 치료에는 둘의 연결(link)이 필요합니다 [T p.5].

```text
Dose regimen → PK exposure-time profile → PD response-time profile → desired/adverse clinical effects
```

| 파라미터/개념 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| Dose regimen | amount, time | 체내로 들어가는 입력 패턴 | 용량, 투여 간격, 경로, 제형, 순응도 |
| Exposure-time profile | concentration over time | 체내 농도와 노출의 시간 경과 | ADME, 생체이용률, 체내 배치, 초회 통과 손실 |
| Response-time profile | effect over time | 원하는/원치 않는 반응의 시간 경과 | 작용부위 농도, 민감도, 평가변수, 질병 상태 |
| Therapeutic window | exposure range | 효과와 위해 사이의 작동 범위 | 효능 한계, 이상 반응, 변이, 측정 부위 |

**PK 단계 맥락**: ADME, 체내 배치(disposition), 초회 통과 손실(first-pass loss), 생체이용률(bioavailability), 장간순환(enterohepatic cycling)은 용량이 전신 노출(systemic exposure)로 바뀌는 생리학적 연쇄의 구성 요소다 [T pp.26–33].

> 💡 **핵심 번역** — dose는 명령문이 아니라 입력 이력(input history)입니다. 임상 판단은 그 입력이 만든 노출과 반응의 시간 경과를 읽을 때 시작됩니다.
> ⚠️ **헷갈림 방지:** PK와 PD는 반대말이 아닙니다. PK는 입력→농도, PD는 농도→효과이며 두 화살표가 이어져야 dosing decision이 완성됩니다.
> 🔑 **치료역 규칙:** 치료역은 “안전한 용량 범위”라기보다 “유효성과 위해 사이에서 작동하는 노출 범위”로 읽어야 합니다 [T p.6].

### B. 치료역(Therapeutic Window)

치료역(therapeutic window)은 노출이 너무 낮으면 무효 치료(ineffective therapy)가 되고, 너무 높으면 이상 반응(adverse effects)이 증가한다는 전제 위에 놓인 작동 범위(operating range)다 [T p.6].

> 💼 **실무 인사이트:** 실무적으로는 치료역을 “치료 반응 확률이 충분하고 이상 사건 확률이 지나치지 않은 노출 범위”로 읽으면 됩니다. 단, 이 확률 집합 표기는 원문 수식이 아니라 교육용 형식화(formalization)입니다.

| 상황 | 파라미터 변화 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| 노출이 낮음 | 작용부위 농도 부족 | → | 무효 치료 | 투여량, 간격, 순응도, 흡수 문제 점검 |
| 노출이 높음 | 이상 반응 구간 진입 | → | 독성 또는 위해 증가 | 용량 감량, 간격 조정, TDM 고려 |
| 입력 이력 불확실 | 겉보기 변이 증가 | → | PK 변이와 누락 투여 혼동 | 순응도·투여 기록 확인 |

### C. 구조적 필연성(Structural Necessity)

T Ch.1은 경험적 시행착오 요법 설계(empirical trial-and-error regimen design)를 합리적 PK/PD 접근법(rational PK/PD approach)과 대비합니다. 예전에는 용량과 투여 간격을 조정하고 원하는/원치 않는 효과를 관찰하면서 요법을 개선했습니다. 그러나 이 방식만으로는 digoxin과 morphine 요법 차이의 원리를 설명하지 못합니다 [T p.4].

Digoxin은 0.125–0.25 mg 1일 1회로 쓰이는 반면, morphine sulfate는 10–50 mg을 하루 최대 6회까지 투여할 수 있습니다. 두 약물 모두 치료역이 비교적 좁지만, morphine은 빠르게 제거되어 자주 투여가 필요하고, digoxin은 천천히 제거되어 1일 1회가 가능합니다 [T pp.4, 7].

💡 **비유:** 같은 좁은 도로라도 어떤 차는 천천히 오래 머물고, 어떤 차는 빠르게 지나갑니다. 치료역이 좁다는 사실만으로는 운전 방식이 정해지지 않고, 농도-시간의 속도가 투여 간격을 결정합니다.

**핵심 예시 — digoxin 축적/디지탈화 용량(Key example — digoxin accumulation/digitalizing dose) [T p.7]**  
Digoxin을 낮은 1일 용량으로 주면 처음에는 무효할 수 있고, 높은 투여 속도로 유지하면 나중에 독성이 나타날 수 있습니다. 그래서 초기에는 여러 소량 투여로 빠르게 치료 농도에 도달시키고 이후 소량 유지 용량으로 유지하는 디지탈화 용량(digitalizing dose) 논리가 나옵니다.

### D. 임상적 중요성(Why It Matters Clinically)

Rowland & Tozer는 부적절한 약물 사용(inappropriate drug use) 때문에 병원 입원 환자의 약 5%가 입원한다는 예를 듭니다 [T p.4]. 이 통계가 시사하는 바는 단순한 약동학 지식의 유용성이 아닙니다. 핵심 메시지는 **요법 설계의 안전성**입니다.

PK/PD는 약물 설계(drug design), 약물 선택(drug selection), 투여 요법 설계, 임상시험 프로토콜 설계, 데이터 해석, 약물 제품 성능 평가, 개인 맞춤 치료(individualized therapy) 개시에도 쓰인다 [T p.20].

> 📖 **교과서 그림 참조:** Rowland & Tozer 5e, p.5, Figure 1-3  
> 이 그림은 PK와 PD를 서로 분리된 과목처럼 잘못 대응시키는 흔한 오해를 막아 줍니다. 치료적으로 유용한 예측을 하려면 두 관계가 효과-시간 프로파일(effect-time profile)로 연결되어야 한다는 점을 보여 줍니다.  
> 확인 시점: Card M2, 특히 §A 정의(Formal Definition)를 읽은 뒤 확인하면 됩니다.

### E. 한계와 현실 세계의 왜곡(Limitations & Real-World Distortions)

| 현실 세계 왜곡 | 원문 앵커 | → | 임상/모델링 결과 | 조치 |
|---|---|---|---|---|
| 측정 부위 문제(Measured site problem) | 작용 부위 농도는 대개 직접 측정하기 어렵고 혈장이 대리 부위로 쓰임 [T p.6] | → | 혈장 농도와 실제 반응의 불일치 | 작용부위 지연·대리성 명시 |
| 순응도 문제(Adherence problem) | 1일 1회 항고혈압제 코호트에서 1년 말 처방약 지속 비율 약 50% [T p.12] | → | 누락 투여가 겉보기 PK 변이로 흡수 | 투여 이력 확인 |
| 변이 문제(Variability problem) | phenytoin, warfarin S-warfarin, G6PD/primaquine, debrisoquine/CYP2D6, terfenadine/ketoconazole [T pp.10–12] | → | 같은 요법이 같은 노출/반응을 보장하지 않음 | 개체 변이와 상호작용 검토 |
| Warfarin 유전학 교정 | CYP2C9/CYP2C19 다형성과 vitamin K epoxide reductase 기전 언급 [T p.10] | → | PDF 범위 밖 표기 혼입 위험 | VKORC1 표기는 이 범위 원문 표현이 아니므로 사용하지 않음 |

> 💼 **실무 인사이트:** 순응도 모니터링이 약하면 겉보기 PK 변이(apparent PK variability)가 실제 누락 투여(missed dose)의 가공물(artifact)일 수 있습니다. 이때 모델은 환자 생리 차이가 아니라 입력 이력 오류를 변이로 흡수할 수 있습니다.

### F. 제텔카스텐 원자(Zettelkasten Atom)

```yaml
aliases: [PK/PD linkage, therapeutic window, input-response phases]
tags: [clinical-pharmacology/dosing, pharmacometrics/pkpd]
source: Rowland & Tozer 5e Ch.1 pp.3-17; Table 2-1 p.20
lock: Dose regimen is useful only after it is translated into exposure-time and response-time profiles.
```

### G. 핵심 요약 박스

> **M2 체화 핵심**
> ① `용량 결정 질문` → dose regimen이 아니라 exposure-time과 response-time 연결이 결정
> ② `PK 단독 vs PD 단독` → 한쪽만 보면 치료역 안에 머무는 시간을 설명하지 못함
> ⚡ `용량 = 반응` → 순응도·측정 부위·변이를 놓쳐 무효 치료나 이상 반응을 예측하지 못함

<!-- SLIDE_START: M3 | title: Emax / C50 / Hill γ -->

## Card M3 — Emax / C50 / Hill γ [T pp.35–43]

> **앞 카드에서 이 카드로:** M2가 용량을 노출과 반응으로 연결했다면, M3는 그 연결 중 “농도가 주어졌을 때 반응이 어떤 모양으로 변하는가”를 분해합니다.

> **거장의 시각**
> $E_{\max}$, $C_{50}$, $\gamma$를 한 덩어리로 외우면 효능, 천장, 가파름이 서로 뒤섞입니다.
> 세 축을 분리해서 보면 용량 적정, 평가변수 선택, 안전역 해석이 각각 어디서 흔들리는지 보입니다.

### A. 형식적 정의 + 수식

**등급 반응(Graded response)**은 농도가 변할 때 반응 강도(response intensity)가 연속적으로 변하는 반응입니다. Ketamine 예시에서 S(+)-ketamine은 R(−)-ketamine보다 더 낮은 $C_{50}$와 더 높은 최대 반응(maximum response)을 보입니다: S(+) $C_{50}$ ≈ 0.7 mg/L, R(−) $C_{50}$ ≈ 1.8 mg/L [T p.40].

**수식 블록 — Hill/$E_{\max}$ 방정식(Equation block — Hill/$E_{\max}$ equation) [T p.40]**

$$
\underbrace{E}_{\text{예측효과}} =
\frac{\overbrace{\underbrace{E_{\max}}_{\text{효과천장}}\,\underbrace{C^{\gamma}}_{\text{농도구동}}}^{\text{효과상승}}}
{\underbrace{C_{50}^{\gamma}}_{\text{효능기준}}+\underbrace{C^{\gamma}}_{\text{현재농도}}}
$$

💡 **비유:** $E_{\max}$는 엘리베이터가 도달할 수 있는 최고층이고, $C_{50}$는 중간층에 도달하는 데 필요한 농도이며, $\gamma$는 버튼을 조금 눌렀을 때 엘리베이터가 얼마나 급하게 반응하는지를 정합니다.

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $E$ | response unit | 특정 농도에서 예측되는 효과 | 농도, 민감도, 평가변수 |
| $E_{\max}$ | response unit | 도달 가능한 최대 반응 또는 효과 천장 | 약물의 최대 약리 효과, 안전성 한계, 평가변수 정의 |
| $C$ | concentration | 현재 농도 | 투여 요법, PK, 측정 매트릭스 |
| $C_{50}$ | concentration | $E_{\max}$의 50%를 만드는 농도 | 효능, 수용체/표적 민감도, 활성 물질 정의 |
| $\gamma$ | dimensionless | 농도-반응 곡선의 가파름 | 반응 민감도, 협동성, 평가변수 절단 |

**노출-시간 앵커(Exposure-time anchor) [T pp.21–22]**: 경구 단회 투여 프로파일(single oral dose profile)에서 $C_{\max}$는 최대 전신 노출(maximum systemic exposure), $t_{\max}$는 그 시간, $AUC$는 총 전신 노출(total systemic exposure)입니다. Fig.2-1의 예시는 $C_{\max}=96\,\mu g/L$, $t_{\max}=3.0$ hr입니다.

$$
\underbrace{C_{\max}=96\,\mu g/L}_{\text{최고농도}},\quad
\underbrace{t_{\max}=3.0\,hr}_{\text{도달시간}},\quad
\underbrace{AUC}_{\text{총노출}}
$$

> 💡 **천장-효능-가파름 구분** — $C_{50}$이 낮다고 항상 좋은 약이 아닙니다. 같은 효능이라도 $E_{\max}$가 낮으면 충분한 임상 반응에 도달하지 못할 수 있습니다 [T pp.40–43].
> ⚠️ **헷갈림 방지:** $\gamma$는 단순한 곡선 장식이 아닙니다. $C_{50}$ 주변에서 작은 농도 변화가 반응 판단을 얼마나 크게 바꾸는지 정합니다.
> 🔑 **식별 가능성 규칙:** 고원과 저반응 영역 없이 $C_{50}$ 주변 자료만 있으면 $\gamma$ 추정이 모델보다 잡음(noise)을 따라갈 수 있습니다.

### B. $\gamma$가 실제로 바꾸는 것(What $\gamma$ Really Changes)

T p.40은 $\gamma=1$이면 20%→80% 반응에 필요한 농도 범위가 $0.25C_{50}$에서 $4C_{50}$, 즉 16배(16-fold)라고 설명합니다. $\gamma=2$이면 $0.5C_{50}$에서 $2C_{50}$, 즉 4배(4-fold)로 압축됩니다.

| 단계 | 근거/가정 | 수식 |
|---|---|---|
| 완만한 곡선 | $\gamma=1$ | $\underbrace{\gamma=1}_{\text{완만}}:\;\underbrace{C_{20}=0.25C_{50}}_{\text{20\%농도}},\;\underbrace{C_{80}=4C_{50}}_{\text{80\%농도}}$ |
| 가파른 곡선 | $\gamma=2$ | $\underbrace{\gamma=2}_{\text{가파름}}:\;\underbrace{C_{20}=0.5C_{50}}_{\text{20\%농도}},\;\underbrace{C_{80}=2C_{50}}_{\text{80\%농도}}$ |
| 임상 해석 | 20–80% 범위가 16배에서 4배로 압축 | 작은 농도 차이가 더 큰 반응 차이로 바뀜 |

💡 **비유:** 완만한 곡선은 긴 완만한 경사로이고, 가파른 곡선은 짧은 계단입니다. 같은 목적지라도 계단에서는 한 발 차이가 훨씬 크게 느껴집니다.

일반적으로 $\gamma$는 1–3 사이에 있습니다. 그러나 매우 크면 최소 반응과 최대 반응 사이의 농도 범위가 좁아집니다. 그 결과 반응이 전부 아니면 전무(all-or-none)처럼 보일 수 있습니다 [T pp.40–41].

> 💼 **실무 인사이트:** $\gamma$는 단순한 곡선 모양이 아니라 처방 사고를 바꿉니다. $\gamma \approx 1$이면 증상 기반 적정(symptom-based titration)이 상대적으로 자연스럽습니다. 반대로 반응이 가파르거나(steep) 역치형(threshold-like)이면 작은 농도 변화가 임상 사건(clinical event)을 바꿀 수 있습니다.

### C. 실제 데이터 앵커(Real Data Anchors)

**핵심 예시 — propranolol [T p.42]**  
운동 유발 빈맥(exercise-induced tachycardia) 감소율과 비결합 propranolol 농도의 관계는 Hill 방정식에 잘 맞고, $\gamma \approx 1$, $E_{\max}\approx 40\%$, $C_{50}=5.3\,\mu g/L$로 제시됩니다.

**핵심 예시 — alfentanil 이분형 반응(quantal response) [T pp.42–43]**  
Alfentanil은 nitrous oxide 마취 중 만족스러운 반응의 누적 빈도(cumulative frequency)로 평가됩니다. $C_{50}$는 유방(breast) 0.27 mg/L, 하복부(lower abdomen) 0.31 mg/L, 상복부(upper abdomen) 0.42 mg/L 순으로 증가합니다. 이 예시는 $\gamma$를 추정한 등급 곡선이 아닙니다. 즉, 이분형 평가변수(quantal endpoint)에서 반응 확률이 농도와 어떻게 연결되는지 보여 주는 예시입니다.

| 데이터 상황 | 파라미터 변화 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| propranolol 등급 반응 | $\gamma\approx1$, $E_{\max}\approx40\%$, $C_{50}=5.3\,\mu g/L$ | → | 연속 반응의 농도-효과 관계 해석 | Hill 방정식 기반 직접 효과 모델 고려 |
| alfentanil 이분형 반응 | 부위별 $C_{50}$ 0.27→0.31→0.42 mg/L | → | 집단 사건 확률의 농도 기준 해석 | 누적 빈도/확률 프레임 유지 |
| endpoint scale 불일치 | 등급형 반응과 이분형 endpoint 혼재 | → | 서로 다른 용량 결론 가능 | 평가변수 정의를 모델보다 먼저 고정 |

### D. 측정과 분석 경계(Measurement & Assay Boundaries)

총 혈장/혈청 농도(total plasma/serum concentration)에는 결합형과 비결합형 약물이 모두 포함됩니다. 그러나 분포, 소실, PD 반응은 비결합 농도(unbound concentration)에 의존합니다. 다만 비결합 분율(fraction unbound)이 일정하면 총 농도로도 충분할 수 있습니다. 반대로 포화성 결합(saturable binding), 약물 상호작용에 의한 전위(displacement interaction), 신장/간 질환, 수술, 중증 화상, 임신처럼 결합이 변하는 조건에서는 비결합 농도 측정이 중요해집니다 [T p.21].

**화학적 물질 경계(Chemical entity boundary)**: 라세미체(racemate), 입체이성질체(stereoisomer), 활성 대사체(active metabolite), 전구약물(prodrug)에서는 “측정한 총 모체 농도(total parent concentration)”가 실제 활성 물질(active moiety)을 대표하지 못할 수 있습니다. Acenocoumarol, methylphenidate, aspirin/salicylic acid 예시는 분석 특이성(assay specificity)이 PK/PD 연결을 좌우합니다 [T pp.23–25].

> 💼 **실무 인사이트:** 용량 범위가 $C_{50}$ 주변에만 몰려 있고 고원(plateau) 정보가 없으면 $\gamma$를 자유롭게 추정하기보다 절약적 가정(parsimonious assumption)을 먼저 검토합니다. “$\gamma$를 추정했다”는 사실보다 “데이터가 $\gamma$를 식별(identify)할 수 있는가”가 먼저입니다.

> 📖 **교과서 그림 참조:** Rowland & Tozer 5e, p.41, Figure 2-16  
> 이 그림은 $\gamma$를 추상적인 지수(exponent)가 아니라 반응 민감도(response sensitivity)의 눈에 보이는 변화로 바꾸어 줍니다. 가파름(steepness)이 달라질 때 같은 $C_{50}$라도 매우 다르게 작동할 수 있음을 보여 줍니다.  
> 확인 시점: Card M3, 특히 §B $\gamma$가 실제로 바꾸는 것(What $\gamma$ Really Changes)을 읽은 뒤 확인하면 됩니다.

### E. 한계(Limitations)와 진단 잠금(Diagnostic Lock)

임상적 $E_{\max}$는 약리학적 최대치(pharmacological maximum)보다 낮을 수 있습니다. 예를 들어 심박수를 올리는 약물에서는 심혈관계가 먼저 악화될 수 있습니다. 그러면 약리학적 최대치에 도달하기 전에 안전성 한계가 옵니다. 따라서 작용제(agonist)의 $E_{\max}$는 길항제(antagonist)보다 임상적으로 정의하기 어렵습니다 [T p.41].

Fig.2-19의 메시지는 노출 지표(exposure metric) 선택에도 적용됩니다. 만성 치료(chronic therapy)에서는 최소 농도 이상 유지 기간(duration above a minimum concentration)이 중요할 수 있고, 두통 완화처럼 빠른 효과가 목적이면 $C_{\max}$와 $t_{\max}$가 더 중요할 수 있으며, 어떤 경우에는 총 $AUC$가 더 관련 있을 수 있습니다 [T p.44].

| 진단 항목 | 잠금 문장 |
|---|---|
| 등급 반응(Graded response) | 농도 변화가 반응 강도의 연속 변화로 이어집니다. |
| 이분형 반응(Quantal response) | 개체 수준 평가변수는 전부 아니면 전무(all-or-none)이며, 집단 수준 누적 빈도로 농도-반응을 봅니다. |
| 평가변수 함정(Endpoint trap) | 약리적 반응은 등급형인데 임상 평가변수가 역치로 절단되어 이분형처럼 분석될 수 있습니다 [T p.43]. |
| 진단 시그니처(Diagnostic signature) [실무 추론] | **Hill $\gamma$ 식별 가능성 붕괴(Hill $\gamma$ Identifiability Collapse)** — 데이터 범위가 고원과 저반응 영역을 충분히 포함하지 못해 $\gamma$ 추정이 모델보다 잡음(noise)을 따라가는 상태. |

### F. 제텔카스텐 원자(Zettelkasten Atom)

```yaml
aliases: [Emax, C50, Hill equation, graded response, quantal response]
tags: [pharmacometrics/pd, exposure-response]
source: Rowland & Tozer 5e Ch.2 pp.35-43
lock: Emax is ceiling, C50 is potency, gamma is steepness; endpoint type decides how response should be modeled.
```

### G. 핵심 요약 박스

> **M3 체화 핵심**
> ① `농도-반응 곡선 해석` → $E_{\max}$, $C_{50}$, $\gamma$의 분리가 결정
> ② `등급형 반응 vs 이분형 endpoint` → 평가변수 척도가 모델 프레임을 지배
> ⚡ `$C_{50}$만 보고 효능 판단` → 천장·가파름·식별 가능성을 놓쳐 용량 적정과 규제 보고가 흔들림

<!-- SLIDE_START: M4 | title: Turnover: Pool Size · Rate · Fractional Rate · Time -->

## Card M4 — Turnover: Pool Size · Rate · Fractional Rate · Time [T pp.44–46]

> **앞 카드에서 이 카드로:** M3가 농도와 반응의 현재 순간 관계를 설명했다면, M4는 반응이 시간상 늦게 나타나는 이유를 내인성 풀의 생성·소실 언어로 설명합니다.

> **거장의 시각**
> 지연 반응을 모두 분포 지연이나 Hill 곡선 문제로 해석하면, 내인성 시스템이 천천히 바뀌는 구조를 놓칩니다.
> 전환 관점으로 보면 정상 상태는 정지 상태가 아니라 입력과 출력이 같아 풀 크기가 일정하게 보이는 동적 평형입니다 [T p.45].

### A. 형식적 정의 + 수식

전환(turnover)은 내인성 물질/시스템이 정상 상태에 있으면서 계속 갱신(renewal)되고 소실(elimination)되는 현상입니다. 경구 항응고제(oral anticoagulants), 항고지혈증제(antihyperlipidemics), 요산 배설 촉진제(uricosuric agents), epoetin alfa는 모두 내인성 화합물/시스템의 생성(formation) 또는 소실을 바꿔 지연 반응을 만들 수 있습니다 [T p.45].

**수식 블록 — 전환 관계식(Equation block — turnover relationships) [T p.45]**

$$
\underbrace{k_t}_{\text{분획속도}} = \frac{\underbrace{R_t}_{\text{전환량}}}{\underbrace{A_{ss}}_{\text{풀크기}}},\quad
\underbrace{t_t}_{\text{전환시간}} = \frac{\underbrace{A_{ss}}_{\text{풀크기}}}{\underbrace{R_t}_{\text{전환량}}},\quad
\underbrace{t_t}_{\text{전환시간}}=\frac{1}{\underbrace{k_t}_{\text{분획속도}}}
$$

💡 **비유:** $R_t$는 하루에 드나드는 물의 리터 수이고, $A_{ss}$는 저수지 크기입니다. 큰 저수지에서는 하루 유입량이 커 보여도 전체 저수지가 갈아엎어지는 속도는 느릴 수 있습니다.

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $A_{ss}$ | amount | 정상 상태 풀 크기(pool size at steady state) | 체내 저장량, 피드백, 질병 상태 |
| $R_t$ | amount/time | 단위 시간당 전환 속도(turnover rate) | 생성률, 소실률, 환경/생리 조건 |
| $k_t$ | time⁻¹ | 풀 크기 대비 분획 전환 속도(fractional turnover rate) | $R_t$ 증가 또는 $A_{ss}$ 감소 시 증가 |
| $t_t$ | time | 평균 전환 시간(turnover time) | $k_t$ 증가 시 감소 |

> 💡 **동적 평형** — steady state는 “아무 일도 일어나지 않음”이 아니라, 들어오는 속도와 나가는 속도가 같아 겉으로 일정해 보이는 상태입니다.
> ⚠️ **헷갈림 방지:** $R_t$가 크다고 과정이 빠르다고 단정하면 안 됩니다. 풀 크기 $A_{ss}$로 나눈 $k_t$와 그 역수 $t_t$가 속도 감각을 더 직접적으로 줍니다.
> 🔑 **지연 반응 규칙:** 농도 최고점과 효과 최고점이 분리되면 직접 효과 Hill만으로 충분한지 먼저 의심하고 전환/지연 구조를 검토합니다.

### B. 핵심 예시(Key Examples)

| 예시 | 관찰 | → | 해석 | 조치 |
|---|---|---|---|---|
| Warfarin [T p.8] | Warfarin sodium 1.5 mg/kg 단회 경구 투여 후 혈장 농도는 빠르게 상승하지만 prothrombin complex activity 반응은 느리게 변함 | → | 농도-시간만으로 반응-시간을 설명할 수 없음 | 반응 지연 구조 고려 |
| Paclitaxel [T pp.8–9] | 체내에서 약 2일 내 제거되지만 백혈구 수 변화는 느리고 최저점은 1주 이후, 회복은 약 3주 | → | 전환 구동 반응(turnover-driven response)의 전형적 시그니처 | 내인성 시스템 변화로 해석 |
| 총 체수분 [T pp.45–46] | 약 42 L, 평균 전환 속도 2.5 L/day, $k_t=0.06$ day⁻¹, $t_t=17$ days | → | 큰 양이 오가도 과정은 느릴 수 있음 | $R_t$보다 $k_t$/$t_t$ 확인 |
| 사막 환경 [T pp.45–46] | 풀 크기가 거의 일정해도 $R_t=21$ L/day, $k_t=0.5$ day⁻¹, $t_t=2$ days | → | 풀 크기가 같아도 전환 속도와 시간은 크게 달라짐 | 환경/생리 조건 반영 |

💡 **비유:** Warfarin과 paclitaxel의 반응 지연은 스위치를 켰는데 방 전체 온도가 늦게 바뀌는 상황과 비슷합니다. 스위치 자체는 빠르게 작동해도, 바뀌어야 할 시스템 풀이 크거나 느리면 효과 peak가 늦어집니다.

### C. 구조적 필연성(Structural Necessity)

M3는 농도와 반응의 즉시적 또는 준정상(quasi-steady) 관계를 다루지만, M4는 측정된 반응이 내인성 풀의 변화를 반영할 때 필요합니다. 판단 기준은 단순합니다. **효과 최고점 시간이 농도 최고점 시간과 분리되어 있으면 직접 효과 Hill만으로 충분한지 의심해야 합니다**.

> 💼 **실무 인사이트:** 전환 모델링에서 더 중요한 질문은 “$R_t$, $k_t$, $t_t$ 중 무엇을 외웠는가”가 아닙니다. 핵심 질문은 “이 시스템에서는 풀 크기가 보존되는가, 분획 전환이 보존되는가, 아니면 전환 속도 자체가 바뀌는가”입니다. 체수분 예시는 풀 크기가 피드백으로 유지될 수 있음을, 콜레스테롤/백혈구 예시는 풀 크기 자체가 변할 수 있음을 각각 보여 줍니다 [T p.46].

### D. 경계와 범위(Boundaries)

이 장은 간접 반응 ODE 코딩(indirect response ODE coding)을 제공하지 않습니다. 이 카드에서 체화할 것은 수식 템플릿이 아니라 전환 파라미터 간 관계와 지연 반응의 원인입니다. ODE, KIN/KOUT, 기저선 파라미터화(baseline parameterization)는 후속 PD 모델링 세션으로 이연합니다.

| 이 카드에서 다루는 것 | → | 후속 세션으로 이월 | 이유 |
|---|---|---|---|
| $A_{ss}$, $R_t$, $k_t$, $t_t$의 관계 | → | 간접 반응 ODE | 실제 생성/소실 항 코딩은 별도 세션 필요 |
| 농도 peak와 효과 peak의 분리 | → | hysteresis, effect compartment, turnover model | 지연 원인 구분이 필요 |
| 총 체수분 전환 예시 | → | 생리학적 feedback 모델 | pool 보존과 rate 변화 해석을 확장 |

> 💼 **실무 인사이트:** 희소 반응-시간 데이터(sparse response-time data)에서 입력과 출력을 동시에 자유롭게 추정하면 파라미터가 서로 보상할 수 있습니다. 먼저 기저선(baseline), 최고점 시점(peak timing), 회복 시점(recovery timing)을 보고 어떤 전환 구성 요소가 데이터로 식별 가능한지 판단합니다.

### E. 진단 잠금(Diagnostic Lock)

- **전환 속도(turnover rate)**가 크다고 과정이 빠른 것은 아닙니다. 풀 크기가 크면 큰 양이 오가도 분획 전환은 느릴 수 있습니다.
- **분획 전환 속도(fractional turnover rate)**와 **전환 시간(turnover time)**이 과정 속도를 더 직접적으로 말합니다.
- **진단 시그니처(Diagnostic signature) [실무 추론]**: **전환-PD 오귀인(Turnover-PD Mis-attribution)** — 지연 반응을 PK 분포 지연이나 Hill $\gamma$ 문제로만 설명하려는 상태.

### F. 제텔카스텐 원자(Zettelkasten Atom)

```yaml
aliases: [Turnover, pool size, fractional turnover rate, turnover time]
tags: [pharmacometrics/indirect-response, physiology/dynamic-equilibrium]
source: Rowland & Tozer 5e Ch.2 pp.44-46
lock: Steady state is dynamic equilibrium; delayed response often means the measured system is turning over.
```

### G. 핵심 요약 박스

> **M4 체화 핵심**
> ① `농도 peak와 효과 peak가 분리될 때` → 전환/지연 구조가 판단을 지배
> ② `$R_t$가 큼 vs 과정이 빠름` → $k_t$와 $t_t$가 실제 속도 감각을 지배
> ⚡ `지연 반응 = poor fit 또는 분포 지연` → 내인성 풀 변화를 놓쳐 간접 반응 모델 채택 근거를 잃음

## §2 요약 — 30초 진단 격자(30-Second Diagnostic Grid)

새 PK/PD 데이터셋을 처음 받은 30초에는 네 개 렌즈를 동시에 켜야 합니다.

| 렌즈(Lens) | 먼저 볼 것 | 즉시 판단할 것 |
|---|---|---|
| M1 | 용량 수준, 채혈 밀도, 농도-시간 도표 | EDA가 모델 구조와 초기 추정치를 줄 수 있는가? |
| M2 | 요법, 투여 경로, 순응도, 측정 부위 | 용량→노출→반응 사슬에서 빠진 연결이 있는가? |
| M3 | 고원, $C_{50}$ 주변 범위 포함 여부, 평가변수 유형 | $E_{\max}$/$C_{50}$/$\gamma$를 식별할 수 있는가, 평가변수가 등급형인가 이분형인가? |
| M4 | 농도 최고점 vs 효과 최고점 시점 | 직접 효과 모델로 충분한가, 전환/지연 구조가 필요한가? |

이 격자의 목적은 제어구문(control stream)을 바로 쓰게 만드는 것이 아닙니다. 어떤 모델을 선택할 근거가 데이터에 있는지 먼저 묻는 것입니다.

<!-- SLIDE_START: §5 | title: 혼동쌍 해부 -->

# §5 — 혼동쌍 해부(Confusion Pair Dissection)

## 혼동쌍 1 — 약동학(Pharmacokinetics) vs 약력학(Pharmacodynamics)

| 비교 기준 | 개념 A: 약동학(Pharmacokinetics) | 개념 B: 약력학(Pharmacodynamics) |
|---|---|---|
| 단위 / 차원 | 혈장/혈청/전혈 농도, $AUC$, $C_{\max}$, $t_{\max}$ | 원하는/원치 않는 반응, 바이오마커, 임상 평가변수 |
| 수식 내 위치 (분자/분모/지수) | 입력 → 농도-시간 축 | 농도 → 효과-시간 축 |
| 변화 원인 (생물학적/병적) | 흡수, 분포, 대사, 배설, 투여 이력 | 작용부위 민감도, 평가변수, 생리/질병 상태 |
| 혼동 시 임상 결과 | 노출(exposure)을 용량(dose)과 동일시 | 반응을 농도 없이 직접 용량과 연결 |

**잠금(Lock)**: PK와 PD는 반대말이 아닙니다. 치료적으로 유용한 예측은 둘이 연결(link)될 때 비로소 가능합니다 [T p.5].

**⚡ 기억 고리 (Memory Hook)**: PK는 *입력 → 농도* 의 화살표이고 PD는 *농도 → 효과* 의 화살표입니다. 두 화살표는 **같은 선상의 앞뒤 화살표**이지 좌우의 반대 화살표가 아닙니다. 따라서 한쪽 화살표만 그리면 용량-효과 사슬이 끊겨 임상 의사결정이 멈춥니다 [T p.5].

## 혼동쌍 2 ⚡ 치명적 타격(Critical Blow) 적용 — 등급 반응(Graded Response) vs 이분형 반응(Quantal Response)

| 비교 기준 | 개념 A: 등급 반응(Graded response) | 개념 B: 이분형 반응(Quantal response) |
|---|---|---|
| 단위 / 차원 | 반응 강도가 연속적으로 변함 | 개체 평가변수는 전부 아니면 전무(all-or-none), 집단 수준은 누적 빈도/확률 |
| 수식 내 위치 (분자/분모/지수) | Hill/$E_{\max}$로 연속 반응을 설명 | 누적 빈도/확률로 사건을 설명 |
| 변화 원인 (생물학적/병적) | ketamine 반응, propranolol 심박수 감소 | alfentanil 만족스러운 마취 반응 |
| 혼동 시 임상 결과 | 연속 VAS 같은 반응 크기를 설명 | 이분형 endpoint를 등급 곡선처럼 읽으면 평가변수 정의와 모델 프레임이 불일치 |

**치명적 타격(Critical Blow) [교육용 가상 시나리오]**: 임상시험 프로토콜의 일차 평가변수(primary endpoint)가 “24시간 내 ≥50% 통증 감소: 예/아니오” 같은 이분형 평가변수인데, 모델러가 연속 VAS 점수를 등급형 Hill 모델로만 분석하면, 통계학자의 이진 평가변수 분석과 모델러의 노출-반응 분석이 서로 다른 용량을 지지할 수 있습니다. 문제는 Hill 방정식 자체가 아닙니다. 문제는 **평가변수 척도(endpoint scale)와 모델링 프레임워크의 불일치**입니다.

> **실패 양식(Failure Mode) — [CRUCIBLE_DERIVED]**
> 이분형 자료를 개체별 등급 곡선처럼 읽으면 Hill 방정식의 문제가 아니라 평가변수 정의의 문제가 됩니다. 먼저 개체 수준 반응 크기인지, 집단 수준 발생 확률인지 분리해야 합니다.

## 혼동쌍 3 — 전환 속도(Turnover Rate) vs 분획 전환 속도(Fractional Turnover Rate)

| 비교 기준 | 개념 A: 전환 속도 $R_t$ | 개념 B: 분획 전환 속도 $k_t$ |
|---|---|---|
| 단위 / 차원 | amount/time | time⁻¹ |
| 수식 내 위치 (분자/분모/지수) | $k_t=R_t/A_{ss}$의 분자, $t_t=A_{ss}/R_t$의 분모 | $t_t=1/k_t$의 분모 |
| 변화 원인 (생물학적/병적) | 생성률, 소실률, 환경/생리 조건 | $R_t$와 $A_{ss}$의 비율 변화 |
| 혼동 시 임상 결과 | 2.5 L/day처럼 큰 값만 보고 빠른 과정으로 오해 | 0.06 day⁻¹, 전환 시간 17 days가 느린 과정임을 보여 줌 |

**잠금(Lock)**: $R_t$만 보면 큰 풀의 느린 전환을 빠른 과정으로 오해할 수 있습니다. 속도는 $k_t$와 $t_t$가 더 잘 말합니다 [T pp.45–46].

<!-- SLIDE_START: §7 | title: 자기 테스트 -->

# §7 — 자기 테스트: 능동 회상 모듈(Self-Test: Active Recall Module)

## Q1. 모델링 회전목마에서 fitting은 몇 번째 단계이며, 왜 그 앞 단계가 중요한가?

**기대 답안(Expected answer)**: fitting은 5단계입니다. 4단계 EDA가 모델 구조와 초기 추정치를 제안하고, 비선형 fitting 알고리즘은 초기 추정치에 민감하기 때문입니다 [G pp.5–6].

## Q2. NCA가 충분한 질문과 구획 모델(compartmental model)이 필요한 질문을 하나씩 들어라.

**기대 답안(Expected answer)**: 생체이용률 또는 총 청소율 요약이 목적이면 NCA가 충분할 수 있습니다. 단회 투여 데이터로 반복 투여 결과를 예측하거나 비선형 약동학 또는 PK/PD 관계를 정량화하려면 모델이 필요합니다 [G p.4].

## Q3. 치료역(therapeutic window)을 용량이 아니라 노출 관점에서 설명하라.

**기대 답안(Expected answer)**: 너무 낮은 노출은 무효 치료로, 너무 높은 노출은 이상 반응 증가로 이어지며, 둘 사이에서 치료 반응을 얻고 과도한 이상 반응을 피하는 노출 범위가 치료역입니다 [T p.6].

## Q4. Digoxin과 morphine 요법 차이를 “투여 빈도 차이”가 아니라 PK/PD 원리로 설명하라.

**기대 답안(Expected answer)**: 두 약물 모두 좁은 치료역을 가질 수 있지만 morphine은 빠르게 제거되어 자주 투여가 필요하고, digoxin은 천천히 제거되어 1일 1회가 가능합니다. Digoxin은 빠른 도달과 유지가 분리되어 디지탈화 용량 + 유지 용량(maintenance dose) 논리가 나옵니다 [T pp.4, 7].

## Q5. $\gamma=1$과 $\gamma=2$에서 20–80% 반응 농도 범위는 어떻게 다른가?

**기대 답안(Expected answer)**: $\gamma=1$이면 $0.25C_{50}$에서 $4C_{50}$까지 16배, $\gamma=2$이면 $0.5C_{50}$에서 $2C_{50}$까지 4배다 [T p.40].

## Q6. Propranolol과 alfentanil 예시가 각각 가르치는 것은 무엇인가?

**기대 답안(Expected answer)**: Propranolol은 비결합 농도와 등급 반응이 Hill 방정식으로 설명되는 예시이며 $\gamma\approx1$, $E_{\max}\approx40\%$, $C_{50}=5.3\,\mu g/L$다. Alfentanil은 이분형 반응에서 $C_{50}$가 집단 사건 확률(population event probability)의 기준이 됨을 보여 준다 [T pp.42–43].

## Q7. 농도 최고점과 효과 최고점이 분리되어 있을 때, 어떤 사고가 켜져야 하는가?

**기대 답안(Expected answer)**: 직접 효과 Hill만으로 충분한지 의심하고 전환/지연 구조를 고려해야 합니다. Warfarin과 paclitaxel은 농도-시간과 반응-시간이 분리되는 예시입니다 [T pp.8–9].

## Q8. $R_t=2.5$ L/day인 총 체수분 전환이 왜 “빠른 과정”이라고 단정할 수 없는가?

**기대 답안(Expected answer)**: 풀 크기가 42 L이므로 분획 전환 속도는 0.06 day⁻¹이고 전환 시간은 17 days입니다. 양/시간이 커도 풀 대비 분획이 작으면 과정은 느리다 [T pp.45–46].

## Q9. Fig.2-19의 두 시나리오가 노출 지표 선택에 주는 메시지는 무엇인가?

**기대 답안(Expected answer)**: 같은 $C_{\max}$/$t_{\max}$라도 감소 속도가 다르면 $AUC$와 유지 기간이 달라질 수 있고, 같은 $AUC$라도 입력 속도가 다르면 $C_{\max}$와 $t_{\max}$가 달라집니다. 어떤 지표가 중요한지는 임상 목표와 노출-반응 관계에 따라 달라집니다 [T p.44].

<!-- SLIDE_START: §8 | title: 메타프레임과 큰 그림 -->

# §8 — 메타프레임 & 큰 그림(Meta-Frame & Big Picture)

## A. 위치(Positioning)

이 세션의 목표는 “PK/PD 용어 암기”가 아니라 **후속 모델링 판단의 언어를 잠그는 것**입니다. M1은 사고 순서를 정합니다. M2는 임상 목적 함수를 정합니다. M3는 농도-반응 형태를 정하고, M4는 시간 지연과 내인성 시스템을 해석합니다.

## B. 의존 관계(Dependencies)

| 후속 세션 | 이 세션에서 열리는 개념 | 이 세션 없으면 실패하는 것 |
|---|---|---|
| GOF/진단/VPC | M1: fitting은 Step 5, 진단은 Step 6 | 소프트웨어 출력을 모델 타당성(model validity)으로 오해 |
| 구획 PK/TDM | M2: 용량→노출→반응 번역 | 농도-시간 곡선을 임상 반응과 분리 |
| 직접 효과 PD/노출-반응 | M3: 천장-효능-가파름, endpoint type | 효능, 천장, 가파름, 평가변수 유형을 한 덩어리로 오해 |
| 간접 반응/질병 진행/TMDD 하류 | M4: 지연 반응과 turnover | 지연 반응을 단순 분포 지연이나 부적합으로만 오해 |

## C. 전문가 해석 지점(Professional Lock) — [EXPERT_INFERENCE, v3]

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| 질문 없이 fitting 시작 | 모델 구조, initial estimate | → | 목적 없는 출력과 주관적 모델 선별 | 질문 기반 workflow 문서화 |
| 용량과 반응을 직접 연결 | exposure-time, response-time | → | PK 변이와 PD 변이의 층위 혼동 | 용량→노출→반응 좌표에서 변이 위치 식별 |
| $C_{50}$만 보고 노출-반응 해석 | $E_{\max}$, $C_{50}$, $\gamma$ | → | 천장과 가파름 정보 상실 | 3축과 endpoint type 함께 보고 |
| 농도-효과 지연을 부적합으로 처리 | $A_{ss}$, $R_t$, $k_t$, $t_t$ | → | 간접 반응 모델 채택 근거 상실 | 농도 peak와 효과 peak의 시간 차이 먼저 기술 |

이 세션의 원리를 구조적으로 내재화한 계량약리학자(pharmacometrician)가 새 데이터셋 앞에서 갖는 것은 다음 네 개입니다.

1. **모델링은 질문 기반 워크플로(question-driven workflow)입니다**: 질문 없이 시작하는 fitting은 답 없는 수식입니다. 데이터를 받는 순간 “무엇을 결정하기 위한 모델인가”를 먼저 쓸 수 있어야 합니다.
2. **PK/PD의 핵심 번역 좌표**: 용량 → 노출 → 반응. 이 세 좌표 사이 어디에서 개체간 변이(IIV)가 생기는지 식별하는 것이 거장의 첫 진단입니다.
3. **$E_{\max}$/Hill은 “천장-효능-가파름”의 3축 문법입니다**: 이 셋을 분리하지 못하면 노출-반응 해석이 무너집니다. $C_{50}$만 보고하는 보고서는 천장과 가파름 정보를 버린 것입니다.
4. **전환은 “지연된 상태”의 첫 번째 문법입니다**: 반응이 늦는 이유가 분포 지연(distribution lag)인지 내인성 시스템 역학(endogenous system dynamics)인지를 구분하는 관문입니다.

## 출력 후 자가검증 체크리스트

| 항목 | 기준 | 결과 |
|---|---|---|
| SLIDE_START 개수 | §섹션수 + 카드수 합산 | 9개 |
| 카드당 callout 합계 ≤ 6 | 전체 카드 | ✓ |
| [E] 박스 존재 | 모든 §2 카드 | ✓ |
| [D] 거장의 시각 존재 | 모든 §2 카드 | ✓ |
| [L] 파라미터 표 존재 | Apex 카드 + 정의 수식 카드 | ✓ |
| §5 혼동 쌍 표 행 순서 고정 (4행) | §5 전체 | ✓ |
| 기호 일관성 | 첫 등장 기준 통일 | ✓ |
| PART B 흔적 없음 | 전체 | ✓ |
| 수치 anchor 보존 | Compound A 등 원본 수치 | ✓ |
| [M] 나비효과 이중 종착점 | Apex 카드 전체 | ✓ |

> **QC 보충:** 원본 PART A에는 Compound A 수치 anchor가 없고, digoxin/morphine, ketamine, propranolol, alfentanil, warfarin, paclitaxel, total body water 수치 anchor가 보존되었습니다.

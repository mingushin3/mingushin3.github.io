# Pre-Sprint — 모델링 철학·용어 (Remastered Edition)

> **이 자료의 사용법.** 외울 것이 아니라 **데이터셋 앞에 앉았을 때 머릿속에서 자동으로 돌아가야 할 회로**임. 처음부터 끝까지 한 번 읽고, 다음 데이터셋을 받았을 때 §3의 "30초 체크리스트"가 입에서 나오면 통과임.

---

## 들어가며 — 임상 장면 하나가 모든 것을 정리해줌

진료실에서 **digoxin**(강심배당체) 한 명, **morphine sulfate**(오피오이드) 한 명이 처방됨. 둘 다 "치료역이 좁은 약"이라고 같은 카테고리로 묶이는 약물임. 그런데 처방 빈도가 정반대임:

- **Digoxin**: 0.125–0.25 mg을 **하루 한 번**
- **Morphine**: 10–50 mg을 **하루 최대 6번**

[Rowland & Tozer, *Clinical Pharmacokinetics and Pharmacodynamics: Concepts and Applications*, 5th ed., Ch.1, pp.4, 7]

여기서 "둘 다 조심해서 쓰면 돼" 라고 묶으면 끝장임. 왜 한쪽은 1일 1회고 다른 쪽은 하루 6번인지, 이유를 처방 의사가 입으로 못 말하면 환자 안전이 통째로 흔들리는 거임.

핵심을 미리 까놓고 들어감 — **치료역의 폭이 투여 빈도를 정하는 게 아님. 노출-시간 곡선의 속도가 정함.** Morphine은 빠르게 빠지니까 자주 줘야 하고, digoxin은 천천히 빠지니까 1일 1회면 됨. 같은 "narrow window"라도 PK 속도가 다르면 처방 전략이 완전히 달라짐.

이 한 장면이 이번 세션 전체의 척추임. 우리가 다룰 네 카드가 결국 다 이 질문을 풉:

1. **(M1)** 모델링은 fitting 버튼이 아니라 사이클임 — 왜 EDA부터 안 보면 망하는가?
2. **(M2)** 용량은 그 자체로 처방이 아님 — exposure-time과 response-time 두 곡선으로 번역해야 함
3. **(M3)** 농도-반응은 한 덩어리가 아니라 세 축(천장·효능·가파름)으로 분리됨
4. **(M4)** 농도 peak ≠ 효과 peak이면, 약물이 아니라 **시스템이 천천히 바뀌고 있는 중**임

이 네 가지를 손에 잡으면 박사과정 PopPK·TDM·노출-반응 모델링 어디서든 "내가 지금 뭘 하고 있는가"를 입으로 말할 수 있게 됨.

---

## §1. 한눈에 지도

```text
              [ Dose Regimen ]
                    │
                    │  (M2: PK — 흡수/분포/대사/배설)
                    ▼
            [ Exposure-Time Profile ]
                    │
                    │  (M3: PD — Emax/C50/γ)
                    ▼
            [ Response-Time Profile ]
                    │
                    │  (M4: Turnover — 시스템이 늦게 따라옴)
                    ▼
         [ Desired/Adverse Clinical Effect ]

       ↑ 이 모든 사슬을 (M1: Modeling Carousel) 6단계 사고 순서로 풀어냄
```

| Card | 무엇을 잡는가 | 출처 |
|---|---|---|
| **M1** ⚡ Apex | 모델링 = 6단계 순환 사고 (fitting은 5단계일 뿐) | G&W 5e, Ch.1 (pp.3–7) |
| **M2** | dose regimen을 exposure-time + response-time으로 번역 | R&T 5e, Ch.1 (pp.3–17) |
| **M3** | 농도-반응을 천장·효능·가파름 세 축으로 분리 | R&T 5e, Ch.2 (pp.35–43) |
| **M4** | 농도 peak ≠ 효과 peak인 이유 = 내인성 시스템 turnover | R&T 5e, Ch.2 (pp.44–46) |

후속 세션이 여기서 갈라짐 — M1 → GOF/VPC/NPDE/CWRES/Bayesian-MAP/**PopPK**, M2 → 구획 PK/TDM/소아·비만 covariate, M3 → 직접 효과 PD/effect compartment, M4 → 간접 반응(IDR)/질병 진행/TMDD.

---

## §2. 네 카드, 한 흐름으로 꿰기

<!-- SLIDE_START: M1 | title: Modeling Carousel & 5대 Dysfunction -->
<!-- SECTION_CORE: SC-03 -->

## Card M1 ⚡ — Modeling Carousel: 모델링은 버튼이 아니라 사이클임

### A. 처음 30초의 함정 — "수렴 떴고 GOF 깔끔하니까 끝"

보고서 회의에서 제일 자주 보는 자기기만임. NONMEM이 `MINIMIZATION SUCCESSFUL` 띄웠다고 모델링 끝난 거 아님. **수렴 메시지는 알고리즘이 멈췄다는 신호일 뿐, 임상 질문에 답했다는 보증서가 아님.** 

이걸 알아도 실무에서는 또 빠짐. 이유는 단순함 — fitting부터 돌리는 게 가장 쉽고 직관적이거든. 그런데 fitting은 **6단계 중 다섯 번째 단계**임. 앞의 네 단계를 건너뛰면 fitting은 그냥 "소프트웨어 기본값 + 모델러의 추측"에서 출발하는 탐색이 되어버림.

### B. 6단계 Modeling Carousel — 외울 게 아니라 의식할 것 [G&W 5e, Fig.1.1, p.4]

| Step | 하는 일 | 산출물 |
|---|---|---|
| 1. **잠정 모델** | 사전 가설, 잠정 시스템 구조 | "무엇을 설명할지" 초기 구조 |
| 2. **설계** | 용량/채혈/반응/대상/시뮬레이션(CATD) | 식별 가능한 데이터를 만드는 계획 |
| 3. **실험 수행** | 설계대로 데이터 수집 | 농도·반응·시간 자료 |
| 4. **EDA** ⭐ | 농도-시간, 반응-시간, 반응-농도 도표 | **구조·비선형성·초기 추정치 후보** |
| 5. **Fitting** | 비선형 회귀 | 추정값·정밀도·목적함수 |
| 6. **모델 판별** | GOF·잔차·검증·경쟁 모델 비교 | 채택/기각 근거 |

매 순간 "**내가 이 6단계 중 어디에 서 있는가**"를 의식하는 게 핵심임. Fitting을 돌리고 있는데 4단계 산출물이 없으면, 5단계는 이미 망한 거임.

### C. Primary vs Secondary 파라미터 — t½ 길어지면 누구를 의심하는가?

파라미터에는 두 층위가 있음 [G&W 5e, pp.1–2]:

- **상수**: 용량 $D$ (입력)
- **Primary (일차)**: $V$, $Cl$ — 이 둘이 시스템을 결정함
- **Secondary (이차)**: $K$, $AUC$, $t_{1/2}$ — primary에서 계산되어 나옴

$$
\underbrace{K}_{\text{소실속도}}=\frac{\overbrace{Cl}^{\text{1차}}}{\underbrace{V}_{\text{1차}}},\quad
\underbrace{AUC}_{\text{총노출}}=\frac{\overbrace{D}^{\text{입력}}}{\underbrace{Cl}_{\text{1차}}},\quad
\underbrace{t_{1/2}}_{\text{반감기(2차)}}=\frac{\ln(2)}{\underbrace{K}_{\text{소실속도(2차)}}}
$$

**왜 이게 중요한가?** "환자의 t½이 길어졌다"는 보고를 받았다고 치자. 원인이 두 가지임:

- $Cl$ 감소 (간기능/신기능 저하?)
- $V$ 증가 (체액 저류? 단백결합 변화?)

**임상 처방이 달라짐.** Cl 감소면 용량 감량, V 증가면 loading dose 증량 고려. Secondary parameter만 보면 두 원인을 구분 못 함. 그래서 primary로 추정해야 함.

| 파라미터 | 단위 | 의미 | 변화 원인 |
|---|---|---|---|
| $D$ | amount | 입력량 | 처방, 투여 오류 |
| $Cl$ | volume/time | 제거 가능한 가상 부피/시간 | 장기 기능, 효소/수송체 활성 |
| $V$ | volume | 농도-체내량 변환 공간 | 조직 분포, 결합, 체성분 |
| $K$ | time⁻¹ | 1구획 소실 속도 | $Cl↑$ 또는 $V↓$ |
| $AUC$ | conc·time | 총 노출 | $D↑$ 또는 $Cl↓$ |
| $t_{1/2}$ | time | 농도 반감 시간 | $K↓$ |

**1구획 예측식과 잔차:**

$$
\underbrace{\hat C}_{\text{예측}} \;=\;
\overbrace{\frac{\overbrace{D}^{\text{투여량}}}{\underbrace{V}_{\text{분포공간}}}}^{\text{초기스케일}\,(C_0)}
\;\cdot\;
\overbrace{\exp\!\left(-\underbrace{\frac{Cl}{V}}_{=\,K}\,t\right)}^{\text{단일지수 감소}}
$$

$$
\underbrace{C}_{\text{관측}} \;=\;
\overbrace{\hat C}^{\text{구조모델}}
\;+\;
\underbrace{\varepsilon}_{\text{잔차(RUV)}}
$$

💡 **물통 비유**: $D/V$는 물감 한 방울을 처음에 얼마나 큰 물통에 떨어뜨렸는지(=초기 농도). $\exp(-Kt)$는 시간이 지나면서 색이 얼마나 빨리 옅어지는지. 관측 $C$는 모델 예측 $\hat C$에 잔차 $\varepsilon$(분석 오차, 표본 처리, 미설명 변동)이 더해진 값임.

### D. EDA가 장식이 아닌 이유 — 초기값이 결과를 결정함

EDA 단계의 진짜 산출물은 예쁜 그림이 아님. **5단계 fitting에 들어갈 모델 구조와 초기 추정치를 만드는 것**임. 

📖 **G&W 5e, Fig.1.2, p.6**: 청소율과 분포용적 두 축으로 그린 목적함수 표면(WRSS). 표면에 골짜기가 여러 개 있고, **출발점(노란 점)이 다르면 도착점(빨간 점)도 다른 골짜기에 빠짐.**

비선형 fitting 알고리즘은 초기 추정치를 요구함. EDA가 없으면 그 초기값은 추측으로 채워짐 → 알고리즘이 엉뚱한 골짜기로 떨어짐 → 수렴은 떴지만 답이 틀림.

> 💼 **실무 인사이트**: EDA의 진짜 산출물은 도표 자체가 아니라 **"초기 추정치 후보 1표 + 비선형성 유무 1줄"**임. 용량 보정 도표에서 비선형성이 보이면, 결론 내기 전에 데이터셋의 용량·시간·사건 코딩 오류부터 배제해야 함.

### E. 5대 함정 [G&W 5e, §1.4, p.4]

| 함정 | 한 줄 |
|---|---|
| ① fitting 전 EDA 경시 | 모델 구조와 초기값이 빈약해짐 |
| ② 수식 맹종 | 수식 외워도 생물학·데이터 구조가 안 보임 |
| ③ 소프트웨어 과신 | 수렴 ≠ 과학적 타당성 |
| ④ 가중치 오용 | 잔차/오차 모델 잘못 두면 구조 판단도 흐려짐 |
| ⑤ 총체적 시야 부재 | 설계·분석법·생물학·반응 시점을 함께 못 봄 |

⑤가 발현되는 가장 흔한 자리가 **식별성(G절)**과 **변량성(H절)**임. 이 둘을 분리해서 보는 훈련이 박사과정 PopPK 입구임.

### F. 모델링은 "필요할 때만" 함

G&W의 메시지는 "많이 하라"가 아니라 "**필요할 때만 하라**"임. 질문이 단순 노출 요약(생체이용률, 총 청소율)이면 **NCA로 끝남** [G&W 5e, p.4]. 모델링이 필요한 건 네 경우뿐임:

1. **단회 투여로 반복 투여 예측**
2. **비선형 약동학 정량화**
3. **PK/PD 관계 정량화**
4. **개체간 변이(IIV) 정량화 = PopPK** ← 이게 NONMEM/Monolix를 부르는 자리

같은 요법인데 환자마다 노출/반응이 다를 때, 그 변이가 어디서 오는가(체중·신기능·유전형)를 정량화하려면 NCA로 답 안 나옴. 그래서 PopPK가 필요함.

### G. 식별성의 두 층위 — 구조적 vs 운영적

5대 함정 중 ⑤가 자주 발현되는 자리. **수렴 떴다고 파라미터가 구별 가능한 건 아님.** 두 층으로 분리해서 봐야 함.

| 층위 | 묻는 질문 | 깨질 때 신호 | 처방 |
|---|---|---|---|
| **구조적(structural)** | 노이즈 없는 무한 데이터에서도 모델 구조가 파라미터를 유일하게 결정하는가? | 두 파라미터가 항상 곱/비로만 나타남 (예: $V/F$) | 모델 자체를 다시 짜야 함 (IV 자료 추가 등) |
| **운영적(operational)** | 우리 실제 데이터로 실용 정밀도로 구별되는가? | RSE 매우 큼, 두 파라미터 상관 ≈ 1, condition number 폭주 | 데이터 보강 또는 한 파라미터 고정 |

**표준 사례 — 경구 단독 자료의 $V/F$ 묶임** [G&W 5e, §2.2.4, Eq.2:39, p.32]:

$$
\underbrace{C(t)}_{\text{관측}} \;=\;
\overbrace{\frac{D_{po}\cdot K_a}{\underbrace{V/F}_{\text{묶인 비}}\cdot(K_a-K)}}^{\text{스케일}}
\cdot
\underbrace{\bigl[\exp(-K\,t)-\exp(-K_a\,t)\bigr]}_{\text{흡수·소실 차분}}
$$

$$
\overbrace{\underbrace{V}_{\text{진짜 분포용적}} \cdot \underbrace{F}_{\text{생체이용률}}}^{\text{개별 식별 불가}}
\;\xrightarrow{\text{경구 단독}}\;
\underbrace{V/F}_{\text{식별 가능 묶음}}
$$

> 💬 G&W 원문: "neither $F$ nor $V$ appears elsewhere in the model, and without information following an intravenous dose, unique values for $F$ and $V$ cannot be determined." [G&W 5e, §2.2.4, p.32]

💡 **열쇠 비유**: 구조적 식별성 = "이 자물쇠가 어떤 열쇠로든 열릴 수 있는 구조인가" (모델 설계 문제). 운영적 식별성 = "내가 손에 든 열쇠 꾸러미로 이걸 열 수 있는가" (데이터셋 문제). 자물쇠가 멀쩡해도 열쇠가 부족하면 안 열림.

> 💼 **실무 인사이트**: NONMEM에서 OMEGA가 0으로 가거나 두 THETA 상관이 0.95+면 거의 다 **운영적 식별성 부족**이지 "모델이 틀린 것" 아님. 처방 두 가지: (1) 흡수상 빠른 시점 추가 같은 informative한 채혈 설계, (2) 한 파라미터를 문헌값으로 고정. **구조적 식별성 깨진 건 데이터 보강으로 해결 안 됨** — 모델 자체를 다시 짜야 함.

### H. 변량성의 세 층 — IIV / IOV / RUV

식별성이 "파라미터들이 구별되는가"라면, 변량성은 "관측된 흩어짐이 어디서 오는가"임. PopPK 워크플로의 척추가 이 분해임.

$$
\underbrace{C_{ij}^{\text{obs}}}_{\text{환자 $i$, 시점 $j$ 관측}}
\;=\;
\overbrace{f\!\bigl(\underbrace{\theta_i}_{\text{개인 파라미터}},\,t_{ij}\bigr)}^{\text{구조 모델}}
\;+\;
\underbrace{\varepsilon_{ij}}_{\text{잔차(RUV)}}
$$

$$
\underbrace{\theta_i}_{\text{개인}} \;=\;
\overbrace{\theta_{\text{pop}}}^{\text{집단 평균}}
\cdot
\exp\!\bigl(\underbrace{\eta_i}_{\text{IIV}}\,+\,\underbrace{\kappa_{ik}}_{\text{IOV (방문 $k$)}}\bigr)
$$

| 층 | 기호 | 잡는 것 | 분산 | 진단 |
|---|---|---|---|---|
| **IIV** | $\eta_i$ | 환자 간 영구적 차이 | $\omega^2$ (OMEGA) | $\eta$-shrinkage |
| **IOV** | $\kappa_{ik}$ | 같은 환자의 방문 간 일시적 변동 | $\pi^2$ | IOV 빼면 IIV가 부풀려짐 |
| **RUV** | $\varepsilon_{ij}$ | 분석 오차·미설명 변동 | $\sigma^2$ (SIGMA) | $\varepsilon$-shrinkage |

💡 **양궁수 비유**: 
- **IIV** = 양궁수마다 평균 명중점이 다름
- **IOV** = 같은 양궁수가 오늘과 내일 컨디션이 달라 평균이 흔들림
- **RUV** = 한 발 한 발이 평균 주변에서 떨림

세 흔들림을 한 덩어리로 보면 "이 양궁수가 평소 어디로 쏘는가"가 안 잡힘.

> 💼 **실무 인사이트**: PopPK 보고서 최대 함정 — **IOV를 모델에 안 넣고 IIV가 비현실적으로 크게 나오는 것**. 그러면 체중·신기능 같은 공변량 끼워 넣을 때 "공변량이 IIV를 설명한다"는 결론이 실제로는 IOV를 설명한 거임. 그리고 $\eta$-shrinkage가 **30%를 넘으면** 개체별 EBE로 공변량 회귀하는 진단이 거의 무력화됨 [Savic & Karlsson 2009].

### M1 — 한 줄로 못 박기

> **Fitting은 6단계 중 5단계임. 새 데이터셋 받는 순간 질문·설계·EDA가 모델 구조와 초기값을 결정함. 수렴 메시지가 아니라 진단·검증이 모델 타당성을 지배함. 그리고 식별성(구조적/운영적)과 변량성($\eta/\kappa/\varepsilon$) 분리가 안 되면 PopPK는 그냥 신기루임.**

---

<!-- SLIDE_START: M2 | title: PK/PD Linkage & Therapeutic Window -->
<!-- SECTION_CORE: SC-04 -->

## Card M2 — PK/PD Linkage: 용량은 명령이 아니라 입력임

### A. 사슬을 한 줄로 — dose → exposure → response

PK는 "용량이 어떻게 농도가 되는가", PD는 "농도가 어떻게 효과가 되는가". **둘이 이어져야 효과-시간 곡선이 나옴.** PK만 보면 농도까지만, PD만 보면 농도-반응 정점만 보임 — 시간 축에서 효과가 어떻게 변하는지를 모르게 됨.

```text
Dose regimen → [PK] → Exposure-time → [PD] → Response-time → Clinical effect
```

[R&T 5e, p.5, Fig.1-3]

| 단계 | 단위 | 의미 | 흔드는 요인 |
|---|---|---|---|
| Dose regimen | amount, time | 입력 이력 | 용량, 간격, 경로, 제형, 순응도 |
| Exposure-time | conc over time | 체내 농도 시간 경과 | ADME, F, 체내 배치, first-pass |
| Response-time | effect over time | 반응의 시간 경과 | 작용부위 농도, 민감도, 평가변수 |
| Therapeutic window | exposure range | 효과·위해 사이 작동 범위 | 효능 한계, AE, 변이, 측정 부위 |

ADME · 체내 배치(disposition) · 초회 통과(first-pass) · 생체이용률(F) · 장간순환(enterohepatic cycling)이 용량을 노출로 바꾸는 생리 사슬임 [R&T 5e, pp.26–33].

> 🔑 **꼭 새겨둘 것**: dose는 명령문이 아니라 **입력 이력(input history)**임. 임상 판단은 그 입력이 만든 노출/반응 시간 경과를 읽을 때 시작됨.

### B. 치료역의 진짜 정의 — "안전 용량 범위"가 아님

치료역은 **노출 범위**임. 용량 범위가 아님.

| 상황 | 노출 | → 결과 / 조치 |
|---|---|---|
| 저노출 | 작용부위 농도 부족 | 무효 치료 → 용량/간격/순응도/흡수 점검 |
| 고노출 | AE 구간 진입 | 독성 ↑ → 감량, 간격 조정, TDM |
| 입력 불확실 | 겉보기 변이 ↑ | PK 변이와 누락 투여 혼동 |

[R&T 5e, p.6, Fig.1-4]

### C. Digoxin vs Morphine 미스터리 풀기

이제 들어가며에서 던진 질문을 풂. 둘 다 좁은 치료역인데 처방 빈도가 다른 이유 — **농도-시간 곡선의 속도가 다르기 때문**임 [R&T 5e, p.4, Fig.1-1; pp.4, 7].

- **Morphine**: 빠르게 제거됨 → 농도가 빨리 떨어짐 → 자주 투여해야 치료역 안에 머무름
- **Digoxin**: 천천히 제거됨 → 농도가 오래 유지됨 → 1일 1회면 충분

💡 **도로 비유**: 같은 좁은 도로라도 어떤 차는 천천히 오래 머물고, 어떤 차는 빠르게 지나감. "도로가 좁다"는 사실 하나로는 운전 방식이 정해지지 않음.

**Digitalizing dose 논리** [R&T 5e, p.7, Fig.1-5]: digoxin을 처음부터 낮은 유지 용량으로만 주면 치료 농도 도달이 너무 느림. 그래서 **초반에 여러 소량을 빠르게 줘서(loading) 치료 농도까지 끌어올린 뒤, 소량 유지 용량으로 전환**하는 게 자연스러움. → "도달 단계"와 "유지 단계"가 분리되는 약물의 사례임.

### D. 임상적 무게 — 처방 안전성이 걸려 있음

입원의 **약 5%가 부적절한 약물 사용**에서 옴 [R&T 5e, p.4]. 이건 약동학 일반론이 아니라 요법 설계 안전성의 문제임. PK/PD는 약물 설계 → 약물 선택 → 요법 설계 → 임상시험 프로토콜 → 데이터 해석 → 약물 평가 → **개인 맞춤 치료(individualized therapy)** 개시까지 모든 단계에 쓰임 [R&T 5e, p.20, Table 2-1].

### E. 현실이 모델을 흔드는 네 가지

| 왜곡 | 원문 앵커 | → 결과 |
|---|---|---|
| **측정 부위** | 작용부위 농도는 직접 측정 어려움 → 혈장이 대리 [R&T 5e, p.6, Fig.1-4] | 혈장 농도-실제 반응 불일치 |
| **순응도** | 1일 1회 항고혈압제 1년 지속률 ≈ **50%** [R&T 5e, p.12, Fig.1-10] | 누락 투여가 겉보기 PK 변이로 흡수됨 |
| **개체 변이** | phenytoin / S-warfarin / primaquine·G6PD / debrisoquine·CYP2D6 / terfenadine·ketoconazole [R&T 5e, pp.10–12, Fig.1-8] | 같은 요법 ≠ 같은 노출/반응 |
| **유전 표기 범위** | CYP2C9/CYP2C19 다형성, vitamin K epoxide reductase 기전 [R&T 5e, p.10] | (VKORC1 표기는 원문 범위 밖) |

> 💼 **실무 인사이트**: 순응도 모니터링 약하면 **겉보기 PK 변이가 실제론 missed dose 가공물**임. 모델은 이걸 환자 생리 차이가 아니라 입력 이력 오류로 흡수해버림. PopPK에서 IIV가 비현실적으로 클 때 제일 먼저 의심해야 할 게 **입력 이력 정확도**임.

### F. Allometric Scaling — 신생아에 mg/kg 외삽이 위험한 이유

같은 약을 70 kg 성인과 3 kg 신생아에 동일 mg/kg으로 주면 **신생아 노출이 더 큼.** 이유 — 청소율은 체중에 선형 비례하지 않음.

$$
\underbrace{CL_i}_{\text{개인 청소율}} \;=\;
\overbrace{CL_{70}}^{\text{70\,kg 표준}}
\cdot
\overbrace{\left(\frac{BW_i}{70}\right)^{0.75}}^{\text{체격(allometric)}}
\cdot
\underbrace{F_{\text{mat}}(PMA_i)}_{\text{성숙도(소아)}}
$$

$$
\underbrace{V_i}_{\text{개인 V}} \;=\;
\overbrace{V_{70}}^{\text{70\,kg 표준}}
\cdot
\underbrace{\left(\frac{BW_i}{70}\right)^{1.0}}_{\text{체격(선형)}}
$$

| 파라미터 | 체중 지수 | 의미 |
|---|---:|---|
| $CL$ | $\propto BW^{0.75}$ | 대사·신배설은 체격에 비선형 |
| $Q$ | $\propto BW^{0.75}$ | 같은 지수 |
| $V$, $V_{ss}$ | $\propto BW^{1.0}$ | 부피는 체격에 선형 |
| $t_{1/2}$ | $\propto BW^{0.25}$ | $V/CL$ 비에서 도출 |

소아는 체중만으로 부족 — **maturation function**이 곱해짐:

$$
\underbrace{F_{\text{mat}}(PMA)}_{\text{성숙도 (0\sim 1)}} \;=\;
\frac{\overbrace{PMA^{\,Hill}}^{\text{나이 효과}}}
{\underbrace{TM_{50}^{\,Hill}}_{\text{성숙 반감 나이}} + PMA^{\,Hill}}
$$

PMA(postmenstrual age) = 임신 시점부터 센 나이, $TM_{50}$ = 성인 CL 50% 도달 나이, Hill = 성숙 곡선 가파름. 신생아에서 $F_{\text{mat}} \ll 1$, 보통 1–2세에 성인 수준.

💡 **엔진 비유**: 체격은 "엔진 크기", 성숙도는 "엔진이 워밍업됐는가". 같은 크기여도 차가운 엔진은 출력이 덜 나옴. 신생아 PK가 mg/kg 외삽으로 안 풀리는 이유가 이거임.

| 상황 | 1차 정규화 | 비고 |
|---|---|---|
| 정상 체중 성인 | TBW | 표준 |
| 비만 성인 | LBW 또는 fat-free mass | 지방 분포 적은 약에서 TBW 과대 외삽 위험 |
| 소아 | TBW + maturation | 1–2세 미만 maturation 누락 시 과량 |
| 신생아 | TBW + maturation + 기관 발달 | NICU TDM 첫 검토 |

> 💼 **실무 인사이트**: 첫 covariate 검토 최대 함정 — **체중을 $BW^{1.0}$ 선형으로 청소율에 넣는 것**. 큰 환자 CL이 과대 추정 → 작은 환자에 과량. NONMEM 표준 코드 한 줄: 
> ```
> CL = THETA(1) * (WT/70)**0.75 * FMAT
> ```
> 비만+소아 혼합 데이터셋이면 LBW와 PMA가 같이 들어가야 함.

### M2 — 한 줄로 못 박기

> **용량 결정은 dose regimen이 아니라 exposure-time × response-time 곱이 답함. PK만 보거나 PD만 보면 "치료역 안에 머무는 시간"이 안 잡힘. 그리고 체격·연령 정규화는 선형이 아니라 allometric($BW^{0.75}$) + maturation이 표준임.**

---

<!-- SLIDE_START: M3 | title: Emax / C50 / Hill γ -->
<!-- SECTION_CORE: SC-05 -->

## Card M3 — Emax/C50/γ: 농도-반응의 세 축

### A. Hill 방정식과 세 축

M2에서 만든 사슬 중 "농도 → 반응" 마디의 모양을 분해함. **$E_{\max}$ · $C_{50}$ · $\gamma$를 한 덩어리로 외우면 효능·천장·가파름이 머릿속에서 뒤섞임.** 세 축을 분리해야 용량 적정·평가변수 선택·안전역 해석이 각각 어디서 흔들리는지 보임.

$$
\underbrace{E}_{\text{예측효과}} \;=\;
\frac{\overbrace{\underbrace{E_{\max}}_{\text{효과천장}}\cdot\underbrace{C^{\gamma}}_{\text{농도구동}}}^{\text{효과상승}}}
{\underbrace{C_{50}^{\,\gamma}}_{\text{효능기준}}\;+\;\underbrace{C^{\gamma}}_{\text{현재농도}}}
$$

[R&T 5e, p.40, Eq.2-4]

💡 **엘리베이터 비유**:
- $E_{\max}$ = 엘리베이터가 도달 가능한 **최고층** (천장, ceiling)
- $C_{50}$ = **중간층까지 가는 데 필요한 농도** (효능, potency)
- $\gamma$ = **버튼 살짝 눌렀을 때 얼마나 급하게 반응하는가** (가파름, steepness)

| 파라미터 | 단위 | 의미 |
|---|---|---|
| $E$ | response unit | 현재 농도에서 예측 효과 |
| $E_{\max}$ | response unit | 최대 반응 (천장) |
| $C$ | concentration | 현재 농도 |
| $C_{50}$ | concentration | $E_{\max}$의 50%를 만드는 농도 |
| $\gamma$ | dimensionless | 농도-반응 가파름 |

**노출-시간 앵커도 챙겨야 함** [R&T 5e, pp.21–22, Fig.2-1]:

$$
\underbrace{C_{\max}}_{\text{최고농도}},\quad
\underbrace{t_{\max}}_{\text{도달시간}},\quad
\underbrace{AUC}_{\text{총노출}}
$$

Fig.2-1 예시: $C_{\max}=96\,\mu g/L$, $t_{\max}=3.0$ hr.

> 🔑 **꼭 새겨둘 것**: $C_{50}$ 낮다고 다 좋은 약 아님. 같은 효능이라도 $E_{\max}$가 낮으면 충분한 임상 반응 도달 못 함 [R&T 5e, pp.40–43]. 그리고 고원·저반응 영역 자료 없이 $C_{50}$ 주변만 있으면 **$\gamma$ 추정은 모델이 아니라 잡음을 따라감.**

### B. γ가 처방을 바꾸는 지점 — 16배 vs 4배

$\gamma$ 값에 따라 **20% → 80% 반응에 필요한 농도 범위**가 어떻게 압축되는지 [R&T 5e, p.40, Fig.2-16]:

| 곡선 | $\gamma$ | 농도 범위 | 임상 의미 |
|---|---|---|---|
| 완만 | 1 | $C_{20}=0.25C_{50}$ → $C_{80}=4C_{50}$ (**16배**) | 노출 16배 변해야 반응 20→80%, 적정 여유 큼 |
| 가파름 | 2 | $C_{20}=0.5C_{50}$ → $C_{80}=2C_{50}$ (**4배**) | 노출 4배만 변해도 반응 20→80%, 작은 농도차가 큰 임상차 |

$$
\underbrace{\gamma=1}_{\text{완만}}:\quad
\overbrace{\underbrace{C_{20}=0.25\,C_{50}}_{\text{20\%반응}}\;\to\;\underbrace{C_{80}=4\,C_{50}}_{\text{80\%반응}}}^{\text{16배 여유}}
$$

$$
\underbrace{\gamma=2}_{\text{가파름}}:\quad
\overbrace{\underbrace{C_{20}=0.5\,C_{50}}_{\text{20\%반응}}\;\to\;\underbrace{C_{80}=2\,C_{50}}_{\text{80\%반응}}}^{\text{4배 여유}}
$$

💡 **계단 비유**: 완만한 곡선은 긴 경사로, 가파른 곡선은 짧은 계단. 같은 목적지여도 계단에서는 한 발 차이가 훨씬 크게 느껴짐.

일반적으로 $\gamma$는 1–3 사이. 매우 크면 농도 범위가 좁아져서 **all-or-none처럼 보임** [R&T 5e, pp.40–41].

> 💼 **실무 인사이트**: $\gamma$는 곡선 모양이 아니라 **용량 적정 전략 자체를 바꿈.** $\gamma \approx 1$이면 증상 기반 적정 자연스러움. 반응이 가파르거나 역치형이면 **작은 농도 변화가 임상 사건을 만듦.** 그래서 협역 치료역 약물(digoxin, aminoglycoside, warfarin)에서 γ 큰 경우 TDM 필수가 됨.

### C. 등급 vs 이분형 — propranolol과 alfentanil

**Propranolol** (비선택적 β-차단제) [R&T 5e, p.42, Fig.2-17]: 운동 유발 빈맥 감소율과 **비결합 농도(unbound concentration in plasma)**의 관계가 Hill에 잘 맞음.

$$
\overbrace{
\underbrace{\gamma\approx 1}_{\text{거의 log-linear}},\quad
\underbrace{E_{\max}\approx 40\%}_{\text{심박수 감소 천장}},\quad
\underbrace{C_{50}=5.3\,\mu g/L}_{\substack{\text{**unbound** 기준}\\\text{(Fig.2-17 caption)}}}
}^{\text{Hill 적용 결과}}
$$

> ⚠️ **출처 정확화**: $C_{50}=5.3\,\mu g/L$는 **plasma unbound** 기준임 [R&T 5e, Fig.2-17 caption, p.42: "Response increases with the unbound concentration of the drug in plasma"]. 총 농도로 잘못 외우면 단백결합 변하는 상황(질병, DDI)에서 외삽 어긋남. 비결합 농도가 반응을 구동한다는 원칙은 R&T 5e, p.40에 명시.

**Alfentanil** (초단시간 opioid) [R&T 5e, pp.42–43, Fig.2-18]: nitrous oxide 마취 중 만족스러운 마취 반응의 **누적 빈도**로 평가됨 — 환자별 "만족/불만족" 이분형. $C_{50}$이 수술 부위별로 다름:

- 유방: **0.27 mg/L**
- 하복부: **0.31 mg/L**
- 상복부: **0.42 mg/L**

→ 그래서 alfentanil은 **이분형 평가변수에서 $C_{50}$이 등급 곡선 50% 지점이 아니라 집단 사건 확률 50% 농도 기준**이라는 사례임.

| 평가변수 | 모델 | 핵심 |
|---|---|---|
| 등급 (propranolol) | Hill 직접 효과 | $E_{\max}/C_{50}/\gamma$ 분리 추정 |
| 이분형 (alfentanil) | 누적 빈도/확률 | 집단 사건 확률의 농도 기준 |
| 평가변수 척도 불일치 | — | **모델보다 평가변수 정의를 먼저 확정** |

또 다른 등급 사례 — **ketamine** (NMDA 길항 마취제) [R&T 5e, p.40, Fig.2-11]: 두 입체이성질체에서 **S(+)**가 R(−)보다 $C_{50}$ 낮고 $E_{\max}$ 높음 — S(+) $C_{50}$ ≈ 0.7 mg/L, R(−) $C_{50}$ ≈ 1.8 mg/L. → 입체이성질체에 따라 효능·천장이 분리되는 사례.

### D. 측정의 함정 — "총 농도 = 활성 분자"가 아님

총 농도에는 결합형+비결합형이 다 들어있지만, **분포·소실·PD 반응은 비결합 농도에 의존함.** $f_u$가 일정하면 총 농도로 충분하지만, **포화성 결합·DDI·신·간 질환·수술·중증 화상·임신**에서 결합이 흔들리면 비결합 농도가 결정적임 [R&T 5e, p.21; G&W 5e, §2.6.5; §2.9.4, Eq.2:373, p.167].

**활성 물질(active moiety) 경계도 같이 봐야 함**:

- **acenocoumarol** (쿠마린계 항응고제): 라세미체
- **methylphenidate** (라세미 자극제, ADHD): d-이성질체가 주 활성
- **aspirin / salicylic acid**: 전구약물-활성 대사체 쌍

[R&T 5e, pp.23–25]. → "**무엇을 측정했는가**"가 효능 해석을 결정함.

> 💼 **실무 인사이트**: 용량 범위가 $C_{50}$ 주변에만 몰리고 고원 정보 없으면, $\gamma$를 자유롭게 추정하기보다 **절약적 가정($\gamma=1$ 고정)을 먼저 검토.** "$\gamma$를 추정했다"가 아니라 "**데이터가 $\gamma$를 식별할 수 있는가**"가 먼저임. 외부 문헌에서는 이걸 "poor identifiability under truncated concentration range" 또는 "uninformative $\gamma$"로 부름.

### E. 임상 $E_{\max}$가 약리학적 최대치보다 낮을 때

심박수를 올리는 약물에서는 심혈관계가 먼저 악화돼서 **약리학적 최대치 전에 안전성 한계가 옴.** → 작용제(agonist)의 $E_{\max}$가 길항제보다 임상적으로 정의하기 어려운 이유임 [R&T 5e, p.41].

**노출 지표 선택도 같이** (Fig.2-19 [R&T 5e, p.44]): 만성 치료에서는 **최소 농도 이상 유지 기간**, 두통 완화 같은 빠른 효과는 $C_{\max}$/$t_{\max}$, 어떤 경우엔 총 $AUC$가 더 관련 있음.

### F. Effect Compartment & Hysteresis — 농도-효과 시간 지연

농도-반응 곡선이 "즉시" 성립하지 않는 경우 흔함. 작용 부위(생체상)는 혈장과 별도 공간이라, 혈장 농도가 올라도 작용부위 농도는 시간차를 두고 따라옴. 이게 **hysteresis loop**(이력 곡선)로 나타남.

| 패턴 | 농도-효과 plot 모양 | 해석 |
|---|---|---|
| **counter-clockwise (반시계)** | 동일 농도에서 시간 ↑ → 효과 ↑ | 작용부위가 혈장보다 느리게 차오름 → effect compartment 필요 |
| **clockwise (시계)** | 동일 농도에서 시간 ↑ → 효과 ↓ | 내성(tolerance) 또는 활성 대사체 변동 |
| **no loop** | 단일 곡선 | 직접 효과 모델로 충분 |

**Effect compartment 모델** [Sheiner-Holford framework]:

$$
\underbrace{\frac{dC_e}{dt}}_{\text{작용부위 변화}} \;=\;
\overbrace{k_{e0}}^{\substack{\text{전달 속도상수}\\\text{(equilibration)}}}
\cdot
\bigl(\underbrace{C_p}_{\text{혈장}}\;-\;\underbrace{C_e}_{\text{작용부위}}\bigr)
$$

$$
\underbrace{E}_{\text{효과}} \;=\;
\frac{\overbrace{E_{\max}\cdot C_e^{\,\gamma}}^{\text{$C_e$로 구동}}}
{\underbrace{C_{50,e}^{\,\gamma}}_{\text{작용부위 효능}}+C_e^{\,\gamma}}
$$

평형 반감기 $t_{1/2,k_{e0}} = \ln(2)/k_{e0}$가 작으면 hysteresis 거의 사라지고, 크면 효과 peak가 농도 peak보다 한참 늦음. 표준 사례 — **midazolam–EEG**, **fentanyl–pupil diameter** 같은 마취 약물군.

> 💼 **실무 인사이트**: 농도 peak와 효과 peak 시간차가 **분포 평형으로 설명 가능(분~수 시간)** → effect compartment. **시간차가 너무 크거나(시간~일)** 또는 농도 사라진 후에도 효과 지속 → 다음 카드(M4) turnover/IDR 영역. 두 모델 다 "지연"을 잡지만, **분포 지연(effect compartment)**인지 **내인성 시스템 변화(IDR)**인지 구분이 결정적임.

### M3 — 한 줄로 못 박기

> **농도-반응은 $E_{\max}$ · $C_{50}$ · $\gamma$ 세 축 분리가 답. 평가변수 척도(등급 vs 이분형)가 모델 프레임을 지배함. $C_{50}$만 보면 천장·가파름·식별성·농도 기준(총 vs unbound)을 다 놓침. 농도-효과 시간 지연 보이면 effect compartment 부터 의심.**

---

<!-- SLIDE_START: M4 | title: Turnover -->
<!-- SECTION_CORE: SC-06 -->

## Card M4 — Turnover: 지연 반응의 문법

### A. Dynamic Equilibrium — 정상 상태는 정지 상태가 아님

M3가 농도-반응의 **지금 이 순간** 관계라면, M4는 반응이 **시간상 늦게 나타나는 이유**를 풂.

함정 패턴: 농도는 빨리 올라갔는데 효과는 늦게 나오는 상황에서, 이걸 다 분포 지연이나 Hill 곡선 문제로 돌리는 것. 그렇게 보면 **내인성 시스템이 천천히 바뀌는 구조**를 놓침. 

전환(turnover) 관점에서 보면 **정상 상태는 정지 상태가 아니라 입력=출력으로 풀 크기가 일정해 보이는 동적 평형(dynamic equilibrium)**임 [R&T 5e, p.45].

임상에서 흔히 만나는 turnover 약물군:
- **경구 항응고제** (warfarin)
- **항고지혈증제**
- **요산 배설 촉진제**
- **epoetin alfa** (재조합 EPO)

이들은 다 내인성 화합물/시스템의 생성·소실을 바꿔서 **지연 반응**을 만듦. 약물의 작용은 빨라도 측정 시스템이 늦게 바뀜.

### B. 전환 방정식 — Rt, Ass, kt, tt

$$
\underbrace{k_t}_{\text{분획 전환속도}} \;=\;
\frac{\overbrace{R_t}^{\text{전환량/시간}}}{\underbrace{A_{ss}}_{\text{풀 크기}}}
\qquad [\text{R\&T 5e, Eq.2-5}]
$$

$$
\underbrace{t_t}_{\text{전환 시간}} \;=\;
\frac{\overbrace{A_{ss}}^{\text{풀 크기}}}{\underbrace{R_t}_{\text{전환량/시간}}}
\;=\;
\frac{1}{\underbrace{k_t}_{\text{분획 전환속도}}}
\qquad [\text{R\&T 5e, Eqs.2-6, 2-7}]
$$

💡 **저수지 비유**: $R_t$는 하루에 드나드는 물의 리터 수, $A_{ss}$는 저수지 크기. **큰 저수지에서는 하루 유입량이 커도 저수지 전체가 갈아엎어지는 속도는 느릴 수 있음.**

| 파라미터 | 단위 | 의미 |
|---|---|---|
| $A_{ss}$ | amount | 정상 상태 풀 크기 |
| $R_t$ | amount/time | 단위 시간당 전환 |
| $k_t$ | time⁻¹ | 풀 대비 분획 전환 |
| $t_t$ | time | 평균 전환 시간 |

> ⚠️ **꼭 새겨둘 것 — $R_t$ 함정**: $R_t$가 크다고 과정이 빠르다고 단정하면 안 됨. 풀 크기 $A_{ss}$로 나눈 **$k_t$와 $t_t$가 속도 감각을 더 직접적으로 줌.** 농도 peak와 효과 peak가 어긋나면 직접 효과 Hill만으로 충분한지 먼저 의심하고 **전환·지연 구조**를 검토해야 함.

### C. 같은 식, 다른 임상 결론 — 네 사례

| 예시 | 관찰 | 해석 |
|---|---|---|
| **warfarin** [R&T 5e, p.8, Fig.1-6] | 1.5 mg/kg 단회 경구 후 농도는 빨리 ↑, prothrombin complex activity는 느리게 ↓ | 농도-시간만으론 반응-시간 설명 불가 → **전환 구동 반응**의 대표 |
| **paclitaxel** [R&T 5e, pp.8–9, Fig.1-7] | 약 **2일 내** 체내 제거, 그러나 **백혈구 최저점 1주 후**, **회복 ~3주** | 약물이 사라진 한참 뒤에 임상 효과 정점 → **내인성 시스템 변화가 반응을 지배** |
| 총 체수분 [R&T 5e, pp.45–46, Fig.2-20] | ~42 L, $R_t=2.5$ L/day, $k_t=0.06$ day⁻¹, $t_t=17$ days | 양이 많이 오가도 분획 전환 작으면 **과정은 느림** |
| 사막 환경 [R&T 5e, pp.45–46] | 풀 크기 거의 일정, $R_t=21$ L/day, $k_t=0.5$ day⁻¹, $t_t=2$ days | 풀 크기 같아도 **전환 속도·시간은 환경에 따라 크게 달라짐** |

💡 **방 온도 비유**: warfarin/paclitaxel의 지연은 스위치를 켰는데 **방 전체 온도가 천천히 바뀌는** 상황. 스위치 자체가 빠르게 작동해도, 바뀌어야 할 시스템 풀이 크거나 느리면 효과 peak가 늦어짐.

> 💼 **실무 인사이트**: 진짜 질문은 "$R_t$, $k_t$, $t_t$ 중 무엇을 외웠는가"가 아님. **"이 시스템에서 풀 크기가 보존되는가, 분획 전환이 보존되는가, 전환 속도 자체가 바뀌는가"**임. 체수분은 풀 크기가 피드백으로 유지되는 경우, 콜레스테롤·백혈구는 풀 크기 자체가 변하는 경우 [R&T 5e, p.46].

### D. IDR 4 변종 — 후속 PD 세션의 출발 어휘

R&T가 turnover로 깔아놓은 풀-속도 분리는 **Dayneka–Garg–Jusko 간접 반응 모델(IDR)** 4 변종의 어휘임. 풀 $R$이 입력 $k_{\text{in}}$과 1차 소실 $k_{\text{out}}\cdot R$의 균형으로 유지된다는 기본식에서, **약물이 어느 항을 바꾸는가**로 네 가지가 갈림.

$$
\underbrace{\frac{dR}{dt}}_{\text{풀 변화율}} \;=\;
\overbrace{k_{\text{in}}}^{\text{생성(0차)}}
\;-\;
\underbrace{k_{\text{out}}\cdot R}_{\text{1차 소실}}
\qquad [\text{정상 상태: } R_{ss}=k_{\text{in}}/k_{\text{out}}]
$$

| Model | 약물 작용 | 효과 함수 | 대표 사례 |
|---|---|---|---|
| **I** | $k_{\text{in}}$ 억제 | $\dfrac{dR}{dt}=k_{\text{in}}\!\cdot\!\bigl(1-\dfrac{I_{\max}C^\gamma}{IC_{50}^\gamma+C^\gamma}\bigr)-k_{\text{out}}R$ | **warfarin**: 응고인자 합성 억제 [R&T 5e, p.8, Fig.1-6] |
| **II** | $k_{\text{out}}$ 억제 | $\dfrac{dR}{dt}=k_{\text{in}}-k_{\text{out}}\!\cdot\!\bigl(1-\dfrac{I_{\max}C^\gamma}{IC_{50}^\gamma+C^\gamma}\bigr)\!R$ | corticosteroid의 림프구 트래픽 |
| **III** | $k_{\text{in}}$ 자극 | $\dfrac{dR}{dt}=k_{\text{in}}\!\cdot\!\bigl(1+\dfrac{E_{\max}C^\gamma}{EC_{50}^\gamma+C^\gamma}\bigr)-k_{\text{out}}R$ | **epoetin alfa**: 적혈구 생성 자극 [R&T 5e, p.45] |
| **IV** | $k_{\text{out}}$ 자극 | $\dfrac{dR}{dt}=k_{\text{in}}-k_{\text{out}}\!\cdot\!\bigl(1+\dfrac{E_{\max}C^\gamma}{EC_{50}^\gamma+C^\gamma}\bigr)\!R$ | 요산 배설 촉진제(uricosuric) |

지연의 핵심 시상수는 **$\ln(2)/k_{\text{out}}$**임. → **PD plateau 도달 시간이 약물 t½이 아니라 시스템 turnover로 결정됨**이 IDR의 가장 큰 메시지. 예시:
- warfarin의 PT 활성 회복 = 응고인자 turnover
- epoetin alfa의 헤모글로빈 변화 = RBC 수명 ≈ **120일**

> 💼 **실무 인사이트**: IDR I과 II는 둘 다 "↓ 효과" 만들지만 곡선 모양이 다름.
> - **Model I** = 생성 차단 → 풀이 **천천히** 비고 ($k_{\text{out}}$ 시상수)
> - **Model II** = 소실 가속 → 풀이 **빠르게** 빠진 뒤 다시 천천히 회복
> 
> 같은 효과 방향인데 적정 전략이 다름. "감소 효과 = Model I"로 직행하면 안 됨.

### E. Effect Compartment vs IDR — 어디서 갈리는가

농도 peak ≠ 효과 peak일 때 두 후보 모델이 있음. 분기 기준은 **시상수의 단위**임.

| 분기 | 시상수 | 해석 |
|---|---|---|
| **Effect compartment** ($k_{e0}$) | 분~수 시간 | 약물 자체가 작용부위에 도달하는 데 시간 걸림 (분포 지연) |
| **IDR** ($k_{\text{out}}$) | 일~주 | 약물 작용은 빠른데 측정 시스템이 내인성 turnover로 천천히 바뀜 |

**진단 패턴**:
- 농도 사라진 후에도 효과 지속? → IDR
- 농도 곡선과 효과 곡선의 peak 시간차가 분 단위? → effect compartment
- Hysteresis loop이 counter-clockwise면서 시간차 짧음 → effect compartment
- Hb 같은 천천히 바뀌는 바이오마커 → IDR ($k_{\text{out}}$ ≈ RBC 수명)

### M4 — 한 줄로 못 박기

> **농도 peak ≠ 효과 peak이면 turnover·지연 구조가 판단을 지배. $R_t$ 크다고 빠른 게 아니라 $k_t$·$t_t$가 속도 감각을 줌. 지연을 단순 poor fit이나 분포 지연으로 보면 IDR 채택 근거를 놓침. 분포 지연(분~시간) = effect compartment, 시스템 변화(일~주) = IDR.**

---

## §3. 데이터셋 앞 30초 — 네 렌즈 체크리스트

새 PK/PD 데이터셋 받는 처음 30초, 네 렌즈를 **동시에** 켬. 모델 코드 작성 **전** 단계임.

| 렌즈 | 먼저 볼 것 | 즉시 판단할 것 |
|---|---|---|
| **M1** | 용량 수준, 채혈 밀도, 농도-시간 도표 | EDA가 모델 구조와 초기값을 줄 수 있는가? 식별성·변량성 분리 가능한가? |
| **M2** | 요법, 경로, 순응도, 측정 부위, 체격·연령 | 용량→노출→반응 사슬에서 빠진 연결이 있는가? Allometric/maturation 필요한가? |
| **M3** | 고원, $C_{50}$ 주변 자료, 평가변수 유형, 농도-효과 시간차 | $E_{\max}/C_{50}/\gamma$ 식별 가능한가? 등급 vs 이분형? Hysteresis 있는가? 농도 기준(총 vs unbound)? |
| **M4** | 농도 peak vs 효과 peak 시점, 기저선 변동 | 직접 효과 모델로 충분한가? 시간차 단위(분 vs 일)로 effect compartment vs IDR 분기 |

이 네 렌즈 켜는 목적은 제어구문을 미리 쓰는 게 아니라 **모델 선택의 근거가 데이터에 있는지를 먼저 묻는 것**임.

---

## §4. 혼동쌍 해부

### 혼동쌍 1 — PK vs PD

| 기준 | A: PK | B: PD |
|---|---|---|
| 단위 | 농도, $AUC$, $C_{\max}$, $t_{\max}$ | 반응, 바이오마커, 임상 평가변수 |
| 사슬 위치 | 입력 → **농도-시간** | 농도 → **효과-시간** |
| 변화 원인 | ADME, 투여 이력 | 작용부위 민감도, 평가변수, 생리/질병 |
| 혼동 시 결과 | 노출 = 용량으로 오해 | 반응을 농도 없이 용량과 직접 연결 |

⚡ **기억 고리**: PK는 *입력 → 농도*, PD는 *농도 → 효과*. **같은 선상의 앞뒤 화살표**이지 좌우 반대 화살표가 아님. 한쪽만 그리면 용량-효과 사슬이 끊겨서 dosing decision 멈춤.

### 혼동쌍 2 ⚡ 치명적 — 등급 vs 이분형 반응

| 기준 | A: 등급(graded) | B: 이분형(quantal) |
|---|---|---|
| 단위 | 강도가 연속적으로 변함 | 개체는 전부/전무, 집단은 누적 빈도 |
| 모델 | Hill/$E_{\max}$ 연속 반응 | 누적 빈도/확률로 사건 |
| 사례 | ketamine, propranolol | alfentanil |
| 혼동 시 결과 | 연속 VAS 적합 | 이분형을 등급 곡선처럼 읽으면 평가변수-모델 어긋남 |

**치명적 시나리오 [교육용]**: 일차 평가변수가 "24h 내 ≥50% 통증 감소: 예/아니오" 이분형인데 모델러가 연속 VAS를 등급형 Hill로 분석함. 통계학자의 이진 분석과 모델러의 노출-반응 분석이 **서로 다른 용량을 지지**함. 문제는 Hill 방정식이 아니라 **평가변수 척도와 모델링 프레임 불일치**임.

> **실패 양식**: 이분형 자료를 개체별 등급 곡선처럼 읽으면 Hill 문제가 아니라 **평가변수 정의 문제**임. 개체 수준 반응 크기인지, 집단 수준 사건 확률인지 먼저 분리해야 함.

### 혼동쌍 3 — $R_t$ vs $k_t$

| 기준 | A: $R_t$ | B: $k_t$ |
|---|---|---|
| 단위 | amount/time | time⁻¹ |
| 식 위치 | $k_t=R_t/A_{ss}$ 분자 | $t_t=1/k_t$ 분모 |
| 사례 | 2.5 L/day | 0.06 day⁻¹ (= $t_t$ 17 days) |
| 혼동 시 결과 | "빠른 과정"으로 오해 | 실제론 **느린 과정**임을 보여줌 |

**핵심**: $R_t$만 보면 큰 풀의 느린 전환을 빠른 과정으로 오해. **속도는 $k_t$와 $t_t$가 더 잘 말해줌** [R&T 5e, pp.45–46].

### 혼동쌍 4 — 구조적 vs 운영적 식별성

| 기준 | A: 구조적 | B: 운영적 |
|---|---|---|
| 묻는 것 | 무한 정확 데이터에서 분리 가능? | 우리 데이터로 실용 정밀도? |
| 신호 | $V/F$, $CL/F$ 묶임 [G&W 5e, p.32] | RSE↑, 상관 ≈ 1, condition number 폭주 |
| 처방 | 모델 재설계 (IV 자료 추가 등) | 데이터 보강 또는 파라미터 고정 |
| 혼동 시 결과 | 운영적으로 오해 → 채혈만 늘려도 해결 안 됨 | 구조적으로 오해 → 모델 폐기 과대반응 |

**핵심**: NONMEM에서 "수렴은 되는데 OMEGA가 무너진다"는 거의 다 **운영적**. "어떻게 해도 두 파라미터가 묶여 나온다"는 **구조적** — 데이터로는 못 풂.

---

## §5. 자기 테스트 — 입으로 답할 수 있어야 통과

**Q1.** 모델링 사이클에서 fitting은 몇 번째이며, 왜 그 앞이 중요한가?  
→ Fitting은 5단계임. 4단계 EDA가 모델 구조와 초기값을 제안하고, 비선형 fitting은 초기값에 민감하기 때문 [G&W 5e, pp.5–6, Fig.1.2].

**Q2.** NCA가 충분한 질문과 모델링이 필요한 질문을 하나씩.  
→ NCA: 생체이용률·총 청소율 요약. 모델링: ① 단회→반복 예측, ② 비선형 PK 정량화, ③ PK/PD 정량화, ④ IIV 정량화(PopPK) [G&W 5e, p.4].

**Q3.** 치료역을 용량이 아닌 노출 관점에서 설명.  
→ 너무 낮은 노출 = 무효, 너무 높은 노출 = AE ↑. 둘 사이에서 치료 반응을 얻고 과도한 AE를 피하는 **노출 범위**임 [R&T 5e, p.6, Fig.1-4].

**Q4.** Digoxin vs morphine 차이를 PK/PD 원리로.  
→ 둘 다 좁은 치료역 가능. morphine은 빨리 제거 → 자주 투여. digoxin은 천천히 제거 → 1일 1회 가능. digoxin은 도달과 유지가 분리되어서 **digitalizing dose + maintenance** 논리가 자연스러움 [R&T 5e, pp.4, 7, Fig.1-5].

**Q5.** $\gamma=1$과 $\gamma=2$의 20–80% 농도 범위 차이?  
→ $\gamma=1$이면 16배($0.25C_{50}$ → $4C_{50}$), $\gamma=2$이면 4배($0.5C_{50}$ → $2C_{50}$) [R&T 5e, p.40, Fig.2-16].

**Q6.** Propranolol과 alfentanil 예시의 가르침. propranolol $C_{50}=5.3\,\mu g/L$의 기준은?  
→ propranolol = 등급 반응이 Hill로 잘 맞는 예 ($\gamma≈1$, $E_{\max}≈40\%$, $C_{50}=5.3\,\mu g/L$). **$C_{50}$은 unbound concentration 기준**(Fig.2-17 caption 명시). alfentanil = 이분형에서 $C_{50}$이 집단 사건 확률 50% 농도 기준 — 유방 0.27, 하복부 0.31, 상복부 0.42 mg/L [R&T 5e, pp.42–43].

**Q7.** 농도 peak와 효과 peak가 어긋날 때 어떤 사고가 켜져야 하나? 후보 모델 둘은 어떻게 구분?  
→ 직접 효과 Hill만으론 부족, **effect compartment ($k_{e0}$)** 또는 **IDR**. 시간차가 분~수 시간 = effect compartment (midazolam–EEG). 일~주 = IDR (warfarin–PT, epoetin alfa–RBC) [R&T 5e, pp.8–9].

**Q8.** $R_t=2.5$ L/day인 총 체수분이 왜 "빠른 과정" 아닌가?  
→ 풀 ~42 L → $k_t=0.06$ day⁻¹, $t_t=17$ days. **풀 대비 분획이 작으면 과정은 느림** [R&T 5e, pp.45–46].

**Q9.** Fig.2-19 두 시나리오가 노출 지표 선택에 주는 메시지?  
→ 같은 $C_{\max}$/$t_{\max}$여도 감소 속도 다르면 $AUC$ 다르고, 같은 $AUC$여도 입력 속도 다르면 $C_{\max}$ 다름. **어떤 지표가 중요한지는 임상 목표·노출-반응 관계에 따라 달라짐** [R&T 5e, p.44].

**Q10.** 구조적 vs 운영적 식별성 차이와 각 처방?  
→ 구조적: 모델 구조가 파라미터 유일 결정? 깨지면 $V/F$로 묶임 → **모델 재설계**. 운영적: 실제 데이터로 구별? 깨지면 RSE↑/상관≈1 → **데이터 보강 또는 파라미터 고정** [G&W 5e, §2.2.4].

**Q11.** PopPK 변량성 세 층 분해 이유? $\eta$-shrinkage 크면?  
→ IIV($\eta$, 환자 간) · IOV($\kappa$, 같은 환자 방문 간) · RUV($\varepsilon$, 잔차) 분리 안 되면 공변량 효과 가짜 부풀려짐. IOV를 빼면 IIV로 흡수되어 covariate 가짜 신호. $\eta$-shrinkage > 30%면 EBE 회귀 진단 무력화.

**Q12.** 신생아 mg/kg 외삽이 위험한 이유? Allometric vs maturation은 각각 뭘 잡나?  
→ CL은 선형($BW^{1.0}$)이 아니라 **$BW^{0.75}$**. mg/kg 외삽 시 작은 환자 과량. 신생아·영아는 효소 미성숙 → $F_{\text{mat}}(PMA)$ 곱해야 함. NONMEM: `CL = THETA(1)*(WT/70)**0.75 * FMAT`.

**Q13.** Effect compartment와 IDR이 둘 다 "지연" 설명하는데 임상적으로 뭐가 다른가?  
→ effect compartment ($k_{e0}$) = 약물 자체가 작용부위 도달에 시간 (분~수 시간), counter-clockwise hysteresis. IDR ($k_{\text{out}}$) = 약물은 빠른데 내인성 시스템이 천천히 바뀜 (일~주), warfarin–PT, epoetin alfa–RBC. **두 모델은 같은 "지연"이라도 임상 적정 전략이 다름.**

---

## §6. 메타 프레임 — 이 세션이 후속에 여는 길

| 후속 세션 | 이 세션이 여는 것 | 이게 없으면 |
|---|---|---|
| GOF/VPC, NPDE/CWRES, Bayesian/MAP | M1: 진단은 Step 6, 식별성 두 층 | 소프트웨어 출력을 모델 타당성으로 오해 |
| PopPK / 공변량 모델링 | M1: NCA-모델링 경계 4번째, 변량성 세 층; M2: 변이 위치, allometric/maturation | 변이를 한 덩어리로 처리, 공변량 누락, IOV→IIV 흡수로 가짜 신호 |
| 구획 PK / TDM | M2: dose → exposure → response, 체격·연령 정규화 | 농도-시간을 반응과 분리, mg/kg 외삽 위험 |
| 직접 효과 PD / Effect compartment | M3: 천장·효능·가파름, endpoint type, hysteresis | 세 축 혼동, 농도-효과 시간차 무시 |
| IDR I–IV / 질병 진행 / TMDD | M4: turnover, IDR 4 변종, $k_{\text{out}}$ 시상수 | 지연을 분포 지연으로 오해, $k_{\text{out}}$이 PD plateau를 정한다는 사실 누락 |

---

## §7. 닫으며 — 이 세션 통과한 사람이 갖는 네 가지 무기

1. **질문 기반 워크플로**  
   데이터 받는 순간 "**무엇을 결정하기 위한 모델인가**"부터 씀. Fitting 버튼은 마지막에 누름.

2. **dose → exposure → response 좌표**  
   세 좌표 중 어디에서 IIV가 생기는지 식별하고, 변량성을 $\eta/\kappa/\varepsilon$ 세 층으로 분해할 준비됨.

3. **천장·효능·가파름 3축**  
   $C_{50}$만 보고하는 보고서는 천장·가파름 정보 통째로 버린 것. $C_{50}$이 총 농도 기준인지 unbound 기준인지, hysteresis 있는지도 같이 봄.

4. **전환 = "지연된 상태"의 문법**  
   반응 지연이 분포 지연($k_{e0}$, 분~시간)인지 내인성 시스템 turnover($k_{\text{out}}$, 일~주)인지 가름. IDR I–IV 어휘로 이어짐.

이 네 가지가 손에 잡혀 있으면, 앞으로 나오는 GOF·구획 PK·TDM·직접/간접 PD·TMDD 어디서든 "**내가 지금 모델링 사이클의 어느 단계에 서 있고, 무엇을 결정하기 위해 이 단계를 밟고 있는가**"를 입으로 말할 수 있게 됨. 그게 이 Pre-Sprint의 진짜 목적임.

---

> **마무리 한 문장.** 모델링은 수식 fitting이 아니라 **임상 질문을 시간 축 위의 두 곡선(노출/반응)으로 번역하는 사고**임. 그 번역이 잘 되면 PopPK/TDM/IDR/TMDD가 다 같은 언어로 풀림. 그 번역이 안 되면 어떤 도구를 써도 신기루를 좇게 됨.

---

*Sources: Gabrielsson & Weiner, Pharmacokinetic and Pharmacodynamic Data Analysis: Concepts and Applications, 5th ed.; Rowland & Tozer, Clinical Pharmacokinetics and Pharmacodynamics: Concepts and Applications, 5th ed.*

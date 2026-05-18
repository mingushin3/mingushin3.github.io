# 12 — 지연의 정체를 찾아서: 약물 시계·시스템 시계·신호 시계 (remastered)

## 들어가며 — 마취과 의사의 5초

마취과 의사가 수술 끝나갈 무렵 환자 옆에 서서 약을 끌지 말지 고민함. remifentanil을 infusion으로 주고 있었다면 — 끄고 1분이면 환자가 깸. 같은 자리에서 morphine을 같은 양으로 줬다면? 끄고 2시간 기다려도 깨워서 회복실 못 보냄. 둘 다 μ-opioid receptor 작용제고, 둘 다 같은 표적에 같은 방식으로 붙음. 그런데 임상 거동이 완전히 다른 약처럼 보임.

여기서 핵심 질문은 — *"왜 같은 표적 약물인데 plasma 농도가 떨어진 뒤 환자 상태가 회복되는 속도가 100배 차이나는가?"* 답은 plasma kinetics가 아님. plasma $t_{1/2}$만 봐서는 절대 못 맞춤. 답은 **약물이 effect site에 도달하고 떠나는 다리의 통행 속도** — $k_{e0}$ — 가 100배 다르기 때문임.

이 강의 전체가 가르치려는 단 하나는 이거임:

> **농도와 반응이 시간상 어긋날 때, 그 어긋남을 만드는 "시계"가 어디 있는지 *이름부터 붙이는* 훈련.**

지연이 보이면 손이 먼저 $k_{e0}$로 가는 게 학생 모델러의 습관임. 마스터 모델러는 정반대 순서로 감 — *"지금 늦는 게 누구냐?"*를 먼저 묻고, 답이 나온 다음에야 ODE 모양을 고름. 이 강의 끝나면 그 5초 안의 사고를 자기 것으로 만들 수 있어야 함.

---

## 본질 한 줄: 같은 단위가 같은 의미는 아님

본격적으로 들어가기 전에 PD21 데이터부터 보자. 길항제 X 실험에서 G&W가 보고하는 세 값임 [G&W p.846]:

$$
\overbrace{k_{e0}=0.025}^{\text{생체상 평형}},\quad \overbrace{k_{out}=0.031}^{\text{시스템 회전}},\quad \overbrace{k_{off}=0.018\ \text{min}^{-1}}^{\text{수용체 해리}}
$$

세 값이 거의 비슷함. 단위도 같음. 학생 모델러가 보면 *"어차피 다 비슷한 시간 상수네"* 하고 넘어감. **이게 함정임.** 셋은 완전히 다른 시계를 가리킴:

| 기호 | 비유 | 실제 의미 |
|---|---|---|
| $k_{e0}$ | **다리 통행 속도** | 약이 plasma에서 effect site로 건너가는 속도 |
| $k_{out}$ | **수조 배수 속도** | 시스템이 반응을 만들고 비우는 속도 |
| $k_{off}$ | **빗장 풀림 속도** | 약물-표적 결합이 해체되는 속도 |

다리, 수조, 빗장. 이 세 비유가 강의 끝까지 따라옴. PD21에서 세 값이 비슷하게 나온 건 *우연*이지 *동치*가 아님. 그래서 single-dose 데이터만 보고 셋 중 어느 시계가 율속하는지 못 가림. 구분하려면 dose stratification, 반복투여, washout 같은 *더 풍부한 실험 설계*가 필요함.

---

## 큰 그림: 데이터 받으면 5초 안에 도는 4막 사고법

농도-반응 시간 지연이 보일 때, 마스터 모델러의 머릿속에서 순서대로 도는 질문임:

```
관찰: 농도와 반응이 시간상 떨어져있다.
        ↓
1막: Hysteresis 방향은? (CCW or CW)
       → 후보 family 좁히기 (단, 결론 아님)
        ↓
2막: 약물 시계인가? → dose-invariant $t_{max}$ + $k_{e0}$ loop collapse 검사
       Yes → Effect compartment 모델
       No  → 다음 막
        ↓
3막: 시스템 시계인가? → 반복투여 trough drift, washout 후 rebound 검사
       Yes → Indirect response + Moderator $M$
       No  → 다음 막
        ↓
4막: 신호 시계인가? → onset이 즉각 지수형이 아니라 delayed sigmoid?
       Yes → Transit chain ($n \times \tau$)
```

이 흐름이 정확히 G&W 챕터 순서(§3.9 → §3.11 → §3.13)와 일치함. 우연이 아님 — Gabrielsson이 책을 쓸 때 의도한 escalation 사슬임. 학생이 외워야 할 건 챕터 번호가 아니라 **이 escalation 순서 그 자체**임.

이제 막 하나씩 들어감.

---

# 1막 — Hysteresis Triage: 방향은 결론이 아니라 필터

CCW(반시계방향) loop가 보이면 반사적으로 *"아 effect compartment 붙이면 되겠네"* 라고 가는 게 학생의 첫 실수임. 마스터의 첫 질문은 다름:

> *"이 loop 방향이 다른 hidden state로도 만들어질 수 있는가?"*

답은 **그렇다**. 그래서 방향은 *진단의 첫 단서*일 뿐 *최종 판결*이 아님.

## 1-1. 방향이 뜻하는 것

이력현상(hysteresis)이란 — *농도가 상승할 때와 하강할 때 반응이 서로 다른 경로를 따르는 현상*. R&T가 두 임상 사례로 보여줌:

- **Digoxin**(강심배당체): IV 투여 후 첫 4시간 동안 plasma는 *감소*하는데 심장 효과는 *증가*함 → 약이 표적 조직으로 늦게 들어가는 분포 지연의 임상 그림 [R&T p.234].
- **Naproxen**(NSAID): 경구 500 mg 투여 후 통증 완화에서 명확한 CCW hysteresis가 나타남 → loop collapse가 깨끗하게 작동하는 분포 지연 사례 [R&T pp.234–235].

> 📖 **R&T Fig.8-2 (p.235):** Naproxen loop에서 같은 농도가 두 시점에 서로 다른 반응에 대응하는 모습 — 방향을 단어 레이블이 아니라 *시간순 경로*로 보여줌.

## 1-2. 방향 → 후보 → 검증 순서

| 방향 | 1차 해석 | 후보 hidden state | 검증할 단서 |
|---|---|---|---|
| **CCW** | 반응이 농도보다 늦음 | 분포 지연, turnover, 느린 결합, 동조성 대사체 | dose-invariant $t_{max}$, loop collapse, repeated-dose 거동 |
| **CW** | 반응이 농도보다 일찍 약화 | 내성/탈감작, 길항성 대사체, down-regulation | 반복투여 trough, washout 후 rebound, 대사체 약리 |
| **8자형/혼합** | 경쟁하는 시간 척도 | 다중 기전 + 희소 샘플링 artifact | 더 조밀한 샘플링 + 기전 기반 실험 설계 |

## 1-3. Loop Collapse — 직관을 수치로

여기 진짜 강력한 진단 도구가 있음. 농도-반응 데이터를 그냥 그리면 CCW loop가 보이는데, $C$ 대신 $C_e$(아직 모르는 추정 농도)에 대해 다시 그리면 — **분포 지연이 정말 율속이면 loop가 단일 곡선으로 collapse됨** [R&T pp.245–246, Fig.8-14]. 그리고 *가장 깨끗하게 collapse를 만드는 $k_{e0}$ 값*이 곧 분포 지연 추정치임.

PD21이 이 도구의 운영을 보여줌. 길항제 X 실험에서 $k_{e0}\approx0.025\ \text{min}^{-1}$이 *상승부와 하강부를 하나의 매끄러운 곡선으로 묶는 값*으로 보고됨 [G&W PD21 pp.840–846]. 이게 1막 → 2막으로 넘어가는 정식 다리임.

## 1-4. 함정 — Input-Rate Artifact

R&T가 중요한 경고를 함 [R&T p.236]. *약물 주입 속도가 분포 속도나 tolerance 발달 속도를 압도하면* — 예컨대 매우 빠른 IV bolus — CW loop가 나타날 수 있음. 이건 tolerance가 아니라 *input-rate artifact*임. 더 느린 infusion이나 경구 데이터로 재검증하면 사라짐. 이 아티팩트를 tolerance로 오인하면 불필요한 Moderator 모델 피팅으로 이어짐.

> **현장 팁:** 희소 샘플링은 가짜 8자형을 만들어냄. 방향을 해석하기 전에 *농도와 반응 양쪽*에서 상승/하강을 포착할 만큼 샘플링 밀도가 충분한지부터 확인할 것. 안 그러면 loop 기하학은 *기전이 아니라 플롯팅 아티팩트*임.

## 1막 핵심 정리

- Loop 방향은 후보를 좁히는 **필터**지 **판결**이 아님.
- CCW 보이면 → loop collapse 시도 → 깨끗하면 2막($k_{e0}$), 안 깨끗하면 3막(turnover/Moderator)으로.
- CW 보이면 → input-rate artifact 먼저 배제 → 통과하면 3막(tolerance).
- "CCW = effect compartment 확정"으로 직행하면 turnover와 transduction을 link 하나로 흡수해버림.

---

# 2막 — 약물 시계 ($k_{e0}$): 다리 통행 속도

이제 본격적으로 첫 hidden state — *생체상 농도 $C_e$* — 를 들여다봄.

## 2-1. 왜 $C_e$가 필요한가

문제 setup: plasma 농도 $C(t)$는 측정됨. 그런데 약이 *실제로 작용하는 곳*(effect site, biophase)의 농도는 측정 안 됨. plasma에서 effect site로 가는 길에 시간 지연이 있으면, 농도-반응 곡선에서 CCW loop가 나타남. 

해결책: **가짜 구획**을 하나 만듦. plasma에서 effect site로 1차 분포 link로 약물이 흘러간다고 가정하고, 그 가상의 농도를 $C_e$라고 부름. 이 $C_e$는 *측정값이 아니라 반응 곡선으로부터 역추정되는 hidden state*임.

> 💡 비유로 정리하면 — $C$는 plasma라는 큰 도로의 차량 밀도, $C_e$는 effect site라는 골목으로 들어간 차량 밀도. $k_{e0}$는 그 골목 입구가 얼마나 빨리 열리는지 — *문 열리는 속도*임.

## 2-2. 핵심 ODE — 외울 거 하나

복잡한 닫힌 해 따위 안 외워도 됨. 운영에 쓰는 형태는 이 한 줄임:

$$
\underbrace{\frac{dC_e}{dt}}_{\text{Ce 변화율}}=\underbrace{k_{e0}}_{\text{$k_{e0}$ 추종속도}}\left(\overbrace{C}^{\text{혈장 농도}}-\overbrace{C_e}^{\text{생체상 농도}}\right)
$$

이게 왜 좋냐 — *구동 함수 $C(t)$에 뭘 넣든 작동*함. 선형 PK든, 비선형 PK든, table function이든. 그래서 NONMEM에서 받아들이기 매우 깔끔함 [G&W p.269; PD21 pp.840–841].

참고로 IV bolus 1구획 PK일 때의 닫힌 해도 알아둘 가치는 있음 — 직관용임:

$$
\underbrace{C_e}_{\text{생체상 농도}}=\overbrace{\frac{\underbrace{k_{e0}}_{\text{$k_{e0}$ 평형화}}\underbrace{D}_{\text{투여량}}}{\underbrace{V_c}_{\text{Vc 희석공간}}\left(\underbrace{k_{e0}-K}_{\text{속도 차}}\right)}}^{\text{농도 스케일}}\left(\overbrace{e^{-Kt}}^{\text{혈장 감소}}-\overbrace{e^{-k_{e0}t}}^{\text{생체상 추종}}\right)
$$

이 형태가 단순화 가정 두 개를 깔고 있음 — $k_{1e}=k_{e0}$(유입 = 평형화)와 $K_p=1$(분배비=1). 이건 *보편적 물리 등식이 아니라*, **두 파라미터를 따로 식별할 수 없어서 적용하는 표준 단순화**임 [G&W pp.263, 265]. 즉 — 데이터가 너 한테 "$k_{e0}$ 하나만 줄게"라고 양보한 거지, 자연이 그렇게 생겼다는 게 아님.

| 파라미터 | 단위 | 의미 |
|---|---|---|
| $C_e$ | concentration | effect site 농도(역추정) |
| $C$ | concentration | plasma 농도(측정/구동) |
| $k_{e0}$ | $\text{time}^{-1}$ | plasma-biophase 평형 속도 |
| $K$ | $\text{time}^{-1}$ | plasma 제거 속도 |
| $V_c$ | volume | central dilution space |

## 2-3. $k_{e0}$의 임상적 함의 — 마취과 의사가 외우는 그 시간

위 ODE의 step-input response가 정의하는 평형 반감기는 한 줄로 떨어짐:

$$
\overbrace{t_{1/2,\,\text{equilibrium}}}^{\text{Ce가 Cp에 평형 도달하는 반감기}} = \frac{\underbrace{\ln 2}_{\text{반감기 상수}}}{\underbrace{k_{e0}}_{\text{$k_{e0}$ 평형화 속도}}}
$$

이게 마취·중환자 의사들이 외워두는 *실제로 의사결정을 바꾸는* 시간임. *"새 dose의 effect는 언제 시작되나?"*의 답은 plasma $t_{1/2}$가 아니라 **이 평형 반감기**임. 도입부에서 깔았던 그 표를 정식으로 가져옴:

| 약물 (분류) | $t_{1/2,k_{e0}}$ | 임상적 onset/offset 특성 | 출처 |
|---|---:|---|---|
| **Remifentanil** (μ-opioid, ultra-short-acting) | ≈ 1 min | 초고속 onset/offset, TCI 마취 표준 | 마취 임상약리 |
| **Fentanyl** (μ-opioid) | ≈ 6 min | spectral edge 반응 기준 6.4 min | [G&W Table 3.9, p.269] |
| **Morphine** (μ-opioid, hydrophilic) | ≈ 2 h | BBB 침투 느림, onset 지연 큼 | R&T 5e Ch.8 |

세 약물이 같은 receptor에 작용하지만 *분포 시계의 길이만으로* 임상에서 완전히 다른 약물처럼 행동함. **Remifentanil은 plasma에서 사라지면 그 자리에서 effect도 사라짐. Morphine은 plasma 농도가 peak를 찍은 뒤에도 한참 동안 effect가 여전히 상승 중**임. → 이래서 2막의 분포 지연 개념이 *infusion 중단 시각, 추가 bolus 결정, recovery room 관찰 시간* 같은 임상 의사결정 timing에 그대로 떨어짐.

> 💡 **출처 경계 주의:** Fentanyl 6.4 min은 G&W Table 3.9가 spectral edge 반응 기준으로 명시한 anchor임 [G&W p.269]. Remifentanil ~1 min과 morphine ~2 h는 R&T 5e Ch.8 pp.236–248의 onset-offset 논의와 마취 임상약리 문헌의 통상 anchor임 — *교과서가 동일 표로 묶어 제시하지는 않으니*, 인용 시 1차 문헌(Minto et al. *Anesthesiology* 1997; Lötsch et al. *Anesthesiology* 2002)을 함께 확인하는 게 안전함.

G&W Table 3.9가 정리한 다른 약물들도 같은 카탈로그 안에 들어옴 [G&W p.269]:

- **Terbutaline**(β2-agonist 기관지확장제) FEV-1 7.5 min
- **Theophylline**(메틸잔틴) FEV-1 11 min
- **d-Tubocurarine/Vecuronium**(비탈분극성 근이완제) 4 min
- **Fentanyl** spectral edge 6.4 min
- **Quinidine**(Class Ia 항부정맥) QT 8 min

> 📖 **G&W Fig.3.53 (p.263):** plasma → $C_e$ → 반응-시간으로 이어지는 흐름. $C_e$가 직접 측정되지 않고 반응 곡선으로부터 역추정되는 이유가 시각적으로 드러남.

## 2-4. ⚠️ 경계 — Succinylcholine은 별개 사례

자주 헷갈리는 게 있음. **Succinylcholine**(탈분극성 근이완제) 0.5 mg/kg IV에서 $T_{50}\approx6$ min, $k\approx0.2\ \text{min}^{-1}$로 80→20% 반응 감소가 약 22%/min임 [R&T pp.249–256]. 이건 *용량-지속시간 예시*임. **G&W Table 3.9의 $t_{1/2,k_{e0}}=4$ min 사례로 잘못 라벨링하면 안 됨.** 같은 4 min 시계로 보여도 가리키는 게 다른 양임.

## 2-5. PD20 — 단회투여의 한계가 드러나는 자리

PD20이 단회투여 effect compartment 추정의 한계를 보여주는 정식 사례임. 진통제 IV bolus, $D=45\ \mu\text{g/kg}$, $V=1\ \text{L/kg}$, $K=0.50\ \text{h}^{-1}$, $E_{max}\approx3{-}5$, $EC_{50}\approx1.5\ \mu\text{g/L}$, $k_{e0}\approx0.1\ \text{h}^{-1}$ [G&W pp.836–839]. **단일 용량이라서 $EC_{50}$ 정밀도가 낮음**. → 그래서 단회투여 effect compartment 모델의 *고유 한계*를 보여주는 사례임.

## 2-6. ☠️ 가장 위험한 함정 — $EC_{50}$ 용량 분기 패턴

여기가 진짜 손이 떨려야 하는 자리임. **회전(turnover)으로 생성된 데이터를 effect compartment 모델에 억지로 끼워 맞추면, 용량별 피팅에서 생물학적으로 말이 안 되는 $EC_{50}$/$E_{max}$/$n$ 변화가 나옴.** G&W §3.9.7 Table 3.10의 그 유명한 예시 [G&W p.271]:

$$
\overbrace{\text{dose 1: } EC_{50}=0.681}^{\text{저용량}} \quad\to\quad \overbrace{\text{dose 10: } EC_{50}=4.85}^{\text{중용량}} \quad\to\quad \overbrace{\text{dose 100: } EC_{50}=0.941}^{\text{고용량}}
$$

용량 사이에 $EC_{50}$이 **약 7배 분산**됨. 이게 뭘 뜻하냐 — 모델은 수렴했고, 각 용량 fit이 따로 보면 그럴듯한데, **세 용량을 같이 보면 "수용체 민감도가 용량에 따라 7배 변한다"는 생물학적으로 비현실적인 결론**을 강요받음. 

이런 패턴이 나오면 결론은 하나임:

> **Link 모델이 회전/적응 misspecification을 강제로 흡수하고 있다.**

이 패턴을 §6에서 **Signature 1: $EC_{50}$ 용량 분기**라는 이름으로 정식 진단 시그니처로 등록함.

> 📖 **G&W Fig.3.59와 Table 3.10 (p.271):** 회전 데이터를 effect compartment에 피팅한 결과. *Fig.3.59는 PD13이 아니라 §3.9.7/Table 3.10(PD12 데이터)에 해당함.* 자료 인용 시 자주 헷갈리는 자리니까 정확히 적을 것.

## 2막 핵심 정리

- CCW + 선형 PK + dose-invariant $t_{max}$ + 단일 $k_{e0}$로 loop collapse가 깨끗 → effect compartment 가설 살아남음.
- 위 네 조건 중 하나라도 흔들리거나 용량별 $EC_{50}$이 migration하면 → **다른 hidden state가 link 모델 뒤에 숨어있다는 신호**. 3막으로 escalation.
- 단일 용량 데이터로는 $k_{e0}$/$k_{out}$/$k_{off}$를 구분 못함(PD21 trap).
- $C_e$는 측정값이 아닌 *추정되는 hidden state*. 그래서 $k_{e0}$ 추정 품질은 *반응의 상승·하강 정보가 얼마나 잘 잡혔는가*가 결정함.

---

# 3막 — 시스템 시계 ($k_{out}, k_{tol}$): 수조와 모더레이터

2막의 loop collapse가 깨끗하지 않거나, 반복투여에서 carry-over가 보이면 — 늦는 게 *약*이 아니라 **시스템 자체**임. 다리 통행 속도에서 수조 배수 속도로 무게중심이 옮겨감.

## 3-1. 임상 장면부터 — Nitroglycerin 작업자의 일주일

3막의 핵심 직관을 가장 잘 보여주는 임상 일화가 *"월요일 두통, 일요일 angina"* 임 — G&W Fig.3.71의 hat TDS 작업자 사례 [G&W pp.284–286].

이야기는 이러함. **Nitroglycerin**(유기질산염 혈관확장제) 모자 제조 공장 작업자들은 평일 5일 내내 nitroglycerin에 피부로 노출됨. 월요일 출근 첫날에는 두통이 심함 (혈관 확장 효과 full). 화요일부터 두통이 점점 줄어듦 (**tolerance** 발달). 금요일쯤이면 두통 없음. 그런데 — 토요일과 일요일에 약 노출이 없어진 뒤, 일요일에 *baseline을 넘어선 vasoconstriction*으로 **angina**가 생김 (**rebound**). 월요일 출근하면 다시 두통 시작. 

이게 왜 충격적인 그림이냐 — **tolerance와 rebound가 동일한 작업자의 일주일에 다 나타남**. 두 현상이 따로 떨어진 게 아니라, **같은 ODE 쌍의 두 phase**라는 거임. 

같은 구조의 변주가 *β-agonist의 점진적 desensitization, opioid의 점진적 내성, cocaine의 급성 심혈관 tolerance* — 다 임상에서 익숙한 약리학적 현상으로 끊임없이 등장함 [G&W pp.284–286, 295–296].

> 💡 **3막의 단 하나 키워드:** *시스템 기억*. 약이 사라져도 시스템이 약물 노출의 흔적을 한동안 기억함. 그 기억이 tolerance를 만들고, 또 같은 기억이 rebound를 만듦.

## 3-2. 모더레이터 $M$ — 시스템 기억의 ODE 구현

Moderator 모델이 그 *시스템 기억*을 수학적으로 잡는 방법임. 반응 $R$을 *뒤따라* 형성되는 지연된 반조절 상태 $M$이 있고, $M$이 반응 방정식을 *되받아 미는* 구조임:

$$
\underbrace{\frac{dR}{dt}}_{\text{R 변화율}}=\overbrace{k_{in}S(C)}^{\text{자극 입력}}-\overbrace{k_{out}M}^{\text{M 억제}}
$$

$$
\underbrace{\frac{dM}{dt}}_{\text{M 변화율}}=\underbrace{k_{tol}}_{\text{$k_{tol}$ 적응속도}}\left(\overbrace{R}^{\text{현재 R}}-\overbrace{M}^{\text{지연 M}}\right)
$$

| 파라미터 | 단위 | 의미 |
|---|---|---|
| $R$ | response unit | 관찰/모델링 반응 수준 |
| $M$ | response unit | 지연된 반조절 상태 = **시스템 기억** |
| $k_{in}$ | response/time | 반응 생성률 |
| $k_{out}$ | $\text{time}^{-1}$ | 반응 소실/회전 속도 |
| $k_{tol}$ | $\text{time}^{-1}$ | moderator 적응 속도 |
| $S(C)$ | dimensionless | 약물 자극 함수 |

> 💡 비유 — $R$은 지금 체온계가 가리키는 숫자, $M$은 뒤늦게 따라오는 자동온도조절기임. 약물이 사라져도 조절기가 한동안 이전 방향으로 밀고 있어서 rebound가 생기는 거임.

## 3-3. 부호가 음수여야 하는 *수학적 이유*

Moderator $M$이 반응 방정식에 *마이너스* 부호로 들어가는 게 임의의 모델링 선택이 아님 — **homeostasis를 만들어야 하는 모든 모델의 구조적 안정성 요구사항**임. 만약 부호가 반대였다면 ($+M$이라면), 약물 자극 → $R$ 증가 → $M$ 증가 → 다시 $R$ 증가… 시스템이 자기증폭해서 발산함. 음의 되먹임 부호 하나가 *Moderator 모델을 homeostatic하게 만드는 유일한 구조*임.

이 부호 하나가 PD13 Model II가 다른 후보들을 압도하는 *수학적 정합성의 출처*임 [G&W pp.297–300].

## 3-4. 자극이 크면 *겉보기* 반감기가 짧아짐

기저 상태에서 $S(C)=1$이면 $R_0=k_{in}/k_{out}$임 [G&W pp.299–300]. 정상상태에서는 $dM/dt=0$이라 $R=M$임 (단순형):

$$
\underbrace{S(C)=1}_{\text{기저 자극}},\quad \underbrace{R_0=\frac{k_{in}}{k_{out}}}_{\text{기저 R}},\quad \underbrace{\frac{dM}{dt}=0}_{\text{정상상태}}\Rightarrow \underbrace{R=M}_{\text{M=R}}
$$

그리고 *겉보기* 반응 반감기는 [G&W p.299, Eq.3:204]:

$$
\underbrace{t_{1/2,k_{out}}}_{\text{겉보기 반감기}}=\frac{\overbrace{\ln 2}^{\text{반감기 상수}}\,\overbrace{R_0}^{\text{기저 R}}}{\underbrace{k_{in}}_{\text{생성률}}\,\underbrace{S(C)}_{\text{약물 자극}}}
$$

이게 *"왜 고용량에서 tolerance가 더 빨리 발달하나"* 의 수학적 답임. 분모에 $S(C)$가 들어있어서, **자극이 클수록 (고용량/강한 약) 같은 kinetic constant 하에서도 effective time scale이 짧아짐**. kinetic 자체가 빨라진 게 아니라 driver가 세져서 빨라 보이는 거임.

> 💡 비유 — 같은 배수관이라도 물탱크 압력이 더 크면 수위 변화가 더 빨라 보임. 관이 굵어진 게 아니라 미는 힘이 세진 거임.

## 3-5. AUC 비대칭성 — 내장된 진단 시그니처

Moderator 시스템의 특징적 그림이 있음. dosing 중 baseline 상방 효과 면적($AUC_E$)이 일반적으로 washout 후 baseline 하방 rebound 면적($AUC_R$)보다 **큼** [G&W Fig.3.82, p.298]:

$$
\underbrace{AUC_R}_{\text{rebound AUC}}<\underbrace{AUC_E}_{\text{효과 AUC}},\qquad \underbrace{AUC_R\approx AUC_E}_{\text{대칭이면 경고}}
$$

왜 그러냐 — dosing 중에는 *약물 자극 + 상승 중인 $M$*이 함께 $R$을 미는 반면, washout 후에는 *잔류 $M$만이* 편차를 만들기 때문임. 임상에서 이 비대칭이 명백히 보이는데 fit한 모델이 $AUC_R \approx AUC_E$를 예측하면 — **moderator 구조 설정이 잘못된 것**.

## 3-6. PD13 — 반복 IV infusion의 정식 사례

PD13이 3막의 교과서적 anchor임. 일반 turnover, Moderator, pool/precursor 세 후보 모델을 비교한 사례 [G&W pp.805–809]. 결론은 Model II(Moderator)가 압도적 승리 — 하지만 *왜 이기는가*를 AIC/WRSS만 보고 끝내면 절반만 학습한 거임. Table 13.1 전체를 읽는 법이 중요함 [G&W p.808]:

| 파라미터 | Model I (no FB) | **Model II (Moderator)** | Model III (pool/precursor) |
|---|---:|---:|---:|
| $k_{in}$ | 21 | **30** | 94 |
| $k_{out}$ | 7.3 | **2.9** | 35 |
| $k_{tol}$ | — | **4.2** | 0.05 |
| $EC_{50}$ / $IC_{50}$ | 390 | **350** | 270 |
| $E_{max}$ / $I_{max}$ | 4.8 | **9.8** | 0.84 |
| n (Hill) | — | **7.4** | — |
| AIC | −39.0 | **−97.5** | −43.5 |
| WRSS | 0.33 | **0.083** | 0.28 |

진짜 mechanistic 발견은 — **Model II의 $k_{tol}=4.2 > k_{out}=2.9$**, 즉 *tolerance 발달 속도가 response turnover 속도보다 빠름*. 이 부등식:

$$
\overbrace{k_{tol}=4.2}^{\text{$k_{tol}$ 내성속도}}>\underbrace{k_{out}=2.9}_{\text{kout turnover}},\qquad \underbrace{k_{tol}=0.05}_{\text{Model III: 비현실}}
$$

이 부등식이 *단일 infusion 안에서도* tolerance가 가시화되는 이유이고, Model III의 $k_{tol}=0.05$가 임상적으로 비현실적인 이유임. Model II는 *반복 infusion 2번째 trough가 첫 번째 trough로 단순 reset되지 않음*을 자연스럽게 예측함 — 이게 PD13이 §6의 **Signature 2: Trough drift / carry-over**의 anchor가 되는 자리임 [G&W p.808].

> 📖 **G&W Fig.13.1과 Table 13.1 (pp.806–808):** Model II의 우위를 단순한 AIC 수치가 아니라 *반복 투여 기억의 가시화*로 보여줌. 두 번째 infusion이 깨끗한 reset인지, 숨은 조절자 상태의 carry-over를 보이는지 그림으로 드러남.

## 3-7. 대안 구조들 — 알아두고 적재적소에

3막의 표준 도구는 Moderator지만, 대안 구조도 압축 맥락으로 알아둬야 함:

- **시간 의존 감쇠(Colburn–Eldon):** 시간에 따른 potency/capacity의 경험적 평탄화. 유용하지만 기전성 약하고 rebound 설명 못함 [G&W pp.291–292].
- **길항성 대사체:** 길항은 설명 가능하지만 추가 구조 없이는 rebound 못 다룸 [G&W pp.292–293].
- **내성 구획 / 반작용 기전:** 적응 시스템을 위한 대안적 상태변수 형식 [G&W pp.293–295].
- **Pool/precursor (PD13 Model III):** 완전 내성만 예측, 부분 내성 설명 불가; Model II에 열등 [G&W pp.807–808].

## 3막 핵심 정리

- **반복 노출 중 효과 감소 + 약물 중단 후 rebound가 한 그림에 보임** → 같은 ODE 쌍의 두 phase. Moderator $M$이 지배함.
- 핵심 부등식: $k_{tol} > k_{out}$이면 단일 노출 안에서도 tolerance가 가시화됨.
- AUC 비대칭($AUC_R < AUC_E$)이 명백한데 모델이 대칭 예측하면 → 구조 오설정.
- "rebound = 약물이 남은 효과"로 등치하지 말 것. **남는 건 약물이 아니라 시스템 기억 $M$**.

---

# 4막 — 신호 시계 ($n \times \tau$): 릴레이 경주

3막의 Moderator $M$ 하나로도 onset 형상이 안 맞으면 — 늦는 게 *약*도 *시스템 회전*도 아니라, **측정 반응까지의 신호 전달 cascade**임. 수조 배수 속도에서 릴레이 경주의 총 통과시간으로 넘어감.

## 4-1. Single vs Relay — Onset 형상이 다름

직관부터 잡자. **1차 ODE 하나**는 $t=0$에서 *최대 기울기*로 출발해서 지수적으로 부드럽게 접근함 — 즉각 출발하는 *단거리 경주*임. 반면 **여러 1차 ODE 연쇄**는 — 첫 주자가 출발해도 마지막 주자가 도착할 때까지 결승선의 반응은 *느리게* 그리고 *S자형으로* 나타남. **릴레이 경주**임:

```
Single (n=1):   t=0에서 최대 slope → 부드러운 지수 접근
Transit (n=3):  t=0에서 slope ≈ 0  → 지연된 sigmoidal 상승
```

핵심 차이는 — *t=0에서의 출발 기울기*. 단일 link 모델은 즉시 움직임. Transit chain은 *기다림*. 데이터에 "지연된 sigmoidal onset"이 보이면 단일 link로는 흉내 못 냄.

## 4-2. ODE — 순차적 1차 연쇄

수용체-구동 단계:

$$
\underbrace{\frac{dR_e}{dt}}_{\text{Re 변화율}}=\underbrace{\frac{1}{\tau}}_{\text{단계 전달속도}}\left(\overbrace{E_0S(C)}^{\text{목표 반응}}-\overbrace{R_e}^{\text{현재 Re}}\right)
$$

순차적 transit compartments:

$$
\underbrace{\frac{dR_i}{dt}}_{\text{Ri 변화율}}=\underbrace{\frac{1}{\tau}}_{\text{단계 전달}}\left(\overbrace{R_{i-1}}^{\text{상류 상태}}-\overbrace{R_i}^{\text{현재 상태}}\right),\quad \underbrace{i=1,2,\ldots,n}_{\text{단계 인덱스}}
$$

관찰되는 반응은 *연쇄의 최종 하류*:

$$
\underbrace{R_{obs}}_{\text{관찰 반응}}=\underbrace{R_n}_{\text{최종 transit}}
$$

각 단계의 통과시간 $\tau$와 분획 회전율 $k_{out,stage}=1/\tau$는 *동일하다고 가정*함 — 이건 identifiability를 위한 단순화임 [G&W pp.323–325].

여기서 헷갈리지 말 것 — 4막의 지연되는 건 *약물의 이동*이 아니라 *반응 신호의 전달*임. 2막은 "약이 부위에 도달했는가", 4막은 "신호가 측정 지점에 도달했는가". **서로 다른 질문**이고 서로 다른 hidden state임.

> 📖 **G&W Fig.3.98–3.99 (p.323):** "약물이 부위에 늦게 도달함"과 "측정 반응까지의 신호 전파가 느림"을 시각적으로 분리해서 보여줌 — 15–20시간 onset 지연 패턴 포함.

## 4-3. PD35 — n 선택의 운영 가이드

PD35가 4막의 교과서적 anchor임. 건강한 남성 지원자에서 3가지 용량(기저 저용량 $C_0=1.05$ nmol/L, 4배, 16배), $K=0.0228\ \text{h}^{-1}$, 반감기 약 30시간 [G&W pp.910–914]. **단순한 1-state 간접반응으로는 15–20시간 onset 지연을 못 잡아냄.** 그래서 transit chain이 필요해진 사례임.

Table 35.1의 모델 비교 시퀀스 [G&W p.914]:

| n (단계 수) | $EC_{50}$ | $E_{max}$ | $\tau$ (h) | $E_0$ | WRSS |
|---:|---:|---:|---:|---:|---:|
| 1 | 0.33 | 7.2 | 20 | 15 | 1319 |
| 2 | 0.34 | 6.0 | 13 | 18 | 789 |
| **3** | **0.35** | **5.4** | **9.8** | **19** | **642** |
| 4 | 0.35 | 5.1 | 7.8 | 20 | 632 |
| 5 | 0.34 | 4.8 | 6.4 | 20 | 682 |

WRSS만 보면 $n=4$가 약간 더 낮음 (642→632). 그런데 $n=5$에서 *악화*됨 (632→682). 이 시퀀스가 가르치는 건 셋임:

1. **$n=1$은 명백히 부족함** (1319→789, 거의 절반으로 떨어짐).
2. **$n=3$이 실용적으로 충분함** (789→642, 또 한 번 의미 있는 개선).
3. **$n=4$부터는 정보 한계** (642→632→682, plateau 후 악화).

여기서 *"왜 $n=4$ 안 고르고 $n=3$ 가나"* 라는 질문이 나옴. 답은 — **$n$은 실제 생물학 단계 수가 아니라 *데이터가 해상할 수 있는 cascade 깊이*임.** $n=4$의 미미한 WRSS 개선은 *데이터가 더 미세한 구조를 못 본다*는 사인이지, *진짜로 4단계가 있다*는 사인이 아님. 절약 원칙(parsimony)이 $n=3$을 추천함.

## 4-4. ⚠️ $n \times \tau$가 *정확히* 상수가 아닌 이유

자주 잘못 외워지는 게 — *"$n$과 $\tau$가 trade-off라서 $n \times \tau$는 상수"*. 사실은 *비슷한 범위에 머무르지만 정확히 상수는 아님*. Table 35.1을 직접 곱해보면 [G&W p.914]:

| $n$ | $\tau$ (h) | $MTT = n\times\tau$ (h) |
|---:|---:|---:|
| 1 | 20 | 20 |
| 2 | 13 | 26 |
| 3 | 9.8 | 29.4 |
| 4 | 7.8 | 31.2 |
| 5 | 6.4 | 32 |

$MTT$가 $n=1\to5$로 갈수록 **20 → 32 h로 약 60% 단조 증가**:

$$
\underbrace{MTT = n\times\tau}_{\text{총 transit time}}:\ \overbrace{20 \to 32\ \text{h}}^{\text{$n=1\to5$, 약 60\% 단조 증가}},\qquad \underbrace{EC_{50},\ E_0}_{\text{민감도/기저}}\approx \text{n 변화에도 안정}
$$

왜 이런 패턴이 나오냐 — *$n$이 커질수록 $t=0$에서 onset slope가 더 0에 가까워지면서 initial lag가 커짐*. 모델이 그 lag를 따라잡으려면 평균 지연 자체를 약간 더 늘려야 함. 그래서 $MTT$가 살짝 증가하면서 onset shape가 더 sigmoidal해짐. 

이게 4막의 핵심 직관 — **transit chain은 지연의 *크기*가 아니라 *형상*을 만든다** — 의 수치적 실체임. 그리고 데이터의 *정보 수용 한계*가 어디인지를 보여주는 운영 단서이기도 함.

## 4-5. 임상 응용 — Friberg-Karlsson Myelosuppression 모델

4막이 추상적 도구로만 안 끝남. *항암제 호중구 감소·회복(myelosuppression)의 표준 PD 모델*인 Friberg-Karlsson 모델이 정확히 이 transit chain 골격 위에 세워져 있음 [Friberg LE et al. *J Clin Oncol* 2002;20(24):4713–4721; 교과서 외 임상 응용 사례].

구조: 골수 전구세포(proliferating cells) → **3단계 maturation transit chain** → 순환 호중구. 약물의 cell-killing은 proliferating cells에 작용, 순환 호중구 감소 시 음의 되먹임이 골수 생산을 재자극:

$$
\underbrace{\frac{dProl}{dt}}_{\text{골수 전구세포}}=\overbrace{k_{prol}\cdot Prol\cdot\left(1-\underbrace{E_{drug}(C)}_{\text{cell-killing}}\right)\cdot\overbrace{\left(\frac{\underbrace{Circ_0}_{\text{기저 호중구}}}{Circ}\right)^{\gamma}}^{\text{음의 되먹임 보상}}}^{\text{생성 (자기증식 + 약물억제 + 보상)}}-\underbrace{k_{tr}\cdot Prol}_{\text{다음 단계로 이행}}
$$

$$
\underbrace{\frac{dTransit_i}{dt}}_{\text{transit chain $i=1,2,3$}}=\overbrace{k_{tr}\cdot Transit_{i-1}}^{\text{상류 유입}}-\underbrace{k_{tr}\cdot Transit_i}_{\text{하류 유출}}
$$

$$
\underbrace{\frac{dCirc}{dt}}_{\text{순환 호중구}}=\overbrace{k_{tr}\cdot Transit_3}^{\text{maturation 완료}}-\underbrace{k_{circ}\cdot Circ}_{\text{소실}}
$$

이 모델 하나에 이 강의의 도구가 *거의 다* 들어감:
- **Transit chain $n\times\tau$** = 4막 (cascade depth = 3)
- **음의 되먹임 보상** $(Circ_0/Circ)^{\gamma}$ = 3막 Moderator 직관 (homeostatic 구조)
- **간접반응 골격** $k_{prol}$ vs $k_{circ}$ = 이전 세션의 $k_{in}/k_{out}$
- **약물 자극 함수** $E_{drug}(C)$ = $E_{max}$/Hill의 cell-killing 적용형

이 모델이 *across-drug standard*가 된 이유는 — *약물이 바뀌어도 transit chain 구조와 $k_{tr}$이 유사하게 유지*되고, *cell-killing 항만 약물별로 다름*. 4막이 가르치는 한 문장 — **신호 시계는 약물이 아니라 시스템에 속한 시계** — 이 임상 차원에서 확인되는 자리임. 호중구 nadir 시각과 회복 시각이 *왜 약물별로 일정한 패턴을 보이는가*에 대한 답이 이 구조에 있음.

## 4-6. 확장 — Black-Leff Operational Model (효력 차원)

4막의 transit chain은 *시간 차원*의 transduction임. 그런데 *효력(efficacy) 차원*에서 같은 "수용체 → 측정 반응" 연쇄를 재구성하는 모델이 따로 있음 — **Black & Leff의 operational model of agonism** [Black JW, Leff P. *Proc R Soc Lond B* 1983;220(1219):141–162; 교과서 외 임상 응용 사례].

Hill 형태의 일반화 표현:

$$
\overbrace{E}^{\text{관찰 반응}} = \frac{\underbrace{E_m}_{\text{시스템 최대}} \cdot \underbrace{\tau^n}_{\text{효력$^n$}} \cdot \underbrace{[A]^n}_{\text{약물 농도$^n$}}}{\overbrace{(K_A + [A])^n}^{\text{비점유 항}} + \overbrace{\tau^n \cdot [A]^n}^{\text{점유 항}}}
$$

여기서 $\tau$는 *transducer ratio* — 약물-수용체 복합체가 측정 반응으로 변환되는 효율을 나타내는 **무차원 효력 지표**임. ⚠️ **transit chain의 $\tau$(시간 차원)와 기호만 같고 의미는 완전히 다름.** 같은 글자가 다른 시계를 가리키는 PD21 trap이 여기서도 반복됨.

Hill 지수 $n=1$의 단순 hyperbolic 형태:

$$
\underbrace{E\big|_{n=1}}_{\text{Hill }n=1\text{의 반응}} = \frac{\overbrace{E_m \cdot \tau \cdot [A]}^{\text{최대 효과 스케일}}}{\underbrace{K_A + [A]\cdot(1+\tau)}_{\text{관찰 EC50을 결정}}}
$$

관찰되는 $EC_{50}^{obs}$와 실제 친화도 $K_A$의 관계:

$$
\overbrace{EC_{50}^{obs}\bigg|_{n=1}}^{\text{Hill }n=1\text{의 관찰 EC50}} = \frac{\underbrace{K_A}_{\text{실제 친화도}}}{\underbrace{1+\tau}_{\text{효력 보정}}}
$$

→ $\tau \gg 1$(full agonist)이면 $EC_{50}^{obs} \to K_A/\tau$로 매우 작아짐. $\tau \ll 1$(partial agonist)이면 $EC_{50}^{obs} \to K_A$로 진짜 친화도에 수렴함. **단일 $E_{max}$/Hill 피팅만으로는 $\tau$와 $K_A$가 분리 안 됨.** 분리하려면 partial agonist 시리즈 비교 실험이나 receptor reserve를 조작하는 *추가 실험 설계*가 필요함.

| 약물 (분류) | 효력 특성 | Operational model 함의 |
|---|---|---|
| **Buprenorphine** (μ-opioid partial agonist) | $\tau$가 morphine보다 낮음 | full agonist 대비 ceiling effect, $E_{max}^{obs} < E_m$ |
| **Aripiprazole** (D2 partial agonist) | low $\tau$, 차단·자극 동시 | functional selectivity, antipsychotic + 부작용 감소 |
| **Biased agonist** (G-protein vs β-arrestin) | 경로별 $\tau$가 다름 | 차세대 GPCR 후보 (TRV130 계열 등) |

> 💡 **Transit chain과 Operational model은 *경쟁이 아니라 직교 차원***임. Transit chain은 *시간 차원의 신호 시계*, operational model은 *효력 차원의 신호 강도*. Partial agonist 데이터를 만났을 때 *어느 차원이 부족한가*를 먼저 물을 것 — onset 형상이 안 맞으면 transit chain($n \times \tau_{transit}$), 점근선 높이($E_{max}^{obs} < E_m$)가 안 맞으면 operational $\tau$.

## 4막 핵심 정리

- onset이 즉각 지수형이 아니라 *delayed sigmoid*면 → transit chain $n\times\tau$ 검토.
- $n$은 *실제 생물학 단계 수가 아니라 데이터가 해상하는 cascade 깊이*. PD35 시퀀스가 plateau에 도달하는 자리에서 $n$ 선택 종료.
- $MTT = n\times\tau$는 *비슷한 범위에 머무르지만 정확히 상수는 아님* (약 60% 증가).
- 4막의 도구가 임상 oncology의 표준 PD 모델(Friberg-Karlsson)의 절반을 차지함.
- Partial agonist의 $E_{max}^{obs}$가 안 맞으면 Black-Leff operational model로 확장.

---

# 막간 — 5개 혼동 쌍 (Confusion Pairs)

4막을 다 봤으면, 이제 학생들이 *어디서 가장 자주 미끄러지는지* 정리할 차례임. 다섯 자리에 anchor 박아둠.

> **참고:** *내성 vs 반동*은 혼동 쌍이 아님 — 같은 Moderator 방정식의 두 phase임. Card 3 §3-1, §3-5에서 이미 정착했음. 대신 Pair 4는 *내성 vs 적응* (시스템 피로 vs 항상성 재보정)을 다룸.

---

## Pair 1 — $k_{e0}$ vs $k_{out}$ vs $k_{off}$ (★ 가장 치명적)

| 차원 | $k_{e0}$ | $k_{out}$ | $k_{off}$ |
|---|---|---|---|
| 무엇의 시계? | Plasma–생체상 평형 | 시스템 회전 | 수용체-리간드 해리 |
| 비유 | **다리 통행** | **수조 배수** | **빗장 풀림** |
| 대표 모델 | 효과구획 (2막) | 간접반응/Moderator (3막) | 수용체 결합 |
| 단위 | $\text{time}^{-1}$ | $\text{time}^{-1}$ | $\text{time}^{-1}$ |
| PD21 값 | 0.025 | 0.031 | 0.018 [G&W p.846] |
| 구분 방법 | 선형 PK 하 $t_{max}$ + loop collapse | 회전/회복 + 반복투여 | 결합/washout + 표적 정보 |

**⚡ 기억 고리:** 시계 바늘 길이($\text{time}^{-1}$)가 같아도 *가리키는 대상*이 다 다름 — 다리, 수조, 빗장. PD21에서 셋이 0.025/0.031/0.018로 비슷하게 나온 건 *우연이지 동치가 아님*. Single-dose로는 구분 불가 → dose stratification, repeated dosing, washout 같은 richer design 필수.

**☠️ 치명적 타격:** 회전 데이터를 분포/link 모델로 피팅하면 *생물학적으로 비현실적인 dose-dependent $EC_{50}$/$E_{max}$/$n$*이 나옴 [G&W pp.271–272]. 이게 §6 Signature 1의 anchor임. 규제 정당화 상황에서 이 패턴이 보이면 reviewer가 대안 모델 비교와 민감도 분석을 요구함.

### 확장 — Drug-Target Residence Time

$k_{off}$의 임상적 의미를 *해리 속도 그 자체*로만 좁히면 현대 신약 개발 맥락을 놓침. **Drug-target residence time** $\bar{t}_R = 1/k_{off}$가 *plasma kinetics가 끝난 뒤에도 약물이 표적에서 작용하는 평균 시간*을 나타냄 [Copeland RA. *Nat Rev Drug Discov* 2016;15(2):87–95; 교과서 외 임상 응용].

$$
\overbrace{\bar{t}_R}^{\text{residence time}} = \frac{1}{\underbrace{k_{off}}_{\text{$k_{off}$ 해리}}},\qquad \underbrace{\bar{t}_R^{(PD21)}}_{\text{PD21 residence time}} = \frac{1}{\overbrace{0.018\ \text{min}^{-1}}^{\text{PD21의 $k_{off}$}}} \approx \underbrace{56\ \text{min}}_{\text{표적 머무름 시간}}
$$

PD21의 $k_{off}=0.018$이 약물-표적 복합체가 *평균 56분 머무름*을 뜻함. **Covalent inhibitor**(KRAS G12C inhibitor, EGFR T790M inhibitor)와 allosteric modulator의 *plasma agnostic* 지속 효과가 이 residence time 개념에서 출발함. → 다리·수조·빗장 비유에 한 줄 추가하면 — **빗장이 풀린 뒤에도 약이 receptor를 떠나기까지 시간이 더 걸림**.

이건 3막의 $M$(시스템 기억)과는 다른 종류의 기억 — **약물-표적 결합 기억**임.

---

## Pair 2 — 효과구획 모델 vs 회전/간접반응 모델

| 차원 | 효과구획 (2막) | 회전/간접반응 (3막) |
|---|---|---|
| 지연의 출처 | 약물이 effect site로 *느리게 이동* | 약물은 즉시 작용, *반응 변수*가 느리게 변함 |
| 숨은 상태 | 생체상 농도 $C_e$ | 반응 풀 $R$ |
| 구동 관계식 | $dC_e/dt = k_{e0}(C - C_e)$ | $dR/dt = k_{in}S(C) - k_{out}R$ |
| 용량 스케일링 | 선형 PK 하 모든 용량 *동일* $t_{max}$ [G&W p.264] | $S(C)$만 변하므로 $t_{max}$가 *용량 따라 이동* |
| 반복 투여 거동 | 단일 $k_{e0}$로 loop collapse | 풀이 reset되지 않으면 *carry-over* |
| 해당 위치 | G&W §3.9, PD20/PD21 | G&W §3.10–3.11, PD13/PD20 |

$$
\underbrace{\frac{dC_e}{dt}=k_{e0}(C-C_e)}_{\text{Ce 지연}}\quad \text{vs}\quad \underbrace{\frac{dR}{dt}=k_{in}S(C)-k_{out}R}_{\text{R 지연}}
$$

**⚡ 기억 고리 — 결정적 진단 질문 하나:** *"투여량을 올리면 response peak의 timing이 달라지는가?"* 달라지면 effect compartment 깨짐 (분포 지연은 dose에 무관해야 함). 안 달라지면 turnover 가능성 높음 ($S(C)$가 커져도 분포 시계는 영향 없음).

---

## Pair 3 — CCW vs CW Hysteresis

| 차원 | 반시계방향(CCW) | 시계방향(CW) |
|---|---|---|
| 같은 농도, 두 방문 | 두 번째 방문에서 **더 강한** 효과 | 두 번째 방문에서 **더 약한** 효과 |
| 흔한 기전 | 분포 지연, 시스템 회전, 느린 결합, 동조성 대사체 | 내성, 길항성 대사체, down-regulation, *input-rate artifact* |
| 예시 | Naproxen, digoxin, warfarin 논리 [R&T pp.234–246] | Cocaine/nitroglycerin 내성 [G&W pp.284–296]; 빠른 IV bolus [R&T p.236] |
| 진단 수순 | $k_{e0}$ loop collapse 먼저 시도 | 반복 투여 확인 + input-rate artifact 배제 |
| 올바른 사용 | **첫 진단 단서** (방향만으로 mechanism 확정 ✗) | **첫 진단 단서** (방향만으로 mechanism 확정 ✗) |

**⚡ 기억 고리:** *"같은 농도라는 약속 장소에 두 번 들렀을 때, 두 번째 방문에서 더 환영받는가(CCW) 아니면 덜 환영받는가(CW)"*. 방향 자체로는 mechanism을 *결정 못함*. 후보 family를 좁힐 뿐임.

---

## Pair 4 — 내성(Tolerance) vs 적응(Adaptation)

| 차원 | 내성(Tolerance) | 적응(Adaptation) |
|---|---|---|
| 기저 기전 | 시스템 *피로* — receptor down-reg, mediator 고갈 | 항상성 *재보정* — 생리학적 되먹임 |
| 가역성 | washout 후에도 *지속* (느린 회복) | 약물 노출 종료 시 *즉각 역전* |
| 필요한 모델 요소 | hidden state $M$ (Moderator) | 음의 되먹임 setpoint 루프 |
| 시간적 시그니처 | *지속 노출 동안* 점진적 효과 감소 | *지속 노출 중에도* 반응이 기저치 접근 |
| 진단적 분리 | 약물 중단 → 느린 역전 또는 rebound | 약물 중단 → rebound 없이 빠른 복귀 |
| 해당 위치 | G&W §3.11, PD13 [pp.297–300, 805–809] | G&W §3.11 개념적 대비; 다수 생리학적 시스템 |

**⚡ 기억 고리 — 피로 vs 재보정:** Tolerance는 시간 가면서 효과 줄어드는 **시스템 피로** — *약 떨어진 뒤에도 지속됨*. Adaptation은 기저치로 돌아오려는 **항상성 재보정** — *약 떨어지면 즉각 역전*. **Reversibility 차이가 둘을 가르는 가장 강한 신호**임.

---

## Pair 5 — 단일 Effect Compartment vs Transit Chain

| 차원 | 단일 $k_{e0}$ link (2막) | Transit chain $n\times\tau$ (4막) |
|---|---|---|
| 지연되는 상태 | 약물 농도 $C_e$ | 반응 상태들 $R_1, \ldots, R_n$ |
| ODE 형태 | 1개의 1차 ODE | $n$개의 순차적 1차 ODE |
| Onset 형상 | 즉각적 평활 ($t=0$에서 최대 기울기) | 지연된 시그모이드 ($t=0$에서 기울기 0) |
| 핵심 진단 | 선형 PK 하 동일 $t_{max}$ | $n=1$이 onset 못 따라잡음, $n=1\to3$에서 WRSS 급락 |
| 앵커 | G&W §3.9, PD20 | G&W §3.13, PD35 (WRSS 1319→789→642) |

**⚡ 기억 고리 — 단거리 vs 릴레이:** Single은 **단거리 경주** — 첫 발이 곧 결승선 향함. Transit은 **릴레이 경주** — 첫 주자가 출발해도 결승선 신호는 마지막 주자 도착 때까지 기다림. 릴레이는 출발 zero slope, 단거리는 출발 maximum slope. *이 한 차이가 onset 형상 전부를 바꿈*.

---

# 진단 시그니처 사전 — Goodness-of-Fit 4대 패턴

> **출처 경계:** 아래 네 패턴은 교과서 anchor에서 도출된 *교육용 기억술*임. 패턴 자체는 G&W §3.9.7, PD13, PD35의 데이터와 표준 NONMEM 진단 플롯에서 관찰 가능하지만, *이름*은 교육적이고 교과서의 직접 명명은 아님.

모델 피팅이 수렴했는데 뭔가 안 맞는 느낌이 들면 — 재모수화 전에 데이터를 이 네 렌즈에 통과시킬 것. 각 패턴의 메시지는 하나임 — **"이 패턴이 보이면, 다음 escalation은 X"**.

## Signature 1 — $EC_{50}$ 용량 분기

- **관찰 패턴:** 용량별 individual fit에서 $EC_{50}$, $E_{max}$, $n$이 기전적 정당화 없이 큰 변동.
- **기계론적 의미:** Link 모델이 *회전/적응 효과를 강제 흡수*하고 있음.
- **교과서 근거:** G&W §3.9.7 Table 3.10 — $EC_{50}$ 0.681, 4.85, 0.941 (약 7배 분산) [G&W p.271].
- **다음 단계:** 2막(Link) → 3막(turnover/Moderator)로. *단일 $EC_{50}$이 회복되는지* 검증.

## Signature 2 — Trough Drift / Carry-Over

- **관찰 패턴:** 반복 투여에서 노출(AUC)이 비슷한데 *2번째 cycle trough가 1번째와 다름*.
- **기계론적 의미:** Hidden state가 *cycle 간 기억을 운반*. Moderator $M$이 washout되기 전에 다음 dose 도착.
- **교과서 근거:** PD13의 2번째 trough가 1번째와 같지 않다는 시그니처 [G&W pp.805–809].
- **다음 단계:** 간접반응 → Moderator(Model II). AIC/WRSS 비교, $k_{tol}/k_{out}$ 부등식 확인.

## Signature 3 — 지연된 / S자형 Onset 잔차

- **관찰 패턴:** 단일 회전($n=1$) 모델 피팅 시, 모델은 반응이 *너무 일찍* 상승한다고 예측하지만 데이터는 *늦게, 급격히* 상승. 시간 잔차가 *under-then-over-then-under* 패턴.
- **기계론적 의미:** 단일 1차 지연으로는 *평탄한 초기 phase 뒤 급격한 상승*을 못 만듦.
- **교과서 근거:** PD35 WRSS 1319→789→642 ($n=1\to3$, 약 2배 개선) [G&W p.914].
- **다음 단계:** 3막 → 4막(transit chain). 절약 원칙으로 $n$ 선택.

## Signature 4 — OFV/WRSS Plateau

- **관찰 패턴:** 구조적 시퀀스 escalation 시 OFV/WRSS가 개선 후 *plateau* → *소폭 악화*.
- **기계론적 의미:** 데이터가 해당 기전 차원에 대해 *정보 수용 한계* 도달. 추가 파라미터가 잡음 흡수 시작.
- **교과서 근거:** PD35 시퀀스 1319 → 789 → 642 → 632 → 682 ($n=4\to5$에서 악화) [G&W p.914].
- **다음 단계:** Escalation *중단*. 절약 원칙 지지 모델 선택. *"데이터가 더 미세한 구조를 해상하지 못한다"는 사실을 문서화*.

> 🎯 **마스터의 시각:** 네 시그니처는 *서로 다른 위치*의 misspecification을 가리킴 — Signature 1은 *모델 family 오류*, 2는 *반복 노출 기억 누락*, 3은 *cascade 깊이 부족*, 4는 *데이터 해상도 한계*. 이 넷을 구분 못하면, 한 패치(예: 재모수화)로 다른 시그니처를 덮으려다 모델 자체가 손상됨.

---

# 자기점검: 능동 회상 12문항

## Q1 — 회상
효과구획 ODE를 쓰고, $k_{1e}=k_{e0}$이 사용되는 이유를 서술할 것.

**정답:** $dC_e/dt=k_{e0}(C-C_e)$ [G&W pp.268–269]. 보편적 물리 법칙이 아니라 *두 파라미터를 따로 추정할 수 없어서(identifiability) 적용하는 표준 단순화* [G&W pp.263, 265].

---

## Q2 — 적용
3개 용량 연구에서 모든 용량의 반응 $t_{max}$가 동일하게 관찰됨. 즉시 Link 모델 선택해도 되는가?

**정답:** 아님. 먼저 **선형 PK** 검증이 필요함. Same-$t_{max}$ 성질은 선형 약물 동태 가정 하에서만 진술됨 [G&W p.264]. 그 다음 dose-stratified PD 파라미터 정합성 확인.

---

## Q3 — 오류 탐지
초안에 "PD13 Table 3.10이 Link 오설정 하의 $EC_{50}$ 용량 분기를 보여준다"고 적혀 있음. 정정할 것.

**정답:** "G&W §3.9.7 Table 3.10 link-model pitfall; Fig.3.59는 PD12 데이터"로 정정. PD13은 *반복 IV infusion 내성/반동 모델 비교 사례* [G&W pp.271, 805–809].

---

## Q4 — 기전 트리아지
농도-반응 플롯이 CCW. 가능한 기전 3가지와 각각의 *추가 식별자*를 나열할 것.

**정답:** ① 분포 지연 → 선형 PK 하 $t_{max}$ 용량 불변성 + $k_{e0}$ loop collapse; ② 회전 지연 → peak shift + 시스템 회복 시간; ③ 느린 결합 → 표적/결합 또는 washout 거동. 대사체 기여는 대사체 농도/약리 데이터 필요.

---

## Q5 — PD13 추론
PD13 Model II: $k_{in}=30$, $k_{out}=2.9$, $k_{tol}=4.2$, $EC_{50}=350$, $E_{max}=9.8$, $n=7.4$, $AIC=-97.5$. AIC를 넘어서, *Model II를 기전적으로 옳은 답으로 만드는 단 하나의 파라미터 관계*는?

**정답:** **$k_{tol}=4.2 > k_{out}=2.9$**, 즉 *조절자 발달이 반응 회전보다 빠름*. 이 부등식이 단일 infusion 안에서도 내성 가시화 + 2번째 cycle carry-over를 만듦 [G&W p.808]. Model III의 $k_{tol}=0.05$는 생물학적으로 비현실적.

---

## Q6 — PD21 추론
$k_{e0}$, $k_{out}$, $k_{off}$가 모두 $\text{min}^{-1}$ 단위에 비슷한 크기. *동일한 의미*로 결론짓는 게 안전하지 않은 이유는?

**정답:** 셋은 *서로 다른 물리적/생물학적 시계* — 다리(생체상 평형), 수조(시스템 회전), 빗장(수용체 해리). PD21이 유사한 값(0.025, 0.031, 0.018 $\text{min}^{-1}$)을 보고하지만 *서로 다른 기전 모델*을 비교함 [G&W p.846].

---

## Q7 — PD35 추론
PD35 Table 35.1: $n=1\to5$, WRSS $1319\to789\to642\to632\to682$. WRSS 최소라는 이유만으로 $n=4$ 선택하면 안 되는 이유는?

**정답:** $n=4$는 $n=3$ 대비 미미한 개선(642→632), $n=5$에서 *악화*(632→682). 패턴이 $n=3$ 부근에서 *실용적 충분성 + 정보 수용 한계*에 도달했음을 보여줌. $n=3$이 절약 원칙의 선택이고, $n=4$를 "더 좋다"고 선언하는 건 *데이터가 해상하는 것 이상을 주장*하는 것 [G&W p.914].

---

## Q8 — 보스 딜레마 (압축형)
모델 A는 안정적 Link 모델이지만 dose-dependent $EC_{50}$ 만듦. 모델 B는 계산적으로 덜 안정하지만 *생물학적으로 정합적인 단일 $EC_{50}$* 유지 + 내성 포착. 어떤 원칙이 선택을 지도하는가?

**정답:** **기전적 타당성이 통계적 편의성에 우선함.** 기전 없이 dose-dependent 수용체 민감도를 함의하는 모델은 G&W §3.9.7 함정(§6 Signature 1)의 반복임. 계산적 불안정성은 *기술적 문제*지만, 생물학적으로 비현실적인 파라미터 거동은 *모델 타당성 문제*임.

---

## Q9 — 율속 단계 비교 (R&T anchor)
**Acenocoumarol**(쿠마린계, plasma $t_{1/2} \approx 15$ h)과 **phenprocoumon**(쿠마린계, plasma $t_{1/2} \approx 5$ days)은 동일 표적이지만 회복 시간이 약 한 자리수 차이. 각 약물 회복을 율속하는 단계는?

**정답:** 회복은 (i) 약물 제거(kinetics)와 (ii) 응고 인자 회전(dynamics) 중 *더 느린 과정*에 의해 율속됨 [R&T Ch.8, Fig.8-11]. **Acenocoumarol**: 약물 청소가 빠르고 응고 인자 회전($t_{1/2} \approx 1{-}2$ days)이 율속 → 회복이 *동역학에 의해 제한*. **Phenprocoumon**: 약물 청소 자체가 가장 느림 → 회복이 *동태에 의해 제한*. **Warfarin**($t_{1/2} \approx 1.5$ days)은 경계에 위치 → 임상 적정이 *민감한* 구조적 이유.

---

## Q10 — 환자 간 이력현상 변이
동일 약물을 받은 두 환자에서 환자 A는 CCW, 환자 B는 CW loop가 관찰됨. 두 가지 그럴듯한 설명은?

**정답:** ① **두 기전이 서로 다른 상대적 우세도로 동시 작동.** 분포 지연과 내성이 모두 기여할 때, 관찰 가능한 방향은 *관찰 창 동안 어느 쪽이 우세한가*에 달림 — 환자 A는 주로 분포 지연 phase, 환자 B는 주로 내성 phase에서 샘플링되었을 수 있음. 더 긴 관찰은 양쪽에서 *8자형*을 드러낼 수 있음. ② **입력 속도 vs 분포 속도 불일치.** R&T는 *약물 입력 속도가 분포 또는 내성 발달 속도보다 빠를 때*에도 CW loop가 나타날 수 있다고 명시 [R&T p.236]. 환자 간 경구 흡수 속도, infusion 속도, first-pass 차이는 *기저 기전이 같아도* 겉보기 방향을 뒤집을 수 있음.

---

## ⚡ Q11 — 보스 딜레마 ★★ (규제 방어)

CCW가 PD에서 명확. PK 선형, sampling 충분, 3개 용량에서 일관된 CCW. 두 경로 사이 결정:

- **선택지 A — 효과구획($k_{e0}$).** 즉시 구현, parameter 간결. Loop collapse 작동 시 수치 확보. **단점:** $k_{e0}$가 용량 의존적이면 정당성 흔들림, 반복투여 내성/반동 *전혀* 설명 못함.
- **선택지 B — Indirect response($k_{in}, k_{out}, S(C)$).** Mechanism이 production/loss 변화로 정당화되면 생물학적으로 더 의미. Repeated-dose에서 trough drift나 carry-over 있으면 Moderator로 확장 가능. **단점:** parameter 추정에 *더 넓은* 데이터 필요. Single-dose만으로는 $k_{in}/k_{out}$이 $C_{baseline}=k_{in}/k_{out}$ 비율로만 결정되어 individually identifiable 아님.

각 선택을 *규제 문서*에서 어떻게 방어하는가?

> **정답 — 마스터의 Trade-off 논리**

**핵심 통찰:** 어느 쪽이든 답변의 70%는 **"다른 쪽을 *왜 배제했는지*"**. 모델 선택은 *증명*이 아니라 *경쟁 가설의 체계적 기각*.

**선택지 A(Effect compartment) 방어:**
- (i) 3개 용량 모두에서 단일 $k_{e0}$ ±20%로 loop collapse 작동했다는 *수치 근거*.
- (ii) 반복투여 데이터(≥2 cycles)에서 *no trough drift, no rebound* → turnover/Moderator 기각.
- (iii) PD13(G&W p.808) 같은 turnover-data 사례와의 *비교 피팅*. 같은 데이터에 turnover fit 시 $EC_{50}$ 분기(§6 Sig.1) 또는 trough drift(§6 Sig.2)가 *나타나지 않음* 입증.
- (iv) 약물의 logP, target tissue partitioning, perfusion이 distributional delay 가설과 *일관*되는 생물학적 논거.

**선택지 B(Indirect response) 방어:**
- (i) 약물 mechanism이 receptor-mediated production/loss라는 *사전 생물학적 근거*(literature, in-vitro).
- (ii) Effect compartment를 *동일 데이터*에 fit한 결과 + dose-stratified $k_{e0}$나 $EC_{50}$ migration(§6 Sig.1) 같은 misspecification 신호 → distribution 가설 기각.
- (iii) Turnover model의 $k_{in}/k_{out}/S(C)$ 식별을 위한 *experimental design* 동반.
- (iv) Repeated-dose data가 있으면 trough drift 또는 AUC 비대칭($AUC_R < AUC_E$) → *명시적 양성 근거*.

**규제 reviewer가 *반드시 묻는* 질문:**  
> **"왜 다른 모델이 아닌가?"**

준비된 답 없으면 어느 모델이든 불충분한 정당화로 평가됨. 마스터의 작업 흐름은 *처음부터 두 모델을 같이 fit하고*, *어느 하나가 명확히 우세한 evidence*를 만든 뒤 *그 evidence를 문서화*. Fit 결과만 첨부하는 건 부족함.

**현장 단서:** Phase 1 단회투여만 있는 경우, A를 *잠정* 선택하되 **Phase 1b/2 protocol에서 반복투여 확장을 미리 *계획*할 것**. 단회투여 effect compartment 모델은 그 자체로 *반증 불가능*하기 때문임.

---

## Q12 — 제한된 샘플링에서의 메커니즘 판별 ★★

**시나리오:** 단회투여 임상시험 데이터. 비용·침습성 제약으로 plasma/effect 각 5개 시간점만. 관찰:
- Plasma는 빠르게 peak 후 단조 감소.
- 효과는 농도 peak보다 *늦게* peak, 명확한 **CCW hysteresis**.
- 두 후보 모델 (Effect compartment vs Indirect response) GOF 사실상 동등.

GOF가 비슷하다는 이유로 effect compartment 잠정 선택하면 안 되는 *구조적 이유*는? 추가로 어떤 정보를 확보해야 하나?

> **정답 — 메커니즘 판별 논리**

**1. CCW loop는 단서지 결정증거 아님.** 동일 CCW가 5가지 이상 다른 기전에서 똑같이 만들어짐.

**2. Effect compartment는 *분포·생체상 지연*. 시계는 *약물 시계*, $k_{e0}$가 지배.**

**3. Indirect response는 *반응 시스템 자체의 생성·소실 속도*. 시계는 *시스템 시계*, $t_{1/2,k_{out}}$이 본질.**

**4. 제한된 샘플링에서는 모델 식별성이 구조적으로 약함.** 단회투여 + 5 시간점은 두 모델을 수치적으로 분리할 자유도 없음. **GOF만으로 잠그면 *데이터 식별성이 아니라 prior assumption*에 의해 모델 결정됨** — 규제 검토 즉시 지적 대상.

**5. 판별을 위한 추가 정보:**
- **농도 peak 이전의 효과 sampling** — 효과가 *얼마나 빨리 움직이기 시작*하는지가 두 모델을 분리. Effect compartment: 즉각 출발 + 부드러운 ramp-up. Turnover: *느린 출발(lag-like onset)*.
- **효과 peak 전후 촘촘한 sampling** — peak 시각·형상이 hidden state 차수 폭로.
- **다른 용량 수준에서 $t_{max}$, onset, recovery 비교** — Effect compartment는 dose 변화에도 onset 변하지 않아야 함. Turnover는 §6 Sig.1/Sig.2를 자연스럽게 만듦.
- **기저선 회복과 rebound·내성 검사** — Effect compartment는 *비대칭 회복*을 설명 못함. $AUC_R < AUC_E$ 보이면 즉시 turnover로 escalation.
- **독립적 생리학적 지식** — 표지 분자의 고유 turnover 반감기, 생성·소실 속도, receptor 동태. 이 prior 없이는 데이터만으로 hidden state 명명 불가.

**6. 결론 원칙:**  
> **Delay는 단순한 시간 지연항이 아니라 hidden state를 가리키는 신호. 그 hidden state가 biophase인지 response turnover인지 구분하는 것이 이 강의의 핵심.**

---

# 마무리 — 큰 그림과 새 데이터를 받았을 때

## 이 강의의 위치

이 강의는 기본 $E_{max}$/Hill/간접반응 모델과 TMDD, PBPK-PD coupling, QSP 같은 고급 통합 PK/PD 시스템 *사이*에 위치함. 가르치는 단 한 가지는 — **세 가지 시계의 구분**:

```
약물 시계 (Drug clock)    →  $k_{e0}$          →  다리 통행 속도
시스템 시계 (System clock)→  $k_{out}$,$k_{tol}$→  수조 배수 + 자동조절기
신호 시계 (Signal clock)  →  $n \times \tau$    →  릴레이 경주 통과시간
```

| 후속 세션 | 이 강의에서 열리는 개념 | 이 강의 없으면 실패하는 것 |
|---|---|---|
| TMDD | binding/receptor state와 $k_{off}$ 해석 | $k_{e0}$·$k_{off}$ 단위 혼동 |
| PBPK-PD coupling | tissue/biophase delay vs system response | 조직분포와 생리학적 turnover 혼동 |
| QSP | downstream cascade와 feedback state | transit chain과 true biology 과해석 |

## 피상적 학습 시 실패 모드

| 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| Link overuse | $k_{e0}$ | → | dose-dependent $EC_{50}$/$E_{max}$/$n$ | turnover/transduction 비교 |
| Tolerance blindness | $M$, $k_{tol}$ | → | trough drift/rebound 누락 | 반복투여·washout 확인 |
| Cascade underfitting | $n\times\tau$ | → | delayed onset misprediction | transit chain + WRSS 변화 |
| Over-parameterization | $n$, $\tau$ | → | 정보 한계를 넘은 기전 주장 | OFV/WRSS plateau + 식별성 |
| Unit-level confusion | $k_{e0}$/$k_{out}$/$k_{off}$ | → | 같은 단위의 다른 시계 혼동 | hidden state 먼저 명명 |

(교차 참조: §6의 네 진단 시그니처가 이 모드들에 직접 대응함.)

## ⚡ Capstone — 새 데이터를 받았을 때 5초 안에 하는 일

지속적 기술의 핵심은 ODE 외우기가 아님. **피팅 전에** 데이터가 어떤 **hidden state**를 요구하는지 *보는 것*임 — 숨은 *생체상 농도*, 숨은 *적응성 조절자*, 숨은 *신호전달 상태들*. 이 구분이 *수학적으로 수렴했지만 생물학적으로 비현실적인* PK/PD 모델을 막아줌.

각 막의 hidden state를 다시 새김:
- **1막(Hysteresis Triage):** loop 방향 = 후보 좁히는 *진단 게이트*
- **2막(약물 시계):** 생체상 농도 $C_e$ (다리)
- **3막(시스템 시계):** 조절자 상태 $M$ — *시스템 기억*, drug compartment 아님 (수조)
- **4막(신호 시계):** 순차적 transit compartments $R_1, \ldots, R_n$ (릴레이)

새 PK/PD 데이터를 받으면 — 이 네 hidden state 중 **어느 것이 작동 중인지**를 *수식 쓰기 전에* 결정함. 다리, 수조, 빗장, 릴레이 — 같은 시계 단위가 가리키는 네 군데 중 어디인지 먼저 명명함. **ODE 선택은 결과이지 시작이 아님.**

> **마스터 한 줄:**  
> *A delay is not a mechanism. Name the delayed state.*  
> **지연은 메커니즘이 아니다. 지연되는 상태에 이름을 붙여라.**

---

`C-260518-000152-K7M`

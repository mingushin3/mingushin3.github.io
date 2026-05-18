# Session 11 Remastered — 같은 농도, 다른 효과
## plasma C와 PD가 따로 노는 모든 경우를 분해하는 법

> **이 자료의 위치**
> 원본(v4.2_final)이 다루는 콘텐츠·범위·수치 anchor·인용을 100% 보존하되, 학습자가 임상 현장에서 데이터를 받았을 때 **머릿속에서 자동으로 돌아가는 진단 순서**대로 다시 짠 강의 노트임. 카드 단위 분절을 풀고, 한 가지 질문("plasma C와 effect의 mismatch는 어디서 오는가?")을 척추로 삼아 8개 카드를 한 바느질로 꿰어냈음. 어미는 음슴체, overbrace/underbrace annotation 유지, [G&W pp.XXX] / [R&T pp.XXX] 인용 유지함.

---

## 0. 이 세션 한 줄로 꿴다면

임상에서 가장 답답한 순간이 있음. 약을 줬는데 **plasma 농도와 효과가 따로 노는 거임**.

- **Naproxen** 500 mg 경구를 dental pain 환자한테 주면, 같은 혈장 농도라도 농도가 올라가는 중이냐 내려오는 중이냐에 따라 통증 완화가 다름 (1–8 h) [R&T pp.234–235].
- **Aspirin** 650 mg은 혈장에서 몇 시간 만에 사라지는데 thromboxane B₂ 억제는 며칠 감 [R&T p.251].

이게 우연이 아니라 임상에서 늘 일어나는 일임. → 그래서 **plasma half-life만 보고 dose interval을 결정하면 어떤 약물에서는 맞고 어떤 약물에서는 완전히 빗나감.**

**이 세션 전체는 한 질문에 답하는 도구상자임** — "plasma C와 effect가 안 맞을 때, 그 mismatch는 어디서 오는가, 그리고 그걸 어떻게 분해해서 임상 의사결정으로 번역하는가?"

답이 될 수 있는 후보는 단 4가지뿐임. 이걸 머릿속에 박아두면 이번 세션이 전부 풀림.

| # | mismatch의 출처 | 모델 도구 | 대표 약물 |
|---|---|---|---|
| 1 | **분포 지연** — 약이 작용 부위에 늦게 도달함 | Effect compartment, $k_{e0}$ | (생체상 평형 지연) |
| 2 | **Turnover** — system이 반응을 만들고 없애는 데 시간이 걸림 | 4-Model (Models I–IV) + Pool/Precursor 확장 | Warfarin, EPO, methylprednisolone |
| 3 | **표적 소비** — 약이 표적을 영구 파괴, 새로 만들 때까지 효과 남음 | $K_{kill}$, 비가역 kill, regrowth | Aspirin, Omeprazole, Paclitaxel |
| 4 | **다른 시계가 더 느림** — PK와 PD 중 느린 쪽이 duration을 결정 | PK-clock vs PD-clock 감별 | Succinylcholine vs Warfarin |

이 표가 이번 세션의 전체 지도임. **베테랑 모델러가 데이터를 받자마자 첫 30초 안에 이 4개 후보 중 어느 쪽인지를 좁힘.** 그 다음에 NONMEM 돌리기 전에 손으로 어디까지 잠가놔야 하는지, fit이 매끄러워도 왜 결론을 미뤄야 하는지, duration 예측 공식을 언제 쓰고 언제 폐기해야 하는지가 줄줄이 갈림.

본론 들어가기 전에 한 가지만 박아둠. **이 분야 베테랑은 fit이 매끄럽다고 좋아하지 않음. 어느 시계가 가장 느린지를 증명할 수 있을 때 좋아함.** 이 차이가 이번 세션 전체를 관통하는 척추임.

---

# PART I — 진단의 첫 단추: 데이터를 받자마자 하는 일

## 1. Hysteresis 방향 — 30초 만에 가설 후보군을 좁히는 도구

학생들이 자주 빠지는 함정 하나. PK/PD 데이터를 받으면 곧장 model을 적합시키려고 NONMEM을 켬. **틀린 순서임.** 진짜 첫 단계는 종이 위에 한 개의 그림을 그리는 것임 — **plasma C(x축) vs response(y축)**, 시간 순서대로 점을 잇기.

이게 hysteresis loop임. 그리고 이 loop의 방향이 위의 4개 후보군을 즉시 가지치기해줌.

### A. Hysteresis가 뭐길래

같은 약물 농도에서 **올라가는 길과 내려오는 길의 반응이 다른 현상**임 [R&T pp.234–235]. C-R 평면에 그리면 loop가 그려짐. 같은 산을 오르내리는 두 길의 고도 기록 같은 거임 — 같은 고도라도 올라가는 중인지 내려오는 중인지에 따라 몸 상태가 다르면, 고도 하나로는 설명이 끝나지 않음.

| 패턴 | 해석 | 대표 사례 | 떠올릴 후보 |
|---|---|---|---|
| **반시계 방향 (counterclockwise)** | 반응이 농도 뒤에서 따라옴 | **Naproxen** 500 mg 경구(NSAID; 진통제), dental pain, Fig 8-2 [R&T pp.234–235]; **Ibuprofen** 6 mg/kg 경구(NSAID; 해열·진통), febrile children, Fig 8-9 [R&T pp.241–242] | 분포 지연, turnover, 활성 대사체 |
| **Hysteresis 없음 (직접 link)** | 작용부위 평형·반응 생성이 sampling보다 훨씬 빠름 | **Midazolam** 15 mg/kg 경구(rat EEG; 진정제), Fig 8-6 [R&T p.239] | direct PK–PD link |
| **시계 방향 (clockwise)** | 내성, 피드백, 활성 대사체, 추가 동역학 | (이 세션 본문에는 사례 없음 — tolerance 장에서) | 내성, feedback |

### B. 첫 30초 진단의 두 줄 규칙

> 🔑 **30초 진단 규칙**
> ① **반시계 방향이면** → 분포 지연 / turnover / 활성 대사체부터 의심
> ② **시계 방향이면** → 내성 / 피드백부터 의심
> ③ **Loop가 안 보이면** → 그렇다고 direct가 확정은 아님. **sampling 해상도 안에서만 그렇다**는 뜻임

세 번째가 중요함. Hysteresis가 안 보인다고 모든 약이 direct response인 게 아님. **sampling 간격보다 지연이 짧으면 안 보일 뿐임.** 그래서 "직접 vs 지연" 판정은 model family를 고르기 전에 **설계 해상도(design-resolution) 결정**으로 먼저 다뤄야 함. 지연이 sampling 척도에서 안 보이면 생물학적으로 완전히 순간적이지 않더라도 direct link로 방어 가능함.

> 📖 **G&W 5e p.235, Fig 3.33 / R&T 5e p.235, Fig 8-2**: 직접 반응과 지연 hysteretic 반응이 어떻게 다르게 그려지는지를 한눈에 보여줌. Fig 8-2는 같은 naproxen 농도에서 상승기/하강기에 따라 통증 완화가 다르게 나타나는 것을 직접 그려놓은 거임. → 그래서 **농도 하나로 반응을 다 설명할 수 없다는 사실의 시각적 증명**임.

---

# PART II — Turnover의 골격: mismatch 출처 #2를 분해하기

반시계 방향 hysteresis가 보였다고 가정함. 이제 그 지연이 turnover에서 오는지를 확인하는 도구를 만들어야 함. 4개 후보 중 가장 흔한 케이스가 이거임.

## 2. 욕조에서 출발하기 — $R_0 = k_{in}/k_{out}$

### A. 가장 중요한 한 줄

Turnover 모델은 response가 두 속도의 균형 위에 떠 있다는 한 줄로 요약됨 [G&W pp.235–237; R&T pp.234–235, 239].

$$
\underbrace{\frac{dR}{dt}}_{\text{변화율}}
=
\underbrace{k_{in}}_{\text{생산속도}}
-
\overbrace{\underbrace{k_{out}}_{\text{소실 clock}}\,\underbrace{R}_{\text{반응 pool}}}^{\text{pool 소실}}
\quad \text{[G\&W Eq 3:74; G\&W p.237]}
$$

정상상태에서:

$$
\underbrace{R_0}_{\text{기저값}}
=
\frac{\underbrace{k_{in}}_{\text{생산}}}{\underbrace{k_{out}}_{\text{소실 clock}}}
\quad \text{[G\&W Eq 3:76; G\&W p.237]}
$$

> 💡 **이 식 하나가 unlocking 시킨다**
> Baseline $R_0$는 **독립 상수가 아님**. 수도꼭지($k_{in}$)와 배수구($k_{out}$)가 만든 균형점일 뿐임. 욕조에 비유하면, 수도꼭지가 일정 속도로 물을 넣고 배수구가 수위에 비례해서 물을 빼면, 어느 수위에서 두 속도가 똑같아지는 지점이 생김 — 그 수위가 $R_0$임.

| 파라미터 | 단위 | 생물학적 의미 |
|---|---:|---|
| $R$ | response unit | 측정된 약리학적 반응 |
| $k_{in}$ | response·time⁻¹ | 0차 생산 속도 |
| $k_{out}$ | time⁻¹ | 1차 소실 속도 = 회복 clock |
| $R_0$ | response unit | 기저 반응 = $k_{in}/k_{out}$ |

### B. 학생이 거의 100% 처음에 빠지는 함정 — Reparameterization

NONMEM에서 $k_{in}$과 $k_{out}$을 **따로 추정**하려고 하면, 거의 항상 다음 두 가지 중 하나가 일어남:
1. correlation이 0.98을 넘어서 covariance matrix가 망가짐
2. OFV가 30 iteration 동안 stuck이다가 갑자기 뚝 떨어짐 (stuck-then-drop 패턴)

이게 왜 일어나냐면, $k_{in}$과 $k_{out}$의 곱은 $R_0$로 데이터가 강하게 잡아주는데 **두 값을 따로 분리할 정보가 데이터에 없기 때문임**. 어두운 방에서 수도꼭지와 배수구를 동시에 만지면서 수위를 맞추는 일이랑 똑같음.

**해결책은 단순함.** $R_0$와 $k_{out}$을 추정하고, $k_{in}$은 곱으로 계산함:

$$
\underbrace{k_{in}}_{\text{생산}}
=
\underbrace{R_0}_{\text{기저값}}\cdot\underbrace{k_{out}}_{\text{소실 clock}}
$$

$$
\underbrace{\frac{dR}{dt}}_{\text{변화율}}
=
\underbrace{k_{out}}_{\text{회복 clock}}
\left(\underbrace{R_0-R}_{\text{기저-현재 거리}}\right)
\quad \text{[G\&W Eq 3:103; G\&W p.247]}
$$

PD4 사례를 봄. Pool 1에서 $k_1$과 $k_{out}$을 따로 추정했더니 $r=0.9999$, CV% 4000%. 같은 데이터에 $k_1 = k_{out}$ 제약을 걸어 만든 Pool 2의 "정상 CV%"는 **데이터가 동등성을 지지한 게 아니라 제약이 비식별성을 해결한 것**임 [G&W pp.742–752].

> 🔑 **NONMEM 출력 진단**: 30 iteration stuck-then-drop 패턴이 보이면, 곧장 `$THETA`를 $(R_0, k_{out})$로 재코딩함. 별다른 진단 없이도 90% 이상 살려낼 수 있는 표준 처방임.

### C. Baseline이 움직일 수도 있음 (보너스)

$k_{out}$이 시간 불변이라는 게 기본 가정인데, 실제로는 system 상태에 따라 움직일 수 있음. **IgG**(면역글로불린; FcRn 의존 항체 보호기전) 사례에서 혈청 IgG 30 mg·mL⁻¹일 때 반감기가 약 11일로 단축됨 — moderator/feedback 모델로 들어가는 입구임 [G&W pp.110–111].

정식 식 구조는 다음과 같음:

$$
\underbrace{\frac{dR}{dt}}_{\text{response 변화}}
=
\overbrace{\underbrace{k_{in}}_{\text{생산}}\,\underbrace{H(C)}_{\text{약물 함수}}}^{\text{drug-modulated input}}
-
\underbrace{k_{out}\,M}_{\text{moderator-driven loss}}
\quad \text{[G\&W Eq 2:261; p.110]}
$$

$$
\underbrace{\frac{dM}{dt}}_{\text{moderator 변화}}
=
\overbrace{\underbrace{k_{tol}\,R}_{\text{R에 의한 생성}}
-\underbrace{k_{tol}\,M}_{\text{1차 소실}}}^{\text{tolerance pool turnover}}
\quad \text{[G\&W Eq 2:262; p.111]}
$$

$$
\underbrace{\text{slope}_{A,B,C}}_{\text{관찰 반감기 기울기}}
=
\underbrace{k_{out}}_{\text{소실 clock}}\!\left(1+\underbrace{\frac{R_{A,B,C}}{M_{50}}}_{\text{포화 분율}}\right)
\quad \text{[G\&W Eq 2:263; p.111]}
$$

⚠️ **이 derivation에서 학생이 거의 다 놓치는 한 줄** — G&W 5e p.111 본문이 명시함: *"The three slopes are functions of $k_{out}$ and $M$, **since $R$ is equal to $M$ at dynamic steady state**…"* 즉 $R_0 = k_{in}/k_{out}$이 위 시스템에서 회수되려면 **$H(C)=1$(약물 없음) + $R=M$ at steady state** 두 조건이 필요함:

$$
\underbrace{\frac{dR}{dt}=0}_{\text{steady state}}
\;\Rightarrow\;
\underbrace{k_{in}}_{\text{생산}}
=
\underbrace{k_{out}\,M}_{\text{소실}}
\;\xrightarrow[R=M]{\text{steady state 가정}}\;
\overbrace{k_{in}=k_{out}\,R}^{\text{moderator-free 골격으로 환원}}
\;\Rightarrow\;
\underbrace{R_0=k_{in}/k_{out}}_{\text{Eq 3:76 재현}}
$$

이 R=M 가정을 놓치면 moderator 모델이 단순 turnover와 어떻게 연결되는지 derivation이 끊김.

---

## 3. 약물이 들어갈 자리는 딱 4개 — 4-Model Taxonomy

Baseline이 잡혔으니 이제 약물이 그 균형을 어디서 깨는지를 봄. **반응 방향(올라가냐 내려가냐)만 보고 모델 이름을 붙이면 안 됨.** 약물 함수가 **input에 붙는지 output에 붙는지**가 진짜 분류 기준임.

### A. 가역적 turnover에서 약물이 작용할 수 있는 자리는 4개뿐임

수도꼭지 잠그기, 수도꼭지 열기, 배수구 막기, 배수구 열기. 그리고 잠그는 함수 $I(C)$와 여는 함수 $S(C)$의 형태는 다음과 같음:

$$
\underbrace{I(C)}_{\text{남은 activity}}
=
1-
\underbrace{\frac{\overbrace{I_{max}\,C^n}^{\text{억제구동}}}{\underbrace{IC_{50}^n}_{\text{절반농도}}+\underbrace{C^n}_{\text{농도항}}}}_{\text{억제분율}},
\quad 0\le I_{max}\le 1
\quad \text{[G\&W Eq 3:77; p.237]}
$$

$$
\underbrace{S(C)}_{\text{촉진배율}}
=
1+
\underbrace{\frac{\overbrace{E_{max}\,C^n}^{\text{촉진구동}}}{\underbrace{EC_{50}^n}_{\text{절반농도}}+\underbrace{C^n}_{\text{농도항}}}}_{\text{촉진분율}}
\quad \text{[G\&W Eq 3:78; p.237]}
$$

### B. 4개 모델 — 한 표로 외움

| Model | ODE | 작용 자리 | $t_{ss}$ 거동 | $R_{ss}$ | 최대 $\Delta R$ | 임상 prototype |
|---|---|---|---|---|---|---|
| **I** 생산 억제 | $\dot R = k_{in}I(C) - k_{out}R$ | 수도꼭지 잠금 | $k_{out}$ 지배, 용량 독립 | $R_0\,I(C_{ss})$ | $R_0\,I_{max}$ | **Warfarin** (vitamin K cycle 억제) [G&W PD4 pp.742–752] |
| **II** 소실 억제 | $\dot R = k_{in} - k_{out}R\,I(C)$ | 배수구 막음 | effective $k_{out}\!\cdot\!I(C)$, **용량 의존** | $R_0/I(C_{ss})$ | $R_0\,I_{max}/(1\!-\!I_{max})$ | **Furosemide**-type retention [G&W p.238] |
| **III** 생산 촉진 | $\dot R = k_{in}S(C) - k_{out}R$ | 수도꼭지 더 엶 | $k_{out}$ 지배, 용량 독립 | $R_0\,S(C_{ss})$ | $R_0\,E_{max}$ | **Erythropoietin** [G&W p.238] |
| **IV** 소실 촉진 | $\dot R = k_{in} - k_{out}R\,S(C)$ | 배수구 더 엶 | effective $k_{out}\!\cdot\!S(C)$, **용량 의존** | $R_0/S(C_{ss})$ | $R_0\,E_{max}/(1\!+\!E_{max})$ | CB1 inverse agonist [G&W p.238]; PD7 compound C [G&W pp.764–769] |

ODE를 같은 자리에 모아두면 패턴이 보임:

$$
\begin{aligned}
\text{Model I: }&\frac{dR}{dt}=\overbrace{k_{in}I(C)}^{\text{input 억제}}-\underbrace{k_{out}R}_{\text{loss}}\\
\text{Model II: }&\frac{dR}{dt}=\underbrace{k_{in}}_{\text{input 유지}}-\overbrace{k_{out}RI(C)}^{\text{loss 억제}}\\
\text{Model III: }&\frac{dR}{dt}=\overbrace{k_{in}S(C)}^{\text{input 촉진}}-\underbrace{k_{out}R}_{\text{loss}}\\
\text{Model IV: }&\frac{dR}{dt}=\underbrace{k_{in}}_{\text{input 유지}}-\overbrace{k_{out}RS(C)}^{\text{loss 촉진}}
\end{aligned}
$$

### C. 학생이 가장 자주 헷갈리는 한 가지

> ⚠️ **반응 방향만으로 모델을 결정하지 말 것**
> "반응이 떨어지니까 Model I (생산 억제)지" — 틀림. Model IV (loss 촉진)도 baseline 아래로 갈 수 있음. 반응이 떨어진다고 input 차단이 확정되는 게 아님. **시간 경과 패턴 + $t_{ss}$의 용량 의존성**을 같이 봐야 함.

### D. Model II의 숨겨진 폭탄 — $I_{max} \to 1$ 발산

Model II의 최대 변화량은 분모에 $(1-I_{max})$가 있음. $I_{max}$가 1에 가까워지면 **무한대로 발산함**:

$$
\underbrace{\Delta R_{M2,\text{max}}}_{\text{M2 최대 변화}}
=
\frac{\underbrace{R_0}_{\text{기저값}}\,\overbrace{I_{max}}^{\to\,1}}{\underbrace{1-I_{max}}_{\to\,0}}
\;\xrightarrow[I_{max}\to 1]{}\;
\overbrace{\infty}^{\text{발산}}
\quad \text{[G\&W p.241]}
$$

수학적 호기심이 아니라 임상적으로 **소실 경로가 완전히 차단되면 $k_{in}$이 계속 들어오는데 빠질 길이 없어서 pool이 무한히 쌓이는 거임**. 욕조에서 배수구를 완전히 막으면 결국 흘러넘침. → 그래서 PPI에 의한 위 $H^+$ 축적, loop diuretic 차단 시 체액 정체, COX 억제 시 prostanoid 일부 측면의 축적 등 **고용량 saturation/toxicity의 구조적 이유**가 여기 있음.

**Model IV는 반대로 $E_{max} \to \infty$여도 $R_0$에서 멈춤** — $\Delta R_{M4,\text{max}} = R_0\,E_{max}/(1+E_{max})$의 분모가 같이 자라기 때문임. 두 모델의 경계 거동이 비대칭이라는 것이 핵심 차이임.

> 🔑 **실무 신호**: 모델 적합 중 $I_{max}$가 1에 매우 가깝게 수렴하면 ⓐ misspecification 신호이거나 ⓑ saturation 임계 진입 신호임. 어느 쪽이든 cross-check 필수.

---

## 4. 시간 신호로 4개 칸 가려내기 — $t_{ss}$와 peak shift

### A. 한 줄 규칙

| 관찰 | 1차 가설 | 주의 |
|---|---|---|
| 용량 간 **유사한** $t_{ss}$ | 생산 측 (Model I or III) | PK rate-limiting일 수도 |
| 용량에 따라 $t_{ss}$ **단축/연장** | 소실 측 (Model II or IV) | PK가 PD clock보다 빠를 때만 |
| 용량 증가에도 peak shift 없음 | **Effect compartment 증명 아님** | PD9가 이 과대해석을 직접 경고 [G&W pp.778–783] |

### B. 학생이 가장 자주 잘못 하는 것 — Early slope에서 $k_{out}$ 외삽

PD7 Fig 7.1을 보면 명확함. 6,400 unit에서 추정된 $k_{out} \approx 0.6\;h^{-1}$, 160,000 unit에서는 $k_{out} \approx 1.6\;h^{-1}$. 같은 약, 다른 용량인데 system 파라미터가 단조 변함. **이건 system biology가 아니라 misspecification artifact임** [G&W p.251].

이유는 단순함. Models I/III에서는 1차 소실 항이 $k_{out}\cdot R$로 유지되니까 시간 상수가 $1/k_{out}$임. 그런데 Models II/IV에서는 약물이 loss 항을 건드리니까 effective time constant가 농도에 따라 달라짐. **이 모델을 Model I/III처럼 다루면서 초기 기울기를 그대로 $k_{out}$으로 읽으면 용량별로 다른 답이 나옴.** 

> 🔑 **Mirror-slope 시그너처**: system 파라미터가 용량에 따라 단조 변하면 biology가 아니라 misspecification임.

### C. $t_{ss}$를 결정적 증거로 과대해석하지 말기

$t_{ss}$는 **공항 보안검색의 금속탐지기**임 — 경고음이 울리면 어디를 더 봐야 할지 알려주지만, 그것만으로 물건 정체가 결정되지 않음. 다음 추가 근거 중 최소 하나가 있어야 함:

| 보조 도구 | 무엇을 확인 |
|---|---|
| 넓은 dose range | 비선형 $H(C)$ 거동이 좁은 범위에서는 숨음 |
| 반복 투여/washout | system recovery clock을 직접 봄 |
| Mechanism prior | production vs loss는 $t_{ss}$만으로는 결판 안 남 |
| PK clock 확인 | PK가 더 느리면 PD clock 진단이 가려짐 |

---

## 5. Cascade가 들어오면 — Pool/Precursor 확장 (Sharma-Jusko 1998)

지금까지가 **단일 stage** turnover였음. 그런데 실제 생물학에서는 약물이 건드리는 자리와 우리가 측정하는 반응 사이에 **상류 pool이 하나 더** 있는 경우가 많음. Corticosteroid가 mRNA를 만들고 그게 enzyme을 만드는 식임.

### A. 2단계 cascade의 구조

$$
\underbrace{\frac{dP}{dt}}_{\text{precursor 변화}}
=
\underbrace{k_{in}}_{\text{0차 생산}}
-
\overbrace{\underbrace{k_p}_{\text{전환 clock}}\,\underbrace{P}_{\text{precursor pool}}}^{\text{precursor 소실 = R로 전환}}
\quad \text{[Sharma \& Jusko 1998 Eq 1]}
$$

$$
\underbrace{\frac{dR}{dt}}_{\text{response 변화}}
=
\overbrace{\underbrace{k_p}_{\text{전환 clock}}\,\underbrace{P}_{\text{precursor}}}^{\text{R로 들어오는 양}}
-
\underbrace{k_{out}\,R}_{\text{response 소실}}
\quad \text{[Sharma \& Jusko 1998 Eq 2]}
$$

기저상태에서:

$$
\underbrace{P_0}_{\text{precursor 기저}}=\frac{k_{in}}{k_p},
\qquad
\underbrace{R_0}_{\text{반응 기저}}=\frac{k_{in}}{k_{out}}
$$

**핵심**: response의 기저값은 single-stage와 같지만, **거기에 도달하는 동역학은 두 시계 $k_p$와 $k_{out}$의 cascade임**.

### B. 약물 작용 자리 확장 — 관행적 Models V–VIII

| Model (관행) | 약물 작용 자리 | ODE 변화 | 사례 |
|---|---|---|---|
| **V** | precursor 생산 억제 | $dP/dt = k_{in}\cdot I(C) - k_p P$ | corticosteroid → TAT mRNA |
| **VI** | precursor 생산 촉진 | $dP/dt = k_{in}\cdot S(C) - k_p P$ | EPO precursor 자극 |
| **VII** | precursor → response 전환 억제 | $dR/dt = k_p P\cdot I(C) - k_{out} R$ | 효소 활성화 차단 |
| **VIII** | precursor → response 전환 촉진 | $dR/dt = k_p P\cdot S(C) - k_{out} R$ | maturation 가속 |

> 📖 **명명법 출처 정정**: Sharma & Jusko (1998, *Br J Clin Pharmacol* 45:229–239) **원 논문은 'Model V/VI/VII/VIII' 번호를 명시적으로 부여하지 않음**. "indirect response models with precursor compartments"로 서술됨. **V–VIII 번호는 후속 표준 문헌(Jusko 그룹 후속 review, Mager-Wyska-Jusko 교과서 등)의 관행임**. 학습자가 원 논문을 펴서 'Model V'를 찾으면 그 표기가 없으니 헷갈리지 않게 해둠.

### C. Single-stage와의 본질적 차이

| 비교 기준 | Single-stage Model I (생산 억제) | Pool/Precursor Model V (상류 생산 억제) |
|---|---|---|
| 약물 작용 후 첫 효과까지 | $\sim 1/k_{out}$ | $\sim 1/k_p + 1/k_{out}$ (cascade lag) |
| Onset 곡선 모양 | exponential approach | **sigmoid 모양** (초기 평탄 구간) |
| 약물 중단 후 회복 | $1/k_{out}$ 단일 clock | 두 clock의 deconvolution 필요 |
| $k_{out}$ 단독 추정 | 종말 회복 기울기로 가능 | $k_p$와 함께 안 하면 cascade depth 흡수 |

> 🔑 **Sigmoid onset 시그너처**: Pool/precursor 약물은 **투약 직후 즉시 효과가 안 나오고 lag-then-rise** 패턴을 보임. 이게 보이는데 single-stage Model I로 적합하면 추정된 $k_{out}$이 **biology가 아니라 cascade depth($1/k_p$)의 일부를 흡수함**. → 임상에서 "측정된 $k_{out}$이 알려진 enzyme half-life보다 작게 나온다"가 cascade misspecification의 시그너처임.

> 💼 **실무 인사이트**: Corticosteroid 약리(prednisolone → tyrosine aminotransferase, methylprednisolone → lymphocyte trafficking 등)의 **표준 PD 골격이 바로 Pool/Precursor**임. Single-stage Model I로 적합하면 effect onset이 너무 빠르게 나옴.

---

## 6. $I_{max}/E_{max}$는 같은 이름이지만 같은 뜻이 아님

### A. 효과 크기 파라미터의 의미는 모델 구조마다 다름

$E_{max} = 0.65$라는 숫자를 봤다고 가정함. 이게 무슨 뜻인지 모델 구조 없이는 답이 안 나옴. **세 가지 가능성이 있음** [G&W p.246]:

| 모델 형태 | 식 | $E_{max}$의 의미 |
|---|---|---|
| Direct additive | $E=E_0+\frac{E_{max}C^n}{EC_{50}^n+C^n}$ | response 단위의 **절대 거리** |
| Direct multiplier | $E=E_0(1+\frac{E_{max}C^n}{EC_{50}^n+C^n})$ | **무차원 배율** |
| Turnover Model III | $R_{ss}=R_0(1+\frac{E_{max}C^n}{EC_{50}^n+C^n})$ | **system turnover를 통한 배율** |

같은 "높이 10"이라도 **센티미터인지 층수인지** 모르면 비교가 불가능함. $E_{max}$도 어떤 축 위의 거리인지 먼저 봐야 함.

$$
\underbrace{E}_{\text{관찰효과}}
=
\underbrace{E_0}_{\text{기저효과}}
+
\underbrace{\frac{\overbrace{E_{max}C^n}^{\text{효과구동}}}{EC_{50}^n+C^n}}_{\text{절대효과}}
\qquad
\underbrace{E}_{\text{관찰효과}}
=
\underbrace{E_0}_{\text{기저효과}}
\left(1+
\underbrace{\frac{\overbrace{E_{max}C^n}^{\text{효과구동}}}{EC_{50}^n+C^n}}_{\text{배율효과}}
\right)
$$

$$
\underbrace{R_{ss}}_{\text{약물 정상상태}}
=
\underbrace{R_0}_{\text{system 기저값}}
\left(1+
\underbrace{\frac{\overbrace{E_{max}C^n}^{\text{input 배율}}}{EC_{50}^n+C^n}}_{\text{turnover 효과}}
\right)
$$

> 🔑 **비교 규칙**: 모델 / 연구 / 화합물 간 효과 파라미터를 비교할 때는 항상 $\Delta R/R_0$로 변환한 뒤 비교함. raw $E_{max}$ 숫자 비교는 거의 항상 무의미함.

### B. 선형 PK가 선형 PD를 의미하지 않음 — Methylprednisolone

**Methylprednisolone**(부신피질호르몬; i.v. phosphate-prodrug)에서 16 / 31 / 63 / 125 / 250 / 500 / 1000 mg를 줌. 혈장 AUC는 용량에 거의 비례적으로 증가하는데 **lymphocyte 반응은 비례하지 않음** — 고용량에서 PD plateau에 가까워지기 때문임 [R&T pp.256–258].

R&T 본문(p.256)이 단호하게 못박아둠 — *"Dose linearity in pharmacokinetics does not result in dose linearity in pharmacodynamics. That is almost never the case."*

또 다른 disconnect 사례. **Rosuvastatin**(HMG-CoA 환원효소 억제제) OATP1B1 polymorphism은 plasma AUC를 substantially 변화시키지만 cholesterol synthesis 반응은 modestly 변함(Fig 8-28/8-29) — **전신 노출 ≠ 작용 부위 노출**의 보조 사례임 [R&T pp.258–259]. Bioequivalence가 효과 동등성을 보장하지 않는 메커니즘으로 자주 인용됨.

> ⚠️ "용량 비례적 노출 → 용량 비례적 반응"이라는 결론을 쓰기 전에 **Hill curve의 어느 영역에 있는지 먼저 확인**함.

> 📖 **G&W 5e p.246, Fig 3.40**: 같은 파라미터 이름이 모델 계열마다 같은 수직 반응 거리를 의미하지 않는다는 것을 보여주는 그림임.

---

# PART III — Estimation Discipline: NONMEM 돌리기 전 손으로 잠가야 할 것들

## 7. Graphical Initial Estimation + Blocking Dose — 사실은 기전적 감사임

### A. 왜 손으로 잡아야 하는가

학생들이 흔히 graphical estimation을 "NONMEM 시대 이전의 향수"라고 무시함. 틀림. **이건 첫 번째 mechanism audit임**. 초기값을 단순 guess로 두면 optimizer가 비식별성 골짜기에서 가짜 수렴을 내놔도 알아채기 어려움 [G&W pp.247–251].

### B. 5단계 작업 흐름

| 단계 | 어디서 읽는가 | 산출물 |
|---|---|---|
| 1 | pre-dose baseline | $R_0$ |
| 2 | 종말 회복 곡선의 log-linear 기울기 (또는 blocked-synthesis 구간) | $k_{out}$ |
| 3 | 1번 × 2번 | $k_{in} = R_0 \cdot k_{out}$ |
| 4 | 2–3개 용량 수준의 정상상태 또는 peak 반응 | $IC_{50}/EC_{50}$, $I_{max}/E_{max}$의 자릿수 |
| 5 | 위 모든 값이 sanity 통과한 후 | NONMEM 추정 시작 |

**PD5 사례**를 봄. Compound A의 PK가 먼저 잡힌 상태($V=40\;\text{L}$, $K=0.9\;h^{-1}$)에서 4000/16000/80000 unit의 6시간 infusion 데이터를 받음. Pre-infusion baseline에서 $R_0$를 읽고, post-infusion 회복 곡선의 semi-log plot 종말 기울기로 $k_{out} \approx 0.43\;h^{-1}$을 얻고, $k_{in} = R_0 \cdot k_{out}$로 production rate 출발점을 잡음. 세 용량의 plateau에서 $IC_{50} \approx 95$, $I_{max} \approx 0.65$의 자릿수까지 잡은 뒤에 NONMEM 들어감(Table 5.1).

> ⚠️ 적합값이 graphical 자릿수에서 한 order 이상 벗어나면 **비식별성이나 misspecification이 작동 중**이라는 신호임. Random effects 확장하기 전에 출발점의 생물학을 먼저 수정함.

### C. Blocking Dose — Warfarin의 임상 등가 방법

**Warfarin** blocking-dose 분석은 $k_{out}$을 직접 뽑아내는 임상적 등가 방법임. 합성이 거의 완전히 차단되면 prothrombin complex activity가 다음을 따름:

$$
\underbrace{\frac{dA}{dt}}_{\text{활성 변화}}
=-\underbrace{k_t}_{\text{소실 clock}}\,\underbrace{A}_{\text{잔여 활성}}
\quad \text{[R\&T Eq 8-6; R\&T pp.244–246]}
$$

비차단 구간에서는 합성 속도를 재구성함:

$$
\underbrace{R_{syn}}_{\text{합성속도}}
=
\underbrace{\frac{A_2-A_1}{\Delta t}}_{\text{관찰변화}}
+
\overbrace{\underbrace{k_t}_{\text{소실 clock}}\frac{\underbrace{A_1+A_2}_{\text{평균 활성}}}{2}}^{\text{소실보정}}
\quad \text{[R\&T Eq 8-7; R\&T p.247]}
$$

이게 hysteretic 반응-시간 기록을 **억제-농도 관계로 변환**하는 방법임 [R&T pp.244–247]. **공장 입구를 거의 완전히 막아놓고 창고가 비는 속도를 재는 실험**과 같음 — 들어오는 물량을 잠그면 배출 시계가 드러남. → 그래서 warfarin이 **합성 억제(Model I) 기전의 임상 prototype**으로 자주 인용되는 거임.

### D. DRT (Dose-Response-Time) — 농도 데이터가 없을 때

DRT는 농도 데이터가 없어도 baseline, slope, potency, maximal effect를 추론하는 방법임. 다만 full PK/PD 모델링보다 거친 역문제임. **노출 데이터가 있으면 DRT로 대체하지 말 것** — 후퇴 대안 또는 교육적 가교로만 둠 [G&W pp.272–275].

---

# PART IV — Turnover로는 안 되는 경우들

## 8. drug=0인데 effect≠0인 경우 — 비가역 작용과 표적 소비

### A. "drug=0이면 effect=0인가?"라는 질문 하나

가역적 turnover에서는 system이 반응을 계속 생산·제거하니까 baseline으로 돌아옴. 그런데 **약물 노출 기간 동안 반응 단위·표적·세포가 영구적으로 제거된 경우**는 다름. 약물이 사라져도 효과가 남음 [G&W pp.256–260; R&T pp.251–252].

핵심 식:

$$
\underbrace{\frac{dR}{dt}}_{\text{생존 변화}}
=
-\overbrace{\underbrace{K_{kill}}_{\text{kill potency}}\,\underbrace{C}_{\text{노출}}\,\underbrace{R}_{\text{잔여 pool}}}^{\text{비가역 kill}}
\quad \text{[G\&W Eq 3:110; p.257]}
$$

적분 형태:

$$
\underbrace{SF}_{\text{생존분율}}
=
\exp\left(-\overbrace{\underbrace{K_{kill}}_{\text{kill potency}}\cdot\underbrace{AUC}_{\text{누적노출}}}^{\text{누적 kill}}
\right)
\quad \text{[G\&W Eq 3:112; p.257]}
$$

> ⚠️ $K_{kill}$은 **2차 약리작용 상수임. 1차 PK 소실 상수가 아님.** 이 자료에서 $K_{kill}/k_k$는 PD killing이고 $K_{elim}$은 PK elimination임.

비가역 kill은 **스위치를 끄는 게 아니라 전구를 빼내는 것**과 같음 — 전기가 다시 들어와도 새 전구를 끼우기 전까지 빛은 안 돌아옴.

### B. 임상 prototype 3개 — 외워야 함

| 약물 | PK | PD | duration 결정자 |
|---|---|---|---|
| **Aspirin** 650 mg 경구 (NSAID; 항혈소판; COX-1 비가역 acetylation) | 짧은 혈장 반감기 | thromboxane B₂ 억제 **수일 지속** | 혈소판 표적 대체 시계 [R&T p.251] |
| **Omeprazole** 40 mg 경구 (PPI; H⁺/K⁺-ATPase 비가역 결합) | 혈장 반감기 <1 h | 산분비 억제 **수일 지속** | proton pump regeneration 시계 [R&T p.252] |
| **Paclitaxel** i.v. (taxane; 미세소관 안정화 항암제) | 혈장 농도 빠르게 감소 | 백혈구 회복 **약 3주** | leukocyte regrowth (Fig 8-22) [R&T pp.253–254] |

> 🔑 **Duration 질문 규칙**: **"drug=0이면 effect=0인가?"**의 답이 NO이면 plasma PK 외에 **target replacement clock을 별도 모델링**함.

### C. 모든 도구가 한 자리에 모이는 응용 — Friberg-Karlsson 항암제 호중구 감소 모델

**Paclitaxel** 백혈구 회복(약 3주)을 한 줄로 짚었는데, 실제 임상에서 항암제 myelosuppression의 **현대 표준 골격**은 한 단계 더 정교함. Friberg와 Karlsson(2002)이 제안한 모델은 **이 세션의 거의 모든 도구를 한 자리에 결합함** — 비가역 cell kill + transit chain maturation + feedback rebound + 약물 농도 함수.

**구조**: 5개 compartment cascade — 증식 pool $Prol$ → transit 1 → transit 2 → transit 3 → 순환 pool $Circ$. 약물은 $Prol$에서 cell을 죽이고, $Circ$의 감소가 다시 $Prol$의 증식을 자극(feedback)함 [Friberg et al., *J Clin Oncol* 2002].

$$
\underbrace{\frac{dProl}{dt}}_{\text{증식 변화}}
=
\overbrace{\underbrace{k_{prol}\,Prol}_{\text{1차 증식}}\,\underbrace{\bigl[1-E_{drug}(C_p)\bigr]}_{\text{약물 kill 보정}}\,
\underbrace{\left(\tfrac{Circ_0}{Circ}\right)^{\gamma}}_{\text{feedback 보정}}}^{\text{net 증식 — drug × feedback}}
-
\underbrace{k_{tr}\,Prol}_{\text{maturation 유출}}
$$

$$
\underbrace{\frac{dT_i}{dt}}_{\text{transit }i\text{ 변화}}
=
\underbrace{k_{tr}\,T_{i-1}}_{\text{이전 단계 유입}}
-
\underbrace{k_{tr}\,T_i}_{\text{다음 단계 유출}}
\quad (i=1,2,3;\;T_0\equiv Prol)
$$

$$
\underbrace{\frac{dCirc}{dt}}_{\text{순환 cell 변화}}
=
\underbrace{k_{tr}\,T_3}_{\text{성숙 cell 유입}}
-
\underbrace{k_{circ}\,Circ}_{\text{1차 소실}}
\quad \text{[Friberg \& Karlsson 2002 Eq 1–3]}
$$

> ⚠️ **모델 구조 제약 — 절대로 임의 고정 아님**
> 원 논문은 식별성 확보를 위해 다음 제약을 모델 정의의 일부로 도입함:
>
> $$
> \overbrace{\underbrace{k_{prol}}_{\text{증식}}=\underbrace{k_{tr,1}}_{\text{transit 1}}=\underbrace{k_{tr,2}}_{\text{transit 2}}=\underbrace{k_{tr,3}}_{\text{transit 3}}=\underbrace{k_{circ}}_{\text{순환 소실}}\equiv k_{tr}}^{\text{모델 정의에 의한 5중 제약}}
> \;\Longrightarrow\;
> \underbrace{MTT}_{\text{mean transit time}}=\underbrace{\frac{n+1}{k_{tr}}=\frac{4}{k_{tr}}}_{n=3\;\text{transit stages}}
> $$
>
> 이 제약이 약물 간 system parameter 일관성($MTT$, $\gamma$가 약물에 거의 무관)의 정량적 기반임. 학생이 이걸 "흔한 관행"으로 오해해서 NONMEM에서 $k_{prol}$, $k_{tr}$, $k_{circ}$를 독립 추정하려고 시도하면 **심각한 비식별성과 과대추정**에 빠짐. **원 논문 그대로 적용할 때만 약물 간 일관성이 회수됨.**

이 모델이 가르치는 것을 한 줄로 꿰면, **이번 세션 + Ch.12의 모든 도구가 한 곳에 모임**:

- **Card 2 (Turnover 골격)** → $Circ_0$가 baseline pool로 등장, feedback이 $k_{out}$ 고정 가정을 위반함
- **Card 3 (4-Model)** → 약물이 증식 항에 곱해지는 구조는 확장된 Model VII/VIII 패턴
- **Card 5 (Pool/Precursor)** → 증식 pool → transit → 순환은 3단계 cascade
- **Card 8 자체 (비가역 kill)** → 약물이 $Prol$에서 cell을 비가역적으로 죽임
- **Ch.12 (transit chain)** → 4-stage cascade가 $MTT = 4/k_{tr}$로 환산
- **Card 10 (PK vs PD clock)** → paclitaxel PK 반감기는 짧지만 $MTT \approx 7$일이 회복 지배

> 💼 **임상적 활용**: 단일 fit으로 호중구 감소의 **nadir 시점, nadir 깊이, 회복 시점**을 모두 예측하고, dose-intensity / dose-density 결정(예: dose-dense AC-T protocol)의 정량 근거가 됨. Docetaxel, paclitaxel, etoposide, 5-FU, vinflunine 등에서 **$\gamma$, $MTT$가 약물 간 일관성**을 보임 — system parameter는 약물에 거의 무관, drug parameter만 약물별로 차이.

> 🔑 **임상 시그너처**: Friberg-Karlsson 적합에서 보통 $MTT \approx 100$–$140$시간(약 4–6일), $\gamma \approx 0.1$–$0.3$이 호중구 표준 범위. 적합값이 이 범위를 크게 벗어나면 ⓐ 동반약물 효과, ⓑ 골수 기능 이상, ⓒ misspecification을 먼저 의심.

> ⚠️ **적용 범위**: Friberg-Karlsson은 **세포독성 항암제**의 myelosuppression 전용임. 표적치료제, 면역항암제는 작용 기전이 달라서 그대로 안 됨. **Lenalidomide의 호중구 감소** 같은 경우는 이 골격을 변형해서 써야 함.

---

# PART V — APEX: 같은 곡선, 두 가지 인과 해석

## 9. Turnover vs Effect Compartment — 데이터만으로 결판 안 나는 위기

이번 세션의 정점임. 학생들이 거의 다 빠지는 함정 하나가 여기 있음.

### A. 같은 곡선을 만드는 두 가지 구조

Turnover 모델:

$$
\underbrace{\frac{dR}{dt}}_{\text{변화율}}
=
\overbrace{\underbrace{k_{in}}_{\text{생산}}\underbrace{S(C)}_{\text{촉진함수}}}^{\text{생산 촉진}}
-
\overbrace{\underbrace{k_{out}}_{\text{소실 clock}}\underbrace{R}_{\text{response pool}}}^{\text{pool 소실}}
$$

Effect compartment:

$$
\underbrace{\frac{dC_e}{dt}}_{\text{effect-site 변화}}
=
\underbrace{k_{e0}}_{\text{평형 clock}}
\left(\underbrace{C-C_e}_{\text{농도차}}\right),
\quad
\underbrace{R}_{\text{반응}}=\underbrace{f(C_e)}_{\text{effect-site 함수}}
\quad \text{[R\&T pp.244–246]}
$$

두 모델은 **같은 그림자를 만드는 두 물체**임. 그림자 모양만 보고 물체를 결정하는 건 위험함. 조명 방향을 바꾸거나 다른 각도에서 봐야 정체가 드러남.

### B. PD6가 보여주는 비식별성의 정량 시그너처

| Metric | Turnover (linear S·$k_{in}$) | Effect compartment | Δ |
|---|---:|---:|---:|
| WRSS | 15,516 | 15,518 | 2 |
| AIC | 1,041 | 1,040 | −1 |
| 시간 상수 | $k_{out}=5.6\;h^{-1}$ | $k_{e0}=5.6\;h^{-1}$ | 0 |
| Half-doubling 농도 | $EC_{50}=1{,}633\;\text{ng}\cdot\text{L}^{-1}$ | $a=0.026 \to \sim 1{,}623\;\text{ng}\cdot\text{L}^{-1}$ | <1% |

> ⚠️ $\Delta WRSS = 2$, $\Delta AIC = -1$은 **사실상 동치**임. "둘 중 하나가 더 매끄럽다"가 아니라 **"데이터가 둘을 못 가른다"는 신호임**.

### C. 학생이 거의 100% 빠지는 함정

**$\Delta AIC = -1$만 보고 AIC가 낮은 모델을 "맞는 모델"이라고 결정함.** 숫자가 우열처럼 보이고 두 곡선이 다 매끄러우니까 그럴싸함. 그런데 이걸 그냥 두면 나비효과가 남:

1. AIC 미세차로 구조 결정
2. → $k_{e0}$ 또는 $k_{out}$에 지연 원인을 잘못 배정
3. → 새 dose range나 반복 투여 때 onset/offset 예측 실패
4. → 규제 단계에서 "대안 구조 평가와 sensitivity analysis가 빠졌다"는 deficiency가 돌아옴

### D. 그럼 어떻게 가르나

| 증거 | Turnover 지지 | Effect compartment 지지 |
|---|---|---|
| 반응 변수 | 내인성 매개물질, 바이오마커, 세포 수, 응고인자, 위산 pH | 약물 분포 지연이 원인 |
| Dose range | 비선형 turnover 거동을 드러낼 만큼 넓을 것 | 안정적 $EC_{50}$과 타당한 $k_{e0}$로 hysteresis 해소 |
| 교란 | 반복 투여 / washout으로 system 회복 시간 노출 | biophase 평형으로 onset/offset 설명 |
| Mechanism prior | 알려진 합성/소실 과정 | 알려진 조직 분포 지연 |

> 💼 **규제 제출에서의 실무 인사이트**
> 두 인과 구조가 똑같이 잘 맞을 때 **규율 있는 접근**은 "어느 모델이 맞다"고 결정하는 게 아니라 **생물학적 가정을 문서화하고, 두 구조를 가를 수 있는 설계 요소를 명시하는 것**임. 모델의 방어 가능성은 곡선의 매끄러움이 아니라 mechanism + design support에서 나옴.

> 📌 **비식별성 우회 전략 — 베테랑이 쓰는 트릭**
> 두 모델을 둘 다 적합시키고 **sensitivity analysis로 용량 결정이 모델 선택에 얼마나 민감한지 제시함**. 두 모델 모두에서 제안된 dose가 안전 한계 안에 있음을 보이면 **모델 선택 자체가 의사결정의 critical path에서 빠짐**. 이게 비식별성 앞에서 모델을 *선택*하지 않고 **비식별성이 의사결정에 영향을 주지 않는 결정 구조를 설계하는** 정통 접근임.

> 📖 **G&W 5e p.759, Fig 6.1; p.763, Table 6.1**: 반응-시간 적합은 본질적으로 동등해 보일 수 있지만 인과 해석은 서로 다르게 남는다는 것을 직접 보여줌. → fit만으로 인과 구조를 결정하면 안 된다는 사실의 정량 증거임.

---

# PART VI — 임상 의사결정으로 번역: 결국 어느 시계가 가장 느린가

## 10. PK clock vs PD clock — Duration 공식은 언제 살아있고 언제 폐기되나

### A. 약을 주면 두 개의 시계가 동시에 돌아감

투약 후 약물의 PK clock(소실 속도)과 반응 system의 PD clock(회복 속도)이 동시에 돌아감. **관찰되는 반응 감소는 둘 중 느린 쪽의 시계가 결정함** [R&T pp.243, 247–256]. 어느 쪽이 느린지를 먼저 정해두면, 임상에서 쓰는 duration 공식이 살아있는 경우와 폐기해야 하는 경우가 그 자리에서 갈림.

| 상황 | 느린 clock | 대표 약물 | 모델링 귀결 |
|---|---|---|---|
| **PK rate-limited** | 약물 소실/분포 | **Succinylcholine** 0.5/1/2/4 mg·kg⁻¹ i.v. (탈분극성 근이완제), **Minoxidil** 25 mg 경구 (K⁺ 채널 개방 혈관확장제, MAP 저하) | $t_D$ 공식이 살아있음 [R&T pp.249–256] |
| **PD rate-limited** | System turnover / 표적 재생 | **Acenocoumarol** vs 응고인자 turnover, **Aspirin** 혈소판, **Omeprazole** proton pump, **Paclitaxel** 백혈구 | Turnover / target-consumption 모델 필요. PK $k$만으로는 duration 예측 불가 [R&T pp.243, 251–254] |
| **약물 PK가 system보다 느림** | 간접 기전에서도 PK가 지배 | **Phenprocoumon** (장반감기 쿠마린계, ~5일) vs 응고인자 동역학 | 항응고 효과 회복이 약물 잔류를 따름 [R&T p.243] |

### B. Region 1/2/3과 선형 감소

계단식 E-logC 관계에서 **중간 구간(Region 2)**에 있을 때, 단일 용량 후 반응이 시간에 따라 **근사적으로 직선으로 감소함**:

$$
\underbrace{Response}_{\text{관찰반응}}
=
\underbrace{E(0)}_{\text{시작효과}}
-
\overbrace{\underbrace{m}_{\text{E-logC 기울기}}\,\underbrace{k}_{\text{PK clock}}\,\underbrace{t}_{\text{시간}}}^{\text{선형 감소}}
\quad \text{[R\&T Eq 8-9; pp.247–249]}
$$

**Succinylcholine의 약 22%/min 감소**가 이 중간 구간 선형성의 예시임. Region 1은 1차 동역학 비슷한 거동으로 돌아가고, Region 3은 plateau에 가까운 구간임. Region 2는 **비탈길 중간의 직선 구간**과 같음 — 위쪽 plateau나 아래쪽 완만한 구간에서는 같은 걸음 수가 같은 높이 변화로 안 바뀜.

### C. Duration 공식 — 언제 쓰는가

**PK-rate-limited 반응에서 노출-반응 관계가 사실상 고정**되어 있을 때만 다음 식을 씀:

$$
\underbrace{t_D}_{\text{duration}}
=
\underbrace{\frac{1}{k}}_{\text{PK clock 역수}}
\ln\left(\frac{\underbrace{Dose}_{\text{투여량}}}{\underbrace{C_{min}V}_{\text{최소 유효량}}}\right)
=
\underbrace{\frac{1}{k}}_{\text{PK clock 역수}}
\ln\left(\frac{\underbrace{Dose}_{\text{투여량}}}{\underbrace{A_{min}}_{\text{효과 최소량}}}\right)
\quad \text{[R\&T Eq 8-12; pp.254–255]}
$$

**용량을 두 배로 올리면 약물 반감기 하나만큼의 duration이 추가됨**:

$$
\underbrace{\Delta t_D}_{\text{duration 추가분}}
=
\frac{\underbrace{\ln 2}_{\text{2배 로그}}}{\underbrace{k}_{\text{PK clock}}}
=
\underbrace{t_{1/2}}_{\text{PK 반감기}}
$$

이게 succinylcholine duration이 **용량 두 배마다 유효 반감기 하나씩 더해지는** 이유임 [R&T pp.255–256]. PK-rate-limited duration에서 dose doubling은 **로그 자 위에서 한 칸 오른쪽 이동**이고, 그 한 칸이 시간축에서 반감기 하나로 번역됨.

### D. 학생이 거의 100% 빠지는 함정 — Eq 8-12를 모든 약에 적용

> ⚠️ **Eq 8-12를 warfarin, aspirin, omeprazole, paclitaxel에 갖다 붙이지 말 것**. 이 약들은 PD-rate-limited임. PK $k$로 계산한 $t_D$는 수학적으로는 매끈하지만 임상적으로는 무의미함. **Duration 계산 전에 먼저 "어느 시계가 더 느린가?"를 물어야 함**. 답이 PD라면 그 자리에서 PK $k$로 duration 계산하는 걸 멈춰야 함.

### E. 같은 기전 ≠ 같은 시계 — Acenocoumarol vs Phenprocoumon

이게 30년 경력 베테랑이 스폰서한테 제일 자주 짚어주는 함정임.

스폰서가 주장함 — "phenprocoumon과 acenocoumarol은 같은 항응고 기전을 공유하니까 반응 회복은 같은 PD turnover half-life로 결정돼야 한다." **거부함.**

- **Acenocoumarol** (PK 반감기 ~15 h) → PK가 짧으니 **PD clock**(응고인자 turnover)이 더 느림 → **PD-rate-limited**
- **Phenprocoumon** (PK 반감기 ~5일) → PK가 더 기니 **PK clock**이 지배 → **PK-rate-limited**

같은 prothrombin complex 동역학을 공유하지만 **서로 다른 rate-limiting clock**임(Fig 8-11) [R&T p.243]. 같은 작용기전 약물군에서도 약물별 PK가 rate-limiting step을 결정함.

스폰서의 단순화를 그냥 채택하면 어떻게 되나:
- 두 약물에 동일한 dose-titration step-up rule 적용
- → phenprocoumon 누적 위험 또는 acenocoumarol 미달 dose
- → 환자 안전 사고 또는 약효 부전 사고

**규제 제출에서 "같은 기전이니까 같은 PD half-life"라는 추론은 design support 없이는 데이터로 방어 불가능함**. "insufficient justification for proposed dosing interval" 형태의 deficiency가 돌아옴.

> 🔑 **정량 시그너처**: 예측 duration이 관측 duration과 50% 이상 어긋나거나, dose 증량 시 예측 증가가 관측치와 비례하지 않으면 **rate-limiting clock이 잘못 잡혔다는 신호임**.

> 📖 **R&T 5e p.243, Fig 8-11**: 같은 항응고 반응 system도 약물 PK에 따라 다른 시계에 의해 제한된다는 것을 보여줌.
> **R&T 5e p.255, Fig 8-23 / p.256, Fig 8-24**: PK가 속도 제한 단계인 조건에서 용량 두 배가 duration에 반감기 하나를 추가하는 패턴을 시각화함.

---

# PART VII — Integration: 한 바느질로 꿰기

## 11. 5분 만에 외우는 혼동 쌍 — 베테랑이 30초 안에 가르는 7가지

각 hook은 두 개념 차이의 **구조적 필연**을 비유로 묶어둠.

### Hook 1 — Direct effect vs Indirect response
*바로 켜지는 전등 vs 서서히 따뜻해지는 전기장판.* Direct는 농도 상승에 즉시 따라옴. Indirect는 약물이 production 또는 loss를 바꾸고 그 변화가 response pool에 쌓이면서 나타나는 지연 반응임. **반응이 $C_{max}$보다 늦게 peak에 도달하면 indirect를 먼저 의심.**

### Hook 2 — Model I (생산 억제) vs Model II (소실 억제)
*수원 틀기 vs 배수구 막기.* 단일 dose range에서는 두 모델이 사실상 같은 데이터를 만들 수 있음. **mechanism prior나 더 넓은 dose range가 필요함.**

$$
\begin{aligned}
\text{Model I: }&\frac{dR}{dt}=\overbrace{k_{in}I(C)}^{\text{production 억제}}-\underbrace{k_{out}R}_{\text{기존 loss}}\\
\text{Model II: }&\frac{dR}{dt}=\underbrace{k_{in}}_{\text{production 유지}}-\overbrace{k_{out}RI(C)}^{\text{loss 억제}}
\end{aligned}
$$

### Hook 3 — $k_{in}$ vs $k_{out}$
*수원 속도 vs 배수 속도.* 기저상태에서 $k_{in}=k_{out}\cdot baseline$이고, $k_{out}=1/MRT_{response}$가 반응 반감기를 결정함.

$$
\underbrace{k_{in}}_{\text{수원 속도}}=
\underbrace{k_{out}}_{\text{배수 clock}}\cdot\underbrace{baseline}_{\text{pool 크기}},
\quad
\underbrace{k_{out}}_{\text{반응 clock}}=
\frac{1}{\underbrace{MRT_{response}}_{\text{평균 체류시간}}},
\quad
\underbrace{t_{1/2,response}}_{\text{반응 반감기}}=
\frac{0.693}{\underbrace{k_{out}}_{\text{소실 clock}}}
$$

### Hook 4 — Baseline $R_0$ vs Steady-state $R_{ss}$
*출발점 vs 목적지.* $R_0$는 약물 투여 전 pool의 자연 균형, $R_{ss}$는 약물 효과 하의 새 균형. **이동 속도는 $k_{out}$이 결정하고, 거리는 $E_{max}/EC_{50}$이 결정함.**

### Hook 5 — Rebound vs Natural recovery
*과교정 vs 자연 복귀.* Rebound는 약물 중단 시 반응이 **baseline을 넘어서는 것**, natural recovery는 그냥 baseline으로 돌아오는 것. **구분 기준은 baseline을 넘어서는가임.**

### Hook 6 — Duration of effect vs AUC of effect
*효과의 길이 vs 효과의 면적.* Duration은 threshold 이상/이하 시간, AUC of effect는 반응-시간 곡선 아래 면적. **같은 duration이어도 반응 높이가 다르면 AUC가 다름.**

### Hook 7 — Non-identifiability vs Misspecification
*지도가 둘 다 정확 vs 지도가 틀림.* 비식별성은 데이터가 둘 중 무엇이 맞는지 결정하지 못하는 상태, misspecification은 데이터와 안 맞는 구조를 고른 상태. **$\Delta WRSS \approx 2$, $\Delta AIC \approx -1$은 비식별성 신호이지 misspecification 신호가 아님.**

### 그리고 보너스 — Reversible turnover vs Irreversible kill
*수도꼭지 잠그기 vs 전구 빼내기.* Reversible은 system이 계속 생산·소실해서 baseline 복귀. Irreversible은 표적/세포가 소비되고 대체/재성장이 필요.

$$
\begin{aligned}
\text{Reversible: }&\frac{dR}{dt}=\underbrace{k_{in}}_{\text{재생산}}-\underbrace{k_{out}R}_{\text{소실}}\\
\text{Irreversible: }&\frac{dR}{dt}=-\overbrace{\underbrace{K_{kill}}_{\text{kill potency}}\underbrace{C}_{\text{노출}}\underbrace{R}_{\text{잔여 target/cell}}}^{\text{target/cell 소비}}
\end{aligned}
$$

### 5가지 clock 위치 오류 — 외워둘 것

| 오류 | 잘못 짚은 clock | 대표 반례 |
|---|---|---|
| **E1. Mirror-slope 오독** | 모든 모델에서 early slope를 $-k_{out}$으로 외삽 | PD7: 6,400U → 0.6 h⁻¹, 160,000U → 1.6 h⁻¹ — misspecification artifact [G&W p.251] |
| **E2. Phantom convergence** | turnover와 effect compartment가 같은 fit → 한쪽 확정 | PD6 Table 6.1: $\Delta WRSS=2$, $k_{out}=k_{e0}=5.6\;h^{-1}$ [G&W pp.758–763] |
| **E3. Wrong-clock $t_D$** | 모든 약물에 Eq 8-12 적용 | warfarin/aspirin/omeprazole/paclitaxel은 PD-rate-limited [R&T pp.251–254] |
| **E4. Linear-PK = linear-PD** | dose-proportional AUC가 곧 dose-proportional response | methylprednisolone 16–1000 mg [R&T pp.256–258] |
| **E5. Same-mechanism = same-clock** | 동일 작용기전이면 같은 rate-limiting step | acenocoumarol(PD-limited) vs phenprocoumon(PK-limited) [R&T p.243] |

**이 다섯을 외운 학습자는 이번 세션의 모델링 결정을 거의 자동으로 방어할 수 있음.**

---

## 12. 자기 테스트 — 능동 회상

### Q1 [회상] Model I ODE와 정상상태

Model I ODE를 쓰고 일정한 $C_{ss}$에서 $R_{ss}$를 도출함.

**정답**
$$
\underbrace{\frac{dR}{dt}}_{\text{변화율}}
=
\overbrace{k_{in}I(C)}^{\text{production 억제}}
-
\underbrace{k_{out}R}_{\text{소실}}
\;\xrightarrow[\text{steady state}]{dR/dt=0}\;
\underbrace{R_{ss}}_{\text{약물 정상상태}}
=
\underbrace{R_0}_{\text{기저값}}
\underbrace{I(C_{ss})}_{\text{남은 production}}
$$

### Q2 [회상] $t_{ss}$ 용량 독립

용량 독립 $t_{ss}$를 가진 모델은? **Models I와 III** — 1차 소실 항이 $k_{out}\cdot R$로 유지되기 때문임. Models II와 IV는 약물이 소실 항을 바꾸니 용량 의존적 $t_{ss}$가 나올 수 있음. 단, **PK가 더 느린 clock이 아닐 때만** 성립함 [G&W pp.247–251; R&T p.243].

### Q3 [응용] Peak shift 부재 해석

용량을 증가시켜도 peak shift가 안 나타남. effect compartment 모델을 증명하나?

**정답**: 아님. PD9는 **peak shift 부재가 link/effect-compartment 모델을 반드시 의미하지 않는다**고 명시적으로 경고함. Dose range, 비선형 약물 함수, system 동역학을 같이 봐야 함 [G&W pp.778–783].

### Q4 [응용] Zooparc® 용량 정정

PD9 관찰된 반복 투여 figure에서 확인된 용량은? **2.5 mg과 5 mg.** 25 mg/day는 투사/대규모 연구 논의이며 관찰 용량 맥락이 아님 [G&W pp.778–783].

### Q5 [응용] Naproxen 정정

"naproxen 250 mg, Fig 8-3"의 오류 표현 수정: **Naproxen 500 mg 경구, dental pain, 1–8 h sampling, 반시계 방향 hysteresis, Fig 8-2.** Fig 8-3은 하류 약력학 도식임 [R&T pp.234–236].

### Q6 [응용] 잘못된 clock의 $t_D$

Aspirin duration에 Eq 8-12가 왜 부적절한가?

**정답**: Aspirin의 혈장 노출은 빠르게 사라지지만 **표적과 혈소판 기능 회복이 더 느림**. Duration은 PD/표적 대체가 결정하지 PK rate-limited가 아님 [R&T p.251].

### Q7 [응용] Turnover vs Effect compartment 결정

단일 용량 데이터가 turnover와 effect-compartment 둘 다에 똑같이 잘 적합함. 결정에 필요한 증거?

**정답**: 반응 변수의 mechanism prior, 더 넓은 dose range, 반복 투여/washout, PK clock 교란, 그리고 $EC_{50}/k_{e0}$의 생물학적 타당성. **적합도 단독으로는 부족함** [G&W pp.758–763; R&T pp.244–246].

### Q8 [응용] Linear PK ≠ Linear PD

Methylprednisolone AUC가 16–1000 mg에서 용량 비례적임. 이게 왜 용량 비례적 lymphocyte 반응을 정당화하지 못하는가?

**정답**: 반응이 노출-반응 곡선의 **plateau 구간에 진입**할 수 있음. R&T 본문(p.256) 인용 — *"Dose linearity in pharmacokinetics does not result in dose linearity in pharmacodynamics. That is almost never the case."* [R&T pp.256–258]

### Q9 [Boss Dilemma — 30년 경력 베테랑이 쓸 방어 논리]

스폰서 주장: "phenprocoumon과 acenocoumarol은 같은 항응고 기전이니까 같은 PD turnover half-life로 회복이 결정돼야 한다."

**거부.** 같은 기전이 같은 rate-limiting clock을 의미하지 않음.
- Acenocoumarol(~15 h): PK 짧음 → 회복이 PD-clock 제한 (응고인자 turnover가 더 느림)
- Phenprocoumon(~5일): PK 김 → 회복이 PK-clock 제한 (약물 잔류가 system clock보다 우세)

[R&T p.243]

**Trade-off 논리**:
- Sponsor 단순화 채택 → 두 약물에 동일 step-up rule → phenprocoumon 누적 위험 또는 acenocoumarol 미달 dose → 환자 안전·약효 부전 사고
- 규제 위험 — "같은 기전이니까 같은 PD half-life"는 design support 없이는 데이터로 방어 불가
- **올바른 방어**: 약물별 PK가 같은 PD system 위에서 어떤 시계를 작동시키는지를 Fig 8-11 데이터로 직접 증명. 약물별 별도 dose-duration model 사용. **단일 PD half-life claim은 phenprocoumon에서 임상적으로 무의미하고 acenocoumarol에서만 유효함.**

### Q10 [⚡ Apex Dilemma] Pool 1 vs Pool 2 모델 선택

두 모델이 $\Delta WRSS=2$, $k_{out}=k_{e0}$로 **사실상 비식별적**일 때 Phase 2 용량 결정에 무엇을 쓰나?

**거장의 Trade-off 논리**:
- 선택지 A (mechanism prior 사용) — 깔끔하지만 데이터 외 prior 사용 비판 받음
- 선택지 B (두 모델 모두 제출 + sensitivity) — 투명하지만 의사결정자 혼란 가능
- **정통 답**: "어느 모델을 선택했나"보다 **"왜 이 불확실성이 용량 결정의 안전성에 영향을 주지 않는가"**를 설명함. 두 모델 모두에서 제안된 Phase 2 용량이 안전 한계 안에 있음을 sensitivity analysis로 증명하면, **모델 선택 자체가 의사결정의 critical path에서 빠짐**.

한 줄 메시지: **비식별성 앞에서 모델을 선택하려고 하지 말고, 비식별성이 의사결정에 영향을 주지 않는 결정 구조를 설계함.**

---

## 13. 큰 그림 — 이 세션이 다른 세션들과 만나는 자리

### A. 약리계측학 아키텍처에서의 위치

이번 세션은 직접 노출-반응 모델링과 고급 질병/반응 시스템 사이임. 여기서부터 모델러는 **곡선 적합을 넘어 원인을 분리**해야 함.

| 후속 세션 | 이번 세션에서 열리는 개념 | 이번 세션 없으면 실패하는 것 |
|---|---|---|
| Transit compartment | 분포/전달 지연과 turnover 지연 분리 | 모든 지연을 effect compartment로 흡수 |
| Tolerance/moderator | feedback, rebound, post-trough 회복 timing | $k_{out}$ 고정 가정 위반을 놓침 |
| Disease progression / baseline drift | $R_0$가 시간에 따라 움직이는 경우 | 질병 진행을 약물 효과로 오독 |
| PopPK/PD IIV | drug parameter와 system parameter 분리 | $E_{max}$, $k_{out}$, $k_{e0}$ 해석 혼동 |
| Sampling design | 숨겨진 시계를 식별할 관측 창 설계 | 비식별성을 후속 시험에 반복 |

### B. 이 세션을 약하게 다뤘을 때의 실패 모드

| 실패 모드 | 실무적 결과 |
|---|---|
| 모든 지연을 effect compartment로 처리 | $k_{e0}$이 생물학을 흡수 → 새 투여 프로토콜에서 시뮬레이션 실패 |
| $t_{ss}$를 결정적 증거로 처리 | 기전적 주장이 설계 근거를 과대평가 |
| $E_{max}$ 단위 혼동 | 교차 연구 또는 in vitro/임상 potency 비교가 오해를 유발 |
| PD-rate-limited 약물에 $t_D$ 적용 | Duration 예측이 생물학적으로 무의미 |
| Baseline drift 무시 | 질병 진행이나 일주기 변동을 약물 효과로 오독 |

### C. 베테랑이 데이터를 받자마자 30초 안에 자동으로 돌리는 진단 순서

경력 있는 약리계측학 심사자는 **곡선이 매끄러운지를 가장 먼저 묻지 않음.** 데이터를 본 첫 30초 안에 다음 순서를 본능적으로 돌림:

| 단계 | 보는 것 | 첫 가설 분기 |
|---|---|---|
| 1 | Plasma C vs response loop의 방향 | 반시계 → 분포/turnover/활성 대사체, 시계 → 내성/feedback, 없음 → direct (단, 해상도 한계 고려) |
| 2 | 반응 방향 + $t_{ss}$ 용량 의존성 조합 | 4-model 칸 중 하나로 좁힘 |
| 3 | Post-trough 회복이 모델보다 빠른가 | moderator/feedback 누락 가능성 |
| 4 | OFV가 30 iteration stuck-then-drop인가 | $r(k_{in},k_{out}) > 0.98$ 가능성 → $R_0, k_{out}$ 재파라미터화 |
| 5 | 새 약물 duration 질문 | PK clock vs PD clock 어느 쪽이 느린가 |

이 다섯 단계를 통과한 뒤에야 NONMEM 출력에 손을 댐. 자동화 도구는 단계 1, 4를 따라할 수 있지만 **단계 2, 3, 5의 "데이터의 의미를 묻는 직관"은 데이터 외부의 mechanistic prior를 요구하기 때문에 복제되지 않음.** 이게 베테랑과 자동화 도구의 차이임.

### D. 최종 한 줄

간접 반응 모델링은 **"지연을 추가하는 일"이 아님**. **올바른 인과 시계에 지연을 배정하는 일임.**

한 번 정해두면 안 흔들리는 작업 순서:

```
hysteresis 방향
  → 4-model 작용 부위
    → t_ss / peak-shift 선별
      → 초기 파라미터 감사 (graphical)
        → turnover vs link 감별 (비식별성 인정)
          → PK/PD clock 선택
            → PK-rate-limited일 때만 duration 공식
```

---

## 14. References — 정확한 교과서·1차 문헌 출처

### A. 주요 교과서

**[G&W 5e] Gabrielsson & Weiner — Pharmacokinetic and Pharmacodynamic Data Analysis**
- Gabrielsson J, Weiner D. *Pharmacokinetic and Pharmacodynamic Data Analysis: Concepts and Applications.* 5th ed. Stockholm: Apotekarsocieteten; 2016. ISBN 978-91-985558-1-2.
- 핵심 참조 단원:
  - **§2.6.7 (pp.110–111)** — Feedback; moderator 모델 Eq 2:261–2:263; IgG saturable protection; "R = M at dynamic steady state"
  - §3.7–3.10 (pp.235–260) — Indirect response, irreversible action, target consumption
  - §3.11 (pp.247–251) — $t_{ss}$, peak shift, graphical estimation
  - §3.12 (pp.272–275) — DRT
  - §3.13 (pp.317–319) — Baseline drift, disease progression
  - §6 PD6 (pp.758–763) — Turnover vs effect compartment 비식별성
  - §7 PD7 (pp.764–769) — Loss-stimulation Model IV with compound C
  - §9 PD9 (pp.778–783) — Peak shift 과대해석 경고 (Zooparc®)
  - §5 PD5 (pp.742–752) — Initial estimation, reparameterization, Pool 1/Pool 2 비식별성
- 자주 인용되는 식 번호: Eq 2:261, 2:262, 2:263 (moderator); Eq 3:74, 3:76 (turnover, baseline); Eq 3:77, 3:78 ($I(C)$, $S(C)$); Eq 3:103 (reparameterized); Eq 3:110, 3:112 (irreversible kill).

**[R&T] Rowland & Tozer — Clinical Pharmacokinetics and Pharmacodynamics**
- Rowland M, Tozer TN. *Clinical Pharmacokinetics and Pharmacodynamics: Concepts and Applications.* 4th ed. Philadelphia: Wolters Kluwer / Lippincott Williams & Wilkins; 2011. ISBN 978-0-7817-5009-7.
- **판본 표기 주의**: 본문 내 일부 "R&T 5e" 표기는 통칭이며 **실제 인용 근거는 R&T 4판(2011) Chapter 8**의 페이지 매김임.
- 핵심 참조: **Chapter 8 — Response: Time Course and Variability** 전체.
  - pp.234–236 — Hysteresis 분류, naproxen Fig 8-2
  - p.239 — Direct PK–PD link, midazolam Fig 8-6
  - pp.241–242 — Ibuprofen Fig 8-9
  - p.243 — Acenocoumarol vs phenprocoumon, Fig 8-11
  - pp.244–247 — Warfarin blocking-dose, Eq 8-6 / 8-7
  - pp.247–249 — Region 2 linear decline, Eq 8-9
  - pp.249–256 — Succinylcholine dose-duration, Eq 8-12
  - pp.251–254 — Aspirin, omeprazole, paclitaxel, Fig 8-22
  - pp.255–256 — Fig 8-23, 8-24 (PK-rate-limited dose duplication)
  - pp.256–258 — Methylprednisolone linear PK ≠ linear PD
  - pp.258–259 — Rosuvastatin/OATP1B1 disconnect

### B. 1차 문헌

**Sharma & Jusko 1998 — Pool/Precursor Indirect Response (관행적 Models V–VIII)**
- Sharma A, Jusko WJ. "Characteristics of indirect pharmacodynamic models and applications to clinical drug responses." *Br J Clin Pharmacol.* 1998;45(3):229–239. DOI: 10.1046/j.1365-2125.1998.00676.x.
- **명명법 정정**: 원 논문은 'Model V/VI/VII/VIII' 번호를 명시적으로 부여하지 않음. V–VIII 명명은 후속 표준 문헌(Jusko 그룹 후속 review, Mager-Wyska-Jusko 교과서 등)의 관행임.

**Friberg & Karlsson 2002 — Chemotherapy-Induced Myelosuppression**
- Friberg LE, Henningsson A, Maas H, Nguyen L, Karlsson MO. "Model of chemotherapy-induced myelosuppression with parameter consistency across drugs." *J Clin Oncol.* 2002;20(24):4713–4721. DOI: 10.1200/JCO.2002.02.140.
- **모델 구조 정정**: 원 논문은 식별성 확보를 위해 $k_{prol}=k_{tr,1}=k_{tr,2}=k_{tr,3}=k_{circ}\equiv k_{tr}$ (5중 제약)을 **모델 정의의 일부**로 도입함. "임의 고정"이 아닌 모델 구조의 본질적 부분임.

### C. 본문 인용 표기 약속

| 형식 | 의미 |
|---|---|
| `[G&W Eq 3:74; G&W p.237]` | Gabrielsson & Weiner 5판 식 3:74, 본문 p.237 |
| `[G&W pp.235–236]` | Gabrielsson & Weiner 5판 페이지 범위 |
| `[G&W PD4 pp.742–752]` | Gabrielsson & Weiner 5판 PD4 case study |
| `[R&T Eq 8-12; R&T pp.254–255]` | Rowland & Tozer Ch.8 식 8-12, 페이지 |
| `[R&T pp.234–235, 239]` | Rowland & Tozer Ch.8 (콤마 = 비연속 페이지) |
| `[Sharma & Jusko 1998]` | 1차 문헌 |
| `[Friberg & Karlsson 2002]` | 1차 문헌 |

---

> **마지막으로 한 가지만 더**
> 이번 세션의 모든 카드를 외운 학생이 보고서나 발표 자리에서 단 한 가지 질문에 답할 수 있어야 함:
>
> *"당신 모델에서 지연이 어디 사는가, 그리고 그걸 어떻게 증명했는가?"*
>
> 이 질문에 **"fit이 매끄럽다"**고 답하는 학생은 30초 만에 들킴. **"이런 mechanism prior와 이런 design에서 이 구조만 데이터를 설명할 수 있어서"**라고 답하는 학생만 살아남음. 이번 세션은 그 답을 만드는 도구상자임.

---

`C-260518-000145-K7M`

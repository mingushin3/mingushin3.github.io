# 세션 08 리마스터드 — 비선형 PK: 분모 하나의 변신술

## 출처 및 범위 노트

이 장은 Gabrielsson & Weiner의 비선형 PK 영역과 Rowland & Tozer Ch.16–17(nonlinearities/DDI)을 원재료로 함. 다루는 범위는 **비선형 PK, Michaelis–Menten, mechanism-based inhibition, nonlinear binding, drug–metabolite model, DDI, mass-action equivalence triangle**임. `FIGURE_POINTER`는 교과서 원본 그림 확인 위치 안내 텍스트임. 첨부 출처 밖의 규제 지침·CPIC·NONMEM 코드는 본문 근거로 쓰지 않음.

이하 약어: **R&T** = Rowland & Tozer, *Clinical Pharmacokinetics and Pharmacodynamics*, 5e / **G&W** = Gabrielsson & Weiner, *Pharmacokinetic and Pharmacodynamic Data Analysis*, 5e.

---

## 입구 — 9배의 충격, 그리고 이 장 전체를 꿰는 한 줄

진료실에 phenytoin 환자가 한 명 앉아 있음. 어제까지 **300 mg/day**에 농도 **4 mg/L**였던 사람임. 발작이 안 잡혀서 **500 mg/day**로 올렸음 — 용량을 **67%** 올린 것임. 일주일 뒤 농도 측정하니 **36 mg/L**가 나옴. **9배**임.

여기서 멈추고 한 번 생각해보셈. 만약 phenytoin이 선형 PK였다면 농도는 1.67배가 됐어야 함. **4 × 1.67 ≈ 6.7 mg/L** 정도. 그런데 9배가 나왔음. 무려 5.4배의 추가 증폭이 있었던 것임. 이 5.4배는 어디서 왔나? 환자가 약을 더 먹은 것도 아니고, 신장이 갑자기 망가진 것도 아님. **수식 안에 숨어 있던 분모 하나가 무너졌기 때문**임.

그 분모가 바로 **$V_m - R_0$**임. 환자의 $V_m$이 약 500 mg/day인데 dosing rate $R_0$가 거기에 너무 가까워지면 분모가 0에 수렴함. 분모가 0에 수렴하면 농도는 발산함. 이게 phenytoin이라는 약이 평생 좁은 치료역을 갖는 진짜 이유임 [R&T pp.491, 503–506].

> 🎯 **이 장 전체를 꿰는 한 줄:** 비선형 PK는 따로따로 외워야 하는 다섯 개의 chapter가 아님. **mass action이 만든 분모 하나($K_m + C$)가 다섯 얼굴로 변신하는 이야기임.** 그 분모가 capacity에서는 효소 처리분모로, DDI에서는 inhibitor가 추가된 경쟁분모로, binding에서는 결합자리 분모로, transport에서는 운반체 분모로, 그리고 time-dependent kinetics에서는 효소 풀 자체가 시간에 따라 변하는 분모로 나타남. 이 통찰 하나가 있으면 챕터 전체가 **"지금 어느 분모가 흔들리고 있나?"** 라는 단 하나의 triage 질문으로 환원됨.

이 장의 목적은 그래서 이거임. phenytoin 환자가 다시 들어왔을 때 머릿속에서 **5초 안에** "아, 지금 분모 어디가 무너지고 있구나"를 잡아내는 감각을 만드는 것임. 다섯 분모를 알면 외울 게 거의 없음.

---

## §1. 5초 진단 프로토콜과 변신 다섯 얼굴

### 1.1 분모 다섯 얼굴 — 한 번에 보기

선형 PK에서는 분모가 그냥 상수임. CL이 상수, AUC = Dose/CL, 끝. 비선형 PK는 이 분모가 **흔들리는** 이야기임. 흔들리는 자리와 방식에 따라 다섯 얼굴이 됨:

$$
\overbrace{K_m + C}^{\text{① Capacity 분모}}
\;\;\Rightarrow\;\;
\overbrace{K_m(1+C_{u,I}/K_I) + C}^{\text{④ DDI 분모(경쟁 추가)}}
$$

$$
\overbrace{K_d + C_u}^{\text{③ Binding 분모}}
\;\;;\;\;
\overbrace{K_T + C}^{\text{Transport 분모}}
\;\;;\;\;
\overbrace{\frac{dE}{dt}=R_{in}-k_{out}E}^{\text{② 시간 분모(효소 풀)}}
$$

$$
\overbrace{C + EC_{50}(1+A/EA_{50})}^{\text{⑤ PD 분모(수용체 경쟁)}}
$$

다섯 식이 사실 같은 골격임. 분자에 처리능 상한($V_{max}$, $T_m$, $E_{max}$, $nP_t$), 분모에 affinity scale($K_m$, $K_T$, $K_d$, $EC_{50}$) + 현재 노출($C$, $C_u$). 이 골격은 전부 **기질-효소 가역 결합의 quasi-steady-state assumption (QSSA)** 이 만든 한 가족임. 외워야 할 식이 다섯 개가 아니라 **사실상 하나**라는 뜻임.

### 1.2 5초 triage — 데이터에서 분모 흔들림 잡아내기

데이터를 처음 받았을 때 머릿속에서 빠르게 훑어볼 6가지 시그널임. 시그널마다 흔들리는 분모가 다름. 지금 외울 필요 없음 — §2 카드를 다 보고 나면 자동으로 박힘.

| # | 데이터 시그널 | 흔들리는 분모 | 1차 의심 | 검증 |
|---|---|---|---|---|
| 1 | semi-log에서 **terminal slope이 dose마다 다름** | ① Capacity ($K_m+C$) | MM saturable elimination | dose-normalized curve 겹침 여부 [G&W p.116] |
| 2 | 같은 dose 반복에서 **trough가 한 방향으로 슬슬 이동** | ② Time ($dE/dt$) | autoinduction or time-dep CL | single vs multi-dose fit 차이 [G&W pp.580–585] |
| 3 | total CL_R은 그대로인데 **unbound CL_R이 변함** | ③ Binding ($K_d+C_u$) | nonlinear protein binding | 용량별 $f_u$ 직접 측정 [R&T pp.511–516] |
| 4 | 같은 inhibitor 병용인데 **oral DDI ≫ IV DDI** | ④ DDI + first-pass | gut wall/first-pass 우세 | IV/oral crossover, $F_G$·$F_H$ 분리 [R&T pp.553–554] |
| 5 | $V_{max}/K_m \approx Q_H$ | 분모 자체보다 **혈류가 율속** | flow-limited (high-extraction) | $E_H = CL_H/Q_H$ 계산 [G&W p.140] |
| 6 | single-dose fit이 multi-dose에서 **체계적 over/under** | ② Time ($k_{out}$ 시계) | autoinduction, MBI, withdrawal trap | enzyme turnover compartment 추가 [G&W pp.580–585] |

$$
\underbrace{E_H}_{\text{간 추출분율}}
=
\frac{\underbrace{CL_H}_{\text{간 CL}}}{\underbrace{Q_H}_{\text{QH 혈류}}}
\qquad;\qquad
\underbrace{V_{max}/K_m}_{\text{저농도 처리능}}\approx \underbrace{Q_H}_{\text{혈류한계}}
$$

### 1.3 진단 순서 — 절대 뒤집으면 안 되는 흐름

```text
[1단계: 분모가 흔들렸나?]
  → dose-normalized concentration-time plot
  → AUC/Dose vs Dose plot
  → 겹치면 선형, 안 겹치면 다음 단계

[2단계: 어느 분모가 흔들렸나?]
  → AUC/Dose ↑ vs ↓  방향성
  → 시간에 따라 변하나?
  → total vs unbound 차이 있나?
  → 다른 약 같이 먹나?

[3단계: 어떤 파라미터가 상수가 아니게 됐나?]
  → V_max, K_m, f_u, f_m, k_out, E_max 중 어디?
  → 그게 임상적으로 무엇을 의미?
```

이 순서를 뒤집으면 비선형 모델을 fitting시키는 건 가능하지만 **왜 파라미터가 흔들리는지는 영영 설명 못 함** [G&W p.113], [R&T p.492]. 즉 NONMEM RUN은 돌아가는데 보고서는 못 쓰는 상황이 됨.

🧭 **읽는 흐름:**
- §2: 분모 다섯 얼굴 하나씩 해부 (Card 1~6)
- §3: 헷갈리는 쌍 8개 (CP1~CP8)
- §4: 5초 triage 자기 테스트 (Q1~Q18)
- §5: 한 페이지 압축 기억 모델

---

## §2. 분모 다섯 얼굴 해부 카드

<!-- SLIDE_START: Card 1 | title: 진단 - 분모가 흔들렸는지부터 보는 첫 그림 -->

### Card 1. 진단 — "어느 분모를 봐야 하지?"는 그 다음 질문, 일단 **흔들렸나**부터

> **거장의 첫 손**  
> 비선형성을 보면 "MM이다", "induction이다", "DDI다" 하고 **모델 이름부터 부르려는 본능**, 그게 함정임. 모델 이름이 먼저 나오면 진단을 건너뛴 것임. 진짜 첫 손은 **dose-normalized plot과 AUC/Dose 방향**을 보는 것임. 이거 보면 CL·F·분포·결합·시간 의존성 중 무엇이 흔들렸는지가 강제로 좁혀짐.

**핵심:** 선형 PK의 정체는 superposition임. 용량을 두 배로 하면 농도도 두 배. 이 superposition이 깨지면 **CL·F·분포·binding 중 적어도 하나가 dose나 time의 함수가 됐다**는 뜻임 [G&W pp.112–114], [R&T p.492].

#### 첫 그림 두 장

비선형 PK 검토에서 **첫 그림은 spaghetti concentration-time plot이 아님.** 그건 가독성도 나쁘고 정보도 없음. 첫 그림은 이 두 장임:

**그림 1: dose-normalized concentration-time plot.** 모든 용량의 농도-시간 곡선을 dose로 나눠서 한 그래프에 겹쳐 그림. 선형이면 모든 곡선이 정확히 겹침. 안 겹치면 비선형임. 단순함.

**그림 2: AUC/Dose vs Dose plot.** $AUC/Dose$가 dose↑와 함께 **올라가면** → CL 감소 or F 증가. **내려가면** → CL 증가 or F 감소.

$$
\underbrace{AUC/Dose}_{\text{용량당 노출}}
\quad\xrightarrow{\text{dose}\uparrow}\quad
\overbrace{\uparrow}^{\text{CL↓ or F↑}}\;\;\text{or}\;\;\overbrace{\downarrow}^{\text{CL↑ or F↓}}
$$

#### 함정 한 가지 — AUC/Dose 내려가면 "elimination↑"라고 닫지 말 것

여기서 흔한 실수가 있음. $AUC/Dose$가 dose↑와 함께 내려가면 "elimination 증가했네, capacity-limited 어디?" 하고 곧장 Card 2로 점프하는 것임. **그러면 안 됨.** F가 떨어진 경우도 정확히 같은 그림이 나옴.

**Gabapentin이 그 prototype임.** 항경련제이자 항신경통제로, LAT1(L-amino acid transporter 1)을 통해 흡수됨. **300 mg 단회 투여 시 F ≈ 60%, 1600 mg 단회 투여 시 F ≈ 27%로 dose↑와 함께 F가 절반 이하로 떨어짐**. 이유? 흡수 transporter가 포화되기 때문임. saturable absorption은 elimination 비선형성과 **정확히 같은 mass action 골격**을 따름. 다만 분모가 luminal $K_T^{abs}+C^{lumen}$일 뿐임 [R&T pp.495–499].

$$
\underbrace{\text{흡수 속도}}_{\text{Rate}_{abs}}
=
\frac{\overbrace{T_m^{abs}}^{\text{흡수상한}}\cdot\underbrace{C^{lumen}}_{\text{관강 C}}}{\underbrace{K_T^{abs}+C^{lumen}}_{\text{흡수분모}}}
\quad\xrightarrow{C^{lumen}\uparrow}\quad
\underbrace{F\downarrow}_{\text{F 감소}}
$$

→ 그래서 진단은 "$AUC/Dose$ 내려감 = elimination↑" 으로 닫지 말고, **CL↑ vs F↓ 두 후보를 IV/oral crossover로 분리**해야 함. 같은 mol을 두 경로로 주고 비교하는 것임.

이게 첫 카드의 핵심 깨달음임 — **흡수 분모, 제거 분모, 억제 분모, 결합 분모가 사실 같은 mass action 골격의 다른 응용임.** Card 1의 흡수 분모는 Card 2의 제거 분모로, 그게 Card 4의 결합 분모로, Card 5의 억제 분모로 이어짐.

#### 시간 의존성의 정의 — 헷갈리지 마셈

농도가 변해서 apparent CL이 달라 보이는 것은 **시간 의존성이 아님.** 그건 농도 의존성임. **효소량·수송체 활성·관류 같은 생리/생화학 상태 자체가 시간에 따라 변해야** 진짜 시간 의존성임 [G&W p.112], [R&T p.492]. 이 정의 안 잡으면 Card 2(농도 의존)와 Card 3(시간 의존)이 평생 섞임.

> 🔑 **실무 규칙:** 비선형성 의심된다? 비선형 모델 fitting부터 시작하면 안 됨. **dose-normalized plot 두 장이 먼저임.** 안 그러면 capacity, F change, time-dependence, binding artifact가 fit 안에서 다 섞여서 어떤 파라미터가 왜 흔들렸는지 끝까지 못 가림.

**Card 1 요약 한 줄:** "비선형이다"를 선언하는 카드가 아니라, 다음 카드 어디로 갈지를 **강제하는** 카드임. 다음 질문 4개를 강제로 띄움 — AUC/Dose ↑↓? 시간에 따라 변? total vs unbound 차이? 다른 약? 이 4개가 Card 2~Card 6의 입구임.

> 📖 **G&W p.113, Fig.2.85·Fig.2.86:** $AUC/Dose$ 패턴 인식 시각 분류임. 곡선이 어떻게 휘는지를 눈으로 익혀두면 패턴 인식이 기억에 의존하지 않게 됨.

---

<!-- SLIDE_START: Card 2 | title: Capacity 분모 K_m+C - phenytoin이 이 카드 자체임 -->

### Card 2. ① Capacity 분모 — $K_m + C$가 직접 모습으로 드러나는 자리

> **앞 카드와의 연결**  
> Card 1에서 dose-normalized profile이 안 겹친다는 걸 확인했음. 이제 묻는 질문은 하나임 — **"그 실패가 제거 capacity의 분모에서 왔나?"**

> **거장의 시각**  
> MM kinetics를 "포화되면 zero-order"라는 한 줄로 외우는 건 진짜 약함. 그런 식의 정리는 시험에는 통하지만 임상 환자한테는 안 통함. 진짜 위력은 거기가 아님. **$K_m + C$ 이 분모 하나가** $CL(C)$ 감소, rate plateau, $C_{ss}$ 폭증, DDI 분모를 **전부 같은 골격으로 묶어줌**. capacity 근처에서 작은 용량 변화가 분모를 깎으면서 큰 노출 변화로 증폭되는 그 비대칭성 — 그게 임상에서 phenytoin 독성을 만드는 핵심임. **이 카드가 이번 장에서 임상 파급력이 가장 큰 카드임.**

#### 분모의 정체

$V_{max}$와 $K_m$의 분모 $K_m + C$는 어디서 왔나? 기질-효소 가역 결합의 **quasi-steady-state assumption (QSSA)** 이 만든 질량 작용의 산물임. 효소-기질 복합체가 빠르게 평형에 도달한다는 가정에서 출발해서 도출되는 식임. 그리고 이 분모가 그대로 Card 5의 DDI에서 competitive 분모 $K_m(1+C_{u,I}/K_I)+C$로 확장됨. **Card 2의 분모와 Card 5의 DDI 분모는 같은 mass action 골격이 다른 맥락에 나타난 것일 뿐임** [G&W pp.115–118].

$$
\underbrace{K_m+C}_{\text{Card 2 분모}}
\quad\xrightarrow{\text{inhibitor 추가}}\quad
\underbrace{K_m(1+C_{u,I}/K_I)+C}_{\text{Card 5 분모}}
$$

#### 핵심 수식

$$
\underbrace{CL(C)}_{\text{농도 CL}}
=
\frac{\overbrace{V_{max}}^{\text{Vmax}}}{\underbrace{K_m}_{\text{Km 반포화}}+\underbrace{C}_{\text{현재 C}}}
$$

[수식 계열: G&W Eq.2:266; source tag: G&W p.115]

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $CL(C)$ | volume/time | 농도에 따라 달라지는 겉보기 청소율 | $C$↑ 시 감소 |
| $V_{max}$ | amount/time or concentration/time | 효소/수송체 처리 상한 | 효소량, 유도/억제, 간기능 |
| $K_m$ | concentration | 반최대 처리 농도 scale | 기질-효소 affinity, 경쟁 억제 |
| $C$ | concentration | 현재 기질 농도 | 투여량, 축적, 분포 |

💡 **톨게이트 비유:** 좁은 톨게이트 한 곳에 차가 몰리는 상황임. 톨게이트의 최대 처리량이 $V_{max}$, 정체가 보이기 시작하는 교통량 scale이 $K_m$. 한산할 땐 차가 두 배 와도 두 배가 그냥 통과함 (저농도 linear, $CL \approx V_{max}/K_m$). 정체가 시작되면 차 한 대 추가될 때마다 통과 속도가 비대칭으로 무너짐 (capacity 근처 비선형성).

$$
\underbrace{Rate}_{\text{처리속도}}
=
\frac{\overbrace{V_{max}}^{\text{Vmax 상한}}\cdot\underbrace{C}_{\text{기질 C}}}{\underbrace{K_m}_{\text{Km}}+\underbrace{C}_{\text{포화구동 C}}}
$$

$$
\underbrace{\frac{dC}{dt}}_{\text{C 변화율}}
=
-\frac{\overbrace{V_{max}}^{\text{제거상한}}\cdot\underbrace{C}_{\text{현재 C}}}{\underbrace{K_m+C}_{\text{포화분모}}}
$$

$$
\underbrace{AUC}_{\text{AUC 노출}}
=
\frac{\underbrace{C^0}_{\text{초기 C}}}{2\overbrace{V_{max}}^{\text{제거상한}}}
\left(
\underbrace{K_m}_{\text{Km}}+\frac{\underbrace{C^0}_{\text{초기 C}}}{2}
\right)
\quad\text{(IV bolus, MM)}
$$

[G&W Eq.2:271; source tag: G&W p.117]

이 AUC 식 한번 음미해보셈 — 고농도에서는 농도 감소가 거의 선형이라 시간평균 농도가 $C^0/2$에 가깝지만, 농도가 $K_m$ 부근까지 내려오면 소실이 지수적으로 가속돼서 시간평균이 그보다 작아짐. **이 AUC 식 안에 $K_m$이 들어 있다는 것 자체가 "용량 한계의 수학적 흔적"임.** 선형 PK라면 $K_m$이 들어올 자리가 없음 [G&W p.117].

⚠️ ODE에서 단위 주의: $V_{max}$가 concentration/time 단위면 $dC/dt$에 직접 쓸 수 있지만, 총량/time 단위면 부피로 나눠야 함. 본문에서는 약식 표기만 두고 주 출처 태그는 Eq.2:266–2:274로 둠.

#### 두 극한의 표정

$$
\underbrace{C\ll K_m}_{\text{저농도}}\Rightarrow \underbrace{CL}_{\text{CL 상수화}}\approx \frac{V_{max}}{K_m}
\qquad;\qquad
\underbrace{C\gg K_m}_{\text{고농도}}\Rightarrow \underbrace{Rate}_{\text{처리속도}}\approx V_{max}
$$

- **저농도 ($C \ll K_m$):** $CL \approx V_{max}/K_m$ 상수. 겉보기로는 1차 속도. **여기서 $V_{max}$와 $K_m$를 따로 추정할 수 없다는 게 핵심 식별성 문제임 (뒤에서 다룸).**
- **고농도 ($C \gg K_m$):** 제거 속도가 $V_{max}$에 도달, 청소율은 떨어짐. 작은 용량 증가가 비대칭적으로 큰 AUC/$C_{ss}$ 증가를 만듦 [G&W pp.115–119], [R&T pp.500–506].

#### 임상 앵커 1 — Phenytoin (CYP2C9 substrate, 좁은 치료역 항경련제)

전형적 성인 환자에서 $V_m \approx 500$ mg/day, $K_m \approx 0.4$ mg/L (unbound), $f_u \approx 0.1$. total 기준으로 환산하면 $K_m' \approx 4$ mg/L임. 그리고 phenytoin의 치료역이 total 10–20 mg/L임 — **이미 $K_m'$의 2.5–5배 영역**임. **우리가 임상에서 노리는 농도 자체가 capacity 한계 근처**라는 뜻임. 이게 phenytoin이 좁은 치료역을 가질 수밖에 없는 수학적 이유임.

도입 사례 다시 봅시다: 300 mg/day → 4 mg/L였던 환자, 500 mg/day로 올렸더니 36 mg/L. 67% 증량이 9배 증가.

**정상상태 분모 방정식:**

$$
\underbrace{C_{u,ss}}_{\text{Css,u}}
=
\frac{\underbrace{K_m}_{\text{Km,u}}\cdot\underbrace{R_0}_{\text{투여 속도}}}{\underbrace{V_m-R_0}_{\text{capacity 여유}}}
$$

[R&T Eq.16-7; source tag: R&T p.503]

이 식의 진짜 정체는 한 문장임 — **$R_0$가 $V_m$에 가까워질수록 분모 $V_m - R_0$가 작아지고, 그래서 $C_{u,ss}$가 발산함.** $K_m$은 unbound 기준이라 total로 작업할 때의 $K_m'$와 구분 필수.

#### $V_m$ 민감도 — 조건부 정량, **portable rule 절대 아님**

여기서 매우 자주 잘못 외워지는 사실 하나임. "phenytoin에서 $V_m$ 20% 감소하면 $C_{ss}$ 2배가 됨" — 이거 들어본 적 있을 것임. **R&T p.506의 원문이 정확히 무슨 말을 했는지** 보자:

조건이 명시되어 있음: $R_0 = 300$ mg/day, $V_{m1} = 500$ mg/day, $V_{m2} = 400$ mg/day. 그러면:

$$
\overbrace{\frac{C_{u,ss,2}}{C_{u,ss,1}}}^{\text{R\&T Eq.16-7 비}}
=
\underbrace{\frac{V_{m1}-R_0}{V_{m2}-R_0}}_{\text{capacity 분모 비}}
=
\frac{\underbrace{500-300}_{=200}}{\underbrace{400-300}_{=100}}
=
\overbrace{2}^{\text{2배 발산}}
$$

→ **이 특정 anchor에서만** $V_m$ 20% 감소 → $C_{ss}$ 정확히 2배임. 같은 $R_0=300$에서 $V_{m2}=600$이면 $(500-300)/(600-300)=0.67$이라 33% 감소. 그리고 R&T가 명시한 발산 위험 — **$V_m$이 300 mg/day로 떨어지면 분모 $V_m - R_0 = 0$이 돼서 $C_{ss} \to \infty$**, $V_m < 300$이면 정상상태 자체가 도달 불가 (input이 capacity 초과) [R&T p.506].

⚠️ **그래서 진짜 식은 비율이 아니라 탄력성임.** capacity 분모 $V_m-R_0$의 탄력성을 보면 발산 경향이 한눈에 보임:

$$
\underbrace{\frac{\Delta C_{ss}/C_{ss}}{\Delta V_m/V_m}}_{\text{Vm 탄력성}}
\approx
-\overbrace{\frac{V_m}{V_m-R_0}}^{\text{capacity 증폭인자}}
$$

→ $R_0 \ll V_m$(저용량 영역)에서는 탄력성 ≈ −1, 거의 **단순 비례**. $R_0 \to V_m$(capacity 근처)에서 **발산**. 한 문장으로 — **"phenytoin 환자라도 시작점이 어디인가가 $V_m$ 변화 민감도의 크기를 결정함."** R&T p.506의 2배 숫자는 $R_0/V_m=0.6$ 시작점의 prototype 정량이지 portable rule 아님. 환자가 capacity 한참 아래($R_0/V_m < 0.3$)면 $V_m$ 20% 감소가 $C_{ss}$ 25% 증가에서 끝나고, capacity 바로 근처($R_0/V_m > 0.8$)에서는 같은 변화가 $C_{ss}$를 4배 이상 증폭시킴.

#### 정상상태 도달 시간 — 발산하는 두 번째 함정

분모 발산만 무서운 게 아님. **plateau에 도달하는 시간 자체가 발산함** (R&T Eq.16-10, p.505). 300/350/400/425 mg/day일 때 plateau 농도는 각각 6/9.3/16/22.7 mg/L인데, **그 plateau에 도달하는 시간은 용량이 $V_m$에 가까울수록 수일에서 수주로 늘어남.** 임상 함의는 직접적임 — capacity 근처에서는 모니터링 간격을 정상상태 도달 시점 **이후로 옮겨야** 함. 1주 만에 측정해서 농도 9.3이라고 안심하면 안 됨. 그 환자는 아직 plateau 도달 전임.

**혼합 경로 (R&T Eq.16-11):** 비선형 경로 비중 $f_m^{NL}$이 **0.5 이상**이면 용량-반응 비대칭이 임상적으로 의미 있게 나타남 [R&T p.506]. 0.5 이하면 다른 선형 경로가 비선형 경로를 희석해서 효과를 줄임.

→ 그래서 **phenytoin은 "capacity 분모가 임상 농도를 직접 만든다"는 사실의 정량 원형(prototype) 사례임.**

#### 임상 앵커 2 — Alcohol (ethanol, capacity 근처 pseudo-steady state의 prototype)

근사값: $V_m \approx 10$ g/hr, $K_m \approx 100$ mg/L, $V_d \approx 42$ L (70 kg). 임상 농도 영역에서는 거의 0차 소실에 가까운 직관을 줌.

- 1 drink ≈ 14 g.
- **4 drinks/hr = 56 g/hr** → $V_m$ 크게 초과 → 농도 무한정 누적.
- **0.5 drinks/hr = 7 g/hr** → $V_m$ 안 → pseudo-steady state $C_{ss} \approx 233$ mg/L (혈중 약 0.23%) [R&T pp.501–502].

다만 ethanol은 capacity 외에도 흡수·혈류·시간 인자가 다 같이 섞여 있음. 단일 MM 사례로 과단순화하면 안 됨. → 그래서 ethanol은 **"$V_m$에 근접한 입력 속도가 pseudo-steady state를 만든다"**는 직관의 사례인 동시에 **"단일 기전 모델의 위험성"**을 보여주는 사례임.

#### 임상 앵커 3 — Ascorbic acid (vitamin C, phenytoin의 거울상)

- 75 mg/day에서 9 mg/L, 10,000 mg/day에서 약 19 mg/L → **133배 용량 증가가 약 2배 농도 증가만** 만듦.
- 이유: 농도 상승과 함께 신장 청소율이 폭발적으로 증가. $CL_R < 0.5$ mL/min @ 9 mg/L → 21 mL/min @ 19 mg/L, **42배 이상 증가**.
- 기전: 포화성 재흡수가 풀리면서 **약물이 빠져나가는 밸브가 열리는** 효과. 즉 같은 mass action 분모지만 방향이 **반대**임 — Card 2의 elimination 분모는 고용량에서 처리가 막혀서 농도 ↑, ascorbic acid의 재흡수 분모는 고용량에서 재흡수가 풀려서 청소율 ↑.

→ 같은 "비선형 PK"인데 임상 결과는 정반대임. **phenytoin은 고용량에서 독성 위험 폭증, ascorbic acid는 고용량에서 추가 노출 효율이 급격히 감소.** → ascorbic acid는 **"비선형 PK가 항상 위험 쪽으로만 가지 않는다"**는 사실의 임상 prototype.

#### 모델링 실무 — 식별성 문제 두 개

🔑 **실무 규칙 1: $V_{max}$와 $K_m$를 따로 추정하려면 농도 범위가 곡률(curvature) 영역을 지나야 함.** 특히 **$K_m$ 주변 또는 그 이하 관측값**이 꼭 있어야 함. high-concentration plateau만 있으면 $V_{max}$와 $K_m$이 ridge처럼 같이 움직임 — 즉 $(2V_{max}, 2K_m)$, $(3V_{max}, 3K_m)$ 같은 조합들이 모두 비슷한 fit을 줌. 곡률이 잡혀야 둘이 분리됨 [G&W p.117].

🔑 **실무 규칙 2: 비선형 적합을 시작하기 전 그래프 방법으로 $V_{max}/K_m$, $V_c$, distribution terms의 초기 추정값을 손산출.** nonlinear fitting은 초기값에 민감해서 손산출 30분이 모델 디버깅 며칠을 줄임 [G&W pp.556–562].

#### "Vmax–Km Ridge Lock" — 식별성 함정

단일 용량 또는 좁은 용량 범위 데이터로 $V_{max}, K_m, V_d$ 동시 추정하면 $\rho(V_{max}, K_m) > 0.9$ 부근의 강한 상관이 생김. G&W p.116에서는 −0.96 사례 보고. $V_d$와 $K_m$ 사이도 −0.95 부근 음의 상관 흔함. **구제 세 가지:** 용량 수준 추가, 외부 정보로 $K_m$ 사전 고정, sampling을 $K_m$ 근방까지 낮춰 곡률 잡기 [G&W p.116, p.117].

#### Single-dose Fit Trap — 다중투여에서 무너지는 단일 용량 모델

흔한 함정 하나 더. 단일 용량 fit이 좋으면 다중 투여 예측도 정확할 거라고 생각하는 것임. **틀린 가정임.** 단일 용량 데이터에서는 여러 $(V_{max}, K_m)$ 조합이 비슷한 농도 궤적과 좋은 OFV 수렴을 만들 수 있음. 그러면 어떻게 되나? 단일 용량 fit을 믿고 다중 투여 예측에 쓰면 — **$V_{max}$–$K_m$ ridge가 그대로 끌려가서 trough envelope를 오예측**함. 임상에서는 phenytoin 독성 농도(>20 mg/L)나 무효 농도(<10 mg/L)를 놓치고, 규제 쪽에서는 RSE와 상관구조 악화로 dose ladder 또는 $K_m$ prior fix를 요구받는 재분석 risk까지 끌어옴.

OFV 잘 수렴, $V_{max}$–$K_m$ RSE 둘 다 50% 초과, $\rho(V_{max}, K_m)$ 강한 음의 상관? 이런 패턴 보이면 단일 모델 fit으로 임상 의사결정 내리지 말고 **용량 사다리(dose ladder) 추가** 또는 **$K_m$ 외부 정보 사전 고정** 후 재추정.

#### 시그널 #1 vs 시그널 #5 — 같은 카드 안에서도 분기를 가르기

§1.2 시그널 중 #1번(terminal slope이 dose마다 다른가)과 #5번($V_{max}/K_m$이 $Q_H$에 근접하는가)이 Card 2의 핵심 판정임. 둘 다 capacity 카드지만 **가리키는 병목 위치와 임상 함의가 다름**:

- **시그널 #1 → intrinsic enzyme capacity 포화 (phenytoin prototype).** $V_{max}$ 자체가 율속. 효소 내재 한계가 dose response 비대칭의 원인. 임상 함의: **dose ladder 폭증, plateau 도달 시간 발산, TDM 모니터링 간격 조정.**
- **시그널 #5 → system-level flow constraint (ethanol prototype).** 효소 capacity가 매우 커서 **간 혈류 $Q_H$ 자체가 율속**이 됨. 임상 함의: **간기능보다 hepatic blood flow 변화(심부전, 운동, 식이, propranolol 같은 혈관활성 약물)가 노출을 흔듦.**

$$
\underbrace{\text{시그널 \#1}}_{\text{효소 내재 한계}}
\Rightarrow
\overbrace{V_{max}\text{ 자체가 율속}}^{\text{intrinsic capacity}}
\qquad;\qquad
\underbrace{\text{시그널 \#5}}_{\text{혈류 한계}}
\Rightarrow
\overbrace{Q_H\text{가 율속}}^{\text{flow-limited}}
$$

판별 한 줄: #1만 yes → MM 효소 capacity 포화. #5만 yes → flow-limited high-extraction drug. **둘 다 yes** → well-stirred 가정 붕괴 신호 → dispersion model 또는 parallel tube model로 확장 검토.

> ⚠️ **자주 잘못되는 추론:** AUC가 증가했다고 해서 그게 F 증가인지 CL 감소인지 **AUC만 봐서는 절대 안 갈림.** 비선형 구간에서 AUC만 보고 bioavailability를 단정하지 말 것. AUC 기반 F 계산은 CL이 상수일 때만 안전함 [G&W p.116].

**Card 2 요약:** MM kinetics의 핵심은 "포화되면 zero-order"가 아님. **CL이 농도의 함수가 되면서 용량 조정·AUC 해석·$t_{1/2}$·정상상태 도달 시간이 전부 비선형화된다**는 것. 이게 진짜 핵심임.

> 📖 **G&W p.115 Fig.2.88; R&T p.503 Fig.16-9, p.505 Fig.16-10:** 같은 분모 직관이 세 가지 형태로 펼쳐짐 — CL은 떨어지고, rate는 plateau에 닿고, 임상 정상상태는 용량 한계 근처에서 미친 듯이 민감해짐.

---

<!-- SLIDE_START: Card 3 | title: 시간 분모 - 효소 시계는 농도 시계와 따로 돈다 -->

### Card 3. ② 시간 분모 — 농도 시계와 효소 시계는 **다른 시계**임

> **앞 카드와의 연결**  
> Card 2가 농도에 따른 capacity 병목이었다면, Card 3는 **파라미터 자체가 시간에 따라 움직이는** 두 번째 시계를 분리해봄.

> **거장의 시각**  
> 시간 의존성을 농도 변화로만 읽으면 induction, autoinduction, MBI, washout trap이 한 데 뒤섞임. 그걸 푸는 방법은 딱 하나 — **약물 농도 시계와 enzyme pool 시계를 따로 떼서** 보는 것. 이 분리 하나가 trough drift와 지연 회복의 원인을 즉시 보이게 만듦.

**핵심:** 시간 의존적 약동학은 농도가 달라져서 청소율이 달라 **보이는** 현상이 아님. **효소·수송체·생리학 자체가 시간에 따라 변하는** 현상임 [G&W p.112], [G&W pp.119–129], [R&T pp.516–519].

#### 사실 시계는 셋임 (master clock 위계)

induction/MBI 상황에서는 세 시계가 동시에 돔. 관찰되는 dynamics는 셋 중 **가장 느린 시계가 지배**함:

- $t_{1/2}^{drug}$ — 약물 자체의 반감기.
- $t_{1/2}^{perpetrator}$ — inducer/inhibitor의 반감기.
- $t_{1/2}^{enzyme} = \ln 2/k_{out}$ — enzyme pool의 turnover.

$$
\underbrace{\text{Master clock}}_{\text{지배 시계}}
=
\max\left(
\overbrace{t_{1/2}^{drug}}^{\text{약물}},
\overbrace{t_{1/2}^{perpetrator}}^{\text{유도/억제제}},
\overbrace{t_{1/2}^{enzyme}}^{\text{효소}}
\right)
$$

이게 왜 중요한지 — 곧 만날 **Phenobarbital–Dicumarol** 케이스에서 plateau 도달이 3–4주 걸리는 이유가 phenobarbital 자체 $t_{1/2} \approx 4$ days가 가장 느려서 induction이 그것에 묶이기 때문임 [R&T pp.560–561].

#### 핵심 전환 방정식

$$
\underbrace{\frac{dE}{dt}}_{\text{효소 변화율}}
=
\underbrace{R_{in}}_{\text{효소 생성}}-
\underbrace{k_{out}E}_{\text{효소 소실}}
\qquad;\qquad
\underbrace{E_{ss}}_{\text{효소 정상상태}}
=
\frac{\underbrace{R_{in}}_{\text{생성속도}}}{\underbrace{k_{out}}_{\text{소실상수}}}
$$

[G&W Eq.2:275–2:278; source tag: G&W pp.120–121]

| 파라미터 | 단위 | 의미 | 변화 원인 |
|---|---|---|---|
| $E$ | enzyme amount/activity | 효소/수송체 pool | 유도, MBI, 회복 |
| $R_{in}$ | amount/time | 효소 생성 속도 | 유도, 생리적 조절 |
| $k_{out}$ | 1/time | 효소 소실 속도상수 | turnover, 질환 상태 |
| $E_{ss}$ | enzyme amount/activity | 효소 정상상태 | $R_{in}/k_{out}$ 균형 |

💡 **공장 비유:** 농도 시계는 혈액 속 약물이 사라지는 시계. 효소 시계는 공장 설비가 새로 설치되거나 고장 난 뒤 교체되는 시계. **MBI에서는 약물이 사라져도 설비 교체가 끝날 때까지 처리능이 회복되지 않음.** 약은 다 빠졌는데 공장은 정상화 안 된 상태임.

#### 효소가 바뀌면 CL이 바뀜

효소 수준이 바뀌면 $CL(t)$가 바뀜. **유도(induction)** 는 효소량이 늘어 $V_{max}$나 $CL_{int}$ capacity를 끌어올림. **탈유도 또는 MBI**는 효소 활성 회복을 $k_{out}$ 시계에 묶어서 처리 능력 회복을 지연시킴 [G&W pp.120–128], [R&T pp.557–561]. 

참고로 $CL_{int}$ (intrinsic clearance)는 비결합 약물에 대한 효소/수송체의 본질적 처리 능력임. well-stirred 간 청소율은:

$$
\underbrace{CL_H}_{\text{간 CL}}
=
\frac{\underbrace{Q_H}_{\text{QH 혈류}}\cdot\underbrace{f_u}_{\text{fu}}\cdot\underbrace{CL_{int}}_{\text{CLint}}}{\underbrace{Q_H}_{\text{혈류한계}}+\underbrace{f_u\cdot CL_{int}}_{\text{fu·CLint}}}
$$

#### 자가유도(autoinduction) — 자기가 자기 청소율을 키움

**PK22 자가유도 (Compound X):** 반복 주입 데이터, 모델 파라미터 7개 ($V_c$, $V_t$, $a$, $k_{12}$, $k_{21}$, $k_{out}$, $E_0$). Table 22.2의 핵심 추정값 $a \approx 0.041$, $k_{out} \approx 0.023$ h⁻¹. → 효소 시상수 $1/k_{out} \approx 43$ h, $t_{1/2}^{enzyme} \approx 30$ h. **이 design의 강점 한 줄:** trough sampling이 효소 동역학 시간 척도를 직접 잡아냄. 그래서 $a$(농도-CL 기울기)와 $k_{out}$(시간 차원)이 따로 식별됨 [G&W pp.580–585, p.583].

**Carbamazepine** (항경련제, 자가유도 prototype): 전환 시간 약 5일. 반복투여 첫 1–2주 동안 청소율이 시간에 따라 변하는 임상 앵커. → carbamazepine 도입기 TDM에서 "trough가 떨어진다 = adherence 문제"가 아니라 **자가유도로 CL이 올라가는 정상 dynamics**일 수 있다는 사실의 임상 사례 [R&T p.518].

**Phenobarbital–Dicumarol** (barbiturate inducer × 항응고제 substrate): 유도 시작/종료가 즉시 일어나지 않고 3–4주 scale로 보이는 이유는 inducer/효소 전환 시계 때문임. **phenobarbital $t_{1/2} \approx 4$ days**가 sustained release처럼 작용해서 induction plateau가 $4$–$5\,t_{1/2} \approx 16$–$20$일 영역에서 도달 [R&T pp.560–561]. → master clock 위계의 직접 anchor.

#### 기전 기반 억제(MBI) — 효소를 망가뜨려 버림

MBI는 가역적 억제와 차원이 다름. **효소를 기능적으로 제거함.** 여기서 "제거"는 효소량이 사라진다는 뜻만이 아니라 **효소 활성이 회복 전까지 유효하지 않다**는 뜻임. 회복은 inhibitor 농도 사라지는 속도뿐 아니라 **효소 재합성/분해 시계**에 의해 제한됨.

#### MBI 정량 — Clarithromycin이 보여주는 충격적 차이

**Clarithromycin–CYP3A4 MBI** (macrolide 항생제, CYP3A4 MBI prototype) [R&T p.558, Eqs.17-13/17-14]

R&T Eq.17-13/14의 in-vivo MBI factor를 정확히 풀어쓰면:

$$
\underbrace{CL_{inhibited}}_{\text{억제 후 CL}}
=
\frac{\underbrace{CL_{normal}}_{\text{기저 CL}}}{1+\overbrace{\dfrac{k_{inact}}{k_E}}^{\text{turnover 대비 불활성화}}\cdot\overbrace{\dfrac{C_u}{K_I}}^{\text{유효 노출}}}
$$

[R&T Eq.17-13; source tag: R&T p.557]

여기서 **두 가지 strength index가 구분됨** — 자주 혼동되는 자리니까 표로 박아둠:

| 지표 | 정의 | 의미 | 차원 |
|---|---|---|---|
| $k_{inact}/K_I$ | **in-vitro MBI potency** | 단위 inhibitor 노출당 효소 불활성화 속도 — **MBI 강도의 표준 보고 지표** | (1/time)/(concentration) |
| $k_{inact}/k_E$ | **in-vivo magnitude factor** | baseline 효소 turnover 대비 불활성화 상대속도 — **Eq.17-13 분모에 들어가 CL 감소의 자릿수를 결정** | dimensionless |
| $C_u/K_I$ | **유효 inhibitor 노출** | 임상 $C_u$가 $K_I$ 대비 얼마나 큰가 | dimensionless |

$$
\underbrace{k_{inact}/K_I}_{\text{in-vitro 강도}}
\xrightarrow{\times\,C_u}
\underbrace{k_{inact}\cdot C_u/K_I}_{\text{in-vivo 불활성화 속도}}
\div
\underbrace{k_E}_{\text{효소 turnover}}
=
\underbrace{(k_{inact}/k_E)\cdot(C_u/K_I)}_{\text{Eq.17-13 분모 항}}
$$

→ **임상 함의:** in-vitro에서 $k_{inact}/K_I$가 큰 inhibitor라도 **효소 turnover가 빠른 조직(예: 장상피)에서는 in-vivo MBI 효과가 제한**됨. 반대로 효소 turnover가 느린 간 CYP3A4에서는 같은 $k_{inact}/K_I$가 자릿수 단위로 큰 CL 감소를 만듦. 이게 R&T가 MBI inhibitor 분류에서 $k_E$를 함께 보라고 명시한 이유임 [R&T p.558].

**Clarithromycin 정량 anchor — 자릿수 단위 차이 확인:**

- $k_{inact} \approx 0.07$ min⁻¹ (포화 억제제 조건의 불활성화 속도) [R&T p.558]
- $K_I \approx 7$ mg/L (in-vitro CYP3A4 억제) [R&T p.556]
- $k_E \approx 0.23$ day⁻¹ (효소 자연 분해 속도상수) → 효소 자연 $t_{1/2} \approx \ln 2/k_E \approx 3$ days [R&T p.558]
- $C_{u,I}/K_I \approx 0.025$ (clarithromycin 임상 노출, $C_u \approx 0.175$ mg/L) [R&T p.556]
- **$k_{inact}/k_E$ 비율 ≈ 438** → 효소가 자연 turnover로 회복하는 속도보다 불활성화가 약 438배 빠름 [R&T p.558].

이제 충격적인 부분임. 같은 $C_{u,I}/K_I = 0.025$에서:

- **가역적 억제 식**으로 평가하면 CL 감소는 **1.025배** ($1 + 0.025$).
- **MBI 식 (Eq.17-13/14)** 으로 평가하면 약 **11배** ($1 + 438 \times 0.025 = 11.95$).

**같은 inhibitor 노출인데 두 기전의 결과가 한 자릿수 단위로 갈림** [R&T p.558]. 이게 reversible와 MBI를 같은 식으로 처리하면 안 되는 이유의 정량 anchor임.

CYP3A4 활성 회복은 inhibitor 중단 후 효소 재합성에 묶여서 **2주 또는 그 이상** 필요 ($3.3 \times t_{1/2}^{enzyme} \approx 3.3 \times 3 = 10$일 이상) [R&T p.558]. → 임상에서 "inhibitor 중단했으니 안전하다"는 timing 가정은 위험함. → MBI는 **"약물이 빠진 시점이 아니라 효소가 회복된 시점이 안전 기준이다"**라는 사실의 정량 앵커임.

수학적으로 정리하면 한 줄임 — **가역적 억제는 분모에 경쟁자를 더하는 문제**, **MBI는 효소 풀 자체를 줄인 뒤 회복 시계까지 계산하는 문제** [R&T p.558].

#### 임상 데이터에서 보이는 세 가지 패턴

이 셋만 잡으면 시간 의존성 진단의 8할이 끝남:

**① "Trough Envelope Drift"** — 반복투여 trough가 한 방향으로 슬슬 움직임. IIV(개인 간 변동)로 설명하려 들지 말고 **time-varying CL을 먼저 의심**. autoinduction이면 trough가 점차 낮아지고, MBI나 자기억제에서는 점차 높아짐 [G&W pp.126–129], [G&W pp.580–585].

**② "Single-dose Fit Trap"** — 단일 용량만 잘 맞는 모델이 반복투여에서 체계적 over/underprediction. autoinduction 또는 time-dependent inhibition 의심. PK22 design의 핵심 — **single-dose data만으로는 효소 compartment가 식별 안 됨** [G&W pp.580–585], [R&T pp.516–519].

**③ "Washout Trap"** — MBI에서 perpetrator 중단 후 substrate exposure가 즉시 정상화된다고 가정하는 실수. 회복은 enzyme clock($2$–$3\,t_{1/2}^{enzyme}$)에 묶임. Clarithromycin MBI에서 회복 2주가 그 예 [R&T pp.557–558].

🔑 **실무 규칙:** 자가유도 연구에서 **dense single-dose sampling만 늘리는 건 $k_{out}$ 식별에 충분하지 않을 수 있음.** multiple-dose trough envelope가 enzyme clock을 훨씬 더 직접적으로 보여줌 [G&W pp.580–585].

**Card 3 요약:** Card 3의 핵심 질문은 "약물 농도가 낮아졌나?"가 아니라 **"enzyme pool이 회복됐나?"** 임. 이 질문 하나가 induction, autoinduction, MBI, withdrawal trap을 한 줄로 묶음.

§1.2의 30초 시그널 중 **#2번(반복투여 trough 한 방향 이동)과 #6번(single-dose vs multi-dose 체계적 차이)** 이 Card 3 판정 신호. 둘 다 yes면 enzyme clock을 drug concentration clock과 분리해서 식별해야 함.

---

<!-- SLIDE_START: Card 4 | title: 결합 분모 K_d + C_u - total은 거짓말, unbound가 진실 -->

### Card 4. ③ 결합 분모 — total 농도는 거짓말, **unbound가 진실**임

> **앞 카드와의 연결**  
> Card 3가 시간에 따른 처리능 변화였다면, Card 4는 **total 농도가 실제 활성 농도를 가리는 관측 경계 문제**로 넘어감.

> **거장의 시각**  
> total concentration을 그대로 노출로 읽으면 protein binding displacement와 실제 unbound exposure 변화를 혼동함. **open system mass balance를 먼저 놓으면** displacement-only DDI가 왜 지속적인 unbound exposure 증가가 아닌지 설명됨. 이게 valproate-phenytoin 사례를 "용량 줄여야 한다"로 오해하지 않게 만드는 핵심임.

**핵심:** 비선형 결합은 total과 unbound의 관계를 비선형화함. total만 보고 노출이나 효과를 판단하기 어렵게 만듦. 특히 **열린 생체 계와 닫힌 시험관 결합 실험을 혼동하면** 단백 결합 치환을 실제 비결합 노출 변화로 과대해석함 [G&W pp.129–134], [R&T pp.538–544].

#### 물질수지가 강제하는 사실 한 줄

열린 계 정상상태에서는 mass balance가 외부 경계조건을 강제함:

$$
\underbrace{C_u}_{\text{Css,u}}
=
\frac{\underbrace{K^0}_{\text{비결합 입력}}}{\underbrace{CL_u}_{\text{비결합 CL}}}
$$

여기서 $K^0$는 unbound input rate, $CL_u$는 unbound clearance임. **단백 결합이 어떻게 변하든 정상상태 $C_u$는 이 비율에 묶임.** total concentration은 free fraction 변화에 맞춰 알아서 조정됨. 이게 바로 **"열린 계에서 displacement-only는 unbound steady state를 지속적으로 바꾸지 못한다"**는 결론의 수학적 출처임 [G&W §2.7.5, Eq.2:303].

#### 결합 분모 자체

$$
\underbrace{C_b}_{\text{결합 C}}
=
\frac{\underbrace{n}_{\text{자리 수}}\cdot\underbrace{P_t}_{\text{총 결합자리}}\cdot\underbrace{C_u}_{\text{자유 C}}}{\underbrace{K_d}_{\text{Kd}}+\underbrace{C_u}_{\text{포화구동 C}}}
$$

[G&W Eq.2:294; source tag: G&W p.129]

이 분모 $K_d + C_u$가 Card 2의 $K_m + C$와 **완전히 같은 골격**임. 분자에 결합 자리 상한($nP_t$), 분모에 affinity($K_d$) + 노출($C_u$). 같은 mass action, 다른 맥락.

| 파라미터 | 의미 |
|---|---|
| $C_b$ | 결합된 약물 농도 |
| $n$ | 결합 자리 수 |
| $P_t$ | 총 결합자리 농도 (albumin, AAG, 표적 등) |
| $C_u$ | 비결합 약물 농도 |
| $K_d$ | 결합 친화도 scale |

💡 **강의실 좌석 비유:** 좌석 수가 정해진 강의실에 학생들이 몰림. 빈 좌석이 많을 땐 대부분 앉지만 좌석이 차면 추가 학생은 서 있어야 함 → unbound fraction 증가. 좌석 = 결합 자리, 앉은 학생 = 결합 약물, 선 학생 = unbound 약물.

#### 열린 계 vs 닫힌 계 — 이게 분기점

- **닫힌 시험관 계:** 총량 고정. 치환이 곧 비결합 분율 증가처럼 보임 [G&W pp.131–132].
- **열린 생체 계:** 유입·청소율·분포가 같이 작동. 총 농도 변화가 곧 약리학적 효과 변화가 아님 [G&W pp.132–134].

핵심 차이 한 줄 — **"시험관 안의 총량 고정" vs "몸 안의 지속적 제거·재분포".**

#### 포화성 결합 — 정량 앵커들 [R&T pp.511–516]

- **Naproxen** (NSAID): 0–4 g 경구 dose 범위에서 AUC 비선형. albumin 결합 포화로 dose↑와 함께 $f_u$가 올라가서 unbound AUC가 total AUC보다 더 가파르게 올라감 [R&T Fig.16-17].
- **Cefonicid** (cephalosporin 항생제): 30 mg/kg i.v. saturable albumin binding prototype [R&T Fig.16-18].
- **Disopyramide** (항부정맥제): α₁-acid glycoprotein(AAG) 결합 비선형성. total $CL_R$과 unbound $CL_R$이 반대 방향 신호를 줄 수 있음 [R&T Fig.16-16].
- **Trandolaprilat** (ACE 억제제): ACE 결합 자체가 nonlinear. $f_u$가 0.05→0.20 영역으로 dose에 따라 변함 [R&T p.514].
- **Bosentan** (endothelin 수용체 길항제, TMDD prototype): dose 증량 시 $V_{ss}$가 **0.67 → 0.16 L/kg로 감소**. high-affinity, low-capacity 수용체 결합 포화로 organ에 잠긴 약물 비율이 줄어들기 때문임. → **저분자 약물에서도 TMDD 거동이 나타난다**는 사실의 임상 앵커 [R&T Fig.16-20, p.515].
- **Dicloxacillin** (penicillin 항생제): $f_u \approx 0.04$, 1 g dose에서 $CL_R \approx 104$ mL/min, 2 g dose에서 $CL_R \approx 63$ mL/min — saturable renal secretion [R&T Fig.16-13, p.508].

#### Salicylic acid — 반대 방향 비선형성 두 개가 동시에 [R&T Figs.16-27~16-29, pp.520–522]

이게 진짜 흥미로운 케이스임. 같은 약물에서 **두 비선형성이 반대 방향으로 동시 작동**함:

- **단백 결합 포화** → $f_u$ ↑ (방향: unbound 노출 ↑)
- **대사 capacity 포화** → unbound CL ↓ (방향: unbound 노출 ↑↑)

그래서 total $C_{ss}$ vs dosing rate 곡선의 모양이 **단일 기전으로는 설명이 안 됨**. → salicylic acid는 **"비선형 PK 진단은 후보 기전을 최소 셋 이상 동시에 손에 쥐고 진행해야 한다"**는 사실의 결정적 임상 앵커임.

#### 포화성 수송 — 같은 분모, 반대 방향 [R&T p.495]

$$
\underbrace{Rate}_{\text{수송속도}}
=
\frac{\overbrace{T_m}^{\text{Tm 상한}}\cdot\underbrace{C_u}_{\text{자유 C}}}{\underbrace{K_T}_{\text{KT}}+\underbrace{C_u}_{\text{점유 C}}}
\quad\text{(Eq.16-3)}
$$

renal secretion(분비)과 reabsorption(재흡수)은 **같은 분모를 공유하지만 방향이 반대**라서 임상 결과가 정반대로 나타남. **Dicloxacillin은 saturable secretion이라 고용량에서 $CL_R$ ↓.** **Ascorbic acid는 saturable reabsorption escape valve라서 고용량에서 $CL_R$ ↑.** 같은 분모, 반대 방향.

#### TMDD와 표적/조직 결합

표적 매개 약물 disposition(TMDD)은 **고친화성·저용량 표적/조직 결합**이 disposition을 바꾸는 경우임. R&T Ch.16은 저분자에서도 bosentan, imirestat, trandolaprilat, draflazine, mitoxantrone 같은 prototype을 제시함.

본 단계에서는 TMDD full mechanistic code나 Mager–Jusko implementation으로 정량 확장하지는 않음. 다만 **근사 위계 한 줄만 짚어둠** — full Mager–Jusko ODE를 그대로 적합하면 $k_{on}/k_{off}$ binding rate 식별이 어렵고 sparse data에서 수렴이 무너짐. 그래서 실무에서는 단순화 가정을 차례로 적용함:

$$
\underbrace{\text{Full TMDD}}_{\text{Mager–Jusko ODE}}
\xrightarrow{\overbrace{k_{on},k_{off}\gg k_{el}}^{\text{빠른 결합·해리}}}
\underbrace{\text{QE 근사}}_{\text{Quasi-Equilibrium}}
\xrightarrow{\overbrace{k_{int}\text{만 살림}}^{\text{complex 정상상태}}}
\underbrace{\text{QSS 근사}}_{\text{Quasi-Steady-State}}
$$

- **QE (Quasi-Equilibrium):** binding-unbinding이 elimination보다 훨씬 빠르다고 가정. free·bound·complex가 순간 평형. 수용체 affinity 매우 높을 때 적용. 식별 가능 파라미터는 $K_D = k_{off}/k_{on}$ 한 덩어리로 축소됨.
- **QSS (Quasi-Steady-State):** complex 형성·소실이 정상상태에 있다고 가정. QE보다 약한 가정이라 **target turnover와 internalization clock($k_{int}$)이 살아 있음**. $K_{SS} = (k_{off}+k_{int})/k_{on}$이 식별 단위.

본 session에서는 두 근사의 **식별성 구조 차이만** 인지하고 정량 implementation은 후속 모델링 세션으로 이관. bosentan $V_{ss}$ 0.67 → 0.16 L/kg dose↑ 감소가 이 framework의 임상 신호.

#### 약물-대사체 비선형 모델 — §2.7.6

활성 대사체가 효과나 독성에 기여하는 약물(carbamazepine-10,11-epoxide, irinotecan-SN38, codeine-morphine 영역)에서, 모약물과 대사체가 **같은 MM 효소를 공유**하면 disposition이 비선형으로 결합됨 [G&W pp.135–139].

**모델 구조:** 2-compartment drug + 1-compartment metabolite + MM elimination. ODE는 Eq.2:304–2:308, 파라미터는 Tables 2.18–2.20. 여기서 대사체 농도 프로파일에 **prolonged tail**이 나타날 수 있는데, **이게 함정임:**

- 대사체 자체의 분포 kinetics 때문일 수도 있음 (i)
- 모약물의 MM elimination이 대사체 형성 속도를 제한해서 생기는 모습일 수도 있음 (ii)

**둘은 parent–metabolite 동시 관측만으로는 식별이 안 됨.** G&W p.137이 명시한 출처 기반 경고 — "parent–metabolite 동시 관측만으로 metabolite disposition kinetics를 **추론적으로 외삽하면 안 됨**. 대사체 단독 투여 disposition 데이터가 없으면 대사체 청소율·분포·$t_{1/2}$가 식별되지 않을 수 있음" [G&W p.137].

→ 임상적으로 활성 대사체의 toxicity/efficacy 기여가 큰 약물에서는 **대사체 단독 투여 disposition study가 식별성 보강 단계로 필요**할 수 있음.

#### Displacement-only DDI — 격하해서 봐야 함

**Phenytoin–Valproate** (항경련제 × 항경련제, displacement-only prototype): total phenytoin이 낮아져도 unbound phenytoin은 상대적으로 유지됨. 이 사례의 진짜 가치는 "용량을 줄여라"가 아니라 **"total만 보고 toxicity/efficacy를 판단하지 마라"** 임. → valproate-phenytoin은 **"열린 계에서는 displacement가 일시적 total 변화로 끝난다"**는 사실의 임상 prototype [R&T p.543].

**Warfarin–Phenylbutazone** (항응고제 × NSAID): 이건 단순 displacement만이 아니라 **inhibition까지 겹친 multifaceted example**. displacement 단독으로 다루면 안 됨 [R&T p.563].

🔑 **실무 규칙:** 단백 결합 비선형성 의심되는 Phase 1/PopPK package에서는 **total만 모으지 말고 용량 수준별 $f_u$를 측정.** total-only dataset은 binding nonlinearity와 clearance nonlinearity를 구분하기 어렵게 만듦 [G&W pp.129–134], [R&T pp.511–516].

**Card 4 요약:** "protein binding이 변하면 위험하다"가 아님. **total과 unbound는 서로 다른 질문에 답한다**는 원칙임.

§1.2 시그널 #3번(total $CL_R$은 그대로인데 unbound $CL_R$이 변함)이 Card 4 판정. Yes면 nonlinear plasma protein binding (metabolic induction 아님) 의심하고 용량 수준별 $f_u$를 직접 측정해서 검증.

---

<!-- SLIDE_START: Card 5 | title: DDI 분모 - inhibitor가 분모에 끼어들 때 -->

### Card 5. ④ DDI 분모 — inhibitor가 분모에 끼어들 때, 그리고 **세 식이 사실 하나**라는 사실

> **앞 카드와의 연결**  
> Card 4에서 unbound와 system boundary를 분리했음. Card 5에서는 그 논리를 **억제 경로 비율과 DDI AUC ratio 계산**으로 확장함.

> **거장의 시각**  
> DDI를 inhibitor 이름(ketoconazole이 강하다, rifampin이 유도제다)으로 분류하면 victim drug의 pathway dependence를 놓침. **$f_m$과 $C_{u,I}/K_I$를 분모에 넣어** 보면 같은 inhibitor라도 victim에 따라 AUC ratio가 왜 완전히 달라지는지 한눈에 보임.

**핵심:** Ch.17의 DDI 정량 framework는 "상호작용이 있다/없다"를 묻지 않음. **피영향 약물의 청소율 중 얼마가 억제된 경로에 의존하는지($f_m$), 억제제 노출이 $K_I$ 대비 얼마나 큰지, 투여 경로와 초회통과가 얼마나 관여하는지** — 이걸 묻는 것임 [R&T pp.531–532], [R&T pp.546–552].

#### 이 세션의 수학적 정점 — 세 식이 같은 골격임

이 챕터 전체에서 가장 강력한 통합이 바로 여기임. **세 식이 사실 같은 분모 구조의 다른 표현**이라는 점 — 이거 하나 잡으면 외울 식이 사실 셋이 아니라 하나임:

$$
\overbrace{CL=\frac{V_{max}}{K_m+C}}^{\text{Card 2: 농도-CL capacity}}
\;\;\Longleftrightarrow\;\;
\overbrace{C_{u,ss}=\frac{K_m R_0}{V_m-R_0}}^{\text{Card 2: Css 분모 발산}}
\;\;\Longleftrightarrow\;\;
\overbrace{\text{AUC ratio}\approx\frac{1}{\frac{f_m}{1+C_{u,I}/K_I}+(1-f_m)}}^{\text{Card 5: DDI 경로몫}}
$$

세 식 모두 **기질-효소 가역 결합의 질량 작용(QSSA)이 만든 같은 골격**을 다른 변수로 표현한 것임:

- **Eq.2:266** = 농도-CL의 질량 작용 직접 표현
- **Eq.16-7** = 그것의 정상상태 분모 발산 형태
- **Eq.17-11** = 억제제가 분모에 추가됐을 때의 노출 비율 형태

→ 세 식을 한 줄로 보면 **비선형 PK와 DDI 직관 전부가 동일한 mass action 분모로 회수됨** [G&W pp.115–118], [R&T p.503], [R&T pp.550–552].

#### 가역적 경쟁 억제 — AUC ratio의 핵심 골격

Eq.17-9~17-12가 **억제된 경로의 청소율 감소와 전신 AUC ratio를 연결**함. 한 경로 억제가 전체 노출을 얼마나 바꾸는지 계산하는 핵심 골격임 [R&T pp.550–552].

$$
\underbrace{\text{AUC ratio}}_{\text{병용 노출비}}
\approx
\frac{1}{
\underbrace{\frac{f_m}{1+C_{u,I}/K_I}}_{\text{억제경로 잔여몫}}
+
\underbrace{(1-f_m)}_{\text{우회경로 몫}}
}
$$

이 식의 직관을 잡자. **분모는 두 조각으로 쪼개짐:**
- **억제경로 잔여몫** $f_m/(1+C_{u,I}/K_I)$ — 원래 $f_m$이 inhibitor에 의해 $(1+C_{u,I}/K_I)$로 나뉘어 작아짐. 강한 억제일수록 0에 수렴.
- **우회경로 몫** $(1-f_m)$ — 억제와 무관한 다른 경로. 이게 AUC ratio의 **바닥**을 결정.

핵심 통찰: **$f_m$이 크면 우회경로가 작아서 강한 inhibitor 효과가 그대로 노출됨.** $f_m$이 작으면 우회경로가 커서 강한 inhibitor도 효과가 제한됨. → 그래서 같은 inhibitor라도 victim에 따라 AUC ratio가 완전히 다름.

#### 임상 앵커 — 정량 사례 4개

**① Theophylline–Enoxacin** (theophylline = bronchodilator/CYP1A2 substrate, enoxacin = fluoroquinolone/CYP1A2 inhibitor) [R&T pp.546–550, Fig.17-6, Fig.17-7]

- $t_{1/2}$ 8.8 h → 22 h (**2.5배 연장**)
- 평균 투여간격 $C_{ss}$ 4 mg/L → 9 mg/L (**약 2.25배**)
- $CL_{inhib}/CL_{normal} = 0.44$
- $f_m \approx 0.67$ (CYP1A2 의존성)
- Eq.17-9~17-12의 **단계적 억제** 주요 임상 예시. 같은 fluoroquinolone 계열에서 enoxacin 용량이 낮아지면 억제가 단계적으로 약해지고, 계열 비교(ciprofloxacin > enoxacin > norfloxacin)에서도 직접 보임.
- → **"$f_m$이 중간값(~0.67)이면 single-pathway 억제가 전신 노출을 2배 영역에서 흔든다"**는 정량 anchor.

**② Desipramine–Quinidine** (CYP2D6; desipramine = TCA, quinidine = CYP2D6/P-gp inhibitor) [R&T pp.549–550]

- $f_m^{CYP2D6} \approx 0.75$
- CL이 약 **4배 감소**
- → **"$f_m$이 높을 때(~0.75) 한 경로의 억제가 전신 CL을 거의 같은 비율로 떨어뜨린다"**는 정량 사례.

**③ Desipramine–Fluoxetine** (fluoxetine = SSRI/CYP2D6 inhibitor, 긴 $t_{1/2}$) [R&T p.552, Table 17-11]

- AUC: 284 → 2110 µg·hr/L (**약 7.4배**)
- $t_{1/2}$: 16.1 h → 63.8 h (약 4배)
- CL/F: 289 → 27.1 L/hr (약 10.7배 감소)
- 같은 desipramine victim인데 **fluoxetine은 quinidine보다 더 강한 효과**를 만듦. 이유: fluoxetine 자체의 긴 $t_{1/2}$와 활성 대사체 norfluoxetine까지 더해진 결과.
- → **"perpetrator의 $t_{1/2}$와 활성 대사체가 같은 victim에서 더 큰 AUC ratio를 만들 수 있다"**는 사실의 정량 사례.

**④ Diltiazem–Lovastatin** (diltiazem = CCB/CYP3A4 inhibitor, lovastatin = statin/CYP3A4 substrate) [R&T p.553, Table 17-7]

- AUC ratio: **1.27 (i.v.) vs 3.57 (oral)** → 경구 상호작용이 IV보다 **약 3배** 큼.
- → 이게 결정적임. **장벽/초회통과 component가 크다는 직접 증거**. 간 청소율 억제만으로는 경구·IV 차이를 절대 설명할 수 없음.
- → **"oral interaction > IV interaction이면 gut wall/first-pass가 우세하다"**는 사실의 정량 anchor.

**⑤ Fluconazole–Midazolam** (fluconazole = azole 항진균제/CYP3A4 inhibitor, midazolam = BZD/CYP3A4 substrate) [R&T p.554, Fig.17-10]

- 경구 AUC: ↑**5.6배**
- IV AUC: ↑**2배**
- F: 24% → 63%
- $F_H$: 0.42 → 0.72 ($F_H$ = 간 생체이용률)
- $F_G$: 0.57 → 0.88 ($F_G$ = 장벽 생체이용률)
- **$F_G$가 $F_H$보다 더 큰 비율로 변함** → midazolam의 경구 초회통과가 장에 상당 부분 위치한다는 뜻.
- → diltiazem-lovastatin과 짝을 이루는 **"gut wall metabolism이 oral DDI를 키운다"**는 두 번째 정량 anchor.

#### 억제제 분류 — Table 17-5 어휘 [R&T p.549]

| 분류 | 기준 (기질 AUC 배수 증가) | 추가 표시 |
|---|---|---|
| 강함(Strong) | ≥5배 또는 >80% CL 감소 | MBI는 별도 (b) 표시 |
| 중등도(Moderate) | 2–5배 | — |
| 약함(Weak) | 1.25–2배 | — |

**기질 민감도 분류 (Table 17-6):** 강한 억제제와 병용 시 **≥4배 AUC 증가**를 보이는 기질이 별도 분류됨. 본문은 textbook reference의 실무 어휘로만 다룸. 다른 규제문서의 분류 체계와 직접 동일시하지 않음.

#### PM × 억제제 — 분모가 발산하는 위험

Eq.17-18은 다형성 경로와 비다형성 잔여 경로가 동시에 고려될 때 **최대 노출 비율이 폭증할 수 있음**을 보여줌. PM 환자에서 남은 비다형성 경로까지 강한 억제제가 막으면 노출 비율이 크게 튐.

$$
\underbrace{\text{Maximum exposure ratio}}_{\text{최대 노출비}}
=
\frac{1}{
\underbrace{1-f_m^{POLY}-f_m^{NP}}_{\text{잔여 CL}}
}
$$

[R&T Eq.17-18; source tag: R&T pp.558–559]

💡 **두 배수구 비유:** 두 배수구 중 하나가 원래 막힌 상태(PM)에서, 남은 배수구까지 막으면 물이 갑자기 차오름. 분모의 잔여 CL 여유가 작을수록 노출 ratio는 폭발적으로 커짐. $f_m^{POLY} + f_m^{NP}$가 1에 가까워지면 분모가 0에 가까워지고 ratio가 발산. → Card 2의 $V_m - R_0 \to 0$ 발산과 **수학적으로 같은 모양**임. **분모가 0으로 가면 농도가 솟구친다는 mass action 골격이 또 한 번 재현됨.**

Fig.17-15의 omeprazole–clarithromycin 사례는 high ratio 사례로 유지함. 다만 특정 배수값은 exact printed number가 아니라 시각 추정/확인이 필요하므로 본문에서는 "매우 큰 exposure ratio 사례"로만 사용 [R&T p.559].

#### 투여 순서와 중단 — 대칭이 아님

🔑 **DDI 판독 규칙:** inhibitor 추가와 제거는 **대칭 사건이 아님.** MBI와 induction에서는 회복 시계가 별도로 남음. 상호작용은 all-or-none이 아니라 농도·시점·순서·시작/중단에 따라 단계적으로 나타남. 그래서 inhibitor를 추가할 때와 제거할 때의 위험이 대칭이 아니고, **induction/MBI에서는 특히 회복 지연이 치명적**임 [R&T pp.532–534], [R&T pp.557–561].

🔑 **실무 규칙:** DDI 예측표에는 최소한 **$f_m$ uncertainty band**를 붙일 것. $f_m$가 0.5인지 0.8인지에 따라 같은 inhibitor라도 AUC ratio 해석이 완전히 달라짐 [R&T pp.550–552].

**Card 5 요약:** 핵심은 억제제 이름이 아니라 **피영향 약물의 pathway dependence**임. $C_{u,I}/K_I$가 커도 $f_m$이 작으면 whole-body AUC ratio는 제한되고, $f_m$이 크면 작은 inhibitor effect도 임상적으로 커짐.

§1.2 시그널 #4번(oral interaction > IV interaction)이 Card 5 핵심 판정. Yes면 gut wall/first-pass metabolism component 우세 — hepatic CL inhibition만으로 설명하지 말 것. **Diltiazem-Lovastatin(1.27 IV vs 3.57 oral)과 Fluconazole-Midazolam($F_G$ 0.57→0.88)** 이 직접 anchor.

---

<!-- SLIDE_START: Card 6 | title: 복합/수송체/PD - 한 perpetrator가 여러 분모를 동시에 흔들 때 -->

### Card 6. ⑤ 복합 분모 — 한 perpetrator가 여러 분모를 동시에 흔들 때, 그리고 PD까지

> **앞 카드와의 연결**  
> Card 5가 한 억제 경로의 정량화였다면, Card 6는 **실제 임상 DDI처럼 여러 기전이 동시에 움직이는** 경우를 판독함.

> **거장의 시각**  
> AUC 하나만 보면 transporter도, distribution도, induction도, PD interaction도 전부 metabolic inhibition처럼 보임. **$C_{max}$, $t_{1/2}$, V/F, route, timing을 한 표에 놓아야** 복합 DDI의 방향성이 분리됨. 그래야 atorvastatin-rifampin 같은 transporter signature를 metabolic inhibition으로 잘못 부르지 않게 됨.

**핵심:** 실제 DDI는 **대사 억제 하나로 끝나지 않음.** 수송체 억제, 분포 변화, 장벽/간 초회통과, 유도, PD 가산성/상승작용/길항이 다 겹칠 수 있음. 그래서 같은 drug라도 **급성/만성, 경구/정맥 조건에서 반대 방향 효과**가 나옴 [R&T pp.563–567].

#### 복합 기전 — 정량 사례 6개

**① Digoxin–Quinidine** (digoxin = 강심배당체/P-gp substrate, quinidine = 항부정맥제/P-gp inhibitor) [R&T p.564, Table 17-8]

- CL: 140 → 72 mL/min (**약 절반**)
- $CL_R$: 101 → 51 mL/min (P-gp 억제로 renal secretion 감소)
- $V_d$: 500 → 240 L (P-gp 억제로 tissue 분포 감소)
- F: 0.75 → 0.85 (intestinal P-gp 억제로 absorption 증가)

→ 정말 흥미로움. **quinidine은 digoxin의 CL, $V_d$, F 셋을 동시에 변화시킴.** 단일 대사 기전만으로는 이 패턴 설명 불가. → digoxin-quinidine은 **"하나의 perpetrator가 한 victim의 CL·V·F를 동시에 흔드는 P-gp 통합 효과"**의 임상 prototype.

**② Atorvastatin–Rifampin acute IV** (atorvastatin = statin/OATP1B1·CYP3A4 substrate, rifampin = 항결핵제) [R&T p.565, Fig.17-19]

- $C_{max}$ ↑**10배**
- AUC ↑**7배**
- $t_{1/2}$: 8 h → 3 h (**감소** — 단순 metabolic inhibition과 반대 방향)

기전: **급성** rifampin이 OATP1B1(간 uptake transporter)을 억제해서 atorvastatin의 간 분포를 차단. → 혈중 누적으로 $C_{max}$/AUC ↑, distribution-limited terminal phase가 사라져서 $t_{1/2}$ ↓.

**활성 대사체 보강:** atorvastatin은 R&T p.565가 "extensively metabolized with little eliminated unchanged; **some of the metabolites are active**"라고 명시한 것처럼, 활성 대사체(2-hydroxy atorvastatin, 4-hydroxy atorvastatin)도 HMG-CoA reductase 억제에 기여함. 따라서 parent AUC ratio 7배는 **PK 시계의 변화**이고, 임상 PD 효과(cholesterol response)는 parent + 활성 대사체의 합산 노출과 cholesterol turnover 시간(약 3–4주, R&T p.343, Fig.11-16)에 의해 결정됨. → **PK ratio ≠ PD ratio가 되는 또 하나의 이유**가 atorvastatin-rifampin 케이스에서 한 번 더 확인됨 [R&T pp.343, 564–565].

→ atorvastatin-rifampin acute IV는 **"AUC↑ + $t_{1/2}$↓의 조합은 metabolic inhibition이 아니라 transporter signature다"**라는 사실의 결정적 anchor. 이 두 지표가 같은 방향으로 움직이지 않을 때 의심해야 할 첫 번째 기전.

**③ Rosuvastatin–Cyclosporine** (rosuvastatin = statin/OATP1B1·BCRP substrate, cyclosporine = 면역억제제/OATP·BCRP inhibitor) [R&T p.555, Fig.17-11]

- $C_{max}$ ↑**11배**
- AUC ↑**7배**
- 기전: cyclosporine이 **OATP1B1 + BCRP를 동시에** 억제해서 rosuvastatin의 간 흡수와 담즙 배출을 둘 다 차단.
- → **"한 perpetrator가 두 transporter를 동시에 막을 때 노출 증폭이 배가된다"**는 임상 사례.

**④ Phenobarbital–Dicumarol** [R&T p.561, Fig.17-17]

- Plateau 도달까지 **3–4주**
- 이유: **phenobarbital $t_{1/2} \approx 4$ days가 유도 시작의 rate-limiter**. $4$–$5\,t_{1/2} \approx 16$–$20$일 영역에서 inducer가 정상상태에 도달, 그 이후에 효소량이 새 plateau로 진입.
- → Card 3에서 봤던 master clock 위계의 직접 anchor. **가장 느린 시계(phenobarbital)가 동역학을 지배.**

**⑤ Fluconazole–Midazolam / Diltiazem–Lovastatin:** oral vs IV 차이가 gut wall/first-pass contribution을 분리하는 단서. Card 5에서 정량값을 다뤘으니 여기서는 기전 어휘로만 회수 [R&T pp.553–554].

**⑥ Renal transporter DDI — hepatic transporter DDI의 거울 면** [R&T Table 17-3, p.535]

지금까지 Card 6의 anchor는 모두 **hepatic transporter**(OATP1B1·P-gp·BCRP)였음. 하지만 같은 mass action 골격이 **신장 transporter**(OCT2·MATE·OAT)에서도 동일하게 작동함. Tozer Table 17-3의 임상 정량 anchor를 짚어두면 framework이 완결됨:

| Transporter | Inhibitor | Affected drug | 임상 영향 |
|---|---|---|---|
| OCT2 / MATE | **Cimetidine** (H2-blocker) | **Metformin** (당뇨약, OCT2/MATE substrate) | **AUC ↑50%, $CL_R$ ↓27%** |
| OCT2 / MATE | Cimetidine | Pindolol (β-blocker) | $CL_R$ ↓34% |
| OCT2 / MATE | Cimetidine | Varenicline (금연보조제) | AUC ↑29% |
| OAT1 / OAT3 | **Probenecid** (통풍약, 고전적 OAT inhibitor) | **Cidofovir** (항바이러스제) | $CL_R$ ↓32% |
| OAT1 / OAT3 | Probenecid | **Acyclovir** (항바이러스제) | **$CL_R$ ↓32%, AUC ↑40%** |
| OAT1 / OAT3 | Probenecid | Furosemide (이뇨제) | $CL_R$ ↓66% |

[R&T Table 17-3; source tag: R&T p.535]

- **Metformin–Cimetidine:** cimetidine이 **basolateral uptake transporter OCT2 + luminal efflux transporter MATE1을 동시에 억제** → metformin의 신장 능동 분비 차단 → $CL_R$ ↓·AUC ↑. metformin은 **간 대사가 거의 없는 약물**이라(R&T Table 5-2에서 renal extraction high 영역) renal transporter DDI가 **유일한 노출 변동 기전**이 됨. Card 4의 dicloxacillin saturable secretion(saturable, dose-dependent)과 짝을 이루는 **DDI 버전**의 신장 분비 차단.
- **Probenecid–Penicillin/Acyclovir/Cidofovir:** 가장 오래된 OAT 억제 prototype. probenecid는 historically penicillin 노출 지속을 위해 **의도적으로 병용**된 사례라, "DDI = 항상 나쁜 것"이 아니라는 사실의 임상 reference이기도 함. R&T Fig.17-12의 **Imipenem–Cilastatin** 사례(cilastatin이 신장 dehydropeptidase를 억제해서 imipenem 요중 회수율을 ~25% → ~70%로 증가)도 같은 "유익한 transporter/효소 억제"의 prototype [R&T pp.555–556, Fig.17-12].

$$
\underbrace{\text{AUC ratio}_{\text{renal}}}_{\text{신장 DDI}}
\approx
\frac{1}{
\underbrace{\dfrac{f_e}{1+C_{u,I}/K_I}}_{\text{억제된 신분비 잔여}}
+
\underbrace{(1-f_e)}_{\text{우회 경로(간/기타)}}
}
$$

→ Card 5의 hepatic AUC ratio 식과 **분모 골격이 동일.** 다만 $f_m$ 자리에 $f_e$ (renal active secretion 분율)가 들어갈 뿐. → renal transporter DDI는 **"mass action 분모는 간이든 신장이든, 대사효소든 transporter든 한 골격"**이라는 사실의 임상 확장. **Cisplatin nephrotoxicity와 OCT2/MATE 매개 신독성**도 같은 framework에서 해석됨 [R&T pp.546–566, Ch.17 renal interaction].

**임상적 차이 한 줄:** hepatic OATP DDI(atorvastatin-rifampin acute)는 간 uptake 차단으로 $t_{1/2}$가 단축되지만, 신장 transporter DDI는 **소실 경로 차단으로 $t_{1/2}$ 연장 + AUC 증가**가 동시에 나타나는 게 시그너처 차이임.

#### 급성/만성 × 경구/정맥 진단 매트릭스

**Rifampin** 같은 perpetrator는 **급성 수송체 억제와 만성 효소 유도가 정반대 방향** 효과를 만들 수 있음. 실무에서는 acute IV, acute oral, chronic IV, chronic oral을 구분해서 기전을 생각해야 함 [R&T pp.560–565]:

| 조건 | 우세 기전 | 예 |
|---|---|---|
| 급성 정맥(Acute IV) | Transporter inhibition (예: OATP1B1) | Atorvastatin–rifampin acute |
| 급성 경구(Acute oral) | 수송체 + 장벽/초회통과 | Rosuvastatin–cyclosporine |
| 만성 정맥(Chronic IV) | Enzyme induction onset | Carbamazepine 자가유도 |
| 만성 경구(Chronic oral) | 효소 유도 × 초회통과 × 수송체 복합 | Long-term rifampin/rifabutin |

#### PD 상호작용 — 같은 분모 골격이 효과 차원에서 [G&W pp.224–227]

PD interaction도 결국 같은 mass action 분모임. 작용제 농도 $C$와 길항제 $A$가 수용체 자리에서 경쟁하는 모양이 Card 5의 효소 자리 경쟁과 수학적으로 동일함.

**다중 결합 부위 모델 (Eq.3:48):** 한 리간드가 여러 결합 부위에 협동적으로 결합할 때의 반응 곡선. Hill 형태 fitting의 기전적 출처 [G&W p.224].

**경쟁적 길항 (Eq.3:49):**

$$
\underbrace{E}_{\text{효과}}
=
\frac{\overbrace{E_{max}}^{\text{Emax 보존}}\cdot\underbrace{C}_{\text{작용제 C}}}{
\underbrace{C}_{\text{작용제 C}}+
\underbrace{EC_{50}}_{\text{기본 EC50}}
\cdot
\overbrace{(1+A/EA_{50})}^{\text{경쟁}}
}
$$

→ 길항제 $A$가 들어오면 $EC_{50}$이 $(1+A/EA_{50})$ factor만큼 **오른쪽으로 이동**하지만 $E_{max}$는 보존됨. **더 높은 농도를 쓰면 같은 효과를 회복 가능**. 질량 작용 등가성의 분모 구조와 동일 — **Card 5의 mass action 분모가 PD에서도 그대로 나타나는 셈**임.

**비경쟁적 길항 (Eq.3:50):**

$$
\underbrace{E}_{\text{효과}}
=
\frac{\overbrace{E_{max}}^{\text{기존 Emax}}}{\underbrace{(1+A/EA_{50})}_{\text{Emax 감소}}}
\cdot
\frac{\underbrace{C}_{\text{작용제 C}}}{\underbrace{C+EC_{50}}_{\text{potency}}}
$$

→ $E_{max}$가 $(1+A/EA_{50})$로 **감소**, $EC_{50}$은 단순 비경쟁 모델에서는 보존. 효현제 농도 무한정 올려도 원래 $E_{max}$ 회복 불가 — **이게 비경쟁적 길항이 임상적으로 다른 결과를 만드는 이유**.

**경쟁 vs 비경쟁 한 줄 요약:**

$$
\overbrace{E=\frac{E_{max}\cdot C}{C+EC_{50}\cdot(1+A/EA_{50})}}^{\text{경쟁: EC50↑, Emax 보존}}
\qquad\text{vs}\qquad
\overbrace{E=\frac{E_{max}}{1+A/EA_{50}}\cdot\frac{C}{C+EC_{50}}}^{\text{비경쟁: Emax↓}}
$$

**경험적 두 약물 모델 (Eq.3:51, Table 3.2):** 두 효과가 작용 부위도 기전도 다를 때의 일반화된 합산/곱셈 framework [G&W p.226].

**거울이성질체 상호작용 (Eq.3:52–3:53):** 같은 receptor의 R/S enantiomer가 서로 다른 affinity를 가질 때. ketamine R-/S- enantiomer 농도-효과 관계가 직접 예시 [G&W p.227].

**동일 수용체 완전 효현제 조합 — Emax 천장 효과** [R&T pp.567–570]

두 완전 효현제가 같은 receptor에 작용하면 **$E_{max}$는 단일 agonist 단독 사용과 같은 ceiling**에 도달. 두 약물의 "더하기"가 효과를 두 배로 만들지는 않음:

$$
\underbrace{E}_{\text{공유효과}}
=
\frac{
\overbrace{E_{max}}^{\text{공유 Emax}}\cdot
\left(\underbrace{C_A/EC_{50,A}}_{\text{A drive}}+
\underbrace{C_B/EC_{50,B}}_{\text{B drive}}\right)
}{
1+\underbrace{C_A/EC_{50,A}}_{\text{A drive}}+
\underbrace{C_B/EC_{50,B}}_{\text{B drive}}
}
$$

[R&T Eq.17-21; source tag: R&T p.568]

**등효능선(Isobologram, Fig.17-21):** 일정 효과 수준(예: 50% $E_{max}$)을 만드는 두 약물 농도 조합을 $(x, y)$ 평면에 그렸을 때:

- 직선 = 가산적(단순 mass action 합산)
- 직선 아래로 휨 = 상승작용(synergy, 예: midazolam–propofol)
- 직선 위로 휨 = less-than-additive (예: isoproterenol–propranolol antagonism)

**Greco general response surface (Eq.17-22):** 두 약물의 임의 PD interaction을 한 식으로 통합하는 advanced reference. master card로 독립 확장하지 않고 reference로만 둠 [R&T p.569].

🔑 **실무 규칙:** DDI 사례 검토 시 **"AUC가 증가했다"로 끝내지 말 것. 함께 움직인 $C_{max}$, $t_{1/2}$, V/F, oral/IV ratio를 함께 볼 것.** 예: AUC↑와 $t_{1/2}$↓가 같이 나오면 단순 metabolic inhibition만으로는 설명 불가 — distribution/transporter 기전 의심 [R&T pp.563–565].

**Card 6 요약:** 단일 기전 모델의 과신을 막는 카드. 같은 DDI pair라도 **route, timing, chronicity에 따라 완전히 다른 기전 시그니처**가 나옴. **AUC↑ + $t_{1/2}$↓ = transporter signature**가 가장 강력한 단일 판독 규칙.

§1.2 시그널 전체 통합 — **AUC↑와 $t_{1/2}$↓가 같은 case에서 함께 보이는가? 또는 acute IV와 chronic oral 결과가 반대 방향인가?** 둘 중 하나라도 yes면 단일 기전 모델 부적절 — transporter/induction/PD interaction matrix를 모두 손에 쥐고 진단해야 함 (Atorvastatin-Rifampin acute IV signature가 anchor).

---

## §3. 혼동쌍 8개 — 헷갈리는 짝들을 한 줄로 분리

비선형 PK에서 학습자가 가장 자주 헷갈리는 쌍 8개임. 진단 단계에서 이 쌍 중 하나라도 잘못 가르면 카드 전체를 다시 풀어야 함.

### CP1. 용량 의존적 capacity vs 진성 시간 의존 동역학

| 비교 기준 | 농도 구동 (Card 2) | 시간 구동 (Card 3) |
|---|---|---|
| 차원 | dose/concentration에 따른 capacity 변화 | 시간에 따른 효소·수송체·생리 변화 |
| 수식 위치 | $K_m+C$, $V_m-R_0$ | $dE/dt = R_{in} - k_{out}E$ |
| 변화 원인 | 농도 증가, 포화성 대사/수송/재흡수 | 효소 유도, MBI, 회복 지연 |
| 혼동 시 결과 | dose ladder 문제를 time-dep CL로 오해 → 설계·모니터링 실패 | 시간 변화를 단순 dose nonlinearity로 오해 → trough drift 예측 실패 |

> **⚡ 기억 고리 — "농도 때문인가, 시간 때문인가"**  
> MM 동역학에서는 농도가 시간에 따라 줄어드니까 apparent CL도 변하지만, **enzyme 자체는 변하지 않음 — 이건 농도 구동 변화임.** True time-dependent kinetics는 **효소량이나 생리학 자체가 시간에 따라 변하는 것.** 진단 기준: **"같은 농도에서 시간이 달라도 CL이 다른가?"** → Yes면 time-dependent 기전.

### CP2. 자가유도(autoinduction) vs 일반적 반복투여 축적(accumulation)

| 비교 기준 | Autoinduction | 일반 축적 |
|---|---|---|
| 차원 | 반복투여에 따른 효소량 변화 | 선형 PK의 투여간격별 축적 |
| 수식 위치 | $k_{out}$, enzyme pool, time-varying CL | 축적비, 반감기, dosing interval |
| 변화 원인 | autoinduction → CL 증가 | 동일 CL에서 input/output equilibrium |
| 혼동 시 결과 | trough 감소를 adherence 문제로 오해 | 자가유도 모델 필요성을 놓침 |

> **⚡ 기억 고리 — "수위 상승 vs 배수구가 넓어짐"**  
> 일반 축적은 linear 파라미터만으로 예측 가능한 **수위 상승.** Autoinduction은 enzyme이 시간에 따라 새로 합성돼서 처리 능력이 커지는 **배수구 자체가 넓어지는 과정.** 그래서 autoinduction에서 trough는 단순 축적 예측보다 낮고, 정상상태까지의 시간도 enzyme turnover half-life에 묶임. **single-dose fit으로 multiple-dose를 예측하면 trough가 체계적으로 과대추정됨.**

### CP3. 용량 한계 제거(capacity-limited elimination) vs 혈류/초회통과 효과

| 비교 기준 | Intrinsic capacity 제한 | 혈류·초회통과·route effect |
|---|---|---|
| 수식 위치 | $V_{max}/(K_m+C)$, $V_m-R_0$ | $Q_H$, $F_G$, $F_H$, extraction ratio |
| 변화 원인 | 효소/수송체 포화 | 간혈류, gut wall/hepatic first-pass 변화 |
| 혼동 시 결과 | AUC 증가를 F vs CL 중 하나로 성급히 단정 | oral/IV 근거 없이 bioavailability 결론 오류 |

> **⚡ 기억 고리 — "공장 한계 vs 도로 한계"**  
> Capacity-limited elimination은 **공장(효소)의 최대 처리 능력**이 한계 — 원료가 아무리 많아도 기계 처리 한계를 못 넘음. Flow/first-pass effect는 **도로(혈류)의 용량**이 한계 — 공장이 빠르더라도 원료 도착 속도 이상은 처리 못함. 둘 다 AUC/Dose를 증가시키지만 방향이 다름: **공장 한계는 고용량에서 폭발적 비선형성, 도로 한계는 고혈류 상황에서 선형 변화.**

### CP4. 열린 생체 내 결합 vs 닫힌 시험관 내 결합

| 비교 기준 | 열린 생체 계 | 닫힌 시험관 계 |
|---|---|---|
| 차원 | 유입·청소율·분포 작동 | 총량 고정 |
| 수식 위치 | $C_u = K^0/CL_u$ | binding equilibrium 식 |
| 변화 원인 | 간·신장 제거, 재분포, unbound CL | 단백 결합 치환, 고정 총량 |
| 혼동 시 결과 | displacement-only를 지속적 unbound 증가로 과대해석 | 시험관 결과를 생체 용량조정으로 직행 |

> **⚡ 기억 고리 — "열린 계 vs 닫힌 계"**  
> In vitro는 총 약물량 고정 **닫힌 계** → displacement 시 unbound가 지속적으로 높아짐. In vivo는 신장·간이 계속 unbound drug를 제거하는 **열린 계** → displacement 후 새 평형에서 unbound concentration이 제거 속도에 따라 결정됨. **In vitro에서 "강한 displacement"라도 in vivo에서 unbound 변화가 임상적으로 의미 없을 수 있는 이유가 여기 있음.**

### CP5. 치환 단독 DDI(displacement-only) vs 억제 DDI(inhibition)

| 비교 기준 | Displacement-only | Inhibition |
|---|---|---|
| 차원 | 결합 자리 치환 | 대사/수송 경로 억제 |
| 수식 위치 | $f_u$, $C_u$ 해석 | $CL_{int}$, $f_m/(1+C_{u,I}/K_I)$ |
| 변화 원인 | protein binding displacement | enzyme/transporter inhibition |
| 혼동 시 결과 | total 감소만 보고 dose 감량 | 지속 AUC 증가를 displacement로 축소 해석 |

> **⚡ 기억 고리 — "자리 뺏기 vs 공장 멈추기"**  
> Displacement는 결합 자리를 뺏어서 unbound concentration을 **일시적으로** 올리지만, 열린 계에서 새 정상상태로 빠르게 재수렴 — "자리 뺏기"는 일시적 효과. Inhibition DDI는 **$CL_{int}$를 직접 줄여서 약물 처리 공장 자체를 느리게** 만들기 때문에 AUC가 지속적으로 증가. 두 기전이 겹치면(warfarin–phenylbutazone) displacement 단독보다 훨씬 큰 AUC 증가가 나오니까 반드시 분리해서 평가.

### CP6. 가역적 억제 vs MBI

| 비교 기준 | Reversible inhibition | MBI |
|---|---|---|
| 차원 | inhibitor 농도 감소와 함께 회복 | enzyme pool 재합성 뒤 회복 |
| 수식 위치 | $1+C_{u,I}/K_I$ 경쟁 분모 | $k_{inact}/K_I$ (in-vitro potency) + $k_{inact}/k_E$ (in-vivo factor), turnover clock |
| 변화 원인 | 가역적 결합 억제 | 효소 기능적 제거와 재합성 지연 |
| 혼동 시 결과 | washout을 inhibitor half-life만으로 설정 | carry-over interaction과 회복 지연 누락 |

> **⚡ 기억 고리 — "문 막기 vs 자물쇠 교체"**  
> Reversible inhibition은 **문을 막고 있는 것** — inhibitor가 사라지면 문이 다시 열림. MBI는 **자물쇠 자체를 망가뜨린 것** — inhibitor가 없어져도 새 자물쇠(효소)가 합성돼야 회복됨. 그래서 **MBI 약물 중단해도 interaction이 enzyme resynthesis 기간(CYP3A4 ≈ 2주) 동안 지속됨.** ⚠️ **MBI 강도는 $k_{inact}/K_I$(in-vitro 보고 지표)와 $k_{inact}/k_E$(in-vivo magnitude factor) 두 차원으로 분리**해서 볼 것 — in-vitro potency만 보고 in-vivo magnitude를 단정하면 organ별 효소 turnover 차이를 놓침. Washout period 설계에서 이 차이를 놓치면 carry-over interaction이 임상 시험 데이터를 오염시킴.

### CP7. 억제 vs 유도, 그리고 rifampin 급성/만성 전환

| 비교 기준 | 급성 transporter/enzyme inhibition | 만성 enzyme/transporter induction |
|---|---|---|
| 수식 위치 | $C_{u,I}/K_I$ | $R_{in}$ 증가, enzyme turnover |
| 변화 원인 | acute rifampin OATP 억제 | chronic rifampin CYP/P-gp 유도 |
| 혼동 시 결과 | 같은 rifampin을 항상 exposure 감소로 단정 | timing·route별 상반 방향 예측 실패 |

> **⚡ 기억 고리 — "방향 전환 스위치"**  
> Rifampin은 만성 투여 시 **유도자(inducer)** — CYP3A4와 P-gp를 늘려서 substrate exposure를 낮춤. 하지만 급성 IV 투여 시에는 **OATP 억제자** — hepatic uptake를 막아서 일부 substrate(atorvastatin)의 $C_{max}$를 10배, AUC를 7배 올림. **같은 약이 투여 경로와 시간에 따라 정반대 방향의 interaction을 만드는 사례임.** Timing × Route × Mechanism의 3차원 매트릭스 없이는 방향 예측 불가능.

### CP8. PK DDI vs PD DDI

| 비교 기준 | PK DDI | PD DDI |
|---|---|---|
| 차원 | 농도-시간 프로파일 변화 | 같은 농도에서 response 변화 |
| 수식 위치 | AUC, CL, F, $C_{max}$, $t_{1/2}$ | $EC_{50}$ shift, $E_{max}$ 감소, isobologram |
| 변화 원인 | 대사/수송/분포 변화 | receptor·효소·생리적 상호작용 |
| 혼동 시 결과 | response 변화를 모두 concentration 변화로 오해 | PD interaction을 PK 모델 오류로 잘못 처리 |

> **⚡ 기억 고리 — "농도 바꾸기 vs 반응 바꾸기"**  
> PK DDI는 농도-시간 프로파일 자체를 바꿔서 response가 달라지는 것 (약이 더 쌓이거나 덜 쌓임). PD DDI는 **같은 농도에서 효과 크기가 달라지는 것** (receptor, 효소, 생리적 경로의 상호작용). 구분 기준: **unbound concentration이 안 변하는데 response가 달라지면 PD interaction 의심.** Isobologram이 그 분리를 보여주는 실험 도구.

---

## §4. 자기 테스트 — 5초 triage 능동 회상 모듈

식 암기 모듈이 아님. **기전 분류(triage)** 를 묻는 모듈임. 모든 답은 "**어떤 파라미터가 상수가 아니게 됐는가?**"로 되돌아가야 함.

### Q1. [회상]
비선형성 진단에서 dose-normalized concentration-time plot과 AUC/Dose vs Dose plot을 먼저 그리는 이유는?  
**정답:** 선형이면 dose-normalized 관측값이 겹침. 안 겹치면 **CL, F, V/distribution, binding, time-dependent process 중 하나가 dose/time의 함수라는 신호**. 이 그림은 "어떤 파라미터가 상수가 아니게 됐는가?"를 묻는 첫 필터임 [G&W pp.112–114], [R&T p.492].

### Q2. [적용]
AUC/Dose가 dose와 함께 증가합니다. 가능한 두 가지 기전은?  
**정답:** **CL 감소 또는 F 증가.** capacity-limited elimination뿐 아니라 first-pass saturation도 가능하니까 **IV/oral 근거 필요** [G&W p.113], [R&T pp.499–506].

### Q3. [회상]
왜 Eq.2:264를 MM ODE citation으로 쓰면 안 되나?  
**정답:** Eq.2:264는 linear superposition 식임. MM clearance/rate/bolus/infusion/input 식은 **Eq.2:266–2:274** 영역 [G&W pp.114–118].

### Q4. [적용]
Phenytoin 300 mg/day에서 4 mg/L, 500 mg/day에서 36 mg/L가 된 이유를 Eq.16-7의 분모 관점에서 설명하세요.  
**정답:** $C_{u,ss} = K_m R_0/(V_m-R_0)$에서 dosing rate $R_0$가 **$V_m \approx 500$ mg/day에 가까워지면 분모가 작아져서** 농도가 비선형으로 솟구침. 전형값 $K_m \approx 0.4$ mg/L (unbound), $f_u \approx 0.1$ → total $K_m' \approx 4$ mg/L. **치료역 10–20 mg/L는 이미 capacity 근처** [R&T pp.491, 503].

### Q5. [적용]
Ascorbic acid는 **133배 dose 증가**에도 농도가 약 2배만 증가했음. phenytoin과 반대 방향의 비선형성이 생긴 이유는?  
**정답:** 농도 상승과 함께 **renal clearance가 saturable reabsorption escape valve로 증가** ($CL_R < 0.5$ mL/min @ 9 mg/L → 21 mL/min @ 19 mg/L, **42배 이상**). saturable reabsorption은 고농도에서 약물 제거를 가속하는 역방향 비선형성을 만듦 [R&T p.492], [R&T pp.507–510].

> 🎯 **Q6 이후로 들어가기 전 한 줄** — $V_{max}$–$K_m$ 식별성, enzyme turnover, $C_u$, $f_m$, route effect를 계산 직관으로 연결해야 답이 흔들리지 않음.

---

### Q6. [회상]
MM 모델에서 $V_{max}$와 $K_m$를 따로 추정하려면 어떤 농도 범위가 필요한가? "Vmax–Km Ridge Lock"이란?  
**정답:** **곡률을 포함하고, 특히 $K_m$ 주변 또는 그 이하의 농도**가 필요. high-concentration plateau만으로는 $V_{max}/K_m$ ridge가 생김 — single-dose data에서 흔히 $|\rho(V_{max}, K_m)| > 0.9$ (G&W p.116에서 −0.96 사례). 이걸 **"Vmax–Km Ridge Lock"**이라 부름. **구제:** 용량 수준 추가 또는 $K_m$ prior fix [G&W p.116, p.117].

### Q7. [적용]
반복투여 중 trough가 계속 낮아지고 single-dose model은 잘 맞아요. 어떤 기전을 먼저 의심?  
**정답:** **autoinduction 또는 time-dependent CL 증가** — **"Trough Envelope Drift" + "Single-dose Fit Trap"**의 결합. enzyme turnover compartment와 $k_{out}$ 식별 가능성 확인. PK22 design에서 $k_{out} \approx 0.023$ h⁻¹, 즉 **enzyme $t_{1/2} \approx 30$ h**가 식별됨 [G&W pp.126–129], [G&W pp.580–585].

### Q8. [적용]
Clarithromycin 병용 후 midazolam exposure가 multiple dosing에서 더 커지고 회복도 느림. reversible inhibition과 어떻게 정량적으로 다른가? **MBI의 두 가지 강도 지표를 구분.**  
**정답:** **MBI는 enzyme activity를 제거**하니까 회복이 inhibitor 농도 소실뿐 아니라 **enzyme resynthesis/degradation clock**에 묶임. **두 강도 지표 분리:** $k_{inact}/K_I$ (in-vitro MBI potency, $K_I$로 normalize한 표준 보고 지표) vs $k_{inact}/k_E$ (in-vivo magnitude factor, baseline 효소 turnover 대비 불활성화 상대속도, Eq.17-13 분모). 정량값: clarithromycin $k_{inact} \approx 0.07$ min⁻¹, $K_I \approx 7$ mg/L, $k_E \approx 0.23$ day⁻¹, $k_{inact}/k_E \approx 438$, $C_{u,I}/K_I \approx 0.025$ → 같은 inhibitor 노출에서 **reversible 식은 1.025배 CL 감소 예측, MBI 식($1+438\times0.025$)은 약 11배 CL 감소 예측.** CYP3A4 회복 약 **2주** 필요 [R&T pp.556–558].

### Q9. [적용]
Valproate 병용 후 total phenytoin은 낮아졌지만 unbound phenytoin은 유지됨. 용량을 줄여야 하나?  
**정답:** **displacement-only에서는 total이 misleading**할 수 있음. **unbound 농도와 임상 반응 기준으로 판단**해야 하고, total 감소만으로 dose 감량하면 안 됨. 열린 계 mass balance ($C_u = K^0/CL_u$)에서는 unbound clearance가 안 변하는 한 unbound steady state가 유지됨 [R&T p.543], [G&W §2.7.5].

### Q10. [계산 직관]
Affected drug의 $f_m$이 0.8이고 inhibitor가 해당 경로를 강하게 억제. 왜 $f_m = 0.3$인 약물보다 AUC ratio가 훨씬 커지나?  
**정답:** Eq.17-11에서 inhibited pathway term $f_m/(1+C_{u,I}/K_I)$가 작아져도 **residual $(1-f_m)$가 exposure ratio의 바닥을 정함.** $f_m = 0.8$이면 **남은 경로가 0.2뿐**이라 ratio가 크게 뛰지만, $f_m = 0.3$이면 0.7의 우회 경로가 있어서 ratio 상승이 제한됨 [R&T pp.550–552].

### Q11. [적용]
Oral midazolam interaction이 IV midazolam interaction보다 큼. 어떤 기전을 시사? Fluconazole–midazolam 정량 anchor 인용.  
**정답:** **gut wall/first-pass metabolism component가 크다**는 뜻. fluconazole 400 mg 병용 시 oral midazolam AUC ↑5.6배, IV ↑2배; F 24%→63%; $F_H$ 0.42→0.72; $F_G$ 0.57→0.88로 **$F_G$가 더 큰 비율로 변함** → midazolam oral first-pass에 gut wall 기여가 상당함 [R&T pp.553–554, Fig.17-10].

> 🎯 **Q12 이후로 들어가기 전 한 줄** — PM, rifampin, PD interaction, parent–metabolite, MBI, 보스 딜레마는 모두 **$f_m$, route, timing, recovery clock**을 순서대로 묻는 질문임.

---

### Q12. [회상]
Eq.17-18의 PM × inhibitor risk가 큰 이유는?  
**정답:** 다형성 경로가 **이미 결손된 PM**에서 남은 비다형성 경로가 inhibitor에 의해 막히면 **잔여 청소율이 매우 작아질 수 있기 때문.** $\text{Maximum exposure ratio} = 1/(1-f_m^{POLY}-f_m^{NP})$니까 **두 항의 합이 1에 가까울수록 ratio가 발산** [R&T pp.558–559].

$$
\underbrace{\text{Maximum exposure ratio}}_{\text{PM+억제}}
=
\frac{1}{\underbrace{1-f_m^{POLY}-f_m^{NP}}_{\text{남은 CL}}}
$$

### Q13. [적용]
Rifampin 병용에서 acute IV study는 AUC 증가, chronic oral 병용은 AUC 감소를 보일 수 있음. 왜 모순이 아닌가? **Atorvastatin acute IV 사례에서 활성 대사체가 PD 해석에 어떻게 끼어드나?**  
**정답:** **acute rifampin은 OATP1B1 같은 transporter 억제**로 hepatic uptake를 차단해 혈중 누적, **chronic rifampin은 enzyme induction**으로 CL 올려서 노출 감소. **timing과 route가 기전을 바꾸는 것.** Atorvastatin-rifampin acute IV: $C_{max}$ 10×, AUC 7×, $t_{1/2}$ 8→3h가 직접 anchor (**transporter signature: AUC↑ + $t_{1/2}$↓**) [R&T pp.560–565, Fig.17-19]. **활성 대사체 보강:** atorvastatin은 parent + 활성 2-hydroxy/4-hydroxy 대사체가 모두 HMG-CoA reductase 억제 (R&T p.564 "some of the metabolites are active"), **parent AUC ratio 7배는 PK 시계의 변화**이고 PD effect(cholesterol response, 3–4주 plateau)는 **합산 활성 노출 × cholesterol turnover 시간**에 의해 결정됨. 따라서 PK ratio와 PD ratio가 분리됨 [R&T pp.343, 564–565].

### Q14. [적용]
Response는 크게 변했지만 unbound 농도-시간 프로파일은 거의 안 변함. 무엇을 의심? 경쟁적 길항과 비경쟁적 길항을 수식 한 줄로 구분.  
**정답:** **PK DDI보다 PD interaction을 의심.** 경쟁적 길항(Eq.3:49)은 $E = E_{max} \cdot C/[C+EC_{50} \cdot (1+A/EA_{50})]$ — **$EC_{50}$을 shift시키지만 $E_{max}$는 보존.** 비경쟁적 길항(Eq.3:50)은 $E = E_{max}/(1+A/EA_{50}) \cdot C/(C+EC_{50})$ — **$E_{max}$를 감소.** 같은 receptor의 두 full agonist는 Eq.17-21로 $E_{max}$ ceiling 공유 [G&W pp.225–226], [R&T pp.567–570].

$$
\overbrace{E=\frac{E_{max}\cdot C}{C+EC_{50}\cdot(1+A/EA_{50})}}^{\text{경쟁: EC50↑}}
\qquad\text{vs}\qquad
\overbrace{E=\frac{E_{max}}{1+A/EA_{50}}\cdot\frac{C}{C+EC_{50}}}^{\text{비경쟁: Emax↓}}
$$

### Q15. [회상]
Drug–metabolite nonlinear model (G&W §2.7.6)에서 활성 대사체 disposition을 parent–metabolite 동시 관측 데이터만으로 추론적으로 외삽하면 안 되는 이유?  
**정답:** Gabrielsson p.137 명시 — "대사체 단독 투여 데이터 없이는 대사체 disposition kinetics에 대한 추가 외삽은 안 됨." 모약물과 대사체가 같은 MM 효소를 공유하면 **대사체의 prolonged tail이 (i) 자체 분포 kinetics 때문인지, (ii) 모약물의 saturable elimination이 대사체 형성 속도를 제한해서인지 식별 안 됨.** → 임상적으로 활성 대사체의 toxicity/efficacy 기여가 큰 약물(carbamazepine-10,11-epoxide, codeine-morphine, atorvastatin 2-/4-hydroxy 영역)에서는 **대사체 단독 투여 disposition study가 식별성 보강 단계로 필요**할 수 있음 [G&W pp.135–139].

### Q16. [회상]
R&T Table 17-5의 inhibitor strength 분류 기준은? Strong/Moderate/Weak는 substrate AUC 변화로 어떻게 구분되나? MBI는 별도 표시 이유?  
**정답:** **Strong = ≥5배 AUC 또는 >80% CL 감소; Moderate = 2–5배 AUC; Weak = 1.25–2배 AUC.** MBI inhibitor는 reversible 식만으로 분류하면 강도를 **과소평가**하니까 별도 표시 — 같은 $C_{u,I}/K_I$에서도 **reversible 1.025× vs MBI 11× CL 감소처럼 자릿수 단위로 다른 결과**가 나옴. 이 분류는 textbook reference이고 다른 규제문서의 분류 체계와 직접 동일시하지 않음 [R&T p.549].

### Q17. [적용]
Metformin이 cimetidine과 병용되었을 때 AUC가 50% 증가. 같은 mass action 분모 framework에서 hepatic AUC ratio 식 (Eq.17-11)이 신장 transporter DDI에도 적용된다는 것을 설명하고, 이게 hepatic OATP DDI와 어떻게 다른 임상 함의를 갖나?  
**정답:** **같은 mass action 분모 골격**이 적용됨 — hepatic AUC ratio 식에서 $f_m$ 자리에 **$f_e$(renal active secretion 분율)가 들어갈 뿐**, 분모 구조는 동일: $\text{AUC ratio}_{renal} \approx 1/[f_e/(1+C_{u,I}/K_I) + (1-f_e)]$. **Metformin–Cimetidine:** cimetidine이 OCT2(basolateral uptake) + MATE1(luminal efflux)를 동시 억제 → AUC ↑50%, $CL_R$ ↓27% (R&T Table 17-3, p.535). **임상적 차이:** metformin은 간 대사가 거의 없어서 **renal transporter DDI가 유일한 노출 변동 기전**이라 신기능 변화와 transporter inhibitor 병용 효과가 가산적으로 나타날 수 있음. hepatic OATP DDI(atorvastatin-rifampin acute)는 간 uptake 차단으로 $t_{1/2}$가 단축되지만, 신장 transporter DDI는 **소실 경로 차단으로 $t_{1/2}$ 연장 + AUC 증가**가 동시에 나타나는 게 시그너처 차이 [R&T Table 17-3, p.535; R&T pp.546–566].

### Q18. [보스 딜레마]
Sponsor가 "inhibitor 병용 시 AUC가 증가하니 label에 일괄 dose reduction을 쓰자"고 함. 10분 안에 기전 기반 검토 순서를 말하시오.  
**정답:**  
(1) **affected drug의 $f_m$과 inhibited pathway 확인** — $f_m$이 작으면 강한 inhibitor라도 whole-body AUC ratio는 제한됨 (Eq.17-11);  
(2) **$C_{u,I}/K_I$와 reversible vs MBI 구분** — MBI라면 $k_{inact}/K_I$ (in-vitro potency)와 $k_{inact}/k_E$ (in-vivo factor) 평가 + enzyme recovery clock 고려;  
(3) **oral/IV route effect 확인** — Diltiazem-Lovastatin 1.27 vs 3.57 (Table 17-7) 패턴이면 gut wall first-pass component 우세;  
(4) **PM 또는 잔여 경로 risk 확인** — Eq.17-18 분모 발산 위험;  
(5) **acute/chronic perpetrator effect와 withdrawal sequence 확인** — phenobarbital-dicumarol 3–4주 plateau onset, MBI 2주 recovery washout trap;  
(6) **transporter/multifaceted signature 확인** — AUC↑ + $t_{1/2}$↓ 패턴이면 metabolic inhibition이 아니라 transporter; **신장 transporter도 같은 mass action framework**으로 평가 (metformin-cimetidine AUC↑50%, probenecid-acyclovir $CL_R$↓32%);  
(7) **활성 대사체 기여 확인** — atorvastatin처럼 활성 대사체가 PD에 기여하면 parent AUC ratio가 PD ratio와 분리됨;  
(8) **세 식이 같은 골격임을 점검** — Eq.2:266 ↔ Eq.16-7 ↔ Eq.17-11이 같은 기전의 다른 표현임을 sponsor에게 명확히 전달.  

단, 여기서는 textbook 기반 기전 체크리스트로만 둠 [R&T pp.546–565], [G&W pp.115–118].

---

## §5. 한 페이지 압축 — 7 문장 기억 모델

세부식을 외우기 전, **기전 분류 순서를 유지하기 위한 압축본**임. 이 일곱 문장으로 비선형 PK 챕터 전체가 압축됨.

**1.** 비선형성은 **중첩 원리 실패(superposition failure)** 로 발견됨. 첫 그림은 항상 dose-normalized profile과 AUC/Dose vs Dose임 [G&W pp.112–114], [R&T p.492].

**2.** **용량 한계(capacity limitation)** 는 $CL(C)$를 만들고, $R_0 \to V_m$에서 정상상태가 발산함 [G&W pp.115–119], [R&T pp.500–506]:

$$
\underbrace{CL(C)}_{\text{농도 CL}}
\qquad;\qquad
\underbrace{R_0\to V_m}_{\text{R0→Vm}}
\Rightarrow
\underbrace{C_{ss}\uparrow\uparrow}_{\text{Css 급상승}}
$$

⚠️ **단, "$V_m$ 20% 감소 → $C_{ss}$ 2배"는 R&T p.506의 $R_0=300, V_m=500$ ($R_0/V_m=0.6$) anchor의 prototype 수치이지 portable rule이 아님.** capacity 탄력성 $-V_m/(V_m-R_0)$이 시작점에 따라 자릿수 단위로 다른 값을 줌.

**3.** **시간 의존성**은 효소/수송체/생리학 시계가 약물 농도 시계와 분리될 때 생김. Master clock = $\max(t_{1/2}^{enzyme}, t_{1/2}^{inducer}, t_{1/2}^{drug})$ [G&W pp.119–129], [R&T pp.516–519], [R&T pp.560–561]. ⚠️ **MBI 강도는 $k_{inact}/K_I$(in-vitro potency)와 $k_{inact}/k_E$(in-vivo magnitude factor) 두 차원으로 분리.**

**4.** **결합**은 total을 속이고, 열린 계에서는 $C_u = K^0/CL_u$ 물질 수지가 비결합 노출을 강제함 [G&W pp.129–134], [R&T pp.538–544]:

$$
\underbrace{C_u}_{\text{자유 노출}}
=
\frac{\underbrace{K^0}_{\text{입력}}}{\underbrace{CL_u}_{\text{자유 CL}}}
$$

**5.** **DDI 예측**은 $f_m$, 억제제 강도($C_{u,I}/K_I$, $k_{inact}/k_E$), 투여 경로, PM/잔여 경로, 유도/MBI 회복을 함께 봄 [R&T pp.546–561]:

$$
\underbrace{f_m}_{\text{경로몫}}
\quad;\quad
\underbrace{C_{u,I}/K_I}_{\text{가역 억제}}
\quad;\quad
\underbrace{k_{inact}/k_E}_{\text{MBI/회복}}
$$

**6.** **복합 DDI와 PD 상호작용**은 "AUC 하나"로 기전을 단정하지 못하게 함. $C_{max}$, $t_{1/2}$, V/F, 경구/정맥 비율, 등효능선(isobologram)을 함께 봄. ⚠️ **신장 transporter DDI(metformin-cimetidine AUC↑50%, probenecid-acyclovir $CL_R$↓32%)도 같은 mass action 분모로 회수됨** [R&T Table 17-3, p.535; R&T pp.563–570].

**7. 세 식은 결국 하나임:** 비선형 PK·TDM·DDI 직관은 같은 분모 구조의 다른 표현임 (Eq.2:266 ↔ Eq.16-7 ↔ Eq.17-11). 이 한 식이 capacity, $C_{ss}$ 발산, DDI AUC ratio를 통째로 꿰어줌 [G&W p.115], [R&T p.503], [R&T p.550]:

$$
\overbrace{CL=\frac{V_{max}}{K_m+C}}^{\text{Card 2}}
\;\Longleftrightarrow\;
\overbrace{C_{u,ss}=\frac{K_m R_0}{V_m-R_0}}^{\text{Card 2 (Css)}}
\;\Longleftrightarrow\;
\overbrace{\text{AUC ratio}\approx\frac{1}{\frac{f_m}{1+C_{u,I}/K_I}+(1-f_m)}}^{\text{Card 5}}
$$

### 후속 세션에서 이 챕터가 여는 것들

| 후속 세션 | 이 챕터에서 열리는 개념 | 이 챕터 없으면 실패하는 것 |
|---|---|---|
| PopPK 모델 구축 | 비선형 CL, 시간 변동 CL, 결합 비선형성, 수송체 DDI 구분 | 파라미터 변동성이 기전 오류를 가림 |
| TDM | phenytoin형 capacity limitation, total-only monitoring 한계, plateau 도달 시간 발산 | 작은 용량 변화와 치환/결합 상황을 잘못 해석 [R&T pp.491–506], [R&T p.543] |
| DDI 연구 해석 | reversible inhibition, MBI(두 강도 지표), induction, transporter(간/신장), route effect 분리 | 약물 시작/중단 권고 오류 [R&T pp.546–565] |
| 약물-대사체 모델링 | parent–metabolite 동시 관측의 식별성 한계, 활성 대사체의 PD 기여 분리 | metabolite disposition 부당하게 외삽, PK ratio와 PD ratio 혼동 [G&W pp.135–139], [R&T pp.343, 564] |
| PD 상호작용 모델링 | $EC_{50}$ 이동, $E_{max}$ 감소, $E_{max}$ ceiling, isobologram | PK 변화 없는 response 변화를 PK 모델 오류로 오해 [G&W pp.224–227], [R&T pp.567–570] |

---

## 마지막 한 줄 — 챕터 전체를 손에 쥐는 방법

이 챕터의 최종 골격을 한 줄로 꿰면 이거임:

> **"비선형성 진단 → 다섯 분모 중 어느 분모인지 식별 → DDI 예측으로 옮기기 → route/timing/unbound/PM/active metabolite 함정 피하기 → 세 식이 하나의 mass action 분모로 회수된다는 사실 확인 (간/신장 transporter, 효소 모두 동일 골격)."**

이 골격을 PhD 1년차가 확실히 체화하면, 비선형 PK와 DDI 챕터의 대부분이 **암기가 아니라 기전 분류로 회수됨.** 정량 anchor는 수식 골격을 임상 정량값으로 채워서 "수식을 외운 것"이 아니라 **"수식을 임상 case에 즉시 매핑할 수 있는 것"** 으로 학습 목표를 끌어올림.

phenytoin 환자가 또 들어오면, 이제 당황하지 않게 됨. 5초 안에 머릿속에서 — "아, 지금 $V_m - R_0$ 분모가 무너지고 있구나"가 떠오르게 됨. 그게 이 챕터의 진짜 목표임.

---

*C-260517-073412-K7Q*

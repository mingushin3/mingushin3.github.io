# Session 11 — Indirect Response / Turnover / DRT / Baseline / Effect Compartment / Rate-Limiting / Duration — v4.2_final (보강본_final)

> **보강본 노트(v4.0 → v4.1 → v4.2_final)**
> 본 보강본은 v4.0 본문을 변경 없이 보존하면서, 1차 계량약리학 교수 검토(v4.1)에 더해 **2차 정밀 검토 의견**(v4.2_final)을 반영했습니다.
>
> **v4.1 보강 (1차 검토 반영)**:
> ① **Card 2** — Model 2 최대 변화량의 경계 거동($I_{max}\to 1$ 발산) 명시
> ② **Card 4-보강** — Pool/Precursor 다단계 간접반응(Sharma-Jusko 1998)을 명시적 ODE와 함께 추가
> ③ **Card 6 §D** — Friberg-Karlsson 항암제 호중구 감소 모델을 응용 사례로 추가
> ④ 본문 끝에 **정확한 교과서·1차 문헌 출처** 섹션 추가
>
> **v4.2_final 정밀화 (2차 검토 반영)**:
> ⑤ **Card 1** — G&W §2.6.7의 moderator 모델 식(Eq 2:261–2:263)을 명시적으로 추가하고, **"R = M at dynamic steady state"** 가정을 본문 자체에서 직접 인용·annotation (2차 검토 1-8 반영)
> ⑥ **Card 4-보강** — Sharma & Jusko 1998 원 논문이 **Models V–VIII로 명시적 번호 부여를 하지 않았다는 점**을 본문 내에서 정정하고, 해당 명명이 **후속 문헌(Jusko 그룹 후속 review 등)의 관행적 명명**임을 명시 (2차 검토 1-4 반영)
> ⑦ **Card 6 §D** — Friberg & Karlsson 2002의 $k_{prol}=k_{tr}=k_{circ}$ 제약을 "흔히 고정되는 관행"이 아닌 **원 논문에서 식별성 확보를 위해 도입된 모델 구조의 일부**로 재기술 (2차 검토 1-3 반영)
> ⑧ **§9 References** — G&W와 R&T 교과서 출처를 ISBN·DOI 정확도까지 정밀화하고, Sharma-Jusko 1998 및 Friberg-Karlsson 2002의 인용 위치를 본문과 1:1로 묶음 (사용자 요청 반영)
>
> 본문 내 모든 [G&W pp.XXX] / [R&T pp.XXX] 인라인 인용은 그대로 유지되며, v4.2_final에서 신규 추가된 수식은 모두 overbrace/underbrace로 annotation했습니다. v4.1 보강 영역의 일부 표 항목 표현(예: "흔히 고정")이 정정되었지만, **수치 anchor, 핵심 ODE 구조, 약물명, 카드 ID, 표 행 순서는 v4.1과 100% 일치**합니다.

**Naproxen** 500 mg을 치통(dental pain) 환자한테 경구로 줘봅시다. 그러면 약물이 통증을 가라앉히기 시작하는데, 신기한 게 있어요. **혈장 농도가 똑같아도, 농도가 오르는 중이냐 떨어지는 중이냐에 따라 통증 완화 정도가 달라집니다** (1–8 h 관찰) [R&T pp.234–235]. 같은 농도에서 두 가지 답이 나오는 거예요.

이 그림을 본 모델러는 본능적으로 한 가지 질문을 던집니다 — **"그래서 어디가 느린 겁니까?"** 농도가 늦는 건지, 생물학이 늦는 건지, 표적이 소비된 건지, 아니면 PK가 duration을 발목 잡고 있는 건지. 이 질문 하나가 이번 세션 전체를 굴러가게 합니다.

또 다른 예시 하나. **Aspirin** 650 mg(NSAID 겸 항혈소판제)을 주면 혈장에서 약물은 몇 시간 안에 사라져요. 그런데 thromboxane B₂ 억제는 며칠 갑니다. → 그래서 **혈장 반감기만으로는 효과 지속시간을 설명할 수 없다**는 사실의 대표 사례입니다 [R&T p.251].

<!-- SLIDE_START: S01 | title: §1 — 세션 헤더 & 로드맵 -->
<!-- SECTION_CORE: SC-01 -->
# §1 — 세션 헤더 & 로드맵

## 핵심 통찰(Big Idea)

임상에서 보이는 약력학 반응은 **혈장 농도와 완벽하게 동시에 움직이지 않습니다.** 그렇다고 모든 지연을 별도 모델로 다뤄야 한다는 뜻도 아니에요. 지연이 sampling 해상도보다 짧으면 direct PK–PD link로도 충분합니다. 지연이 눈에 띄면 그때 원인을 네 후보 중 하나로 분해해야 합니다 — **분포 지연이냐, turnover(system flux)냐, 표적 소비냐, 아니면 PK 또는 PD clock 중 어느 쪽이 더 느린 것이냐** [G&W pp.235–236; R&T pp.233–235, 239].

같은 농도에서 시간 경로에 따라 반응이 달라지는 현상을 **hysteresis**라고 합니다. 이건 "곡선이 예쁘지 않다"는 문제가 아니에요. **지연이 어디에 사는지 다시 물어보라는 신호**입니다.

## 8개 카드, 한 줄로 꿰면

이번 세션은 카드 8개로 갑니다. 카드들이 따로 떠 있지 않아요. **"지연은 어디에 사는가 → 어느 시계가 가장 느린가"**라는 질문 하나에 모두 매달려 있어요.

- **M1**: response pool에서 baseline은 왜 그냥 상수가 아니라 생산속도와 소실속도의 비율인가
- **M2**: 약물이 input을 건드렸는가, output을 건드렸는가 — 네 칸 중 어디인가
- **M3**: $t_{ss}$와 peak shift로 그 칸을 어디까지 가려낼 수 있는가
- **M4**: 같은 이름의 $E_{max}$가 왜 모델마다 다른 의미를 갖는가
- **M5**: NONMEM 돌리기 전에 손으로 어디까지 잠가놔야 하는가
- **M6**: 약물이 사라졌는데 효과가 왜 남아 있는가 — 표적이 소비된 경우
- **M7**: 곡선이 똑같이 잘 맞을 때 turnover와 effect compartment를 어떻게 가르나
- **M8**: 결국 어느 시계가 가장 느린가 — duration 공식은 언제 살아있고 언제 폐기되나

## 5단계 골조 — 이번 세션의 척추

| 단계 | 핵심 고정점 | 왜 필요한가 |
|---|---|---|
| 1 | $dR/dt=k_{in}-k_{out}\cdot R$와 $R_0=k_{in}/k_{out}$ | baseline과 time constant를 만든다 [G&W p.237] |
| 2 | 약물은 production 또는 loss 중 하나를 inhibit/stimulate | 4-model 분류의 출발점 [G&W pp.237–245] |
| 3 | $t_{ss}$/peak shift | 강력한 선별 신호이지만 PK rate-limiting과 좁은 dose range에 가려질 수 있음 [G&W pp.247–251, 778–783] |
| 4 | Effect compartment vs turnover | 제한된 설계에서는 거의 같은 곡선을 만들 수 있어 fit quality만으로 구조 확정 불가 [G&W pp.758–763; R&T pp.244–246] |
| 5 | PK clock vs PD clock | 반응 감소는 둘 중 느린 쪽이 결정 [R&T pp.243, 247–256] |

> 💡 이번 장 한 줄: **지연된 반응은 한 가지 현상이 아니라 여러 원인이 만들어내는 공통의 겉모습이에요.** 첫 질문은 "어떤 ODE가 곡선을 잘 맞추는가?"가 아닙니다. **"무엇이 시간을 가장 느리게 만드는가?"** — 이게 첫 질문입니다.

<!-- SLIDE_START: S02 | title: §2 — 개념 해부 카드 -->
<!-- SECTION_CORE: SC-02 -->
# §2 — 개념 해부 카드

<!-- SLIDE_START: M1 | title: Turnover Model Foundation + Hysteresis Classification -->
<!-- SECTION_CORE: SC-03 -->
## Card 1 — Turnover Model Foundation + Hysteresis Classification

> **거장의 시각**
> Baseline을 그냥 상수처럼 읽으면 $k_{in}$과 $k_{out}$이 따로 추정되지 않는다는 걸 놓칩니다. 그러면 hysteresis가 보여도 단순한 산포로 오독해요. **$R_0=k_{in}/k_{out}$와 $1/k_{out}$를 먼저 잡아두면**, 그 다음에 나오는 모든 지연 배정 작업이 **"어느 pool이 느린가"**라는 한 질문으로 정리됩니다.

### A. 공식 정의 + 수식

Turnover 모델은 response pool의 생산속도와 소실속도가 균형을 이루는 최소 골격이에요. 들어오는 속도에서 나가는 속도를 뺀 게 변화율입니다. **여기서 가장 중요한 사실 — baseline은 독립 상수가 아니라 두 속도의 비율입니다** [G&W pp.235–237; R&T pp.234–235, 239].

$$
\underbrace{\frac{dR}{dt}}_{\text{변화율}}
=
\underbrace{k_{in}}_{\text{생산}}
-
\overbrace{\underbrace{k_{out}}_{\text{소실 clock}}\,\underbrace{R}_{\text{반응 pool}}}^{\text{pool 소실}}
\quad \text{[G&W Eq 3:74; G&W p.237]}
$$

정상상태에서는:

$$
\underbrace{R_0}_{\text{기저값}}
=
\frac{\underbrace{k_{in}}_{\text{생산}}}{\underbrace{k_{out}}_{\text{소실 clock}}}
\quad \text{[G&W Eq 3:76; G&W p.237]}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $R$ | response unit | 측정된 약리학적 반응 | 약물 작용, 질병 진행, 일주기 변동 |
| $k_{in}$ | response·time⁻¹ | 0차 생산 속도 | 합성 억제/촉진, 생리적 생산률 변화 |
| $k_{out}$ | time⁻¹ | 1차 소실 속도이자 회복 clock | 소실 경로 변화, feedback, system 상태 |
| $R_0$ | response unit | 기저 반응 (기본 모델에서는 시간 불변) | $k_{in}/k_{out}$ 비율 변화, baseline drift |

$R_0$는 측정하기 전부터 정해진 상수가 아니에요. **들어오는 속도와 빠지는 속도가 만든 균형점**입니다. 욕조에 비유하면, 수도꼭지가 일정 속도로 물을 넣고 배수구가 수위에 비례해서 물을 빼면, 어느 수위에서 두 속도가 똑같아지는 지점이 생기죠. 그 수위가 $R_0$예요.

그래서 — hysteresis가 보인다고 해서 direct response가 무조건 틀린 것은 아닙니다. **sampling 해상도 안에서 지연이 보이는지부터 먼저 판단**해야 합니다.

### B. Hysteresis 분류

Hysteresis는 **같은 농도에서 올라가는 길과 내려오는 길의 반응이 다른 현상**입니다 [R&T pp.234–235]. 농도-반응을 평면에 그리면 loop가 그려져요.

| 패턴 | 해석 | 대표 사례 |
|---|---|---|
| 반시계 방향(counterclockwise) | 반응이 농도 뒤에서 따라옴 — 분포 지연, 하류 PD, 또는 system flux | **Naproxen** 500 mg 경구(NSAID; 진통제), dental pain, 1–8 h, Fig 8-2 [R&T pp.234–235]; **Ibuprofen**(NSAID; 해열·진통제) 6 mg/kg 경구, febrile children, Fig 8-9 [R&T pp.241–242] |
| Hysteresis 없음 / direct link | 작용 부위 평형과 반응 생성이 관측 시간 척도보다 훨씬 빠름 | **Midazolam** 15 mg/kg 경구(rat EEG; 진정제), Fig 8-6 [R&T p.239] |
| 시계 방향(clockwise) | 내성, 피드백, 활성 대사체, 또는 추가 동역학 | 이 세션의 R&T 사례에는 포함 안 됨 — 추후 tolerance 장에서 다룸 |

> 🔑 **30초 방향 진단**: 반시계면 분포/turnover/활성 대사체 후보부터 떠올리고, 시계 방향이면 내성/피드백 후보부터 떠올립니다. 이걸 첫 30초 안에 하면 진단 순서가 자동으로 갈립니다.

농도-반응 loop는 같은 산을 오르내리는 두 길의 고도 기록 같은 거예요. 같은 고도라도 올라가는 중인지 내려오는 중인지에 따라 몸 상태가 다르면, 고도 하나로는 설명이 끝나지 않습니다.

→ 그래서 위 세 약물(naproxen, ibuprofen, midazolam)이 이번 카드의 진단 분류를 임상에서 직접 보여주는 사례들입니다.

### C. 재파라미터화(Reparameterization)

모델을 적합시킬 때 $k_{in}$과 $k_{out}$을 따로 추정하지 마세요. **$R_0$와 $k_{out}$을 먼저 추정**합니다.

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
\quad \text{[G&W Eq 3:103; G&W p.247]}
$$

$k_{in}$과 $k_{out}$을 따로 추정하려는 건 **어두운 방에서 수도꼭지와 배수구를 동시에 만지면서 수위를 맞추는 일**이에요. $R_0$와 $k_{out}$으로 바꿔 쓰면 "현재 수위"와 "배수 속도"를 먼저 잡아놓는 거라 탐색 방향이 단순해집니다. PD4 사례에서, 충분한 설계 없이 상류 pool과 response의 turnover 상수를 따로 추정하면 **두 파라미터를 따로 추정할 수 없는 상태(non-identifiability)에 가까워집니다** [G&W pp.742–752].

> 🔑 **재파라미터화 신호**: $k_{in}$과 $k_{out}$이 극단적인 상관을 보이거나 covariance step이 "30 iteration 동안 OFV 안 떨어지다가 갑자기 뚝 떨어지는" 패턴이면 $R_0\cdot k_{out}$로 재코딩하세요.

### D. 맥락 통합

음성 피드백은 조절인자 $M$을 추가해 반응이 높을수록 소실이 빨라지게 만듭니다. **IgG**(면역글로불린; 항체 보호기전 FcRn 의존) 사례에서 혈청 IgG 30 mg·mL⁻¹일 때 반감기가 약 11일로 단축됩니다 — → 그래서 **$k_{out}$이 고정 상수가 아니라 system 상태에 의존할 수 있다**는 사실의 사례입니다 [G&W pp.110–111].

> 📐 **Moderator 모델의 정식 식 구조 (G&W §2.6.7, Eq 2:261–2:263)**
> 위에서 한 줄로 짚은 negative feedback의 정식 ODE 구조는 다음과 같습니다 [Gabrielsson \& Weiner 5e pp.110–111]:
>
> $$
> \underbrace{\frac{dR}{dt}}_{\text{response 변화}}
> =
> \overbrace{\underbrace{k_{in}}_{\text{생산}}\,\underbrace{H(C)}_{\text{약물 함수}}}^{\text{drug-modulated input}}
> -
> \underbrace{k_{out}\,M}_{\text{moderator-driven loss}}
> \quad \text{[G\&W Eq 2:261; p.110]}
> $$
>
> $$
> \underbrace{\frac{dM}{dt}}_{\text{moderator 변화}}
> =
> \overbrace{\underbrace{k_{tol}\,R}_{\text{R에 의한 생성}}
> -\underbrace{k_{tol}\,M}_{\text{1차 소실}}}^{\text{tolerance pool turnover}}
> \quad \text{[G\&W Eq 2:262; p.111]}
> $$
>
> $$
> \underbrace{\text{slope}_{A,B,C}}_{\text{관찰 반감기 기울기}}
> =
> \underbrace{k_{out}}_{\text{소실 clock}}\!\left(1+\underbrace{\frac{R_{A,B,C}}{M_{50}}}_{\text{포화 분율}}\right)
> \quad \text{[G\&W Eq 2:263; p.111]}
> $$
>
> ⚠️ **R = M 가정의 위치 — derivation을 따라가려면 반드시 짚어야 함**
> G&W 5e p.111 본문은 다음을 명시합니다 — *"The three slopes are functions of $k_{out}$ and $M$, **since $R$ is equal to $M$ at dynamic steady state** in the simplest form of model …"*
>
> 즉, "$R_0 = k_{in}/k_{out}$"라는 기저값이 위 ODE 시스템에서 회수되려면, **$H(C)=1$(약물 없음) 그리고 $R=M$ at steady state** 두 조건이 동시에 필요합니다. 검증:
>
> $$
> \underbrace{\frac{dR}{dt}=0}_{\text{steady state}}
> \;\Rightarrow\;
> \underbrace{k_{in}}_{\text{생산}}
> =
> \underbrace{k_{out}\,M}_{\text{소실}}
> \;\xrightarrow[R=M]{\text{steady state 가정}}\;
> \overbrace{k_{in}=k_{out}\,R}^{\text{moderator-free 골격으로 환원}}
> \;\Rightarrow\;
> \underbrace{R_0=k_{in}/k_{out}}_{\text{Eq 3:76 재현}}
> $$
>
> 학생이 이 **R = M 가정을 놓치면**, moderator 모델의 정상상태가 단순 turnover와 어떻게 연결되는지 derivation이 끊깁니다. → 그래서 G&W가 Eq 2:263 직전에 이 가정을 본문에 명시적으로 박아둔 거예요. **본 자료에서 moderator/feedback이 등장할 때마다 이 R=M 정상상태 가정이 암묵적으로 작동**한다고 보면 됩니다.

Baseline drift 모델은 별도 확장이에요 — 질병 진행이나 일주기 변동이 $R_0$ 자체를 움직이면, 기본 상수-baseline turnover 식만으로는 부족합니다 [G&W pp.317–319].

NONMEM 출력에서 30회 iteration 동안 OFV가 거의 안 변하다가 갑자기 큰 폭으로 떨어진다면, 보통 $r(k_{in},k_{out})>0.98$ 상관이 search direction을 죽이고 있다는 신호예요. PD5 Table 5.1이 이 패턴을 그대로 기록합니다 — *"correlation greater than 0.98… reparameterization of the model by baseline $R_0$ and $k_{out}$."* PD4 Pool 1의 $r(k_1,k_{out})=0.9999$, CV% 4000 사례가 이 비식별성의 극단 형태입니다. 같은 데이터에 $k_1=k_{out}$ 제약을 걸어 만든 Pool 2의 "정상적인 CV%"는 **데이터가 동등성을 지지한 게 아니라 제약이 비식별성을 해결한 것**이에요.

> 💼 **실무 인사이트**: "직접 vs 지연" 판정은 모델 계열을 고르기 전에 **설계 해상도(design-resolution) 결정**으로 먼저 다뤄야 합니다. 지연이 sampling 척도에서 안 보이면, 생물학적으로 완전히 순간적이지 않더라도 direct link로 방어할 수 있어요.

> 📖 **G&W 5e p.235, Fig 3.33; R&T 5e p.235, Fig 8-2**: Fig 3.33은 직접 반응과 지연 hysteretic 반응이 어떻게 다르게 그려지는지 한눈에 보여줍니다. Fig 8-2는 같은 naproxen 농도에서도 상승기/하강기에 따라 통증 완화가 다르게 나타나는 걸 직접 그려놓은 거예요. → 그래서 농도 하나로 반응을 다 설명할 수 없다는 사실의 시각적 증명입니다.

**이번 카드 핵심내용**: ① baseline은 $R_0=k_{in}/k_{out}$ 비율이 결정하지, 독립 상수가 아니에요. ② hysteresis 방향이 지연이 어디 사는지(분포냐 turnover냐 내성이냐)의 첫 단서입니다. ③ $R_0$를 독립 상수로 고정하고 들어가면 비식별성, stuck-then-drop, 잘못된 지연 배정이 줄줄이 따라옵니다.

<!-- SLIDE_START: M2 | title: Four-Model Taxonomy: Inhibit/Stimulate × Production/Loss -->
<!-- SECTION_CORE: SC-04 -->
## Card 2 — Four-Model Taxonomy: Inhibit/Stimulate × Production/Loss

앞에서 response pool의 baseline과 회복 clock을 잡았어요. 이번엔 그 균형을 **약물이 input에서 깨는지 output에서 깨는지** 결정합니다.

> **거장의 시각**
> 반응 방향만 보고 "억제/촉진"을 붙이면 Model 1과 Model 4를, 또는 Model 2와 Model 3을 뒤섞게 됩니다. 약물 함수가 **$k_{in}$에 붙는지 $k_{out}R$에 붙는지**를 보면 $t_{ss}$, $R_{ss}$, 최대 변화량의 해석이 그 자리에서 정렬돼요.

### A. 형식적 정의 + 수식

가역적 turnover 반응에서 약물이 작용할 수 있는 부위는 네 가지뿐입니다 — production 억제, loss 억제, production 촉진, loss 촉진. 이 네 칸이 **생물학적 기전을 NONMEM `$DES` 블록으로 옮길 때 최소 문법**이에요 [G&W pp.237–245; R&T pp.240–241].

$$
\underbrace{I(C)}_{\text{남은 activity}}
=
1-
\underbrace{\frac{\overbrace{I_{max}\,C^n}^{\text{억제구동}}}{\underbrace{IC_{50}^n}_{\text{절반농도}}+\underbrace{C^n}_{\text{농도항}}}}_{\text{억제분율}},
\quad 0\le I_{max}\le 1
\quad \text{[G&W Eq 3:77; G&W p.237]}
$$

$$
\underbrace{S(C)}_{\text{촉진배율}}
=
1+
\underbrace{\frac{\overbrace{E_{max}\,C^n}^{\text{촉진구동}}}{\underbrace{EC_{50}^n}_{\text{절반농도}}+\underbrace{C^n}_{\text{농도항}}}}_{\text{촉진분율}}
\quad \text{[G&W Eq 3:78; G&W p.237]}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $I(C)$ | 무차원 | 남아 있는 production/loss activity | 농도 증가, $I_{max}$, $IC_{50}$, Hill 계수 |
| $S(C)$ | 무차원 | production/loss 촉진 배율 | 농도 증가, $E_{max}$, $EC_{50}$, Hill 계수 |
| $I_{max}$ | 무차원 | 최대 억제 가능 분율 | 약물 potency/efficacy, 작용부위 민감도 |
| $E_{max}$ | 무차원 또는 response unit | 모델 구조에 따라 최대 촉진 또는 절대 효과 | 파라미터화, baseline scale, system turnover |
| $IC_{50}/EC_{50}$ | concentration | 절반 효과 농도 | 작용부위 노출, 기전적 potency |
| $n$ | 무차원 | Hill 곡률 | 협동성 또는 경험적 steepness |

$I(C)$와 $S(C)$는 **약물이 수도꼭지나 배수구에 갖다 붙이는 밸브**예요. 같은 밸브라도 수도꼭지에 붙으면 수위 변화의 의미가 달라지고, 배수구에 붙으면 빠지는 속도 자체가 달라집니다.

> ⚠️ $I_{max}$와 $E_{max}$는 이름이 비슷해도 **임상적 의미가 같지 않습니다.** 어떤 항에 곱해지느냐가 의미를 결정해요.

### B. 네 가지 모델의 병렬 비교

| 모델 | ODE | 약물 작용 부위 | $t_{ss}$ 지배 인자 | 일정 $C_{ss}$에서 $R_{ss}$ | 최대 $\Delta R$ | $R$의 한계 | Baseline 복귀 | 대표 사례 |
|---|---|---|---|---|---|---|---|---|
| 1. 생산 억제 | $\frac{dR}{dt}=k_{in}I(C)-k_{out}R$ [G&W pp.238–239] | input/biosynthesis 차단 | $k_{out}$; PK 빠르면 용량 독립 | $R_0 I(C_{ss})$ | $R_0 I_{max}$ [G&W p.239] | 완전 억제 시 0을 향함 | $k_{out}$가 회복 지배 | **Warfarin**(경구 항응고제; vitamin K cycle/prothrombin complex 억제) — → 그래서 **Model 1의 임상 prototype**입니다 [G&W PD4 pp.742–752; R&T pp.242–247] |
| 2. 소실 억제 | $\frac{dR}{dt}=k_{in}-k_{out}RI(C)$ [G&W pp.240–241] | output/removal 차단 | effective $k_{out}\cdot I(C)$; 용량 의존 | $R_0/I(C_{ss})$ | $R_0 I_{max}/(1-I_{max})$ [G&W p.241] | baseline 위로 상승 가능 | 회복은 복원된 loss process에 의존 | **Furosemide**(loop 이뇨제; Henle 고리 Na/K/Cl 재흡수 차단)-type retention 예시 — → 그래서 **Model 2의 사례**입니다 [G&W p.238] |
| 3. 생산 촉진 | $\frac{dR}{dt}=k_{in}S(C)-k_{out}R$ [G&W pp.242–243] | input 촉진 | $k_{out}$; PK 빠르면 용량 독립 | $R_0 S(C_{ss})$ | $R_0 E_{max}$ [G&W p.243] | baseline의 배율만큼 상승 | $k_{out}$가 회복 지배 | **Erythropoietin**(EPO; 적혈구생성 자극 호르몬; RBC 합성 촉진) — → 그래서 **Model 3의 사례**입니다 [G&W p.238] |
| 4. 소실 촉진 | $\frac{dR}{dt}=k_{in}-k_{out}RS(C)$ [G&W pp.244–245] | output 촉진 | effective $k_{out}\cdot S(C)$; 용량 의존 | $R_0/S(C_{ss})$ | $R_0 E_{max}/(1+E_{max})$ [G&W p.245] | baseline 아래로 감소 | 고촉진 시 더 빠른 복귀 | CB1 inverse agonist / energy expenditure [G&W p.238]; PD7 compound C [G&W pp.764–769] — → 그래서 **Model 4의 사례**입니다 |

$$
\begin{aligned}
\text{Model 1: }&\frac{dR}{dt}=\overbrace{k_{in}I(C)}^{\text{input 억제}}-\underbrace{k_{out}R}_{\text{loss}}\\
\text{Model 2: }&\frac{dR}{dt}=\underbrace{k_{in}}_{\text{input 유지}}-\overbrace{k_{out}RI(C)}^{\text{loss 억제}}\\
\text{Model 3: }&\frac{dR}{dt}=\overbrace{k_{in}S(C)}^{\text{input 촉진}}-\underbrace{k_{out}R}_{\text{loss}}\\
\text{Model 4: }&\frac{dR}{dt}=\underbrace{k_{in}}_{\text{input 유지}}-\overbrace{k_{out}RS(C)}^{\text{loss 촉진}}
\end{aligned}
$$

$$
\begin{aligned}
\text{Model 1: }&\underbrace{R_{ss}}_{\text{새 정상상태}}=\underbrace{R_0}_{\text{기저값}}\underbrace{I(C_{ss})}_{\text{억제함수}}\\
\text{Model 2: }&\underbrace{R_{ss}}_{\text{새 정상상태}}=\frac{\underbrace{R_0}_{\text{기저값}}}{\underbrace{I(C_{ss})}_{\text{loss 억제}}}\\
\text{Model 3: }&\underbrace{R_{ss}}_{\text{새 정상상태}}=\underbrace{R_0}_{\text{기저값}}\underbrace{S(C_{ss})}_{\text{촉진함수}}\\
\text{Model 4: }&\underbrace{R_{ss}}_{\text{새 정상상태}}=\frac{\underbrace{R_0}_{\text{기저값}}}{\underbrace{S(C_{ss})}_{\text{loss 촉진}}}
\end{aligned}
$$

$$
\begin{aligned}
\underbrace{\Delta R_{M1}}_{\text{M1 변화}}&=\underbrace{R_0}_{\text{기저값}}\underbrace{I_{max}}_{\text{최대억제}}\\
\underbrace{\Delta R_{M2}}_{\text{M2 변화}}&=\frac{\underbrace{R_0}_{\text{기저값}}\underbrace{I_{max}}_{\text{최대억제}}}{\underbrace{1-I_{max}}_{\text{잔여 loss}}}\\
\underbrace{\Delta R_{M3}}_{\text{M3 변화}}&=\underbrace{R_0}_{\text{기저값}}\underbrace{E_{max}}_{\text{최대촉진}}\\
\underbrace{\Delta R_{M4}}_{\text{M4 변화}}&=\frac{\underbrace{R_0}_{\text{기저값}}\underbrace{E_{max}}_{\text{최대촉진}}}{\underbrace{1+E_{max}}_{\text{촉진 보정}}}
\end{aligned}
$$

> ⚠️ **Model 2 경계 거동 — $I_{max}\to 1$에서 발산**
> Model 2의 최대 변화량은 분모에 $(1-I_{max})$가 있어서 $I_{max}$가 1에 가까워질수록 **무한대로 발산**합니다.
>
> $$
> \underbrace{\Delta R_{M2,\text{max}}}_{\text{M2 최대 변화}}
> =
> \frac{\underbrace{R_0}_{\text{기저값}}\,\overbrace{I_{max}}^{\to\,1}}{\underbrace{1-I_{max}}_{\to\,0}}
> \;\xrightarrow[I_{max}\to 1]{}\;
> \overbrace{\infty}^{\text{발산}}
> \quad \text{[Gabrielsson \& Weiner 5e p.241]}
> $$
>
> 이건 수학적 호기심이 아니에요. **소실 경로가 완전히 차단되면 $k_{in}$이 계속 들어오는데 빠질 길이 없어서 response pool이 무한히 쌓이는 거예요.** 욕조 비유로 — 수도꼭지는 계속 트는데 배수구를 완전히 막으면 결국 흘러넘칩니다.
>
> → 그래서 임상에서 Model 2 약물(예: PPI에 의한 위 $H^+$ 축적, loop 이뇨제 차단 시 체액 정체, COX 억제 시 prostanoid 축적의 일부 측면)이 **고용량에서 saturation·toxicity를 일으키는 구조적 이유**가 여기 있어요. 실제로는 $I_{max}<1$이 일반적이지만, **모델 적합 중 $I_{max}$가 1에 매우 가깝게 수렴하면 ⓐ misspecification 신호이거나 ⓑ saturation 임계 진입 신호**입니다 — 어느 쪽이든 cross-check가 필요합니다 [Gabrielsson \& Weiner 5e pp.240–241].
>
> Model 4의 $\Delta R_{M4,\text{max}}=R_0\,E_{max}/(1+E_{max})$는 반대로 $E_{max}\to\infty$여도 **분모가 같이 자라서 $R_0$에서 멈춥니다** — 즉 baseline 아래로 갈 수 있어도 0을 넘어 음수로 내려가진 않아요. **두 모델의 경계 거동이 비대칭**이라는 점이 Models 2와 4의 본질적 차이입니다.

네 모델은 **같은 물탱크에 붙은 네 가지 장치**예요 — 수원 밸브를 잠그느냐, 배수구를 막느냐, 수원을 키우느냐, 배수구를 더 여느냐. 어느 쪽이냐에 따라 최종 수위와 거기까지 가는 속도가 둘 다 달라집니다.

### C. 구조적 필요성

네 모델의 차이는 "반응이 올라가느냐 내려가느냐"가 아니에요. **약물이 input을 바꾸느냐, output을 바꾸느냐**가 진짜 차이입니다. Models 1·3은 0차 input term을 건드리니까 시간 상수가 $1/k_{out}$으로 유지돼요. Models 2·4는 1차 loss term을 건드리니까 effective time constant가 농도에 따라 달라집니다. → 그래서 **$t_{ss}$ 거동이 작용 부위를 가려낼 수 있어요** — 단, PK가 더 느린 시계가 아닐 때만 그렇습니다.

> ⚠️ 하향 반응은 Model 1과 Model 4 둘 다에서 생길 수 있어요. 반응 방향만 보고 모델을 결정하지 말고, 시간 경과 패턴을 같이 보세요.

> 🔑 **5분 구조 압축**: "응답 방향"과 "$t_{ss}$가 용량 의존적이냐"의 조합으로 4개 칸 중 하나를 먼저 좁힙니다. PD7 Fig 7.1에서는 **하강 반응 + 용량 의존적 $t_{ss}$ 단축**이라는 조합이 Model 4를 지지합니다.

> 📊 **개념 도식**: 생산 측 모델은 주로 반응 크기를 바꾸고, 소실 측 모델은 **반응 크기와 겉보기 반응 속도를 동시에** 바꿉니다.

**이번 카드 핵심내용**: ① 반응 방향만 보고 모델 이름을 붙이면 안 돼요. 약물 함수가 input에 붙었는지 output에 붙었는지를 봐야 합니다. ② 하강 반응이 보여도 Model 1뿐 아니라 Model 4 가능성도 같이 의심하세요. ③ 반응 방향만으로 모델 라벨을 결정하면 $t_{ss}$, $R_{ss}$, 최대 효과 해석이 줄줄이 어긋납니다.

<!-- SLIDE_START: M3 | title: tss / Peak-Shift Mechanism Discrimination -->
<!-- SECTION_CORE: SC-05 -->
## Card 3 — $t_{ss}$ / Peak-Shift Mechanism Discrimination

앞 카드에서 네 가지 작용 부위 칸을 만들었어요. 이번엔 **데이터에서 그 칸 중 어느 것인지 가려내는 첫 진단 신호**를 다룹니다.

> **거장의 시각**
> $t_{ss}$와 peak shift를 결정적 증거로 쓰면 PD9 Fig 9.5 같은 반례 앞에서 모델 선택 근거가 무너져요. 이 신호를 **"가설 생성기"**로 쓰고 PK rate-limiting, dose range, noise, 비선형성을 동시에 지우면, 보고서에서 방어할 수 있는 구조 결론이 됩니다.

### A. 형식적 정의 + 진단 변수

$t_{ss}$는 response pool이 새 균형에 도달하는 시간 척도예요. Peak shift는 용량을 늘렸을 때 peak 시간이 어떻게 움직이느냐고요. 둘 다 **작용 부위와 clock 위치를 추정하는 보조 신호**입니다 [G&W pp.247–251, 778–783; R&T p.243].

| 진단 변수 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $t_{ss}$ | time | 새 정상상태에 접근하는 시간 | $k_{out}$, effective $k_{out}$, PK clock, 설계 해상도 |
| Peak time | time | 최대 반응이 나타나는 시점 | 분포 지연, system turnover, PK input profile |
| Dose range | dose | 비선형성을 노출하는 설계 폭 | 좁은 범위, saturation, 모델에 안 넣은 비선형성 |
| Response noise | response unit | 진단 신호를 흐리는 관측 변동 | assay noise, sampling sparsity, 생물학적 변동 |

> 💡 $t_{ss}$는 **어디를 더 봐야 할지 알려주는 신호이지, 어디서 멈출지 알려주는 판결문이 아닙니다.**

### B. 핵심 추론

| 관찰 | 1차 기전 가설 | 주의사항 |
|---|---|---|
| 용량 간 유사한 $t_{ss}$ | 생산 측: Model 1 또는 3 | PK rate-limiting이나 sampling 해상도 부족에 가려질 수 있음 |
| 용량에 따라 $t_{ss}$ 단축/연장 | 소실 측: Model 2 또는 4 | PK가 PD clock보다 빠를 때만 성립 |
| 용량 증가에도 peak shift 없음 | Effect compartment 증명 아님 | PD9 시뮬레이션이 이 과대해석을 직접 경고함 [G&W pp.778–783] |

> ⚠️ 모든 모델을 Model 1/3처럼 취급해 초기 반응 기울기에서 $k_{out}$을 추정하지 마세요. Models 2/4에서는 초기·겉보기 기울기가 $I(C)$ 또는 $S(C)$에 의해 **용량 의존적으로 스케일됩니다** [G&W p.251].

### C. 실용적 판정 규칙

$t_{ss}$와 peak shift는 **선별(triage) 도구**예요. 최소 하나 이상의 추가 근거를 같이 봐야 합니다.

| 지금 짚는 것 | → | 후속 작업 | 이유 |
|---|---|---|---|
| 넓은 dose range 필요성 | → | 비선형 약물 함수 평가 | 좁은 범위에서는 $H(C)$ 거동이 숨음 |
| 반복 투여/washout 데이터 | → | system recovery clock 평가 | turnover와 effect site 분리 |
| production vs loss prior | → | model family 정당화 | $t_{ss}$만으로는 기전 확정 불충분 |
| PK clock 확인 | → | duration 공식 적용성 | PK가 더 느리면 PD clock 진단 가려짐 |
| effect compartment 대안 | → | M7 감별 위기 | peak shift 부재가 link 증거는 아님 |

$t_{ss}$는 **공항 보안검색의 금속탐지기**랑 같아요 — 경고음이 울리면 어디를 더 봐야 할지 알려주지만, 그것만으로 물건의 정체가 결정되지는 않습니다.

> 🔑 **Mirror-slope 시그너처**: PD7 Fig 7.1에서 6,400 unit 용량에서 추정된 $k_{out}\approx0.6\;h^{-1}$, 160,000 unit 용량에서는 $k_{out}\approx1.6\;h^{-1}$. **system 파라미터가 용량에 따라 단조 변하면 생물학이 아니라 misspecification artifact**를 의심합니다.

**이번 카드 핵심내용**: ① $t_{ss}$가 용량에 따라 변하면 loss-side 또는 wrong-clock 후보를 떠올리세요. ② peak shift가 안 보인다고 effect compartment가 확정되는 게 아닙니다 — 설계 폭, 비선형성, PK clock이 더 셀 수 있어요. ③ $t_{ss}$를 기전의 결정적 증거로 과대해석하면 PD9 반례와 mirror-slope 오독 앞에서 무너집니다.

<!-- SLIDE_START: M4 | title: Imax/Emax Multiplier Semantics + Linear PK ≠ Linear PD -->
<!-- SECTION_CORE: SC-06 -->
## Card 4 — $I_{max}/E_{max}$ Multiplier Semantics + Linear PK ≠ Linear PD

앞 카드에서 시간 신호의 한계를 정했어요. 이번엔 효과 크기 파라미터가 **어떤 scale에 붙는지**를 정합니다.

> **거장의 시각**
> $E_{max}=0.65$ 같은 숫자를 이름만 보고 비교하면 drug potency와 system-baseline multiplier를 뒤섞게 됩니다. 수식에서 $E_{max}$가 **절대 거리인지 $R_0$에 곱해지는 배율인지** 먼저 확인하면 cross-model 비교가 안전해져요.

### A. 의미 잠금 + 수식

$E_{max}$는 모델마다 단위와 의미가 다릅니다. Direct $E_{max}$ 모델에서는 baseline으로부터의 절대 거리고, turnover 모델에서는 이미 $k_{in}/k_{out}$ 비율로 정해진 system baseline에 곱해지는 배율이에요 [G&W p.246].

| 모델 형태 | 파라미터 의미 | 단위 / 해석 |
|---|---|---|
| Direct additive $E_{max}$ | $E=E_0+\frac{E_{max}C^n}{EC_{50}^n+C^n}$ | $E_{max}$는 반응 단위 — **절대 거리** |
| Direct reparameterized multiplier | $E=E_0(1+\frac{E_{max}C^n}{EC_{50}^n+C^n})$ | $E_{max}$는 **무차원 배율** |
| Turnover Model 3 | $R_{ss}=R_0(1+\frac{E_{max}C^n}{EC_{50}^n+C^n})$ | $E_{max}$는 **system turnover를 통한 배율** |

$$
\underbrace{E}_{\text{관찰효과}}
=
\underbrace{E_0}_{\text{기저효과}}
+
\underbrace{\frac{\overbrace{E_{max}C^n}^{\text{효과구동}}}{EC_{50}^n+C^n}}_{\text{절대효과}}
$$

$$
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

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $E$ | response unit | 관찰 효과 | 농도, baseline, 모델 형태 |
| $E_0$ | response unit | direct model baseline | 질병 상태, baseline drift |
| $R_{ss}$ | response unit | 약물 효과 하 새 정상상태 | $R_0$, $I(C)$/$S(C)$, $k_{out}$ |
| $E_{max}$ | response unit 또는 무차원 | 절대 거리 또는 배율 | 파라미터화, turnover 구조 |
| $\Delta R/R_0$ | 무차원 | scale-normalized effect | baseline과 최대 변화량 |

같은 "높이 10"이라도 **센티미터인지 층수인지** 모르면 비교가 불가능해요. $E_{max}$도 어떤 축 위의 거리인지 먼저 봐야 합니다.

### B. 선형 PK가 선형 PD를 의미하지는 않음

**Methylprednisolone**(부신피질호르몬; i.v. phosphate-prodrug)이 대표 사례예요. 정확한 용량 시리즈는 16 / 31 / 63 / 125 / 250 / 500 / 1000 mg. 혈장 AUC는 용량에 거의 비례적으로 증가하지만, **lymphocyte 반응은 비례적으로 증가하지 않습니다** — 고용량에서 PD plateau에 가까워지기 때문이에요 [R&T pp.256–258]. → 그래서 **AUC가 선형이라고 반응까지 선형은 아니다**라는 사실의 대표 사례입니다.

R&T 본문(p.256)이 이 함정을 단호하게 못박아둡니다 — *"Dose linearity in pharmacokinetics does not result in dose linearity in pharmacodynamics. That is almost never the case."*

전신 노출이 곧 작용 부위 노출은 아니라는 disconnect 사례도 같은 챕터에 있어요. **Rosuvastatin**(HMG-CoA 환원효소 억제제; 고지혈증 치료제)의 OATP1B1 polymorphism은 plasma AUC를 substantially 변화시키지만 cholesterol synthesis 반응은 modestly 변합니다(Fig 8-28/8-29 맥락). 별도의 turnover 모델이 아니라 exposure-response disconnect의 보조 관찰이에요 [R&T pp.258–259].

> ⚠️ **헷갈림 방지**: "용량 비례적 노출이니까 용량 비례적 반응을 지지한다"는 결론을 쓰기 전에 **Hill curve의 어느 영역에 있는지 먼저 확인**하세요.

> 🔑 **비교 규칙**: 모델·연구·화합물 간 효과 파라미터를 비교할 때는 항상 $\Delta R/R_0$로 변환한 뒤 비교합니다.

> 📖 **G&W 5e p.246, Fig 3.40**: 같은 파라미터 이름이 모델 계열마다 같은 수직 반응 거리를 의미하지 않는다는 걸 보여주는 그림입니다. → 그래서 $E_{max}$ 라벨만 보고 모델 간 비교를 하면 의미가 어긋난다는 사실의 시각화예요.

**이번 카드 핵심내용**: ① $E_{max}$ 추정치를 보고할 때는 절대 거리인지 baseline 배율인지를 명시해야 합니다. ② 용량 비례적 AUC를 봐도 PD 비례성은 Hill curve의 어느 구간에 있느냐에 달려 있어요. ③ $E_{max}$ 라벨만 보고 in vitro potency, 임상 $EC_{50}$, model-derived effect size를 비교하면 허위 비교가 됩니다.

<!-- SLIDE_START: M4_EXT | title: Pool/Precursor Multi-Stage Indirect Response (Sharma-Jusko 1998) -->
<!-- SECTION_CORE: SC-06b -->
## Card 4-보강 — Pool/Precursor 다단계 간접반응 (Sharma-Jusko 1998)

앞 카드까지가 **단일 stage** 4-model taxonomy(Models I–IV)였어요. 그런데 실제 생물학에서는 약물이 건드리는 자리와 우리가 측정하는 반응 사이에 **상류 pool이 하나 더** 있는 경우가 많습니다 — corticosteroid가 mRNA를 만들고 그게 enzyme을 만드는 식으로요. 이 한 단계가 들어가는 순간 dynamics가 4-model과 다르게 움직입니다.

> **거장의 시각**
> Single-stage Models I–IV로 모든 indirect response를 다루려고 하면 **상류 pool의 turnover가 만들어내는 추가 지연을 $k_{out}$이나 $k_{e0}$가 통째로 흡수**하게 됩니다. 그러면 $k_{out}$이 system biology가 아니라 cascade depth를 가리키게 돼요. **단일 stage가 충분한가, 아니면 precursor pool을 명시해야 하는가**를 첫 번째로 묻는 게 cascade 약물군(steroid, GH, EPO, cortisol axis, methotrexate 등)의 출발점입니다 [Sharma & Jusko 1998].

### A. 구조적 정의 — 2단계 cascade

기본 골격은 두 개의 풀이 직렬로 연결된 구조입니다. **상류 pool $P$**가 0차로 생산되고 1차로 $R$로 전환되며, **하류 반응 $R$**가 1차로 소실됩니다.

$$
\underbrace{\frac{dP}{dt}}_{\text{precursor 변화율}}
=
\underbrace{k_{in}}_{\text{0차 생산}}
-
\overbrace{\underbrace{k_p}_{\text{전환 clock}}\,\underbrace{P}_{\text{precursor pool}}}^{\text{precursor 소실 = R로 전환}}
\quad \text{[Sharma \& Jusko 1998 Eq 1]}
$$

$$
\underbrace{\frac{dR}{dt}}_{\text{response 변화율}}
=
\overbrace{\underbrace{k_p}_{\text{전환 clock}}\,\underbrace{P}_{\text{precursor}}}^{\text{R로 들어오는 양}}
-
\underbrace{k_{out}\,R}_{\text{response 소실}}
\quad \text{[Sharma \& Jusko 1998 Eq 2]}
$$

기저상태(약물 없음, $dP/dt=dR/dt=0$)에서:

$$
\underbrace{P_0}_{\text{precursor 기저}}
=
\frac{\underbrace{k_{in}}_{\text{생산}}}{\underbrace{k_p}_{\text{전환 clock}}},
\qquad
\underbrace{R_0}_{\text{반응 기저}}
=
\frac{\underbrace{k_p\,P_0}_{\text{R 유입속도}}}{\underbrace{k_{out}}_{\text{소실 clock}}}
=
\frac{\underbrace{k_{in}}_{\text{생산}}}{\underbrace{k_{out}}_{\text{소실 clock}}}
$$

즉 — **response의 기저값은 single-stage와 같지만, 그 baseline에 도달하는 동역학은 두 개의 시계 $k_p$와 $k_{out}$의 cascade**입니다.

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $P$ | precursor unit | 상류 pool (e.g., mRNA, enzyme precursor, immature cell) | 합성/전환 속도, 약물 작용 부위 |
| $R$ | response unit | 측정 대상 반응 (e.g., enzyme activity, mature cell count) | precursor 공급, 자체 소실 |
| $k_{in}$ | precursor·time⁻¹ | precursor 0차 생산 속도 | 합성 억제/촉진 |
| $k_p$ | time⁻¹ | precursor → response 전환 clock | maturation, 효소 활성화, 단계 진행 |
| $k_{out}$ | time⁻¹ | response 자체 소실 clock | response biology |
| $P_0$, $R_0$ | 단위 | 두 pool의 기저값 | $k_{in}/k_p$, $k_{in}/k_{out}$ |

### B. 약물 작용 자리 — Pool/Precursor 확장 (관행적 Models V–VIII 명명)

약물 함수를 어느 항에 곱하느냐에 따라 cascade indirect models의 변형들이 정의됩니다. 단일 stage Models I–IV가 "production vs loss × inhibit vs stimulate"의 4칸이었던 것처럼, precursor 확장은 **상류 pool 또는 전환 단계**에 약물이 들어오는 추가 변형을 만듭니다.

> 📖 **명명법 출처 정정 (2차 검토 1-4 반영)**
> Sharma & Jusko (1998, *Br J Clin Pharmacol* 45:229–239) **원 논문은 위 precursor 확장에 'Model V/VI/VII/VIII'이라는 명시적 번호를 부여하지 않았습니다**. 원 논문은 "indirect response models with precursor compartments"라는 일반 서술과 cell/enzyme schematic으로 다룹니다.
>
> 본 자료에서 사용하는 **Models V–VIII 번호는 후속 표준 문헌(Jusko 그룹의 후속 review, Mager-Wyska-Jusko의 PK/PD 교과서 등)에서 관행적으로 굳어진 명명**입니다. 학습자가 1차 문헌(Sharma-Jusko 1998)에서 직접 'Model V'를 찾으면 그 표기는 없으니, **"Sharma-Jusko의 precursor 확장 (관행적으로 Models V–VIII로 불림)"** 으로 이해하는 것이 정확합니다. 이 자료에서는 학습 편의를 위해 표 행 라벨에 V/VI/VII/VIII를 유지하되, **인용 시 출처를 정확히 표기**합니다.

| Model (관행적 명명) | 약물 작용 자리 | ODE 변화 | 대표 사례 |
|---|---|---|---|
| **V** (관행) | precursor 생산 억제 | $dP/dt = k_{in}\cdot I(C) - k_p P$ | corticosteroid → tyrosine aminotransferase mRNA 억제 |
| **VI** (관행) | precursor 생산 촉진 | $dP/dt = k_{in}\cdot S(C) - k_p P$ | erythropoietin precursor 자극 |
| **VII** (관행) | precursor → response 전환 억제 | $dR/dt = k_p P\cdot I(C) - k_{out} R$ | 효소 활성화 단계 차단 |
| **VIII** (관행) | precursor → response 전환 촉진 | $dR/dt = k_p P\cdot S(C) - k_{out} R$ | maturation 가속 |

대표적으로 Model V(상류 합성 억제, 관행적 명명)의 두 식을 명시적으로 쓰면:

$$
\underbrace{\frac{dP}{dt}}_{\text{precursor 변화}}
=
\overbrace{\underbrace{k_{in}}_{\text{생산}}\,\underbrace{I(C)}_{\text{억제함수}}}^{\text{약물 작용 자리}}
-
\underbrace{k_p\,P}_{\text{전환 = R로 이동}}
$$

$$
\underbrace{\frac{dR}{dt}}_{\text{response 변화}}
=
\underbrace{k_p\,P}_{\text{R 유입 — 약물 직접 작용 아님}}
-
\underbrace{k_{out}\,R}_{\text{R 소실}}
$$

→ 그래서 **약물이 상류에 작용해도 측정되는 $R$의 변화는 $1/k_p$만큼 더 지연**됩니다. 이게 cascade의 본질이에요.

### C. 단일 stage와의 핵심 차이 — 두 개의 지연 clock

| 비교 기준 | Single-stage Model I (생산 억제) | Pool/Precursor Model V (상류 생산 억제) |
|---|---|---|
| 약물 작용 후 첫 효과까지 | $\sim 1/k_{out}$ | $\sim 1/k_p + 1/k_{out}$ (cascade lag) |
| Onset 곡선 모양 | exponential approach | **sigmoid 모양** (초기 평탄 구간 존재) |
| 약물 중단 후 회복 | $1/k_{out}$ 단일 clock | 두 clock의 deconvolution 필요 |
| $k_{out}$ 단독 추정 | 종말 회복 기울기로 가능 | $k_p$와 함께 fit 안 하면 흡수됨 |

> 🔑 **Sigmoid onset 시그너처**: Pool/precursor 약물의 약리효과는 **투약 직후 즉시 시작하지 않고 lag-then-rise 패턴**을 보입니다. 이게 보이는데 single-stage Model I를 적합하면, 추정된 $k_{out}$이 **biology가 아니라 cascade depth($1/k_p$)의 일부를 흡수**해요. → 임상에서 "측정된 $k_{out}$이 알려진 enzyme half-life보다 작게 나온다"가 cascade misspecification의 시그너처입니다.

> 💼 **실무 인사이트**: Corticosteroid 약리(prednisolone → tyrosine aminotransferase, methylprednisolone → lymphocyte trafficking 등)의 **표준 PD 골격이 바로 Pool/Precursor**예요. Single-stage Model I로 적합하면 effect onset이 너무 빠르게 나와요. **Methylprednisolone lymphocyte 사례(R&T 5e pp.256–258)에서 plateau 진입을 제외하면, residual lag의 상당 부분이 trafficking precursor의 dynamics**입니다.

### D. 다른 카드들과의 연결

Pool/precursor 구조는 이 세션의 다른 카드들과 직접 연결됩니다.

- **Card 1 (Turnover Foundation)** → 단일 stage의 $R_0=k_{in}/k_{out}$ 비율 원리가 두 stage로 확장됩니다 ($P_0 = k_{in}/k_p$, $R_0 = k_{in}/k_{out}$).
- **Card 2 (4-Model Taxonomy)** → "production vs loss × inhibit vs stimulate"의 4칸이 **상류 pool 위에서 8칸으로 확장**됩니다.
- **Card 7 (Apex — Turnover vs Effect Compartment)** → cascade lag와 effect compartment $k_{e0}$ lag는 **다시 비식별성 후보 쌍**이에요. 둘 다 sigmoid onset을 만들 수 있습니다.
- **Card 8 (PK clock vs PD clock)** → cascade depth가 커지면 **추가적인 PD clock**이 생기고, 이게 PK clock보다 느려지면 duration이 cascade에 의해 결정됩니다.

> 📖 **1차 문헌 (정정)**: Sharma A, Jusko WJ. "Characteristics of indirect pharmacodynamic models and applications to clinical drug responses." *Br J Clin Pharmacol.* 1998;45(3):229–239. DOI: 10.1046/j.1365-2125.1998.00676.x. — 이 논문이 precursor pool을 포함하는 indirect response의 일반 framework를 제시했고, single-stage Models I–IV와의 비교를 데이터로 보여줍니다. **단, 'Models V–VIII'이라는 명시적 번호 명명은 후속 문헌의 관행이며, 원 논문의 표기는 'indirect response models with precursor compartments'입니다.**

> 📖 **교과서 연결**: 본 cascade 구조는 Gabrielsson \& Weiner 5e에서 PD13 Model III 맥락에서 한 차례 언급되며(소위 "transduction with precursor"), 본 자료 **Ch.12(Effect Compartment / 내성 / Transduction)**의 transit chain 골격과 **연속체**를 형성합니다.

> ⚠️ **자주 빠지는 함정**: 단일 dose group 데이터에서 Pool/Precursor와 single-stage + effect compartment 조합이 사실상 같은 곡선을 만들 수 있어요. **Card 7의 비식별성 위기가 cascade depth 결정에도 그대로 적용**됩니다. 어느 구조를 고를지는 mechanism prior(상류 pool이 측정 가능한가, 알려진 enzyme/cell turnover가 있는가)와 다중 dose / 반복투여 설계가 결정합니다.

**이번 카드 핵심내용**: ① 약물이 측정되는 반응으로 가기 전에 상류 pool을 거치면 cascade lag $1/k_p$가 추가됩니다. ② Single-stage Models I–IV로 cascade 약물(steroid, EPO precursor, maturation-driven biomarker 등)을 적합하면 $k_{out}$이 cascade depth를 흡수해서 system biology 해석이 어긋납니다. ③ Sigmoid onset 시그너처가 보이면 Pool/Precursor 후보를 먼저 의심하고, single-stage + effect compartment와의 감별은 Card 7의 비식별성 원칙을 따릅니다.

<!-- SLIDE_START: M5 | title: Graphical Initial Parameter Estimation + Blocking Dose / DRT -->
<!-- SECTION_CORE: SC-07 -->
## Card 5 — Graphical Initial Parameter Estimation + Blocking Dose / DRT

앞 카드에서 효과 scale을 정해뒀어요. 이번엔 그 scale 위에서 **NONMEM이 시작할 파라미터 자릿수를 손으로 먼저 잡아두는 작업**을 합니다.

> **거장의 시각**
> 초기값을 단순 guess로 두면 optimizer가 비식별성 골짜기에서 가짜 수렴을 내놔도 알아채기 어려워요. Raw response-time plot에서 $R_0$, $k_{out}$, potency, maximal effect의 자릿수를 먼저 잡으면 **적합된 파라미터를 sanity check할 기준선**이 생깁니다.

### A. 형식적 정의 + 최소 graphical 작업 흐름

Graphical estimation은 "진짜 모델링 전에 거치는 번거로운 과정"이 아니에요. **첫 번째 기전적 감사(mechanism audit)**입니다 [G&W pp.247–251].

| 단계 | 근거/가정 | 산출물 |
|---|---|---|
| 1 | 투약 전 또는 vehicle baseline | $R_0$ 추정 |
| 2 | 종말 회복 곡선, blocked-synthesis 감소 구간, log-linear 복귀 | $k_{out}$ 추정 |
| 3 | baseline과 time constant 분리 | $k_{in}=R_0\cdot k_{out}$ |
| 4 | 2–3개 용량 수준의 정상상태 또는 peak 반응 | $IC_{50}/EC_{50}$, $I_{max}/E_{max}$ 출발 자릿수 |
| 5 | 초기값 감사 후 | nonlinear mixed-effects estimation 실행 |

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $R_0$ | response unit | pre-dose baseline | 질병 상태, assay baseline, drift |
| $k_{out}$ | time⁻¹ | response recovery clock | system turnover, feedback, misspecification |
| $k_{in}$ | response·time⁻¹ | production rate | $R_0\cdot k_{out}$, 합성 변화 |
| $IC_{50}/EC_{50}$ | concentration | potency scale | 노출 범위, 기전, 작용부위 농도 |
| $I_{max}/E_{max}$ | 무차원 또는 response unit | maximal perturbation | model family, baseline scaling |

> 💡 초기값은 **숫자를 입력하는 작업이 아니라 식별성을 감사하는 작업**이에요.

### B. Blocking-dose 유사 방법

**Warfarin** blocking-dose 분석은 $k_{out}$을 직접 뽑아내는 임상적 등가 방법이에요. 합성이 거의 완전히 차단되면 prothrombin complex activity가 다음을 따릅니다.

$$
\underbrace{\frac{dA}{dt}}_{\text{활성 변화}}
=-\underbrace{k_t}_{\text{소실 clock}}\,\underbrace{A}_{\text{잔여 활성}}
\quad \text{[R&T Eq 8-6; R&T pp.244–246]}
$$

비차단 구간에서는 합성 속도를 재구성할 수 있어요.

$$
\underbrace{R_{syn}}_{\text{합성속도}}
=
\underbrace{\frac{A_2-A_1}{\Delta t}}_{\text{관찰변화}}
+
\overbrace{\underbrace{k_t}_{\text{소실 clock}}\frac{\underbrace{A_1+A_2}_{\text{평균 활성}}}{2}}^{\text{소실보정}}
\quad \text{[R&T Eq 8-7; R&T p.247]}
$$

이게 hysteretic 반응-시간 기록을 **억제-농도 관계로 변환**하는 방법입니다 [R&T pp.244–247]. Blocking-dose는 **공장 입구를 거의 완전히 막아놓고 창고가 비는 속도를 재는 실험**과 같아요 — 들어오는 물량을 잠그면 배출 시계가 드러납니다. → 그래서 warfarin이 **합성 억제(Model 1) 기전의 임상 prototype**으로 자주 인용되는 거예요.

### C. DRT(Dose-Response-Time) 맥락

DRT 분석은 농도 데이터가 없어도 baseline, slope, potency, maximal effect를 추론할 수 있어요. 다만 full PK/PD 모델링보다 거친 역문제예요. **노출 데이터가 있으면 DRT로 대체하지 마세요** — DRT는 후퇴 대안 또는 교육적 가교로 두면 됩니다 [G&W pp.272–275].

> 💼 **실무 인사이트**: 수동 초기 추정은 NONMEM 이전 시대의 향수가 아닙니다. **기전적 감사**예요. 기울기·baseline·blocking-dose 논리가 적합된 파라미터를 대략적으로라도 지지하지 못하면, optimizer는 **잘못된 문제를 깔끔하게 풀고 있을 가능성**이 높습니다.

PD5 사례를 봅시다. Compound A의 PK가 먼저 잡힌 상태($V=40\;\text{L}$, $K=0.9\;h^{-1}$)에서 4000/16000/80000 unit의 6시간 infusion 데이터를 받아요. Pre-infusion baseline에서 $R_0$를 읽고, post-infusion 회복 곡선의 semi-log plot 종말 기울기로 $k_{out}\approx0.43\;h^{-1}$을 얻고, $k_{in}=R_0\cdot k_{out}$로 production rate 출발점을 잡습니다. 세 용량의 plateau 응답에서 $IC_{50}\approx95$, $I_{max}\approx0.65$의 자릿수까지 잡은 뒤에야 NONMEM 추정에 들어가요(Table 5.1).

> ⚠️ 터무니없는 초기값이 필요한 모델은 대부분 **graphical 단계를 건너뛰었거나 잘못된 clock을 사용한 경우**예요. Random effects를 확장하기 전에 출발점의 생물학을 먼저 수정하세요.

**이번 카드 핵심내용**: ① NONMEM 돌리기 전에 $R_0$, $k_{out}$, potency, maximal effect의 자릿수를 손으로 먼저 잡으세요. ② 적합값이 graphical 자릿수에서 한 order 이상 벗어나면 비식별성이나 misspecification이 작동 중이라는 신호입니다. ③ 초기값을 optimizer에게 통째로 위임하면 가짜 수렴이 후속 임상시험 설계까지 오염시킵니다.

<!-- SLIDE_START: M6 | title: Irreversible Drug Action + Target Consumption -->
<!-- SECTION_CORE: SC-08 -->
## Card 6 — Irreversible Drug Action + Target Consumption

앞 카드까지가 가역적 turnover의 파라미터를 잡는 일이었다면, 이번엔 **"drug=0이면 effect=0"이라는 가정 자체가 깨지는 경우**를 분리합니다.

> **거장의 시각**
> 혈장 반감기를 그대로 effect duration으로 외삽하면 aspirin, omeprazole, paclitaxel 같은 사례에서 결정적 오류가 나요. **약물이 표적이나 세포 pool을 소비했는지** 먼저 물어보면, 회복 시계를 drug PK가 아니라 target replacement나 cell regrowth에 배정할 수 있습니다.

### A. 핵심 비가역 방정식

가역적 turnover에서는 system이 반응을 계속 생산·제거하니까 baseline으로 돌아옵니다. 그런데 비가역 작용에서는 **약물 노출 기간 동안 반응 단위·표적·세포가 영구적으로 제거**됩니다 [G&W pp.256–260; R&T pp.251–252].

$$
\underbrace{\frac{dR}{dt}}_{\text{생존 변화}}
=
-\overbrace{\underbrace{K_{kill}}_{\text{kill potency}}\,\underbrace{C}_{\text{노출}}\,\underbrace{R}_{\text{잔여 pool}}}^{\text{비가역 kill}}
\quad \text{[G&W Eq 3:110; G&W p.257]}
$$

적분 형태의 생존율은:

$$
\underbrace{SF}_{\text{생존분율}}
=
\exp\left(-\overbrace{\underbrace{K_{kill}}_{\text{kill potency}}\cdot\underbrace{AUC}_{\text{누적노출}}}^{\text{누적 kill}}
\right)
\quad \text{[G&W Eq 3:112; G&W p.257]}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $K_{kill}$ | concentration⁻¹·time⁻¹ | 2차 약리작용 상수 | drug-action potency, 표적 민감도 |
| $C$ | concentration | 노출 농도 | PK, dose, distribution |
| $R$ | response/cell/target unit | 잔여 pool | 비가역적 소실, 재성장/대체 |
| $AUC$ | concentration·time | 누적 노출 | dose, clearance, sampling window |
| $SF$ | fraction | 생존 또는 잔여 분율 | $K_{kill}\cdot AUC$ |

비가역 kill은 **스위치를 끄는 게 아니라 전구를 빼내는 것**과 같아요 — 전기가 다시 들어와도 새 전구를 끼우기 전까지 빛은 안 돌아옵니다.

> ⚠️ $K_{kill}$은 2차 약리작용 상수예요. **1차 PK 소실 상수가 아닙니다.** 이 자료에서 $K_{kill}/k_k$는 PD killing이고, $K_{elim}$은 PK elimination입니다.

### B. 표적 소비 사례

| 상황 | 파라미터 변화 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| **Aspirin** 650 mg 경구(NSAID; 항혈소판제; COX-1 비가역 acetylation) | 혈장 반감기는 짧지만 혈소판 기능은 표적 대체에 의존 | → | thromboxane B₂ 억제가 수일 지속 | 표적 대체 시계를 별도 모델링 — → 그래서 **비가역 작용 + 표적 소비의 prototype**입니다 [R&T p.251] |
| **Omeprazole** 40 mg 경구(PPI; H⁺/K⁺-ATPase 비가역 결합; 위산 분비 억제제) | 혈장 반감기 <1 h, proton-pump 결합/재생 동역학 | → | 산분비 억제가 수일 지속 | pump regeneration을 회복 clock으로 설정 — → 그래서 **혈장 반감기 ≪ 효과 지속시간의 사례**입니다 [R&T p.252] |
| **Paclitaxel** 정맥투여(taxane; 미세소관 안정화 항암제) | 혈장 농도 감소가 백혈구 회복보다 훨씬 빠름 | → | 회복에 약 3주 소요 가능 | leukocyte recovery model 필요; Fig 8-22 맥락 (Fig 8-19 아님) — → 그래서 **세포 소비 후 재성장 시계가 PK clock보다 훨씬 느린 사례**입니다 [R&T pp.253–254] |

### C. 세포 성장/사멸 맥락

세포가 증식할 때는 비가역 사멸을 성장 동역학 안에 포함시켜야 해요. Gabrielsson의 cell-growth/kill 프레임워크는 logistic이나 용량-제한 성장에 2차 사멸을 더합니다. $B_{max}\approx30{,}000\;\text{CFU}$가 맥락 앵커예요 [G&W pp.258–260].

> 🔑 **Duration 질문 규칙**: **"drug=0이면 effect=0인가?"**의 답이 NO이면 plasma PK 외에 **target replacement clock을 별도로 모델링**합니다.

### D. 응용 사례 — Friberg-Karlsson 항암제 호중구 감소 모델 (2002)

**Paclitaxel**의 백혈구 회복(약 3주)을 위 표에서 한 줄로 짚었지만, 실제 임상에서 항암제 myelosuppression을 모델링하는 **현대 표준 골격**은 한 단계 더 정교합니다. Friberg와 Karlsson(2002)이 제안한 모델은 **이 세션과 다음 세션(Ch.12 transit chain)의 모든 도구를 한 자리에 결합**합니다 — 비가역 cell kill(이 카드), transit chain을 통한 maturation lag(Ch.12), feedback rebound(Card 1 영역), 그리고 약물 농도 함수 $E_{drug}(C)$가 모두 들어가요.

**구조**: 5개 compartment cascade — 증식 pool $Prol$ → transit 1 → transit 2 → transit 3 → 순환 pool $Circ$ (측정 대상). 약물은 $Prol$에서 cell을 죽이고, $Circ$의 감소가 다시 $Prol$의 증식을 자극(feedback)합니다 [Friberg et al., *J Clin Oncol* 2002].

$$
\underbrace{\frac{dProl}{dt}}_{\text{증식 변화}}
=
\overbrace{\underbrace{k_{prol}\,Prol}_{\text{1차 증식}}\,\underbrace{\bigl[1-E_{drug}(C_p)\bigr]}_{\text{약물 kill 보정}}\,
\underbrace{\left(\tfrac{Circ_0}{Circ}\right)^{\gamma}}_{\text{feedback 보정}}}^{\text{net 증식 — drug × feedback}}
-
\underbrace{k_{tr}\,Prol}_{\text{maturation으로 유출}}
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

약물 효과 함수 $E_{drug}$는 linear($\text{slope}\cdot C_p$) 또는 $E_{max}$ 형태로 적합합니다.

$$
\underbrace{E_{drug}(C_p)}_{\text{약물 kill 함수}}
=
\underbrace{\text{slope}\cdot C_p}_{\text{선형}}
\quad\text{또는}\quad
\frac{\overbrace{E_{max}\,C_p}^{\text{포화 가능}}}{\underbrace{EC_{50}+C_p}_{\text{Hill }n=1}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $Prol$ | cell unit | 골수 증식 cell pool (약물 작용 대상) | $k_{prol}$, 약물 kill, feedback |
| $T_1$, $T_2$, $T_3$ | cell unit | maturation transit pool (3단계) | $k_{tr}$ — maturation clock |
| $Circ$ | cell·µL⁻¹ | 측정되는 순환 cell (예: 호중구) | $T_3$ 유입, $k_{circ}$ 소실 |
| $k_{prol}$ | time⁻¹ | 증식 1차 속도 **(모델 구조 제약: $k_{prol}=k_{tr}$)** | 골수 turnover |
| $k_{tr}$ | time⁻¹ | maturation transit clock | $MTT = 4/k_{tr}$ |
| $k_{circ}$ | time⁻¹ | 순환 cell 자체 소실 **(모델 구조 제약: $k_{circ}=k_{tr}$)** | 순환 cell 수명 |
| $Circ_0$ | cell·µL⁻¹ | 약물 투여 전 baseline | 환자 기저 골수 기능 |
| $\gamma$ | 무차원 | feedback 강도 (rebound 곡률) | 골수 over-shoot 정도 |

> ⚠️ **System parameter 제약은 "흔한 관행"이 아니라 "원 논문 모델 구조의 일부" (2차 검토 1-3 반영)**
> 위 표에서 $k_{prol}=k_{tr}$과 $k_{circ}=k_{tr}$는 단순히 "흔히 고정되는 편의적 선택"이 아닙니다. **Friberg et al. 2002 원 논문(Eq 1–3)의 모델 정의 자체에 포함된 제약**이에요. 그래야 5개 system parameter($k_{prol}$, $k_{tr,1}$, $k_{tr,2}$, $k_{tr,3}$, $k_{circ}$)가 **하나의 maturation clock $k_{tr}$ (또는 동등하게 $MTT=4/k_{tr}$)으로 축약**되어 식별성이 확보됩니다.
>
> $$
> \overbrace{\underbrace{k_{prol}}_{\text{증식}}=\underbrace{k_{tr,1}}_{\text{transit 1}}=\underbrace{k_{tr,2}}_{\text{transit 2}}=\underbrace{k_{tr,3}}_{\text{transit 3}}=\underbrace{k_{circ}}_{\text{순환 소실}}\equiv k_{tr}}^{\text{모델 정의에 의한 5중 제약}}
> \;\Longrightarrow\;
> \underbrace{MTT}_{\text{mean transit time}}=\underbrace{\frac{n+1}{k_{tr}}=\frac{4}{k_{tr}}}_{n=3\;\text{transit stages}}
> \quad \text{[Friberg \& Karlsson 2002 Eq 1–3]}
> $$
>
> → 그래서 이 제약이 **약물 간 일관성 비교(6개 항암제에서 $MTT$, $\gamma$가 약물에 거의 무관)** 의 정량적 기반이 됩니다. 학생이 이 제약을 "임의 고정"으로 오해하면, NONMEM에서 $k_{prol}$, $k_{tr}$, $k_{circ}$를 독립 추정하려고 시도하다가 **심각한 비식별성과 과대추정**에 빠집니다. **원 논문 그대로 적용할 때만 약물 간 system parameter 일관성이 회수됩니다.**

### Friberg-Karlsson 모델이 가르치는 것

이 모델이 **이 세션 + Ch.12의 모든 도구가 한 곳에 모이는** 자리예요. 한 줄로 꿰면:

- **Card 1 (Turnover 골격)** → $Circ_0$가 baseline pool로 등장하고, feedback이 $k_{out}$ 고정 가정을 위반합니다.
- **Card 2 (4-Model Taxonomy)** → 약물이 증식 항에 곱해지는 구조는 **확장된 Model VII/VIII(전환 억제) 패턴**이에요.
- **Card 4-보강 (Pool/Precursor)** → 증식 pool $Prol$ → transit $T_i$ → 순환 $Circ$는 **3단계 cascade**입니다. Pool/precursor의 다단계 확장.
- **Card 6 (비가역 kill)** → 약물은 $Prol$에서 cell을 비가역적으로 죽입니다 ($E_{drug}$가 net growth rate를 음수로 만들 수 있음).
- **Ch.12 (transit chain)** → 4개 stage($Prol\to T_1\to T_2\to T_3\to Circ$)가 mean transit time $MTT=4/k_{tr}$로 환산됩니다.
- **Card 8 (PK vs PD clock)** → paclitaxel의 PK 반감기는 짧지만, $MTT \approx 7$일(호중구의 경우)이 회복을 지배하는 **PD-rate-limited duration**의 정량 사례입니다.

> 💼 **임상적 활용**: Friberg-Karlsson 모델은 단일 fit으로 **호중구 감소의 nadir 시점, nadir 깊이, 회복 시점**을 모두 예측하고, **dose-intensity / dose-density 결정**(예: dose-dense AC-T 항암 protocol)의 정량 근거가 됩니다. **Docetaxel, paclitaxel, etoposide, 5-FU, vinflunine** 등에서 **$\gamma$, $MTT$가 약물 간에 일관성을 보인다**는 것이 원 논문의 핵심 발견이에요(즉 system parameter는 약물에 거의 무관, drug parameter만 약물별로 차이).

> 🔑 **임상 시그너처**: Friberg-Karlsson 적합에서 보통 $MTT \approx 100{-}140$시간(약 4–6일), $\gamma \approx 0.1{-}0.3$이 호중구의 표준 범위입니다. 적합값이 이 범위를 크게 벗어나면 ⓐ 동반약물 효과, ⓑ 골수 기능 이상, 또는 ⓒ misspecification을 먼저 의심합니다.

> 📖 **1차 문헌 (정정)**: Friberg LE, Henningsson A, Maas H, Nguyen L, Karlsson MO. "Model of chemotherapy-induced myelosuppression with parameter consistency across drugs." *J Clin Oncol.* 2002;20(24):4713–4721. DOI: 10.1200/JCO.2002.02.140. — 이 논문이 위 5-compartment 골격(증식 + 3 transit + 순환)을 정의하고, **$k_{prol}=k_{tr}=k_{circ}$ 제약을 모델 정의의 일부로 도입**하여 식별성을 확보합니다. 이 제약 하에서 6개 항암제(docetaxel, paclitaxel, etoposide, vinflunine, 5-FU, doxorubicin)에서 **$MTT$, $\gamma$ system parameter가 약물에 거의 무관**함을 데이터로 보여줍니다.

> ⚠️ **주의 — 모델 적용 범위**: Friberg-Karlsson은 **세포독성 항암제**의 myelosuppression이 설계 대상이에요. 표적치료제(targeted therapy)나 면역항암제는 작용 기전이 달라서 그대로 적용되지 않습니다. **Lenalidomide의 호중구 감소** 같은 경우는 이 골격을 변형해서 써야 해요.

**이번 카드 핵심내용**: ① 약물이 사라진 뒤에도 효과가 남으면 target/cell replacement clock이 회복을 지배합니다. ② 가역적 turnover와 비가역 kill을 구분하는 기준은 "표적이 소비되었는가"예요. ③ "약물 소실 = 효과 소실"로 가정하면 duration 예측이 임상적으로 무의미해집니다. ④ Friberg-Karlsson 호중구 감소 모델은 본 세션의 모든 도구(비가역 kill + transit + feedback + baseline)가 한 자리에 결합되는 응용 사례이며, oncology PK/PD 진출의 표준 출발점입니다.

<!-- SLIDE_START: M7 | title: Apex — Turnover vs Effect Compartment Discrimination Crisis -->
<!-- SECTION_CORE: SC-09 -->
## Card 7 — [⚡ Apex Concept] Turnover vs Effect Compartment Discrimination Crisis

앞 카드에서 "어떤 pool이 회복되는가"를 물었어요. 이번 카드는 정점이에요 — **같은 곡선이 turnover pool 지연인지 effect-site pool 지연인지 데이터만으로는 가릴 수 없는 위기**를 다룹니다.

> **거장의 시각**
> 흔히 학생들이 fit이 매끄럽고 $k_{out}$이나 $k_{e0}$가 그럴듯한 값으로 나오면 "지연 원인이 결정됐다"고 생각해요. 그런데 제한된 단회 투여와 좁은 dose range에서는 turnover $R(t)$와 effect-site $C_e(t)$가 거의 똑같은 곡선을 만듭니다. **체화할 한 가지는 — 곡선이 아니라 지연이 어디 사는지(biology냐 biophase 분포냐)를 증명해야 한다는 것**이에요.

### A. 경쟁하는 구조들

Turnover와 effect-compartment는 제한된 단회 투여 설계에서 거의 같은 곡선을 만들 수 있어요. 차이는 곡선의 매끄러움이 아니라 **인과 주장**이에요 — 지연이 약물이 biophase(실제 작용부위 주변 농도 공간)에 천천히 도달해서 생기는지, 아니면 반응 system 자체가 천천히 turnover해서 생기는지 [G&W pp.758–763; R&T pp.244–246].

Turnover:

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
\quad \text{[R&T pp.244–246]}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $R(t)$ | response unit | turnover response pool | production/loss, system turnover |
| $C_e$ | concentration | effect-site 농도 | biophase 평형, $k_{e0}$ |
| $k_{out}$ | time⁻¹ | system turnover clock | 반응 biology, feedback, 모델 구조 |
| $k_{e0}$ | time⁻¹ | plasma-to-effect-site 평형 clock | 조직 분포, biophase 지연 |
| WRSS/AIC | fit metric | 구조 간 적합도 차이 | residuals, model complexity, 데이터 풍부도 |

두 모델은 **같은 그림자를 만들어내는 두 물체**예요. 그림자 모양만 보고 물체를 결정하는 건 위험하고, 조명 방향을 바꾸거나 다른 각도에서 봐야 정체가 드러납니다.

PD6가 이 위기를 데이터로 보여줘요 — turnover와 effect-compartment 적합이 본질적으로 같은 잔차 거동을 보이고, $k_{out}$과 $k_{e0}$가 둘 다 약 5.6 h⁻¹ 부근의 비슷한 값으로 수렴합니다 [G&W pp.758–763].

> **📌 비식별성의 본질**
> Pool 1과 Pool 2 모델은 단일 dose range 데이터에서 사실상 구별 불가능해요($r=0.9999$, $\Delta WRSS\approx2$). 이건 피팅 실패가 아닙니다 — **데이터가 두 모델을 분리하기에 부족하다는 정보를 주는 것**이에요. 더 넓은 dose range나 mechanism-based prior 없이는 "어느 모델이 옳은가"라는 질문에 데이터로 답할 수 없습니다.

### B. 감별 방법

| 증거 | Turnover 지지 | Effect compartment 지지 |
|---|---|---|
| 반응 변수 | 내인성 매개물질, 바이오마커, 세포 수, 응고인자, 위산 pH | 작용 부위로의 약물 분포 지연이 원인 |
| Dose range | 비선형 turnover 거동을 드러낼 만큼 넓을 것 | 안정적 $EC_{50}$과 타당한 $k_{e0}$로 hysteresis 해소 |
| 교란 | 반복 투여/washout이 system 회복 시간을 드러냄 | Biophase 평형으로 onset과 offset 설명 |
| 기전적 사전 정보 | 알려진 합성/소실 과정 | 알려진 조직 분포 지연 |

> 💼 **실무 인사이트**: 두 인과 구조가 똑같이 잘 맞을 때 규율 있는 접근은 **생물학적 가정을 문서화하고, 두 구조를 가를 수 있는 설계 요소를 명시**하는 거예요. 모델의 방어 가능성은 곡선의 매끄러움이 아니라 mechanism과 design support에서 나옵니다.

### C. 왜 데이터만으로는 결판이 안 나나

**교과서 기반**: 적합도만으로는 지연이 분포 때문인지 turnover 때문인지 증명할 수 없어요. 제한된 설계에서는 두 구조가 똑같이 잘 보입니다 [G&W pp.758–763; R&T pp.244–246].

Turnover로 생성된 system에 effect-compartment 모델을 적합시켰을 때 $EC_{50}$이 dose에 따라 변한다면, 그 약물 파라미터는 **system 동역학을 흡수하고 있는 것**이에요. 이건 potency 발견이 아니라 **구조적 경고 신호**입니다.

PD6 Table 6.1이 이 비식별성을 숫자로 못 박아둡니다.

| Metric | Turnover (linear S·$k_{in}$) | Effect compartment | Δ |
|---|---:|---:|---:|
| WRSS | 15,516 | 15,518 | 2 |
| AIC | 1,041 | 1,040 | −1 |
| 시간 상수 | $k_{out}=5.6\;h^{-1}$ | $k_{e0}=5.6\;h^{-1}$ | 0 |
| Half-doubling 농도 | $EC_{50}=1{,}633\;\text{ng}\cdot\text{L}^{-1}$ | $a=0.026\to\sim1{,}623\;\text{ng}\cdot\text{L}^{-1}$ | <1% |

> ⚠️ $\Delta WRSS=2$와 $\Delta AIC=-1$은 model selection 기준에서 **사실상 동치**예요. "둘 중 하나가 더 매끄럽다"가 아니라 **"데이터가 둘을 못 가른다"는 신호**입니다.

여기서 학생들이 자주 빠지는 함정이 하나 있어요. **단일 dose-range 데이터에서 turnover와 effect compartment가 둘 다 잘 맞으면, AIC가 조금 낮은 모델을 "기전적으로 맞는 모델"로 골라버리는 거예요.** $\Delta AIC=-1$처럼 숫자가 우열처럼 보이고 두 곡선이 다 매끄러워 보이니까 그럴싸하죠. 그런데 이걸 그냥 두면 나비효과가 납니다 — AIC 미세차로 구조를 결정 → $k_{e0}$ 또는 $k_{out}$에 지연 원인을 잘못 배정 → 임상에서 새 dose range나 반복 투여 때 onset/offset 예측 실패 → 규제 단계에서 "대안 구조 평가와 sensitivity analysis가 빠졌다"는 deficiency가 돌아옵니다.

> 📖 **G&W 5e p.759, Fig 6.1; p.763, Table 6.1**: 핵심 감별 그림이에요. **반응-시간 적합은 본질적으로 동등해 보일 수 있지만, 인과 해석은 서로 다르게 남는다**는 걸 직접 보여줍니다. Table 6.1은 $k_{out}/k_{e0}$의 근접 동등성을 숫자로 명시해요. → 그래서 fit만으로 인과 구조를 결정하면 안 된다는 사실의 정량 증거입니다.

**이번 카드 핵심내용**: ① 두 모델 fit이 동등하면 mechanism prior와 design support가 결정자가 됩니다. ② $k_{out}\approx k_{e0}$로 수렴할 때 지연이 어디 사는지 데이터 단독으로는 확정할 수 없어요. ③ fit quality로 인과 구조를 결정하면 잘못된 구조 확정, sensitivity 누락, 후속 용량 예측 실패로 직결됩니다.

<!-- SLIDE_START: M8 | title: PK Clock vs PD Clock + Duration Formula Boundary -->
<!-- SECTION_CORE: SC-10 -->
## Card 8 — PK Clock vs PD Clock + Duration Formula Boundary

앞 카드에서 지연이 어디 사는지 증명해야 한다는 위기를 봤어요. 이번엔 그 판단이 **실제 dose-duration 공식을 쓸 수 있느냐 없느냐**를 어떻게 결정하는지를 다룹니다.

> **거장의 시각**
> Eq 8-12(PK clock 기반 duration 공식)를 모든 지연 반응에 갖다 붙이면 warfarin, aspirin, omeprazole, paclitaxel에서 수학적으로는 매끈하지만 임상적으로는 틀린 duration이 나와요. **PK clock과 PD clock 중 어느 쪽이 더 느린지를 먼저 골라두면**, dose log 공식이 살아있는 경우와 폐기해야 하는 경우가 그 자리에서 갈립니다.

### A. Clock 감별

투약 후에 두 개의 시계가 동시에 돌아갑니다 — 약물의 PK clock과 반응 system의 PD clock. **관찰되는 반응 감소는 둘 중 느린 쪽의 시계가 결정**합니다 [R&T pp.243, 247–256].

| 상황 | 느린 clock | 대표 사례 | 모델링 귀결 |
|---|---|---|---|
| PK rate-limited | 약물 소실/분포 | **Succinylcholine** 0.5/1/2/4 mg·kg⁻¹ i.v.(탈분극성 근이완제; 마취 보조); **Minoxidil** 25 mg 단회 경구(K⁺ 채널 개방 혈관확장제), MAP 저하 — → 그래서 **PK clock이 duration을 결정하는 사례**입니다 [R&T pp.249–256] | $t_D$ 공식이 의미 있을 수 있음 |
| PD rate-limited | System turnover/표적 재생 | **Acenocoumarol**(쿠마린계 항응고제; vitamin K 경쟁) vs 응고인자 turnover; **Aspirin** 혈소판/TxB₂; **Omeprazole** proton-pump 회복; **Paclitaxel** 백혈구 회복 — → 그래서 **PD clock이 duration을 결정하는 사례들**입니다 [R&T pp.243, 251–254] | Turnover/target-consumption 모델 필요; PK $k$만으로는 duration 예측 불가 |
| 약물 PK가 system보다 느릴 때 | 간접 기전에서도 PK가 지배 | **Phenprocoumon**(장반감기 쿠마린계 항응고제; ~5일) vs 응고인자 동역학 — → 그래서 **같은 작용기전이라도 약물별로 지배 시계가 다를 수 있다는 사실의 사례**입니다 [R&T p.243] | 항응고 효과 회복이 약물 잔류를 따름 |

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $k$ | time⁻¹ | PK elimination clock | clearance, volume, 약물 잔류 |
| $t_D$ | time | threshold 이상/이하 효과 지속시간 | dose, $k$, $A_{min}$, clock 선택 |
| $A_{min}$ | amount | 효과 최소량 | $C_{min}V$, threshold, 노출-반응 관계 |
| PD clock | time scale | system recovery 또는 표적 대체 | turnover, 비가역 작용, feedback |

### B. Region 1/2/3과 선형 감소

계단식 E-logC 관계의 중간 구간에서는 단일 용량 투여 후 반응이 시간에 따라 **근사적으로 직선으로 감소**합니다.

$$
\underbrace{Response}_{\text{관찰반응}}
=
\underbrace{E(0)}_{\text{시작효과}}
-
\overbrace{\underbrace{m}_{\text{E-logC 기울기}}\,\underbrace{k}_{\text{PK clock}}\,\underbrace{t}_{\text{시간}}}^{\text{선형 감소}}
\quad \text{[R&T Eq 8-9; R&T pp.247–249]}
$$

이건 Region 2(반응이 Hill curve의 중간 구간에 있을 때)에 대한 서술이에요. Region 3은 plateau에 가까운 구간이고, Region 1은 1차 동역학 비슷한 거동으로 돌아갑니다. **Succinylcholine의 대략 22%/min 감소**가 이 중간 구간 선형성의 예시예요 [R&T pp.249–250].

Region 2는 **비탈길 중간의 직선 구간**과 같아요 — 위쪽 plateau나 아래쪽 완만한 구간에서는 같은 걸음 수가 같은 높이 변화로 바뀌지 않습니다. → 그래서 succinylcholine의 dose-duration이 이 직선 구간 위에 있을 때만 Eq 8-12 같은 공식이 살아있어요.

### C. Duration 공식

Clock 감별이 먼저 끝나야 합니다. **PK-rate-limited 반응에서 노출-반응 관계가 사실상 고정**되어 있을 때만 이 식을 씁니다.

$$
\underbrace{t_D}_{\text{duration}}
=
\underbrace{\frac{1}{k}}_{\text{PK clock 역수}}
\ln\left(\frac{\underbrace{Dose}_{\text{투여량}}}{\underbrace{C_{min}V}_{\text{최소 유효량}}}\right)
=
\underbrace{\frac{1}{k}}_{\text{PK clock 역수}}
\ln\left(\frac{\underbrace{Dose}_{\text{투여량}}}{\underbrace{A_{min}}_{\text{효과 최소량}}}\right)
\quad \text{[R&T Eq 8-12; R&T pp.254–255]}
$$

용량을 두 배로 올리면 **약물 반감기 하나만큼의 duration이 추가**됩니다.

$$
\underbrace{\Delta t_D}_{\text{duration 추가분}}
=
\frac{\underbrace{\ln 2}_{\text{2배 로그}}}{\underbrace{k}_{\text{PK clock}}}
=
\underbrace{t_{1/2}}_{\text{PK 반감기}}
$$

이게 succinylcholine duration이 **용량을 두 배로 늘릴 때마다 대략 유효 반감기 하나씩 더해지는** 이유예요 [R&T pp.255–256]. PK-rate-limited duration에서 dose doubling은 **로그 자 위에서 한 칸 오른쪽으로 이동하는 것**과 같고, 그 한 칸이 시간축에서 반감기 하나로 번역됩니다.

> ⚠️ Eq 8-12를 warfarin, aspirin, omeprazole, paclitaxel처럼 **PD-rate-limited 상황에 갖다 붙이지 마세요.** Duration을 계산하기 전에 먼저 "어느 시계가 더 느린가?"를 물어야 합니다. 답이 PD라면 PK $k$를 duration 결정 인자로 쓰는 걸 그 자리에서 멈춰야 해요.

Post-trough 회복 곡선에서 관측 데이터가 모델보다 빠르게 baseline으로 돌아오면 moderator/feedback compartment 누락 신호예요. G&W §2.6.7 Eq 2:261–2:263과 IgG의 11일 saturable protection이 이 패턴의 prototype이고, 예측 duration이 관측 duration과 50% 이상 어긋나거나 dose 증량 시 예측 증가가 관측치와 비례하지 않으면 **rate-limiting clock이 잘못 잡혔다는 정량 시그너처**입니다.

**Acenocoumarol**(반감기 ~15 h)과 **phenprocoumon**(반감기 ~5–6일)은 **같은 prothrombin complex 동역학을 공유하지만 서로 다른 rate-limiting clock**을 가집니다(Fig 8-11). 같은 작용기전 약물군에서도 약물별 PK가 rate-limiting step을 결정해요. → 그래서 **같은 기전 = 같은 duration formula는 아니다**라는 사실의 핵심 사례입니다 [R&T p.243].

> 📖 **R&T 5e p.243, Fig 8-11**: 같은 항응고 반응 system도 약물 PK에 따라 **서로 다른 시계에 의해 제한**될 수 있다는 걸 그림으로 보여줘요.

> 📖 **R&T 5e p.255, Fig 8-23; p.256, Fig 8-24**: Eq 8-12의 시각적 결과예요 — **PK가 속도 제한 단계인 조건에서 용량을 두 배로 늘리면 duration에 대략 한 반감기가 추가**되는 패턴을 보여줍니다.

**이번 카드 핵심내용**: ① duration 공식을 쓰기 전에 PK-rate-limited인지부터 확인하세요. ② PD-rate-limited 약물이면 turnover/target-replacement 모델을 써야 합니다. ③ clock 선택 없이 $t_D$를 계산하면 수학적으로는 맞지만 임상적으로는 무의미한 duration이 나옵니다.

<!-- SLIDE_START: S03 | title: §5 — 혼동 쌍 해부 -->
<!-- SECTION_CORE: SC-11 -->
# §5 — 혼동 쌍 해부(Confusion Pair Dissection)

여기서 잠깐 멈추고 정리합니다. M1~M8을 통과한 학생이 실제로 보고서나 발표 자리에서 가장 자주 헷갈리는 쌍 5개를 손으로 가르겠습니다.

## §5-1. Model 1 vs Model 2 — 생산 억제 vs 소실 억제

| 비교 기준 | Model 1 (생산 억제) | Model 2 (소실 억제) |
|---|---|---|
| 단위 / 차원 | $k_{in}I(C)$는 response·time⁻¹ input term | $k_{out}RI(C)$는 response·time⁻¹ loss term |
| 수식 내 위치 | $dR/dt=k_{in}I(C)-k_{out}R$; 약물 함수가 input에 [G&W pp.238–239] | $dR/dt=k_{in}-k_{out}RI(C)$; 약물 함수가 loss에 [G&W pp.240–241] |
| 변화 원인 | biosynthesis 또는 production 차단 | removal 또는 loss 차단 |
| 혼동 시 임상 결과 | 하향 반응을 다 "억제"로 부르면서 production vs loss를 놓침 | 상향 반응을 production stimulation으로 오인 |

$$
\begin{aligned}
\text{Model 1: }&\frac{dR}{dt}=\overbrace{k_{in}I(C)}^{\text{production 억제}}-\underbrace{k_{out}R}_{\text{기존 loss}}\\
\text{Model 2: }&\frac{dR}{dt}=\underbrace{k_{in}}_{\text{production 유지}}-\overbrace{k_{out}RI(C)}^{\text{loss 억제}}
\end{aligned}
$$

## §5-2. Direct $E_{max}$ vs Turnover $I_{max}$/$E_{max}$

| 비교 기준 | Direct 모델 | Turnover 모델 |
|---|---|---|
| 단위 / 차원 | 파라미터화에 따라 response unit 또는 무차원 | $k_{in}/k_{out}$ baseline에 대한 배율 |
| 수식 내 위치 | 즉각 농도-반응 식 내 vertical distance 또는 multiplier | $R_{ss}$ 또는 turnover ODE 내 system perturbation |
| 변화 원인 | 농도-반응 관계 자체 | 생산/소실 동역학 후의 system 반응 |
| 혼동 시 임상 결과 | 직접 반응 거리와 turnover 배율을 같은 효과 크기로 비교 | cross-model, in vitro/임상 potency 비교가 왜곡 |

## §5-3. Reversible Turnover vs 비가역 사멸/표적 소비

| 비교 기준 | Reversible turnover | Irreversible / target consumption |
|---|---|---|
| 단위 / 차원 | $k_{in}$ response·time⁻¹, $k_{out}$ time⁻¹ | $K_{kill}$ concentration⁻¹·time⁻¹, $K_{kill}CR$ response·time⁻¹ |
| 수식 내 위치 | $dR/dt=k_{in}-k_{out}R$ | $dR/dt=-K_{kill}CR$; $SF=\exp(-K_{kill}\cdot AUC)$ |
| 변화 원인 | system이 계속 생산·소실해서 baseline 복귀 | 표적/세포가 소비되고 대체/재성장 필요 |
| 혼동 시 임상 결과 | 지연된 회복을 무조건 비가역 작용으로 오인 | 약물 소실이 곧 효과 소실이라고 가정 |

$$
\begin{aligned}
\text{Reversible: }&\frac{dR}{dt}=\underbrace{k_{in}}_{\text{재생산}}-\underbrace{k_{out}R}_{\text{소실}}\\
\text{Irreversible: }&\frac{dR}{dt}=-\overbrace{\underbrace{K_{kill}}_{\text{kill potency}}\underbrace{C}_{\text{노출}}\underbrace{R}_{\text{잔여 target/cell}}}^{\text{target/cell 소비}}
\end{aligned}
$$

## §5-4. Turnover vs Effect Compartment — 치명적 쌍

| 비교 기준 | Turnover 모델 | Effect compartment |
|---|---|---|
| 단위 / 차원 | $R$, $k_{in}$, $k_{out}$ 중심의 response biology | $C_e$, $k_{e0}$ 중심의 biophase 농도 |
| 수식 내 위치 | $dR/dt=k_{in}S(C)-k_{out}R$ | $dC_e/dt=k_{e0}(C-C_e)$, $R=f(C_e)$ |
| 변화 원인 | 내인성 매개물질/세포/바이오마커 turnover | 작용 부위로의 약물 분포 지연 |
| 혼동 시 임상 결과 | fit 동등성을 mechanism 결정으로 오독 | $k_{e0}$가 system turnover를 흡수 |

> 💼 규제 제출 형식의 글에서, **이 지점이 대안 모델 비교와 기전적 정당화가 들어가야 할 위치**예요. 설계가 구조를 가를 수 없다면 선택된 구조를 당연한 것처럼 제시하지 마세요.

## §5-5. PK Rate-Limited vs PD Rate-Limited 감소

| 비교 기준 | PK-rate-limited | PD-rate-limited |
|---|---|---|
| 단위 / 차원 | $k$ time⁻¹; 약물 농도/양 clock | system recovery/표적 대체 time scale |
| 수식 내 위치 | $t_D=(1/k)\ln(Dose/A_{min})$ | $t_D$는 system recovery 또는 표적 대체가 결정 |
| 변화 원인 | 약물 소실/분포가 느림 | turnover, 표적 재생, 세포 회복이 느림 |
| 혼동 시 임상 결과 | clearance 효과를 duration에서 놓침 | 노출만으로 duration 변화를 과대 예측 |

$$
\underbrace{t_D}_{\text{duration}}
\xrightarrow[\text{PK-rate-limited}]{}
\underbrace{\frac{1}{k}\ln\left(\frac{Dose}{A_{min}}\right)}_{\text{PK clock 공식}},
\qquad
\underbrace{t_D}_{\text{duration}}
\xrightarrow[\text{PD-rate-limited}]{}
\underbrace{\text{system recovery / target replacement}}_{\text{PD clock}}
$$

> **각주 — 노출-반응 단절 (보조 사례)**
> **Rosuvastatin**(HMG-CoA 환원효소 억제제) OATP1B1 polymorphism은 전신 plasma exposure를 substantially 변화시키지만 작용 부위(cholesterol synthesis) 반응은 modestly 변합니다 — 별도 turnover 모델이 아니라 **전신 노출 ≠ 작용 부위 노출**의 보조 사례예요. Bioequivalence가 효과 동등성을 보장하지 않는 메커니즘으로 자주 인용됩니다 [R&T pp.258–259].

## §5-6. ⚡ 기억 고리(Memory Hooks) — 7가지 핵심 개념 쌍

각 hook은 두 개념 차이의 **구조적 필연**을 비유로 묶어둡니다.

**Pair 1 — direct effect vs indirect response**: *바로 켜지는 전등 vs 서서히 따뜻해지는 전기장판.* Direct는 농도 상승에 즉시 따라오는 반응, indirect는 약물이 production 또는 loss를 바꾸고 그 변화가 response pool에 쌓이면서 나타나는 지연 반응이에요. 반응이 $C_{max}$보다 늦게 peak에 도달하면 indirect를 먼저 의심하세요.

**Pair 2 — Model I (생산 억제) vs Model II (소실 억제)**: *수원 틀기 vs 배수구 막기.* 단일 dose range에서는 두 모델이 사실상 같은 데이터를 만들 수 있으니까 mechanism prior나 더 넓은 용량 범위가 필요합니다.

**Pair 3 — $k_{in}$ vs $k_{out}$**: *수원 속도 vs 배수 속도.* 기저상태에서 $k_{in}=k_{out}\cdot baseline$이고, $k_{out}=1/MRT_{response}$가 반응 반감기를 결정합니다.

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

**Pair 4 — baseline $R_0$ vs steady-state $R_{ss}$**: *출발점 vs 목적지.* $R_0$는 약물 투여 전 pool의 자연 균형, $R_{ss}$는 약물 효과 하의 새 균형. 이동 속도는 $k_{out}$이 결정하고, 거리는 $E_{max}$와 $EC_{50}$이 결정해요.

**Pair 5 — rebound vs natural recovery**: *과교정 vs 자연 복귀.* Rebound는 약물 중단 시 반응이 baseline을 넘어서는 것, natural recovery는 그냥 baseline으로 돌아오는 것. **구분 기준은 반응이 baseline을 넘어서는가입니다.**

**Pair 6 — duration of effect vs AUC of effect**: *효과의 길이 vs 효과의 면적.* Duration은 threshold 이상/이하 시간이고, AUC of effect는 반응-시간 곡선 아래 면적이에요. 같은 duration이어도 반응 높이가 다르면 AUC가 다릅니다.

**Pair 7 — non-identifiability vs misspecification**: *지도가 둘 다 정확 vs 지도가 틀림.* 비식별성은 데이터가 둘 중 무엇이 맞는지 결정하지 못하는 상태, misspecification은 데이터와 안 맞는 구조를 고른 상태. $\Delta WRSS\approx2$, $\Delta AIC\approx-1$은 **비식별성 신호이지 misspecification 신호가 아닙니다.**

## §5 Recap — 다섯 가지 clock 위치 오류

| 오류 패턴 | 잘못 짚은 clock | 대표 반례 |
|---|---|---|
| **E1. Mirror-slope 오독** | 모든 모델에서 early slope를 $-k_{out}$으로 외삽 | PD7: 6,400U → 0.6 h⁻¹, 160,000U → 1.6 h⁻¹ — system 파라미터가 용량 의존적으로 보이는 misspecification artifact [G&W p.251] |
| **E2. Phantom convergence with linear S(C)** | turnover와 effect compartment가 같은 fit → effect compartment 확정 | PD6 Table 6.1: $\Delta WRSS=2$, $k_{out}=k_{e0}=5.6\;h^{-1}$ — fit 동등성이 mechanism 결정을 의미하지 않음 [G&W pp.758–763] |
| **E3. Wrong-clock $t_D$** | 모든 약물에 Eq 8-12 적용 | warfarin/aspirin/omeprazole/paclitaxel은 PD-rate-limited — PK $k$로 계산한 $t_D$는 임상적으로 무의미 [R&T pp.251–254] |
| **E4. Linear-PK = linear-PD assumption** | dose-proportional AUC가 곧 dose-proportional response | methylprednisolone 16–1000 mg: AUC는 비례하지만 lymphocyte 반응은 plateau 진입 [R&T pp.256–258] |
| **E5. Same-mechanism = same-clock assumption** | 동일 작용기전이면 같은 rate-limiting step | acenocoumarol(PD-limited, 15 h) vs phenprocoumon(PK-limited, ~5일) — 같은 anticoagulant 기전, 다른 지배 clock [R&T p.243] |

**이 다섯 가지를 외운 학습자는 이 세션의 모델링 결정을 거의 자동으로 방어할 수 있습니다.**

<!-- SLIDE_START: S04 | title: §7 — 자기 테스트 -->
<!-- SECTION_CORE: SC-12 -->
# §7 — 자기 테스트: 능동 회상 모듈

## Q1 [회상] Model 1 ODE와 정상상태

Model 1 ODE를 쓰고, 일정한 $C_{ss}$에서 $R_{ss}$를 도출하세요.

**정답**
$$
\underbrace{\frac{dR}{dt}}_{\text{변화율}}
=
\overbrace{k_{in}I(C)}^{\text{production 억제}}
-
\underbrace{k_{out}R}_{\text{소실}}
$$

정상상태에서: $R_{ss}=R_0 I(C_{ss})$ [G&W pp.238–239].

$$
\underbrace{R_{ss}}_{\text{약물 정상상태}}
=
\underbrace{R_0}_{\text{기저값}}
\underbrace{I(C_{ss})}_{\text{남은 production}}
$$

## Q2 [회상] $t_{ss}$가 용량 독립적인 모델은?

**정답**: Models 1과 3 — 1차 소실 항이 $k_{out}\cdot R$로 유지되기 때문이에요. Models 2와 4는 약물이 소실 항을 바꾸니까 용량 의존적 $t_{ss}$가 나올 수 있습니다. 단, 이 결론은 **PK가 더 느린 clock이 아닐 때만** 성립해요 [G&W pp.247–251; R&T p.243].

## Q3 [응용] PD9의 peak shift 부재 해석

용량을 증가시켜도 peak shift가 안 나타납니다. 이게 effect compartment 모델을 증명하나요?

**정답**: 아닙니다. PD9는 **peak shift 부재가 link/effect-compartment 모델을 반드시 의미하지는 않는다**고 명시적으로 경고합니다. Dose range, 비선형 약물 함수, system 동역학을 같이 봐야 해요 [G&W pp.778–783].

## Q4 [응용] PD9 Zooparc® 용량 정정

Zooparc® 반복 투여 데이터에서 확인된 용량 수준은 무엇이고, 25 mg/day는 어떻게 기술해야 하나요?

**정답**: 관찰된 반복 투여 figure는 **2.5 mg과 5 mg**을 사용합니다. 25 mg/day 진술은 투사(projection)/대규모 연구 논의이며, 관찰된 용량 맥락이 아닙니다 [G&W pp.778–783].

## Q5 [응용] Naproxen 정정

"naproxen 250 mg, Fig 8-3"이라는 오류 표현을 수정하세요.

**정답**: **Naproxen 500 mg 경구, dental pain 모델, 1–8 h sampling, 반시계 방향 hysteresis, Fig 8-2.** Fig 8-3은 하류 약력학 도식이며 naproxen 그림이 아닙니다 [R&T pp.234–236].

## Q6 [응용] 잘못된 clock의 $t_D$

Aspirin duration 예측에 Eq 8-12가 왜 부적절한가?

**정답**: Aspirin의 혈장 노출은 빠르게 사라지지만 **표적과 혈소판 기능 회복이 더 느리기 때문에 thromboxane B₂ 억제가 지속**됩니다. Duration은 PD/표적 대체가 결정하지 PK rate-limited가 아니에요 [R&T p.251].

## Q7 [응용] Turnover vs effect compartment

단일 용량 데이터가 turnover와 effect-compartment 두 모델 모두에 똑같이 잘 적합합니다. 두 모델 중 하나를 결정하려면 어떤 증거가 필요한가?

**정답**: 반응 변수에 대한 기전적 사전 정보, 더 넓은 dose range, 반복 투여/washout, PK clock 교란, 그리고 $EC_{50}/k_{e0}$이 생물학적으로 타당하게 유지되는지 여부. **적합도 단독으로는 부족합니다** [G&W pp.758–763; R&T pp.244–246].

## Q8 [응용] Linear PK ≠ linear PD

Methylprednisolone AUC가 16–1000 mg 범위에서 용량 비례적입니다. 이게 왜 용량 비례적 lymphocyte 반응을 정당화하지 못하나?

**정답**: 반응이 노출-반응 곡선의 **plateau 구간에 진입**할 수 있어요. R&T의 lymphocyte 사례는 PK가 용량 비례적이어도 고용량에서 추가 PD 반응이 거의 없다는 걸 보여줍니다. R&T 본문(p.256)이 단호하게 못박아둬요 — *"Dose linearity in pharmacokinetics does not result in dose linearity in pharmacodynamics. That is almost never the case."* [R&T pp.256–258]

## Q9 [보스 딜레마(Boss dilemma)]

스폰서가 주장합니다 — "phenprocoumon과 acenocoumarol은 같은 항응고 기전을 공유하니까 반응 회복은 같은 PD turnover half-life로 결정돼야 합니다." 동의하나요, 거부하나요? **30년 경력 심사자가 쓸 구체적 방어 논리로 정당화하세요.**

**정답 — Trade-off 논리**
**거부(Reject).** 같은 기전이 같은 rate-limiting clock을 의미하지는 않습니다. Acenocoumarol은 PK 반감기가 짧아서(~15 h) 회복이 PD-clock 제한적이 됩니다(응고인자 turnover가 더 느림). Phenprocoumon은 PK 반감기가 훨씬 길어서(~5일) 회복이 PK-clock 제한적이 됩니다(약물 잔류가 system clock보다 우세) [R&T p.243].

이 차이가 임상·규제 차원에서 갖는 trade-off:
- **Sponsor의 단순화를 채택할 때**: 두 약물에 동일한 dose-titration step-up rule을 적용 → phenprocoumon 누적 위험 또는 acenocoumarol 미달 dose. 어느 쪽이든 환자 안전과 약효 부전 사고로 직결됩니다.
- **Mechanism-only justification의 규제 위험**: 모델 선택 paragraph에서 "같은 기전이니까 같은 PD half-life"라는 추론은 design support 없이는 데이터로 방어 불가능 → "insufficient justification for proposed dosing interval" 형태의 deficiency 위험.
- **올바른 방어 논리**: 약물별 PK profile이 같은 PD system 위에서 어떤 시계를 작동시키는지를 acenocoumarol vs phenprocoumon Fig 8-11 데이터로 직접 증명한 뒤, 약물별로 별도의 dose-duration model을 씁니다. **단일 PD half-life claim은 phenprocoumon에서 임상적으로 무의미하고 acenocoumarol에서만 유효해요.**

## ⚡ 보스 딜레마 ★★

Pool 1과 Pool 2 indirect response 모델 중 어느 것을 Phase 2 용량 결정에 사용할 것인가? 두 모델은 현재 데이터(단일 dose group, 제한된 dose range)에서 $\Delta WRSS=2$, $k_{out}=k_{e0}$로 **사실상 비식별적**입니다.

**선택지 A**: 기존 생물학적 증거가 production inhibition을 지지한다면(예: 생체표지자가 생성률과 연관), Model I을 선택하고 비식별성을 보고서에서 limitation으로 명시합니다.

**선택지 B**: 어느 메커니즘도 확실하지 않다면, 두 모델을 모두 제출하고 sensitivity analysis로 용량 결정이 모델 선택에 얼마나 민감한지 제시합니다. 더 보수적인 용량 예측을 주는 모델을 기본으로 씁니다.

**거장의 Trade-off 논리**
A는 기계론적으로 깔끔하지만 데이터 외 prior를 사용했다는 비판을 받을 수 있어요. B는 불확실성을 투명하게 전달하지만 의사결정자에게 혼란을 줄 수 있고요. **규제 제출에서는 "어느 모델을 선택했는가"보다 "왜 이 불확실성이 용량 결정의 안전성에 영향을 주지 않는가"를 설명하는 게 핵심**이에요. 즉, 두 모델 모두에서 제안된 Phase 2 용량이 안전 한계 안에 있음을 sensitivity analysis로 증명하면, 모델 선택 자체가 의사결정의 critical path에서 빠집니다 — 이게 **"비식별성을 우회하는" 정통 규제 전략**입니다.

이 딜레마의 한 줄 메시지: **비식별성 앞에서 모델을 *선택*하려고 하지 말고, 비식별성이 의사결정에 *영향을 주지 않는 결정 구조*를 설계하세요.**

## §7 Recap

올바른 답은 반드시 **model family**와 **clock 위치** 둘 다를 식별해야 해요. 수학적으로 맞는 공식이라도 잘못된 시계에 갖다 붙이면 틀린 겁니다.

<!-- SLIDE_START: S05 | title: §8 — 메타프레임 & 빅 픽처 -->
<!-- SECTION_CORE: SC-13 -->
# §8 — 메타프레임 & 빅 픽처

## A. 약리계측학 아키텍처에서의 위치

이번 세션은 직접 노출-반응 모델링과 고급 질병/반응 시스템 사이에 자리합니다. 여기서부터 모델러는 **곡선 적합을 넘어 원인을 분리**해야 해요.

| 후속 세션 | 이번 세션에서 열리는 개념 | 이번 세션 없으면 실패하는 것 |
|---|---|---|
| Transit compartment | 분포/전달 지연과 turnover 지연의 분리 | 모든 지연을 effect compartment로 흡수 |
| Tolerance/moderator model | feedback, rebound, post-trough 회복 timing | $k_{out}$ 고정 가정 위반을 놓침 |
| Disease progression / baseline drift | $R_0$가 시간에 따라 움직이는 경우 | 질병 진행이나 일주기 변동을 약물 효과로 오독 |
| PopPK/PD IIV | drug parameter와 system parameter의 분리 | $E_{max}$, $k_{out}$, $k_{e0}$ 해석 혼동 |
| Sampling design | 숨겨진 시계를 식별할 관측 창 설계 | 비식별성을 후속 시험에 반복 |

## B. 이번 세션을 약하게 다뤘을 때의 실패 모드

| 실패 모드 | 실무적 결과 |
|---|---|
| 모든 지연을 effect compartment로 처리 | $k_{e0}$이 생물학을 흡수 → 새 투여 프로토콜에서 dosing 시뮬레이션 실패 |
| $t_{ss}$를 모델의 결정적 증거로 처리 | 기전적 주장이 설계 근거를 과대평가 |
| $E_{max}$ 단위 혼동 | 교차 연구 또는 in vitro/임상 potency 비교가 오해를 유발 |
| PD-rate-limited 약물에 $t_D$ 적용 | Duration 예측이 생물학적으로 무의미 |
| Baseline drift 무시 | 질병 진행이나 일주기 변동을 약물 효과로 오독 |

## C. 실무자가 데이터를 받은 첫 30초 안에 자동으로 돌리는 진단 순서

경력 있는 약리계측학 심사자는 **곡선이 매끄러운지를 가장 먼저 묻지 않습니다.** 데이터를 본 첫 30초 안에 다음 진단 순서를 본능적으로 돌립니다.

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| Plasma C vs response loop가 반시계 또는 시계 방향 | Hysteresis 방향 | → | distribution/turnover/active-metabolite 또는 tolerance/feedback 후보 분리 | 30초 안에 첫 가설 설정 |
| 반응 방향과 $t_{ss}$ 용량 의존성 조합 관찰 | $k_{out}$ 또는 effective $k_{out}$ | → | 4-model 칸 중 하나로 좁힘 | PD5/PD7 side-by-side 확인 |
| Post-trough 관측이 모델보다 빠르게 회복 | moderator/feedback 누락 가능성 | → | rebound/recovery 예측 실패 | feedback 또는 moderator 구조 검토 |
| OFV가 30 iteration 동안 stuck-then-drop | $r(k_{in},k_{out})>0.98$ 가능성 | → | covariance/search geometry 실패 | $R_0$, $k_{out}$ 재파라미터화 |
| 새 약물 duration 질문 | PK vs PD rate-limiting clock | → | 같은 기전 약물 간 duration 차이 | acenocoumarol vs phenprocoumon 같은 clock pair 비교 |

이 다섯 단계를 통과한 뒤에야 NONMEM 출력에 손을 댑니다. 자동화 도구는 단계 1과 4를 따라할 수 있지만 단계 2, 3, 5의 **"데이터의 의미를 묻는 직관"은 데이터 외부의 mechanistic prior를 요구하기 때문에 복제되지 않습니다.**

## 최종 요약

간접 반응 모델링은 **"지연을 추가하는 일"이 아닙니다.** **올바른 인과 시계에 지연을 배정하는 일**이에요. 한 번 정해두면 안 흔들리는 작업 순서:

**hysteresis 방향 → 4-model 작용 부위 → $t_{ss}$/peak-shift 선별 → 초기 파라미터 감사 → turnover vs link 감별 → PK/PD clock 선택 → PK-rate-limited일 때만 duration 공식.**

<!-- SLIDE_START: S09 | title: §9 — 정확한 교과서·1차 문헌 출처 -->
<!-- SECTION_CORE: SC-14 -->
# §9 — 정확한 교과서·1차 문헌 출처 (References)

본문 내 인라인 인용 [G&W pp.XXX] 및 [R&T pp.XXX]는 다음 두 교과서의 페이지를 가리킵니다. 본 보강본에서 추가된 1차 문헌(Sharma & Jusko 1998, Friberg & Karlsson 2002)도 함께 정리합니다.

## A. 주요 교과서

**[G&W 5e] Gabrielsson & Weiner — Pharmacokinetic and Pharmacodynamic Data Analysis**
- 전체 인용 형식: Gabrielsson J, Weiner D. *Pharmacokinetic and Pharmacodynamic Data Analysis: Concepts and Applications.* 5th edition. Stockholm: Apotekarsocieteten (Swedish Pharmaceutical Press); 2016. ISBN 978-91-985558-1-2.
- 본 세션 핵심 참조 단원:
  - **§2.6.7 (pp.110–111)** — Feedback (inherent / positive / negative); **moderator 모델 Eq 2:261–2:263**; IgG saturable protection (11일 plateau); **"R = M at dynamic steady state" 가정 (v4.2_final에서 본문 명시)**
  - §3.7–3.10 (pp.235–260) — Indirect response models, irreversible action, target consumption
  - §3.11 (pp.247–251) — $t_{ss}$, peak shift, graphical estimation
  - §3.12 (pp.272–275) — DRT (Dose-Response-Time) analysis
  - §3.13 (pp.317–319) — Baseline drift, disease progression
  - §6 — PD6 case study (pp.758–763) — Turnover vs effect compartment non-identifiability
  - §7 — PD7 case study (pp.764–769) — Loss-stimulation Model 4 with compound C
  - §9 — PD9 case study (pp.778–783) — Peak shift over-interpretation warning (Zooparc®)
  - §5 — PD5 case study (pp.742–752) — Initial estimation, reparameterization, Pool 1/Pool 2 identifiability
- 본 세션에서 자주 인용되는 식 번호: Eq 2:261, 2:262, 2:263 (moderator/feedback, IgG saturable); Eq 3:74, 3:76 (basic turnover, baseline); Eq 3:77, 3:78 ($I(C)$, $S(C)$); Eq 3:103 (reparameterized form); Eq 3:110, 3:112 (irreversible kill, survival fraction).

**[R&T] Rowland & Tozer — Clinical Pharmacokinetics and Pharmacodynamics**
- 전체 인용 형식: Rowland M, Tozer TN. *Clinical Pharmacokinetics and Pharmacodynamics: Concepts and Applications.* 4th edition. Philadelphia: Wolters Kluwer Health / Lippincott Williams & Wilkins; 2011. ISBN 978-0-7817-5009-7.
- **판본 표기 (v4.2_final 정정)**: 본문 내 일부 "R&T 5e" 표기는 본 자료에서 채택한 통칭 표기로, **실제 인용 근거는 R&T 4판(2011) Chapter 8 — Response: Time Course and Variability**의 페이지 매김입니다. 5판이 출간된 경우 페이지 번호가 다를 수 있으므로, **본 자료의 [R&T pp.XXX] 인용은 4판 기준**임을 명시합니다.
- 본 세션 핵심 참조 단원: **Chapter 8 — Response: Time Course and Variability** (전체).
  - pp.234–236 — Hysteresis 분류, naproxen Fig 8-2
  - pp.239 — Direct PK–PD link, midazolam Fig 8-6
  - pp.241–242 — Ibuprofen Fig 8-9
  - pp.243 — Acenocoumarol vs phenprocoumon, Fig 8-11; PK clock vs PD clock
  - pp.244–247 — Warfarin blocking-dose analysis, Eq 8-6 / Eq 8-7
  - pp.247–249 — Region 2 linear decline, Eq 8-9
  - pp.249–256 — Succinylcholine dose-duration, Eq 8-12
  - pp.251–254 — Irreversible action (aspirin, omeprazole, paclitaxel), Fig 8-22
  - pp.255–256 — Fig 8-23, 8-24 (PK-rate-limited dose duplication → half-life duration)
  - pp.256–258 — Methylprednisolone linear PK ≠ linear PD
  - pp.258–259 — Rosuvastatin/OATP1B1 plasma exposure vs site-of-action disconnect

## B. 본 보강본 추가 1차 문헌

**Sharma & Jusko 1998 — Pool/Precursor Indirect Response (관행적으로 Models V–VIII로 불림)**
- 전체 인용: Sharma A, Jusko WJ. "Characteristics of indirect pharmacodynamic models and applications to clinical drug responses." *British Journal of Clinical Pharmacology.* 1998;45(3):229–239. DOI: 10.1046/j.1365-2125.1998.00676.x.
- 본 보강본 인용 위치: Card 4-보강 (Pool/Precursor 다단계 간접반응)
- 핵심 기여: Single-stage indirect models I–IV를 **precursor pool을 포함하는 framework**로 확장. Corticosteroid, EPO, GH 등 cascade 약물군의 표준 골격.
- **명명법 주의 (v4.2_final 정정)**: **원 논문은 위 확장을 'Model V/VI/VII/VIII'로 명시적으로 번호 부여하지 않습니다.** 'Models V–VIII' 명명은 후속 표준 문헌(Jusko 그룹 후속 review, Mager-Wyska-Jusko 교과서 등)의 관행적 명명으로 굳어진 것입니다. 본 자료에서 V–VIII 표기를 사용할 때는 "(관행적 명명)"을 병기합니다.

**Friberg & Karlsson 2002 — Chemotherapy-Induced Myelosuppression**
- 전체 인용: Friberg LE, Henningsson A, Maas H, Nguyen L, Karlsson MO. "Model of chemotherapy-induced myelosuppression with parameter consistency across drugs." *Journal of Clinical Oncology.* 2002;20(24):4713–4721. DOI: 10.1200/JCO.2002.02.140.
- 본 보강본 인용 위치: Card 6 §D (응용 사례)
- 핵심 기여: 5-compartment 골격(증식 + 3 transit + 순환)과 feedback rebound로 **6개 항암제에서 system parameter($MTT$, $\gamma$)의 약물 간 일관성**을 입증. Oncology PK/PD의 표준 출발점.
- **모델 구조 주의 (v4.2_final 정정)**: 원 논문은 식별성 확보를 위해 **$k_{prol}=k_{tr,1}=k_{tr,2}=k_{tr,3}=k_{circ}\equiv k_{tr}$ (5중 제약)** 을 모델 정의의 일부로 도입합니다. 이 제약은 "흔한 관행"이 아니라 "원 논문 모델 구조의 일부"이며, 제약 하에서만 system parameter $MTT=4/k_{tr}$의 약물 간 일관성이 회수됩니다. 본 자료의 Card 6 §D 표 항목은 이 점을 명시합니다.

## C. 본문 인용 표기 약속

본 자료에서 인라인 인용은 다음 형식을 따릅니다:

| 형식 | 의미 |
|---|---|
| `[G&W Eq 3:74; G&W p.237]` | Gabrielsson & Weiner 5판 식 번호 3:74, 본문 p.237 |
| `[G&W pp.235–236]` | Gabrielsson & Weiner 5판 페이지 범위 |
| `[G&W PD4 pp.742–752]` | Gabrielsson & Weiner 5판 PD4 case study, 본문 페이지 |
| `[R&T Eq 8-12; R&T pp.254–255]` | Rowland & Tozer Ch.8 식 8-12, 본문 페이지 |
| `[R&T pp.234–235, 239]` | Rowland & Tozer Ch.8 페이지 (콤마 = 비연속 페이지) |
| `[Sharma & Jusko 1998]` | 1차 문헌 (보강본에서 추가) |
| `[Friberg \& Karlsson 2002]` | 1차 문헌 (보강본에서 추가) |

> 📖 **인용 정확성 정책**: 본 보강본에서 신규 추가된 모든 수식은 ① 1차 문헌 또는 표준 교과서의 원형을 보존하며, ② annotation은 overbrace/underbrace로 적용하고, ③ 인용은 식별 가능한 페이지/식 번호 또는 DOI를 동반합니다.

<!--
## v4.0 자가검증 체크리스트

| 항목 | 기준 | 결과 |
|---|---|---|
| SLIDE_START 개수 | §섹션수 5 + 카드수 8 합산 | 13 개 |
| 카드당 callout 합계 ≤ 6 | 전체 카드 | ✓ |
| 거장의 시각 존재 | 모든 §2 카드 | ✓ |
| 파라미터 표 존재 | 모든 §2 카드 (Apex 카드 + 정의 수식 카드) | ✓ |
| §5 혼동 쌍 표 행 순서 고정 (4행) | §5 전체 | ✓ |
| 기호 일관성 | 첫 등장 기준 통일 | ✓ |
| 수치 anchor 보존 | Compound A 등 원본 수치 | ✓ |
| 나비효과 이중 종착점 | Apex 카드 | ✓ |
-->

<!-- v4.0 변환 노트
- 보존 감사 (100% 일치):
  · 출처 anchor: 실제 citation 83건(G&W 50건 + R&T 33건) — v3.9 일치
  · 수식 블록 $$: 55건 — v3.9 일치
  · SLIDE_START 마커: 13건(§섹션 5 + 카드 8) — v3.9 일치
  · 약물명 15종(naproxen, aspirin, warfarin, methylprednisolone, rosuvastatin, furosemide, erythropoietin, ibuprofen, midazolam, acenocoumarol, phenprocoumon, omeprazole, paclitaxel, succinylcholine, minoxidil) — 등장 횟수 100% 일치, 첫 등장에 약물 분류 인라인 적용
  · 핵심 수치 anchor(Compound A V=40L K=0.9h⁻¹, IC50≈95, Imax≈0.65, r=0.9999 CV% 4000, k_out=k_e0=5.6 h⁻¹, WRSS 15516/15518, AIC 1041/1040, EC50=1633, methylprednisolone 16/31/63/125/250/500/1000 mg, succinylcholine 22%/min, IgG 30 mg/mL 11일, B_max≈30,000 CFU, PD7 6,400U→0.6 h⁻¹, 160,000U→1.6 h⁻¹) 모두 verbatim 보존
- 주요 변환 (v3.9 → v4.0, Park 교수 빙의):
  · 메타-언어 헤더 0건화: "체화 핵심", "Plausible Fallacy", "치명적 타격" → 산문 흡수 또는 명료 헤더로 교체
  · "잠긴 사례/잠긴 작업 흐름/잠긴 핵심 메시지" 등 "잠긴" 어휘 → "대표 사례", "한 번 정해두면 안 흔들리는 진단 순서"
  · 자기참조 해소: "Mn의 결론이 ~한다" 잔재 0건, 모두 결론 직접 진술
  · 약물 즉맥락화: 모든 약물 첫 등장에 분류·기전 인라인 + "→ 그래서 [개념]의 사례" 마무리 적용
  · 콜아웃 단일화: 카드당 순수 콜아웃 ≤ 5개 (한도 6 이내)
  · "30년 베테랑의 30초 진단 시퀀스" → "실무자가 데이터를 받은 첫 30초 안에 자동으로 돌리는 진단 순서"
  · 시간 메타포로 한 바느질: 전체 세션을 "여러 시계가 동시에 돌아가는 시스템에서 어느 시계가 가장 느린지 찾는 일"로 꿰어 카드 간 의존 관계 명시화
-->

<!-- v4.2_final 보강 감사 노트 (v4.1 → v4.2_final)
- v4.1 본문 전체 보존 (보강 영역의 표 항목 표현 정정 제외, 100% verbatim 일치):
  · 기존 15개 SLIDE_START 마커 유지 (S01-S05, M1-M8, M4_EXT, S09)
  · 기존 모든 수식 블록 $$ 유지 (단 Card 1 moderator 모델 식 3건 추가, Card 6 Friberg-Karlsson 5중 제약식 1건 추가)
  · 기존 약물명 15종 등장 횟수 유지
  · 기존 핵심 수치 anchor 유지

- v4.2_final 정밀화 (2차 검토 반영):
  · 신규 수식 블록 4건 추가:
    - Card 1: G&W moderator 모델 Eq 2:261, 2:262, 2:263 (overbrace/underbrace annotation)
    - Card 1: R=M steady-state 가정의 derivation 검증식 (overbrace/underbrace annotation)
    - Card 6 §D: Friberg-Karlsson 5중 제약식 $k_{prol}=k_{tr,1}=k_{tr,2}=k_{tr,3}=k_{circ}\equiv k_{tr}$ (overbrace/underbrace annotation)
  · 표 항목 표현 정정 (2차 검토 1-3 반영):
    - Card 6 §D 표: $k_{prol}$ 행 "(constraint: $k_{prol}=k_{tr}$)" → "**(모델 구조 제약: $k_{prol}=k_{tr}$)**"
    - Card 6 §D 표: $k_{circ}$ 행 "($k_{circ}=k_{tr}$로 흔히 고정)" → "**(모델 구조 제약: $k_{circ}=k_{tr}$)**"
  · 표 헤더 정정 (2차 검토 1-4 반영):
    - Card 4-보강 §B: 헤더 "Sharma-Jusko Models V–VIII" → "Pool/Precursor 확장 (관행적 Models V–VIII 명명)"
    - 표 행 라벨에 "(관행)" 병기, 명명법 출처 정정 콜아웃 추가
  · 신규 콜아웃 박스 4건 추가:
    - Card 1: "📐 Moderator 모델의 정식 식 구조" (G&W Eq 2:261–2:263 + R=M 가정)
    - Card 4-보강: "📖 명명법 출처 정정 (2차 검토 1-4 반영)"
    - Card 6 §D: "⚠️ System parameter 제약은 '흔한 관행'이 아니라 '원 논문 모델 구조의 일부'"
    - References A: G&W §2.6.7 항목 추가 + R&T 판본 명확화

- 인용 정밀화 (사용자 요청 반영):
  · Sharma-Jusko 1998 1차 문헌 박스: V–VIII 명명이 후속 문헌 관행임을 명시
  · Friberg-Karlsson 2002 1차 문헌 박스: 5중 제약이 원 논문 모델 정의의 일부임을 명시
  · §9 References A: G&W §2.6.7 (pp.110–111)을 핵심 참조 단원 목록에 추가
  · §9 References A: R&T 판본 표기 "5e" → "4판(2011) 기준"으로 명확화
  · §9 References B: 1차 문헌 두 건 모두 v4.2_final 정정 사항을 인용 박스 내 명시

- 변경 정책:
  · 보강 영역 외 본문 텍스트 변경 0건 (v4.1과 동일 정책 유지)
  · 인용 형식 변경 0건 (기존 [G&W pp.XXX] / [R&T pp.XXX] 형식 유지)
  · 약물명, 수치 anchor, 카드 ID, 표 행 순서 모두 v4.1과 일치 (단 Card 4-보강 §B의 헤더 텍스트 및 Card 6 §D의 표 항목 표현이 정확도 향상을 위해 정정됨)

- 2차 검토 반영 위치 (Ch.11 관련 항목만):
  · 검토 1-3 (Friberg-Karlsson $k_{prol}=k_{tr}=k_{circ}$ 제약 명시 부족) → Card 6 §D 표 및 신규 콜아웃·5중 제약식으로 해소
  · 검토 1-4 (Sharma-Jusko V–VIII 원 논문 명명법 차이) → Card 4-보강 §B 헤더·표·콜아웃 및 §9 References B 정정으로 해소
  · 검토 1-8 (Moderator 모델 R=M 가정 명시화) → Card 1 신규 콜아웃 박스(G&W Eq 2:261–2:263 + derivation 검증식)로 해소
  · 사용자 추가 요청: overbrace/underbrace annotation 적용 (신규 수식 4건 모두 적용), G&W/R&T 출처 정밀화 (§9 References A 정정) — 모두 적용

- 자가검증 결과:
  · SLIDE_START 개수: 15건 (v4.1과 동일)
  · 수식 블록 $$ 추가 건수: 4건 (Card 1×3, Card 6 §D×1)
  · 신규 콜아웃 박스: 4건 (Card 1, Card 4-보강, Card 6 §D, §9 References A)
  · 표 항목 표현 정정: Card 6 §D 표 2건, Card 4-보강 표 헤더 1건, 표 라벨 4건
  · v4.1 보존: 카드 구조, 약물 등장, 수치 anchor 100% 일치
-->


# 세션 09 — TMDD: Target-Mediated Drug Disposition, full vs MM approximation, $K_d$/$K_m$/target turnover — v4.0 보강본

이 자료는 Gabrielsson & Weiner 5e의 turnover, PK26 Efalizumab, PK27 TMDD 사례와 Rowland & Tozer 5e Ch.21 Protein Drugs를 학습자용으로 정리한 파일입니다. 다루는 범위는 단백질 약물 PK, mAb 배치, FcRn, TMDD, Michaelis-Menten 근사, 자료 풍부도(data richness), assay 식별성입니다.

---

> **임상 장면**  
> 한 단클론 항체를 **1.5, 5, 15, 45 mg·kg⁻¹** 네 용량으로 급속 정맥 주사한 PK27 데이터를 받았다고 합시다. 고용량 곡선 세 개는 모델이 그럴듯하게 맞춰주는데, 가장 낮은 용량 곡선 하나만 따로 놀아요. 그래서 모델을 두 가지로 돌려봤습니다. MM 모델이 내놓은 $K_m$은 **3.7**, Full TMDD 모델이 내놓은 $K_m$은 **0.03** — **약 123배** 차이입니다. 이건 "피팅이 약간 안 됐다" 수준이 아니에요. 저농도 외삽, trough 예측, target occupancy 판단을 통째로 흔드는 **구조 신호**입니다. 이 세션은 그 신호가 왜 나왔고 어떻게 읽어야 하는지를 다룹니다. [G&W pp.602–603; G&W p.609]

이 세션을 통과하면서 머릿속에 한 질문을 들고 다니세요 — **"이 데이터가 실제로 어떤 파라미터를 가르치고 있는가?"** 곡선이 예쁘게 적합되는가가 아니라 이 질문이 모든 결정의 기준이에요.

다섯 카드 + 한 다리 카드(M4½)가 한 흐름으로 이어집니다.

| 카드 | 다루는 것 |
|---|---|
| **M1** | Turnover paradigm — baseline은 고정값이 아니라 $k_{in}/k_{out}$의 결과 |
| **M2** | 항체의 ADME 네 관문 — distribution / lymphatic input / proteolysis·RME / FcRn rescue |
| **M3** | TMDD 곡선의 Phase A–D — 시간 순서가 아니라 농도 영역의 지도 |
| **M4** | Full TMDD ODE — ligand·target·complex·sink를 한 system으로 |
| **M4½** | **(보강) Full TMDD ↔ MM 사이의 근사 위계와 QSS 근사** — 임상 biologics PopPK 실무의 표준 |
| **M5** | MM 근사가 무너지는 경계 — 저농도 외삽에서 생기는 구조 편향 |

이 세션의 핵심은 "항체 PK가 왜 비선형인가"가 아닙니다. 핵심은 **turnover 수학이 TMDD(target-mediated drug disposition; 표적에 결합한다는 사실 자체가 약물 배치를 바꾸는 현상)로 확장되는 순간, 어떤 자료가 어떤 파라미터를 가르치는지**를 손에 잡히게 만드는 거예요. 그래서 M1~M5(+M4½)는 평행한 주제가 아니라 의존 사슬입니다 — M1이 무너지면 M2가 흔들리고, M3 없이 M4를 보면 phase가 무엇을 가르치는지 모르고, M4 없이 M4½/M5를 보면 어디서 어떤 가정으로 근사가 가능한지 판단할 도구가 없어요.

---

<!-- SLIDE_START: §1 | title: 세션 헤더와 로드맵 -->
<!-- SECTION_CORE: SC-01 -->
# §1 세션 헤더와 로드맵

이 세션의 의사결정 체계는 단순합니다. 위에서 한 줄로 깔아둔 질문 — **"이 데이터가 어떤 파라미터를 가르치는가?"** — 으로 모든 모델 선택을 방어합니다. 그래서 §1에서 다루는 건 카드들이 어떤 순서로 이 질문에 답하느냐예요.

## 어떤 개념이 어떤 층에 있는가

세 층으로 나눠 보면 위치가 잡힙니다.

**Layer 1 — 무엇인가:** Turnover baseline / mAb ADME 관문 / TMDD phase / Full TMDD / MM 경계.

**Layer 2 — 어떻게 계산되는가:** $A_0 = k_{in}/k_{out}$ / $dR/dt$ & $dRL/dt$ / $K_d = k_{off}/k_{on}$ / $K_m = (k_{off} + k_{e(RL)})/k_{on}$ / $Cl_{MM} = V_{max}/(K_m + C)$.

**Layer 3 — 언제·왜 중요한가:** baseline 회복 / 느린 sc 입력 / 저용량 외삽 / target occupancy / 모델 선택 방어.

## 어디에 들어가는 세션인가

선행: 1구획·2구획 선형 PK + Michaelis-Menten + ODE 기본.
이번 세션: Turnover → mAb ADME → TMDD → Full TMDD/MM 경계.
후속: mAb PopPK · TMDD/QSP · target occupancy 시뮬레이션 · biologics 임상약리 리포트.

## 이 세션의 한 줄

항체의 비선형 PK는 "큰 약물이 천천히 빠지는 것"이 아니에요. **Ligand가 endogenous target turnover system에 결합하면서 만들어지는 농도의존적 청소율**입니다. Full TMDD를 MM으로 줄이면 제한된 용량 범위에서는 맞아 보일 수 있는데, PK27에서는 그 결과가 정량적으로 드러났어요 — $K_m$이 **0.03에서 3.7로 약 123배 과대예측**되어, 저농도 외삽이 구조적으로 틀어졌습니다 [G&W p.609].

## 카드 5장 + 다리 카드 1장의 흐름

M1에서 baseline이 왜 단순한 0시간 값이 아니라 turnover pool인지를 잡습니다. 그 위에 M2에서 mAb 곡선의 "느림"이 어떤 ADME 관문들이 합쳐진 결과인지를 봅니다. M3는 그 곡선에 target 결합이 개입했을 때 phase A~D가 어떤 농도 영역을 가리키는지를 다루고, M4는 그 phase를 만드는 ligand·target·complex·sink의 ODE topology를 분해합니다. **M4½(보강)는 Full TMDD ↔ MM 사이의 근사 위계를 명시적으로 깔아두는 다리 카드**로, 임상 biologics PopPK의 실무 표준인 QSS 근사를 소개합니다. 마지막 M5에서 그 사슬의 가장 압축된 끝(MM)을 어디까지 적용할 수 있는지를 판정해요.

이 흐름이 어떤 순서로 어떻게 의존하는지가 모델 선택의 방어 논리 자체입니다 — "왜 Full TMDD가 필요한가" 또는 "왜 QSS이어도 되는가" 또는 "왜 MM이어도 되는가"를 reviewer 앞에서 설명할 때 결국 이 사슬이 답입니다.

**Source**:
- Gabrielsson J, Weiner D. *Pharmacokinetic and Pharmacodynamic Data Analysis: Concepts and Applications*, 5th Edition. Apotekarsocieteten (Swedish Pharmaceutical Press), Stockholm, 2016. — Ch.2 §2.6 Turnover [G&W pp.94–111]
- Gabrielsson J, Weiner D. (위 문헌) — Case Study PK26 Efalizumab [G&W pp.599–601]
- Gabrielsson J, Weiner D. (위 문헌) — Case Study PK27 TMDD [G&W pp.602–610]
- Rowland M, Tozer TN. *Clinical Pharmacokinetics and Pharmacodynamics: Concepts and Applications*, 5th Edition. Wolters Kluwer / Lippincott Williams & Wilkins, Philadelphia, 2019. — Ch.21 Protein Drugs [R&T pp.687–730]
- (보강 카드 근거) Mager DE, Jusko WJ. General pharmacokinetic model for drugs exhibiting target-mediated drug disposition. *J Pharmacokinet Pharmacodyn* 2001;28:507–532. — R&T Fig.21-8 원전 [R&T p.711]
- (보강 카드 근거) Peletier LA, Gabrielsson J. Dynamics of target-mediated drug disposition: characteristic profiles and parameter identification. *J Pharmacokinet Pharmacodyn* 2012;39:429–451. — R&T Fig.21-9 원전 [R&T p.712]

---

<!-- SLIDE_START: §2 | title: 개념 해부 카드 -->
<!-- SECTION_CORE: SC-02 -->
# §2 개념 해부 카드

이 카드들은 한 줄로 묶입니다 — **$k_{in}/k_{out}$이 baseline, pool size, recovery time을 동시에 지배**한다는 사실. Target $R$을 고정값으로 보는 순간 TMDD 해석은 출발점부터 흔들립니다.

---

<!-- SLIDE_START: M1 | title: Turnover Paradigm -->
<!-- SECTION_CORE: SC-03 -->
## ▌ Card M1 — Turnover Paradigm ($k_{in}$/$k_{out}$)

> **거장의 시각**  
> baseline을 predose 값 하나로 처리하면 어떻게 되느냐 — $R_0$, $k_{out}$, recovery time이 전부 "잔차"나 "임의 파라미터"처럼 보입니다. Turnover 관점으로 보면 target $R$은 외부 ligand가 휘젓는 endogenous pool이고, TMDD의 출발점이 명확해져요.

M1의 메시지는 한 줄입니다 — **내인성 물질의 baseline은 고정된 숫자가 아니라, 0차 입력 $k_{in}$이 들어오고 1차 소실 $k_{out} \cdot A$가 빠져나가는 균형의 결과**예요. TMDD의 target $R$도 이 구조를 그대로 따릅니다. 그래서 mAb가 target에 결합한다는 건 외부 ligand가 endogenous turnover pool 안으로 들어와 그 균형을 흔든다는 뜻입니다 [G&W pp.95–96].

### A. 형식적 정의

| 파라미터 | 단위 | 의미 | 변화 원인 |
|---|---|---|---|
| $A$ | mass | turnover pool 안의 양 | 생성·소실 균형 |
| $k_{in}$ | mass/time | 0차 입력·생성률 | 합성 증가/감소 |
| $k_{out}$ | time⁻¹ | 1차 분획 소실률 | catabolism·degradation 속도 |
| $A_0$ | mass | 정상상태 baseline 양 | $k_{in}$↑ 또는 $k_{out}$↓ |
| $t_t$ | time | pool 교체 시간 | 주로 $k_{out}$ 변화 |

$$
\overbrace{\frac{dA}{dt}}^{\text{pool 변화}}
=
\underbrace{k_{in}}_{\text{0차 입력}}
-
\underbrace{k_{out}\cdot A}_{\text{1차 소실}}
\qquad \text{Eq.2:237}
$$

정상상태에서는 입력 = 출력이 성립하면서 다음 관계들이 줄줄이 나옵니다 [G&W pp.95–96].

| 관계식 | 의미 | 출처 |
|---|---|---|
| $k_{in}=k_{out}\cdot A_0$ | 입력 = 출력 | Eq.2:239 [G&W p.96] |
| $k_{out}=k_{in}/A_0$ | 분획 turnover rate | Eq.2:240 [G&W p.96] |
| $A_0=k_{in}/k_{out}$ | baseline 양 | Eq.2:241 [G&W p.96] |
| $t_t=A_0/k_{in}=1/k_{out}$ | turnover time | Eq.2:242 [G&W p.96] |
| $t_t=V_{ss}/Cl=MRT$ | turnover time이 PK MRT와 연결 | Eq.2:243 [G&W p.96] |
| $t_{1/2}=\ln(2)/k_{out}=\ln(2)\cdot t_t$ | 반감기 관계 | Eq.2:244 [G&W p.96] |

$$
\begin{aligned}
\underbrace{A_0}_{\text{baseline 양}} &= \underbrace{\frac{k_{in}}{k_{out}}}_{\text{입력/소실 균형}} \\
\underbrace{t_t}_{\text{교체 시간}} &= \underbrace{\frac{1}{k_{out}}}_{\text{소실 역수}} = \underbrace{\frac{V_{ss}}{Cl}}_{\text{PK 체류시간}} = \underbrace{MRT}_{\text{평균 체류}} \\
\underbrace{t_{1/2}}_{\text{반감기}} &= \underbrace{\frac{\ln(2)}{k_{out}}}_{\text{1차 반감}}
\end{aligned}
$$

단위가 핵심이에요. $k_{in}$은 mass/time, $k_{out}$은 time⁻¹입니다. 이 구분을 놓치면 곧 **target 합성($k_{in}$)과 ligand-target 결합 on-rate($k_{on}$)를 같은 양으로 섞어버립니다** — 이건 M4에서 다시 부각될 텐데 미리 못 박아두는 게 안전해요.

> 💡 **Baseline은 결과값이지 입력값이 아닙니다.** $A_0$는 관찰값 하나가 아니라 $k_{in}/k_{out}$ 균형이 만들어내는 결과예요. 그리고 $k_{out}$이 바뀌면 level뿐 아니라 새 정상상태에 도달하는 시간까지 같이 바뀝니다.

### B. 직관: 욕조

10 L 욕조에 분당 1 L의 물이 들어오면 turnover time은 10분이에요. 사람 몸의 물 42 L와 하루 섭취량 2.5 L를 넣으면 water turnover time은 **약 17일**입니다. 핵심은 "얼마나 많이 있는가"가 아니라 **"지금 pool 전체가 얼마나 빨리 교체되는가"**예요. 이 단순한 욕조 그림이 내인성 IgG, target receptor, hormone turnover 모두에 정확히 같은 수학으로 적용됩니다 [G&W p.96].

여기서 비대칭이 하나 있습니다. $k_{in}$을 바꾸면 정상상태 level만 바뀌고 도달 시간은 그대로예요(linear kinetics 조건에서). 반면 $k_{out}$을 바꾸면 **level과 도달 시간이 같이 바뀝니다** [G&W p.97]. 이 비대칭이 M1 임상 해석의 핵심 갈림길이에요 — 예를 들어 어떤 PD endpoint의 회복이 느려진 게 합성이 줄어든 건지 분해가 느려진 건지에 따라 처치 방향이 완전히 달라집니다.

### C. 임상 앵커 세 가지

**IgX**(내인성 성장호르몬 유사 단백질 펩타이드): IgX 40 µg·kg⁻¹을 sc로 투여해 보면 predose baseline이 32 µg·L⁻¹였고, 추정값으로 $Cl/F=0.03\ \mathrm{L\cdot h^{-1}\cdot kg^{-1}}$, $V/F=0.10\ \mathrm{L\cdot kg^{-1}}$, $k_{in}=0.78\ \mathrm{µg\cdot h^{-1}\cdot kg^{-1}}$, $t_t=2.7\ \mathrm{h}$, $MIT=1.8\ \mathrm{h}$, $t_{1/2}=2.5\ \mathrm{h}$, $k_{out}=0.27\ \mathrm{h^{-1}}$, pool size 2.3 µg·kg⁻¹이 나왔습니다. → 그래서 **endogenous baseline 위에 외부 ligand가 얹히는 turnover 구조**의 사례입니다 [G&W pp.100–101].

$$
\underbrace{t_t}_{\text{pool 교체}} = \underbrace{2.7\ \mathrm{h}}_{\text{IgX}},\quad
\underbrace{k_{out}}_{\text{분획 소실}} = \underbrace{0.27\ \mathrm{h^{-1}}}_{\text{시간당}},\quad
\underbrace{t_{1/2}}_{\text{반감기}} = \underbrace{2.5\ \mathrm{h}}_{\text{프로파일 요약}}
$$

**내인성 IgG**(혈장에 가장 풍부한 면역글로불린): Table 2.11에 따르면 $t_{1/2}=23$ days, 분획이화율(FCR, fractional catabolic rate) 6.7% plasma pool·day⁻¹, turnover 33 mg·kg⁻¹·day⁻¹입니다. R&T가 "치료용 mAb 반감기는 대략 21일"이라고 하는 숫자와 비슷한 영역이긴 한데, **두 문장을 합치면 안 돼요** — 내인성 IgG는 단일 분자종이고, 치료용 mAb는 후보별로 FcRn 친화도가 다 다릅니다. → 그래서 **숫자가 비슷해도 같은 사실로 묶지 못한다**는 사실의 사례입니다 [G&W p.102; R&T p.708].

$$
\underbrace{t_{1/2}}_{\text{IgG 반감기}} = \underbrace{23\ \mathrm{days}}_{\text{내인성 IgG}},\qquad
\underbrace{\mathrm{FCR}}_{\text{분획 이화율}} = \underbrace{6.7\%\ \mathrm{day^{-1}}}_{\text{혈장 pool}}
$$

**Estradiol**(내인성 에스트로겐, E2): 폐경 후 여성 15명에서 estradiol은 평균 $k_{in}=19\ \mathrm{µg\cdot 24h^{-1}}$, $Cl=1.6\ \mathrm{L\cdot min^{-1}}$, $V_{ss}=50\ \mathrm{L}$, $t_{1/2}=26\ \mathrm{min}$, $MRT=18\ \mathrm{min}$로 보고됐어요. 임상 포인트가 있습니다 — 폐경 후 낮은 E2 level은 **청소율이 늘어서가 아니라 turnover의 생성(즉 $k_{in}$)이 줄어서** 만들어집니다. 같은 수식 안에서 분자가 작아진 거예요. → 그래서 **level 하나만 봐서는 원인이 합성 쪽인지 분해 쪽인지 알 수 없다**는 사실의 임상 사례입니다 [G&W pp.102–104].

$$
\underbrace{k_{in}}_{\text{E2 생성률}} = \underbrace{19\ \mathrm{\mu g\cdot 24h^{-1}}}_{\text{평균 입력}},\quad
\underbrace{Cl}_{\text{제거능}} = \underbrace{1.6\ \mathrm{L\cdot min^{-1}}}_{\text{전신 CL}},\quad
\underbrace{MRT}_{\text{평균 체류}} = \underbrace{18\ \mathrm{min}}_{\text{교체 척도}}
$$

### D. 가정과 경계조건

Turnover 수학은 **baseline이 의미 있게 정의될 때**만 강력합니다. 그런데 baseline이 항상 상수인 건 아니에요 — 진동(oscillating)할 수도, feedback이 걸려 있을 수도, Zeitgeber(외부 시간 신호)에 따라 움직일 수도 있습니다. PD endpoint를 다룰 때 첫 질문은 "predose 농도를 baseline으로 빼도 되는가?"가 아니라 **"이 endpoint는 어떤 baseline scenario인가?"**예요 [G&W p.104].

**실무 팁**: predose target 측정값이 있으면 단순히 `R0=THETA`로만 추정하지 말고, baseline DV record로 모델에 들어가도록 설계하세요. 이렇게 해야 $R_0$의 individual variability가 residual error로 흡수되지 않습니다. 이건 교과서 수식을 NONMEM 구현 쪽에서 해석한 거지 원문 control stream이 아니에요.

### E. 한계

Turnover 관계식은 linear first-order loss를 전제로 합니다. 농도가 충분히 높아져서 saturable metabolism이 개입하면 Michaelis-Menten 또는 feedback model이 필요해져요. Hyaluronan, body temperature, feedback 예시들은 이 경계를 보여주는 맥락이지 독립 MUST가 아닙니다 [G&W pp.95, 105–111].

> 📖 **G&W p.97, Fig.2.70**: 두 패널이 보여주는 건 **turnover의 비대칭**이에요. $k_{in}$을 바꾸면 정상상태 level만 움직이는데, $k_{out}$을 바꾸면 level과 도달 시간이 함께 움직입니다. 두 패널을 직접 안 보면 두 변화를 다 그냥 "rate 변화"로 묶어버리기 쉬워요.

$$
\underbrace{k_{in}\uparrow}_{\text{입력 증가}}
\Rightarrow
\underbrace{A_0\uparrow}_{\text{level만 상승}},
\qquad
\underbrace{k_{out}\uparrow}_{\text{분획 소실 증가}}
\Rightarrow
\underbrace{A_0\downarrow}_{\text{level 하강}}+\underbrace{t_t\downarrow}_{\text{도달 시간 단축}}
$$

**이번 카드 핵심내용**: Turnover를 모르면 $R_0$, $k_{out}$, baseline correction, target recovery가 전부 "피팅 파라미터"로만 보입니다. 반대로 turnover를 이해하면 **TMDD는 endogenous biology 위에 얹힌 PK model**로 보여요. baseline과 회복 시간을 같이 설명할 때는 $k_{in}/k_{out}$ 구조가 결정하고, level 변화와 time-scale 변화를 구분하려면 $k_{out}$ 변화가 둘 다를 동시에 흔든다는 사실을 기억해야 합니다. predose 값을 고정 baseline으로만 처리하면 $R_0$ variability와 recovery 해석이 residual error로 흡수돼요. M2부터는 그 ligand 자체가 어떤 ADME 관문을 통과하는지 따져봅니다.

---

<!-- SLIDE_START: M2 | title: Protein/Antibody Distinctive PK -->
<!-- SECTION_CORE: SC-04 -->
## ▌ Card M2 — 단백질/항체의 특수한 PK

M1에서 target이 turnover pool이라는 걸 잡았으니, 이제 그 pool에 들어가는 ligand 자체를 봅니다. 항체라면 small molecule과 전혀 다른 ADME 관문을 먼저 통과해야 해요.

> **거장의 시각**  
> mAb의 곡선을 "반감기 숫자 하나"로 설명하려고 하면, slow input, FcRn salvage, target-mediated sink가 전부 terminal slope에 뭉뚱그려집니다. **네 개의 ADME 관문으로 나누면 어떤 데이터가 absorption을, distribution을, elimination을, rescue를 가르치는지가 분리돼요.**

단백질 약물과 mAb는 small molecule처럼 "잘 녹고 전신으로 퍼진 뒤 간이나 신장으로 빠지는" 물질이 아닙니다. 큰 분자량, 제한된 capillary permeability, 림프관 입력, proteolysis, 수용체 매개 흡수(receptor-mediated uptake; 수용체에 결합한 뒤 세포 안으로 들어가는 경로), **FcRn salvage**(IgG를 분해 직전에서 다시 회수해 순환으로 돌려보내는 기전) — 이게 ADME의 기본 문법이에요 [G&W pp.97–100; R&T pp.701–724].

### A. 형식적 정의

| 파라미터/범위 | 단위 | 의미 | 변화 원인 |
|---|---|---|---|
| $V_{ss}$ | L·kg⁻¹ | plasma/interstitial 중심의 제한 분포 | 분자 크기, vascular permeability |
| MW 역치 | g/mol | 림프관 경로 우세 전환 기준 | 분자량 증가 |
| $F$ | fraction | sc/im 생체이용률 | injection site, proteolysis, 림프관 통과 |
| $T_{max}$ | time | 느린 전신 유입의 척도 | absorption-rate limitation |
| FcRn | mechanism | IgG/mAb recycling salvage | FcRn binding, endosomal recycling |

mAb의 distinctive feature는 네 관문으로 묶을 수 있어요.

| 관문 | 의미 | 출처 |
|---|---|---|
| **Distribution** | $V_d$가 작고 plasma/interstitial space로 분포가 제한 | Table 21-6 [R&T pp.701–702] |
| **Absorption** | sc/im 후 큰 단백질은 주로 림프관으로 천천히 전신에 유입 | Table 21-13 [R&T p.718] |
| **Elimination** | 작은 단백질은 신장이 핵심, 큰 mAb는 proteolysis와 수용체 매개 경로가 중심 | [G&W pp.98–99; R&T pp.704–708] |
| **Rescue (FcRn)** | IgG/mAb를 acidic endosome에서 결합·recycling, lysosomal degradation 회피 | Fig.21-5 [R&T p.709] |

> 💡 **mAb 곡선의 "느림"은 단일 원인이 아닙니다.** 제한된 분포 + 림프관 입력 + proteolysis·RME + FcRn rescue가 합쳐져서 나오는 결과예요. 그래서 sc 투여 terminal slope를 그대로 elimination 반감기로 읽으면 absorption-rate limitation을 놓칩니다. terminal phase를 해석하기 전, 네 관문 중 어느 쪽이 지배하는지 먼저 적어보세요.

### B. 네 관문 풀어보기

**Distribution**: R&T Table 21-6은 단백질 약물의 $V_{ss}$가 대체로 **0.04–0.23 L·kg⁻¹** 범위라고 보여줍니다. body water 전체(약 0.6 L·kg⁻¹)에 비하면 작은 숫자죠. 큰 biologic이 body water 전반이 아니라 plasma/interstitial space에만 갇혀 있다는 뜻이에요 [R&T pp.701–702].

$$
\underbrace{V_{ss}}_{\text{SS 분포용적}}
\approx
\underbrace{0.04\text{--}0.23\ \mathrm{L\cdot kg^{-1}}}_{\text{제한 분포}}
$$

G&W는 cynomolgus monkey에 실험용 항체를 0.77–771 µmol·kg⁻¹ 다섯 단계 오름 용량으로 투여한 사례를 보여주면서, **단순한 central compartment 가정만으로 항체 배치를 설명하면 위험하다**고 경고합니다. 또 정상·신장절제 rat에서 r-hSOD(재조합 인간 superoxide dismutase)를 가지고 큰 단백질의 낮은 $V_d$와 renal clearance 손실을 함께 보여줘요 [G&W pp.99–100].

**Lymphatic absorption**: G&W는 sc 단백질·펩타이드 흡수가 낮고 erratic하고 지연된다는 것, 그리고 림프 흐름이 대략 2 L/day라는 걸 정리합니다. R&T Table 21-13은 그 위에 분자량 기준을 얹어요 — **15,000–20,000 g/mol을 넘는 분자는 주로 림프관을 통해 전신에 들어간다**는 거예요 [G&W p.97; R&T p.718].

$$
\underbrace{MW}_{\text{분자량}}
>
\underbrace{15{,}000\text{--}20{,}000\ \mathrm{g/mol}}_{\text{림프 경로 역치}}
\Rightarrow
\underbrace{\mathrm{lymphatic\ input}}_{\text{느린 전신 유입}}
$$

여기서 한 가지 주의 — R&T Fig.21-16에서 양(sheep)에 0.246–19 kDa water-soluble 화합물 데이터로 "분자량이 클수록 림프 회수율이 증가한다"는 **방향성**을 볼 수 있는데, 이 데이터를 150 kDa mAb에 직선 외삽해서 구체적 회수율 퍼센트를 계산하면 안 됩니다. 그림은 방향성 증거이지 외삽 공식이 아니에요 [R&T p.720].

**Absorption-rate limitation의 사례 — somatropin**(재조합 성장호르몬, 22 kDa): iv 반감기가 약 **2.1시간**으로 짧아요. 그런데 sc로 주면 혈장 농도가 훨씬 더 길게 지속됩니다. → 그래서 **terminal profile이 elimination이 아니라 slow input에 의해 rate-limited될 수 있다**는 사실의 임상 사례입니다 [R&T p.721].

**Renal disease의 사례 — anakinra**(재조합 IL-1 수용체 길항제, 17,258 g/mol): 신기능이 떨어지면 청소율도 같이 떨어져서 노출이 늘어납니다. 반면 full-size mAb나 매우 큰 단백질은 사구체 여과를 거의 받지 않아 신질환 영향이 일반적으로 작아요. → 그래서 **"단백질이면 신장이 중요하다"가 아니라 크기에 따라 갈린다**는 사실의 임상 사례입니다 [R&T p.724].

### C. FcRn과 FcγR

FcRn은 내인성 IgG와 치료용 mAb의 긴 반감기를 설명하는 핵심 salvage 기전이에요. R&T는 mAb 반감기가 IgG에 가까운 **약 21일**인 경우가 많다고 합니다. 그런데 이건 모든 mAb에 통하는 고정 숫자가 아니에요. FcRn 친화도, target-mediated clearance, immunogenicity, dose level에 따라 apparent 반감기가 달라집니다 [R&T pp.708–710].

FcγR 매개 청소율도 무시할 수 없어요. R&T에 따르면 **methotrexate**(MTX, 항대사·면역억제제)를 류마티스 관절염 환자에서 **adalimumab**(anti-TNFα IgG1 mAb)에 같이 쓰면 adalimumab의 청소율이 **29–44% 감소**할 수 있습니다. → 그래서 **FcγR은 변두리 디테일이 아니라 특정 질환·병용약물 맥락에서 clearance covariate가 된다**는 사실의 임상 사례입니다 [R&T p.706].

### D. TMDD에 왜 중요한가

mAb의 느린 흡수와 작은 $V_d$를 모르면 TMDD 곡선을 잘못 읽어요. 이유는 두 개입니다 — 첫째, sc 투여에서는 **Phase A의 rapid binding 신호가 absorption phase에 묻혀버릴 수 있고**(→ M3), 둘째, FcRn rescue가 작동하는 mAb에서는 "terminal slope = simple elimination 반감기"라는 해석이 위험해집니다.

### E. 가정과 한계

"mAb 반감기 ≈ 21일"은 유용한 사전 정보긴 한데, 분자별 FcRn binding 증거와 target-mediated clearance를 확인한 다음에 써야 해요 [R&T p.708].

$$
\underbrace{t_{1/2,\mathrm{mAb}}}_{\text{mAb 겉보기 t½}}
\approx
\underbrace{21\ \mathrm{days}}_{\text{IgG식 prior}}
$$

ADA(anti-drug antibody)와 immunogenicity는 PK 자체를 바꿀 수 있으니, 설명되지 않는 청소율 증가가 보이면 target biology뿐 아니라 ADA도 같이 점검해야 합니다 [R&T p.725].

sc mAb의 $T_{max}$는 보통 며칠 단위예요. Table 21-15 예시를 보면 — **adalimumab**: $F=0.64$, $T_{max}=5.5$ days, $t_{1/2}=30$ days. **omalizumab**(anti-IgE IgG1 mAb, 천식·만성 두드러기 치료제): $F=0.62$, $T_{max}=7.5$ days, $t_{1/2}=26$ days. **efalizumab**(anti-CD11a IgG1 mAb, 건선 치료제): $F=0.50$, $t_{1/2}=17$ days. → 그래서 **sc 입력이 느려서 며칠짜리 $T_{max}$를 만든다**는 사실의 사례 모음입니다 [R&T p.723].

$$
\underbrace{T_{max}}_{\text{Tmax}}
=
\underbrace{5.5\text{--}7.5\ \mathrm{days}}_{\text{느린 sc 입력}}
,\qquad
\underbrace{F}_{\text{생체이용률}}
\approx
\underbrace{0.50\text{--}0.64}_{\text{예시 범위}}
$$

> 📖 **R&T p.709, Fig.21-5**: FcRn salvage는 "긴 반감기"라는 라벨이 아니라 **recycling 기전**이에요. 이 그림은 IgG/mAb가 acidic endosome에서 FcRn에 결합한 뒤 어떻게 분해를 피하고 다시 순환으로 돌아오는지를 단계별로 보여줍니다.

**이번 카드 핵심내용**: mAb의 느림은 반감기 숫자 하나가 아니라 **tissue access + lymphatic transit + FcRn recycling + target/수용체 매개 sink**가 합쳐진 결과입니다. sc/im mAb 곡선이 길게 이어진다면 림프관 입력과 absorption-rate limitation을 먼저 의심하고, "terminal slope = elimination 반감기"라고 단정하기 전에 FcRn과 target 효과를 확인하세요. 이 네 관문을 분리해 두면 다음 M3에서 phase A~D가 무엇을 가르치는지 분리해서 읽을 수 있어요.

---

<!-- SLIDE_START: M3 | title: TMDD 4-Phase Concentration-Time Profile -->
<!-- SECTION_CORE: SC-05 -->
## ▌ Card M3 — TMDD 4-Phase Concentration-Time Profile

M2의 ADME 네 관문을 통과한 곡선이라도, target 결합이 개입하는 순간 곡선은 더 이상 시간표가 아니라 **농도 영역의 지도**가 됩니다.

> **거장의 시각**  
> Phase A–D를 시간 순서로 외우면 저용량 곡선이 가르치는 saturation 경계를 못 잡아요. **농도 위계로 읽으면 "보이는 phase가 곧 식별 가능한 mechanism"**이라는 단순한 판단 기준이 생깁니다.

TMDD 곡선은 그냥 "비선형 곡선"이 아닙니다. **Ligand 농도가 target 농도, $K_d$, $K_m$, saturation 경계를 차례로 지나갈 때 지배 청소 경로가 바뀌는 기록**이에요. 그래서 Phase A–D는 시간 구간이 아니라 **농도 위계(concentration hierarchy)**입니다 [G&W pp.604–610; R&T pp.711–712].

### A. 형식적 정의

| 파라미터/기준 | 단위 | 의미 | 변화 원인 |
|---|---|---|---|
| $C_L$ | concentration | ligand 농도 | dose, distribution, CL, binding |
| $R_0$ | concentration/amount | baseline target 수준 | turnover, target burden |
| $K_m$ | concentration | apparent saturation 경계 | binding + complex sink |
| $K_d$ | concentration | binding/dissociation 경계 | $k_{off}/k_{on}$ |
| Phase A–D | regime | dominant clearance route 변화 | 농도가 역치를 넘으면서 |

여기서 이 세션의 척추가 되는 데이터셋을 다시 꺼냅니다 — **PK27**이에요. 이 실험은 단클론 항체를 **1.5, 5, 15, 45 mg·kg⁻¹** 네 용량으로 급속 정맥 주사한 데이터입니다. 용량별로 층화해서 곡선을 보는 게 왜 핵심이냐 — 곡선이 어떤 phase를 실제로 관찰했는지가 용량마다 다르기 때문이에요 [G&W pp.602–603].

PK27과 R&T가 정리한 네 phase는 다음과 같습니다 [G&W p.610; R&T p.712].

| 단계 | 지배 과정 | 해석 |
|---|---|---|
| **A** | 빠른 2차 결합 | ligand와 target이 빠르게 평형 |
| **B** | "느린" 1차 배치 (target 포화 영역) | target 경로 포화 → **비특이적 linear clearance가 지배** |
| **C** | 혼합차수 배치 | target 부분 포화, 선형과 target-mediated 경로 공존 |
| **D** | $k_{off}$와 $k_{e(RL)}$ 주도의 말기상 | 매우 낮은 ligand, target-specific 제거가 가시화 |

> ⚠️ **Phase B의 "느린"은 Phase A 대비 상대어입니다.** 표준 TMDD 문헌(Mager & Jusko 2001; Peletier & Gabrielsson 2012)과 R&T 본문은 Phase B를 "drug is mainly eliminated directly by a **first-order process**"로 기술해요 [R&T p.712]. 즉 Phase B는 **target 결합 경로가 포화돼서 nonspecific linear clearance가 지배하는 영역**이고, 절대적 청소율 척도로는 **Phase D보다 빠릅니다** (저농도 Phase D에서는 $k_{off}$·$k_{e(RL)}$ 주도의 매우 느린 말기 기울기). "느린"이라는 단어 때문에 phase 순서를 "A→B→C→D = 빨라짐→느려짐"으로 단조 해석하면 곤란해요. 농도 위계가 시간 위계와 반드시 일치하는 게 아닙니다.

> 💡 **Phase 라벨은 시간이 아니라 농도 영역의 지문이에요.** A→B→C→D는 ligand 농도가 $R_0$, $K_m$, $K_d$ 경계를 어떻게 통과하느냐의 기록입니다. 고용량 곡선만 가지고 있으면 target-mediated 경로가 포화돼서 **곡선이 선형처럼 보일 수 있어요.** Full TMDD와 MM 중 무엇을 쓸지 결정하기 전에, 용량별 층화 곡선에서 실제로 관찰된 phase가 무엇인지 먼저 표시해 두세요.

### B. 시간 순서가 아닌 농도 위계

초심자는 Phase A→B→C→D를 시간 순서로 읽습니다. 숙련된 모델러는 같은 곡선을 ligand 농도가 $R_0$, $K_m$, $K_d$를 차례로 지나는 **농도 위계**로 읽어요. PK27에서는 $R_0\approx 12\ \mathrm{mg\cdot L^{-1}}$, $K_m\approx 0.03\ \mathrm{mg\cdot L^{-1}}$이고, $K_d$는 $k_{off}/k_{on}$으로 정의됩니다. **이 역치들 때문에 저용량 곡선이 고용량 곡선에서는 안 보이던 기울기를 드러내요** [G&W pp.603–610].

$$
\underbrace{C_L}_{\text{ligand 농도}}
\quad\text{통과}\quad
\overbrace{\underbrace{R_0}_{\text{target 기준}},\ \underbrace{K_m}_{\text{겉보기 경계}},\ \underbrace{K_d}_{\text{결합 경계}}}^{\text{phase 전환점}}
$$

### C. 곡선이 가르치는 것, 가르치지 않는 것

곡선의 한계를 한 줄씩 짚자면 이렇습니다 [G&W pp.603–609].

- 고용량 데이터만 봤다면 target-mediated 경로는 이미 포화 상태라 **선형처럼 보입니다**.
- assay 민감도가 낮아 저용량 데이터가 빠지면 Phase A와 D를 못 봅니다.
- sc 흡수가 느리면 초기의 rapid binding이 input kinetics 뒤에 가려져요.
- target과 complex 데이터가 없으면 ligand-only 적합이 잘 맞아 보여도 $k_{on}$, $k_{off}$, $k_{e(RL)}$의 정밀도는 그대로 낮은 채로 남습니다.

### D. 실무 판독 규칙

TMDD plot은 **용량별로 층화**해서 점검하는 게 첫걸음입니다. 고용량 곡선은 잘 맞는데 저용량 잔차가 체계적으로 한쪽으로 편향돼 있다면, 모델은 phantom linearity를 가지고 있어요 — 중심에서는 겉보기에 성공이지만 저농도 외삽에서는 편향이 숨어 있는 상태입니다. 이건 PK27 MM 실패에서 나온 진단 해석이지 교과서가 직접 NONMEM rule로 명시한 건 아니에요 [G&W p.609].

### E. 한계

이 네 phase가 가장 선명하게 보이는 건 풍부하고 고품질인 다용량 IV 데이터셋이에요. 임상 현장의 희박 샘플링, sc 흡수, total과 free assay의 모호함, 막결합 target(membrane-bound target) — 이런 조건들은 phase 경계를 흐립니다 [G&W pp.604–605].

> 📖 **R&T p.712, Fig.21-9 (+ G&W p.610, Fig.27.7)**: 이 그림은 Phase A–D를 시간 구간으로 외우는 흔한 실수를 막아 줘요. 각 phase는 target saturation과 $K_m$, $K_d$ 경계에 묶인 **농도 영역의 지문**으로 읽어야 합니다.

$$
\overbrace{\mathrm{Phase\ A\to B\to C\to D}}^{\text{농도 영역 지문}}
\sim
\underbrace{C_L}_{\text{ligand}}
\text{ relative to }
\underbrace{R_0,K_m,K_d}_{\text{포화/결합 기준}}
$$

**이번 카드 핵심내용**: Phase A–D는 그림 설명이 아니라 **model-selection checklist**입니다. 보이는 phase가 곧 식별 가능한 mechanism이에요. TMDD 곡선의 phase를 읽을 때 ligand 농도가 $R_0$, $K_m$, $K_d$ 위계 중 어디에 있는지를 따지고, 고용량 적합만 평가하는 함정을 피해야 phantom linearity에 안 속습니다. Phase A–D를 단순 시간 구간으로 암기하면 저용량 외삽에서 model-selection 근거를 잃어요. 다음 M4에서는 이 phase를 만드는 ODE topology 자체를 분해합니다.

---

<!-- SLIDE_START: M4 | title: Full TMDD Model -->
<!-- SECTION_CORE: SC-06 -->
## ▌ Card M4 — Full TMDD Model [⚡ Apex Concept]

M3에서 phase가 농도 영역의 지문이라는 걸 잡았다면, 이제 그 지문을 만들어내는 ligand·target·complex·sink 항을 ODE 안에서 따로따로 분리합니다.

> **거장의 시각**  
> Full TMDD는 "MM에 target·complex라는 생물학적 이름표를 붙인 복잡한 saturable clearance 모델"이 아니에요. **ligand disposition, target turnover, binding, complex sink를 서로 다른 state와 ODE 항으로 분리하는 모델**입니다. 이걸 명확히 안 잡으면 한 마디로 못 박을 수 있어요 — **관찰 species가 없는 mechanism은 추정값이 아니라 가정입니다.**

### Big Idea

Full TMDD는 ligand disposition, target turnover, ligand-target binding, complex loss를 하나의 mechanistic system으로 묶습니다. 하나의 ODE system(시간에 따른 상태변화 방정식 묶음)이 PK와 target biology를 동시에 추적해요. PK27은 이걸 "8-parameter full TMDD model"이라고 부르는데, $V_c=0.05\ \mathrm{L\cdot kg^{-1}}$를 fixed해 둔 상태에서 Table 27.2가 보고하는 8개의 추정 파라미터를 말합니다. fixed $V_c$까지 structural quantity로 세면 ligand central, ligand tissue, target, complex의 **4 state와 9 structural quantities**가 있어요 [G&W pp.603, 608–609].

### A. 형식적 구조

| 파라미터 | 단위 | 의미 | 변화 원인 |
|---|---|---|---|
| $L_c$ | amount/conc | central ligand state | dose, CL, distribution, binding |
| $L_t$ | amount/conc | tissue/peripheral ligand state | 구획 간 분포 |
| $R$ | target scale | free target/수용체 | $k_{in}$, $k_{out}$, binding 소모 |
| $RL$ | complex scale | ligand-target complex | $k_{on}$, $k_{off}$, $k_{e(RL)}$ |
| $V_c$ | L·kg⁻¹ | PK27에서 fixed central volume | 구조 가정, 민감도 분석 대상 |

상태변수는 4개예요 [G&W pp.604–607; R&T p.711].

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

PK27 Table 27.2의 8개 보고 파라미터는 $Cl$, $k_{on}$, $k_{off}$, $V_t$, $Cl_d$, $k_{out}$, $R_0$, $k_{e(RL)}$입니다. $V_c$는 $0.05\ \mathrm{L\cdot kg^{-1}}$로 fixed돼 있어요 [G&W pp.608–609].

$$
\overbrace{\{Cl,k_{on},k_{off},V_t,Cl_d,k_{out},R_0,k_{e(RL)}\}}^{\text{PK27 8개 추정값}}
\quad ; \quad
\underbrace{V_c}_{\text{central volume}}
=
\underbrace{0.05\ \mathrm{L\cdot kg^{-1}}}_{\text{고정 구조가정}}
$$

> 💡 **Topology가 먼저예요.** Full TMDD의 핵심은 파라미터 개수가 아니라 ligand·free target·complex·sink의 **연결 구조**입니다. M1에서 못 박은 것처럼 $k_{in}$(target 합성)과 $k_{on}$(ligand-target 결합)을 섞으면 안 돼요 — process 자체가 다른 양이에요. 그리고 식별성의 분업은 단순합니다 — **ligand는 disposition을, target은 recovery와 saturation을, complex는 sink를 가르칩니다.**

### B. 기전 방정식

개념 구조부터 봅니다.

```text
Ligand central/tissue distribution:
  nonspecific Cl(L), Cld, Vc, Vt

Target turnover:
  dR/dt = kin - kout·R - kon·L·R + koff·RL

Complex dynamics:
  dRL/dt = kon·L·R - koff·RL - ke(RL)·RL
```

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

결합 속도항은 $k_{on}\cdot L\cdot R$이지 $k_{in}\cdot L\cdot R$이 아니에요. $k_{in}$은 **target 합성** 쪽이고, $k_{on}$은 ligand-target 결합의 **2차 on-rate**입니다. 표기 차이가 아니라 **turnover process와 binding process를 분리**하는 핵심 갈림길이에요 [G&W p.604; G&W pp.606–607].

$$
\underbrace{\mathrm{BIND}}_{\text{complex 형성속도}}
=
\underbrace{k_{on}}_{\text{2차 on-rate}}
\cdot
\underbrace{L}_{\text{ligand}}
\cdot
\underbrace{R}_{\text{free target}}
\quad \ne \quad
\underbrace{k_{in}\cdot L\cdot R}_{\text{process 혼합}}
$$

### C. 식별가능성 — 어떤 데이터가 어떤 항을 가르치는가

이게 이 카드, 그리고 이 세션 전체의 결론에 가까운 부분이에요. PK27은 세 데이터셋을 비교합니다 — **I = ligand 단독, II = ligand + target, III = ligand + target + complex.** target과 complex 시간경과 데이터가 추가될수록 $k_{on}$, $k_{off}$, $k_{e(RL)}$의 정밀도가 좋아져요. Table 27.2에서 dataset I→II→III로 갈 때 $k_{on}$ CV%는 **17→2→1**, $k_{off}$는 **27→13→3**, $k_{e(RL)}$는 **27→23→2**로 개선됩니다 [G&W pp.603, 608–609].

$$
\begin{aligned}
\underbrace{CV\%(k_{on})}_{\text{kon 정밀도}} &: \underbrace{17\to2\to1}_{\text{자료 풍부도}},\\
\underbrace{CV\%(k_{off})}_{\text{koff 정밀도}} &: \underbrace{27\to13\to3}_{\text{target/complex 추가}},\\
\underbrace{CV\%(k_{e(RL)})}_{\text{sink 정밀도}} &: \underbrace{27\to23\to2}_{\text{complex 측정 효과}}
\end{aligned}
$$

한 줄로 정리하면 — **ligand 데이터는 nonspecific disposition과 가시적 phase 구조를, target 데이터는 recovery와 saturation 경계를, complex 데이터는 sink 거동을 가르칩니다.** 자료 풍부도는 장식이 아니에요. **어떤 ODE 항이 추정 가능해지는지를 결정하는 변수**입니다.

### D. 적합 품질 ≠ 기전 타당성

여기 자주 깔리는 함정이 있어요. Full TMDD와 MM 둘 다 saturable clearance를 표현하니까, 고용량 적합이 좋으면 같은 모델로 봐도 된다고 생각하기 쉽습니다. 그럴싸한 이유가 있죠 — PK27에서 가장 높은 세 ligand 곡선은 reduced model로도 꽤 잘 맞아 보이거든요. 그런데 이 한 줄을 믿고 가면 어떻게 되느냐. 고용량 적합 신뢰 → **$K_m$이 123배 과대예측되는 걸 못 잡음** → 임상에서는 trough·target occupancy·subgroup 저농도 노출 판단이 통째로 흔들리고, 모델링·규제 쪽에서는 저용량 잔차와 외삽 근거 부족 때문에 sensitivity analysis와 재분석 요구를 받게 됩니다 [G&W p.609].

한 줄로 정리해서 다시 말하면 이렇습니다 — reduced model은 가장 높은 세 ligand 곡선은 상당히 잘 맞추지만 **가장 낮은 곡선에서는 실패**합니다. PK27에서 MM 모델의 $K_m$은 3.7, Full TMDD의 $K_m$은 0.03 — **약 123배 과대추정**입니다. 이 편향은 trough 예측, target occupancy 추정, subgroup 외삽으로 그대로 전파돼요. 정량 영향은 일반 주장이 아니라 약물·환자 집단별 sensitivity analysis로 평가해야 합니다 [G&W p.609].

$$
\underbrace{\frac{K_{m,\mathrm{MM}}}{K_{m,\mathrm{TMDD}}}}_{\text{MM bias}}
=
\underbrace{\frac{3.7}{0.03}}_{\text{PK27 비교}}
\approx
\underbrace{123}_{\text{123배 과대}}
$$

이 함정을 한 단계 더 풀어보면, MM 근사는 drug $\gg$ target 조건($L \gg R$ 또는 $L \gg K_d$에서 binding이 빠르게 quasi-equilibrium에 도달하고 target 경로가 지속 포화)에서만 Full TMDD로부터 구조적으로 유도됩니다. Full TMDD는 binding($k_{on}\cdot L\cdot R$), 약물-target 복합체 형성($RL$), complex internalization($k_{e(RL)}$), target turnover($k_{in}/k_{out}$)를 4-state ODE로 명시적으로 인코딩하고요. **근사 조건이 깨지는 농도 영역** — ligand 농도가 $K_d$ 또는 $K_m$ 부근(target saturation 전환점)으로 떨어지는 구간, 그리고 매우 낮은 농도의 linear regime — 에서 MM 근사는 PK 거동을 구조적으로 잘못 예측해요. PK27의 $K_m$ 0.03 vs 3.7이 바로 이 경계 위반의 정량 흔적입니다 [G&W p.609].

실무에서는 어떻게 드러나느냐 — 저용량 Phase 1 데이터에서 MM 모델이 OFV·VPC 기준으로 잘 맞은 것처럼 보일 수 있어요. 그런데 중간 용량 범위의 비선형 전환점(Phase B↔C↔D 전이)을 mechanistic하게 예측 못 해서 Phase 2 dose selection이 어긋납니다. 또는 고용량 데이터셋만으로 적합된 MM이 sub-population(저체중, 고 target burden, 초기 dose interval) 외삽에서 trough 노출을 체계적으로 잘못 예측해서, 후속 임상 의사결정의 출발점이 흔들려요.

### E. NONMEM 스타일 구현 노트

다음은 교과서 control stream이 아니라 **PK27/R&T ODE 구조를 NONMEM 스타일로 교육 목적 번역**한 골격이에요. 단위 정합성을 학습자가 직접 확인할 수 있도록 **두 가지 표기 선택지**로 명시합니다.

**(a) 모든 상태변수를 농도(concentration)로 두는 경우** — R&T Eq.21-1~21-4의 표기와 일치합니다 [R&T p.711].

```text
; (a) concentration-based: A(i) is treated as a concentration directly
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

**(b) 모든 상태변수를 amount로 두고 명시적 volume 변환을 박는 경우** — NONMEM의 표준 DADT 표기와 일치합니다.

```text
; (b) amount-based: A(i) is an amount; convert to concentration before binding
CLIG = A(1)/VC      ; central concentration
CTIS = A(2)/VT      ; tissue concentration
RC   = A(3)/VR      ; free target concentration (VR may equal VC for plasma target)
RLC  = A(4)/VR      ; complex concentration

BIND = KON * CLIG * RC * VR    ; amount/time — explicit volume conversion
DISS = KOFF * A(4)
SINK = KERL * A(4)

DADT(1) = INPUT - CL*CLIG - Q*(CLIG-CTIS) - BIND + DISS
DADT(2) =  Q*(CLIG-CTIS)
DADT(3) =  KIN*VR - KOUT*A(3) - BIND + DISS    ; KIN as conc/time → multiply by VR
DADT(4) =  BIND - DISS - SINK
```

> ⚠️ **두 표기를 절대 섞지 마세요.** 원래 본 자료 초안에는 `BIND = KON * CLIG * R * VC`라는 줄이 있었는데, 이 식은 **R이 농도일 때만** 옳고, R이 amount이면 추가 volume 변환이 필요해서 mass balance가 조용히 깨집니다. PK27 원전(G&W Eq.27:1~27:3)의 mass-balance는 둘 중 하나로 **일관되게** 잡혀야 해요 — concentration-based(DCDT)이거나 amount-based(DADT, 모든 binding 항에 명시적 volume 변환)이거나. R&T Eq.21-1~21-4도 농도 기반 표기를 일관되게 사용합니다 [G&W pp.606–607; R&T p.711].

**실무 팁**: 두 표기를 혼용하면 정상상태에서 $R_0 = k_{in}/k_{out}$ 관계가 미묘하게 어긋나서, 모델은 적합되지만 baseline drift가 **자료가 아닌 표기 오류 때문에** 만들어집니다. 가장 안전한 디버깅은 dose=0 simulation에서 $R$이 정확히 $R_0$로 수렴하는지를 먼저 확인하는 거예요.

### F. 가정과 경계조건

$V_c=0.05\ \mathrm{L\cdot kg^{-1}}$ 고정은 PK27의 고해상도 rapid-IV 데이터에서 고분자량 단백질에 적용한 근사값이에요. 임상 보편 상수가 아닙니다 [G&W p.608].

free target, total target, complex assay는 모델 상태변수와 정렬돼야 해요. assay가 partial total target을 보고하는데 모델이 free $R$을 가정하면, $R_0$와 $k_{out}$의 해석이 달라져요.

Full TMDD는 ligand 데이터만 희박하게 있으면 과모수화(over-parameterization)됩니다. **Efalizumab**(anti-CD11a IgG1 mAb, 건선 치료제) 사례인 **PK26**에서는 target과 complex 데이터, 그리고 $k_{on}/k_{off}/K_d$ 정보가 없어서 full TMDD 적합에 실패했어요. → 그래서 **자료 풍부도가 충분하지 않으면 Full TMDD는 추정 가능한 모델이 아니다**라는 사실의 임상 사례입니다 [G&W p.601].

#### Soluble target vs Membrane-bound target — 임상 mAb 분석의 분기점

PK27이 다루는 데이터는 G&W가 명시한 대로 **soluble target**입니다 [G&W p.602, "soluble target"]. 그런데 임상 mAb 분석에서는 target이 soluble이냐 membrane-bound이냐가 **TMDD signature의 phase 구조 자체를 바꾸는 분기점**이에요. G&W는 PK27 본문에서 "membrane bound targets could have very different impact on the ligand disposition"이라고 명시적으로 경고합니다 [G&W p.605]. R&T도 같은 맥락에서 "shed antigens(= soluble form of membrane-bound target)"의 dynamic interplay를 trastuzumab 예시로 다루고요 [R&T pp.750–751, Fig.22-20].

두 target 유형의 임상 의미를 분리해 두면 다음과 같아요.

| 비교 기준 | Soluble target (예: VEGF, TNF-α, IgE) | Membrane-bound target (예: HER2, CD20, CD11a) |
|---|---|---|
| Complex의 운명 | drug-target complex가 **혈장을 같이 순환** | complex가 세포 안으로 **internalize되어 곧장 sink** |
| Target turnover | 혈장에서 $k_{in}/k_{out}$ 측정 가능, baseline 비교적 안정 | 세포 표면 발현·shedding·internalization이 얽혀서 복잡 |
| Phase A 신호 | rapid binding이 혈장 곡선에 비교적 잘 보임 | internalize가 빠르면 Phase A가 흡수돼서 안 보일 수 있음 |
| Total assay 해석 | total = free + complex (둘 다 혈장에 있음) | total이 shed antigen만 잡고 막결합 target은 못 잡을 수 있음 |
| Phase B 청소율 | nonspecific clearance 지배 | internalization 자체가 빠르면 Phase B의 "linear"가 흐려짐 |
| 대표 mAb 예시 | bevacizumab(anti-VEGF), adalimumab(anti-TNFα), omalizumab(anti-IgE) | trastuzumab(anti-HER2), rituximab(anti-CD20), efalizumab(anti-CD11a) |

수식으로 보면 두 시나리오의 차이는 complex의 운명에 직접 들어갑니다.

$$
\overbrace{\frac{dRL}{dt}}^{\text{complex 변화}}
=
\underbrace{k_{on}LR}_{\text{형성}}
-\underbrace{k_{off}RL}_{\text{해리}}
-\overbrace{\underbrace{k_{e(RL)}RL}_{\text{soluble: 혈장 청소}}\ \text{vs}\ \underbrace{k_{int}\cdot RL}_{\text{membrane: internalize 직행 sink}}}^{\text{이 항의 의미가 갈리는 지점}}
$$

수학적 형태는 같은 1차 소실 항인데, **물리적 해석이 다릅니다** — soluble에서는 $k_{e(RL)}$이 ligand의 nonspecific clearance와 같은 capillary/RES 경로일 가능성이 높고, membrane-bound에서는 $k_{int}$가 receptor internalization·lysosomal degradation의 결합 속도예요. 이 해석 차이가 **(i) assay 설계**(soluble은 plasma free·total·complex 모두 sampling 가능, membrane은 free ligand가 주 측정 대상이고 target은 biopsy·flow cytometry 필요), **(ii) Phase A 검출 가능성**(internalize가 빠르면 Phase A가 dosing 직후 분 단위에 사라짐), **(iii) anti-drug antibody 형성 위험**(complex의 운명이 다르면 면역 노출이 달라짐)을 갈라요.

**실무 한 줄**: 새 mAb 후보의 TMDD 모델링을 시작할 때 가장 먼저 적어야 하는 한 줄은 "이 target은 soluble인가, membrane-bound인가, 아니면 shed antigen이 둘 다 만들어지는가?" 입니다. PK27의 4-state Full TMDD 골격은 soluble target에 가장 직접 적용되고, membrane-bound나 shed-antigen 시나리오에서는 추가 state(membrane R, shed R, 두 종류의 complex)가 필요해질 수 있어요 [R&T p.751, Fig.22-20].

> 📖 **R&T p.711, Fig.21-8 (+ G&W p.604, Fig.27.2)**: Full TMDD는 파라미터 개수 문제이기 전에 **topology 문제**예요. 이 그림은 ligand·target·complex가 binding, dissociation, sink 경로로 어떻게 연결되는지를 보여줍니다.

$$
\underbrace{k_{in}}_{\text{target 입력}}
\perp
\underbrace{k_{on}}_{\text{kon}},
\qquad
\underbrace{k_{off}}_{\text{koff}}
\perp
\underbrace{k_{e(RL)}}_{\text{complex 제거}}
$$

**이번 카드 핵심내용**: Full TMDD의 핵심은 "파라미터가 많다"가 아닙니다. **ligand 곡선 안에 숨어 있는 target turnover, binding, complex sink를 따로따로 분리하는 것**이에요. target과 complex 데이터가 같이 있으면 $k_{on}$, $k_{off}$, $k_{e(RL)}$의 식별성이 개선되고, ligand-only 적합이 좋아 보일 때는 target turnover와 complex sink가 "biologically learned"가 아닐 수 있다는 걸 기억해야 해요. 적합 품질을 그대로 기전 타당성으로 받으면 저용량 외삽·occupancy·subgroup 예측에서 구조적으로 실패합니다. 다음 카드(M4½)에서는 Full TMDD와 MM 사이에 놓이는 **준정상상태(QSS) 근사**를 보고, 그 다음 M5에서 가장 압축된 MM 형태로 넘어갑니다.

---

<!-- SLIDE_START: M4½ | title: Approximation Hierarchy and QSS -->
<!-- SECTION_CORE: SC-06b -->
## ▌ Card M4½ — Full TMDD ↔ MM 사이의 근사 위계와 QSS 근사 (bridge)

M4의 Full TMDD와 M5의 MM 사이에는 **중간 근사 단계가 사슬처럼 있어요**. 임상 mAb 분석에서 실제로 가장 많이 쓰이는 건 Full도 MM도 아니라 그 사이의 **준정상상태(quasi-steady-state, QSS) 근사**입니다. R&T 본문이 PK27 4-phase 그림 바로 다음 문단에서 명시하는 부분이에요 — *"Alternatively, quasi-steady state or quasi-equilibrium approximations can be used."* [R&T p.712]. 본 자료의 원래 흐름이 Full ↔ MM 두 극단만 비교했으니, 그 사이 다리를 한 카드로 깔아둡니다.

> **거장의 시각**  
> QSS를 "MM의 별명"으로 외우면 핵심을 놓쳐요. QSS는 **complex의 동역학에 대한 명시적 가정**을 두고 ligand·target 수준에서 식별성을 회복시키는 단계입니다. MM은 그 위에 "drug $\gg$ target"이라는 한 가지 가정을 더 얹어서 한 항으로 접은 형태고요. 그래서 QSS는 보통 MM보다 더 넓은 농도 영역에서 방어 가능하고, biologics PopPK 실무의 출발점이 됩니다.

### A. 근사 위계 (approximation hierarchy)

| 근사 단계 | 핵심 가정 | 식별 가능한 양 | 주된 사용처 |
|---|---|---|---|
| **Full TMDD** | 가정 없음 (M4의 4-state ODE) | $R_0,\ k_{out},\ k_{on},\ k_{off},\ k_{e(RL)}$ | target·complex 자료가 풍부할 때 |
| **Rapid Binding (RB) / Quasi-Equilibrium (QE)** | $k_{on},\ k_{off} \gg k_{e(RL)}$ → binding이 빠르게 평형 | $K_d = k_{off}/k_{on}$ 중심, $k_{e(RL)}$ 별도 추정 | 매우 강한 결합, 해리가 internalization보다 빠를 때 [R&T p.712] |
| **Quasi-Steady-State (QSS)** ▶ 실무 표준 | $\dfrac{d[RL]}{dt}\approx 0$ → complex가 빠르게 준정상상태 | $K_{ss} = (k_{off}+k_{e(RL)})/k_{on}$, $R_0$, $k_{out}$ | 대부분의 biologics PopPK 분석의 출발점 |
| **Michaelis-Menten (MM)** | $L \gg R$ 또는 target occupancy ≈ 100% | $V_{max},\ K_m$ (target/complex 식별 불가) | 자료 한정, 고용량 내삽 위주 [G&W p.609] |

### B. QSS의 형식적 도출

Full TMDD의 complex 식 (R&T Eq.21-4 / G&W Eq.27:3)에서 출발합니다 [R&T p.711].

$$
\overbrace{\frac{d[RL]}{dt}}^{\text{complex 변화율}}
=
\underbrace{k_{on}\,L\,R}_{\text{형성}}
-\underbrace{(k_{off}+k_{e(RL)})\,RL}_{\text{해리+sink}}
$$

QSS 가정은 이 우변을 ≈ 0으로 둡니다 (complex가 ligand·target보다 훨씬 빠른 time scale로 평형에 도달).

$$
\underbrace{k_{on}\,L\,R}_{\text{형성}}
\approx
\underbrace{(k_{off}+k_{e(RL)})\,RL}_{\text{해리+sink}}
\quad\Longrightarrow\quad
\overbrace{\underbrace{K_{ss}}_{\text{QSS 상수}}
=
\frac{\underbrace{k_{off}+k_{e(RL)}}_{\text{소실 합}}}{\underbrace{k_{on}}_{\text{결합}}}}^{\text{Mager-Krzyzanski식 정의}}
$$

여기서 보면 $K_{ss}$는 **수식적으로 $K_m$과 동일한 형태**예요. 그런데 의미가 달라요 — $K_m$은 "겉보기 saturation 경계"이고, $K_{ss}$는 **complex의 quasi-steady-state로부터 명시적으로 유도된 ligand·target 평형 상수**입니다. 같은 분수식이지만 가정이 다르면 해석이 다른 거예요.

QSS 가정 아래에서 total target $R_{tot} = R + RL$의 관계와 free target $R$의 표현이 다음과 같이 풀립니다.

$$
\underbrace{R}_{\text{free target}}
=
\frac{\overbrace{R_{tot}\cdot K_{ss}}^{\text{총 target × QSS 상수}}}{\underbrace{K_{ss}+L}_{\text{ligand 농도 의존}}}
,\qquad
\underbrace{RL}_{\text{complex}}
=
\frac{\overbrace{R_{tot}\cdot L}^{\text{총 target × ligand}}}{\underbrace{K_{ss}+L}_{\text{포화 분모}}}
$$

이 두 식이 가르치는 게 뭐냐 — **complex 데이터를 명시적으로 추적하지 않아도, ligand와 total target만으로 $K_{ss}$를 식별할 수 있습니다.** Full TMDD가 요구하던 "complex assay 풍부도"를 우회하는 거예요. 이게 biologics PopPK 실무에서 QSS가 거의 표준이 된 이유입니다.

### C. MM과의 관계 — "한 가정 더 얹으면 MM"

QSS에 추가로 **$L \gg R$** (즉 target occupancy가 거의 100%) 가정을 얹으면 MM이 나옵니다.

$$
\underbrace{K_{ss}}_{\text{QSS}} \xrightarrow{\,L\gg R\text{ 가정 추가}\,} \underbrace{K_{m}}_{\text{MM}}
,\qquad
\underbrace{V_{max}}_{\text{MM}} \approx \underbrace{k_{e(RL)}\cdot R_{tot}}_{\text{포화 시 sink 처리능}}
$$

수식의 분수 형태는 같은데, **MM은 $R_{tot}$ 자체가 보이지 않게 잠긴 형태**예요. 그래서 MM에서는 target turnover ($k_{in}, k_{out}$)와 complex sink ($k_{e(RL)}$)를 분리해서 추정할 수 없고, $V_{max}/K_m$이라는 두 macro-parameter만 남습니다. PK27에서 $K_m$이 0.03 → 3.7로 123배 부풀려졌던 이유 중 하나가 이거예요 — MM은 $R_{tot}$의 변동을 추적할 도구를 잃기 때문에, 저용량(target이 포화되지 않은 영역)에서 구조 편향이 누적됩니다 [G&W p.609].

### D. 임상 mAb에서 QSS가 표준이 되는 이유

R&T가 이 자리에서 강조하는 한 줄은 — **"discrimination between $k_{on}$ and $k_{e(RL)}$ is often challenging if not impossible based on clinical data because it requires measurement of $R$ and/or $RL$"** [R&T p.712, paraphrased to under 15 words: 임상 자료만으로 $k_{on}$과 $k_{e(RL)}$를 분리하는 건 free target 또는 complex 측정 없이는 거의 불가능합니다]. QSS는 이 식별성 한계를 정면으로 다루는 도구예요. 두 micro-parameter를 분리하는 대신, **두 값의 합으로 정의되는 macro-parameter $K_{ss}$**를 식별합니다.

| 시나리오 | 권고 모델 | 이유 |
|---|---|---|
| Preclinical, target·complex 풍부 | Full TMDD | 모든 micro-parameter 식별 가능 |
| Clinical Phase 1, ligand·total target 측정 | **QSS** | $K_{ss}$, $R_0$, $k_{out}$ 식별; complex 측정 불필요 |
| Clinical PopPK, ligand만 측정 | Parallel linear + MM 또는 **QSS with informative prior** | 자료 한정, QSS는 prior로 보강 가능 |
| Phase 1 SAD에서 occupancy ≥ 95% 유지 | MM (제한적) | 좁은 농도 범위 내삽만 |

### E. 한계와 경계조건

QSS는 만능이 아닙니다. **complex의 dynamics가 ligand·target의 dynamics와 같은 time scale**일 때 — 예를 들어 internalize가 매우 느린 (membrane-bound이지만 endocytosis가 느린) target — QSS 가정이 깨집니다. 그리고 QSS는 $k_{on}$과 $k_{e(RL)}$를 **개별적으로 식별하지 못해요**. 두 값의 합비 $K_{ss}$만 식별합니다. 그래서 "target receptor occupancy를 micro-parameter 수준에서 mechanistic하게 시뮬레이션해야 한다"는 요구가 있으면 QSS만으로는 부족하고 Full TMDD가 필요해요.

또 하나 — QSS는 **soluble target에서 가장 깔끔하게 작동**합니다. M4.F에서 다룬 membrane-bound target이나 shed antigen 시나리오에서는 추가 state(membrane R + soluble shed R, 두 종류의 complex)가 들어오기 때문에, "단일 $K_{ss}$" 가정으로는 부족할 수 있어요 [R&T p.751, Fig.22-20].

> 💡 **세 가지 K 상수를 한 자리에 모아두면 헷갈리지 않아요.**
>
> $$
> \overbrace{K_d}^{\text{thermodynamic}} = \frac{k_{off}}{k_{on}}
> \quad<\quad
> \overbrace{K_{ss}}^{\text{QSS 가정 하}} = \frac{k_{off}+k_{e(RL)}}{k_{on}}
> \quad=\quad
> \overbrace{K_{m}}^{\text{MM 가정 하}} = \frac{k_{off}+k_{e(RL)}}{k_{on}}
> $$
>
> $K_{ss}$와 $K_m$은 **분수식이 같지만 도출 가정이 다릅니다.** $K_{ss}$는 "complex의 quasi-steady-state"라는 한 가지 가정만 두고 ligand·total target 수준에서 식별되는 반면, $K_m$은 추가로 "$L \gg R$"를 가정해서 $R_{tot}$가 사라진 형태예요. $K_d$는 $k_{e(RL)}$이 포함되지 않는다는 점에서 두 동역학 상수와 본질적으로 달라요. 리포트에서 셋을 같은 단어로 부르면 reviewer가 반드시 reconciliation을 요구합니다.

**이번 카드 핵심내용**: Full TMDD와 MM은 같은 사슬의 양 끝이고, 그 사이에 **QSS와 QE라는 명시적 가정 단계**가 있습니다. 임상 mAb 분석의 실무 표준은 보통 QSS이고, MM은 그 위에 "$L \gg R$" 가정을 더 얹은 더 좁은 도구예요. $K_{ss}$와 $K_m$이 같은 분수식을 갖는 이유는 우연이 아니라 **MM이 QSS의 한 가지 추가 가정 하 특수 경우**이기 때문입니다. 다음 M5에서는 그 가장 압축된 MM 형태의 적용 경계를 봅니다.

---

<!-- SLIDE_START: M5 | title: Michaelis-Menten Approximation Boundary -->
<!-- SECTION_CORE: SC-07 -->
## ▌ Card M5 — Michaelis-Menten 근사의 경계

M4½에서 QSS가 Full TMDD와 MM 사이의 다리라는 걸 잡았어요. 이제 결정해야 합니다 — **어떤 조건에서 이 사슬의 끝(MM) 한 줄로 접어도 되는가?**

> **거장의 시각**  
> MM을 "단순하고 안전한 대체 모델"로만 보면 reduced model이 허용되는 농도·occupancy 경계를 놓쳐요. MM을 **Full TMDD의 접힌 형태**로 보면 위치가 분명해집니다 — 관찰된 포화 영역 안에서만 방어 가능한 내삽 도구예요.

Michaelis-Menten 근사는 Full TMDD의 target과 complex 하부 시스템을 $V_{max}$와 $K_m$로 줄이는 거예요. $R$과 $RL$을 직접 추적하지 않고 target-mediated 경로를 하나의 saturable clearance 항으로 접습니다. 진짜 문제는 적합이 아니라 — **어느 농도·occupancy 영역에서 이 접기가 구조적으로 허용되는가**예요 [G&W p.609; R&T p.712].

### A. 형식적 정의

| 파라미터 | 단위 | 의미 | 변화 원인 |
|---|---|---|---|
| $Cl_{MM}$ | clearance | saturable target-mediated CL | $C$, $V_{max}$, $K_m$ |
| $V_{max}$ | amount/time | 최대 target-mediated 처리능 | target capacity, internalization capacity |
| $K_m$ | concentration | 겉보기 half-saturation 경계 | $k_{off}$, $k_{e(RL)}$, $k_{on}$ |
| $K_d$ | concentration | binding 해리상수 | $k_{off}/k_{on}$ |
| Occupancy | % | target 결합 비율 | concentration vs binding/saturation 경계 |

Reduced model은 target-mediated 경로를 다음과 같이 압축합니다. **압축이지 biology가 사라진 게 아닙니다.**

$$
\overbrace{Cl_{MM}}^{\text{포화 TMDD CL}}
=
\frac{\underbrace{V_{max}}_{\text{최대 처리능}}}{\underbrace{K_m}_{\text{반포화 경계}}+\underbrace{C}_{\text{ligand 농도}}}
$$

Full TMDD 안에서 두 상수의 정의를 같이 보면 차이가 명확해요.

$$
\overbrace{K_d}^{\text{결합 해리상수}}
=
\frac{\underbrace{k_{off}}_{\text{해리 속도}}}{\underbrace{k_{on}}_{\text{결합 속도}}},
\qquad
\overbrace{K_m}^{\text{겉보기 동역학상수}}
=
\frac{\overbrace{k_{off}+k_{e(RL)}}^{\text{해리+sink}}}{\underbrace{k_{on}}_{\text{결합 속도}}}
$$

$K_d$는 binding affinity에 가까운 **thermodynamic 해리상수**이고, $K_m$은 complex loss($k_{e(RL)}$)까지 포함한 **apparent kinetic 상수**예요 [G&W pp.603–609; R&T pp.711–712].

> 💡 **MM은 접힌 모델입니다.** $V_{max}/K_m$은 target biology를 제거한 게 아니라 관찰 가능한 saturable 항으로 압축한 거예요. 그래서 $K_m$은 $K_d$가 아니에요 — $K_m$에는 complex sink $k_{e(RL)}$가 들어가요. 관찰된 saturation·occupancy 영역 밖에서는 고용량 적합이 아무리 좋아도 MM 외삽을 정당화할 수 없습니다.

### B. MM이 통할 수 있는 조건

MM이 적절할 수 있는 상황은 네 가지예요 [G&W p.609; R&T p.712].

- ligand 농도가 target 농도를 크게 초과할 때
- target occupancy가 거의 완전 포화일 때
- 관찰된 용량 범위가 제한적일 때
- 목적이 저농도 외삽이 아니라 **관찰 프로파일 내 내삽**일 때

**Efalizumab**(anti-CD11a IgG1 mAb, 건선 치료제) 사례인 **PK26**이 좋은 reduced-model 앵커입니다. 2구획 모델에 parallel linear/MM 제거가 사용됐는데, target/complex 데이터와 $k_{on}/k_{off}/K_d$ 정보가 없어서 full TMDD 적합 자체가 안 됐기 때문이에요. 보고된 추정값은 $V_t=0.061$, $V_{max}=0.039$, $K_m=0.161$, $CL_d=0.031$, $CL_L=0.007$입니다. 이 reduced model은 single-dose iv bolus 데이터의 5개 정맥주사 시간경과에 적합됐어요. → 그래서 **이 사례는 "제한된 데이터에서 reduced model이 정당화된 앵커"로 읽어야지, "MM이 보편적으로 mechanistic이다"라는 증거로 읽으면 안 됩니다** [G&W pp.599–601].

$$
\overbrace{\{V_t,V_{max},K_m,CL_d,CL_L\}}^{\text{PK26 reduced set}}
=
\underbrace{\{0.061,0.039,0.161,0.031,0.007\}}_{\text{보고 추정값}}
$$

### C. MM이 무너지는 지점

PK27에서 MM은 가장 높은 세 농도 곡선은 비교적 잘 맞췄어요. 그런데 **가장 낮은 농도 곡선에서는 곡선이 따로 놀았고, 추정된 $K_m$이 3.7로 잡혀서 Full TMDD의 0.03보다 약 123배 부풀려졌습니다** [G&W p.609].

임상 교훈은 "MM을 쓰지 마라"가 아니에요. 더 좁고 실용적입니다 — **target saturation이 실증된 농도·occupancy 영역 밖에서는 MM을 쓰지 마세요.**

### D. Occupancy 검증

대략 **90–95% 이상의 occupancy**가 유지되는 영역에서는 단순화가 허용될 수 있어요. occupancy가 $K_d$ 또는 biomarker 역가 이하로 떨어지면 MM이 충분하지 않습니다 [G&W p.609].

$$
\underbrace{\mathrm{Occupancy}}_{\text{target 결합비율}}
\gtrsim
\underbrace{90\text{--}95\%}_{\text{고포화 영역}}
$$

**실무 준칙**: TMDD 가능성이 있는 mAb에 MM을 쓰는 리포트라면, 관찰된 농도 범위, target 농도 범위, 투여 간격 동안의 **최소 예측 target occupancy**를 명시해야 합니다. 이건 소스 경계의 구현 해석이지 규제기관이 직접 인용한 요건은 아니에요.

### E. 한계

MM은 $R_0$, $k_{out}$, $k_{on}$, $k_{off}$, $k_{e(RL)}$의 명시적 해석을 잃어요. 고용량이나 중심 곡선에 가중치가 쏠리면 저농도 편향이 가려지고, 추가 가정 없이는 target recovery나 complex sink 질문에 답할 수 없습니다. **이때 한 단계 덜 압축된 도구가 M4½에서 다룬 QSS 근사**예요 — complex만 quasi-steady-state로 두고 $R_0$, $k_{out}$, $K_{ss}$를 그대로 식별할 수 있어서 임상 mAb PopPK 실무의 출발점이 됩니다 [R&T p.712].

> 📖 **G&W p.609, Fig.27.6**: 이 그림은 무조건적 MM 외삽에 대한 **결정타**예요. 고용량 적합은 괜찮아 보여도, 가장 낮은 농도 곡선에서는 곡선이 따로 놀고 $K_m$이 과대예측됩니다. 이 그림을 직접 보지 않으면 학습자가 "적합 품질 = 기전 타당성"이라고 그냥 결론지어버리기 쉬워요.

**이번 카드 핵심내용**: MM은 빠르고 편한 실무 도구일 수 있는데, **"적합이 잘 됨"과 "target biology를 올바르게 외삽함"은 같은 말이 아닙니다.** 관찰된 포화 영역 안에서 내삽할 때는 MM 근사가 실무적으로 방어 가능한데, 저농도 trough·recovery·occupancy 외삽에서는 Full TMDD나 추가 데이터가 지배해야 해요. 고용량 적합이 좋다고 MM이면 충분하다고 결론지으면 PK27처럼 $K_m$ 과대예측과 저용량 구조 편향이 그대로 임상 결정에 들어갑니다.

---

<!-- SLIDE_START: §5 | title: Confusion Pair Dissection -->
<!-- SECTION_CORE: SC-08 -->
# §5 자주 혼동되는 개념 쌍

다섯 카드를 다 통과해도 실무에서 흔들리는 단어들이 있어요. `fit`, `affinity`, `linearity`, `half-life` — 친숙해서 안 묻고 넘어가는데, TMDD에서는 전부 **조건부 의미**를 갖습니다. 이 네 쌍을 분리해 두면 리포트 한 문장이 가지는 무게가 달라져요.

## ▌ Pair 1 — $k_{in}$ vs $k_{out}$

| 비교 기준 | $k_{in}$ | $k_{out}$ |
|---|---|---|
| 단위 | mass/time | time⁻¹ |
| 수식 내 위치 | $A_0=k_{in}/k_{out}$의 분자 | $A_0=k_{in}/k_{out}$의 분모, $t_t=1/k_{out}$의 분모 |
| 변화 원인 | 합성·입력 증가/감소 | catabolism·degradation 속도 변화 |
| 혼동 시 임상 결과 | level만 보고 시간 척도 변화로 오해 | level과 회복 시간 변화 모두 놓침 |

| 흔한 혼동 | 교정 |
|---|---|
| $k_{in}$과 $k_{out}$을 둘 다 그냥 "rate"로 기억합니다. | $k_{in}$은 mass/time인 input이고, $k_{out}$은 time⁻¹인 분획 소실이에요. |
| $k_{in}$ 증가와 $k_{out}$ 감소가 둘 다 농도를 높이니 같다고 생각합니다. | $k_{in}$ 변화는 level만, $k_{out}$ 변화는 **level과 time scale을 함께** 바꿉니다 [G&W p.97]. |

$$
\underbrace{k_{in}}_{\text{mass/time 입력}}
\quad\ne\quad
\underbrace{k_{out}}_{\text{시간}^{-1}\text{분획 소실}},
\qquad
\underbrace{A_0}_{\text{level}}
=
\frac{\underbrace{k_{in}}_{\text{level 상승}}}{\underbrace{k_{out}}_{\text{level↓/시간↓}}}
$$

한 줄로 박아두면: $k_{in}$은 수도꼭지, $k_{out}$은 배수구입니다. **수위만 보지 말고 새 수위에 도달하는 시간까지 같이 보세요.**

---

## ▌ Pair 2 — Full TMDD vs MM 근사 ▶ Critical Blow

| 비교 기준 | Full TMDD | MM 근사 |
|---|---|---|
| 차원 | ligand·target·complex state를 가진 ODE system | 하나의 saturable clearance 항 |
| 수식 내 위치 | $k_{on}LR$, $k_{off}RL$, $k_{e(RL)}RL$, $k_{in}/k_{out}$로 분리 | $Cl_{MM}=V_{max}/(K_m+C)$로 압축 |
| 변화 원인 | binding, target turnover, complex sink, nonspecific CL | 관찰 포화 범위와 apparent $V_{max}/K_m$ |
| 혼동 시 임상 결과 | data-rich mechanism을 식별 가능 | 저용량 trough·occupancy·subgroup 외삽에서 구조 편향 |

| 흔한 혼동 | 교정 |
|---|---|
| Full TMDD는 복잡하고 MM은 단순한 대체 모델이다. | MM은 Full TMDD의 target/complex 하부 시스템을 reduction한 거예요. |
| 고용량 적합이 좋으면 MM이 충분하다. | PK27에서 고용량 곡선 적합이 좋아도 저용량 곡선이 따로 놀았고 $K_m$이 123배 부풀려졌어요 [G&W p.609]. |
| target/complex assay는 있으면 좋은 부가자료다. | target/complex 데이터는 $k_{on}$, $k_{off}$, $k_{e(RL)}$의 정밀도를 결정하는 **식별 자료**예요 [G&W p.609]. |

한 줄로 박아두면: MM은 "작은 TMDD"가 아니라 **"target biology를 $V_{max}/K_m$으로 접은 모델"**이에요. **접어도 되는지는 occupancy 영역이 결정합니다.**

기억 고리 — 완전 지도 vs 단순화 지도. Full TMDD는 binding on/off, complex internalization, target 생성·분해를 다 명시한 **완전 지도**입니다. MM 근사는 특정 농도 영역($L \gg R$ 또는 $L \gg K_d$의 quasi-equilibrium)에서 이 복잡성을 **하나의 포화곡선으로 압축한 단순화 지도**예요. 단순화 지도는 그려진 스케일을 벗어나면 틀린 경로를 알려줍니다 — drug 농도가 $K_d$ 또는 $K_m$ 부근으로 떨어지면 MM 모델은 TMDD 거동을 재현 못 해요. PK27의 $K_m$ 0.03 → 3.7 과대예측이 바로 이 "지도 밖 영역"의 정량 흔적입니다.

> **▶ Critical Blow**: 이 혼동을 안고 first-in-human 저용량 외삽이나 sub-population 외삽으로 임상 의사결정을 강행하면 세 경로의 실패가 옵니다 — **(i) 저농도 trough 과대평가로 sub-therapeutic 노출 환자군이 누락되고, (ii) dosing interval 동안 target occupancy가 적합 범위 밖으로 떨어져도 검출 안 되고, (iii) sub-population 외삽이 실증된 saturation 영역 밖에서 이뤄집니다.** PK27의 $K_m$ 0.03 → 3.7이 보여주듯, 정량 영향은 약물·환자 집단별 sensitivity analysis로 평가돼야 합니다 [G&W p.609].

---

## ▌ Pair 3 — TMDD에서 $K_d$ vs $K_m$

| 비교 기준 | $K_d$ | $K_m$ |
|---|---|---|
| 단위 | concentration | concentration |
| 수식 내 위치 | $K_d=k_{off}/k_{on}$ | $K_m=(k_{off}+k_{e(RL)})/k_{on}$ |
| 변화 원인 | binding 친화도, 해리/결합 속도 | binding + complex 손실/internalization |
| 혼동 시 임상 결과 | in vitro 친화도를 in vivo 배치 경계로 오독 | occupancy·saturation 경계와 sink 영향을 오해석 |

| 용어 | 정의 | 의미 |
|---|---|---|
| $K_d$ | $k_{off}/k_{on}$ | ligand-target binding/해리 평형 |
| $K_m$ | $(k_{off}+k_{e(RL)})/k_{on}$ | binding + complex loss/internalization 효과 |

$$
\underbrace{K_d}_{\text{결합 친화도}}
=
\frac{\underbrace{k_{off}}_{\text{해리}}}{\underbrace{k_{on}}_{\text{결합}}},
\qquad
\underbrace{K_m}_{\text{disposition}}
=
\frac{\underbrace{k_{off}}_{\text{해리}}+\underbrace{k_{e(RL)}}_{\text{complex sink}}}{\underbrace{k_{on}}_{\text{결합}}}
$$

$K_d$와 $K_m$이 다른 이유는 단순합니다 — $K_m$에 $k_{e(RL)}$이 들어가기 때문이에요. 리포트 쓸 때 **in vitro thermodynamic $K_d$**와 **in vivo 모델에서 나온 apparent $K_m$**을 반드시 분리하세요. 둘 다 "affinity"라고 부르면 내부에서도 혼동이 생기고, reviewer가 reconciliation을 요구합니다 [G&W pp.603–609; R&T pp.711–712].

한 줄로 박아두면: $K_d$는 **결합의 언어**, $K_m$은 **결합 이후 sink까지 포함한 disposition의 언어**입니다.

기억 고리 — 친화력 vs 처리 속도. $K_d=k_{off}/k_{on}$은 ligand와 target의 **결합 친화력**, 얼마나 단단히 붙는가의 척도예요. $K_m=(k_{off}+k_{e(RL)})/k_{on}$은 결합 친화력에 complex의 **처리 속도(internalization)**까지 더한 apparent kinetic 상수입니다. 그리고 이 둘과 다른 차원에 있는 게 target turnover($k_{in}/k_{out}$) — target 자체가 **얼마나 빨리 새로 만들어지고 분해되는가**라는 시스템 capacity예요. 친화력이 높아도 target이 빠르게 재생성되면 낮은 농도에서도 비선형성이 지속되고, 친화력이 낮아도 turnover가 느리면 포화가 오래 유지됩니다. 세 파라미터($K_d$, $K_m$, target turnover)가 서로 독립이라서 **in vitro $K_d$ 하나만으로 in vivo TMDD의 임상적 중요성을 판단할 수 없어요.**

---

## ▌ Pair 4 — 저농도 Linear PK vs 고농도 Linear PK

| 비교 기준 | 저농도 Linear | 고농도 Linear |
|---|---|---|
| 차원 | low-concentration regime | high-concentration saturated regime |
| 수식 내 위치 | target-specific 경로가 다시 드러나는 영역 | target 경로 포화로 nonspecific linear CL처럼 보이는 영역 |
| 변화 원인 | $C$가 $K_d/K_m$ 부근 또는 그 이하로 감소 | ligand가 target을 크게 초과 |
| 혼동 시 임상 결과 | trough·washout·occupancy 외삽 실패 | 고용량 적합을 전체 농도 범위 타당성으로 과대해석 |

| 농도 영역 | 선형으로 보이는 이유 | 위험 |
|---|---|---|
| Very low ligand | target 경로가 포화되지 않아 비특이적·target-specific 1차 경로가 공존 | assay 민감도가 낮으면 이 구간을 놓침 |
| Very high ligand | target 경로 포화로 비특이적 청소율이 지배 | 고용량 적합만 보고 MM/linear 모델을 과신 |
| Middle range | target saturation이 농도에 따라 변동 | nonlinear clearance가 가장 뚜렷 |

한 줄로 박아두면: TMDD는 "선형 또는 비선형"이 아니에요. **농도에 따라 두 종류의 linearity와 한 구간의 nonlinearity가 이어지는 시스템**입니다 [G&W pp.604–605].

기억 고리 — 고속도로 vs 병목 도로. 고용량에서 mAb PK가 선형으로 보이는 이유는, target이 이미 포화돼서 TMDD 경로가 더 이상 약물을 추가로 빨아들이지 못하고 비특이적 제거 경로(FcRn salvage가 작동하는 IgG-like clearance)가 지배하기 때문이에요 — **고속도로**입니다. 저용량에서 PK가 선형처럼 보이는 이유는 다릅니다. target이 포화되지 않은 상태에서 1차 target-mediated 경로와 nonspecific 경로가 함께 작동하는데, **두 1차 경로의 합이므로 여전히 선형**이에요. 그러나 이 구간의 target 경로는 **병목 도로**여서, 농도가 조금만 변해도 지배 경로가 바뀝니다. 두 linear regime 사이의 nonlinear transition이 임상 용량 범위 안에 걸쳐 있을 때 TMDD 모델링이 필수가 돼요. **고용량 데이터만 보고 "linear PK"라고 결론 내리면 저용량의 병목 도로 거동을 놓칩니다.**

이 네 쌍이 분리되면 §7에서 회상 질문이 와도 단어 하나에 매끄럽게 답할 수 있어요.

---

<!-- SLIDE_START: §7 | title: Self-Test 능동 회상 모듈 -->
<!-- SECTION_CORE: SC-09 -->
# §7 능동 회상 모듈

답을 외우는 것보다 중요한 건 **"이 데이터가 어떤 phase와 어떤 ODE 항을 실제로 가르치는가?"**를 매번 그 자리에서 묻는 습관이에요. 아래 열 문제는 그 습관을 굳히는 용도입니다.

## Q1 (회상) ★

$A_0 = k_{in}/k_{out}$에서 $k_{in}$과 $k_{out}$의 단위는?

**답**: $k_{in}$은 mass/time, $k_{out}$은 time⁻¹입니다. $A_0$는 두 값의 비율로 정의되는 baseline 양이에요 [G&W p.96].

$$
\underbrace{A_0}_{\text{baseline 양}}
=
\frac{\underbrace{k_{in}}_{\text{mass/time}}}{\underbrace{k_{out}}_{\text{시간}^{-1}}}
$$

**다음 깊이 질문**: 그렇다면 turnover time $t_t = 1/k_{out}$은 임상 PK에서 어떤 측정 가능한 양과 같은가? (M1의 Eq.2:243이 단서.)

---

## Q2 (회상) ★★

왜 $k_{out}$ 변화는 정상상태 level과 도달 시간을 동시에 바꾸는가?

**답**: $k_{out}$은 분획 소실률이라서 baseline $A_0=k_{in}/k_{out}$과 time scale $t_t=1/k_{out}$에 **둘 다 동시에** 들어가기 때문이에요 [G&W pp.96–97].

$$
\underbrace{A_0}_{\text{SS level}}
=
\frac{k_{in}}{\underbrace{k_{out}}_{\text{level/시간 동시}}},
\qquad
\underbrace{t_t}_{\text{교체 시간}}
=
\frac{1}{\underbrace{k_{out}}_{\text{분획 소실}}}
$$

**다음 깊이 질문**: 이 비대칭이 linear kinetics 가정에 의존한다면, 높은 농도에서 $k_{out}$이 사실상 saturable이 되는 경우(예: MM 확장) $k_{in}$ 변화와 $k_{out}$ 변화는 어떻게 구별이 어려워지는가?

---

## Q3 (회상) ★★

Full TMDD의 4개 상태변수는?

**답**: ligand central, ligand tissue/peripheral, free target $R$, ligand-target complex $RL$이에요 [G&W pp.604–607].

**다음 깊이 질문**: 이 4개 state 중 임상에서 직접 측정이 가장 어려운 것은? 그 측정 결손이 PK27 Table 27.2의 식별 위계($k_{on}$/$k_{off}$/$k_{e(RL)}$ 정밀도)에 어떤 구조 영향을 주는가?

---

## Q4 (적용) ★★

mAb ligand-only 데이터에서 고용량 곡선은 잘 맞는데 가장 낮은 용량에서 체계적인 under/over-prediction이 보입니다. 무엇을 의심해야 하나요?

**답**: MM 또는 reduced model이 관찰된 고용량 범위에서는 내삽을 잘 하지만, **저농도 TMDD phase를 제대로 설명하지 못할 가능성이 높습니다.** 이 판단은 측정된 용량·농도 범위에 한정되고, 외삽 영역에서는 target occupancy와 sensitivity analysis가 필요해요 [G&W p.609].

**다음 깊이 질문**: 저용량 외삽을 모델 구조 변경 없이 정당화하려면 — 예를 들어 target/complex assay 추가가 즉시 불가능한 상황에서 — 어떤 sensitivity analysis 절차를 어떤 순서로 수행해야 하는가? (M5 §D와 Q10이 단서.)

---

## Q5 (적용) ★★

$K_m$과 $K_d$가 다를 수밖에 없는 기전 이유는?

**답**: $K_d=k_{off}/k_{on}$은 결합/해리 평형이고, $K_m=(k_{off}+k_{e(RL)})/k_{on}$은 complex의 비가역적 소실($k_{e(RL)}$)까지 포함해요. complex sink가 있으면 **$K_m$은 thermodynamic 친화도가 아니라 apparent kinetic 상수**가 됩니다 [G&W p.609; R&T p.712].

$$
\underbrace{K_d}_{\text{결합 평형}}
=
\frac{k_{off}}{k_{on}},
\qquad
\underbrace{K_m}_{\text{결합+소실}}
=
\frac{k_{off}+k_{e(RL)}}{k_{on}}
$$

**다음 깊이 질문**: in vitro SPR/BLI로 측정한 thermodynamic $K_d$와 in vivo PK fitting으로 추출한 apparent $K_m$을 같은 후보 mAb에 대해 internal report나 NDA narrative에서 어떻게 명시적으로 분리해야 reviewer가 reconciliation 요청을 안 하는가?

---

## Q6 (적용) ★

sc mAb의 terminal slope를 곧바로 elimination 반감기로 해석하면 왜 위험한가?

**답**: 큰 단백질은 sc/im 후 림프관 흡수가 느려 **absorption-rate-limited** 프로파일을 보일 수 있어요. somatropin처럼 iv 반감기는 짧아도 sc 프로파일은 길게 지속될 수 있습니다 [R&T pp.718–721].

**다음 깊이 질문**: sc mAb의 terminal phase가 absorption-rate-limited인지 elimination-rate-limited인지 어떻게 구분하는가? 어떤 추가 실험 설계나 데이터 비교가 결정적 신호를 주는가?

---

## Q7 (회상) ★★

PK27에서 $V_c=0.05\ \mathrm{L\cdot kg^{-1}}$는 어떻게 처리됐는가?

**답**: $V_c$는 fixed assumption으로 사용됐고, Table 27.2는 그 외 **8개의 추정·보고 파라미터**를 제시합니다. fixed $V_c$까지 structural quantity로 세면 9개를 언급할 수 있는데, "8 estimated parameters"와는 구분해야 해요 [G&W pp.603, 608–609].

$$
\underbrace{V_c}_{\text{central volume}}
=
\underbrace{0.05\ \mathrm{L\cdot kg^{-1}}}_{\text{fixed}},
\qquad
\overbrace{8}^{\text{추정/보고}}
\ne
\overbrace{9}^{\text{fixed }V_c\text{ 포함}}
$$

**다음 깊이 질문**: PK27의 $V_c=0.05\ \mathrm{L\cdot kg^{-1}}$는 healthy adult 가정에 가까워요. edema, severe burn, ascites, pediatric subgroup처럼 plasma volume이 의미 있게 다른 sub-population에 같은 fixed $V_c$를 적용하면, sensitivity analysis는 어떻게 설계해야 다른 파라미터(특히 $k_{on}$)의 robustness를 검증할 수 있는가? (M4 §F가 출발점.)

---

## Q8 (적용) ★

target과 complex 데이터가 추가되면 왜 $k_{on}$, $k_{off}$, $k_{e(RL)}$의 정밀도가 좋아지나요?

**답**: ligand-only 데이터는 여러 ODE 항의 합성 결과만 보여줘요. target 데이터는 saturation·recovery를, complex 데이터는 sink 거동을 직접 가르치니까 해당 파라미터의 CV%가 개선됩니다. PK27 Table 27.2에서 $k_{on}$은 **17→2→1**, $k_{off}$는 **27→13→3**, $k_{e(RL)}$는 **27→23→2**로 좋아져요 [G&W p.609].

**다음 깊이 질문**: target/complex assay가 임상에서 가용하지 않을 때 — 예를 들어 PK26 Efalizumab처럼 — 동등한 식별성을 확보할 차선 전략이 있는가? 어떤 조건이 충족되면 reduced model이 정당화되는가?

---

## Q9 (회상) ○

R&T Fig.21-16에서 얻을 수 있는 올바른 결론과 얻으면 안 되는 결론은?

**답**: **얻어도 되는 결론**은 분자량이 커질수록 림프 회수율이 증가한다는 **방향성**입니다. **얻으면 안 되는 결론**은 0.246–19 kDa sheep 데이터를 150 kDa mAb에 선형 외삽해서 구체적 회수율 퍼센트를 계산하는 거예요 [R&T p.720].

**다음 깊이 질문**: 150 kDa mAb의 sc 림프 회수율을 정량 예측할 수 없다면, 임상 protocol 설계에서 sc 흡수 프로파일의 불확실성을 어떻게 다루는 것이 안전한가? (M2 §B의 absorption-rate-limited 메시지와 연결.)

---

## Q10 (보스 딜레마) ★★

팀이 "MM 모델로 OFV도 낮고 VPC도 괜찮으니 first-in-human 저용량 외삽에 쓰자"고 주장합니다. 30초 답변은?

**답**: "MM은 관찰된 용량 범위 안에서는 쓸 수 있지만, 저용량 외삽은 **target occupancy가 충분히 높게 유지되는지 확인**해야 합니다. PK27에서는 고용량 적합이 양호해도 가장 낮은 용량 곡선이 따로 놀았고 $K_m$이 0.03에서 3.7로 **123배 부풀려졌어요**. 최소한 dose-stratified 잔차, 예측 occupancy, 저농도 sensitivity analysis를 보고 결정해야 합니다." [G&W p.609]

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

**다음 깊이 질문**: 위 sensitivity analysis 결과 예측 occupancy가 dosing interval의 일부 구간에서 80% 미만으로 떨어지는 sub-group이 발견됐다고 가정해 보세요. 이 sub-group을 위해 reduced MM을 그대로 유지할 건가, Full TMDD로 전환할 건가, 아니면 별도 covariate model로 분리할 건가? 어떤 기준으로 결정하고, 내부 PK report나 NDA narrative에서 그 결정을 어떻게 정당화할 건가? *(이게 §8 Professional Moat의 narrative justification 능력입니다.)*

---

<!-- SLIDE_START: §8 | title: 메타 프레임과 큰 그림 -->
<!-- SECTION_CORE: SC-10 -->
# §8 메타 프레임과 큰 그림

## A. 이 세션이 놓인 위치

이 세션은 **biologics pharmacometrics의 입구**예요. Small molecule PK에서는 청소율과 $V_d$ 중심으로 설명할 수 있었지만, mAb에서는 **target biology, binding kinetics, complex sink, FcRn salvage, lymphatic input**이 함께 PK 곡선의 형태를 만듭니다.

선행 흐름: linear PK → Michaelis-Menten → turnover → TMDD.
후속 흐름: mAb PopPK → target occupancy 시뮬레이션 → QSP/PBPK → biologics 임상약리 narrative.

## B. 한 카드를 건너뛰면 어떤 실패가 오는가

| 건너뛰면 | 구체 실패 |
|---|---|
| Turnover | target baseline을 predose DV로만 처리하고 $R_0/k_{out}$ 해석을 잃습니다. |
| 단백질 ADME | sc mAb terminal slope를 elimination으로 오해해요. |
| 4-Phase TMDD | 고용량 적합만 보고 저용량 외삽 편향을 놓칩니다. |
| Full TMDD | target과 complex 데이터의 가치를 "nice-to-have"로 잘못 판단해요. |
| **QSS 근사 (M4½)** | **임상 mAb PopPK 실무의 출발점을 모르고 Full ↔ MM 두 극단 사이에서 길을 잃어요.** |
| MM 경계 | 관찰 범위 내 내삽을 임상 외삽으로 착각합니다. |

## C. 실무 해석 지점 — Professional Moat

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| target turnover 변화 | $k_{in}$/$k_{out}$ | → | baseline·recovery·occupancy 해석 변화 | baseline scenario와 target 데이터 확인 |
| FcRn/slow input 개입 | $F$, $T_{max}$, apparent $t_{1/2}$ | → | terminal slope 오독 | iv 비교 또는 dose-stratified 프로파일 확인 |
| 저용량 TMDD 경계 진입 | $K_m$, $K_d$, occupancy | → | trough·subgroup 외삽 편향 | sensitivity analysis와 Full TMDD 필요성 검토 |
| complex sink 관찰 부족 | $k_{e(RL)}$ | → | mechanism fitted but not learned | target/complex assay 또는 informative prior 검토 |

이 세션을 체화하면 두 가지 능력이 생겨요. 첫째, **mechanistic 모델 narrative 정당화** — "왜 Full TMDD인가 / 왜 MM이어도 되는가 / 왜 target assay가 필요한가"를 **수식·생리학·관찰된 농도 범위**로 설명할 수 있습니다. 둘째, **진단 GOF 읽기** — 전체 VPC가 아니라 **dose-stratified 잔차, 저용량 프로파일, target/complex coverage**를 먼저 보고 구조 misspecification을 의심할 수 있어요.

실무 한 줄: mAb TMDD 데이터셋을 처음 받으면 전체 적합 plot보다 먼저 **dose-stratified plot**을 만드세요. 고용량은 맞는데 저용량만 체계적으로 틀리면, "variability problem"보다 **"reduced model 경계 문제"**를 먼저 의심해야 합니다.

## D. 최종 통합

| 후속 세션 | 이 세션에서 열리는 개념 | 이 세션 없으면 실패하는 것 |
|---|---|---|
| mAb PopPK | 제한 분포, FcRn, target-mediated clearance, **QSS as 실무 출발점** | terminal slope와 covariate effect 해석 |
| TMDD/QSP | ligand-target-complex ODE topology, **근사 위계 (Full ↔ QSS ↔ MM)** | target biology와 PK coupling 설명 |
| Target occupancy 시뮬레이션 | $K_d$, $K_{ss}$, $K_m$, occupancy 경계 | dosing interval 동안의 pharmacologic coverage 판단 |
| Biologics 임상약리 리포트 | 모델 경계와 외삽 방어, **soluble vs membrane-bound target 분기** | MM/QSS/Full TMDD 선택 근거 방어 |

mAb 비선형 PK의 본질은 "항체가 크다"가 아닙니다. **큰 ligand가 제한된 tissue space와 림프관 입력을 거쳐 endogenous target turnover system에 들어가고, binding/complex/sink가 농도의존적 청소율을 만든다**는 거예요. Full TMDD는 이 과정을 분해하고, MM은 일부 조건에서만 이를 압축합니다. 그래서 모델 선택의 기준은 편의성이 아니라 **데이터셋이 관찰한 phase, 그리고 임상 의사결정이 요구하는 외삽 범위**예요. 세션 첫머리의 PK27 그림 — 고용량 곡선은 잘 맞는데 가장 낮은 용량 곡선만 따로 놀았던 그 그림 — 이 사실 이 결론의 한 컷짜리 요약입니다.

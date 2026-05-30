# 세션 09 — TMDD·항체 PK · 쉬운판

> TMDD(target-mediated drug disposition, 표적 매개 약물 배치 — "약이 자기 표적에 들러붙어서 그 약이 어떻게 사라지는지가 달라지는 현상")와 항체(monoclonal antibody, 단일클론 항체) PK를 **대학 1학년·비전공자도 한 번에 이해하게** 쉬운 음슴체로 다시 쓴 노트임. 어려운 말은 나오는 그 자리에서 바로 풀어줄 거임.

---

## 메타블록 (이 문서가 뭔지 6가지로)

- **출처 약어(첫머리 1회 풀이)**
  - **G&W** = Gabrielsson & Weiner, *Pharmacokinetic and Pharmacodynamic Data Analysis*(약동·약력 데이터 분석) 5판. 표기 `_G_`. (주 출처)
  - **R&T** = Rowland & Tozer, *Clinical Pharmacokinetics and Pharmacodynamics*(임상 약동·약력학) 5판. 표기 `_T_`. (보조 출처)
  - 인용은 **본문 인쇄 쪽(원판 교재 기준)**을 우선 쓰고, 인쇄 쪽이 안 보이면 `[파일명 PDF page N]`으로 적음. **"쪽=원판 교재 기준"**임(우리가 본 추출 txt의 줄 번호가 아님).
- **대상**: 계량약리학(pharmacometrics, 약물 농도와 효과를 수학모델로 다루는 학문)을 처음 보는 사람. **비전공·대학 1학년도 OK.**
- **선행(미리 알면 좋은 것, 몰라도 그 자리에서 보충함)**: 1구획·2구획 선형 PK(약이 몸에서 1차로 빠지는 기본 모델), Michaelis-Menten(효소 포화식, §5에서 풀어줌), ODE(ordinary differential equation, 상미분방정식 — "시간에 따라 양이 어떻게 변하나"를 적은 식). 이전 세션 연결: §05 2구획 모델, §08 비선형 PK 계열.
- **범위**: 단백질 약물 PK, mAb(항체) 배치, FcRn(아래에서 풀이), TMDD, Full TMDD ODE, 근사 사다리(Full→QSS(quasi-steady-state, 준정상상태 근사)→MM), 자료 풍부도(data richness)와 식별성, soluble vs membrane-bound 표적, ADA(항약물항체). **다음 세션 연결: §11 간접반응(욕조)·§13 IIV(개체간 변동).**
- **원천 목록**
  - G&W §2.6 Turnover [G&W pp.94–111]
  - G&W Case Study PK26 Efalizumab [G&W pp.599–601]
  - G&W Case Study PK27 TMDD [G&W pp.602–610] (이 세션의 척추)
  - R&T Ch.21 Protein Drugs [R&T pp.687–730] (보조)
  - (원전) Mager & Jusko 2001 [R&T Fig.21-8 원전]; Peletier & Gabrielsson 2012 [R&T Fig.21-9 원전]
- **쪽 주의**: 위에 적은 쪽수는 전부 **원판 교재 인쇄 쪽**임. R&T(`_T_`)는 09 세션 고유 내용이 아니라 **보조 출처**라서, 인용할 때마다 `[R&T ...]`로 명시함.

---

## 이 문서 한 장 지도 (+ 관통 척추)

이 세션은 항체(약) 하나를 네 가지 용량으로 주사한 데이터에서 시작함. 고용량 곡선 세 개는 모델이 예쁘게 맞춰주는데, **가장 낮은 용량 곡선 하나만 따로 놂.** 그래서 같은 데이터를 두 모델로 돌렸더니, "포화상수"라는 값이 한쪽은 **0.03**, 다른 쪽은 **3.7** — 약 **123배** 차이가 났음 [G&W p.609]. 이 한 컷이 세션 전체를 끌고 감.

> **★ 관통 척추 (도입부 박스 선언 — 모든 섹션에서 최소 1번 다시 부름)**
>
> "이 데이터가 실제로 **어떤 파라미터를 식별 가능하게 하는가** — **곡선이 예쁘게 맞느냐(fit)**보다 **자료 풍부도(data richness: 측정한 농도 영역이 넓고, 표적·복합체까지 같이 쟀나)**가 어떤 파라미터를 정할 수 있는지를 결정함. 그리고 그 모든 비선형의 뿌리는 **표적(target)이 살아있는 욕조(turnover)**라는 것임."

쉽게 말하면 — "측정 안 한 건 모델이 못 지어냄." 리간드(약) 곡선만 있으면 절대 못 정하는 상수가, 표적·복합체 곡선까지 재면 갑자기 정해짐. 이게 척추임.

**섹션 지도(읽는 순서):**

| 섹션 | 한 줄 | 핵심 |
|---|---|---|
| **§1** | 표적은 살아있는 욕조임 | $R_0=k_{syn}/k_{deg}$, baseline은 결과지 입력이 아님 |
| **§2** | mAb는 작은 약처럼 안 빠짐 | 4관문(분포·림프·제거·FcRn)으로 18~24일 버팀 |
| **§3** | TMDD 4 phase는 시간표가 아니라 농도 지도임 | A~D는 농도 영역 |
| **§4** | Full TMDD = 4-state ODE | ligand·target·complex·sink 분리, 자료 풍부도 |
| **§4½** | QSS = Full과 MM 사이 실무 표준 | complex만 준정상상태로 |
| **§5** | MM의 경계 = PK27 123배 사건 | 관찰 범위 밖 외삽 금지 + 혼동쌍 정정 |

이 표 순서대로 가면 막힘 없이 읽힘. 그럼 시작.

---

## §1 — 표적은 "살아있는 욕조"임 (turnover)

> 🎯 **학습목표**: 이 섹션 끝내면 "표적 $R$이 왜 고정값이 아니라 $k_{syn}/k_{deg}$가 만들어내는 **균형의 결과값**인지", 그리고 "합성을 바꿀 때와 분해를 바꿀 때 결과가 어떻게 다른지"를 설명할 수 있게 됨.

**왜 지금 이걸 하냐 (동기)**: PK27의 123배 사건이 터진 첫 번째 이유는 사람들이 **표적(target)을 고정된 벽처럼** 생각하기 때문임. 그런데 표적은 약이 들어오기 전부터 몸 안에서 끊임없이 새로 만들어지고(생성) 끊임없이 부서지는(소실) **살아있는 시스템**임. 이걸 안 박아두면 뒤에 나오는 $R_0$, 회복시간 같은 게 전부 "그냥 잡은 숫자"로 보임. (척추 호출: "모든 비선형의 뿌리는 표적이 살아있는 욕조" — 그 욕조를 지금 본다.)

### 비유 먼저 — 욕조 한 컷

표적을 **욕조에 담긴 물**이라고 보면 됨.

- **수도꼭지** = 표적을 새로 만드는 속도 (생성)
- **배수구** = 표적이 부서져 빠지는 속도 (소실)
- **수위(물 높이)** = 지금 몸 안의 표적 양

수도꼭지에서 들어오는 양과 배수구로 빠지는 양이 똑같아지면 수위가 안 변함 — 이게 **정상상태(steady state, 들어오는 양 = 나가는 양)**, 즉 **baseline(기저 수위)**임. 핵심은 "물이 얼마나 많냐"가 아니라 **"지금 욕조 전체가 얼마나 빨리 새 물로 갈리느냐(turnover, 교체)"**임 [G&W p.96].

숫자 예시로 감 잡기 — 욕조 용량 10 L, 수도꼭지가 분당 1 L면, 10 L를 다 채우는 데 10분 걸림. 이 "10분"이 **turnover time(교체 시간)**임. 사람 몸물 42 L, 하루 섭취 2.5 L를 넣으면 물의 교체 시간은 약 **17일**임 (42÷2.5). 같은 욕조 수학이 표적 수용체에도, 내인성 항체(IgG)에도, 호르몬에도 **글자 그대로 똑같이** 적용됨 [G&W p.96].

### 식 — ①왜 필요→②기호 뜻→③한 줄 결론

**① 왜 필요**: 수위가 어떻게 변하는지 한 줄로 적어야, "지금 약이 이 균형을 흔든다"를 수학으로 말할 수 있음.

$$
\overbrace{\frac{dA}{dt}}^{\text{수위 변화 속도}}
=
\underbrace{k_{syn}}_{\text{수도꼭지(생성, 0차)}}
-
\underbrace{k_{deg}\cdot A}_{\text{배수구(소실, 1차)}}
\qquad \text{[G\&W Eq.2:237]}
$$

**② 기호 뜻**:
- $A$ = 욕조 안 물의 양(표적 양)
- $k_{syn}$ = 생성 속도(synthesis). G&W 본문은 turnover 일반론에서 $k_{in}$이라고도 부름. 단위는 **양/시간**(예: µg/h). "1분에 몇 L 들어오나" 같은 고정된 양.
- $k_{deg}$ = 소실 속도상수(degradation). G&W는 $k_{out}$이라고도 씀. 단위는 **1/시간**(예: h⁻¹). "남은 것의 몇 %가 빠지나" 같은 분획(비율).
- (용어 주의) R&T 본문(Eq.21-3)은 표적을 **$k_{syn}$(생성)·$k_{deg}$(분해)**로 표기하고, G&W의 turnover 장은 **$k_{in}$·$k_{out}$**로 표기함. **이름만 다르고 같은 자리**임. 이 노트는 표적엔 $k_{syn}/k_{deg}$를, 일반 욕조엔 $k_{in}/k_{out}$를 섞어 쓰되, 처음 나올 때 다리를 놓아줌.

**③ 한 줄 결론**: 표적의 기저 수위는 "수도꼭지÷배수구"임.

다리문장 하나 — 위 식에서 수위가 안 변할 때($dA/dt=0$)를 풀면, 줄줄이 관계식이 나옴 [G&W pp.95–96]:

$$
\underbrace{R_0}_{\text{기저 표적량(baseline)}}
=
\frac{\overbrace{k_{syn}}^{\text{생성}}}{\underbrace{k_{deg}}_{\text{소실}}}
,\qquad
\underbrace{t_t}_{\text{교체 시간}}
=
\frac{1}{k_{deg}}
=
\underbrace{MRT}_{\text{평균 체류시간}}
=
\underbrace{\frac{V_{ss}}{Cl}}_{\text{PK 식으로도 같음}}
,\qquad
\underbrace{t_{1/2}}_{\text{반감기}}
=
\frac{\ln 2}{k_{deg}}
$$

(용어) $R_0$ = 약 들어오기 전 표적의 기저량. $MRT$(mean residence time, 평균 체류시간) = 분자 하나가 시스템에 머무는 평균 시간. $V_{ss}$ = 정상상태 분포용적, $Cl$ = 청소율. **이 세 개($t_t$, $MRT$, $V_{ss}/Cl$)가 다 같은 값**이라는 게 욕조 ↔ PK를 잇는 다리임 [G&W Eq.2:243].

### ★혼동쌍 즉시정정 (C7) — $k_{syn}$ 바꿈 vs $k_{deg}$ 바꿈

여기가 임상에서 진짜 중요한 자리라 헷갈리는 그 순간 바로 못박음. **생성($k_{syn}$)만 바꾸는 거랑 분해($k_{deg}$)를 바꾸는 건 결과가 다름** [G&W p.97]:

- **$k_{syn}$만 바꾸면** → **수위(level)만** 바뀜. 새 수위에 도달하는 **시간은 그대로**임. (수도꼭지를 더 틀어도, 배수구가 그대로면 평형 잡히는 속도는 안 변함.)
- **$k_{deg}$를 바꾸면** → **수위와 회복 시간($1/k_{deg}$)이 둘 다** 바뀜. (배수구는 위 식에서 $R_0$의 분모이자 $t_t$의 분모라서 두 군데 동시에 들어감.)

$$
\underbrace{k_{syn}\uparrow}_{\text{생성↑}}
\Rightarrow
\underbrace{R_0\uparrow}_{\text{수위만}}
,\qquad\qquad
\underbrace{k_{deg}\uparrow}_{\text{분해↑}}
\Rightarrow
\underbrace{R_0\downarrow}_{\text{수위↓}}
+
\underbrace{t_t\downarrow}_{\text{시간도 단축}}
$$

> 💡 이건 **§11 간접반응 모델의 $k_{in}/k_{out}$ 함정과 같은 쌍**임 — §11에서도 "수위만 보면 원인을 못 잡는다"가 핵심임. 미리 한 줄로 §11을 불러둠. 어떤 PD 지표 회복이 느려졌을 때, 합성이 줄어든 건지 분해가 느려진 건지에 따라 처치 방향이 완전히 갈림. **수위 하나만 봐선 원인을 못 잡음.**

> 💡 (단위 함정 선제 경고) $k_{syn}$은 **양/시간**, $k_{deg}$는 **1/시간**임. 이거 안 구분하면 곧 **표적 생성 $k_{syn}$과 약-표적 결합 속도 $k_{on}$을 같은 양으로 섞어버림** — §4에서 이 함정이 다시 나옴. 지금 박아두면 안전.

### 숫자 예시 — "같은 식, 다른 맥락" 3개

1. **IgX**(내인성 성장호르몬 유사 펩타이드): 약 주기 전 기저농도 32 µg·L⁻¹, $k_{syn}=0.78$ µg·h⁻¹·kg⁻¹, 교체시간 2.7 h, 반감기 2.5 h, $k_{deg}=0.27$ h⁻¹ ("몸에 있는 양의 약 27%가 시간당 빠짐"). **이미 돌아가는 기저 위에 외부 약이 얹히는** 전형 [G&W pp.100–101].
2. **내인성 IgG**: 반감기 **23일**, 하루에 혈장 풀의 6.7%가 교체, turnover 33 mg·kg⁻¹·day⁻¹ [G&W p.102]. (비교 기준) R&T가 말하는 "치료용 mAb 반감기 ≈ 21일"과 **비슷한 영역**인데, **두 문장을 하나로 합치면 안 됨** — 내인성 IgG는 단일 분자종이고 치료용 mAb는 후보마다 FcRn 친화도가 다 다름. 숫자가 비슷하다고 같은 사실이 아님 [R&T p.708].
3. **Estradiol(에스트라디올)** (폐경 후 여성): $k_{syn}=19$ µg·24h⁻¹, $Cl=1.6$ L·min⁻¹, $V_{ss}=50$ L, 반감기 26 min. **임상 포인트** — 폐경 후 낮은 에스트라디올은 "청소율이 늘어서"가 아니라 **생성 $k_{syn}$이 줄어서** 만들어짐 [G&W pp.102–104]. 수위 하나로는 합성 쪽인지 분해 쪽인지 모름(위 혼동쌍 그대로).

### 흔한 실수 (D2)

표적의 약 주기 전 값을 그냥 `R0 = THETA`(추정 파라미터)로만 넣으면, $R_0$의 사람마다 다른 변동이 잔차(residual error)로 흡수돼서 사라짐. 약 주기 전 측정값(baseline DV record)을 모델에 직접 넣어줘야 함. (이건 교과서 본문이 아니라 NONMEM 구현 해석임 — NONMEM은 §4에서 정의함.)

**§1 한 줄 결론**: 표적을 고정값으로 보면 TMDD는 출발부터 망함. $R$은 $k_{syn}/k_{deg}$가 만드는 **균형의 결과값**이고, 외부 약(ligand)은 이 균형을 흔드는 침입자임. 이게 척추가 말한 "살아있는 욕조"임.

---

## §2 — mAb는 작은 약처럼 안 빠짐: 4개의 관문

> 🎯 **학습목표**: 이 섹션 끝내면 "왜 항체가 보통 약(몇 시간~며칠)보다 훨씬 길게 18~24일이나 버티는지"를, 반감기 숫자 하나가 아니라 **4개의 관문(분포·림프·제거·FcRn)**으로 분리해서 설명할 수 있게 됨.

**왜 지금 (동기 / 다리)**: §1에서 약이 들어가는 "욕조(표적)"를 봤음. 이제 그 욕조에 들어가는 **약(ligand) 자체**를 봐야 함. 약이 항체(mAb)면 작은 분자약과 전혀 다른 길로 흡수·분포·제거됨. 이걸 "반감기 21일" 한 숫자로 뭉치면, 느린 흡수·FcRn 재활용·표적 제거가 다 terminal slope(말기 기울기)에 섞여서 **어떤 데이터가 어떤 기전을 가르치는지 못 가림** [G&W pp.97–100; R&T pp.701–724]. (척추 호출: "자료 풍부도가 식별성을 정한다" — 여기선 4관문을 분리해 둬야 §3 phase가 뭘 가르치는지 분리해서 읽힘.)

| 관문 | 무슨 일이 일어나나 | 출처 |
|---|---|---|
| **① 분포(Distribution)** | $V_d$가 작음 — 혈장/조직간질 공간에만 갇힘 | [R&T pp.701–702] |
| **② 흡수(림프, lymphatic)** | sc/im 후 큰 단백질은 주로 림프관으로 느리게 들어옴 | [R&T p.718] |
| **③ 제거(Elimination)** | 작은 단백질은 신장이 핵심, 큰 mAb는 단백분해+세포 흡수 | [G&W pp.98–99; R&T pp.704–708] |
| **④ 회수(FcRn salvage)** | 분해 직전 항체를 건져 순환으로 되돌림 | [R&T p.709] |

### 관문 ① — 분포: "혈관 안에 갇힌 큰 덩어리"

(비유) 작은 분자약은 몸 곳곳 물에 잘 퍼지는데, 항체는 너무 커서 혈관/조직간질 공간(혈관 바로 바깥)에만 거의 갇힘. R&T Table 21-6은 단백질 약물의 $V_{ss}$가 대략 **0.04–0.23 L·kg⁻¹**라고 함. (비교 기준) 몸물 전체는 약 0.6 L·kg⁻¹임 — 그보다 훨씬 작은 숫자임 [R&T pp.701–702].

$$
\underbrace{V_{ss}}_{\text{정상상태 분포용적}}
\approx
\underbrace{0.04\text{–}0.23\ \mathrm{L\cdot kg^{-1}}}_{\text{제한 분포(혈장)}}
\quad\ll\quad
\underbrace{0.6\ \mathrm{L\cdot kg^{-1}}}_{\text{몸물 전체(비교)}}
$$

### 관문 ② — 림프 흡수: "혈관 아니라 림프관 타고 들어옴"

(비유) 큰 짐(항체)은 좁은 혈관벽 문을 못 지나서, 옆에 있는 **림프관(lymphatic, 조직 사이 액체를 모아 혈관으로 되돌리는 배수관)**이라는 넓은 뒷문으로 천천히 들어옴. 림프 흐름은 하루 약 2 L로 매우 느림 [G&W p.97]. R&T Table 21-13의 분자량 기준 — **15,000~20,000 g/mol을 넘으면 주로 림프관 경로**임 [R&T p.718]:

$$
\underbrace{MW}_{\text{분자량}}
>
\underbrace{15{,}000\text{–}20{,}000\ \mathrm{g/mol}}_{\text{림프 경로 역치}}
\Rightarrow
\underbrace{\text{림프관 입력}}_{\text{느린 전신 유입}}
$$

(주의 한 줄) R&T Fig.21-16은 양(sheep)의 0.246~19 kDa 데이터로 "분자량 클수록 림프 회수율↑"라는 **방향성**만 보여줌. 이걸 150 kDa mAb에 직선 외삽해서 회수율 %를 계산하면 안 됨 [R&T p.720]. (150 kDa mAb의 정확한 림프 회수율은 `[교과서 외]`로 둠 — txt 범위 밖.)

(숫자 예시) **somatropin**(재조합 성장호르몬, 22 kDa): 정맥주사 반감기는 **2.1시간**인데, 피하주사(sc)로 주면 농도가 훨씬 길게 지속됨 [R&T p.721]. → **말기 곡선이 제거(elimination)가 아니라 느린 흡수(slow input)에 의해 율속될 수 있다**는 사례임. (흡수가 제거보다 느리면, 보이는 말기 기울기는 사실 흡수 속도임.)

### 관문 ③ — 제거: "크기에 따라 갈림"

작은 단백질은 신장(콩팥)이 핵심 제거 경로지만, 큰 항체는 사구체(신장 여과막)를 거의 못 지나서 신장 영향이 작음. 대신 큰 항체는 온몸의 **단백분해효소**와 **세포 흡수(endocytosis)**로 부서짐 [R&T pp.704–706].

(숫자 예시) **anakinra**(재조합 IL-1 수용체 길항제, 17,258 g/mol): 신기능 떨어지면 청소율도 같이 떨어짐 (creatinine clearance와 비례) [R&T pp.723–724]. 반면 full-size mAb는 신질환 영향이 작음. → **"단백질이면 신장이 중요"가 아니라 크기에 따라 갈림.**

### 관문 ④ — FcRn salvage: "분해 직전에서 구조됨"

> 🎯 (이 관문이 18~24일 반감기의 핵심)

(비유) **FcRn**(neonatal Fc receptor, 신생아 Fc 수용체 — 원래 엄마 항체를 아기에게 넘겨주는 수용체라 "신생아"란 이름이 붙음)은 **재활용 트럭**임. 세포가 항체를 일단 삼키는데, 그 안 산성 주머니(endosome)에서 FcRn이 항체를 **분해(lysosome, 세포 내 소각장) 직전에 건져서 세포 밖 순환으로 되돌려보냄** [R&T p.709, Fig.21-5]. 그래서 항체가 **약 21일**(보통 작은 분자약은 몇 시간~며칠)이나 버팀.

$$
\underbrace{t_{1/2,\,\mathrm{mAb}}}_{\text{mAb 겉보기 반감기}}
\approx
\underbrace{21\ \text{days}}_{\text{IgG식 prior}}
\quad(\text{분자마다 다르니 prior일 뿐})
$$

(정직 표기) 고정 사양은 "18~24일"이라 했고 R&T 본문은 "약 21일(IgG에 가까움)"이라고 함 [R&T p.708]. 둘은 같은 영역임 — **표 21-3·21-15의 실제 mAb 반감기 범위가 대략 11~30일대**(adalimumab 30일, omalizumab 26일, efalizumab 17일 등 [R&T p.723])라서 "18~24일"은 그 가운데 IgG-like 대표값으로 읽으면 됨. **FcRn 친화도, 표적 매개 제거, 면역원성, 용량에 따라 달라짐**이 핵심이라, 단일 고정값으로 못 박음.

(추가 디테일) FcRn 결합은 치료용 mAb 농도에서 보통 **포화되지 않음(nonsaturable)**, 그리고 **pH 의존적**임 — pH가 낮을수록(산성 endosome) 더 단단히 붙음. 이게 "산성 주머니에서 건져 올린다"의 분자 기전임 [R&T p.708].

(숫자 예시 — FcγR 매개 제거) **adalimumab + 메토트렉세이트(MTX)**: 류마티스 관절염 환자에서 MTX 병용 시 adalimumab 청소율이 **29~44% 감소**할 수 있음(MTX가 FcγR 발현을 낮춤) [R&T p.706]. → **FcγR(Fc 감마 수용체, 항체 Fc 부위에 붙어 식세포 작용을 일으키는 수용체)은 변두리 디테일이 아니라, 특정 질환·병용약 맥락에서 clearance covariate(청소율에 영향 주는 공변량)가 됨.**

### sc mAb 예시 — "Tmax가 며칠 단위"

R&T Table 21-15 [R&T p.723]:

| mAb | $F$(생체이용률) | $T_{max}$(최고농도 도달시간) | $t_{1/2}$ |
|---|---|---|---|
| **adalimumab**(항-TNFα) | 0.64 | 5.5일 | 30일 |
| **omalizumab**(항-IgE) | 0.62 | 7.5일 | 26일 |
| **efalizumab**(항-CD11a) | 0.50 | 17일(반감기) | 17일 |

$T_{max}$가 **며칠 단위**라는 것 자체가 "sc 입력이 느리다"는 신호임. (비교 기준) 작은 분자약은 보통 $T_{max}$가 분~시간 단위임.

> 💡 mAb 곡선의 "느림"은 **단일 원인이 아님** — 4관문이 합쳐진 결과임. 그래서 sc 말기 기울기를 그대로 제거 반감기로 읽으면 위험함. 말기 phase를 해석하기 전에 **4관문 중 어느 게 지배하는지 먼저 적어보는 습관**이 필요함.

(예고) **ADA(anti-drug antibody, 항약물항체)** — 설명 안 되는 청소율 증가가 보이면 표적 생물학뿐 아니라 ADA도 점검해야 함. ADA가 TMDD signature(신호)를 시점에 따라 어떻게 바꾸는지는 §4에서 따로 다룸 [R&T p.725]. (E4: 지금은 예고만 — 자료는 §4에 있음.)

**§2 한 줄 결론**: mAb의 느림은 반감기 숫자가 아니라 **조직 접근(작음) + 림프 통과 + FcRn 재활용 + 표적 sink**가 합쳐진 결과임. 이 4관문을 분리해 두면, 다음 §3에서 phase A~D가 무엇을 가르치는지 분리해서 읽을 수 있음.

---

## §3 — TMDD 곡선의 4 phase: 시간이 아니라 농도 영역의 지도

> 🎯 **학습목표**: 이 섹션 끝내면 "TMDD 곡선의 Phase A~D를 **시간 순서가 아니라 농도 영역의 지도**로 읽는 법"과, "왜 고용량 곡선만 잘 맞아도 저용량에서 함정(phantom linearity)이 숨을 수 있는지"를 설명할 수 있게 됨.

**왜 지금 (동기 / 다리)**: §2의 4관문을 통과한 곡선이라도, **표적 결합이 끼는 순간 곡선은 더 이상 시간표가 아님** — 농도 영역의 지도가 됨. Phase A→B→C→D를 "시간 순서"로 외우면 임상에서 망함. **농도 위계**로 읽어야 함. (척추 호출: 어떤 phase가 실제로 보이느냐가 곧 어떤 파라미터가 식별 가능하냐를 정함.)

### 먼저 — 왜 TMDD가 비선형인가 (1학년 막히는 지점, 비유 선제 배치)

(비유) **약 = 유도탄, 표적 = 적 기지(수용체), 같이 사라짐 = internalization(세포 안으로 끌려들어가 함께 분해됨).** 유도탄(약)이 적 기지(표적)에 **달라붙으면 함께 폭발(분해)**함. 그런데 **적 기지 수가 한정돼 있음.** 그래서—

- **약을 조금만 주면(저농도)**: 표적이 아직 안 찼으니, 약이 표적에 붙어 같이 사라지는 **표적 경로가 강하게 작동** → 농도 따라 청소율이 변함 = **비선형**.
- **약을 잔뜩 주면(고농도)**: 표적이 이미 다 차버려서(포화) 표적 경로가 더 이상 약을 못 빨아들임 → 남는 건 비특이적 제거뿐 = **선형**.

이 1:1 대응을 꼭 기억 — 유도탄=약, 적 기지=표적, 같이 폭발=internalization(complex가 세포로 끌려가 소실). 이게 TMDD 비선형의 전부임. 표적은 §1에서 본 "유한한 욕조"라서 다 차면 더는 못 받음 [G&W p.604, Fig.27.3].

### PK27 데이터셋 한 번 더

이 세션의 척추 PK27을 다시 꺼냄. 항체(약, ligand=L)를 **1.5, 5, 15, 45 mg·kg⁻¹** 네 용량으로 급속 정맥주사한 데이터임 [G&W pp.602–603]. 용량별로 층화(나눠서)해서 봐야 하는 이유 — **곡선이 어떤 phase를 실제로 관찰했는지가 용량마다 다름.**

PK27에서 표적 기저량 $R_0 \approx 12$ mg·L⁻¹, 그리고 $K_m \approx 0.03$ mg·L⁻¹임 (이 $K_m$이 뭔지는 §5에서 풀어줌 — 지금은 "포화 경계 농도"로만). 약 농도 $C_L$이 이 역치들을 통과하면서 phase가 갈림:

$$
\underbrace{C_L}_{\text{약(ligand) 농도}}
\quad\text{고농도→저농도 순차 통과}\quad
\overbrace{
  \underbrace{R_0}_{\text{표적 수준}}
  \;\to\;
  \underbrace{K_m}_{\text{포화 경계}}
  \;\to\;
  \underbrace{K_d}_{\text{결합 경계}}
}^{\text{phase 전환점}}
$$

### 4 phase의 정체

| 단계 | 지배 과정 | 농도 위치 | 쉬운 해석 |
|---|---|---|---|
| **A** | 빠른 2차 결합 | 주사 직후 최고 농도 | 약과 표적이 순식간에 평형 |
| **B** | **1차 비특이 제거** | 표적 포화 영역 | 표적 경로가 다 차서 비특이 선형 제거가 지배 |
| **C** | 혼합차수 배치 | 표적 부분 포화 | 선형 + 표적 매개 경로 공존 |
| **D** | $k_{off}$·$k_{e(RL)}$ 주도 | 매우 낮은 약 농도 | 표적 특이 제거가 드디어 보임 |

(용어 미리) $k_{off}$ = complex가 풀리는 속도, $k_{e(RL)}$ = complex가 세포로 끌려가 비가역으로 사라지는 sink 속도. 둘 다 §4에서 풀어줌.

> ⚠️ **Phase B의 "느린(slow)"은 함정임.** 표준 TMDD 문헌(Mager & Jusko 2001; Peletier & Gabrielsson 2012)과 R&T 본문은 Phase B를 *"drug is mainly eliminated directly by a first-order process"*(약이 주로 1차 과정으로 직접 제거됨)로 기술함 [R&T p.712]. 즉 Phase B는 **표적 경로가 포화돼 비특이 선형 청소율이 지배하는 영역**이고, 절대적 청소율 척도로는 **Phase D보다 빠름**. 저농도 Phase D에서 오히려 $k_{off}$·$k_{e(RL)}$ 주도의 **매우 느린 말기 기울기**가 나옴. "slow"라는 단어 때문에 "A→B→C→D = 점점 느려짐"으로 단조 해석하면 안 됨. **농도 위계가 시간 위계와 꼭 일치하는 게 아님.**

### 왜 시간 순서가 아니라 농도 위계인가 — 한방 직관

생각해볼 것 — 고용량(45 mg/kg)을 주면 약이 표적을 완전히 압도해서, 곡선은 비특이 제거 쪽(Phase B)만 길게 깔리고 정말 마지막 미량에서야 Phase D가 살짝 보임. **저용량(1.5 mg/kg)을 주면** 약이 표적에 비해 충분히 많지 않으니 표적 특이 경로가 처음부터 끝까지 계속 작동함 → **Phase C, D가 훨씬 일찍, 훨씬 뚜렷하게** 보임 [G&W p.605]. 그래서 phase는 시간 좌표가 아님 — **용량이 정하는 농도 영역의 지문**임.

### 곡선이 가르치는 것 / 안 가르치는 것

곡선의 한계를 한 줄씩 [G&W pp.603–609]:

- 고용량 데이터만 봤다면 표적 경로가 이미 포화라 **선형처럼 보임** → MM 모델로도 잘 맞는 것처럼 보임.
- assay(측정법) 민감도가 낮아 저용량 데이터가 빠지면 Phase A와 D를 못 봄.
- sc 흡수가 느리면 초기의 빠른 결합(Phase A)이 흡수 동역학 뒤에 가려짐.
- 표적·복합체 데이터가 없으면 ligand-only 적합이 좋아 보여도 $k_{on}, k_{off}, k_{e(RL)}$의 정밀도는 그대로 낮음. (척추: 측정 안 한 종은 모델이 못 지어냄.)

### 실무 판독 규칙 (D2 — 흔한 실수)

TMDD plot은 **용량별로 층화**해서 보는 게 첫걸음임. 고용량은 잘 맞는데 **저용량 잔차가 체계적으로 한쪽으로 쏠려 있으면** — 이게 **phantom linearity(가짜 선형성)**의 신호임. 중심에선 겉보기 성공인데 저농도 외삽에선 편향이 숨은 상태임. PK27의 123배 사건이 정확히 이 패턴이었음 [G&W p.609].

> 💡 **Phase 라벨은 시간이 아니라 농도 영역의 지문임.** Full TMDD와 MM 중 뭘 쓸지 정하기 전에, 용량별 층화 곡선에서 **실제로 관찰된 phase가 무엇인지 먼저 표시**해 둬야 함.

**§3 한 줄 결론**: **보이는 phase가 곧 식별 가능한 기전임.** 고용량 적합만 평가하는 함정을 피해야 phantom linearity에 안 속음. (다리: 그럼 그 phase를 만들어내는 ODE 자체를 §4에서 분해함.)

---

## §4 — Full TMDD: 4-state ODE의 정체 [핵심 섹션]

> 🎯 **학습목표**: 이 섹션 끝내면 "Full TMDD의 4개 상태변수와 각 방정식이 무엇을 뜻하는지", 그리고 "**자료 풍부도(ligand만 vs +target vs +complex)**가 $k_{on}, k_{off}, k_{e(RL)}$의 정밀도를 어떻게 바꾸는지"를 숫자로 설명할 수 있게 됨.

**왜 지금 (동기 / 다리)**: §3에서 4 phase가 농도 지문이라는 걸 잡았으면, 이제 그 지문을 **만들어내는 ODE 자체**를 분해해야 함. 이게 Full TMDD임. (척추 정중앙: 이 섹션의 결론이 곧 "자료 풍부도가 식별성을 정한다"임.)

### Full TMDD는 "복잡한 MM"이 아님 (흔한 오해 먼저)

가장 자주 하는 오해부터 깸 — Full TMDD는 "MM에 target·complex 이름표를 붙인 복잡한 포화 청소율 모델"이 **아님**. **약의 배치, 표적 turnover, 결합, complex sink를 서로 다른 state(상태)와 ODE 항으로 분리하는 모델**임. 한 마디로 — **관찰 안 한 종(species)의 기전은 추정값이 아니라 가정임.**

### 4개의 상태변수 (state)

(용어) state = "이 시각에 얼마나 있나"를 추적하는 양. PK27은 이걸 **8-parameter full TMDD model**이라 부름 — $V_c=0.05$ L·kg⁻¹를 고정한 뒤 Table 27.2가 보고하는 추정 파라미터가 8개라서임. 고정한 $V_c$까지 구조량으로 세면 **4 state + 9 structural quantities**임 [G&W pp.603, 608–609].

| 상태변수 | 의미 |
|---|---|
| $L_c$ | 중심 구획(central, 혈장)의 약(ligand) |
| $L_t$ | 조직/말초(tissue) 구획의 약 |
| $R$ | 자유 표적(free target/receptor) |
| $RL$ | 약-표적 복합체(complex) |

$$
\underbrace{\mathbf{x}(t)}_{\text{TMDD 상태벡터}}
=
\left(
\underbrace{L_c}_{\text{혈장 약}},\;
\underbrace{L_t}_{\text{조직 약}},\;
\underbrace{R}_{\text{자유 표적}},\;
\underbrace{RL}_{\text{복합체}}
\right)
$$

PK27 Table 27.2의 8개 보고 파라미터는 $Cl, k_{on}, k_{off}, V_t, Cl_d, k_{out}, R_0, k_{e(RL)}$임(여기 $k_{out}$은 §1에서 배운 표적 배수구 $k_{deg}$와 **같은 것** — G&W 표는 $k_{out}$으로, 우리 ODE는 $k_{deg}$로 적었을 뿐임). $V_c$는 $0.05$ L·kg⁻¹로 고정 [G&W pp.603, 608].

### 핵심 ODE — Target과 Complex 식 (식 3단)

약(ligand) 식은 일반 2구획 + 결합 sink 형태라 익숙함. 진짜 핵심은 **target과 complex 식**임. 식 두 개가 연달아 나오니 사이에 다리를 깔며 읽음.

**① 왜 필요**: §1 욕조(생성·소실)에 §3 결합(붙고 떨어짐)을 합쳐야, "표적이 약 때문에 줄었다가 회복하는" 전 과정을 적을 수 있음.

$$
\overbrace{\frac{dR}{dt}}^{\text{자유 표적 변화}}
=
\underbrace{k_{syn}}_{\text{생성(§1 수도꼭지)}}
-\underbrace{k_{deg}R}_{\text{자연 소실(§1 배수구)}}
-\underbrace{k_{on}LR}_{\text{약과 결합해 빠짐}}
+\underbrace{k_{off}RL}_{\text{복합체 풀려 돌아옴}}
$$

**② 기호 뜻**: 앞 두 항은 §1 욕조 그대로($k_{syn}$ 생성, $k_{deg}$ 소실). 뒤 두 항이 새것 — $k_{on}LR$은 약 $L$과 표적 $R$이 만나 복합체로 빠지는 양(2차 = $L$과 $R$ 둘 다 곱함), $k_{off}RL$은 복합체가 도로 풀려 표적이 돌아오는 양.

(다리 한 줄) 표적이 빠진 만큼 복합체가 생기니, 복합체 식은 그 거울임:

$$
\overbrace{\frac{dRL}{dt}}^{\text{복합체 변화}}
=
\underbrace{k_{on}LR}_{\text{복합체 형성}}
-\underbrace{k_{off}RL}_{\text{해리(풀림)}}
-\underbrace{k_{e(RL)}RL}_{\text{sink: 세포로 끌려가 소실}}
$$

**③ 한 줄 결론**: 표적은 욕조처럼 돌면서 약과 붙었다 떨어지고, 붙은 복합체는 일부가 $k_{e(RL)}$로 영영 사라짐(=유도탄+기지 동반 폭발). 이 sink가 약을 추가로 없애는 게 TMDD의 핵심 [G&W Eq.27:1–27:3, pp.606–607].

### ★혼동쌍 즉시정정 (C7) — $k_{on}LR$ vs $k_{syn}\cdot L\cdot R$

여기서 **절대 헷갈리면 안 되는 한 줄** — 결합 속도항은 $k_{on}\cdot L\cdot R$임. **$k_{syn}\cdot L\cdot R$이 아님.** $k_{syn}$은 **표적 합성**(§1 수도꼭지) 쪽이고, $k_{on}$은 **약-표적 결합의 2차 on-rate**(붙는 속도)임. 표기 차이가 아니라 **turnover(생성) 과정과 binding(결합) 과정을 가르는 핵심 갈림길**임 [G&W pp.604, 606–607]:

$$
\underbrace{\text{결합속도}}_{\text{복합체 형성}}
=
\underbrace{k_{on}}_{\text{2차 on-rate(붙기)}}
\cdot
\underbrace{L}_{\text{약}}
\cdot
\underbrace{R}_{\text{자유 표적}}
\quad\ne\quad
\underbrace{k_{syn}\cdot L\cdot R}_{\text{과정 혼합(오류)}}
$$

(§1에서 예고한 단위 함정이 바로 여기임 — $k_{syn}$은 양/시간, $k_{on}$은 농도⁻¹·시간⁻¹. 둘을 섞으면 단위부터 안 맞음.)

### 자료 풍부도 — 이 세션의 진짜 결론 (★척추)

여기가 이 섹션, 그리고 세션 전체 결론에 가까운 부분임. PK27은 세 데이터셋을 비교함:

- **Dataset I**: ligand(약) 단독
- **Dataset II**: ligand + target
- **Dataset III**: ligand + target + complex

표적·복합체 시간경과 데이터가 추가될수록 핵심 파라미터의 정밀도가 줄줄이 좋아짐. **CV%**(coefficient of variation, 변동계수 — 추정값이 얼마나 흔들리나, 작을수록 정밀)의 변화 [G&W p.609, Table 27.2]:

$$
\begin{aligned}
\underbrace{CV\%(k_{on})}_{\text{붙는 속도 정밀도}} &: \underbrace{17 \to 2 \to 1}_{\text{I → II → III}},\\
\underbrace{CV\%(k_{off})}_{\text{풀림 속도 정밀도}} &: \underbrace{27 \to 13 \to 3}_{\text{target 추가}},\\
\underbrace{CV\%(k_{e(RL)})}_{\text{sink 정밀도}} &: \underbrace{27 \to 23 \to 2}_{\text{complex 추가가 결정타}}
\end{aligned}
$$

읽는 법 — $k_{e(RL)}$(sink)는 target까지 재도(27→23) 별로 안 좋아지다가, **complex를 재는 순간 2로 급좋아짐**. complex의 거동을 가장 직접적으로 가르치는 게 complex 데이터라서임.

한 줄로 — **ligand 데이터는 비특이 배치와 보이는 phase 구조를, target 데이터는 회복·포화 경계를, complex 데이터는 sink 거동을 가르침** [G&W pp.603, 608–609].

> 💡 **식별성의 분업표**:
> - **ligand 데이터** → 배치(disposition)를 가르침
> - **target 데이터** → 회복(recovery)·포화 경계를 가르침
> - **complex 데이터** → sink를 가르침
>
> 측정 안 한 종의 파라미터는 "추정값"이 아니라 "가정"임. (← 척추 그 자체)

### 적합 품질 ≠ 기전 타당성 — PK27의 123배 사건 (★PK27 경계 사례)

여기가 이 세션 hook(낚싯바늘)의 정체임. PK27에서:

$$
\underbrace{\frac{K_{m,\mathrm{MM}}}{K_{m,\mathrm{TMDD}}}}_{\text{MM 편향}}
=
\underbrace{\frac{3.7}{0.03}}_{\text{PK27 두 값}}
\approx
\underbrace{123}_{\text{약 123배 과대}}
$$

(정직 표기 — B2/B3) 이건 "충돌"이 아니라 **근사 단계(Full vs MM)에 따라 달라지는 값**임 [G&W pp.602–610]. Full TMDD 모델이 준 $K_m$은 0.03, 줄인 MM 모델이 준 $K_m$은 3.7 — MM이 **약 123배 과대추정**한 거임 [G&W p.609]. "곡선은 맞아도 파라미터가 틀림"의 대표 사례임.

reduced(MM) 모델은 가장 높은 세 곡선은 꽤 잘 맞춤. 그런데 **가장 낮은 곡선에서 실패**함. 그 결과 $K_m$이 123배 부풀고, 이 편향이 trough(최저농도) 예측·target occupancy(표적 점유율) 추정·subgroup 외삽으로 그대로 번짐 [G&W p.609].

**왜 이런 일이?** — MM 근사는 **약 ≫ 표적** 조건(약이 표적을 압도해 결합이 빠르게 평형 도달, 표적 경로가 계속 포화)에서만 Full TMDD로부터 구조적으로 유도됨. 그 조건이 깨지는 영역 — 약 농도가 $K_d$나 $K_m$ 부근(표적 포화 전환점)으로 떨어지는 구간, 그리고 매우 낮은 선형 영역 — 에서 MM은 PK 거동을 구조적으로 잘못 예측함. PK27의 0.03 vs 3.7이 바로 이 경계 위반의 정량 흔적임.

**임상에서 어떻게 드러나나** — 저용량 1상 데이터에서 MM이 OFV·VPC(적합 지표) 기준으로 잘 맞은 것처럼 보일 수 있음. 그런데 중간 용량의 비선형 전환점(Phase B↔C↔D 전이)을 기전적으로 못 예측해서 **2상 용량 선택이 어긋남**. 또는 고용량으로 적합된 MM이 sub-population(저체중, 높은 표적 부담 등) 외삽에서 trough를 체계적으로 잘못 예측해서 후속 임상 결정의 출발 좌표가 흔들림.

### 도구 정의 — NONMEM 스타일 구현 (D3 — 도구 정의 먼저)

(도구 정의) **NONMEM**(NONlinear Mixed-Effects Modeling) = 약동·약력 데이터를 비선형 혼합효과 모델로 적합하는 표준 소프트웨어임. 아래는 교과서 control stream이 아니라 **PK27/R&T ODE 구조를 NONMEM 스타일로 교육용 번역**한 골격임. 단위 정합성을 직접 확인하라고 **두 가지 표기**를 보여줌.

**(a) 모든 상태변수를 농도로 두는 경우** — R&T Eq.21-1~21-4 표기와 일치 [R&T p.711]:

```text
; (a) 농도 기반: A(i)를 농도로 직접 처리
CLIG = A(1)        ; 중심 구획 약 농도
CTIS = A(2)        ; 조직 구획 약 농도
R    = A(3)        ; 자유 표적 농도
RL   = A(4)        ; 복합체 농도

BIND = KON * CLIG * R          ; 농도/시간, volume 변환 없음
DISS = KOFF * RL
SINK = KERL * RL

DCDT(1) = INPUT/VC - (CL/VC)*CLIG - (Q/VC)*(CLIG-CTIS) - BIND + DISS
DCDT(2) = (Q/VT)*(CLIG-CTIS)
DCDT(3) = KSYN - KDEG*R - BIND + DISS
DCDT(4) = BIND - DISS - SINK
```

**(b) 모든 상태변수를 amount(양)로 두고 volume 변환을 명시하는 경우** — NONMEM 표준 DADT 표기:

```text
; (b) 양 기반: A(i)는 양, 결합 전에 농도로 변환
CLIG = A(1)/VC      ; 중심 농도
CTIS = A(2)/VT      ; 조직 농도
RC   = A(3)/VR      ; 자유 표적 농도 (혈장 표적이면 VR=VC)
RLC  = A(4)/VR      ; 복합체 농도

BIND = KON * CLIG * RC * VR    ; 양/시간 — volume 변환 명시
DISS = KOFF * A(4)
SINK = KERL * A(4)

DADT(1) = INPUT - CL*CLIG - Q*(CLIG-CTIS) - BIND + DISS
DADT(2) =  Q*(CLIG-CTIS)
DADT(3) =  KSYN*VR - KDEG*A(3) - BIND + DISS    ; KSYN가 농도/시간이면 VR 곱함
DADT(4) =  BIND - DISS - SINK
```

> ⚠️ **두 표기를 절대 섞으면 안 됨.** 흔한 함정 — `BIND = KON * CLIG * R * VC`라고 쓰는 경우가 있는데, 이건 **R이 농도일 때만** 옳음. R이 amount면 volume 변환이 더 필요해서 mass balance(질량 보존)가 조용히 깨짐. PK27 원전(G&W Eq.27:1~27:3) mass-balance는 둘 중 하나로 **일관되게** 잡혀야 함 [G&W pp.606–607; R&T p.711].

**실무 디버깅 한 줄** — 두 표기를 혼용하면 정상상태에서 $R_0=k_{syn}/k_{deg}$ 관계가 미묘하게 어긋나, 모델은 적합되는데 baseline drift(기준선 표류)가 **자료가 아니라 표기 오류 때문에** 생김. 가장 안전한 디버깅은 **dose=0 시뮬레이션에서 $R$이 정확히 $R_0$로 수렴하는지** 먼저 확인하는 것임.

### Soluble(가용성) vs Membrane-bound(막결합) 표적 — 임상 분기점

PK27이 다루는 표적은 **soluble target**(혈장에 떠다니는 가용성 표적)임 [G&W p.602]. 그런데 임상 mAb에서는 표적이 soluble이냐 membrane-bound(세포막에 박힌)냐가 **TMDD signature의 phase 구조 자체를 바꾸는 갈림길**임. G&W도 PK27 본문에서 *"membrane bound targets could have very different impact on the ligand disposition"*(막결합 표적은 약 배치에 매우 다른 영향을 줄 수 있음)이라고 명시 경고함 [G&W p.605].

| 비교 기준 | Soluble (VEGF, TNF-α, IgE) | Membrane-bound (HER2, CD20, CD11a) |
|---|---|---|
| 복합체의 운명 | 약-표적 복합체가 **혈장에 같이 순환** | 복합체가 세포 안으로 **internalize**돼 곧장 sink |
| 표적 turnover | 혈장에서 $k_{syn}/k_{deg}$ 측정 가능 | 세포 표면 발현·shedding(떨어져 나옴)·internalization 얽힘 |
| Phase A 신호 | 빠른 결합이 혈장 곡선에 잘 보임 | internalize 빠르면 Phase A가 흡수돼 안 보일 수 있음 |
| Total assay 해석 | total = free + complex(둘 다 혈장) | total이 떨어져 나온 항원만 잡고 막결합 표적은 못 잡음 |
| 대표 mAb | bevacizumab(VEGF), adalimumab(TNF), omalizumab(IgE) | trastuzumab(HER2), rituximab(CD20), efalizumab(CD11a) |

(임상 mAb 예시 출처 — R&T) trastuzumab=항-HER2(유방암) [R&T p.699·p.714 분류표], rituximab=항-CD20(비호지킨 림프종, 표적세포 파괴) [R&T p.715], efalizumab=항-CD11a(건선, 세포 기능 변경) [R&T p.714]. **rituximab/trastuzumab류는 복합체가 세포로 끌려가는 internalization sink**, **bevacizumab/adalimumab/omalizumab류는 가용성 표적**임. (efalizumab은 막결합 CD11a 표적이지만 PK26에서 reduced model로 다룸 — §5 참조.)

수식으로 보면 차이는 complex sink 항의 **물리적 해석**에 들어감:

$$
\overbrace{\frac{dRL}{dt}}^{\text{복합체 변화}}
=
\underbrace{k_{on}LR}_{\text{형성}}
-\underbrace{k_{off}RL}_{\text{해리}}
-\overbrace{\underbrace{k_{e(RL)}RL}_{\text{soluble: 혈장 청소}}\ \text{vs}\ \underbrace{k_{int}\cdot RL}_{\text{membrane: internalize 직행}}}^{\text{같은 1차 항인데 의미가 갈림}}
$$

수학 형태는 같은 1차 소실인데, soluble에선 $k_{e(RL)}$이 약의 비특이 청소와 비슷한 경로일 가능성이 높고, membrane-bound에선 $k_{int}$가 수용체 internalization·lysosome 분해의 결합 속도임.

**실무 한 줄** — 새 mAb 후보 모델링을 시작할 때 가장 먼저 적을 한 줄은 "이 표적은 soluble인가, membrane-bound인가, 아니면 둘 다(shed antigen)인가?"임. PK27의 4-state Full TMDD는 soluble에 가장 직접 적용되고, membrane-bound/shed-antigen이면 추가 state(막 R, shed R, 두 종류 complex)가 필요할 수 있음 `[교과서 외: G&W·R&T 09 본문 범위를 넘는 일반 모델링 디테일]`.

### ADA — TMDD signature의 시간 의존 변형

soluble vs membrane이 **표적 쪽 분기**라면, ADA(anti-drug antibody, 항약물항체 — 몸이 약을 외부 침입자로 보고 만드는 항체)는 **숙주 면역계 쪽 분기**임. PK27의 single-dose(단회) 데이터엔 ADA가 안 보이지만, **임상 mAb의 repeated-dose(반복) 데이터에선 ADA 형성이 TMDD signature를 시점에 따라 변형**시킴 [R&T p.712].

기전 — 항약물항체가 생기면 mAb-ADA 면역복합체가 식세포(phagocyte)의 흡수와 lysosome 분해를 자극해 mAb 청소율을 끌어올림 [R&T p.712].

| signature 변형 | 임상·모델링 신호 |
|---|---|
| **Phase B(선형) 청소율 급증** | 표적 turnover 변화 없이 비특이 선형 CL이 시간 따라 증가 |
| **변동 폭발(BSV↑)** | 일부 환자만 trough가 치료 이하로 떨어지고 나머지는 그대로 (이봉성) |
| **시점 의존 PK** | 같은 환자 PK가 초기 dose와 후기 dose에서 다름 |

ADA 시간 척도 — R&T Fig.21-19(cynomolgus monkey의 anti-tetanus toxoid ADA)가 보여줌: **ADA titer가 약 200시간(약 8~9일)에 검출 시작, 약 400~500시간(약 17~21일)에 정점** [R&T p.725]. 이 정도면 다회 투여 mAb의 2~3번째 dose 구간부터 "변하지 않는 선형 CL" 가정이 깨질 수 있음.

ADA 위험 인자 [R&T p.725]:
- 투여 경로: **s.c. > i.m. > i.v.** (피하가 가장 면역원성↑)
- 분자 응집(aggregation)이 많을수록 면역원성↑
- 단백질의 인간 유사도: murine(쥐) > chimeric(키메라) > humanized(인간화) > human(인간) 순으로 면역원성↑

> ⚠️ **모델링 함정** — ADA 매개 청소율 증가를 단순 "표적 turnover 변화"로 잡으면 $k_{syn}$나 $R_0$를 잘못 추정함. 두 신호는 **시간 위계가 다름** — 표적 turnover 변화는 보통 baseline 시점부터 차이가 있는 반면, ADA 매개 변형은 **dose 후 약 200h 이후부터 켜지는 시간 지연 신호**임. ADA가 의심되면 **dose-elapsed-time(투여 후 경과시간) 공변량**이나 occasion-based IOV(투여 회차별 변동) 구조로 두 신호를 분리할 수 있는지 먼저 봐야 함.

**§4 한 줄 결론**: Full TMDD의 핵심은 "파라미터가 많다"가 아니라 **약 곡선 안에 숨은 표적 turnover·결합·complex sink를 분리하는 것**임. target과 complex 데이터가 같이 있어야 $k_{on}, k_{off}, k_{e(RL)}$의 식별성이 살아남. ligand-only 적합이 좋아 보일 땐 "biologically learned(기전을 배움)"가 아니라 "fitted but not learned(맞췄지만 못 배움)"일 수 있다는 걸 기억해야 함.

---

## §4½ — QSS: Full과 MM 사이의 실무 표준

> 🎯 **학습목표**: 이 섹션 끝내면 "근사 사다리(Full → QSS → MM)에서 **QSS가 어떤 가정에서 나오고**, 왜 임상 mAb 분석의 실무 출발점이 되는지", 그리고 "$K_{ss}$와 $K_m$이 왜 같은 분수식인데 다른 뜻인지"를 설명할 수 있게 됨.

**왜 지금 (동기 / 다리)**: §4의 Full TMDD와 §5의 MM 사이엔 **중간 근사 단계가 사슬처럼** 있음. 임상 mAb 분석에서 실제로 가장 많이 쓰는 건 Full도 MM도 아니라 그 사이의 **준정상상태(QSS) 근사**임. R&T 본문이 PK27 4-phase 그림 바로 다음 문단에서 *"quasi-steady state or quasi-equilibrium approximations can be used"*(준정상상태 또는 준평형 근사를 쓸 수 있다)라고 명시함 [R&T p.712].

핵심 — **QSS를 "MM의 별명"으로 외우면 안 됨.** QSS는 complex의 동역학에 명시적 가정을 두고 **ligand·target 수준에서 식별성을 회복**시키는 단계임. MM은 그 위에 "약 ≫ 표적" 가정을 한 개 더 얹어 한 항으로 접은 형태임. 그래서 QSS는 보통 MM보다 **더 넓은 농도 영역에서 방어 가능**하고, 생물약품 PopPK 실무의 출발점이 됨.

(범위 정직 표기) R&T 본문이 직접 인용한 건 "QSS/QE 근사를 쓸 수 있다 + QE는 internalization이 dissociation보다 훨씬 느릴 때 적절" [R&T p.712]까지임. 아래의 **$K_{ss}=(k_{off}+k_{e(RL)})/k_{on}$ 유도와 free/complex의 QSS 해**는 표준 계량약리학(Mager·Gibiansky류)이지만 **09 본문 txt 범위는 넘음** → `[교과서 외: 표준 TMDD 근사 이론, 09_G/09_T 본문엔 식 자체는 없음]`로 표시함.

### 근사 사다리 — 한 표로

| 근사 단계 | 핵심 가정 | 식별 가능한 양 | 주 사용처 |
|---|---|---|---|
| **Full TMDD** | 가정 없음 | $R_0, k_{deg}, k_{on}, k_{off}, k_{e(RL)}$ | target·complex 자료 풍부할 때 |
| **Rapid Binding / Quasi-Equilibrium (QE)** | $k_{on}, k_{off} \gg k_{e(RL)}$ | $K_d=k_{off}/k_{on}$ 중심 | 매우 강한 결합 [R&T p.712] |
| **Quasi-Steady-State (QSS)** ▶ **실무 표준** | $d[RL]/dt \approx 0$ | $K_{ss}=(k_{off}+k_{e(RL)})/k_{on}, R_0, k_{deg}$ | 대부분 생물약품 PopPK 출발점 `[교과서 외 식]` |
| **Michaelis-Menten (MM)** | $L \gg R$ 또는 점유율 ≈ 100% | $V_{max}, K_m$ (target/complex 식별 불가) | 자료 한정, 고용량 내삽 위주 |

### QSS 도출 — 한 줄로 (식 3단)

**① 왜 필요**: complex를 매번 풀기 싫고(자료도 없고), 그래도 ligand·target 수준 상수는 살리고 싶음.

Full TMDD의 complex 식(R&T Eq.21-4)에서 출발:

$$
\overbrace{\frac{d[RL]}{dt}}^{\text{복합체 변화}}
=
\underbrace{k_{on}LR}_{\text{형성}}
-\underbrace{(k_{off}+k_{e(RL)})RL}_{\text{해리+sink}}
$$

**② 기호 뜻 / 가정**: QSS 가정 = complex가 ligand·target보다 **훨씬 빠른 시간 척도**로 평형에 도달 → 우변 ≈ 0으로 둠:

$$
\underbrace{k_{on}LR}_{\text{형성}}
\approx
\underbrace{(k_{off}+k_{e(RL)})RL}_{\text{해리+sink}}
\;\Longrightarrow\;
\overbrace{\underbrace{K_{ss}}_{\text{QSS 상수}}=\frac{k_{off}+k_{e(RL)}}{k_{on}}}^{\text{[교과서 외 식]}}
$$

(다리 — 비유) complex가 "엄청 빠르게 들락거리는 회전문"이라 평균적으로 양이 안 변한다고 보는 거임. 그럼 그 회전문 양은 ligand·target만으로 계산됨.

**③ 한 줄 결론**: $K_{ss}$는 **수식 형태가 $K_m$과 똑같음**. 그런데 의미가 다름 —
- $K_m$ = "겉보기 포화 경계"(MM에서)
- $K_{ss}$ = **complex의 준정상상태로부터 명시적으로 유도된 ligand·target 평형 상수**(QSS에서)

같은 분수, 다른 가정, 다른 해석임. (이 구분이 아래 §5 C7의 핵심.)

QSS 아래 total target $R_{tot}=R+RL$ 관계에서 free $R$과 complex $RL$이 풀림 `[교과서 외 식]`:

$$
\underbrace{R}_{\text{자유 표적}}
=
\frac{R_{tot}\,K_{ss}}{K_{ss}+L}
,\qquad
\underbrace{RL}_{\text{복합체}}
=
\frac{R_{tot}\,L}{K_{ss}+L}
$$

이게 가르치는 것 — **complex를 직접 안 재도, ligand와 total target만으로 $K_{ss}$를 식별할 수 있음.** Full TMDD가 요구하던 "complex assay 풍부도"를 우회함. 이게 생물약품 PopPK에서 QSS가 거의 표준이 된 이유임.

### MM과의 관계 — "한 가정 더 얹으면 MM"

QSS에 추가로 **$L \gg R$**(표적 점유율 ≈ 100%) 가정을 얹으면 MM이 나옴:

$$
\underbrace{K_{ss}}_{\text{QSS}} \xrightarrow{\,L\gg R\text{ 추가}\,} \underbrace{K_m}_{\text{MM}}
,\qquad
\underbrace{V_{max}}_{\text{MM}} \approx \underbrace{k_{e(RL)}\cdot R_{tot}}_{\text{포화 시 sink 처리능}}
$$

결정적 차이 — MM에선 **$R_{tot}$ 자체가 안 보이게 잠김**. 그래서 MM은 표적 turnover($k_{syn}, k_{deg}$)와 complex sink($k_{e(RL)}$)를 분리 추정 못 하고, $V_{max}/K_m$ 두 macro-parameter만 남음. **PK27에서 $K_m$이 0.03→3.7로 123배 부푼 이유 중 하나가 정확히 이거임** — MM은 $R_{tot}$ 변동을 추적할 도구를 잃어서, 저용량(표적이 안 찬 영역)에서 구조 편향이 쌓임 [G&W p.609].

### 세 K 상수 한 자리에 (★C7 즉시정정 — $K_d$ vs $K_{ss}$ vs $K_m$)

> 💡 **세 가지 K 상수를 절대 같은 단어로 부르면 안 됨.** 같은 'K'지만 각각 **다른 가정에서 나온 환율(환산 상수)**임.
>
> $$
> \overbrace{K_d}^{\text{순수 결합 세기}} = \frac{k_{off}}{k_{on}}
> \;\;<\;\;
> \overbrace{K_{ss}}^{\text{준정상상태 겉보기 비}} = \frac{k_{off}+k_{e(RL)}}{k_{on}}
> \;\;=\;\;
> \overbrace{K_{m}}^{\text{MM 포화 겉보기 상수}} = \frac{k_{off}+k_{e(RL)}}{k_{on}}
> $$
>
> - **$K_d$**(dissociation constant, 해리상수) = off÷on, **순수 결합 세기**. complex sink가 안 들어감 → 두 동역학 상수와 본질이 다름.
> - **$K_{ss}$** = "complex의 QSS" 한 가정만 두고 ligand·total target 수준에서 식별되는 **겉보기 비**.
> - **$K_m$** = 거기에 "$L\gg R$" 한 가정을 더 얹어 $R_{tot}$가 사라진 **MM 포화 겉보기 상수**.
>
> $K_{ss}$와 $K_m$은 **분수식은 같지만 도출 가정이 다름.** 셋을 "포화상수" 하나로 뭉뚱그리면 논문 숫자를 오독함 — 리포트에서 셋을 같은 단어로 부르면 reviewer가 반드시 reconciliation(정합 설명)을 요구함.

### QSS의 한계

QSS도 만능은 아님:
- complex 동역학이 ligand·target과 **같은 시간 척도**면 QSS가 깨짐 (예: internalize가 매우 느린 막결합 표적).
- QSS는 $k_{on}$과 $k_{e(RL)}$를 **개별 식별 못 함** — 두 값의 합비 $K_{ss}$만. "표적 점유율을 micro-parameter 수준에서 기전적으로 시뮬레이션" 요구가 있으면 Full TMDD 필요.
- **soluble 표적에서 가장 깔끔**하게 작동. 막결합·shed antigen은 추가 state 필요.

**§4½ 한 줄 결론**: Full TMDD와 MM은 같은 사슬의 양 끝이고, 사이에 **QSS·QE라는 명시적 가정 단계**가 있음. 임상 mAb 실무 표준은 보통 QSS임. MM은 그 위에 "$L\gg R$"를 더 얹은 더 좁은 도구임. $K_{ss}$와 $K_m$이 같은 분수인 건 우연이 아니라 **MM이 QSS의 한 가정 추가 특수 경우**라서임.

---

## §5 — Michaelis-Menten의 경계: PK27 사건의 정량 흔적

> 🎯 **학습목표**: 이 섹션 끝내면 "MM 근사가 **어떤 4가지 조건**에서 허용되고 언제 깨지는지", 그리고 "$K_d$와 $K_m$을 왜 분리해야 하는지"를 설명하고, PK27 123배 사건을 한 컷으로 요약할 수 있게 됨.

**왜 지금 (동기 / 다리)**: §4½에서 QSS가 Full과 MM 사이 다리란 걸 잡았으면, 이제 결정해야 함 — **어떤 조건에서 이 사슬의 끝(MM) 한 줄로 접어도 되는가?**

(선행 보충 — C5) **Michaelis-Menten(미카엘리스-멘텐)이 뭐냐**: 원래 효소가 기질을 처리하는 속도식임. 일꾼(효소/표적)이 유한해서, 일감(약)이 적으면 비례해 빨리 처리하다가, 일감이 넘치면 일꾼이 다 차서 처리 속도가 **최대치 $V_{max}$로 포화**되는 곡선임. 그 반쯤 포화되는 농도가 $K_m$임. TMDD에선 "표적이라는 유한한 일꾼"이 약을 처리하는 걸 이 식으로 흉내 냄.

### MM은 "단순한 대체 모델"이 아님

MM 근사는 Full TMDD의 target·complex 하부 시스템을 $V_{max}$와 $K_m$ 둘로 줄이는 거임. $R$과 $RL$을 직접 안 보고 표적 매개 경로를 **하나의 포화 청소율 항**으로 접음. 진짜 문제는 적합이 아니라 — **어느 농도·점유율 영역에서 이 접기가 구조적으로 허용되나**임 [G&W p.609; R&T p.712]:

$$
\overbrace{Cl_{MM}}^{\text{포화 TMDD 청소율}}
=
\frac{\underbrace{V_{max}}_{\text{최대 처리능}}}{\underbrace{K_m}_{\text{반포화 경계}}+\underbrace{C}_{\text{약 농도}}}
$$

### ★C7 즉시정정 (TMDD에서 $K_d$ vs $K_m$)

Full TMDD 안에서 두 상수 정의를 같이 보면 차이가 명확함:

$$
\overbrace{K_d}^{\text{결합 해리상수}}
=
\frac{\underbrace{k_{off}}_{\text{해리}}}{\underbrace{k_{on}}_{\text{결합}}}
,\qquad
\overbrace{K_m}^{\text{겉보기 동역학상수}}
=
\frac{\overbrace{k_{off}+k_{e(RL)}}^{\text{해리+sink}}}{\underbrace{k_{on}}_{\text{결합}}}
$$

$K_d$는 binding affinity(결합 친화도)에 가까운 **열역학 해리상수**, $K_m$은 complex 손실($k_{e(RL)}$)까지 포함한 **겉보기 동역학상수**임 [G&W pp.603–609; R&T pp.711–712]. **$K_d \ne K_m$인 이유는 단순함 — $K_m$에 $k_{e(RL)}$이 더 들어가서임.** 리포트 쓸 때 in vitro 열역학 $K_d$와 in vivo 모델 $K_m$을 반드시 분리해야 함. 둘 다 "affinity"라 부르면 내부 혼동이 생기고 reviewer가 reconciliation을 요구함.

(기억 고리) **$K_d$ = 결합의 언어(얼마나 단단히 붙나), $K_m$ = 결합 이후 sink까지 포함한 disposition의 언어.** 그리고 이 둘과 또 다른 차원이 표적 turnover($k_{syn}/k_{deg}$) — 표적이 얼마나 빨리 새로 만들어지고 분해되나라는 시스템 capacity임. **세 개가 서로 독립**이라 in vitro $K_d$ 하나로 in vivo TMDD의 임상 중요성을 판단 못 함.

> 💡 **MM은 접힌 모델임.** $V_{max}/K_m$은 표적 생물학을 없앤 게 아니라 관찰 가능한 포화 항으로 **압축**한 거임. 그래서 $K_m$은 $K_d$가 아니고($k_{e(RL)}$ 포함), **관찰된 포화·점유 영역 밖에선** 고용량 적합이 아무리 좋아도 MM 외삽을 정당화 못 함.

### MM이 통할 수 있는 4가지 조건

[G&W p.609; R&T p.712]:

1. 약(ligand) 농도가 표적 농도를 **크게 초과**할 때 ($L \gg R$)
2. 표적 점유율(occupancy)이 **거의 완전 포화**일 때
3. 관찰된 **용량 범위가 제한적**일 때
4. 목적이 저농도 외삽이 아니라 **관찰 프로파일 안에서의 내삽**일 때

(숫자 기준) 대략 **90~95% 이상 점유율**이 유지되면 단순화가 허용될 수 있음. 점유율이 $K_d$나 biomarker 역가 이하로 떨어지면 MM은 불충분 [G&W p.609]:

$$
\underbrace{\text{Occupancy(점유율)}}_{\text{표적 결합 비율}}
\gtrsim
\underbrace{90\text{–}95\%}_{\text{고포화 영역}}
\;\Rightarrow\;\text{MM 단순화 허용 가능}
$$

### PK26 Efalizumab — "reduced model이 정당화된 앵커" (숫자 예시 + 정직 표기)

**Efalizumab**(항-CD11a IgG1 mAb, 건선 치료제) 사례인 **PK26**이 좋은 reduced-model 앵커임. 2구획 모델 + parallel linear/MM 제거를 씀. **표적/복합체 데이터와 $k_{on}/k_{off}/K_d$ 정보가 없어서 full TMDD 적합 자체가 불가능**했기 때문임 [G&W pp.599–601]. 보고된 추정값:

$$
\overbrace{\{V_t, V_{max}, K_m, CL_d, CL_L\}}^{\text{PK26 reduced set}}
=
\underbrace{\{0.061,\,0.039,\,0.161,\,0.031,\,0.007\}}_{\text{보고 추정값 [G\&W Table 26.1]}}
$$

이 reduced model은 single-dose iv bolus의 5개 시간경과에 적합됨. → **"제한된 데이터에서 reduced model이 정당화된 앵커"로 읽어야 함.** "MM이 보편적으로 기전적"이라는 증거가 아님. (PK26과 PK27의 대비가 핵심 — PK26은 자료가 없어서 MM이 정당, PK27은 자료가 있는데도 MM이 저용량서 무너짐.)

### PK27 — MM이 무너지는 정량 흔적 (★다시 한 번)

PK27에서 MM은 가장 높은 세 곡선은 비교적 잘 맞춤. 그런데 **가장 낮은 곡선이 따로 놀았고, 추정 $K_m$이 3.7로 잡혀 Full TMDD의 0.03보다 약 123배 부풀었음** [G&W p.609].

임상 교훈은 "MM을 쓰지 마라"가 아님. 더 좁고 실용적임 — **표적 포화가 실증된 농도·점유 영역 밖에선 MM을 쓰지 마라.**

### 흔한 실수 / 혼동쌍 (D2)

| 흔한 혼동 | 교정 |
|---|---|
| Full TMDD는 복잡, MM은 단순한 대체 모델 | MM은 Full의 target/complex 하부를 reduction한 것 |
| 고용량 적합 좋으면 MM 충분 | PK27: 고용량 적합 좋아도 저용량 따로 놀고 $K_m$ 123배 부풂 |
| target/complex assay는 있으면 좋은 부가자료 | target/complex는 $k_{on}, k_{off}, k_{e(RL)}$ 정밀도를 정하는 **식별 자료** |

**실무 준칙** — TMDD 가능성이 있는 mAb에 MM을 쓰는 리포트라면 **관찰된 농도 범위, 표적 농도 범위, 투여 간격 동안 최소 예측 표적 점유율**을 명시해야 함. (이건 소스 경계의 구현 해석이지 규제기관이 직접 인용한 요건은 아님 — `[확인 필요: 규제 문서 직접 인용 아님]`.)

**§5 한 줄 결론**: MM은 빠르고 편한 도구일 수 있는데, **"적합이 잘 됨"과 "표적 생물학을 올바르게 외삽함"은 같은 말이 아님.** 관찰된 포화 영역 안 내삽이면 MM이 방어 가능하지만, 저농도 trough·recovery·점유 외삽에선 Full TMDD나 추가 데이터가 지배해야 함. 고용량 적합이 좋다고 MM이면 충분하다 결론지으면 **PK27처럼 $K_m$ 과대예측과 저용량 구조 편향이 그대로 임상 결정에 들어감.**

---

## 한 줄 요약

mAb 비선형 PK의 본질은 "항체가 크다"가 아님. **큰 약(ligand)이 제한된 조직 공간과 림프관 입력을 거쳐, 살아있는 표적 turnover 욕조(§1)에 들어가고, 결합·복합체·sink가 농도의존 청소율(§3 4-phase)을 만든다**는 것임. Full TMDD(§4)는 이 과정을 분해하고, QSS(§4½)는 임상 자료 한계 안에서 식별성을 회복시키고, MM(§5)은 일부 조건에서만 이를 한 항으로 압축함. 그래서 모델 선택 기준은 편의가 아니라 **데이터가 관찰한 phase + 임상 결정이 요구하는 외삽 범위**임. 척추 질문은 처음과 같음 — **"이 데이터가 실제로 어떤 파라미터를 식별 가능하게 하는가?"** 그리고 그 모든 비선형의 뿌리는 **표적이 살아있는 욕조**라는 것. PK27의 한 컷($K_m$ 0.03 vs 3.7, 약 123배)이 이 전부의 요약임.

---

## 자가점검 (풀고 답 보기)

**Q1 (★ 쉬움)** — 표적 기저량 식 $R_0=k_{syn}/k_{deg}$에서 $k_{syn}$과 $k_{deg}$의 단위는? 그리고 둘 중 어느 걸 바꿔야 "수위와 회복시간이 둘 다" 변하나?
<details><summary>답</summary>
$k_{syn}$ = 양/시간(예 µg/h), $k_{deg}$ = 1/시간(예 h⁻¹). **$k_{deg}$**를 바꾸면 수위($R_0$의 분모)와 회복시간($t_t=1/k_{deg}$)이 둘 다 변함. $k_{syn}$만 바꾸면 수위만 변함 [G&W pp.96–97].
</details>

**Q2 (★★ 중간)** — mAb가 18~24일이나 버티는 핵심 관문은 4개 중 무엇이고, 그 기전을 한 줄로?
<details><summary>답</summary>
**④ FcRn salvage.** 세포가 삼킨 항체를 산성 endosome에서 FcRn이 분해 직전 건져 순환으로 되돌림(재활용 트럭). FcRn 결합은 치료 농도에서 보통 비포화·pH 의존적임. R&T는 mAb 반감기가 IgG에 가까운 약 21일이라 함 [R&T pp.708–709].
</details>

**Q3 (★★ 중간)** — TMDD 곡선 Phase B의 "slow 1st order"를 "A→D로 갈수록 점점 느려짐"으로 읽으면 왜 틀리나?
<details><summary>답</summary>
Phase B는 **표적 경로가 포화돼 비특이 선형 제거가 지배**하는 영역으로, 절대 청소율로는 **Phase D보다 빠름**. 저농도 Phase D가 $k_{off}$·$k_{e(RL)}$ 주도로 더 느림. 농도 위계 ≠ 시간 위계임 [R&T p.712; G&W Fig.27.7].
</details>

**Q4 (★★ 중간)** — PK27에서 ligand만(I) → +target(II) → +complex(III)로 갈 때 $k_{e(RL)}$의 CV%는 어떻게 변했고, 왜 complex가 결정타인가?
<details><summary>답</summary>
**27 → 23 → 2.** target까지 재도 sink는 잘 안 좋아지다가(27→23), complex를 재는 순간 2로 급좋아짐. complex의 거동을 가장 직접 가르치는 게 complex 데이터라서임. "측정 안 한 종은 가정일 뿐"의 정량 증거 [G&W p.609].
</details>

**Q5 (★★★ 어려움)** — $K_d$, $K_{ss}$, $K_m$을 각각 분수식과 "어떤 가정에서 나오는지"로 구분하고, PK27의 $K_m$이 0.03 vs 3.7로 갈린 이유를 한 줄로?
<details><summary>답</summary>
$K_d=k_{off}/k_{on}$(순수 결합, sink 없음), $K_{ss}=(k_{off}+k_{e(RL)})/k_{on}$(complex QSS 가정), $K_m=(k_{off}+k_{e(RL)})/k_{on}$($L\gg R$ 추가로 $R_{tot}$ 잠김). $K_{ss}$·$K_m$은 같은 분수, 다른 가정. PK27의 0.03(Full) vs 3.7(MM, 약 123배)은 **근사 단계 차이** — MM이 저용량(표적 비포화)에서 $R_{tot}$ 변동을 못 추적해 구조 편향이 쌓인 흔적임 [G&W p.609; R&T pp.711–712]. (충돌이 아니라 단계 의존 값.)
</details>

**Q6 (★★ 중간)** — 팀이 "MM 모델 OFV 낮고 VPC 괜찮으니 first-in-human 저용량 외삽에 쓰자"고 함. 30초 답변은?
<details><summary>답</summary>
"MM은 **관찰된 용량 범위 안**에선 쓸 수 있음. 그런데 저용량 외삽은 **표적 점유율이 충분히 높게 유지되는지** 확인해야 함. PK27에선 고용량 적합이 양호해도 가장 낮은 곡선이 따로 놀았고 $K_m$이 0.03→3.7로 **123배** 부풀었음. 최소한 **dose-stratified 잔차, 예측 점유율, 저농도 sensitivity analysis**를 보고 결정하자." [G&W p.609]
</details>

---

## 검증 체크리스트 통과표 (A1~G)

| 항목 | ✅ | 근거 (1줄) |
|---|---|---|
| **A1** (앵커 전부 풀이·손실0) | ✅ | 살아있는 욕조·mAb 4관문·TMDD 비선형·4 phase·Full 4-state ODE·근사 사다리(Full/QSS/MM)·PK27 123배·soluble vs membrane·세 K 상수·ADA·점유 시뮬 전부 쉽게 풀어 포함 |
| **A2** (위계·인과 보존) | ✅ | 원인($k_{syn},k_{deg},Cl,k_{on}$) → 결과(반감기·phase·식별성) 사슬을 §1→§5 흐름으로 보존 |
| **A3** (이전·다음 연결) | ✅ | 선행 §05 2구획·§08 비선형 명시, 혼동쌍서 §11 욕조 호출, 다음 §13 IIV 메타블록·BSV서 연결 |
| **B1** (인용 txt 실제확인·placeholder 0) | ✅ | 123배·CV%(17→2→1 등)·0.04–0.23·29–44%·200/400h 등 전부 원문 대조, 리터럴 자리표시자 0개 |
| **B2** (범위 밖 플래그) | ✅ | QSS 유도식·membrane 추가 state·150kDa 림프%·규제 요건을 `[교과서 외]`/`[확인 필요]`로 표기 |
| **B3** (충돌 드러내고 정정) | ✅ | PK27 $K_m$ 0.03 vs 3.7을 "충돌 아니라 근사 단계별 값"으로 정직 서술 [G&W pp.602–610]; 18~24일 vs 21일 영역 정합 |
| **B4** (메타블록 약어풀이+쪽주의) | ✅ | G&W·R&T 첫머리 1회 풀이 + "쪽=원판 교재 기준" 1줄 명시 |
| **C1** (용어 즉시 괄호설명·점프0) | ✅ | TMDD·FcRn·ADA·CV%·NONMEM·MM·internalization·soluble 등 첫 등장 자리서 풀이 |
| **C2** (식 3단: 왜→기호→결론) | ✅ | 욕조식·target/complex ODE·QSS·MM 청소율 모두 ①왜②기호③결론 3단 |
| **C2-b** (식 연속 밀집 금지) | ✅ | target·complex 식 사이 "거울" 다리, QSS에 "회전문" 비유 삽입 |
| **C3** (새 개념마다 "왜 지금") | ✅ | 모든 섹션 머리에 동기 문단 + 다리문장 |
| **C3-b** (모든 섹션 🎯학습목표) | ✅ | §1~§5 전부 🎯 1줄 부착 (동기와 별도) |
| **C4** (비유 먼저→정의, 1:1 대응) | ✅ | 욕조(수도꼭지/배수구), 유도탄=약·기지=표적·동반폭발=internalization, 재활용 트럭=FcRn, 회전문=QSS, 고속도로/병목 |
| **C5** (1학년 선행 그 자리 보충) | ✅ | Michaelis-Menten·정상상태·MRT·구획·on-rate를 등장 자리서 보충 |
| **C6** (음슴체 일관) | ✅ | 전체 "~임/~함/~됨" 일관 |
| **C7** (혼동쌍 즉시정정) | ✅ | $k_{syn}$ vs $k_{deg}$(§1), $k_{on}LR$ vs $k_{syn}LR$(§4), $K_d/K_{ss}/K_m$(§4½·§5) 그 자리 정정 |
| **C8** (모든 수치에 비교 기준) | ✅ | $V_{ss}$ 0.04–0.23 vs 몸물 0.6; mAb Tmax 며칠 vs 소분자 분~시간; CV% 비교 등 |
| **D1** (핵심마다 숫자예시≥1) | ✅ | IgX·IgG·estradiol·somatropin·anakinra·adalimumab+MTX·PK26 set·PK27 CV%·123배 |
| **D2** (흔한실수·혼동쌍) | ✅ | baseline DV 처리, phantom linearity, 두 표기 혼용, MM 혼동표 |
| **D3** (도구 정의 먼저) | ✅ | NONMEM·CV%·MM·VPC/OFV 정의 후 사용 |
| **D4** (자가점검 3~5+답) | ✅ | Q1~Q6 + 접이식 답 |
| **E1** (척추 도입부 박스+매 섹션 호출) | ✅ | 도입 박스 선언 + §1~§5 각 동기/결론서 척추 호출 |
| **E2** (섹션 전환 다리문장) | ✅ | 각 섹션 머리 "왜 지금/다리", 결론 끝 다음 섹션 예고 |
| **E3** (도입 지도+말미 요약) | ✅ | "이 문서 한 장 지도" 표 + "한 줄 요약" |
| **E4** (자료 부족분 예고+출처+플래그) | ✅ | ADA를 §2서 예고→§4서 전개; QSS 식 범위밖 플래그 |
| **F1** (한국어·음슴체·MD) | ✅ | 전체 한국어 음슴체 Markdown |
| **F2** (LaTeX·표·ASCII) | ✅ | `$...$` 수식, 표 다수, NONMEM ASCII 블록 |
| **F3** (메타블록 6요소) | ✅ | 약어/대상="비전공·1학년 OK"/선행/범위/원천목록/쪽주의 6요소 |
| **G** (naive-reader 막힘 0) | ✅ | 갑작스런 왜·미설명 점프·빈 숫자·비유 미착지·깨진 §참조 0 (§ 교차참조 §1·§2·§3·§4·§4½·§5·§11·§13 전부 실제 절과 일치) |

# 세션 11 — Indirect Response: Turnover·DRT·Baseline · 쉬운판
## 같은 농도인데 효과가 따로 노는 모든 경우를, 한 질문으로 분해하기

---

## 0. 메타블록 — 읽기 전에 딱 30초만

> **출처 약어 풀이 (처음 한 번만 풀고 이후엔 약어로 씀)**
> - **G&W** = **Gabrielsson & Weiner**, *Pharmacokinetic and Pharmacodynamic Data Analysis* (약동·약력학 데이터 분석), **5판(5e)**. (이 세션의 `_G_` 추출텍스트)
> - **R&T** = **Rowland & Tozer**, *Clinical Pharmacokinetics and Pharmacodynamics* (임상 약동·약력학), **5판(5e)**. (이 세션의 `_T_` 추출텍스트, Chapter 8 "Response")
> - **쪽번호는 원판 교재 기준임.** 본문에 인쇄된 교재 쪽번호(예: 235, 247)를 우선 쓰고, 그게 안 보이면 `[파일명 PDF page N]`으로 적음.
>
> **대상**: 비전공자·대학 1학년도 OK. 약을 한 번도 안 배운 사람 기준으로 모든 용어를 그 자리에서 괄호로 풂.
>
> **선행지식**: 사실상 없음. "농도가 시간에 따라 변한다", "미분=변화율" 정도만 알면 됨. 더 필요한 건 나올 때마다 한 줄씩 보충함.
>
> **다루는 범위**: (1) 농도와 효과가 시간차로 어긋나는 현상(hysteresis) 진단 → (2) Turnover(턴오버=만들고 없애는 회전) 모델 4종 + 상류 pool 확장 → (3) NONMEM(논멤, 인구집단 약동학 분석 표준 소프트웨어) 돌리기 전 손으로 잠그는 추정 규율 → (4) 가역 turnover로 설명 안 되는 비가역 작용·표적 소비 → (5) 같은 곡선의 두 해석(turnover vs effect compartment) → (6) 어느 시계가 더 느린가로 임상 의사결정 번역 → (7) Baseline(기저값)이 움직이는 경우.
>
> **원천 자료 목록**:
> - 백본 노트: `11_indirect_response_remastered.md` (이 쉬운판이 100% 보존하는 원본)
> - `_pdf_text/011_G_Indirect Response Turnover·DRT·Baseline.txt` (G&W 5e §2.6.7, §3.7–3.12, PD4·PD5·PD6·PD7·PD9 사례)
> - `_pdf_text/011_T_Indirect Response Turnover·DRT·Baseline.txt` (R&T 5e Chapter 8 전체)
>
> **한 가지 정직한 메모(공유 출처)**: 이 주제의 R&T(`_T_`) 추출텍스트는 옆 세션들과 **같은 Chapter 8(단일 투여 후 노출-반응·시간지연)**임. 즉 R&T 본문은 여러 PKPD 세션의 공통 출처라서, R&T를 인용할 때는 "이건 이 챕터가 공통으로 깔아주는 사실"이라는 점을 의식하고 씀. 주제 고유의 깊은 내용은 G&W(`_G_`)와 백본 노트를 주 출처로 삼음.

---

## 1. 이 문서 한 장 지도 — 관통 척추 먼저 박기

이 세션 전체가 답하는 **단 하나의 질문**이 척추임:

> 🦴 **척추 질문**: *"plasma 농도(C)와 효과(effect)가 시간상 안 맞을 때, 그 어긋남(mismatch)은 어디서 오고, 그걸 어떻게 분해해서 임상 결정으로 번역하는가?"*

흐름은 이렇게 흘러감(5~8줄 미리보기):

1. 데이터 받으면 NONMEM부터 켜지 말고 **농도 vs 효과 그림(hysteresis loop)** 한 장을 그림. loop 방향이 후보를 좁혀줌.
2. 어긋남의 출처 후보는 딱 **4개**뿐임 → (분포 지연 / turnover / 표적 소비 / 더 느린 시계).
3. Turnover가 후보면 **욕조 비유**($R_0=k_{in}/k_{out}$)로 골격을 세우고, 약물이 들어갈 자리 **4칸**을 가려냄.
4. NONMEM 돌리기 전 **손으로 초기값을 잠그는 규율**(graphical estimation, blocking dose, DRT)을 익힘.
5. 가역 turnover로 안 되면 **비가역 kill·표적 소비**(아스피린·오메프라졸·항암제)로 넘어감.
6. 같은 곡선을 **두 구조(turnover vs effect compartment)**가 똑같이 그릴 수 있음을 인정하고, 데이터 밖 증거로 가름.
7. 마지막은 **"어느 시계가 더 느린가"** 하나로 duration 공식이 살거나 폐기됨.

> 💡 **이 세션을 한 문장으로**: 간접 반응 모델링은 "지연을 추가하는 일"이 아니라 **"올바른 인과 시계(causal clock)에 지연을 배정하는 일"**임. 그리고 베테랑은 *fit이 매끄럽다고* 좋아하지 않고, *어느 시계가 가장 느린지를 증명할 수 있을 때* 좋아함. 이 한 줄이 문서 끝까지 따라옴.

---

## 2. 임상에서 진짜 답답한 순간 — 동기부터

> 🎯 **이 섹션 끝내면**: 농도와 효과가 시간상 어긋나는 현상을 보고, 그 mismatch의 출처가 **딱 4가지뿐**임을 떠올려 어느 후보인지 좁히기 시작할 수 있게 됨.

> **[왜 지금 배우나]** 약을 줬는데 혈중 농도와 효과가 따로 노는 일은 예외가 아니라 일상임. 이걸 모르면 반감기만 보고 투약 간격을 정했다가 어떤 약에서는 완전히 빗나감.

일상 비유부터. **전기장판**을 생각해 봄. 스위치를 켜도 바로 안 따뜻하고, 끄고 나서도 한참 따뜻함. "스위치 위치(=약물 농도)"와 "이불 온도(=효과)"가 시간상 안 맞음. 약도 똑같음.

실제 사례 두 개로 감을 잡음:

- **Naproxen(나프록센, 비스테로이드 소염진통제=NSAID)** 500 mg을 입으로(경구) 치과 통증 환자한테 주면, **같은 혈장 농도라도 농도가 올라가는 중이냐 내려오는 중이냐에 따라 통증 완화가 다름** (1~8시간 관찰). 농도가 올라갈 땐 효과가 뒤처지고, 농도가 내려갈 때도 효과는 계속 올라가다가 5시간 지나서야 농도를 따라 내려옴 [R&T p.235, Fig 8-2].
- **Aspirin(아스피린)** 650 mg은 혈장에서 2시간이면 거의 사라짐(반감기 약 15분). 그런데 혈소판의 thromboxane B₂(트롬복산 B₂=혈소판 응집 촉진 물질) 억제 효과는 **며칠** 감 [R&T p.251, Fig 8-20].

이게 우연이 아님. → 그래서 **plasma half-life(혈장 반감기)만 보고 dose interval(투약 간격)을 정하면 어떤 약에서는 맞고 어떤 약에서는 완전히 빗나감.**

> 📖 **R&T p.234, Fig 8-1**: 더 극적인 예로, digoxin(디곡신=강심제)을 정맥주사(i.v. bolus=정맥 한 번에 주입)하면 **혈장 농도는 떨어지는데 심장 효과(좌심실 박출시간 지표)는 오히려 4시간 동안 올라감**. 농도가 낮을수록 효과가 크다는 황당한 관계가 보임. 진짜 이유는 디곡신이 심장 조직으로 천천히 분포해서 표적 수용체에 늦게 결합하기 때문임. 그래서 약 6시간 기다려 분포 평형이 잡힌 뒤에 농도를 효과의 지표로 써야 함.

**그래서 이 세션 전체는 도구상자임** — "C와 effect가 안 맞을 때, 그 mismatch는 어디서 오는가, 그리고 그걸 어떻게 분해해서 임상 의사결정으로 번역하는가?"

답이 될 수 있는 후보는 **단 4가지뿐**임. 이걸 머릿속에 박아두면 이번 세션이 전부 풀림.

| # | mismatch의 출처 | 쉬운 말로 | 모델 도구 | 대표 약물 |
|---|---|---|---|---|
| 1 | **분포 지연** | 약이 작용 부위(작용점)에 늦게 도착함 | Effect compartment(효과 구획), $k_{e0}$ | digoxin, naproxen(생체상 평형 지연) |
| 2 | **Turnover** | system이 반응을 만들고 없애는 데 시간이 걸림 | 4-Model(Model I~IV) + Pool/Precursor 확장 | Warfarin, Erythropoietin, methylprednisolone |
| 3 | **표적 소비** | 약이 표적을 영구 파괴, 새로 만들 때까지 효과 남음 | $K_{kill}$, 비가역 kill, regrowth(재성장) | Aspirin, Omeprazole, Paclitaxel |
| 4 | **다른 시계가 더 느림** | PK와 PD 중 느린 쪽이 효과 지속시간을 결정 | PK-clock vs PD-clock 감별 | Succinylcholine vs Warfarin |

> 용어 즉시 풀이: **PK**(pharmacokinetics, 약동학=몸이 약에 하는 일=흡수·분포·대사·배설, "농도가 시간에 따라 어떻게 변하나"), **PD**(pharmacodynamics, 약력학=약이 몸에 하는 일=효과, "농도가 효과를 어떻게 만드나"). **system**은 우리 몸의 생리 시스템(혈압·혈당·세포 수 같은 걸 만들고 없애는 장치)이라고 생각하면 됨.

이 표가 이번 세션의 전체 지도임. **베테랑 모델러는 데이터를 받자마자 첫 30초 안에 이 4개 후보 중 어느 쪽인지를 좁힘.** 그 다음에 NONMEM 돌리기 전에 손으로 어디까지 잠가놔야 하는지, fit이 매끄러워도 왜 결론을 미뤄야 하는지, duration(효과 지속시간) 예측 공식을 언제 쓰고 언제 버려야 하는지가 줄줄이 갈림.

> 🔑 한 줄 결론: 이 분야 베테랑은 **fit이 매끄럽다고 좋아하지 않음. 어느 시계가 가장 느린지를 증명할 수 있을 때 좋아함.** 이게 척추임.

> 🌉 **다리문장**: 그럼 그 첫 30초에 뭘 하느냐 → 종이 한 장에 그림을 그림. 그게 다음 절임.

---

# PART I — 진단의 첫 단추: 데이터를 받자마자 하는 일

## 3. Hysteresis 방향 — 30초 만에 가설 후보를 좁히는 도구

> 🎯 **이 섹션 끝내면**: 농도-반응 점을 시간순으로 이은 고리(loop)의 **방향(반시계/시계/없음)**만 보고 의심할 후보군을 즉시 가지치기하고, "loop가 안 보임=direct 확정"이 왜 틀린지 짚어낼 수 있게 됨.

> **[왜 지금 배우나]** 모델 적합(fitting)부터 들어가면 가짜 수렴에 속기 쉬움. 진짜 첫 단계는 "그림 한 장"이고, 그 그림의 모양이 4개 후보를 즉시 가지치기해 줌.

### A. Hysteresis가 뭐길래

학생들이 자주 빠지는 함정 하나. PK/PD 데이터를 받으면 곧장 model을 적합시키려고 NONMEM을 켬. **틀린 순서임.** 진짜 첫 단계는 종이 위에 한 개의 그림을 그리는 것임 — **plasma C(x축) vs response(y축)**, 점들을 **시간 순서대로** 잇기.

이게 hysteresis loop(히스테리시스 고리)임.

> 용어 풀이: **hysteresis(히스테리시스)** = 같은 약물 농도에서 **올라가는 길과 내려오는 길의 반응이 다른 현상**임 [R&T p.234]. C-R(농도-반응) 평면에 시간 순으로 점을 이으면 한 점에서 출발해 한 바퀴 도는 **고리(loop)**가 그려짐. **response(반응)**는 측정한 약리 효과(통증 완화, 혈압 변화, 세포 수 등).

일상 비유: **같은 산을 오르내리는 두 갈래 길의 고도 기록** 같은 거임. 같은 고도(=같은 농도)라도 올라가는 중인지 내려오는 중인지에 따라 몸 상태(=반응)가 다르면, 고도 하나로는 설명이 안 끝남. 비유-실제 대응: 고도=농도, 몸 상태=반응, 올라감/내려감=흡수기/소실기.

### B. loop 방향 3종 — 표로 외움

| 패턴 | 그림으로 | 해석 | 대표 사례 | 떠올릴 후보 |
|---|---|---|---|---|
| **반시계 방향 (counterclockwise)** | ↺ | 반응이 농도 뒤에서 따라옴 | **Naproxen** 500 mg 경구(NSAID; 진통제), 치과 통증, Fig 8-2 [R&T pp.234–235]; **Ibuprofen(이부프로펜)** 6 mg/kg 경구(NSAID; 해열·진통), 열나는 아이들, Fig 8-9 [R&T pp.241–242] | 분포 지연, turnover, 활성 대사체 |
| **Hysteresis 없음 (직접 link)** | • (loop 없이 한 줄) | 작용부위 평형·반응 생성이 sampling(채혈 간격)보다 훨씬 빠름 | **Midazolam(미다졸람)** 15 mg/kg 경구(쥐 EEG=뇌파; 진정제), Fig 8-6 [R&T p.239] | direct PK–PD link(직접 연결) |
| **시계 방향 (clockwise)** | ↻ | 내성, 피드백, 활성 대사체, 추가 동역학 | (이 세션 G&W 본문 중 **PD9 Zooparc® 정상상태 농도-반응 그림이 시계 방향** [G&W p.779, Fig 9.2]) — 본격 사례는 tolerance(내성) 장에서 | 내성, feedback(되먹임) |

> 용어 풀이: **활성 대사체(active metabolite)** = 약이 몸에서 변형되어 생긴, 그 자체로 효과를 내는 물질. 원래 약은 사라져도 대사체가 남아 효과를 끌면 농도-효과가 어긋남. **EEG**(electroencephalogram, 뇌파=뇌 전기활동 기록). **sampling**은 "몇 분/몇 시간마다 피를 뽑아 측정하느냐"의 간격.

> ⚠️ **충돌 정정 (현재 노트 vs 원문)**: 백본 노트는 시계 방향 칸에 "이 세션 본문에는 사례 없음"이라고 적었음. 그런데 **G&W PD9(Zooparc®)의 정상상태 농도-반응 그림(Fig 9.2, p.779)은 명시적으로 시계 방향(clockwise) hysteresis**임("Note the clockwise hysteresis at both dose levels"). 그래서 위 표에서 이 사실을 드러내 정정함. 다만 PD9의 본질은 turnover(Model 1) 모델이고, 정상상태 plot에서 보이는 시계 방향은 반복투여 정상상태에서의 시간순서 효과라서, "시계 방향=무조건 내성"으로 단정하면 안 됨(아래 D 참고).

### C. 첫 30초 진단의 세 줄 규칙

> 🔑 **30초 진단 규칙**
> ① **반시계 방향이면** → 분포 지연 / turnover / 활성 대사체부터 의심
> ② **시계 방향이면** → 내성 / 피드백부터 의심
> ③ **Loop가 안 보이면** → 그렇다고 direct(직접)가 확정은 아님. **sampling 해상도 안에서만 그렇다**는 뜻임

세 번째가 진짜 중요함. Hysteresis가 안 보인다고 모든 약이 direct response인 게 아님. **sampling 간격보다 지연이 짧으면 그냥 안 보일 뿐임.** 그래서 "직접 vs 지연" 판정은 model family(모델 계열)를 고르기 전에 **설계 해상도(design-resolution) 결정**으로 먼저 다뤄야 함. 지연이 sampling 척도에서 안 보이면, 생물학적으로 완전히 순간적이지 않더라도 direct link로 방어 가능함.

> 💡 G&W도 같은 말을 함 — *"all responses to be delayed in nature"* (모든 반응은 본질적으로 지연돼 있다고 본다), 다만 *"a matter of time and resolution of the data"*(시간 척도와 데이터 해상도의 문제)일 뿐이라고 [G&W p.236, p.252]. 즉 "직접이냐 지연이냐"는 절대 구분이 아니라 우리가 얼마나 촘촘히 봤느냐의 문제임.

### D. 숫자 예시 + 흔한 실수

- **숫자 예시(반시계)**: ibuprofen은 농도가 높은 초기엔 효과가 거의 없고, 농도가 15 mg/L까지 **떨어졌을 때 최대 효과**가 나옴 [R&T pp.241–242]. 농도 30 → 효과 작음, 농도 15(내려오는 중) → 효과 최대. 같은 15 mg/L라도 올라갈 때와 내려올 때 효과가 다름 → 반시계 loop.
- **흔한 실수 / 혼동쌍**: "loop가 안 보임 = direct 확정"으로 착각. → 틀림. 위 ③번. **"sampling 해상도 안에서 direct로 보인다"**가 정확한 표현임.
- **혼동쌍 2**: "시계 방향 = 무조건 내성". → PD9처럼 turnover 모델인데도 정상상태 plot이 시계 방향으로 보일 수 있음. 방향은 **첫 가설 분기**일 뿐, 확정 도구가 아님.

> 📖 **G&W p.235, Fig 3.33 / R&T p.235, Fig 8-2**: 직접 반응과 지연(hysteretic) 반응이 어떻게 다르게 그려지는지를 한눈에 보여줌. Fig 3.33은 왼쪽 열에 "농도 하나당 반응 하나"인 직접 반응을, 오른쪽 열에 고리가 생기는 지연 반응을 나란히 그려놓음. → 그래서 **농도 하나로 반응을 다 설명할 수 없다는 사실의 시각적 증명**임.

> 🌉 **다리문장**: 반시계 loop가 보였다고 치자. 이제 그 지연이 turnover에서 오는지 확인하는 도구를 만들어야 함. 4개 후보 중 가장 흔한 케이스라서 여기에 가장 공들임. → PART II.

---

# PART II — Turnover의 골격: mismatch 출처 #2를 분해하기

## 4. 욕조에서 출발하기 — $R_0 = k_{in}/k_{out}$

> 🎯 **이 섹션 끝내면**: baseline이 $k_{in}/k_{out}$ 균형점임을 욕조로 설명하고, NONMEM에서 $k_{in}\cdot k_{out}$을 따로 추정하려다 터지는 이유와 $(R_0,k_{out})$ 재모수화로 살리는 처방을 댈 수 있게 됨.

> **[왜 지금 배우나]** Turnover 모델을 이해하려면 먼저 "약이 없을 때 반응이 왜 일정한 값에 머무는가"부터 알아야 함. 그 일정한 값(baseline)이 사실은 두 속도의 균형이라는 게 모든 것의 출발점임.

### A. 가장 중요한 한 줄 — 욕조 비유

일상 비유: **욕조**. 수도꼭지가 일정 속도로 물을 넣고($k_{in}$), 배수구가 수위에 비례해서 물을 뺌($k_{out}\cdot R$). 그러면 어느 수위에서 들어오는 양과 빠지는 양이 똑같아지는 지점이 생김 — 그 수위가 **baseline(기저값) $R_0$**임. 비유-실제 대응: 수위=반응 $R$, 수도꼭지=생산속도 $k_{in}$, 배수구=소실 시계 $k_{out}$, 평형 수위=기저값 $R_0$.

Turnover 모델은 한 줄로 요약됨 — **response가 두 속도(생산·소실)의 균형 위에 떠 있다** [G&W pp.235–237; R&T pp.234, 239].

> **[수식: 왜 필요한가]** 반응이 시간에 따라 어떻게 변하는지(=변화율)를 식으로 적어야 약이 그 변화를 어디서 건드리는지 말할 수 있음.

$$
\underbrace{\frac{dR}{dt}}_{\text{반응의 변화율}}
=
\underbrace{k_{in}}_{\text{생산속도(수도꼭지)}}
-
\overbrace{\underbrace{k_{out}}_{\text{소실 clock(배수구 시계)}}\,\underbrace{R}_{\text{반응 pool(수위)}}}^{\text{pool에서 빠지는 양}}
\quad \text{[G\&W Eq 3:74; G\&W p.237]}
$$

기호 풀이: $dR/dt$는 "반응이 시간당 얼마나 변하나"(미분=변화율). $k_{in}$은 0차(zero-order) 생산속도 = 수위와 무관하게 일정하게 들어오는 양. $k_{out}\cdot R$은 1차(first-order) 소실 = 수위가 높을수록 더 많이 빠짐. **한 줄 결론: 변화율 = 들어오는 양 − 빠지는 양.**

> 용어 풀이: **0차(zero-order)** = 속도가 농도/수위와 **무관하게 일정**(수도꼭지를 일정하게 틀어둠). **1차(first-order)** = 속도가 현재 양에 **비례**(수위가 높을수록 빨리 빠짐). **pool**은 "고여 있는 양"이라고 생각하면 됨.

약이 없으면(정상상태=steady state, 변화율이 0) 들어오는 양과 빠지는 양이 같아짐:

$$
\underbrace{\frac{dR}{dt}=0}_{\text{정상상태}}
\;\Rightarrow\;
k_{in}=k_{out}R_0
\;\Rightarrow\;
\underbrace{R_0}_{\text{기저값}}
=
\frac{\underbrace{k_{in}}_{\text{생산}}}{\underbrace{k_{out}}_{\text{소실 clock}}}
\quad \text{[G\&W Eq 3:76; G\&W p.237]}
$$

**한 줄 결론: baseline은 독립 상수가 아니라 수도꼭지÷배수구의 균형점임.**

| 파라미터 | 단위 | 생물학적 의미 |
|---|---:|---|
| $R$ | response unit(반응 단위) | 측정된 약리학적 반응 |
| $k_{in}$ | response·time⁻¹ | 0차 생산 속도 |
| $k_{out}$ | time⁻¹ | 1차 소실 속도 = 회복 clock(회복 시계) |
| $R_0$ | response unit | 기저 반응 = $k_{in}/k_{out}$ |

> 💡 G&W가 직접 적어둠: 반응 변수 $R$은 매개물질(mediator), 신경전달물질(transmitter), 또는 심박수·혈압·행복감(euphoria) 같은 기능적 반응일 수 있고, **$R_0$는 시간 불변(time-invariant=시간이 지나도 안 변함)이라고 가정**함 [G&W p.237]. (이 "시간 불변" 가정이 뒤에서 깨지는 게 §13 Baseline 이야기로 이어짐.)

> 인과 위계 메모(거장 시점): **$k_{in}$·$k_{out}$이 원인(1차 파라미터)**이고, **$R_0$·반응 반감기는 결과(2차)**임. 마치 PK에서 CL(청소율)·V(분포용적)가 원인이고 $k$·$t_{1/2}$가 결과인 것과 똑같은 구조임. 이 위계를 거꾸로 잡으면 추정이 꼬임(바로 다음 B).

### B. 학생이 거의 100% 처음에 빠지는 함정 — Reparameterization(재모수화)

> 용어 풀이: **NONMEM(논멤)** = NONlinear Mixed-Effects Modeling의 약자. 여러 사람의 약물 농도·효과 데이터를 한꺼번에 분석해서 파라미터를 추정하는 **인구집단 약동·약력학 분석 표준 소프트웨어**임. "여러 환자 데이터를 넣으면 $k_{in}$, $k_{out}$ 같은 값을 자동으로 찾아주는 프로그램"이라고 보면 됨. **재모수화(reparameterization)** = 같은 모델을 추정하기 쉬운 다른 파라미터 조합으로 바꿔 쓰는 것.

NONMEM에서 $k_{in}$과 $k_{out}$을 **따로 추정**하려고 하면, 거의 항상 둘 중 하나가 일어남:

1. **correlation(상관계수)이 0.98을 넘어서** covariance matrix(공분산 행렬=추정 불확실성 표)가 망가짐
2. **OFV(objective function value, 목적함수값=모델이 데이터와 안 맞는 정도의 점수, 낮을수록 좋음)가 30번 반복(iteration) 동안 꼼짝 안 하다가 갑자기 뚝 떨어짐** (stuck-then-drop 패턴)

왜 그러냐면, $k_{in}$과 $k_{out}$의 **곱**은 $R_0$로 데이터가 강하게 잡아주는데, **두 값을 따로 분리할 정보가 데이터에 없기 때문**임. 일상 비유: **어두운 방에서 수도꼭지와 배수구를 동시에 만지며 수위를 맞추는 일**이랑 똑같음 — 수위(=곱)는 맞출 수 있어도 둘 중 뭘 얼마나 돌렸는지(=각각)는 알 수 없음.

> 용어 풀이: **비식별성(non-identifiability)** = 데이터만으로는 두 파라미터(또는 두 모델)를 구별해서 정할 수 없는 상태. 위 어두운 방이 딱 비식별성임.

**해결책은 단순함.** $R_0$와 $k_{out}$을 추정하고(둘 다 데이터에서 직접 읽힘), $k_{in}$은 곱으로 계산함:

$$
\underbrace{k_{in}}_{\text{생산}}
=
\underbrace{R_0}_{\text{기저값}}\cdot\underbrace{k_{out}}_{\text{소실 clock}}
$$

그러면 식은 이렇게 다시 써짐:

$$
\underbrace{\frac{dR}{dt}}_{\text{변화율}}
=
\underbrace{k_{out}}_{\text{회복 clock}}
\left(\underbrace{R_0-R}_{\text{기저-현재 거리}}\right)
\quad \text{[G\&W Eq 3:103; G\&W p.247]}
$$

기호 풀이: $R_0-R$은 "지금 수위가 평형 수위에서 얼마나 떨어져 있나". **한 줄 결론: 반응은 항상 기저값으로 돌아가려 하고, 그 복귀 속도는 $k_{out}$이 정함.** G&W도 같은 이유를 댐 — *"both $R_0$ and $k_{out}$ can be directly estimated from the data whereas $k_{in}$ has to be estimated indirectly"* (R₀와 kout은 데이터에서 직접 추정되지만 kin은 간접적으로만 추정됨), 그래서 $(R_0, k_{out})$로 쓰면 둘 사이 상관이 줄어든다고 명시함 [G&W p.247].

**숫자 예시 (PD4 warfarin 사례, 실측)**: 백본 노트가 인용한 Pool 1(=Model 3) 사례를 원문으로 검증함. (여기서 **Pool**=상류 전구체를 둔 모델로 §7에서 상술하고, **Model 3·4**=곧 §5에서 정리할 4모델(생산억제 I~소실촉진 IV)의 3·4번임 — 로마숫자 Model I~IV와 아라비아 Model 3·4가 같은 분류임. 지금은 '약이 생성 쪽을 건드린 경우'로만 읽으면 됨.) $k_1$과 $k_{out}$을 따로 추정했더니 **상관계수 0.9999, CV%(추정 변동계수=불확실성, 클수록 못 믿음) 무려 4000%**가 나옴. 같은 데이터에 **$k_1=k_{out}$ 제약**을 건 Pool 2(=Model 4)의 "정상 CV%(7%)"는 **데이터가 동등성을 지지한 게 아니라 제약이 비식별성을 해결한 것**임 [G&W PD4, Table 4.1, pp.749–752].

> 🔑 **NONMEM 출력 진단 처방**: 30번 반복 동안 stuck-then-drop 패턴이 보이면, 곧장 `$THETA`(NONMEM에서 추정할 파라미터를 적는 블록)를 $(R_0, k_{out})$로 재코딩함. 별다른 진단 없이도 90% 이상 살려내는 표준 처방임.

> **흔한 실수**: Pool 1처럼 CV%가 4000%로 터졌는데도 "모델이 수렴했으니 OK"라고 넘어감. → CV%가 수백~수천%면 그 파라미터는 사실상 추정 안 된 거임. 제약을 걸거나 재모수화해야 함.

### C. Baseline이 움직일 수도 있음 (예고편)

$k_{out}$이 시간 불변이라는 게 기본 가정인데, 실제로는 system 상태에 따라 움직일 수 있음. 이게 §13에서 본격적으로 다룰 **moderator/feedback(조절자/되먹임) 모델**의 입구임. 여기서는 식 구조만 미리 봄(자세한 풀이는 §13).

$$
\underbrace{\frac{dR}{dt}}_{\text{response 변화}}
=
\overbrace{\underbrace{k_{in}}_{\text{생산}}\,\underbrace{H(C)}_{\text{약물 함수}}}^{\text{약물이 조절한 생산}}
-
\underbrace{k_{out}\,M}_{\text{moderator가 끄는 소실}}
\quad \text{[G\&W Eq 2:261; p.110]}
$$

$$
\underbrace{\frac{dM}{dt}}_{\text{moderator 변화}}
=
\overbrace{\underbrace{k_{tol}\,R}_{\text{R이 만든 moderator}}
-\underbrace{k_{tol}\,M}_{\text{moderator 1차 소실}}}^{\text{tolerance pool 회전}}
\quad \text{[G\&W Eq 2:262; p.111]}
$$

여기서 $H(C)$는 약물이 생산을 켜거나 끄는 함수, $M$은 moderator(조절자=반응을 다시 억누르는 되먹임 물질), $k_{tol}$은 moderator의 생산·소실을 정하는 1차 속도상수임.

> 🌉 **다리문장**: Baseline이 잡혔으니, 이제 약물이 그 균형을 **어디서** 깨는지 봐야 함. 자리는 딱 4개뿐임. → 다음 절.

---

## 5. 약물이 들어갈 자리는 딱 4개 — 4-Model Taxonomy(4모델 분류)

> 🎯 **이 섹션 끝내면**: 약물이 욕조의 input·output 중 어디를 건드리느냐로 Model I~IV를 분류하고, "반응 방향만 보고 모델을 확정하면 안 되는" 이유를 ODE로 설명할 수 있게 됨.

> **[왜 지금 배우나]** "반응이 떨어지니까 생산 억제 약이지" 같은 짐작은 자주 틀림. 약물 함수가 input(생산)에 붙는지 output(소실)에 붙는지가 진짜 분류 기준이고, 이걸 알아야 시간 패턴으로 모델을 가려낼 수 있음.

### A. 욕조에서 약이 손댈 수 있는 곳은 4군데

수도꼭지를 **잠그기 / 더 열기**, 배수구를 **막기 / 더 열기**. 끝. 그리고 잠그는 함수 $I(C)$와 여는 함수 $S(C)$의 형태는 이렇게 생김.

> **[수식: 왜 필요한가]** 약물 농도 $C$가 생산이나 소실을 "몇 % 줄이거나 늘리는지"를 농도의 함수로 적어야, 농도가 변할 때 반응이 어떻게 따라가는지 계산할 수 있음.

$$
\underbrace{I(C)}_{\text{남은 생산 활성(0~1)}}
=
1-
\underbrace{\frac{\overbrace{I_{max}\,C^n}^{\text{억제 구동}}}{\underbrace{IC_{50}^n}_{\text{절반 농도}^n}+\underbrace{C^n}_{\text{농도}^n}}}_{\text{억제된 분율}},
\quad 0\le I_{max}\le 1
\quad \text{[G\&W Eq 3:77; p.237]}
$$

$$
\underbrace{S(C)}_{\text{촉진 배율(1 이상)}}
=
1+
\underbrace{\frac{\overbrace{E_{max}\,C^n}^{\text{촉진 구동}}}{\underbrace{EC_{50}^n}_{\text{절반 농도}^n}+\underbrace{C^n}_{\text{농도}^n}}}_{\text{촉진된 분율}}
\quad \text{[G\&W Eq 3:78; p.237]}
$$

기호 풀이:
- $I_{max}$ = 최대 억제 분율(0~1). 1이면 100% 차단 가능, 0.5면 절반까지만 차단.
- $E_{max}$ = 최대 촉진 효과(배율의 추가분). $E_{max}=4$면 최대 5배까지 촉진.
- $IC_{50}$/$EC_{50}$ = 최대 효과의 **절반**을 내는 농도(potency=효력의 척도, 작을수록 강한 약).
- $n$ = sigmoidicity(시그모이드 가파름=Hill 계수). 클수록 농도에 따라 효과가 가파르게 켜짐/꺼짐.
- $C$ = 약물 농도.

**한 줄 결론**: $C$가 0이면 $I(C)=1$(생산 그대로), $S(C)=1$(배율 1=변화 없음). 농도가 올라가면 $I(C)$는 0쪽으로(생산 차단), $S(C)$는 위로(촉진) 감.

> 💡 G&W는 $I(C)$, $S(C)$가 위 형태 말고도 여러 형태(완전/부분 억제, 무한 자극, 선형, 로그형 등)를 가질 수 있다고 표로 정리함 [G&W p.246, Table 3.4]. 즉 위 두 식은 **가장 흔한 형태**일 뿐, 유일한 형태는 아님.

### B. 4개 모델 — 한 표로 외움

| Model | ODE(미분방정식) | 작용 자리 | $t_{ss}$(정상상태 도달시간) 거동 | $R_{ss}$ | 최대 $\Delta R$ | 임상 prototype(원형) |
|---|---|---|---|---|---|---|
| **I** 생산 억제 | $\dot R = k_{in}I(C) - k_{out}R$ | 수도꼭지 잠금 | $k_{out}$ 지배, **용량 독립** | $R_0\,I(C_{ss})$ | $R_0\,I_{max}$ | **Warfarin**(비타민 K 순환 억제) [G&W PD4 pp.742–752] |
| **II** 소실 억제 | $\dot R = k_{in} - k_{out}R\,I(C)$ | 배수구 막음 | 유효 $k_{out}\!\cdot\!I(C)$, **용량 의존** | $R_0/I(C_{ss})$ | $R_0\,I_{max}/(1\!-\!I_{max})$ | **Furosemide(푸로세미드)**-형 (요중 수분 재흡수 억제) [G&W p.238] |
| **III** 생산 촉진 | $\dot R = k_{in}S(C) - k_{out}R$ | 수도꼭지 더 엶 | $k_{out}$ 지배, **용량 독립** | $R_0\,S(C_{ss})$ | $R_0\,E_{max}$ | **Erythropoietin(에리트로포이에틴=적혈구 생성 촉진 호르몬, EPO)** (적혈구 생산 자극) [G&W p.238] |
| **IV** 소실 촉진 | $\dot R = k_{in} - k_{out}R\,S(C)$ | 배수구 더 엶 | 유효 $k_{out}\!\cdot\!S(C)$, **용량 의존** | $R_0/S(C_{ss})$ | $R_0\,E_{max}/(1\!+\!E_{max})$ | **CB1 inverse agonist**(에너지 소비 촉진) [G&W p.238]; PD7 compound A [G&W pp.764–769] |

> 용어 풀이: **ODE**(ordinary differential equation, 상미분방정식=변화율을 적은 식). $\dot R$은 $dR/dt$의 줄임 표기(점 하나=시간 미분). **$t_{ss}$**(time to steady state)=새 평형에 도달하는 데 걸리는 시간. **$R_{ss}$**(response at steady state)=약물 하에서의 새 평형 반응. **$\Delta R$**=기저값에서의 변화량. **prototype**=그 모델의 대표 약물(교과서 단골 예).

> ⚠️ **충돌 정정 (현재 노트 vs 원문)**: 백본 노트는 Model IV의 prototype을 "PD7 compound C"라고 적었음. 그런데 **G&W PD7 본문은 "compound A" 같은 별명을 쓰지 않고 그냥 "a new chemical/compound"라고만 부름**(PD4·PD5의 "compound A"와 혼동한 것으로 보임). 여기서는 안전하게 **"PD7의 화합물(loss 촉진, Model 4)"**로 적음 [G&W pp.764–769]. 표에는 표기 일관성을 위해 "compound A"라 두되 이 정정 메모를 명시함. (PD7 final: $k_{in}=27$, $k_{out}=0.92\ h^{-1}$, $SC_{50}=50$, $S_{max}=4.5$, 반응 반감기 약 54분.)

ODE를 같은 자리에 모아두면 패턴이 보임 — **약이 input에 붙으면 $S(C)$/$I(C)$가 $k_{in}$ 옆에, output에 붙으면 $k_{out}$ 옆에** 붙음:

$$
\begin{aligned}
\text{Model I: }&\frac{dR}{dt}=\overbrace{k_{in}I(C)}^{\text{input 억제}}-\underbrace{k_{out}R}_{\text{loss 그대로}}\\
\text{Model II: }&\frac{dR}{dt}=\underbrace{k_{in}}_{\text{input 그대로}}-\overbrace{k_{out}RI(C)}^{\text{loss 억제}}\\
\text{Model III: }&\frac{dR}{dt}=\overbrace{k_{in}S(C)}^{\text{input 촉진}}-\underbrace{k_{out}R}_{\text{loss 그대로}}\\
\text{Model IV: }&\frac{dR}{dt}=\underbrace{k_{in}}_{\text{input 그대로}}-\overbrace{k_{out}RS(C)}^{\text{loss 촉진}}
\end{aligned}
$$

**정상상태 값도 패턴이 있음**: input을 건드리면 $R_{ss}=R_0\times(\text{함수})$ (곱), output을 건드리면 $R_{ss}=R_0\div(\text{함수})$ (나눗셈). 예를 들어 Model I은 $R_{ss}=R_0 I(C_{ss})$ — 생산이 절반 차단되면 정상상태 반응도 절반. Model II는 $R_{ss}=R_0/I(C_{ss})$ — 소실이 절반 차단되면 반응이 2배로 쌓임 [G&W Eq 3:80~3:101, pp.238–245].

### C. 학생이 가장 자주 헷갈리는 한 가지

> ⚠️ **반응 방향만으로 모델을 결정하지 말 것 (혼동쌍 핵심)**
> "반응이 떨어지니까 Model I(생산 억제)지" — 틀림. **Model IV(loss 촉진)도 baseline 아래로 갈 수 있음.** 반응이 떨어진다고 input 차단이 확정되는 게 아님. 반대로 반응이 올라가는 것도 Model II(loss 억제)일 수도, Model III(생산 촉진)일 수도 있음. → **시간 경과 패턴 + $t_{ss}$의 용량 의존성**을 같이 봐야 함(다음 §6).
> G&W도 PD5/PD7에서 같은 경고를 함: 사전 기전 정보가 없으면 "반응 상승"을 만드는 모델이 **두 개**(loss 억제 vs 생산 촉진), "반응 하강"을 만드는 모델도 **두 개**(생산 억제 vs loss 촉진)라서 헷갈린다고 [G&W p.757, p.768].

### D. Model II의 숨겨진 폭탄 — $I_{max}\to1$ 발산

Model II의 최대 변화량은 분모에 $(1-I_{max})$가 있음. $I_{max}$가 1에 가까워지면 **무한대로 발산함**:

$$
\underbrace{\Delta R_{M2,\text{max}}}_{\text{M2 최대 변화}}
=
\frac{\underbrace{R_0}_{\text{기저값}}\,\overbrace{I_{max}}^{\to\,1}}{\underbrace{1-I_{max}}_{\to\,0}}
\;\xrightarrow[I_{max}\to 1]{}\;
\overbrace{\infty}^{\text{발산}}
\quad \text{[G\&W Eq 3:89; p.242]}
$$

수학 호기심이 아니라 임상적 의미가 있음: **소실 경로가 완전히 차단되면 $k_{in}$이 계속 들어오는데 빠질 길이 없어서 pool이 무한히 쌓임.** 욕조에서 배수구를 완전히 막으면 결국 흘러넘침. → 그래서 PPI(proton pump inhibitor, 양성자펌프 억제제=위산 분비 억제제)에 의한 위 $H^+$ 축적, loop diuretic(고리 이뇨제) 차단 시 체액 정체, COX(cyclooxygenase, 사이클로옥시게나제=프로스타글란딘 생성 효소) 억제 시 일부 prostanoid(프로스타노이드=염증 매개물질) 축적 등 **고용량에서 포화·독성이 생기는 구조적 이유**가 여기 있음.

**Model IV는 반대로 $E_{max}\to\infty$여도 $R_0$에서 멈춤** — $\Delta R_{M4,\text{max}}=R_0\,E_{max}/(1+E_{max})$인데 분모가 분자랑 같이 자라서, 아무리 크게 촉진해도 반응은 0(=$R_0$에서 $R_0$만큼 빠진 값)으로만 수렴함 [G&W Eq 3:101, p.245]. **두 모델의 경계 거동이 비대칭이라는 게 핵심 차이임** (II는 위로 무한, IV는 아래로 0에서 멈춤).

> 🔑 **실무 신호**: 모델 적합 중 $I_{max}$가 1에 매우 가깝게 수렴하면 ⓐ misspecification(모델 잘못 고름) 신호이거나 ⓑ 포화 임계 진입 신호임. 어느 쪽이든 cross-check(교차 확인) 필수.

> 🌉 **다리문장**: 그럼 4칸 중 어느 칸인지 어떻게 가리나? 핵심 단서는 **시간**임 — 정상상태 도달시간($t_{ss}$)이 용량에 따라 변하느냐 아니냐. → 다음 절.

---

## 6. 시간 신호로 4칸 가려내기 — $t_{ss}$와 peak shift

> 🎯 **이 섹션 끝내면**: 정상상태 도달시간($t_{ss}$)의 용량 의존성으로 생산측(I/III)과 소실측(II/IV)을 갈라내고, 초기 기울기를 $k_{out}$으로 외삽하는 흔한 실수(mirror-slope artifact)를 잡아낼 수 있게 됨.

> **[왜 지금 배우나]** 정상상태 값($R_{ss}$)만 보면 input형과 output형이 안 갈림. 그런데 "정상상태에 도달하는 데 걸리는 시간"이 용량에 따라 변하는지를 보면 두 묶음으로 갈라짐.

### A. 한 줄 규칙

일상 비유: $t_{ss}$는 **공항 보안검색의 금속탐지기**임 — 경고음(=용량에 따른 $t_{ss}$ 변화)이 울리면 어디를 더 봐야 할지 알려주지만, 그것만으로 물건 정체가 결정되진 않음.

| 관찰 | 1차 가설 | 주의 |
|---|---|---|
| 용량 간 **비슷한** $t_{ss}$ | 생산 측 (Model I or III) | PK가 더 느리면(rate-limiting) 그렇게 보일 수도 |
| 용량에 따라 $t_{ss}$ **단축/연장** | 소실 측 (Model II or IV) | PK가 PD clock보다 빠를 때만 성립 |
| 용량 증가에도 peak shift(최대반응 시점 이동) 없음 | **Effect compartment 증명 아님** | PD9가 이 과대해석을 직접 경고 [G&W pp.778–783] |

왜 이렇게 갈리나: **Models I/III**에서는 소실 항이 $k_{out}\cdot R$로 그대로라서 시간상수(= 얼마나 빨리 새 평형에 가나)가 $1/k_{out}$로 **용량과 무관**. 마치 1차 동역학 약물에서 주입속도를 바꿔도 정상상태 농도만 바뀌고 도달 시간은 안 바뀌는 것과 같음. **Models II/IV**에서는 약이 소실 항($k_{out}$)을 건드리니 유효 시간상수가 농도(=용량)에 따라 변함. 마치 청소율(clearance)을 바꾸면 정상상태 농도와 도달 시간이 둘 다 바뀌는 것과 같음 [G&W pp.248–249].

**숫자 예시 (PD7, loss 촉진=Model IV)**: 6,400 / 32,000 / 160,000 unit를 4시간 주입했더니, 저용량은 약 2시간, 고용량은 1시간 안에 정상상태 도달 — **용량이 클수록 $t_{ss}$가 짧아짐**. 이게 loss 촉진(Model IV)의 시그너처임. 반대로 PD6/PD9(생산 쪽)에서는 용량이 달라도 peak 시점이 거의 같음 [G&W p.766, p.781].

### B. 학생이 가장 자주 잘못 하는 것 — Early slope(초기 기울기)에서 $k_{out}$ 외삽

PD7 Fig 7.1을 보면 명확함. 초기 기울기로 읽은 **겉보기 $k_{out}$이 용량에 따라 0.6~1.6 $h^{-1}$ 범위로 단조 변함**(저용량 쪽 약 0.6, 고용량 쪽 약 1.6) [G&W p.765]. 같은 약, 다른 용량인데 system 파라미터가 용량 따라 변하는 것처럼 보임. **이건 system biology가 아니라 misspecification artifact(모델 잘못 고른 데서 생긴 인공물)임** [G&W p.251 일반 논의, PD7 데이터].

이유는 단순함. Models II/IV에서는 약물이 loss 항을 건드리니 effective time constant(유효 시간상수)가 농도에 따라 달라짐. **이 모델을 Model I/III처럼 다루면서 초기 기울기를 그대로 $k_{out}$으로 읽으면 용량별로 다른 답이 나옴.** 정확히는 그 초기 기울기가 $k_{out}\cdot S(C)$(또는 $k_{out}\cdot I(C)$)라서 농도가 끼어든 값임.

> ⚠️ **충돌 정정 (현재 노트 vs 원문)**: 백본 노트는 "6,400 unit → 0.6, 160,000 unit → 1.6"으로 **개별 용량에 기울기를 1:1로 못박았음.** 원문(G&W p.765, Fig 7.1)은 *"the initial slopes give the apparent fractional turnover rates of 0.6 – 1.6 h⁻¹"*라고 **범위로만** 적음(어느 용량이 정확히 어느 값인지는 그림에서 읽는 근사임). 의미(겉보기 $k_{out}$이 용량 따라 단조 변함)는 그대로지만, "정확히 6400→0.6, 160000→1.6"은 근사 해석임을 밝혀둠.

> 🔑 **Mirror-slope(거울 기울기) 시그너처**: system 파라미터(원래 약물과 무관해야 함)가 용량에 따라 단조롭게 변하면, biology가 아니라 misspecification임. → "약을 바꾼 것도 아닌데 system 시계가 용량 따라 변한다? 그럼 내가 모델을 잘못 골랐다"가 기본 반응이어야 함.

### C. $t_{ss}$를 결정적 증거로 과대해석하지 말기

$t_{ss}$ 하나로 결판내지 말고, 다음 보조 근거 중 **최소 하나**가 있어야 함:

| 보조 도구 | 무엇을 확인 |
|---|---|
| 넓은 dose range(용량 범위) | 좁은 범위에선 숨는 비선형 $H(C)$ 거동을 드러냄 |
| 반복 투여 / washout(약물 제거 후 회복 관찰) | system recovery clock(회복 시계)을 직접 봄 |
| Mechanism prior(기전 사전지식) | 생산 vs 소실은 $t_{ss}$만으로는 결판 안 남 |
| PK clock 확인 | PK가 더 느리면 PD clock 진단이 가려짐 |

> 🌉 **다리문장**: 지금까지는 약이 건드리는 자리와 우리가 보는 반응이 한 단계로 붙어 있었음(단일 stage). 그런데 실제 생물학은 사이에 **상류 pool**이 하나 더 있는 경우가 많음. → 다음 절.

---

## 7. Cascade가 끼면 — Pool/Precursor 확장 (Sharma-Jusko 1998)

> 🎯 **이 섹션 끝내면**: 상류 pool이 끼는 2단계 cascade 구조를 알아보고, sigmoid onset(lag 후 상승)이 보이는데 single-stage로 적합하면 $k_{out}$이 cascade 깊이를 흡수해 작게 나오는 시그너처를 짚어낼 수 있게 됨.

> **[왜 지금 배우나]** 스테로이드처럼 약이 직접 건드리는 곳(상류)과 우리가 재는 반응(하류) 사이에 중간 단계가 있으면, 단일 stage 모델로 적합했을 때 $k_{out}$이 엉뚱하게 작게 나옴. 그 함정을 피하려고 배움.

### A. 2단계 cascade(연쇄)의 구조

일상 비유: **공장 → 창고 → 매장** 2단계. 약이 공장(precursor=전구체)을 건드리면, 그 변화가 창고를 거쳐 매장(우리가 보는 반응)까지 오는 데 두 단계의 시간이 걸림. 비유-실제: precursor pool $P$=중간 창고, response $R$=매장 진열량, $k_p$=창고→매장 전환 시계.

> 용어 풀이: **precursor(전구체)** = 최종 반응 물질이 되기 전 단계의 물질(예: mRNA → 효소). **cascade(캐스케이드)** = 단계가 줄줄이 이어진 연쇄. **Corticosteroid(코르티코스테로이드=부신피질호르몬)**가 mRNA를 만들고 그게 효소를 만드는 식.

$$
\underbrace{\frac{dP}{dt}}_{\text{precursor 변화}}
=
\underbrace{k_{in}}_{\text{0차 생산}}
-
\overbrace{\underbrace{k_p}_{\text{전환 clock}}\,\underbrace{P}_{\text{precursor pool}}}^{\text{R로 넘어가며 빠지는 양}}
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

**한 줄 결론**: response의 기저값($R_0$)은 단일 stage와 똑같지만(여전히 $k_{in}/k_{out}$), **거기 도달하는 동역학은 두 시계 $k_p$와 $k_{out}$의 cascade**라서 더 느리고 모양이 다름.

### B. 약물 작용 자리 확장 — 관행적 Models V~VIII

상류(precursor)에서도 약이 생산을 억제/촉진하거나, 전환을 억제/촉진할 수 있음 → 4가지가 더 생김:

| Model (관행) | 약물 작용 자리 | ODE 변화 | 사례 |
|---|---|---|---|
| **V** | precursor 생산 억제 | $dP/dt = k_{in}\cdot I(C) - k_p P$ | corticosteroid → TAT mRNA (타이로신 아미노전이효소 mRNA) |
| **VI** | precursor 생산 촉진 | $dP/dt = k_{in}\cdot S(C) - k_p P$ | EPO precursor 자극 |
| **VII** | precursor → response 전환 억제 | $dR/dt = k_p P\cdot I(C) - k_{out} R$ | 효소 활성화 차단 |
| **VIII** | precursor → response 전환 촉진 | $dR/dt = k_p P\cdot S(C) - k_{out} R$ | maturation(성숙) 가속 |

> 📖 **명명법 출처 정정 (정직 플래그)**: Sharma & Jusko (1998, *Br J Clin Pharmacol* 45:229–239) **원 논문은 'Model V/VI/VII/VIII' 번호를 명시적으로 부여하지 않음.** "precursor compartment(전구체 구획)를 가진 간접반응 모델"로 서술함. **V~VIII 번호는 후속 표준 문헌(Jusko 그룹 후속 review, Mager-Wyska-Jusko 교과서 등)의 관행임.** 학습자가 원 논문을 펴서 'Model V'를 찾으면 그 표기가 없으니 헷갈리지 않게 해둠. (이 1차 문헌은 제공된 .txt 범위 **밖**이라 [교과서 외] 표기이며, 백본 노트의 출처 기록을 그대로 보존함.)

### C. Single-stage와의 본질적 차이

| 비교 기준 | Single-stage Model I (생산 억제) | Pool/Precursor Model V (상류 생산 억제) |
|---|---|---|
| 약물 작용 후 첫 효과까지 | $\sim 1/k_{out}$ | $\sim 1/k_p + 1/k_{out}$ (cascade lag=연쇄 지연) |
| Onset(시작) 곡선 모양 | exponential approach(지수적 접근) | **sigmoid 모양** (초기 평탄 구간 = lag) |
| 약물 중단 후 회복 | $1/k_{out}$ 단일 clock | 두 clock의 deconvolution(분리) 필요 |
| $k_{out}$ 단독 추정 | 종말 회복 기울기로 가능 | $k_p$와 함께 안 하면 cascade depth(연쇄 깊이)를 흡수 |

> 🔑 **Sigmoid onset 시그너처**: Pool/precursor 약물은 **투약 직후 바로 효과가 안 나오고 lag-then-rise(잠깐 멈췄다 올라감)** 패턴을 보임. 이게 보이는데 single-stage Model I로 적합하면 추정된 $k_{out}$이 **biology가 아니라 cascade depth($1/k_p$)의 일부를 흡수함.** → 임상에서 **"측정된 $k_{out}$이 알려진 효소 반감기보다 작게 나온다"**가 cascade misspecification의 시그너처임.

> 💼 **실무 인사이트**: Corticosteroid 약리(prednisolone → tyrosine aminotransferase=타이로신 아미노전이효소; methylprednisolone → lymphocyte trafficking=림프구 이동 등)의 **표준 PD 골격이 바로 Pool/Precursor**임. Single-stage Model I로 적합하면 effect onset(효과 시작)이 실제보다 너무 빠르게 나옴.

> 🌉 **다리문장**: 여기서 자주 나오는 헷갈림 하나 — 모델마다 $E_{max}$, $I_{max}$라는 같은 이름을 쓰는데, **그 숫자의 뜻이 모델 구조마다 다름.** 이걸 짚지 않으면 비교가 다 어긋남. → 다음 절.

---

## 8. $I_{max}/E_{max}$는 같은 이름이지만 같은 뜻이 아님

> 🎯 **이 섹션 끝내면**: 같은 $E_{max}$ 숫자가 모델 구조마다 절대거리·배율·turnover배율로 뜻이 달라짐을 알고, 비교할 땐 $\Delta R/R_0$로 변환해야 함을, "선형 PK ≠ 선형 PD"와 함께 판단할 수 있게 됨.

> **[왜 지금 배우나]** 논문이나 보고서에서 "$E_{max}=0.65$" 같은 숫자를 비교할 때, 모델 구조를 모르면 그 비교가 무의미함. 같은 "10"이라도 cm인지 층수인지 모르면 못 비교하는 것과 같음.

### A. 효과 크기 파라미터의 의미는 모델 구조마다 다름

$E_{max}=0.65$라는 숫자를 봤다고 가정함. 모델 구조 없이는 뜻이 안 정해짐. **세 가지 가능성**이 있음 [G&W p.246, Fig 3.40]:

| 모델 형태 | 식 | $E_{max}$의 의미 |
|---|---|---|
| Direct additive(직접·덧셈형) | $E=E_0+\frac{E_{max}C^n}{EC_{50}^n+C^n}$ | response 단위의 **절대 거리**(예: 혈압 −20 mmHg) |
| Direct multiplier(직접·곱셈형) | $E=E_0(1+\frac{E_{max}C^n}{EC_{50}^n+C^n})$ | **무차원 배율**(예: 기저의 1.65배) |
| Turnover Model III | $R_{ss}=R_0(1+\frac{E_{max}C^n}{EC_{50}^n+C^n})$ | **system turnover를 통한 배율**(약물 효력×기저값) |

일상 비유: 같은 "높이 10"이라도 **센티미터인지 층수인지** 모르면 비교 불가능함. $E_{max}$도 어떤 축 위의 거리인지 먼저 봐야 함. G&W도 못박음 — direct $E_{max}$는 *"a combination of drug (affinity, efficacy) and system specific (kin, kout) parameters"* (약물 특성과 system 특성이 섞인 값)이라서 모델마다 의미가 다르다고 [G&W p.247].

$$
\underbrace{E}_{\text{관찰효과}}
=
\underbrace{E_0}_{\text{기저효과}}
+
\underbrace{\frac{E_{max}C^n}{EC_{50}^n+C^n}}_{\text{절대 효과(덧셈)}}
\qquad
\underbrace{E}_{\text{관찰효과}}
=
\underbrace{E_0}_{\text{기저효과}}
\left(1+
\underbrace{\frac{E_{max}C^n}{EC_{50}^n+C^n}}_{\text{배율 효과(곱)}}
\right)
$$

$$
\underbrace{R_{ss}}_{\text{약물 정상상태}}
=
\underbrace{R_0}_{\text{system 기저값}}
\left(1+
\underbrace{\frac{E_{max}C^n}{EC_{50}^n+C^n}}_{\text{turnover 통한 배율}}
\right)
$$

**한 줄 결론**: 세 식의 $E_{max}$는 각각 절대거리·배율·turnover배율이라 **서로 다른 단위/의미**임.

> 🔑 **비교 규칙**: 모델 / 연구 / 화합물 간 효과 파라미터를 비교할 땐 항상 **$\Delta R/R_0$(기저 대비 변화 비율)**로 변환한 뒤 비교함. raw(가공 안 한) $E_{max}$ 숫자 비교는 거의 항상 무의미함.

### B. 선형 PK가 선형 PD를 의미하지 않음 — Methylprednisolone

> **[왜 지금 배우나]** "용량 2배 → 농도 2배 → 효과도 2배"라는 착각이 임상에서 흔함. 이게 왜 틀리는지를 실제 데이터로 봄.

**Methylprednisolone(메틸프레드니솔론=부신피질호르몬; 정맥 phosphate-prodrug 형태)**에서 **16 / 31 / 63 / 125 / 250 / 500 / 1000 mg** 7개 용량을 줌. 혈장 AUC(area under the curve, 농도-시간 곡선 아래 넓이=총 노출)는 용량에 **거의 정확히 비례**해서 늘어남(용량 2배면 농도 2배). 그런데 **lymphocyte(림프구) 반응은 비례하지 않음** — 고용량(특히 500, 1000 mg)에서는 반응 차이를 거의 알아보기 어려울 만큼 plateau(고원=더 안 올라가는 천장)에 가까워짐 [R&T pp.256–258, Fig 8-25~8-27].

R&T 본문(p.256)이 단호하게 못박음 — *"Dose linearity in pharmacokinetics does not result in dose linearity in pharmacodynamics. That is almost never the case."* (약동학의 용량 선형성이 약력학의 용량 선형성으로 이어지지 않는다. 거의 절대 그렇지 않다.)

또 다른 disconnect(분리) 사례. **Rosuvastatin(로수바스타틴=HMG-CoA 환원효소 억제제=콜레스테롤 합성 차단 고지혈증약)**의 **OATP1B1**(간 흡수 수송체=약을 간으로 퍼올리는 단백질) 유전다형성은 혈장 AUC를 **substantially(상당히, TC형 +63%, CC형 +111%)** 바꾸는데 **콜레스테롤 합성 반응은 거의 안 변함(3.1%, 5.8% 감소)** (Fig 8-28/8-29). 이유는 작용 부위(간)의 농도로 효과가 결정되기 때문 — **전신 노출 ≠ 작용 부위 노출**의 보조 사례임 [R&T pp.258–259]. 그래서 **bioequivalence(생물학적 동등성=두 제제의 혈중 노출이 같음)가 효과 동등성을 보장하지 않는** 메커니즘으로 자주 인용됨.

> ⚠️ **흔한 실수**: "용량 비례적 노출 → 용량 비례적 반응"이라는 결론을 쓰기 전에 **Hill curve(힐 곡선=S자 농도-효과 곡선)의 어느 영역에 있는지 먼저 확인**함. plateau에 들어가면 농도를 2배 해도 효과는 거의 안 늘어남.

> 📖 **G&W p.246, Fig 3.40**: 같은 파라미터 이름($E_{max}$)이 모델 계열마다 같은 수직 반응 거리를 의미하지 않는다는 것을 그림으로 보여줌(왼쪽=직접 Emax, 가운데=배율형, 오른쪽=turnover Model 3).

> 🌉 **다리문장**: 여기까지가 "무엇을 모델링하나"였음. 이제 "어떻게 신중하게 추정하나"로 넘어감 — NONMEM 돌리기 전에 손으로 잠가야 할 것들. → PART III.

---

# PART III — Estimation Discipline: NONMEM 돌리기 전 손으로 잠가야 할 것들

## 9. Graphical Initial Estimation + Blocking Dose — 사실은 기전 감사임

> 🎯 **이 섹션 끝내면**: 그래프에서 $R_0$·$k_{out}$·$k_{in}$ 초기값을 손으로 잡는 5단계를 수행하고, blocking dose(차단 용량)와 DRT(농도 없을 때)로 $k_{out}$·합성속도를 뽑아내는 방법을 골라 쓸 수 있게 됨.

> **[왜 지금 배우나]** 초기값을 대충 넣으면 optimizer(최적화기=값을 자동으로 찾아주는 부분)가 비식별성 골짜기에서 가짜 수렴을 내놔도 못 알아챔. 손으로 초기값을 잡는 건 향수가 아니라 첫 번째 기전 점검임.

### A. 왜 손으로 잡아야 하는가

학생들이 흔히 graphical estimation(그래프로 초기값 잡기)을 "NONMEM 시대 이전의 향수"라고 무시함. 틀림. **이건 첫 번째 mechanism audit(기전 감사)임.** 초기값을 단순 guess(짐작)로 두면 optimizer가 비식별성 골짜기에서 가짜 수렴을 내놔도 알아채기 어려움 [G&W pp.247–251]. G&W도 강력 권고함 — *"We highly recommend that the analyst invest some time in manual derivation of the initial parameter estimates."* (분석자가 초기 파라미터를 손으로 유도하는 데 시간을 투자할 것을 강력히 권한다), 특히 약력학에서 흔한 고도 비선형 모델에서 보람이 크다고 [G&W p.251].

### B. 5단계 작업 흐름

| 단계 | 어디서 읽는가 | 산출물 |
|---|---|---|
| 1 | pre-dose baseline(투약 전 기저 구간) | $R_0$ |
| 2 | 종말 회복 곡선의 log-linear(반로그) 기울기 (또는 합성 차단 구간) | $k_{out}$ |
| 3 | 1번 × 2번 | $k_{in} = R_0 \cdot k_{out}$ |
| 4 | 2~3개 용량 수준의 정상상태 또는 peak 반응 | $IC_{50}/EC_{50}$, $I_{max}/E_{max}$의 자릿수 |
| 5 | 위 값이 다 sanity(상식) 통과한 후 | NONMEM 추정 시작 |

**숫자 예시 (PD5 사례, 실측)**: Compound A(화합물 A)의 PK가 먼저 잡힌 상태($V=40\;\text{L}$, $K=0.9\;h^{-1}$)에서 **4,000 / 16,000 / 80,000 unit**의 6시간 정맥 주입 데이터를 받음. ① pre-infusion baseline에서 $R_0$(약 45 units)를 읽고, ② post-infusion 회복 곡선의 semi-log(반로그) plot 종말 기울기로 $k_{out}$를 잡고, ③ $k_{in}=R_0\cdot k_{out}$로 production rate 출발점(초기 추정 19)을 잡음. ④ 세 용량의 정상상태에서 $IC_{50}$, $I_{max}$의 자릿수(초기 $IC_{50}\approx30$, $I_{max}\approx0.25$)를 잡은 뒤에 NONMEM 들어감. **최종 추정**: $k_{in}=19$, $k_{out}=0.43\;h^{-1}$, $IC_{50}=95$, $I_{max}=0.65$ (Table 5.1) [G&W PD5, pp.753–757].

> ⚠️ **충돌 정정 (현재 노트 vs 원문)**: 백본 노트는 PD5에서 "$k_{out}\approx0.43\;h^{-1}$"를 **graphical(초기) 단계 산출물**처럼 적었음. 원문을 보면 PD5의 **초기** $k_{out}$ 추정은 0.5이고, **0.43은 NONMEM 최종 추정값**임(Table 5.1) [G&W p.757]. 즉 0.43은 손으로 읽은 값이 아니라 최종값임. 숫자 자체는 맞으니 "이게 초기값이냐 최종값이냐"만 정정함. (PD5는 **Model 2 = inhibition of loss=소실 억제** 사례이고, 사전 기전 정보가 없으면 "loss 억제(I·kout)" vs "생산 촉진(S·kin)"이 헷갈린다고 원문이 명시함 [G&W p.757].)

> ⚠️ **흔한 실수**: 적합값이 graphical 자릿수에서 **한 자릿수(order) 이상** 벗어나면 **비식별성이나 misspecification이 작동 중**이라는 신호임. Random effects(개인차 항)를 늘리기 전에 출발점의 생물학을 먼저 수정함. (참고로 PD4에서는 일부러 $k_{out}$ 초기값을 진짜 값의 10배로 틀리게 넣어도 프로그램이 회복하는 걸 보여줬지만 [G&W p.746], 이건 "초기값이 틀려도 된다"가 아니라 "robust한 알고리즘 시연"임.)

### C. Blocking Dose(차단 용량) — Warfarin의 임상 등가 방법

> **[왜 지금 배우나]** $k_{out}$을 깔끔하게 뽑는 가장 강력한 방법은 "생산을 거의 완전히 막아놓고, 남은 게 빠지는 속도만 보는" 것임. Warfarin이 이걸 임상에서 실제로 할 수 있는 약임.

> 용어 풀이: **Warfarin(와파린=경구 항응고제=피 굳는 걸 막는 약)**. 효과는 **prothrombin complex activity(PCA, 프로트롬빈 복합체 활성=혈액 응고인자들의 활성)**로 측정. 응고인자(II, VII, IX, X)는 끊임없이 만들어지고 분해됨(turnover).

일상 비유: **공장 입구를 거의 완전히 막아놓고 창고가 비는 속도를 재는 실험**과 같음 — 들어오는 물량을 잠그면 순수하게 배출 시계($k_{out}$)만 드러남.

합성이 거의 완전히 차단되면, 응고인자 활성 $A$는 1차로 빠짐:

$$
\underbrace{\frac{dA}{dt}}_{\text{활성 변화}}
=-\underbrace{k_t}_{\text{소실 clock}}\,\underbrace{A}_{\text{잔여 활성}}
\quad \text{[R\&T Eq 8-6의 차단 상태; R\&T pp.244–247]}
$$

기호 풀이: $k_t$는 응고인자의 degradation rate constant(분해 속도상수=$k_{out}$에 해당). 차단 상태에서 활성의 **반로그 plot이 직선**이 되고, 그 기울기가 $-k_t$임. **숫자 예시**: warfarin 1.5 mg/kg 경구를 주면 처음 48시간 PCA가 지수적으로 감소하고, 더 높은 용량을 줘도 36시간 시점 잔여 활성으로 본 감소 속도는 더 안 빨라짐(=이미 완전 차단) [R&T p.247, Fig 8-15].

차단이 풀린 구간에서는 합성 속도를 거꾸로 재구성함:

$$
\underbrace{R_{syn}}_{\text{합성속도}}
=
\underbrace{\frac{A_2-A_1}{\Delta t}}_{\text{관찰된 변화}}
+
\overbrace{\underbrace{k_t}_{\text{소실 clock}}\frac{\underbrace{A_1+A_2}_{\text{구간 평균 활성}}}{2}}^{\text{소실 보정}}
\quad \text{[R\&T Eq 8-7; R\&T p.247]}
$$

기호 풀이: $A_1$, $A_2$는 시간 구간 양 끝의 활성, $\Delta t$는 구간 길이. **한 줄 결론**: "겉보기 변화(왼쪽) + 그 사이 빠져나간 양(오른쪽) = 진짜 만들어진 양". 이렇게 구한 합성 억제율을 농도의 로그에 대해 그리면 **hysteresis 없는 깔끔한 농도-효과(graded response) 곡선**이 드러남 [R&T p.247, Fig 8-16]. 이게 hysteretic한 반응-시간 기록을 **억제-농도 관계로 변환**하는 방법임.

> 💡 임상 활용: 이렇게 직접 효과 관계를 분리하면, 약효가 변했을 때 그게 **PK 변화(약물 청소율↑)** 때문인지 **system 반응성 변화** 때문인지 가를 수 있음. 예: warfarin + heptabarbital(헵타바르비탈=효소 유도제) 병용 시 효과 감소는 **순전히 청소율 증가** 때문이고 직접 효과 관계는 안 변함 [R&T p.247, Fig 8-16]. → 그래서 warfarin이 **합성 억제(Model I) 기전의 임상 prototype**으로 자주 인용됨.

### D. DRT (Dose-Response-Time) — 농도 데이터가 아예 없을 때

> **[왜 지금 배우나]** 안약·흡입제·국소제처럼 혈중 농도를 못 재거나 의미 없는 경우가 있음. 그래도 "반응-시간" 곡선만 있으면 약물 동역학을 일부 건질 수 있음.

> 용어 풀이: **DRT(Dose-Response-Time) 모델** = 농도(C) 데이터 없이 **용량(Dose)–반응(Response)–시간(Time)**만으로 baseline, slope(기울기), potency(효력), maximal effect(최대 효과)를 추론하는 방법. **biophase(생체상)** = 약이 실제로 작용하는 부위(혈장과 다를 수 있음), 그 부위의 약물량을 $A_b$로 씀.

DRT는 농도 데이터가 없어도 추론하는 방법인데, **full PK/PD 모델링보다 거친 역문제(inverse problem=결과에서 원인을 거꾸로 푸는 문제)임.** G&W가 던지는 핵심 질문 — *"can any useful information... be obtained when only effect versus time data are available?"* (효과-시간 데이터만 있을 때 약물의 동역학/약력학 정보를 건질 수 있는가?) → 좋은(또는 최적에 가까운) 설계가 있으면 가능하다고 [G&W p.272].

DRT가 분해하려는 3덩어리 [G&W p.272, Fig 3.60]:
- **biophase kinetics**: $K$(소실), $K_a$(흡수), $F^*$(biophase 가용성) → 약이 작용 부위에 들어오고 빠지는 속도
- **response turnover**: $k_{in}$, $k_{out}$ → system이 반응을 만들고 없애는 속도
- **약력학 결정자**: potency $ED_{50}/ID_{50}$, efficacy $E_{max}/I_{max}$ → 약물 자체의 세기

**숫자 예시 1 (안과 miotic data, 고양이 모델)**: 새 프로스타글란딘(prostaglandin=안압 낮추는 물질)을 **0.1 / 1.0 / 10 µg** 세 용량으로 결막강에 점안하고 **miotic response(동공 수축 반응)**만 측정함. biophase 동역학을 1차 입력/출력 + lag-time(지연시간) 모델(Eq 3:148)로, 약력학을 inhibitory sigmoid $I_{max}$ 모델(Eq 3:149)로 두고 **반응-시간 데이터에만 동시 적합**해서 $K_a$, $t_{lag}$, $K$ 같은 biophase 동역학을 추정함. 단, 이게 성립하려면 **(가)hysteresis 없음(한 $A_b$당 한 반응), (나)측정 효과가 $A_b$와 순간 평형, (다)$E_0$가 시간에 안 변함(stationarity), (라)활성 화합물이 하나만 존재**라는 조건이 필요함 [G&W pp.273–275, PD25].

**숫자 예시 2 (locomotor activity, 쥐 dexamphetamine)**: dexamphetamine(덱스암페타민=중추 흥분제)을 **두 용량(3.12, 5.62 µg/kg)** 복강내 투여하고 행동활성 점수를 측정. **상승·하강 둘 다 데이터 해상도가 좋고 용량에 따른 뚜렷한 peak-shift**가 있어서 DRT에 적합함. 흥미롭게도 **peak 이후 직선 감소의 기울기가 용량·투여경로와 무관**했음 [G&W pp.274–275, Fig 3.64~3.65; 원자료는 R&T Fig 8-7과 동일 출처 Van Rossum].

> 🔑 **DRT 사용 규칙**: **노출(농도) 데이터가 있으면 DRT로 대체하지 말 것.** DRT는 농도를 못 잴 때의 후퇴 대안 또는 교육적 가교로만 둠 [G&W pp.272–275]. (다만 어떤 약은 임상 endpoint=바이오마커가 PK보다 생동성 평가에 더 적합할 수 있다고 G&W가 덧붙임 [G&W p.273].)

> 🌉 **다리문장**: 지금까지는 전부 **가역(reversible) turnover** — system이 계속 만들고 없애서 결국 baseline으로 돌아오는 경우였음. 그런데 약이 표적을 **영구히** 부수면? 약이 사라져도 효과가 남음. → PART IV.

---

# PART IV — Turnover로는 안 되는 경우들

## 10. drug=0인데 effect≠0 — 비가역 작용과 표적 소비

> 🎯 **이 섹션 끝내면**: "drug=0이면 effect=0인가?"의 답이 NO인 약(아스피린·오메프라졸·항암제)을 알아보고, 비가역 kill(2차 상수·누적 AUC)에선 plasma 반감기가 아니라 표적 교체 시계로 duration을 잡아야 함을 판단할 수 있게 됨.

> **[왜 지금 배우나]** 아스피린·오메프라졸·항암제는 혈중에서 금방 사라지는데 효과는 며칠~몇 주 감. 가역 turnover로는 절대 설명 안 됨. "약이 사라지면 효과도 사라지나?"의 답이 NO인 경우를 따로 배워야 함.

### A. "drug=0이면 effect=0인가?"라는 질문 하나

가역적 turnover에서는 system이 반응을 계속 생산·제거하니까 baseline으로 돌아옴. 그런데 **약물 노출 기간 동안 반응 단위·표적·세포가 영구적으로 제거된 경우**는 다름. 약물이 사라져도 효과가 남음 [G&W pp.256–260; R&T pp.251–252].

일상 비유: 가역은 **스위치를 끄는 것**(다시 켜면 불 들어옴), 비가역은 **전구를 빼내는 것** — 전기가 다시 들어와도 새 전구를 끼우기 전까지 빛은 안 돌아옴. 비유-실제: 전구=표적/세포, 전구 빼기=비가역 파괴, 새 전구 끼우기=재합성/재성장.

핵심 식 (세포 죽이기, cell killing):

> **[수식: 왜 필요한가]** 가역 turnover와 달리, 소실이 약물 농도에 비례해서 **표적을 영구히 깎는** 항으로 적어야 "약 없으면 안 깎임"을 표현할 수 있음.

$$
\underbrace{\frac{dR}{dt}}_{\text{생존량 변화}}
=
-\overbrace{\underbrace{K}_{\text{kill 속도상수}}\,\underbrace{C}_{\text{노출}}\,\underbrace{R}_{\text{잔여 pool}}}^{\text{비가역 kill (2차)}}
\quad \text{[G\&W Eq 3:110; p.257]}
$$

기호 풀이: $K$는 죽이는 속도상수, $C$는 약물 농도, $R$은 남은 세포(표적) 수. **약이 0이면($C=0$) 통째로 0** = 더 안 죽음. 이게 가역 모델($-k_{out}R$, 약이 없어도 빠짐)과의 결정적 차이임.

적분(쌓아서 푼) 형태 — **생존 분율(SF)**:

$$
\underbrace{SF}_{\text{생존 분율}}
=
\exp\left(-\overbrace{\underbrace{K}_{\text{kill 속도상수}}\cdot\underbrace{AUC}_{\text{누적 노출}}}^{\text{누적 kill}}
\right)
\quad \text{[G\&W Eq 3:112; p.257]}
$$

기호 풀이: $AUC$는 농도-시간 곡선 아래 넓이(=총 노출, dose와 청소율 Cl의 함수). **한 줄 결론: 얼마나 죽느냐는 순간 농도가 아니라 누적 노출(AUC)이 정함.** 그래서 효과가 약이 사라진 뒤에도 "지나간 AUC"로 남음.

> ⚠️ **혼동쌍 핵심**: $K$(이 자료에서 $K_{kill}$ 또는 $k_k$로도 표기)는 **2차(second-order) 약리작용 상수**임. **1차 PK 소실 상수($K_{elim}$)가 아님.** G&W가 명시함 — 비가역 모델에서 *"kout now becomes a second-order rate constant"* (kout이 이제 2차 속도상수가 된다), 약물이 0이면 소실 속도도 0이라고 [G&W p.256, Fig 3.47]. 즉 같은 기호라도 가역에선 1차, 비가역에선 2차임. **PK 청소 상수랑 절대 헷갈리지 말 것.**

> 💡 참고 (출처 정직 메모): 백본 노트는 kill 상수를 일관되게 $K_{kill}$로 씀. **G&W 원문은 식에서 그냥 $K$(또는 §3.8.2 이후 $k_k$)로 표기**하고 "the rate constant of bacterial killing"이라 부름. 의미는 동일하니 $K_{kill}=K=k_k$로 보면 됨.

### B. 임상 prototype 3개 — 외워야 함

| 약물 | PK | PD | duration 결정자 |
|---|---|---|---|
| **Aspirin** 650 mg 경구 (NSAID; 항혈소판; COX-1 비가역 acetylation=아세틸화로 효소 영구 차단) | 짧은 혈장 반감기(~15분, 2시간이면 거의 소실) | thromboxane B₂ 억제 **수일 지속** | 혈소판 표적 교체 시계(새 혈소판 생성, 느림) [R&T p.251, Fig 8-20] |
| **Omeprazole** 40 mg 경구 (PPI; H⁺/K⁺-ATPase=양성자펌프 비가역 결합) | 혈장 반감기 <1 h(3시간이면 거의 소실) | 위산 분비 억제 **수일 지속** | proton pump 재생 시계 + 매우 단단한 결합의 느린 해리 [R&T p.252, Fig 8-21] |
| **Paclitaxel(파클리탁셀)** i.v. (taxane=택산계; 미세소관 안정화 항암제) | 혈장 농도 빠르게 감소(2일이면 거의 소실) | 백혈구(leukocyte) 회복 **약 3주** | leukocyte regrowth(백혈구 재성장) — 골수의 성숙 백혈구 재생 (Fig 8-22) [R&T pp.253–254] |

> 💡 omeprazole의 디테일(R&T p.252): 단순히 "표적 비가역 결합"만으로는 관찰된 패턴이 다 설명 안 되고, **국소에서 생긴 omeprazole 유도체가 펌프에 극도로 단단히 붙어 아주 천천히 해리**되는 것도 한몫함. 혈장 농도는 빨리 측정한계 아래로 떨어져서 "약이 없는데 효과가 남는 것처럼" 보이지만 실제로는 작용 부위에 남아 작동 중임.

> 🔑 **Duration 질문 규칙**: **"drug=0이면 effect=0인가?"**의 답이 **NO**이면, plasma PK 외에 **target replacement clock(표적 교체 시계)을 별도로 모델링**함. plasma 반감기로 duration을 계산하면 안 됨.

### C. 세포 성장과 함께 — 박테리아 kill/growth + MIC

> **[왜 지금 배우나]** 항생제처럼 약이 세포를 죽이는 동시에 세포가 다시 자라는 경우엔, kill과 growth(성장)를 같이 적어야 함. 이게 비가역 작용의 가장 흔한 응용임.

세포가 1차로 자라면서($\mu R$ 또는 $k_g N$) 동시에 약이 죽이는($-KCR$) 경우 [G&W §3.8.2, pp.258–260]:

$$
\underbrace{\frac{dN}{dt}}_{\text{세포수 변화}}
=
\overbrace{\underbrace{k_g}_{\text{1차 성장}}\,N\,\underbrace{\left(1-\frac{N}{B_{max}}\right)}_{\text{성장 한계(자리 부족)}}}^{\text{logistic 성장}}
-
\underbrace{k_k\,N\,f(C)}_{\text{2차 약물 kill}}
\quad \text{[G\&W Eq 3:117; p.259]}
$$

기호 풀이: $N$=세포 수, $k_g$=1차 성장 속도상수, $B_{max}$=최대 세포 수(영양·자리의 천장), $1-N/B_{max}$=세포가 $B_{max}$에 가까워지면 성장이 멈추는 되먹임(이 항이 붙은 성장 모양을 **logistic(로지스틱, S자 성장곡선)**이라 부름), $k_k$=2차 kill 상수, $f(C)$=약물 함수. **한 줄 결론: 관찰되는 곡선은 "자라는 힘 − 죽이는 힘"의 줄다리기임.** 초기 하강(kill 우세) → 종말 상승(growth 우세, $B_{max}$로 수렴)으로 나타남.

> 💡 **숫자 예시 + 도구 이름**: G&W Fig 3.49에서 박테리아 수가 약 **30,000(=$B_{max}$)**에서 평평해짐. growth 없는 단순 kill 모델(상위 모델)은 **DRECKER 모델**(Jusko 1971)이라 부름 [G&W p.257, Fig 3.48]. **MIC(minimum inhibitory concentration, 최소 억제 농도=세균 성장을 막는 최소 약물 농도)**도 이 kill/growth 균형식에서 나옴 — kill과 growth가 정확히 비기는 농도가 MIC 근처임 [G&W §3.8.3, p.260].

### D. 모든 도구가 한 자리에 모이는 응용 — Friberg-Karlsson 항암제 호중구감소 모델

> **[왜 지금 배우나]** Paclitaxel 백혈구 회복(약 3주)을 한 줄로 짚었는데, 실제 임상에서 항암제 골수억제(myelosuppression)의 **현대 표준 골격**은 한 단계 더 정교함. 그리고 이 모델 하나가 이번 세션의 거의 모든 도구를 한 자리에 결합함.

> 정직 플래그: **Friberg-Karlsson 모델은 제공된 .txt(_G_·_T_) 범위 밖의 1차 문헌**임(R&T Fig 8-22는 paclitaxel 백혈구 데이터만 보여주고 이 모델식은 안 실음). 백본 노트의 깊이 보존을 위해 그대로 가져오되, **[교과서 외, 1차 문헌 Friberg et al. 2002]**로 표기함.

> 용어 풀이: **호중구(neutrophil)** = 백혈구의 한 종류(세균 방어). **myelosuppression(골수억제)** = 항암제가 골수를 눌러 혈구 수가 떨어지는 부작용. **nadir(나디르)** = 수치가 가장 낮게 떨어지는 바닥점.

**구조**: 5개 compartment cascade — 증식 pool $Prol$ → transit 1 → transit 2 → transit 3 → 순환 pool $Circ$. 약물은 $Prol$에서 세포를 죽이고, $Circ$(순환 호중구)의 감소가 다시 $Prol$의 증식을 자극(feedback=되먹임)함 [Friberg et al., *J Clin Oncol* 2002].

$$
\underbrace{\frac{dProl}{dt}}_{\text{증식 변화}}
=
\overbrace{\underbrace{k_{prol}\,Prol}_{\text{1차 증식}}\,\underbrace{\bigl[1-E_{drug}(C_p)\bigr]}_{\text{약물 kill 보정}}\,
\underbrace{\left(\tfrac{Circ_0}{Circ}\right)^{\gamma}}_{\text{feedback 보정}}}^{\text{순 증식 — 약물×되먹임}}
-
\underbrace{k_{tr}\,Prol}_{\text{성숙으로 유출}}
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
\underbrace{\frac{dCirc}{dt}}_{\text{순환 호중구 변화}}
=
\underbrace{k_{tr}\,T_3}_{\text{성숙 세포 유입}}
-
\underbrace{k_{circ}\,Circ}_{\text{1차 소실}}
\quad \text{[Friberg \& Karlsson 2002 Eq 1–3]}
$$

기호 풀이: $Prol$=증식 중인 전구세포, $T_1$~$T_3$=성숙 중간단계, $Circ$=혈중 순환 호중구, $Circ_0$=그 기저값, $E_{drug}(C_p)$=혈중 농도에 따른 약물 효과(kill), $\gamma$(감마)=feedback 세기, $k_{tr}$=단계 간 전이 속도. **한 줄 결론: 약이 증식을 누르면 → 며칠 뒤 순환 호중구가 바닥(nadir) → 그 바닥이 증식을 다시 자극(rebound=반동 회복).**

> ⚠️ **모델 구조 제약 — 절대로 임의 고정 아님**
> 원 논문은 식별성 확보를 위해 다음 제약을 **모델 정의의 일부**로 도입함:
>
> $$
> \overbrace{\underbrace{k_{prol}}_{\text{증식}}=\underbrace{k_{tr,1}}_{\text{transit 1}}=\underbrace{k_{tr,2}}_{\text{transit 2}}=\underbrace{k_{tr,3}}_{\text{transit 3}}=\underbrace{k_{circ}}_{\text{순환 소실}}\equiv k_{tr}}^{\text{모델 정의에 의한 5중 제약}}
> \;\Longrightarrow\;
> \underbrace{MTT}_{\text{mean transit time}}=\underbrace{\frac{n+1}{k_{tr}}=\frac{4}{k_{tr}}}_{n=3\;\text{transit 단계}}
> $$
>
> 용어 풀이: **MTT**(mean transit time, 평균 통과시간) = 전구세포가 증식 pool에서 순환까지 오는 데 걸리는 평균 시간. 이 제약이 약물 간 system parameter 일관성($MTT$, $\gamma$가 약물에 거의 무관)의 정량적 기반임. 학생이 이걸 "흔한 관행"으로 오해해서 NONMEM에서 $k_{prol}$, $k_{tr}$, $k_{circ}$를 **독립 추정**하려 하면 **심각한 비식별성과 과대추정**에 빠짐. **원 논문 그대로 적용할 때만 약물 간 일관성이 회수됨.**

이 모델이 가르치는 것을 한 줄로 꿰면, **이번 세션 + Ch.12(transit chain 세션)의 모든 도구가 한 곳에 모임**:

- **§4 (Turnover 골격)** → $Circ_0$가 baseline pool로 등장, feedback이 "$k_{out}$ 고정" 가정을 위반함
- **§5 (4-Model)** → 약물이 증식 항에 곱해지는 구조는 확장된 Model VII/VIII 패턴
- **§7 (Pool/Precursor)** → 증식 pool → transit → 순환은 3단계 이상 cascade
- **§10 자체 (비가역 kill)** → 약물이 $Prol$에서 세포를 비가역적으로 죽임
- **Ch.12 (transit chain)** → 4-stage cascade가 $MTT=4/k_{tr}$로 환산
- **§12 (PK vs PD clock)** → paclitaxel PK 반감기는 짧지만 $MTT$(약 7일)가 회복을 지배

> 💼 **임상적 활용**: 단일 fit으로 호중구감소의 **nadir 시점, nadir 깊이, 회복 시점**을 모두 예측하고, dose-intensity(용량 강도) / dose-density(용량 밀도) 결정(예: dose-dense AC-T 항암 프로토콜)의 정량 근거가 됨. Docetaxel, paclitaxel, etoposide, 5-FU, vinflunine 등에서 **$\gamma$, $MTT$가 약물 간 일관성**을 보임 — system parameter는 약물에 거의 무관, drug parameter만 약물별로 다름.

> 🔑 **임상 시그너처**: Friberg-Karlsson 적합에서 보통 $MTT\approx100$~$140$시간(약 4~6일), $\gamma\approx0.1$~$0.3$이 호중구 표준 범위. 적합값이 이 범위를 크게 벗어나면 ⓐ 동반약물 효과, ⓑ 골수 기능 이상, ⓒ misspecification을 먼저 의심.

> ⚠️ **적용 범위**: Friberg-Karlsson은 **세포독성 항암제**의 myelosuppression 전용임. 표적치료제, 면역항암제는 작용 기전이 달라 그대로 안 됨. **Lenalidomide(레날리도마이드)의 호중구감소** 같은 경우는 이 골격을 변형해서 써야 함.

> 🌉 **다리문장**: 여기까지 "어떤 구조를 쓰나"를 익혔음. 그런데 이 세션의 정점은 따로 있음 — **같은 곡선을 두 구조가 똑같이 그릴 수 있다**는 위기. → PART V.

---

# PART V — APEX(정점): 같은 곡선, 두 가지 인과 해석

## 11. Turnover vs Effect Compartment — 데이터만으로 결판 안 나는 위기

> 🎯 **이 섹션 끝내면**: "효과-시간 곡선이 매끄럽게 잘 맞았다"는 것만으로는 **지연의 정체(turnover냐 분포 지연이냐)를 절대 못 정한다**는 걸 알고, 둘을 가르려면 무슨 추가 증거가 필요한지 댈 수 있게 됨.

> **[왜 지금 배우나]** 이게 이 세션의 정점임. 지금까지 turnover 모델을 열심히 세웠는데, 알고 보니 **완전히 다른 구조(effect compartment=효과 구획, 분포 지연)가 똑같은 곡선을 그릴 수 있음.** 이걸 모르면 fit이 잘 됐다고 좋아하다가 규제 단계에서 박살남.

> 🦴 **척추 재호출**: 약은 신호를 직접 안 만들고 **살아있는 욕조의 수도꼭지($k_{in}$)·배수구($k_{out}$)**를 누를 뿐이라 효과가 늦게 움직임 — 이게 turnover 해석임. 그런데 "효과가 늦는" 똑같은 현상을 **"약이 작용 부위에 늦게 도착해서"**라고 설명할 수도 있음(effect compartment). 겉보기 늦음의 정체가 **turnover(회전)냐 분포냐**, 그걸 데이터만으로는 못 가르는 게 이 PART의 위기임.

### A. 같은 곡선을 만드는 두 가지 구조

일상 비유부터. **같은 그림자를 만드는 두 물체**임. 벽에 비친 그림자(=효과-시간 곡선) 모양만 보고 "이건 공이다/상자다"라고 단정하면 위험함 — 조명을 옆에서 비추거나(=용량을 바꾸거나) 물체를 돌려봐야(=반복 투여해 봐야) 정체가 드러남. 비유-실제 대응: 그림자=관측된 효과-시간 곡선, 물체=진짜 기전(구조), 조명 각도 바꾸기=용량/투여횟수 바꾸기.

후보 ①: **Turnover 모델** (지금까지 배운 것 — 약이 생산·소실을 건드림):

$$
\underbrace{\frac{dR}{dt}}_{\text{반응 변화율}}
=
\overbrace{\underbrace{k_{in}}_{\text{생산(수도꼭지)}}\underbrace{S(C)}_{\text{촉진함수}}}^{\text{생산 촉진}}
-
\overbrace{\underbrace{k_{out}}_{\text{소실 clock(배수구)}}\underbrace{R}_{\text{반응 pool(수위)}}}^{\text{pool에서 빠지는 양}}
$$

기호 풀이: 이미 다 배운 것임 — $k_{in}$=생산속도, $S(C)$=농도가 생산을 몇 배로 키우는 함수, $k_{out}$=소실 시계, $R$=반응 수위. **지연의 원인은 "system이 새 수위로 차오르는 데 시간이 걸려서"**임.

후보 ②: **Effect compartment(효과 구획=link 모델, 분포지연 모델)** — 약이 혈장에서 작용 부위(생체상)로 천천히 건너가서 늦는다고 보는 구조:

> **[수식: 왜 필요한가]** "혈장 농도 $C$"와 "작용 부위 농도 $C_e$"가 다르고, $C_e$가 $C$를 시차를 두고 따라간다고 적으면, 효과가 농도보다 늦는 걸 **분포 지연**으로 설명할 수 있음.

$$
\underbrace{\frac{dC_e}{dt}}_{\text{작용부위 농도 변화}}
=
\underbrace{k_{e0}}_{\text{평형 clock}}
\left(\underbrace{C-C_e}_{\text{혈장-작용부위 농도차}}\right),
\quad
\underbrace{R}_{\text{반응}}=\underbrace{f(C_e)}_{\text{작용부위 농도의 함수}}
\quad \text{[R\&T pp.244–246]}
$$

기호 풀이:
- $C_e$ = effect-site concentration(작용 부위=생체상 농도). 혈장 농도 $C$랑 다름.
- $k_{e0}$ = 혈장↔작용부위 **평형 속도상수**(작을수록 천천히 따라감 = 더 큰 지연). "이퀄리브리엄(equilibrium=평형) 시계"라고 읽으면 됨.
- $C-C_e$ = 혈장과 작용부위의 농도차(이게 클수록 빨리 채워짐).
- $f(C_e)$ = 작용부위 농도로 효과를 내는 함수(보통 직접 Emax 또는 선형).

**한 줄 결론**: turnover는 "**system이 느려서**" 늦고, effect compartment는 "**약 도착이 느려서**" 늦음 — 원인이 완전히 다른데 **곡선은 똑같이 나올 수 있음.**

> 💡 G&W도 이 조합(분포지연 + turnover를 한 모델에 합치는 것)을 이론적으로 거론하지만, *"we have not yet seen data that support such estimation of the model parameters with reasonable precision"* (그런 모델 파라미터를 합리적 정밀도로 추정할 수 있게 받쳐주는 데이터를 아직 본 적 없다)며 신중함 [G&W p.252, Fig 3.44].

### B. PD6가 보여주는 비식별성의 정량 시그너처

> **[왜 지금 배우나]** "정말 데이터가 둘을 못 가르나?"를 막연한 주장이 아니라 **실제 숫자**로 봐야 함. G&W의 PD6 사례가 이걸 정량으로 박아둠.

PD6 사례: 한 자원자에게 새 화합물을 정맥 한 번에 **10.75 / 43 / 172 mg** 세 용량 주고 8시간 반응을 봄. 약의 PK는 1-구획($V=5.205\ \text{L}$, $k=0.456\ h^{-1}$). 약은 생산을 촉진(Model III, 선형 $S(C)$). 이 데이터를 **turnover 모델**과 **effect compartment 모델** 둘 다로 적합함 [G&W PD6, pp.758–763].

| 지표 | Turnover (선형 $S\cdot k_{in}$) | Effect compartment | 차이 Δ |
|---|---:|---:|---:|
| **WRSS**(가중 잔차제곱합=안 맞는 정도, 작을수록 좋음) | 15,516 | 15,518 | **2** |
| **AIC**(아카이케 정보기준=적합도-복잡도 균형 점수, 작을수록 좋음) | 1,041 | 1,040 | **−1** |
| 시간 상수 | $k_{out}=5.6\ h^{-1}$(7분) | $k_{e0}=5.6\ h^{-1}$(7분) | **0** |
| 반응 2배 농도 | $EC_{50}=1{,}633\ \text{ng}\cdot\text{L}^{-1}$ | $a=0.026 \to \sim 1{,}623\ \text{ng}\cdot\text{L}^{-1}$ | **<1%** |

> 용어 풀이: **WRSS**(weighted residual sum of squares)=예측이 데이터에서 벗어난 정도를 가중해서 더한 값. **AIC**(Akaike Information Criterion)=WRSS에 "파라미터 많이 쓴 벌점"을 더해 모델끼리 비교하는 점수. 둘 다 **낮을수록 좋음**. **비교 기준(anchor)**: 보통 AIC가 2~3 이상 차이 나야 "의미 있게 더 낫다"고 보고, $\Delta$AIC가 1 정도면 사실상 무승부임.

> ⚠️ **$\Delta$WRSS = 2, $\Delta$AIC = −1은 사실상 동치임.** "둘 중 하나가 더 매끄럽다"가 아니라 **"데이터가 둘을 못 가른다"는 신호임.** 게다가 $k_{out}$과 $k_{e0}$이 **정확히 같은 값(5.6)**으로, 두 모델 다 "농도가 EC₅₀일 때(약 1,600 ng/L) 반응이 baseline의 2배"라고 똑같이 예측함. 곡선이 겹치는 게 우연이 아니라 구조적으로 그렇게 됨 [G&W Table 6.1, p.763].

### C. 학생이 거의 100% 빠지는 함정 (혼동쌍 즉시정정)

> ⚠️ **혼동쌍 — "AIC 낮은 게 맞는 모델" (헷갈리는 그 자리에서 못박음)**
> $\Delta$AIC = −1만 보고 **"AIC가 낮은 effect compartment가 맞는 모델"**이라고 결정함. → **틀림.** 숫자가 우열처럼 보이고 두 곡선이 다 매끄러우니까 그럴싸하지만, $\Delta$AIC=−1은 **노이즈 수준의 차이**임. 이건 "어느 게 맞나"의 문제가 아니라 **"데이터가 못 가른다(비식별성)"**의 문제임. → §15 혼동쌍 표의 **Hook 7(비식별성 vs 모델 오설정)**과 정확히 같은 함정임.

이걸 그냥 두면 나비효과가 줄줄이 남:

1. AIC 미세차로 구조를 결정함(예: effect compartment 채택)
2. → 지연의 원인을 $k_{e0}$(분포)에 잘못 배정함 (사실은 $k_{out}$=turnover였는데)
3. → 새 용량 범위나 반복 투여 때 onset(시작)/offset(소멸) 예측이 빗나감
4. → 규제 단계에서 *"대안 구조 평가와 sensitivity analysis(민감도 분석)가 빠졌다"*는 deficiency(보완요구)가 돌아옴

> 용어 풀이: **sensitivity analysis(민감도 분석)** = 파라미터나 모델을 조금씩 바꿔보며 결론(예: 권장 용량)이 얼마나 흔들리는지 보는 것. **deficiency(데피션시)** = 규제기관이 "이거 더 채워라"라고 돌려보내는 보완요구.

### D. 그럼 어떻게 가르나 — 데이터 밖 증거를 끌어옴

핵심은 **"곡선 한 장으로는 못 가르니, 곡선 밖에서 둘을 갈라놓는 자리를 찾는다"**임:

| 증거 | Turnover를 지지 | Effect compartment를 지지 |
|---|---|---|
| **반응 변수의 정체** | 내인성 매개물질·바이오마커·세포 수·응고인자·위산 pH(=system이 만들고 없애는 것) | 약물 분포 지연이 원인일 만한 것(조직 침투) |
| **Dose range(용량 범위)** | 비선형 turnover 거동이 드러날 만큼 넓힘 | 안정적 $EC_{50}$과 타당한 $k_{e0}$로 hysteresis가 풀림 |
| **교란(반복 투여/washout)** | 반복 투여·약물 제거로 **system 회복 시간**($1/k_{out}$)을 직접 노출 | biophase(생체상) 평형으로 onset/offset 설명 |
| **Mechanism prior(기전 사전지식)** | 알려진 합성/소실 과정이 있음 | 알려진 조직 분포 지연이 있음 |

> 🔑 **갈라놓는 결정타 = 용량 의존성 + 반복투여 carry-over**: §6에서 배운 게 여기서 빛을 봄. ① **비선형 turnover면** 용량을 키울 때 peak 시점이 이동하거나 $t_{ss}$가 변함(effect compartment의 $k_{e0}$는 용량과 무관해서 안 변함). ② **반복 투여하면** turnover는 직전 용량의 잔여 반응(carry-over=이월 효과)이 쌓여 trough(골)가 점점 깊어지는데, effect compartment는 $C_e$가 혈장만 따라가서 패턴이 다름. ③ **반시계 고리(hysteresis loop)의 모양**: turnover 고리는 보통 더 통통하고, 용량 따라 모양이 변함. → 이 세 가지가 "그림자 밖에서 물체를 돌려보는" 방법임.

> 💼 **규제 제출에서의 실무 인사이트**: 두 인과 구조가 똑같이 잘 맞을 때 **규율 있는 접근**은 "어느 모델이 맞다"고 우기는 게 아니라 **(가) 생물학적 가정을 문서화하고 (나) 두 구조를 가를 수 있는 설계 요소(넓은 용량·반복투여)를 명시**하는 것임. 모델의 방어 가능성은 곡선의 매끄러움이 아니라 **mechanism + design support**에서 나옴.

> 📌 **비식별성 우회 전략 — 베테랑이 쓰는 트릭**: 두 모델을 **둘 다** 적합시키고, **sensitivity analysis로 "용량 결정이 모델 선택에 얼마나 민감한가"**를 제시함. 두 모델 모두에서 제안 용량이 안전 한계 안에 들면, **모델 선택 자체가 의사결정의 critical path(핵심 경로)에서 빠짐.** 즉 비식별성 앞에서 모델을 *고르려고 애쓰지 말고*, **비식별성이 결정에 영향을 안 주도록 결정 구조를 설계**하는 게 정통임.

> 📖 **G&W p.759, Fig 6.1; p.763, Table 6.1**: 반응-시간 적합은 본질적으로 동등해 보일 수 있지만 인과 해석은 서로 다르게 남는다는 걸 직접 보여줌. → **fit만으로 인과 구조를 결정하면 안 된다**는 정량 증거임. (G&W는 §3.7.5에서도 같은 경고를 함: effect compartment 모델을 turnover 데이터에 억지로 맞추면 $IC_{50}/EC_{50}$, $E_{max}$, $n$이 **용량 따라 변하는 생물학적으로 말 안 되는 상황**이 생긴다고 [G&W p.253].)

> 🌉 **다리문장**: 그럼 어느 쪽이든, 결국 임상에선 **"효과가 얼마나 오래 가나(duration)"**로 번역돼야 함. 그 답은 turnover냐 effect compartment냐가 아니라 **"PK 시계와 PD 시계 중 어느 게 더 느리냐"** 하나로 갈림. → PART VI.

---

# PART VI — 임상 의사결정으로 번역: 결국 어느 시계가 가장 느린가

## 12. PK clock vs PD clock — Duration 공식은 언제 살아있고 언제 폐기되나

> 🎯 **이 섹션 끝내면**: 약효 지속시간(duration)을 계산하는 교과서 공식을 **언제 써도 되고 언제 쓰면 큰일 나는지**를 "어느 시계가 느린가" 하나로 판정할 수 있게 됨.

> **[왜 지금 배우나]** 임상에서 제일 자주 하는 질문이 "이 약 얼마나 자주 줘야 하나(=효과가 얼마나 가나)"임. 답을 PK 반감기로만 계산하면 어떤 약은 맞고 어떤 약은 완전히 빗나감(이게 세션 도입부 동기였음). 그 갈림을 여기서 정밀하게 마무리함.

> 🦴 **척추 재호출**: 약은 욕조의 수도꼭지/배수구를 누를 뿐이라, 약이 사라져도 **수위(효과)가 돌아오는 속도는 배수구 시계($1/k_{out}$)가 지배**함. 그래서 "약이 빠지는 속도(PK)"와 "수위가 회복되는 속도(PD=turnover)" 중 **느린 쪽**이 효과 지속시간을 정함.

### A. 약을 주면 두 개의 시계가 동시에 돌아감

일상 비유: **두 사람이 손잡고 걷는데, 느린 사람이 전체 속도를 정함.** 약물의 PK clock(소실 속도)과 반응 system의 PD clock(회복 속도)이 동시에 돌아가는데, **관찰되는 효과 감소는 둘 중 느린 쪽이 결정함** [R&T pp.243, 247–256]. 비유-실제 대응: 두 사람=두 시계(PK, PD), 느린 사람=rate-limiting clock(속도 제한 시계), 전체 걷는 속도=관측 효과 소멸 속도.

> 용어 풀이: **rate-limiting(속도 제한)** = 여러 단계 중 가장 느린 단계가 전체 속도를 정한다는 뜻. **PK clock** = 약물 소실 시계($1/k$, $k$=PK 소실속도상수). **PD clock** = 반응 회복 시계($1/k_{out}$, turnover).

| 상황 | 느린 clock | 대표 약물 | 모델링 귀결 |
|---|---|---|---|
| **PK rate-limited**(약물이 더 느림) | 약물 소실/분포 | **Succinylcholine(석시닐콜린=속효성 근이완제)** 0.5/1/2/4 mg·kg⁻¹ 정맥, **Minoxidil(미녹시딜=K⁺채널 여는 혈관확장제, 평균동맥압 MAP 낮춤)** 25 mg 경구 | duration 공식 $t_D$가 **살아있음** [R&T pp.249–256] |
| **PD rate-limited**(system이 더 느림) | System turnover / 표적 재생 | **Acenocoumarol(아세노쿠마롤)** vs 응고인자 turnover, **Aspirin** 혈소판, **Omeprazole** 양성자펌프, **Paclitaxel** 백혈구 | Turnover / 표적소비 모델 필요. PK $k$만으로 duration 예측 **불가** [R&T pp.243, 251–254] |
| **약물 PK가 system보다 느림** | 간접 기전인데도 PK가 지배 | **Phenprocoumon(펜프로쿠몬=장반감기 쿠마린계, ~5일)** vs 응고인자 동역학 | 항응고 효과 회복이 **약물 잔류**를 따라감 [R&T p.243] |

### B. Region 1/2/3과 선형 감소 — 왜 효과가 한동안 "직선"으로 떨어지나

> **[왜 지금 배우나]** 단일 용량 후 효과가 시간에 따라 **직선처럼** 떨어지는 구간이 있음. 이게 왜 직선인지 알면 duration 공식(다음 C)이 어디서 오는지 이해됨.

선행지식 1줄: 효과-로그농도($E$-$\log C$) 관계는 보통 **S자(시그모이드)**임 — 아주 낮거나(바닥) 아주 높은(천장) 농도에선 평평하고, 가운데에서만 가파르게 변함.

계단식 $E$-$\log C$ 관계에서 **중간 구간(Region 2, 최대효과의 약 20~80%)**에 있을 때, 단일 용량 후 반응이 시간에 따라 **근사적으로 직선으로 감소함**:

$$
\underbrace{Response}_{\text{관측 반응}}
=
\underbrace{E(0)}_{\text{시작 효과}}
-
\overbrace{\underbrace{m}_{E\text{-}\log C\ \text{기울기}}\,\underbrace{k}_{\text{PK clock}}\,\underbrace{t}_{\text{시간}}}^{\text{선형 감소항}}
\quad \text{[R\&T Eq 8-9; pp.247–249]}
$$

기호 풀이: $E(0)$=시작 시점 효과, $m$=$E$-$\log C$ 곡선의 (중간 구간) 기울기, $k$=PK 소실속도상수, $t$=시간. **한 줄 결론: 농도는 지수적으로(로그-직선) 떨어지는데, 효과는 농도의 로그에 비례하니까, 그 둘이 합쳐져서 효과가 시간에 대해 직선으로 떨어짐.**

일상 비유: **비탈길 중간의 직선 구간**임 — 위쪽 평지(천장 plateau)나 아래쪽 완만한 자락(바닥)에선 같은 걸음 수(=같은 시간)에 높이가 별로 안 변하지만, 비탈 가운데(Region 2)에선 걸음마다 일정하게 내려감. 비유-실제: 비탈 가운데=Region 2, 일정한 내려감=선형 감소, 걸음 수=시간.

> 💡 **숫자 예시 + 비교 기준**: succinylcholine은 이 중간 구간에서 효과가 **약 22%/min**로 감소함 [R&T pp.249–256]. 비교 기준: 이건 "분 단위로 빠르게 풀리는 근이완"이라 마취과에서 삽관용으로 씀(=PK가 빨라서 PK-rate-limited의 전형). Region 1은 1차 동역학 비슷한 거동, Region 3은 천장(plateau)에 가까운 구간임.

### C. Duration 공식 — 언제 쓰는가

**PK-rate-limited이고 노출-반응 관계가 사실상 고정**일 때만 다음을 씀:

> **[수식: 왜 필요한가]** "용량을 얼마 주면 효과가 언제까지 가나"를 손으로 계산하고 싶을 때 쓰는 공식임. 단, 아래 조건(PK가 느린 시계)을 만족할 때만 유효함.

$$
\underbrace{t_D}_{\text{duration(효과 지속시간)}}
=
\underbrace{\frac{1}{k}}_{\text{PK clock 역수}}
\ln\!\left(\frac{\underbrace{Dose}_{\text{투여량}}}{\underbrace{C_{min}V}_{\text{최소 유효 약물량}}}\right)
=
\underbrace{\frac{1}{k}}_{\text{PK clock 역수}}
\ln\!\left(\frac{\underbrace{Dose}_{\text{투여량}}}{\underbrace{A_{min}}_{\text{효과 최소량}}}\right)
\quad \text{[R\&T Eq 8-12; pp.254–255]}
$$

기호 풀이: $t_D$=효과 지속시간, $k$=PK 소실속도상수, $Dose$=투여량, $C_{min}$=효과가 유지되는 최소 농도, $V$=분포용적, $A_{min}=C_{min}V$=효과 최소 약물량. **한 줄 결론: 효과 지속시간은 PK 반감기와 "용량이 최소 유효량의 몇 배냐"의 로그에 비례함.**

**용량을 두 배로 올리면 약물 반감기 하나만큼 duration이 추가됨**:

$$
\underbrace{\Delta t_D}_{\text{duration 추가분}}
=
\frac{\underbrace{\ln 2}_{\text{2배의 로그}}}{\underbrace{k}_{\text{PK clock}}}
=
\underbrace{t_{1/2}}_{\text{PK 반감기}}
$$

**한 줄 결론**: succinylcholine duration이 **용량 두 배마다 유효 반감기 하나씩** 더해지는 게 이 때문임 [R&T pp.255–256]. 일상 비유로, PK-rate-limited duration에서 dose doubling은 **로그 자 위에서 한 칸 오른쪽 이동**이고, 그 한 칸이 시간축에서 반감기 하나로 번역됨.

### D. 학생이 거의 100% 빠지는 함정 — Eq 8-12를 모든 약에 적용 (혼동쌍 즉시정정)

> ⚠️ **혼동쌍 — "duration 공식은 아무 약에나 쓴다" (그 자리에서 못박음)**
> Eq 8-12를 **warfarin, aspirin, omeprazole, paclitaxel**에 갖다 붙이지 말 것. 이 약들은 **PD-rate-limited**(system/표적이 더 느림)임. PK $k$로 계산한 $t_D$는 수학적으로는 매끈하게 나오지만 **임상적으로는 무의미**함. → **Duration 계산 전에 먼저 "어느 시계가 더 느린가?"를 물어야 함.** 답이 PD라면 그 자리에서 PK $k$로 duration 계산하는 걸 멈춰야 함. (§10에서 배운 "drug=0이면 effect=0인가? NO" 약들이 전부 여기 해당함.)

### E. 같은 기전 ≠ 같은 시계 — Acenocoumarol vs Phenprocoumon (Boss 함정)

> **[왜 지금 배우나]** 실무에서 30년 경력 베테랑이 스폰서(임상시험 의뢰사)에게 가장 자주 짚어주는 함정임. "같은 작용기전이면 같은 회복 속도"라는 그럴듯한 추론이 왜 틀리는지 봄.

스폰서가 주장함 — *"phenprocoumon과 acenocoumarol은 같은 항응고 기전(둘 다 쿠마린계, 응고인자 합성 억제)을 공유하니까 반응 회복은 같은 PD turnover 반감기로 결정돼야 한다."* → **거부함.**

- **Acenocoumarol** (PK 반감기 ~15시간) → PK가 짧으니 **PD clock**(응고인자 turnover)이 더 느림 → **PD-rate-limited**
- **Phenprocoumon** (PK 반감기 ~5일) → PK가 더 기니 **PK clock**이 지배 → **PK-rate-limited**

같은 prothrombin complex(프로트롬빈 복합체=응고인자) 동역학을 공유하지만 **서로 다른 rate-limiting clock**임(Fig 8-11) [R&T p.243]. **같은 작용기전 약물군에서도 약물별 PK가 속도 제한 단계를 정함.**

스폰서의 단순화를 그냥 채택하면:
- 두 약물에 **동일한 dose-titration(용량 적정) 규칙** 적용
- → phenprocoumon **누적 위험**(약이 오래 남아 과항응고) 또는 acenocoumarol **미달 용량**(효과 부족)
- → 환자 안전 사고 또는 약효 부전 사고
- → 규제: *"insufficient justification for proposed dosing interval(제안 투약 간격의 근거 불충분)"* 형태의 deficiency가 돌아옴

> 🔑 **정량 시그너처**: 예측 duration이 관측 duration과 **50% 이상 어긋나거나**, dose 증량 시 예측 증가가 관측치와 비례하지 않으면 → **rate-limiting clock을 잘못 잡았다는 신호임.**

> 📖 **R&T p.243, Fig 8-11**: 같은 항응고 반응 system도 약물 PK에 따라 다른 시계에 제한된다는 걸 보여줌. **R&T p.255, Fig 8-23 / p.256, Fig 8-24**: PK가 속도 제한일 때 용량 두 배가 duration에 반감기 하나를 더하는 패턴을 시각화함.

> 🌉 **다리문장**: 지금까지는 baseline($R_0$)이 시간 내내 안 변한다고 가정했음(§4의 "$R_0$는 time-invariant"). 그런데 질병이 진행하거나 하루주기 리듬이 있으면 **baseline 자체가 움직임.** 이걸 약효로 오독하면 큰일남. → 다음 절.

---

## 13. Baseline이 움직일 때 — Disease Progression·일주기 리듬

> 🎯 **이 섹션 끝내면**: "$R_0$가 일정하다"는 가정이 깨지는 경우(질병 진행·생체리듬)를 알아보고, 그 움직임을 **약효로 착각하지 않게** 됨.

> **[왜 지금 배우나]** §4에서 "$R_0=k_{in}/k_{out}$는 시간이 지나도 안 변한다(time-invariant)"고 가정했음. 그런데 만성질환이나 호르몬처럼 **baseline 자체가 천천히 드리프트(drift=표류)**하면, 그 움직임을 약 효과로 오독하기 쉬움. 그래서 따로 다룸.

> 🦴 **척추 재호출**: baseline은 수도꼭지($k_{in}$)와 배수구($k_{out}$)의 균형 수위임. 그렇다면 **질병이 수도꼭지나 배수구를 천천히 비틀면**, 약을 안 줘도 수위(baseline)가 표류함. 약이 없는데 수위가 움직이는 거니까, 약효랑 헷갈리면 안 됨.

### A. baseline이 표류하는 두 가지 결: 질병 vs 리듬

G&W는 baseline이 일정하지 않은 경우를 정리함 [G&W §3.12, pp.317–319]:

- **Chronobiologic rhythm(생체리듬)**: 심혈관 변화, 내분비(인슐린·에스트라디올·난포자극호르몬·성장호르몬·프로락틴), 활동량·체온 조절 등이 **하루주기로 오르내림.** 특히 체온은 패턴이 비대칭이고, 실험동물 시설의 **12/12시간 명암주기(light/dark cycle)** 같은 외부 시계(synchronizer=동기화 신호)에 강하게 끌림 [G&W p.317, Fig 3.92].
- **Disease progression(질병 진행)**: 질병이 **$k_{in}$ 또는 $k_{out}$ 중 하나를 바꿔서** baseline이 발병 시점부터 표류함 [G&W p.318, Fig 3.93].

> 용어 풀이: **chronobiologic(크로노바이올로직)** = 생체의 시간 리듬에 관한. **disease progression(질병 진행)** = 질병이 시간에 따라 악화/변화하는 과정. **drift(드리프트)** = 천천히 한 방향으로 밀려가는 표류.

### B. 질병이 baseline을 바꾸는 4패턴 — 욕조로 다시

§5의 4모델과 똑같은 구조임 — 다만 이번엔 **약이 아니라 질병**이 수도꼭지/배수구를 건드림:

| 질병의 작용 | 욕조로 | baseline 변화 | [출처] |
|---|---|---|---|
| 생산 $k_{in}$ **감소** | 수도꼭지 잠김 | baseline 내려감 | [G&W Fig 3.93 좌상] |
| 생산 $k_{in}$ **증가** | 수도꼭지 더 열림 | baseline 올라감 | [G&W Fig 3.93 우상] |
| 소실 $k_{out}$ **감소** | 배수구 막힘 | baseline 올라감 | [G&W Fig 3.93 좌하] |
| 소실 $k_{out}$ **증가** | 배수구 더 열림 | baseline 내려감 | [G&W Fig 3.93 우하] |

> ⚠️ **혼동쌍 즉시정정 — "baseline이 움직였다 = 약이 들었다"**: 틀림. 위 표처럼 **약 없이 질병만으로도** baseline이 위아래로 감. 약효는 "baseline 표류분"을 빼고(보정하고) 봐야 함. → §15 큰그림 표의 "baseline drift 무시 → 질병 진행을 약물 효과로 오독"이 정확히 이 실수임.

### C. 자기조절(self-regulating) baseline 식 — 천장이 있는 표류

baseline이 무한정 안 가고 어떤 **생리적 한계(physiological limit)**에서 멈추게 하려면, "한계에 가까울수록 차오름이 줄어드는" 항을 넣음:

$$
\underbrace{\frac{dR}{dt}}_{\text{baseline 변화}}
=
\underbrace{k_{in}}_{\text{생산}}
-
\underbrace{k_{out}R}_{\text{소실}}
,\qquad
\text{자기조절형} \;\Rightarrow\;
\text{차오름}\propto\underbrace{(R_{ss}-R)}_{\text{한계까지 남은 거리}}
\quad \text{[G\&W Eq 3:248–3:250; pp.318–319]}
$$

기호 풀이: $R_{ss}$=생리적 한계(천장), $R_{ss}-R$=한계까지 남은 거리(이게 0에 가까워지면 차오름이 멈춤). G&W는 여기에 유연성을 더하려고 $(R_{ss}-R)/R_{ss}$로 나누거나 지수 $a,b$를 추가한 변형도 제시함 [G&W Eq 3:249, 3:250]. **한 줄 결론: baseline 표류도 결국 turnover 골격($k_{in}-k_{out}R$)의 변형으로 적되, "한계에 가까울수록 느려진다"는 되먹임을 끼움.**

> 💡 **이상적 설계 메모(거장 시점)**: G&W는 *"baseline 값($k_{in}/k_{out}$)을 정하는 함수가 생리적 한계와 독립이도록"* 모델을 짜는 게 이상적이라고 함 — 즉 **"평소 수위"와 "천장"을 따로 추정**할 수 있어야 두 개가 안 섞임 [G&W p.319]. 실제론 되먹임이 baseline과 다른 기전으로 굴러가는 경우가 많음.

> 💡 **숫자 예시 (예고로 본 IgG, §4-C에서 미리 언급)**: 면역글로불린 IgG는 혈청 농도가 올라갈수록 반감기가 **점점 짧아지다가 30 mg·mL⁻¹에서 약 11일로 하한**에 멈춤(그 이상 올려도 더 안 짧아짐) — IgG 특이적 **포화성 보호기전(saturable protection, FcRn 의존)** 때문임 [G&W p.111]. 비교 기준: 보통 IgG 반감기는 약 3주(~21일)인데, 고농도에서 11일까지 단축되는 것임. 이건 "$k_{out}$이 system 상태(농도)에 따라 변하는" moderator/feedback의 실제 사례라서, §4-C의 moderator 식과 §15 tolerance로 이어짐.

> 🌉 **다리문장**: 이제 도구가 다 모였음 — 진단(hysteresis)→골격(turnover)→4모델→추정규율→비가역→비식별성→PK/PD시계→baseline. 이걸 **베테랑이 30초에 가르는 혼동쌍**으로 압축하고, 도구(NONMEM)와 이웃 세션 연결로 마무리함. → PART VII.

---

# PART VII — Integration(통합): 한 바느질로 꿰기

## 14. NONMEM이 뭔지부터 — 이 세션의 모든 진단이 도구로 들어가는 자리

> 🎯 **이 섹션 끝내면**: 앞에서 계속 나온 **NONMEM**이 정확히 뭘 하는 프로그램인지 알고, 이 세션의 손-진단들이 NONMEM 워크플로의 어디에 들어가는지 그릴 수 있게 됨.

> **[왜 지금 배우나]** 이 세션 내내 "NONMEM 돌리기 전에 손으로 잠가라"고 했는데, 정작 NONMEM이 뭔지 한 번도 정리 안 함. 1학년 기준으로 "그게 뭔지"부터 박음(루브릭 D3).

> 용어 풀이(도구 그게 뭔지): **NONMEM**(논멤, **NON**linear **M**ixed-**E**ffects **M**odeling=비선형 혼합효과 모델링) = 여러 사람의 약물 농도·효과 데이터를 **한꺼번에** 넣으면 $k_{in}$, $k_{out}$, $EC_{50}$ 같은 파라미터를 자동으로 찾아주는 **인구집단 약동·약력학 분석 표준 소프트웨어**임. "혼합효과(mixed-effects)"라는 건 **(가) 모든 사람이 공유하는 평균 파라미터(고정효과)**와 **(나) 사람마다 다른 개인차(랜덤효과=IIV, inter-individual variability=개인간 변동)**를 동시에 추정한다는 뜻임.

NONMEM이 쓰는 핵심 부품·점수:
- **`$THETA`(세타 블록)** = 추정할 **고정효과 파라미터**(평균값)를 적는 칸. §4에서 "$\$THETA$를 $(R_0, k_{out})$로 재코딩하라"가 바로 여기를 고치라는 말이었음.
- **OFV**(objective function value, 목적함수값) = 모델이 데이터와 안 맞는 정도의 점수(**낮을수록 좋음**). §4의 "30 iteration stuck-then-drop(30번 반복 동안 안 움직이다 뚝 떨어짐)"이 OFV 거동임.
- **covariance matrix**(공분산 행렬) = 추정값들의 불확실성·상관을 담은 표. 여기서 **correlation(상관계수)**과 **CV%**(추정 변동계수)를 읽음. §4의 "상관 0.98 초과, CV% 4000%"가 여기서 터지는 경고임.

**이 세션의 손-진단이 NONMEM 워크플로에 박히는 자리**(앞에서 다 배운 것의 재배치):

| 손으로 하는 진단 | NONMEM에서 대응되는 자리 | 어느 절에서 배웠나 |
|---|---|---|
| hysteresis 방향 그리기 | (모델 family 고르기 전 사전 결정) | §3 |
| $R_0,k_{out}$ 재모수화 | `$THETA`를 $(R_0,k_{out})$로 코딩 | §4 |
| graphical 초기값 | `$THETA` 초기값 입력 | §9 |
| stuck-then-drop 감지 | OFV iteration 로그 읽기 | §4 |
| 상관/CV% 폭발 감지 | covariance matrix 읽기 | §4 |
| turnover vs link 비식별성 | 두 모델 AIC/WRSS 비교 + sensitivity | §11 |

> 🔑 한 줄: NONMEM은 "**값을 찾아주는** 엔진"이지 "**기전을 정해주는** 판관"이 아님. 기전 판단(어느 시계가 느린가, 어느 구조가 맞나)은 **데이터 밖 prior와 설계**에서 나옴 — 이게 척추임.

> 🌉 **다리문장**: 이제 베테랑이 30초에 가르는 혼동쌍들을 한 표로 압축함. → 다음 절.

---

## 15. 5분 만에 외우는 혼동 쌍 — 베테랑이 30초 안에 가르는 7가지(+보너스)

> 🎯 **이 섹션 끝내면**: 이 세션에서 헷갈리기 쉬운 개념쌍들을 비유 한 줄로 즉시 가를 수 있게 됨(시험·발표 방어용 압축 카드).

> **[왜 지금 배우나]** 앞에서 흩어져 나온 혼동쌍들을 한 곳에 모아 "구조적 필연"을 비유로 못박음. 각 hook은 두 개념 차이의 핵심을 한 비유로 묶음.

### Hook 1 — Direct effect(직접 효과) vs Indirect response(간접 반응)
*바로 켜지는 전등 vs 서서히 따뜻해지는 전기장판.* Direct는 농도 상승에 즉시 따라옴. Indirect는 약이 생산/소실을 바꾸고 그 변화가 반응 pool에 쌓이며 늦게 나타남. **반응이 $C_{max}$(최고농도 시점)보다 늦게 peak에 도달하면 indirect를 먼저 의심.**

### Hook 2 — Model I(생산 억제) vs Model II(소실 억제)
*수원(水源) 틀기 vs 배수구 막기.* 단일 용량 범위에선 두 모델이 사실상 같은 데이터를 만들 수 있음. **mechanism prior나 더 넓은 dose range가 필요함.**

$$
\begin{aligned}
\text{Model I: }&\frac{dR}{dt}=\overbrace{k_{in}I(C)}^{\text{생산 억제}}-\underbrace{k_{out}R}_{\text{기존 소실}}\\
\text{Model II: }&\frac{dR}{dt}=\underbrace{k_{in}}_{\text{생산 유지}}-\overbrace{k_{out}RI(C)}^{\text{소실 억제}}
\end{aligned}
$$

### Hook 3 — $k_{in}$ vs $k_{out}$ (★ 이 세션 C7 핵심 함정 — 09 TMDD와 같은 자리)
*수원 속도 vs 배수 속도.* 기저상태에서 $k_{in}=k_{out}\cdot baseline$이고, $k_{out}=1/MRT_{response}$가 반응 반감기를 정함.

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

> ⚠️ **혼동쌍 즉시정정 (C7, 헷갈리는 그 자리에서 못박음)**: **$k_{in}$만 바꾸면** 새 정상 수위(steady-state 반응)로 가되 **돌아오는 속도($=1/k_{out}$)는 그대로**임(수도꼭지를 조절해도 배수구 시계는 안 변하니까). 반면 **$k_{out}$을 바꾸면 수위와 회복속도가 둘 다** 바뀜(배수구를 비틀면 평형 수위도, 빠지는 속도도 변함). → 그래서 Model I/III($k_{in}$ 건드림)은 $t_{ss}$가 **용량 독립**, Model II/IV($k_{out}$ 건드림)는 **용량 의존**이었던 것임(§6). **이건 09 TMDD에서 target turnover의 $k_{syn}$ vs $k_{deg}$를 헷갈리던 것과 똑같은 함정임** — 생성속도를 건드리는 것과 소실속도를 건드리는 것은 "회복 시계"에 미치는 영향이 근본적으로 다름. 헷갈리면 여기로 돌아올 것.

> 용어 풀이: **MRT**(mean residence time, 평균 체류시간)=반응 분자가 pool에 머무는 평균 시간. $MRT_{response}=1/k_{out}$.

### Hook 4 — Baseline $R_0$ vs Steady-state $R_{ss}$
*출발점 vs 목적지.* $R_0$는 약 투여 전 pool의 자연 균형, $R_{ss}$는 약 효과 하의 새 균형. **이동 속도는 $k_{out}$이 정하고, 이동 거리는 $E_{max}/EC_{50}$이 정함.**

### Hook 5 — Rebound(반동) vs Natural recovery(자연 복귀)
*과교정 vs 자연 복귀.* Rebound는 약 중단 시 반응이 **baseline을 넘어서는 것**(되먹임/내성 때문), natural recovery는 그냥 baseline으로 돌아오는 것. **구분 기준: baseline을 넘어서는가.**

### Hook 6 — Duration of effect(효과 길이) vs AUC of effect(효과 면적)
*효과의 길이 vs 효과의 면적.* Duration은 역치 이상/이하 시간, AUC of effect는 반응-시간 곡선 아래 면적. **같은 duration이어도 반응 높이가 다르면 AUC가 다름.**

### Hook 7 — Non-identifiability(비식별성) vs Misspecification(모델 오설정)
*지도가 둘 다 정확 vs 지도가 틀림.* 비식별성은 데이터가 둘 중 무엇이 맞는지 못 정하는 상태, misspecification은 데이터와 안 맞는 구조를 고른 상태. **$\Delta WRSS\approx 2$, $\Delta AIC\approx -1$은 비식별성 신호이지 misspecification 신호가 아님**(§11 PD6). 이게 둘을 가르는 정량 기준임.

### 보너스 — Reversible turnover(가역 회전) vs Irreversible kill(비가역 죽이기)
*수도꼭지 잠그기 vs 전구 빼내기.* Reversible은 system이 계속 생산·소실해 baseline 복귀. Irreversible은 표적/세포가 소비돼 대체/재성장이 필요.

$$
\begin{aligned}
\text{Reversible: }&\frac{dR}{dt}=\underbrace{k_{in}}_{\text{재생산}}-\underbrace{k_{out}R}_{\text{소실}}\\
\text{Irreversible: }&\frac{dR}{dt}=-\overbrace{\underbrace{K_{kill}}_{\text{kill 세기}}\underbrace{C}_{\text{노출}}\underbrace{R}_{\text{잔여 target/cell}}}^{\text{target/cell 소비}}
\end{aligned}
$$

### 5가지 clock 위치 오류 — 외워둘 것

> 이 다섯이 "지연을 엉뚱한 시계에 배정하는" 대표 사고임. 이걸 외우면 모델링 결정을 거의 자동으로 방어함.

| 오류 | 잘못 짚은 clock | 대표 반례(+비교 기준) |
|---|---|---|
| **E1. Mirror-slope(거울 기울기) 오독** | 모든 모델에서 초기 기울기를 $-k_{out}$으로 외삽 | PD7: 초기기울기 0.6~1.6 h⁻¹로 **용량 따라 변함** — system이 약과 무관해야 하는데 변하면 misspecification artifact [G&W p.251, p.765] |
| **E2. Phantom convergence(유령 수렴)** | turnover와 effect compartment가 같은 fit → 한쪽 확정 | PD6: $\Delta WRSS=2$, $k_{out}=k_{e0}=5.6\ h^{-1}$ — 비식별성 [G&W pp.758–763] |
| **E3. Wrong-clock $t_D$(잘못된 시계로 duration)** | 모든 약에 Eq 8-12 적용 | warfarin/aspirin/omeprazole/paclitaxel은 PD-rate-limited [R&T pp.251–254] |
| **E4. Linear-PK = linear-PD** | 용량비례 AUC면 곧 용량비례 반응 | methylprednisolone 16–1000 mg에서 AUC는 비례, lymphocyte 반응은 plateau [R&T pp.256–258] |
| **E5. Same-mechanism = same-clock** | 같은 작용기전이면 같은 속도제한 단계 | acenocoumarol(PD-limited, ~15h) vs phenprocoumon(PK-limited, ~5일) [R&T p.243] |

> 🌉 **다리문장**: 이 혼동쌍들이 어디서 왔고 어디로 가는지(이웃 세션 연결)와 한 줄 메시지로 닫음. → 다음 절.

---

## 16. 큰 그림 — 이 세션이 다른 세션들과 만나는 자리 (이전 10 ↔ 다음 12)

> 🎯 **이 섹션 끝내면**: 이 세션이 약리계측학 전체 지도에서 어디에 있고, 직전(10 PKPD)·직후(12 숨은 상태) 세션과 어떻게 연결되는지 한 문장으로 말할 수 있게 됨.

### A. 직전·직후 연결 (루브릭 A3)

- **← 이전(세션 10, PKPD·노출-반응)**: 세션 10은 "농도→효과"를 **시간 없이** 본 직접 노출-반응(Emax 등)이었음. 이번 11은 거기에 **시간(turnover 지연)**을 넣어, 같은 농도라도 효과가 늦게/따로 움직이는 걸 분해함. (※ 정직 메모: R&T `011_T`는 본문 내용이 세션 10의 `010_T`와 동일한 공통 챕터(R&T Ch.8)임 — 페이지 배너의 파일명만 다르고 본문은 같음. 그래서 R&T 인용은 11 고유 깊이가 아니라 **PKPD 공통 토대**로 썼음. 11 고유 내용은 G&W(`011_G`)와 백본 노트가 주 출처임.)
- **→ 다음(세션 12, 숨은 상태·effect compartment·transit)**: 이번 11의 **PART V 비식별성**이 정확히 12로 넘어가는 다리임. "효과-시간 곡선만으로는 turnover(숨은 system 상태)와 분포지연(effect compartment)을 못 가른다" → 12는 그 **숨은 상태(latent state)**를 effect compartment·transit chain으로 정식 모델링함. §10의 Friberg-Karlsson transit cascade가 그 예고편이었음.

### B. 약리계측학 아키텍처에서의 위치

이번 세션은 직접 노출-반응 모델링과 고급 질병/반응 시스템 사이임. 여기서부터 모델러는 **곡선 적합을 넘어 "원인을 분리"**해야 함.

| 후속 세션 | 이번 세션에서 열리는 개념 | 이번 세션 없으면 실패하는 것 |
|---|---|---|
| Transit compartment(12) | 분포/전달 지연과 turnover 지연 분리 | 모든 지연을 effect compartment로 흡수 |
| Tolerance/moderator | feedback, rebound, trough 이후 회복 타이밍 | $k_{out}$ 고정 가정 위반을 놓침 |
| Disease progression / baseline drift | $R_0$가 시간에 따라 움직이는 경우(§13) | 질병 진행을 약물 효과로 오독 |
| PopPK/PD IIV(13) | drug 파라미터와 system 파라미터 분리 | $E_{max}$, $k_{out}$, $k_{e0}$ 해석 혼동 |
| Sampling design | 숨은 시계를 식별할 관측 창 설계 | 비식별성을 후속 시험에 반복 |

### C. 이 세션을 약하게 다뤘을 때의 실패 모드

| 실패 모드 | 실무적 결과 |
|---|---|
| 모든 지연을 effect compartment로 처리 | $k_{e0}$이 생물학을 흡수 → 새 투여 프로토콜 시뮬레이션 실패 |
| $t_{ss}$를 결정적 증거로 처리 | 기전 주장이 설계 근거를 과대평가 |
| $E_{max}$ 단위 혼동 | 교차 연구·in vitro/임상 효력 비교가 오해 유발 |
| PD-rate-limited 약에 $t_D$ 적용 | duration 예측이 생물학적으로 무의미 |
| Baseline drift 무시 | 질병 진행·일주기 변동을 약물 효과로 오독 |

### D. 베테랑이 데이터를 받자마자 30초에 자동으로 돌리는 진단 순서

경력 있는 심사자는 **곡선이 매끄러운지를 먼저 묻지 않음.** 첫 30초에 다음을 본능적으로 돌림:

| 단계 | 보는 것 | 첫 가설 분기 |
|---|---|---|
| 1 | Plasma C vs response loop 방향 | 반시계→분포/turnover/활성대사체, 시계→내성/feedback, 없음→direct(단, 해상도 한계 고려) |
| 2 | 반응 방향 + $t_{ss}$ 용량 의존성 | 4-model 칸 중 하나로 좁힘 |
| 3 | trough 이후 회복이 모델보다 빠른가 | moderator/feedback 누락 가능성 |
| 4 | OFV가 30 iteration stuck-then-drop인가 | $r(k_{in},k_{out})>0.98$ 가능성 → $(R_0,k_{out})$ 재모수화 |
| 5 | 새 약 duration 질문 | PK clock vs PD clock 어느 쪽이 느린가 |

이 다섯을 통과한 뒤에야 NONMEM 출력에 손댐. 자동화 도구는 1·4단계는 흉내 내도 **2·3·5의 "데이터의 의미를 묻는 직관"은 데이터 밖 mechanistic prior를 요구해서 복제 안 됨.** 이게 베테랑과 자동화의 차이임.

### E. 최종 한 줄

간접 반응 모델링은 **"지연을 추가하는 일"이 아님.** **올바른 인과 시계에 지연을 배정하는 일임.** 한 번 정하면 안 흔들리는 순서:

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

## 한 줄 요약

> **약은 신호를 직접 못 만듦 — 살아있는 욕조(생성 $k_{in}$·소실 $k_{out}$)의 수도꼭지나 배수구를 누를 뿐임.** 그래서 효과가 농도와 따로 늦게 움직이고(hysteresis), 그 늦음의 정체는 보통 **분포가 아니라 turnover(회전)**임. baseline은 $k_{in}/k_{out}$, 회복 속도는 $1/k_{out}$, 약이 들어갈 자리는 4칸. **fit이 매끄러운 건 자랑이 아님 — 어느 시계가 가장 느린지를 증명할 수 있어야 함.** (PART V: 같은 곡선을 turnover와 effect compartment가 똑같이 그릴 수 있으니, 용량·반복투여·고리 모양으로 갈라야 함 → 12번 숨은 상태로.)

---

## 자가점검 (풀고 나서 답 확인)

**Q1 [회상].** Turnover 기본식 $dR/dt = k_{in}-k_{out}R$에서 baseline $R_0$는? 그리고 약을 끊었을 때 효과가 원위치로 돌아오는 속도를 지배하는 건 $k_{in}$인가 $k_{out}$인가?

**Q2 [혼동쌍].** "$k_{in}$만 바꿨다"와 "$k_{out}$을 바꿨다"는 회복 속도($1/k_{out}$)에 각각 어떤 영향을 주나? 이게 왜 Model I/III(용량 독립 $t_{ss}$)와 Model II/IV(용량 의존 $t_{ss}$)의 차이로 이어지나?

**Q3 [응용].** 용량을 키워도 peak shift가 안 나타남. 이게 effect compartment 모델을 증명하나?

**Q4 [APEX].** 단일 용량 데이터가 turnover와 effect compartment 둘 다에 똑같이 잘 맞음($\Delta WRSS=2$, $\Delta AIC=-1$, $k_{out}=k_{e0}$). 둘을 가르려면 무슨 증거가 필요한가?

**Q5 [임상].** Aspirin duration에 $t_D=\frac{1}{k}\ln(Dose/A_{min})$(Eq 8-12)을 쓰면 왜 부적절한가?

**Q6 [Boss].** 스폰서: "phenprocoumon과 acenocoumarol은 같은 항응고 기전이니 같은 PD 반감기로 회복이 결정된다." 이걸 어떻게 반박하나?

---

### 자가점검 답

**A1.** $R_0=k_{in}/k_{out}$(붓는 양과 빠지는 양이 같아지는 평형 수위). 돌아오는 속도는 **$k_{out}$**이 지배함(회복 시정수 $=1/k_{out}$) — 약을 끊으면 식이 $dR/dt=k_{out}(R_0-R)$가 돼서 $k_{out}$이 복귀 속도를 정함 [G&W Eq 3:76, 3:103].

**A2.** $k_{in}$만 바꾸면 새 정상 수위로 가되 **회복 속도($1/k_{out}$)는 그대로**(수도꼭지를 조절해도 배수구 시계는 안 변함). $k_{out}$을 바꾸면 **수위와 회복 속도가 둘 다** 바뀜. → 약이 $k_{in}$에 붙는 Model I/III은 $t_{ss}$가 **용량 독립**(소실항 $k_{out}R$ 그대로), 약이 $k_{out}$에 붙는 Model II/IV는 유효 시간상수가 농도 따라 변해 **용량 의존**임 [G&W pp.247–249]. (09 TMDD의 $k_{syn}$ vs $k_{deg}$와 같은 함정.)

**A3.** **아님.** PD9(Zooparc®)가 직접 경고함 — 약 함수 $S(C)$가 **선형이면** 생산에 작용해도 peak shift가 안 생김. 즉 "peak shift 없음"이 effect compartment를 의미하지 않음. 용량 범위·비선형 약물함수·system 동역학을 같이 봐야 함 [G&W pp.778–783, *"a lack of peak shift… does not necessarily imply an effect compartment model"*].

**A4.** 적합도 단독으로는 부족함. 필요한 증거: ① 반응 변수의 **mechanism prior**(내인성 매개물질이면 turnover, 조직 분포 지연이면 link), ② **더 넓은 dose range**(비선형 turnover 거동 노출), ③ **반복 투여/washout**(system 회복 시계 직접 관찰), ④ **PK clock 교란**, ⑤ $EC_{50}/k_{e0}$의 생물학적 타당성 [G&W pp.758–763; R&T pp.244–246].

**A5.** Aspirin은 혈장에서 빨리 사라지지만(반감기 ~15분) **표적(COX-1 비가역 아세틸화)·혈소판 기능 회복이 훨씬 느림**(수일). 즉 **PD-rate-limited**라서 duration은 PK $k$가 아니라 표적 교체 시계가 정함. PK $k$로 계산한 $t_D$는 매끈해도 임상적으로 무의미함 [R&T p.251].

**A6.** **거부.** 같은 기전이 같은 속도제한 시계를 뜻하지 않음. acenocoumarol(PK ~15h, 짧음)은 PK가 빨라 **PD clock**이 지배(응고인자 turnover가 더 느림), phenprocoumon(PK ~5일, 김)은 **PK clock**이 지배(약물 잔류가 더 느림). 같은 prothrombin complex 동역학을 공유해도 **약물별 PK가 rate-limiting clock을 바꿈**(Fig 8-11). 단일 PD 반감기 주장은 phenprocoumon에선 임상적으로 무의미하고 acenocoumarol에서만 유효함 — 약물별 별도 dose-duration 모델로 방어해야 함 [R&T p.243].

---

## 검증 체크리스트 통과표 (A1~G)

| 항목 | 통과 | 근거 1줄 |
|---|:---:|---|
| **A1** 앵커 전부 풀이(손실0) | ✅ | 욕조·baseline=$k_{in}/k_{out}$·4모델 I~IV·$I_{max}/IC_{50}$·$E_{max}/EC_{50}$·회복$=1/k_{out}$·hysteresis 방향·DRT·cascade·Friberg·PART V 비식별성 전부 포함 |
| **A2** 위계·인과 보존 | ✅ | $k_{in},k_{out}$=1차 원인 / $R_0$,반응반감기=2차 결과 명시(§4 인과위계 메모), 진단→골격→4모델→추정→비가역→비식별→시계 순서 유지 |
| **A3** 이전(10)·다음(12) 연결 | ✅ | §16-A: 10=시간없는 노출-반응, 12=숨은상태(PART V 비식별성이 다리)로 1줄씩 명시 |
| **B1** 인용 txt 실제확인·자리표시자 0 | ✅ | PD4(Table4.1 CV4000%)·PD5(kin19/kout0.43/IC50 95/Imax0.65)·PD6(WRSS15516/15518,AIC1041/1040,kout=ke0 5.6,EC50 1633)·PD7(0.6~1.6,SC50 50)·PD9(baseline80,IC50 0.25,clockwise Fig9.2) 원문 대조 완료, placeholder 없음 |
| **B2** 범위밖 플래그 | ✅ | Sharma-Jusko V~VIII 명명·Friberg-Karlsson은 [교과서 외/1차문헌]로 표기(기존 보존) |
| **B3** 충돌 드러내고 정정 | ✅ | 기존 PART I~IV의 충돌정정(PD7 compound명, PD5 0.43=최종값, Zooparc 시계방향, mirror-slope 범위표기) 보존 + PART V Zooparc 2.5/5mg(Fig9.2) vs 5/25mg(Fig9.1) 라벨차 의식 |
| **B4** 메타블록 약어+쪽주의 | ✅ | §0 메타블록에 G&W/R&T 풀이 + "쪽=원판 교재 기준" + 011_T=010_T 중복 정직 메모 |
| **C1** 용어 즉시 괄호설명 | ✅ | NONMEM·$C_e$·$k_{e0}$·WRSS·AIC·sensitivity·deficiency·rate-limiting·MRT·chronobiologic·drift 등 첫 등장 시 괄호 풀이 |
| **C2** 수식 3단(왜→기호→결론) | ✅ | effect compartment식·Eq8-9·Eq8-12·자기조절baseline식 모두 [왜 필요]→기호풀이→한줄결론 |
| **C2-b** 식 밀집 해소 | ✅ | PART V·VI 식 사이마다 욕조/그림자/비탈길 비유·PD6 숫자·다리문장 삽입 |
| **C3** 새 개념마다 "왜 지금" | ✅ | §11~16 각 [왜 지금 배우나] 박스 |
| **C3-b** 섹션 학습목표 | ✅ | §2~§16 전 섹션 학습목표 부착 — 각 🎯 "이 섹션 끝내면~" |
| **C4** 비유 먼저+1:1 대응 | ✅ | 그림자=곡선/물체=기전/조명각도=용량·반복(§11), 두사람걷기=두시계(§12), 비탈가운데=Region2(§12) 대응 명시 |
| **C5** 1학년 선행지식 보충 | ✅ | $E$-$\log C$ S자, mixed-effects 뜻, 명암주기 등 그 자리 1줄 보충 |
| **C6** 음슴체 일관 | ✅ | 전 구간 ~함/~음/~임 |
| **C7** 혼동쌍 즉시정정 | ✅ | $k_{in}$ vs $k_{out}$(Hook3, 09 TMDD 연결)·AIC낮은게맞는모델(§11C)·duration공식 아무약(§12D)·baseline움직임=약효(§13B) 모두 그 자리 정정 |
| **C8** 수치에 비교 기준 | ✅ | $\Delta$AIC 1≈무승부(기준 2~3)·22%/min=분단위·IgG 11일 vs 평소 21일·MTT 100~140h 등 anchor |
| **D1** 핵심개념 숫자예시 | ✅ | PD6(10.75/43/172mg, WRSS차 2)·succinylcholine 22%/min·IgG 30mg/mL→11일 |
| **D2** 흔한 실수·혼동쌍 | ✅ | E1~E5 clock 오류표 + Hook 1~7 + 보너스 |
| **D3** 도구 "그게 뭔지" | ✅ | §14 NONMEM 전체(약자 풀이·$THETA$·OFV·covariance·워크플로 매핑) |
| **D4** 자가점검 3~5(+답) | ✅ | Q1~Q6 + 답 6개 |
| **E1** 척추 박스+매섹션 호출 | ✅ | 도입부 척추 박스(기존) + §11·§12·§13 🦴 재호출 + 한줄요약 |
| **E2** 섹션전환 다리문장 | ✅ | 매 절 끝 🌉 다리문장 |
| **E3** 도입 지도+말미 요약 | ✅ | §1 한장지도(기존) + 말미 "한 줄 요약" |
| **E4** 부족분 예고+플래그 | ✅ | Friberg·Sharma-Jusko [교과서외], 그림자합성모델 G&W 신중 인용 |
| **F1** 한국어·음슴체·MD | ✅ | 전체 |
| **F2** LaTeX·표·ASCII | ✅ | $...$ 수식·표 다수·§16 ASCII 순서도 |
| **F3** 메타블록 6요소 | ✅ | §0: 약어/대상(비전공·1학년OK)/선행지식/범위/원천목록/쪽주의 |
| **G** naive-reader 막힘 0 | ✅ | 모든 용어 즉시 괄호·비유 착지·숫자 anchor·다리문장으로 "갑자기 왜/이게 뭐지/되돌아가야 함" 차단 |

---

`C-260518-000145-K7M`

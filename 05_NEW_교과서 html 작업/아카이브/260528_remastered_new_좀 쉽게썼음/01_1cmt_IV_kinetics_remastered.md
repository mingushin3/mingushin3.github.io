# 세션 01 [Remastered] — 1구획 IV 동력학: 같은 기울기, 다른 결정

**원재료:** Gabrielsson & Weiner 5e Ch.2 §2.2.1–2.2.5 + Case Study PK1 / Rowland & Tozer 5e Ch.3
**페이지:** G&W p.14–32, p.469–475 / R&T p.53–76
**대상:** 계량약리학 박사과정, PopPK 입문–중급
**한 줄 약속:** 이 세션 끝나면 반로그 도표 하나만 보고 "유지용량 권고"를 절대 안 쓰게 됨.

---

## §0. 시작 전 — 이 세션이 끝까지 메아리치는 한 줄

> **약물의 체내 처리는 $CL$과 $V$ 두 개가 정함. $K$랑 $t_{1/2}$는 그 둘이 만든 결과지, 독립적인 원인이 아님.**

이 한 줄을 진짜로 체화하면, 앞으로 받는 모든 IV 보고서에서 같은 질문 두 개를 자동으로 던지게 됨 — **"AUC는 어떻게 변했음? $C^0$는 어떻게 변했음?"** 이 두 질문이 안 던져진 보고서는 그 자체로 다시 돌려보내는 거임. 다른 거 다 잊어도 이거 하나면 됨.

---

<!-- SLIDE_START: §1 | title: §1 함정 — 같은 K, 두 배 다른 CL -->

## §1. 함정 — 같은 기울기 뒤에 두 배 다른 청소율이 숨어 있음

월요일 아침. Compound A 10 mg IV bolus, 4명 데이터를 받음. 반로그 도표를 그림. Subject 1이랑 Subject 4를 봄. **말단 기울기가 거의 똑같음.** $K\approx 0.01\;\mathrm{min^{-1}}$, $t_{1/2}$도 거의 같음. 자연스럽게 머릿속에 떠오르는 결론 — "아, 둘 다 약물 처리 능력이 비슷하네. 같은 유지용량 권고 가능."

이게 함정임. 표 좀 보면 [G&W 5e, Case Study PK1, Tables 1.2/1.3, p.473–474]:

| Subject | $K$ (min⁻¹) | $V$ (L) | $CL$ (L/min) | $AUC$ (µg·min·L⁻¹) |
|---|---:|---:|---:|---:|
| 1 | 0.01 | 10 | **0.1** | 98,000 |
| 2 | 0.02 | 9.8 | 0.2 | 49,000 |
| 3 | 0.02 | 10 | 0.2 | 51,000 |
| 4 | 0.01 | **20** | **0.2** | 51,000 |

$K$랑 $t_{1/2}$는 S1≈S4인데, **$CL$은 두 배 차이임** (S1: 0.1, S4: 0.2 L/min). 같은 주입속도 $R_{in}$을 두 사람에게 주면 항정 농도 $C_{ss}$가 정확히 두 배 차이가 남 (이 계산은 §7 Q5에서 직접 함). 한 명은 독성역, 한 명은 sub-therapeutic 됨. **보고서 한 장이 두 환자를 동시에 망가뜨림.**

왜 같아 보였음? 답은 한 줄임:

$$
\underbrace{K}_{\text{기울기}}=\frac{\underbrace{CL}_{\text{정화능}}}{\underbrace{V}_{\text{분포공간}}}
$$

S4는 $CL$도 두 배(0.2 L/min), $V$도 두 배(20 L)임. 분자랑 분모가 동시에 두 배니까 비율은 보존됨. **반로그 기울기는 비율만 보여줌. 절대값을 안 보여줌.**

이 함정이 이 세션 전체의 spine임. 앞으로 나오는 모든 카드가 "그래서 S1 vs S4가 어떻게 갈리는지"에 한 번씩 등장함.

---

<!-- SLIDE_START: §2 | title: §2 욕조 모델 — 마스터 비유 -->

## §2. 욕조 모델 — 이 세션의 마스터 비유

함정에서 빠져나오려면 머릿속에 정확한 그림이 박혀 있어야 함. 그래서 욕조 하나 그려둠. 앞으로 모든 카드가 이 욕조 좌표 안에서 움직임.

```
          ┌─────────────┐
          │             │ ← 약물 (총량 = D)
          │   욕조 V    │ ← V = 욕조 크기 (분포공간)
          │             │
          │  농도 = C   │ ← C = 욕조 안 약물 농도
          └─────┬───────┘
                │ 배수구 = CL
                ▼ (단위 시간당 빠지는 깨끗한 물의 부피)
              제거됨
```

| 욕조 좌표 | PK 파라미터 | 단위 | 직관 |
|---|---|---|---|
| **배수구 크기** | $CL$ (clearance) | 부피/시간 | 단위 시간당 깨끗해지는 혈액의 부피 |
| **욕조 크기** | $V$ (volume) | 부피 | 같은 약물량이 들어왔을 때 얼마나 묽어지는지 |
| **수위 떨어지는 속도** | $K = CL/V$ | 1/시간 | 남은 양 중 매 시간 빠지는 비율 |
| **수위가 절반이 되는 시간** | $t_{1/2} = \ln 2 / K$ | 시간 | 절반시간 |

### 욕조 비유의 진짜 가치 — 사라지지 않는 한 줄

이 비유에서 절대 잊으면 안 되는 한 줄:

> **수위가 떨어지는 속도($K$)만 보고 배수구 크기($CL$)를 알 수 없음.**

같은 속도로 떨어져도, 배수구도 두 배 욕조도 두 배면 실제 단위 시간당 빠지는 물의 양은 두 배임. 이게 정확히 S1 vs S4임. S4는 큰 욕조에 큰 배수구를 달고 있는 것임. 표면(=수위 떨어지는 속도)에선 작은 욕조 작은 배수구랑 구분 안 됨.

🎯 **앞으로의 모든 카드에서 이 좌표를 씀**: $CL$ 얘기할 때 = 배수구, $V$ 얘기할 때 = 욕조, $K$ 얘기할 때 = 수위 속도, $t_{1/2}$ 얘기할 때 = 절반 시간.

---

<!-- SLIDE_START: §3 | title: §3 위계 규칙 — 원인과 결과 분리 -->

## §3. 위계 규칙 — 일차(원인) vs 이차(결과)를 영구히 분리

PK 파라미터 4–5개를 동등하게 줄세워서 외우려고 하면 무조건 헷갈림. 위계로 박아둬야 함:

```
[일차 파라미터 — 원인]            [이차 파라미터 — 결과]
   CL ─────────────┐
                   ├── K = CL/V ── t½ = 0.693·V/CL
   V  ─────────────┘                MRT = 1/K  (1-cpt IV bolus만)

   ↑                                ↑
   생리학·해부학이                  반로그 도표가
   직접 결정                         보여주는 시간 표지
```

| 파라미터 | 위계 | 무엇이 정함 | 임상에서 무엇을 결정함 |
|---|---|---|---|
| $CL$ | **일차** | 혈류·추출·대사·배설 | AUC, $C_{ss}$, **유지용량** |
| $V$ | **일차** | 조직 결합, 체수분, 측정 공간 | $C^0$, **부하용량** |
| $K$ | 이차 | $CL/V$ 비율 | 반로그 기울기, ODE 시상수 |
| $t_{1/2}$ | 이차 | $\ln 2 / K = 0.693V/CL$ | 항정 도달 시간, 채혈 창 |
| $MRT$ | 이차 | $AUMC/AUC$ | 평균 체류 시간, $V_{ss}$ 환산 |

⚡ **이 위계가 깨지는 순간 일어나는 일**: NONMEM에서 $K$에 공변량 붙임 → 신기능 변화($CL$) vs 부종 변화($V$)가 한 변수에 섞임 → 잔차가 체중·CrCl이랑 같이 움직이는 이유를 설명 못함 → 규제 리뷰에서 재분석 요구 들어옴. 한 위계 오해가 보고서 끝에서 폭발하는 거임.

> 📖 **Rowland & Tozer 5e, p.54–55, Fig.3-1, Fig.3-2**: 같은 용량을 줬을 때 "초기 농도", "기울기", "AUC" 셋이 각각 다른 정보를 담고 있다는 사실을 한 그림 안에서 분리해서 보여줌. Drugs A/B는 $V$ 같고 $CL$ 다름 (→ 기울기·AUC 다름, 절편 같음). Drugs C/D는 $CL/V$ 비율 같음 (→ 반감기 같음, 절편·AUC 다름). 이 그림 한 번 안 보고 가면 절편·기울기·AUC를 한 덩어리 '노출 지표'로 묶어 읽게 됨.

---

## §4. 다섯 장 카드 — 위계대로 한 장씩

<!-- SLIDE_START: C1 | title: C1 청소율 CL -->

### 🃏 C1. 청소율 $CL$ — AUC·유지용량의 일차 결정자 [⚡ Apex]

**한 줄 정의**: $CL$은 단위 시간당 약물이 완전히 비워지는 가상의 혈장 부피임. 단위가 L/min임. **속도(rate)가 아니라 유량(flow)**임. [G&W p.16; R&T p.56]

$$
\underbrace{\text{Rate of elimination}}_{\text{제거속도}}=\underbrace{CL}_{\text{정화부피/시간}}\cdot\underbrace{C}_{\text{현재농도}} \qquad [\text{R\&T Eq.3-4, p.56; G\&W Eq.2:2, p.16}]
$$

$$
\underbrace{CL}_{\text{정화부피/시간}}=\underbrace{Q}_{\text{혈류(운반)}}\cdot\underbrace{E}_{\text{추출분율}} \qquad [\text{R\&T Eq.3-5, p.56}]
$$

| 파라미터 | 의미 | 변화 원인 |
|---|---|---|
| $Q$ | 장기로 약물을 운반하는 혈류량 | 장기 혈류 변화 |
| $E$ | 장기 통과 중 제거되는 분율 | 효소·수송체·배설능 변화 |
| $CL$ | $Q\cdot E$의 곱 (얼마나 많이 지나가고, 그중 얼마를 빼내는가) | 위 둘의 합 |

> 💡 $CL=Q\cdot E$를 단순 공식이 아니라 **"얼마나 많은 혈액이 지나가고 그중 얼마를 빼내는가"**로 읽으면, 간/신 청소율 후속 세션에서 고추출·저추출 약물 분기가 자연스럽게 이어짐.

#### 왜 $CL$이 일차임? — "$V$가 사라지는" 두 식

**식 1. 노출량 식 (전체 투약 사건을 한 번 적분한 결과)**:

$$
\underbrace{CL}_{\text{정화능}}=\frac{\underbrace{Dose}_{\text{투여량}}}{\underbrace{AUC_0^\infty}_{\text{총노출}}} \qquad [\text{G\&W p.19; R\&T p.59–60}]
$$

**식 2. 항정상태 식 (constant infusion)**:

$$
\underbrace{\frac{dC}{dt}}_{\text{농도변화}}=\underbrace{\frac{R_{in}}{V}}_{\text{입력/V}}-\underbrace{\frac{CL}{V}C}_{\text{제거/V}}\;\;\xrightarrow{dC/dt=0}\;\;\underbrace{C_{ss}}_{\text{항정농도}}=\frac{\underbrace{R_{in}}_{\text{주입속도}}}{\underbrace{CL}_{\text{정화능}}} \qquad [\text{G\&W Eq.2:22, p.23}]
$$

**두 식 모두 $V$가 깨끗하게 사라짐.** 이게 핵심임. 분포공간은 곡선 출발점($C^0$)이랑 시상수($K$)는 바꾸지만, 한 번 적분해버리거나(=AUC) 시간을 무한히 늘려버리면(=Css), 노출·항정의 중심에는 $CL$만 남음.

#### S1 vs S4 — 함정 카드 1번 적용

| Subject | $K$ | $t_{1/2}$ | $CL$ | $R_{in}=10\;\mu g/min$ 줄 때 $C_{ss}$ |
|---|---:|---:|---:|---:|
| 1 | 0.01 | 68 min | 0.1 L/min | $10/0.1 = \mathbf{100}\;\mu g/L$ |
| 4 | 0.01 | 71 min | 0.2 L/min | $10/0.2 = \mathbf{50}\;\mu g/L$ |

기울기(=K)·반감기 거의 같음. **항정 농도는 정확히 두 배 차이.** $CL$이 정한 거임. 표면(반로그 기울기) 신뢰가 임상적으로 얼마나 위험한지 숫자로 보여주는 자리임. [G&W Eq.2:22, p.23; G&W Case Study PK1, p.473–474]

> 💼 **실무 인사이트 (PopPK 모수화)**: NONMEM에서 공변량을 $K$에 직접 붙이면 안 됨. 신기능이 좋아져서 $CL$이 올라간 건지, 부종이 빠져서 $V$가 줄어든 건지 식별 안 됨. **`TRANS2`로 $CL$과 $V$를 따로 두는 게 단순 코딩 관습이 아니라 위계 보존 안전장치임.**

> **C1 핵심 한 줄**
> ① 노출(AUC) 질문, 유지용량 질문 → 무조건 $CL$
> ② $K$ 같음 ≠ $CL$ 같음 (S1 vs S4)
> ⚡ $K$로 건너뛰는 순간 유지용량 권고가 두 배 어긋남

---

<!-- SLIDE_START: C2 | title: C2 분포용적 V -->

### 🃏 C2. 분포용적 $V$ — $C^0$·부하용량의 일차 결정자

**한 줄 정의**: $V$는 실제 부피가 아니라, **체내 총량을 혈장 농도 하나로 환산하는 겉보기 공간**임. [G&W p.20; R&T p.63]

$$
\underbrace{V}_{\text{환산공간}}=\frac{\underbrace{A_b}_{\text{체내총량}}}{\underbrace{C}_{\text{측정농도}}} \qquad [\text{G\&W Eq.2:14, p.20; R\&T Eq.3-26, p.63}]
$$

IV bolus에서는 시간 0으로 외삽한 절편으로 계산함:

$$
\underbrace{V}_{\text{초기희석공간}}=\frac{\underbrace{D_{iv}}_{\text{IV 용량}}}{\underbrace{C^0}_{\text{외삽초기농도}}} \qquad [\text{G\&W Eq.2:13, p.20}]
$$

말단 정보가 있으면 우회식도 씀:

$$
\underbrace{V}_{\text{말단용적}}=\frac{\underbrace{CL}_{\text{정화능}}}{\underbrace{K}_{\text{말단기울기}}}=\underbrace{1.44}_{1/\ln 2}\cdot\underbrace{CL}_{\text{정화능}}\cdot\underbrace{t_{1/2}}_{\text{반감기}} \qquad [\text{R\&T Eq.3-27/3-28, p.63}]
$$

#### "겉보기" — 이 한 단어가 안 박히면 게임 끝남

**Quinacrine** (항말라리아제, 조직 결합이 극단적으로 강함). $V \approx 40{,}000$ L임. 체중 70 kg 사람한테 40,000 L 부피가 어디 있음? 없음. 그게 포인트임.

$V$가 큰 이유를 정확히 풀면 이거임:
- 약물 총량은 그대로인데 (분자 $A_b$)
- 측정 농도 ($C$)가 낮음 — 왜? 약물 대부분이 조직에 묶여서 혈장에 잘 안 나옴
- $V = A_b / C$ 식에서 분모가 작아지니까 $V$가 커 보임

$$
\underbrace{V}_{\text{관찰용적}}=\underbrace{V_u}_{\text{비결합용적}}\cdot\underbrace{f_u}_{\text{유리분율}} \qquad [\text{G\&W Eq.2:15, p.20}]
$$

> 📖 **G&W 5e, p.15, Fig.2.3**: 두 양동이 그림임. 실제 물 부피는 같은데 측정 농도가 다르면 겉보기 용적이 10 L vs 100 L로 갈라지는 장면을 직접 그려서 보여줌. 이 그림 안 보고 가면 $V$를 해부학적 부피로 오해함.

#### S1 vs S4 — 함정 카드 2번 적용

Compound A에서 S1–3는 $V\approx 10$ L, S4만 20 L임. **S4의 절편(=$C^0$)이 다른 사람들보다 낮음.** 같은 10 mg 용량인데 보이는 농도가 절반이니까 환산 공간이 두 배인 거임.

$V$가 커지면 → $C^0=D/V$가 낮아짐 → **부하용량을 더 줘야 같은 초기 농도에 도달.**

근데 주의: $V$가 두 배 됐다고 $AUC$가 두 배 되는 건 아님 ($AUC$는 $CL$이 정함, C1에서 봤음). [G&W p.470, p.473]

#### 부하용량 ↔ 유지용량 한 줄 정리

$$
\underbrace{LD}_{\text{부하용량}}=\underbrace{V}_{\text{분포공간}}\cdot\underbrace{C_{target}}_{\text{목표농도}},\qquad
\underbrace{MD}_{\text{유지용량/단위시간}}=\underbrace{CL}_{\text{정화능}}\cdot\underbrace{C_{ss,target}}_{\text{목표 Css}}
$$

**부하용량은 $V$ 함수, 유지용량은 $CL$ 함수.** 이 한 줄이면 임상 용량 결정의 80%가 정리됨.

> 💼 **실무 인사이트**: 반로그 도표에 명백한 꺾임점(break point)이 보이면, 1구획 $V$를 그대로 부하용량에 쓰기 전에 점검 — **중심 구획 $V_c$인지, 항정 상태 $V_{ss}$인지**. 초기 빠른 효과 목적이면 $V_c$, 평형 후 농도 유지가 목적이면 $V_{ss}$. (다구획 세션 예고편)

> **C2 핵심 한 줄**
> ① $C^0$ 질문, 부하용량 질문 → 무조건 $V$
> ② "$V$가 크다" = "혈장에 보이는 농도가 낮다" (조직에 숨어 있음)
> ⚡ $V$를 해부학적 부피로 읽으면 부하용량 판단이 무너짐

---

<!-- SLIDE_START: C3 | title: C3 소실속도상수 K -->

### 🃏 C3. 소실속도상수 $K$ — 반로그 기울기는 원인이 아니라 결과

**한 줄 정의**: $K$는 단위 시간당 남은 양 중 제거되는 분율임. 구조적으로는 $CL/V$임. [G&W p.17; R&T Eq.3-7, p.56]

$$
\underbrace{K}_{\text{제거분율/시간}}=\frac{\underbrace{CL}_{\text{정화능}}}{\underbrace{V}_{\text{분포공간}}}
$$

#### ODE에서 반로그 직선까지 — 한 호흡에 끝냄

$$
\underbrace{\frac{dC}{dt}}_{\text{농도변화}}=-\underbrace{K}_{\text{분율속도}}\cdot\underbrace{C}_{\text{현재농도}}=-\frac{\underbrace{CL}_{\text{정화능}}}{\underbrace{V}_{\text{분포공간}}}\cdot\underbrace{C}_{\text{현재농도}} \qquad [\text{G\&W Eq.2:1, p.16}]
$$

적분:

$$
\underbrace{C(t)}_{\text{시간 }t\text{ 농도}}=\underbrace{C^0}_{\text{초기농도}}\cdot\underbrace{e^{-K\cdot t}}_{\text{지수감소}}=\frac{\underbrace{D}_{\text{용량}}}{\underbrace{V}_{\text{분포공간}}}\cdot e^{-(CL/V)\cdot t} \qquad [\text{G\&W Eq.2:4, p.17}]
$$

양변 로그:

$$
\underbrace{\ln C}_{\text{로그농도}}=\underbrace{\ln C^0}_{\text{로그절편}}-\underbrace{K}_{\text{기울기 절대값}}\cdot\underbrace{t}_{\text{시간}}
$$

**반로그 도표에서 직선의 기울기가 $-K$**임. [G&W Fig.2.4/2.6, p.15–17; R&T Eq.3-11, p.58]

#### 욕조 비유 다시 — "분율 제거"의 직관

지수감소가 헷갈리는 이유는 "매 시간 똑같은 양을 퍼낸다"고 착각해서임. 아님. **남은 양의 같은 비율을 계속 퍼냄.** R&T Table 3-1: $K=0.1$ hr⁻¹로 100 mg 시작하면 1시간 후 90 mg, 2시간 후 81 mg, 3시간 후 72.9 mg. **매 시간 10 mg이 아니라, 남은 양의 10%가 사라지는 거임.** [R&T p.57]

$$
\underbrace{\frac{A}{Dose}}_{\text{남은분율}}=\underbrace{e^{-K t}}_{\text{지수잔존}}=\left(\frac12\right)^{\underbrace{n}_{t/t_{1/2}}} \qquad [\text{R\&T Eq.3-19, p.59}]
$$

#### S1 vs S4 — 함정 카드 3번 적용 (이 카드의 핵심)

$K=0.01$이 같다는 건 $CL/V$ 비율이 같다는 뜻일 뿐임. S1: $0.1/10 = 0.01$. S4: $0.2/20 = 0.01$. **같은 비율을 만드는 ($CL$, $V$) 조합은 무한히 많음.** $K$만 봐서는 어느 조합인지 알 수 없음.

이게 왜 PopPK 모수화에서 결정적임?

> 💼 **실무 인사이트 (TRANS1 vs TRANS2)**: `ADVAN1 TRANS1`은 $K$를 직접 추정함. 적합 자체는 됨. 그런데 신기능 covariate를 어디에 붙임? $K$에 붙이면 $CL$ 변화인지 $V$ 변화인지 모름. `TRANS2`는 $CL$과 $V$를 따로 추정함 → 공변량 위치를 분리할 수 있음. **모수화 선택이 PopPK 해석 가능성을 결정하는 자리임.**

> **C3 핵심 한 줄**
> ① 반로그 기울기 = $K = CL/V$. **표면 표지지, 일차 파라미터 아님.**
> ② $K$가 같다고 $CL$이 같지 않음 (S1 vs S4: 같은 K, 두 배 다른 CL)
> ⚡ $K$를 일차 파라미터로 모델링하면 공변량 위치가 섞임

---

<!-- SLIDE_START: C4 | title: C4 반감기 t1/2 -->

### 🃏 C4. 반감기 $t_{1/2}$ — 임상에서 가장 자주 오해받는 파라미터

C4는 이 세션의 **절정**임. 왜? 임상에서 가장 자주 인용되는 파라미터인데, 가장 자주 잘못 해석됨.

> **흔한 실수**: "반감기가 늘었다 → 신기능 저하다 → 용량 감량"
> **진실**: $t_{1/2}=0.693\cdot V/CL$임. $V$가 늘어도 $t_{1/2}$가 길어짐. 부종 환자에서 반감기가 늘었다고 신장 용량 감량을 권고하면, **실제로는 분포공간만 늘어난 것일 수도 있음.**

$$
\underbrace{t_{1/2}}_{\text{반감기}}=\frac{\underbrace{\ln 2}_{\text{절반조건}}}{\underbrace{K}_{\text{분율속도}}}=\frac{\underbrace{0.693}_{\ln 2}\cdot\underbrace{V}_{\text{분포공간}}}{\underbrace{CL}_{\text{정화능}}} \qquad [\text{G\&W Eq.2:3/2:6, p.17–18; R\&T Eq.3-15, p.58}]
$$

#### Creatinine vs Inulin — 같은 $CL$, 다른 $t_{1/2}$의 깔끔한 사례

R&T가 두 생리학 marker로 직접 보여줌 — **creatinine** (근육 대사산물, total body water에 가까운 분포)과 **inulin** (다당류, extracellular water에 가까운 분포). [R&T p.58]

| Compound | $CL$ (L/hr) | $V$ (L) | $t_{1/2}$ (hr) | 분포 특성 |
|---|---:|---:|---:|---|
| Creatinine | 4.5 | 42 | **6.5** | TBW 근접 (세포 안까지 들어감) |
| Inulin | 4.5 | 16 | **2.5** | ECW 근접 (세포 안 못 들어감) |

**$CL$이 똑같이 4.5인데 반감기가 2.5배 차이.** $V$가 다르니까. → "긴 반감기 ≠ 낮은 청소율"의 깔끔한 증거임. 

#### 항정 도달 시간 — $V$가 $C_{ss}$는 안 바꾸지만 시간은 바꿈

| 반감기 수 | 항정 도달 분율 |
|---:|---:|
| 1 | 50% |
| 2 | 75% |
| 3 | 87.5% |
| 4 | ~94% |
| 6.64 | ~99% |

[G&W p.22; R&T p.59]

**$C_{ss} = R_{in}/CL$**에서 $V$는 사라짐. 그런데 **$t_{1/2}=0.693 V/CL$**을 통해 항정 도달 시간은 $V$에 비례함. 부종 환자 (큰 $V$)는 같은 $C_{ss}$에 도달하는 데 더 오래 걸림. **유지용량 결정과 부하용량/도달시간 결정은 분리해서 해야 함.**

실무 응용 한 줄 — 부하용량 근사 (1구획 IV, 투약 간격 $\tau$):

$$
\underbrace{LD}_{\text{부하용량}}\approx\underbrace{MD}_{\text{유지용량}}\cdot\frac{\underbrace{\tau}_{\text{투약간격}}}{\underbrace{0.693\cdot t_{1/2}}_{\text{반감기 단위}}}
$$

반감기 긴 약물 (digoxin이 전형 예) → 부하용량 없으면 항정 도달까지 며칠씩 걸림.

#### 말단 단계가 진짜 소실 단계인가? — Midazolam vs Gentamicin

C4에서 가장 위험한 함정. **"말단 직선 = 소실 단계"는 자동 성립이 아님.**

**Midazolam (안전한 케이스).** 79 kg 성인, 7.5 mg base IV bolus. 반로그 프로파일이 **이상성(biphasic)**임. 처음 ~1시간 분포 단계, 그 뒤 소실 단계. 5분 시점에 혈장에 0.61 mg, **나머지 6.9 mg (92%)는 이미 혈장 밖**. R&T Fig.3-5: 2시간까지 누적 AUC가 전체의 **48%**. → 분포 단계 AUC 비율이 절반 정도라 일부 목적에서 1구획 근사 안전함. [R&T p.61–65]

**Gentamicin (위험한 케이스).** Aminoglycoside, 신장 청소가 매우 빠른 친수성 약물, 조직 침투는 매우 느림 (특히 신피질). R&T Fig.3-7 원문: **"More than 95% of an i.v. dose of this antibiotic is eliminated into the urine before distribution equilibrium has occurred"**. [R&T p.66, Fig.3-7]

여기서 가장 헷갈리는 게 "distribution equilibrium"의 정체임. **두 시점 명확히 분리해야 함**:

$$
\underbrace{t_{\alpha}}_{\text{혈장↔말초 빠른 평형}}\approx\underbrace{30\;\mathrm{min}}_{\text{α-phase 시상수}}\;\;\ll\;\;\underbrace{t_{\beta\text{-deep}}}_{\text{깊은 조직 분포 평형}}\approx\underbrace{36\;\mathrm{hr}}_{\text{R\&T Fig.3-7}}
$$

R&T가 말하는 "분포 평형"은 빠른 α-phase가 아니라 **깊은 조직 (신피질 등) 분포 평형 (≈36시간)**임. 36시간 도달 전에 신장이 이미 95% 비워버림. 즉 **말단 직선 (36시간 이후)은 깊은 조직에서 천천히 빠져나오는 5% 미만을 보고 있는 것**일 뿐, 소실 능력 대표가 아님. [R&T p.66; Adelman et al., Antimicrob Agents Chemother 1982;22:800–804]

#### 결정 기준 — 한 줄로

> **"분포 단계 AUC가 전체 AUC의 몇 %를 차지하는가"** 가 모든 걸 정함.
> Midazolam ≈ 48% → 1구획 근사 안전 (일부 목적).
> Gentamicin > 95%가 분포 평형 도달 전에 빠져나감 → 말단 기울기 신뢰 위험.

> 💼 **실무 인사이트**: 말단 기울기 채택할 때 던질 질문은 "마지막이 직선이냐?"가 아님. **"그 직선이 분포 단계 오염이 충분히 작아진 뒤의 직선이냐?"**임. 점검 항목 — 최소 데이터 포인트 수, 회귀 $R^2$, **분포 단계 AUC 비율**.

> **C4 핵심 한 줄**
> ① $t_{1/2}$ 변화 → $CL$인지 $V$인지 분리 필요 (AUC·$C^0$ 함께 봄)
> ② 말단 직선 = 소실 단계 자동 성립 아님 (gentamicin trap)
> ⚡ "긴 반감기 = 신기능 저하"로 건너뛰면 불필요한 감량 또는 분포 오판

---

<!-- SLIDE_START: C5 | title: C5 평균체류시간 MRT -->

### 🃏 C5. 평균체류시간 $MRT$ — 1구획 IV의 수학적 서명

**한 줄 정의**: $MRT$는 약물 분자가 체내에 머무는 시간의 평균값임. 시간가중 평균임. [G&W Eq.2:11, p.19]

$$
\underbrace{AUC_0^\infty}_{\text{총노출}}=\int_0^\infty \underbrace{C(t)}_{\text{농도함수}}\,dt,\qquad
\underbrace{AUMC_0^\infty}_{\text{시간가중노출}}=\int_0^\infty \underbrace{t}_{\text{시간가중치}}\cdot\underbrace{C(t)}_{\text{}}\,dt
$$

$$
\underbrace{MRT}_{\text{평균체류}}=\frac{\underbrace{AUMC_0^\infty}_{\text{시간가중면적}}}{\underbrace{AUC_0^\infty}_{\text{총면적}}}
$$

> 💡 **비유**: $t_{1/2}$이 "농도가 반이 되는 한 시점 (중위값)"이라면, $MRT$는 **모든 분자가 머문 시간을 평균낸 출석부 (무게중심)**. 한 분자는 5분 머물고 다른 분자는 5시간 머물면, 이걸 다 평균낸 값이 $MRT$.

#### 1구획 IV bolus의 "수학적 서명" — $MRT/t_{1/2} \approx 1.443$

1구획 IV bolus에서 특별히 다음이 성립함 [R&T Eq.3-25, p.60]:

$$
\underbrace{MRT}_{\text{평균체류}}=\frac{1}{\underbrace{K}_{\text{분율속도}}}=\frac{\underbrace{t_{1/2}}_{\text{반감기}}}{\underbrace{\ln 2}_{\text{절반조건}}}\approx\underbrace{1.443}_{1/\ln 2}\cdot\underbrace{t_{1/2}}_{\text{반감기}}
$$

Compound A 4명 데이터로 확인 [G&W 5e, Case Study PK1, Table 1.3, p.474]:

| Subject | $K$ (min⁻¹) | $t_{1/2}$ (min) | $MRT$ (min) | $MRT/t_{1/2}$ |
|---|---:|---:|---:|---:|
| 1 | 0.01 | 68 | 98 | 1.44 |
| 2 | 0.02 | 34 | 48 | 1.41 |
| 3 | 0.02 | 36 | 53 | 1.47 |
| 4 | 0.01 | 71 | 100 | 1.41 |

> 📌 **표 값 vs 이론값 각주**: 이론적으로 $MRT/t_{1/2}$는 정확히 $1/\ln 2 \approx 1.4427$임. 표에서 1.41~1.47로 흩어진 건 측정 노이즈가 아니라 **표 원본이 분 단위로 반올림됐기 때문**임 (S1: $98/68=1.441$, S4: $100/71=1.408$). 수식상으로는 정확히 $1/\ln 2$. 이 동일성이 **단일지수 1구획 IV bolus의 수학적 서명**.

$$
\underbrace{\frac{MRT}{t_{1/2}}}_{\text{1구획 IV bolus 비율}}=\underbrace{\frac{1/K}{\ln 2 /K}}_{\text{정의 대입}}=\underbrace{\frac{1}{\ln 2}}_{\text{무차원 수학상수}}\approx\underbrace{1.4427}_{\text{이론값}}
$$

#### 이 비율이 깨지면 무엇을 의심할 것인가

$MRT/t_{1/2}$가 1.443에서 멀어진 데이터를 봤음. 가장 먼저 던질 질문:

> **"이 자료가 정말 1구획처럼 행동하는가?"**

가능한 원인:
- 다구획성 (분포 단계가 별도)
- 혈관외 투여 (흡수 단계가 더해짐)
- 말단 외삽 품질 문제 (AUMC가 AUC보다 외삽 오차에 더 민감)

#### MRT의 박사과정 실무 가치 — $V_{ss}$ 환산

NCA에서 MRT를 보고하는 진짜 이유:

$$
\underbrace{V_{ss}}_{\text{항정상태 분포용적}}=\underbrace{CL}_{\text{정화능}}\cdot\underbrace{MRT}_{\text{평균체류}}
$$

구획 모델 없이 (model-independent하게) $V_{ss}$를 뽑을 수 있는 NCA의 무기임. 다구획 세션 예고편.

> **C5 핵심 한 줄**
> ① 평균 체류시간 = $AUMC/AUC$
> ② $MRT/t_{1/2} \approx 1.443$이 무너지면 1구획 가정을 재검토
> ⚡ $1.443\times t_{1/2}$를 단순 변환식으로만 외우면 다구획·혈관외에서 NCA 해석 무너짐

---

<!-- SLIDE_START: §5 | title: §5 혼동쌍 3개 -->

## §5. 자주 헷갈리는 세 쌍 — 표면은 비슷, 위계는 다름

다섯 카드를 다 봤으면 이제 임상·모델링에서 매번 헷갈리는 세 쌍을 정리. **공통점: 표면 비슷, 위계 다름.**

### 🔀 혼동쌍 1. $CL$ vs $K$ — 일차 vs 이차

| 비교 | $CL$ | $K$ |
|---|---|---|
| 단위 | L/min (유량) | 1/min (속도) |
| 위계 | **일차** | 이차 |
| 식 위치 | $Dose/AUC$, $R_{in}/C_{ss}$, $Q\cdot E$ | $CL/V$, $\ln 2 / t_{1/2}$ |
| 변화 원인 | 혈류·추출·대사·배설 | $CL/V$ **비율** 변화 |
| 혼동 시 결과 | (없음 — 일차임) | 유지용량·공변량 위치 모두 망가짐 |

> ⚡ **기억 고리 — 배수구 vs 수위 속도**: $CL$ = 배수구 크기, $K$ = 수위가 떨어지는 상대 속도. 배수구 커도 욕조가 크면 수위는 천천히 떨어짐 → **$K$ 같아도 $CL$은 두 배 다를 수 있음** (S1 vs S4). 공변량이 붙는 자리는 **배수구($CL$)와 욕조($V$)지, 그 비율($K$)이 아님**.

### 🔀 혼동쌍 2. $V$ vs $V_{ss}$ — 겉보기 bolus 용적 vs 항정 분포 용적

| 비교 | $V$ (bolus) | $V_{ss}$ |
|---|---|---|
| 식 | $D/C^0$ 또는 $CL/K$ | $CL\cdot MRT$, 조직 분배 합 |
| 시점 | 분포 평형 직후 외삽 | 항정 평형 |
| 다구획에서 | 중심 구획 $V_c$와 구분 필요 | NCA에서 모델-독립적 |
| 혼동 시 결과 | 부하용량에 말단 용적 잘못 적용 | 1구획처럼 단순화 |

> ⚡ **기억 고리 — 실제 vs 외관상 용기**: $V$는 "약이 실제로 어디 있는가"가 아님. 관측 농도 설명을 위해 **가정해야 하는 겉보기 공간 크기**임. 조직 결합 강할수록 $V$가 실제 체적을 훨씬 초과 (Quinacrine: 40,000 L).

본 세션 범위는 "$V$가 겉보기 파라미터"라는 사실까지. $V_{ss}$ 본격 해석은 다구획 분포 세션. [G&W p.20–21; R&T p.63–64]

### 🔀 혼동쌍 3. $t_{1/2}$ vs $MRT$ — 절반시간 vs 평균체류

| 비교 | $t_{1/2}$ | $MRT$ |
|---|---|---|
| 정의 | $\ln 2 / K$ | $AUMC/AUC$ |
| 직관 | 농도 반감의 **한 시점 (중위)** | 분자 체류시간의 **평균 (무게중심)** |
| 1구획 IV에서 관계 | — | $= 1/K = 1.443 \cdot t_{1/2}$ |
| 다구획·혈관외에서 | 말단 기울기 의존 | 분포·흡수 구조까지 반영 |
| 혼동 시 결과 | 항정 시간과 청소 능력 혼동 | NCA 체류시간·$V_{ss}$ 해석 오류 |

> ⚡ **기억 고리 — 중위값 vs 무게중심**: $t_{1/2}$은 농도가 반으로 줄어드는 **한 시점**. $MRT$는 모든 분자의 체류시간을 **평균낸 값**. 1구획 IV에서만 $MRT = 1.443 \times t_{1/2}$가 깔끔하게 성립. 분포 지연·흡수 지연 더해지면 $MRT$가 $t_{1/2}$보다 훨씬 길어질 수 있음.

---

## §6. PopPK 실무 보강 — C1–C5 결과를 실제 데이터에 적용하는 두 게이트

여기까지(§1–§5)가 G&W Ch.2 + R&T Ch.3 본문 내용임. §6은 **그 결과를 실제 NONMEM 데이터셋에 적용할 때 박사과정 PopPK 학습자가 가장 자주 발이 걸리는 두 자리**임. 본 세션 출처 범위 밖이지만, 1구획 IV 단계에서 미리 잡아두면 후속 다구획·공변량 세션 출발이 훨씬 안정됨.

두 게이트:
- **M1. BLQ 처리**: $K$·말단 $V$·외삽 $AUC$·$CL$ 사슬의 **신뢰성 게이트**
- **M2. Allometric scaling**: $CL$·$V$의 **공변량 비교 가능성 게이트**

<!-- SLIDE_START: M1 | title: M1 BLQ 처리 -->

### 🃏 M1. BLQ (정량 한계 미만) — 말단을 어떻게 다루는가가 모든 걸 결정

**한 줄 정의**: BLQ는 LLOQ 미만이라 정량값 보고가 불가능한 농도 구간. 보고서엔 보통 "BLQ", "<LLOQ", 또는 missing 표기.

$$
\underbrace{C_{obs}}_{\text{관측농도}}<\underbrace{LLOQ}_{\text{정량하한}}\;\;\Rightarrow\;\;\underbrace{\text{BLQ tag}}_{\text{보고 분류}}
$$

#### 왜 1구획 IV 세션에서 BLQ를 짚어야 함?

**말단 영역 = 농도 낮은 영역 = BLQ 점들이 모이는 자리.** 그리고 그 자리가 **$K$를 결정하는 자리**임. 즉:

```
BLQ 처리 규칙 → 말단 회귀 직선 → K 추정 → t½ → AUC 외삽 → CL = Dose/AUC → 유지용량
```

**한 단계라도 흔들리면 사슬 끝 유지용량 권고가 어긋남.**

#### NCA 단계 — 위치별 결정론적 규칙

| 위치 | 표준 처리 | 영향 |
|---|---|---|
| **첫 정량값 이전 BLQ** | 0 처리 | AUC 시작점 미미 |
| **정량값 사이 끼인 BLQ** | 선형 보간 또는 결측 | log-linear 회귀 가중치 |
| **말단 BLQ** | **0 또는 결측 후 외삽** | **$K$·말단 $V$·$AUC_t^\infty$에 직접** |

말단 영역 BLQ를 0 치환 후 단순 회귀하면 두 왜곡이 동시 발생:

1. **$K$ 과대추정**: 마지막 점이 0이 되면서 회귀선이 가팔라짐 → $K\uparrow$, $t_{1/2}\downarrow$
2. **외삽 $AUC$ 과소**: $AUC_t^\infty = C_{last}/K$인데 $K$가 부풀려져서 외삽분 축소 → 총 $AUC\downarrow$ → $CL = Dose/AUC$ 과대 → 유지용량 권고 어긋남

$$
\underbrace{AUC_t^\infty}_{\text{말단외삽분}}=\frac{\underbrace{C_{last}}_{\text{마지막 정량값}}}{\underbrace{K}_{\text{말단 기울기}}}
$$

> 💼 **실무 게이트**: NCA 보고서에 **% AUC extrapolated**가 항상 같이 와야 함. **20% 넘으면 그 보고서는 신뢰 약함으로 분류** (많은 가이던스 권고). 보고서 검토 1차 질문 — "말단 BLQ 어떻게 처리했음? 외삽 비율 몇 %임?"

#### PopPK 단계 — Beal M1/M3/M5/M6/M7 likelihood 분기

NCA는 한 환자 곡선의 결정론적 규칙. NONMEM은 다름 — **BLQ 점을 likelihood에 어떻게 반영하는가**가 분기점. Beal 2001 + Ahn 2008 + Bergstrand & Karlsson 2009가 표준 reference. [Beal SL. *J Pharmacokinet Pharmacodyn* 2001;28:481–504; Ahn JE et al. *J Pharmacokinet Pharmacodyn* 2008;35:401–421; Bergstrand M, Karlsson MO. *AAPS J* 2009;11:371–380]

| 방법 | 처리 방식 | 적합 상황 | 한계 |
|---|---|---|---|
| **M1** | BLQ 점 결측 처리 후 제외 | BLQ 비율 < 10% | 비율 늘면 $K$ 편향 |
| **M3** | **누적분포 $\Phi(LLOQ\mid\hat C,\sigma)$를 likelihood에 추가** | **표준 권고**, BLQ 10–60% | 계산 비용 ↑ |
| **M5** | $LLOQ/2$ 치환 후 정량값처럼 처리 | 빠른 비교용 | 편향 발생 |
| **M6** | 연속 BLQ 중 첫 점만 $LLOQ/2$ 보존 | 말단 tail 긴 경우 | 이론적 근거 약함 |
| **M7** | 0 치환 후 정량값처럼 처리 | **사용 비권장** | 가장 큰 편향 |

M3가 표준인 이유 — 한 줄로:

$$
\underbrace{\mathcal{L}_{M3}}_{\text{우도}}=\underbrace{\prod_{C_i\geq LLOQ} \phi(C_i\mid \hat C_i, \sigma)}_{\text{정량값: 확률밀도}}\cdot\underbrace{\prod_{C_j<LLOQ} \Phi\!\left(\frac{LLOQ-\hat C_j}{\sigma}\right)}_{\text{BLQ: 누적확률 (censoring)}}
$$

핵심 직관 — **"BLQ 점은 '측정값이 LLOQ보다 작다는 사실(censoring event)'만 알고 있음"** 을 likelihood에 그대로 반영. 0으로 깎거나(M7) 절반값으로 미는 것(M5)이 아니라, **"이 시점엔 농도가 LLOQ 이하라는 확률 한 덩어리"**를 그 자리에 넣는 것임.

NONMEM 구현: `F_FLAG=1` 또는 `YLO` 구문으로 `LAPLACE` 방법과 함께.

> 💼 **보고서 검토 2차 질문**: PopPK 단계에서는 "**M3 적용했음? BLQ 비율 몇 %임?**"이 첫 질문. NCA 결정론적 규칙 → PopPK likelihood 기반 처리로 넘어가는 다리가 M3임.

**M1 정리**: BLQ는 "0"이 아니라 "정량 불가". 말단 BLQ 처리 한 줄이 $K$ → $t_{1/2}$ → $AUC$ → $CL$ → 유지용량 권고 전체를 흔듦.

---

<!-- SLIDE_START: M2 | title: M2 Allometric scaling -->

### 🃏 M2. Allometric scaling — 체중 표준화의 0.75 vs 1.0

**한 줄 정의**: 생리학적 파라미터를 체중의 거듭제곱 함수로 표준화하는 framework.

$$
\underbrace{P_i}_{\text{개체 i 파라미터}}=\underbrace{P_{ref}}_{\text{기준 체중 (보통 70 kg)}}\cdot\left(\frac{\underbrace{BW_i}_{\text{개체 체중}}}{\underbrace{BW_{ref}}_{\text{70 kg}}}\right)^{\underbrace{\theta}_{\text{지수}}}
$$

| 파라미터 | 표준 지수 | 직관 |
|---|---:|---|
| **$CL$** | **0.75** | 대사·열 손실은 표면적(∝$BW^{2/3}$)과 활동(∝$BW^{1}$)의 절충 |
| **$V$** | **1.0** | 체수분·세포외액·조직 부피는 체중에 거의 선형 |
| $Q$ | 0.75 | $CL$과 같은 유량 차원 |
| $t_{1/2}$ (예측) | 0.25 | $V^{1.0}/CL^{0.75}=BW^{0.25}$ → 큰 체중일수록 약간 길어짐 |

#### 왜 1구획 IV 세션에서 이걸 짚어야 함?

C1·C2에서 $CL$이 유지용량, $V$가 부하용량을 정한다고 했음. 그런데 환자 체중이 50–100 kg 범위로 흩어진 자료를 보고 있다면, **$CL$·$V$를 raw 값으로 환자별 비교하는 게 의미 없음.**

Compound A S1($V=10, CL=0.1$)이랑 S4($V=20, CL=0.2$)도 만약 체중이 두 배 차이라면, **allometric scaling 후 두 배 차이가 거의 사라질 수 있음.** 진짜 covariate 신호를 보려면 체중을 먼저 표준화한 뒤 남는 잔차를 봐야 함.

#### NONMEM 코드 (가장 빈번한 형태)

```fortran
CL = THETA(1)*(WT/70)**0.75 * EXP(ETA(1))
V  = THETA(2)*(WT/70)       * EXP(ETA(2))
```

> 💼 **PopPK 1주차 흔한 실수**:
> ① 체중 covariate 누락 → 잔차 패턴이 체중과 같이 움직임
> ② 체중을 **선형**으로 넣음 ($CL \propto BW^{1.0}$) → 큰 체중 환자에서 $CL$ 과대추정
> **$CL$엔 0.75, $V$엔 1.0** — 이게 표준 출발점.

#### 소아·신생아 — size × maturation 분리

성인에서 잘 되는 ¾제곱이 신생아에서 깨지는 이유 한 줄: **체중이 작아진다는 사실(size)과 효소·신기능이 미성숙하다는 사실(maturation)의 시간 척도가 다름.** 체중은 출생부터 단조 증가하지만 CYP3A·UGT·신사구체 여과율은 발달의 sigmoid 궤적을 따라 늦게 성숙. [Anderson BJ, Holford NHG. *Annu Rev Pharmacol Toxicol* 2008;48:303–332]

표준형 — 두 항의 **곱**:

$$
\underbrace{CL_i}_{\text{개체 청소율}}=\underbrace{CL_{std}}_{\text{성인 표준값}}\cdot\underbrace{\left(\frac{BW_i}{70}\right)^{0.75}}_{\text{size 항 (allometric)}}\cdot\underbrace{F_{mat}(PMA_i)}_{\text{maturation 항}}
$$

$$
\underbrace{F_{mat}(PMA)}_{\text{성숙 분율}}=\frac{\underbrace{PMA^{Hill}}_{\text{현재 성숙 정도}}}{\underbrace{TM_{50}^{Hill}}_{\text{50\% 도달 PMA}}+\underbrace{PMA^{Hill}}_{\text{}}}\;\;\in\;\;[0,\;1]
$$

| 기호 | 의미 | 직관 |
|---|---|---|
| **PMA** | post-menstrual age (수태 후 주수) | 출생일 아니라 **수태**부터 센 시계. 조산아·만삭아를 한 좌표에 둘 수 있음 |
| **$TM_{50}$** | $F_{mat}=0.5$가 되는 PMA | 약물·기전별 (신사구체여과 ≈ 47.7주) |
| **Hill** | sigmoid 가팔기 | 보통 3–5 |
| **$F_{mat}$** | 무차원 분율 (0=미성숙 ~ 1=성숙) | 성인은 $\approx 1$로 수렴 |

> 💡 **왜 출생일이 아니라 PMA임?** 조산아 (PMA 32주 출생)와 만삭아 (PMA 40주 출생)를 출생 후 일자로 정렬하면 "생후 0일"의 청소 능력이 서로 완전히 다름. PMA로 정렬하면 같은 sigmoid 위에 자연스럽게 놓임. **출생이라는 사건이 결정점이 아니라 수태부터의 발달 시간이 결정점**임.

> 💼 **신생아 PopPK 보고서 흔한 코멘트 두 가지**:
> ① "체중만 covariate, maturation 누락" → 신생아 $CL$ 과대추정
> ② "출생 후 일자(postnatal age)를 maturation 시계로 사용" → 조산아·만삭아 정렬 실패
> 둘 다 표준 출발점은 **size × maturation 분리 + PMA-based $F_{mat}$ sigmoid**.

**M2 정리**: $CL$·$V$ raw 값 비교 전에 체중 표준화 (성인: 0.75/1.0, 소아: + maturation). 진짜 covariate 신호와 단순 체격 효과를 분리하는 게이트.

---

## §7. 자기 테스트 (9문항)

### Q1 [회상 ★★] $t_{1/2}$를 $V$, $CL$로 표현하고 왜 "이차"인지 설명

$$
\underbrace{t_{1/2}}_{\text{반감기}}=\frac{\underbrace{0.693\cdot V}_{\text{}}}{\underbrace{CL}_{\text{}}}
$$

$t_{1/2}$만으로 $CL$ 감소인지 $V$ 증가인지 구분 불가. **다른 두 변수가 만들어낸 표지값**이라는 게 "이차"의 진짜 뜻. [G&W p.17–18]

### Q2 [회상 ★] $V$의 정의식 두 가지

$$
\underbrace{V}_{\text{환산공간}}=\frac{\underbrace{A_b}_{\text{체내총량}}}{\underbrace{C}_{\text{측정농도}}},\qquad \underbrace{V}_{\text{IV용적}}=\frac{\underbrace{D_{iv}}_{\text{}}}{\underbrace{C^0}_{\text{}}}
$$

말단 정보 있으면 $V=CL/K=1.44\cdot CL\cdot t_{1/2}$. [G&W p.20]

### Q3 [회상 ★] $C_{ss}=R_{in}/CL$ 도출

$$
\underbrace{\frac{dC}{dt}}_{\text{}}=\underbrace{\frac{R_{in}}{V}}_{\text{}}-\underbrace{\frac{CL}{V}C}_{\text{}}\xrightarrow{dC/dt=0}\underbrace{C_{ss}=\frac{R_{in}}{CL}}_{\text{}}
$$

$V$가 사라짐. **$V$는 도달 시간엔 영향, 최종 $C_{ss}$엔 영향 없음.** [G&W p.22–23]

### Q4 [회상 ○] $MRT$ 정의와 1구획 IV와의 관계

$$
\underbrace{MRT}_{\text{}}=\frac{\underbrace{AUMC}_{\text{}}}{\underbrace{AUC}_{\text{}}},\qquad \underbrace{MRT_{\text{1구획IV}}}_{\text{}}=\frac{1}{K}=1.443\cdot t_{1/2}
$$

두 번째 등식은 **1구획 IV bolus 한정**.

### Q5 [적용 ★★] S1·S4에 같은 $R_{in}=10$ µg/min — $C_{ss}$ 같음?

$$
C_{ss,1}=\frac{10}{0.1}=\mathbf{100}\;\mu g/L,\qquad C_{ss,4}=\frac{10}{0.2}=\mathbf{50}\;\mu g/L
$$

**두 배 차이.** $K$·$t_{1/2}$ 비슷해도 $C_{ss}$는 $CL$이 정함. **이게 §1 함정의 결정적 숫자임.** [G&W Eq.2:22, p.23]

### Q6 [적용 ★★] $t_{1/2}$ 늘었음 — $CL\downarrow$ vs $V\uparrow$ 어떻게 분리함?

**AUC와 $C^0$ 분리해서 봄**:
- $CL\downarrow$ → $AUC=Dose/CL\uparrow$
- $V\uparrow$ → $C^0=D/V\downarrow$

둘 다 변하면 $t_{1/2}$ 하나로는 분리 불가. [R&T p.58–60]

### Q7 [적용 ★] R&T midazolam: 79 kg, 7.5 mg IV, AUC = 287 µg·hr/L, $t_{1/2}=3.8$ hr. (a) $CL$? (b) $V$? (c) 5분 농도 180 µg/L, 혈장 부피 3.4 L이면 혈장 밖 분율?

$$
CL=\frac{7500}{287}\approx \mathbf{26}\;L/hr
$$

$$
V=1.44\times 26\times 3.8\approx \mathbf{142}\;L
$$

혈장 내 약물 = $180\times 3.4=612$ µg = 0.612 mg. 혈장 밖 = $7.5-0.612=6.89$ mg = **약 92%**. 5분 만에 조직으로 빠르게 분포한다는 직접 증거. [R&T p.61–63]

### Q8 [적용 ★] IV bolus 자료 $MRT/t_{1/2}=1.85$. 무엇을 의심함?

1구획 IV bolus 단일지수 가정 위배. **분포 동력학** 또는 **말단 외삽 품질** 문제 의심. 본 세션 출처 범위 결론은 여기까지, 구체적 NONMEM ADVAN 선택은 후속 실무 판단. [G&W p.19; R&T p.60–66]

### Q9 [Boss Dilemma ★★] 새 IV 약물 반로그 도표 biphasic — 1구획 vs 2구획 어떻게 방어함?

질문 자체가 잘못됨. "어느 모델이 항상 옳음?"이 아니라 **"분포 단계가 임상적으로 중요한 시간대임?"**임.

$$
\underbrace{\text{말단 = 소실 대표}}_{\text{1구획 안전}}\;\Leftrightarrow\;\underbrace{\text{분포 단계 AUC 비율 작음}}_{\text{midazolam (\approx 48\%) OK}}\;\;\text{vs}\;\;\underbrace{\text{비율 매우 큼}}_{\text{gentamicin: > 95\% 신배설 (분포 평형 전)}}
$$

방어 시 함께 제시할 두 가지:
1. **분포 단계 AUC 비율**
2. **임상 의사결정 시점이 분포 단계인가 소실 단계인가**

[R&T p.61–66, Fig.3-5·3-6·3-7]

> **§7 정리**: 계산 문제 핵심은 수식 암기가 아니라 **"어떤 식에서 어떤 파라미터가 사라지는가"**임. $C_{ss}$에선 $V$가 사라지고, $t_{1/2}$엔 $CL$·$V$가 함께 남음. 이 사라짐과 남음의 패턴이 임상 결정의 일차 좌표를 알려줌.

---

## §8. 메타프레임 — 이 세션이 PK/PD 그래프에서 차지하는 위치

### A. 위치 — 모든 후속 구조의 출발점

이 세션은 PK/PD 학습 그래프의 **루트 노드**임. 후속 모든 가지가 여기서 갈라짐:

| 후속 세션 | 이 세션에서 열린 개념 | 이 세션 없으면 실패하는 것 |
|---|---|---|
| 다구획 모델 | 말단 단계가 소실 대표인지 판정 | terminal slope 자동 신뢰 |
| 흡수 모델 | 혈관외 말단 기울기의 정체 ($K$ vs $K_a$) | flip-flop 혼동 |
| 간/신 청소율 | $CL=Q\cdot E$, $CL_R=f_e\cdot CL$ 분해 | 장기별 생리학 연결 실패 |
| PopPK 공변량 | $CL$ vs $V$ 위치 배치 | $K$ 직접 모수화로 원인 혼재 |
| NCA | $AUC$, $AUMC$, $MRT$ 모멘트 해석 | 평균체류 vs 반감기 혼동 |
| **NCA 보고 품질 (§6 M1)** | 말단 BLQ + % AUC extrapolated | $K$·$CL$ 사슬 신뢰도 손실 |
| **PopPK BLQ likelihood (§6 M1)** | Beal M3 censoring | BLQ 큰 자료에서 추정 편향 |
| **성인 PopPK covariate (§6 M2)** | $CL\propto BW^{0.75}$, $V\propto BW^{1.0}$ | 체격 효과와 진짜 신호 혼재 |
| **소아 PopPK (§6 M2)** | size × maturation + PMA $F_{mat}$ | 신생아 $CL$ 과대추정 |

### B. 대충 넘기면 실제로 일어나는 7가지 실패

1. **$t_{1/2}$ 단독 해석** — "긴 반감기 = 신기능 저하" 자동 결론 → 부종 환자 ($V\uparrow$) 놓침. 정답: **AUC·$C^0$ 함께 봄**.
2. **$V$를 해부학적 부피로 오해** — Quinacrine 40,000 L 보고 "모델 틀림" 결론. 정답: $V$는 **혈장 측정 농도와 총량의 환산률**.
3. **말단 단계 자동 신뢰** — gentamicin trap (95% 신배설이 깊은 조직 분포 평형 (≈36 hr) 도달 전). 정답: **분포 단계 AUC 비율 확인**.
4. **$K$ 직접 모수화** — TRANS1로 공변량을 $K$에 붙임. $CL/V$ 분리 불가. 정답: **TRANS2로 $CL$·$V$ 분리**.
5. **BLQ 무시 (§6 M1)** — 말단 0 치환 → $K\uparrow\to t_{1/2}\downarrow\to AUC\downarrow\to CL\uparrow$ 사슬 폭발. 정답: **NCA 위치별 규칙 + PopPK M3, % AUC extrapolated 함께**.
6. **체중 표준화 누락 (§6 M2)** — raw $CL$·$V$ 비교 → 체격 효과와 covariate 신호 혼재. 정답: **0.75 / 1.0 표준 출발**.
7. **소아 maturation 누락 (§6 M2)** — 체중만 ¾제곱 → 신생아 $CL$ 과대. 정답: **size × maturation 분리 + PMA**.

### C. 전문가가 만드는 차이

자동화 도구는 단일지수 적합으로 $CL$·$V$·$K$·$t_{1/2}$ 출력은 빠르게 함. **전문가의 가치는 숫자 출력이 아니라 숫자의 위계를 읽는 것**임:

- $C_{ss}$가 다른 이유를 $t_{1/2}$가 아니라 $CL$에서 찾음
- $t_{1/2}$ 변화 시 $CL$·$V$ 먼저 분해
- 반로그 말단 직선이 언제 소실 대표가 아닌지 앎
- 출처 기반 진술과 실무 인사이트를 구분

### D. 임상 결정 좌표 한 장 요약

| 변화 | 일차 파라미터 | 임상 결과 | 조치 |
|---|---|---|---|
| AUC·유지용량 | $CL$ | $CL$↓ 절반 → AUC 두 배 | 즉시 $CL$ 역수 계산 |
| $C^0$·부하용량 | $V$ | $V$ 불변이면 부하 수정 불요 | 부하용량은 $V$ 함수 |
| 말단 기울기 | $CL/V$ | 단독으로 결정 불가 | AUC·$C^0$ 함께 확인 |
| 잔차 패턴 | $CL$ 또는 $V$ | $K$ 모수화는 혼재 | 배수구·욕조 가설로 세움 |
| NCA $MRT$ | $AUMC/AUC$ | $V_{ss}=CL\cdot MRT$ | 구획 $V/CL$과 차이 명시 |
| CWRES vs WT/CrCl | $CL$ 또는 $V$ | 잔차 원인 위치가 모델 방어력 정함 | 공변량 위치 재검토 |

### E. 최종 한 줄

1구획 IV bolus PK는 네 식으로 마무리됨:

$$
\underbrace{CL}_{\text{노출결정}}=\frac{Dose}{AUC},\qquad
\underbrace{V}_{\text{초기농도 결정}}=\frac{D}{C^0},\qquad
\underbrace{K}_{\text{시간기울기}}=\frac{CL}{V},\qquad
\underbrace{t_{1/2}}_{\text{시간척도}}=\frac{0.693\cdot V}{CL}
$$

진짜 목표는 **식 암기가 아니라 위계 체화**임:

> **$CL$·$V$를 먼저 보고, $K$·$t_{1/2}$를 그 결과로 읽음.**

S1 vs S4가 끝까지 가르쳐준 한 줄임. 다음 세션부터는 이 위계를 다구획·흡수·간/신·PopPK 공변량으로 확장함.

---

**End of Session 01 [Remastered]**

---

C-260518-063000-7K2

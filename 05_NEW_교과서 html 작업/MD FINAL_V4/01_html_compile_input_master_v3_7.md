# 세션 01 — 1구획 IV 동력학: CL · V · t½ · K — v3.7

<!-- 기호 통일: V_max/Vmax 해당 없음 — 본 세션은 CL, V, K, t_{1/2}, MRT 표기를 첫 등장 기준으로 유지 -->
<!-- 기호 통일: C0 → C^0 (원문 첫 등장 표기 기준) -->

**Source:** Gabrielsson & Weiner 5e Ch.2 §2.2.1–2.2.5 + Case Study PK1 / Rowland & Tozer 5e Ch.3  
**Pages:** G p.14–32, p.469–475 / R&T p.53–76  
**Mode:** A-Critical  
**Learner:** 계량약리학 박사과정, PopPK 입문–중급  
**그림 권한 안내(Figure rights note):** 이 자료에는 교과서 그림을 직접 수록하지 않습니다. `FIGURE_POINTER` 마커는 학습자가 참고해야 할 교과서 그림을 안내합니다. `FIGURE_SCHEMATIC` 마커는 원본 그림을 복제하지 않고 새로 설계할 도식의 요약(brief)을 기술합니다.



> **임상 장면 — 같은 $K$, 다른 결정**  
> Compound A 10 mg IV bolus 자료에서 Subject 1과 Subject 4는 모두 $K\approx0.01\;\mathrm{min^{-1}}$처럼 보입니다. 그러나 Subject 1은 $V=10$ L, $CL=0.1$ L/min이고 Subject 4는 $V=20$ L, $CL=0.2$ L/min입니다. 같은 기울기로 보인 두 환자는 실제로 유지용량과 부하용량의 결정 좌표가 갈라집니다. [G p.473–474]

## 학습 내비게이션 안내

### 이 자료 사용법

1. §1을 한 번 읽으면서 파라미터 위계를 먼저 고정하면 됩니다. $CL$과 $V$가 일차 파라미터(primary parameter)이고, $K$, $t_{1/2}$, 1구획 $MRT$는 이 둘로부터 파생됩니다.
2. §2는 카드 순서대로 학습하면 됩니다. C1과 C2는 건너뛰지 않는 것이 좋습니다. 이후의 모든 시간 파라미터가 이 두 카드에 의존하기 때문입니다.
3. Figure pointer가 나오면 계속 읽기 전에 해당 교과서 그림을 먼저 확인하면 됩니다. 이 마커는 장식용 주석이 아니라 학습 경로의 일부입니다.
4. §7 자기 테스트를 하기 전에 §5를 통해 주요 혼동 쌍을 먼저 능동적으로 구분해 보세요.
5. §8은 최종 전문가 시각으로 활용하면 됩니다. 숫자를 해석하기 전에 파라미터 위계부터 읽어야 합니다.

### 학습 순서

`§1 로드맵 → C1 청소율 → C2 분포용적 → C3 K → C4 반감기 → C5 MRT → §5 혼동쌍 → §7 자기 테스트 → §8 메타프레임`

### 시작 전 / 완료 후 체크포인트

| 체크 항목 | 시작 전 | 완료 후 |
|---|---|---|
| 파라미터 위계 | $CL$과 $V$가 일차(primary)인 이유를 말할 수 있는가? | $K$와 $t_{1/2}$가 이차(secondary)인 이유를 암기 문구 없이 설명할 수 있는가? |
| 노출량(Exposure) 대 시간 | AUC, $C^0$, 기울기(slope), $C_{ss}$를 구분할 수 있는가? | 각각을 결정하는 파라미터를 지목할 수 있는가? |
| 겉보기 용적(Apparent volume) | $V$가 해부학적 부피가 아닌 이유를 말할 수 있는가? | 매우 큰 $V$를 실제 체적으로 오해하지 않고 해석할 수 있는가? |
| 말단 기울기(Terminal slope) | 반로그 말단 기울기(semilog terminal slope)를 정의할 수 있는가? | terminal slope가 전체 소실(elimination)을 안전하게 대표하지 못하는 조건을 말할 수 있는가? |
| NCA 연결 | $MRT$를 정의할 수 있는가? | $MRT=1/K=1.443\cdot t_{1/2}$가 1구획 IV bolus에서만 성립하는 이유를 설명할 수 있는가? |

$$
\underbrace{MRT}_{\text{평균체류}}=\frac{1}{\underbrace{K}_{\text{분율속도}}}=\underbrace{1.443}_{1/\ln2}\cdot\underbrace{t_{1/2}}_{\text{반감기}}
$$


---


<!-- SLIDE_START: §1 | title: §1 세션 헤더와 로드맵 -->

## §1 — 세션 헤더와 로드맵


**핵심 아이디어(Big Idea):** $CL$과 $V$는 약물 체내 처리(disposition), 즉 분포와 소실을 묶은 체내 처리 과정을 결정하는 두 일차 좌표(primary coordinate)입니다. $K$와 $t_{1/2}$는 그 좌표가 만든 시간 그림자입니다. 다시 말해, 관찰되는 기울기(slope)와 반감기(half-life)는 원인이 아니라 결과입니다. 그림자($K$, $t_{1/2}$)만 보고 원인이 $CL$인지 $V$인지 단정하면 유지용량, 부하용량, 공변량 위치가 모두 틀릴 수 있습니다. [G p.17; R&T p.58]

```
IV bolus, 1-cmt, first-order
        │
        ├── Primary:  CL  ──┐
        │                   ├── K = CL/V ── t½ = ln(2)/K = 0.693V/CL
        └── Primary:  V   ──┘

Exposure/AUC  ← governed by CL
Initial concentration C0 ← governed by V
Mean residence time MRT ← 1/K only in 1-cmt IV bolus
```

$$
\underbrace{K}_{\text{시간기울기}}=\frac{\underbrace{CL}_{\text{정화능}}}{\underbrace{V}_{\text{분포공간}}},\qquad
\underbrace{t_{1/2}}_{\text{반감기}}=\frac{\underbrace{\ln 2}_{\text{절반조건}}}{\underbrace{K}_{\text{분율속도}}}=\frac{\underbrace{0.693}_{\ln 2}\cdot\underbrace{V}_{\text{분포공간}}}{\underbrace{CL}_{\text{정화능}}}
$$


R&T의 도입 그림(opening figures)은 이 구조를 가장 빠르게 보여 줍니다. Drugs A/B는 같은 초기 농도에서 출발하지만 기울기와 AUC가 다릅니다. 반대로 Drugs C/D는 같은 반감기(half-life)를 보이지만 초기 농도와 AUC가 다릅니다. 즉, "처음 높이"와 "기울기"는 같은 정보가 아닙니다. 서로 다른 일차 결정인자(primary determinant)가 표면에 드러난 모습입니다. [R&T p.54–55]

이 세션에서는 다음 다섯 카드만 고정합니다: **C1 청소율(Clearance) → C2 분포용적(Volume) → C3 소실속도상수(Elimination Rate Constant) → C4 반감기(Half-life) → C5 MRT**.

**선행:** 1차 ODE, 자연로그, 혈장/혈액/조직 구분.  
**후속:** 다구획 동력학(multi-compartment kinetics), 흡수 모델(absorption models), 간/신 청소율(hepatic/renal clearance), 집단약동학(PopPK, population pharmacokinetics) 공변량 모델링(covariate modeling), NCA 모멘트 분석(moment analysis).

---


> 📖 **교과서 그림 참조:** [Rowland & Tozer 5e, p.54, Fig.3-1; p.55, Fig.3-2]
> 같은 용량(dose)에서 "초기 농도", "기울기", "AUC"가 서로 다른 정보를 담는다는 사실을 한 번에 분리해 보여 줍니다. 이 그림이 없으면 학습자가 $C^0$, 기울기(slope), AUC를 하나의 노출 지표처럼 뭉뚱그려 읽을 위험이 큽니다.
> 확인 시점: §1 로드맵을 읽은 뒤에 확인하면 됩니다.


> **전문가 보강(Mastery Augmentation) — [CRUCIBLE_DERIVED]**  
> 이 핸드아웃의 판정 순서는 간단합니다. 노출량·유지용량 질문은 먼저 $CL$로, 초기농도·부하용량 질문은 먼저 $V$로, 시간축 질문은 $CL/V$ 또는 $V/CL$ 조합으로 되돌려 읽으면 됩니다. 이 순서가 지켜져야 기울기와 반감기가 원인처럼 보이는 착시를 피할 수 있습니다.



### ASCII 레이어 개념 지도

```text
Layer 1 — 무엇인가
  CL = 정화 능력        V = 환산 공간        K/t½/MRT = 시간 표지

Layer 2 — 어떻게 계산되는가
  CL = Dose/AUC        V = D/C^0            K = CL/V
  t½ = 0.693·V/CL      MRT = AUMC/AUC       (1-cmt IV bolus: MRT = 1/K)

Layer 3 — 언제, 왜 중요한가
  유지용량·AUC → CL    부하용량·C^0 → V     시간축·채혈창 → CL/V 또는 V/CL
  공변량 위치 → CL vs V 분리                  규제 방어 → 원인 좌표 보존
```

🧭 **읽는 순서:**  
카드 1 (C1): 노출량과 유지용량을 정말로 결정하는 것은 기울기인가, 청소율인가?  
카드 2 (C2): 분포용적은 왜 실제 체적이 아니라 농도 환산률인가?  
카드 3 (C3): 반로그 기울기 $K$는 왜 독립 소실 능력이 아니라 $CL/V$인가?  
카드 4 (C4): 반감기가 길어졌을 때 왜 $CL$ 감소와 $V$ 증가를 분리해야 하는가?  
카드 5 (C5): $MRT$는 왜 반감기의 단순 변형이 아니라 시간가중 평균인가?

### 지식 그래프 위치

```text
[선행 세션: 1차 ODE · 자연로그 · 혈장/조직 구분]
        → [이 세션: CL · V · K · t½ · MRT의 위계]
        → [후속 세션: 다구획 · 흡수 · 간/신 청소율 · PopPK 공변량 · NCA 모멘트]
```

<!-- SLIDE_START: §2 | title: §2 개념 해부 카드 -->

## §2 — 개념 해부 카드


<!-- SLIDE_START: C1 | title: C1 청소율 -->

### 🃏 C1. 청소율(Clearance, $CL$) [⚡ Apex Concept]

> **거장의 시각**
> 💢 **흔한 오해:** $CL$을 농도가 내려가는 속도나 $K$와 같은 시간 기울기로 읽습니다.
> ✅ **실제는:** $CL$은 단위 시간당 완전히 비워지는 가상의 혈장/혈액 부피이며, AUC·$C_{ss}$·유지용량을 직접 지배합니다.
> 🎯 **체화할 단 하나의 직관:** 기울기는 그림자이고, 정화 능력의 원인 좌표는 $CL$입니다.

#### A. 형식적 정의(Formal Definition)

**청소율(Clearance, $CL$; ← 정화 능력):** 단위 시간당 혈장 또는 혈액에서 약물이 완전히 제거되는 겉보기 용적(apparent volume)입니다. 단위는 유속 단위(flow unit)입니다. [G p.16; R&T p.56]

$$
\underbrace{\text{Rate of elimination}}_{\text{제거속도}}=\underbrace{CL}_{\text{정화부피/시간}}\cdot\underbrace{C}_{\text{현재농도}} \qquad [\text{R\&T Eq.3-4, p.56; G Eq.2:2, p.16}]
$$


$$
\underbrace{CL}_{\text{정화부피/시간}}=\underbrace{Q}_{\text{혈류(운반)}}\cdot\underbrace{E}_{\text{추출분율}} \qquad [\text{R\&T Eq.3-5, p.56}]
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $CL$ | 용적/시간 | 혈장/혈액에서 약물이 완전히 제거되는 겉보기 유량 | 혈류, 추출, 대사·배설 경로 |
| $Q$ | 용적/시간 | 장기로 약물을 운반하는 혈류량 | 장기 혈류 변화 |
| $E$ | 무차원 분율 | 장기 통과 중 제거되는 비율 | 효소·수송체·배설능 변화 |
| $C$ | 농도 | 현재 측정 공간의 약물 농도 | 투여량, 분포, 소실 진행 |

💡 **유량 구조가 핵심** — $CL=Q\cdot E$는 속도 공식이 아니라 “얼마나 많은 혈액이 지나가고, 그중 얼마를 빼내는가”를 곱한 식입니다.



#### B. 용량, AUC, 그리고 항정상태


AUC는 시간 전체에 걸친 노출 적분(exposure integral), 즉 농도-시간 곡선 아래 면적입니다. 1차 IV bolus에서는 제거된 총량이 $CL\cdot AUC$로 표현됩니다. 전체 용량(dose)이 결국 제거되므로 다음 관계가 성립합니다. [G p.19; R&T p.59–60]

$$
\underbrace{CL}_{\text{정화부피/시간}}=\frac{\underbrace{Dose}_{\text{투여량}}}{\underbrace{AUC_0^\infty}_{\text{총노출}}}
$$


일정 속도 주입(constant infusion)에서는 다음과 같습니다.

$$
\underbrace{\frac{dC}{dt}}_{\text{농도변화}}=\underbrace{\frac{R_{in}}{V}}_{\text{입력/V}}-\underbrace{\frac{CL}{V}C}_{\text{제거/V}}
$$


항정상태에서 $dC/dt=0$이므로 다음과 같습니다.

$$
\underbrace{C_{ss}}_{\text{항정농도}}=\frac{\underbrace{R_{in}}_{\text{주입속도}}}{\underbrace{CL}_{\text{정화능}}} \qquad [\text{G Eq.2:22, p.23}]
$$


여기서 $V$가 소거됩니다. $V$는 항정상태에 도달하는 **속도**를 바꾸지만, 동일 주입속도(infusion rate)에서 최종 $C_{ss}$는 $CL$이 결정합니다. [G p.22–23]


#### C. Compound A 기준 데이터

Gabrielsson Case Study PK1은 4명에게 Compound A 10 mg IV bolus를 투여한 출처 기반(source-bound) 계산 기준점입니다. [G p.469–475]

| Subject | Sex | $K$ (min⁻¹) | $V$ (L) | $CL$ (L/min) | $AUC$ (µg·min·L⁻¹) |
|---|---:|---:|---:|---:|---:|
| 1 | M | 0.01 | 10 | 0.1 | 98,000 |
| 2 | M | 0.02 | 9.8 | 0.2 | 49,000 |
| 3 | F | 0.02 | 10 | 0.2 | 51,000 |
| 4 | F | 0.01 | 20 | 0.2 | 51,000 |

[Source: G Tables 1.2/1.3, p.473–474]

💡 **비유:** 같은 속도로 물 높이가 내려가도 욕조 크기와 배수구 크기가 동시에 달라지면 실제 배수 능력은 다릅니다. Compound A의 Subject 1과 4가 바로 그 경우입니다.

**정정된 핵심:** Subject 1과 4는 $K$와 $t_{1/2}$가 비슷하지만 $CL$은 2배 다릅니다. S1은 $CL=0.1$ L/min, S4는 $CL=0.2$ L/min입니다. S4에서는 $V$도 동일 비율로 커져 있어 $K=CL/V$가 우연히 보존된 결과입니다. 따라서 같은 $R_{in}$에서 두 사람의 $C_{ss}$는 절반 차이가 납니다(§7 Q5에서 정량 확인). $K$와 $t_{1/2}$만 보고 "두 사람이 같은 약물 처리 능력을 가졌다"고 읽는 것이 이 세션 전체의 핵심 함정입니다. [G p.473–474; G Eq.2:22, p.23]

#### D. 경계 및 압축

| 이 카드에서 다루는 것 | → | 후속 세션으로 이월 | 이유 |
|---|---|---|---|
| $CL=Q\cdot E$의 기본 구조 | → | 고추출/저추출 약물, 장기별 간·신 청소율 모델 | 이 카드는 $CL$의 원인 좌표만 고정합니다. [R&T p.56] |
| 혈관외 투여에서의 겉보기 파라미터 | → | $K_a$, $F$, $t_{lag}$ | 흡수와 생체이용률은 별도 세션의 핵심입니다. [G p.28–32] |
| $CL_R=f_e\cdot CL$ | → | 신장 기여분 분해 | 여기서는 신장 기여분의 방향만 유지합니다. [R&T p.66–68] |


> 💼 **실무 인사이트:** NONMEM에서 공변량을 $K$에 직접 묶으면 $CL$ 변화와 $V$ 변화가 한 항에 섞입니다. `TRANS2`처럼 $CL$과 $V$를 분리해 두는 이유는 통계적 편의가 아니라 인과 위치 보존입니다.


**C1 요약(Recap):** $CL$은 노출량과 유지용량을 결정하는 일차 소실 파라미터(primary elimination parameter)입니다. $t_{1/2}$이나 $K$가 아니라 $CL$을 먼저 물어야 합니다.



**Plausible Fallacy — 나비효과 연쇄 [EXPERT_INFERENCE, v3]**

**오류:** Compound A에서 Subject 1과 Subject 4의 $K$가 같으면 두 피험자의 소실 능력도 같다고 판단한다.  
**왜 그럴싸한가:** 반로그 도표에서는 두 피험자의 말단 기울기가 비슷하게 보이고, $K$는 제거 속도처럼 보이기 때문이다.  
**나비효과:** $K$ 동일성만 보고 $CL$ 동일성으로 해석 → Subject 1($CL=0.1$ L/min)과 Subject 4($CL=0.2$ L/min)의 유지용량 차이를 놓침 → [임상] 같은 $R_{in}$에서 $C_{ss}$ 차이를 미예측 → [모델링/규제] $K$ 공변량 모델로 $CL$·$V$ 원인 분리가 실패하고 신기능/체중 잔차 패턴을 설명하지 못해 재분석 요구 가능.


> **C1 체화 핵심**
> ① `AUC·$C_{ss}$·유지용량 질문` → $CL$이 결정
> ② `같은 $K$라도 다른 Subject 1 vs 4` → $CL$과 $V$가 동시에 달라질 수 있음
> ⚡ `$K$ 같음 = 소실 능력 같음` → 유지용량과 공변량 위치가 함께 틀림
<!-- 편집 주: [E] Apex 카드라 Plausible Fallacy와 Compound A 수치 anchor를 보존하기 위해 4줄 구성으로 압축 -->

---


> 📖 **교과서 그림 참조:** [Rowland & Tozer 5e, p.55, Fig.3-3]
> 저장소-추출기 도식(reservoir-extractor diagram)은 $Q$, $E$, $C$, $C_{out}$이 어떻게 연결되어 $CL=Q\cdot E$가 되는지 시각적으로 고정해 줍니다. 텍스트만 읽으면 $CL$을 단순 기울기(slope)나 제거 속도로 오해하기 쉽습니다.
> 확인 시점: C1 청소율(Clearance) 카드를 읽은 뒤에 확인하면 됩니다.

$$
\underbrace{CL}_{\text{정화부피/시간}}=\underbrace{Q}_{\text{흐름부피/시간}}\cdot\underbrace{E}_{\text{추출분율}},\qquad
\underbrace{Q\cdot C}_{\text{유입량/시간}}\cdot\underbrace{E}_{\text{추출분율}}
$$


> **전문가 보강(Mastery Augmentation) — [CRUCIBLE_DERIVED]**  
> $CL=Dose/AUC$에서 $V$가 사라진다는 사실은 암기용 공식이 아니라 유지용량 판단의 구조입니다. 분포공간은 곡선의 출발점과 시간상수를 바꾸지만, 전체 투약 사건을 적분하면 노출-용량 변환의 중심에는 $CL$만 남습니다.


<!-- SLIDE_START: C2 | title: C2 분포용적 -->

### 🃏 C2. 분포용적(Volume of Distribution, $V$)

> **앞 카드에서 이 카드로:** C1이 AUC와 유지용량의 원인 좌표를 $CL$로 고정했다면, C2는 초기농도와 부하용량의 원인 좌표를 $V$로 분리합니다.

> **거장의 시각**
> $V$를 실제 해부학적 부피로 읽으면 quinacrine처럼 큰 값이나 낮은 초기농도를 모델 오류로 오판합니다.
> $V$를 체내 총량과 측정 농도 사이의 환산률로 읽으면 부하용량과 $C^0$ 해석이 즉시 정리됩니다.

#### A. 형식적 정의(Formal Definition)

$$
\underbrace{V}_{\text{환산공간}}=\frac{\underbrace{A_b}_{\text{체내총량}}}{\underbrace{C}_{\text{측정농도}}} \qquad [\text{G Eq.2:14, p.20; R\&T Eq.3-26, p.63}]
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $V$ | 용적 | 체내 총량을 측정 농도로 환산하는 겉보기 공간 | 조직 결합, 측정 공간, 체성분 변화 |
| $A_b$ | 질량 | 체내에 존재하는 총 약물량 | 투여량, 분포 진행, 제거 진행 |
| $C$ | 농도 | 혈장/혈액 등 측정 공간의 농도 | 조직 분배, 결합, 시점 |
| $C^0$ | 농도 | IV bolus 직후 외삽 초기농도 | 용량과 초기 분포공간 |

⚠️ **헷갈림 방지:** 큰 $V$는 큰 몸통이 아니라 낮게 보이는 측정 농도입니다. 실제 체적처럼 읽으면 부하용량 판단이 흔들립니다.



IV bolus에서는 역외삽 절편(back-extrapolated intercept)으로 다음을 계산합니다.

$$
\underbrace{V}_{\text{초기희석공간}}=\frac{\underbrace{D_{iv}}_{\text{IV 용량}}}{\underbrace{C^0}_{\text{외삽초기농도}}} \qquad [\text{G Eq.2:13, p.20}]
$$


R&T는 시간 0 외삽(time-zero extrapolation)만으로 $V$를 확신하기 어려운 상황을 지적합니다. 분포 평형이 완성되기 전의 절편은 실제 분포공간을 안정적으로 대표하지 못할 수 있기 때문입니다. 그래서 말단 단계(terminal phase)에서 $CL$과 $k$로 $V$를 구하는 우회식을 제시합니다. [R&T p.63]

$$
\underbrace{V}_{\text{말단용적}}=\frac{\underbrace{CL}_{\text{정화능}}}{\underbrace{K}_{\text{말단기울기}}}=\underbrace{1.44}_{1/\ln 2}\cdot\underbrace{CL}_{\text{정화능}}\cdot\underbrace{t_{1/2}}_{\text{반감기}} \qquad [\text{R\&T Eq.3-27/3-28, p.63}]
$$


#### B. 겉보기 분포용적이 거대해질 수 있는 이유

Gabrielsson은 $V$를 비결합 용적(unbound volume)과 유리 분율(free fraction)로 분해합니다. [G p.20]

$$
\underbrace{V}_{\text{관찰용적}}=\underbrace{V_u}_{\text{비결합용적}}\cdot\underbrace{f_u}_{\text{유리분율}} \qquad [\text{G Eq.2:15, p.20}]
$$


조직 분배(tissue partition)까지 고려하면 $V_{ss}$는 혈액 부피와 조직별 분배계수의 합으로 표현됩니다. [G Eq.2:16–2:18, p.20–21]

$$
\underbrace{V_{ss}}_{\text{항정분포용적}}=\underbrace{V_B}_{\text{혈액부피}}+\sum \underbrace{V_{Ti}}_{\text{조직부피}}\cdot\underbrace{K_{Pi}}_{\text{조직분배}}\cdot\underbrace{(1-E_{Ti})}_{\text{잔류분율}}
$$


Quinacrine의 $V=40{,}000$ L는 겉보기 분포용적(apparent volume)의 극단값입니다. 이 값은 실제 체적이 아니라 조직 결합(tissue binding)과 측정 공간(measurement space)의 불일치를 흡수한 환산률로 읽어야 합니다. [G p.20]

#### C. Compound A 기준 데이터

Compound A에서 Subject 1–3의 $V$는 약 10 L이고, Subject 4는 20 L입니다. Gabrielsson Fig.1.2는 Subject 4의 낮은 절편(intercept)이 더 큰 용적(volume)을 의미한다고 설명합니다. [G p.470, p.473]


$V$가 커지면 동일 용량(dose)에서 $C^0=D/V$가 낮아집니다. 그러나 $V$만으로 AUC가 결정되지는 않습니다. AUC는 $CL$이 결정합니다. [G Fig.2.6, p.17; G Fig.2.12, p.26–27]

#### D. 경계 및 압축

| 이 카드에서 다루는 것 | → | 후속 세션으로 이월 | 이유 |
|---|---|---|---|
| 1구획에서의 $V$ | → | $V_c$, $V_{ss}$, terminal $V_z$ | 다구획에서는 용적 정의가 목적별로 분기됩니다. [G p.20–21; R&T p.61] |
| $V$ 기반 부하용량 | → | 분포 단계가 충분히 빠른지의 판단 | 분포가 느리면 초기 절편과 임상 목표농도 연결이 흔들립니다. [R&T p.62–64] |


> 💼 **실무 인사이트:** 반로그 도표(semi-log plot)에서 명백한 꺾임점(break point)이 보이면, 1구획 $V$를 곧바로 부하용량(loading dose)에 쓰기 전에 중심 구획 용적(central volume) 대 항정상태 용적(steady-state volume) 문제를 점검합니다.


**C2 요약(Recap):** $V$는 "약물이 어디에 얼마나 숨어 있는가"를 혈장 농도 하나로 환산한 겉보기 파라미터(apparent parameter)입니다. $C^0$와 부하용량(loading dose)에는 직접적이지만, 유지 노출량(maintenance exposure)은 $CL$이 결정합니다.


> **C2 체화 핵심**
> ① `동일 용량에서 $C^0$가 낮을 때` → $V$가 결정
> ② `큰 $V$ vs 실제 큰 체적` → 겉보기 환산공간과 해부학적 부피를 분리
> ⚡ `$V$를 실제 부피로 해석` → 부하용량과 분포 단계 판단 실패

---


> 📖 **교과서 그림 참조:** [Gabrielsson & Weiner 5e, p.15, Fig.2.3]
> 두 양동이(bucket)의 실제 물 부피가 같아도 측정 농도 차이 때문에 겉보기 용적(apparent volume)이 10 L와 100 L로 달라지는 장면을 보여 줍니다. 이 그림이 없으면 $V$를 실제 해부학적 부피로 오해하기 쉽습니다.
> 확인 시점: C2 분포용적(Volume of Distribution) 카드를 읽은 뒤에 확인하면 됩니다.


> **전문가 보강(Mastery Augmentation) — [AUDIT_DERIVED]**  
> $V$가 매우 크다는 말은 "몸 안에 실제로 그만한 부피가 있다"는 뜻이 아닙니다. 측정 공간(plasma)에서 보이는 농도가 낮아졌기 때문에 총량을 그 농도로 환산한 겉보기 공간(apparent space)이 커진 것입니다.


<!-- SLIDE_START: C3 | title: C3 소실속도상수 -->

### 🃏 C3. 소실속도상수(Elimination Rate Constant, $K$)

> **앞 카드에서 이 카드로:** $CL$과 $V$가 각각 정화 능력과 환산 공간을 정했다면, C3의 $K$는 두 원인 좌표가 만든 시간 기울기입니다.

> **거장의 시각**
> $K$를 독립 제거 능력으로 추정하면 신기능 변화와 분포공간 변화가 한 항에 섞입니다.
> $K=CL/V$로 되돌려 읽으면 반로그 직선의 원인이 $CL$인지 $V$인지 다시 묻게 됩니다.

#### A. 형식적 정의와 ODE

$$
\underbrace{K}_{\text{제거분율/시간}}=\frac{\underbrace{CL}_{\text{정화능}}}{\underbrace{V}_{\text{분포공간}}} \qquad [\text{G p.17; R\&T Eq.3-7, p.56}]
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $K$ | 1/시간 | 단위 시간당 남은 양 중 제거되는 분율 | $CL$ 증가·감소, $V$ 증가·감소 |
| $CL$ | 용적/시간 | 정화 능력 | 신기능, 대사·배설 변화 |
| $V$ | 용적 | 분포공간/환산공간 | 체중, 수분 상태, 조직 결합 |

🔑 **원인 분해 규칙:** $K$가 변하면 먼저 $CL$ 변화인지 $V$ 변화인지 분리합니다.



$$
\underbrace{\frac{dC}{dt}}_{\text{농도변화}}=-\underbrace{K}_{\text{분율속도}}\cdot\underbrace{C}_{\text{현재농도}}=-\frac{\underbrace{CL}_{\text{정화능}}}{\underbrace{V}_{\text{분포공간}}}\cdot\underbrace{C}_{\text{현재농도}} \qquad [\text{G Eq.2:1, p.16; R\&T Eq.3-9, p.57}]
$$


적분하면 다음과 같습니다.

💡 **비유:** 지수감소는 매 시간 같은 양을 퍼내는 양동이가 아니라, 남아 있는 물의 같은 비율을 계속 퍼내는 배수구입니다.

$$
\underbrace{C}_{\text{시간 }t\text{ 농도}}=\underbrace{C^0}_{\text{초기농도}}\cdot\underbrace{e^{-K\cdot t}}_{\text{지수감소}}=\frac{\underbrace{D}_{\text{용량}}}{\underbrace{V}_{\text{분포공간}}}\cdot e^{-(\underbrace{CL}_{\text{정화능}}/\underbrace{V}_{\text{분포공간}})\cdot t} \qquad [\text{G Eq.2:4, p.17; R\&T Eq.3-10, p.58}]
$$


반로그 도표(semi-log plot)에서는 다음과 같습니다.

$$
\underbrace{\ln C}_{\text{로그농도}}=\underbrace{\ln C^0}_{\text{로그절편}}-\underbrace{K}_{\text{기울기}}\cdot\underbrace{t}_{\text{시간}}
$$


따라서 기울기(slope)는 $-K$입니다. [G Fig.2.4/2.6, p.15–17; R&T Eq.3-11, p.58]


#### B. 분율 제거의 직관

R&T Table 3-1은 $K=0.1$ hr⁻¹인 저장소(reservoir)에서 100 mg이 1시간 후 90 mg, 2시간 후 81 mg, 3시간 후 72.9 mg으로 감소하는 예를 제시합니다. 매 시간 "10 mg"이 아니라 **남아 있는 양의 10%**가 제거됩니다. [R&T p.57]

$$
\underbrace{\frac{A}{Dose}}_{\text{남은분율}}=\underbrace{e^{-K t}}_{\text{지수잔존}}=\left(\frac12\right)^{\underbrace{n}_{t/t_{1/2}}},\quad \underbrace{n}_{\text{반감기수}}=\frac{\underbrace{t}_{\text{시간}}}{\underbrace{t_{1/2}}_{\text{반감기}}} \qquad [\text{R\&T Eq.3-19, p.59}]
$$


#### C. 경계(Boundary)

| 이 카드에서 다루는 것 | → | 후속 세션으로 이월 | 이유 |
|---|---|---|---|
| 반로그 기울기로 보이는 $K$ | → | 분포 단계와 말단 단계 구분 | 초기 빠른 저하는 소실이 아니라 분포일 수 있습니다. [R&T p.61–62] |
| 혈관외 flip-flop 가능성 | → | 흡수 속도와 말단 기울기 분리 | 말단 기울기가 $K_a$를 반영할 수 있습니다. [G p.29–30] |


> 💼 **실무 인사이트:** `ADVAN1 TRANS1`에서 $K$를 직접 추정하면 적합(fit) 자체는 가능하지만, 공변량이 $CL$에 작용하는지 $V$에 작용하는지 분리하기 어렵습니다. `TRANS2`식 $CL/V$ 모수화(parameterization)는 후속 PopPK 해석 가능성을 보존합니다.


**C3 요약(Recap):** $K$는 반로그 기울기(semi-log slope)로 보이는 값이지만, 구조적으로는 $CL/V$입니다. 기울기가 변했을 때 $CL$이 변했는지 $V$가 변했는지는 별도로 판단해야 합니다.


> **C3 체화 핵심**
> ① `반로그 기울기 변화` → $K=CL/V$가 결정
> ② `$CL$ 변화 vs $V$ 변화` → 같은 $K$ 변화라도 원인 파라미터가 다름
> ⚡ `$K$를 일차 파라미터로 모델링` → 공변량 위치가 섞여 PopPK 해석 실패

---


<!-- SLIDE_START: C4 | title: C4 반감기 -->

### 🃏 C4. 반감기(Half-life, $t_{1/2}$)

> **앞 카드에서 이 카드로:** C3에서 $K$가 $CL/V$의 시간 그림자임을 고정했으므로, C4는 그 그림자를 임상적으로 가장 자주 오해하는 반감기로 전환합니다.

> **거장의 시각**
> $t_{1/2}$ 증가를 곧바로 제거 능력 저하로 해석하면 $V$ 증가나 분포 단계 문제를 놓칩니다.
> $t_{1/2}=0.693\cdot V/CL$로 보면 항정상태 도달 시간과 용량 조절 질문을 분리할 수 있습니다.

#### A. 형식적 정의(Formal Definition)

$$
\underbrace{t_{1/2}}_{\text{반감기}}=\frac{\underbrace{\ln 2}_{\text{절반조건}}}{\underbrace{K}_{\text{분율속도}}}=\frac{\underbrace{0.693}_{\ln 2}\cdot\underbrace{V}_{\text{분포공간}}}{\underbrace{CL}_{\text{정화능}}} \qquad [\text{G Eq.2:3/2:6, p.17–18; R\&T Eq.3-15/3-16, p.58}]
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $t_{1/2}$ | 시간 | 농도가 절반으로 감소하는 시간 척도 | ↑ $V$, ↓ $CL$ |
| $K$ | 1/시간 | 분율 제거 속도 | $CL/V$ 비율 변화 |
| $V$ | 용적 | 분포공간 | 부종, 체수분, 조직 결합 |
| $CL$ | 용적/시간 | 정화 능력 | 신기능·대사·배설 변화 |

⚠️ **헷갈림 방지:** 반감기는 원인 진단명이 아닙니다. $t_{1/2}$만으로는 용량 감량 여부를 결정할 수 없습니다.



같은 $CL$이라도 $V$가 다르면 $t_{1/2}$는 달라집니다. R&T의 creatinine과 inulin 예시는 이 점을 직접 보여 줍니다. [R&T p.58]

| Compound | $CL$ (L/hr) | $V$ (L) | $t_{1/2}$ (hr) | 해석 |
|---|---:|---:|---:|---|
| Creatinine | 4.5 | 42 | 6.5 | total body water에 가까운 분포 |
| Inulin | 4.5 | 16 | 2.5 | extracellular water에 가까운 분포 |

같은 $CL=4.5$ L/hr인데 $t_{1/2}$가 다른 이유는 $V$가 다르기 때문입니다. [R&T p.58]


#### B. 항정상태 도달 시간

일정 속도 주입(constant infusion)에서 항정상태 도달 정도는 반감기 단위로 표현됩니다. Gabrielsson Fig.2.8은 1 반감기 후 50%, 2 반감기 후 75%, 3 반감기 후 87.5%, 3–4 반감기 후 약 90% 도달을 보여 줍니다. [G p.22]

R&T는 6.64 반감기 후 약 99%가 제거된다고 설명합니다. [R&T p.59]


$V$는 $C_{ss}$ 자체를 바꾸지 않지만, $t_{1/2}=0.693\cdot V/CL$을 통해 항정상태 도달 시간을 바꿉니다. 따라서 유지용량(maintenance dose)과 부하용량(loading dose)의 질문은 분리해야 합니다. [G p.22–23]


#### C. 분포 단계의 한계

R&T midazolam case는 7.5 mg base IV bolus 후 반로그 농도 프로파일(semilog profile)이 이상성(biphasic)이며, 초기 약 1시간은 분포 단계(distribution phase)라고 설명합니다. 이때 5분 시점 혈장에는 0.61 mg만 있고, 7.5 mg 중 6.9 mg, 즉 92%가 혈장 밖으로 분포되어 있습니다. [R&T p.61–62]

R&T Fig.3-5는 2시간까지 AUC가 전체 AUC의 48%라고 제시합니다. Fig.3-6은 분포와 소실의 속도 경쟁을 두 시나리오로 설명합니다. Midazolam처럼 분포가 소실보다 빠르고 분포 단계 동안 누적 AUC가 전체의 절반 정도에 머물면 말단 단계가 소실을 대표하기 쉽습니다. [R&T p.64–65]

반대로 gentamicin은 말단 단계 도달 전 대부분의 소실이 이미 발생합니다. R&T는 gentamicin IV dose의 95% 초과가 분포 평형(distribution equilibrium) 전에 소변으로 제거된다고 설명합니다. 이 경우 말단 단계를 곧바로 "소실 전체의 대표"로 읽으면 안 됩니다. [R&T p.66]


결국 *분포 단계 AUC 대 전체 AUC의 비율* 하나가 모델 단순화의 가능성을 결정합니다. Midazolam처럼 50% 부근이면 1구획 근사가 일부 임상 목적에서 안전하고, gentamicin처럼 95%가 분포 단계 동안 빠져나가면 말단 기울기(terminal slope)를 소실 대표값으로 쓰는 것 자체가 위험합니다. [R&T p.64–66]


> 💼 **실무 인사이트:** 말단 기울기(terminal slope)는 "마지막 직선"이 아니라 "분포 단계 오염이 충분히 작아진 뒤의 직선"으로 잡아야 합니다. 최소 데이터 포인트 수, 회귀 품질(regression quality), AUC 분율(fraction)을 함께 점검합니다.


**C4 요약(Recap):** $t_{1/2}$가 길어졌다는 말은 원인 진단이 아닙니다. 반드시 "$CL$ 변화인가, $V$ 변화인가, 분포 단계 문제인가"를 되물어야 합니다.


> **C4 체화 핵심**
> ① `항정상태 도달 시간·채혈창` → $t_{1/2}=0.693\cdot V/CL$이 결정
> ② `$t_{1/2}$ 증가` → $CL$ 감소인지 $V$ 증가인지 분리해야 함
> ⚡ `긴 반감기 = 신기능 저하` → 불필요한 용량 감량 또는 분포 단계 오판

---


> 📊 **개념 도식 (HTML에서 렌더링):** 분포 단계(distribution phase)와 소실 단계(elimination phase)의 경쟁 판정 — 말단 단계(terminal phase)는 자동으로 소실 단계(elimination phase)가 아닙니다. 분포(distribution)와 소실(elimination)의 속도 경쟁이 허락할 때만 소실 해석에 안전하게 쓰입니다.


> **전문가 보강(Mastery Augmentation) — [CRUCIBLE_DERIVED]**  
> 말단 기울기(terminal slope)를 채택할 때의 질문은 "마지막 구간이 직선인가?"가 아닙니다. "그 직선이 전체 소실 과정을 대표할 만큼 분포 단계의 영향이 작아졌는가?"입니다. 이 차이가 $t_{1/2}$를 안전한 요약값으로 쓸 수 있는지 결정합니다.


<!-- SLIDE_START: C5 | title: C5 평균체류시간 -->

### 🃏 C5. 평균체류시간(Mean Residence Time, $MRT$)

> **앞 카드에서 이 카드로:** C4가 절반으로 줄어드는 시점을 다뤘다면, C5는 전체 농도-시간 곡선에서 분자가 평균적으로 머무는 시간을 다룹니다.

> **거장의 시각**
> $MRT$를 $1.443\times t_{1/2}$로만 외우면 다구획·혈관외 상황에서 NCA 해석이 무너집니다.
> $MRT=AUMC/AUC$로 읽으면 시간가중 평균이라는 본질과 1구획 IV bolus 한정 조건이 동시에 보입니다.

#### A. 형식적 정의(Formal Definition)

$$
\underbrace{AUC_0^\infty}_{\text{총노출}}=\int_0^\infty \underbrace{C(t)}_{\text{농도함수}}\,dt \qquad [\text{G Eq.2:8, p.19}]
$$


$$
\underbrace{AUMC_0^\infty}_{\text{시간가중노출}}=\int_0^\infty \underbrace{t}_{\text{시간가중치}}\cdot\underbrace{C(t)}_{\text{농도함수}}\,dt \qquad [\text{G Eq.2:10, p.19}]
$$


$$
\underbrace{MRT}_{\text{평균체류}}=\frac{\underbrace{AUMC_0^\infty}_{\text{시간가중노출}}}{\underbrace{AUC_0^\infty}_{\text{총노출}}} \qquad [\text{G Eq.2:11, p.19}]
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $MRT$ | 시간 | 약물 분자가 체내에 평균적으로 머무는 시간 | AUMC와 AUC의 상대 변화 |
| $AUC_0^\infty$ | 농도×시간 | 총 노출 | $CL$, 용량, 외삽 품질 |
| $AUMC_0^\infty$ | 농도×시간² | 시간가중 노출 | 말단 외삽, 장기 체류 성분 |
| $K$ | 1/시간 | 1구획 IV bolus에서의 분율 제거 속도 | $CL/V$ 변화 |

💡 **비유:** $t_{1/2}$가 “절반이 되는 한 시점”이라면, $MRT$는 모든 분자가 남긴 체류 시간을 평균낸 출석부입니다.



1구획 IV bolus에서는 다음이 성립합니다. [R&T Eq.3-25, p.60]

$$
\underbrace{MRT}_{\text{평균체류}}=\frac{1}{\underbrace{K}_{\text{분율속도}}}=\frac{\underbrace{t_{1/2}}_{\text{반감기}}}{\underbrace{\ln 2}_{\text{절반조건}}}\approx\underbrace{1.443}_{1/\ln2}\cdot\underbrace{t_{1/2}}_{\text{반감기}}
$$


#### B. Compound A 기준 데이터

| Subject | $K$ (min⁻¹) | $t_{1/2}$ (min) | $MRT$ (min) | $MRT/t_{1/2}$ |
|---|---:|---:|---:|---:|
| 1 | 0.01 | 68 | 98 | 1.44 |
| 2 | 0.02 | 34 | 48 | 1.41 |
| 3 | 0.02 | 36 | 53 | 1.47 |
| 4 | 0.01 | 71 | 100 | 1.41 |

[Source: G Table 1.3, p.474]


4명 모두 $MRT/t_{1/2}$가 약 1.44에 모입니다. 이 비율은 1구획 IV bolus에서 단일지수 감소(monoexponential decline)가 성립한다는 수학적 서명(signature)입니다. 이 세션에서는 이 사실까지만 고정하고, 다구획 또는 혈관외(extravascular) MRT 전개는 후속 세션으로 보냅니다. [G p.19, p.474; R&T p.60–61]

#### C. 경계(Boundary)

| 이 카드에서 다루는 것 | → | 후속 세션으로 이월 | 이유 |
|---|---|---|---|
| $AUMC$의 말단 외삽 민감성 | → | NCA 외삽 품질 평가 | 시간가중 적분이라 말단 오차가 AUC보다 크게 증폭됩니다. [G p.19] |
| $MRT=1/K=1.443\,t_{1/2}$ | → | 혈관외·다구획 MRT 일반화 | 이 단순 관계는 1구획 IV bolus에 한정됩니다. [R&T p.60–61] |


**C5 요약(Recap):** $MRT$는 NCA에서 "평균 체류 시간"을 주는 연결 파라미터(bridge parameter)입니다. 1구획 IV bolus에서는 $1/K$로 단순하지만, 이 단순성이 성립하는 조건을 기억해야 합니다.


> **C5 체화 핵심**
> ① `평균 체류시간 질문` → $MRT=AUMC/AUC$가 결정
> ② `1구획 IV bolus vs 다구획·혈관외` → $1.443\times t_{1/2}$ 관계의 적용 가능성이 갈림
> ⚡ `$MRT$를 반감기 변형으로만 암기` → NCA 외삽·다구획성 진단 실패

---


> **전문가 보강(Mastery Augmentation) — [TEXTBOOK_DERIVED]**  
> $MRT/t_{1/2}\approx 1.443$은 단순한 암기값이 아니라 단일지수(monoexponential) 1구획 IV bolus 구조의 서명입니다. 이 비율이 크게 흐트러지면 먼저 "자료가 1구획처럼 행동하고 있는가?"를 점검해야 합니다.


<!-- SLIDE_START: §5 | title: §5 혼동쌍 해부 -->

## §5 — 혼동쌍 해부(Confusion Pair Dissection)


### 🔀 혼동쌍 1. $CL$ vs $K$ — 일차 vs 이차(Primary vs Secondary)


| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | 용적/시간(volume/time) | 1/시간(1/time) |
| 수식 내 위치 (분자/분모/지수) | $Dose/AUC$, $R_{in}/C_{ss}$, $Q\cdot E$의 결과 | $K=CL/V$ 및 $e^{-Kt}$의 지수 기울기 |
| 변화 원인 (생물학적/병적) | 혈류, 추출, 대사, 배설 경로 | $CL$과 $V$의 비율 변화 |
| 혼동 시 임상 결과 | 유지용량·노출 판단 오류 | 공변량 위치 혼재, 신부전 용량 조절 근거 약화 |


$$
\underbrace{CL}_{\text{일차정화}}=\frac{\underbrace{Dose}_{\text{투여량}}}{\underbrace{AUC}_{\text{노출}}}=\frac{\underbrace{R_{in}}_{\text{입력속도}}}{\underbrace{C_{ss}}_{\text{항정농도}}}=\underbrace{Q}_{\text{혈류}}\cdot\underbrace{E}_{\text{추출분율}},\qquad
\underbrace{K}_{\text{이차시간}}=\frac{\underbrace{CL}_{\text{정화능}}}{\underbrace{V}_{\text{분포공간}}}
$$


**핵심 정정:** $K$가 같아도 $CL$이 같다는 뜻은 아닙니다. Compound A Subject 1과 4는 $K\approx0.01$ min⁻¹로 유사하지만 $CL$은 0.1 vs 0.2 L/min으로 다릅니다. [G p.473–474]

> **⚡ 기억 고리 (Memory Hook) — *배수구 vs 배수 속도* — [EXPERT_INFERENCE, v3]**
> $CL$은 **배수구의 크기**(단위 시간당 혈액 정화량 = 처리 용량)이고, $K$는 **수위가 떨어지는 상대 속도**($=CL/V$, 욕조 크기로 나눈 값)입니다. 배수구가 커도 욕조가 크면 수위는 천천히 떨어집니다. 그래서 $K$가 같아도 $CL$은 전혀 다를 수 있습니다. 공변량(covariate)이 붙는 곳은 배수구($CL$)와 욕조($V$)이지, 그 비율($K$)이 아닙니다.


> 💼 **실무 인사이트:** 통계적 적합도(fit)가 좋아도 공변량을 $K$에 직접 묶으면 $CL$ 매개 변화와 $V$ 매개 변화가 분리되지 않을 수 있습니다. 적합 통과와 외삽 가능성(extrapolation)은 같은 문제가 아닙니다.


### 🔀 혼동쌍 2. $V$ vs $V_{ss}$ — 겉보기 bolus 용적 vs 항정상태 분포 용적


| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | 용적 | 용적 |
| 수식 내 위치 (분자/분모/지수) | $V=D/C^0$ 또는 $V=CL/K$ | $V_{ss}=CL\cdot MRT$ 및 조직분배 합 |
| 변화 원인 (생물학적/병적) | 초기 절편, 측정 농도, 말단 기울기 | 조직 분배, 분포 평형, 체류시간 |
| 혼동 시 임상 결과 | 부하용량에 말단 용적을 잘못 적용 | 다구획 분포를 1구획처럼 단순화 |


$$
\underbrace{V}_{\text{bolus 용적}}=\frac{\underbrace{A_b}_{\text{체내총량}}}{\underbrace{C}_{\text{측정농도}}}\quad\text{or}\quad
\underbrace{V}_{\text{초기용적}}=\frac{\underbrace{D}_{\text{용량}}}{\underbrace{C^0}_{\text{외삽초기농도}}}
$$


**고정:** 본 세션에서는 "$V$는 겉보기 파라미터(apparent parameter)"까지만 체화하면 됩니다. $V_{ss}$의 본격 해석은 후속 분포 동력학(distribution kinetics)에서 다룹니다. [G p.20–21; R&T p.63–64]

> **⚡ 기억 고리 (Memory Hook) — *용기 크기 vs 외관상 용기 크기* — [EXPERT_INFERENCE, v3]**
> $V$는 "약이 실제로 어디에 있는가"가 아니라, 관측된 혈장 농도(plasma concentration)를 설명하기 위해 **가정해야 하는 겉보기 공간의 크기**입니다. 조직 결합이 강할수록 $V$는 실제 체적을 훨씬 초과합니다. $V_{ss}$는 평형 상태에서의 이 겉보기 크기이며, 다구획 모델에서는 중심 구획 $V$와 달라집니다. 두 개의 수조 중 하나가 조직이고 약이 그 안에 갇혀 있다면, 혈장만 재면 수조가 훨씬 커 보이는 원리와 같습니다.


### 🔀 혼동쌍 3. $t_{1/2}$ vs $MRT$


| 비교 기준 | 개념 A | 개념 B |
|---|---|---|
| 단위 / 차원 | 시간 | 시간 |
| 수식 내 위치 (분자/분모/지수) | $t_{1/2}=\ln2/K$ | $MRT=AUMC/AUC$; 1구획 IV bolus에서 $1/K$ |
| 변화 원인 (생물학적/병적) | $V/CL$ 비율, 말단 기울기 | 체류시간 분포, AUMC 외삽, 분포·흡수 구조 |
| 혼동 시 임상 결과 | 항정상태 시간과 제거 능력 혼동 | NCA 체류시간 및 $V_{ss}$ 해석 오류 |


$$
\underbrace{t_{1/2}}_{\text{절반시간}}=\frac{\underbrace{0.693}_{\ln2}}{\underbrace{K}_{\text{분율속도}}}=0.693\cdot\underbrace{MRT}_{\text{1구획 평균체류}},\qquad
\underbrace{MRT}_{\text{평균체류}}=\frac{\underbrace{AUMC}_{\text{시간가중면적}}}{\underbrace{AUC}_{\text{총면적}}}=1.443\cdot\underbrace{t_{1/2}}_{\text{반감기}}
$$


> **⚡ 기억 고리 (Memory Hook) — *중위 vs 무게중심* — [EXPERT_INFERENCE, v3]**
> $t_{1/2}$은 농도가 반으로 줄어드는 **중위 시간**이고, $MRT$는 약 분자 한 개가 체내에 머무는 **평균 체류 시간**($AUMC/AUC$)입니다. 1구획 1차 제거에서 $MRT=1/K=t_{1/2}/\ln 2\approx 1.443\times t_{1/2}$입니다. 이 1.443배는 생리학적 차이가 아니라 **지수함수 적분의 수학적 필연**입니다. 분포나 흡수 지연이 더해지면 $MRT$는 $t_{1/2}$보다 훨씬 더 길어질 수 있어, 반감기 하나로 체류 시간을 추정하는 오류가 생깁니다.


**§5 요약(Recap):** 세 혼동쌍은 모두 "표면적으로 비슷하지만 위계가 다르다"는 문제입니다. $CL$ vs $K$는 일차/이차(primary/secondary)의 차이입니다. $V$ vs $V_{ss}$는 겉보기/항정상태(apparent/steady-state)의 차이입니다. $t_{1/2}$ vs $MRT$는 절반이 되는 시간과 평균 체류 시간의 차이입니다.

---


<!-- SLIDE_START: §7 | title: §7 자기 테스트 -->

## §7 — 자기 테스트: 능동 회상 모듈(Active Recall Module)


### Q1 [회상 ★★]
$t_{1/2}$을 $V$와 $CL$로 표현하고, 왜 이차 파라미터(secondary parameter)인지 설명해 보세요.

**정답:**
$$
\underbrace{t_{1/2}}_{\text{반감기}}=\frac{\underbrace{0.693}_{\ln2}\cdot\underbrace{V}_{\text{분포공간}}}{\underbrace{CL}_{\text{정화능}}}
$$

따라서 $t_{1/2}$은 $V$와 $CL$의 함수입니다. $t_{1/2}$만 보고 $CL$ 감소인지 $V$ 증가인지 알 수 없습니다. [G p.17–18; R&T p.58]

### Q2 [회상 ★]
$V$의 정의식 두 가지를 쓰세요.

**정답:**
$$
\underbrace{V}_{\text{환산공간}}=\frac{\underbrace{A_b}_{\text{체내총량}}}{\underbrace{C}_{\text{측정농도}}},\qquad \underbrace{V}_{\text{IV bolus 용적}}=\frac{\underbrace{D_{iv}}_{\text{투여량}}}{\underbrace{C^0}_{\text{시간0 농도}}}
$$

또는 말단 단계(terminal phase) 정보가 있으면 $V=CL/K=1.44\cdot CL\cdot t_{1/2}$로 계산합니다. [G p.20; R&T p.63]


### Q3 [회상 ★]
$C_{ss}=R_{in}/CL$을 1구획 주입(infusion) ODE에서 도출해 보세요.

**정답:**
$$
\underbrace{\frac{dC}{dt}}_{\text{농도변화}}=\underbrace{\frac{R_{in}}{V}}_{\text{입력항}}-\underbrace{\frac{CL}{V}C}_{\text{제거항}}
$$

항정상태에서 $dC/dt=0$입니다:
$$
\underbrace{C_{ss}}_{\text{항정농도}}=\frac{\underbrace{R_{in}}_{\text{주입속도}}}{\underbrace{CL}_{\text{정화능}}}
$$

$V$는 소거됩니다. $V$는 항정 도달 시간에 영향을 주지만 최종 $C_{ss}$ 자체는 $CL$이 결정합니다. [G p.22–23]

### Q4 [회상 ○]
$MRT$의 정의식과 1구획 IV bolus에서 $t_{1/2}$와의 관계를 쓰세요.

**정답:**
$$
\underbrace{MRT}_{\text{평균체류}}=\frac{\underbrace{AUMC}_{\text{시간가중면적}}}{\underbrace{AUC}_{\text{총면적}}},\qquad \underbrace{MRT}_{\text{1구획 IV 평균체류}}=\frac{1}{\underbrace{K}_{\text{분율속도}}}=\underbrace{1.443}_{1/\ln2}\cdot\underbrace{t_{1/2}}_{\text{반감기}}
$$

단, 두 번째 등식은 1구획 IV bolus 한정입니다. [G p.19; R&T p.60]

### Q5 [적용 ★★]
Compound A Subject 1과 4는 다음과 같습니다. 같은 주입속도(infusion rate) $R_{in}=10$ µg/min를 주면 $C_{ss}$는 같을까요?

| Subject | $V$ (L) | $CL$ (L/min) | $K$ (min⁻¹) | $t_{1/2}$ (min) |
|---|---:|---:|---:|---:|
| 1 | 10 | 0.1 | 0.01 | 68 |
| 4 | 20 | 0.2 | 0.01 | 71 |

[Source: G Tables 1.2/1.3, p.473–474]

**정답:** 같지 않습니다.
$$
\underbrace{C_{ss,1}}_{\text{S1 항정농도}}=\frac{\underbrace{10}_{\text{입력속도}}}{\underbrace{0.1}_{\text{CL}}}=\underbrace{100\;\mu g/L}_{\text{예측농도}}
$$

$$
\underbrace{C_{ss,4}}_{\text{S4 항정농도}}=\frac{\underbrace{10}_{\text{입력속도}}}{\underbrace{0.2}_{\text{CL}}}=\underbrace{50\;\mu g/L}_{\text{예측농도}}
$$

두 subject는 $K$와 $t_{1/2}$가 비슷하지만 $CL$이 다릅니다. 항정 농도는 $CL$이 결정합니다. [G Eq.2:22, p.23]


### Q6 [적용 ★★]
어떤 환자군에서 $t_{1/2}$가 길어졌습니다. 이것이 $CL$ 감소 때문인지 $V$ 증가 때문인지 구분하려면 무엇을 보아야 할까요?

**정답:** AUC와 $C^0$를 분리해서 봅니다. $CL$ 감소는 $AUC=Dose/CL$ 증가로 나타납니다. $V$ 증가는 $C^0=D/V$ 감소로 나타납니다. 따라서 둘이 동시에 변하면 $t_{1/2}$ 하나로는 원인 분리가 불가능합니다. [G p.17–20; R&T p.58–60]

### Q7 [적용 ★]
R&T midazolam case: 79-kg 성인, 7.5 mg base IV bolus, AUC = 287 µg·hr/L, $t_{1/2}=3.8$ hr.  
(a) $CL$은? (b) $V$는? (c) 5분 혈장 농도 180 µg/L, 혈장 용적 3.4 L이면 혈장 내 약물량과 혈장 밖 분율(fraction)은?

**정답:**
$$
\underbrace{CL}_{\text{정화능}}=\frac{\underbrace{7500}_{\text{용량}}}{\underbrace{287}_{\text{AUC}}}=\underbrace{26.1\;L/hr}_{\text{계산값}}\approx26\;L/hr
$$

$$
\underbrace{V}_{\text{말단용적}}=\underbrace{1.44}_{1/\ln2}\times\underbrace{26}_{\text{CL}}\times\underbrace{3.8}_{\text{반감기}}=\underbrace{142\;L}_{\text{계산값}}
$$

혈장(plasma) 내 약물량은 $180\;\mu g/L\times 3.4\;L=612\;\mu g=0.612$ mg입니다. 따라서 $7.5-0.612=6.89$ mg, 약 92%가 이미 혈장 밖에 있습니다. [R&T p.61–63]


### Q8 [적용 ★]
어떤 IV bolus 자료에서 $MRT/t_{1/2}$가 1.85였습니다. 1구획 IV bolus의 기대값 1.443과 다릅니다. 무엇을 의심해야 할까요?

**정답:** 1구획 IV bolus의 단순 지수 감소가 아닐 가능성, 특히 분포 동력학(distribution kinetics) 또는 말단 외삽(terminal extrapolation) 문제를 의심합니다. 출처 기반 결론은 여기까지입니다. 구체적인 NONMEM ADVAN 선택은 후속 실무 모델링 판단입니다. [G p.19; R&T p.60–66]

### Q9 — 출처 기반 보스 딜레마(Boss Dilemma) ★★
새 IV bolus 약물이 반로그 도표(semilog plot)에서 이상성 감소(biphasic decline)를 보입니다. 1구획 모델은 단순하고 AUC 중심 결정을 설명하기 쉽습니다. 2구획 모델은 분포 단계를 더 잘 설명하지만 현재 데이터가 희박합니다(sparse). 어떤 논리로 모델 구조를 방어해야 할까요?

**정답:** "어느 모델이 항상 옳은가"가 아니라 **분포 단계가 임상적으로 중요한 시간대인지**를 먼저 판단합니다. Midazolam처럼 분포가 빠르고 분포 단계 AUC가 전체의 50% 미만이면 1구획 근사가 일부 목적에서 가능합니다. 그러나 gentamicin처럼 말단 단계 전에 대부분의 소실이 발생하면 말단 기울기 중심 해석은 위험합니다. 따라서 모델 선택은 통계적 단순성만이 아니라 농도-시간 프로파일에서 분포와 소실이 경쟁하는 방식에 근거해야 합니다. [R&T p.61–66]


**§7 요약(Recap):** 계산 문제의 핵심은 수식 암기가 아니라 "어떤 식에서 어떤 파라미터가 소거되는가"를 보는 것입니다. $C_{ss}$에서는 $V$가 소거되고, $t_{1/2}$에서는 $CL$과 $V$가 함께 남습니다.

---


<!-- SLIDE_START: §8 | title: §8 메타프레임과 큰 그림 -->

## §8 — 메타프레임과 큰 그림(Meta-Frame & Big Picture)

### A. 위치 지정(Positioning)

이 세션은 PK/PD 학습 그래프의 출발점입니다. 이후의 모든 구조는 여기서 갈라집니다.

- **다구획 모델:** 말단 단계가 정말 소실을 대표하는지 묻습니다. [R&T p.61–66]
- **흡수 모델(Absorption models):** 혈관외 말단 기울기가 $K$인지 $K_a$인지 묻습니다. [G p.28–32]
- **간/신 청소율(Hepatic/Renal clearance):** $CL=Q\cdot E$와 $CL_R=f_e\cdot CL$을 장기별 생리학으로 분해합니다. [R&T p.55–68]
- **PopPK 공변량:** 공변량을 $CL$에 둘지 $V$에 둘지 결정합니다.
- **NCA:** $AUC$, $AUMC$, $MRT$가 구획 모델 없이 노출과 체류 시간을 요약합니다. [G p.19; R&T p.60]


### B. 의존성(Dependencies) — 대충 넘기면 생기는 실패 모드

1. **$t_{1/2}$ 단독 해석 오류**  
   $t_{1/2}$ 증가를 곧바로 $CL$ 감소로 읽으면 $V$ 변화 가능성을 놓칩니다. 정답은 항상 "AUC와 $C^0$가 어떻게 변했는가"를 같이 묻는 것입니다. [G p.17–20; R&T p.58–60]

2. **$V$를 실제 부피로 오해**  
   $V=40{,}000$ L 같은 값을 보고 모델이 틀렸다고 판단하면 겉보기 용적(apparent volume) 개념을 놓친 것입니다. $V$는 측정 공간인 혈장 농도(plasma concentration)와 총량 사이의 환산률입니다. [G p.20; R&T p.63–64]

3. **말단 단계 자동 신뢰(Terminal phase 자동 신뢰)**  
   Midazolam처럼 말단 단계가 소실을 잘 대표하는 경우도 있지만, gentamicin처럼 대부분의 소실이 말단 단계 전에 끝나는 예외도 있습니다. [R&T p.61–66]

4. **$K$-직접 모수화($K$-direct parameterization)의 해석 손실**  
   > 💼 **실무 인사이트:** $K$에 공변량을 직접 묶으면 $CL$ 변화와 $V$ 변화가 구분되지 않습니다. 이 세션의 일차/이차(primary/secondary) 위계는 단순한 교과서 문장이 아니라 PopPK 모수화(parameterization)의 안전장치입니다.


### C. 전문가 해석 지점(Professional Moat)

자동화 도구는 IV bolus 자료(data)에 단일지수 적합(monoexponential fit)을 빠르게 수행하고 $CL$, $V$, $K$, $t_{1/2}$를 출력할 수 있습니다. 그러나 전문가의 가치는 **숫자를 출력하는 것**이 아닙니다. 핵심은 **숫자의 위계를 읽는 것**입니다.

- $C_{ss}$가 다른 이유를 $t_{1/2}$가 아니라 $CL$에서 찾습니다.
- $t_{1/2}$가 바뀌었을 때 $CL$인지 $V$인지 먼저 분해합니다.
- 반로그 도표의 말단 직선(terminal straight line)이 언제 소실을 대표하지 않는지 압니다.
- 출처 기반 진술(source-bound statement)과 실무 인사이트를 구분합니다.

**v3 확장 — 결정 방향성의 구체화 [EXPERT_INFERENCE, v3]:**

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| AUC와 유지용량 변화 | $CL$ | → | $CL$이 반으로 줄면 AUC는 두 배 | 용량 조절 회의에서 $CL$ 역수 방향을 즉시 계산 |
| IV bolus 직후 $C^0$와 부하용량 | $V$ | → | $V$가 변하지 않으면 부하용량 수정 불필요 | 부하용량은 $V$ 함수로 판단 |
| 말단 기울기와 반감기 변화 | $CL/V$ | → | 단독으로 $CL$도 $V$도 결정 불가 | AUC와 $C^0$를 함께 확인 |
| 공변량 잔차 패턴 | $CL$ 또는 $V$ | → | $K$ 대상 모델은 생리학 혼재 | 공변량이 배수구($CL$)인지 욕조 크기($V$)인지 가설화 |
| NCA에서 $MRT$ 보고 | $AUMC/AUC$ | → | $V_{ss}=CL\cdot MRT$ 해석 필요 | 구획 모델의 $V/CL$과 차이를 명시 |
| CWRES가 체중·CrCl과 연동 | $CL$ 또는 $V$ | → | 잔차 원인 위치가 모델 방어력을 결정 | $CL$·$V$ 중 공변량 위치를 재검토 |

| 후속 세션 | 이 세션에서 열리는 개념 | 이 세션 없으면 실패하는 것 |
|---|---|---|
| 다구획 모델 | 말단 단계가 소실을 대표하는지 판정 | terminal slope 자동 신뢰 |
| 흡수 모델 | 혈관외 말단 기울기의 정체 질문 | $K$와 $K_a$ 혼동 |
| 간/신 청소율 | $CL=Q\cdot E$, $CL_R=f_e\cdot CL$ 분해 | 장기별 생리학 연결 실패 |
| PopPK 공변량 | 공변량 위치를 $CL$ 또는 $V$로 배치 | $K$ 직접 모수화로 원인 혼재 |
| NCA | AUC, AUMC, MRT의 모멘트 해석 | 평균 체류시간과 반감기 혼동 |


**최종 요약(Final Recap):** 1구획 IV bolus PK의 본질은 네 식으로 잠깁니다: $CL=Dose/AUC$, $V=D/C^0$, $K=CL/V$, $t_{1/2}=0.693\cdot V/CL$. 그러나 이 자료의 진짜 목표는 식 암기가 아니라 위계 체화입니다. **$CL$과 $V$를 먼저 보고, $K$와 $t_{1/2}$를 그 결과로 읽으면 됩니다.**

$$
\underbrace{CL}_{\text{노출결정}}=\frac{\underbrace{Dose}_{\text{용량}}}{\underbrace{AUC}_{\text{총노출}}},\qquad
\underbrace{V}_{\text{초기농도 결정}}=\frac{\underbrace{D}_{\text{용량}}}{\underbrace{C^0}_{\text{초기농도}}},\qquad
\underbrace{K}_{\text{시간기울기}}=\frac{\underbrace{CL}_{\text{정화능}}}{\underbrace{V}_{\text{분포공간}}},\qquad
\underbrace{t_{1/2}}_{\text{시간척도}}=\frac{\underbrace{0.693}_{\ln2}\cdot\underbrace{V}_{\text{분포공간}}}{\underbrace{CL}_{\text{정화능}}}
$$

---

## v3.7 자가검증 체크리스트

| 항목 | 기준 | 결과 |
|---|---|---|
| SLIDE_START 개수 | §섹션수 + 카드수 합산 | 10 개 |
| 카드당 callout 합계 ≤ 6 | 전체 카드 | ✓ |
| [E] 박스 존재 | 모든 §2 카드 | ✓ |
| [D] 거장의 시각 존재 | 모든 §2 카드 | ✓ |
| [L] 파라미터 표 존재 | Apex 카드 + 정의 수식 카드 | ✓ |
| §5 혼동 쌍 표 행 순서 고정 (4행) | §5 전체 | ✓ |
| 기호 일관성 | 첫 등장 기준 통일 | ✓ |
| PART B 흔적 없음 | 전체 | ✓ |
| 수치 anchor 보존 | Compound A 등 원본 수치 | ✓ |
| [M] 나비효과 이중 종착점 | Apex 카드 전체 | ✓ |

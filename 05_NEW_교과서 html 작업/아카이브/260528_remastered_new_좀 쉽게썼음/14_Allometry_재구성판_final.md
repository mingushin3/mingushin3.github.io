# 세션 14 (재구성판) — 알로메트릭 스케일링: "종간 환율표" 한 장으로 꿰는 FIH dose 결정 엔진

> 이 챕터의 한 줄 약속 — *"$0.75$를 외우는 사람"이 되지 말고, **"$0.75$가 prior라는 걸 알고, 언제 그게 깨지는지, 그 위에 뭘 곱해야 사람 dose가 나오는지"** 를 아는 사람이 되자.*

---

## §0. 왜 이 챕터 하나로 Phase 1 회의실 분위기가 갈리는지

화이트보드 한 장을 상상해봄. 좌측엔 **23 g mouse**에서 잰 청소율, 우측엔 **70 kg human**으로 옮긴 추정값. 그 사이를 잇는 건 거듭제곱 한 줄. 그런데 그 거듭제곱의 지수를 $b=1$로 쓰느냐 $b=0.75$로 쓰느냐만으로 —

| Species pair | b=1 vs b=0.75 격차 |
|---|---:|
| Mouse 23 g → Human 70 kg | **약 7.4배** [G&W PK28 p.611–614] |
| Mouse 20 g → Human 70 kg | **3500 vs 455 = 7.7배** [R&T p.733] |
| Rat 250 g → Human 70 kg | **약 4.1배** |

이게 단순 산수 차이가 아님. **Target AUC를 맞추려고 dose를 잡는 순간 CL을 과대평가하면 dose도 그만큼 과대 산출됨.** 규제 심사자가 표 한 칸을 짚고 "이 지수 어떻게 정당화하셨어요?"라고 물으면 그 자리에서 답해야 함. 이 챕터가 그 한 칸을 방어하는 도구임.

이 챕터를 다 읽고 나면 머릿속에 이런 단일 다이어그램이 자동 작동해야 함:

```text
[Step 1] 이 변수가 흐름인가, 공간인가, 시간인가?
              ↓
[Step 2] 그래서 환율(지수)이 뭐임? — flow면 0.75, extent면 1
              ↓
[Step 3] 그 환율이 이 약물에서 진짜 버티는가? — 6가지 예외 체크
              ↓
[Step 4] Dedrick으로 곡선이 진짜 겹치는가? — Elementary or Complex?
              ↓
[Step 5] Equal-AUCu backbone으로 dose 환산 — 단, 이건 "다리의 철골"임
              ↓
[Step 6] 사람 안 보정 5층 — Maturation × LBW/TBW × Organ × Strategy × Pregnancy
```

자, 이제 한 정거장씩 감.

---

## §1. The Big Idea — 알로메트리는 회귀식이 아니라 "환율표"임

### 1-1. 마스터식을 다시 보기

대부분 이 식을 처음 만나면 회귀선처럼 읽음:

$$
\underbrace{Y}_{\text{대상 변수}}=\underbrace{a}_{\text{절편}}\cdot \underbrace{BW}_{\text{체중}}^{\overbrace{b}^{\text{지수}}}
\quad\text{[G\&W Eq.2:374, p.173; R\&T Eq.22-2, p.732]}
$$

근데 회귀선으로 읽는 순간 함정에 빠짐. "fitting이 잘 됐으니까 OK"라고 넘어가게 됨. **이 식의 진짜 의미는 "체중 배율을 바꿔도 같은 법칙이 그대로 유지된다"는 주장임.** 즉 환율식임. 마우스 1 kg과 사람 1 kg을 잇는 "통화 변환 규칙" 그 자체임.

로그 변환하면 직선:

$$
\underbrace{\ln(Y)}_{\text{로그 }Y}=\underbrace{\ln(a)}_{\text{로그 절편}}+\overbrace{\underbrace{b}_{\text{기울기=환율}}\cdot\underbrace{\ln(BW)}_{\text{로그 }BW}}^{\text{log-log}}
\quad\text{[G\&W Eq.2:379, p.176; R\&T Eq.22-1, p.732]}
$$

### 1-2. 변수별로 환율이 다름 — 이게 전부임

이 챕터의 모든 게 결국 한 표로 압축됨:

| 변수 종류 | 대표 변수 | 환율(지수) | 직관 |
|---|---|---:|---|
| **흐름/속도** | CL, GFR, 장기 혈류, 대사율 | $b\approx 0.75$ | "단위 시간당 처리량" |
| **공간/범위** | V, 혈액량, 조직량, 체수분 | $d\approx 1.0$ | "퍼질 수 있는 부피" |
| **시간** | $t_{1/2}=\ln2\cdot V/CL$ | $d-b\approx 0.25$ | 큰 동물 = 긴 반감기 |
| **속도상수** | $k_{el}=CL/V$ | $b-d\approx -0.25$ | 큰 동물 = 작은 fraction/시간 |

💡 한 줄 멘트로 박아두기 — **"흐름은 0.75, 공간은 1, 시간은 그 차이 0.25, 속도상수는 그 부호 뒤집기."** 이 네 줄이 안 외워지면 뒤 §전체가 흔들림.

### 1-3. 왜 흐름은 1이 아니고 0.75인가

G&W가 두 줄로 정리함 [G&W §2.10, p.173] — **대사율 ∝ $BW^{0.75}$**, **에너지 함량 ∝ $BW^1$** → 따라서 turnover time ∝ $BW^{0.25}$. 한 문장 압축: *"덩치가 커지면 절대 처리량은 늘지만, 단위 체중당 효율은 떨어짐."*

코끼리가 쥐보다 100만 배 무겁다고 100만 배 많은 음식을 먹지 않음. 약 $100,000^{0.75}\approx 178,000$배만 더 먹음. 같은 원리로 코끼리 CL이 쥐 CL의 100만 배가 아니라 약 18만 배임. 이게 자연이 정한 환율임.

---

## §2. 첫 번째 환율 — CL의 b ≈ 0.75 (가장 위험한 카드)

### 2-1. 가장 흔한 임상 사고는 "kg당 사고"임

임상의의 머리는 mg/kg 처방에 길들여져 있음. "30 mg/kg 줘"라는 말이 입에 붙어있으니 자연스럽게 **"CL도 kg당 선형 비례"** 즉 $b=1$이라고 무의식적으로 가정함. 이게 가장 흔한 사고임.

근데 CL은 kg당 변수가 아님. CL은 "단위 시간당 약물을 처리해 비워내는 부피"임 — 즉 **흐름 변수**. 흐름 변수의 환율은 자연이 0.75로 정해놨음 [G&W Eq.2:380, p.176].

$$
\underbrace{CL_i}_{\text{개체 CL}}=\underbrace{a}_{\text{CL 절편}}\cdot\underbrace{BW_i}_{\text{개체 BW}}^{\overbrace{b}^{\text{CL 지수}\approx 0.75}}
$$

### 2-2. 0.75와 1의 차이가 임상에서 얼마나 큰지 — 자릿수 감각

지수 하나 차이가 격차로 펼쳐지는 공식:

$$
\underbrace{\left(\frac{BW_{human}}{BW_{animal}}\right)^{1-0.75}}_{\text{= }(BW_{ratio})^{0.25}}=\text{환율 오류로 발생하는 배수}
$$

- Mouse 25 g → Human 70 kg에서 CL 예측: $b=0.75$면 약 **4.6 L/hr**, $b=1$이면 약 **33.6 L/hr**. **7.3배 차이**.
- 그래서 Phase 1 starting dose에서 $b=1$로 잘못 계산하면 "혹시 모르니까 안전하게 낮게 시작하자"가 아니라 **target AUC 대비 dose를 7배쯤 과대 산출**할 수 있음.

### 2-3. 그렇다고 0.75를 법칙처럼 박으면 안 됨 — 보스 딜레마

G&W Fig.2.159는 91개 화합물 CL 지수를 다 그려봤더니 **0.5~1.0 범위에 흩어져 있음** [G&W p.191]. 즉 0.75는 **prior**일 뿐 자연상수가 아님.

🚨 **실패 트리거 6가지** (입에 붙여둘 것):

1. 종간 혈장 단백 결합($f_u$) 차이
2. CYP isoform 조성 차이 (예: CYP3A4 vs CYP3A8)
3. 비선형 Michaelis-Menten 동태
4. 장간 순환 (enterohepatic recirculation)
5. 투여 경로·제형 차이
6. 중심/말초 V 비율 종간 drift

이 중 하나라도 강하게 의심되면 — **$b=0.75$를 primary로 두되, $b\in\{0.5, 0.62, 0.75, 1.0\}$를 sensitivity로 동시 제시**. FIH 문서에서 단일 지수를 박는 건 가장 깨지기 쉬운 진술임.

### 2-4. $f_u$가 종간 크게 다르면 → $CL_u$ scaling으로 갈아탐

$$
\underbrace{CL_{u,man}}_{\text{human }CL_u}=\underbrace{CL_{u,rat}}_{\text{rat }CL_u}\cdot\left(\frac{\overbrace{BW_{man}}^{\text{human BW}}}{\overbrace{BW_{rat}}^{\text{rat BW}}}\right)^{\overbrace{b}^{\text{CLu 지수}}}
\quad\text{[G\&W Eq.2:421, p.190]}
$$

대표 예시 — **cefazolin** (1세대 cephalosporin, 단백 결합 큼, 신장 배설) [R&T Table 22-1, p.740]. 사람과 동물 간 단백 결합 차이가 의미 있게 다르면 total CL scaling 결과가 어긋남. 이 경우 $f_u$ 측정은 **같은 농도·buffer·온도·assay**에서 비교해야 의미가 있음.

🎯 **C2 한 줄로 닫기** — *"kg당 사고는 dose 과대로, 0.75 과신은 기전 예외 누락으로 감. 둘 다 위험. 답은 '0.75 prior + sensitivity 표'."*

---

## §3. 두 번째 환율 — V의 d ≈ 1.0 (그리고 시간은 거기서 떨어져 나옴)

### 3-1. V는 공간이지 흐름이 아님

V를 CL처럼 흐름 변수로 읽는 순간 모든 게 꼬임. V는 **약물이 분포할 수 있는 부피의 크기** — 그러니까 체수분, 혈액량, 조직량을 따라감.

$$
\underbrace{V_i}_{\text{개체 }V}=\underbrace{c}_{\text{V 절편}}\cdot\underbrace{BW_i}_{\text{개체 BW}}^{\overbrace{d}^{\text{V 지수}\approx 1.0}}
\quad\text{[G\&W Eq.2:382, p.179]}
$$

G&W Table 2.22가 이걸 못 박아줌 — 혈액량 지수 0.99, 골격근량 1.09, $V_d$ ≈ 1.0 [G&W p.180]. 즉 공간 변수들은 거의 다 체중에 비례함.

### 3-2. 시간축은 환율 차이에서 자동으로 나옴 — 외울 게 아니라 떨어져 나오는 것임

$$
\underbrace{t_{1/2}}_{\text{반감기}}=\underbrace{\ln2}_{\text{반감 상수}}\cdot\frac{\overbrace{V}^{\text{공간}}}{\overbrace{CL}^{\text{흐름}}}=\ln2\cdot\frac{\underbrace{c\cdot BW^d}_{\text{V 스케일}}}{\underbrace{a\cdot BW^b}_{\text{CL 스케일}}}\propto \underbrace{BW^{d-b}}_{\text{시간지수}\approx 0.25}
$$

$$
\underbrace{k_{el}}_{\text{제거속도}}=\frac{\overbrace{CL}^{\text{흐름}}}{\overbrace{V}^{\text{공간}}}\propto\underbrace{BW^{b-d}}_{\text{속도지수}\approx -0.25}
$$

### 3-3. "큰 동물 = 느린 시계" 직관

코끼리 심박은 분당 30회, 쥐 심박은 분당 600회. 코끼리는 시간이 천천히 흐르고 쥐는 빨리 흐르는 것처럼 보임. **약동학적으로도 동일** — 큰 동물은 약물 반감기가 김.

근데 여기서 헷갈리지 말 것 — 이건 **단위 시간당 fraction 제거가 작다**는 뜻이지 절대 CL이 작다는 게 아님. 절대 CL은 코끼리가 쥐보다 훨씬 큼. 비유하자면 — 코끼리는 거대한 정수기, 쥐는 작은 정수기. 코끼리 정수기가 1분에 처리하는 물의 절대량은 훨씬 많지만, 코끼리 몸 전체 물의 비율로 보면 쥐가 1분에 더 큰 비율을 처리함.

### 3-4. 데이터 anchor — Methadone (PK28)

저추출 μ-opioid 작용제. 간 추출률 <10%니까 CL이 효소 활성에 직접 반응하고 알로메트리 신호가 깨끗하게 나옴 [G&W p.186; PK28 p.613].

| 종 | BW | Dose | $t_{1/2}$ (§2.10.6 set) | $t_{1/2}$ (PK28 case set) |
|---|---:|---:|---:|---:|
| Mouse | 23 g | 25 µg IV | 1.5 h | 1.5 h |
| Rat | 250 g | 500 µg IV | **2.9 h** | **3.9 h** |
| Man | 70 kg | 100 mg IV | 35 h | 35 h |

⚠️ Rat $t_{1/2}$가 출처에 따라 다름. **보고서 인용 시 `[§2.10.6 set]` 또는 `[PK28 case set]`을 반드시 명시.** 둘 중 하나로 임의 고정은 무결성 위반임.

🎯 **C3 한 줄로 닫기** — *"$t_{1/2}\propto BW^{0.25}$만 외우면 절반만 본 것. 더 중요한 건 $k_{el}\propto BW^{-0.25}$ — 큰 동물은 fraction 제거 속도가 작음."*

---

## §4. 환율 검증 도구 — Dedrick Superposition

### 4-1. Dedrick이 하는 일 — "프레임 동기화"

서로 다른 속도로 재생되는 동영상 5개를 같은 프레임 속도로 맞춰서 겹쳐보는 작업이 Dedrick임. 시간축을 정규화해서 mouse·rat·dog·monkey·human의 PK 곡선을 한 그래프에 올렸을 때 **진짜로 겹치면** → 환율 가정이 그 자료에서 통한다는 진단. 안 겹치고 fan-out하면 → 환율이 깨졌거나 다른 기전이 작동 중.

### 4-2. Elementary (d=1 가정) — 가장 흔한 형태

$$
\underbrace{y}_{\text{농도축}}=\frac{\overbrace{C}^{\text{농도}}}{\underbrace{Dose/BW}_{\text{kg당 용량}}},\qquad \underbrace{x}_{\text{시간축}}=\frac{\overbrace{t}^{\text{시간}}}{\underbrace{BW^{1-b}}_{\text{기본 시간}}}
$$

이름이 **Kallynochron** ("kg당 생리학적 시간"). K는 kg으로 외움.

### 4-3. Complex (d ≠ 1) — V가 비례를 벗어날 때

$$
\underbrace{y}_{\text{농도축}}=\frac{\overbrace{C}^{\text{농도}}\cdot\overbrace{BW^d}^{\text{공간 보정}}}{\underbrace{Dose}_{\text{투여량}}},\qquad \underbrace{x}_{\text{시간축}}=\frac{\overbrace{t}^{\text{시간}}}{\underbrace{BW^{d-b}}_{\text{복합 시간}}}
$$

이름이 **Apolysichron** ("anyspace 생리학적 시간"). A는 anyspace로 외움.

### 4-4. 전환 규칙 — 한 줄로 결정

> **log-log $V$ vs $BW$ 기울기가 0.9~1.1 안 → Elementary, 밖 → Complex.**

벤치마크 쌍 (입에 붙여둘 것):

| Case | $d$ | 전환 | 의미 |
|---|---:|---|---|
| **PK28 Methadone** | ≈1.0 | Elementary 통과 | 저추출 + 공간 비례 → backbone 가정 모두 OK |
| **PK29 Compound X** | **1.18~1.21** | Complex 필요 | V가 체중에 살짝 강하게 비례 → Elementary 쓰면 fan-out |

PK29 자료 [G&W §2.10.7 p.189 / PK29 case p.619]:

| 출처 | $a$ | $b$ | $c$ | $d$ | $e$ | $g$ |
|---|---|---|---|---|---|---|
| G&W §2.10.7 | 0.021 | 0.74 | 0.076 | 1.18 | 0.56 | 0.075 |
| PK29 case | 0.021 | 0.75 | 0.10 | 1.21 | 0.54 | 0.071 |

같은 약물인데 출처 내 수치가 미세하게 다름. 인용 시 **citation scope 표기 의무**.

### 4-5. Curve fan-out을 "그림 문제"로 오독하지 말 것

Dedrick plot에서 겹침이 깨졌을 때 흔한 오해 — "그림이 안 예쁘게 그려졌네"로 넘기는 것. 절대 아님. Fan-out은 **기전 신호**임. 의심 순위:

1. $d=1$ 가정 실패 → Complex Dedrick으로 갈아탐
2. 다구획성 → multi-compartment 모델
3. Model misspecification (분포상이 평형 안 됨, dose level 부족)
4. 비선형 PK (포화 대사 등)

🎯 **C4 한 줄로 닫기** — *"Dedrick은 환율 검증 도구. 겹치면 환율 OK, fan-out하면 기전 신호. PK28은 통과, PK29는 Complex로 갈아탐."*

---

## §5. 환율을 dose로 번역하는 다리 — Equal-AUCu Backbone

### 5-1. 핵심 식 한 줄

비결합 노출이 같으면 약리 효과가 같다는 전제 위에서:

$$
\underbrace{AUC_{u,rat}}_{\text{rat }AUC_u}=\underbrace{AUC_{u,man}}_{\text{human }AUC_u}=\frac{\overbrace{Dose_{rat}}^{\text{rat dose}}}{\underbrace{CL_{u,rat}}_{\text{rat }CL_u}}=\frac{\overbrace{Dose_{man}}^{\text{human dose}}}{\underbrace{CL_{u,man}}_{\text{human }CL_u}}
\quad\text{[G\&W Eq.2:417, p.190]}
$$

여기서 dose 환산 공식이 떨어져 나옴:

$$
\underbrace{Dose_{man}}_{\text{human dose}}=\underbrace{Dose_{rat}}_{\text{rat dose}}\cdot\left(\frac{\overbrace{BW_{man}}^{\text{human BW}}}{\overbrace{BW_{rat}}^{\text{rat BW}}}\right)^{\overbrace{b}^{\text{CL/AUC 지수}}}
\quad\text{[G\&W Eq.2:420, p.190]}
$$

### 5-2. mg/kg 비로 다시 적으면 — 직관 한 방

$$
\underbrace{\frac{Dose_{man}/BW_{man}}{Dose_{rat}/BW_{rat}}}_{\text{mg/kg 비}}=\left(\frac{\overbrace{BW_{man}}^{\text{큰 종 BW}}}{\overbrace{BW_{rat}}^{\text{작은 종 BW}}}\right)^{\overbrace{b-1}^{\text{kg당 지수}\approx -0.25}}
$$

$b<1$이면 **큰 동물의 mg/kg dose는 작은 동물보다 낮음.** 그래서 — *"rat에서 효과 본 mg/kg을 그대로 사람에 적용하면 사람 dose가 과대"* 라는 임상 격언이 여기서 떨어져 나옴.

### 5-3. 🚨 이 식이 곧 FIH starting dose가 *아님* — "다리의 철골"임

이 식 그대로 IND 문서에 박으면 안 됨. 이건 **노출 backbone**일 뿐이고, 그 위에 다음이 다 얹혀야 진짜 첫 사람 dose가 됨:

| Layer | 무엇을 하는가 |
|---|---|
| ① **PD metric** | AUC-driven? Cmax-driven? Time>threshold? |
| ② **$f_u$ 보정** | 종간 $f_u$ 다르면 total CL → $CL_u$로 갈아탐 |
| ③ **PK 선형성** | 선형 구간 검증, 비선형이면 별도 처리 |
| ④ **Safety margin** | NOAEL/LOAEL 기반 toxicology margin |
| ⑤ **Route/formulation** | IV vs PO, BA 차이, formulation 효과 |

⚠️ **G&W가 직접 박은 caveat** — *"동일 AUC라도 농도-시간 곡선의 모양은 상당히 다를 수 있음"* [G&W p.190]. Equal-AUCu가 같은 PD 효과 또는 같은 곡선 모양을 보장하지 *않음*.

🎯 **C5 한 줄로 닫기** — *"Eq.2:420은 종간 환율의 마무리식이지 FIH dose 공식이 아님. backbone 위에 5 layer 얹혀야 처방이 됨."*

---

## §6. 사람 안에서는 backbone 위에 다섯 층을 또 얹어야 함

여기서부터가 보강본_final의 핵심임. C5까지는 *종간*의 이야기였음. 이제 *사람 안에서* — 신생아·소아·노인·비만·신부전·간부전·임신부에게 dose를 줄 때 — backbone만으로는 안 되는 이유들임.

**한 줄 마스터 공식**:

$$
\underbrace{Dose_{patient}}_{\text{환자 dose}}=\overbrace{\underbrace{Dose_{std}}_{\text{표준 dose}}\cdot\left(\frac{BW}{70}\right)^{0.75}}^{\text{C5 backbone}}\cdot \overbrace{F_{mat}}^{\text{성숙}}\cdot \overbrace{f_{size}}^{\text{LBW/TBW}}\cdot \overbrace{[RF\cdot fe + (1-fe)\cdot \text{age factor}]}^{\text{장기 기능}}\cdot \overbrace{f_{strategy}}^{\text{표기 단위}}\cdot \overbrace{f_{preg}}^{\text{임신 보정}}
$$

곱셈 하나라도 빼면 한 자릿수씩 어긋날 수 있음. 하나씩 봄.

---

### 6-1. Maturation Layer — 신생아·영아의 핵심

R&T 본문이 한 줄로 박음 [R&T p.420]:

> *"creatinine clearance in this age range can be thought of as the product of an adjustment based on body size and a maturation component"*

즉 신생아 CL은:

$$
\underbrace{CL_{neonate}}_{\text{신생아 CL}}=\overbrace{\underbrace{Adjustment(BW)}_{\text{체격 보정}}}^{\text{algometric}}\cdot \overbrace{\underbrace{Maturation\ component}_{\text{출생 후 성숙도}}}^{\text{maturation}}
\quad\text{[R\&T p.420]}
$$

#### 결정적 자료 — R&T Fig.14-9

미숙아 conceptional age 28주 → 40주 사이에 BSA로 정규화한 크레아티닌 청소율이 **지수적으로 약 8배 증가**:

$$
\underbrace{CL_{cr}\left(\tfrac{mL}{min\cdot 1.73m^2}\right)}_{\text{BSA-정규화 CL}_{cr}}=\underbrace{0.373}_{\text{Fig.14-9 절편}}\cdot \overbrace{e^{\,0.111\cdot Age_{wk}}}^{\text{지수 성장}}
\quad\text{[R\&T Fig.14-9, p.421]}
$$

#### 함수형 sigmoid (Anderson-Holford형, `[교과서 외 구현]`)

$$
\underbrace{F_{mat}(PMA)}_{\text{성숙 분율}}=\frac{\overbrace{PMA^{\,Hill}}^{\text{post-menstrual age 지수}}}{\underbrace{TM_{50}^{\,Hill}}_{\text{50\% 성숙 PMA}}+\overbrace{PMA^{\,Hill}}^{\text{PMA 지수}}}
$$

- $PMA$ = 수태 후 주수 (= 40 + 출생 후 주수)
- $TM_{50}$ = 50% 성숙 도달 PMA, 약물·효소마다 다름
- 완전 성숙이면 $F_{mat}\to 1$

#### 임상 함의 — 연령대별

| 연령대 | $F_{mat}$ | 임상 조치 |
|---|---|---|
| **신생아 (0~28일)** | 매우 낮음. 미숙아일수록 더 낮음 | **TDM 거의 필수** [R&T p.430] |
| **영아 (1개월~2세)** | 빠르게 변함, 며칠 단위 | 모니터링 지속 업데이트 |
| **소아 (2세~12세)** | ≈ 1 | $BW^{0.75}$ backbone 직접 적용 가능 [R&T p.424] |

⚠️ **함정** — R&T가 직접 박은 경고: *"the lack of maturation of renal and hepatic function necessitates that the rate of administration of drugs to both neonates and young infants be reduced, **even on a body-weight basis**, if toxicity is to be avoided"* [R&T p.430]. **mg/kg 그대로 신생아에 적용하면 toxic할 수 있음.**

---

### 6-2. Body Composition Layer — LBW vs TBW

비만 환자에게 어떤 체중 단위를 쓸지가 **약물의 극성(친수성 vs 친지질)**에 따라 갈림.

#### R&T가 직접 박은 두 줄

1. **친수성·극성 약물**: *"digoxin and polar drugs, for example, do not partition well into fat. Accordingly, **for these drugs, $V_u$ correlates better with lean body mass**"* [R&T p.418, p.434].
2. **친지질 약물**: R&T Table 14-7에서 **diazepam**은 비만에서 V가 2.81 L/kg, 정상에서 1.53 L/kg → **체중 보정 후에도 비만에서 더 큼** [R&T p.439].

#### LBW 공식 (R&T Eq.14-10·14-11, p.434)

$$
\underbrace{LBW_{male}(kg)}_{\text{남성 LBW}}=\underbrace{1.10}_{\text{선형 계수}}\cdot\overbrace{Weight(kg)}^{\text{체중}}-\underbrace{\frac{128\cdot\overbrace{Weight(kg)^2}^{\text{체중 제곱}}}{\underbrace{(100\cdot Height(m))^2}_{\text{신장 제곱 보정}}}}_{\text{지방 보정항}}
$$

$$
\underbrace{LBW_{female}(kg)}_{\text{여성 LBW}}=\underbrace{1.07}_{\text{선형 계수}}\cdot\overbrace{Weight(kg)}^{\text{체중}}-\underbrace{\frac{148\cdot\overbrace{Weight(kg)^2}^{\text{체중 제곱}}}{\underbrace{(100\cdot Height(m))^2}_{\text{신장 제곱 보정}}}}_{\text{지방 보정항}}
$$

⚠️ R&T 단서 — *"these relationships do not apply to highly muscular individuals"* [R&T p.434]. 보디빌더·운동선수에는 안 맞음.

#### 약물별 체격 지표 결정 (R&T Table 14-7 자료)

| 약물 | 극성 | V/kg (obese) | V/kg (control) | 선택 |
|---|---|---:|---:|---|
| Theophylline | 친수성 | 0.32 | 0.47 | **LBW** |
| Digoxin | 친수성 | 10.7 | 14.3 | **LBW** |
| Diazepam | 친지질 | 2.81 | 1.53 | **TBW** |

#### 한 줄 의사결정

> **친수성/극성 → LBW. 친지질 → TBW. 약물 극성을 먼저 묻지 않으면 같은 식에 두 약물군이 섞임.**

---

### 6-3. Organ Function Layer — 신장공장 vs 간공장 분기

Total CL은 사실 **두 공장의 합** — 신장공장($CL_R$, GFR 의존)과 간공장($CL_H$, 효소·혈류 의존). 두 공장의 알로메트릭 거동이 다름.

#### R&T Eq.15-7 — 사람 안 보정의 표준식

$$
\underbrace{R_d}_{\text{환자/표준 CL}_u\text{ 비}}=\frac{\underbrace{CL_u(d)}_{\text{환자 CL}_u}}{\underbrace{CL_u(t)}_{\text{표준 60세/70kg}}}=\overbrace{\underbrace{RF\cdot fe(t)}_{\text{신장 경로}}}^{\text{신장공장}}+\overbrace{\underbrace{[1-fe(t)]\cdot\frac{(140-Age)\cdot Wt^{0.75}}{1936}}_{\text{비신장(간) 경로}}}^{\text{간공장}}
\quad\text{[R\&T Eq.15-7, p.453]}
$$

| 기호 | 의미 |
|---|---|
| $RF$ | renal function (표준 대비 비) |
| $fe(t)$ | 표준 환자 신장 배설 분율 ($= CL_R/CL_{total}$) |
| $140-Age$ | Cockcroft-Gault형 연령 보정 |
| $Wt^{0.75}$ | 간 청소율 backbone |
| $1936$ | $(140-60)\cdot 70^{0.75}\approx 1936$ |

#### 정량 예시 — 75세, 60 kg, RF=0.6 환자

| 약물 | $fe$ | $R_d$ 계산 | 결과 |
|---|---:|---|---:|
| A (신장 dominant) | 0.85 | $0.6\cdot 0.85 + 0.15\cdot 0.726$ | **≈ 0.62** |
| B (간 dominant) | 0.10 | $0.6\cdot 0.10 + 0.90\cdot 0.726$ | **≈ 0.71** |

(연령·체중 항: $(140-75)\cdot 60^{0.75}/1936 \approx 0.726$)

- **약물 A**: RF가 $R_d$를 직접 끌어내림 → 신부전 환자에서 dose 감량 결정적
- **약물 B**: 연령·체중 항이 거의 다 결정 → RF 변화에 거의 무관

⚠️ R&T 본문 직접 — *"ideally, **renal clearance should be correlated with creatinine clearance, and the nonrenal clearance should be examined separately**"* [R&T p.455]. PopPK에서 total CL에 WT exponent 하나만 박는 게 통상이지만, **$fe$ 정보가 있으면 분리하는 게 R&T의 직접 권고**.

#### 노인의 신·간 분리 진술

- **신장**: ~ **1%/yr 감소** (성인기 크레아티닌 청소율) [R&T p.422]
- **간 (CYP3A)**: 노인(65~75세) 평균 CL이 청년(25~35세)의 **약 60~70%** [R&T p.424, Fig.14-13]

🚨 *"CYP3A4가 60세 이상에서 매년 1%씩 감소한다"는 단정 진술은 R&T가 직접 뒷받침하지 않음.* R&T가 적은 건 ① 신장 1%/yr, ② CYP3A 청소율이 노인에서 감소함, 두 가지. 두 사실을 합쳐서 "CYP3A도 1%/yr"라고 적으면 안 됨.

---

### 6-4. Dosing Strategy Layer — mg/kg vs mg/m² vs BW^0.75

같은 환자에게 같은 약을 처방해도 표기 단위 하나로 dose가 달라짐. 이게 임상에서 가장 무의식적으로 지나가는 결정임.

#### 세 strategy를 한 줄에

$$
\overbrace{\underbrace{Dose_{mg/kg}}_{\text{체중 비례}}=k_1\cdot BW}^{\text{Strategy 1: 항암·항생 관행}}\quad
\overbrace{\underbrace{Dose_{mg/m^2}}_{\text{BSA 비례}}=k_2\cdot BSA}^{\text{Strategy 2: 소아 신장배설}}\quad
\overbrace{\underbrace{Dose_{allom}}_{\text{알로메트릭}}=k_3\cdot BW^{0.75}}^{\text{Strategy 3: 현대 PopPK}}
$$

#### 같은 환자, 같은 약, 다른 dose — 정량 비교

**성인 60 kg 기준 600 mg/일 약물을 4세 소아 15 kg에 적용**:

| Strategy | 계산 | Dose |
|---|---|---:|
| mg/kg | $600\cdot(15/60)$ | **150 mg** |
| mg/1.73 m² | $600\cdot(15/60)^{0.75}$ | **약 213 mg** |
| BW^0.75 | $600\cdot(15/60)^{0.75}$ | **약 213 mg** |

mg/m²와 BW^0.75은 R&T Eq.14-2가 $BSA\propto BW^{0.75}$를 쓰기 때문에 수학적으로 **동일**. mg/kg만 약 30% 낮은 dose를 내놓음.

**같은 약물을 BMI 40, 140 kg 비만 환자에 적용**:

| Strategy | 계산 | Dose |
|---|---|---:|
| mg/kg | $600\cdot(140/60)$ | **1400 mg** |
| mg/1.73 m² | $600\cdot(140/60)^{0.75}$ | **약 1130 mg** |

mg/kg을 그대로 적용한 1400 mg에 대해 R&T가 직접 박은 경고 [R&T p.435]:

> *"Does a grossly obese patient really need more of a drug because of his or her extra body fat? ... In these cases, there is a danger that too high a dose is calculated adopting this procedure."*

#### R&T의 직접 권장 — "broader use is suspect"

> *"Expressing dosage in mg/kg or mg/1.73 m² is reasonable if the limits (age, body composition, renal function) of its application are specified. However, **the broader use of such rules is suspect**. ... A more reasonable approach is one that takes the pharmacokinetics (i.e., renal function, phenotyping, genotyping, if needed) and pharmacodynamics into account."* [R&T p.435]

즉 — **표기 strategy를 쓰면 그 적용 한계(연령·체조성·신기능)를 *반드시 명시*. 단순 일률 적용 대신 PK/PD 기반 개별화가 R&T의 권장.**

#### 항암제 BSA dosing의 R&T 직접 정당화 조건

> *"for the alkylating agents ... the dosing rate needed to achieve a steady-state concentration was directly proportional to body surface area. ... **Obviously, this adjustment is only warranted if surface area explains variability in clearance better than body weight**."* [R&T Ch.22, p.738]

→ "항암제니까 BSA"는 자동 적용 아님. **약물별로 BSA가 BW보다 CL 변동성을 더 잘 설명하는지** 자료로 보여야 함.

#### 임상 의사결정 트리

```text
환자 dose 표기 결정
   │
   ├── 신장 배설 우세 + 소아 → mg/1.73 m² 또는 BW^0.75 (R&T 권장)
   │
   ├── 항암제 alkylating-type → mg/m² (Ch.22 p.738, BSA 우세 검증 시)
   │
   ├── 비만 + 친수성 → LBW 기반 (R&T p.418, p.434)
   │
   ├── 비만 + 친지질 → TBW 기반 (Table 14-7)
   │
   └── 좁은 TI + 근육질/왜소/소아 → PK·PD 개별화 (R&T p.435 최우선)
```

---

### 6-5. Pregnancy Layer — 임신부의 두 함정

임신부는 **모체 + 태아** 두 시스템이 PK에 동시 관여함. R&T Ch.14가 직접 적은 두 명제가 임상 의사결정의 핵심임.

#### 함정 ①: Albumin 감소 → Total ↓이지만 Unbound는 보존됨

R&T 직접 [R&T p.429]:

> *"By the time of parturition, the serum albumin drops to about 50% to 60% of the value before pregnancy. ... Lower total exposures are therefore seen during pregnancy, but **the unbound drug concentration does not generally seem to be affected**. **There is, therefore, no need to adjust dosage because of the reduction in plasma albumin**."*

수식으로 — 왜 unbound가 보존되는가:

$$
\underbrace{C_u^{ss}}_{\text{정상상태 unbound}}=\overbrace{\underbrace{f_u}_{\uparrow\text{(albumin↓)}}}^{\text{↑ binding↓}}\cdot \overbrace{\underbrace{C_{total}^{ss}}_{\downarrow\text{(albumin↓)}}}^{\text{↓ binding↓}}=\overbrace{\frac{\underbrace{Dosing\ rate}_{\text{투여속도}}}{\underbrace{CL_u}_{\text{비결합 CL}}}}^{\text{불변}}
\quad\text{[R\&T p.429]}
$$

$f_u\uparrow$와 $C_{total}\downarrow$가 서로 상쇄. **임신부 TDM에서 total이 낮아 보인다고 dose 올리는 게 가장 흔한 임상 오류임.**

🎯 *Phenytoin 임상 예시* — 임신 35주 환자에서 total phenytoin 5 mg/L (비임신 정상범위 10~20 mg/L 하한 미달) 측정. **Dose 올리지 말 것.** Albumin 감소가 fu를 보상 → unbound는 거의 그대로. Total만 보고 증량하면 unbound가 진짜로 올라가 toxicity(소뇌 증후군, 안진, 운동 실조) 위험.

#### 함정 ②: 태반 통과 약물의 모체-태아 unbound 평형

R&T 직접 [R&T p.430]:

> *"For those drugs that can pass the placenta, **the unbound plateau concentration in the fetus is likely to equal that in the pregnant mother** receiving chronic therapy. With eliminating capacity generally poorly developed, the fetus acts for the most part as an additional 'tissue' of distribution, with half-life in the fetus being virtually the same as that in the mother."*

수식으로:

$$
\underbrace{C_u^{fetus,\,ss}}_{\text{태아 fu 정상상태}}\approx \overbrace{\underbrace{C_u^{mother,\,ss}}_{\text{모체 fu 정상상태}}}^{\text{R\&T p.430}},\quad \underbrace{t_{1/2}^{fetus}}_{\text{태아 반감기}}\approx \underbrace{t_{1/2}^{mother}}_{\text{모체 반감기}}
$$

→ **모체 unbound 모니터링이 fetus 노출의 surrogate.** 태아는 자체 청소 기관이 없고 모체의 distribution tissue처럼 작동.

#### 함정 ③: 분만 직후 신생아의 급변

R&T 직접 [R&T p.430]:

> *"**A drastic change occurs, however, on delivery.** Deprived of access to the fully developed eliminating organs of the mother, elimination of drug from the newborn child, especially the premature, can be very slow."*

```text
임신 중                  분만 순간                분만 후
─────────                ───────                  ─────────
fetus = 모체 tissue       탯줄 단절                신생아 = 독립 PK
C_u(fetus) ≈ mother      CL_mother 차단            자기 F_mat로만 작동
t1/2 ≈ mother            약물 잔류                 t1/2 급격히 길어짐
                                                  → TDM 필수
```

분만 직전까지 fetus는 모체 CL에 "기생". 탯줄이 끊어지는 순간 신생아는 **자기 $F_{mat}$로만** 작동 — 그런데 §6-1에서 본 것처럼 신생아 $F_{mat}\ll 1$. 모체로부터 받은 약물이 매우 천천히 빠짐. **미숙아일수록 더 느림.**

#### 모유 수유 — 두 위험 인자

R&T 직접 [R&T p.430]: *"The risks are greatest for drugs that are (i) **poorly cleared by the infant** and (ii) have a **narrow therapeutic index**."*

두 조건 겹치면 모유로도 영아 축적 가능. 시각 예시 — bupropion 모유-혈장 농도 비 [R&T Fig.14-21, p.431].

#### 임신부 의사결정 골격

```text
임신부 약물 처방
   │
   Step 1: Albumin binding 강한가?
       예 → total ↓ 보고 dose 증량 금지 [R&T p.429]
       아니오 → albumin 변화에 둔감
   │
   Step 2: 태반 통과하는가? (lipophilicity·MW·ionization)
       예 → fetus unbound ≈ mother unbound, 모체 모니터링 [R&T p.430]
       아니오 → fetus 노출 무시 가능
   │
   Step 3: 분만 직후 신생아 PK
       대부분 F_mat ≪ 1 → TDM 필수 [R&T p.430]
   │
   Step 4: 수유 시
       영아 CL 낮 + 약물 좁은 TI → 모유 노출 모니터링 [R&T p.430]
```

---

## §7. 가장 헷갈리는 5가지 분기점 — 한 표로 정리

### Pair 1. CL 지수 $b$ vs V 지수 $d$

| | $b$ (CL) | $d$ (V) |
|---|---|---|
| 변수 성격 | 흐름/속도 | 공간/범위 |
| 전형값 | 0.75 | 1.0 |
| 식 | $CL=a\cdot BW^b$ | $V=c\cdot BW^d$ |
| 혼동 시 | mg/kg 선형 사고로 dose 과대 | 시간축 부호 뒤집힘 |

**치명타** — Mouse → Human에서 7.4~7.7배 격차. 종 pair와 fold를 같이 외울 것.

### Pair 2. Kallynochron vs Apolysichron

| | Kallynochron | Apolysichron |
|---|---|---|
| 시간축 | $t/BW^{1-b}$ | $t/BW^{d-b}$ |
| 가정 | $d=1$ | $d\ne 1$ 허용 |
| 사용 | Elementary Dedrick | Complex Dedrick |

**기억 고리** — K는 **k**g, A는 **a**nyspace.

### Pair 3. BW Allometry vs BSA Scaling

| | $BW^b$ allometry | BSA scaling |
|---|---|---|
| 식 | $Y=a\cdot BW^b$ | $BSA\approx 1.73(BW/70)^{0.75}$ |
| 본질 | 자연 환율식 | $BW^{0.75}$의 임상 근사 표기 |
| R&T 단서 | — | 적용 한계(age, composition, renal) 명시 의무 [R&T p.435] |

⚠️ **R&T가 BSA 식을 두 개 제시함** — Eq.14-1(BW+Height형)과 Eq.14-2(BW-only 0.75형). 0.75는 *"BSA의 진짜 알로메트릭 지수"가 아님* — 실제 종간 BSA 지수는 약 2/3 (0.67). R&T가 0.75로 채택한 건 **알로메트리 챕터의 CL/GFR prior와 매칭하는 편의식** [R&T Ch.22 p.734].

### Pair 4. mg/kg vs mg/1.73 m² vs BW^0.75

| | mg/kg | mg/1.73 m² | BW^0.75 |
|---|---|---|---|
| 관행 분야 | 항암·항생제 | 소아 신장배설 | 현대 PopPK |
| R&T 권장 조건 | 적용 한계 명시 시 [p.435] | 신장배설 약물 [p.435] | 기본 backbone [Eq.14-6] |
| 비만 환자 위험 | dose 과대 | — | $F_{mat}$ 누락 |

**기억 고리** — 같은 15 kg 소아에 60 kg 성인 600 mg → mg/kg은 150 mg, 다른 둘은 213 mg. **약 30% 차이**가 매번 발생.

### Pair 5. 임신부 Total vs Unbound

| | Total exposure | Unbound exposure |
|---|---|---|
| 임신 후반기 변화 | **감소** (albumin 50~60%) | **거의 불변** |
| 약리 효과 결정 | 간접 | **직접** |
| Dose 조정 권고 | total만 보고 증량 = **toxic 위험** | albumin만으로는 조정 불필요 |
| Fetus 노출 surrogate | 무효 | **모체 unbound와 평형** |

**치명타** — *"눈에 보이는 total은 줄어도 약리 효과를 만드는 unbound는 그대로."* R&T p.429를 외울 것.

---

## §8. 자기점검 — 압축 핵심 13문항

1. **회상** — $Y=a\cdot BW^b$에서 $a$, $b$의 의미와 CL/V 전형 지수
2. **회상** — Mouse 23g → Human 70kg, Rat 250g → Human에서 $b=1$ vs $b=0.75$ 격차
3. **도출** — $t_{1/2}\propto BW^{d-b}$와 $k_{el}\propto BW^{b-d}$를 한 줄로
4. **Dedrick** — Elementary vs Complex 변환, 전환 규칙 (log-log V vs BW slope 0.9~1.1)
5. **출처 무결성** — PK28 rat $t_{1/2}$ 불일치(2.9 vs 3.9 h), PK29 두 set 인용 방식
6. **적용** — Mouse 25g, CL=0.012 L/hr → Human CL ($b=0.75$ vs $b=1$), 차이 약 7.3배
7. **소아·노인** — 왜 $BW^{0.75}$만으론 부족한가 (chronologic ≠ functional age)
8. **보스 딜레마** — Two-species 회귀 $b=0.62$ vs prior $b=0.75$, primary는 prior + sensitivity 표
9. **[보강본] BSA 식** — Eq.14-1 vs Eq.14-2, 0.75 지수의 R&T 편의 매칭 의미
10. **[보강본] 두 환자** — 미숙아(maturation), 비만 여성 130 kg(LBW vs TBW, 약물 극성)
11. **[보강본] 신장·간 분기** — $fe=0.85$ vs $fe=0.10$ 약물의 75세·60kg·RF=0.6 환자 $R_d$
12. **[보강본_final] Dosing strategy** — 600 mg/60 kg 성인 → 15 kg 소아, 140 kg 비만에서 세 strategy 정량 비교
13. **[보강본_final] 임신부 phenytoin** — Total 5 mg/L 시 (i) dose 증량? (ii) fetus 노출? (iii) 분만 직후?

---

## §9. 최종 마인드맵 — 7단계 의사결정 알고리즘

```text
Step 1. 변수의 종류부터 물음
    - flow/rate? (CL, GFR, 혈류)        → b ≈ 0.75
    - space/extent? (V, 혈액량, 조직량)  → d ≈ 1.0
    - time? (V/CL)                     → d-b ≈ 0.25
    - rate constant? (CL/V)            → b-d ≈ -0.25

Step 2. Prior 타당성 — 6개 실패 트리거 체크
    f_u 차이 / CYP isoform / 비선형 / 장간순환 / route 차이 / V 비율 drift

Step 3. 시간축 도출 — t1/2와 k_el 부호 둘 다 동시에

Step 4. Dedrick 진단
    log-log V vs BW slope:
      0.9~1.1 안 → Elementary (PK28 type)
      밖         → Complex (PK29 type)

Step 5. Equal-AUCu backbone 적용 (Eq.2:420)
    + PD metric, f_u 보정, 선형성, safety margin, route/formulation 5 layer

Step 6. [보강본] 사람 안 보정 3 layer
    A. Maturation: F_mat(PMA) — 신생아·영아 핵심
    B. Body composition: 약물 극성으로 LBW vs TBW 선택
    C. Organ function: fe·RF + (1-fe)·(140-Age)·Wt^0.75/1936

Step 7. [보강본_final] 표기·임신부 2 layer
    D. Dosing strategy: mg/kg vs mg/m² vs BW^0.75
       — R&T 요구 "limits of application" 명시 의무
       — 항암제 BSA는 "surface area explains variability better" 검증 시만
    E. Pregnancy:
       - Albumin ↓ → total ↓이지만 unbound 보존 → dose 증량 금지 [R&T p.429]
       - 태반 통과 약물 → fetus unbound ≈ mother unbound [R&T p.430]
       - 분만 직후 신생아 → 자기 F_mat로만 작동, TDM 필수 [R&T p.430]
```

---

## §10. 한 줄로 닫기

이 챕터의 진짜 메시지는 *"$0.75$를 외워라"*가 아님. 진짜 메시지는 다음 한 줄임:

> **"$0.75$를 자연 환율 prior로 두고, 그게 언제 깨지는지 6가지 트리거로 진단하며, Dedrick으로 자료에서 검증하고, Equal-AUCu backbone으로 dose에 옮기되, 사람 안에서는 그 위에 maturation × body composition × organ function × dosing strategy × pregnancy 다섯 층을 곱해서 처방에 도달한다."**

알로메트리는 공식 암기가 아니라 — **종간 환율표 → 노출 backbone → 사람 안 dose 결정 엔진** 으로 이어지는 단일 사고 흐름임. 이 흐름이 자동 작동하면 Phase 1 회의실 화이트보드 앞에서, NDA 심사 질의 자리에서, 신생아·임신부 처방 결정 자리에서 — 같은 한 장의 환율표를 꺼내서 답할 수 있음.

---

**C-260517-104723-Q8M**

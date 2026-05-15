# 세션 14 — Allometric Scaling: Interspecies · Dedrick · Equal-AUC$_u$ · FIH dose backbone — v3.9

## 임상 장면: 왜 이 세션이 필요한가

Phase 1 회의에서 **23-g mouse**의 CL을 **70-kg human**으로 옮길 때, $b=1$을 쓰면 $b=0.75$보다 첫 사람 노출 추정이 **약 7.4배** 커집니다 [G&W PK28 p.611–614]. R&T의 20-g mouse → 70-kg human 예시에서는 **3500 vs 455 (7.7배 차이)**가 나옵니다 [R&T p.733]. 이건 단순한 계산 취향 차이가 아니라, **target AUC를 맞추려고 용량을 정할 때 CL을 과대평가하면 용량도 과대 산출된다**는 규제 검토 지점입니다.

## §0.5 빠른 읽기 경로

시간이 부족하면 **C1 → C2 → C3 → C4 → C5** 순서로 읽으면 됩니다. §5는 세 가지 혼동(특히 $b$ vs $d$)을 차단하는 용도이고, §7은 능동 회상, §8은 큰 그림 마무리입니다.

| 카드 | 이 경로에서의 역할 |
|---|---|
| **C1** | $Y=a\cdot BW^b$가 회귀선이 아니라 **스케일 법칙**임 |
| **C2** | CL 지수 $b\approx0.75$ — $b=1$ 오류 차단 |
| **C3** | V 지수 $d\approx1.0$ — 시간축이 왜 $d-b$로 나오는가 |
| **C4** | Dedrick — 곡선이 한 축 위에 겹치는지 진단 |
| **C5** | Equal-AUCu dose backbone — 최종 FIH 용량이 아닌 골격 |

**시작 전 점검:** CL, V, AUC, 반감기, 비결합 분율(fu), 일차 제거가 정의되는가.  
**완료 후 점검:** ① $b=0.75$와 $b=1$이 왜 호환 불가인가, ② 시간이 왜 $d-b$로 스케일링되는가, ③ 소아·노인 용량에서 왜 체중 외에 기능적 연령과 장기 기능 보정이 더 필요한가.

<!-- SLIDE_START: §1 | title: 세션 개요와 로드맵 -->
<!-- SECTION_CORE: SC-01 -->

## §1 — 세션 개요와 로드맵(Session Header & Roadmap)

**Source:** Gabrielsson & Weiner 5e §2.10 (p.170–191), Case Study PK28 (p.611–614), Case Study PK29 (p.615–620); Rowland & Tozer 5e Ch.14 (p.411–441), Ch.22 allometry section (p.731–743).

### 개념 지도 (3-layer)

```text
Layer 1 — 무엇인가
  Allometry / CL / V / Dedrick / AUCu backbone

Layer 2 — 어떻게 계산되는가
  Y=a·BW^b → CL∝BW^b, V∝BW^d → t1/2∝BW^(d-b), kel∝BW^(b-d)

Layer 3 — 언제, 왜 중요한가
  b=1 오류 차단 → Dedrick 중첩 진단 → equal-AUCu dose backbone → 소아·노인·FIH caveat
```

### 지식 그래프 위치

```text
[선행: CL·V·AUC·반감기·비결합 분율] → [이 세션: allometric spine] → [후속: PopPK WT covariate / PBPK scaling / FIH exposure table]
```

🧭 **읽는 순서:**  
카드 1 (C1): $Y=a\cdot BW^b$는 왜 단순 회귀가 아니라 척도 불변(scale-invariance) 주장인가?  
카드 2 (C2): CL 지수 $b\approx0.75$는 언제 prior이고, 언제 의심해야 하는가?  
카드 3 (C3): V 지수 $d\approx1$과 CL 지수 차이가 왜 시간축을 만드는가?  
카드 4 (C4): Dedrick plot은 어떤 지수 가정이 버티는지 어떻게 드러내는가?  
카드 5 (C5): Equal-AUCu dose backbone을 왜 최종 FIH 용량으로 쓰면 안 되는가?

### 핵심 아이디어(Big Idea)

$Y=a\cdot BW^b$는 단순 회귀식이 아닙니다. **종간 체중 차이를 PK 파라미터(CL, V, dose) 차이로 번역하는 거듭제곱 언어**입니다. 가장 흔한 함정은 $b=0.75$와 $b=1$의 차이를 작게 보는 것입니다 — 작은 동물에서 사람으로 옮길 때 그 차이는 **수 배에서 거의 한 자릿수까지** 벌어집니다.

| 비교 | 차이 |
|---|---|
| **20-g mouse → 70-kg human** ($b=1$ vs $b=0.75$) | 3500 vs 455 = **7.7배** [R&T p.733] |
| **23-g mouse → 70-kg human** (PK28) | **약 7.4배** |
| **Rat 250-g → 70-kg human** | **약 4.1배** |

이건 "용량을 낮게 시작/높게 시작" 같은 단순 구호가 아니라, **target AUC 기반으로 용량을 잡을 때 CL이 과대평가되면 dose도 과대 산출된다**는 방향성 문제입니다.

$$
\overbrace{b=1}^{\text{kg당 선형}}\quad vs\quad \overbrace{b=0.75}^{\text{CL prior}}
$$

> **▶ 목표 사고 모델(Target Mental Model)**  
> 이 세션을 마치면 다음 4단계가 자동 회상되어야 합니다.
>
> 1. **변수의 종류부터 묻습니다.**
>    - 흐름/속도(flow/rate)인가? CL, GFR, 혈류 → $b\approx 0.75$
>    - 공간/분포 범위(extent)인가? V, 혈액량, 조직량 → $d\approx 1$
>    - 시간인가? $V/CL \to BW^{d-b}$ (≈0.25)
>    - 속도상수인가? $CL/V \to BW^{b-d}$ (≈−0.25)
> 2. **종간 용량 번역은 비결합 노출(AUCu) 관점**으로 읽습니다. AUCu equality이면 $Dose \propto BW^b$, mg/kg 비는 $BW^{b-1}$.
> 3. **예외를 먼저 찾습니다** — fu 차이, CYP isoform 차이, 비선형 PK, 수송체, 장간 순환, 투여 경로·제형 차이.
> 4. **출처 언어를 지킵니다** — PDF가 직접 뒷받침하는 것(G&W/R&T 수식, PK28/PK29 anchor, R&T age/renal/BSA caution)과 직접 뒷받침하지 않는 것(ICH/FDA/MABEL/NONMEM/QSP 단정)을 분리합니다.
>
> 이 4단계가 §8 E의 최종 사고 모델 그대로이며, §1–§8 전체가 이 4단계를 정당화하는 과정입니다.

### 개념 항법도

```text
[C1] Master Equation: Y = a·BW^b
        │
        ├──▶ [C2] CL exponent b≈0.75 ─────────────┐
        │                                           ├──▶ [C5] Equal-AUCu dose backbone
        └──▶ [C3] V exponent d≈1.0 ────────────────┘
                  │
                  ├──▶ t1/2 ∝ BW^(d-b)≈BW^0.25
                  ├──▶ kel ∝ BW^(b-d)≈BW^-0.25
                  └──▶ [C4] Dedrick Superposition
```

**선행 전제:** CL, V, AUC, 반감기 정의 / 일구획 지수 감소 / 혈장 단백 결합과 비결합 청소율.  
**직접 후속:** 소아·노인 용량 조정, PopPK 체중 공변량 선택, PBPK 장기 혈류·부피 스케일링, FIH 노출 번역 표.  
**주의:** NONMEM control stream, ICH/FDA/MABEL 표현, QSP 구현은 본 PDF가 직접 다루지 않으므로 `[교과서 외 구현/실무 해석]`으로만 다룹니다.

**§1 요약:** 이 세션의 중심축은 $Y=a\cdot BW^b \to CL\ b\approx0.75 \to V\ d\approx1 \to time\ d-b\approx0.25 \to Dedrick \to equal\text{-}AUCu\ dose\ backbone$입니다. 반드시 잡아야 할 교정 지점은 **4.1/7.4/7.7-fold를 species pair와 함께 분리해서 외우는 것**과, **Eq.2:420을 standalone FIH 시작 용량 공식이 아니라 노출 backbone으로 낮춰 쓰는 것**입니다.

---

> 📊 **개념 도식 (HTML 렌더링용):** 알로메트릭 중심축 — 변수 유형 → 지수 → 시간/용량. $Y=a\cdot BW^b$는 독립 수식이 아니라 CL, V, time, Dedrick, equal-AUCu 용량 번역을 연결하는 척추입니다.

$$
\underbrace{Y=a\cdot BW^b}_{\text{마스터식}}\rightarrow\underbrace{CL\sim BW^{0.75}}_{\text{CL 흐름}}\; /\;\underbrace{V\sim BW^1}_{\text{V 공간}}\rightarrow\underbrace{t_{1/2}\sim BW^{d-b}}_{\text{시간축}}\; /\;\underbrace{k_{el}\sim BW^{b-d}}_{\text{제거속도}}\rightarrow\underbrace{Dose\sim BW^b}_{\text{AUCu 용량}}
$$

<!-- SLIDE_START: §2 | title: 개념 해부 카드 -->
<!-- SECTION_CORE: SC-02 -->

## §2 — 개념 해부 카드(Concept Anatomy Cards)

---

<!-- SLIDE_START: C1 | title: 마스터 알로메트릭 방정식 -->
<!-- SECTION_CORE: SC-03 -->

### ━━ C1. 마스터 알로메트릭 방정식(Master Allometric Equation): $Y=a\cdot BW^b$ ━━

> **거장의 시각**  
> $Y=a\cdot BW^b$를 단순 회귀선으로 보면 기울기 점추정값에 과신하게 됩니다. 이 식을 **"체중 배율이 달라져도 같은 법칙이 유지된다"는 주장**으로 보면, C2–C5의 모든 판단이 "이 약물에서 이 지수 prior가 유지되는가?" 하나의 질문으로 정렬됩니다.

#### A. 정형 정의(Formal Definition)

$$
\underbrace{Y}_{\text{대상 변수}}=\underbrace{a}_{\text{절편}}\cdot \underbrace{BW}_{\text{체중}}^{\overbrace{b}^{\text{지수}}}
$$
[G&W Eq.2:374, p.173; R&T Eq.22-2, p.732]

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $Y$ | 변수별 상이 | 스케일링 대상 PK/생리 변수 | CL, V, dose 등 선택 변수 |
| $a$ | $Y/BW^b$ | 화합물·변수 의존 절편 | 약물 특성, 단위, 기준 체중 |
| $BW$ | kg 또는 g | 체중 기반 크기 척도 | 종, 연령, 체조성 |
| $b$ | 무차원 | 체중 변화에 대한 지수 | 변수 유형, 자료 품질, 결합·기전 차이 |

> 💡 로그-로그 직선은 회귀선이 아니라 **"체중 배율이 바뀌어도 같은 법칙이 유지된다"는 주장**입니다. 그래서 회귀선을 보기 전에 먼저 이 변수가 flow인지, extent인지, time인지를 물어야 합니다.

> ⚠️ $b$는 자연상수가 아니라 **변수 유형과 자료가 함께 만드는 prior**입니다.

양변 로그 변환:

$$
\underbrace{\ln(Y)}_{\text{로그 }Y}=\underbrace{\ln(a)}_{\text{로그 절편}}+\overbrace{\underbrace{b}_{\text{기울기}}\cdot\underbrace{\ln(BW)}_{\text{로그 }BW}}^{\text{log-log}}
$$
[G&W Eq.2:379, p.176; R&T Eq.22-1, p.732]

- **$a$:** 약물·화합물 의존적 절편. 단위는 $b$에 따라 달라집니다.
- **$b$:** 대체로 변수 유형이 정합니다. 다만 실제 CL 지수는 자료 품질, 종 수, 비선형성, 종간 단백 결합 차이에 따라 흔들립니다 [G&W p.177–178].

#### B. 도출(Derivation) — 왜 거듭제곱 함수인가

G&W는 **대사율 ∝ $BW^{0.75}$**, **에너지 함량 ∝ $BW^1$** → 순환 시간(turnover time) ∝ $BW^{0.25}$로 정리합니다 [G&W Eq.2:375–377, p.173]. 한 문장으로: **"체중이 커지면 절대 처리량은 늘지만, 단위 체중당 처리 효율은 떨어진다."**

기하학적으로도 같은 방향입니다. 표면적은 길이의 제곱, 부피는 세제곱이므로 표면적은 부피의 $2/3$승에 비례합니다. 다만 실제 생리학 변수는 단순 외부 표면적보다 복잡해서 Brody의 경험적 지수는 0.5–0.8 범위로 나타납니다 [G&W p.173–174].

#### C. 구조적 의미(Structural Meaning)

> 💼 **실무 인사이트:** 로그-로그 직선이 잘 맞는다는 건 "회귀가 잘 맞는다"가 아니라 **"체중 배율이 달라져도 같은 지수 법칙이 유지된다"**는 가정이 통한다는 뜻입니다. 이 가정이 깨지는 순간이 알로메트리 실패의 시작입니다.

#### D. 경계 조건(Boundary Conditions)

알로메트리가 잘 통하는 경우: 약물 분포가 물리적 수송 과정에 지배되고, 혈장 단백 결합의 종간 차이가 크지 않은 화합물. 잘 안 통하는 경우: **종간 대사·배설의 질적 차이, CYP450 isozyme 구성 차이, 단백 결합 차이가 큰 화합물** [G&W p.173].

#### E. 제텔카스텐 원자(Zettelkasten Atom)

```yaml
aliases: [allometric law, allometric power function, Y=a·BW^b]
tags: [pharmacometrics/allometry, scaling/inter-species]
source: "G&W §2.10.3 p.173–176; R&T Ch.22 p.731–733"
```

---

> **C1 체화 핵심**  
> ① 종간 PK 차이를 한 식으로 묶을 때 → $Y=a\cdot BW^b$는 **회귀가 아닌 척도 불변 주장**입니다.  
> ② 기울기 점추정값과 생리학적 prior가 충돌하면 → **자료 품질·종 수·기전 차이**가 해석을 정합니다.  
> ⚡ $b$를 자연상수처럼 고정 → 기전 신호를 회귀 잔차로 오독 → C2–C5 추론이 무너집니다.

<!-- SLIDE_START: C2 | title: 청소율 지수 -->
<!-- SECTION_CORE: SC-04 -->

### ━━ C2. [⚡ Apex Concept] 청소율 지수(Clearance Exponent) $b\approx0.75$ ━━

> **앞 카드에서 이 카드로**  
> C1에서 $b$가 척도 불변 prior임을 잡았으니, 이제 가장 위험한 변수인 CL에서 그 prior가 어떤 임상 격차를 만드는지를 봐야 합니다.

> **거장의 시각**  
> mg/kg 처방에 익숙하다 보면 CL도 체중에 선형 비례한다고 생각하기 쉽지만, CL은 **기능적 흐름 변수**라 $b\approx0.75$가 출발 prior입니다. 다만 G&W는 실제 CL 지수가 **0.2부터 1을 넘는 값까지** 갈 수 있다고 경고합니다 [G&W p.178]. **체화할 한 줄: "flow는 0.75로 시작하되, fu·수송체·포화·종간 대사 차이가 보이면 즉시 sensitivity로 격하한다."**

#### A. 정형 정의(Formal Definition)

$$
\underbrace{CL_i}_{\text{개체 CL}}=\underbrace{a}_{\text{CL 절편}}\cdot\underbrace{BW_i}_{\text{개체 BW}}^{\overbrace{b}^{\text{CL 지수}}}
$$
[G&W Eq.2:380, p.176; PK28 Eq.28:1, p.611]

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $CL_i$ | volume/time | 개체별 청소율, 단위 시간당 처리 흐름 | 혈류, GFR, 대사능, 수송체 |
| $a$ | CL/$BW^b$ | CL allometry 절편 | 화합물 특성, 종간 자료 범위 |
| $BW_i$ | kg 또는 g | 개체 체중 | 종, 연령, 체조성 |
| $b$ | 무차원 | CL 체중 지수 | ↑ 수송체/대사 차이, ↓ 결합·자료 leverage 부족 |

> 💡 CL은 "몸 안 공간의 크기"가 아니라 **"시간당 얼마나 처리되는가"**입니다. $b=0.75$도 법칙이 아니라 prior이며, 실제 CL 지수는 약 0.2에서 1을 넘는 값까지 변할 수 있습니다 [G&W p.178]. → **FIH 방어 규칙: primary 지수와 sensitivity 지수를 같은 표에 둬야 dose narrative가 방어됩니다.**

G&W Fig.2.159는 91개 화합물의 CL 지수가 주로 **0.5–1.0 범위**에 놓임을 보여 줍니다 [G&W p.191].

#### B. 그럴듯한 오해(Plausible Fallacy) — $b=1$ 선형 kg당 스케일링

**오류:** "mg/kg 처방에 익숙하니 청소율도 kg에 선형 비례한다"고 생각하는 것 — **선형 kg당 스케일링**(kg당 값이 일정하다는 가정).

**교정:** CL은 흐름·속도 변수이므로 $b\approx0.75$가 생리학적 prior입니다.

- **R&T 20-g mouse → 70-kg human:** $b=1$이면 3500, $b=0.75$이면 455 → **7.7배 차이** [R&T p.733].
- **G&W PK28 23-g mouse → 70-kg human:** $(70/0.023)^{0.25}\approx$ **7.4배 차이**.
- **Rat 250-g → 70-kg human:** $(70/0.25)^{0.25}\approx$ **4.1배 차이**.

$$
\underbrace{\left(\frac{BW_{human}}{BW_{animal}}\right)^{1-0.75}}_{\text{b=1/0.75}}=\underbrace{\left(\frac{BW_{human}}{BW_{animal}}\right)^{0.25}}_{\text{종 격차}}
$$

Target AUC 기반 용량 계산에서는 **CL을 과대평가하면 목표 AUC를 맞추기 위한 dose도 과대 산출됩니다.** ("CL 과대평가 → subtherapeutic 시작"이라는 단정은 쓰지 않습니다.)

#### C. 실패 조건(Failure Conditions)

알로메트리 실패는 단순 무작위 오차가 아니라 **기전 신호일 수 있습니다.** G&W Fig.2.145에 따르면 스케일링이 잘 되는 화합물은 70-kg human CL 예측구간이 약 **10-fold** 범위이지만, 잘 안 되는 화합물은 약 **1000-fold**까지 넓어집니다 [G&W p.174].

주요 실패 트리거 6가지:
① 종간 혈장 단백 결합 차이, ② 대사 경로 또는 CYP isozyme 조성 차이, ③ 비선형 미카엘리스-멘텐 거동, ④ 장간 순환, ⑤ 투여 경로·제형 차이, ⑥ 중심·말초 분포용적 비율 변동 [G&W p.191].

> **[TRENCH — 비결합 청소율($CL_u$) 스케일링]**  
> 종간 fu 차이가 크면 total CL이 아니라 $CL_u=CL/f_u$를 스케일링합니다. G&W Eq.2:421은 $CL_{u,man}=CL_{u,rat}\cdot(BW_{man}/BW_{rat})^b$ 형태로 제시되며 [G&W p.190], R&T Table 22-1은 cefazolin 같은 약물에서 human-animal 단백 결합 차이가 클 수 있음을 보여 줍니다 [R&T p.740]. fu 비교는 가능하면 **같은 농도·buffer·온도·assay**에서 측정된 값끼리 해야 합니다.

#### D. 전문가 진단 트리거

> 💼 **실무 인사이트:** PopPK 또는 종간 회귀에서 **$b>1$**이 나오면 "추정값을 그대로 믿을 것인가?"가 아니라 "**단백 결합, 수송체, 포화, 자료 품질** 중 무엇이 기울기를 밀어 올렸는가?"를 먼저 묻습니다. 반대로 두 종만으로 얻은 **$b<0.5$**는 생리학적 신호보다는 **통계적 지렛대 부족** 쪽일 가능성이 큽니다.

#### E. 제텔카스텐 원자

```yaml
aliases: [clearance allometric exponent, b_CL, Brody-Kleiber clearance scaling]
tags: [pharmacometrics/allometry, clearance, FIH/exposure-translation]
source: "G&W §2.10.3 p.176–180; G&W Fig.2.159 p.191; R&T Ch.22 p.732–735"
```

CL의 $b\approx0.75$가 시간당 처리량의 지수라면, V는 왜 $d\approx1$일까요? V가 "흐름"이 아니라 "공간"이기 때문입니다 (→ C3).

> 📖 **Rowland & Tozer 5e, Ch.22, p.733, Fig.22-2:** $b=1$과 $b=0.75$의 7.7배 mouse-human 격차를 **계산이 아니라 눈으로 확인하게** 해 주는 가장 명확한 원출처 그림입니다.

> 📖 **Gabrielsson & Weiner 5e, §2.10.3, p.174, Fig.2.145:** allometry가 유용한 예측을 주는 화합물과 예측구간이 위험하게 넓어지는 화합물을 분리해서 보여 줍니다 → 실패가 잡음이 아니라 **기전·자료 품질 신호**라는 C2의 메시지를 직접 뒷받침합니다.

---

**Plausible Fallacy — C2 Apex**

- **오류:** $b=1$ mg/kg 선형 scaling 또는 $b=0.75$ 고정 prior 하나로 human CL/dose 문제가 해결된다고 판단합니다.
- **왜 그럴싸한가:** 저용량·소수 종 자료에서는 log-log 직선이 그럴듯해 보이고, R&T/G&W 모두 $0.75$ prior의 생리학적 근거를 제시하기 때문입니다.
- **나비효과:** 지수 선택 오류 → human CL **4.1/7.4/7.7배 격차** → [임상] target AUC 기반 dose 과대/과소 산출, 독성·치료 실패 위험 → [모델링/규제] NONMEM/종간 회귀 지수 정당화 요구, sensitivity 재제출, Deficiency Letter성 질의 가능.

> **C2 체화 핵심**  
> ① Target AUC 기반 human CL/dose 예측 → CL 지수 $b\approx0.75$가 첫 노출 추정을 결정합니다.  
> ② mg/kg 선형 사고는 CL/dose 과대, $b=0.75$ 과신은 기전 예외 누락 — **둘 다 위험**입니다.  
> ⚡ $0.75$를 법칙처럼 적용 → fu·수송체·포화·대사 차이 누락 → Phase 1 노출 오판 및 지수 정당화 요구.

<!-- SLIDE_START: C3 | title: 분포용적 지수 -->
<!-- SECTION_CORE: SC-05 -->

### ━━ C3. 분포용적 지수(Volume Exponent) $d\approx1.0$ ━━

> **앞 카드에서 이 카드로**  
> C2가 CL을 시간당 흐름으로 잡았으니, 이제 V를 **공간 변수**로 분리해야 반감기와 제거속도의 지수 부호가 맞아 들어갑니다.

> **거장의 시각**  
> V를 CL처럼 흐름 변수로 읽으면 $t_{1/2}$와 $k_{el}$의 지수 부호가 동시에 뒤집힙니다. V를 **분포 공간**으로 보면, $d\approx1$과 $b\approx0.75$의 차이 $d-b$가 시간축 전체를 만든다는 사실이 즉시 보입니다.

#### A. 정형 정의(Formal Definition)

$$
\underbrace{V_i}_{\text{개체 }V}=\underbrace{c}_{\text{V 절편}}\cdot\underbrace{BW_i}_{\text{개체 BW}}^{\overbrace{d}^{\text{V 지수}}}
$$
[G&W Eq.2:382, p.179; PK28 Eq.28:2, p.611]

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $V_i$ | volume | 개체별 분포용적 | 체수분, 조직량, 지방 분포, 결합 |
| $c$ | V/$BW^d$ | V allometry 절편 | 조직 친화성, 화합물 특성 |
| $BW_i$ | kg 또는 g | 개체 체중 | 종, 연령, 체조성 |
| $d$ | 무차원 | V 체중 지수 | 조직 친화성, 지방 분포, 수송체, 단백 결합 |

> 💡 V는 처리 능력이 아니라 **약물이 퍼질 수 있는 공간의 크기**입니다. CL의 $b$와 V의 $d$를 바꿔 쓰면 half-life와 rate constant 부호가 **동시에 틀어집니다.** → **시간축 규칙: 시간은 $V/CL$이니까 $d-b$가 지배합니다.**

G&W Table 2.22는 **혈액량 지수 0.99, 골격근량 1.09, Vd ≈ 1.0**을 제시합니다 [G&W p.180].

#### B. 결과(Consequence) — 반감기와 속도상수

$$
\underbrace{t_{1/2}}_{\text{반감기}}=\underbrace{\ln2}_{\text{반감 상수}}\cdot\frac{\overbrace{V}^{\text{공간}}}{\overbrace{CL}^{\text{흐름}}}=\ln2\cdot\frac{\underbrace{c\cdot BW^d}_{\text{V 스케일}}}{\underbrace{a\cdot BW^b}_{\text{CL 스케일}}}\propto \underbrace{BW^{d-b}}_{\text{시간지수}}
$$

$d\approx1$, $b\approx0.75$이면:

$$
\underbrace{t_{1/2}}_{\text{반감기}}\propto \underbrace{BW^{0.25}}_{\text{큰 종↑}},\qquad \underbrace{k_{el}}_{\text{제거속도}}=\frac{\overbrace{CL}^{\text{흐름}}}{\overbrace{V}^{\text{공간}}}\propto\underbrace{BW^{b-d}}_{\text{큰 종↓}}\approx BW^{-0.25}
$$

"$t_{1/2}\propto BW^{0.25}$"만 외우면 절반만 본 것입니다. 더 중요한 사실은 **큰 동물일수록 모든 일차 속도상수가 작아진다**는 것 — 같은 $V/CL$을 시간으로 읽으면 반감기, 뒤집어 $CL/V$로 읽으면 속도상수입니다. **큰 동물은 절대 CL이 크지만, 단위 시간당 제거되는 분율은 작습니다.**

#### C. 데이터 앵커 — Methadone (PK28)

**Methadone** (μ-opioid 작용제, 저추출 약물; PK28 사례)의 종간 자료:

| 종 | BW | Dose | 비고 |
|---|---:|---:|---|
| Mouse | 23 g | 25 µg IV bolus | 기본 Dedrick 앵커 |
| Rat | 250 g | 500 µg IV bolus | 출처 내부 $t_{1/2}$ 불일치 있음 |
| Man | 70 kg | 100,000 µg IV bolus | human 앵커 |

- $a=0.319$, $AUC=1/a=3.13$ [G&W §2.10.6 p.186; PK28 p.613]
- 간 추출률 **<10%** (저추출) [G&W p.186; PK28 p.613]
- **$t_{1/2}$ 불일치:** G&W §2.10.6 본문은 1.5/2.9/35 h, PK28 case는 1.5/**3.9**/35 h로 rat 값이 다릅니다. **인용할 때는 `[§2.10.6 set]` 또는 `[PK28 case set]`을 반드시 명시**합니다 (둘 중 하나로 임의 고정 금지).

#### D. 한계(Limitations)

V 지수는 대체로 1에 가깝지만 $V_{ss}$는 조직 친화성·지방 분포·수송체·단백 결합에 따라 **0.8–1.2 범위로 흔들립니다.** R&T의 비만 예시도 같은 메시지를 줍니다 — **"체중이 늘 생물학적으로 의미 있는 분포용적은 아니다"** [R&T p.439].

> 📊 **개념 도식 (HTML 렌더링용):** 흐름과 공간의 분리 — CL은 흐름이라 $b\approx0.75$, V는 공간이라 $d\approx1$. 두 지수의 차이가 시간과 속도상수를 반대 방향으로 만듭니다.

$$
\underbrace{CL=a\cdot BW^b}_{\text{CL 흐름}}\quad vs\quad\underbrace{V=c\cdot BW^d}_{\text{V 공간}}\quad\Rightarrow\quad\underbrace{t_{1/2}\propto BW^{d-b}}_{\text{시간↑}}\; ,\;\underbrace{k_{el}\propto BW^{b-d}}_{\text{분율 속도↓}}
$$

---

> **C3 체화 핵심**  
> ① 큰 동물에서 half-life가 길어지는 이유 → $d-b\approx0.25$가 정합니다.  
> ② 절대 CL은 증가하지만 제거 분율은 감소 → $CL/V$의 $b-d\approx-0.25$가 지배합니다.  
> ⚡ $t_{1/2}$만 암기 → $k_{el}$ 부호를 놓침 → CL/V 해석과 시간축 정규화 실패.

<!-- SLIDE_START: C4 | title: Dedrick 중첩 -->
<!-- SECTION_CORE: SC-06 -->

### ━━ C4. Dedrick 중첩(Dedrick Superposition): 기본형(Elementary) + 복합형(Complex) ━━

> **앞 카드에서 이 카드로**  
> C2·C3에서 잡은 $b$와 $d$는 숫자로만 끝나지 않습니다. 실제 종간 PK 곡선이 **한 축 위에 겹치는지** 검증하는 도구가 Dedrick 변환입니다.

> **거장의 시각**  
> Dedrick plot을 예쁜 overlay 그림으로만 읽으면 fan-out을 "그림이 안 예쁘다"로 오해합니다. 이걸 **지수 구조의 진단 도구**로 보면, $d=1$ 가정 / 다구획성 / 모델 잘못 지정 중 무엇이 곡선 중첩을 깨뜨렸는지 추적할 수 있습니다.

#### A. 정형 정의(Formal Definitions)

**기본 Dedrick(Elementary)** — $d=1$ 가정:

$$
\underbrace{y}_{\text{농도축}}=\frac{\overbrace{C}^{\text{농도}}}{\underbrace{Dose/BW}_{\text{kg당 용량}}},\qquad \underbrace{x}_{\text{시간축}}=\frac{\overbrace{t}^{\text{시간}}}{\underbrace{BW^{1-b}}_{\text{기본 시간}}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $y$ | dose-normalized concentration | 종간 농도축 정규화 | dose, BW, V 지수 가정 |
| $x$ | normalized time | 종간 시간축 정규화 | $b$, $d$, 체중 범위 |
| $b$ | 무차원 | CL/flow 지수 | 대사·혈류·GFR prior 및 예외 |
| $d$ | 무차원 | V/extent 지수 | $d=1$ 여부가 elementary/complex를 가름 |

> 💡 **비유:** Dedrick plot은 서로 다른 속도로 재생되는 영상을 같은 프레임 속도에 맞춰 겹쳐 보는 작업입니다. 시간이 어긋나면 배우가 다른 게 아니라 **프레임 보정이 틀렸을** 수 있습니다. Elementary는 $d=1$을 숨은 가정으로 갖기 때문에, PK29처럼 $d\ne 1$이면 Complex로 넘어가야 합니다. → **Switch 규칙: log-log V vs BW 기울기가 0.9–1.1 밖이면 Complex Dedrick을 검토합니다.**

**복합 Dedrick(Complex)** — $d\ne 1$ 일반형:

$$
\underbrace{y}_{\text{농도축}}=\frac{\overbrace{C}^{\text{농도}}}{\underbrace{Dose/BW^d}_{\text{V지수 용량}}}=\frac{\overbrace{C}^{\text{농도}}\cdot\overbrace{BW^d}^{\text{공간 보정}}}{\underbrace{Dose}_{\text{투여량}}},\qquad \underbrace{x}_{\text{시간축}}=\frac{\overbrace{t}^{\text{시간}}}{\underbrace{BW^{d-b}}_{\text{복합 시간}}}
$$

Kallynochron은 $d=1$ 가정 아래의 **kg당 생리학적 시간**, Apolysichron은 $d$를 명시적으로 반영한 **일반화된 생리학적 시간**입니다 [G&W §2.10.6–2.10.7, p.184–189].

#### B. 도출(Derivation)

단일 지수 모델:

$$
\underbrace{C}_{\text{농도}}=\frac{\underbrace{D_{iv}}_{\text{IV dose}}}{\underbrace{V}_{\text{V 공간}}}\cdot \overbrace{e^{-(CL/V)t}}^{\text{일차 제거}}
$$

알로메트릭 치환:

$$
\underbrace{C}_{\text{농도}}=\frac{\underbrace{D_{iv}}_{\text{Dose}}}{\underbrace{c\cdot BW^d}_{\text{V 스케일}}}\cdot \overbrace{e^{-\left(\underbrace{a/c}_{\text{CL/V 절편}}\right)\cdot\underbrace{BW^{b-d}}_{\text{k 체중지수}}\cdot \underbrace{t}_{\text{시간}}}}^{\text{체중 보정 제거}}
$$
[G&W Eq.2:384, p.179]

농도는 $Dose/BW^d$로, 시간은 $BW^{d-b}$로 정규화되어야 합니다. 차원 해석(Buckingham π 정리류)의 PK 버전이라고 보면 됩니다 — 질량·시간·부피 차원을 제거하면 독립적인 무차원 그룹이 남고, Dedrick 변환은 그 그룹입니다.

#### C. AUC 관계식

기본 Dedrick 맥락에서 G&W는 AUC가 $1/a$로 정리됨을 보입니다 [G&W Eq.2:386, p.179]. 이건 C5의 'equal unbound AUC' 조건과 동떨어진 별개 사실이 아니라, **같은 논리가 수식으로 먼저 나타난 단계**입니다.

#### D. 데이터 앵커 — PK28과 PK29

**PK28 Methadone** (저추출, 5종 중 mouse/rat/man IV bolus 자료): 기본 Dedrick으로 중첩됩니다 [G&W p.184–186; PK28 p.611–614]. **단, case는 단일 dose level**이라 G&W도 ≥2 dose levels, 다회 투여·항정상태, 모델 잘못 지정 배제가 필요하다고 경고합니다 [PK28 p.614].

**PK29 Compound X** (5종: mouse 20 g, rat 250 g, monkey 3.5 kg, dog 14 kg, man 70 kg) [G&W p.186–189; PK29 p.615–620]:

| 출처 | $a$ | $b$ | $c$ | $d$ | $e$ | $g$ |
|---|---|---|---|---|---|---|
| G&W §2.10.7 [G&W p.189] | 0.021 | 0.74 | 0.076 | 1.18 | 0.56 | 0.075 |
| PK29 case [G&W p.619] | 0.021 | 0.75 | 0.10 | 1.21 | 0.54 | 0.071 |

체중 범위는 산술적으로 $70/0.020=3500$-fold, PK29 case 본문에서는 약 3000-fold — **본문에서는 "약 3000–3500-fold"로 표기**합니다.

> **[TRENCH — Elementary vs Complex Dedrick 전환]**  
> log-log $V$ vs $BW$ 기울기가 0.9–1.1 밖이면 Elementary($d=1$ 가정)를 고집하지 않습니다. PK29처럼 $d\approx1.18$이면 $C/(Dose/BW^d)$와 $t/BW^{d-b}$를 쓰는 Complex Dedrick으로 전환합니다.

> 📖 **G&W Case Study PK28, p.613, Fig.28.2:** Methadone의 elementary Dedrick 중첩 — mouse/rat/human 농도-시간 곡선이 **공통 생리학적 시간 척도 위로 접혀 들어가는** 모습을 학습자 관점에서 가장 잘 보여 줍니다.

> 📖 **G&W Case Study PK29, p.619, Fig.29.3:** $d\ne 1$이고 다구획 스케일링이 들어올 때 **왜 Complex Dedrick이 필요한지**를 보여 주는 최종 시각 증거입니다 — allometric parameter set이 곡선 중첩에 어떻게 연결되는지를 직접 보여 줍니다.

---

> **C4 체화 핵심**  
> ① PK28처럼 $d\approx1$인 곡선 중첩 → Elementary Dedrick으로 충분합니다.  
> ② PK29처럼 $d\approx1.18$–1.21인 약물 → Complex Dedrick으로 가야 합니다.  
> ⚡ overlay가 안 예쁘면 "그림 문제"로 보기 → fan-out의 기전 신호를 놓침 → model misspecification 또는 $d$ 추정 실패.

<!-- SLIDE_START: C5 | title: FIH 용량 번역 -->
<!-- SECTION_CORE: SC-07 -->

### ━━ C5. FIH 용량 번역(FIH Dose Translation)의 알로메트릭 백본(Allometric Backbone) ━━

> **앞 카드에서 이 카드로**  
> C4에서 지수 구조가 **곡선 수준에서** 버티는지 확인했으니, 이제 그 구조가 dose/exposure backbone으로 어떻게 번역되는지를 봅니다.

> **거장의 시각**  
> Equal-AUCu 식을 최종 FIH 시작 용량 공식처럼 쓰면 안전성 margin, PD metric, route/formulation, 기능적 연령이 전부 누락됩니다. **이 식을 노출 backbone으로 낮춰 읽어야** 수식은 보존하면서 IND/NDA 문서에서 방어 가능한 caveat 구조가 만들어집니다.

#### A. Equal-unbound-AUC 백본

$$
\underbrace{AUC_{u,rat}}_{\text{rat }AUC_u}=\underbrace{AUC_{u,man}}_{\text{human }AUC_u}=\frac{\overbrace{Dose_{rat}}^{\text{rat dose}}}{\underbrace{CL_{u,rat}}_{\text{rat }CL_u}}=\frac{\overbrace{Dose_{man}}^{\text{human dose}}}{\underbrace{CL_{u,man}}_{\text{human }CL_u}}
$$
[G&W Eq.2:417, p.190]

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $AUC_u$ | concentration×time | 비결합 노출 | dose, $CL_u$, fu, 선형성 |
| $Dose$ | mass | 투여량 | 종, 안전역, route/formulation |
| $CL_u$ | volume/time | 비결합 청소율 | fu 보정, 대사·배설 기전 |
| $b$ | 무차원 | dose backbone에 들어가는 CL 지수 | flow prior, 기전 예외, sensitivity 선택 |

> 💡 **비유:** C5 식은 완성된 처방전이 아니라 **다리의 철골**입니다. 철골 위에 안전 난간·하중 제한·통행 규칙을 붙여야 실제 환자가 건널 수 있습니다. → **Backbone 규칙: Eq.2:420은 최종 FIH 용량이 아니라 노출 번역 backbone입니다.**

> ⚠️ Equal-AUCu는 같은 PD나 같은 전체 곡선 모양을 보장하지 않습니다 [G&W p.190].

$$
\underbrace{Dose_{man}}_{\text{human dose}}=\underbrace{Dose_{rat}}_{\text{rat dose}}\cdot\left(\frac{\overbrace{BW_{man}}^{\text{human BW}}}{\overbrace{BW_{rat}}^{\text{rat BW}}}\right)^{\overbrace{b}^{\text{CL/AUC}}}
$$
[G&W Eq.2:420, p.190]

$$
\underbrace{CL_{u,man}}_{\text{human }CL_u}=\underbrace{CL_{u,rat}}_{\text{rat }CL_u}\cdot\left(\frac{\overbrace{BW_{man}}^{\text{human BW}}}{\overbrace{BW_{rat}}^{\text{rat BW}}}\right)^{\overbrace{b}^{\text{CLu 지수}}}
$$
[G&W Eq.2:421, p.190]

mg/kg dose 비로 쓰면:

$$
\underbrace{\frac{Dose_{man}/BW_{man}}{Dose_{rat}/BW_{rat}}}_{\text{mg/kg 비}}=\left(\frac{\overbrace{BW_{man}}^{\text{큰 종 BW}}}{\overbrace{BW_{rat}}^{\text{작은 종 BW}}}\right)^{\overbrace{b-1}^{\text{kg당 지수}}}
$$

$b<1$이면 큰 동물의 mg/kg dose는 작은 동물보다 낮아집니다.

#### B. 가정(Assumptions)

5가지 가정이 동시에 성립해야 backbone이 의미를 갖습니다:
① 비결합 AUC가 약리 효과와 연결됨, ② 표적 친화도와 관련 약리학이 종간 크게 다르지 않음, ③ PK가 선형 구간에 있음, ④ fu 차이가 있으면 $CL_u$로 보정, ⑤ AUC가 적절한 노출 지표(AUC 같은 양)임. **Cmax 의존 독성**이나 **역치 초과 시간 지표**가 끼면 별도 판단이 필요합니다.

G&W는 **동일 AUC라도 농도-시간 곡선의 모양은 상당히 다를 수 있음**을 명시합니다 [G&W p.190]. C5는 AUC backbone일 뿐이며, **전체 곡선 등가성을 보장하지 않습니다.**

#### C. 소아·노인 맥락 — R&T 기반

R&T Ch.14는 **연령·체중·성별이 약물 반응 변동성의 주요 원천**이며, **생활연령(chronologic age)이 기능적 연령(functional age)을 정의하지 않는다**고 경고합니다 [R&T p.411–412]. 연령을 고려하지 않는 일률 용량은 개별 노인의 필요를 충족하지 못할 수 있습니다 [R&T p.412].

R&T Key Relationships의 BSA 근사:

$$
\underbrace{BSA}_{\text{BSA 근사}}=\underbrace{1.73}_{\text{70kg BSA}}\cdot\left(\frac{\overbrace{Weight}^{\text{체중}}}{\underbrace{70}_{\text{70kg}}}\right)^{\overbrace{0.75}^{\text{BSA 지수}}}
$$
[R&T p.436]

60세 일반 성인 대비 소아 유지 용량:

$$
\underbrace{Child\ maintenance\ dose}_{\text{소아 유지용량}}=\underbrace{1.5}_{\text{성인 보정}}\cdot\left(\frac{\overbrace{Weight_{child}}^{\text{소아 체중}}}{\underbrace{70}_{\text{70kg}}}\right)^{\overbrace{0.75}^{\text{BW 지수}}}\cdot\underbrace{Typical\ adult\ maintenance\ dose}_{\text{성인 용량}}
$$
[R&T Eq.14-6, p.432; Key Relationships, p.436]

다만 R&T는 **mg/kg 또는 mg/1.73 m² 규칙의 폭넓은 사용은 적용 한계(연령·체조성·신기능)를 명시하지 않으면 의심스럽다**고 경고합니다 [R&T p.435]. **BW 알로메트리는 시작점이지, 소아·노인 용량 결정 공식 전체를 대체하지 않습니다.**

#### D. 노인 대사 진술 교정

"CYP3A4 대사가 60세 이상 매년 1% 감소"라는 문장은 **과단정**입니다. R&T가 실제로 제시하는 것은: ① 크레아티닌 청소율이 성인기에서 약 **1%/yr** 감소한다는 경험 법칙 [R&T p.422], ② CYP3A 기질에서 노인이 청년보다 청소율이 낮으며, 그 연령 차이를 해석할 때 1%/yr 크레아티닌 청소율 경험치가 관련된다는 점 [R&T p.424]. 정리하면 — **노인에서는 신·간 기능과 생물학적 연령을 별도로 봐야 하며, CYP3A 청소율도 청년 대비 감소할 수 있지만 단순 선형 시간 함수로 쓰지 않습니다.**

> 📖 **R&T 5e, Ch.14, p.430, Fig.14-20:** $BW^{0.75}$ 하나로 소아·노인 용량이 해결된다는 흔한 오류를 **시각적으로 막아 줍니다** — 연령에 따라 maintenance-dose fraction이 달라지는 모습이 바로 C5의 caveat입니다.

---

> **C5 체화 핵심**  
> ① Equal unbound AUC를 맞추는 종간 dose backbone → $Dose\propto BW^b$가 정합니다.  
> ② 소아·노인·FIH **실제** 용량 → functional age, renal/hepatic function, PD metric, safety margin이 지배합니다.  
> ⚡ Eq.2:420을 최종 FIH 용량으로 사용 → caveat 누락 → 재분석·정당화 요구 가능.

> ## ▶ §2 폐막 — 알로메트릭 의사결정 워크스루(Allometric Decision Walkthrough)
>
> 이 워크스루는 **새 수치나 새 예시를 도입하지 않습니다.** C1–C5 본문에서 확정된 수식·anchor·진단만으로, 동물 PK 데이터셋 하나를 받아 사람 노출 추정에 도달하는 **5단계 의사결정**을 한 호흡에 통과하는 시연입니다.
>
> **Step 1 — 변수 유형 진단 (C1 → C2/C3)**  
> 받은 변수가 무엇인가? CL/GFR/blood flow면 **흐름**이라 $b\approx 0.75$로 진입 (C2). V/blood volume/tissue mass면 **공간**이라 $d\approx 1$로 진입 (C3). 한 줄: **"flow면 0.75, extent면 1."** 이 분류가 틀리면 C4–C5 전체가 무너집니다.
>
> **Step 2 — Prior 타당성 점검 (C1 척도 불변 + C2 failure conditions)**  
> $b\approx 0.75$ prior를 그대로 써도 되는가? **6개 트리거** 중 하나라도 강하게 의심되면 prior를 sensitivity로 격하합니다 — 종간 fu 차이, CYP isoform 차이, 비선형 MM 동태, 장간 순환, 투여 경로·제형 차이, central/peripheral V 비율 drift. fu 차이가 크면 total CL 대신 $CL_u$를 스케일링합니다 (Eq.2:421).
>
> **Step 3 — 시간축 도출 (C3)**  
> $b$와 $d$로 두 시간축을 **동시에** 적습니다 — $t_{1/2} \propto BW^{d-b} \approx BW^{0.25}$ (큰 동물 = 긴 반감기), $k_{el} \propto BW^{b-d} \approx BW^{-0.25}$ (큰 동물 = 작은 fraction 제거 속도). 두 부호를 같이 보지 못하면 C4 정규화가 어긋납니다.
>
> **Step 4 — Dedrick 진단 (C4)**  
> 종간 자료가 있으면 Elementary($d=1$ 가정, $t/BW^{1-b}$)를 먼저 시도합니다. log-log V vs BW 기울기가 **0.9–1.1 안**이면 Elementary로 충분, 밖이면 Complex($t/BW^{d-b}$, $C\cdot BW^d/Dose$)로 전환. **PK28(Elementary 통과) ↔ PK29($d\approx 1.18$로 Complex 필요)** 가 그 벤치마크 쌍입니다. Curve fan-out이 남으면 그건 "예쁜 overlay 실패"가 아니라 **기전 신호**입니다.
>
> **Step 5 — Equal-AUCu Dose Backbone 적용 (C5 + R&T 보강)**  
> $Dose_{man}=Dose_{animal}\cdot (BW_{man}/BW_{animal})^b$를 한 줄로 적되, 그 위에 **6개 레이어**를 명시적으로 얹습니다 — (i) AUC vs Cmax-driven 독성 선택 근거, (ii) fu 보정, (iii) PK 선형성 가정 점검, (iv) safety margin/toxicology, (v) route/formulation, (vi) PD metric. 소아·노인에는 R&T Ch.14의 BSA 근사식, 소아 유지 용량 식, chronologic vs functional age 경고, 크레아티닌 청소율 ~1%/yr 경험치를 backbone 위에 한 층 더 얹습니다.
>
> **한 줄 마무리:** 이 5단계가 자동 회상되면 §1 Target Mental Model이 완성됩니다. 완성된 학습자는 "$0.75$를 외우는 사람"이 아니라 **"$0.75$를 prior로 두고, 자료가 prior를 언제 밀어내는지 판단하는 사람"**입니다.

---

<!-- SLIDE_START: §5 | title: 혼동쌍 분해 -->
<!-- SECTION_CORE: SC-08 -->

## §5 — 혼동쌍 분해(Confusion Pair Dissection)

### Pair 1. 청소율 지수 $b$ vs 분포용적 지수 $d$

| 비교 기준 | 개념 A: $b$ — CL 지수 | 개념 B: $d$ — V 지수 |
|---|---|---|
| 단위 / 차원 | 무차원; flow/rate 변수의 체중 스케일 | 무차원; space/extent 변수의 체중 스케일 |
| 수식 내 위치 | $CL=a\cdot BW^b$, $k_{el}\propto BW^{b-d}$ | $V=c\cdot BW^d$, $t_{1/2}\propto BW^{d-b}$ |
| 변화 원인 | 대사율, 장기 혈류, GFR, 단백 결합·수송체·비선형성 | 체수분, 혈액량, 조직 부피, 지방 분포, 조직 친화성 |
| 혼동 시 임상 결과 | CL scaling에 $d=1$을 넣어 $b=1$ 선형 kg당 오류 발생 | V scaling에 $b=0.75$를 넣어 분포용적·시간축 오판 |

**치명적 타격:** rat 250 g → human 70 kg에서 $b=0.75$ 대신 $d=1$처럼 선형으로 스케일링하면 $(70/0.25)^{0.25}\approx$ **4.1배 차이**, mouse 23 g → human은 약 **7.4배**, R&T 20-g mouse 예시는 **7.7배**입니다. 첫 사람 노출 추정의 자릿수가 바뀝니다.

> ⚡ **기억 고리 — *기능 vs 공간*:** CL은 기능적 처리 능력, V는 물리적 분포 공간입니다. 결론은 $t_{1/2}=0.693\cdot V/CL\propto BW^{d-b}\approx BW^{0.25}$ — 큰 동물은 절대 CL은 크지만 단위 시간당 fraction 제거는 작습니다.

### Pair 2. Kallynochron vs Apolysichron

| 비교 기준 | 개념 A: Kallynochron | 개념 B: Apolysichron |
|---|---|---|
| 단위 / 차원 | $t/BW^{1-b}$; $d=1$ 가정의 생리학적 시간 | $t/BW^{d-b}$; $d$ 반영 생리학적 시간 |
| 수식 내 위치 | Elementary Dedrick x축 | Complex Dedrick x축 |
| 변화 원인 | V가 체중에 거의 비례할 때 유지 | V 지수가 1에서 벗어날 때 필요 |
| 혼동 시 임상 결과 | $d\ne 1$에서 curve fan-out을 놓침 | 필요 없는 complex 보정으로 해석 과잉 가능 |

**기억 고리:** Kallynochron은 kg 단위로 정규화한 생리학적 시간, Apolysichron은 $BW^d$ 단위로 정규화한 생리학적 시간. PK29 compound X처럼 $d>1$이면 차이가 드러납니다.

### Pair 3. BW 알로메트릭 스케일링 vs BSA 스케일링

| 비교 기준 | 개념 A: $BW^b$ allometry | 개념 B: BSA scaling |
|---|---|---|
| 단위 / 차원 | 변수별 지수 $b$를 갖는 체중 기반 거듭제곱 | $BSA\approx1.73(Weight/70)^{0.75}$ 형태의 체표면적 근사 |
| 수식 내 위치 | $Y=a\cdot BW^b$의 지수 | BSA 또는 mg/1.73 m² dose rule에 들어가는 근사 지수 |
| 변화 원인 | 화합물·변수 특이성, 종 수, 결합, 대사·수송 기전 | 연령, 체조성, 신기능 한계를 명시해야 함 [R&T p.435] |
| 혼동 시 임상 결과 | 종 수 부족 시 기울기 불안정 또는 기전 예외 누락 | 소아·노인 용량을 과도하게 단순화 |

**정리:** BSA는 알로메트리의 적이 아니라 임상적으로 굳어진 $BW^{0.75}$ 근사입니다. 다만 "BSA"라는 이름이 붙었다고 maturation·obesity·functional age 문제가 사라지지는 않습니다.

> ⚡ **기억 고리 — *직선 도로 vs 우회로*:** 단순 알로메트리($y=a\cdot BW^b$)는 종간 스케일링을 끝내는 직선 도로. MLP·brain weight·PPB correction 같은 보정 인자는 특정 약물에서 대사·결합 차이가 클 때 필요한 우회로이며, BSA 변환도 maturation/binding/disease state 문제까지 해결해 주지는 않습니다.

**§5 요약:** $b/d$, Kallynochron/Apolysichron, BSA/BW allometry 중 **하나만 섞여도** 표·그림·dose narrative가 동시에 흔들립니다.

<!-- SLIDE_START: §7 | title: 자기점검 -->
<!-- SECTION_CORE: SC-09 -->

## §7 — 자기점검(Self-Test): 능동 회상 모듈

---

### Q1. 회상 — $a$와 $b$의 의미

*왜 이 질문:* C1의 수식 골격이 손에서 입으로 옮겨지는지 확인. 여기가 안 되면 C2 이후가 다 흔들립니다.

**질문:** $Y=a\cdot BW^b$에서 $a$와 $b$를 각각 한 문장으로 설명하고, CL과 V의 전형적 지수를 답하세요.

**정답:**
- $a$: 화합물 의존적 절편($BW=1$에서의 기준값), 단위는 $b$에 의존.
- $b$: 체중 변화에 대한 스케일링 지수, 대체로 변수 유형이 정하지만 자료 품질·기전이 흔듭니다.
- CL: $b\approx0.75$ (대사율/기능적 흐름 변수).
- V: $d\approx1.0$ (분포용적/공간 변수).
- 따라서 $t_{1/2}\propto BW^{d-b}\approx BW^{0.25}$, $k_{el}\propto BW^{b-d}\approx BW^{-0.25}$.

---

### Q2. 회상 — 왜 $b=1$이 위험한가

*왜 이 질문:* **4.1 vs 7.4 vs 7.7-fold**가 species pair와 함께 입에 나오는지 확인. species pair 없이 fold만 외우면 보고서 검토에서 바로 깨집니다.

**질문:** 23-g mouse → 70-kg human에서 $b=1$과 $b=0.75$ 차이는 몇 배인가? rat 250 g → human에서는?

**정답:**
- Mouse 23 g → human 70 kg: $(70/0.023)^{1-0.75}\approx$ **7.4배**.
- Rat 250 g → human 70 kg: $(70/0.25)^{0.25}\approx$ **4.1배**.
- R&T 20-g mouse 예시: **3500 vs 455 = 7.7배** [R&T p.733].
- Target AUC 기반 용량 계산에서는 CL 과대예측이 dose 과대 산출로 이어질 수 있습니다.

---

### Q3. 도출 — $t_{1/2}$와 $k_{el}$의 종간 지수

*왜 이 질문:* 한 번 손으로 도출하면 $V/CL$과 $CL/V$의 부호가 반대라는 사실이 오래 남습니다. C3 실패 모드("$k_{el}$ 부호 놓침")의 직접 예방.

**질문:** $CL=a\cdot BW^b$, $V=c\cdot BW^d$일 때 $t_{1/2}$와 $k_{el}$의 BW 지수를 도출하세요.

**정답:**

$$
\underbrace{t_{1/2}}_{\text{반감기}}=\underbrace{\ln2}_{\text{반감 상수}}\cdot\frac{\overbrace{V}^{\text{V}}}{\overbrace{CL}^{\text{CL}}}=\ln2\cdot\left(\frac{\underbrace{c}_{\text{V 절편}}}{\underbrace{a}_{\text{CL 절편}}}\right)\cdot\underbrace{BW^{d-b}}_{\text{시간지수}}
$$

$$
\underbrace{k_{el}}_{\text{제거속도}}=\frac{\overbrace{CL}^{\text{CL}}}{\overbrace{V}^{\text{V}}}=\left(\frac{\underbrace{a}_{\text{CL 절편}}}{\underbrace{c}_{\text{V 절편}}}\right)\cdot\underbrace{BW^{b-d}}_{\text{k 지수}}
$$

$d=1$, $b=0.75$이면 $t_{1/2}\propto BW^{0.25}$, $k_{el}\propto BW^{-0.25}$. 큰 동물은 절대 CL이 크지만 단위 시간당 제거 분율은 작습니다.

---

### Q4. Dedrick — Elementary vs Complex

*왜 이 질문:* PK28 ↔ PK29 벤치마크 쌍을 switch trigger와 함께 외우게 만드는 진단 회상. "log-log V vs BW 기울기가 0.9–1.1 밖이면 Complex"가 입버릇이 되어야 PK29류 약물에서 정규화가 안 어긋납니다.

**질문:** Elementary Dedrick과 Complex Dedrick의 y축/x축 변환을 쓰고, 언제 Complex가 필요한지 답하세요.

**정답:**
- Elementary: $C/(Dose/BW)$ vs $t/BW^{1-b}$; $d=1$ 가정.
- Complex: $C/(Dose/BW^d)$ 또는 $C\cdot BW^d/Dose$ vs $t/BW^{d-b}$.
- log-log $V$ vs $BW$ 기울기가 1에서 벗어나면 (예: PK29 compound X의 $d\approx1.18$) Complex Dedrick이 필요합니다.

---

### Q5. 출처 불일치 처리 — PK28/PK29

*왜 이 질문:* 학술 보고서·심사 문서에서 source-internal 수치 불일치를 임의로 하나로 "고정"하는 것은 **무결성 위반**입니다. citation scope를 함께 적는 습관이 들어야 합니다.

**질문:** PK28 methadone과 PK29 compound X의 source-internal 수치 불일치를 어떻게 인용해야 하나요?

**정답:**
- **PK28 methadone rat $t_{1/2}$:** G&W §2.10.6 본문은 2.9 h, PK28 case는 3.9 h. 하나로 고르지 말고 **`[§2.10.6 set]` 또는 `[PK28 case set]`을 명시**합니다.
- **PK29 parameter set:** G&W §2.10.7은 $a=0.021, b=0.74, c=0.076, d=1.18, e=0.56, g=0.075$; PK29 case는 $a=0.021, b=0.75, c=0.10, d=1.21, e=0.54, g=0.071$. **citation scope와 수치를 일치시킵니다.**

---

### Q6. 적용 — human CL 예측

*왜 이 질문:* 숫자가 손에서 나오는지 확인. 이 계산이 입에서 자동으로 안 나오면 FIH 노출 번역 표를 그 자리에서 채울 수 없습니다.

**시나리오:** Mouse BW=25 g, observed CL=0.012 L/hr. 70-kg human CL을 (a) $b=0.75$, (b) $b=1.0$으로 계산하고 차이를 해석하시오.

**정답:**

(a) $CL_{human}=0.012\cdot(70/0.025)^{0.75}\approx$ **4.6 L/hr**.  
(b) $CL_{human}=0.012\cdot(70/0.025)^1\approx$ **33.6 L/hr**.

$$
\underbrace{CL_{human}}_{\text{human CL}}=\underbrace{CL_{mouse}}_{0.012}\cdot\left(\frac{\overbrace{70}^{\text{human kg}}}{\overbrace{0.025}^{\text{mouse kg}}}\right)^{\overbrace{b}^{\text{선택 지수}}}
$$

차이는 **약 7.3배**. $b=1$은 선형 kg당 오류이며, target AUC 기반에서는 dose도 과대 산출할 수 있습니다.

---

### Q7. 적용 — 소아·노인 용량 맥락

*왜 이 질문:* R&T Ch.14의 핵심 메시지(chronologic ≠ functional age)가 입에서 나오는지 확인. C5 backbone만 외운 학습자는 소아·노인 용량을 단순화 오류로 망칩니다.

**질문:** 왜 소아·노인 용량에서 $BW^{0.75}$만으로 충분하지 않나요?

**정답:** R&T Ch.14는 **생활연령이 기능적 연령을 정의하지 않는다**고 설명합니다 [R&T p.411–412]. 소아에서는 renal/hepatic maturation, 체수분·결합 변화가 중요하고, 노인에서는 renal function, hepatic metabolism, 질환 상태, 체조성이 중요합니다. **$BW^{0.75}$는 시작점일 뿐이며, renal/hepatic function과 생물학적 연령 보정이 따로 필요합니다.**

---

### Q8. 보스 딜레마 — two-species 회귀 vs 생리학적 prior

*왜 이 질문:* 보스 딜레마입니다. 점추정값과 생리학적 prior가 충돌할 때 **무엇을 primary로 두고 무엇을 sensitivity로 보일지를 입으로 정당화**할 수 있어야 합니다. 동시에 ICH/FDA 단정문을 자발적으로 차단하는 source language discipline이 동작하는지 확인합니다.

**시나리오:** Rat와 dog 두 종만으로 log-log CL 회귀를 했더니 $b=0.62$가 나왔습니다. 문헌적 생리학적 prior $b=0.75$와 충돌합니다. FIH 노출 번역 표에는 무엇을 primary로 두겠습니까?

**정답:** 두 종 회귀의 점추정값은 leverage가 약하고 신뢰구간이 넓을 가능성이 큽니다. 따라서 **primary는 생리학적 prior $b=0.75$**로 두고, **$b=0.5, 0.62, 0.75, 1.0$ sensitivity analysis**를 함께 제시합니다. 단, $b=0.75$를 특정 ICH/FDA 조항이 직접 명시한다고 쓰지는 않습니다. 본 PDF 범위에서 방어 가능한 표현은 **"mammalian metabolic rate와 functional flow variable의 알로메트릭 근거에 기반한 prior"**입니다. `[확인 필요]` 규제 문구는 원문 가이드라인을 확인하기 전에는 쓰지 않습니다.

---

**§7 요약:** 자기점검의 목표는 수치 암기가 아니라 **세 가지 방어 능력**입니다 — (1) $b$와 $d$를 구별, (2) $b=1$ 오류가 dose/AUC에 주는 방향 설명, (3) 출처 불일치와 NOT_IN_SOURCE 규제 표현을 자발적으로 차단.

---

<!-- SLIDE_START: §8 | title: 메타 프레임과 큰 그림 -->
<!-- SECTION_CORE: SC-10 -->

## §8 — 메타 프레임과 큰 그림(Meta-Frame & Big Picture)

### A. 위치 잡기 — 이 세션이 시스템으로 작동하는 세 순간

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| 동물-인간 노출 번역 표 작성 | $b$, $d$, $CL_u$ | → | 첫 사람 노출 추정의 자릿수 변화 | C1–C5 spine을 한 표에 연결 |
| PopPK 체중 공변량 결정 | WT exponent | → | 좁은 WT range에서 SE 증가·점추정값 흔들림 | $b=0.75$ fixed primary + sensitivity |
| PBPK 장기 스케일링 | organ blood flow, organ volume | → | flow/extent 혼동 시 장기별 CL/V 오판 | 혈류는 rate-like, 부피는 extent-like로 분리 [R&T p.731–743] |

### B. 이 섹션이 약할 때의 실패 모드

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| 성인 60–90 kg처럼 WT range가 좁음 | CL exponent | → | 기울기 drift, SE 증가 | fixed prior와 estimated model을 분리 |
| PK29 compound X처럼 $d>1$ | V exponent | → | Elementary Dedrick fan-out | $d$ estimate 또는 Complex Dedrick 검토 |
| 소아·노인에서 BW scaling만 사용 | functional age, renal/hepatic function | → | maturation·신기능·체조성 누락 | R&T age/weight caveat를 별도 gate로 둠 [R&T p.412–415] |

### C. 전문가 해석 지점

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| $b>1$ 또는 $b<0.5$ | CL exponent | → | 기전 신호와 통계 잡음 혼재 | 종 수, leverage, 결합, 비선형성, 대사 경로 확인 |
| FIH/노출 번역 문장 작성 | Eq.2:420 | → | 최종 시작 용량 overclaim 위험 | equal-AUCu dose backbone으로만 기술 |
| Dedrick plot fan-out | $d$, 구획 비율 | → | overlay 실패를 그림 문제로 오독 | $d\ne 1$, 다구획성, 모델 잘못 지정 점검 |
| PK28/PK29 출처 불일치 | citation scope | → | 수치 무결성 손상 | `[§2.10.6 set]` 또는 `[PK28 case set]`처럼 범위 명시 |

### D. 후속 세션 연결 지식 그래프

| 후속 세션 | 이 세션에서 열리는 개념 | 이 세션 없으면 실패하는 것 |
|---|---|---|
| PopPK 체중 공변량 | flow vs extent 지수 분리 | CL/V WT exponent를 기계적으로 고정하거나 추정 |
| PBPK 장기 스케일링 | organ blood flow vs organ volume | 장기 혈류와 부피를 같은 지수로 처리 |
| FIH 노출 번역 | equal-AUCu backbone + sensitivity | Eq.2:420을 최종 시작 용량 규칙으로 오용 |
| 소아·노인 용량 | chronologic ≠ functional age | BW/BSA만으로 maturation·신기능 누락 |

### E. 최종 1페이지 사고 모델

```text
1. 변수의 종류를 먼저 묻는다.
   - flow/rate?  → CL, GFR, blood flow → b≈0.75
   - space/extent? → V, blood volume, tissue mass → d≈1
   - time? → V/CL → d-b≈0.25
   - rate constant? → CL/V → b-d≈-0.25

2. 종간 dose/exposure translation은 total dose가 아니라
   unbound exposure 관점에서 읽는다.
   - AUCu equality → Dose ∝ BW^b
   - mg/kg ratio → BW^(b-1)

3. 예외를 먼저 찾는다.
   - fu 차이, CYP isoform 차이, nonlinear PK, transporter,
     enterohepatic recirculation, route/formulation 차이

4. source language를 지킨다.
   - PDF-supported: G&W/R&T 수식, PK28/PK29 anchor,
     R&T age/renal/BSA caution
   - not directly supported: ICH/FDA/MABEL/NONMEM/QSP claims
     → 삭제 또는 [교과서 외 해석]
```

**§8 최종 요약:** Session 14의 핵심은 **"0.75를 외우는 것"이 아닙니다.** 어떤 변수가 왜 0.75이고, 어떤 변수는 왜 1이며, 그 차이가 시간과 dose를 어떻게 바꾸는지를 **보는 것**입니다. 이 관점이 allometry를 공식 암기에서 모델링 판단으로 바꿉니다.

---

<!--
## v3.8 출력 후 자가검증 체크리스트

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
| 수치 anchor 보존 | PK28/PK29, 4.1/7.4/7.7 fold, R&T/G&W page tag 보존 | ✓ |
| [M] 나비효과 이중 종착점 | Apex 카드 전체 | ✓ |

-->
<!-- v3.8 변환 노트
- 활자량: v3.7 839줄 (63,013 bytes) → v3.8 822줄 (55,576 bytes); 바이트 기준 약 11.8% 감축.
  · 라인 수 차이가 작은 이유: §3 HARD PRESERVE 규칙에 따라 수식 LaTeX 블록(60+개), 출처 anchor(G&W 28건/R&T 17건/PK28·PK29 60+건), 파라미터 표, SLIDE_START 마커 10개를 byte-level 보존했기 때문. 이들이 전체 활자량의 큰 비중을 차지.
  · prose(설명 산문)만 보면 verbose한 학습 항법 안내, [EXPERT_INFERENCE] 태그, "확인 시점:" 가이드, "학습 지시:" 라인, 다중 콜아웃 박스 등이 광범위하게 압축됨.
  · 컴파일러 §2.3의 "40–55% 감축" 목표보다 §3 보존 우선("의심스러우면 보존, 보존 손실=변환 실패")이 상위 규범이므로 trade-off를 보존 쪽에 둠.
- 보존 감사:
  · SLIDE_START 마커: 10개 = v3.7 일치 (§1, §2, C1–C5, §5, §7, §8)
  · 출처 anchor: G&W/R&T/PK28/PK29 page tag, Eq 번호 100% 보존
  · 핵심 수치: 4.1/7.4/7.7-fold, 3500/455, b=0.75/d=1.0, PK29 두 parameter set, 3000–3500-fold, 1%/yr 모두 보존
  · 약물명: methadone (PK28), compound X (PK29), cefazolin (TRENCH) 보존
  · 수식 LaTeX 블록: 모든 overbrace/underbrace 주석 보존
- 주요 변환:
  · 메타 문구 제거: "기호 통일" HTML 코멘트, "[EXPERT_INFERENCE, ver2 V*]" 태그, "확인 시점:" 가이드, "학습 지시:" 등
  · "학습 항법 안내" → §0.5 빠른 읽기 경로(1개 표)로 압축
  · 콜아웃 단일화: C1·C2 등에서 💡+⚠️+🔑 중복을 단일 박스 통합
  · 자기참조 해소: "C2와 C3에서 얻은 b와 d는..." 같은 forward reference를 inline 결론 + 포인터 형태로 재작성
  · 약물 즉맥락: methadone(μ-opioid, 저추출), compound X(PK29, 5종) 첫 등장에 분류 인라인
  · PK29 두 parameter set을 줄글에서 2x6 표로 시각화
  · §5 표는 4행 구조 그대로 유지하며 셀 내부만 톤 손봄
-->

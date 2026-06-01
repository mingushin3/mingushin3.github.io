# 세션 14 — Allometric Scaling: Interspecies · Dedrick · Equal-AUC$_u$ · FIH dose backbone — v4.0 보강본

> 📝 **보강본 변경 요약(v4.0 → v4.0 보강본).** 본문 C1–C5, §5, §7 Q1–Q8, §8은 원본 그대로 보존했습니다. 다음 네 항목을 보강했어요 — ① **BSA 근사식 출처 명시 강화**(C5 내부, Eq.14-2 옆에 보완 callout), ② **소아 maturation 모델 카드 추가**(C5+ A), ③ **Lean body mass vs Total body weight**(C5+ B), ④ **신장·간 청소율의 알로메트릭 분기**(C5+ C). §7 자기점검에 Q9–Q11이 추가됐고, §8 후속 연결 표에 한 줄이 더해졌습니다.

## 임상 장면 — 왜 이 세션 하나가 회의 분위기를 결정하는가

Phase 1 회의실, 화이트보드 앞이라고 생각해 보세요. **23-g mouse**에서 측정한 청소율(clearance, CL)을 **70-kg human**으로 옮기는 표가 한 장 걸려 있습니다. 누가 한 줄을 잘못 그으면 첫 사람 노출 추정이 **거의 한 자릿수**가 어긋납니다 — $b=1$을 쓰면 $b=0.75$ 대비 **약 7.4배** 높게 나옵니다 [G&W PK28 p.611–614]. R&T의 20-g mouse → 70-kg human 예시에서는 같은 차이가 **3500 대 455, 즉 7.7배**로 벌어집니다 [R&T p.733].

이게 단순한 "계산 취향"이 아니에요. **target AUC를 맞추려고 용량을 잡는 순간 CL을 과대평가하면 용량도 과대 산출됩니다.** 규제 심사자가 이 표 한 칸을 짚고 "이 지수 어떻게 정당화하셨어요?"라고 물으면, 우리는 그 자리에서 답할 수 있어야 합니다. 이번 세션 전체가 **그 한 칸을 방어하는 도구**예요.

> 🧭 **이 챕터를 통과하는 다섯 정거장.** C1에서 $Y=a\cdot BW^b$가 회귀가 아니라 **체중을 PK 파라미터로 환산하는 환율식**이라는 걸 잡습니다. C2에서 CL의 환율(=지수)이 왜 0.75인지, C3에서 V의 환율이 왜 1.0인지, 그 차이가 어떻게 시간축을 만드는지 봅니다. C4에서 Dedrick으로 그 환율이 실제 자료에서 버티는지 진단하고, C5에서 그게 어떻게 FIH 용량 backbone이 되는지 — 그리고 그 backbone 위에 무엇을 더 얹어야 진짜 첫 사람 용량이 되는지를 마무리합니다. **보강본**에서는 C5 뒤에 **C5+ 임상 확장 카드**가 더해져 maturation·body composition·신장/간 청소율 분기까지 다룹니다.

**시작 전에 입에 붙어 있어야 할 것:** CL, V, AUC, 반감기, 비결합 분율($f_u$), 일차 제거. **세션 끝에 입으로 답할 것:** ① $b=0.75$랑 $b=1$이 왜 같이 쓰일 수 없는지, ② 시간이 왜 $d-b$로 스케일링되는지, ③ 소아·노인 용량에서 왜 체중 외에 기능적 연령과 장기 기능 보정이 더 필요한지.

<!-- SLIDE_START: §1 | title: 세션 개요와 로드맵 -->
<!-- SECTION_CORE: SC-01 -->

## §1 — 세션 개요와 로드맵(Session Header & Roadmap)

**Source:** Gabrielsson & Weiner 5e §2.10 (p.170–191), Case Study PK28 (p.611–614), Case Study PK29 (p.615–620); Rowland & Tozer 5e Ch.14 (p.411–441), Ch.22 allometry section (p.731–743). **보강본 추가 인용:** R&T 5e Ch.14 Eq.14-1·14-2 (p.421), Eq.14-10·14-11 LBW (p.434), Fig.14-8·14-9 maturation (p.420–421), Fig.14-11·14-12 CYP maturation (p.423–424), Fig.14-13 CYP3A elderly (p.424), Key Relationships (p.436); R&T Ch.15 Eq.15-7·15-8 renal-nonrenal split (p.453–454).

### 세 층으로 본 이 세션

```text
Layer 1 — 무엇인가
  Allometry / CL / V / Dedrick / AUCu backbone / Clinical extensions

Layer 2 — 어떻게 계산되는가
  Y=a·BW^b → CL∝BW^b, V∝BW^d → t1/2∝BW^(d-b), kel∝BW^(b-d)
  → Pediatric: BW^0.75 × maturation × organ function
  → Renal/Hepatic: fe·RF + (1-fe)·age·BW^0.75/1936

Layer 3 — 언제, 왜 중요한가
  b=1 오류 차단 → Dedrick 중첩 진단 → equal-AUCu dose backbone
  → 소아·노인·FIH caveat → maturation/LBW/renal-hepatic 분기
```

이 세션은 어디에 들어가나요?

```text
[선행: CL·V·AUC·반감기·비결합 분율] → [이 세션: allometric spine + clinical extensions] → [후속: PopPK WT covariate / PBPK scaling / FIH exposure table / Pediatric MIPD]
```

🧭 **다섯 카드를 한 줄로 잇기:**
**C1**에서 $Y=a\cdot BW^b$를 회귀가 아닌 **환율식**으로 잡고 → **C2**에서 CL의 환율 $b\approx0.75$가 왜 prior가 되는지, 언제 의심해야 하는지 보고 → **C3**에서 V의 환율 $d\approx1$이 왜 다른지, 그 차이가 시간축을 어떻게 만드는지 짚고 → **C4**에서 Dedrick으로 환율이 실제 자료에서 버티는지 진단하고 → **C5**에서 그 환율이 FIH dose backbone으로 어떻게 번역되는지 — 그리고 그 backbone만으로는 왜 부족한지를 마무리합니다. **C5+ 보강본 카드**에서는 backbone에 maturation·body composition·신장/간 분기를 어떻게 얹는지를 명시합니다.

### 이 세션의 한 줄 핵심

$Y=a\cdot BW^b$는 단순 회귀식이 아니에요. **종간 체중 차이를 PK 파라미터(CL, V, dose)로 환전하는 거듭제곱 언어**입니다. 가장 흔한 함정은 $b=0.75$랑 $b=1$ 차이를 작게 보는 거예요 — 작은 동물에서 사람으로 옮길 때 그 차이는 **수 배에서 거의 한 자릿수까지** 벌어집니다.

| 비교 | 차이 |
|---|---|
| **20-g mouse → 70-kg human** ($b=1$ vs $b=0.75$) | 3500 vs 455 = **7.7배** [R&T p.733] |
| **23-g mouse → 70-kg human** (PK28) | **약 7.4배** |
| **Rat 250-g → 70-kg human** | **약 4.1배** |

이건 "용량을 낮게 시작/높게 시작" 같은 단순 구호가 아니라, **target AUC 기반으로 용량을 잡을 때 CL이 과대평가되면 dose도 과대 산출된다**는 방향성 문제예요.

$$
\overbrace{b=1}^{\text{kg당 선형}}\quad vs\quad \overbrace{b=0.75}^{\text{CL prior}}
$$

이 세션을 다 듣고 나면 다음 네 단계가 머릿속에서 자동으로 굴러가야 합니다.

1. **변수의 종류부터 물어요.** 흐름/속도(flow/rate)인가? CL, GFR, 혈류 → $b\approx 0.75$. 공간/분포 범위(extent)인가? V, 혈액량, 조직량 → $d\approx 1$. 시간인가? $V/CL \to BW^{d-b}$ (≈0.25). 속도상수인가? $CL/V \to BW^{b-d}$ (≈−0.25).
2. **종간 용량 번역은 비결합 노출(AUCu) 관점**으로 읽어요. AUCu equality이면 $Dose \propto BW^b$, mg/kg 비는 $BW^{b-1}$.
3. **예외를 먼저 찾아요** — $f_u$ 차이, CYP isoform 차이, 비선형 PK, 수송체, 장간 순환, 투여 경로·제형 차이.
4. **출처 언어를 지킵니다** — PDF가 직접 뒷받침하는 것(G&W/R&T 수식, PK28/PK29 anchor, R&T age/renal/BSA caution)과 직접 뒷받침하지 않는 것(ICH/FDA/MABEL/NONMEM/QSP 단정)을 분리해요.

이 4단계가 §8 E의 최종 사고 모델 그대로이고, §1–§8 전체가 이걸 정당화하는 과정입니다.

### 카드 간 연결 지도

```text
[C1] Master Equation: Y = a·BW^b
        │
        ├──▶ [C2] CL exponent b≈0.75 ─────────────┐
        │                                           ├──▶ [C5] Equal-AUCu dose backbone
        └──▶ [C3] V exponent d≈1.0 ────────────────┘                  │
                  │                                                    │
                  ├──▶ t1/2 ∝ BW^(d-b)≈BW^0.25                        ▼
                  ├──▶ kel ∝ BW^(b-d)≈BW^-0.25                  [C5+] Clinical Extensions
                  └──▶ [C4] Dedrick Superposition                  ├── A. Maturation function
                                                                    ├── B. LBW vs TBW
                                                                    └── C. CL_R vs CL_H 분기
```

**선행 전제:** CL, V, AUC, 반감기 정의 / 일구획 지수 감소 / 혈장 단백 결합과 비결합 청소율. **직접 후속:** 소아·노인 용량 조정, PopPK 체중 공변량 선택, PBPK 장기 혈류·부피 스케일링, FIH 노출 번역 표. **주의:** NONMEM control stream, ICH/FDA/MABEL 표현, QSP 구현은 본 PDF가 직접 다루지 않으니 `[교과서 외 구현/실무 해석]`으로만 다룹니다.

**§1 한 줄로 닫기:** 이 세션의 척추는 $Y=a\cdot BW^b \to CL\ b\approx0.75 \to V\ d\approx1 \to time\ d-b\approx0.25 \to Dedrick \to equal\text{-}AUCu\ dose\ backbone$입니다. 반드시 잡아야 할 두 가지는 **4.1/7.4/7.7배를 species pair랑 같이 외우는 것**, 그리고 **Eq.2:420을 standalone FIH 시작 용량 공식이 아니라 노출 backbone으로 낮춰서 쓰는 것**. **보강본에서는** 그 backbone 위에 maturation·body composition·신장/간 분기 세 레이어가 어떻게 얹히는지까지를 추가 학습 목표로 둡니다.

---

> 📊 **알로메트릭 척추 한눈에:** 변수 유형 → 지수 → 시간/용량으로 이어집니다. $Y=a\cdot BW^b$는 독립 수식이 아니라 CL, V, time, Dedrick, equal-AUCu 용량 번역을 모두 잇는 척추예요.

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

**거장의 시각 — 압축 한 줄:** $Y=a\cdot BW^b$를 회귀선으로 보면 기울기 점추정값에 과신하게 돼요. 이걸 **"체중 배율을 바꿔도 같은 법칙이 그대로 유지된다"는 주장**으로 보면, C2–C5의 모든 판단이 하나의 질문으로 정렬됩니다 — "이 약물에서 이 지수 prior가 유지되는가?"

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

💡 로그-로그 직선이 잘 맞는다는 건 회귀선이 예쁘게 나온다는 뜻이 아니에요. **"체중 배율이 바뀌어도 같은 법칙이 그대로 유지된다"는 가정**이 통한다는 뜻입니다. 그래서 회귀선을 보기 전에 먼저 물어야 해요 — 이 변수가 flow냐, extent냐, time이냐?

양변 로그 변환:

$$
\underbrace{\ln(Y)}_{\text{로그 }Y}=\underbrace{\ln(a)}_{\text{로그 절편}}+\overbrace{\underbrace{b}_{\text{기울기}}\cdot\underbrace{\ln(BW)}_{\text{로그 }BW}}^{\text{log-log}}
$$
[G&W Eq.2:379, p.176; R&T Eq.22-1, p.732]

- **$a$:** 약물·화합물 의존 절편이에요. 단위는 $b$가 뭐냐에 따라 같이 바뀝니다.
- **$b$:** 대체로 변수 유형이 정해 주는 값이에요. 다만 실제 CL 지수는 자료 품질, 종 수, 비선형성, 종간 단백 결합 차이에 따라 흔들립니다 [G&W p.177–178]. 그러니까 $b$는 자연상수가 아니라 **변수 유형과 자료가 함께 만드는 prior**입니다.

#### B. 도출(Derivation) — 왜 거듭제곱 함수인가

G&W는 이걸 두 줄로 정리합니다 — **대사율 ∝ $BW^{0.75}$**, **에너지 함량 ∝ $BW^1$** → 따라서 순환 시간(turnover time) ∝ $BW^{0.25}$ [G&W Eq.2:375–377, p.173]. 한 문장으로 옮기면 이거예요: **"체중이 커지면 절대 처리량은 늘어요. 그런데 단위 체중당 처리 효율은 떨어집니다."**

기하학적으로도 같은 방향이에요. 표면적은 길이의 제곱, 부피는 세제곱이니까 표면적은 부피의 $2/3$승에 비례해요. 다만 실제 생리학 변수는 단순 외부 표면적보다 복잡해서 Brody의 경험적 지수는 0.5–0.8 범위로 나타납니다 [G&W p.173–174].

#### C. 구조적 의미

💼 **실무 함정:** 로그-로그 직선이 잘 맞는다는 걸 보고 "회귀가 잘 맞으니까 OK"라고 넘어가면 한참 멀리 가서 발목 잡혀요. 잘 맞는다는 건 **"체중 배율이 달라져도 같은 지수 법칙이 유지된다"**는 가정이 통한다는 뜻인데, 이 가정이 깨지는 순간이 알로메트리가 실패하기 시작하는 순간입니다.

#### D. 경계 조건

알로메트리가 잘 통하는 경우 — 약물 분포가 물리적 수송 과정에 지배되고, 혈장 단백 결합의 종간 차이가 크지 않은 화합물. 잘 안 통하는 경우 — **종간 대사·배설의 질적 차이, CYP450 isozyme 구성 차이, 단백 결합 차이가 큰 화합물** [G&W p.173].

---

**C1 이번 카드 핵심내용.**
종간 PK 차이를 한 식으로 묶을 때, $Y=a\cdot BW^b$는 회귀가 아니라 **체중 배율이 바뀌어도 같은 법칙이 유지된다는 주장**으로 읽어야 해요. 기울기 점추정값과 생리학적 prior가 충돌하면 자료 품질·종 수·기전 차이를 보고 해석을 정합니다. **$b$를 자연상수처럼 고정하는 순간** 기전 신호를 회귀 잔차로 오독하게 되고, C2–C5 추론이 줄줄이 무너집니다.

<!-- SLIDE_START: C2 | title: 청소율 지수 -->
<!-- SECTION_CORE: SC-04 -->

### ━━ C2. [⚡ Apex Concept] 청소율 지수(Clearance Exponent) $b\approx0.75$ ━━

C1에서 $b$가 체중 배율 환산의 지수 prior라는 걸 잡았어요. 이제 가장 위험한 변수인 CL에서 그 prior가 임상 노출에 어떤 격차를 만드는지를 봅니다.

**거장의 시각 — 실무 함정:** mg/kg 처방에 익숙해지면 CL도 체중에 선형으로 비례한다고 생각하기 쉬워요. 그런데 CL은 **기능적인 처리 흐름 — 시간당 얼마나 처리되느냐**라서 $b\approx0.75$가 출발 prior입니다. G&W는 한 발 더 들어가서, 실제 CL 지수가 **0.2부터 1을 넘는 값까지** 갈 수 있다고 경고해요 [G&W p.178]. 그러니까 입에 붙어 있어야 할 한 줄은 이겁니다 — **"flow는 0.75로 시작하되, $f_u$·수송체·포화·종간 대사 차이가 보이면 즉시 sensitivity로 격하한다."**

#### A. 정형 정의

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

💡 CL은 "몸 안 공간의 크기"가 아니라 **"시간당 얼마나 처리되는가"**예요. $b=0.75$도 법칙이 아니라 prior이고, 실제 CL 지수는 약 0.2에서 1을 넘는 값까지 변할 수 있습니다 [G&W p.178]. 그래서 FIH 방어 규칙은 단순해요 — **primary 지수랑 sensitivity 지수를 같은 표에 같이 둬야** dose narrative가 방어됩니다.

G&W Fig.2.159는 91개 화합물의 CL 지수가 주로 **0.5–1.0 범위**에 놓이는 모습을 보여 줍니다 [G&W p.191].

#### B. 가장 흔한 오해 — "$b=1$ 선형 kg당 스케일링"

많이들 이렇게 생각해요 — "mg/kg 처방에 익숙하니까 청소율도 kg에 선형 비례한다." 직관적으로 그럴싸하죠. 저용량·소수 종 자료에서는 log-log 직선이 그럴듯해 보이고, R&T랑 G&W 모두 $0.75$ prior의 생리학적 근거를 제시하니까 어느 쪽으로 가야 할지 헷갈리기도 합니다. 맞는 얘기 같지만 — CL은 흐름·속도 변수라서 **$b\approx0.75$가 생리학적 prior**이고, 작은 동물에서 사람으로 옮기는 순간 그 차이가 임상적으로 거대해집니다.

- **R&T 20-g mouse → 70-kg human:** $b=1$이면 3500, $b=0.75$이면 455 → **7.7배 차이** [R&T p.733].
- **G&W PK28 23-g mouse → 70-kg human:** $(70/0.023)^{0.25}\approx$ **7.4배 차이**.
- **Rat 250-g → 70-kg human:** $(70/0.25)^{0.25}\approx$ **4.1배 차이**.

$$
\underbrace{\left(\frac{BW_{human}}{BW_{animal}}\right)^{1-0.75}}_{\text{b=1/0.75}}=\underbrace{\left(\frac{BW_{human}}{BW_{animal}}\right)^{0.25}}_{\text{종 격차}}
$$

이걸 그냥 두면 어떤 일이 벌어지냐 — target AUC 기반 용량 계산에서 **CL을 과대평가하면 목표 AUC를 맞추기 위한 dose도 과대 산출됩니다.** (단, "CL 과대평가 → subtherapeutic 시작"이라는 단정은 PDF가 직접 뒷받침하지 않으니 쓰지 않아요.) 지수 선택 하나가 모델링/규제 라인을 타고 가면 — sensitivity 재제출, 지수 정당화 요구, Deficiency Letter성 질의까지 갈 수 있습니다.

#### C. 실패 조건

알로메트리 실패는 단순 무작위 오차가 아니라 **기전 신호일 수 있어요.** G&W Fig.2.145가 이걸 시각적으로 못 박아 줍니다 — 스케일링이 잘 되는 화합물은 70-kg human CL 예측구간이 약 **10-fold** 범위인데, 잘 안 되는 화합물은 약 **1000-fold**까지 넓어집니다 [G&W p.174].

실패 트리거 6가지를 입에 붙여 두세요: ① 종간 혈장 단백 결합 차이, ② 대사 경로 또는 CYP isozyme 조성 차이, ③ 비선형 미카엘리스-멘텐 거동, ④ 장간 순환, ⑤ 투여 경로·제형 차이, ⑥ 중심·말초 분포용적 비율 변동 [G&W p.191].

**비결합 청소율($CL_u$) 스케일링.** 종간 $f_u$ 차이가 크면 total CL이 아니라 $CL_u=CL/f_u$를 스케일링해야 합니다. G&W Eq.2:421이 이걸 $CL_{u,man}=CL_{u,rat}\cdot(BW_{man}/BW_{rat})^b$ 형태로 정리합니다 [G&W p.190]. R&T Table 22-1에서는 **cefazolin**(1세대 cephalosporin 항생제, 단백 결합 높은 신장 배설 약물)처럼 human-animal 단백 결합 차이가 큰 경우를 보여 줘요 — 종간 $f_u$가 의미 있게 다르면 total CL 스케일링으로는 첫 사람 노출 추정이 어긋납니다 [R&T p.740]. → 그래서 **$f_u$가 크게 다른 약물에서는 $CL_u$ scaling으로 옮겨 가야 한다**는 사실의 임상 예시예요. $f_u$ 비교는 가능하면 **같은 농도·buffer·온도·assay**에서 측정된 값끼리 해야 합니다.

#### D. 전문가 진단 트리거

💼 **실무 함정 — $b$가 양극단으로 갈 때:** PopPK나 종간 회귀에서 **$b>1$**이 나오면 "추정값을 그대로 믿을까?"가 아니라 "**단백 결합, 수송체, 포화, 자료 품질** 중 무엇이 기울기를 밀어 올렸나?"를 먼저 물어요. 반대로 두 종만으로 얻은 **$b<0.5$**는 생리학적 신호보다는 **통계적 지렛대 부족**일 가능성이 큽니다.

---

CL의 $b\approx0.75$가 시간당 처리량의 지수라면, V는 왜 $d\approx1$일까요? V가 "흐름"이 아니라 "공간"이라서 그래요 (→ C3).

> 📖 **Rowland & Tozer 5e, Ch.22, p.733, Fig.22-2:** $b=1$과 $b=0.75$의 7.7배 mouse-human 격차를 계산이 아니라 **눈으로 확인하게** 해 주는 가장 명확한 원출처 그림입니다. 작은 동물에서 사람으로 한 칸 옮길 때 두 선이 얼마나 벌어지는지 한 번 보고 나면 잊히지 않아요.

> 📖 **Gabrielsson & Weiner 5e, §2.10.3, p.174, Fig.2.145:** 알로메트리가 유용한 예측을 주는 화합물과, 예측구간이 위험하게 넓어지는 화합물을 분리해서 보여 주는 그림이에요. 실패가 "잡음"이 아니라 **기전·자료 품질 신호**라는 C2의 메시지를 직접 뒷받침합니다.

---

**C2 이번 카드 핵심내용.**
Target AUC 기반 human CL/dose 예측에서 첫 노출 추정을 결정하는 게 CL 지수 $b\approx0.75$예요. mg/kg 선형 사고는 CL/dose 과대로 가고, $b=0.75$ 과신은 기전 예외 누락으로 갑니다 — **둘 다 위험**합니다. $0.75$를 법칙처럼 적용하면 $f_u$·수송체·포화·대사 차이를 놓치고, Phase 1 노출 오판 + 지수 정당화 요구까지 이어질 수 있습니다.

<!-- SLIDE_START: C3 | title: 분포용적 지수 -->
<!-- SECTION_CORE: SC-05 -->

### ━━ C3. 분포용적 지수(Volume Exponent) $d\approx1.0$ ━━

C2에서 CL을 시간당 흐름 변수로 잡았어요. 이번에는 V를 **공간 변수**로 분리해야 반감기랑 제거속도의 지수 부호가 맞아 들어갑니다.

**거장의 시각 — 경계 조건:** V를 CL처럼 흐름 변수로 읽으면 $t_{1/2}$랑 $k_{el}$의 지수 부호가 **동시에** 뒤집혀요. V를 **분포 공간**으로 보는 순간 $d\approx1$이랑 $b\approx0.75$의 차이 $d-b$가 시간축 전체를 만든다는 사실이 즉시 보입니다.

#### A. 정형 정의

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

💡 V는 처리 능력이 아니라 **약물이 퍼질 수 있는 공간의 크기**입니다. CL의 $b$랑 V의 $d$를 바꿔 쓰면 half-life랑 rate constant 부호가 **동시에 틀어져요.** 시간축 규칙은 단순합니다 — 시간은 $V/CL$이니까 $d-b$가 지배합니다.

G&W Table 2.22는 **혈액량 지수 0.99, 골격근량 1.09, Vd ≈ 1.0**을 제시합니다 [G&W p.180]. 그러니까 "V는 거의 체중에 비례한다"는 prior가 단순한 직관이 아니라 여러 생리학적 변수에서 같은 신호로 나오는 거예요.

#### B. 결과 — 반감기와 속도상수

$$
\underbrace{t_{1/2}}_{\text{반감기}}=\underbrace{\ln2}_{\text{반감 상수}}\cdot\frac{\overbrace{V}^{\text{공간}}}{\overbrace{CL}^{\text{흐름}}}=\ln2\cdot\frac{\underbrace{c\cdot BW^d}_{\text{V 스케일}}}{\underbrace{a\cdot BW^b}_{\text{CL 스케일}}}\propto \underbrace{BW^{d-b}}_{\text{시간지수}}
$$

$d\approx1$, $b\approx0.75$이면:

$$
\underbrace{t_{1/2}}_{\text{반감기}}\propto \underbrace{BW^{0.25}}_{\text{큰 종↑}},\qquad \underbrace{k_{el}}_{\text{제거속도}}=\frac{\overbrace{CL}^{\text{흐름}}}{\overbrace{V}^{\text{공간}}}\propto\underbrace{BW^{b-d}}_{\text{큰 종↓}}\approx BW^{-0.25}
$$

"$t_{1/2}\propto BW^{0.25}$"만 외우면 절반만 본 거예요. 더 중요한 사실 — **큰 동물일수록 모든 일차 속도상수가 작아진다**. 같은 $V/CL$을 시간으로 읽으면 반감기, 뒤집어 $CL/V$로 읽으면 속도상수입니다. 한 줄로 말하면 — **큰 동물은 절대 CL은 크지만 단위 시간당 제거되는 분율은 작습니다.**

#### C. 데이터 앵커 — Methadone (PK28)

**Methadone**(μ-opioid 작용제, 저추출 약물; PK28 사례)이 PK28의 종간 자료 주인공이에요. 저추출이라는 게 핵심이에요 — 간 추출률이 10%도 안 되니까 CL이 효소 활성·$CL_{int}$에 직접 반응하고, 종간 스케일링에서 알로메트리 신호를 깨끗하게 보여 줄 수 있는 약입니다. → 그래서 **$d\approx1$ 가정 하에서 elementary Dedrick이 통과하는** 모범 사례로 G&W가 PK28을 든 거예요.

| 종 | BW | Dose | 비고 |
|---|---:|---:|---|
| Mouse | 23 g | 25 µg IV bolus | 기본 Dedrick 앵커 |
| Rat | 250 g | 500 µg IV bolus | 출처 내부 $t_{1/2}$ 불일치 있음 |
| Man | 70 kg | 100,000 µg IV bolus | human 앵커 |

- $a=0.319$, $AUC=1/a=3.13$ [G&W §2.10.6 p.186; PK28 p.613]
- 간 추출률 **<10%** (저추출) [G&W p.186; PK28 p.613]
- **$t_{1/2}$ 불일치:** G&W §2.10.6 본문은 1.5/2.9/35 h, PK28 case는 1.5/**3.9**/35 h로 rat 값이 달라요. 보고서에 인용할 때는 **`[§2.10.6 set]` 또는 `[PK28 case set]`을 반드시 명시**합니다. 둘 중 하나로 임의 고정하면 무결성 위반이에요.

#### D. 한계 — V를 받아들일 때 조심할 점

V 지수는 대체로 1에 가깝지만 $V_{ss}$는 조직 친화성·지방 분포·수송체·단백 결합에 따라 **0.8–1.2 범위로 흔들립니다.** R&T의 비만 예시도 같은 메시지를 줘요 — **"체중이 늘어난 게 곧 분포용적이 의미 있게 늘어났다는 뜻은 아니다"** [R&T p.439]. 비만 환자에서 lipophilic 약물은 V가 비례적으로 늘지만, hydrophilic 약물은 V가 거의 안 늘 수도 있어요.

> 📊 **흐름과 공간의 분리:** CL은 흐름이라 $b\approx0.75$, V는 공간이라 $d\approx1$. 두 지수의 차이가 시간과 속도상수를 반대 방향으로 끌고 갑니다.

$$
\underbrace{CL=a\cdot BW^b}_{\text{CL 흐름}}\quad vs\quad\underbrace{V=c\cdot BW^d}_{\text{V 공간}}\quad\Rightarrow\quad\underbrace{t_{1/2}\propto BW^{d-b}}_{\text{시간↑}}\; ,\;\underbrace{k_{el}\propto BW^{b-d}}_{\text{분율 속도↓}}
$$

---

**C3 이번 카드 핵심내용.**
큰 동물에서 half-life가 길어지는 이유는 $d-b\approx0.25$가 정해요. 절대 CL은 증가하지만 제거 분율은 감소 — $CL/V$의 $b-d\approx-0.25$가 지배합니다. $t_{1/2}$만 암기하고 $k_{el}$ 부호를 놓치면 CL/V 해석이랑 시간축 정규화가 동시에 실패합니다.

<!-- SLIDE_START: C4 | title: Dedrick 중첩 -->
<!-- SECTION_CORE: SC-06 -->

### ━━ C4. Dedrick 중첩(Dedrick Superposition): 기본형(Elementary) + 복합형(Complex) ━━

C2·C3에서 잡은 $b$랑 $d$는 숫자로만 끝나면 의미가 없어요. 실제 종간 PK 곡선이 **한 축 위에 진짜로 겹치는지** 검증해야 하는데, 그 도구가 Dedrick 변환입니다.

**거장의 시각 — 실무 함정:** Dedrick plot을 "예쁜 overlay 그림"으로만 읽으면 fan-out을 "그림이 안 예쁘게 그려졌다"로 오해해요. 이걸 **지수 구조의 진단 도구**로 보는 순간, curve 겹치기가 안 되는 이유가 $d=1$ 가정 실패인지, 다구획성인지, 모델 잘못 지정인지를 추적할 수 있습니다.

#### A. 정형 정의

**기본 Dedrick(Elementary)** — $d=1$을 숨은 가정으로 깔고 가는 버전이에요:

$$
\underbrace{y}_{\text{농도축}}=\frac{\overbrace{C}^{\text{농도}}}{\underbrace{Dose/BW}_{\text{kg당 용량}}},\qquad \underbrace{x}_{\text{시간축}}=\frac{\overbrace{t}^{\text{시간}}}{\underbrace{BW^{1-b}}_{\text{기본 시간}}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $y$ | dose-normalized concentration | 종간 농도축 정규화 | dose, BW, V 지수 가정 |
| $x$ | normalized time | 종간 시간축 정규화 | $b$, $d$, 체중 범위 |
| $b$ | 무차원 | CL/flow 지수 | 대사·혈류·GFR prior 및 예외 |
| $d$ | 무차원 | V/extent 지수 | $d=1$ 여부가 elementary/complex를 가름 |

💡 **비유 — 비디오 프레임 정렬:** Dedrick plot은 서로 다른 속도로 재생되는 영상을 같은 프레임 속도에 맞춰서 겹쳐 보는 작업이에요. 시간이 어긋나면 배우가 다른 게 아니라 **프레임 보정이 틀렸을** 수 있어요. Elementary는 $d=1$이라는 숨은 가정을 갖고 있어서, PK29처럼 $d\ne 1$인 약물에서는 Complex로 넘어가야 합니다. 입에 붙여 둘 switch 규칙은 — **log-log V vs BW 기울기가 0.9–1.1 밖이면 Complex Dedrick을 검토합니다.**

**복합 Dedrick(Complex)** — $d\ne 1$ 일반형:

$$
\underbrace{y}_{\text{농도축}}=\frac{\overbrace{C}^{\text{농도}}}{\underbrace{Dose/BW^d}_{\text{V지수 용량}}}=\frac{\overbrace{C}^{\text{농도}}\cdot\overbrace{BW^d}^{\text{공간 보정}}}{\underbrace{Dose}_{\text{투여량}}},\qquad \underbrace{x}_{\text{시간축}}=\frac{\overbrace{t}^{\text{시간}}}{\underbrace{BW^{d-b}}_{\text{복합 시간}}}
$$

이름이 두 개 있어요 — Kallynochron은 $d=1$ 가정 아래의 **kg당 생리학적 시간**, Apolysichron은 $d$를 명시적으로 반영한 **일반화된 생리학적 시간**입니다 [G&W §2.10.6–2.10.7, p.184–189]. 영어 그리스어식 이름이라 외우기 까다로운데, **K는 kg(=1), A는 anyspace($d$)**로 머릿속에 묶어 두면 헷갈리지 않아요.

#### B. 도출

단일 지수 모델에서 출발해 봅니다:

$$
\underbrace{C}_{\text{농도}}=\frac{\underbrace{D_{iv}}_{\text{IV dose}}}{\underbrace{V}_{\text{V 공간}}}\cdot \overbrace{e^{-(CL/V)t}}^{\text{일차 제거}}
$$

여기 알로메트릭 식을 그대로 대입:

$$
\underbrace{C}_{\text{농도}}=\frac{\underbrace{D_{iv}}_{\text{Dose}}}{\underbrace{c\cdot BW^d}_{\text{V 스케일}}}\cdot \overbrace{e^{-\left(\underbrace{a/c}_{\text{CL/V 절편}}\right)\cdot\underbrace{BW^{b-d}}_{\text{k 체중지수}}\cdot \underbrace{t}_{\text{시간}}}}^{\text{체중 보정 제거}}
$$
[G&W Eq.2:384, p.179]

식이 말하는 건 결국 — 농도는 $Dose/BW^d$로, 시간은 $BW^{d-b}$로 정규화돼야 한다는 거예요. Buckingham π 정리류의 차원 해석을 PK에 옮긴 버전이라고 보면 됩니다 — 질량·시간·부피 차원을 제거하면 독립적인 무차원 그룹이 남고, Dedrick 변환이 바로 그 그룹이에요.

#### C. AUC 관계식

기본 Dedrick 맥락에서 G&W는 AUC가 $1/a$로 정리됨을 보입니다 [G&W Eq.2:386, p.179]. 이건 C5의 'equal unbound AUC' 조건이랑 동떨어진 별개 사실이 아니에요 — **같은 논리가 수식으로 먼저 나타난 단계**입니다. 그러니까 Dedrick 정규화가 통과한다는 건, equal-AUCu backbone이 그 자료에서 작동할 수 있다는 신호이기도 해요.

#### D. 데이터 앵커 — PK28과 PK29

**PK28 Methadone**(저추출 μ-opioid, 5종 자료 중 mouse/rat/man IV bolus 사용)는 기본 Dedrick으로 깔끔하게 중첩됩니다 [G&W p.184–186; PK28 p.611–614]. → 그래서 **$d\approx1$ 가정 하에서 Elementary Dedrick이 통과하는** 대표 사례예요. **단, case는 단일 dose level**이라서 G&W도 ≥2 dose levels, 다회 투여·항정상태, 모델 잘못 지정 배제가 필요하다고 경고합니다 [PK28 p.614].

**PK29 Compound X**(미상의 5종 약물; mouse 20 g, rat 250 g, monkey 3.5 kg, dog 14 kg, man 70 kg) [G&W p.186–189; PK29 p.615–620]:

| 출처 | $a$ | $b$ | $c$ | $d$ | $e$ | $g$ |
|---|---|---|---|---|---|---|
| G&W §2.10.7 [G&W p.189] | 0.021 | 0.74 | 0.076 | 1.18 | 0.56 | 0.075 |
| PK29 case [G&W p.619] | 0.021 | 0.75 | 0.10 | 1.21 | 0.54 | 0.071 |

PK29에서 핵심은 $d\approx1.18$~1.21이라는 점이에요 — V가 체중에 거의 비례하지 않고 살짝 강하게 늘어나요. → 그래서 **$d\ne1$일 때 Elementary가 깨지고 Complex Dedrick으로 가야 한다**는 사실의 정량적 사례입니다. 체중 범위는 산술적으로 $70/0.020=3500$-fold, PK29 case 본문에서는 약 3000-fold — 본문에서는 **"약 3000–3500-fold"로 표기**합니다.

**Elementary vs Complex 전환 규칙을 한 줄로:** log-log $V$ vs $BW$ 기울기가 **0.9–1.1 밖**이면 Elementary($d=1$ 가정)를 고집하지 않아요. PK29처럼 $d\approx1.18$이면 $C/(Dose/BW^d)$랑 $t/BW^{d-b}$를 쓰는 Complex Dedrick으로 갑니다.

> 📖 **G&W Case Study PK28, p.613, Fig.28.2:** Methadone의 elementary Dedrick 중첩 — mouse/rat/human 농도-시간 곡선이 공통 생리학적 시간 척도 위로 접혀 들어가는 모습을 학습자 관점에서 가장 잘 보여 줍니다. 한 번 보면 "왜 정규화 시간축을 쓰는지"가 그림 한 장으로 정리돼요.

> 📖 **G&W Case Study PK29, p.619, Fig.29.3:** $d\ne 1$이고 다구획 스케일링이 들어올 때 **왜 Complex Dedrick이 필요한지**를 보여 주는 최종 시각 증거입니다 — allometric parameter set이 곡선 중첩에 어떻게 연결되는지를 그림으로 보여 줘요.

---

**C4 이번 카드 핵심내용.**
PK28처럼 $d\approx1$인 곡선 중첩은 Elementary Dedrick으로 충분해요. PK29처럼 $d\approx1.18$–1.21인 약물은 Complex Dedrick으로 가야 하고요. **overlay가 안 예쁘다고 그림 문제로 보는 순간** fan-out에 숨은 기전 신호를 놓치고, model misspecification 또는 $d$ 추정 실패로 이어집니다.

<!-- SLIDE_START: C5 | title: FIH 용량 번역 -->
<!-- SECTION_CORE: SC-07 -->

### ━━ C5. FIH 용량 번역(FIH Dose Translation)의 알로메트릭 백본(Allometric Backbone) ━━

C4에서 지수 구조가 **곡선 수준에서** 버틴다는 걸 확인했어요. 이제 그 구조가 dose/exposure backbone으로 어떻게 번역되는지를 봅니다. 그리고 — **이 backbone만으로는 첫 사람 용량이 안 된다**는 사실을 분명하게 짚어요.

**거장의 시각 — 실무 함정:** Equal-AUCu 식을 최종 FIH 시작 용량 공식처럼 쓰면 안전성 margin, PD metric, route/formulation, 기능적 연령이 전부 누락됩니다. **이 식은 노출 backbone으로 낮춰서 읽어야** 수식은 보존하면서 IND/NDA 문서에서 방어 가능한 caveat 구조가 만들어져요.

#### A. Equal-unbound-AUC 백본

$$
\underbrace{AUC_{u,rat}}_{\text{rat }AUC_u}=\underbrace{AUC_{u,man}}_{\text{human }AUC_u}=\frac{\overbrace{Dose_{rat}}^{\text{rat dose}}}{\underbrace{CL_{u,rat}}_{\text{rat }CL_u}}=\frac{\overbrace{Dose_{man}}^{\text{human dose}}}{\underbrace{CL_{u,man}}_{\text{human }CL_u}}
$$
[G&W Eq.2:417, p.190]

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $AUC_u$ | concentration×time | 비결합 노출 | dose, $CL_u$, $f_u$, 선형성 |
| $Dose$ | mass | 투여량 | 종, 안전역, route/formulation |
| $CL_u$ | volume/time | 비결합 청소율 | $f_u$ 보정, 대사·배설 기전 |
| $b$ | 무차원 | dose backbone에 들어가는 CL 지수 | flow prior, 기전 예외, sensitivity 선택 |

💡 **비유 — 다리 철골:** C5 식은 완성된 처방전이 아니에요. **다리의 철골**입니다. 철골 위에 안전 난간, 하중 제한, 통행 규칙을 다 붙여야 실제 환자가 건널 수 있어요. 그래서 backbone 규칙을 입에 붙여 두세요 — **Eq.2:420은 최종 FIH 용량이 아니라 노출 번역 backbone입니다.**

⚠️ Equal-AUCu가 같은 PD 효과나 같은 전체 곡선 모양을 보장하지 않아요 [G&W p.190].

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

$b<1$이면 큰 동물의 mg/kg dose는 작은 동물보다 낮아집니다. 그래서 — rat에서 mg/kg 그대로 사람에 적용하면 사람 dose가 과대해질 가능성이 높아요.

#### B. 가정 — 다섯 개가 동시에 성립해야 합니다

① 비결합 AUC가 약리 효과랑 연결돼야 해요. ② 표적 친화도와 관련 약리학이 종간에 크게 다르지 않아야 하고요. ③ PK가 선형 구간에 있어야 합니다. ④ $f_u$ 차이가 있으면 $CL_u$로 보정해야 하고요. ⑤ AUC가 적절한 노출 지표여야 해요 — 즉 "AUC 같은 양"이 PD에 해당하는 약물이어야 합니다. **Cmax 의존 독성**이나 **역치 초과 시간 지표**가 끼면 별도 판단이 필요해요.

G&W는 한 번 더 못 박습니다 — **동일 AUC라도 농도-시간 곡선의 모양은 상당히 다를 수 있다** [G&W p.190]. 그러니까 C5는 AUC backbone일 뿐이고, **전체 곡선 등가성을 보장하지 않아요.**

#### C. 소아·노인 맥락 — R&T 기반

R&T Ch.14는 한 줄로 정리합니다 — **연령·체중·성별이 약물 반응 변동성의 주요 원천**이고, **생활연령(chronologic age)이 기능적 연령(functional age)을 정의하지 않는다** [R&T p.411–412]. 연령을 고려하지 않는 일률 용량은 개별 노인의 필요를 충족하지 못할 수 있어요 [R&T p.412].

R&T Key Relationships의 BSA 근사:

$$
\underbrace{BSA}_{\text{BSA 근사}}=\underbrace{1.73}_{\text{70kg BSA}}\cdot\left(\frac{\overbrace{Weight}^{\text{체중}}}{\underbrace{70}_{\text{70kg}}}\right)^{\overbrace{0.75}^{\text{BSA 지수}}}
$$
[R&T p.436]

> 📌 **[보완 1] BSA 근사식의 출처와 다른 임상 BSA 식과의 관계 — 출처 명시 강화**
>
> 위 식은 **R&T Eq.14-2 (p.421)**예요. R&T가 같은 챕터에서 BSA 식을 **두 개** 함께 제시한다는 점이 중요합니다 — BW+Height 형(Eq.14-1)과 BW-only 0.75 형(Eq.14-2):
>
> $$
> \underbrace{BSA(m^2)}_{\text{BW+Height 형}}=\underbrace{0.0243}_{\text{R\&T 절편}}\cdot\overbrace{Weight(kg)^{0.538}}^{\text{BW 지수}}\cdot\overbrace{Height(cm)^{0.396}}^{\text{H 지수}}\qquad\text{[R\&T Eq.14-1, p.421]}
> $$
>
> $$
> \underbrace{BSA(m^2)}_{\text{BW-only 근사}}=\underbrace{1.73}_{\text{70kg BSA}}\cdot\left(\frac{\overbrace{Weight(kg)}^{\text{체중}}}{\underbrace{70}_{\text{기준 BW}}}\right)^{\overbrace{0.75}^{\text{편의적 매칭}}}\qquad\text{[R\&T Eq.14-2, p.421]}
> $$
>
> ⚠️ **R&T 본문이 직접 단 단서:** R&T p.421이 Eq.14-2를 도입할 때 명시적으로 적습니다 — **"Another approximation takes body weight only into account, provided that body weight is close to that expected for body height"** [R&T p.421]. 즉 Eq.14-2는 **신장이 체중에 부합할 때 쓰는 BW-only 근사식**이고, 체조성·비만·왜소 등으로 신장-체중 불일치가 있으면 Eq.14-1을 쓰는 편이 정확합니다.
>
> 💡 **0.75 지수의 의미 — "BSA의 진짜 알로메트릭 지수"가 아닙니다.** R&T Fig.22-3(p.734)은 종간 BSA의 알로메트릭 지수가 **2/3(0.67)에 가깝다**고 보여 줍니다 [R&T p.733–734]. 그런데 본 챕터 Eq.14-2는 0.67이 아니라 **0.75**를 씁니다. 왜요? R&T가 알로메트리 챕터(Ch.22)에서 명시적으로 적어요 — "in reality, we are not spherical, and functions are not directly proportional to body surface area, and **a value for b in the order of 0.75 is more appropriate**" [R&T p.734], 그리고 "given the inherent biological variability across species, in practice, the experimental data often do not allow a ready distinction between values of 0.67 and 0.75" [R&T p.734]. 결국 Eq.14-2의 0.75는:
>
> $$
> \underbrace{0.67}_{\text{기하학적 BSA}}\;\xrightarrow{\text{R\&T 편의적 매칭}}\;\underbrace{0.75}_{\text{Eq.14-2 채택값}}\;\xleftarrow{\text{CL/GFR prior와 한 줄로 정렬}}\;\underbrace{b\approx 0.75}_{\text{flow 변수 prior}}
> $$
>
> 한 줄로 — **Eq.14-2의 0.75는 "BSA의 진짜 알로메트릭 지수"가 아니라, 알로메트리 챕터 맥락에서 CL·GFR의 0.75 prior와 매칭하기 위한 R&T의 편의적 BW-only 근사**입니다.
>
> 💼 **실무 함정 — Eq.14-2를 "BSA 정의식"으로 외우지 않기.** 임상에서 BSA를 정확히 계산하려면 **신장과 체중을 둘 다** 쓰는 식이 더 적절합니다. R&T 자체가 Eq.14-1을 BW+Height 표준으로 함께 제공해요. 학습자가 Eq.14-2를 단독 정의식처럼 외우면 — 임상 표준 BSA 공식(Du Bois, Mosteller 등은 R&T 본 PDF에서 직접 인용 없음, `[교과서 외 임상 표준]`)과의 관계를 잃습니다. 보고서·심사 문서에서는 **"R&T Eq.14-2는 신장-체중 불일치가 작을 때의 BW-only 근사이며, 알로메트리 챕터의 0.75 prior에 매칭된 편의식"**으로 적습니다.

60세 일반 성인 대비 소아 유지 용량:

$$
\underbrace{Child\ maintenance\ dose}_{\text{소아 유지용량}}=\underbrace{1.5}_{\text{성인 보정}}\cdot\left(\frac{\overbrace{Weight_{child}}^{\text{소아 체중}}}{\underbrace{70}_{\text{70kg}}}\right)^{\overbrace{0.75}^{\text{BW 지수}}}\cdot\underbrace{Typical\ adult\ maintenance\ dose}_{\text{성인 용량}}
$$
[R&T Eq.14-6, p.432; Key Relationships, p.436]

다만 R&T는 곧바로 경고를 붙입니다 — **mg/kg 또는 mg/1.73 m² 규칙의 폭넓은 사용은 적용 한계(연령·체조성·신기능)를 명시하지 않으면 의심스럽다** [R&T p.435]. **BW 알로메트리는 시작점일 뿐이고, 소아·노인 용량 결정 공식 전체를 대체하지 않아요.**

#### D. 노인 대사 진술 — 단정하기 쉬운 함정

"CYP3A4 대사가 60세 이상 매년 1% 감소한다"라는 문장은 **과단정**이에요. R&T가 실제로 제시하는 건 두 줄입니다 — ① 크레아티닌 청소율이 성인기에서 약 **1%/yr** 감소한다는 경험 법칙 [R&T p.422], ② CYP3A 기질에서 노인이 청년보다 청소율이 낮으며, 그 연령 차이를 해석할 때 1%/yr 크레아티닌 청소율 경험치가 관련된다는 점 [R&T p.424]. 정리하면 — **노인에서는 신·간 기능과 생물학적 연령을 별도로 봐야 하고, CYP3A 청소율도 청년 대비 감소할 수 있지만 단순 선형 시간 함수로 쓰면 안 됩니다.**

> 📖 **R&T 5e, Ch.14, p.430, Fig.14-20:** $BW^{0.75}$ 하나로 소아·노인 용량이 해결된다는 흔한 오류를 **시각적으로 막아 줍니다** — 연령에 따라 maintenance-dose fraction이 달라지는 모습이 바로 C5의 caveat예요.

---

**C5 이번 카드 핵심내용.**
Equal unbound AUC를 맞추는 종간 dose backbone은 $Dose\propto BW^b$가 정해요. 그런데 소아·노인·FIH **실제** 용량은 functional age, renal/hepatic function, PD metric, safety margin이 지배합니다. Eq.2:420을 최종 FIH 용량으로 쓰는 순간 caveat가 누락되고, 재분석·정당화 요구로 이어질 수 있어요.

<!-- SLIDE_START: C5+ | title: 임상 확장 — Maturation, Body Composition, CL_R vs CL_H -->
<!-- SECTION_CORE: SC-07B -->

### ━━ C5+. [보강본] 임상 확장(Clinical Extensions): Maturation · Body Composition · $CL_R$ vs $CL_H$ ━━

C5의 equal-AUCu backbone은 **종간** 용량 번역의 척추예요. 그런데 같은 backbone을 **사람 안에서** 쓰려고 하면 — 신생아·영아·소아·노인·비만·신부전·간부전 환자들 — backbone만으로는 안 됩니다. 그래서 R&T가 Ch.14·Ch.15 전체에 걸쳐 깔아 둔 세 가지 보정 레이어를 명시적으로 잡아 둡니다.

**거장의 시각 — 한 줄 압축:** 사람 안 dose는 $\overbrace{BW^{0.75}}^{\text{C5 backbone}}\times \overbrace{F_{mat}}^{\text{maturation}}\times \overbrace{f_{size}}^{\text{LBW/TBW}}\times \overbrace{[RF\cdot fe+(1-fe)\cdot age]}^{\text{장기 기능}}$의 곱으로 봅니다. backbone 단독은 **종간 환율** 단계이고, 곱셈 한 칸이 빠질 때마다 임상에서 한 자릿수씩 어긋날 수 있어요.

```text
[C5 backbone]   →   [C5+ A. Maturation]   →   [C5+ B. Body Composition]   →   [C5+ C. CL_R vs CL_H 분기]
  BW^b              PMA-기반 sigmoid           LBW vs TBW (약물 극성)        fe·RF + (1-fe)·age factor
  종간 환율          0–2세 영아 핵심            비만·왜소 환자 핵심          신/간 dominant 약물 분리
```

---

#### A. Maturation 함수 — 영아·소아 청소율의 두 번째 곱셈 항

R&T Ch.14가 가장 강하게 못 박는 두 가지 사실:

1. **출생 후 신장·간 기능은 빠르게 성숙**합니다. **체중으로 정규화한** 크레아티닌 청소율은 신생아에서 낮다가 **약 6개월에 일반 60세 성인의 약 2배까지** 올라가고, 그 이후 천천히 감소해서 평생에 걸쳐 변화합니다 [R&T p.420, Fig.14-8].
2. **미숙아의 conceptional age(수태 후 주수)가 신장 기능을 예측**합니다 — R&T Fig.14-9는 conceptional age 28주에서 40주 사이에 크레아티닌 청소율이 **지수적으로 약 8배 증가**한다는 자료를 그려 줍니다 [R&T p.420–421]:

$$
\underbrace{CL_{cr}\left(\tfrac{mL}{min\cdot 1.73\,m^2}\right)}_{\text{BSA-정규화 CL}_{cr}}=\underbrace{0.373}_{\text{Fig.14-9 절편}}\cdot \overbrace{e^{\,0.111\cdot Age_{wk}}}^{\text{지수 성장}}\qquad\text{[R\&T Fig.14-9, p.421]}
$$

R&T 본문 표현 그대로 — **신생아 CL은 BSA로 정규화해도 여전히 크게 depressed** 되어 있고, 따라서 알로메트리($BW^{0.75}$)만으로는 신생아·영아 용량을 못 잡아요 [R&T p.420–421]. R&T는 같은 챕터에서 간 효소(CYP2D6, CYP3A4)도 출생 후 1년 내 빠르게 성숙한다는 자료(Fig.14-11)와, gut wall CYP3A4 활성도 출생 후 빠르게 증가한다는 자료(Fig.14-12)를 함께 제시합니다 [R&T p.423–424].

##### A-1. R&T가 직접 제시하는 maturation 골격

R&T가 명시적으로 적은 형태를 옮기면 (보강본의 일반화 없이 본문 그대로):

$$
\underbrace{CL_{cr}(neonate)}_{\text{신생아 신장 CL}}=\overbrace{\underbrace{Adjustment}_{\text{체격(BW/BSA) 기반}}}^{\text{algometric}}\cdot \overbrace{\underbrace{Maturation\ component}_{\text{출생 후 성숙}}}^{\text{maturation}}\qquad\text{[R\&T 본문, p.420]}
$$

R&T 본문 인용 그대로 — **"creatinine clearance in this age range can be thought of as the product of an adjustment based on body size and a maturation component"** [R&T p.420]. 즉 사람 안에서 청소율은 알로메트리 단독이 아니라 **알로메트리 × maturation**의 곱이라는 게 R&T의 직접 진술이에요.

##### A-2. Anderson-Holford 형 sigmoid — `[교과서 외 구현/실무 해석]`

현대 소아 PopPK에서 maturation은 보통 sigmoid (Hill-type) 함수로 모델링됩니다. **본 PDF (G&W 5e §2.10, R&T 5e Ch.14)에는 직접 제시되지 않은 형태**예요 — 이건 R&T가 본문 텍스트로 풀어 둔 "adjustment × maturation component" 골격을 pharmacometrics 문헌이 명시적 함수형으로 정리한 것입니다. 따라서 다음 표기는 **`[교과서 외 구현/실무 해석]`** 태그로 분리합니다:

$$
\underbrace{F_{mat}(PMA)}_{\text{성숙 분율}}=\frac{\overbrace{PMA^{\,Hill}}^{\text{post-menstrual age 지수}}}{\underbrace{TM_{50}^{\,Hill}}_{\text{50\% 성숙 PMA}}+\overbrace{PMA^{\,Hill}}^{\text{PMA 지수}}}\qquad\text{[교과서 외 구현 — pharmacometrics 표준형]}
$$

- $PMA$ = postmenstrual age (= 40 + 출생 후 주수), 단위 주.
- $TM_{50}$ = 50% 성숙에 도달하는 PMA, 약물·효소·경로마다 다름.
- $Hill$ = sigmoid의 가파름.
- $F_{mat}\to 1$이면 완전 성숙, $F_{mat}\to 0$이면 미성숙 상태.

이걸 C5 backbone 위에 곱해서 쓰면 — **사람 안 dose 계산의 표준 골격**이 나옵니다:

$$
\underbrace{CL_{individual}}_{\text{개체 CL}}=\overbrace{\underbrace{CL_{std}}_{\text{성인 표준 CL}}\cdot\left(\frac{\overbrace{BW}^{\text{체중}}}{\underbrace{70}_{\text{성인 기준}}}\right)^{\overbrace{0.75}^{\text{C5 backbone}}}}^{\text{알로메트리}}\cdot \overbrace{F_{mat}(PMA)}^{\text{A. maturation}}\cdot \overbrace{OF}^{\text{C. organ function}}\qquad\text{[교과서 외 표준 구현]}
$$

여기서 $OF$ = organ function adjustment (다음 C 절). **R&T가 본문 텍스트로 깔아 둔 골격을 함수형으로 적은 형태**라는 점을 보고서에 명시합니다.

⚠️ **함정 — $BW^{0.75}$ 단독은 영아 dose에 부정확.** R&T 본문이 직접 적습니다 — "the lack of maturation of renal and hepatic function necessitates that the rate of administration of drugs to both neonates and young infants be reduced, **even on a body-weight basis**, if toxicity is to be avoided" [R&T p.430]. 즉 신생아·영아에서는 mg/kg 그대로 적용해도 toxic할 수 있어요 — backbone에 $F_{mat}$를 곱하지 않으면 안 됩니다.

##### A-3. 임상 함의

- **신생아 (postnatal 0–28일):** $F_{mat}$가 매우 낮습니다. R&T Fig.14-9에 따르면 미숙아일수록 더 낮아요. **TDM이 거의 필수**예요 — R&T 본문이 직접 언급합니다 [R&T p.430].
- **영아 (1개월–2세):** $F_{mat}$가 빠르게 변합니다. **약물 노출이 며칠 단위로 달라질 수 있어** 모니터링을 계속 업데이트해야 해요 [R&T p.420].
- **소아 (2세–12세):** $F_{mat}\approx 1$. 이 시점부터는 $BW^{0.75}$ 알로메트리가 다시 주된 backbone이 됩니다. R&T 본문 — "from about 6 months to 20 years of age, metabolism follows the same general trend as does the renal function" [R&T p.424].

> 📖 **R&T 5e, Ch.14, p.420–421, Fig.14-8/Fig.14-9:** 신생아 신장 기능이 출생 직후 며칠 안에 거의 두 배로 뛰는 모습, 그리고 conceptional age 28–40주 사이에 BSA-정규화 후에도 큰 격차가 남는 모습이 한 장에 들어 있어요. "$BW^{0.75}$ × maturation"을 곱셈으로 보지 않으면 신생아 용량은 못 잡힌다는 메시지의 가장 직접 증거입니다.

---

#### B. Body Composition — Lean Body Weight vs Total Body Weight

R&T Ch.14가 비만·왜소 환자 용량을 다룰 때 가장 강조하는 분기점이 **약물의 물리화학적 성질에 따라 어떤 체격 지표를 쓰느냐**입니다. R&T 본문이 직접 적은 두 줄을 분리해 둡니다:

1. **친수성·극성 약물 (digoxin 등):** "digoxin and polar drugs, for example, do not partition well into fat. Accordingly, **for these drugs, $V_u$ correlates better with lean body mass (body weight minus fat content)**, which is similar in obese and average persons of the same height and frame, than with total body weight" [R&T p.418, p.434].
2. **친지질 약물 (diazepam 등):** R&T Table 14-7이 직접 보여 줍니다 — diazepam은 비만 환자에서 V가 **2.81 L/kg**, 정상에서 **1.53 L/kg**으로 **체중 보정 후에도** 의미 있게 큽니다 [R&T p.439]. 반면 theophylline·digoxin(극성)은 비만/정상에서 weight-corrected V가 오히려 비만에서 **낮아져요** [R&T p.439, Table 14-7].

##### B-1. R&T가 제시하는 Lean Body Weight 식

R&T Key Relationships(p.436)이 직접 제공하는 LBW 공식 (Eq.14-10·14-11):

$$
\underbrace{LBW_{male}(kg)}_{\text{남성 LBW}}=\underbrace{1.10}_{\text{선형 계수}}\cdot\overbrace{Weight(kg)}^{\text{체중}}-\underbrace{\frac{128\cdot\overbrace{Weight(kg)^2}^{\text{체중 제곱}}}{\underbrace{(100\cdot Height(m))^2}_{\text{신장 제곱 보정}}}}_{\text{지방 보정항}}\qquad\text{[R\&T Eq.14-10, p.434]}
$$

$$
\underbrace{LBW_{female}(kg)}_{\text{여성 LBW}}=\underbrace{1.07}_{\text{선형 계수}}\cdot\overbrace{Weight(kg)}^{\text{체중}}-\underbrace{\frac{148\cdot\overbrace{Weight(kg)^2}^{\text{체중 제곱}}}{\underbrace{(100\cdot Height(m))^2}_{\text{신장 제곱 보정}}}}_{\text{지방 보정항}}\qquad\text{[R\&T Eq.14-11, p.434]}
$$

R&T 본문이 직접 단 단서 — **"these relationships do not apply to highly muscular individuals"** [R&T p.434]. 즉 LBW 공식은 보디빌더·운동선수 같은 고근육량 개체에는 안 맞아요.

##### B-2. 약물별 체격 지표 선택 — R&T의 직접 자료

R&T Table 14-7의 자료를 정리하면:

| 약물 | 극성 | Obese V (L) | Control V (L) | Obese V/kg | Control V/kg | 보정 결론 |
|---|---|---:|---:|---:|---:|---|
| Theophylline | 극성 (친수성) | 29 | 27 | 0.32 | 0.47 | weight-corrected V가 비만에서 ↓ → **LBW 기반 보정** |
| Digoxin | 극성 (친수성) | 981 | 937 | 10.7 | 14.3 | 같은 패턴 → **LBW 기반 보정** |
| Diazepam | 비극성 (친지질) | 292 | 91 | 2.81 | 1.53 | weight-corrected 후에도 ↑ → **TBW 기반 보정** |

R&T 직접 인용 그대로 [R&T p.439, Table 14-7].

##### B-3. 임상 의사결정 트리

R&T 본문이 명시하는 두 가지 — ① "drug elimination (e.g., renal clearance) is not increased because of either added adipose or muscle tissue" [R&T p.434], ② "in overweight and obese patients, creatinine clearance can be estimated, to a first approximation, **from lean body weight**" [R&T p.434]. 즉:

- **친수성·극성 약물 + 비만 환자 → LBW 기반 dose / CrCl 추정.**
- **친지질 약물 + 비만 환자 → TBW 기반 dose** (V가 체중에 비례 이상으로 커지는 자료 있음).
- **고근육량 환자 → Eq.14-10/14-11 적용 안 됨, 별도 판단 필요.**

⚠️ **함정 — "체중이 늘었으니 dose도 그만큼 늘린다"는 단순화.** R&T가 직접 경고합니다 — "the difference in loading dose may not be as great as anticipated from body weight alone. However, as with age-related changes in distribution, **much depends on the physicochemical properties of the drug**" [R&T p.418]. 약물의 극성을 먼저 확인하지 않고 TBW로 일률적으로 보정하면 친수성 약물에서 dose 과대로 갈 수 있어요.

> 📖 **R&T 5e, Ch.14, p.439, Table 14-7:** theophylline/digoxin/diazepam 세 약물의 obese vs control V 자료가 한 표에 들어 있어요. "친수성·친지질 약물의 V는 체중에 다르게 반응한다"는 메시지를 자료 한 장으로 못 박는 R&T의 핵심 표입니다.

---

#### C. $CL_R$ vs $CL_H$ — 알로메트리 backbone의 신장·간 분기

C5 backbone $Dose \propto BW^b$는 **total CL에 단일 지수 $b$**를 적용합니다. 그런데 실제로 청소율은 **신장 청소율($CL_R$, GFR 의존)**과 **간 청소율($CL_H$, 효소·혈류 의존)**의 합이에요 — 두 경로의 알로메트릭 거동이 다릅니다.

##### C-1. R&T의 직접 분리식

R&T Ch.15는 사람 안 비결합 청소율 분리를 명시적으로 적습니다 [R&T p.453, Eq.15-7]:

$$
\underbrace{R_d}_{\text{환자/표준 CL}_u\text{ 비}}=\frac{\underbrace{CL_u(d)}_{\text{환자 CL}_u}}{\underbrace{CL_u(t)}_{\text{표준 60세/70kg CL}_u}}=\overbrace{\underbrace{RF\cdot fe(t)}_{\text{신장 경로}}}^{\text{C-1a}}+\overbrace{\underbrace{[1-fe(t)]\cdot\frac{(140-Age)\cdot Wt^{0.75}}{1936}}_{\text{비신장(주로 간) 경로}}}^{\text{C-1b}}\qquad\text{[R\&T Eq.15-7, p.453]}
$$

| 기호 | 의미 |
|---|---|
| $RF$ | renal function (표준 환자 대비 비) |
| $fe(t)$ | 표준 환자에서 신장 배설 분율 (= $CL_R / CL_{total}$) |
| $Age$ | 환자 연령 (년) |
| $Wt$ | 환자 체중 (kg) |
| $140 - Age$ | Cockcroft-Gault 형 연령 보정항 |
| $1936$ | 60세·70kg 표준 환자에서 $(140-60)\cdot 70^{0.75}\approx 1936$ |

이 식이 직접 보여 주는 두 가지:

1. **신장 경로 ($fe$ 높은 약물):** $R_d$가 $RF$에 거의 비례. R&T Fig.15-9A — $fe(t)\to 1$일 때 $R_d$는 거의 $RF$ 그 자체 [R&T p.454].
2. **비신장(간) 경로 ($1-fe$ 높은 약물):** $R_d$가 $(140-Age)\cdot Wt^{0.75}/1936$에 따라 움직임 — **연령·체중 알로메트릭 보정이 명시적으로 들어옴** [R&T p.453].

##### C-2. 한 표로 본 알로메트릭 분기

```text
                 ┌── 신장 (CL_R) ─── GFR-driven ── b ≈ 0.7-0.75
  Total CL   ────┤                                 (R&T: CrCl ∝ (140-Age)·Wt^0.75)
                 │
                 │                                 ┌─ High extraction → 간 혈류 지배 (b ≈ 0.75)
                 └── 비신장 (CL_NR) ─── Hepatic ───┤
                                                    └─ Low extraction → 효소 활성 지배 (b 다양)
```

##### C-3. R&T가 직접 적은 hepatic CL 변동성

R&T Ch.15(p.460대)가 cirrhosis 환자에서 hepatic CL을 high/intermediate/low extraction으로 분리해서 다룹니다. 핵심 메시지 — **high-extraction 약물은 hepatic blood flow에 비례** (verapamil 사례에서 CL이 cirrhosis에서 감소하며 F는 증가), **low-extraction 약물은 효소 활성과 $f_u$에 비례** (meptazinol 사례). 즉 간 청소율의 알로메트릭 거동은 **추출률에 따라 달라요** — 단일 $b=0.75$ prior로 묶으면 신장·간이 같은 약물끼리 섞입니다.

##### C-4. R&T의 노인 자료 — 신장·간 분리 진술

R&T Ch.14의 노인 자료를 분리해서 보면:

- **신장 (creatinine clearance):** 성인기에서 약 **1%/yr 감소** [R&T p.422]. → C-1의 $(140-Age)$ 항이 이걸 직접 반영.
- **간 (CYP3A 청소율):** 노인(65–75세) 평균 청소율이 청년(25–35세)의 **약 60–70%** [R&T p.424, Fig.14-13]. → 같은 약 30–40년 연령 차이를 1%/yr 신장 감소와 연결해서 해석하는 R&T 본문의 직접 진술 [R&T p.424].

R&T 본문이 직접 명시한 caveat — **"variability in all of these renal and hepatic functions, not only with age and weight but also across a given patient population of the same age and weight"** [R&T p.436]. 즉 신장·간 청소율은 age·weight 보정 후에도 여전히 환자 간 변동이 큽니다.

##### C-5. 임상 함의 — 캡스톤(Ch.16) 연결

이 분리가 왜 중요하냐 — Ch.16 캡스톤 워크플로우에서 환자 청소율 추정 시 $fe$가 0.5 이상이면 RF 보정이 dose에 직접, $fe$가 0.2 이하면 hepatic age/weight 보정이 dose에 직접 들어갑니다. **단일 $BW^{0.75}$ prior로 묶으면 신장 의존 약물과 간 의존 약물이 같은 식에 섞여서 PK 변동성을 임상에서 잘못 해석**하게 돼요 [R&T p.453–455 골격].

⚠️ **함정 — total CL에 $b=0.75$ 한 줄 보정의 한계.** R&T 본문 직접 — "ideally, **renal clearance should be correlated with creatinine clearance, and the nonrenal clearance should be examined separately** for its dependence on age, weight, and perhaps renal disease" [R&T p.455]. PopPK 보고서에 total CL에 WT exponent 하나만 박는 게 통상이지만, **fe 정보가 있으면 분리해서 모델링하는 게 R&T의 직접 권고**입니다.

> 📖 **R&T 5e, Ch.15, p.453–454, Eq.15-7 + Fig.15-9:** 신장·간 청소율 분리가 한 식과 한 그림에 들어 있어요. $fe$에 따라 $R_d$가 어떻게 달라지는지, 그 안에서 알로메트릭 $Wt^{0.75}$가 어디에 박혀 있는지를 한 번에 보여 주는 R&T의 핵심 도해입니다.

---

**C5+ 이번 카드 핵심내용.**
사람 안 dose 계산은 C5 backbone $BW^{0.75}$ 단독이 아니라, **알로메트리 × maturation × body composition × organ function**의 곱입니다. R&T Ch.14 본문이 직접 적은 골격을 옮긴 것이고, 함수형 sigmoid maturation(Anderson-Holford)은 R&T 골격의 pharmacometrics 표준 구현으로 `[교과서 외 구현]`. 세 레이어 중 하나만 빠져도 신생아·비만·신부전 환자에서 dose가 한 자릿수씩 어긋날 수 있어요 — 특히 backbone-only로 LBW vs TBW 차이를 무시하면 친수성/친지질 약물군이 통째로 섞이고, $fe$ 분리를 빼면 신장 의존 약물과 간 의존 약물이 같은 prior에 묶입니다.

> ## ▶ §2 폐막 — 알로메트릭 의사결정 워크스루(Allometric Decision Walkthrough)
>
> 이 워크스루는 새 수치나 새 예시를 도입하지 않아요. C1–C5 본문에서 확정된 수식·anchor·진단만으로, **동물 PK 데이터셋 하나를 받아서 사람 노출 추정에 도달하는 5단계 의사결정**을 한 호흡에 통과하는 시연입니다.
>
> **Step 1 — 변수 유형 진단 (C1 → C2/C3).** 받은 변수가 뭐예요? CL/GFR/blood flow면 **흐름**이라 $b\approx 0.75$로 진입 (C2). V/blood volume/tissue mass면 **공간**이라 $d\approx 1$로 진입 (C3). 한 줄로: **"flow면 0.75, extent면 1."** 이 분류가 틀리면 C4–C5 전체가 무너집니다.
>
> **Step 2 — Prior 타당성 점검 (C1 척도 가정 + C2 실패 조건).** $b\approx 0.75$ prior를 그대로 써도 될까? **6개 트리거** 중 하나라도 강하게 의심되면 prior를 sensitivity로 격하해요 — 종간 $f_u$ 차이, CYP isoform 차이, 비선형 MM 동태, 장간 순환, 투여 경로·제형 차이, central/peripheral V 비율 drift. $f_u$ 차이가 크면 total CL 대신 $CL_u$를 스케일링합니다 (Eq.2:421).
>
> **Step 3 — 시간축 도출 (C3).** $b$랑 $d$로 두 시간축을 **동시에** 적어요 — $t_{1/2} \propto BW^{d-b} \approx BW^{0.25}$ (큰 동물 = 긴 반감기), $k_{el} \propto BW^{b-d} \approx BW^{-0.25}$ (큰 동물 = 작은 fraction 제거 속도). 두 부호를 같이 보지 못하면 C4 정규화가 어긋납니다.
>
> **Step 4 — Dedrick 진단 (C4).** 종간 자료가 있으면 Elementary($d=1$ 가정, $t/BW^{1-b}$)를 먼저 시도해요. log-log V vs BW 기울기가 **0.9–1.1 안**이면 Elementary로 충분, 밖이면 Complex($t/BW^{d-b}$, $C\cdot BW^d/Dose$)로 전환. **PK28(Elementary 통과) ↔ PK29($d\approx 1.18$로 Complex 필요)** 가 그 벤치마크 쌍입니다. Curve fan-out이 남으면 그건 "예쁜 overlay 실패"가 아니라 **기전 신호**예요.
>
> **Step 5 — Equal-AUCu Dose Backbone 적용 (C5 + R&T 보강).** $Dose_{man}=Dose_{animal}\cdot (BW_{man}/BW_{animal})^b$를 한 줄로 적되, 그 위에 **6개 레이어**를 명시적으로 얹습니다 — (i) AUC vs Cmax-driven 독성 선택 근거, (ii) $f_u$ 보정, (iii) PK 선형성 가정 점검, (iv) safety margin/toxicology, (v) route/formulation, (vi) PD metric. 소아·노인에는 R&T Ch.14의 BSA 근사식, 소아 유지 용량 식, chronologic vs functional age 경고, 크레아티닌 청소율 ~1%/yr 경험치를 backbone 위에 한 층 더 얹어요.
>
> **Step 6 — [보강본] 임상 확장 레이어 적용 (C5+).** Backbone과 R&T 6 레이어 위에 마지막으로 **사람 안 보정 3 레이어**를 얹습니다 — (A) Maturation: 환자가 신생아·영아면 $F_{mat}(PMA)$를 곱하고, BW^0.75 단독은 사용하지 않음; (B) Body composition: 약물 극성을 먼저 확인하고 친수성→LBW(Eq.14-10/14-11), 친지질→TBW로 보정 선택; (C) Organ function 분기: $fe$로 신장·간 경로를 분리하고, R&T Eq.15-7의 $RF\cdot fe + (1-fe)\cdot (140-Age)\cdot Wt^{0.75}/1936$ 구조로 환자 청소율을 추정.
>
> **한 줄 마무리:** 이 6단계가 자동 회상되면 §1 Target Mental Model이 완성됩니다. 완성된 학습자는 "$0.75$를 외우는 사람"이 아니라 **"$0.75$를 prior로 두고, 자료가 prior를 언제 밀어내는지 판단하고, 그 backbone 위에 maturation·body composition·organ function을 어떻게 곱할지 결정하는 사람"**이에요.

---

<!-- SLIDE_START: §5 | title: 혼동쌍 분해 -->
<!-- SECTION_CORE: SC-08 -->

## §5 — 혼동쌍 분해(Confusion Pair Dissection)

이 세 쌍 중 하나만 머릿속에서 섞여도 표·그림·dose narrative가 동시에 흔들립니다. 그래서 각 쌍을 **무엇이 다른지**가 아니라 **헷갈리면 어떤 임상 결과가 나오는지** 기준으로 분해해요.

### Pair 1. 청소율 지수 $b$ vs 분포용적 지수 $d$

| 비교 기준 | 개념 A: $b$ — CL 지수 | 개념 B: $d$ — V 지수 |
|---|---|---|
| 단위 / 차원 | 무차원; flow/rate 변수의 체중 스케일 | 무차원; space/extent 변수의 체중 스케일 |
| 수식 내 위치 | $CL=a\cdot BW^b$, $k_{el}\propto BW^{b-d}$ | $V=c\cdot BW^d$, $t_{1/2}\propto BW^{d-b}$ |
| 변화 원인 | 대사율, 장기 혈류, GFR, 단백 결합·수송체·비선형성 | 체수분, 혈액량, 조직 부피, 지방 분포, 조직 친화성 |
| 혼동 시 임상 결과 | CL scaling에 $d=1$을 넣어 $b=1$ 선형 kg당 오류 발생 | V scaling에 $b=0.75$를 넣어 분포용적·시간축 오판 |

**치명타.** rat 250 g → human 70 kg에서 $b=0.75$ 대신 $d=1$처럼 선형으로 스케일링하면 $(70/0.25)^{0.25}\approx$ **4.1배 차이**, mouse 23 g → human은 약 **7.4배**, R&T 20-g mouse 예시는 **7.7배**. 첫 사람 노출 추정의 자릿수가 바뀝니다.

⚡ **기억 고리 — 기능 vs 공간:** CL은 기능적 처리 능력, V는 물리적 분포 공간. 결론은 한 줄이에요 — $t_{1/2}=0.693\cdot V/CL\propto BW^{d-b}\approx BW^{0.25}$. 큰 동물은 절대 CL은 크지만 단위 시간당 fraction 제거는 작습니다.

### Pair 2. Kallynochron vs Apolysichron

| 비교 기준 | 개념 A: Kallynochron | 개념 B: Apolysichron |
|---|---|---|
| 단위 / 차원 | $t/BW^{1-b}$; $d=1$ 가정의 생리학적 시간 | $t/BW^{d-b}$; $d$ 반영 생리학적 시간 |
| 수식 내 위치 | Elementary Dedrick x축 | Complex Dedrick x축 |
| 변화 원인 | V가 체중에 거의 비례할 때 유지 | V 지수가 1에서 벗어날 때 필요 |
| 혼동 시 임상 결과 | $d\ne 1$에서 curve fan-out을 놓침 | 필요 없는 complex 보정으로 해석 과잉 가능 |

**기억 고리.** Kallynochron은 kg 단위로 정규화한 생리학적 시간, Apolysichron은 $BW^d$ 단위로 정규화한 생리학적 시간. PK29 compound X처럼 $d>1$이면 차이가 그제야 드러납니다.

### Pair 3. BW 알로메트릭 스케일링 vs BSA 스케일링

| 비교 기준 | 개념 A: $BW^b$ allometry | 개념 B: BSA scaling |
|---|---|---|
| 단위 / 차원 | 변수별 지수 $b$를 갖는 체중 기반 거듭제곱 | $BSA\approx1.73(Weight/70)^{0.75}$ 형태의 체표면적 근사 |
| 수식 내 위치 | $Y=a\cdot BW^b$의 지수 | BSA 또는 mg/1.73 m² dose rule에 들어가는 근사 지수 |
| 변화 원인 | 화합물·변수 특이성, 종 수, 결합, 대사·수송 기전 | 연령, 체조성, 신기능 한계를 명시해야 함 [R&T p.435] |
| 혼동 시 임상 결과 | 종 수 부족 시 기울기 불안정 또는 기전 예외 누락 | 소아·노인 용량을 과도하게 단순화 |

**정리.** BSA는 알로메트리의 적이 아니라 임상적으로 굳어진 $BW^{0.75}$ 근사예요. 다만 "BSA"라는 이름이 붙었다고 maturation·obesity·functional age 문제가 사라지진 않습니다. **보강본 추가:** R&T가 같은 챕터에서 BW+Height 형(Eq.14-1, $0.0243\cdot W^{0.538}\cdot H^{0.396}$)을 함께 제시한다는 점을 잊지 마세요 — 0.75 형(Eq.14-2)은 신장-체중 부합이 전제된 BW-only 근사입니다.

⚡ **기억 고리 — 직선 도로 vs 우회로:** 단순 알로메트리($y=a\cdot BW^b$)는 종간 스케일링을 끝내는 직선 도로. MLP·brain weight·PPB correction 같은 보정 인자는 특정 약물에서 대사·결합 차이가 클 때 필요한 우회로이고, BSA 변환도 maturation/binding/disease state 문제까지 해결해 주진 않아요.

**§5 한 줄로 닫기:** $b/d$, Kallynochron/Apolysichron, BSA/BW allometry 중 **하나만 섞여도** 표·그림·dose narrative가 동시에 흔들립니다.

<!-- SLIDE_START: §7 | title: 자기점검 -->
<!-- SECTION_CORE: SC-09 -->

## §7 — 자기점검(Self-Test): 능동 회상 모듈

자기점검의 목표는 수치 암기가 아니에요. 입에서 자동으로 나와야 하는 건 **세 가지 방어 능력** — (1) $b$랑 $d$를 즉시 구별, (2) $b=1$ 오류가 dose/AUC에 주는 방향을 설명, (3) 출처 불일치랑 NOT_IN_SOURCE 규제 표현을 자발적으로 차단. **보강본**에서는 Q9–Q11을 추가해 maturation·LBW·신장/간 분기를 능동 회상하게 합니다.

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

*왜 이 질문:* **4.1 vs 7.4 vs 7.7배**가 species pair와 함께 입에서 나오는지 확인. species pair 없이 fold만 외우면 보고서 검토에서 바로 깨집니다.

**질문:** 23-g mouse → 70-kg human에서 $b=1$과 $b=0.75$ 차이는 몇 배인가? rat 250 g → human에서는?

**정답:**
- Mouse 23 g → human 70 kg: $(70/0.023)^{1-0.75}\approx$ **7.4배**.
- Rat 250 g → human 70 kg: $(70/0.25)^{0.25}\approx$ **4.1배**.
- R&T 20-g mouse 예시: **3500 vs 455 = 7.7배** [R&T p.733].
- Target AUC 기반 용량 계산에서는 CL 과대예측이 dose 과대 산출로 이어질 수 있습니다.

---

### Q3. 도출 — $t_{1/2}$와 $k_{el}$의 종간 지수

*왜 이 질문:* 한 번 손으로 도출하면 $V/CL$이랑 $CL/V$의 부호가 반대라는 사실이 오래 남아요. C3 실패 모드("$k_{el}$ 부호 놓침")의 직접 예방.

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

*왜 이 질문:* PK28 ↔ PK29 벤치마크 쌍을 switch trigger와 함께 외우게 만드는 진단 회상이에요. "log-log V vs BW 기울기가 0.9–1.1 밖이면 Complex"가 입버릇이 되어야 PK29류 약물에서 정규화가 안 어긋납니다.

**질문:** Elementary Dedrick과 Complex Dedrick의 y축/x축 변환을 쓰고, 언제 Complex가 필요한지 답하세요.

**정답:**
- Elementary: $C/(Dose/BW)$ vs $t/BW^{1-b}$; $d=1$ 가정.
- Complex: $C/(Dose/BW^d)$ 또는 $C\cdot BW^d/Dose$ vs $t/BW^{d-b}$.
- log-log $V$ vs $BW$ 기울기가 1에서 벗어나면 (예: PK29 compound X의 $d\approx1.18$) Complex Dedrick이 필요합니다.

---

### Q5. 출처 불일치 처리 — PK28/PK29

*왜 이 질문:* 학술 보고서·심사 문서에서 source-internal 수치 불일치를 임의로 하나로 "고정"하는 것은 **무결성 위반**이에요. citation scope를 함께 적는 습관이 들어야 합니다.

**질문:** PK28 methadone과 PK29 compound X의 source-internal 수치 불일치를 어떻게 인용해야 하나요?

**정답:**
- **PK28 methadone rat $t_{1/2}$:** G&W §2.10.6 본문은 2.9 h, PK28 case는 3.9 h. 하나로 고르지 말고 **`[§2.10.6 set]` 또는 `[PK28 case set]`을 명시**합니다.
- **PK29 parameter set:** G&W §2.10.7은 $a=0.021, b=0.74, c=0.076, d=1.18, e=0.56, g=0.075$; PK29 case는 $a=0.021, b=0.75, c=0.10, d=1.21, e=0.54, g=0.071$. **citation scope와 수치를 일치시킵니다.**

---

### Q6. 적용 — human CL 예측

*왜 이 질문:* 숫자가 손에서 나오는지 확인. 이 계산이 입에서 자동으로 안 나오면 FIH 노출 번역 표를 그 자리에서 못 채웁니다.

**시나리오:** Mouse BW=25 g, observed CL=0.012 L/hr. 70-kg human CL을 (a) $b=0.75$, (b) $b=1.0$으로 계산하고 차이를 해석하시오.

**정답:**

(a) $CL_{human}=0.012\cdot(70/0.025)^{0.75}\approx$ **4.6 L/hr**.
(b) $CL_{human}=0.012\cdot(70/0.025)^1\approx$ **33.6 L/hr**.

$$
\underbrace{CL_{human}}_{\text{human CL}}=\underbrace{CL_{mouse}}_{0.012}\cdot\left(\frac{\overbrace{70}^{\text{human kg}}}{\overbrace{0.025}^{\text{mouse kg}}}\right)^{\overbrace{b}^{\text{선택 지수}}}
$$

차이는 **약 7.3배**. $b=1$은 선형 kg당 오류이고, target AUC 기반에서는 dose도 과대 산출할 수 있습니다.

---

### Q7. 적용 — 소아·노인 용량 맥락

*왜 이 질문:* R&T Ch.14의 핵심 메시지(chronologic ≠ functional age)가 입에서 나오는지 확인. C5 backbone만 외운 학습자는 소아·노인 용량을 단순화 오류로 망칩니다.

**질문:** 왜 소아·노인 용량에서 $BW^{0.75}$만으로 충분하지 않나요?

**정답:** R&T Ch.14는 **생활연령이 기능적 연령을 정의하지 않는다**고 설명합니다 [R&T p.411–412]. 소아에서는 renal/hepatic maturation, 체수분·결합 변화가 중요하고, 노인에서는 renal function, hepatic metabolism, 질환 상태, 체조성이 중요해요. **$BW^{0.75}$는 시작점일 뿐이고, renal/hepatic function과 생물학적 연령 보정이 따로 필요합니다.**

---

### Q8. 보스 딜레마 — two-species 회귀 vs 생리학적 prior

*왜 이 질문:* 보스 딜레마예요. 점추정값이랑 생리학적 prior가 충돌할 때 **무엇을 primary로 두고 무엇을 sensitivity로 보일지를 입으로 정당화**할 수 있어야 합니다. 동시에 ICH/FDA 단정문을 자발적으로 차단하는 source language discipline이 동작하는지 확인하는 자리예요.

**시나리오:** Rat와 dog 두 종만으로 log-log CL 회귀를 했더니 $b=0.62$가 나왔습니다. 문헌적 생리학적 prior $b=0.75$와 충돌합니다. FIH 노출 번역 표에는 무엇을 primary로 두겠습니까?

**정답:** 두 종 회귀의 점추정값은 leverage가 약하고 신뢰구간이 넓을 가능성이 큽니다. 그래서 **primary는 생리학적 prior $b=0.75$**로 두고, **$b=0.5, 0.62, 0.75, 1.0$ sensitivity analysis**를 함께 제시해요. 단, $b=0.75$를 특정 ICH/FDA 조항이 직접 명시한다고 쓰지는 않습니다. 본 PDF 범위에서 방어 가능한 표현은 **"mammalian metabolic rate와 functional flow variable의 알로메트릭 근거에 기반한 prior"**예요. `[확인 필요]` 규제 문구는 원문 가이드라인을 확인하기 전에는 쓰지 않습니다.

---

### Q9. [보강본] 적용 — BSA 근사식의 두 형태와 0.75 지수의 의미

*왜 이 질문:* C5 보완 callout이 입에서 나오는지 확인. R&T가 BSA 식을 두 개 함께 제시한다는 사실, 그리고 0.75 지수가 "BSA의 진짜 알로메트릭 지수"가 아니라 R&T의 편의적 매칭이라는 점을 자발적으로 분리할 수 있어야 합니다.

**질문:** R&T가 Ch.14에서 BSA를 계산하는 두 가지 식을 제시합니다. 두 식의 차이와, 0.75 지수가 어디서 온 값인지 설명하세요.

**정답:**
- **R&T Eq.14-1 (BW+Height 형):** $BSA(m^2) = 0.0243 \cdot Weight(kg)^{0.538} \cdot Height(cm)^{0.396}$ [R&T p.421]. 신장과 체중을 둘 다 쓰는 형태.
- **R&T Eq.14-2 (BW-only 근사):** $BSA(m^2) = 1.73 \cdot (Weight/70)^{0.75}$ [R&T p.421]. R&T 본문이 명시한 조건 — **"provided that body weight is close to that expected for body height"**.
- **0.75 지수의 출처:** R&T Fig.22-3(p.734)이 종간 BSA 알로메트릭 지수를 **2/3(0.67)**로 보여 줍니다. R&T 본문이 직접 — "a value for b in the order of 0.75 is more appropriate", "the experimental data often do not allow a ready distinction between values of 0.67 and 0.75" [R&T p.734]. → Eq.14-2의 0.75는 **BSA의 진짜 지수가 아니라 알로메트리 챕터의 CL/GFR prior 0.75와 매칭한 편의적 BW-only 근사**입니다.
- **실무 함의:** Eq.14-2를 "BSA 정의식"으로 외우면 신장-체중 불일치가 있는 비만·왜소 환자에서 BSA가 부정확해집니다 — 이 경우 Eq.14-1을 쓰는 것이 R&T의 직접 권고입니다.

---

### Q10. [보강본] 적용 — Maturation 모델과 LBW vs TBW

*왜 이 질문:* C5+ A와 B 카드의 임상 의사결정 트리가 입에서 나오는지 확인. 신생아·영아 용량과 비만 환자 용량 둘 다에서 backbone-only 사고가 깨지는 지점을 능동 회상합니다.

**시나리오:** 다음 두 환자에 대해 dose 보정의 기본 골격을 설명하세요.
- (a) 28주 미숙아, 출생 후 7일, BW 1.2 kg. 신장 배설 항생제(예: gentamicin) dosing.
- (b) BMI 38, BW 130 kg, height 165 cm 여성 환자. (i) digoxin (극성, 친수성), (ii) diazepam (비극성, 친지질) dosing.

**정답:**

**(a) 미숙아 — Maturation 지배:**
- 단순 $BW^{0.75}$ 알로메트리만으로는 부정확. R&T Fig.14-9 — conceptional age 28–40주에서 CL이 지수적으로 8배 증가합니다 [R&T p.420–421].
- Conceptional age 28주 + 1주 = postmenstrual age 29주. $F_{mat}$가 매우 낮은 구간.
- R&T 본문 골격: $CL = adjustment(BW) \times maturation(PMA)$. 함수형 표현은 $F_{mat} = PMA^{Hill}/(TM_{50}^{Hill}+PMA^{Hill})$ — `[교과서 외 구현]`.
- **결론:** mg/kg 그대로 적용 금지, TDM 거의 필수 [R&T p.430 본문]. 자료가 며칠 단위로 변하므로 dosing은 지속적 업데이트 필요.

**(b) 비만 여성 환자:**
- 먼저 LBW 계산: $LBW_{female} = 1.07 \cdot 130 - 148 \cdot (130/165)^2 \approx 139.1 - 91.7 \approx 47.4$ kg [R&T Eq.14-11, p.434]. (참고: 식 적용에 한계가 있을 수 있음 — R&T는 "highly muscular individuals"에는 안 맞는다고 단서 [R&T p.434].)
- **(i) Digoxin (극성):** R&T Table 14-7에서 weight-corrected V가 비만에서 **낮아짐** [R&T p.439]. R&T 직접 — "$V_u$ correlates better with lean body mass... than with total body weight" [R&T p.418]. → **LBW(약 47 kg) 기반 dose** 권고. CrCl도 LBW로 추정 [R&T p.434].
- **(ii) Diazepam (친지질):** R&T Table 14-7에서 weight-corrected V가 비만에서도 **더 큼** (2.81 vs 1.53 L/kg) [R&T p.439]. → **TBW(130 kg) 기반 dose** 적용 가능.
- **공통 원칙:** R&T 본문 — "the difference in loading dose may not be as great as anticipated from body weight alone... **much depends on the physicochemical properties of the drug**" [R&T p.418]. 약물 극성을 먼저 확인하지 않으면 친수성/친지질 약물이 한 식으로 섞입니다.

---

### Q11. [보강본] 적용 — 신장·간 청소율 알로메트릭 분기

*왜 이 질문:* C5+ C의 R&T Eq.15-7 분리식이 입에서 나오는지 확인. $fe$ 정보가 있을 때 total CL에 단일 $BW^{0.75}$를 박는 게 왜 부적절한지를 자발적으로 설명할 수 있어야 합니다.

**질문:** $fe=0.85$인 약물 A와 $fe=0.10$인 약물 B를 75세, 60 kg 환자에 dosing합니다. R&T Eq.15-7을 이용해 두 약물의 $R_d$($CL_u$ 환자/표준 비)를 계산하는 골격을 적고, 단일 $BW^{0.75}$ 보정과의 차이를 설명하세요. (가정: RF = 0.6, 표준 환자 = 60세·70kg.)

**정답:**

R&T Eq.15-7 [R&T p.453]:

$$
R_d = RF \cdot fe(t) + [1-fe(t)] \cdot \frac{(140-Age)\cdot Wt^{0.75}}{1936}
$$

연령·체중 항: $(140-75)\cdot 60^{0.75}/1936 = 65 \cdot 21.6/1936 \approx 0.726$.

- **약물 A ($fe=0.85$ — 신장 dominant):** $R_d = 0.6 \cdot 0.85 + 0.15 \cdot 0.726 = 0.510 + 0.109 = $ **약 0.62**. → RF 감소가 $R_d$를 강하게 끌어내림. **renal function이 dose의 1차 결정 인자**.
- **약물 B ($fe=0.10$ — 간 dominant):** $R_d = 0.6 \cdot 0.10 + 0.90 \cdot 0.726 = 0.060 + 0.653 = $ **약 0.71**. → 연령·체중 보정항이 $R_d$를 거의 결정. **hepatic age/weight factor가 dose의 1차 결정 인자**.

**단일 $BW^{0.75}$ 보정과의 차이:** total CL에 $BW^{0.75}$만 박으면 두 약물이 같은 인자로 보정됩니다 — 그런데 위 자료대로 신장 dominant 약물은 RF에 강하게, 간 dominant 약물은 (140-Age)에 강하게 반응해요. R&T 본문 직접 — "ideally, **renal clearance should be correlated with creatinine clearance, and the nonrenal clearance should be examined separately**" [R&T p.455].

**임상 함의:** 신부전 환자에서 약물 A의 dose는 RF 비례 감량, 약물 B는 RF에 거의 영향 없음. 단일 BW 알로메트리로 묶으면 약물 A에서 dose가 과대(toxicity 위험), 약물 B에서 dose가 과소(undertreatment) 방향으로 어긋날 수 있습니다.

---

<!-- SLIDE_START: §8 | title: 메타 프레임과 큰 그림 -->
<!-- SECTION_CORE: SC-10 -->

## §8 — 메타 프레임과 큰 그림(Meta-Frame & Big Picture)

### A. 이 세션이 시스템으로 작동하는 세 순간

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| 동물-인간 노출 번역 표 작성 | $b$, $d$, $CL_u$ | → | 첫 사람 노출 추정의 자릿수 변화 | C1–C5 spine을 한 표에 연결 |
| PopPK 체중 공변량 결정 | WT exponent | → | 좁은 WT range에서 SE 증가·점추정값 흔들림 | $b=0.75$ fixed primary + sensitivity |
| PBPK 장기 스케일링 | organ blood flow, organ volume | → | flow/extent 혼동 시 장기별 CL/V 오판 | 혈류는 rate-like, 부피는 extent-like로 분리 [R&T p.731–743] |

### B. 이 세션이 약하면 어디서 무너지는가

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| 성인 60–90 kg처럼 WT range가 좁음 | CL exponent | → | 기울기 drift, SE 증가 | fixed prior와 estimated model을 분리 |
| PK29 compound X처럼 $d>1$ | V exponent | → | Elementary Dedrick fan-out | $d$ estimate 또는 Complex Dedrick 검토 |
| 소아·노인에서 BW scaling만 사용 | functional age, renal/hepatic function | → | maturation·신기능·체조성 누락 | R&T age/weight caveat를 별도 gate로 둠 [R&T p.412–415] |
| [보강본] 신생아·영아에서 backbone만 적용 | $F_{mat}(PMA)$ | → | mg/kg toxic 가능 [R&T p.430] | maturation 곱셈 항을 명시적으로 적용, TDM |
| [보강본] 비만 환자에서 약물 극성 무시 | LBW vs TBW 선택 | → | 친수성 dose 과대, 친지질 dose 부적절 | R&T Table 14-7의 약물 극성 분기 적용 |
| [보강본] $fe$ 정보가 있는데 total CL 단일 보정 | $RF \cdot fe + (1-fe)\cdot age$ | → | 신장/간 dominant 약물 혼재 | R&T Eq.15-7 분리식으로 보정 [R&T p.453] |

### C. 전문가가 짚어 주는 해석 지점

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| $b>1$ 또는 $b<0.5$ | CL exponent | → | 기전 신호와 통계 잡음 혼재 | 종 수, leverage, 결합, 비선형성, 대사 경로 확인 |
| FIH/노출 번역 문장 작성 | Eq.2:420 | → | 최종 시작 용량 overclaim 위험 | equal-AUCu dose backbone으로만 기술 |
| Dedrick plot fan-out | $d$, 구획 비율 | → | overlay 실패를 그림 문제로 오독 | $d\ne 1$, 다구획성, 모델 잘못 지정 점검 |
| PK28/PK29 출처 불일치 | citation scope | → | 수치 무결성 손상 | `[§2.10.6 set]` 또는 `[PK28 case set]`처럼 범위 명시 |
| [보강본] BSA 식 인용 | Eq.14-1 vs Eq.14-2 선택 | → | 0.75 지수를 "BSA 진짜 지수"로 오해 | "BW-only 편의 근사" 명시, Eq.14-1 BW+Height 형 병기 |

### D. 후속 세션 연결 지식 그래프

| 후속 세션 | 이 세션에서 열리는 개념 | 이 세션 없으면 실패하는 것 |
|---|---|---|
| PopPK 체중 공변량 | flow vs extent 지수 분리 | CL/V WT exponent를 기계적으로 고정하거나 추정 |
| PBPK 장기 스케일링 | organ blood flow vs organ volume | 장기 혈류와 부피를 같은 지수로 처리 |
| FIH 노출 번역 | equal-AUCu backbone + sensitivity | Eq.2:420을 최종 시작 용량 규칙으로 오용 |
| 소아·노인 용량 | chronologic ≠ functional age | BW/BSA만으로 maturation·신기능 누락 |
| [보강본] 소아 MIPD | C5+ A maturation function | 신생아·영아에서 mg/kg 그대로 적용 위험 |
| [보강본] 비만 환자 dosing | C5+ B LBW vs TBW | 약물 극성 무시한 일률 TBW 보정 |
| [보강본] Ch.16 캡스톤 신부전 dosing | C5+ C $fe \cdot RF + (1-fe)$ age | 신장/간 dominant 약물을 같은 식으로 묶음 |

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

5. [보강본] 사람 안에서는 backbone에 3 레이어를 곱한다.
   - Maturation: F_mat(PMA) — 신생아·영아 핵심
       R&T 본문 골격, 함수형은 [교과서 외 구현]
   - Body composition: 약물 극성으로 LBW vs TBW 선택
       R&T Eq.14-10/14-11, Table 14-7
   - Organ function 분기: RF·fe + (1-fe)·(140-Age)·Wt^0.75/1936
       R&T Eq.15-7
```

**§8 마지막 한 줄.** Session 14의 핵심은 **"0.75를 외우는 것"이 아니에요.** 어떤 변수가 왜 0.75이고, 어떤 변수는 왜 1이며, 그 차이가 시간과 dose를 어떻게 바꾸는지를 **보는 것**입니다. **보강본**에서는 한 줄이 더 붙어요 — 그 backbone 위에 maturation·body composition·organ function 세 레이어를 어떻게 곱해 사람 안 dose에 도달할지를 **R&T가 직접 적은 골격으로 따라가는 것**입니다. 이 관점이 allometry를 공식 암기에서 모델링 판단으로 바꿔 줘요.

---

> 📝 **보강본 메타 노트.** 본 보강본은 검토 의견 중 Ch.14 해당 4개 항목(BSA 출처 명시 / Maturation / LBW vs TBW / 신장·간 청소율 분기)을 반영했습니다. 다른 챕터(Ch.09 QSS·membrane-bound target, Ch.10 operational model·aspirin/salicylate, Ch.11 pool/precursor·Friberg-Karlsson, Ch.12 n×τ 정정, Ch.13 OMEGA BLOCK·BLOQ·η-shrinkage, Ch.15 VPC·AIC, Ch.16 digoxin·vancomycin·MIPD·Sheiner-Tozer 등)의 보강은 본 파일에 포함되지 않습니다. 각 챕터별 보강본을 별도로 진행해 주세요. 본 파일의 모든 신규 인용은 R&T 5e Ch.14 (p.411–441), Ch.15 (p.443–490), Ch.22 (p.731–743), G&W 5e §2.10 (p.170–191), PK28/PK29 case studies의 직접 본문에서 확인 가능합니다.

---

**C-260516-085200-K7M**

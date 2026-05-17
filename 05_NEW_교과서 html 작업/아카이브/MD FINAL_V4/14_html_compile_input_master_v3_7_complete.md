# 14_HTML Compile Input Master — v3.7

<!-- 기호 통일: AUC_u prose → AUCu (수식 표기는 AUC_{u} 유지) -->
<!-- 기호 통일: Vd 일반명 → V/분포용적 표현 유지 (원문 V_{ss}는 별도 개념으로 보존) -->

## 임상 장면: 왜 이 세션이 필요한가

Phase 1 회의에서 23-g mouse의 CL을 70-kg human으로 옮길 때 $b=1$을 쓰면, $b=0.75$와 비교해 약 7.4배 다른 첫 human 노출 추정이 나온다 [G&W PK28 p.611–614]. R&T의 20-g mouse→70-kg human 예시는 3500 대 455, 즉 7.7배 차이를 보여 준다 [R&T p.733]. 이 차이는 “계산 방식이 조금 다르다”가 아니라, target AUC 기반 dose가 과대 산출될 수 있는 규제 검토 지점이다.

## 학습 항법 안내(Learner Navigation Aid)

**이 자료 활용법:** §1을 한 번 읽어 전체 뼈대를 잡은 뒤, §2 C1–C5를 순서대로 학습하고, §7에 도전하기 전에 §5로 세 가지 혼동을 먼저 차단하세요. Figure pointer는 교과서 그림을 그대로 복제하지 않습니다. Pointer가 등장하면 출처 PDF·교과서에서 명시된 figure를 직접 펼쳐 확인하시면 됩니다.

**각 C-카드는 v3.7 핵심 요약 박스로 마무리되며, 임상 상황·지배 파라미터·가장 위험한 오개념을 압축합니다.** §2는 알로메트릭 의사결정 워크스루(Allometric Decision Walkthrough)로 마무리되어 C1→C5를 하나의 작업 흐름으로 연결합니다.

**학습 경로:**

1. C1: $Y=a\cdot BW^b$가 단순 회귀선이 아닌 **스케일 법칙**임을 이해합니다.
2. C2: CL 지수와 $b=1$ 오류(fallacy)를 확실히 잡습니다.
3. C3: 흐름(flow) 지수 $b$와 분포 범위(extent) 지수 $d$를 분리하고 시간·속도 결과를 도출합니다.
4. C4: Dedrick 도표(Dedrick plot)를 지수 구조의 진단 도구로 활용합니다.
5. C5: 알로메트릭 용량(allometric dose) 외삽을 최종 임상 용량이 아니라 equal-AUCu 백본(backbone)으로 다룹니다.
6. §2 폐막 워크스루(Walkthrough): 동물 PK 데이터셋 하나를 C1→C5 흐름으로 통과시켜 전체 흐름을 잠급니다.
7. §5–§7: 출처(source) 불일치, 근거 없는 규제 언어, 지수 혼동 오류를 스스로 차단할 수 있는지 점검합니다.

**시작 전 점검:** CL, V, AUC, 반감기(half-life), 비결합 분율(unbound fraction), 일차 제거(first-order elimination)를 정의할 수 있는지 확인합니다.  
**완료 후 체크:** $0.75$와 $1.0$이 왜 호환되지 않는지, 시간이 왜 $d-b$로 스케일링되는지, 소아·노인 용량에서 왜 기능적 연령(functional age)과 장기 기능 보정이 체중 외에 추가로 필요한지 설명할 수 있어야 합니다.

<!-- SLIDE_START: §1 | title: 세션 개요와 로드맵 -->

## §1 — 세션 개요와 로드맵(Session Header & Roadmap)

**Source:** Gabrielsson & Weiner 5e §2.10 (p.170–191), Case Study PK28 (p.611–614), Case Study PK29 (p.615–620); Rowland & Tozer 5e Ch.14 (p.411–441), Ch.22 allometry section (p.731–743).

### ASCII 레이어 개념 지도

```text
Layer 1 — 무엇인가
  Allometry / CL / V / Dedrick / AUCu backbone

Layer 2 — 어떻게 계산되는가
  Y=a·BW^b → CL∝BW^b, V∝BW^d → t1/2∝BW^(d-b), kel∝BW^(b-d)

Layer 3 — 언제, 왜 중요한가
  b=1 오류 차단 → Dedrick 중첩 진단 → equal-AUCu dose backbone → 소아·노인·FIH caveat
```

### 지식 그래프 위치 — v3.7 압축

```text
[선행 세션: CL·V·AUC·반감기·비결합 분율] → [이 세션: allometric spine] → [후속 세션: PopPK WT covariate / PBPK scaling / FIH exposure table]
```

🧭 **읽는 순서:**
카드 1 (C1): $Y=a\cdot BW^b$는 왜 단순 회귀식이 아니라 scale-invariance 주장인가?  
카드 2 (C2): CL 지수 $b\approx0.75$는 언제 prior이고, 언제 의심해야 하는가?  
카드 3 (C3): V 지수 $d\approx1$과 CL 지수 차이가 왜 시간축을 만드는가?  
카드 4 (C4): Dedrick plot은 어떤 지수 가정이 버티는지 어떻게 드러내는가?  
카드 5 (C5): Equal-AUCu dose backbone을 왜 final FIH dose로 쓰면 안 되는가?

### 핵심 아이디어(Big Idea)

$Y=a\cdot BW^b$는 단순 회귀식이 아닙니다. 종간 체중 차이를 **파라미터 스케일(parameter scale)**로 번역하는 거듭제곱 언어입니다.

여기서 파라미터 스케일(parameter scale, 체중 차이를 파라미터 단위로 옮기는 척도)은 “kg 차이”를 CL, V, 용량(dose) 같은 PK 파라미터의 차이로 바꾸어 읽는 방식입니다. 핵심 오류는 $b=0.75$와 $b=1.0$의 차이를 작게 보는 것입니다. R&T의 20-g mouse→70-kg human 예시에서는 같은 값 1이 $b=1$이면 3500, $b=0.75$이면 455가 되어 7.7배 차이가 납니다 [R&T p.733]. G&W PK28의 23-g mouse→70-kg human에서는 약 7.4배, rat 250-g→human 70-kg에서는 약 4.1배 차이입니다. 이 차이는 “용량을 낮게 시작한다/높게 시작한다”라는 단순 구호가 아니라, **target AUC 기반에서는 CL 과대예측이 dose 과대 산출로 이어질 수 있다**는 dose/AUC 방향성 문제입니다.

$$
\overbrace{b=1}^{\text{kg당 선형}}\quad vs\quad \overbrace{b=0.75}^{\text{CL 흐름 prior}}
$$

> **▶ 목표 사고 모델(Target Mental Model) — [TEXTBOOK_DERIVED, ver2 V1]**  
> 이 세션을 마치는 순간, 다음 4단계가 자동으로 회상되어야 합니다.
> 1. **변수 종류부터 묻습니다** — 흐름/속도(flow/rate) 변수인가(CL, GFR, 혈류량(blood flow) → $b\approx 0.75$), 공간/분포 범위(space/extent) 변수인가(V, 혈액량(blood volume), 조직량(tissue mass) → $d\approx 1$), 시간(time) 변수인가($V/CL \rightarrow BW^{d-b}$), 속도상수(rate constant) 변수인가($CL/V \rightarrow BW^{b-d}$).
> 2. **종간 용량 번역(dose translation)은 비결합 노출(unbound exposure) 관점**으로 읽습니다. AUCu equality이면 $Dose \propto BW^b$, mg/kg 비는 $BW^{b-1}$입니다.
> 3. **예외를 먼저 찾습니다** — fu, CYP 동종효소(isoform), 비선형 PK(nonlinear PK), 수송체(transporter), 장간 순환(enterohepatic recirculation), 투여 경로·제형(route/formulation) 차이입니다.
> 4. **출처 언어(source language)를 지킵니다** — PDF에서 직접 뒷받침되는 항목(PDF-supported: G&W/R&T 수식, PK28/PK29 anchor, R&T age/renal/BSA caution)과 직접 뒷받침되지 않는 항목(not directly supported: ICH/FDA/MABEL/NONMEM/QSP 단정)을 분리합니다. 이 4단계 자체가 §8 D 최종 사고 모델(Final Mental Model)의 압축이며, §1–§8 전체가 이 4단계의 정당화 과정입니다.

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

### 지식 그래프 위치

**선행 전제:** CL, V, AUC, 반감기(half-life)의 정의; 일구획 지수 감소(one-compartment exponential decay); 혈장 단백 결합(plasma protein binding, 단백 결합으로 자유 약물 농도가 달라지는 현상)과 비결합 청소율(unbound clearance) 개념입니다.  

**직접 후속:** 소아·노인 용량 조정(pediatric/elderly dose adjustment), 모집단 약동학 체중 공변량 선택(PopPK weight covariate choice), PBPK 장기 혈류·부피 스케일링(PBPK organ blood flow/volume scaling), 최초 인체 투여 노출 번역 표(FIH exposure translation table).  
**주의:** NONMEM control stream, ICH/FDA/MABEL 언어(language), QSP 구현(implementation)은 본 PDF가 직접 다루는 내용이 아니므로, 본문에서는 `[교과서 외 구현/실무 해석]`으로만 다룹니다.

**§1 요약:** 이 세션의 중심축(spine)은 $Y=a\cdot BW^b \rightarrow CL\ b\approx0.75 \rightarrow V\ d\approx1 \rightarrow time\ d-b\approx0.25 \rightarrow Dedrick \rightarrow equal\text{-}AUCu\ dose\ backbone$입니다. 반드시 고정해야 할 교정 지점은 $4.1/7.4/7.7$ fold 기준을 분리하고, FIH dose formula를 standalone starting-dose rule이 아닌 allometric exposure backbone으로 낮추는 것입니다.

---

> 📊 **개념 도식 (HTML에서 렌더링):** 알로메트릭 중심축: 변수 유형 → 지수 → 시간/용량 결과 — $Y=a\cdot BW^b$는 독립 수식이 아니라 CL, V, 시간(time), Dedrick, equal-AUCu 용량 번역(dose translation)을 연결하는 중심축입니다.

$$
\underbrace{Y=a\cdot BW^b}_{\text{마스터식}}\rightarrow\underbrace{CL\sim BW^{0.75}}_{\text{CL 흐름}}\; /\;\underbrace{V\sim BW^1}_{\text{V 공간}}\rightarrow\underbrace{t_{1/2}\sim BW^{d-b}}_{\text{시간축}}\; /\;\underbrace{k_{el}\sim BW^{b-d}}_{\text{제거속도}}\rightarrow\underbrace{Dose\sim BW^b}_{\text{AUCu 용량}}
$$

<!-- SLIDE_START: §2 | title: 개념 해부 카드 -->

## §2 — 개념 해부 카드(Concept Anatomy Cards)

---

<!-- SLIDE_START: C1 | title: 마스터 알로메트릭 방정식 -->

### ━━ C1. 마스터 알로메트릭 방정식(Master Allometric Equation): $Y=a\cdot BW^b$ ━━

> **거장의 시각**
> $Y=a\cdot BW^b$를 회귀식으로만 읽으면 기울기 점추정값에 과신하고, 종 수·기전·결합 차이가 만든 실패 신호를 놓칩니다.
> 이 식을 scale-invariance 주장으로 보면 C2–C5의 모든 판단이 “이 약물에서 이 지수 prior가 유지되는가?”라는 하나의 질문으로 정렬됩니다.

#### A. 정형 정의(Formal Definition)

$$Y=a\cdot BW^b \quad [G\&W\ Eq.2:374,\ p.173;\ R\&T\ Eq.22\text{-}2,\ p.732]$$

$$
\underbrace{Y}_{\text{대상 변수}}=\underbrace{a}_{\text{절편}}\cdot \underbrace{BW}_{\text{체중}}^{\overbrace{b}^{\text{지수}}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $Y$ | 변수별 상이 | 스케일링 대상 PK/생리 변수 | CL, V, dose 등 선택 변수 |
| $a$ | $Y/BW^b$ | 화합물·변수 의존 절편 | 약물 특성, 단위, 기준 체중 |
| $BW$ | kg 또는 g | 체중 기반 크기 척도 | 종, 연령, 체조성 |
| $b$ | 무차원 | 체중 변화에 대한 지수 | 변수 유형, 자료 품질, 결합·기전 차이 |

💡 **Scale-invariance 직관** — 로그-로그 직선은 단순 회귀선이 아니라 “체중 배율이 바뀌어도 같은 법칙이 유지된다”는 주장입니다.
⚠️ **헷갈림 방지:** $b$는 자연상수가 아니라 변수 유형과 자료가 함께 만드는 prior입니다.
🔑 **첫 질문 규칙:** 회귀선을 보기 전에 먼저 이 변수가 flow인지, extent인지, time인지 묻습니다.

양변 로그 변환:

$$\ln(Y)=\ln(a)+b\cdot\ln(BW) \quad [G\&W\ Eq.2:379,\ p.176;\ R\&T\ Eq.22\text{-}1,\ p.732]$$

$$
\underbrace{\ln(Y)}_{\text{로그 }Y}=\underbrace{\ln(a)}_{\text{로그 절편}}+\overbrace{\underbrace{b}_{\text{기울기}}\cdot\underbrace{\ln(BW)}_{\text{로그 }BW}}^{\text{log-log 체중효과}}
$$

- **$a$:** 약물 의존적(drug-dependent) 또는 화합물 의존적(compound-dependent) 절편(intercept)입니다. 단위는 $b$에 의존합니다.
- **$b$:** 대체로 변수 유형에 의존하는(variable type-dependent) 지수입니다. 다만 실제 CL 지수(exponent)는 자료 품질, 종 수, 비선형성, 종간 단백 결합(protein binding) 차이 등에 따라 변동할 수 있습니다 [G&W p.177–178].

#### B. 도출(Derivation) — 왜 거듭제곱 함수인가

G&W는 대사율(metabolic rate)이 $BW^{0.75}$로 스케일링하고, 에너지 함량(energy content)이 대략 $BW^1$에 비례하므로 순환 시간(turnover time, 에너지 순환 주기)이 $BW^{0.25}$로 나온다고 제시합니다 [G&W Eq.2:375–377, p.173]. 즉 알로메트리는 “체중이 커질수록 절대 처리량은 증가하지만, 단위 체중당 처리 효율은 감소한다”는 생리학적 압축입니다.

표면적·부피 직관도 같은 방향을 줍니다. 기하학적으로 표면적(surface)은 길이의 제곱(length²), 부피(volume)는 길이의 세제곱(length³)이므로 표면적은 부피의 $2/3$승에 비례합니다. 그러나 실제 생리학 변수는 단순 외부 표면적보다 더 복잡해, Brody의 경험적 지수는 0.5–0.8 범위로 나타납니다 [G&W p.173–174].

#### C. 구조적 의미(Structural Meaning)

로그-로그(log-log) 직선은 단순히 “회귀가 잘 맞는다”는 뜻이 아닙니다.

> 💼 **실무 인사이트:** 체중 배율이 달라져도 같은 지수 법칙이 유지되는 척도 불변(scale-invariant) 구조를 가정한다는 뜻입니다. 이 가정이 깨지는 순간이 알로메트리 실패(allometry failure)의 시작입니다.

#### D. 경계 조건(Boundary Conditions)

G&W는 알로메트리(allometry)가 물리적 수송 과정(physical transport processes)에 지배되는 변수에서, 그리고 약물 분포가 혈장 단백 결합(plasma protein binding)에 크게 좌우되지 않는 물질에서 특히 유용하다고 설명합니다. 반대로 종간 대사·배설(metabolism/excretion)의 질적 차이, CYP450 동종효소(isozyme) 구성 차이, 혈장 단백 결합 차이가 크면 알로메트리는 실패할 수 있습니다 [G&W p.173].

#### E. 제텔카스텐 원자(Zettelkasten Atom)

```yaml
aliases: [allometric law, allometric power function, Y=a·BW^b]
tags: [pharmacometrics/allometry, scaling/inter-species]
source: "G&W §2.10.3 p.173–176; R&T Ch.22 p.731–733"
```

---

> **C1 체화 핵심**
> ① `종간 PK 차이를 한 식으로 압축할 때` → $Y=a\cdot BW^b$가 scale-invariance 주장을 결정
> ② `기울기 점추정값 vs 생리학적 prior` → 자료 품질·종 수·기전 차이가 해석을 지배
> ⚡ `b를 자연상수처럼 고정` → 실패 신호를 회귀 오차로 오독 → C2–C5 추론 붕괴

<!-- SLIDE_START: C2 | title: 청소율 지수 -->

### ━━ C2. [⚡ Apex Concept] 청소율 지수(Clearance Exponent) $b\approx0.75$ ━━

> **앞 카드에서 이 카드로:** C1에서 $b$가 scale-invariance prior임을 잡았으므로, 이제 가장 위험한 변수인 CL에서 그 prior가 어떤 임상 격차를 만드는지 확인해야 합니다.

> **거장의 시각**
> 💢 **흔한 오해:** mg/kg 처방에 익숙하니 CL도 체중에 선형 비례하거나, 반대로 $b=0.75$를 모든 약물의 법칙처럼 쓰면 된다고 생각합니다.
> ✅ **실제는:** CL은 기능적 흐름 변수라 $b\approx0.75$가 출발 prior이지만, G&W는 실제 CL 지수가 0.2에서 $>1$까지 변할 수 있다고 경고합니다 [G&W p.178].
> 🎯 **체화할 단 하나의 직관:** “flow는 0.75로 시작하되, fu·수송체·포화·종간 대사 차이가 보이면 즉시 sensitivity로 격하한다.”

#### A. 정형 정의(Formal Definition)

$$CL_i=a\cdot BW_i^b \quad [G\&W\ Eq.2:380,\ p.176;\ PK28\ Eq.28:1,\ p.611]$$

$$
\underbrace{CL_i}_{\text{개체 CL}}=\underbrace{a}_{\text{CL 절편}}\cdot\underbrace{BW_i}_{\text{개체 BW}}^{\overbrace{b}^{\text{CL 지수}}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $CL_i$ | volume/time | 개체별 청소율, 단위 시간당 처리 흐름 | 혈류, GFR, 대사능, 수송체 |
| $a$ | CL/$BW^b$ | CL allometry 절편 | 화합물 특성, 종간 자료 범위 |
| $BW_i$ | kg 또는 g | 개체 체중 | 종, 연령, 체조성 |
| $b$ | 무차원 | CL 체중 지수 | ↑ 수송체/대사 차이, ↓ 결합·자료 leverage 부족 |

💡 **흐름 변수 핵심** — CL은 “몸 안 공간의 크기”가 아니라 “시간당 얼마나 처리되는가”입니다.
⚠️ **헷갈림 방지:** $b=0.75$도 법칙이 아니라 prior입니다. G&W는 실제 CL 지수가 0.2에서 $>1$까지 변할 수 있다고 경고합니다 [G&W p.178].
🔑 **FIH 방어 규칙:** primary 지수와 sensitivity 지수를 같은 표에 두어야 dose narrative가 방어됩니다.

G&W는 CL/대사율(metabolic rate)의 대표 지수(exponent)를 0.75로 제시하지만, 실제 CL 지수는 약 0.2에서 $>1$까지 변할 수 있다고 경고합니다 [G&W p.178]. Fig.2.159는 91개 화합물의 CL 지수 분포가 주로 0.5–1.0 범위에 놓임을 보여 줍니다 [G&W p.191].

#### B. 그럴듯한 오해(Plausible Fallacy) — $b=1$ 선형 kg당(per-kg) 스케일링

**오류:** “mg/kg 처방에 익숙하니 청소율(clearance)도 kg에 선형 비례한다”라고 생각하기 쉽습니다. 이것이 선형 kg당 스케일링(linear per-kg scaling, kg당 값이 일정하다는 가정) 오류입니다.  

**교정:** CL은 흐름·속도 변수(rate/flow variable)이므로 $b\approx0.75$가 생리학적 prior(physiological prior)입니다.

- **R&T 20-g mouse→70-kg human:** $b=1$이면 3500, $b=0.75$이면 455 → 7.7배 차이 [R&T p.733].
- **G&W PK28 23-g mouse→70-kg human:** $(70/0.023)^{0.25}\approx7.4$배 차이.
- **Rat 250-g→70-kg human:** $(70/0.25)^{0.25}\approx4.1$배 차이.

$$
\underbrace{\left(\frac{BW_{human}}{BW_{animal}}\right)^{1-0.75}}_{\text{b=1 vs 0.75 격차}}=\underbrace{\left(\frac{BW_{human}}{BW_{animal}}\right)^{0.25}}_{\text{species 격차}}
$$

Target AUC 용량(dose) 계산에서는 CL 과대예측이 목표 AUC를 맞추기 위한 dose 과대 산출로 이어질 수 있습니다. 따라서 “CL 과대평가 → subtherapeutic 시작”이라는 단정은 사용하지 않습니다.

#### C. 실패 조건(Failure Conditions)

알로메트리 실패(allometry failure)는 단순한 무작위 오차(random error)가 아니라 **메커니즘 신호(mechanism signal)**일 수 있습니다. G&W Fig.2.145는 스케일링 가능한 화합물(scalable compound)에서는 70-kg human CL 예측구간(prediction interval)이 약 10-fold 범위이지만, 스케일링이 어려운 화합물(less scalable compound)에서는 약 1000-fold 범위까지 넓어질 수 있음을 보여 줍니다 [G&W p.174].

주요 실패 트리거(failure trigger)는 다음과 같습니다:

1. 종간 혈장 단백 결합(species-dependent plasma protein binding) 차이;
2. 대사 경로 또는 CYP isozyme 조성(different metabolic routes or CYP isozyme composition) 차이;
3. 비선형 미카엘리스-멘텐 거동(nonlinear Michaelis-Menten behavior);
4. 장간 순환(enterohepatic recirculation);
5. 투여 경로·제형(route/formulation) 차이;
6. 중심·말초 분포용적 비율 변동(variable central/peripheral volume ratio) [G&W p.191].

> 
> **[TRENCH — 비결합 청소율 스케일링(unbound clearance scaling)]** 종간 fu 차이가 크면 total CL이 아니라 $CL_u=CL/f_u$를 스케일링합니다. G&W Eq.2:421은 $CL_{u,man}=CL_{u,rat}\cdot(BW_{man}/BW_{rat})^b$ 형태로 제시되며 [G&W p.190], R&T Table 22-1은 cefazolin 등에서 human-animal plasma protein binding 차이가 크게 나타날 수 있음을 보여 줍니다 [R&T p.740]. > 💼 **실무 인사이트:** fu 비교는 가능하면 동일 농도, buffer, 온도, assay method에서 측정된 값끼리 해야 합니다.

#### D. 전문가 진단 트리거(Expert Diagnostic Trigger)

> 💼 **실무 인사이트:** > 💼 **실무 인사이트:** PopPK 또는 종간 회귀에서 추정된 $b>1$이 나오면 “추정값을 그대로 믿을 것인가?”가 아니라 “종간 단백 결합(binding), 수송체(transporter), 포화(saturation), 자료 품질(data quality) 중 무엇이 기울기(slope)를 밀어 올렸는가?”를 먼저 물어야 합니다. 반대로 두 종만으로 얻은 $b<0.5$는 생리학적 신호보다 통계적 지렛대 부족(statistical leverage failure)일 가능성이 큽니다.

#### E. 제텔카스텐 원자(Zettelkasten Atom)

```yaml
aliases: [clearance allometric exponent, b_CL, Brody-Kleiber clearance scaling]
tags: [pharmacometrics/allometry, clearance, FIH/exposure-translation]
source: "G&W §2.10.3 p.176–180; G&W Fig.2.159 p.191; R&T Ch.22 p.732–735"
```

CL의 $b\approx0.75$는 시간당 처리량의 지수입니다. 그럼 V는 왜 $d\approx1$일까요? 답은 V가 “흐름”이 아니라 “공간”이기 때문입니다.

> 📖 **교과서 그림 참조:** Rowland & Tozer 5e, Ch.22, p.733, Fig.22-2
> 이 그림은 $b=1$과 $b=0.75$ 오류를 보여 주는 가장 명확한 원출처 시각 자료입니다. 7.7배의 mouse-human 격차를 계산으로만 이해하는 것이 아니라 눈으로 확인하게 해 줍니다.
> 확인 시점: C2의 그럴듯한 오해(Plausible Fallacy)를 읽은 뒤, C2 실패 조건(Failure Conditions)으로 넘어가기 전에 확인하시면 됩니다.

> 📖 **교과서 그림 참조:** Gabrielsson & Weiner 5e, §2.10.3, p.174, Fig.2.145
> 이 그림은 allometry가 유용한 예측을 제공하는 화합물과 예측구간이 위험하게 넓어지는 화합물을 분리해서 보여 줍니다. 이는 실패가 단순 잡음이 아니라 기전/자료 품질 신호(mechanism/data-quality signal)일 수 있다는 C2의 메시지를 직접 뒷받침합니다.
> 확인 시점: C2 실패 조건(Failure Conditions)을 읽은 뒤 확인하시면 됩니다.

---

**Plausible Fallacy — C2 Apex**

**오류:** $b=1$ mg/kg 선형 scaling 또는 $b=0.75$ 고정 prior 하나로 human CL/dose 문제가 해결된다고 판단한다.  
**왜 그럴싸한가:** 저용량·소수 종 자료에서는 log-log 직선이 그럴듯하게 보이고, R&T/G&W 모두 $0.75$ prior의 생리학적 근거를 제시하기 때문이다.  
**나비효과:** 지수 선택 오류 → human CL 4.1/7.4/7.7배 격차 → [임상] target AUC 기반 dose 과대/과소 산출 및 독성·치료 실패 위험 → [모델링/규제] NONMEM/종간 회귀 지수 정당화 요구, sensitivity analysis 재제출, Deficiency Letter성 질의 가능.

> **C2 체화 핵심**
> ① `target AUC 기반 human CL/dose 예측` → CL 지수 $b\approx0.75$가 첫 노출 추정을 결정
> ② `mg/kg 선형 사고 vs b=0.75 과신` → 전자는 CL/dose 과대, 후자는 기전 예외 누락이 지배
> ⚡ `0.75를 법칙처럼 적용` → fu·수송체·포화·대사 차이 누락 → Phase 1 노출 오판 및 지수 정당화 요구

<!-- SLIDE_START: C3 | title: 분포용적 지수 -->

### ━━ C3. 분포용적 지수(Volume Exponent) $d\approx1.0$ ━━

> **앞 카드에서 이 카드로:** C2가 CL을 시간당 흐름으로 고정했으므로, 이제 V를 공간 변수로 분리해야 반감기와 제거속도 부호가 닫힙니다.

> **거장의 시각**
> V를 CL처럼 흐름 변수로 읽으면 $t_{1/2}$와 $k_{el}$의 지수 부호가 동시에 뒤집힙니다.
> V를 분포 공간으로 보면 $d\approx1$과 $b\approx0.75$의 차이 $d-b$가 시간축 전체를 만든다는 점이 즉시 보입니다.

#### A. 정형 정의(Formal Definition)

$$V_i=c\cdot BW_i^d \quad [G\&W\ Eq.2:382,\ p.179;\ PK28\ Eq.28:2,\ p.611]$$

$$
\underbrace{V_i}_{\text{개체 }V}=\underbrace{c}_{\text{V 절편}}\cdot\underbrace{BW_i}_{\text{개체 BW}}^{\overbrace{d}^{\text{V 지수}}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $V_i$ | volume | 개체별 분포용적 | 체수분, 조직량, 지방 분포, 결합 |
| $c$ | V/$BW^d$ | V allometry 절편 | 조직 친화성, 화합물 특성 |
| $BW_i$ | kg 또는 g | 개체 체중 | 종, 연령, 체조성 |
| $d$ | 무차원 | V 체중 지수 | 조직 친화성, 지방 분포, 수송체, 단백 결합 |

💡 **공간 변수 핵심** — V는 처리 능력이 아니라 약물이 퍼질 수 있는 공간의 크기입니다.
⚠️ **헷갈림 방지:** CL의 $b$와 V의 $d$를 바꾸면 half-life와 rate constant 부호가 동시에 틀어집니다.
🔑 **시간축 규칙:** 시간은 $V/CL$이므로 $d-b$가 지배합니다.

G&W Table 2.22는 혈액량 지수(blood volume exponent) 0.99, 골격근량(skeletal mass) 1.09, Vd 약 1.0을 제시합니다 [G&W p.180].

#### B. 결과(Consequence) — 반감기(half-life)와 속도상수(rate constant)

$$t_{1/2}=\ln2\cdot\frac{V}{CL}=\ln2\cdot\frac{c\cdot BW^d}{a\cdot BW^b}\propto BW^{d-b}$$

$$
\underbrace{t_{1/2}}_{\text{반감기}}=\underbrace{\ln2}_{\text{반감 상수}}\cdot\frac{\overbrace{V}^{\text{공간}}}{\overbrace{CL}^{\text{흐름}}}=\ln2\cdot\frac{\underbrace{c\cdot BW^d}_{\text{V 스케일}}}{\underbrace{a\cdot BW^b}_{\text{CL 스케일}}}\propto \underbrace{BW^{d-b}}_{\text{시간지수}}
$$

$d\approx1$, $b\approx0.75$이면 다음과 같습니다:

$$t_{1/2}\propto BW^{0.25},\qquad k_{el}=\frac{CL}{V}\propto BW^{b-d}\approx BW^{-0.25}$$

$$
\underbrace{t_{1/2}}_{\text{반감기}}\propto \underbrace{BW^{0.25}}_{\text{큰 종↑}},\qquad \underbrace{k_{el}}_{\text{제거속도}}=\frac{\overbrace{CL}^{\text{흐름}}}{\overbrace{V}^{\text{공간}}}\propto\underbrace{BW^{b-d}}_{\text{큰 종↓}}\approx BW^{-0.25}
$$

학습자는 “$t_{1/2}\propto BW^{0.25}$”를 암기하는 데 그치기 쉽습니다. 그러나 더 중요한 것은 **큰 동물일수록 모든 일차 속도상수(first-order rate constant)가 작아진다**는 사실입니다. 같은 분수 $V/CL$을 시간으로 읽으면 반감기(half-life)이고, 뒤집어 $CL/V$로 읽으면 속도상수(rate constant)입니다. 다시 말해, 큰 동물은 절대 CL이 크지만 단위 시간당 제거되는 분율(fraction)은 작습니다.

#### C. 데이터 앵커(Data Anchor) — Methadone PK28

G&W PK28 methadone 앵커는 다음과 같습니다:

| 종(Species) | BW | Dose | 비고(Note) |
|---|---:|---:|---|
| Mouse | 23 g | 25 µg IV bolus | 기본 Dedrick 앵커(elementary Dedrick anchor) |
| Rat | 250 g | 500 µg IV bolus | 출처 내부 $t_{1/2}$ 불일치(source-internal discrepancy) 있음 |
| Man | 70 kg | 100,000 µg IV bolus | human 앵커 |

- $a=0.319$, $AUC=1/a=3.13$ [G&W §2.10.6 p.186; PK28 p.613].
- 간 추출률(hepatic extraction) <10% [G&W p.186; PK28 p.613].
- **$t_{1/2}$ 불일치(discrepancy):** G&W §2.10.6 본문은 1.5/2.9/35 h, PK28 case는 1.5/3.9/35 h로 rat 값이 다릅니다. 본문 인용 시 `[§2.10.6 set]` 또는 `[PK28 case set]`을 명시합니다.

#### D. 한계(Limitations)

V 지수는 대체로 1에 가깝지만, $V_{ss}$는 조직 친화성(tissue affinity), 지방 분포(fat distribution), 수송체(transporter), 단백 결합(protein binding)에 따라 0.8–1.2 범위로 흔들릴 수 있습니다. R&T Ch.14의 비만(obesity) 예시도 “체중(body weight)이 항상 생물학적으로 관련된 분포용적(biologically relevant volume)은 아니다”라는 경고로 읽어야 합니다 [R&T p.439].

> 📊 **개념 도식 (HTML에서 렌더링):** 흐름과 분포 범위의 분리: 왜 $b$와 $d$를 바꾸어 쓰면 안 되는가 — CL은 흐름(flow)이므로 $b\approx0.75$, V는 분포 범위(extent)이므로 $d\approx1$이며, 두 지수의 차이가 시간(time)과 속도상수(rate constant)를 반대 방향으로 만듭니다.

$$
\underbrace{CL=a\cdot BW^b}_{\text{CL 흐름}}\quad vs\quad\underbrace{V=c\cdot BW^d}_{\text{V 공간}}\quad\Rightarrow\quad\underbrace{t_{1/2}\propto BW^{d-b}}_{\text{시간↑}}\; ,\;\underbrace{k_{el}\propto BW^{b-d}}_{\text{fraction 속도↓}}
$$

---

> **C3 체화 핵심**
> ① `큰 동물에서 half-life가 길어지는 이유` → $d-b\approx0.25$가 결정
> ② `절대 CL 증가 vs 제거 분율 감소` → $CL/V$의 $b-d\approx-0.25$가 지배
> ⚡ `$t_{1/2}$만 암기` → $k_{el}$ 부호를 놓침 → CL/V 해석과 시간축 정규화 실패

<!-- SLIDE_START: C4 | title: Dedrick 중첩 -->

### ━━ C4. Dedrick 중첩(Dedrick Superposition): 기본형(Elementary) + 복합형(Complex) ━━

> **앞 카드에서 이 카드로:** C2와 C3에서 얻은 $b$와 $d$는 숫자로 끝나지 않고, 실제 종간 PK 곡선이 한 축 위에 겹치는지 검증하는 Dedrick 변환으로 넘어갑니다.

> **거장의 시각**
> Dedrick plot을 예쁜 overlay 그림으로만 읽으면 fan-out을 그래픽 실패로 오해합니다.
> 이를 지수 구조의 진단 도구로 보면 $d=1$ 가정, 다구획성, model misspecification 중 무엇이 곡선 중첩을 깨뜨렸는지 추적할 수 있습니다.

#### A. 정형 정의(Formal Definitions)

**기본 Dedrick 도표(Elementary Dedrick plot)** — $d=1$ 가정:

$$y=\frac{C}{Dose/BW},\qquad x=\frac{t}{BW^{1-b}}$$

$$
\underbrace{y}_{\text{농도축}}=\frac{\overbrace{C}^{\text{농도}}}{\underbrace{Dose/BW}_{\text{kg당 용량}}},\qquad \underbrace{x}_{\text{시간축}}=\frac{\overbrace{t}^{\text{시간}}}{\underbrace{BW^{1-b}}_{\text{elementary 시간}}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $y$ | dose-normalized concentration | 종간 농도축 정규화 | dose, BW, V 지수 가정 |
| $x$ | normalized time | 종간 시간축 정규화 | $b$, $d$, 체중 범위 |
| $b$ | 무차원 | CL/flow 지수 | 대사·혈류·GFR prior 및 예외 |
| $d$ | 무차원 | V/extent 지수 | $d=1$ 여부가 elementary/complex를 가름 |

💡 **비유:** Dedrick plot은 서로 다른 속도로 재생되는 영상을 같은 프레임 속도에 맞춰 겹쳐 보는 작업입니다. 시간이 어긋나면 배우가 다른 것이 아니라 프레임 보정이 틀린 것일 수 있습니다.
⚠️ **헷갈림 방지:** Elementary는 $d=1$을 숨은 가정으로 갖습니다. PK29처럼 $d
eq1$이면 Complex로 넘어가야 합니다.
🔑 **Switch 규칙:** log-log V vs BW slope가 0.9–1.1 밖이면 Complex Dedrick을 검토합니다.

**복합 Dedrick 도표(Complex Dedrick plot)** — $d\neq1$ 일반형:

$$y=\frac{C}{Dose/BW^d}=\frac{C\cdot BW^d}{Dose},\qquad x=\frac{t}{BW^{d-b}}$$

$$
\underbrace{y}_{\text{농도축}}=\frac{\overbrace{C}^{\text{농도}}}{\underbrace{Dose/BW^d}_{\text{V지수 용량}}}=\frac{\overbrace{C}^{\text{농도}}\cdot\overbrace{BW^d}^{\text{공간 보정}}}{\underbrace{Dose}_{\text{투여량}}},\qquad \underbrace{x}_{\text{시간축}}=\frac{\overbrace{t}^{\text{시간}}}{\underbrace{BW^{d-b}}_{\text{complex 시간}}}
$$

Kallynochron은 $d=1$ 가정 하의 kg당 시간 척도(per-kg time scale)이고, Apolysichron은 $d$를 명시적으로 반영한 일반화 생리학적 시간 척도(generalized physiological time scale)입니다 [G&W §2.10.6–2.10.7, p.184–189].

#### B. 도출(Derivation)

단일 지수 모델(mono-exponential model):

$$C=\frac{D_{iv}}{V}\cdot e^{-(CL/V)t}$$

$$
\underbrace{C}_{\text{농도}}=\frac{\underbrace{D_{iv}}_{\text{IV dose}}}{\underbrace{V}_{\text{V 공간}}}\cdot \overbrace{e^{-(CL/V)t}}^{\text{일차 제거}}
$$

알로메트릭 치환(allometric substitution):

$$C=\frac{D_{iv}}{c\cdot BW^d}\cdot e^{-(a/c)\cdot BW^{b-d}\cdot t} \quad [G\&W\ Eq.2:384,\ p.179]$$

$$
\underbrace{C}_{\text{농도}}=\frac{\underbrace{D_{iv}}_{\text{Dose}}}{\underbrace{c\cdot BW^d}_{\text{V 스케일}}}\cdot \overbrace{e^{-\left(\underbrace{a/c}_{\text{CL/V 절편}}\right)\cdot\underbrace{BW^{b-d}}_{\text{k 체중지수}}\cdot \underbrace{t}_{\text{시간}}}}^{\text{체중 보정 제거}}
$$

따라서 농도(concentration)는 $Dose/BW^d$로, 시간(time)은 $BW^{d-b}$로 정규화되어야 합니다. > 💼 **실무 인사이트:**으로 말하면, 이는 Buckingham π 정리(Buckingham π theorem)류의 차원 해석(dimensional analysis)과 같은 직관입니다. 변수들이 가진 질량·시간·부피(mass/time/volume) 차원을 제거하면 독립적인 무차원 그룹(dimensionless group)이 남고, Dedrick 변환은 그 그룹의 PK 버전입니다.

#### C. AUC 관계식(AUC relation)

기본 Dedrick(Elementary Dedrick) 맥락에서 G&W는 AUC가 $1/a$로 정리됨을 보입니다 [G&W Eq.2:386, p.179]. 이것은 C5의 'equal unbound AUC' 조건과 무관한 별개의 사실이 아니라, 같은 논리가 수식으로 먼저 나타나는 전단계입니다.

#### D. 데이터 앵커(Data Anchor) — PK28과 PK29

**PK28 Methadone**: mouse/rat/man IV bolus 자료를 기본 Dedrick 도표(elementary Dedrick plot)로 중첩합니다 [G&W p.184–186; PK28 p.611–614]. 단, case는 단일 dose level이며 G&W도 ≥2 dose levels, 다회 투여·항정상태(multiple dosing/steady state), 모델 잘못 지정(model misspecification) 배제가 필요하다고 경고합니다 [PK28 p.614].

**PK29 Compound X**: mouse 20 g, rat 250 g, monkey 3.5 kg, dog 14 kg, man 70 kg의 5종 자료를 사용합니다 [G&W p.186–189; PK29 p.615–620].

- G&W §2.10.7 parameter set: $a=0.021$, $b=0.74$, $c=0.076$, $d=1.18$, $e=0.56$, $g=0.075$ [G&W p.189].
- PK29 case set: $a=0.021$, $b=0.75$, $c=0.10$, $d=1.21$, $e=0.54$, $g=0.071$ [PK29 p.619].
- 체중 범위(weight range): 산술적으로 $70/0.020=3500$-fold; PK29 case 본문은 약 3000-fold로 표기할 수 있습니다. 본문에서는 “약 3000–3500-fold”로 표기합니다.

> 
> **[TRENCH — 기본형 vs 복합형 Dedrick 전환(Elementary vs Complex Dedrick switch)]** log-log $V$ vs $BW$ slope가 0.9–1.1 밖이면 기본 Dedrick(Elementary, $d=1$ 가정)을 고집하지 않습니다. PK29처럼 $d\approx1.18$이면 $C/(Dose/BW^d)$와 $t/BW^{d-b}$를 쓰는 복합 Dedrick(Complex Dedrick)으로 전환합니다.

> 📖 **교과서 그림 참조:** Gabrielsson & Weiner 5e, Case Study PK28, p.613, Fig.28.2
> 이 그림은 methadone의 기본 Dedrick 중첩(elementary Dedrick superposition)을 학습자 관점에서 가장 잘 보여 줍니다. 정규화가 mouse, rat, human의 concentration-time curve를 공통 생리학적 시간 척도 위로 접어 넣기 위한 것임을 확인할 수 있습니다.
> 확인 시점: C4 데이터 앵커(Data Anchor) — PK28을 읽은 뒤, C4 한계(limitations)를 읽기 전에 확인하시면 됩니다.

> 📖 **교과서 그림 참조:** Gabrielsson & Weiner 5e, Case Study PK29, p.619, Fig.29.3
> 이 그림은 $d\neq1$이고 multicompartment scaling이 들어올 때 왜 Complex Dedrick이 필요한지를 보여 주는 최종 시각 증거입니다. allometric parameter set이 곡선 중첩(curve superposition)과 어떻게 연결되는지 보여 줍니다.
> 확인 시점: F5 이후, 그리고 C4 Complex Dedrick / PK29 자료를 읽은 뒤 확인하시면 됩니다.

---

> **C4 체화 핵심**
> ① `PK28처럼 d≈1인 곡선 중첩` → Elementary Dedrick이 결정
> ② `PK29처럼 d≈1.18–1.21인 약물` → Complex Dedrick이 지배
> ⚡ `overlay가 안 예쁘면 그림 문제` → fan-out의 기전 신호를 누락 → model misspecification 또는 d 추정 실패

<!-- SLIDE_START: C5 | title: FIH 용량 번역 -->

### ━━ C5. FIH 용량 번역(FIH Dose Translation)의 알로메트릭 백본(Allometric Backbone) ━━

> **앞 카드에서 이 카드로:** C4에서 지수 구조가 곡선 수준에서 버티는지 확인했으므로, 마지막으로 그 구조가 dose/exposure backbone으로 어떻게 번역되는지 봐야 합니다.

> **거장의 시각**
> Equal-AUCu 식을 final FIH starting-dose 공식처럼 쓰면 안전성 margin, PD metric, route/formulation, functional age가 모두 누락됩니다.
> 이 식을 exposure backbone으로 낮춰 읽으면 수식은 보존하면서도 IND/NDA 문서에서 방어 가능한 caveat 구조를 만들 수 있습니다.

#### A. Equal-unbound-AUC 백본(backbone)

$$AUC_{u,rat}=AUC_{u,man}=\frac{Dose_{rat}}{CL_{u,rat}}=\frac{Dose_{man}}{CL_{u,man}} \quad [G\&W\ Eq.2:417,\ p.190]$$

$$
\underbrace{AUC_{u,rat}}_{\text{rat }AUC_u}=\underbrace{AUC_{u,man}}_{\text{human }AUC_u}=\frac{\overbrace{Dose_{rat}}^{\text{rat dose}}}{\underbrace{CL_{u,rat}}_{\text{rat }CL_u}}=\frac{\overbrace{Dose_{man}}^{\text{human dose}}}{\underbrace{CL_{u,man}}_{\text{human }CL_u}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $AUC_u$ | concentration×time | 비결합 노출 | dose, $CL_u$, fu, 선형성 |
| $Dose$ | mass | 투여량 | 종, 안전역, route/formulation |
| $CL_u$ | volume/time | 비결합 청소율 | fu 보정, 대사·배설 기전 |
| $b$ | 무차원 | dose backbone에 들어가는 CL 지수 | flow prior, 기전 예외, sensitivity 선택 |

💡 **비유:** C5 식은 완성된 처방전이 아니라 다리의 철골입니다. 철골 위에 안전 난간, 하중 제한, 통행 규칙을 붙여야 실제 환자에게 건널 수 있습니다.
⚠️ **헷갈림 방지:** Equal-AUCu는 같은 PD나 같은 전체 곡선 모양을 보장하지 않습니다 [G&W p.190].
🔑 **Backbone 규칙:** Eq.2:420은 final FIH dose가 아니라 exposure translation backbone입니다.

$$Dose_{man}=Dose_{rat}\cdot\left(\frac{BW_{man}}{BW_{rat}}\right)^b \quad [G\&W\ Eq.2:420,\ p.190]$$

$$
\underbrace{Dose_{man}}_{\text{human dose}}=\underbrace{Dose_{rat}}_{\text{rat dose}}\cdot\left(\frac{\overbrace{BW_{man}}^{\text{human BW}}}{\overbrace{BW_{rat}}^{\text{rat BW}}}\right)^{\overbrace{b}^{\text{CL/AUC 지수}}}
$$

$$CL_{u,man}=CL_{u,rat}\cdot\left(\frac{BW_{man}}{BW_{rat}}\right)^b \quad [G\&W\ Eq.2:421,\ p.190]$$

$$
\underbrace{CL_{u,man}}_{\text{human }CL_u}=\underbrace{CL_{u,rat}}_{\text{rat }CL_u}\cdot\left(\frac{\overbrace{BW_{man}}^{\text{human BW}}}{\overbrace{BW_{rat}}^{\text{rat BW}}}\right)^{\overbrace{b}^{\text{CLu 지수}}}
$$

mg/kg dose 비(ratio)로 쓰면 다음과 같습니다:

$$\frac{Dose_{man}/BW_{man}}{Dose_{rat}/BW_{rat}}=\left(\frac{BW_{man}}{BW_{rat}}\right)^{b-1}$$

$$
\underbrace{\frac{Dose_{man}/BW_{man}}{Dose_{rat}/BW_{rat}}}_{\text{mg/kg 비}}=\left(\frac{\overbrace{BW_{man}}^{\text{큰 종 BW}}}{\overbrace{BW_{rat}}^{\text{작은 종 BW}}}\right)^{\overbrace{b-1}^{\text{kg당 지수}}}
$$

$b<1$이면 큰 동물의 mg/kg dose는 작은 동물보다 낮아집니다.

#### B. 가정(Assumptions)

1. 비결합 AUC(unbound AUC)가 약리 효과(pharmacologic effect)와 연결됩니다;
2. 표적 친화도(target affinity)와 관련 약리학(relevant pharmacology)이 종간 크게 다르지 않습니다;
3. PK가 선형 구간(linear range)에 있습니다;
4. fu(비결합 분율, unbound fraction) 차이가 있으면 $CL_u$로 보정합니다;
5. AUC가 적절한 노출 지표(exposure metric)입니다. 최고농도 기반 독성(Cmax-driven toxicity) 또는 역치 초과 시간 지표(time-above-threshold metric)이면 별도 판단이 필요합니다.

G&W는 동일 AUC(equal AUC)라도 농도-시간 곡선(concentration-time curve)의 모양(shape)은 상당히 다를 수 있음을 명시합니다 [G&W p.190]. 따라서 C5는 AUC 백본일 뿐이며, 전체 곡선 등가성(full curve equivalence)을 보장하지 않습니다.

#### C. 소아·노인 맥락(Pediatric and elderly context) — R&T 기반

R&T Ch.14는 연령(age), 체중(weight), 성별(gender)이 약물 반응 변동성(drug response variability)의 중요한 원천이며, 생활연령(chronologic age)이 기능적 연령(functional age)을 정의하지 않는다고 경고합니다 [R&T p.411–412]. 또한 연령을 고려하지 않는 일률 용량(flat dosing)은 개별 노인 환자(elderly patient)의 필요를 충족하지 못할 수 있다고 설명합니다 [R&T p.412].

R&T Key Relationships는 BSA를 다음처럼 체중 기반으로 근사합니다:

$$BSA=1.73\cdot\left(\frac{Weight}{70}\right)^{0.75} \quad [R\&T\ p.436]$$

$$
\underbrace{BSA}_{\text{BSA 근사}}=\underbrace{1.73}_{\text{70kg BSA}}\cdot\left(\frac{\overbrace{Weight}^{\text{체중}}}{\underbrace{70}_{\text{70kg}}}\right)^{\overbrace{0.75}^{\text{BSA 지수}}}
$$

그리고 60세 일반 성인(typical 60-year-old adult) 대비 소아 유지 용량(child maintenance dose)을 다음처럼 제시합니다:

$$Child\ maintenance\ dose=1.5\cdot\left(\frac{Weight_{child}}{70}\right)^{0.75}\cdot Typical\ adult\ maintenance\ dose \quad [R\&T\ Eq.14\text{-}6,\ p.432;\ Key\ Relationships,\ p.436]$$

$$
\underbrace{Child\ maintenance\ dose}_{\text{소아 유지용량}}=\underbrace{1.5}_{\text{성인 보정}}\cdot\left(\frac{\overbrace{Weight_{child}}^{\text{소아 체중}}}{\underbrace{70}_{\text{70kg}}}\right)^{\overbrace{0.75}^{\text{BW 지수}}}\cdot\underbrace{Typical\ adult\ maintenance\ dose}_{\text{성인 용량}}
$$

다만 R&T는 mg/kg 또는 mg/1.73 m² 규칙의 폭넓은 사용(broader use)은 적용 한계(연령, 체조성, 신기능)를 명시하지 않으면 의심스럽다고 경고합니다 [R&T p.435]. 즉 **BW 알로메트리는 시작점이지, 소아·노인 용량 결정 공식 전체를 대체하지 않습니다.**

#### D. 노인 대사 진술 교정(Elderly metabolism statement correction)

“CYP3A4 metabolism이 60세 이상 매년 1% 감소”라는 문장은 과단정입니다. R&T는 크레아티닌 청소율(creatinine clearance)이 성인기(adulthood)에서 대략 1%/yr 감소한다는 경험 법칙(rule of thumb)을 제시하고 [R&T p.422], CYP3A 기질(substrate)에서는 노인군(elderly group)이 청년군(young adult)보다 낮은 청소율을 보이며 그 연령 차이를 해석할 때 1%/yr 크레아티닌 청소율 경험치(heuristic)가 관련된다고 설명합니다 [R&T p.424]. 따라서 최종 문장은 다음처럼 제한합니다: **노인에서는 신·간 기능(renal/hepatic function)과 생물학적 연령(biological age)을 별도로 보아야 하며, CYP3A 청소율도 청년 대비 감소할 수 있지만 단순 선형 시간 함수로 쓰지 않습니다.**

> 📖 **교과서 그림 참조:** Rowland & Tozer 5e, Ch.14, p.430, Fig.14-20
> 이 그림은 $BW^{0.75}$만으로 pediatric/elderly dosing이 해결된다고 보는 흔한 오류를 시각적으로 막아 줍니다. 연령에 따라 maintenance-dose fraction이 달라지는 모습을 보여 주며, 이것이 바로 C5의 caveat입니다.
> 확인 시점: C5 소아·노인 맥락(Pediatric and elderly context)을 읽은 뒤, C5 recap을 읽기 전에 확인하시면 됩니다.

---

> 

> **C5 체화 핵심**
> ① `equal unbound AUC를 맞추는 종간 dose backbone` → $Dose\propto BW^b$가 결정
> ② `소아·노인·FIH 실제 용량` → functional age, renal/hepatic function, PD metric, safety margin이 지배
> ⚡ `Eq.2:420을 final FIH dose로 사용` → caveat 누락 → 재분석·정당화 요구 가능

> ## ▶ §2 폐막 — 알로메트릭 의사결정 워크스루(Allometric Decision Walkthrough) — [EXPERT_INFERENCE, ver2 V3]
>
> 이 워크스루(walkthrough)는 **새로운 수치도, 새로운 명명 예시(named example)도 도입하지 않습니다.** C1–C5 본문에서 이미 확정된 수식·anchor·진단만 사용하여, 학습자가 **하나의 동물 PK 데이터셋을 받아 인간 노출 추정에 도달하는 5단계 의사결정**을 한 호흡에 통과시키는 시연입니다. 이 walkthrough를 닫는 순간 §1 Target Mental Model이 닫힙니다.
>
> **Step 1 — 변수 유형 진단(Variable Type Diagnosis; C1 ↔ C2/C3 진입점)**  
> 받은 변수가 무엇인지 먼저 묻습니다. CL/GFR/blood flow면 **흐름 변수(flow variable)**이므로 $b\approx 0.75$ prior로 진입합니다 (C2). V/blood volume/tissue mass면 **분포 범위 변수(extent variable)**이므로 $d\approx 1$ prior로 진입합니다 (C3). 이 분류 자체가 틀리면 C4–C5 전체가 무너집니다. 한 줄 cheat: “**flow면 0.75, extent면 1**.”
>
> **Step 2 — Prior 타당성 점검(Prior Validity Check; C1 scale-invariance + C2 failure conditions)**  
> $b\approx 0.75$ prior를 그대로 적용해도 되는지 점검합니다. 다음 6개 trigger 중 하나라도 강하게 의심되면 prior를 sensitivity analysis로 격하합니다: 종간 fu 차이, CYP isoform 차이, nonlinear MM kinetics, enterohepatic recirculation, route/formulation 차이, central/peripheral V ratio drift. fu 차이가 크면 total CL이 아니라 $CL_u$로 스케일링합니다 (Eq.2:421 라인).
>
> **Step 3 — 시간축 도출(Time-axis Derivation; C3)**  
> $b$와 $d$로부터 두 시간축을 동시에 적습니다. $t_{1/2} \propto BW^{d-b} \approx BW^{0.25}$ (큰 동물 = 긴 반감기), $k_{el} \propto BW^{b-d} \approx BW^{-0.25}$ (큰 동물 = 작은 fraction 제거 속도). 이 두 식의 부호를 동시에 보지 못하면 C4 정규화가 어긋납니다.
>
> **Step 4 — Dedrick 진단 통과(Dedrick Diagnostic Pass; C4)**  
> 종간 자료가 있으면 Elementary Dedrick($d=1$ 가정, $t/BW^{1-b}$)을 먼저 시도합니다. log-log V vs BW slope가 **0.9–1.1 안**이면 Elementary로 충분합니다. 0.9–1.1을 벗어나면 Complex Dedrick($t/BW^{d-b}$, $C\cdot BW^d/Dose$)으로 전환합니다. PK28(elementary 통과) ↔ PK29($d\approx 1.18$로 Complex 필요)가 그 벤치마크 쌍입니다. Curve fan-out이 남으면 그건 “예쁜 overlay 실패”가 아니라 **mechanism signal**입니다.
>
> **Step 5 — Equal-AUCu 용량 백본 적용(Equal-AUCu Dose Backbone Application; C5 + R&T 보강층)**  
> $Dose_{man}=Dose_{animal}\cdot (BW_{man}/BW_{animal})^b$를 backbone 한 줄로 적되, 그 위에 (i) AUC vs Cmax-driven toxicity 선택 근거, (ii) fu 보정, (iii) PK linearity 가정 점검, (iv) safety margin/toxicology, (v) route/formulation, (vi) PD metric — 6개 layer를 명시적으로 얹습니다. 소아/노인 환자에 적용할 때는 R&T Ch.14의 BSA 근사식, pediatric maintenance 식, chronologic vs functional age 경고, creatinine clearance ~1%/yr heuristic을 backbone 위에 다시 한 층 얹습니다.
>
> **닫는 한 줄:** 이 5단계가 자동 회상되어야 §1 Target Mental Model이 닫힙니다. 닫힌 학습자는 “0.75를 외우는 사람”이 아니라 “0.75를 prior로 두고 자료가 prior를 언제 밀어내는지 판단하는 사람”입니다.

---

<!-- SLIDE_START: §5 | title: 혼동쌍 분해 -->

## §5 — 혼동쌍 분해(Confusion Pair Dissection)

### Pair 1. 청소율 지수(Clearance exponent) $b$ vs 분포용적 지수(Volume exponent) $d$

| 비교 기준 | 개념 A: $b$ — CL 지수 | 개념 B: $d$ — V 지수 |
|---|---|---|
| 단위 / 차원 | 무차원 지수; flow/rate 변수의 체중 스케일 | 무차원 지수; space/extent 변수의 체중 스케일 |
| 수식 내 위치 (분자/분모/지수) | $CL=a\cdot BW^b$, $k_{el}\propto BW^{b-d}$ | $V=c\cdot BW^d$, $t_{1/2}\propto BW^{d-b}$ |
| 변화 원인 (생물학적/병적) | 대사율, 장기 혈류, GFR, 단백 결합·수송체·비선형성 | 체수분, 혈액량, 조직 부피, 지방 분포, 조직 친화성 |
| 혼동 시 임상 결과 | dose/CL scaling에 $d=1$을 넣어 $b=1$ 선형 kg당 오류 발생 | V scaling에 $b=0.75$를 넣어 분포용적·시간축 오판 |

**치명적 타격(Critical Blow):** rat 250 g→human 70 kg에서 $b=0.75$ 대신 $d=1$처럼 선형 scaling하면 차이는 $(70/0.25)^{0.25}\approx4.1$배입니다. mouse 23 g→human에서는 약 7.4배, R&T 20-g mouse 예시는 7.7배입니다. 이 오류는 첫 human exposure estimate의 order를 바꿉니다.

**⚡ 기억 고리 (Memory Hook) — *기능 vs 공간*: [EXPERT_INFERENCE, v3]**  
CL은 기능적 처리 능력이고 V는 물리적 분포 공간입니다. 결론은 $t_{1/2}=0.693\cdot V/CL\propto BW^{d-b}\approx BW^{0.25}$이며, 큰 동물은 절대 CL은 크지만 단위 시간당 fraction 제거는 작습니다.

### Pair 2. Kallynochron vs Apolysichron

| 비교 기준 | 개념 A: Kallynochron | 개념 B: Apolysichron |
|---|---|---|
| 단위 / 차원 | $t/BW^{1-b}$; $d=1$ 가정의 생리학적 시간 | $t/BW^{d-b}$; $d$ 반영 생리학적 시간 |
| 수식 내 위치 (분자/분모/지수) | Elementary Dedrick x축 | Complex Dedrick x축 |
| 변화 원인 (생물학적/병적) | V가 체중에 거의 비례할 때 유지 | V 지수가 1에서 벗어날 때 필요 |
| 혼동 시 임상 결과 | $d
eq1$에서 curve fan-out을 놓침 | 필요 없는 complex 보정으로 해석 과잉 가능 |

**기억 고리:** Kallynochron은 kg 단위로 정규화한 생리학적 시간이고, Apolysichron은 $BW^d$ 단위로 정규화한 생리학적 시간입니다. PK29 compound X처럼 $d>1$이면 차이가 드러납니다.

### Pair 3. 체중 알로메트릭 스케일링(Body Weight Allometric Scaling) vs 체표면적 스케일링(Body Surface Area Scaling)

| 비교 기준 | 개념 A: $BW^b$ allometry | 개념 B: BSA scaling |
|---|---|---|
| 단위 / 차원 | 변수별 지수 $b$를 갖는 체중 기반 거듭제곱 관계 | $BSA\approx1.73(Weight/70)^{0.75}$ 형태의 체표면적 근사 |
| 수식 내 위치 (분자/분모/지수) | $Y=a\cdot BW^b$의 지수 | BSA 또는 mg/1.73 m² dose rule에 들어가는 근사 지수 |
| 변화 원인 (생물학적/병적) | 화합물·변수 특이성, 종 수, 결합, 대사·수송 기전 | 연령, 체조성, 신기능 한계를 명시해야 함 [R&T p.435] |
| 혼동 시 임상 결과 | 종 수 부족 시 slope 불안정 또는 기전 예외 누락 | pediatric/elderly dosing을 과도하게 단순화 |

**정리:** BSA는 allometry의 적이 아니라 임상적으로 굳어진 $BW^{0.75}$ 근사입니다. 그러나 BSA라는 이름이 붙었다고 renal maturation, obesity, functional age 문제가 사라지는 것은 아닙니다.

**⚡ 기억 고리 (Memory Hook) — *직선 도로 vs 우회로*: [EXPERT_INFERENCE, v3]**  
단순 알로메트리는 $y=a\cdot BW^b$만으로 종간 스케일링을 완성하는 직선 도로입니다. 보정 인자(MLP, brain weight, PPB correction)는 특정 약물에서 대사 또는 결합 차이가 클 때 필요한 우회로이며, BSA 변환도 maturation/binding/disease state 문제를 해결하지는 않습니다.

**§5 요약:** $b/d$, Kallynochron/Apolysichron, BSA/BW allometry 중 하나라도 섞이면 table, figure, dose narrative가 동시에 흔들립니다.

<!-- SLIDE_START: §7 | title: 자기점검 -->

## §7 — 자기점검(Self-Test): 능동 회상 모듈(Active Recall Module)

---

### Q1. 회상(Recall) — $a$와 $b$의 의미

*왜 이 질문 — [EXPERT_INFERENCE, ver2 V4]:* C1의 수식 골격을 손에서 입으로 옮길 수 있는지 확인합니다. 이 회상이 안 되면 C2 이후 모든 추론이 흔들립니다.

**질문:** $Y=a\cdot BW^b$에서 $a$와 $b$를 각각 한 문장으로 설명하고, CL과 V의 전형적 지수(exponent)를 답하세요.

**정답:**

- $a$: 화합물 의존적 절편(compound-dependent intercept); $BW=1$에서의 기준값이며 단위는 $b$에 의존합니다.
- $b$: 체중 변화에 대한 스케일링 지수(scaling exponent); 대체로 변수 유형에 의존하지만 자료 품질과 기전(mechanism)에 따라 변합니다.
- CL: $b\approx0.75$; 대사율/기능적 흐름 변수(metabolic rate/functional flow variable).
- V: $d\approx1.0$; 분포용적/분포 범위 변수(volume/extent variable).
- 따라서 $t_{1/2}\propto BW^{d-b}\approx BW^{0.25}$, $k_{el}\propto BW^{b-d}\approx BW^{-0.25}$.

---

### Q2. 회상(Recall) — 왜 $b=1$이 위험한가

*왜 이 질문 — [EXPERT_INFERENCE, ver2 V4]:* Phase 1 patch memo MUST_FIX 1번(4.1 vs 7.4 vs 7.7 fold 분리)이 입에 자동으로 나오는지 확인. species pair를 명시하지 않고 fold를 외우면 보고서 검토에서 곧장 깨진다.

**질문:** 23-g mouse에서 70-kg human으로 CL을 외삽할 때 $b=1$과 $b=0.75$의 차이는 몇 배인가요? rat 250 g→human에서는 몇 배인가요?

**정답:**

- Mouse 23 g→human 70 kg: $(70/0.023)^{1-0.75}\approx7.4$배.
- Rat 250 g→human 70 kg: $(70/0.25)^{0.25}\approx4.1$배.
- R&T의 20-g mouse 예시는 3500 vs 455로 7.7배 차이를 제시한다 [R&T p.733].
- Target AUC 기반 dose 계산에서는 CL 과대예측이 dose 과대 산출로 이어질 수 있다.

---

### Q3. 도출(Derivation) — $t_{1/2}$와 $k_{el}$의 종간 지수

*왜 이 질문 — [EXPERT_INFERENCE, ver2 V4]:* 도출을 한 번 손으로 해보면 $V/CL$과 $CL/V$의 부호가 반대라는 사실이 오래 남습니다. C3 실패 모드(Failure Mode, "$k_{el}$ 부호 놓침")의 직접 예방책입니다.

**질문:** $CL=a\cdot BW^b$, $V=c\cdot BW^d$일 때 $t_{1/2}$와 $k_{el}$의 BW 지수(exponent)를 도출하세요.

**정답:**

$$t_{1/2}=\ln2\cdot V/CL=\ln2\cdot(c/a)\cdot BW^{d-b}$$

$$
\underbrace{t_{1/2}}_{\text{반감기}}=\underbrace{\ln2}_{\text{반감 상수}}\cdot\frac{\overbrace{V}^{\text{V}}}{\overbrace{CL}^{\text{CL}}}=\ln2\cdot\left(\frac{\underbrace{c}_{\text{V 절편}}}{\underbrace{a}_{\text{CL 절편}}}\right)\cdot\underbrace{BW^{d-b}}_{\text{시간지수}}
$$

$$k_{el}=CL/V=(a/c)\cdot BW^{b-d}$$

$$
\underbrace{k_{el}}_{\text{제거속도}}=\frac{\overbrace{CL}^{\text{CL}}}{\overbrace{V}^{\text{V}}}=\left(\frac{\underbrace{a}_{\text{CL 절편}}}{\underbrace{c}_{\text{V 절편}}}\right)\cdot\underbrace{BW^{b-d}}_{\text{k 지수}}
$$

$d=1$, $b=0.75$이면 $t_{1/2}\propto BW^{0.25}$이고 $k_{el}\propto BW^{-0.25}$입니다. 큰 동물은 절대 CL이 크지만, 단위 시간당 제거 분율(fraction)은 작습니다.

---

### Q4. Dedrick — Elementary vs Complex

*왜 이 질문 — [EXPERT_INFERENCE, ver2 V4]:* PK28 ↔ PK29 벤치마크 쌍을 "switch trigger"와 함께 외우게 만드는 진단 회상 문제. log-log V vs BW slope가 0.9–1.1 밖이면 Complex라는 입버릇이 안 만들어지면 PK29류 약물에서 정규화가 어긋난다.

**질문:** Elementary Dedrick과 Complex Dedrick의 y축/x축 변환을 쓰고, 언제 Complex가 필요한지 답하세요.

**정답:**

- Elementary: $C/(Dose/BW)$ vs $t/BW^{1-b}$; $d=1$ 가정.
- Complex: $C/(Dose/BW^d)$ 또는 $C\cdot BW^d/Dose$ vs $t/BW^{d-b}$.
- log-log $V$ vs $BW$ slope가 1에서 벗어나면, 예를 들어 PK29 compound X처럼 $d\approx1.18$이면 Complex Dedrick이 필요합니다.

---

### Q5. 출처 불일치 처리(Source discrepancy handling) — PK28/PK29

*왜 이 질문 — [EXPERT_INFERENCE, ver2 V4]:* 학술 보고서·심사 문서에서 source-internal 수치 불일치를 임의로 하나로 "고정"하는 것은 무결성 위반입니다. citation scope를 함께 적는 습관이 들어야 합니다.

**질문:** PK28 methadone과 PK29 compound X의 source-internal numerical discrepancy를 어떻게 인용해야 하나요?

**정답:**

- PK28 methadone rat $t_{1/2}$: G&W §2.10.6 본문은 2.9 h, PK28 case는 3.9 h로 다릅니다. 하나를 고르지 말고 `[§2.10.6 set]` 또는 `[PK28 case set]`을 명시합니다.
- PK29 parameter set: G&W §2.10.7은 $a=0.021,b=0.74,c=0.076,d=1.18,e=0.56,g=0.075$; PK29 case는 $a=0.021,b=0.75,c=0.10,d=1.21,e=0.54,g=0.071$입니다. citation scope와 수치를 일치시킵니다.

---

### Q6. 적용(Application) — human CL 예측

*왜 이 질문 — [EXPERT_INFERENCE, ver2 V4]:* 숫자가 손에서 나오는지 확인. 이 계산이 입에서 자동으로 안 나오면 FIH exposure translation 표를 그 자리에서 채울 수 없다.

**시나리오:** Mouse BW=25 g, observed CL=0.012 L/hr. 70-kg human CL을 (a) $b=0.75$, (b) $b=1.0$으로 계산하고 차이를 해석하시오.

**정답:**

(a) $CL_{human}=0.012\cdot(70/0.025)^{0.75}\approx4.6$ L/hr.  
(b) $CL_{human}=0.012\cdot(70/0.025)^1\approx33.6$ L/hr.

$$
\underbrace{CL_{human}}_{\text{human CL}}=\underbrace{CL_{mouse}}_{0.012}\cdot\left(\frac{\overbrace{70}^{\text{human kg}}}{\overbrace{0.025}^{\text{mouse kg}}}\right)^{\overbrace{b}^{\text{선택 지수}}}
$$

  
차이는 약 7.3배입니다. $b=1$은 선형 kg당 오류(linear per-kg fallacy)이며, target AUC 기반에서는 dose도 과대 산출할 수 있습니다.

---

### Q7. 적용(Application) — child/elderly dose context

*왜 이 질문 — [EXPERT_INFERENCE, ver2 V4]:* R&T Ch.14의 핵심 메시지(chronologic ≠ functional age)가 입에서 나오는지 확인. C5 backbone만 외운 학습자는 소아/노인 용량을 단순화 오류로 망친다.

**질문:** 왜 소아 또는 노인 용량에서 $BW^{0.75}$만으로 충분하지 않을까요?

**정답:**

R&T Ch.14는 생활연령(chronologic age)이 기능적 연령(functional age)을 정의하지 않는다고 설명합니다 [R&T p.411–412]. 소아에서는 renal/hepatic maturation, 체수·binding 변화가 중요하고, 노인에서는 renal function, hepatic metabolism, disease state, body composition이 중요합니다. 따라서 $BW^{0.75}$는 시작점일 뿐이며, renal/hepatic function과 biological age 보정이 필요합니다.

---

### Q8. 보스 딜레마(Boss Dilemma) — two-species regression vs physiological prior

*왜 이 질문 — [EXPERT_INFERENCE, ver2 V4]:* 보스 딜레마(Boss Dilemma)입니다. 점추정값과 physiological prior가 충돌할 때 무엇을 primary로 두고 무엇을 sensitivity로 보일지를 입으로 정당화할 수 있어야 합니다. 동시에 ICH/FDA 단정문을 자발적으로 차단하는 source language discipline이 동작하는지 확인합니다.

**시나리오:** Rat와 dog 두 종만으로 log-log CL 회귀를 했더니 $b=0.62$가 나왔습니다. 문헌적 physiological prior $b=0.75$와 충돌합니다. FIH exposure translation table에는 무엇을 primary로 두겠습니까?

**정답:**

두 종 회귀의 점추정값은 leverage가 약하고 confidence interval이 넓을 가능성이 큽니다. 따라서 primary는 생리학적 prior(physiological prior) $b=0.75$로 두고, $b=0.5,0.62,0.75,1.0$ sensitivity analysis를 함께 제시합니다. 단, $b=0.75$를 특정 ICH/FDA 조항이 직접 명시한다고 쓰지는 않습니다. 본 PDF 범위에서 방어 가능한 표현은 “mammalian metabolic rate와 functional flow variable의 allometric rationale에 근거한 prior”입니다. `[확인 필요]` 규제 문구는 원문 가이드라인 확인 전 사용하지 않습니다.

---

**§7 요약:** 자기점검(self-test)의 목표는 수치 암기가 아니라 세 가지 방어 능력입니다. (1) $b$와 $d$를 구별합니다. (2) $b=1$ 오류가 dose/AUC에 주는 방향을 설명합니다. (3) source discrepancy와 NOT_IN_SOURCE 규제 표현을 스스로 차단합니다.

---

<!-- SLIDE_START: §8 | title: 메타 프레임과 큰 그림 -->

## §8 — 메타 프레임과 큰 그림(Meta-Frame & Big Picture)

### A. 위치 잡기(Positioning) — 이 세션이 시스템으로 작동하는 세 순간

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| 동물-인간 노출 번역 표 작성 | $b$, $d$, $CL_u$ | → | first human exposure estimate의 order 변화 | C1–C5 spine을 한 표에 연결 |
| PopPK 체중 공변량 결정 | WT exponent | → | 좁은 WT range에서 SE 증가·점추정값 흔들림 | $b=0.75$ fixed primary + sensitivity |
| PBPK 장기 스케일링 | organ blood flow, organ volume | → | flow/extent 혼동 시 장기별 CL/V 오판 | 혈류는 rate-like, 부피는 extent-like로 분리 [R&T p.731–743] |

### B. 이 섹션이 약할 때의 실패 모드(Failure Modes)

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| 성인 60–90 kg처럼 WT range가 좁음 | CL exponent | → | slope drift, SE 증가 | fixed prior와 estimated model을 분리 |
| PK29 compound X처럼 $d>1$ | V exponent | → | Elementary Dedrick fan-out | $d$ estimate 또는 Complex Dedrick 검토 |
| 소아·노인에서 BW scaling만 사용 | functional age, renal/hepatic function | → | maturation·renal function·body composition 누락 | R&T age/weight caveat를 별도 gate로 둠 [R&T p.412–415] |

### C. 전문가 해석 지점(Professional Moat)

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| $b>1$ 또는 $b<0.5$ | CL exponent | → | 기전 신호와 통계 잡음 혼재 | 종 수, leverage, binding, nonlinearity, metabolism route 확인 |
| FIH/exposure translation 문장 작성 | Eq.2:420 | → | final starting-dose overclaim 위험 | equal-AUCu dose backbone으로만 기술 |
| Dedrick plot fan-out | $d$, compartment ratio | → | overlay 실패를 그림 문제로 오독 | $d
eq1$, multicompartment, model misspecification 점검 |
| PK28/PK29 source discrepancy | citation scope | → | 수치 무결성 손상 | `[§2.10.6 set]` 또는 `[PK28 case set]`처럼 범위 명시 |

### D. 후속 세션 연결 지식 그래프

| 후속 세션 | 이 세션에서 열리는 개념 | 이 세션 없으면 실패하는 것 |
|---|---|---|
| PopPK weight covariate | flow vs extent 지수 분리 | CL/V WT exponent를 기계적으로 고정하거나 추정 |
| PBPK organ scaling | organ blood flow vs organ volume | 장기 혈류와 부피를 같은 지수로 처리 |
| FIH exposure translation | equal-AUCu backbone + sensitivity | Eq.2:420을 final starting-dose rule로 오용 |
| Pediatric/elderly dosing | chronologic age ≠ functional age | BW/BSA만으로 maturation·renal function 누락 |

### E. 최종 1페이지 사고 모델(Final One-Page Mental Model)

```text
1. 변수의 종류를 먼저 묻는다.
   - flow/rate?  → CL, GFR, blood flow → b≈0.75
   - space/extent? → V, blood volume, tissue mass → d≈1
   - time? → V/CL → d-b≈0.25
   - rate constant? → CL/V → b-d≈-0.25

2. 종간 dose/exposure translation은 total dose가 아니라 unbound exposure 관점에서 읽는다.
   - AUCu equality → Dose ∝ BW^b
   - mg/kg ratio → BW^(b-1)

3. 예외를 먼저 찾는다.
   - fu 차이, CYP isoform 차이, nonlinear PK, transporter, enterohepatic recirculation, route/formulation 차이

4. source language를 지킨다.
   - PDF-supported: G&W/R&T 수식, PK28/PK29 anchor, R&T age/renal/BSA caution
   - not directly supported: ICH/FDA/MABEL/NONMEM/QSP claims → 삭제 또는 [교과서 외 해석]
```

**§8 최종 요약:** Session 14의 핵심은 “0.75를 외우는 것”이 아닙니다. 어떤 변수가 왜 0.75이고, 어떤 변수는 왜 1이며, 그 차이가 시간과 dose를 어떻게 바꾸는지 보는 것입니다. 이 관점이 allometry를 공식 암기에서 모델링 판단으로 바꿉니다.

---

## v3.7 출력 후 자가검증 체크리스트

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
| 수치 anchor 보존 | Compound A 등 원본 수치 | ✓ (PK28/PK29, 4.1/7.4/7.7 fold, R&T/G&W page tag 보존) |
| [M] 나비효과 이중 종착점 | Apex 카드 전체 | ✓ |

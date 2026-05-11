# 10 — PK/PD 모델 기초: Emax·Hill·AUEC

## 출처 및 범위 노트

이 장은 Gabrielsson & Weiner 5e Ch.3의 수용체 결합(receptor binding), $E_{max}$/Hill, 비정상상태 반응/AUEC(non-steady-state response/AUEC) 관련 범위와 Rowland & Tozer 5e Ch.8의 시간 지연(time delay), 히스테리시스(hysteresis), 효과 구획(effect compartment), 간접 반응(indirect response), 효과 지속 시간(duration of effect) 관련 범위를 바탕으로 합니다.

- 사용 범위: G&W p.199–224, p.229–234, p.732–741; R&T p.233–264.
- 교과서 원그림은 본문에 직접 삽입하지 않습니다. `FIGURE_POINTER`는 원그림 확인 위치를 안내하고, `FIGURE_SCHEMATIC`은 교과서 원그림을 복제하지 않고 새로 구성한 해설 도식입니다.
- 범위 밖 구간은 본문에서 `[확인 필요 — 첨부 PDF 미포함 구간]`처럼 표시하며, 본 자료에서 추정하여 보강하지 않습니다.

---

## PART A — 학습자용 전체 핸드아웃

## 학습자 내비게이션 안내

**이 자료 사용법:** 먼저 §1에서 C1–C5의 위치를 잡고, §2의 각 개념 해부 카드(Concept Anatomy Card)를 순서대로 읽으면 됩니다. `FIGURE_POINTER`는 교과서 원그림을 직접 확인하라는 안내이며, 본 문서에는 저작권 그림을 삽입하지 않습니다. `FIGURE_SCHEMATIC`은 교과서 원그림을 복제하지 않고 새로 구성한 해설 도식입니다.

**학습 경로:** C1에서는 $K_d$와 $EC_{50}$의 층위를 분리합니다. C2에서는 Hill $n$을 가파름/설계 파라미터(steepness/design parameter)로 고정합니다. C3–C4에서는 히스테리시스(hysteresis)가 보일 때 직접 혈장-반응 가정을 내려놓고 지연 위상(delay topology)을 선택하는 법을 익힙니다. C5에서는 AUEC와 지속 시간(duration)이 약물 반감기(drug half-life)만으로 결정되지 않는다는 점을 반응-시간 척도(response-time scale)에서 확인합니다.

**시작 전 점검:** 평형(equilibrium), 1차 제거(first-order elimination), 기저 반응(baseline response), 농도-시간 곡선(concentration-time curve), 반응-시간 곡선(response-time curve)의 차이를 먼저 떠올리면 됩니다.  
**학습 후 확인:** $K_d\neq EC_{50}$, $n\neq$ 기전 증명, 히스테리시스 $\neq$ 잡음, 약물 $t_{1/2}\neq$ 효과 지속 시간을 각각 한 문장으로 설명할 수 있어야 합니다.

---

# §1 — 세션 개요와 로드맵

**소스 통합:** G&W Ch.3는 수용체 결합(receptor binding) → $E_{max}$/Hill → 비정상상태 반응/AUEC(non-steady-state response/AUEC)의 수식적 골격을 제공합니다. R&T Ch.8은 같은 개념을 임상 시간축, 히스테리시스(hysteresis), 효과 구획(effect compartment), 간접 반응(indirect response), 효과 지속 시간(duration of effect)으로 번역합니다.

<!-- MASTER LENS -->
**Big Idea:** PD 모델링의 본질은 농도-효과 관계의 **비선형성($E_{max}$ / Hill $n$)**과 **시간 지연(hysteresis)**을 동시에 해부하는 것입니다. 전자는 용량 증량(dose escalation)의 단계 크기와 농도범위 설계를 결정합니다. 후자는 발현/소실(onset/offset), 투여 간격(dosing interval), 율속 과정(rate-limiting process) 판단을 결정합니다.

G&W는 PK/PD 모델링의 목적을 생리·병리 조건에서 반응의 크기(response magnitude)와 시간 경과(time course)를 예측하는 핵심 in vivo 특성의 식별로 제시합니다. 따라서 용량-반응(dose-response)만으로는 충분하지 않습니다. 효과와 연결되는 관련 구획(relevant compartment)에서 시간 경과에 따른 노출(exposure over time)과 생물학적 반응을 연결해야 합니다. 이상적인 PD 지표는 민감하고(sensitive), 점진적이며(gradual), 임상적으로 의미 있고(meaningful), 객관적이고(objective), 재현 가능해야(reproducible) 합니다. 또한 대조군(control)을 포함한 2–4개 용량 수준 중 최소 하나는 최대 반응(maximum response)에 도달하도록 설계하는 것이 권장됩니다. [G&W p.199–200]

> **Insertion I1 — [TEXTBOOK_DERIVED]** (Audit T5-B SHOULD_FIX: R&T objectives 명시)  
> R&T Ch.8의 출발점은 명시적입니다. 약효 해석에는 항상 *시간*이 동반되어야 합니다. 따라서 본 챕터의 학습 목표는 (i) 혈장 농도(plasma concentration)와 반응(response) 사이의 시간 지연을 *진단*하는 법(C3 hysteresis), (ii) 그 지연을 구조적으로 *흡수*하는 법(C4 effect compartment vs systems-in-flux/indirect response), (iii) 효과의 *지속*을 혈장 반감기(plasma half-life)와 분리해 해석하는 법(C5 PK vs PD rate-limiting)입니다. [R&T p.233]

**개념 항법도:**
- C1. 질량작용법칙(Law of Mass Action) → $E_{max}$ 골격. [G&W p.202–204]
- C2. Sigmoid $E_{max}$ / Hill 모델 [⚡ Apex Concept]. [G&W p.216–220; PD3 p.732–741]
- C3. 히스테리시스(Hysteresis) — 시간 지연의 시각적 진단. [R&T p.233–235]
- C4. 효과 구획(Effect Compartment) + 유동 시스템(Systems-in-flux) / 간접 반응(Indirect Response). [R&T p.241–248]
- C5. AUEC + 지속 시간(Duration) + PK/PD 율속(rate-limiting). [G&W p.229–234; R&T p.249–259]

<!-- ANCHOR -->
**구조적 흐름:** 질량작용법칙(C1) → $E_{max}$ 쌍곡선 → Hill $n$ 도입으로 sigmoid 일반화(C2) → 평형 가정의 붕괴가 히스테리시스로 드러남(C3) → 효과 구획 또는 시스템 전환(system turnover)으로 시간 지연 흡수(C4) → 반응-시간 곡선의 적분량과 지속 시간을 설계 지표로 사용(C5)의 순서로 읽으면 됩니다.

**범위 경계:** G&W §3.6.1의 경쟁적 길항(competitive antagonism) 시작부까지만 본문에 포함합니다. G&W §3.6.2–§3.6.5 및 G&W §3.12 기저치 모델링(baseline modeling)은 `[확인 필요 — 첨부 PDF 미포함 구간]`으로 유지하고 본 세션에서 추정하지 않습니다.

---

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.199, Fig.3.1
Why this matters: 이 그림은 전체 세션을 농도-반응 감수성(concentration-response sensitivity)과 반응-시간 거동(response-time behavior)이라는 두 개의 연결된 PD 문제로 잡아 줍니다. 이 그림이 없으면 C1–C5가 하나의 PK→PD 번역 사슬이 아니라 서로 분리된 수식처럼 보일 수 있습니다.
When to look: §1 로드맵을 읽기 전, 또는 §1의 Big Idea를 읽은 직후에 확인하면 됩니다.
Learner instruction: 왼쪽 패널에서 potency/efficacy를, 오른쪽 패널에서 onset/intensity/duration을 확인하세요. 그런 다음 C1–C2는 왼쪽 패널에, C3–C5는 오른쪽 패널에 대응시키면 됩니다.
<!-- /FIGURE_POINTER -->

---

# §2 — 개념 해부 카드

---

## Card C1 — 질량작용법칙(Law of Mass Action) → $E_{max}$ 골격


<!-- MASTER LENS -->
### [개념 Big Idea]

$K_d$는 리간드-수용체 결합 친화도(ligand-receptor binding affinity)의 지표입니다. $EC_{50}$는 결합 이후 신호전달(transduction)과 조직 반응(tissue response)까지 포함한 기능적 감수성(functional sensitivity)의 지표입니다. **$K_d$와 $EC_{50}$가 다를 수 있다는 사실**이 C1의 핵심입니다. 그 차이를 만드는 대표 이유가 여분 수용체(spare receptor)와 증폭 연쇄(cascade amplification)입니다. [G&W p.203–206]

<!-- ANNOTATION -->
즉, 결합이 강하다는 말과 조직에서 절반 효과가 낮은 농도에서 나온다는 말은 같은 뜻이 아닙니다.

<!-- ANCHOR -->
평형 결합의 미시적 동역학을 점유율(occupancy) 식으로 정리하면, $E_{max}$ 모델의 분자와 분모가 왜 같은 농도 단위를 가져야 하는지 드러납니다.

### A. 형식적 정의(Formal Definition)

가역적 1:1 약물-수용체 결합(drug-receptor binding)에서 반응 $E$는 결합된 수용체 복합체(occupied receptor complex — 약물이 결합한 수용체 풀) $[RC]$에 비례합니다. 수용체가 모두 점유(occupied)될 때 $E_{max}$(← 농도가 무한대일 때 도달하는 최대 가능 효과) $=\alpha[R_T]$이며, $\alpha$는 고유활성(intrinsic activity — 수용체 1단위가 만들어내는 효과 크기, 부분효현제일수록 작음)입니다. [G&W p.203]

### B. 도출(Derivation)

**평형 결합:**

$$
\frac{d[RC]}{dt}=k_1[R][C]-k_{-1}[RC]=0
$$

따라서

$$
K_d=\frac{k_{-1}}{k_1}=\frac{[C][R]}{[RC]}
$$

총 수용체 농도 $[R_T]=[R]+[RC]$를 대입하면

$$
\frac{[RC]}{[R_T]}=\frac{[C]}{[C]+K_d}
$$

반응 비례성(response proportionality)을 적용하면

$$
\frac{E}{E_{max}}=\frac{[C]}{[C]+K_d}, \qquad E=\frac{E_{max}\cdot [C]}{[C]+K_d}
$$

기능적 반응(functional response)에서는 $K_d$ 대신 $EC_{50}$가 사용됩니다.

$$
E=\frac{E_{max}\cdot C}{EC_{50}+C}
$$

`[출처: G&W 5e, Ch.3, p.202–204, Eq.3:1–3:10]`

### C. 구조적 필연성(Structural Necessity)

분자 $[C]$는 이용 가능한 리간드(available ligand)가 늘수록 수용체 점유율이 증가한다는 질량작용법칙의 결과입니다. 분모 $[C]+K_d$는 수용체 보존(receptor conservation — 수용체 총량 보존)을 반영합니다. 이 구조 때문에 점유율은 0–1 사이에 머물며, 반응도 $E_{max}$를 초과하지 않습니다.

### D. 가정과 경계 조건(Assumptions & Boundary Conditions)

- 1:1 가역적 결합(reversible binding), 평형(equilibrium), 단일 유효 생체구획 농도(single effective biophase concentration).
- 반응은 $[RC]$에 비례합니다. 수용체 비축분(receptor reserve — 여분 수용체에 의한 증폭 여지)이 있으면 수용체가 완전히 점유되지 않아도 최대에 가까운 효과가 발생할 수 있습니다.
- $EC_{50}\neq K_d$일 수 있습니다. G&W는 점유율-반응 불일치(occupancy-response 불일치)와 신호 증폭(signal amplification)을 명시합니다. [G&W p.204–206]

### E. 한계(Limitations)

여분 수용체가 많거나 증폭 이득(cascade gain)이 큰 조직에서는 수용체의 소량 점유(small occupancy)만으로도 큰 반응(large response)이 나타날 수 있습니다. G&W Fig.3.5는 10% 점유율이 90% 반응으로 증폭되는 연쇄 증폭 예를 제시합니다. Fig.3.6은 동일 반응에 필요한 점유율이 조직마다 다를 수 있음을 보여줍니다. [G&W p.205–206]

포화/치환 결합(saturation/displacement binding)과 Cheng-Prusoff 변환은 수용체 결합 분석(receptor binding assay)의 Ki/$IC_{50}$ 해석에 필요하지만, 본 세션에서는 기능적 $EC_{50}$와 결합 $K_d$를 혼동하지 않는 경계로만 사용합니다. [G&W p.206–210]

<!-- TRENCH -->
**[실무 팁(Trench-Level Tip)]** $EC_{50}$ 공변량 효과(covariate effect)가 보이면 먼저 “약물 측(drug-side) 변화인가, 시스템 측(system-side) 변화인가?”를 분리합니다. 총 농도(total concentration) 기반 $EC_{50}$ 변화는 단백질 결합(protein binding) 변화일 수 있습니다. 따라서 비결합 농도(unbound concentration) 분석이 없으면 수용체 감수성(receptor sensitivity) 변화로 단정하지 않습니다. `[실무 구현 번역]`

### F. 제텔카스텐 원자 노트(Zettelkasten Atom)

**원자 노트 C1(Atom C1):** $K_d$는 결합 강도, $EC_{50}$는 결합 이후 조직·신호 시스템까지 포함한 기능적 감수성(functional sensitivity)입니다. $E_{max}$ 식의 쌍곡선은 수용체 보존(receptor conservation)과 평형 질량작용(equilibrium mass action)에서 나옵니다.

<!-- RECAP -->
**요약(Recap):** C1은 $E_{max}$ 모델을 “경험식”이 아니라 수용체 점유율(receptor occupancy)과 반응 신호전달(response transduction)의 압축형으로 보게 만듭니다.

> **숙련 노트(Mastery Note) — [AUDIT_DERIVED]**  
> C1을 읽은 뒤에는 $K_d$, 총 $EC_{50}$, 비결합 $EC_{50}$, 조직 반응 감수성(tissue response sensitivity)을 같은 층위의 숫자로 배열하지 않습니다. 어느 숫자가 결합 분석(binding assay)에서 왔고, 어느 숫자가 기능적 반응(functional response)에서 왔는지를 먼저 분리해야 후속 공변량 해석이 무너지지 않습니다.

> **실무 체화 요약(Practice Brief) — C1 — [EXPERT_INFERENCE, v3]**  
> 보고서나 리뷰에서 새로운 $EC_{50}$ 값을 만났을 때 던질 첫 두 질문: (1) **출처가 결합 분석(binding assay)인가, 기능적 분석(functional assay)인가?** (2) **총 농도(total)인가 비결합 농도(unbound)인가?** 이 두 분리가 안 된 $EC_{50}$ 숫자는 임상 결정 근거로 사용하지 말고, 원자료의 단백질 결합(protein binding) 정보부터 확인합니다. 임상약사 출신이라면 vancomycin/tacrolimus의 비결합 분율(unbound fraction) 변동 경험이 그대로 적용됩니다.

<!-- FIGURE_SCHEMATIC -->
Title: $K_d$와 $EC_{50}$의 분리: 수용체 점유율(receptor occupancy) → 신호전달(transduction) → 반응(response)
Mode: R
Visual objective: 학습자가 5초 안에 기능적 반응 곡선(functional response curve)이 수용체 점유율 곡선(receptor occupancy curve)보다 왼쪽으로 이동할 수 있음을 볼 수 있어야 합니다.
Core message: $K_d$는 결합 친화도(binding affinity)에 속하고, $EC_{50}$는 증폭된 조직/시스템 반응(tissue/system response)에 속합니다.
Elements to include: 공통 농도 x축, $K_d$로 표시된 수용체 점유율/자극 곡선, $EC_{50}$로 표시된 왼쪽 이동 기능적 반응 곡선, 수용체 점유율 → 자극/신호전달 → 반응 화살표 사슬, $EC_{50}$가 $K_d$와 다를 수 있으며 예외가 존재한다는 주석.
Elements to exclude: Cheng-Prusoff 도출, full/partial agonist profile, 교과서 원 레이아웃, 원 색상 체계, 세부 수용체 만화.
Suggested rendering: SVG
Caption: 수용체 결합과 기능적 반응은 반드시 일치하지 않습니다. 신호전달/연쇄 증폭(transduction/cascade amplification) 때문에 $EC_{50}$는 $K_d$와 달라질 수 있습니다.
Alt text: 두 개의 농도-반응 곡선이 하나의 농도축을 공유하며, 기능적 반응 곡선이 수용체 점유율 곡선보다 왼쪽으로 이동해 $EC_{50}$–$K_d$ 분리를 보여 줍니다.
Source relation: 교과서 개념을 바탕으로 재도식화함.
<!-- /FIGURE_SCHEMATIC -->


---

## Card C2 — Sigmoid $E_{max}$ / Hill 모델 [⚡ Apex Concept]


<!-- MASTER LENS -->
### [개념 Big Idea]

> **임상 직관 도입 — [EXPERT_INFERENCE, v3]**  
> 항생제 또는 항부정맥제를 두 배 증량했는데 효과가 두 배가 되지 않는 경험은 임상 약사라면 이미 알고 있습니다. 왜일까요? 효과에는 천장($E_{max}$)이 있기 때문입니다. 그렇다면 그 천장에 *얼마나 빨리* 도달하는가 — 그것을 결정하는 것이 곡선의 가파름, 즉 **Hill coefficient $\gamma(=n)$**입니다. $E_{max}$/Hill 모델은 이 세 양을 분리합니다: **천장($E_{max}$), 효능($EC_{50}$), 가파름($\gamma$)**. 특히 $\gamma$가 1보다 클수록 작은 농도 변화가 큰 반응 변화를 만들어 협역 치료역(narrow therapeutic window) 특성이 형성됩니다 — 이것이 이 카드를 Apex로 만드는 이유입니다.

Hill $n$은 기전 증명(mechanism proof)이 아니라 **곡선 가파름/유연성 파라미터(curve steepness/flexibility parameter)**입니다. 그러나 임상적으로는 강력합니다. $n$이 커질수록 효과 50%에서 90%로 상승하는 데 필요한 농도 배율(concentration ratio)이 줄어듭니다. 즉, 더 좁은 농도 구간 안에서 반응이 완성됩니다. 따라서 용량 조절 단계 크기(dose-titration step size)와 안전 마진(safety margin) 해석이 더 민감해집니다. [G&W p.216, p.220]

선형/로그-선형 효과 모델(linear/log-linear effect models)은 제한된 농도 범위에서는 유용합니다. 그러나 효과 고원부(effect plateau — 농도 증가에도 효과가 더 늘지 않는 구간)와 급격한 전환(steep transition)을 설명하려면 일반 $E_{max}$를 넘어 sigmoid $E_{max}$가 필요합니다. [G&W p.210–216]

### A. 형식적 정의(Formal Definition)

Sigmoid $E_{max}$ 모델:

$$
E=\frac{E_{max}\cdot C^n}{EC_{50}^n+C^n}
$$

기저치(baseline)가 있는 억제 반응(inhibitory response)에서는 다음과 같이 씁니다.

$$
E=E_0-\frac{I_{max}\cdot C^n}{IC_{50}^n+C^n}
$$

`[출처: G&W 5e, Ch.3, p.216, p.218, Eq.3:32, Eq.3:34–3:35]`

> **⚡ 기억 고리 (Memory Hook) — *최대 자극 vs 최대 억제* ($E_{max}$ vs $I_{max}$) — [EXPERT_INFERENCE, v3]**  
> $E_{max}$ 모델은 **자극(stimulation) 모델** — 효과가 0(또는 기저치)에서 출발해 천장 $E_{max}$까지 *상승*합니다. $I_{max}$ 모델은 **억제(inhibition) 모델** — 효과가 기저치 $E_0$에서 출발해 $(1-I_{max})\cdot E_0$까지 *감소*합니다. $I_{max}=1$이면 완전 억제(기저치가 0이 됨)를 뜻합니다. 두 모델은 같은 sigmoid 형태이지만 **방향이 반대**입니다 — 부호와 기저치의 위치가 핵심입니다. PD 모델 선택 시 자극 데이터에 $I_{max}$를 적용하거나 그 반대로 하면 노출-반응 곡선의 천장이 과대추정되거나 억제 효율이 잘못 계산되어 용량-반응(dose-response) 결론이 정반대로 나올 수 있습니다.

### B. 파라미터 복원과 PD3 앵커(Parameter Recovery and PD3 Anchor)

그래프 기울기(graphical slope) 관계:

$$
m=\frac{n\cdot E_{max}}{4}, \qquad n=\frac{4m}{E_{max}}
$$

절편 복원(intercept recovery):

$$
C_0=EC_{50}\cdot e^{-2/n}
$$

`[출처: G&W p.219, Eq.3:38–3:42]`

> **Insertion I2 — [TEXTBOOK_DERIVED]** (Audit T3/T5-A SHOULD_FIX: G&W p.200 design message anchor)  
> Sigmoid $E_{max}$/$I_{max}$ 식의 *식별 가능성*은 모델 형태에 의해서만 결정되지 않고 실험 설계에 의해 결정됩니다. G&W p.200은 PD 모델 식별의 최소 설계 요건으로 대조군(control) + 2–4개 용량 수준(dose levels), 그중 적어도 한 용량(dose)이 최대 반응(maximum response)에 도달할 것을 명시합니다. PD3가 이 원칙의 직접 시연입니다 — 0–500 µg/L 설계(design)는 고원부(plateau)에 충분히 닿지 못해 sigmoid 우월성(sigmoid superiority)을 통계적으로 입증하지 못하지만, 0–800 µg/L 설계(design)는 같은 원칙을 만족시켜 모델 판별(model discrimination)을 가능하게 합니다. [G&W p.200, p.734–741]

PD3 혈압 억제 $I_{max}$ 사례(blood-pressure inhibitory $I_{max}$ case)는 초기 그래프 추정치(initial graphical estimate)와 최종 모델 추정치(final model estimate)를 연결합니다. 0–800 µg/L 설계(design)의 sigmoid $I_{max}$ 모델에서 $E_0=171$, $I_{max}=34.7$, $IC_{50}=140$, $n=2.03$, AIC=45.6이 제시되며, 일반 $I_{max}$ 모델(ordinary $I_{max}$ model)은 $E_0=177$, $I_{max}=49.8$, $IC_{50}=175$, AIC=50.8로 비교됩니다. [G&W p.733–735]

PD3가 전달하는 핵심 메시지는 '파라미터 추가는 곧 과적합(overfitting)'이라는 통념이 틀릴 수 있다는 것입니다. Sigmoid 모델에서 $IC_{50}$ 정밀도(precision)가 개선되고 AIC/F-test/VIF가 함께 지지되면, $n$은 단순 장식이 아니라 데이터가 실제로 요구하는 곡률 파라미터(curvature parameter — 곡선 굽힘을 설명하는 파라미터)입니다. [G&W p.734–741]

### C. 구조적 필연성(Structural Necessity)

$C^n$이 분자와 분모에 동시에 들어가는 이유는 효과가 농도의 비선형 변환(nonlinear transformation)을 거치더라도 0–$E_{max}$ 경계를 보존해야 하기 때문입니다. $n=1$이면 일반 $E_{max}$로 돌아갑니다. $n>1$이면 농도-반응 전환이 급격해집니다. $n<1$이면 활성 대사체(active metabolite), 다중 수용체 부위(multiple receptor sites), 이질성(heterogeneity) 등의 가능성을 시사할 수 있습니다. 단, 이는 단독 기전 증명(mechanism proof)이 아닙니다. [G&W p.216]

비결합 농도 변환(unbound concentration transformation)에서도 $n$은 보존됩니다.

$$
E=\frac{E_{max}(C_u/f_u)^n}{EC_{50}^n+(C_u/f_u)^n}
=\frac{E_{max}\cdot C_u^n}{EC_{u50}^n+C_u^n}
$$

단백결합 차이가 큰 비교에서는 총 $EC_{50}$가 아니라 비결합 $EC_{50}$(unbound $EC_{50}$)를 점검해야 합니다. 그래야 역가(potency) 변화와 단백질 결합(protein binding) 변화를 혼동하지 않습니다. [G&W p.216–217]

### C-2. 그럴듯한 오해(Plausible Fallacy): “곡률 억제(Curvature Suppression)”

<!-- CONFUSION -->
**오류:** “sigmoid해 보이지만 일반 $E_{max}$(ordinary $E_{max}$)도 대충 맞으니 $n=1$로 단순화합니다.”  
**교정:** PD3는 같은 약물이라도 0–500 µg/L 설계(design)에서는 F-test가 sigmoid 우월성을 통과하지 못하는 반면, 0–800 µg/L로 확장하면 통과함을 보여줍니다. 따라서 올바른 결론은 'sigmoid가 필요 없다'가 아니라, '농도 범위가 곡률(curvature)을 확인하기에 충분한가?'입니다. [G&W p.734–735, p.740–741]

Hill $n$을 “양성 협동성(positive cooperativity)이 증명되었다”라고 쓰면 출처 충실성(source fidelity)이 깨집니다. 독립적인 결합 근거(orthogonal binding evidence)가 없는 한, $n$은 가파름(steepness)과 용량 조절 민감도(dose-titration sensitivity)를 설명하는 현상학적 파라미터로 기술합니다. `[교과서 기반 + 교과서 외 규제 해석]`

> **Insertion I3 — [CRUCIBLE_DERIVED]** (Crucible Intuition #2 / Grade B: Precision-Improvement diagnostic)  
> **체화 신호(Mastery signal) — $IC_{50}$ CV 방향성 진단:** 같은 데이터에 일반 $I_{max}$(ordinary $I_{max}$)와 sigmoid $I_{max}$를 모두 적합했을 때, sigmoid에서 $IC_{50}$의 CV%가 ordinary보다 *향상*된다는 사실 자체가 $n$ 추가의 정당성을 가장 직접적으로 보여주는 신호입니다. PD3 Table 3.2에서 일반 $IC_{50}$ CV가 약 31%였던 것이 sigmoid에서 약 11%로 떨어집니다 — 진정한 과파라미터화(overparameterization)라면 정밀도가 *악화*되어야 하므로, **정밀도 향상 자체가 추가 파라미터가 데이터를 진정으로 설명하고 있다는 직접 증거**입니다. F-test나 AIC가 임계값 근처일 때 이 진단이 결정적인 보조 증거가 됩니다. [G&W p.735 Table 3.2]

> **⚡ Plausible Fallacy — Apex Concept 전용 — [EXPERT_INFERENCE, v3]**  
> **그럴듯한 오해:** "$EC_{50}$만 알면 해당 농도에서 임상 효과를 예측할 수 있습니다."  
> **왜 틀렸는가:** $EC_{50}$은 곡선의 **중간점(midpoint)** 위치만을 결정합니다. 그러나 실제 임상 반응의 *크기*는 $E_{max}$(천장)와 **Hill $\gamma$(가파름)**에 의해 함께 결정됩니다. $\gamma$가 3이면 $EC_{50}$의 ±30% 농도 변화가 반응을 약 20%→80%로 끌어올려 — 치료역이 매우 좁아집니다. 같은 ±30% 변화가 $\gamma=1$에서는 약 40%→60%에 그칩니다. 즉, **같은 $EC_{50}$라도 $\gamma$가 다르면 임상 용량 조절의 정밀도 요구가 완전히 달라집니다.**  
> **실무에서 어떻게 드러나는가:** 용량 조절 가이드라인이나 노출-반응(exposure-response) 보고서에서 $EC_{50}$만 제시하고 $\gamma$를 명시하지 않으면, 좁은 치료역 약물(면역억제제, 항부정맥제, 일부 vitamin K antagonist)에서 용량 조절 폭이 실제보다 *관대하게* 계산될 수 있습니다. 규제 심사 관행상 Hill $\gamma$가 빠진 PK-PD 섹션은 "Hill coefficient의 임상적 의의" 추가 기술 요청(deficiency)을 받기 쉽습니다. **따라서 이 카드의 핵심 결론은 단순합니다 — $\gamma$는 곡선의 미적 디테일이 아니라 임상 안전 마진 그 자체입니다.** `[교과서 기반 + 교과서 외 규제 해석]`

### D. 가정과 경계 조건(Assumptions & Boundary Conditions)

- 농도 범위가 $EC_{50}$ 주변과 고원부(plateau)를 충분히 포함해야 $n$과 $E_{max}/I_{max}$가 식별됩니다.
- 기저치 $E_0$가 시간에 따라 변하면 기저치 모델(baseline model)이 필요합니다. `[확인 필요 — G&W §3.12 첨부 PDF 미포함 구간]`
- 목표 농도 역산(target concentration inversion)은 절대 반응(absolute response)과 기저치 상대 반응(baseline-relative response)을 구분해야 합니다. [G&W p.221]

### E. 한계(Limitations)

복합 $E_{max}$(composite $E_{max}$)는 하나의 단순 sigmoid로 설명되지 않는 반응을 두 개 이상의 하위 반응(sub-response)으로 분리합니다. 즉, 관찰된 곡선 하나가 실제 생물학적 과정 하나를 의미한다고 단정하지 않습니다. Lundström et al. 예시는 $IC_{50,1}=1.8$, $IC_{50,2}=23$ µg/L, $I_{max,1}=4$, $I_{max,2}=3.2$, $n_1=1.4$, $n_2=3.7$을 제시합니다. [G&W p.221–223]

다중 결합 부위 모델(multiple binding site model)은 caffeine brain concentration 예처럼 비단조 또는 복합 곡선의 가능성을 보여주지만, 본 세션에서는 “하나의 단일 Hill 곡선(single Hill curve)이 모든 생물학을 증명하지 않는다”는 경계(boundary)로만 둡니다. [G&W p.224]

<!-- TRENCH -->
**[실무 팁(Trench-Level Tip)]** Sigmoid $E_{max}$ 적합(fitting)은 일반 $E_{max}$/$I_{max}$로 먼저 $E_0/E_{max}/EC_{50}$ 초기값을 잡은 뒤 $n=1$에서 시작합니다. PD3처럼 오차(error)가 커지면 $n$ 정밀도(precision)가 악화될 수 있으므로 “폭발” 같은 표현 대신 CV와 민감도 분석(sensitivity analysis)으로 말합니다. [G&W p.738–739] `[실무 구현 번역]`

**[실무 팁(Trench-Level Tip)]** `[실무 구현 번역]` 농도 범위 부족 Hill(Range-Starved Hill)은 농도 범위가 $IC_{50}$ 주변과 상단 고원부(upper plateau)를 충분히 건드리지 못하는 상황입니다. 이때 $n$은 1로 수렴하거나 RSE가 커질 수 있습니다. 이는 알고리즘 문제가 아니라 설계 정보(design information) 부족입니다.

### F. 제텔카스텐 원자 노트(Zettelkasten Atom)

**원자 노트 C2(Atom C2):** Hill $n$은 기전의 증명이 아니라 농도-효과 곡선(concentration-effect curve)이 얼마나 급하게 전환되는지를 나타내는 감수성 지렛대(sensitivity lever)입니다. PD3는 그 지렛대가 모델 선택과 농도범위 설계에 어떻게 연결되는지 보여줍니다.

<!-- RECAP -->
**요약(Recap):** C2는 “곡률(curvature)을 본다”는 것이 단순한 시각적 취향이 아니라 용량 범위(dose range), 정밀도(precision), 목표 농도(target concentration) 해석의 문제임을 고정합니다.

> **실무 렌즈(Practice Lens) — [CRUCIBLE_DERIVED]**  
> Hill $n$을 보고 가장 먼저 던질 질문은 “무슨 기전인가?”가 아니라 “이 농도 범위가 $IC_{50}/EC_{50}$ 주변과 고원부(plateau)를 충분히 지나갔는가?”입니다. 이 질문을 먼저 통과해야 $n$을 용량 조절 민감도(titration sensitivity) 또는 모델 판별(model discrimination)의 언어로 방어할 수 있습니다.

> **실패 모드(Failure Mode) — [AUDIT_DERIVED]**  
> $n>1$을 양성 협동성(positive cooperativity)의 증거라고 단정하면 교과서 경계를 넘습니다. 보고서 문장에서는 “가파름/유연성(steepness/flexibility)을 설명하는 현상학적 파라미터이며 가능한 기전 가설을 제시할 수 있다” 정도로 낮추는 것이 안전합니다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, Case Study PD3, p.733 Fig.PD3-3.1; p.735 Table PD3-3.2; p.741 Table PD3-3.4
Why this matters: 핵심 교훈은 단순히 sigmoid 모델이 더 잘 맞는다는 점만이 아닙니다. 원 PD3 자료는 농도 범위가 모델 판별(model discrimination)과 파라미터 정밀도(parameter precision)를 어떻게 바꾸는지 보여 줍니다.
When to look: Card C2 §B와 §C-2를 읽은 뒤 확인하면 됩니다.
Learner instruction: VIF 논의를 읽기 전에 0–500 µg/L 설계와 0–800 µg/L 설계를 비교하세요. 데이터 범위가 $IC_{50}$ 주변의 곡률(curvature)과 상단 반응 영역을 드러내기에 충분히 넓은지 먼저 물어보면 됩니다.
<!-- /FIGURE_POINTER -->


---

## Card C3 — 히스테리시스(Hysteresis): 시간 지연의 진단 도구


<!-- MASTER LENS -->
### [개념 Big Idea]

히스테리시스(Hysteresis — 같은 농도에서도 시간 방향에 따라 효과가 달라지는 현상)는 단순히 “농도와 효과가 다르게 움직인다”는 현상이 아닙니다. 오히려 이는 혈장 농도(plasma concentration)가 작용 부위(site of action) 또는 하류 반응(downstream response)을 즉시 대표하지 못한다는 구조적 진단 신호로 읽어야 합니다. R&T Ch.8은 시간(time)이 항상 고려되어야 한다고 시작하며, 단회 투여(single dose) 후 반응(response)이 혈장 농도를 따라가지 않는 사례를 제시합니다. [R&T p.233–235]

<!-- ANNOTATION -->
즉, 히스테리시스는 그림의 잡음이 아니라 모델 구조(model structure)를 바꾸라는 신호입니다.

### A. 형식적 정의(Formal Definition)

히스테리시스는 농도가 상승 구간(rising phase)에 있을 때와 하강 구간(falling phase)에 있을 때 농도-반응(concentration-response) 궤적이 달라지는 현상입니다. 경구 naproxen 500 mg 치과 통증 모델에서 비결합 혈장 농도(unbound plasma concentration)와 평균 통증 완화(mean pain relief)를 직접 도시하면 반시계 방향 고리(counterclockwise loop)가 나타납니다. 같은 농도라도 시간 순서가 다르면 효과(effect)가 다르게 보인다는 뜻입니다. [R&T p.234–235]

### B. 진단 논리(Diagnostic Logic)

Digoxin 1 mg 정맥 급속 투여(i.v. bolus) 후 첫 4시간 동안 혈장 농도는 감소하지만 좌심실 구출 시간 지표(left ventricular ejection-time index)는 증가합니다. 겉으로는 낮은 농도에서 더 큰 효과가 나는 것처럼 보입니다. R&T는 심장 조직 분포(cardiac tissue distribution)와 수용체 결합이 느리므로 혈장-효과 관계를 해석하려면 약 6시간의 분포 평형(distribution equilibrium)을 기다려야 한다고 설명합니다. [R&T p.234]

Naproxen 500 mg 경구 예시는 시간-농도/효과 도표에서는 지연이 약하게 보이지만, 효과를 비결합 농도에 직접 도시하면 고리가 명확해진다는 점을 보여줍니다. [R&T p.234–235]

### C. 구조적 필연성(Structural Necessity)

반시계 방향 히스테리시스(counterclockwise hysteresis)는 보통 효과가 혈장보다 늦는 상황입니다. 원인은 크게 두 축으로 나뉩니다.

1. **동력학적 지연(kinetic delay):** 약물이 작용 부위(site of action)에 늦게 도달하거나 느린 결합/해리(slow binding/dissociation)를 보입니다. [R&T p.235–238]
2. **역학적 지연(dynamic delay):** 측정된 반응이 하류 구획(downstream compartment)이나 전환 시스템(turnover system)에 의해 늦게 변합니다. [R&T p.236–244]

### D. 가정과 경계 조건(Assumptions & Boundary Conditions)

- 혈장 농도가 작용 부위 농도(site concentration)를 즉시 대표하지 못할 수 있습니다.
- 측정 종말점(measured endpoint)이 표적 결합(target engagement)에 가까울수록 지연이 작고, 하류 반응(downstream response)일수록 지연이 커집니다. [R&T p.236–238]
- 반시계 방향 고리는 지연을 말하지만, 지연의 원인이 분포(distribution)인지 전환(turnover)인지는 별도 진단이 필요합니다.

### E. 한계(Limitations)

채혈이 희소(sparse)하면 히스테리시스 고리의 방향과 폭이 왜곡될 수 있습니다. 또한 위약 보정(placebo correction), 기저치 변동(baseline drift), 내인성 리듬(endogenous rhythm)이 있으면 농도-반응 고리를 인과 경로(causal path)로 과해석하면 안 됩니다. 이 경우 고리(loop)는 진단 단서이지 최종 기전 증명(mechanism proof)이 아닙니다. [R&T p.244]

<!-- TRENCH -->
**[실무 팁(Trench-Level Tip)]** 히스테리시스 고리를 보면 먼저 (1) 고리 폭(loop width)이 약물 반감기의 몇 배인지, (2) 최대 효과 시점(peak effect time)이 용량 의존적(dose-dependent)인지 확인합니다. 최대 효과 시점이 용량 의존적이면 효과 구획 가능성이 커지고, 용량 비의존적(dose-invariant)이면 전환/간접 반응(turnover/indirect response) 쪽으로 기웁니다. `[실무 구현 번역]`

### F. 제텔카스텐 원자 노트(Zettelkasten Atom)

**원자 노트 C3(Atom C3):** 히스테리시스(Hysteresis)는 모델 선택 전에 보는 탐색적 자료 분석 진단(EDA diagnostic)입니다. 농도-효과 고리(loop)는 “어떤 연결 함수(link function)를 쓸 것인가”보다 먼저 “혈장(plasma)이 효과 부위(effect site)를 대표하는가”를 묻습니다.

<!-- RECAP -->
**요약(Recap):** C3는 시간 지연을 그림으로 감지하는 단계이며, C4의 효과 구획(effect compartment)과 간접 반응(indirect response)은 이 지연을 구조적으로 흡수하는 방식입니다.

> **숙련 노트(Mastery Note) — [TEXTBOOK_DERIVED]**  
> 히스테리시스 도표는 단순한 시각화가 아니라 모델 선택의 분류 도구(triage 도구)입니다. 시간-농도/효과 도표에서 지연이 애매해도 농도-반응 고리가 생기면, 혈장이 인과적 생체구획(causal biophase)을 즉시 대표한다는 가정을 내려놓아야 합니다.

> **실무 체화 요약(Practice Brief) — C3 — [EXPERT_INFERENCE, v3]**  
> 새 PD 데이터셋을 받았을 때 *모델 적합 전에* 반드시 시행할 탐색적 자료 분석 순서: (1) **시간-농도 도표와 시간-효과 도표를 같은 축에서 그려서 시간 단위가 한 자릿수 이상 다른지 확인**(Insertion I6 빠른 진단 활용), (2) **농도-효과 고리를 시간 순서로 도시하여 반시계/시계/비고리 판정**, (3) **용량 군별 최대 효과 시점이 용량 의존적인지 확인**. 이 세 단계가 끝나기 전에는 어떤 연결 함수(link function)도 고정하지 않습니다.

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.234 Fig.8-1; p.235 Fig.8-2
Why this matters: 히스테리시스(hysteresis)는 산문만으로는 충분히 이해하기 어렵습니다. 시각적 고리는 같은 혈장 농도라도 농도가 상승 중인지 하강 중인지에 따라 서로 다른 반응값에 대응할 수 있음을 보여 줍니다.
When to look: Card C3 §A–B를 읽은 뒤 확인하면 됩니다.
Learner instruction: Fig.8-2에서 고리를 따라 시간 순서의 sampling number를 따라가 보세요. 농도-반응 관계가 하나의 정적인 곡선이 아니라 경로 의존적(path-dependent)이라는 점에 집중하면 됩니다.
<!-- /FIGURE_POINTER -->


---

## Card C4 — 효과 구획(Effect Compartment) + 유동 시스템(Systems-in-flux) / 간접 반응(Indirect Response)


<!-- MASTER LENS -->
### [개념 Big Idea]

C4의 첫 질문은 “반응(response)이 혈장 농도(plasma concentration)를 늦게 따라오는가?”가 아닙니다. 진짜 질문은 **지연(delay)이 작용 부위 평형화(site-of-action equilibration) 때문인가, 아니면 생물학적 시스템 전환(biological system turnover) 때문인가?**입니다. 전자라면 효과 구획(effect compartment)이 더 자연스럽습니다. 후자라면 간접 반응/유동 시스템(indirect response/systems-in-flux)이 더 자연스럽습니다. [R&T p.245–248]

### A. C4a. 효과 구획(Effect Compartment)

효과 구획(effect compartment — 혈장과 반응 사이 지연을 흡수하는 가상 구획)은 혈장 농도와 반응을 연결하기 위해 도입한 가설적 구획(hypothetical compartment)입니다. R&T는 naproxen 히스테리시스를 효과 구획을 통해 줄이고, 효과 부위 농도(effect-site concentration)와 반응을 더 직접적으로 연결하는 그림을 제시합니다. [R&T p.245–246]

이 구획은 미시적 장기 구획(microscopic organ compartment)이 아니라 총괄 지연 표현(lumped delay representation — 여러 지연 원인을 하나로 묶은 표현)입니다. 조직 관류(tissue perfusion), 투과성(permeability), 조직 친화도, 결합 동역학(binding kinetics), 신호전달 지연(signal transduction lag)이 복합적으로 반영된 결과일 수 있습니다. 따라서 $k_{e0}$를 특정 생리상수처럼 외삽하지 않습니다. [R&T p.235–236, p.245–246]

### B. C4b. 유동 시스템(Systems-in-flux) / 간접 반응(Indirect Response)

유동 시스템(systems-in-flux)에서는 약물이 내인성 물질(endogenous substance) 또는 생리적 반응의 생성/소멸 과정(formation/loss process)을 바꿉니다. Warfarin은 프로트롬빈 복합체 전환(prothrombin complex turnover)을 통해 혈장 농도와 효과가 분리되는 대표 예입니다. Sodium warfarin 1.5 mg/kg 경구 투여 후 프로트롬빈 복합체 반응은 전환 반감기(turnover half-life) 1–2일의 영향을 받습니다. 즉, 혈장 농도가 변해도 반응은 시스템 회복 속도에 묶입니다. [R&T p.241–248]

일반 전환 골격(general turnover skeleton)은 다음과 같습니다.

$$
\frac{dR}{dt}=k_{in}-k_{out}R
$$

약물은 $k_{in}$ 또는 $k_{out}$을 자극(stimulation)/억제(inhibition)할 수 있습니다. 본 식은 G&W 비정상상태 반응 체계(non-steady-state response framework)와 R&T 유동 시스템 설명을 연결하는 최소 골격입니다. [G&W p.229–230; R&T p.241–248]

### C. 구조적 필연성(Structural Necessity)

효과 구획은 혈장과 효과 부위 사이의 평형화 지연(equilibration delay)을 흡수합니다. 간접 반응은 반응 변수 자체가 느린 전환율(turnover)을 갖기 때문에 지연이 생깁니다. 이 둘을 구분하지 않으면 현재 데이터에 대한 적합은 비슷해 보여도 외삽 결과가 달라집니다. 특히 용량 변경이나 투여 간격 변경 상황에서 예측 오차가 크게 벌어집니다.

<!-- ANCHOR -->
**용량 비의존적 최대 효과 시점 진단(dose-invariant peak time diagnostic):** 간접 반응에서는 최대 효과가 $dR/dt=0$ 조건, 즉 유입/유출 균형(input/output balance)에 의해 결정됩니다. 용량이 반응 진폭(response amplitude)을 바꿔도 시스템 전환 시간 척도가 변하지 않으면 최대 효과 시점이 거의 일정할 수 있습니다. 효과 구획에서는 용량과 농도-시간 양상(concentration-time profile)이 효과 부위 평형화의 모양을 바꿉니다. 따라서 최대 효과 시점이 용량 의존적이 될 가능성이 큽니다. `[교과서 기반 개념 + 실무 진단 번역]`

### D. 가정(Assumptions)

- 효과 구획(effect compartment)은 가설적 연결(hypothetical link)이며 실제 출처 구획(source compartment)이 아닙니다. [R&T p.245]
- 간접 반응(indirect response)은 내인성 시스템(endogenous system)의 생성/소멸 과정(formation/loss process)을 전제로 합니다. [R&T p.241–248]
- Warfarin-like 반응에서는 혈장 농도(plasma concentration)가 빨리 변해도 반응(response)은 프로트롬빈 복합체 전환(prothrombin complex turnover)에 의해 느리게 변합니다. [R&T p.242, p.247]

### E. 한계(Limitations)

NONMEM `$DES`, 격자 탐색(grid search), ETA 배치는 R&T 원문이 아니라 구현 계층(implementation layer)입니다. 본 자료에서는 모델링 실무로 연결할 때만 `[실무 구현 번역]`이라고 명시합니다.

<!-- TRENCH -->
**[실무 팁(Trench-Level Tip)]** `[실무 구현 번역]` 히스테리시스 모델 선택은 혈장 직접(plasma direct) → 효과 구획 → 간접 반응 순서로 적합합니다. 각 단계에서 용량 군별 최대 효과 시점의 용량 의존성이 사라지는지 봅니다. 효과 구획에서 충분히 사라지면 분포 지연이 주원인이고, 간접 반응에서만 설명되면 전환 시스템이 본질입니다.

**[실무 팁(Trench-Level Tip)]** `[실무 구현 번역]` PK와 혼동된 $k_{e0}$(PK-Aliased $k_{e0}$)는 추정된 효과 반감기(estimated effect half-life)가 혈장 반감기와 너무 가까워 $k_{e0}$와 제거 속도(elimination rate)가 분리되지 않는 패턴입니다. 이때 $k_{e0}$ 수치 자체보다 밀집 채혈(dense sampling) 또는 민감도 분석(sensitivity analysis)이 더 중요합니다.

### F. 제텔카스텐 원자 노트(Zettelkasten Atom)

**원자 노트 C4(Atom C4):** 효과 구획(effect compartment)은 “작용 부위 평형화 지연(site equilibration delay)”, 간접 반응(indirect response)은 “시스템 전환 지연(system turnover delay)”을 설명합니다. 히스테리시스를 줄이는 적합(fit)보다 더 중요한 것은 어떤 지연(delay)을 외삽할 것인지의 구조 선택입니다.

<!-- RECAP -->
**요약(Recap):** C4는 C3에서 감지한 시간 지연을 구조화합니다. 같은 고리라도 분포 문제인지 시스템 전환 문제인지에 따라 투여 간격(dosing interval), 발현 예측(onset 예측), 특수 집단 외삽(special population extrapolation)이 달라집니다.

> **실무 렌즈(Practice Lens) — [CRUCIBLE_DERIVED]**  
> 효과 구획(effect compartment)은 ‘작용 부위 평형화 지연(site equilibration delay)’을 흡수하고, 간접 반응(indirect response)은 ‘시스템 전환 지연(system turnover delay)’을 설명합니다. 둘이 모두 적합(fit)될 수 있을 때는 최대 효과 시점(peak-time)의 용량 의존성(dose-dependence), 반응 회복 척도(response recovery scale), 생물학적 타당성(biological plausibility)을 먼저 비교해야 합니다.

<!-- FIGURE_SCHEMATIC -->
Title: 지연 원천 위상(delay-source topology): 효과 부위 평형화(effect-site equilibration) vs 시스템 전환(system turnover)
Mode: R
Visual objective: 학습자가 5초 안에 혈장→효과 부위 지연(plasma-to-effect-site delay)과 하류 반응 전환 지연(downstream response-turnover delay)을 구분할 수 있어야 합니다.
Core message: 효과 구획(effect compartment)과 간접 반응(indirect response)은 서로 바꿔 쓸 수 있는 지연 보정 패치가 아닙니다. 두 구조는 서로 다른 인과 구조를 담고 있습니다.
Elements to include: 경로 A: 혈장 농도 $C(t)$ → 효과 부위 농도 $C_e(t)$ → 반응 $E(t)$; 경로 B: 혈장 농도 $C(t)$ → $k_{in}/k_{out}$ 조절 → 전환 반응 $R(t)$; 부위 평형화 지연(site equilibration delay)과 시스템 전환 지연(system turnover delay) 라벨; 최대 효과 시점의 용량 의존성 vs 용량 비의존성에 대한 진단 콜아웃.
Elements to exclude: NONMEM code, 수치 $k_{e0}$, 복잡한 feedback loop, 하나를 넘는 하류 전환 구획.
Suggested rendering: Mermaid
Caption: 같은 지연 반응 패턴도 부위 평형화 또는 생물학적 전환에서 생길 수 있습니다. 어떤 모델을 선택하느냐가 외삽 거동을 결정합니다.
Alt text: 두 개의 병렬 인과 경로가 혈장 농도에서 시작해, 하나는 효과 부위 구획과 반응으로 이어지고 다른 하나는 $k_{in}/k_{out}$ 전환 조절과 지연 반응으로 이어집니다.
Source relation: 교과서 개념을 바탕으로 재도식화함.
<!-- /FIGURE_SCHEMATIC -->


---

## Card C5 — AUEC + 지속 시간(Duration) + PK/PD 율속(Rate-Limiting)


<!-- MASTER LENS -->
### [개념 Big Idea]

효과 지속 시간은 약물 반감기(drug half-life)만으로 결정되지 않습니다. 혈장 농도(plasma concentration)가 사라져도 반응(response)이 남는 경우는 흔합니다. 이때 율속은 PK 제거(PK elimination)가 아니라 수용체 결합(receptor binding), 비가역적 작용(irreversible action), 표적 전환(target turnover), 하류 시스템 회복(downstream system recovery)일 수 있습니다. [R&T p.249–253]

Methylprednisolone 예시는 PK AUC가 용량 비례적(dose-proportional)이어도 림프구 반응(lymphocyte response)은 고용량(high-dose) 구간에서 포화(saturate)될 수 있음을 보여줍니다. 즉 PK 선형성(PK linearity)은 PD 선형성(PD linearity)을 보장하지 않습니다. [R&T p.257–258]

### A. 형식적 정의(Formal Definition)

AUEC(← 반응-시간 곡선 아래 면적, area under the effect curve)는 반응-시간 곡선을 하나의 면적값으로 요약한 지표입니다.

$$
AUEC=\int_0^{\infty}E(t)dt
$$

> **Insertion I4 — [TEXTBOOK_DERIVED]** (Audit T1 RESTORED/PARTIAL: G&W §3.6.6 Non-Steady-State Response framework bridge)  
> AUEC는 진공 속에서 정의되지 않습니다. G&W §3.6.6은 비정상상태 반응(non-steady-state response)의 동력학 틀(framework)을 제공합니다 — 약물 농도(drug concentration)가 시간에 따라 변하면 반응(response)도 비정상상태로 변하며, 그 결과 곡선의 모양은 입력(input, concentration-time)의 모양과 반응 시스템(response system, $E_{max}$/Hill)의 비선형성에 의해 동시에 결정됩니다. AUEC는 그 틀(framework)이 만들어낸 결과 곡선을 적분한 면적 요약 지표이며, 따라서 폐쇄형 식(closed form)은 틀의 가정(일반 $E_{max}$ + 1차 제거, ordinary $E_{max}$ + first-order elimination) 아래에서만 가능합니다. [G&W p.229–234, Eq.3:56–3:73]

1구획 1차 제거(one-compartment first-order elimination)와 일반 $E_{max}$ 모델(ordinary $E_{max}$ model)에서 G&W는 다음 폐쇄형 식(closed form)을 제시합니다.

$$
AUEC=\frac{E_{max}}{K}\ln\left(1+\frac{D}{EC_{50}\cdot V}\right)
$$

`[출처: G&W p.233–234, Eq.3:72–3:73]`

Sigmoid $E_{max}$에서는 동일한 폐쇄형 식(closed form)이 출처(source)에 제시되지 않았습니다. 따라서 수치 적분(numerical integration) 필요성은 `[수학적 추론]`으로만 표시합니다.

### B. 효과 지속 시간(Duration of Effect)

R&T는 반응 감소(response decline)의 중간 영역(약 80–20% 최대치)에서 반응이 시간에 대해 거의 선형적으로 감소할 수 있음을 설명합니다. 또한 지속 시간이 용량의 로그(logarithm)에 비례하는 관계를 제시합니다. [R&T p.249, p.254–256]

$$
t_D=\frac{1}{K}\ln\left(\frac{D}{A_{min}}\right)
$$

용량을 두 배로 늘리면 조건이 맞을 때 지속 시간은 약 반감기 1회분만큼 증가합니다. Succinylcholine 0.5 mg/kg 정맥 급속 투여 예시는 $k\approx0.2\ \mathrm{min}^{-1}$, $t_{1/2}\approx4$ min의 효과 감소와 용량-지속 시간 관계를 보여줍니다. 여기서 핵심은 용량 증가가 최대 효과(peak effect)보다 지속 시간을 더 읽기 쉽게 바꿀 수 있다는 점입니다. [R&T p.249–256]

### C. PK 율속(PK-rate-limited) vs PD 율속(PD-rate-limited)

- **PK 율속(PK-rate-limited):** 효과가 사라지는 속도가 약물 농도가 사라지는 속도에 의해 결정되는 경우입니다. 즉, 효과 감소(effect decline)가 혈장 농도 감소(plasma concentration decline)와 같은 시간 척도에서 움직입니다.
- **PD 율속(PD-rate-limited):** 효과가 사라지는 속도가 수용체/시스템(receptor/system) 회복 속도에 의해 결정되는 경우입니다. 혈장 농도(plasma concentration)는 빠르게 사라지더라도, 반응(response)은 수용체/시스템 전환(receptor/system turnover)이 완료될 때까지 오래 지속됩니다.

Aspirin은 650 mg 경구 투여 후 혈장 $t_{1/2}$가 약 15 min이지만 항혈소판 활성(antiplatelet activity)이 수일간 지속되는 예입니다. 즉, 혈장에서 약물이 빨리 사라져도 반응 시스템은 더 늦게 회복될 수 있습니다. [R&T p.251]

Omeprazole은 40 mg 경구 투여 후 혈장 $t_{1/2}$가 1시간 미만이고 약 3시간 후 혈장에는 거의 남지 않지만, 위산 분비 억제(gastric acid secretion inhibition)는 수일 단위로 회복됩니다. [R&T p.252]

Paclitaxel은 혈장에는 2일 후 거의 남지 않지만 백혈구 분율(leukocyte fraction) 변화가 수주(weeks) 척도로 움직이는 예입니다. [R&T p.253]

Acenocoumarol과 phenprocoumon 비교에서는 acenocoumarol $t_{1/2}$ 15시간, phenprocoumon $t_{1/2}$ 6일 및 반응 회복 시간(response recovery time) 차이가 PK vs PD 율속 판단의 교육적 앵커가 됩니다. [R&T p.243–244]

> **Insertion I5 — [TEXTBOOK_DERIVED]** (Audit T6 ESSENTIAL: Acenocoumarol/Phenprocoumon PK vs PD rate-limiting anchor 강화)  
> Acenocoumarol($t_{1/2}$ 15 h, 기저치 회복 약 3 days)과 phenprocoumon($t_{1/2}$ 6 days, 기저치 회복 약 2 weeks)의 직접 비교는, **같은 vitamin K antagonist 계열 안에서도 PK 율속(PK rate-limited)과 PD 율속(PD rate-limited) 패턴이 약물별로 갈라질 수 있음**을 보여주는 R&T의 교육적 앵커입니다. Acenocoumarol에서는 혈장 제거(plasma elimination) 속도와 프로트롬빈 복합체(prothrombin complex) 회복 속도가 같은 시간 척도에 가까워 PK가 율속에 더 가깝지만, phenprocoumon에서는 혈장 반감기(plasma half-life)가 시스템 전환(system turnover) 시간 안에 들어가 PD-system이 율속의 일부가 됩니다. **이 비교는 “PK/PD 율속(rate-limiting)은 약물 분류 라벨이 아니라 두 시간 척도의 비율($\tau_{drug}/\tau_{system}$)에서 결정되는 스펙트럼(spectrum)”이라는 framing을 직접 가르칩니다.** [R&T p.243–244, Fig.8-11]

### D. 가정(Assumptions)

- AUEC 폐쇄형(closed form)은 일반 $E_{max}$ + 1차 제거(first-order elimination) 조건에서만 출처에 근거합니다. [G&W p.233]
- 지속 시간-로그 용량 관계(duration log-dose relation)는 최소 유효량(minimum effective amount), 1차 감소(first-order decline), 일정한 역치(threshold) 등의 조건을 전제로 합니다. [R&T p.254–255]
- PD 율속 예시(PD-rate-limited example)는 “약물이 아직 많다”가 아니라 “시스템(system)이 아직 회복되지 않았다”는 뜻일 수 있습니다. [R&T p.249–253]

### E. 한계(Limitations)

Aspirin 75 mg, 수술 전후 7일 중단, 출혈 가이드라인은 본 PDF 출처 밖이므로 삭제합니다. 이 세션에서 출처 기반으로 고정되는 aspirin 문장(source-grounded aspirin statement)은 650 mg oral, $t_{1/2}$ 15 min, 항혈소판 활성(antiplatelet activity) several days까지만입니다. [R&T p.251]

특수 집단 용량 조정(special population dose adjustment)에서 PK 변화만 보고 투여 간격을 정하면 PD 율속 약물에서는 과소 또는 과대 조정이 생길 수 있습니다. 단, 특정 label/guidance 조항은 본 PDF 범위 밖입니다. 따라서 해당 적용은 `[확인 필요 — 교과서 외 규제 적용]`으로 남깁니다.

<!-- TRENCH -->
**[실무 팁(Trench-Level Tip)]** 도표(plot)의 x축(x-axis)이 한 자리 이상 다른 시간 단위로 벌어지면 PD 율속(PD-rate-limited) 가능성이 큽니다. Aspirin은 혈장 도표(plasma plot)가 hours, 항혈소판 효과 도표(antiplatelet effect plot)가 days scale로 보입니다. 따라서 “농도 주도 지속 시간(concentration-driven duration)”이라는 직관을 즉시 버려야 합니다. [R&T p.251]

**[실무 팁(Trench-Level Tip)]** 용량-반응이 고용량에서 평탄해지면 더 높은 용량이 정보를 늘리는 것이 아니라 고원부를 반복 확인할 가능성이 큽니다. Methylprednisolone처럼 PK AUC는 증가해도 PD 반응이 포화되면 하류 바이오마커(downstream biomarker) 또는 투여 간격 종말점(dosing interval endpoint)을 다시 설계합니다. [R&T p.257–258] `[실무 구현 번역]`

### F. 제텔카스텐 원자 노트(Zettelkasten Atom)

**원자 노트 C5(Atom C5):** AUEC와 지속 시간은 농도-시간 곡선을 반응-시간 곡선으로 번역한 면적·시간 지표입니다. 효과 지속성(effect persistence)은 약물 반감기가 아니라 더 느린 과정이 결정합니다.

<!-- RECAP -->
**요약(Recap):** C5는 “농도가 없어졌는데 효과가 남는다”는 현상을 예외가 아니라 PD 모델링의 핵심 설계 문제로 바꿉니다.

> **실패 모드(Failure Mode) — [TEXTBOOK_DERIVED]**  
> 효과 지속 시간을 혈장 반감기만으로 요약하면 PD 율속 약물에서 가장 중요한 회복 과정을 지워버립니다. 지속 시간 또는 AUEC를 보고할 때는 어떤 역치(threshold), 어떤 반응 변수(response variable), 어떤 시간 척도(time scale)에서 정의했는지 함께 고정해야 합니다.

> **실무 체화 요약(Practice Brief) — C5 — [EXPERT_INFERENCE, v3]**  
> 새 약물의 투여 간격을 설계할 때 던질 결정 트리: (1) **혈장 $t_{1/2}$ vs 반응 회복 시간의 비율($\tau_{drug}/\tau_{system}$)을 한 자리 수 단위로 비교** — 비슷하면 PK 율속, 한 자리 이상 차이 나면 PD 율속 확정, (2) **PD 율속이면 투여 간격은 혈장 동역학(plasma kinetics)이 아니라 시스템 회복 척도(system recovery scale)에 따라 결정**(omeprazole, aspirin이 매일 투여인 본질적 이유), (3) **AUEC 또는 지속 시간 보고 시 역치·반응 변수·시간 척도를 동시 명시**. 임상약사 출신이라면 warfarin INR 모니터링 주기가 혈장 $t_{1/2}$가 아니라 프로트롬빈 복합체 전환에 묶여 있다는 사실을 떠올리면 됩니다.

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.251 Fig.8-20; p.252 Fig.8-21
Why this matters: 이 예시들은 혈장 반감기(plasma half-life)와 효과 지속 시간(effect duration)을 반드시 분리해서 보게 합니다. 시각적으로 드러나는 시간축의 간격이 핵심 구조 신호입니다.
When to look: Card C5 §C를 읽은 뒤 확인하면 됩니다.
Learner instruction: 혈장 농도 시간 경과(plasma concentration time course)와 반응 시간 경과(response time course)를 비교하세요. 이 그림에서 aspirin의 수술 전후 지침이나 omeprazole의 임상 규칙을 추론하지 마세요. 이 그림은 PD 율속 지속성(PD-rate-limited persistence)을 알아보는 용도로만 사용하면 됩니다.
<!-- /FIGURE_POINTER -->

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.255 Fig.8-23; p.256 Fig.8-24
Why this matters: 지속 시간 식은 간결하지만, 학습자는 용량 변화가 역치 통과 시간(threshold-crossing time)으로 어떻게 번역되는지 직접 보아야 합니다. Fig.8-24는 이 추상적 관계를 succinylcholine 예시에 고정해 줍니다.
When to look: Card C5 §B를 읽은 뒤 확인하면 됩니다.
Learner instruction: 각 용량 곡선이 최소 유효량/효과 역치(minimum effective amount/effect threshold)를 어디에서 통과하는지 따라가 보세요. 그런 다음 그 통과 시간을, 명시된 가정 아래에서 용량을 두 배로 늘리면 지속 시간이 약 한 번의 반감기만큼 연장될 수 있다는 문장과 연결하면 됩니다.
<!-- /FIGURE_POINTER -->


---

# §5 — 혼동 쌍 해부

## 혼동 쌍 1(Pair 1) — $K_d$ vs $EC_{50}$

<!-- CONFUSION -->
| 비교 축 | $K_d$ | $EC_{50}$ |
|---|---|---|
| 본질 | 약물-표적 복합체의 결합 친화도(binding affinity) | 약물 + 조직/시스템의 기능적 감수성(functional sensitivity) |
| 변화 원인 | 리간드-수용체 결합 변화 | 결합, 수용체 밀도, 증폭 이득, 조직 반응 변화 모두 가능 |

**⚡ 기억 고리 (Memory Hook) — *결합 vs 효능*: [EXPERT_INFERENCE, v3]**  
$K_d$는 약물이 수용체에 *얼마나 잘 붙는가* — 분자 수준의 친화도입니다. $EC_{50}$는 *그 결합이 조직과 신호 시스템을 거쳐 절반의 효과로 나오기까지 필요한 농도* — 시스템 수준의 효능입니다. 둘이 다를 수 있는 이유는 수용체 점유율(receptor occupancy)과 기능적 반응(functional response) 사이에 여분 수용체(spare receptor)와 연쇄 증폭(cascade amplification)이라는 증폭 단계가 끼기 때문입니다. 따라서 $EC_{50}<K_d$도 가능합니다 — *수용체 10%만 점유해도 90% 효과가 나오는* 조직(tissue)이 존재하기 때문입니다. **결합은 분자, 효능은 시스템 — 같은 층위가 아닙니다.**

**핵심 교정(Critical Correction):** $EC_{50}$가 공변량에 따라 변하면 그것이 약물 측 결합(drug-side binding) 변화인지 시스템 측 감수성(system-side sensitivity) 변화인지 구분해야 합니다. 비결합 농도와 결합 증거(binding evidence) 없이 총 $EC_{50}$ 변화만으로 기전을 단정하지 않습니다. 이 구분이 없으면 공변량 효과를 생물학적 감수성 변화로 과해석하기 쉽습니다. [G&W p.203–206, p.215–217]

## 혼동 쌍 2(Pair 2) — 일반 $E_{max}$ ($n=1$) vs Sigmoid $E_{max}$ ($n\neq1$)

<!-- CONFUSION -->
| 비교 축 | 일반 $E_{max}$ | Sigmoid $E_{max}$ |
|---|---|---|
| 곡선 형태 | 쌍곡선형, 완만한 전환 | 더 급하거나 완만한 전환 가능 |
| 파라미터 | $E_{max}$, $EC_{50}$ | $E_{max}$, $EC_{50}$, $n$ |
| 위험 | 고원부 없는 데이터에서 $E_{max}$ 식별 불안정 | 농도범위가 좁으면 $n$ 식별 불안정 |

**⚡ 기억 고리 (Memory Hook) — *중간점 vs 가파름*: [EXPERT_INFERENCE, v3]**  
$EC_{50}$은 곡선의 **중간점 위치(midpoint)**입니다 — x축 위에서 반응의 절반이 나오는 농도, 즉 *어디에서* 효과의 절반에 도달하는지를 말합니다. Hill $\gamma(=n)$은 곡선의 **가파름(steepness)**입니다 — $\gamma$가 1이면 완만한 S자, $\gamma$가 5면 거의 계단 함수에 가까우며, 즉 *얼마나 좁은 농도 구간에서* 0%에서 100%로 전환되는지를 말합니다. 두 파라미터는 수학적으로 독립입니다 — $EC_{50}$이 낮아도(sensitive) $\gamma$가 낮으면(완만) 임상 허용 폭이 넓고, $EC_{50}$이 높아도(potency 낮음) $\gamma$가 높으면(가파름) 작은 농도 차이가 독성/무효의 경계를 가릅니다. **협역 치료역 약물에서 임상적으로 더 위험한 파라미터는 $EC_{50}$이 아니라 $\gamma$입니다 — 위치보다 가파름이 안전 마진을 결정합니다.**

| **치명적 타격 (Critical Blow) — [EXPERT_INFERENCE, v3]** | Hill $\gamma$를 보고서에서 생략하고 $EC_{50}$만으로 dose-response를 제출하면, 협역 치료역 약물(면역억제제, 항부정맥제, 일부 vitamin K antagonist)에서 위험이 생깁니다. 이러한 약물은 용량-반응 전환이 급격하므로, $\gamma$ 없이 설계된 임상 용량 조절 가이드는 *과관대하게* 설정되어 독성 발생률을 과소예측할 수 있습니다. 규제 심사관은 "Hill coefficient의 임상적 의의" 섹션을 추가하라는 deficiency를 발행하는 것이 일반적인 관행이며, 이는 NDA/BLA 검토 일정의 직접 지연으로 이어집니다. `[교과서 외 규제 해석]` |

$n>1$은 "협동성 증명(cooperativity 증명)"이 아닙니다. 이는 가설을 제시할 수 있지만 증명하지는 않는 현상학적 가파름 파라미터(phenomenologic steepness parameter)입니다. [G&W p.216, p.220]

## 혼동 쌍 3(Pair 3) — PK 율속 vs PD 율속 감소

<!-- CONFUSION -->
| 비교 축 | PK 율속(PK-rate-limited) | PD 율속(PD-rate-limited) |
|---|---|---|
| 율속 과정 | 약물 제거/분포 | 수용체 결합, 비가역적 작용, 전환, 하류 회복 |
| 도표 신호 | 혈장과 반응이 유사한 시간 척도 공유 | 혈장 시간 척도와 반응 시간 척도가 괴리 |
| 예시 | Succinylcholine 1차 감소 하 용량-지속 시간 | Aspirin, omeprazole, paclitaxel |

**치명적 타격(Critical Blow):** 약물 반감기가 짧다고 해서 효과 지속 시간도 짧다고 결론지으면, PD 율속 약물에서는 틀린 판단이 됩니다. Aspirin은 혈장 $t_{1/2}$ 약 15 min이지만 항혈소판 활성은 수일간 지속됩니다. Omeprazole도 혈장은 빠르게 사라지지만 위산 억제는 수일 척도로 회복됩니다. 따라서 투여 간격 판단에는 혈장 반감기뿐 아니라 반응 회복 시간(response recovery time)이 필요합니다. [R&T p.251–252]

> **Insertion I6 — [CRUCIBLE_DERIVED]** (Crucible Intuition #3 / Grade A: Time-axis fast-diagnostic)  
> **시각적 빠른 진단(Visual fast-diagnostic) — 0.5초 식별:** 도표(plot)의 x축(x-axis) 단위가 한 자리수 이상 차이 나면(예: aspirin 혈장 도표는 0–2 hours, 항혈소판 효과 도표는 0–192 hours) PD 율속(PD-rate-limited)으로 즉시 확정할 수 있습니다. 같은 시간축에서 두 곡선이 비슷한 모양이면 PK 율속(PK-rate-limited)입니다. **이 진단은 적합 통계량(fit statistic)이나 모델 비교 이전에 EDA 단계에서 도표의 시간 축만 보아도 가능합니다 — 두 도표가 *다른 시간 척도*에서 그려졌다는 사실 자체가 율속 과정(rate-limiting process)이 다르다는 직접 증거이기 때문입니다.** [R&T p.251–253; PD-rate-limited 시각 진단의 source anchor]

## 혼동 쌍 4(Pair 4) — 직접 연결 / 효과 구획 vs 간접 반응

<!-- CONFUSION -->
| 비교 축 | 직접 / 효과 구획(Effect Compartment) | 간접 반응(Indirect Response) |
|---|---|---|
| 지연 원인 | 혈장-작용 부위 평형화 또는 효과 부위 농도 | 내인성 반응 변수의 생성/소멸 | 
| 진단 | 효과 부위 농도로 히스테리시스가 줄어듦 | 최대 효과 시점이 시스템 전환에 의해 용량 비의존적일 수 있음 |
| 위험 | $k_{e0}$를 미시적 생리 상수(microscopic physiology)로 오해 | $k_{in}/k_{out}$을 단순 곡선 적합 파라미터로 오해 |

**빠른 진단(Fast Diagnostic):** 히스테리시스 고리의 폭과 최대 효과 시점의 용량 의존성을 먼저 봅니다. 용량 의존적 최대 효과 시점이면 효과 구획 가능성, 용량 비의존적 최대 효과 시점이면 간접 반응 가능성이 커집니다. 이 판단은 적합 통계량(fit statistic)보다 먼저 보는 구조 진단입니다. `[실무 구현 번역]`

<!-- RECAP -->
**요약(Recap):** 가장 위험한 혼동은 “농도가 반응(response)을 즉시 구동한다”는 가정입니다. 이 가정이 깨지는 순간 $K_d$/$EC_{50}$, $E_{max}$/Hill, 효과 구획/간접 반응(effect compartment/indirect response), PK/PD 율속(PK/PD rate-limiting)이 모두 연결됩니다.

> **체화 노트(Mastery Note) — [EXPERT_INFERENCE]**  
> 네 개의 혼동 쌍(confusion pair)는 모두 같은 질문으로 환원됩니다: “현재 숫자는 결합(binding), 부위 농도(site concentration), 측정 반응(measured response), 시스템 회복(system recovery) 중 어느 층위를 대표하는가?” 이 층위를 분리하면 파라미터 명명(parameter naming)은 단순 암기가 아니라 모델 구조 검토가 됩니다.

---

# §7 — 자기 테스트: 능동 회상 모듈

<!-- SELF-TEST -->
## Q1. 질량작용법칙에서 $E_{max}$ 식을 도출하세요.

**문제:** $d[RC]/dt=k_1[R][C]-k_{-1}[RC]$와 $[R_T]=[R]+[RC]$에서 $E=E_{max}\cdot C/(K_d+C)$를 도출하세요.

**정답:** 평형에서 $k_1[R][C]=k_{-1}[RC]$, $K_d=[C][R]/[RC]$. $[R]=[R_T]-[RC]$를 대입하면 $[RC]/[R_T]=C/(C+K_d)$. 여기에 $E=\alpha[RC]$, $E_{max}=\alpha[R_T]$를 대입하면 $E/E_{max}=C/(C+K_d)$가 됩니다. [G&W p.202–204]

## Q2. $K_d$와 $EC_{50}$가 다른 이유를 한 문장으로 설명하세요.

**정답:** $K_d$는 수용체 결합 친화도이고 $EC_{50}$는 수용체 점유 이후 조직 신호전달과 반응 증폭까지 포함하므로, 여분 수용체/증폭 연쇄가 있으면 $EC_{50}$는 $K_d$와 달라질 수 있습니다. [G&W p.204–206]

## Q3. Hill $n=2.03$을 “cooperativity 증거”라고 쓰면 왜 틀리는가?

**정답:** G&W는 Hill 지수(Hill exponent)가 직접적인 생물학적 해석(direct biological interpretation)을 갖지 않는다고 설명합니다. $n=2.03$은 PD3 데이터의 가파름(steepness)을 설명하는 파라미터이며, 협동성(cooperativity)은 가능한 가설(hypothesis)일 뿐 증명(proof)이 아닙니다. [G&W p.216, p.220, p.735]

## Q4. Sigmoid 억제 $I_{max}$ 모델에서 목표 반응을 해석할 때 기저치 상대값과 절대값을 구분하세요.

**문제:** $E=E_0-I_{max}\cdot C^n/(IC_{50}^n+C^n)$에서 목표 $E_{target}$이 주어졌을 때 어떤 값을 억제 분율(inhibition fraction)으로 넣어야 하는가?

**정답:** 절대 반응(absolute response)으로 주어진 $E_{target}$은 먼저 $I=E_0-E_{target}$으로 억제 크기(inhibition magnitude)를 계산합니다. 그 다음 $I/I_{max}$를 분율로 두고 농도를 역산합니다. 기저치 상대 반응(baseline-relative response)을 절대 반응처럼 넣으면 부호와 비율이 틀어집니다. [G&W p.218–221]

## Q5. Naproxen 히스테리시스에서 지지되지 않는 $k_{e0}$ 수치를 쓰지 말고, 출처에 근거한 결론만 말하세요.

**정답:** R&T는 naproxen 500 mg 경구 치과 통증 모델에서 비결합 농도와 통증 완화가 반시계 방향 히스테리시스를 보이고, 효과 구획이 이 히스테리시스를 줄이는 개념적 모델을 제시합니다. $k_{e0}\approx0.5–1\ \mathrm{hr}^{-1}$ 수치는 본 PDF 범위에서 확인되지 않으므로 쓰지 않습니다. [R&T p.234–246]

## Q6. Warfarin 반응이 혈장 농도를 즉시 따라가지 않는 이유는 무엇인가?

**정답:** Warfarin 효과는 프로트롬빈 복합체 전환에 의해 나타나므로 혈장 농도 변화와 반응 변화가 분리됩니다. R&T는 sodium warfarin 1.5 mg/kg 경구 투여 후 프로트롬빈 복합체 활성이 시스템 전환 반감기의 영향을 받는 예를 제시합니다. [R&T p.242, p.247]

## Q7. AUEC 폐쇄형 식의 적용 조건을 말하세요.

**정답:** G&W의 $AUEC=\frac{E_{max}}{K}\ln\left(1+\frac{D}{EC_{50}\cdot V}\right)$는 일반 $E_{max}$와 1차 제거 조건에서 출처에 근거합니다. Sigmoid $E_{max}$의 AUEC 수치 적분(numerical integration)은 합리적 수학 추론이지만 본문에 폐쇄형으로 제시된 출처 사실은 아닙니다. [G&W p.233–234]

## Q8. Aspirin과 omeprazole 예시로 PD 율속 지속 시간을 설명하세요.

**정답:** Aspirin 650 mg 경구는 혈장 $t_{1/2}$가 약 15 min이지만 항혈소판 활성이 수일간 지속됩니다. Omeprazole 40 mg 경구는 혈장 $t_{1/2}$가 1시간 미만이고 약 3시간 후 혈장이 거의 사라지지만 위산 억제는 수일 척도로 회복됩니다. 두 예시는 효과 지속 시간이 약물 반감기가 아니라 시스템/수용체 회복에 의해 제한될 수 있음을 보여줍니다. [R&T p.251–252]

## Q9. 보스 딜레마(Boss Dilemma) — Phase 2 PK/PD 데이터셋에서 반시계 방향 히스테리시스가 보입니다. 혈장 직접, 효과 구획, 간접 반응 중 어떤 순서로 검토할 것인가?

**정답:** 먼저 혈장 직접 모델(plasma direct model)로 모델 오명세(misspecification)의 크기를 봅니다. 다음으로 효과 구획을 적용해 히스테리시스가 줄어드는지 확인합니다. 그래도 용량 군별 최대 효과 시점이 용량 비의존적이거나 반응 회복이 시스템 시간 척도를 보이면 간접 반응을 검토합니다. 즉, 모델 선택은 AIC만으로 하지 않습니다. 최대 효과 시점의 용량 의존성, 채혈 밀도(sampling density), 생물학적 타당성(biological plausibility)을 함께 봅니다. `[실무 구현 번역]`

---

# §8 — 메타 프레임과 큰 그림

## A. 위치와 실패 모드

이 세션은 PK/PD 구조(PK/PD architecture)에서 “농도-시간 프로파일(concentration-time profile)을 반응-시간 프로파일(response-time profile)로 변환하는 첫 관문”입니다. C1–C2는 농도-반응 비선형성(concentration-response nonlinearity)을 담당합니다. C3–C4는 시간 지연(time delay)을, C5는 반응 적분/지속 시간(response integration/duration)을 담당합니다.

이 세션을 대충 넘기면 다음 실패가 발생합니다.

1. **$K_d$를 $EC_{50}$처럼 사용:** 결합 친화도를 기능적 역가(functional potency)로 오인합니다.
2. **Hill $n$을 기전 증명으로 과해석:** 곡선 적합 파라미터를 생물학적 증거로 둔갑시킵니다.
3. **히스테리시스를 잡음으로 처리:** 부위 평형화 또는 전환 지연을 놓칩니다.
4. **PK 반감기로 투여 간격을 결정:** PD 율속 반응에서 지속 시간을 잘못 예측합니다.
5. **AUEC를 단순 AUC처럼 취급:** 반응 적분의 모델 조건을 잊습니다.

## B. 전문가 해석 지점

계량약리학자(pharmacometrician)의 해석 지점은 복잡한 식을 많이 아는 데 있지 않습니다. 같은 농도-효과 데이터를 두고 무엇이 부족한지 구분할 줄 아는 데 있습니다. 더 좋은 최적화기(optimizer)가 필요한가, 더 넓은 농도 범위가 필요한가, 더 가까운 바이오마커가 필요한가, 아니면 더 긴 반응 채취(response sampling)가 필요한가 — 이 네 갈래를 구분할 줄 알아야 합니다.

PD3는 이 해석 지점의 좋은 예입니다. 0–500 µg/L 설계에서는 sigmoid 우월성이 명확하지 않습니다. 그러나 0–800 µg/L 설계는 모델 판별(model discrimination)을 가능하게 합니다. 이는 모델 선택이 통계기법 문제만이 아니라 실험 설계(experimental design) 문제임을 보여줍니다. [G&W p.734–741]

R&T Ch.8은 또 다른 해석 지점을 줍니다. 혈장 농도가 낮아졌는데 효과가 남아 있을 때 "약물이 없는데 효과가 이상하게 남았다"고 보지 않습니다. 대신 "시스템 전환 또는 비가역적 작용(irreversible action)이 더 느린 과정인가?"를 묻습니다. [R&T p.249–253]

> **Hill $\gamma$의 임상 함의 — Apex 파라미터로서의 위상 — [EXPERT_INFERENCE, v3]**  
> 이 세션의 Apex 개념인 Hill $\gamma$는 단순한 곡선 모양 파라미터가 아니라 임상 의사결정의 정밀도 자체를 결정하는 양입니다. 임상약사 출신 모델러가 가장 빠르게 체득할 수 있는 moat는, 다음 세 가지를 보고서에서 명확히 분리해 기술하는 능력입니다.
> - **$\gamma$ > 1의 임상적 의미:** 농도-반응 관계에 *역치 특성(threshold-like behavior)*이 생깁니다. $EC_{50}$ 근처에서 소량의 농도 변화가 큰 반응 변화를 일으키므로 — 같은 약물이라도 $\gamma$가 높을수록 치료역(therapeutic window)이 *수학적으로* 좁아집니다. $\gamma$는 약물이 협역인지 광역인지를 정량화하는 가장 직접적인 파라미터입니다.
> - **용량 조절 정밀도 요구의 정량화:** $\gamma$가 높은 약물은 용량을 조금만 올려도 독성 범위에 진입합니다. TDM 목표 농도(target concentration)를 폭넓게 설정하면 과소치료와 독성 사이를 오갑니다. 8년의 vancomycin/tacrolimus/aminoglycoside TDM 경험에서 알듯이, 같은 trough range가 약물에 따라 임상적 의미가 다른 본질적 이유가 바로 $\gamma$입니다.
> - **Exposure-response 보고서의 필수 항목:** 보고서에 $\gamma$ 추정치와 confidence interval을 반드시 명시해야 합니다 — $\gamma$ 추정의 불확실성이 투여 용량 결정의 불확실성으로 *직접* 전파되기 때문입니다. $\gamma$가 보고서에 없다는 것은 임상적으로 가장 중요한 한 정보를 누락한 것과 같습니다. `[교과서 기반 + 교과서 외 규제 해석]`

## C. 경계 플래그 보존

[확인 필요 — 첨부 PDF 미포함 구간]:
- G&W §3.6.2–§3.6.5 (pp.225–228): competitive antagonism 이후 interaction model 연속부. 본 세션에서 추정·보완하지 않음.
- G&W §3.12 baseline modeling: C2 limitation에서 baseline time-varying issue로만 언급. 본 세션에서 상세 모델링 보류.
- `[확인 필요 — 교과서 외 규제 적용]`: PD 율속 약물(PD-rate-limited drug)의 특수 집단 용량 조정(special population dose adjustment)이나 FDA guidance 문구는 본 PDF 범위 밖이므로 일반 원칙으로만 유지.

<!-- RECAP -->
**최종 요약(Final Recap):** 이 세션의 압축 결론은 세 문장입니다.  
1. $E_{max}$/Hill 모델은 수용체 결합에서 시작하지만 반응 시스템을 포함합니다.  
2. 히스테리시스는 혈장 농도가 효과를 즉시 대표하지 못한다는 시각적 경고입니다.  
3. 지속 시간과 AUEC는 약물 반감기보다 더 느린 생물학적 과정을 찾아야 제대로 해석됩니다.

> **실무 렌즈(Practice Lens) — [EXPERT_INFERENCE]**  
> 이 세션을 HTML로 학습할 때 최종 목표는 식을 외우는 것이 아니라 “이 데이터로 어떤 질문은 방어 가능하고, 어떤 질문은 아직 설계가 부족한가?”를 말할 수 있게 되는 것입니다. $E_{max}$/Hill, 히스테리시스(hysteresis), AUEC는 모두 모델 결과가 아니라 연구 설계(study design)의 충분성을 되묻는 언어입니다.

---

## PART B — Compiler-Only Appendix

This appendix is not learner-facing. It exists only to protect Phase 5 rendering fidelity.

### B1. Compilation Contract

- PART A is the only learner-facing body.
- Phase 5 must render PART A without altering the scientific content, equations, page tags, figure marker content, or mastery-note labels.
- PART B is instruction/guardrail only and must not appear as learner content unless explicitly requested.
- Do not restore deprecated material from Step 1 Draft v0.
- Do not add new scientific content, new examples, new page tags, new figures, or new regulatory claims during HTML compilation.
- Do not generate HTML, Mermaid, or SVG at Phase 4D; Phase 5 handles rendering.
- ver2 Insertion blocks (I1–I6) are labeled bounded blocks with explicit source basis (TEXTBOOK_DERIVED / CRUCIBLE_DERIVED). Phase 5 should render them with the same Mastery Note callout style as existing labeled augmentations; do not strip the labels.

### B2. Figure Rendering Instructions

**Image rights:** None. Do not embed copyrighted textbook figures. Render `FIGURE_POINTER` as text-only callouts. Render `FIGURE_SCHEMATIC` as structurally distinct redraws based only on the brief.

| # | Mode | Source | Phase 5 action | Decision |
|---|---|---|---|---|
| 1 | P | G&W p.199 Fig.3.1 | Text-only textbook pointer | KEEP |
| 3 | R | G&W p.204 Fig.3.4; p.205 Fig.3.5 | Structurally distinct schematic brief | KEEP |
| 5 | P | G&W PD3 p.733 Fig.PD3-3.1; p.735 Table PD3-3.2; p.741 Table PD3-3.4 | Text-only textbook pointer | KEEP |
| 6 | P | R&T p.234 Fig.8-1; p.235 Fig.8-2 | Text-only textbook pointer | KEEP |
| 7 | R | R&T p.236 Fig.8-3 | Structurally distinct schematic brief | KEEP |
| 8 | P | R&T p.251 Fig.8-20; p.252 Fig.8-21 | Text-only textbook pointer | KEEP |
| 9 | P | R&T p.255 Fig.8-23; p.256 Fig.8-24 | Text-only textbook pointer | KEEP |
| 2 | P | G&W p.202 Fig.3.3 | Rejected as redundant within C1 budget | REJECT |
| 4 | P | G&W p.213 Fig.3.12; p.216 Fig.3.16 | Rejected as lower ROI than PD3 | REJECT |
| 10 | N | None | Rejected due to budget and drift control | REJECT |

Additional constraints:

- Preserve P/R/N/I decisions and all Source fields in marker blocks.
- Do not propose or generate new figures.
- Do not render rejected figure candidates #2, #4, or #10.
- Place rendered figures at the end of the relevant concept card unless the marker position already makes a safer local placement obvious.
- For redrawn schematics, preserve conceptual relation but avoid the textbook’s exact layout, color palette, and figure composition.

### B3. Page Tag Rendering Rules

- Preserve all existing `[p.XX]`, `[pp.XX–YY]`, `[pp.XX, YY]`, and `[p.확인 필요]` tokens.
- Do not fabricate, delete, renumber, or relocate page tags.
- Apply page-tag wrapping only to body text; do not wrap tags inside code blocks or inside `FIGURE_*` marker blocks.
- Source page tags must remain visible in print mode.
- `[확인 필요 — 첨부 PDF 미포함 구간]` remains visible unless a later verified source explicitly resolves it.
- ver2 Insertion blocks reuse existing page tags only; no new page numbers were introduced in I1–I6.

### B4. HTML Compiler Requirements

#### Marker-to-component mapping

| Marker / Pattern | HTML Component | Required handling |
|---|---|---|
| `<!-- MASTER LENS -->` | Callout box | border-left gold; low-opacity gold background |
| `<!-- ANNOTATION -->` | Inline annotation / tooltip style | muted italic small text |
| `<!-- ANCHOR -->` | Bridge sentence | muted italic text |
| `<!-- TRENCH -->` | Practical tip box | rose-left-border callout |
| `<!-- CONFUSION -->` | Side-by-side comparison | amber comparison component |
| `<!-- SELF-TEST -->` | Accordion | prompt visible; answer hidden until click |
| `<!-- RECAP -->` | Recap box | blue-left-border summary |
| `[확인 필요]` | Highlighted flag | render with `<mark>` |
| `[p.XX]`, `[pp.XX–YY]`, `[pp.XX, YY]` | Inline source-page tag | wrap in `<span class="source-page">…</span>` |
| `[p.확인 필요]` | Uncertain source tag | wrap in `<span class="source-page source-uncertain">…</span>` |
| `<!-- FIGURE_POINTER -->` | Text-only textbook reference callout | never embed textbook image |
| `<!-- FIGURE_SCHEMATIC -->` | Inline schematic `<figure>` | generate visually distinct Mermaid/SVG/CSS from brief only |
| `<!-- FIGURE_IMAGE_SLOT -->` | Image/placeholder figure | not used in this session unless user-supplied/open-license file exists |
| `> **Insertion I[1-6]` blockquotes | Mastery Note callout (gold-left-border) | render same as existing `> **Mastery Note —`, `> **Practice Lens —`, `> **Failure Mode —` blocks; preserve the source-basis label `[TEXTBOOK_DERIVED]` / `[CRUCIBLE_DERIVED]` exactly |
| `> **⚡ Plausible Fallacy —` blockquotes | Apex-only Fallacy callout | gold-left-border with red ⚡ accent; render with bold "그럴듯한 오해 / 왜 틀렸는가 / 실무에서 어떻게 드러나는가" sub-labels intact (v3 only on Apex card) |
| `> **⚡ 기억 고리 (Memory Hook) —` blockquotes | Memory Hook callout | gold-left-border with ⚡ accent; render the italic dash-flanked subtitle (예: *결합 vs 효능*, *중간점 vs 가파름*) as visible kicker (v3 표준 블록) |
| `> **Practice Brief —` blockquotes | Practice Brief callout | rose-left-border (Trench-Tip 계열과 시각적 구분); preserve the `[EXPERT_INFERENCE, v3]` source-basis label exactly |
| `\| **치명적 타격 (Critical Blow) —` table row | Critical Blow row | render in red/crimson background within the surrounding confusion-pair table; bold the leading "치명적 타격" label; preserve the `[EXPERT_INFERENCE, v3]` or `[교과서 외 규제 해석]` source-basis label exactly |

#### Rendering, navigation, interaction, and output requirements

- Render PART A only as learner-facing content; do not render PART B unless explicitly requested.
- Produce one self-contained HTML file with inline CSS/JS.
- Preserve text content; do not rewrite scientific body, equations, examples, or page tags.
- MathJax: support inline and display equations.
- Navigation: sticky left sidebar TOC on desktop; mobile-collapse allowed; each major § heading and each §2 concept card should have stable unique ids.
- Navigation anchor integrity: every sidebar `href="#id"` must match exactly one body `id`; no duplicate ids; `html { scroll-behavior: smooth; }` must be present.
- Self-test: render answer keys hidden by default and revealed on user click.
- Controls: code-copy button where code exists, print/PDF button via `window.print()`.
- Responsive/print: ≤768px single-column; hide navigation in print; preserve source-page tags in print.
- Figure pointers: render as text-only callouts with Source / Why this matters / When to look / Learner instruction.
- Figure schematics: render from brief only; do not reproduce textbook layout, color scheme, or exact figure.
- Mermaid self-check: use valid Mermaid syntax only; if node labels/special characters make Mermaid fragile, fall back to inline SVG or CSS cards.
- Allowed external runtime dependencies only: MathJax CDN, Mermaid CDN, and permitted highlighting libraries; no external local CSS/JS/font/image files.
- Prohibited: iframe/embed, unauthorized textbook images, visible self-test answers by default, raw markers left unrendered, raw page tags left unwrapped, duplicate/unstable ids, unmatched TOC targets, new figure ideas, or new scientific content.

### B5. Audit Guardrails

Do not restore or add any of the following:

- “5–100배 오차,” FIH dose overprediction, NDA recommended dose, FDA deficiency letter, clinical hold, or similar regulatory claims as source-derived statements.
- Hill `n` as direct proof of cooperativity, cascade, receptor-effector heterogeneity, or a named mechanism without orthogonal evidence.
- Aspirin 75 mg, 7–10 days, perioperative stopping rules, or bleeding-guideline claims; source scope supports aspirin 650 mg, plasma t1/2 about 15 min, antiplatelet effect several days only.
- Naproxen `ke0 ≈ 0.5–1 hr⁻¹` or any unverified effect-compartment numeric range.
- Untagged NONMEM `$DES`, grid-search, IIV-on-EC50/Emax/n, reviewer-deficiency, or submission consequences as textbook facts.
- G&W §3.6.2–§3.6.5 content from pp.225–228; keep `[확인 필요 — 첨부 PDF 미포함 구간]` rather than reconstructing.
- New page tags, new named drug examples, unapproved code blocks, unapproved figures, or copyrighted textbook image embedding.

### B6. Crucible Guardrails

- Crucible is a judgment/insight source, not a raw learner-prose source at Phase 4D.
- Preserve only adopted or explicitly allowed Grade A logic: Hill `n` as titration/design lever, IDR peak-time diagnostic logic, `ke0` as lumped/phenomenologic delay, PD3 concentration-range design lesson, and PK/PD rate-limiting as a relative time-scale problem.
- ver2 additionally adopts Crucible Intuition #2 (precision-improvement diagnostic, Insertion I3) and Intuition #3 (time-axis fast-diagnostic, Insertion I6) — both are CRUCIBLE_DERIVED and labeled accordingly.
- Do not turn expert inference into textbook-derived fact.
- Do not add unsupported numeric expert claims from Crucible unless already present in Content Lock v2 and properly tagged.
- Do not reintroduce lower-priority, speculative, external, or rejected Crucible material.

### B7. Deprecated and Forbidden Restorations

- Step 1 Draft v0 is deprecated and must not be used as a learner-body source except through the Micro-Patch Gate.
- Content Lock v1 is superseded by Content Lock v2 and must not override the v2 body.
- Phase 1 Patch Memo is contextual only; it must not override Audit v1 or Content Lock v2.
- Do not restore rejected overclaims, unsupported numbers, unsupported regulatory claims, source-unsupported examples, unapproved code, unapproved figures, or any NOT_IN_SOURCE item rejected by Audit/Content Lock.
- ver1 master is superseded by ver2 only with respect to the six labeled insertions; all other content is identical.

### B8. PATCH MODE Splice Verification Table

| Marker # | Anchor text | Anchor found? | Match count | Inserted? | Final location (§ + card) |
|---|---|---|---|---|---|
| 1 | # §1 — Session Header & Roadmap | YES | 1 | YES | §1 — Session Header & Roadmap |
| 2 | ## Card C1 — Law of Mass Action → Emax 골격 | YES | 1 | YES | §2 / Card C1 |
| 3 | ## Card C2 — Sigmoid Emax / Hill Model [⚡ Apex Concept] | YES | 1 | YES | §2 / Card C2 |
| 4 | ## Card C3 — Hysteresis: 시간 지연의 진단 도구 | YES | 1 | YES | §2 / Card C3 |
| 5 | ## Card C4 — Effect Compartment + Systems-in-flux / Indirect… | YES | 1 | YES | §2 / Card C4 |
| 6 | ## Card C5 — AUEC + Duration + PK/PD Rate-Limiting | YES | 1 | YES | §2 / Card C5 |
| 7 | ## Card C5 — AUEC + Duration + PK/PD Rate-Limiting | YES | 1 | YES | §2 / Card C5 |

#### ver2 Insertion Splice Verification

| Insertion # | Anchor text (truncated) | Anchor found? | Match count | Inserted? | Final location |
|---|---|---|---|---|---|
| I1 | "Ideal PD measure는 sensitive, gradual, meaningful…" (end of §1 first paragraph) | YES | 1 | YES | §1 — after Big Idea paragraph |
| I2 | `[출처: G&W p.219, Eq.3:38–3:42]` (end of §B Parameter Recovery code-fence line) | YES | 1 | YES | §2 / Card C2 / §B — before PD3 anchor paragraph |
| I3 | "Hill `n`을 "positive cooperativity가 증명되었다"라고…" (end of §C-2 paragraph 2) | YES | 1 | YES | §2 / Card C2 / §C-2 — after closing fallacy paragraph |
| I4 | `$$\nAUEC=\int_0^{\infty}E(t)dt\n$$` (end of §A first display equation) | YES | 1 | YES | §2 / Card C5 / §A — between AUEC definition and closed form |
| I5 | "Acenocoumarol과 phenprocoumon 비교에서는…[R&T p.243–244]" (end of §C last paragraph) | YES | 1 | YES | §2 / Card C5 / §C — after acenocoumarol paragraph |
| I6 | "따라서 dosing interval 판단에는 plasma half-life뿐 아니라 response recovery time이 필요하다. [R&T p.251–252]" (end of Pair 3 Critical blow paragraph) | YES | 1 | YES | §5 / Pair 3 — after Critical blow paragraph |

### B9. Zero-Omission Coverage Matrix — v3

| Domain | Required item | Evidence in PART A | Status | Action |
|---|---|---|---|---|
| C1 Scope Lock Required Concepts | C1 Mass Action/Emax; C2 Sigmoid Emax/Hill; C3 Hysteresis; C4 Effect Compartment/IDR; C5 AUEC/Duration | PART A §1 roadmap and §2 C1–C5 cards | PRESENT | None |
| C2 Scope Lock Required Data Anchors | PD3 E0/Imax/IC50/n; Lundström composite Imax values; R&T examples including digoxin, naproxen, warfarin, aspirin, omeprazole, succinylcholine, paclitaxel, methylprednisolone, acenocoumarol/phenprocoumon | PART A C2, C3, C4, C5 and self-test Q5–Q8 + ver2 I5 (acenocoumarol/phenprocoumon anchor preserved verbatim in v3) | PRESENT | None |
| C3 Audit MUST_FIX | Unsupported 5–100×/FIH/NDA claims removed; Hill n mechanism proof downgraded; aspirin/naproxen/NONMEM regulatory overclaims controlled | PART A C1–C5, §5, §7; PART B guardrails | PRESENT | Regression forbidden in PART B |
| C4 Audit T5 Coverage — SHOULD_FIX | (a) Ideal PD measure + control + 2–4 dose levels; (b) R&T objectives in §1; (c) §3.6.6 framework bridge; (d) acenocoumarol/phenprocoumon as PK/PD rate-limiting anchor | (a) §1 + ver2 I2 in C2 §B; (b) ver2 I1 in §1; (c) ver2 I4 in C5 §A; (d) ver2 I5 in C5 §C | PRESENT (ver2) | All four SHOULD_FIX items closed |
| **C4-bis V5.0 Apex Framework Coverage — v3 (NEW)** | (a) Apex 마커 표준화 `[⚡ Apex Concept]`; (b) Plausible Fallacy 블록(Apex 1개); (c) §5 Memory Hook 표준화; (d) Critical Blow 행(최고 파급력 쌍 1개); (e) Big Idea 직관-우선 구조; (f) Practice Brief 라벨 | (a) §1 항법도 + §2 C2 header + B8 splice table; (b) §2 C2 §C-2 신규 블록; (c) §5 Pair 1·Pair 2 + §2 C2 §A 보조 hook; (d) §5 Pair 2 Critical Blow 행; (e) §2 C2 Big Idea 임상 직관 lead-in; (f) §2 C1·C3·C5 Practice Brief 블록 | PRESENT (v3) | All six framework items closed by P1–P6 |
| C5 Figure Coverage | Phase 4C KEEP items #1, #3, #5, #6, #7, #8, #9 | PART A contains 5 FIGURE_POINTER and 2 FIGURE_SCHEMATIC markers exactly once | PRESENT | No image embedding; rejected #2/#4/#10 not restored |
| C6 Page Tag Integrity | Preserve G&W/R&T page tags and uncertainty flags | PART A inherited v2 source tags; B3 enforces rendering without fabrication; ver2 insertions reuse existing page tags only; v3 patches add no new page tags | PRESENT | No new page tags added in v3 |
| C7 Crucible Grade A Preservation | Dose-invariant peak time, Hill n as titration lever, ke0 as lumped delay, PD3 design range, PK/PD rate-limiting ratio, Intuition #2 (precision improvement), Intuition #3 (time-axis fast-diagnostic) | PART A C2/C4/C5 plus mastery notes; ver2 I3 (Intuition #2) and I6 (Intuition #3) preserved in v3; v3 P5 adds Hill γ clinical implications | PRESENT (v3 expanded) | Two Grade A intuitions explicit + γ clinical moat |
| C8 Deprecated Draft Regression | Step 1 rejected material not restored | PART A uses Content Lock v2 base; B5/B7 prohibit restorations; v3 adds no rejected material | PRESENT | None |
| C9 Canonical Body Integrity | Content Lock v2 learner body retained with approved 4C markers plus labeled augmentations | PART A §1–§8; B8 splice verification incl. ver2 insertions; v3 patches are additive labeled blocks; no body sentence rewritten | PRESENT | No broad rewrite; v3 added 7 labeled patches only |
| **C10 Non-Negotiable Preservation — v3 (NEW)** | (a) Acenocoumarol/phenprocoumon I5 verbatim; (b) Q9 Boss Dilemma verbatim; (c) all page tags preserved; (d) all v3 additions tagged `[EXPERT_INFERENCE, v3]` | (a) §2 C5 §C I5 block 검증; (b) §7 Q9 검증; (c) page tag 회귀 검증 (pre/post diff); (d) v3 패치 7개 라벨 검증 | PRESENT (v3) | Hard preservation rule satisfied |

### B10. Micro-Patch Log

ver1: No micro-patches needed.  
ver2: No micro-patches in the body. All ver2 changes are explicit, labeled insertion blocks (I1–I6) and corresponding PART B updates (certificate table, splice verification, coverage matrix, augmentation log). No source page tags were added or changed; no body sentence from Content Lock v2 was rewritten.  
v3: No micro-patches in the canonical body sentences. All v3 changes are explicit, labeled patch blocks (P1–P7) tagged `[EXPERT_INFERENCE, v3]`. v3 modifies (a) C2 header label `[Apex]` → `[⚡ Apex Concept]` (3 locations: §1 항법도, §2 header, B8 splice table — pure label standardization, no semantic shift), (b) Pair 1 in-table 기억 고리 row → standardized independent block (table-cell to blockquote elevation, content reworded structurally per V5.0 Memory Hook rule), (c) C1 §A `Emax`·`intrinsic activity` 첫 등장 ANNOTATION 보강 (parenthetical addition only, no source claim rewritten), (d) C5 §C `PK-rate-limited`·`PD-rate-limited` 첫 등장 ANNOTATION 보강 (parenthetical addition only). All other v3 changes are pure additions (new blocks, new rows, new bullets). No source page tags were added or changed.  
**v3.1: Korean Readability Patch — prose-only readability pass on PART A (KR-01 ~ KR-22, all Risk = Low).** v3.1 applies 22 surgical Korean-readability edits across §1, §2 (Cards C1–C5), §5 (Pairs 2 and 3), §7 (Q9), and §8 (Professional Moat + Hill γ block). Edit categories: (i) **Sentence split** (KR-01, KR-04, KR-08, KR-09, KR-15, KR-16) — long English-grammar Korean sentences split into 2 shorter Korean-natural sentences; (ii) **Korean flow improvement** (KR-02, KR-05, KR-07, KR-09, KR-10, KR-11, KR-12, KR-15, KR-16, KR-17, KR-18, KR-19, KR-20, KR-21) — passive/awkward predicates replaced with active Korean verbs; dangling subjects restored; English-Korean fragments harmonized; (iii) **First-use gloss** (KR-03 receptor conservation, KR-06 concentration ratio, KR-11 rising/falling phase, KR-12 tissue perfusion·permeability·binding kinetics·signal transduction lag) — Korean parenthetical added at first occurrence only, never repeated; (iv) **Concept clarification** (KR-06, KR-13, KR-22) — meaning preserved but expressed more concretely. **Strict non-modifications in v3.1:** no scientific claim altered; no equation, code block, or NONMEM syntax touched; no page tag added/removed/renumbered; no figure marker (`FIGURE_POINTER`, `FIGURE_SCHEMATIC`) altered; no HTML compiler marker (`<!-- MASTER LENS -->`, `<!-- ANNOTATION -->`, `<!-- TRENCH -->`, `<!-- CONFUSION -->`, `<!-- SELF-TEST -->`, `<!-- RECAP -->`, `<!-- ANCHOR -->`) touched; no source-basis label (`[EXPERT_INFERENCE, v3]`, `[TEXTBOOK_DERIVED]`, `[CRUCIBLE_DERIVED]`, `[교과서 외 규제 해석]`, `[실무 구현 번역]`, `[수학적 추론]`, `[교과서 기반 + 교과서 외 규제 해석]`) altered; no Insertion I1–I6 or Patch P1–P7 source-anchored sentence rewritten in a way that changes its anchored claim; Acenocoumarol/Phenprocoumon Insertion I5 preserved verbatim; Q9 Boss Dilemma Answer key receives only KR-19 ("다음" → "다음으로") which does not change the dilemma's clinical/regulatory content; PART B compilation contract unchanged; Phase 5 marker-to-component mapping unchanged; B8 Splice Verification unchanged.
**v3.2: Korean-Dominant Readability Patch — systematic Korean-dominance pass on PART A.** v3.2 goes beyond v3.1's surgical edits by systematically converting all remaining learner-facing English prose to Korean and applying `한글(English)` paired-term formatting to career-critical pharmacometrics terms. Edit scope: all §1–§8 PART A sections. Edit categories: (i) **Section header Koreanization** — all English-only sub-headers (Formal Definition, Derivation, Structural Necessity, Assumptions & Boundary Conditions, Limitations, Zettelkasten Atom, etc.) receive `한글(English)` paired format; (ii) **Prose Koreanization** — general English phrases (receptor occupancy, functional sensitivity, binding assay, etc.) converted to Korean with first-use `한글(English)` pair; subsequent uses in Korean only; (iii) **Label Koreanization** — Recap→요약(Recap), Mastery Note→숙련 노트, Practice Brief→실무 체화 요약, Failure Mode→실패 모드, Practice Lens→실무 관점, Trench-Level Tip→실무 팁, Answer key→정답, Prompt→문제, Critical correction→핵심 교정, Critical blow→치명적 타격, Fast diagnostic→빠른 진단, Learner Navigation Aid→학습자 내비게이션 안내; (iv) **Table header Koreanization** — Axis→비교 축, Curve→곡선 형태, etc. **Strict non-modifications in v3.2:** no scientific claim, equation, numerical anchor, code block, NONMEM syntax, page tag, figure marker, source-basis label, HTML compiler marker, section/card structure, or PART B guardrail altered. All Insertion I1–I6 and Patch P1–P7 source-anchored claims preserved in meaning (only surrounding prose Koreanized). Acenocoumarol/Phenprocoumon Insertion I5 preserved verbatim. Q9 Boss Dilemma clinical/regulatory content preserved. B8 Splice Verification table unchanged. B4 Marker-to-component mapping unchanged.

### B11. Mastery Augmentation Log — v3

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
|---|---|---|---|---|---|---|
| 1 | §2 / Card C1 | J | True | AUDIT_DERIVED | Kd–EC50 혼동 및 total/unbound 해석 과잉을 예방 | Low |
| 2 | §2 / Card C2 | J/F | True | CRUCIBLE_DERIVED + AUDIT_DERIVED | Hill n의 해석 경계와 설계 판단을 고정 | Low |
| 3 | §2 / Card C3 | M | True | TEXTBOOK_DERIVED | R&T hysteresis figure의 진단적 의미를 학습 동선으로 고정 | Low |
| 4 | §2 / Card C4 | J | True | CRUCIBLE_DERIVED | Effect compartment와 indirect response의 topology 구분을 강화 | Low |
| 5 | §2 / Card C5 | F | True | TEXTBOOK_DERIVED | AUEC/duration 정의와 PD-rate-limiting 오해 예방 | Low |
| 6 | §5 / Confusion Pair Dissection | M | True | EXPERT_INFERENCE | 혼동쌍을 하나의 층위 분리 mental model로 통합 | Medium |
| 7 | §8 / Meta-Frame | W | True | EXPERT_INFERENCE | 세션 전체를 모델링/설계 판단으로 연결 | Medium |
| **I1 (ver2)** | §1 / Roadmap | W | True | TEXTBOOK_DERIVED | R&T Ch.8 출발 메시지 명시화 — Audit T5-B SHOULD_FIX 종료 | Low |
| **I2 (ver2)** | §2 / Card C2 §B | W | True | TEXTBOOK_DERIVED | G&W p.200 design message anchor — Audit T3/T5-A SHOULD_FIX 종료 | Low |
| **I3 (ver2)** | §2 / Card C2 §C-2 | M | True | CRUCIBLE_DERIVED | IC50 CV 향상 진단 — Crucible Grade B Intuition #2 명시화 | Low |
| **I4 (ver2)** | §2 / Card C5 §A | W | True | TEXTBOOK_DERIVED | G&W §3.6.6 framework bridge — Audit T1 PARTIAL 종료 | Low |
| **I5 (ver2)** | §2 / Card C5 §C | W | True | TEXTBOOK_DERIVED | Acenocoumarol/Phenprocoumon spectrum anchor — Audit T6 ESSENTIAL 강화 | Low |
| **I6 (ver2)** | §5 / Pair 3 | M | True | CRUCIBLE_DERIVED | 시간축 한 자리 차이 fast-diagnostic — Crucible Grade A Intuition #3 명시화 | Low |
| **P1 (v3)** | §2 / Card C2 header + §C-2 | F/M | True | EXPERT_INFERENCE, v3 | Apex 마커 표준화(`[⚡ Apex Concept]`) + Plausible Fallacy 블록 신규 — V5.0 framework 미준수 항목 종료. EC50/Emax/γ 분리 임상 함의 명시 | Low |
| **P2 (v3)** | §2 / Card C2 Big Idea | F | True | EXPERT_INFERENCE, v3 | Big Idea를 임상 직관-우선으로 재배치 — 항생제 증량 직관 lead-in으로 Apex 학습 진입 마찰 감소. 기존 수식 텍스트 보존, 위치만 후순위 | Low |
| **P3 (v3)** | §5 Pair 1 / Pair 2 / §2 Card C2 §A | M | True | EXPERT_INFERENCE, v3 | Memory Hook 표준화 — Pair 1 in-table → 독립 블록 격상; Pair 2 신규 hook(중간점 vs 가파름); C2 §A 보조 hook(Emax vs Imax). 모두 구조적 필연 인코딩 | Low |
| **P4 (v3)** | §5 / Pair 2 | M | True | EXPERT_INFERENCE, v3 | Critical Blow 신규 — Hill γ 누락 시 협역 치료역 약물의 임상 용량 조절 과관대화 → 규제 deficiency 시나리오 | Medium |
| **P5 (v3)** | §8 / Professional Moat | W | True | EXPERT_INFERENCE, v3 | Hill γ 임상 함의 3-bullet 추가 — 역치 특성, 용량 조절 정밀도, exposure-response 보고서 필수 항목. TDM 임상경험 anchor 활용 | Low |
| **P6 (v3)** | §2 / Card C1, C3, C5 | M | True | EXPERT_INFERENCE, v3 | Practice Brief 라벨 표준화 — C1/C3/C5에 신규 Practice Brief 블록 추가. Emax/intrinsic activity/PK·PD-rate-limited 첫 등장 ANNOTATION 보강 | Low |
| **P7 (v3)** | PART B 전체 | W | True | EXPERT_INFERENCE, v3 | Phase 4D Certification 표 v3 컬럼 추가; Marker-to-component 매핑 4종 신규 라벨 추가; Augmentation Log v3 항목 추가 | Low |

#### Rejected or Deferred Augmentation Candidates (unchanged from ver1)

| Rejected candidate | Reason for rejection |
|---|---|
| Reintroduce "5–100× FIH/NDA" warning | Rejected: Audit classifies direct support as NOT_IN_SOURCE for this PDF scope |
| Add new clinical dosing/guideline examples for aspirin or omeprazole | Rejected: would add external clinical guidance beyond source pages |
| Add numerical ke0 range for naproxen or effect compartment examples | Rejected: Audit identifies the specific naproxen ke0 range as unsupported in the PDF |
| Add new Mermaid/SVG code in Phase 4D | Rejected: Phase 4D may include briefs/markers only; Phase 5 renders visuals |
| Add new page tags in ver2 or v3 | Rejected: Phase 4D / Phase 4 is closed for page-tag generation; ver2/v3 reuse only existing tags |
| Add Crucible Grade B Tip #5 (`k_t` prior 우회로 with platelet 10일/prothrombin 1–2일) | Deferred: requires careful boundary between R&T turnover ranges and external prior values; out of scope for v3 minimal-delta release |
| Add Crucible Tip #4 (F-test bootstrap procedure) | Deferred: implementation-level statistical procedure; covered functionally by I3 (precision-improvement diagnostic) at the conceptual level |
| Rewrite C1/C3/C4/C5 Big Idea blocks to identical "임상 직관 lead-in" structure | Deferred (v3): independent reviewer flagged C2 (Apex card) as the priority; remaining cards already open intuition-first per spot-check. Future ver may standardize all five cards uniformly. |

---

## Final Verdict — v3

```text
GO        : HTML compile (Phase 5) cleared with v3 enhancements applied on top of ver2 base.
NO-GO     : Independent reviewer's NO-GO on ver2 (V5.0 Apex framework gaps) is now closed.
REDO      : Not required.
PASS      : Learner-Standalone (PASS+), Zero-Omission (PASS unconditional), Mastery-Uplift (PASS++),
            Source-Boundary (PASS), HTML-Readiness (PASS) — all PASS at v3 level.
DELTA     : v3 closes the three structural gaps flagged by independent review:
            (1) Apex marker `[⚡ Apex Concept]` standardized + Plausible Fallacy block added (P1)
            (2) Memory Hooks elevated to standardized `**⚡ 기억 고리 (Memory Hook)**` blocks (P3)
            (3) Critical Blow row added to highest-impact confusion pair (Pair 2, P4)
            Plus: Big Idea intuition-first re-ordering on Apex card (P2),
                  Hill γ clinical implications in Professional Moat (P5),
                  Practice Brief labels + key-term ANNOTATIONs (P6),
                  PART B v3 trace updates (P7).
SCOPE     : Seven labeled patches (P1–P7), all `[EXPERT_INFERENCE, v3]` tagged.
            ver2 body sentences preserved verbatim.
            Acenocoumarol/phenprocoumon rate-limiting anchor (Insertion I5) preserved.
            Q9 Boss Dilemma preserved.
            All page tags preserved; no new page tags introduced.
            pp.225–228 boundary preserved.
            aspirin-75mg, naproxen-ke0, 5–100×/FIH/NDA still excluded.
ACTION    : Phase 5 HTML compile may proceed. Render PART A only; render v3 patch blocks per the
            updated Marker-to-component mapping (Plausible Fallacy / Memory Hook / Practice Brief /
            Critical Blow). Preserve all `[EXPERT_INFERENCE, v3]` source-basis labels exactly.
```

---

## Final v3 All-Pass Checklist (8 items)

| # | Check item | Verification | Status |
|---|---|---|---|
| 1 | C2 카드 헤더가 `[⚡ Apex Concept]`로 표준화됨 (PATCH 1a/1b) | §1 항법도 line + §2 Card C2 header line + PART B B8 splice table line — 3개 위치 동기화 | ✅ PASS |
| 2 | C2 §C-2 영역에 Plausible Fallacy 블록 신규 존재 (PATCH 1c) | `**⚡ Plausible Fallacy — Apex Concept 전용 — [EXPERT_INFERENCE, v3]**` 블록 + 그럴듯한 오해/왜 틀렸는가/실무에서 어떻게 드러나는가 3-part 구조 | ✅ PASS |
| 3 | C2 Big Idea가 임상 직관 lead-in으로 시작 (PATCH 2) | "항생제 또는 항부정맥제를 두 배 증량했는데..." lead-in 블록이 기존 Hill `n` 수식 해석 텍스트 *앞*에 위치. 기존 텍스트는 보존 | ✅ PASS |
| 4 | §5 Pair 1·2에 표준 Memory Hook 독립 블록, C2 §A에 보조 Hook (PATCH 3) | Pair 1: `**⚡ 기억 고리 — *결합 vs 효능***`; Pair 2: `**⚡ 기억 고리 — *중간점 vs 가파름***`; C2 §A: `**⚡ 기억 고리 — *최대 자극 vs 최대 억제* (Emax vs Imax)***` — 3 hooks all standardized | ✅ PASS |
| 5 | §5 Pair 2에 Critical Blow 행 존재 (PATCH 4) | `\| **치명적 타격 (Critical Blow) — [EXPERT_INFERENCE, v3]** \|` 행이 Pair 2 표 직후 위치, Hill γ 누락 시 규제 deficiency 시나리오 명시 | ✅ PASS |
| 6 | §8 Professional Moat에 Hill γ 임상 함의 3-bullet 존재 (PATCH 5) | γ>1 역치 특성 / 용량 조절 정밀도 / Exposure-response 보고서 필수 — 3-bullet, TDM 임상경험 anchor 포함 | ✅ PASS |
| 7 | C1·C3·C5에 Practice Brief 신규 블록 + 핵심 용어 ANNOTATION 보강 (PATCH 6) | C1 Practice Brief (Mastery Note 직후), C3 Practice Brief (Mastery Note 직후), C5 Practice Brief (Failure Mode 직후) + Emax/intrinsic activity/PK·PD-rate-limited annotation 추가 | ✅ PASS |
| 8 | 비협상 보존 항목이 모두 보존됨 (Non-Negotiable Preservation Rules) | (a) Acenocoumarol/phenprocoumon Insertion I5 verbatim, (b) Q9 Boss Dilemma verbatim, (c) 모든 page tag 보존(새 page tag 미도입), (d) 모든 v3 추가는 `[EXPERT_INFERENCE, v3]` 라벨링 | ✅ PASS |

---

## Final Verdict — ver2 (보존, 참고용)

```text
GO        : HTML compile (Phase 5) cleared.
NO-GO     : Direct HTML compile of ver1 without ver2 enhancements is no longer the recommended path.
REDO      : Not required.
PASS      : Learner-Standalone, Zero-Omission, Mastery-Uplift, Source-Boundary, HTML-Readiness — all PASS.
DELTA     : ver2 closes Audit T5 SHOULD_FIX (4 items) and Crucible Grade A/B intuitions (2 items) via 6 labeled insertions.
SCOPE     : Six insertions only; no body rewriting; no new page tags; no rejected claims restored; pp.225–228 boundary preserved.
ACTION    : Phase 5 HTML compile may proceed. Render PART A only; render Insertion blocks as Mastery-Note callouts with labels preserved.
```

---

## v3.1 Final Checklist

| # | Check item | Verification | Status |
|---|---|---|---|
| 1 | PART A readability improved | KR-01 ~ KR-22 적용 완료 — 영어식 형용사 나열·passive 술어·주어 dangling·과도한 영어-한국어 혼합·긴 합성문이 한국어-자연스러운 능동·분리·gloss 형태로 교정됨. PART A의 모든 §1, §2(C1–C5), §5(Pair 2·Pair 3), §7(Q9), §8(Professional Moat·Hill γ block)에서 학습자 독해 마찰이 감소. | ✅ PASS |
| 2 | Scientific content unchanged | 모든 22개 patch는 prose-level surgical edit. 어떤 과학적 주장·정의·결론·기전·임상 추론도 변경되지 않음. KR-04는 "Response is proportional to [RC]; full effect may occur..."를 한국어로 번역했으나 의미·수치·조건 모두 동일. KR-15는 PK-rate-limited / PD-rate-limited 정의의 parenthetical을 완전한 한국어 문장으로 elevate했으나 정의 자체는 변경 없음. | ✅ PASS |
| 3 | Equations preserved | MathJax 수식 블록(`$...$`, `$$...$$`) 전체 보존. C1 평형 결합, Kd, Hill, Imax, AUEC closed form, Duration log-dose 식 모두 원문 그대로. NONMEM `$DES`, code-fence `[출처: ...]` 라인 모두 비변경. | ✅ PASS |
| 4 | Page tags preserved | `[G&W p.199–200]`, `[G&W p.202–204]`, `[G&W p.216, p.220]`, `[R&T p.234–235]`, `[R&T p.243–244]`, `[R&T p.251–252]`, `[R&T p.249–253]`, `[확인 필요 — 첨부 PDF 미포함 구간]`, `[확인 필요 — 교과서 외 규제 적용]` 등 모든 page tag 토큰의 위치·숫자 불변. v3.1에서 새 page tag를 도입하지 않음. | ✅ PASS |
| 5 | Figure markers preserved | `<!-- FIGURE_POINTER -->` 5개, `<!-- FIGURE_SCHEMATIC -->` 2개 — 합 7개 figure marker 블록 전체 보존. Source / Why this matters / When to look / Learner instruction / Title / Mode / Visual objective / Core message / Elements / Caption / Alt text / Source relation 필드 모두 원문 그대로. KEEP/REJECT 결정(P 5개 + R 2개) 불변. | ✅ PASS |
| 6 | Source-boundary preserved | pp.225–228 boundary 유지. Aspirin 75 mg, naproxen ke0, 5–100×/FIH/NDA, FDA deficiency letter, perioperative 7-day rule 모두 미복원. PART B B5 Audit Guardrails / B7 Deprecated and Forbidden Restorations 전체 비변경. Insertion I5(acenocoumarol/phenprocoumon) verbatim, Q9 Boss Dilemma의 임상/규제 결론 비변경(KR-19는 "다음" → "다음으로" 한 글자 추가). 모든 source-basis label(`[EXPERT_INFERENCE, v3]`, `[TEXTBOOK_DERIVED]`, `[CRUCIBLE_DERIVED]`, `[교과서 외 규제 해석]`, `[실무 구현 번역]`, `[수학적 추론]`) 불변. | ✅ PASS |
| 7 | HTML-readiness preserved | PART B 전체(B1 Compilation Contract ~ B11 Mastery Augmentation Log) 비변경. Marker-to-component mapping 14행 비변경. PATCH MODE Splice Verification Table(B8) 비변경. CSS class hint(`source-page`, `source-uncertain`, `figure-pointer` 등) 미변경. MathJax CDN, Mermaid CDN dependency 사양 불변. Phase 5 컴파일러는 v3와 동일한 rendering contract로 v3.1을 처리할 수 있음. (B10 Micro-Patch Log에 v3.1 trace 항목만 추가됨 — guardrail 변경 아님.) | ✅ PASS |
| 8 | Ready for Phase 5 HTML compilation | v3.1은 v3에 대한 prose-only delta이며, v3가 통과한 5개 인증서(Learner-Standalone PASS+, Zero-Omission PASS unconditional, Mastery-Uplift PASS++, Source-Boundary PASS, HTML-Readiness PASS)에 대한 회귀 위험이 없다. Phase 5 컴파일러는 v3.1을 입력으로 받아, v3에서 정의된 marker mapping·page tag wrapping·figure rendering rule·MathJax 처리·Self-Test accordion·navigation anchor integrity·responsive/print mode 모두 그대로 적용하면 된다. **GO — Phase 5 HTML 컴파일 가능.** | ✅ PASS |

---

*v3.1 = v3 + Korean Readability Patch (22 surgical Low-risk edits on PART A prose).*  
*Phase 5 HTML compilation: cleared.*

---

## v3.2 Final Checklist

| # | Check item | Verification | Status |
|---|---|---|---|
| 1 | PART A 일반 설명문이 한국어 중심으로 전환됨 | §1–§8 전체의 일반 영어 산문이 한국어로 변환됨. 모든 §2 카드 소제목(Formal Definition, Structural Necessity 등)에 `한글(English)` 병기 적용. 학습 장치 레이블(Recap, Mastery Note, Practice Brief, Trench-Level Tip, Failure Mode 등) 한국어화. §5 혼동 쌍 테이블 헤더·§7 질문/정답 레이블 한국어화. | ✅ PASS |
| 2 | 영어로 남은 표현이 전문용어·기호·코드·마커·career-critical term에 한정 | CL, V, EC50, Emax, Hill n, AUC, AUEC, ODE 등 표준 기호/약어, NONMEM 코드, MathJax 수식, page tag, source-basis label, figure marker, HTML compiler marker만 영어 유지. 일반 설명 영어 문장은 한국어로 전환 완료. | ✅ PASS |
| 3 | Career-critical term에 `한글(English)` 형식 적용 | functional sensitivity→기능적 감수성(functional sensitivity), receptor occupancy→수용체 점유율(receptor occupancy), binding assay→결합 분석(binding assay), dose-titration sensitivity→용량 조절 감수성(dose-titration sensitivity), model discrimination→모델 판별(model discrimination) 등 주요 전문용어에 첫 등장 병기 적용. | ✅ PASS |
| 4 | 수식·page tag·source label·figure marker·HTML compiler marker 보존 | 모든 MathJax 수식(`$...$`, `$$...$$`) 불변. 모든 page tag(`[G&W p.XX]`, `[R&T p.XX]` 등) 불변. 모든 source-basis label 불변. 모든 `<!-- FIGURE_POINTER -->`, `<!-- FIGURE_SCHEMATIC -->` 마커 블록 내용 불변. 모든 HTML compiler marker 불변. | ✅ PASS |
| 5 | 새 과학적 주장·수치·예시·reference 미추가 | v3.2는 순수 한국어화 패치. 어떤 과학적 사실, 수치, 임상 예시, 규제 주장, page tag, figure도 추가하지 않음. | ✅ PASS |
| 6 | Section/card 구조·anchor 미변경 | PART A의 §1–§8 구조, 카드 C1–C5 순서, 혼동 쌍 Pair 1–4 순서, Q1–Q9 순서 모두 보존. PART B B8 Splice Verification Table 및 B4 Marker-to-component mapping 미변경. | ✅ PASS |
| 7 | Code block·NONMEM/R/Python syntax 미번역 | 코드 블록 내부, `[출처: ...]` 라인, NONMEM syntax 모두 원문 유지. | ✅ PASS |
| 8 | Phase 5 HTML 컴파일 준비 완료 | v3.2는 v3.1에 대한 한국어화 전용 delta이며, v3가 통과한 5개 인증서에 대한 회귀 위험이 없다. Phase 5 컴파일러는 v3.2를 입력으로 받아 동일한 rendering contract를 적용하면 된다. **GO — Phase 5 HTML 컴파일 가능.** | ✅ PASS |

---

*v3.2 = v3.1 + Korean-Dominant Readability Patch (systematic Korean-dominance pass on all PART A learner-facing prose).*  
*Phase 5 HTML compilation: cleared.*

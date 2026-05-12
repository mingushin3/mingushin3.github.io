# 10 — PK/PD 모델 기초: Emax·Hill·AUEC — v3.7

<!-- 기호 통일: Emax/Imax/EC50/IC50 → LaTeX 표기 $E_{max}$/$I_{max}$/$EC_{50}$/$IC_{50}$ (본문 수식 기준) -->
<!-- 기호 통일: Hill $\gamma$와 Hill $n$은 원문 병기를 유지하되, 핵심 수식 표기는 Hill $n$ 중심으로 통일 -->

## 출처 및 범위 노트

이 장은 Gabrielsson & Weiner 5e Ch.3의 수용체 결합(receptor binding), $E_{max}$/Hill, 비정상상태 반응/AUEC(non-steady-state response/AUEC) 관련 범위와 Rowland & Tozer 5e Ch.8의 시간 지연(time delay), 히스테리시스(hysteresis), 효과 구획(effect compartment), 간접 반응(indirect response), 효과 지속 시간(duration of effect) 관련 범위를 바탕으로 합니다.

- 사용 범위: G&W p.199–224, p.229–234, p.732–741; R&T p.233–264.
- 교과서 원그림은 본문에 직접 삽입하지 않습니다. 교과서 그림 참조는 원그림 확인 위치를 안내하고, 개념 도식 안내는 교과서 원그림을 복제하지 않고 새로 구성한 해설 도식입니다.
- 범위 밖 구간은 본문에서 `[확인 필요 — 첨부 PDF 미포함 구간]`처럼 표시하며, 본 자료에서 추정하여 보강하지 않습니다.

---

## 임상 장면 — 왜 이 세션이 필요한가

Digoxin 1 mg 정맥 급속 투여 후 첫 4시간에는 혈장 농도가 감소해도 좌심실 구출 시간 지표는 오히려 증가할 수 있습니다. Naproxen 500 mg 경구 치과 통증 모델에서는 같은 비결합 혈장 농도라도 시간 순서에 따라 통증 완화가 달라지는 반시계 방향 히스테리시스가 나타납니다. Aspirin 650 mg 경구 투여 후 혈장 $t_{1/2}$는 약 15 min이지만 항혈소판 활성은 수일간 지속됩니다. 따라서 PK/PD 판단은 "농도가 얼마인가"에서 끝나지 않고, "그 농도가 어떤 시간 지연과 반응 시스템을 통과하는가"까지 읽어야 합니다. [R&T p.234–235; R&T p.251]


## 학습자 내비게이션 안내

**이 자료 사용법:** 먼저 §1에서 C1–C5의 위치를 잡고, §2의 각 개념 해부 카드(Concept Anatomy Card)를 순서대로 읽으면 됩니다. 교과서 그림 참조는 원그림을 직접 확인하라는 안내이며, 본 문서에는 저작권 그림을 삽입하지 않습니다. 개념 도식 안내는 교과서 원그림을 복제하지 않고 새로 구성한 해설 도식입니다.

**학습 경로:** C1에서는 $K_d$와 $EC_{50}$의 층위를 분리합니다. C2에서는 Hill $n$을 가파름/설계 파라미터(steepness/design parameter)로 고정합니다. C3–C4에서는 히스테리시스(hysteresis)가 보일 때 직접 혈장-반응 가정을 내려놓고 지연 위상(delay topology)을 선택하는 법을 익힙니다. C5에서는 AUEC와 지속 시간(duration)이 약물 반감기(drug half-life)만으로 결정되지 않는다는 점을 반응-시간 척도(response-time scale)에서 확인합니다.

**시작 전 점검:** 평형(equilibrium), 1차 제거(first-order elimination), 기저 반응(baseline response), 농도-시간 곡선(concentration-time curve), 반응-시간 곡선(response-time curve)의 차이를 먼저 떠올리면 됩니다.  
**학습 후 확인:** $K_d\neq EC_{50}$, $n\neq$ 기전 증명, 히스테리시스 $\neq$ 잡음, 약물 $t_{1/2}\neq$ 효과 지속 시간을 각각 한 문장으로 설명할 수 있어야 합니다.

---


<!-- SLIDE_START: §1 | title: 세션 개요와 로드맵 -->

# §1 — 세션 개요와 로드맵


## 3-레이어 개념 지도

```text
레이어 1 — 무엇인가
  K_d / EC50 / Hill n / hysteresis / effect compartment / AUEC / duration

레이어 2 — 어떻게 계산되는가
  Mass action → Emax hyperbola → Sigmoid Emax/Hill
  C(t) → Ce(t) → E(t)
  AUEC = ∫E(t)dt, duration = log-dose relation

레이어 3 — 언제, 왜 중요한가
  EC50 공변량 해석 → 용량 조절 민감도 → delay-source 선택
  → 투여 간격·효과 지속 시간·규제 방어 가능성
```

## 지식 그래프 위치

```text
[선행 세션: 선형 PK·농도-시간 해석] → [이 세션: 농도-효과·시간 지연·반응 지속성] → [후속 세션: PopPK/PD 공변량·시뮬레이션·용량 최적화]
```

🧭 **읽는 순서:**  
카드 1 (C1): $K_d$와 $EC_{50}$는 왜 같은 숫자로 취급하면 안 되는가?  
카드 2 (C2): $EC_{50}$만으로는 왜 임상 안전 마진을 설명할 수 없는가?  
카드 3 (C3): 농도-반응 고리는 언제 모델 구조 변경 신호가 되는가?  
카드 4 (C4): 지연은 효과 부위 평형화인가, 시스템 전환인가?  
카드 5 (C5): 효과 지속 시간은 왜 혈장 반감기의 그림자가 아닌가?


**소스 통합:** G&W Ch.3는 수용체 결합(receptor binding) → $E_{max}$/Hill → 비정상상태 반응/AUEC(non-steady-state response/AUEC)의 수식적 골격을 제공합니다. R&T Ch.8은 같은 개념을 임상 시간축, 히스테리시스(hysteresis), 효과 구획(effect compartment), 간접 반응(indirect response), 효과 지속 시간(duration of effect)으로 번역합니다.

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

**구조적 흐름:** 질량작용법칙(C1) → $E_{max}$ 쌍곡선 → Hill $n$ 도입으로 sigmoid 일반화(C2) → 평형 가정의 붕괴가 히스테리시스로 드러남(C3) → 효과 구획 또는 시스템 전환(system turnover)으로 시간 지연 흡수(C4) → 반응-시간 곡선의 적분량과 지속 시간을 설계 지표로 사용(C5)의 순서로 읽으면 됩니다.

**범위 경계:** G&W §3.6.1의 경쟁적 길항(competitive antagonism) 시작부까지만 본문에 포함합니다. G&W §3.6.2–§3.6.5 및 G&W §3.12 기저치 모델링(baseline modeling)은 `[확인 필요 — 첨부 PDF 미포함 구간]`으로 유지하고 본 세션에서 추정하지 않습니다.

---


> 📖 **교과서 그림 참조:** Gabrielsson & Weiner 5e, p.199, Fig.3.1
> 이 그림은 전체 세션을 농도-반응 감수성(concentration-response sensitivity)과 반응-시간 거동(response-time behavior)이라는 두 개의 연결된 PD 문제로 잡아 줍니다. 이 그림이 없으면 C1–C5가 하나의 PK→PD 번역 사슬이 아니라 서로 분리된 수식처럼 보일 수 있습니다.
> 확인 시점: §1 로드맵을 읽기 전, 또는 §1의 Big Idea를 읽은 직후에 확인하면 됩니다.
> 학습 지시: 왼쪽 패널에서 potency/efficacy를, 오른쪽 패널에서 onset/intensity/duration을 확인하세요. 그런 다음 C1–C2는 왼쪽 패널에, C3–C5는 오른쪽 패널에 대응시키면 됩니다.

---


<!-- SLIDE_START: §2 | title: 개념 해부 카드 -->

# §2 — 개념 해부 카드

---

<!-- SLIDE_START: C1 | title: 질량작용법칙과 Emax 골격 -->

## Card C1 — 질량작용법칙(Law of Mass Action) → $E_{max}$ 골격

> **거장의 시각**
> $K_d$와 $EC_{50}$를 같은 potency 숫자로 배열하면 결합층과 기능층이 섞여 공변량 해석이 무너집니다.
> 이 관점으로 보면 $E_{max}$ 식은 경험식이 아니라 수용체 점유율과 신호 증폭을 압축한 구조식입니다.


$K_d$는 리간드-수용체 결합 친화도(ligand-receptor binding affinity)의 지표입니다. $EC_{50}$는 결합 이후 신호전달(transduction)과 조직 반응(tissue response)까지 포함한 기능적 감수성(functional sensitivity)의 지표입니다. **$K_d$와 $EC_{50}$가 다를 수 있다는 사실**이 C1의 핵심입니다. 그 차이를 만드는 대표 이유가 여분 수용체(spare receptor)와 증폭 연쇄(cascade amplification)입니다. [G&W p.203–206]

즉, 결합이 강하다는 말과 조직에서 절반 효과가 낮은 농도에서 나온다는 말은 같은 뜻이 아닙니다.

평형 결합의 미시적 동역학을 점유율(occupancy) 식으로 정리하면, $E_{max}$ 모델의 분자와 분모가 왜 같은 농도 단위를 가져야 하는지 드러납니다.

### A. 형식적 정의(Formal Definition)

가역적 1:1 약물-수용체 결합(drug-receptor binding)에서 반응 $E$는 결합된 수용체 복합체(occupied receptor complex — 약물이 결합한 수용체 풀) $[RC]$에 비례합니다. 수용체가 모두 점유(occupied)될 때 $E_{max}$(← 농도가 무한대일 때 도달하는 최대 가능 효과) $=\alpha[R_T]$이며, $\alpha$는 고유활성(intrinsic activity — 수용체 1단위가 만들어내는 효과 크기, 부분효현제일수록 작음)입니다. [G&W p.203]

$$
\underbrace{E_{max}}_{\text{최대효과}}
=
\underbrace{\alpha}_{\text{고유활성}}
\underbrace{[R_T]}_{\text{총수용체}}
$$

### B. 도출(Derivation)


**평형 결합:**

$$
\underbrace{\frac{d[RC]}{dt}}_{\text{복합체 변화}}
=
\underbrace{k_1[R][C]}_{\text{결합 생성}}
-
\underbrace{k_{-1}[RC]}_{\text{해리 손실}}
=
\underbrace{0}_{\text{평형}}
$$


따라서

$$
\underbrace{K_d}_{\text{해리상수}}
=
\underbrace{\frac{k_{-1}}{k_1}}_{\text{해리/결합비}}
=
\underbrace{\frac{[C][R]}{[RC]}}_{\text{유리/결합비}}
$$


총 수용체 농도 $[R_T]=[R]+[RC]$를 대입하면

$$
\underbrace{\frac{[RC]}{[R_T]}}_{\text{점유율}}
=
\underbrace{\frac{[C]}{[C]+K_d}}_{\text{농도-친화도}}
$$


반응 비례성(response proportionality)을 적용하면

$$
\underbrace{\frac{E}{E_{max}}}_{\text{상대반응}}
=
\underbrace{\frac{[C]}{[C]+K_d}}_{\text{점유율}}
,\qquad
\underbrace{E}_{\text{반응}}
=
\frac{\underbrace{E_{max}}_{\text{천장}}\cdot \underbrace{[C]}_{\text{농도}}}{\underbrace{[C]+K_d}_{\text{농도+Kd}}}
$$


기능적 반응(functional response)에서는 $K_d$ 대신 $EC_{50}$가 사용됩니다.

$$
\underbrace{E}_{\text{효과}}
=
\frac{\underbrace{E_{max}}_{\text{천장}}\cdot \underbrace{C}_{\text{농도}}}{\underbrace{EC_{50}}_{\text{절반효과}}+\underbrace{C}_{\text{농도}}}
$$


`[출처: G&W 5e, Ch.3, p.202–204, Eq.3:1–3:10]`

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $E_{max}$ | 반응 단위 | 수용체 점유와 고유활성이 만들 수 있는 최대 효과 | 총 수용체량, 조직 반응성, 고유활성 |
| $K_d$ | 농도 | 결합층의 해리상수 | 결합/해리 속도 변화 |
| $EC_{50}$ | 농도 | 기능층에서 절반 효과가 나오는 농도 | 결합, 수용체 밀도, 증폭 이득, 조직 반응 |
| $C$ 또는 $[C]$ | 농도 | 관련 생체구획의 약물 농도 | 투여량, 분포, 결합, 제거 |

💡 **결합층 vs 기능층** — $K_d$는 붙는 힘이고, $EC_{50}$는 붙은 뒤 시스템이 절반 반응을 내는 농도입니다.  
⚠️ **헷갈림 방지:** $EC_{50}<K_d$는 오류가 아니라 여분 수용체와 증폭 연쇄가 있을 때 가능한 기능적 결과입니다.


### C. 구조적 필연성(Structural Necessity)

분자 $[C]$는 이용 가능한 리간드(available ligand)가 늘수록 수용체 점유율이 증가한다는 질량작용법칙의 결과입니다. 분모 $[C]+K_d$는 수용체 보존(receptor conservation — 수용체 총량 보존)을 반영합니다. 이 구조 때문에 점유율은 0–1 사이에 머물며, 반응도 $E_{max}$를 초과하지 않습니다.

### D. 가정과 경계 조건(Assumptions & Boundary Conditions)

- 1:1 가역적 결합(reversible binding), 평형(equilibrium), 단일 유효 생체구획 농도(single effective biophase concentration).
- 반응은 $[RC]$에 비례합니다. 수용체 비축분(receptor reserve — 여분 수용체에 의한 증폭 여지)이 있으면 수용체가 완전히 점유되지 않아도 최대에 가까운 효과가 발생할 수 있습니다.
- $EC_{50}\neq K_d$일 수 있습니다. G&W는 점유율-반응 불일치(occupancy-response 불일치)와 신호 증폭(signal amplification)을 명시합니다. [G&W p.204–206]

$$
\underbrace{EC_{50}}_{\text{기능 EC50}}
\neq
\underbrace{K_d}_{\text{결합 Kd}}
$$

### E. 한계(Limitations)

여분 수용체가 많거나 증폭 이득(cascade gain)이 큰 조직에서는 수용체의 소량 점유(small occupancy)만으로도 큰 반응(large response)이 나타날 수 있습니다. G&W Fig.3.5는 10% 점유율이 90% 반응으로 증폭되는 연쇄 증폭 예를 제시합니다. Fig.3.6은 동일 반응에 필요한 점유율이 조직마다 다를 수 있음을 보여줍니다. [G&W p.205–206]

포화/치환 결합(saturation/displacement binding)과 Cheng-Prusoff 변환은 수용체 결합 분석(receptor binding assay)의 Ki/$IC_{50}$ 해석에 필요하지만, 본 세션에서는 기능적 $EC_{50}$와 결합 $K_d$를 혼동하지 않는 경계로만 사용합니다. [G&W p.206–210]

> 💼 **실무 인사이트:** $EC_{50}$ 공변량 효과(covariate effect)가 보이면 먼저 “약물 측(drug-side) 변화인가, 시스템 측(system-side) 변화인가?”를 분리합니다. 총 농도(total concentration) 기반 $EC_{50}$ 변화는 단백질 결합(protein binding) 변화일 수 있습니다. 따라서 비결합 농도(unbound concentration) 분석이 없으면 수용체 감수성(receptor sensitivity) 변화로 단정하지 않습니다.

### F. 제텔카스텐 원자 노트(Zettelkasten Atom)

**원자 노트 C1(Atom C1):** $K_d$는 결합 강도, $EC_{50}$는 결합 이후 조직·신호 시스템까지 포함한 기능적 감수성(functional sensitivity)입니다. $E_{max}$ 식의 쌍곡선은 수용체 보존(receptor conservation)과 평형 질량작용(equilibrium mass action)에서 나옵니다.

**요약(Recap):** C1은 $E_{max}$ 모델을 “경험식”이 아니라 수용체 점유율(receptor occupancy)과 반응 신호전달(response transduction)의 압축형으로 보게 만듭니다.

> **C1 체화 핵심**
> ① `새 $EC_{50}$ 값을 만났을 때` → 결합 분석인지 기능 분석인지가 먼저 결정
> ② `총 농도 vs 비결합 농도 혼동` → 단백결합 변화가 apparent potency를 지배
> ⚡ `$K_d=EC_{50}$로 단정` → 결합층과 기능층 혼합 → 공변량 기전 해석 실패

> 📊 **개념 도식 (HTML에서 렌더링):** $K_d$와 $EC_{50}$의 분리: 수용체 점유율(receptor occupancy) → 신호전달(transduction) → 반응(response) — $K_d$는 결합 친화도(binding affinity)에 속하고, $EC_{50}$는 증폭된 조직/시스템 반응(tissue/system response)에 속합니다.


---

<!-- SLIDE_START: C2 | title: Sigmoid Emax / Hill 모델 -->

## Card C2 — Sigmoid $E_{max}$ / Hill 모델 [⚡ Apex Concept]

> **앞 카드에서 이 카드로:** C1이 결합과 기능의 층위를 분리했다면, C2는 기능 반응 곡선 안에서 천장·중간점·가파름을 분리합니다.

> **거장의 시각**
> 💢 **흔한 오해:** $EC_{50}$만 알면 해당 농도에서 임상 효과를 예측할 수 있다고 생각합니다.
> ✅ **실제는:** 실제 반응 크기와 안전 마진은 $E_{max}$, $EC_{50}$, Hill $n$이 함께 결정합니다.
> 🎯 **체화할 단 하나의 직관:** Hill $n$은 곡선 장식이 아니라 용량 조절 정밀도를 바꾸는 임상 안전 마진 파라미터입니다.


> **임상 직관 도입 — [EXPERT_INFERENCE, v3]**  
> 항생제 또는 항부정맥제를 두 배 증량했는데 효과가 두 배가 되지 않는 경험은 임상 약사라면 이미 알고 있습니다. 왜일까요? 효과에는 천장($E_{max}$)이 있기 때문입니다. 그렇다면 그 천장에 *얼마나 빨리* 도달하는가 — 그것을 결정하는 것이 곡선의 가파름, 즉 **Hill coefficient $\gamma(=n)$**입니다. $E_{max}$/Hill 모델은 이 세 양을 분리합니다: **천장($E_{max}$), 효능($EC_{50}$), 가파름($\gamma$)**. 특히 $\gamma$가 1보다 클수록 작은 농도 변화가 큰 반응 변화를 만들어 협역 치료역(narrow therapeutic window) 특성이 형성됩니다 — 이것이 이 카드를 Apex로 만드는 이유입니다.

Hill $n$은 기전 증명(mechanism proof)이 아니라 **곡선 가파름/유연성 파라미터(curve steepness/flexibility parameter)**입니다. 그러나 임상적으로는 강력합니다. $n$이 커질수록 효과 50%에서 90%로 상승하는 데 필요한 농도 배율(concentration ratio)이 줄어듭니다. 즉, 더 좁은 농도 구간 안에서 반응이 완성됩니다. 따라서 용량 조절 단계 크기(dose-titration step size)와 안전 마진(safety margin) 해석이 더 민감해집니다. [G&W p.216, p.220]

선형/로그-선형 효과 모델(linear/log-linear effect models)은 제한된 농도 범위에서는 유용합니다. 그러나 효과 고원부(effect plateau — 농도 증가에도 효과가 더 늘지 않는 구간)와 급격한 전환(steep transition)을 설명하려면 일반 $E_{max}$를 넘어 sigmoid $E_{max}$가 필요합니다. [G&W p.210–216]

### A. 형식적 정의(Formal Definition)


Sigmoid $E_{max}$ 모델:

$$
\underbrace{E}_{\text{효과}}
=
\frac{\underbrace{E_{max}}_{\text{천장}}\cdot \underbrace{C^n}_{\text{농도^n}}}{\underbrace{EC_{50}^n}_{\text{중간점}}+\underbrace{C^n}_{\text{농도}}}
$$


기저치(baseline)가 있는 억제 반응(inhibitory response)에서는 다음과 같이 씁니다.

$$
\underbrace{E}_{\text{관찰반응}}
=
\underbrace{E_0}_{\text{기저치}}
-
\frac{\underbrace{I_{max}}_{\text{억제천장}}\cdot \underbrace{C^n}_{\text{농도^n}}}{\underbrace{IC_{50}^n}_{\text{절반억제}}+\underbrace{C^n}_{\text{농도}}}
$$


`[출처: G&W 5e, Ch.3, p.216, p.218, Eq.3:32, Eq.3:34–3:35]`

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $E_{max}$ / $I_{max}$ | 반응 단위 또는 비율 | 자극 또는 억제의 천장 | 표적 용량, 반응 시스템 한계, 기저치 구조 |
| $EC_{50}$ / $IC_{50}$ | 농도 | 절반 자극 또는 절반 억제 농도 | 역가, 단백결합, 생체구획 농도, 시스템 감수성 |
| $n$ | 무차원 | 곡선 가파름과 전환 민감도 | 농도 범위, 기전 후보, 이질성, 설계 정보 |
| $E_0$ | 반응 단위 | 약물 투여 전 또는 기준 반응 | 기저질환, 시간 변동, placebo/drift |

💡 **천장·중간점·가파름 분리** — $EC_{50}$는 위치, $E_{max}$는 높이, Hill $n$은 경사입니다.  
⚠️ **헷갈림 방지:** $n>1$은 협동성 증명이 아니라, 먼저 가파름을 설명하는 현상학적 파라미터로 써야 합니다.

> **⚡ 기억 고리 (Memory Hook) — *최대 자극 vs 최대 억제* ($E_{max}$ vs $I_{max}$) — [EXPERT_INFERENCE, v3]**  
> $E_{max}$ 모델은 **자극(stimulation) 모델** — 효과가 0(또는 기저치)에서 출발해 천장 $E_{max}$까지 *상승*합니다. $I_{max}$ 모델은 **억제(inhibition) 모델** — 효과가 기저치 $E_0$에서 출발해 $(1-I_{max})\cdot E_0$까지 *감소*합니다. $I_{max}=1$이면 완전 억제(기저치가 0이 됨)를 뜻합니다. 두 모델은 같은 sigmoid 형태이지만 **방향이 반대**입니다 — 부호와 기저치의 위치가 핵심입니다. PD 모델 선택 시 자극 데이터에 $I_{max}$를 적용하거나 그 반대로 하면 노출-반응 곡선의 천장이 과대추정되거나 억제 효율이 잘못 계산되어 용량-반응(dose-response) 결론이 정반대로 나올 수 있습니다.

### B. 파라미터 복원과 PD3 앵커(Parameter Recovery and PD3 Anchor)


그래프 기울기(graphical slope) 관계:

$$
\underbrace{m}_{\text{중간기울기}}
=
\frac{\underbrace{n}_{\text{Hill n}}\cdot \underbrace{E_{max}}_{\text{천장}}}{\underbrace{4}_{\text{중간점 보정}}}
,\qquad
\underbrace{n}_{\text{추정 n}}
=
\frac{4\underbrace{m}_{\text{관찰 m}}}{\underbrace{E_{max}}_{\text{최대효과}}}
$$


절편 복원(intercept recovery):

$$
\underbrace{C_0}_{\text{절편 C0}}
=
\underbrace{EC_{50}}_{\text{EC50}}
\cdot
\underbrace{e^{-2/n}}_{\text{Hill 보정}}
$$


`[출처: G&W p.219, Eq.3:38–3:42]`

💡 **비유:** Hill $n$은 산길의 경사와 같습니다. 같은 목적지($EC_{50}$)를 향해 가더라도 경사가 급하면 조금만 움직여도 고도, 즉 반응이 크게 달라집니다.


> **Insertion I2 — [TEXTBOOK_DERIVED]** (Audit T3/T5-A SHOULD_FIX: G&W p.200 design message anchor)  
> Sigmoid $E_{max}$/$I_{max}$ 식의 *식별 가능성*은 모델 형태에 의해서만 결정되지 않고 실험 설계에 의해 결정됩니다. G&W p.200은 PD 모델 식별의 최소 설계 요건으로 대조군(control) + 2–4개 용량 수준(dose levels), 그중 적어도 한 용량(dose)이 최대 반응(maximum response)에 도달할 것을 명시합니다. PD3가 이 원칙의 직접 시연입니다 — 0–500 µg/L 설계(design)는 고원부(plateau)에 충분히 닿지 못해 sigmoid 우월성(sigmoid superiority)을 통계적으로 입증하지 못하지만, 0–800 µg/L 설계(design)는 같은 원칙을 만족시켜 모델 판별(model discrimination)을 가능하게 합니다. [G&W p.200, p.734–741]

PD3 혈압 억제 $I_{max}$ 사례(blood-pressure inhibitory $I_{max}$ case)는 초기 그래프 추정치(initial graphical estimate)와 최종 모델 추정치(final model estimate)를 연결합니다. 0–800 µg/L 설계(design)의 sigmoid $I_{max}$ 모델에서 $E_0=171$, $I_{max}=34.7$, $IC_{50}=140$, $n=2.03$, AIC=45.6이 제시되며, 일반 $I_{max}$ 모델(ordinary $I_{max}$ model)은 $E_0=177$, $I_{max}=49.8$, $IC_{50}=175$, AIC=50.8로 비교됩니다. [G&W p.733–735]

PD3가 전달하는 핵심 메시지는 '파라미터 추가는 곧 과적합(overfitting)'이라는 통념이 틀릴 수 있다는 것입니다. Sigmoid 모델에서 $IC_{50}$ 정밀도(precision)가 개선되고 AIC/F-test/VIF가 함께 지지되면, $n$은 단순 장식이 아니라 데이터가 실제로 요구하는 곡률 파라미터(curvature parameter — 곡선 굽힘을 설명하는 파라미터)입니다. [G&W p.734–741]


---

### C. 구조적 필연성(Structural Necessity)

$C^n$이 분자와 분모에 동시에 들어가는 이유는 효과가 농도의 비선형 변환(nonlinear transformation)을 거치더라도 0–$E_{max}$ 경계를 보존해야 하기 때문입니다. $n=1$이면 일반 $E_{max}$로 돌아갑니다. $n>1$이면 농도-반응 전환이 급격해집니다. $n<1$이면 활성 대사체(active metabolite), 다중 수용체 부위(multiple receptor sites), 이질성(heterogeneity) 등의 가능성을 시사할 수 있습니다. 단, 이는 단독 기전 증명(mechanism proof)이 아닙니다. [G&W p.216]


비결합 농도 변환(unbound concentration transformation)에서도 $n$은 보존됩니다.

$$
\underbrace{E}_{\text{효과}}
=
\frac{\underbrace{E_{max}}_{\text{천장}}\underbrace{(C_u/f_u)^n}_{\text{총농도 환산}}}{\underbrace{EC_{50}^n}_{\text{총 EC50}}+\underbrace{(C_u/f_u)^n}_{\text{환산농도}}}
=
\frac{\underbrace{E_{max}}_{\text{천장}}\cdot \underbrace{C_u^n}_{\text{비결합농도}}}{\underbrace{EC_{u50}^n}_{\text{비결합 EC50}}+\underbrace{C_u^n}_{\text{비결합농도}}}
$$


단백결합 차이가 큰 비교에서는 총 $EC_{50}$가 아니라 비결합 $EC_{50}$(unbound $EC_{50}$)를 점검해야 합니다. 그래야 역가(potency) 변화와 단백질 결합(protein binding) 변화를 혼동하지 않습니다. [G&W p.216–217]

💡 **비유:** 총 농도는 항구에 도착한 모든 컨테이너이고, 비결합 농도는 실제로 문을 열고 공장 안으로 들어간 화물입니다. 효과를 만드는 것은 대개 후자입니다.


### C-2. 그럴듯한 오해(Plausible Fallacy): “곡률 억제(Curvature Suppression)”

**오류:** “sigmoid해 보이지만 일반 $E_{max}$(ordinary $E_{max}$)도 대충 맞으니 $n=1$로 단순화합니다.”  
**교정:** PD3는 같은 약물이라도 0–500 µg/L 설계(design)에서는 F-test가 sigmoid 우월성을 통과하지 못하는 반면, 0–800 µg/L로 확장하면 통과함을 보여줍니다. 따라서 올바른 결론은 'sigmoid가 필요 없다'가 아니라, '농도 범위가 곡률(curvature)을 확인하기에 충분한가?'입니다. [G&W p.734–735, p.740–741]

Hill $n$을 “양성 협동성(positive cooperativity)이 증명되었다”라고 쓰면 출처 충실성(source fidelity)이 깨집니다. 독립적인 결합 근거(orthogonal binding evidence)가 없는 한, $n$은 가파름(steepness)과 용량 조절 민감도(dose-titration sensitivity)를 설명하는 현상학적 파라미터로 기술합니다. `[교과서 기반 + 교과서 외 규제 해석]`

> **Insertion I3 — [CRUCIBLE_DERIVED]** (Crucible Intuition #2 / Grade B: Precision-Improvement diagnostic)  
> **체화 신호(Mastery signal) — $IC_{50}$ CV 방향성 진단:** 같은 데이터에 일반 $I_{max}$(ordinary $I_{max}$)와 sigmoid $I_{max}$를 모두 적합했을 때, sigmoid에서 $IC_{50}$의 CV%가 ordinary보다 *향상*된다는 사실 자체가 $n$ 추가의 정당성을 가장 직접적으로 보여주는 신호입니다. PD3 Table 3.2에서 일반 $IC_{50}$ CV가 약 31%였던 것이 sigmoid에서 약 11%로 떨어집니다 — 진정한 과파라미터화(overparameterization)라면 정밀도가 *악화*되어야 하므로, **정밀도 향상 자체가 추가 파라미터가 데이터를 진정으로 설명하고 있다는 직접 증거**입니다. F-test나 AIC가 임계값 근처일 때 이 진단이 결정적인 보조 증거가 됩니다. [G&W p.735 Table 3.2]

> **⚡ Plausible Fallacy — Apex Concept 전용 — [EXPERT_INFERENCE, v3]**  
> **그럴듯한 오해:** "$EC_{50}$만 알면 해당 농도에서 임상 효과를 예측할 수 있습니다."  
> **왜 틀렸는가:** $EC_{50}$은 곡선의 **중간점(midpoint)** 위치만을 결정합니다. 그러나 실제 임상 반응의 *크기*는 $E_{max}$(천장)와 **Hill $\gamma$(가파름)**에 의해 함께 결정됩니다. $\gamma$가 3이면 $EC_{50}$의 ±30% 농도 변화가 반응을 약 20%→80%로 끌어올려 — 치료역이 매우 좁아집니다. 같은 ±30% 변화가 $\gamma=1$에서는 약 40%→60%에 그칩니다. 즉, **같은 $EC_{50}$라도 $\gamma$가 다르면 임상 용량 조절의 정밀도 요구가 완전히 달라집니다.**  
> **실무에서 어떻게 드러나는가:** 용량 조절 가이드라인이나 노출-반응(exposure-response) 보고서에서 $EC_{50}$만 제시하고 $\gamma$를 명시하지 않으면, 좁은 치료역 약물(면역억제제, 항부정맥제, 일부 vitamin K antagonist)에서 용량 조절 폭이 실제보다 *관대하게* 계산될 수 있습니다. 규제 심사 관행상 Hill $\gamma$가 빠진 PK-PD 섹션은 "Hill coefficient의 임상적 의의" 추가 기술 요청(deficiency)을 받기 쉽습니다. **따라서 이 카드의 핵심 결론은 단순합니다 — $\gamma$는 곡선의 미적 디테일이 아니라 임상 안전 마진 그 자체입니다.** `[교과서 기반 + 교과서 외 규제 해석]`

**오류:** $EC_{50}$만 알면 해당 농도에서 임상 효과를 예측할 수 있다고 판단합니다.  
**왜 그럴싸한가:** $EC_{50}$는 곡선의 중간점이라 potency를 대표하는 가장 익숙한 숫자처럼 보입니다.  
**나비효과:** $EC_{50}$ 단독 보고 → Hill $n$ 누락 → [임상] 협역 치료역 약물에서 용량 조절 폭이 과관대해져 독성 또는 치료 실패 예측 실패 → [모델링/규제] exposure-response 보고서에서 Hill coefficient의 임상적 의의 추가 기술 또는 재분석 요구.


### D. 가정과 경계 조건(Assumptions & Boundary Conditions)

- 농도 범위가 $EC_{50}$ 주변과 고원부(plateau)를 충분히 포함해야 $n$과 $E_{max}/I_{max}$가 식별됩니다.
- 기저치 $E_0$가 시간에 따라 변하면 기저치 모델(baseline model)이 필요합니다. `[확인 필요 — G&W §3.12 첨부 PDF 미포함 구간]`
- 목표 농도 역산(target concentration inversion)은 절대 반응(absolute response)과 기저치 상대 반응(baseline-relative response)을 구분해야 합니다. [G&W p.221]

### E. 한계(Limitations)

복합 $E_{max}$(composite $E_{max}$)는 하나의 단순 sigmoid로 설명되지 않는 반응을 두 개 이상의 하위 반응(sub-response)으로 분리합니다. 즉, 관찰된 곡선 하나가 실제 생물학적 과정 하나를 의미한다고 단정하지 않습니다. Lundström et al. 예시는 $IC_{50,1}=1.8$, $IC_{50,2}=23$ µg/L, $I_{max,1}=4$, $I_{max,2}=3.2$, $n_1=1.4$, $n_2=3.7$을 제시합니다. [G&W p.221–223]

다중 결합 부위 모델(multiple binding site model)은 caffeine brain concentration 예처럼 비단조 또는 복합 곡선의 가능성을 보여주지만, 본 세션에서는 “하나의 단일 Hill 곡선(single Hill curve)이 모든 생물학을 증명하지 않는다”는 경계(boundary)로만 둡니다. [G&W p.224]

> 💼 **실무 인사이트:** Sigmoid $E_{max}$ 적합(fitting)은 일반 $E_{max}$/$I_{max}$로 먼저 $E_0/E_{max}/EC_{50}$ 초기값을 잡은 뒤 $n=1$에서 시작합니다. PD3처럼 오차(error)가 커지면 $n$ 정밀도(precision)가 악화될 수 있으므로 “폭발” 같은 표현 대신 CV와 민감도 분석(sensitivity analysis)으로 말합니다. [G&W p.738–739]

> 💼 **실무 인사이트:** 농도 범위 부족 Hill(Range-Starved Hill)은 농도 범위가 $IC_{50}$ 주변과 상단 고원부(upper plateau)를 충분히 건드리지 못하는 상황입니다. 이때 $n$은 1로 수렴하거나 RSE가 커질 수 있습니다. 이는 알고리즘 문제가 아니라 설계 정보(design information) 부족입니다.

### F. 제텔카스텐 원자 노트(Zettelkasten Atom)

**원자 노트 C2(Atom C2):** Hill $n$은 기전의 증명이 아니라 농도-효과 곡선(concentration-effect curve)이 얼마나 급하게 전환되는지를 나타내는 감수성 지렛대(sensitivity lever)입니다. PD3는 그 지렛대가 모델 선택과 농도범위 설계에 어떻게 연결되는지 보여줍니다.

**요약(Recap):** C2는 “곡률(curvature)을 본다”는 것이 단순한 시각적 취향이 아니라 용량 범위(dose range), 정밀도(precision), 목표 농도(target concentration) 해석의 문제임을 고정합니다.

> **C2 체화 핵심**
> ① `용량 증가 시 반응이 급격히 바뀔 때` → Hill $n$이 용량 조절 민감도를 결정
> ② `ordinary vs sigmoid 선택` → 농도 범위와 고원부 도달 여부가 식별 가능성을 지배
> ③ `총 EC50 vs 비결합 EC50 비교` → 단백결합 변화와 역가 변화를 분리
> ⚡ `$n>1$을 협동성 증명으로 단정` → 교과서 경계 초과 → 기전·규제 문장 방어 실패
<!-- 편집 주: [E] 형식 완전 적용 불가 — C2는 Apex 카드로 설계·정밀도·비결합 변환 함의가 모두 핵심이라 4줄 요약으로 확장함 -->

> 📖 **교과서 그림 참조:** Gabrielsson & Weiner 5e, Case Study PD3, p.733 Fig.PD3-3.1; p.735 Table PD3-3.2; p.741 Table PD3-3.4
> 핵심 교훈은 단순히 sigmoid 모델이 더 잘 맞는다는 점만이 아닙니다. 원 PD3 자료는 농도 범위가 모델 판별(model discrimination)과 파라미터 정밀도(parameter precision)를 어떻게 바꾸는지 보여 줍니다.
> 확인 시점: Card C2 §B와 §C-2를 읽은 뒤 확인하면 됩니다.
> 학습 지시: VIF 논의를 읽기 전에 0–500 µg/L 설계와 0–800 µg/L 설계를 비교하세요. 데이터 범위가 $IC_{50}$ 주변의 곡률(curvature)과 상단 반응 영역을 드러내기에 충분히 넓은지 먼저 물어보면 됩니다.


---

<!-- SLIDE_START: C3 | title: 히스테리시스와 시간 지연 진단 -->

## Card C3 — 히스테리시스(Hysteresis): 시간 지연의 진단 도구

> **앞 카드에서 이 카드로:** C2가 정적 농도-반응 곡선의 비선형성을 다루었다면, C3는 같은 농도라도 시간 경로가 다르면 반응이 달라지는 상황을 진단합니다.

> **거장의 시각**
> 히스테리시스를 잡음으로 처리하면 혈장이 효과 부위를 즉시 대표한다는 틀린 가정이 모델에 고정됩니다.
> 고리의 방향과 폭을 먼저 읽으면 직접 연결, 효과 구획, 간접 반응 중 어떤 구조를 시험해야 하는지 즉시 좁혀집니다.


히스테리시스(Hysteresis — 같은 농도에서도 시간 방향에 따라 효과가 달라지는 현상)는 단순히 “농도와 효과가 다르게 움직인다”는 현상이 아닙니다. 오히려 이는 혈장 농도(plasma concentration)가 작용 부위(site of action) 또는 하류 반응(downstream response)을 즉시 대표하지 못한다는 구조적 진단 신호로 읽어야 합니다. R&T Ch.8은 시간(time)이 항상 고려되어야 한다고 시작하며, 단회 투여(single dose) 후 반응(response)이 혈장 농도를 따라가지 않는 사례를 제시합니다. [R&T p.233–235]

즉, 히스테리시스는 그림의 잡음이 아니라 모델 구조(model structure)를 바꾸라는 신호입니다.

### A. 형식적 정의(Formal Definition)

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| 혈장 농도 | 농도 | 관찰 가능한 전신 노출 | 흡수, 분포, 제거, 단백결합 |
| 효과 부위 농도 | 농도 | 반응에 더 가까운 biophase 노출 | 분포 평형화, 투과성, 결합 동역학 |
| 반응 $E(t)$ | 반응 단위 | 시간에 따른 관찰 약효 | 하류 전환, 기저치, 지연, 회복 |
| 고리 방향 | 방향성 | 효과가 농도보다 늦거나 빠른 구조 신호 | 동력학적 지연 또는 역학적 지연 |

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

> 💼 **실무 인사이트:** 히스테리시스 고리를 보면 먼저 (1) 고리 폭(loop width)이 약물 반감기의 몇 배인지, (2) 최대 효과 시점(peak effect time)이 용량 의존적(dose-dependent)인지 확인합니다. 최대 효과 시점이 용량 의존적이면 효과 구획 가능성이 커지고, 용량 비의존적(dose-invariant)이면 전환/간접 반응(turnover/indirect response) 쪽으로 기웁니다.

### F. 제텔카스텐 원자 노트(Zettelkasten Atom)

**원자 노트 C3(Atom C3):** 히스테리시스(Hysteresis)는 모델 선택 전에 보는 탐색적 자료 분석 진단(EDA diagnostic)입니다. 농도-효과 고리(loop)는 “어떤 연결 함수(link function)를 쓸 것인가”보다 먼저 “혈장(plasma)이 효과 부위(effect site)를 대표하는가”를 묻습니다.

**요약(Recap):** C3는 시간 지연을 그림으로 감지하는 단계이며, C4의 효과 구획(effect compartment)과 간접 반응(indirect response)은 이 지연을 구조적으로 흡수하는 방식입니다.

> **C3 체화 핵심**
> ① `같은 농도에서 시간별 반응이 다를 때` → 히스테리시스 고리 방향과 폭이 구조 신호
> ② `시간-농도/효과 도표가 애매할 때` → 농도-효과 고리를 시간 순서로 다시 그림
> ⚡ `히스테리시스를 잡음으로 처리` → 혈장 직접 연결 고정 → delay-source 모델 선택 실패

> 📖 **교과서 그림 참조:** Rowland & Tozer 5e, p.234 Fig.8-1; p.235 Fig.8-2
> 히스테리시스(hysteresis)는 산문만으로는 충분히 이해하기 어렵습니다. 시각적 고리는 같은 혈장 농도라도 농도가 상승 중인지 하강 중인지에 따라 서로 다른 반응값에 대응할 수 있음을 보여 줍니다.
> 확인 시점: Card C3 §A–B를 읽은 뒤 확인하면 됩니다.
> 학습 지시: Fig.8-2에서 고리를 따라 시간 순서의 sampling number를 따라가 보세요. 농도-반응 관계가 하나의 정적인 곡선이 아니라 경로 의존적(path-dependent)이라는 점에 집중하면 됩니다.


---

<!-- SLIDE_START: C4 | title: 효과 구획과 간접 반응 -->

## Card C4 — 효과 구획(Effect Compartment) + 유동 시스템(Systems-in-flux) / 간접 반응(Indirect Response)

> **앞 카드에서 이 카드로:** C3에서 고리로 지연을 보았다면, C4에서는 그 지연이 부위 평형화인지 시스템 전환인지 구조적으로 분해해야 합니다.

> **거장의 시각**
> 효과 구획과 간접 반응을 단순한 delay 보정 패치로 바꾸어 쓰면 외삽 인과가 틀어집니다.
> 지연의 원천을 나누면 투여 간격, onset/offset, 특수 집단 외삽에서 어떤 모델이 더 방어 가능한지 결정됩니다.


C4의 첫 질문은 “반응(response)이 혈장 농도(plasma concentration)를 늦게 따라오는가?”가 아닙니다. 진짜 질문은 **지연(delay)이 작용 부위 평형화(site-of-action equilibration) 때문인가, 아니면 생물학적 시스템 전환(biological system turnover) 때문인가?**입니다. 전자라면 효과 구획(effect compartment)이 더 자연스럽습니다. 후자라면 간접 반응/유동 시스템(indirect response/systems-in-flux)이 더 자연스럽습니다. [R&T p.245–248]

$$
\underbrace{C(t)}_{\text{혈장 농도}}
\rightarrow
\underbrace{C_e(t)}_{\text{효과부위}}
\rightarrow
\underbrace{E(t)}_{\text{관찰반응}}
$$


### A. C4a. 효과 구획(Effect Compartment)

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $C(t)$ | 농도 | 혈장 농도 시간 경과 | 흡수, 분포, 제거 |
| $C_e(t)$ | 농도 | 효과 부위 농도 또는 lumped delay 상태 | 부위 평형화, 투과성, 결합 지연 |
| $k_{e0}$ | 시간$^{-1}$ | 효과 부위 평형화 속도 | 조직 분포, 결합/해리, sampling 정보 |
| $E(t)$ / $R(t)$ | 반응 단위 | 관찰 반응 또는 전환 변수 | 시스템 회복, $k_{in}/k_{out}$, feedback |

💡 **지연 원천 구분** — 같은 히스테리시스라도 $C_e(t)$ 지연과 turnover 지연은 서로 다른 외삽을 만듭니다.

효과 구획(effect compartment — 혈장과 반응 사이 지연을 흡수하는 가상 구획)은 혈장 농도와 반응을 연결하기 위해 도입한 가설적 구획(hypothetical compartment)입니다. R&T는 naproxen 히스테리시스를 효과 구획을 통해 줄이고, 효과 부위 농도(effect-site concentration)와 반응을 더 직접적으로 연결하는 그림을 제시합니다. [R&T p.245–246]

이 구획은 미시적 장기 구획(microscopic organ compartment)이 아니라 총괄 지연 표현(lumped delay representation — 여러 지연 원인을 하나로 묶은 표현)입니다. 조직 관류(tissue perfusion), 투과성(permeability), 조직 친화도, 결합 동역학(binding kinetics), 신호전달 지연(signal transduction lag)이 복합적으로 반영된 결과일 수 있습니다. 따라서 $k_{e0}$를 특정 생리상수처럼 외삽하지 않습니다. [R&T p.235–236, p.245–246]


### B. C4b. 유동 시스템(Systems-in-flux) / 간접 반응(Indirect Response)

유동 시스템(systems-in-flux)에서는 약물이 내인성 물질(endogenous substance) 또는 생리적 반응의 생성/소멸 과정(formation/loss process)을 바꿉니다. Warfarin은 프로트롬빈 복합체 전환(prothrombin complex turnover)을 통해 혈장 농도와 효과가 분리되는 대표 예입니다. Sodium warfarin 1.5 mg/kg 경구 투여 후 프로트롬빈 복합체 반응은 전환 반감기(turnover half-life) 1–2일의 영향을 받습니다. 즉, 혈장 농도가 변해도 반응은 시스템 회복 속도에 묶입니다. [R&T p.241–248]

일반 전환 골격(general turnover skeleton)은 다음과 같습니다.

$$
\underbrace{\frac{dR}{dt}}_{\text{반응 변화}}
=
\underbrace{k_{in}}_{\text{생성}}
-
\underbrace{k_{out}R}_{\text{소실}}
$$


💡 **비유:** 효과 구획은 약물이 표적 방까지 가는 복도 지연이고, 간접 반응은 표적 방 안의 생산라인이 천천히 바뀌는 지연입니다. 복도 문제와 생산라인 문제는 같은 delay처럼 보여도 수리 방법이 다릅니다.

약물은 $k_{in}$ 또는 $k_{out}$을 자극(stimulation)/억제(inhibition)할 수 있습니다. 본 식은 G&W 비정상상태 반응 체계(non-steady-state response framework)와 R&T 유동 시스템 설명을 연결하는 최소 골격입니다. [G&W p.229–230; R&T p.241–248]


### C. 구조적 필연성(Structural Necessity)

효과 구획은 혈장과 효과 부위 사이의 평형화 지연(equilibration delay)을 흡수합니다. 간접 반응은 반응 변수 자체가 느린 전환율(turnover)을 갖기 때문에 지연이 생깁니다. 이 둘을 구분하지 않으면 현재 데이터에 대한 적합은 비슷해 보여도 외삽 결과가 달라집니다. 특히 용량 변경이나 투여 간격 변경 상황에서 예측 오차가 크게 벌어집니다.

**용량 비의존적 최대 효과 시점 진단(dose-invariant peak time diagnostic):** 간접 반응에서는 최대 효과가 $dR/dt=0$ 조건, 즉 유입/유출 균형(input/output balance)에 의해 결정됩니다. 용량이 반응 진폭(response amplitude)을 바꿔도 시스템 전환 시간 척도가 변하지 않으면 최대 효과 시점이 거의 일정할 수 있습니다. 효과 구획에서는 용량과 농도-시간 양상(concentration-time profile)이 효과 부위 평형화의 모양을 바꿉니다. 따라서 최대 효과 시점이 용량 의존적이 될 가능성이 큽니다. `[교과서 기반 개념 + 실무 진단 번역]`

$$
\underbrace{\frac{dR}{dt}}_{\text{반응 변화}}=\underbrace{0}_{\text{peak/평형}}
\quad\Longleftrightarrow\quad
\underbrace{\text{input}}_{\text{유입}}=
\underbrace{\text{output}}_{\text{유출}}
$$

### D. 가정(Assumptions)

- 효과 구획(effect compartment)은 가설적 연결(hypothetical link)이며 실제 출처 구획(source compartment)이 아닙니다. [R&T p.245]
- 간접 반응(indirect response)은 내인성 시스템(endogenous system)의 생성/소멸 과정(formation/loss process)을 전제로 합니다. [R&T p.241–248]
- Warfarin-like 반응에서는 혈장 농도(plasma concentration)가 빨리 변해도 반응(response)은 프로트롬빈 복합체 전환(prothrombin complex turnover)에 의해 느리게 변합니다. [R&T p.242, p.247]

### E. 한계(Limitations)

NONMEM `$DES`, 격자 탐색(grid search), ETA 배치는 R&T 원문이 아니라 구현 계층(implementation layer)입니다. 본 자료에서는 모델링 실무로 연결할 때만이라고 명시합니다.

> 💼 **실무 인사이트:** 히스테리시스 모델 선택은 혈장 직접(plasma direct) → 효과 구획 → 간접 반응 순서로 적합합니다. 각 단계에서 용량 군별 최대 효과 시점의 용량 의존성이 사라지는지 봅니다. 효과 구획에서 충분히 사라지면 분포 지연이 주원인이고, 간접 반응에서만 설명되면 전환 시스템이 본질입니다.

> 💼 **실무 인사이트:** PK와 혼동된 $k_{e0}$(PK-Aliased $k_{e0}$)는 추정된 효과 반감기(estimated effect half-life)가 혈장 반감기와 너무 가까워 $k_{e0}$와 제거 속도(elimination rate)가 분리되지 않는 패턴입니다. 이때 $k_{e0}$ 수치 자체보다 밀집 채혈(dense sampling) 또는 민감도 분석(sensitivity analysis)이 더 중요합니다.

### F. 제텔카스텐 원자 노트(Zettelkasten Atom)

**원자 노트 C4(Atom C4):** 효과 구획(effect compartment)은 “작용 부위 평형화 지연(site equilibration delay)”, 간접 반응(indirect response)은 “시스템 전환 지연(system turnover delay)”을 설명합니다. 히스테리시스를 줄이는 적합(fit)보다 더 중요한 것은 어떤 지연(delay)을 외삽할 것인지의 구조 선택입니다.

**요약(Recap):** C4는 C3에서 감지한 시간 지연을 구조화합니다. 같은 고리라도 분포 문제인지 시스템 전환 문제인지에 따라 투여 간격(dosing interval), 발현 예측(onset 예측), 특수 집단 외삽(special population extrapolation)이 달라집니다.

> **C4 체화 핵심**
> ① `효과가 혈장보다 늦을 때` → $C_e(t)$ 평형화 지연인지 먼저 확인
> ② `최대 효과 시점이 용량 비의존적일 때` → turnover/indirect response 가능성이 지배
> ⚡ `$k_{e0}$를 생리 상수처럼 외삽` → lumped delay 오해 → 투여 간격·특수집단 예측 실패

> 📊 **개념 도식 (HTML에서 렌더링):** 지연 원천 위상(delay-source topology): 효과 부위 평형화(effect-site equilibration) vs 시스템 전환(system turnover) — 효과 구획(effect compartment)과 간접 반응(indirect response)은 서로 바꿔 쓸 수 있는 지연 보정 패치가 아닙니다. 두 구조는 서로 다른 인과 구조를 담고 있습니다.


---

<!-- SLIDE_START: C5 | title: AUEC와 지속 시간 -->

## Card C5 — AUEC + 지속 시간(Duration) + PK/PD 율속(Rate-Limiting)

> **앞 카드에서 이 카드로:** C4가 지연의 원천을 구조화했다면, C5는 그 지연이 반응 총량과 효과 지속 시간으로 어떻게 누적되는지 읽습니다.

> **거장의 시각**
> 혈장 반감기로 효과 지속 시간을 요약하면 PD 율속 약물에서 가장 느린 회복 과정을 지워버립니다.
> AUEC와 duration을 반응-시간 지표로 보면 투여 간격은 약물 제거가 아니라 시스템 회복 척도로 결정될 수 있음을 확인할 수 있습니다.


효과 지속 시간은 약물 반감기(drug half-life)만으로 결정되지 않습니다. 혈장 농도(plasma concentration)가 사라져도 반응(response)이 남는 경우는 흔합니다. 이때 율속은 PK 제거(PK elimination)가 아니라 수용체 결합(receptor binding), 비가역적 작용(irreversible action), 표적 전환(target turnover), 하류 시스템 회복(downstream system recovery)일 수 있습니다. [R&T p.249–253]

Methylprednisolone 예시는 PK AUC가 용량 비례적(dose-proportional)이어도 림프구 반응(lymphocyte response)은 고용량(high-dose) 구간에서 포화(saturate)될 수 있음을 보여줍니다. 즉 PK 선형성(PK linearity)은 PD 선형성(PD linearity)을 보장하지 않습니다. [R&T p.257–258]

### A. 형식적 정의(Formal Definition)


AUEC(← 반응-시간 곡선 아래 면적, area under the effect curve)는 반응-시간 곡선을 하나의 면적값으로 요약한 지표입니다.

$$
\underbrace{AUEC}_{\text{반응 총량}}
=
\int_{\underbrace{0}_{\text{시작}}}^{\underbrace{\infty}_{\text{추적 끝}}}
\underbrace{E(t)}_{\text{순간반응}}\,dt
$$


| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| AUEC | 반응×시간 | 전체 반응 부담 또는 총 효과량 | $E(t)$ 크기, 지속 시간, 시스템 회복 |
| $E(t)$ | 반응 단위 | 순간 반응 | 농도 입력, $E_{max}$/Hill, 지연 구조 |
| $D$ | 용량 | 입력량 | 투여 설계, 생체이용률, 투여 경로 |
| $K$ | 시간$^{-1}$ | 1차 감소 속도 | 제거 또는 효과 감소 과정 |
| $A_{min}$ | 양 또는 효과 기준 | 최소 유효량/역치 | endpoint 정의, 임상 목표 |

💡 **비유:** AUEC는 순간속도계가 아니라 여행 전체의 이동거리입니다. 짧게 강한 반응과 길게 약한 반응은 같은 면적을 만들 수 있으므로, 면적만 보고 시간 구조를 지우면 안 됩니다.

> **Insertion I4 — [TEXTBOOK_DERIVED]** (Audit T1 RESTORED/PARTIAL: G&W §3.6.6 Non-Steady-State Response framework bridge)  
> AUEC는 진공 속에서 정의되지 않습니다. G&W §3.6.6은 비정상상태 반응(non-steady-state response)의 동력학 틀(framework)을 제공합니다 — 약물 농도(drug concentration)가 시간에 따라 변하면 반응(response)도 비정상상태로 변하며, 그 결과 곡선의 모양은 입력(input, concentration-time)의 모양과 반응 시스템(response system, $E_{max}$/Hill)의 비선형성에 의해 동시에 결정됩니다. AUEC는 그 틀(framework)이 만들어낸 결과 곡선을 적분한 면적 요약 지표이며, 따라서 폐쇄형 식(closed form)은 틀의 가정(일반 $E_{max}$ + 1차 제거, ordinary $E_{max}$ + first-order elimination) 아래에서만 가능합니다. [G&W p.229–234, Eq.3:56–3:73]


1구획 1차 제거(one-compartment first-order elimination)와 일반 $E_{max}$ 모델(ordinary $E_{max}$ model)에서 G&W는 다음 폐쇄형 식(closed form)을 제시합니다.

$$
\underbrace{AUEC}_{\text{AUEC}}
=
\underbrace{\frac{E_{max}}{K}}_{\text{천장×시간}}
\ln\left(
1+
\underbrace{\frac{D}{EC_{50}\cdot V}}_{\text{용량/감수성}}
\right)
$$


`[출처: G&W p.233–234, Eq.3:72–3:73]`

💡 **비유:** 로그식 duration은 물통을 두 배 크게 한다고 배수 시간이 두 배가 되지 않는 상황과 같습니다. 감소가 1차 과정이면 용량 증가는 지속 시간을 선형이 아니라 로그로 늘립니다.

Sigmoid $E_{max}$에서는 동일한 폐쇄형 식(closed form)이 출처(source)에 제시되지 않았습니다. 따라서 수치 적분(numerical integration) 필요성은 `[수학적 추론]`으로만 표시합니다.


### B. 효과 지속 시간(Duration of Effect)

R&T는 반응 감소(response decline)의 중간 영역(약 80–20% 최대치)에서 반응이 시간에 대해 거의 선형적으로 감소할 수 있음을 설명합니다. 또한 지속 시간이 용량의 로그(logarithm)에 비례하는 관계를 제시합니다. [R&T p.249, p.254–256]

$$
\underbrace{t_D}_{\text{지속시간}}
=
\underbrace{\frac{1}{K}}_{\text{감소시간}}
\ln\left(
\underbrace{\frac{D}{A_{min}}}_{\text{용량/역치}}
\right)
$$


용량을 두 배로 늘리면 조건이 맞을 때 지속 시간은 약 반감기 1회분만큼 증가합니다. Succinylcholine 0.5 mg/kg 정맥 급속 투여 예시는 $k\approx0.2\ \mathrm{min}^{-1}$, $t_{1/2}\approx4$ min의 효과 감소와 용량-지속 시간 관계를 보여줍니다. 여기서 핵심은 용량 증가가 최대 효과(peak effect)보다 지속 시간을 더 읽기 쉽게 바꿀 수 있다는 점입니다. [R&T p.249–256]


### C. PK 율속(PK-rate-limited) vs PD 율속(PD-rate-limited)

- **PK 율속(PK-rate-limited):** 효과가 사라지는 속도가 약물 농도가 사라지는 속도에 의해 결정되는 경우입니다. 즉, 효과 감소(effect decline)가 혈장 농도 감소(plasma concentration decline)와 같은 시간 척도에서 움직입니다.
- **PD 율속(PD-rate-limited):** 효과가 사라지는 속도가 수용체/시스템(receptor/system) 회복 속도에 의해 결정되는 경우입니다. 혈장 농도(plasma concentration)는 빠르게 사라지더라도, 반응(response)은 수용체/시스템 전환(receptor/system turnover)이 완료될 때까지 오래 지속됩니다.

Aspirin은 650 mg 경구 투여 후 혈장 $t_{1/2}$가 약 15 min이지만 항혈소판 활성(antiplatelet activity)이 수일간 지속되는 예입니다. 즉, 혈장에서 약물이 빨리 사라져도 반응 시스템은 더 늦게 회복될 수 있습니다. [R&T p.251]

Omeprazole은 40 mg 경구 투여 후 혈장 $t_{1/2}$가 1시간 미만이고 약 3시간 후 혈장에는 거의 남지 않지만, 위산 분비 억제(gastric acid secretion inhibition)는 수일 단위로 회복됩니다. [R&T p.252]

Paclitaxel은 혈장에는 2일 후 거의 남지 않지만 백혈구 분율(leukocyte fraction) 변화가 수주(weeks) 척도로 움직이는 예입니다. [R&T p.253]

Acenocoumarol과 phenprocoumon 비교에서는 acenocoumarol $t_{1/2}$ 15시간, phenprocoumon $t_{1/2}$ 6일 및 반응 회복 시간(response recovery time) 차이가 PK vs PD 율속 판단의 교육적 앵커가 됩니다. [R&T p.243–244]

$$
\underbrace{t_{1/2}}_{\text{혈장 t1/2}}
\quad\text{vs}\quad
\underbrace{t_{recovery}}_{\text{회복시간}}
$$

> **Insertion I5 — [TEXTBOOK_DERIVED]** (Audit T6 ESSENTIAL: Acenocoumarol/Phenprocoumon PK vs PD rate-limiting anchor 강화)  
> Acenocoumarol($t_{1/2}$ 15 h, 기저치 회복 약 3 days)과 phenprocoumon($t_{1/2}$ 6 days, 기저치 회복 약 2 weeks)의 직접 비교는, **같은 vitamin K antagonist 계열 안에서도 PK 율속(PK rate-limited)과 PD 율속(PD rate-limited) 패턴이 약물별로 갈라질 수 있음**을 보여주는 R&T의 교육적 앵커입니다. Acenocoumarol에서는 혈장 제거(plasma elimination) 속도와 프로트롬빈 복합체(prothrombin complex) 회복 속도가 같은 시간 척도에 가까워 PK가 율속에 더 가깝지만, phenprocoumon에서는 혈장 반감기(plasma half-life)가 시스템 전환(system turnover) 시간 안에 들어가 PD-system이 율속의 일부가 됩니다. **이 비교는 “PK/PD 율속(rate-limiting)은 약물 분류 라벨이 아니라 두 시간 척도의 비율($\tau_{drug}/\tau_{system}$)에서 결정되는 스펙트럼(spectrum)”이라는 framing을 직접 가르칩니다.** [R&T p.243–244, Fig.8-11]

### D. 가정(Assumptions)

- AUEC 폐쇄형(closed form)은 일반 $E_{max}$ + 1차 제거(first-order elimination) 조건에서만 출처에 근거합니다. [G&W p.233]
- 지속 시간-로그 용량 관계(duration log-dose relation)는 최소 유효량(minimum effective amount), 1차 감소(first-order decline), 일정한 역치(threshold) 등의 조건을 전제로 합니다. [R&T p.254–255]
- PD 율속 예시(PD-rate-limited example)는 “약물이 아직 많다”가 아니라 “시스템(system)이 아직 회복되지 않았다”는 뜻일 수 있습니다. [R&T p.249–253]

### E. 한계(Limitations)

Aspirin 75 mg, 수술 전후 7일 중단, 출혈 가이드라인은 본 PDF 출처 밖이므로 삭제합니다. 이 세션에서 출처 기반으로 고정되는 aspirin 문장(source-grounded aspirin statement)은 650 mg oral, $t_{1/2}$ 15 min, 항혈소판 활성(antiplatelet activity) several days까지만입니다. [R&T p.251]

특수 집단 용량 조정(special population dose adjustment)에서 PK 변화만 보고 투여 간격을 정하면 PD 율속 약물에서는 과소 또는 과대 조정이 생길 수 있습니다. 단, 특정 label/guidance 조항은 본 PDF 범위 밖입니다. 따라서 해당 적용은 `[확인 필요 — 교과서 외 규제 적용]`으로 남깁니다.

> 💼 **실무 인사이트:** 도표(plot)의 x축(x-axis)이 한 자리 이상 다른 시간 단위로 벌어지면 PD 율속(PD-rate-limited) 가능성이 큽니다. Aspirin은 혈장 도표(plasma plot)가 hours, 항혈소판 효과 도표(antiplatelet effect plot)가 days scale로 보입니다. 따라서 “농도 주도 지속 시간(concentration-driven duration)”이라는 직관을 즉시 버려야 합니다. [R&T p.251]

> 💼 **실무 인사이트:** 용량-반응이 고용량에서 평탄해지면 더 높은 용량이 정보를 늘리는 것이 아니라 고원부를 반복 확인할 가능성이 큽니다. Methylprednisolone처럼 PK AUC는 증가해도 PD 반응이 포화되면 하류 바이오마커(downstream biomarker) 또는 투여 간격 종말점(dosing interval endpoint)을 다시 설계합니다. [R&T p.257–258]

### F. 제텔카스텐 원자 노트(Zettelkasten Atom)

**원자 노트 C5(Atom C5):** AUEC와 지속 시간은 농도-시간 곡선을 반응-시간 곡선으로 번역한 면적·시간 지표입니다. 효과 지속성(effect persistence)은 약물 반감기가 아니라 더 느린 과정이 결정합니다.

**요약(Recap):** C5는 “농도가 없어졌는데 효과가 남는다”는 현상을 예외가 아니라 PD 모델링의 핵심 설계 문제로 바꿉니다.

> **C5 체화 핵심**
> ① `투여 간격 설계` → $\tau_{drug}/\tau_{system}$ 비율이 PK/PD 율속을 결정
> ② `AUEC 또는 duration 보고` → 역치·반응 변수·시간 척도 정의가 지배
> ⚡ `혈장 반감기=효과 지속 시간` → PD 율속 회복 과정 삭제 → 지속 시간 예측 실패

> 📖 **교과서 그림 참조:** Rowland & Tozer 5e, p.251 Fig.8-20; p.252 Fig.8-21
> 이 예시들은 혈장 반감기(plasma half-life)와 효과 지속 시간(effect duration)을 반드시 분리해서 보게 합니다. 시각적으로 드러나는 시간축의 간격이 핵심 구조 신호입니다.
> 확인 시점: Card C5 §C를 읽은 뒤 확인하면 됩니다.
> 학습 지시: 혈장 농도 시간 경과(plasma concentration time course)와 반응 시간 경과(response time course)를 비교하세요. 이 그림에서 aspirin의 수술 전후 지침이나 omeprazole의 임상 규칙을 추론하지 마세요. 이 그림은 PD 율속 지속성(PD-rate-limited persistence)을 알아보는 용도로만 사용하면 됩니다.


> 📖 **교과서 그림 참조:** Rowland & Tozer 5e, p.255 Fig.8-23; p.256 Fig.8-24
> 지속 시간 식은 간결하지만, 학습자는 용량 변화가 역치 통과 시간(threshold-crossing time)으로 어떻게 번역되는지 직접 보아야 합니다. Fig.8-24는 이 추상적 관계를 succinylcholine 예시에 고정해 줍니다.
> 확인 시점: Card C5 §B를 읽은 뒤 확인하면 됩니다.
> 학습 지시: 각 용량 곡선이 최소 유효량/효과 역치(minimum effective amount/effect threshold)를 어디에서 통과하는지 따라가 보세요. 그런 다음 그 통과 시간을, 명시된 가정 아래에서 용량을 두 배로 늘리면 지속 시간이 약 한 번의 반감기만큼 연장될 수 있다는 문장과 연결하면 됩니다.


---

<!-- SLIDE_START: §5 | title: 혼동 쌍 해부 -->

# §5 — 혼동 쌍 해부


## 혼동 쌍 1(Pair 1) — $K_d$ vs $EC_{50}$

| 비교 기준 | $K_d$ | $EC_{50}$ |
|---|---|---|
| 단위 / 차원 | 농도 | 농도 |
| 수식 내 위치 (분자/분모/지수) | 결합 점유율 식의 분모에서 $[C]+K_d$ 구성 | 기능 반응식의 분모에서 $EC_{50}+C$ 또는 $EC_{50}^n+C^n$ 구성 |
| 변화 원인 (생물학적/병적) | 리간드-수용체 결합 변화 | 결합, 수용체 밀도, 증폭 이득, 조직 반응 변화 모두 가능 |
| 혼동 시 임상 결과 | 결합 친화도를 기능적 역가로 오인 | 공변량 효과를 수용체 감수성 변화로 과해석 |

**⚡ 기억 고리 (Memory Hook) — *결합 vs 효능*: [EXPERT_INFERENCE, v3]**  
$K_d$는 약물이 수용체에 *얼마나 잘 붙는가* — 분자 수준의 친화도입니다. $EC_{50}$는 *그 결합이 조직과 신호 시스템을 거쳐 절반의 효과로 나오기까지 필요한 농도* — 시스템 수준의 효능입니다. 둘이 다를 수 있는 이유는 수용체 점유율(receptor occupancy)과 기능적 반응(functional response) 사이에 여분 수용체(spare receptor)와 연쇄 증폭(cascade amplification)이라는 증폭 단계가 끼기 때문입니다. 따라서 $EC_{50}<K_d$도 가능합니다 — *수용체 10%만 점유해도 90% 효과가 나오는* 조직(tissue)이 존재하기 때문입니다. **결합은 분자, 효능은 시스템 — 같은 층위가 아닙니다.**

**핵심 교정(Critical Correction):** $EC_{50}$가 공변량에 따라 변하면 그것이 약물 측 결합(drug-side binding) 변화인지 시스템 측 감수성(system-side sensitivity) 변화인지 구분해야 합니다. 비결합 농도와 결합 증거(binding evidence) 없이 총 $EC_{50}$ 변화만으로 기전을 단정하지 않습니다. 이 구분이 없으면 공변량 효과를 생물학적 감수성 변화로 과해석하기 쉽습니다. [G&W p.203–206, p.215–217]


## 혼동 쌍 2(Pair 2) — 일반 $E_{max}$ ($n=1$) vs Sigmoid $E_{max}$ ($n\neq1$)

| 비교 기준 | 일반 $E_{max}$ | Sigmoid $E_{max}$ |
|---|---|---|
| 단위 / 차원 | $n=1$ 고정, $E_{max}$와 $EC_{50}$ 중심 | $n$은 무차원, $E_{max}$와 $EC_{50}$에 가파름 추가 |
| 수식 내 위치 (분자/분모/지수) | $C$와 $EC_{50}$가 1차 항 | $C^n$와 $EC_{50}^n$가 지수 항 |
| 변화 원인 (생물학적/병적) | 완만한 쌍곡선 전환 | 급격하거나 완만한 전환, 이질성 또는 가능한 기전 가설 |
| 혼동 시 임상 결과 | 고원부 없는 데이터에서 $E_{max}$ 식별 불안정 | 농도범위가 좁으면 $n$ 식별 불안정, 안전 마진 과대평가 |

**⚡ 기억 고리 (Memory Hook) — *중간점 vs 가파름*: [EXPERT_INFERENCE, v3]**  
$EC_{50}$은 곡선의 **중간점 위치(midpoint)**입니다 — x축 위에서 반응의 절반이 나오는 농도, 즉 *어디에서* 효과의 절반에 도달하는지를 말합니다. Hill $\gamma(=n)$은 곡선의 **가파름(steepness)**입니다 — $\gamma$가 1이면 완만한 S자, $\gamma$가 5면 거의 계단 함수에 가까우며, 즉 *얼마나 좁은 농도 구간에서* 0%에서 100%로 전환되는지를 말합니다. 두 파라미터는 수학적으로 독립입니다 — $EC_{50}$이 낮아도(sensitive) $\gamma$가 낮으면(완만) 임상 허용 폭이 넓고, $EC_{50}$이 높아도(potency 낮음) $\gamma$가 높으면(가파름) 작은 농도 차이가 독성/무효의 경계를 가릅니다. **협역 치료역 약물에서 임상적으로 더 위험한 파라미터는 $EC_{50}$이 아니라 $\gamma$입니다 — 위치보다 가파름이 안전 마진을 결정합니다.**

| **치명적 타격 (Critical Blow) — [EXPERT_INFERENCE, v3]** | Hill $\gamma$를 보고서에서 생략하고 $EC_{50}$만으로 dose-response를 제출하면, 협역 치료역 약물(면역억제제, 항부정맥제, 일부 vitamin K antagonist)에서 위험이 생깁니다. 이러한 약물은 용량-반응 전환이 급격하므로, $\gamma$ 없이 설계된 임상 용량 조절 가이드는 *과관대하게* 설정되어 독성 발생률을 과소예측할 수 있습니다. 규제 심사관은 "Hill coefficient의 임상적 의의" 섹션을 추가하라는 deficiency를 발행하는 것이 일반적인 관행이며, 이는 NDA/BLA 검토 일정의 직접 지연으로 이어집니다. `[교과서 외 규제 해석]` |

$n>1$은 "협동성 증명(cooperativity 증명)"이 아닙니다. 이는 가설을 제시할 수 있지만 증명하지는 않는 현상학적 가파름 파라미터(phenomenologic steepness parameter)입니다. [G&W p.216, p.220]


## 혼동 쌍 3(Pair 3) — PK 율속 vs PD 율속 감소

| 비교 기준 | PK 율속(PK-rate-limited) | PD 율속(PD-rate-limited) |
|---|---|---|
| 단위 / 차원 | 혈장 농도 감소 시간 척도 | 반응 회복 또는 시스템 전환 시간 척도 |
| 수식 내 위치 (분자/분모/지수) | 혈장 $t_{1/2}$ 또는 제거 속도 중심 | $t_{recovery}$, $\tau_{system}$, turnover 중심 |
| 변화 원인 (생물학적/병적) | 약물 제거/분포 | 수용체 결합, 비가역적 작용, 전환, 하류 회복 |
| 혼동 시 임상 결과 | 혈장과 반응이 유사한 시간 척도라는 전제 | aspirin/omeprazole/paclitaxel처럼 효과 지속 시간을 과소예측 |

**치명적 타격(Critical Blow):** 약물 반감기가 짧다고 해서 효과 지속 시간도 짧다고 결론지으면, PD 율속 약물에서는 틀린 판단이 됩니다. Aspirin은 혈장 $t_{1/2}$ 약 15 min이지만 항혈소판 활성은 수일간 지속됩니다. Omeprazole도 혈장은 빠르게 사라지지만 위산 억제는 수일 척도로 회복됩니다. 따라서 투여 간격 판단에는 혈장 반감기뿐 아니라 반응 회복 시간(response recovery time)이 필요합니다. [R&T p.251–252]

> **Insertion I6 — [CRUCIBLE_DERIVED]** (Crucible Intuition #3 / Grade A: Time-axis fast-diagnostic)  
> **시각적 빠른 진단(Visual fast-diagnostic) — 0.5초 식별:** 도표(plot)의 x축(x-axis) 단위가 한 자리수 이상 차이 나면(예: aspirin 혈장 도표는 0–2 hours, 항혈소판 효과 도표는 0–192 hours) PD 율속(PD-rate-limited)으로 즉시 확정할 수 있습니다. 같은 시간축에서 두 곡선이 비슷한 모양이면 PK 율속(PK-rate-limited)입니다. **이 진단은 적합 통계량(fit statistic)이나 모델 비교 이전에 EDA 단계에서 도표의 시간 축만 보아도 가능합니다 — 두 도표가 *다른 시간 척도*에서 그려졌다는 사실 자체가 율속 과정(rate-limiting process)이 다르다는 직접 증거이기 때문입니다.** [R&T p.251–253; PD-rate-limited 시각 진단의 source anchor]


## 혼동 쌍 4(Pair 4) — 직접 연결 / 효과 구획 vs 간접 반응

| 비교 기준 | 직접 / 효과 구획(Effect Compartment) | 간접 반응(Indirect Response) |
|---|---|---|
| 단위 / 차원 | $C(t)$ 또는 $C_e(t)$ 농도 축 | $R(t)$ 반응량과 $k_{in}/k_{out}$ 시간 축 |
| 수식 내 위치 (분자/분모/지수) | 혈장→효과 부위→반응 연결 | 생성/소멸 미분방정식 안의 input/output 항 |
| 변화 원인 (생물학적/병적) | 혈장-작용 부위 평형화 또는 효과 부위 농도 지연 | 내인성 반응 변수의 생성/소멸 지연 |
| 혼동 시 임상 결과 | $k_{e0}$를 미시적 생리 상수로 오해 | $k_{in}/k_{out}$을 단순 곡선 적합 파라미터로 오해 |

**빠른 진단(Fast Diagnostic):** 히스테리시스 고리의 폭과 최대 효과 시점의 용량 의존성을 먼저 봅니다. 용량 의존적 최대 효과 시점이면 효과 구획 가능성, 용량 비의존적 최대 효과 시점이면 간접 반응 가능성이 커집니다. 이 판단은 적합 통계량(fit statistic)보다 먼저 보는 구조 진단입니다.

**요약(Recap):** 가장 위험한 혼동은 “농도가 반응(response)을 즉시 구동한다”는 가정입니다. 이 가정이 깨지는 순간 $K_d$/$EC_{50}$, $E_{max}$/Hill, 효과 구획/간접 반응(effect compartment/indirect response), PK/PD 율속(PK/PD rate-limiting)이 모두 연결됩니다.

> **§5 체화 핵심 — [EXPERT_INFERENCE]**  
> 네 개의 혼동 쌍(confusion pair)는 모두 같은 질문으로 환원됩니다: “현재 숫자는 결합(binding), 부위 농도(site concentration), 측정 반응(measured response), 시스템 회복(system recovery) 중 어느 층위를 대표하는가?” 이 층위를 분리하면 파라미터 명명(parameter naming)은 단순 암기가 아니라 모델 구조 검토가 됩니다.

---

<!-- SLIDE_START: §7 | title: 자기 테스트: 능동 회상 모듈 -->

# §7 — 자기 테스트: 능동 회상 모듈

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

**정답:** 먼저 혈장 직접 모델(plasma direct model)로 모델 오명세(misspecification)의 크기를 봅니다. 다음으로 효과 구획을 적용해 히스테리시스가 줄어드는지 확인합니다. 그래도 용량 군별 최대 효과 시점이 용량 비의존적이거나 반응 회복이 시스템 시간 척도를 보이면 간접 반응을 검토합니다. 즉, 모델 선택은 AIC만으로 하지 않습니다. 최대 효과 시점의 용량 의존성, 채혈 밀도(sampling density), 생물학적 타당성(biological plausibility)을 함께 봅니다.

---

<!-- SLIDE_START: §8 | title: 메타 프레임과 큰 그림 -->

# §8 — 메타 프레임과 큰 그림

## A. 위치와 실패 모드

이 세션은 PK/PD 구조(PK/PD architecture)에서 “농도-시간 프로파일(concentration-time profile)을 반응-시간 프로파일(response-time profile)로 변환하는 첫 관문”입니다. C1–C2는 농도-반응 비선형성(concentration-response nonlinearity)을 담당합니다. C3–C4는 시간 지연(time delay)을, C5는 반응 적분/지속 시간(response integration/duration)을 담당합니다.

이 세션을 대충 넘기면 다음 실패가 발생합니다.

1. **$K_d$를 $EC_{50}$처럼 사용:** 결합 친화도를 기능적 역가(functional potency)로 오인합니다.
2. **Hill $n$을 기전 증명으로 과해석:** 곡선 적합 파라미터를 생물학적 증거로 둔갑시킵니다.
3. **히스테리시스를 잡음으로 처리:** 부위 평형화 또는 전환 지연을 놓칩니다.
4. **PK 반감기로 투여 간격을 결정:** PD 율속 반응에서 지속 시간을 잘못 예측합니다.
5. **AUEC를 단순 AUC처럼 취급:** 반응 적분의 모델 조건을 잊습니다.


| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| $K_d$를 $EC_{50}$처럼 사용 | 결합/기능 층위 | → | 기능적 역가 오인 | assay source와 unbound 기준 확인 |
| Hill $n$을 기전 증명으로 과해석 | 가파름 파라미터 | → | 용량 조절 위험 과소평가 | 농도 범위·고원부·정밀도 동시 검토 |
| 히스테리시스를 잡음으로 처리 | 시간 지연 | → | delay-source 누락 | 고리 방향·폭·peak-time 진단 |
| PK 반감기로 투여 간격 결정 | $t_{1/2}$ vs $t_{recovery}$ | → | PD 율속 반응 지속 시간 오판 | $\tau_{drug}/\tau_{system}$ 비교 |
| AUEC를 단순 AUC처럼 취급 | 반응 적분 | → | endpoint 정의 누락 | 역치·반응 변수·시간 척도 명시 |

## B. 전문가 해석 지점

계량약리학자(pharmacometrician)의 해석 지점은 복잡한 식을 많이 아는 데 있지 않습니다. 같은 농도-효과 데이터를 두고 무엇이 부족한지 구분할 줄 아는 데 있습니다. 더 좋은 최적화기(optimizer)가 필요한가, 더 넓은 농도 범위가 필요한가, 더 가까운 바이오마커가 필요한가, 아니면 더 긴 반응 채취(response sampling)가 필요한가 — 이 네 갈래를 구분할 줄 알아야 합니다.

PD3는 이 해석 지점의 좋은 예입니다. 0–500 µg/L 설계에서는 sigmoid 우월성이 명확하지 않습니다. 그러나 0–800 µg/L 설계는 모델 판별(model discrimination)을 가능하게 합니다. 이는 모델 선택이 통계기법 문제만이 아니라 실험 설계(experimental design) 문제임을 보여줍니다. [G&W p.734–741]

R&T Ch.8은 또 다른 해석 지점을 줍니다. 혈장 농도가 낮아졌는데 효과가 남아 있을 때 "약물이 없는데 효과가 이상하게 남았다"고 보지 않습니다. 대신 "시스템 전환 또는 비가역적 작용(irreversible action)이 더 느린 과정인가?"를 묻습니다. [R&T p.249–253]

> **Hill $\gamma$의 임상 함의 — Apex 파라미터로서의 위상 — [EXPERT_INFERENCE, v3]**  
> 이 세션의 Apex 개념인 Hill $\gamma$는 단순한 곡선 모양 파라미터가 아니라 임상 의사결정의 정밀도 자체를 결정하는 양입니다.
>
> | 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
> |---|---|---|---|---|
> | $\gamma>1$ | Hill $\gamma$ | → | $EC_{50}$ 근처의 작은 농도 변화가 큰 반응 변화로 전파 | 치료역을 좁게 해석 |
> | 용량 조절 폭 설정 | Hill $\gamma$와 TDM 목표 농도 | → | 과소치료와 독성 사이를 오갈 수 있음 | 목표 농도 폭과 titration step 재검토 |
> | Exposure-response 보고서 | $\gamma$ 추정치와 confidence interval | → | 투여 용량 결정 불확실성 누락 | $\gamma$의 임상적 의의와 불확실성 명시 |
> `[교과서 기반 + 교과서 외 규제 해석]`


## C. 후속 세션 연결 지식 그래프

| 후속 세션 | 이 세션에서 열리는 개념 | 이 세션 없으면 실패하는 것 |
|---|---|---|
| PopPK/PD 공변량 모델링 | $EC_{50}$, $E_{max}$, Hill $n$의 층위 분리 | 공변량 효과를 잘못된 생물학 층위에 배정 |
| Exposure-response 시뮬레이션 | 농도 범위, 고원부, sigmoid 식별 가능성 | 용량 조절 step과 안전 마진 과대평가 |
| Delay/turnover 모델링 | effect compartment vs indirect response | 히스테리시스 원천 오분류와 외삽 실패 |
| 투여 간격 최적화 | AUEC, duration, PK/PD 율속 | 혈장 반감기만으로 지속 시간 판단 |

## D. 경계 플래그 보존

[확인 필요 — 첨부 PDF 미포함 구간]:
- G&W §3.6.2–§3.6.5 (pp.225–228): competitive antagonism 이후 interaction model 연속부. 본 세션에서 추정·보완하지 않음.
- G&W §3.12 baseline modeling: C2 limitation에서 baseline time-varying issue로만 언급. 본 세션에서 상세 모델링 보류.
- `[확인 필요 — 교과서 외 규제 적용]`: PD 율속 약물(PD-rate-limited drug)의 특수 집단 용량 조정(special population dose adjustment)이나 FDA guidance 문구는 본 PDF 범위 밖이므로 일반 원칙으로만 유지.

**최종 요약(Final Recap):** 이 세션의 압축 결론은 세 문장입니다.  
1. $E_{max}$/Hill 모델은 수용체 결합에서 시작하지만 반응 시스템을 포함합니다.  
2. 히스테리시스는 혈장 농도가 효과를 즉시 대표하지 못한다는 시각적 경고입니다.  
3. 지속 시간과 AUEC는 약물 반감기보다 더 느린 생물학적 과정을 찾아야 제대로 해석됩니다.

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

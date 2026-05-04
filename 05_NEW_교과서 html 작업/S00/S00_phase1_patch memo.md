## 판정

**상당히 잘 작업된 Phase 1 v0입니다. 다만 “최적 완성본”은 아니고, HTML로 바로 넘기기 전 Source Fidelity Audit + 과장 표현 패치가 필요합니다.**

점수로 보면 대략 다음 정도입니다.

| 항목                      |       평가 |
| ----------------------- | -------: |
| Curation Map 적절성        |     9/10 |
| 핵심 개념 선별                |     9/10 |
| 두 교과서 역할 분담             |   8.5/10 |
| 실제 수치 anchor 반영         |     8/10 |
| Source fidelity / 과장 방지 | 6.5–7/10 |
| HTML 전환 준비도             |   7.5/10 |

**종합: 조건부 Go.**
Phase 1을 다시 만들 필요는 없지만, **바로 Step 2 HTML로 가지 말고 Phase 2 감사 후 패치**하는 것이 맞습니다.

---

## 잘된 부분

### 1. Curation Map의 MUST 4개 선정은 매우 좋습니다

Scope Lock은 이 세션을 “Pre-Sprint 철학·용어 기반 세션”으로 정의하고, G Ch.1은 모델링 방법론·규율, T Ch.1–2는 임상 PK/PD 언어와 정량 수식 체계를 담당한다고 명시합니다. 특히 Modeling Carousel, Emax/Hill, Turnover, Therapeutic Window는 B-Standard지만 C-Fast-Safe로 넘길 수 없는 핵심이라고 되어 있습니다. 

Draft도 정확히 이 구조를 따라 **M1 Modeling Carousel**, **M2 PK/PD Linkage & Therapeutic Window**, **M3 Emax/C50/Hill γ**, **M4 Turnover** 네 개만 MUST로 잡았습니다. 이는 Scope Lock의 “§2 카드 수 조절” 지시와 잘 맞습니다.  

### 2. “쉬운 챕터처럼 보이지만 사고 순서를 각인하는 세션”이라는 핵심을 잘 잡았습니다

Scope Lock의 보충 메모는 이 세션의 함정이 “쉬워 보인다”는 점이라고 지적합니다. Emax, ADME, PK/PD 용어 자체보다 중요한 것은 **EDA 없이 fitting하는 습관, local minimum 회피, PK와 PD를 분리하지 않는 통합 시각**입니다. 

Draft의 M1 Apex Concept는 이 지점을 강하게 반영했습니다. 특히 “fitting은 시작점이 아니라 6단계 중 5번째”라는 메시지는 Gabrielsson Ch.1의 Modeling Carousel을 학습자에게 각인시키는 데 효과적입니다. 

### 3. 실제 수치 anchor도 대체로 충실합니다

Draft 완료 블록은 warfarin 1.5 mg/kg oral, propranolol γ≈1·C50=5.3 µg/L, alfentanil C50 0.27/0.31/0.42 mg/L, total body water turnover 수치 등을 Data Anchoring으로 정리했습니다. 이는 Scope Lock에서 “가상 수치 대체 금지, 실제 수치 anchor 우선”으로 지정한 항목들과 대체로 일치합니다.  

원문 PDF에서도 PK/PD linkage, therapeutic window, warfarin 지연 반응, propranolol Hill fitting, alfentanil quantal response 등이 실제로 확인됩니다.   

---

## 최적이라고 보기 어려운 부분

### 1. Big Idea와 Plausible Fallacy가 약간 과장되었습니다

가장 큰 문제는 **교육적 임팩트를 위해 일부 문장이 원문 근거보다 강하게 쓰였다는 점**입니다.

예를 들어 M1에서 “데이터를 받자마자 NONMEM에 던지는 신진 모델러는 반드시 local minimum에 수렴한 모델을 들고 와서 잘못된 용량을 추천한다”, “AUC를 30–50% 잘못 예측” 같은 표현은 교육적으로는 강하지만, 업로드된 Gabrielsson Ch.1에서 직접 확인되는 정량 수치는 아닙니다. 원문은 initial estimate가 local minimum 회피에 중요하고 여러 initial estimate로 재실행하라고 권고하는 수준입니다.  

따라서 이 문장은 다음처럼 낮추는 것이 좋습니다.

> EDA 없이 임의 초기값으로 fitting을 시작하면 local minimum에 수렴할 위험이 커지고, 이 경우 CL, V, AUC, t½ 등 후속 해석이 체계적으로 왜곡될 수 있다.

즉, **방향성은 맞지만 “반드시”, “30–50%”, “FDA/EMA reviewer가 이의 제기 못 함” 같은 표현은 삭제 또는 [실무 추론] 표시**가 필요합니다.

### 2. CONTEXT 항목이 일부 1–2문장보다 길어졌습니다

Curation Map에서는 CONTEXT 항목을 “가장 적합한 MUST 카드에 1–2문장으로 흡수”한다고 선언했습니다. 

그런데 M2 안의 ADME, Disposition, First-pass loss, Bioavailability, Enterohepatic cycle 설명은 1–2문장보다 길고, 거의 mini-card처럼 확장되어 있습니다. 내용 자체는 틀리지 않지만, **B-Standard 세션의 미니멀 구조**와는 약간 어긋납니다. 

패치 방향은 간단합니다.

> ADME는 PK phase가 전제하는 해부·생리학적 경로이며, bioavailability와 first-pass loss는 “투여량”이 실제 systemic exposure로 바뀌는 과정의 손실을 설명한다. Enterohepatic cycling은 단순 elimination이 아니라 exposure-time profile을 길게 만드는 distribution component로 이해한다.

이 정도로 압축하면 충분합니다.

### 3. “Regulatory / NDA deficiency” 표현은 근거 등급을 분리해야 합니다

§5 Critical Blow와 §7 boss dilemma 쪽에서 “deficiency letter”, “regulatory submission”, “FDA/EMA reviewer” 표현이 꽤 강하게 들어갑니다. 프롬프트 자체가 Critical Blow에서 규제·임상 파급을 쓰라고 요구하므로 방향은 맞습니다. 다만 현재 문장 일부는 “실제 원문 근거”와 “실무적 확장 해석”이 섞여 있습니다.  

HTML 전환 전에는 다음처럼 태그를 나누는 것이 안전합니다.

* `[원문 근거]`: EDA, initial estimate, local minimum, PK/PD linkage, therapeutic window
* `[실무 추론]`: regulatory documentation, deficiency letter 방어 논리
* `[교육용 가상 시나리오]`: Phase 2b 18시간 회의, 수백억 원 의사결정 등

이렇게 하면 거장의 시각은 살리면서 hallucination 위험을 줄일 수 있습니다.

### 4. Figure policy는 맞지만 Phase 4C에서 주의가 필요합니다

Scope Lock은 원본 figure 직접 임베드를 금지하고, Phase 4C에서 FIGURE_POINTER(P) 모드만 허용한다고 명시합니다. 특히 G Fig.1.2, T Fig.1-3, T Fig.2-11은 ESSENTIAL 후보로 지정되어 있습니다. 

Draft는 현재 Figure를 직접 삽입하지 않았고, Step 1 산출물로는 적절합니다. 다만 Phase 4C에서 SVG를 만들 때 **교재 그림을 1:1 재현하면 안 됩니다.** “같은 구조를 설명하는 독자적 개념도”로 바꿔야 합니다.

---

## 바로 고쳐야 할 패치 목록

### Patch 1 — 과장 수치 제거

삭제 또는 수정 대상:

* “반드시 local minimum”
* “AUC 30–50% 잘못 예측”
* “FDA/EMA reviewer가 이의 제기 못 함”
* “수백억 원 의사결정” 같은 과장형 표현

대체 문장:

> EDA 없이 fitting을 시작하면 initial estimate가 불안정해지고, local minimum 또는 잘못된 model discrimination으로 이어질 수 있다. 이 위험은 용량 예측과 규제 문서화에서 반드시 설명·완화되어야 한다.

### Patch 2 — CONTEXT 압축

M2의 ADME/Disposition/Bioavailability/Enterohepatic cycle 설명, M3의 stereoisomer/prodrug/biomarker 설명은 **각각 1–2문장으로 줄이는 것**이 좋습니다. Curation Map이 선언한 규칙과 맞춰야 합니다. 

### Patch 3 — Source vs Inference 태그 분리

특히 다음 범주는 명시적으로 구분해야 합니다.

| 범주                | 표기              |
| ----------------- | --------------- |
| PDF에 직접 있는 수치·사례  | `[출처: ...]`     |
| 원문에서 논리적으로 도출한 해석 | `[해석]`          |
| 실무 경험 기반 확장       | `[실무 추론]`       |
| 교육용 회의실 시나리오      | `[교육용 가상 시나리오]` |
| 확인 불가             | `[확인 필요]`       |

### Patch 4 — Phase 2를 먼저 진행

Draft 마지막도 스스로 “Unified v3.3.2 워크플로우에 따르면 Step 2 직접 진행이 아니라 Phase 2 Source Fidelity Audit → Phase 3 → Phase 4 → Phase 5”라고 정리하고 있습니다. 이 판단이 맞습니다. 

---

## 최종 결론

**이 Phase 1 결과물은 방향과 구조가 매우 좋습니다.**
특히 Curation Map, MUST 4개 선별, G/T 역할 분담, 실제 수치 anchor 반영은 잘됐습니다.

하지만 **최적본은 아닙니다.** 문제는 내용 누락보다 **원문 근거와 실무적 확장 해석이 섞인 점**, 그리고 일부 Big Idea/Regulatory 표현이 과장된 점입니다.

따라서 다음 진행은:

> **Phase 1 재작성 X → Phase 2 Source Fidelity Audit O → 과장/CONTEXT 압축 패치 → Phase 3/4 → HTML Compile**

이 동선이 가장 효율적입니다.

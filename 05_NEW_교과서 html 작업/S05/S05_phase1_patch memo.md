## 판정

**이번 Session 05 Phase 1 v0는 지금까지의 세션들 중 구조적으로 가장 안정적인 편입니다.**
재작성 대상은 아닙니다. 다만 **최적 완성본은 아니고, 바로 HTML로 넘기면 안 됩니다.**

권장 동선은 동일합니다.

> **원본 v0 보존 → Audit Attention Memo 첨부 → Phase 2 Source Fidelity Audit → Phase 4A에서 공식 패치 → Phase 4C → HTML Compile**

종합 점수는 대략 다음입니다.

| 항목                    |     평가 |
| --------------------- | -----: |
| Scope Lock 반영         | 8.5/10 |
| Curation Map 적절성      |   9/10 |
| MUST/CONTEXT 분리       | 8.5/10 |
| 2구획 핵심 개념 포착          |   9/10 |
| V₁/Vss/Vβ Apex 설정     |   9/10 |
| 수식·수치 source fidelity |   7/10 |
| 실무·규제 확장 통제           | 6.5/10 |
| HTML 직행 준비도           |   7/10 |

---

## 잘된 부분

### 1. MUST 5개 선정은 매우 적절합니다

Scope Lock은 이 세션의 핵심을 **이중지수 방정식**, **macro/micro/physiological parameter 변환**, **재파라미터화 5종**, **V₁/Vss/Vβ 구분**, **분포 속도론의 임상 파급**으로 정의했습니다. Draft도 정확히 M1–M5의 5개 카드로 압축했습니다.  

이전 Session 04처럼 MUST가 과도하게 늘어난 문제가 없고, Curation Map에서 R&T 임상 사례를 CONTEXT 또는 M5로 흡수한 점도 좋습니다. Scope Lock이 경고한 “R&T 사례가 MUST 카드로 과잉 흡수될 위험”을 잘 피했습니다. 

### 2. M3를 Apex로 둔 판단은 맞습니다

Scope Lock은 가장 치명적인 혼동쌍을 **Vss vs Vβ(Vz)**로 지정하고, R&T의 aspirin/gentamicin 비교를 핵심 근거로 삼으라고 했습니다. Draft도 M3를 Apex Concept로 지정하고, §5 Critical Blow를 Vss vs Vβ 혼동쌍으로 배치했습니다. 

이 선택은 매우 타당합니다. 2구획 모델에서 실제 임상 오류는 α/β 수식을 외우지 못해서 생기기보다, **terminal slope로부터 계산된 Vβ를 steady-state amount 계산이나 loading dose 해석에 잘못 쓰는 데서** 발생하기 때문입니다.

### 3. G&W와 R&T의 역할 분담도 잘 유지됐습니다

G&W 쪽은 Fig.2.43의 bi-exponential decomposition, Eq.2:117 이후 macro/micro 변환, PK7/PK8 수치 anchor로 쓰였고, R&T 쪽은 aspirin, thiopental, nicardipine, gentamicin 같은 임상 해석 사례로 사용됐습니다. G&W 원문은 2구획 모델에서 두 번째 지수항이 추가되고, Fig.2.43에서 A≈70, B=28, α와 β 계산을 제시합니다.  R&T도 aspirin 650 mg IV bolus에서 `C = 67e^-0.23t + 33e^-0.050t` 형태의 biexponential 식을 제시하고, early sampling을 놓치면 1구획 해석으로 오인될 수 있음을 설명합니다. 

### 4. PK8 condition number를 핵심 카드로 올린 것은 좋습니다

G&W PK8은 동일한 2구획 데이터를 5가지 parameterization으로 fitting하고, WRSS와 condition number를 비교합니다. 원문 Table 8.1에서 ODE model은 condition number 29.69로 가장 낮고, Takada model은 WRSS는 가장 낮지만 condition number가 3186으로 큽니다.  Draft가 이를 “parameterization 선택이 단순 취향이 아니라 수치 안정성의 문제”로 끌어올린 것은 좋은 해석입니다.

---

## 최적이라고 보기 어려운 부분

### 1. Condition number 최대값이 불일치합니다

Curation Map의 M4에는 condition number가 **29.69–4,104** 범위라고 되어 있습니다. 그런데 draft 본문 표와 G&W PK8 원문 Table 8.1에서는 최대값이 **Takada 3186**으로 보입니다. Draft 본문 표도 Macro 125.2, Takada 3186, Colburn 2243, Reparameterized 2306, ODE 29.69로 정리했습니다.   

**필수 패치:**
`29.69 ~ 4,104` → `29.69 ~ 3,186`으로 수정하거나, 4,104가 다른 표/반올림/다른 모델에서 온 값이면 `[확인 필요]`로 표시해야 합니다.

### 2. Aspirin 예시의 “30% 과소평가” 방향이 위험합니다

Draft M1은 aspirin에서 1구획 모델 CL=985 mL/min, 2구획 모델 CL=683 mL/min을 비교하면서 “clearance가 30% 빗나간다”는 메시지를 사용합니다. 이 자체는 교육적으로 좋지만, 이어지는 “모든 후속 용량 계산이 30% 과소평가된다”는 표현은 방향이 틀릴 가능성이 있습니다. R&T 원문은 terminal slope만으로 1구획 해석을 하면 V=20 L, CL=0.98 L/min으로 계산된다고 설명하고, biexponential 식에서는 aspirin의 초기 phase를 별도로 고려합니다. 

CL을 683이 아니라 985 mL/min으로 잡으면 maintenance dose는 보통 **과소평가가 아니라 과대평가** 쪽으로 갑니다.
따라서 다음처럼 바꾸는 것이 안전합니다.

> 초기 sampling을 놓치고 terminal phase만으로 1구획 해석을 하면 CL과 V 추정이 체계적으로 왜곡된다. Aspirin 예시에서는 1구획식 CL이 2구획 해석보다 크게 산출되므로, 유지용량 또는 exposure 예측이 잘못될 수 있다.

### 3. “NDA Deficiency Letter” 표현은 실무 추론으로 분리해야 합니다

Scope Lock 자체가 A-Critical 근거로 “재파라미터화 선택 오류 → COV step 조건수 폭등 → NDA Deficiency Letter”를 언급하고 있어 draft가 이를 반영한 것은 이해됩니다.  다만 교재 원문은 PK8에서 condition number와 parameter precision 문제를 다루지, 실제 NDA deficiency letter를 말하는 것은 아닙니다. 

**권장 처리:**
`NDA Deficiency Letter의 실제 발화점` → `[실무 추론] 규제 제출에서 covariance failure, high RSE, parameter identifiability 설명 요구로 이어질 수 있음` 정도로 낮추세요.

### 4. 선형대수/eigenvalue 설명은 유용하지만 “교재 원문”은 아닙니다

M1의 “α, β는 system matrix의 eigenvalue” 설명은 수학적으로 맞고 매우 좋습니다. 하지만 G&W/R&T 원문은 macro-constant, micro-constant 변환과 biexponential 해를 제시하지, 행렬 고윳값 해석을 직접 가르치는 구조는 아닙니다. G&W는 Eq.2:117 이후 A, α, B, β와 k10/k12/k21 변환식을 제시합니다. 

이 부분은 삭제할 필요는 없습니다. 다만 **Source tag를 분리**해야 합니다.

> `[수학적 해석] 2×2 linear ODE의 eigenvalue 해석으로 보면 α, β는 system matrix의 고유 시간척도다.`

이렇게 하면 정확성과 교육적 깊이를 모두 살릴 수 있습니다.

### 5. NONMEM ADVAN3/4/11/12 연결은 후속 지식으로 유지해야 합니다

Draft는 NONMEM ADVAN3/4/11/12 선택 근거, η-shrinkage, OMEGA 양정치성까지 연결합니다. Scope Lock도 후속 개념으로 이를 열어두었습니다.  하지만 이 세션의 source PDF 자체는 G&W/R&T 교재이지 NONMEM manual이 아닙니다.

따라서 §1 지식 그래프나 §8 professional moat에서는 유지해도 좋지만, §2 본문에서 “교재 근거”처럼 쓰면 안 됩니다. `후속 PopPK 구현 연결` 또는 `[실무 확장]` 태그를 붙이는 편이 안전합니다.

### 6. “항상 빗나간다” 같은 표현은 약간 낮추는 것이 좋습니다

M5에는 “임상의가 1구획 직관으로 dosing interval을 정하면 항상 빗나간다”는 표현이 있습니다. Draft의 핵심 메시지는 맞지만, 문장은 과합니다. R&T는 terminal half-life가 모든 경우에 단순 적용되지 않는다는 점, 그리고 분포 kinetics가 multiple dosing과 infusion 해석을 바꾼다는 점을 설명합니다. 특히 plasma fluctuation이 작거나 input이 느리면 Vss 적용이 가능하다고도 말합니다. 

**권장 수정:**
`항상 빗나간다` → `terminal phase의 fractional contribution과 dosing context를 확인하지 않으면 빗나갈 수 있다`.

---

## 바로 Phase 2에 넘기기 전 붙일 Audit Attention Memo

```markdown
# Audit Attention Memo — Session 05 Step 1 Draft v0

## 1. Condition number 범위 점검
Curation Map M4에는 “29.69 ~ 4,104”로 되어 있으나,
draft 본문과 G&W PK8 Table 8.1은 29.69 ~ 3,186으로 보임.
Phase 2에서 Table 8.1 원문과 1:1 대조 후 수정.

## 2. Aspirin 1구획 vs 2구획 CL 해석 방향 점검
M1 Big Idea에서 “용량 계산이 30% 과소평가”라고 되어 있으나,
1구획 terminal-only 해석에서는 CL이 0.98 L/min, 2구획 해석은 0.683 L/min으로 더 작음.
따라서 과소/과대 방향을 재검토하고 “CL/V 추정 왜곡”으로 표현 완화.

## 3. Regulatory 표현 태그 분리
“NDA Deficiency Letter”, “심사관 발화점” 등은 PDF 직접 근거가 아니라 실무 추론.
[실무 추론] 태그를 붙이거나 “규제 문서에서 identifiability 설명 요구 가능”으로 완화.

## 4. Eigenvalue 해석 source tag 분리
M1의 2×2 ODE eigenvalue 설명은 수학적으로 유용하나 교재 직접 서술은 아님.
[수학적 해석] 또는 [해석]으로 태그 분리.

## 5. NONMEM ADVAN/OMEGA/shrinkage 연결은 후속 지식으로 유지
§1/§8에서는 유지 가능.
§2 본문에서는 교재 직접 근거처럼 쓰지 말고 [실무 확장] 처리.

## 6. Terminal half-life 문장 강도 조정
“항상 빗나간다”는 표현은 과강함.
“fractional area와 dosing context를 확인하지 않으면 빗나갈 수 있다”로 조정.

## 7. CONTEXT 1–2문장 준수 확인
Takada/Colburn, infusion/extravascular/urine data, eptifibatide 등은 CONTEXT로 유지.
M4/M5에서 mini-card처럼 확장되지 않았는지 Phase 4A에서 압축 점검.
```

---

## 최종 결론

**이번 v0는 좋은 Phase 1 초안입니다.**
특히 **MUST 5개 압축, M3 Apex 설정, G&W/R&T 역할 분담, PK8 condition number를 M4로 끌어올린 판단**은 매우 좋습니다.

하지만 **수치 하나(condition number 4,104), aspirin CL 해석 방향, regulatory 표현 강도, 교재 직접 근거와 수학/실무 확장의 태그 분리**는 반드시 정리해야 합니다.

따라서 최적 판단은:

> **재작성 X / HTML 직행 X / Phase 2 Audit 진행 O**

입니다.
이번 세션은 구조가 좋기 때문에 Phase 4A에서 대폭 뜯어고칠 필요는 크지 않고, **Source Fidelity 중심의 정밀 패치**만 거치면 좋은 Content Lock으로 갈 가능성이 높습니다.

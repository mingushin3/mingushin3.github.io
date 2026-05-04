## 판정

**Session 15 Phase 1은 “상당히 잘 나온 Draft v0”입니다. 다만 최적 완료본은 아닙니다.**
현재 상태는 **Phase 2 Source Fidelity Audit으로 넘기기에 충분히 좋지만, HTML 직행은 금지**가 맞습니다.

| 항목                  |         평가 |
| ------------------- | ---------: |
| Scope Lock 준수       | **8.5/10** |
| Curation Map 적절성    | **8.0/10** |
| 초기값·GOF·F-test 축 구성 | **8.5/10** |
| 실제 수치 anchor 반영     | **8.0/10** |
| 수식·표기 안정성           | **7.0/10** |
| 출처 없는 규제/실무 해석 통제   | **5.5/10** |
| HTML 전환 준비도         | **아직 불충분** |

**최종 판정:**
`Phase 1 재실행 불필요 / Phase 2 필수 / HTML 직행 금지`

현재 워크플로우도 Phase 1 이후 바로 HTML이 아니라 **Phase 2 Source Fidelity Audit → Phase 3 Insight Crucible → Phase 4 Content Lock → Phase 4C Visual Pedagogy → Phase 5 HTML Compile** 순서로 설계되어 있습니다. 

---

## 잘 된 부분

### 1. Curation Map의 6개 MUST 구성은 대체로 타당합니다.

Draft는 **초기값 획득 → 잔차 기반 GOF → F 검정 → 파라미터 정밀도/상관 → 편미분 기반 최적 샘플링 → 민감도 분석**으로 modeling carousel 한 사이클을 구성했습니다. 이 흐름은 Scope Lock이 요구한 “초기값, GOF, 모델 판별, 실험 설계” 축과 잘 맞습니다.

특히 **F 검정 적용 조건을 Apex Concept로 둔 판단은 적절**합니다. 원문도 F-test는 hierarchical/nested model에서만 F distribution을 사용할 수 있고, non-nested model에서는 F ratio가 F distribution을 따르지 않는다고 설명합니다. 

### 2. 초기값 획득 파트는 강합니다.

Fig.4.17의 IV bolus 10 mg 예시에서 `K = 0.01 min⁻¹`, `t½ ≈ 65 min`, `AUC = 100,000 µg·L⁻¹·min`, `Cl = 0.1 L·min⁻¹`, `V = 10 L`로 이어지는 도출은 잘 반영되어 있습니다. Fig.4.18의 bi-exponential 예시 `A=1`, `B=0.8`, `α=0.05`, `β=0.003 min⁻¹`도 적절하게 들어갔습니다.

또 Gabrielsson이 p.353에서 강조하는 “초기값이 나쁘면 wrong final value나 physiologically impossible local minimum으로 수렴할 수 있다”는 메시지를 Big Idea로 끌어올린 것도 좋습니다. 

### 3. r 값 오용과 AIC/F-test 한계는 잘 잡았습니다.

원문은 Fig.4.53에서 `r=0.96`인 OLS fit이 terminal observations를 systematic하게 underestimate하고, 오히려 `r=0.94`인 IRLS fit이 전체적으로 더 낫다고 설명합니다. Draft가 이를 혼동쌍으로 둔 것은 교육 효과가 큽니다.

AIC/SC도 잘 배치되었습니다. 원문은 AIC/SC가 nested model을 요구하지는 않지만, **same weighting scheme**이 필요하며, AIC/SC만으로 GOF를 판단하지 말라고 경고합니다. 

---

## 반드시 고쳐야 할 부분

### 1. “Deficiency Letter / 6-month review extension”은 교과서 기반 사실이 아닙니다.

Draft에는 “NDA/IND 심사관의 Deficiency Letter”, “Major Deficiency”, “6-month review extension” 같은 문장이 반복됩니다.

하지만 첨부 PDF가 직접 지지하는 것은 다음 정도입니다.

```text
F-test는 nested model + equal weighting 조건에서만 유효하다.
AIC/SC도 같은 weighting 조건에서 비교해야 한다.
상관계수 r만으로 GOF를 판단하면 안 된다.
```

원문은 regulatory deficiency letter나 review extension 기간을 직접 말하지 않습니다. 따라서 Phase 4에서 다음처럼 낮춰야 합니다.

```text
[교과서 기반]
F-test는 nested model + equal weighting 조건에서만 유효하며, MM elimination과 first-order elimination처럼 non-nested이거나 weighting이 다른 모델 비교에는 사용할 수 없다.

[교과서 외 실무 해석]
규제 제출 문서에서는 이러한 비교 조건 위반이 모델 선택 근거의 신뢰성을 약화시키므로, AIC/SC, residual diagnostics, sensitivity analysis, simulation-based comparison 등을 함께 제시해야 한다.
```

---

### 2. 상관계수 r 수식이 잘못 전사된 것으로 보입니다.

Draft의 혼동쌍 #2에는 다음 형태가 들어갑니다.

```text
r = 1 - [ ... ]
```

이 표현은 일반적인 Pearson correlation coefficient 형태와 맞지 않습니다. 또한 분모에 square root 구조가 보이지 않아 수식 전사 오류 가능성이 큽니다. 

원문은 Eq.4:53에서 correlation coefficient를 제시하고, 이어서 “높은 r 값이 좋은 fit을 보장하지 않는다”는 메시지를 Fig.4.53으로 설명합니다.

Phase 2에서 PDF 원식을 육안 확인하고, 일반적으로는 아래 형태에 맞춰야 합니다.

```text
r =
\frac{\sum_i (X_i-\bar X)(C_i-\bar C)}
{\sqrt{\sum_i (X_i-\bar X)^2 \sum_i (C_i-\bar C)^2}}
```

현재 Draft의 `1 -` 형태는 **MUST_FIX**입니다.

---

### 3. Warfarin-PCA slope 식의 부호가 값과 맞지 않습니다.

Draft의 B-3에서는 다음처럼 되어 있습니다.

```text
slope = [ln(124) - ln(56.77)] / (24 - 0) ≈ -0.03 h^-1
```

하지만 이 식 그대로 계산하면 양수입니다. 감소 slope를 표현하려면 다음 중 하나여야 합니다.

```text
slope = [ln(56.77) - ln(124)] / (24 - 0) ≈ -0.03 h^-1
```

또는

```text
slope = [ln(124) - ln(56.77)] / (0 - 24) ≈ -0.03 h^-1
```

원문은 prothrombin complex activity의 downswing에서 `kout`를 추정하며, slope가 `-kout`가 된다는 구조를 제시합니다.

이건 작은 typo처럼 보이지만, **초기값 추정 세션에서는 부호 하나가 핵심**이라 반드시 고쳐야 합니다.

---

### 4. NONMEM/CWRES/NPDE/SCM/Bayesian/Fisher information 확장은 라벨링이 필요합니다.

Draft에는 `CWRES`, `NPDE`, `Pirana/Xpose`, `SCM`, `Bayesian TDM`, `Fisher information matrix`, `D-optimal`, `mrgsolve`, `Sobol index` 등 실무 확장 개념이 많이 들어갑니다. 교육적으로는 유용하지만, 이번 Scope의 직접 소스는 Gabrielsson Ch.4–5이고, NONMEM/Owen/PIPET 문헌은 Scope 안에 없습니다.

따라서 Phase 4에서 다음 라벨을 붙여야 합니다.

```text
[교과서 외 구현 번역]
NONMEM CWRES/NPDE, Pirana/Xpose, SCM, Bayesian TDM, Fisher information, D-optimal design은 본 세션의 개념을 현대 PopPK workflow로 번역한 예시이다. 원문 직접 내용은 아니다.
```

삭제할 필요는 없지만, **source-supported 본문과 implementation bridge를 분리**해야 합니다.

---

### 5. “모든 모델링 실패의 80%” 같은 수치는 삭제해야 합니다.

Draft에는 “도구를 잘못된 맥락에서 적용한 결과가 모든 모델링 실패의 80%를 차지한다”는 식의 표현이 있습니다. 

강한 문장이라 교육 효과는 있지만, PDF source-supported 수치가 아닙니다. 다음 정도로 낮추는 것이 안전합니다.

```text
모델링 실패의 상당수는 도구 자체를 몰라서가 아니라, 도구의 적용 조건을 잘못 이해해서 발생한다.
```

---

### 6. pp.365–367 누락 구간 처리 원칙은 잘 지켰지만, 계속 감시해야 합니다.

Scope Lock은 §4.5 Minimization과 §4.6 Weighting, 즉 pp.365–367이 업로드 PDF에 없으므로 임의 보완하지 말라고 지시합니다. Draft는 이 구간을 `[확인 필요 — pp.365-367 업로드 부재]`로 표시하고 있어 이 점은 잘했습니다.

다만 F-test와 residual diagnostics에서 weighting 설명이 계속 등장하므로, Phase 2에서는 **weighting 관련 문장이 §4.7–4.8 가시 범위에서 확인되는 내용인지, 아니면 누락된 §4.6을 일반 지식으로 보완한 것인지**를 분류해야 합니다. 원문 §4.8은 F-test와 AIC/SC 비교에서 equal weighting 필요성을 직접 말하므로 그 부분은 source-supported입니다.

---

## 종합 판정

```text
GO: Phase 2 Source Fidelity Audit
NO-GO: HTML Compile
REDO: 불필요
MUST_FIX: 있음
```

이번 Phase 1은 **구조·큐레이션·수치 anchor가 좋은 고품질 초안**입니다. 다만 다음 6개는 Phase 2–4에서 반드시 잡아야 합니다.

```text
MUST_FIX

1. Deficiency Letter / 6-month extension / NDA 심사 문구를 [교과서 외 실무 해석]으로 라벨링 또는 삭제.
2. Eq.4:53 상관계수 r 수식 전사 오류 수정.
3. Warfarin-PCA slope 식의 부호/분자-분모 방향 수정.
4. NONMEM/CWRES/NPDE/SCM/Bayesian/Fisher information/Sobol 등은 [교과서 외 구현 번역]으로 분리.
5. “모델링 실패의 80%” 등 출처 없는 수치 삭제.
6. weighting 관련 설명이 pp.365–367 부재 구간을 임의 보완한 것인지 전수 분류.
```

## Phase 2에 추가할 감사 지시

```text
추가 감사 지시:

1. Eq.4:53 correlation coefficient 수식을 PDF 원문과 전수 대조하라. Draft의 “r = 1 − …” 형태가 맞는지 확인하고, 오류이면 정확한 Pearson correlation 형태로 수정하라.

2. Warfarin-PCA Eq.4:22 slope 계산에서 numerator/denominator 방향과 부호가 일관적인지 확인하라. 최종 slope는 −kout ≈ −0.03 h⁻¹가 되어야 한다.

3. Deficiency Letter, Major Deficiency, 6-month review extension, NDA Module 5 문장이 PDF source-supported인지 분류하라. 직접 근거가 없으면 [교과서 외 실무 해석]으로 라벨링하라.

4. NONMEM, CWRES, NPDE, SCM, Bayesian TDM, Fisher information, D-optimal, Sobol, mrgsolve 관련 표현이 원문 직접 내용인지 구현 번역인지 분류하라.

5. §4.5–4.6 pp.365–367 부재 구간에서 온 내용이 Draft에 섞였는지 확인하라. 섞였으면 [확인 필요 — pp.365–367 업로드 부재]로 플래그하라.

6. Table 4.5–4.7의 pure error / lack-of-fit 수치, Fig.4.53의 r=0.96 vs 0.94, Table 4.8의 F-test/AIC 제한 조건, §5.2.3의 최적 sampling time 1.4 h/14 h, §5.2.4 sensitivity 수치를 전수 대조하라.
```

**한 줄 결론:**
이번 Phase 1은 **modeling carousel의 핵심 실행 기술을 잘 잡은 성공적인 Draft v0**입니다. 하지만 **r 수식 전사, slope 부호, 규제 문장 과잉, 구현 확장 라벨링**을 잡기 전에는 최종 Step 1로 잠그면 안 됩니다.

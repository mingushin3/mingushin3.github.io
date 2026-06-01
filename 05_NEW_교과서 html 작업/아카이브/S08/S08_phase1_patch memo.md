## 판정

**이번 Session 08 Phase 1 v0는 “자료 포착력은 매우 높지만, 최적의 Step 1 완성본은 아닙니다.”**
재작성할 정도의 실패는 아니지만, **이대로 HTML로 넘기면 과밀한 백과사전형 HTML이 될 가능성이 큽니다.**

최종 판단은:

> **조건부 Go — 재작성 X / HTML 직행 X / Phase 2 Source Fidelity Audit 필수 / Phase 4A에서 강한 compression 필요**

입니다.

---

## 종합 점수

| 항목                    |       평가 |
| --------------------- | -------: |
| Source coverage       |     9/10 |
| Scope Lock 반영         | 7.5–8/10 |
| Curation Map 작성       |     7/10 |
| 핵심 mechanism 포착       |     9/10 |
| Ch.16/17 임상 anchor 반영 |   8.5/10 |
| DDI 정량 framework 포착   |   8.5/10 |
| MUST/CONTEXT 압축       | 5.5–6/10 |
| 원문 근거 vs 실무 확장 분리     | 5.5–6/10 |
| HTML 직행 준비도           |     5/10 |

---

## 잘된 부분

### 1. 핵심 source coverage는 매우 높습니다

Draft는 Gabrielsson Ch.2.7/Ch.3.6/PK17·18·22를 Stage 1 mechanism canonical로 두고, Rowland & Tozer Ch.16을 임상 정량 layer, Ch.17을 DDI prediction framework로 확장했습니다. 이 3-stage 구조 자체는 이번 세션의 방대한 범위를 처리하기 위한 합리적인 선택입니다. 

Scope Lock도 capacity-limited kinetics, time-dependent kinetics, nonlinear binding, nonlinear drug–metabolite model, ethanol 통합 사례, DDI interaction PD models를 모두 in-scope로 지정하고 있습니다. 특히 Eq.17-9~17-14와 Eq.16-7~16-10은 수식 복원 우선순위로 명시되어 있습니다.  

### 2. Big Idea의 방향은 좋습니다

Draft의 중심축은 “비선형 PK는 capacity·time·flow·binding이 서로 다른 표면형으로 드러나는 하나의 nonlinear system 문제”라는 구조입니다. Gabrielsson 원문도 비선형성을 capacity, time, flow, binding 관점에서 설명하고, dose-normalized AUC vs dose 및 superposition 위반을 진단 출발점으로 제시합니다. 

R&T Ch.16도 phenytoin에서 67% 용량 증가가 9배 혈중농도 상승으로 이어지는 예와, ascorbic acid에서 133배 용량 증가가 약 2배 농도 증가에 그치는 예를 통해 nonlinear kinetics의 임상적 의미를 매우 강하게 제시합니다. 

### 3. Ch.17 DDI layer를 붙인 판단도 방향은 맞습니다

R&T Ch.17은 drug interaction을 PK 또는 PD가 다른 약물에 의해 바뀌는 현상으로 정의하고, interaction은 all-or-none이 아니라 농도·용량·환자 요인에 따라 graded하다고 설명합니다. Draft가 이를 T5–T10으로 확장해 displacement, competitive inhibition, MBI, induction, transporter-mediated DDI, PD interaction까지 연결한 것은 큰 그림상 타당합니다. 

---

## 최적이라고 보기 어려운 부분

### 1. MUST 카드가 너무 많습니다

이번 draft의 가장 큰 문제는 **coverage가 부족한 것이 아니라 너무 많다는 점**입니다.

Phase 1 protocol은 핵심 개념을 3–6개 수준으로 추출하도록 설계되어 있고, Scope Lock도 Ch.16에서는 Michaelis-Menten 정상상태 수식과 포화 대사의 임상 결과, Ch.17에서는 CLinhib/CLnormal 예측 수식과 extraction ratio 조건 분기를 최상위 MUST로 보라고 지시합니다.  

그런데 draft는 Stage 1 M1–M9, Stage 2 M2-EXT/M3-EXT/M5-EXT/T1–T4, Stage 3 T4-EXT/T5–T10까지 사실상 20개 이상을 핵심 단위로 유지합니다. 

이 구조는 **Phase 2 감사용 coverage draft**로는 좋지만, **학습자가 읽을 최종 Step 1**로는 과밀합니다.

권장 압축 구조는 다음 정도입니다.

| 최종 MUST 후보                              | 흡수할 항목                                    |
| --------------------------------------- | ----------------------------------------- |
| C1. 비선형성 진단과 superposition 위반           | M1, dose-normalized AUC, Fig.2.85–2.86    |
| C2. Capacity-limited MM kinetics        | M2, M2-EXT, phenytoin, alcohol, PK17/18   |
| C3. Time-dependent turnover kinetics    | M3, M4, M3-EXT, auto/heteroinduction, MBI |
| C4. Binding/TMDD/nonlinear distribution | M5, M5-EXT, T3, displacement-only DDI     |
| C5. DDI 정량 예측 framework                 | T4-EXT, T6, T7, T8, T9                    |
| C6. PD interaction layer                | M8, M9, T10                               |

즉, **20개를 6개 master card로 묶고, 나머지는 CONTEXT / Case Anchor / Trench Tip으로 내려야 합니다.**

---

### 2. Stage 1을 “별도 산출물 참조”로 둔 것은 위험합니다

Draft는 Stage 1 Mechanism Cards M1–M9에 대해 “정본은 별도 Stage 1 산출물 참조, 본 통합본은 구조 anchor만 표시”라고 되어 있습니다. 

이건 Phase 1 workflow 관점에서 위험합니다. 최종 HTML은 **single self-contained HTML**이어야 하므로, 핵심 mechanism을 별도 파일에 의존하면 Phase 2/4/HTML 단계에서 누락이나 중복이 생깁니다. 특히 M2 capacity-limited MM은 이번 세션의 가장 핵심적인 개념인데, 이를 “anchor 요약”으로만 두면 후속 T6/T7 DDI framework가 공중에 뜰 수 있습니다.

권장 처리:

> Stage 1 M1–M9 전체를 모두 full card로 되살릴 필요는 없지만, **C1–C3 master card 안에 필수 수식과 임상 anchor는 반드시 통합**해야 합니다.

---

### 3. Scope creep가 일부 있습니다

Draft 안에는 `FDA DDI Guidance`, `NDA Section 12.3`, `CPIC guideline`, `Mager-Jusko 2001`, `NONMEM quasi-equilibrium TMDD code` 같은 표현이 보입니다.  

이 중 일부는 실무적으로 유용하지만, 첨부 source 자체는 Gabrielsson/R&T 교재입니다. Scope Lock도 OUT OF SCOPE로 PopPK IIV/RUV 구조, 별도 강의 영역 등을 명시합니다. 

따라서 다음은 Phase 4A에서 태그 분리해야 합니다.

| 표현                    | 권장 처리               |
| --------------------- | ------------------- |
| FDA DDI Guidance 핵심식  | `[후속 규제 연결]`        |
| NDA Section 12.3      | `[실무 추론]`           |
| CPIC guideline        | 삭제 또는 §8 후속 지식      |
| Mager-Jusko TMDD code | §8 후속 세션으로 이동       |
| NONMEM code blocks    | `[실무 확장]` 또는 삭제/부록화 |

특히 **TMDD code block은 현재 source 범위를 넘어서는 구현 예시**입니다. Small-molecule TMDD prototype 설명은 가능하지만, full quasi-equilibrium TMDD 구현 코드는 이번 Step 1 본문에 넣지 않는 편이 안전합니다.

---

### 4. “Regulatory language”가 원문 근거처럼 보입니다

Draft는 “NDA reviewer는 mechanism이 정확하면 dose가 안전하다는 단일 명제로 평가한다”, “contraindication”, “dose 25–50% 감량” 같은 문장을 강하게 사용합니다.  

이런 문장은 교육적 임팩트는 있지만, 교재 직접 근거라기보다 **실무적 확장 해석**입니다. R&T Ch.17이 interaction의 graded nature, polypharmacy, severe interaction, market withdrawal 사례를 말하는 것은 맞지만, 특정 NDA reviewer language까지 직접 제공하는 것은 아닙니다. 

권장 문장 강도:

> `[실무 추론]` mechanism과 exposure-ratio 예측을 명확히 제시하지 못하면, 규제 문서에서 DDI risk management와 dose adjustment 근거 설명을 요구받을 수 있다.

---

### 5. Displacement-only DDI는 CONTEXT로 내려야 합니다

Scope Lock은 Ch.17에서 displacement 단독 상호작용은 CONTEXT 처리가 적절하다고 지시합니다.  그런데 draft는 T5로 독립 카드화하고 있습니다. 

Displacement는 중요한 혼동쌍이지만, 이 세션의 중심은 **CLinhib/CLnormal, AUC ratio, MBI/induction time course, extraction route effect**입니다. Displacement-only는 C4 또는 C5 안의 confusion pair로 충분합니다.

---

### 6. Figure/visual load가 Phase 4C에서 폭발할 가능성이 큽니다

이번 세션은 figure 후보가 많습니다. Gabrielsson Fig.2.85–2.90, R&T Ch.16 Fig.16-1, 16-18~23, R&T Ch.17 Fig.17 계열까지 모두 학습 가치가 있습니다. 그러나 workflow는 A-Critical에서도 pointer 최대 5, schematic 최대 2 정도로 제한합니다. 

따라서 Phase 4C에서 강한 triage가 필요합니다. Figure를 많이 넣는 방식이 아니라, 다음처럼 줄이는 편이 좋습니다.

* **Pointer**: Fig.2.85–2.86, Fig.16-1, Fig.17-6 또는 17-13, Fig.17-15, Fig.17-21
* **New schematic**: “capacity/time/binding/DDI one mechanism map” 1개
* **New schematic**: “reversible inhibition vs MBI vs induction time course” 1개

---

## 권장 Audit Attention Memo

Phase 2에 아래 메모를 같이 붙이세요.

```markdown
# Audit Attention Memo — Session 08 Step 1 Draft v0

## 1. MUST 과밀 문제
Draft는 Stage 1 M1–M9, Stage 2 EXT/T1–T4, Stage 3 T4-EXT/T5–T10까지 20개 이상을 핵심 단위로 유지함.
Phase 4A에서 5–6개 master card로 강한 compression 필요.
Displacement-only DDI, combination products, transporter examples는 CONTEXT 또는 case anchor로 하향.

## 2. Stage 1 별도 산출물 의존성
Draft는 Stage 1 mechanism 정본을 별도 산출물 참조로 두고 있음.
최종 HTML은 self-contained여야 하므로, M2 MM, M3 turnover, M5 binding의 필수 수식과 anchor는 본 통합본 안에 반드시 통합 필요.

## 3. Source fidelity 태그 분리
FDA DDI Guidance, NDA Section 12.3, CPIC guideline, Mager-Jusko 2001, NONMEM TMDD code는 PDF 직접 근거가 아님.
[실무 추론] / [후속 규제 연결] / [후속 세션]으로 분리하거나 삭제.

## 4. Eq.17-9~17-14 / Eq.17-18 수식 복원 검증
Scope Lock에서 Ch.17 DDI 수식은 수식 복원 우선순위로 지정됨.
Phase 2에서 원문과 1:1 대조하고, 복원식에는 [복원] 태그 유지.

## 5. Eq.16-7~16-10 검증
Phenytoin 정상상태 수식, t90 발산, Vm/R0 관계는 Ch.16 핵심.
Draft의 M2-EXT 수식과 원문 Eq.16-7~16-10을 대조.

## 6. PK17/PK18/PK22 data anchor 검증
PK17 linear vs MM WRSS/AIC, PK18 ethanol Vmax/Km, PK22 autoinduction parameter는 Gabrielsson source fidelity 핵심.
실제 수치, 단위, table 번호, case study 번호를 Phase 2에서 확인.

## 7. Displacement-only DDI 위치 조정
Scope Lock은 displacement 단독 상호작용을 CONTEXT 처리하는 것이 적절하다고 지시.
T5 독립 full card 유지 여부를 Phase 4A에서 재판정.

## 8. Regulatory wording 완화
“NDA reviewer”, “contraindication”, “dose 25–50% 감량” 등은 PDF 직접 근거가 아니라 실무 판단.
문장 강도를 낮추고 태그 분리.

## 9. Figure budget 폭발 방지
Phase 4C에서 pointer 최대 5, schematic 최대 2 기준 적용.
Fig.2.85–2.86, Fig.16-1, Fig.17-6/13/15/21 중 ESSENTIAL만 남길 것.
```

---

## 최종 결론

**이번 Phase 1은 버릴 초안이 아니라, 매우 풍부한 coverage draft입니다.**
하지만 최적 Step 1이라고 보기는 어렵습니다.

핵심 문제는:

1. **MUST가 너무 많아 학습 흐름이 과밀**
2. **Stage 1 mechanism을 별도 산출물에 의존**
3. **PDF 직접 근거와 실무/규제 확장이 섞임**
4. **DDI 예시가 지나치게 많이 독립 카드화**
5. **Figure 후보가 Phase 4C에서 폭발할 가능성**

입니다.

따라서 다음 동선이 가장 좋습니다.

> **재작성 X → 원본 v0 보존 → 위 Audit Attention Memo 첨부 → Phase 2 Source Fidelity Audit → Phase 3 Insight Crucible → Phase 4A에서 5–6개 master card로 강한 압축 → Phase 4C → HTML Compile**

**바로 HTML로 넘기면 안 됩니다.**
이번 세션의 품질은 Phase 1 생성보다 **Phase 4A compression에서 결정**됩니다.

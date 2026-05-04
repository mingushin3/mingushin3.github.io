## 결론

**이번 Phase 1 결과물은 상당히 잘 나왔습니다.**
다만 **“최적으로 완료된 Step 1 확정본”은 아니고, “Phase 2 감사로 넘기기에 충분히 좋은 Draft v0”**입니다.

판정은 다음입니다.

| 항목                   |         판정 |
| -------------------- | ---------: |
| Scope Lock 준수        | **8.5/10** |
| 핵심 개념 큐레이션           | **8.5/10** |
| Gabrielsson + R&T 통합 | **8.0/10** |
| 수식·수치 안정성            | **7.0/10** |
| 환각/과잉 실무해석 위험        |  **주의 필요** |
| HTML 직행 가능성          |     **불가** |
| Phase 2 진행 가능성       |     **가능** |

**최종 판정: Phase 1 재실행은 불필요. 단, Phase 2 Source Fidelity Audit은 반드시 거쳐야 합니다. HTML로 바로 넘어가면 안 됩니다.**

---

## 잘 된 부분

### 1. MUST 카드 5개 선정은 거의 적절합니다.

Scope Lock은 이 세션을 **Turnover**, **Protein/Antibody PK**, **TMDD**, **MM 근사 경계**를 통합 체화하는 A-Critical 세션으로 정의했고, MUST 카드는 5개 이내로 제한하며 Apex Concept는 Full TMDD에 두라고 지시했습니다. 실제 Draft도 M1 Turnover, M2 Antibody PK, M3 TMDD 4-phase, M4 Full TMDD, M5 MM approximation boundary로 정리되어 있어 큰 방향은 정확합니다.  

특히 **§2.6.6 Body Temperature / §2.6.7 Feedback을 독립 MUST 카드로 만들지 않고 CONTEXT로 흡수한 점**은 좋습니다. Scope Lock이 우려했던 “74쪽 범위 전체를 다 MUST로 끌어올리는 과잉 큐레이션”을 피했습니다. 

---

### 2. Turnover → TMDD로 이어지는 구조적 spine은 잘 잡았습니다.

Gabrielsson 원문은 turnover를 `kin`과 `kout·A`의 균형으로 설명하고, turnover time이 `A0/kin`, `1/kout`, `Vss/CL`, MRT와 연결된다고 제시합니다. Draft의 M1은 이 구조를 그대로 잡고, 이를 TMDD의 target compartment로 연결했습니다. 

또 `kin`을 바꾸면 steady-state level만 바뀌고 도달 시간은 유지되지만, `kout`을 바꾸면 level과 time-to-steady-state가 함께 바뀐다는 Fig.2.70의 메시지를 M1의 핵심 직관으로 둔 것도 적절합니다. 

---

### 3. TMDD 4-phase와 MM 근사 경계는 소스 메시지를 잘 반영했습니다.

Gabrielsson PK27과 R&T Ch.21은 TMDD에서 저농도와 고농도에서는 linear, 중간 농도에서는 nonlinear behavior가 나타나며, target/complex 데이터가 없으면 parameter 식별이 어렵다고 설명합니다. Draft는 이를 M3–M5의 중심축으로 잘 반영했습니다.  

MM 근사의 한계도 핵심을 잘 잡았습니다. 원문은 MM 모델이 제한된 dose range에서는 작동할 수 있지만, drug concentration이 target concentration을 충분히 초과하거나 target occupancy가 거의 100%인 조건에서 더 타당하다고 설명합니다. Draft도 이 경계를 M5에 배치했습니다.  

---

## 반드시 고쳐야 할 문제

### 1. “8-parameter Full TMDD” 표현이 혼선 위험이 있습니다.

Draft는 M4를 **“8-parameter ODE system”**이라고 부르면서도, 실제 설명에서는 `Cl_L, Vc, Cl_d, Vt, kon, koff, ke(RL), R0, kout`처럼 **9개 structural quantity**를 나열합니다. 

PK27 Table 27.2에서는 `Cl, Kon, Koff, Vt, Cld, Kout, R0, Ke(RL)`의 8개 estimate가 제시되고, `Vc`는 별도로 0.05 L/kg로 고정하는 초기 가정/근사로 설명됩니다. 

따라서 Phase 4에서 다음처럼 정리해야 합니다.

```text
Full TMDD model contains 9 structural quantities if fixed Vc is counted:
Cl(L), Vc, Cld, Vt, kon, koff, kout, R0, ke(RL).

In PK27 Table 27.2, 8 parameters are estimated/reported because Vc is fixed to 0.05 L/kg.
```

이걸 안 고치면 독자가 “8개라면서 왜 9개를 쓰지?”라고 느끼고, Apex Concept의 신뢰도가 떨어집니다.

---

### 2. NDA Deficiency Letter, 6–18개월 지연, 200만 달러 손실 등은 출처 없는 실무 시나리오입니다.

Draft는 MM 근사를 잘못 쓰면 FDA reviewer가 특정 문구의 Deficiency Letter를 보내고, 6–18개월 modeling 추가 작업과 200만 달러 손실이 발생한다고 매우 구체적으로 씁니다. 

하지만 첨부 PDF가 직접 지지하는 것은 **MM 모델이 저용량 ligand profile에서 systematic deviation을 보이고, Km이 3.7 vs 0.03으로 크게 over-predicted되었다는 점**입니다.  

따라서 아래처럼 낮춰야 합니다.

```text
[교과서 기반] PK27에서는 MM 근사가 저농도 profile에서 systematic deviation을 보였고, Km이 TMDD 기반 값보다 크게 over-predicted되었다.

[교과서 외 실무 해석] 이런 상황에서 외삽 기반 용량 정당화를 제출하면 reviewer가 target occupancy, sensitivity analysis, Full TMDD 또는 QSS/QE 근사의 정당화를 요구할 수 있다.
```

**“FDA 문구”, “6–18개월”, “200만 달러”는 삭제하거나 `[교과서 외 실무 가상 시나리오]`로 명확히 라벨링해야 합니다.** Scope Lock도 출처 없는 수치·조건·page citation을 만들지 말라고 명시합니다. 

---

### 3. M2의 일부 extrapolation은 과감합니다.

M2에서 `lymph recovery ≈ 3.2% per kDa`, **mAb 150 kDa에서 lymph recovery >80% 추정**이라는 표현은 교육적으로는 직관적이지만, 그대로 “문헌 수치”처럼 두면 위험합니다. Draft는 R&T Table/Figure 기반으로 신장 sieving, lymphatic recovery, sc bioavailability를 잘 끌어왔지만, 150 kDa mAb에 대한 단순 선형 외삽은 원문 직접 수치가 아니라 계산적 해석입니다.  

수정 권장:

```text
R&T의 Supersaxo data는 MW 증가에 따라 lymphatic recovery가 증가하는 방향성을 보여준다.
다만 150 kDa mAb에 이를 단순 선형 외삽하는 것은 교육용 직관일 뿐, 정량 예측값으로 사용하면 안 된다.
```

---

### 4. NONMEM `$DES` 코드는 “출처 기반”이 아니라 “구현 번역”입니다.

Draft에는 TMDD를 NONMEM `$DES` 형태로 구현한 코드가 들어가고, 이를 “Gabrielsson PK27 + 표준 NONMEM ADVAN13 패턴”으로 설명합니다. 

문제는 첨부 PDF 자체가 NONMEM control stream을 제공한 것은 아니라는 점입니다. 따라서 코드를 넣는 것은 좋지만, 라벨을 바꿔야 합니다.

```text
[교과서 외 구현 번역 예시]
아래 코드는 PK27의 ODE 구조를 NONMEM ADVAN13 스타일로 옮긴 교육용 skeleton이다.
원문에 수록된 control stream은 아니다.
```

이 라벨링만 하면 오히려 매우 유용한 콘텐츠가 됩니다.

---

### 5. Completion block의 “계속 입력하면 Step 2”는 현재 워크플로우와 충돌합니다.

Draft 마지막은 “계속을 입력하면 Step 2 HTML 컴파일러가 실행됩니다”라고 끝납니다. 
하지만 현재 사용 중인 HTML 워크플로우는 **Phase 1 → Phase 2 Source Fidelity Audit → Phase 3 Insight Crucible → Phase 4 Content Lock → Phase 4C Visual Pedagogy → Phase 5 HTML Compile** 순서입니다. 특히 A-Critical에서는 Source Fidelity와 Visual Pedagogy를 생략하면 안 된다고 되어 있습니다.  

따라서 지금은 “계속”으로 HTML을 만들면 안 됩니다.
다음 입력은 **Phase 2 감사 프롬프트**여야 합니다.

---

## 종합 판정

```text
Phase 1 재실행: 불필요
Phase 2 진행: 필요
HTML 직행: 금지
핵심 수정 필요: 있음
치명적 붕괴: 없음
```

이 결과물은 **Phase 1 Draft v0로는 성공**입니다.
다만 다음 5개는 Phase 2/4에서 반드시 잡아야 합니다.

```text
MUST_FIX
1. “8-parameter” vs “Vc 포함 9 structural quantities” 표현 정리
2. NDA Deficiency Letter/6–18개월/200만 달러 등 출처 없는 실무 수치 라벨링 또는 삭제
3. lymph recovery >80% 같은 선형 외삽 표현을 교육용 해석으로 격하
4. NONMEM `$DES` 코드를 원문 수록 코드가 아니라 구현 번역 예시로 라벨링
5. “계속 → Step 2” 지시를 무시하고 Phase 2 Source Fidelity Audit으로 진행
```

## 다음 단계 권장

바로 **Phase 2 Source Fidelity Audit**을 실행하세요.
감사 프롬프트에는 특히 아래 항목을 명시적으로 추가하는 것이 좋습니다.

```text
추가 감사 지시:
- Full TMDD의 “8-parameter” 표현이 Vc fixed 여부와 일관적인지 확인.
- NDA/FDA/Deficiency Letter/6–18개월/200만 달러 등 규제·비용·기간 관련 문장이 PDF source에 직접 있는지 확인.
- mAb lymph recovery >80% 및 3.2% per kDa 외삽이 source-supported인지 확인.
- NONMEM `$DES` 코드가 원문 기반인지, 교육용 구현 번역인지 분류.
- PK26 Efalizumab 수치(Vt, Vmax, Km, Cl_d, Cl_L)와 PK27 Table 27.2 수치가 정확한지 전수 대조.
```

최종적으로는 **“Phase 1은 잘 뽑혔지만, 과감한 실무 해석이 섞인 고밀도 초안”**입니다. 이 상태에서 Phase 2 감사만 제대로 걸면 좋은 Content Lock으로 갈 수 있습니다.

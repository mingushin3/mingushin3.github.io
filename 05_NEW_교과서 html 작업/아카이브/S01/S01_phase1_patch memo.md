## 판정

**Phase 1 Draft v0는 꽤 잘 뽑혔습니다. “재작성” 대상은 아닙니다.**
다만 **최적 완성본은 아니고, Phase 2 Source Fidelity Audit으로 넘기기 전 “Audit Attention Memo”를 붙이는 것이 좋습니다.**

요약 판정은 다음입니다.

| 항목                    |     평가 |
| --------------------- | -----: |
| Scope Lock 준수         |   8/10 |
| Curation Map 적절성      |   9/10 |
| MUST/CONTEXT 분리       | 8.5/10 |
| CL·V·K·t½ 위계 설명       |   9/10 |
| Gabrielsson/R&T 역할 분담 |   8/10 |
| 원문 근거 없는 실무 확장 억제     | 6.5/10 |
| HTML 전환 준비도           |   7/10 |

**종합: 조건부 Go.**
바로 HTML로 넘기지는 말고, **원본 v0 보존 → Phase 2 Audit → Phase 4A에서 압축·패치**가 맞습니다.

---

## 잘된 부분

### 1. Curation Map은 거의 정답에 가깝습니다

Scope Lock은 이 세션의 핵심을 **CL·V·t½·K의 정의, 도출, 상호의존 관계**로 못 박고, 카드 수를 “CL·V·t½·K 핵심 4개 + MRT 1개 이내”로 제한했습니다. Draft는 정확히 **C1 Clearance, C2 Volume, C3 K, C4 Half-life, C5 MRT** 5개로 구성했습니다. 이건 매우 좋은 선택입니다.  

특히 “$CL$과 $V$는 primary, $K$와 $t_{1/2}$는 secondary”라는 중심축은 원문과 잘 맞습니다. Gabrielsson도 $CL$과 $V$를 독립적 primary parameter로 보고, $K$, $t_{1/2}$, AUC를 derived/secondary parameter로 설명합니다. 

### 2. Ka·F를 MUST로 승격하지 않은 점이 좋습니다

Scope Lock에서 가장 큰 함정으로 지적한 부분이 **extravascular absorption, Ka, F, tlag를 MUST 카드로 승격하지 말 것**이었습니다. Draft는 이를 CONTEXT로 분류하고, “별도 흡수 모델 세션 주제”라고 처리했습니다. 이건 정확합니다.  

### 3. Gabrielsson과 R&T의 역할 분담도 대체로 맞습니다

Draft는 Gabrielsson을 수식 도출·Compound A 계산 anchor로, R&T를 reservoir-extractor model, $CL = Q \cdot E$, distribution/terminal phase 해석으로 사용했습니다. 이 분담은 Scope Lock의 지시와 부합합니다. 

R&T Ch.3도 reservoir-extractor 모델에서 extraction ratio와 $CL = Q \cdot E$를 도출하고, $k = CL/V$ 및 $t_{1/2}=0.693 \cdot V/CL$ 관계를 설명합니다. Draft의 큰 수식 흐름은 원문 구조와 맞습니다. 

---

## 최적이라고 보기 어려운 부분

### 1. Big Idea 일부가 원문보다 강합니다

C1 Big Idea에서 “환자를 죽일 수 있는 추론” 같은 표현은 교육적 임팩트는 있지만, 원문 기반 표현으로는 과합니다. 원문은 $t_{1/2}$가 $CL$과 $V$ 모두에 의존한다는 점을 강조하지, 특정 임상 결과를 그렇게 단정하지는 않습니다. 

권장 패치 방향:

> “치명적 오판으로 이어질 수 있다” 정도로 낮추고, “환자를 죽일 수 있다”는 표현은 삭제하거나 `[실무 추론]`으로 표시.

### 2. “신부전 + 부종으로 V 30–50% 증가”는 Source Fidelity Audit 대상입니다

Draft의 Plausible Fallacy에서 “신부전 환자에서 부종이 동반되면 $V$가 30–50% 증가 가능”이라고 했는데, 현재 Scope Lock의 지정 원문 범위에서 바로 확인되는 수치 anchor는 아닙니다. 이런 표현은 **NOT_IN_SOURCE 가능성이 높습니다.** 

이 문장은 다음처럼 바꾸는 편이 안전합니다.

> $t_{1/2}$ 증가는 $CL$ 감소, $V$ 증가, 또는 둘의 조합으로 발생할 수 있다. 따라서 $t_{1/2}$만 보고 유지용량을 조정하면 원인을 잘못 짚을 수 있다.

### 3. High/low extraction 설명은 약간 앞서 나갑니다

Draft C1의 Limitations에는 high-extraction, low-extraction 약물 분기가 꽤 구체적으로 들어갑니다. R&T Ch.3에서 $CL = Q \cdot E$까지는 범위 내이지만, high/low extraction의 임상 분기와 예시 약물까지 본격화하는 것은 후속 clearance/hepatic extraction 세션 쪽 내용입니다. Scope Lock도 이 세션은 CL·V·K·t½ 중심이고, hepatic/renal clearance 기전은 후속 지식으로 열어주는 위치라고 정리했습니다. 

처리 권장:

> C1에서는 “$CL=Q \cdot E$는 후속 hepatic/renal clearance 세션에서 high/low extraction 분기로 확장된다” 한 문장만 남기고, propranolol/warfarin/phenytoin 예시는 삭제 또는 후속 세션 링크로 이동.

### 4. GOF 시그니처와 NONMEM 진단 표현은 원문 밖입니다

“Volume Drift pattern”, “CWRES vs TIME 초기 시점 음의 편향”, “eGFR을 CL에만 모델링했을 때” 같은 문장은 실무적으로 유용하지만, Gabrielsson/R&T 지정 범위의 직접 내용은 아닙니다. 

이런 내용은 완전히 삭제할 필요는 없지만, Phase 4A에서 다음처럼 처리하는 것이 좋습니다.

> `[실무 추론]` 또는 `<!-- TRENCH -->`로 분리하고, 1–2문장으로 압축.

### 5. MRT는 좋은 MUST지만, 다구획 확장은 조심해야 합니다

MRT를 C5로 둔 것은 좋습니다. Gabrielsson은 AUMC/AUC로 MRT를 정의하고, 1구획 IV bolus에서는 $MRT = 1/K$ 흐름이 자연스럽게 나옵니다. 

다만 Q8에서 $MRT/t_{1/2}=1.85$이면 다구획 가능성, ADVAN3/TRANS4 전환, $V_{ss}=V_1+V_2$ 검증까지 이어지는 설명은 학습적으로 좋지만, 이 세션 원문에서 직접 도출된 것과 후속 PopPK 실무 추론이 섞여 있습니다. 

권장 처리:

> Q8은 유지 가능. 단, “후속 다구획 세션으로 연결되는 진단적 힌트”라고 명시하고, Phase 2에서 NOT_IN_SOURCE가 나오면 `[실무 확장]` 태그를 붙이는 방식이 안전합니다.

---

## 바로 수정하지 말고 Phase 2로 넘겨야 하는 이유

이 Draft 자체도 마지막에 “계속”을 누르면 HTML로 갈 수 있지만, v3.3.2 워크플로우에 따르면 다음 단계는 **Step 2 직접 진행이 아니라 Phase 2 Source Fidelity Audit**이라고 스스로 적어두었습니다. 이 판단이 맞습니다. 

특히 이번 세션은 **A-Critical**입니다. Scope Lock에서 CL·V·t½는 모든 PopPK 모델링의 추정 파라미터이자 NDA/IND PopPK 보고서 핵심 기술 항목이라고 분류했으므로, “좋아 보이니 바로 HTML”로 가면 안 됩니다. 

---

## 권장 Patch Memo

Phase 1 원본은 그대로 보존하고, Phase 2에 아래 메모를 같이 붙이세요.

```markdown
# Audit Attention Memo — Session 01 Step 1 Draft v0

## 1. Big Idea 강도 점검
C1 Clearance Big Idea의 “환자를 죽일 수 있는 추론” 표현은 원문보다 강할 수 있음.
Phase 2에서 PDF 근거 여부를 확인하고, 필요 시 “치명적 오판으로 이어질 수 있다”로 완화.

## 2. NOT_IN_SOURCE 가능성
C1 Plausible Fallacy의 “신부전 환자에서 부종 동반 시 V 30–50% 증가”는 PDF 직접 근거 확인 필요.
근거 없으면 삭제하거나 [실무 추론]으로 표시.

## 3. High/Low extraction 범위 초과 가능성
C1 Limitations의 high-extraction / low-extraction 구체 예시는 후속 Ch.5 clearance 세션 내용일 수 있음.
본 세션에서는 “CL = Q·E가 후속 extraction model로 확장된다” 1문장으로 압축 권장.

## 4. GOF/NONMEM 진단 표현
“Volume Drift pattern”, “CWRES vs TIME 초기 음의 편향”은 원문 직접 내용이 아니라 실무 확장 가능성이 큼.
Phase 4A에서 TRENCH tip으로 1–2문장 압축하거나 [실무 추론] 표시.

## 5. MRT 다구획 확장
Q8의 MRT/t½ 비율 기반 다구획 진단은 교육적으로 유용하지만 후속 세션 확장임.
원문 직접 근거와 실무 확장 범위를 구분.
```

---

## 최종 결론

이번 Phase 1은 **이전 Pre-Sprint 세션보다 더 안정적입니다.**
Curation Map, 카드 수, CL·V·K·t½ 위계, Ka·F 차단은 잘 됐습니다.

다만 **“거장의 시각”을 살리려다 원문보다 강해진 문장**이 있고, 일부 실무 진단 표현이 PDF 범위를 넘어갑니다. 그래서 최적 동선은 다음입니다.

> **재작성 X → 원본 v0 보존 → Audit Attention Memo 첨부 → Phase 2 Source Fidelity Audit → Phase 4A에서 공식 패치 → Phase 5 HTML Compile**

즉, **좋은 v0이지만, 바로 HTML로 넘길 완성본은 아닙니다.**

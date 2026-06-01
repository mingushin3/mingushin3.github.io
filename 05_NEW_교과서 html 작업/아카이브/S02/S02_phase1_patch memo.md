## 판정

**전체적으로는 잘 작업된 Phase 1 v0입니다. 재작성할 정도의 실패작은 아닙니다.**
다만 이번 Session 02는 A-Critical이고, draft 안에 **원문 기반 내용과 실무 확장·규제 표현이 섞인 부분**이 있어 **바로 HTML로 넘기면 안 됩니다.**

결론은:

> **조건부 Go — 원본 v0 보존 → Audit Attention Memo 첨부 → Phase 2 Source Fidelity Audit → Phase 4A에서 공식 패치**

입니다.

---

## 잘된 부분

### 1. Curation Map의 큰 구조는 좋습니다

Scope Lock은 이 세션의 핵심을 막투과, 관류/투과성 제한, Vd 구조, fu/fuT, 총 농도 vs 비결합 농도 선택으로 정의했고, MUST-tier 상한도 최대 6개로 제한했습니다. 

Draft는 정확히 **M1 막투과**, **M2 분포 율속**, **M3 Vd 수학 구조**, **M4 단백결합 비선형성**, **M5 조직결합/Kp**, **M6 총 vs 비결합 노출 지표**의 6개로 정리했습니다. 방향 자체는 Scope Lock에 매우 잘 맞습니다. 

### 2. Apex를 M3, Critical Blow를 C vs Cu로 둔 판단은 적절합니다

Apex를 **분포용적의 수학 구조**로 둔 것은 좋습니다. 이 세션의 본질은 “Vd는 실제 부피가 아니라 fu와 fuT, Kp가 만든 비례상수”라는 점이기 때문입니다. Scope Lock도 Vd의 수학 구조와 fu/fuT가 후속 간 추출비, covariate modeling, PBPK, TDM의 토대라고 명시합니다. 

Critical Blow를 **C vs Cu**로 둔 것도 맞습니다. G&W는 total concentration이 fu에 의해 confounded될 수 있고, unbound concentration이 종간 비교와 safety margin 예측에서 더 적절한 경우가 많다고 설명합니다. 

### 3. 핵심 실제 데이터 anchor를 꽤 잘 잡았습니다

Warfarin nephrotic syndrome 데이터는 Scope Lock의 핵심 anchor였고, 원문에도 V 9.4→13.7 L, CL 0.20→0.58 L/hr, t½ 36→18 hr, albumin 43→12.5 g/L가 제시되어 있습니다. 

PK47도 Compound 1/2의 protein concentration, n, Ka≈6, 동시 fitting의 의미를 잘 반영했습니다. G&W는 실제로 Compound 1은 protein concentration 50/0.3, Compound 2는 10/0.1에서 fitting하고, low/high protein concentration 동시 fitting으로 n과 Ka의 correlation을 줄이고 precision을 높인다고 설명합니다. 

---

## 최적이라고 보기 어려운 부분

### 1. M4의 수식 표기가 Curation Map에서 불안정합니다

Curation Map의 M4에는 PK47 식이 `fu = 1/[1 + ...]`처럼 요약되어 있는데, 본문 카드에서는 `fu = 1 - 1/(1 + Cu/(nPT) + 1/(Ka·nPT))` 형태로 씁니다.  

이건 작은 문제처럼 보이지만 A-Critical 세션에서는 **수식 일관성 오류**로 취급해야 합니다. 특히 Phase 2에서 반드시 Eq.47:1 원문과 대조해야 합니다. 원문 PDF는 Eq.47:1이 Cu와 fu의 관계를 나타낸다고 설명하고, Eq.47:3, Eq.47:4로 low-Cu 근사와 Ka 초기 추정을 이어갑니다. 

**패치 방향:** Curation Map에서는 복잡한 식을 쓰지 말고 이렇게 바꾸는 것이 안전합니다.

> **M4 | 혈장단백결합과 fu의 농도의존성** — R&T Eq.4-17~4-19와 G&W PK47 Eq.47:1~47:4를 통해 fu가 Cu, protein concentration, n, Ka의 함수임을 이해한다.

### 2. PK47이 독립 개념처럼 보입니다

Scope Lock은 “G&W PK47 데이터는 §2 B항 수치 앵커로만 사용”하고, “PK47은 독립 개념이 아니라 단백결합 MUST 카드의 Dynamic Source Anchoring 소스”라고 명시했습니다. 

Draft의 M4는 제목 자체가 “단백결합의 비선형성”이라 개념상은 맞지만, 괄호 안에 PK47 식을 전면에 내세워 **PK47이 별도 MUST 개념처럼 보이는 위험**이 있습니다. 

**패치 방향:** M4 제목을 유지하되, PK47은 “B. Derivation / Source-anchored data” 안으로 내리세요. 제목은 다음이 더 좋습니다.

> **M4 · 혈장단백결합과 fu의 농도의존성**

### 3. Big Idea 일부가 원문보다 강합니다

M1 Big Idea에서 “CNS 약물 개발에서 후보 물질이 BBB를 통과하지 못해 임상 1상에서 폐기되는 일이 매년 수십 건”이라는 표현은 원문 범위에서 확인되는 수치가 아닙니다. Draft에는 그렇게 쓰여 있지만, 원문은 BBB 투과가 logP, size, P-gp substrate 여부에 영향을 받는다는 예시를 제시하는 수준입니다.  

**패치 방향:** “매년 수십 건”은 삭제하고, 원문 기반으로 낮추세요.

> CNS 노출이 필요한 약물에서는 BBB 투과성이 후보물질 선별의 핵심 병목이 된다. R&T의 Fig.4-4처럼 lipophilicity가 높아도 P-gp 기질이면 실제 BBB 투과가 낮을 수 있다.

### 4. Regulatory 표현이 과합니다

M6에서 “FDA reviewer가 deficiency letter를 발행한다”는 문장은 교육적 임팩트는 있지만, 첨부 원문 자체의 직접 표현은 아닙니다. Draft에는 이렇게 강하게 들어가 있고, Scope Lock도 IND/NDA 규제 언어를 다루라고 했지만, “deficiency letter 발행”까지는 실무 추론으로 분리해야 합니다.  

**패치 방향:**

> `[실무 추론]` 태그를 붙이거나, “규제 검토에서 active species 정의의 근거를 요구받을 수 있다” 정도로 낮추는 편이 안전합니다.

### 5. M5의 Rodgers–Rowland/PBPK 확장이 약간 앞서 갑니다

M5의 조직결합/Kp 설명은 좋습니다. R&T 원문도 metoprolol의 tissue Kp가 acidic phospholipid content와 관련된다는 Fig.4-24를 제시합니다. 

다만 draft는 “Rodgers–Rowland method의 핵심”, “약 80%의 분산 설명”, “FIH dose prediction에서 Vd를 한 자릿수 단위로 빗나감”처럼 상당히 강한 PBPK 확장 표현을 씁니다.  이 중 일부는 후속 PBPK 세션이나 외부 문헌 영역입니다.

**패치 방향:** M5 본문에서는 원문 기반으로 “acidic phospholipid와 Kp의 강한 관련성”까지만 두고, Rodgers–Rowland method는 `[후속 PBPK 연결]` 1문장으로 줄이는 것이 좋습니다.

### 6. CONTEXT 항목 일부가 실제로는 꽤 길어질 위험이 있습니다

Scope Lock은 Appendix B는 CONTEXT 고정, Appendix C/D는 독립 MUST 카드 금지라고 했습니다.  Draft는 Curation Map에서는 이 규칙을 잘 지켰습니다. 

다만 실제 본문에서 App.C의 small-Vd 모델, App.D의 plasma-to-blood ratio가 길게 확장되면 Curation Map의 선언과 어긋날 수 있습니다. App.C는 Vd 카드의 B항 수식 보조로는 매우 중요하지만, 별도 “부록 해설 카드”처럼 커지면 안 됩니다. App.C 원문은 Eq.C-13, C-14로 albumin-bound small-Vd 약물의 V가 fu와 선형으로 변한다는 핵심을 제시합니다. 

---

## 이번 v0의 종합 점수

| 항목             |       점수 |
| -------------- | -------: |
| Scope Lock 반영  |   8.5/10 |
| Curation Map   | 8.5–9/10 |
| 핵심 개념 선정       |     9/10 |
| 실제 데이터 anchor  |   8.5/10 |
| 원문 충실성         |     7/10 |
| 과장·실무 확장 통제    |   6.5/10 |
| Phase 2 투입 준비도 |     8/10 |
| HTML 직행 준비도    |   6.5/10 |

---

## 권장 진행

**Phase 1을 다시 돌릴 필요는 없습니다.**
하지만 지금 상태로 HTML로 넘기는 것은 비추천입니다. 이 v0는 “좋은 초안”이지 “Content Lock”은 아닙니다.

다음처럼 진행하세요.

```markdown
# Audit Attention Memo — Session 02

## 1. M4 수식 일관성 점검
Curation Map의 M4 식과 본문 M4 Eq.47:1 표기가 다르게 보임.
Phase 2에서 G&W PK47 Eq.47:1 원문과 대조 후 Curation Map 표현을 단순화할 것.

## 2. PK47의 위치 조정
Scope Lock은 PK47을 독립 개념이 아니라 단백결합 카드의 수치 anchor로 지정함.
M4 제목을 “혈장단백결합과 fu의 농도의존성”으로 조정하고, PK47은 B항 데이터 anchor로 유지.

## 3. M1 Big Idea 과장 표현
“CNS 후보물질이 BBB 미통과로 임상 1상에서 매년 수십 건 폐기”는 PDF 직접 근거 확인 필요.
근거 없으면 삭제하거나 [실무 추론]으로 표시.

## 4. Regulatory 표현 완화
“FDA reviewer deficiency letter” 표현은 원문 직접 근거가 아니라 실무 추론일 가능성.
“active species 정의와 unbound exposure 근거를 요구받을 수 있다” 정도로 완화.

## 5. Rodgers–Rowland/PBPK 확장 압축
M5의 acidic phospholipid/Kp 설명은 유지.
Rodgers–Rowland method, FIH prediction 오차 표현은 후속 PBPK 연결 1문장으로 축소.

## 6. Appendix C/D 비대화 방지
App.C Eq.C-13/C-14는 M3 B항에 유지하되, 별도 카드처럼 확장하지 말 것.
App.D plasma-to-blood ratio는 M5 또는 M6에서 1–2문장만 유지.
```

## 최종 결론

이번 Phase 1은 **내용 포착력은 높고, 구조도 좋습니다.** 특히 M3 Apex와 C vs Cu Critical Blow는 맞게 잡았습니다.

문제는 **잘못된 구조가 아니라 과밀도와 과장 강도**입니다. 원문 근거가 있는 강한 내용과, 실무적으로 맞지만 PDF 직접 근거가 약한 표현이 섞여 있습니다.

따라서 최적 동선은:

> **재작성 X → 원본 v0 보존 → 위 Audit Attention Memo 첨부 → Phase 2 Source Fidelity Audit → Phase 4A에서 공식 패치**

입니다.

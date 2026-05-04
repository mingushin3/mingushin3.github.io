## 판정

**이번 Phase 1 결과물은 “내용 포착력은 높지만, 최적화된 Step 1 완성본은 아닙니다.”**
재작성할 정도의 실패작은 아니지만, **바로 HTML로 넘기기에는 과밀하고, 일부 항목은 Source Fidelity Audit 전까지 잠금 처리하면 안 됩니다.**

종합 판정은:

> **조건부 Go — 원본 v0 보존 → Audit Attention Memo 첨부 → Phase 2 Source Fidelity Audit → Phase 4A에서 강한 압축·정렬 후 HTML 진행**

입니다.

점수로 보면 대략 다음 정도입니다.

| 항목                      |       평가 |
| ----------------------- | -------: |
| 전체 source 포착력           |     9/10 |
| 청소율·간·신장·대사체 핵심 개념 커버리지 |     9/10 |
| Scope Lock 반영           | 7.5–8/10 |
| Curation 효율성            |     6/10 |
| CONTEXT 압축 규칙 준수        |     6/10 |
| Source fidelity 위험 관리   | 6.5–7/10 |
| HTML 직행 준비도             | 5.5–6/10 |

---

## 잘된 부분

### 1. 큰 범위의 source 통합 자체는 잘 됐습니다

Draft는 Gabrielsson §2.3, §2.5, PK5와 Tozer Ch.5, Ch.20, App.D/E를 모두 명시하고, 각 부분의 mode mapping도 구분했습니다. 특히 Gabrielsson §2.5, Tozer Ch.5, Tozer Ch.20을 A-Critical로 본 판단은 Scope Lock과도 맞습니다. 

Scope Lock도 이 세션을 신장 청소율, 간 청소율 모델, IVIVE, PK5 실전 적용, Tozer Ch.5, Ch.20까지 포괄하는 다층 구조로 정의합니다. 

### 2. 핵심 개념 누락은 크지 않습니다

Curation Map은 M1–M20으로 clearance 정의, ClR/fe, ARE vs excretion rate plot, well-stirred model, high/low extraction, route×fu, IVIVE, Table 2.9, PK5, plasma vs blood clearance, clearance additivity, renal reabsorption, half-life, extended clearance, parent–metabolite mass balance, rate-limiting step, first-pass metabolite effect, steady-state metabolite, renal impairment metabolite accumulation까지 포괄합니다. 

이 정도면 “중요한 내용을 빠뜨렸다”는 쪽의 문제는 아닙니다. 오히려 반대입니다. **너무 많이 살렸습니다.**

### 3. App.D/E를 독립 MUST로 올리지 않은 판단은 좋습니다

Draft는 App.D/E를 B-Standard 보강 자료로 두고, 기존 M4, M10, M15, M18에 붙이는 구조를 택했습니다. 이건 맞는 방향입니다. Scope Lock도 App.D/E가 first-principles 보강 역할이지 독립 세션 핵심이 아님을 암시합니다. 

### 4. Figure marker를 넣지 않은 점은 맞습니다

Scope Lock은 Image rights = None이고, 교재 figure는 임베드 금지, 대신 자체 SVG/CSS 제작을 지시합니다.  Draft도 Phase 1에서는 FIGURE marker를 넣지 않았다고 명시합니다. 

---

## 최적이라고 보기 어려운 부분

### 1. MUST가 20개인 것은 “Master’s Lens”라기보다 “전체 백과사전”에 가깝습니다

Draft는 Rule 1을 만족한다고 하면서 M1–M20을 모두 full Concept Anatomy Card로 처리했다고 스스로 적고 있습니다. 

문제는 **20개 모두가 정말 “이 개념 없이는 다음 개념 이해가 구조적으로 붕괴하는가?”라는 MUST test를 통과했느냐**입니다. 이 중 상당수는 반드시 full card여야 하는 개념이라기보다, 상위 card 안에 들어갈 submodule 또는 clinical extension입니다.

예를 들어 다음은 full MUST로 두기보다 압축 가능합니다.

* M12 Biliary/EHC → M11 또는 M13의 elimination route subcard
* M14 Half-life as derived parameter → M1/M11의 derived parameter bridge
* M18 First-pass metabolite impact → M16/M17의 route-dependent extension
* M19 Steady-state metabolite → M16/M20의 dosing-regimen extension
* App.D/E 보강부 → M10/M4/M15/M18의 1–2문장 또는 appendix note

따라서 현재 v0는 **“coverage draft”로는 좋지만 “curated learner-facing Step 1”로는 과밀**합니다.

### 2. CONTEXT 1–2문장 규칙이 실질적으로 약해졌습니다

Curation Map은 CONTEXT를 “가장 가까운 MUST 카드 안에 1–2문장 흡수”라고 선언했습니다.  그런데 완료 블록을 보면 App.D Study Problem 정량 풀이, KpBC 계산, anemic/nephrotic C/Cb 계산, Q14 정량 시나리오까지 확장되어 있습니다. 

이건 나쁜 내용은 아니지만, **CONTEXT 처리라기보다 mini-card 또는 advanced worked example**에 가깝습니다. HTML로 가면 학습자는 “핵심 흐름”과 “부록 검증”을 같은 무게로 읽게 됩니다.

### 3. Table 2.9는 아직 HTML 직행 불가입니다

Scope Lock은 Table 2.9의 Well-stirred / Parallel tube / Distributed / Dispersion model 수식을 원문과 1:1 대조하라고 명시했고, 특히 Distributed/Dispersion의 지수 표현식은 오타 위험이 높다고 경고했습니다. 

Draft 완료 블록도 M8 Table 2.9의 Distributed/Dispersion 식은 “Roberts & Rowland 1986 원전 재검증 필요”로 남아 있다고 적고 있습니다.  원문 PDF도 p.93–94에서 distributed model과 dispersion model의 식 및 Table 2.9 요약을 다루므로, 이 부분은 Phase 2에서 반드시 대조해야 합니다. 

**이 항목 하나만으로도 HTML 직행은 보류해야 합니다.**

### 4. §7 Self-Test가 너무 비대합니다

Draft는 §7을 “Q1–Q8 + Q14 + Quick Self-Test 19문항” 구조로 만들었습니다.  Q14 자체는 두 목표가 충돌하는 Socratic Dilemma 형식을 갖추었지만, 전체 §7은 이미 하나의 독립 casebook처럼 커졌습니다. 

원래 §7의 역할은 마지막에 개념 간 tension을 응축하는 것입니다. 지금은 **Self-Test가 학습 정리라기보다 mini-exam + case simulation + decision tree**가 되었습니다. A-Critical이라도 HTML에서는 본문 질문 6–8개 + final dilemma 1개 정도가 적절합니다.

### 5. “가설 시나리오”와 “원문 수치”가 섞여 있습니다

Q14와 metabolite dose adjustment 쪽은 교육적으로 좋지만, 일부 수치는 내부 가정 기반입니다. Draft도 Q14 정량을 “가설 시나리오”라고 명시합니다. 

이런 부분은 삭제할 필요는 없지만, HTML 전환 전 다음처럼 구분해야 합니다.

* `[원문 직접 수치]`: Tozer 예제, PK5 최종값, Table 수치
* `[원문 기반 계산]`: 교재 식을 사용해 재계산한 값
* `[교육용 가상 시나리오]`: Q14처럼 scenario를 구성한 값
* `[실무 추론]`: AIMS DDI, NONMEM metadata tip 등

현재 draft에는 “신부전 코호트 용량 5–10% 과소추정”, “7배 과량”, “AIMS DDI phase 1 safety” 같은 문장이 강하게 들어가는데, 일부는 교재 직접 근거가 아니라 실무 확장입니다.  

### 6. 파일명과 세션명이 혼동됩니다

업로드 맥락은 Session 04인데 draft 내부 제목은 `01_step1_draft_v0.md`로 되어 있습니다.  작은 문제처럼 보이지만, 이 워크플로우는 파일을 스노우볼로 넘기므로 **파일명/세션명 불일치가 이후 Phase 2/4/HTML 관리에서 실제 혼선**을 만듭니다.

---

## 최종 판단

이번 결과물은 **“잘 모은 초안”**입니다.
하지만 **“잘 큐레이팅된 최종 Step 1”은 아닙니다.**

가장 큰 문제는 내용 부족이 아니라:

1. **MUST 20개로 인한 과밀**
2. **CONTEXT의 mini-card화**
3. **Table 2.9 검증 미완**
4. **§7 과대 확장**
5. **원문 수치와 교육용 가상 시나리오의 구분 부족**
6. **파일명/세션명 혼선**

입니다.

따라서 **Phase 1 재작성은 비효율적**이고, 대신 Phase 2와 Phase 4A에서 강하게 정리하는 것이 맞습니다.

---

## 권장 Audit Attention Memo

Phase 2에 아래 메모를 같이 붙이세요.

```markdown
# Audit Attention Memo — Session 04 Step 1 Draft v0

## 1. MUST 20개 과밀 점검
Draft는 M1–M20을 모두 full Concept Anatomy Card로 처리함.
Phase 2/4A에서 실제 MUST인지, subcard/context로 낮출 수 있는지 검토 필요.
특히 M12, M14, M18, M19, App.D/E 보강부는 압축 후보.

## 2. CONTEXT 1–2문장 규칙 점검
App.D/E는 CONTEXT로 분류되어 있으나, Study Problem 계산과 Q14 시나리오까지 확장됨.
Phase 4A에서 M4/M10/M15/M18 내 1–2문장 보강 또는 appendix note로 축소.

## 3. Table 2.9 검증 필수
Scope Lock은 Distributed/Dispersion model 수식의 1:1 대조를 요구함.
Draft 완료 블록에도 M8 Table 2.9 Distributed/Dispersion 식 재검증 필요가 남아 있음.
Phase 2에서 원문 Table 2.9 및 Eq.2:234–2:236과 대조.

## 4. PK5 수치 구분
PK5 최종 추정값 Cl = 1.2 L/h, fe ≈ 35%, ClR = 0.42 L/h와
초기 추정값 V ≈ 7 L, Cl ≈ 2 L/h가 혼용되지 않았는지 확인.

## 5. §7 Self-Test 압축
현재 Q1–Q8 + Q14 + Quick Self-Test 19문항 구조.
HTML 전환 전 본문 질문 6–8개 + final Socratic Dilemma 1개로 축소 권장.

## 6. 원문 수치 vs 가상 시나리오 태그 분리
Q14 및 13배/7배/25–30% dose reduction 관련 문장은
[원문 직접 수치] / [원문 기반 계산] / [교육용 가상 시나리오] / [실무 추론]으로 구분.

## 7. 타 챕터 교차 참조 태그 점검
Scope Lock은 Ch.5 ↔ Ch.20 ↔ App.D/E 교차 참조 시 [확인 필요] 태그 또는 보강 수준을 요구함.
내용 확장인지 단순 연결인지 Phase 2에서 판정.

## 8. 파일명 정리
내부 제목이 01_step1_draft_v0.md로 되어 있음.
Session 04와 맞도록 04_step1_draft_v0.md로 정리.
```

---

## 결론

**이 Phase 1은 버리면 안 됩니다.**
커버리지는 훌륭하고, 큰 개념축도 대부분 맞습니다.

하지만 **이대로 HTML로 넘기면 과밀한 백과사전형 HTML이 될 가능성이 큽니다.**
따라서 최적 동선은 다음입니다.

> **재작성 X → 원본 v0 보존 → Audit Attention Memo 첨부 → Phase 2 Source Fidelity Audit → Phase 4A에서 강한 compression/content lock → Phase 4C → HTML Compile**

이번 세션은 특히 **Phase 4A의 압축 능력이 품질을 결정**합니다. Phase 2는 오류를 잡는 단계이고, Phase 4A는 “20개 atomic unit을 학습자가 실제로 체화할 수 있는 형태로 줄이는 단계”가 되어야 합니다.

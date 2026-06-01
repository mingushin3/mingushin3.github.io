## 판정

**이번 Session 06 Phase 1 v0는 구조는 좋고, 핵심 개념 선별도 꽤 정확합니다.**
다만 **최적 완성본은 아닙니다. 바로 HTML로 넘기면 안 됩니다.**

가장 적절한 판정은:

> **조건부 Go — 재작성 X / 원본 v0 보존 / Audit Attention Memo 첨부 / Phase 2 Source Fidelity Audit 진행**

입니다.

점수로 보면 대략 다음입니다.

| 항목                |       평가 |
| ----------------- | -------: |
| Scope Lock 반영     |     8/10 |
| Curation Map 적절성  |   8.5/10 |
| MUST 개념 선별        |     9/10 |
| NCA 핵심 수식 포착      |   8.5/10 |
| MRT/Vss Apex 설정   |     9/10 |
| 실제 data anchor 반영 | 6.5–7/10 |
| 원문 근거 vs 실무 확장 분리 |     6/10 |
| HTML 직행 준비도       |   6.5/10 |

---

## 잘된 부분

### 1. MUST 4개 선정은 좋습니다

Scope Lock은 이 세션을 **AUC/AUMC/MRT/Vss 수식 도출, λz 추정 전략, NCA→회귀 모델 전환, BA/BE·NDA 노출 지표, 비선형 PK 초기모수 전략**이 모두 포함된 A-Critical 챕터로 지정했습니다. 

Draft는 이를 **C1 AUC 계산**, **C2 AUMC/MRT**, **C3 CL·Vss·Vz와 투여경로 보정**, **C4 노출 지표 분류**의 4개 MUST로 압축했습니다. 이 구성은 좋습니다. 특히 C3를 Apex로 둔 것은 맞습니다. 

### 2. Big Idea의 방향은 매우 적절합니다

Draft의 핵심 문장인 **“NCA는 model-free가 아니라 compartment-free”**는 이 세션의 본질을 잘 잡았습니다. Gabrielsson 원문도 NCA가 특정 compartment model을 요구하지는 않지만, sampling compartment에서의 elimination은 linear라고 가정한다고 설명합니다. 즉, draft의 핵심 프레이밍은 source와 잘 맞습니다.  

### 3. AUC / log-linear trapezoid / λz / 외삽 구조는 잘 잡았습니다

Draft는 선형 사다리꼴, 로그-선형 사다리꼴, 외삽 AUC, λz 추정을 C1에 묶었습니다. Gabrielsson 원문도 linear trapezoid의 상승·하강 구간 편향, Eq.2:310, Eq.2:311, log-linear trapezoid Eq.2:316, 외삽 Eq.2:319를 순차적으로 제시합니다. 

### 4. §2.8.8을 Apex에 연결한 판단은 좋습니다

Scope Lock은 투여경로 보정, 특히 infusion 시간 보정 누락 시 음수 Vss가 나올 수 있다는 점을 핵심 위험으로 잡았습니다.  Gabrielsson 원문도 half-life가 input time에 비해 짧을 때 Eq.2:328/2:337 대신 Eq.2:366/2:367이 더 robust하고, zero 또는 negative Vss를 피한다고 설명합니다. 

---

## 최적이라고 보기 어려운 부분

### 1. PK41 Turbojoint data anchor가 너무 뒤로 밀렸습니다

Scope Lock은 Turbojoint® PK41 데이터를 **반드시 인용**하라고 지정했습니다. 구체적으로 1명 지원자, 3회 5시간 IV infusion, 310/520/780 µg·kg⁻¹, CL 1.6→0.9 L·h⁻¹·kg⁻¹, V 2.3→1.8 L·kg⁻¹, MRT 1.4→1.9 h, MM 최종 추정 Vmax=184, Km=83, V=1.8을 명시했습니다. 

그런데 draft는 Curation Map에서 PK41의 구체 수치를 “§6 시나리오 전용, §2 카드 침투 금지”로 빼고 있습니다.  문제는 현재 Phase 1 출력 포맷이 `Curation Map → §1 → §2 → §5 → §7 → §8`이고, §6이 없습니다. 따라서 **Dynamic Source Anchoring이 현재 산출물 안에서 충분히 구현되지 않은 상태**입니다.

**패치 권장:** C4 또는 §8에 “PK41 data anchor box”를 4–6줄로 넣으세요. 독립 카드로 만들 필요는 없지만, 완전히 뒤로 밀면 Scope Lock 위반에 가깝습니다.

---

### 2. R&T Table A-1을 “zileuton”으로 부른 부분은 오류 가능성이 큽니다

Draft Curation Map에는 “R&T Table A-1 zileuton & Table H-1”이라고 되어 있습니다.  하지만 R&T Appendix A의 Table A-1은 **경구 50 mg 투여 후 AUC 26.6 mg·hr/L을 계산하는 일반 예제**입니다. Zileuton은 Scope Lock상 Table A-2에 해당합니다.  

**필수 패치:**
`R&T Table A-1 zileuton` → `R&T Table A-1: oral 50 mg generic example, AUC=26.6 mg·hr/L`
`Zileuton`은 `Table A-2`로 분리해야 합니다.

---

### 3. “AUMC 외삽 30–60%”는 Source Fidelity Audit 대상입니다

Draft C2는 “AUMC 외삽이 전체의 30–60%를 차지한다”고 말합니다.  R&T Appendix H는 AUMC 외삽이 AUC 외삽보다 더 중요할 수 있다는 개념을 분명히 보여주지만, 현재 확인 가능한 원문 snippet에서는 특정하게 “30–60%”라는 일반 규칙은 보이지 않습니다. 오히려 Table H-1 예제에서는 AUC, AUMC, MRT 계산값을 제시하며 first-moment curve의 tail이 더 중요하다는 교육적 메시지를 줍니다. 

**패치 권장:**
근거가 확인되지 않으면 다음처럼 완화하세요.

> AUMC 외삽은 AUC 외삽보다 tail에 더 민감하므로, MRT는 AUC보다 λz 선택에 더 크게 흔들릴 수 있다.

숫자 `30–60%`는 Phase 2에서 MATCH가 확인될 때만 유지하세요.

---

### 4. Regulatory 표현이 일부 과강합니다

Draft는 `NDA Deficiency Letter`, `Clinical Hold`, `FDA reviewer`, `Information Request` 같은 표현을 여러 곳에서 강하게 사용합니다. 특히 §8 실패 모드에서는 λz 선택 오류가 FOCE local optimum, suboptimal NDA 제출, FDA reviewer 지적으로 이어지는 긴 나비효과를 제시합니다. 

교육적으로는 강하지만, 이 대부분은 교재 PDF 직접 근거가 아니라 **실무 추론**입니다. Scope Lock도 “규제 제출 파급력”은 말하지만, 개별 FDA reviewer 시나리오나 Clinical Hold를 원문 근거로 제시한 것은 아닙니다. 

**패치 권장:**
삭제할 필요는 없지만 `[실무 추론]` 또는 `[교육용 가상 시나리오]` 태그를 붙이세요. HTML에서는 “교재 사실”처럼 보이면 안 됩니다.

---

### 5. BA/BE 규제 프레임이 원문 범위보다 앞서갑니다

Draft는 “FDA 21 CFR 320 — NCA 기반 90% CI 동등성”을 후속 지식으로 넣었습니다.  BA/BE와 NCA 연결은 타당하지만, 이 세션의 PDF 자체가 규제문서가 아니라 교과서 범위이므로 **source 직접 근거와 외부 규제 지식이 섞이는 지점**입니다.

**패치 권장:**
`[후속 규제 연결]`로 표시하고, 본문 핵심 카드에서는 `AUC, Cmax, td가 노출 지표로 쓰인다` 정도로 제한하는 것이 안전합니다.

---

### 6. Completion block 기준으로 보면 §7은 양호하지만 약간 많습니다

Draft completion block은 §7이 9문항이고, Boss Dilemma를 포함한다고 정리합니다.  A-Critical 세션이라 9문항은 허용 가능한 범위입니다. 다만 HTML에서는 너무 시험지처럼 보이지 않도록 **Recall 3–4개 + Application 3–4개 + final dilemma 1개** 정도로 압축하는 것이 좋습니다.

---

## 권장 Audit Attention Memo

Phase 1 원본은 고치지 말고, 아래 메모를 Phase 2에 같이 붙이세요.

```markdown
# Audit Attention Memo — Session 06 Step 1 Draft v0

## 1. PK41 Turbojoint data anchor 반영 여부
Scope Lock은 PK41 Turbojoint® 실제 데이터를 반드시 인용하도록 지정함.
현재 draft는 PK41 수치를 “§6 시나리오 전용”으로 보존한다고 했으나,
Step 1 출력에는 §6이 없으므로 실제 data anchor가 약해질 수 있음.
Phase 2에서 누락 여부를 판정하고, Phase 4A에서 C4 또는 §8에 4–6줄 anchor box 삽입 권장.

## 2. R&T Table A-1 / A-2 구분 오류 가능성
Draft에서 “R&T Table A-1 zileuton”이라고 되어 있음.
R&T Table A-1은 oral 50 mg generic example, AUC=26.6 mg·hr/L.
Zileuton은 Table A-2로 분리해야 함.

## 3. AUMC 외삽 30–60% 수치 검증
Draft C2의 “AUMC 외삽이 전체의 30–60%” 표현은 PDF 직접 근거 확인 필요.
근거 없으면 “AUMC는 tail에 더 민감하다”로 완화.

## 4. Regulatory 표현 태그 분리
NDA Deficiency Letter, Clinical Hold, FDA reviewer, Information Request는
PDF 직접 근거가 아니라 실무 추론/교육용 시나리오일 가능성이 큼.
[실무 추론] 또는 [교육용 가상 시나리오]로 태그 분리.

## 5. BA/BE regulatory citation 범위 정리
FDA 21 CFR 320, 90% CI 등은 후속 규제 연결로는 유용하나,
교과서 source fidelity와 분리 필요.
본문에서는 “AUC/Cmax/td 노출 지표” 중심으로 유지.

## 6. §2.8.8 대안 공식 수식 확인
Eq.2:363–2:367, 특히 Eq.2:366과 Eq.2:367의 표기와 단위 검증 필요.
음수 Vss 방지 메시지는 유지하되 수식은 원문과 1:1 대조.

## 7. §7 Self-Test 압축 검토
현재 9문항은 허용 가능하나 HTML에서는 과밀할 수 있음.
Phase 4A에서 7–8문항 + final Socratic Dilemma 1개로 압축 검토.
```

---

## 최종 결론

이번 v0는 **좋은 Phase 1 초안**입니다.
특히 **Curation Map 4개 MUST, C3 Apex 설정, NCA는 compartment-free라는 핵심 프레임, §2.8.8 음수 Vss 위험 연결**은 잘됐습니다.

하지만 최적본은 아닙니다. 핵심 패치 대상은 다음 4개입니다.

1. **PK41 실제 수치 anchor가 약함**
2. **R&T Table A-1을 zileuton으로 부른 오류 가능성**
3. **AUMC 외삽 30–60% 같은 수치 근거 확인 필요**
4. **규제/실무 시나리오 표현이 교재 근거처럼 보이는 문제**

따라서 다음 단계는:

> **재작성 X → 원본 v0 보존 → Audit Attention Memo 첨부 → Phase 2 Source Fidelity Audit → Phase 4A에서 공식 패치 → Phase 4C → HTML Compile**

입니다.
**바로 HTML로 넘기기에는 아직 이릅니다.**

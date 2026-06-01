## 판정

**이번 Session 11 Phase 1 결과물은 상당히 잘 나온 고밀도 Draft v0입니다.**
하지만 **“최적으로 완료된 Step 1 확정본”은 아닙니다.** 현재 상태는 **Phase 2 Source Fidelity Audit으로 넘기기에 충분히 좋지만, HTML 직행은 금지**가 맞습니다.

| 항목                |         평가 |
| ----------------- | ---------: |
| Scope Lock 반영     | **8.5/10** |
| G&W + R&T 통합 구조   | **8.5/10** |
| Data anchoring 밀도 | **8.5/10** |
| Curation Map 적절성  | **7.5/10** |
| 수식·수치 안정성         | **7.0/10** |
| 출처 없는 규제/실무 해석 통제 | **5.5/10** |
| HTML 전환 준비도       | **아직 불충분** |

**최종 판정:**
`Phase 1 재실행 불필요 / Phase 2 필수 / HTML 직행 금지`

---

## 잘 된 부분

### 1. Stage 1 + Stage 2 통합 방향은 좋습니다.

Draft는 Gabrielsson을 **수식 도출, 4-model taxonomy, ODE 구조, PD4–PD9 case study** 담당으로 두고, R&T를 **hysteresis, PK vs PD rate-limiting, duration formula, target consumption** 담당으로 분리했습니다. 이 역할 분담은 이번 혼합 소스 세션의 목적에 잘 맞습니다. 

특히 R&T Ch.8의 핵심 목표가 **time delay, effect compartment, indirect response model, PK/PD rate-limited response, duration of effect**를 다루는 것이라는 점을 고려하면, Draft가 R&T를 단순 보충 자료가 아니라 **Card 8–9의 신규 축**으로 끌어올린 판단은 타당합니다. 

### 2. Data anchoring은 매우 풍부합니다.

Draft는 PD4, PD5, PD6, PD7, PD9뿐 아니라 digoxin, naproxen, warfarin, succinylcholine, minoxidil, aspirin, omeprazole, paclitaxel, methylprednisolone, rosuvastatin까지 실제 예시를 체계적으로 배치했습니다. 

특히 succinylcholine의 **dose doubling → duration +1 half-life** 메시지는 R&T 원문과 잘 맞습니다. R&T는 succinylcholine 0.5, 1, 2, 4 mg/kg i.v.에서 T50을 비교하며, dose를 두 배로 올릴 때 effect duration이 half-life만큼 증가한다고 설명합니다. 

### 3. “PK clock vs PD clock” 프레임은 교육적으로 강합니다.

Draft의 Big Idea는 **PK clock과 PD clock 중 느린 쪽이 임상 거동을 지배한다**는 구조로 세션 전체를 묶습니다. 이는 R&T의 “time must always be considered”라는 Ch.8 출발점과 잘 맞고, effect가 plasma concentration을 바로 따라가지 않는 이유를 임상적으로 설명하기 좋습니다. 

### 4. PD6의 “turnover vs effect compartment discrimination crisis”를 Apex로 잡은 것은 타당합니다.

G&W PD6에서는 turnover model과 effect compartment model이 같은 dose/time range에서 거의 같은 WRSS를 보이고, `kout`과 `ke0`가 동일하게 추정되는 상황을 제시합니다. 원문도 두 모델을 구분하려면 더 높은 dose, 반복 dose-response data, 또는 molecular mechanism 정보가 필요하다고 설명합니다. 

따라서 Card 7을 Apex로 둔 것은 충분히 방어 가능합니다.

---

## 반드시 고쳐야 할 부분

### 1. Naproxen 용량 표기가 문서 안에서 흔들립니다.

Draft 상단 data anchoring에는 **naproxen 500 mg oral**로 들어가 있는데, 후반 요약 쪽에서는 **naproxen 250 mg**처럼 보이는 부분이 있습니다.

R&T 원문은 **single 500-mg dose of naproxen** 후 dental pain model에서 counterclockwise hysteresis를 보인다고 설명합니다. 

수정:

```text
Naproxen: 500 mg oral, dental pain model, 1–8 h sampling, counterclockwise hysteresis.
```

**250 mg 표기는 삭제 또는 [확인 필요] 처리**해야 합니다.

---

### 2. “NDA/IND Deficiency Letter” 표현은 출처 기반이 아닙니다.

Draft는 여러 곳에서 “NDA/IND 문서 수준에서 방어”, “NDA Deficiency Letter의 흔한 사유”, “FDA Briefing Document 문구” 같은 표현을 사용합니다. 이 방향성은 실무적으로 유용하지만, 첨부된 G&W/R&T 원문이 직접 제공한 표현은 아닙니다.

수정 권장:

```text
[교과서 기반]
Turnover model과 effect compartment model은 특정 설계에서는 유사한 fit을 보일 수 있으며, 모델 구분에는 추가 dose range, repeated dosing, 또는 mechanistic information이 필요하다.

[교과서 외 실무 해석]
규제 제출 문서에서는 모델 선택 근거, sensitivity analysis, alternative model comparison을 명확히 제시해야 한다.
```

“Deficiency Letter”라는 단어는 남기더라도 반드시 **[교과서 외 실무 해석]**으로 라벨링해야 합니다.

---

### 3. MUST 카드 9개는 Phase 1로는 좋지만, Content Lock에서는 과밀합니다.

이번 Draft는 기존 7개 MUST에 R&T 기반 Card 8–9를 추가해 총 9개 카드가 되었습니다. 구조적으로는 이해되지만, HTML 학습 페이지로 만들면 너무 무거워질 가능성이 큽니다. 

권장 구조는 다음입니다.

```text
Content Lock 권장 구조:

Core Card 1. Turnover foundation + four-model taxonomy
Core Card 2. tss / peak-shift mechanism discrimination
Core Card 3. Graphical initial parameter estimation
Core Card 4. Irreversible action + target consumption
Core Card 5. Turnover vs effect compartment discrimination crisis
Core Card 6. PK vs PD rate-limiting + duration formula
```

즉, **Card 8과 Card 9는 합쳐도 됩니다.**
R&T 신규 기여의 핵심은 “rate-limiting 판별 후, tD formula 적용 가능성을 결정한다”이므로 한 카드로 묶는 편이 더 강합니다.

---

### 4. “모든 측정 가능한 약리반응은 시간 지연을 가진다”는 문장은 낮추는 것이 안전합니다.

G&W는 모든 response가 본질적으로 delayed nature를 가진다고 말하는 흐름이 있지만, R&T는 direct PK-PD link 또는 rapidly equilibrating response도 분명히 다룹니다. Draft의 Big Idea 문장은 교육적으로 강하지만, 그대로 두면 “direct response model을 부정하는가?”라는 오해가 생길 수 있습니다.

수정 권장:

```text
수정 전:
모든 측정 가능한 약리반응은 시간 지연을 가진다.

수정 후:
대부분의 임상적으로 관찰되는 약리반응은 plasma concentration과 완전히 동시에 움직이지 않으며, 그 지연이 무시 가능할 정도로 짧은 경우에만 direct response처럼 다룰 수 있다.
```

이렇게 바꾸면 G&W와 R&T를 모두 만족합니다.

---

### 5. tss 기반 mechanism discrimination은 강력하지만, 결정 규칙처럼 쓰면 안 됩니다.

Draft는 Models 1&3은 dose-independent tss, Models 2&4는 dose-dependent tss로 정리했습니다. 이 자체는 G&W Table 3.6/관련 설명과 잘 맞고, 매우 좋은 교육 포인트입니다.

다만 원문 PD9도 **peak shift가 없다고 해서 반드시 effect compartment model이라는 뜻은 아니다**라고 경고합니다. 

따라서 문장 수위를 다음처럼 조정해야 합니다.

```text
tss / peak-shift는 모델 선택의 강력한 진단 신호다.
하지만 최종 모델 선택은 PK rate-limiting 여부, dose range, nonlinear H(C), repeated dosing, mechanistic prior를 함께 고려해야 한다.
```

---

### 6. Card 6의 “K 표기 충돌”은 Phase 2에서 반드시 전수 확인해야 합니다.

Draft는 §3.8의 `K`가 bacterial kill 2차 상수와 PK elimination 1차 상수 모두에 사용된다고 보고 [확인 필요]로 표시했습니다. 이 처리는 좋습니다. 

다만 Phase 4에서 그대로 두면 학습자가 혼란스러울 수 있으므로, Content Lock에서는 표기를 분리하는 것이 좋습니다.

```text
권장 표기:
Kelim = PK elimination first-order rate constant
Kkill 또는 kk = second-order bacterial kill constant
```

원문 표기와 교육용 표기를 병기하면 됩니다.

---

### 7. R&T 사례 수치가 너무 많아 “핵심 구조”가 흐려질 위험이 있습니다.

Data anchoring은 강점이지만, 지금은 R&T 사례가 너무 많이 들어가서 Card별 우선순위가 흐려질 수 있습니다. 특히 rosuvastatin OATP1B1, methylprednisolone, paclitaxel, ranitidine까지 모두 본문 깊숙이 들어가면 Session 11의 핵심인 **turnover / indirect response / duration**이 약해질 수 있습니다.

정리 권장:

```text
MUST 유지:
- digoxin
- naproxen
- warfarin
- succinylcholine
- aspirin / omeprazole
- acenocoumarol vs phenprocoumon

CONTEXT 압축:
- ranitidine
- ibuprofen
- minoxidil
- paclitaxel
- methylprednisolone
- rosuvastatin OATP1B1
```

특히 rosuvastatin은 Draft도 CONTEXT 처리로 결정했으므로, 본문에서는 1–2문장 이상 확장하지 않는 편이 좋습니다. 

---

## 종합 판정

이번 Phase 1은 **실패가 아니라 매우 좋은 원석**입니다. 다만 지금 상태는 **“잘 통합된 대형 초안”**이지, **“학습용 HTML로 바로 변환 가능한 확정본”**은 아닙니다.

```text
GO: Phase 2 Source Fidelity Audit
NO-GO: HTML Compile
REDO: 불필요
MUST_FIX: 있음
```

## Phase 2에 추가할 감사 지시

아래 항목을 Source Fidelity Audit 프롬프트에 추가하는 것을 권장합니다.

```text
추가 감사 지시:

1. Naproxen 용량이 Draft 전체에서 500 mg으로 일관되는지 확인하라. 250 mg 표기가 있으면 ERROR로 분류하라.
2. NDA/IND/FDA Briefing Document/Deficiency Letter 관련 문장이 PDF source-supported인지, 교과서 외 실무 해석인지 분류하라.
3. “모든 반응은 delayed”라는 표현이 direct response/direct PK-PD link 사례와 충돌하지 않는지 확인하라.
4. tss / peak-shift 기반 모델 선택 설명이 deterministic rule처럼 과장되어 있지 않은지 확인하라.
5. PD4/PD5/PD6/PD7/PD9 수치와 R&T 사례 수치를 전수 대조하라.
6. Card 6의 K 표기 충돌을 확인하고, 교육용 표기 분리안(Kelim vs Kkill/kk)을 제안하라.
7. Card 8–9를 하나로 압축할 수 있는지 Content Lock 관점에서 평가하라.
8. R&T 사례 중 MUST와 CONTEXT가 적절히 분리되었는지 확인하라.
```

**한 줄 결론:**
이번 Phase 1은 **G&W의 turnover 수식축과 R&T의 rate-limiting/duration 임상축을 잘 결합한 고품질 Draft v0**입니다. 다만 **naproxen 용량 불일치, 규제 문장 과잉, 9개 카드 과밀, tss 진단 규칙의 과잉 단정**을 Phase 2–4에서 정리해야 최종 Step 1로 잠글 수 있습니다.

## 판정

**Phase 1 Draft v0로는 꽤 잘 뽑혔습니다. 하지만 “최적으로 완료된 Step 1 확정본”은 아닙니다.**
현재 상태는 **Phase 2 Source Fidelity Audit으로 넘기기에 충분히 좋은 고밀도 초안**이고, **HTML 직행은 금지**가 맞습니다.

| 항목               |         평가 |
| ---------------- | ---------: |
| Scope Lock 반영    | **8.5/10** |
| Curation Map 적절성 | **8.0/10** |
| G&W + R&T 통합 구조  | **8.0/10** |
| 수식·수치 안정성        | **7.0/10** |
| 출처 없는 실무해석 통제    | **6.0/10** |
| HTML 전환 준비도      | **아직 불충분** |

**최종 판정:**
`Phase 1 재실행 불필요 / Phase 2 필수 / HTML 직행 금지`

---

## 잘 된 부분

### 1. Curation Map의 5개 MUST 선정은 전반적으로 타당합니다.

이번 Scope Lock은 G&W Ch.3의 **질량작용법칙 → Emax/Sigmoid Emax → 비평형/AUEC** 흐름과 R&T Ch.8의 **시간 지연, hysteresis, effect compartment, indirect response, duration of effect**를 통합하도록 설계되어 있습니다. Draft가 C1–C5를 각각 **Mass Action, Sigmoid Emax/Hill, Hysteresis, Effect Compartment/Indirect Response, AUEC/Duration**으로 잡은 것은 큰 틀에서 적절합니다.  

특히 C2를 Apex로 둔 판단은 설득력이 있습니다. G&W는 Sigmoid Emax가 ordinary Emax에 `n`을 추가해 곡선의 steepness/curvature를 조절하는 일반화라고 설명하고, PD3에서는 실제 inhibitory Imax 모델의 model discrimination과 experimental design 문제가 직접 연결됩니다.  

### 2. G&W와 R&T의 역할 분담은 잘 작동했습니다.

G&W 쪽은 수식 도출과 PD3 실험 데이터 anchor를 담당하고, R&T 쪽은 시간 지연·hysteresis·effect compartment·indirect response의 임상 해석을 담당하도록 Scope Lock이 잡혀 있습니다. Draft도 대체로 이 역할 분담을 유지했습니다. 

R&T Ch.8의 핵심 메시지도 잘 반영되어 있습니다. 원문은 “실제로는 time을 항상 고려해야 한다”고 시작하며, digoxin 1 mg i.v. 후 혈장 농도는 떨어지는데 좌심실 박출 시간 지수는 4시간 동안 증가하는 예, naproxen 500 mg oral 후 counterclockwise hysteresis가 나타나는 예를 제시합니다. Draft의 C3–C4 흐름은 이 메시지를 잘 살렸습니다.  

### 3. PD3 수치 anchor는 강점입니다.

PD3의 그래픽 초기값과 최종 추정값을 잘 끌어왔습니다. 원문은 baseline 약 175 mmHg, Imax 약 35 mmHg, IC50 약 120 µg/L, n 약 2를 그래픽 초기 추정값으로 제시하고, 이후 sigmoid Imax 모델에서 `Imax=34.7`, `IC50≈140`, `n≈2.03`, `E0≈171` 계열의 추정값과 experimental error/VIF 분석을 제공합니다.   

---

## 반드시 고쳐야 할 부분

### 1. “5–100배 오차”는 출처 기반 문장이 아닙니다.

Draft의 Big Idea와 C1에는 **“FIH 용량이 5–100배 과추정될 수 있다”**, **“Phase 1 용량 예측에서 5–100배 오차”** 같은 표현이 들어갑니다.  

교과서가 직접 지지하는 것은 **Kd와 EC50가 달라질 수 있다**, **EC50가 Kd보다 훨씬 작을 수 있다**, **spare receptor/cascade 때문에 occupancy와 response가 일치하지 않을 수 있다**는 내용입니다. 하지만 “5–100배”, “FIH 용량”은 이 첨부 범위에서 직접 확인되는 수치가 아닙니다. 

수정 권장:

```text
[교과서 기반] Kd와 EC50는 동일하지 않을 수 있으며, spare receptor 또는 signal amplification 때문에 EC50가 Kd보다 작아질 수 있다.

[교과서 외 실무 해석] 이를 무시하고 in vitro Kd를 in vivo potency처럼 사용하면 FIH 용량 예측이 과대 또는 과소 추정될 수 있다.
```

---

### 2. Hill `n`의 생물학적 의미를 너무 강하게 단정했습니다.

Draft는 `n>1`을 cooperativity/cascade의 “직접 증거”처럼 설명하는 부분이 있습니다. 그러나 G&W 원문은 **Hill exponent `n`은 direct biological interpretation을 갖지 않으며, curve curvature를 설명하기 위한 flexibility parameter로 보아야 한다**고 명시합니다. 다만 `n<1`은 active metabolites 또는 multiple receptor sites를 시사할 수 있다고 설명합니다. 

따라서 Phase 4에서 문장을 낮춰야 합니다.

```text
수정 전:
n>1은 cascade가 작동 중이라는 직접적 증거.

수정 후:
n>1은 curve가 steep하다는 현상학적 신호이며, cooperativity·cascade amplification·system-level threshold 같은 가능성을 제시할 수 있지만, 단독으로 특정 기전을 증명하지는 않는다.
```

이건 중요한 수정입니다. 이대로 두면 교육적으로는 강렬하지만, source fidelity 기준에서는 과잉 해석입니다.

---

### 3. C4가 너무 많은 것을 한 카드에 담고 있습니다.

C4는 **Effect Compartment + Direct/Indirect link + indirect response 4표준형 + NONMEM `$DES` workflow**까지 한 번에 묶습니다. R&T Ch.8은 effect compartment로 naproxen hysteresis를 제거하는 개념과, systems in flux에서 input/output modulation의 네 가지 가능성을 설명합니다.  

하지만 Draft의 “Vol II의 kin/kout 표준 코드”, “NONMEM `$DES` 표준 워크플로”, “grid search로 식별성 확인”은 교과서 직접 내용이라기보다 **실무 구현 번역**입니다. 

수정 권장:

```text
[교과서 기반] R&T Ch.8은 time delay를 effect compartment 또는 systems-in-flux/indirect response 관점으로 설명한다.

[교과서 외 구현 번역] NONMEM에서는 이 구조가 effect compartment ODE 또는 kin/kout indirect response code로 구현된다.
```

가능하면 C4를 Phase 4에서 둘로 나누는 것도 좋습니다.

```text
C4a. Effect Compartment — distribution delay를 흡수
C4b. Indirect Response — system turnover가 response를 지배
```

단, 길이가 늘어나면 분리하지 말고 내부 소제목으로만 구분하세요.

---

### 4. Naproxen `ke0 ≈ 0.5–1 hr⁻¹`는 확인 필요입니다.

Draft의 Self-Test에는 “Naproxen의 추정된 `ke0` 값은 약 0.5–1 hr⁻¹ 범위”라는 문장이 있습니다. 

R&T 원문은 naproxen effect compartment를 사용하면 hysteresis가 제거되고 effect-site concentration과 response의 직접 관계가 드러난다고 설명하지만, 검색된 범위에서는 `ke0=0.5–1 hr⁻¹` 수치가 직접 확인되지 않습니다. 원문은 “distribution half-life가 minutes to hours 범위일 수 있다”고 설명합니다.  

수정 권장:

```text
Naproxen 예시에서 effect compartment를 적용하면 hysteresis가 제거된다.
[확인 필요] 구체적 ke0 수치는 원문 표/본문에서 재확인 필요.
```

---

### 5. Aspirin “75 mg, 7–10일, 수술 전 7일 중단”은 교과서 외 임상 지식입니다.

Draft는 aspirin 단회 75 mg 후 platelet thromboxane B2 inhibition이 7–10일 지속되고, 수술 전 7일 중단 권고를 언급합니다. 

Scope Lock이 지정한 R&T anchor는 **aspirin 650 mg PO, plasma t½ 15분, antiplatelet 효과가 며칠 지속**입니다. “75 mg”, “7–10일”, “perioperative bleeding”, “표준 권고 7일”은 교과서 범위 밖의 임상 확장입니다. 

수정 권장:

```text
[교과서 기반] Aspirin은 plasma half-life가 짧아도 platelet 관련 효과가 며칠 지속될 수 있다.

[교과서 외 임상 해석] 실제 수술 전 중단 시점은 적응증, 출혈위험, 혈전위험 및 최신 지침에 따라 별도 판단이 필요하다.
```

---

### 6. 마지막 “계속 → Step 2 HTML” 안내는 현재 워크플로우와 충돌합니다.

Draft 마지막에 “계속을 입력하면 Step 2 HTML 컴파일러가 실행됩니다”라고 되어 있습니다. 

하지만 현재 사용 중인 HTML 워크플로우는 **Phase 1 → Phase 2 Source Fidelity Audit → Phase 3 Insight Crucible → Phase 4 Content Lock → Phase 4C Visual Pedagogy → Phase 5 HTML Compile** 순서입니다. A-Critical에서는 Source Fidelity와 Visual Pedagogy를 유지해야 한다고 명시되어 있습니다. 

따라서 지금은 “계속”이 아니라 **Phase 2 감사 프롬프트**로 가야 합니다.

---

## 종합 판정

```text
GO: Phase 2 Source Fidelity Audit
NO-GO: HTML Compile
REDO: 불필요
MUST_FIX: 있음
```

이번 Phase 1은 **실패가 아니라 성공적인 Draft v0**입니다. 다만 “거장의 해석”이 강하게 들어가면서, 일부 문장이 **교과서 기반 사실**과 **실무적 확장 해석**을 섞고 있습니다. 이걸 Phase 2에서 분리하면 좋은 Content Lock으로 갈 수 있습니다.

## Phase 2에 추가할 감사 지시

아래 항목을 Phase 2 Source Fidelity Audit 프롬프트에 추가하는 것을 권장합니다.

```text
추가 감사 지시:

1. “5–100배 오차”, “FIH 용량 과추정”, “NDA 권장 용량” 표현이 PDF source에 직접 있는지 확인.
2. Hill coefficient n에 대한 설명이 G&W의 “no direct biological interpretation” 문장과 충돌하지 않는지 확인.
3. Naproxen effect compartment 관련 ke0 ≈ 0.5–1 hr⁻¹ 수치가 PDF에 직접 있는지 확인.
4. Aspirin 75 mg, 7–10일, 수술 전 7일 중단 권고가 PDF source-supported인지 확인.
5. NONMEM `$DES`, grid search, IIV on EC50/Emax/n 관련 문장이 원문 내용인지, 교과서 외 구현 번역인지 분류.
6. G&W pp.225–228 미포함 구간이 실제로 추정·보완 없이 [확인 필요]로만 처리되었는지 확인.
7. PD3 수치(E0, Imax, IC50, n), VIF, F-test, AIC, delta-function 관련 수치가 원문과 일치하는지 전수 대조.
```

**한 줄 결론:**
이번 Phase 1은 **최상급 원석에 가깝지만, 아직 최종본은 아닙니다.** Source Fidelity Audit으로 unsupported 수치와 과잉 해석만 걷어내면 충분히 좋은 Step 1 확정본으로 갈 수 있습니다.

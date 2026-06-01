## 판정

**이번 Phase 1은 구조적으로는 잘 뽑혔지만, “최적으로 완료된 Step 1 확정본”은 아닙니다.**
특히 이번 세션은 **Effect Compartment / Tolerance / Transduction**이 서로 비슷해 보이지만 모델 선택 결과가 완전히 달라지는 고위험 구간이라, **Phase 2 Source Fidelity Audit 없이 HTML로 직행하면 안 됩니다.**

| 항목               |         평가 |
| ---------------- | ---------: |
| Scope Lock 준수    | **8.5/10** |
| Curation Map 적절성 | **8.0/10** |
| 수식·ODE 전개        | **7.0/10** |
| 실제 데이터 anchor 반영 | **8.0/10** |
| 출처 없는 실무해석 통제    | **6.0/10** |
| HTML 전환 준비도      | **아직 불충분** |

**최종 판정:**
`Phase 1 재실행 불필요 / Phase 2 필수 / HTML 직행 금지`

---

## 잘 된 부분

### 1. Scope Lock의 큰 구조는 잘 반영했습니다.

Scope Lock은 이번 세션을 세 가지 시간 지연 해법으로 정의했습니다. 즉, **분포 지연 → Effect Compartment**, **체계 반응의 지연·적응 → Tolerance/Rebound/Feedback**, **수용체와 관찰 반응 사이의 연쇄 → Transduction**입니다. Draft도 이 구조를 거의 그대로 따라가고 있습니다. 

또한 §3.10 Dose-Response-Time Models, §3.12 Receptor occupancy theory, §3.14 Synergistic effects를 의도적으로 제외한 점은 좋습니다. Draft가 Scope 밖 내용을 마구 확장하지 않고, Curation Map에서 제외 항목을 명시한 것은 안정적인 작업입니다. 

### 2. Effect Compartment의 핵심 메시지는 잘 잡았습니다.

G&W 원문은 effect compartment model을 plasma와 biophase 농도를 1차 속도상수로 연결하는 hypothetical first-order distribution model로 설명하고, `Ce`는 직접 측정되는 값이 아니라 response-time course에서 간접 추정된다고 설명합니다. Draft도 이 부분을 잘 반영했습니다. 

특히 **linear PK에서 Link model은 dose가 증가해도 같은 `tmax`를 예측한다**는 점을 모델 선택의 진단 도구로 끌어낸 것은 매우 좋습니다. G&W도 이 성질이 link model과 turnover-driven response model을 구별하는 유용한 도구라고 명시합니다. 

### 3. PD35 Transduction anchor도 잘 들어갔습니다.

PD35는 23세 남성 volunteer의 세 dose 조건에서 concentration-time과 response-time data를 동시에 모델링한 사례이고, 낮은 dose의 `C0=1.05 nmol/L`, `K=0.0228 h⁻¹`, t½ 약 30 h, 4배·16배 dose escalation이 제시됩니다. Draft가 이를 Transduction 카드의 중심 anchor로 사용한 것은 적절합니다. 

또 Table 35.1의 WRSS 비교도 잘 반영했습니다. 실제로 transduction step 1, 2, 3, 4, 5에서 WRSS가 각각 1319, 789, 642, 632, 682로 제시되므로, n=3과 n=4의 차이는 작고 n=5는 악화됩니다. Draft가 “n=3을 practical/parsimony 관점에서 채택”한 것은 타당합니다. 

---

## 반드시 고쳐야 할 문제

### 1. 가장 큰 오류: Table 3.10 pitfall을 PD13이라고 부르는 것은 부정확합니다.

Draft는 “PD13처럼 Link 모델을 turnover 데이터에 잘못 적용 → EC50가 0.681, 4.85, 0.941로 분기”라고 반복합니다. 그러나 이 수치는 **G&W §3.9.7 Problems and pitfalls의 Table 3.10**에서 나온 값입니다. 해당 원문은 turnover model로 생성한 세 dose dataset을 effect compartment model로 fit했을 때 implausible EC50가 나온다고 설명하며, Figure 3.59는 Case Study **PD12** data라고 적습니다. 

반면 **PD13은 repeated intravenous infusions에서 tolerance/rebound 모델을 비교하는 case study**입니다. PD13은 Model I, Model II, Model III를 비교하고, negative feedback Model II가 좋은 fit을 보이는 tolerance/rebound 사례입니다. 

수정해야 할 문장 구조는 다음입니다.

```text
수정 전:
PD13처럼 Link 모델을 turnover 데이터에 잘못 적용하면 EC50가 dose별로 0.681, 4.85, 0.941로 분기된다.

수정 후:
G&W §3.9.7 Table 3.10의 link-model pitfall 예시처럼, turnover-driven response data를 effect compartment model로 잘못 fit하면 dose별 EC50가 0.681, 4.85, 0.941로 비현실적으로 분기될 수 있다.
PD13은 별도로 tolerance/rebound에서 negative feedback Model II의 우수성을 보여주는 case study이다.
```

이건 **MUST_FIX 1순위**입니다. 용어 하나의 문제가 아니라, case study label이 틀리면 학습자가 PD13의 역할을 잘못 기억하게 됩니다.

---

### 2. `k1e = ke0`를 “물리적 정합성 때문에 강제”라고 설명한 것은 과도합니다.

Draft는 `k1e = ke0` 가정에 대해 “identifiability 때문이 아니라 물리적 정합성 때문에 강제됨”이라고 설명합니다. 하지만 G&W 원문은 **동시에 여러 rate constants를 추정하기 어려운 identifiability problem 때문에 `k1e = ke0`로 둔다**고 설명하고, partitioning이 있으면 `Ce`와 `C`가 steady state에서도 다를 수 있다고 분명히 말합니다. 

따라서 다음처럼 고쳐야 합니다.

```text
수정 전:
k1e = ke0는 물리적 정합성 때문에 강제된다.

수정 후:
k1e와 ke0는 response-time data만으로 동시에 안정적으로 식별하기 어렵기 때문에, 표준 effect compartment model에서는 보통 k1e = ke0 또는 Kp 관련 단순화를 둔다. 이는 식별가능성과 모델 단순화를 위한 가정이지, 모든 생리학적 상황에서 물리적으로 반드시 참인 등식은 아니다.
```

이 부분은 **수식 신뢰도에 직접 영향을 주는 오류**입니다.

---

### 3. Succinylcholine과 d-tubocurarine 수치가 섞였습니다.

Draft의 Big Idea에는 **succinylcholine 추가 투여 시점에서 `t½,ke0 = 4 min`**이라고 표현되어 있습니다. 그런데 Scope Lock의 실제 anchor는 다릅니다.

* G&W Table 3.9: `d-tubocurarine`의 `t½,ke0 = 4 min`
* R&T: `succinylcholine 0.5 mg/kg i.v.`, `T50 ≈ 6 min`, `k ≈ 0.2 min⁻¹`, 80→20% response decline이 약 22%/min 

따라서 이렇게 분리해야 합니다.

```text
d-tubocurarine: G&W Table 3.9의 effect compartment 예시, t½,ke0 = 4 min.
succinylcholine: R&T Ch.8의 neuromuscular blockade duration 예시, T50 ≈ 6 min 및 response decline 설명.
```

현재처럼 쓰면 독자가 **succinylcholine의 ke0가 4분이라고 오해**할 수 있습니다.

---

### 4. “Hysteresis 방향이 모델 선택을 결정한다”는 표현은 조금 강합니다.

Draft는 “방향 자체가 모델 선택을 결정”한다고 쓰고 있습니다. 교육적으로 강력한 문장이지만, 실제로는 **방향은 중요한 진단 단서이지, 단독 결정 규칙은 아닙니다.**

R&T는 digoxin, naproxen 사례를 통해 response가 plasma concentration을 따라가지 않을 때 hysteresis가 시간 지연 진단에 유용하다고 설명합니다. Naproxen 500 mg oral 예시는 counterclockwise hysteresis이며, distribution delay를 effect compartment로 보정하면 underlying concentration-response relationship을 드러낼 수 있다고 설명합니다.  

하지만 같은 counterclockwise hysteresis라도 원인은 distribution delay, indirect response, slow receptor binding, active metabolite 등일 수 있습니다. G&W도 시간 지연 원인으로 tissue distribution, active metabolites, arteriovenous differences, receptor upregulation, slow ligand-receptor on/off 등을 나열합니다. 

수정 권장:

```text
수정 전:
hysteresis 방향 자체가 모델 선택을 결정한다.

수정 후:
hysteresis 방향은 모델 선택의 첫 번째 진단 단서다. 다만 최종 선택은 dose별 tmax shift, rising/falling limb data, mechanism 정보, repeated-dose/tolerance pattern, model comparison을 함께 보고 결정한다.
```

---

### 5. “NDA Deficiency Letter”는 교과서 기반 사실이 아니라 실무 해석입니다.

Scope Lock에는 모델 선택 오류가 NDA/IND Deficiency Letter 위험과 연결될 수 있다고 적혀 있고, Draft도 “NDA 제출장”, “Critical Blow — NDA Deficiency Letter” 같은 표현을 사용합니다.  

이 방향성은 실무적으로는 타당하지만, G&W/R&T 원문이 직접 “NDA Deficiency Letter”라고 말하는 것은 아닙니다. 따라서 Content Lock에서는 다음처럼 라벨링해야 합니다.

```text
[교과서 기반]
잘못된 link model 적용은 dose별 EC50 분기와 systematic deviation을 만들 수 있다.

[교과서 외 실무 해석]
이런 모델을 규제 제출용 exposure-response 근거로 사용하면, reviewer가 model misspecification, mechanism justification, sensitivity analysis를 요구할 수 있다.
```

“Deficiency Letter”라는 표현을 남기고 싶다면, 반드시 **교과서 외 실무 해석**으로 분리해야 합니다.

---

### 6. Transduction 카드의 공학·수학 analogies는 유용하지만 Source Fidelity에서는 NOT_IN_SOURCE입니다.

Draft의 Transduction 카드에는 transfer function, gamma PDF, Bode plot, PFR tanks-in-series, RC delay line, Erlang distribution, NONMEM do-loop 등이 들어갑니다. 

이것들은 학습 효과는 좋지만, G&W 원문이 직접 제시한 내용은 아닙니다. 원문은 receptor-ligand coupling과 observed response 사이를 chain of events/compartments로 생각할 수 있고, rate constant가 `1/τ = kout`로 근사될 수 있다고 설명합니다. 

따라서 Phase 4에서 이렇게 라벨링하면 됩니다.

```text
[구조적 비유 — 교과서 외 확장]
Transfer function / Erlang / tanks-in-series / RC delay line은 transduction chain의 수학적 동형성을 설명하기 위한 외부 비유이다. 원문 직접 표현은 아니다.
```

삭제할 필요는 없지만, **출처 기반 본문과 외부 비유를 구분**해야 합니다.

---

## 종합 평가

이번 Phase 1은 **실패작이 아니라 꽤 좋은 Draft v0**입니다. 특히 Curation Map, source split, §3.10 제외, PD20/PD21/PD35 anchor 반영은 좋습니다. 그러나 다음 오류들은 Phase 2에서 반드시 잡아야 합니다.

```text
MUST_FIX

1. Table 3.10 link-model pitfall을 PD13이라고 부르는 오류 수정.
2. k1e = ke0를 “물리적 필연”이 아니라 “식별가능성/단순화 가정”으로 수정.
3. succinylcholine T50 예시와 d-tubocurarine t½,ke0=4 min 예시 분리.
4. hysteresis 방향 = 모델 결정이라는 표현을 “진단 단서”로 낮추기.
5. NDA Deficiency Letter / regulatory blow 표현을 [교과서 외 실무 해석]으로 라벨링.
6. transfer function, Bode plot, Erlang, NONMEM do-loop 등은 [교과서 외 구조적 비유/구현 번역]으로 라벨링.
```

## 다음 단계 권장

**Phase 1 재실행은 하지 마세요.**
이 정도면 원석은 충분히 좋습니다. 바로 Phase 2로 넘기되, 감사 프롬프트에 아래 문장을 추가하는 것이 좋습니다.

```text
추가 감사 지시:

1. Draft에서 “PD13”으로 지칭한 EC50 dose-dependence 사례가 실제로 PD13인지, G&W §3.9.7 Table 3.10 / PD12 관련 사례인지 확인하라.
2. k1e = ke0 가정 설명이 G&W p.263–265의 identifiability 설명과 일치하는지 확인하라.
3. succinylcholine, d-tubocurarine, Table 3.9의 t½,ke0 수치가 서로 섞이지 않았는지 확인하라.
4. hysteresis 방향과 모델 선택의 관계가 deterministic rule처럼 과장되어 있지 않은지 확인하라.
5. NDA Deficiency Letter, Critical Blow, regulatory 제출 관련 표현이 source-supported인지 또는 교과서 외 실무 해석인지 분류하라.
6. Transduction 카드의 Bode plot, Erlang, tanks-in-series, NONMEM do-loop가 원문 직접 내용인지 외부 비유/구현 번역인지 분류하라.
7. PD20, PD21, PD35의 실제 수치와 Table 35.1 WRSS가 원문과 일치하는지 전수 대조하라.
```

**한 줄 결론:**
이번 Phase 1은 **구조 설계는 좋지만, case label 오류와 일부 과잉 해석이 남아 있는 고품질 초안**입니다. Phase 2에서 위 6개만 잡으면 충분히 좋은 Content Lock으로 갈 수 있습니다.

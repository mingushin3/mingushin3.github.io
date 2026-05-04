## 판정

**이번 Session 016 Phase 1은 “매우 야심차고 잘 통합된 Draft v0”입니다. 그러나 최적으로 완료된 Step 1 확정본은 아닙니다.**
특히 이번 세션은 단일 챕터 요약이 아니라 **Ch.6 Pattern Recognition → Ch.15 Disease → PK35 Bayesian TDM → Ch.18 Initiating Therapy → PK15 Toxicokinetics**를 한 임상 의사결정 사슬로 묶는 캡스톤이라, 지금 상태 그대로 HTML로 넘기면 과밀도와 출처 외 실무 확장이 같이 전파될 위험이 큽니다. Draft 자체도 Stage 1–3 누적 통합본이며, Ch.6, Ch.15, Ch.18, PK35, PK15를 한 흐름으로 연결했다고 명시하고 있습니다. 

| 항목                         |         평가 |
| -------------------------- | ---------: |
| Scope Lock 반영              | **8.5/10** |
| 캡스톤 통합 구조                  | **8.5/10** |
| Ch.6 패턴 인식 축               | **8.0/10** |
| PK35 Bayesian TDM 축        | **8.5/10** |
| Ch.15 질환/Rd/투석 축           | **8.0/10** |
| Ch.18 TCS/LD/missed dose 축 | **8.0/10** |
| 출처 외 실무·규제 문장 통제           | **5.5/10** |
| HTML 직행 가능성                |     **불가** |

**최종 판정:**
`Phase 1 재실행 불필요 / Phase 2 Source Fidelity Audit 필수 / HTML 직행 금지`

현재 워크플로우 자체도 Phase 1 이후 곧바로 HTML이 아니라 **Phase 2 Source Fidelity Audit → Phase 3 Insight Crucible → Phase 4 Content Lock → Phase 4C Visual Pedagogy → Phase 5 HTML Compile** 순서로 설계되어 있습니다. 

---

## 잘 된 부분

### 1. “모델 → 환자 → 추정 → 처방”의 캡스톤 spine은 좋습니다.

Draft의 최종 내러티브는 **Ch.6 Pattern Recognition으로 PD 모델 구조를 선택하고, Ch.15 Disease로 환자가 모집단에서 벗어나는 이유를 설명하고, PK35 Bayesian으로 개인 파라미터를 추정한 뒤, Ch.18로 실제 용량 처방에 연결**하는 구조입니다. 이 사슬은 이번 세션의 목적에 잘 맞습니다. 

특히 PK35를 “Bayesian Objective Function” 카드로 둔 것은 타당합니다. 원문 PK35는 Bayesian objective function을 최소화해 개인별 clearance와 volume을 추정하며, 농도 관측값, population parameter, 측정오차, population variability를 함께 사용한다고 설명합니다. 또 no concentration, no prior, full Bayesian의 세 가지 극단을 구분합니다. 

### 2. 실제 데이터 anchor는 강합니다.

PK35 digoxin 사례의 핵심 수치, 즉 **55세 60 kg 남성 CHF 환자, Lanoxicap 0.2 mg, digoxin 2.5 µg/L at 458 h, 0.9 µg/L at 479 h, population CL 1.8 L/h, V 500 L, 최종 추정 CL 5.7 L/h, V 119.6 L, t½ 14.5 h**가 잘 반영되어 있습니다. Scope Lock도 이 수치들을 그대로 인용하라고 명시했습니다.

Ch.18의 missed dose framework도 잘 잡았습니다. 원문은 missed dose 보정이 superposition/additivity 원리에 기반하며, 정상상태 예상 농도에서 missed dose가 남겼을 농도 기여분을 빼는 방식으로 Eq.18-1과 Eq.18-2를 제시합니다. Draft가 §2.12를 독립 MUST로 둔 것은 임상 TDM 관점에서 타당합니다.

### 3. Ch.6 Pattern Recognition의 핵심 질문도 잘 살렸습니다.

G&W Ch.6은 response-time profile을 볼 때 **baseline, time delay, peak shift, saturation, slope**를 확인하라고 제시하고, pattern recognition이 kinetic/dynamic data modeling의 핵심 활동이라고 설명합니다. Draft의 §2.1–§2.5는 이 메시지를 잘 반영했습니다. 

특히 Case A–C에서 **peak-shift 방향과 saturation 유무로 turnover, effect compartment, receptor on/off 모델을 분기**하는 흐름은 원문 Fig.6.2–6.3의 논리와 잘 맞습니다. G&W도 Case B의 leftward shift, Case C의 rightward shift와 high dose flat portion을 모델 구분 신호로 설명합니다. 

---

## 반드시 고쳐야 할 부분

### 1. MUST 카드 12개는 HTML 학습문서로는 과밀합니다.

이번 Draft는 최종 MUST가 12개입니다. 캡스톤이라 넓은 것은 이해되지만, HTML 학습 페이지로는 너무 무겁습니다. **Phase 1 원석으로는 좋지만, Phase 4 Content Lock에서는 7–8개 정도로 압축하는 것이 좋습니다.**

권장 압축 구조:

```text
Core 1. Pattern Recognition Decision Tree
Core 2. Peak-shift Directionality + Saturation
Core 3. Effect Compartment vs Turnover vs Receptor On/Off
Core 4. Bayesian Objective Function for TDM
Core 5. Disease/Rd/Cockcroft-Gault/Dialysis Adjustment
Core 6. TCS Criteria
Core 7. Loading Dose vs Maintenance Dose
Core 8. Missed/Erratic Dosing Superposition
```

특히 **2.7 Rd Framework, 2.8 Cockcroft-Gault, 2.9 Hemodialysis**는 하나의 “Disease-adjusted dosing” 카드로 합치는 편이 HTML 가독성에 좋습니다.

---

### 2. “Peak-shift 방향 = 모델 클래스”는 너무 결정론적으로 쓰면 안 됩니다.

Draft는 Peak-shift Directionality를 Apex #1로 두고 “좌/우 방향이 곧 모델 클래스”라고 강하게 표현합니다. 방향성은 강력한 진단 신호가 맞지만, 원문 Ch.6은 여러 alternative solution을 함께 제시하고, pattern recognition을 통해 “potential models”를 평가하라고 합니다. 즉, 방향은 **결정 규칙**이 아니라 **모델 후보를 줄이는 1차 필터**입니다. 

수정 권장:

```text
수정 전:
좌/우 peak-shift 방향이 곧 모델 클래스다.

수정 후:
좌/우 peak-shift 방향은 모델 클래스 후보를 강하게 좁히는 1차 진단 신호다. 최종 선택은 saturation, dose range, concentration-response loop, mechanism prior, 추가 설계 자료와 함께 판단해야 한다.
```

---

### 3. TCS의 “5개 criterion 모두 충족 → 필수 적용” 표현은 낮춰야 합니다.

Draft는 TCS를 “5개 criteria 모두 충족 시 적용”으로 잘 구조화했지만, 일부 문장에서 **digoxin, vancomycin, cyclosporine, phenytoin, theophylline, nortriptyline = TCS 필수**처럼 단정합니다.

R&T Ch.18의 목적은 “어떤 low therapeutic index drug에서는 plasma concentration monitoring이 유용하고, 어떤 경우에는 그렇지 않은지”를 설명하는 것입니다. 즉, TCS는 단순히 약물명만으로 자동 적용되는 것이 아니라 **concentration-response 관계, PK/PD variability 구조, population PK 정보, assay reliability, 임상 의사결정 시점**을 함께 봐야 합니다. 

수정 권장:

```text
수정 전:
Phenytoin·digoxin·vancomycin·cyclosporine·theophylline·nortriptyline = TCS 필수.

수정 후:
이 약물들은 TCS가 자주 유용한 대표 후보군이다. 다만 실제 적용 여부는 환자 상태, sampling timing, assay turnaround, active metabolite/free concentration 이슈, 임상 의사결정 필요성에 따라 달라진다.
```

---

### 4. Loading dose 카드의 “V 5–10%, CL 30–40%” 수치는 Phase 2에서 반드시 확인해야 합니다.

Draft는 Loading Dose 카드에서 **V는 covariate로 5–10% 정확도, CL은 30–40%**라고 제시합니다. 
이 문장은 매우 유용하지만, 정확한 수치가 R&T Ch.18의 Fig.18-5 또는 관련 표에서 직접 나온 것인지 Phase 2에서 확인해야 합니다. 출처 직접 근거가 없으면 다음처럼 낮춰야 합니다.

```text
수정 후:
Loading dose는 주로 V에 의존하고, maintenance dose는 주로 CL에 의존한다. V와 CL의 예측 가능성은 약물과 covariate 구조에 따라 다르며, R&T Fig.18-5의 맥락에서 구체적으로 해석해야 한다.
```

또 `D_L = V·C_target/F` 자체는 맞지만, 실제 임상에서는 분포 속도, 투여 속도, 제형, dose strength, 독성 위험 때문에 분할 loading이 필요할 수 있습니다. Ch.18 objective도 “왜 여러 sequential doses가 loading dose로 쓰이는가”를 별도 목표로 둡니다. 

---

### 5. Q8의 digoxin 처방 권고는 source-supported 사실이 아니라 “통합 추론 예시”입니다.

Draft 후반에는 55세 CHF digoxin 환자에 대해 **loading dose 0.4 mg 분할, maintenance 0.1–0.125 mg/day, NDA Briefing Document 문구**까지 제시합니다. 

문제는 PK35 원문은 Bayesian model로 개인 CL/V를 추정하는 사례이지, 해당 환자에게 이런 loading/maintenance regimen을 처방하라고 제시한 것은 아닙니다. 원문은 CL=5.7 L/h, V=119.6 L, t½=14.5 h를 추정하고, V가 population average에서 크게 벗어난 이유로 low body weight 가능성을 언급합니다. 

따라서 이 부분은 반드시 다음처럼 라벨링해야 합니다.

```text
[교과서 기반]
PK35는 두 농도값과 population prior를 이용해 이 환자의 CL, V, t½를 추정한다.

[교과서 외 통합 추론 예시]
아래 loading/maintenance dose 제안은 PK35 + R&T Ch.15 + Ch.18 원리를 결합한 교육용 clinical reasoning exercise이며, 원문에 수록된 직접 처방 권고가 아니다.
```

특히 “NDA Briefing Document 언어”는 교과서 직접 내용이 아니므로 삭제하거나 `[교과서 외 실무 번역]`으로 분리해야 합니다.

---

### 6. “TDM 환자의 80%” 같은 수치는 삭제해야 합니다.

§2.12에는 “TDM 환자의 80%가 완벽한 정상상태 fixed-interval regimen이 아니다”라는 취지의 문장이 있습니다. 
방향성은 맞지만, **80%라는 수치가 R&T 원문에서 직접 확인되지 않으면 NOT_IN_SOURCE**입니다.

수정 권장:

```text
수정 전:
TDM 환자의 80%가 완벽한 정상상태 fixed-interval regimen이 아니다.

수정 후:
실제 TDM에서는 missed dose, unequal interval, erratic dosing이 흔해, 완전한 정상상태 fixed-interval 가정만으로는 측정 농도를 해석하기 어렵다.
```

---

### 7. NONMEM, BestDose, ID-ODS, Pmetrics, NDA/IND/RMP 문장은 “교과서 외 구현 번역”으로 분리해야 합니다.

Draft는 후속 영역으로 **NONMEM $DES, BestDose, ID-ODS, Pmetrics, NDA/IND PK/PD section, Phase 4 RMP** 등을 다수 언급합니다.

이 연결은 교육적으로 유용하지만, 이번 첨부 source의 직접 내용은 G&W/R&T textbook입니다. 따라서 원문 기반 본문과 현대 구현/규제 번역을 명확히 분리해야 합니다.

```text
[교과서 외 구현 번역]
NONMEM $DES, BestDose, ID-ODS, Pmetrics, NDA/IND/RMP 언어는 본 세션의 원리를 현대 PopPK/TDM/규제 workflow로 옮긴 예시다. 원문 교과서에 직접 제시된 software 또는 regulatory template은 아니다.
```

이 라벨링 없이 두면 Source Fidelity Audit에서 대량의 NOT_IN_SOURCE가 발생할 가능성이 높습니다.

---

### 8. PK15가 §2 카드에서 빠진 것은 이해되지만, §8 또는 §6에서 최소 anchor는 더 명확해야 합니다.

Scope Lock은 PK15를 B-Standard 가중으로 처리하고, **10/56/320 µmol·day⁻¹·kg⁻¹, Cmax/AUC 선형성, 치료 농도 0.05–0.1 µM, Cmax 약 50 µM, >100배 안전역**을 그대로 인용하라고 했습니다. 

Draft는 PK15를 §2 카드로 만들지 않고, data anchoring과 Step 2 §6 예약으로 처리했습니다. 이것은 캡스톤 과밀도를 줄이는 면에서는 타당합니다. 다만 최종 HTML에서는 **“모델/추정/질환/처방 → 노출 보고”로 닫히는 마지막 bridge**가 약해지면 캡스톤 완결성이 떨어집니다. 

권장:

```text
§8 또는 §6에 mini-closing block 추가:
PK15는 처방 자체가 아니라 “선택된 용량에서 어떤 exposure와 safety margin을 보고할 것인가”를 담당한다.
```

---

## 종합 판정

```text
GO: Phase 2 Source Fidelity Audit
NO-GO: HTML Compile
REDO: 불필요
MUST_FIX: 있음
```

이번 Phase 1은 **캡스톤 통합 원석으로는 성공**입니다. 다만 다음 7개는 Phase 2–4에서 반드시 잡아야 합니다.

```text
MUST_FIX

1. 12개 MUST 카드를 7–8개 core card로 압축.
2. Peak-shift directionality를 “결정 규칙”이 아니라 “1차 진단 신호”로 낮추기.
3. TCS “필수 적용” 표현을 “적용 후보/조건부 유용성”으로 수정.
4. Loading dose 카드의 V 5–10%, CL 30–40% 수치 source 확인.
5. PK35 digoxin 처방 권고/Q8 NDA 문구를 [교과서 외 통합 추론 예시]로 라벨링.
6. “TDM 환자 80%” 등 출처 없는 수치 삭제.
7. NONMEM/BestDose/ID-ODS/Pmetrics/NDA/IND/RMP 문장을 [교과서 외 구현·규제 번역]으로 분리.
```

## Phase 2에 추가할 감사 지시

```text
추가 감사 지시:

1. Ch.6 peak-shift 방향성 설명이 원문처럼 “potential models 평가”인지, Draft처럼 deterministic rule로 과장되었는지 확인하라.

2. TCS 5 criteria, Table 18-2/18-5/18-6의 약물 예시가 Draft와 일치하는지 확인하라. 특히 “TCS 필수” 표현이 원문보다 강한지 평가하라.

3. Loading dose 카드의 “V 5–10%, CL 30–40%” 및 “V 90%, CL 40% 설명” 수치가 R&T Fig.18-5 또는 본문에서 직접 확인되는지 대조하라.

4. PK35 digoxin 사례에서 원문이 제시한 것은 CL/V/t½ 추정인지, Draft의 loading/maintenance dose recommendation까지 포함하는지 구분하라.

5. Missed dose, two missed doses, 9-13-17-21, erratic dosing의 Eq.18-1~18-4 및 worked examples: digoxin 0.39 µg/L, vancomycin 2.03 mg/L, erratic 34 vs 33.7 mg/L를 전수 대조하라.

6. “TDM 환자의 80%”, “Deficiency Letter”, “NDA Briefing Document”, “Phase 4 RMP”, “BestDose/ID-ODS/Pmetrics”가 PDF source-supported인지, 교과서 외 실무 번역인지 분류하라.

7. PK15 safety margin 수치가 최종 §6 또는 §8에서 충분히 연결되는지 확인하라.
```

**한 줄 결론:**
이번 Phase 1은 **Session 016 캡스톤의 통합 방향은 매우 좋지만, 카드 수가 과밀하고 실무·규제 번역이 source-supported 본문과 섞인 상태**입니다. Phase 2에서 unsupported 수치와 과잉 단정을 걷어내고, Phase 4에서 7–8개 core card로 압축하면 좋은 Step 1 확정본으로 갈 수 있습니다.

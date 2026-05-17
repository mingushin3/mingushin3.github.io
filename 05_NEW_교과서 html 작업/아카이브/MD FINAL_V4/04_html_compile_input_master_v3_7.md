# 04_HTML Compile Input Master — v3.7

<!-- 기호 통일: Vmax → V_{max} (첫 등장 M6 기준) -->
<!-- 기호 통일: Km → K_m (첫 등장 M6 기준) -->
<!-- 기호 통일: CLint → CL_{int} (첫 등장 §1/M4 기준) -->

## PART A — 학습자용 완성 핸드아웃(Learner-Facing Complete Handout)

> **임상 장면**  
> 간 혈류 $Q_H=81\ \mathrm{L/h}$인 성인에서 plasma $CL=60\ \mathrm{L/h}$만 보고 “중등도 이상 hepatic extraction”이라고 판단했다고 가정합니다 [T5 p.125]. 그런데 $C/C_b=0.5$이면 blood 기준 $CL_b$는 30 L/h가 되고, $E_H$는 0.37로 내려갑니다. 이 한 번의 기준 선택 오류가 DDI 해석, 간장애 라벨, PBPK 입력값 전체를 바꿉니다.

## 학습자 네비게이션 안내(Learner Navigation Aid)

**이 자료의 활용법**: PART A를 네 번에 나눠 읽으세요. 먼저 §1에서 이 장의 핵심 질문을 확인하고, §2 M1–M14를 개념 카드로 순서대로 읽으세요. 이어서 §5에서 혼동되기 쉬운 개념 쌍을 분리하고, §7 Self-Test에 먼저 답한 뒤 §8을 검토하세요.

**학습 경로**: `M1 clearance 정의 → M2–M3 신장 측정 → M4–M6 간 clearance / extraction / IVIVE → M7 구현 연결 → M8–M10 blood 기반 · extended clearance → M11–M14 대사체 · 신부전 결정`.

**그림 활용 원칙**: image rights가 `None`으로 고정되어 있으므로, 교과서 원본 그림은 이 파일에 재현하지 않습니다. Figure pointer는 학습자가 교과서 원본을 직접 열어서 확인하도록 안내합니다.

<!-- SLIDE_START: §1 | title: §1 이 장이 중요한 이유(Why This Chapter Matters) -->

## §1 이 장이 중요한 이유(Why This Chapter Matters)

### v3.7 레이어 개념 지도

```text
레이어 1 — 무엇인가
  CL / CL_R / CL_H / CL_b / f_e / f_u / f_{ub} / f_m / CL(m)
        ↓
레이어 2 — 어떻게 계산되는가
  Rate = CL·C → 장기별 CL 분해 → well-stirred → ρ/extended clearance → AUC(m)/AUC
        ↓
레이어 3 — 언제, 왜 중요한가
  신장애·간장애·DDI·first-pass·active metabolite·NONMEM covariate 위치·label defense
```

### 지식 그래프 위치

```text
[선행 세션: 선형 1구획 PK·AUC·mass balance]
      → [이 세션: clearance의 생리학적 분해]
      → [후속 세션: PBPK·PopPK covariate·parent–metabolite joint model·impairment label]
```

🧭 **읽는 순서:**  
카드 1 (M1): 왜 $t_{1/2}$가 원인이 아니라 $CL$과 $V$의 결과인가?  
카드 2 (M2): total $CL$ 중 신장 경로만 어떻게 떼어내는가?  
카드 3 (M3): 같은 소변 데이터에서 왜 ARE와 rate plot이 다른 약점을 보이는가?  
카드 4 (M4): 간 $CL$은 $Q_H$와 $f_{ub}CL_{int}$ 중 무엇에 막히는가?  
카드 5 (M5): 단백결합 변화는 왜 IV/oral·high/low extraction에 따라 뒤집히는가?  
카드 6 (M6): IVIVE 실패는 모델식 때문인가, 입력 데이터 압축 때문인가?  
카드 7 (M7): plasma와 urine을 왜 동시에 fitting해야 하는가?  
카드 8 (M8): plasma $CL$을 왜 blood $CL_b$로 바꿔야 하는가?  
카드 9 (M9): $CL_{int}$가 충분해도 왜 hepatocyte 접근성이 병목이 되는가?  
카드 10 (M10): transporter–enzyme architecture는 well-stirred를 어떻게 확장하는가?  
카드 11 (M11): metabolite terminal slope는 누구의 half-life인가?  
카드 12 (M12): $AUC(m)/AUC$는 왜 $f_m$ 하나로 읽을 수 없는가?  
카드 13 (M13): oral first-pass metabolite는 어떻게 정상상태 위험으로 이어지는가?  
카드 14 (M14): 작은 $f_m$이 왜 신장애에서 가장 큰 안전성 문제가 되는가?

**핵심 아이디어(Big Idea)**: 청소율(CL, clearance; 농도 대비 제거능)은 $Dose/AUC$로 끝나는 숫자가 아닙니다. **혈류($Q$), 단백결합($f_u$, $f_{ub}$), 내인성 청소율(intrinsic clearance) $CL_{int}$, 투과성/수송체(permeability/transporter), 신장 여과/분비/재흡수(renal filtration/secretion/reabsorption), 대사체 형성/제거(metabolite formation/elimination)**가 한 식 안에서 충돌한 결과입니다. 이 장의 목표는 $CL$을 외우는 것이 아니라, 관찰된 $CL$, $t_{1/2}$, $AUC(m)/AUC$, $C/C_b$ 변화가 어느 생리학적 병목에서 왔는지 역추적하는 것입니다.

학습 흐름은 네 단계입니다. 먼저 $Rate=CL\cdot C$로 청소율(clearance)의 비례관계를 세웁니다. 둘째, 신장에서는 $CL_R=f_e\cdot CL$과 여과/분비/재흡수(filtration/secretion/reabsorption)로 분해합니다. 셋째, 간에서는 well-stirred 식으로 $Q_H$, $f_{ub}$, $CL_{int}$, 투과성(permeability)을 분리합니다. 넷째, 모약물–대사체(parent–metabolite) 시스템에서는 $f_m$, $CL(m)$, 율속단계(rate-limiting step; 전체 속도를 정하는 느린 단계), 신장애(renal impairment)를 별도 축으로 추가합니다.

이 문서에서 버릴 수 없는 한 문장은 다음입니다. **“어떤 청소율(clearance)입니까?”라는 질문은 항상 “어느 농도 기준인가, 어느 장기인가, 어느 율속단계인가, 모약물(parent)인가 대사체(metabolite)인가?”로 풀어야 합니다.**

> **지식 그래프 위치(Knowledge-graph Positioning) — [EXPERT_INFERENCE]**  
> 본 세션은 PopPK·PBPK·TMDD·모약물–대사체 공동 모델링(parent–metabolite joint modeling)이 공유하는 **생리학 층위의 중심축(physiology layer spine)**을 닫습니다. 이 장이 없으면 공변량 선택(covariate selection; `eGFR`, $f_u$, transporter genotype, hepatic function score)은 숫자 연습(numeric exercise)에 머물고, 후속 수업에서 “왜 이 공변량을 이 식의 어느 자리에 넣는가”라는 근거를 잃게 됩니다. 이 장을 통과한 뒤에는 매 공변량 결정이 “어느 생리학적 병목을 가설화하는가”라는 질문으로 바뀝니다. 이것이 본 세션이 학습 위계에서 차지하는 위치입니다.

---

> 📊 **개념 도식 (HTML에서 렌더링):** 청소율 해석 의사결정 지도: 장기, 투여 경로, 농도 기준, 대사체 축 — $CL$ 해석은 “어느 농도 기준인가, 어느 장기인가, 어느 투여 경로(route)인가, 모약물(parent)인가 대사체(metabolite)인가?”를 순서대로 묻는 구조적 문제입니다.

## §1.5 v3.4 학습 항법 오버레이: 14개 카드를 한 번에 다 읽지 않는 법

[EXPERT_INFERENCE — senior reviewer navigation patch; 기존 source equations와 card structure를 보존하기 위한 학습 항법 보강]

**A. 이 세션을 읽는 핵심 원칙**

File 04는 처음부터 끝까지 한 방향으로 흘러가는 직선형 강의가 아닙니다. 제거(elimination)와 대사(metabolism)를 해부하기 위한 **지도(map)**입니다. 첫 회독에서 M1부터 M14까지 14개 카드를 모두 같은 강도로 소화하려고 하면, 정작 가장 중요한 의사결정 좌표를 잃고 페이지 사이에서 길을 잃습니다.

이 장 전체를 관통하는 단 하나의 핵심 질문은 다음과 같습니다.

> **"지금 다루는 것이 어떤 청소율(clearance)입니까?"**

그리고 이 질문은 항상 다음 4개 좌표(coordinates)로 분해해서 풀어야 합니다.

| # | 좌표 | 묻는 내용 |
|---|---|---|
| 1 | 농도 기준(concentration basis) | 혈장(plasma)인가, 전혈(blood)인가, 비결합(unbound)인가? |
| 2 | 장기(organ) | 신장(kidney)인가, 간(liver)인가, 그 밖의 조직(tissue)인가? |
| 3 | 투여 경로(route) | 정맥(IV)인가, 경구(oral)인가, 초회통과(first-pass)가 작동합니까? |
| 4 | 분석 대상(analyte) | 모약물(parent)인가, 대사체(metabolite)인가? |

매 카드를 펼칠 때마다 머릿속에서 이 4개 좌표를 먼저 찍고 본문에 들어가세요. 그래야 같은 $CL$이라는 기호가 카드마다 다른 대상을 가리킨다는 사실, 즉 이 장의 진짜 함정이 보입니다.

**B. 90분 최소 회독 경로 (Minimum-Viable Pass)**

시간이 부족하거나 첫 통독에서 골격만 잡고 싶다면, 다음 5개 카드만 순서대로 읽어도 이 장의 의사결정 체계는 작동합니다.

**M1 → M2 → M4 → M5 → M14**

| 카드 | 이 경로에서의 역할 |
|---|---|
| **M1** | 청소율(clearance)의 비례식과 기본 좌표 — $Rate=CL \cdot C$로 시작해서 4개 좌표가 왜 필요한지를 정의한다 |
| **M2** | 신장 청소율(renal clearance)의 분해 — 여과(filtration), 분비(secretion), 재흡수(reabsorption)로 $CL_R$을 풀어낸다 |
| **M4** | 간 청소율(hepatic clearance)과 well-stirred 모델 — $Q_H$, $f_{ub}$, $CL_{int}$을 한 식 안에서 분리한다 |
| **M5** | 고추출/저추출(high/low extraction ratio) 해석 — 같은 식이 추출률(extraction ratio)에 따라 어떻게 다른 임상 함의로 갈라지는지 본다 |
| **M14** | 신장애(renal impairment) + 활성 대사체(active metabolite) 통합 시나리오 — 위 4개 카드가 한 환자에서 동시에 충돌하는 임상·규제 의사결정 사례 |

이 경로가 끝나면, 나머지 카드(M3, M6–M13)는 이 5개 좌표의 정밀화·확장·예외 처리로 읽으시면 됩니다.

**C. 정독 경로 (Full Sweep)**

M1–M14를 모두 읽는 경우, 14개를 한 흐름으로 읽지 말고 다음 **세 덩어리(chunk)**로 나누세요. 각 덩어리가 끝날 때마다 잠시 덮고 4개 좌표를 스스로 재구성해 본 뒤 다음 덩어리로 넘어가는 것이 권장됩니다.

| 덩어리 | 카드 | 학습 목표 |
|---|---|---|
| **① 기본 제거 좌표** | M1–M5 | 청소율(clearance) 정의, 신장·간 분해, well-stirred 모델, 추출률(extraction ratio) 해석 — 4개 좌표 자체의 정립 |
| **② 구현/자료해석 확장** | M6–M10 | 농도 기준 변환($C$ vs $C_b$), 단백결합(protein binding)의 영향, 투과성(permeability)·수송체(transporter), 경구 생체이용률(oral bioavailability)과 초회통과(first-pass) 처리 — 좌표를 실제 데이터에 적용하는 도구 |
| **③ 대사체와 임상위험 통합** | M11–M14 | 모약물/대사체(parent/metabolite) 시스템, 형성·제거 율속(formation/elimination rate-limited), 신장애(renal impairment) 환자에서 활성 대사체(active metabolite) 축적 — 좌표 4(분석 대상) 축의 임상·규제 함의 |

**D. 전문가형 2회독 경로 (Expert Re-Pass)**

이미 기본 약동학(basic PK)을 알고 있는 학습자, 또는 첫 정독을 마치고 두 번째 회독에 들어가는 학습자에게는 다음 순서가 권장됩니다.

**M4 → M10 → M11 → M12 → M14 → §8E**

이 경로의 목적은 카드를 다시 외우는 것이 아니라, **간 대사(hepatic metabolism), 확장 청소율(extended clearance), 대사체 노출(metabolite exposure), NONMEM/PopPK 구현 번역(implementation bridge)을 하나의 의사결정 체계로 묶는 것**입니다. 즉, 환자 수준의 임상 관찰($AUC$, $t_{1/2}$, $AUC(m)/AUC$ 변동) → 생리학적 병목 가설($Q_H$, $f_{ub}$, $CL_{int}$, transporter, formation/elimination rate-limit) → 모델 구현(공변량(covariate) 자리 결정, 모약물/대사체 joint model 구조)까지 하나의 흐름으로 추적하는 훈련입니다.

**E. 주의 문장 — 이 오버레이의 범위**

> 이 §1.5는 **새로운 약동학 이론(new PK theory)을 추가하는 것이 아닙니다.** 이미 PART A에 존재하는 M1–M14 카드를 **읽는 순서를 명시**해 학습자의 인지부하(cognitive load)를 낮추기 위한 v3.4 항법 패치(navigation patch)일 뿐입니다. 신규 page tag, 신규 수식, 신규 약물 예시, 신규 규제 인용, 신규 figure marker는 단 한 건도 추가되지 않았습니다. 모든 카드의 본문, 수식, 페이지 태그, 그림 마커, source anchor는 v3.3에서 byte-level로 보존됩니다.

---

---

<!-- SLIDE_START: §2 | title: §2 개념 해부 카드(Concept Anatomy Cards) -->

## §2 개념 해부 카드(Concept Anatomy Cards)

<!-- SLIDE_START: M1 | title: M1. 청소율 비례성과 반감기의 파생성(Clearance proportionality + half-life is derived) -->

### M1. 청소율 비례성과 반감기의 파생성(Clearance proportionality + half-life is derived)

> **거장의 시각**
> 반감기 변화에서 바로 원인을 찾으면 $CL$ 변화와 $V$ 변화를 섞어 해석하게 됩니다.
> 먼저 $CL$과 $V$를 분리하면 신장애·간장애·단백결합 변화가 어느 축에서 왔는지 보입니다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: 청소율(clearance)은 제거 속도 자체가 아니라 **농도로 정규화(normalize)한 제거능**입니다. 따라서 $CL$은 first-order 조건에서 시간마다 새로 바뀌는 숫자가 아니라, 관찰 구간 전체를 설명하는 하나의 비례상수로 취급됩니다. $AUC$는 그 제거능이 시간 전체에 남긴 관찰량입니다.

**핵심 방정식** [G p.49 Eq 2:83–2:86; G pp.77–79 Eq 2:180–2:185; T5 pp.124–128 Eq 5-1–5-8]

$$
\underbrace{\frac{dX}{dt}}_{\text{체내 변화속도}}=-\underbrace{CL}_{\text{제거능}}\cdot \underbrace{C}_{\text{농도 신호}}
$$

#### 파라미터 해부 표

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $CL$ | L/h | 농도 대비 제거능 | 신장·간 기능, 단백결합, 대사능 |
| $C$ | mg/L | 제거 속도를 정규화하는 농도 신호 | 투여량, 분포, 시간 |
| $V$ | L | 농도를 양으로 환산하는 분포용적 | 조직분포, 단백결합, 체액량 |
| $t_{1/2}$ | h | $V/CL$에서 파생되는 관찰 결과 | ↑ $V$, ↓ $CL$ |

> 💡 **원인과 결과 구분** — $t_{1/2}$는 독립 파라미터가 아니라 $V/CL$의 그림자입니다.
> ⚠️ **헷갈림 방지:** 반감기가 늘었다는 문장은 $CL$ 감소인지 $V$ 증가인지 말해 주지 않습니다.

$$
\underbrace{CL}_{\text{IV 실제 CL}}=\frac{\underbrace{Dose_{iv}}_{\text{IV 투여량}}}{\underbrace{AUC_{0-\infty}}_{\text{IV 전신노출}}}, \qquad \underbrace{\frac{CL}{F}}_{\text{경구 CL/F}}=\frac{\underbrace{D_{po}}_{\text{경구 투여량}}}{\underbrace{AUC_{po}}_{\text{경구 노출}}}
$$

$$
\underbrace{CL}_{\text{총농도 CL}}=\underbrace{f_u}_{\text{유리분율}}\cdot\underbrace{CL_u}_{\text{유리 CL}}
$$

**반감기(half-life)는 원인이 아니라 결과** [T5 pp.148–150 Eq 5-24–5-27]

$$
\underbrace{k}_{\text{소실상수}}=\frac{\underbrace{CL}_{\text{제거능}}}{\underbrace{V}_{\text{분포용적}}}, \qquad \underbrace{t_{1/2}}_{\text{반감기}}=\frac{\underbrace{0.693}_{\ln 2}\cdot\underbrace{V}_{\text{분포용적}}}{\underbrace{CL}_{\text{제거능}}}
$$

$t_{1/2}$가 변했다는 말은 $CL$ 또는 $V$가 변했다는 결과 신호입니다. $t_{1/2}$ 자체가 $CL$을 결정하지 않습니다.

**현장 팁(Trench-level tip)**: 신부전, 간부전, 단백결합 변화에서 “반감기(half-life)가 늘었다/줄었다”로 시작하지 말고 $CL$과 $V$를 먼저 분리하세요. 같은 $t_{1/2}$라도 $CL↑+V↑$가 동시에 생긴 경우와 둘 다 변하지 않은 경우는 완전히 다릅니다.

M1의 $CL$을 신장에 적용하면 M2의 $CL_R$, 간에 적용하면 M4의 $CL_H$, 대사체에 적용하면 M12의 $CL_f$와 $CL(m)$이 됩니다.

---

---

> **M1 체화 핵심**
> ① `반감기가 변했을 때` → $CL$과 $V$ 분리가 원인 진단을 결정
> ② `CL 변화 vs V 변화 혼동` → 같은 $t_{1/2}$라도 전혀 다른 임상 상황
> ⚡ `t_{1/2}$를 원인으로 취급` → covariate 위치 오류와 용량 해석 실패

<!-- SLIDE_START: M2 | title: M2. 신장 청소율 분해: $CL_R$, $f_e$, 여과/분비/재흡수(Renal clearance decomposition: $CL_R$, $f_e$, filtration/secretion/reabsorption) -->

### M2. 신장 청소율 분해: $CL_R$, $f_e$, 여과/분비/재흡수(Renal clearance decomposition: $CL_R$, $f_e$, filtration/secretion/reabsorption)

> **앞 카드에서 이 카드로:** M1에서 $CL$을 농도로 정규화한 제거능으로 정의했으므로, 이제 그중 신장 경로가 차지하는 몫을 분해해야 합니다.

> **거장의 시각**
> $f_e$를 “신기능 영향의 크기”로만 읽으면 nonrenal clearance까지 함께 줄이는 모델을 만들기 쉽습니다.
> $CL_R=f_e\cdot CL$을 경로 분해로 보면 renal covariate를 어느 자리에 넣어야 하는지 즉시 정해집니다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: $CL_R=f_e\cdot CL$은 단순 비례식이 아닙니다. **혈장 AUC와 소변 누적 배설량을 연결하는 측정 교량(measurement bridge)**입니다. 혈장은 몸 안 노출을 보여주고, 소변은 신장 경로(renal route)로 빠져나간 양을 보여줍니다. 둘을 함께 보아야 renal route의 지분 $f_e$와 $CL_R$가 열립니다.

**신장 생리 요약** [G p.48; T5 pp.138–145]

네프론(nephron)은 보먼주머니(Bowman’s capsule), 근위세뇨관(proximal tubule), 헨레고리(loop of Henle), 원위세뇨관(distal tubule), 집합관(collecting duct)으로 구성됩니다. GFR은 Gabrielsson에서 110–130 mL/min, Tozer에서는 참고값(reference)으로 약 120 mL/min입니다. Urine pH는 4.5–8 범위로 변할 수 있습니다 [G p.48; T5 pp.119–120, pp.138–145]. Inulin은 GFR marker로 언급되지만 본 핸드아웃에서는 생리학적 맥락(physiology context)으로만 유지합니다.

Tozer의 참고값은 평균 신장 혈류를 약 `1.1 L/min`으로 제시합니다. 이 값은 신장 장기 추출(organ extraction)의 혈류 천장이며, GFR은 신장 혈장의 여과된 부분집합입니다 [T5 pp.127, 140].

**핵심 신장 방정식** [G pp.49–50 Eq 2:87–2:89; T5 pp.139–142 Eq 5-17–5-23]

$$
\underbrace{\frac{dX_u}{dt}}_{\text{소변 배설속도}}=\underbrace{CL_R}_{\text{신장 CL}}\cdot\underbrace{C}_{\text{혈장농도}}
$$

#### 파라미터 해부 표

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $CL_R$ | L/h | 신장 경로로 제거되는 청소율 | GFR, 분비, 재흡수 |
| $f_e$ | fraction | 전체 CL 중 신장 경로 지분 | 약물 경로, 신기능 |
| $GFR$ | mL/min | 사구체 여과율 | 연령, 신장애, 체표면적 |
| $F_R$ | fraction | 재흡수된 비율 | urine pH, flow, transporter |

> 🔑 **경로 분해 규칙:** 신기능 covariate는 가능하면 total $CL$이 아니라 $CL_R$ 위치에 적용합니다.
> ⚠️ **헷갈림 방지:** $f_e$가 작아도 active metabolite가 renal elimination이면 위험은 작지 않을 수 있습니다.

$$
\underbrace{X_{u,0-\infty}}_{\text{총 소변량}}=\underbrace{CL_R}_{\text{신장 CL}}\cdot\underbrace{AUC_{0-\infty}}_{\text{전신노출}}
$$

$$
\underbrace{CL_R}_{\text{구간 신장 CL}}=\frac{\underbrace{X_u(t_1,t_2)}_{\text{구간 소변량}}}{\underbrace{AUC(t_1,t_2)}_{\text{동일구간 노출}}}
$$

$$
\underbrace{f_e}_{\text{신장 지분}}=\frac{\underbrace{CL_R}_{\text{신장 CL}}}{\underbrace{CL}_{\text{전체 CL}}}
$$

$$
\underbrace{CL_R}_{\text{순 신장 CL}}=\underbrace{(1-F_R)}_{\text{재흡수 잔여율}}\cdot(\underbrace{CL_f}_{\text{여과}}+\underbrace{CL_S}_{\text{분비}}), \qquad \underbrace{CL_f}_{\text{여과 CL}}=\underbrace{f_u}_{\text{유리분율}}\cdot\underbrace{GFR}_{\text{여과율}}
$$

$CL_R>f_u\cdot GFR$이면 분비(secretion)가 필요하고, $CL_R<f_u\cdot GFR$이면 재흡수(reabsorption) 또는 측정 조건을 의심해야 합니다.

**청소율 가산성(Clearance additivity)** [T5 pp.127–128 Eq 5-9]

$$
\underbrace{CL}_{\text{전체 CL}}=\underbrace{CL_R}_{\text{신장}}+\underbrace{CL_H}_{\text{간}}+\underbrace{CL_{other}}_{\text{기타}}
$$

담즙 배설(biliary excretion)과 장간순환(enterohepatic cycling)은 소실 프로파일을 바꿀 수 있지만, 본 문서에서는 M2의 경로 분해 안에 압축한다 [T5 pp.137–138]. 폐 청소율(pulmonary clearance)은 장기 가산성 해석에서 특수 예외로만 기억한다 [T5 p.128].

**혼동 지점(Confusion)**: $f_e$가 작으면 신장애(renal impairment) 영향이 작다고 단정하기 쉽습니다. Parent 기준으로는 대체로 맞을 수 있지만, active metabolite가 renal elimination을 받으면 M14의 결론이 완전히 달라집니다.

M2는 M7의 혈장+소변 동시 적합(simultaneous plasma+urine fitting)과 M14의 신장애 대사체 시나리오(renal impairment metabolite scenario)로 연결됩니다.

---

---

> **M2 체화 핵심**
> ① `신기능이 변했을 때` → $CL_R=f_e\cdot CL$ 분해가 결정
> ② `renal vs nonrenal 경로 혼동` → total $CL$ 보정이 nonrenal pathway까지 왜곡
> ⚡ `$f_e$가 작으면 안전` → active metabolite renal elimination을 놓쳐 신장애 위험 실패

<!-- SLIDE_START: M3 | title: M3. ARE 플롯과 배설속도 플롯(ARE plot vs Excretion Rate plot) -->

### M3. ARE 플롯과 배설속도 플롯(ARE plot vs Excretion Rate plot)

> **앞 카드에서 이 카드로:** M2에서 신장 경로의 양을 정의했으므로, 이제 그 양이 실제 소변 수집 데이터에서 어떻게 왜곡되어 보이는지 확인해야 합니다.

> **거장의 시각**
> ARE와 rate plot의 기울기 불일치를 곧바로 compartment 문제로 보면 urinary artifact를 구조 모델로 오인합니다.
> 두 plot을 함께 보면 collection interval, bladder emptying, pH/flow 변동을 먼저 걸러낼 수 있습니다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: ARE plot과 excretion-rate plot은 같은 urinary data에서 $K$를 추정합니다. 그러나 한쪽은 interval excretion rate를 보고, 다른 한쪽은 남은 누적 배설량을 봅니다. 그래서 noise와 시간 정보가 다르게 보입니다. Rate plot은 renal clearance의 시간 변동을 잘 드러내고, ARE plot은 누적량 기반이라 변동을 평활합니다.

**배설속도 플롯(Rate plot)** [G pp.50–51 Eq 2:90–2:92]

$$
\underbrace{\ln\left(\frac{dX_u}{dt}\right)}_{\text{로그 배설속도}}=\underbrace{\ln\left(CL_R\cdot\frac{D_{iv}}{V}\right)}_{\text{초기절편}}-\underbrace{K}_{\text{소실기울기}}\cdot\underbrace{t}_{\text{시간}}
$$

#### 파라미터 해부 표

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $dX_u/dt$ | amount/time | 구간 소변 배설속도 | 수집 간격, pH/flow |
| $X_{u,0-\infty}$ | amount | 총 소변 회수량 | 수집 완료도, 방광 배출 |
| $K$ | 1/time | 소실 기울기 | $CL/V$, 데이터 배치 |

> 💡 **두 plot의 역할** — Rate plot은 시간 변동을 노출하고, ARE plot은 누적량으로 변동을 평활합니다.
> ⚠️ **헷갈림 방지:** slope 불일치가 곧바로 multi-compartment evidence는 아닙니다.

**ARE 플롯** [G pp.50–52 Eq 2:93–2:98]

$$
\underbrace{\ln(X_{u,0-\infty}-X_u)}_{\text{잔여량 로그}}=\underbrace{\ln(X_{u,0-\infty})}_{\text{총량절편}}-\underbrace{K}_{\text{소실기울기}}\cdot\underbrace{t}_{\text{시간}}
$$

| 판단 축 | 배설속도 플롯(Excretion-rate plot) | ARE 플롯 |
|---|---|---|
| 수집 간격이 반감기보다 길 때 | 취약 | 상대적으로 안정 |
| 불완전 방광 배출 | 취약 | 누적 편향 가능 |
| $X_{u,0-\infty}$ 필요도 | 낮음 | 높음 |
| pH/urine flow에 따른 $CL_R$ 시간 변동 | 잘 보임 | 평활되어 덜 보임 |

**Audit SHOULD_FIX 반영**: 정확한 소변 결과를 위해서는 약물의 소변 농도(drug urinary concentration)가 무시할 수준(negligible level)으로 돌아올 때까지 소변 시료를 수집하는 것이 좋다 [G p.51].

**핵심 예시**: PK5에서 urine collection interval은 0.5–12 h로 다양하고, rate plot/ARE plot에서 half-life가 약 6–6.3 h로 figure-derived 추정된다 [G p.497; 확인 필요: figure-derived value]. Methamphetamine은 urine pH에 따라 urinary recovery가 acidic urine에서 70–80%, alkaline urine에서 1–2%로 크게 달라지는 예로 제시된다 [T5 p.145].

**현장 팁(Trench-level tip)**: urinary data를 보면 먼저 ARE와 rate plot을 둘 다 그리세요. 두 plot이 같은 $K$를 주지 않으면 먼저 collection interval, bladder emptying, pH/flow 변동을 의심하고, 곧바로 compartment 수를 늘리지 마세요.

---

> 📖 **교과서 그림 참조:** [Gabrielsson & Weiner, p.50, Fig 2.35]
> M3의 핵심 혼동은 두 도표(plot)의 기울기(slope)가 모두 $K$를 주더라도 시간 배치와 잡음 민감도(noise sensitivity)가 다르다는 점입니다. 원 그림은 ARE의 실제 시간(actual time)과 배설속도 도표(rate plot)의 중간점 관례(midpoint convention)를 직접 보여 줍니다.
> 확인 시점: 이 카드를 읽은 뒤 확인하세요.

---

> **M3 체화 핵심**
> ① `urinary data가 있을 때` → ARE와 rate plot 동시 진단이 결정
> ② `plot slope 불일치` → 구조 모델보다 collection artifact를 먼저 의심
> ⚡ `바로 compartment 추가` → pH/flow·방광 배출 문제를 모델 구조로 오인

<!-- SLIDE_START: M4 | title: M4. Well-stirred 간 청소율과 4-모델 압축(Well-stirred hepatic clearance + 4-model compression) -->

### M4. Well-stirred 간 청소율과 4-모델 압축(Well-stirred hepatic clearance + 4-model compression)

> **앞 카드에서 이 카드로:** M2–M3가 신장 경로를 측정했다면, 이제 간 경로에서는 혈류와 효소 용량이 어떤 식으로 경쟁하는지 보아야 합니다.

> **거장의 시각**
> 간청소율을 하나의 $CL_H$ 숫자로 읽으면 high/low extraction과 단백결합 효과가 뒤섞입니다.
> $Q_H$와 $f_{ub}CL_{int}$의 경쟁으로 보면 혈류 제한과 용량·결합 제한이 분리됩니다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: Well-stirred model(← 간을 즉시 섞인 장기로 보는 모델)은 hepatic clearance를 세 입력값으로 압축합니다: blood flow $Q_H$, blood unbound fraction $f_{ub}$, intrinsic clearance $CL_{int}$. 분모에서 $Q_H$가 큰지, $f_{ub}\cdot CL_{int}$가 큰지에 따라 high/low extraction 분류와 임상 해석이 갈립니다.

**핵심 방정식** [G pp.79–82 Eq 2:188–2:195; T5 pp.130–135 Eq 5-14–5-15; TE pp.777–778 Eq E-1–E-8]

$$
\underbrace{CL_{H,b}}_{\text{간 CL_b}}=\underbrace{Q_H}_{\text{간혈류}}\cdot\underbrace{E_H}_{\text{추출률}}=\frac{\underbrace{Q_H}_{\text{혈류한계}}\cdot\underbrace{f_{ub}}_{\text{혈액 유리분율}}\cdot\underbrace{CL_{int}}_{\text{간세포 제거능}}}{\underbrace{Q_H}_{\text{혈류}}+\underbrace{f_{ub}\cdot CL_{int}}_{\text{유리·효소축}}}
$$

#### 파라미터 해부 표

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $CL_{H,b}$ | L/h | blood 기준 간 청소율 | $Q_H$, $f_{ub}$, $CL_{int}$ |
| $Q_H$ | L/h | 간으로 들어오는 혈류 천장 | 간혈류, 심박출량 |
| $f_{ub}$ | fraction | blood 기준 비결합 분율 | 단백결합, 혈구분배 |
| $CL_{int}$ | L/h | 간세포 내재 제거능 | 효소·수송체 활성 |

> 🔑 **Well-stirred 판독법:** $Q_H$가 큰지 $f_{ub}CL_{int}$가 큰지를 먼저 비교합니다.
> ⚠️ **헷갈림 방지:** Organ extraction은 blood 기준으로 판단해야 하며 plasma 기준 식으로 대체하지 않습니다.

💡 **비유:** 간은 수도관과 정수기가 붙은 장치입니다. 물이 적게 들어오면 혈류가 한계이고, 정수기 용량이 작으면 $f_{ub}CL_{int}$가 한계입니다.

$$
\underbrace{E_H}_{\text{추출분율}}=\frac{\underbrace{CL_{H,b}}_{\text{간 CL_b}}}{\underbrace{Q_H}_{\text{간혈류}}}=\frac{\underbrace{f_{ub}\cdot CL_{int}}_{\text{제거용량}}}{\underbrace{Q_H}_{\text{혈류공급}}+\underbrace{f_{ub}\cdot CL_{int}}_{\text{제거용량}}}
$$

$Q_H$는 Tozer reference에서 약 1.35 L/min (=81 L/h)로 제시된다 [T5 p.125].

**극한 근사(Limiting cases)** [T5 pp.130–135]

| 조건 | 근사식 | 해석 |
|---|---|---|
| $f_{ub}\cdot CL_{int}\gg Q_H$ | $CL_{H,b} \approx Q_H$ | 혈류 제한(flow-limited), high extraction |
| $f_{ub}\cdot CL_{int}\ll Q_H$ | $CL_{H,b} \approx f_{ub}\cdot CL_{int}$ | 용량/결합 제한(capacity/binding-limited), low extraction |
$$
\begin{aligned}\underbrace{f_{ub}CL_{int}\gg Q_H}_{\text{제거용량>혈류}}&\Rightarrow \underbrace{CL_{H,b}\approx Q_H}_{\text{혈류제한}}\\ \underbrace{f_{ub}CL_{int}\ll Q_H}_{\text{제거용량<혈류}}&\Rightarrow \underbrace{CL_{H,b}\approx f_{ub}CL_{int}}_{\text{용량·결합제한}}\end{aligned}
$$

**네 가지 간 청소율 모델** [G pp.90–94 Table 2.9]

Well-stirred, parallel-tube, distributed, dispersion model은 모두 간 extraction을 설명합니다. 차이는 간 안에서 혈액과 hepatocyte가 얼마나 섞이는지, 그리고 농도 기울기(concentration gradient)를 어떻게 처리하는지에 있습니다. 본 Content Lock에서는 개념적 차이만 보존하고, distributed/dispersion 상세 수식은 출처 충실성 위험 때문에 `[p.94; 확인 필요: formula-level 1:1 재검산 전까지 잠금]`으로 둔다.

**혼동 지점(Confusion)**: “간청소율 식”을 plasma $C$ 기준으로 쓰면 extraction ratio가 틀어집니다. Organ extraction은 blood concentration 기준이며, plasma에서 측정한 값은 M8의 $C/C_b$ 변환을 거쳐야 합니다.

---

> 📖 **교과서 그림 참조:** [Gabrielsson & Weiner, p.79, Fig 2.58; optional companion: Rowland & Tozer, p.131, Fig 5-7]
> Well-stirred equation은 장기 input-output 구조에서 출발합니다. 그림을 보지 않으면 $Q_H$가 단순 공변량(covariate)이 아니라 장기로 들어오는 혈류 천장(blood flow ceiling)이라는 점이 약해집니다.
> 확인 시점: 이 카드를 읽기 전에 확인하세요.

> **M4 체화 핵심**
> ① `간 $CL$을 해석할 때` → $Q_H$와 $f_{ub}CL_{int}$ 경쟁이 결정
> ② `high vs low extraction 혼동` → 단백결합·DDI 해석이 뒤집힘
> ⚡ `plasma 기준 extraction` → organ blood flow와 단위 불일치로 분류 실패

<!-- SLIDE_START: M5 | title: M5. 고/저 추출률과 투여 경로 × 추출률 × $f_u$ 매트릭스(High/low extraction + route × extraction × $f_u$ matrix) -->

### M5. 고/저 추출률과 투여 경로 × 추출률 × $f_u$ 매트릭스(High/low extraction + route × extraction × $f_u$ matrix)

> **앞 카드에서 이 카드로:** M4의 well-stirred 식은 투여 경로와 단백결합 상태가 바뀌면 전혀 다른 임상 결론으로 분기됩니다.

> **거장의 시각**
> “High extraction이면 $f_u$ 무관”을 전체 상황에 적용하면 oral first-pass와 unbound endpoint 해석이 뒤집힙니다.
> 투여 경로 × extraction class × total/unbound의 3축으로 놓으면 같은 $f_u$ 변화도 올바른 칸에 배치됩니다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: 단백결합 변화의 해석은 투여 경로 × 추출률 × total/unbound concentration의 3축 문제입니다. 즉, 같은 $f_u$ 변화라도 IV인지 oral인지, high extraction인지 low extraction인지, total을 보는지 unbound를 보는지에 따라 결론이 달라집니다. “High extraction이면 $f_u$ 무관”은 **IV total concentration**에 한정되는 위험한 반쪽 문장입니다.

**투여 경로 매트릭스(Route matrix)** [G pp.83–85; T5 pp.150–163]

| 시나리오 | Total concentration / AUC | Unbound concentration |
|---|---|---|
| IV + High extraction | $CL \approx Q_H$, total $C$는 $f_u$에 둔감 | $C_u=f_u\cdot C$, $f_u$ 증가 시 unbound 증가 가능 |
| IV + Low extraction | $CL \approx f_u\cdot CL_{int}$, total $C$ 감소 | $C_u$는 대체로 $CL_{int}$에 의해 보존 |
| Oral + High extraction | first-pass 때문에 total AUC가 $f_u\cdot CL_{int}$에 민감 | unbound AUC는 $CL_{int}$ 중심으로 해석 |
| Oral + Low extraction | total AUC가 $f_u\cdot CL_{int}$에 민감 | unbound AUC는 $CL_{int}$ 중심으로 해석 |
$$
\begin{aligned}\text{IV high: }&\underbrace{CL\approx Q_H}_{\text{혈류제한 CL}},\quad \underbrace{C_u=f_uC}_{\text{유리농도 확인}}\\ \text{Low/oral 축: }&\underbrace{CL\approx f_uCL_{int}}_{\text{결합·용량민감}},\quad \underbrace{AUC\propto (f_uCL_{int})^{-1}}_{\text{경구노출 민감}}\end{aligned}
$$

#### 파라미터 해부 표

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $f_u$ | fraction | plasma 비결합 분율 | 알부민, AAG, displacement |
| $C_u$ | concentration | pharmacologically available 농도 | $f_u$, total $C$ |
| $AUC$ | concentration·time | total exposure | route, extraction, $CL_{int}$ |
| $F$ | fraction | 경구 생체이용률 | first-pass, 흡수, 장/간 대사 |

> 💡 **반쪽 문장 경계** — “High extraction이면 $f_u$ 무관”은 IV total endpoint에만 제한적으로 적용됩니다.
> 🔑 **3축 판독법:** route, extraction class, total/unbound endpoint를 동시에 지정해야 합니다.

**Tozer 통합 예시** [T5 pp.152–163]

- Alfentanil + rifampin: low extraction에서 효소 유도(enzyme induction) → clearance 증가, AUC 감소 [T5 p.152].
- Alprenolol + pentobarbital: high extraction IV에서 효소 유도 효과가 작고, 경구 생체이용률(oral bioavailability)은 감소한다 [T5 p.153].
- Fentanyl + itraconazole vs ritonavir: itraconazole은 정맥 fentanyl PK에 큰 영향이 없지만, ritonavir는 clearance를 0.94 → 0.32 L/h/kg로 낮춰 high-to-low extraction 전환을 일으킨다 [T5 pp.154–155].
- Phenytoin 요독증(uremia): $f_u$ 증가로 총 농도(total concentration)는 낮아질 수 있으나 비결합(unbound) 관점 해석이 필요하다 [T5 pp.159–160].
- Clofibric acid 신증후군(nephrotic syndrome): 작은 $V$에서 $f_u$ 증가가 $CL$ 변화를 통해 반감기 단축을 만들 수 있다 [T5 pp.161–162].

**현장 팁(Trench-level tip)**: high extraction drug에서 IV DDI가 음성이라고 oral DDI도 안전하다고 결론 내리지 마세요. Route가 바뀌면 first-pass와 $f_u\cdot CL_{int}$ 민감도가 바뀝니다.

---

> 📊 **개념 도식 (HTML에서 렌더링):** 투여 경로 × 추출률 × 단백결합 해석 매트릭스 — 단백결합 효과(protein binding effect)는 약물 라벨 하나로 결정되지 않고, 투여 경로(route), 추출률 분류(extraction class), total/unbound endpoint에 따라 달라집니다.

---

> **M5 체화 핵심**
> ① `단백결합 변화가 있을 때` → route × extraction × endpoint가 결정
> ② `IV high extraction vs oral high extraction 혼동` → first-pass DDI 위험 누락
> ⚡ `IV negative DDI를 oral 안전으로 일반화` → 라벨 방어 실패

<!-- SLIDE_START: M6 | title: M6. IVIVE 함정: 단일점, MMP, 데이터 압축(IVIVE pitfalls: single-point, MMP, data condensation) -->

### M6. IVIVE 함정: 단일점, MMP, 데이터 압축(IVIVE pitfalls: single-point, MMP, data condensation)

> **앞 카드에서 이 카드로:** M4–M5가 간 청소율 식의 해석을 세웠다면, 이제 그 식에 넣는 $CL_{int}$ 입력값이 어디서 무너질 수 있는지 점검해야 합니다.

> **거장의 시각**
> IVIVE 실패를 hepatic model의 문제로만 보면 이미 압축되어 사라진 in vitro curvature를 복구하려고 하게 됩니다.
> 입력 데이터가 single point·MMP·condensation 중 어디서 정보를 잃었는지 먼저 보면 실패 원인이 상류에서 보입니다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: IVIVE는 $V_{max}$, $K_m$, microsomal protein scaling을 넣는 계산 문제가 아닙니다. 먼저 **어떤 정보를 버렸는지**를 점검해야 합니다. 한 점에서 얻은 $CL_{int}$, 잘못된 MMP 보정, 과도한 data condensation은 모두 in vivo clearance를 왜곡합니다.

**핵심 흐름** [G pp.85–90]

$$
\underbrace{CL_{int,in\ vitro}}_{\text{in vitro 제거능}}\rightarrow \underbrace{CL_{int,scaled}}_{\text{체내 스케일}}\rightarrow \underbrace{CL_H}_{\text{예측 간 CL}}=\frac{\underbrace{Q_H}_{\text{혈류}}\cdot\underbrace{f_u}_{\text{유리분율}}\cdot\underbrace{CL_{int}}_{\text{스케일 제거능}}}{\underbrace{Q_H}_{\text{혈류}}+\underbrace{f_u\cdot CL_{int}}_{\text{제거용량}}}
$$

#### 파라미터 해부 표

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $CL_{int,in\ vitro}$ | volume/time | in vitro 제거능 | 농도범위, 비결합 보정 |
| $CL_{int,scaled}$ | volume/time | 체내로 스케일된 제거능 | MMP, liver weight, scaling factor |
| $V_{max}/K_m$ | volume/time | 저농도 선형 근사 제거능 | 포화, enzyme capacity |

> ⚠️ **헷갈림 방지:** 정교한 hepatic model은 single-point 입력에서 사라진 curvature를 복구하지 못합니다.
> 🔑 **IVIVE 검토 순서:** single-point → MMP scaling → data condensation → transporter/permeability 누락 순서로 점검합니다.

💡 **비유:** IVIVE는 흐릿하게 압축된 사진을 고해상도 화면에 띄우는 작업과 같습니다. 원본 rate 곡선이 사라졌다면 뒤의 모델은 잃어버린 곡률을 만들 수 없습니다.

**세 가지 함정**

1. **단일 농도 함정(Single-point trap)**: 한 농도에서 얻은 rate를 $V_{max}/K_m$처럼 쓰면 비선형성(nonlinearity)과 포화(saturation)를 놓친다 [G pp.85–89].
2. **MMP 보정 함정(MMP scaling trap)**: 간 조직 g당 microsomal protein 보정은 평균값 하나가 아니라 변이(variability)와 비율 처리 방식에 민감하다 [G p.87].
3. **데이터 압축 함정(Data condensation trap)**: 원시 농도–속도 관계를 하나의 $CL_{int}$로 압축하면 곡선 형태(curvature)와 이상치 구조가 사라진다 [G pp.88–89].

**현장 팁(Trench-level tip)**: IVIVE report를 검토할 때 첫 질문은 “well-stirred 식이 맞는가?”가 아니라 “in vitro rate 정보가 single point로 collapse되었는가?”다. Collapse된 입력은 정교한 hepatic model로도 복구되지 않는다.

---

> **M6 체화 핵심**
> ① `IVIVE 예측이 빗나갈 때` → 입력 데이터 압축 여부가 결정
> ② `single-point rate vs MM 정보 혼동` → saturation과 curvature 소실
> ⚡ `정교한 간 모델로 복구 가능하다는 믿음` → Phase 1 CL 예측 실패

<!-- SLIDE_START: M7 | title: M7. PK5 혈장+소변 동시 적합(PK5 simultaneous plasma+urine fitting) -->

### M7. PK5 혈장+소변 동시 적합(PK5 simultaneous plasma+urine fitting)

> **앞 카드에서 이 카드로:** M2–M6의 장기별 분해는 실제 데이터에서 plasma와 urine을 동시에 맞출 때 비로소 추정 가능한 구조가 됩니다.

> **거장의 시각**
> 소변 데이터를 별도 계산표로 분리하면 $f_e$와 $CL_R$ 식별성이 plasma model 밖으로 밀려납니다.
> Plasma와 urine을 동시에 적합하면 endpoint별 오차와 renal fraction을 같은 구조 안에서 추정할 수 있습니다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: PK5는 urinary data를 별도 계산표로 처리하지 않는다. **Plasma concentration과 cumulative urine amount를 한 모델에서 동시에 fitting**합니다. 이 구조가 NONMEM에서 plasma+urine, IV+oral, parent+metabolite를 함께 fitting하는 사고방식의 출발점입니다.

**문제 앵커** [G pp.494–499]

- Dose: 250 mg i.v. bolus [G p.494].
- 초기 추정값: $V \approx 7 L$, $CL \approx 2\ \mathrm{L/h}$, $f_e \approx 0.3$ [G p.497].
- 최종 추정값: $CL \approx 1.2\ \mathrm{L/h}$, $f_e \approx 35\%$, $CL_R \approx 0.42\ \mathrm{L/h}$; parameter CVs <5%; plasma/urine CV estimates 2.84% and 8.96% [G p.498].

**해석적 풀이 vs ODE 등가성** [G pp.497–499]

해석적 풀이와 미분방정식 시스템은 거의 동일한 최종 파라미터 추정값과 정밀도를 산출합니다.

**모델 골격** [G pp.497–499]

$$
\underbrace{C(t)}_{\text{혈장농도}}=\frac{\underbrace{D_{iv}}_{\text{IV 용량}}}{\underbrace{V}_{\text{분포용적}}}\exp\left(-\underbrace{\frac{CL}{V}}_{\text{소실상수 }k}\underbrace{t}_{\text{시간}}\right)
$$

#### 파라미터 해부 표

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $C(t)$ | mg/L | 시간별 plasma 농도 | $D_{iv}$, $V$, $CL$ |
| $X_u(t)$ | amount | 누적 소변 배설량 | $f_e$, $D_{iv}$, $CL/V$ |
| $f_e$ | fraction | 신장 제거 지분 | renal route, urine recovery |

> 💡 **동시 적합의 의미** — Plasma는 exposure를, urine은 renal route의 양을 알려주므로 둘을 분리하면 $f_e$가 흔들립니다.
> ⚠️ **헷갈림 방지:** endpoint별 CV가 다르면 residual error도 분리해야 합니다.

💡 **비유:** Plasma 곡선은 저수지 수위이고 urine 누적량은 배수구로 빠진 총량입니다. 둘을 같이 봐야 밸브가 얼마나 신장 쪽으로 열려 있는지 알 수 있습니다.

$$
\underbrace{X_u(t)}_{\text{누적 소변량}}=\underbrace{f_e}_{\text{신장 지분}}\cdot\underbrace{D_{iv}}_{\text{IV 용량}}\left[1-\exp\left(-\underbrace{\frac{CL}{V}}_{\text{소실상수}}\underbrace{t}_{\text{시간}}\right)\right]
$$

> 💼 **실무 인사이트:** plasma와 urine endpoint를 하나의 residual error scale로 묶지 않는다. PK5가 직접 보여주듯 두 endpoint의 CV는 서로 다르므로, `DVID` 기반 endpoint 분리와 각 전용 residual error block을 사용합니다.

---

---

> **M7 체화 핵심**
> ① `plasma+urine 데이터가 있을 때` → endpoint 동시 적합이 $f_e$와 $CL_R$를 결정
> ② `plasma-only fit` → renal fraction 식별 불가
> ⚡ `오차 모델 통합` → endpoint별 산포 차이를 흡수해 추정 편향

<!-- SLIDE_START: M8 | title: M8. 혈장-혈액 비와 혈액 청소율(Plasma-to-blood ratio and blood clearance) -->

### M8. 혈장-혈액 비와 혈액 청소율(Plasma-to-blood ratio and blood clearance)

> **앞 카드에서 이 카드로:** M4–M7의 간·신장 해석은 농도 기준이 맞아야 작동하므로, plasma 기준을 blood 기준으로 바꾸는 교량이 필요합니다.

> **거장의 시각**
> Plasma $CL$을 그대로 $Q_H$와 비교하면 organ extraction의 분모가 틀어져 false-high extraction이 생깁니다.
> $C/C_b$를 통과해 $CL_b$로 바꾸면 혈류와 같은 단위에서 간 extraction을 판단할 수 있습니다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: Organ extraction ratio(← 장기 통과 중 제거된 비율)는 blood flow와 비교하므로 **blood concentration 기준 clearance**가 필요합니다. 그런데 실제 측정은 대부분 plasma concentration입니다. $C/C_b$ 변환을 하지 않으면 denominator가 달라진다. 그 결과 extraction ratio 분류가 systematic하게 틀어집니다.

**청소율 관계식** [T5 pp.124–128 Eq 5-4–5-6]

$R=C/C_b$로 정의합니다.

$$
\underbrace{CL_b}_{\text{혈액 CL}}=\underbrace{CL}_{\text{혈장 CL}}\cdot\underbrace{\frac{C}{C_b}}_{\text{기준변환}}=\underbrace{CL}_{\text{혈장 CL}}\cdot\underbrace{R}_{\text{변환비}}
$$

#### 파라미터 해부 표

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $CL_b$ | L/h | blood 기준 청소율 | plasma $CL$, $C/C_b$ |
| $R=C/C_b$ | ratio | plasma-to-blood 변환비 | hematocrit, RBC partition |
| $H$ | fraction | hematocrit | 환자 혈구용적률 |
| $K_{PBC}$ | ratio | 혈구-비결합 혈장 분배 | RBC binding/partition |

> 🔑 **Extraction 전 필수 변환:** hepatic $E_H$ 계산 전 plasma $CL$을 $CL_b$로 변환합니다.
> ⚠️ **헷갈림 방지:** $f_u$와 $f_{ub}$는 같은 분율이 아니라 농도 기준이 다른 분율입니다.

$$
\underbrace{CL}_{\text{혈장 CL}}=\underbrace{CL_b}_{\text{혈액 CL}}\cdot\underbrace{\frac{C_b}{C}}_{\text{역변환}}=\frac{\underbrace{CL_b}_{\text{혈액 CL}}}{\underbrace{R}_{C/C_b}}
$$

**App.D 질량수지** [TD pp.775–776 Eq D-1–D-8]

$$
\underbrace{\frac{C}{C_b}}_{\text{혈장/혈액비}}=\frac{1}{1+\underbrace{H}_{\text{적혈구용적률}}\left(\underbrace{f_u}_{\text{혈장 유리분율}}\underbrace{K_{PBC}}_{\text{RBC 분배}}-1\right)}
$$

여기서 $H$는 hematocrit, $f_u$는 혈장 내 비결합 분율(unbound fraction in plasma), $K_{PBC}$는 혈구-비결합 혈장 분배계수(blood-cell-to-unbound-plasma partition coefficient)다.

**미세 패치 — App.D 역행렬 필수** [TD pp.775–776 Eq D-8]

$$
\underbrace{K_{PBC}}_{\text{RBC/혈장 분배}}=\frac{\underbrace{H}_{\text{적혈구용적률}}-1+\underbrace{(C_b/C)}_{\text{혈액/혈장비}}}{\underbrace{f_u}_{\text{유리분율}}\cdot\underbrace{H}_{\text{RBC 분율}}}
$$

**해석상 함의**

- $R<1$이면 혈장 농도가 혈액 농도보다 높습니다. 비율 사용 방식에 따라 plasma CL이 실제보다 다르게 보일 수 있습니다.
- 간 extraction에는 plasma $CL_H/Q_H$가 아닌 $E_H=CL_{H,b}/Q_H$를 사용해야 합니다.
- $f_u$와 $f_{ub}$는 호환되지 않는다. $f_{ub}=f_u\cdot (C/C_b)$로 변환됩니다.

**혼동 지점(Confusion)**: $CL=60\ \mathrm{L/h}$, $Q_H=81\ \mathrm{L/h}$이면 중등도 extraction처럼 보일 수 있습니다. 그러나 $R=C/C_b=0.5$이면 $CL_b=30\ \mathrm{L/h}$이고 $E_H=0.37$입니다. 분류가 바뀐다.

---

ho$와 extended clearance는 $CL_{int}$가 충분해도 hepatocyte 접근성과 transporter 단계가 전체 $CL_H$를 막을 수 있음을 보여준다.

---

> **M8 체화 핵심**
> ① `간 extraction을 판단할 때` → $CL_b=CL\cdot C/C_b$ 변환이 결정
> ② `plasma CL vs blood CL 혼동` → false-high extraction 분류
> ⚡ `$CL/Q_H$ 직접 비교` → PBPK 입력과 DDI 해석 실패

<!-- SLIDE_START: M9 | title: M9. 투과성 속도 제한 간 흡수: App.E $\rho$ (Permeability-rate-limited hepatic uptake: App.E $\rho$) -->

### M9. 투과성 속도 제한 간 흡수: App.E $\rho$ (Permeability-rate-limited hepatic uptake: App.E $\rho$)

> **앞 카드에서 이 카드로:** M8에서 blood 기준을 맞춘 뒤에도, hepatocyte 내부로 들어가는 접근성이 느리면 well-stirred의 전제가 무너집니다.

> **거장의 시각**
> $CL_{int}$가 충분하면 hepatic clearance도 충분하다고 보면 hepatocyte 접근성 병목을 놓칩니다.
> $\rho$를 넣으면 세포막 uptake가 효소 제거능보다 앞단에서 clearance를 제한할 수 있음을 볼 수 있습니다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: Basic well-stirred model은 liver cell 안팎의 unbound concentration이 빠르게 평형이라고 가정합니다. 그러나 hepatic uptake permeability가 느리면 hepatocyte 내부 unbound concentration이 blood unbound concentration보다 낮아진다. 이 경우 $CL_{int}$만으로는 hepatic clearance를 설명할 수 없습니다.

**App.E Model II** [TE pp.778–779 Eq E-9–E-15]

$\rho$(← 세포 안팎 unbound 비율)는 hepatocyte 내부 unbound concentration이 혈액 쪽 unbound concentration을 얼마나 따라가는지 나타낸다.

$$
\underbrace{\rho}_{\text{세포접근성}}=\frac{\underbrace{P_{in}\cdot SA}_{\text{유입투과}}}{\underbrace{P_{out}\cdot SA}_{\text{유출투과}}+\underbrace{CL_{int}}_{\text{대사제거}}}
$$

#### 파라미터 해부 표

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $\rho$ | ratio | hepatocyte 접근성 | uptake/outflow permeability, $CL_{int}$ |
| $P_{in}\cdot SA$ | volume/time | 세포 유입 투과능 | transporter, membrane permeability |
| $P_{out}\cdot SA$ | volume/time | 세포 유출 투과능 | efflux, passive diffusion |
| $CL_{int}$ | volume/time | 세포 내 대사 제거능 | enzyme activity |

> 💡 **접근성 병목** — 효소가 충분해도 약물이 hepatocyte 안으로 못 들어가면 clearance는 낮아집니다.
> 🔑 **ρ 판독법:** passive diffusion이 충분하면 $\rho\to1$, uptake가 느리면 $\rho<1$입니다.

💡 **비유:** $\rho$는 공장 문 앞의 회전문 속도입니다. 공장 안 효소가 아무리 빨라도 회전문이 느리면 전체 생산량은 느려집니다.

$$
\underbrace{CL_{H,b}}_{\text{간 CL_b}}=\frac{\underbrace{Q_H}_{\text{혈류}}\cdot\underbrace{f_{ub}}_{\text{혈액 유리분율}}\cdot\underbrace{\rho}_{\text{세포접근성}}\cdot\underbrace{CL_{int}}_{\text{대사제거}}}{\underbrace{Q_H}_{\text{혈류}}+\underbrace{f_{ub}\cdot \rho\cdot CL_{int}}_{\text{보정 제거축}}}
$$

**감사 수정(Audit correction)**

수동 확산(passive diffusion) / permeability가 충분히 커서 세포 내외의 비결합 농도(unbound concentration)가 빠르게 평형에 가까워지면 $\rho\to1$이 되어 basic well-stirred model로 환원됩니다. 반대로 uptake permeability가 작으면 $\rho<1$이고 clearance는 permeability-limited가 된다 [TE pp.778–779].

**경구 투여 교량(Oral bridge)** [TE pp.779–780 Eq E-19–E-20]

상기 가정하에 간 extraction으로만 제거되는 약물의 경우:

$$
\underbrace{AUC_{po}}_{\text{경구노출}}=\frac{\underbrace{Dose}_{\text{투여량}}}{\underbrace{f_{ub}}_{\text{혈액 유리분율}}\cdot\underbrace{\rho}_{\text{세포접근성}}\cdot\underbrace{CL_{int}}_{\text{제거능}}}
$$

**현장 팁(Trench-level tip)**: transporter substrate에서 $f_u$와 $CL_{int}$만으로 IVIVE를 강행하면 permeability bottleneck을 $CL_{int}$ 부족으로 오해할 수 있습니다.

---

> **M9 체화 핵심**
> ① `$CL_{int}$로 설명되지 않는 간 CL` → $\rho$가 결정
> ② `효소 부족 vs uptake 병목 혼동` → covariate 선택 위치 오류
> ⚡ `$\rho$ 생략` → transporter substrate의 IVIVE mismatch 은폐

<!-- SLIDE_START: M10 | title: M10. 확장 청소율: 수송체–효소 구조(Extended clearance: transporter–enzyme architecture) -->

### M10. 확장 청소율: 수송체–효소 구조(Extended clearance: transporter–enzyme architecture)

> **앞 카드에서 이 카드로:** M9의 $\rho$는 단일 보정항처럼 보이지만, 실제로는 uptake·metabolism·efflux의 다층 구조를 열어 줍니다.

> **거장의 시각**
> 간 소실을 enzyme 하나로 축약하면 transporter 단계의 DDI와 IVIVE mismatch가 모두 $CL_{int}$ 오류처럼 보입니다.
> Uptake·metabolism·efflux를 나누면 어느 membrane step이 전체 clearance를 막는지 분류할 수 있습니다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: Extended clearance는 hepatic elimination을 “enzyme 하나”로 보지 않는다. **Sinusoidal uptake, canalicular efflux, basolateral efflux, intracellular metabolism**의 네 흐름으로 봅니다. Basic well-stirred는 이 네 흐름 중 membrane step이 충분히 빠른 특수한 경우다.

**핵심 출처** [T5 pp.136–138 Eq 5-35–5-36]

T5는 간 소실이 관류(perfusion), 혈장 단백결합(plasma protein binding), 간세포 활성(hepatocellular activity)만으로 끝나지 않고, 막 투과성(membrane permeability)과 수송체(transporter)에 의해 달라질 수 있음을 명시합니다. App.E는 이 점을 $\rho$로 제1원리화(first-principles)한다 [TE pp.778–779].

**최소 해석**

- Uptake-limited: 혈장/혈액에서 hepatocyte로 들어가는 단계가 병목.
- Metabolism-limited: 세포 내부 도달은 충분하고 효소 용량(enzyme capacity)이 병목.
- Efflux-limited: 담즙 또는 혈액 방향 유출(efflux)이 병목.

M10은 M6의 IVIVE trap과 M9의 $\rho$를 연결합니다. 즉, poor IVIVE가 항상 enzyme assay 문제는 아니며, transporter/permeability term 누락일 수 있습니다.

---

> 📖 **교과서 그림 참조:** [Rowland & Tozer, p.136, Fig 5-11; companion equations: Tozer App.E pp.778–779, Eq E-9–E-15]
> M10은 세포막(cell membrane)을 사이에 둔 uptake, metabolism, efflux의 위치 관계가 핵심입니다. 이 위치 관계를 보지 않으면 permeability-limited clearance를 단순한 낮은 $CL_{int}$로 오해하기 쉽습니다.
> 확인 시점: 이 카드를 읽기 전에 확인하세요.

---

#### 파라미터 해부 표

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| Uptake | — | 혈액→hepatocyte 유입 | OATP/OCT/OAT, permeability |
| Metabolism | — | 세포 내 효소 제거 | CYP/UGT activity |
| Efflux | — | 담즙/혈액 방향 유출 | canalicular/basolateral transporter |
| $\rho$ | ratio | membrane bottleneck 요약 | uptake vs metabolism 경쟁 |

> 💡 **구조 확장** — Extended clearance는 enzyme 하나가 아니라 uptake·metabolism·efflux의 병렬/직렬 구조입니다.
> ⚠️ **헷갈림 방지:** empirical scalar는 transporter 병목을 숨길 수 있습니다.

> **M10 체화 핵심**
> ① `수송체 기질 간 소실` → uptake/metabolism/efflux 단계가 결정
> ② `enzyme-only 사고` → transporter DDI와 efflux 병목 누락
> ⚡ `empirical scalar로 봉합` → 구조 원인 은폐와 예측 외삽 실패

<!-- SLIDE_START: M11 | title: M11. 대사체 처리(disposition)의 율속단계(Rate-limiting step in metabolite disposition) -->

### M11. 대사체 처리(disposition)의 율속단계(Rate-limiting step in metabolite disposition)

> **앞 카드에서 이 카드로:** M10까지 parent clearance의 병목을 분해했다면, 이제 metabolite 곡선의 terminal slope가 무엇을 반영하는지 분리해야 합니다.

> **거장의 시각**
> Metabolite terminal slope를 곧바로 metabolite half-life라고 쓰면 formation-limited 상황에서 parent의 그림자를 metabolite 특성으로 오인합니다.
> Formation과 elimination 중 느린 단계를 확인하면 observed slope와 true metabolite disposition을 분리할 수 있습니다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: 대사체 농도-시간 곡선의 terminal slope(← 말단 감소 구간의 기울기)는 대사체 자체의 half-life가 아닐 수 있습니다. Formation이 느리면 대사체는 parent의 “그림자”처럼 parent half-life로 감소합니다. Elimination이 느리면 대사체 자체 half-life가 terminal phase를 지배합니다.

**대사체가 중요한 이유** [T20 pp.658–659]

대사체가 임상적으로 중요한 이유는 다섯 가지다: **활성(action), 독성(toxicity), 억제(inhibition), 유도(induction), 치환(displacement)**. 그러나 대사체가 그런 성질을 가져도 충분한 농도에 도달하지 않으면 치료적 우려는 작다 [T20 p.659]. 즉, “active metabolite가 있다”와 “임상적으로 중요하다”는 같은 말이 아닙니다.

**질량수지(Mass balance)** [T20 pp.659–662 Eq 20-1–20-3]

$$
\underbrace{\frac{dA(m)}{dt}}_{\text{대사체 변화}}=\underbrace{k_fA}_{\text{형성입력}}-\underbrace{k(m)A(m)}_{\text{제거출력}}
$$

#### 파라미터 해부 표

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $k_f$ | 1/time | parent→metabolite 형성속도 | 효소, parent 노출 |
| $k(m)$ | 1/time | metabolite 제거속도 | renal/hepatic metabolite CL |
| $A(m)$ | amount | 체내 대사체 양 | 형성입력·제거출력 |
| terminal slope | 1/time | 관찰된 말단 감소 | formation 또는 elimination 율속 |

> 🔑 **Terminal slope 규칙:** downstream substance의 terminal decline은 가장 느린 step이 지배합니다.
> ⚠️ **헷갈림 방지:** parallel decline은 metabolite own half-life의 증거가 아니라 formation-limited 신호일 수 있습니다.

💡 **비유:** 대사체는 앞차(parent)를 따라가는 차량처럼 보일 수 있습니다. 앞차가 느리면 뒤차의 속도계가 아니라 교통 흐름 전체가 느린 것입니다.

| 분류 | 조건 | 관찰 패턴 | 해석 |
|---|---|---|---|
| Formation rate-limited | $k \ll k(m)$ | parent에 나란히 감소 | 관찰된 metabolite terminal $t_{1/2}$은 parent의 half-life |
| Elimination rate-limited | $k(m) \ll k$ | metabolite가 더 늦게 peak, 더 느리게 감소 | terminal $t_{1/2}$은 metabolite 자신의 half-life |
$$
\begin{aligned}\underbrace{k\ll k(m)}_{\text{형성 느림}}&\Rightarrow \underbrace{t_{1/2,\mathrm{obs}}(m)\approx t_{1/2,\mathrm{parent}}}_{\text{parent 그림자}}\\ \underbrace{k(m)\ll k}_{\text{제거 느림}}&\Rightarrow \underbrace{t_{1/2,\mathrm{obs}}(m)\approx t_{1/2,\mathrm{metabolite}}}_{\text{대사체 지배}}\end{aligned}
$$

**감사 수정(Audit correction)**

Sequential chain에서는 “fastest k가 결정한다”가 아니라, downstream substance의 terminal decline은 **가장 느린 step**에 의해 지배된다 [T20 p.661]. Renal impairment에서는 parent CL 보정이 metabolite exposure를 자동 보정하지 않는다; metabolite CL과 rate-limiting step을 별도로 평가해야 한다 [T20 pp.673–675].

**혼동 지점(Confusion)**: parent와 metabolite가 parallel decline이면 metabolite half-life를 parent와 같다고 보고하기 쉽다. 정확히는 “observed terminal half-life after parent dosing”이 parent의 half-life를 반영할 뿐입니다.

---

> 📖 **교과서 그림 참조:** [Rowland & Tozer, p.660, Fig 20-1]
> 대사체의 terminal slope는 formation과 elimination 중 더 느린 step에 의해 결정됩니다. 원 그림은 parent → metabolite → eliminated metabolite 흐름에서 $k_f$, $k(m)$, other elimination을 동시에 보여 줍니다.
> 확인 시점: 이 카드를 읽기 전에 확인하세요.

> **M11 체화 핵심**
> ① `metabolite terminal slope를 볼 때` → formation/elimination 율속단계가 결정
> ② `parallel decline vs own half-life 혼동` → metabolite half-life 과대 해석
> ⚡ `system slope를 metabolite label로 보고` → renal impairment 축적 예측 실패

<!-- SLIDE_START: M12 | title: M12. $AUC(m)/AUC$ 분해: $f_m × CL/CL(m)$ ($AUC(m)/AUC$ decomposition: $f_m × CL/CL(m)$) -->

### M12. $AUC(m)/AUC$ 분해: $f_m × CL/CL(m)$ ($AUC(m)/AUC$ decomposition: $f_m × CL/CL(m)$)

> **앞 카드에서 이 카드로:** M11에서 formation과 elimination 율속을 나눴으므로, 이제 $AUC(m)/AUC$를 $f_m$과 $CL(m)$으로 분해해야 합니다.

> **거장의 시각**
> $AUC(m)/AUC$를 $f_m$으로 읽으면 formation 문제와 metabolite clearance 문제를 구분할 수 없습니다.
> 비를 $f_m\times CL/CL(m)$으로 분해하면 active metabolite risk의 정량 좌표가 생깁니다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: $AUC(m)/AUC$는 $f_m$ 그 자체가 아닙니다. 이 비는 metabolite formation fraction과 metabolite clearance가 함께 들어간 compound quantity다. 따라서 AUC ratio 하나만 보고 formation 쪽 문제인지 elimination 쪽 문제인지 분리할 수 없습니다.

**핵심 방정식** [T20 pp.662–665 Eq 20-4–20-7]

$$
\underbrace{\frac{dA(m)}{dt}}_{\text{대사체 변화}}=\underbrace{CL_f\cdot C}_{\text{형성입력}}-\underbrace{CL(m)\cdot C(m)}_{\text{제거출력}}
$$

#### 파라미터 해부 표

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $AUC(m)/AUC$ | ratio | metabolite/parent 노출비 | $f_m$, $CL$, $CL(m)$ |
| $CL_f$ | L/h | metabolite 형성 clearance | $f_m\cdot CL$ |
| $f_m$ | fraction | parent 제거 중 형성분율 | metabolic pathway share |
| $CL(m)$ | L/h | metabolite 제거 clearance | renal/hepatic function |

> 💡 **복합량 주의** — $AUC(m)/AUC$는 $f_m$과 $CL(m)$이 섞인 값입니다.
> ⚠️ **헷갈림 방지:** AUC ratio 하나로 formation 문제와 elimination 문제를 분리할 수 없습니다.

💡 **비유:** $AUC(m)/AUC$는 수도꼭지 유입량($f_m$)과 배수구 크기($CL(m)$)가 함께 만든 수위입니다. 수위만 보고 수도꼭지 크기를 단정할 수 없습니다.

시간에 대해 적분하면:

$$
\underbrace{\frac{AUC(m)}{AUC}}_{\text{노출비}}=\frac{\underbrace{CL_f}_{\text{형성 CL}}}{\underbrace{CL(m)}_{\text{대사체 CL}}}
$$

여기서:

$$
\underbrace{CL_f}_{\text{형성 CL}}=\underbrace{f_m}_{\text{형성분율}}\cdot\underbrace{CL}_{\text{parent CL}}
$$

따라서:

$$
\boxed{\underbrace{\frac{AUC(m)}{AUC}}_{\text{노출비}}=\underbrace{f_m}_{\text{형성분율}}\cdot\frac{\underbrace{CL}_{\text{parent CL}}}{\underbrace{CL(m)}_{\text{대사체 CL}}}}
$$

**미세 패치 — 필수 Eq.20-7** [T20 p.664 Eq 20-7]

$$
\underbrace{\frac{k(m)}{k}}_{\text{속도비}}=\frac{\underbrace{CL(m)/CL}_{\text{청소율비}}}{\underbrace{V(m)/V}_{\text{분포비}}}
$$

**감사 수정(Audit correction)**

$AUC(m)/AUC<1$이고 $f_m$이 알려지지 않은 경우, $CL(m) ≥ CL/f_m$이라고 추론할 수 없습니다. Source에 부합하는 부등식은 $CL(m)>f_m\cdot CL$뿐입니다. 같은 AUC ratio는 낮은 $f_m$, 높은 $CL(m)$, 또는 두 조건 모두에서 발생할 수 있습니다.

**보존된 예시** [T20 pp.662–665]

Methylprednisolone hemisuccinate → methylprednisolone, tolbutamide → hydroxytolbutamide, propranolol → naphthoxylactic acid는 대사체 곡선이 율속단계와 상대적 청소율을 어떻게 구분하는지 보여주는 예시다. 개별 그림 수치는 이 문서에서 확장하지 않는다.

**현장 팁(Trench-level tip)**: active metabolite PopPK에서 $AUC(m)/AUC$가 작다는 이유로 metabolite를 무시하지 않는다. $f_m$이 작아도 $CL(m)$이 renal impairment에서 크게 줄면 M14의 문제가 됩니다.

---

---

> **M12 체화 핵심**
> ① `AUC(m)/AUC가 주어졌을 때` → $f_m$과 $CL(m)$ 분해가 결정
> ② `노출비 vs 형성분율 혼동` → 신부전·DDI 외삽 오류
> ⚡ `AUC ratio 단독 보고` → formation/elimination 원인 구분 실패

<!-- SLIDE_START: M13 | title: M13. 초회통과 대사체 기여와 정상상태 대사체(First-pass metabolite contribution + steady-state metabolite) -->

### M13. 초회통과 대사체 기여와 정상상태 대사체(First-pass metabolite contribution + steady-state metabolite)

> **앞 카드에서 이 카드로:** M12의 노출비 분해는 단회 노출을 넘어 first-pass 형성과 정상상태 축적 문제로 이어집니다.

> **거장의 시각**
> Oral metabolite 노출을 단순히 bioavailability 문제로 보면 first-pass formation과 systemic formation이 섞입니다.
> 입력 경로를 둘로 나누면 정상상태 축적과 IV-oral 비교 설계의 필요성이 드러납니다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: Oral parent dosing 후 metabolite는 두 경로에서 생길 수 있다: absorption 중 first-pass formation, 그리고 흡수된 systemic parent에서 생기는 post-absorption formation. 이것은 “oral이 항상 더 강하다”는 규칙이 아닙니다. Parent가 high first-pass extraction을 보이고 metabolite가 active 또는 clinically relevant할 때 문제가 됩니다.

**First-pass 이중 입력 모델** [T20 pp.665–669]

경구 parent 투여 후 관찰되는 대사체는 두 입력의 합이다:

1. 흡수·first-pass 과정에서 형성된 대사체, 그리고
2. 흡수된 전신 parent에서 이후 형성된 대사체.

**수정된 예시**

- Propranolol: 원전 예시는 단일 **20 mg 경구 투여**이며, 80 mg이 아닙니다. Naphthoxylactic acid는 propranolol과 거의 같은 시간에 최고 농도에 도달하며, 이는 first-pass 대사체 유입과 일치한다 [T20 p.666].
- Morphine/M6G: 원전은 경구 **11.7 mg**과 정맥 **5 mg** morphine을 비교하며, 10 mg 등가 용량 틀이 아닙니다. Morphine의 경구 생체이용률은 낮지만, first-pass 형성이 기여하므로 M6G 노출량/총량은 비슷할 수 있다 [T20 pp.667–668].
- Isoproterenol: 투여 경로에 따른 소변 회수 패턴 차이가 장벽/간외 대사(gut-wall/extrahepatic metabolism)를 시사하는 예시다 [T20 p.669].

**정상상태 대사체** [T20 pp.669–673 Eq 20-11–20-15]

일정 속도 주입(constant-rate input) 시:

$$
\underbrace{C(m)_{ss}}_{\text{대사체 Css}}=\frac{\underbrace{f_m}_{\text{형성분율}}\cdot\underbrace{R_{inf}}_{\text{parent 입력속도}}}{\underbrace{CL(m)}_{\text{대사체 CL}}}
$$

#### 파라미터 해부 표

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $C(m)_{ss}$ | concentration | 정상상태 metabolite 농도 | $f_m$, $R_{inf}$, $CL(m)$ |
| $R_{inf}$ | amount/time | parent 입력속도 | infusion/dosing rate |
| $\tau$ | time | 투여간격 | dosing regimen |
| $AUC(m)_{single}$ | concentration·time | 단회 metabolite 노출 | first-pass/systemic formation |

> 🔑 **Oral metabolite 판독법:** first-pass formation과 systemic formation을 같은 입력으로 합치면 식별성이 무너집니다.
> ⚠️ **헷갈림 방지:** oral 단독 데이터는 두 형성 경로를 원리적으로 분리하지 못할 수 있습니다.

💡 **비유:** Oral metabolite 노출은 공항 입국장과 도심 도로 두 곳에서 동시에 들어오는 사람 수와 같습니다. 총 인원만 보면 어느 입구가 병목인지 알기 어렵습니다.

중첩 원리(superposition)에 의한 다회 경구 투여 시:

$$
\underbrace{C(m)_{av,ss}}_{\text{평균 Css}}=\frac{\underbrace{AUC(m)_{single}}_{\text{단회 노출}}}{\underbrace{\tau}_{\text{투여간격}}}
$$

정상상태 도달 시간은 rate-limiting 패턴에 따라 parent elimination 또는 metabolite elimination 중 더 느린 쪽이 결정한다 [T20 pp.670–673]. N-desalkylhalazepam에서 대사체 축적/감소는 parent보다 느리다. 정확한 timing은 현재 이 문서에 고정하지 않는다 `[T20 p.672; 확인 필요: figure-derived value]`. Carbamazepine autoinduction은 정성적 추세만 보존하며 — 용량 정규화 parent가 감소하고 대사체 관계가 변화하지만, 정확한 용량 범위는 고정하지 않는다 `[T20 p.676; 확인 필요]`.

**현장 팁(Trench-level tip)**: oral parent 단독 데이터만으로는 낮은 parent bioavailability와 대규모 first-pass metabolite formation을 항상 구분할 수 없습니다. Route 비교는 단순 bioavailability 계산을 넘어 진단 도구로 기능합니다.

---

> **M13 체화 핵심**
> ① `oral parent 후 metabolite가 보일 때` → first-pass와 systemic formation 분리가 결정
> ② `oral 단독 데이터 과해석` → identifiability 실패
> ⚡ `정상상태 축적 경시` → active metabolite 라벨 wording 실패

<!-- SLIDE_START: M14 | title: M14. 신장애 활성 대사체 시나리오와 상호전환(Renal impairment active-metabolite scenario + interconversion) -->

### M14. 신장애 활성 대사체 시나리오와 상호전환(Renal impairment active-metabolite scenario + interconversion)

> **앞 카드에서 이 카드로:** M13의 정상상태 metabolite 개념은 신장애에서 active metabolite가 전체 위험을 지배하는 최종 시나리오로 수렴합니다.

> **거장의 시각**
> 💢 **흔한 오해:** 대부분은 $f_m$이 작으면 metabolite 위험도 작다고 생각한다.
> ✅ **실제는:** 실제 위험은 형성분율보다 대사체 $CL(m)$이 신장애에서 얼마나 붕괴하는지가 결정한다.
> 🎯 **체화할 단 하나의 직관:** 작은 형성 경로도 제거 경로가 닫히면 전체 활성 노출의 지배 경로가 된다.

#### A. 형식적 정의 + 핵심 수식

**핵심 아이디어(Big Idea)**: Active metabolite가 존재할 때, parent $f_e$ 하나만으로는 신부전 용량 결정을 내릴 수 없습니다. 가장 위험한 상황이 반드시 'parent가 주로 신배설되는' 경우인 것은 아닙니다. 'Parent가 일부 대사되어 생성된 active metabolite가 그 자체로 신배설을 받는' 경우도 동일하게 위험합니다.

**Tozer 풀이 시나리오** [T20 pp.673–675; Fig 20-10; Table 20-4]

정상 신기능 예시:

| 파라미터 | Parent drug | Active metabolite |
|---|---:|---:|
| 전체 CL | 30 L/h | 10 L/h |
| 신장 CL | 15 L/h | 8.5 L/h |
| Parent 경구 F / 형성 분율 | $F=0.8$ | $f_m=0.3$ |
$$
\underbrace{F=0.8}_{\text{경구 F}},\qquad \underbrace{f_m=0.3}_{\text{형성분율}}
$$

#### 파라미터 해부 표

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---:|---|---|
| $F$ | fraction | 경구 bioavailability | absorption, first-pass |
| $f_m$ | fraction | active metabolite 형성분율 | metabolic pathway share |
| $CL(m)$ | L/h | active metabolite 제거능 | renal impairment, anuria |
| dose ratio | ratio | 정상 총 활성 농도 유지 감량비 | parent+metabolite combined exposure |

> 💡 **위험의 중심 이동** — 신장애에서는 parent보다 active metabolite가 전체 활성을 지배할 수 있습니다.
> 🔑 **방어 논리 규칙:** parent-only 감량은 scenario (3)을 닫지 못하므로 combined exposure 또는 monitoring 논리가 필요합니다.

경구 10 mg/h 투여 시, 정상 상태 총 활성 농도는 parent 0.27 mg/L + 대사체 0.24 mg/L = 0.51 mg/L이다 [T20 pp.673–674]. 무뇨 상태에서 parent는 약 2배 증가하지만, 대사체는 약 13배까지 증가할 수 있습니다. 정상 총 활성을 맞추기 위한 용량비(dose ratio)는 약 0.14이다 [T20 p.674].

**시나리오 규칙** [T20 p.675]

1. 대사체 형성이 parent의 주요 제거 경로이고 대사체가 활성인 경우, 용량은 대사체 clearance를 기준으로 설정해야 할 수 있습니다.
2. Parent의 신배설이 주요 경로이고 대사체 형성이 부차적인 경우, parent 노출이 지배적입니다.
3. 대사체 형성 비율이 작지만 대사체 제거가 거의 신배설에만 의존하고 대사체가 활성인 경우, 신부전에서 대사체가 전체 활성을 지배할 수 있습니다.

**Interconversion** [T20 pp.676–679]

Interconversion(← 상호전환)은 parent와 대사체가 서로를 재생성할 수 있음을 뜻합니다. 따라서 metabolite 쪽 renal impairment가 parent의 apparent elimination까지 늦출 수 있습니다. Clofibric acid는 정성적 예시로 보존합니다. 그림에서 도출된 수치 앵커는 고정하지 않는다 `[T20 p.679; 확인 필요]`.

**혼동 지점(Confusion)**: 'minor metabolite pathway'는 'minor safety concern'과 같은 말이 아닙니다. 신부전에서 metabolite $CL(m)$이 붕괴하면, 작은 $f_m$이라도 주요 노출 경로가 될 수 있습니다.

---

> 📖 **교과서 그림 참조:** [Rowland & Tozer, p.674, Fig 20-10 and Table 20-4]
> M14의 위험은 parent exposure 상승보다 active metabolite exposure 상승이 훨씬 클 수 있다는 비대칭성입니다. Fig 20-10/Table 20-4는 parent-only dose adjustment가 왜 실패하는지 보여 주는 핵심 evidence object입니다.
> 확인 시점: 이 카드를 읽은 뒤 확인하세요.

---

#### M. Plausible Fallacy — 나비효과 연쇄

**오류:** "$f_m$이 작으면 metabolite는 minor concern입니다."  
**왜 그럴싸한가:** 정상 신기능에서는 metabolite mass balance가 $f_m\times Dose$로 들어오므로, 작은 $f_m$은 작은 metabolite 노출량처럼 보입니다.  
**나비효과:** active metabolite elimination이 거의 신배설이라면($f_e(m)\approx1$), 무뇨 상태에서 $CL(m)$이 거의 0으로 무너짐 → Tozer worked example에서 $f_m=0.3$임에도 metabolite Css 약 13배 상승 [T20 pp.673–675] → [임상] parent-only 감량 후 active metabolite 독성 농도 미예측 → [모델링/규제] combined exposure 재계산, ESRD metabolite PK 재분석, label defense logic 보완 요구.  
**Detection signature:** parent CL은 신기능 비례로 감소하지만 metabolite Css가 10배 이상 상승하는 비대칭 패턴.  
**Defense:** Combined exposure(parent + active metabolite, equipotent or potency-weighted)을 정상 수준으로 맞추는 dose ratio를 별도로 계산해야 합니다.

> **M14 체화 핵심**
> ① `신장애 + active metabolite` → parent+metabolite combined exposure가 결정
> ② `minor pathway vs minor concern 혼동` → 작은 $f_m$의 위험을 과소평가
> ⚡ `parent-only 감량` → [임상] metabolite 독성 농도 미예측 + [규제] ESRD PK 재분석 요구

<!-- SLIDE_START: §5 | title: §5 혼동 쌍(Confusion Pairs) — 반드시 분리해야 하는 개념 쌍 -->

## §5 혼동 쌍(Confusion Pairs) — 반드시 분리해야 하는 개념 쌍

### 쌍 1(Pair 1). $CL$, $CL_R$, $f_e$

#### 2×4 혼동 분리 매트릭스

| 비교 기준 | $CL$ | $CL_R$ / $f_e$ |
|---|---|---|
| 단위 / 차원 | L/h, 전체 전신 청소율 | $CL_R$: L/h; $f_e$: fraction |
| 수식 내 위치 (분자/분모/지수) | $CL=CL_R+CL_H+CL_{other}$의 합 | $f_e=CL_R/CL$; $CL_R=f_e\cdot CL$ |
| 변화 원인 (생물학적/병적) | renal + nonrenal pathway 전체 | 신기능, urine route, filtration/secretion/reabsorption |
| 혼동 시 임상 결과 | total CL 전체에 renal covariate 적용 | nonrenal clearance까지 줄어 systematic underestimation |

> **⚡ 기억 고리 — [TEXTBOOK_DERIVED]**: $f_e$는 "renal pathway의 지분"이다 — $CL_R=f_e\cdot CL$은 곱셈 분해이지 비례 단축이 아닙니다. 신부전 covariate는 $CL$ 전체에 곱하지 말고 $CL_R$ 위치(분해된 자리)에만 곱해야 합니다.

### 쌍 2(Pair 2). ARE 플롯 vs 배설속도 플롯(ARE plot vs Excretion-rate plot)

#### 2×4 혼동 분리 매트릭스

| 비교 기준 | ARE plot | Excretion-rate plot |
|---|---|---|
| 단위 / 차원 | 잔여 누적량 로그 | 구간 배설속도 로그 |
| 수식 내 위치 (분자/분모/지수) | $\ln(X_{u,0-\infty}-X_u)$ | $\ln(dX_u/dt)$ |
| 변화 원인 (생물학적/병적) | $X_{u,0-\infty}$ 추정, 누적 편향 | collection interval, pH/flow, bladder emptying |
| 혼동 시 임상 결과 | 평활된 누적량을 시간 변동 없음으로 오인 | sampling artifact를 구조 모델로 오인 [G p.51] |

> **⚡ 기억 고리 — [AUDIT_DERIVED]**: Rate plot은 *시간 정보를 노출*하고, ARE plot은 *누적량으로 평활*합니다. 두 plot의 slope가 달라지면 모델 구조(compartment 수)가 아니라 sampling design (collection interval, bladder emptying, urine pH/flow)을 먼저 의심합니다.

### 쌍 3(Pair 3). 혈장 $CL$ vs 혈액 $CL_b$ (Plasma $CL$ vs Blood $CL_b$)

#### 2×4 혼동 분리 매트릭스

| 비교 기준 | Plasma $CL$ | Blood $CL_b$ |
|---|---|---|
| 단위 / 차원 | plasma concentration 기준 L/h | blood concentration 기준 L/h |
| 수식 내 위치 (분자/분모/지수) | $CL=Dose/AUC_{plasma}$ | $CL_b=CL\cdot C/C_b$ |
| 변화 원인 (생물학적/병적) | plasma binding, plasma measurement | hematocrit, RBC partition, $C/C_b$ |
| 혼동 시 임상 결과 | $CL/Q_H$로 false-high extraction | $E_H=CL_b/Q_H$를 놓쳐 DDI 해석 실패 [T5 pp.124–128; TD pp.775–776] |

> **⚡ 기억 고리 — [TEXTBOOK_DERIVED]**: $E_H=CL_b / Q_H$이지 $CL / Q_H$가 아닙니다. $R=C/C_b<1$인 약물에서 plasma 기준 비교를 하면 같은 약물이 false-high extraction으로 분류되어 임상·DDI 해석이 통째로 틀어진다 — App.D bridge 없이 organ extraction을 말하지 않는다.

### 쌍 4(Pair 4). $f_u$ vs $f_{ub}$

#### 2×4 혼동 분리 매트릭스

| 비교 기준 | $f_u$ | $f_{ub}$ |
|---|---|---|
| 단위 / 차원 | plasma 내 unbound fraction | blood 내 unbound fraction |
| 수식 내 위치 (분자/분모/지수) | plasma binding 식 | well-stirred의 $f_{ub}\cdot CL_{int}$ |
| 변화 원인 (생물학적/병적) | albumin/AAG, displacement | $f_u$ + $C/C_b$ 변환 |
| 혼동 시 임상 결과 | plasma 분율을 blood 식에 직접 대입 | hepatic extraction과 PBPK 입력 단위 오류 [TD pp.775–776] |

> **⚡ 기억 고리 — [TEXTBOOK_DERIVED]**: Plasma 식에서 blood 식으로 옮길 때 $R=C/C_b$를 곱합니다. $f_u$와 $f_{ub}$는 *분모가 다른 두 측정량*이지 동일 변수의 별명이 아니다 — 이 한 곱이 빠지면 well-stirred 분자($f_{ub}\cdot CL_{int}$)가 통째로 잘못된 단위에서 평가됩니다.

### 쌍 5(Pair 5). 고추출 IV vs 고추출 경구(High extraction IV vs High extraction oral)

#### 2×4 혼동 분리 매트릭스

| 비교 기준 | High extraction IV | High extraction oral |
|---|---|---|
| 단위 / 차원 | systemic $CL\approx Q_H$ | first-pass bioavailability/AUC |
| 수식 내 위치 (분자/분모/지수) | 혈류 제한 항 | $F$, first-pass, $f_{ub}CL_{int}$ 민감 항 |
| 변화 원인 (생물학적/병적) | hepatic blood flow | enzyme induction/inhibition, first-pass formation |
| 혼동 시 임상 결과 | IV DDI 음성을 oral 안전으로 오판 | route-dependent DDI와 metabolite formation 위험 누락 [G pp.83–85; T20 pp.665–669] |

> **⚡ 기억 고리 — [TEXTBOOK_DERIVED]**: IV에서는 $Q_H$ 천장(flow-limited)이 enzyme 변화를 가린다. Oral에서는 first-pass의 $f_{ub}\cdot CL_{int}$ 민감도가 그 천장을 풀어줍니다. **IV negative DDI는 oral safety의 보장이 아니다** — route를 바꾸는 순간 같은 enzyme 변화가 다른 endpoint로 표현됩니다.

---

### 쌍 6(Pair 6). Well-stirred vs 확장/투과성 제한 모델(Well-stirred vs extended/permeability-limited model)

#### 2×4 혼동 분리 매트릭스

| 비교 기준 | Well-stirred | Extended/permeability-limited |
|---|---|---|
| 단위 / 차원 | rapid equilibration 가정 | membrane/transporter 병목 포함 |
| 수식 내 위치 (분자/분모/지수) | $f_{ub}CL_{int}$ | $f_{ub}\rho CL_{int}$ 또는 uptake/efflux 단계 |
| 변화 원인 (생물학적/병적) | blood flow, binding, enzyme | uptake permeability, transporter, efflux |
| 혼동 시 임상 결과 | 낮은 $CL_{int}$처럼 오인 | transporter/permeability covariate 누락 [TE pp.778–779] |

> **⚡ 기억 고리 — [TEXTBOOK_DERIVED]**: Well-stirred는 "cell 안팎이 즉시 평형"이라는 가정입니다. $\rho<1$이면 *enzyme이 아니라 membrane*이 병목이며, IVIVE의 $CL_{int}$ 부족처럼 보이는 mismatch가 실제로는 transporter/permeability term 누락입니다. $\rho\to1$이 회복되는 조건은 passive diffusion이 $CL_{int}$보다 충분히 클 때다.

### 쌍 7(Pair 7). 단일점 $CL_{int}$ vs Michaelis–Menten 정보(Single-point $CL_{int}$ vs Michaelis–Menten information)

#### 2×4 혼동 분리 매트릭스

| 비교 기준 | 단일점 $CL_{int}$ | Michaelis–Menten 정보 |
|---|---|---|
| 단위 / 차원 | 한 농도 rate의 압축값 | 농도-속도 곡선 정보 |
| 수식 내 위치 (분자/분모/지수) | $CL_{int}$ 하나로 입력 | $V_{max}$, $K_m$, free concentration |
| 변화 원인 (생물학적/병적) | 측정 농도 선택, scaling | saturation, enzyme capacity, transporter uptake |
| 혼동 시 임상 결과 | 곡선 정보 소실 후 정교한 모델 적용 | IVIVE 예측 실패와 FIH CL mismatch [G pp.85–89] |

> **⚡ 기억 고리 — [TEXTBOOK_DERIVED]**: 한 농도에서의 rate를 그대로 $V_{max}/K_m$로 쓰는 것은 **곡선을 버린 다음 분수식을 정교화**하는 셈입니다. Saturation, free concentration, MMP scaling, transporter-mediated uptake 중 어느 하나라도 누락되면 그 위에 어떤 hepatic model을 얹어도 입력 정보가 이미 collapse되어 있어 회복되지 않는다.

### 쌍 8(Pair 8). 형성 율속 vs 제거 율속 대사체(Formation-rate-limited vs elimination-rate-limited metabolite)

#### 2×4 혼동 분리 매트릭스

| 비교 기준 | Formation-rate-limited | Elimination-rate-limited |
|---|---|---|
| 단위 / 차원 | parent가 metabolite terminal slope 지배 | metabolite own elimination 지배 |
| 수식 내 위치 (분자/분모/지수) | $k \ll k(m)$ | $k(m) \ll k$ |
| 변화 원인 (생물학적/병적) | 느린 parent disappearance/formation | 느린 metabolite clearance |
| 혼동 시 임상 결과 | parent 그림자를 metabolite half-life로 라벨링 | renal impairment 축적·multiple-dose 예측 실패 [T20 pp.659–662] |

> **⚡ 기억 고리 — [TEXTBOOK_DERIVED]**: **평행 감소이면 metabolite는 parent의 그림자다.** 보고된 metabolite terminal $t_{1/2}$은 metabolite *자신의* 것이 아닐 수 있습니다. "Formation rate-limited"는 metabolite가 자신의 elimination 속도가 아니라 parent의 elimination 속도를 입고 사라지는 상태다.

> **▶ 치명적 타격 (Critical Blow) — [TEXTBOOK_DERIVED + AUDIT_DERIVED]**  
> 이 혼동을 품고 NDA 또는 임상 dosing decision을 강행했을 때: parent와 metabolite의 종말 $t_{1/2}$이 같다는 보고가 metabolite 자체의 elimination 특성을 나타내지 *않는다*. Sponsor가 metabolite의 IV 단독 시험 없이 "metabolite half-life는 X시간"이라 명시하면, 이는 system-level terminal slope에 metabolite 라벨을 붙인 것입니다. 그 결과 (a) renal impairment에서 metabolite 축적 외삽이 빗나가고, (b) multiple-dose accumulation 예측이 빗나가며, (c) dose-response timing 평가가 동시에 빗나간다. Audit T4에서 "Sequential chain에서는 fastest k가 결정한다가 아니라 downstream substance의 terminal decline은 가장 느린 step에 의해 지배된다"가 본 항목의 정확한 source statement다 [T20 pp.659–662; Audit MUST_FIX #5/T4-12].

### 쌍 9(Pair 9). $AUC(m)/AUC$ vs $f_m$

#### 2×4 혼동 분리 매트릭스

| 비교 기준 | $AUC(m)/AUC$ | $f_m$ |
|---|---|---|
| 단위 / 차원 | 노출비 | 형성분율 |
| 수식 내 위치 (분자/분모/지수) | $f_m\cdot CL/CL(m)$ | 형성항 단독 |
| 변화 원인 (생물학적/병적) | formation + metabolite clearance | metabolic pathway share |
| 혼동 시 임상 결과 | 낮은 ratio를 낮은 formation으로 단정 | $CL(m)$ 변화와 신장애 위험 누락 [T20 pp.662–665] |

> **⚡ 기억 고리 — [AUDIT_DERIVED]**: $AUC(m)/AUC<1$은 **하나의 식에 두 미지수**다 — $f_m$이 작아서일 수도, $CL(m)$이 커서일 수도, 둘 다일 수도 있습니다. $f_m$을 알지 못하면 $CL(m)/CL$ 부등식을 쓰지 않는다. Source-consistent inequality는 오직 $CL(m)>f_m\cdot CL$뿐입니다.

### 쌍 10(Pair 10). 순차 대사 vs 상호전환(Sequential metabolism vs interconversion)

#### 2×4 혼동 분리 매트릭스

| 비교 기준 | Sequential metabolism | Interconversion |
|---|---|---|
| 단위 / 차원 | 한 방향 대사 흐름 | 양방향 parent↔metabolite 흐름 |
| 수식 내 위치 (분자/분모/지수) | downstream chain | reversible transfer 항 |
| 변화 원인 (생물학적/병적) | 대사 경로 순차 진행 | 재생성, enterohepatic/재전환 가능성 |
| 혼동 시 임상 결과 | parent profile만으로 renal-safe 오판 | metabolite 신부전이 parent apparent elimination까지 지연 [T20 pp.676–679] |

> **⚡ 기억 고리 — [TEXTBOOK_DERIVED]**: Sequential은 *한 방향*, interconversion은 *양방향*입니다. 후자에서는 parent의 $f_e$가 작아도 metabolite 쪽 신부전이 parent의 *apparent* elimination까지 늦출 수 있다 — parent profile만 보고 "renal-safe"로 분류하면 mechanism을 놓친다.

혼동 쌍의 공통 메시지: **같아 보이는 두 숫자가 실제로는 서로 다른 분모(denominator), 투여 경로(route), 구획(compartment), 또는 율속단계(rate-limiting step)를 갖는다.**

---

---

<!-- SLIDE_START: §7 | title: §7 자기 검증(Self-Test) — 소크라테스식 딜레마 -->

## §7 자기 검증(Self-Test) — 소크라테스식 딜레마

### Q1. 청소율 정의

$CL=Dose/AUC$가 compartment model 없이도 성립하는 이유를 $Rate=CL\cdot C$의 시간 적분으로 설명하세요.  
**답 방향**: 총 제거량 = dose이고, $\int Rate\,dt=CL\cdot\int C\,dt$이므로 $CL=Dose/AUC$가 모델 독립적으로 성립합니다.

### Q2. 신장 분해

정상 $CL=10\ \mathrm{L/h}$, $f_e=0.6$인 약물에서 renal function이 25%로 떨어지고 nonrenal CL은 보존됩니다. 새 total CL은?  
**답 방향**: renal CL=6→1.5, nonrenal=4, total=5.5 L/h.

### Q3. 소변 플롯

Rate plot과 ARE plot의 slope가 다르고, rate plot에서 시간별 변동이 큽니다. 어떤 artifact 또는 physiology를 먼저 의심해야 합니까?  
**답 방향**: 수집 간격(collection interval), 방광 배출(bladder emptying), pH/소변 유량 변동(urine flow variation), $X_{u,\infty}$ 편향을 순서대로 점검합니다.

### Q4. Well-stirred 극한 근사

$Q_H=81\ \mathrm{L/h}$, $f_{ub}\cdot CL_{int}=20\ \mathrm{L/h}$이면 high/low/intermediate 중 어디에 가깝습니까? $f_{ub}$가 4배 증가하면?  
**답 방향**: 초기 $E=20/(81+20)=0.20$으로 낮은 편. $f_{ub}$가 4배이면 80이 되어 $E \approx 0.50$, 중간 수준으로 상승합니다.

---

### Q5. 혈장 CL vs 혈액 CL

Plasma $CL=60\ \mathrm{L/h}$, $C/C_b=0.5$, $Q_H=81\ \mathrm{L/h}$. $CL_b$와 extraction ratio는? Plasma CL만 쓰면 어떤 오류가 생깁니까?  
**답 방향**: $CL_b=30\ \mathrm{L/h}$, $E=0.37$. Plasma 기준으로 비교하면 실제보다 높은 extraction으로 분류되는 오류가 발생합니다.

### Q6. IVIVE 함정

한 substrate concentration에서 얻은 in vitro rate로 $CL_{int}$를 만들고 MMP 평균값 하나로 scaling했다. Phase 1에서 in vivo CL이 예측의 1/5입니다. 어떤 세 가지 원인을 우선 점검할 것인가?  
**답 방향**: 단일 농도 비선형성(single-point nonlinearity), 결합/비결합 농도 오류(binding/free concentration), MMP/scaling 변이, transporter/permeability 항 누락을 순서대로 확인합니다.

### Q7. 대사체 율속단계

Parent dosing 후 parent와 metabolite가 parallel terminal decline을 보입니다. 별도 metabolite dosing에서는 metabolite half-life가 더 짧다. 어떤 case입니까?  
**답 방향**: Formation rate-limited 상태다. Parent 투여 후 관찰되는 대사체 slope는 parent에 의해 지배됩니다.

### Q8. AUC 비

$AUC(m)/AUC=0.5$입니다. 이 값만으로 $f_m=0.5$라고 말할 수 있습니까?  
**답 방향**: 불가능합니다. $CL(m)/CL$이 필요합니다. 식은 $AUC(m)/AUC=f_m\cdot CL/CL(m)$입니다.

### Q9. 보스 딜레마(Boss Dilemma) — 신장애 + 활성 대사체(renal impairment + active metabolite)

Parent drug의 정상 $CL=30\ \mathrm{L/h}$, renal CL=15 L/h, oral $F=0.8$입니다. Active metabolite의 $CL(m)=10\ \mathrm{L/h}$, renal CL(m)=8.5 L/h, 형성 분율(formation fraction) $f_m=0.3$입니다. 무뇨(anuric) 상태에서 parent renal CL과 metabolite renal CL이 모두 0이 됩니다. Parent만의 용량 조정이 왜 불안전합니까?  
**답 방향**: Parent 노출은 약 2배 증가하지만, 대사체 CL은 10에서 1.5 L/h로 붕괴하며 Tozer 시나리오에서 형성 분율이 증가할 수 있습니다. 대사체 노출이 전체 활성을 지배할 수 있고, 원전 예시에서 약 13배 대사체 증가와 약 0.14의 용량비가 보고된다 [T20 pp.673–675].

> **전문가의 절충 판단(Master's Trade-off) — [EXPERT_INFERENCE]**  
> Q9에는 두 가지 *방어 가능한* 입장이 존재한다 — 어느 쪽을 택하든 그 결정은 라벨/CSR에서 어떻게 방어할 수 있는지를 함께 답해야 합니다.  
>  
> **(a) 통합 노출 기반 용량 조정(Combined-exposure dose adjustment).** Parent + active metabolite의 통합 활성을 정상 수준으로 맞추는 용량비(Tozer worked example의 약 0.14)를 적용합니다. *방어 논리*: 대사체가 parent와 equipotent에 가깝거나 potency-weighted sum이 독성 유발인자라면, 통합 Css를 기준점으로 삼는 것이 가장 보수적입니다. *Trade-off 비용*: parent 주도 치료 효과를 과소 투여(underdose)할 위험이 있습니다. 라벨 문구 요구: "based on combined active exposure".  
>  
> **(b) 2단계 모니터링(Two-tier monitoring).** Parent 용량은 parent CL 변화에만 맞추되, active metabolite TDM 또는 PK/PD biomarker로 안전 안내선을 운영합니다. *방어 논리*: parent와 대사체의 potency 차이가 분명하고, 대사체 분석법(assay)과 turnaround time이 가능하면 일률 감량보다 정밀합니다. *Trade-off 비용*: 분석법 검증, 채혈 설계, 조치 역치(action threshold)가 모두 라벨에 명시되어야 합니다.  
>  
> **두 입장 모두에서 방어 불가능한 것**: "parent $f_e$ 변화에 비례한 일률 감량" 단독. T20 p.675는 위 (1)/(2)/(3) scenario rule로 이를 수식적으로 차단합니다. Sponsor가 active metabolite의 ESRD PK를 측정하지 않은 상태에서 parent-only 비례 감량을 제출하면, scenario (3) 가능성을 닫지 못한 채 권고가 발행되는 것이며, 이것이 본 딜레마의 *진짜* 위험입니다.

---

---

<!-- SLIDE_START: §8 | title: §8 요약 & NONMEM/PopPK 교량 -->

## §8 요약 & NONMEM/PopPK 교량

### §8A. 학습 위계상 위치(Positioning) — 28-session arc 내 위치 — [EXPERT_INFERENCE]

본 세션은 PopPK 학습 위계의 **physiology layer spine**을 닫는 chapter다.

- **선행 의존성**: one-compartment IV/oral 동역학, AUC의 정의와 trapezoidal 적분, mass balance 적분 — 이전 세션의 기초 위에 본 세션이 *생리학적 분해*를 얹는다.
- **본 세션이 담당하는 자리**: "관찰된 $CL$/$t_{1/2}$/$AUC(m)/AUC$/$C/C_b$ 변화가 어느 생리학적 병목에서 왔는가"의 역추적 frame을 확립.
**본 세션이 열어주는 후속 영역**:

| 후속 세션 | 이 세션에서 열리는 개념 | 이 세션 없으면 실패하는 것 |
|---|---|---|
| PBPK 모델링 | well-stirred / extended clearance의 organ-level first principle | organ input을 empirical scalar로만 보정 |
| PopPK covariate selection | eGFR, $f_u$, transporter genotype, hepatic function score의 식 내 위치 | 통계적 유의성만으로 covariate 채택 |
| Parent–metabolite joint modeling | $f_m$, $CL(m)$, rate-limiting step의 identifiability spine | $F$와 $f_m$ product confounding |
| Renal/Hepatic impairment label | scenario rule 기반 dose/label wording | parent-only 또는 route-insensitive label 작성 |

### §8B. 선행 의존성(Dependencies) — 본 chapter를 대충 넘겼을 때의 후속 실패 모드 — [EXPERT_INFERENCE]

- **D1. Plasma↔Blood unit collapse**: App.D bridge 생략으로 hepatic $E_H$가 $R=C/C_b$만큼 systematic하게 빗나간다. 그 결과 high/low extraction 분류가 통째로 잘못되며, route-dependent DDI 해석이 빗나가고, PBPK input의 $f_{ub}\cdot CL_{int}$가 잘못된 단위에서 평가됩니다.
- **D2. f_e covariate misapplication**: $f_e$를 곱셈 분해가 아닌 비례 단축으로 다루어 신부전 covariate를 total $CL$ 전체에 곱하면, nonrenal pathway까지 같이 줄여 *systematic CL underestimation*이 발생. 시판 후 dose adjustment recommendation이 임상 안전성과 어긋난다.
- **D3. Metabolite identifiability failure**: rate-limiting step을 분리하지 않은 채 $f_m$/$CL(m)$/$V(m)$을 자유 추정하면 oral data만으로 $F$와 $f_m$이 product로만 들어가 식별 불가. NONMEM `$COV` step 실패 또는 RSE 폭증으로 표면화.
- **D4. Renal impairment scenario (3) miss**: 작은 $f_m$을 minor concern으로 분류하여 active metabolite의 ESRD PK를 측정하지 않으면, 라벨이 parent-only 감량을 권고하게 되고 metabolite 영역에서 oversaturation이 발생.

### §8C. 전문성 해자(Professional Moat) — 이 chapter를 진정으로 내면화한 연구자만이 갖는 것 — [EXPERT_INFERENCE]

NONMEM control stream을 작성하고 GOF plot을 만드는 일은 이미 자동화 영역에 가깝다. 본 chapter의 원리를 *구조적 이해*의 수준에서 내면화한 모델러는 그 자동화가 복제할 수 없는 것을 갖는다 — 관찰된 PK/PD signal을 *어느 생리학적 병목*에서 왔는지 역추적할 능력입니다. 구체적으로:

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| 수렴 실패 또는 GOF anomaly | 단위, 율속단계, $\rho$, interconversion | → | 구조 모델 과증식 또는 병목 오판 | §8D 4개 시그니처 순서로 점검 |
| Covariate 선택 회의 | eGFR, $f_u$, transporter genotype | → | 통계적 유의성만으로 생리학 위치 누락 | covariate가 들어갈 식의 자리를 먼저 명시 |
| Renal/Hepatic impairment 라벨 회의 | parent $CL$, $CL(m)$, combined exposure | → | parent-only 감량 또는 route 오류 | scenario rule과 defense logic을 라벨 문구로 연결 |

### §8D. 진단 시그니처 카탈로그(Diagnostic Signatures Catalog) — [EXPERT_INFERENCE]

본 catalog는 §6 Diagnostic Pathology 요건을 위해 추가된 4개의 진단 시그니처다. 모두 PART A의 source-anchored M card 위에서만 의미를 갖는다 — 본문 외부의 새로운 사실 주장이 아니라 본문 내용의 *failure mode 요약*입니다.

| ID | 시그니처 명칭 | Trigger pattern (관찰 신호) | 기계론적 원인 | Anchor card |
|---|---|---|---|---|
| **DS-1** | Phantom Plasma Clearance | 추정 $CL$이 $Q_H$ (≈81 L/h)를 초과하는 결과가 나옴 — 생리학적으로 불가능한 값 | Plasma $CL$을 그대로 organ flow와 비교한 단위 mismatch. $R=C/C_b<1$인 약물에서 발생. App.D bridge로 $CL_b=CL \cdot R$을 적용해야 함. | M8 (Plasma-to-blood ratio) |
| **DS-2** | Phantom Metabolite Half-life | metabolite의 추정 `k`가 parent의 `k`와 거의 동일하게 잡힘 | Formation rate-limited 상태에서 *terminal slope를 metabolite 자신의 slope로 오해*. Parent의 그림자가 metabolite 라벨을 입은 결과. Separate metabolite IV 또는 model-based formation rate fixing이 필요. | M11 (Rate-limiting step) |
| **DS-3** | Renal Covariate Asymmetry | metabolite의 CrCl power coefficient가 1.0에 가깝고 parent의 power는 작은 비대칭 | metabolite가 거의 신배설 ($f_e(m)\approx1$)인데 parent의 $f_e$는 작은 시나리오 — Tozer Scenario (3)의 직접 신호. Active metabolite renal impairment risk가 parent-only 보정으로는 검출되지 않음. | M14 (Renal impairment + active metabolite) |
| **DS-4** | Permeability Rate-Limited Mismatch | hepatic clearance covariate로 $f_u$를 넣었으나 모든 cohort에서 비유의/계수 ≈ 0; IVIVE에서 $CL_{int}$만 5–10배 underestimate | Transporter substrate에서 $\rho<1$ 상태. $f_u$보다 uptake permeability/transporter genotype이 dominant covariate일 가능성 — basic well-stirred의 rapid equilibration 가정이 무너짐. | M9, M10 (Permeability/Extended clearance) |

### §8E. NONMEM/PopPK 구현 교량(Implementation Bridge) `[교과서 외 해석 — source equations 기반]`

| 원전 개념 | PopPK 구현 시사점 |
|---|---|
| $CL=CL_R + CL_H + CL_other$ | 신기능 covariate를 total $CL$에 무차별 적용하지 말고 경로별(route-specific) 구성요소에 적용합니다. |
| $CL_R=f_e\cdot CL$ | 소변 데이터(urinary data) 또는 외부 $f_e$ 정보가 없으면 신장 분율을 과해석하지 않는다. |
| PK5 혈장+소변 동시 적합 | `DVID`/endpoint별 잔차오차(residual error)로 혈장과 소변 데이터를 동시에 적합(fit)합니다. |
| $CL_b=CL\cdot C/C_b$ | 간 extraction 또는 PBPK 입력에는 혈액 기준 청소율(blood-based clearance)을 사용합니다. |
| well-stirred + App.E $\rho$ | 수송체 기질(transporter substrate)에서는 $CL_{int}$ covariate보다 uptake/permeability covariate 가능성을 먼저 점검합니다. |
| $AUC(m)/AUC=f_m\cdot CL/CL(m)$ | 대사체 모델에서 $f_m$, $CL(m)$, $V(m)$의 식별가능성(identifiability)을 투여 경로/용량/대사체 데이터로 확인합니다. |
| 율속단계(rate-limiting step) | 대사체 terminal slope를 곧바로 대사체 자신의 $t_{1/2}$로 쓰지 않는다. |
| 신부전 활성 대사체 | parent와 대사체의 통합 노출(combined exposure)을 라벨/용량 시나리오 민감도로 계산합니다. |

### §8F. 한 페이지 요약(One-page Recap)

**한 페이지 요약(One-page recap)**

1. $CL$은 농도로 정규화한 제거 능력이다 — 제거 속도 자체가 아니다 [G p.49; T5 pp.124–128].
2. $t_{1/2}$은 $V/CL$에서 파생된 결과값입니다. $CL$과 $V$를 먼저 분해하지 않고 $t_{1/2}$만 해석하지 않는다 [T5 pp.148–150].
3. $CL_R=f_e\cdot CL$이지만, renal clearance 자체는 filtration + secretion − reabsorption이며, urine pH와 flow가 이 값을 변화시킨다 [G pp.48–56; T5 pp.138–148].
4. Well-stirred hepatic clearance는 $Q_H$, $f_{ub}$, $CL_{int}$가 결정합니다. High/low extraction은 극한 근사값이지, 약물에 영구히 붙는 라벨이 아니다 [G pp.79–85; T5 pp.130–135].
5. 장기 extraction 계산에서 plasma concentration은 blood concentration으로 변환해야 합니다. App.D가 이 변환의 mass-balance 교량을 제공한다 [TD pp.775–776].
6. IVIVE는 in vitro 입력이 이미 정보를 잃었을 때 실패한다 — single-point $CL_{int}$, 부적절한 scaling, 또는 permeability/transporter 항 누락이 대표적이다 [G pp.85–90; T5 pp.136–138; TE pp.778–779].
7. Parent–metabolite 시스템은 $f_m$, $CL(m)$, rate-limiting step을 따로 파악해야 합니다. $AUC(m)/AUC$는 $f_m$ 그 자체가 아니다 [T20 pp.659–665].
8. 신부전 용량 조정은 parent $f_e$만이 아니라, active metabolite clearance를 별도로 평가해야 한다 [T20 pp.673–679].

---

## v3.7 출력 후 자가검증 체크리스트

| 항목 | 기준 | 결과 |
|---|---|---|
| SLIDE_START 개수 | §섹션수 + 카드수 합산 | 19 개 |
| 카드당 callout 합계 ≤ 6 | 전체 카드 | ✓ |
| [E] 박스 존재 | 모든 §2 카드 | ✓ |
| [D] 거장의 시각 존재 | 모든 §2 카드 | ✓ |
| [L] 파라미터 표 존재 | Apex 카드 + 정의 수식 카드 | ✓ |
| §5 혼동 쌍 표 행 순서 고정 (4행) | §5 전체 | ✓ |
| 기호 일관성 | 첫 등장 기준 통일 | ✓ |
| PART B 흔적 없음 | 전체 | ✓ |
| 수치 anchor 보존 | Compound A 등 원본 수치 | ✓ |
| [M] 나비효과 이중 종착점 | Apex 카드 전체 | ✓ |

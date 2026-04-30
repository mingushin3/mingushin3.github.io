---
title: "I-07 비선형 PK — 비선형이 보이면 '방향'을 먼저 읽어라"
subtitle: "거장의 시각 통합본 (검증·정정·심화 v2.0)"
sources:
  - "Rowland & Tozer 5e Ch.16 (pp.491–529)"
  - "Gabrielsson & Weiner 5e §2.7.1–2.7.5, PK17, PK21"
session: "I-07"
volume: "Vol I — 임상 이론 + 데이터 이론 혼합"
apex_concept: "Michaelis-Menten 소실 동역학"
critical_blow: "Vmax vs Km — Css 민감도의 비대칭성"
data_anchors:
  - "G&W PK17: Agent X, Vmax=107 µg/min, Km=0.56 µg/mL"
  - "G&W PK21: NT-Pb, kout t½=158 h"
  - "R&T Table 16-3: Alcohol Vm=10 g/hr, Km=100 mg/L"
  - "R&T Fig 16-10: Phenytoin Km'=4 mg/L, Vm=500 mg/day"
  - "R&T Fig 16-18: Cefonicid 30 mg/kg IV (Dudley 1986)"
  - "R&T Table 16-6: Salicylate urinary recovery (Levy 1965)"
  - "R&T Table 16-2: Nicardipine F (Wagner 1987)"
errata_v2:
  - "[정정] NONMEM $ERROR 블록: SIGMA는 분산이므로 SQRT(SIGMA*IPRED²+SIGMA) — **2 제거"
  - "[정정] Table 16-12 IV 고추출비+fu↑ 행: ↓↓가 아닌 Css↔, Cu,ss↑"
  - "[정정] PK17 −0.96 상관: 'identifiability 실패'가 아닌 G&W 원문대로 '상관은 높지만 정밀도는 양호'"
  - "[추가] Bupivacaine — IV 고추출비 좁은 치료역에서 단백결합이 임상적으로 유일하게 의미 있는 예외 (G&W p.134)"
  - "[추가] R&T Fig 16-8 vignette: 5-hr infusion이면 zero-order paradox에서 AUC=0이 가능하다"
  - "[추가] AUC/Dose vs Dose 4가지 패턴 (G&W §2.7.1)"
tags: [pharmacometrics/pk/nonlinear, clinical/TDM, nonmem/DES/ADVAN13, P3_Audit]
filing: "01_ZETTELKASTEN/013_PopPK-NONMEM/ + 02_LITERATURE/024_Gabrielson-Textbook/"
---

# ✦ I-07 비선형 PK: 비선형이 보이면 "방향"을 먼저 읽어라

> **소스**: Rowland & Tozer 5e Ch.16 (pp.491–529) + Gabrielsson & Weiner 5e §2.7.1–2.7.5, PK17, PK21
> **감지된 소스 유형**: Vol I 혼합 (R&T 임상 기전 + G&W 수식·데이터)
> **버전**: v2.0 — 1차 검증본 오류 정정 + 누락 핵심 예시 통합

---

## 🗺️ 이 세션을 읽기 전에 — 거장이 먼저 보는 풍경

> **두 장면을 떠올려 보세요.**
>
> **장면 1.** 페니토인(항경련제)을 300 mg/day로 2주 썼는데 효과가 없습니다. 500 mg/day로 올렸더니 20일 후 혈중농도가 4 mg/L → **36 mg/L** (9배). 환자는 안구진탕·운동실조로 응급실에 옵니다. **용량 67% 증량 → 농도 9배.** [R&T p.491 도입부 임상 vignette]
>
> **장면 2.** 비타민 C를 75 mg/day → 10,000 mg/day(**133배**)로 올렸더니 혈중농도는 9 → 19 mg/L(2배). 그런데 신장 청소율은 0.5 → 21 mL/min으로 **42배** 증가했습니다. 용량을 100배 넘게 올려도 농도는 거의 안 변하는 자기조절(homeostasis). [R&T p.492]
>
> **이 두 정반대 현상이 같은 원인에서 옵니다.** 둘 다 superposition(중첩 원리) 붕괴이며, 단지 **붕괴의 방향이 반대**일 뿐입니다. I-07은 그 '방향'을 체계적으로 읽어내는 법을 가르칩니다.

---

## §1 — 세션 헤더 & 로드맵

### Big Idea (한 문장)

비선형 PK는 "농도가 폭발하는 이상한 현상"이 아니라, **dose-normalized 관찰값이 superimpose하지 않는 구조적 붕괴**이며, 그 붕괴의 **방향**($F$↑/$F$↓ · $CL$↑/$CL$↓ · $V$↑/$V$↓)을 먼저 읽어내는 것이 수석 모델러의 첫 번째 임무다.

> 💡 **"superimpose한다"가 무슨 뜻인가?**
> 100 mg과 200 mg 투여 후의 농도-시간 곡선을 각각 용량으로 나눠 겹쳐 그렸을 때 두 곡선이 **딱 포개지면** 선형(linear) PK입니다. 200 mg에서 모든 시점의 농도가 정확히 2배라는 뜻이니까요. 이것이 **중첩 원리(principle of superposition)**입니다 [R&T p.492 정의]. 이게 깨지면 비선형입니다.

---

### 개념 항법도 — 세 개의 레이어

```
[레이어 1] 진단 프레임워크 — "비선형을 어떻게 알아보는가"
  └ EDA 5단계, AUC/Dose vs Dose 패턴 (G&W §2.7.1)
  └ R&T 4단계 워크플로우, R&T Table 16-1 비선형 카탈로그
  └ C50 vs Km 위치 관계 — "왜 대부분 PK는 선형인가" (R&T Fig 16-3)

[레이어 2] 기전별 수식과 사례 — "각 방향이 어떤 임상 약물에서 오는가"
  └ Michaelis-Menten 소실 ⚡ Apex (Phenytoin, Alcohol, PK17 Agent X)
  └ 입력속도 Catastrophe (Phenytoin pseudosteady-state, Alcohol zero-order paradox)
  └ Saturable first-pass — F↑ 역방향 (Nicardipine, Methylphenidate)
  └ 신배설 비선형 (Penicillin/Dicloxacillin↓, Ascorbic acid↑)
  └ 단백·조직결합 비선형 (Cefonicid, Salicylate, Bosentan/TMDD)
  └ 시간 의존성 (Carbamazepine 자가유도, Clarithromycin MBI, NT-Pb 이종유도)

[레이어 3] 종합 진단 도구 — "현장에서 어떻게 적용하는가"
  └ Salicylate 4단계 완전 적용 (R&T pp.519–523)
  └ IV vs Oral 방향성 종합 정리 (R&T pp.511–512, 523–524 본문)
```

### 지식 그래프 위치

```
[선행]                              [I-07]                          [후속]
I-01 CL · V 기본          ─→     비선형 PK         ─→        I-08 TMDD
I-03 1구획 ODE                 (선형→비선형 관문)              I-09 Emax PD
I-05 단백결합 기초                                              I-10 Indirect Response
I-06 추출비/혈류 의존                                            II-04 ADVAN13 / $DES
```

> 이전 세션들이 "평평한 고속도로"를 달리는 법을 가르쳤다면, I-07은 그 도로가 **갑자기 경사지고 굽어지는 구간**에서 어떻게 판단하는지를 가르칩니다.

---

## §2 — 개념 해부 카드

---

### 🃏 카드 1. 진단학으로서의 비선형 PK — 거장이 먼저 보는 좌표계

#### ━━ [거장의 시각: 왜 이 카드가 가장 먼저인가] ━━

**왜 치명적으로 중요한가:** 비선형을 보면 많은 사람이 반사적으로 "대사 포화 → CL↓"를 떠올립니다. 그러나 R&T Table 16-1은 **여섯 방향**을 명시합니다 — 그중 **$F$↑(saturable first-pass)는 정반대 방향**의 비선형입니다. 이 한 가지 오해만으로도 고용량 임상시험 설계가 완전히 뒤집힙니다 (Nicardipine 사례).

**체화해야 할 단 하나의 직관:** 비선형이 관찰되면, 첫 질문은 *"왜 폭발했는가?"*가 아니라 **"dose-normalized값이 어느 방향으로 superimpose를 실패했는가?"**입니다. 방향이 기전을 결정하고, 기전이 임상 처방·규제 문서를 결정합니다.

---

#### A. 정의 — 선형 vs 비선형의 정확한 경계

> **중요한 전제:** 동일 투여 경로 · 동일 제형 · 동일 투여 방법으로 다른 용량을 비교해야 합니다. 경로/제형이 다르면 superimpose 실패는 그냥 방법 차이이지 비선형이 아닙니다 [R&T p.492].

$$\text{선형(Linear)} \;=\; \text{dose-normalized 농도 · AUC · 소변 회수율이 모든 시점에서 superimpose}$$

$$\text{비선형(Nonlinear)} \;=\; \text{superimpose 실패} \;=\; \text{하나 이상의 PK 파라미터가 용량/농도/시간에 따라 변함}$$

**시간 의존성의 정의 — Levy [1982]** [G&W §2.7.1, p.112 인용]:
> *"진정한 시간 의존성 시스템이라면, 약물 농도가 시간 불변인 상태에서 청소율이 시간과 함께 변해야 한다."*

> 💡 **핵심 구분:** 농도 변화 때문에 CL이 변하면 → **용량(capacity) 의존성**. 농도와 무관하게 시간이 지나면서 CL이 변하면 → **시간(time) 의존성**. 둘 다 동시 발생도 가능 (예: 알코올). 원인·임상 결과·NONMEM 모델 구조가 모두 다릅니다.

---

#### B. Gabrielsson EDA 5단계 — 데이터를 받으면 이 순서로 그려라

**G&W §2.7.1의 핵심 조언:** 모델을 세우기 전에 반드시 그림부터 그려라.

1. **Linear plot** → 전체 패턴 확인
2. **Semi-log plot** → 기울기가 일정한지(선형) vs 시간에 따라 변하는지(비선형)
3. **Dose-normalized C-time plot** → 다른 용량 곡선이 겹치는지 — superposition 직접 검증
4. **AUC vs Dose** → 선형이면 직선 (원점 통과)
5. **AUC/Dose vs Dose** ← **가장 결정적 그래프** [G&W Fig 2.86, p.113]

> 💡 **AUC/Dose vs Dose 패턴 4가지 — 비선형의 시각적 지문(fingerprint):**
>
> | 패턴 | 의미 | 대표 약물 |
> |---|---|---|
> | **수평선 (flat)** | 선형 PK — 정상 | 대부분의 약물 |
> | **단조 상승** | $CL$↓ (또는 $F$↑) → 농도가 올라갈수록 효율 떨어짐 | Phenytoin (MM), Nicardipine (saturable first-pass) |
> | **단조 감소** | $CL$↑ (또는 $F$↓) → 농도가 올라갈수록 청소 가속 | Carbamazepine (자가유도), Amoxicillin (흡수 포화) |
> | **저용량 상승 후 plateau** | MM + 1차 병렬 경로 혼합 | Salicylate |

---

#### C. R&T Table 16-1 — 비선형이 올 수 있는 모든 과정의 지도

> 이 표는 세션 전체의 **목차**입니다. 각 행이 이후 카드에서 깊게 다뤄집니다.

| 과정 | 기전 | PK 파라미터 방향 | 대표 약물 |
|---|---|---|---|
| 용해도 | Limited solubility | $F$↓ | Griseofulvin |
| 장관 능동수송 | Saturable active absorption | $F$↓ | Amoxicillin |
| **Efflux transport 포화** | P-gp 포화 → 흡수 증가 | **$F$↑** | Protease inhibitors, fexofenadine |
| P-gp induction | Time-dependent ↑ | $F$↓ | Tipranavir |
| 신 분비 포화 | Tubular secretion 포화 | $CL_R$↓ | Penicillin G, Dicloxacillin |
| 신 재흡수 포화 | Active reabsorption 포화 | $CL_R$↑ | Ascorbic acid |
| 담즙 분비 | Biliary secretion 포화 | $CL_H$↓ | Sulfates, glucuronides |
| 대사 포화 | Capacity-limited | $CL$↓ | **Phenytoin**, paroxetine, voriconazole |
| **Saturable first-pass** | 초회통과 대사 포화 | **$F$↑** | **Nicardipine**, mesalamine, niacin |
| 자가유도 | Autoinduction (time-dep) | $CL$↑ | Carbamazepine |
| MBI(자가억제) | Suicide substrate (time-dep) | $CL$↓ | Clarithromycin, ticlopidine, clopidogrel |
| 단백결합 포화 | Saturable plasma binding | $V$↑, $CL$ ↑/↔ (E에 따름) | Salicylate, disopyramide, naproxen |
| 수용체 결합 포화 | TMDD | $V$↓ | **Bosentan**, imirestat, draflazine, mitoxantrone |

[출처: R&T 5e, Ch.16, Table 16-1, p.496]

> ⚠️ **Efflux transport 포화 함정:** P-gp 같은 efflux transporter는 약물을 다시 장 안으로 밀어냅니다. 이게 포화되면 흡수가 **증가**합니다($F$↑). 용량이 늘수록 AUC가 "더 많이" 증가하는 역방향 비선형 — 대사 포화($F$↓)와 정반대 방향이므로 혼동하면 임상시험 설계가 거꾸로 갑니다.

---

#### D. R&T 4단계 비선형 인식 워크플로우

> 이 4단계를 밟으면 어떤 비선형 약물도 체계적으로 분석할 수 있습니다. (카드 10에서 salicylate로 완전 적용)

**Step 1.** Dose-normalized 비교 → superimpose 실패 확인 ("비선형인가?")
**Step 2.** 변화한 파라미터의 **방향** 식별 ("무엇이, 어느 방향으로?")
**Step 3.** Primary PK 파라미터 결정 → $CL_H$, $CL_R$, $V$, $K_a$, $F$, $f_u$ 중 어느 것?
**Step 4.** 가정된 기전과 관찰 일치 여부 확인 ("설명이 되는가?")

[출처: R&T 5e, Ch.16, p.519]

---

#### G. Zettelkasten Atom

```yaml
aliases: [비선형 PK 진단, superposition 붕괴, dose-dependent kinetics]
tags: [pharmacometrics/pk/nonlinear, clinical/TDM, methodology/EDA]
source: "R&T 5e, Ch.16, pp.491–496, 519–521; G&W 5e, §2.7.1, pp.112–113"
```

비선형 PK 진단의 핵심은 superposition 붕괴의 **방향** 읽기다. AUC/Dose vs Dose 그래프 기울기 방향(평·↑·↓·plateau)이 1차 단서이며, R&T 4단계 워크플로우가 체계적 역추론의 도구다. 첫 반사가 "대사 포화"여서는 안 된다 — 여섯 방향(F↑↓·CL↑↓·V↑↓) 중 어느 것인지 먼저 묻는다.

---

### 🃏 카드 2. C50 vs Km 위치 관계 — "왜 대부분 PK는 선형이고 PD는 항상 비선형인가"

#### ━━ [거장의 시각] ━━

**왜 치명적으로 중요한가:** "비선형 PK는 드문 예외인가?"라는 질문에 대한 R&T의 명쾌한 답이 이 카드에 있습니다. 비선형 PK 약물이 "특이한 예외"처럼 보이지만, 사실은 **구조적으로 예측 가능한 예외**입니다.

**체화해야 할 단 하나의 직관:** 약물 개발팀은 항상 더 강력한 약(낮은 $C_{50}$)을 추구합니다. 효능이 강할수록 치료 농도가 낮아지고, 낮은 치료 농도는 자동으로 효소 포화 농도($K_m$)보다 훨씬 아래에 위치합니다. 결과적으로 **"효능 추구"가 역설적으로 PK의 선형성을 보장**합니다.

---

#### A & B. 핵심 관계 — C50과 Km의 위치가 전부를 결정한다

$$E = \frac{E_{max} \cdot C^{\gamma}}{C_{50}^{\gamma} + C^{\gamma}} \quad \text{(PD: Emax 모델)}$$

$$Rate = \frac{V_m \cdot C_{u_H}}{K_m + C_{u_H}} \quad \text{(PK: MM 대사 속도)}$$

> 💡 두 수식은 **수학적으로 완전히 동일한 쌍곡선 형태**입니다. PD가 "항상 비선형", PK가 "대체로 선형"인 이유는 수식 구조 차이가 아니라 **$C_{50}$과 $K_m$의 위치 차이**입니다 [R&T Fig 16-3, p.497].

**실제 수치 앵커 (R&T Fig 16-3):**

| 약물 | CYP3A $K_m$ (또는 $K_d$) | 약효 $C_{50}$ | 비율 | PK 결과 |
|---|---|---|---|---|
| Midazolam | ≈ 3.3 µM | ≈ 0.05 µM (진정) | **66배 차이** | PK ≈ 선형 |
| **Phenytoin** | $K_m$ ≈ 4 mg/L (총) | 10–20 mg/L | **동일 범위** | **비선형!** |
| **Alcohol** | $K_m$ ≈ 100 mg/L | $C_{50}$ > 200 mg/L | $K_m < C_{50}$ — 희귀 | **비선형!** |
| TMDD (bosentan, draflazine, imirestat) | $K_d$ ≈ pharmacological 농도 | ≈ $K_d$ | 동일 범위 | **비선형!** |

[출처: R&T 5e, Ch.16, pp.495–497]

> 🔑 **외울 규칙:** "비선형 PK는 치료 농도가 $K_m$에 가까운 약물에서 온다." Phenytoin · Alcohol · TMDD 약물이 예외적인 이유는 **치료 농도 자체가 효소(또는 표적) 포화 농도 근처**이기 때문이며, 이는 약리학적 효력(potency)이 제한적임의 다른 표현입니다.

**임상·규제 함의:** Phase 1 FIH 용량 설계 시, in vitro $K_m$ 추정치와 목표 치료 농도를 반드시 비교해야 합니다. 치료 농도가 $K_m$에 근접하면 고용량 코호트에서 폭발적 비선형을 만날 수 있습니다.

---

### 🃏 카드 3. ⚡ Michaelis-Menten 소실 동역학 [Apex Concept]

> ⚡ **이 카드가 세션 전체의 보스입니다.** 이하의 카드(페니토인, 알코올, salicylate, cefonicid)는 이 카드의 응용 사례입니다. 이 카드의 직관을 완전히 장착하면 나머지는 자동으로 따라옵니다.

#### ━━ [거장의 시각] ━━

**왜 치명적으로 중요한가:** 페니토인 300 → 500 mg/day 증량 시 농도 4 → 36 mg/L (9배)로 독성 뇌증이 발생합니다. 이것은 "의사의 실수"가 아니라 **MM 동역학의 수학적 필연**입니다. 그리고 PK17처럼 데이터가 $K_m$ 주변 곡률을 충분히 포함하지 않으면 — 비록 $V_{max}$·$K_m$의 점추정 정밀도(CV%)가 낮아도 — 외삽이 위험할 수 있습니다.

**체화해야 할 단 하나의 직관:**

> **"고농도에서 maximal인 것은 Rate(소실 속도)이고, 저농도에서 maximal인 것은 Clearance(청소율)이다."**

이 두 축을 헷갈리면 모든 임상·NONMEM 추론이 거꾸로 됩니다.

> 💡 **공장 비유로 영구히 각인하기:**
> - **Rate** = "하루 총 생산량" → 원료(약물)가 넘치면 최대($V_{max}$), 부족하면 비례 감소
> - **Clearance** = "원료 단위당 처리 효율" → 원료가 넘치면 효율 바닥, 원료가 희박하면 효율 최고($V_{max}/K_m$)

---

#### A. 정의

약물 소실 속도가 효소 포화로 인해 농도에 비례하지 않고 최대 소실 속도 $V_{max}$에 점근하는 saturable 과정. 치료 농도가 $K_m$에 근접·초과할 때 비선형이 됩니다.

---

#### B. 수식 체계 — 단계별로 쌓기

**Step 1. 선형 기준선 (비교 대상)**

$$\frac{dC}{dt} = -\frac{CL}{V} \cdot C \quad \text{(CL은 상수)} \tag{G\&W Eq.2:265}$$

**Step 2. MM clearance — CL이 농도의 함수가 됨**

$$CL(C) = \frac{V_{max}}{K_m + C} \tag{G\&W Eq.2:266}$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $V_{max}$ | µg/min · g/hr · mg/day 등 | 효소 총량에 비례하는 최대 대사 속도 | 유도↑, 간경변↓, 비경쟁억제↓ |
| $K_m$ | µg/mL (농도 단위) | 소실 속도 = $V_{max}/2$일 때의 농도 = 효소 친화도의 역수 | 경쟁억제↑ |

[출처: G&W 5e, §2.7.2, Eq.2:266, p.115; R&T 5e, Ch.16, Eq.16-1~2, p.494]

> 💡 **$K_m$의 직관:** $K_m$이 낮을수록 효소·약물 친화도가 높음(소량으로도 잘 처리). 높을수록 효소가 약물에 둔감(농도를 높여야 절반 속도 도달).

**Step 3. Rate vs CL 이중 극한 — 알코올 Table 16-3 수치**

R&T Table 16-3: Alcohol ($V_m$=10 g/hr, $K_m$=100 mg/L) [출처: R&T p.500]

| 혈중 농도 (mg/L) | Rate (g/hr) | CL (L/hr) |
|---|---|---|
| 7,000 | **9.9** | **1.4** |
| 5,000 | 9.8 | 2.0 |
| 3,000 | 9.7 | 3.2 |
| 1,000 | 9.1 | 9.1 |
| 500 | 8.3 | 17 |
| 200 | 6.7 | 33 |
| 100 | 5.0 | 50 |
| 50 | 3.3 | 67 |
| **10** | **0.91** | **91** |

> 🔑 **이 표에서 읽어야 할 것:** 농도가 700배 감소(7,000→10 mg/L)할 때 Rate는 약 11배 감소하지만 CL은 65배 증가합니다. **Rate와 CL은 같은 방정식의 서로 다른 얼굴**이며, 이 비대칭성이 모든 임상 함의의 출발점입니다. 또한 저농도 한계에서 $V_m/K_m$ ≈ 100 L/hr ≈ 1.6 L/min — 이는 **간 혈류량을 초과**하므로 매우 낮은 농도에서는 알코올이 사실상 perfusion-limited(고추출비)로 동작합니다 [R&T p.501].

**Step 4. IV Bolus ODE**

$$\frac{dC}{dt} = -\frac{V_{max} \cdot C}{K_m + C} \cdot \frac{1}{V} \tag{G\&W Eq.2:270}$$

**Step 5. 상수속도주입 ODE**

$$\frac{dC}{dt} = \left( Input - \frac{V_{max} \cdot C}{K_m + C} \right) \cdot \frac{1}{V} \tag{G\&W Eq.2:273}$$

> ⚠️ **치명적 주의:** Input > $V_{max}$이면 $dC/dt > 0$ 항상 → **항정상태 수학적 불가능**. PK17의 slow infusion rate = 5,484.8 µg/39.63 min = **138.4 µg/min** > $V_{max}$ ≈ 107 µg/min이므로 이 실험으로는 원리상 $C_{ss}$를 관찰할 수 없습니다. **이것이 G&W가 PK17을 "pilot study에 불과"하다고 명시한 이유입니다** [G&W PK17 p.555 직접 인용].

**Step 6. AUC (IV bolus, 1구획)**

$$AUC = \frac{C^0}{V_{max} \cdot 2} \cdot \left[K_m + \frac{C^0}{2}\right] = \frac{K_m \cdot C^0}{2 V_{max}} + \frac{(C^0)^2}{4 V_{max}} \tag{G\&W Eq.2:271}$$

> 💡 **AUC가 이차함수인 이유:** 첫 항은 $C^0$에 선형, 둘째 항은 $C^0$의 제곱. 저농도에서는 첫 항 지배 → 선형처럼 보이지만, 농도가 올라가면 제곱항이 지배해 AUC가 폭발합니다. **"고농도 코호트 없이 비선형을 포착하기 어렵다"의 수학적 근거**가 여기 있습니다.

**Step 7. 순간 반감기 — 선형과 정반대 방향**

$$t_{1/2}^{inst}(C) = \ln(2) \cdot \frac{V}{V_{max}} \cdot (K_m + C) \tag{G\&W Eq.2:272; PK17 Eq.17:3}$$

> 🔑 **선형 PK vs MM PK 반감기 비교:**
>
> | | 선형 PK | MM PK |
> |---|---|---|
> | 반감기 | 농도 무관, 일정 | **농도↑ → 반감기↑** |
> | Semi-log 기울기 | 일정한 직선 | 시간이 지날수록 **가팔라짐** |
> | $5\times t_{1/2}$ 규칙 | 사용 가능 | **사용 불가** |
> | 단위 정합 | $h^{-1} \cdot V \cdot V^{-1}$ | $V/V_{max} \cdot K_m$ — $K_m$이 농도 차원 |
>
> G&W 경고 — **$K_m$의 10–20% 농도에서 이미 비선형이 시작됩니다** [G&W p.119]. "$K_m$을 넘어야 비선형"이라는 단순화는 위험합니다. $K_m$ = 1 µg/mL 약물이라면 0.1–0.2 µg/mL부터 이미 비선형 구간입니다.

**Step 8. 두 극한 조건**

$$C \gg K_m: \quad Rate \approx V_{max} \quad \text{(zero-order, 영차)} \tag{Eq.2:268}$$
$$C \ll K_m: \quad Rate \approx \frac{V_{max}}{K_m} \cdot C = K' \cdot C \quad \text{(first-order, 일차)} \tag{Eq.2:269}$$

> ⚠️ **저농도 극한의 함정:** $C \ll K_m$일 때 추정 가능한 것은 비율 $K' = V_{max}/K_m$ 하나뿐 — $V_{max}$와 $K_m$을 분리해 추정하려면 **데이터가 $K_m$ 주변 곡률을 반드시 포함**해야 합니다.

---

#### PK17 실제 파라미터 (Agent X, single subject) [G&W PK17 pp.553–555]

| 파라미터 | Linear 모델 | MM 모델 | CV% |
|---|---|---|---|
| $V$ (mL) | 1,380 | **1,450** | 5 |
| $CL$ (mL/min) | 43.3 | — | — |
| $V_{max}$ (µg/min) | — | **107** | **2** |
| $K_m$ (µg/mL) | — | **0.56** | 5 |

> 🔑 **PK17 두 핵심 경고 — G&W 원문대로:**
>
> **① 시스템 포화로 항정상태 미관찰:** Slow infusion rate 138.4 µg/min > $V_{max}$ 107 µg/min. *"Using information obtained for V_max and K_m, and the infusion rate, we conclude that one would never achieve steady state with the present rate and duration of infusion since the system is saturated. Therefore, this experiment could only be used as a pilot study"* [G&W p.555 직접 인용].
>
> **② $K_m$–$V$ 상관 = −0.96, 그러나 정밀도는 양호:** *"the correlation between some parameters of the Michaelis-Menten model was high (Km and V = -0.96), the parameter precision is still good"* [G&W p.554]. **즉 점추정 신뢰도(CV% 2–5%)는 충분하나 — 모델 외삽 시 두 파라미터가 함께 움직이는 ridge를 따라 불확실성이 전파**되므로 두 배·세 배 용량으로 외삽하면 위험합니다. 해결: **고용량 코호트(2배·3배 dose)를 추가**해야 한다고 G&W가 명시 [p.555].
>
> 최단 $t_{1/2}$ ≈ **5 min** (C=0 기준), 선형 모델 예측 ≈ 20 min — **4배 차이**. 최고 CL ≈ **190 mL/min** (저농도 극한). 농도 1.5 µg/mL 부근에서 두 모델이 만남.
>
> ✱ *v1 정정:* 1차본의 "structural identifiability 실패" 표현은 G&W 원문보다 강했습니다. 정확한 표현은 "**높은 파라미터 상관 + 협소한 농도 범위 → 외삽 위험**"이며, identifiability 자체의 실패는 아닙니다.

---

#### NONMEM 구현 코드 (L5)

```fortran
;; ─────────────────────────────────────────────────────────
;; PK17 1-compartment Michaelis-Menten via $DES (ADVAN13)
;; ─────────────────────────────────────────────────────────

$SUBROUTINES ADVAN13 TOL=6        ;; user-defined DES — 확장성 최대

$MODEL
  COMP (CENTRAL)                  ;; CMT=1, S1 참조

$PK
  VMAX = THETA(1) * EXP(ETA(1))   ;; µg/min
  KM   = THETA(2) * EXP(ETA(2))   ;; µg/mL
  V    = THETA(3) * EXP(ETA(3))   ;; mL
  S1   = V                        ;; ⚠️ 단위 함정 — 아래 박스 참조

$DES
  CONC    = A(1) / V                       ;; µg/mL
  RATE_EL = VMAX * CONC / (KM + CONC)      ;; µg/min
  DADT(1) = -RATE_EL                       ;; (R1은 NONMEM이 RATE column으로 자동 공급)

$ERROR
  IPRED = A(1) / S1
  ;; ⚠️ SIGMA는 분산이므로 제곱 금지! (1차본 정정사항)
  W     = SQRT(SIGMA(1,1) * IPRED**2 + SIGMA(2,2))
  Y     = IPRED + W * EPS(1)

$THETA
  (0, 107)        ;; VMAX — PK17 기준
  (0, 0.56)       ;; KM
  (0, 1450)       ;; V

$OMEGA
  0.04            ;; IIV-VMAX (CV ≈ 20%)
  0.04            ;; IIV-KM
  0.04            ;; IIV-V

$SIGMA
  0.04            ;; proportional error variance (CV² ≈ 0.04 → CV ≈ 20%)
  0.1             ;; additive error variance (µg/mL)²

$ESTIMATION METHOD=1 INTERACTION MAXEVAL=9999
$COVARIANCE PRINT=E
```

> ⚠️ **silent error 트랩 ① — `$ERROR` 분산-표준편차 혼동 (1차본 정정):**
> NONMEM의 `$SIGMA`는 **분산(variance)** 을 저장합니다. 따라서 가중치 $W$ 계산 시
> `W = SQRT(SIGMA(1,1) * IPRED**2 + SIGMA(2,2))` ← 이미 분산이므로 그대로 사용
> ~~`W = SQRT(SIGMA(1,1)**2 * IPRED**2 + SIGMA(2,2)**2)`~~ ← **틀림**: 분산을 또 제곱하면 가중치가 약 1/4로 축소되고 잔차 패턴이 왜곡됩니다.
> 진단: SIGMA 추정값에 단위 주석 `(µg/mL)²`가 붙어 있으면 분산 기준입니다.

> ⚠️ **silent error 트랩 ② — S1 단위 함정 (가장 흔한 실무 오류):**
> - `A(1)`의 단위 = µg (약물량)
> - `V`의 단위 = mL
> - `S1 = V`로 설정해야 IPRED = µg/mL (농도 단위)
>
> S1을 설정 안 하면 NONMEM은 `A(1)` 자체(=µg)를 IPRED로 출력합니다. 모델이 "수렴"하는 척하면서 모든 파라미터 추정이 망가집니다 — 단위 검증을 코드 작성마다 명시적으로 수행하세요.

> 💡 **ADVAN10 대안:** 1구획 MM 내장, 파라미터명 `VM`·`KM` 직접 사용. 단순하지만 2구획·병렬 경로 확장 불가. PIPET-Lab의 first-paper 워크플로우는 ADVAN13 + $DES를 표준으로 잡는 편입니다(확장성).

---

#### C. Structural Necessity — 왜 쌍곡선 형태인가

MM 방정식이 쌍곡선 형태인 이유: **quasi-steady-state 가정**(효소-기질 복합체 [ES]가 자유 기질보다 훨씬 빠르게 평형)에서 유일하게 유도됩니다. 이 가정이 깨지면(효소 농도 ≈ 기질 농도) → **TMDD 모델로 확장 필요**(I-08 브리지).

---

#### ⚡ C-2. Plausible Fallacy — 가장 위험한 그럴싸한 오류

**오류:** "$K_m$보다 훨씬 낮은 치료 농도에서 dose-normalized 프로파일이 superimpose됨 → 고용량 AUC를 선형 외삽 허용."

**왜 그럴싸한가:** 저용량 Phase 1에서 GOF가 좋고 dose-proportionality 통계도 통과합니다. 논리적으로 합리적으로 들립니다.

**나비효과:** G&W가 명시한 대로 $K_m$의 **10–20%에서 이미 비선형이 시작**됩니다. $K_m$ = 1 µg/mL 약물이라면 0.1–0.2 µg/mL부터 이미 비선형 구간 → 이를 무시하고 Phase 2 설계 시 목표 농도 계산이 완전히 틀립니다.

**NONMEM 진단 시그니처 — "Sinusoidal CWRES Bias":**
- CWRES가 고농도에서 체계적 양(+) 편향
- 저농도에서 체계적 음(−) 편향
- GOF에서 고농도 구간 systematic underprediction

---

#### D. 가정 및 경계조건

- **1구획 순간 혼합:** 위반 시 분포상이 MM 파라미터와 혼동 → cefonicid처럼 잘못된 2구획 해석
- **단일 효소 경로 ($f_m$ = 1):** 병렬 경로 존재 시 비선형성 완화 (salicylate 사례)
- **$K_m$·$V_{max}$ 시간 불변:** 자가유도 시 $V_{max}(t)$로 확장 필요 (carbamazepine 사례)
- **Input ≤ $V_{max}$:** 초과 시 $C_{ss}$ 수학적 불가능 (PK17, 한 잔/시간 알코올 사례)

---

#### G. Zettelkasten Atom

```yaml
aliases: [Michaelis-Menten PK, MM 소실, 포화 동역학, capacity-limited]
tags: [pharmacometrics/pk/nonlinear/capacity, nonmem/DES/ADVAN13, clinical/TDM/phenytoin]
source: "G&W 5e, §2.7.2, PK17 pp.553–555; R&T 5e, Ch.16, pp.493–500"
```

MM 소실의 이중 극한: **저농도 = maximal CL($V_{max}/K_m$), 고농도 = maximal Rate($V_{max}$)**. $K_m$의 10–20%에서 이미 비선형 시작. Input > $V_{max}$ → $C_{ss}$ 수학적 불존재. PK17 −0.96 상관은 identifiability 실패가 아니라 **외삽 위험 신호** — 정밀도는 양호하나 ridge ridge를 따라 불확실성이 전파됨. NONMEM 함정 두 가지: **SIGMA 분산-표준편차 혼동**과 **S1=V 단위 정합**.

---

### 🃏 카드 4. 입력 속도 Catastrophe — Phenytoin & Alcohol + Zero-order 역설

#### ━━ [거장의 시각] ━━

**왜 치명적으로 중요한가:** 페니토인에서 **bioavailability 12% 변화**(0.85→0.95)가 $C_{ss}$를 **2배**로 올려 독성으로 진입시킵니다. 그리고 알코올은 zero-order 소실에서 **느리게 투여하면 AUC가 오히려 감소**하는 — 선형 PK와 정반대 — 역설을 보여줍니다.

**체화해야 할 단 하나의 직관:** 발산 경계는 $R_0 \to V_m$이고, **$V_m$ 변화는 비선형 폭발, $K_m$ 변화는 선형 비례**입니다. 그리고 zero-order 소실에서 느린 흡수는 AUC를 줄입니다.

---

#### A. 항정상태 농도 공식

$$C_{u,ss} = \frac{K_m \cdot R_0}{V_m - R_0} \tag{R\&T Eq.16-6, p.501}$$

> 💡 **이 수식이 말하는 것:** 분모가 $(V_m - R_0)$입니다. $R_0$가 $V_m$에 가까워질수록 분모가 0에 수렴하고 $C_{ss}$는 **무한대**로 발산합니다 — 이것이 "발산 경계"입니다.

**페니토인 정량 예시** ($K_m'$=4 mg/L, $V_m$=500 mg/day, $V$=50 L) [R&T Fig 16-10, p.505]:

| $R_0$ (mg/day) | $C_{ss}$ (mg/L) | 임상 해석 |
|---|---|---|
| 300 | 6.0 | 치료역 미달 |
| 350 | 9.3 | |
| 400 | 16.0 | 치료역 내 |
| 425 | 22.7 | 독성 경계 |
| **500 (= $V_m$)** | **∞** | **항정상태 불가능** |

---

#### B. $V_m$ 변화 vs $K_m$ 변화의 비대칭성 — 임상에서 가장 중요한 구분

$$\frac{C_{u,ss,2}}{C_{u,ss,1}} = \frac{V_{m1} - R_0}{V_{m2} - R_0}$$

- **$V_m$ 20% 감소** (간경변, 500→400 mg/day, $R_0$=300): 분모 200→100 → $C_{ss}$ **2배**
- **$V_m$ 20% 증가** (효소 유도, 500→600): $C_{ss}$ 33% **감소** (비대칭)
- **$K_m$ 50% 증가** (cimetidine, 4→6 mg/L): $C_{ss}$ 50% **선형 비례** 증가

> ⚠️ **임상 함정:** "cimetidine이 페니토인 독성을 유발한다"고 많이 가르치지만, 실제 영향($K_m$ 50%↑ → 농도 50%↑)은 **선형이고 예측 가능**합니다. 진짜 위험은 **간경변·약물상호작용으로 $V_m$이 조금만 줄 때** — 이때 비선형 폭발이 일어납니다.

---

#### C. Bioavailability 변화 → Css 폭발 [R&T pp.503–504]

환자 파라미터: $K_m'$=3 mg/L, $V_m$=425 mg/day, 200 mg q12h (일일 처방용량 $D$=400 mg)

- **현재 (F=0.85):** $R_0 = 0.85 \times 400 = 340$ mg/day → $C_{ss} = 12$ mg/L
- **제형 전환 후 (F=0.95):** $R_0 = 0.95 \times 400 = 380$ mg/day
$$C_{ss}' = \frac{3 \times 380}{425 - 380} = \frac{1140}{45} = \mathbf{25.3} \text{ mg/L (독성)}$$

**→ F가 12% 증가했을 뿐인데 $C_{ss}$는 2배 폭발.** 페니토인 제형 변경 시 반드시 TDM을 시행해야 하는 정량적 근거가 여기에 있습니다. (FDA가 페니토인 generic 등재에 narrow therapeutic index 분류를 적용한 이유)

---

#### D. Pseudosteady-state 현상 — "왜 페니토인 TDM은 1달 기다려야 하는가"

$$t_{90} = \frac{K_m' \cdot V \cdot (2.303 \cdot V_m - 0.9 \, R_0)}{(V_m - R_0)^2} \tag{R\&T Eq.16-10, p.504}$$

R&T Fig 16-11: 250 → 200 mg/day **감량** 후 **23일** 뒤에야 새 $C_{ss}$ 도달. **20% 감량 → 50% $C_{ss}$ 감소** [R&T p.505].

> 💡 **왜 이렇게 오래 걸리는가?** 분모의 $(V_m - R_0)^2$ 항을 보세요. $R_0$가 $V_m$에 가까울수록 분모가 작아지고 $t_{90}$은 급격히 커집니다. 이것은 선형 PK의 "$5 \times t_{1/2}$"과 전혀 다른 물리입니다. **임상 실무 규칙: 페니토인 TDM은 용량 변경 후 최소 3–4주 뒤.**

---

#### E. 알코올 — Zero-order elimination의 3가지 결과

**(1) $C_{ss}$ 계산 ("virtual impunity"):**

- 한 잔/시간 (=14 g/hr) > $V_m$ 10 g/hr → 항정상태 불가능 → 농도 무한 축적
- 반 잔/시간 (=7 g/hr) < $V_m$:
$$C_{ss} = \frac{100 \times 7}{10 - 7} = \frac{700}{3} \approx \mathbf{233} \text{ mg/L}$$
약하게 취하는 수준 — "반 잔씩 마시면 거의 효과 없는" 이유입니다 [R&T p.501; 원문은 "약 230 mg/L"로 반올림].

**(2) 치사 축적 계산:**
- $V$ ≈ 42 L/70 kg, 치사 농도 ≈ 5,000 mg/L → 체내 필요량 ≈ **200 g**
- 14 g/hr (한 잔/시간): 초과분 4 g/hr → 200 g 축적에 **약 50시간 (2일, 48 drinks)** [R&T 원문]
- 56 g/hr (4잔/hr): 초과분 46 g/hr → **약 5시간 내 (20 drinks)** 치사 [R&T p.501]

**(3) Zero-order paradox — 가장 반직관적인 핵심 ★★★**

> 💡 **선형 PK와 정반대입니다.**

| | 선형 소실 | Zero-order(MM) 소실 |
|---|---|---|
| Input rate ↓ 시 AUC | **불변** ($AUC = Dose/CL$) | **감소** |
| 이유 | CL 일정이므로 총 제거 = 총 투여 | 주입 기간 동안 일정 속도 제거 → 잔량 감소 |
| 음식 + 알코올 | 흡수 늦춰도 AUC 불변 | **흡수 늦추면 AUC 감소** |
| Oral bioavailability | AUC 비교 = gold standard | AUC 비교 **사용 불가** |

> 🔑 **R&T Fig 16-8 vignette (1차본 누락 — 보강):**
> *"if the dose had been infused over a 5-hr period (i.e., at 200 mg/hr), output would have matched input and there would have been no AUC in this hypothetical example"* [R&T p.502 직접 인용].
> **즉 1,000 mg을 5시간(=200 mg/hr = $V_m$) 동안 정확히 주입하면 — 이론적으로 AUC = 0이 됩니다.** 들어가는 즉시 같은 속도로 빠져나가기 때문입니다. Zero-order 약물에서 input rate가 AUC를 결정하는 메커니즘의 극한 사례입니다.

> 🔑 **임상 함의:** "식후 음주가 식전보다 덜 취하는" 정량적 근거가 여기 있습니다. 그리고 zero-order 소실 약물은 IV bolus와 oral AUC 비교로 F를 계산하면 **틀린 결과**가 나옵니다. **IV microtracer가 필수**입니다.

[출처: R&T 5e, Fig 16-7, Fig 16-8, pp.501–502]

---

#### G. Zettelkasten Atom

```yaml
aliases: [페니토인 Css, MM 항정상태, pseudosteady-state, zero-order paradox]
source: "R&T 5e, Ch.16, Eq.16-6–16-10, pp.500–506"
```

발산 경계 $R_0 \to V_m$. **$V_m$ 변화 = 비선형 폭발** (간경변 20%↓ → Css 2배), **$K_m$ 변화 = 선형 비례** (cimetidine 50%↑ → Css 50%↑). F 12% 변화가 Css 2배 (페니토인 NTI). $t_{90} \propto (V_m-R_0)^{-2}$ — 페니토인 TDM 3–4주 대기. Zero-order 소실에서 input rate ↓ → **AUC 감소** (선형의 정반대). 5-hr 주입 with $R_0 = V_m$ 시 AUC = 0의 극한.

---

### 🃏 카드 5. 혼합 병렬 경로 — Salicylic Acid의 두 비선형 상쇄

#### ━━ [거장의 시각] ━━

**왜 치명적으로 중요한가:** Salicylate의 총 clearance는 치료 범위에서 비교적 일정해서 **"선형"처럼 보입니다.** 그러나 두 비선형이 서로 상쇄되어 총 CL이 flat한 것이고, **그 뒤에서 비결합 농도($C_{u,ss}$)는 조용히 초비례로 쌓입니다** [R&T Fig 16-29, p.523]. 임상 독성은 총 농도가 아닌 비결합 농도에서 옵니다. 총 농도 TDM에 의존하면 독성 진입을 못 잡습니다.

---

#### A & B. 병렬 경로 수식

$$CL = CL_{lin} + \frac{V_{max} \cdot C}{K_m + C} \tag{R\&T Eq.16-11, p.506}$$

$f_m$ 임계값: **포화 경로 $f_m \geq 0.5$이어야** 총 CL에 실질적 영향 [R&T p.506].

**소변 회수율 (Levy 1965)** [R&T Table 16-6, p.519]:

| 용량 (mg) | Unchanged SA (%) | Salicyluric acid (%) | Salicyl phenolic + acyl glucuronides (%) |
|---|---|---|---|
| 192 | 3 | **83** | 17 |
| 767 | 5 | **70** | 24 |
| 1,533 | 17 | **59** | 24 |
| 3,000 | 14 | **50** | 30 |

> 💡 **이 표에서 읽어야 할 것:** 총 회수율은 용량 전반에서 거의 100% → 대사 포화가 원인. Salicyluric acid 경로(83%→50%)가 포화되며 unchanged drug 회수가 늘고 다른 경로로 흘러갑니다.

**두 비선형의 상쇄 메커니즘** [R&T Fig 16-28, p.522]:
- 포화 대사 → $CL_{int}$ ↓ → CL ↓ 경향
- 포화 단백결합 → $f_u$ ↑ → $CL = f_u \cdot CL_{int}$에서 CL ↑ 경향

이 두 효과가 우연히 상쇄되어 **총 CL ≈ 일정**. 그러나 비결합 CL ($CL_u = CL_{int}$)은 계속 감소하므로 $C_{u,ss}$는 초비례 증가합니다 [R&T Fig 16-29].

> 🔑 **R&T Fig 16-29의 메시지:** Aspirin 투여 속도(mg/hr per kg) vs 비결합 salicylate 농도 — 곡선이 점점 가팔라집니다. 1 → 3 mg/hr/kg(3배)로 올리면 비결합 농도는 약 10배 증가. **총 농도로 보면 선형, 비결합 농도로 보면 폭발** — Reye 증후군·아스피린 독성의 정량적 모델.

---

### 🃏 카드 6. Saturable First-Pass & Absorption — F↑ 역방향 기전

#### ━━ [거장의 시각] ━━

**왜 치명적으로 중요한가:** Efflux transporter(P-gp) 포화와 saturable first-pass 대사 포화 모두 **$F$↑**를 만듭니다. 이를 대사 포화($F$↓)와 혼동하면 고용량에서 노출이 감소할 것으로 잘못 예측합니다 — 방향 판단이 완전히 뒤집히는 오류입니다.

---

#### A. Nicardipine — Saturable First-Pass의 교과서 사례

[R&T Table 16-2, p.499; Wagner 1987, n=6]

| 용량 (mg q8h) | Bioavailability (%) (mean ± SE) |
|---|---|
| 10 | 19 ± 4 |
| 20 | 22 ± 5 |
| 30 | 28 ± 5 |
| **40** | **36 ± 6** |

**해석:** 반감기 변화 없음 → 소실 $CL$ 불변 → **$F$↑가 유일한 원인**. 간 초회통과 대사가 포화됩니다.

**감별의 핵심:** Oral 데이터만으로는 $F$↓($CL$↑) vs $F$↑($CL$↓) 구분 불가 → **IV comparator 또는 IV microtracer 필수.**

---

#### B. Methylphenidate enantiomers — "Parent AUC↑ but metabolite AUC unchanged" 패턴

[R&T Fig 16-6; Aoyama et al. 1993]

| 지표 | (+)-MPH | (−)-MPH |
|---|---|---|
| Bioavailability | ≈ 20% | ≈ 4% |
| Metabolite (ritalinic acid) AUC | **≈ 동일** | **≈ 동일** |

> 💡 **해석 논리 — 두 가설 비교:**
>
> **가설 A (saturable first-pass, F↑):** Parent AUC는 두 enantiomer가 다르지만 대사물 AUC는 같음 → 간 처리량은 같으나 first-pass에서 (+)-MPH가 더 많이 "탈출"한 것. ✓ 관찰과 일치.
>
> **가설 B (전신 CL 포화):** CL↓ → 약물이 더 오래 머물 → metabolite 형성 시간↑ → **metabolite AUC도 증가**해야 함. ✗ 관찰과 불일치 → 배제.
>
> 결론: **Parent AUC↑ but metabolite AUC unchanged = saturable first-pass의 진단 시그니처.**

---

#### C. Amoxicillin — Saturable Active Absorption (F↓)

[R&T Fig 16-5; Sjövall 1985]

용량 375 → 750 → 1500 → 3000 mg 증가 시:
- Dose-normalized AUC, $C_{max}$ → **감소**
- $t_{max}$ → **거의 불변**

> 💡 **$t_{max}$ 불변이 진단의 핵심:** 흡수 부위가 소장 특정 구역에 고정 → 통과 시간 불변 → $t_{max}$ 불변. **용해도 제한이라면 $t_{max}$가 용량에 따라 변할 것**입니다 (느린 dissolution 때문에). 이 차이가 saturable transport vs solubility-limited dissolution을 구분합니다 [R&T pp.497–498 비교].

---

### 🃏 카드 7. 신배설 비선형성

**(1) 포화 분비 — Dicloxacillin** [R&T Fig 16-13; Nauta 1976]
$f_u$=0.04, 1g→2g IV → renal CL **감소**, extrarenal CL 불변 → 포화 분비 → 신배설 감소 → 전신 AUC 초비례 증가.

> 🔑 **수치 검증:** $f_u$ × GFR = 0.04 × 120 mL/min ≈ 4.8 mL/min (filtration만의 기여). 관찰된 renal CL ≈ 104 mL/min ≫ 4.8 → **분비가 압도적**. 분비가 포화되는 게 자연스러움.

**(2) 포화 재흡수 — Ascorbic acid** [R&T Fig 16-15, Table 16-4]

| 일일 용량 | $C_{ss}$ | $CL_R$ |
|---|---|---|
| 75 mg/day (식이) | 9 mg/L | < 0.5 mL/min |
| **10,000 mg/day (133배)** | **19 mg/L (2배)** | **21 mL/min (42배)** |

133배 용량 → 농도 2배 — 두 비선형(흡수 포화 + 재흡수 포화 해제)이 동시 작용해 **$C_{ss}$를 좁은 범위로 자동 유지하는 생물학적 homeostasis**.

> 💡 **신배설 비선형 감별:**
>
> | 기전 | 용량↑ 시 $CL_R$ 변화 | 대표 약물 |
> |---|---|---|
> | 분비(Secretion) 포화 | $CL_R$ ↓ | Penicillin G, Dicloxacillin |
> | 재흡수(Reabsorption) 포화 | $CL_R$ ↑ | Ascorbic acid |
> | 단백결합 변화 artifact | 겉보기 ↓ (총 기준), 실제 ↔ (비결합 기준) | Disopyramide |

**(3) 결합 artifact — Disopyramide** [R&T Fig 16-16; Giacomini 1982]
1.5 mg/kg IV 후 — 총 $CL_R$은 시간에 따라 감소(60→27 mL/min)하지만 **비결합 $CL_R$은 일정**(≈190–210 mL/min). $\alpha_1$-AGP 포화에 의한 $f_u$ 변화가 원인 → **겉보기 $CL_R$ 감소는 신기능 저하가 아니라 단백결합 변화**. 고단백결합 약물 신배설 평가 시 반드시 비결합 $CL_R$을 측정해야 합니다.

---

### 🃏 카드 8. 단백·조직결합 비선형성 & TMDD 브리지

#### ━━ [거장의 시각] ━━

**왜 치명적으로 중요한가:** Warfarin-phenylbutazone 상호작용의 실제 원인은 단백결합 경쟁이 아니라 **CYP2C9 억제**입니다 [G&W p.134]. 그리고 cefonicid의 apparent biexponential decline을 2구획 분포로 잘못 해석하면 완전히 틀린 모델을 사용하게 됩니다.

**체화해야 할 단 하나의 직관:** *In vitro* 폐쇄계에서는 결합↑ → 비결합 농도↓ → 약효↓. 그러나 *in vivo* 개방계에서는 $C_u^{ss} = R_0 / CL_u$ — **$f_u$가 변해도 $CL_u$ 불변이면 $C_u^{ss}$ 불변 → 약효 불변**.

> 💡 **욕조 비유 — 폐쇄계 vs 개방계 [G&W Fig 2.104–2.105]:**
> - **In vitro 폐쇄계** = 수도꼭지·배수구 없는 욕조. 단백질을 추가하면 물이 단백질에 붙어 자유 수위(비결합 농도)가 내려감.
> - **In vivo 개방계** = 수도꼭지(투여 $R_0$)와 배수구($CL_u$)가 달린 욕조. 욕조 벽 두께($f_u$)를 바꿔도 수위($C_u$)는 수도꼭지·배수구 크기가 결정.

---

#### A. $f_u$ 비선형 거동 수식 (G&W §2.7.5)

$$f_u = \frac{C_u + K_d}{C_u + K_d + n \cdot [P_T]} \tag{Eq.2:301}$$

극한 형태:
$$f_u \approx \frac{1}{1 + K_a \cdot n \cdot [P_T]} \quad (C_u \ll 1/K_a) \tag{Eq.2:298}$$
$$f_u \to 1 \quad (C_u \gg 1/K_a) \tag{Eq.2:299}$$

[출처: G&W 5e, §2.7.5, Eqs.2:297–2:299, pp.130–131]

> 🔑 **20% 점유율 경험 규칙 [R&T p.511]:** "결합 부위의 20% 이상 점유 시 $f_u$ 변화 가시화." Albumin (≈600 µM, 1 binding site) 기준 약물 농도 ≈ 120 µM부터 비선형 시작. MW 250인 약물이면 30 mg/L. $\alpha_1$-AGP (≈15 µM) 기준이면 0.75 mg/L부터 시작 — 따라서 basic drug + $\alpha_1$-AGP 결합은 더 흔하게 비선형이 발생.

---

#### B. Cefonicid — "Apparent Biexponential ≠ 2구획" [R&T Fig 16-18; Dudley 1986]

30 mg/kg IV 단회 투여 후:
- **총 농도**: 완만한 단일지수 감소처럼 보임
- **비결합 농도**: 초기 2시간 내 **급격히** 감소, 이후 완만 → semi-log에서 biphasic 패턴
- **$f_u$**: 시간 따라 0.18 → 0.03으로 체계적 감소

**기전:** 고농도 시 albumin 결합 부위 포화 → $f_u$↑ → 겉보기 CL 높음 → 빠른 초기 소실. 농도 하강 → $f_u$↓ → CL 감소 → 느린 terminal phase.

> ⚠️ **핵심 함정:** 이 biphasic을 보고 2구획 모델로 피팅하면 peripheral compartment가 실제로는 **포화 단백결합을 흡수**하고 있는 것입니다. **단회 데이터만으로는 이 둘을 구분 불가** → 반드시 여러 용량 데이터 필요.

> ⚠️ **또 다른 역설 — Oral F > 1.0 가능 [R&T p.512]:** Cefonicid를 oral로 투여하면 IV 대비 "bioavailability > 100%"가 계산될 수 있습니다. 이유: IV는 초기 고농도 → 포화 결합 → $f_u$↑ → CL↑ → AUC 낮음. Oral은 서서히 흡수되어 포화 구간을 피해 CL이 낮게 유지됨 → AUC가 IV보다 클 수 있음. **즉 "F > 1"은 흡수가 100% 넘는 것이 아니라 saturable binding의 silent fingerprint.**

---

#### C. 단백결합 변화의 임상 결과 (IV 투여 기준) [R&T pp.511–512 본문]

> ✱ *v1 정정:* 1차본의 "Table 16-12 기반 정리" 표는 **R&T 원본 Table 16-12가 비어 있는 study problem**이라는 사실이 누락되었습니다. 아래는 R&T pp.511–512 본문 서술을 기반으로 재구성한 IV 투여 시 방향성입니다.

**저추출비 약물 + $f_u$↑ (R&T p.511 직접 인용):**
> *"the steady-state total plasma concentration is not increased much on doubling the rate of administration. The steady-state unbound concentration, however, doubles as a consequence of no change in unbound clearance."*

| | 총 $C_{ss}$ | 비결합 $C_{u,ss}$ | 약효 |
|---|---|---|---|
| **저추출비 + $f_u$↑ (IV)** | **↔ (거의 불변)** | **↑** | **↑ — 독성 위험** |
| 자가유도 발생 | ↓ | ↓ | ↓ |
| **고추출비 + $f_u$↑ (IV)** | **↔** (CL ≈ Q로 flow-limited) | **↑** | **↑ — 단, 임상적으로 거의 무의미** |
| 고추출비 + $f_u$↑ (oral) | ↓ (E↑ → F↓) | ↓ | ↓ |

> ✱ *v1 정정 핵심:* 1차본은 IV 고추출비 + $f_u$↑ 행을 "↓↓ ↓"로 적었습니다. 이는 oral 시나리오를 IV 행에 혼입한 것입니다. **IV 고추출비에서 CL ≈ $Q_H$이므로 $C_{ss} = R_0/Q_H \approx$ 일정, $C_{u,ss} = f_u \times C_{ss}$ ↑** 가 정확합니다.

> ⚠️ **TDM 함정:** 저추출비 약물에서 $f_u$ 증가하면 총 농도는 거의 변하지 않습니다. **총 농도 기준 TDM으로는 "정상"으로 보이지만 실제로는 비결합 농도가 올라 독성**이 올 수 있습니다.

> 🔑 **Bupivacaine — 이 모든 규칙의 임상적 유일 예외 [G&W p.134 직접 인용] (1차본 누락):**
> *"the unbound drug concentration is independent of the plasma protein concentration or tissue binding in an open system. … no dose adjustment will be necessary unless in rare cases for drugs with a high extraction ratio and narrow therapeutic window that are given intravenously … We are only aware of one compound that is given intravenously and has a narrow therapeutic interval and short equilibration time between concentration and response, and that is **bupivacaine**."*
>
> 즉 IV 고추출비 + $f_u$↑가 임상적으로 의미를 갖는 것은 (a) IV이고 (b) 고추출비이며 (c) 좁은 치료역이고 (d) PK/PD 평형이 빠른 — **이 네 조건이 동시에 성립하는 단 하나의 약물 = bupivacaine**. 이 사실을 모르면 거꾸로 단백결합 영향을 과대평가하게 됩니다.

**Warfarin-phenylbutazone 사례:** 둘 다 CYP2C9 기질 → 단백결합 경쟁이 아닌 **대사 억제**가 임상 상호작용의 실제 원인 [G&W p.134 명시].

---

#### D. TMDD 예시들 [R&T pp.513–516] → I-08 브리지

| 약물 | TMDD 부위 | 비선형 방향 |
|---|---|---|
| **Bosentan** | Endothelin receptor | $V_{ss}$ 0.67→0.16 L/kg (10→750 mg dose) |
| Imirestat | Aldose reductase | $V_{ss}$ dose-dependent, 후기 plateau 역전 |
| Draflazine | Nucleoside transporter (RBC) | 혈장 vs 전혈 큰 차이 |
| Trandolaprilat | ACE (plasma + tissue) | 4-fold $f_u$ 변화, biphasic decline = binding kinetics, accumulation ratio 1.49 (예상보다 낮음) |
| Mitoxantrone | DNA intercalation | 조직 분포 ∝ DNA content |

---

### 🃏 카드 9. 시간 의존성 동역학 + Product Inhibition

#### ━━ [거장의 시각] ━━

**왜 치명적으로 중요한가:** Carbamazepine 단기 PK로 만든 투여 계획이 2–3주 후 완전히 무효가 됩니다 [R&T Fig 16-25]. Clarithromycin은 250 → 500 mg 단순 증량 시 AUC 비례 이상으로 증가 + 7번째 dose 후 반감기 추가 연장 [R&T Fig 16-26]. Product inhibition은 농도가 낮아져도 CL이 회복되지 않는 독특한 패턴으로 감별합니다.

**체화해야 할 단 하나의 직관:**
- **Capacity-dependence** = "농도 때문에" CL이 바뀜 (농도 낮아지면 CL 회복)
- **Time-dependence (induction)** = "효소 pool이 늘어서" CL이 증가 (Cmazepine 자가유도)
- **Time-dependence (MBI)** = "효소가 자살해서" CL이 감소 (Clarithromycin)
- **Product inhibition** = "대사물이 쌓여서" CL이 감소 (농도 낮아져도 회복 안 됨)

---

#### A. 효소 Turnover ODE

$$\frac{dE}{dt} = R_{in} - k_{out} \cdot E \tag{G\&W Eq.2:275}$$

> 💡 **욕조 비유:** 효소 pool = 욕조. $R_{in}$ = 수도꼭지(합성), $k_{out}$ = 배수구(분해). **욕조가 새 수위에 도달하는 속도는 수도꼭지 크기가 아니라 배수구 크기($k_{out}$)가 결정합니다**. 유도제가 수도꼭지를 열어도 새 정상상태 도달 시간은 $k_{out}$에 의존.

$$Cl_t = Cl' - (Cl' - Cl) \cdot e^{-k_{out}(t-t_{lag})} \tag{G\&W Eq.2:282}$$

---

#### B. Product Inhibition vs Capacity vs Time — Levy [1982] 판별 [G&W Fig 2.87]

| 시그니처 | Capacity | Time-dep (induction) | Product inhibition |
|---|---|---|---|
| 농도 ↑일 때 CL | ↓ | (시간 무관 즉시) ↔ | ↓ (대사물 축적) |
| 농도 ↓로 회복 후 CL | **즉시 회복** | (느리게 회복: $k_{out}$ 시간) | **회복 안 됨** (대사물 잔류) |
| 반복 투여 trough | 안정적 | trough 변화 (CL 변동) | trough 점진 상승 |

---

#### C. G&W Table 2.16 — 효소 반감기 선택값 [G&W p.120]

| 유발 약물 | 기전 | $t_{1/2}$ of $k_{out}$ |
|---|---|---|
| Carbamazepine | Auto + hetero induction | **24–806 h** |
| Phenobarbital → Nortriptyline | Heteroinduction | 140 h |
| Methadone | Autoinduction | 94 h |
| Ifosfamide | Autoinduction | 2–6 h |
| Cyclophosphamide | Autoinduction | 6–240 h |

> 💡 **Carbamazepine 24–806 h 범위가 왜 이렇게 넓은가?** 유도 효소(CYP3A4, CYP2C8) 기저 발현량, 병용 약물, 자가유도 vs 이종유도 기전 혼합의 개인차가 극단적. 어떤 환자는 1일, 어떤 환자는 1달 이상 걸립니다 — 단회 PK로 만든 투여 계획이 임상에서 실패하는 이유.

---

#### D. PK21 (NT-Pb) — 핵심 수치 [G&W PK21 p.124]

- Pre-induction $Cl_{po}$ = 46 L/h → 유도 후 118 L/h (**2.6배**)
- $k_{out}$ $t_{1/2}$ = **158 h** (≈ 6.6일)
- MRT 36 → 14 h
- $V/F$ 추정 ≈ Dose/Cmax (pre-induction 단계)

> 💡 **이 연구 설계의 강점:** "**반복 trough values가 $k_{out}$ 추정의 핵심**"입니다. 단회 PK 데이터로는 유도 속도(=효소 turnover) 추정 불가. Trough 반복 측정이 효소 pool의 동적 변화를 포착합니다 [G&W Fig 2.95–2.97].

---

#### E. Clarithromycin — Mechanism-Based Autoinhibition (MBI) [R&T Fig 16-26]

250 → 500 mg q12h 단순 비례 증량:
- 단회 dose 7th vs 1st: AUC **초비례 증가** + **반감기 연장**
- 7th dose 시점에는 1st dose 반감기보다 명확히 김 — 효소가 자살한 것

> 🔑 **Suicide substrate:** 대사 과정에서 효소를 영구히 비활성화시키는 약물. 효소 단백 자체가 줄어드는 것 → 농도 낮아져도 즉시 회복 불가, 새 효소가 합성되어야 ($k_{out}$ 시간 단위) 회복. **약물 상호작용에서 가장 위험한 분류** — 한번 inhibitor가 효소를 잡으면 inhibitor 약물이 사라져도 효과 지속.

---

#### F. G&W Fig 2.89 — 개체간 Km 차이가 일으키는 IIV

두 피험자 (25 unit vs 100 unit IV bolus): terminal semi-log 기울기가 완전히 다름. 이유: 피험자 A $K_m$ ≈ 300 µg/L, 피험자 B $K_m$ ≈ 1,000 µg/L.

> 💡 **PopPK 함의:** MM 약물에서 IIV가 매우 크게 나타나는 이유는 단순히 "CL의 개체차"가 아니라 **비선형 파라미터 공간에서 개체가 어디 위치하는가**의 차이입니다. 같은 용량을 투여해도 $K_m$이 다르면 농도-시간 곡선의 **형태 자체가 달라집니다**. 따라서 PopPK 모델에서 $\eta$를 어디에 둘지(Vmax vs Km vs 둘 다) 신중한 결정 필요 — 둘 다에 두면 −0.96 같은 강한 상관이 등장.

---

### 🃏 카드 10. R&T 4단계 워크플로우 — Salicylate 완전 적용 [R&T pp.519–523]

> 카드 1에서 배운 프레임워크를 실제 데이터에 적용하는 연습입니다.
>
> **사례:** Sodium salicylate 3 g 단회 경구 투여 후 분석.

---

**Step 1. 소변 데이터로 비선형 탐지 (Table 16-6)**
- 선형 PK라면 용량과 무관하게 각 형태의 회수 비율이 일정해야 함
- 관찰: 용량↑ → unchanged salicylate 회수↑ (3→14%), salicyluric acid 회수↓ (83→50%)
- **→ superimpose 실패 확인. 기전 가설: (a) F↑, (b) $CL_R$↑, (c) 대사 포화**

---

**Step 2. C-time 프로파일로 파라미터 방향 식별 (Fig 16-27)**
- Semi-log 플롯: 기울기가 시간 지날수록 **가팔라진다**. 선형 PK라면 기울기 일정.
- **→ $CL$ ↑ with time, 즉 농도 감소와 함께 CL 회복 (capacity-dependence)**

---

**Step 3. 영향 받은 Primary 파라미터 결정**
- 최고 농도 ≈ 200 mg/L, 용량 3 g → $V/F$ ≈ 3,000/200 = 15 L (매우 작음)
- $V$가 15 L로 작으므로 농도 변화에 따른 $V$ 변화 가능성 낮음 → **$CL$↑가 주원인**
- 소변 데이터에서 metabolite 회수율 감소 → **대사 포화가 주요 기전**

---

**Step 4. 단백결합 데이터로 기전 확인 (Fig 16-28)**
- $f_u$가 농도↑ 시 증가 (고농도 albumin 결합 포화)
- $CL_u$(비결합 CL)는 농도↑ 시 감소 (대사 포화)
- **총 $CL$은 두 효과의 상쇄로 비교적 일정** — "선형처럼 보이는" 이유
- 그러나 **비결합 CL은 단조 감소** → $C_{u,ss}$는 dosing rate에 초비례 [Fig 16-29]

**최종 결론:** 두 비선형 기전 공존 + 상쇄 → 총 CL ≈ 일정, 그러나 **$C_{u,ss}$는 초비례** (독성의 실제 원인). 비결합 농도 측정 또는 dosing rate 기반 보수적 처방 필요.

---

### 🃏 카드 11. 비선형 PK 종합 방향성 정리 (R&T 본문 + Table 16-12 study problem 기반)

> ✱ **중요 정정:** R&T 원본 Table 16-12는 **학생이 채워 넣어야 하는 study problem 7번 빈 표**입니다. 완성된 directional 표는 교과서 본문(pp.511–512, 523–524)의 서술적 설명에서 도출해야 합니다. 아래는 그 본문 기반 재구성.

| 비선형 원인 | $V$ | $CL$ | $t_{1/2}$ | 총 $C_{ss}$/Rate | 비결합 $C_{u,ss}$/Rate |
|---|---|---|---|---|---|
| **경구 투여** | | | | | |
| Bioavailability ↓ (용해도/흡수 포화) | ↔ | ↔ | ↔ | ↓ | ↓ |
| **Bioavailability ↑** (saturable first-pass) | ↔ | ↔ | ↔ | ↑ | ↑ |
| **정맥 투여** | | | | | |
| $f_u$ ↑, **저추출비** 약물 | ↑ | ↑ | ↔ | **↔** | **↑** |
| $f_u$ ↑, **고추출비** 약물 (IV) | ↑ | ↔ (CL≈Q) | ↑ | **↔** | **↑** |
| 조직결합 포화 ($V$ ↓, e.g., bosentan) | ↓ | ↔ | ↓ | ↑ (초기) | ↑ |
| **대사 $CL$ ↓** (포화 대사, phenytoin) | ↔ | ↓ | ↑ | **↑** (비선형 폭발) | **↑** |
| 신 $CL$ ↓ (포화 분비, dicloxacillin) | ↔ | ↓ | ↑ | ↑ | ↑ |
| 신 $CL$ ↑ (포화 재흡수 해제, ascorbate) | ↔ | ↑ | ↓ | ↓ (homeostasis) | ↓ |
| 자가유도 (carbamazepine, time-dep) | ↔ | ↑ | ↓ | ↓ | ↓ |
| MBI / autoinhibition (clarithromycin, time-dep) | ↔ | ↓ | ↑ | ↑ | ↑ |

[출처: R&T 5e, Ch.16 본문 종합 — pp.499, 511–512, 519–523. R&T Table 16-12은 study problem 빈 표.]

> 💡 **가장 중요한 행 읽기:**
>
> **$f_u$ ↑ + 저추출비 (IV):** 총 농도 ↔(불변)이지만 비결합 농도 ↑. TDM에서 총 농도 보면 "정상"처럼 보이지만 실제로 독성이 올 수 있음.
>
> **$f_u$ ↑ + 고추출비 (IV):** CL ≈ $Q_H$ flow-limited이므로 총 농도 ↔. **임상적으로는 일반적으로 무의미** — 단, **bupivacaine처럼 (고추출비 + IV + 좁은 치료역 + 빠른 PD 평형)이 모두 성립하는 약물**에서만 독성 위험 (G&W p.134).
>
> **대사 $CL$ ↓ (phenytoin):** 가장 극단적 비선형. 총·비결합 모두 폭발.

---

## §5 — 혼동 쌍 해부

### 혼동 쌍 1: $V_{max}$ vs $K_m$ — Css 민감도의 비대칭성 ← **Critical Blow**

| 비교 차원 | $V_{max}$ | $K_m$ |
|---|---|---|
| **표면적 유사성** | 둘 다 MM 방정식의 파라미터, 둘 다 변하면 $C_{ss}$가 바뀜 | |
| **수식 위치** | $C_{ss} = \frac{K_m \cdot R_0}{V_m - R_0}$ → **분모**($V_m - R_0$) | **분자**($K_m \cdot R_0$) |
| **생물학적 지시체** | 효소 총량(amount/time) | 효소 친화도의 역수 (concentration) |
| **변화 유발 원인** | 유도↑, 간경변↓, 비경쟁억제↓ | 경쟁억제↑; 유도는 불변 |
| **$C_{ss}$ 반응** | **비선형 폭발**: $V_m$ 20%↓ → $C_{ss}$ **2배** | **선형 비례**: $K_m$ 50%↑ → $C_{ss}$ **50%** |
| **임상 함의** | 간경변·약물상호작용에서 발견되면 즉각 50% 이상 감량 | 흔한 DDI(cimetidine) — 예측 가능한 비례 조정 |
| **⚡ 기억 고리** | **$V_{max}$는 분모를 지배 — 0에 가까워질수록 폭발. $K_m$은 분자에만 있어 선형 비례. 비선형 폭발은 항상 분모가 만든다.** | |

| **🔥 치명적 타격** | 간경변 환자에서 $V_m$ 20% 감소를 $K_m$ 변화(선형)로 오인 → "50% 농도 증가"로 예측하고 50% 감량 → 실제로는 2배 상승을 막기에 부족해 독성 진입. NDA 시 모델 예측과 실제 농도가 2배 이상 괴리되어 심사관의 Deficiency Letter — 모델 부적합 사유로 명시. |
|---|---|

---

### 혼동 쌍 2: Zero-order 소실에서 Input Rate↓ → AUC↓ vs 선형에서 Input Rate↓ → AUC↔

| 비교 차원 | Zero-order(MM) 소실 | 선형(1차) 소실 |
|---|---|---|
| **Input rate ↓ 시 AUC** | **AUC 감소** | **AUC 불변** |
| **이유** | 주입 기간 동안 일정 속도로 계속 제거 → 주입 완료 시 잔량 ↓ | $CL$ 일정이면 $AUC = Dose/CL$ |
| **극한 사례** | $R_0 = V_m$로 5시간 주입 → **AUC = 0** (R&T Fig 16-8) | 어떤 경우에도 AUC = $Dose/CL$ 일정 |
| **Oral F 평가** | AUC 비교 방법 **사용 불가** → IV microtracer 필수 | AUC 비교 = gold standard |
| **⚡ 기억 고리** | **Zero-order는 "배수구 속도가 일정한 욕조". 수도꼭지를 천천히 틀면 들어오는 동안 배수구가 더 많이 빼내어 욕조(AUC)가 작아진다. 수도꼭지 = 배수구 속도면 욕조는 영원히 비어 있다(AUC=0).** | |

---

### 혼동 쌍 3: MM 순간 반감기 vs 선형 terminal half-life

| 비교 차원 | MM $t_{1/2}^{inst}(C)$ | 선형 terminal $t_{1/2}$ |
|---|---|---|
| **수식** | $\ln(2) \cdot \frac{V}{V_{max}} \cdot (K_m+C)$ | $0.693 \cdot V/CL$ |
| **농도 의존성** | 농도에 **비례 증가** | **농도 무관** |
| **Semi-log 거동** | 시간 지날수록 기울기 **가팔라짐** | 직선 |
| **$5\times t_{1/2}$ 규칙** | **사용 불가** | 신뢰 가능 |
| **PK17 수치** | C=0에서 ≈ 5 min, C=1.5 µg/mL에서 ≈ 20 min | 선형 모델 추정 ≈ 20 min (모든 농도) |
| **⚡ 기억 고리** | **MM 반감기는 농도가 만드는 순간 초상화 — 농도가 내려갈수록 화가의 붓질이 빨라진다. 선형 반감기는 처음부터 끝까지 같은 속도로 그려지는 정물화다.** | |

---

### 혼동 쌍 4: 단백결합 변화 — In vitro vs In vivo 약효 방향

| 비교 차원 | In vitro 폐쇄계 | In vivo 개방계 |
|---|---|---|
| **시스템** | 수도꼭지·배수구 없는 욕조 | 수도꼭지($R_0$)와 배수구($CL_u$)가 있는 욕조 |
| **핵심 관계** | 총 약물량 고정 → $f_u$↑ → $C_u$↑ → 약효↑ | $C_u^{ss} = R_0/CL_u$ → $f_u$가 변해도 $CL_u$ 불변이면 $C_u^{ss}$ 불변 |
| **약효 방향** | $f_u$↑ → 약효 **↑** | $f_u$↑ → 약효 **거의 변화 없음** |
| **임상적 유일 예외** | (해당 없음) | **Bupivacaine** — IV + 고추출비 + 좁은 치료역 + 빠른 PD 평형 [G&W p.134] |
| **Warfarin-phenylbutazone 진실** | 시험관에서 displacement 보임 | In vivo에서는 **CYP2C9 억제**가 실제 원인 |
| **⚡ 기억 고리** | **시험관(폐쇄계)은 저수지 없는 수영장. 생체(개방계)는 수도꼭지·배수구가 달린 수영장 — 벽 두께($f_u$)를 바꿔도 수위($C_u$)는 수도꼭지·배수구 크기가 결정한다. 단 한 가지 예외: bupivacaine.** | |

---

### 혼동 쌍 5: Capacity-dependent vs Time-dependent vs Product Inhibition

| 비교 차원 | Capacity | Time-dep (induction) | Time-dep (MBI) | Product Inhibition |
|---|---|---|---|---|
| **원인** | 농도 자체 | 효소 pool 합성 ↑ | 효소 자살 (효소 단백 파괴) | 대사물 축적 |
| **Levy 판별 기준** | 농도 일정 시 CL도 일정 | 농도 일정해도 CL 시간 따라 변함 | 동일 (자살 축적) | 동일 (대사물 축적) |
| **농도 ↓ 후 CL 회복** | 즉시 회복 | 새 효소 합성으로 점진 회복 | 새 효소 합성으로 점진 회복 | 대사물 잔류 시 회복 안 됨 |
| **대표 약물** | Phenytoin, Alcohol | Carbamazepine | Clarithromycin, Clopidogrel | (드문 약물; GW Fig 2.87 우측) |
| **⚡ 기억 고리** | **농도 변화로 시스템이 달라 보이면 capacity. 효소 pool이 늘어 시스템이 달라지면 induction. 효소가 자살해 줄어들면 MBI. 대사물이 쌓여 시스템이 달라지면 product inhibition.** | | | |

---

## §7 — Self-Test: Active Recall Module

**Q1** [★★] MM 방정식에서 "저농도에서 maximal"과 "고농도에서 maximal"인 것은 각각 무엇인가? $CL = V_{max}/2$가 되는 농도 조건은? R&T Table 16-3에서 알코올 농도 100 mg/L 대비 7,000 mg/L에서 Rate와 CL이 각각 몇 배 차이인지 계산하라.

<details><summary>정답 공개</summary>

저농도: **Clearance** 최대 ($V_{max}/K_m$). 고농도: **Rate** 최대 ($V_{max}$). $C = K_m$일 때 $CL = V_{max}/2$ (그리고 Rate = $V_{max}/2$).

알코올 ($V_m$=10 g/hr, $K_m$=100 mg/L):
- Rate: 7,000 mg/L → 9.9 g/hr; 100 mg/L → 5.0 g/hr → **약 2배**
- CL: 7,000 mg/L → 1.4 L/hr; 100 mg/L → 50 L/hr → **약 36배**

G&W 경고: $K_m$의 10–20%에서 이미 비선형 시작 — "$K_m$이 경계"라는 단순화는 위험하다.

**다음 깊이 질문:** 알코올 저농도 한계에서 $V_m/K_m$ ≈ 100 L/hr ≈ 1.6 L/min. 이것이 간 혈류를 초과한다는 사실의 의미는?
</details>

---

**Q2** [★★] 페니토인 $K_m'$=4 mg/L, $V_m$=500 mg/day, $V$=50 L 환자.
(a) 흡수된 약물의 입력속도 $R_0$=400 mg/day일 때 $C_{ss}$.
(b) 같은 환자에서 처방 일일 용량(F·D=$R_0$의 $D$)을 유지한 채 F가 0.85→0.95로 변하면 새 $C_{ss}$.
(c) 간경변으로 $V_m$이 400 mg/day로 감소하면 ($R_0$=300 mg/day로 감량 시)?

<details><summary>정답 공개</summary>

(a) $C_{ss} = \frac{4\times400}{500-400} = \mathbf{16}$ mg/L

(b) (a)에서 $R_0=400$이려면 $D = 400/0.85 ≈ 471$ mg/day. F=0.95로 바뀌면 새 $R_0 = 0.95 \times 471 ≈ 447$ mg/day.
$C_{ss}' = \frac{4 \times 447}{500-447} ≈ \mathbf{33.7}$ mg/L (독성)
→ F가 약 12% 변화 → Css 2배 이상 폭발.

(c) $V_m$=400, $R_0$=400이면 분모 = 0 → **$C_{ss} = \infty$, 항정상태 불가능**. $R_0$=300 감량 시: $\frac{4 \times 300}{400-300} = \mathbf{12}$ mg/L (치료역 내).

**다음 깊이 질문:** cimetidine이 $K_m'$를 4→6 mg/L로 올리면 (a) 조건에서 $C_{ss}$는? — $\frac{6\times400}{100} = 24$ mg/L (50% 증가, 선형 비례). **이는 (c)의 $V_m$ 변화 시나리오와 정량적으로 어떻게 다른가?** $V_m$ 감소는 분모를 깎고, $K_m$ 증가는 분자만 키운다 — 비선형 폭발 vs 선형 비례.
</details>

---

**Q3** [★★] PK17 (Agent X)에서 G&W가 "pilot study에 불과"하다고 명시한 두 이유를 수학적 근거와 함께 설명하라. 또한 $K_m$–$V$ 상관 −0.96의 정확한 의미를 G&W 원문에 따라 설명하라 (1차본의 'identifiability 실패' 표현 정정).

<details><summary>정답 공개</summary>

**이유 ① 시스템 포화로 정상상태 미관찰:** Slow infusion rate = 5,484.8 µg / 39.63 min ≈ **138.4 µg/min** > $V_{max}$ ≈ 107 µg/min. Eq.2:273에서 $dC/dt > 0$ 항상 → 항정상태 수학적 불가능. G&W p.555 직접 인용: *"one would never achieve steady state with the present rate and duration of infusion since the system is saturated. Therefore, this experiment could only be used as a pilot study."*

**이유 ② 데이터가 $K_m$ 주변 곡률 부족:** 측정 농도 범위가 $K_m$ 주변 곡률을 충분히 포함하지 않으면 외삽이 불안정. G&W는 해결책으로 **"a higher dose should also be investigated. By doubling or even tripling the highest dose, potential nonlinear behavior should be discernible"** 제시 [p.555].

**−0.96 상관의 정확한 의미:** G&W p.554 원문 — *"the correlation between some parameters of the Michaelis-Menten model was high (Km and V = -0.96), the parameter precision is still good."*

→ 즉 점추정 정밀도(CV% 2–5%)는 **양호**합니다. 그러나 두 파라미터가 함께 움직이는 ridge가 존재하므로 외삽 시 두 파라미터의 결합 불확실성이 함께 전파됩니다. **"identifiability 실패"는 G&W 원문보다 강한 표현이며 부정확** — 정확한 표현은 "**높은 파라미터 상관 + 협소한 농도 범위 → 외삽 위험**"입니다.

**다음 깊이 질문:** −0.96 상관을 줄이는 실험 설계 변경은? — (a) 고용량 코호트 추가로 $K_m$ 주변 곡률 확보 (G&W 권장), (b) IV bolus + slow infusion 조합으로 빠른 분포 + 느린 소실을 분리 캡처, (c) 다중 피험자 PopPK로 $\eta$ 위치를 통한 부분 분리.
</details>

---

**Q4** [★] Zero-order 소실 약물에서 input rate를 절반으로 줄이면 AUC는 어떻게 되는가? 선형 소실과 비교하고, R&T Fig 16-8의 "5-hr infusion → AUC=0" 극한 사례와 oral bioavailability 측정에 어떤 함의를 갖는지 설명하라.

<details><summary>정답 공개</summary>

**Zero-order 소실:** Input rate ↓ → AUC **감소**. 주입 기간 동안 약물이 일정 속도로 계속 제거되므로 주입 완료 시 잔량이 적음 [R&T Fig 16-8].

**선형 소실:** Input rate ↓ → AUC **불변** ($AUC = Dose/CL$, CL 일정).

**극한 사례:** R&T 원문 — *"if the dose had been infused over a 5-hr period (i.e., at 200 mg/hr), output would have matched input and there would have been no AUC in this hypothetical example."* 즉 1,000 mg을 5시간 동안 정확히 $V_m$ = 200 mg/hr로 주입 시, 들어오는 즉시 같은 속도로 빠져나가 **AUC = 0**. 들어오는 약물이 곧장 대사되어 농도가 측정 가능한 수준까지 올라가지 않습니다.

**Oral bioavailability 함의:** Zero-order 소실 약물은 IV bolus와 oral의 AUC 비교로 F를 계산하면 틀린 결과. IV는 빠른 input → 제한된 대사; oral은 느린 absorption → 더 많은 대사 → oral AUC가 IV보다 낮게 나와 F 과소추정. **IV microtracer 필수.**

**다음 깊이 질문:** 알코올에서 음식이 AUC를 줄이는 기전을 이 원리로 설명하라 — 음식 → 위 배출 지연 → 흡수 input rate 감소 → AUC 감소 (R&T Fig 16-7: tap water vs light cream vs 33% glucose).
</details>

---

**Q5** [★] Methylphenidate enantiomer 사례에서 "parent AUC↑ but metabolite AUC unchanged"가 saturable first-pass를 지지하는 이유를 두 가설 비교로 설명하라.

<details><summary>정답 공개</summary>

**가설 A (saturable first-pass, F↑) — 관찰과 일치:**
First-pass 단계에서 포화 대사를 피해 전신으로 탈출(F↑). 탈출한 약물 중 일부는 이후 전신에서 대사되어 metabolite 형성, 그러나 **간 first-pass + 전신 대사 합산 = 일정** → metabolite AUC ≈ 동일.

**가설 B (전신 CL 포화, AUC↑ 추가 원인) — 관찰과 불일치:**
CL ↓ → 약물이 더 오래 체내 머물 → metabolite 형성 시간↑ → metabolite AUC도 **함께 증가**해야 한다. 그런데 관찰에서는 일정 → 가설 B 배제.

**진단 시그니처 ★:** **Parent AUC ↑ + metabolite AUC ↔ = saturable first-pass의 fingerprint.**

**다음 깊이 질문:** Nicardipine의 oral F↑를 IV comparator 없이 감지하려면? — (a) 주요 metabolite AUC가 dose에 비례하는지 확인, (b) elimination $t_{1/2}$가 dose에 무관함을 보임 (R&T Wagner 1987이 활용한 방법).
</details>

---

**Q6** [★] Cefonicid의 총농도는 단일지수 감소처럼 보이는데 비결합 농도는 초기에 매우 빠르게 감소한다. 이것이 2구획 분포가 아닌 saturable binding 때문임을 어떻게 증명하는가? 추가로 "oral F > 1.0"이 saturable binding의 silent fingerprint인 이유는?

<details><summary>정답 공개</summary>

**증거 1:** 비결합 농도의 빠른 초기 감소가 총농도 감소 속도와 비례하지 않음 — 2구획 분포라면 총·비결합 농도가 proportional 관계 유지해야 함.

**증거 2:** $f_u$가 시간 따라 **체계적으로 감소**(0.18 → 0.03) [R&T Fig 16-18B]. 2구획이라면 $f_u$ 일정.

**결정적 증거:** 여러 용량 비교 — saturable binding이라면 저용량에서 biphasic 덜 뚜렷, 고용량에서 더 뚜렷. 2구획 분포라면 dose-normalized 프로파일 superimpose.

**Oral F > 1.0 fingerprint:** IV 투여 시 초기 고농도 → 결합 포화 → $f_u$↑ → CL↑ → AUC 낮음. Oral은 서서히 흡수되어 포화 구간을 피해 CL이 낮게 유지 → AUC가 IV보다 큼 → F = AUC_oral / AUC_IV > 1.0이 산출. 흡수가 100% 넘는 게 아니라 **분모(IV AUC)가 saturable binding으로 작아진 것**.

**다음 깊이 질문:** Cefonicid를 PopPK 모델로 적합할 때 단순 2구획 + linear PK를 사용하면 어떤 GOF 시그니처가 보이는가? — 고농도 구간 systematic underprediction + CWRES vs IPRED에서 sigmoidal 편향.
</details>

---

**Q7** [★] G&W Table 2.16에서 carbamazepine의 $k_{out}$ $t_{1/2}$ 범위가 24–806 h이다. 이 IIV의 원인과 PopPK 모델링 어려움은? 단회 PK로 만든 carbamazepine 투여 계획이 임상에서 실패하는 구체적 시나리오는?

<details><summary>정답 공개</summary>

**IIV 원인:** (1) 유도 효소(CYP3A4, CYP2C8) 기저 발현량 개체차, (2) 병용 약물 효과, (3) 자가 vs 이종 induction 기전 혼합.

**PopPK 어려움:** 24–806 h 범위에서 어떤 개체는 1일, 어떤 개체는 1달 이상 걸림. 단일 $\omega_{k_{out}}^2$로 표현 시 추정 불안정. 또한 carbamazepine은 자신의 $k_{out}$을 시간에 따라 바꾸므로 $k_{out}$이 고정 파라미터가 아닌 동적 변수 → 모델 매우 복잡 (G&W §2.7.3.4 feedback model 참조).

**임상 실패 시나리오:** 단회 100 mg → $C_{max}$ 측정으로 $V/F$ 추정 → 5 mg/kg q12h 처방. 첫 1주일 trough 모니터링에서 안정적으로 보임. **2–3주 후 자가유도가 정상상태에 도달하면서 trough가 50% 감소** → 발작 재발. 환자는 "약효가 떨어졌다"고 느끼고 임의로 증량. 이때 다시 자가유도가 따라잡으면서 다시 농도 감소 → 의사도 환자도 적정 용량 감을 잃음. **반복 trough 모니터링 (G&W PK22 권장)**과 **자가유도 ramp-up 기간 명시적 설명**이 표준이어야 함.

**다음 깊이 질문:** 자가유도 약물의 임상시험에서 정상상태 도달 시점을 어떻게 정의하는가? — Single-dose 후 **3 × $k_{out}$ $t_{1/2}$ 이상 반복 투여 후 trough 안정화** 확인.
</details>

---

**Q8** [★] R&T 본문 기반 (pp.511–512): 저추출비 약물에서 $f_u$가 증가할 때 (a) $V$, (b) $CL$, (c) 총 $C_{ss}$, (d) 비결합 $C_{u,ss}$의 방향을 예측하라. 그리고 고추출비 약물 IV 투여 시 같은 분석을 하고, **bupivacaine이 왜 임상적 유일 예외인가**를 설명하라.

<details><summary>정답 공개</summary>

**저추출비 + $f_u$ ↑:**
- (a) $V$ ↑ (비결합 약물이 조직 분포 증가)
- (b) $CL = f_u \cdot CL_{int}$ → $CL$ ↑
- (c) $C_{ss} = R_0/CL$ → $C_{ss}$ ↓ ... but 위 R&T 인용에 따르면 *"not increased much on doubling the rate"* — **거의 변하지 않음(↔)**
- (d) $C_{u,ss} = f_u \cdot C_{ss}$, R&T 원문 *"doubles as a consequence of no change in unbound clearance"* → **↑ (비례)**

**고추출비 + $f_u$ ↑ (IV):**
- $CL ≈ Q_H$ flow-limited이므로 $f_u$ 변화에 둔감 → $CL$ ↔
- $C_{ss} = R_0/Q_H$ → ↔
- $C_{u,ss} = f_u \cdot C_{ss}$ → **↑** (비례)
- 그러나 임상적으로 **거의 무의미**: 일반적으로 고추출비 약물은 IV로 잘 투여하지 않거나(투여하더라도 신중) PD 평형이 느려서 transient $C_u$ 변화가 효과로 안 나타남

**Bupivacaine이 유일 예외인 이유 (G&W p.134 명시):**
4가지 조건이 동시에 성립해야 단백결합 영향이 임상적으로 의미 있음:
1. 고추출비 (so $CL ≈ Q_H$ 둔감)
2. IV 투여 (so first-pass F↓ 우회 메커니즘 부재)
3. 좁은 치료역 (so 작은 $C_u$ 변화도 독성 진입)
4. 빠른 PK/PD 평형 (so transient $f_u$ 변화가 효과로 즉시 반영)

→ **이 네 조건을 모두 충족하는 약물은 bupivacaine 하나** [G&W *"We are only aware of one compound..."*]. 다른 모든 경우 단백결합 변화의 임상적 영향은 미미.

**TDM 함정:** 저추출비 약물에서 총 $C_{ss}$ 거의 변화 없음 — 그러나 $C_{u,ss}$는 doubling. 임상의가 총농도 기준 "정상"이라 판단하면 비결합 농도 과잉 → 독성. **고단백결합 저추출비 약물(많은 항전간제)은 비결합 농도 측정 또는 기전 이해 기반 해석 필수.**

**다음 깊이 질문:** 신부전 환자에서 albumin 감소로 $f_u$가 증가한 phenytoin을 TDM할 때? — 총 농도 목표 범위를 **하향 조정** (예: 일반 10–20 mg/L → 신부전 5–10 mg/L). 또는 **비결합 농도 직접 측정**(목표 1–2 mg/L 유지). 단순 총 농도 목표 사용은 비결합 농도 과잉을 놓침.
</details>

---

### ⭐ Q9 — 보스 딜레마 [★★]

> **시나리오:** 새 항간질제 XN-150의 Phase 1 FIH. 4개 용량 코호트(50, 100, 200, 400 mg)에서 dose-normalized AUC가 50→400 mg 구간에서 단조 상승(AUC/Dose: 1.2→2.8 ng·hr/mL/mg). 추정 $K_m'$ = 280 ng/mL (95% CI: 80–950 ng/mL), RSE 45%. 치료 목표 농도 150–300 ng/mL.
>
> **회사 규제팀:** "CI가 넓지만 MM 모델이 선형보다 OFV 12.3 낮음. Phase 2 용량 설계에 MM 모델 사용 허가."
> **안전팀:** "RSE 45%면 파라미터 불신뢰. 선형으로 외삽해야 안전."
>
> 당신은 수석 모델러로서 어떤 판단을 내리는가? 어느 쪽을 선택하든 그 결정을 어떻게 규제 문서로 방어할 것인가?

<details><summary>수석 모델러의 Trade-off 논리</summary>

**핵심 판단:** 이것은 "선형 vs MM" 선택이 아니라 **불확실성 관리의 문제**입니다.

**안전팀 취약점:** "RSE 45%면 선형으로"는 논리적으로 틀렸습니다. 선형 모델은 OFV가 더 높고 AUC/Dose vs Dose의 단조 상승을 설명하지 못합니다. **선형 외삽이 더 안전한 것이 아니라 더 틀린 것**입니다 (편향 + 작은 분산 = MSE 더 큼).

**규제팀 취약점:** RSE 45% + 95% CI (80–950 ng/mL)는 사실상 "$K_m$이 한 자릿수에서 세 자릿수까지 가능"이라는 선언입니다.
- $K_m'$=80이면: 치료 목표(150–300)가 $K_m$의 2–4배 → **상당히 비선형 구간** → 용량 증가 시 AUC 폭발 가능
- $K_m'$=950이면: 치료 목표가 $K_m$의 16–32% → 거의 선형 (그러나 G&W 10–20% 경고에 따르면 이 구간도 비선형 시작점에 가까움)

**수석 모델러의 결정 (4단계):**

① **두 모델 모두 FDA에 투명하게 보고.** MM과 선형 모델의 Phase 2 용량 예측 결과를 나란히 제시. *"Both models are presented; the MM model better describes the observed AUC/Dose pattern but with limited precision in $K_m$."*

② **Phase 2 시작 전 고용량 PK 코호트(600 mg) 추가를 FDA에 제안.** $K_m$ CI를 좁힐 수 있는 결정적 데이터. PK17 사례에서 G&W가 권장한 정확히 그 해결책.

③ **Phase 2 초기 용량은 보수적으로:** 두 모델 외삽의 하한 또는 평균 부근에서 시작, 반복 PK로 확인하며 **dose titration with PK-guided escalation**.

④ **FDA Type B meeting에서 서면화:** *"Current Phase 1 data support nonlinear PK characterized by Michaelis-Menten elimination, but parameter identifiability is sufficient for point estimation yet limited for high-dose extrapolation. A pre-Phase 2 PK supplementation cohort at 600 mg is proposed to refine $K_m$ before Phase 2 dose finalization."*

**왜 이 답이 PK17의 가르침과 일치하는가:** G&W가 PK17에서 명시한 해결책 — *"In order to discriminate between the two models, a higher dose should also be investigated"* — 을 정확히 동일한 논리로 적용한 것. **불확실성 자체가 Deficiency Letter 사유가 아니라, 그것을 인식하지 못하거나 관리 계획이 없는 것이 사유.**

**의외의 조언:** 이 시나리오에서 **선형이 안전하지 않다**는 것을 안전팀에게 설득하는 것이 가장 어려운 정치적 과제일 수 있습니다. 이때 G&W "10–20% of Km" 경고를 제시하면 — 안전팀의 직관(작은 모델이 보수적)과 통계적 사실(편향이 분산보다 크면 작은 모델이 위험)을 매개하는 강력한 카드가 됩니다.
</details>

---

## §8 — Meta-Frame & Big Picture

### A. Positioning — 28세션 아키텍처에서의 위치

I-07은 **"선형 PK의 안전한 세계가 구조적으로 붕괴되는 첫 번째 관문"**입니다.

```
I-01~I-06: 선형 PK의 세계 ──────────────────────┐
                                                  │
I-07: 비선형 PK (이 세션) ◀── 여기가 관문         │
       ↓ 공급하는 개념:                            │
       - Saturable 효소 동역학 (V_max, K_m)         │
       - C50 vs Km 위치 관계                       ↓
       - Zero-order 역설                  I-08 TMDD (saturable target binding)
       - 비선형 단백결합                   I-09 Emax PD (동형 수식의 PD 버전)
       - Time-dep induction/MBI            I-10 Indirect Response (turnover ODE)
       - TDM 실무 판단                     II-04 ADVAN13/$DES 구현
                                           II-08 PopPK 공변량 모델
                                           III-XX PBPK 간 효소 스케일링
```

- **이전:** I-01 (CL·V), I-03 (1구획 ODE), I-05 (단백결합 기초), I-06 (추출비)
- **직후:** I-08 (TMDD), I-09 (Emax), I-10 (Indirect Response), II-04 (ADVAN13/$DES)
- **결정적으로 의존하는 고급 도메인:** PopPK ($\eta$ 위치 선택), PBPK (간 효소 포화 스케일링), TMDD (PK·PD 통합), QSP (시스템 비선형성)

---

### B. Dependencies — 이 세션을 대충 넘겼을 때의 구체적 실패 모드

**실패 1:** Bosentan처럼 $V_{ss}$가 용량 의존적인 약물을 표준 2구획으로 피팅 → peripheral compartment 과잉 추정 → $CL_d$ 왜곡 → 반복 투여 축적 예측 완전히 틀림. IND 제출 시 Deficiency Letter ("the proposed model does not adequately describe the dose-dependent behavior of the volume of distribution").

**실패 2:** Zero-order 소실 약물의 oral F를 AUC 비교로 계산 → input rate 의존성 때문에 F 과소/과대 추정 → Phase 2 용량이 sub-therapeutic 또는 toxic. (Cefonicid처럼 F > 1이 나오면 즉시 saturable binding 의심)

**실패 3:** PK17 −0.96 상관과 RSE 45% 시나리오를 단순 정밀도 문제로 무시 → 외삽 위험 선언 없이 Phase 2 진행 → 치료 농도에서 AUC 폭발. **$COVARIANCE step의 condition number > 1,000**이 외삽 위험 신호임을 I-07에서 처음 체험합니다.

**실패 4:** 총농도 기반 TDM에서 $f_u$ 증가를 무시 → "농도가 낮으니 용량 증가" 판단 → 실제로는 비결합 농도 정상이거나 이미 독성 → Reye 증후군 같은 사건 발생.

**실패 5 (시간 의존성 누락):** 단회 PK로 만든 carbamazepine 투여 계획 → 2주 후 trough 50% 감소 → 발작 재발 → 환자 임의 증량 → 자가유도가 따라잡으면서 다시 감소 → 의사·환자 모두 적정 용량 감을 잃음.

---

### C. Professional Moat — 구조적 필연성 수준의 답

AI와 소프트웨어는 MM 모델을 피팅하고 $V_{max}$·$K_m$을 출력합니다. 주니어 모델러는 GOF가 좋으면 그 결과를 믿습니다.

**이 세션을 진정으로 내면화한 모델러는 다음 다섯 가지를 동시에 수행합니다:**

**① 점추정 정밀도와 외삽 신뢰성을 분리해서 판단합니다.** $COVARIANCE step 출력에서 $K_m$–$V$ 상관 −0.96, $K_m$ RSE 45%, condition number > 1,000을 보는 순간 — *"이것은 점추정 정밀도 문제가 아니라 결합 외삽 위험의 신호다. CV%는 양호해도 ridge가 좁으면 두 파라미터의 결합 불확실성이 외삽으로 전파된다"* — 라고 즉시 판단하고, FDA 방어 언어로 번역합니다 (G&W PK17이 가르치는 정확히 그 교훈).

**② Zero-order elimination + oral input의 조합에서 "AUC 비교로 F를 측정하면 틀릴 수 있다"** 는 것을 즉시 인식하고 IV microtracer 설계를 제안합니다. 그리고 "F > 1.0"이 보고되면 saturable binding의 silent fingerprint임을 즉각 의심합니다 (cefonicid).

**③ 총농도 TDM 결과를 보고 "$f_u$가 변했을 가능성, 비선형 단백결합 가능성"을 먼저 배제**한 뒤 용량 조정을 권고합니다 — 이것이 임상약사 TDM 경험과 계량약리학 기전 이해가 결합하는 지점입니다. 그리고 단백결합이 임상적으로 문제 되는 유일 사례(bupivacaine)와 그렇지 않은 다수 사례를 명확히 구분합니다.

**④ 비선형의 6가지 방향(F↑/F↓·CL↑/CL↓·V↑/V↓)**을 머릿속에 카탈로그로 갖고 있어서, AUC/Dose vs Dose 그래프 패턴 한 장으로 기전 가설을 4개로 좁힙니다. *"단조 상승 → CL↓ or F↑. 두 가능성을 분리하려면 IV comparator 또는 metabolite AUC 분석이 필요하다"*를 즉각 판단.

**⑤ Capacity vs Time vs Product Inhibition 감별을 Levy 1982 기준**으로 즉시 수행합니다. *"농도가 일정한데도 CL이 시간에 따라 변하면 시간 의존성. 농도 ↓ 후 CL이 회복되면 capacity, 회복 안 되면 product inhibition 또는 MBI."* 이 한 문장이 carbamazepine·clarithromycin·MBI 약물 전체의 임상 행동을 설명합니다.

이 다섯 가지는 알고리즘이 복제할 수 없는 **수식의 구조적 의미와 임상·규제 결과를 연결하는 인과 추론 역량**입니다. G&W의 *"The system may already behave in a nonlinear fashion at concentrations which are 10–20% of Km"*이라는 한 줄을 외운 게 아니라, 그 경고의 파급력을 **Phase 1 설계 → FDA 미팅 → Phase 2 용량 → TDM 해석 → 임상 실패 시나리오**의 전체 체인으로 추적할 수 있을 때 완성됩니다.

**그리고 이것이 8년 임상 TDM 경험을 가진 약사가 박사과정에서 가질 수 있는 가장 강력한 차별점입니다 —** AI가 모델을 피팅할 수는 있어도, 페니토인 환자 침대 옆에서 *"이 환자의 albumin 5 g/dL는 페니토인의 $f_u$ 이상을 의미하고, 따라서 총 농도 기준 TDM은 6–12 mg/L로 하향해야 한다"* 를 결정할 수 없습니다. 그 결정은 임상 + 기전이 결합한 인간 모델러의 영역입니다.

---

## ✦ v2.0 정정 및 보강 요약

### 주요 정정사항

1. **NONMEM `$ERROR` 블록의 분산-표준편차 혼동 수정** — `SIGMA**2 * IPRED**2 + SIGMA**2` → `SIGMA * IPRED**2 + SIGMA` (SIGMA는 이미 분산이므로 제곱 금지).

2. **Table 16-12 IV 고추출비 + $f_u$↑ 행 재구성** — 원본 R&T Table 16-12은 student의 study problem 빈 표라는 사실을 누락했었음. 본문(pp.511–512) 기반 재구성: IV 고추출비에서 $CL ≈ Q_H$ flow-limited → 총 $C_{ss}$ ↔, 비결합 $C_{u,ss}$ ↑.

3. **PK17 −0.96 상관의 표현 정정** — "structural identifiability 실패"는 G&W 원문보다 강한 표현. 정확한 표현은 "**높은 파라미터 상관 + 협소한 농도 범위 → 외삽 위험 (정밀도는 양호)**." 이는 G&W p.554 *"the parameter precision is still good"* 직접 인용.

### 누락 보강사항

4. **Bupivacaine — IV 고추출비 + $f_u$↑가 임상적으로 의미 있는 유일 예외** (G&W p.134 직접 인용). 4가지 조건(IV + 고추출비 + 좁은 치료역 + 빠른 PD 평형)이 동시 성립해야 함.

5. **R&T Fig 16-8 vignette — Zero-order paradox 극한 사례.** $R_0 = V_m$ × 5시간 주입 시 이론적 AUC = 0 (R&T p.502 직접 인용).

6. **AUC/Dose vs Dose 4가지 패턴** (G&W §2.7.1) — flat / 단조 상승 / 단조 감소 / plateau의 구조적 진단.

7. **저농도 알코올의 perfusion limit** — $V_m/K_m$ ≈ 100 L/hr > 간 혈류 → 매우 낮은 농도에서 알코올이 사실상 flow-limited (R&T p.501).

8. **Clarithromycin MBI** — 7th dose 후 반감기 추가 연장 (R&T Fig 16-26).

9. **Levy 판별 4-way 표** (Capacity / Induction / MBI / Product Inhibition) 통합.

---

### Filing & Tagging

```yaml
저장 위치:
  - 02_LITERATURE/024_Gabrielson-Textbook/  # 챕터 정리 + 검증 노트
  - 01_ZETTELKASTEN/013_PopPK-NONMEM/       # 핵심 atom 노트들
파일명: 2026-04-30_I07_비선형PK_거장의시각_정정통합본.md
태그:
  - #pharmacometrics/pk/nonlinear/capacity
  - #pharmacometrics/pk/nonlinear/binding
  - #pharmacometrics/pk/nonlinear/time-dependent
  - #nonmem/error-model
  - #nonmem/DES/ADVAN13
  - #clinical/TDM/phenytoin
  - #regulatory/FDA-deficiency-letter
  - #P3_Audit  ;; 1차본 오류 검증 통과
  - #P1_Action ;; 다음 액션: HTML 컴파일러 실행
링크:
  - "[[NONMEM_sigma_variance_vs_sd]]"
  - "[[High_E_drug_protein_binding_bupivacaine_exception]]"
  - "[[MM_소실_동역학]]"
  - "[[C50_vs_Km_위치_관계]]"
  - "[[Zero_order_paradox]]"
  - "[[salicylate_4단계_워크플로우]]"
  - "[[carbamazepine_자가유도]]"
  - "[[clarithromycin_MBI]]"
  - "[[bosentan_TMDD_브리지]]"
```

---

```
─────────────────────────────────────────────────────
✦ I-07 정정통합본 (v2.0) 완료 — HTML Step 2 ready

  • §1 헤더 & 로드맵 (3-레이어 + 지식 그래프)
  • §2 개념 해부 카드 11개 (Apex: MM 소실 동역학)
  • §5 혼동 쌍 5개 (Critical Blow: Vmax vs Km)
  • §7 Self-test 9문제 (보스 딜레마 포함, 모두 정답 공개 + 다음 깊이 질문)
  • §8 메타프레임 — Positioning · Dependencies · Professional Moat (5가지)
  • v2.0 정정 3건, 누락 보강 6건 (총 9건)
  • Source citations: G&W §2.7, PK17, PK21 + R&T Ch.16
  • Style: HTML Step 2 컴파일 ready
    - LaTeX MathJax 호환
    - Micro-citation tag style
    - 거장의 시각 강조 박스 marker (▬ ━━ [거장의 시각])
    - Self-test details/summary 인터랙티브 호환
─────────────────────────────────────────────────────
```

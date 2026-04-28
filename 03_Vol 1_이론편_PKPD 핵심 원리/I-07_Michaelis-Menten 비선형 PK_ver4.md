아래는 I-07 세션 Step 1의 **친절한 재표현본**입니다. 내용은 원본과 동일하나, 흐름이 그림처럼 그려지도록 각 개념의 진입 방식을 다듬었습니다.

---

# ✦ STEP 1 — I-07 비선형 PK: 비선형이 보이면 "방향"을 먼저 읽어라

> **소스**: Rowland & Tozer 5e Ch.16 (pp.491–529) + Gabrielsson & Weiner 5e §2.7.1–2.7.5, PK17, PK21
> **감지된 소스 유형**: Vol I 혼합 (R&T 임상 기전 + G&W 수식·데이터)

---

## 🗺️ 이 세션을 읽기 전에 — 전체 지도 먼저

> **비선형 PK를 배우기 전에 한 장면을 상상해 보세요.**
>
> 페니토인(항경련제) 환자에게 300 mg/day를 쓰고 있었는데 효과가 없어서 500 mg/day로 올렸더니, 혈중농도가 4 mg/L에서 36 mg/L로 **9배** 뛰어버렸습니다. 용량은 67% 올렸을 뿐인데. 환자는 독성 증상(안구진탕, 운동실조)으로 응급실에 옵니다.
>
> 비타민 C(아스코르브산)는 하루 75 mg을 먹을 때 혈중농도가 9 mg/L인데, **133배**인 10,000 mg으로 올려도 농도는 고작 19 mg/L(2배)로 밖에 안 오릅니다. 용량과 농도의 관계가 정반대로 이상합니다.
>
> **이 두 이상한 현상의 공통된 원인이 바로 비선형 PK입니다.** 이 세션은 그 '이상함'이 어떤 구조에서 오는지를 체계적으로 해부합니다.

---

## §1 — 세션 헤더 & 로드맵

### Big Idea (한 문장)

비선형 PK는 "농도가 폭발하는 이상한 현상"이 아니라, **dose-normalized 관찰값이 superimpose하지 않는 구조적 붕괴**이며, 그 붕괴의 **방향**($F$↑/$F$↓/$CL$↑/$CL$↓/$V$↑/$V$↓)을 먼저 읽어내는 것이 수석 모델러의 핵심 임무다.

> 💡 **"superimpose한다"는 게 무슨 뜻인가?**
> 100 mg 투여와 200 mg 투여 후의 농도-시간 곡선을 각각 용량으로 나눠서 겹쳐 그렸을 때, 두 곡선이 **딱 포개지면** 선형(linear) PK입니다. 200 mg 투여 시 모든 시점에서 농도가 정확히 2배라는 뜻이니까요. 이게 "중첩 원리(principle of superposition)"입니다. 이것이 깨지면 비선형입니다.

---

### 개념 항법도 — 이 세션에서 다루는 개념들

이 세션은 크게 **세 개의 레이어**로 구성됩니다.

```
[레이어 1] 진단 프레임워크
  → 비선형을 어떻게 알아보는가? (EDA, 4단계 워크플로우)
  → 왜 대부분의 PK는 선형인가? (C50 vs Km 위치 관계)

[레이어 2] 각 기전별 수식과 사례
  → Michaelis-Menten 소실 ← 이 세션의 핵심 보스
  → 입력속도 Catastrophe (페니토인, 알코올)
  → 혼합 병렬 경로, saturable first-pass
  → 신배설 비선형, 단백결합 비선형, 시간의존성

[레이어 3] 종합 진단 도구
  → R&T 4단계 워크플로우 완전 적용 (salicylate)
  → Table 16-12 방향성 종합표
```

---

### 지식 그래프 위치

```
[선행 필수]                    [이 세션]                   [이 세션 이후]
I-01 CL·V 기본        →      I-07 비선형 PK      →      I-08 TMDD
I-03 1구획 ODE        →      (여기가 선형→비선형  →      I-09 Emax PD
I-05 단백결합 기초     →       전환의 관문)         →      II-04 ADVAN13/$DES
```

> 이전 세션들이 "평평한 고속도로"를 달리는 법을 가르쳤다면, I-07은 그 도로가 **갑자기 경사지고 굽어지는 구간에서** 어떻게 판단하는지를 가르칩니다.

---

## §2 — 개념 해부 카드

---

### 🃏 카드 1. 진단학으로서의 비선형 PK — 거장이 먼저 보는 좌표계

---

#### ━━ [거장의 시각: 왜 이 카드가 가장 먼저인가] ━━

**왜 치명적으로 중요한가:**
비선형 PK를 보면 많은 사람이 반사적으로 "대사 포화(CL↓)"를 떠올립니다. 하지만 비선형의 실제 원인은 **여섯 가지 방향** 중 하나입니다.

| 방향 | 의미 | 대표 기전 |
|---|---|---|
| $F$↓ | 흡수 감소 | 용해도 제한, 능동 수송 포화 |
| $F$↑ | 흡수 증가 | **Saturable first-pass** — 역방향! |
| $CL$↓ | 소실 감소 | 대사 효소 포화 (페니토인) |
| $CL$↑ | 소실 증가 | 자가유도, 신배설 재흡수 포화 |
| $V$↓ | 분포 감소 | 조직 표적결합 포화 (bosentan) |
| $V$↑ | 분포 증가 | 단백결합 포화 |

"대사 포화 → $F$↓"로만 반사적으로 연결하면, **$F$↑ 기전(saturable first-pass)**을 정반대로 예측하게 됩니다. 이 하나의 오해만으로도 고용량 임상시험 설계가 완전히 뒤집힙니다.

**체화해야 할 단 하나의 직관:**
비선형이 관찰되면, 가장 먼저 던져야 할 질문은 *"왜 폭발했는가?"*가 아니라 **"dose-normalized값이 어느 방향으로 superimpose를 실패했는가?"**입니다. 방향이 기전을 결정하고, 기전이 임상 처방을 결정합니다.

---

#### A. 정의 — "선형"과 "비선형"을 정확하게 구분하기

> **중요한 전제:** 동일한 투여 경로, 동일한 제형, 동일한 투여 방법으로 각각 다른 용량을 투여했을 때를 비교해야 합니다. 경로나 제형이 달라서 superimpose가 실패하면, 그건 비선형이 아니라 그냥 방법이 다른 것입니다.

$$\text{선형(Linear)} = \text{dose-normalized 농도·AUC·소변 회수율이 모든 시점에서 superimpose}$$

$$\text{비선형(Nonlinear)} = \text{superimpose 실패} = \text{하나 이상의 PK 파라미터가 용량에 따라 변함}$$

**시간 의존성(time-dependent)의 정의** — Levy [1982] 인용:
> *"만약 그것이 진정한 시간 의존성 시스템이라면, 약물 농도가 시간 불변인 상태에서 약물 청소율이 시간과 함께 변해야 한다."*

> 💡 **핵심 구분**: 농도가 변하기 때문에 CL이 변하면 → **용량(capacity) 의존성**. 농도와 무관하게 시간이 지나면서 CL이 변하면 → **시간(time) 의존성**. 이 둘은 원인도, 임상 결과도, NONMEM 모델 구조도 완전히 다릅니다.

---

#### B. Gabrielsson EDA 권장 절차 — 데이터를 받으면 이 순서로 그려라

**G&W §2.7.1의 핵심 조언:** 모델을 세우기 전에 반드시 그림부터 그려라.

1. **Linear plot** → 전체 패턴 확인
2. **Semi-log plot** → 기울기가 일정한지(선형) vs. 시간에 따라 변하는지(비선형) 확인
3. **Dose-normalized C-time plot** → 서로 다른 용량의 곡선이 겹치는지 확인
4. **AUC vs Dose** → 선형이면 직선
5. **AUC/Dose vs Dose** ← **가장 중요한 그래프**

> 💡 **AUC/Dose vs Dose 그래프 읽는 법:**
>
> | AUC/Dose 패턴 | 의미 |
> |---|---|
> | 수평선 (flat) | 선형 PK — 정상 |
> | **단조 상승** | CL↓ 또는 F↑ → MM 소실(페니토인), saturable first-pass |
> | 단조 감소 | CL↑ 또는 F↓ → 자가유도, 흡수 포화 |
> | 저용량 상승 후 plateau | MM + 1차 병렬 경로 혼합 → salicylate |

[출처: G&W 5e, §2.7.1, Figure 2.86, p.113]

---

#### C. R&T Table 16-1 — 비선형이 올 수 있는 모든 과정의 지도

> 이 표는 이 세션 전체의 **목차**입니다. 각 행이 이후 개별 카드에서 깊게 다뤄집니다.

| 과정 | 기전 | PK 파라미터 방향 | 대표 약물 |
|---|---|---|---|
| 용해도 | Limited solubility | $F$↓ | Griseofulvin |
| 장관 능동수송 | Saturable active absorption | $F$↓ | Amoxicillin |
| **Efflux transport 포화** | P-gp 포화 → 흡수 증가 | **$F$↑** | Protease inhibitors, fexofenadine |
| 신 분비 포화 | Tubular secretion 포화 | $CL_R$↓ | Penicillin G |
| 신 재흡수 포화 | Active reabsorption 포화 | $CL_R$↑ | Ascorbic acid |
| 대사 포화 | Capacity-limited | $CL$↓ | **Phenytoin**, voriconazole |
| **Saturable first-pass** | 초회통과 대사 포화 | **$F$↑** | **Nicardipine**, methylphenidate |
| 자가유도 | Autoinduction | $CL$↑ | Carbamazepine |
| MBI(자가억제) | Suicide substrate | $CL$↓ | Clarithromycin |
| 단백결합 포화 | Saturable plasma binding | $V$↑, $CL$↑ or ↔ | Salicylate, naproxen |
| **TMDD** | 표적 결합 포화 | $V$↓ | **Bosentan**, imirestat |

[출처: R&T 5e, Ch.16, Table 16-1, p.496]

> ⚠️ **Efflux transport 포화 함정 강조:** P-glycoprotein 같은 efflux transporter(장벽에서 약물을 다시 장 안으로 밀어내는 단백질)가 포화되면 약물이 더 많이 흡수됩니다($F$↑). 용량이 늘수록 AUC가 "더 많이" 증가하는 역방향 비선형입니다. 대사 포화($F$↓)와 방향이 정반대이므로 혼동에 주의하세요.

---

#### D. R&T 4단계 비선형 인식 워크플로우 — 현장에서 쓰는 순서

> 데이터를 보면서 이 4단계를 밟으면, 어떤 비선형 약물도 체계적으로 분석할 수 있습니다. (§2 카드 10에서 salicylate로 완전 적용)

**Step 1.** Dose-normalized 비교 → superimpose 실패 확인 ("비선형인가?")
**Step 2.** 변화한 파라미터의 **방향** 식별 ("무엇이, 어느 방향으로?")
**Step 3.** Primary PK 파라미터 결정 → $CL_H$, $CL_R$, $V$, $K_a$, $F$, $f_u$ 중 어느 것?
**Step 4.** 가정된 기전과 관찰 일치 여부 확인 ("설명이 되는가?")

---

#### G. Zettelkasten Atom

```yaml
aliases: [비선형 PK 진단, superposition 붕괴, dose-dependent kinetics]
tags: [pharmacometrics/pk/nonlinear, clinical/TDM, methodology/EDA]
source: "R&T 5e, Ch.16, pp.491–496, 519–521; G&W 5e, §2.7.1, pp.112–113"
```

비선형 PK 진단의 핵심은 superposition 붕괴의 **방향** 읽기이며, AUC/Dose vs Dose 그래프 기울기 방향과 R&T 4단계 워크플로우가 체계적 역추론의 도구다.

---

### 🃏 카드 2. C50 vs Km 위치 관계 — "왜 PK는 대체로 선형인가?"

---

#### ━━ [거장의 시각] ━━

**왜 치명적으로 중요한가:**
"비선형 PK는 드문 현상인가?"라는 질문에 대한 R&T의 명쾌한 답이 이 카드에 있습니다. 이것을 모르면, 비선형 PK 약물이 "특이한 예외"처럼 보이지만, 사실은 **구조적으로 예측 가능한 예외**입니다.

**체화해야 할 단 하나의 직관:**
약물 개발팀은 항상 더 강력한 약(낮은 $C_{50}$)을 추구합니다. 그런데 효능이 강할수록 치료 농도가 낮아지고, 낮은 치료 농도는 자동으로 효소 포화 농도($K_m$)보다 훨씬 아래에 위치합니다. 결과적으로 **"효능 추구"가 역설적으로 PK의 선형성을 보장**합니다.

---

#### A & B. 핵심 관계 — C50과 Km의 위치가 전부를 결정한다

$$E = \frac{E_{max} \cdot C^{\gamma}}{C_{50}^{\gamma} + C^{\gamma}} \quad \text{(PD: Emax 모델)}$$

$$Rate = \frac{V_m \cdot C_{u_H}}{K_m + C_{u_H}} \quad \text{(PK: MM 대사 속도)}$$

> 💡 이 두 수식은 **수학적으로 완전히 동일한 형태**입니다. 분자의 파라미터만 $E_{max}$ vs $V_m$으로 다를 뿐. PD는 "항상 비선형", PK는 "대체로 선형"인 이유는 수식 구조의 차이가 아니라 **$C_{50}$과 $K_m$의 위치 차이**입니다.

**실제 수치 앵커 (R&T Fig 16-3, p.497):**

| 약물 | CYP3A $K_m$ | 약효 $C_{50}$ | 비율 | PK 결과 |
|---|---|---|---|---|
| Midazolam | ≈ 3.3 µM | ≈ 0.05 µM (진정) | **66배 차이** | PK ≈ 선형 |
| **Phenytoin** | ≈ 4 mg/L (총) | 10–20 mg/L | **동일 범위** | **비선형!** |
| **Alcohol** | Km ≈ 100 mg/L | C50 > 200 mg/L | **Km < C50** | **비선형!** |
| TMDD 약물 (bosentan) | (Kd 수준) | ≈ Kd | 동일 범위 | **비선형!** |

> 🔑 **규칙으로 외우기:** "비선형 PK는 치료 농도가 $K_m$에 가까운 약물에서 온다." Phenytoin, alcohol, TMDD 약물이 예외적인 이유는 **치료 농도 자체가 효소 포화 농도 근처**이기 때문입니다.

**임상·규제 함의:**
Phase 1 FIH(First-in-Human) 용량 설계 시, in vitro $K_m$ 추정치와 목표 치료 농도를 반드시 비교해야 합니다. 치료 농도가 $K_m$에 근접하면 고용량 코호트에서 폭발적 비선형을 만날 수 있습니다.

---

### 🃏 카드 3. ⚡ Michaelis-Menten 소실 동역학 [Apex Concept]

> ⚡ **이 카드가 세션 전체의 보스입니다.** 이하의 모든 카드(페니토인, 알코올, salicylate, cefonicid)는 이 카드의 "응용 사례"입니다. 이 카드의 직관을 완전히 장착하면, 나머지는 자동으로 따라옵니다.

---

#### ━━ [거장의 시각] ━━

**왜 치명적으로 중요한가:**
페니토인 300 mg/day→500 mg/day 증량 시 혈중농도 4→36 mg/L (9배 폭증)으로 독성 뇌증이 발생합니다. 이것은 "의사의 실수"가 아니라 **MM 동역학의 수학적 필연**입니다. 그리고 PK17처럼 데이터가 $K_m$ 주변 곡률을 충분히 포함하지 않으면 $V_{max}$와 $K_m$이 분리 추정 불가능해서, 선형처럼 보이는 피팅 결과가 Phase 2 독성 폭발을 유발합니다.

**체화해야 할 단 하나의 직관:**

> **"고농도에서 maximal인 것은 rate(소실 속도)이고, 저농도에서 maximal인 것은 clearance(청소율)이다."**

이 두 축을 헷갈리면 모든 임상·NONMEM 추론이 거꾸로 됩니다.

> 💡 **공장 비유로 영구히 각인하기:**
>
> - **Rate** = "하루 총 생산량" → 원료(약물)가 넘치면 최대, 부족하면 감소
> - **Clearance** = "원료 단위당 처리 효율" → 원료가 넘치면 효율 바닥, 원료가 희박하면 효율 최고
>
> 공장에 원료가 넘쳐흐를 때(고농도): 생산량(Rate)은 최대지만 효율(CL)은 바닥. 원료가 희박할 때(저농도): 효율(CL)은 최고지만 생산량(Rate)은 적다.

---

#### A. 정의

약물 소실 속도가 효소 포화로 인해 농도에 비례하지 않고, 최대 소실 속도 $V_{max}$에 점근하는 saturable 과정. 치료 농도가 $K_m$에 근접하거나 초과할 때 비선형이 됩니다.

---

#### B. 수식 체계 — 단계별로 쌓기

**Step 1. 선형 기준선 (비교 대상)**

$$\frac{dC}{dt} = -\frac{CL}{V} \cdot C \quad \text{여기서 CL은 상수} \tag{G\&W Eq.2:265}$$

**Step 2. MM clearance 도입 — CL이 농도의 함수가 됨**

$$CL(C) = \frac{V_{max}}{K_m + C} \tag{G\&W Eq.2:266}$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $V_{max}$ | µg/min | 효소 총량에 비례하는 최대 대사 속도 | 유도↑, 간경변↓ |
| $K_m$ | µg/mL | 소실 속도 = $V_{max}/2$일 때의 농도 = 효소 친화도의 역수 | 경쟁억제↑ |

[출처: G&W 5e, §2.7.2, Eq.2:266, p.115; R&T 5e, Ch.16, Eq.16-1~2, p.494]

> 💡 **$K_m$의 직관:** $K_m$이 낮을수록 효소와 약물의 친화도가 높습니다(소량만 있어도 잘 처리). $K_m$이 높을수록 효소가 약물에 둔감합니다(농도를 높여야 절반 속도에 도달).

**Step 3. Rate vs CL 이중 극한 — 알코올 Table 16-3으로 수치 확인**

R&T Table 16-3: $V_m=10$ g/hr, $K_m=100$ mg/L인 알코올의 농도별 Rate와 CL:

| 혈중 농도 (mg/L) | Rate (g/hr) | CL (L/hr) |
|---|---|---|
| 7,000 | **9.9** | **1.4** |
| 1,000 | 9.1 | 9.1 |
| 200 | 6.7 | 33 |
| 100 | 5.0 | 50 |
| **10** | **0.91** | **91** |

[출처: R&T 5e, Ch.16, Table 16-3, p.500]

> 🔑 **이 표에서 읽어야 할 것:** 농도가 700배 감소(7,000→10 mg/L)할 때 Rate는 10배 감소하지만, CL은 65배 증가합니다. Rate와 CL은 같은 방정식의 서로 다른 얼굴입니다. 이 비대칭성이 모든 임상 함의의 출발점입니다.

**Step 4. IV Bolus ODE**

$$\frac{dC}{dt} = -\frac{V_{max} \cdot C}{K_m + C} \cdot \frac{1}{V} \tag{G\&W Eq.2:270}$$

**Step 5. 상수속도주입 ODE**

$$\frac{dC}{dt} = \left( Input - \frac{V_{max} \cdot C}{K_m + C} \right) \cdot \frac{1}{V} \tag{G\&W Eq.2:273}$$

> ⚠️ **치명적 주의:** Input > $V_{max}$이면 $dC/dt > 0$ 항상 → **항정상태 수학적으로 불가능**. PK17의 slow infusion rate = 138.4 µg/min > $V_{max}$ = 107 µg/min이므로, 이 실험으로는 원리상 $C_{ss}$를 관찰할 수 없습니다. 이것이 PK17이 "pilot study에 불과"한 첫 번째 이유입니다.

**Step 6. AUC (IV bolus, 1구획)**

$$AUC = \frac{C^0}{V_{max} \cdot 2} \cdot \left[K_m + \frac{C^0}{2}\right] \tag{G\&W Eq.2:271}$$

> 💡 **AUC가 이차함수인 이유:** 전개하면 $AUC = \frac{K_m \cdot C^0}{2V_{max}} + \frac{(C^0)^2}{4V_{max}}$. 첫 항은 $C^0$에 선형, 둘째 항은 $C^0$의 제곱. 저농도에서는 첫 항 지배 → 선형처럼 보이지만, 농도가 올라가면 제곱항이 지배하여 AUC가 폭발합니다. "고농도 코호트 없이 비선형을 포착하기 어렵다"는 말의 수학적 근거입니다.

[출처: G&W 5e, Eq.2:271, p.117]

**Step 7. 순간 반감기 — 선형 PK와 정반대 방향**

$$t_{1/2}^{inst}(C) = \ln(2) \cdot \frac{V}{V_{max}} \cdot (K_m + C) \tag{G\&W Eq.2:272; PK17 Eq.17:3}$$

> 🔑 **선형 PK vs MM PK 반감기 비교:**
>
> | | 선형 PK | MM PK |
> |---|---|---|
> | 반감기 방향 | 농도 무관, 일정 | **농도↑ → 반감기↑** |
> | Semi-log 기울기 | 일정한 직선 | 시간이 지날수록 **가팔라짐** |
> | $5\times t_{1/2}$ 규칙 | 사용 가능 | **사용 불가** |
>
> G&W 경고: **$K_m$의 10–20% 농도에서 이미 비선형이 시작된다.** "$K_m$을 넘어야 비선형"이라는 단순화는 위험합니다.

**Step 8. 두 극한 조건**

$$C \gg K_m: \quad Rate \approx V_{max} \quad \text{(zero-order, 영차)} \tag{Eq.2:268}$$
$$C \ll K_m: \quad Rate \approx \frac{V_{max}}{K_m} \cdot C = K' \cdot C \quad \text{(first-order, 일차)} \tag{Eq.2:269}$$

---

**PK17 실제 파라미터** (Agent X, single subject): [출처: G&W 5e, PK17, pp.553–555]

| 파라미터 | Linear 모델 | MM 모델 | CV% |
|---|---|---|---|
| $V$ (mL) | 1,380 | **1,450** | 5 |
| $CL$ (mL/min) | 43.3 | — | — |
| $V_{max}$ (µg/min) | — | **107** | **2** |
| $K_m$ (µg/mL) | — | **0.56** | 5 |

> 🔑 **PK17 두 가지 핵심 경고:**
>
> **①** 최단 $t_{1/2}$ ≈ 5 min (C=0 기준), 선형 모델 예측 ≈ 20 min → **4배 차이**. 선형으로 외삽하면 Phase 2 용량 설계가 완전히 틀립니다.
>
> **②** $K_m$–$V$ 상관 = **−0.96** → structural identifiability 실패. 이는 "$V_{max}$와 $K_m$을 독립적으로 신뢰할 수 없다"는 선언입니다. 실제로 우리가 추정한 것은 $V_{max}/K_m$ 비율 하나에 가깝습니다. 이 상태로 Phase 2 용량을 외삽하면 위험합니다.

---

#### NONMEM 구현 코드 (L5)

```fortran
$SUBROUTINES ADVAN13 TOL=6    ;; user-defined DES — 확장성 최대

$MODEL
  COMP (CENTRAL)               ;; CMT=1, S1 참조

$PK
  VMAX = THETA(1) * EXP(ETA(1))   ;; µg/min
  KM   = THETA(2) * EXP(ETA(2))   ;; µg/mL
  V    = THETA(3) * EXP(ETA(3))   ;; mL
  S1   = V        ;; ⚠️ 단위 함정 참조

$DES
  C       = A(1) / V               ;; 현재 농도 (µg/mL)
  RATE_EL = VMAX * C / (KM + C)    ;; 소실 속도 (µg/min)
  DADT(1) = R1 - RATE_EL           ;; R1: NONMEM이 RATE column에서 자동 공급

$ERROR
  IPRED = A(1) / S1
  W     = SQRT(SIGMA(1,1)**2 * IPRED**2 + SIGMA(2,2)**2)
  Y     = IPRED + W * EPS(1)

$THETA
  (0, 107)   ;; VMAX — PK17 기준
  (0, 0.56)  ;; KM
  (0, 1450)  ;; V

$OMEGA BLOCK(1)
  0.04        ;; IIV-VMAX
$OMEGA BLOCK(1)
  0.04        ;; IIV-KM
$OMEGA BLOCK(1)
  0.04        ;; IIV-V

$SIGMA
  0.04        ;; proportional error
  0.1         ;; additive error (µg/mL)²

$ESTIMATION METHOD=1 INTERACTION MAXEVAL=9999
$COVARIANCE PRINT=E
```

> ⚠️ **S1 단위 함정 (가장 흔한 silent error):**
> - `A(1)`의 단위 = µg (약물량)
> - `V`의 단위 = mL
> - `S1 = V`로 설정해야 IPRED = µg/mL (농도 단위)
>
> S1을 설정하지 않으면 NONMEM은 `A(1)` 자체(= µg)를 IPRED로 출력합니다. 단위가 틀려도 모델이 "수렴"하는 척 할 수 있어서, 이 오류는 소리 없이 모든 파라미터 추정을 망칩니다.

> 💡 **ADVAN10 대안:** 1구획 MM 내장, 파라미터명 `VM`, `KM` 직접 사용. 단순하지만 2구획·병렬 경로 확장 불가.

---

#### C. Structural Necessity — 왜 쌍곡선 형태인가

MM 방정식이 쌍곡선인 이유: **quasi-steady-state 가정** (효소-기질 복합체[ES]가 자유 기질보다 훨씬 빠르게 평형)에서 유일하게 유도됩니다. 이 가정이 깨지면(효소 농도 ≈ 기질 농도) → TMDD 모델로 확장 필요.

---

#### ⚡ C-2. Plausible Fallacy — 가장 위험한 그럴싸한 오류

**오류:** "$K_m$보다 훨씬 낮은 치료 농도에서 선형 PK 확인 → 고용량 AUC 선형 외삽 허용."

**왜 그럴싸한가:** 저용량 Phase 1에서 dose-normalized 프로파일이 superimpose되고 GOF도 좋습니다. 논리적으로 합리적으로 들립니다.

**나비효과:** G&W가 명시한 대로 $K_m$의 **10–20%에서 이미 비선형이 시작**됩니다. $K_m = 1$ µg/mL인 약물이라면 **0.1–0.2 µg/mL부터 이미 비선형 구간**입니다. 이를 무시하고 Phase 2 설계 시 목표 농도 계산이 완전히 틀립니다.

**NONMEM 진단 시그니처 — "정현파 CWRES 편향(Sinusoidal CWRES Bias)":**
- CWRES가 고농도에서 체계적 양(+) 편향
- 저농도에서 체계적 음(−) 편향
- GOF에서 고농도 구간에서 systematic underprediction

---

#### D. 가정 및 경계조건

- 1구획 순간 혼합: 위반 시 분포상이 MM 파라미터와 혼동됨
- 단일 효소 경로($f_m=1$): 병렬 경로 존재 시 비선형성 완화
- $K_m$·$V_{max}$ 시간 불변: 자가유도 시 $V_{max}(t)$로 확장 필요
- Input ≤ $V_{max}$: 초과 시 $C_{ss}$ 수학적으로 불가능

---

#### G. Zettelkasten Atom

```yaml
aliases: [Michaelis-Menten PK, MM 소실, 포화 동역학, capacity-limited]
tags: [pharmacometrics/pk/nonlinear/capacity, nonmem/DES/ADVAN13, clinical/TDM/phenytoin]
source: "G&W 5e, §2.7.2, PK17 pp.553–555; R&T 5e, Ch.16, pp.493–500"
```

MM 소실의 핵심: **저농도 = maximal CL, 고농도 = maximal Rate**. $K_m$의 10–20%에서 이미 비선형 시작. Input > $V_{max}$ → $C_{ss}$ 불존재. PK17 상관 −0.96 = structural identifiability 실패. S1=V 설정이 NONMEM에서 가장 흔한 silent unit error.

---

### 🃏 카드 4. 입력 속도 Catastrophe — Phenytoin & Alcohol + Zero-order 역설

---

#### ━━ [거장의 시각] ━━

**왜 치명적으로 중요한가:**
페니토인에서 **bioavailability 12% 변화**(제형 교체: 0.85→0.95)가 $C_{ss}$를 **2배**(12→25 mg/L)로 올려 독성 진입시킵니다. 그리고 알코올은 zero-order 소실에서 **느리게 투여하면 AUC가 오히려 감소**하는 — 선형 PK와 정반대의 — 역설을 보여줍니다.

**체화해야 할 단 하나의 직관:**
발산 경계는 $R_0 \to V_m$이고, $V_m$ 변화는 **비선형 폭발**, $K_m$ 변화는 **선형 비례**입니다. 그리고 zero-order 소실에서 느린 흡수는 AUC를 줄입니다.

---

#### A. 항정상태 농도 공식

$$C_{u,ss} = \frac{K_m \cdot R_0}{V_m - R_0} \tag{R\&T Eq.16-6, p.501}$$

> 💡 **이 수식이 말하는 것:**
> 분모가 $(V_m - R_0)$입니다. $R_0$가 $V_m$에 가까워질수록 분모가 0에 수렴하고, $C_{ss}$는 **무한대**로 발산합니다. 이것이 "발산 경계"입니다. 마치 차가 벽에 점점 가까이 가면서 속도를 줄이지 않으면 충돌하는 것처럼, $R_0$가 $V_m$에 가까이 갈수록 농도는 폭발합니다.

**페니토인 정량 예시** ($K_m'=4$ mg/L, $V_m=500$ mg/day, $V=50$ L): [출처: R&T 5e, Fig 16-10, p.505]

| $R_0$ (mg/day) | $C_{ss}$ (mg/L) | 비고 |
|---|---|---|
| 300 | 6.0 | 치료역 미달 |
| 350 | 9.3 | |
| 400 | 16.0 | 치료역 내 |
| 425 | 22.7 | 독성 경계 |
| **500 (= $V_m$)** | **∞** | **항정상태 불가능** |

---

#### B. $V_m$ 변화 vs $K_m$ 변화의 비대칭성 — 임상에서 가장 중요한 구분

$$\frac{C_{u,ss,2}}{C_{u,ss,1}} = \frac{V_{m1} - R_0}{V_{m2} - R_0}$$

- **$V_m$ 20% 감소** (간경변, $500→400$ mg/day, $R_0=300$): 분모 200→100 → $C_{ss}$ **2배**
- **$K_m$ 50% 증가** (cimetidine, $4→6$ mg/L): $C_{ss}$ **50% 선형 비례** 증가

> ⚠️ **임상 함정:** "cimetidine이 페니토인 독성을 유발한다"고 많이 가르치지만, 실제 영향($K_m$ 50%↑ → 농도 50%↑)은 선형이고 예측 가능합니다. **진짜 위험은 간경변·약물상호작용으로 $V_m$이 조금만 줄 때** — 이때 비선형 폭발이 일어납니다.

---

#### C. Bioavailability 변화 → Css 폭발 계산

R&T 예시 (p.503–504): $K_m'=3$ mg/L, $V_m=425$ mg/day 환자, F=0.85, 200mg q12h:
- 현재 $R_0 = 0.85 \times 400 = 340$ mg/day → $C_{ss} = 12$ mg/L

제형 전환 후 F=0.95:
- 새 $R_0 = 0.95 \times 400 \approx 380$ mg/day
$$C_{ss}' = \frac{3 \times 380}{425 - 380} = \frac{1140}{45} = \mathbf{25.3} \text{ mg/L}$$

**→ 12% bioavailability 증가 → $C_{ss}$ 2배 폭발.** 이것이 페니토인 제형 변경 시 반드시 TDM을 시행해야 하는 정량적 근거입니다.

---

#### D. Pseudosteady-state 현상 — "왜 페니토인 TDM은 1달 기다려야 하는가"

시간 도달 공식:
$$t_{90} = \frac{K_m' \cdot V(2.303 \cdot V_m - 0.9 R_0)}{(V_m - R_0)^2} \tag{R\&T Eq.16-10, p.504}$$

R&T Fig 16-11: 250→200 mg/day 감량 후 **23일** 뒤에야 새 $C_{ss}$ 도달. 20% 감량 → 50% $C_{ss}$ 감소.

> 💡 **왜 이렇게 오래 걸리는가?** 분모의 $(V_m-R_0)^2$ 항을 보세요. $R_0$가 $V_m$에 가까울수록 분모가 작아지고 $t_{90}$이 급격히 커집니다. 이것은 선형 PK의 "$5 \times t_{1/2}$"과 전혀 다른 물리입니다. 임상 실무 규칙: **페니토인 TDM은 용량 변경 후 최소 3–4주 뒤.**

---

#### E. 알코올 — Zero-order elimination의 3가지 결과

**(1) $C_{ss}$ 계산 ("virtual impunity" 예시)**

한 잔/시간 (=14 g/hr) 음주: 14 g/hr > $V_m$ 10 g/hr → 항정상태 불가능 → 농도 무한 축적.

반 잔/시간 (=7 g/hr): $R_0 < V_m$이므로:
$$C_{ss} = \frac{100 \times 7}{10 - 7} = \frac{700}{3} = \mathbf{233} \text{ mg/L}$$
약하게 취하는 수준. 이것이 "반 잔씩 마시면 거의 효과 없는" 이유입니다.

**(2) 치사 축적 계산**
- $V$ ≈ 42 L/70 kg, 치사 농도 ≈ 5,000 mg/L → 체내 필요량 ≈ **200 g**
- 14 g/hr: 초과분 4 g/hr → 200 g 축적에 **50시간 (약 2일)**
- 4잔/hr (56 g/hr): 초과분 46 g/hr → **5시간** 내 치사

**(3) Zero-order paradox — 가장 반직관적인 핵심 ★★★**

> 💡 **이 개념이 선형 PK와 완전히 반대입니다.** 직접 그림으로 비교:

| | 선형 소실 | Zero-order(MM) 소실 |
|---|---|---|
| Input rate 절반으로 감소 시 AUC | **불변** ($AUC = Dose/CL$, CL 일정) | **감소** |
| 이유 | CL이 일정하므로 총 제거량 = 총 투여량 | 주입 기간 동안 약물이 일정 속도로 계속 제거됨 → 주입 완료 시 잔량이 더 적음 |
| 음식 + 알코올 | 음식이 흡수 늦춰도 AUC 불변 | **음식이 흡수 늦추면 AUC 감소** |

> 🔑 **임상 함의:** "식후 음주가 식전보다 덜 취하는" 이유의 정량적 근거가 여기 있습니다. 그리고 zero-order 소실 약물은 IV bolus와 oral AUC를 비교해서 F를 계산하면 **틀린 결과**가 나옵니다. IV microtracer가 필수입니다.

[출처: R&T 5e, Fig 16-7, Fig 16-8, p.501–502]

---

#### G. Zettelkasten Atom

```yaml
aliases: [페니토인 Css, MM 항정상태, pseudosteady-state, zero-order paradox]
source: "R&T 5e, Ch.16, Eq.16-6–16-10, pp.500–506"
```

발산 경계 $R_0 \to V_m$. $V_m$ 변화=비선형 폭발, $K_m$ 변화=선형 비례. 12% F 변화가 Css 2배. $t_{90} \propto (V_m-R_0)^{-2}$. Zero-order 소실에서 느린 흡수 → AUC **감소** — 선형 PK의 정반대.

---

### 🃏 카드 5. 혼합 병렬 경로 — Salicylic Acid

---

#### ━━ [거장의 시각] ━━

**왜 치명적으로 중요한가:**
salicylate의 총 clearance는 치료 범위에서 비교적 일정해서 선형처럼 보입니다. 그러나 두 비선형 기전이 서로 상쇄되어 총 CL이 flat한 것이고, 그 뒤에서 **비결합 농도($C_{u,ss}$)는 조용히 초비례로 쌓입니다.** 임상 독성은 총 농도가 아닌 비결합 농도에서 옵니다.

---

#### A & B. 병렬 경로 수식

$$CL = CL_{lin} + \frac{V_{max} \cdot C}{K_m + C} \tag{R\&T Eq.16-11, p.506}$$

[출처: R&T 5e, Ch.16, Eq.16-11, p.506]

$f_m$ 임계값: **포화 경로 $f_m \geq 0.5$이어야** 총 CL에 실질적 영향.

**소변 회수율 (Levy 1965 데이터):** [출처: R&T 5e, Table 16-6, p.519]

| 용량 (mg) | Unchanged SA (%) | Salicyluric acid (%) | Glucuronide (%) |
|---|---|---|---|
| 192 | 3 | **83** | 17 |
| 767 | 5 | **70** | 24 |
| 1,533 | 17 | **59** | 24 |
| 3,000 | 14 | **50** | 30 |

> 💡 **이 표에서 읽어야 할 것:** 총 회수율은 용량 전반에서 거의 100% → 대사 포화가 원인. Salicyluric acid 경로(83%→50%)가 포화되면서 unchanged drug 회수가 늘고 다른 경로로 흘러갑니다.

**두 비선형의 상쇄:**
- 포화 대사 → $CL_{int}$↓ → CL↓
- 포화 단백결합 → $f_u$↑ → $CL = f_u \cdot CL_{int}$에서 CL↑

이 두 효과가 우연히 상쇄되어 **총 CL ≈ 일정**. 그러나 $CL_u$(비결합 CL)는 계속 감소하므로 $C_{u,ss}$는 초비례 증가합니다(R&T Fig 16-29).

---

### 🃏 카드 6. Saturable First-Pass & Absorption — F↑ 역방향 기전

---

#### ━━ [거장의 시각] ━━

**왜 치명적으로 중요한가:**
Efflux transporter(P-gp) 포화와 saturable first-pass 대사 포화는 모두 **$F$↑**를 만듭니다. 이를 대사 포화($F$↓)와 혼동하면 고용량에서 노출이 감소할 것으로 잘못 예측합니다. 방향 판단이 완전히 뒤집히는 오류입니다.

---

#### A. Nicardipine — Saturable First-Pass의 교과서 사례

[출처: R&T 5e, Table 16-2, p.499; Wagner et al. 1987]

| 용량 (mg q8h) | Bioavailability (%) |
|---|---|
| 10 | 19 (4) |
| 20 | 22 (5) |
| 30 | 28 (5) |
| **40** | **36 (6)** |

반감기 변화 없음 → 소실 $CL$ 불변 → **$F$↑가 유일한 원인**. 간 초회통과 대사가 포화됩니다.

**감별 핵심:** Oral 데이터만으로는 $F$↓($CL$↑) vs $F$↑($CL$↓) 구분 불가 → **IV comparator 또는 IV microtracer 필수**.

---

#### B. Methylphenidate enantiomers — "Parent AUC↑ but metabolite AUC unchanged" 패턴

R&T Fig 16-6 (Aoyama et al. 1993):

| 지표 | (+)-MPH | (−)-MPH |
|---|---|---|
| Bioavailability | ≈ 20% | ≈ 4% |
| Metabolite (ritalinic acid) AUC | **≈ 동일** | **≈ 동일** |

> 💡 **해석 논리:** Parent AUC는 두 enantiomer가 다르지만 대사물 AUC는 같습니다. 간에서 총 처리량이 같다는 뜻 → first-pass 단계에서 (+)-MPH가 더 많이 "빠져나온" 것(F↑)이지, 전신 대사량이 다른 것이 아닙니다.
>
> 이 패턴: **Parent AUC↑ but metabolite AUC unchanged = saturable first-pass의 진단 시그니처**
>
> 만약 전신 CL이 포화된 것이라면? → 약물이 더 오래 머물 것 → metabolite AUC도 함께 증가해야 합니다. 이것이 관찰되지 않았으므로 전신 CL 포화는 배제됩니다.

---

#### C. Amoxicillin — Saturable Active Absorption (F↓)

[출처: R&T 5e, Fig 16-5; Sjövall 1985]

용량 증가 시: Dose-normalized AUC, $C_{max}$ 감소 + **$t_{max}$ 거의 불변**

> 💡 **$t_{max}$ 불변이 중요한 이유:** 흡수 부위가 소장 특정 구역에 고정 → 통과 시간 불변 → $t_{max}$ 불변. 용해도 제한이라면 $t_{max}$가 용량에 따라 변할 것입니다. 이 차이가 기전 감별의 단서입니다.

---

### 🃏 카드 7. 신배설 비선형성

**포화 분비 (Dicloxacillin, Nauta 1976):** $f_u=0.04$, 1g→2g IV, $CL_R$ 감소. 포화 분비 → 신배설 감소 → 전신 AUC 초비례 증가.

**포화 재흡수 (Ascorbic acid):** 75 mg/day → 10,000 mg/day (133배), $C_{ss}$ 9→19 mg/L (2배). $CL_R$ < 0.5→21 mL/min (42배 증가). 포화 재흡수 해제 → 신배설 급증 → $C_{ss}$ 상승 억제. 두 비선형이 동시 작용해 $C_{ss}$를 좁은 범위로 자동 유지하는 "생물학적 homeostasis".

> 💡 **신배설 비선형 감별:**
>
> | 기전 | 용량↑ 시 $CL_R$ 변화 |
> |---|---|
> | 분비(Secretion) 포화 | $CL_R$↓ (penicillin, dicloxacillin) |
> | 재흡수(Reabsorption) 포화 | $CL_R$↑ (ascorbic acid) |

**결합 artifact (Disopyramide, Giacomini 1982):** 총 $CL_R$ 시간에 따라 감소하지만 비결합 $CL_R$은 일정. $\alpha_1$-AGP 포화에 의한 $f_u$ 변화 → **겉보기 $CL_R$ 감소는 신기능 저하가 아닌 단백결합 변화**. 고단백결합 약물 신배설 평가에는 반드시 비결합 $CL_R$을 측정해야 합니다.

---

### 🃏 카드 8. 단백·조직결합 비선형성 & TMDD 브리지

---

#### ━━ [거장의 시각] ━━

**왜 치명적으로 중요한가:**
Warfarin-phenylbutazone 상호작용의 실제 원인은 단백결합 경쟁이 아니라 CYP2C9 억제입니다. 그리고 cefonicid의 apparent biexponential decline을 2구획 분포로 잘못 해석하면 완전히 틀린 모델을 사용하게 됩니다.

**체화해야 할 단 하나의 직관:**
In vitro 폐쇄계에서는 결합↑ → 비결합 농도↓ → 약효↓. 그러나 in vivo 개방계에서는 $C_u^{ss} = Dose\ rate / CL_u$ — **$f_u$가 변해도 $CL_u$ 불변이면 $C_u^{ss}$ 불변 → 약효 불변**.

> 💡 **욕조 비유:**
> - In vitro 폐쇄계 = 수도꼭지·배수구 없는 욕조. 단백질을 추가하면 물이 단백질에 붙어 자유수위(비결합 농도)가 내려갑니다.
> - In vivo 개방계 = 수도꼭지(투여)와 배수구($CL_u$)가 달린 욕조. 욕조 벽 두께($f_u$)를 바꿔도, 수위($C_u$)는 수도꼭지와 배수구 크기가 결정합니다.

---

#### A. $f_u$ 비선형 거동 수식 (G&W §2.7.5)

$$f_u \approx \frac{1}{1 + K_a \cdot n \cdot [P_T]} \quad (C_u \ll 1/K_a) \tag{Eq.2:298}$$
$$f_u \to 1 \quad (C_u \gg 1/K_a) \tag{Eq.2:299}$$

[출처: G&W 5e, §2.7.5, Eqs.2:297–2:299, pp.130–131]

---

#### B. Cefonicid — "Apparent Biexponential ≠ 2구획"

R&T Fig 16-18 (Dudley et al. 1986): 30 mg/kg IV 단회 투여 후
- 총 농도: 완만한 단일지수 감소처럼 보임
- 비결합 농도: 초기 2시간 내 **급격히** 감소, 이후 완만

**기전:** 고농도 시 albumin 결합 부위 포화 → $f_u$↑ → 겉보기 CL 높음 → 빠른 초기 소실. 농도 하강 → $f_u$↓ → CL 감소 → 느린 terminal phase.

> ⚠️ **핵심 함정:** 이 biphasic pattern을 보고 2구획 모델로 피팅하면 peripheral compartment가 실제로는 포화 단백결합을 "흡수"하고 있습니다. **단회 데이터만으로는 이 둘을 구분할 수 없습니다** → 반드시 여러 용량의 데이터 필요.
>
> **또 다른 역설:** Cefonicid를 oral로 투여하면 IV 대비 "bioavailability > 100%"가 계산될 수 있습니다. 이유: IV 투여 시 초기 고농도에서 포화 결합으로 CL이 높아 AUC가 낮지만, oral은 서서히 흡수되어 포화 구간을 피해 CL이 낮게 유지되기 때문입니다.

---

#### C. 단백결합 변화의 임상 결과 요약

In vivo 개방계 결론 (G&W Fig 2.104–2.105, R&T p.511–512):

| 상황 | 총 $C_{ss}$ | 비결합 $C_{u,ss}$ | 약효 |
|---|---|---|---|
| 저추출비 약물 + $f_u$ 증가 | ↔ (거의 불변) | ↑ | **↑ — 독성 위험** |
| 자가유도 발생 | ↓ | ↓ | ↓ |
| 고추출비 약물 + $f_u$ 증가 | ↓ | ↓ | ↓ |

> ⚠️ **TDM 함정:** 저추출비 약물에서 $f_u$가 증가하면 총 농도는 거의 변하지 않습니다. 총 농도 기준 TDM으로는 "정상"으로 보이지만 실제로는 비결합 농도가 올라 독성이 올 수 있습니다.

**Warfarin-phenylbutazone:** 둘 다 CYP2C9 기질 → 단백결합 경쟁이 아닌 **대사 억제**가 임상 상호작용의 실제 원인.

---

#### D. TMDD 예시들 (R&T pp.514–516) → I-08 브리지

| 약물 | TMDD 부위 | 비선형 방향 |
|---|---|---|
| **Bosentan** | Endothelin receptor | $V_{ss}$↓ with dose↑ |
| Imirestat | Aldose reductase | $V_{ss}$ dose-dependent |
| Draflazine | Nucleoside transporter (RBC) | 혈장 vs 전혈 큰 차이 |
| Trandolaprilat | ACE (plasma + tissue) | Biphasic decline = binding kinetics |

---

### 🃏 카드 9. 시간 의존성 동역학 + Product Inhibition

---

#### ━━ [거장의 시각] ━━

**왜 치명적으로 중요한가:**
Carbamazepine 단기 PK로 만든 투여 계획이 2–3주 후 완전히 무효가 됩니다. 그리고 product inhibition은 농도가 낮아져도 CL이 회복되지 않는 독특한 패턴으로 감별합니다.

**체화해야 할 단 하나의 직관:**
- **Capacity-dependence** = "농도 때문에" CL이 바뀜
- **Time-dependence** = "몸(효소 pool)이 바뀌어서" CL이 바뀜
- **Product inhibition** = "대사물이 쌓여서" CL이 바뀜

---

#### A. 효소 Turnover ODE

$$\frac{dE}{dt} = R_{in} - k_{out} \cdot E \tag{G\&W Eq.2:275}$$

> 💡 **욕조 비유:** 효소 pool을 욕조라고 하면, $R_{in}$은 수도꼭지(합성), $k_{out}$은 배수구(분해). 욕조가 새 수위(새 $E_{ss}$)에 도달하는 속도는 **수도꼭지 크기가 아니라 배수구 크기($k_{out}$)**가 결정합니다. 유도제가 수도꼭지를 열어도, 욕조가 새 수위에 도달하는 속도는 배수구($k_{out}$)가 지배합니다.

$$Cl_t = Cl' - (Cl' - Cl) \cdot e^{-k_{out}(t-t_{lag})} \tag{G\&W Eq.2:282}$$

---

#### B. Product Inhibition (G&W Fig 2.87 우측 열)

대사물이 $V_{max}$를 억제 → $CL$ 감소.

**감별 방법:**
- 농도가 낮아져도 CL이 **회복되지 않으면** → time-dependence (효소가 실제로 줄었거나, 대사물이 계속 억제)
- 농도가 낮아지면 CL이 **회복되면** → capacity-dependence

---

#### C. G&W Table 2.16 — 효소 반감기 선택값

| 유발 약물 | 기전 | $t_{1/2}$ of $k_{out}$ |
|---|---|---|
| Carbamazepine | Auto+hetero induction | **24–806 h** |
| Phenobarbital → Nortriptyline | Heteroinduction | 140 h |
| Methadone | Autoinduction | 94 h |
| Ifosfamide | Autoinduction | 2–6 h |

[출처: G&W 5e, Table 2.16, p.120]

> 💡 **Carbamazepine의 범위(24–806h)가 왜 이렇게 넓은가?** 유도 효소(CYP3A4, CYP2C8)의 기저 발현량, 병용 약물, 자가유도 vs 이종유도 기전의 개인차가 극단적으로 큽니다. 어떤 환자는 하루 만에 새 항정상태, 어떤 환자는 한 달 이상이 걸립니다.

---

#### D. PK21 (NT-Pb) — 핵심 수치

Pre-induction $Cl_{po}$ = 46 L/h → 유도 후 118 L/h (2.6배). $k_{out}$ $t_{1/2}$ = **158 h**. MRT 36→14 h.

> 💡 **이 연구 설계의 강점:** "반복 trough values가 $k_{out}$ 추정의 핵심"입니다. 단회 PK 데이터로는 유도 속도를 알 수 없습니다. Trough 반복 측정이 효소 pool의 동적 변화를 포착합니다.

---

#### E. G&W Fig 2.89 — 개체간 Km 차이

두 피험자 (25 unit vs 100 unit IV bolus): terminal semi-log 기울기가 완전히 다름. 이유: 피험자 A $K_m ≈ 300$ µg/L, 피험자 B $K_m ≈ 1,000$ µg/L.

> 💡 **PopPK 함의:** MM 약물에서 IIV가 매우 크게 나타나는 이유는 단순히 "CL의 개체차"가 아니라 **비선형 파라미터 공간에서의 개체 위치 차이**입니다. 같은 용량을 투여해도 $K_m$이 다르면 농도-시간 곡선의 형태 자체가 달라집니다.

---

### 🃏 카드 10. 4단계 인식 워크플로우 — Salicylate 완전 적용 (신규)

> 이 카드는 R&T pp.519–523의 분석 사례를 4단계 틀로 완전히 재현합니다. 카드 1에서 배운 프레임워크를 실제 데이터에 적용하는 연습입니다.

**사례:** Sodium salicylate 3 g 단회 경구 투여 후 분석

---

**Step 1. 소변 데이터로 비선형 탐지 (Table 16-6)**

선형 PK라면 용량과 무관하게 각 형태의 회수 비율이 일정해야 합니다.
관찰: 용량↑ → unchanged salicylate 회수↑, salicyluric acid 회수↓
→ **superimpose 실패 확인. 기전 가설: (a) F↑, (b) $CL_R$↑, (c) 대사 포화**

---

**Step 2. C-time 프로파일로 파라미터 방향 식별 (Fig 16-27)**

Semi-log 플롯: 기울기가 시간이 지날수록 **가팔라진다**. 선형 PK라면 기울기 일정.
→ **$CL$↑ with time, 즉 농도 감소와 함께 CL 회복 (용량 의존성)**

---

**Step 3. 영향 받은 Primary 파라미터 결정**

최고 농도 ≈ 200 mg/L, 용량 3 g → $V/F$ ≈ 3,000/200 = 15 L (매우 작음)
$V$가 15 L로 작으므로 농도 변화에 따른 $V$ 변화 가능성 낮음 → **$CL$↑가 주원인**
소변 데이터에서 metabolite 회수율 감소 → **대사 포화가 주요 기전**

---

**Step 4. 단백결합 데이터로 기전 확인 (Fig 16-28)**

- $f_u$가 농도↑ 시 증가 (고농도 albumin 결합 포화)
- $CL_u$(비결합 CL)은 농도↑ 시 감소 (대사 포화)
- **총 $CL$은 두 효과의 상쇄로 비교적 일정** — "선형처럼 보이는" 이유

**최종 결론:** 두 비선형 기전 공존 + 상쇄 → 총 CL ≈ 일정, 그러나 **$C_{u,ss}$는 초비례** (독성의 실제 원인).

---

### 🃏 카드 11. 비선형 PK 종합 방향성 테이블 (R&T Table 16-12 기반) (신규)

> 이 표를 외우면 PopPK 공변량 방향성 예측과 규제 문서 작성에 직접 사용할 수 있습니다. **세션 전체의 요약표**입니다.

| 비선형 원인 | V | CL | t½ | 총 $C_{ss}/Rate$ | 비결합 $C_{u,ss}/Rate$ |
|---|---|---|---|---|---|
| **경구 투여** | | | | | |
| Bioavailability↓ | ↔ | ↔ | ↔ | ↓ | ↓ |
| **Bioavailability↑** (saturable first-pass) | ↔ | ↔ | ↔ | ↑ | ↑ |
| **정맥 투여** | | | | | |
| $f_u$↑, 저추출비 약물 | ↑ | ↑ | ↔ | ↔ | ↑ |
| $f_u$↑, 고추출비 약물 | ↑ | ↑ | ↔ | ↓ | ↓ |
| 조직결합 포화 ($V$↓) | ↓ | ↔ | ↓ | ↑ (초기) | ↑ |
| **대사 $CL$↓** (포화 대사) | ↔ | ↓ | ↑ | **↑** | **↑** |
| 신 $CL$↓ (포화 분비) | ↔ | ↓ | ↑ | ↑ | ↑ |

[출처: R&T 5e, Ch.16, Table 16-12, p.528 기반 재구성]

> 💡 **가장 중요한 행 읽기:**
>
> **$f_u$↑ + 저추출비:** 총 농도 ↔(불변)이지만 비결합 농도 ↑. TDM에서 총 농도 보면 "정상"처럼 보이지만 실제로 독성이 올 수 있습니다.
>
> **대사 $CL$↓:** 가장 극단적 비선형. Phenytoin 유형. 총·비결합 모두 폭발.

---

## §5 — 혼동 쌍 해부

---

### 혼동 쌍 1: $V_{max}$ vs $K_m$ — Css 민감도의 비대칭성 ← **Critical Blow**

| 비교 차원 | $V_{max}$ | $K_m$ |
|---|---|---|
| **표면적 유사성** | 둘 다 MM 방정식의 파라미터, 둘 다 변하면 $C_{ss}$가 바뀜 | |
| **수식 위치** | $C_{ss} = K_m \cdot R_0 / (V_m - R_0)$ → **분모**에 위치 | **분자**에 위치 |
| **생물학적 지시체** | 효소 총량에 비례 | 효소 친화도의 역수 |
| **변화 유발 원인** | 유도↑, 간경변↓, 비경쟁억제↓ | 경쟁억제↑; 유도는 불변 |
| **$C_{ss}$ 반응** | **비선형 폭발**: $V_m$ 20% 감소 → $C_{ss}$ 2배 | **선형 비례**: $K_m$ 50% 증가 → $C_{ss}$ 50% |
| **⚡ 기억 고리** | **$V_{max}$는 분모 $(V_m-R_0)$를 지배한다 — 조금만 줄어도 분모가 0에 급격히 수렴한다. $K_m$은 분자에만 있어 선형으로 비례한다. 비선형 폭발은 항상 분모가 만든다.** | |

| **치명적 타격** | 간경변 환자에서 $V_m$ 20% 감소를 $K_m$ 변화(선형 비례)로 오인 → "50% 농도 증가"로 예측하고 50% 감량 → 실제로는 2배 상승을 막기에 부족해 독성 진입. NDA 시 예측 농도와 실제 농도가 2배 이상 괴리되어 Deficiency Letter. |
|---|---|

---

### 혼동 쌍 2: Zero-order 소실에서 Input Rate↓ → AUC↓ vs 선형 PK에서 Input Rate↓ → AUC↔

| 비교 차원 | Zero-order(MM) 소실 | 선형(1차) 소실 |
|---|---|---|
| **Input rate 감소 시 AUC** | **AUC 감소** | **AUC 불변** |
| **이유** | 느린 주입 기간 동안 대사가 지속적으로 진행 → 주입 완료 시 잔량이 더 적음 | $CL$ 일정이면 $AUC = Dose/CL$ |
| **Oral bioavailability 평가** | AUC 비교 방법 **사용 불가** | AUC 비교 = gold standard |
| **⚡ 기억 고리** | **Zero-order 소실은 "배수구 속도가 일정한 욕조"다. 수도꼭지를 천천히 틀면 물이 들어오는 동안 배수구가 더 많이 빼내어 욕조(AUC)가 더 작아진다.** | |

---

### 혼동 쌍 3: MM 순간 반감기 vs 선형 terminal half-life

| 비교 차원 | MM $t_{1/2}^{inst}(C)$ | 선형 terminal $t_{1/2}$ |
|---|---|---|
| **수식** | $\ln(2) \cdot V/V_{max} \cdot (K_m+C)$ | $0.693 \cdot V/CL$ |
| **농도 의존성** | 농도에 **비례 증가** | **농도 무관** |
| **Semi-log 거동** | 시간이 지날수록 기울기 **가팔라짐** | 직선 |
| **$5 \times t_{1/2}$** | **사용 불가** | 신뢰 가능 |
| **⚡ 기억 고리** | **MM 반감기는 약물 농도가 만드는 순간 초상화 — 농도가 내려갈수록 화가의 붓질이 빨라진다. 선형 반감기는 처음부터 끝까지 같은 속도로 그려지는 정물화다.** | |

---

### 혼동 쌍 4: 단백결합 변화 — In vitro vs In vivo 약효 방향

| 비교 차원 | In vitro 폐쇄계 | In vivo 개방계 |
|---|---|---|
| **핵심 관계** | 총 약물량 고정 → $f_u$↑ → $C_u$↑ → 약효↑ | $C_u^{ss}=Dose\ rate/CL_u$ → $f_u$가 변해도 $CL_u$ 불변이면 $C_u^{ss}$ 불변 |
| **⚡ 기억 고리** | **시험관(폐쇄계)은 저수지 없는 수영장. 생체(개방계)는 수도꼭지(투여)와 배수구(CL)가 달린 수영장 — 벽 두께($f_u$)를 바꿔도 수위($C_u$)는 수도꼭지와 배수구 크기가 결정한다.** | |

---

### 혼동 쌍 5: Capacity-dependent vs Time-dependent

| 비교 차원 | Capacity-dependent | Time-dependent |
|---|---|---|
| **Levy 판별 기준** | 농도 일정 시 CL도 일정 | 농도 일정해도 CL이 시간과 함께 변함 |
| **Product inhibition** | 농도↓ 시 CL 회복됨 | 대사물 축적 시 농도↓해도 CL 미회복 |
| **⚡ 기억 고리** | **농도가 바뀌어 시스템이 달라 보이면 capacity. 시간이 지나 몸(효소 pool)이 바뀌어 시스템이 달라지면 time-dependence. 대사물이 쌓여 시스템이 달라지면 product inhibition.** | |

---

## §7 — Self-Test: Active Recall Module

---

**Q1** [★★] MM 방정식에서 "저농도에서 maximal"인 것과 "고농도에서 maximal"인 것은 무엇인가? $CL = V_{max}/2$가 되는 농도 조건은? R&T Table 16-3에서 알코올 농도 100 mg/L 대비 7,000 mg/L에서 Rate와 CL이 각각 몇 배 차이인지 계산하라.

<details><summary>정답 공개</summary>

저농도: **Clearance** 최대 ($V_{max}/K_m$). 고농도: **Rate** 최대 ($V_{max}$). $C = K_m$일 때 $CL = V_{max}/2$.

알코올 ($V_m=10$ g/hr, $K_m=100$ mg/L):
- Rate: 7,000 mg/L → 9.9 g/hr; 100 mg/L → 5.0 g/hr → **약 2배**
- CL: 7,000 mg/L → 1.4 L/hr; 100 mg/L → 50 L/hr → **약 36배**

G&W 경고: $K_m$의 10–20%에서 이미 비선형 시작 — "$K_m$이 경계"라는 단순화는 위험하다.

**다음 깊이 질문:** 알코올을 1시간에 14 g 마시면 왜 결국 치명적인가?
</details>

---

**Q2** [★★] 페니토인 $K_m'=4$ mg/L, $V_m=500$ mg/day, $V=50$ L.
(a) $R_0=400$ mg/day에서 $C_{ss}$.
(b) 같은 환자에서 bioavailability가 0.85→0.95로 변하면 ($D$=400 mg/day 동일) 새 $C_{ss}$.
(c) 간경변으로 $V_m$이 400 mg/day로 감소하면?

<details><summary>정답 공개</summary>

(a) $C_{ss} = 4\times400/(500-400) = \mathbf{16}$ mg/L

(b) 새 $R_0 = 0.95 \times 400/0.85 \approx 447$ mg/day
$C_{ss}' = 4 \times 447 / (500-447) = 1,788/53 \approx \mathbf{33.7}$ mg/L (독성)
→ 12% F 변화 → Css 2배 이상

(c) $V_m=400$ → 분모 = $400-400 = 0$ → **$C_{ss} = \infty$, 항정상태 불가능**. $R_0=300$으로 감량 시: $4\times300/(400-300)=12$ mg/L (치료역 내).

**다음 깊이 질문:** cimetidine이 $K_m'$을 4→6 mg/L로 올리면 $R_0=400$ mg/day에서 $C_{ss}$는?
</details>

---

**Q3** [★★] PK17에서 "pilot study에 불과"한 이유 두 가지를 수학적 근거와 함께 설명하라. ADVAN13에서 S1의 단위 함정은 무엇인가?

<details><summary>정답 공개</summary>

**이유 ①:** Slow infusion rate = 138.4 µg/min > $V_{max}$ = 107 µg/min → Eq.2:273에서 $dC/dt > 0$ 항상 → 항정상태 수학적으로 불가능. 실험 설계 자체가 $V_{max}$ 추정에 불충분.

**이유 ②:** $K_m$–$V$ 상관 = **−0.96** → structural identifiability 실패. 현재 추정된 $K_m$=0.56과 $V_{max}$=107은 독립 추정치가 아니라 $V_{max}/K_m$ 비율 하나만 추정한 것에 가깝다. 고농도 코호트 없이는 외삽 금지.

**S1 단위 함정:** A(1)이 µg이고 V가 mL이면 S1=V로 설정해야 IPRED = µg/mL. 설정 안 하면 µg이 그대로 IPRED → 단위 불일치 → sigma가 폭발하거나 파라미터가 완전히 틀려도 모름.

**다음 깊이 질문:** 상관 −0.96을 줄이기 위한 실험 설계 변경은?
</details>

---

**Q4** [★] Zero-order 소실 약물에서 input rate를 절반으로 줄이면 AUC는 어떻게 되는가? 선형 소실과 비교하여 설명하고, oral bioavailability 측정에 어떤 함의를 갖는가?

<details><summary>정답 공개</summary>

**Zero-order 소실:** Input rate↓ → AUC **감소**. 느린 주입 기간 동안 약물이 지속적으로 일정 속도로 대사되므로, 주입 완료 시점에 체내 잔량이 더 적다(R&T Fig 16-8).

**선형 소실:** Input rate↓ → AUC **불변** ($AUC = Dose/CL$, CL 일정).

**Oral bioavailability 함의:** Zero-order 소실 약물은 IV bolus와 oral의 AUC 비교로 F를 계산하면 틀린 결과가 나온다. IV는 빠른 input → 제한된 대사; oral은 느린 absorption → 더 많은 대사 → oral AUC가 IV보다 낮게 나와 F가 과소추정된다. **IV microtracer 필수.** [R&T p.501]

**다음 깊이 질문:** 알코올에서 음식이 AUC를 줄이는 기전을 이 원리로 설명하라.
</details>

---

**Q5** [★] Methylphenidate enantiomer 사례에서 "parent AUC↑ but metabolite AUC unchanged"가 saturable first-pass를 지지하는 이유는? 전신 CL이 포화된 경우 metabolite AUC는 어떻게 되어야 하는가?

<details><summary>정답 공개</summary>

**Saturable first-pass 논리:** First-pass 단계에서 포화 대사를 피해 전신으로 탈출(F↑). 탈출한 약물 중 일부는 이후 전신에서 대사되어 metabolite를 만들지만, **총 대사량(간 first-pass + 전신 대사)은 거의 일정** → metabolite AUC ≈ 동일.

**만약 전신 CL이 포화되어 AUC↑라면:** CL↓ → 약물이 더 오래 체내에 머물 → metabolite 형성 시간↑ → **metabolite AUC도 함께 증가**해야 한다. 이것이 관찰되지 않았으므로 전신 CL 포화는 배제.

**다음 깊이 질문:** Nicardipine의 oral F↑를 IV comparator 없이 감지하려면 어떤 데이터가 필요한가?
</details>

---

**Q6** [★] Cefonicid의 총농도는 단일지수 감소처럼 보이는데 비결합 농도는 초기에 매우 빠르게 감소한다. 이것이 2구획 분포가 아닌 saturable binding 때문임을 어떻게 증명하는가?

<details><summary>정답 공개</summary>

**증거 1:** 비결합 농도의 빠른 초기 감소가 총농도 감소 속도와 비례하지 않는다 — 2구획이라면 총·비결합 농도가 proportional 관계 유지해야 한다.

**증거 2:** $f_u$가 시간에 따라 **체계적으로 감소**한다(Fig 16-18B). 2구획 모델이라면 $f_u$가 일정해야 한다.

**결정적 증거:** 여러 용량 비교 시 저용량에서 biphasic 덜 뚜렷하고 고용량에서 더 뚜렷하면 → saturable binding 확인. 2구획 분포라면 dose-normalized 프로파일이 superimpose해야 한다.

**다음 깊이 질문:** Cefonicid에서 "oral bioavailability > 1.0"이 관찰되는 이유는?
</details>

---

**Q7** [★] G&W Table 2.16에서 carbamazepine의 $k_{out}$ $t_{1/2}$ 범위가 24–806 h이다. 이 IIV의 원인과 PopPK 모델링에서 어떤 어려움이 있는가?

<details><summary>정답 공개</summary>

**IIV 원인:** (1) 유도 효소(CYP3A4, CYP2C8)의 기저 발현량 개체차, (2) 병용 약물의 효과, (3) 자가유도 vs 이종유도 기전의 혼합.

**PopPK 어려움:** 범위(24–806h)가 극단적이라 어떤 개체는 1일, 어떤 개체는 1달 이상이 걸린다. 단일 $\omega_{k_{out}}^2$으로 표현하면 추정 불안정. 또한 carbamazepine이 자신의 $k_{out}$을 바꾸는 특성 때문에 $k_{out}$이 고정 파라미터가 아닌 동적 변수가 되어 모델이 매우 복잡해진다.

**실무 접근:** 반복 trough 측정이 $k_{out}$ 추정의 핵심.

**다음 깊이 질문:** 단회 PK로 만든 carbamazepine 투여 계획이 임상에서 실패하는 구체적 시나리오는?
</details>

---

**Q8** [★] R&T Table 16-12 기반: 저추출비 약물에서 $f_u$가 증가할 때 (a) $V$, (b) $CL$, (c) 총 $C_{ss}$, (d) 비결합 $C_{u,ss}$의 방향을 예측하라. TDM 실무의 함정은?

<details><summary>정답 공개</summary>

저추출비 약물, $f_u$↑:
- (a) $V$↑ (비결합 약물이 조직 분포 증가)
- (b) $CL = f_u \cdot CL_{int}$ → $CL$↑
- (c) $C_{ss} = R_0/CL$ → $C_{ss}$↓
- (d) $C_{u,ss} = f_u \cdot C_{ss}$ → $f_u$↑ × $C_{ss}$↓ = **거의 불변** (상쇄)

**TDM 함정:** 총 $C_{ss}$ 감소했지만 비결합 농도는 일정. 임상의가 총농도 기준으로 "용량 늘려야 한다"고 판단하면 비결합 농도 과잉 → 독성 발생. 고단백결합 저추출비 약물(많은 항전간제)에서 반드시 비결합 농도 측정 또는 기전 이해 기반 해석 필요.

**다음 깊이 질문:** 신부전 환자에서 albumin 감소로 $f_u$가 증가한 phenytoin을 TDM할 때 어떻게 해야 하는가?
</details>

---

### ⭐ Q9 — 보스 딜레마 [★★]

> **시나리오:** 새 항간질제 XN-150의 Phase 1 FIH 연구. 4개 용량 코호트(50, 100, 200, 400 mg)에서 dose-normalized AUC가 50→400 mg 구간에서 단조 상승(AUC/Dose: 1.2→2.8 ng·hr/mL/mg). 추정 $K_m'$ = 280 ng/mL (95% CI: 80–950 ng/mL), RSE 45%. 치료 목표 농도 150–300 ng/mL.
>
> **회사 규제팀:** "CI가 넓지만 MM 모델이 선형보다 OFV 12.3 낮음. Phase 2 용량 설계에 MM 모델 사용 허가."
> **안전팀:** "RSE 45%면 파라미터 불신뢰. 선형으로 외삽해야 안전."
>
> 당신은 수석 모델러로서 어떤 판단을 내리는가?

<details><summary>수석 모델러의 Trade-off 논리</summary>

**핵심 판단:** 이것은 "선형 vs MM" 선택이 아니라 **identifiability 실패 선언의 문제**입니다.

**안전팀 취약점:** "RSE 45%면 선형으로"는 논리적으로 틀렸습니다. 선형 모델은 OFV가 더 높고 AUC/Dose vs Dose의 단조 상승을 설명하지 못합니다. 선형 외삽이 더 안전한 것이 아니라 **더 틀린** 것입니다.

**규제팀 취약점:** RSE 45% + 95% CI (80–950 ng/mL)는 사실상 "Km이 얼마인지 모른다"는 선언입니다.
- $K_m'$=80이면: 치료 목표(150–300)가 $K_m$의 2–4배 → 상당히 비선형 구간 → 용량 증가 시 AUC 폭발 가능
- $K_m'$=950이면: 치료 목표가 $K_m$의 16–32% → 거의 선형 구간

**수석 모델러의 결정 (4단계):**

① MM 모델과 선형 모델 모두 FDA에 투명하게 보고. 두 모델의 Phase 2 용량 예측 결과를 나란히 제시.

② **Phase 2 시작 전 고용량 PK 코호트 추가를 FDA에 제안:** 600 mg 코호트 추가 → $K_m$ CI를 좁혀야 합니다. Phase 2 첫 파트로 설계 가능.

③ Phase 2 초기 용량은 **보수적으로:** 선형 외삽과 MM 외삽의 중간값 또는 하한으로 시작, 반복 PK로 확인하며 titration.

④ FDA Type B meeting에서 서면화: *"Current data support nonlinear PK but parameter identifiability is insufficient for robust Phase 2 dose projection. Additional PK cohort at high dose is planned."*

이것은 "MM 선택 vs 선형 선택"이 아니라 **"불확실성을 어떻게 관리하는가"**의 문제입니다. 규제 심사관은 불확실성 자체보다 그것을 인식하고 관리하는 계획이 없을 때 Deficiency Letter를 보냅니다.
</details>

---

## §8 — Meta-Frame & Big Picture

### A. Positioning — 28세션 아키텍처에서의 위치

I-07은 28세션 아키텍처에서 **"선형 PK의 안전한 세계가 구조적으로 붕괴되는 첫 번째 관문"**입니다.

```
I-01~I-06: 선형 PK의 세계 ──────────────────────┐
                                                  │
I-07: 비선형 PK (이 세션) ◀── 여기가 관문         │
       ↓ 공급하는 개념:                            │
       - Saturable 효소 동역학                     │
       - Km·Vmax 파라미터 직관                    ↓
       - C50 vs Km 위치 관계               I-08 TMDD (saturable target binding)
       - Zero-order 역설                   I-09 Emax PD (동형 수식의 PD 버전)
       - TDM 실무 판단                     I-10 Indirect Response (turnover ODE)
                                           II-04 ADVAN13/$DES 구현
```

- **이전에 온 것:** I-01 (CL·V), I-03 (1구획 ODE), I-05 (단백결합 기초)
- **직후:** I-08 (TMDD), I-09 (Emax), I-10 (Indirect Response), II-04 (ADVAN13/$DES)
- **의존 고급 도메인:** PopPK (η 위치 선택), PBPK (간 효소 포화 스케일링), TMDD (PKPD 통합), QSP

---

### B. Dependencies — 이 세션을 대충 넘겼을 때의 구체적 실패 모드

**실패 1:** Bosentan처럼 $V_{ss}$가 용량 의존적인 약물을 표준 2구획으로 피팅 → peripheral compartment를 과잉 추정 → $CL_d$ 왜곡 → 반복 투여 축적 예측 완전히 틀림. IND 제출 시 Deficiency Letter.

**실패 2:** Zero-order 소실 약물의 oral bioavailability를 AUC 비교로 계산 → input rate 의존성 때문에 F 과소 또는 과대 추정 → Phase 2 용량이 sub-therapeutic 또는 toxic.

**실패 3:** PK17 상관 −0.96을 단순 정밀도 문제로 무시 → structural identifiability 실패 선언 없이 Phase 2 진행 → 치료 농도에서 AUC 폭발. **$COV step의 condition number > 1,000이 identifiability 실패의 신호**임을 I-07에서 처음 체험합니다.

**실패 4:** 총농도 기반 TDM에서 $f_u$ 증가를 무시 → "농도가 낮으니 용량 증가" 판단 → 실제로는 비결합 농도 정상이었는데 독성 진입.

---

### C. Professional Moat — 구조적 필연성 수준의 답

AI와 소프트웨어는 MM 모델을 피팅하고 $V_{max}$·$K_m$을 출력합니다. 주니어 모델러는 GOF가 좋으면 그 결과를 믿습니다.

**이 세션을 진정으로 내면화한 모델러는 다음 세 가지를 동시에 수행합니다:**

**첫째:** $COV step 출력에서 $K_m$–$V$ 상관 **−0.96**, $K_m$ RSE **45%**, condition number > 1,000을 보는 순간 — "이것은 정밀도 문제가 아니라 structural identifiability 실패다. 현재 추정된 $V_{max}/K_m$은 하나의 선형 비율로 추정된 것이며, $V_{max}$와 $K_m$을 독립적으로 신뢰할 수 없다" — 라고 즉시 판단하고, 이를 FDA Deficiency Letter 방어 언어로 번역합니다.

**둘째:** Zero-order elimination + oral input의 조합에서 "AUC 비교로 F를 측정하면 틀릴 수 있다"는 것을 즉시 인식하고 IV microtracer 설계를 제안합니다.

**셋째:** 총농도 TDM 결과를 보고 "$f_u$가 변했을 가능성, 비선형 단백결합 가능성"을 먼저 배제한 뒤 용량 조정을 권고합니다 — 이것이 임상약사 TDM 경험과 계량약리학 기전 이해가 결합하는 지점입니다.

이 세 가지는 알고리즘이 복제할 수 없는 **수식의 구조적 의미와 임상·규제 결과를 연결하는 인과 추론 역량**입니다. 그리고 이 역량은 G&W의 "The system may already behave in a nonlinear fashion at concentrations which are 10–20% of Km"이라는 경고 한 줄을 단순히 외운 것이 아니라, 그 경고의 파급력을 **Phase 1 설계 → FDA 미팅 → Phase 2 용량 → TDM 해석**의 전체 체인으로 추적할 수 있을 때 완성됩니다.

---

```
---
✦ STEP 1 완료. (친절한 재표현본 — 내용 하드 픽스 + 가독성 보강판)

다음이 준비되었습니다:
  • §1 세션 헤더 & 로드맵 (전체 지도 선제시, 3-레이어 구조화)
  • §2 개념 해부 카드 (11개 개념, Apex: MM 소실 동역학)
      - 주요 보강: 공장 비유, 욕조 비유, 배수구 비유 통합
      - 주요 보강: Zero-order paradox 비교표, S1 단위 함정 명시
      - 주요 보강: 수식 단계별 쌓기 + 각 수식 직관 주석
  • §5 혼동 쌍 해부 (5개 쌍, Critical Blow: Vmax vs Km)
  • §7 자기 테스트 (9개 질문, 보스 딜레마 포함)
  • §8 메타프레임 & 빅 픽처
  • 감지된 소스 유형: Vol I 혼합 (R&T 5e Ch.16 + G&W 5e §2.7)
  • Data Anchoring:
      - G&W PK17: Agent X, Vmax=107µg/min, Km=0.56µg/mL
      - G&W PK21: NT-Pb, kout t½=158h
      - R&T Table 16-3: Alcohol Vm=10g/hr, Km=100mg/L
      - R&T Fig 16-10: Phenytoin Km'=4mg/L, Vm=500mg/day
      - R&T Fig 16-18: Cefonicid 30mg/kg IV (Dudley 1986)
      - R&T Table 16-6: Salicylate urinary recovery (Levy 1965)
      - R&T Table 16-2: Nicardipine F (Wagner 1987)

"계속"을 입력하면 Step 2 HTML 컴파일러가 실행됩니다.
---
```

C-260426-154230-7KQ

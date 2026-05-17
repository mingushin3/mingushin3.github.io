# 07_html_compile_input_master — v3.8

## 임상 장면 — 왜 이 세션이 필요한가

Phenobarbital 100 mg q24h, $t_{1/2}=4$ days 환자에서 trough가 높다고 해서 "아직 plateau에 도달하지 못해서"라고 말할 수 없습니다 [R&T pp.324–326]. **같은 다중투여 문제 안에서도 세 가지 질문이 각각 다른 파라미터의 지배를 받기 때문**입니다 — 도달 시간은 $t_{1/2}$, 축적 배율은 $\tau/t_{1/2}$, 평균 수준은 $CL$과 평균 입력률이 정합니다.

**Daptomycin**(cyclic lipopeptide 항생제)에서 75 mg/kg/day가 같아도 q24h와 q8h의 CPK가 **991 vs 3996 U/L**로 4배 차이가 났습니다 [R&T pp.351–353]. → 총용량 하나로 독성 판단을 끝낼 수 없다는 사례입니다.

## 학습자 안내

먼저 §1의 **큐레이션 맵**으로 M1–M10의 결정자 구조를 훑고, §2 카드를 순서대로 읽은 뒤, §5 혼동 쌍과 §7 자기 테스트로 오개념을 제거하면 됩니다. 시작 전에는 $CL$, $t_{1/2}$, $\tau/t_{1/2}$, $C_{av,ss}$, $A_{av,ss}$, 치료역(therapeutic window; 효과와 안전성을 함께 고려한 농도 구간)이 **서로 다른 질문에 답한다**는 점만 기억하면 됩니다.

---

## 큐레이션 맵(Curation Map)

### MUST — 10분 핸드아웃에 반드시 남길 개념

| ID | 개념 | 핵심 잠금 문장 | 핵심 수식 / 앵커 | §2 카드 | 출처 |
|---|---|---|---|---|---|
| M1 | 정속 주입 plateau 농도 | 항정상태 농도 수준은 $t_{1/2}$가 아니라 $CL$(← 단위 시간당 제거되는 용적)이 정합니다. | $C_{ss}=R_{in}/CL$ | §2-M1 | [G p.23; R&T p.288] |
| M2 | plateau 도달 시간 | 목표 plateau가 높든 낮든 접근 시간표는 반감기의 함수입니다. | $C(t)=C_{ss}(1-e^{-Kt})$; 1·2·3·3–4 half-lives에서 각각 50%, 75%, 87.5%, $\approx90\%$ | §2-M2 | [G pp.22–23; R&T pp.290–292] |
| M3 | 다중투여 축적계수 | 축적은 dose가 아니라 $\tau/t_{1/2}$가 정합니다. | $R_{ac}=1/(1-e^{-K\tau})=1/(1-2^{-\tau/t_{1/2}})$ | §2-M3 (Apex) | [G pp.43–45; R&T pp.322–326; R&T pp.795–797] |
| M4 | 평균 plateau: 농도 vs 약물량 | $C_{av,ss}$와 $A_{av,ss}$를 등치하면 안 됩니다 — 농도는 $CL$, 약물량은 $MRT$로 표현됩니다. | $C_{av,ss}=F\text{Dose}/(CL\tau)$; $A_{av,ss}=1.44F\text{Dose}t_{1/2}/\tau$; 1-구획에서만 $C_{av,ss}=A_{av,ss}/V$ | §2-M4 | [G p.45; R&T p.324; R&T p.337] |
| M5 | Flip-flop | terminal slope가 소실이 아니라 흡수를 말할 수 있습니다. | $K_a<K$이면 terminal slope $\approx K_a$ | §2-M5 | [G pp.45–46; R&T pp.332–334, 337–338] |
| M6 | 치료역 | TW는 "좋은 농도 범위"가 아니라 benefit–harm 균형을 농도 축에 투영한 의사결정 구간입니다. | TW와 therapeutic concentration range 구별; TI는 전임상 ratio와 임상 exposure sensitivity가 다름 | §2-M6 | [R&T pp.267–281] |
| M7 | 부하 + 유지 용량 | 목표 근처에서 시작하려면 부하용량이, 유지에는 평균 입력률이 필요합니다. | $D_M=D_L(1-e^{-K\tau})$; $D_L=R_{ac}D_M$; bolus+주입 앵커 | §2-M7 | [R&T pp.293–295; R&T pp.326–329; G pp.537–539] |
| M8 | 치료역 기반 투여 설계 | $C_{upper}$, $C_{lower}$, $t_{1/2}$, $V$, $F$가 있으면 투여간격과 용량 상한을 계산할 수 있습니다. | $\tau_{max}=1.44t_{1/2}\ln(C_{upper}/C_{lower})$; $D_{M,max}=(V/F)(C_{upper}-C_{lower})$ | §2-M8 | [R&T pp.334–337] |
| M9 | PD 기반 plateau | 효과 plateau는 약물 PK plateau보다 늦을 수 있습니다 — **무엇의 반감기인지** 먼저 물어야 합니다. | atorvastatin: PK $t_{1/2}=14$ h, PD plateau 3–4주; erythropoietin: PK $t_{1/2}=9$ h, hematocrit plateau $\approx70$일 | §2-M9 + §2-M6 PK/PD clocks | [R&T pp.341–345] |
| M10 | 용량분할 독성 | 같은 일일 용량이라도 분할투여가 회복 시간을 바꾸면 독성이 달라집니다. | Daptomycin Study A: 75 mg/kg q24h vs 25 mg/kg q8h, CPK 991 vs 3996 U/L | §2-M10 + §2-M7 daptomycin anchor | [R&T pp.351–353] |

$$
\begin{aligned}
\underbrace{C_{ss}}_{\text{plateau}}&=\underbrace{R_{in}/CL}_{\text{입력/CL}}\\
\underbrace{R_{ac}}_{\text{축적계수}}&=\frac{1}{1-e^{-K\tau}}\\
\underbrace{C_{av,ss}}_{\text{평균농도}}&=\frac{F\cdot Dose}{CL\cdot\tau}
\end{aligned}
$$

### CONTEXT — 유지하되 확장하지 않을 항목

| ID | 항목 | 잠금 결정 | 출처 |
|---|---|---|---|
| C1 | 항정상태 vs 열역학적 평형 | 용어만 구분 — 독립 카드로 확장 안 함 | [G p.25] |
| C2 | 입력 함수 분류 | bolus/zero-order/first-order/multiple input은 "입력이 바뀌면 곡선이 바뀐다" 수준만 유지 | [G p.43] |
| C3 | 다중 흡수 부위 | multiple peaks가 곧 enterohepatic recirculation을 뜻하지 않음 — 주의만 유지 | [G p.46] |
| C4 | PK11 | PK clock = PD clock의 단순 anchor로만 사용 | [G pp.528–531] |
| C5 | PK13 | bolus+infusion IC coding anchor로 사용 | [G pp.537–539] |
| C6 | 정속 장치(constant-rate devices) | infusion 원리의 확장 예시로만 유지 | [R&T pp.284–286] |
| C7 | 주입 후 감소(post-infusion decline) | infusion 중단 후 농도는 half-life에 따라 감소하되, extravascular continued input은 예외 | [R&T p.291] |
| C8 | Clobazam 단회투여 AUC | single-dose AUC로 plateau average를 예측할 수 있다는 1문장 anchor | [R&T p.336] |
| C9 | 방출 조절(modified release) | intentional flip-flop의 임상 활용 — morphine MR, leuprolide depot만 짧게 유지 | [R&T pp.337–338] |
| C10 | 투여법 평가 | fluctuation, relative bioavailability, renal clearance는 evaluation context로만 유지 | [R&T pp.339–341] |
| C11 | DDI 패턴 | ER 중심 4패턴만 유지 — protein binding 단독 논리는 금지 | [R&T pp.309–310; R&T pp.350–351] |
| C12 | 연습 문제 | 본문 통합 금지 — §7 가상/응용 문항으로만 사용 가능 | [R&T pp.353–358] |

---

<!-- SLIDE_START: §1 | title: §1 — 세션 헤더 & 로드맵 -->
# §1 — 세션 헤더 & 로드맵

## 1A. 개념 지도 (3-레이어)

```text
레이어 1 — 무엇인가
  steady state / therapeutic window / flip-flop / PD plateau / fractionation

레이어 2 — 어떻게 계산되는가
  Css = Rin/CL
  C(t) = Css(1 - e^{-Kt})
  Rac = 1/(1 - e^{-Kτ})
  Cav,ss = F·Dose/(CL·τ)
  τmax = 1.44·t1/2·ln(Cupper/Clower)

레이어 3 — 언제, 왜 중요한가
  TDM 조정 / NONMEM SS flag / loading-maintenance design / TW algorithm / PD·toxicity timing
```

## 1B. 지식 그래프 위치

```text
[선행: single-dose PK, CL·V·t1/2, oral absorption]
   → [이 세션: steady-state grammar, accumulation, TW-driven regimen design]
   → [후속: TDM, PopPK covariate interpretation, exposure-response, Phase 1 MAD design]
```

🧭 **읽는 순서**
카드 1 (M1): 정속 주입 plateau의 높이는 무엇이 정하는가?
카드 2 (M2): 그 plateau에 도달하는 시간표는 무엇이 정하는가?
카드 3 (M3): 반복투여에서 축적 배율은 왜 dose가 아니라 interval의 문제인가?
카드 4 (M4): 평균농도와 평균 약물량은 왜 같은 평균이 아닌가?
카드 5 (M5): terminal slope는 언제 elimination이 아니라 absorption을 말하는가?
카드 6 (M6): PK 농도식은 언제 therapeutic window라는 임상 제약으로 바뀌는가?
카드 7 (M7): loading dose와 maintenance dose는 각각 어떤 질문에 답하는가?
카드 8 (M8): 치료역을 알면 interval과 dose 상한을 어떻게 계산하는가?
카드 9 (M9): 효과 plateau는 왜 drug half-life만으로 예측되지 않는가?
카드 10 (M10): 같은 daily dose가 왜 같은 toxicity를 보장하지 않는가?

## 1. 거장의 렌즈

**이 세션의 핵심은 항정상태를 하나의 숫자가 아니라 세 개의 독립 질문으로 분해하는 능력입니다.**

항정상태(steady state; 입력률과 제거률이 같아진 상태)는 "도달했는가 / 얼마인가 / 얼마나 출렁이는가"를 따로 물어야 합니다.

1. **언제 도달하는가?** → $t_{1/2}$가 정합니다.
2. **평균 수준은 어디인가?** → $CL$과 평균 입력속도가 정합니다.
3. **얼마나 출렁이는가?** → $\tau/t_{1/2}$가 정합니다.

같은 평균 투여율이라면 평균량의 plateau 접근 시간표는 같지만, 투여간격이 길어질수록 변동이 커집니다 (R&T Fig. 11-3) [R&T p.325]. 이 분리를 잡고 있으면 `SS=1`, `ADDL/II`, 부하용량, 유지용량을 같은 구조로 읽을 수 있고, 치료역 기반 투여 설계도 이 세 축 위에서 작동합니다.

> 📊 **개념 도식**: 항정상태는 시간(timing) × 수준(level) × 진폭(amplitude)의 세 질문으로 분해됩니다.

$$
\underbrace{\text{Timing}}_{t_{1/2}}\;+\;\underbrace{\text{Level}}_{CL,\;R_{in}}\;+\;\underbrace{\text{Amplitude}}_{\tau/t_{1/2}}
$$

## 2. 로드맵

- **M1–M2**: 정속 주입에서 $CL$은 plateau 수준, $t_{1/2}$는 접근 시간을 정합니다.
- **M3–M4**: 다중투여에서 축적과 평균 plateau를 계산합니다 — **약물량(amount)과 농도(concentration)는 차원이 다릅니다.**
- **M5**: 흡수가 느리면 terminal slope가 elimination을 말하지 않습니다.
- **M6**: 치료역은 PK 식의 결과가 아니라 임상 효용의 제약조건입니다.
- **M7–M8**: 부하/유지 용량과 치료역 기반 알고리즘으로 위 분리를 실제 투여 설계로 옮깁니다.
- **M9**: 효과 plateau는 turnover나 세포 수명이라는 **별개의 시계**가 정할 수 있습니다 — 약물 PK plateau가 답이 아닐 수 있습니다.
- **M10**: 같은 일일 용량이라도 분할이 회복 시간을 어그러뜨리면 독성이 누적됩니다 — 한 개의 노출 변수로 위해를 설명할 수 없습니다.

> 🔑 **세션 잠금**: 항정상태는 "**시간=$t_{1/2}$, 수준=$CL$, 진폭=$\tau/t_{1/2}$**"의 세 축으로 잠급니다. 이 세 축을 섞는 순간 NONMEM steady-state coding, TDM 조정, 부하용량 근거, 치료역 기반 설계가 동시에 흐려집니다.

$$
\underbrace{\text{시간}}_{\text{도달}}:t_{1/2}\quad;\quad\underbrace{\text{수준}}_{\text{평균/plateau}}:CL\quad;\quad\underbrace{\text{진폭}}_{\text{축적/변동}}:\tau/t_{1/2}
$$

---

## §1.5 빠른 읽기 경로

시간이 부족하면 **M1 → M2 → M3 → M4(정의만 skim) → M7 → M8 → M6 → M9 → M10** 순서로 읽으면 이 장의 의사결정 체계가 작동합니다. M4의 $C_{av,ss}$/$A_{av,ss}$ 수식 세부와 M5(flip-flop)는 2회독에서 정독하면 됩니다. 단, **"평균농도와 평균량은 차원이 다른 두 개의 plateau"**라는 사실 하나는 1회독에서 반드시 잡고 가야 M7·M8이 흐려지지 않습니다.

| 시계 구분 | 카드 | 이 묶음이 답하는 질문 |
|---|---|---|
| **약동학 시계 (PK clock)** | M1–M5 | 약물 쪽 시간 구조 — 언제 도달, 얼마나 축적, 농도/약물량 분리, flip-flop |
| **설계 다리 (dosing-design bridge)** | M7–M8 | PK 시계를 임상 투여 설계로 옮김 — loading/maintenance, TW-driven algorithm |
| **PD/안전성 시계 (PD/safety clock)** | M6, M9, M10 | 환자 쪽 시간 — 치료역, 효과 시계, 분할 독성 |

---

<!-- SLIDE_START: §2 | title: §2 — 개념 해부 카드(Concept Anatomy Cards) -->
# §2 — 개념 해부 카드(Concept Anatomy Cards)


<!-- SLIDE_START: M1 | title: §2-M1. 정속 주입 항정상태 농도: $C_{ss}=R_{in}/CL$ -->
## §2-M1. 정속 주입 항정상태 농도: $C_{ss}=R_{in}/CL$

> **거장의 시각**
> 정속 주입 농도를 dose나 volume으로 설명하면, 입력률 오류와 청소율 변화를 같은 원인처럼 섞게 됩니다. $C_{ss}=R_{in}/CL$로 보면 유지 투여의 첫 질문은 **"얼마나 넣고, 얼마나 지우는가"** 하나로 정리됩니다.

### A. 형식적 정의 + 수식

$$
\underbrace{\frac{dC}{dt}}_{\text{농도 변화}}=\underbrace{\frac{R_{in}}{V}}_{\text{입력/V}}-\underbrace{\frac{CL}{V}C}_{\text{제거/V}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $C_{ss}$ | 농도 | 정속 주입 plateau 농도 | $R_{in}$ 증가 시 ↑, $CL$ 증가 시 ↓ |
| $R_{in}$ | dose/time | 단위시간당 입력률 | 주입속도·라인 중단·처방 변경 |
| $CL$ | volume/time | 단위시간당 제거되는 용적 | 신기능·간기능·DDI·질병 상태 |
| $V$ | volume | 농도 상승의 시간상수에 관여하는 분포 용적 | 체성분·단백결합·조직분포 |

> 💡 **수준과 시간은 다른 질문입니다.** $C_{ss}$의 높이는 $CL$과 $R_{in}$의 균형이고, 도달 속도는 다음 카드의 $t_{1/2}$ 문제입니다. $V$가 커지면 상승 곡선은 느려질 수 있지만 plateau 높이를 직접 정하지는 않습니다.
> 🔑 **유지 투여 규칙**: 목표 농도를 정했으면 먼저 $R_{in}=C_{ss}\cdot CL$을 확인합니다.

💡 **비유**: 정속 주입은 수도꼭지를 일정하게 열어 둔 욕조입니다. 수위의 최종 높이는 들어오는 물($R_{in}$)과 배수구 크기($CL$)의 균형으로 정해집니다.

$$
\underbrace{C(t)}_{\text{t시점 농도}}=\overbrace{\underbrace{\frac{R_{in}}{CL}}_{\text{plateau}}}^{C_{ss}}\;\underbrace{\left(1-e^{-(CL/V)t}\right)}_{\text{접근분율}}
$$

$$
\underbrace{C_{ss}}_{\text{SS 농도}}=\frac{\underbrace{R_{in}}_{\text{입력률}}}{\underbrace{CL}_{\text{청소율}}}
$$

### B. 핵심 기억 사항

유지 투여를 시작할 때 먼저 묻는 것은 **"목표농도 × 청소율"**입니다. 목표 $C_{ss}$를 맞추려면 $R_{in}$을 조정하고, 환자의 $CL$ 변화를 반영해야 합니다. $V$는 loading이나 onset 쪽으로 질문이 이동합니다.

> ⚠️ **실무 함정**: 주입 중 관찰 농도가 기대 plateau보다 낮다고 해서 곧바로 $CL$ 증가로 해석하지 마세요. 먼저 **실제 입력률, 라인 중단, sampling time, infusion stop/start 기록**을 확인해야 합니다. 교과서가 보증하는 것은 $C_{ss}=R_{in}/CL$ 구조이지, 특정 현장 오류의 빈도가 아닙니다.

**요약**: 항정상태 농도의 지배자는 청소율, plateau까지 가는 시간의 지배자는 반감기입니다.

> **M1 체화 핵심**
> ① 정속 주입 목표 농도 → $R_{in}/CL$ 균형이 결정
> ② 도달 속도를 묻는 상황 → $V$와 $CL$이 만드는 $t_{1/2}$로 질문 이동
> ⚡ "낮은 관찰 농도 = CL 증가"로 단정 → 입력률·중단·sampling time 미확인 → 보정 방향 실패

---

<!-- SLIDE_START: M2 | title: §2-M2. 항정상태 도달 시간: 3–4 $t_{1/2}$ 규칙 -->
## §2-M2. 항정상태 도달 시간: 3–4 $t_{1/2}$ 규칙

> **앞 카드에서 이 카드로**
> M1에서 plateau의 높이를 $CL$과 입력률로 잠갔으니, 이제 같은 plateau에 **어느 속도로 접근하는지**를 분리합니다.

> **거장의 시각**
> plateau가 높으면 더 오래 걸린다고 생각하면 목표 수준과 접근 비율을 혼동하게 됩니다. $1-e^{-Kt}$로 보면 도달 시간은 **목표 높이가 아니라 $K$와 $t_{1/2}$의 시간표**입니다.

### A. 형식적 정의 + 수식

$$
\underbrace{C(t)}_{\text{t시점 농도}}=\underbrace{C_{ss}}_{\text{plateau}}\;\underbrace{(1-e^{-Kt})}_{\text{도달률}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $C(t)$ | 농도 | 시간 $t$의 농도 | $C_{ss}$와 도달률에 의해 변화 |
| $C_{ss}$ | 농도 | 접근 대상 plateau | $R_{in}/CL$ |
| $K$ | 1/time | 소실 속도상수 | $CL/V$ 변화 |
| $t_{1/2}$ | time | 농도가 절반으로 감소하는 시간 | $K$ 감소 시 ↑ |
| $t_{90}$ | time | plateau 90% 접근 시간 | 약 $3.32t_{1/2}$ |

> 💡 **도달은 비율의 문제입니다.** 90% 도달은 목표 농도의 높이가 아니라 plateau에 대한 접근 비율입니다. 입력률을 올리면 plateau 높이는 바뀌지만 3–4 half-lives 규칙 자체가 빨라지지는 않습니다.
> 🔑 **SS 판단 규칙**: `SS=1`은 실제 투여 이력이 3–4 $t_{1/2}$ 이상인지 확인한 뒤 사용합니다.

💡 **비유**: plateau 접근은 엘리베이터가 목표층으로 가는 것이 아니라 **남은 거리의 절반을 일정 시간마다 줄이는 과정**입니다.

도달률은 $1-e^{-Kt}$이고 $K=\ln2/t_{1/2}$입니다. 90% 도달 시간은 $t=\ln(10)/K\approx3.32\,t_{1/2}$입니다 [R&T p.291].

$$
\underbrace{1-e^{-Kt}}_{\text{도달률}},\qquad \underbrace{K}_{\text{소실 K}}=\frac{\ln 2}{\underbrace{t_{1/2}}_{\text{반감기}}},\qquad \underbrace{t_{90}}_{\text{90\% 도달}}=\frac{\ln 10}{K}\approx3.32t_{1/2}
$$

### B. 실무적 해석

**eptifibatide**($t_{1/2}=2.5$ h, glycoprotein IIb/IIIa 억제제)는 plateau에 비교적 빨리 접근하고, **t-PA**($t_{1/2}=5$ min, 혈전용해제)는 약 17분이면 90% 수준에 도달합니다 [R&T pp.288–293]. 반대로 **phenobarbital**($t_{1/2}=4$ days, 장기 항경련제)처럼 반감기가 길면 plateau 접근 자체가 며칠 걸립니다 [R&T pp.324–325].

**NONMEM 연결**: 항정상태 가정은 "평균적으로 충분히 오래 투여했다"는 시간 조건입니다. `SS=1`을 쓰기 전에 실제 투여 이력이 최소 3–4 half-lives 이상인지 먼저 확인해야 합니다.

**요약**: 목표 수준이 바뀌어도 접근 비율의 시간표는 반감기로만 움직입니다.

> **M2 체화 핵심**
> ① 새 plateau에 언제 도달하는가 → $K$와 $t_{1/2}$가 결정
> ② plateau 높이가 얼마인가 → $R_{in}/CL$ 또는 평균 입력률이 지배
> ⚡ "dose를 올리면 SS 도달도 빨라진다" → level과 timing 혼동 → `SS=1` 적용 오류

---

<!-- SLIDE_START: M3 | title: §2-M3. [⚡ Apex Concept] 다중투여 축적인자 $R_{ac}=1/(1-e^{-K\tau})$ -->
## §2-M3. [⚡ Apex Concept] 다중투여 축적인자 $R_{ac}=1/(1-e^{-K\tau})$

> **앞 카드에서 이 카드로**
> M2에서 도달 시간표가 $t_{1/2}$의 문제임을 잠갔으니, 이제 반복투여가 만드는 **배율과 진폭**을 따로 봅니다.

> **거장의 시각 — 단 하나의 직관**
> $R_{ac}$는 **"얼마나 쌓이는가"**의 배율이지 **"언제 도달하는가"**의 시계가 아닙니다. 흔한 오해 — $R_{ac}$가 크면 항정상태 도달 시간도 길어질 것 같지만, 축적 정도는 $\tau/t_{1/2}$가 정하고 도달 속도는 $K$ 또는 $t_{1/2}$가 정합니다.

### A. 형식적 정의 + 수식

$$
\underbrace{R_{ac}}_{\text{축적계수}}=\frac{1}{1-\underbrace{e^{-K\tau}}_{\text{잔여분}}}=\frac{1}{1-\underbrace{2^{-\tau/t_{1/2}}}_{\text{반감기 잔여}}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $R_{ac}$ | 무차원 | 반복투여가 만든 축적 배율 | $\tau/t_{1/2}$ 감소 시 ↑ |
| $K$ | 1/time | 잔여분 감소 속도 | $CL/V$ 변화 |
| $\tau$ | time | 투여간격 | regimen 설계 |
| $t_{1/2}$ | time | 잔여분을 반으로 줄이는 시간 | clearance·volume 변화 |

> 💡 **배율은 dose-free입니다.** 선형 PK에서 dose를 키우면 농도는 올라가지만 같은 $\tau/t_{1/2}$의 $R_{ac}$ 배율은 그대로입니다. $R_{ac}$ 조정과 항정상태 도달 가속은 같은 조작이 아닙니다.
> 🔑 **Regimen 규칙**: 축적과 fluctuation을 바꾸려면 dose가 아니라 $\tau/t_{1/2}$를 봅니다.

💡 **비유**: $R_{ac}$는 매번 남은 잔돈이 다음 입금에 더해지는 저금통 배율입니다. 입금액이 커져도 같은 주기로 같은 비율이 남으면 배율 자체는 바뀌지 않습니다.

이 식에는 dose가 들어가지 않습니다. 축적 정도는 **용량 크기**가 아니라 **반감기 대비 투여간격($\tau/t_{1/2}$)**이 정합니다 [G pp.44–45; R&T pp.325–326].

### B. 세 결정자 잠금

- **시간 (Timing)**: plateau 접근 시간 = $t_{1/2}$.
- **수준 (Level)**: 평균 plateau 농도 = $CL$과 평균 입력률.
- **진폭 (Amplitude)**: peak-trough fluctuation과 축적계수 = $\tau/t_{1/2}$.

R&T의 200 mg/day 예시는 평균 투여율이 같으면 평균량의 접근 시간표가 같다는 점을 보여줍니다. 달라지는 것은 투여간격이 길어질수록 커지는 변동입니다 [R&T p.325].

### C. Phenobarbital 라벨 잠금

**Phenobarbital**(장기 항경련제) 예시는 "느린 반감기 + 짧은 간격"이 큰 축적과 느린 plateau 접근을 만든다는 좋은 anchor입니다. 단, 라벨을 분리해야 합니다 — R&T 본문은 $t_{1/2}=4$ days, 100 mg q24h에서 축적 지수 **5.8**을 언급하지만, Eq. 11-3/11-10의 peak/trough 기준으로 계산하면 $A_{max,ss}/Dose=630/100\approx$ **6.3**입니다. 즉, 5.8은 $A_{av,ss}/Dose\approx5.76$에 해당하는 **평균 축적 비율**이고, 6.3은 **peak/trough 기준 $R_{ac}$**입니다. 두 숫자는 서로 다른 라벨이므로 혼용하면 안 됩니다 [R&T pp.324–326].

$$
\underbrace{A_{av,ss}/Dose}_{\text{평균 기준}}\approx5.76\qquad;\qquad\underbrace{A_{max,ss}/Dose}_{\text{peak/trough}}\approx6.3
$$

> ⚠️ **실무 함정 — 유령 Plateau 편향**: 투여 시작 직후 자료에 `SS=1`을 부적절하게 적용하면 상승 구간을 plateau로 강제 설명하게 됩니다. 이때 $CL$, bioavailability, IIV 추정이 연쇄적으로 왜곡될 수 있습니다.

### D. Plausible Fallacy — 나비효과 연쇄

**오류**: "$R_{ac}$가 클수록 항정상태 도달 시간이 길어진다."

**왜 그럴싸한가**: trough가 높고 축적이 커 보이면, 임상가는 이를 "아직 plateau에 도달하지 못해서"라고 느끼기 쉽습니다.

**나비효과**: $R_{ac}$를 도달 시간으로 오독 → $\tau$ 조정과 부하용량 전략을 같은 축으로 처리 → [임상] trough 초과 환자에서 interval 조정 방향 또는 loading 판단 실패 → [모델링/규제] `SS=1` 부적절 적용, $CL$·bioavailability·IIV 추정 편향, steady-state 가정 재설명·재분석 요구.

**요약**: 축적인자는 dose 독립, $\tau/t_{1/2}$ 의존입니다. Dose를 키우면 수준은 올라가지만 축적 비율 자체는 바뀌지 않습니다.

> 📖 **Rowland & Tozer 5e, p.325, Fig. 11-3**: 같은 평균 투여율은 평균량 plateau로의 접근 시간을 같게 만들지만, 투여 빈도가 변동을 바꿉니다. → "dose가 아니라 $\tau/t_{1/2}$가 축적과 변동을 정한다"는 M3의 직관을 시각적으로 고정합니다.

> **M3 체화 핵심**
> ① 반복투여에서 얼마나 쌓이는가 → $\tau/t_{1/2}$와 $R_{ac}$가 결정
> ② 절대 평균 농도가 얼마인가 → dose, $CL$, 평균 입력률이 지배
> ⚡ "$R_{ac}$가 크면 도달도 늦다" → 축적 배율과 도달 시간 혼동 → regimen 조정·SS coding 실패

---

<!-- SLIDE_START: M4 | title: §2-M4. 항정상태 평균농도와 평균 amount: $C_{av,ss}$ vs $A_{av,ss}$ -->
## §2-M4. 항정상태 평균농도와 평균 amount: $C_{av,ss}$ vs $A_{av,ss}$

> **앞 카드에서 이 카드로**
> M3에서 반복투여의 배율을 잠갔으니, 이제 항정상태에서 **평균 농도와 평균 약물량의 차원을 분리**합니다.

> **거장의 시각**
> $C_{av,ss}$와 $A_{av,ss}$를 같은 평균 plateau로 읽으면 mg/L와 mg의 단위 방화벽이 무너집니다. **농도는 $CL$ 기반 노출 언어, 약물량은 $MRT$ 기반 체류 언어**로 보면 용량 공식의 자리가 분리됩니다.

### A. 형식적 정의 + 수식

$$
\underbrace{C_{av,ss}}_{\text{평균농도}}=\frac{\underbrace{AUC_{0-\tau,ss}}_{\text{간격 AUC}}}{\underbrace{\tau}_{\text{투여간격}}}=\frac{\underbrace{F\cdot Dose}_{\text{유입량}}}{\underbrace{CL\cdot\tau}_{\text{CL×간격}}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $C_{av,ss}$ | 농도 | 투여간격 평균 농도 | $F\cdot Dose$ ↑, $CL\cdot\tau$ ↑ |
| $AUC_{0-\tau,ss}$ | 농도×시간 | 간격 내 총 노출 | 입력량·청소율 변화 |
| $A_{av,ss}$ | amount | 체내 평균 약물량 | $t_{1/2}$·$F\cdot Dose$ 증가 시 ↑ |
| $MRT$ | time | 분자 평균 체류시간 | $V/CL$ 및 구획 구조 |
| $V$ | volume | amount를 concentration으로 잇는 다리 | 분포·단백결합·구획 가정 |

> 💡 **차원 방화벽**: 평균농도는 mg/L, 평균량은 mg이며, $V$라는 다리 없이 서로 등치할 수 없습니다. $1.44t_{1/2}$가 들어간다고 해서 농도식이 되는 것이 아니라 residence-time 기반 amount 식입니다.
> 🔑 **보고서 규칙**: $C_{av,ss}$와 $A_{av,ss}$는 같은 표라도 단위 열을 분리합니다.

💡 **비유**: $C_{av,ss}$는 욕조의 평균 수위이고 $A_{av,ss}$는 욕조 안 물의 평균 양입니다. 욕조 크기($V$)를 모르면 물의 양을 수위로 바꿀 수 없습니다.

$$
\underbrace{A_{av,ss}}_{\text{평균량}}=\frac{\underbrace{1.44\cdot t_{1/2}}_{\text{MRT 근사}}\;\underbrace{F\cdot Dose}_{\text{유입량}}}{\underbrace{\tau}_{\text{투여간격}}}
$$

첫 식의 단위는 농도, 두 번째 식의 단위는 약물량입니다. **1-구획에서 $MRT=V/CL=1.44t_{1/2}$가 성립할 때만** $C_{av,ss}=A_{av,ss}/V$로 연결됩니다 [R&T p.289; R&T p.324]. 다구획에서는 amount-to-concentration 변환이 모델 구조에 의존합니다.

$$
\underbrace{MRT}_{\text{MRT}}=\underbrace{V/CL}_{\text{V/CL}}=\underbrace{1.44t_{1/2}}_{\text{반감기 시간}}\quad\Rightarrow\quad\underbrace{C_{av,ss}}_{\text{평균농도}}=\frac{\underbrace{A_{av,ss}}_{\text{평균량}}}{\underbrace{V}_{\text{용적}}}
$$

### B. 왜 중요한가

$C_{av,ss}$는 임상 목표·TDM·exposure-response 분석의 언어이고, $A_{av,ss}$는 체내 약물 부담과 체류 시간의 언어입니다. 둘을 섞으면 "농도 목표"와 "체내 약물량" 차원이 무너집니다.

### C. 예시 앵커

- **Table 11-1의 200 mg q24h 예시**는 단회 곡선을 시간 이동해 더하는(superposition; 단회 투여 곡선을 시간 이동해 더함) 방식으로 반복투여 곡선을 예측할 수 있음을 보여줍니다 [R&T pp.320–321].
- **Clobazam**(GABAₐ 양성 알로스테릭 조절제, 항경련제) 예시는 단회 AUC와 투여간격으로 평균 plateau 농도를 예측하는 논리의 anchor입니다 [R&T p.336].
- **Amoxicillin / naproxen / piroxicam** 예시는 같은 amount-time 틀 안에서 **세 가지 다른 $t_{1/2}/\tau$ 영역**을 보여줍니다 [R&T pp.330–332].
  - **Amoxicillin**(짧은 반감기 β-lactam): 투여간격에 비해 elimination이 빠름 → **변동 크고 축적 작음**, peak-trough가 plateau 중심에서 멀리 흔들림.
  - **Naproxen**(중간 반감기 NSAID): 변동과 축적이 모두 적당한 균형 영역.
  - **Piroxicam**(긴 반감기 NSAID): 투여간격이 half-life에 비해 짧음 → **변동 작고 축적 큼**, plateau 곡선이 거의 평탄.
  
  세 약물 모두 같은 식($C_{av,ss}=F\text{Dose}/(CL\tau)$, $A_{av,ss}=1.44F\text{Dose}t_{1/2}/\tau$)으로 평균은 정의되지만, 환자가 실제로 경험하는 **농도 진폭**은 $\tau/t_{1/2}$ 영역에 따라 본질적으로 달라집니다.

**요약**: $C_{av,ss}$는 $CL$ 기반 농도식, $A_{av,ss}$는 $MRT$ 기반 약물량식 — 두 식은 차원이 다릅니다.

> 📊 **개념 도식**: $C_{av,ss}$(농도)와 $A_{av,ss}$(약물량) 사이에는 1-구획 + $V$가 알려진 조건에서만 다리가 놓입니다.

$$
\underbrace{C_{av,ss}}_{\text{농도}}=\frac{F\cdot Dose}{CL\cdot\tau}\;\;\not\equiv\;\;\underbrace{A_{av,ss}}_{\text{약물량}}=\frac{1.44F\cdot Dose\cdot t_{1/2}}{\tau}
$$

> **M4 체화 핵심**
> ① TDM/exposure-response 평균 농도 → $C_{av,ss}$와 $CL$ 기반 식이 결정
> ② body burden/residence time → $A_{av,ss}$와 $MRT$ 기반 식이 지배
> ⚡ $A_{av,ss}$를 농도식으로 표기 → 단위 붕괴 → 용량 rationale 오류

---

<!-- SLIDE_START: M5 | title: §2-M5. Flip-flop 동태: $K_a<K$일 때 terminal slope의 정체 -->
## §2-M5. Flip-flop 동태: $K_a<K$일 때 terminal slope의 정체

> **앞 카드에서 이 카드로**
> M4에서 농도와 약물량의 차원을 분리했으니, 이제 곡선의 **말단 기울기가 정말 elimination을 뜻하는지** 점검합니다.

> **거장의 시각**
> terminal slope를 자동으로 elimination으로 번역하면 **제형이 만든 느린 input을 약물 자체의 느린 제거로 오판**합니다. $K_a<K$ 가능성을 먼저 열어두면 투여경로·제형·흡수 지속시간이 해석의 앞자리에 옵니다.

### A. 형식적 정의 + 수식

$$
\underbrace{K_a<K}_{\text{느린 흡수}}\;\Rightarrow\;\underbrace{\text{terminal slope}}_{\text{말단 기울기}}\approx\underbrace{K_a}_{\text{흡수 K}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $K_a$ | 1/time | 흡수 속도상수 | 제형·투여경로·depot 방출 |
| $K$ | 1/time | 소실 속도상수 | $CL/V$ 변화 |
| terminal slope | 1/time | 말단 구간을 지배하는 더 느린 과정 | $K_a<K$이면 absorption, $K_a>K$이면 elimination |

> 💡 **느린 쪽이 tail을 그립니다.** terminal slope는 elimination이 아니라 **더 느린 process**를 반영합니다. 긴 terminal half-life를 곧바로 느린 elimination으로 쓰지 말고 IV 또는 제형 정보를 먼저 확인합니다.
> 🔑 **Flip-flop 규칙**: $K_a<K$이면 투여간격 판단에 input duration까지 함께 검토합니다.

일반적인 경우는 $K_a>K$이고 terminal slope가 $K$를 반영합니다. Flip-flop에서는 terminal half-life가 길어 보이지만, **약물 소실이 느리다는 뜻이 아니라 흡수 input이 오래 지속되는 상황**일 수 있습니다.

### B. 임상적 비대칭성

**Modified-release(MR) 제형과 depot 제형**은 의도적으로 input을 느리게 만들어 변동을 줄입니다. 즉, 제형이 absorption/input을 지배하면 terminal slope와 투여간격의 임상 의미가 달라집니다.

- **Morphine MR**(모르핀 서방형, 만성 통증): 짧은 elimination half-life에도 q24h regimen 가능.
- **Leuprolide depot**(GnRH 효현제, 전립선암·자궁내막증): 짧은 half-life에도 월 1회 투여 가능.

이것은 "나쁜 flip-flop"이 아니라 **의도된 input 제어**입니다 [R&T pp.337–338].

**요약**: 말단 기울기를 곧바로 elimination으로 번역하지 마세요. 먼저 투여경로, 제형, 흡수 지속시간을 확인합니다.

> 📖 **Gabrielsson & Weiner 5e, p.45, Fig. 2.29**: ordinary case와 flip-flop case의 terminal phase 정체를 분리해 보여줍니다 — terminal slope를 elimination slope로 잘못 읽는 오류가 어디에서 발생하는지를 시각적으로 잡습니다.

> **M5 체화 핵심**
> ① terminal slope가 길어 보일 때 → $K_a<K$ 가능성이 결정
> ② ordinary extravascular decline → $K_a>K$에서 terminal slope가 $K$를 반영
> ⚡ "terminal half-life = elimination half-life" 고정 → 제형/input 효과 누락 → 투여간격 판단 실패

---

<!-- SLIDE_START: M6 | title: §2-M6. Therapeutic Window — PK 식을 임상 의사결정으로 바꾸는 제약조건 -->
## §2-M6. Therapeutic Window — PK 식을 임상 의사결정으로 바꾸는 제약조건

> **앞 카드에서 이 카드로**
> M5에서 입력 함수가 곡선 해석을 바꿀 수 있음을 확인했으니, 이제 PK 식을 **임상 benefit–harm 제약**으로 옮깁니다.

> **거장의 시각**
> 치료역을 단순 농도 범위로만 읽으면 PK 식이 임상 판단으로 넘어가는 지점이 사라집니다. **TW를 효용 역치의 농도 축 투영**으로 보면 $C_{lower}$와 $C_{upper}$가 regimen 설계의 제약조건이 됩니다.

### A. 용어 잠금

- **Therapeutic concentration range**: 임상 경험상 효과가 있고 위해가 받아들여질 만한 농도 범위 [R&T p.272].
- **Therapeutic window**: 효용 곡선의 역치 이상으로 정의되는 임상 의사결정 구간. 두 범위는 겹칠 수 있지만 **같은 개념은 아닙니다** [R&T pp.273–274].
- **Therapeutic index**: 전임상에서는 $TD_{50}/ED_{50}$ ratio로, 임상에서는 **노출 변화에 대한 개별 환자의 limiting effect sensitivity**(노출이 위해·효과를 얼마나 예민하게 바꾸는가)로 이해해야 합니다 [R&T p.278].

$$
\underbrace{TI}_{\text{TI}}\sim\frac{\underbrace{TD_{50}}_{\text{독성 TD50}}}{\underbrace{ED_{50}}_{\text{효과 ED50}}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $C_{lower}$ | 농도 | 효과가 기대되는 하한 | efficacy threshold |
| $C_{upper}$ | 농도 | 위해가 커지는 상한 | toxicity threshold |
| Therapeutic Window | 농도 구간 | benefit–harm 균형의 의사결정 영역 | 임상 반응·환자 민감도 |
| Therapeutic Index | ratio/민감도 | 전임상 ratio 또는 노출 민감도 | 독성 여유·개체변이 |

> 💡 **PK에서 임상으로 넘어가는 문턱**: TW는 식의 결과가 아니라 regimen이 통과해야 하는 benefit–harm 제약입니다. TW와 TI를 같은 안전성 표현으로 합치면 용량 근거가 흐려집니다.
> 🔑 **제약조건 규칙**: $C_{lower}$는 효과 하한, $C_{upper}$는 위해 상한으로 분리해 씁니다.

### B. 효용 수식화 잠금

$U(C)=\sum w_iP_i(C)$ 같은 표현은 **교과서 원수식이 아니라 개념을 식 형태로 표현한 교육적 formalization**입니다. 출처 식과 구별해 읽어야 합니다.

$$
\underbrace{U(C)}_{\text{C별 효용}}=\sum_i \underbrace{w_i}_{\text{가중치}}\;\underbrace{P_i(C)}_{\text{결과확률}}
$$

R&T Fig. 9-4의 가중치 예시는 저자 판단에 따른 illustrative weighting이므로, 표준 규제 가중치처럼 쓰면 안 됩니다 [R&T p.273].

### C. PK/PD 반응 시계

혈장 농도가 항상 효과를 즉시 설명하지는 않습니다.

- **Atorvastatin**(HMG-CoA 환원효소 억제제, 스타틴): PK 반감기 약 14시간이지만 cholesterol 반응 plateau는 3–4주.
- **Erythropoietin**(EPO, 적혈구 생성 자극인자): PK 반감기 약 9시간이지만 hematocrit plateau는 약 70일에 걸침 [R&T pp.343–344].

여기서 질문은 **"약물의 반감기인가, turnover 시스템의 반감기인가"**입니다.

### D. 항균제 앵커

항균제 regimen은 PK index가 다르면 dosing logic도 달라집니다.

- **β-lactam 계열**(time above MIC가 중요): prolonged/continuous infusion이 합리적.
- **Aminoglycoside**(peak/MIC와 toxicity window가 중요): once-daily fractionation이 합리적.

[R&T pp.307–312; R&T pp.347–348]. R&T Fig. 11-20의 **AUC/MIC > 101** 예시는 내성 회피 논리의 정량적 근거입니다 [R&T p.348].

> ⚠️ **실무 함정 — DDI 변수**: protein binding만으로 DDI 민감도를 설명하면 안 됩니다. R&T의 low/high 추출률 예시는 plateau 변화의 핵심 변수가 **간 추출률**임을 보여줍니다 [R&T pp.309–310; R&T pp.350–351].

**요약**: 치료역은 PK 식의 마지막 줄이 아니라 **투여 설계의 제약조건**입니다 — 목표농도, 변동, PD 지연, 독성 메커니즘을 동시에 제한합니다.

> 📖 **Rowland & Tozer 5e, p.272, Fig. 9-3**: 치료역을 단순 농도범위가 아니라 **효과성 · 유해반응 · 효용의 균형**으로 보게 만드는 원문 핵심 그림입니다.

> **M6 체화 핵심**
> ① regimen이 임상적으로 허용되는가 → 치료역이 결정
> ② 안전 여유가 얼마나 민감한가 → 치료지수/노출 민감도가 지배
> ⚡ TW와 TI 동의어 처리 → 농도 구간과 민감도 혼동 → 용량 근거 불명확

---

<!-- SLIDE_START: M7 | title: §2-M7. Loading Dose + Maintenance: 목표 즉시 도달과 유지의 분리 -->
## §2-M7. Loading Dose + Maintenance: 목표 즉시 도달과 유지의 분리

> **앞 카드에서 이 카드로**
> M6에서 치료역이라는 임상 제약을 세웠으니, 이제 **목표에 빨리 도달하는 용량과 유지하는 용량**을 분리합니다.

> **거장의 시각**
> 부하용량과 유지용량을 같은 "용량"으로 뭉치면 즉시 도달과 평균 유지가 섞입니다. **$D_L$은 초기 위치를 잡고, $D_M$은 반복 입력률을 유지한다**는 관점으로 보면 두 식이 하나의 설계 언어가 됩니다.

### A. 형식적 정의 + 수식

$$
\underbrace{D_M}_{\text{유지용량}}=\underbrace{D_L}_{\text{부하용량}}\;\underbrace{(1-e^{-K\tau})}_{\text{보충분율}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $D_L$ | dose | 목표 근처로 즉시 올리는 부하용량 | target 농도·$V/F$ |
| $D_M$ | dose | 반복 투여로 평균 입력률을 유지하는 용량 | $CL$, $\tau$, target 농도 |
| $R_{ac}$ | 무차원 | 유지용량과 부하용량을 잇는 축적 배율 | $\tau/t_{1/2}$ 변화 |
| $K$ | 1/time | 도달 시간과 잔여분을 지배 | $CL/V$ 변화 |

> 💡 **시작과 유지의 분리**: $D_L$은 위치를 맞추고, $D_M$은 평균 입력률을 유지합니다. 부하용량으로 항정상태 시간상수를 바꾸는 것이 아니라 **시작점을 target 근처로 옮기는 것**입니다.
> 🔑 **용량 설계 규칙**: 빠른 발현이 필요하면 $D_L$을, 장기 유지면 $D_M$과 $CL$을 먼저 봅니다.

💡 **비유**: 부하용량은 차를 고속도로 제한속도까지 올리는 가속페달이고, 유지용량은 그 속도를 유지하는 크루즈 컨트롤입니다.

$$
\underbrace{D_L}_{\text{부하용량}}=\frac{\underbrace{D_M}_{\text{유지용량}}}{\underbrace{1-e^{-K\tau}}_{\text{보충분율}}}=\underbrace{R_{ac}}_{\text{축적계수}}\;\underbrace{D_M}_{\text{유지용량}}
$$

**Doxycycline**(테트라사이클린계 항생제) 예시: $t_{1/2}=24$ h, $D_L=200$ mg, $D_M=100$ mg/day, $R_{ac}=2$라는 단순 anchor입니다 [R&T p.327]. **Sirolimus**(mTOR 억제제, 면역억제제): $t_{1/2}=2.5$ days, loading 6 mg, maintenance 2 mg/day — 이론식과 실제 내약성 사이의 조정 필요성을 보여줍니다 [R&T pp.326–327].

$$
\underbrace{D_L}_{200\text{ mg}}=\underbrace{R_{ac}}_{2}\times\underbrace{D_M}_{100\text{ mg/day}}
$$

### B. Bolus + 주입 앵커

정속 주입에서 즉시 plateau 근처로 올리려면 bolus와 infusion을 결합할 수 있습니다 — 먼저 bolus가 초기 농도 위치를 만들고, infusion이 이후 input rate를 유지합니다. Gabrielsson PK13의 수치 anchor: **400 µg/kg bolus + 800 µg/kg over 26 min**, 치료역 50–300 µg/L, $V_c=2.0$ L/kg, $CL=1.0$ L/min/kg, $CL_d=1.0$ L/min/kg, $V_t=5.0$ L/kg [G pp.537–539].

### C. Daptomycin 분할투여 앵커

**Daptomycin**(MRSA 등 그람양성 균에 쓰는 cyclic lipopeptide 항생제) Study A: **75 mg/kg q24h vs 25 mg/kg q8h**. 둘 다 75 mg/kg/day로 같은 일일 용량이지만 CPK는 **991 vs 3996 U/L**로 약 4배 차이가 났습니다 [R&T pp.351–353]. Study B에서는 **같은 $C_{max}=58$ µg/mL** 조건에서도 AUC와 CPK가 분할 패턴에 따라 달랐습니다. → $C_{max}$나 AUC 하나만으로 독성을 설명할 수 없고, **회복 시간과 분할 패턴을 함께** 봐야 한다는 사례입니다.

> 📖 **Rowland & Tozer 5e, p.352 Fig. 11-24 / p.353 Table 11-7**: 이 세션에서 "같은 일일 용량" 비교군을 잘못 잡으면 결론 전체가 뒤집힙니다. Fig. 11-24와 Table 11-7을 함께 보아야 농도 프로파일, 일일 용량, CPK 결과가 분리됩니다.

**요약**: 부하용량은 **초기 조건**, 유지용량은 **장기 입력 속도**, 분할투여는 **회복 시간과 변동**을 바꿉니다.

$$
\underbrace{LD}_{\text{부하용량}}=\frac{\underbrace{V}_{\text{V}}\;\underbrace{\text{target}}_{\text{목표농도}}}{\underbrace{F}_{\text{F}}},\qquad
\underbrace{MD}_{\text{유지용량}}=\underbrace{CL}_{\text{청소율}}\;\underbrace{\text{target}}_{\text{목표농도}}\;\underbrace{\tau}_{\text{투여간격}}
$$

**실무 활용**: 중환자실 부하용량 프로토콜에서 신기능 조정 항목을 LD와 MD에 분리해 명시합니다. Daptomycin Study A(75 mg/kg q24h vs 25 mg/kg q8h, CPK 991 vs 3996 U/L)는 "같은 일일 용량 ≠ 같은 독성"의 라벨 근거입니다.

> **M7 체화 핵심**
> ① 초기 목표 근처에서 시작해야 할 때 → $D_L$과 $V/F$가 결정
> ② 장기 평균을 유지할 때 → $D_M$, $CL$, $\tau$가 지배
> ⚡ "부하용량이 SS 시간을 단축한다" → 시작점 이동과 시간상수 혼동 → 발현 근거 과장

---

<!-- SLIDE_START: M8 | title: §2-M8. 치료역 기반 투여 설계 알고리즘(TW-Driven Dosage Design Algorithm) -->
## §2-M8. 치료역 기반 투여 설계 알고리즘(TW-Driven Dosage Design Algorithm)

> **앞 카드에서 이 카드로**
> M7에서 부하와 유지의 역할을 분리했으니, 이제 $C_{upper}$와 $C_{lower}$로 **실제 투여간격과 용량 상한**을 계산합니다.

> **거장의 시각**
> TW 알고리즘을 자동 처방기로 읽으면 선형 PK와 즉각적 농도–반응 가정이 무너진 순간에도 공식을 밀어붙이게 됩니다. 이를 **타당성 점검(feasibility screen)**으로 읽으면 interval, dose size, loading 필요성을 각각 다른 파라미터로 방어할 수 있습니다.

### A. 형식적 정의 + 수식

$$
\underbrace{C_{lower}}_{\text{하한}}=\underbrace{C_{upper}}_{\text{상한}}\;\underbrace{e^{-K\tau_{max}}}_{\text{허용감소}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $\tau_{max}$ | time | 치료역 안에 머물 수 있는 최대 투여간격 | $t_{1/2}$, $C_{upper}/C_{lower}$ |
| $D_{M,max}$ | dose | 유지용량 상한 | $V/F$, $C_{upper}-C_{lower}$ |
| $C_{upper}$ | 농도 | 안전성 상한 | toxicity threshold |
| $C_{lower}$ | 농도 | 효과 하한 | efficacy threshold |
| $V/F$ | volume | apparent volume 다리 | bioavailability·분포 변화 |

> 💡 **TW는 알고리즘의 울타리**: $C_{upper}/C_{lower}$는 interval을, $C_{upper}-C_{lower}$는 dose size를 제약합니다. PD plateau, flip-flop, 비선형성이 의심되면 TW 공식은 최종 처방이 아니라 **screen에 그칩니다**.
> 🔑 **중단 규칙**: 선형 PK와 즉각적 농도–반응 가정이 깨지면 모델 확장으로 돌아갑니다.

💡 **비유**: 치료역 기반 알고리즘은 차선 폭 안에서 속도와 차간거리를 정하는 운전 규칙입니다. 차선이 좁으면 간격과 속도 선택의 자유가 줄어듭니다.

$$
\underbrace{\tau_{max}}_{\text{최대간격}}=\frac{\underbrace{\ln(C_{upper}/C_{lower})}_{\text{로그폭}}}{\underbrace{K}_{\text{소실 K}}}=\underbrace{1.44t_{1/2}}_{\text{시간척도}}\;\underbrace{\ln\left(\frac{C_{upper}}{C_{lower}}\right)}_{\text{TW 폭}}
$$

$$
\underbrace{D_{M,max}}_{\text{최대 MD}}=\underbrace{\frac{V}{F}}_{\text{V/F 보정}}\;\underbrace{(C_{upper}-C_{lower})}_{\text{허용상승}}
$$

$$
\underbrace{C_{ss,av}}_{\text{허용평균}}=\frac{\underbrace{C_{upper}-C_{lower}}_{\text{선형폭}}}{\underbrace{\ln(C_{upper}/C_{lower})}_{\text{로그폭}}}
$$

### B. 알고리즘 잠금

1. $C_{lower}$, $C_{upper}$를 정합니다.
2. $t_{1/2}$로 $\tau_{max}$를 계산합니다.
3. $V/F$로 $D_{M,max}$를 계산합니다.
4. 실제 제형 강도와 복약 순응도를 고려해 practical $\tau$와 $D_M$을 선택합니다.
5. 필요하면 $D_L$로 initial target에 접근합니다.

> ⚠️ **실무 함정**: 이 알고리즘은 **선형 PK, 고정 투여간격, target 농도와 임상 반응 사이의 충분한 직접 연결**을 전제로 합니다. 단회 투여 치료나 PD plateau가 turnover로 지배되는 약물에서는 그대로 적용하면 안 됩니다 [R&T p.279; R&T pp.341–345].

**요약**: M8은 M1–M7을 투여 알고리즘으로 묶는 끝점입니다. $C_{upper}/C_{lower}$는 interval, $V/F$는 용량 크기, $CL$은 평균 농도를 각각 제약합니다.

$$
\underbrace{\tau_{max}}_{\text{간격상한}}=1.44t_{1/2}\ln\left(\frac{C_{upper}}{C_{lower}}\right),\qquad
\underbrace{D_{M,max}}_{\text{용량상한}}=\frac{V}{F}(C_{upper}-C_{lower})
$$

**실무 활용**: 신약 임상시험 dose-finding 프로토콜의 표준 sequence로 치료역 기반 알고리즘을 기본값으로 채택하되, **선형 PK 비성립 · 즉각적 농도-반응 가정 깨짐 · flip-flop · 단회 투여 치료 · turnover 지배 PD plateau** 중 하나라도 의심되면 적용을 중단하고 모델 확장으로 돌아간다는 점을 프로토콜 첫 페이지에 명시합니다.

> 📖 **Rowland & Tozer 5e, p.335, Fig. 11-10**: $C_{upper}$, $C_{lower}$, $\tau_{max}$, $D_M$, $D_L$이 하나의 투여 설계 순서임을 같은 틀 안에 묶어 보여줍니다.

> **M8 체화 핵심**
> ① 치료역 안에서 투여간격을 정할 때 → $\tau_{max}$와 $C_{upper}/C_{lower}$가 결정
> ② 유지용량 상한을 정할 때 → $D_{M,max}$와 $V/F$가 지배
> ⚡ TW 알고리즘을 자동 처방기로 사용 → 가정 위반 누락 → 모델 확장 필요성 놓침

---

<!-- SLIDE_START: M9 | title: §2-M9. PD 기반 Plateau(PD-Driven Plateau): 효과의 시계는 약물의 시계와 다를 수 있습니다 -->
## §2-M9. PD 기반 Plateau(PD-Driven Plateau): 효과의 시계는 약물의 시계와 다를 수 있습니다

> **앞 카드에서 이 카드로**
> M8에서 PK 기반 투여 알고리즘의 적용 조건을 잠갔으니, 이제 **효과 plateau가 PK plateau와 다른 시계로 움직이는 예외**를 봅니다.

> **거장의 시각**
> PK plateau를 효과 plateau로 옮겨 쓰면 statin과 EPO 같은 turnover 지배 약물에서 평가 시점을 앞당기게 됩니다. **"무엇의 반감기인가"**를 먼저 물으면 약물 시계와 생물학적 시계가 분리됩니다.

### A. 형식적 정의 + 앵커

- **Atorvastatin**(HMG-CoA 환원효소 억제제): PK $t_{1/2}\approx14$ h이지만 cholesterol 반응의 최대 효과는 **3–4주** [R&T p.343].
- **Erythropoietin**(EPO, 적혈구 생성 자극인자): PK $t_{1/2}\approx9$ h이지만 hematocrit plateau는 **약 70일** (RBC 수명 약 120일에 종속) [R&T p.344].

$$
\underbrace{t_{1/2,\;PK}}_{\text{PK 시계}}\not\equiv\underbrace{t_{\text{PD plateau}}}_{\text{PD 시계}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $t_{1/2,PK}$ | time | 약물 농도 plateau의 시계 | 약물 청소율·용적 |
| $t_{PD\ plateau}$ | time | 효과 plateau의 시계 | turnover·세포 수명 |
| turnover | 1/time 또는 time | 반응 변수의 생성·소실 구조 | 생리적 회복·세포 수명 |
| response variable | 효과 단위 | cholesterol, hematocrit 등 관찰 반응 | 약물 효과 + 생물학적 시계 |

> 💡 **무엇의 반감기인가**: 약물 반감기와 반응 시스템의 반감기는 같은 숫자가 아닐 수 있습니다. 3–4 $t_{1/2}$ 규칙을 cholesterol 반응이나 hematocrit plateau에 그대로 옮기면 발현을 과대평가합니다.
> 🔑 **평가 시점 규칙**: turnover 지배 약물은 PK sampling 일정과 PD endpoint timing을 따로 설계합니다.

### B. 핵심 기억 사항

**"언제 효과 plateau에 도달하는가?"의 답은 "약물 $t_{1/2}$의 3–4배"가 아닐 수 있습니다.** 먼저 무엇의 반감기인지 물어야 합니다 — 약물의 반감기인가, cholesterol 합성의 turnover time인가, RBC의 수명인가.

**M2 / M8 연결**: M2의 "3–4 half-lives ≈ 90%" 규칙을 PD plateau에 그대로 옮기면 발현을 과대평가합니다. M8 TW 알고리즘은 즉각적 농도–반응 가정이 성립할 때만 유효합니다. **turnover 지배 약물에서는 알고리즘 적용 전에 PD 시간척도 검토를 먼저 수행**해야 합니다.

**요약**: PK plateau ≠ PD plateau. 효과의 시계는 약물 분자가 아니라 **내인성 전환 시스템**이 정할 수 있습니다.

> ⚠️ **실무 함정 — PD Plateau 시점 오류**: PD plateau 도달 시점 예측에서 가장 흔한 함정은 약물 $t_{1/2}$ 숫자를 turnover 시스템에 그대로 대입하는 것입니다. Atorvastatin의 최대 cholesterol 반응을 "3–4 half-lives = 2–3일"로 예측하면, 실제 plateau인 3–4주까지 regimen 결정 시점을 심각하게 앞당기게 됩니다 [R&T pp.341–345]. 효과 평가 시점을 설계하기 전에 반드시 **"무엇의 반감기인가 — 약물인가, turnover/세포 수명인가"**를 확인합니다.

> **M9 체화 핵심**
> ① 효과 plateau가 늦게 올 때 → turnover/세포 수명이 결정
> ② 혈장 농도 plateau → 약물 $t_{1/2}$와 PK clock이 지배
> ⚡ "PD plateau = 3–4 drug half-lives" → 효과 평가 시점 조기화 → regimen 판단 실패

---

<!-- SLIDE_START: M10 | title: §2-M10. 용량분할 독성(Dose Fractionation Toxicity): 같은 일일 용량(daily dose)가 같은 위해를 의미하지 않습니다 -->
## §2-M10. 용량분할 독성(Dose Fractionation Toxicity): 같은 일일 용량(daily dose)가 같은 위해를 의미하지 않습니다

> **앞 카드에서 이 카드로**
> M9에서 효과의 시계가 약물 농도와 분리될 수 있음을 확인했으니, 마지막으로 **독성 누적이 분할과 회복 시간에 의해 달라지는 상황**을 봅니다.

> **거장의 시각**
> "같은 일일 용량이면 같은 독성"이라고 읽으면 회복 시간이 짧아진 조직 손상을 놓칩니다. **분할을 회복 시간과 함께** 보면 혈장 노출과 조직 손상 누적이 분리됩니다.

### A. 형식적 정의 + 앵커

**Daptomycin Study A** — **75 mg/kg q24h vs 25 mg/kg q8h**. 두 regimen 모두 75 mg/kg/day로 일일 용량이 같지만 CPK는 **991 vs 3996 U/L**로 약 4배 차이 [R&T pp.351–353].

Study B는 **같은 $C_{max}=58$ µg/mL** 조건에서도 AUC와 CPK가 분할 패턴에 따라 달라짐을 보여주었습니다 [R&T p.353].

$$
\underbrace{C_{max}}_{\text{최대농도}}=58\ \mu\mathrm{g/mL}\quad\not\Rightarrow\quad\underbrace{\text{동일독성}}_{\text{AUC·회복시간 의존}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $C_{max}$ | 농도 | 최고 농도 | dose 크기·흡수속도·분할패턴 |
| AUC | 농도×시간 | 총 노출 | dose·청소율 |
| fractionation interval | time | 분할투여 간격 | q24h, q8h 등 regimen |
| recovery time | time | 표적 조직이 손상에서 회복하는 시간 | 조직 생물학 |
| CPK | U/L | 근육 독성 표지자 | daptomycin 분할 패턴 |

> 💡 **같은 일일 용량의 함정**: 총량이 같아도 q24h와 q8h는 회복 시간을 다르게 남깁니다. $C_{max}$ 또는 AUC 하나만으로 독성을 고정하면 분할 효과가 사라집니다.
> 🔑 **비교군 규칙**: 분할 논문에서는 mg/kg/day가 정말 같은지 먼저 계산합니다.

💡 **비유**: 같은 양의 운동도 휴식 없이 세 번 나누어 하면 근육 손상이 커질 수 있습니다. 분할은 총량보다 **회복 틈을 얼마나 남기는지**의 문제입니다.

### B. 핵심 기억 사항

독성을 단일 변수($C_{max}$ 또는 AUC) 하나로만 설명하면 안 됩니다. 분할이 짧은 회복 간격을 만들면, **표적 조직이 회복하지 못한 상태에서 다음 노출이 시작되어 누적 손상**이 일어날 수 있습니다.

**M3 / M7 연결**: M3의 $R_{ac}$ 식은 plasma compartment의 누적만 다룹니다. M10은 **"약물 자체의 누적"이 아니라 "조직 손상의 누적"**이라는 다른 차원의 누적을 말합니다. M7의 부하 + 유지 분리에서도 용량 크기만 보지 말고 분할 패턴과 회복 시간을 함께 봐야 합니다.

**요약**: 같은 일일 용량 ≠ 같은 독성. 회복 시간이 분할 간격보다 길면 누적 손상이 발생할 수 있습니다.

> ⚠️ **실무 함정 — 비교군 정의 오류**: 분할 독성 분석에서 비교군을 잘못 정의하면 결론 전체가 뒤집힙니다. Daptomycin Study A에서 "같은 일일 용량" 비교군이 **75 mg/kg q24h vs 25 mg/kg q8h**임을 직접 확인해야 합니다 [R&T pp.351–353]. 이를 25 mg/kg q24h vs 25 mg/kg q8h로 오독하면 일일 용량이 3배 차이가 나므로 분할의 순수 효과를 분리할 수 없습니다. 문헌에서 "same dose"라는 표현이 등장할 때마다 분자와 분모를 직접 계산해 실제 일일 총량을 확인하는 습관이 필수입니다.

> **M10 체화 핵심**
> ① 같은 일일 용량인데 독성이 다를 때 → 분할과 회복 시간이 결정
> ② 혈장 노출 비교 → $C_{max}$, AUC, trough가 각각 다른 정보를 지배
> ⚡ "same daily dose = same toxicity" → 조직 회복 시간 누락 → regimen 선택 오류

---

<!-- SLIDE_START: §5 | title: §5 — 혼동 쌍 해부(Confusion Pair Dissection) -->
# §5 — 혼동 쌍 해부(Confusion Pair Dissection)

## §5-쌍1. $C_{ss}$ vs $C_{av,ss}$ vs $A_{av,ss}$

| 비교 기준 | $C_{av,ss}$ | $A_{av,ss}$ |
|---|---|---|
| 단위 / 차원 | 농도 | 약물량 |
| 수식 내 위치 | $F\text{Dose}/(CL\tau)$ | $1.44F\text{Dose}t_{1/2}/\tau$ |
| 변화 원인 | $CL$, $F$, dose, interval | $MRT$, $t_{1/2}$, dose, interval |
| 혼동 시 임상 결과 | TDM target 왜곡 | body burden을 농도 target으로 오독 |

| 항목 | 정확한 분리 | 왜 중요한가 |
|---|---|---|
| $C_{ss}$ | 정속 주입 plateau 농도: $R_{in}/CL$ | infusion 유지 target |
| $C_{av,ss}$ | 다중투여 간격 평균 농도: $F\text{Dose}/(CL\tau)$ | TDM/노출-반응 target |
| $A_{av,ss}$ | plateau 평균 약물량: $1.44F\text{Dose}t_{1/2}/\tau$ | residence time/body burden |

$$
\underbrace{C_{ss}}_{\text{plateau}},\quad \underbrace{C_{av,ss}}_{\text{interval 평균농도}},\quad \underbrace{A_{av,ss}}_{\text{평균량}}
$$

**치명적 타격**: $1.44F\text{Dose}t_{1/2}/\tau$를 농도 식으로 쓰면 단위가 틀립니다. **1-구획과 알려진 $V$가 명시되지 않으면 약물량-농도 변환이 성립하지 않습니다** [R&T p.324; R&T p.337].

**⚡ 기억 고리 — 물 비유로 차원 인코딩**: $C_{av,ss}$는 **욕조의 평균 수위**(mass/volume), $A_{av,ss}$는 **욕조 안 물의 평균 양**(mass), $C_{ss}$는 **수도꼭지를 정해진 속도로 열어둔 정상상태의 수위**입니다. 같은 욕조($V$ 알려짐, 1-구획)에서만 "수위 = 물의 양 / 욕조 크기"라는 다리가 놓입니다. 욕조 모양이 바뀌면(다구획) 같은 양의 물이라도 수위가 달라집니다.

---

## §5-쌍2. NONMEM `SS=1` vs `SS=2`

| 비교 기준 | `SS=1` | `SS=2` |
|---|---|---|
| 단위 / 차원 | steady-state dose event flag | steady-state infusion/input condition |
| 수식 내 위치 | 초기조건/투여 event | 초기조건/input function |
| 변화 원인 | 충분한 반복투여 이력 | input 형태와 정상상태 조건 |
| 혼동 시 임상 결과 | 상승 구간을 plateau로 오인 | bolus/infusion 초기조건 설정 오류 |

| 항목 | `SS=1` | `SS=2` |
|---|---|---|
| 의미 | 정상상태 dose event | 정상상태 infusion/input condition |
| 위험 | 실제 축적 단계를 plateau로 오인 | bolus/infusion 초기조건을 잘못 설정 |
| 선행 질문 | 충분한 투여 이력이 있었는가? | input이 어떤 형태였는가? |

**치명적 타격**: 정상상태 플래그는 "편의상 넣는 옵션"이 아니라 **초기 조건을 수학적으로 바꾸는 명령**입니다. 투여 이력이 plateau 조건을 만족하지 않으면 쓰지 않습니다.

**⚡ 기억 고리 — 깃발 비유로 시제 인코딩**: `SS=1`은 **"옛날부터 같은 dose가 충분히 반복됐다"**고 NONMEM에 알리는 **과거형 깃발** — 직전 사건만이 아니라 무한 과거의 같은 패턴이 누적된 결과를 가정합니다. `SS=2`는 **"지금 이 순간 정상상태 입력이 진행 중"**임을 알리는 **현재진행형 깃발** — bolus가 아닌 input function의 형태가 plateau 조건을 채웠음을 가정합니다. 두 깃발 모두 시제를 잘못 꽂으면 NONMEM은 존재하지 않는 history를 만들어냅니다.

---

## §5-쌍3. Flip-flop vs ordinary extravascular decline

| 비교 기준 | Ordinary extravascular | Flip-flop |
|---|---|---|
| 단위 / 차원 | $K_a>K$ | $K_a<K$ |
| 수식 내 위치 | terminal slope $\approx K$ | terminal slope $\approx K_a$ |
| 변화 원인 | 흡수보다 소실이 상대적으로 느림 | 제형·depot·흡수 지속시간 |
| 혼동 시 임상 결과 | elimination half-life 해석 가능 | absorption-limited tail을 elimination으로 오독 |

| Ordinary | Flip-flop |
|---|---|
| $K_a>K$ | $K_a<K$ |
| terminal slope $\approx$ elimination | terminal slope $\approx$ absorption |
| terminal half-life가 약물 elimination 정보를 줌 | terminal half-life가 제형/input 정보를 줄 수 있음 |

$$
\underbrace{K_a>K}_{\text{일반형}}\Rightarrow\text{terminal slope}\approx K,\qquad \underbrace{K_a<K}_{\text{flip-flop}}\Rightarrow\text{terminal slope}\approx K_a
$$

**치명적 타격**: 말단 기울기만 보고 elimination 반감기를 확정하면 안 됩니다. **투여경로, 제형, 흡수 지속시간이 먼저**입니다 [G pp.45–46].

**⚡ 기억 고리 — 수도꼭지/배수구 역할 전도**: **Ordinary**: 큰 배수구(빠른 elimination, $K$가 큼) + 작은 수도꼭지(느린 absorption) → 입력이 끝나면 배수구가 빠르게 비워서 **배수구의 속도($K$)**가 terminal slope를 그립니다. **Flip-flop**: 작은 배수구(느린 elimination) + 더 작은 수도꼭지(더 느린 absorption, $K_a<K$) → 입력이 길게 이어져서 **수도꼭지의 속도($K_a$)**가 terminal slope를 그립니다. 즉, terminal phase가 보여주는 것은 "더 느린 쪽의 속도"이지 항상 elimination이 아닙니다 — terminal slope의 정체는 **두 process 중 더 율속단계(rate-limiting; 전체 속도를 정하는 느린 단계)인 쪽**입니다.

---

## §5-쌍4. 도달 시간 vs 축적 정도 vs fluctuation

| 비교 기준 | 도달 시간 | 축적/진폭 |
|---|---|---|
| 단위 / 차원 | time | 무차원 배율 또는 농도 진폭 |
| 수식 내 위치 | $1-e^{-Kt}$ | $R_{ac}=1/(1-e^{-K\tau})$; $\tau/t_{1/2}$ |
| 변화 원인 | $t_{1/2}$, $K$ | 투여간격, 반감기 대비 interval |
| 혼동 시 임상 결과 | SS 도달 시점 오판 | dose/interval 조정 방향 오류 |

| 질문 | 결정자 | 대표식 |
|---|---|---|
| plateau에 언제 도달하는가? | $t_{1/2}$ | $1-e^{-Kt}$ |
| 얼마나 축적되는가? | $\tau/t_{1/2}$ | $R_{ac}=1/(1-e^{-K\tau})$ |
| 평균 수준은 어디인가? | $CL$과 평균 입력률 | $C_{av,ss}=F\text{Dose}/(CL\tau)$ |
| peak-trough 진폭은? | $\tau/t_{1/2}$ | 투여간격이 길수록 커짐 |

$$
\underbrace{1-e^{-Kt}}_{\text{도달률}},\quad \underbrace{R_{ac}}_{\text{축적계수}}=\frac{1}{1-e^{-K\tau}},\quad \underbrace{C_{av,ss}}_{\text{평균수준}}=\frac{F\text{Dose}}{CL\tau}
$$

**치명적 타격**: 용량을 두 배로 하면 농도 수준은 올라가지만, **$R_{ac}$ 자체는 변하지 않습니다.**

**⚡ 기억 고리 — 4개의 자(scale)가 같은 약 한 방울에서 갈라진다**: **도달 시간**($1-e^{-Kt}$)은 **시계** — $t_{1/2}$로 똑딱입니다. **축적 정도**($R_{ac}$)는 **배율** — $\tau/t_{1/2}$로 결정되며 dose 크기와 무관합니다. **평균 농도**($C_{av,ss}$)는 **무게중심** — $CL$과 평균 입력률이 정합니다. **진폭**(peak-trough swing)은 **출렁임** — 같은 평균이라도 $\tau/t_{1/2}$가 클수록 큰 파도. 같은 약물에 손을 댈 때 어느 자(시계/배율/무게중심/출렁임)를 움직이려는지 먼저 묻는 것이 숙련자의 첫 질문입니다.

---

## §5-쌍5. Therapeutic Window vs Therapeutic Index

| 비교 기준 | Therapeutic Window | Therapeutic Index |
|---|---|---|
| 단위 / 차원 | 농도 구간 | ratio 또는 노출 민감도 |
| 수식 내 위치 | $C_{lower}$–$C_{upper}$ 경계 | 전임상 ratio 또는 임상 민감도 |
| 변화 원인 | 효과/독성 역치 | 독성 여유, 변동성, 민감도 |
| 혼동 시 임상 결과 | 농도 경계 오판 | 안전 여유 과대해석 |

| 개념 | 정확한 의미 | 오해 |
|---|---|---|
| Therapeutic Window | 효용 역치 이상의 농도 영역 | "경험적 치료농도범위"와 동의어로 사용 |
| Therapeutic Concentration Range | 임상 경험상 효과와 허용 위해를 만족하는 농도 범위 | TW와 항상 같은 수치라고 가정 |
| Therapeutic Index | 전임상 ratio 또는 임상 노출 민감도 | high TI가 모든 환자의 안전을 보장한다고 해석 |

**치명적 타격**: **넓은 치료역과 높은 치료지수는 같은 문장이 아닙니다.** 전자는 농도 경계, 후자는 노출 변화에 대한 안전 여유/민감도 문제입니다 [R&T pp.272–278].

**⚡ 기억 고리 — 자(ruler)와 떨림(tremor)의 구조 차이**: **Therapeutic Window**는 농도라는 **자 위에 그어진 두 선** — $C_{lower}$와 $C_{upper}$로 정의되는 **공간**의 문제. 넓은 window는 두 선 사이가 멀다는 뜻일 뿐입니다. **Therapeutic Index**는 그 **선의 굵기(전임상 ratio)**이거나 **환자의 손떨림(임상 노출 민감도)** — 같은 두 선을 그은 자라도 손이 떨리는 환자(높은 변동성)에서는 효과적인 자가 못 됩니다. 즉 TW는 **공간 척도**, TI는 **변동성/민감도 척도**입니다. wide TW + low TI 환자는 아주 흔한 임상 시나리오이며, 두 개념을 같다고 보면 이 환자군 전체가 보이지 않습니다.

---

## §5-쌍6. MRT vs half-life

| 비교 기준 | $t_{1/2}$ | MRT |
|---|---|---|
| 단위 / 차원 | time | time |
| 수식 내 위치 | slope 기반 $\ln2/K$ | $AUMC/AUC$ moment ratio |
| 변화 원인 | $K$, $CL/V$ | 체류시간, 구획 분포, elimination |
| 혼동 시 임상 결과 | slope time을 평균 체류시간으로 오독 | 약물량/농도 연결 오류 |

| 항목 | 의미 | 주의 |
|---|---|---|
| $t_{1/2}$ | 약물량/농도가 절반이 되는 시간 | 1차 감소의 slope 기반 |
| MRT | 분자가 체내에 머무는 평균 시간 | moment-based: $AUMC/AUC$ |
| 1-구획 | $MRT=1/K=1.44t_{1/2}=V/CL$ | 단순식 가능 |
| 다구획 | $MRT=AUMC_{0-\infty}/AUC_{0-\infty}$ | $V/CL$ 단순 치환 위험 |

$$
\underbrace{MRT}_{\text{MRT}}=\frac{\underbrace{AUMC_{0-\infty}}_{\text{시간가중 AUC}}}{\underbrace{AUC_{0-\infty}}_{\text{총 AUC}}}
$$

**치명적 타격**: $1.44t_{1/2}$는 1차 선형 시스템의 시간척도일 뿐이고, **어떤 구획의 농도를 대표하는지는 모델 구조가 결정**합니다 [R&T p.289; R&T pp.299–304].

**⚡ 기억 고리 — 기울기 시간 vs 무게중심 시간**: $t_{1/2}$는 **곡선의 기울기**가 만든 시간 — "절반이 될 때까지"라는 곡선 모양에 종속된 척도입니다. **MRT**는 **곡선 아래 면적의 무게중심** — 분자 한 개가 평균적으로 머문 시간을 묻는 moment-based 척도입니다. 두 척도는 **1-구획에서만 우연히 깔끔한 비율**($MRT=1.443\,t_{1/2}=V/CL$)로 일치합니다. 다구획에서는 분자가 central → tissue → central을 왕복하므로 MRT가 단순 $V/CL$로 환원되지 않습니다. 즉, $1.443\times t_{1/2}$를 어떤 구획의 시간척도로 바로 옮기는 순간 **moment를 slope로 압축**하는 차원 함몰이 일어납니다.

---

## §5-쌍7. Acquired Resistance vs Tolerance

| 비교 기준 | Acquired Resistance | Tolerance |
|---|---|---|
| 단위 / 차원 | population/mutation 변화 | 환자/시스템 PD 적응 |
| 수식 내 위치 | 노출 target·resistance window | 반응 함수·feedback |
| 변화 원인 | 선택 압력, clonal shift | 수용체 둔감화, 항상성 |
| 혼동 시 임상 결과 | 항균제 노출 전략 실패 | drug holiday/속도 제어 전략 실패 |

| 항목 | Acquired resistance | Tolerance |
|---|---|---|
| 본질 | 세포/미생물 population 또는 mutation 변화 | 환자/시스템의 PD 적응 |
| 시간 구조 | 선택 압력과 population shift | 수용체 둔감화 또는 항상성 feedback |
| 관리 논리 | 노출 target, resistance window 회피 | drug holiday, modified release, rate-of-change 제어 |

**치명적 타격**: 효과 감소가 보인다고 모두 tolerance가 아닙니다. 항균제에서는 resistance selection이, **nitrate / nicotine / nifedipine**(혈관확장제·중추신경 작용제·칼슘채널 차단제)에서는 PD 적응이 핵심일 수 있습니다 [R&T pp.346–348].

**⚡ 기억 고리 — 적이 변했나, 내가 변했나**: **Acquired Resistance**: **적이 변한 것** — 표적 미생물·세포 population이 선택 압력 하에 mutation/clonal shift로 약물에 둔감해졌습니다. 약물도 환자도 그대로지만 표적이 다른 표적이 되었습니다. **Tolerance**: **내가 변한 것** — 환자/시스템(수용체 downregulation, 항상성 feedback)이 같은 약물에 적응했습니다. 표적은 그대로지만 내 반응이 약해졌습니다. 임상 관리 논리도 다릅니다 — resistance는 **노출 패턴(MIC 회피, AUC/MIC 확보)**으로, tolerance는 **drug holiday, modified-release, rate-of-change 제어**로 다룹니다. "효과가 떨어진다"는 같은 표면 증상에서 두 메커니즘은 정반대 방향의 처방을 만듭니다.

**§5 요약**: 위험한 혼동은 "수학식의 기호가 비슷해서"만 생기지 않습니다. 더 자주 생기는 원인은 **결정자가 다른 질문을 같은 질문으로 취급**하는 것입니다.

---

<!-- SLIDE_START: §7 | title: §7 — 자기 테스트 모듈(Self-Test Module) -->
# §7 — 자기 테스트 모듈(Self-Test Module)

## §7-회상 영역(Recall Layer)

### Q1. 정속 주입에서 $C_{ss}$를 결정하는 파라미터는?
**답**: $C_{ss}=R_{in}/CL$이므로 plateau 농도 수준은 **청소율과 입력률**이 정합니다 [G p.23; R&T p.288].

### Q2. 90% plateau에 도달하는 데 필요한 시간은 대략 몇 half-lives인가?
**답**: 약 3.3 half-lives, 실무적으로 3–4 half-lives [G p.22; R&T p.291].

### Q3. 다중투여 축적계수에 dose가 들어가지 않는 이유는?
**답**: 같은 dose가 반복될 때 잔여분의 비율은 $e^{-K\tau}$이고, 반복합은 등비수열이므로 ratio는 **$\tau/t_{1/2}$에만 의존**합니다 [G pp.44–45; R&T pp.795–797].

### Q4. $C_{av,ss}$와 $A_{av,ss}$의 차원은 각각 무엇인가?
**답**: $C_{av,ss}$는 농도, $A_{av,ss}$는 약물량입니다. **$A_{av,ss}$를 농도처럼 쓰면 차원 오류**입니다 [R&T p.324; R&T p.337].

### Q5. Flip-flop에서 말단 기울기는 무엇을 반영하는가?
**답**: $K_a<K$이면 말단 기울기는 **흡수속도**를 반영합니다 [G pp.45–46].

---

## §7-적용 영역(Application Layer)

### Q6. 어떤 약물의 $t_{1/2}=8$ h이고 q24h 투여합니다. 축적은 클까?
**답**: $\tau/t_{1/2}=3$이므로 $R_{ac}=1/(1-2^{-3})\approx1.14$로 크지 않습니다. q24h라도 half-life 대비 interval이 길면 축적은 작습니다.

$$
\underbrace{\tau/t_{1/2}}_{3}\Rightarrow \underbrace{R_{ac}}_{\text{축적계수}}=\frac{1}{1-2^{-3}}\approx1.14
$$

### Q7. 같은 일일 용량을 q24h에서 q8h로 바꾸면 무엇이 변하는가?
**답**: 평균 입력률이 같으므로 **$C_{av,ss}$는 원칙적으로 같지만, peak-trough 변동은 줄어듭니다.** 단, 독성이 회복 시간/분할에 의존하면 결과가 달라질 수 있습니다 [R&T p.325; R&T pp.351–353].

### Q8. $C_{av,ss}=F\text{Dose}/(CL\tau)=1.44F\text{Dose}t_{1/2}/\tau$라고 쓴 문장을 교정하세요.
**답**: 앞 식은 농도, 뒤 식은 약물량입니다. 정확히는 $C_{av,ss}=F\text{Dose}/(CL\tau)$이고, $A_{av,ss}=1.44F\text{Dose}t_{1/2}/\tau$입니다. **1-구획에서만 $C_{av,ss}=A_{av,ss}/V$**입니다.

$$
\underbrace{C_{av,ss}}_{\text{평균농도}}=\frac{F\text{Dose}}{CL\tau}\quad\neq\quad \underbrace{A_{av,ss}}_{\text{평균량}}=\frac{1.44F\text{Dose}t_{1/2}}{\tau}
$$

### Q9. Phenobarbital 100 mg q24h, $t_{1/2}=4$ days에서 R&T의 5.8과 식의 6.3을 어떻게 설명할 것인가?
**답**: 5.8은 $A_{av,ss}/Dose\approx5.76$에 해당하는 **평균 축적 비율**이고, peak/trough 축적 지수 $R_{ac}$는 Eq. 11-10 기준 약 6.3입니다. 둘을 같은 라벨로 쓰면 안 됩니다 [R&T pp.324–326].

### Q10. Atorvastatin에서 PK plateau와 PD plateau가 다를 수 있는 이유는?
**답**: 혈장 농도의 반감기와 cholesterol turnover 반응의 시간척도가 다르기 때문입니다. Atorvastatin은 $t_{1/2}\approx14$ h이지만 최대 cholesterol 반응은 3–4주가 걸릴 수 있습니다 [R&T p.343].

### Q11. Daptomycin Study A에서 "같은 일일 용량" 비교군은 무엇인가?
**답**: **75 mg/kg q24h와 25 mg/kg q8h**입니다. 둘 다 75 mg/kg/day이며, CPK는 991 vs 3996 U/L로 달랐습니다 [R&T pp.351–353].

### Q12. TW 알고리즘에서 $C_{upper}/C_{lower}$ ratio가 주로 결정하는 것은?
**답**: **허용 가능한 투여간격의 상한**입니다. $\tau_{max}=1.44t_{1/2}\ln(C_{upper}/C_{lower})$ [R&T p.334].

---

## §7-보스 딜레마(Boss Dilemma)

### Q-BD. 새로운 경구 약물이 선형 PK를 보이고, $F=0.6$, $V=100$ L, $t_{1/2}=4$ h이며, 제안된 치료역이 1–4 mg/L라고 가정합니다. Phase 1 MAD 프로토콜을 IRB에 제출하기 위해 두 regimen이 검토 중입니다.

**Regimen A — 안정적 목표 유지(Steady aim)**:
$200$ mg q8h, **부하용량 없음**.
- 장점: $\tau=8$ h에서 $C_{max,ss}/C_{min,ss}$ 변동이 비교적 좁아 peak이 $C_{upper}=4$ mg/L를 안정적으로 유지(peak safety 우선).
- 단점: plateau 도달까지 약 $3\text{–}4\times t_{1/2}=12\text{–}16$ h 동안 $C_{lower}=1$ mg/L 미달 구간 존재 — 초기 약 1 투여간격 동안 환자가 "효과 sub-window" 상태에 놓입니다.

**Regimen B — 빠른 도달 후 유지(Hit and hold)**:
$400$ mg loading + $200$ mg q8h maintenance.
- 장점: 첫 dose 직후 농도가 즉시 window 중앙 근처 — 효과 발현이 plateau 대기 시간 없이 시작(time-to-effect 우선).
- 단점: $D_L=400$ mg 직후 $C_{max}$ 추정치는 $F\cdot D_L/V=0.6\times400/100=2.4$ mg/L로 $C_{upper}=4$ 이내지만, **상부 95% CI**가 IIV 30%만 가정해도 $C_{upper}$를 일시적으로 침범할 수 있습니다.

Phase 1 프로토콜에서 어느 쪽을 채택하고, IRB 또는 FDA pre-IND 응답에서 그 선택을 어떻게 방어할 것인지 판단하세요. **이 문제는 가상 연습 문제임을 명시해야 합니다.**

**정답 — 거장의 상충 판단(Trade-off) 논리**:

이 문제는 단순 계산이 아니라 **두 충돌하는 최적화 목표** 사이의 양자택일입니다:
- **목표 X (peak safety)**: $C_{max}$가 $C_{upper}$를 절대 초과하지 않게 함.
- **목표 Y (time to effect)**: 효과 sub-window 노출 시간을 최소화함.

1. **사례 명시**: 이 문제는 교과서 등재 약물이 아닌 **가상 연습 문제**이며, 실제 Phase 1 프로토콜은 IIV·sample size·sparse sampling design을 동반한 model-based simulation으로 결정됩니다.

2. **$\tau_{max}$ 타당성 점검**: $\tau_{max}=1.44\times4\times\ln(4/1)\approx7.98$ h. 즉 q8h는 TW 알고리즘이 허용하는 **이론적 상한**에 정확히 맞춰진 interval입니다. q12h는 window를 벗어납니다 [R&T p.334]. 따라서 두 regimen 모두 q8h 채택은 정당합니다.

$$
\underbrace{\tau_{max}}_{\text{최대간격}}=1.44\times\underbrace{4}_{t_{1/2}}\times\underbrace{\ln(4/1)}_{\text{TW 비}}\approx7.98\ \mathrm{h}
$$

3. **선택 — Regimen A를 원칙적 1차 선택으로 권고**:
   - **이유 ①** (Phase 1 특수성): Phase 1 first-time-in-multiple-dose는 IIV가 아직 정량화되지 않은 상태입니다. Regimen B의 peak이 IIV 가정에 따라 $C_{upper}$를 침범할 가능성이 있다면, **peak-safety가 time-to-effect보다 불확실성 우선순위에서 위**에 있습니다.
   - **이유 ②** (M9 PD-driven plateau 가능성): 효과 plateau가 PK plateau가 아닌 turnover 시스템에 종속되는 약물이라면, 부하용량으로 PK plateau에 빨리 도달해도 **효과 발현은 빨라지지 않습니다** — Regimen B의 실익이 사라집니다.
   - **이유 ③** (M5 flip-flop 가능성): Phase 1 단계에서 $K_a<K$ 가능성이 배제되지 않았다면, observed $t_{1/2}=4$ h가 elimination이 아닐 수 있어 부하용량 산정의 전제가 무너집니다.

4. **Regimen B를 1차 선택으로 정당화하려면**:
   - 활성 대사체 없음, PD-driven plateau 부재, $K_a>K$ 확인이 in vitro/in silico로 사전 확보되어야 합니다.
   - IIV 추정치(또는 사전 분포)가 $C_{upper}$ 침범 위험을 받아들일 수 있는 수준임을 시뮬레이션으로 보여주어야 합니다.
   - 효과 발현 지연이 임상적으로 수용 불가능한 적응증(급성 항생제 등)일 때 정당화하기 쉽습니다.

5. **IRB 응답 프레임**: 어느 쪽을 선택하든, 응답 문서는 **"우리는 X와 Y 중 X(또는 Y)를 우선시했습니다. 그 이유는 [Phase 1 단계의 IIV 미정량성 / 적응증의 효과 발현 임상 중요도]입니다"**라는 trade-off 논리를 명시해야 합니다. "이 regimen이 안전하다"는 단정은 두 목표를 동시에 만족시킬 수 있다는 잘못된 함의를 줍니다.

6. **알고리즘 적용 중단 조건**: 선형 PK 비성립, 즉각적 농도-반응 깨짐, PD plateau가 turnover 지배, flip-flop, 단회 투여 치료 — 이 중 하나라도 의심되면 TW 알고리즘은 타당성 점검에 그치고 모델 확장으로 돌아갑니다.

**§7 요약**: 계산 문제의 핵심은 숫자를 넣는 것이 아니라 **"어떤 식이 어떤 조건에서만 유효한가"**를 먼저 잠그는 것입니다.

---

<!-- SLIDE_START: §8 | title: §8 — 메타프레임 & 전체 그림 -->
# §8 — 메타프레임 & 전체 그림

## §8A — 위치 설정

Session 07은 pharmacometrics의 **"steady-state grammar"**를 만듭니다. 이전 세션의 단회 투여 PK는 시간-농도 곡선의 기본 모양을 제공합니다. 이 세션은 그 곡선을 **반복·유지·제약하는 법**을 제공합니다. 이후 TDM, PopPK 공변량 해석, 노출-반응, Phase 1 MAD 설계는 모두 이 문법 위에 올라갑니다.

---

## §8B — 의존성과 실패 모드

| 실패 모드 | 원인 | 결과 |
|---|---|---|
| 초기 자료에 `SS=1` 적용 | plateau 시간 조건 무시 | CL/F, V/F, ETA 추정 왜곡 |
| $A_{av,ss}$를 $C_{av,ss}$로 표기 | 약물량/농도 차원 혼합 | 용량 근거 오류 |
| dose 크기로 축적 비율 설명 | $R_{ac}$의 dose 독립성 미이해 | regimen 변경 효과 오판 |
| terminal half-life를 elimination으로 고정 | flip-flop 미인식 | 제형/흡수 해석 오류 |
| TW와 TI 혼용 | 농도 경계와 안전 민감도 혼동 | 용량 근거 불명확 |
| PD plateau를 PK plateau로 가정 | turnover/세포 수명 무시 | 효과 발현/지속시간 예측 실패 |
| $C_{max}$ 또는 AUC 단일 변수로 독성 설명 | 분할/회복 시간 무시 | regimen 선택 오류 |

---

## §8C — 전문가 해자(Professional Moat)

전문가의 해자는 복잡한 식을 많이 외우는 데 있지 않습니다. **같은 regimen 질문을 다음 결정자 표로 즉시 분해**하는 데 있습니다.

| 질문 | 결정자 | 대표 사용처 |
|---|---|---|
| 목표 평균 농도는? | $CL$, 평균 입력률 | 유지용량, TDM |
| 목표에 얼마나 빨리 도달하나? | $t_{1/2}$ | washout, Day-to-SS, sampling 일정 |
| peak-trough 진폭은? | $\tau/t_{1/2}$ | 투여간격, 순응도, 독성 |
| loading이 필요한가? | target onset, $V/F$, $R_{ac}$ | urgent therapy, bolus+infusion |
| TW 안에 머무르는가? | $C_{upper}$, $C_{lower}$, $V/F$, $t_{1/2}$ | 투여 설계 |
| 효과가 늦게 오나? | turnover/세포 수명 | statin, EPO, 간접 반응 |
| 제형이 terminal slope를 바꾸나? | absorption/input duration | MR/depot/flip-flop |
| 독성이 회복 시간에 의존하나? | 분할, 최소 노출 지속시간 | daptomycin류 |

> 💼 **실무 인사이트**: 이 표는 규제 제출 문장을 대신 쓰는 것이 아니라, 교과서 수식을 제출 가능한 정량 논리로 번역하기 위한 **내부 검토 틀**입니다.

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| 목표 평균 농도 변화 | $CL$, 평균 입력률 | → | 유지용량 변경 | $R_{in}$ 또는 $D_M/\tau$ 재계산 |
| 도달 시간 지연 | $t_{1/2}$ | → | sampling·washout 일정 변경 | 3–4 half-lives 기준 확인 |
| peak-trough 진폭 과다 | $\tau/t_{1/2}$ | → | 독성 또는 trough failure | 투여간격 재설계 |
| 효과 plateau 지연 | turnover/세포 수명 | → | 효과 평가 시점 오류 | PD endpoint timing 분리 |

---

## §8D — 28세션 항법

이 세션이 잠그는 것은 네 가지입니다.

| 후속 세션 | 이 세션에서 열리는 개념 | 이 세션 없으면 실패하는 것 |
|---|---|---|
| TDM | $C_{ss}=R_{in}/CL$와 $C_{av,ss}$ | 농도 보정에서 $CL$·입력률·sampling time 혼동 |
| PopPK 공변량 해석 | $CL$, $V$, $t_{1/2}$, $\tau/t_{1/2}$ 분리 | 공변량 효과를 level·timing·fluctuation에 잘못 연결 |
| 노출-반응 | TW, PD plateau, turnover clock | PK plateau를 효과 plateau로 오독 |
| Phase 1 MAD 설계 | 축적, 부하/유지, 분할 | `SS=1`, interval, 독성 회복 판단 실패 |

다음 세션으로 넘어갈 때 이 문장을 유지하면 됩니다.

> **"항정상태는 하나의 숫자가 아니라, 시간 · 수준 · 진폭 · 임상제약을 분리해 다시 조립하는 작업입니다."**

---

## 출력 후 자가검증 체크리스트

| 항목 | 기준 | 결과 |
|---|---|---|
| SLIDE_START 개수 | §섹션수 + 카드수 합산 | 15 개 |
| 카드당 callout 합계 ≤ 6 | 전체 카드 | ✓ |
| [E] 박스 존재 | 모든 §2 카드 | ✓ |
| [D] 거장의 시각 존재 | 모든 §2 카드 | ✓ |
| [L] 파라미터 표 존재 | Apex 카드 + 정의 수식 카드 | ✓ |
| §5 혼동 쌍 표 행 순서 고정 (4행) | §5 전체 | ✓ |
| 기호 일관성 | 첫 등장 기준 통일 | ✓ |
| PART B 흔적 없음 | 전체 | ✓ |
| 수치 anchor 보존 | Compound A 등 원본 수치 | ✓ |
| [M] 나비효과 이중 종착점 | Apex 카드 전체 | ✓ |

---

<!-- v3.8 변환 노트
- 활자량: v3.7 1312줄 → v3.8 1074줄 (줄 수 기준 18% 감축, 바이트 기준 15.8% 감축)
- 보존 감사 결과:
  - SLIDE_START 마커 16건 (v3.7 일치)
  - 수식 블록 35개 unique / 70개 $$ 라인 (v3.7 일치, 중복 0건)
  - 출처 anchor 52종 고유 / 71회 등장 (v3.7 일치, 누락 0건)
  - 핵심 약물명 보존: phenobarbital 5, atorvastatin 6, daptomycin 10, EPO 10, erythropoietin 3, morphine 2, leuprolide 2, doxycycline 1, sirolimus 1, clobazam 2, eptifibatide 1
  - 핵심 수치 보존: 991/3996 (daptomycin CPK), 5.8/6.3 (phenobarbital 축적), 14 h / 3-4주 (atorvastatin), 9 h / 70일 (EPO), 75 mg/kg (daptomycin), 1.44 시간상수
- 주요 변환:
  - 메타 문구 완전 제거: §1.5 정독 경로 A/B/C/D 분기 전체, "확인 시점" 라인, [EXPERT_INFERENCE] 태그, 카드 위치 메모, "본 카드는 ver1에서…" 컴파일러 주석, byte-level/Content Lock 안내 — 모두 0건
  - §1.5를 5카드 빠른 읽기(M1→M2→M4→M5→M14) 한 박스로 축약
  - 자기참조("Mn의 결론이 ~한다") 인라인 해소
  - 약물명 첫 등장에 약물군 분류 인라인: daptomycin(cyclic lipopeptide 항생제), atorvastatin(HMG-CoA 환원효소 억제제), erythropoietin(EPO 적혈구 생성 자극인자), morphine MR, leuprolide depot(GnRH 효현제), sirolimus(mTOR 억제제 면역억제제), eptifibatide(GP IIb/IIIa 억제제), nitrate/nicotine/nifedipine(혈관확장제·중추신경 작용제·CCB) 등
  - 콜아웃 단일화: 한 블록에 💡+⚠️ 중복 제거, 카드당 콜아웃 ≤ 6개
  - 시각화 우선: 줄글 3개 이상 분류는 표/박스로 전환
- 미달 사항:
  - 컴파일러 권고 활자량 감축 목표 40-55%는 미충족 (실제 15.8-18%)
  - 사유: v3.7 PART A가 이미 컨텐츠 밀도가 높았고, 사용자 우선순위(보존 > 압축)를 준수한 결과. 약물 예시 즉맥락화(§7)와 비유 박스 유지가 추가 활자량을 가져옴
  - 보존 손실 0건이라는 점에서 §15 SCOPE BOUNDARIES("v3.8은 v3.7과 같은 강의입니다") 원칙에 부합
-->

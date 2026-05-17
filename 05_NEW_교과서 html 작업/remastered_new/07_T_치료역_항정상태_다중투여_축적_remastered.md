# 세션 07 — 다중투여·축적·항정상태: $\tau/t_{1/2}$, $C_{av,ss}$, accumulation — Remastered

## 0. 이 챕터의 cheat-code — 한 줄 척추

이 챕터 전체를 관통하는 한 줄을 먼저 박아두고 시작함. **"항정상태(steady-state)는 한 개의 숫자가 아니라 세 개의 자(rulers)임."**

- **시계** (언제 도달함?) → $t_{1/2}$
- **무게중심** (평균 수준은?) → $CL$과 평균 입력률
- **출렁임** (얼마나 흔들리고 얼마나 쌓임?) → $\tau/t_{1/2}$

이 세 자를 손에 들고 가면 챕터 끝까지 길을 안 잃음. 반대로 이걸 못 잡으면 phenobarbital trough도, daptomycin의 4배 독성도, NONMEM `SS=1` 플래그도, TDM 보정도, 부하용량 근거도 전부 같은 진흙탕에서 헤맴.

이게 이 챕터의 cheat-code임. 그럼 왜 이 자(ruler)들을 따로 분리해야 하는지, 두 임상 장면부터 보자.

---

## 1. 왜 이 챕터를 따로 떼서 다뤄야 함? — 두 임상 미스터리

### 장면 1. Phenobarbital trough

**Phenobarbital**(장기 항경련제) 100 mg q24h, $t_{1/2}=4$ days인 환자. 어느 날 trough가 높게 잡힘. 후배 약사가 보고하길 *"아직 plateau 도달 안 해서 그런 거예요."*

이 한 마디가 왜 위험한가?

**같은 단어가 두 개의 다른 질문에 동시에 답을 주고 있어서임.** trough가 높다는 건 **축적**의 결과($R_{ac}$가 크다 = $\tau/t_{1/2}$가 작다)이고, plateau에 도달했냐는 건 **시간**의 문제임($t_{1/2}=4$일이니까 90% 도달까진 12~16일). 두 자가 다름. 그런데 후배는 두 자를 한 자처럼 섞어서 "도달 안 해서 trough가 높다"라고 한 거임. 

→ 이 진단을 그대로 받으면 $\tau$ 조정 방향이 거꾸로 가고, NONMEM에 `SS=1`을 잘못 꽂아서 $CL/F$·$V/F$·ETA 추정이 다 무너짐 [R&T 5e pp.324–326].

### 장면 2. Daptomycin 4배 독성

**Daptomycin**(MRSA 같은 그람양성균에 쓰는 cyclic lipopeptide 항생제) 동물 실험에서 75 mg/kg/day로 **일일 총용량을 똑같이 맞춤**. 그런데 한 번에 줄 때(q24h)와 8시간마다 나눠 줄 때(q8h)의 근육독성 지표(CPK)가 **991 vs 3996 U/L**. 거의 **4배 차이**가 남.

→ 같은 일일 용량이 같은 독성을 보장하지 않음. 이게 "총량으로 독성을 예측한다"는 흔한 직관이 깨지는 자리임 [R&T 5e pp.351–353].

> ⚠️ **임상 용량 혼동 주의**: 위 75 mg/kg/day는 **임상 daptomycin 용량이 아니라** dose fractionation toxicity를 분리해서 보기 위한 **실험적(개 모델) design dose**임 [R&T 5e pp.351–353, Oleson et al. 2000 *Antimicrob Agents Chemother* 44:2948–2953 인용]. **임상 daptomycin 용량은 4–6 mg/kg/day**(복잡성 균혈증·심내막증에서 8–12 mg/kg/day까지)로 한 자릿수 mg/kg 영역임. 살아남는 교훈은 **"같은 daily dose ≠ 같은 toxicity"** 한 줄이고, 임상 적용 시 dose 수준은 완전히 다른 척도에서 결정됨.

### 두 장면의 공통 뿌리

두 장면은 같은 뿌리에서 옴 — **"항정상태"라는 한 단어 안에 사실은 세 개의 다른 질문이 들어있는데, 그중 어떤 자(ruler)를 묻고 있는지 분리 안 하면 임상 판단이 어긋남.**

| 질문 | 자(ruler) | 답을 정하는 파라미터 |
|---|---|---|
| **언제** 거기에 도달함? | 시계 | $t_{1/2}$ |
| 평균 **수준**은 어디임? | 무게중심 | $CL$, 평균 입력률 |
| 얼마나 **출렁이고/쌓임?** | 출렁임 / 배율 | $\tau/t_{1/2}$ |

이 세 자를 분리하는 게 이 챕터의 척추임. 그래서 이 세션은 **"항정상태를 세 개의 자로 분해해서 다시 조립하는 법"**을 다루는 것임.

---

## 2. 큐레이션 맵(Curation Map) — 무엇이 MUST이고 무엇이 CONTEXT인가

### MUST — 10분 핸드아웃에 반드시 남길 개념

| ID | 개념 | 한 문장 결론 | 핵심 수식 / 앵커 | §2 카드 | 출처 |
|---|---|---|---|---|---|
| M1 | 정속 주입 plateau 농도 | plateau **높이**를 정하는 건 $t_{1/2}$가 아니라 $CL$임 (단위시간당 제거되는 용적). | $C_{ss}=R_{in}/CL$ | §2-M1 | [G&W 5e p.23; R&T 5e p.288] |
| M2 | plateau 도달 시간 | 목표가 높든 낮든, 거기까지 가는 **시간표**는 반감기로만 정해짐. | $C(t)=C_{ss}(1-e^{-Kt})$; 1·2·3·3–4 half-lives에서 50%, 75%, 87.5%, $\approx90\%$ | §2-M2 | [G&W 5e pp.22–23; R&T 5e pp.290–292] |
| M3 | 다중투여 축적계수 | 축적은 **dose 크기**가 아니라 **$\tau/t_{1/2}$**가 정함. | $R_{ac}=1/(1-e^{-K\tau})=1/(1-2^{-\tau/t_{1/2}})$ | §2-M3 (Apex) | [G&W 5e pp.43–45; R&T 5e pp.322–326; R&T 5e pp.795–797 Appendix I] |
| M4 | 평균 plateau: 농도 vs 약물량 | $C_{av,ss}$와 $A_{av,ss}$를 같다고 쓰면 **단위가 무너짐** — 농도는 $CL$이, 약물량은 $MRT$가 답함. | $C_{av,ss}=F\text{Dose}/(CL\tau)$; $A_{av,ss}=1.44F\text{Dose}t_{1/2}/\tau$; 1-구획에서만 $C_{av,ss}=A_{av,ss}/V$ | §2-M4 | [G&W 5e p.45; R&T 5e p.324; R&T 5e p.337] |
| M5 | Flip-flop | terminal slope가 elimination이 아니라 **흡수**를 말할 수 있음. | $K_a<K$이면 terminal slope $\approx K_a$ | §2-M5 | [G&W 5e pp.45–46; R&T 5e pp.332–334, 337–338] |
| M6 | 치료역 (Therapeutic Window) | TW는 "좋은 농도 범위"가 아니라 효과와 위해의 균형을 농도 축에 그어놓은 **의사결정 구간**임. | TW와 therapeutic concentration range 구별; TI는 전임상 ratio와 임상 노출 민감도가 다름 | §2-M6 | [R&T 5e pp.267–281] |
| M7 | 부하 + 유지 용량 | 부하용량은 **시작점**을, 유지용량은 **평균 입력률**을 정함. | $D_M=D_L(1-e^{-K\tau})$; $D_L=R_{ac}D_M$; bolus+주입 앵커 | §2-M7 | [R&T 5e pp.293–295; R&T 5e pp.326–329; G&W 5e pp.537–539] |
| M8 | 치료역 기반 투여 설계 | $C_{upper}$, $C_{lower}$, $t_{1/2}$, $V$, $F$만 있으면 **투여간격과 용량 상한**이 계산됨. | $\tau_{max}=1.44t_{1/2}\ln(C_{upper}/C_{lower})$; $D_{M,max}=(V/F)(C_{upper}-C_{lower})$ | §2-M8 | [R&T 5e pp.334–337] |
| M9 | PD 기반 plateau | 효과 plateau는 약물 plateau보다 늦을 수 있음 — **"무엇의 반감기인지"** 먼저 물어야 함. | atorvastatin: PK $t_{1/2}=14$ h, PD plateau 3–4주; erythropoietin: PK $t_{1/2}=9$ h, hematocrit plateau $\approx70$일 | §2-M9 + §2-M6 PK/PD clocks | [R&T 5e pp.341–345] |
| M10 | 용량분할 독성 | 같은 일일 용량이라도 분할이 **회복 시간**을 어그러뜨리면 독성이 달라짐. | Daptomycin Study A: 75 mg/kg q24h vs 25 mg/kg q8h, CPK 991 vs 3996 U/L | §2-M10 + §2-M7 daptomycin anchor | [R&T 5e pp.351–353] |

큐레이션 맵의 핵심 세 식을 한 묶음으로 잡고 가자. **높이·배율·무게중심** 세 단어가 이 챕터의 모든 카드 라벨임:

$$
\begin{aligned}
\overbrace{\underbrace{C_{ss}}_{\text{plateau}}}^{\text{높이}}&=\underbrace{R_{in}/CL}_{\text{입력/CL}}\\
\overbrace{\underbrace{R_{ac}}_{\text{축적계수}}}^{\text{배율}}&=\frac{1}{1-e^{-K\tau}}\\
\overbrace{\underbrace{C_{av,ss}}_{\text{평균농도}}}^{\text{무게중심}}&=\frac{F\cdot Dose}{CL\cdot\tau}
\end{aligned}
$$

### CONTEXT — 유지하되 확장하지 않을 항목

| ID | 항목 | 짧게 짚는 한 줄 | 출처 |
|---|---|---|---|
| C1 | 항정상태 vs 열역학적 평형 | 용어만 구분 — 별도 카드로 확장하지 않음 | [G&W 5e p.25] |
| C2 | 입력 함수 분류 | bolus/zero-order/first-order/multiple input — "입력이 바뀌면 곡선이 바뀐다" 수준만 | [G&W 5e p.43] |
| C3 | 다중 흡수 부위 | multiple peaks를 곧바로 enterohepatic recirculation으로 읽지 말 것 | [G&W 5e p.46] |
| C4 | PK11 | PK clock과 PD clock의 단순 anchor로만 사용 | [G&W 5e pp.528–531] |
| C5 | PK13 | bolus+infusion 초기조건 코딩 anchor로 사용 | [G&W 5e pp.537–539] |
| C6 | 정속 장치(constant-rate devices) | infusion 원리의 확장 예시로만 | [R&T 5e pp.284–286] |
| C7 | 주입 후 감소(post-infusion decline) | infusion 중단 후 농도는 half-life로 감소하되, 경구 등 input이 계속되면 예외 | [R&T 5e p.291] |
| C8 | Clobazam 단회투여 AUC | single-dose AUC로 plateau 평균을 예측할 수 있다는 한 줄 anchor | [R&T 5e p.336] |
| C9 | 방출 조절(modified release) | 의도적 flip-flop의 임상 활용 — morphine MR, leuprolide depot만 짧게 | [R&T 5e pp.337–338] |
| C10 | 투여법 평가 | fluctuation, relative bioavailability, renal clearance는 평가 맥락으로만 | [R&T 5e pp.339–341] |
| C11 | DDI 패턴 | 추출률 기준 4패턴만 — protein binding 단독 논리는 금지 | [R&T 5e pp.309–310; R&T 5e pp.350–351] |
| C12 | 연습 문제 | 본문 통합 금지 — §7 가상/응용 문항으로만 사용 가능 | [R&T 5e pp.353–358] |

---

<!-- SLIDE_START: §1 | title: §1 — 세션 헤더 & 로드맵 -->
<!-- SECTION_CORE: SC-01 -->
# §1 — 세션 헤더 & 로드맵

## 1A. 척추 한 번 더 — 세 개의 자(rulers)를 한 그림으로

큐레이션 맵의 척추를 그림 한 장으로 압축함. 임상가가 "항정상태"라는 단어를 입에 올릴 때 사실은 **세 질문이 동시에** 들어오는 거임:

$$
\overbrace{\underbrace{\text{Timing}}_{t_{1/2}}}^{\text{언제}}\;+\;\overbrace{\underbrace{\text{Level}}_{CL,\;R_{in}}}^{\text{얼마나 높이}}\;+\;\overbrace{\underbrace{\text{Amplitude}}_{\tau/t_{1/2}}}^{\text{얼마나 출렁이게}}
$$

이 세 축을 손에 들고 있으면, NONMEM의 `SS=1`이랑 `ADDL/II`, 부하용량과 유지용량, 치료역 기반 투여 설계가 전부 **같은 문법** 위에서 읽힘. 반대로 세 축을 한 번이라도 섞기 시작하면 — 예를 들어 *"축적이 크니까 도달이 늦다"*라고 한 마디 하는 순간 — TDM 조정, NONMEM 코딩, 부하용량 근거가 동시에 흐려짐.

R&T 5e Fig. 11-3을 보면 같은 평균 투여율에서도 투여간격이 길어질수록 변동이 어떻게 커지는지 시각적으로 잡힘 [R&T 5e p.325].

> 💡 **세션의 한 줄**: 항정상태는 **시간 · 수준 · 진폭** 세 축으로 잠금. 이 분리 하나가 이 챕터 전체의 척추임.

## 1B. 지식 그래프 위치

```text
[선행: single-dose PK, CL·V·t1/2, oral absorption]
   → [이 세션: steady-state 문법, 축적, 치료역 기반 regimen 설계]
   → [후속: TDM, PopPK 공변량 해석, exposure-response, Phase 1 MAD 설계]
```

## 1C. 카드 흐름 — 세 묶음으로 보는 10장의 카드

이 챕터는 카드 10장으로 구성되는데, 묶음을 세 개로 나누면 흐름이 보임:

| 묶음 | 카드 | 답하는 큰 질문 |
|---|---|---|
| **묶음 ① PK 시계(PK clock)** | M1–M5 | 약물 쪽 시간 구조 — 언제 도달, 얼마나 축적, 농도/약물량 분리, flip-flop |
| **묶음 ② 설계 다리(dosing-design bridge)** | M6–M8 | PK 시계를 임상 투여 설계로 옮김 — loading/maintenance, TW 알고리즘 |
| **묶음 ③ PD/안전성 시계(PD/safety clock)** | M9–M10 | 환자 쪽 시간 — 약물 시계와 다를 수 있는 효과 시계, 분할 독성 |

🧭 **카드별 핵심 한 줄 질문**
- **M1**: 정속 주입 plateau의 **높이**는 누가 정함?
- **M2**: 그 plateau에 **언제** 도달함?
- **M3 [⚡Apex]**: 반복투여에서 **축적**은 왜 dose가 아니라 interval의 문제임?
- **M4**: 평균농도와 평균량은 **왜 같은 평균이 아님?**
- **M5**: terminal slope는 언제 **elimination이 아니라 흡수**를 말함?
- **M6**: PK 식은 언제 **치료역**이라는 임상 제약으로 바뀜?
- **M7**: 부하용량과 유지용량은 각각 **어떤 질문에 답함?**
- **M8**: 치료역만 알면 **interval과 dose 상한**을 어떻게 계산함?
- **M9**: 효과 plateau는 왜 **drug half-life만으로 예측이 안 됨?**
- **M10**: 같은 daily dose가 왜 **같은 독성을 보장 안 함?**

각 카드는 위 세 묶음 중 어딘가에 속하면서 **자기가 어느 자(ruler)를 잠그고 있는지**를 라벨로 들고 다닐 거임. 카드를 다 읽고 나면 §5에서 혼동쌍, §7에서 자기테스트, §8에서 메타프레임으로 마무리함.

---

<!-- SLIDE_START: §2 | title: §2 — 개념 해부 카드(Concept Anatomy Cards) -->
<!-- SECTION_CORE: SC-02 -->
# §2 — 개념 해부 카드(Concept Anatomy Cards)

이제 10장의 카드를 묶음별로 펴자. 카드마다 **(1) 어느 자를 잠그는가** → **(2) 식과 의미** → **(3) 임상 anchor** → **(4) 어디서 자주 틀리는가** 순으로 감.

---

## 묶음 ① — PK 시계(PK clock): 약물 쪽 시간 구조 (M1–M5)

<!-- SLIDE_START: M1 | title: §2-M1. 정속 주입 항정상태 농도: $C_{ss}=R_{in}/CL$ -->
<!-- SECTION_CORE: SC-03 -->
## §2-M1. 정속 주입 plateau 농도 — **누가 높이를 정함?** ($C_{ss}=R_{in}/CL$)

### 잠그는 자: **무게중심(level)**

여기서 잠그는 건 plateau의 **높이**임. 시간이 아님, 진폭도 아님. "주입을 켜놓고 무한히 기다리면 농도는 어디서 멈추는가" — 이 질문 하나에만 답하는 카드임.

**한 줄 cheat**: plateau 농도를 dose나 volume으로 설명하려고 하면 입력률 오류랑 청소율 변화를 같은 원인처럼 섞게 됨. **유지 투여의 첫 질문은 단 하나 — "얼마나 넣고, 얼마나 지움?"** 이게 끝임.

### A. 정의와 수식

농도 변화는 유입과 유출의 차이임:

$$
\underbrace{\frac{dC}{dt}}_{\text{농도 변화}}=\overbrace{\underbrace{\frac{R_{in}}{V}}_{\text{입력/V}}}^{\text{유입}}-\overbrace{\underbrace{\frac{CL}{V}C}_{\text{제거/V}}}^{\text{유출}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $C_{ss}$ | 농도 | 정속 주입 plateau 농도 | $R_{in}$ 증가 시 ↑, $CL$ 증가 시 ↓ |
| $R_{in}$ | dose/time | 단위시간당 입력률 | 주입속도·라인 중단·처방 변경 |
| $CL$ | volume/time | 단위시간당 제거되는 용적 | 신기능·간기능·DDI·질병 상태 |
| $V$ | volume | 농도 상승의 시간상수에 관여하는 분포 용적 | 체성분·단백결합·조직분포 |

미분방정식을 풀면 시간 곡선이 나옴:

$$
\underbrace{C(t)}_{\text{t시점 농도}}=\overbrace{\underbrace{\frac{R_{in}}{CL}}_{\text{plateau}}}^{C_{ss}}\;\underbrace{\left(1-e^{-(CL/V)t}\right)}_{\text{접근분율}}
$$

이 식의 핵심 두 조각만 떼어 보면:

$$
\underbrace{C_{ss}}_{\text{SS 농도}}=\frac{\overbrace{\underbrace{R_{in}}_{\text{입력률}}}^{\text{단위시간당 들어오는 양}}}{\overbrace{\underbrace{CL}_{\text{청소율}}}^{\text{단위시간당 지워지는 용적}}}
$$

> 💡 **수준이랑 시간은 다른 질문임.** $C_{ss}$의 **높이**는 $CL$과 $R_{in}$의 균형에서 나옴. 그 높이까지 **언제 도달함**은 다음 카드 M2의 $t_{1/2}$ 문제임. $V$가 커지면 상승 곡선이 느려질 수는 있지만 plateau **높이를 직접 정하진 않음**.

### B. 비유 — 욕조 모델

수도꼭지(입력 $R_{in}$)를 일정하게 열어둔 욕조에 배수구($CL$)가 같이 열려있는 상황임. **마지막에 수위가 어디서 멈추는지**는 들어오는 물의 양과 배수구 크기의 균형으로 결정됨. 욕조 크기($V$)는 그 수위까지 도달하는 **속도**에는 영향을 주지만, 수위 자체의 **위치**를 정하진 않음.

### C. 실무 한 컷 — 유지 투여 시작할 때 첫 질문

유지 투여 시작할 때 약사가 첫 번째로 던져야 할 질문은 **"목표농도 × 청소율"**임. 목표 $C_{ss}$를 정하면 $R_{in}$을 거기에 맞춰 잡고, 환자의 $CL$이 바뀌면 그걸 즉시 반영해야 함. $V$는 loading이나 발현 시간 쪽으로 질문이 옮겨갈 때 등장함.

> ⚠️ **실무 함정 — "낮은 농도 = CL 증가"는 너무 빠른 점프**: 주입 중 농도가 기대 plateau보다 낮게 나왔다고 곧바로 "$CL$이 늘었네"로 점프하면 안 됨. **실제 입력률·라인 중단·sampling time·infusion stop/start 기록**부터 확인하는 게 순서임. 교과서가 보증하는 건 $C_{ss}=R_{in}/CL$이라는 **구조**이지, 현장 어디서 오류가 잘 나는지의 빈도가 아님.

### 한 줄 마무리

정속 주입에서 plateau **농도**의 지배자는 청소율. 그 농도에 **도달하는 시간**의 지배자는 반감기 (→ M2). 둘은 같은 자가 아님.

---

<!-- SLIDE_START: M2 | title: §2-M2. 항정상태 도달 시간: 3–4 $t_{1/2}$ 규칙 -->
<!-- SECTION_CORE: SC-04 -->
## §2-M2. 항정상태 도달 시간 — **누가 시계를 정함?** (3–4 $t_{1/2}$ 규칙)

### 잠그는 자: **시계(timing)**

M1에서 plateau의 **높이**를 $CL$과 $R_{in}$의 균형으로 잠갔음. 이제 같은 plateau에 **어느 속도로 접근하는지**를 분리함.

**한 줄 cheat**: *"plateau가 높으면 거기까지 가는 데 더 오래 걸리겠지"* — 이게 가장 흔한 직관적 오류임. **틀림.** 도달은 **비율**의 문제임, 목표 높이의 문제가 아님. 도달 시간표는 **$K$와 $t_{1/2}$만** 정함.

### A. 정의와 수식

도달 곡선을 두 조각으로 분해:

$$
\underbrace{C(t)}_{\text{t시점 농도}}=\overbrace{\underbrace{C_{ss}}_{\text{plateau}}}^{\text{높이(=결정됨)}}\;\overbrace{\underbrace{(1-e^{-Kt})}_{\text{도달률}}}^{\text{비율(시간만의 함수)}}
$$

핵심은 **높이($C_{ss}$)와 도달률($1-e^{-Kt}$)이 곱셈으로 분리**된다는 점임. 도달률은 시간만의 함수임. plateau 높이를 두 배로 올려도, 도달률 곡선의 모양은 똑같음.

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $C(t)$ | 농도 | 시간 $t$의 농도 | $C_{ss}$와 도달률에 의해 변화 |
| $C_{ss}$ | 농도 | 접근 대상 plateau | $R_{in}/CL$ |
| $K$ | 1/time | 소실 속도상수 | $CL/V$ 변화 |
| $t_{1/2}$ | time | 농도가 절반으로 감소하는 시간 | $K$ 감소 시 ↑ |
| $t_{90}$ | time | plateau 90% 접근 시간 | 약 $3.32t_{1/2}$ |

90% 도달까지의 시간 계산:

$$
\underbrace{1-e^{-Kt}}_{\text{도달률}},\qquad \underbrace{K}_{\text{소실 K}}=\frac{\ln 2}{\underbrace{t_{1/2}}_{\text{반감기}}},\qquad \overbrace{\underbrace{t_{90}}_{\text{90\% 도달}}}^{\approx\,3.32\,t_{1/2}}=\frac{\ln 10}{K}
$$

→ 그래서 실무에서 **"3–4 half-lives면 거의 도달"**이라는 규칙이 나옴 [R&T 5e p.291].

> 💡 **도달은 비율임.** 90% 도달은 절대 농도가 아니라 plateau에 대한 **접근 비율**임. 입력률을 올리면 plateau 자체가 올라가지만, **3–4 half-lives라는 시간표 자체는 그대로** 유지됨.

### B. 비유 — 엘리베이터

엘리베이터가 5층으로 가든 50층으로 가든, **"남은 거리의 절반을 줄이는 데 걸리는 시간"** 자체는 똑같다고 생각하면 됨. 목표가 더 멀어도 한 step에 줄어드는 비율은 같음. 즉 시간표는 목표와 무관함.

### C. 약물 예시 — 빠른 약, 느린 약

| 약물 | 분류 | $t_{1/2}$ | 90% 도달 시간 |
|---|---|---|---|
| **t-PA** | 혈전용해제 | 5 min | $\approx 17$ min |
| **Eptifibatide** | 항혈소판제 (GP IIb/IIIa 억제제) | 2.5 h | $\approx 8$ h |
| **Phenobarbital** | 장기 항경련제 | 4 days | $\approx 13$일 |

→ 그래서 hook의 phenobarbital이 plateau 도달에만 12~16일 걸린다는 사실이 여기서 정량적으로 잠금됨 [R&T 5e pp.288–293; R&T 5e pp.324–325].

### D. NONMEM 연결 — `SS=1` 플래그의 의미

`SS=1` 플래그는 **"이 환자가 평균적으로 충분히 오래 투여받았다"**는 **시간 조건**임. 쓰기 전에 실제 투여 이력이 **최소 3–4 half-lives 이상**인지 먼저 확인해야 함. 그 조건이 안 채워졌는데 `SS=1`을 꽂으면 — NONMEM이 상승 구간을 강제로 plateau라고 설명하게 됨 → $CL/F$, $V/F$, ETA 추정이 다 왜곡됨.

### 한 줄 마무리

목표 수준이 바뀌어도 접근 비율의 시간표는 반감기로만 움직임. *"dose 올리면 SS 도달도 빨라진다"*고 말하는 순간 level과 timing이 섞이고, `SS=1` 적용이 오판으로 감.

---

<!-- SLIDE_START: M3 | title: §2-M3. [⚡ Apex Concept] 다중투여 축적인자 $R_{ac}=1/(1-e^{-K\tau})$ -->
<!-- SECTION_CORE: SC-05 -->
## §2-M3. [⚡ Apex Concept] 다중투여 축적계수 — **왜 dose가 안 들어가는가?** ($R_{ac}=1/(1-e^{-K\tau})$)

### 잠그는 자: **출렁임/배율(amplitude/ratio)**

이 카드가 이 챕터의 **정점(Apex)**임. 가장 흔히 헷갈리고, 가장 자주 임상 판단을 거꾸로 돌리는 자리거든.

**한 줄 cheat**: trough가 자꾸 올라오면 임상가는 본능적으로 *"아직 plateau에 도달 안 했네"*라고 진단함. **이게 hook의 phenobarbital 미스터리의 정체임.** trough가 올라오는 건 **축적**의 결과($\tau/t_{1/2}$ 작음, $R_{ac}$ 큼)이고, 도달 여부는 **시간**의 문제임 (→ M2). **다른 자임.** 둘을 섞는 순간 처방 조정 방향이 뒤집힘.

### A. 정의와 수식 — dose가 안 보이는 식

$$
\overbrace{\underbrace{R_{ac}}_{\text{축적계수}}}^{\text{dose-free 배율}}=\frac{1}{1-\overbrace{\underbrace{e^{-K\tau}}_{\text{잔여분}}}^{\text{interval 끝 fraction}}}=\frac{1}{1-\underbrace{2^{-\tau/t_{1/2}}}_{\text{반감기 잔여}}}
$$

이 식에서 가장 먼저 봐야 할 건 **dose가 어디에도 안 보인다는 점**임. 선형 PK에서 dose를 두 배로 올리면 농도는 두 배로 올라가지만, 같은 $\tau/t_{1/2}$의 $R_{ac}$ 배율은 그대로임 [G&W 5e pp.44–45; R&T 5e pp.325–326].

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $R_{ac}$ | 무차원 | 반복투여가 만든 축적 배율 | $\tau/t_{1/2}$ 감소 시 ↑ |
| $K$ | 1/time | 잔여분 감소 속도 | $CL/V$ 변화 |
| $\tau$ | time | 투여간격 | regimen 설계 |
| $t_{1/2}$ | time | 잔여분을 반으로 줄이는 시간 | clearance·volume 변화 |

> 💡 **배율은 dose-free임.** $R_{ac}$를 키우려면 dose가 아니라 **$\tau$를 줄여야 함**. dose만 키우면 평균 수준만 올라가고 축적 비율 자체는 그대로임.

### B. 비유 — 저금통 배율

$R_{ac}$는 매번 남은 잔돈이 다음 입금에 더해지는 **저금통 배율**임. 입금액(=dose)이 커져도, 같은 주기로 같은 비율(=$\tau/t_{1/2}$)이 남으면 배율 자체는 안 바뀜. 저금통 안의 절대 금액은 커지지만, "다음 입금 직전에 얼마나 남아있는지의 비율"은 같음.

### C. 세 결정자 다시 정리 — 한 표로

| 질문 | 자(ruler) | 결정자 |
|---|---|---|
| **시간**: plateau 접근 시간 | 시계 | $t_{1/2}$ |
| **수준**: 평균 plateau 농도 | 무게중심 | $CL$과 평균 입력률 |
| **진폭/배율**: peak-trough fluctuation과 축적계수 | 출렁임 | $\tau/t_{1/2}$ |

R&T 5e Fig. 11-3의 200 mg/day 예시는 이 분리를 시각적으로 보여줌. 평균 투여율이 같으면 평균량의 접근 시간표는 같지만, **투여간격이 길어질수록 변동만 커짐** [R&T 5e p.325, Fig. 11-3].

### D. PTF — 출렁임을 숫자로 잠그기 (peak-trough fluctuation index)

$R_{ac}$가 "얼마나 쌓이는가"를 잠그면, 그 옆에 짝꿍 지표가 **"얼마나 출렁이는가"**를 잠금. 그게 PTF임. 같은 $C_{av,ss}$라도 $\tau/t_{1/2}$가 크면 환자가 경험하는 농도의 출렁임은 본질적으로 달라짐. R&T 5e Fig. 11-14에서 degree of fluctuation = $(C_{max,ss}-C_{min,ss})/C_{av,ss}$로 정의됨 [R&T 5e pp.339–341, Fig. 11-14].

$$
\overbrace{\underbrace{\mathrm{PTF\%}}_{\text{변동지수}}}^{\text{평균 대비 진폭}}=\overbrace{\frac{\overbrace{\underbrace{C_{max,ss}-C_{min,ss}}_{\text{진폭(peak-trough)}}}^{\text{출렁임 크기}}}{\underbrace{C_{av,ss}}_{\text{평균농도}}}}^{\text{비율}}\times 100
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $\mathrm{PTF\%}$ | % | 평균농도 대비 peak-trough 진폭 비율 | $\tau/t_{1/2}$ 증가 시 ↑ |
| $C_{max,ss}-C_{min,ss}$ | 농도 | 진폭(swing) | dose 크기, $\tau/t_{1/2}$ |
| $C_{av,ss}$ | 농도 | 간격 평균 농도 | $F\text{Dose}/(CL\tau)$ |

선형 1구획 IV bolus 다중투여에서 PTF는 **$\tau/t_{1/2}$만의 함수**로 환원됨. 정리하면:

$$
\overbrace{\underbrace{\mathrm{PTF}}_{\text{변동}}}^{\tau/t_{1/2}만의\;함수}=\frac{\overbrace{\underbrace{K\tau}_{=\ln 2\cdot\tau/t_{1/2}}}^{\text{interval / 반감기}}\cdot \underbrace{(1-e^{-K\tau})}_{\text{보충분율}}}{\underbrace{1-e^{-K\tau}}_{\text{누적분율}}}=\underbrace{K\tau}_{\ln 2\cdot \tau/t_{1/2}}
$$

> 💡 **PTF와 $R_{ac}$는 서로의 짝꿍임.** $\tau/t_{1/2}$가 줄어들면 $R_{ac}$는 올라가고 PTF는 내려감. 같은 평균을 유지하면서 변동을 줄이고 싶다면(예: 좁은 치료역) **$\tau$를 줄이고 dose를 비례적으로 줄여라**가 정량적 처방임. 반대로 dose만 키우면 평균은 올라가지만 PTF는 안 바뀜 [R&T 5e pp.339–341의 dose 분할 평가 맥락].

**임상 anchor 숫자**: $\tau/t_{1/2}=1$이면 PTF $\approx 69\%$, $\tau/t_{1/2}=2$면 PTF $\approx 139\%$, $\tau/t_{1/2}=0.5$면 PTF $\approx 35\%$. M4에서 만날 amoxicillin(짧은 $t_{1/2}$ → 큰 PTF) / naproxen / piroxicam(긴 $t_{1/2}$ → 작은 PTF) 비교가 정확히 이 라디칼임.

### E. Phenobarbital의 두 숫자 — 라벨 분리

여기서 hook의 phenobarbital을 다시 보자. **R&T 5e 본문**은 $t_{1/2}=4$ days, 100 mg q24h에서 축적 지수를 **5.8**로 적음. 그런데 같은 책의 **Eq. 11-3/11-10** peak/trough 기준으로 계산하면 $A_{max,ss}/Dose=630/100\approx$ **6.3**이 나옴. → 이 두 숫자는 **다른 라벨**임. 5.8은 평균 기준($A_{av,ss}/Dose\approx5.76$)의 축적이고, 6.3은 peak/trough 기준의 $R_{ac}$임 [R&T 5e pp.324–326].

$$
\overbrace{\underbrace{A_{av,ss}/Dose}_{\text{평균 기준}}}^{\approx 5.76}\qquad;\qquad\overbrace{\underbrace{A_{max,ss}/Dose}_{\text{peak/trough}}}^{\approx 6.3}
$$

두 숫자를 같은 라벨로 쓰면 보고서에서 방어 못 함. 항상 **"이 축적 숫자는 평균 기준이냐, peak 기준이냐"**를 명시해야 함.

### F. 그래서 hook의 trough — 다시 보기

이제 hook으로 돌아감. *"phenobarbital trough가 높다 → 아직 plateau 도달 안 해서"*라는 진단이 왜 위험한가? **두 가지가 섞여 있어서임.**

- **trough가 높다** = 축적의 결과 ($\tau/t_{1/2}=0.25$ → 매우 작음 → $R_{ac}$ 매우 큼)
- **plateau 도달 여부** = 시간의 문제 ($t_{1/2}=4$일 × 3~4 = 12~16일 경과했냐)

→ **두 질문임.** 이걸 섞어서 "도달 안 해서"라고 진단하면, $\tau$ 조정과 부하용량 전략을 같은 축으로 처리하게 되고, trough 초과 환자에서 interval을 어떻게 만질지 판단이 뒤집힘. 모델링·규제 쪽으로는 `SS=1` 부적절 적용, $CL$·bioavailability·IIV 추정 편향, steady-state 가정 재설명 요구로 이어짐.

> ⚠️ **실무 함정 — 유령 Plateau 편향**: 투여 시작 직후 자료에 `SS=1`을 잘못 적용하면 상승 구간을 plateau로 강제 설명하게 됨. 그러면 $CL$, bioavailability, IIV 추정이 연쇄적으로 왜곡됨.

> 📖 **R&T 5e, p.325, Fig. 11-3**: 같은 평균 투여율은 평균량 plateau로의 접근 시간을 같게 만들지만, 투여 빈도가 변동을 바꿈. → *"dose가 아니라 $\tau/t_{1/2}$가 축적과 변동을 정한다"*는 M3의 직관을 시각적으로 박아주는 그림임.

### 한 줄 마무리

축적인자는 **dose 독립, $\tau/t_{1/2}$ 의존**. dose를 키우면 수준만 올라가고 축적 비율은 그대로임. *"$R_{ac}$가 크면 도달도 늦다"*고 말하는 순간 배율과 시계가 섞이고, regimen 조정과 SS 코딩이 동시에 실패함.

---

<!-- SLIDE_START: M4 | title: §2-M4. 항정상태 평균농도와 평균 amount: $C_{av,ss}$ vs $A_{av,ss}$ -->
<!-- SECTION_CORE: SC-06 -->
## §2-M4. 항정상태 평균농도 vs 평균 약물량 — **왜 같은 평균이 아닌가?** ($C_{av,ss}$ vs $A_{av,ss}$)

### 잠그는 자: **무게중심(level)** — 다만 단위가 두 개

M3에서 반복투여의 배율을 잠갔음. 이번엔 항정상태에서 **평균 농도(mg/L)와 평균 약물량(mg)을 차원적으로 분리**하는 카드임. 한 줄로 — **단위 방화벽**을 세우는 카드임.

**한 줄 cheat**: $C_{av,ss}$와 $A_{av,ss}$를 둘 다 "평균 plateau"라고 묶어서 같은 줄에 쓰는 순간 mg/L와 mg가 섞임. **농도는 $CL$ 기반 노출 언어, 약물량은 $MRT$ 기반 체류 언어** — 두 언어를 분리하면 용량 공식이 어디에 들어가는지 자리가 잡힘.

### A. 정의와 수식 — 두 식, 두 단위

$$
\overbrace{\underbrace{C_{av,ss}}_{\text{평균농도}}}^{\text{mg/L}}=\frac{\overbrace{\underbrace{AUC_{0-\tau,ss}}_{\text{간격 AUC}}}^{\text{총 노출}}}{\underbrace{\tau}_{\text{투여간격}}}=\frac{\overbrace{\underbrace{F\cdot Dose}_{\text{유입량}}}^{\text{실제 흡수량}}}{\underbrace{CL\cdot\tau}_{\text{CL×간격}}}
$$

$$
\overbrace{\underbrace{A_{av,ss}}_{\text{평균량}}}^{\text{mg}}=\frac{\overbrace{\underbrace{1.44\cdot t_{1/2}}_{\text{MRT 근사}}}^{\text{체류시간}}\;\underbrace{F\cdot Dose}_{\text{유입량}}}{\underbrace{\tau}_{\text{투여간격}}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $C_{av,ss}$ | 농도 | 투여간격 평균 농도 | $F\cdot Dose$ ↑, $CL\cdot\tau$ ↑ |
| $AUC_{0-\tau,ss}$ | 농도×시간 | 간격 내 총 노출 | 입력량·청소율 변화 |
| $A_{av,ss}$ | amount | 체내 평균 약물량 | $t_{1/2}$·$F\cdot Dose$ 증가 시 ↑ |
| $MRT$ | time | 분자 평균 체류시간 | $V/CL$ 및 구획 구조 |
| $V$ | volume | amount를 concentration으로 잇는 다리 | 분포·단백결합·구획 가정 |

첫 식의 단위는 **농도(mg/L)**, 둘째 식의 단위는 **약물량(mg)**임. 두 식이 연결되려면 다리($V$)가 필요함. **1-구획에서 $MRT=V/CL=1.44t_{1/2}$가 성립할 때만** $C_{av,ss}=A_{av,ss}/V$가 됨 [R&T 5e p.289; R&T 5e p.324]. 다구획이면 amount-to-concentration 변환은 모델 구조에 따라 달라짐.

$$
\underbrace{MRT}_{\text{MRT}}=\underbrace{V/CL}_{\text{V/CL}}=\underbrace{1.44t_{1/2}}_{\text{반감기 시간}}\quad\Rightarrow\quad\overbrace{\underbrace{C_{av,ss}}_{\text{평균농도}}}^{\text{mg/L}}=\frac{\overbrace{\underbrace{A_{av,ss}}_{\text{평균량}}}^{\text{mg}}}{\underbrace{V}_{\text{용적 (L)}}}
$$

> 💡 **차원 방화벽 — 한 번에 정리**: 평균농도는 mg/L, 평균량은 mg임. $V$라는 다리 없이 등치 못 함. $1.44t_{1/2}$가 식에 들어간다고 해서 그게 농도 식이 되는 게 아님 — 그건 체류시간 기반 **약물량 식**임.

### B. 비유 — 욕조 다시

$C_{av,ss}$는 욕조의 **평균 수위**, $A_{av,ss}$는 욕조 안 **물의 평균 양**임. 욕조 크기($V$)를 모르면 물의 양으로 수위를 알 수 없음. 욕조 모양이 바뀌면(다구획) 같은 양의 물이라도 수위가 달라짐. → **수위와 물의 양은 다른 단위. $V$라는 다리가 있어야 통역됨.**

### C. 왜 이 분리가 임상에서 중요한가

$C_{av,ss}$는 **임상 목표·TDM·노출-반응 분석의 언어**임. *"이 환자 평균 농도를 4 mg/L에 맞추자"*라고 말할 때 쓰는 게 이거임. $A_{av,ss}$는 **체내 약물 부담과 체류 시간의 언어**고. *"지금 환자 몸 안에 약물이 평균 얼마나 머무르고 있나"*를 물을 때 쓰는 거임. 두 언어를 섞으면 보고서에서 "농도 목표"와 "체내 약물량 목표"가 같은 줄에 들어가서 용량 근거가 무너짐.

### D. 약물 예시 — 같은 식, 다른 $\tau/t_{1/2}$ 영역

**R&T 5e Table 11-1의 200 mg q24h 예시**는 단회 곡선을 시간 이동해서 더하는 방식(superposition; 단회 투여 곡선을 시간 이동해 더해서 반복투여 곡선을 만드는 기법)으로 반복투여 곡선이 예측됨을 보여줌 [R&T 5e pp.320–321]. **Clobazam**(GABAₐ 양성 알로스테릭 조절제, 항경련제) 예시는 단회 AUC와 투여간격만으로 평균 plateau 농도를 예측한다는 사실의 anchor임 [R&T 5e p.336].

세 NSAID/항생제로 **같은 식이 세 가지 다른 $\tau/t_{1/2}$ 영역**에서 어떻게 보이는지 비교할 수 있음 [R&T 5e pp.330–332]:

| 약물 | 분류 | $\tau/t_{1/2}$ 영역 | 결과 |
|---|---|---|---|
| **Amoxicillin** | 짧은 반감기 β-lactam, 페니실린계 | 큼 (interval ≫ $t_{1/2}$) | **변동 크고 축적 작음**. peak-trough가 평균에서 멀리 흔들림 |
| **Naproxen** | 중간 반감기 NSAID | 중간 | 변동과 축적이 둘 다 적당한 균형 영역 |
| **Piroxicam** | 긴 반감기 NSAID, $t_{1/2}\approx 50$ h (R&T 5e Fig. 11-7) | 작음 (interval ≪ $t_{1/2}$) | **변동 작고 축적 큼**. plateau 곡선이 거의 평탄 |

세 약물 다 같은 식($C_{av,ss}=F\text{Dose}/(CL\tau)$, $A_{av,ss}=1.44F\text{Dose}t_{1/2}/\tau$)으로 평균이 정의되지만, **환자가 실제 경험하는 농도 진폭은 $\tau/t_{1/2}$ 영역에 따라 본질적으로 달라짐**. → 그래서 *"같은 평균이면 같은 노출"*이 아니라는 사실의 임상 예시임.

$$
\overbrace{\underbrace{C_{av,ss}}_{\text{농도}}}^{\text{mg/L}}=\frac{F\cdot Dose}{CL\cdot\tau}\;\;\not\equiv\;\;\overbrace{\underbrace{A_{av,ss}}_{\text{약물량}}}^{\text{mg}}=\frac{1.44F\cdot Dose\cdot t_{1/2}}{\tau}
$$

### 한 줄 마무리

$C_{av,ss}$는 $CL$ 기반 농도식, $A_{av,ss}$는 $MRT$ 기반 약물량식. 두 식은 **차원이 다른** 두 답임. TDM·노출-반응이면 $C_{av,ss}$, body burden·체류시간이면 $A_{av,ss}$. $A_{av,ss}$를 농도식처럼 쓰는 순간 단위가 무너지고 용량 rationale이 깨짐.

---

<!-- SLIDE_START: M5 | title: §2-M5. Flip-flop 동태: $K_a<K$일 때 terminal slope의 정체 -->
<!-- SECTION_CORE: SC-07 -->
## §2-M5. Flip-flop — **terminal slope가 elimination을 말하지 않는다면?**

### 잠그는 자: **시계(timing)**의 정체

M4에서 농도와 약물량의 차원을 분리했음. 이번엔 곡선의 **말단 기울기**를 보고 elimination이라고 부르는 게 항상 맞는지 점검함.

**한 줄 cheat**: terminal slope를 자동으로 elimination으로 번역하면, **제형이 만든 느린 input을 약물 자체의 느린 제거로 오판**함. $K_a<K$ 가능성을 먼저 열어두면 투여경로·제형·흡수 지속시간이 해석의 앞자리에 옴.

### A. 정의와 수식

$$
\overbrace{\underbrace{K_a<K}_{\text{느린 흡수}}}^{\text{flip-flop 조건}}\;\Rightarrow\;\overbrace{\underbrace{\text{terminal slope}}_{\text{말단 기울기}}}^{\text{둘 중 느린 쪽 반영}}\approx\underbrace{K_a}_{\text{흡수 K}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $K_a$ | 1/time | 흡수 속도상수 | 제형·투여경로·depot 방출 |
| $K$ | 1/time | 소실 속도상수 | $CL/V$ 변화 |
| terminal slope | 1/time | 말단 구간을 지배하는 더 느린 과정 | $K_a<K$이면 absorption, $K_a>K$이면 elimination |

일반적으로는 $K_a>K$여서 terminal slope가 $K$를 반영함. Flip-flop은 그 반대임 — terminal half-life가 길게 보이는데, **약물 소실이 느리다는 뜻이 아니라 흡수 input이 오래 지속되는 상황**일 수 있음.

> 💡 **느린 쪽이 tail을 그림.** terminal slope는 elimination이 아니라 **두 과정 중 더 느린 쪽**을 반영함. 긴 terminal half-life를 보고 곧바로 "느린 elimination이구나" 하지 말고, **IV 데이터나 제형 정보를 먼저 확인**해야 함.

### B. 비유 — 수도꼭지/배수구

수도꼭지가 작고(느린 입력) 배수구가 크면(빠른 제거), 수도꼭지를 잠가도 배수구 속도로 빠르게 빠짐 → terminal slope = elimination. 반대로 수도꼭지는 더 작고 배수구가 그것보다 컸다면, 욕조 수위 곡선은 결국 **수도꼭지 속도(입력 끊김의 속도)**가 그리게 됨. **두 과정 중 율속단계(rate-limiting; 전체 속도를 정하는 느린 단계)가 tail을 그리는 것**임.

### C. 임상에서 — "나쁜 flip-flop"이 아니라 **"의도된 input 제어"**

서방형이나 depot 제형은 일부러 input을 느리게 만듦. 변동을 줄이고 투여 빈도를 낮추려고. 즉 제형이 absorption/input을 지배하면 terminal slope와 투여간격의 임상적 의미가 같이 바뀜.

- **Morphine MR**(모르핀 서방형, 만성 통증): 모르핀 자체의 elimination half-life가 짧은데도 서방형으로 만들면 q24h 투여가 가능해짐.
- **Leuprolide depot**(GnRH 효현제, 전립선암·자궁내막증): leuprolide 자체는 half-life가 짧지만 depot 제형으로 월 1회 투여가 가능함.

→ 그래서 두 약 모두 **terminal slope가 $K_a$를 반영하는 의도된 flip-flop**의 임상 사례임 [R&T 5e pp.337–338].

> 📖 **G&W 5e, p.45, Fig. 2.29**: ordinary case와 flip-flop case의 terminal phase 정체가 어떻게 다른지 한 그림에 비교해서 보여줌 — terminal slope를 elimination slope로 잘못 읽는 오류가 어디서 발생하는지 시각적으로 박힘.

### 한 줄 마무리

말단 기울기를 곧바로 elimination으로 번역하지 말 것. **투여경로 → 제형 → 흡수 지속시간** 순으로 먼저 확인함. *"terminal half-life = elimination half-life"*로 고정하면 제형·input 효과가 누락되고 투여간격 판단이 거꾸로 감.

---

## 묶음 ② — 설계 다리(dosing-design bridge): PK 시계를 임상 투여 설계로 (M6–M8)

여기서부터는 PK **식**이 임상 **결정**으로 넘어가는 자리임. M6에서 치료역이라는 임상 제약을 세우고, M7에서 부하/유지로 시작점과 유지를 분리하고, M8에서 그 두 개를 알고리즘 한 줄로 묶음.

---

<!-- SLIDE_START: M6 | title: §2-M6. Therapeutic Window — PK 식을 임상 의사결정으로 바꾸는 제약조건 -->
<!-- SECTION_CORE: SC-08 -->
## §2-M6. 치료역(Therapeutic Window) — **PK 식을 임상 결정으로 바꾸는 제약조건**

### 잠그는 자: **임상 제약(clinical constraint)** — 새로운 자가 추가됨

M5까지는 약물 쪽 시계만 봤음. 이제 환자 쪽 자가 하나 추가됨 — **효과와 위해의 균형**임.

**한 줄 cheat**: 치료역을 단순 "농도 범위"로만 읽으면 PK 식이 임상 판단으로 넘어가는 지점이 사라짐. **치료역은 농도 축 위에 그어놓은 두 개의 선**임. 아래 선($C_{lower}$)은 효과 하한, 위 선($C_{upper}$)은 위해 상한. **이 두 선이 regimen 설계의 제약조건**임.

### A. 용어 잠금 — 세 개를 분리

비슷해 보이는 세 용어가 다 다름. 보고서 작성 시 가장 자주 섞이는 자리임:

| 용어 | 정의 | 출처 |
|---|---|---|
| **Therapeutic concentration range** | 임상 경험상 효과가 있고 위해가 받아들여질 만한 농도 범위 | [R&T 5e p.272] |
| **Therapeutic window (TW)** | 효용 곡선의 역치 이상으로 정의되는 임상 의사결정 구간 | [R&T 5e pp.273–274] |
| **Therapeutic index (TI)** | 전임상에서 $TD_{50}/ED_{50}$ ratio. **임상에서는 노출 변화에 대한 개별 환자의 limiting effect sensitivity**(노출이 위해/효과를 얼마나 예민하게 바꾸는가) | [R&T 5e p.278] |

위 세 개를 한 표로 묶어 외우면:

$$
\overbrace{\underbrace{TI}_{\text{TI}}}^{\text{전임상 ratio}}\sim\frac{\overbrace{\underbrace{TD_{50}}_{\text{독성 TD50}}}^{\text{50\%에서 독성}}}{\overbrace{\underbrace{ED_{50}}_{\text{효과 ED50}}}^{\text{50\%에서 효과}}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $C_{lower}$ | 농도 | 효과가 기대되는 하한 | efficacy threshold |
| $C_{upper}$ | 농도 | 위해가 커지는 상한 | toxicity threshold |
| Therapeutic Window | 농도 구간 | 효과–위해 균형의 의사결정 영역 | 임상 반응·환자 민감도 |
| Therapeutic Index | ratio/민감도 | 전임상 ratio 또는 노출 민감도 | 독성 여유·개체변이 |

> 💡 **PK에서 임상으로 넘어가는 문턱**: 치료역은 PK 식의 **결과**가 아니라 regimen이 **통과해야 하는 제약**임. TW와 TI를 같은 안전성 용어처럼 합치는 순간 용량 근거가 흐려짐.

### B. 효용 수식화 — 교과서 원수식이 아니라 교육적 표현

$U(C)=\sum w_iP_i(C)$ 같은 표현은 **교과서 원수식이 아니라 개념을 식 형태로 표현한 교육적 formalization**임. 출처 식과 구별해서 읽어야 함.

$$
\overbrace{\underbrace{U(C)}_{\text{C별 효용}}}^{\text{교육용 표현}}=\sum_i \underbrace{w_i}_{\text{가중치}}\;\underbrace{P_i(C)}_{\text{결과확률}}
$$

R&T 5e Fig. 9-4의 가중치 예시는 저자 판단에 따른 illustrative weighting이라 표준 규제 가중치처럼 쓰면 안 됨 [R&T 5e p.273].

### C. PK 시계와 PD 시계는 다를 수 있음 (→ M9에서 다시 자세히)

혈장 농도가 항상 효과를 즉시 설명하지는 않음. 두 약물 anchor만 미리 박아둠 — 정량 분석은 M9에서:

- **Atorvastatin**(HMG-CoA 환원효소 억제제, 스타틴): parent PK 반감기 약 14 h (R&T 5e Fig. 11-16 caption), 활성 대사체(2-/4-hydroxy atorvastatin)의 $t_{1/2}$는 약 20–30 h. 그런데 cholesterol 반응 plateau는 3–4주 — LDL turnover 시상수 지배.
- **Erythropoietin**(EPO, 적혈구 생성 자극인자): PK 반감기 약 9 h이지만 hematocrit plateau는 약 70일 — RBC lifespan ($\approx 120$일) 지배 [R&T 5e pp.343–344].

→ 그래서 효과 평가 시점을 잡을 때 항상 묻는 질문 — **"이 시간상수는 누구의 반감기인가 — 약물인가, turnover 시스템인가?"** 정량 분석은 M9의 $t_{PD\;plateau}\approx \ln 10/k_{out}$에서 다시 봄.

### D. 항균제 — PK index가 다르면 dosing logic도 달라짐

항균제는 **어떤 PK 지표가 효과와 연결되는지**에 따라 dosing logic이 완전히 갈림 [R&T 5e pp.307–312; R&T 5e pp.347–348]:

- **β-lactam 계열**(time above MIC가 효과 결정): MIC 위에 머무는 시간이 핵심이니까 prolonged/continuous infusion이 합리적임.
- **Aminoglycoside**(peak/MIC 효과 + toxicity window): peak이 높을수록 효과가 좋고 trough가 낮을수록 신독성이 적으니까 once-daily 분할이 합리적임.

R&T 5e Fig. 11-20의 **AUC/MIC > 101** 예시는 내성 회피의 정량적 근거임 [R&T 5e p.348]. → 그래서 **같은 항균제 카테고리라도 PK index가 다르면 치료역 적용 방식도 다르다**는 임상 사례임.

### D′. Once-daily aminoglycoside의 정량적 근거 — $C_{max}/\mathrm{MIC}$ + post-antibiotic effect (PAE)

위에서 aminoglycoside의 once-daily 분할이 "합리적"이라고만 했는데, **왜 합리적인지의 정량적 근거**는 두 PD 인자가 같이 작동하기 때문임. 이 분리가 없으면 *"trough가 낮으면 위험 아닌가?"*라는 흔한 임상 반대 논거를 방어 못 함.

$$
\overbrace{\underbrace{\text{효과}}_{\text{살균력}}}^{\text{PD outcome}}\;\sim\;\overbrace{\underbrace{C_{max}/\mathrm{MIC}}_{\text{≥8–10 권장}}}^{\text{농도의존 살균}}\;\;+\;\;\overbrace{\underbrace{\mathrm{PAE}}_{\text{2–4 h 잔효}}}^{\text{C\;<\;MIC에서도 성장 지연}}
$$

| 인자 | 값 anchor | 임상적 의미 |
|---|---|---|
| $C_{max}/\mathrm{MIC}$ | $\geq 8\text{–}10$ | 농도의존(concentration-dependent) 살균 — high peak이 효과 핵심 |
| post-antibiotic effect (PAE) | $\approx 2\text{–}4$ h | 농도가 MIC 아래로 떨어진 뒤에도 균 성장이 억제되는 시간 |
| 신독성 trigger | 누적 노출 + **지속적 trough 노출**(trough $\geq$ 임계치 시간) | 잦은 분할 시 trough가 항상 일정 수준 이상 유지 → renal cortex 축적 |

→ **q24h once-daily 처방의 정량적 정당성**: (1) **high peak**으로 $C_{max}/\mathrm{MIC}\geq 8\text{–}10$ 확보, (2) PAE 덕분에 다음 dose 전 농도가 MIC 아래로 떨어져도 균 성장이 억제됨, (3) **drug-free interval**이 길어서 trough가 충분히 낮은 시간을 확보 → renal cortex의 약물 washout이 가능 → 신독성 위험 감소. **세 효과가 같은 방향으로 정렬됨.**

> 💡 **분할로 trough를 항상 일정 수준 이상 유지하면 오히려 위험**: aminoglycoside는 β-lactam처럼 "time above MIC"가 결정자가 아니라 **peak/MIC + PAE**가 결정자임. q8h로 trough를 유지하는 전략은 신독성만 키우고 효과는 별로 안 늘림 — PD index가 정반대 방향으로 작동하는 약물임 [R&T 5e pp.347–348].

이게 M3의 PTF 직관과 정확히 정합임. once-daily는 **$\tau/t_{1/2}$를 일부러 크게** 잡아 PTF를 크게 만든 처방 — peak은 효과로, trough(낮은 농도 구간)는 안전성으로 분리 활용하는 설계임.

> ⚠️ **실무 함정 — DDI는 protein binding만으로 설명하지 말 것**: DDI 민감도를 protein binding 하나로 정리하려 들면 어긋남. R&T 5e의 low/high 추출률 예시는 plateau 변화의 핵심 변수가 **간 추출률**임을 보여줌 [R&T 5e pp.309–310; R&T 5e pp.350–351].

> 📖 **R&T 5e p.272, Fig. 9-3**: 치료역을 "단순 농도 범위"가 아니라 **효과성 · 유해반응 · 효용의 균형**으로 보게 만드는 원문 핵심 그림임.

### E. TDM 임상 target reference — 알고리즘의 "목적지" 잠그기

M8에서 보게 될 TW 알고리즘이 작동하려면 $C_{lower}$와 $C_{upper}$를 채워 넣어야 함. 알고리즘은 이미 있는데 destination 없이 돌면 답이 안 나옴. 여기서는 PopPK/TDM 실무에서 가장 자주 다뤄지는 target reference를 한 표에 모아둠. R&T 5e Table 9-1의 임상 치료농도범위(therapeutic window)를 기본 anchor로 하되, 항균제(vancomycin AUC-based)는 2020 ASHP/IDSA consensus 같은 최신 임상 reference를 함께 명시함 [R&T 5e Table 9-1, p.276].

| 약물 | 임상 target (정상 신/간 기능 기준) | 측정 시점/매트릭스 | PD index 근거 |
|---|---|---|---|
| **Vancomycin** | $\mathrm{AUC}_{24}/\mathrm{MIC}\approx \mathbf{400\text{–}600}$ (MRSA 침습 감염) | 2-point Bayesian 추정 권장 — trough 단독은 deprecated | AUC-driven, time-above-MIC 보조 |
| **Aminoglycoside (gentamicin, tobramycin)** | $C_{max}\approx 8\text{–}10\,$mg/L, trough $<\mathbf{1\text{–}2}$ mg/L (q24h once-daily) | trough = 다음 dose 직전 | $C_{max}/\mathrm{MIC}\geq 8\text{–}10$ + PAE |
| **Digoxin** | $\mathbf{0.5\text{–}2}$ ng/mL (HF에서 $0.5\text{–}0.9$ 권장) | 다음 dose 전 ≥ 6 h | narrow window, 분포 평형 후 측정 필수 |
| **Lithium** | $\mathbf{0.6\text{–}1.2}$ mmol/L (급성 1.0–1.2, 유지 0.6–0.8) | 마지막 dose 후 12 h trough | narrow TI, dose dependence |
| **Tacrolimus** | $\mathbf{5\text{–}20}$ ng/mL (이식 phase에 따라 가변) | **whole blood** trough (RBC 분배 큼) | exposure-rejection-toxicity 삼각 |
| **Phenytoin** | total $\mathbf{10\text{–}20}$ mg/L, **unbound $1\text{–}2$ mg/L** | 저알부민·요독 환자에서는 unbound 직접 측정 권장 | 비선형 PK + 단백결합 변화 |
| **Cyclosporine** | 이식 phase별 가변 (C0 또는 C2 monitoring) | **whole blood** | 분획 매트릭스 의존성 큼 |

> 💡 **목적지 없이 알고리즘 없음**: M8 TW 알고리즘의 $C_{lower}$, $C_{upper}$는 이 표가 채워줌. 단, **이 값들은 임상 reference이지 절대 기준이 아님** — 적응증, 신/간 기능, 단백결합 상태, 측정 매트릭스(plasma vs whole blood)에 따라 조정됨. **vancomycin trough 단독 monitoring은 2020 consensus 이후 deprecated**되고 AUC-based로 옮겨갔다는 점도 같이 기억해둘 것.

> ⚠️ **매트릭스 함정 — whole blood vs plasma/serum**: tacrolimus·cyclosporine은 **whole blood**, phenytoin·warfarin은 **plasma**, digoxin은 **serum**에서 측정함. 보고서가 어느 매트릭스에서 측정된 값인지 확인하지 않으면 PopPK fitting의 noise가 신호로 잘못 들어감. 이 줄을 안 짚으면 covariate 검색이 매트릭스 효과를 covariate으로 잘못 잡음.

이 표는 **이 세션의 식을 임상 의사결정으로 옮기는 마지막 다리**임. M8 알고리즘이 "어떻게(how)"를 잠그면, 이 표는 "어디로(where to)"를 잠금.

### 한 줄 마무리

치료역은 PK 식의 마지막 줄이 아니라 **투여 설계의 제약조건**임. 목표농도, 변동, PD 지연, 독성 메커니즘을 동시에 제한함. TW와 TI를 동의어로 쓰는 순간 농도 구간과 민감도가 섞이고 용량 근거가 불명확해짐.

---

<!-- SLIDE_START: M7 | title: §2-M7. Loading Dose + Maintenance: 목표 즉시 도달과 유지의 분리 -->
<!-- SECTION_CORE: SC-09 -->
## §2-M7. 부하 + 유지 용량 — **시작점과 유지를 따로 잡기** ($D_L$ + $D_M$)

### 잠그는 자: **시계의 시작점** + **무게중심의 유지**

M6에서 치료역이라는 임상 제약을 세웠음. 이제 그 제약 안에서 작동할 두 가지 용량 — **목표에 빨리 도달하는 부하용량**과 **거기를 유지하는 유지용량**을 분리함.

**한 줄 cheat**: 부하용량과 유지용량을 한 단어 "용량"으로 뭉치면 즉시 도달과 평균 유지가 섞임. **$D_L$은 시작점 위치를 잡고, $D_M$은 반복 입력률을 유지함** — 이 분리를 잡으면 두 식이 하나의 설계 언어가 됨.

### A. 정의와 수식

부하용량과 유지용량의 관계는 한 식으로 잠금:

$$
\overbrace{\underbrace{D_M}_{\text{유지용량}}}^{\text{interval당 보충}}=\overbrace{\underbrace{D_L}_{\text{부하용량}}}^{\text{시작점 형성}}\;\underbrace{(1-e^{-K\tau})}_{\text{보충분율}}
$$

이 식을 뒤집어서 부하/유지 관계로 보면:

$$
\overbrace{\underbrace{D_L}_{\text{부하용량}}}^{\text{시작점}}=\frac{\underbrace{D_M}_{\text{유지용량}}}{\underbrace{1-e^{-K\tau}}_{\text{보충분율}}}=\overbrace{\underbrace{R_{ac}}_{\text{축적계수}}}^{\text{ratio}}\;\underbrace{D_M}_{\text{유지용량}}
$$

→ **부하용량은 유지용량의 $R_{ac}$배.** M3에서 본 $R_{ac}$가 여기서 부하/유지 ratio로 다시 등장함. 즉 **축적계수는 한 카드(M3)에서 끝나는 게 아니라 부하용량 계산의 핵심 ratio로 재등장**함.

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $D_L$ | dose | 목표 근처로 즉시 올리는 부하용량 | target 농도·$V/F$ |
| $D_M$ | dose | 반복 투여로 평균 입력률을 유지하는 용량 | $CL$, $\tau$, target 농도 |
| $R_{ac}$ | 무차원 | 유지용량과 부하용량을 잇는 축적 배율 | $\tau/t_{1/2}$ 변화 |
| $K$ | 1/time | 도달 시간과 잔여분을 지배 | $CL/V$ 변화 |

또 다른 식 형태(보다 임상 친화적):

$$
\overbrace{\underbrace{LD}_{\text{부하용량}}}^{\text{시작점}}=\frac{\overbrace{\underbrace{V}_{\text{V}}\;\underbrace{\text{target}}_{\text{목표농도}}}^{\text{체내 목표량}}}{\underbrace{F}_{\text{F}}},\qquad
\overbrace{\underbrace{MD}_{\text{유지용량}}}^{\text{입력 속도}}=\overbrace{\underbrace{CL}_{\text{청소율}}\;\underbrace{\text{target}}_{\text{목표농도}}\;\underbrace{\tau}_{\text{투여간격}}}^{\text{interval당 손실 보충}}
$$

> 💡 **시작과 유지의 분리**: $D_L$은 **위치**를, $D_M$은 **평균 입력률**을 정함. 부하용량으로 항정상태 **시간상수**를 바꾸는 게 아님 — **시작점을 target 근처로 옮기는 것**임.

### B. 비유 — 자동차 가속 vs 크루즈 컨트롤

부하용량은 차를 고속도로 제한속도까지 올리는 **가속페달**, 유지용량은 그 속도를 유지하는 **크루즈 컨트롤**임. 가속페달은 한 번 강하게 밟고 끝, 크루즈 컨트롤은 끊임없이 미세 조정. **둘은 같은 페달이 아님.** 같은 자동차에 두 종류의 입력 제어가 있는 것임.

### C. 약물 예시 — 단순 anchor 두 개

**Doxycycline**(테트라사이클린계 항생제, 광범위 그람양성/음성/비전형): $t_{1/2}=24$ h, $D_L=200$ mg, $D_M=100$ mg/day, $R_{ac}=2$.

$$
\overbrace{\underbrace{D_L}_{200\text{ mg}}}^{\text{doxycycline 부하}}=\underbrace{R_{ac}}_{2}\times\overbrace{\underbrace{D_M}_{100\text{ mg/day}}}^{\text{doxycycline 유지}}
$$

→ 그래서 $D_L=R_{ac}\times D_M=2\times 100=200$ mg이라는 부하/유지 관계의 **가장 단순한 임상 anchor**임 [R&T 5e p.327].

**Sirolimus**(mTOR 억제제, 신장이식 면역억제제): $t_{1/2}=2.5$ days, loading 6 mg, maintenance 2 mg/day. → 식대로면 $R_{ac}\approx4.3$, $D_L\approx8.6$ mg이지만 실제 임상 용법은 6 mg / 2 mg/day임. **이론식과 실제 내약성 사이의 조정이 어떻게 들어가는지** 보여주는 사례임 [R&T 5e pp.326–327].

### D. Bolus + 주입 — 정속 주입에서 즉시 plateau 만들기

정속 주입에서 즉시 plateau 근처에 올리고 싶으면 bolus와 infusion을 결합함. **bolus가 초기 농도 위치를 만들고, infusion이 그 뒤로 input rate를 유지함.** Gabrielsson PK13의 수치 anchor: **400 µg/kg bolus + 800 µg/kg over 26 min**, 치료역 50–300 µg/L, $V_c=2.0$ L/kg, $CL=1.0$ L/min/kg, $CL_d=1.0$ L/min/kg, $V_t=5.0$ L/kg [G&W 5e pp.537–539].

### D′. Target Controlled Infusion (TCI) — bolus+infusion의 임상 자동화

위 bolus+infusion이 **한 시점**의 즉시 plateau 진입 문제라면, **TCI**(target controlled infusion)는 그걸 **연속 시간 축**에서 자동화한 임상 시스템임. 마취과에서 propofol·remifentanil로 매일 쓰이는데, 그 안의 PK 논리는 정확히 이 세션의 **M7 + M5 + M3을 합쳐놓은 것**임.

$$
\overbrace{\underbrace{C_{target}(t)}_{\text{시간별 목표농도}}}^{\text{임상가가 설정}}\;\;\rightarrow\;\;\overbrace{\underbrace{\text{펌프 알고리즘}}_{\text{내장 PK 모델}}}^{\text{3구획 PK 식 풀이}}\;\;\rightarrow\;\;\overbrace{\underbrace{R_{in}(t)}_{\text{실시간 가변 주입률}}}^{\text{출력}}=\overbrace{\underbrace{CL\cdot C_{target}}_{\text{유지}}}^{D_M에 해당}+\overbrace{\underbrace{V\cdot \frac{dC_{target}}{dt}}_{\text{목표 변화 보정}}}^{D_L에 해당}+\overbrace{\underbrace{Q\cdot(C_p-C_t)}_{\text{재분포 보정}}}^{\text{다구획 보정}}
$$

| 구성요소 | 임상 의미 | M7과의 연결 |
|---|---|---|
| $C_{target}$ 설정 | 임상가가 "혈장(또는 effect-site) 목표농도"를 직접 지정 | M6의 TW 안쪽 목표점 |
| 펌프 내장 PK | 보통 3-구획 PK 모델 (Marsh / Schnider for propofol, Minto for remifentanil) | M5/§4의 다구획 구조 |
| 초기 bolus | 목표농도로 즉시 진입 | M7-A의 $D_L$ |
| 가변 infusion | 재분포·elimination에 맞춰 실시간 조정 | M7-A의 $D_M$의 시간 연속 버전 |
| effect-site mode | $k_{e0}$를 추가해 효과 부위 농도를 직접 target | M9의 PK-PD 시계 분리를 자동화 |

> 💡 **TCI는 부하/유지의 시간 연속 일반화임.** M7의 $D_L$ + $D_M$이 "한 번 부하 + 일정 유지"라면, TCI는 "매 순간 부하·유지·재분포 보정이 자동으로 합쳐진 가변 주입"임. 같은 식의 시간 연속 버전 — **펌프 안에 다구획 PK 모델이 내장되어 있는 것**임.

**임상 약물 anchor**:
- **Propofol** (GABA_A 양성 알로스테릭 조절제, 정맥 마취제): Marsh 또는 Schnider 모델 내장. 혈장 또는 effect-site target 선택 가능. 빠른 onset/offset이 핵심.
- **Remifentanil** (초단기 μ-opioid agonist, 비특이 esterase로 분해): Minto 모델 내장. Context-sensitive half-time이 거의 일정($\approx 3\text{–}4$ min) — 장시간 주입 후에도 회복이 빠른 게 임상 장점임.

> ⚠️ **TCI 실패의 가장 흔한 자리 — covariate 적용 한계**: TCI 알고리즘의 PK 모델은 healthy adult 평균 환자에서 유도된 것임. 비만, 소아, 노인, 심한 간/신 기능 저하 환자에서는 모델 prediction error가 커짐. *"펌프가 알아서 한다"*가 아니라 **펌프 안의 PK 가정을 임상가가 알고 있어야** 안전 마진을 잡을 수 있음.

### E. 다시 daptomycin — 분할 자체가 regimen 변수

같은 75 mg/kg/day인데 q24h와 q8h의 CPK가 **991 vs 3996 U/L**, 약 4배 차이 났음 [R&T 5e pp.351–353]. Study B에서는 한 단계 더 — **같은 $C_{max}=58$ µg/mL** 조건에서도 분할 패턴에 따라 AUC와 CPK가 달랐음. → 그래서 $C_{max}$ 하나로도, AUC 하나로도 독성을 설명할 수 없고 **회복 시간과 분할 패턴을 함께 봐야 한다**는 사실의 임상 사례임. 자세한 분석은 M10에서.

> 📖 **R&T 5e, p.352 Fig. 11-24 / p.353 Table 11-7**: 이 세션에서 "같은 일일 용량" 비교군을 잘못 잡으면 결론이 통째로 뒤집힘. Fig. 11-24와 Table 11-7을 같이 보아야 농도 프로파일, 일일 용량, CPK 결과가 분리됨.

### 한 줄 마무리

부하용량은 **초기 조건**, 유지용량은 **장기 입력 속도**, 분할투여는 **회복 시간과 변동**을 바꿈. *"부하용량이 SS 시간을 단축한다"*고 말하면 **시작점 이동과 시간상수**가 섞이고, 발현 근거가 과장됨.

**실무 활용**: 중환자실 부하용량 프로토콜에서 신기능 조정 항목을 **LD와 MD에 따로** 명시해야 함. Daptomycin Study A의 991 vs 3996 U/L는 "같은 일일 용량 ≠ 같은 독성"이라는 라벨의 임상 근거임.

---

<!-- SLIDE_START: M8 | title: §2-M8. 치료역 기반 투여 설계 알고리즘(TW-Driven Dosage Design Algorithm) -->
<!-- SECTION_CORE: SC-10 -->
## §2-M8. 치료역 기반 투여 설계 알고리즘 — **$C_{upper}$/$C_{lower}$만 있으면 interval과 dose 상한이 계산된다**

### 잠그는 자: **시계 + 무게중심**을 임상 제약 안에 가둠

M7에서 부하와 유지의 역할을 나눴음. 이제 $C_{upper}$와 $C_{lower}$만 있으면 **실제 투여간격과 용량 상한**이 계산된다는 걸 봄. 즉 M1~M7을 한 알고리즘으로 묶는 종착역임.

**한 줄 cheat**: 이 알고리즘을 **자동 처방기**로 읽으면 선형 PK나 즉각적 농도-반응 가정이 깨진 순간에도 공식을 밀어붙이게 됨. **타당성 점검(feasibility screen)**으로 읽어야 함 — interval, dose size, loading 필요성을 각각 다른 파라미터로 방어할 수 있도록.

### A. 정의와 수식

알고리즘의 출발점은 한 줄임 — *"농도가 $C_{upper}$에서 $C_{lower}$로 감소하는 데 걸리는 시간을 $\tau$로 잡으면 TW 안에 머무름"*:

$$
\overbrace{\underbrace{C_{lower}}_{\text{하한}}}^{\text{효과 역치}}=\overbrace{\underbrace{C_{upper}}_{\text{상한}}}^{\text{독성 역치}}\;\underbrace{e^{-K\tau_{max}}}_{\text{허용감소}}
$$

이걸 $\tau_{max}$에 대해 풀면 **interval 상한**이 나오고, 같은 TW 폭에서 dose 한 번에 채울 수 있는 차이로 풀면 **dose 상한**이 나옴:

$$
\overbrace{\underbrace{\tau_{max}}_{\text{최대간격}}}^{\text{TW 내 머무는 한계}}=\frac{\overbrace{\underbrace{\ln(C_{upper}/C_{lower})}_{\text{로그폭}}}^{\text{TW ratio}}}{\underbrace{K}_{\text{소실 K}}}=\underbrace{1.44t_{1/2}}_{\text{시간척도}}\;\overbrace{\underbrace{\ln\left(\frac{C_{upper}}{C_{lower}}\right)}_{\text{TW 폭}}}^{\text{무차원 ratio}}
$$

$$
\overbrace{\underbrace{D_{M,max}}_{\text{최대 MD}}}^{\text{용량 상한}}=\overbrace{\underbrace{\frac{V}{F}}_{\text{V/F 보정}}}^{\text{apparent volume}}\;\underbrace{(C_{upper}-C_{lower})}_{\text{허용상승}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $\tau_{max}$ | time | 치료역 안에 머물 수 있는 최대 투여간격 | $t_{1/2}$, $C_{upper}/C_{lower}$ |
| $D_{M,max}$ | dose | 유지용량 상한 | $V/F$, $C_{upper}-C_{lower}$ |
| $C_{upper}$ | 농도 | 안전성 상한 | toxicity threshold |
| $C_{lower}$ | 농도 | 효과 하한 | efficacy threshold |
| $V/F$ | volume | apparent volume 다리 | bioavailability·분포 변화 |

> 💡 **두 비율, 두 다른 답**: $C_{upper}/C_{lower}$ **비율(ratio)**은 interval을 제약함. $C_{upper}-C_{lower}$ **차이(difference)**는 dose size를 제약함. 그래서 같은 치료역이라도 ratio가 좁으면 interval을 줄여야 하고, difference가 작으면 dose를 줄여야 함.

평균농도는 한 번 더 짚으면:

$$
\overbrace{\underbrace{C_{ss,av}}_{\text{허용평균}}}^{\text{log mean}}=\frac{\underbrace{C_{upper}-C_{lower}}_{\text{선형폭}}}{\underbrace{\ln(C_{upper}/C_{lower})}_{\text{로그폭}}}
$$

### B. 비유 — 운전 차선 규칙

치료역 기반 알고리즘은 **차선 폭 안에서 속도와 차간거리를 정하는 운전 규칙**임. 차선이 좁아지면(좁은 TW) 속도 선택의 자유와 차간거리 선택의 자유가 같이 줄어듦. **차선 ratio(폭/길이)는 속도를, 차선 difference(좌-우 폭)는 차폭을 제약**하는 것처럼, $C_{upper}/C_{lower}$ ratio는 interval을, $C_{upper}-C_{lower}$ difference는 dose 크기를 각각 제약함.

### C. 알고리즘 한 줄씩

1. $C_{lower}$, $C_{upper}$를 정함 — 임상 자료 기반으로 (M6-E 표 참고).
2. $t_{1/2}$로 $\tau_{max}$를 계산.
3. $V/F$로 $D_{M,max}$를 계산.
4. 실제 제형 강도와 복약 순응도를 고려해서 실용적 $\tau$와 $D_M$을 선택.
5. 필요하면 $D_L$로 initial target에 접근 (→ M7).

> ⚠️ **실무 함정 — 적용 중단 조건을 미리 적어두기**: 이 알고리즘은 **선형 PK, 고정 투여간격, target 농도와 임상 반응 사이의 충분한 직접 연결**을 전제로 함. 단회 투여 치료나 PD plateau가 turnover로 지배되는 약물에서는 적용 못 함 [R&T 5e p.279; R&T 5e pp.341–345]. 프로토콜 첫 페이지에 **"선형 PK 비성립 · 즉각적 농도-반응 가정 깨짐 · flip-flop · 단회 투여 · turnover 지배 PD plateau 중 하나라도 의심되면 모델 확장으로 돌아간다"**를 명시해둘 것.

### D. 한 줄에 다 묶기

M8은 M1–M7을 **투여 알고리즘으로 묶는 끝점**임. $C_{upper}/C_{lower}$ 비율은 interval을, $V/F$는 dose 크기를, $CL$은 평균 농도를 각각 제약함:

$$
\overbrace{\underbrace{\tau_{max}}_{\text{간격상한}}=1.44t_{1/2}\ln\left(\frac{C_{upper}}{C_{lower}}\right)}^{\text{ratio가 정함}},\qquad
\overbrace{\underbrace{D_{M,max}}_{\text{용량상한}}=\frac{V}{F}(C_{upper}-C_{lower})}^{\text{difference가 정함}}
$$

> 📖 **R&T 5e, p.335, Fig. 11-10**: $C_{upper}$, $C_{lower}$, $\tau_{max}$, $D_M$, $D_L$이 하나의 투여 설계 순서로 묶여 있음을 같은 틀 안에 보여주는 그림임.

### 한 줄 마무리

이 알고리즘을 자동 처방기처럼 쓰면 가정 위반을 못 보고 모델 확장 필요성을 놓침. **타당성 점검 = 적용 중단 조건을 같이 적어두는 것**임. 그리고 그 적용 중단 조건의 핵심이 바로 다음 두 카드(M9, M10)에서 다룰 PD plateau와 분할 독성임.

---

## 묶음 ③ — PD/안전성 시계(PD/safety clock): 환자 쪽 시간 (M9–M10)

M1–M8은 모두 약물 쪽 시계가 임상 결정을 정하는 영역이었음. 이제 마지막 두 카드는 **그 영역이 깨지는 자리**임 — 효과의 시계가 약물 시계와 다르고(M9), 독성 누적이 plasma 농도 누적과 다른(M10) 상황.

---

<!-- SLIDE_START: M9 | title: §2-M9. PD 기반 Plateau(PD-Driven Plateau): 효과의 시계는 약물의 시계와 다를 수 있습니다 -->
<!-- SECTION_CORE: SC-11 -->
## §2-M9. PD 기반 Plateau — **"이 반감기는 누구의 반감기인가?"**

### 잠그는 자: **새로운 시계** — 약물 시계가 아닌 turnover 시계

M8에서 PK 기반 투여 알고리즘의 적용 조건을 잠갔음. 이번엔 그 알고리즘이 **그대로 통하지 않는 영역** — 효과 plateau가 PK plateau와 다른 시계로 움직이는 경우를 봄.

**한 줄 cheat**: PK plateau를 효과 plateau로 옮겨 쓰면 statin이나 EPO 같은 turnover 지배 약물에서 평가 시점을 너무 일찍 잡게 됨. **"이 반감기는 누구의 반감기인가?"**를 먼저 물어야 약물 시계와 생물학적 시계가 분리됨.

### A. 정의와 anchor

두 약물 anchor를 정량 비교로 박아둠:

- **Atorvastatin**(HMG-CoA 환원효소 억제제, 스타틴): parent compound의 PK $t_{1/2}\approx14$ h. 그런데 cholesterol 반응의 최대 효과는 **3–4주** 걸림 [R&T 5e p.343, Fig. 11-16]. → 그래서 **약물 반감기와 turnover 시스템 반감기가 다르다**는 사실의 임상 사례임.
- **Erythropoietin**(EPO, 적혈구 생성 자극인자): PK $t_{1/2}\approx9$ h. 그런데 hematocrit plateau는 **약 70일** — RBC 수명 약 120일에 종속임 [R&T 5e p.344]. → 그래서 **반응 변수의 시계가 세포 수명에 묶여 있다**는 사실의 임상 사례임.

핵심 부등식:

$$
\overbrace{\underbrace{t_{1/2,\;PK}}_{\text{PK 시계}}}^{\text{약물 분자의 반감기}}\;\not\equiv\;\overbrace{\underbrace{t_{\text{PD plateau}}}_{\text{PD 시계}}}^{\text{반응변수 turnover 시상수}}
$$

### B. PD plateau의 정량 — turnover 시상수가 정함

위 두 약물의 PD plateau가 PK plateau와 다른 이유는 **반응 변수가 turnover 시스템에 속해 있기 때문**임. 그 turnover의 1차 시상수가 PD plateau 시간을 결정함. 메시지를 정성적으로 두지 말고, 정량적으로 잠궈둘 수 있음.

기본 turnover 모델 (indirect response model, Type I/III) [R&T 5e p.343]에서 반응 변수 $R$은:

$$
\overbrace{\underbrace{\frac{dR}{dt}}_{\text{반응 변화}}}^{\text{Type I/III IDR}}=\overbrace{\underbrace{k_{in}}_{\text{생성률}}}^{\text{약물이 자극/억제}}-\overbrace{\underbrace{k_{out}\cdot R}_{\text{1차 소실}}}^{\text{내인성 turnover}}
$$

→ 항정상태에서 약물 변화 후 새로운 $R_{ss}$로의 접근은 **$k_{out}$이 정하는 1차 과정**임. 따라서:

$$
\overbrace{\underbrace{t_{PD\;plateau}}_{\text{PD plateau 90\%}}}^{\text{접근 시간}}\;\approx\; \frac{\overbrace{\underbrace{\ln 10}_{\approx 2.3}}^{\text{90\% 기준}}}{\underbrace{k_{out}}_{\text{반응변수 소실속도}}}\;\;,\qquad \overbrace{\underbrace{t_{1/2,\,PD}}_{\text{PD 반감기}}}^{\text{turnover 반감기}}=\frac{\ln 2}{k_{out}}
$$

이게 M2의 *"3–4 half-lives 규칙"*과 같은 식 구조인데, **K가 $k_{out}$으로 바뀌었을 뿐**임. 즉 **M2 식 자체는 그대로 통하지만, "어떤 K인가"의 답만 바뀐 것**임.

#### Atorvastatin (cholesterol) — 정량 anchor

- Parent $t_{1/2}$ 14 h, **활성 대사체**(2-hydroxy / 4-hydroxy atorvastatin)의 $t_{1/2}$는 **약 20–30 h**로 더 김. 따라서 PK 시계의 실효 반감기는 14 h 단독이 아니라 parent + 활성 대사체 합성으로 보아야 함.
- 그런데도 PD plateau 3–4주의 진짜 정체는 PK 시계가 아님. **LDL 수용체와 cholesterol pool의 turnover** — $t_{1/2,\,LDL\;receptor}\approx 14$일 → $k_{out}\approx \ln 2/14\,\text{일}\approx 0.05\,\text{day}^{-1}$, 따라서 $t_{PD\;90\%}\approx 2.3/0.05\approx 46\,\text{일}$. 실제 임상 plateau 3–4주는 LDL 수용체 upregulation 시상수가 cholesterol pool의 다른 빠른 경로(생성 억제 즉시 효과)와 섞인 결과임.

$$
\overbrace{\underbrace{14\;\mathrm{h}}_{\text{parent }t_{1/2}}}^{\text{PK 시계}}\;\ll\;\overbrace{\underbrace{20\text{–}30\;\mathrm{h}}_{\text{활성 대사체}}}^{\text{보정 PK 시계}}\;\ll\;\overbrace{\underbrace{3\text{–}4\;\text{주}}_{\text{LDL turnover 시상수}}}^{\text{PD 시계}}
$$

#### EPO (hematocrit) — 정량 anchor

- $t_{1/2,\,PK}\approx 9$ h이지만, 반응 변수인 hematocrit의 turnover는 **RBC lifespan $\approx 120$일**이 정함. $k_{out}\approx \ln 2/120\,\text{일}\approx 0.0058\,\text{day}^{-1}$, 따라서 $t_{PD\;90\%}\approx 2.3/0.0058\approx 400\,\text{일}$이지만, 실제로는 RBC 생성률 자극 + 순환 RBC 누적이라 plateau 70일에 도달.

$$
\overbrace{\underbrace{9\;\mathrm{h}}_{\text{PK }t_{1/2}}}^{\text{PK 시계}}\;\ll\;\overbrace{\underbrace{70\;\text{일}}_{\text{관찰 PD plateau}}}^{\text{PD 시계}}\;\lesssim\;\overbrace{\underbrace{120\;\text{일}}_{\text{RBC lifespan}}}^{\text{생리적 상한}}
$$

→ 두 약물 모두 **PD plateau의 시상수가 PK 시상수가 아니라 반응변수의 $k_{out}$**(또는 세포 수명)에서 옴. 이게 M2의 "3–4 half-lives 규칙"을 PD에 그대로 옮기면 안 되는 이유의 **정량적 핵심**임.

> 💡 **PD plateau의 시상수 = $\ln 2 / k_{out}$**: 무엇의 반감기인지를 확정하는 방법은 단순함. **반응 변수의 turnover 시상수**를 먼저 식별함. cholesterol이면 LDL pool 동역학, hematocrit이면 RBC lifespan, blood pressure(β차단제)이면 baroreceptor 적응 시상수, glucose(SGLT2 억제제)이면 renal threshold 회복 — 각각 다른 $k_{out}$임. 이 분리가 안 되면 임상시험 PD endpoint 측정 시점이 통째로 어긋남.

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $t_{1/2,PK}$ | time | 약물 농도 plateau의 시계 | 약물 청소율·용적 |
| $t_{PD\ plateau}$ | time | 효과 plateau의 시계 | turnover·세포 수명 |
| $k_{out}$ | 1/time | 반응 변수의 1차 소실 속도 (turnover) | 생리적 회복·세포 수명·수용체 turnover |
| turnover | 1/time 또는 time | 반응 변수의 생성·소실 구조 | 생리적 회복·세포 수명 |
| response variable | 효과 단위 | cholesterol, hematocrit 등 관찰 반응 | 약물 효과 + 생물학적 시계 |

> 💡 **무엇의 반감기인가**: 약물 반감기와 반응 시스템의 반감기는 같은 숫자가 아닐 수 있음. M2의 3–4 half-lives 규칙을 cholesterol 반응이나 hematocrit plateau에 그대로 옮기면 발현 시점을 심하게 앞당기게 됨.

### C. M2 / M8과 어떻게 연결되나

M2에서 봤던 "3–4 half-lives ≈ 90%" 규칙은 **PK plateau에만 해당**함. 이걸 PD plateau에 그대로 옮기면 atorvastatin의 cholesterol 반응을 *"3–4 half-lives = 2–3일"*이라고 예측하게 되는데, 실제 plateau는 **3–4주**임. 결정 시점을 거의 **10배 앞당기는 셈**임 [R&T 5e pp.341–345].

M8 TW 알고리즘은 **즉각적 농도-반응 가정**이 성립할 때만 유효함. turnover 지배 약물에서는 알고리즘 적용 전에 **PD 시간척도 검토를 먼저** 수행해야 함.

> ⚠️ **실무 함정 — PD Plateau 시점 오류**: 효과 평가 시점을 잡기 전에 반드시 **"이 시간상수는 누구의 반감기인가 — 약물인가, turnover/세포 수명인가"**를 확인해야 함. 같은 숫자(예: 9 h)라도 약물 반감기와 hematocrit plateau를 결정하는 시계는 **완전히 다른 시계**임.

### 한 줄 마무리

PK plateau ≠ PD plateau. 효과의 시계는 약물 분자가 아니라 **내인성 turnover 시스템**이 정할 수 있음. *"PD plateau = 3–4 drug half-lives"*로 고정하면 효과 평가 시점이 조기화되고 regimen 판단이 거꾸로 감.

---

<!-- SLIDE_START: M10 | title: §2-M10. 용량분할 독성(Dose Fractionation Toxicity): 같은 일일 용량(daily dose)가 같은 위해를 의미하지 않습니다 -->
<!-- SECTION_CORE: SC-12 -->
## §2-M10. 용량분할 독성 — **plasma 누적과 조직 손상 누적은 다른 차원이다**

### 잠그는 자: **두 번째 새 시계** — 조직 회복 시계

M9에서 효과의 시계가 약물 농도와 분리될 수 있음을 봤음. 마지막으로 — **독성 누적이 분할과 회복 시간에 의해 어떻게 달라지는지**, hook의 daptomycin 사례로 다시 돌아가서 분석함.

**한 줄 cheat**: *"같은 일일 용량 = 같은 독성"*이라고 읽으면 **회복 시간이 짧아진 조직 손상**을 놓침. 분할과 회복 시간을 함께 보면 **plasma 노출(plasma exposure)과 조직 손상 누적이 분리**됨 — 두 개가 다른 차원의 누적이라는 게 핵심임.

### A. Daptomycin Study A — 가장 깨끗한 사례

**75 mg/kg q24h vs 25 mg/kg q8h.** 둘 다 75 mg/kg/day로 일일 용량이 같지만 CPK는 **991 vs 3996 U/L**, 약 **4배 차이** [R&T 5e pp.351–353, Table 11-7, Fig. 11-24; Oleson et al. 2000 *Antimicrob Agents Chemother* 44:2948–2953 인용].

> ⚠️ **재확인 — 이 75 mg/kg/day는 임상 daptomycin 용량이 아님**: hook(§1)에서 짚었듯, 이 dose는 fractionation toxicity를 분리해서 보기 위한 **개 모델 등 실험적 design dose**임. 임상 daptomycin은 4–6 mg/kg/day (특정 적응증에서 8–12 mg/kg/day까지)로 한 자릿수 mg/kg 영역. 이 카드의 학습 메시지는 *"같은 daily dose ≠ 같은 toxicity"*라는 개념이지, 임상 daptomycin 용량의 anchor가 아님. 임상에서 daptomycin을 75 mg/kg/day로 처방하면 안 됨 [R&T 5e pp.351–353].

Study B로 한 단계 더 들어가면: **같은 $C_{max}=58$ µg/mL** 조건에서도 분할 패턴에 따라 AUC와 CPK가 달랐음 [R&T 5e p.353, Table 11-7]. 이 Study B의 dose 영역(5 mg/kg q24h vs 5 mg/kg q8h)은 임상 daptomycin 용량(4–6 mg/kg/day)에 더 가깝다는 점도 함께 짚어둘 가치가 있음.

$$
\overbrace{\underbrace{C_{max}}_{\text{최대농도}}}^{\text{같음 (58 µg/mL)}}\quad\not\Rightarrow\quad\overbrace{\underbrace{\text{동일독성}}_{\text{AUC·회복}}}^{\text{분할 패턴이 가름}}
$$

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $C_{max}$ | 농도 | 최고 농도 | dose 크기·흡수속도·분할패턴 |
| AUC | 농도×시간 | 총 노출 | dose·청소율 |
| fractionation interval | time | 분할투여 간격 | q24h, q8h 등 regimen |
| recovery time | time | 표적 조직이 손상에서 회복하는 시간 | 조직 생물학 |
| CPK | U/L | 근육 독성 표지자 | daptomycin 분할 패턴 |

> 💡 **같은 일일 용량의 함정**: 총량이 같아도 q24h와 q8h는 **회복 시간을 다르게 남김**. $C_{max}$ 하나로 또는 AUC 하나로 독성을 설명하면 분할 효과가 안 보임.

### B. 비유 — 운동과 회복

같은 양의 운동도 휴식 없이 세 번 나눠서 하면 근육 손상이 훨씬 커짐. **분할은 총량의 문제가 아니라 "회복 틈을 얼마나 남기는지의 문제"**임. 트레이너가 "주 3회 한 시간씩"과 "매일 20분씩"을 다르게 처방하는 이유와 동일함.

### C. M3 / M7과의 연결 — 두 종류의 누적

여기서 가장 중요한 통찰임. **M3의 $R_{ac}$는 plasma 구획 안에서의 약물 누적**만 다룸. M10은 다른 차원임 — **"약물 자체의 누적"이 아니라 "조직 손상의 누적"**임.

| 누적의 종류 | 무엇이 쌓이는가 | 결정자 | 카드 |
|---|---|---|---|
| **약물 누적 (plasma)** | 약물 농도 | $\tau/t_{1/2}$ | M3 |
| **조직 손상 누적** | 표적 조직의 미회복 손상 | $\tau$ vs 조직 회복 시간 | M10 |

표적 조직이 회복하지 못한 상태에서 다음 노출이 시작되면 손상이 쌓임. 그래서 회복 시간이 분할 간격보다 길면 plasma의 $R_{ac}$가 작은 경우에도 조직 손상은 누적될 수 있음. M7에서 부하 + 유지를 나눌 때도 **용량 크기만 보지 말고 분할 패턴과 회복 시간을 같이 봐야 하는 이유**가 여기 있음.

> ⚠️ **실무 함정 — 비교군 정의 오류**: 분할 독성 논문에서 비교군을 잘못 잡으면 결론 전체가 뒤집힘. Daptomycin Study A의 비교군은 정확히 **75 mg/kg q24h vs 25 mg/kg q8h**임 [R&T 5e pp.351–353]. 이걸 25 mg/kg q24h vs 25 mg/kg q8h로 오독하면 일일 총량이 3배 차이가 나니까 분할의 순수 효과를 분리할 수 없게 됨. 문헌에서 "same dose"라는 표현 만나면 **분자와 분모를 직접 계산해서 실제 일일 총량부터 확인하는 습관**이 필수임.

### 한 줄 마무리

같은 일일 용량 ≠ 같은 독성. 회복 시간이 분할 간격보다 길면 누적 손상이 발생함. *"same daily dose = same toxicity"*로 고정하면 조직 회복 시간이 누락되고 regimen 선택이 거꾸로 감.

---

<!-- SLIDE_START: §5 | title: §5 — 혼동 쌍 해부(Confusion Pair Dissection) -->
<!-- SECTION_CORE: SC-13 -->
# §5 — 혼동 쌍 해부(Confusion Pair Dissection)

여기는 본문에서 짚었던 **"헷갈리기 쉬운 자리"**를 표 형태로 한 번에 모아두는 자리임. 보고서 작성하기 직전에 한 번씩 훑어보면 되는 체크리스트로 쓸 것. 위험한 혼동은 *"기호가 비슷해서"*만 생기지 않음. 더 자주 생기는 원인은 **결정자가 다른 질문을 같은 질문으로 취급하는 것**임. 이 §5의 일곱 쌍은 다 그 자리임.

## §5-쌍1. $C_{ss}$ vs $C_{av,ss}$ vs $A_{av,ss}$

| 비교 기준 | $C_{av,ss}$ | $A_{av,ss}$ |
|---|---|---|
| 단위 / 차원 | 농도 | 약물량 |
| 수식 내 위치 | $F\text{Dose}/(CL\tau)$ | $1.44F\text{Dose}t_{1/2}/\tau$ |
| 변화 원인 | $CL$, $F$, dose, interval | $MRT$, $t_{1/2}$, dose, interval |
| 혼동 시 임상 결과 | TDM target 왜곡 | body burden을 농도 target으로 오독 |

세 항목을 한 번에 분리하면:

| 항목 | 정확한 분리 | 왜 중요한가 |
|---|---|---|
| $C_{ss}$ | 정속 주입 plateau 농도: $R_{in}/CL$ | infusion 유지 target |
| $C_{av,ss}$ | 다중투여 간격 평균 농도: $F\text{Dose}/(CL\tau)$ | TDM/노출-반응 target |
| $A_{av,ss}$ | plateau 평균 약물량: $1.44F\text{Dose}t_{1/2}/\tau$ | residence time/body burden |

$$
\overbrace{\underbrace{C_{ss}}_{\text{plateau}}}^{\text{infusion}},\quad \overbrace{\underbrace{C_{av,ss}}_{\text{평균농도}}}^{\text{multi-dose}},\quad \overbrace{\underbrace{A_{av,ss}}_{\text{평균량}}}^{\text{body burden}}
$$

**가장 치명적인 자리**: $1.44F\text{Dose}t_{1/2}/\tau$를 농도 식으로 쓰면 단위가 틀림. **1-구획에 알려진 $V$가 같이 명시되지 않으면 약물량-농도 변환은 성립 안 함** [R&T 5e p.324; R&T 5e p.337].

물 비유로 다시 한 번 잡고 가자. $C_{av,ss}$는 **욕조의 평균 수위**(mg/L), $A_{av,ss}$는 **욕조 안 물의 평균 양**(mg), $C_{ss}$는 **수도꼭지를 정해진 속도로 열어둔 정상상태의 수위**임. 같은 욕조($V$ 알려짐, 1-구획)에서만 *"수위 = 물의 양 / 욕조 크기"*라는 다리가 놓임. 욕조 모양이 바뀌면(다구획) 같은 양의 물이라도 수위가 달라짐.

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

**가장 치명적인 자리**: 정상상태 플래그는 *"편의상 넣는 옵션"*이 아니라 **초기 조건을 수학적으로 바꾸는 명령**임. 투여 이력이 plateau 조건을 만족 안 하면 안 씀.

기억 고리 한 줄. `SS=1`은 **"옛날부터 같은 dose가 충분히 반복됐다"**고 NONMEM에 알리는 **과거형 깃발**임 — 직전 사건만이 아니라 무한 과거의 같은 패턴이 누적된 결과를 가정함. `SS=2`는 **"지금 이 순간 정상상태 입력이 진행 중"**임을 알리는 **현재진행형 깃발**임 — bolus가 아니라 input function이 plateau 조건을 채웠다고 가정함. 두 깃발 모두 **시제(時制)를 잘못 꽂는 순간 NONMEM이 존재하지 않는 history를 만들어냄.**

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
\overbrace{\underbrace{K_a>K}_{\text{일반형}}}^{\text{absorption이 빠름}}\Rightarrow\text{terminal slope}\approx K,\qquad \overbrace{\underbrace{K_a<K}_{\text{flip-flop}}}^{\text{absorption이 느림}}\Rightarrow\text{terminal slope}\approx K_a
$$

**가장 치명적인 자리**: 말단 기울기만 보고 elimination 반감기를 확정하면 안 됨. **투여경로 → 제형 → 흡수 지속시간**이 먼저임 [G&W 5e pp.45–46].

수도꼭지/배수구 비유로 정리해보면 — **Ordinary**는 배수구가 크고(빠른 elimination, $K$ 큼) 수도꼭지는 작음(느린 absorption). 그래서 입력이 끝나면 배수구가 빠르게 비워서 **배수구 속도($K$)**가 terminal slope를 그림. **Flip-flop**은 반대로 배수구가 작고(느린 elimination), 수도꼭지가 더 작음($K_a<K$). 입력이 길게 이어져서 **수도꼭지 속도($K_a$)**가 terminal slope를 만듦. 즉 terminal phase가 보여주는 건 항상 **"두 과정 중 더 느린 쪽의 속도"** — elimination이 아니라 **율속단계(rate-limiting; 전체 속도를 정하는 느린 단계)인 쪽**임.

---

## §5-쌍4. 도달 시간 vs 축적 정도 vs fluctuation

| 비교 기준 | 도달 시간 | 축적/진폭 |
|---|---|---|
| 단위 / 차원 | time | 무차원 배율 또는 농도 진폭 |
| 수식 내 위치 | $1-e^{-Kt}$ | $R_{ac}=1/(1-e^{-K\tau})$; $\tau/t_{1/2}$ |
| 변화 원인 | $t_{1/2}$, $K$ | 투여간격, 반감기 대비 interval |
| 혼동 시 임상 결과 | SS 도달 시점 오판 | dose/interval 조정 방향 오류 |

네 질문을 결정자 별로 분리:

| 질문 | 결정자 | 대표식 |
|---|---|---|
| plateau에 언제 도달함? | $t_{1/2}$ | $1-e^{-Kt}$ |
| 얼마나 축적됨? | $\tau/t_{1/2}$ | $R_{ac}=1/(1-e^{-K\tau})$ |
| 평균 수준은 어디임? | $CL$과 평균 입력률 | $C_{av,ss}=F\text{Dose}/(CL\tau)$ |
| peak-trough 진폭은? | $\tau/t_{1/2}$ | 투여간격이 길수록 커짐 |

$$
\overbrace{\underbrace{1-e^{-Kt}}_{\text{도달률}}}^{\text{시간 (clock)}},\quad \overbrace{\underbrace{R_{ac}}_{\text{축적계수}}=\frac{1}{1-e^{-K\tau}}}^{\text{배율 (ratio)}},\quad \overbrace{\underbrace{C_{av,ss}}_{\text{평균수준}}=\frac{F\text{Dose}}{CL\tau}}^{\text{무게중심 (centroid)}}
$$

**가장 치명적인 자리**: 용량을 두 배로 하면 농도 수준은 올라가지만 **$R_{ac}$ 자체는 안 바뀜**.

이 챕터 전체의 척추를 한 번 더 잡고 가자. 같은 약물에 손을 댈 때 **어느 자(scale)를 움직이려는지** 먼저 묻는 게 숙련자의 첫 질문임. **도달 시간**($1-e^{-Kt}$)은 **시계** — $t_{1/2}$로 똑딱임. **축적 정도**($R_{ac}$)는 **배율** — $\tau/t_{1/2}$로 결정되고 dose 크기와 무관함. **평균 농도**($C_{av,ss}$)는 **무게중심** — $CL$과 평균 입력률이 정함. **진폭**(peak-trough swing)은 **출렁임** — 같은 평균이라도 $\tau/t_{1/2}$가 클수록 큰 파도가 됨. **네 개의 자가 같은 약 한 방울에서 갈라져 나가는 것**임.

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

**가장 치명적인 자리**: **넓은 치료역이랑 높은 치료지수는 같은 문장이 아님.** 전자는 농도 경계의 문제, 후자는 노출 변화에 대한 안전 여유/민감도의 문제임 [R&T 5e pp.272–278].

자(ruler)와 떨림(tremor)으로 정리하면 — **Therapeutic Window**는 농도라는 **자 위에 그어놓은 두 선** — $C_{lower}$와 $C_{upper}$로 정의되는 **공간**의 문제임. 넓은 window는 두 선 사이가 멀다는 뜻일 뿐임. **Therapeutic Index**는 그 **선의 굵기(전임상 ratio)**거나 **환자의 손떨림(임상 노출 민감도)**임. 같은 두 선을 그어놓은 자라도 손이 떨리는 환자(높은 변동성)에선 효과적인 자가 못 됨. 즉 TW는 **공간 척도**, TI는 **변동성/민감도 척도**. **wide TW + low TI 환자는 임상에서 아주 흔한 시나리오**인데, 두 개념을 같다고 보면 이 환자군 전체가 안 보임.

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
\overbrace{\underbrace{MRT}_{\text{MRT}}}^{\text{moment-based}}=\frac{\overbrace{\underbrace{AUMC_{0-\infty}}_{\text{AUMC}}}^{\text{first moment}}}{\overbrace{\underbrace{AUC_{0-\infty}}_{\text{총 AUC}}}^{\text{zeroth moment}}}
$$

**가장 치명적인 자리**: $1.44t_{1/2}$는 1차 선형 시스템의 시간척도일 뿐임. **어느 구획의 농도를 대표하는지는 모델 구조가 정함** [R&T 5e p.289; R&T 5e pp.299–304].

$t_{1/2}$는 **곡선의 기울기**가 만든 시간임 — *"절반이 될 때까지"*라는 곡선 모양에 종속된 척도. MRT는 **곡선 아래 면적의 무게중심** — 분자 한 개가 평균적으로 머문 시간을 묻는 moment-based 척도임. 두 척도는 **1-구획에서만 우연히 깔끔한 비율**($MRT=1.44\,t_{1/2}=V/CL$)로 일치함. 다구획에서는 분자가 central → tissue → central을 왕복하니까 MRT가 단순 $V/CL$로 환원이 안 됨. 즉 $1.44\times t_{1/2}$를 어느 구획의 시간척도로 바로 옮기는 순간 **moment를 slope로 압축**하는 차원 함몰이 일어남.

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

**가장 치명적인 자리**: 효과 감소가 보인다고 다 tolerance가 아님. 항균제에서는 resistance selection이, **nitrate**(혈관확장제, 협심증), **nicotine**(중추신경 작용제), **nifedipine**(칼슘채널 차단제, 고혈압)에서는 PD 적응이 핵심일 수 있음 [R&T 5e pp.346–348].

한 줄로 잡으면 — **Acquired Resistance는 "적이 변한 것"**임. 표적 미생물·세포 population이 선택 압력 하에 mutation이나 clonal shift로 약물에 둔감해진 것임. 약물도 환자도 그대로지만 표적이 다른 표적이 됨. **Tolerance는 "내가 변한 것"**임. 환자/시스템(수용체 downregulation, 항상성 feedback)이 같은 약물에 적응한 것임. 표적은 그대로지만 내 반응이 약해진 것. 임상 관리도 정반대로 감 — resistance는 **노출 패턴(MIC 회피, AUC/MIC 확보)**으로, tolerance는 **drug holiday, modified-release, rate-of-change 제어**로 다룸. **"효과가 떨어진다"는 같은 표면 증상에서 두 메커니즘은 정반대 방향의 처방을 만듦**.

---

<!-- SLIDE_START: §7 | title: §7 — 자기 테스트 모듈(Self-Test Module) -->
<!-- SECTION_CORE: SC-14 -->
# §7 — 자기 테스트 모듈(Self-Test Module)

이 챕터의 카드들을 머리에 단단히 박았는지 확인하는 자가 점검 영역임. **회상(recall) → 적용(application) → 보스 딜레마(boss dilemma)** 세 단계로 구성됨.

## §7-회상 영역(Recall Layer)

### Q1. 정속 주입에서 $C_{ss}$를 결정하는 파라미터는?
**답**: $C_{ss}=R_{in}/CL$이므로 plateau 농도 수준은 **청소율과 입력률**이 정함 [G&W 5e p.23; R&T 5e p.288].

### Q2. 90% plateau에 도달하는 데 필요한 시간은 대략 몇 half-lives인가?
**답**: 약 3.3 half-lives, 실무적으로 3–4 half-lives [G&W 5e p.22; R&T 5e p.291].

### Q3. 다중투여 축적계수에 dose가 안 들어가는 이유는?
**답**: 같은 dose가 반복될 때 잔여분의 비율은 $e^{-K\tau}$이고, 반복합은 등비수열이라 ratio가 **$\tau/t_{1/2}$에만** 의존함 [G&W 5e pp.44–45; R&T 5e pp.795–797 Appendix I].

### Q4. $C_{av,ss}$와 $A_{av,ss}$의 차원은 각각 무엇인가?
**답**: $C_{av,ss}$는 농도, $A_{av,ss}$는 약물량임. **$A_{av,ss}$를 농도처럼 쓰면 차원 오류** [R&T 5e p.324; R&T 5e p.337].

### Q5. Flip-flop에서 말단 기울기는 무엇을 반영하는가?
**답**: $K_a<K$이면 말단 기울기가 **흡수속도**를 반영함 [G&W 5e pp.45–46].

---

## §7-적용 영역(Application Layer)

### Q6. 어떤 약물의 $t_{1/2}=8$ h이고 q24h 투여함. 축적은 큼?
**답**: $\tau/t_{1/2}=3$이므로 $R_{ac}=1/(1-2^{-3})\approx1.14$로 별로 안 큼. q24h라도 half-life 대비 interval이 길면 축적은 작음.

$$
\overbrace{\underbrace{\tau/t_{1/2}}_{3}}^{\text{interval/반감기}}\Rightarrow \overbrace{\underbrace{R_{ac}}_{\text{축적계수}}=\frac{1}{1-2^{-3}}\approx1.14}^{\text{거의 1}}
$$

### Q7. 같은 일일 용량을 q24h에서 q8h로 바꾸면 무엇이 변하는가?
**답**: 평균 입력률이 같으니까 **$C_{av,ss}$는 원칙적으로 같음. 다만 peak-trough 변동은 줄어듦.** 단, 독성이 회복 시간/분할에 의존하면 결과가 달라질 수 있음 [R&T 5e p.325; R&T 5e pp.351–353].

### Q8. $C_{av,ss}=F\text{Dose}/(CL\tau)=1.44F\text{Dose}t_{1/2}/\tau$라고 쓴 문장을 교정할 것.
**답**: 앞 식은 농도, 뒤 식은 약물량임. 정확히는 $C_{av,ss}=F\text{Dose}/(CL\tau)$이고 $A_{av,ss}=1.44F\text{Dose}t_{1/2}/\tau$. **1-구획에서만 $C_{av,ss}=A_{av,ss}/V$**임.

$$
\overbrace{\underbrace{C_{av,ss}}_{\text{평균농도}}=\frac{F\text{Dose}}{CL\tau}}^{\text{mg/L}}\quad\neq\quad \overbrace{\underbrace{A_{av,ss}}_{\text{평균량}}=\frac{1.44F\text{Dose}t_{1/2}}{\tau}}^{\text{mg}}
$$

### Q9. Phenobarbital 100 mg q24h, $t_{1/2}=4$ days에서 R&T 5e의 5.8과 식의 6.3을 어떻게 설명할 것인가?
**답**: 5.8은 $A_{av,ss}/Dose\approx5.76$에 해당하는 **평균 축적 비율**이고, peak/trough 축적 지수 $R_{ac}$는 R&T 5e Eq. 11-10 기준 약 6.3임. 둘을 같은 라벨로 쓰면 안 됨 [R&T 5e pp.324–326].

### Q10. Atorvastatin에서 PK plateau와 PD plateau가 다를 수 있는 이유는?
**답**: 혈장 농도의 반감기와 cholesterol turnover 반응의 시간척도가 다르기 때문임. Atorvastatin parent는 $t_{1/2}\approx14$ h, 활성 대사체(2-/4-hydroxy atorvastatin)는 약 20–30 h이지만, 최대 cholesterol 반응 plateau는 **LDL turnover 시상수**(약 14일, $k_{out}\approx \ln 2/14$일)가 정해서 3–4주가 걸림 — PD plateau의 시상수는 $\approx \ln 10/k_{out}$로 잠금됨 [R&T 5e p.343, Fig. 11-16].

### Q11. Daptomycin Study A에서 "같은 일일 용량" 비교군은 무엇인가?
**답**: **75 mg/kg q24h와 25 mg/kg q8h**임. 둘 다 75 mg/kg/day이고, CPK는 991 vs 3996 U/L로 달랐음. 단, 이 75 mg/kg/day는 **임상 daptomycin 용량(4–6 mg/kg/day)이 아니라 fractionation toxicity 분리를 위한 실험적 design dose**(개 모델)임을 함께 기억해야 함. 학습 메시지는 *"같은 daily dose ≠ 같은 toxicity"*의 개념임 [R&T 5e pp.351–353, Table 11-7].

### Q12. TW 알고리즘에서 $C_{upper}/C_{lower}$ ratio가 주로 결정하는 것은?
**답**: **허용 가능한 투여간격의 상한**임. $\tau_{max}=1.44t_{1/2}\ln(C_{upper}/C_{lower})$ [R&T 5e p.334].

---

## §7-보스 딜레마(Boss Dilemma)

### Q-BD. 새로운 경구 약물이 선형 PK를 보이고, $F=0.6$, $V=100$ L, $t_{1/2}=4$ h이며, 제안된 치료역이 1–4 mg/L라고 가정함. Phase 1 MAD 프로토콜을 IRB에 제출하려고 두 regimen이 검토 중임.

**Regimen A — 안정적 목표 유지(Steady aim)**:
$200$ mg q8h, **부하용량 없음**.
- 장점: $\tau=8$ h에서 $C_{max,ss}/C_{min,ss}$ 변동이 비교적 좁아 peak이 $C_{upper}=4$ mg/L를 안정적으로 유지 (peak safety 우선).
- 단점: plateau 도달까지 약 $3\text{–}4\times t_{1/2}=12\text{–}16$ h 동안 $C_{lower}=1$ mg/L 미달 구간 존재 — 초기 약 1 투여간격 동안 환자가 "효과 sub-window" 상태에 놓임.

**Regimen B — 빠른 도달 후 유지(Hit and hold)**:
$400$ mg loading + $200$ mg q8h maintenance.
- 장점: 첫 dose 직후 농도가 즉시 window 중앙 근처 — 효과 발현이 plateau 대기 시간 없이 시작 (time-to-effect 우선).
- 단점: $D_L=400$ mg 직후 $C_{max}$ 추정치는 $F\cdot D_L/V=0.6\times400/100=2.4$ mg/L로 $C_{upper}=4$ 이내이지만, **상부 95% CI**가 IIV 30%만 가정해도 $C_{upper}$를 일시적으로 침범할 수 있음.

Phase 1 프로토콜에서 어느 쪽을 채택하고, IRB 또는 FDA pre-IND 응답에서 그 선택을 어떻게 방어할 것인가? **이 문제는 가상 연습 문제임을 명시해야 함.**

**정답 — 상충 판단(Trade-off) 논리**:

이 문제는 단순 계산이 아니라 **두 충돌하는 최적화 목표** 사이의 양자택일임:
- **목표 X (peak safety)**: $C_{max}$가 $C_{upper}$를 절대 초과 안 함.
- **목표 Y (time to effect)**: 효과 sub-window 노출 시간을 최소화.

1. **사례 명시**: 이 문제는 교과서 등재 약물이 아닌 **가상 연습 문제**이고, 실제 Phase 1 프로토콜은 IIV·sample size·sparse sampling design을 동반한 model-based simulation으로 결정됨.

2. **$\tau_{max}$ 타당성 점검**: $\tau_{max}=1.44\times4\times\ln(4/1)\approx7.98$ h. 즉 q8h는 TW 알고리즘이 허용하는 **이론적 상한**에 거의 정확히 맞춰진 interval임. q12h는 window를 벗어남 [R&T 5e p.334]. 따라서 두 regimen 모두 q8h 채택은 정당함.

$$
\overbrace{\underbrace{\tau_{max}}_{\text{최대간격}}}^{\text{TW 한계}}=1.44\times\underbrace{4}_{t_{1/2}}\times\underbrace{\ln(4/1)}_{\text{TW 비}}\approx7.98\ \mathrm{h}
$$

3. **선택 — Regimen A를 원칙적 1차 선택으로 권고**:
   - **이유 ① (Phase 1 특수성)**: Phase 1 first-time-in-multiple-dose는 IIV가 아직 정량화 안 된 상태임. Regimen B의 peak이 IIV 가정에 따라 $C_{upper}$를 침범할 가능성이 있다면, **peak-safety가 time-to-effect보다 불확실성 우선순위에서 위**에 있음.
   - **이유 ② (M9 PD-driven plateau 가능성)**: 효과 plateau가 PK plateau가 아니라 turnover 시스템에 종속되는 약물이면, 부하용량으로 PK plateau에 빨리 도달해도 **효과 발현은 안 빨라짐** — Regimen B의 실익이 사라짐.
   - **이유 ③ (M5 flip-flop 가능성)**: Phase 1 단계에서 $K_a<K$ 가능성이 배제 안 됐다면 observed $t_{1/2}=4$ h가 elimination이 아닐 수 있음 — 부하용량 산정의 전제가 무너짐.

4. **Regimen B를 1차 선택으로 정당화하려면**:
   - 활성 대사체 없음, PD-driven plateau 부재, $K_a>K$ 확인이 in vitro/in silico로 사전 확보돼야 함.
   - IIV 추정치(또는 사전 분포)가 $C_{upper}$ 침범 위험을 받아들일 수 있는 수준임을 시뮬레이션으로 보여줘야 함.
   - 효과 발현 지연이 임상적으로 수용 불가능한 적응증(급성 항생제 등)이면 정당화하기 쉬움.

5. **IRB 응답 프레임**: 어느 쪽을 선택하든, 응답 문서는 **"우리는 X와 Y 중 X(또는 Y)를 우선시했습니다. 그 이유는 [Phase 1 단계의 IIV 미정량성 / 적응증의 효과 발현 임상 중요도]입니다"**라는 trade-off 논리를 명시해야 함. *"이 regimen이 안전하다"*라고 단정하면 두 목표를 동시에 만족시킬 수 있다는 잘못된 함의를 줌.

6. **알고리즘 적용 중단 조건**: 선형 PK 비성립, 즉각적 농도-반응 깨짐, PD plateau가 turnover 지배, flip-flop, 단회 투여 치료 — 이 중 하나라도 의심되면 TW 알고리즘은 타당성 점검에서 끝내고 모델 확장으로 돌아감.

§7의 핵심 한 줄: **계산 문제의 핵심은 숫자를 넣는 게 아니라 "어떤 식이 어떤 조건에서만 유효한가"를 먼저 잠그는 것**임.

---

<!-- SLIDE_START: §8 | title: §8 — 메타프레임 & 전체 그림 -->
<!-- SECTION_CORE: SC-15 -->
# §8 — 메타프레임 & 전체 그림

## §8A — 위치 설정

Session 07이 만드는 건 pharmacometrics의 **"steady-state 문법"**임. 이전 세션의 단회 투여 PK가 시간-농도 곡선의 기본 모양을 줬다면, 이 세션은 그 곡선을 **반복·유지·제약하는 법**을 줌. 이후 TDM, PopPK 공변량 해석, 노출-반응, Phase 1 MAD 설계는 전부 이 문법 위에 올라감.

---

## §8B — 의존성과 실패 모드

이 세션을 잘못 잡으면 어디서 실패가 나는지를 한 표로 잠궈둠:

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

전문가의 해자는 복잡한 식을 많이 외우는 데 있지 않음. **같은 regimen 질문을 다음 결정자 표로 즉시 분해**하는 능력이 해자임:

| 질문 | 결정자 | 대표 사용처 |
|---|---|---|
| 목표 평균 농도는? | $CL$, 평균 입력률 | 유지용량, TDM |
| 목표에 얼마나 빨리 도달함? | $t_{1/2}$ | washout, Day-to-SS, sampling 일정 |
| peak-trough 진폭은? | $\tau/t_{1/2}$ | 투여간격, 순응도, 독성 |
| loading이 필요함? | target onset, $V/F$, $R_{ac}$ | urgent therapy, bolus+infusion |
| TW 안에 머무름? | $C_{upper}$, $C_{lower}$, $V/F$, $t_{1/2}$ | 투여 설계 |
| 효과가 늦게 옴? | turnover/세포 수명 | statin, EPO, 간접 반응 |
| 제형이 terminal slope를 바꿈? | absorption/input duration | MR/depot/flip-flop |
| 독성이 회복 시간에 의존함? | 분할, 최소 노출 지속시간 | daptomycin류 |

> 💼 **실무 인사이트**: 이 표는 규제 제출 문장을 대신 쓰는 게 아니라, **교과서 수식을 제출 가능한 정량 논리로 번역하는 내부 검토 틀**임.

변화가 들어왔을 때 어디부터 봐야 하는지 1차 진단표:

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| 목표 평균 농도 변화 | $CL$, 평균 입력률 | → | 유지용량 변경 | $R_{in}$ 또는 $D_M/\tau$ 재계산 |
| 도달 시간 지연 | $t_{1/2}$ | → | sampling·washout 일정 변경 | 3–4 half-lives 기준 확인 |
| peak-trough 진폭 과다 | $\tau/t_{1/2}$ | → | 독성 또는 trough failure | 투여간격 재설계 |
| 효과 plateau 지연 | turnover/세포 수명 | → | 효과 평가 시점 오류 | PD endpoint timing 분리 |

---

## §8D — 28세션 항법

이 세션이 잠그는 건 네 가지임:

| 후속 세션 | 이 세션에서 열리는 개념 | 이 세션 없으면 실패하는 것 |
|---|---|---|
| TDM | $C_{ss}=R_{in}/CL$와 $C_{av,ss}$ | 농도 보정에서 $CL$·입력률·sampling time 혼동 |
| PopPK 공변량 해석 | $CL$, $V$, $t_{1/2}$, $\tau/t_{1/2}$ 분리 | 공변량 효과를 level·timing·fluctuation에 잘못 연결 |
| 노출-반응 | TW, PD plateau, turnover clock | PK plateau를 효과 plateau로 오독 |
| Phase 1 MAD 설계 | 축적, 부하/유지, 분할 | `SS=1`, interval, 독성 회복 판단 실패 |

다음 세션으로 넘어갈 때 **이 한 문장만 들고 가면 됨**:

> **"항정상태는 하나의 숫자가 아니라, 시간 · 수준 · 진폭 · 임상제약을 따로 분리해서 다시 조립하는 작업임."**

이 한 줄이 hook의 phenobarbital trough도, daptomycin CPK 4배 차이도, 그리고 앞으로 만날 TDM 조정, PopPK 공변량, Phase 1 MAD 설계도 같은 문법으로 읽히게 해줌.

<!-- Remastered 변경 사항 노트
원본: 07_T_치료역_항정상태_다중투여_축적_v4_0_보강본_final.md (v4.0 보강본_final)
재구성: 콘텐츠 범위·출처·수식·section markers 100% 보존, 강의 동선만 재설계

[핵심 재구성 원칙]
1. "세 개의 자(rulers)" 마스터 메타포를 챕터 전체의 척추로 명시화
   - §0에 챕터 cheat-code 한 줄로 박아둠 (시계/무게중심/출렁임)
   - 모든 카드 첫 줄에 "잠그는 자(ruler)" 라벨 명시
   - §5-쌍4에서 네 개의 자(시계·배율·무게중심·출렁임)로 마무리 한 번 더

2. 카드를 묶음 ①(M1-M5 PK 시계) / ②(M6-M8 설계 다리) / ③(M9-M10 PD 시계) 구조로 명시 분리
   - 각 묶음 진입부에 한 줄 transition 추가
   - M3을 [⚡Apex Concept]로 더 강조

3. 카드 내부 동선 통일: 잠그는 자 → 한 줄 cheat → 정의/수식 → 비유 → 임상 anchor → 함정 → 한 줄 마무리
   - "거장의 시각" 박스를 본문 흐름에 자연스럽게 녹임
   - "한 줄 마무리"로 다음 카드 transition 명료화

4. 비유 라이브러리 통일: 욕조(M1, M4) / 엘리베이터(M2) / 저금통(M3) / 수도꼭지·배수구(M5, §5-쌍3) / 자동차 가속·크루즈(M7) / 운전 차선(M8) / 운동과 회복(M10)
   - 같은 욕조 비유가 M1과 M4에서 일관되게 연결되도록 명시

5. 어미 음슴체 전환 (~함, ~것임, ~음)
   - 강의체 호흡은 유지하되 문장 종결은 음슴체로 통일

[보존 사항]
- SLIDE_START 마커 15건 (모두 보존)
- SECTION_CORE 마커 15건 (SC-01 ~ SC-15 모두 보존)
- 모든 약물명·핵심 수치·출처 anchor (R&T 5e, G&W 5e, Oleson 2000) 보존
- 카드 ID M1–M10, C1–C12 보존
- §5 혼동쌍 7쌍, §7 Q1–Q12 + 보스 딜레마, §8 메타프레임 보존
- v4.0 보강본의 모든 신규 절(M3-B′, M3-E, M6-D′, M6-E, M7-D′ TCI, M9-A′, M10-A 경고) 보존
- 모든 overbrace/underbrace 양방향 annotation 보존 및 신규 추가
- 본문 산문, 비유, 임상 anchor 텍스트 의미 100% 보존하면서 어미·동선만 재구성
-->

---

C-260517-122734-Q3M

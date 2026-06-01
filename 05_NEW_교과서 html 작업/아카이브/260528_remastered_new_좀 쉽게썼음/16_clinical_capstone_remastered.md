# 세션 16 — 임상 통합 캡스톤 [REMASTERED]
## "한 환자의 dose를 결정한다"는 사건을 다섯 마디로 푸는 법

---

## 프롤로그 — 책상 위에 환자 차트 한 장 올려두고 시작함

자, 시작 전에 사건 하나 깔아두고 가자. 오늘 강의 내내 이 환자한테 돌아옴.

> **사건 — PK35 digoxin 케이스**
> 55세 남자, 60 kg, **CHF(심부전)**. **Lanoxicap (digoxin) 0.2 mg 매일 복용 중**. 어제 두 번 채혈했음 — **458시간 시점에 2.5 µg/L, 21시간 뒤(479시간)에 0.9 µg/L**. Bayesian TDM 소프트웨어가 이 환자의 개인 추정값으로 **$CL$ 5.7 L/h, $V$ 119.6 L, $t_{1/2}$ 14.5 h**를 내놓음. 그런데 population prior는 **$CL_{pop}$ 1.8 L/h, $V_{pop}$ 500 L**. → **$CL$이 3배 늘고, $V$는 1/4로 줄어든 셈** [Gabrielsson & Weiner 5e, PK35 Bayesian model — Digoxin, pp.641–643].

이 숫자 그대로 처방전에 옮기기 전에 던져야 할 질문은 단 하나임 —

**"이 두 점의 채혈이, 정말로 이 환자의 $CL$을 식별할 수 있는 정보였나?"**

이 한 줄이 오늘 강의의 손잡이임. 모양 읽기부터 monitoring 결정까지 이 질문 하나로 다 꿰어짐. 그리고 답을 미리 흘리자면 — **"그 시점의 채혈로는 $CL$이 식별 안 됨. 그럼에도 처방을 바꿔야 한다면 어떻게 할 거임?"** 이게 임상가-모델러의 차이임.

> ⚠️ **시작하자마자 짚고 갈 caveat — 두 개의 t₁/₂가 있음** `[교과서 외 임상 실무 갱신]`
> 위 prior 숫자로 단순 환산하면 모집단 $t_{1/2,\,pop} = 0.693 \cdot V_{pop}/CL_{pop} \approx 192$ h ≈ **약 8일**임. 그런데 임상 표준 digoxin $t_{1/2}$는 **약 36 ± 8 h** (정상 신기능 성인) [Rowland & Tozer 5e, Table 18-7, p.598]. 둘이 5배 넘게 차이남.
>
> 헷갈리지 말 것. PK35의 1.8 L/h·500 L는 **"이 환자 posterior가 prior에서 얼마나 떨어졌는지 보여주려고 책에 깔아둔 학습용 anchor"**임. 36 h는 **실제 임상에서 dosing interval과 sampling time을 잡을 때 쓰는 작업 기준**임. PK35의 prior 숫자를 "digoxin의 임상 PK"로 외우면 안 됨.
>
> $$
> \underbrace{t_{1/2,\,pop}}_{\text{PK35 학습용 prior}}
> = \frac{\overbrace{0.693}^{\ln 2}\cdot\underbrace{V_{pop}}_{500\,\mathrm{L}}}{\underbrace{CL_{pop}}_{1.8\,\mathrm{L/h}}}
> \approx \underbrace{192\,\mathrm{h}}_{\text{학습용}}
> \;\;\neq\;\;
> \underbrace{36\pm 8\,\mathrm{h}}_{\text{R\&T Table 18-7 임상 표준}}
> $$

---

## §0 — 다섯 마디 척추, 한 줄로

오늘 강의가 풀어내는 사슬은 정확히 이거임. 외울 거 다른 거 없음.

```
[모양 읽기]      → 어떤 모델 후보가 살아 있나?       (Ch.6)
[환자 보정]      → 이 환자는 왜 population에서 벗어났나? (Ch.15)
[개인 추정]      → 농도와 prior로 어떻게 묶어 추정하나? (PK35)
[처방 결정]      → 어디서 monitoring을 시작하고, LD/MD를 어떻게 가르나? (Ch.18)
[노출 보고]      → 선택된 용량의 exposure와 safety margin은? (PK15)
```

시간 없으면 **§1 → §3 → §2 → §4 → §5** 순서로 봐도 됨. 척추 중에서도 척추는 §2와 §3임 — **"왜 벗어났는가"** + **"posterior가 진짜 그 환자를 잡았는가"**, 이 두 마디.

**오늘 내내 머리에 박아둘 네 줄 분리 원칙** — 이게 안 박혀 있으면 어떤 카드도 따로 노는 느낌이 남.

1. **모양은 신호지 증명이 아님.** plot으로 모델 후보를 줄이는 거지, 모델을 확정하는 게 아님.
2. **$f_e$(약물)와 $RF$(환자)는 다른 축.** 같은 신부전이라도 약마다 dose 조정 크기가 다름.
3. **LD는 $V$, MD는 $CL$.** 같이 처리하면 사고남.
4. **측정 가능 ≠ 해석 가능.** dosing history와 sampling time 없이는 농도는 그냥 숫자임.

---

## 소스 범위

- **Gabrielsson J, Weiner D.** *Pharmacokinetic and Pharmacodynamic Data Analysis: Concepts and Applications*, 5th ed., Apotekarsocieteten, Stockholm, 2016.
  - Ch.6 Pattern Recognition [Gabrielsson & Weiner 5e pp.423–466]
  - PK15 Toxicokinetics [Gabrielsson & Weiner 5e pp.546–548]
  - PK35 Bayesian model — Digoxin [Gabrielsson & Weiner 5e pp.641–643]
- **Rowland M, Tozer TN.** *Clinical Pharmacokinetics and Pharmacodynamics: Concepts and Applications*, 5th ed., Wolters Kluwer / Lippincott Williams & Wilkins, Philadelphia, 2011.
  - Ch.15 Disease [Rowland & Tozer 5e pp.443–489]
  - Ch.18 Initiating and Managing Therapy [Rowland & Tozer 5e pp.577–610]

---

# §1 — 첫째 마디: 모양으로 후보 좁히기

## §1.1 — 모양 읽는 순서는 정해져 있음

새 response-time plot 앞에 앉으면, 머릿속에서 모델 이름부터 튀어나오는 게 사람의 본능임. **그걸 누르고 묘사부터 해야 함.** 묘사 순서가 이미 정해져 있음.

```
1. Baseline  — 안정한가? 흘러가는가? 진행/적응 흔적이 있나?
2. Delay     — 농도 peak과 response 극값이 분리되나?
3. Peak-shift— 용량 올리면 극값이 좌/우로 움직이나?
4. Saturation— 고용량에서 flat 구간이 보이나?
5. C-R plot  — direct / indirect / rebound / tolerance / hysteresis 중 누가 남나?
```

**왜 이 순서냐면.** baseline이 흐르거나 adaptation/rebound가 있는데 direct-effect 모델로 fitting 시작하면, 모델은 통과해도 해석은 처음부터 틀어짐. 이 순서로 묘사를 거친 다음에야 비로소 **"어느 모델을 후보에 남길지"**가 보임 [Gabrielsson & Weiner 5e Ch.6 Fig.6.1, p.423; Fig.6.12 pp.465–466].

> 💡 **모양 먼저 원칙.** plot 보자마자 "이건 turnover네"라고 말하지 말 것. baseline → delay → peak-shift → saturation 순서로 묘사부터 함. 후보를 빨리 줄였다고 해서 모델이 검증된 건 아님. fitting, diagnostics, sampling adequacy가 뒤에 줄줄이 남아 있음.

**실무에서 가장 자주 보는 함정 하나.** "PopPK 모델만 통과하면 posterior, TDM, dosing decision은 소프트웨어가 알아서 처리한다"는 믿음. 이게 무서운 이유 — Bayesian TDM 소프트웨어는 어떤 sampling이든 posterior mean을 출력해줌. 그래서 그럴싸한 숫자가 항상 나옴. 하지만 sampling이 $CL$을 식별 못 하는 시점이면, 그 posterior는 **prior에 농도가 살짝 끌려간 환영**임. 그 환영으로 dose를 결정하면? → 식별 불가 posterior가 처방에 그대로 들어가서, 독성이나 치료 실패가 났을 때 "왜 그렇게 결정했냐"는 답을 못 함.

---

## §1.2 — Peak가 어디로 갔는가는 단서지 결론이 아님

용량 올렸을 때 trough가 좌측으로 이동했다고 해서 곧장 "이건 receptor on/off 모델"이라고 외워두면 안 됨. 같은 좌측 이동을 turnover의 loss stimulation도 만들 수 있음. **방향은 후보를 줄이는 1차 필터지, 모델 클래스를 확정하는 도장이 아님** [Gabrielsson & Weiner 5e pp.424–428].

| 관찰 패턴 | 가능한 해석 |
|---|---|
| plasma peak이 $R_{min}$ 도달 시간의 약 1/3에서 발생 | response delay 있음. direct-effect 단독 모델은 후보에서 거의 빠짐 |
| 고용량에서 trough가 **좌측** 이동 | turnover loss stimulation **또는** receptor on/off (둘 중 어느 하나로 단정 X) |
| 최고용량에서 trough **우측** 이동 + flat 구간 | saturation 동반 input inhibition 강한 후보 |

> 💡 **방향은 단서지 결론이 아님.** 좌측 이동을 곧장 "$k_{on}$이 큰 약물"로 읽으면, finite receptor pool 때문에 nadir가 빨라지는 turnover loss stimulation 후보를 그 자리에서 지워버림. 두 모델은 같은 모양인데 메커니즘이 다름.

**실무 팁.** 단일 용량의 response-time curve 하나로 mechanism 확정하지 말 것. **중요한 건 dose escalation에서 모양이 어떻게 바뀌느냐**임. 용량을 올렸을 때 peak가 옮겨가면 turnover나 finite-pool 후보, 거의 안 움직이면 effect compartment 후보. 이게 1차 분기점임 [Gabrielsson & Weiner 5e Fig.6.2 p.424, Fig.6.3 p.428].

---

## §1.3 — Delay가 어느 state에 박혔는가 — 세 prototype

후보 줄였으면 이제 그 후보가 ODE state에서 어떻게 갈라지는지 봐야 함. Ch.6의 Case A–I 식을 통째로 외우려 들지 말고, **delay가 $C_e$에 박혔나, $R$에 박혔나, $RC$에 박혔나** 이 한 질문만 던지면 세 prototype이 갈라짐.

### Prototype 1 — Effect compartment (delay가 $C_e$에 박힘)

Time-delay는 있는데 dose 올려도 peak-shift가 약함 → link 모델 의심.

$$
\underbrace{\frac{dC_e}{dt}}_{\text{$C_e$ 변화}}
=
\underbrace{k_{e0}}_{\text{평형 속도}}
\overbrace{\left(\underbrace{C}_{\text{혈장}}-\underbrace{C_e}_{\text{효과부위}}\right)}^{\text{농도 차}}
$$

💡 **비유.** Effect compartment는 혈장이라는 복도에서 실제 효과가 일어나는 방으로 약이 들어가는 **작은 대기실**임. 복도 농도가 이미 높아도 대기실 농도가 늦게 차면 반응도 늦게 옴. counter-clockwise hysteresis가 보이면 link 모델의 전형적 신호 [Gabrielsson & Weiner 5e p.426].

### Prototype 2 — Turnover model (delay가 $R$에 박힘)

baseline이 흐르거나 rebound/adaptation이 있음 → turnover 의심.

$$
\underbrace{\frac{dR}{dt}}_{\text{$R$ 순변화}}
=
\overbrace{\underbrace{k_{in}}_{\text{생성}}\cdot\underbrace{I(C)}_{\text{농도 조절}}}^{\text{input 모듈}}
-
\underbrace{k_{out}R}_{\text{소실}}
\qquad\text{또는}\qquad
\underbrace{\frac{dR}{dt}}_{\text{$R$ 순변화}}
=
\underbrace{k_{in}}_{\text{기본 생성}}
-
\overbrace{\underbrace{k_{out}R}_{\text{소실}}\cdot\underbrace{S(C)}_{\text{농도 자극}}}^{\text{loss 모듈}}
$$

💡 **비유.** Turnover는 **물탱크 = 수도꼭지 + 배수구**임. 약이 탱크 크기 자체를 바꾸는 게 아니라, 들어오는 속도나 빠지는 속도를 바꿔서 새 수위를 만듦. baseline $R_0=k_{in}/k_{out}$는 정적인 비율이 아니라 **동적 평형**이고, 새 평형까지 도달하는 속도는 주로 $k_{out}$이 정함.

### Prototype 3 — Receptor on/off (delay가 $RC$에 박힘)

finite receptor pool 위에서 binding/dissociation이 경쟁함.

$$
\underbrace{\frac{dRC}{dt}}_{\text{$RC$ 변화}}
=
\overbrace{\underbrace{k_{on}}_{\text{결합}}\underbrace{C}_{\text{농도}}\underbrace{(R_T-RC)}_{\text{free R}}}^{\text{결합 형성}}
-
\underbrace{k_{off}RC}_{\text{해리}}
$$

💡 **비유.** 자리(receptor)는 한정돼 있는 의자임. 약(C)이 의자 앉기 경쟁을 하는데, $k_{on}$이 빠르면 자리가 빨리 차고($RC$ 빨리 올라감), $k_{off}$가 빠르면 자리에서 빨리 일어남.

| state | $C_e$ | $R$ | $RC$ |
|---|---|---|---|
| 어디 박힘 | effect site로 가는 시간 | response system의 turnover | 결합/해리 경쟁 |
| 진단 단서 | counter-clockwise hysteresis | baseline drift, rebound, adaptation | dose 올리면 nadir 좌측 이동 + finite pool |
| 핵심 파라미터 | $k_{e0}$ | $k_{in}$, $k_{out}$ | $k_{on}$, $k_{off}$, $R_T$ |

> 🔑 **§1 한 줄 잠금.** Ch.6의 진짜 목적은 plot 모양으로 **모델 후보를 줄이는 것**임. 패턴은 증명이 아니라 분류 신호임. Case A–I 식 통째로 외우는 게 아니라, "delay가 어디 박혔는지"만 잡으면 세 prototype이 갈라지고, 그 다음 단계로 넘어갈 수 있음.

**다시 디곡신 케이스로.** 우리 환자는 농도 두 점만 있는 PK case임. PD response data가 없음. 그러니 §1의 모양 읽기 도구는 직접 적용 안 됨. 하지만 만약 이 환자의 심박수나 PR interval 같은 PD endpoint를 같이 모으게 된다면? — digoxin은 receptor-mediated인데 distribution이 느려서 hysteresis가 잘 보이는 약물임. Effect compartment prototype이 가장 먼저 후보에 올라옴. **이 감각이 §1의 진짜 실무 가치임** — "어떤 PD 모델을 처음부터 후보군에 둘 거임?"을 plot 보기 전에 미리 판단하는 것.

---

# §2 — 둘째 마디: 이 환자가 왜 population에서 벗어났나

## §2.1 — $f_e$와 $RF$를 분리해야 답이 보임

신부전 환자가 왔다 → "그럼 dose 줄여야지" — 이 한 줄로 가버리면 **약물별 신장 의존도를 통째로 무시**하는 꼴임. 같은 신부전이라도 약마다 dose 조정 크기가 완전히 달라야 함. 이유 — 분리할 게 두 개이기 때문임:

- **$f_e$ = 미변화체 신장 배설분율 → 약물 속성.** drug마다 정해진 값.
- **$RF$ = typical 대비 환자 신기능 → 환자 속성.** 환자마다 다른 값.

이 둘을 곱한 게 renal contribution이고, 거기에 비신장 기여를 더하면 maintenance 요구량의 비율 $R_d$가 나옴.

$$
\underbrace{R_d}_{\text{유지용량 비율}}
=
\overbrace{\underbrace{RF}_{\text{환자 신기능}}\cdot\underbrace{f_e}_{\text{약물 renal}}}^{\text{renal 기여}}
+
\underbrace{(1-f_e)}_{\text{비신 기여}}
$$

$$
\underbrace{CL}_{\text{총 CL}}
=
\underbrace{CL_{non\text{-}renal}}_{\text{비신 CL}}
+
\overbrace{\underbrace{f_e}_{\text{renal 분율}}\cdot\underbrace{CL_{total}}_{\text{기준 CL}}\cdot\underbrace{RF}_{\text{환자 RF}}}^{\text{renal CL}}
$$

💡 **비유.** $R_d$는 **다이얼 두 개**임. 하나는 약이 원래 신장에 얼마나 의존하는지($f_e$), 다른 하나는 지금 이 환자 신장이 얼마나 남았는지($RF$). 두 다이얼을 같이 돌려야 답이 나옴.

**$f_e × RF$ 영역별 결정 테이블.**

| $f_e \cdot RF$ 영역 | 해석 | 모델링 함의 | 용량/TDM 지침 |
|---|---|---|---|
| < 0.1 | 신기능이 거의 기여 안 함 | $CL_{renal}$ 사실상 무시; 간/대사 covariate에 집중 | 신기능 기반 maintenance 조절 불필요 |
| 0.1–0.5 | 신기능이 부분 기여 | $CL = CL_{non-renal} + f_e \cdot CL_{total} \cdot RF$로 분리; $RF$ covariate 탐색 | 부분 maintenance 감량 + TDM으로 개별화 |
| > 0.5 | 신기능이 주된 경로 | $CL$이 $RF$에 강하게 의존; 신기능 covariate가 $\omega^2$ 주설명 변수 | 적극적 MD 감량; **LD는 $V$ 기반으로 별도 결정**; TDM 필수 |

> 🔑 **약물 × 환자 규칙.** $f_e$는 약물, $RF$는 환자. 둘을 분리하면 같은 신부전이라도 약마다 dose 조정이 왜 달라지는지 숫자로 보임. **그리고 $R_d$는 loading dose 공식이 아님** — $V$가 안 변하면 LD는 따로 판단해야 함. (§4.2에서 다시 옴.)

**우리 디곡신 환자에게는?** Digoxin은 $f_e \approx 0.6$–0.7로 신장 배설 분율이 큼. 그래서 CHF + 노인 + 신기능 감소 가능성이 있으면 maintenance dose는 $R_d$ 비례로 적극 감량 대상임. **하지만 LD는 별도** — digoxin uremia에서는 오히려 $V$ 자체가 감소하는 예외적 현상이 있어서, 단순히 LD까지 같이 줄이면 초기 농도 미달이 발생할 수 있음 [Rowland & Tozer 5e p.464].

**간 질환은 또 완전히 다른 축.** 간경변에서는 high-extraction 경구 약물이 portal bypass + first-pass loss 감소 → $F$가 올라가서 노출이 급격히 상승함. 반대로 low-extraction에 단백결합이 강한 약물에서는 $f_u$ 증가가 total $CL$을 높이긴 하는데, **unbound $CL$은 거의 안 변함**. → "간 질환 = 모든 $CL$ 감소"는 틀린 일반화임 [Rowland & Tozer 5e pp.444–446].

**실무 사례.** **phenytoin** — 단백결합 강함(albumin 결합) + low extraction. uremia, 수술, displacement drug가 있으면 $f_u\uparrow$. 이때 total 농도 target을 그대로 쓰면 같은 unbound exposure가 과소평가됨. 그래서 phenytoin에서는 $f_e/RF$ 분리만으로는 부족하고, **단백결합 변화까지 같이 봐야 함**. (§4.1 TCS criteria에서 다시 옴.)

---

## §2.2 — Cockcroft-Gault의 함정 — SCr은 지연된 거울

$RF$를 계산식에 넣으려면 입력값이 필요함. 그 입력값을 만들어주는 게 Cockcroft-Gault임. 그런데 **SCr 자체가 실시간 신기능을 보여주는 거울이 아님** — creatinine turnover가 반영된 지연 지표임.

$$
\underbrace{CL_{cr}}_{\text{CrCL 추정}}\,(\mathrm{mL/min})
=
\frac{\underbrace{(140-\text{age})}_{\text{연령}}\cdot\underbrace{WT}_{\text{체중}}}{\underbrace{72\cdot SCr}_{\text{SCr 보정}}}
\qquad
\text{(여성은 }\times 0.85)
$$

💡 **비유.** SCr은 **뒤늦은 거울**임. 오늘 거울을 봤다고 해서 오늘의 얼굴이 비치는 게 아니라, **며칠 전의 얼굴이 천천히 비쳐오는 상태**. 안정 상태에서는 거울이 맞지만, AKI처럼 신기능이 급변할 때는 거울이 며칠씩 뒤처짐.

**AKI에서 왜 위험하냐면.** 신기능이 급격히 떨어져도 SCr은 천천히 따라 올라감. Rowland & Tozer Table 15-6에 따르면 신기능이 떨어질수록 creatinine turnover time과 half-life가 길어짐 [Rowland & Tozer 5e pp.459–461]. → **오늘 측정한 SCr로 오늘의 $RF$를 과신하면, 처음 24–48시간 동안 독성이 쌓이는 걸 그대로 놓침.**

> 💡 **SCr은 뒤늦은 거울 — 두 가지 작업 분리.**
> ① 안정 상태 성인 → C-G가 $RF$ 입력값을 결정함. snapshot 계산 OK.
> ② AKI나 급성 변화 → SCr **trend**(어제 1.0, 오늘 1.6, 내일 2.2 같은 slope)를 같이 봐야 함. snapshot은 신뢰하지 말 것.

**실무 디테일.** 노인·근감소·비만·AKI 환자에서는 어떤 체중을 쓸지(IBW vs ABW vs adjusted)도 dose error의 주된 원인임. 이건 별도 학습 주제라 여기서는 짚고 넘어감.

---

## §2.3 — 투석은 hard threshold가 아님 — 좌표 평면으로 봐야 함

투석 중에 half-life가 짧아짐 → "그럼 보충 용량 줘야지" — 이 사고로 가버리면 **high-$V_u$ 약물을 과보충**하기 쉬움. 핵심은 half-life 단축이 아니라 **세션 동안 몸에서 빠진 양**임. 그리고 그 양은 좌표 평면 위에서 결정됨.

$$
\underbrace{k_D}_{\text{투석 중 제거}}
=
\frac{\overbrace{\underbrace{CL_u}_{\text{자체 CL}}+\underbrace{CL_{uD}}_{\text{투석 CL}}}^{\text{total uCL}}}{\underbrace{V_u}_{\text{unbound V}}},
\qquad
\underbrace{1-\exp(-k_D\cdot T)}_{\text{세션 동안 제거된 분율}},
\qquad
\underbrace{\frac{CL_{uD}}{CL_u+CL_{uD}}}_{\text{투석 기여 분율}}
$$

💡 **비유.** 투석은 **수영장에서 물을 퍼내는 펌프**임. 펌프 성능($CL_{uD}$)이 좋아도 수영장($V_u$)이 너무 크면, 3시간 동안 수위는 조금밖에 안 내려감.

**Rowland & Tozer Fig.15-18의 진짜 메시지.** high-flux 3시간 투석에서, unbound $V$가 약 120 L를 넘거나 환자 본인의 unbound clearance가 dialysis clearance보다 훨씬 크면 → dialysis가 제거하는 fraction은 20% 미만으로 작아질 수 있음 [Rowland & Tozer 5e pp.471–472]. **이건 hard AND gate가 아니라 연속적인 trade-off임.**

**실무 사례.** **phenobarbital**(고용량 진정·항경련제) — 투석 중 half-life는 크게 줄어도, 3시간짜리 single session으로는 몸 안의 양이 충분히 빠지지 않을 수 있음. → 반감기 단축 ≠ 세션 중 빠진 약물량.

**CAPD 대조.** CAPD clearance는 대부분의 약물에서 혈액투석 clearance보다 낮음. 그래서 "투석 환자"라는 라벨 하나로 용량 규칙을 묶을 수 없음 [Rowland & Tozer 5e pp.475–477].

> 🔑 **§2 한 줄 잠금.** 이 환자가 왜 population에서 벗어났는지를 설명하는 작업은 **$f_e$/$RF$/$R_d$ 분리 → SCr lag 점검 → 투석이라면 좌표 평면 위에서 판단**. 라벨 하나로 사고하지 말 것 — 모든 dose 조정은 "약물 속성 × 환자 속성"의 곱임.

---

# §3 — 셋째 마디: Bayesian으로 이 환자 잡기 (PK35 해부)

## §3.1 — Posterior는 줄다리기임

이제 우리 환자로 돌아옴. §2가 "왜 벗어났는가"의 **메커니즘**을 줬다면, §3은 그 환자의 **숫자**를 어떻게 추정하는지 말함.

Bayesian TDM은 관측 농도만 믿지도 않고, population average만 믿지도 않음. **농도 likelihood와 population prior의 상대적 variance**를 같이 봐서 둘 사이 어딘가에 posterior를 둠.

$$
\underbrace{OBJ_{Bayes}}_{\text{총 penalty}}
\approx
\underbrace{\sum_i\frac{\left(C_{obs,i}-\hat C_i\right)^2}{\operatorname{var}(\hat C_i)}}_{\text{농도 mismatch}}
+
\underbrace{\sum_j\frac{\left(P_{pop,j}-\hat P_j\right)^2}{\operatorname{var}(\hat P_j)}}_{\text{prior 이탈}}
$$

💡 **비유.** Bayesian TDM은 **두 사람의 줄다리기**임. 농도 자료 쪽 줄이 약하면 prior가 끌고, prior 쪽이 약하면 농도가 끔. **어느 줄이 더 튼튼한지는 variance가 정함.**

세 가지 시나리오로 정리됨:
- **농도 없음** → population average가 사실상 추정값. (개인 정보 0)
- **prior 없음** → maximum-likelihood concentration fitting. (생리학적으로 불가능한 $V/CL$ 나올 수 있음)
- **농도 + prior 다 있음** → complete Bayesian. (이게 정상 작동)

> 💡 **데이터 없음 vs 사전 지식 없음.** posterior mean은 항상 출력됨. 하지만 **그게 likelihood가 끌어서 나온 거냐, prior가 끌어서 나온 거냐**는 다른 문제임. 식별 가능한 정보 위에 있지 않은 posterior는 dose 결정의 근거가 아님.

---

## §3.2 — 우리 환자에게 무슨 일이 일어났는가

PK35 anchor를 다시 깔자:

> **PK35 디곡신 케이스 재확인** — 55세, 60 kg, CHF, Lanoxicap 0.2 mg daily, 458 h에 2.5 µg/L, 479 h에 0.9 µg/L. $CL_{pop}$ 1.8 L/h, $V_{pop}$ 500 L → 추정 $CL$ 5.7 L/h, $V$ 119.6 L, $t_{1/2}$ 14.5 h [Gabrielsson & Weiner 5e pp.641–643].

**여기서 먼저 짚을 디테일 하나.** 같은 0.2 mg이라도 제형에 따라 흡수되는 양이 다름:

| 제형 | $F$ (R&T Table 18-7) |
|---|---|
| Tablet | 0.70–0.75 |
| **Capsule (Lanoxicap)** | **0.95–1.00** |
| Elixir | 0.80 |

PK35 환자는 **Lanoxicap (capsule)** 임. tablet과 비교하면 **25–30% 더 흡수**되고 있음. LD/MD 계산에서 $F$를 무시하면 안 됨 [Rowland & Tozer 5e Table 18-7, p.598].

$$
\underbrace{D_L}_{\text{loading}}
= \frac{\overbrace{\underbrace{V}_{\text{분포}}\cdot\underbrace{C_{target}}_{\text{목표 농도}}}^{\text{필요 amount}}}{\underbrace{F}_{\text{제형 의존}}}
\quad\Rightarrow\quad
\underbrace{F_{\text{Lanoxicap}}\approx 0.95}_{\text{capsule}}
\;\neq\;
\underbrace{F_{\text{tablet}}\approx 0.72}_{\text{tablet}}
$$

---

## §3.3 — Sampling identifiability — "그 채혈로 $CL$이 식별 됐냐"

자, 이게 오늘 강의 전체의 손잡이 질문임. 답을 미리 흘렸음 — **그 두 점으로는 $CL$이 식별 안 됨.**

**왜?** Rowland & Tozer Fig.18-13의 메시지는 한 줄로 압축됨:

- **이른 sample(< 1×$t_{1/2}$)** → $V$에 더 민감.
- **늦은 sample / plateau / steady-state** → $CL$에 더 민감.
- **그래서** $1\times t_{1/2}$ 근처 sampling만으로는 $CL$ 1/3 변화와 $V$ 3배 변화를 **따로 구분할 수 없음.**

수식으로 보면 일찍 채혈한 시점에서는:

$$
\underbrace{CL\times\frac{1}{3}}_{\text{낮은 CL}}
\;\approx_{\text{early sample}}\;
\underbrace{V\times3}_{\text{큰 V}},
\qquad
\underbrace{t\geq 4\times t_{1/2}}_{\text{이 시점에야 CL 분리}}
$$

**$CL$을 정확히 추정하려면 $\geq 4\times t_{1/2}$ post-infusion 또는 steady-state 시점의 정보가 필요함** [Rowland & Tozer 5e pp.605–606].

**우리 환자의 458 h, 479 h 채혈은?** Digoxin의 임상 표준 $t_{1/2}$가 36 h이므로 458 h는 dose 시작 후 약 12–13 half-life 지난 시점. **이건 충분히 늦은 sample임** — 이론적으로 $CL$ 식별 가능 구간임. 그래서 PK35 posterior의 $CL = 5.7$ L/h는 **likelihood가 끌어준 숫자**로 봐도 됨.

**하지만 $V = 119.6$ L는?** 두 점 다 늦은 시점이고, distribution phase 정보가 전혀 없음. → $V$ 추정의 신뢰도는 **prior에 끌려간 영역**일 가능성이 큼. 119.6 L가 환자의 실제 $V$인지, prior(500 L)와 likelihood의 타협으로 떨어진 숫자인지 구별이 안 됨.

> ⚠️ **NONMEM 신호 해독 — 실패 모드 시그니처.** η-shrinkage on $CL$ > 30%, $V$는 < 15%, RSE($CL$) > 50%인데 fit이 통과한다? → 거의 확실하게 **"sampling time mismatch"** 신호임. 데이터가 식별 못 한 양을 추정한 결과임. 해결 — $V$를 strong prior로 고정하고 $CL$만 개별화하거나, $\geq 4\times t_{1/2}$ sample을 추가.

---

## §3.4 — 디곡신 치료영역 — 책 값 vs 현대 임상 기준

다시 우리 환자의 458 h 농도 2.5 µg/L를 보자. 이게 toxic인가 아닌가?

**책에서는** — Rowland & Tozer Table 18-7이 digoxin trough 치료영역을 **0.8–2 µg/L (Murphy)** 또는 **0.5–2 µg/L, CHF: 0.5–1 µg/L (Winter)** 로 인용 [Rowland & Tozer 5e p.598].

**현대 임상에서는** — **DIG trial post hoc analysis (Rathore et al., JAMA 2003)** 이후 심부전(HF)에서는 **목표 0.5–0.9 µg/L**, 0.9 µg/L 초과 시 사망률 증가가 관찰됨. AHA/ACC, ESC, 한국순환기학회 가이드라인 다 같은 방향으로 갔음.

$$
\underbrace{C_{target,\,DIG\text{-}trial}}_{\text{HF, post-2003}}
= \overbrace{0.5\text{–}0.9\,\mu\mathrm{g/L}}^{\text{현대 표준}}
\;\;\subset\;\;
\underbrace{0.8\text{–}2\,\mu\mathrm{g/L}}_{\text{R\&T Table 18-7 (Murphy)}}
$$

**그래서 우리 환자의 2.5 µg/L는?** 책 상한(2 µg/L)을 약간 넘은 정도가 아니라 — **현대 HF 기준에서는 명백한 toxicity range**임. CHF 환자에서 digoxin toxicity는 nausea, visual disturbance, arrhythmia(특히 ventricular)로 나타날 수 있음. **모니터링 → dose 결정 사슬이 막 시작된 셈임.**

> ⚠️ **R&T 책 값은 source-locked로 보존**하되, 임상 의사결정 시점에서는 **DIG trial 이후 기준(0.5–0.9 µg/L)** 을 함께 읽어야 함. 책 인용은 학습용, 처방은 현대 기준.

**경계 명시.** PK35는 $CL/V/t_{1/2}$ 추정 사례임. "Loading 0.4 mg, maintenance 0.1–0.125 mg/day"처럼 구체적 처방 문장은 교과서의 직접 권고가 아니라 `[교과서 외 통합 추론 예시]`로만 다룸. Sheiner 1977을 NONMEM의 직접 조상이라고 단정하는 표현은 `[확인 필요]` 영역.

> 🔑 **§3 한 줄 잠금.** Bayesian posterior는 **두 줄(농도 vs prior)의 줄다리기 결과**이고, 그 결과를 dose에 옮겨도 되는지는 **sampling이 그 파라미터를 진짜 식별했냐**에 달려 있음. posterior 숫자 자체에 대한 신뢰가 아니라, **그 숫자가 sampling geometry 위에서 식별 가능한가**가 질문임.

---

# §4 — 넷째 마디: Monitoring 결정과 처방

## §4.1 — TCS는 5개 순차 필터임 (병렬 체크리스트 X)

좋음, 우리 환자의 posterior를 얻었고 toxic range에 와 있다고 판단함. 그럼 routine monitoring을 도입할까? 이게 **Target Concentration Strategy(TCS)** 의사결정임.

**가장 흔한 오해 한 줄로.** "TCS 후보 약물이니까 농도 잰다" — 이 한 마디로 가버리면 **placebo monitoring**(잘 시키는데 결정을 못 바꾸는 모니터링)이 됨. TCS는 약물 이름 자동 적용이 아니라 **5개 기준의 순차 필터**임. 하나라도 막히면 결정 가치가 줄어듦 [Rowland & Tozer 5e pp.594–597].

```
필터 1. concentration-response 관계가 충분히 좋은가?
필터 2. therapeutic failure 가능성이 높은가? 
        (low TI, 큰 PK variability, 유전·질환·DDI 위험, nonadherence 가능성)
필터 3. PopPK 정보가 있는가?
필터 4. 신뢰할 만한 assay가 가능한가?
필터 5. assay 결과가 다음 처방 결정 *전에* 도착하는가?
```

**Table 18-5 후보군** — **cyclosporine, digoxin, gentamicin, nortriptyline, phenytoin, theophylline**. → 이름만으로 TCS가 필수라는 뜻은 아님. 5개 기준이 대부분 충족될 때 보조 전략으로 가치 있음 [Rowland & Tozer 5e Table 18-5, pp.595–596].

**Table 18-6 — "농도값 하나만으로는 해석 안 됨".** 완전한 농도 해석에 필요한 것 — dosing history, sampling time, previous concentrations, clinical status, renal/hepatic lab data, protein binding, concurrent drugs, assay method, usual PK parameters. **이게 다 갖춰져야 비로소 그 숫자가 해석 가능한 농도가 됨** [Rowland & Tozer 5e Table 18-6, p.597].

---

### Vancomycin TDM — 패러다임 시프트 (교과서 너머)

> ⚠️ **Trough에서 AUC₂₄/MIC로** `[교과서 외 임상 실무 갱신]`
> R&T Table 18-7은 vancomycin trough 5–15 mg/L를 표준 target으로 제시 [Rowland & Tozer 5e p.598]. 그런데 **2020 ASHP/IDSA/PIDS/SIDP joint consensus guideline (Rybak et al. 2020)** 이후로 표준은 **AUC₂₄/MIC ≥ 400** (목표 AUC₂₄ 400–600 mg·h/L, MIC 1 mg/L 가정)으로 이동.
>
> 이유 — trough 기반은 (a) AUC를 안정적으로 예측 못 하고, (b) 신독성과 더 강하게 연관됨. 현대 실무는 **Bayesian AUC estimation**(2 농도 포인트로 개별 AUC 추정).
>
> $$
> \underbrace{\text{Trough}\,5\text{–}15\,\mathrm{mg/L}}_{\text{R\&T 5e (2011)}}
> \;\xrightarrow{\text{2020 consensus}}\;
> \overbrace{\underbrace{AUC_{24}/MIC}_{\text{exposure index}} \;\geq\; \underbrace{400}_{\text{efficacy threshold}}}^{\text{현대 표준}}
> $$

---

### Phenytoin Sheiner-Tozer 보정 — 단백결합 변동의 정량 처리

> 🧪 **Sheiner-Tozer 정식 (보강본 정정 반영)** `[교과서 외 임상 실무 갱신]`
> R&T 5e가 "altered protein binding에서 target total을 같은 unbound에 맞추도록 조정해야 한다"는 **원칙**은 명시함 [Rowland & Tozer 5e p.596]. 그런데 임상에서 실제로 쓰는 **정량 보정식**은 Sheiner & Tozer (1979)의 다음 식임:
>
> $$
> \overbrace{
> \underbrace{C_{corrected}}_{\text{정상 alb 환산}}
> = \frac{\overbrace{C_{measured}}^{\text{측정 total}}}{\underbrace{0.2\cdot Alb_{(g/dL)}}_{\text{bound 항}}+\underbrace{0.1}_{\text{unbound 분율}}}
> }^{\text{Form A: Sheiner-Tozer 정식 (g/dL 입력)}}
> $$
>
> **검증** — 정상 albumin 4.4 g/dL 대입 시 분모 = $0.2\times 4.4 + 0.1 = 0.98 \approx 1$ ✓
>
> 정규화 비율로 입력하려면:
>
> $$
> \overbrace{
> C_{corrected}
> = \frac{C_{measured}}{\underbrace{0.9\cdot(Alb/4.4)}_{\text{정규화 bound}}+\underbrace{0.1}_{\text{unbound}}}
> }^{\text{Form B: 정규화 형태}}
> $$
>
> 검증 — $Alb=4.4$ 대입 시 분모 = $0.9\times 1 + 0.1 = 1.0$ ✓
>
> **신부전 변형 (Anderson)** — uremia에서는 단백결합 친화도 자체가 감소:
>
> $$
> \underbrace{C_{corrected,\,uremia}}_{\text{신부전 보정}}
> = \frac{\overbrace{C_{measured}}^{\text{측정 total}}}{\underbrace{0.1\cdot Alb_{(g/dL)}}_{\text{감소 bound}}+\underbrace{0.1}_{\text{unbound}}}
> $$

> 🔑 **TCS 한 줄 잠금.** TCS는 약물명 자동 적용 ❌, 5개 순차 필터 ⭕. 그리고 측정된 농도와 해석 가능한 농도는 다름 — dosing history + sampling time + clinical status가 다 갖춰져야 "해석 가능한 농도"가 됨.

---

## §4.2 — LD ≠ MD — 절대 같은 다이얼로 돌리지 말 것

자, monitoring 도입을 결정했다면 이제 dose 자체를 어떻게 바꿀지 결정해야 함. **여기서 가장 흔한 사고가 LD와 MD를 같이 처리하는 것**임. 둘은 다른 파라미터가 지배함.

$$
\underbrace{D_L}_{\text{loading dose}}
=
\frac{\overbrace{\underbrace{V}_{\text{분포 공간}}\cdot\underbrace{C_{target}}_{\text{목표 농도}}}^{\text{필요 amount}}}{\underbrace{F}_{\text{이용률}}}
$$

$$
\underbrace{D_M/\tau}_{\text{유지 dose rate}}
=
\frac{\overbrace{\underbrace{CL}_{\text{제거능}}\cdot\underbrace{C_{ss,avg}}_{\text{목표 평균 농도}}}^{\text{재공급량}}}{\underbrace{F}_{\text{이용률}}}
$$

💡 **비유.** LD는 **빈 욕조를 목표 수위까지 한 번 채우는 일**, MD는 **배수구로 빠지는 만큼 계속 채워넣는 일**. 욕조 크기가 그대로($V$ 안 변함)면 채우는 양도 그대로. 배수 속도($CL$)가 줄면 보충 속도도 줄여야 함. **이 두 작업은 따로 결정해야 함.**

| 작업 | 지배 파라미터 | 변하는 원인 |
|---|---|---|
| LD | $V$, $C_{target}$, $F$ | body size, tissue distribution, disease |
| MD | $CL$, $C_{target}$, $\tau$, $F$ | renal/hepatic function, interaction, disease |

**Fig.18-5 — 변동성 분할, prediction accuracy 아님.** 자주 헷갈리는 그림. Rowland & Tozer Fig.18-5는 **각 파라미터가 covariate로 얼마나 설명되는지의 비율**을 보여줌:

- $V$ → body weight 25% + age 10% + renal function 10% = **약 45% 설명, 55% 미설명**
- hepatic $CL$ → **약 40% 설명, 60% 미설명**
- renal $CL$ → renal function 50% + body weight 15% + age 15% = **약 80% 설명**
- $F$ → **약 5%만 설명**

→ 이건 "이만큼 정확하게 예측 가능"이 **아니라** "이만큼만 covariate로 설명되고 나머지는 IIV"라는 뜻 [Rowland & Tozer 5e p.582]. 자주 오독되는 그림임.

**임상 함의 테이블.**

| 상황 | 파라미터 변화 | 결과 | 조치 |
|---|---|---|---|
| Renal-CL dominant | $RF$가 $CL$ 강하게 설명 | maintenance 예측 가능성 ↑ | $RF/R_d$ 기반 MD 조정 |
| Hepatic-CL dominant | demographic으로 설명 안 되는 IIV ↑ | 개인 노출 불확실성 ↑ | TCS 기준 충족 시 monitoring 고려 |
| 이론적 LD가 매우 큼 | $V\cdot C_{target}$ 요구량 큼 | 단회 투여 독성/투여 가능성 문제 | divided loading 검토 |

> 💡 **신부전이라 LD도 줄인다 — 이 자동 규칙은 틀릴 수 있음.** LD는 $V$ 문제, MD는 $CL$ 문제. 다만 **digoxin uremia처럼 $V$ 자체가 줄어드는 예외**는 별도 잡음.

**우리 환자에게 적용.** 디곡신 toxic range(2.5 µg/L). HF target 0.5–0.9 µg/L. → **MD를 줄여야 함 (CL 작업)**. LD는 이미 들어간 약이 spread돼 있는 상태라 별 의미 없음. 만약 신기능 저하 의심이 있어 $RF$가 70% 정도라면, $f_e\approx 0.65$인 digoxin에서 $R_d \approx 0.65\times 0.7 + 0.35 = 0.81$. → MD를 약 80% 수준으로 적용. 동시에 dose hold하고 농도가 target range로 내려갈 때까지 기다리는 게 안전한 임상 동선.

(다시 강조 — 위 dose 수치는 `[교과서 외 통합 추론 예시]`임. PK35 원문에 직접 권고된 처방이 아님.)

---

## §4.3 — Missed / Erratic dosing은 superposition 문제임

실제 환자가 dose를 빼먹거나, ICU에서 dosing interval이 깨졌을 때 — TDM 농도를 어떻게 해석할 것임? **"자료 오염"으로 처리해버리면 adherence 문제가 IIV에 통째로 흡수돼서 모델이 망함.**

핵심 — **불규칙 dosing은 superposition 문제임.** 각 dose의 남은 농도 기여를 더하고 빼는 작업.

$$
\underbrace{C(t)}_{\text{현재 농도}}
= \overbrace{\sum_{i}\underbrace{C_i(t-t_i)}_{\text{i번째 dose의 잔여 기여}}}^{\text{superposition}}
$$

| 시나리오 | 수식 | 핵심 |
|---|---|---|
| 한 번 missed | Eq.18-1 | 예상 ss 농도에서 missed dose의 잔여 기여를 뺌 |
| 연속 2번 missed | Eq.18-2 | 두 missed dose 기여를 뺌 |
| Unequal interval (9-13-17-21) | Eq.18-3 | 일중 간격 unequal한 24h cycle |
| Dose+interval 모두 unequal | Eq.18-4 | 이전 dose 잔여량 합산; $4\times t_{1/2}$ 이전 dose는 무시 가능 |

💡 **비유.** Superposition은 **방 안에 남은 향수 냄새 더하기**임. 방금 뿌린 향수만 보지 말고, 어제 뿌린 향수가 얼마나 남았는지를 다 합산해야 함.

**유지 풀이 예제 — 실무 감각용**:

- **Digoxin missed 2회** — 0.25 mg daily 환자가 2번 빼먹은 경우 예상 농도 0.39 µg/L. therapeutic range 0.8–2.0 µg/L보다 낮음 [Rowland & Tozer 5e p.602].
- **Vancomycin 9-13-17-21** — 20 kg, 5세 환아, $V$ 14 L, $CL$ 3.3 L/h, $k$ 0.24 h⁻¹, 250 mg regimen → 8:00 농도 2.03 mg/L. therapeutic 5–15 mg/L보다 낮음 [Rowland & Tozer 5e pp.602–603].
- **Erratic vancomycin** — 68 kg, 60세 남성, SCr 2.2 mg/dL, $CL_{cr}$ 34 mL/min, $V$ 42.2 L, $k$ 0.049 h⁻¹; observed 34 mg/L vs predicted 33.7 mg/L. → kinetics는 일관됨, dose 자체가 너무 높다는 신호 [Rowland & Tozer 5e p.604].

---

### Forgivability — Regimen이 얼마나 결손에 견디는가

> 📐 **Osterberg-Urquhart Forgiveness** `[교과서 외 임상 실무 갱신]`
> "forgiving/unforgiving"은 라벨이 아니라 연속 변수임. **Osterberg-Urquhart (*Br J Clin Pharmacol* 2005)** 의 정의:
>
> $$
> \overbrace{
> \underbrace{\mathrm{Forgiveness}}_{\text{용서력}}
> \;\sim\;
> \underbrace{D_a}_{\text{효과 지속}}\;-\;\underbrace{\tau}_{\text{투여 간격}}
> }^{\text{여유 시간}},
> \qquad
> \underbrace{D_a/\tau}_{\text{비율}}
> \begin{cases}
> <1 & \text{unforgiving} \\
> \approx 1 & \text{borderline} \\
> \geq 2 & \text{highly forgiving}
> \end{cases}
> $$
>
> **실무 검증** — simulation으로 (a) 1회 결손 시 trough가 lower therapeutic limit 아래로 떨어지나, (b) 연속 2회 결손을 견디나.

> ⚠️ **PK35 환자 forgivability — 어떤 $t_{1/2}$를 쓸 것이냐?**
> 세 개의 $t_{1/2}$가 같이 존재함:
> - $t_{1/2,\,pop} \approx 192$ h (PK35 prior 환산)
> - $t_{1/2,\,clinical} \approx 36$ h (R&T Table 18-7 임상 reference)
> - **$t_{1/2,\,posterior} = 14.5$ h** (이 환자 Bayesian 추정)
>
> 임상 reference 36 h를 쓰면 $t_{1/2}/\tau \approx 36/24 \approx 1.5$ → **borderline forgiving**.
> **하지만 이 환자의 posterior 14.5 h를 쓰면** $t_{1/2}/\tau \approx 14.5/24 \approx 0.6$ → **unforgiving 영역**.
>
> $$
> \underbrace{\frac{t_{1/2,\,PK35\,posterior}}{\tau}}_{\text{환자 specific}}
> = \frac{\overbrace{14.5\,\mathrm{h}}^{\text{Bayesian}}}{\underbrace{24\,\mathrm{h}}_{\tau}}
> \approx \underbrace{0.6}_{\text{unforgiving}}
> \;\;\neq\;\;
> \underbrace{\frac{t_{1/2,\,clinical}}{\tau}}_{\text{population}}
> = \frac{\overbrace{36\,\mathrm{h}}^{\text{Table 18-7}}}{\underbrace{24\,\mathrm{h}}_{\tau}}
> \approx \underbrace{1.5}_{\text{borderline}}
> $$
>
> → 이 환자에게는 **1회 결손에도 trough가 sub-therapeutic으로 떨어질 위험**으로 분류해야 함. Forgivability는 무조건 환자별 PK로 계산해야 의미 있음.

> 🔑 **§4 한 줄 잠금.** Monitoring 도입은 5개 순차 필터 통과 시 보조 전략. Dose 변경은 **LD($V$) vs MD($CL$) 분리**. 불규칙 dosing은 자료 오염이 아니라 **superposition 문제**. 그리고 어떤 $t_{1/2}$를 쓸지에 따라 forgivability 판단이 뒤집힘.

---

# §5 — 다섯째 마디: 노출 보고로 마무리

이건 세션 16에서 짧게 짚고 가는 마디임. **선택된 용량의 exposure와 safety margin을 어떻게 보고할 것이냐**가 PK15의 역할임 [Gabrielsson & Weiner 5e pp.546–548].

핵심 anchor 숫자만 잠금:

- **Dose levels** — 10 / 56 / 320 µmol·day⁻¹·kg⁻¹
- **노출 지표** — Cmax / AUC
- **Therapeutic 농도** — 0.05–0.1 µM
- **High-dose Cmax** — 약 50 µM
- **Safety margin** — >100배

이게 의미하는 바 — **dosing decision의 사슬은 처방 자체에서 끝나는 게 아니라, "그 dose에서 환자가 받는 exposure와 안전역이 얼마였는지"를 보고하는 데서 끝남.** 임상 보고서, NDA dose-rationale, regulatory document에서 이게 마지막 layer임.

> 🔑 **§5 한 줄 잠금.** Dose 결정으로 끝내지 말 것. **선택된 dose에서의 exposure(Cmax, AUC)와 safety margin**을 source boundary 안에서 보고하는 게 사슬의 진짜 끝임.

---

# §6 — 혼동 쌍 6장 정리

> 🎯 혼동 쌍은 시험 암기용이 아니라 **실무 오류 차단 장치**임. 끝까지 분리해야 할 네 가지 — $C_e/R/RC$, $RF/f_e$, $V/CL$, sampling 신뢰도.

---

## §6.1 — Effect compartment vs Turnover

| 기준 | Effect compartment | Turnover |
|---|---|---|
| 단위 | $C_e$: 농도; $k_{e0}$: 시간⁻¹ | $R$: response 단위; $k_{in}$, $k_{out}$ |
| 수식 | $dC_e/dt=k_{e0}(C-C_e)$ | $dR/dt = k_{in}\cdot I(C) - k_{out}R$ |
| 원인 | plasma–effect site 평형 지연 | input/loss process가 약으로 바뀜 |
| 혼동 시 사고 | delay를 전부 turnover로 과해석 | response system 변화를 link 모델로 축소 |

> ⚡ **분포 지연 vs 시스템 지연.** Effect compartment는 약이 effect site로 **이동하는 시간** 때문. Turnover는 약은 이미 도달했는데 **response system이 바뀌는 시간** 때문. 진단 단서 — dose 올리며 peak가 옮겨가면 turnover, 안 옮겨가면 effect compartment 쪽.

---

## §6.2 — 좌측 이동 vs 우측 이동

| 기준 | 좌측 trough shift | 우측 shift + 고용량 flat |
|---|---|---|
| 시간축 | earlier로 이동 | later로 이동 + flat 구간 |
| 후보 | turnover loss stimulation 또는 receptor on/off | saturation 동반 input inhibition |
| 혼동 시 사고 | "무조건 receptor on/off" 과잉 확정 | absorption delay로 오독 |

> ⚡ **방향은 단서지 결론이 아님.** 1차 필터지 최종 판단이 아님. 가설 줄이고 추가 데이터로 지워가는 순서.

---

## §6.3 — Bayesian "농도 없음" vs "prior 없음"

| 기준 | 농도 없음 | prior 없음 |
|---|---|---|
| 누가 지배 | prior penalty가 지배 | concentration mismatch가 지배 |
| 결과 | population average에 가까움 | maximum-likelihood concentration fitting |
| 사고 | 환자 특이 deviation 놓침 | 생리학적으로 불가능한 $V/CL$ |

> ⚡ **데이터 없음 vs 사전 지식 없음.** posterior 숫자 자체가 아니라 **누가 끌고 갔는지**를 인식해야 함.

---

## §6.4 — 간 고추출 약물 vs 신장 배설 약물

| 기준 | 간 고추출/단백결합 | 신장 배설 미변화 |
|---|---|---|
| 축 | $F$, extraction ratio, $f_u$, unbound $CL$ | $RF$, $f_e$, renal $CL$ |
| 수식 위치 | 경구에서 $F$↑와 $CL$ 변화가 노출 지배 | $R_d = RF\cdot f_e + (1-f_e)$ |
| 혼동 시 사고 | "간 질환 = 모든 $CL$ 감소" 오독 | 약물/환자 속성 혼동 |

> ⚡ **"간 질환 = $CL$ 감소"의 함정.** High-extraction 경구는 간경변에서 $F$가 올라서 노출이 급격히 ↑. Low-extraction + albumin 결합 강한 약물은 total target 자체를 재해석해야 함.

---

## §6.5 — LD vs MD

| 기준 | Loading dose | Maintenance dose |
|---|---|---|
| 단위 | dose; $V\cdot C_{target}/F$ | dose rate; $CL\cdot C_{target}\cdot\tau/F$ |
| 지배 | $V$, target 농도 | $CL$, $RF$, $R_d$ |
| 원인 | body size, tissue distribution | renal/hepatic, interaction |
| 혼동 시 사고 | 신부전이라고 LD까지 줄여 초기 농도 미달 | 장기 dosing에 $V$ 논리 적용 → accumulation/underdosing |

> ⚡ **욕조 채우기 vs 욕조 유지하기.** LD = 일회성 채우기. MD = 새는 만큼 보충. 신부전이어도 $V$ 안 변하면 LD 줄일 이유 없음.

---

## §6.6 — 채혈 식별가능성 vs Point estimate 신뢰도

| 기준 | 채혈 식별가능성 | Point estimate 신뢰도 |
|---|---|---|
| 영역 | sampling geometry, $t/t_{1/2}$ | posterior mean, RSE, shrinkage |
| 핵심 | early → $V$, late/ss → $CL$ | 같은 likelihood의 여러 $(V,CL)$ 조합 위 |
| 사고 | $CL$ collapse를 개인 $CL$로 오독 | 식별 불가 posterior로 dose 결정 |

> ⚡ **지도가 식별 가능한 영역에 있는가.** $1\times t_{1/2}$ 이전 sample은 $V$는 잡지만 $CL$은 prior로 collapse. TDM 농도 보면 먼저 — **"이 농도가 $CL$을 실제로 추정한 거 맞아?"** 부터 물어야 함.

> 💡 **실패 모드 시그니처.** NONMEM에서 η-shrinkage on $CL$ > 30%, $V$는 < 15%, RSE($CL$) > 50%인데 fit 통과 → **"sampling time mismatch"** 신호.

**§6 한 줄.** 오류 대부분은 **하나의 관찰을 하나의 원인에 고정**할 때 생김. 판단 단위는 단일 수치가 아니라 **shape + covariate + dose history + sampling time의 묶음**임.

---

# §7 — 자기 테스트: 능동 회상

> 🎯 답 확인용이 아니라 **판단 사슬에 누수가 있는지 보는 검사**임.

---

**Q1.** Response-time curve에서 baseline → time-delay → peak-shift → saturation/slope를 왜 이 순서로 읽어야 하나?

**A.** baseline이 흐르거나 adaptation/rebound가 있으면 direct 모델 해석이 먼저 깨짐. time-delay와 peak-shift는 effect-site delay / turnover / receptor on/off 후보를 가르는 신호. saturation/slope는 고용량 비선형을 드러냄 [Gabrielsson & Weiner 5e pp.423–424].

---

**Q2.** Case B의 좌측 peak-shift를 "모델 클래스 확정"으로 쓰면 왜 위험한가?

**A.** 좌측 shift는 turnover loss stimulation도, receptor on/off도 만들 수 있음. 원문은 가능한 모델들을 평가하라고 했지 방향만으로 확정하라고 하지 않음 [Gabrielsson & Weiner 5e pp.424–428].

---

**Q3.** Effect compartment와 turnover를 가장 짧게 어떻게 구분?

**A.** Effect compartment = 농도가 effect site로 늦게 평형되는 분포 지연. Turnover = response variable의 production/loss rate 자체가 약으로 바뀜 [Gabrielsson & Weiner 5e pp.425–426].

---

**Q4.** Bayesian TDM에서 농도가 없을 때 vs prior가 없을 때 어떻게 다른가?

**A.** 농도 없음 → population average가 추정값. Prior 없음 → maximum-likelihood concentration fitting. Sparse concentration + weak prior 조합은 생리학적으로 불가능한 $V/CL$을 만들어낼 수 있음 [Gabrielsson & Weiner 5e pp.641–643].

---

**Q5.** PK35 case에서 반드시 보존할 수치 anchor는?

**A.** 55세, 60 kg, CHF, Lanoxicap 0.2 mg daily, 458 h 2.5 µg/L, 479 h 0.9 µg/L, $CL_{pop}$ 1.8 L/h, $V_{pop}$ 500 L, 추정 $CL$ 5.7 L/h, $V$ 119.6 L, $t_{1/2}$ 14.5 h [Gabrielsson & Weiner 5e pp.641–643].

---

**Q6.** $R_d = RF\cdot f_e + (1-f_e)$에서 $f_e$와 $RF$를 왜 분리?

**A.** $f_e$는 약물 속성, $RF$는 환자 속성. 분리해야 신부전이 maintenance 노출에 미치는 영향을 정량화 가능 [Rowland & Tozer 5e pp.450–453].

---

**Q7.** AKI에서 Cockcroft-Gault를 그대로 적용하면 왜 위험?

**A.** SCr은 즉시값이 아니라 creatinine turnover 반영된 지연값. 급성 변화에서는 실제 $RF$가 SCr 기반 추정보다 더 낮을 수 있음 [Rowland & Tozer 5e pp.459–461].

---

**Q8.** 혈액투석에서 half-life 단축 = 보충 용량 필요?

**A.** 아님. **세션 동안 몸에서 빠진 양**이 핵심. $V_u$가 크거나 $CL_u\gg CL_{uD}$이면 single session fraction removed는 작을 수 있음 [Rowland & Tozer 5e pp.471–472].

---

**Q9.** TCS 후보 약물이면 항상 monitoring?

**A.** 아님. concentration-response 양호 + therapeutic failure 가능성 + PopPK 정보 + 신뢰할 만한 assay + 결정 전 도착하는 turnaround, 5개가 대부분 충족돼야 routine strategy [Rowland & Tozer 5e pp.594–597].

---

**Q10.** Phenytoin total target을 그대로 해석하면 왜 틀릴 수 있나?

**A.** Phenytoin은 albumin 결합 강함 + saturable metabolism. Uremia, 수술, displacement drug 있으면 단백결합 변화 → total target을 같은 unbound 농도에 맞춰 조정. 정량 보정은 Sheiner-Tozer $C_{corrected}=C_{measured}/(0.2\cdot Alb + 0.1)$ [Rowland & Tozer 5e pp.588, 595–596].

---

**Q11.** LD와 MD를 한 문장으로 구분?

**A.** LD는 $V$와 target 농도의 문제. MD는 $CL$과 target 평균 노출의 문제 [Rowland & Tozer 5e pp.584–586].

---

**Q12.** Fig.18-5를 "V는 정확히 예측 가능"으로 읽으면 왜 틀린가?

**A.** Fig.18-5는 variability partition임. $V$ 약 45%, hepatic $CL$ 약 40%, renal $CL$ 약 80%, $F$ 약 5% 설명. 이건 prediction accuracy 값이 아님 [Rowland & Tozer 5e p.582].

---

**Q13.** Vancomycin 9-13-17-21 예제의 핵심?

**A.** 24h total daily dose가 같아도 일중 간격이 unequal하면 trough가 크게 떨어질 수 있음. 250 mg 9-13-17-21에서 8:00 농도 2.03 mg/L로 therapeutic 5–15 mg/L보다 낮음 [Rowland & Tozer 5e pp.602–603].

---

**Q14.** PK35 처방 권고를 source-locked로 쓰면 안 되는 이유?

**A.** PK35는 $CL/V/t_{1/2}$ 추정 사례이고, 0.4 mg loading이나 0.1–0.125 mg/day maintenance를 직접 권고하는 처방 문서 아님. 그런 답은 `[교과서 외 통합 추론 예시]`로만 제시 [Gabrielsson & Weiner 5e pp.641–643].

---

## ⚡ 보스 딜레마 ★★

**Q15.** Hepatic-$CL$ dominant 약물 X로 maintenance 단계 환자. Fig.18-5에 따르면 hepatic $CL$은 demographic으로 약 40%만 설명됨. TCS 5 기준 중 "concentration-response 양호"는 충족, "결정 전 도착 turnaround"는 marginal. Routine TDM 도입? Demographic 기반 표준? 어떻게 방어?

**A.** 양자택일이 정답 아님. **두 trade-off를 명시적으로 분리해서 인식하는 게** 핵심.

- **Demographic-only 비용** — hepatic $CL$의 60% IIV가 covariate로 설명 안 됨 → 개인 노출 ±50% 이상 벗어날 수 있음. 다만 sampling/assay/turnaround 운영 위험 0.
- **Routine TDM 비용** — 60% IIV 개별화 가능. 그런데 turnaround marginal → 도착한 농도가 다음 dose 결정 시점을 *지나서* 도착할 수 있음. 측정값은 있는데 의사결정 input이 아닌 상태 = placebo monitoring.
- **마스터 모델러의 선택** — TCS 기준이 대부분 충족되니 도입 *후보*는 맞음. 그런데 turnaround marginal을 운영적으로 해결할 방법(sampling timing 조정, lab cutoff 협의)이 없으면 데이터만 쌓고 결정 못 바꾸는 placebo monitoring이 됨. → 운영 조건 잡히기 전까지는 demographic + clinical response monitoring으로 가되, "hepatic-$CL$ dominant이고 demographic으로 60% 미설명, IIV outlier 가능"을 명시 보고. 운영 조건 확보되는 즉시 TCS 전환 [Rowland & Tozer 5e pp.582, 594–597].

---

**Q16.** Vancomycin PopPK fit에서 η-shrinkage on $CL$ > 30%, $V$ < 15%, COV step 통과, RSE($CL$) > 50%. 데이터셋은 ICU 첫 24시간 dense sampling. 무슨 신호?

**A.** **"Fit은 통과했지만 데이터가 식별할 수 없었던 양을 추정하려 한"** 신호. $1\times t_{1/2}$ 이전 sample에서는 $CL\times 1/3$과 $V\times 3$이 거의 같은 likelihood → NONMEM이 $V$는 잡고 $CL$은 population mean으로 collapse. 

**해결** — (a) $V$를 strong prior로 고정하고 $CL$만 개별화, (b) $\geq 4\times t_{1/2}$ post-infusion sample 추가 [Rowland & Tozer 5e pp.605–606].

$$
\underbrace{CL\times\frac{1}{3}}_{\text{낮은 CL}}
\;\approx_{\text{early}}\;
\underbrace{V\times 3}_{\text{큰 V}},
\qquad
\underbrace{t\geq 4\times t_{1/2}}_{\text{$CL$ 분리 가능}}
$$

> 🔑 **§7 한 줄.** 자기 테스트의 목적은 계산 정답보다 **"어떤 정보가 없으면 해석이 불가능한가"**를 즉시 말하게 만드는 것. Q15·Q16은 단일 정답 없는 trade-off를 *방어 가능한 추론*으로 바꾸는 문제.

---

# §8 — 메타 프레임: 큰 그림에서 다시 보기

## A. 이 세션의 위치 — Model에서 Decision으로

이 세션은 **"모델 구축"과 "임상 dosing 결정" 사이의 연결부**임. 모델을 만든 다음 실제 환자 용량 판단으로 넘어가는 지점.

- Ch.6 — model structure를 좁히는 눈
- Ch.15 — 질환이 파라미터를 어떻게 움직이는지 설명
- PK35 — individual parameter를 posterior로 만듦
- Ch.18 — 그 estimate를 LD/MD/monitoring/missed-dose 해석으로 바꿈
- PK15 — 선택된 dose의 exposure/safety margin 보고

---

## B. MIPD — 현대 임상약리 표준 용어로 다시 부르기

> 🌐 **MIPD (Model-Informed Precision Dosing)** `[교과서 외 임상 실무 갱신]`
> 이 세션이 다루는 다섯 마디 — *plot shape → 질환 covariate → Bayesian posterior → LD/MD 분리 → exposure 보고* — 가 현대 표준 용어로는 **MIPD**임. ASCPT/PSCC가 핵심 educational priority로 채택, FDA/EMA 규제 권고에도 등장.
>
> R&T 5e(2011)는 이 용어를 안 썼지만 Ch.18 구조 자체가 MIPD framework임. 학습자에게 — **Bayesian TDM + target concentration strategy = MIPD라는 임상 의사결정 패러다임** — 매핑을 한 번은 명시해둘 것. (InsightRX, BestDose, DoseMeRx 같은 구현 도구는 본 강의 범위 밖.)
>
> $$
> \overbrace{
> \underbrace{\text{MIPD}}_{\text{현대 표준 용어}}
> \;\equiv\;
> \underbrace{\text{PopPK prior}}_{\text{Ch.13/15}}
> \;+\;\underbrace{\text{Bayesian posterior}}_{\text{PK35}}
> \;+\;\underbrace{\text{target concentration}}_{\text{Ch.18 TCS}}
> \;+\;\underbrace{\text{LD/MD 분리}}_{\text{Ch.18}}
> }^{\text{model-informed individualization cycle}}
> $$

---

## C. 네 가지 메타 패턴 — 다 곱셈, 다 좌표

1. **두 인자의 곱이 결정함.**
$$
\underbrace{R_d}_{\text{renal}}
\sim
\overbrace{\underbrace{f_e}_{\text{약물}}\times\underbrace{RF}_{\text{환자}}}^{\text{renal}},
\quad
\underbrace{\text{forgiveness}}_{\text{용서력}}
\sim
\overbrace{\underbrace{t_{1/2}/\tau}_{\text{시간 여유}}\times\underbrace{\text{TI}}_{\text{농도 여유}}}^{\text{여유}},
\quad
\underbrace{TCS}_{\text{monitoring}}
\sim
\overbrace{\underbrace{\text{risk}}_{\text{위험}}\times\underbrace{\text{measurability}}_{\text{측정성}}}^{\text{TCS}}
$$

2. **식별가능성은 채혈 시점에 달려 있음.** 이른 농도 → $V$, 늦은/steady-state → $CL$.

3. **현실은 연속, 소통은 이산.** Renal stage, TCS 후보 list, dialysis threshold는 의사소통 도구지 hard biological cutoff가 아님.

4. **$CL$의 해부학이 용량 논리를 결정.** Renal-$CL$ dominant, hepatic-$CL$ dominant, high-extraction, low-extraction, protein-bound — 같은 "$CL$ 감소"라는 말로 묶을 수 없음.

---

## D. Source-locked 전문가 해석 지점 — 체크리스트

- ☐ Plot 모양으로 ODE 후보를 줄였는가
- ☐ $f_e/RF/R_d$로 신질환 maintenance 조정을 계산했는가
- ☐ C-G를 쓰되 SCr lag와 body composition caveat를 같이 봤는가
- ☐ Bayesian 출력을 prior, 농도, sampling time, dosing history의 산물로 읽었는가
- ☐ TCS를 약물명 자동 적용이 아니라 5개 기준 기반 보조 전략으로 운용했는가
- ☐ LD와 MD를 $V$ vs $CL$ 문제로 분리했는가
- ☐ Missed/erratic dosing을 자료 오염이 아니라 superposition 문제로 계산했는가

---

## E. 사용 금지 / 대체 표현 — 최종 잠금

**❌ 사용 금지:**

```
- "peak-shift direction = model class"
- "TCS candidate drug = mandatory TCS"
- "V/CL Fig.18-5 percentages = dosing accuracy"
- "PK35 = 직접 처방 권고"
- "TDM patients 80% irregular dosing"
- "hemodialysis decision = simple Vu<120 AND CLu<CLuD"
- "NDA/IND/RMP/software workflow = textbook source claim"
- Sheiner-Tozer 분모에 (Alb/4.4)를 그대로 0.2와 곱하는 표기 (정상 alb에서 보정 인자 ≠ 1)
```

**⭕ 대체:**

```
- peak-shift direction narrows competing models
- TCS is useful as adjunct when criteria are satisfied
- Fig.18-5 is variability partition (NOT accuracy)
- PK35 estimates individual CL/V/t½; prescription is separate inference
- missed/unequal/erratic dosing is common enough to need equations
- dialysis effectiveness lies on Vu·CLu·CLuD coordinate plane
- implementation/regulatory extrapolations require [교과서 외 구현/규제 번역]
- Sheiner-Tozer 정식: C_corrected = C_measured / (0.2·Alb + 0.1)
  (정상 alb=4.4에서 분모 ≈ 0.98 ≈ 1 검증)
```

---

## F. 최종 요약 — 한 줄로 다시 꿰면

**plot 모양으로 모델 후보를 좁히고, 질환과 환자 특성으로 파라미터 편차를 설명하고, Bayesian TDM과 dosing 식으로 치료 의사결정에 연결함.**

피해야 할 다섯 함정:
1. 방향 하나로 모델을 단정하는 deterministic overclaim
2. 근거 없는 백분율
3. 라벨 없는 규제/소프트웨어 외삽
4. PDF에 없는 직접 처방 주장
5. 산술적으로 검증 안 되는 보정식

---

## 부록 — v4.0 → v4.1 변경 사항 (Remastered판 보존)

본 remastered 버전은 v4.1의 다음 정정·보강 사항을 모두 보존했음:

1. **Sheiner-Tozer 보정식 정정** — Form A (g/dL 입력)와 Form B (정규화)를 모두 명시. 정상 albumin에서 보정 인자 ≈ 1 검증. Anderson 신부전 변형 포함.
2. **PK35 forgivability에서 환자-specific $t_{1/2}$ 사용** — pop prior 환산 192 h, 임상 reference 36 h, posterior 14.5 h 세 가지 구분 및 임상 적용 가이드.
3. **수식 annotation 강화** — MD 식, MIPD 정의, Forgiveness 정의, Sheiner-Tozer 세 형태 모두에 overbrace/underbrace.
4. **출처 표기 정확화** — 표제 인용은 "Gabrielsson & Weiner 5e" / "Rowland & Tozer 5e" 풀이 형태. DIG trial (Rathore JAMA 2003), Vancomycin consensus (Rybak 2020), Osterberg-Urquhart (2005) 1차 문헌 명시.
5. **사용 금지/대체 표현에 Sheiner-Tozer 산술 오류 항목 추가**.

본 remastered 판본은 v4.1의 source-locking 원칙을 유지하면서, 척추(M1→M4→M5→M8→M9)를 다섯 마디 서사 구조로 재배열하고, PK35 디곡신 케이스를 강의 전체의 running anchor로 사용함. 다루는 콘텐츠 범위는 v4.1과 동일.

---

**C-260518-051847-Q9X**

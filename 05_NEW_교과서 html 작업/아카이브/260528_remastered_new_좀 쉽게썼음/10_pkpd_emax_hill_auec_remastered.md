# 10 — PK/PD 모델 기초: Emax·Hill·AUEC — Remastered

> 🎯 **이 강의의 마스터 프레임 (한 줄로 꿴 큰 그림)**
>
> 임상에서 약을 주면 머릿속에 자동으로 그려지는 그림이 있음 — *농도가 10이면 효과도 10*. 그런데 **이 그림은 거의 항상 틀림**. 왜 틀리느냐 — 농도-시간 곡선을 반응-시간 곡선으로 번역하는 과정에서 **세 군데서 동기화가 깨지기 때문**임.
>
> ① **수직축 decoupling**: 같은 농도라도 반응 크기가 안 맞음 (천장 있음 + 가파름 다름) → **Emax / Hill 모델**
> ② **수평축 decoupling**: 같은 농도라도 *언제* 그 농도에 있는지에 따라 반응이 다름 → **Hysteresis → Effect Compartment / Indirect Response**
> ③ **종결시점 decoupling**: 약이 사라져도 효과는 안 사라짐 → **PK 율속 vs PD 율속**
>
> 이 강의의 모든 개념($K_d$, $EC_{50}$, Hill $\gamma$, AUEC, duration, $k_{e0}$, $k_{in}/k_{out}$, ...)은 이 셋 중 어디서 깨진 동기화를 어떻게 모델에 흡수할지에 대한 도구일 뿐임. 임상 케이스 하나를 만나면 머릿속에서 *"이건 어느 축에서 깨진 거지?"* 한 번만 물으면 됨. 그 다음엔 도구 상자에서 맞는 모델을 꺼내면 됨.

---

## 출처와 범위

이 강의는 **Gabrielsson & Weiner 5e Ch.3** (수용체 결합, $E_{max}$/Hill, 비정상상태 반응과 AUEC, 사례연구 PD3) 와 **Rowland & Tozer 5e Ch.8** (시간 지연, 히스테리시스, 효과 구획, 간접 반응, 효과 지속 시간) 두 책의 범위 안에서 만들었음. 이 두 책을 벗어난 보강은 모두 `📌 교과서 외 보강` 박스로 분리하고 1차 문헌을 명시함.

- 사용 범위: Gabrielsson & Weiner 5e p.199–224, p.229–234, p.732–741; Rowland & Tozer 5e p.233–264.
- 본문 외 보강 출처: Black & Leff (1983), Sheiner-Holford (1981), Awtry-Loscalzo (2000), Patrono et al. (2017).
- 범위 밖 구간은 `[확인 필요 — 첨부 PDF 미포함 구간]`으로 명시.

---

# §1 — 임상 장면 세 개로 문제 정의하기

강의를 추상적으로 시작하지 않겠음. 진료실에서 마주칠 수 있는 세 장면부터 깔고 가겠음. 이 세 장면이 강의 전체의 출발점임.

**장면 ①** — Digoxin 1 mg을 정맥으로 빠르게 줬음. 첫 4시간 동안 채혈하면서 좌심실 구출 시간 지표를 같이 잼. 그런데 이상한 게 — *혈장 농도는 떨어지는데 효과 지표는 오히려 올라감*. 혈장이 효과를 대표한다면 둘이 같이 움직여야 하는데, 따로 놂. → **수평축 decoupling 사례.** [Rowland & Tozer 5e p.234]

**장면 ②** — Naproxen 500 mg을 경구로 주고 치과 통증 모델에서 비결합 혈장 농도와 통증 완화를 분 단위로 잼. 그런 다음 *농도-효과 평면*에 점을 찍어보면 **반시계 방향 고리**가 그려짐. 같은 농도인데 시간 순서에 따라 효과가 다름. → **수평축 decoupling 사례 ②.** [Rowland & Tozer 5e p.234–235]

**장면 ③** — Aspirin 650 mg을 경구로 줬음. 혈장 반감기는 약 15분. 그런데 항혈소판 효과는 *수일* 감. 약은 진작에 사라졌는데 효과는 안 사라짐. → **종결시점 decoupling 사례.** [Rowland & Tozer 5e p.251]

이 세 장면이 던지는 메시지는 하나임 — **"농도가 얼마인가"만 보고 PK/PD를 끝낼 수 없다.** 그 농도가 어떤 시간 지연과 어떤 반응 시스템을 통과해서 효과로 번역되는가 — 거기까지 읽어야 임상 결정을 할 수 있음.

이 강의가 다섯 단계로 그 번역 과정을 분해함:

```text
[수직축 decoupling]
  Block A. 천장과 가파름 — 왜 농도 두 배가 효과 두 배가 아닌가?
            └ Kd vs EC50 분리, Emax 골격, Hill γ 가 임상 안전의 진짜 키

[수평축 decoupling]
  Block B. 시간 지연 진단 — 같은 농도 다른 효과 (히스테리시스)
  Block C. 시간 지연 구조화 — 부위 평형화인가, 시스템 전환인가?

[종결시점 decoupling]
  Block D. 효과 적분과 지속 시간 — 약이 사라져도 효과가 남는 이유
            └ AUEC, duration-log dose, PK 율속 vs PD 율속

[종합]
  Block E. 만성 투여로 가는 다리 — 정상상태 E-R 평면과 의사결정
```

선행: 선형 PK · 농도-시간 해석 → **이 강의** → 후속: PopPK/PD 공변량 · 시뮬레이션 · 용량 최적화.

> 📖 **Gabrielsson & Weiner 5e p.199 Fig.3.1** — 이 그림 한 장이 강의 전체를 묶어줌. 왼쪽 패널은 **농도-반응 감수성** (potency/efficacy), 오른쪽 패널은 **반응-시간 거동** (onset/intensity/duration). 우리 구분으로 옮기면 왼쪽 = Block A (수직축), 오른쪽 = Block B·C·D (수평축 + 종결시점).

PD 모델링의 본질을 G&W가 명시한 대로 옮기면: **반응 크기와 시간 경과를 예측하는 in vivo 특성을 식별하는 것**. 이상적인 PD 지표 5가지 — 민감·점진·임상적 의미·객관·재현. 최소 설계 요건 — **대조군 + 2~4개 용량 수준, 그중 최소 한 용량은 최대 반응 도달**. [Gabrielsson & Weiner 5e p.199–200]

이 최소 설계 요건이 왜 그렇게 중요한지는 Block A 끝의 PD3 사례에서 직접 보게 됨.

---

# §2 — Block A: 수직축 decoupling — 천장과 가파름

## §2.1 첫 번째 분리 — $K_d$와 $EC_{50}$은 같은 숫자가 아님

가장 흔한 임상약사·약리학 교과서 함정부터 잡고 시작하겠음.

**$K_d$**: 약물이 수용체에 *얼마나 잘 붙는가* — 분자 수준 결합 친화도.
**$EC_{50}$**: 약물이 *그 결합을 거쳐서 절반 효과를 내는 농도* — 시스템 수준 기능적 감수성.

이 둘이 같은 농도 단위라서 자주 같은 표에 나란히 놓이는데, **이렇게 놓으면 안 됨**. 둘은 다른 층위의 이야기임.

> 💡 **치트키 비유 — 비밀번호와 회사 운영**
> $K_d$는 *회사 출입 비밀번호 정확도*. 비밀번호를 맞춰야 들어감.
> $EC_{50}$은 *비밀번호를 맞춰서 회사 전체가 절반 가동되는 데 필요한 출입자 수*.
> 비밀번호가 강한 거랑(=$K_d$가 낮은 거랑) 회사가 잘 돌아가는 거(=$EC_{50}$이 낮은 거)는 다른 얘기임. 직원 한 명만 들어와도 회사 전체가 풀가동되도록 시스템이 설계되어 있으면(여분 수용체 + 증폭 연쇄), **출입자가 적어도 가동률이 높음** — 즉 $EC_{50} < K_d$.

### 어디서 그 차이가 오나

질량작용법칙(law of mass action)에서 식을 따라가보면 답이 나옴. 가역적 1:1 결합, 평형, 단일 구획 농도 가정으로:

평형 결합:
$$
\underbrace{\frac{d[RC]}{dt}}_{\text{복합체 변화}}
= \underbrace{k_1[R][C]}_{\text{결합 생성}}
- \underbrace{k_{-1}[RC]}_{\text{해리 손실}}
= \underbrace{0}_{\text{평형}}
$$

해리상수 정의:
$$
\underbrace{K_d}_{\text{해리상수}}
= \underbrace{\frac{k_{-1}}{k_1}}_{\text{해리/결합비}}
= \underbrace{\frac{[C][R]}{[RC]}}_{\text{유리/결합비}}
$$

총 수용체 보존식 $[R_T] = [R] + [RC]$ 대입 → 점유율:
$$
\underbrace{\frac{[RC]}{[R_T]}}_{\text{점유율}}
= \underbrace{\frac{[C]}{[C]+K_d}}_{\text{농도-친화도 관계}}
$$

여기서 반응이 점유에 비례하고, $E_{max} = \alpha [R_T]$로 두면 (단, $\alpha$ = 고유활성, intrinsic activity):
$$
\underbrace{E}_{\text{반응}}
= \frac{\underbrace{E_{max}}_{\text{천장}} \cdot \underbrace{[C]}_{\text{농도}}}
{\underbrace{[C]+K_d}_{\text{농도+Kd}}}
$$

기능 반응 단으로 옮기면 $K_d$ 자리에 $EC_{50}$이 들어옴:
$$
\underbrace{E}_{\text{효과}}
= \frac{\underbrace{E_{max}}_{\text{천장}} \cdot \underbrace{C}_{\text{농도}}}
{\underbrace{EC_{50}}_{\text{절반효과}} + \underbrace{C}_{\text{농도}}}
$$

`[출처: Gabrielsson & Weiner 5e Ch.3 p.202–204, Eq.3:1–3:10]`

### 왜 $EC_{50} \neq K_d$ 인가

핵심 두 가지:

**여분 수용체(spare receptor)** — 조직이 수용체를 *많이* 갖고 있어서, 다 점유 안 해도 최대 효과 근처에 도달함.
**증폭 연쇄(cascade amplification)** — 수용체 한 개가 신호를 켜면 하류에서 다단계로 증폭됨. 10% 점유가 90% 반응으로 번질 수 있음.

$$
\underbrace{EC_{50}}_{\text{기능 EC50}}
\neq \underbrace{K_d}_{\text{결합 Kd}}
$$

G&W Fig.3.5가 **10% 점유율이 90% 반응으로 증폭되는 연쇄 증폭** 사례를, Fig.3.6이 **같은 반응에 필요한 점유율이 조직마다 다른** 사례를 보여줌. [Gabrielsson & Weiner 5e p.205–206]

| 파라미터 | 단위 | 생물학적 의미 | 변하는 원인 |
|---|---:|---|---|
| $E_{max}$ | 반응 단위 | 점유×고유활성의 최대 효과 | 총 수용체량, 조직 반응성, 고유활성 |
| $K_d$ | 농도 | 결합층 해리상수 | 결합/해리 속도 |
| $EC_{50}$ | 농도 | 기능층 절반 효과 농도 | 결합 + 수용체 밀도 + 증폭 + 조직 반응 |
| $C$ | 농도 | 관련 생체구획 농도 | 투여량, 분포, 결합, 제거 |

### 임상에서 이거 안 분리하면 어떻게 깨지나

**시나리오** — Phase 2 PopPK/PD 보고서에서 어떤 공변량(예: 신기능 저하군)에서 $EC_{50}$이 50% 낮게 추정됐음. "신기능 저하군이 약에 더 민감하다"고 결론 내림.

**이게 왜 위험한가** — 세 가지 가능한 기전이 모두 같은 $EC_{50}$ 변화로 보일 수 있음:
- 단백결합 감소 → **비결합** 농도가 증가 → 총 $EC_{50}$만 낮아 보임 (약물 측, PK 변화)
- 활성 대사체 축적 → 추가 약리 활성 (약물 측, 대사 변화)
- 수용체 감수성 증가 → 진짜 PD 변화 (시스템 측)

비결합 농도 분석 없이 총 $EC_{50}$ 변화만 보고 "감수성 증가"로 단정하면, 신기능 저하군 용량 조정이 잘못된 기전 가정 위에 세워짐. 라벨 deficiency 발행 위험.

> 💼 **실무 인사이트** — 새 $EC_{50}$ 값을 만나면 두 가지를 자동 체크:
> ① **결합 분석(binding assay)인지 기능 분석(functional assay)인지** 먼저 확인.
> ② **총 농도 기반인지 비결합 농도 기반인지** 확인. 단백결합 변화는 apparent potency를 지배함.
> 이거 안 하고 $K_d = EC_{50}$으로 단정해버리면 공변량 기전 해석이 통째로 망가짐.

**Block A 첫 매듭** — $K_d$는 *결합 강도*, $EC_{50}$은 *결합 + 증폭 + 조직 반응까지 포함한 기능적 감수성*. $E_{max}$ 식의 쌍곡선 모양은 수용체 보존 + 질량작용에서 자연 도출됨. 경험식이 아니라 **점유율과 신호 증폭을 한 줄로 압축한 구조식**임.

---

## §2.2 두 번째 분리 — Hill $\gamma$가 임상 안전의 진짜 키 ⚡

이제 가파름 얘기로 넘어가겠음. 여기가 **이 강의의 Apex (정점) 개념**이라고 말한 이유를 곧 알게 됨.

임상에서 한 번쯤 이런 경험 있을 거임 — 항부정맥제나 면역억제제를 약간만 증량했는데 *갑자기* 독성이 터짐. 반대로 어떤 약은 두 배 올려도 효과가 별로 안 늘어남. 이 두 현상이 같은 식에서 나옴 — **Sigmoid $E_{max}$ / Hill 모델**.

$$
\underbrace{E}_{\text{효과}}
= \frac{\underbrace{E_{max}}_{\text{천장}} \cdot \underbrace{C^n}_{\text{농도^n}}}
{\underbrace{EC_{50}^n}_{\text{중간점^n}} + \underbrace{C^n}_{\text{농도^n}}}
$$

기저치 있는 억제 반응(혈압, 위산 등):
$$
\underbrace{E}_{\text{관찰반응}}
= \underbrace{E_0}_{\text{기저치}}
- \frac{\underbrace{I_{max}}_{\text{억제천장}} \cdot \underbrace{C^n}_{\text{농도^n}}}
{\underbrace{IC_{50}^n}_{\text{절반억제}} + \underbrace{C^n}_{\text{농도^n}}}
$$

`[출처: Gabrielsson & Weiner 5e Ch.3 p.216, p.218, Eq.3:32, Eq.3:34–3:35]`

### 세 파라미터를 완전히 분리해서 보기

| 파라미터 | 의미 | 직관 |
|---|---|---|
| $E_{max}$ / $I_{max}$ | **천장** — 효과가 최대 어디까지 갈 수 있나 | 곡선의 *높이* |
| $EC_{50}$ / $IC_{50}$ | **중간점** — 절반 효과가 어디서 나오나 | 곡선의 *위치* |
| Hill $\gamma$ (=$n$) | **가파름** — 얼마나 좁은 농도 구간에서 0→100%로 전환되나 | 곡선의 *경사* |

이 셋이 **수학적으로 독립**이라는 게 가장 중요함.

> 💡 **치트키 비유 — 스위치 vs 다이얼**
> $\gamma = 1$이면 농도-반응이 **다이얼**처럼 부드럽게 돌아감 — 농도 5배 차이가 효과 5배 차이.
> $\gamma = 5$면 거의 **on/off 스위치** — 농도 1.5배 차이가 효과 0%→100%.
> 같은 $EC_{50}$이라도 $\gamma$가 1이냐 5냐에 따라 *치료 허용 폭이 완전히 달라짐*.

### 왜 이 식이 Apex 개념인가 — 임상 안전 마진의 진짜 결정자

흔한 오해 — **"$EC_{50}$만 알면 그 농도에서 임상 효과를 예측할 수 있다."**

이게 왜 틀렸냐. 임상 반응 크기와 안전 마진은 $E_{max}$, $EC_{50}$, $\gamma$가 **함께** 결정함. 특히 **협역 치료역 약물**에서는 $\gamma$가 결정적임:

$$
\overbrace{
\underbrace{\gamma = 1}_{\text{완만한 다이얼}}
\;:\;
\underbrace{EC_{50} \pm 30\%}_{\text{농도 변화}}
\;\to\;
\underbrace{40\% \to 60\% \text{ 반응}}_{\text{20\%p 변화}}
}^{\text{넓은 치료 허용 폭}}
$$

$$
\overbrace{
\underbrace{\gamma = 3}_{\text{급한 스위치}}
\;:\;
\underbrace{EC_{50} \pm 30\%}_{\text{같은 농도 변화}}
\;\to\;
\underbrace{20\% \to 80\% \text{ 반응}}_{\text{60\%p 변화}}
}^{\text{매우 좁은 치료 허용 폭}}
$$

> ⚡ **이 식이 보고서에서 빠지면 어떻게 되나** — Exposure-response 보고서에 $EC_{50}$만 적고 $\gamma$를 빼버리면, 협역 치료역 약물 (vancomycin, tacrolimus, 항부정맥제, 일부 vitamin K antagonist) 의 임상 용량 조절 가이드가 *과관대*하게 설계됨 → 독성과 치료 실패가 모두 빗나감 → 규제 심사관이 "Hill coefficient의 임상적 의의" 섹션에 deficiency 발행 → NDA/BLA 일정 지연. `[교과서 외 규제 해석]`

> 💡 $EC_{50}$은 "곡선이 어디 있나"(위치), $\gamma$는 "그 곡선이 얼마나 가파른가"(안전 마진). **위치보다 가파름이 협역 치료역 약물의 안전을 결정한다는 게 Apex 개념의 핵심.**

### 그래프에서 파라미터 복원

중간 기울기 $m$에서 $\gamma$ 역산:
$$
\underbrace{m}_{\text{중간기울기}}
= \frac{\underbrace{n}_{\text{Hill n}} \cdot \underbrace{E_{max}}_{\text{천장}}}
{\underbrace{4}_{\text{중간점 보정}}}
\;\;\Rightarrow\;\;
\underbrace{n}_{\text{추정 n}}
= \frac{4 \, \underbrace{m}_{\text{관찰 m}}}{\underbrace{E_{max}}_{\text{최대효과}}}
$$

절편 $C_0$ 복원:
$$
\underbrace{C_0}_{\text{절편 C0}}
= \underbrace{EC_{50}}_{\text{EC50}}
\cdot \underbrace{e^{-2/n}}_{\text{Hill 보정}}
$$

`[출처: Gabrielsson & Weiner 5e p.219, Eq.3:38–3:42]`

### 단백결합 환산 — 식 그대로 보존됨

비결합 농도로 옮겨도 $\gamma$는 보존됨:
$$
\underbrace{E}_{\text{효과}}
= \frac{\underbrace{E_{max}}_{\text{천장}} \cdot \underbrace{C_u^n}_{\text{비결합농도^n}}}
{\underbrace{EC_{u50}^n}_{\text{비결합 EC50^n}} + \underbrace{C_u^n}_{\text{비결합농도^n}}}
$$

단백결합 차이 큰 비교에서는 **반드시** 비결합 농도 기준. 그래야 단백결합 변화와 역가 변화가 안 섞임. [Gabrielsson & Weiner 5e p.216–217]

> 💡 총 농도는 *항구에 도착한 모든 컨테이너*, 비결합 농도는 *실제로 공장 안으로 들어간 화물*. 효과를 만드는 건 후자임.

---

## §2.3 PD3 사례연구 — 설계가 모델 식별을 결정한다

이 사례가 왜 중요한지 한 줄로 — **"파라미터 추가는 무조건 과적합"이라는 흔한 통념이 항상 맞지 않는다는 걸 같은 약 같은 모델 다른 설계로 증명한 케이스**임.

같은 PD3 혈압 억제 $I_{max}$ 데이터, 두 가지 농도 범위 설계:

**0–500 µg/L 설계** (고원부 미도달)
→ Sigmoid 우월성 입증 실패. F-test 통과 안 함.

**0–800 µg/L 설계** (G&W 최소 설계 요건 만족)
→ 모델 판별 성공.
- Sigmoid $I_{max}$: $E_0=171$, $I_{max}=34.7$, $IC_{50}=140$, $n=2.03$, **AIC=45.6**
- 일반 $I_{max}$: $E_0=177$, $I_{max}=49.8$, $IC_{50}=175$, **AIC=50.8**

[Gabrielsson & Weiner 5e p.200, p.733–741]

**결정적인 증거 — $IC_{50}$ CV 방향**

진짜 과적합이면 정밀도가 *악화*되어야 정상임. 그런데 PD3에서는 반대 — 일반 $I_{max}$의 $IC_{50}$ CV가 약 **31%**였던 게 sigmoid에서 약 **11%**로 *향상*됨. **추가 파라미터가 데이터를 진정으로 설명한다**는 직접 증거임. F-test/AIC가 임계값 근처에서 흔들릴 때 결정적인 보조 증거가 됨. [Gabrielsson & Weiner 5e p.735 Table 3.2]

> 💼 **실무 인사이트** — Sigmoid $E_{max}$ 적합은 정석 순서:
> ① 일반 $E_{max}$/$I_{max}$로 $E_0/E_{max}/EC_{50}$ 초기값 잡기.
> ② $n=1$에서 출발해서 자유화.
> ③ Sigmoid에서 $IC_{50}$ CV가 *향상*되면 → $n$ 추가 정당화.
> ④ 정밀도가 악화되거나 $n$이 1로 수렴하면 → 알고리즘 문제가 아니라 **농도 범위 정보 부족**임 (고원부 미도달).

### Hill $\gamma > 1$을 "협동성 증명"으로 쓰면 왜 틀리나

이게 흔한 함정임. Hill 식 자체는 **현상학적**이라서, $\gamma > 1$이 나왔다는 사실만으로는 협동성을 증명 못 함. 결합 단의 독립 근거 없이 $\gamma$를 협동성으로 해석하면 출처 충실성이 깨짐. 가능한 *가설*로 제시할 수는 있지만 *증명*은 아님. [Gabrielsson & Weiner 5e p.216, p.220]

| $\gamma$ 값 | 가능한 해석 |
|---|---|
| $\gamma = 1$ | 일반 Emax 쌍곡선 (단일 점유 모델) |
| $\gamma > 1$ | 급격 전환. 협동성? 다중 부위? 이질성? — **가설 후보들, 증명 아님** |
| $\gamma < 1$ | 활성 대사체? 다중 수용체 부위? 이질성? — **마찬가지로 가설** |

---

## §2.4 📌 교과서 외 보강 — Black-Leff Operational Model

> 📌 **부분효현제에서 $E_{max}$/Hill의 한계**
>
> Buprenorphine, aripiprazole, brexpiprazole, pindolol, TRV130 같은 **부분효현제(partial agonist)** 를 다룰 때 — 표준 $E_{max}$/Hill 식만으로는 **약물 측 친화도($K_A$)와 약물·시스템 결합 측 고유효능($\tau$)을 수학적으로 분리할 수 없음**. 관찰된 $E_{max}^{obs}$와 $EC_{50}^{obs}$ 두 숫자가 이 두 양의 *조합*이라서, 같은 곡선 모양이 서로 다른 $(K_A, \tau)$ 쌍에서 나옴.
>
> Black & Leff (1983) 이 이 두 양을 명시적으로 분리함:
>
> $$
> \overbrace{
> \underbrace{E}_{\text{관찰 효과}}
> = \frac{
>   \underbrace{E_m}_{\text{시스템 최대}}
>   \cdot \underbrace{\tau^n}_{\text{전환비^n (효능)}}
>   \cdot \underbrace{[A]^n}_{\text{작용제^n}}
> }{
>   \underbrace{(K_A + [A])^n}_{\text{친화도 항}}
>   + \underbrace{\tau^n \cdot [A]^n}_{\text{효능 항}}
> }
> }^{\text{Black-Leff 1983, Hill-form 일반화}}
> $$
>
> | 파라미터 | 의미 | 표준 $E_{max}$/Hill 식과의 관계 |
> |---|---|---|
> | $E_m$ | **시스템** 최대 (조직 상한, 약물 비의존) | $E_{max}^{obs}$가 *아님* |
> | $K_A$ | **약물-수용체** 해리상수 (친화도, $K_d$와 같은 결합층) | $EC_{50}^{obs}$가 *아님* |
> | $\tau$ | **Transducer ratio** (고유효능). 완전효현제 $\tau \gg 1$, 부분효현제 $\tau$ 작음, 길항제 $\tau = 0$ | §2.1의 "신호 증폭 이득"을 정량화한 한 숫자 |
> | $n$ | Transducer slope | §2.2의 Hill $\gamma$를 일반화 |
>
> 관찰값과의 관계 (Hill-form 일반):
>
> $$
> \underbrace{E_{max}^{obs}}_{\text{관찰 천장}}
> = \frac{E_m \cdot \tau^n}{1 + \tau^n}
> ,\qquad
> \underbrace{EC_{50}^{obs}}_{\text{관찰 EC50}}
> = \frac{K_A}{(2 + \tau^n)^{1/n} - 1}
> $$
>
> **Hill $n=1$ 단순 hyperbolic 특수 경우 (직관 잡기에 가장 좋음)**:
>
> $$
> \overbrace{
> \underbrace{E_{max}^{obs}\bigg|_{n=1}}_{\text{n=1 관찰 천장}}
> = \frac{E_m \cdot \tau}{1 + \tau}
> ,\qquad
> \underbrace{EC_{50}^{obs}\bigg|_{n=1}}_{\text{n=1 관찰 EC50}}
> = \frac{K_A}{1 + \tau}
> }^{\text{n=1 단순 hyperbolic 해 — Black & Leff 1983}}
> $$
>
> 점근선 분석으로 두 극한 보기:
>
> **완전효현제 극한 ($\tau \gg 1$)**:
> $$
> \underbrace{EC_{50}^{obs}}_{\text{관찰 EC50}}
> = \frac{K_A}{1+\tau}
> \;\xrightarrow{\tau \gg 1}\;
> \underbrace{\frac{K_A}{\tau}}_{\text{spare receptor 극한}}
> ,\quad
> \underbrace{E_{max}^{obs}}_{\text{관찰 천장}} \to E_m
> $$
> → 관찰 EC50이 친화도보다 *훨씬 낮게* 측정됨. 이게 §2.1에서 말한 "$EC_{50} < K_d$ 가능성"을 정량화한 것.
>
> **부분효현제 극한 ($\tau \ll 1$)**:
> $$
> \underbrace{EC_{50}^{obs}}_{\text{관찰 EC50}}
> \approx K_A
> ,\quad
> \underbrace{E_{max}^{obs}}_{\text{관찰 천장}}
> \approx E_m \cdot \tau
> $$
> → 관찰 EC50이 친화도와 거의 같지만 **천장이 낮게 정착**. 부분효현제 임상 직관 ("천장이 낮은 약") 의 정량화.
>
> **임상 함의** — Aripiprazole 같은 도파민 부분효현제는 *고용량에서도 천장이 낮아 안전 마진이 넓지만 효능이 제한적*. 완전효현제는 *천장이 높지만 부작용 마진이 좁음*. 표준 $E_{max}$/Hill로 적합한 두 약을 같은 표에 놓으면 이 차이가 안 보임. Operational model로 분리해야 보임.
>
> `[교과서 외 보강 — Black JW, Leff P. Operational models of pharmacological agonism. Proc R Soc Lond B Biol Sci. 1983;220(1219):141-62. G&W 5e Ch.3 p.203–206 직관의 후속 정량화.]`

---

## §2.5 Block A 종합

**한 줄 정리** — 수직축 decoupling은 세 층으로 분해됨:
- **결합층** ($K_d$, $K_A$) — 약물이 수용체에 얼마나 잘 붙나
- **효능층** ($\tau$, 증폭 이득) — 같은 점유율이 얼마나 큰 반응으로 번지나
- **관찰층** ($E_{max}^{obs}$, $EC_{50}^{obs}$, Hill $\gamma$) — 임상에서 실제로 잡히는 곡선 모양

표준 $E_{max}$/Hill 식은 결합층과 효능층을 한 덩어리($EC_{50}$)로 묶은 식임. 그래서:
- 공변량 효과 해석 시 → 비결합 농도와 결합 분석으로 결합층/효능층 가르기.
- 부분효현제 외삽 시 → Operational model로 친화도와 효능 분리.
- 협역 치료역 보고서 작성 시 → **Hill $\gamma$를 빼지 말 것**. 위치보다 가파름이 안전 마진 결정.
- 모델 비교 시 → 농도 범위가 고원부 도달했는지 먼저 확인. 안 했으면 sigmoid 우월성 판별 자체가 불가능.

> 📊 **§2 큰 그림**: $K_d \to K_A$ (친화도) — $EC_{50}$ (효능 + 결합 혼합) — Hill $\gamma$ (가파름, 안전 마진의 진짜 키) — Black-Leff $\tau$ (효능 분리). 이 네 개념이 수직축 decoupling을 완전히 설명함.

---

# §3 — Block B: 수평축 decoupling 진단 — 히스테리시스

지금까지는 *정적*인 농도-반응 곡선을 다뤘음. 농도가 X면 효과는 Y, 정해진 함수 관계. 그런데 임상 데이터에서 이 그림이 자주 깨짐 — *시간*이 끼어들기 때문임.

같은 농도라도 농도가 올라가는 중이냐 내려가는 중이냐에 따라 효과가 다름. 농도-효과 평면에 시간 순서대로 점을 찍어 선으로 이으면 **고리(loop)** 가 그려짐. 이게 히스테리시스(hysteresis)임.

## §3.1 진단 — 두 임상 사례

**Digoxin 사례 (분포 지연)** — 1 mg IV bolus 후 첫 4시간. 혈장은 떨어지는데 좌심실 구출 시간은 오히려 올라감. 표면적으로는 "낮은 농도에서 더 큰 효과"처럼 보임. 진실은 — 심장 조직 분포와 수용체 결합이 느려서 혈장-효과 평형까지 약 6시간 필요. [Rowland & Tozer 5e p.234]

**Naproxen 사례 (시각적 진단)** — 500 mg PO 치과 통증 모델. 시간-농도와 시간-효과 곡선을 따로 보면 지연이 잘 안 보임. *그런데 농도-효과 평면에 그리면 반시계 방향 고리가 명확하게 나옴*. **같은 데이터를 어떤 평면에 그리느냐가 진단을 좌우함.** [Rowland & Tozer 5e p.234–235]

> 💡 **치트키 — 두 평면을 항상 같이 봐라**
> 시간-농도 / 시간-효과 두 도표만 보면 약한 지연은 잘 안 보임. **농도-효과 평면**에서 시간 순서대로 점을 이으면 고리가 시각적으로 드러남. 이게 히스테리시스 진단의 첫 단계임.

## §3.2 고리 방향이 알려주는 것

**반시계 방향 고리** — 효과가 농도보다 *늦게* 따라옴. 가장 흔한 패턴. 두 원천:
- **동력학적 지연 (kinetic delay)** — 약이 작용 부위에 늦게 도달하거나 결합/해리가 느림 → Block C의 effect compartment
- **역학적 지연 (dynamic delay)** — 측정 반응이 하류 시스템 전환이라 늦게 변함 → Block C의 indirect response

**시계 방향 고리** — 효과가 농도보다 *먼저* 떨어짐. 내성(tolerance), 길항 대사체, 음성 피드백 같은 상황. 이 강의 본 범위에서는 깊이 안 들어감.

[Rowland & Tozer 5e p.235–244]

## §3.3 진단 신호 — 다음 단계로 가는 다리

히스테리시스 고리를 봤다면 **두 가지를 추가로 확인**해서 Block C의 어느 구조로 갈지 좁힘:

| 진단 항목 | Effect Compartment 신호 | Indirect Response 신호 |
|---|---|---|
| 고리 폭 / 약물 반감기 비율 | 작은 폭, 빠른 평형 가능 | 큰 폭, 느린 회복 |
| **최대 효과 시점의 용량 의존성** | **용량 의존적** | **용량 비의존적** |
| 측정 종말점이 표적 결합에 얼마나 가까운가 | 가까움 (수용체 측 지연) | 멀음 (하류 시스템 측 지연) |

> 💼 **실무 인사이트 — Peak-time test**
> 용량 군별로 최대 효과 시점을 잼. 용량이 올라갈수록 peak time이 *바뀌면* → effect compartment 가능성. 용량이 바뀌어도 peak time이 *거의 일정*하면 → indirect response 가능성. 이게 모델 선택의 1차 분기점임.

## §3.4 함정 — 고리를 잡음으로 처리하면

히스테리시스를 "측정 잡음 같은 것"으로 치워버리면 **"혈장이 효과 부위를 즉시 대표한다"** 는 틀린 가정이 모델에 박혀버림. 그 모델로:
- 투여 간격 결정 → 빗나감
- 특수 집단 외삽 → 빗나감
- Peak/trough 시점 예측 → 빗나감

히스테리시스는 **잡음이 아니라 모델 구조를 바꾸라는 알람**임. 가장 안전한 디폴트는 "혈장 = 효과 부위"가 아니라 "혈장 ≠ 효과 부위, 다만 평형이 얼마나 빠른지 확인 필요"임. [Rowland & Tozer 5e p.244]

> 📖 **Rowland & Tozer 5e p.234 Fig.8-1; p.235 Fig.8-2** — 시각적 고리를 직접 봐야 와닿음. Fig.8-2에서 sampling number 순서를 따라가면, 농도-반응 관계가 **경로 의존적(path-dependent)** 이라는 게 그림으로 보임.

**Block B 한 줄 정리** — 히스테리시스는 *진단*. 농도-효과 평면에 시간 순서대로 점을 이어보고, 고리가 보이면 (1) 방향, (2) 폭/반감기 비, (3) peak-time 용량 의존성 — 세 가지를 봐서 다음 단계 구조 선택을 좁힘.

---

# §4 — Block C: 수평축 decoupling 구조화 — Effect Compartment vs Indirect Response

Block B에서 히스테리시스로 *지연을 감지*했음. 이제 그 지연을 **모델 안에 흡수**할 차례임. 두 가지 도구가 있고, *둘은 결코 호환되는 패치가 아님*. 어느 쪽을 고르느냐에 따라 외삽이 완전히 갈라짐.

전체 변환 사슬:
$$
\underbrace{C(t)}_{\text{혈장 농도}}
\to \underbrace{C_e(t)}_{\text{효과부위}}
\to \underbrace{E(t)}_{\text{관찰반응}}
$$

## §4.1 Effect Compartment — 부위 평형화 지연

**핵심 개념** — 혈장과 작용 부위 사이에 가상의 구획을 하나 더 둠. 약물이 그 구획으로 옮겨가는 데 시간 걸림. 이 시간을 $k_{e0}$ 한 파라미터로 흡수.

$$
\underbrace{\frac{dC_e}{dt}}_{\text{효과부위 변화}}
= \underbrace{k_{e0}}_{\text{평형화 속도}}
\left( \underbrace{C(t)}_{\text{혈장}} - \underbrace{C_e(t)}_{\text{효과부위}} \right)
$$

그 다음 $C_e(t)$를 $E_{max}$/Hill 식에 넣어 $E(t)$ 계산.

> 💡 **치트키 비유 — 복도의 지연**
> Effect compartment는 **약물이 표적 방까지 가는 복도의 지연**. 복도가 길고 좁으면 약이 늦게 도착함. 도착 후엔 즉시 반응. $k_{e0}$는 그 복도의 통과 속도.

**중요한 경고** — $C_e$는 *실제 미시적 장기 구획이 아님*. 조직 관류, 투과성, 조직 친화도, 결합 동역학, 신호전달 지연이 다 한 가상 구획에 묶인 **lumped delay representation**임. 그래서 **$k_{e0}$를 특정 생리 상수처럼 외삽하면 안 됨**. [Rowland & Tozer 5e p.235–236, p.245–246]

## §4.2 Indirect Response — 시스템 전환 지연

**핵심 개념** — 약물은 반응을 직접 만들지 않음. 약물이 **반응 변수의 생성/소멸을 바꿈**. 반응 자체가 자기 시간 척도($k_{in}/k_{out}$)로 천천히 변함.

기본 골격 (turnover model):
$$
\underbrace{\frac{dR}{dt}}_{\text{반응 변화}}
= \underbrace{k_{in}}_{\text{생성}}
- \underbrace{k_{out} \cdot R}_{\text{소실}}
$$

약물은 $k_{in}$이나 $k_{out}$을 **자극** 또는 **억제**할 수 있음. 네 가지 모델 변형이 가능 — $k_{in}$ 자극, $k_{in}$ 억제, $k_{out}$ 자극, $k_{out}$ 억제. [Gabrielsson & Weiner 5e p.229–230; Rowland & Tozer 5e p.241–248]

> 💡 **치트키 비유 — 생산라인의 지연**
> Indirect response는 **표적 방 안의 생산라인이 천천히 바뀌는 지연**. 약을 줘서 생산을 멈춰도, 이미 만들어진 제품이 소비되기까지 시간이 걸림. 생산라인의 회전 시간이 시스템 시간 척도.

**Warfarin 정전(canonical) 사례** — Vitamin K antagonist. Sodium warfarin 1.5 mg/kg PO. 혈장 농도가 빨리 변해도 항응고 효과는 **프로트롬빈 복합체 전환 (반감기 1–2일)** 에 묶여서 천천히 따라옴. 약은 진작에 정상상태에 들어갔는데도 INR은 며칠 더 움직임. [Rowland & Tozer 5e p.241–248]

$$
\underbrace{\frac{dR}{dt}}_{\text{반응 변화}}
= \underbrace{0}_{\text{peak / 평형}}
\quad\Longleftrightarrow\quad
\underbrace{\text{input}}_{\text{유입}} = \underbrace{\text{output}}_{\text{유출}}
$$

## §4.3 두 구조가 외삽에서 갈라지는 지점 ⚡

같은 히스테리시스 고리에 두 모델을 각각 적합하면 — **현재 데이터 적합은 비슷할 수 있음**. AIC도 비슷할 수 있음. 그런데 **외삽이 완전히 다름**.

### Peak-time test (가장 깔끔한 진단)

**Effect compartment** — Peak 시점은 $C(t)$와 $C_e(t)$의 평형 시점. 용량을 바꾸면 $C(t)$ 모양이 바뀌고 → $C_e(t)$ 모양도 바뀌고 → **peak time이 용량 의존적**.

**Indirect response** — Peak 시점은 $dR/dt = 0$ 시점, 즉 시스템의 유입=유출 시점. 시스템 시간 척도($k_{out}$)가 같으면 → 용량이 진폭만 바꿈 → **peak time이 용량 비의존적**.

### 외삽 차이의 임상 임팩트

**시나리오** — Phase 2 데이터에서 두 모델이 비슷하게 적합됨. 그냥 effect compartment를 선택. 그런데 진짜 기전이 indirect response.
- **투여 간격 추천** → 빗나감. 시스템 회복 시간 무시하고 약물 반감기 기준으로 추천하기 때문.
- **특수 집단 외삽** → 빗나감. 신기능 저하군에서 $k_{e0}$가 변할 거라고 잘못 가정.
- **Onset 예측** → 빗나감. 약을 시작하고 며칠 후 효과가 안정화될 텐데 짧게 예측.

> 💼 **실무 인사이트 — 모델 선택 순서**
> ① 혈장 직접 연결 적합 → 잔차에 systematic pattern 보면 시간 지연 의심.
> ② Effect compartment 적합 → 잔차가 깨끗해지는지 확인.
> ③ Peak-time 용량 의존성 보존되어 있으면 → effect compartment 유지.
> ④ Peak-time 용량 비의존적이면 → indirect response로 갈아탐.
> ⑤ $k_{e0}$가 혈장 제거 속도와 너무 가깝게 추정되면 (서로 분리 추정 안 됨) — 모델 식별 실패. 채혈 밀도 늘리거나 모델 단순화.

| 비교 항목 | Effect Compartment | Indirect Response |
|---|---|---|
| 지연 원천 | 부위 평형화 | 시스템 전환 |
| 비유 | 복도의 지연 | 생산라인의 지연 |
| Peak time | 용량 의존적 | 용량 비의존적 |
| 임상 예시 | Digoxin, Naproxen | Warfarin (vitamin K antagonist) |
| 외삽 시 핵심 | $k_{e0}$를 생리상수 취급 금지 | $k_{in}/k_{out}$ 단순 적합 파라미터 취급 금지 |

**Block C 한 줄 정리** — Effect compartment는 *복도의 지연*, indirect response는 *생산라인의 지연*. 같은 고리도 분포 문제냐 시스템 전환 문제냐에 따라 투여 간격·onset 예측·특수 집단 외삽이 다 갈라짐. 두 모델은 "delay 보정 패치"로 바꿔 쓸 수 없음.

---

# §5 — Block D: 종결시점 decoupling — AUEC, Duration, PK/PD 율속

이제 마지막 축. *약은 사라졌는데 효과는 안 사라지는 현상*을 다룸. 이게 임상 결정의 종착점임 — *총 효과량은 얼마인가, 효과는 언제까지 가는가, 그래서 투여 간격을 어떻게 잡을 것인가.*

## §5.1 AUEC — 반응-시간 곡선의 면적

AUC가 *농도*-시간 곡선의 면적이라면, AUEC는 *반응*-시간 곡선의 면적임.

$$
\underbrace{AUEC}_{\text{반응 총량}}
= \int_{\underbrace{0}_{\text{시작}}}^{\underbrace{\infty}_{\text{추적 끝}}}
\underbrace{E(t)}_{\text{순간반응}} \, dt
$$

| 파라미터 | 단위 | 의미 |
|---|---:|---|
| AUEC | 반응×시간 | 전체 반응 부담 (총 효과량) |
| $E(t)$ | 반응 단위 | 순간 반응 |
| $D$ | 용량 | 입력량 |
| $K$ | 시간$^{-1}$ | 1차 감소 속도 |
| $A_{min}$ | 양/효과 기준 | 최소 유효량 (역치) |

> 💡 AUEC는 *순간속도계가 아니라 여행 전체의 이동거리*. 짧고 강한 반응과 길고 약한 반응이 같은 면적을 만들 수 있으니, 면적만 보고 시간 구조를 지우면 안 됨.

### AUEC 폐쇄형 식 (제한 조건 명시)

**1구획 1차 제거 + 일반 $E_{max}$** 조건에서:
$$
\underbrace{AUEC}_{\text{AUEC}}
= \underbrace{\frac{E_{max}}{K}}_{\text{천장 × 시간}}
\ln\left(1 + \underbrace{\frac{D}{EC_{50} \cdot V}}_{\text{용량/감수성}}\right)
$$

`[출처: Gabrielsson & Weiner 5e p.233–234, Eq.3:72–3:73]`

**중요** — 이 식은 **일반 $E_{max}$ ($n=1$) + 1차 제거** 조건에서만 출처에 근거함. Sigmoid $E_{max}$ ($n \neq 1$)의 AUEC 폐쇄형은 출처에 없음. 수치 적분 필요 (이건 `[수학적 추론]`).

> 💡 **로그식 duration의 직관** — 물통 크기를 두 배로 해도 배수 시간이 두 배가 아님. 감소가 1차 과정이면 **용량 증가가 지속 시간을 선형이 아니라 로그로 늘림**.

## §5.2 효과 지속 시간 — 용량의 로그에 비례

Rowland & Tozer는 반응이 감소하는 **중간 영역(약 80–20% 최대치)** 에서 시간에 대해 거의 선형으로 감소할 수 있음을 보임. 그래서:

$$
\underbrace{t_D}_{\text{지속시간}}
= \underbrace{\frac{1}{K}}_{\text{감소시간상수}}
\ln\left(\underbrace{\frac{D}{A_{min}}}_{\text{용량/역치}}\right)
$$

**조건이 맞으면** — 용량을 두 배로 늘려도 지속 시간은 *약 반감기 1회분*만큼 늘어남.

**Succinylcholine 사례** — 0.5 mg/kg IV bolus. $k \approx 0.2 \text{ min}^{-1}$, $t_{1/2} \approx 4$ min. 용량-지속 시간 관계가 위 식과 일치. [Rowland & Tozer 5e p.249–256]

> 📖 **Rowland & Tozer 5e p.255 Fig.8-23; p.256 Fig.8-24** — 각 용량 곡선이 역치를 어디서 통과하는지 따라가 보면, "용량 두 배가 지속 시간 한 번의 반감기만큼 연장"이 그림으로 보임.

## §5.3 PK 율속 vs PD 율속 — 종결시점 decoupling의 핵심

지금까지의 식은 **PK가 율속**이라고 암묵적으로 가정함 (효과 감소 속도 = 약물 농도 감소 속도). 그런데 임상에서 이 가정이 깨지는 약이 한둘이 아님.

| | PK 율속 | PD 율속 |
|---|---|---|
| 효과 감소를 결정하는 것 | **약물 농도 감소 속도** | **수용체/시스템 회복 속도** |
| 시간 척도 | 혈장 $t_{1/2}$ | $t_{recovery}$, $\tau_{system}$ |
| 도구 | 식 in §5.2 | 시스템 회복 시간 분석 |

### 세 가지 임상 사례 — 모두 "혈장에서는 빨리 사라지는데 효과는 오래 감"

**Aspirin** 650 mg PO — 혈장 $t_{1/2}$ 약 **15분**, 항혈소판 활성 **수일**. [Rowland & Tozer 5e p.251]

**Omeprazole** 40 mg PO — 혈장 $t_{1/2}$ **1시간 미만**, 약 3시간 후 혈장은 거의 0인데 위산 분비 억제는 **수일** 단위로 회복. [Rowland & Tozer 5e p.252]

**Paclitaxel** — 혈장에는 2일 후 거의 없는데 백혈구 분율 변화는 **수주** 척도. [Rowland & Tozer 5e p.253]

> 💡 **치트키 — 0.5초 진단법**
> 두 도표의 x축 시간 단위를 봐라. 혈장 도표가 **hours**, 효과 도표가 **days**면 — **무조건 PD 율속**. 적합 통계 보기도 전에 도표 두 개만 비교해도 즉시 판별 가능. *시간축 자릿수 차이 자체가 율속 과정이 다르다는 직접 증거.*

### Acenocoumarol vs Phenprocoumon — 율속은 라벨이 아니라 스펙트럼

둘 다 vitamin K antagonist임:
- **Acenocoumarol**: $t_{1/2}$ **15시간**, 기저치 회복 약 **3 days**. 두 시간 척도가 비슷 → **PK가 율속에 가까움**.
- **Phenprocoumon**: $t_{1/2}$ **6 days**, 기저치 회복 약 **2 weeks**. 혈장 반감기가 시스템 전환 시간 안에 들어감 → **PD 시스템이 율속의 일부**.

핵심 메시지 — **PK/PD 율속은 약물 분류 라벨이 아니라, 두 시간 척도의 비율 $\tau_{drug}/\tau_{system}$에서 결정되는 스펙트럼**. 약 이름 하나로 정해지지 않음. [Rowland & Tozer 5e p.243–244, Fig.8-11]

$$
\underbrace{\tau_{drug}}_{\text{약물 t1/2}}
\quad\text{vs}\quad
\underbrace{\tau_{system}}_{\text{시스템 회복 시간}}
\;\Rightarrow\;
\begin{cases}
\tau_{drug} \gg \tau_{system} & : \text{PK 율속} \\
\tau_{drug} \ll \tau_{system} & : \text{PD 율속} \\
\tau_{drug} \approx \tau_{system} & : \text{스펙트럼 중간}
\end{cases}
$$

## §5.4 📌 교과서 외 보강 — Aspirin의 진짜 율속 기전

> 📌 **Rowland & Tozer 인용 "$t_{1/2}$ 15분, 항혈소판 수일"의 두 함정**
>
> R&T p.251이 인용한 aspirin 사례는 메시지(*PD 율속 = 시스템 회복*)는 정확함. 그런데 학습자가 모약물과 활성 대사체를 *구분하지 않으면*, "수일 지속"의 진짜 기전을 잘못 일반화할 위험이 있음.
>
> $$
> \overbrace{
> \underbrace{\text{Aspirin}}_{\text{acetylsalicylic acid, 모약물}}
> \xrightarrow{\underbrace{\text{esterase 가수분해}}_{\text{혈장·간}}}
> \underbrace{\text{Salicylate}}_{\text{활성 대사체}}
> }^{\text{모약물·대사체 사슬}}
> $$
>
> 세 시간 척도를 따로:
>
> | 화학종 / 효과 | $t_{1/2}$ | 비고 |
> |---|---:|---|
> | **Aspirin (acetylsalicylic acid)** | $\approx$ 15–20 분 | R&T 인용값. esterase로 빠르게 가수분해 |
> | **Salicylate (활성 대사체)** | **2–30 시간, 용량 의존적** | Michaelis-Menten 포화 제거 (glycine·glucuronide conjugation 포화). 고용량에서 비선형 연장 |
> | **항혈소판 활성** | **수일 (≈7–10일)** | 혈소판 수명에 가까운 시간 척도 |
>
> **결정적 — "수일 지속"의 율속은 salicylate 잔존이 아님.** 모약물 aspirin이 혈소판 COX-1 효소의 Ser529 잔기를 **비가역적으로 acetylation**해서, 그 혈소판이 새로 만들어질 때까지 (혈소판은 핵이 없어 자체 단백질 합성 불가) 효소 회복 불가.
>
> $$
> \underbrace{\text{COX-1}_{\text{Ser529-OH}}}_{\text{활성형}}
> + \underbrace{\text{Aspirin}}_{\text{모약물}}
> \xrightarrow{\underbrace{\text{비가역}}_{\text{covalent}}}
> \underbrace{\text{COX-1}_{\text{Ser529-O-acetyl}}}_{\text{불활성, 회복 불가}}
> + \underbrace{\text{Salicylate}}_{\text{부산물}}
> $$
>
> **PD 율속의 진짜 원천 두 가지**:
> ① **효소 비가역 작용** (COX-1 covalent acetylation) — 약이 없어도 효소가 회복 안 됨.
> ② **혈소판 회전 시간** (turnover) — 새 혈소판이 생성되어야 COX-1 풀이 복구됨.
>
> 약물(모약물이든 대사체든) 잔존이 율속이 *아님*.
>
> **공통 구조** — Aspirin / Omeprazole / Paclitaxel 셋 다 *"비가역 효소·구조 결합 + 표적 세포 회전"* 이 율속임:
> - Aspirin → COX-1 비가역 acetylation + 혈소판 회전
> - Omeprazole → H+/K+ ATPase 비가역 결합 + 위벽세포 회전
> - Paclitaxel → 미세소관 결합 + 세포 회전
>
> 단순히 "활성 대사체가 길어서"로 외워버리면 이 공통 구조가 안 보임.
>
> `[교과서 외 보강 — Awtry EH, Loscalzo J. Aspirin. Circulation. 2000;101(10):1206-18. Patrono C, et al. Drugs. 2017;77(10):1059-72. R&T 5e p.251 본문 사례의 임상약리 보강.]`

## §5.5 Block D 함정 — Methylprednisolone

**PK 선형성이 PD 선형성을 보장하지 않음.** Methylprednisolone은 PK AUC가 용량에 비례해도 림프구 반응이 고용량 구간에서 *포화*됨. 곧 더 높은 용량은 정보를 추가하지 않고 고원부를 반복 확인하는 셈. 하류 바이오마커나 투여 간격 종말점을 다시 설계해야 함. [Rowland & Tozer 5e p.257–258]

**Block D 한 줄 정리** — 종결시점 decoupling은 *약물 시간 척도와 시스템 시간 척도의 비*에서 결정됨. 혈장 반감기로 효과 지속 시간을 결정하면 PD 율속 약물에서 항상 빗나감. 진단은 두 도표의 x축 자릿수 차이를 보는 것에서 시작. 그 다음 율속 기전(비가역 결합 + 표적 세포 회전 같은) 을 식별.

---

# §6 — Block E: 만성 투여로 가는 다리 — 정상상태 E-R 평면

지금까지는 단회 투여 후 시간 지연을 다뤘음. 실제 만성 투여 의사결정에서는 다른 평면이 필요함.

## §6.1 📌 교과서 외 보강 — 정상상태 E-R 관계와 개별 titration

> 📌 **시간축에서 농도축으로 — 의사결정 평면 전환**
>
> **정상상태 도달 조건**: 다회 투여로 약 $4\text{–}5 \times t_{1/2}$ (PK 율속) 또는 $4\text{–}5 \times \tau_{system}$ (PD 율속, 더 긴 쪽이 율속) 후, 평균 정상상태 농도 $\overline{C}_{ss}$와 그 시점 평균 반응 $\overline{E}_{ss}$가 한 점에 모임. 이 점들을 환자군 전체에서 모으면 **정상상태 E-R 곡선**이 됨.
>
> $$
> \overbrace{
> \underbrace{\overline{E}_{ss}}_{\text{정상상태 평균 반응}}
> = \underbrace{E_0}_{\text{기저치}}
> - \frac{
>   \underbrace{I_{max}}_{\text{억제 천장}}
>   \cdot \underbrace{\overline{C}_{ss,u}^n}_{\text{비결합 정상상태^n}}
> }{
>   \underbrace{EC_{u50}^n}_{\text{비결합 EC50^n}}
>   + \underbrace{\overline{C}_{ss,u}^n}_{\text{비결합 정상상태^n}}
> }
> }^{\text{만성 dosing의 의사결정 평면}}
> $$
>
> **이 식이 임상에서 갖는 의미 두 가지**:
>
> **① 개체간 변이의 두 축 분해**
> $$
> \underbrace{\text{관찰 } \overline{E}_{ss} \text{ 변이}}_{\text{개체간 변이}}
> = \overbrace{f(\underbrace{\text{CL 변이}}_{\text{PK 측}})}^{\text{PK 변이}}
> \;\circ\;
> \overbrace{f(\underbrace{EC_{u50}, E_{max}, \gamma \text{ 변이}}_{\text{PD 측}})}^{\text{PD 변이}}
> $$
> 임상 개별 titration은 결국 이 두 축의 변이를 흡수하는 작업임.
>
> **② 시간 지연의 한 점 수렴**
> $$
> \overbrace{
> \underbrace{C(t) \to C_e(t) \to E(t)}_{\text{단회 — 시간 지연 명시적}}
> \xrightarrow{\underbrace{\text{정상상태 도달}}_{4\text{–}5 \, t_{1/2}}}
> \underbrace{\overline{C}_{ss,u} \to \overline{E}_{ss}}_{\text{만성 — 시간 지연 한 점에 흡수}}
> }^{\text{시간축 → 농도축 평면 전환}}
> $$
> 정상상태에서는 $C_e \approx C$이라서 Block B–C의 히스테리시스가 *한 점으로 수렴*. 만성 dosing은 정상상태 E-R 곡선 위 위치로 결정.
>
> **단, PD 율속 약물에서는 이 가정 자체가 깨짐.** $\overline{C}_{ss}$가 0에 가까워도 효과는 유지됨 → 농도 평면이 아니라 **반응-시간 평면**에서 직접 dosing 결정.
>
> | 약물 유형 | 의사결정 평면 | titration 단계 |
> |---|---|---|
> | **PK 율속 만성 투여** | 정상상태 E-R 평면 | $\overline{C}_{ss,u}$ 조정 |
> | **PD 율속 만성 투여** | 반응 회복 시간 + 효과 지속 시간 | 투여 간격 또는 누적 약리 효과 조정 |
>
> 이 평면 전환이 후속 세션(PopPK/PD 공변량 모델링, exposure-response 시뮬레이션) 의 직접 다리임.
>
> `[교과서 외 보강 — Sheiner LB, Holford NH. Clin Pharmacol Ther. 1981;30(6):817-23; Holford NH, Sheiner LB. Clin Pharmacokinet. 1981;6(6):429-53. G&W 5e p.221 (비결합 환산), R&T 5e p.249–253 (PD 율속) 본문 사실을 만성 투여 의사결정 맥락으로 확장.]`

---

# §7 — 혼동 쌍 빠른 정리

다섯 카드 분량을 다 봤음. 이제 임상·보고서에서 자주 헷갈리는 네 쌍을 정리. 각 쌍마다 **어디서 헷갈리고, 헷갈리면 임상 결과가 어떻게 나오는가** — 이 두 질문에 답함.

## Pair 1 — $K_d$ vs $EC_{50}$ (결합층 vs 기능층)

| 기준 | $K_d$ | $EC_{50}$ |
|---|---|---|
| 층위 | 분자 (결합 친화도) | 시스템 (결합 + 증폭 + 조직 반응) |
| 수식 위치 | 점유율 분모 $[C] + K_d$ | 효과식 분모 $EC_{50} + C$ |
| 변하는 원인 | 결합/해리 속도 | 결합 + 수용체 밀도 + 증폭 + 조직 반응 |
| 혼동 시 임상 결과 | 결합 친화도를 기능적 역가로 오인 | 공변량 효과를 수용체 감수성 변화로 단정 |

**기억 고리** — $EC_{50} < K_d$ *가능*함. 여분 수용체 10% 점유로 90% 효과 가능. 결합과 효능은 다른 층위.

**핵심 교정** — $EC_{50}$이 공변량에 따라 변하면 비결합 농도 + 결합 분석으로 **약물 측 vs 시스템 측** 가르기.

## Pair 2 — 일반 $E_{max}$ ($n=1$) vs Sigmoid $E_{max}$ ($n \neq 1$) ⚡

| 기준 | 일반 $E_{max}$ | Sigmoid $E_{max}$ |
|---|---|---|
| 곡선 모양 | 완만한 쌍곡선 | 가파른 S자 (n에 따라) |
| 식별 조건 | 일반 농도 범위 | **고원부 도달 + $EC_{50}$ 주변 + 충분한 정밀도** |
| 혼동 시 임상 결과 | 고원부 없는 데이터에서 $E_{max}$ 식별 불안정 | 농도 범위 좁으면 $n$ 식별 불안정 → 안전 마진 과대평가 |

**기억 고리 — 위치 vs 가파름** — $EC_{50}$은 곡선이 *어디 있나* (위치), Hill $\gamma$는 *얼마나 가파른가* (가파름). 협역 치료역에서는 **위치보다 가파름이 안전 마진을 결정함**.

**치명적 타격** — Hill $\gamma$를 보고서에서 빼고 $EC_{50}$만 제출하면, 협역 치료역 약물(vancomycin, tacrolimus, 항부정맥제, vitamin K antagonist) 의 임상 용량 조절 가이드가 *과관대*하게 설계됨 → 독성 과소예측 → 규제 deficiency. `[교과서 외 규제 해석]`

**$n > 1$은 협동성 증명이 아님** — 가설로는 가능, 증명 아님. 현상학적 가파름 파라미터.

## Pair 3 — Effect Compartment vs Indirect Response

| 기준 | Effect Compartment | Indirect Response |
|---|---|---|
| 비유 | 복도의 지연 | 생산라인의 지연 |
| 지연 원천 | 부위 평형화 | 시스템 전환 |
| Peak time | 용량 의존적 | 용량 비의존적 |
| 외삽 함정 | $k_{e0}$를 생리 상수 취급 | $k_{in}/k_{out}$ 단순 적합 파라미터 취급 |

**빠른 진단** — 용량 군별 peak-time 비교. 변하면 effect compartment, 일정하면 indirect response.

## Pair 4 — PK 율속 vs PD 율속

| 기준 | PK 율속 | PD 율속 |
|---|---|---|
| 결정 인자 | $t_{1/2}$ | $t_{recovery}$, $\tau_{system}$ |
| 시간축 단위 | 두 도표 비슷 | **한 자릿수 이상 차이** |
| 임상 예시 | Acenocoumarol에 가까움 | Aspirin, Omeprazole, Paclitaxel |
| 혼동 시 임상 결과 | 투여 간격 적절 | 효과 지속 시간 과소예측 → 투여 간격 과조밀 |

**0.5초 진단법** — 도표 두 개의 x축 자릿수 비교. 한 자릿수 차이면 **즉시 PD 율속 확정**.

---

**§7 한 줄 정리** — 네 쌍이 결국 같은 질문 하나로 환원됨: **"지금 보는 숫자가 결합, 부위 농도, 측정 반응, 시스템 회복 중 어느 층위를 대표하는가?"** 가장 위험한 혼동은 **"농도가 반응을 즉시 구동한다"** 는 가정. 이게 깨지는 순간 네 쌍 전부 연결됨.

---

# §8 — 자기 테스트 (능동 회상)

**Q1.** 질량작용법칙에서 $E = E_{max} \cdot C / (K_d + C)$를 도출하시오.

> 평형: $k_1 [R][C] = k_{-1}[RC]$, $K_d = [C][R]/[RC]$. $[R_T] = [R] + [RC]$ 대입 → $[RC]/[R_T] = C/(C + K_d)$. $E = \alpha [RC]$, $E_{max} = \alpha [R_T]$ 대입 → $E/E_{max} = C/(C + K_d)$. `[G&W 5e p.202–204]`

**Q2.** $K_d$와 $EC_{50}$이 다른 이유를 한 문장으로.

> $K_d$는 수용체 결합 친화도, $EC_{50}$은 결합 + 신호전달 + 반응 증폭까지 포함하므로 여분 수용체나 증폭 연쇄가 있으면 둘이 다를 수 있음. `[G&W 5e p.204–206]`

**Q3.** Hill $n = 2.03$을 "협동성 증거"라고 쓰면 왜 틀리는가?

> G&W는 Hill 지수가 직접적 생물학적 해석을 갖지 않는다고 명시함. $n = 2.03$은 데이터 가파름을 설명하는 현상학적 파라미터. 협동성은 *가능한 가설*이지 증명이 아님. `[G&W 5e p.216, p.220, p.735]`

**Q4.** Sigmoid 억제 $I_{max}$ 모델에서 목표 반응 해석 시 기저치 상대값과 절대값을 구분하시오.

> 절대 반응 $E_{target}$이 주어지면 먼저 $I = E_0 - E_{target}$로 억제 크기 계산, 그 다음 $I/I_{max}$를 분율로 두고 농도 역산. 기저치 상대 반응을 절대 반응처럼 넣으면 부호와 비율이 둘 다 틀어짐. `[G&W 5e p.218–221]`

**Q5.** Naproxen 히스테리시스에서 지지되지 않는 $k_{e0}$ 수치를 쓰지 말고 출처에 근거한 결론만.

> R&T는 naproxen 500 mg PO 치과 통증 모델에서 비결합 농도와 통증 완화가 반시계 방향 히스테리시스를 보이고, effect compartment가 이 히스테리시스를 줄이는 개념적 모델을 제시함. $k_{e0}$ 특정 수치는 본 PDF 범위 안에서 확인 안 됨. `[R&T 5e p.234–246]`

**Q6.** Warfarin 반응이 혈장 농도를 즉시 따라가지 않는 이유?

> Warfarin 효과는 **프로트롬빈 복합체 전환**(반감기 1–2일)을 통해 나타나므로 혈장 농도 변화와 반응 변화가 분리됨. Sodium warfarin 1.5 mg/kg PO 사례. `[R&T 5e p.242, p.247]`

**Q7.** AUEC 폐쇄형 식의 적용 조건?

> $AUEC = (E_{max}/K) \ln(1 + D/(EC_{50} V))$는 **일반 $E_{max}$ + 1차 제거** 조건에서만 출처에 근거. Sigmoid $E_{max}$ 의 폐쇄형은 출처에 없음 (수치 적분 필요, `[수학적 추론]`). `[G&W 5e p.233–234]`

**Q8.** Aspirin과 omeprazole 사례로 PD 율속 지속 시간을 설명.

> Aspirin 650 mg PO: 혈장 $t_{1/2}$ 15분, 항혈소판 활성 수일. Omeprazole 40 mg PO: 혈장 $t_{1/2}$ 1시간 미만, 위산 억제는 수일. 효과 지속 시간이 약물 반감기가 아니라 **시스템/수용체 회복**에 의해 제한됨. `[R&T 5e p.251–252]`
>
> 📌 **보강** — Aspirin $t_{1/2}$ 15분은 **모약물 acetylsalicylic acid**의 값. 활성 대사체 salicylate는 용량 의존적 $t_{1/2}$ 2–30시간. "수일 지속"의 진짜 율속은 **COX-1 비가역 acetylation + 혈소판 회전 시간**. `[교과서 외 보강]`

**Q9.** Phase 2 데이터에서 반시계 방향 히스테리시스를 봤음. 모델 선택 순서?

> ① 혈장 직접 적합으로 잔차 systematic pattern 확인. ② Effect compartment 적용해서 히스테리시스 축소되는지. ③ Peak time 용량 의존성 확인 — 변하면 effect compartment, 일정하면 indirect response. ④ AIC만 보지 말고 **peak-time 용량 의존성 + 채혈 밀도 + 생물학적 타당성** 같이 봄.

**Q10.** Black-Leff Operational Model에서 Hill $n = 1$일 때 $EC_{50}^{obs}$와 $K_A$, $\tau$의 관계? 완전효현제와 부분효현제 극한 비교.

> $n = 1$ 단순 hyperbolic: $EC_{50}^{obs} = K_A / (1 + \tau)$, $E_{max}^{obs} = E_m \tau / (1 + \tau)$.
> - 완전효현제 ($\tau \gg 1$): $EC_{50}^{obs} \to K_A / \tau$ (spare receptor), $E_{max}^{obs} \to E_m$.
> - 부분효현제 ($\tau \ll 1$): $EC_{50}^{obs} \approx K_A$, $E_{max}^{obs} \approx E_m \tau$ (천장 낮음).
>
> 표준 $E_{max}$/Hill 로는 $K_A$와 $\tau$ 분리 불가 → 부분효현제 임상 외삽 시 operational model 필요. `[교과서 외 보강 — Black & Leff 1983]`

---

# §9 — 메타 프레임과 다음 세션으로의 다리

## 다섯 가지 실패 모드와 1차 조치 — 한 표로

| 실패 모드 | 1차 파라미터 | 임상 결과 | 1차 조치 |
|---|---|---|---|
| $K_d$를 $EC_{50}$처럼 사용 | 결합/기능 층위 혼동 | 기능적 역가 오인 | Assay source + unbound 기준 확인 |
| Hill $n$을 기전 증명으로 과해석 | 가파름 파라미터 | 용량 조절 위험 과소평가 | 농도 범위 + 고원부 + 정밀도 동시 검토 |
| 히스테리시스를 잡음 처리 | 시간 지연 | 지연 원천 누락 → 외삽 실패 | 고리 방향 + 폭 + peak-time 진단 |
| PK 반감기로 투여 간격 결정 | $t_{1/2}$ vs $t_{recovery}$ | PD 율속 약물 지속 시간 오판 | $\tau_{drug}/\tau_{system}$ 비교 |
| AUEC를 단순 AUC처럼 취급 | 반응 적분 조건 | endpoint 정의 누락 | 역치 + 반응 변수 + 시간 척도 명시 |

## 계량약리학자의 진짜 일

계량약리학자가 일하는 자리는 **복잡한 식을 많이 아는 자리**가 아님. 같은 농도-효과 데이터를 두고 **무엇이 부족한지 구분할 줄 아는 자리**임. 더 좋은 최적화기? 더 넓은 농도 범위? 더 가까운 바이오마커? 더 긴 반응 채취? — **이 네 갈래를 가르는 게 진짜 실력.**

PD3가 그 예임 — 0–500 µg/L에서는 sigmoid 우월성이 명확하지 않은데, 0–800 µg/L에서는 모델 판별 가능. **모델 선택은 통계 기법 문제만이 아니라 실험 설계 문제.** [Gabrielsson & Weiner 5e p.734–741]

R&T Ch.8이 추가로 가르치는 것 — 혈장이 낮아져도 효과 남으면, "이상한 현상" 으로 보지 말고 **"시스템 전환이나 비가역 작용이 더 느린 과정인가?"** 를 묻는 것. [Rowland & Tozer 5e p.249–253]

## 다음 세션으로 가는 다리

| 후속 세션 | 이 강의에서 열린 개념 | 이 강의 없으면 실패하는 것 |
|---|---|---|
| PopPK/PD 공변량 모델링 | $EC_{50}$, $E_{max}$, Hill $\gamma$ 층위 분리 + 정상상태 E-R 두 축 분해 | 공변량 효과를 잘못된 생물학 층위에 배정 |
| Exposure-response 시뮬레이션 | 농도 범위, 고원부, sigmoid 식별 가능성 | 용량 조절 step과 안전 마진 과대평가 |
| Delay/turnover 모델링 | Effect compartment vs indirect response | 히스테리시스 원천 오분류 → 외삽 실패 |
| 투여 간격 최적화 | AUEC, duration, PK/PD 율속 | 혈장 반감기만으로 지속 시간 판단 |
| 부분효현제 임상 외삽 | Black-Leff operational model ($K_A$, $\tau$ 분리, n=1 특수 해 포함) | $E_{max}$/Hill로는 친화도와 효능 분리 못 함 |
| 만성 dosing titration | 정상상태 E-R 평면 + PD 율속 분기 | 단회 모델로 만성 의사결정 외삽 |

## 경계 플래그 — 안 다룬 것

`[확인 필요 — 첨부 PDF 미포함 구간]`:
- **G&W 5e §3.6.2–§3.6.5** (pp.225–228): competitive antagonism 이후 interaction model. 이 강의에서 추정·보완 안 함.
- **G&W 5e §3.12 baseline modeling**: §2.2 한계에서 baseline time-varying issue로만 언급. 상세 모델링은 보류.
- `[확인 필요 — 교과서 외 규제 적용]`: PD 율속 약물 특수 집단 용량 조정, FDA guidance 문구는 본 PDF 범위 밖.

---

## 🎯 세 줄로 압축한 최종 결론

> ① **수직축**: $E_{max}$/Hill 모델은 결합층 + 효능층 + 가파름을 분리. **Hill $\gamma$가 협역 치료역의 진짜 안전 마진 결정자.**
> ② **수평축**: 히스테리시스는 잡음이 아니라 모델 구조 알람. Effect compartment(부위 평형화)와 indirect response(시스템 전환)는 **바꿔 쓸 수 없는 다른 인과 구조** — peak-time 용량 의존성이 분기점.
> ③ **종결시점**: 효과 지속 시간은 약물 반감기가 아니라 **그보다 더 느린 시스템 회복 과정**이 결정. 두 도표 x축 자릿수 차이가 0.5초 진단.
>
> 임상 케이스 하나를 만나면 머릿속에서 *"이건 어느 축에서 깨진 거지?"* 한 번만 물으면 됨. 그 다음엔 도구 상자에서 맞는 모델을 꺼내면 됨.

---

## 부록: Remastered 변경 이력

| 항목 | 원본 위치 | Remaster 위치 | 변경 종류 |
|---|---|---|---|
| 마스터 프레임 (수직축/수평축/종결시점 decoupling 3분류) | 분절된 카드 C1–C5 | §1 모든 후속 블록 | **신규 구조화** — 모든 개념을 3축에 슬롯팅 |
| 임상 장면 3개 하드 오프닝 (Digoxin/Naproxen/Aspirin) | 흩어진 사례 | §1 도입 | **재배치** — 세 사례가 3축에 각각 매핑 |
| Block A 통합 (Kd/EC50 + Emax/Hill + PD3 + Black-Leff) | C1, C2 분리 | §2 한 블록 | **통합** — 수직축 decoupling 한 줄로 |
| 비밀번호·복도·생산라인·스위치 비유 | 부분 존재 | §2, §3, §4 | **신규 추가** — 직관 비유 강화 |
| Peak-time test 진단법 명시 표 | 산문 안에 분산 | §3.3, §4.3 | **명시화** — 진단 의사결정 알고리즘으로 |
| 0.5초 진단법 (x축 자릿수 비교) | §5에 부분 언급 | §5.3, §7 Pair 4 | **강조** — 즉시 진단 도구로 명시 |
| 만성 투여 정상상태 E-R | C5 끝 박스 | §6 별도 블록 | **승격** — 후속 세션 다리로 독립 |
| 출처 표기 통일 (G&W 5e / R&T 5e 전체 명기) | 부분적 약어 사용 | 본문 전체 | 표기 통일 |
| 어미 음슴체 | 본문은 합쇼체 혼재 | 본문 전체 | **체계 변경** |
| Black-Leff n=1 특수 해 | v4.0 보강본 final에서 추가 | §2.4 보강 박스 | **보존** |
| Aspirin 모약물·대사체 분리 + COX-1 acetylation | C5 보강 박스 | §5.4 보강 박스 | **보존** |
| 정상상태 E-R + Sheiner-Holford | C5 보강 박스 | §6 보강 박스 | **보존, 위상 승격** |

**원본 대비 내용 보존 검증** — 다음 모든 항목 보존됨:
- G&W 5e Ch.3 본문 사실 (질량작용법칙, $E_{max}$/Hill 식, 비결합 환산, AUEC 폐쇄형, PD3 사례, 최소 설계 요건)
- R&T 5e Ch.8 본문 사실 (digoxin, naproxen, warfarin, aspirin, omeprazole, paclitaxel, succinylcholine, methylprednisolone, acenocoumarol/phenprocoumon, effect compartment, indirect response, duration-log dose)
- 교과서 외 보강 3건 (Black-Leff operational model + n=1 단순해, Aspirin 모약물·대사체 + COX-1 비가역, 정상상태 E-R + Sheiner-Holford)
- 모든 자기 테스트 10문항
- 모든 경계 플래그 (G&W §3.6.2–§3.6.5, §3.12, 규제 적용)

**고유번호**: C-260518-094215-J3R

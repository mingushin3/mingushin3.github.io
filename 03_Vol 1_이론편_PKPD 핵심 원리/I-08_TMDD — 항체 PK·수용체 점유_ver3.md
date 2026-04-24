기준 초안의 핵심 구조와 수치 앵커는 유지했고, 이해 난도가 높아지는 지점에만 `💡 직관 브릿지`, `⚠️ 헷갈림 방지`, `🧭 읽는 순서` 주석을 삽입했습니다. 특히 원 초안의 4대 보강축인 플립플롭 조건식, TMDD $DES$ 초기조건, Table 2.13 알로메트릭 연결, ADA 시간 사건 감별은 그대로 살렸습니다.  TMDD와 MM 근사 선택 문제는 문헌에서도 독립적으로 다루는 핵심 이슈이며, NONMEM `ADVAN13`은 stiff/non-stiff ODE 자동 전환을 위해 LSODA를 사용하는 것으로 공식 가이드에 명시됩니다. ([PubMed][1]) Anakinra는 DailyMed 기준으로 신기능 저하에서 clearance가 감소하고 severe renal insufficiency/ESRD에서는 격일 투여 고려가 명시되어 있어, 카드 1의 신기능-소분자 단백질 연결 설명을 임상적으로 지지합니다. ([DailyMed][2])

---

# I-08 TMDD — 항체 PK·수용체 점유

## PK/PD Mastery Protocol V5.4 | Step 1 친절 주석 강화판

*(V5.3 최종 강화판 기반 — 핵심 내용 고정, 설명표시·주석·비유만 선별 삽입)*

---

# §1 — Session Header & Roadmap

**소스:**

* **Gabrielsson & Weiner 5e** — §2.6.1–2.6.3·§2.6.5·§2.6.7·Table 2.11·Table 2.13 (pp.94–111) + Case Study PK27 (pp.602–610) + Case Study PK30 (pp.100–101)
* **Rowland & Tozer 5e (R&T)** — Chapter 21: Protein Drugs (pp.687–730), Tables 21-6·21-9·21-13·21-15·21-16·21-21, Figures 21-5·21-7·21-9·21-10·21-14·21-16·21-17·21-18·21-19·21-20

---

**Big Idea (한 문장):**

단백질 약물의 PK는 분자량이 배정한 물리적 경로 위에 세워지고, 그 위에서 TMDD는 표적 turnover가 결합되면서 PD 작용 부위와 소실 경로가 동일한 존재가 되는 현상이다 — 따라서 항체 PK/PD 모델링의 본질은 농도 곡선 피팅이 아니라, 리간드·표적·복합체 세 생체계의 동역학을 동시에 식별하는 일이다.

> 💡 **이 문장의 쉬운 버전:**
> 작은 단백질은 “신장으로 빠지는 약”처럼 행동하고, 큰 항체는 “림프·세포·수용체·FcRn 사이를 도는 생체 시스템”처럼 행동한다. TMDD는 그중에서도 약이 표적에 붙는 순간, 표적이 단순한 작용점이 아니라 약을 없애는 배수구가 되는 현상이다.

---

**개념 항법도:**

1. 단백질 약물 PK의 구조적 특이성 — 분자량이 경로를 결정한다
2. 내인성 Turnover — 수용체 pool의 ODE 원형과 Figure 2.70의 숨겨진 통찰
3. **[Apex] TMDD 풀 모델** — 4개 ODE의 구조적 필연성과 $K_m \neq K_d$ 착각 + NONMEM 초기조건
4. TMDD 4상 패턴 — 농도-시간 곡선으로 지배 방정식을 읽는 눈
5. MM 근사의 계보와 구조적 한계
6. 데이터 식별성·임상 번역·면역원성 감별

**지식 그래프 위치:**

* **선행 필수:** I-01, I-04, I-07, I-09
* **직접 열어주는 것:** II-04($DES$ ODE 코딩·ADVAN13 강성 솔버), II-08(공변량 — $R_0$·질환 심각도), II-11(NONMEM PK/PD 결합)
* **의존하는 고급 도메인:** Bispecific mAb PK, ADC 복합 모델, PBPK-TMDD 통합

> 🧭 **읽는 순서:**
> 카드 1은 “단백질 약물이 몸 안에서 어디로 가는가”, 카드 2는 “수용체가 왜 고정된 벽면이 아니라 살아 움직이는 pool인가”, 카드 3은 “그 둘이 결합했을 때 왜 TMDD ODE가 생기는가”를 설명한다. 카드 4 이후는 그래프·근사·규제 판단으로 넘어가는 응용부다.

---

# §2 — Concept Anatomy Cards

---

## 카드 1: 단백질 약물 PK의 구조적 특이성 — 분자량이 경로를 결정한다

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가:** Anakinra(17 kDa)를 ESRD 환자에게 표준 용량으로 투여하면 AUC가 정상인 대비 크게 증가한다. 반대로 150 kDa mAb는 신기능이 완전히 붕괴해도 PK가 거의 변하지 않는다. “단백질 약물 = 신기능 조정”이라는 단순 직관이 **분자량 경계 하나**를 모르면 완전히 틀린다.

**체화해야 할 단 하나의 직관:** 분자량이 커질수록 혈관 모세관은 닫히고 림프계가 열린다 — 이 단 하나의 물리 원리가 흡수 속도, 분포 용적, 신장 처리, 반감기의 패턴을 동시에 결정한다.

**이 직관을 머릿속에 박고 아래를 읽어라:** “고분자는 림프계의 승객이다”를 유지한 채 아래 수치를 읽으면 교과서 전체가 하나의 물리 원리에서 파생된다.

> 💡 **임상약사식 비유:**
> Vancomycin에서 CrCl을 먼저 보는 습관은 작은 단백질에는 맞지만, mAb에는 그대로 적용하면 안 된다. Anakinra는 “신장 배수구를 타는 비교적 작은 단백질”이고, mAb는 “신장 여과막을 통과하지 못하는 대형 화물”이다.

---

**A. Formal Definition**

단백질 약물(MW ~1–200 kDa)의 PK:
(1) 흡수 — MW 의존적 혈관/림프계 분기
(2) 분포 — $V_d \approx$ 혈장~세포외액
(3) 소실 — MW에 따라 사구체 여과·수용체 매개 내포·FcRn 재순환으로 갈린다.

> ⚠️ **헷갈림 방지:**
> 여기서 핵심은 “단백질 약물은 모두 비슷하다”가 아니다. 단백질 약물 내부에서도 17 kDa, 40 kDa, 150 kDa는 완전히 다른 교통망을 탄다.

---

**B. 핵심 데이터 앵커링**

**림프계 흡수의 MW 의존성 (R&T Figure 21-16, Supersaxo 양 실험):**

SC 투여 후 배출 림프에서 회수된 비율:

| 화합물             | MW (g/mol) |   림프 회수율 |
| --------------- | ---------: | -------: |
| FUdR            |        246 |      ~2% |
| Inulin          |      5,200 |     ~20% |
| Cytochrome C    |     12,300 |     ~40% |
| Interferon-α-2a |     19,000 | **~60%** |

`[출처: R&T 5e, Ch.21, Figure 21-16; Supersaxo et al. Pharm Res 1990;7:167-169]`

> 💡 **한 줄 해석:**
> SC 주사 후 분자가 커질수록 바로 혈관으로 들어가기 어렵고, 느린 림프 통로를 우회로처럼 타게 된다. 그래서 큰 단백질의 SC 흡수는 “빠른 정맥 진입”이 아니라 “림프를 통한 완만한 배달”에 가깝다.

**사구체 체 계수 (R&T Table 21-9, Maack et al.):**

| 단백질                  | MW (g/mol) |  사구체 체 계수 |
| -------------------- | ---------: | --------: |
| Insulin              |      6,000 |      0.89 |
| Myoglobin            |     16,900 |      0.75 |
| Growth hormone       |     22,000 |      0.65 |
| Superoxide dismutase |     32,000 |      0.33 |
| Albumin              |     69,000 | **0.001** |

`[출처: R&T 5e, Ch.21, Table 21-9]`

> 💡 **비유:**
> 사구체는 체와 같다. Insulin은 거의 빠져나가는 모래, albumin은 체에 걸리는 자갈이다. 150 kDa mAb는 자갈보다 더 큰 화물이라 사구체 여과 경로와 사실상 무관하다.

**mAb $V_d$ 실측치 (R&T Table 21-6):** 0.043–0.18 L/kg — 혈장 공간 수준.
`[출처: R&T 5e, Ch.21, Table 21-6]`

> ⚠️ **해석 포인트:**
> mAb의 $V_d$가 작은 것은 “분포가 없다”는 뜻이 아니라, 세포 안쪽이나 깊은 조직으로 자유롭게 퍼지지 못한다는 뜻이다. 즉, 큰 항체는 대부분 혈장·세포외액이라는 제한된 공간 안에서 움직인다.

---

**FcRn 재순환 — 4단계 기전 (R&T Figure 21-5):**

1. 혈중 IgG → 내피세포/단핵세포 endocytosis → 산성 엔도좀(pH ~6.0)
2. 낮은 pH에서 FcRn이 IgG Fc 부위 고친화도 결합
3. FcRn-IgG 복합체 → 재순환 → 세포 표면 귀환
4. 생리적 pH(7.4)에서 친화도 급감 → 혈중 방출

**결과:** IgG t½ ≈ 21일. R&T 원문: “Binding to FcRn is typically **nonsaturable at therapeutic mAb concentrations**.” FcRn 포화는 혈청 IgG ≥ **30 mg/mL**에서야 발생 → t½ ~11일 단축.
`[출처: R&T 5e, Ch.21, Figure 21-5, p.708; Gabrielsson 5e, §2.6.7, Figure 2.84]`

> 💡 **비유:**
> FcRn은 IgG의 “세포 내 구조대”다. 세포가 IgG를 삼킨 뒤 그냥 lysosome으로 보내면 분해되지만, 산성 엔도좀에서 FcRn이 붙으면 “이건 버리지 말고 다시 혈액으로 돌려보내라”는 재활용 표식이 붙는다.

---

**▶ 플립플롭 수학 — ①결함 보완**

플립플롭 성립 조건: $k_{el} < k_a$. 이 조건에서 SC 말단 기울기 = $k_a$, SC 말단 t½:

$$
t_{1/2,SC} \approx \frac{0.693}{k_a}
\quad \text{(플립플롭 조건 하, } k_{el} < k_a \text{)}
$$

> ⚠️ **여기서 가장 중요한 점:**
> SC 말단 t½이 길다고 해서 항상 “소실이 느리다”는 뜻은 아니다. SC에서는 흡수가 더 느리면, 말단 기울기가 소실이 아니라 흡수를 반영한다. 즉, 마지막 직선의 주인은 배수구($k_{el}$)가 아니라 수도꼭지($k_a$)일 수 있다.

**Anakinra 정량적 증명 (R&T Tables 21-16·21-21):**

| 상황   |      IV t½ |      SC t½ |                   AUC 배수 |
| ---- | ---------: | ---------: | -----------------------: |
| 정상   |      2.6 h |     5.24 h |                       기준 |
| 혈액투석 | **7.15 h** | **9.71 h** | **6.7배↑(IV), 3.9배↑(SC)** |

“The elimination half-life must exceed that of the absorption half-life before any change is expected in the terminal decline.” (R&T 원문)

**메커니즘:** CrCl 95→41 mL/min: $k_{el}$ 감소하지만 여전히 $k_{el} > k_a$ → flip-flop 유지 → SC t½ 거의 불변. AUC = Dose·F/CL이므로 CL 감소에 직접 비례 → AUC 폭증. ESRD에서야 $k_{el} < k_a$ 역전 → flip-flop 해제 → SC t½ 9.71h.

`[출처: R&T 5e, Ch.21, Tables 21-16·21-21, Figures 21-18·21-20, pp.723-729]`

> 💡 **임상적으로 기억할 문장:**
> “AUC는 CL을 보고, SC 말단 t½은 때로 $k_a$를 본다.”
> 그래서 신기능 저하에서 AUC는 크게 변해도 SC t½은 한동안 거의 안 변할 수 있다.

**Somatropin 플립플롭 실증 (R&T Figure 21-17):** MW 22,125 g/mol, IV t½=2.1h, SC 후 24h 이상 흡수 지속.

---

**F. Five Cognitive Layers**

| 레이어    | 내용                                                                                        |
| ------ | ----------------------------------------------------------------------------------------- |
| L1 수학  | 플립플롭: $t_{1/2,SC} \approx 0.693/k_a$ (조건: $k_{el}<k_a$); AUC = Dose·F/CL → CL 감소가 AUC를 구동 |
| L2 기하학 | MW-permeability 그래프: 5,000–60,000 g/mol 구간에서 수 자릿수 급락                                     |
| L3 동형성 | 사구체 여과 = 분자 크기 크로마토그래피의 생체 내 버전                                                           |
| L4 생리  | FcRn: pH-switch 포획-방출 사이클. 산성→포획, 중성→방출                                                   |
| L5 실무  | PopPK 공변량: CrCl(MW < 30 kDa만), FcRn 다형성; SC 용량 설계 시 flip-flop 확인 우선                       |

---

**G. Zettelkasten Atom**

```yaml
---
aliases: [단백질 약물 PK, biologic PK, lymphatic absorption, FcRn recycling, flip-flop]
tags: [pharmacometrics/pk, biologic/absorption, biologic/elimination, FcRn]
up: "[[I-08 TMDD MOC]]"
related: ["[[TMDD 풀 모델]]", "[[SC flip-flop 반감기]]", "[[Anakinra 신기능 역설]]"]
source: "R&T 5e, Ch.21, pp.700-730; Gabrielsson 5e, §2.6.2, Table 2.10"
---
```

단백질 약물 PK 결정인자: 분자량 → (1) 흡수: MW>16kDa → 림프계 50%↑; (2) 분포: mAb $V_d$=0.043–0.18 L/kg; (3) 소실: MW<30kDa → 신장 주경로; IgG → FcRn t½=21일. **플립플롭 조건**: $k_{el}<k_a$ → SC t½ ≈ 0.693/$k_a$. Anakinra: IV t½=2.6h → ESRD 7.15h; AUC 6.7배↑(IV), SC AUC 3.9배↑. 150 kDa mAb: 사구체 체 계수 ≈ 0 → 신기능 무관.

---

## 카드 2: 내인성 Turnover — 수용체 pool의 ODE 원형과 Table 2.13의 동형성

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가:** TMDD 수용체 ODE가 “선험적으로 존재”하는 것이 아님을 이해해야 한다. 내인성 단백질 항상성의 기초 수학 없이는 수용체가 왜 고정 binding site가 아니라 **태어나고 죽는 생체 pool**인지 이해 불가하다.

**체화해야 할 단 하나의 직관:** $k_{in}$을 바꾸면 **정상상태 수준만** 달라지고 $T_{ss}$는 그대로다. $k_{out}$을 바꾸면 **수준과 $T_{ss}$ 동시에** 달라진다 — 이 비대칭성이 “수용체가 많아졌다”와 “수용체 대사가 느려졌다”를 임상적으로 구분하는 열쇠다.

> 💡 **비유:**
> 욕조에 물이 들어오고($k_{in}$), 배수구로 빠진다($k_{out}$). 수도꼭지를 더 열면 물높이는 올라가지만 새 평형에 도달하는 시간감각은 크게 바뀌지 않는다. 배수구를 좁히면 물높이도 올라가고, 물이 바뀌는 속도 자체도 느려진다.

---

**B. 수식 도출 + Table 2.13 동형성 — ③결함 보완**

**기본 Turnover ODE:**

$$
\frac{dA}{dt} = k_{in} - k_{out} \cdot A \quad [Eq.\ 2{:}237]
$$

정상상태:

$$
A_0 = \frac{k_{in}}{k_{out}}
$$

반감기:

$$
t_{1/2} = \frac{\ln 2}{k_{out}}
$$

Turnover time:

$$
\bar{t} = \frac{1}{k_{out}}
= \frac{t_{1/2}}{\ln2}
\approx 1.44 \cdot t_{1/2}
$$

$$
\bar{t} = \frac{V_{ss}}{CL} = MRT \quad [Eq.\ 2{:}243]
$$

`[출처: Gabrielsson 5e, §2.6.1, Eqs 2:237–2:244, pp.94-96]`

> ⚠️ **중요한 해석:**
> $A_0$는 “얼마나 쌓여 있는가”이고, $1/k_{out}$은 “얼마나 빨리 교체되는가”다. 같은 $A_0$라도 $k_{in}$과 $k_{out}$이 모두 큰 시스템은 빠르게 태어나고 빠르게 사라지는 pool이고, 둘 다 작은 시스템은 느리게 유지되는 pool이다.

---

**Gabrielsson Table 2.13 — 세 모델의 구조적 동형성 (완전판):**

|                   | **청소율 모델**                        | **Turnover 모델**                    | **반응 모델**                          |
| ----------------- | --------------------------------- | ---------------------------------- | ---------------------------------- |
| 주 변수              | $C$                               | $A$                                | $R$                                |
| 파라미터              | $V, Cl$                           | $k_{in}, k_{out}$                  | $k_{in}, k_{out}$                  |
| ODE               | $V \cdot dC/dt = In - CL \cdot C$ | $dA/dt = k_{in} - k_{out} \cdot A$ | $dR/dt = k_{in} - k_{out} \cdot R$ |
| 기저값               | 0                                 | $k_{in}/k_{out}$                   | $k_{in}/k_{out}$                   |
| t½                | $\ln2 \cdot V_{ss}/CL$            | $\ln2/k_{out}$                     | $\ln2/k_{out}$                     |
| MRT/Turnover time | $V_{ss}/CL$                       | $1/k_{out}$                        | $1/k_{out}$                        |
| **알로메트릭 스케일**     | $CL \propto BW^b$                 | $k_{in} \propto BW^b$              | $k_{in} \propto BW^b$              |
| **스케일**           | $k \propto BW^{-0.25}$            | $k_{out} \propto BW^{-0.25}$       | $k_{out} \propto BW^{-0.25}$       |
| **스케일**           | $MRT \propto BW^{0.25}$           | $\bar{t} \propto BW^{0.25}$        | $\bar{t} \propto BW^{0.25}$        |

`[출처: Gabrielsson 5e, §2.6.5, Table 2.13, p.105]`

> 💡 **동형성의 한 문장 요약:**
> 약물이 몸에서 사라지는 모델, 내인성 단백질이 교체되는 모델, PD 반응이 켜졌다 꺼지는 모델은 모두 “들어오는 힘 − 나가는 힘”이라는 같은 뼈대를 가진다. 이름만 $C$, $A$, $R$로 바뀔 뿐 구조는 같다.

**핵심 통찰:** $k_{out} \propto BW^{-0.25}$는 청소율 모델의 $k_{el}$과 동일 스케일 법칙. TMDD 수용체의 $k_{out}$도 동일 법칙으로 종간 스케일 가능 — I-13 알로메트릭 세션과 직접 연결.

---

**Figure 2.70의 두 패널 (Gabrielsson §2.6.1):**

* $R_{in}(k_{in})$ 변화: 정상상태 수준만 이동, $T_{ss}$ 불변
  *(infusion rate 변경과 유사)*
* $k_{out}$ 변화: 정상상태 수준 + $T_{ss}$ 동시 이동
  *(clearance 변경과 유사)*

> ⚠️ **실무적 감별 포인트:**
> 환자군에서 soluble target baseline이 높다고 해서 무조건 “생산 증가”라고 해석하면 안 된다. $k_{in}$ 증가와 $k_{out}$ 감소는 baseline 상승이라는 같은 표면현상을 만들지만, 시간 반응과 washout 예측은 다르다.

---

**IgX PK30 파라미터 (Gabrielsson, SC 40 µg/kg, 건강인 1명):**

| 파라미터                    |    값 | 단위      |
| ----------------------- | ---: | ------- |
| $Cl/F$                  | 0.03 | L/h/kg  |
| $V/F$                   | 0.10 | L/kg    |
| $k_{in}$                | 0.78 | µg/h/kg |
| $k_{out}$               | 0.27 | h⁻¹     |
| t½                      |  2.5 | h       |
| Turnover time $\bar{t}$ |  2.7 | h       |

**식별성 한계:** SC 데이터만으로 $Cl$와 $k_{in}$ 개별 추정 불가.

$$
C_{baseline} = \frac{k_{in}}{Cl}
$$

즉, 비율만 식별된다. IV 투여 필수.

`[출처: Gabrielsson 5e, §2.6.3, Figure 2.74, p.101]`

> 💡 **쉽게 말하면:**
> SC 데이터만 있으면 “생산이 많은지”와 “청소율이 낮은지”를 분리해서 보기 어렵다. 같은 baseline 농도는 높은 $k_{in}$과 높은 $Cl$의 조합으로도, 낮은 $k_{in}$과 낮은 $Cl$의 조합으로도 만들어질 수 있다.

---

**면역글로불린 클래스별 Turnover (Gabrielsson Table 2.11):**

|              | IgA | IgD |    IgE | **IgG** | IgM |
| ------------ | --: | --: | -----: | ------: | --: |
| MW (kDa)     | 160 | 175 |    190 | **150** | 950 |
| t½ (일)       | 5.8 | 2.8 |    2.5 |  **23** | 5.1 |
| 분획 이화율 (%/일) |  25 |  37 | **89** |     6.7 |  18 |

IgG t½=23일의 이유: FcRn이 $k_{out}$을 6.7%/일로 극소화. IgE 분획 이화율 89%/일 = FcRn 결합 구조 부재의 직접 결과.

`[출처: Gabrielsson 5e, §2.6.3, Table 2.11, p.102; Waldmann et al. 1970]`

---

**G. Zettelkasten Atom**

```yaml
---
aliases: [Turnover model, IgX PK30, immunoglobulin turnover, Figure 2.70, Table 2.13 isomorphism]
tags: [pharmacometrics/pk, turnover/endogenous, biologic/immunoglobulin, allometric]
up: "[[I-08 TMDD MOC]]"
related: ["[[TMDD 수용체 ODE]]", "[[FcRn 메커니즘]]", "[[Clearance-Turnover 동형성]]", "[[알로메트릭 스케일링]]"]
source: "Gabrielsson 5e, §2.6.1-2.6.3, Table 2.11·2.13, Figure 2.70·2.74, pp.94-105"
---
```

Turnover ODE: $dA/dt = k_{in} - k_{out}A$. Figure 2.70: $k_{in}$ 변화 → 정상상태만 이동($T_{ss}$ 불변); $k_{out}$ 변화 → 수준+$T_{ss}$ 동시. $\bar{t} = t_{1/2}/\ln2$. **Table 2.13 동형성**: CL모델·Turnover·Response 동형; **알로메트릭 확장**: $k_{out} \propto BW^{-0.25}$, $\bar{t} \propto BW^{0.25}$. IgX PK30: $k_{out}=0.27/h$, $\bar{t}=2.7h$. IgG t½=23일 vs IgE 2.5일.

---

## 카드 3 [⚡ Apex Concept]: TMDD 풀 모델 — 4개 ODE + NONMEM 구현 브릿지

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가:** FIH 첫 투여 용량의 MABEL 산정, 환자-건강인 PK 차이의 규제적 설명, Phase 1 assay 설계 결정 — 이 셋은 모두 TMDD 8개 파라미터를 이해하지 못하면 방어 불가하다. 특히 “$K_m = K_d$”라는 착각은 표적 포화 농도를 수십~수백 배 과대 추정하게 한다.

**체화해야 할 단 하나의 직관:** TMDD 모델에서 수용체($R$)는 약물의 PD 작용 부위인 동시에 약물의 소실 경로 자체다 — $R_0$가 클수록 $CL_{total}$이 크다.

> 💡 **핵심 비유:**
> 일반 PK에서 receptor는 “약이 효과를 내는 문손잡이”처럼 느껴진다. 하지만 TMDD에서는 그 문손잡이가 약을 붙잡은 뒤 안으로 끌고 들어가 분해시키는 “배수구”이기도 하다. 즉, target abundance가 곧 clearance capacity가 된다.

---

**B. 4개 ODE 도출 (Gabrielsson PK27 + R&T Ch.21 통합)**

**ODE 1 — 리간드 중심 구획 (Eq. 27:1):**

$$
\frac{dC_L}{dt} =
\frac{1}{V_c}
\left[
Input_L

* CL_L \cdot C_L
* Cl_d(C_L - C_t)
* k_{on} \cdot C_L \cdot R

- k_{off} \cdot C_{RL}
  \right]
  $$

> 🧭 **읽는 법:**
> 이 식은 리간드가 중심구획에서 어떻게 줄고 늘어나는지를 말한다.
> $CL_L \cdot C_L$은 비특이적 제거, $Cl_d(C_L-C_t)$는 조직과의 교환, $k_{on}C_LR$은 target에 붙어 사라지는 항, $k_{off}C_{RL}$은 복합체가 풀려 다시 돌아오는 항이다.

**ODE 2 — 조직 구획:**

$$
\frac{dC_t}{dt} =
\frac{Cl_d}{V_t}(C_L - C_t)
$$

**ODE 3 — 수용체 Turnover (Eq. 27:2):**

$$
\frac{dR}{dt} =
k_{in}

* k_{out} \cdot R
* k_{on} \cdot C_L \cdot R

- k_{off} \cdot C_{RL}
  $$

> 💡 **수용체 식의 직관:**
> 수용체는 새로 만들어지고($k_{in}$), 자연적으로 사라지고($k_{out}R$), 약과 결합해 사라지고($k_{on}C_LR$), 복합체가 해리되면 다시 돌아온다($k_{off}C_{RL}$).

**ODE 4 — 복합체 (Eq. 27:3):**

$$
\frac{dC_{RL}}{dt} =
k_{on} \cdot C_L \cdot R

* k_{off} \cdot C_{RL}
* k_{e(RL)} \cdot C_{RL}
  $$

$$
K_m =
\frac{k_{off} + k_{e(RL)}}{k_{on}},
\quad
K_d =
\frac{k_{off}}{k_{on}}
$$

`[출처: R&T 5e, Ch.21, Eqs 21-1~21-6, p.711; Gabrielsson 5e, PK27, Eqs 27:1~27:3, pp.606-607]`

> ⚠️ **한 줄 구조:**
> $K_d$는 “붙었다 떨어지는 순수 결합 친화도”이고, $K_m$은 “붙은 뒤 내부화되어 사라지는 손실까지 포함한 PK적 포화 척도”다. 둘을 같다고 두면 TMDD의 핵심인 internalization을 지워버리는 셈이다.

---

**▶ NONMEM 구현 브릿지 — ②결함 보완**

**$DES 블록 초기조건 설정 원리:**

```nonmem
$DES
; 상태변수: A(1)=C_L*Vc, A(2)=C_t*Vt, A(3)=R, A(4)=RL

; 초기조건 (NONMEM $PK 블록에서 설정)
R0   = KLIN / KOUT          ; 정상상태: R0 = kin/kout
                              ; 약물 투여 전 수용체는 항상성 유지

; INIT 설정:
; A_0(1) = 0                ; 리간드: 투여 전 0
; A_0(2) = 0                ; 조직 리간드: 0
; A_0(3) = R0               ; 수용체: 정상상태 = kin/kout ← 핵심
; A_0(4) = 0                ; 복합체: 0

DADT(1) = (Input_L - CLL*A(1)/VC - CLDD*(A(1)/VC - A(2)/VT) &
           - KON*A(1)/VC*A(3) + KOFF*A(4)) / VC

DADT(2) = CLDD*(A(1)/VC - A(2)/VT) / VT

DADT(3) = KLIN - KOUT*A(3) - KON*A(1)/VC*A(3) + KOFF*A(4)

DADT(4) = KON*A(1)/VC*A(3) - KOFF*A(4) - KERL*A(4)
```

> ⚠️ **초기조건이 중요한 이유:**
> 투여 전 리간드와 복합체는 0이어도, 수용체는 0이면 안 된다. 생체는 투여 전에도 receptor pool을 유지하고 있기 때문이다. $R(0)=0$으로 시작하면 모델은 “표적이 없는 몸에 약을 넣은 뒤, 시간이 지나며 표적이 생기는” 비생리적 세계를 시뮬레이션한다.

**강성 ODE 시간 스케일 분리 문제:**

* $k_{on}$ 시간 스케일: **분 단위**
* $k_{out}$·$CL_L$ 시간 스케일: **시간~일 단위**
* 비율 = $k_{on}/k_{out}$ ≈ 수백~수천배 → **Stiff ODE**
* NONMEM 솔버 선택: **ADVAN13** 또는 **ADVAN15**
* FOCE INT 사용 필수; TOL 설정 ≥ 6 권장

```nonmem
$SUBROUTINES ADVAN13 TOL=6
```

> 💡 **stiff ODE 비유:**
> 한 모델 안에 “눈 깜짝할 사이에 일어나는 결합”과 “며칠에 걸쳐 변하는 turnover”가 같이 들어 있다. 초고속 시계와 저속 시계를 한 번에 맞춰야 하므로 일반 ODE보다 수치적으로 훨씬 까다롭다.

**Molar units 경고 (Gabrielsson PK27 p.610):** $k_{on}$은 2차 속도 상수 [L/(mg·h)] 또는 [nM⁻¹·h⁻¹]. mg와 nmol 단위 혼용 시 $k_{on}$ 추정값이 분자량 배수만큼 달라짐 → 단위 통일 필수.

> ⚠️ **실무 함정:**
> TMDD 모델에서 단위 오류는 단순 scale error가 아니다. $k_{on}$, $K_d$, $K_m$, $R_0$가 모두 연결되어 있기 때문에 단위 하나가 표적 포화 농도와 MABEL 해석까지 오염시킨다.

---

**PK27 파라미터 (cynomolgus monkey mAb, Table 27.2):**

| 파라미터        |         추정값 | L-only CV% | L+R+RL CV% |
| ----------- | ----------: | ---------: | ---------: |
| $k_{on}$    |       0.096 |        17% |     **1%** |
| $k_{off}$   |       0.001 |        27% |     **3%** |
| $k_{e(RL)}$ | 0.002–0.003 |        27% |     **2%** |
| $k_{out}$   |       0.009 |         6% |     **2%** |
| $R_0$       |     12 mg/L |         4% |     **1%** |

`[출처: Gabrielsson 5e, PK27, Table 27.2, p.609]`

> 💡 **해석:**
> ligand만 보면 모델은 “약 농도 곡선 하나”에서 결합·해리·내재화·수용체 turnover를 모두 추측해야 한다. ligand + receptor + complex를 같이 보면, 모델은 눈을 하나 더 얻는다. 그래서 CV%가 급격히 줄어든다.

---

**C-2. Plausible Fallacy — “$K_m = K_d$” 착각 [Apex Concept]**

**오류의 형태:** MM 피팅 $K_m$을 in vitro SPR $K_d$와 동일시.

**왜 수학적으로 불가능한가:**

$$
K_m - K_d =
\frac{k_{e(RL)}}{k_{on}}
\geq 0
\quad \text{(수학적 필연)}
$$

> 💡 **직관 브릿지:**
> $K_d$는 결합이 얼마나 잘 풀리는지만 본다. $K_m$은 결합이 풀리기 전에 복합체가 세포 안으로 끌려 들어가 사라지는 손실까지 본다. 그래서 $K_m$에는 “내재화 세금”이 붙는다.

**PK27 정량적 증거:**

|                        |                 값 (mg/L) |
| ---------------------- | -----------------------: |
| $K_d = k_{off}/k_{on}$ |              ≈ **0.010** |
| $K_m$(TMDD 풀 모델)       |               ≈ **0.03** |
| MM 피팅 $\hat{K}_m$      | **3.7** → **123배 과대 추정** |

“The estimated $K_m$ value 3.7 is **dramatically over predicted** (3.7 as compared to **0.03** obtained from the TMDD model).” (Gabrielsson PK27 원문)

`[출처: Gabrielsson 5e, PK27, Figure 27.6, p.609]`

**GOF 시그니처 — “Phase D 낙차 오인 패턴”:**

MM을 저용량 포함 다용량에 피팅 → 말단 Phase D 구간 **CWRES 음성 편향(< –2)**. 이유: MM 저농도 극한 기울기 = $V_{max}/K_m$ ≠ Phase D 실제 기울기 $k_{e(RL)}$.

> ⚠️ **규제적 의미:**
> $K_m$을 $K_d$처럼 해석하면 표적 점유율과 포화 농도 예측이 무너진다. GOF가 그럴듯해 보여도, 말단 저농도 영역에서 구조적으로 틀린 모델이면 FIH/MABEL 방어가 취약해진다.

---

**G. Zettelkasten Atom**

```yaml
---
aliases: [TMDD full model, Mager Jusko 2001, TMDD ODE, Km-vs-Kd, ADVAN13, stiff ODE]
tags: [pharmacometrics/pk, TMDD/full-model, biologic/mAb, Apex-Concept, NONMEM/ADVAN13]
up: "[[I-08 TMDD MOC]]"
related: ["[[TMDD 4상 패턴]]", "[[MM 근사 한계]]", "[[ADVAN13 강성 솔버]]"]
source: "R&T 5e, Ch.21, Eqs 21-1~21-6, p.711; Gabrielsson 5e, PK27, pp.602-610, Table 27.2"
---
```

TMDD 풀 모델: 4 ODE, 초기조건 $R(0)=k_{in}/k_{out}$·$C_{RL}(0)=0$ 필수. **강성 ODE**: $k_{on}$(분) vs $k_{out}$(일) → ADVAN13 TOL≥6. $K_m=(k_{off}+k_{e(RL)})/k_{on}$, $K_d=k_{off}/k_{on}$, 항상 $K_m \geq K_d$. PK27: MM $K_m$=3.7 vs 실제 0.03 → **123배 과대**. L-only: $k_{off}$·$k_{e(RL)}$ CV=27%; L+R+RL: CV=3·2%.

---

## 카드 4: TMDD 4상 패턴 — 곡선으로 지배 방정식을 읽는 눈

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가:** 다용량 semi-log 플롯에서 저용량 곡선이 고용량보다 가파르게 교차한다 — 이것이 TMDD Phase A 시그니처임을 즉각 인식하는 눈이 없으면 잘못된 모델 구조 선택이 이어진다.

**체화해야 할 단 하나의 직관:** 용량이 낮을수록 Phase D가 일찍, 더 두드러지게 나타난다. 다용량 곡선의 교차(cross-over)가 TMDD의 시각적 시그니처다.

> 💡 **그래프를 보는 법:**
> Semi-log plot에서 직선이면 “1차 소실”이라고만 생각하면 부족하다. TMDD에서는 직선이 두 번 나온다. Phase B의 직선은 비특이적 clearance, Phase D의 직선은 target-mediated complex internalization을 반영한다.

---

**B. 4상 지배 방정식 (Gabrielsson Figure 27.7, R&T Figure 21-9):**

| Phase | 농도 조건             | 지배 방정식                                                        | 특징                                   |
| ----- | ----------------- | ------------------------------------------------------------- | ------------------------------------ |
| **A** | 고농도, 수용체 풍부       | $-dC_L/dt \approx k_{on} \cdot C_L \cdot R$                   | 2차 반응, 저용량이 더 가파름, **다용량 교차**        |
| **B** | $C_L \gg R_0$, 포화 | $-dC_L/dt \approx (CL_L/V_c) \cdot C_L$                       | 1차, 평행, semi-log 직선, 기울기=$CL_L/V_c$  |
| **C** | 혼합                | $-dC_L/dt \approx (CL_L/V_c)C_L + k_{in} \cdot C_L/(C_L+K_d)$ | 비선형 전환, 용량 곡선 수렴                     |
| **D** | $C_L \ll K_m$     | $-dC_L/dt \approx k_{e(RL)} \cdot C_L$                        | 1차, semi-log 직선, **기울기=$k_{e(RL)}$** |

`[출처: Gabrielsson 5e, PK27, Figure 27.7, p.610; R&T 5e, Ch.21, Figure 21-9, p.712]`

> 🧭 **Phase 암기법:**
> A = receptor가 아직 배고파서 약을 적극적으로 잡아먹는 구간.
> B = receptor가 배불러서 비특이적 clearance만 보이는 구간.
> C = 다시 target-mediated clearance가 살아나는 전환 구간.
> D = 농도가 낮아져 target이 다시 지배하는 말단 구간.

**PK27 실제 데이터 (cynomolgus, 4 IV bolus):**

| 용량 (mg/kg) | 초기 $C_L$ (mg/L) | $C_L/R_0$ |
| ---------- | --------------: | --------: |
| 1.5        |             ~30 |      2.5배 |
| 45         |            ~900 |       75배 |

**Phase B vs Phase D 구별 필수:** 둘 다 semi-log 직선이지만 기울기가 의미하는 파라미터가 완전히 다름.

> ⚠️ **헷갈림 방지:**
> Phase B와 Phase D는 둘 다 직선이라 눈으로 보면 비슷하다. 그러나 Phase B는 “표적 포화 후 남은 일반 배수구”, Phase D는 “표적이 다시 살아난 배수구”다. 같은 직선, 다른 생리다.

---

**▶ 면역원성 감별 정량화 — ④결함 보완**

**ADA(항약물항체) 매개 소실의 시간 패턴 (R&T Figure 21-19, cynomolgus tetanus toxoid):**

| 시점         | 이벤트       |
| ---------- | --------- |
| 0 h        | 투여        |
| ~200 h     | ADA 검출 시작 |
| ~400–500 h | ADA peak  |

**정량적 감별 기준:**

| 특성       | **TMDD Phase D**               | **ADA 매개 소실**                      |
| -------- | ------------------------------ | ---------------------------------- |
| 의존성      | **농도 의존적** ($C_L < K_m$ 진입 시)  | **시간 의존적** (~200h 이후)              |
| 모델 진단    | 단일 투여에서도 발생; 용량별 곡선 특정 농도에서 수렴 | 반복 투여 trough 사이클마다 지속 하락           |
| GOF 시그니처 | 저용량 말단 CWRES 음성 편향             | 후기 사이클 관측값 < 예측값, ADA titer와 CL 상관 |

`[출처: R&T 5e, Ch.21, pp.712, Figure 21-19, p.725]`

> 💡 **한 문장 감별법:**
> Phase D는 “농도가 낮아졌기 때문에” 생기고, ADA는 “시간이 지나 면역계가 반응했기 때문에” 생긴다. 전자는 Y축 농도 사건, 후자는 X축 시간 사건이다.

---

**G. Zettelkasten Atom**

```yaml
---
aliases: [TMDD 4상, Phase ABCD, cross-over pattern, ADA vs Phase D]
tags: [pharmacometrics/pk, TMDD/phases, biologic/mAb, immunogenicity]
up: "[[I-08 TMDD MOC]]"
source: "Gabrielsson 5e, PK27, Figure 27.7; R&T 5e, Figure 21-9, Figure 21-19"
---
```

4상: A(2차, 교차) → B($CL_L/V_c$, 포화, 평행) → C(혼합) → D($k_{e(RL)}$, 탈포화). **Phase B vs D**: 기울기 의미 완전히 다름. ADA 감별: 농도 사건(Phase D) vs 시간 사건(ADA, 200h~; Figure 21-19).

---

## 카드 5: MM 근사의 계보와 구조적 한계

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가:** MM 근사는 TMDD 풀 모델을 빠르게 요약하는 유용한 도구이지만, 모든 농도 범위를 설명하는 모델이 아니다. 특히 저농도 Phase D와 target occupancy 예측이 중요한 상황에서는 “잘 맞는 단순 모델”이 아니라 “중요한 구간을 틀리게 단순화한 모델”이 될 수 있다.

**체화해야 할 단 하나의 직관:** MM은 target이 거의 포화되어 있을 때의 그림자다. 그림자가 본체를 대신할 수 있는 구간이 있고, 절대 대신할 수 없는 구간이 있다.

---

**MM 근사 적용 조건 (R&T Ch.21 원문):**

> “adequate when drug concentrations **significantly exceed target concentrations** or when target occupancy is **close to 100%**”

* QE(quasi-equilibrium): $k_{e(RL)} \ll k_{off}$ → $K_d$ 사용
* QSS(quasi-steady state): $K_{ss}=(k_{off}+k_{e(RL)})/k_{on}$
* MM 근사: TO>90–100% 또는 $C_L \gg R_0$

> ⚠️ **해석:**
> MM은 “표적이 이미 거의 포화되어 있는 상황”에서는 실용적이다. 그러나 저농도에서 receptor가 다시 약을 잡아먹기 시작하는 Phase D를 설명하려면, receptor와 complex를 상태변수로 남겨야 한다.

**PK27 구조적 실패:** MM $K_m$=3.7 vs 실제 0.03 → **123배**.
“structurally very different behaviour, which cannot mimic the complete concentration and time range.”
`[출처: Gabrielsson 5e, PK27, p.609]`

---

## 카드 6: 데이터 식별성·임상 번역·UK-279,276

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가:** TMDD 모델은 데이터가 충분하지 않으면 기전적으로 멋진 수식을 쓰고도 파라미터가 식별되지 않는다. 반대로 ligand·target·complex를 함께 측정하면 단순 농도 곡선에서는 보이지 않던 결합·해리·내재화 구조가 갑자기 분리된다.

**체화해야 할 단 하나의 직관:** TMDD는 모델링 문제가 아니라 assay design 문제이기도 하다. 데이터를 생성하기 전에 무엇을 측정할지 정하지 못하면, 나중에 아무리 좋은 모델을 써도 식별성은 회복되지 않는다.

---

**PK27 식별성 Table 27.2:** L-only → $k_{off}$·$k_{e(RL)}$ CV=27%; L+R+RL → CV=2–3%.

> 💡 **실무 해석:**
> Phase 1에서 soluble target 또는 complex assay를 빼면, 모델러는 나중에 “왜 이 파라미터 RSE가 큰가”를 설명하는 사람이 된다. 반대로 처음부터 assay를 설계하면, 모델러는 “임상 설계를 바꾸는 사람”이 된다.

**UK-279,276 (R&T Figure 21-10):** MW 41 kDa, CD11b 길항제. 뇌졸중 → $R_0$↑ → $CL_{TMDD}$↑ → 건강인 PK 외삽 실패. $R_0$를 질환 심각도 공변량으로 사전 정의 필수.

**약동학적 vs 약력학적 속도 제한:**

* Eptifibatide: t½=2h, 효과 즉각 → **PK 속도 제한**
* Leuprolide: t½=3h, testosterone 효과 ~2주 → **PD 속도 제한**

> ⚠️ **헷갈림 방지:**
> t½이 짧다고 효과도 빨리 사라지는 것은 아니다. 약물 농도가 효과를 제한하면 PK-limited, downstream 생리 반응이 효과를 제한하면 PD-limited다.

---

# §5 — Confusion Pair Dissection

## 혼동쌍 1: $K_m$ vs $K_d$ ← Critical Blow

| 비교 차원       | **$K_m$**                                                                                                                 | **$K_d$**                      |
| ----------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **수식**      | $(k_{off} + k_{e(RL)})/k_{on}$                                                                                            | $k_{off}/k_{on}$               |
| **크기 관계**   | 항상 $K_m \geq K_d$                                                                                                         | 기준 결합 친화도                      |
| **PK27**    | MM 피팅: 3.7 mg/L                                                                                                           | TMDD: 0.010 mg/L               |
| **오차**      | **123배 과대**                                                                                                               | —                              |
| **⚡ 기억 고리** | $K_m$은 $K_d$에 내재화 세금($k_{e(RL)}/k_{on}$)이 붙은 것이다. 복합체가 리소좀으로 비가역 소실될수록 같은 $C_L$에서 더 많은 수용체를 써버리므로, 절반 포화 농도($K_m$)가 올라간다. | $K_d$는 결합했다가 풀리는 순수 affinity다. |

**💥 Critical Blow:**
NDA 임상약리 섹션에서 in vitro $K_d$를 MM $K_m$과 동일시하면 FDA는 “왜 $K_m$이 $K_d$보다 수십-수백 배 큰지 mechanistic justification을 제시하라”는 Deficiency Letter를 보낼 수 있다. Phase D 구조적 설명 불가 시 임상약리 섹션 방어력이 급격히 약해진다.

---

## 혼동쌍 2: Phase B (표적 포화 선형) vs Phase D (TMDD 지배 말단 선형)

| 비교 차원           | **Phase B**                             | **Phase D**                            |
| --------------- | --------------------------------------- | -------------------------------------- |
| **지배 방정식**      | $-dC_L/dt \approx (CL_L/V_c) \cdot C_L$ | $-dC_L/dt \approx k_{e(RL)} \cdot C_L$ |
| **발생 농도**       | 고농도 ($C_L \gg R_0$)                     | 저농도 ($C_L \ll K_m$)                    |
| **기울기 의미**      | $CL_L/V_c$ (비특이적 청소율)                   | $k_{e(RL)}$ (복합체 내재화 속도)               |
| **⚡ 구조적 기억 고리** | B는 표적이 배부른 구간 — 약이 비특이적 배수구로만 빠진다.      | D는 표적이 다시 굶은 구간 — 배수구가 아니라 수용체가 지배한다.  |

> 💡 **짧은 암기:**
> B는 “target saturated”, D는 “target re-engaged”.

---

## 혼동쌍 3: SC 말단 t½ vs IV 소실 t½

| 비교 차원           | **SC 말단 t½**                                                                | **IV 소실 t½**               |
| --------------- | --------------------------------------------------------------------------- | -------------------------- |
| **지배 요인**       | 플립플롭 시 $\approx 0.693/k_a$                                                  | $0.693 \cdot V_{ss}/CL$    |
| **성립 조건**       | $k_{el} < k_a$                                                              | 항상 소실 지배                   |
| **Anakinra**    | CrCl 95→41에서 5.24→5.24 h (불변)                                               | 정상→혈액투석: 2.64→7.15 h       |
| **⚡ 구조적 기억 고리** | SC 말단 기울기는 배수구(소실)가 아니라 수도꼭지(흡수) 속도일 수 있다. 수도꼭지가 느리면 배수구를 막아도 수위는 거의 안 변한다. | IV는 수도꼭지가 없으므로 배수구 자체를 본다. |

---

## 혼동쌍 4: TMDD Phase D vs ADA(항약물항체) 매개 소실

| 비교 차원           | **TMDD Phase D**                | **ADA 매개 소실**                 |
| --------------- | ------------------------------- | ----------------------------- |
| **의존성 본질**      | **농도 의존적** ($C_L < K_m$)        | **시간 의존적** (~200h 이후)         |
| **정량적 시간 앵커**   | $K_m$ 값에 따라 결정                  | 검출 ~200h, peak ~400–500h      |
| **모델링 대응**      | TMDD 파라미터 추정                    | ADA titer 측정·시간-가변 CL 모델      |
| **⚡ 구조적 기억 고리** | Phase D는 표적이 굶어서 약을 잡아먹는 농도 사건. | ADA는 면역계가 깨어나서 약을 제거하는 시간 사건. |

> 💡 **실전 감별:**
> 특정 농도 아래로 내려갈 때마다 반복되는 패턴이면 Phase D를 의심한다. 특정 투여 후 시간이 충분히 지난 뒤부터 새로운 소실 증가가 나타나면 ADA를 의심한다.

---

# §7 — Self-Test: Active Recall Module

**Q1 ★★ [회상]** 수용체($R$)와 복합체($C_{RL}$)의 ODE를 모두 포함하여 작성하고, 정상상태에서 $R_0$를 $k_{in}$·$k_{out}$으로 표현하라. NONMEM $DES에서 이 초기조건을 어떻게 구현하는가?

<details><summary>정답 공개</summary>

$$
\frac{dR}{dt} =
k_{in}

* k_{out} \cdot R
* k_{on} \cdot C_L \cdot R

- k_{off} \cdot C_{RL}
  $$

$$
\frac{dC_{RL}}{dt} =
k_{on} \cdot C_L \cdot R

* k_{off} \cdot C_{RL}
* k_{e(RL)} \cdot C_{RL}
  $$

정상상태:

$$
R_0 = \frac{k_{in}}{k_{out}}
$$

NONMEM $PK 블록: `R0 = KLIN/KOUT`. $DES 블록 시작 전 $A_0(3)=R0$, $A_0(4)=0$으로 설정. 강성 ODE이므로 `$SUBROUTINES ADVAN13 TOL=6` 사용.

💡 **풀이 직관:** 투여 전 약물은 없어도 수용체는 이미 생체 항상성으로 존재한다. 그래서 ligand와 complex는 0, receptor는 $R_0$에서 시작한다.

**다음 깊이 질문:** $k_{on}$ 단위를 mg에서 nmol로 변환하면 $k_{on}$ 추정값은 어떻게 달라지는가?

</details>

---

**Q2 ★★ [회상]** $K_m$과 $K_d$의 수식, 크기 관계, PK27 교과서 기준 수치와 오차 배수를 서술하라.

<details><summary>정답 공개</summary>

$$
K_m = \frac{k_{off}+k_{e(RL)}}{k_{on}},
\quad
K_d = \frac{k_{off}}{k_{on}}
$$

항상 $K_m \geq K_d$.

PK27: $K_d$ ≈ 0.010, $K_m$(TMDD) ≈ 0.03, MM 피팅 3.7 → **123배 과대**. FIH MABEL에서 포화 농도를 수백 배 과장하는 방향으로 왜곡될 수 있다.

💡 **풀이 직관:** $K_d$는 결합 친화도, $K_m$은 결합 후 내부화 손실까지 포함한 PK적 포화 척도다.

**다음 깊이 질문:** $k_{e(RL)} \rightarrow 0$이 되는 생물학적 상황은? QE 근사가 정당해지는 이유는?

</details>

---

**Q3 ★★ [회상]** Table 2.13이 보여주는 CL 모델·Turnover 모델·Response 모델의 동형성을 서술하고, 알로메트릭 스케일 관계를 각 모델의 해당 파라미터로 표현하라.

<details><summary>정답 공개</summary>

세 모델의 ODE:

$$
V \cdot \frac{dC}{dt} = In - CL \cdot C
$$

$$
\frac{dA}{dt} = k_{in} - k_{out} \cdot A
$$

$$
\frac{dR}{dt} = k_{in} - k_{out} \cdot R
$$

구조는 모두 “입력 − 출력”이다.

알로메트릭:

$$
CL \propto BW^b
$$

$$
k_{out} \propto BW^{-0.25}
$$

$$
MRT = \bar{t} \propto BW^{0.25}
$$

TMDD 수용체 $k_{out}$도 동일 법칙으로 종간 스케일 가능하다.

💡 **풀이 직관:** 약물 clearance, 단백질 turnover, PD response는 이름이 다를 뿐 같은 동역학 문법을 공유한다.

**다음 깊이 질문:** TMDD $R_0$의 알로메트릭 스케일은 $k_{in}/k_{out}$에서 어떻게 결정되는가? $k_{in} \propto BW^b$, $k_{out} \propto BW^{-0.25}$이면 $R_0 \propto ?$

</details>

---

**Q4 ★★ [회상]** Anakinra SC 데이터에서 CrCl 95→41에도 SC t½이 거의 불변인 이유를 플립플롭 수식으로 설명하고, IV 데이터에서는 어떤 패턴이 나타나는지 서술하라.

<details><summary>정답 공개</summary>

IV t½=2.6h, SC t½=5.24h → $k_{el} > k_a$ → flip-flop. CrCl 감소 → $k_{el}$ 감소하지만 여전히 $k_{el} > k_a$ → 말단 기울기 = $k_a$ →

$$
t_{1/2,SC} \approx \frac{0.693}{k_a}
$$

따라서 SC t½은 거의 불변. 반면 AUC는 Dose·F/CL이므로 CL 감소로 증가한다.

ESRD: $k_{el} < k_a$ 역전 → flip-flop 해제 → SC t½=9.71h. IV: AUC 6.7배↑, t½ 2.64→7.15h.

💡 **풀이 직관:** SC 말단 t½은 때로 소실 속도가 아니라 흡수 속도를 본다.

**다음 깊이 질문:** 150 kDa mAb는 ESRD에서 AUC가 왜 거의 변하지 않는가? Table 21-9 수치로 설명하면?

</details>

---

**Q5 ★ [회상]** Figure 2.70이 보여주는 두 패널의 핵심 메시지를 서술하고, 류마티스 환자에서 $R_0$ 증가의 두 가능한 기전과 모델링 전략 차이를 설명하라.

<details><summary>정답 공개</summary>

$k_{in}$ 변화: 정상상태만 이동, $T_{ss}$ 불변.
$k_{out}$ 변화: 정상상태 + $T_{ss}$ 동시 이동.

류마티스 환자 $R_0$ 증가 경로:

1. $k_{in}$↑(생산 증가) → $k_{in}$을 염증 바이오마커 공변량으로 탐색, $k_{out}$ 고정
2. $k_{out}$↓(이화 감소) → $k_{out}$을 공변량으로, $k_{in}$ 고정

둘의 구분이 투여 용량 시뮬레이션 방향을 결정한다.

💡 **풀이 직관:** baseline만 보면 둘은 비슷하지만, 회복 속도와 washout은 다르다.

**다음 깊이 질문:** UK-279,276 임상 실패를 예방하려면 Phase 1 프로토콜에 어떤 biomarker 측정이 사전에 포함되어야 했는가?

</details>

---

**Q6 ★ [적용]** TMDD 4용량 semi-log 플롯에서 (a) 저용량이 고용량보다 가파른 초기 교차, (b) 4용량 평행, (c) 곡선 수렴+기울기 변화 패턴의 Phase명·지배방정식·임상 해석을 서술하라.

<details><summary>정답 공개</summary>

(a) Phase A:

$$
-dC_L/dt \approx k_{on} \cdot C_L \cdot R
$$

저용량 수용체 풍부 → 2차 반응 강함. 교차 = TMDD 시그니처.

(b) Phase B:

$$
-dC_L/dt \approx (CL_L/V_c) \cdot C_L
$$

표적 포화 → 비특이적 1차. 평행.

(c) Phase C→D:

$$
-dC_L/dt \approx k_{e(RL)} \cdot C_L
$$

기울기 ≠ Phase B 기울기.

💡 **풀이 직관:** 같은 직선이라도 Phase B는 non-specific clearance, Phase D는 complex internalization이다.

**다음 깊이 질문:** Phase B와 D의 기울기 차이가 없다면 무엇을 의미하는가? ($k_{e(RL)} \approx CL_L/V_c$ 케이스)

</details>

---

**Q7 ★ [적용]** ADA 매개 소실과 TMDD Phase D를 GOF 분석으로 감별하는 정량적 기준을 서술하라. R&T Figure 21-19의 수치를 근거로 활용하라.

<details><summary>정답 공개</summary>

**TMDD Phase D 진단:** 저용량 코호트 말단에서 CWRES < –2. 발생 시점이 $K_m$ 수준과 연동 — 농도 의존적.

**ADA 진단:** 반복 투여 시 trough가 사이클마다 지속 하락. Figure 21-19 기준: 시작 ~200h, peak ~400–500h — 시간 의존적. CL 증가가 시간 추이를 따른다.

혼재 시: L+ADA titer 동시 측정 후 시간-가변 CL 모델 적용. TMDD 파라미터는 고정 후 ADA 항만 시간 가변으로 추가.

💡 **풀이 직관:** Phase D는 “농도가 낮아지면 다시 나타나는 현상”, ADA는 “면역계가 반응할 시간이 지나야 나타나는 현상”이다.

**다음 깊이 질문:** 단일 코호트 단회 투여 데이터만 있을 때 Phase D와 ADA를 구별하는 것이 원칙적으로 가능한가?

</details>

---

## ⚡ Q8 [보스 딜레마] ★★ | TMDD 풀 모델 vs MM 근사 — Phase 2b 용량 결정 회의

**상황:** 항 IL-6R mAb Phase 2b 용량 결정 회의. Phase 2a 4코호트(1–10 mg/kg) 분석 완료.

**모델러 A (MM 근사):**
“4코호트 전체 CWRES ±2 이내, GOF 양호. 추정 $K_m=2.3$ µg/mL. Phase 2b 목표 농도(5–50 µg/mL) 커버 가능. 추가 assay 없이 MM으로 충분.”

**모델러 B (TMDD 풀 모델):**
“1 mg/kg 코호트 말단(t > 1000h)에서 CWRES < –2.5. Phase D 시그니처. 가용성 sIL-6R 데이터 이미 있음. MM $K_m=2.3$ µg/mL이 in vitro $K_d$(0.02 µg/mL)의 115배. 중증 환자에서 $R_0$ 3–5배 높아 용량 부족 위험.”

**당신은 어떤 모델을 선택하고, 규제 제출에서 어떻게 방어하는가?**

<details><summary>수석 모델러의 Trade-off 논리</summary>

**결정: TMDD 풀 모델 채택. MM 근사는 sensitivity analysis로 보조.**

**Trade-off 논리:**

MM의 GOF가 Phase 2a 농도 범위 내에서 좋아 보여도, 1 mg/kg 말단 CWRES < –2.5는 Phase D 구조적 실패를 직접 지시한다. Phase B 기울기($CL_L/V_c$)와 Phase D 기울기($k_{e(RL)}$)가 구조적으로 다르므로 MM은 이 둘을 동시에 재현하기 어렵다.

$K_m=2.3$ µg/mL ≫ $K_d=0.02$ µg/mL (115배): MM이 표적 포화 농도를 과대 추정 → Phase 2b 시뮬레이션에서 표적 점유율 체계적 과소 예측 → 실제로는 서브세라퓨틱 위험.

$R_0$ 3–5배 팽창: TMDD에서만 $R_0$를 질환 심각도 공변량으로 탐색 가능. MM으로는 이 변동성을 파라미터 구조 안에 수용하기 어렵다.

**FDA 규제 방어 언어:**

> “The proposed Phase 2b dose was selected using a TMDD mechanistic model with simultaneous regression of free ligand and soluble target concentration-time data from Phase 2a (n=4 dose cohorts). The MM approximation was found structurally inadequate in the terminal phase at 1 mg/kg (CWRES < –2.5 at t > 1000h), consistent with re-emergence of target-mediated clearance (Phase D, governed by $k_{e(RL)}$, not $CL_L/V_c$). The MM-estimated $K_m$ of 2.3 µg/mL exceeded the TMDD-estimated $K_d$ (0.02 µg/mL) by 115-fold, precluding its use as a surrogate for target occupancy prediction. TMDD simulation accounting for disease-associated $R_0$ elevation (3–5× in severe patients) projects target occupancy >80% throughout the dosing interval at the proposed dose.”

**MM sensitivity analysis의 전략적 가치:**
MM을 Phase 2a 농도 범위(5–50 µg/mL) 내에서 sensitivity analysis로 제시 → 두 모델의 일치 구간 명시 → mechanistic model의 superior fit 입증과 동시에 투명성 확보.

**방어 불가한 상황:**
“우리는 MM을 썼지만 $K_m$이 $K_d$보다 115배 크다는 것은 안다” → mechanistic justification 없이 제출하면 방어 취약.

💡 **보스 딜레마의 핵심:**
좋은 GOF와 좋은 모델은 다르다. 규제 제출에서 중요한 것은 “전체 평균적으로 잘 맞았다”가 아니라 “임상 의사결정을 좌우하는 구간에서 구조적으로 맞는가”다.

**다음 깊이 질문:** Phase 2b에서 sIL-6R assay를 제외했다면 $R_0$의 IIV를 어떻게 처리하고 규제 보고서에 어떻게 기술하는가?

</details>

---

# §8 — Meta-Frame & Big Picture

## A. Positioning

**선행:** I-01, I-04, I-07($V_{max}$·$K_m$ 기원), I-09(수용체-리간드 PD)

**직접 열어주는 것:** II-04($DES$ ODE·ADVAN13 강성 솔버·TOL 설정), II-08(공변량 — $R_0$·질환 중증도·ANC SCM 전략), II-11(NONMEM PK/PD 결합 모델)

**의존하는 고급 도메인:** Bispecific mAb PK, ADC payload 방출 TMDD, PBPK-TMDD 통합, 면역-종양학 tumor target burden covariate

> 💡 **이 세션의 위치:**
> 이 세션은 “항체 PK 이론”이 아니라, 이후 biologics PopPK 모델링에서 receptor, soluble target, ADA, disease severity를 어떻게 같은 구조 안에서 판단할지 결정하는 중심축이다.

---

## B. Dependencies

**실패 모드 1:** $K_m$·$K_d$ 혼동 → FIH MABEL 오결정. 2006년 TGN1412 사건은 작용제 mAb MABEL 오류의 임상적 결과를 보여주는 대표적 경고 사례다.

**실패 모드 2:** $DES$ 초기조건 미설정($R(0)=0$으로 오기) → 수용체 pool이 “0에서 시작”하는 비생리학적 모델 → 초기 Phase A 재현 불가, $k_{on}$ 추정 편향.

**실패 모드 3:** Stiff ODE를 부적절한 solver로 푸는 경우 → 수렴 불안정 또는 허위 수렴(local minimum). ADVAN13 미선택이 “데이터 불량”으로 오진되는 전형적 패턴.

> ⚠️ **실무적 더러운 진실:**
> TMDD 모델이 안 맞을 때 초보자는 자주 “데이터가 noisy하다”고 말한다. 그러나 실제로는 초기조건, 단위, solver, assay 설계 중 하나가 틀린 경우가 많다.

---

## C. Professional Moat — 구조적 필연성 수준의 해자

이 세션 고유의 세 가지 불가복제 역량:

**첫째, 곡선의 형태를 보는 순간 기전을 읽는 직관.**
다용량 semi-log 플롯에서 저용량 곡선이 고용량보다 가파르게 교차한다 — TMDD Phase A 시그니처를 즉시 인식하고 이것이 assay 설계 권고로 직결되는 것은 단순 알고리즘이 아니라 기전 직관의 영역이다.

**둘째, 임상 설계를 바꾸는 권한.**
PK27이 증명하듯 ligand-only에서 $k_{off}$·$k_{e(RL)}$ CV=27%이지만 L+R+RL에서 CV=2–3%. “Phase 1 프로토콜에 가용성 표적 assay를 추가해야 한다”는 결정은 데이터 생성 전에만 가능하다.

**셋째, 초기조건을 생리학에서 유도하는 능력.**
NONMEM $DES에서 $R(0) = k_{in}/k_{out}$이 아닌 임의 값으로 시작하면 모델은 수렴해도 파라미터는 틀린다. 이 한 줄의 초기조건은 카드 2의 Turnover ODE 기초 없이는 도출 불가하다 — 수식이 연결되어야 코드가 정확해진다.

> 💡 **전문가의 해자 한 문장:**
> AI가 control stream을 만들어도, “왜 $R(0)=0$이면 생리학적으로 틀렸는지”, “왜 MM $K_m$이 $K_d$보다 100배 큰 것이 GOF 문제가 아니라 구조 문제인지”를 판단하는 사람만이 모델의 주인이 된다.

---

✦ STEP 1 인지 컴파일 완료.

[로드맵 현황]
• §1 세션 헤더 & 로드맵
• §2 개념 해부 카드 (6개, ⚡ Apex Concept: TMDD 풀 모델)
• §5 혼동쌍 해부 (4개, 💥 Critical Blow: $K_m$ vs $K_d$)
• §7 자기주도 인출 테스트 (8문항, 보스 딜레마 장전)
• §8 메타프레임 & 전문가의 해자
• 문헌 감지: Vol I — R&T + Gabrielsson 혼합
• Data Anchoring: Gabrielsson PK27 Table 27.2·Figure 27.6·27.7; PK30 Figure 2.74; Table 2.11·2.13; Figure 2.70·2.84; R&T Tables 21-6·21-9·21-16·21-21; Figures 21-5·21-9·21-10·21-14·21-16·21-17·21-19·21-20

"계속"을 입력하시면 Step 2가 실행되어,
위 내용에 §3(동형성 지도), §4(인터랙티브 시뮬레이터), §6(실전 규제 시나리오)를 더해
브라우저용 '단일 완성형 Interactive HTML'로 컴파일합니다.

[1]: https://pubmed.ncbi.nlm.nih.gov/20012173/?utm_source=chatgpt.com "Selection between Michaelis-Menten and target-mediated drug disposition pharmacokinetic models - PubMed"
[2]: https://www.dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=d9d74915-6606-4570-9c52-c4001d3177de&type=display "These highlights do not include all the information needed to use KINERET safely and effectively. See full prescribing information for KINERET.
 
      
KINERET® (anakinra) injection, for subcutaneous use
 
Initial U.S. Approval: 2001
"

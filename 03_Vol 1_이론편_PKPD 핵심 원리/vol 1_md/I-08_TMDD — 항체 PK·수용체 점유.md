# §1 — 세션 헤더 & 로드맵

**소스 자동 추출 결과**

| 문헌 | 챕터/섹션 | 제목 | 페이지 범위 |
|---|---|---|---|
| Rowland & Tozer (R&T) 5e | Chapter 21 | Protein Drugs | pp. 687–730 (44p) |
| Gabrielsson & Weiner 5e | §2.6.1–2.6.7 | Turnover | pp. 94–111 (18p) |
| Gabrielsson & Weiner 5e | Case Study PK27 | Target Mediated Drug Disposition | pp. 602–610 (9p) |

**감지된 소스 유형:** Vol I 혼합 — R&T (임상 이론·생리학적 기전) + Gabrielsson (수식 도출·실험 데이터 앵커링)

---

### Big Idea (한 문장)

항체와 단백질 약물의 비선형 PK는 약물이 자신의 pharmacologic target(수용체)과 고친화도로 결합하여 청소율 경로 자체를 포화시키는 생물학적 필연이며, 이 TMDD 현상을 이해해야만 임상 용량 설계, Phase 1 FIH 예측, 그리고 규제 제출 시 비선형성 정당화 문서를 작성할 수 있다.

---

### 개념 항법도

1. **Turnover 삼각 관계** — $k_{in}$, $k_{out}$, $A_0 = k_{in}/k_{out}$의 정상상태 대수학
2. **단백질 약물 PK 특이성** — 흡수·분포·제거 메커니즘의 소분자와의 근본적 차이
3. **FcRn 매개 IgG 보존 메커니즘** — 왜 mAb 반감기가 21일인가
4. **[⚡ Apex] TMDD 풀 모델** — Levy(1994)/Mager & Jusko(2001) 프레임워크의 8파라미터 ODE 체계
5. **Michaelis-Menten 근사 vs 풀 TMDD** — PK27 데이터로 검증된 근사의 한계
6. **TMDD 4상 패턴 판독법** — Phase A~D와 농도-청소율 관계

---

### 지식 그래프 위치

**전제 선행 지식:** I-01 (CL·V 기초 기하학), I-04 (2구획 분포상 PK), I-05 (간·신장 추출비), I-07 (Michaelis-Menten 비선형 PK)

**열어주는 후속 세션:** II-04 (General ADVAN·$DES ODE 작성법), II-08 (공변량 분석 — 분자량·MW 공변량), II-11 (PK/PD NONMEM 구현)

**의존 고급 도메인:** QSP(Quantitative Systems Pharmacology), ADC(Antibody-Drug Conjugate) PK, 면역종양학 PopPK 모델링, Bayesian TDM in biologic therapeutics

---

# §2 — 개념 해부 카드

---

## 카드 1: Turnover — $k_{in}$·$k_{out}$·$A_0$의 삼각 관계

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가:** 항체(mAb) 투여 후 혈장 내 receptor 농도가 감소하고 다시 회복하는 현상을 설명하지 못하면, TMDD 모델에서 $k_{in}$/$k_{out}$ 파라미터를 올바르게 추정할 수 없고, 그 결과 표적 점유율(target occupancy)과 용량-반응 관계가 왜곡된다.

**체화해야 할 단 하나의 직관:** Turnover는 "항상 흐르고 있는 물"이다 — $k_{in}$은 수도꼭지의 유량, $k_{out}$은 배수구의 비율, $A_0$는 균형점의 수위. 약물은 이 수위를 올리거나 내리는 외력이지, 수조 자체를 변경하는 것이 아니다.

**이 직관을 머릿속에 박고 아래를 읽어라:** $k_{in}$과 $k_{out}$이 동일하게 변하면 $A_0$는 바뀌지 않지만, $t_{1/2}$는 변한다 — 이것이 TMDD에서 $k_{out}$ 추정이 왜 receptor 데이터 없이는 불가능한지의 핵심 이유다.

---

**A. 정의**

Turnover란 내인성 화합물(호르몬, 효소, 단백질, 수용체)이 합성(분비)과 분해(이화) 사이의 동적 평형 상태에서 존재하는 현상이다. 한 개체의 화합물 농도는 합성 속도 차이 또는 분해 속도 차이 또는 둘 다에 의해 결정되며, 단순히 정적 풀(pool)이 아니다.

---

**B. Derivation — 수식 도출**

기본 turnover ODE (Gabrielsson Eq. 2:237):

$$\frac{dA}{dt} = k_{in} - k_{out} \cdot A$$

정상상태(baseline)에서 $dA/dt = 0$이므로 (Gabrielsson Eq. 2:238):

$$k_{in} = k_{out} \cdot A_0 \quad \Rightarrow \quad A_0 = \frac{k_{in}}{k_{out}}$$

`[출처: Gabrielsson 5e, §2.6.1, p.95]`

Turnover time $t_t$ — 현재 steady-state 양만큼을 합성하는 데 걸리는 시간 (Gabrielsson Eq. 2:242):

$$t_t = \bar{t} = \frac{A_0}{k_{in}} = \frac{1}{k_{out}}$$

Turnover time과 MRT의 관계 (Gabrielsson Eq. 2:243):

$$t_t = \frac{A_0}{k_{in}} = \frac{C_0 \cdot V_{ss}}{C_0 \cdot Cl} = \frac{V_{ss}}{Cl} = MRT$$

`[출처: Gabrielsson 5e, §2.6.1, p.96]`

반감기와 turnover time의 관계 (Gabrielsson Eq. 2:244):

$$t_{1/2} = \frac{\ln 2}{k_{out}} = \ln(2) \cdot t_t$$

**Gabrielsson PK30 데이터 앵커링 — IgX (growth hormone immunoglobulin) in healthy human volunteer:**
- 투여: sc, 40 µg/kg
- 측정된 기저 농도: 32 µg/L (pre-dose)
- 추정 파라미터:
  - $Cl/F = 0.03$ L/h/kg, $V/F = 0.10$ L/kg
  - Turnover rate ($k_{in}$) = **0.78 µg/h/kg**
  - Turnover time: **2.7 h**
  - Terminal $t_{1/2}$ = **2.5 h**
  - Fractional turnover rate = **0.27 h⁻¹** (= 27% of body load eliminated per hour)
  - Pool size at steady state: **2.3 µg/kg**
- ODE (Gabrielsson Eq. 2:245):
$$V \cdot \frac{dIgX}{dt} = k_{in} + In_{sc} - Cl \cdot C_{IgX}$$
- 피하 흡수 함수 (Gabrielsson Eq. 2:246):
$$In_{sc} = K_a \cdot F \cdot D_{sc} \cdot e^{-K_a \cdot t}$$

`[출처: Gabrielsson 5e, §2.6.3, p.101, Case Study PK30]`

**Turnover 조작 방향성 — 핵심 임상 결과 (Figure 2.70 기반):**
- $k_{in}$ 변화(≈ 주입속도 변화): steady-state 수준만 변하고 $t_{ss}$는 불변 (선형 kinetics 가정)
- $k_{out}$ 변화(≈ CL 변화): steady-state 수준과 $t_{ss}$ 모두 변함

**Clearance/Turnover/Response 모델 삼각 대응표 (Gabrielsson Table 2.13):**

| 항목 | Clearance model | Turnover model | Response model |
|---|---|---|---|
| 1차 변수 | $C$ | $A$ | $R$ |
| 파라미터 | $V$, $Cl$ | $k_{in}$, $k_{out}$ | $k_{in}$, $k_{out}$ |
| ODE | $V\frac{dC}{dt} = In - Cl\cdot C$ | $\frac{dA}{dt}=k_{in}-k_{out}\cdot A$ | $\frac{dR}{dt}=k_{in}-k_{out}\cdot R$ |
| Steady-state | $C_{ss}=In/Cl$ | $A_{ss}=k_{in}/k_{out}$ | $R_{ss}=k_{in}/k_{out}$ |
| Half-life | $t_{1/2}=\ln2\cdot V_{ss}/Cl$ | $t_{1/2}=\ln2/k_{out}$ | $t_{1/2}=\ln2/k_{out}$ |
| Scale factor | $Cl \propto BW^b$ | $k_{in} \propto BW^b$ | $k_{in} \propto BW^b$ |

---

**C. Structural Necessity**

$k_{in}$이 zero-order이고 $k_{out}$이 first-order인 이유: 생체 내 대부분의 합성 과정은 기질 농도에 독립적(효소 기질 농도가 항상 충분)이므로 zero-order이고, 분해는 해당 화합물의 농도에 비례하므로 first-order다. 이 비대칭성이 바로 정상상태($A_0$)를 수학적으로 안정적으로 만드는 필연적 구조다.

---

**D. 가정 & 경계 조건**

단순 turnover 모델은 다음을 가정한다: (1) 선형 kinetics, (2) $k_{out}$이 농도 독립적, (3) 피드백 조절 없음, (4) 단일 구획, (5) 기저값($A_0$)이 시간에 따라 일정. 이 가정들이 위반될 때: 비선형 turnover(hyaluronan — saturable), 피드백 조절(estradiol — 시상하부-뇌하수체 축), 일주 리듬(체온 — Zeitgeber 모델로 확장 필요).

---

**E. 한계**

포화 가능한 대사 과정(예: hyaluronan turnover, PK32)은 Michaelis-Menten 형태의 $k_{out}$이 필요하다. 피드백이 있는 시스템(에스트라디올, IgG)은 $k_{in}$ 또는 $k_{out}$이 반응의 함수가 되어 고차 ODE 체계가 요구된다.

---

**F. Five Cognitive Layers**

| 레이어 | 내용 |
|---|---|
| **L1 형식적 수학** | $dA/dt = k_{in} - k_{out}\cdot A$, 해: $A(t) = A_0 + (A_{init}-A_0)e^{-k_{out}t}$, 단위: $k_{in}$ [amount/time], $k_{out}$ [time⁻¹] |
| **L2 기하학적 직관** | 곡선의 점근선 = $A_0 = k_{in}/k_{out}$; 접근 속도는 오직 $k_{out}$에 의해 결정 |
| **L3 구조적 동일성** | RC 회로(충전/방전), 인구 동역학(출생/사망), 약물 정주 주입-청소율 평형과 완전히 동형 |
| **L4 생리학적 의미** | $k_{in}$ ↓ → 폐경 후 에스트라디올 저하(CL은 유지된 채 합성만 감소); TMDD에서 수용체($R$)의 $k_{out}$ = 수용체 내재화 속도 |
| **L5 실무 투영** | NONMEM: `$PRED` 또는 `ADVAN13`에서 `DADT(R) = KIN - KOUT*R - KON*C*R + KOFF*RL` 로 구현 |

---

**G. Zettelkasten Atom**

```yaml
---
aliases: [Turnover model, kin kout model, 내인성 turnover]
tags: [pharmacometrics/pk, endogenous/compound, tmdd/prerequisite]
up: "[[PK·PD 개요 MOC]]"
related: ["[[TMDD 풀 모델]]", "[[Indirect Response Model]]", "[[FcRn 메커니즘]]"]
source: "Gabrielsson 5e, §2.6.1, pp.94–96; Case Study PK30, pp.100–101"
---
```

Turnover 모델의 핵심은 내인성 화합물의 정상상태 농도($A_0 = k_{in}/k_{out}$)가 합성과 분해의 비율로 결정된다는 것이다. 약물은 이 두 파라미터 중 하나 또는 둘 모두를 조작함으로써 효과를 발휘한다. Turnover time은 $1/k_{out}$ = MRT이며, 새로운 정상상태 도달 시간($T_{ss}$)은 오직 $k_{out}$(즉, $t_{1/2}$)에 의해 결정된다. 이 구조는 Clearance/Turnover/Indirect Response 모델에 공통으로 적용된다.

---

## 카드 2: 단백질 약물 PK의 특이성 — 소분자와의 근본적 차이

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가:** biologic 약물의 PK는 소분자 약물의 ADME 프레임워크를 그대로 적용하면 체계적으로 틀린 예측이 나온다 — SC 투여 후 $F$를 100%로 가정하거나, 신기능 저하가 mAb CL에 영향 없다고 단정하거나, 단순 CYP 대사로 drug interaction을 예측하는 오류가 실제 IND/NDA 제출에서 빈번히 발생한다.

**체화해야 할 단 하나의 직관:** 단백질 약물은 "크기와 전하가 운명을 결정하는" 세계에서 산다 — 분자량이 5 kDa 미만이면 신사구체 여과가 주 경로, 20 kDa 이상이면 림프계가 주 흡수 경로, 60 kDa 이상이면 사구체 여과가 차단되고 수용체 매개 내재화가 제거를 지배한다.

**이 직관을 머릿속에 박고 아래를 읽어라:** 분자량 하나가 흡수·분포·제거 세 프로세스의 주도적 메커니즘을 모두 결정한다.

---

**A. 정의**

단백질 약물(protein drugs)은 2개 이상의 아미노산이 펩타이드 결합으로 연결된 모든 치료용 물질을 포괄하며, 분자량 범위는 수백 Da(소형 펩타이드)부터 >150,000 Da(IgG mAb)까지 방대하다. 2011–2016년 FDA 승인 치료용 단백질의 약 50%가 monoclonal antibody(mAb)였다.

---

**B. 흡수·분포·제거 비교 — R&T 실제 데이터 앵커링**

**흡수 (SC/IM 경로):**

분자량이 흡수 경로를 결정한다 (R&T Figure 21-16, sheep 모델):
- FUdR (246 g/mol): 림프 회수율 ~1%
- Inulin (5,200 g/mol): ~20%
- Cytochrome C (12,300 g/mol): ~40%
- Interferon-α-2a (19,000 g/mol): ~60%

→ **분자량 >16,000 g/mol에서 주사 용량의 50% 이상이 림프계를 통해 흡수**

림프 유속은 심박출량(5 L/min)의 1/5000 수준으로 매우 느리다. R&T Figure 21-17에서 somatropin (rh-GH, MW = 22,125 g/mol)의 경우:
- IV 투여 시: $t_{1/2}$ = 2.1 hr
- SC 투여 시: 24시간 후에도 지속적 흡수가 관찰됨 — 흡수 속도 제한(absorption rate-limited) elimination

**SC 투여 후 생체이용률 (R&T Table 21-14, 선택):**

| 단백질 | MW (kDa) | $F$ | $T_{max}$ (hr) |
|---|---|---|---|
| Insulin | 5.6 | 0.84 | 1–2 |
| Interleukin-2 | 15.5 | 0.3–0.8 | 2–4 |
| Human growth hormone | 22 | 0.5–0.8 | 5–8 |
| Interferon-α | 19.5 | >0.8 | 6–8 |
| Erythropoietin | 34–39 | 0.2–0.36 | 13–18 |

**mAb SC 생체이용률 (R&T Table 21-15):**

| 항체 | MW (kDa) | $F$ | $T_{peak}$ (days) | $t_{1/2}$ (days) |
|---|---|---|---|---|
| Adalimumab | 148 | 0.64 | 5.5 | 30 |
| Omalizumab | 149 | 0.62 | 7.5 | 26 |
| Efalizumab | 150 | 0.50 | — | 17 |

**분포:**

단백질 약물은 친수성으로 세포막을 통과하기 어렵다. 분포 용적은 혈장(0.04 L/kg)과 세포외액(0.23 L/kg) 사이에 분포한다.

mAb $V_{ss}$ 범위 (R&T Table 21-6, 선택):
- Adalimumab: 0.067–0.086 L/kg
- Bevacizumab: 0.043 L/kg
- Rituximab: 0.137 L/kg

**신장 제거:**

사구체 여과 차단 기준 ≈ 60,000 g/mol. 분자량 및 전하가 여과를 결정 (R&T Table 21-9 — glomerular sieving coefficient):

| 단백질 | 크기 (g/mol) | Sieving 계수 |
|---|---|---|
| Insulin | 6,000 | 0.89 |
| Growth hormone | 22,000 | 0.65 |
| Horseradish peroxidase (anionic) | 40,000 | 0.007 |
| Albumin | 69,000 | 0.001 |

분자량 <5 kDa: 사구체 여과율(GFR) 수준의 신장 청소율. 분자량 >30 kDa: 신장 여과 급감 → 신기능 저하가 이 약물들의 PK에 미치는 영향은 제한적.

**증거 사례 — anakinra (IL-1 수용체 길항제, 17,258 g/mol) (R&T Table 21-16):**
- 정상 신기능: CL ≈ 1640 mL/min 수준, $t_{1/2}$ = 5.24 hr
- 말기 신부전(ESRD): $t_{1/2}$ = 9.71 hr, AUC 3.8배 증가
- → 신기능 저하가 소분자 단백질에는 임상적으로 유의한 영향을 미침

**대사:**

거의 모든 단백질 약물은 단백분해효소(proteolytic enzymes)에 의해 구성 아미노산까지 분해된다. 주요 부위: 내피세포(표면적 >1,000 m², 성인), 간, 세망내피계(RES). 분자 크기에 따른 신장 대사 메커니즘:
- MW < 5 kDa: 사구체 여과 후 관상 내강의 brush border 효소로 가수분해
- MW 5–60 kDa: 사구체 여과 후 근위세뇨관 세포 내 endocytosis → 리소좀 분해

---

**C. Structural Necessity**

소분자가 CYP 효소에 의한 간대사와 신장 소변 배설로 제거되는 이유는 친지질성과 소형 크기 때문이다. 단백질은 반대로 친수성과 대형 분자 때문에 이 경로를 사용할 수 없으므로, 수용체 매개 내재화와 단백분해 효소 경로만이 물리적으로 가능한 제거 메커니즘이 된다.

---

**D. 가정 & 경계 조건**

R&T의 단백질 PK 프레임은 다음을 가정한다: (1) 불순물(heterogeneity)을 평균 MW로 대표, (2) 면역원성이 PK를 교란하지 않는 단기 관측 기간, (3) 종양 microenvironment의 모세혈관 투과성 변화 무시. 이 가정들이 위반되면: 항약물 항체(ADA) 형성으로 CL 변화, 염증 시 모세혈관 투과성 급증으로 조직 분포 확대.

---

**E. 한계**

단백질 약물의 PK를 혈장 데이터만으로 $V_{ss}$와 CL을 추정할 때, 중심 구획 외 조직에서의 제거(예: antibody catabolism in peripheral tissues)를 무시하면 $V_{ss}$가 과소 추정된다 — R&T는 이를 명시적으로 경고한다.

---

**G. Zettelkasten Atom**

```yaml
---
aliases: [protein drug PK, biologic ADME, mAb pharmacokinetics]
tags: [pharmacometrics/biologic, absorption/lymphatic, elimination/renal]
up: "[[TMDD 세션 MOC]]"
related: ["[[FcRn 메커니즘]]", "[[TMDD 풀 모델]]", "[[글로메룰러 여과]]"]
source: "R&T 5e, Ch.21, pp.700–725"
---
```

단백질 약물의 ADME는 분자량과 전하가 지배한다. SC 투여 후 MW >16 kDa에서는 림프계가 주 흡수 경로이고, MW >30 kDa에서는 신사구체 여과가 차단되어 대사(단백분해)가 주 제거 경로가 된다. mAb는 FcRn 보존 메커니즘으로 21일의 긴 반감기를 가진다.

---

## 카드 3: FcRn 매개 IgG 보존 메커니즘

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가:** mAb의 반감기가 왜 ~21일인지 이해하지 못하면, FcRn 포화에 의한 dose-dependent PK 변화나 FcRn 경쟁 drug interaction을 예측할 수 없고, IVIVC 실패와 임상 용량 선택 오류로 이어진다.

**체화해야 할 단 하나의 직관:** FcRn은 IgG의 "구조 대원"이다 — 세포 내 산성 엔도좀에서 IgG를 낚아채어 리소좀 분해로부터 구출하고 다시 혈액으로 내보낸다. FcRn이 없으면 IgG의 반감기는 며칠에 불과하다.

**이 직관을 머릿속에 박고 아래를 읽어라:** FcRn은 내피세포와 단핵구에 발현하며, 산성 엔도좀(pH↓)에서 IgG와 결합하고 생리적 pH에서 해리하는 pH 의존적 메커니즘으로 작동한다.

---

**A. 정의**

Neonatal Fc receptor(FcRn), 또는 Brambell receptor는 IgG의 Fc 영역에 결합하여 IgG를 리소좀 분해로부터 보호하고 순환계로 재활용(recycling)하는 수용체다. 이로 인해 mAb의 반감기가 내인성 IgG의 반감기 ~21일에 근접하게 된다.

---

**B. 메커니즘 도출**

FcRn 작동 사이클 (R&T Figure 21-5):

1. 혈액(생리적 pH 7.4): 내피세포가 IgG를 포함한 혈청 단백질을 비특이적 endocytosis
2. 산성 엔도좀(pH ~5.5~6.0): FcRn이 IgG-Fc에 **높은 친화도로 결합** (pH↓ → 친화도↑)
3. Recycling endosome: FcRn-IgG 복합체가 세포 표면으로 이동
4. 세포 표면(생리적 pH 7.4): IgG가 FcRn에서 **해리**하여 순환계로 방출
5. FcRn에 결합하지 못한 기타 단백질: 리소좀으로 이동 → 분해

핵심 관계:
$$t_{1/2,IgG} \approx 21 \text{ days} \Leftarrow \text{FcRn recycling이 proteolytic degradation을 차단}$$

FcRn 결합은 치료 농도에서 일반적으로 비포화(nonsaturable)이다. 그러나 **매우 고용량 IgG 투여 시** FcRn이 포화되어 미결합 IgG가 리소좀 경로로 유입되고 CL이 증가한다 → dose-dependent 비선형 PK의 원인이 될 수 있다.

**IgG 클래스별 Turnover 실제 데이터 (Gabrielsson Table 2.11):**

| 특성 | IgA | IgG | IgM |
|---|---|---|---|
| $t_{1/2}$ (days) | 5.8 | **23** | 5.1 |
| Fractional catabolic rate (%/day) | 25 | **6.7** | 18 |
| Turnover rate (mg/kg/day) | 24 | **33** | 6.7 |

IgG의 $t_{1/2}$ = 23일, fractional catabolic rate = 6.7%/day — FcRn의 강력한 보존 효과를 직접 보여준다.

**IgG의 농도 의존적 $t_{1/2}$ 단축 (Gabrielsson §2.6.7, Figure 2.84 기반):**

Moderator $M$에 의해 $R$의 소실이 증가하는 negative feedback 시스템에서 slope는:
$$slope_{A,B,C} = k_{out} \cdot \left(1 + \frac{R_{A,B,C}}{M_{50}}\right)$$

IgG는 혈청 농도 30 mg/mL에서 $t_{1/2}$가 최소값 ~11일로 수렴한다 — 더 이상 단축되지 않는 포화된 보호 시스템.

`[출처: Gabrielsson 5e, §2.6.7, pp.110–111]`

---

**C. Structural Necessity**

FcRn 메커니즘이 필요한 이유: IgG는 면역 기억의 장기 매개체이므로, 진화적으로 긴 혈중 반감기를 유지하는 능동적 보존 기전이 발달했다. FcRn 없이는 IgG가 non-specific endocytosis 후 리소좀 분해되어 수일 내 소실된다.

---

**D. 가정 & 경계 조건**

FcRn 결합은 치료 농도에서 비포화라고 가정한다. 이 가정이 위반되면(초고용량 IgG 과부하): IVIG 고용량 투여 시 내인성 IgG의 FcRn 경쟁에 의해 mAb CL이 증가하는 drug interaction이 발생할 수 있다.

---

**G. Zettelkasten Atom**

```yaml
---
aliases: [FcRn, neonatal Fc receptor, Brambell receptor, IgG recycling]
tags: [pharmacometrics/biologic, elimination/mechanism, mAb/half-life]
up: "[[TMDD 세션 MOC]]"
related: ["[[TMDD 풀 모델]]", "[[단백질 약물 PK]]", "[[Turnover 삼각 관계]]"]
source: "R&T 5e, Ch.21, pp.707–708; Gabrielsson 5e, Table 2.11, pp.102"
---
```

FcRn은 pH 의존적으로 내피세포 내 산성 엔도좀에서 IgG를 포착하고 생리적 pH에서 다시 방출하여 리소좀 분해를 방지한다. 이 메커니즘이 IgG(및 mAb)의 반감기 ~21일을 만들며, 치료 농도에서 비포화이지만 초고용량에서는 dose-dependent CL 증가를 일으킬 수 있다.

---

## [⚡ Apex Concept] 카드 4: TMDD 풀 모델 — Mager & Jusko(2001) 프레임워크

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가:** mAb가 표적(수용체)에 고친화도로 결합하면 수용체 경로를 통한 청소율이 비선형이 되고, 이를 단순 MM 근사로 처리하면 저용량 농도-시간 곡선이 완전히 틀리게 예측되어 FIH 시험에서 용량 선택 오류와 효력 기준 실패로 이어진다.

**체화해야 할 단 하나의 직관:** TMDD는 약물 자체가 자신의 청소율 경로를 "예약"한다 — 표적이 비어 있을 때는 빠르게 제거되고, 표적이 가득 찼을 때는 선형 PK처럼 느리게 제거된다. 이 농도 의존적 청소율이 4상 곡선의 핵심 원리다.

**이 직관을 머릿속에 박고 아래를 읽어라:** $K_m$과 $K_d$는 다른 개념이며, TMDD에서 $K_m = (k_{off} + k_{e(RL)})/k_{on}$은 준정상상태 근사이고, $K_d = k_{off}/k_{on}$은 평형 해리상수다.

---

**A. 정의**

Target-Mediated Drug Disposition(TMDD)은 약물이 높은 친화도로 pharmacologic target(수용체, 항원)에 결합하여 그 결합이 약물의 PK에 유의미하게 영향을 미치는 현상이다 (Levy, 1994). 약물-수용체 복합체(RL)의 형성·분해·내재화가 비선형 청소율 경로를 구성한다.

---

**B. 풀 TMDD 모델 수식 도출**

Mager & Jusko(2001) 프레임워크 — 8파라미터 2구획 TMDD 모델 (R&T Equations 21-1~21-6, Gabrielsson Equations 27:1~27:3):

**리간드 (mAb, L) ODE:**
$$\frac{dC_L}{dt} = \left[Input_L - Cl_L \cdot C_L - Cl_d\cdot(C_L - C_t) - k_{on}\cdot C_L\cdot R + k_{off}\cdot C_{RL}\right]\cdot\frac{1}{V_c}$$

**조직 구획 리간드:**
$$\frac{dC_t}{dt} = \left[Cl_d\cdot C_L - Cl_d\cdot C_t\right]\cdot\frac{1}{V_t}$$

**수용체 (R) ODE — Turnover 구조:**
$$\frac{dR}{dt} = k_{in} - k_{out}\cdot R - k_{on}\cdot C_L\cdot R + k_{off}\cdot C_{RL}$$

`[출처: Gabrielsson 5e, Case Study PK27, Eq. 27:2, p.607]`

**리간드-수용체 복합체 (RL) ODE:**
$$\frac{dC_{RL}}{dt} = k_{on}\cdot C_L\cdot R - k_{off}\cdot C_{RL} - k_{e(RL)}\cdot C_{RL}$$

`[출처: Gabrielsson 5e, Case Study PK27, Eq. 27:3, p.607]`

**핵심 파라미터 관계:**

$$K_m = \frac{k_{off} + k_{e(RL)}}{k_{on}}, \quad K_d = \frac{k_{off}}{k_{on}}, \quad R_0 = \frac{k_{in}}{k_{out}}$$

`[출처: R&T 5e, Ch.21, Eqs. 21-5~21-6, p.711]`

**Gabrielsson PK27 — cynomolgus monkey mAb 데이터 (실제 파라미터, Table 27.2):**

4가지 용량 IV 주사 (1.5, 5, 15, 45 mg/kg):
- $V_c$ = 0.05 L/kg (고정)
- $Cl_L$ = 0.001 L/h/kg (AUC 최고용량 기반: $45/41820 = 0.001$)
- $k_{on}$ = 0.096 L/h/mg (all 3 datasets)
- $k_{off}$ = 0.001 h⁻¹
- $V_t$ = 0.100 L/kg
- $k_{out}$ = 0.009 h⁻¹
- $R_0$ = 12 mg/L
- $k_{e(RL)}$ = 0.003 h⁻¹

`[출처: Gabrielsson 5e, PK27, Table 27.2, p.609]`

**데이터 풍부도에 따른 정밀도 변화 (PK27 핵심 교훈):**

| 파라미터 | 리간드만(CV%) | 리간드+표적(CV%) | 리간드+표적+복합체(CV%) |
|---|---|---|---|
| $k_{on}$ | 17 | 2 | **1** |
| $k_{off}$ | 27 | 13 | **3** |
| $k_{e(RL)}$ | 27 | 23 | **2** |

→ **복합체(RL) 농도-시간 데이터 추가가 $k_{e(RL)}$ 정밀도를 27→2%로 극적 개선**

---

**C. Structural Necessity**

왜 이 형태의 ODE가 불가피한가: $k_{on}$이 2차 반응(second-order, $C_L \times R$)인 이유는 충돌 이론(collision theory)에서 반응 속도는 두 반응물 농도의 곱에 비례하기 때문이다. $k_{off}$가 1차(first-order, $C_{RL}$)인 이유는 복합체 해리가 단분자 과정이기 때문이다.

**C-2. Plausible Fallacy — [⚡ Apex Concept에만 적용]**

**그럴싸한 오류:** "PK27 가장 높은 용량(45 mg/kg)에서 리간드-시간 곡선이 선형처럼 보이므로 전체 농도 범위를 단순 2구획 선형 모델로 피팅해도 된다."

**실제 결과:** 45 mg/kg에서는 표적이 완전 포화되어 선형처럼 보이지만, 1.5 mg/kg 저용량에서는 표적 매개 제거가 지배적이다. 이 오류로 Michaelis-Menten 근사 시 $K_m$ = 3.7 mg/L로 추정되었으나, 실제 풀 TMDD 모델의 $K_m$ = 0.03 mg/L로 **100배 이상 과대 추정**된다.

**NONMEM 피팅에서의 나비효과:** $K_m$ 과대 추정 → Phase C(비선형 전환 구간)에서 체계적 잔차 패턴 → CWRES가 저농도 구간에서 양성 편향 → 저용량 임상 효력 및 PD 관계 예측 실패.

**GOF 시그니처 — "Low-Dose Cliff Sign":**
- 최저 용량 군의 농도-시간 곡선에서 예측값이 관측값보다 지속적으로 높게 나타남
- CWRES vs. TIME: 저용량 군에서 체계적 양성 편향
- 원인: 저농도에서 $K_m$이 실제 농도보다 훨씬 커서 이차 포화 효과를 무시하는 편향

---

**D. 가정 & 경계 조건**

풀 TMDD 모델의 가정:
1. Soluble target (가용성 수용체) — membrane-bound target는 모델 구조가 다름
2. 단일 표적 풀 (compartment)
3. 복합체 RL의 비특이적 분포 없음
4. 단위: mg와 molar 단위는 $k_{on}$ 추정에 영향 — PK27에서는 합성 데이터이므로 mg 단위 사용 가능

---

**E. 한계**

막결합 수용체(membrane-bound target)는 표적이 중심 구획의 세포 표면에 존재하므로 $V_c$ 정의가 달라진다. $k_{off} \ll k_{e(RL)}$이면 준평형 근사(quasi-equilibrium)가 부적절하고 준정상상태(quasi-steady-state, QSS) 근사가 필요하다.

---

**G. Zettelkasten Atom**

```yaml
---
aliases: [TMDD, Target Mediated Drug Disposition, Mager Jusko model, Levy 1994]
tags: [pharmacometrics/pk, biologic/nonlinear, mAb/receptor]
up: "[[TMDD 세션 MOC]]"
related: ["[[Michaelis-Menten 근사 vs TMDD]]", "[[4상 패턴]]", "[[FcRn 메커니즘]]"]
source: "Gabrielsson 5e, PK27, pp.602–610; R&T 5e, Ch.21, pp.709–712"
---
```

TMDD는 mAb가 고친화도 수용체와 결합하여 receptor-mediated endocytosis로 제거되는 비선형 PK 현상이다. Mager & Jusko(2001)의 8파라미터 풀 모델($k_{on}$, $k_{off}$, $k_{e(RL)}$, $R_0$, $k_{out}$, $Cl_L$, $Cl_d$, $V_c$)이 이를 완전히 기술하며, $K_m = (k_{off}+k_{e(RL)})/k_{on}$과 $K_d = k_{off}/k_{on}$의 차이를 이해하는 것이 핵심이다.

---

## 카드 5: Michaelis-Menten 근사 vs 풀 TMDD 모델

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가:** MM 근사는 TMDD 모델의 5파라미터를 2파라미터로 줄이는 것처럼 보여 편리하지만, 이 근사가 타당한 농도 범위를 벗어나면 예측이 완전히 붕괴한다 — 특히 Phase 1 저용량 코호트에서.

**체화해야 할 단 하나의 직관:** MM 근사는 "표적 농도가 리간드 농도보다 훨씬 낮거나($C_L \gg R_0$), 표적 점유율이 거의 100%에 근접할 때"만 유효하다. 그 범위를 벗어나면 사용하지 말아야 한다.

---

**B. 수식 비교**

**풀 TMDD 모델 (5파라미터 수용체 부분):**

$$\frac{dR}{dt} = k_{in} - k_{out}\cdot R - k_{on}\cdot C_L\cdot R + k_{off}\cdot C_{RL}$$

$$\frac{dC_{RL}}{dt} = k_{on}\cdot C_L\cdot R - k_{off}\cdot C_{RL} - k_{e(RL)}\cdot C_{RL}$$

**MM 근사 (Gabrielsson Eq. 27:5, R&T 21-4):**

$$Cl_{MM} = \frac{V_{max}}{K_m + C_L}$$

2구획 + MM 병렬 선형 제거 ODE (Gabrielsson Eq. 27:4):

$$\frac{dC_L}{dt} = \left[Input_L - Cl_L\cdot C_L - Cl_d\cdot(C_L - C_t) - Cl_{MM}\cdot C_L\right]\cdot\frac{1}{V_c}$$

`[출처: Gabrielsson 5e, PK27, Eq. 27:4~27:5, p.607]`

**PK27 MM 근사 실패 사례:**
- 3개 고용량(5, 15, 45 mg/kg): 상대적으로 양호한 피팅
- 최저 용량(1.5 mg/kg): **심각한 체계적 편차** — 초기 Phase A(2차 반응 지배 구간)를 MM 모델이 포착하지 못함
- MM 추정 $K_m$ = **3.7 mg/L** vs. 풀 TMDD 모델 $K_m$ = **0.03 mg/L** → 123배 과대 추정

`[출처: Gabrielsson 5e, PK27, p.609; Figure 27.6]`

---

**D. MM 근사가 타당한 조건:**

1. 표적 점유율 >90–95%: 사실상 선형 1차 제거 모델로 단순화 가능
2. $C_L \gg K_d = k_{off}/k_{on}$: 약물 농도가 해리 상수보다 훨씬 높을 때
3. **주의:** membrane-bound target의 경우 MM이 일부 용량 범위에서 합리적이지만, soluble target의 저농도에서는 부적절

---

## 카드 6: TMDD 4상 패턴 판독법

### ━━ [개념 Big Idea: 거장의 시각] ━━

**왜 치명적으로 중요한가:** TMDD 4상 패턴을 반로그 스케일 농도-시간 곡선에서 즉각 인식하지 못하면 일반 비선형 PK로 오진하여 모델 선택 오류를 범하게 되며, 이는 Phase 2 용량 탐색 설계 실패로 이어진다.

---

**B. 4상 패턴 — Gabrielsson Figure 27.7 + R&T Figure 21-9 통합**

$$
\text{Phase A} \xrightarrow{\text{표적 포화}} \text{Phase B} \xrightarrow{\text{표적 재출현}} \text{Phase C} \xrightarrow{k_{off}, k_{e(RL)} \text{ 지배}} \text{Phase D}
$$

| Phase | 지배 과정 | 농도 범위 | ODE 근사 | 임상 의미 |
|---|---|---|---|---|
| **A** | $k_{on}$·리간드·수용체 (2차 반응) | $C_L \gg R_0$ 초기 | $dL/dt \approx -k_{on}\cdot L\cdot R$ | 빠른 초기 하강; 저용량일수록 **더 가파름** (역설!) |
| **B** | 비특이적 선형 CL 지배 | 표적 포화 구간 | $dL/dt \approx -Cl_L/V_c\cdot L$ | 선형 PK처럼 보임; 이 구간만 보면 TMDD 오판 위험 |
| **C** | 선형 + 표적 매개 혼합 | $C_L$ ≈ $K_m$ 구간 | 두 경로 병존 | 비선형성 가장 뚜렷한 구간; 치료 유효 농도 범위 |
| **D** | $k_{off}$·$k_{e(RL)}$ 지배 terminal | $C_L \ll K_m$ | $dL/dt \approx -k_{e(RL)}\cdot L$ | 다시 선형; terminal slope로 $k_{off}$+$k_{e(RL)}$ 추정 가능 |

**Phase A의 역설적 용량-반비례 기울기:**
- PK27 Figure 27.1: 저용량(1.5 mg/kg)에서 Phase A 하강이 고용량(45 mg/kg)보다 더 가파름
- 원인: 저농도에서 $k_{on}\cdot C_L\cdot R$ 항의 R 분율이 상대적으로 크기 때문

**청소율 vs 리간드 농도 관계 (R&T Figure 21-8 기반):**
$$Cl_{total}(C_L) = Cl_L + \frac{V_{max}}{K_m + C_L}$$
- 저농도: $Cl_{total} \approx Cl_L + V_{max}/K_m$ (최대; 표적 경로 미포화)
- 고농도: $Cl_{total} \approx Cl_L$ (표적 포화로 TMDD 기여 감소)

---

# §5 — 혼동쌍 해부

---

## 혼동쌍 1: $K_m$ (TMDD 준정상상태) vs $K_d$ (평형 해리상수)

| 비교 차원 | $K_m$ | $K_d$ |
|---|---|---|
| **표면적 유사성** | 둘 다 농도 단위(mg/L, nM)를 가지며 "결합 친화도"처럼 들린다 | |
| **수식** | $K_m = \dfrac{k_{off} + k_{e(RL)}}{k_{on}}$ | $K_d = \dfrac{k_{off}}{k_{on}}$ |
| **생물학적 지시체** | 복합체 형성과 내재화 속도를 모두 반영한 **효율적 농도** — 복합체 소실(분해 포함)을 고려한 준정상상태 값 | 순수 결합-해리 평형의 친화도 — 내재화 속도($k_{e(RL)}$)와 무관 |
| **변화 방향** | $k_{e(RL)}$ 증가 → $K_m$ 증가 (내재화 빠른 약물이 $K_m$ 더 큼) | $k_{e(RL)}$와 무관; 오직 $k_{off}/k_{on}$에 의존 |
| **임상·모델링 결과** | $K_d$를 $K_m$으로 잘못 사용하면 표적 점유율을 과소 추정하고, 임상적으로 효과적인 농도 범위를 설계 실패 | |
| **⚡ 기억 고리** | "$K_m$은 $K_d$의 야심(aspiration)이 내재화(internalization)라는 현실에 의해 확대된 것이다 — 세포가 복합체를 빠르게 집어삼킬수록 $K_m$은 $K_d$보다 커진다." | |

---

## 혼동쌍 2: $k_{in}$ 변화 vs $k_{out}$ 변화의 임상적 결과

| 비교 차원 | $k_{in}$ 변화 (합성 속도 변화) | $k_{out}$ 변화 (분해 속도 = CL 변화) |
|---|---|---|
| **표면적 유사성** | 둘 다 steady-state 수준 변화를 유발한다 | |
| **수식** | $A_{ss} = k_{in}/k_{out}$에서 $k_{in}$ 변화 | $t_{ss} \propto 1/k_{out}$; $A_{ss} = k_{in}/k_{out}$ 둘 다 변화 |
| **생물학적 지시체** | 합성/분비 조절 — 호르몬 결핍, 염증 매개체 생성 변화 | 청소율 조절 — 수용체 발현 밀도, FcRn 포화, 항약물 항체 |
| **변화 방향** | $A_{ss}$만 변화; $t_{ss}$ (새 정상상태 도달 시간)는 **불변** | $A_{ss}$와 $t_{ss}$ **모두** 변화 (Gabrielsson Figure 2.70) |
| **임상 결과** | 폐경 후 에스트라디올 저하의 원인: $k_{out}$ 변화가 아닌 $k_{in}$ 감소가 원인임 (R&T PK31) | TMDD에서 고용량 투여 시 표적 포화로 $k_{out,RL}$ 감소 → $t_{1/2}$ 연장 |
| **⚡ 기억 고리** | "$k_{in}$은 수도꼭지 — 잠그면 수위(steady-state)만 내려가고, 수조의 배수 속도($t_{ss}$)는 그대로다. $k_{out}$은 배수구 — 막으면 수위도 오르고 수조가 차는 시간($t_{ss}$)도 길어진다." | |

---

## 혼동쌍 3: TMDD 풀 모델 vs Michaelis-Menten 근사 — **Critical Blow 혼동쌍**

| 비교 차원 | 풀 TMDD 모델 | MM 근사 |
|---|---|---|
| **표면적 유사성** | 둘 다 비선형 PK를 기술하며, 고농도에서 수렴하는 것처럼 보인다 | |
| **수식** | 4개 ODE 8파라미터 ($k_{on}$, $k_{off}$, $k_{e(RL)}$, $R_0$, $k_{out}$ + 비특이적 disposition) | $Cl_{MM} = V_{max}/(K_m+C_L)$ — 2파라미터 |
| **생물학적 지시체** | 리간드·수용체·복합체의 실제 질량 균형; 표적 점유율 예측 가능 | 표적의 존재를 블랙박스화; 표적 점유율 예측 불가 |
| **농도 범위 적용성** | 전체 농도 범위(저농도 TMDD 지배 ~ 고농도 선형 CL 지배)에서 유효 | **고농도($C_L \gg R_0$)에서만 유효**; 저농도에서 체계적 편차 |
| **임상 결과** | PK27: $K_m$ = 0.03 mg/L (정확 추정) | PK27 MM 근사: $K_m$ = 3.7 mg/L → **123배 과대 추정** → 저용량 곡선 완전 실패 |
| **⚡ 기억 고리** | "풀 TMDD는 수용체를 '살아있는 존재'로 본다 — turnover가 있고 약물과 대화한다. MM 근사는 수용체를 '배수구 구멍'으로만 본다 — 크기는 알지만 그 안에서 무슨 일이 일어나는지는 모른다." | |

| **치명적 타격** | 저용량 코호트(FIH dose escalation)에서 MM 근사 기반으로 PK 모델이 구축된 경우, Phase C(혼합 비선형 구간)에서 약물 농도를 체계적으로 과대 예측하여 임상적으로 유효한 표적 점유율 유지 용량이 실제보다 낮다고 판단, 치료 실패 용량이 "유효"로 IND에 제출될 수 있다. |

---

# §7 — Self-Test: Active Recall Module

---

**Q1** ★★ [회상] | Gabrielsson PK27 cynomolgus monkey 모델에서 리간드만(Dataset I) 피팅했을 때와 리간드+표적+복합체(Dataset III) 피팅했을 때, $k_{e(RL)}$의 CV%는 각각 얼마였는가? 이 차이가 발생하는 수학적 이유를 설명하라.

<details>
<summary>정답 공개</summary>

Dataset I(리간드만): CV% = 27, Dataset III(리간드+표적+복합체): CV% = 2. 27배 개선. **이유:** $k_{e(RL)}$은 복합체(RL) 소실 속도를 결정하지만, 리간드 데이터만으로는 $k_{off}\cdot C_{RL}$과 $k_{e(RL)}\cdot C_{RL}$ 두 소실 경로가 parameter identifiability 문제로 분리 불가능하다. RL 농도-시간 곡선이 추가되어야 $k_{e(RL)}$의 직접 관찰값이 생겨 precision이 급격히 향상된다. 이것이 TMDD 임상 연구에서 soluble target(R) 및 complex(RL) biomarker 측정이 필요한 이유다.

**다음 깊이 질문:** PK27에서 $k_{off}$의 CV%도 27→3%로 개선되었다. $k_{off}$가 RL 데이터 없이 잘 추정되지 않는 이유는 무엇인가?
</details>

---

**Q2** ★★ [회상] | TMDD 4상 패턴에서 역설적으로 저용량 mAb 투여 시 Phase A에서 농도 하강 기울기가 더 가파른 이유를 $k_{on}\cdot C_L\cdot R$ 항으로 설명하라.

<details>
<summary>정답 공개</summary>

Phase A에서는 $dC_L/dt \approx -k_{on}\cdot C_L\cdot R$이 지배한다. 고용량 투여 시 초기 농도가 매우 높아 수용체 $R$이 거의 즉시 포화($R\approx 0$)되므로 이 항이 급격히 감소한다. 반면 저용량에서는 초기 $C_L$이 낮지만 $R \approx R_0$ (미포화 상태 유지)이므로 $k_{on}\cdot C_L\cdot R_0$가 상당한 청소율 기여를 유지한다. 따라서 상대적 제거 속도($dC_L/dt$ ÷ $C_L$)가 저용량에서 더 크다.

**다음 깊이 질문:** 이 역설이 FIH dose escalation에서 어떤 안전성 함의를 가지는가?
</details>

---

**Q3** ★ [회상] | Gabrielsson §2.6.4 에스트라디올 turnover 연구에서 폐경 후 여성의 에스트라디올 저하 원인이 CL 증가가 아닌 $k_{in}$ 감소임을 밝히기 위해 사용된 설계는 무엇이었는가?

<details>
<summary>정답 공개</summary>

급속 정맥 주입(rapid IV infusion)으로 외인성 에스트라디올을 추가 투여하여 내인성 turnover rate과 CL을 분리 추정했다. 15명 폐경 후 여성에서 $Cl = 0.76$–2.9 L/min으로 가임 여성과 유사하게 측정되어 CL은 변하지 않았고, $k_{in}$ (turnover rate)만 감소(<1~36 µg/24h, mean 19 µg/24h)한 것이 확인되었다. 외인성 도전(exogenous challenge)이 내인성 합성과 제거를 분리하는 핵심 설계 원리다.

**다음 깊이 질문:** IV 도전 없이 SC 투여만으로는 $t_t$와 MIT를 완전히 분리할 수 없는 이유는?
</details>

---

**Q4** ★★ [적용] | 어떤 항체 약물의 PK27 유사 데이터에서 MM 근사로 피팅하니 저용량 군에서 CWRES가 +2.5~+3.0으로 지속적으로 양성이었다. 이 패턴의 이름을 지정하고, 풀 TMDD 모델로 전환해야 하는 임상 판단 근거를 서술하라.

<details>
<summary>정답 공개</summary>

이 패턴은 **"Low-Dose Cliff Sign"**이다 (카드 4에서 명명). CWRES 양성 편향은 MM 근사가 저농도에서 실제 $K_m$보다 훨씬 큰 값으로 추정하여 실제 제거가 더 빠름에도 예측 농도를 과대 추정하는 것을 나타낸다. 전환 근거: (1) Phase 1 FIH에서 저용량 코호트의 $C_{max}$가 $R_0$에 근접하는 경우, (2) 다음 코호트 용량 예측에 MM이 사용되면 안전 마진 오계산, (3) 표적 점유율 예측이 요구될 때 (면역종양학적 효력 endpoint). 규제 문서에서 "TMDD 모델이 더 mechanistic하므로 전체 용량 범위의 농도를 정확히 기술한다"로 방어.

**다음 깊이 질문:** Phase A의 저용량 역설적 가파름이 임상 안전성에서 갖는 의미는?
</details>

---

**Q5** ★ [적용] | Anakinra (IL-1 수용체 길항제, MW = 17,258 g/mol)를 중증 신부전 환자에게 투여 시, 정상 신기능 환자 대비 AUC가 3.8배 증가했지만 SC 투여 후 terminal $t_{1/2}$는 5.24 hr에서 9.71 hr로만 증가했다. 이 불균형($AUC$ 3.8배 vs $t_{1/2}$ 1.85배)을 설명하라.

<details>
<summary>정답 공개</summary>

SC 투여 후 terminal $t_{1/2}$는 absorption rate-limited이다: 정상 신기능 환자에서 IV $t_{1/2}$ = 2.6 hr, SC terminal $t_{1/2}$ = 5.24 hr → SC 흡수 반감기가 제거 반감기보다 길어 absorption phase가 terminal slope를 지배한다. 신부전에서 IV $t_{1/2}$가 크게 증가해도, 흡수가 여전히 느리다면 SC terminal $t_{1/2}$ 변화는 제한적이다. AUC는 $F\cdot Dose / CL$이므로 CL 감소(3.8배)가 AUC 증가에 직접 반영되지만, terminal $t_{1/2}$는 흡수 속도에 의해 둔화된 변화를 보인다. 이 현상이 ESRD 환자에서 dosing 조절이 AUC 기반으로 이루어져야 하는 이유다.

**다음 깊이 질문:** IV와 SC 투여를 모두 수행해야만 이 분리를 명확히 할 수 있는 이유는?
</details>

---

**Q6** ★★ [적용] | FcRn 매개 IgG 보존에서 메토트렉세이트(methotrexate)가 adalimumab CL을 29–44% 감소시키는 기전을 설명하라. 이것이 병용 투여 PK 설계에서 갖는 함의는?

<details>
<summary>정답 공개</summary>

메토트렉세이트는 비장 macrophage의 Fc-γ 수용체(FcγRI, FcγRIII)를 하향 조절한다. FcγR은 IgG-opsonized 복합체의 식세포 작용을 통한 제거 경로를 담당하므로, 그 발현 감소는 adalimumab의 Fc 매개 제거를 억제하여 CL이 29–44% 감소하고 노출이 증가한다. 임상 함의: (1) RA 임상시험에서 MTX 병용군이 adalimumab 단독군보다 효력이 더 높은 이유 중 하나가 이 PK 상호작용, (2) 설계 시 병용 vs 단독 코호트를 분리하고 PK 매개변수를 공변량으로 처리해야 함.

**다음 깊이 질문:** 도파민 작용제(leuprolide, pergolide)가 FcγR을 상향 조절한다면 mAb의 CL에 어떤 영향을 미칠 것으로 예측하는가?
</details>

---

**Q7** ★★ [적용] | R&T Table 21-8에서 복합체 형태의 h-growth hormone(GH-binding protein 결합)이 비결합 상태보다 CL이 6.1배 낮고 $V_{ss}$가 3.6배 낮다. 이 현상을 단백질 약물 PK의 관점에서 설명하라.

<details>
<summary>정답 공개</summary>

비결합 GH(MW ~22,000 g/mol)는 신사구체 여과(sieving coefficient ~0.65)와 조직 수용체 매개 내재화로 빠르게 제거된다. GH-binding protein(MW ~60,000 g/mol)와 복합체를 형성하면 총 MW가 ~82,000 g/mol로 증가하여: (1) 사구체 여과가 거의 차단, (2) 조직 분포(수용체 접근성)가 감소, (3) 혈장 단백질 결합으로 비특이적 단백분해 효소 접근이 제한된다. 따라서 CL 6.1배 감소(2.3→14 mL/min·kg), $V_{ss}$ 3.6배 감소(71→256 mL/kg). 이는 PEGylation(polyethylene glycol 부착)과 glycosylation이 단백질 약물 반감기를 연장하는 같은 원리다.

**다음 깊이 질문:** GH-binding protein이 $V_{ss}$를 감소시킨다면, 결합 단백질은 조직 분포를 저해하는 것인가 촉진하는 것인가?
</details>

---

**Q8 — 보스 딜레마 [★★ 고정]** | [Socratic Dilemma]

**임상 시나리오:** Phase 1 mAb FIH 시험에서 4개 용량 코호트(1, 5, 15, 45 mg/kg IV)의 리간드 PK 데이터를 수집했다. GOF 분석에서 MM 근사 모델은 가장 낮은 코호트(1 mg/kg)에서 CWRES = +2.8로 양성 편향을 보이지만, $OFV$는 풀 TMDD 모델보다 6점 낮다(파라미터가 2개 적으므로 ΔAIC가 유리). 수용체 데이터와 복합체 데이터는 없다. Phase 2 용량(목표: 임상적으로 유효한 표적 점유율 >80%)을 결정하는 규제 제출용 최종 모델을 선택해야 한다.

**당신은 어느 모델을 선택하는가: (A) MM 근사 또는 (B) 풀 TMDD 모델?**

<details>
<summary>수석 모델러의 Trade-off 논리 공개</summary>

**현실적 답변: 조건부 (B) 풀 TMDD 모델, 단 parameter identifiability 충분한지 검증 후.**

**MM 근사를 선택하면 안 되는 이유:**
AIC/OFV 우위는 모델 복잡도 패널티를 고려한 통계적 지표이지만, 1 mg/kg 코호트의 체계적 편차(CWRES +2.8)는 모델의 구조적 misspecification을 의미한다. 이 코호트의 농도 범위가 Phase 2 치료 농도 범위와 겹칠 경우(표적 점유율 80% 달성 용량이 1~5 mg/kg 사이라면), MM 근사로 예측한 용량은 표적 점유율을 과소 추정하여 치료 실패 용량을 "유효 용량"으로 규제 제출하게 된다.

**풀 TMDD 모델의 리스크와 관리:**
수용체·복합체 데이터 없이 풀 TMDD를 피팅하면 $k_{off}$와 $k_{e(RL)}$의 개별 추정이 불가능할 수 있다 (PK27 CV% 27%). 해결 전략: (1) $k_{off}/k_{on} = K_d$를 in vitro SPR(surface plasmon resonance) 측정값으로 고정, (2) $R_0$를 문헌 수용체 밀도 데이터로 초기화, (3) VPC로 전체 용량 범위의 예측 성능 검증.

**규제 제출 방어 언어:** "The full TMDD model better characterizes the mechanistic basis of nonlinear elimination across the entire concentration-time range observed in the Phase 1 study. Although the quasi-steady-state approximation (Michaelis-Menten) yielded lower OFV with fewer parameters, the systematic positive bias in the lowest dose cohort (CWRES = +2.8) indicates structural misspecification in the therapeutically relevant concentration range. The full TMDD model was selected as it enables prediction of target occupancy required for Phase 2 dose selection."

**다음 깊이 질문:** $R_0$를 문헌에서 고정하면 population variability를 어떻게 처리해야 하는가?
</details>

---

# §8 — Meta-Frame & Big Picture

---

### A. 28세션 아키텍처 내 위치

이 세션(I-08)은 Vol I의 핵심 전환점에 위치한다:

- **이전에서 온 것:** I-07(Michaelis-Menten 비선형 PK)에서 포화 가능 제거라는 개념을 배웠고, I-01의 CL·V 기초 위에 서 있다. Turnover 개념은 PD 세션들(I-09 Emax, I-10 Indirect Response)의 직접 전제다.
- **바로 다음에 오는 것:** I-09(Emax·Hill 모델)에서 $k_{in}/k_{out$ 구조가 pharmacodynamic response 모델로 확장되고, I-10(Indirect Response)에서 수용체 turnover와 약물 효과 결합이 완성된다.
- **이 기반에 결정적으로 의존하는 고급 도메인:**
  - **PopPK:** mAb PK 모델에서 IIV가 어떤 파라미터($k_{on}$, $R_0$, $k_{e(RL)}$)에 붙는지 결정하려면 TMDD 구조 이해 필수
  - **QSP:** 수용체 turnover와 피드백 회로가 복잡 생리 시스템 모델의 핵심 구성 요소
  - **ADC PK:** linker stability, payload release가 TMDD에 추가된 복합 구조

---

### B. Dependencies — 이 세션을 대충 넘겼을 때의 고급 실패 모드

**실패 모드 1: 비선형 PK 오진**
Turnover와 TMDD를 이해하지 못하면, mAb의 4상 패턴에서 Phase B(선형처럼 보이는 구간)만 보고 단순 2구획 선형 모델로 피팅하게 된다. 이 모델로 Phase C 영역(치료 농도)을 예측하면 AUC를 체계적으로 과소 추정한다. 인과관계: I-08 누락 → II-07 기저 모델 구축 오류 → II-08 공변량 분석에서 표적 발현량(수용체 밀도)을 공변량으로 시도하지 않음 → Phase 2 용량 선택 실패.

**실패 모드 2: 단백질 약물 SC 투여 PK 분석 오류**
림프계 흡수의 느린 속도와 first-pass 단백분해를 이해하지 못하면 SC mAb의 긴 $T_{max}$(5–17일)를 비정상 흡수로 오판하거나, SC $t_{1/2}$가 absorption rate-limited인지 elimination rate-limited인지 구분하지 못한다. 이는 NDA 제출 시 population PK 모델의 흡수 서브모델 misspecification으로 이어져 특수 집단(소아, 신부전 환자) dose adjustment 권고 오류를 야기한다.

---

### C. Professional Moat

**NONMEM을 실행하여 파라미터를 추출하는 것은 이미 자동화 가능하다. 이 세션의 TMDD 구조와 turnover 수학을 진정으로 내면화한 모델러만이 — 수렴 실패, $K_m$ vs $K_d$ 혼동, 저용량 CWRES 체계 편차 앞에서 — 무엇을 할 수 있는가?**

구조적 필연성 수준의 정확한 답: 이 모델러만이 **"무엇이 데이터에 없는 정보인가"를 안다** — $k_{off}$와 $k_{e(RL)}$이 리간드 데이터만으로 분리 불가능함을 사전에 인식하고, in vitro $K_d$ 측정값을 사전정보로 활용하는 Bayesian 피팅 전략을 설계하거나, 실험 설계 단계에서 soluble target biomarker 측정을 프로토콜에 포함시키도록 임상팀을 설득할 수 있다. 또한 MM 근사의 $K_m$ 과대 추정이 Phase 2 용량 선택에 미치는 구체적 위험을 수치로 규제 문서에 명시할 수 있다 — "estimated $K_m$ from MM approximation (3.7 mg/L) is 123-fold greater than that derived from the mechanistic TMDD model (0.03 mg/L), indicating that the MM approximation is not appropriate for dose-response prediction in the sub-$R_0$ concentration range."

---

```
✦ STEP 1 완료.

다음이 준비되었습니다:
  • §1 세션 헤더 & 로드맵
  • §2 개념 해부 카드 (6개 개념, Apex: TMDD 풀 모델 — Mager & Jusko 프레임워크)
  • §5 혼동쌍 해부 (3개 쌍, Critical Blow 적용: TMDD 풀 모델 vs MM 근사)
  • §7 자기 테스트 (8개 질문, 보스 딜레마 포함)
  • §8 메타프레임 & 빅 픽처
  • 감지된 소스 유형: Vol I — R&T + Gabrielsson 혼합
  • Data Anchoring 소스:
      - Gabrielsson PK27: cynomolgus monkey mAb, 4 IV 용량(1.5/5/15/45 mg/kg),
        Table 27.2 실제 파라미터 (kon=0.096, koff=0.001, R0=12, kout=0.009, ke(RL)=0.003)
      - Gabrielsson PK30: IgX (growth hormone) in healthy human, SC 40 µg/kg,
        Cl/F=0.03 L/h/kg, turnover rate=0.78 µg/h/kg, t½=2.5h, kout=0.27 h⁻¹
      - Gabrielsson PK31: Estradiol in 15 post-menopausal women, Cl=0.76-2.9 L/min
      - R&T Table 21-16: Anakinra renal function groups (CrCl 95→ESRD, AUC/t½ progression)
      - R&T Table 21-14/21-15: SC bioavailability 실제 수치 (somatropin, adalimumab 등)

"계속"을 입력하면 Step 2 HTML 컴파일러가 실행됩니다.
Step 2는 위 내용 전체(§1·§2·§5·§7·§8) +
§3(구조적 동형성 지도) + §4(인터랙티브 시뮬레이터 + Assumption Collapse 토글) +
§6(실용 시나리오 & 진단 병리)를 단일 완성 HTML 파일로 통합합니다.
---
```

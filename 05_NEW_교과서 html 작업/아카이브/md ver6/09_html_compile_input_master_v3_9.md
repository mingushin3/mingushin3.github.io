# 세션 09 — TMDD: Target-Mediated Drug Disposition, full vs MM approximation, $K_d$/$K_m$/target turnover — v3.9

이 자료는 Gabrielsson & Weiner 5e의 turnover, PK26 Efalizumab, PK27 TMDD 사례와 Rowland & Tozer 5e Ch.21 Protein Drugs를 학습자용으로 정리한 파일입니다. 다루는 범위는 단백질 약물 PK, mAb 배치, FcRn, TMDD, Michaelis-Menten 근사, 자료 풍부도(data richness), assay 식별성입니다.

---

## PART A — 학습자용 완성 핸드아웃

> 🎯 **이 세션의 한 줄 경로**: Turnover → mAb ADME → TMDD → Full TMDD → MM 경계.  
> 모든 판단의 기준은 단 하나 — **"어떤 데이터가 어떤 파라미터를 가르쳤는가?"**

---

> **임상 장면**  
> 한 단클론 항체를 **1.5, 5, 15, 45 mg·kg⁻¹** 네 용량으로 급속 정맥 주사한 PK27 데이터. 고용량 곡선은 그럴듯하게 맞지만, 가장 낮은 용량의 곡선만 체계적으로 어긋납니다. MM 모델의 $K_m$은 **3.7**, Full TMDD 모델의 $K_m$은 **0.03** — 약 **123배** 차이입니다. 이건 "피팅이 약간 안 됐다"가 아닙니다. 저농도 외삽, trough 예측, target occupancy 판단을 통째로 흔드는 **구조적 신호**입니다. [G&W pp.602–603; G&W p.609]

## 빠른 읽기 경로

시간이 부족하면 **M1 → M2 → M3 → M4 → M5** 다섯 카드만 순서대로 읽으면 이 세션의 의사결정 체계가 작동합니다.

| 카드 | 이 경로에서의 역할 |
|---|---|
| **M1** | Turnover paradigm — baseline은 고정값이 아니라 $k_{in}/k_{out}$의 결과 |
| **M2** | 항체의 ADME 4관문 — distribution / lymphatic input / proteolysis·RME / FcRn rescue |
| **M3** | TMDD 곡선의 Phase A–D — 시간 순서가 아니라 농도 영역의 지도 |
| **M4** | Full TMDD ODE — ligand·target·complex·sink를 한 system으로 |
| **M5** | MM 근사가 무너지는 경계 — 저농도 외삽에서의 구조적 편향 |

읽는 동안 다음 한 질문을 가지고 다닙니다: **"이 파라미터를 실제로 가르쳐주는 데이터는 무엇인가?"**

**학습 완료 후 체크**:
- $k_{in}$, $k_{out}$, $k_{on}$, $k_{off}$, $k_{e(RL)}$, $K_d$, $K_m$이 왜 서로 대체 불가능한지 입으로 설명할 수 있는가?
- Full TMDD가 필요한 상황과 MM 근사가 내삽 도구에만 머무는 상황을 데이터 기반으로 구분할 수 있는가?
- 고용량 적합이 좋다는 사실이 왜 저용량 외삽을 자동으로 정당화하지 않는지 설명할 수 있는가?

---

# 갱신된 큐레이션 맵

이 세션의 핵심은 "항체 PK" 자체가 아닙니다. 핵심은 **turnover 수학이 TMDD(target-mediated drug disposition; 표적 결합이 약물 배치 자체를 바꾸는 현상)로 확장되는 순간, 어떤 자료가 어떤 파라미터를 가르치는가**를 체화하는 것입니다. 10분 핸드아웃 기준으로 남겨야 할 중심축은 5개입니다.

## MUST

| # | 개념 | 왜 핵심인가 |
|---|---|---|
| M1 | **Turnover Paradigm ($k_{in}$/$k_{out}$)** | TMDD의 target($R$)은 endogenous turnover pool입니다. $k_{in}/k_{out}$ 없이는 target baseline, recovery, $R_0$, $k_{out}$ 식별이 설명되지 않습니다. [G&W pp.95–97] |
| M2 | **단백질/항체의 특수한 PK** | 큰 분자량, 작은 $V_d$, 림프관 흡수, 신장 cutoff, FcRn salvage — mAb 곡선의 "느림"과 비선형성은 모두 여기서 나옵니다. [G&W pp.97–102; R&T pp.701–724] |
| M3 | **TMDD 4-Phase 곡선** | Phase A–D를 읽을 줄 알아야 Full TMDD와 MM 근사 중 무엇을 쓸지 데이터 기반으로 결정할 수 있습니다. [G&W pp.603–610; R&T pp.711–712] |
| M4 | **Full TMDD Model** **[⚡ Apex Concept]** | ligand, target, complex, sink가 하나의 ODE system으로 묶이는 지점. PK와 PD가 같은 수식으로 연결됩니다. [G&W pp.603–609; R&T pp.711–712] |
| M5 | **Michaelis-Menten 근사의 경계** | 관찰된 용량 범위 안에서는 쓸 수 있습니다. 하지만 저농도 외삽과 occupancy(← 표적 중 ligand가 결합한 비율) 판단에서는 구조적 편향을 만들 수 있습니다. [G&W p.609; R&T p.712] |

## CONTEXT

| 맥락 | 어디에 들어가는가 |
|---|---|
| 욕조에 물 차오르는 비유 | M1 직관 보조 [G&W p.96] |
| IgX sc 40 µg·kg⁻¹ + immunoglobulin turnover | M1 임상 앵커 [G&W pp.100–102] |
| 폐경 후 여성의 estradiol turnover | M1 내인성 turnover 확장 [G&W pp.102–104] |
| Baseline scenarios / circadian / feedback | M1 가정 경계 [G&W pp.104–111] |
| 단백질 $V_d$, renal sieving, hepatic uptake, FcγR/FcRn | M2 ADME 기전 [R&T pp.701–709] |
| Somatropin sc absorption-rate-limited | M2 흡수 맥락 [R&T p.721] |
| Anakinra 신장질환 | M2 신장질환 맥락 [R&T p.724] |
| Efalizumab PK26 reduced model | M5 "MM이 제한적으로 통하는 사례" [G&W pp.599–601; R&T p.710] |

---

<!-- SLIDE_START: §1 | title: 세션 헤더와 로드맵 -->
<!-- SECTION_CORE: SC-01 -->
# §1 세션 헤더와 로드맵(Session Header & Roadmap)

## 3-Layer 개념 지도

```text
Layer 1 — 무엇인가
  Turnover baseline / mAb ADME 관문 / TMDD phase / Full TMDD / MM 경계

Layer 2 — 어떻게 계산되는가
  A0 = kin/kout / dR/dt & dRL/dt / Kd = koff/kon / Km = (koff + ke(RL))/kon / ClMM = Vmax/(Km+C)

Layer 3 — 언제·왜 중요한가
  baseline 회복 / 느린 SC 입력 / 저용량 외삽 / target occupancy / 모델 선택 방어
```

## 지식 위치

```text
1구획·2구획 선형 PK + Michaelis-Menten + ODE 기본
        → 이 세션: Turnover → mAb ADME → TMDD → Full TMDD/MM 경계
        → mAb PopPK · TMDD/QSP · target occupancy 시뮬레이션 · biologics 임상약리 리포트
```

🧭 **읽는 순서**  
카드 1 (M1): baseline은 왜 단순한 0시간 값이 아니라 turnover pool인가?  
카드 2 (M2): mAb 곡선의 느림은 어떤 ADME 관문들이 합쳐진 결과인가?  
카드 3 (M3): TMDD 곡선의 Phase A–D는 어떤 농도 영역을 가리키는가?  
카드 4 (M4): ligand·target·complex·sink는 어떤 ODE topology로 묶이는가?  
카드 5 (M5): MM 근사는 어느 경계 안에서만 방어 가능한가?

**Source**:
- Gabrielsson & Weiner 5e, Ch.2 §2.6 Turnover [G&W pp.94–111]
- Gabrielsson & Weiner 5e, Case Study PK26 Efalizumab [G&W pp.599–601]
- Gabrielsson & Weiner 5e, Case Study PK27 TMDD [G&W pp.602–610]
- Rowland & Tozer 5e, Ch.21 Protein Drugs [R&T pp.687–730]

## 핵심 아이디어(Big Idea)

> 항체의 비선형 PK는 "큰 약물이 천천히 빠지는 것"이 아닙니다. **Ligand가 endogenous target turnover system에 결합하면서 만들어지는 농도의존적 청소율**입니다. Full TMDD를 MM으로 줄이면 제한된 용량 범위에서는 맞아 보일 수 있지만, PK27에서는 $K_m$이 **0.03에서 3.7로 약 123배 과대예측**되어 저농도 외삽이 구조적으로 틀어졌습니다. [G&W p.609]

## 로드맵

```text
M1. Turnover Paradigm
       ↓
M2. 단백질/항체 ADME 특수성
       ↓
M3. TMDD 4-phase 곡선 읽기
       ↓
M4. Full TMDD Model: ligand + target + complex + sink
       ↓
M5. Michaelis-Menten 근사: 언제 통하고 언제 무너지는가
```

이 세션은 1구획/2구획 PK, Michaelis-Menten kinetics, ODE 기본, NONMEM `$DES` 구조를 전제로 합니다. 후속으로는 mAb PopPK, TMDD/QSP, target occupancy 시뮬레이션, FcRn engineering, biologics 임상약리 리포트 작성으로 이어집니다.

**Section recap**: 이 세션의 판단 기준은 "곡선이 예쁘게 적합되는가?"가 아닙니다. **"이 데이터가 target turnover, binding, complex sink를 분리해서 가르치는가?"**입니다.

---

<!-- SLIDE_START: §2 | title: 개념 해부 카드 -->
<!-- SECTION_CORE: SC-02 -->
# §2 개념 해부 카드(Concept Anatomy Cards)

> 🎯 **이 카드들이 존재하는 이유**: $k_{in}$/$k_{out}$이 baseline, pool size, recovery time을 동시에 지배합니다. Target $R$을 고정값으로 보는 순간 TMDD 해석은 출발점부터 흔들립니다.

---

<!-- SLIDE_START: M1 | title: Turnover Paradigm -->
<!-- SECTION_CORE: SC-03 -->
## ▌ Card M1 — Turnover Paradigm ($k_{in}$/$k_{out}$)

> **거장의 시각**  
> baseline을 단순한 predose 값으로 읽으면 $R_0$, $k_{out}$, recovery time이 모두 잔차나 임의 파라미터처럼 보입니다. Turnover 관점으로 보면 target $R$은 ligand가 교란하는 endogenous pool이고, TMDD의 출발점이 명확해집니다.

Turnover의 핵심 메시지는 이것입니다 — 내인성 물질의 baseline은 고정된 숫자가 아니라, **0차 입력 $k_{in}$과 1차 소실 $k_{out}\cdot A$가 만들어내는 동적 평형**입니다. TMDD의 target $R$도 같은 구조를 따릅니다. 그래서 mAb가 target에 결합한다는 것은 외부 ligand가 endogenous turnover pool에 개입한다는 뜻입니다. [G&W pp.95–96]

### A. 형식적 정의

| 파라미터 | 단위 | 의미 | 변화 원인 |
|---|---|---|---|
| $A$ | mass | turnover pool 안의 양 | 생성·소실 균형 |
| $k_{in}$ | mass/time | 0차 입력·생성률 | 합성 증가/감소 |
| $k_{out}$ | time⁻¹ | 1차 분획 소실률 | catabolism·degradation 속도 |
| $A_0$ | mass | 정상상태 baseline 양 | $k_{in}$↑ 또는 $k_{out}$↓ |
| $t_t$ | time | pool 교체 시간 | 주로 $k_{out}$ 변화 |

$$
\overbrace{\frac{dA}{dt}}^{\text{pool 변화}}
=
\underbrace{k_{in}}_{\text{0차 입력}}
-
\underbrace{k_{out}\cdot A}_{\text{1차 소실}}
\qquad \text{Eq.2:237}
$$

정상상태에서 다음 관계가 성립합니다. [G&W pp.95–96]

| 관계식 | 의미 | 출처 |
|---|---|---|
| $k_{in}=k_{out}\cdot A_0$ | 입력 = 출력 | Eq.2:239 [G&W p.96] |
| $k_{out}=k_{in}/A_0$ | 분획 turnover rate | Eq.2:240 [G&W p.96] |
| $A_0=k_{in}/k_{out}$ | baseline 양 | Eq.2:241 [G&W p.96] |
| $t_t=A_0/k_{in}=1/k_{out}$ | turnover time | Eq.2:242 [G&W p.96] |
| $t_t=V_{ss}/Cl=MRT$ | turnover time이 PK MRT와 연결 | Eq.2:243 [G&W p.96] |
| $t_{1/2}=\ln(2)/k_{out}=\ln(2)\cdot t_t$ | 반감기 관계 | Eq.2:244 [G&W p.96] |

$$
\begin{aligned}
\underbrace{A_0}_{\text{baseline 양}} &= \underbrace{\frac{k_{in}}{k_{out}}}_{\text{입력/소실 균형}} \\
\underbrace{t_t}_{\text{교체 시간}} &= \underbrace{\frac{1}{k_{out}}}_{\text{소실 역수}} = \underbrace{\frac{V_{ss}}{Cl}}_{\text{PK 체류시간}} = \underbrace{MRT}_{\text{평균 체류}} \\
\underbrace{t_{1/2}}_{\text{반감기}} &= \underbrace{\frac{\ln(2)}{k_{out}}}_{\text{1차 반감}}
\end{aligned}
$$

단위가 핵심입니다 — $k_{in}$은 mass/time, $k_{out}$은 time⁻¹입니다. 이 구분을 놓치면 **target 합성($k_{in}$)과 ligand-target binding on-rate($k_{on}$)를 섞게 됩니다.**

> 💡 **Baseline은 결과값이지 입력값이 아닙니다.** $A_0$는 관찰값 하나가 아니라 $k_{in}/k_{out}$ 균형이 만들어내는 결과입니다. 그리고 $k_{out}$이 바뀌면 level뿐 아니라 새 정상상태에 도달하는 시간까지 함께 바뀝니다.

### B. 직관: 수도꼭지와 배수구

10 L 욕조에 분당 1 L의 물이 들어오면 turnover time은 10분입니다. 사람 몸의 물 42 L와 하루 섭취량 2.5 L를 넣으면 water turnover time은 **약 17일**입니다. 핵심은 "얼마나 많이 있는가"가 아니라 **"현재 pool 전체가 얼마나 빨리 교체되는가"**입니다. 이 단순한 욕조 그림이 endogenous IgG, target receptor, hormone turnover와 정확히 같은 수학입니다. [G&W p.96]

비대칭이 하나 있습니다 — $k_{in}$을 바꾸면 정상상태 level만 바뀝니다(linear kinetics 조건에서 도달 시간은 그대로). 반면 $k_{out}$을 바꾸면 **level과 도달 시간이 같이 바뀝니다.** [G&W p.97]

### C. 임상 앵커

**IgX 사례**: Growth hormone-like **IgX**(내인성 단백질형 펩타이드)를 40 µg·kg⁻¹ sc 투여했더니 predose baseline이 32 µg·L⁻¹였습니다. 추정값: $Cl/F=0.03\ \mathrm{L\cdot h^{-1}\cdot kg^{-1}}$, $V/F=0.10\ \mathrm{L\cdot kg^{-1}}$, $k_{in}=0.78\ \mathrm{µg\cdot h^{-1}\cdot kg^{-1}}$, $t_t=2.7\ \mathrm{h}$, $MIT=1.8\ \mathrm{h}$, $t_{1/2}=2.5\ \mathrm{h}$, $k_{out}=0.27\ \mathrm{h^{-1}}$, pool size 2.3 µg·kg⁻¹. → endogenous baseline 위에 외부 ligand가 얹히는 turnover의 사례입니다. [G&W pp.100–101]

$$
\underbrace{t_t}_{\text{pool 교체}} = \underbrace{2.7\ \mathrm{h}}_{\text{IgX}},\quad
\underbrace{k_{out}}_{\text{분획 소실}} = \underbrace{0.27\ \mathrm{h^{-1}}}_{\text{시간당}},\quad
\underbrace{t_{1/2}}_{\text{반감기}} = \underbrace{2.5\ \mathrm{h}}_{\text{프로파일 요약}}
$$

**내인성 IgG turnover**: Table 2.11에서 $t_{1/2}=23$ days, 분획이화율(FCR) 6.7% plasma pool·day⁻¹, turnover 33 mg·kg⁻¹·day⁻¹입니다. 이는 R&T의 "치료용 mAb 반감기는 대략 21일"과 비슷한 숫자지만, **두 문장을 같은 사실로 합치면 안 됩니다** — 내인성 IgG는 single분자 종, 치료용 mAb는 후보별 FcRn 친화도가 다릅니다. [G&W p.102; R&T p.708]

$$
\underbrace{t_{1/2}}_{\text{IgG 반감기}} = \underbrace{23\ \mathrm{days}}_{\text{내인성 IgG}},\qquad
\underbrace{\mathrm{FCR}}_{\text{분획 이화율}} = \underbrace{6.7\%\ \mathrm{day^{-1}}}_{\text{혈장 pool}}
$$

**Estradiol turnover**: 폐경 후 여성 15명에서 estradiol(내인성 호르몬)은 평균 $k_{in}=19\ \mathrm{µg\cdot 24h^{-1}}$, $Cl=1.6\ \mathrm{L\cdot min^{-1}}$, $V_{ss}=50\ \mathrm{L}$, $t_{1/2}=26\ \mathrm{min}$, $MRT=18\ \mathrm{min}$로 보고됩니다. 폐경 후 낮은 E2 level은 **청소율 증가가 아니라 turnover(생성) 감소**로 설명됩니다 — 같은 수식 안에서 분자가 줄어든 것입니다. [G&W pp.102–104]

$$
\underbrace{k_{in}}_{\text{E2 생성률}} = \underbrace{19\ \mathrm{\mu g\cdot 24h^{-1}}}_{\text{평균 입력}},\quad
\underbrace{Cl}_{\text{제거능}} = \underbrace{1.6\ \mathrm{L\cdot min^{-1}}}_{\text{전신 CL}},\quad
\underbrace{MRT}_{\text{평균 체류}} = \underbrace{18\ \mathrm{min}}_{\text{교체 척도}}
$$

### D. 가정과 경계조건

Turnover 수학은 **baseline이 의미 있게 정의될 때** 강력합니다. 그러나 baseline은 constant일 수도, 진동(oscillating)할 수도, feedback-governed일 수도, Zeitgeber(외부 시간 신호) 의존일 수도 있습니다. PD endpoint를 다룰 때 첫 질문은 "predose 농도를 baseline으로 빼도 되는가?"가 아닙니다. **"이 endpoint는 어떤 종류의 baseline scenario인가?"**입니다. [G&W p.104]

**Trench-level tip**: predose target 측정값이 있으면 단순히 `R0=THETA`로 추정하지 말고, baseline DV record로 모델에 들어가도록 설계합니다. 이렇게 해야 $R_0$의 individual variability가 residual error로 흡수되지 않습니다. (이건 교과서 수식의 NONMEM 구현 해석이지 원문 control stream이 아닙니다.)

### E. 한계

Turnover 관계식은 linear first-order loss를 전제로 합니다. 농도가 충분히 높아져 saturable metabolism이 개입하면 Michaelis-Menten 또는 feedback model이 필요합니다. Hyaluronan, body temperature, feedback 예시들은 이 경계를 보여주는 맥락이지 독립 MUST가 아닙니다. [G&W pp.95, 105–111]

### G. Zettelkasten Atom

```text
Turnover = dynamic baseline.
A0 = kin/kout, tt = 1/kout = Vss/Cl = MRT.
TMDD target R is an endogenous turnover pool perturbed by ligand binding.
```

> 📖 **Gabrielsson & Weiner 5e, p.97, Fig.2.70**: 두 패널이 보여주는 것은 **turnover의 비대칭**입니다. $k_{in}$을 바꾸면 정상상태 level만 움직이지만, $k_{out}$을 바꾸면 level과 도달 시간이 함께 움직입니다. 이 두 패널을 직접 보지 않으면 두 변화를 모두 그냥 "rate 변화"로 묶어버리기 쉽습니다.

$$
\underbrace{k_{in}\uparrow}_{\text{입력 증가}}
\Rightarrow
\underbrace{A_0\uparrow}_{\text{level만 상승}},
\qquad
\underbrace{k_{out}\uparrow}_{\text{분획 소실 증가}}
\Rightarrow
\underbrace{A_0\downarrow}_{\text{level 하강}}+\underbrace{t_t\downarrow}_{\text{도달 시간 단축}}
$$

**M1 recap**: Turnover를 모르면 $R_0$, $k_{out}$, baseline correction, target recovery가 모두 "피팅 파라미터"로만 보입니다. Turnover를 이해하면 **TMDD는 endogenous biology 위에 얹힌 PK model**로 보입니다.

> **M1 체화 핵심**  
> ① baseline과 회복 시간을 같이 설명할 때 → $k_{in}/k_{out}$ 구조가 결정합니다  
> ② level 변화와 time-scale 변화를 구분할 때 → $k_{out}$ 변화는 둘 다 동시에 흔듭니다  
> ⚡ predose 값을 고정 baseline으로만 처리하면 → $R_0$ variability와 recovery 해석이 residual error로 흡수됩니다

---

<!-- SLIDE_START: M2 | title: Protein/Antibody Distinctive PK -->
<!-- SECTION_CORE: SC-04 -->
## ▌ Card M2 — Protein/Antibody Distinctive PK

> **앞 카드에서 이 카드로**  
> M1에서 target이 turnover pool이라는 걸 정리했습니다. 그런데 그 pool에 들어가는 ligand 자체도 — 항체라면 — small molecule과 전혀 다른 ADME 관문을 먼저 통과해야 합니다.
>
> **거장의 시각**  
> mAb의 곡선을 "반감기 하나"로 설명하면, slow input, FcRn salvage, target-mediated sink가 모두 terminal slope 하나에 뭉뚱그려집니다. **네 개의 ADME 관문으로 나누면 어떤 데이터가 absorption, distribution, elimination, rescue를 가르치는지가 분리됩니다.**

단백질 약물과 mAb는 small molecule처럼 "잘 녹고 전신으로 퍼진 뒤 간이나 신장으로 빠지는" 물질이 아닙니다. 큰 분자량, 제한된 capillary permeability, 림프관 입력, proteolysis, 수용체 매개 흡수(receptor-mediated uptake; 수용체 결합 후 세포 내 유입), **FcRn salvage**(IgG를 분해에서 회수하는 기전) — 이것들이 ADME의 기본 문법입니다. [G&W pp.97–100; R&T pp.701–724]

### A. 형식적 정의

| 파라미터/범위 | 단위 | 의미 | 변화 원인 |
|---|---|---|---|
| $V_{ss}$ | L·kg⁻¹ | plasma/interstitial 중심의 제한 분포 | 분자 크기, vascular permeability |
| MW 역치 | g/mol | 림프관 경로 우세 전환 기준 | 분자량 증가 |
| $F$ | fraction | sc/im 생체이용률 | injection site, proteolysis, 림프관 통과 |
| $T_{max}$ | time | 느린 전신 유입의 척도 | absorption-rate limitation |
| FcRn | mechanism | IgG/mAb recycling salvage | FcRn binding, endosomal recycling |

mAb의 distinctive features를 네 개의 관문으로 묶으면 다음과 같습니다.

| 관문 | 의미 | 출처 |
|---|---|---|
| **Distribution** | $V_d$가 작고 plasma/interstitial space로 분포가 제한 | Table 21-6 [R&T pp.701–702] |
| **Absorption** | sc/im 후 큰 단백질은 주로 림프관으로 천천히 전신에 유입 | Table 21-13 [R&T p.718] |
| **Elimination** | 작은 단백질은 신장 처리가 핵심, 큰 mAb는 proteolysis/수용체 매개 경로가 중심 | [G&W pp.98–99; R&T pp.704–708] |
| **Rescue (FcRn)** | IgG/mAb를 acidic endosome에서 결합 후 recycling, lysosomal degradation을 회피 | Fig.21-5 [R&T p.709] |

> 💡 **느림은 단일 원인이 아닙니다.** mAb 곡선의 느림은 제한된 분포 + 림프관 입력 + proteolysis/RME + FcRn rescue가 합쳐진 결과입니다. 그래서 sc 투여 terminal slope를 곧바로 elimination 반감기로 읽으면 absorption-rate limitation을 놓칩니다. terminal phase를 해석하기 전, 위 네 관문 중 어느 쪽이 지배하는지 먼저 적어봅니다.

### B. 핵심 기전

**Distribution**: R&T Table 21-6은 단백질 약물의 $V_{ss}$가 대체로 **0.04–0.23 L·kg⁻¹** 범위라고 보여줍니다. large biologics가 body water 전체가 아니라 plasma/interstitial space에 제한된다는 뜻입니다. [R&T pp.701–702]

$$
\underbrace{V_{ss}}_{\text{SS 분포용적}}
\approx
\underbrace{0.04\text{--}0.23\ \mathrm{L\cdot kg^{-1}}}_{\text{제한 분포}}
$$

**G&W의 항체 사례 앵커**: cynomolgus monkey에 0.77–771 µmol·kg⁻¹ 범위로 다섯 차례 오름 용량을 투여한 실험용 항체 사례를 제시하며, **단순 central compartment 가정만으로 항체 배치를 설명하면 위험하다**고 경고합니다. 또한 정상·신장절제 rat에서 r-hSOD 실험을 통해 큰 단백질의 낮은 $V_d$와 renal clearance 손실을 보여줍니다. [G&W pp.99–100]

**Lymphatic absorption**: G&W는 sc 투여된 단백질/펩타이드의 흡수가 낮고 erratic하며 지연된다고 설명하고, 림프 흐름을 약 2 L/day로 제시합니다. R&T Table 21-13은 분자량 **15,000–20,000 g/mol을 넘는 분자**는 주로 림프관을 통해 전신에 들어간다고 정리합니다. [G&W p.97; R&T p.718]

$$
\underbrace{MW}_{\text{분자량}}
>
\underbrace{15{,}000\text{--}20{,}000\ \mathrm{g/mol}}_{\text{림프 경로 역치}}
\Rightarrow
\underbrace{\mathrm{lymphatic\ input}}_{\text{느린 전신 유입}}
$$

**방향성이지 외삽 공식이 아님**: R&T Fig.21-16은 양에서 0.246–19 kDa water-soluble 화합물의 분자량이 클수록 림프 회수율이 증가한다는 **방향성**을 보여줍니다. 이건 150 kDa mAb의 회수율을 직선으로 외삽해 구체적 퍼센트를 계산하는 근거가 아닙니다. [R&T p.720]

**Absorption-rate limitation**: **somatropin**(재조합 성장호르몬, 22 kDa)은 i.v. 반감기가 약 **2.1시간**으로 짧은데, sc 투여 후에는 plasma 농도가 훨씬 길게 지속됩니다. → terminal profile이 elimination이 아니라 **slow input**에 의해 rate-limited될 수 있다는 사례입니다. [R&T p.721]

**Renal disease**: **anakinra**(재조합 IL-1 수용체 길항제, 17,258 g/mol)는 신기능이 떨어지면 청소율도 같이 떨어져 노출이 증가합니다. 반면 full-size mAb나 매우 큰 단백질은 사구체 여과를 거의 받지 않아 신질환 영향이 일반적으로 작습니다. → "단백질이면 신장이 중요하다"가 아니라 **크기에 따라 갈린다**는 사례입니다. [R&T p.724]

### C. FcRn과 FcγR

FcRn은 내인성 IgG와 치료용 mAb의 긴 반감기를 설명하는 핵심 salvage 기전입니다. R&T는 mAb 반감기가 IgG에 가까운 **약 21일**인 경우가 많다고 설명하지만, 이건 모든 mAb의 고정된 숫자가 아닙니다. FcRn binding, target-mediated clearance, immunogenicity, dose level에 따라 apparent 반감기는 달라집니다. [R&T pp.708–710]

FcγR 매개 청소율도 무시할 수 없습니다. R&T는 **methotrexate**(MTX, 면역억제제)가 류마티스 관절염 환자에서 **adalimumab**(anti-TNFα IgG1 mAb)의 청소율을 **29–44% 감소**시킬 수 있다고 제시합니다. → FcγR은 변두리 디테일이 아니라, 특정 질환·병용약물 맥락에서는 **clearance covariate**가 될 수 있다는 사례입니다. [R&T p.706]

### D. TMDD에 왜 중요한가

mAb의 느린 흡수와 작은 $V_d$를 모르면 TMDD 곡선을 잘못 읽습니다. 왜냐하면 sc 투여에서는 **Phase A의 rapid binding signature가 absorption phase와 confound될 수 있기** 때문입니다. 또한 FcRn rescue가 있는 mAb에서는 "terminal slope = simple elimination 반감기"라는 해석이 위험해집니다.

### E. 가정과 한계

- "mAb 반감기 ≈ 21일"은 유용한 사전 정보일 수 있지만, 분자별 FcRn binding 증거와 target-mediated clearance를 확인해야 합니다. [R&T p.708]

$$
\underbrace{t_{1/2,\mathrm{mAb}}}_{\text{mAb 겉보기 t½}}
\approx
\underbrace{21\ \mathrm{days}}_{\text{IgG식 prior}}
$$

- ADA(anti-drug antibody)/immunogenicity는 PK를 변화시킬 수 있으므로, 설명되지 않는 청소율 증가가 보이면 target biology뿐 아니라 ADA도 점검해야 합니다. [R&T p.725]
- sc mAb의 $T_{max}$는 보통 며칠 단위입니다. Table 21-15의 예시: **adalimumab** $F=0.64$, $T_{max}=5.5$ days, $t_{1/2}=30$ days; **omalizumab**(anti-IgE) $F=0.62$, $T_{max}=7.5$ days, $t_{1/2}=26$ days; **efalizumab**(anti-CD11a) $F=0.50$, $t_{1/2}=17$ days. → 모두 sc 입력이 느려서 며칠짜리 $T_{max}$를 만드는 사례입니다. [R&T p.723]

$$
\underbrace{T_{max}}_{\text{Tmax}}
=
\underbrace{5.5\text{--}7.5\ \mathrm{days}}_{\text{느린 sc 입력}}
,\qquad
\underbrace{F}_{\text{생체이용률}}
\approx
\underbrace{0.50\text{--}0.64}_{\text{예시 범위}}
$$

### G. Zettelkasten Atom

```text
Antibody PK = restricted distribution + lymphatic input + proteolytic/receptor-mediated elimination + FcRn salvage.
Do not read mAb half-life as a single molecule property when TMDD or slow input is active.
```

> 📖 **Rowland & Tozer 5e, p.709, Fig.21-5**: FcRn salvage는 "긴 반감기"의 라벨이 아니라 **recycling 기전**입니다. 이 그림은 IgG/mAb가 acidic endosome에서 FcRn에 결합한 뒤 어떻게 분해를 피하고 다시 순환으로 돌아오는지 단계별로 보여줍니다.

**M2 recap**: mAb의 느림은 반감기 숫자 하나가 아니라, **tissue access + lymphatic transit + FcRn recycling + target/수용체 매개 sink**가 합쳐진 결과입니다.

> **M2 체화 핵심**  
> ① sc/im mAb 곡선이 길게 이어질 때 → 림프관 입력과 absorption-rate limitation이 결정합니다  
> ② mAb 반감기를 고정값처럼 해석할 때 → FcRn, target-mediated clearance, ADA가 다른 해석을 지배합니다  
> ⚡ "terminal slope = elimination 반감기"로 단정 → slow input이나 FcRn/target 효과를 놓쳐 TMDD 곡선 판독 실패

---

<!-- SLIDE_START: M3 | title: TMDD 4-Phase Concentration-Time Profile -->
<!-- SECTION_CORE: SC-05 -->
## ▌ Card M3 — TMDD 4-Phase Concentration-Time Profile

> **앞 카드에서 이 카드로**  
> M2의 ADME 관문을 통과한 곡선이라도, target 결합이 개입하면 곡선은 더 이상 시간표가 아니라 **농도 영역의 지도**가 됩니다.
>
> **거장의 시각**  
> Phase A–D를 시간 순서로 외우면 저용량 곡선이 가르치는 saturation 경계를 놓칩니다. **농도 위계로 읽으면 "보이는 phase가 곧 식별 가능한 mechanism"**이라는 판단 기준이 생깁니다.

TMDD 곡선은 "비선형 곡선"이 아닙니다. **Ligand 농도가 target 농도, $K_d$, $K_m$, saturation 경계를 차례로 지나갈 때 dominant clearance route가 바뀌는 기록**입니다. 그래서 Phase A–D는 단순한 시간 구간이 아니라 **농도 위계(concentration hierarchy)**입니다. [G&W pp.604–610; R&T pp.711–712]

### A. 형식적 정의

| 파라미터/기준 | 단위 | 의미 | 변화 원인 |
|---|---|---|---|
| $C_L$ | concentration | ligand 농도 | dose, distribution, CL, binding |
| $R_0$ | concentration/amount | baseline target 수준 | turnover, target burden |
| $K_m$ | concentration | apparent saturation 경계 | binding + complex sink |
| $K_d$ | concentration | binding/dissociation 경계 | $k_{off}/k_{on}$ |
| Phase A–D | regime | dominant clearance route 변화 | 농도가 역치를 넘으면서 |

**PK27 용량 앵커**: PK27의 full-TMDD 실험은 단클론 항체를 **1.5, 5, 15, 45 mg·kg⁻¹** 네 용량으로 급속 정맥 주사한 데이터입니다. 용량별 층화 곡선 판독이 장식이 아니라 핵심인 이유가 여기에 있습니다. [G&W pp.602–603]

PK27과 R&T는 특징적 TMDD 곡선을 네 phase로 설명합니다. [G&W p.610; R&T p.712]

| 단계 | 지배 과정 | 해석 |
|---|---|---|
| **A** | 빠른 2차 결합 | ligand와 target이 빠르게 평형 |
| **B** | 느린 1차 배치 | target 경로 포화, 비특이적 경로가 지배 |
| **C** | 혼합차수 배치 | target 부분 포화, 선형과 target-mediated 경로 공존 |
| **D** | $k_{off}$와 $k_{e(RL)}$ 주도의 말기상 | 매우 낮은 ligand, target-specific 제거가 가시화 |

> 💡 **Phase는 농도 서명입니다.** A–D는 시간 라벨이 아니라 ligand 농도가 $R_0$, $K_m$, $K_d$ 경계를 지나는 방식의 기록입니다. 고용량 곡선만 잘 맞으면 target-mediated 경로가 포화되어 **선형처럼 보일 수 있습니다.** Full TMDD/MM을 고르기 전에, 용량별 층화 곡선에서 실제로 관찰된 phase가 무엇인지 먼저 표시합니다.

### B. 시간 순서가 아닌 농도 위계

초심자는 Phase A→B→C→D를 시간 순서로 읽습니다. 숙련된 모델러는 같은 곡선을 ligand 농도가 $R_0$, $K_m$, $K_d$를 차례로 지나는 농도 위계로 읽습니다. PK27에서는 $R_0\approx 12\ \mathrm{mg\cdot L^{-1}}$, $K_m\approx 0.03\ \mathrm{mg\cdot L^{-1}}$이며, $K_d$는 $k_{off}/k_{on}$으로 정의됩니다. **이 역치들 때문에 저용량 곡선이 고용량 곡선에서는 보이지 않는 기울기를 드러냅니다.** [G&W pp.603–610]

$$
\underbrace{C_L}_{\text{ligand 농도}}
\quad\text{통과}\quad
\overbrace{\underbrace{R_0}_{\text{target 기준}},\ \underbrace{K_m}_{\text{겉보기 경계}},\ \underbrace{K_d}_{\text{결합 경계}}}^{\text{phase 전환점}}
$$

### C. 곡선이 가르치는 것 (그리고 가르치지 않는 것)

- 고용량 데이터만 관찰했다면 target-mediated 경로는 포화 상태로 들어가서 **선형처럼 보입니다.**
- assay 민감도가 낮아 저용량 데이터가 빠지면 Phase A/D를 못 봅니다.
- sc 흡수가 느리면 초기의 rapid binding이 input kinetics에 가려집니다.
- target/complex 데이터가 없으면 ligand-only 적합이 좋아 보여도 $k_{on}$, $k_{off}$, $k_{e(RL)}$의 정밀도는 낮은 채로 남습니다. [G&W pp.603–609]

### D. 실무 판독 규칙

TMDD plot은 **용량별로 층화해서** 점검합니다. 고용량 곡선은 잘 맞지만 저용량 잔차가 체계적으로 편향된다면, 모델은 phantom linearity를 가지고 있습니다 — 중심 곡선에서는 겉보기에 성공이지만 저농도 외삽에서는 편향이 숨어 있는 상태입니다. (이건 PK27 MM 실패에서 나온 진단적 해석이지 교과서가 직접 NONMEM rule로 명시한 건 아닙니다.) [G&W p.609]

### E. 한계

네 개 phase는 풍부하고 고품질의 다용량 IV 데이터셋에서 가장 뚜렷합니다. 임상 현장의 희박 샘플링, sc 흡수, total vs free assay의 모호함, 막결합 target(membrane-bound target)은 phase 경계를 흐리게 만듭니다. [G&W pp.604–605]

### G. Zettelkasten Atom

```text
TMDD phases are concentration-regime signatures.
Do not choose MM or Full TMDD before asking which phases the dataset actually observes.
```

> 📖 **Rowland & Tozer 5e, p.712, Fig.21-9 (+ Gabrielsson p.610, Fig.27.7)**: 이 그림은 Phase A–D를 시간 구간으로 외우는 흔한 실수를 막아 줍니다. 각 phase는 target saturation과 $K_m$/$K_d$ 경계에 묶인 **농도 영역 서명**으로 읽어야 합니다.

$$
\overbrace{\mathrm{Phase\ A\to B\to C\to D}}^{\text{농도 영역 서명}}
\sim
\underbrace{C_L}_{\text{ligand}}
\text{ relative to }
\underbrace{R_0,K_m,K_d}_{\text{포화/결합 기준}}
$$

**M3 recap**: Phase A–D는 그림 설명이 아니라 **model-selection checklist**입니다. 보이는 phase가 곧 식별 가능한 mechanism입니다.

> **M3 체화 핵심**  
> ① TMDD 곡선의 phase를 읽을 때 → ligand 농도와 $R_0/K_m/K_d$ 위계가 결정합니다  
> ② 고용량 적합만 평가할 때 → 포화된 target 경로가 phantom linearity를 만듭니다  
> ⚡ Phase A–D를 시간 구간으로 암기 → 저용량 외삽에서 model-selection 근거를 잃습니다

---

<!-- SLIDE_START: M4 | title: Full TMDD Model -->
<!-- SECTION_CORE: SC-06 -->
## ▌ Card M4 — Full TMDD Model [⚡ Apex Concept]

> **앞 카드에서 이 카드로**  
> Phase가 농도 영역의 서명이라면, 그 서명을 만들어내는 ligand·target·complex·sink 항을 ODE 안에서 따로따로 분리해야 합니다.
>
> **거장의 시각**  
> 💢 **흔한 오해**: Full TMDD는 MM에 target·complex라는 생물학적 이름표를 붙인 복잡한 saturable clearance 모델일 뿐이다.  
> ✅ **실제**: Full TMDD는 ligand disposition, target turnover, binding, complex sink를 서로 다른 state와 ODE 항으로 분리합니다.  
> 🎯 **체화할 단 하나의 직관**: **관찰 species가 없는 mechanism은 추정값이 아니라 가정으로 남습니다.**

### [⚡ Apex Concept] Big Idea

Full TMDD는 ligand disposition, target turnover, ligand-target binding, complex loss를 하나의 mechanistic system으로 묶습니다. 하나의 ODE system(시간에 따른 상태변화 방정식 묶음)이 PK와 target biology를 동시에 추적합니다. PK27은 이를 "8-parameter full TMDD model"이라 부르지만, 이는 $V_c=0.05\ \mathrm{L\cdot kg^{-1}}$를 fixed한 상태에서 Table 27.2가 보고하는 8개의 estimated parameter를 말합니다. fixed $V_c$까지 structural quantity로 세면 ligand central, ligand tissue, target, complex의 **4 state와 9 structural quantities**가 존재합니다. [G&W pp.603, 608–609]

### A. 형식적 구조

| 파라미터 | 단위 | 의미 | 변화 원인 |
|---|---|---|---|
| $L_c$ | amount/conc | central ligand state | dose, CL, distribution, binding |
| $L_t$ | amount/conc | tissue/peripheral ligand state | 구획 간 분포 |
| $R$ | target scale | free target/수용체 | $k_{in}$, $k_{out}$, binding 소모 |
| $RL$ | complex scale | ligand-target complex | $k_{on}$, $k_{off}$, $k_{e(RL)}$ |
| $V_c$ | L·kg⁻¹ | PK27에서 fixed central volume | 구조 가정, 민감도 분석 대상 |

Full TMDD의 상태변수는 다음 4개입니다. [G&W pp.604–607; R&T p.711]

| 상태변수 | 의미 |
|---|---|
| $L_c$ | central 구획의 ligand |
| $L_t$ | tissue/peripheral 구획의 ligand |
| $R$ | free target/수용체 |
| $RL$ | ligand-target complex |

$$
\underbrace{\mathbf{x}(t)}_{\text{TMDD 상태벡터}}
=
\left(
\underbrace{L_c}_{\text{central ligand}},
\underbrace{L_t}_{\text{tissue ligand}},
\underbrace{R}_{\text{free target}},
\underbrace{RL}_{\text{LT complex}}
\right)
$$

PK27 Table 27.2의 8개 보고 파라미터는 $Cl$, $k_{on}$, $k_{off}$, $V_t$, $Cl_d$, $k_{out}$, $R_0$, $k_{e(RL)}$입니다. $V_c$는 $0.05\ \mathrm{L\cdot kg^{-1}}$로 fixed되었습니다. [G&W pp.608–609]

$$
\overbrace{\{Cl,k_{on},k_{off},V_t,Cl_d,k_{out},R_0,k_{e(RL)}\}}^{\text{PK27 8개 추정값}}
\quad ; \quad
\underbrace{V_c}_{\text{central volume}}
=
\underbrace{0.05\ \mathrm{L\cdot kg^{-1}}}_{\text{고정 구조가정}}
$$

> 💡 **Topology가 먼저입니다.** Full TMDD의 핵심은 파라미터 개수가 아니라 ligand·free target·complex·sink의 **연결 구조**입니다. 그리고 $k_{in}$(target 합성)과 $k_{on}$(ligand-target 결합)을 섞으면 안 됩니다 — process 자체가 다른 양입니다. 식별성의 분업은 이렇습니다: **ligand는 disposition을, target은 recovery/saturation을, complex는 sink를 가르칩니다.**

### B. 기전 방정식

개념적 구조:

```text
Ligand central/tissue distribution:
  nonspecific Cl(L), Cld, Vc, Vt

Target turnover:
  dR/dt = kin - kout·R - kon·L·R + koff·RL

Complex dynamics:
  dRL/dt = kon·L·R - koff·RL - ke(RL)·RL
```

$$
\begin{aligned}
\overbrace{\frac{dR}{dt}}^{\text{free target 변화}}
&=
\underbrace{k_{in}}_{\text{target 생성}}
-\underbrace{k_{out}R}_{\text{target 자연 소실}}
-\underbrace{k_{on}LR}_{\text{LT 결합}}
+\underbrace{k_{off}RL}_{\text{complex 해리}} \\
\overbrace{\frac{dRL}{dt}}^{\text{complex 변화율}}
&=
\underbrace{k_{on}LR}_{\text{complex 형성}}
-\underbrace{k_{off}RL}_{\text{해리}}
-\underbrace{k_{e(RL)}RL}_{\text{complex sink}}
\end{aligned}
$$

결합 속도항은 $k_{on}\cdot L\cdot R$이지 $k_{in}\cdot L\cdot R$이 아닙니다. $k_{in}$은 **target 합성** 쪽이고, $k_{on}$은 ligand-target 결합의 **2차 on-rate**입니다. 표기 차이가 아니라 **turnover process와 binding process를 분리**하는 핵심입니다. [G&W p.604; G&W pp.606–607]

$$
\underbrace{\mathrm{BIND}}_{\text{complex 형성속도}}
=
\underbrace{k_{on}}_{\text{2차 on-rate}}
\cdot
\underbrace{L}_{\text{ligand}}
\cdot
\underbrace{R}_{\text{free target}}
\quad \ne \quad
\underbrace{k_{in}\cdot L\cdot R}_{\text{process 혼합}}
$$

### C. 식별가능성: 어떤 데이터가 어떤 항을 가르치는가

PK27은 세 데이터셋을 사용합니다 — **I = ligand 단독, II = ligand + target, III = ligand + target + complex.** target과 complex 시간경과 데이터가 추가될수록 $k_{on}$, $k_{off}$, $k_{e(RL)}$의 정밀도가 좋아집니다. Table 27.2에서 dataset I→II→III에 걸쳐 $k_{on}$ CV%는 **17→2→1**, $k_{off}$는 **27→13→3**, $k_{e(RL)}$는 **27→23→2**로 개선됩니다. [G&W pp.603, 608–609]

$$
\begin{aligned}
\underbrace{CV\%(k_{on})}_{\text{kon 정밀도}} &: \underbrace{17\to2\to1}_{\text{자료 풍부도}},\\
\underbrace{CV\%(k_{off})}_{\text{koff 정밀도}} &: \underbrace{27\to13\to3}_{\text{target/complex 추가}},\\
\underbrace{CV\%(k_{e(RL)})}_{\text{sink 정밀도}} &: \underbrace{27\to23\to2}_{\text{complex 측정 효과}}
\end{aligned}
$$

한 줄로 정리하면 — **ligand 데이터는 nonspecific disposition과 가시적 phase 구조를 가르치고, target 데이터는 recovery와 saturation 경계를 가르치고, complex 데이터는 sink 거동을 가르칩니다.** 자료 풍부도는 장식이 아닙니다. **어떤 ODE 항이 추정 가능해지는지를 결정합니다.**

### D. 그럴듯한 오해: 적합 품질 ≠ 기전 타당성

**오해**: Full TMDD와 MM은 둘 다 saturable clearance를 표현하니, 고용량 적합이 좋으면 같은 모델로 봐도 된다.  
**왜 그럴싸한가**: 가장 높은 세 ligand 곡선은 reduced model에서도 꽤 잘 맞아 보입니다.  
**나비효과**: 고용량 적합 신뢰 → $K_m$ 123배 과대예측 놓침 → [임상] trough·target occupancy·subgroup 저농도 노출 판단 실패 → [모델링/규제] 저용량 잔차와 외삽 근거 부족으로 sensitivity analysis 및 재분석 요구 위험 증가. [G&W p.609]

압축 진술: reduced model은 가장 높은 세 ligand 곡선은 상당히 잘 맞추지만 **가장 낮은 곡선에서는 실패**합니다. PK27에서 MM 모델은 $K_m=3.7$을 산출했고 Full TMDD는 $K_m=0.03$을 제시했습니다. **약 123배 과대추정**입니다. 이 편향은 trough 예측, target occupancy 추정, subgroup 외삽으로 전파됩니다. 정량 영향은 일반적 주장이 아니라 약물·환자 집단별 sensitivity analysis로 평가해야 합니다. [G&W p.609]

$$
\underbrace{\frac{K_{m,\mathrm{MM}}}{K_{m,\mathrm{TMDD}}}}_{\text{MM bias}}
=
\underbrace{\frac{3.7}{0.03}}_{\text{PK27 비교}}
\approx
\underbrace{123}_{\text{123배 과대}}
$$

이 오해의 mechanism을 3분 구조로 분해하면 이렇습니다.

**왜 틀렸는가**: MM 근사는 drug $\gg$ target 조건($L \gg R$ 또는 $L \gg K_d$에서 binding이 빠르게 quasi-equilibrium에 도달하고 target 경로가 지속 포화)에서만 Full TMDD로부터 구조적으로 유도됩니다. Full TMDD는 binding($k_{on}\cdot L\cdot R$), 약물-target 복합체 형성($RL$), complex internalization($k_{e(RL)}$), target turnover($k_{in}/k_{out}$)를 4-state ODE로 명시적으로 인코딩합니다. **근사 조건이 깨지는 농도 영역** — ligand 농도가 $K_d$ 또는 $K_m$ 부근(target saturation 전환점)으로 떨어지는 구간과 매우 낮은 농도의 linear regime — 에서 MM 근사는 PK 거동을 구조적으로 잘못 예측합니다. PK27의 $K_m$ 0.03 vs 3.7이 바로 이 경계 위반의 정량적 흔적입니다. [G&W p.609]

**실무에서 어떻게 드러나는가**: 저용량 Phase 1 데이터에서 MM 근사 모델이 OFV/VPC 기준으로 잘 맞은 것처럼 보일 수 있습니다. 그런데 중간 용량 범위의 비선형 전환점(Phase B↔C↔D 전이)을 mechanistic하게 예측하지 못해 Phase 2 dose selection이 어긋납니다. 또는 고용량 데이터셋만으로 적합된 MM이 sub-population(저체중, 고 target burden, 초기 dose interval) 외삽에서 trough 노출을 체계적으로 잘못 예측해서, 후속 임상 의사결정의 출발점이 흔들립니다.

### E. NONMEM 스타일 구현 노트

다음은 교과서 control stream이 아니라 **PK27/R&T ODE 구조를 NONMEM 스타일로 교육 목적 번역**한 골격입니다.

```text
; conceptual only
CLIG = A(1)/VC
CTIS = A(2)/VT
R    = A(3)/VR_OR_SCALE
RL   = A(4)/VC

BIND = KON * CLIG * R * VC     ; amount/time 스케일에는 volume conversion 필요
DISS = KOFF * A(4)
SINK = KERL * A(4)

DADT(1) = INPUT - CL*CLIG - Q*(CLIG-CTIS) - BIND + DISS
DADT(2) =  Q*(CLIG-CTIS)
DADT(3) =  KIN - KOUT*A(3) - BIND + DISS
DADT(4) =  BIND - DISS - SINK
```

**Trench-level tip**: `BIND`는 `DADT`에 들어가기 전에 amount/time 단위를 가져야 합니다. 필요한 amount scale conversion 없이 $k_{on}\cdot C_L\cdot R$로 그대로 쓰면, 모델이 조용히 mass balance를 위반합니다.

### F. 가정과 경계조건

- $V_c=0.05\ \mathrm{L\cdot kg^{-1}}$ 고정은 PK27의 고해상도 rapid-IV/고분자량 근사값입니다. 임상 보편 상수가 아닙니다. [G&W p.608]
- free target, total target, complex assay는 모델의 상태변수와 정렬되어야 합니다. assay가 partial total target을 보고하는데 모델이 free $R$을 가정하면 $R_0$와 $k_{out}$의 해석이 달라집니다.
- Full TMDD는 ligand 데이터만 희박하게 있으면 과모수화(over-parameterization)됩니다. **PK26 Efalizumab**(anti-CD11a IgG1)에서는 target/complex 및 $k_{on}/k_{off}/K_d$ 정보가 없어 full TMDD 적합에 실패했습니다. → 자료 풍부도가 충분치 않으면 Full TMDD는 추정 가능한 모델이 아닙니다. [G&W p.601]

### H. Zettelkasten Atom

```text
Full TMDD = 4-state mechanistic system:
ligand central + ligand tissue + free target + complex.
PK27 reports 8 estimated parameters because Vc is fixed at 0.05 L·kg⁻¹.
```

> 📖 **Rowland & Tozer 5e, p.711, Fig.21-8 (+ Gabrielsson p.604, Fig.27.2)**: Full TMDD는 파라미터 개수 문제이기 전에 **topology 문제**입니다. 이 그림은 ligand·target·complex·binding·dissociation·sink가 어떻게 연결되는지 보여줍니다.

$$
\underbrace{k_{in}}_{\text{target 입력}}
\perp
\underbrace{k_{on}}_{\text{kon}},
\qquad
\underbrace{k_{off}}_{\text{koff}}
\perp
\underbrace{k_{e(RL)}}_{\text{complex 제거}}
$$

**M4 recap**: Full TMDD의 핵심은 "파라미터가 많다"가 아닙니다. **ligand 곡선 안에 숨어 있는 target turnover, binding, complex sink를 따로따로 분리하는 것**입니다.

> **M4 체화 핵심**  
> ① target·complex 데이터가 같이 있을 때 → $k_{on}$, $k_{off}$, $k_{e(RL)}$ 식별성이 개선됩니다  
> ② ligand-only 적합이 좋아 보일 때 → target turnover와 complex sink는 "biologically learned"가 아닐 수 있습니다  
> ⚡ 적합 품질 = 기전 타당성으로 단정 → 저용량 외삽·occupancy·subgroup 예측에서 구조적 실패

---

<!-- SLIDE_START: M5 | title: Michaelis-Menten Approximation Boundary -->
<!-- SECTION_CORE: SC-07 -->
## ▌ Card M5 — Michaelis-Menten Approximation Boundary

> **앞 카드에서 이 카드로**  
> M4에서 Full TMDD의 topology가 명확해졌습니다. 이제 결정해야 합니다 — **어떤 조건에서 이 topology를 MM 항 하나로 접어도 되는가?**
>
> **거장의 시각**  
> MM을 "단순하고 안전한 대체 모델"로 읽으면 reduced model이 허용되는 농도·occupancy 경계를 놓칩니다. MM을 **Full TMDD의 접힌 형태**로 보면, 관찰된 포화 영역 안에서만 방어 가능한 내삽 도구라는 위치가 분명해집니다.

Michaelis-Menten 근사는 Full TMDD의 target/complex 하부 시스템을 $V_{max}$와 $K_m$로 줄이는 것입니다. $R$과 $RL$을 직접 추적하지 않고 target-mediated 경로를 하나의 saturable clearance 항으로 접습니다. 진짜 문제는 적합이 아니라 — **어느 농도/occupancy 영역에서 이 접기가 구조적으로 허용되는가**입니다. [G&W p.609; R&T p.712]

### A. 형식적 정의

| 파라미터 | 단위 | 의미 | 변화 원인 |
|---|---|---|---|
| $Cl_{MM}$ | clearance | saturable target-mediated CL | $C$, $V_{max}$, $K_m$ |
| $V_{max}$ | amount/time | 최대 target-mediated 처리능 | target capacity, internalization capacity |
| $K_m$ | concentration | 겉보기 half-saturation 경계 | $k_{off}$, $k_{e(RL)}$, $k_{on}$ |
| $K_d$ | concentration | binding 해리상수 | $k_{off}/k_{on}$ |
| Occupancy | % | target 결합 비율 | concentration vs binding/saturation 경계 |

Reduced model은 target-mediated 경로를 다음으로 압축합니다. **압축은 단순화이지 biology가 사라졌다는 뜻이 아닙니다.**

$$
\overbrace{Cl_{MM}}^{\text{포화 TMDD CL}}
=
\frac{\underbrace{V_{max}}_{\text{최대 처리능}}}{\underbrace{K_m}_{\text{반포화 경계}}+\underbrace{C}_{\text{ligand 농도}}}
$$

Full TMDD에서 관련 상수는:

$$
\overbrace{K_d}^{\text{결합 해리상수}}
=
\frac{\underbrace{k_{off}}_{\text{해리 속도}}}{\underbrace{k_{on}}_{\text{결합 속도}}},
\qquad
\overbrace{K_m}^{\text{겉보기 동역학상수}}
=
\frac{\overbrace{k_{off}+k_{e(RL)}}^{\text{해리+sink}}}{\underbrace{k_{on}}_{\text{결합 속도}}}
$$

$K_d$는 binding affinity에 가까운 **thermodynamic 해리상수**이고, $K_m$은 complex loss($k_{e(RL)}$)까지 포함한 **apparent kinetic 상수**입니다. [G&W pp.603–609; R&T pp.711–712]

> 💡 **MM은 접힌 모델입니다.** $V_{max}/K_m$은 target biology를 제거한 게 아니라 관찰 가능한 saturable 항으로 압축한 것입니다. 그래서 $K_m$은 $K_d$가 아닙니다 — $K_m$에는 complex sink $k_{e(RL)}$가 들어갑니다. 관찰된 saturation/occupancy 영역 밖에서는 고용량 적합이 좋아도 MM 외삽을 정당화할 수 없습니다.

### B. MM이 통할 수 있는 조건

MM이 적절할 수 있는 상황은:

- ligand 농도가 target 농도를 크게 초과할 때
- target occupancy가 거의 완전 포화일 때
- 관찰된 용량 범위가 제한적일 때
- 목적이 저농도 외삽이 아니라 **관찰 프로파일 내 내삽**일 때 [G&W p.609; R&T p.712]

**PK26 Efalizumab**(anti-CD11a IgG1, 건선 치료제)이 유용한 reduced-model 앵커입니다. 2구획 모델에 parallel linear/MM 제거가 사용되었는데, target/complex 및 $k_{on}/k_{off}/K_d$ 정보가 없어 full TMDD 적합에 실패했기 때문입니다. 보고된 추정값: $V_t=0.061$, $V_{max}=0.039$, $K_m=0.161$, $CL_d=0.031$, $CL_L=0.007$. **PK26 dose anchor**: 이 reduced model은 single-dose i.v. bolus 데이터의 5개 정맥주사 시간경과에 적합되었습니다. 따라서 이 사례는 **제한된 데이터의 reduced-model 앵커**로 읽어야지, MM이 보편적으로 mechanistic이라는 증거로 읽으면 안 됩니다. [G&W pp.599–601]

$$
\overbrace{\{V_t,V_{max},K_m,CL_d,CL_L\}}^{\text{PK26 reduced set}}
=
\underbrace{\{0.061,0.039,0.161,0.031,0.007\}}_{\text{보고 추정값}}
$$

### C. MM이 무너지는 지점

PK27에서 MM은 가장 높은 세 농도 곡선은 비교적 잘 적합했지만, **가장 낮은 농도 곡선에서는 심각한 체계적 편차**를 보였습니다. 추정된 $K_m=3.7$은 Full TMDD의 $0.03$에 비해 극적으로 과대추정되었습니다. [G&W p.609]

임상적 교훈은 "MM을 쓰지 말라"가 아닙니다. 교훈은 더 좁고 실용적입니다 — **target saturation이 실증된 농도/occupancy 영역 밖에서는 MM을 쓰지 마세요.**

### D. Occupancy 검증

대략 **90–95% 이상의 occupancy**가 유지되는 영역에서는 단순화가 허용될 수 있습니다. occupancy가 $K_d$ 또는 biomarker 역가 이하로 떨어지면 MM이 충분하지 않습니다. [G&W p.609]

$$
\underbrace{\mathrm{Occupancy}}_{\text{target 결합비율}}
\gtrsim
\underbrace{90\text{--}95\%}_{\text{고포화 영역}}
$$

실무 준칙: TMDD 가능성이 있는 mAb에 MM을 사용하는 리포트라면, 관찰된 농도 범위, target 농도 범위, 투여 간격 동안의 **최소 예측 target occupancy**를 명시해야 합니다. (이건 소스 경계의 구현 해석이지 규제기관이 직접 인용한 요건이 아닙니다.)

### E. 한계

- MM은 $R_0$, $k_{out}$, $k_{on}$, $k_{off}$, $k_{e(RL)}$의 명시적 해석을 잃습니다.
- 고용량이나 중심 곡선에 가중치가 쏠리면 저농도 편향이 숨겨집니다.
- 추가 가정 없이는 target recovery나 complex sink 질문에 답할 수 없습니다.
- QSS/QE 근사는 관련 개념이지만 이 세션의 범위 밖입니다(후속 modeling 세션 주제).

### G. Zettelkasten Atom

```text
MM approximation is acceptable only inside a demonstrated saturation/occupancy domain.
PK27 shows why good high-dose fit can coexist with low-dose structural bias.
```

> 📖 **Gabrielsson & Weiner 5e, p.609, Fig.27.6**: 이 그림은 무조건적 MM 외삽에 대한 **critical blow**입니다. 고용량 적합은 괜찮아 보여도, 가장 낮은 농도 곡선에서는 체계적 편차가 드러나고 $K_m$이 과대예측됩니다. 이 그림을 보지 않으면 학습자가 "적합 품질 = 기전 타당성"으로 단정하기 쉽습니다.

**M5 recap**: MM은 빠른 실무 도구일 수 있지만, **"적합이 잘 됨"과 "target biology를 올바르게 외삽함"은 같은 말이 아닙니다.**

> **M5 체화 핵심**  
> ① 관찰된 포화 영역 안에서 내삽할 때 → MM 근사가 실무적으로 방어 가능합니다  
> ② 저농도 trough·recovery·occupancy 외삽을 할 때 → Full TMDD 또는 추가 데이터가 지배합니다  
> ⚡ 고용량 적합 좋으니 MM이면 충분 → PK27처럼 $K_m$ 과대예측과 저용량 구조적 편향 발생

---

<!-- SLIDE_START: §5 | title: Confusion Pair Dissection -->
<!-- SECTION_CORE: SC-08 -->
# §5 Confusion Pair Dissection (자주 혼동되는 개념 쌍)

## ▌ Pair 1 — $k_{in}$ vs $k_{out}$

| 비교 기준 | $k_{in}$ | $k_{out}$ |
|---|---|---|
| 단위 | mass/time | time⁻¹ |
| 수식 내 위치 | $A_0=k_{in}/k_{out}$의 분자 | $A_0=k_{in}/k_{out}$의 분모, $t_t=1/k_{out}$의 분모 |
| 변화 원인 | 합성·입력 증가/감소 | catabolism·degradation 속도 변화 |
| 혼동 시 임상 결과 | level만 보고 시간 척도 변화로 오해 | level과 회복 시간 변화 모두 놓침 |

| 흔한 혼동 | 교정 |
|---|---|
| $k_{in}$과 $k_{out}$을 둘 다 그냥 "rate"로 기억합니다. | $k_{in}$은 mass/time인 input이고, $k_{out}$은 time⁻¹인 분획 소실입니다. |
| $k_{in}$ 증가와 $k_{out}$ 감소가 둘 다 농도를 높이니까 같다고 생각합니다. | $k_{in}$ 변화는 level만, $k_{out}$ 변화는 **level과 time scale을 함께** 바꿉니다. [G&W p.97] |

$$
\underbrace{k_{in}}_{\text{mass/time 입력}}
\quad\ne\quad
\underbrace{k_{out}}_{\text{시간}^{-1}\text{분획 소실}},
\qquad
\underbrace{A_0}_{\text{level}}
=
\frac{\underbrace{k_{in}}_{\text{level 상승}}}{\underbrace{k_{out}}_{\text{level↓/시간↓}}}
$$

**Locked sentence**: $k_{in}$은 수도꼭지, $k_{out}$은 배수구입니다. **수위만 보지 말고 새 수위에 도달하는 시간까지 같이 보세요.**

---

## ▌ Pair 2 — Full TMDD vs MM 근사 ▶ **Critical Blow**

| 비교 기준 | Full TMDD | MM 근사 |
|---|---|---|
| 차원 | ligand·target·complex state를 가진 ODE system | 하나의 saturable clearance 항 |
| 수식 내 위치 | $k_{on}LR$, $k_{off}RL$, $k_{e(RL)}RL$, $k_{in}/k_{out}$로 분리 | $Cl_{MM}=V_{max}/(K_m+C)$로 압축 |
| 변화 원인 | binding, target turnover, complex sink, nonspecific CL | 관찰 포화 범위와 apparent $V_{max}/K_m$ |
| 혼동 시 임상 결과 | data-rich mechanism을 식별 가능 | 저용량 trough·occupancy·subgroup 외삽에서 구조적 편향 |

| 흔한 혼동 | 교정 |
|---|---|
| Full TMDD는 복잡하고 MM은 단순한 대체 모델이다. | MM은 Full TMDD의 target/complex 하부 시스템의 reduction입니다. |
| 고용량 적합이 좋으면 MM이 충분하다. | PK27에서 고용량 곡선 적합이 좋아도 저용량 곡선에서 체계적 편차와 $K_m$ 123배 편향이 발생했습니다. [G&W p.609] |
| target/complex assay는 있으면 좋은 부가자료다. | target/complex 데이터는 $k_{on}$, $k_{off}$, $k_{e(RL)}$의 정밀도를 결정하는 **식별 자료**입니다. [G&W p.609] |

**Locked sentence**: MM은 "작은 TMDD"가 아니라 **"target biology를 $V_{max}/K_m$으로 접은 모델"**입니다. **접어도 되는지는 occupancy 영역이 결정합니다.**

**⚡ 기억 고리 — 완전 지도 vs 단순화 지도**:  
Full TMDD는 binding on/off, complex internalization, target 생성·분해를 모두 명시한 **완전 지도**입니다. MM 근사는 특정 농도 영역($L \gg R$ 또는 $L \gg K_d$의 quasi-equilibrium)에서 이 복잡성을 **하나의 포화곡선으로 압축한 단순화 지도**입니다. 단순화 지도는 그려진 스케일을 벗어나면 틀린 경로를 안내합니다 — drug 농도가 $K_d$ 또는 $K_m$ 부근으로 떨어지면 MM 모델은 TMDD 거동을 재현할 수 없습니다. PK27의 $K_m$ 0.03 → 3.7 과대예측이 바로 이 "지도 밖 영역"의 정량적 흔적입니다.

> **▶ Critical Blow**: 이 혼동을 안고 first-in-human 저용량 외삽이나 sub-population 외삽으로 임상 의사결정을 강행하면 세 경로의 실패가 발생합니다 — **(i) 저농도 trough 과대평가로 sub-therapeutic 노출 환자군 누락, (ii) dosing interval 동안 target occupancy가 적합 범위 밖으로 떨어져도 검출되지 않음, (iii) sub-population 외삽이 실증된 saturation 영역 밖에서 이루어짐.** PK27의 $K_m$ 0.03 → 3.7이 보여주듯, 정량 영향은 약물·환자 집단별 sensitivity analysis로 평가되어야 합니다. [G&W p.609]

---

## ▌ Pair 3 — TMDD에서 $K_d$ vs $K_m$

| 비교 기준 | $K_d$ | $K_m$ |
|---|---|---|
| 단위 | concentration | concentration |
| 수식 내 위치 | $K_d=k_{off}/k_{on}$ | $K_m=(k_{off}+k_{e(RL)})/k_{on}$ |
| 변화 원인 | binding 친화도, 해리/결합 속도 | binding + complex 손실/internalization |
| 혼동 시 임상 결과 | in vitro 친화도를 in vivo 배치 경계로 오독 | occupancy·saturation 경계와 sink 영향을 오해석 |

| 용어 | 정의 | 의미 |
|---|---|---|
| $K_d$ | $k_{off}/k_{on}$ | ligand-target binding/해리 평형 |
| $K_m$ | $(k_{off}+k_{e(RL)})/k_{on}$ | binding + complex loss/internalization 효과 |

$$
\underbrace{K_d}_{\text{결합 친화도}}
=
\frac{\underbrace{k_{off}}_{\text{해리}}}{\underbrace{k_{on}}_{\text{결합}}},
\qquad
\underbrace{K_m}_{\text{disposition}}
=
\frac{\underbrace{k_{off}}_{\text{해리}}+\underbrace{k_{e(RL)}}_{\text{complex sink}}}{\underbrace{k_{on}}_{\text{결합}}}
$$

$K_d$와 $K_m$이 다를 수밖에 없는 이유는 $K_m$에 $k_{e(RL)}$가 포함되기 때문입니다. 리포트 작성 시, **in vitro thermodynamic $K_d$**와 **in vivo 모델에서 나온 apparent $K_m$**은 반드시 분리해야 합니다. 두 값을 모두 "affinity"로 부르면 내부 혼동과 reviewer 불일치가 생깁니다. [G&W pp.603–609; R&T pp.711–712]

**Locked sentence**: $K_d$는 **결합의 언어**, $K_m$은 **결합 이후 sink까지 포함한 disposition의 언어**입니다.

**⚡ 기억 고리 — 친화력 vs 처리 속도**:  
$K_d=k_{off}/k_{on}$은 ligand와 target의 **결합 친화력** — 얼마나 단단히 붙는가. $K_m=(k_{off}+k_{e(RL)})/k_{on}$은 결합 친화력에 complex의 **처리 속도(internalization)**까지 더한 apparent kinetic 상수입니다. 그리고 이 둘과 다른 차원에 있는 것이 target turnover($k_{in}/k_{out}$) — target 자체가 **얼마나 빨리 새로 만들어지고 분해되는가**라는 시스템 capacity입니다. 친화력이 높아도 target이 빠르게 재생성되면 낮은 농도에서도 비선형성이 지속되고, 친화력이 낮아도 turnover가 느리면 포화가 오래 유지됩니다. 세 파라미터($K_d$, $K_m$, target turnover)가 서로 독립이므로, **in vitro $K_d$ 하나만으로 in vivo TMDD의 임상적 중요성을 판단할 수 없습니다.**

---

## ▌ Pair 4 — 저농도 Linear PK vs 고농도 Linear PK

| 비교 기준 | 저농도 Linear | 고농도 Linear |
|---|---|---|
| 차원 | low-concentration regime | high-concentration saturated regime |
| 수식 내 위치 | target-specific 경로가 다시 드러나는 영역 | target 경로 포화로 nonspecific linear CL처럼 보이는 영역 |
| 변화 원인 | $C$가 $K_d/K_m$ 부근 또는 그 이하로 감소 | ligand가 target을 크게 초과 |
| 혼동 시 임상 결과 | trough·washout·occupancy 외삽 실패 | 고용량 적합을 전체 농도 범위 타당성으로 과대해석 |

| 농도 영역 | 선형으로 보이는 이유 | 위험 |
|---|---|---|
| Very low ligand | target 경로가 포화되지 않아 비특이적·target-specific 1차 경로가 공존 | assay 민감도가 낮으면 이 구간을 놓침 |
| Very high ligand | target 경로 포화로 비특이적 청소율이 지배 | 고용량 적합만 보고 MM/linear 모델을 과신 |
| Middle range | target saturation이 농도에 따라 변동 | nonlinear clearance가 가장 뚜렷 |

**Locked sentence**: TMDD는 "선형 또는 비선형"이 아닙니다. **농도에 따라 두 종류의 linearity와 한 구간의 nonlinearity가 이어지는 system**입니다. [G&W pp.604–605]

**⚡ 기억 고리 — 고속도로 vs 병목 도로**:  
고용량에서 mAb PK가 선형으로 보이는 이유는, target이 이미 포화되어 TMDD 경로가 더 이상 약물을 추가로 흡수하지 못하고 비특이적 제거 경로(FcRn salvage가 작동하는 IgG-like clearance)가 지배하기 때문입니다 — **고속도로**입니다. 저용량에서 PK가 선형처럼 보이는 이유는 다릅니다. target이 포화되지 않은 상태에서 1차 target-mediated 경로와 nonspecific 경로가 함께 작동하지만, **두 1차 경로의 합이므로 여전히 선형**입니다. 그러나 이 구간의 target 경로는 **병목 도로**여서, 농도가 조금만 변해도 지배 경로가 바뀝니다. 두 linear regime 사이의 nonlinear transition이 임상 용량 범위 안에 걸쳐 있을 때 TMDD 모델링이 필수가 됩니다. **고용량 데이터만 보고 "linear PK"로 결론 내리면 저용량의 병목 도로 거동을 놓칩니다.**

**§5 recap**: 이 세션의 가장 위험한 혼동은 `fit`, `affinity`, `linearity`, `half-life` 같은 친숙한 단어가 TMDD에서는 **모두 조건부 의미**를 갖는다는 점입니다.

---

<!-- SLIDE_START: §7 | title: Self-Test 능동 회상 모듈 -->
<!-- SECTION_CORE: SC-09 -->
# §7 Self-Test: 능동 회상 모듈(Active Recall Module)

## Q1 (회상) ★

$A_0 = k_{in}/k_{out}$에서 $k_{in}$과 $k_{out}$의 단위는?

**Answer**: $k_{in}$은 mass/time, $k_{out}$은 time⁻¹입니다. $A_0$는 두 값의 비율로 정의되는 baseline 양입니다. [G&W p.96]

$$
\underbrace{A_0}_{\text{baseline 양}}
=
\frac{\underbrace{k_{in}}_{\text{mass/time}}}{\underbrace{k_{out}}_{\text{시간}^{-1}}}
$$

**다음 깊이 질문**: 그렇다면 turnover time $t_t = 1/k_{out}$은 임상 PK에서 어떤 측정 가능한 양과 같은가? (M1의 Eq.2:243이 단서.)

---

## Q2 (회상) ★★

왜 $k_{out}$ 변화는 정상상태 level과 도달 시간을 동시에 바꾸는가?

**Answer**: $k_{out}$은 분획 소실률이므로 baseline $A_0=k_{in}/k_{out}$과 time scale $t_t=1/k_{out}$에 **둘 다 동시에** 들어가기 때문입니다. [G&W pp.96–97]

$$
\underbrace{A_0}_{\text{SS level}}
=
\frac{k_{in}}{\underbrace{k_{out}}_{\text{level/시간 동시}}},
\qquad
\underbrace{t_t}_{\text{교체 시간}}
=
\frac{1}{\underbrace{k_{out}}_{\text{분획 소실}}}
$$

**다음 깊이 질문**: 이 비대칭이 linear kinetics 가정에 의존한다면, 높은 농도에서 $k_{out}$이 사실상 saturable이 되는 경우(예: MM 확장) $k_{in}$ 변화와 $k_{out}$ 변화는 어떻게 구별이 어려워지는가?

---

## Q3 (회상) ★★

Full TMDD의 4개 상태변수는?

**Answer**: ligand central, ligand tissue/peripheral, free target $R$, ligand-target complex $RL$입니다. [G&W pp.604–607]

**다음 깊이 질문**: 이 4개 state 중 임상에서 직접 측정이 가장 어려운 것은? 그 측정 결손이 PK27 Table 27.2의 식별 위계($k_{on}$/$k_{off}$/$k_{e(RL)}$ 정밀도)에 어떤 구조적 영향을 주는가?

---

## Q4 (적용) ★★

mAb ligand-only 데이터에서 고용량 곡선은 잘 맞지만 가장 낮은 용량에서 체계적인 under/over-prediction이 보입니다. 무엇을 의심해야 하는가?

**Answer**: MM 또는 reduced model이 관찰된 고용량 범위에서는 내삽을 하지만, **저농도 TMDD phase를 제대로 설명하지 못할 가능성이 높습니다.** 이 판단은 측정된 용량/농도 범위에 한정되며, 외삽 영역에서는 target occupancy와 sensitivity analysis가 필요합니다. [G&W p.609]

**다음 깊이 질문**: 저용량 외삽을 모델 구조 변경 없이 정당화하려면 — 예를 들어 target/complex assay 추가가 즉시 불가능한 상황에서 — 어떤 sensitivity analysis 절차를 어떤 순서로 수행해야 하는가? (M5 §D 및 Q10이 단서.)

---

## Q5 (적용) ★★

$K_m$과 $K_d$가 다를 수밖에 없는 기전적 이유는?

**Answer**: $K_d=k_{off}/k_{on}$은 결합/해리 평형이고, $K_m=(k_{off}+k_{e(RL)})/k_{on}$은 complex의 비가역적 소실($k_{e(RL)}$)까지 포함합니다. complex sink가 있으면 **$K_m$은 thermodynamic 친화도가 아니라 apparent kinetic 상수**가 됩니다. [G&W p.609; R&T p.712]

$$
\underbrace{K_d}_{\text{결합 평형}}
=
\frac{k_{off}}{k_{on}},
\qquad
\underbrace{K_m}_{\text{결합+소실}}
=
\frac{k_{off}+k_{e(RL)}}{k_{on}}
$$

**다음 깊이 질문**: in vitro SPR/BLI로 측정한 thermodynamic $K_d$와 in vivo PK fitting으로 추출한 apparent $K_m$을 같은 후보 mAb에 대해 internal report나 NDA narrative에서 어떻게 명시적으로 분리해야 reviewer가 reconciliation 요청을 안 하는가?

---

## Q6 (적용) ★

sc mAb의 terminal slope를 곧바로 elimination 반감기로 해석하면 왜 위험한가?

**Answer**: 큰 단백질은 sc/im 후 림프관 흡수가 느려 **absorption-rate-limited** 프로파일을 보일 수 있습니다. somatropin처럼 i.v. 반감기는 짧아도 sc 프로파일은 길게 지속될 수 있습니다. [R&T pp.718–721]

**다음 깊이 질문**: sc mAb의 terminal phase가 absorption-rate-limited인지 elimination-rate-limited인지 어떻게 구분하는가? 어떤 추가 실험 설계나 데이터 비교가 결정적 신호를 주는가?

---

## Q7 (회상) ★★

PK27에서 $V_c=0.05\ \mathrm{L\cdot kg^{-1}}$는 어떻게 처리되었는가?

**Answer**: $V_c$는 fixed assumption으로 사용되었고, Table 27.2는 그 외 **8개의 추정/보고 파라미터**를 제시합니다. fixed $V_c$까지 structural quantity로 세면 9개를 언급할 수 있지만, "8 estimated parameters"와는 구분해야 합니다. [G&W pp.603, 608–609]

$$
\underbrace{V_c}_{\text{central volume}}
=
\underbrace{0.05\ \mathrm{L\cdot kg^{-1}}}_{\text{fixed}},
\qquad
\overbrace{8}^{\text{추정/보고}}
\ne
\overbrace{9}^{\text{fixed }V_c\text{ 포함}}
$$

**다음 깊이 질문**: PK27의 $V_c=0.05\ \mathrm{L\cdot kg^{-1}}$는 healthy adult 가정에 가깝습니다. edema, severe burn, ascites, pediatric subgroup처럼 plasma volume이 의미 있게 다른 sub-population에 같은 fixed $V_c$를 적용하면, sensitivity analysis는 어떻게 설계해야 다른 파라미터(특히 $k_{on}$)의 robustness를 검증할 수 있는가? (M4 §F가 출발점.)

---

## Q8 (적용) ★

target과 complex 데이터가 추가되면 왜 $k_{on}$, $k_{off}$, $k_{e(RL)}$의 정밀도가 좋아지는가?

**Answer**: ligand-only 데이터는 여러 ODE 항의 합성 결과만 보여줍니다. target 데이터는 saturation/recovery를, complex 데이터는 sink 거동을 직접 가르치므로 해당 파라미터의 CV%가 개선됩니다. PK27 Table 27.2에서 $k_{on}$은 **17→2→1**, $k_{off}$는 **27→13→3**, $k_{e(RL)}$는 **27→23→2**로 개선됩니다. [G&W p.609]

**다음 깊이 질문**: target/complex assay가 임상에서 가용하지 않을 때 — 예를 들어 PK26 Efalizumab처럼 — 동등한 식별성을 확보할 차선 전략이 있는가? 어떤 조건이 충족되어야 reduced model이 정당화되는가?

---

## Q9 (회상) ○

R&T Fig.21-16에서 얻을 수 있는 올바른 결론과 얻으면 안 되는 결론은?

**Answer**: **올바른 결론**은 분자량 증가에 따라 림프 회수율이 증가한다는 **방향성**입니다. **얻으면 안 되는 결론**은 0.246–19 kDa sheep 데이터를 150 kDa mAb에 선형 외삽해서 구체적 recovery 퍼센트를 계산하는 것입니다. [R&T p.720]

**다음 깊이 질문**: 150 kDa mAb의 sc 림프 회수율을 정량 예측할 수 없다면, 임상 protocol 설계에서 sc 흡수 프로파일의 불확실성을 어떻게 다루는 것이 안전한가? (M2 §B의 absorption-rate-limited 메시지와 연결.)

---

## Q10 (보스 딜레마) ★★

팀이 "MM 모델로 OFV도 낮고 VPC도 괜찮으니 first-in-human 저용량 외삽에 쓰자"고 주장합니다. 30초 답변은?

**Answer**: "MM은 관찰된 용량 범위 안에서는 쓸 수 있지만, 저용량 외삽은 **target occupancy가 충분히 높게 유지되는지 확인**해야 합니다. PK27에서는 고용량 적합이 양호해도 가장 낮은 용량 곡선에서 체계적 편차가 있었고 $K_m$이 0.03에서 3.7로 **123배 과대예측**되었습니다. 최소한 dose-stratified 잔차, 예측 occupancy, 저농도 sensitivity analysis를 보고 결정해야 합니다." [G&W p.609]

$$
\underbrace{K_{m,\mathrm{MM}}}_{\text{reduced model}}
=
\underbrace{3.7}_{\text{PK27 MM}},
\qquad
\underbrace{K_{m,\mathrm{TMDD}}}_{\text{full model}}
=
\underbrace{0.03}_{\text{PK27 TMDD}},
\qquad
\frac{K_{m,\mathrm{MM}}}{K_{m,\mathrm{TMDD}}}\approx123
$$

**다음 깊이 질문**: 위 sensitivity analysis 결과 예측 occupancy가 dosing interval의 일부 구간에서 80% 미만으로 떨어지는 sub-group이 발견되었다고 가정해 보세요. 이 sub-group을 위해 reduced MM을 그대로 유지할 것인가, Full TMDD로 전환할 것인가, 아니면 별도 covariate model로 분리할 것인가? 어떤 기준으로 결정하며, 내부 PK report나 NDA narrative에서 그 결정을 어떻게 정당화할 것인가? *(이것이 §8 Professional Moat의 narrative justification 능력입니다.)*

**§7 recap**: 답을 외우는 것보다 중요한 건, **"이 데이터가 어떤 phase와 어떤 ODE 항을 실제로 가르치는가?"**를 매번 그 자리에서 묻는 습관입니다.

---

<!-- SLIDE_START: §8 | title: 메타 프레임과 큰 그림 -->
<!-- SECTION_CORE: SC-10 -->
# §8 메타 프레임과 큰 그림(Meta-Frame & Big Picture)

## A. 위치 설정

이 세션은 **biologics pharmacometrics의 입구**입니다. Small molecule PK에서는 청소율과 $V_d$ 중심으로 설명할 수 있었습니다. 그러나 mAb에서는 **target biology, binding kinetics, complex sink, FcRn salvage, lymphatic input**이 함께 PK 곡선의 형태를 만듭니다.

선행 지식: `linear PK → Michaelis-Menten → turnover → TMDD`  
후속 지식: `mAb PopPK → target occupancy 시뮬레이션 → QSP/PBPK → biologics 임상약리 narrative`

## B. 의존 관계와 실패 모드

| 건너뛰면 | 구체적 실패 |
|---|---|
| Turnover | target baseline을 predose DV로만 처리하고 $R_0/k_{out}$ 해석을 잃습니다. |
| 단백질 ADME | sc mAb terminal slope를 elimination으로 오해합니다. |
| 4-Phase TMDD | 고용량 적합만 보고 저용량 외삽 편향을 놓칩니다. |
| Full TMDD | target/complex 데이터의 가치를 "nice-to-have"로 잘못 판단합니다. |
| MM 경계 | 관찰 범위 내 내삽을 임상 외삽으로 착각합니다. |

## C. 전문가 해석 지점 (Professional Moat)

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| target turnover 변화 | $k_{in}$/$k_{out}$ | → | baseline·recovery·occupancy 해석 변화 | baseline scenario와 target 데이터 확인 |
| FcRn/slow input 개입 | $F$, $T_{max}$, apparent $t_{1/2}$ | → | terminal slope 오독 | i.v. 비교 또는 dose-stratified 프로파일 확인 |
| 저용량 TMDD 경계 진입 | $K_m$, $K_d$, occupancy | → | trough·subgroup 외삽 편향 | sensitivity analysis와 Full TMDD 필요성 검토 |
| complex sink 관찰 부족 | $k_{e(RL)}$ | → | mechanism fitted but not learned | target/complex assay 또는 informative prior 검토 |

이 세션을 체화하면 두 가지 능력이 생깁니다:

1. **Mechanistic 모델 narrative 정당화**: "왜 Full TMDD인가 / 왜 MM이어도 되는가 / 왜 target assay가 필요한가"를 **수식·생리학·관찰된 농도 범위**로 설명할 수 있습니다.
2. **진단적 GOF 읽기**: 전체 VPC가 아니라 **dose-stratified 잔차, 저용량 프로파일, target/complex coverage**를 먼저 보고 구조적 misspecification을 의심할 수 있습니다.

**Trench-level diagnostic rule**: mAb TMDD 데이터셋을 처음 받으면 전체 적합 plot보다 먼저 **dose-stratified plot**을 만듭니다. 고용량은 맞고 저용량만 체계적으로 틀리면, "variability problem"보다 **"reduced model 경계 문제"**를 먼저 의심합니다.

## D. 최종 통합

| 후속 세션 | 이 세션에서 열리는 개념 | 이 세션 없으면 실패하는 것 |
|---|---|---|
| mAb PopPK | 제한 분포, FcRn, target-mediated clearance | terminal slope와 covariate effect 해석 |
| TMDD/QSP | ligand-target-complex ODE topology | target biology와 PK coupling 설명 |
| Target occupancy 시뮬레이션 | $K_d$, $K_m$, occupancy 경계 | dosing interval 동안의 pharmacologic coverage 판단 |
| Biologics 임상약리 리포트 | 모델 경계와 외삽 방어 | MM/Full TMDD 선택 근거 방어 |

mAb 비선형 PK의 본질은 "항체가 크다"가 아니라, **큰 ligand가 제한된 tissue space와 림프관 입력을 거쳐 endogenous target turnover system에 들어가고, binding/complex/sink가 농도의존적 청소율을 만든다**는 점입니다. Full TMDD는 이 과정을 분해하고, MM은 일부 조건에서만 이를 압축합니다. **모델 선택의 기준은 편의성이 아니라 데이터셋이 관찰한 phase와 임상 의사결정이 요구하는 외삽 범위**입니다.

<!-- v3.8 변환 노트
- 활자량 감축: v3.7 1,367줄 → v3.8 1,075줄 (감축률 ≈ 21%, 카드 내부 콘텐츠 보존 우선)
  · 컴파일러 프롬프트 §2.3 목표(40–55%)보다 감축 폭은 작음. 이유: 카드 내부 수치·약물·기전 설명은 byte 보존 우선이었고, 줄어든 분량은 주로 §1.5 학습 항법 오버레이·기호 통일 주석·자가검증 체크리스트·자기참조 안내·관념체 문장에서 회수됨.
- 보존 감사:
  · SLIDE_START 마커 = 10개 (§1, §2, M1–M5, §5, §7, §8)
  · 수식 블록 = 60개 (전부 unique; bare-equation + annotated-equation 쌍은 annotated 단일 블록으로 통합, Eq.2:237 등은 annotated 끝에 \qquad \text{Eq.X:Y} 라벨로 보존)
  · 출처 anchor: [G&W p.609] 13회, [G&W p.96] 9회 등 단일 페이지 anchor 다수 + 복합 anchor(세미콜론 결합) 14종 전부 보존
  · 핵심 약물명: somatropin·anakinra·adalimumab·omalizumab·efalizumab·methotrexate·IgX·estradiol 모두 분류 인라인 + "→ ~의 사례" 닫음
  · 핵심 수치: PK27 1.5/5/15/45 mg·kg⁻¹, $K_m$ 0.03 vs 3.7 (123배), Vc=0.05, CV% 17→2→1 / 27→13→3 / 27→23→2, FCR 6.7%, $V_{ss}$ 0.04–0.23 L·kg⁻¹, MW 15,000–20,000 g/mol, T_max 5.5/7.5, F 0.50/0.62/0.64, t1/2 17/26/30 days, occupancy 90–95% 모두 보존
- 주요 변환:
  · 메타 문구 제거(기호 통일 HTML 주석, 그림 정책 단락, 학습 경로 ASCII, 시작 전/완료 후 점검의 관념체, [EXPERT_INFERENCE] 태그)
  · §1.5 빠른 읽기 경로 박스로 학습자 안내 압축(M1→M2→M3→M4→M5 5카드 경로 + 학습 완료 후 체크)
  · 자기참조 해소: "Mn의 결론이 ~한다" 형태를 해당 결론 한 문장 + 포인터(→ Mn 참조)로 변환
  · 약물 즉맥락화: 첫 등장 시 분류 인라인 + 사례 닫음
  · 콜아웃 단일화: 카드별 💡⚠️🔑 중복을 1개 박스로 통합(카드당 콜아웃 ≤ 6)
  · 수식 중복 제거: bare + annotated 쌍 → annotated only
  · v3.7 자가검증 체크리스트 섹션은 PART B 흔적으로 판단 → 제거
-->

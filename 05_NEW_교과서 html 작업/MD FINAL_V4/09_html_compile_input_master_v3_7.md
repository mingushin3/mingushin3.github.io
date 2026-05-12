# 09_HTML Compile Input Master — v3.7
<!-- 기호 통일: Vmax → V_{max} (첫 등장 M5 기준) -->
<!-- 기호 통일: K_on/K_off/K_out/K_e(RL) → k_{on}/k_{off}/k_{out}/k_{e(RL)} (수식 첫 등장 기준) -->


## 출처 및 범위 노트

이 자료는 Gabrielsson & Weiner 5e의 turnover, PK26 Efalizumab, PK27 Target Mediated Drug Disposition 범위와 Rowland & Tozer 5e Ch.21 Protein Drugs 범위에 근거하여 protein PK, mAb disposition, FcRn, TMDD, Michaelis-Menten approximation, data richness, assay identifiability를 학습자용으로 정리한 파일입니다.

교과서 그림은 저작권상 직접 삽입하지 않고, 원그림 참조와 새 해설 도식으로 안내합니다. 새 외부 근거, 새 수치, 새 page tag, 새 reference는 추가하지 않고 기존 page tag와 source label을 유지합니다.

---

## PART A — 학습자용 완성 핸드아웃


> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** Turnover→mAb ADME→TMDD→Full TMDD→MM boundary를 한 줄 경로로 고정해라 — 이 세션의 모든 판단은 “어떤 데이터가 어떤 파라미터를 가르쳤는가”로 귀결된다.

---



> **임상 장면**
> 항체를 1.5, 5, 15, 45 mg·kg⁻¹로 급속 정맥 주사한 PK27 데이터에서 high-dose profile은 그럴듯하게 맞지만 lowest-dose profile은 체계적으로 어긋납니다. MM 모델의 $K_m$은 3.7, TMDD 모델의 $K_m$은 0.03으로 약 123배 차이가 납니다. 이 차이는 단순한 적합 품질 문제가 아니라 저농도 외삽, trough 예측, target occupancy 판단을 흔드는 구조적 신호입니다. [G pp.602–603; G p.609]

## 학습자 안내(Learner Navigation Aid)

**이 자료 사용법**

1. MUST 카드 5개를 순서대로 읽습니다: M1 turnover → M2 protein/antibody PK → M3 TMDD curve phases → M4 Full TMDD → M5 MM boundary.
2. 📖 **교과서 그림 참조**가 나오면 해당 교과서 그림을 직접 확인합니다. 저작권상 이미지는 본 자료에 삽입하지 않습니다.
3. §5에서 자주 혼동되는 개념 쌍을 정리하고, §7에서 능동 회상을 점검하며, §8에서 전문가 수준의 통합 판단을 완성하면 됩니다.
4. §7 Self-Test에서 ★★는 핵심 질문입니다. 자동으로 답이 나올 때까지 반복하면 됩니다. ★는 중요 질문이고, 오답이면 재점검합니다. ○는 표준 수준입니다. 각 답변 뒤에는 "다음 깊이 질문"이 이어져 후속 질문 층위를 열어 줍니다.
5. §5에서 **Critical Blow**로 표시된 쌍은 이 세션에서 혼동할 경우 임상 의사결정에 가장 큰 왜곡을 일으키는 쌍입니다.

**학습 경로**

```text
M1 kin/kout baseline → M2 biologics ADME gates → M3 concentration-regime curve reading → M4 mechanistic ODE topology → M5 reduced-model boundary → §5 confusion pairs → §7 self-test → §8 professional synthesis
```

**시작 전 점검**

- 1구획·2구획 선형 PK, Michaelis-Menten 표기법, ODE 상태변수(state variable) 개념을 이미 알고 있어야 합니다.
- 학습 내내 이 질문을 가지고 읽으면 됩니다: "이 파라미터를 실제로 가르쳐주는 데이터는 무엇입니까?"

**학습 완료 후 점검**

- $k_{in}$, $k_{out}$, $k_{on}$, $k_{off}$, $k_{e(RL)}$, $K_d$, $K_m$이 왜 서로 대체 불가한지 설명할 수 있어야 합니다.
- Full TMDD가 필요한 상황과 MM 근사가 내삽(interpolation) 도구에 머무는 상황을 데이터 기반으로 구분하고 방어할 수 있어야 합니다.
- 고용량 적합(fit) 품질이 왜 저용량·저농도 외삽을 자동으로 정당화하지 않는지 설명할 수 있어야 합니다.

---


# 갱신된 큐레이션 맵(Updated Curation Map)


본 세션의 핵심은 “항체 PK” 자체가 아닙니다. 핵심은 **turnover 수학이 표적매개 약물배치(TMDD, target-mediated drug disposition; 표적 결합이 약물 배치를 바꾸는 현상)로 확장되는 순간, 어떤 자료가 어떤 파라미터를 가르치는가**를 체화하는 것입니다. 10분 핸드아웃 기준으로 남길 중심축은 5개뿐입니다.

## MUST

| # | 개념 | 고정 근거 |
|---|---|---|
| M1 | **Turnover Paradigm ($k_{in}$/$k_{out}$)** | TMDD의 target compartment($R$)는 endogenous turnover pool입니다. 따라서 $k_{in}/k_{out}$ 없이는 target baseline, recovery, $R_0$, $k_{out}$ 식별을 설명할 수 없습니다. [G pp.95–97] |
| M2 | **Protein/Antibody Distinctive PK** | 큰 분자량, 제한적 $V_d$, lymphatic absorption, renal cutoff, FcRn salvage가 mAb PK의 “느림”과 비선형성의 생리학적 전제입니다. [G pp.97–102; R&T pp.701–724] |
| M3 | **TMDD 4-Phase Profile** | 곡선 모양을 Phase A–D로 읽어야 Full TMDD와 MM approximation 중 무엇을 선택할지 데이터 기반으로 판단할 수 있습니다. [G pp.603–610; R&T pp.711–712] |
| M4 | **Full TMDD Model** **[⚡ Apex Concept]** | ligand, target, complex, sink가 하나의 ODE system으로 결합되는 지점이며, PD와 PK가 같은 수식으로 묶입니다. [G pp.603–609; R&T pp.711–712] |
| M5 | **Michaelis-Menten Approximation Boundary** | MM은 limited dose range에서는 쓸 수 있습니다. 그러나 low-concentration extrapolation과 occupancy(← 표적 중 ligand가 결합한 비율) 판단에서는 구조적 bias를 만들 수 있습니다. [G p.609; R&T p.712] |

## CONTEXT

| 맥락 항목 | 고정 배치 |
|---|---|
| 욕조/물 turnover 예시 | M1 직관 보조 1문장 [G p.96] |
| IgX sc 40 µg·kg⁻¹ 및 immunoglobulin turnover | M1 임상 앵커 [G pp.100–102] |
| 폐경 후 여성의 estradiol turnover | M1 endogenous turnover 확장 [G pp.102–104] |
| Baseline scenarios / circadian 및 feedback 예시 | M1 가정 경계; independent MUST로 승격하지 않음 [G pp.104–111] |
| Protein $V_d$, renal sieving, hepatic uptake, FcγR/FcRn | M2 ADME 기전 [R&T pp.701–709] |
| Somatropin sc absorption-rate-limited 예시 | M2 흡수 맥락 1문장 [R&T p.721] |
| Anakinra renal disease 예시 | M2 renal disease 맥락 1문장 [R&T p.724] |
| Efalizumab PK26 reduced model | M5 “MM이 제한적으로 통하는 사례” 앵커 [G pp.599–601; R&T p.710] |

---

---



<!-- SLIDE_START: §1 | title: 세션 헤더와 로드맵 -->
# §1 세션 헤더와 로드맵(Session Header & Roadmap)

## 3-레이어 개념 지도(ASCII Layer Map)

```text
Layer 1 — 무엇인가
  Turnover baseline / mAb ADME gates / TMDD phase / Full TMDD / MM boundary

Layer 2 — 어떻게 계산되는가
  A0 = kin/kout / dR-dt & dRL-dt / Kd = koff/kon / Km = (koff + keRL)/kon / ClMM = Vmax/(Km+C)

Layer 3 — 언제, 왜 중요한가
  baseline recovery / slow SC input / low-dose extrapolation / target occupancy / model-selection defense
```

## 지식 그래프 위치(Knowledge Graph Position)

```text
1구획·2구획 선형 PK + Michaelis-Menten + ODE 기본
        → 이 세션: Turnover → mAb ADME → TMDD → Full TMDD/MM boundary
        → mAb PopPK · TMDD/QSP · target occupancy simulation · biologics clinical pharmacology report
```

🧭 **읽는 순서:**
카드 1 (M1): baseline은 왜 단순한 0시간 값이 아니라 turnover pool인가?
카드 2 (M2): mAb profile의 느림은 어떤 ADME gate들이 합성한 결과인가?
카드 3 (M3): TMDD curve의 Phase A–D는 어떤 농도 영역을 가리키는가?
카드 4 (M4): ligand, target, complex, sink는 어떤 ODE topology로 묶이는가?
카드 5 (M5): MM approximation은 어느 경계 안에서만 방어 가능한가?



**Source**: [혼합]

- Gabrielsson & Weiner 5e, Ch.2 §2.6 Turnover [G pp.94–111]
- Gabrielsson & Weiner 5e, Case Study PK26 Efalizumab [G pp.599–601]
- Gabrielsson & Weiner 5e, Case Study PK27 Target Mediated Drug Disposition [G pp.602–610]
- Rowland & Tozer 5e, Ch.21 Protein Drugs [R&T pp.687–730]

**그림 정책**: 교과서 그림은 직접 삽입하지 않고, 원그림 참조 또는 새 해설 도식으로 안내합니다.  
**범위 한계**: 새 외부 근거 없이 기존 page tag와 source label을 유지합니다.

## 핵심 아이디어(Big Idea)

> **항체의 비선형 PK는 “큰 약물이 천천히 빠진다”가 아닙니다. Ligand가 endogenous target turnover system에 결합하면서 생기는 농도의존적 청소율(concentration-dependent clearance)입니다. Full TMDD를 MM으로 줄이면 제한된 용량 범위(dose range)에서는 맞아 보일 수 있습니다. 그러나 PK27에서는 $K_m$이 0.03에서 3.7로 약 123배 과대예측(over-predicted)되어 저농도 외삽(low-concentration extrapolation)이 구조적으로 틀어졌습니다.** [G p.609]


## 로드맵(Roadmap)

```text
M1. Turnover Paradigm
       ↓
M2. Protein/Antibody ADME 특수성
       ↓
M3. TMDD 4-phase curve reading
       ↓
M4. Full TMDD Model: ligand + target + complex + sink
       ↓
M5. Michaelis-Menten Approximation: 언제 허용되고 언제 무너지는가
```


## 지식 위치(Knowledge Position)

이 세션은 1구획/2구획 PK(one-/two-compartment PK), Michaelis-Menten kinetics, ODE 기본, NONMEM `$DES` 구조를 전제로 합니다. 후속으로는 mAb PopPK, TMDD/QSP, target occupancy simulation, FcRn engineering, biologics clinical pharmacology report 작성으로 이어집니다. 단, 본 자료에서는 교과서 범위를 넘어가는 specific regulatory timeline, cost, company-risk narrative는 포함하지 않습니다.


**Section recap**: 이 세션의 판단 기준은 “curve가 예쁘게 fit되는가?”가 아닙니다. “이 데이터가 target turnover, binding, complex sink를 분리해서 가르치는가?”입니다.

---


<!-- SLIDE_START: §2 | title: 개념 해부 카드 -->
# §2 개념 해부 카드(Concept Anatomy Cards)

---


> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** $k_{in}$/$k_{out}$은 baseline, pool size, recovery time을 동시에 지배한다 — target $R$을 고정값으로 보는 순간 TMDD 해석은 출발점부터 흔들린다.

---



<!-- SLIDE_START: M1 | title: Turnover Paradigm -->
## ▌ Card M1 — Turnover Paradigm ($k_{in}$/$k_{out}$)

> **거장의 시각**
> baseline을 단순 predose 값으로 읽으면 $R_0$, $k_{out}$, recovery time이 모두 잔차·임의 파라미터처럼 보입니다.
> turnover 관점으로 보면 target $R$은 ligand가 교란하는 endogenous pool이며, TMDD의 출발점이 명확해집니다.


Turnover는 내인성 물질(endogenous compound; 체내에서 원래 생성되는 물질)의 baseline이 고정된 숫자가 아니라, **0차 입력(zero-order input) $k_{in}$과 1차 소실(first-order loss) $k_{out}\cdot A$가 유지하는 동적 평형**임을 뜻합니다. TMDD의 target $R$도 이 구조를 따릅니다. 따라서 mAb가 target에 결합한다는 것은 외부 ligand가 endogenous turnover pool에 개입한다는 뜻입니다. [G pp.95–96]


### A. 형식적 정의(Formal Definition)

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $A$ | mass | turnover pool 안의 양 | 생성·소실 균형 변화 |
| $k_{in}$ | mass/time | 0차 입력·생성률 | 합성 증가/감소, baseline 생성 변화 |
| $k_{out}$ | time⁻¹ | 1차 분획 소실률 | catabolism·degradation·turnover 속도 변화 |
| $A_0$ | mass | steady-state baseline amount | $k_{in}$ 증가 또는 $k_{out}$ 감소 |
| $t_t$ | time | pool 교체 시간 | 주로 $k_{out}$ 변화 |


$$\frac{dA}{dt}=k_{in}-k_{out}\cdot A \qquad \text{Eq.2:237}$$

$$
\overbrace{\frac{dA}{dt}}^{\text{pool 변화}}
=
\underbrace{k_{in}}_{\text{0차 입력}}
-
\underbrace{k_{out}\cdot A}_{\text{1차 소실}}
$$


정상상태에서는 다음 관계가 성립합니다. [G pp.95–96]

| 관계식 | 의미 | 출처 |
|---|---|---|
| $k_{in}=k_{out}\cdot A_0$ | 입력 = 출력 | Eq.2:239 [G p.96] |
| $k_{out}=k_{in}/A_0$ | fractional turnover rate | Eq.2:240 [G p.96] |
| $A_0=k_{in}/k_{out}$ | baseline amount | Eq.2:241 [G p.96] |
| $t_t=A_0/k_{in}=1/k_{out}$ | turnover time | Eq.2:242 [G p.96] |
| $t_t=V_{ss}/Cl=MRT$ | turnover time이 PK MRT와 연결됨 | Eq.2:243 [G p.96] |
| $t_{1/2}=\ln(2)/k_{out}=\ln(2)\cdot t_t$ | 반감기 관계 | Eq.2:244 [G p.96] |

$$
\begin{aligned}
\underbrace{k_{in}}_{\text{SS 입력}} &= \underbrace{k_{out}\cdot A_0}_{\text{SS 출력}} \\
\underbrace{k_{out}}_{\text{분획 소실}} &= \underbrace{\frac{k_{in}}{A_0}}_{\text{입력/pool}} \\
\underbrace{A_0}_{\text{baseline 양}} &= \underbrace{\frac{k_{in}}{k_{out}}}_{\text{입력-소실 균형}} \\
\underbrace{t_t}_{\text{교체 시간}} &= \underbrace{\frac{A_0}{k_{in}}}_{\text{pool/입력}} = \underbrace{\frac{1}{k_{out}}}_{\text{소실역수}} \\
\underbrace{t_t}_{\text{교체 시간}} &= \underbrace{\frac{V_{ss}}{Cl}}_{\text{PK 체류시간}} = \underbrace{MRT}_{\text{평균 체류}} \\
\underbrace{t_{1/2}}_{\text{반감기}} &= \underbrace{\frac{\ln(2)}{k_{out}}}_{\text{1차 반감}} = \underbrace{\ln(2)\cdot t_t}_{\text{교체시간 연결}}
\end{aligned}
$$


$k_{in}$은 mass/time, $k_{out}$은 time⁻¹입니다. 이 단위 구분을 놓치면 target synthesis와 binding on-rate를 혼동하게 됩니다.


> 💡 **Baseline은 결과값** — $A_0$는 관찰값 하나가 아니라 $k_{in}/k_{out}$ 균형의 결과입니다.
> ⚠️ **헷갈림 방지:** $k_{in}$은 mass/time 입력이고 $k_{out}$은 time⁻¹ 분획 소실입니다. 둘 다 “rate”라고 부르면 합성과 소실을 섞게 됩니다.
> 🔑 **시간척도 규칙:** $k_{out}$이 바뀌면 level뿐 아니라 새 steady state에 접근하는 시간도 함께 바뀝니다.


### B. 직관: 수도꼭지 vs 배수구

10 L 욕조에 1 L·min⁻¹로 물이 들어오면 turnover time은 10분입니다. 사람 몸의 물 42 L와 하루 intake 2.5 L를 쓰면 water turnover time은 약 17일입니다. 즉, 핵심은 “얼마나 많이 있는가”보다 “현재 pool 전체가 얼마나 빨리 교체되는가”입니다. 이 단순한 예가 endogenous IgG, target receptor, hormone turnover와 같은 수학입니다. [G p.96]

Fig.2.70의 핵심은 비대칭성입니다. $k_{in}$을 바꾸면 steady-state level만 바뀌고, time-to-steady-state는 linear kinetics 조건에서 유지됩니다. 반면 $k_{out}$을 바꾸면 level과 time-to-steady-state가 함께 바뀝니다. [G p.97]


### C. 임상 앵커(Clinical Anchors)

**IgX sc 예시**: Growth hormone-like IgX 40 µg·kg⁻¹ sc 투여에서 predose baseline은 32 µg·L⁻¹였습니다. 추정값은 $Cl/F=0.03\ \mathrm{L\cdot h^{-1}\cdot kg^{-1}}$, $V/F=0.10\ \mathrm{L\cdot kg^{-1}}$, $k_{in}=0.78\ \mathrm{µg\cdot h^{-1}\cdot kg^{-1}}$, $t_t=2.7\ \mathrm{h}$, $MIT=1.8\ \mathrm{h}$, $t_{1/2}=2.5\ \mathrm{h}$, $k_{out}=0.27\ \mathrm{h^{-1}}$, pool size 2.3 µg·kg⁻¹였습니다. [G pp.100–101]

$$
\begin{aligned}
\underbrace{t_t}_{\text{pool 교체}} &= \underbrace{2.7\ \mathrm{h}}_{\text{IgX 추정값}}, \\
\underbrace{k_{out}}_{\text{분획 소실}} &= \underbrace{0.27\ \mathrm{h^{-1}}}_{\text{시간당 소실}}, \\
\underbrace{t_{1/2}}_{\text{반감기}} &= \underbrace{2.5\ \mathrm{h}}_{\text{profile 요약}}
\end{aligned}
$$


**Immunoglobulin turnover**: endogenous IgG는 Table 2.11에서 $t_{1/2}=23\ \mathrm{days}$, fractional catabolic rate 6.7% plasma pool·day⁻¹, turnover 33 mg·kg⁻¹·day⁻¹로 제시됩니다. 이는 R&T의 therapeutic mAb half-life “approximately 21 days”와 비슷하지만, 두 문장을 같은 사실로 합치면 안 됩니다. [G p.102; R&T p.708]

$$
\underbrace{t_{1/2}}_{\text{IgG 반감기}}
=
\underbrace{23\ \mathrm{days}}_{\text{내인성 IgG}},
\qquad
\underbrace{\mathrm{FCR}}_{\text{분획 이화율}}
=
\underbrace{6.7\%\ \mathrm{day^{-1}}}_{\text{혈장 pool 소실}}
$$


**Estradiol turnover**: postmenopausal women 15명에서 estradiol은 평균 $k_{in}=19\ \mathrm{µg\cdot 24h^{-1}}$, $Cl=1.6\ \mathrm{L\cdot min^{-1}}$, $V_{ss}=50\ \mathrm{L}$, $t_{1/2}=26\ \mathrm{min}$, $MRT=18\ \mathrm{min}$로 보고됩니다. 낮은 E2 level은 clearance 증가보다 turnover 감소로 설명됩니다. [G pp.102–104]

$$
\begin{aligned}
\underbrace{k_{in}}_{\text{E2 생성률}} &= \underbrace{19\ \mathrm{\mu g\cdot 24h^{-1}}}_{\text{평균 입력}}, \\
\underbrace{Cl}_{\text{제거능}} &= \underbrace{1.6\ \mathrm{L\cdot min^{-1}}}_{\text{전신 CL}}, \\
\underbrace{MRT}_{\text{평균 체류 시간}} &= \underbrace{18\ \mathrm{min}}_{\text{교체 척도}}
\end{aligned}
$$


### D. 가정과 경계조건

Turnover는 baseline이 의미 있게 정의될 때 강력합니다. 그러나 Fig.2.77은 baseline이 constant, oscillating, feedback-governed, Zeitgeber-driven일 수 있음을 보여 줍니다. 따라서 PD endpoint를 처리할 때 첫 질문은 “predose concentration을 baseline으로 빼도 되는가?”가 아닙니다. “이 endpoint는 Fig.2.77 중 어떤 baseline scenario인가?”여야 합니다. [G p.104]


**Trench-level tip**: predose target measurement가 있으면 단순히 `R0=THETA`로 추정하지 말고, 가능하면 baseline DV record로 모델에 들어가도록 설계해야 $R_0$ variability가 residual error로 흡수되는 것을 줄일 수 있습니다. 이 구현 팁은 교과서 수식의 NONMEM translation이며, 원문 control stream은 아닙니다.

### E. 한계(Limitations)

Turnover 관계식은 linear first-order loss를 전제로 합니다. 높은 농도에서 saturable metabolism이 개입하면 Michaelis-Menten 또는 더 복잡한 feedback model이 필요합니다. Hyaluronan, body temperature, feedback examples는 이 boundary를 보여 주는 맥락(context)이지, 본 세션의 독립 MUST는 아닙니다. [G pp.95, 105–111]


### G. 제텔카스텐 원자(Zettelkasten Atom)

```text
Turnover = dynamic baseline.
A0 = kin/kout, tt = 1/kout = Vss/Cl = MRT.
TMDD target R is an endogenous turnover pool perturbed by ligand binding.
```


**M1 recap**: Turnover를 모르면 $R_0$, $k_{out}$, baseline correction, target recovery를 모두 “피팅 파라미터”로만 보게 됩니다. Turnover를 이해하면 TMDD가 endogenous biology 위에 얹힌 PK model로 보입니다.

---


> 📖 **교과서 그림 참조:** Gabrielsson & Weiner 5e, p.97, Fig.2.70
> 이 그림은 turnover의 비대칭 논리를 고정해 줍니다. $k_{in}$ 변화는 steady-state level을 바꾸지만, $k_{out}$ 변화는 level과 time-to-steady-state를 함께 바꿉니다. 두 패널을 직접 보지 않으면 학습자가 둘을 모두 일반적인 “rate change”로 처리하기 쉽습니다.
> 확인 시점: Card M1을 읽은 뒤 확인하면 됩니다.


$$
\underbrace{k_{in}\uparrow}_{\text{입력 증가}}
\Rightarrow
\underbrace{A_0\uparrow}_{\text{level 상승}},
\qquad
\underbrace{k_{out}\uparrow}_{\text{분획 소실 증가}}
\Rightarrow
\underbrace{A_0\downarrow}_{\text{level 하강}}+\underbrace{t_t\downarrow}_{\text{접근 시간 단축}}
$$


> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** mAb PK의 느린 profile은 half-life 하나가 아니라 distribution·lymphatic input·elimination·FcRn rescue gate가 합성한 결과다.

---

> **M1 체화 핵심**
> ① `baseline과 회복 시간을 함께 설명해야 할 때` → $k_{in}/k_{out}$ turnover 구조가 결정
> ② `level 변화와 time-scale 변화를 구분할 때` → $k_{out}$ 변화가 level과 접근 시간을 동시에 지배
> ⚡ `predose 값을 고정 baseline으로 처리` → $R_0$ variability와 recovery 해석이 residual error로 흡수될 수 있음


---


<!-- SLIDE_START: M2 | title: Protein/Antibody Distinctive PK -->
## ▌ Card M2 — Protein/Antibody Distinctive PK

> **앞 카드에서 이 카드로:** target이 turnover pool이라면, ligand로 들어오는 mAb 자체도 small molecule과 다른 ADME gate를 먼저 통과해야 합니다.
> **거장의 시각**
> mAb half-life 하나로 profile을 설명하면 slow input, FcRn salvage, target-mediated sink를 terminal slope 하나에 섞게 됩니다.
> 네 가지 ADME gate로 나누면 어떤 데이터가 absorption, distribution, elimination, rescue를 가르치는지 분리됩니다.


Protein drugs와 mAbs는 small molecules와 달리 “잘 녹고 전신으로 퍼진 뒤 간/신장으로 빠지는” 물질이 아닙니다. 큰 분자량, 제한된 capillary permeability, lymphatic input, proteolysis, receptor-mediated uptake(← 수용체 결합 후 세포 내 유입), FcRn salvage(← IgG를 분해에서 회수하는 기전)가 ADME의 기본 문법입니다. [G pp.97–100; R&T pp.701–724]


### A. 형식적 정의(Formal Definition)

| 파라미터/범위 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $V_{ss}$ | L·kg⁻¹ | plasma/interstitial 중심의 제한 분포 | 분자 크기, vascular permeability, tissue access |
| MW threshold | g/mol | lymphatic route 우세 전환 기준 | 분자량 증가 |
| $F$ | fraction | sc/im 생체이용률 | injection site, proteolysis, lymphatic transit |
| $T_{max}$ | time | 느린 전신 유입의 관찰 척도 | absorption-rate limitation |
| FcRn | mechanism | IgG/mAb recycling salvage | FcRn binding, endosomal recycling |


Protein/antibody PK의 distinctive features는 다음 네 가지 게이트로 압축됩니다.

| 게이트 | 의미 | 출처 |
|---|---|---|
| Distribution gate | $V_d$가 작고 plasma/interstitial space 중심으로 제한됩니다. | Table 21-6 [R&T pp.701–702] |
| Absorption gate | sc/im 후 큰 단백질은 주로 lymphatic route로 천천히 systemic circulation에 들어갑니다. | Table 21-13 [R&T p.718] |
| Elimination gate | 작은 protein은 renal handling이 중요하고, 큰 mAb는 proteolysis/receptor-mediated pathways가 중심입니다. | [G pp.98–99; R&T pp.704–708] |
| Rescue gate | FcRn은 IgG/mAbs를 acidic endosome에서 binding 후 recycling하여 lysosomal degradation을 피하게 합니다. | Fig.21-5 [R&T p.709] |


> 💡 **느림은 단일 원인이 아님** — mAb profile의 느림은 제한 분포, 림프 입력, proteolysis/RME, FcRn rescue가 합성한 결과입니다.
> ⚠️ **헷갈림 방지:** sc 투여 terminal slope를 곧바로 elimination half-life로 읽으면 absorption-rate limitation을 놓칠 수 있습니다.
> 🔑 **게이트 판독 규칙:** terminal phase 해석 전 distribution / absorption / elimination / FcRn rescue 중 지배 후보를 먼저 적습니다.


### B. 핵심 기전(Key Mechanisms)

**Distribution**: R&T Table 21-6은 protein drugs의 $V_{ss}$가 대체로 0.04–0.23 L·kg⁻¹ 범위임을 보여 줍니다. 이는 large biologics가 body water 전체가 아니라 plasma/interstitial space에 제한된다는 해석을 뒷받침합니다. [R&T pp.701–702]

$$
\underbrace{V_{ss}}_{\text{SS 분포용적}}
\approx
\underbrace{0.04\text{--}0.23\ \mathrm{L\cdot kg^{-1}}}_{\text{제한 분포범위}}
$$


**G&W protein/antibody data anchors**: G&W는 cynomolgus monkey에 다섯 차례 연속 오름 용량(0.77–771 µmol·kg⁻¹)으로 실험용 항체를 투여한 사례를 제시하며, 단순한 central compartment 가정만으로 항체 배치(disposition)를 설명하는 것의 위험을 경고합니다. 또한 정상·신장절제 rat에서의 r-hSOD 실험을 통해 대형 protein의 낮은 $V_d$와 renal clearance 손실을 보여 줍니다. [G pp.99–100]

**Lymphatic absorption**: G&W는 sc 투여된 proteins/peptides의 absorption이 low, erratic, delayed라고 설명하고, lymph flow를 about 2 L/day로 제시합니다. R&T Table 21-13은 larger molecules $>15{,}000$–$20{,}000\ \mathrm{g/mol}$가 primarily lymphatics를 통해 systemic circulation에 들어간다고 정리합니다. [G p.97; R&T p.718]

$$
\underbrace{MW}_{\text{분자량}}
>
\underbrace{15{,}000\text{--}20{,}000\ \mathrm{g/mol}}_{\text{림프 경로역치}}
\Rightarrow
\underbrace{\mathrm{lymphatic\ input}}_{\text{느린 전신유입}}
$$


**Directionality, not extrapolated formula**: R&T Fig.21-16은 sheep에서 0.246–19 kDa 범위의 water-soluble compounds가 molecular weight 증가와 함께 lymph recovery가 증가하는 방향성을 보여 줍니다. 이것은 150 kDa mAb의 recovery를 선형식으로 정량 예측하는 근거가 아닙니다. [R&T p.720]

**Absorption-rate limitation**: Somatropin은 i.v. half-life가 약 2.1 h인데, sc 후 plasma concentration이 길게 지속됩니다. 이는 큰 단백질의 terminal profile이 elimination이 아니라 slow input에 의해 rate-limited될 수 있음을 보여 줍니다. [R&T p.721]

**Renal disease**: anakinra(17,258 g/mol)는 renal function 감소에 따라 clearance가 감소하고 exposure가 증가하는 예시입니다. 반대로 full-size antibodies와 매우 큰 proteins는 glomerular filtration을 거의 받지 않아 renal disease 영향이 일반적으로 작습니다. [R&T p.724]


### C. FcRn과 FcγR

FcRn은 endogenous IgG와 therapeutic mAbs의 long half-life를 설명하는 핵심 salvage mechanism입니다. R&T는 mAb half-life가 IgG에 가까워 approximately 21 days인 경우가 많다고 설명하지만, 이는 모든 mAb의 고정 half-life가 아닙니다. FcRn binding, target-mediated clearance, immunogenicity, dose level에 따라 apparent half-life는 달라집니다. [R&T pp.708–710]

FcγR-mediated clearance도 무시할 수 없습니다. R&T는 methotrexate가 rheumatoid arthritis patients에서 adalimumab clearance를 29–44% 감소시킬 수 있음을 제시합니다. 따라서 “FcγR은 peripheral detail”이 아니라, 특정 질환/병용약물 맥락에서는 clearance covariate가 될 수 있습니다. [R&T p.706]


### D. TMDD에 왜 중요한가

mAb의 slow absorption과 small $V_d$를 모르면 TMDD curve를 잘못 읽습니다. 왜냐하면 sc 투여에서는 Phase A의 rapid binding signature가 absorption phase와 confound될 수 있기 때문입니다. 또한 FcRn rescue가 있는 mAb에서는 “terminal slope = simple elimination half-life”라는 해석이 위험해집니다.


### E. 가정과 한계(Assumptions & Limitations)

- “mAb half-life $\approx 21$ days”는 useful prior일 수 있지만, molecule-specific FcRn binding evidence와 target-mediated clearance를 확인해야 합니다. [R&T p.708]

$$
\underbrace{t_{1/2,\mathrm{mAb}}}_{\text{mAb 겉보기 t½}}
\approx
\underbrace{21\ \mathrm{days}}_{\text{IgG식 prior}}
$$

- ADA/immunogenicity는 PK를 변화시킬 수 있으므로, unexplained clearance increase가 나타나면 target biology뿐 아니라 ADA도 점검해야 합니다. [R&T p.725]
- sc mAb $T_{max}$는 Table 21-15에서 보통 며칠 단위이며, adalimumab F=0.64, $T_{max}=5.5 days$, $t_{1/2}=30 days$; omalizumab F=0.62, $T_{max}=7.5 days$, $t_{1/2}=26 days$; efalizumab F=0.50, $t_{1/2}=17 days$로 제시됩니다. [R&T p.723]

$$
\underbrace{T_{max}}_{\text{Tmax}}
=
\underbrace{5.5\text{--}7.5\ \mathrm{days}}_{\text{느린 SC 입력}}
,\qquad
\underbrace{F}_{\text{생체이용률}}
\approx
\underbrace{0.50\text{--}0.64}_{\text{예시 범위}}
$$


### G. 제텔카스텐 원자(Zettelkasten Atom)

```text
Antibody PK = restricted distribution + lymphatic input + proteolytic/receptor-mediated elimination + FcRn salvage.
Do not read mAb half-life as a single molecule property when TMDD or slow input is active.
```


**M2 recap**: mAb PK의 느림은 단일 half-life 숫자가 아니라, tissue access, lymphatic transit, FcRn recycling, target/receptor-mediated sink가 합쳐진 결과입니다.

---


> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** 그림과 practice brief에서는 terminal slope를 곧바로 elimination으로 읽지 말고 네 가지 ADME gate와 FcRn recycling을 먼저 통과시켜라.

---


> 📊 **개념 도식 (HTML에서 렌더링):** 단백질/항체 PK(Protein/Antibody PK) 네 가지 게이트 지도 — 단백질/항체 PK(Protein/antibody PK)는 제한적 분포(restricted distribution), 림프 경로 입력(lymphatic input), 분자 크기 의존적 소실(size-dependent elimination), FcRn rescue가 합쳐져 형성됩니다.


> 📖 **교과서 그림 참조:** Rowland & Tozer 5e, p.709, Fig.21-5
> FcRn salvage는 단순히 긴 half-life를 설명하는 라벨이 아니라 recycling mechanism입니다. 이 그림은 IgG/mAbs가 어떻게 degradation을 피하고 circulation으로 되돌아가는지를 보여 줍니다.
> 확인 시점: Card M2를 읽은 뒤 확인하면 됩니다.


> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** TMDD Phase A–D는 시간표가 아니라 ligand가 $R_0$, $K_m$, $K_d$ 경계를 지나며 clearance route를 바꾸는 농도 지도다.

---

> **M2 체화 핵심**
> ① `sc/im mAb profile이 길게 이어질 때` → lymphatic input과 absorption-rate limitation이 결정
> ② `mAb half-life를 고정값처럼 해석할 때` → FcRn, target-mediated clearance, ADA가 다른 해석을 지배
> ⚡ `terminal slope = elimination half-life` → slow input 또는 FcRn/target 효과를 놓쳐 TMDD curve 판독 실패


---


<!-- SLIDE_START: M3 | title: TMDD 4-Phase Concentration-Time Profile -->
## ▌ Card M3 — TMDD 4-Phase Concentration-Time Profile

> **앞 카드에서 이 카드로:** mAb ADME gate를 통과한 profile이라도 target 결합이 개입하면 곡선은 시간표가 아니라 농도 영역 지도가 됩니다.
> **거장의 시각**
> Phase A–D를 시간 순서로 외우면 low-dose curve가 가르치는 saturation boundary를 놓칩니다.
> concentration hierarchy로 읽으면 보이는 phase가 곧 식별 가능한 mechanism이라는 판단 기준이 생깁니다.


TMDD curve는 “비선형 곡선”이 아닙니다. **ligand concentration이 target concentration, $K_d$, $K_m$, saturation boundary를 지나갈 때 dominant clearance route가 바뀌는 기록**입니다. 따라서 Phase A–D는 단순 시간 구간이 아니라 concentration hierarchy다. [G pp.604–610; R&T pp.711–712]


### A. 형식적 정의(Formal Definition)

| 파라미터/기준 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $C_L$ | concentration | ligand concentration | dose, distribution, clearance, binding |
| $R_0$ | concentration/amount | baseline target level | turnover, disease target burden |
| $K_m$ | concentration | apparent saturation boundary | binding + complex sink |
| $K_d$ | concentration | binding/dissociation boundary | $k_{off}/k_{on}$ |
| Phase A–D | regime | dominant clearance route 변화 | concentration crossing thresholds |


PK27과 R&T는 characteristic TMDD profile을 네 phase로 설명합니다. [G p.610; R&T p.712]

**PK27 dose anchor**: PK27의 full-TMDD 시범은 단클론 항체를 1.5, 5, 15, 45 mg·kg⁻¹로 급속 정맥 주사한 실험입니다. 이것이 용량별 층화 곡선 판독이 장식이 아닌 핵심인 이유입니다. [G pp.602–603]

| 단계 | 지배적 과정 | 해석 |
|---|---|---|
| A | 빠른 2차 결합(rapid second-order binding) | ligand와 target이 빠르게 평형에 도달 |
| B | 느린 1차 배치(slow first-order disposition) | target 경로 포화; 비특이적 경로 지배 |
| C | 혼합차수 배치(mixed-order disposition) | target 부분 포화; 선형과 target-mediated 경로 공존 |
| D | $k_{off}$와 $k_{e(RL)}$ 주도 말기상(terminal phase) | 매우 낮은 ligand; target-specific 제거 가시화 |


> 💡 **Phase는 농도 서명** — A–D는 시간이 아니라 ligand가 $R_0$, $K_m$, $K_d$ 경계를 지나는 방식의 기록입니다.
> ⚠️ **헷갈림 방지:** 고용량 profile만 잘 맞으면 target-mediated route가 포화되어 선형처럼 보일 수 있습니다.
> 🔑 **모델 선택 규칙:** Full TMDD와 MM을 고르기 전에 dose-stratified curve에서 실제 관찰된 phase를 먼저 표시합니다.


### B. 시간 순서가 아닌 농도 위계(Concentration Hierarchy)

초심자는 Phase A→B→C→D를 시간 순서로 읽습니다. 숙련된 모델러는 같은 곡선을 ligand concentration이 $R_0$, $K_m$, $K_d$를 차례로 지나는 concentration hierarchy로 읽습니다. PK27에서는 $R_0\approx 12\ \mathrm{mg\cdot L^{-1}}$, $K_m\approx 0.03\ \mathrm{mg\cdot L^{-1}}$이며, $K_d$는 $k_{off}/k_{on}$으로 정의됩니다. 이 역치들이 저용량 곡선이 고용량 곡선으로는 보이지 않는 기울기를 드러내는 이유입니다. [G pp.603–610]

$$
\underbrace{C_L}_{\text{ligand 농도}}
\quad\text{통과}\quad
\overbrace{\underbrace{R_0}_{\text{target 기준}},\ \underbrace{K_m}_{\text{겉보기 경계}},\ \underbrace{K_d}_{\text{결합 경계}}}^{\text{phase 전환점}}
$$


### C. 곡선이 가르치는 것

- 고용량 데이터만 관찰했다면 target-mediated route는 포화·선형으로 보일 수 있습니다.
- assay sensitivity가 낮아 저용량 데이터가 누락되면 Phase A/D가 보이지 않을 수 있습니다.
- sc absorption이 느리면 초기 rapid binding이 input kinetics에 가려질 수 있습니다.
- target·complex 데이터가 없으면 ligand-only fitting이 적합해 보여도 $k_{on}$, $k_{off}$, $k_{e(RL)}$의 정밀도는 낮은 상태로 남습니다. [G pp.603–609]


### D. 실무 판독 규칙(Practical Reading Rule)

TMDD plot은 용량별로 층화해서 점검해야 합니다. 고용량 profile은 잘 맞지만 저용량 residual이 체계적으로 편향된다면, 모델이 phantom linearity를 가지고 있을 수 있다 — 즉, 중심 profile에서는 겉보기 성공이지만 저농도 외삽에서는 편향이 숨어 있는 상태다. 이것은 PK27 MM failure에서 도출된 진단적 해석이며, 교과서가 직접 제공하는 NONMEM rule이 아닙니다. [G p.609]

### E. 한계(Limitations)

4개 phase는 풍부하고 고품질의 다용량 IV형 데이터셋에서 가장 명확하게 드러난다. 임상의 희박 샘플링, sc absorption, total vs free assay의 모호성, 또는 membrane-bound target은 phase 경계를 흐릴 수 있습니다. [G pp.604–605]


### G. 제텔카스텐 원자(Zettelkasten Atom)

```text
TMDD phases are concentration-regime signatures.
Do not choose MM or Full TMDD before asking which phases the dataset actually observes.
```


**M3 recap**: Phase A–D는 그림 설명이 아니라 model-selection checklist다. 보이는 phase가 곧 식별 가능한 mechanism입니다.

---


> 📖 **교과서 그림 참조:** Rowland & Tozer 5e, p.712, Fig.21-9; cross-check Gabrielsson & Weiner 5e, p.610, Fig.27.7
> 이 그림은 TMDD Phase A–D를 단순한 시간 구간으로 외우는 흔한 실수를 막아 줍니다. 각 phase는 target saturation 및 $K_m$/$K_d$ 경계와 연결된 concentration-regime signature로 읽어야 합니다.
> 확인 시점: Card M3를 읽은 뒤, Card M5를 읽기 전에 확인하면 됩니다.


$$
\overbrace{\mathrm{Phase\ A\to B\to C\to D}}^{\text{농도영역 서명}}
\sim
\underbrace{C_L}_{\text{ligand}}
\text{ relative to }
\underbrace{R_0,K_m,K_d}_{\text{포화/결합 기준}}
$$


> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** Full TMDD는 ligand·target·complex·sink를 한 ODE topology로 묶는다 — 관찰 species가 없으면 해당 mechanism은 추정값이 아니라 가정으로 남는다.

---

> **M3 체화 핵심**
> ① `TMDD 곡선의 phase를 읽을 때` → ligand 농도와 $R_0/K_m/K_d$ 위계가 결정
> ② `고용량 fit만 평가할 때` → 포화된 target route가 phantom linearity를 만들 수 있음
> ⚡ `Phase A–D를 시간 구간으로 암기` → low-dose/low-concentration 외삽에서 model-selection 근거 상실


---


<!-- SLIDE_START: M4 | title: Full TMDD Model -->
## ▌ Card M4 — Full TMDD Model [⚡ Apex Concept]

> **앞 카드에서 이 카드로:** Phase가 농도 영역 서명이라면, 그 서명을 만드는 ligand·target·complex·sink 항을 ODE 안에서 분리해야 합니다.
> **거장의 시각**
> 💢 **흔한 오해:** Full TMDD는 MM에 target·complex라는 생물학적 이름을 붙인 복잡한 포화 clearance 모델이라고 생각합니다.
> ✅ **실제는:** Full TMDD는 ligand disposition, target turnover, binding, complex sink를 서로 다른 state와 ODE term으로 분리합니다.
> 🎯 **체화할 단 하나의 직관:** 관찰 species가 없는 mechanism은 추정값이 아니라 가정으로 남습니다.



### [⚡ Apex Concept] Big Idea


Full TMDD는 ligand disposition, target turnover, ligand-target binding, complex loss를 하나의 mechanistic system으로 묶습니다. 즉, 하나의 ODE system(← 시간에 따른 상태변화 방정식 묶음)이 PK와 target biology를 동시에 추적합니다. PK27은 이를 “eight-parameter full TMDD model”로 부르지만, $V_c=0.05\ \mathrm{L\cdot kg^{-1}}$를 fixed한 상태에서 Table 27.2가 8 estimated parameters를 보고합니다. fixed $V_c$까지 structural quantity로 세면 ligand central, ligand tissue, target, complex의 4 state와 9 structural quantities가 존재합니다. [G pp.603, 608–609]


### A. 형식적 구조(Formal Structure)

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $L_c$ | amount/concentration scale | central ligand state | dose, CL, distribution, binding |
| $L_t$ | amount/concentration scale | tissue/peripheral ligand state | intercompartmental distribution |
| $R$ | target scale | free target/receptor | $k_{in}$, $k_{out}$, binding depletion |
| $RL$ | complex scale | ligand-target complex | $k_{on}$, $k_{off}$, $k_{e(RL)}$ |
| $V_c$ | L·kg⁻¹ | central volume fixed in PK27 | structural assumption, sensitivity target |


Full TMDD의 상태변수(state variables)는 다음 4개입니다. [G pp.604–607; R&T p.711]

| 상태변수 | 의미 |
|---|---|
| $L_c$ | ligand in central compartment |
| $L_t$ | ligand in tissue/peripheral compartment |
| $R$ | free target/receptor |
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


PK27 Table 27.2의 8 estimated/reported parameters는 $Cl$, $k_{on}$, $k_{off}$, $V_t$, $Cl_d$, $k_{out}$, $R_0$, $k_{e(RL)}$입니다. $V_c$는 $0.05\ \mathrm{L\cdot kg^{-1}}$로 fixed되었습니다. [G pp.608–609]

$$
\overbrace{\{Cl,K_{on},K_{off},V_t,Cl_d,K_{out},R_0,K_{e(RL)}\}}^{\text{PK27 8개 추정값}}
\quad ; \quad
\underbrace{V_c}_{\text{central volume}}
=
\underbrace{0.05\ \mathrm{L\cdot kg^{-1}}}_{\text{고정 구조가정}}
$$


> 💡 **Topology가 먼저** — Full TMDD의 핵심은 파라미터 수가 아니라 ligand, free target, complex, sink의 연결 구조입니다.
> ⚠️ **헷갈림 방지:** $k_{in}$은 target 생성이고 $k_{on}$은 ligand-target 결합입니다. 이 둘을 섞으면 process 자체가 달라집니다.
> 🔑 **식별성 규칙:** ligand는 disposition, target은 recovery/saturation, complex는 sink를 가르칩니다.


### B. 기전적 방정식(Mechanistic Equations)

개념적으로, 이 모델은 다음을 포함합니다:

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


결합 속도항은 $k_{on}\cdot L\cdot R$이며, $k_{in}\cdot L\cdot R$이 아닙니다. $k_{in}$은 target 합성에 속하고, $k_{on}$은 ligand-target 결합의 2차 on-rate입니다. 이 구분은 단순 표기 문제가 아니라, turnover process와 binding process를 분리하는 핵심입니다. [G p.604; G pp.606–607]

$$
\underbrace{\mathrm{BIND}}_{\text{complex 형성속도}}
=
\underbrace{k_{on}}_{\text{2차 on-rate}}
\cdot
\underbrace{L}_{\text{ligand scale}}
\cdot
\underbrace{R}_{\text{free target}}
\quad \ne \quad
\underbrace{k_{in}\cdot L\cdot R}_{\text{process 혼합}}
$$


### C. 식별가능성(Identifiability): 어떤 데이터가 어떤 항을 가르치는가

PK27은 세 데이터셋을 사용합니다: I = ligand 단독, II = ligand + target, III = ligand + target + complex. Target 및 complex 시간경과 데이터가 추가될수록 $k_{on}$, $k_{off}$, $k_{e(RL)}$의 정밀도가 개선됩니다. Table 27.2에서 $k_{on}$ CV%는 17→2→1, $k_{off}$는 27→13→3, $k_{e(RL)}$는 27→23→2로 datasets I→II→III에 걸쳐 개선됩니다. [G pp.603, 608–609]

$$
\begin{aligned}
\underbrace{CV\%(k_{on})}_{\text{kon 정밀도}} &: \underbrace{17\to2\to1}_{\text{자료 풍부도}},\\
\underbrace{CV\%(k_{off})}_{\text{koff 정밀도}} &: \underbrace{27\to13\to3}_{\text{target/complex 추가}},\\
\underbrace{CV\%(k_{e(RL)})}_{\text{sink 정밀도}} &: \underbrace{27\to23\to2}_{\text{complex 측정효과}}
\end{aligned}
$$


숙련된 모델러의 해석은 간명합니다. ligand 데이터는 nonspecific disposition과 가시적 phase 구조를 가르치고, target 데이터는 target recovery와 saturation 경계를 가르칩니다. complex 데이터는 sink 거동을 가르칩니다. 즉, 데이터의 풍부함은 장식이 아닙니다.  어떤 ODE term이 추정 가능해지는지를 결정합니다.


### D. 그럴듯한 오해(Plausible Fallacy): 기전 없는 적합 품질

**오류:** Full TMDD와 MM은 둘 다 saturable clearance를 표현하므로 high-dose fit이 좋으면 같은 모델로 보아도 된다고 판단합니다.
**왜 그럴싸한가:** 가장 높은 세 ligand profile은 reduced model에서도 상당히 잘 맞아 보일 수 있습니다.
**나비효과:** high-dose fit 신뢰 → $K_m$ 123배 과대예측을 놓침 → [임상] trough·target occupancy·subgroup low-concentration exposure 판단 실패 → [모델링/규제] low-dose residual과 외삽 근거 부족으로 sensitivity analysis 및 재분석 요구 위험 증가. [G p.609]


기존 압축 진술은 다음과 같이 유지됩니다.  reduced model은 가장 높은 세 ligand profile은 상당히 잘 맞출 수 있지만 가장 낮은 profile에서는 실패합니다. PK27에서 MM 모델은 $K_m=3.7$을 산출했지만 TMDD 모델은 $K_m=0.03$을 제시했으며, 이는 123배 과대추정에 해당합니다. 이 편향은 trough 예측, target occupancy 추정, subgroup 외삽으로 전파될 수 있습니다. 정량적 영향은 일반적 주장이 아닌, 약물·환자 집단별 sensitivity analysis로 평가해야 합니다. [G p.609]

$$
\underbrace{\frac{K_{m,\mathrm{MM}}}{K_{m,\mathrm{TMDD}}}}_{\text{MM bias}}
=
\underbrace{\frac{3.7}{0.03}}_{\text{PK27 비교}}
\approx
\underbrace{123}_{\text{123배 과대}}
$$


이 진술 위에 V5.0 Apex Edition protocol의 3분 구조로 fallacy의 mechanism을 분해합니다. [EXPERT_INFERENCE, v3]

**그럴듯한 오해**: "TMDD는 Michaelis-Menten에 생물학적 단어(target, complex, binding)만 붙인 것입니다. 따라서 Full TMDD를 쓰든 MM 근사를 쓰든, 결국 saturable clearance를 표현하는 같은 수학입니다."

**왜 틀렸는가**: MM 근사는 drug $\gg$ target 조건($L \gg R$ 또는 $L \gg K_d$에서 binding이 빠르게 quasi-equilibrium에 도달하고 target route가 지속 포화 상태)에서만 Full TMDD로부터 구조적으로 도출될 수 있습니다. Full TMDD는 binding($k_{on}\cdot L\cdot R$), drug-target complex formation ($RL$), complex internalization ($k_{e(RL)}$), target turnover($k_{in}$/$k_{out}$)를 4-state ODE로 명시적으로 인코딩합니다. 근사 조건이 위반되는 농도 범위 — 특히 ligand concentration이 $K_d$ 또는 $K_m$ 부근(target saturation 전환점)으로 떨어지는 구간과 매우 낮은 농도의 linear regime — 에서 MM 근사는 PK 거동을 구조적으로 잘못 예측합니다. PK27의 $K_m$ 0.03 vs 3.7은 이 boundary 위반의 정량적 흔적입니다. [G p.609]

**실무에서 어떻게 드러나는가**: 저용량 Phase 1 데이터에서 MM 근사 모델이 OFV·VPC 기준으로 잘 맞은 것처럼 보일 수 있습니다. 그러나 중간 용량 범위의 비선형 전환점(Phase B↔C↔D 전이)을 mechanistic하게 예측하지 못해 Phase 2 dose selection이 어긋날 수 있습니다. 또 다른 시나리오로, high-dose dataset만으로 적합된 MM이 sub-population(저체중, 고 target burden, 초기 dose interval) extrapolation에서 trough exposure를 systematic하게 잘못 예측하면, 후속 임상 의사결정의 출발점이 흔들립니다. 진단 신호는 §5 Pair 2 Critical Blow에 명시된 세 mechanism 경로(low-concentration trough 과대평가, occupancy의 fitted range 이탈, demonstrated saturation domain 외 외삽)이며, 정량 영향은 약물·환자 집단별 sensitivity analysis로 평가됩니다.


### E. NONMEM 스타일 구현 노트

[교과서 외 구현 번역 예시] 다음은 교과서의 control stream이 아닙니다. PK27/R&T ODE 구조를 NONMEM 스타일로 교육 목적으로 번역한 골격입니다.

```text
; conceptual only
CLIG = A(1)/VC
CTIS = A(2)/VT
R    = A(3)/VR_OR_SCALE
RL   = A(4)/VC

BIND = KON * CLIG * R * VC     ; amount/time scale requires volume conversion
DISS = KOFF * A(4)
SINK = KERL * A(4)

DADT(1) = INPUT - CL*CLIG - Q*(CLIG-CTIS) - BIND + DISS
DADT(2) =  Q*(CLIG-CTIS)
DADT(3) =  KIN - KOUT*A(3) - BIND + DISS
DADT(4) =  BIND - DISS - SINK
```


**Trench-level tip**: `BIND`는 `DADT`에 들어가기 전에 amount/time 단위를 가져야 합니다. 필요한 amount scale conversion 없이 $k_{on}\cdot C_L\cdot R$로 쓰면, 모델이 조용히 mass balance를 위반할 수 있습니다.


### F. 가정과 경계조건

- $V_c=0.05\ \mathrm{L\cdot kg^{-1}}$ 고정은 PK27의 고해상도 rapid-IV/고분자량 근사값이며, 범용 임상 상수가 아닙니다. [G p.608]
- free target, total target, complex assay는 모델의 state variable과 정렬되어야 합니다. assay가 partial total target을 보고하는데 모델이 free $R$을 가정하면 $R_0$와 $k_{out}$의 해석이 달라집니다.
- Full TMDD는 희박한 ligand 데이터만 존재하면 과모수화(over-parameterization)될 수 있습니다. PK26에서는 target/complex 및 $k_{on}/k_{off}/K_d$ 정보가 없어 full TMDD 적합에 실패했습니다. [G p.601]


### H. 제텔카스텐 원자(Zettelkasten Atom)

```text
Full TMDD = 4-state mechanistic system:
ligand central + ligand tissue + free target + complex.
PK27 reports 8 estimated parameters because Vc is fixed at 0.05 L·kg⁻¹.
```


**M4 recap**: Full TMDD의 핵심은 “파라미터가 많다”가 아니라, ligand curve 안에 숨어 있는 target turnover, binding, complex sink를 분리하는 것입니다.

---


> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** Full TMDD 도식과 practice는 parameter 개수보다 topology·자료 풍부도·$V_c$ 처리 방식이 식별성을 결정한다는 점을 고정한다.

---


> 📖 **교과서 그림 참조:** Rowland & Tozer 5e, p.711, Fig.21-8; cross-check Gabrielsson & Weiner 5e, p.604, Fig.27.2
> Full TMDD는 parameter-count 문제이기 전에 topology 문제입니다. 이 그림은 ligand, target, complex, binding, dissociation, sink가 어떻게 연결되는지 보여 줍니다.
> 확인 시점: Card M4를 읽은 뒤 확인하면 됩니다.


$$
\underbrace{k_{in}}_{\text{target 입력}}
\perp
\underbrace{k_{on}}_{\text{kon}},
\qquad
\underbrace{k_{off}}_{\text{koff}}
\perp
\underbrace{k_{e(RL)}}_{\text{complex 제거}}
$$


> 📊 **개념 도식 (HTML에서 렌더링):** 자료 풍부도(Data Richness) → ODE 항 식별가능성(ODE Term Identifiability) 지도 — target 및 complex 측정(assays)은 장식이 아닙니다. 숨겨진 ODE 항(ODE terms)을 분리해 줍니다.


> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** MM approximation은 Full TMDD를 접은 내삽 도구다 — $V_{max}$와 $K_m$이 편리해도 저농도 occupancy 외삽을 자동으로 허락하지 않는다.

---

> **M4 체화 핵심**
> ① `target·complex data가 함께 있을 때` → $k_{on}$, $k_{off}$, $k_{e(RL)}$ 식별성이 개선
> ② `ligand-only fit이 좋아 보일 때` → target turnover와 complex sink는 biologically learned가 아닐 수 있음
> ⚡ `fit 품질 = mechanism 타당성` → low-dose extrapolation·occupancy·subgroup 예측에서 구조적 실패


---


<!-- SLIDE_START: M5 | title: Michaelis-Menten Approximation Boundary -->
## ▌ Card M5 — Michaelis-Menten Approximation Boundary

> **앞 카드에서 이 카드로:** Full TMDD topology가 명확해지면, 이제 어떤 조건에서 그 topology를 MM 항 하나로 접어도 되는지를 판단해야 합니다.
> **거장의 시각**
> MM을 단순하고 안전한 대체 모델로 읽으면 reduced model이 허용되는 농도·occupancy 경계를 놓칩니다.
> MM을 Full TMDD의 접힌 형태로 보면 관찰된 포화 domain 안에서만 방어 가능한 내삽 도구라는 위치가 분명해집니다.


Michaelis-Menten approximation은 Full TMDD의 target/complex subsystem을 $V_{max}$와 $K_m$로 줄이는 것입니다. 즉, $R$과 $RL$을 직접 추적하지 않고 target-mediated route를 하나의 saturable clearance term으로 접는다. 문제는 fit이 아니라 **어느 concentration/occupancy range에서 이 reduction이 구조적으로 허용되는가**입니다. [G p.609; R&T p.712]


### A. 형식적 정의(Formal Definition)

| 파라미터 | 단위 | 생물학적 의미 | 변화 원인 |
|---|---|---|---|
| $Cl_{MM}$ | clearance scale | saturable target-mediated clearance | $C$, $V_{max}$, $K_m$ |
| $V_{max}$ | amount/time | 최대 target-mediated 처리능 | target capacity, internalization capacity |
| $K_m$ | concentration | apparent half-saturation boundary | $k_{off}$, $k_{e(RL)}$, $k_{on}$ |
| $K_d$ | concentration | binding dissociation constant | $k_{off}/k_{on}$ |
| Occupancy | % | target 결합 비율 | concentration relative to binding/saturation boundary |


Reduced model은 target-mediated route를 다음 형태로 압축합니다. 여기서 압축은 단순화이지, biology가 사라졌다는 뜻이 아닙니다.

$$Cl_{MM}=\frac{V_{max}}{K_m+C}$$

$$
\overbrace{Cl_{MM}}^{\text{포화 TMDD CL}}
=
\frac{\underbrace{V_{max}}_{\text{최대 처리능}}}{\underbrace{K_m}_{\text{반포화 경계}}+\underbrace{C}_{\text{ligand 농도}}}
$$


Full TMDD에서 relevant constants are:

$$K_d=\frac{k_{off}}{k_{on}}$$

$$
\overbrace{K_d}^{\text{결합 해리상수}}
=
\frac{\underbrace{k_{off}}_{\text{해리 속도}}}{\underbrace{k_{on}}_{\text{결합 속도}}}
$$


$$K_m=\frac{k_{off}+k_{e(RL)}}{k_{on}}$$

$$
\overbrace{K_m}^{\text{겉보기 동역학상수}}
=
\frac{\overbrace{k_{off}+k_{e(RL)}}^{\text{해리+sink}}}{\underbrace{k_{on}}_{\text{결합 속도}}}
$$


$K_d$는 binding affinity에 가까운 thermodynamic dissociation constant이고, $K_m$은 complex loss까지 포함한 apparent kinetic constant입니다. [G pp.603–609; R&T pp.711–712]


> 💡 **MM은 접힌 모델** — $V_{max}/K_m$은 target biology를 제거한 것이 아니라 관찰 가능한 saturable term으로 압축한 것입니다.
> ⚠️ **헷갈림 방지:** $K_m$은 $K_d$가 아닙니다. $K_m$에는 complex sink $k_{e(RL)}$가 들어갑니다.
> 🔑 **외삽 금지 규칙:** demonstrated saturation/occupancy domain 밖에서는 high-dose fit이 좋아도 MM 외삽을 정당화하지 않습니다.


### B. MM이 작동할 수 있는 조건

MM이 적절할 수 있는 상황은 다음과 같다:

- ligand concentration이 target concentration을 크게 초과할 때;
- target occupancy가 완전 포화에 가까울 때;
- 관찰된 용량 범위가 제한적일 때;
- 목적이 저농도 외삽이 아닌, 관찰 profile 내 내삽(interpolation)일 때. [G p.609; R&T p.712]

PK26 Efalizumab은 유용한 reduced-model 앵커다. 2구획 모델에 parallel linear/MM 제거가 사용되었는데, target/complex 및 $k_{on}/k_{off}/K_d$ 정보 없이 full TMDD가 실패했기 때문입니다. 보고된 추정값은 $V_t=0.061$, $V_{max}=0.039$, $K_m=0.161$, $CL_d=0.031$, $CL_L=0.007$이었다. [G pp.599–601]

$$
\overbrace{\{V_t,V_{max},K_m,CL_d,CL_L\}}^{\text{PK26 reduced set}}
=
\underbrace{\{0.061,0.039,0.161,0.031,0.007\}}_{\text{보고 추정값}}
$$


**PK26 dose anchor**: Efalizumab의 reduced model은 single-dose i.v. bolus 데이터의 5개 정맥주사 시간경과에 적합되었으므로, 제한적 데이터의 reduced-model 앵커로 읽어야지 MM이 보편적으로 mechanistic이라는 증거로 읽으면 안 됩니다. [G pp.599–601]


### C. MM이 무너지는 지점

PK27에서 MM은 가장 높은 세 농도 profile을 비교적 잘 적합했지만, 가장 낮은 농도 profile에서는 심각한 체계적 편차를 보였습니다. 추정된 $K_m=3.7$은 TMDD 모델의 $0.03$에 비해 극적으로 과대추정되었습니다. [G p.609]

임상적 교훈은 "MM을 쓰지 말라"가 아닙니다. 교훈은 더 좁고 더 실용적이다 — **target saturation이 실증된 concentration/occupancy 범위 밖에서는 MM을 사용하지 마세요**.


### D. Occupancy 검증

약 90–95% 이상의 occupancy가 필요한 경우 단순화가 허용될 수 있습니다. occupancy가 $K_d$ 또는 biomarker 역가 이하로 떨어지면 MM이 충분하지 않을 수 있습니다. [G p.609]

$$
\underbrace{\mathrm{Occupancy}}_{\text{target 결합비율}}
\gtrsim
\underbrace{90\text{--}95\%}_{\text{고포화 영역}}
$$


실무 준칙: TMDD 가능성이 있는 mAb에 MM을 사용하는 보고서라면, 관찰된 농도 범위, target 농도 범위, 투여 간격 동안의 최소 예측 target occupancy를 명시해야 합니다. 이것은 source boundary의 구현 해석이며, 규제 기관이 직접 인용한 요건이 아닙니다.

### E. 한계(Limitations)

- MM은 $R_0$, $k_{out}$, $k_{on}$, $k_{off}$, $k_{e(RL)}$의 명시적 해석을 상실합니다.
- 고용량 또는 중심 profile만 가중되면 저농도 편향이 숨겨질 수 있습니다.
- 추가 가정 없이는 target recovery나 complex sink 질문에 답할 수 없습니다.
- QSS/QE 근사는 관련 개념이지만 이 세션의 범위에서는 다루지 않습니다; 후속 modeling 세션의 주제입니다.


### G. 제텔카스텐 원자(Zettelkasten Atom)

```text
MM approximation is acceptable only inside a demonstrated saturation/occupancy domain.
PK27 shows why good high-dose fit can coexist with low-dose structural bias.
```


**M5 recap**: MM은 빠른 실무 도구일 수 있지만, “fit이 잘 됨”과 “target biology를 올바르게 외삽함”은 같은 말이 아닙니다.

---


> 📖 **교과서 그림 참조:** Gabrielsson & Weiner 5e, p.609, Fig.27.6
> Fig.27.6은 무조건적 MM 외삽에 대한 critical blow입니다. high-dose fit은 괜찮아 보일 수 있지만, lowest-dose profile에서는 systematic deviation이 나타나고 $K_m$이 과대예측됩니다. 이 그림을 보지 않으면 학습자가 fit 품질을 mechanistic validity와 동일시하기 쉽습니다.
> 확인 시점: Card M5를 읽은 뒤 확인하면 됩니다.


> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** $k_{in}$/$k_{out}$, Full TMDD/MM, $K_d$/$K_m$, low/high linearity를 섞으면 좋은 fit이 잘못된 mechanism을 가리는 함정이 된다.

---

> **M5 체화 핵심**
> ① `관찰된 포화 범위 안에서 interpolation할 때` → MM approximation이 실무적으로 방어 가능
> ② `저농도 trough·recovery·occupancy 외삽을 할 때` → Full TMDD 또는 추가 데이터가 지배
> ⚡ `high-dose fit이 좋으니 MM이 충분` → PK27처럼 $K_m$ 과대예측과 low-dose structural bias 발생


---


<!-- SLIDE_START: §5 | title: Confusion Pair Dissection -->
# §5 Confusion Pair Dissection


## ▌ Pair 1 — Turnover Rate ($k_{in}$) vs Fractional Turnover Rate ($k_{out}$)

| 비교 기준 | 개념 A: $k_{in}$ | 개념 B: $k_{out}$ |
|---|---|---|
| 단위 / 차원 | mass/time | time⁻¹ |
| 수식 내 위치 (분자/분모/지수) | $A_0=k_{in}/k_{out}$의 분자 | $A_0=k_{in}/k_{out}$의 분모, $t_t=1/k_{out}$의 분모 |
| 변화 원인 (생물학적/병적) | 합성·입력 증가/감소 | catabolism·degradation·turnover 속도 변화 |
| 혼동 시 임상 결과 | level 상승만 보고 time scale 변화로 오해 | level과 recovery time 변화를 놓쳐 target recovery 해석 실패 |



| 혼동 | 교정 |
|---|---|
| $k_{in}$과 $k_{out}$을 둘 다 “rate”로만 기억합니다. | $k_{in}$은 mass/time인 input이고, $k_{out}$은 time⁻¹인 fractional loss입니다. |
| $k_{in}$ 증가와 $k_{out}$ 감소가 둘 다 concentration 증가라서 같다고 생각합니다. | $k_{in}$ 변화는 level만, $k_{out}$ 변화는 level과 time scale을 함께 바꿉니다. [G p.97] |

$$
\underbrace{k_{in}}_{\text{mass/time 입력}}
\quad\ne\quad
\underbrace{k_{out}}_{\text{시간}^{-1}\text{분획 소실}},
\qquad
\underbrace{A_0}_{\text{level}}
=
\frac{\underbrace{k_{in}}_{\text{level 상승}}}{\underbrace{k_{out}}_{\text{level↓/시간↓}}}
$$


**Locked sentence**: $k_{in}$은 수도꼭지이고 $k_{out}$은 배수구입니다. 수위만 볼 것이 아니라 새 수위에 도달하는 시간까지 함께 보세요.

---


## ▌ Pair 2 — Full TMDD vs Michaelis-Menten Approximation ▶ **Critical Blow**

| 비교 기준 | 개념 A: Full TMDD | 개념 B: Michaelis-Menten Approximation |
|---|---|---|
| 단위 / 차원 | ligand·target·complex state를 가진 ODE system | saturable clearance term |
| 수식 내 위치 (분자/분모/지수) | $k_{on}LR$, $k_{off}RL$, $k_{e(RL)}RL$, $k_{in}/k_{out}$ 항으로 분리 | $Cl_{MM}=V_{max}/(K_m+C)$의 압축항 |
| 변화 원인 (생물학적/병적) | binding, target turnover, complex sink, nonspecific CL | 관찰 포화 범위와 apparent $V_{max}/K_m$ |
| 혼동 시 임상 결과 | data-rich mechanism을 식별 가능 | low-dose trough·occupancy·subgroup 외삽에서 structural bias |



| 혼동 | 교정 |
|---|---|
| Full TMDD는 복잡하고 MM은 단순한 대체 모델입니다. | MM은 Full TMDD target/complex subsystem의 reduction입니다. |
| 고용량 fit이 좋으면 MM이 충분합니다. | PK27에서는 high-dose profiles fit이 좋아도 low-dose profile에서 systematic deviation과 $K_m$ 123× bias가 발생했습니다. [G p.609] |
| target/complex assay는 있으면 좋은 부가자료입니다. | target/complex data는 $k_{on}$, $k_{off}$, $k_{e(RL)}$ precision을 개선하는 식별 자료입니다. [G p.609] |

**Locked sentence**: MM은 “작은 TMDD”가 아니라 “target biology를 $V_{max}/K_m$으로 접은 모델”입니다. 접어도 되는지는 occupancy range가 결정합니다.

**⚡ 기억 고리 (Memory Hook)** — *완전 지도 vs 단순화 지도*: [EXPERT_INFERENCE, v3]
Full TMDD는 binding on/off, complex internalization, target production/degradation을 모두 명시한 **완전 지도**입니다. MM 근사는 특정 농도 범위($L \gg R$ 또는 $L \gg K_d$의 quasi-equilibrium 영역)에서 이 복잡성을 하나의 포화곡선으로 압축한 **단순화 지도**입니다. 단순화 지도는 지도가 그려진 스케일을 벗어나면 틀린 경로를 안내합니다 — drug concentration이 $K_d$ 또는 $K_m$에 가까운 범위로 떨어지면 MM 근사 모델은 TMDD 거동을 재현할 수 없습니다. PK27의 $K_m$ 0.03 → 3.7 over-prediction이 바로 이 “지도 밖 영역”의 정량적 자국입니다.

> **▶ Critical Blow** — 이 혼동을 품고 first-in-human low-dose 외삽 또는 sub-population 외삽으로 임상 의사결정을 강행했을 때 발생하는 mechanism은 세 경로입니다: (i) low-concentration trough 농도 과대평가로 sub-therapeutic exposure를 가진 환자군이 누락되고, (ii) target occupancy가 dosing interval 동안 fitted range 밖으로 떨어지는데도 검출되지 않으며, (iii) sub-population 외삽이 demonstrated saturation domain 밖에서 이루어집니다. PK27의 $K_m$ 0.03 → 3.7 over-prediction이 보여주듯, 정량 영향은 약물·환자 집단별 sensitivity analysis로 평가되어야 합니다. *(mechanism-only, source-bounded; Crucible A7과 정합)* [G p.609]

---


## ▌ Pair 3 — TMDD에서 $K_d$ vs $K_m$

| 비교 기준 | 개념 A: $K_d$ | 개념 B: $K_m$ |
|---|---|---|
| 단위 / 차원 | concentration | concentration |
| 수식 내 위치 (분자/분모/지수) | $K_d=k_{off}/k_{on}$ | $K_m=(k_{off}+k_{e(RL)})/k_{on}$ |
| 변화 원인 (생물학적/병적) | binding affinity, dissociation/on-rate | binding plus complex loss/internalization |
| 혼동 시 임상 결과 | in vitro affinity를 in vivo disposition 경계로 오독 | occupancy·saturation boundary와 sink 영향을 잘못 해석 |



| 용어 | 정의 | 의미 |
|---|---|---|
| $K_d$ | $k_{off}/k_{on}$ | ligand-target binding/dissociation equilibrium |
| $K_m$ | $(k_{off} + k_{e(RL)})/k_{on}$ | binding plus complex loss/internalization effect |

$$
\underbrace{K_d}_{\text{결합 친화도}}
=
\frac{\underbrace{k_{off}}_{\text{해리}}}{\underbrace{k_{on}}_{\text{결합}}},
\qquad
\underbrace{K_m}_{\text{disposition}}
=
\frac{\underbrace{k_{off}}_{\text{해리}}+\underbrace{k_{e(RL)}}_{\text{complex sink}}}{\underbrace{k_{on}}_{\text{결합}}}
$$


$K_d$와 $K_m$이 다를 수밖에 없는 이유는 $K_m$에 $k_{e(RL)}$가 포함되기 때문입니다. 보고서 작성 시, in vitro thermodynamic $K_d$와 in vivo model에서 도출된 apparent $K_m$은 반드시 분리해야 합니다. 두 값을 모두 "affinity"로 부르면 내부 혼동과 reviewer 입장에서의 불일치가 생기기 쉽습니다. [G pp.603–609; R&T pp.711–712]

**Locked sentence**: $K_d$는 결합의 언어이고, $K_m$은 결합 이후 sink까지 포함한 disposition의 언어입니다.

**⚡ 기억 고리 (Memory Hook)** — *친화력 vs 처리 속도*: [EXPERT_INFERENCE, v3]
$K_d=k_{off}/k_{on}$은 ligand와 target의 **결합 친화력** — 얼마나 단단히 붙는가. $K_m=(k_{off}+k_{e(RL)})/k_{on}$은 결합 친화력에 complex의 **처리 속도(internalization)**까지 더한 apparent kinetic constant입니다. 그리고 이 둘과 또 다른 차원에 있는 것이 target turnover($k_{in}$/$k_{out}$) — target 자체가 **얼마나 빨리 새로 만들어지고 분해되는가**라는 system capacity입니다. 친화력이 높아도 target이 빠르게 재생성되면 낮은 농도에서도 비선형성이 지속되고, 친화력이 낮아도 turnover가 느리면 포화가 오래 유지됩니다. 세 파라미터($K_d$, $K_m$, target turnover)가 서로 독립적이므로, in vitro $K_d$ 하나만으로 in vivo TMDD의 임상적 중요성을 판단할 수 없습니다.

---


## ▌ Pair 4 — 저농도 Linear PK vs 고농도 Linear PK

| 비교 기준 | 개념 A: 저농도 Linear PK | 개념 B: 고농도 Linear PK |
|---|---|---|
| 단위 / 차원 | low-concentration regime | high-concentration saturated regime |
| 수식 내 위치 (분자/분모/지수) | target-specific route가 다시 드러나는 영역 | target route saturation으로 nonspecific linear CL처럼 보이는 영역 |
| 변화 원인 (생물학적/병적) | $C$가 $K_d/K_m$ 부근 또는 이하로 감소 | ligand가 target을 크게 초과 |
| 혼동 시 임상 결과 | trough·washout·occupancy 외삽 실패 | high-dose fit을 전체 농도범위 타당성으로 과대해석 |



| 농도 영역 | 선형으로 보이는 이유 | 위험 |
|---|---|---|
| Very low ligand | target route가 포화되지 않아 비특이적·target-specific first-order route가 공존하기 때문입니다. | assay sensitivity가 낮으면 이 구간을 놓칩니다. |
| Very high ligand | target route가 포화되어 비특이적 clearance가 지배하기 때문입니다. | high-dose fit만 보고 MM/linear model을 과신합니다. |
| Middle range | target saturation이 농도에 따라 변하기 때문입니다. | nonlinear clearance가 가장 뚜렷합니다. |

**Locked sentence**: TMDD는 “선형 또는 비선형”이 아니라, concentration에 따라 두 종류의 linearity와 한 구간의 nonlinearity가 이어지는 system입니다. [G pp.604–605]

**⚡ 기억 고리 (Memory Hook)** — *고속도로 vs 병목 도로*: [EXPERT_INFERENCE, v3]
고용량에서 mAb PK가 선형으로 보이는 이유는 target이 이미 포화되어 TMDD 경로가 더 이상 약물을 추가로 흡수하지 못하고, 비특이적 제거 경로(FcRn salvage가 작동하는 IgG-like clearance)가 지배하기 때문입니다 — 이것은 **고속도로**입니다. 저용량에서 PK가 선형처럼 보이는 이유는 다릅니다. target이 포화되지 않은 상태에서 first-order target-mediated route와 nonspecific route가 함께 작동하지만, 두 first-order 경로의 합이므로 여전히 선형입니다 — 그러나 이 구간의 target route는 **병목 도로**여서, 농도가 약간만 변해도 dominant route가 바뀝니다. 두 linear regime 사이의 nonlinear transition이 임상 용량 범위 안에 걸쳐 있을 때 TMDD 모델링이 필수가 됩니다. 고용량 데이터만 보고 “linear PK”로 결론 내리면 저용량 영역의 병목 도로 거동을 놓칩니다.


**§5 recap**: 이 세션의 가장 위험한 혼동은 `fit`, `affinity`, `linearity`, `half-life` 같은 친숙한 단어가 TMDD에서는 모두 조건부 의미를 갖는다는 점입니다.

---


> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** Self-test Q1–Q5는 turnover 단위, 비대칭성, state variable, low-dose bias, $K_d$/$K_m$ 분리를 자동 회상 수준으로 고정한다.

---



<!-- SLIDE_START: §7 | title: Self-Test 능동 회상 모듈 -->
# §7 Self-Test: 능동 회상 모듈(Active Recall Module)


## Q1 (회상) ★

$A_0 = k_{in}/k_{out}$에서 $k_{in}$과 $k_{out}$의 단위는 각각 무엇입니까?

**Answer**: $k_{in}$은 mass/time, $k_{out}$은 time⁻¹입니다. $A_0$는 두 값의 ratio로 정의되는 baseline amount입니다. [G p.96]

$$
\underbrace{A_0}_{\text{baseline 양}}
=
\frac{\underbrace{k_{in}}_{\text{mass/time}}}{\underbrace{k_{out}}_{\text{시간}^{-1}}}
$$


**다음 깊이 질문**: 그렇다면 turnover time $t_t = 1/k_{out}$은 임상 PK에서 어떤 측정 가능한 양과 같은가? (M1의 Eq.2:243이 답을 가지고 있습니다.)

---


## Q2 (회상) ★★

왜 $k_{out}$ 변화는 steady-state level과 time-to-steady-state를 동시에 바꾸는가?

**Answer**: $k_{out}$은 fractional loss rate이므로 baseline $A_0=k_{in}/k_{out}$와 time scale $t_t=1/k_{out}$에 동시에 들어갑니다. [G pp.96–97]

$$
\underbrace{A_0}_{\text{SS level}}
=
\frac{k_{in}}{\underbrace{k_{out}}_{\text{level/시간 동시}}},
\qquad
\underbrace{t_t}_{\text{교체 시간}}
=
\frac{1}{\underbrace{k_{out}}_{\text{분획 소실}}}
$$


**다음 깊이 질문**: 이 비대칭성이 linear kinetics 가정에 의존한다면, 높은 농도에서 $k_{out}$이 사실상 saturable이 되는 경우(예: MM extension) $k_{in}$ 변화와 $k_{out}$ 변화는 어떻게 구별이 어려워집니까?

---


## Q3 (회상) ★★

Full TMDD의 4 state variables는 무엇입니까?

**Answer**: ligand central, ligand tissue/peripheral, free target $R$, ligand-target complex $RL$입니다. [G pp.604–607]

**다음 깊이 질문**: 이 4개 state 중 임상에서 직접 측정이 가장 어려운 것은 무엇이며, 그 측정 결손이 PK27 Table 27.2의 식별 위계($k_{on}$/$k_{off}$/$k_{e(RL)}$ precision)에 어떤 구조적 영향을 줍니까?

---


## Q4 (적용) ★★

mAb ligand-only data에서 high-dose profiles는 잘 맞지만 lowest dose에서 systematic under/over-prediction이 보입니다. 어떤 판단을 해야 합니까?

**Answer**: MM 또는 reduced model이 observed high-dose range에서는 interpolation을 하고 있지만, low-concentration TMDD phase를 제대로 설명하지 못할 가능성이 높습니다. 이 판단은 측정된 dose/concentration 범위에 한정되며, 외삽 영역에서는 target occupancy와 sensitivity analysis가 필요합니다. [G p.609]

**다음 깊이 질문**: low-dose extrapolation을 모델 구조 변경 없이 정당화하려면 — 예를 들어 target/complex assay 추가가 즉시 불가능한 상황에서 — 어떤 sensitivity analysis 절차를 어떤 순서로 수행해야 합니까? (M5 §D 및 Q10이 답의 단초를 가지고 있습니다.)

---


## Q5 (적용) ★★

$K_m$과 $K_d$가 다를 수밖에 없는 mechanistic 이유는 무엇입니까?

**Answer**: $K_d=k_{off}/k_{on}$은 결합/해리 equilibrium이고, $K_m=(k_{off}+k_{e(RL)})/k_{on}$은 complex irreversible loss를 포함합니다. 따라서 complex sink가 있으면 $K_m$은 thermodynamic affinity가 아니라 apparent kinetic constant가 됩니다. [G p.609; R&T p.712]

$$
\underbrace{K_d}_{\text{결합 평형}}
=
\frac{k_{off}}{k_{on}},
\qquad
\underbrace{K_m}_{\text{결합+소실}}
=
\frac{k_{off}+k_{e(RL)}}{k_{on}}
$$


**다음 깊이 질문**: in vitro SPR/BLI로 측정한 thermodynamic $K_d$와 in vivo PK fitting으로 추출한 apparent $K_m$을, 같은 후보 mAb에 대해 internal report 또는 NDA narrative에서 어떻게 명시 분리해야 reviewer 입장에서 reconciliation 요청이 발생하지 않습니까?

---


> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** Self-test Q6–Q10은 sc terminal slope, fixed $V_c$, data richness, lymph 방향성, MM low-dose 외삽을 보고서 방어문장으로 바꾼다.

---


## Q6 (적용) ★

sc mAb의 terminal slope를 보고 곧바로 elimination half-life라고 해석하면 왜 위험합니까?

**Answer**: 큰 protein은 sc/im 후 lymphatic absorption이 느리고 absorption-rate-limited profile을 보일 수 있습니다. Somatropin처럼 i.v. half-life는 짧아도 sc profile은 길게 지속될 수 있습니다. [R&T pp.718–721]

**다음 깊이 질문**: sc mAb의 terminal phase가 absorption-rate-limited인지 elimination-rate-limited인지 어떻게 구분할 수 있습니까? 어떤 추가 실험 설계 또는 데이터 비교가 결정적인 신호를 줍니까?

---


## Q7 (회상) ★★

PK27에서 $V_c=0.05\ \mathrm{L\cdot kg^{-1}}$는 어떻게 처리되었습니까?

**Answer**: $V_c$는 fixed assumption으로 사용되었고, Table 27.2는 그 외 8 estimated/reported parameters를 제시합니다. fixed $V_c$까지 structural quantity로 세면 9개를 언급할 수 있지만, “8 estimated parameters”와 구분해야 합니다. [G pp.603, 608–609]

$$
\underbrace{V_c}_{\text{central volume}}
=
\underbrace{0.05\ \mathrm{L\cdot kg^{-1}}}_{\text{fixed}},
\qquad
\overbrace{8}^{\text{추정/보고값}}
\ne
\overbrace{9}^{\text{fixed }V_c\text{ 포함 구조수량}}
$$


**다음 깊이 질문**: PK27의 $V_c=0.05\ \mathrm{L\cdot kg^{-1}}$는 healthy adult 가정에 가깝습니다. edema, severe burn, ascites, pediatric subgroup처럼 plasma volume이 의미 있게 다른 sub-population에 같은 fixed $V_c$를 적용하면, sensitivity analysis는 어떻게 설계해야 다른 파라미터(특히 $k_{on}$)의 robustness를 검증할 수 있습니까? (M4 §F가 출발점입니다.)

---


## Q8 (적용) ★

target and complex data가 추가되면 왜 $k_{on}$, $k_{off}$, $k_{e(RL)}$ precision이 좋아집니까?

**Answer**: ligand-only data는 여러 ODE term의 합성 결과만 보여 줍니다. target data는 saturation/recovery를, complex data는 sink behavior를 직접 가르치므로 해당 파라미터의 CV%가 개선됩니다. PK27 Table 27.2에서 $k_{on}$ 17→2→1, $k_{off}$ 27→13→3, $k_{e(RL)}$ 27→23→2로 개선됩니다. [G p.609]

**다음 깊이 질문**: target/complex assay가 임상에서 가용하지 않을 때 — 예를 들어 PK26 Efalizumab처럼 — 동등한 식별성을 확보할 수 있는 차선 전략이 있습니까? 어떤 조건이 충족되어야 reduced model이 정당화됩니까?

---


## Q9 (회상) ○

R&T Fig.21-16에서 얻을 수 있는 올바른 결론과 얻으면 안 되는 결론은 무엇입니까?

**Answer**: 올바른 결론은 molecular weight 증가에 따라 lymphatic recovery가 증가하는 방향성입니다. 얻으면 안 되는 결론은 0.246–19 kDa sheep data를 150 kDa mAb에 선형 외삽해 구체 recovery percentage를 계산하는 것입니다. [R&T p.720]

**다음 깊이 질문**: 150 kDa mAb의 sc lymph recovery를 정량 예측할 수 없다면, 임상 protocol 설계에서 sc absorption profile의 불확실성을 어떻게 다루는 것이 안전한가? (M2 §B의 absorption-rate-limited 메시지와 연결됩니다.)

---


## Q10 (보스 딜레마) ★★

팀이 “MM model로 OFV도 낮고 VPC도 괜찮으니 first-in-human low-dose extrapolation에 쓰자”고 주장합니다. 30초 답변은?

**Answer**: “MM은 observed dose range 안에서는 쓸 수 있지만, low-dose extrapolation은 target occupancy가 충분히 높게 유지되는지 확인해야 합니다. PK27에서는 high-dose fit이 양호해도 lowest-dose profile에서 systematic deviation이 있었고 $K_m$이 0.03에서 3.7로 123× over-predicted되었습니다. 최소한 dose-stratified residual, predicted occupancy, low-concentration sensitivity analysis를 보고 결정해야 합니다.” [G p.609]

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


**다음 깊이 질문**: 위 sensitivity analysis 결과 predicted occupancy가 dosing interval의 일부 구간에서 80% 미만으로 떨어지는 sub-group이 발견되었다고 가정해 보세요. 이 sub-group을 위해 reduced MM 모델을 그대로 유지할 것인가, Full TMDD로 전환할 것인가, 아니면 별도 covariate model로 분리할 것인가? 어떤 기준으로 결정해야 하며, 그 결정을 내부 PK report 또는 NDA narrative에서 어떻게 정당화할 것입니까? *(이것이 §8 Professional Moat의 narrative justification 능력입니다.)*


**§7 recap**: 답을 외우는 것보다 중요한 것은 “이 데이터가 어떤 phase와 어떤 ODE term을 실제로 가르치는가?”를 즉시 묻는 것입니다.

---


> 🎯 **[지금 이 슬라이드들이 존재하는 이유]** 최종 전문성은 모델을 고르는 기술이 아니라 수식·생리학·관찰 농도 범위로 Full TMDD 또는 MM 선택을 방어하는 narrative 능력이다.

---



<!-- SLIDE_START: §8 | title: 메타 프레임과 큰 그림 -->
# §8 메타 프레임과 큰 그림(Meta-Frame & Big Picture)


## A. 위치 설정(Positioning)


이 세션은 biologics pharmacometrics의 입구입니다. Small molecule PK에서는 clearance와 $V_d$를 중심으로 설명할 수 있었습니다. 그러나 mAb에서는 target biology, binding kinetics, complex sink, FcRn salvage, lymphatic input이 함께 PK 곡선의 형태를 만듭니다.

선행 지식:

```text
linear PK → Michaelis-Menten → turnover → TMDD
```

후속 지식:

```text
mAb PopPK → target occupancy simulation → QSP/PBPK → clinical pharmacology narrative
```


## B. 의존 관계와 실패 모드(Dependencies & Failure Modes)

| 건너뛰면 | 구체적 실패 |
|---|---|
| Turnover | target baseline을 predose DV로만 처리하고 $R_0/k_{out}$ interpretation을 잃습니다. |
| Protein ADME | sc mAb terminal slope를 elimination으로 오해합니다. |
| 4-phase TMDD | high-dose fit만 보고 low-dose extrapolation bias를 놓칩니다. |
| Full TMDD | target/complex data의 value를 “nice-to-have”로 오판합니다. |
| MM boundary | observed range interpolation을 clinical extrapolation으로 착각합니다. |


## C. 전문가 해석 지점(Professional Moat)

| 변화 상황 | 1차 파라미터 | → | 임상 결과 | 조치 |
|---|---|---|---|---|
| target turnover 변화 | $k_{in}$/$k_{out}$ | → | baseline·recovery·occupancy 해석 변화 | baseline scenario와 target data 확인 |
| FcRn/slow input 개입 | $F$, $T_{max}$, apparent $t_{1/2}$ | → | terminal slope 오독 | i.v. 비교 또는 dose-stratified profile 확인 |
| low-dose TMDD boundary 진입 | $K_m$, $K_d$, occupancy | → | trough·subgroup 외삽 편향 | sensitivity analysis와 Full TMDD 필요성 검토 |
| complex sink 관찰 부족 | $k_{e(RL)}$ | → | mechanism fitted but not learned | target/complex assay 또는 informative prior 검토 |


이 세션을 제대로 체화하면 두 가지 능력이 생깁니다.

1. **Mechanistic model narrative justification**: “왜 Full TMDD인가 / 왜 MM이어도 되는가 / 왜 target assay가 필요한가”를 수식, physiology, observed concentration range로 설명할 수 있습니다.
2. **Diagnostic GOF reading**: 전체 VPC가 아니라 dose-stratified residual, low-dose profile, target/complex coverage를 먼저 보고 structural misspecification을 의심할 수 있습니다.


**Trench-level diagnostic rule**: mAb TMDD dataset을 처음 받으면 전체 fit plot보다 먼저 dose-stratified plot을 만듭니다. 고용량은 맞고 저용량만 systematic하게 틀리면, “variability problem”보다 “reduced model boundary problem”을 먼저 의심합니다.


## D. 최종 확정 통합(Final Locked Synthesis)

| 후속 세션 | 이 세션에서 열리는 개념 | 이 세션 없으면 실패하는 것 |
|---|---|---|
| mAb PopPK | restricted distribution, FcRn, target-mediated clearance | terminal slope와 covariate effect 해석 |
| TMDD/QSP | ligand-target-complex ODE topology | target biology와 PK coupling 설명 |
| Target occupancy simulation | $K_d$, $K_m$, occupancy boundary | dosing interval 동안의 pharmacologic coverage 판단 |
| Biologics clinical pharmacology report | model boundary and extrapolation defense | MM/Full TMDD 선택 근거 방어 |



mAb 비선형 PK의 본질은 “항체가 크다”가 아니라, **큰 ligand가 제한된 tissue space와 lymphatic input을 거쳐 endogenous target turnover system에 들어가고, binding/complex/sink가 concentration-dependent clearance를 만든다**는 점입니다. Full TMDD는 이 과정을 분해하고, MM은 일부 조건에서만 이를 압축합니다. 모델 선택의 기준은 편의성이 아니라 dataset이 관찰한 phase와 임상 의사결정이 요구하는 extrapolation 범위입니다.

---

# v3.7 자가검증 체크리스트

| 항목 | 기준 | 결과 |
|---|---|---|
| SLIDE_START 개수 | §섹션수 + 카드수 합산 | 10개 |
| 카드당 callout 합계 ≤ 6 | 전체 카드 | ✓ |
| [E] 박스 존재 | 모든 §2 카드 | ✓ |
| [D] 거장의 시각 존재 | 모든 §2 카드 | ✓ |
| [L] 파라미터 표 존재 | Apex 카드 + 정의 수식 카드 | ✓ |
| §5 혼동 쌍 표 행 순서 고정 (4행) | §5 전체 | ✓ |
| 기호 일관성 | 첫 등장 기준 통일 | ✓ |
| PART B 흔적 없음 | 전체 | ✓ |
| 수치 anchor 보존 | Compound A 등 원본 수치 | ✓ |
| [M] 나비효과 이중 종착점 | Apex 카드 전체 | ✓ |


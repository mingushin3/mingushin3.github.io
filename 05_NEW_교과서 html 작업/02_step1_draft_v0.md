# PK/PD Mastery Protocol — Step 1 Draft v0
## Session 02: 분포의 생물학 — 막투과·분포용적·단백결합

> **Source**: Rowland & Tozer 5e Ch.4 (p.77–118) + Appendix B (p.763–765, 참조) + Appendix C (p.767–773, 보조) + Appendix D (p.775–776, 보조) / Gabrielsson & Weiner 5e Ch.2 §2.9.3–§2.9.5 (p.163–169) + PK47 (p.690–693)
> **Mode**: A-Critical
> **Image rights**: None
> **Phase**: 1 (Master's Lens Draft)

---

## Curation Map — Master's Lens First

본 세션은 "왜 약물이 혈장 밖으로 나가는가, 얼마나 나가는가, 무엇이 그 양을 결정하는가"의 **생물학적·수학적 토대**를 확립한다. 두 소스의 역할 분담은 다음과 같다.

- **R&T (Vol I)**: 막투과부터 Vd, 단백결합까지의 **생리학·임상 기전**을 체계적으로 전개. 임상 결과의 방향(high-extraction vs low-extraction, 신증후군에서 warfarin Vd 변화)을 담당.
- **G&W (Vol I) — PK47**: 단백결합의 **데이터-모델 fit**을 정량적으로 다룸. fu의 비선형성, 결합 site n과 affinity Ka의 동시 추정.

### MUST (6개 — 상한 도달)

| # | 개념 | MUST 근거 (downstream collapse test) |
|---|---|---|
| **M1** | **막투과의 결정인자** (size, lipophilicity, charge, transporters) | M2의 "perfusion vs permeability 율속" 판단은 분자가 막을 통과하는 속도를 알아야 가능. 막투과 결정인자를 모르면 어떤 약물이 perfusion-rate-limited인지 permeability-rate-limited인지 판단 불가 → MUST. |
| **M2** | **분포의 율속 단계** (perfusion- vs permeability-rate limitation) | M3의 Vd 해석은 **distribution equilibrium**이 어떻게 도달되는지의 메커니즘을 전제. PBPK 구획 설계, TDM 시 sampling time 결정이 모두 율속 단계 이해에 의존 → MUST. |
| **M3** | **분포용적의 수학 구조** (V = Vp + VTW·fu/fuT, Eq. C-13의 작은 Vd 모델) **[⚡ Apex Concept]** | M5(Kp 결정인자), M6(C vs Cu 선택), §5(Critical Blow)이 모두 V의 의미와 fu 변화 방향성에 의존. covariate 모델링(albumin → V), loading dose 결정의 토대 → MUST. |
| **M4** | **단백결합의 비선형성** (PK47: fu = 1/[1 + 1/(Cu/n[PT]) + 1/(Ka·n·[PT])]) | M6(노출 지표 선택)은 fu가 일정하다는 가정의 위반 시점을 판단해야 가능. saturable binding은 NDA 시 routine으로 검증되는 항목 → MUST. |
| **M5** | **조직결합과 Kp의 결정인자** (acidic phospholipids, transporters, Eq. 4-29) | basic drug Vd > 1000 L 현상, P-gp efflux로 인한 CSF/plasma unbound ratio < 1 등이 모두 조직-수준 메커니즘으로 설명되며, M3을 임상 데이터에 적용할 때 필수 → MUST. |
| **M6** | **노출 지표 선택: 총 vs 비결합** (C = Cu/fu, AUCu vs AUC, IND/NDA 권고) | 본 세션의 임상·규제적 정점. §5 Critical Blow 쌍(C vs Cu)의 직접 토대. Benet & Hoener [2003] 456개 약물 결론은 이 카드에서 다룸 → MUST. |

### CONTEXT (MUST 카드 내 1–2문장 처리)

| 항목 | 처리 위치 | 근거 |
|---|---|---|
| **Ionization & pH partition (App.B)** | M1 카드 내 1–2문장 | Scope Lock 강제 조건. 임상약사 PhD에게 선수지식. 약산/약염기의 막투과 시 un-ionized form만 통과한다는 원칙만 짧게 명시. |
| **림프 시스템과 macromolecule 분포** (R&T p.100–101) | M2 카드 내 짧게 | M2의 permeability-rate-limited 케이스의 **극단**으로 1–2문장. Vol I-A의 핵심 메커니즘이지만 PopPK 모델링에서는 protein drug 한정. |
| **Plasma-to-blood concentration ratio** (App.D) | M5 카드 내 1–2문장 | Cb/C = 1 + H[fu·KPBC – 1]만 명시. 간 추출비 계산(Ch.5)에서 본격 활용. |
| **Vd 범위 (3 L–40,000 L)** | M3 카드 내 예시 인용 | quinacrine, ampicillin 등 양 극단 예시. 별도 설명 불필요. |
| **조직별 perfusion rates** (Table 4-4) | M2 카드 내 표 1행 발췌 | adipose 0.025, kidney 4.0 mL/min/g 정도만. |
| **SGLT2 inhibitor 약물학적 활용** (R&T p.91–92, Fig.4-12) | 미포함 | 본 세션 학습 목표(분포 메커니즘)에서 벗어남. transporter as drug target은 별도 세션. |
| **Activated charcoal 역흡수** (R&T Table 4-3) | 미포함 | reversibility 원리의 응용으로 연관성은 있으나, Vd·단백결합·막투과 핵심에서 벗어남. |

### REJECT (Step 1에 포함하지 않음)

- Skin layer 그림 4-1 해부학적 세부 (PopPK 학습 목표 외)
- Antihistamine 1세대/2세대 비교 (P-gp 사례로 M1 또는 M5에서 1줄 언급 가능, 별도 cards 불필요)
- Toxicokinetics 정의 (G&W §2.9.5 후반, 본 세션 범위 외)
- 동물간 AUC 비교 경고 (G&W Fig.2.136 — M6의 td 카드 내 1줄로 충분)

### Apex Concept 지정

- **M3 (분포용적의 수학 구조)**.
- 근거: V = 7.5 + (7.5 + VR/fuR)·fu (Eq. C-13)는 **작은 Vd 약물에서 plasma 단백결합이 변할 때 Vd가 어떻게 응답하는지**를 정의하며, 이것이 cephalosporin 데이터(Fig. 4-25, Vd-fu intercept 7 L)와 warfarin in nephrotic syndrome 데이터(Table 4-12)를 동시에 설명한다. PhD 학습자가 가장 자주 빠지는 함정—"fu가 증가하면 unbound 농도가 증가하므로 loading dose를 조정해야 한다"—이 이 카드 안에서 정량적으로 반박된다.

### Critical Blow 지정 (§5)

- **C (총 농도) vs Cu (비결합 농도)**.
- 근거: Scope Lock 사전 지정. NDA/IND 규제 맥락(IND에서는 PPB measurement, NDA에서는 unbound·total 동시 측정 권고), Benet & Hoener [2003] 456개 약물 결론, 신증후군 warfarin 사례가 모두 이 혼동에서 비롯되는 임상·규제 실패 시나리오로 직접 연결됨.

---

## §1 — Session Header & Roadmap

### Big Idea (한 문장)

분포용적은 **물리적 부피가 아니라 비례 상수**이며, 이 상수의 값은 **plasma 단백결합 fu와 조직결합 fuT 사이의 경쟁 비율**로 결정된다 — 따라서 $V$와 $C$는 약물의 분포를 설명하지 않는다, $f_u$와 $f_{uT}$만이 설명한다.

### 개념 항법도 (Concept Navigation)

```
M1 (막투과 결정인자)
   ↓ 막을 빠르게 통과하는가?
M2 (perfusion- vs permeability-rate limitation)
   ↓ 분포 평형은 도달하는가? 도달 후 어떻게 분포하는가?
M3 (Vd의 수학 구조) [⚡ Apex]
   ↓ Vd를 지배하는 두 결합 변수는?
M4 (단백결합의 비선형성)  ←→  M5 (조직결합과 Kp)
   ↓                            ↓
        M6 (노출 지표: 총 vs 비결합)
                ↓
        §5 Critical Blow: C vs Cu
                ↓
        §7 Boss Dilemma: total 측정으로 갈 것인가, unbound 측정으로 갈 것인가?
```

### 지식 그래프 위치

**전제하는 선행 지식**:
- Session 01 (1구획 모델 IV bolus): $C(t) = (Dose/V) \cdot e^{-kt}$, $k = CL/V$. 본 세션은 이 $V$의 의미를 해부한다.
- 약산/약염기의 ionization (App.B) — Henderson-Hasselbalch 방정식. CONTEXT 처리.
- 단백질의 binding affinity (general biochemistry) — $K_a = [DP]/([D][P])$.

**바로 다음에 오는 것**:
- Ch.5 Elimination — Hepatic extraction ratio $E_H$, well-stirred model. 본 세션의 fu가 $CL_H = Q_H \cdot E_H = Q_H \cdot \frac{f_u \cdot CL_{int}}{Q_H + f_u \cdot CL_{int}}$의 분자에서 직접 등장.
- Ch.6 Multiple-Dose Regimens — Loading dose 계산 시 V가 분모에 등장. 본 세션 M3의 Apex Concept이 직결.

**이 기반에 결정적으로 의존하는 고급 도메인**:
- **PopPK covariate modeling**: $V \sim \text{albumin}$, $V \sim \text{age}$, $V \sim \text{body weight}$ 관계는 모두 M3·M4·M5의 변형.
- **PBPK**: 각 조직 구획의 $K_p$는 M5의 acidic phospholipid binding 모델로부터 mechanistic하게 계산됨 (Rodgers & Rowland method).
- **TMDD 항체 약물**: 큰 분자의 lymphatic 분포(M2 CONTEXT)와 small Vd 거동(M3 Apex)이 모두 등장.
- **TDM**: free phenytoin assay(저알부민혈증 환자), warfarin in nephrotic syndrome — 모두 M6과 §5 Critical Blow의 직접 응용.

---

## §2 — Concept Anatomy Cards

---

### M1 · 막투과의 결정인자 (Determinants of Membrane Permeability)

<!-- MASTER LENS -->
**[개념 Big Idea: 거장의 시각]**

1. **왜 치명적으로 중요한가**: 약물이 흡수되어 시스템에 들어와도, 작용 부위에 도달하지 못하면 약효는 0이다. CNS 약물 개발에서 후보 물질이 blood-brain barrier를 통과하지 못해 임상 1상에서 폐기되는 일이 매년 수십 건이며, 통과 여부는 분자량·logP·이온화도·P-gp affinity 네 변수의 결합으로 사전에 거의 결정된다.

2. **체화해야 할 단 하나의 직관**: 막투과를 "지질에 녹는가"의 **단일 변수**로 보지 말고, **"크기 × 지질친화도 × 전하 × 수송체"의 4차원 직조(weave)**로 보라. 그러면 vinblastine이 logP 2.0인데도 BBB를 통과하지 못하는 이유(P-gp 기질)와, 같은 logP 2.0의 caffeine은 자유롭게 통과하는 이유(P-gp 비기질)가 한 그림에서 설명된다.

3. **이 직관을 머릿속에 박고 아래를 읽어라**: Eq. 4-1의 단순한 형태($\text{Net rate} = P \cdot SA \cdot \Delta C_u$)는 4차원 직조가 모두 $P$ 안으로 들어간 결과이다. $P$를 **분해**할 줄 알아야 약물 개발의 첫 관문에서 살아남는다.

#### A. Formal Definition

투과성(permeability) $P$는 단위 농도 차이 당 막을 통과하는 약물의 **단위 시간·단위 표면적당 net rate**이다 (단위: cm/min). 막을 사이에 둔 두 수성구획 사이의 net rate of transport는

$$\text{Net rate of transport} = P \cdot SA \cdot (Cu_1 - Cu_2)$$
[출처: R&T 5e, Ch.4, Eq. 4-1, p.80]

여기서 $Cu_1, Cu_2$는 양쪽 비결합 농도(unbound), $SA$는 표면적이다. **bound form은 막을 통과하지 못하므로** driving force는 $Cu$이지 $C$가 아니다.

#### B. Derivation / Code Structure (Vol I 모드)

$P$를 결정하는 4개의 분자 속성:

**① 분자량 (size)**: 같은 lipophilicity에서 MW 400 → 800 g/mol로 두 배 증가 시 $P$가 약 300배 감소 (Fig. 4-3). atenolol (246 g/mol) — oral bioavailability 50%, oxytocin (1007 g/mol) — 위장관 흡수 거의 0%. 단순한 점성 효과가 아니라 **막 단단함(rigidity)에 의한 입체적 차단**.

**② 지질친화도 (n-octanol/water partition coefficient, log P)**: BBB 투과 데이터(Fig. 4-4)에서 caffeine(logP ≈ 0)부터 lomustine(logP ≈ 2)까지 약 4 log unit에 걸쳐 $P$가 단조 증가. 단, vinblastine·vincristine은 logP 1.7~1.8임에도 $P$가 100배 낮음 — P-gp 기질이기 때문.

**③ 전하 (degree of ionization)**:

CONTEXT — **pH partition hypothesis (App.B)**: 약산/약염기는 un-ionized form만 lipoidal membrane을 통과한다는 가정. 평형 시 양쪽의 un-ionized 농도는 같지만, pKa에 따라 양쪽 total 농도는 다르다 ([출처: R&T 5e, App.B, p.763–764]). pKa 7.5 이상 약산은 모든 생리 pH에서 거의 un-ionized → pH 의존성 미미. pKa 3–7.5 약산은 위장관·신세뇨관 pH 변동에 민감.

**④ 수송체 (transporter)**: 두 종류로 나뉨.
- **Equilibrating transporter (passive facilitated)**: 농도 평형은 동일, 도달 속도만 빠르게. nucleoside analogue(cytarabine, gemcitabine).
- **Concentrating transporter (active)**: ATP 의존. 농도 차를 만든다. P-gp(MDR1, ABCB1) — apical efflux, 장 흡수·간 담즙 배설·신세뇨관 분비·BBB 보호 모두 관여. SLC superfamily — 주로 uptake, ABC superfamily — 주로 efflux.

활성 수송체가 관여할 때 막 양쪽 unbound 농도 ratio는 (Eq. 4-26 [출처: R&T 5e, Ch.4, p.110]):

$$\frac{Cu_T}{Cu} = \frac{P_{uptake}}{P_{efflux}}$$

수동 확산만 있을 때 $P_{uptake} = P_{efflux} = P_{passive}$이고 $Cu_T/Cu = 1$.

#### C. Structural Necessity

Eq. 4-1이 Fick's first law의 적분형이며, 이 형태가 불가피한 수학적 이유: 농도 차에 비례하는 net flux는 (a) 분자 운동의 무작위성과 (b) 충돌 빈도가 농도에 1차 비례한다는 사실에서 직접 유도된다. 만약 $P \cdot SA \cdot \Delta C^2$ 형태였다면 두 분자가 동시에 막에 충돌해야 통과한다는 의미인데, 수동 확산에서는 이런 cooperativity가 없다.

수송체 매개 수송에서 형태가 변하는 이유: carrier의 binding site가 saturable하므로 high $C$에서 plateau에 도달 (Fig. 4-6의 transport maximum). Michaelis-Menten 형태로 수렴.

#### D. Assumptions & Boundary Conditions

- **막 양쪽 well-stirred** — boundary layer 효과 무시. 실제로는 unstirred water layer가 존재하여 small lipophilic 분자에서는 $P$가 과대 추정될 수 있음.
- **분자가 막을 변형시키지 않음** — saponins, detergents 같은 막 활성 물질은 예외.
- **수동 확산만 가정 시**: 막 양쪽 unbound 농도가 평형 시 같아짐. 활성 수송체 존재 시 위반.

#### E. Limitations

- **Eq. 4-1은 단일 막 가정**. 실제 흡수·분포는 다층 막(stratum corneum의 여러 cell layer, 장 epithelium의 apical+basolateral) 직렬. 가장 느린 층이 율속.
- **$P$는 측정 어려움**. 보통 in vitro Caco-2 monolayer 또는 PAMPA로 surrogate.
- 단순 logP 기반 예측은 **수송체 기질 여부**를 놓침. P-gp/BCRP screening이 후보 선별 단계에서 필수.

#### F. Five Cognitive Layers

| Layer | Vol I 해석 |
|---|---|
| **L1 형식적 수학** | $\text{Net rate} = P \cdot SA \cdot \Delta C_u$. $P$는 분자별·막별 상수. |
| **L2 기하학적 직관** | Fig. 4-3의 등MW 직선. 4 log unit logP 증가가 4 log unit $P$ 증가. 수직축은 log scale → permeability는 logP에 지수적이지만 plot 상으로는 선형. |
| **L3 구조적 동일성** | Ohm의 법칙: $I = V/R$. 농도 차는 voltage, $1/(P \cdot SA)$는 resistance. 직렬 막은 저항 합산. |
| **L4 생리학적 의미** | $P$는 분자가 lipid bilayer에 partition되고, bilayer를 가로지르고, 반대편 aqueous phase로 desorb하는 3단계 모두를 합친 macroscale 상수. P-gp 같은 efflux pump는 partition된 분자를 다시 lumen으로 던지므로 effective $P$를 낮춤. |
| **L5 실무 투영** | 약물 개발에서 후보 분자의 logP, MW, ionization, P-gp affinity가 모두 적정 범위(Lipinski's rule of 5 + P-gp screen)에 들어가야 함. 이를 어긴 화합물은 phase 1 진입 전 소실. |

#### G. Zettelkasten Atom

```yaml
---
aliases: [Membrane permeability, 막투과 결정인자, P_app]
tags: [pharmacometrics/distribution, biopharmaceutics/permeability, drug-design/admet]
up: "[[MOC — 분포의 생물학]]"
related: ["[[Perfusion vs Permeability rate limitation]]", "[[P-glycoprotein]]", "[[BBB]]", "[[pH partition hypothesis]]"]
source: "Rowland & Tozer 5e, Ch.4, p.77–93"
---
```

투과성 $P$는 분자량, lipophilicity (logP), 전하(degree of ionization), 수송체 기질 여부 네 변수의 결합으로 결정된다. unbound form만 막을 통과하므로 driving force는 $\Delta Cu$이지 $\Delta C$가 아니다. 같은 logP라도 P-gp 기질이면 effective $P$가 100배 이상 감소할 수 있어, BBB 투과는 logP만으로 예측 불가하다.

<!-- ANCHOR -->
> 막을 통과하는 속도가 분자별로 결정된 후, 다음 질문은 "분포 평형은 빠르게 도달하는가, 느리게 도달하는가, 무엇이 율속인가"이다 — 이것이 M2의 영역이다.

---

### M2 · 분포의 율속 단계 (Perfusion- vs Permeability-Rate Limitation)

<!-- MASTER LENS -->
**[개념 Big Idea: 거장의 시각]**

1. **왜 치명적으로 중요한가**: PopPK에서 1구획 vs 2구획 모델 결정, sampling time 설계, TDM에서 평형 도달 시점 예측, PBPK에서 각 조직의 ODE rate constant 산정 — 이 모든 의사결정이 "분포가 perfusion에 의해 율속되는가, permeability에 의해 율속되는가"의 한 질문에 의존.

2. **체화해야 할 단 하나의 직관**: 율속 단계를 **"공급(perfusion)"과 "관문(permeability)" 중 어느 줄이 더 긴가**로 보라. 둘 중 짧은 줄은 보이지 않는다 (rate-limiting step). thiopental은 perfusion이 율속(짧은 줄), penicillin into CNS는 permeability가 율속.

3. **이 직관을 머릿속에 박고 아래를 읽어라**: $k_T = (Q/V_T)/Kp_b$의 단순한 형태 뒤에는, 이 식이 **perfusion-rate-limited 가정 하에서만 성립**한다는 미세한 조건이 숨어있다. 이 조건을 놓치면 PBPK 시뮬레이션은 silently 잘못된 답을 낸다.

#### A. Formal Definition

**Perfusion-rate limitation**: 조직 막의 투과성이 충분히 커서, 조직과 emergent venous blood가 항상 평형 상태($C_V = C_T/Kp_b$). 율속은 혈류 $Q$.

**Permeability-rate limitation**: 막 투과성이 작아서, blood–tissue 평형이 도달되기 전에 blood가 빠져나감. 율속은 $P \cdot SA$.

#### B. Derivation / Code Structure (Vol I 모드)

조직 한 개를 1구획으로 보고 IV bolus 후 arterial 농도 $C_A$가 일정하게 유지된다고 가정 (Fig. 4-15).

**Perfusion-rate limited case** — 조직 농도 $C_T$의 시간 변화 (Eq. 4-7):

$$C_T(t) = Kp_b \cdot C_A \cdot (1 - e^{-k_T \cdot t})$$
[출처: R&T 5e, Ch.4, Eq. 4-7, p.97]

여기서 분포 rate constant는

$$k_T = \frac{Q/V_T}{Kp_b}$$

분포 half-life:

$$t_{1/2,\text{distribution}} = \frac{0.693 \cdot Kp_b}{Q/V_T}$$
[출처: R&T 5e, Ch.4, Eq. 4-6, p.97]

**핵심 의미**: 평형 도달 시간은 (a) 조직 perfusion rate $Q/V_T$의 역수에 비례하고, (b) **partition coefficient $Kp_b$에 정비례**한다. **친화도가 큰 조직일수록 평형이 늦게 도달한다** — 이는 직관 반대 방향. 친화도가 클수록 평형까지 더 많은 약물을 채워넣어야 하기 때문.

조직별 perfusion rate (Table 4-4 [출처: R&T 5e, p.96]):
- Lung: 10.0 mL/min/g
- Kidney: 4.0 mL/min/g
- Brain: 0.5 mL/min/g
- Adipose: 0.025 mL/min/g
- Muscle (inactive): 0.025 mL/min/g

따라서 **adipose tissue로의 분포는 muscle과 perfusion이 같은데도, 친화도($Kp_b$)가 크면 muscle보다 더 늦게 평형**. thiopental의 fat 평형은 약 3.5시간(Fig. 4-13).

**Permeability-rate limited case**: 위 식들은 성립하지 않는다. blood와 tissue cell이 분리된 별개 구획으로 modeling되어야 하며, 보통 2구획 또는 3구획 모델에서 distribution의 fast/slow phase로 등장.

CONTEXT — **림프 시스템과 macromolecule 분포** (R&T p.100–101): MW > 5000 g/mol 분자(특히 단백질 약물)는 capillary endothelium을 거의 통과 못함. 일단 interstitial space에 들어간 분자는 **lymphatic drainage**(약 1 mL/min)를 통해 systemic circulation으로 복귀. 따라서 단백질 약물의 IM/SC 흡수는 lymphatic-mediated이며 흡수 속도가 매우 느림.

#### C. Structural Necessity

왜 perfusion-rate-limited에서 $k_T$가 $Kp_b$의 역수가 아니라 분모에 들어가는가? 평형 시 organ 내 amount = $V_T \cdot Kp_b \cdot C_V$이고, 매분 조직을 떠나는 양 = $Q \cdot C_V$. 따라서 **fractional rate of leaving** = $Q/(V_T \cdot Kp_b) = (Q/V_T)/Kp_b$. 친화도가 높을수록 amount는 크고 leaving rate는 작아진다 — 분모에 등장.

#### C-2. Plausible Fallacy — 적용 안 함 (Apex Concept이 M3에 지정됨)

#### D. Assumptions & Boundary Conditions

Perfusion-rate-limited equation의 가정:
- **막이 즉각 평형**. $P \cdot SA \gg Q$. 위반 시 $k_T$ 식 무효.
- **조직 내 well-stirred**. heterogeneous tissue(예: liver의 acinar zonation)는 위반.
- **조직 결합이 linear**. saturable binding 시 $Kp_b$가 농도 의존.
- **흐름이 일정**. exercise, sepsis, cardiac failure에서 위반.

#### E. Limitations

- 두 율속의 **연속 스펙트럼**이 실제. ribitol(Fig. 4-17)은 mixed regime — 어느 한쪽 가정도 명확히 만족 안 함.
- **막 종류별 지배 변수가 다름** (Table 4-1): blood capillary는 거의 모든 작은 분자에 대해 freely permeable, BBB는 거의 모든 polar 분자에 대해 permeability-rate-limited.
- 조직 내 metabolism이 있으면 $Kp_b$ 자체가 sink 효과로 평형값이 아닌 steady-state 값.

#### F. Five Cognitive Layers

| Layer | Vol I 해석 |
|---|---|
| **L1 형식적 수학** | Eq. 4-7: $C_T(t) = Kp_b \cdot C_A \cdot (1 - e^{-k_T t})$. mono-exponential rise to plateau. |
| **L2 기하학적 직관** | Fig. 4-16의 kidney(빠름) vs brain(중간) vs fat(느림) 곡선. 평형값과 평형 도달 시간이 **별개 변수**. |
| **L3 구조적 동일성** | RC 회로 충전: $V(t) = V_\infty(1 - e^{-t/RC})$. $Kp_b$는 capacitance, $1/Q$는 resistance. |
| **L4 생리학적 의미** | thiopental가 빠르게 induction을 일으키나 짧게 작용하는 이유 — 빠른 brain perfusion으로 빠른 평형, 그리고 적당한 $Kp_b$로 곧 fat redistribution이 시작. |
| **L5 실무 투영** | PBPK 모델에서 각 organ을 perfusion-limited로 둘지 permeability-limited 2구획으로 둘지의 의사결정. polar 약물·BBB·태반은 permeability로, lipophilic 약물·muscle·heart는 perfusion으로. |

#### G. Zettelkasten Atom

```yaml
---
aliases: [Distribution rate limitation, 분포 율속, Perfusion-limited]
tags: [pharmacometrics/distribution, pbpk/structural, physiology/perfusion]
up: "[[MOC — 분포의 생물학]]"
related: ["[[Vd 수학 구조]]", "[[Kp tissue partition]]", "[[2구획 모델]]", "[[PBPK]]"]
source: "Rowland & Tozer 5e, Ch.4, p.94–101"
---
```

조직으로의 약물 분포 속도는 perfusion rate ($Q/V_T$) 또는 permeability ($P \cdot SA$) 중 작은 값에 의해 율속된다. perfusion-rate-limited 시 $k_T = (Q/V_T)/Kp_b$이며, **친화도가 큰 조직일수록 평형이 늦게** 도달한다. PBPK 구획 설계의 기본 분류 변수.

<!-- ANCHOR -->
> 분포가 어떻게 진행되는지를 알았으면, 다음은 "최종 평형 상태에서 약물이 얼마나 넓게 퍼지는가"의 정량 — 즉 **분포용적 V**의 의미이다.

---

### M3 · 분포용적의 수학 구조 (Volume of Distribution) **[⚡ Apex Concept]**

<!-- MASTER LENS -->
**[개념 Big Idea: 거장의 시각]**

1. **왜 치명적으로 중요한가**: Loading dose 계산($D_L = V \cdot C_{target}$)이 정확하지 않으면 첫 투여에서 toxicity 또는 underdose. PopPK covariate 모델링에서 V가 잘못 spec되면 BSV와 RSE가 모두 부풀고, regulatory submission에서 dose adjustment 권고가 통째로 무너진다. 신증후군 환자에서 warfarin의 V가 9.4 → 13.7 L로 변하는 현상(Table 4-12)을 fu 변화 하나로 설명할 수 있어야 NDA-grade 모델러이다.

2. **체화해야 할 단 하나의 직관**: $V$는 **부피가 아니라 비례 상수**이다 — $V \cdot C = $ amount in body. 그리고 이 비례 상수를 결정하는 것은 plasma 단백결합과 조직 결합 사이의 **경쟁 비율 $f_u/f_{uT}$**이다. $V$를 "약물이 들어간 공간"으로 보지 말고, "plasma 농도 한 단위가 body에서 몇 단위의 약물을 의미하는지의 환산 계수"로 보라.

3. **이 직관을 머릿속에 박고 아래를 읽어라**: 같은 fu 변화가 큰 V 약물(>50 L)과 작은 V 약물(<15 L)에서 **정반대 방향의 임상 결과**를 만든다는 것이 본 카드의 핵심이며, Eq. C-13의 작은 Vd 모델이 이를 정량화한다.

#### A. Formal Definition

분포용적 $V$ = 평형 시 body에 있는 약물 amount를 plasma 농도로 나눈 비례 상수 (단위: L 또는 L/kg).

$$V = \frac{\text{Amount in body at equilibrium}}{\text{Plasma drug concentration}} = \frac{A}{C}$$
[출처: R&T 5e, Ch.4, Eq. 4-8, p.102]

물리적 부피와 일치하지 않는 경우가 대부분이며, body 전체 volume(약 42 L)을 훨씬 초과할 수 있다 (quinacrine: ~50,000 L, chloroquine: ~13,000 L).

#### B. Derivation / Code Structure (Vol I 모드)

**일반 모델 (큰 Vd)**:

body를 plasma + 단일 tissue 구획으로 단순화하면 (Fig. 4-20):

$$A = V_p \cdot C + V_T \cdot Kp \cdot C$$
[출처: R&T 5e, Ch.4, Eq. 4-11, p.103]

따라서

$$V = V_p + V_T \cdot Kp$$

여러 조직으로 확장하면

$$V = V_p + \sum_i V_{T,i} \cdot Kp_i$$
[출처: R&T 5e, Ch.4, Eq. 4-13, p.104]

여기서 $Kp_i$는 i번째 조직의 tissue-to-plasma equilibrium ratio. **fu와 fuT로 다시 쓰면**:

$$Kp \approx \frac{f_u}{f_{uT}}, \quad V = V_p + V_{TW} \cdot \frac{f_u}{f_{uT}}$$
[출처: R&T 5e, Ch.4, Eq. 4-25, p.109]

여기서 $V_{TW}$는 plasma 외의 body water aqueous volume (≈ 39 L). 이 식은 V > 50 L 인 약물에 거의 정확.

**작은 Vd 모델 (App.C — V < 15 L 대 albumin 결합 약물)**:

소용적 약물에서는 $V_p$의 albumin이 extravascular space의 albumin과 분리 처리되어야 하며, App.C의 mass balance에서 (Eq. C-13):

$$V = 7.5 + \left(7.5 + \frac{V_R}{f_{uR}}\right) \cdot f_u$$
[출처: R&T 5e, App.C, Eq. C-13, p.769]

$V_R$ ≈ 27 L (cellular 영역 aqueous volume), $f_{uR}$ = cellular 영역의 fraction unbound. 7.5 L = albumin 자체의 distribution volume.

이 식의 **가장 중요한 함의**: $f_u \to 0$일 때조차 $V$는 7.5 L 아래로 떨어지지 않는다. albumin 자체의 distribution volume이 floor이다.

**Source-anchored data (Fig. 4-25, cephalosporins)**: $V$를 $f_u$에 plot했을 때 11개 cephalosporin이 거의 직선상에 놓이며, $f_u \to 0$ 외삽 시 intercept ≈ 7 L. 이는 Eq. C-13의 첫 항(7.5)과 정확히 일치 — albumin 자체가 약물을 끌고 다니는 "운반 상자"임을 데이터로 보여주는 사례.

CONTEXT — **Vd 범위 (Fig. 4-19)**: warfarin·ketoprofen ~10 L (small Vd, albumin-bound 산성 약물), erythromycin·phenytoin ~50 L (medium), digoxin ~600 L (large), quinacrine ~50,000 L (extreme).

CONTEXT — **단백질 약물의 Vd**: trastuzumab, erythropoietin 등 MW > 70,000 g/mol 분자는 capillary 통과 못함 → V ≈ 5–10 L (plasma volume + lymphatic equilibrium).

#### C. Structural Necessity

**왜 $f_u$가 분자, $f_{uT}$가 분모에 등장하는가?**

평형 시 양쪽 unbound concentration이 같다는 조건($Cu_T = Cu$):

$$Cu = f_u \cdot C, \quad Cu_T = f_{uT} \cdot C_T$$

따라서 $C_T/C = f_u/f_{uT}$. tissue 농도가 plasma보다 높아지려면 (a) plasma에 약물이 더 많이 결합 안 됨(높은 $f_u$) **또는** (b) tissue가 약물을 더 강하게 잡음(낮은 $f_{uT}$). 두 효과는 같은 방향.

#### C-2. Plausible Fallacy ⚡ (이 카드는 Apex)

**❌ 그럴싸한 오류**:

> "신증후군 환자에서 warfarin의 albumin이 절반으로 줄어 fu가 두 배가 되었으니, plasma 농도(C)도 보정해서 loading dose를 줄여야 한다."

**✅ 진실**: warfarin은 V ≈ 10 L의 small-Vd 약물이지만, 임상적으로 의미 있는 약물의 active species는 **unbound 농도 Cu**이지 total 농도 C가 아니다. Eq. C-13을 통해 보면, fu가 두 배 되면 V도 거의 두 배 가까이 증가한다 (Table 4-12: 9.4 → 13.7 L). 따라서 같은 dose를 주었을 때:

- C (total)는 V 증가로 인해 상쇄되어 **거의 변하지 않거나 약간 감소**
- Cu = fu × C는 fu 증가가 C 감소를 압도해 **소폭 증가**

하지만 큰 Vd 약물(V > 50 L)의 경우 Eq. C-13은 부적합하고 Eq. 4-25($V = V_{TW} \cdot f_u/f_{uT}$)가 적용되어, 같은 fu 증가가 V를 비례 증가시키므로 Cu = (Loading Dose)·fu/V = (Loading Dose)·fuR/VR, **즉 fu와 무관**. 이 약물군에서는 loading dose를 조정할 필요 없다.

**나비효과 — NONMEM 피팅 시그니처**:
- 만약 모델러가 V를 fu의 함수로 covariate 넣지 않고 albumin level을 직접 V에 covariate로 spec하면, large-Vd 약물에서는 spurious correlation으로 OFV가 약간 떨어지지만 BSV가 잘못 잡힌다.
- 이 오류의 GOF signature 이름: **"Albumin-V False Covariate Pattern"** — V vs albumin의 ETA scatter plot에서 약한 양의 상관, 그러나 CL vs albumin에서는 더 강한 **음의 상관**(저알부민혈증에서 fu 증가 → CL 증가). CL 쪽 covariate를 빠뜨리면 model misspecification.

#### D. Assumptions & Boundary Conditions

- **평형 도달 가정**. distribution phase 중에는 $V$가 시간 의존적. $V_{ss}$(steady-state) vs $V_\beta$(elimination phase) 구분 필요.
- **Linear binding**. saturable binding 시 $V$가 농도 의존(M4와 연결).
- **Unbound 농도가 양쪽 같음 가정**. active transport나 pH gradient(lysosomal trapping) 시 위반.
- **소용적 모델 (Eq. C-13)은 albumin-bound 산성 약물에만 적용**. basic drug는 alpha1-acid glycoprotein 결합 + acidic phospholipid tissue binding으로 작은 Vd 거의 없음.

#### E. Limitations

- $V$는 single number지만, 실제로는 **다구획 분포의 시간 가중 평균**. 2구획 모델에서 $V_1, V_{ss}, V_\beta$가 다 다름.
- $V$로부터 약물이 "어느 조직에 갔는가"는 알 수 없음. 같은 V = 100 L 약물도 muscle dominant vs adipose dominant가 가능.
- Eq. 4-25의 $f_{uT}$는 **모든 조직의 평균값**. brain만의 binding 변화는 V에 거의 반영 안 됨 (brain = body의 2%).

#### F. Five Cognitive Layers

| Layer | Vol I 해석 |
|---|---|
| **L1 형식적 수학** | $V = V_p + V_T \cdot Kp$. 일반화: $V = V_p + V_{TW} \cdot f_u/f_{uT}$. 작은 Vd: $V = 7.5 + (7.5 + V_R/f_{uR}) \cdot f_u$. |
| **L2 기하학적 직관** | Fig. 4-25의 cephalosporin 산점도 — V vs fu 직선, intercept가 albumin volume(7 L). |
| **L3 구조적 동일성** | 화학평형 partitioning: 두 phase 사이의 약물 분배는 affinity ratio로 결정. plasma protein + tissue components 사이의 multi-equilibria. |
| **L4 생리학적 의미** | $V_p$ = 3 L (plasma), $V_p \cdot R_{E/I}$ = albumin이 분포한 extravascular space. fu가 작은 약물은 albumin을 ferry로 사용해서 extravascular space로 운반됨. |
| **L5 실무 투영** | NONMEM `$THETA` 정의 시 $V$를 직접 추정할지, $V \sim f_u$ covariate model을 쓸지의 결정. PopPK NDA에서 disease state의 V 변화 mechanistic 해석. |

#### G. Zettelkasten Atom

```yaml
---
aliases: [Volume of distribution, Vd, V, 분포용적]
tags: [pharmacometrics/distribution, pk-parameters/v, popk/covariate]
up: "[[MOC — 분포의 생물학]]"
related: ["[[Plasma protein binding]]", "[[Tissue binding]]", "[[Loading dose]]", "[[Small Vd model]]"]
source: "Rowland & Tozer 5e, Ch.4, p.102–115; App.C, p.767–773"
---
```

분포용적 $V$는 부피가 아니라 비례 상수이다. $V = V_p + V_{TW} \cdot f_u/f_{uT}$로 일반화되며, **plasma 단백결합 fu와 조직 결합 fuT의 비율**이 결정한다. small-Vd 약물(V < 15 L)에서는 albumin distribution volume(~7.5 L)이 floor이며, fu 변화가 V를 비례 증가시킨다. fu만 변하고 fuT가 변하지 않으면 large-Vd 약물의 unbound 농도는 변하지 않으나, small-Vd 약물에서는 미세 변화가 있다. Loading dose 조정의 first-principle은 large-Vd 약물에서는 불필요, small-Vd narrow-therapeutic-index 약물에서는 신중 평가 필요.

<!-- ANCHOR -->
> $V$의 분자에 등장하는 fu가 농도에 따라 어떻게 변하는지가 다음 카드의 영역이다 — single binding site 모델로는 부족하며, PK47의 nonlinear binding으로 들어가야 한다.

---

### M4 · 단백결합의 비선형성 (Plasma Protein Binding Nonlinearity)

<!-- MASTER LENS -->
**[개념 Big Idea: 거장의 시각]**

1. **왜 치명적으로 중요한가**: NDA submission 시 "이 약물의 plasma protein binding은 농도 독립적인가?"가 reviewer의 standard question. 답이 "No"이면 dose-response 비선형성, time-varying CL, AUC와 dose의 비례 깨짐이 따라온다 — 모두 routine ex vivo PPB 측정으로 사전 검출 가능. fu = 1/(1 + Ka·n·[PT])의 가정이 깨지는 시점을 모델러가 모르면 phase 1에서 phase 2로 넘어가는 dose-finding이 통째로 잘못된다.

2. **체화해야 할 단 하나의 직관**: fu를 **"상수"가 아니라 "low-Cu 영역에서만 일정한 plateau"**로 보라. Cu가 1/Ka 근처에 도달하면 protein이 saturate되기 시작하고, fu는 1로 빠르게 상승 — 이때부터 total 농도 C는 unbound 농도 Cu에 nonlinear하게 응답한다.

3. **이 직관을 머릿속에 박고 아래를 읽어라**: PK47의 Eq. 47:1은 single binding site의 일반해이며, Eq. 47:3은 그 low-Cu 근사이다. **언제 어느 식이 맞는가**의 판단이 본 카드의 실무 핵심.

#### A. Formal Definition

**Fraction unbound** $f_u$ = unbound 농도를 total 농도로 나눈 비율:

$$f_u = \frac{Cu}{C}$$
[출처: R&T 5e, Ch.4, Eq. 4-17, p.105]

$f_u$는 일반적으로 농도의 함수이며, 결합 단백질 농도 [PT], affinity Ka, binding site 수 n에 의존.

#### B. Derivation / Code Structure (Vol I + Vol I-B 통합 모드)

**Single binding site mass action** (R&T Eq. 4-19):

$$f_u = \frac{1}{1 + Ka \cdot f_{up} \cdot P_t}$$

여기서 $P_t$는 total protein 농도, $f_{up}$는 occupied되지 않은 site fraction. 일반 임상 농도에서 $f_{up} \approx 1$이면

$$f_u \approx \frac{1}{1 + Ka \cdot P_t}$$

**G&W PK47 mechanistic model** (Eq. 47:1):

$$f_u = 1 - \frac{1}{1 + \frac{Cu}{n \cdot [P_T]} + \frac{1}{Ka \cdot n \cdot [P_T]}}$$
[출처: G&W 5e, PK47, Eq. 47:1, p.691]

여기서 $n$ = protein 분자당 binding site 수, $[P_T]$ = total protein 농도, $Ka$ = affinity constant, $Cu$ = unbound 농도. 이 식은 두 가지 한계 case를 가짐.

**Low Cu limit** ($Cu \ll 1/Ka$, 즉 binding이 linear):

$$f_u \approx \frac{1}{1 + Ka \cdot n \cdot [P_T]}$$
[출처: G&W 5e, PK47, Eq. 47:3, p.692]

이 영역에서 fu는 **Cu 독립**, [PT]에만 의존.

**High Cu limit** ($Cu \gg 1/Ka$, protein saturated):

$$f_u \to 1$$

total 농도 C와 unbound 농도 Cu가 평행하게 함께 증가.

**Source-anchored data — PK47 Compound 1 vs Compound 2**:
- Compound 1: $n = 2$ binding sites, $[P_T]$ = 0.3 and 50 (low/high protein experiments)
- Compound 2: $n = 4$ binding sites, $[P_T]$ = 0.1 and 10
- Compound 1 initial Ka 추정: $f_u$ = 0.15% (low Cu, $[P_T]$ = 50)일 때 Eq. 47:3에 대입:

$$0.0015 = \frac{1}{1 + 2 \cdot Ka \cdot 50}$$ 

즉 $Ka \approx 6$ concentration units [출처: G&W 5e, PK47, Eq. 47:4, p.693].

n은 보통 1~4 범위 (PK47 결론: "n commonly varies between 1 and 4"). 두 protein 농도(low + high)에서 동시 fit해야 n과 Ka의 correlation이 줄어들고 parameter precision 확보.

**총 농도 C와 Cu의 관계** (PK47 Eq. 47:2):

$$C = \frac{Cu}{f_u} = \frac{Dose\,rate / Cl_u}{1 - \frac{1}{1 + Cu/(n \cdot [P_T]) + 1/(Ka \cdot n \cdot [P_T])}}$$

이 식은 Cu가 dosing rate / unbound clearance에 의해 1차적으로 결정되고, fu가 두 농도를 잇는 nonlinear proportionality constant라는 G&W의 핵심 통찰을 형식화.

#### C. Structural Necessity

**왜 fu가 Cu에 대해 nonlinear한가?** Mass action — protein의 binding site 수는 finite하다. low Cu에서는 site가 풍부 → fu 일정. Cu가 saturation 근처에 가면 추가로 들어오는 약물이 갈 곳이 없어 unbound 비율이 증가 — 시그모이드 형태 (Fig. 47.1).

**왜 [PT]를 두 단계로 fit해야 하는가?** Eq. 47:3에서 $f_u \approx 1/(Ka \cdot n \cdot [P_T])$ — Ka와 n이 항상 곱으로 등장. 두 변수의 separate 추정은 saturation regime이 데이터에 포함되어야 가능하며, 이를 위해 high [PT]와 low [PT] 동시 측정이 필수.

#### C-2. Plausible Fallacy — 적용 안 함 (Apex는 M3)

#### D. Assumptions & Boundary Conditions

- **Single binding site class** (또는 multiple class에서 가장 강한 site 한 종류). 실제로 albumin은 site I (warfarin site), site II (diazepam site)이 동시 존재 — 이 식은 둘 중 하나가 dominant일 때만 정확.
- **Reversible, fast equilibrium** (R&T p.80: "equilibrium established within milliseconds"). irreversible covalent binding 시 위반.
- **Binding 외 다른 plasma 성분에 영향 없음**. lipoprotein binding이 albumin과 동시에 활성화되면 별도 모델 필요.
- **Free fraction in blood ($f_{ub}$)는 1 초과 가능**: blood cell uptake가 음이거나 매우 약할 때. R&T p.106 명시.

#### E. Limitations

- **In vitro [PT]가 in vivo와 다를 수 있음** — equilibrium dialysis vs ultrafiltration의 method bias.
- **Drug-drug displacement**가 여러 site에서 동시 발생할 때 단일 식으로 부족.
- **Disease state에서 [PT] 변화 + 단백질 변형(예: glycation in diabetes)** — Ka도 같이 변할 수 있음.

#### F. Five Cognitive Layers

| Layer | Vol I + I-B 해석 |
|---|---|
| **L1 형식적 수학** | Eq. 47:1 (full), Eq. 47:3 (low-Cu approximation), Eq. 47:2 (C as function of Cu and fu). |
| **L2 기하학적 직관** | Fig. 47.1의 sigmoidal curves on semilog scale — low Cu에서 plateau, 1/Ka 근처에서 inflection, high Cu에서 fu → 1. |
| **L3 구조적 동일성** | Receptor occupancy theory (Hill equation, n=1): $\theta = [L]/(K_d + [L])$. PPB는 receptor binding의 mass action analogue. |
| **L4 생리학적 의미** | albumin은 약 35–50 g/L (~600 µM), alpha1-acid glycoprotein 0.4–1.0 g/L (~15 µM). 1/Ka가 이들 protein 농도와 비교되어 saturation 시점 결정. 대부분 약물에서 therapeutic Cu < 1/Ka. |
| **L5 실무 투영** | NONMEM에서 fu를 covariate로 spec할 때 [albumin]을 explicit predictor로. nonlinear binding이 의심되면 dose level별 fu 측정 필요. NDA reviewer는 "binding linearity over therapeutic range"를 standard로 묻는다. |

#### G. Zettelkasten Atom

```yaml
---
aliases: [Plasma protein binding, fu, PPB, free fraction]
tags: [pharmacometrics/distribution, biochemistry/binding, regulatory/nda]
up: "[[MOC — 분포의 생물학]]"
related: ["[[Albumin]]", "[[Alpha1-acid glycoprotein]]", "[[Saturable binding]]", "[[Hill equation]]"]
source: "Rowland & Tozer 5e, Ch.4, p.105–108; G&W 5e, PK47, p.690–693"
---
```

Plasma fraction unbound $f_u = Cu/C$는 일반적으로 농도 의존적이다. PK47 mechanistic model: $f_u = 1 - 1/(1 + Cu/(n[P_T]) + 1/(Ka \cdot n \cdot [P_T]))$. low Cu ($Cu \ll 1/Ka$) 영역에서 $f_u \approx 1/(1 + Ka \cdot n \cdot [P_T])$로 단순화되며 Cu 독립. high Cu에서 protein saturation으로 $f_u \to 1$. high·low [PT] 동시 fit으로 Ka와 n의 separation 정확도 확보. NDA에서 binding linearity 검증은 routine.

<!-- ANCHOR -->
> plasma 쪽 fu가 명료해지면, 이제 V의 또 다른 분모인 **tissue 쪽 fuT**의 결정인자로 — basic drug의 거대한 Vd가 acidic phospholipid 결합 하나로 거의 다 설명된다는 사실이 다음 카드의 핵심이다.

---

### M5 · 조직결합과 Kp의 결정인자 (Tissue Binding and Kp Determinants)

<!-- MASTER LENS -->
**[개념 Big Idea: 거장의 시각]**

1. **왜 치명적으로 중요한가**: PBPK 모델링에서 각 organ의 $Kp$를 in silico로 예측해야 하는데, **acidic vs basic vs neutral의 분류 하나로 약 80%의 분산**이 설명된다. basic drug의 Vd > 1000 L 현상을 plasma binding으로 설명하려는 시도는 모두 실패하며, 진짜 답은 tissue acidic phospholipid binding이다(Fig. 4-24). 이를 모르면 first-in-human dose prediction에서 Vd를 한 자릿수 단위로 빗나가게 추정.

2. **체화해야 할 단 하나의 직관**: $K_p$를 결정하는 것은 **plasma와 tissue의 결합 affinity 비율**이다 — $K_p \approx f_u/f_{uT}$. fu가 0.1이고 fuT가 0.001이면 Kp = 100 — 즉 이 약물은 조직에서 plasma의 100배 농도. 이것이 Vd가 body volume을 초과하는 메커니즘.

3. **이 직관을 머릿속에 박고 아래를 읽어라**: Eq. 4-29는 transporter까지 포함한 **완전한 일반식**이며, transporter가 없을 때 4-25로 reduce된다. P-gp가 BBB에서 작용하면 brain의 $Cu_T < Cu_{plasma}$가 되는 메커니즘이 이 식 안에 있다.

#### A. Formal Definition

**Tissue-to-plasma equilibrium distribution ratio** $Kp$ = 평형 시 tissue 총 농도 / plasma 총 농도:

$$Kp = \frac{C_T}{C} = \frac{f_u}{f_{uT}} \cdot \frac{Cu_T}{Cu}$$
[출처: R&T 5e, Ch.4, Eq. 4-28, p.111]

수동 확산만 있을 때 $Cu_T = Cu$, 즉 $Kp = f_u/f_{uT}$.

#### B. Derivation / Code Structure (Vol I 모드)

**일반화된 Vd 식 (transporter 포함)** (Eq. 4-29):

$$V = V_p + V_{TW} \cdot \frac{f_u}{f_{uT}} \cdot \frac{P_{uptake}}{P_{efflux}}$$
[출처: R&T 5e, Ch.4, Eq. 4-29, p.111]

수동 확산만 있을 때 $P_{uptake} = P_{efflux} = P_{passive}$이고 식은 4-25로 reduce.

**조직별 Kp의 source — acidic phospholipid binding** (basic drugs):

Fig. 4-24 [출처: R&T 5e, p.110]: metoprolol의 Kp가 조직별 acidic phospholipid 함량과 강한 양의 상관 ($r > 0.85$). 
- liver: 4.5 mg/g phospholipid → Kp ≈ 40
- kidney: 4.8 mg/g → Kp ≈ 28
- adipose: 0.5 mg/g → Kp ≈ 2
- muscle: 1.0 mg/g → Kp ≈ 8

basic drug는 tissue의 음전하 acidic phospholipid (phosphatidylserine, phosphatidylinositol)와 ion-pair 형성. acidic drug에는 이 메커니즘이 없으므로 Vd가 작다.

**Source-anchored data — propranolol (basic, Fig. 4-23)**: 
- 6 control + 15 hepatic disease 환자에서 V ≈ 200~700 L (40 mg IV bolus 후), fu = 0.04~0.30 범위.
- $V$ vs $f_u$가 거의 직선상 — 이것은 (Eq. 4-25에서 본) $V = V_p + V_{TW} \cdot f_u/f_{uT}$ 이며 $V_{TW}/f_{uT}$가 근사 상수임을 의미.
- $f_{uT}$가 individual 간 거의 동일 (~constant tissue binding) → V의 BSV는 거의 fu의 BSV로 환원.

**Source-anchored data — thiopental in dog (Fig. 4-13)**: 25 mg/kg IV bolus 후 liver(early peak), muscle(slower rise), fat(very slow rise to dominant compartment by 3.5 hr) — 동일 약물이 perfusion과 affinity에 따라 시간 prof.이 완전히 다름.

CONTEXT — **Plasma-to-blood concentration ratio** (App.D): $C_b/C = 1 + H \cdot [f_u \cdot Kp_{BC} - 1]$. blood cell이 약물을 잡으면 ($Kp_{BC} > 1$) blood 농도가 plasma보다 높음. 간 추출비 계산(Ch.5)에서 $CL_b = CL/(C/C_b)$로 환산 필요.

CONTEXT — **Indinavir CSF/plasma ratio (Fig. 4-10)**: 800 mg q8h × 8 HIV adults에서 CSF unbound concentration이 plasma unbound의 1/10 수준. 이는 (a) BBB에서 P-gp efflux가 강하고 (b) CSF 생성 속도가 indinavir 분자의 BBB diffusion보다 빨라 sink 효과 발생하기 때문 → Eq. 4-26의 $Cu_T/Cu = P_{uptake}/P_{efflux}$가 1보다 훨씬 작음.

#### C. Structural Necessity

**왜 Kp의 mechanistic 식이 acidic phospholipid 함량으로 치환 가능한가?** Rodgers & Rowland(2005)의 분류:
- Strong base (pKa > 7, plasma에서 양전하): acidic phospholipid 결합 dominant.
- Weak base / neutral: lipid partition (logP) dominant.
- Acid: albumin (extravascular distribution) dominant.

각 약물 class는 tissue 내의 **다른 결합 상대**를 가지므로, 같은 logP라도 acid vs base의 Vd는 한 자릿수 단위로 다르다.

#### D. Assumptions & Boundary Conditions

- **Transporter 없으면 unbound 농도가 양쪽 같음**. 위반 시 Eq. 4-29의 $P_{uptake}/P_{efflux}$ 항이 1이 아님.
- **Linear tissue binding**. saturable tissue binding(예: high-dose at receptor)은 Vd의 농도 의존성 유발.
- **Tissue가 well-stirred**. liver의 acinar zonation 등 위반.
- **fuT가 모든 tissue의 평균**. brain만의 binding 변화는 V에 거의 안 보임.

#### E. Limitations

- in vivo $f_{uT}$는 직접 측정 불가. tissue homogenate에서 측정해도 실제 in vivo와 다를 수 있음.
- transporter activity는 sex·age·disease·drug interaction으로 크게 변동.
- Eq. 4-29는 single-tissue 가정의 확장 — real body는 14+ tissue로 modeling됨 (PBPK).

#### F. Five Cognitive Layers

| Layer | Vol I 해석 |
|---|---|
| **L1 형식적 수학** | $Kp = (f_u/f_{uT}) \cdot (Cu_T/Cu)$. transporter 포함: $Cu_T/Cu = P_{uptake}/P_{efflux}$. |
| **L2 기하학적 직관** | Fig. 4-24의 Kp vs acidic phospholipid 산점도 — 9 organ이 거의 직선상. |
| **L3 구조적 동일성** | Henry's law: gas dissolves in solvent에 비례. drug partitions into tissue에 acidic phospholipid 함량 비례. drug-tissue affinity = "용해도 상수". |
| **L4 생리학적 의미** | basic drug Vd > 1000 L의 mechanistic source는 acidic phospholipid에 strong binding + low fuT. P-gp는 brain·testes·placenta를 protect하여 sanctuary site 형성. |
| **L5 실무 투영** | PBPK에서 organ별 Kp를 Rodgers-Rowland 식으로 in silico 예측. drug-drug interaction 분석에서 P-gp inhibitor가 victim drug의 brain exposure를 어떻게 변화시킬지 정량. |

#### G. Zettelkasten Atom

```yaml
---
aliases: [Tissue partition coefficient, Kp, fuT, tissue binding]
tags: [pharmacometrics/distribution, pbpk/parameters, transporter/p-gp]
up: "[[MOC — 분포의 생물학]]"
related: ["[[Acidic phospholipid binding]]", "[[Rodgers-Rowland method]]", "[[P-glycoprotein]]", "[[BBB]]"]
source: "Rowland & Tozer 5e, Ch.4, p.108–111; App.D, p.775–776"
---
```

Tissue-to-plasma equilibrium ratio $Kp = f_u/f_{uT}$ (수동 확산), transporter 포함 시 $Kp = (f_u/f_{uT})(P_{uptake}/P_{efflux})$. basic drug의 거대한 Vd는 plasma 결합이 아니라 tissue acidic phospholipid 결합으로 설명되며, 조직별 Kp는 acidic phospholipid 함량에 강한 상관(Rodgers-Rowland model의 핵심). P-gp efflux가 작용하는 sanctuary site (CNS, testes)에서는 $Cu_T < Cu$.

<!-- ANCHOR -->
> 분포의 정량(V)과 기전(fu, fuT, transporter)이 모두 정리되었으면, 마지막 질문은 노출(exposure)을 측정·보고할 때 **C로 할 것인가, Cu로 할 것인가**의 임상·규제적 의사결정 — M6의 영역이다.

---

### M6 · 노출 지표의 선택: 총 농도 vs 비결합 농도 (Exposure Metrics: Total vs Unbound)

<!-- MASTER LENS -->
**[개념 Big Idea: 거장의 시각]**

1. **왜 치명적으로 중요한가**: NDA submission에서 "이 약물의 dose-response는 total AUC로 보고하는가, AUCu로 보고하는가?"의 답이 잘못되면, FDA reviewer는 "thermodynamically active species"가 잘못 정의되었다고 판단하고 deficiency letter를 발행한다. Benet & Hoener [2003]의 456개 약물 review가 결정한 결론은 "대부분 PPB 변화는 임상 결과를 바꾸지 않는다, 단 IV high-extraction narrow-therapeutic-window 약물 제외"이며, 이 예외 case를 식별하는 능력이 본 카드의 정점.

2. **체화해야 할 단 하나의 직관**: 약리학적으로 활성인 species는 **항상 unbound drug**이다. plasma protein-bound drug는 receptor에 도달하지 못한다. 따라서 "exposure"의 정의가 "약효 또는 toxicity와 인과적으로 연결된 양"이라면, **AUCu/Cmax,u가 first-principle**이고 AUC/Cmax는 그저 측정 편의를 위한 surrogate.

3. **이 직관을 머릿속에 박고 아래를 읽어라**: G&W §2.9.3–2.9.4의 핵심 도식 두 장(Fig. 2.134, 2.140, 2.141)은 이 직관을 직접 보여준다 — total 농도로 보면 dog-rat-mouse의 potency 차이가 90배인데, unbound 농도로 보면 **모두 같은 EC50 (~2 nM)**이다.

#### A. Formal Definition

**Total plasma concentration**: $C$ = bound + unbound 약물의 합 (분석 시 sample을 protein과 함께 측정).

**Unbound (free) plasma concentration**: $Cu = f_u \cdot C$ — 단백질에 결합되지 않은 fraction. equilibrium dialysis 또는 ultrafiltration으로 측정.

연결식 (G&W Eq. 2:373):
$$C = \frac{Cu}{f_u} = \frac{Dose\,rate / Cl_u}{f_u}$$
[출처: G&W 5e, Ch.2, Eq. 2:373, p.167]

여기서 $Cl_u$는 unbound clearance — 약물의 본질적 elimination 능력 측정값.

#### B. Derivation / Code Structure (Vol I + I-B 통합 모드)

**Exposure metrics 비교** (G&W Table 2.21 [출처: p.169]):
- $C_{max}$: 짧은 plasma-response equilibration에 적합 (cardiovascular effects, arrhythmia).
- $C_{ss}$: delayed concentration-response에 적합 (turnover action, irreversible enzyme inhibition).
- $C_{u,ss}$ (= $f_u \cdot C_{ss}$): inter-species PPB 차이가 클 때 — in vitro IC50와 직접 비교 가능.
- $AUC_{0-\infty}$: 통합 노출 — turnover action 또는 tissue damage cumulative.
- $t_d$: 역치 농도 초과 시간 — antibacterial T > MIC, antiarrhythmic 등.
- $AUC_d$: target 이상 면적 — turnover action에 적용.

**G&W 핵심 통찰 (Fig. 2.134, p.163)** — Compound A (F > 95%, fu = 0.05) vs Compound B (F < 5%, fu = 0.01):
- Dose-response: A가 B보다 **90배 더 potent**해 보임.
- Total concentration-response: A가 여전히 우세.
- **Unbound concentration-response: 순서 역전, B가 A보다 potent** ($EC_{u,50}$ ≈ 0.5 vs A는 더 큼).

이것이 unbound 농도의 first-principle 위치를 보여주는 결정적 demonstration.

**G&W Fig. 2.141 (p.168)** — dog-rat-mouse 동일 화합물 in vivo response curve:
- Total: 종간 potency 차이 huge (dog ~10 nM, mouse ~100 nM).
- Unbound: 모두 $EC_{u,50}$ ≈ 2 nM. **종간 PPB 차이 보정으로 본질적 potency 일치**.

**Benet & Hoener [2003] 456개 약물 review** [인용: G&W p.168]:
- 결론: "PPB 변화는 PK parameter는 변경하지만 임상 결과는 보통 변경하지 않는다."
- 예외 (dose adjustment 필요): IV 투여 + high extraction ratio + narrow therapeutic window 약물.
- Less likely 예외: 매우 빠른 K-PD equilibration을 가진 narrow-therapeutic-index oral 약물.

**규제 권고 (G&W §2.9.5, p.169)**:
- **IND 단계**: ex vivo PPB를 여러 plasma 농도, 여러 종(human 포함)에서 routine으로 측정. Drug metabolism + safety documentation에 동반.
- **NDA 단계**: 제한된 임상 연구에서 unbound + total plasma 농도 둘 다 측정. routine "good to have" sampling은 권장하지 않음 (cost-benefit 균형).

CONTEXT — **AUC만으로 종간 비교 위험** (G&W Fig. 2.136, p.164): 같은 AUC에 대해 high-Cmax-short-t1/2 vs low-Cmax-long-t1/2 두 곡선이 toxic 임계값을 넘는 시간이 완전히 다름. AUC는 shape, extent, duration 정보를 잃음.

#### C. Structural Necessity

**왜 unbound 농도가 first-principle인가?** Receptor binding은 mass action에 따른다: $\theta = [Cu]/(K_d + [Cu])$ — receptor는 plasma protein의 존재를 모르고 unbound drug만 본다. 만약 PPB가 receptor binding보다 affinity가 더 강하면 (rare case), drug는 receptor에 거의 도달하지 못함.

**왜 대부분 PPB 변화가 임상적으로 무관한가?** 위 식에서 large-Vd drug의 unbound 농도 $Cu = (\text{Dose rate})/Cl_u/f_u \cdot f_u = (\text{Dose rate})/Cl_u$ — fu가 cancel out. fu 변화는 C에 영향을 주지만 Cu에는 영향 없음 (Eq. 2:373이 그것을 직접 보여줌). 따라서 dose adjustment 불필요.

**예외 case의 구조**: IV high-extraction (E ≈ 1) 약물에서 $CL = Q_H$ (flow-limited). 이 때 $Cu = (\text{Dose rate}) \cdot f_u / CL$ — fu가 nominally cancel하지 않고 명시적으로 등장. 그러나 E ≈ 1에서도 fu 변화가 임상적으로 의미 있으려면 **narrow therapeutic window**가 동시 충족되어야 함 (Benet & Hoener 결론).

#### C-2. Plausible Fallacy — 적용 안 함 (Apex는 M3)

#### D. Assumptions & Boundary Conditions

- **약물 활성종 = unbound drug** 가정. prodrug나 active metabolite-mediated effect는 별도 처리.
- **Plasma와 site of action 사이의 빠른 equilibration**. delayed effect (turnover, indirect response)는 PK/PD 모델 필요.
- **PPB 측정 ex vivo가 in vivo 반영**. matrix effect, time-dependent binding 등 위반 가능.

#### E. Limitations

- Cu 측정은 cost·assay sensitivity 한계로 routine 어려움. 특히 highly bound drug ($f_u < 0.01$)의 Cu는 LC-MS/MS LOQ 근처.
- Cmax,u vs AUCu의 적절한 metric 선택은 PD mechanism (rapid equilibrium vs cumulative damage)에 의존.
- AUC만으로 종간 노출 비교 시 species-dependent kinetic shape 무시 (G&W Fig. 2.136).

#### F. Five Cognitive Layers

| Layer | Vol I + I-B 해석 |
|---|---|
| **L1 형식적 수학** | $C = Cu/f_u$, $AUC = AUCu/f_u$ (linear binding). non-linear binding 시 AUC와 AUCu의 관계가 dose에 따라 변화. |
| **L2 기하학적 직관** | Fig. 2.140의 두 plot — fu vs total C는 noisy, fu vs unbound Cu는 clean. fu가 농도 의존적임을 보여줄 때는 unbound 축이 정답. |
| **L3 구조적 동일성** | "Effective concentration at target"는 receptor 인근의 unbound 농도. plasma binding은 carrier protein이 약물을 운반하는 매개체 — 운반 후 receptor에서는 free form만 활성. |
| **L4 생리학적 의미** | 종간 PPB 차이 (예: 사람 알부민 vs 쥐 알부민의 affinity 차이)가 total로 보면 "다른 약물처럼" 보이게 만듦. unbound로 보면 inter-species potency가 같음 (Fig. 2.141). |
| **L5 실무 투영** | NONMEM에서 dose-Cu-effect를 covariate로 spec할지, dose-C-effect를 spec할지의 결정. fu가 covariate dependent (예: albumin)이면 후자는 model misspecification. |

#### G. Zettelkasten Atom

```yaml
---
aliases: [Total vs unbound concentration, AUCu, exposure metric, free fraction]
tags: [pharmacometrics/exposure, pk-pd/active-species, regulatory/ind-nda]
up: "[[MOC — 분포의 생물학]]"
related: ["[[Plasma protein binding]]", "[[Hepatic extraction]]", "[[Benet Hoener 2003]]", "[[High-extraction drug]]"]
source: "G&W 5e, §2.9.3–2.9.5, p.163–169; R&T 5e, Ch.4, p.107–115"
---
```

약리학적 활성 species는 **unbound drug**이다. C = Cu/fu, AUCu = AUC × fu. 종간 비교, 질병 상태에서의 PPB 변화 해석, dose-response 비선형성 검출에서 unbound 농도가 first-principle. Benet & Hoener [2003] 결론: 대부분 PPB 변화는 임상 결과를 바꾸지 않으나, IV high-extraction narrow-therapeutic-window 약물은 예외. IND 단계 ex vivo PPB routine 측정, NDA 단계 제한된 임상 연구에서 unbound + total 동시 측정이 표준 권고.

<!-- RECAP §2 -->
> **§2 종합**: 막투과(M1) → 분포 율속(M2) → 분포용적의 수학(M3, ⚡Apex) → fu 비선형성(M4) ⇄ tissue binding(M5) → 노출 지표 선택(M6). 핵심 통합 등식: $V = V_p + V_{TW} \cdot f_u/f_{uT}$ (large Vd) 또는 $V = 7.5 + (7.5 + V_R/f_{uR}) \cdot f_u$ (small Vd). C와 Cu는 fu에 의해 묶이며, 임상·규제 의사결정의 정점은 §5 Critical Blow에서 다룬다.

---

## §5 — Confusion Pair Dissection

### Confusion Pair 1: **C vs Cu (총 농도 vs 비결합 농도)** — ⚠ Critical Blow 지정

<!-- CONFUSION -->

| 비교 차원 | C (총 농도) | Cu (비결합 농도) |
|---|---|---|
| **표면적 유사성** | 둘 다 plasma에서 측정되는 약물 농도 단위 (µg/mL)이며, 같은 단위로 보고됨. routine bioanalysis는 보통 C만 측정. 이름이 비슷해 분석 보고서에서 자주 혼용. | 위와 동일. |
| **수식/코드 형태** | $C = Cu/f_u = (\text{Dose rate}/Cl_u)/f_u$ | $Cu = f_u \cdot C = \text{Dose rate}/Cl_u$ |
| **생리학적/구조적 지시체** | bound + unbound 약물의 합. plasma protein bound form은 receptor에 도달하지 못함. | receptor·enzyme·transporter에 실제 도달하는 약리학적 활성 species. mass action의 driving force. |
| **변화 방향 — 신증후군에서 albumin 50% 감소 시** | warfarin V가 9.4 → 13.7 L 증가. 같은 dose에서 C는 거의 변하지 않거나 약간 감소 (Table 4-12). | fu가 거의 두 배 증가. Cu는 미세하게 증가하거나 거의 같음 (특히 large Vd 약물). |
| **임상/모델링 결과 — 같은 dose 투여 시** | C가 "정상 범위"로 보이지만 실제로는 albumin 감소가 fu를 증가시켰을 수 있음. C 단독 보고는 노출의 의미를 잃음. | Cu가 약효·toxicity의 mechanistic predictor. covariate 모델링에서 fu 변화의 covariate(예: albumin)를 explicit하게 넣어야 model misspecification 회피. |
| **⚡ 기억 고리** | **C는 약물의 "인구조사"이고, Cu는 약물의 "유권자"이다 — 인구는 100명이라도 투표하는 사람은 fu·100명이며, 정책(약효)을 결정하는 것은 항상 후자.** plasma binding은 약물을 운반하는 carrier일 뿐, receptor 앞에서는 carrier가 떨어져 나가야 한다. |

#### ⚠ Critical Blow (치명적 타격)

> **NDA 제출에서 "이 약물의 dose-response는 total Cmax로 보고된다"고 기술한 후, 신부전 환자(albumin 감소)의 phenotype 부분군에서 dose-response 곡선이 shift하면, FDA reviewer는 다음과 같이 판단한다: (1) thermodynamically active species 정의가 잘못되었거나, (2) PopPK 모델이 fu의 covariate dependence를 빠뜨렸다. 두 경우 모두 deficiency letter 사유이며, 임상 측면에서는 narrow-therapeutic-window 환자에게 normal C 농도임에도 toxic Cu에 노출되는 사고로 직접 연결된다 — phenytoin in hypoalbuminemia, warfarin in nephrotic syndrome이 대표 사례.**

---

### Confusion Pair 2: **Perfusion-rate limitation vs Permeability-rate limitation**

<!-- CONFUSION -->

| 비교 차원 | Perfusion-rate limited | Permeability-rate limited |
|---|---|---|
| **표면적 유사성** | 둘 다 "약물이 조직에 도달하는 속도가 느리다"는 현상의 설명. PBPK 또는 multi-compartment 모델에서 distribution phase로 관찰됨. | 위와 동일. |
| **수식/코드 형태** | $k_T = (Q/V_T)/Kp_b$, $t_{1/2} = 0.693 \cdot Kp_b/(Q/V_T)$. 율속 변수는 **Q/V_T** (혈류). | $k_T \propto P \cdot SA$. 율속 변수는 **P·SA** (막 투과성·표면적). |
| **생리학적/구조적 지시체** | 막 투과는 즉각, 평형은 emergent venous blood = tissue. blood와 tissue가 한 구획으로 modeling 가능. | 막이 sink와 sink 사이의 병목. blood-membrane-tissue가 분리된 별개 구획. 2-compartment 또는 더 큰 모델 필요. |
| **변화 방향 — 혈류를 두 배로 증가 시** | distribution rate가 거의 두 배 증가. AUC vs t curve가 압축. | distribution rate 거의 변화 없음. 막 통과가 율속이므로 혈류는 supply만 충분하면 그만. |
| **임상/모델링 결과** | 작은 lipophilic 약물 + muscle/heart/liver. lung perfusion 변화에 민감 (sepsis, exercise). | polar 약물 + BBB/CSF/eye/testes. P-gp inhibitor가 주는 효과의 bulk가 여기. |
| **⚡ 기억 고리** | **두 줄에 서 있는 사람을 상상하라 — 혈류 줄(공급)과 막 줄(관문). 짧은 줄(rate-limiting step)만 보이고 긴 줄은 보이지 않는다.** thiopental은 BBB를 자유로 통과(긴 막 줄) → 혈류가 율속(짧은 줄). penicillin은 BBB를 거의 통과 못함(긴 막 줄, 그러나 P-gp efflux로 효과적 음수) → 막이 율속. |

---

### Confusion Pair 3: **fu (plasma fraction unbound) vs fuT (tissue fraction unbound)**

<!-- CONFUSION -->

| 비교 차원 | fu | fuT |
|---|---|---|
| **표면적 유사성** | 둘 다 "단백질에 결합되지 않은 비율"이라는 dimensionless 값. 둘 다 V를 결정하는 변수. | 위와 동일. |
| **수식/코드 형태** | $f_u = Cu/C$ — plasma. PK47 mechanistic: $f_u = 1/(1 + Ka \cdot n \cdot [P_T])$ at low Cu. 측정 가능. | $f_{uT} = Cu_T/C_T$ — tissue. 평균값. **직접 측정 거의 불가능**. tissue homogenate로부터 inferred. |
| **생리학적/구조적 지시체** | albumin (acidic drug), $\alpha_1$-acid glycoprotein (basic drug), lipoproteins (neutral). plasma-soluble protein. | acidic phospholipid (basic drug), tissue albumin (acidic drug, App.C model), specific tissue components. tissue-bound. |
| **변화 방향 — V에 미치는 효과** | $V = V_p + V_{TW} \cdot f_u/f_{uT}$ — fu 증가 시 V 증가 (분자에). | fuT 감소 시 V 증가 (분모에). 즉 두 변수는 **반대 방향**으로 V를 움직임. |
| **임상/모델링 결과** | 측정 가능. NDA에서 routine. covariate 모델링에서 albumin level의 surrogate. | 측정 불가능. 추론만 가능. fu 변화는 large-Vd 약물의 Cu에 영향 없음, fuT 변화는 직접 영향. |
| **⚡ 기억 고리** | **fu는 "감옥 밖"의 약물 비율(plasma의 carrier protein이 잡아둔 것에서 풀린 비율), fuT는 "탑 밖"의 약물 비율(tissue의 receptor·phospholipid에서 풀린 비율). V는 두 자유의 비율이다 — fu가 클수록 약물이 plasma에서 탈출하기 쉽고, fuT가 작을수록 약물이 tissue에 묶인다. 두 효과가 같은 방향으로 V를 증가시킨다.** |

---

### Confusion Pair 4: **Vd 작음 (V < 15 L) vs Vd 큼 (V > 50 L) — 단백결합 변화 응답**

<!-- CONFUSION -->

| 비교 차원 | Small Vd (e.g., warfarin V ≈ 10 L) | Large Vd (e.g., propranolol V ≈ 200–700 L) |
|---|---|---|
| **표면적 유사성** | 둘 다 V vs fu plot이 직선상 (Eq. C-13 또는 Eq. 4-25). 신증후군에서 둘 다 V가 변할 수 있다는 사실. | 위와 동일. |
| **수식/코드 형태** | $V = 7.5 + (7.5 + V_R/f_{uR}) \cdot f_u$ (Eq. C-13). albumin 자체의 distribution이 floor (~7.5 L). | $V \approx V_{TW} \cdot f_u/f_{uT}$ (Eq. 4-25 근사). plasma 항 무시 가능. |
| **생리학적/구조적 지시체** | 약물이 거의 albumin 위에만 머물고, intracellular space로 거의 안 들어감. 산성 약물 + 작은 분자 + albumin-bound. | 약물이 tissue 깊숙이 분포. basic drug + acidic phospholipid binding 또는 lipophilic neutral. |
| **변화 방향 — fu 두 배 증가 시 (예: 알부민 50% 감소)** | V가 거의 두 배 가까이 증가 (Eq. C-13). C는 거의 같음. **Cu는 미세하게 증가** (warfarin: V 9.4→13.7, fu 0.005→0.0077, Cu = D·fu/V → 약간 증가). | V가 fu에 비례 증가 (Eq. 4-25). 따라서 **Cu = D·fu/V는 변하지 않음** (fu가 분자·분모에 cancel). |
| **임상/모델링 결과** | narrow therapeutic index 약물(warfarin, phenytoin)에서 PPB 변화에 민감. dose adjustment 신중 평가. | 거의 모든 PPB 변화에 robust. dose adjustment 불필요 (Benet & Hoener 결론). |
| **⚡ 기억 고리** | **작은 Vd 약물에서 fu는 V의 분자에 거의 단독으로 살고, large Vd 약물에서 fu는 V의 분자와 Cu의 분자 모두에 살아 cancel된다. 작은 Vd에서는 fu가 V를 끌고 가지만 Cu는 약간만 끌고, 큰 Vd에서는 fu가 V와 Cu를 같은 비율로 끌고 가서 둘이 만난다 — 그래서 large Vd 약물의 dose adjustment가 거의 필요 없는 것이다.** |

---

## §7 — Self-Test: Active Recall Module

<!-- SELF-TEST -->

### Q1 (Recall, ★)

Eq. 4-1 ($\text{Net rate} = P \cdot SA \cdot \Delta C_u$)에서 driving force가 $\Delta C$가 아니라 $\Delta C_u$인 이유를 한 문장으로 설명하라.

<details>
<summary>📖 정답 공개</summary>

Plasma protein-bound form은 분자량이 큰 단백질에 결합되어 있어 lipoidal cell membrane을 통과할 수 없으므로, 막을 통과할 수 있는 driving force는 unbound (free) drug의 농도 차이뿐이다. bound drug는 일종의 reservoir이며, fast equilibrium 가정 하에 unbound 농도가 감소함에 따라 dissociate된다.

**다음 깊이 질문**: 만약 PPB의 dissociation rate가 막 투과 rate보다 느리면 (slow-off binding), 이 driving force 가정이 어떻게 깨지는가?

</details>

---

### Q2 (Recall, ★★ — 다음 세션 재등장)

Perfusion-rate-limited distribution에서 tissue distribution half-life의 식을 유도 없이 쓰고, **친화도가 높은 조직일수록 평형이 더 늦게 도달하는** 이유를 한 문장으로 설명하라.

<details>
<summary>📖 정답 공개</summary>

$$t_{1/2,\text{distribution}} = \frac{0.693 \cdot Kp_b}{Q/V_T}$$

친화도가 높을수록 조직이 평형 농도에 도달하기 위해 채워야 할 약물 amount가 크고, 이 amount를 공급하는 혈류는 일정하므로, **평형까지의 시간이 partition coefficient $Kp_b$에 정비례**하여 늘어난다. 직관과 반대.

**다음 깊이 질문**: 두 조직의 perfusion rate가 같다면, 친화도가 더 큰 조직과 더 작은 조직 중 어디에 약물이 더 늦게 누적되는가? 그리고 이것이 thiopental의 biphasic action(빠른 induction, 짧은 duration) 메커니즘과 어떻게 연결되는가?

</details>

---

### Q3 (Recall, ★)

분포용적의 두 가지 표현을 쓰라: (a) tissue 합으로 (b) fu와 fuT로.

<details>
<summary>📖 정답 공개</summary>

(a) $V = V_p + \sum_i V_{T,i} \cdot Kp_i$ (Eq. 4-13)
(b) $V = V_p + V_{TW} \cdot \frac{f_u}{f_{uT}}$ (Eq. 4-25, large-Vd 근사)

**다음 깊이 질문**: 이 두 식 사이의 연결은 $Kp \approx f_u/f_{uT}$이다. 이 등식이 성립하기 위한 조건 두 가지를 들라.

</details>

---

### Q4 (Application, ★★)

PK47 데이터에서 Compound 1은 fu = 0.15% at low Cu (Cu << 1/Ka), [PT] = 50 conc units, n = 2를 가진다. Eq. 47:3을 사용하여 Ka의 초기 추정값을 계산하라. (정답은 약 6 conc units이다.)

<details>
<summary>📖 정답 공개</summary>

Eq. 47:3: $f_u \approx 1/(1 + Ka \cdot n \cdot [P_T])$ → $0.0015 = 1/(1 + Ka \cdot 2 \cdot 50)$ → $1 + 100 Ka = 1/0.0015 \approx 667$ → $Ka \approx 6.66 \approx 6$ concentration units. (Note: G&W은 $f_u = 0.15$ %를 0.0015로 변환한 후 Eq. 47:3에 직접 대입하여 약 6을 얻는다.)

**다음 깊이 질문**: 이 추정값의 큰 한계는 n과 Ka가 항상 곱으로 등장한다는 것이다 — 두 파라미터를 분리 추정하기 위해 G&W는 어떤 실험 설계를 권고하는가?

</details>

---

### Q5 (Application, ★)

신증후군 환자에서 albumin이 43 → 12.5 g/L로 감소했다 (Table 4-12). warfarin의 fu가 정상 0.005인 경우 신증후군 환자에서의 fu를 추정하라 (low-Cu, $f_u \ll 1$ 가정).

<details>
<summary>📖 정답 공개</summary>

R&T Eq. 4-20 (low-Cu, $f_u \ll 1$ 영역): $f_u' = (P_t/P_t') \cdot f_u = (43/12.5) \cdot 0.005 \approx 0.0172$. 약 3.4배 증가.

**다음 깊이 질문**: 이 fu 증가가 warfarin의 V (9.4 L)에 미치는 효과를 Eq. C-13으로 계산하면 약 13.7 L이 되는데(Table 4-12 데이터와 일치), 같은 dose에서 Cu는 어떻게 변하는가?

</details>

---

### Q6 (Application, ★)

R&T Fig. 4-23에서 propranolol의 V vs fu가 거의 직선 ($V \approx V_{TW} \cdot f_u/f_{uT}$, intercept ≈ 0)으로 나타난다. 이 직선의 slope이 cohort 사이에서 거의 일정하다면, individual-to-individual V 변동의 dominant source는 무엇인가?

<details>
<summary>📖 정답 공개</summary>

Slope = $V_{TW}/f_{uT}$가 일정 → $V_{TW}$ (body water)와 $f_{uT}$ (tissue binding) 모두 individual 간 거의 일정. 따라서 **V의 BSV는 거의 fu의 BSV로 환원**된다. 이는 propranolol과 같이 strongly tissue-bound basic drug에서, plasma binding 변동이 individual V variability의 dominant source임을 의미.

**다음 깊이 질문**: 이 구조는 PopPK NONMEM 모델에서 V를 어떻게 spec하라는 것을 의미하는가?

</details>

---

### Q7 (Application, ★★)

Eq. 4-29 ($V = V_p + V_{TW} \cdot (f_u/f_{uT}) \cdot (P_{uptake}/P_{efflux})$)에서, P-gp inhibitor (verapamil)을 동시 투여하여 brain efflux를 억제하면, brain의 unbound 농도와 V는 각각 어떻게 변할 것으로 예상되는가?

<details>
<summary>📖 정답 공개</summary>

P-gp efflux 억제 → $P_{efflux}$ 감소 → $P_{uptake}/P_{efflux}$ 증가 → $Cu_T/Cu$ 증가 (Eq. 4-26). 즉 brain의 unbound 농도가 plasma unbound와 같아지거나 더 높아질 수 있음. 그러나 brain은 body의 약 2%이므로, V (body-wide 평균)에는 거의 영향 없음. 임상적으로는 substrate drug의 CNS exposure가 증가하여 toxicity 발생 가능 (예: loperamide의 P-gp 의존 CNS exclusion이 P-gp inhibitor 동반 시 사라져 opiate-like effect 출현).

**다음 깊이 질문**: brain efflux 억제로 인한 CNS toxicity의 정량적 예측을 위해 PBPK 모델은 어떤 parameter를 필요로 하는가?

</details>

---

### Q8 (Application, ★★)

G&W Fig. 2.141에서 dog, rat, mouse의 in vivo response를 total plasma 농도에 plot하면 potency가 약 90배 차이 나지만, unbound 농도에 plot하면 EC50,u ≈ 2 nM로 일치한다. 이것이 first-in-human (FIH) dose prediction에서 **어떤 함의**를 가지는가?

<details>
<summary>📖 정답 공개</summary>

FIH dose prediction에서는 effective concentration의 species 외삽이 필수이며, total 농도 기준 외삽은 fu의 species 차이로 인해 한 자릿수 단위 오차를 낸다. **unbound 농도 (Cu) 기준 외삽**은 이 PPB 차이를 자동 보정하므로 정확한 dose prediction을 가능하게 한다. NCE (new chemical entity)의 IND submission에서 ex vivo PPB를 multiple species (mouse/rat/dog/human)에서 routine으로 측정하는 이유가 정확히 이것이다.

**다음 깊이 질문**: 만약 in vitro IC50를 사용해 FIH dose를 predict한다면, IC50 자체가 어떤 농도 (total vs unbound)로 보고되어야 하는가? in vitro assay에서도 PPB를 보정해야 할까?

</details>

---

### Q9 (Application, ★★)

**Boss Dilemma — Socratic Final Question** (★★)

> 당신은 narrow-therapeutic-index 항부정맥제 (lidocaine analog, IV 투여, $E_H \approx 0.7$, fu = 0.3)의 NDA-grade PopPK 모델을 만들고 있다. 데이터셋에서 cohort A는 정상 대상자, cohort B는 surgical trauma 후 환자(α1-acid glycoprotein 2배 증가, fu = 0.15로 감소)이다.
> 
> **선택 1**: total plasma concentration (C)을 기준으로 dose-response를 보고하고, "α1-AGP를 covariate로 하는 fu shift"를 covariate 모델에 explicit하게 spec하지 않는다. 모델은 simple하고 reviewer가 이해하기 쉬우나, B cohort에서 dose-response curve가 left-shift되어 보임 (potency 증가처럼 보임).
> 
> **선택 2**: unbound plasma concentration (Cu)을 기준으로 dose-response를 보고하고, fu를 α1-AGP의 함수로 covariate 모델에 spec한다. 모델은 복잡하고 추가 ex vivo PPB 측정이 필요하나, dose-response가 cohort 간 일치하여 mechanistic interpretation이 명확해진다.
> 
> 당신은 어느 쪽을 택하며, 그 결정을 NDA submission에서 어떻게 방어할 것인가?

<details>
<summary>📖 정답 공개 — 수석 모델러의 Trade-off 논리</summary>

**최종 선택: 선택 2 (unbound 기준 + fu covariate model)**.

**Trade-off 논리**:

1. **이 약물의 정확한 risk profile은 dose-Cu-effect로 규정**된다. lidocaine analog + IV 투여 + $E_H = 0.7$ + narrow therapeutic window의 조합은 Benet & Hoener [2003] 결론에서 명시한 **dose adjustment가 필요한 예외 case** ($E_H \to 1$ 한계로 갈수록 fu가 CL에 explicit하게 등장하여 cancellation 깨짐). 이 약물에서는 surgical trauma cohort의 fu 감소가 임상적으로 의미 있는 Cu 변화를 만들 가능성이 높다.

2. **선택 1은 model misspecification**을 만든다. 같은 dose에서 cohort B의 C가 cohort A보다 높게 보일 것이며 (fu 감소 → V 감소 → C 증가), 이 차이가 "약물 dynamics 변화"로 잘못 해석될 수 있다. PopPK reviewer가 이 패턴을 발견하면 첫 deficiency letter 사유 — "Has the contribution of altered protein binding to apparent dose-response shift been mechanistically separated from genuine PD differences?"

3. **선택 2의 비용은 정당화된다**. 추가 ex vivo PPB 측정은 IND 단계에서 routine 권고 (G&W §2.9.5); NDA에서는 "limited number of clinical studies specially designed for this purpose"가 표준 권고이며, surgical trauma cohort는 정확히 그 study에 해당한다. 모델 복잡성은 "regulatory rigor"의 신호로 reviewer에게 받아들여진다.

4. **방어 언어**: "Given the IV high-extraction nature ($E_H \approx 0.7$) and narrow therapeutic window of [drug], we model unbound plasma concentration as the active species in accordance with FDA Guidance on PopPK Analyses (2022) and Benet-Hoener (2003) framework. Plasma binding (fu) is incorporated as a covariate of α1-acid glycoprotein, allowing mechanistic separation of disease-induced binding shifts from PD effects. Cohort-specific Cu-response coherence is presented in Fig. X as evidence of model adequacy."

**규제적 방어의 핵심**: deficiency letter 사유를 사전에 차단하고, "thermodynamically active species"의 정의를 first-principle 수준에서 정확히 한다. simplicity는 미덕이 아니다 — explicability와 mechanistic transparency가 미덕이다.

</details>

---

## §8 — Meta-Frame & Big Picture

### A. Positioning (28-Session 지식 아키텍처에서의 위치)

**이전에 온 것**:
- Session 01: 1구획 모델 IV bolus의 $V$ 정의 (operational definition만). $C(t) = (Dose/V) e^{-kt}$의 $V$가 무엇인지 본 세션에서 해부됨.
- 약산/약염기의 ionization (App.B, CONTEXT). 막투과의 결정인자 중 charge 부분.
- 단백질 결합의 mass action 일반론 (선수지식).

**바로 다음에 오는 것**:
- **Session 03 (Ch.5 Elimination)**: Hepatic extraction model, well-stirred liver, $CL_H = Q_H \cdot E_H = Q_H \cdot \frac{f_u \cdot CL_{int}}{Q_H + f_u \cdot CL_{int}}$. **fu가 분자에서 직접 등장** — high-extraction vs low-extraction의 분류, 그리고 §5 Critical Blow의 "예외 case" (IV high-extraction narrow-therapeutic-window)의 정량적 메커니즘이 여기에서 설명됨.
- **Session 04 (Ch.6 Multiple-Dose Regimens)**: Loading dose $D_L = V \cdot C_{target}$. M3의 Apex Concept (small Vd의 fu-loading dose 관계)이 직결.

**이 기반에 결정적으로 의존하는 고급 도메인**:

1. **PopPK Covariate Modeling (NONMEM)**: covariate model에서 V ~ albumin, V ~ α1-AGP, V ~ body weight 관계는 모두 본 세션 M3·M4·M5의 변형. covariate가 잘못 spec되면 BSV가 잘못 잡히고, RSE가 부풀고, η-shrinkage가 증가.

2. **Physiologically-Based Pharmacokinetics (PBPK)**: 14+ tissue compartment 모델에서 각 organ의 $K_p$를 in silico 예측 (Rodgers-Rowland method). M5의 acidic phospholipid binding이 이 method의 핵심.

3. **TMDD (Target-Mediated Drug Disposition)**: 항체 약물의 작은 Vd (5–10 L), lymphatic-mediated 분포(M2 CONTEXT의 macromolecule)의 메커니즘이 본 세션의 small-Vd 모델의 직접 응용.

4. **TDM (Therapeutic Drug Monitoring)**: free phenytoin assay (저알부민혈증 환자), warfarin in nephrotic syndrome — 모두 §5 Critical Blow의 임상 응용. ICU 환자에서 albumin·α1-AGP 동시 변화 처리는 본 세션 없이 불가능.

5. **DDI (Drug-Drug Interaction) — Plasma Binding Displacement**: high-extraction IV 약물에서만 임상적으로 의미 있다는 Benet-Hoener 결론은 본 세션 M6의 직접 결론.

### B. Dependencies — 이 섹션을 대충 넘겼을 때의 구체적 실패 모드

**실패 모드 1 — Hepatic extraction misclassification (Session 03)**:
- 본 세션의 fu가 고정 상수가 아니라는 점(M4)을 놓치면, $CL = f_u \cdot CL_{int}$의 covariance가 잘못 계산됨.
- 추적: dose-AUC linearity가 데이터에서 깨질 때 reviewer가 "saturable PPB가 검사되었는가?"를 묻고, IND 단계에서 $f_u$ at multiple Cu가 측정되지 않았으면 dossier에 hole 발생.

**실패 모드 2 — PopPK V covariate misspecification (PopPK)**:
- M3 Apex Concept의 large vs small Vd 응답 차이를 놓치면, large-Vd 약물에서 albumin을 V의 covariate로 잘못 spec.
- 추적: ETA correlation matrix에서 V와 CL의 ETA가 spurious correlation을 보이며, OFV는 떨어지지만 simulation에서 prediction interval이 잘못 잡힘. visual predictive check (VPC)에서 disease state 환자군의 prediction이 underpredict.

### C. Professional Moat — 이 섹션의 통달이 만드는 것

NONMEM을 실행하고 GOF 플롯을 생성할 수 있는 주니어 모델러와, 2구획 모델을 데이터에 적합시킬 수 있는 AI가 이미 존재한다. **본 세션의 원리를 — 메커니즘이 아닌 구조적 이해의 수준에서 — 진정으로 내면화한 연구자만이 다음을 할 수 있다**:

1. **fu-CL-V의 cancellation 패턴을 한눈에 읽는다**. 신증후군 환자의 warfarin 데이터에서 V 증가 + CL 증가 + t1/2 감소 + Cu 거의 일정의 4중 패턴이 단일 fu 증가 한 변수로 설명되는 것을 즉각 안다. 다른 사람은 4개의 covariate를 각각 spec하려 하다가 model overfitting에 빠진다.

2. **Vd의 mechanistic decomposition을 본다**. propranolol Vd = 200~700 L의 huge BSV가 거의 모두 fu의 BSV에서 비롯됨을 Fig. 4-23 한 장에서 읽는다. 다른 사람은 BSV를 random effect로만 처리하고 mechanistic source를 놓친다.

3. **Critical Blow를 사전에 차단한다**. NDA dossier 작성 시 "thermodynamically active species" 정의를 first-principle 수준으로 명시하고, fu shift cohort에 대한 Cu-based dose-response를 사전 분석. 다른 사람은 deficiency letter를 받고 추가 study에 1년을 추가 지출.

4. **PBPK predictivity의 source를 안다**. tissue Kp의 80% variance가 acidic phospholipid binding 하나에서 오는 것을 알고, 후보 분자의 logP·pKa·MW만으로 in silico Vd를 한 자릿수 단위 정확도로 예측. 다른 사람은 in vivo data 없이는 prediction을 시도하지 못함.

5. **약물 개발의 첫 관문에서 살아남는다**. 후보 분자의 4D matrix (size × logP × charge × P-gp affinity)를 첫 5분의 in silico screening으로 평가. 다른 사람은 in vitro 실험 후에야 "BBB 통과 안 되네"를 안다.

이것은 **구조적 필연성 수준의 transferable expertise**이며, 자동화될 수 없는 이유는 약물별 mechanistic context를 매번 새로 평가해야 하기 때문이다. 패턴 인식이 아니라 first-principle 적용이 본 세션의 결과물이다.

---

✦ STEP 1 완료.

다음이 준비되었습니다:
  • §1 세션 헤더 & 로드맵
  • §2 개념 해부 카드 (6개 개념, Apex: M3 분포용적의 수학 구조)
  • §5 혼동 쌍 해부 (4개 쌍, Critical Blow 적용: C vs Cu)
  • §7 자기 테스트 (9개 질문, 보스 딜레마 포함 — narrow-therapeutic IV high-extraction 약물의 PopPK 모델 선택)
  • §8 메타프레임 & 빅 픽처
  • 감지된 소스 유형: 혼합 (Vol I-A: R&T 임상·생리학 / Vol I-B: G&W 데이터·수식 + PK47 mechanistic binding)
  • Data Anchoring 소스: warfarin in nephrotic syndrome (R&T Table 4-12), cephalosporin V-fu series (Fig. 4-25), propranolol V-fu (Fig. 4-23), thiopental dog tissue distribution (Fig. 4-13), indinavir CSF/plasma (Fig. 4-10), metoprolol Kp-acidic phospholipid (Fig. 4-24), G&W PK47 Compound 1·2 (Table 47.1, Eq. 47:4 Ka ≈ 6 conc units), Benet & Hoener [2003] 456-drug review.

"계속"을 입력하면 Step 2 HTML 컴파일러가 실행됩니다.
Step 2는 위 내용 전체(§1·§2·§5·§7·§8) +
§3(구조적 동형성 지도) + §4(인터랙티브 시뮬레이터 + Assumption Collapse 토글) +
§6(실용 시나리오 & 진단 병리)를 단일 완성 HTML 파일로 통합합니다.

---
*Phase 1 markers inserted: MASTER LENS (6개 카드), ANCHOR (5개 bridge), CONFUSION (4개 pair), SELF-TEST (9개), RECAP (1개 §2 종합). FIGURE markers는 Phase 4C에서 삽입됨.*

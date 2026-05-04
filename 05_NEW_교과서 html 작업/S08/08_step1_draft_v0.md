# Step 1 Draft v0 — Session 08 (Final Integrated)
# 비선형 PK · TDM · Drug Interactions의 통합 마스터리 레이어

> **⚑ 진행 상태 — 3-Stage 확장통합 최종본 (FINAL)**
>
> 본 문서는 Phase 1 Master's Lens Draft의 **3-stage 확장통합 최종 산출물**이다.
> Phase 2(Source Fidelity Audit), Phase 3(Insight Crucible) 입력으로 사용된다.
>
> | Stage | 소스 | 페이지 | 역할 | 산출 카드 |
> |---|---|---|---|---|
> | **1** | Gabrielsson & Weiner 5e | Ch.2.7 (pp.112–141) + Ch.3.6 (pp.224–227) + PK17·18·22 | Mechanism canonical | M1–M9 |
> | **2** | Rowland & Tozer 5e | Ch.16 (pp.491–529) | 임상 정량 layer | M2-EXT, M3-EXT, M5-EXT + T1–T4 |
> | **3** | Rowland & Tozer 5e | Ch.17 (pp.531–576) | DDI 정량 prediction framework | T4-EXT + T5–T10 |
>
> **확장통합 원칙 (워크플로우 v3.3.2)**:
> - Stage 1 (M1–M9): mechanism의 정본(canonical). 수식 도출·NONMEM 코드 구조의 근거.
> - Stage 2 (T1–T4, X-EXT): Stage 1 mechanism을 임상 영역에서 **정량 anchor**와 함께 재해석.
> - Stage 3 (T5–T10, T4-EXT): Stage 1·2를 전제로 **DDI 정량 예측 프레임워크**와 **규제·NDA 의사결정 언어**로 외화. FDA DDI Guidance Eq.17-11 / Eq.17-18을 mechanism으로부터 직접 도출.
> - Cross-reference만 사용 — mechanism 재도출·정의 재서술 금지.

---

## ▶ Master's Lens — 3-Stage 통합 Curation Map

### MUST 카드 (체화 필수 — 풀 §2 카드)

#### Stage 1 — Mechanism Canonical (정본은 별도 Stage 1 산출물 참조; 본 통합본은 구조 anchor만 표시)

| 코드 | 카드 | 핵심 mechanism | 체화 실패 시 붕괴 |
|---|---|---|---|
| **M1** | 비선형성 진단 (Nonlinearity Diagnostics) | Dose-normalized AUC vs Dose, superposition 위반 판별 | 비선형 약물에 선형 모델 적용 → fitting 실패 진단 미스 |
| **M2** | Capacity-limited MM 소거 | $Cl = V_m/(K_m+C)$, two-extreme behavior, $C_0/V_d$ 영역별 거동 (Eq 2:264–2:274, 2:309) | MM 약물에 선형 dose 조정 적용 시 비대칭 toxicity |
| **M3** | 효소 turnover 모델 | $dE/dt = R_{in} - k_{out}\cdot E$, $Cl(t)$ 시간 함수 (Eq 2:275–2:287) | Time-dependent kinetics를 IIV 변동성으로 오해 |
| **M4** | PK22 Autoinduction Feedback | Vc/Vt/a/k12/k21/kout/E0 (Eq 2:289–2:293, Table 22.2; PIPET) | Multiple-dose 시 t½ 변화를 측정 오류로 오인 |
| **M5** | Nonlinear protein binding | $C_b = n\cdot P_t \cdot C_u/(K_d+C_u)$, open vs closed system 결론 (Eq 2:294–2:303) | 단백 결합 변화를 dose 조정 사유로 잘못 사용 |
| **M6** | Drug-metabolite nonlinear model | 2구획 drug + 1구획 metabolite + MM 소거 (Eq 2:304–2:308; Table 2.18–2.20) | Flip-flop을 분포 kinetics로 오독 |
| **M7** | Ethanol 통합 사례 (Capacity + Time + Flow) | 3중 의존성, $F_{oral}$ 농도 의존성 (Eq 18:13) | 한 mechanism만 보고 다른 두 mechanism missed |
| **M8** | DDI 경쟁적 길항 PD 모델 | Eq 3:49, EC50 이동 (단일 receptor, 평형) | Receptor-level 경쟁을 기전 기반으로 잘못 해석 |
| **M9** | DDI 비경쟁·Enantiomer·Multiple binding PD | Eq 3:50–3:53, Table 3.2 (ketamine enantiomer) | Emax 감소를 PK 변화로 오독 |

#### Stage 2 — 임상 정량 layer (M2/3/5-EXT + T1–T4)

| 코드 | 카드 | Tozer Ch.16 추가 anchor |
|---|---|---|
| **M2-EXT** | Capacity-limited MM 임상 정량 | Phenytoin (Vm≈500, Km'=4 mg/L; 67%↑→9× Css), Alcohol (Vm≈10 g/hr, zero-order plateau), Ascorbic acid (133× dose → 2× Css). $C_{u,ss}=K_m R_0/(V_m-R_0)$ (Eq.16-7), $t_{90}$ 발산 (Eq.16-10), 혼합 경로 (Eq.16-11) |
| **M3-EXT** | Time-dependent kinetics 임상 anchor | Carbamazepine autoinduction turnover ~5d (Fig.16-25), Verapamil chronopharm |
| **M5-EXT** | Nonlinear binding 4가지 prototype | Cefonicid (saturable albumin), Trandolaprilat (ACE binding), Naproxen (saturable albumin), Disopyramide (α₁-AAG); Salicylic acid opposing nonlinearities |
| **T1** | 포화 신장 이송 (Saturable renal transport) | Dicloxacillin (CLR↓ with dose, secretion), Ascorbic acid (CLR↑ with dose, reabsorption); $Rate=T_m\cdot C_u/(K_T+C_u)$ (Eq.16-3) |
| **T2** | 포화 First-Pass Metabolism | Nicardipine (F=19→36% across 10–40 mg q8h); Methylphenidate enantiomer F 차이 |
| **T3** | TMDD 기초 (Small molecule prototype) | Bosentan (Vss 0.67→0.16 L/kg), Imirestat, Trandolaprilat (ACE), Draflazine (RBC transporter), Mitoxantrone |
| **T4** | Mechanism-Based Inhibition mechanism | Clarithromycin: kinact=0.07/min, kE≈0.23/day (효소 t½≈3d); $dE/dt$에 분해 항 추가 |

#### Stage 3 — DDI 정량 prediction framework (T4-EXT + T5–T10)

| 코드 | 카드 | Tozer Ch.17 핵심 anchor + Eq |
|---|---|---|
| **T4-EXT** | MBI 정량 (Eq.17-13/14) | Clarithromycin: kinact/kE = 438, Cu_I/K_I = 0.025 → **11배 CL 감소** (vs reversible 1.025배). Recovery time = enzyme t½ ≈ 3d → 회복 2주 (Fig.17-13 midazolam) |
| **T5** | Displacement-only DDI 재해석 | Phenytoin–Valproate (Fig.17-3): N=25/11/9; total↓ 일정 unbound. Warfarin–Phenylbutazone: 초기 displacement 가설 → 실제는 displacement+inhibition. $V=V_p+V_t\cdot fu/fu_T$ (Eq.17-1), Fig.17-2/17-4 시뮬레이션 |
| **T6** | 경쟁적 억제 정량 framework (Eq.17-9~17-12) | Theophylline–Enoxacin (Fig.17-6): t½ 8.8→22h, Css 4→9 mg/L, CL_inh/CL_normal=0.44, fm=0.67. Desipramine–Quinidine (CYP2D6, fm=0.75 → 4× CL감소). Desipramine–Fluoxetine (Table 17-11: AUC 284→2110, t½ 16→64h). Strong inhibitor (Table 17-5)·≥4× CYP3A/2D6 substrates (Table 17-6). Eq.17-11 AUC ratio = FDA Guidance 핵심식 |
| **T7** | PM + Inhibition Risk Amplification (Eq.17-18) | Maximum Exposure Ratio = $1/(1-fm_{POLY}-fm_{NP})$. Fig.17-15 임상 검증 (omeprazole-clarithromycin 33×). PM 환자에서 nonpolymorphic 경로 strong inhibitor → 10×+ exposure |
| **T8** | 유도 PK Time Course (Eq.17-15 framework) | Phenobarbital–Dicumarol (Fig.17-17): 3–4 weeks plateau, 시상수 = phenobarbital t½ (4 days). Carbamazepine autoinduction (Stage 2 M3-EXT)과 동일 mechanism의 hetero-induction. 철수 trap |
| **T9** | Multifaceted/Transporter-Mediated DDI | Digoxin–Quinidine (Table 17-8: CL 140→72, V 500→240, F 0.75→0.85 — PgP+OATP). Atorvastatin–Rifampin IV acute (Fig.17-19: Cmax 10×, AUC 7×, t½ 8→3h — OATP1B1 inhibition). Rosuvastatin–Cyclosporine (Fig.17-11: 11× Cmax). Diltiazem–Lovastatin route effect (Table 17-7: 1.27 IV vs 3.57 oral). Fluconazole–Midazolam (Fig.17-10: 5.6× oral vs 2× IV; F_H 0.42→0.72, F_G 0.57→0.88) |
| **T10** | Pharmacodynamic Interactions | Eq.17-21 두 full agonist 결합, Emax 천장. Isobologram (Fig.17-21): 가산성 직선/길항 위/시너지 아래. Greco Eq.17-22 정량. Midazolam-propofol (시너지), Isoproterenol-propranolol (길항) |

### CONTEXT (1–2 문장으로 흡수)

#### Stage 1 흡수 항목 (Stage 1 카드 본문 내 1–2 문장)
- §2.7.4 Flow-dependent kinetics: 개념 참조만 (M7 ethanol에서 통합 흡수)
- bupivacaine 임상 결론 예외: M5 카드 1줄

#### Stage 2 흡수 항목 (Stage 2 EXT/T 카드 본문 내)
- Griseofulvin solubility-limited absorption (T2 흡수절)
- Amoxicillin saturable peptide transport, Vitamin B12 IF saturation (T1)
- Methylphenidate enantiomer first-pass (T2 본문)
- Salicylic acid opposing nonlinearities (M5-EXT F절)
- Ethchlorvynol overdose (§8 dependencies)
- Verapamil chronopharm (M3-EXT)
- Glucose renal threshold (T1 prototype)

#### Stage 3 흡수 항목 (Stage 3 T 카드 본문 내)
- **Combination products** (Table 17-2): Lopinavir/Ritonavir, L-Dopa/Carbidopa, Imipenem/Cilastatin, Amoxicillin/Clavulanate — T6/T9에서 1줄 (beneficial DDI)
- **Penicillin–Probenecid** (anionic transport competition): T6 또는 T9 1줄 (beneficial)
- **Imipenem–Cilastatin** (Fig.17-12, renal dehydropeptidase inhibition): T6 1줄 (beneficial)
- **Lidocaine–Propranolol** (hemodynamic interaction, hepatic blood flow ↓): T9 1줄
- **Salicylic acid renal CL pH-sensitive**: T9 또는 §8 1줄
- **Ritonavir–CYP3A4** (보조 inhibitor): T6 Strong inhibitor list 흡수
- **Aminoglycoside nephrotoxicity** (이미 Stage 2 M3-EXT에서 1줄, time-dependent CLR↓ self-toxicity)
- **Loperamide–Quinidine** (CNS PgP), **Ketoconazole–Ritonavir** (CSF PgP): T9 또는 §8 1줄
- **PD additive vs synergism vs antagonism** isobole 외 정의: T10 1줄
- **Sequence of administration** (인지 어려움): §8 dependencies

---

## §1. Session Header & Roadmap (3-Stage 통합)

**Session 08 — 비선형 PK · TDM · Drug Interactions 통합 마스터리**

**Sources**:
- **[A]** `08_G_비선형_PK_MM_DDI_기전.pdf` — Gabrielsson & Weiner 5e, Ch.2.7 (pp.112–141) + Ch.3.6.1–3.6.4 (pp.224–227) + Case Studies PK17/PK18/PK22 (pp.553–585)
- **[B]** `08_T_비선형_PK_MM_DDI_기전_01.pdf` — Rowland & Tozer 5e, Ch.16 Nonlinearities (pp.491–529)
- **[C]** `08_T_비선형_PK_MM_DDI_기전_02.pdf` — Rowland & Tozer 5e, Ch.17 Drug Interactions (pp.531–576)

**감지된 소스 유형**: 혼합 (Vol I 임상 + Vol I 데이터 이론 + Vol II PIPET 코딩 잠재 호출)
- Gabrielsson 5e = 데이터 이론 + PK17/18/22 정량 anchor 정본
- Rowland & Tozer 5e Ch.16 = 임상 정량 anchor 정본
- Rowland & Tozer 5e Ch.17 = DDI 정량 prediction framework + 규제 언어 정본

**Big Idea (단일 통합 문장)**:
> 비선형 PK는 *carrier saturation*이라는 단일 기하학을 capacity·time·flow·binding의 4개 도메인에 평행하게 표면화하며, 그 표면화가 임상에서는 *분모 발산* (phenytoin 67% dose↑ → 9× Css)·*시상수 다층화* (drug PK ≠ enzyme PK ≠ inducer PK)·*시너지 비대칭* (oral first-pass DDI ≫ IV)으로 드러난다. NDA reviewer는 *mechanism이 정확하면 dose가 안전하다*는 단일 명제로 본 세션의 모든 사례를 압축 평가하며, FDA DDI Guidance의 핵심식 (AUC ratio = $1/[fm/(1+Cu_I/K_I) + (1-fm)]$)은 본 세션 mechanism 카드 (M2 + T4 + T6)의 직접 정량 외화이다.

---

### 3-Stage 통합 지식 그래프 위치

```
[Stage 1 mechanism canonical layer] — 정본
        │
        ├── M1 비선형성 진단 ────── Dose-normalized AUC test
        ├── M2 Capacity MM ────────── Vmax/Km/Cl(C) ─────────────────┐
        ├── M3 Time turnover ──────── dE/dt = Rin − kout·E ───────────┤
        ├── M4 PK22 autoinduction ─── kout/E0 specific case ──────────┤
        ├── M5 Nonlinear binding ──── fu(C), open vs closed system ──┤
        ├── M6 Drug-Metabolite ────── 2-compartment + MM ────────────┤
        ├── M7 Ethanol 통합 ─────────── Capacity + Time + Flow ─────────┤
        ├── M8 DDI competitive PD ─── Eq 3:49 EC50 shift ─────────────┤
        └── M9 DDI noncompetitive PD ─ Eq 3:50–3:53 Emax shift ───────┤
                                                                       │
[Stage 2 임상 정량 layer]                                               │
        │                                                              │
        ├── M2-EXT ←──── M2 ────── Phenytoin/Alcohol/Ascorbic acid 정량 │
        ├── M3-EXT ←──── M3 ────── Carbamazepine 5d turnover           │
        ├── M5-EXT ←──── M5 ────── 4가지 protein binding prototype     │
        ├── T1 (NEW) ──────────────── Saturable renal transport         │
        ├── T2 (NEW) ──────────────── Saturable first-pass               │
        ├── T3 (NEW) ←── M5 (변형) ── TMDD basics                        │
        └── T4 (NEW) ←── M3 (반전) ── MBI mechanism                      │
                                                                       │
[Stage 3 DDI 정량 layer]                                                │
        │                                                              │
        ├── T4-EXT ←──── T4 ────── MBI 정량 Eq.17-13/14 (clarithromycin)│
        ├── T5 (NEW) ←── M5 + M5-EXT ── Displacement-only DDI 재해석    │
        ├── T6 (NEW) ←── M2 + M8 ────── 경쟁적 억제 Eq.17-9~17-12        │
        ├── T7 (NEW) ←── T6 + 약물유전 ── PM × Inhibition Eq.17-18       │
        ├── T8 (NEW) ←── M3 + M3-EXT ── Induction Time Course Eq.17-15 │
        ├── T9 (NEW) ←── T2 + 모든 mechanism ─ Multifaceted DDI          │
        └── T10 (NEW) ←── M8 + M9 ────── PD Interactions Eq.17-21       │
                                                                       │
[고급 모듈로의 출구]                                                   ↓
        ├── PopPK 비선형 IIV·RUV 구조 (별도 세션)
        ├── PBPK Whole-body model (별도 세션)
        ├── TMDD Full quasi-equilibrium (Stage 2 T3 → 단백 의약품 PK)
        └── FDA DDI Guidance (Stage 3 Eq.17-11/17-18 → IND/NDA 직접 적용)
```

**Apex Concept 지정 (각 Stage별 1개)**:
- Stage 1 Apex: **M2** Capacity-limited MM (mechanism의 원형)
- Stage 2 Apex: **T4** Mechanism-Based Inhibition (turnover ODE의 반전 구조)
- Stage 3 Apex: **T6** 경쟁적 억제 정량 framework (Eq.17-11이 FDA DDI Guidance의 핵심)

**Critical Blow 지정 (각 Stage별 1개 혼동쌍)**:
- Stage 1 Critical Blow: CP1 (capacity-limited vs flow-limited — 별도 Stage 1 산출물)
- Stage 2 Critical Blow: **CP5** (Competitive vs MBI inhibition)
- Stage 3 Critical Blow: **CP8** (Inhibition vs Induction — 시상수와 방향성 모두 반전)

---

## §2. Concept Anatomy Cards

### Stage 1 Mechanism Cards (M1–M9) — 구조 anchor 요약
*정본은 별도 Stage 1 산출물(가브리엘슨 + PK17/18/22 정본 카드)에 존재. 본 통합본은 Stage 2·3에서의 cross-reference 무결성 확보를 위한 구조 anchor만 표시.*

#### M1. 비선형성 진단 (Nonlinearity Diagnostics)
**Mechanism**: Superposition 위반 판별. Dose-normalized AUC vs Dose 그래프에서 *수평선*은 선형, *기울기 있는 곡선*은 비선형.
**Cross-ref**: T6 (Eq.17-11 기반의 AUC ratio가 dose ≠ 1 영역에서는 본 카드 진단 도구의 *DDI 변형*).

#### M2. Capacity-limited Michaelis-Menten 소거
**Mechanism**: $\frac{dC}{dt} = -\frac{V_m \cdot C}{K_m + C}$ (Eq 2:264). 두 극한:
- $C \ll K_m$: $Cl \approx V_m/K_m$ (first-order, linear)
- $C \gg K_m$: $-dC/dt \approx V_m/V_d$ (zero-order)
**핵심 Apex Concept (Stage 1)**. **Cross-ref**: M2-EXT (임상 정량), T6 (경쟁적 억제로 $K_m^{app} = K_m(1+I/K_I)$ 변형), T4-EXT (MBI로 $V_m$ 자체 감소).

#### M3. 효소 turnover 모델
**Mechanism**: $\frac{dE}{dt} = R_{in} - k_{out} \cdot E$ (Eq 2:275). 정상상태 $E^{ss} = R_{in}/k_{out}$. 약물에 의한 $R_{in}$ 변화 (induction) 또는 $E$ 분해 가속 (MBI)이 본 turnover 구조의 *분기 변형*.
**Cross-ref**: M3-EXT (carbamazepine 임상 정량), T4 (MBI 분해 항 추가), T8 (induction time course).

#### M4. PK22 Autoinduction Feedback
**Mechanism**: 약물이 자기 대사 효소 $R_{in}$을 stimulate. Vc/Vt 2-compartment + enzyme compartment ODE. 파라미터: a (induction strength), kout (turnover), E0.
**Cross-ref**: M3-EXT (carbamazepine 동일 mechanism의 *임상 prototype*), T8 (induction PK time course의 mathematical framework).

#### M5. Nonlinear protein binding
**Mechanism**: $C_b = n \cdot P_t \cdot C_u/(K_d + C_u)$ (Eq 2:294). Open system에서 $C_u = K^0/CL_u$ — *단백 농도/affinity 변화는 dosing rate 변화 사유 아님*. Closed system (in vitro)와 결론 반대.
**Cross-ref**: M5-EXT (4가지 prototype), T3 (TMDD = M5의 극한 case), T5 (displacement-only DDI 임상 함의).

#### M6. Drug-Metabolite Nonlinear Model
**Mechanism**: 2-compartment drug + 1-compartment metabolite + MM 소거. Flip-flop은 *분포가 아닌 metabolite 형성률 한계*.
**Cross-ref**: T6 (active metabolite가 inhibition target일 때 임상 결과 분기), T9 (clopidogrel 활성 metabolite DDI).

#### M7. Ethanol 통합 사례 (Capacity + Time + Flow)
**Mechanism**: 단일 약물에 *3개 mechanism 동시 작동*. Vmax≈10g/hr, Km≈100mg/L (Capacity), CYP2E1 자기 induction (Time), 저농도 hepatic flow-limited (Flow).
**Cross-ref**: M2-EXT (zero-order plateau anchor), M3-EXT (CYP2E1 induction), §8 multifaceted (T9의 small-molecule prototype).

#### M8. DDI 경쟁적 길항 PD 모델
**Mechanism**: 두 ligand가 동일 receptor 경쟁. EC50 이동: $EC50^{app} = EC50(1 + [I]/K_i)$ (Eq 3:49).
**Cross-ref**: T6 (PK 도메인의 동일 mathematical structure — Eq.17-9의 $K_m \to K_m(1+Cu_I/K_I)$가 본 카드의 PK 변형), T10 (Eq.17-21 두 agonist 합산).

#### M9. DDI 비경쟁·Enantiomer·Multiple binding PD
**Mechanism**: Eq 3:50 (Emax 감소), Eq 3:51 (일반 경험), Eq 3:52–3:53 (enantiomer interaction, ketamine R/S 차이), Eq 3:48 (multiple binding sites, p.224).
**Cross-ref**: T2 (methylphenidate enantiomer first-pass — 본 카드의 PK 표면화), T10 (Isobologram의 *비경쟁성·시너지 정량*).

---

### Stage 2 카드 (M2-EXT, M3-EXT, M5-EXT, T1–T4) — 임상 정량 layer

*이하 Stage 2 산출물에서 *그대로* 통합. mechanism 재도출 없음.*


---

### M2-EXT. Capacity-limited MM — 임상 정량 layer

<!-- ANCHOR -->
Stage 1 M2 카드는 MM을 *수식과 NONMEM 코딩*으로 다루었다. 본 EXT는 Tozer가 수십 년에 걸쳐 임상에서 쌓은 *세 가지 prototype 약물* (phenytoin, alcohol, ascorbic acid)을 통해 같은 mechanism이 *어떤 모양의 dose-response*를 만드는지 — 그리고 그 모양을 임상의가 어떻게 오독하는지 — 를 다룬다.

<!-- MASTER LENS -->
> **[개념 Big Idea: 거장의 시각]**
>
> **왜 치명적으로 중요한가**: Tozer Ch.16 chapter-opening 시나리오 (p.491) — 간질 환자가 phenytoin 300 mg/day에서 4 mg/L에 머물고 있어 의사가 500 mg/day로 *67% 증량*했더니 20일 후 36 mg/L (9배)에 도달해 nystagmus·ataxia로 응급실에 온다. Vm을 향해 dose가 접근할 때 Cu_ss는 *수직 점근선*을 만들며 발산한다 (Fig.16-9). 임상 phenytoin은 일반적으로 *Vm=500 mg/day의 60–80% 영역*에서 운영되므로, dose의 작은 변화가 분모 (Vm−R₀)에 비대칭적으로 영향을 미친다.
>
> **체화해야 할 단 하나의 직관**: Cu_ss = Km·R₀/(Vm−R₀). 분모 (Vm−R₀)가 *0에 접근*하면 Cu_ss는 어떤 값이든 될 수 있다. *분모에 가까이 갈수록 모든 변화가 위험하다*.
>
> **이 직관을 머릿속에 박고 아래를 읽어라**: Stage 1 M2가 mechanism이라면 본 EXT는 *그 mechanism이 임상에서 만드는 곡선의 모양*. Phenytoin·alcohol·ascorbic acid 세 약물이 같은 mechanism의 다른 dose 영역에 살고 있다 — phenytoin은 변곡점, alcohol은 zero-order plateau, ascorbic acid는 escape valve 영역.

#### A. 임상 정상상태 수식 — Cu_ss = Km·R₀/(Vm−R₀)

Stage 1 Eq 2:271은 *single dose AUC*. 임상에서는 multiple dose 정상상태가 일차적 관심.

**Eq.16-7 (R&T)** `[출처: Tozer 5e, Eq.16-7, p.503]`:

$$C_{u,ss} = \frac{K_m \cdot R_0}{V_m - R_0}$$

총농도 기준 변환: $K_m'  = K_m / f_u$. 따라서:

$$C_{ss}^{total} = \frac{K_m' \cdot R_0}{V_m - R_0}$$

**구조적 통찰**: 분모 발산 영역에서 phenytoin·alcohol이 운영. $R_0 \to V_m$일 때 Cu_ss → ∞.

#### B. Phenytoin — 변곡점 prototype `[출처: Tozer 5e, p.503–506]`

전형적 파라미터:
- $V_m \approx 500$ mg/day (개인차 200–1000)
- $K_m \approx 0.4$ mg/L (unbound)
- $f_u \approx 0.1$ → $K_m' = 4$ mg/L (총)
- 치료역: 10–20 mg/L

**1. Plateau 비례 위반 (Fig.16-9, p.503)**: Vm 접근 시 Css 발산. dashed line이 $K_m'$ (4 mg/L)에서 변곡점.

**2. F의 작은 변화 → Css의 큰 변화**:
환자: $K_m' = 3$ mg/L, $V_m = 425$ mg/day, 200 mg PO q12h, F=0.85에서 Css ≈ 12 mg/L. F=0.95 변경 시 Css ≈ 25 mg/L (*2배*).

**3. Time-to-plateau 비선형 발산 (Eq.16-10)**:

$$t_{90} = \frac{K_m' \cdot V \cdot (2.303 \cdot V_m - 0.9 \cdot R_0)}{(V_m - R_0)^2}$$

Fig.16-10 ($K_m'=4$, $V_m=500$, $V=50$):

| Dose (mg/day) | Css (mg/L) | t₉₀ |
|---|---|---|
| 300 | 6 | ~6일 |
| 350 | 9.3 | ~10일 |
| 400 | 16 | ~17일 |
| 425 | 22.7 | ~24일 |

**임상 함의**: dose 증량 후 *3주* trough 추적 권장.

**4. Vm vs Km' 변화의 비대칭성**:
$$\frac{C_{u,ss,2}}{C_{u,ss,1}} = \frac{V_{m,1} - R_0}{V_{m,2} - R_0}$$

#### C. Alcohol — zero-order plateau prototype `[출처: Tozer 5e, p.500–502]`

- $V_m \approx 10$ g/hr, $K_m \approx 100$ mg/L, $V_d \approx 42$ L/70kg
- 약리효과 ≈ 200 mg/L, 치사역 ≈ 5,000 mg/L

저농도 hepatic flow-limited: $V_m/K_m = 100$ L/hr ≈ 1.6 L/min (간 flow ≈ 1.4 L/min).

Hourly drink: 1 drink = 14 g; 4 drinks/hr (56 g/hr) → 5h에 200 g; 0.5 drink/hr (7 g/hr) Css = 233 mg/L.

Fig.16-7: input rate 효과 (water/cream/glucose). Fig.16-8: zero-order assumption — 5h infusion (Vm rate)이면 AUC=0.

#### D. Ascorbic acid — escape-valve prototype `[Tozer 5e, p.492; Table 16-4]`

| Daily intake | Css plasma |
|---|---|
| 75 mg | 9 mg/L |
| 1–3 g | 15.4 mg/L |
| 8–12 g | 19.5 mg/L |
| 10,000 mg | 19 mg/L |

**비대칭 응답**: 133배 dose가 농도 ~2배만. 두 saturable mechanism 동시:
1. Saturable absorption (F 감소)
2. Saturable renal reabsorption (CLR 0.5→21 mL/min)

Phenytoin이 *trap*이라면 ascorbic acid는 *self-limiting*.

#### E. Mixed pathway: CL_lin + saturable (Eq.16-11)

$$CL = CL_{lin} + \frac{V_m \cdot C}{K_m + C}$$
$$t_{1/2} = \frac{0.693 \cdot V}{CL_{lin} + V_m/(K_m+C)}$$

조건: $f_m \geq 0.5$일 때만 total CL 유의 비선형.

**Salicylic acid**: 저용량 t½ 2–3h; 과량 (>10 g) t½ 24h.

#### F. NONMEM 코딩 함의

```
$DES
DADT(1) = -(VM*A(1)/V) / (KM + A(1)/V)        ; pure MM
DADT(1) = -CL_LIN*A(1)/V - (VM*A(1)/V)/(KM+A(1)/V)  ; mixed
```

#### G. Zettelkasten Atom

```yaml
---
aliases: [Phenytoin Vm Km, Alcohol zero-order, Ascorbic acid plateau, Cu_ss formula]
tags: [pharmacometrics/nonlinear-pk, kinetics/capacity, clinical/tdm, tozer]
up: "[[M2 Michaelis-Menten 소거]]"
related: ["[[Phenytoin TDM]]", "[[Sheiner-Tozer 보정]]", "[[T6 경쟁적 억제]]"]
source: "Rowland & Tozer 5e, Ch.16, pp.491–506; Eq.16-7, 16-10, 16-11"
---

Cu_ss = Km·R₀/(Vm−R₀)는 임상 MM 정상상태식 — 분모 (Vm−R₀)가 발산 점근선. Phenytoin (Vm=500, Km'=4)은 dose가 Vm의 60–80% 영역에 살아 작은 변화가 비대칭 농도 변화. t₉₀이 (Vm−R₀)²에 반비례. Alcohol (Vm=10g/hr, Km=100)은 거의 zero-order. Ascorbic acid는 saturable absorption + reabsorption 합으로 self-limiting. 임상: Vm 근처는 작은 increment + 3주 추적.
```

---

### M3-EXT. Time-dependent kinetics — 임상 정량 layer

<!-- ANCHOR -->
Stage 1 M3·M4는 induction의 ODE 구조와 PK22 autoinduction. 본 EXT는 임상 prototype carbamazepine + verapamil chronopharm.

#### A. Carbamazepine autoinduction — turnover ~5일 prototype

**Fig.16-25 (p.518)**:
- 6 mg/kg PO daily × 22일
- Single-dose 예측 (induction 없으면): trough ≈ 14 mg/L 평탄
- 실제: trough day 7 (8 mg/L) → day 23 (4 mg/L)
- 효소 turnover time ≈ **5일**

**Stage 1 M4 PK22 비교**:
- PK22: $a=0.041$, $k_{out}=0.023$ h⁻¹ ($t_{1/2}^{ind}$ = 30h)
- Carbamazepine: turnover 5일

차이는 효소 종류 (CYP3A4 dominant)와 inducer 특성 — mechanism은 동일.

**임상 함의**: Day 1 t½로는 day 23 예측 불가. Plateau = 4–5 × turnover = 20–25일. Dose 적정 *최소 3주 간격*.

#### B. Verapamil chronopharmacokinetics (CONTEXT, Fig.16-24)

식사 + 위장 운동 + 효소 활성 + 단백 결합 circadian 합산. 시간 의존성의 가장 단순한 형태로 1줄 인지.

#### C. Aminoglycoside nephrotoxicity (CONTEXT)

Time-dependent CLR↓ — drug-induced 신독성으로 자기 청소율 감소. *Positive feedback toxicity*.

#### D. Stage 3 forward pointer

Tozer Ch.17 Eq.17-15 induction PK time course (phenobarbital-dicumarol Fig.17-17, 3–4주 plateau)는 본 EXT의 turnover 개념 *직접 호출* — 같은 mechanism의 *DDI* 형태 (T8 카드).

---

### M5-EXT. Nonlinear protein binding — Tozer 4가지 prototype

<!-- ANCHOR -->
Stage 1 M5는 open vs closed system 결론. 본 EXT는 Tozer의 4 prototype — 다른 결합 단백·다른 saturable mechanism.

#### A. Cefonicid — saturable albumin (Fig.16-18, p.513)

- 30 mg/kg IV bolus
- Total: 1구획 monoexponential
- Unbound: 첫 2h *훨씬 빠른 감소* → 이후 평행
- $f_u$ 0.18 → 0.04

**Mechanism**: 초기 albumin saturable → fu↑ → unbound CL↑. 농도 감소 시 fu↓ 재정상.
**오독 위험**: total monoexponential을 1구획 약물로 결론. NONMEM ADVAN1 부적절.

#### B. Trandolaprilat — ACE *자체* binding (Fig.16-19, p.514)

ACE inhibitor active metabolite. 결합 단백이 ACE enzyme — *low-capacity high-affinity*.

- AUC vs trandolapril dose (0.5–4.0 mg PO): 비선형
- Single dose semi-log: 4 dose terminal 갈라짐
- Multiple dose (2 mg q24h × 10d): accumulation ratio = **1.49** (long t½ 무관)
- $f_u$ 0.05 → 0.20

**Mechanism**: ACE는 plasma·vascular endothelium 분포, 농도 극저, 친화도 극고. 저 trandolaprilat → ACE에 결합 → renal CLR↓ → terminal long. 농도↑ → ACE saturable → fu↑ → CLR↑ → 빠른 elimination. Single dose만으로 *concentration-dependent binding*과 *2-compartment* 구별 불가 (p.514).

#### C. Naproxen — saturable albumin (Fig.16-17, p.512)

- Weak acid, MW 230, albumin 결합
- AUC vs single dose (0–4 g): plateau 향함
- V/F ≈ 9 L (대부분 albumin 결합)
- 100–200 mg/L = 430–870 µM ≈ albumin 600 µM

**Mechanism**: 고용량 albumin saturable → fu↑ → unbound CL↑ → AUC plateau. Total Css 일정해도 *unbound Css doubling*.

#### D. Disopyramide — α₁-AAG (Fig.16-16, p.510)

- 1.5 mg/kg IV
- Total CLR 60 → 30 mL/min (시간↑)
- Unbound CLR ≈ 200 mL/min 일정

**Mechanism**: 초기 고농도 α₁-AAG saturable → fu↑ → total CLR 외관상↑. Time → 농도↓ → fu↓ → total CLR↓. *Unbound CLR 농도 무관*.

#### E. 통합 패턴 — 4가지 prototype

| 약물 | 결합 단백 | Saturable 이유 | 임상 시그너처 |
|---|---|---|---|
| Cefonicid | Albumin | 단백 600 µM, 약물 그 영역 | Total monoexponential, unbound 빠른 감소 |
| Trandolaprilat | ACE 자체 | Target binding | Long terminal t½, accumulation 1.5 |
| Naproxen | Albumin | 약물 농도 ≈ albumin | AUC vs dose plateau |
| Disopyramide | α₁-AAG | AAG 15 µM | Total CLR 시간 의존 |

**공통**: $C_b = n\cdot P_t \cdot C_u/(K_d+C_u)$ saturation. **차이**: $n\cdot P_t$ (capacity).

#### F. Salicylic acid — *opposing nonlinearities* prototype (Fig.16-28)

p.522 핵심 통찰:
- $f_u$↑ with C (saturable albumin) → CL↑
- $CL_u$↓ with C (saturable metabolism) → CL↓

**결과**: 치료역 (10–60 mg/L) total CL 일정 (Fig.16-28B). *Unbound* Cu_ss는 dosing rate에 비대칭 증가 (Fig.16-29).

**진단 통합 (Fig.16-28의 4-step)**:
1. t½ 시간 의존
2. Urinary metabolite 비율 변화 → saturable metabolism
3. Plasma binding fu↑ with C → saturable binding
4. 두 mechanism 동시

#### G. Stage 3 forward

Trandolaprilat ACE binding은 **TMDD** (T3) 핵심 사례. T5 (Stage 3 displacement-only DDI 재해석)에서 Phenytoin–Valproate (Fig.17-3) 본 카드 mechanism으로 직접 해석.

---

### T1. 포화 신장 이송 — Saturable Renal Transport (Tozer-only)

<!-- MASTER LENS -->
> **[개념 Big Idea]**
>
> **왜 치명적**: 신부전 환자 dicloxacillin 의사가 "MIC 도달 안 되니 dose 2배"한다 — Fig.16-13에서 1g CLR=104, 2g CLR=63 mL/min (40%↓). Dose 2배인데 CLR 줄어 AUC가 *4배 가까이* 증가. Tubular secretion saturable mechanism 모르면 antibiotic toxicity (penicillin family neurotoxicity, seizure).
>
> **체화 직관**: 신장 운반체 (secretion·active reabsorption)는 metabolism과 *동일* MM 구조 ($Rate = T_m\cdot C_u/(K_T+C_u)$). 단, *방향*이 약물별 두 가지. Secretion saturable → CLR↓ with dose; reabsorption saturable → CLR↑ with dose.

#### A. Formal Definition (Eq.16-3, p.495)

$$Rate = \frac{T_m \cdot C_u}{K_T + C_u}$$

#### B. 두 방향 분기 (Fig.16-14)

- **Curve A — Filtration only**: $CL_R = f_u \cdot GFR$ 일정
- **Curve B — Secretion saturable**: 저C CLR↑↑, 고C CLR→GFR (penicillin G, dicloxacillin)
- **Curve C — Reabsorption saturable**: 저C CLR↓↓, 고C CLR→GFR (ascorbic acid, glucose)

**진단**: dose-normalized CLR vs dose. ↓ = secretion, ↑ = reabsorption, 일정 = filtration.

#### C. Dicloxacillin — saturable secretion (Fig.16-13)

- $f_u = 0.04$
- 1g IV: $CL_R = 104$ mL/min vs filtration 예상 ($f_u \cdot GFR = 4.8$) — 22배
- 2g IV: $CL_R = 63$ mL/min (40%↓)
- Extrarenal CL dose 무관 → 신장 단독

#### D. Ascorbic acid — saturable reabsorption (Fig.16-15)

- 9 mg/L → CLR 0.5; 19 mg/L → CLR 21 mL/min (42×)
- 두 mechanism 동시 (intestinal + renal) → escape valve

#### E. Glucose — Tm prototype (renal threshold)

10–14 mM까지 거의 0 → 그 이상 selectively excreted. 당뇨 진단 historical 기반.

#### F. 흡수 saturable transport (소장 — CONTEXT)

- Amoxicillin: PEPT1 (Fig.16-5)
- Vitamin B12: intrinsic factor (Table 16-5: 0.5 µg → 80% vs 500 µg → 1.1%)
- Griseofulvin: solubility-limited (Fig.16-4)

#### G. NONMEM

```
$PK
CL_REN = TM_R / (KT + (A(1)/V))   ; saturable secretion
CL = CL_REN + CL_NR
```

#### H. Zettelkasten Atom

```yaml
---
aliases: [Saturable renal transport, Tubular secretion saturable, Tubular reabsorption saturable]
tags: [pharmacometrics/nonlinear-pk, kinetics/transport, renal, tozer]
up: "[[비선형 PK MOC]]"
related: ["[[Dicloxacillin]]", "[[Ascorbic acid]]", "[[Penicillin G]]", "[[T9 Transporter DDI]]"]
source: "Tozer 5e, pp.506–510, 515; Eq.16-3; Fig.16-13/14/15"
---

신장 transport은 metabolism과 동일 MM. 진단 첫 단추 = *방향*: dose↑ 시 CLR↓ (secretion) vs CLR↑ (reabsorption). Dicloxacillin 1g→2g: 104→63 mL/min — secretion. Ascorbic acid 9→19 mg/L: 0.5→21 — reabsorption. 임상: secretion-saturable의 dose↑은 AUC 비선형↑ → toxicity; reabsorption-saturable은 self-limiting. NONMEM CL_REN 자체를 농도 함수로.
```

---

### T2. 포화 First-Pass Metabolism

<!-- MASTER LENS -->
> **[개념 Big Idea]**
>
> **왜 치명적**: Nicardipine 10 mg q8h F=19% 측정 → "high-extraction" 결론 → PopPK fixed F=0.19 → 30 mg q8h dose escalation 시 환자가 *예측의 1.7배* AUC → toxicity. F가 dose에 따라 *증가*하는 것을 "흡수율 변동성"으로 오해.
>
> **체화 직관**: First-pass는 *MM의 표면화*. Hepatic intrinsic clearance가 $V_m/(K_m+C)$이므로 oral dose↑ → portal C↑ → 간 saturate → *F가 dose↑에 따라 증가*. 단 *systemic CL은 변하지 않을 수 있다* — systemic 농도가 Km 미만이면 systemic linear.

#### A. Formal Definition

$$F_H = \frac{Q_H}{Q_H + Cl_{int}} = \frac{Q_H}{Q_H + V_m/(K_m + C_{portal})}$$

$C_{portal}$↑ → $Cl_{int}$↓ → $F_H$↑.

#### B. Nicardipine — prototype (Table 16-2)

| Dose (mg q8h) | F (%) |
|---|---|
| 10 | 19 (4) |
| 20 | 22 (5) |
| 30 | 28 (5) |
| 40 | 36 (6) |

**임상 함의**: dose 4× → F 1.9× → AUC ratio 7.6× for 4× dose.

**Systemic CL 검증** (IV tracer 0.885 mg 동시): IV CL 변화 없음 — *first-pass*만 saturable.

#### C. Methylphenidate — enantiomer (Fig.16-6)

라세미체 30 mg PO:
- (+)-isomer (active): F ≈ 20%
- (−)-isomer: F ≈ 4%
- Ritalinic acid metabolite: 양 isomer 동일

**Mechanism**: 같은 carboxylesterase, 다른 affinity. Stage 1 CTX-4 (M9 enantiomer) Eq 3:53의 *PK 버전*.

#### D. Stage 3 forward — Diltiazem-Lovastatin (CRITICAL)

T9 (Stage 3) Table 17-7 핵심:
- AUC ratio **1.27 IV vs 3.57 oral**
- Lovastatin = high-E + first-pass; IV → first-pass 우회
- Diltiazem이 first-pass 효소 억제 → oral AUC dramatic, IV minimal

**본 T2 카드 mechanism이 그대로 *DDI route effect*의 기반**.

#### E. NONMEM

```
$PK
F1 = QH / (QH + VM/(KM + DOSE/V_PORTAL))
; 또는 dose covariate: F1 = θ_F0 * (1 + θ_DOSE * (DOSE - DOSE_REF))
```

#### F. Zettelkasten Atom

```yaml
---
aliases: [Saturable first-pass, Nicardipine F, Hepatic capacity-limited bioavailability]
tags: [pharmacometrics/nonlinear-pk, kinetics/first-pass, oral, tozer]
up: "[[비선형 PK MOC]]"
related: ["[[Nicardipine]]", "[[Methylphenidate enantiomers]]", "[[T9 Diltiazem-Lovastatin]]"]
source: "Tozer 5e, pp.498–499; Table 16-2; Fig.16-6"
---

First-pass capacity-limited 시 oral F가 dose↑에 *증가*. Nicardipine 10→40 mg: F 19→36%, AUC 7.6× for 4× dose. Systemic CL은 saturable 아닐 수 있음 (Km을 systemic 안 초과). Paradox = 진단 핵심: F 비선형, t½ dose 무관. Methylphenidate enantiomer 5× F 차이 = same mechanism, different esterase affinity. DDI route effect (Diltiazem-Lovastatin: 1.27 IV vs 3.57 oral) mechanism 기반.
```

---

### T3. Target-Mediated Drug Disposition (TMDD) — 기초

<!-- MASTER LENS -->
> **[개념 Big Idea]**
>
> **왜 치명적**: Bosentan dose escalation에서 *V_d가 dose↓ 따라 감소* — 10mg=0.67 L/kg, 750mg=0.16 L/kg (Fig.16-20). V_d를 "고정 약리 상수"로 가정 → dose-response 해석 무너짐. TMDD는 *효과 결합 자체가 PK 결정* — PK·PD 분리 불가.
>
> **체화 직관**: TMDD에서 *target binding*이 효과 mediate함과 동시에 *분포·제거의 saturable mechanism*. 일반 plasma protein binding과 다름 — 결합 단백이 *receptor* 자체.

#### A. Formal Definition

약물이 target site에 *고친화·저용량* binding:
1. PD를 mediate
2. PK (V_d, CL)를 비선형 영향

#### B. 다섯 prototype

**(1) Bosentan — saturable tissue binding (Fig.16-20)**:
- Endothelin receptor antagonist
- $V_{ss}$: 10mg=0.67 → 750mg=0.16 L/kg
- 저C V_d↑ = receptor sequester

**(2) Imirestat — aldose reductase (Fig.16-21)**:
- 단일 dose 2/10/20/50mg PO
- 6–36h dose-normalized 다른 위치 → 96h 역전
- AUC dose-normalized wide range 일정

**(3) Trandolaprilat — ACE binding** (M5-EXT B 본문):
- accumulation 1.49 despite long t½

**(4) Draflazine — RBC nucleoside transporter (Fig.16-22, 16-23)**:
- Plasma vs whole blood profile *완전 다름*
- 0.1 plasma → 30 ng/mL blood; 100 plasma → 90 blood (1000× plasma → 3× blood)
- 측정 매트릭스가 PK 해석 *완전 변경*

**(5) Mitoxantrone — DNA intercalation**:
- 효과 mechanism = 분포 dominant determinant
- Tissue Kp ∝ DNA content

#### C. PK·PD 분리 불가

- 전통: PK = "drug get to target", PD = "drug do something"
- TMDD: *모두 한 mechanism*

**임상**: target occupancy가 PK도 결정. Target concentration covariate.

#### D. 구별 — TMDD vs 일반 plasma protein binding (M5-EXT)

| 측면 | M5-EXT | TMDD |
|---|---|---|
| 결합 단백 | Albumin/AAG (대용량) | Receptor (소용량) |
| 결합 농도 | mM | nM |
| Open system 결론 | Cu = K⁰/CLu (단백 변화 무영향) | Dose 변화 자체가 PK 변경 |
| Vd | 농도 무관 | 농도 의존 |
| 약물 | Phenytoin, naproxen | Bosentan, mAb |

#### E. Stage 3 + Session I-08 cross-link

본 T3 = small molecule TMDD. Session I-08 antibody PK = 단백 의약품 (≫ 50 kDa) 적용.

#### F. NONMEM (quasi-equilibrium TMDD, Mager-Jusko 2001)

```
$DES
DADT(1) = -KEL*A(1) - KON*A(1)*A(2)/V + KOFF*A(3)
DADT(2) = -KON*A(1)*A(2)/V + KOFF*A(3) - KDEG*A(2) + KSYN
DADT(3) = KON*A(1)*A(2)/V - KOFF*A(3) - KINT*A(3)
```

#### G. Zettelkasten Atom

```yaml
---
aliases: [Target-mediated drug disposition, TMDD, Saturable tissue binding, Bosentan kinetics]
tags: [pharmacometrics/nonlinear-pk, tmdd, protein-binding, tozer]
up: "[[비선형 PK MOC]]"
related: ["[[Antibody PK Session I-08]]", "[[Bosentan]]", "[[Trandolaprilat]]", "[[T5 Displacement DDI]]"]
source: "Tozer 5e, pp.515–516; Fig.16-20/21/22/23"
---

TMDD: target binding이 효과 + PK saturable mechanism 원천. Plasma binding의 극한 (low capacity, high affinity). Bosentan V_ss dose↓ 따라 감소. Draflazine plasma vs blood 완전 다름. PK·PD 분리 불가가 핵심. Dose 조정 자체가 PK 변경. 단백 의약품 PK fundamental.
```

---

### T4. Mechanism-Based Inhibition (MBI) — Suicide Substrate

<!-- ANCHOR -->
M3 induction이 turnover의 *합성 가속*이라면, T4 MBI는 turnover의 *분해 가속*. 같은 ODE 구조의 정반대 방향.

<!-- MASTER LENS -->
> **[개념 Big Idea]**
>
> **왜 치명적**: Clarithromycin 단일 dose t½ ~3h → multiple dose day 7 t½ ~9h (Fig.16-26). HIV 환자 saquinavir/ritonavir와 함께 → Day 7 *예상의 3배* → QT 연장 → torsade. MBI는 *시간 의존·비가역* — 일반 competitive (분 단위 평형)과 *근본적으로 다른 dynamics*.
>
> **체화 직관**: MBI inhibitor는 enzyme의 substrate로 들어가 enzyme을 *covalently 비가역 inactivate*. "Suicide substrate". 회복 = *new protein synthesis*만 → t½_recovery = t½_enzyme. M3 induction의 *시상수 같지만 방향 반대*.

#### A. Formal Definition

$$\frac{dE}{dt} = R_{in} - k_{out} \cdot E - \frac{k_{inact} \cdot [I] \cdot E}{K_I + [I]}$$

새 정상상태:

$$E_{ss}^{MBI} = \frac{R_{in}}{k_{out} + k_{inact} \cdot I/(K_I + I)}$$

#### B. Clarithromycin — prototype `[Tozer 5e, p.518–519, Fig.16-26]`

- $k_{inact} = 0.07$ min⁻¹
- $k_E$ ≈ 0.23 day⁻¹ → t½_enzyme ≈ **3일**
- $k_{inact}/k_E = 438$ (438× inactivation rate)
- $C_{u,I}/K_I = 0.025$ → **11배 CL 감소** (T4-EXT Eq.17-14에서 정량 도출)

**Fig.16-26**:
- 250 mg single → AUC small, t½ short
- 500 mg single → 2.5× (이미 dose-disproportional)
- Day 7 (250 mg q12h ×7): AUC, t½ 모두 단일 대비↑
- Day 7 (500 mg q12h ×7): 가장 큰 AUC + t½

#### C. M3 induction과 비교 — turnover 두 방향

| 측면 | M3 Induction | T4 MBI |
|---|---|---|
| Effect | $R_{in}$↑ | $k_{out}$↑ (effective) |
| E^ss | ↑ | ↓ |
| 시상수 | $1/k_{out}$ | $1/(k_{out} + k_{inact}I/(K_I+I))$ |
| 회복 | $1/k_{out}$ | $1/k_{out}$ (original) |
| Prototype | Carbamazepine (~5d) | Clarithromycin (~3d) |

**핵심 mirror**: 두 mechanism 모두 *효소 turnover ODE 변형*, *어느 항*이 다르다.

#### D. 다른 MBI prototype

- **Ticlopidine**: 단일 250 mg t½=2h → 수 주 후 4–5일 (>50배). Study problem 2 (p.525).
- **Clopidogrel**: 활성 metabolite가 P2Y12 *비가역 covalent* — 별개 mechanism이나 dynamics 유사.

#### E. NONMEM

```
$DES
DADT(1) = -CL_DRUG*A(1)/V                                      ; drug central
DADT(2) = R_IN - K_OUT*A(2) - K_INACT*A(1)/V*A(2)/(K_I+A(1)/V) ; enzyme
$PK
CL_DRUG = (V_MAX*A(2)/E_REF) / (K_M + A(1)/V)                  ; CL ∝ E(t)
```

핵심: enzyme compartment 별도 ODE. Multiple-dose 시 enzyme state maintain.

#### F. Stage 3 forward — quantitative MBI (T4-EXT)

Tozer Ch.17 Eq.17-13/14가 본 카드의 *정량 prediction 형태*. Clarithromycin parameter 대입 시 11× CL 감소 prediction이 mechanism으로부터 직접 도출.

#### G. Zettelkasten Atom

```yaml
---
aliases: [Mechanism-based inhibition, MBI, Suicide substrate, Enzyme inactivation kinetics]
tags: [pharmacometrics/nonlinear-pk, kinetics/time-dependent, autoinhibition, tozer]
up: "[[효소 turnover 모델]]"
related: ["[[Clarithromycin]]", "[[Ticlopidine]]", "[[T4-EXT MBI 정량]]", "[[T8 Induction time course]]"]
source: "Tozer 5e, pp.518–519; Fig.16-26; Eq forward Ch.17 Eq.17-13/14"
---

MBI: 약물이 enzyme substrate가 되어 *비가역 inactivate*. dE/dt = Rin − kout·E − kinact·I·E/(KI+I) — M3 induction turnover ODE에 *분해 항 추가*. Recovery 시상수 = enzyme t½ (carbamazepine ~5d, clarithromycin ~3d). kinact=0.07/min, kE≈0.23/day, ratio=438. 단일 vs multiple dose 질적으로 다른 profile. 임상: macrolide·protease inhibitor·H2 blocker multiple dose DDI 단일 dose data로 불가.
```


---

### Stage 3 카드 (T4-EXT + T5–T10) — DDI 정량 prediction layer

*Tozer Ch.17의 핵심 정량 framework. Stage 1·2 mechanism을 전제로 FDA DDI Guidance·NDA 의사결정 언어로 외화.*

---

### T4-EXT. MBI 정량 — Eq.17-13/14 (Stage 2 T4 발전)

<!-- ANCHOR -->
Stage 2 T4가 MBI mechanism (turnover ODE에 분해 항 추가)이라면, 본 EXT는 그 ODE에서 *정상상태 CL 감소비*를 *직접 계산하는 정량 formula*. FDA DDI Guidance에서 macrolide·protease inhibitor·H2 blocker MBI inhibitor classification (Table 17-5의 mechanism-based 표시 항목)의 mathematical 기반.

<!-- MASTER LENS -->
> **[개념 Big Idea]**
>
> **왜 치명적**: Clarithromycin 임상 plasma 0.7 mg/L, fu=0.25, K_I=7 mg/L → **Cu_I/K_I = 0.025** (in vitro). 이 값을 reversible inhibition Eq.17-9에 대입하면 1.025× — 즉 *임상적으로 무시할 만한 inhibitor*. 그러나 실제 midazolam AUC가 7×↑ (oral) / 2.7×↑ (IV) — 강력한 inhibitor (Fig.17-13). 이 280×의 격차가 mechanism-based의 *시상수 증폭 인자* $k_{inact}/k_E$. 본 EXT의 Eq.17-13/14를 모르면 in vitro $K_I$가 작아 보여도 임상 in vivo에서는 *치명적 DDI*인 약물을 놓친다.
>
> **체화 직관**: MBI 정량 = *Cu_I/K_I이 본질적 measure가 아니라*, $k_{inact} \cdot Cu_I / (K_I \cdot k_E)$이 *효과 modifier*. 즉 *enzyme 분해의 시상수 비율*이 reversible inhibition의 *결합 친화도 비율*을 대체한다. 이 modifier가 1×보다 훨씬 클 때 dramatic CL 감소.
>
> **이 직관을 머릿속에 박고 아래를 읽어라**: Eq.17-13/14에서 $Cu_I/K_I$을 그대로 쓰지 말고, 항상 $k_{inact}/k_E$ 곱한 값으로 변형하여 reversible Eq.17-10과 동일 형태로 비교하라.

#### A. Formal Definition (Eq.17-13/14)

기본 (substrate fm = 1, single pathway):

$$CL_{f,\text{inhibited}} = CL_{f,\text{normal}} \cdot \left[\frac{1}{1 + k_{inact} \cdot \dfrac{Cu_I}{K_I \cdot k_E}}\right] \quad \text{[Eq.17-13]}$$

다중 pathway substrate (fm = affected pathway 비율):

$$CL_{\text{inhibited}} = CL_{\text{normal}} \cdot \left[\frac{f_m}{1 + k_{inact} \cdot \dfrac{Cu_I}{K_I \cdot k_E}} + (1 - f_m)\right] \quad \text{[Eq.17-14]}$$

**Eq.17-10 (reversible, 비교용)**:

$$CL_{\text{inhibited}} = CL_{\text{normal}} \cdot \left[\frac{f_m}{1 + Cu_I/K_I} + (1 - f_m)\right]$$

**핵심 비교**: Eq.17-10의 $Cu_I/K_I$가 Eq.17-14에서 $k_{inact} \cdot Cu_I / (K_I \cdot k_E)$로 *치환*된다. 즉 $k_{inact}/k_E$가 *modifier multiplicative factor*.

#### B. Clarithromycin — Tozer 정량 case study `[출처: Tozer 5e, p.557–558]`

**파라미터**:
- 임상 dose: 500 mg PO BID, average plateau plasma C ≈ 0.7 mg/L
- $f_u$ = 0.25 (in plasma)
- $K_I = 7$ mg/L (in vitro CYP3A4 inhibition)
- $k_{inact} = 0.07$ min⁻¹ (in vitro enzyme inactivation rate)
- $k_E$ ≈ 0.23 day⁻¹ (CYP3A4 endogenous degradation rate)

**계산**:
- $C_u = 0.7 \times 0.25 = 0.175$ mg/L (unbound plasma)
- $Cu_I/K_I = 0.175 / 7 = 0.025$
- $k_{inact}/k_E$ = $0.07 \text{ min}^{-1} \times (1440 \text{ min/day}) / 0.23 \text{ day}^{-1}$
  - = $100.8 / 0.23$ = **438** (단위 통일 후)
- Modifier $k_{inact} \cdot Cu_I / (K_I \cdot k_E)$ = 438 × 0.025 = **10.95**

**Reversible 가정 (Eq.17-10)** — midazolam (fm ≈ 1):
- AUC ratio (Eq.17-11) = $1 / (1/(1+0.025))$ = **1.025**
- → "weak inhibitor 정도도 못 됨"

**MBI 가정 (Eq.17-14)** — midazolam (fm ≈ 1):
- AUC ratio = $1 / (1/(1+10.95))$ = **11.95**
- → 약 **11–12배 AUC 증가** prediction

**임상 관측 (Fig.17-13)**:
- Midazolam IV AUC: 2.7× ↑
- Midazolam oral AUC: 7× ↑

**Mechanism prediction과의 정합**: 11–12× prediction이 임상 7× (oral) / 2.7× (IV)와 *order of magnitude* 일치. IV가 작은 이유는 *gut wall CYP3A4* 영향 부재. Mechanism이 정확히 reproduce.

#### C. Strong inhibitor 분류 (Table 17-5) — MBI 추가 기준

Table 17-5의 mechanism-based 표시 항목 (각주 b):
- **Strong**: Clarithromycin, Ritonavir, Telithromycin (CYP3A)
- **Moderate**: Diltiazem, Erythromycin, Grapefruit juice (CYP3A)

**핵심**: Reversible inhibitor는 $Cu_I/K_I$만으로 분류 가능. MBI는 $Cu_I/K_I$ + $k_{inact}/k_E$ *둘 다* 필요. *임상 dose 영역*에서의 modifier 값이 분류 기준.

#### D. 회복 시간 — *반드시* enzyme t½

**핵심 차이점**: Reversible inhibitor 제거 시 즉시 회복. MBI는 *enzyme 합성 회복* 필요.

- CYP3A4 t½(enzyme) ≈ 3일 (보고에 따라 2주까지) `[출처: Tozer 5e, p.558]`
- Recovery to normal = 3.3 × t½ ≈ **2주 이상** (CYP3A4 기준)

**임상 함의**:
1. MBI inhibitor 제거 후 다른 substrate를 추가할 때 **2주 wash-out** 권고
2. Single dose 연구로 multiple-dose DDI prediction 불가
3. NONMEM model에서 enzyme compartment를 *별도 ODE로 maintain*해야 (Stage 2 T4 코드 참조)

#### E. Multifaceted MBI sources (CONTEXT)

Tozer Ch.17 본문 (p.557): clarithromycin metabolic intermediate complex with heme moiety of CYP3A4. 다른 MBI mechanism:
- **Ritonavir**: covalent CYP3A4 binding
- **Diltiazem**: 본 카드 mechanism + active metabolite (T9에서 lovastatin route effect와 연결)
- **Grapefruit juice**: furanocoumarins이 gut wall CYP3A4 MBI

#### F. Stage 1 M3 ODE와 mathematical 동등성

Stage 1 M3 turnover: $dE/dt = R_{in} - k_{out} \cdot E$.

T4 MBI: $dE/dt = R_{in} - k_{out} \cdot E - k_{inact} \cdot I \cdot E/(K_I + I)$.

정상상태 ($dE/dt = 0$):
$$E^{ss}_{MBI} = \frac{R_{in}}{k_{out} + k_{inact} \cdot I/(K_I + I)} = \frac{E^{ss}_{normal}}{1 + k_{inact}/(k_{out}) \cdot I/(K_I + I)}$$

CL ∝ E이므로 $CL^{ss}_{MBI} / CL^{ss}_{normal} = E^{ss}_{MBI} / E^{ss}_{normal}$ — 이것이 Eq.17-13의 mathematical 도출.

따라서 **본 EXT는 Stage 1 M3 turnover ODE의 정상상태 해**일 뿐, 새로운 mechanism 아님. Stage 1 정본 + T4 분해 항 추가 = 본 정량 formula.

#### G. NONMEM 함의 (T4 코드의 임상 적용)

```
$PK
; --- enzyme compartment ---
KOUT_ENZ = 0.23/24      ; hr⁻¹ (CYP3A4)
KINACT   = 0.07*60      ; hr⁻¹ (clarithromycin)
KI       = 1.75         ; mg/L (Cu_I 기준, fu*KI total = 7 mg/L)
RIN_ENZ  = KOUT_ENZ * 1 ; baseline E^ss = 1 (relative)

; --- substrate (midazolam) ---
CL_BASE  = 30           ; L/hr, midazolam baseline CL
FM       = 0.95         ; CYP3A4 fraction

$DES
DADT(1) = -CL_DRUG*A(1)/V                                          ; midazolam
DADT(2) = -CL_INHIB*A(2)/V_INHIB                                   ; clarithromycin
DADT(3) = RIN_ENZ - KOUT_ENZ*A(3) - KINACT*(A(2)/V_INHIB)/(KI + A(2)/V_INHIB)*A(3)
                                                                   ; CYP3A4 enzyme
$PK
CL_DRUG = CL_BASE * (FM*A(3) + (1-FM))   ; A(3) = E(t)/E_ss = relative enzyme
```

#### H. Stage 3 forward — T6 reversible과의 통합 framework

T6 (다음 카드)는 *Eq.17-9~17-12 reversible competitive*. 본 T4-EXT와 합쳐 Tozer Ch.17의 *DDI 정량 prediction framework 완성*. FDA DDI Guidance Eq.17-11 AUC ratio를 본 두 카드가 *직접 도출*.

#### I. Zettelkasten Atom

```yaml
---
aliases: [MBI quantitative, Eq.17-13, Eq.17-14, Clarithromycin 11-fold prediction]
tags: [pharmacometrics/ddi, kinetics/time-dependent, fda-guidance, tozer]
up: "[[T4 MBI mechanism]]"
related: ["[[T6 경쟁적 억제 정량]]", "[[T8 Induction PK time course]]", "[[FDA DDI Guidance]]"]
source: "Tozer 5e, Ch.17, pp.557–558; Eq.17-13, 17-14; Fig.17-13"
---

MBI 정량 (Eq.17-14): CL_inh = CL_normal × [fm/(1 + kinact·Cu_I/(K_I·kE)) + (1-fm)]. Eq.17-10 reversible의 Cu_I/K_I가 *kinact·Cu_I/(K_I·kE)로 치환* — kinact/kE가 modifier. Clarithromycin: kinact=0.07/min, kE=0.23/day, ratio=438. Cu_I/K_I=0.025. Modifier=10.95 → 11.95× CL 감소 prediction (vs reversible 1.025×의 280× 증폭). 임상 midazolam 7× oral / 2.7× IV와 order 일치. 회복=enzyme t½ (CYP3A4 3d → 2주). NONMEM enzyme compartment 별도 ODE.
```

---

### T5. Displacement-Only DDI 재해석 — Acute vs Plateau의 진단 framework

<!-- MASTER LENS -->
> **[개념 Big Idea]**
>
> **왜 치명적**: Tozer Ch.17 historical lesson (p.562) — "warfarin–phenylbutazone fatal bleeding의 원인은 displacement"라는 1967년 가설이 *수십 년간 임상의 사고*를 형성. 결과: 임상의가 *displacement interactions에 과도하게 경계*하여 모든 단백 결합 약물 조합에 dose 조정 시도 → false economy + true mechanism (inhibition) missed. Phenytoin–valproate (Fig.17-3) 데이터를 보면 *total Css↓ 일정 unbound* — *순수 displacement는 dose 조정 사유 아님*. 그러나 warfarin–phenylbutazone에서는 *unbound도 sustained 증가* — 이것이 진정한 mechanism (inhibition + displacement) signature.
>
> **체화 직관**: Displacement 진단의 단일 question = "*unbound C가 transient (h–day) 또는 sustained (지속)?*" Transient = 순수 displacement = 무영향. Sustained = 추가 mechanism (보통 inhibition) = 임상 위험. 이 진단으로 *displacement-only는 dose 조정 사유 아니다*는 Stage 1 M5 open system 결론을 임상 적용.
>
> **이 직관을 머릿속에 박고 아래를 읽어라**: 본 카드는 Stage 1 M5의 open system 수식 ($Cu = K^0/CLu$, 단백 변화 무영향)이 임상 시나리오에서 *어떻게 검증되는지*의 케이스 모음. Warfarin–phenylbutazone은 *순수 displacement가 아닌* 사례. 이 중요한 차이가 1967년 가설이 1980년대까지 지속된 이유.

#### A. Tozer Ch.17 displacement framework (Eq.17-1–17-3)

**Eq.17-1**: $V = V_p + V_T \cdot \frac{f_u}{f_{u,T}}$ — 단백 결합이 V에 미치는 영향.

**Eq.17-2**: $CL_u \cdot Cu = CL \cdot C$ — unbound clearance equality.

**Eq.17-3** (low extraction, infusion): $R_{inf} = CL_{int} \cdot Cu_{ss} = CL \cdot C_{ss}$.

**핵심 결론** (Stage 1 M5 재확인): low-extraction drug에서 displacement는 fu↑·CL↑·C↓ 동시 일으키나 *Cu는 불변*. → **Cu 기반 임상 효과 변화 없음** = dose 조정 불필요.

#### B. 진단 framework — Acute vs Plateau

**Acute events (단발 dose 또는 시작 직후)**:
- 일반적으로 *transient* — Vu (unbound volume) 변화로 redistribution
- 예외: small Vd (< 15 L/70 kg) + plasma binding 약물에서 sustained Cu↑ 가능

**Events at plateau (chronic dosing)**:
- Low extraction ratio: **Cu 변화 없음** (Eq.17-3 적용; Fig.17-2 left)
- High extraction IV: **Cu↑** (드물게 fentanyl에서 conceivable; 임상 보고 없음)
- High extraction oral: **CL↓ + F↓ 부분 상쇄** → 작은 Cu 변화 (Fig.17-2 right)

**시간 차원 (Fig.17-4)**:
- Displacer가 drug보다 *느린* kinetics → drug는 항상 virtual steady state → *Cu 불변*
- Total C는 displacer 농도에 *역상관* 변동 (displacement 정도 반영)

#### C. Phenytoin–Valproate (Fig.17-3, p.543) — *순수 displacement* prototype

**임상 데이터** (Mattson et al. 1978):
- N = 25 patients stabilized on phenytoin
- + 11 patients receive 900 mg/day sodium valproate
- + 9 patients receive 1350 mg/day

**관측**:
| 군 | Total C (mg/L) | Unbound C |
|---|---|---|
| Phenytoin alone | ~14 | unchanged baseline |
| + 900 mg valproate | ~12 | unchanged |
| + 1350 mg valproate | ~10 | unchanged |

- Total C는 valproate dose 증가에 따라 감소
- Unbound C는 *변화 없음*

**임상 함의**: phenytoin은 low extraction, fu↑이 CL↑로 직접 cancel. → *Phenytoin dose 조정 불필요*.

**Stage 1 M5 결론과의 정합**: 본 사례가 open system (Cu = K⁰/CLu, 단백 변화 무영향) 결론의 *임상 검증*. 단순 임상 시나리오에서 Stage 1의 mechanism 직접 confirm.

#### D. Warfarin–Phenylbutazone (Fig.17-18) — *Displacement + Inhibition* multifaceted

**임상 시나리오 (Schary et al. 1975)**:
- Warfarin 10 mg/day daily + days 13–22: phenylbutazone 100 mg t.i.d.

**Warfarin baseline**:
- Total Css ≈ 4 mg/L
- $f_u$ = 0.005 (Cu = 0.02 mg/L)
- F ≈ 1.0, CL ≈ 0.1 L/hr (low extraction, highly bound)

**Phenylbutazone baseline**:
- Css plateau ≈ 100 mg/L (10일째 도달)
- $f_u$ = 0.004–0.010, t½ = 3 days

**관측 데이터 (Fig.17-18)**:
- Total warfarin C: 4 → 2 mg/L (절반 감소)
- $f_u$ warfarin: 0.005 → 0.015 (3배 증가)
- **Cu warfarin**: 0.02 → 0.03 mg/L (sustained 증가)
- 약리효과 (prothrombin time): sustained 증가

**Mechanism 분석**:
- Cu가 *sustained 증가*는 Eq.17-3로부터 $R_{inf}/CL_{int}$ 증가를 의미
- Dose 변화 없음 → *$CL_{int}$ 감소* (즉 inhibition)
- 후속 metabolite 분석: phenylbutazone이 7-(S)-hydroxywarfarin 형성 inhibit (S-warfarin metabolism, 5× active isomer)

**1967년 Aggeler 가설의 오류**:
- "Total C 감소 = displacement"라는 partial 정확
- 실제는 *displacement + S-warfarin selective inhibition*
- Displacement만으로는 sustained Cu↑ 설명 불가 (Eq.17-3로부터)

**임상 함의 (재해석)**:
- "Warfarin 단백 결합에 대한 displacement 약물 주의" → *과잉 일반화*
- 진정한 위험 = Selective S-warfarin inhibition (CYP2C9 inhibitor: amiodarone, fluconazole, sulfinpyrazone — Table 17-5)
- 단순 displacement (e.g., naproxen): 임상 의의 적음 (Fig.17-3 phenytoin–valproate 모델)

#### E. 통합 결론 — Displacement-only는 dose 조정 사유 아님

**Tozer Ch.17 명시 (p.540, p.563)**:
> "Displacement interactions in plasma have been studied primarily in vitro... Substantial displacement is frequently demonstrated, yet this may be of little therapeutic consequence."

**Stage 1 M5 → Stage 3 T5 일관성**:
- Stage 1 M5 (mechanism): Open system → 단백 변화 무영향
- Stage 2 M5-EXT (4 prototype): 단백 결합 변화는 임상 시그너처일 뿐 dose 조정 사유 아님
- Stage 3 T5 (DDI 적용): *Displacement-only DDI 임상 의의 미미*

**진단 알고리즘**:
1. Total Css 변화 측정 + Unbound Cu 직접 측정
2. Cu transient/return-to-baseline → 순수 displacement → no action
3. Cu sustained 변화 → 추가 mechanism (보통 inhibition) → 본격 진단 (T6 framework로 이동)

#### F. 단백 결합 약물 high-V 사례 (CONTEXT, p.541)

V = 100 L 약물에서 fu = 0.01 → bound plasma = 3% of body amount. 100% displacement 시 Cu marginally 증가. → *Vd 큰 약물의 displacement 임상 의의 거의 없음*.

#### G. NONMEM 함의

```
$PK
; Stage 1 M5 open system 수식 직접 적용
FU_VICTIM   = THETA(1)                 ; baseline fu
FU_DISPL    = THETA(2)*(1+THETA(3)*A(2)/V_DISPL)  ; displacer-dependent fu
CL_VICTIM   = CL_INT * FU_VICTIM       ; CL = CLint * fu
CL_VICTIM_INHIB = CL_VICTIM * THETA(4) ; inhibition factor (separate from displacement)
```

**핵심**: Displacement effect는 fu에, inhibition effect는 CL_INT에 *분리* covariate로. 합쳐서 modeling하면 진단 식별 불가.

#### H. Zettelkasten Atom

```yaml
---
aliases: [Displacement DDI, Phenytoin valproate, Warfarin phenylbutazone, fu-CL coupling]
tags: [pharmacometrics/ddi, protein-binding, tozer, multifaceted-DDI]
up: "[[M5 Nonlinear binding]]"
related: ["[[M5-EXT]]", "[[T6 경쟁적 억제]]", "[[CP7 Displacement vs Inhibition]]"]
source: "Tozer 5e, Ch.17, pp.539–544, 562–564; Fig.17-2/17-3/17-4/17-18; Eq.17-1/17-2/17-3"
---

Displacement-only DDI: Stage 1 M5 open system 결론의 임상 검증. Phenytoin-valproate (Fig.17-3): total↓ unbound 일정 → dose 조정 불필요. Warfarin-phenylbutazone (Fig.17-18): unbound *sustained↑* → 추가 inhibition mechanism (S-warfarin CYP2C9). 진단: Cu transient = displacement only; Cu sustained = inhibition + displacement. 1967 historical 오해 = displacement만 강조 → 진정 mechanism missed. 임상: pure displacement 임상 의의 미미; 추가 mechanism 동반 시만 dose 조정.
```

---

### T6. 경쟁적 억제 정량 framework — Eq.17-9~17-12 (Stage 3 Apex)

<!-- ANCHOR -->
T5가 displacement의 *임상 의의 부재*를 확립했다면, T6는 *진정한 위험 mechanism*인 inhibition의 정량 framework. FDA DDI Guidance Eq.17-11 AUC ratio가 본 카드의 핵심.

<!-- MASTER LENS -->
> **[개념 Big Idea: 거장의 시각]**
>
> **왜 치명적**: 신약 후보 X는 fm=0.85 (CYP3A4 dominant). Phase 2에서 환자 일부가 ketoconazole (strong CYP3A4 inhibitor) 동반 복용 시 *예상 dose의 1.5배 toxicity*. NDA 제출 시 reviewer가 "AUC ratio prediction 누락"을 지적하면 *6–12개월 deficiency response* 지연. Eq.17-11 ($AUC_{inh}/AUC_{normal} = 1/[fm/(1+Cu_I/K_I) + (1-fm)]$)에 fm=0.85, Cu_I/K_I=4 (ketoconazole strong) 대입 시 AUC ratio = 4.4 — *Table 17-6의 ≥4× substrate 분류*에 해당. 본 prediction을 Phase 1 시점에 안 했다면 이미 too late.
>
> **체화해야 할 단 하나의 직관**: Eq.17-11의 분모는 *두 항*: $fm/(1+Cu_I/K_I)$ (inhibited pathway, 줄어듦) + $(1-fm)$ (unaffected pathways, 보존). $fm \to 1$일 때만 inhibition이 dramatic 증폭; $fm < 0.5$이면 영향 marginal. 즉 *DDI 위험 = fm × inhibitor 강도*의 곱.
>
> **이 직관을 머릿속에 박고 아래를 읽어라**: 본 카드는 Stage 1 M2 (capacity-limited MM)의 enzyme kinetics + Stage 1 M8 (PD competitive antagonism Eq 3:49)의 mathematical structure 두 가지가 *동일한 공식* (Cu_I/K_I 추가)으로 표면화한 것. PK·PD를 분리해서 배운 학습자가 본 카드에서 *합쳐지는* 순간이 mastery 진입.

#### A. Formal Definition (Eq.17-9~17-12)

**Eq.17-9** (rate of metabolism with inhibitor):
$$Rate = \frac{CL_{int,f} \cdot Cu_{cell}}{1 + Cu_I/K_I} = \frac{f_m \cdot CL_{int} \cdot Cu_{cell}}{1 + Cu_I/K_I}$$

**Eq.17-10** (clearance):
$$CL_{\text{inhibited}} = CL_{\text{normal}} \left[\frac{f_m}{1 + Cu_I/K_I} + (1 - f_m)\right]$$

**Eq.17-11** (AUC ratio — **FDA DDI Guidance 핵심식**):
$$\frac{AUC_{\text{inhibited}}}{AUC_{\text{normal}}} = \frac{F_{\text{inhibited}}}{F_{\text{normal}}} \left[\frac{1}{\dfrac{f_m}{1 + Cu_I/K_I} + (1 - f_m)}\right]$$

**Eq.17-12** (dose adjustment):
$$\frac{(\text{Dose}/\tau)_{\text{inhibited}}}{(\text{Dose}/\tau)_{\text{normal}}} = \frac{F_{\text{normal}}}{F_{\text{inhibited}}} \left[\frac{f_m}{1 + Cu_I/K_I} + (1 - f_m)\right]$$

**구조적 통찰**: Eq.17-9는 Stage 1 M8 PD Eq 3:49 ($EC_{50}^{app} = EC_{50}(1 + I/K_i)$)와 *동일 mathematical form*. PK 도메인의 enzyme 경쟁이 PD 도메인의 receptor 경쟁과 *같은 방정식*으로 기술된다. M2 (capacity-limited MM)의 $K_m$이 inhibitor에 의해 *apparent $K_m^{app} = K_m(1 + I/K_I)$*로 변하는 것이 본 카드 mechanism.

#### B. Theophylline–Enoxacin — primary case study (Fig.17-6, 17-7)

**Source**: Rogge et al. 1989 `[출처: Tozer 5e, Fig.17-6, pp.545–547]`

**임상 design**:
- Theophylline 150 mg controlled-release q12h × 12 days (288 hr)
- Enoxacin 400 mg q12h × 4 days (시작 96 hr 시점)

**관측**:
- Pre-enoxacin trough: ~4.8 mg/L (avg interdose 4 mg/L)
- + Enoxacin: trough rises to ~9 mg/L (avg interdose 9 mg/L)
- Post-enoxacin withdrawal: 점진 회복 (수일 소요)

**Eq.17-5** (half-life relation):
$$t_{1/2,\text{inh}} = t_{1/2,\text{normal}} \cdot \frac{CL_{\text{normal}}}{CL_{\text{inh}}}$$

**Eq.17-6** (clearance ratio):
$$\frac{CL_{\text{inh}}}{CL_{\text{normal}}} = \frac{C_{ss,av,\text{normal}}}{C_{ss,av,\text{inh}}} = \frac{4}{9} = 0.44$$

→ Enoxacin이 theophylline CL을 **56% 감소** (CL_inh = 0.44 × CL_normal).

**t½ 계산**:
- Normal t½ = 8.8 hr (alone)
- Inhibited t½ = 8.8 × (1/0.44) = **22 hr**
- 4 day plateau 도달 (inhibited t½ × 5)과 일치

**Withdrawal slow recovery 설명** (p.547):
- Enoxacin 본인 t½ = 4–5 hr — 그러나 plasma C가 *충분히 오래 inhibition 유지*
- Theophylline t½는 enoxacin C 감소에 따라 *연속적으로 감소* → 회복 완만

**fm 추정 (Eq.17-10에서)**:
- Theophylline은 demethylation + ring oxidation + renal — 복수 경로
- 최대 enoxacin (400 mg) 영향: CL ratio = 0.44
- Eq.17-10: $0.44 = fm/(1 + Cu_I/K_I) + (1-fm)$
- 가정 ($Cu_I/K_I \to \infty$, full inhibition): $0.44 = (1-fm)$ → **fm ≈ 0.56–0.67** (Tozer p.549 명시: ~67%)

**Fig.17-7 graded effect**:
- 25 mg, 100 mg, 400 mg enoxacin → 각각 다른 inhibition 정도
- 400 mg 최대 효과 → fm 한계 도달

#### C. Desipramine–Quinidine — CYP2D6 prototype (p.549)

- Desipramine fm(CYP2D6) ≈ 0.75 (extensive metabolizer)
- Quinidine: strong CYP2D6 inhibitor ($Cu_I/K_I \gg 1$)
- Predicted CL_inh = $(1-0.75) \cdot CL_{normal}$ = **0.25 × CL** (4배 감소)
- Predicted t½ = **4× 정상**

**임상 함의**: Extensive metabolizer가 quinidine 동반 시 *poor metabolizer phenotype으로 전환*. Desipramine dose 25%로 감량 권고.

**Stage 3 T7 forward**: PM 환자에서 같은 quinidine inhibition은 *fm 거의 0* → 영향 미미.

#### D. Desipramine–Fluoxetine (Table 17-11) — 정량 anchor

**Bergstrom 1992** (study problem 5):
- Desipramine 50 mg PO single dose 단독 vs 8일 fluoxetine (60 mg/day) 후
- AUC 단독: 284 ± 244 µg·hr/L
- AUC + fluoxetine: 2110 ± 900 µg·hr/L → **7.4× 증가**
- t½: 16.1 → 63.8 hr (4× 증가)
- CL/F: 289 → 27.1 L/hr (10.6× 감소)

**Eq.17-11 검증**:
- Fluoxetine: strong CYP2D6 inhibitor ($Cu_I/K_I$ 추정 큰 값)
- AUC ratio observed = 7.4
- Eq.17-11 예측: $1 / (fm/X + (1-fm))$. Desipramine fm(CYP2D6) ~ 0.75
- 만약 $Cu_I/K_I \to \infty$: $1/(1-0.75) = 4$ — 관측 7.4 다소 초과
- 추가 fm 또는 multiple pathways inhibition 가능 (CYP3A4 minor도 fluoxetine 영향)

#### E. Strong/Moderate/Weak inhibitor classification (Table 17-5)

| Strength | AUC fold-increase | CYP3A 예시 | CYP2D6 예시 |
|---|---|---|---|
| **Strong** | ≥ 5× | Clarithromycin (b)*, Itraconazole, Ketoconazole, Ritonavir (b), Telithromycin (b) | Fluoxetine, Paroxetine, Quinidine |
| **Moderate** | 2–5× | Diltiazem (b), Erythromycin (b), Fluconazole, Grapefruit juice (b), Verapamil | Terbinafine |
| **Weak** | 1.25–2× | Cimetidine | Amiodarone, Sertraline |

(b) = mechanism-based (T4-EXT 적용)

**Substrate 측 (Table 17-6)** — strong inhibitor 동반 시 ≥ 4× AUC↑:
- **CYP3A**: Brecanavir, Buspirone, Felodipine, Lovastatin, Midazolam, Nelfinavir, Saquinavir, Sildenafil, Simvastatin, Triazolam, Voriconazole
- **CYP2D6**: Atomoxetine, Desipramine, Dextromethorphan, Metoprolol, Nortriptyline, Tolterodine

**임상 함의**: Table 17-6 substrate를 처방받는 환자가 strong inhibitor (Table 17-5) 시작 시 *dose 25% 감량 또는 alternative*.

#### F. Time course of inhibition (Fig.17-9 — insidious progression)

**Tozer p.551 핵심**: $fm \to 1$ + 10× CL 감소 시 t½도 10× 증가. → *plateau 도달 시간 자체가 길어짐*.
- Normal t½ = 0.5 day → inhibited t½ = 5 days
- 새 plateau 도달 = 5 × 5 days = 25 days (1개월 가까이)
- 추가로 inhibitor 자체 plateau 도달 시간 (multiple-dose) → 합쳐서 *수개월*

**임상 위험**: 환자가 inhibitor 추가 후 *수주~수개월 후* 갑자기 toxicity 발현 → 임상의가 mechanism 인지 실패.

#### G. Multiple weak inhibitors의 합산 효과 (p.551)

- 환자가 moderate/weak inhibitor 여러 개 동시 복용
- 각각 단독으로는 dose 조정 불필요
- 합산 효과 → 효과적으로 *strong inhibitor* 분류
- 임상 함의: polypharmacy 환자에서 *cumulative inhibition effect* 확인 필요

#### H. Route of administration 효과 (Table 17-7) — 본 카드의 임상 엣지

**Diltiazem–Lovastatin (T9 forward로 연결)**:
- Diltiazem oral (130 µg/L Css) vs IV (73–140 µg/L) — 유사 systemic
- Lovastatin AUC ratio: **1.27 IV vs 3.57 oral**
- Mechanism: lovastatin = high-E + first-pass metabolized
- Oral lovastatin → first-pass에서 diltiazem이 hepatic + gut wall CYP3A inhibit → dramatic
- IV → first-pass 우회 → 작은 효과

**Eq.17-11의 $F_{inh}/F_{normal}$ 항이 본 효과**: oral inhibition은 *F 변화*도 반영하므로 IV보다 큰 AUC ratio.

**Fluconazole–Midazolam (Fig.17-10)** (T9에서 자세히):
- 400 mg fluconazole + midazolam
- IV: 2× AUC↑
- Oral: 5.6× AUC↑
- F: 24% → 63% (oral)
- F_H = 0.42 → 0.72; F_G = 0.57 → 0.88 (gut wall + hepatic 분리 분석)

#### I. Beneficial competitive inhibition (CONTEXT, p.555)

Intentional combinations (Table 17-2):
- **Penicillin–Probenecid**: probenecid가 anionic transport (renal secretion) inhibit → 더 높고 prolonged penicillin C
- **Imipenem–Cilastatin (Fig.17-12)**: cilastatin이 renal dehydropeptidase inhibit → 24% 회수 → 80% 회수
- **L-Dopa–Carbidopa**: peripheral decarboxylase inhibit → CNS L-dopa 증가
- **Lopinavir–Ritonavir**: ritonavir가 CYP3A4 inhibit → lopinavir oral F·CL 개선

#### J. NONMEM (T6 정량 framework 적용)

```
$PK
; --- victim drug ---
CL_BASE  = 30           ; L/hr
FM       = 0.75         ; CYP2D6 fraction
CU_I_KI  = COV_KI_RATIO ; covariate (개별 환자 inhibitor 노출)

; --- inhibition factor (Eq.17-10) ---
INHIB_FACTOR = FM / (1 + CU_I_KI) + (1 - FM)
CL_INH = CL_BASE * INHIB_FACTOR

; --- AUC ratio prediction (Eq.17-11) ---
AUC_RATIO = 1 / INHIB_FACTOR  ; F unchanged 가정
```

**FDA DDI Guidance 적용**: NDA submission 시 본 framework로 "expected AUC ratio" prediction 표 제공. Sensitivity analysis: fm uncertainty band, Cu_I/K_I 범위에서 worst-case AUC ratio.

#### K. Stage 1 M2 + M8 통합 — Stage 3 Apex Concept

**핵심 통찰**: Eq.17-9의 분모 $(1 + Cu_I/K_I)$가:
- Stage 1 M2 enzyme kinetics에서 $K_m^{app} = K_m(1 + I/K_I)$ 형태로 나타남
- Stage 1 M8 receptor kinetics에서 $EC_{50}^{app} = EC_{50}(1 + I/K_I)$ 형태로 나타남
- 동일 mathematical structure → PK·PD가 *receptor·enzyme 경쟁*이라는 단일 mechanism의 두 표현

본 통합이 Stage 3 Apex Concept인 이유.

#### L. Zettelkasten Atom

```yaml
---
aliases: [Eq.17-9, Eq.17-10, Eq.17-11, Competitive inhibition quantitative, FDA DDI Guidance, Theophylline enoxacin, Desipramine quinidine]
tags: [pharmacometrics/ddi, kinetics/inhibition, fda-guidance, regulatory, tozer]
up: "[[T4 MBI mechanism]]"
related: ["[[T4-EXT MBI 정량]]", "[[T7 PM × Inhibition]]", "[[T9 Multifaceted DDI]]", "[[Stage 1 M2 capacity-limited]]", "[[Stage 1 M8 PD competitive]]"]
source: "Tozer 5e, Ch.17, pp.544–555; Eq.17-9, 17-10, 17-11, 17-12; Fig.17-6/7/8/9; Table 17-5/17-6/17-7"
---

경쟁적 억제 정량 framework: Eq.17-11 AUC ratio = 1/[fm/(1+Cu_I/K_I) + (1-fm)] = FDA DDI Guidance 핵심식. Stage 1 M2 enzyme + M8 PD receptor 경쟁의 *동일 mathematical form*. Theophylline-Enoxacin (Fig.17-6): 4 day enoxacin → t½ 8.8→22h, CL ratio 0.44, fm≈0.67. Desipramine-Quinidine: fm(CYP2D6)=0.75 → 4× CL감소. Strong/Moderate/Weak (Table 17-5) + ≥4× substrates (Table 17-6). Time course (Fig.17-9): t½ × 10 → plateau 1개월 — insidious progression. Multiple weak inhibitors 합산 → strong. Route effect (Table 17-7 Diltiazem-Lovastatin): oral 3.57× vs IV 1.27× (first-pass). NONMEM: INHIB_FACTOR = FM/(1+Cu_I_KI) + (1-FM).
```


---

### T7. PM × Inhibition Risk Amplification — Eq.17-18

<!-- ANCHOR -->
T6가 *extensive metabolizer*에서의 inhibition 정량이라면, T7은 *poor metabolizer*에서 같은 inhibition이 만드는 *증폭된 위험*. 같은 약물·같은 inhibitor라도 환자의 CYP2D6/2C9/2C19 phenotype에 따라 노출 차이가 *order of magnitude* 수준으로 커진다.

<!-- MASTER LENS -->
> **[개념 Big Idea]**
>
> **왜 치명적**: Omeprazole CYP2C19 PM 환자가 clarithromycin (CYP3A4 strong MBI) 동반 시 EM + clarithromycin 대비 *33배 exposure ratio* (Fig.17-15). 이 33배는 단순 가산이 아니라 *Eq.17-18 분모의 잔여 경로 잠식*에서 발산. PM 환자에서 nonpolymorphic 경로마저 inhibit되면 *제거할 길이 거의 없어진다*. 임상의가 phenotype 무시하고 "표준 dose + 표준 inhibitor 주의" 수준으로만 처방하면 PM 5–10%의 환자가 toxicity.
>
> **체화 직관**: PM에서 inhibition은 *분모 (1 - fm_POLY - fm_NP)*를 0에 접근시킨다. 즉 EM에서는 polymorphic + nonpolymorphic 두 경로가 모두 살아있어 inhibition 영향이 dilute되지만, PM에서는 polymorphic 경로가 이미 없는데 nonpolymorphic 경로마저 차단되면 *남는 경로 (CL_O)만으로 약물 제거*. fm_POLY가 클수록 (e.g., 0.75 이상) PM × inhibition은 *dramatic 위험 영역*.

#### A. Formal Definition (Eq.17-15~17-18)

**전제**:
- $CL_{EM}$ = extensive metabolizer 정상 clearance
- $CL_{PM}$ = poor metabolizer 정상 clearance (polymorphic pathway 결손)
- $CL_{NP}$ = nonpolymorphic pathway clearance (양 표현형 동일 가정)
- $CL_O$ = 다른 unaffected pathways
- $fm_{POLY}$ = polymorphic 경로 비율 (EM 기준)
- $fm_{NP}$ = nonpolymorphic 경로 비율 (EM 기준)

**Eq.17-15**: $CL_{EM} = CL_{POLY} + CL_{NP} + CL_O$

**Eq.17-16**: $CL_{PM} = CL_{NP} + CL_O$ (polymorphic pathway 결손)

**Eq.17-17**: $CL_{PM,\text{inhibited}} = CL_O = (1 - fm_{POLY} - fm_{NP}) \cdot CL_{EM}$
(nonpolymorphic도 inhibit → 잔여는 다른 경로만)

**Eq.17-18 — Maximum Exposure Ratio**:
$$\text{Maximum Exposure Ratio} = \frac{AUC_{PM,\text{inhibited}}}{AUC_{EM}} = \frac{1}{1 - fm_{POLY} - fm_{NP}}$$

#### B. Fig.17-15 임상 검증 — substrate-inhibitor pair 데이터

`[출처: Tozer 5e, Fig.17-15, p.559; Collins et al. 2006]`

| Pair (substrate – inhibitor of NP pathway) | $fm_{POLY}$ 추정 | Observed Max Ratio |
|---|---|---|
| Citalopram – Troleandomycin | ~0.20 | ~1.5 |
| Diazepam – Diltiazem | ~0.30 | ~1.5 |
| Dolasetron – Aprepitant | ~0.55 | ~3.0 |
| Venlafaxine – Ketoconazole | ~0.60 | ~3.5 |
| Pimozide – Clarithromycin | ~0.65 | ~10 |
| R-Lansoprazole – Clarithromycin | ~0.75 | ~10 |
| Omeprazole – Ketoconazole | ~0.80 | ~10 |
| S-Lansoprazole – Clarithromycin | ~0.80 | ~13 |
| Omeprazole – Troleandomycin | ~0.85 | ~10 |
| Omeprazole – Clarithromycin | ~0.92 | **~33** |

**핵심 패턴**: $fm_{POLY}$이 0.75를 넘으면 exposure ratio가 *order 10*로 치솟음. Eq.17-18에서 $1/(1-0.75-0.20) = 1/0.05 = 20$ 수준의 발산.

**Tozer p.559 명시**:
> "When fm_POLY reaches 0.75, exposure ratios in the order of 10 or more occur when one of the other pathway is strongly inhibited, often reason indeed to reduce the dose in poor metabolizers."

#### C. Stage 3 forward — NDA labeling 함의

본 카드는 NDA Section 12.3 Pharmacokinetics 및 Section 17 Patient Counseling Information의 mechanism 기반:
- "Poor metabolizers of CYP2C19 should not co-administer with strong CYP3A4 inhibitors"
- 또는 "Reduce dose by 75% in PM phenotype when co-prescribing [inhibitor]"
- *fm_POLY × inhibitor 강도*가 dose 권고의 정량 framework

#### D. Stage 1 M2 + Stage 3 T6와의 통합

T7은 T6의 *phenotype-specific 적용*. EM에서 Eq.17-11 AUC ratio prediction이 PM에서는 Eq.17-18로 *upper bound* 변환. 이는 Stage 1 M2 mechanism (단일 효소 capacity-limited)이 *효소 phenotype distribution*과 결합할 때 임상에서 *bimodal 위험 분포*를 생성하는 것의 정량 외화.

#### E. NONMEM (PopPK + 약물유전체)

```
$PK
; --- phenotype covariate ---
CYP2D6_PHENO = COV_PHENO   ; 0=PM, 1=IM, 2=EM, 3=UM
FM_POLY = THETA(1) * (CYP2D6_PHENO/2)  ; PM: 0, EM: full

; --- inhibition + phenotype interaction ---
INHIB_NP = FM_NP / (1 + CU_I_KI) + (1 - FM_NP)  ; nonpolymorphic만 inhibit
CL = CL_O + (FM_POLY * CL_EM_FULL) + (FM_NP * CL_EM_FULL * (CL_NP_INH/CL_NP))

; --- Maximum exposure ratio (label용) ---
MAX_RATIO_PM = 1 / (1 - FM_POLY - FM_NP)
```

#### F. 임상 의사결정 sequence

1. 환자 phenotype 확인 (CYP2D6/2C9/2C19 genotyping if 가능)
2. EM: Eq.17-11 AUC ratio prediction → strong inhibitor 동반 시 dose 25–50% 감량
3. PM: Eq.17-18 maximum exposure ratio → strong inhibitor 동반 시 *해당 약물 contraindication*
4. fm_POLY > 0.75 + nonpolymorphic strong inhibitor = clinical use 재검토

#### G. Zettelkasten Atom

```yaml
---
aliases: [Eq.17-18, Maximum exposure ratio, PM inhibition, Polymorphic-nonpolymorphic interaction, Phenotype DDI]
tags: [pharmacometrics/ddi, pharmacogenomics, cyp2d6, cyp2c19, regulatory, tozer]
up: "[[T6 경쟁적 억제 정량]]"
related: ["[[T4-EXT MBI 정량]]", "[[T9 Multifaceted DDI]]", "[[FDA DDI Guidance]]", "[[CPIC guideline]]"]
source: "Tozer 5e, Ch.17, pp.558–559; Eq.17-15/16/17/18; Fig.17-15"
---

PM × Inhibition: Max Exposure Ratio = 1/(1 - fm_POLY - fm_NP). Polymorphic pathway 결손 PM에서 nonpolymorphic 경로마저 strong inhibitor로 차단 시 잔여 (CL_O)만 남아 발산. fm_POLY > 0.75일 때 ratio 10× 이상 dramatic. Omeprazole-clarithromycin: fm_POLY≈0.92 → 33× exposure (Fig.17-15). 임상: PM phenotype 환자에서 strong inhibitor 동반은 종종 contraindication 사유. NDA Section 12.3 mechanism 기반. Stage 1 M2 단일 효소 mechanism이 phenotype distribution과 결합 시 bimodal 위험 분포로 외화.
```

---

### T8. Induction PK Time Course — Eq.17-15 framework

<!-- ANCHOR -->
T6/T7이 inhibition (즉시 효과·즉시 회복 reversible / 시상수 enzyme t½ MBI)이라면, T8은 induction의 *역방향 turnover dynamics*. Stage 2 M3-EXT carbamazepine autoinduction의 hetero-induction 형태로 *DDI 시상수가 enzyme/inducer 중 느린 쪽*에 의해 결정된다.

<!-- MASTER LENS -->
> **[개념 Big Idea]**
>
> **왜 치명적**: 환자가 dicumarol (oral anticoagulant) 안정화 후 phenobarbital 60 mg/day 추가 → *3–4주 후* dicumarol Css 30 → 10 mg/L (Fig.17-17). 임상의가 즉시 효과 없다 판단하여 dicumarol dose *증가* → phenobarbital 철수 시 dicumarol Css가 같은 시상수로 *재상승* → hemorrhagic crisis. 본 trap의 mechanism = *phenobarbital 시상수 (t½ 4 days) ≫ dicumarol 시상수* → DDI dynamics가 phenobarbital kinetics에 종속.
>
> **체화 직관**: Induction time course = max(enzyme t½, inducer t½). Carbamazepine autoinduction (Stage 2 M3-EXT)에서는 enzyme t½ ≈ 5d가 dominant. Phenobarbital-dicumarol에서는 phenobarbital t½ ≈ 4d가 dominant. 두 mechanism 모두 *느린 쪽*의 시상수가 임상 monitoring 간격을 결정.
>
> **이 직관을 머릿속에 박고 아래를 읽어라**: 본 카드는 Stage 2 M3-EXT의 *self-induction*이 Stage 3에서 *cross-induction*으로 변형. 같은 turnover ODE, 같은 시상수, 다른 dose-response 패턴.

#### A. Mechanism (M3 → M3-EXT → T8)

Stage 1 M3: $dE/dt = R_{in} - k_{out} \cdot E$
Stage 2 M3-EXT (autoinduction): $R_{in}$이 약물 자체에 의해 stimulate → $R_{in}^{induced} = R_{in,0} \cdot (1 + \alpha \cdot C_{drug})$
Stage 3 T8 (heteroinduction): $R_{in}$이 *다른 약물* (inducer)에 의해 stimulate → $R_{in}^{induced} = R_{in,0} \cdot (1 + \beta \cdot C_{inducer})$

**정상상태**:
$$E^{ss}_{induced} = \frac{R_{in,0} \cdot (1 + \beta \cdot C_{inducer})}{k_{out}}$$

→ **CL ∝ E이므로 inducer C에 비례하여 victim drug CL 증가**.

#### B. Phenobarbital–Dicumarol — prototype (Fig.17-17, p.561)

`[출처: Tozer 5e, Cucinell et al. 1965]`

**임상 design**:
- Patient stabilized on dicumarol 75 mg/day (oral anticoagulant)
- Phenobarbital 60 mg/day 추가 (days 30–80)

**관측**:
- Plasma dicumarol C: 30 mg/L → 약 12 mg/L 도달 (60% 감소)
- Prothrombin time도 동시 감소
- 도달 시상수: **3–4 weeks** (phenobarbital plateau 도달과 일치)
- Phenobarbital 철수 후 회복 시상수: 동일 3–4 weeks

**Mechanism 분석**:
- Dicumarol t½ (단독) ≈ 1–2 days (relatively fast)
- Phenobarbital t½ ≈ **4 days** — *느린 쪽*
- 따라서 DDI dynamics가 phenobarbital kinetics에 종속
- Enzyme synthesis (induced) 가속이 즉시 발생하지만 *enzyme level은 phenobarbital plateau에 따라 점진 상승*

**핵심 통찰** (Tozer p.561):
> "When elimination of the inducer is the rate-limiting step, changes in the concentration of inducer are then reflected almost instantaneously by changes in the amount of enzyme and hence clearance of the affected drug."

#### C. Stage 2 M3-EXT carbamazepine과 비교 — 두 induction prototype

| 측면 | M3-EXT Autoinduction | T8 Heteroinduction |
|---|---|---|
| Inducer | Drug itself (carbamazepine) | Other drug (phenobarbital) |
| 시상수 dominant | Enzyme t½ (~5d, faster than drug t½) | Inducer t½ (4d, slower than victim t½) |
| 시간 | 20–25 days plateau | 3–4 weeks plateau |
| Withdrawal | 자체 t½로 회복 | Inducer t½로 회복 |
| 진단 어려움 | Single-dose t½로 multiple-dose 예측 불가 | 임상의가 시간 인과 관계 못 잡음 |

#### D. Inducer 분류 (Fig.17-5에서 추출)

**CYP3A**: Rifampin (강력), Carbamazepine (M3-EXT), Phenobarbital
**CYP2C9/19**: Rifampin
**CYP2B6**: Rifampin (다중 표적 inducer)
**CYP2E1**: Ethanol (M7 통합 사례에서 자기 induction)

**핵심 inducer**: Rifampin은 CYP3A/2B6/2C 모두에 대해 *strong inducer*. T9 atorvastatin–rifampin 사례에서 multi-faceted 효과.

#### E. 시간 차원의 임상 trap (Fig.17-16 vs 17-17)

**Fig.17-16 모식적 (즉시 효과 가정)**: Drug A C가 즉시 50% 감소 (idealized).
**Fig.17-17 실제 (느린 dynamics)**: 3–4 weeks 점진 감소.

**임상 의사결정 trap**:
1. Inducer 시작 후 1–2주 평가 → 효과 미미 → *dose 증량 시도*
2. 3–4주 후 plateau 도달 → 환자 *toxicity (높은 dose × induction → withdrawal 시 trap 활성)*
3. Inducer 철수 후 *enzyme level 회복 동안 victim drug C 점진 상승* → 임상 hemorrhagic event

#### F. Graded induction (CONTEXT)

Inducer dose ↑ → induction 강도 ↑. Strong inducer (rifampin 600 mg/day)와 weak inducer (cimetidine moderate) 차이. Multiple induction 합산 효과는 inhibition만큼 systematic 연구 안 됨.

#### G. NONMEM (induction with enzyme compartment)

```
$PK
; --- enzyme compartment (M3 turnover) ---
KOUT_ENZ  = 0.173        ; day⁻¹ (CYP3A4, t½=4d)
RIN_BASE  = KOUT_ENZ * 1 ; relative E^ss = 1
ALPHA_IND = THETA(1)     ; induction strength

; --- victim drug ---
CL_BASE   = 30           ; L/hr
FM_INDUCED = 0.85        ; affected pathway

$DES
DADT(1) = -CL_VICTIM * A(1) / V                              ; victim
DADT(2) = -CL_INDUCER * A(2) / V_IND                         ; inducer
DADT(3) = RIN_BASE * (1 + ALPHA_IND * A(2)/V_IND) - KOUT_ENZ * A(3)
                                                              ; enzyme

$PK
CL_VICTIM = CL_BASE * (FM_INDUCED * A(3) + (1 - FM_INDUCED))
```

#### H. Stage 1 M3 + Stage 2 M3-EXT 통합 — Stage 3 시상수 framework

**핵심 통찰**: Stage 1 M3 ODE의 *시상수* $1/k_{out}$는:
- Stage 1 mechanism: enzyme turnover의 abstract 시간상수
- Stage 2 M3-EXT: carbamazepine 5d (자기 induction)
- Stage 2 T4: clarithromycin 3d (MBI, 같은 enzyme이 inactivation으로 변형)
- Stage 3 T8: phenobarbital 4d (cross-induction, *inducer t½*에 종속)

같은 ODE에서 *어느 시상수가 dominant*인지가 임상 시간 차원을 결정.

#### I. Zettelkasten Atom

```yaml
---
aliases: [Eq.17-15 framework, Induction time course, Phenobarbital dicumarol, Heteroinduction, Enzyme turnover DDI]
tags: [pharmacometrics/ddi, kinetics/induction, time-dependent, tozer]
up: "[[M3 Enzyme turnover]]"
related: ["[[M3-EXT Carbamazepine autoinduction]]", "[[T4 MBI mechanism]]", "[[T9 Atorvastatin Rifampin]]"]
source: "Tozer 5e, Ch.17, pp.560–562; Fig.17-16/17-17; Fig.17-5 inducer list"
---

Induction time course: dominant 시상수 = max(enzyme t½, inducer t½). Phenobarbital-Dicumarol (Fig.17-17): 3–4 weeks plateau, 시상수 = phenobarbital t½ (4d). Carbamazepine autoinduction (Stage 2 M3-EXT, ~5d enzyme dominant)와 mechanism 동일, dominant 시상수만 다름. 임상 trap: 1–2주 평가 시 효과 미미 → dose 증량 → 4주 후 toxicity. 주요 inducer: Rifampin (CYP3A/2B6/2C strong), Carbamazepine, Phenobarbital. Withdrawal recovery 동일 시상수. NONMEM: enzyme compartment ODE에 inducer C 비례 R_in 증가.
```

---

### T9. Multifaceted/Transporter-Mediated DDI — 통합 Master Card

<!-- ANCHOR -->
T5–T8이 *단일 mechanism* 정량 framework이라면, T9는 *복수 mechanism 동시 작동*의 임상 사례. 같은 약물 조합에서 displacement + inhibition (warfarin–phenylbutazone), CYP + transporter (atorvastatin–rifampin), gut + hepatic (fluconazole–midazolam)이 결합되어 simple framework로 예측 불가능한 DDI 발생.

<!-- MASTER LENS -->
> **[개념 Big Idea]**
>
> **왜 치명적**: Atorvastatin–Rifampin IV acute (Fig.17-19): Cmax 10×↑, AUC 7×↑, t½ 8h → 3h. *Rifampin은 inducer*인데 IV acute 단일 dose에서 *AUC 증가* — 임상의가 mechanism 모순으로 혼란. 진실: rifampin이 CYP3A4 inhibitor/inducer *동시*이지만 IV acute는 OATP1B1 (hepatic uptake transporter) 차단이 dominant → hepatic 진입 차단 → systemic AUC 증가. Multiple-dose 만성 rifampin은 induction 효과 (CYP3A4) dominant → AUC 감소. 단일 mechanism framework로는 예측 불가. NDA submission 시 본 mechanism 누락 → reviewer "transporter pathway not addressed" deficiency.
>
> **체화 직관**: 임상 DDI 60% 이상이 multifaceted. 진단 sequence: (1) Total CL 변화, (2) F 변화 (oral vs IV 비교), (3) Vd 변화, (4) renal CL 변화, (5) plasma binding 변화 — 각 변화를 *분리해서* 측정 후 mechanism 합산. Single-mechanism framework (T6 Eq.17-11)은 *단순 사례*에만 적용; multifaceted 경우 각 mechanism의 partial contribution을 분리해 합산해야.
>
> **이 직관을 머릿속에 박고 아래를 읽어라**: 본 카드는 Stage 1 M5 + M6 + Stage 2 T1 + T2 + T3 + Stage 3 T6 + T8까지 모든 mechanism이 *임상 사례 단일 약물 쌍*에 동시 표면화하는 케이스 모음. 각 사례의 진단 sequence가 본 통합 capability의 외화.

#### A. Digoxin–Quinidine (Table 17-8, p.564) — Transporter + 분포 변화

**파라미터 변화**:
| 측면 | Alone | + Quinidine | 변화 |
|---|---|---|---|
| Oral F | 0.75 | 0.85 | +13% |
| Total CL | 140 mL/min | 72 mL/min | −49% |
| Renal CL (CL_R) | 101 mL/min | 51 mL/min | −50% |
| Volume Vd | 500 L | 240 L | −52% |
| $f_u$ | 0.79 | 0.79 | 무변화 |

**Mechanism 분리**:
1. **Renal CL 감소**: $CL_R = 101$ mL/min vs $f_u \cdot GFR = 0.79 \times 120 = 95$ mL/min — *기존엔 거의 GFR + 미세 secretion*. Quinidine이 PgP (renal tubule) inhibit → secretion blocked → CL_R 감소. *그러나* CL_R < $f_u \cdot GFR$이 되어 *reabsorption도 작동*함을 시사 → secretion + reabsorption 균형 변화 (Stage 2 T1 mechanism의 *임상 발현*).

2. **Nonrenal CL 감소**: $CL_{nonrenal} = 140 - 101 = 39$ → $72 - 51 = 21$ mL/min. Hepatic biliary PgP secretion inhibit → biliary CL 감소.

3. **Vd 감소 (500 → 240 L)**: $f_u$ 무변화 → tissue uptake 감소가 mechanism. Stage 2 T3 TMDD 카드의 *uptake transporter inhibition* mechanism (OATP1B3가 digoxin tissue uptake mediate; quinidine이 inhibit). $V = V_p + V_{TW} \cdot (P_{uptake}/P_{efflux}) \cdot (f_u/f_{u,T})$ (Eq.4-29) — uptake 감소 → Kp 감소 → V 감소.

4. **Oral F 미세 증가**: gut PgP inhibit → 소량 absorption 증가.

**임상 함의**:
- Digoxin maintenance dose **50% 감량**
- Loading dose **50% 감량** (Vd 감소 때문)
- 이는 단일 mechanism (단순 inhibition) 가정에서는 예측 불가능

**Stage 2 T1·T3 통합**: 본 사례는 T1 (renal saturable transport), T3 (TMDD-like tissue uptake)의 *임상 발현*. 두 mechanism 모두 같은 inhibitor (quinidine, PgP/OATP)에 의해 동시 차단.

#### B. Atorvastatin–Rifampin IV Acute (Fig.17-19, p.565) — OATP1B1 inhibition

**파라미터 변화** (single oral atorvastatin 40 mg + IV rifampin 600 mg):
- Cmax: ~10 → ~140 µg/L (**10×↑**)
- AUC: ~30 → ~210 µg·hr/L (**7×↑**)
- t½: 8h → 3h (**3.7× 감소**)
- Atorvastatin CL/F: 6.8 → 0.88 mL/hr/kg (**9× 감소**)
- Vss/F: 66 → 3.8 L/kg (**17× 감소**)

**Mechanism 분리** (Tozer p.566):

1. **CYP3A inhibition? — 부정**. Rifampin이 CYP3A 강력한 *inducer*임은 잘 알려짐. *In vitro* CYP3A inhibition은 임상 농도보다 훨씬 높은 농도에서만 발생. → CYP3A inhibition mechanism 기각.

2. **OATP1B1 inhibition — confirmed**. Atorvastatin은 OATP1B1로 hepatic uptake. Rifampin이 OATP1B1 inhibit → atorvastatin이 *hepatic 진입 못 함* → systemic 노출 증가. 이는 **rate-limiting step이 metabolism에서 uptake로 이동**.

3. **t½ 단축의 paradox**: AUC 증가 + t½ 감소 동시? → 이는 Vd 감소가 dominant. Hepatic uptake 차단 시 atorvastatin이 *liver 안으로 안 들어감* → tissue distribution 줄어듦 → Vd 감소. CL/V = ke 비율에서 V 감소가 CL 감소보다 더 크면 t½ 감소.

4. **Multiple-dose rifampin과의 paradox**: 만성 rifampin은 CYP3A induction dominant → atorvastatin AUC *감소*. Single-dose IV vs multiple-dose oral rifampin이 *질적으로 다른 DDI 결과*.

**임상 함의**:
- 단일 dose / multiple dose / IV / oral rifampin 각각 다른 DDI mechanism dominant
- Mechanism without route distinction 처방 가이드는 *임상에서 무너짐*
- NDA section 12.3에서 *각 시나리오별 mechanism* 설명 필수

**Stage 2 T2 + Stage 3 T6/T8 통합**: T2 first-pass (oral 효과), T6 inhibition (uptake transporter), T8 induction (만성 다른 효과). 세 framework가 같은 약물 쌍에서 시간/route에 따라 dominant switch.

#### C. Rosuvastatin–Cyclosporine (Fig.17-11, p.555)

**임상 시나리오** (heart transplant recipients):
- Rosuvastatin 10 mg/day × multiple
- + Cyclosporine (anti-rejection)
- Cmax: ~5 → ~55 µg/L (**11×↑**)
- AUC: **7×↑**

**Mechanism**: Cyclosporine이 OATP1B1 (hepatic uptake) inhibit. Rosuvastatin은 hepatic uptake로 작용 + biliary secretion으로 제거 — metabolism 거의 없음. Uptake 차단 → systemic 노출 증가.

**Atorvastatin과 비교**:
- Atorvastatin: CYP3A로 metabolize + OATP1B1 uptake
- Rosuvastatin: 거의 metabolize 안 됨 + OATP1B1 uptake + biliary secretion
- 둘 다 OATP1B1 inhibition 영향 받지만 *다운스트림 mechanism*은 다름

**임상 함의**: Statin class 내에서도 *transporter-DDI 위험 차별화*. Pravastatin (가장 hydrophilic, transporter-only)과 비교 시 다른 DDI profile.

#### D. Diltiazem–Lovastatin Route Effect (Table 17-7) — T6 forward에서 자세히

**Table 17-7**:
- IV diltiazem (mean 73–140 µg/L) + oral lovastatin: AUC ratio **1.27**
- Oral diltiazem (mean 130 µg/L) + oral lovastatin: AUC ratio **3.57**

**Mechanism 분리**:
- Oral diltiazem → *gut wall + hepatic CYP3A 동시 inhibit* → first-pass loss 강력 차단 → oral lovastatin AUC 3.57×
- IV diltiazem → systemic CYP3A inhibit (거의 hepatic만) → 1.27×

**Stage 2 T2 + Stage 3 T6 통합**: T2 first-pass mechanism + T6 inhibition framework. Oral inhibitor의 *gut wall 효과*가 IV 대비 *2.8×의 추가 inhibition*.

#### E. Fluconazole–Midazolam (Fig.17-10, p.554) — Gut + Hepatic 분리

**임상 시나리오**:
- 400 mg fluconazole oral + midazolam (IV 1 mg / oral 3 mg)

**관측**:
- Midazolam IV AUC: **2× ↑**
- Midazolam oral AUC: **5.6× ↑**

**Mechanism 분리** (p.553):
- Midazolam F (control): 24%
- Midazolam F (+ fluconazole): 63%
- F = $F_G \cdot F_H$
- $F_H = 1 - E_H$ — IV 데이터로부터: $E_H$ control = 0.58 → $E_H$ inhibited = 0.28 → $F_H = 0.42 \to 0.72$
- $F_G$: control 0.57 → inhibited 0.88 (gut wall 거의 완전 inhibit)

**핵심 통찰**:
- Fluconazole이 oral administration → gut wall에 *고농도 직접 노출* → gut CYP3A 거의 완전 차단
- Hepatic은 systemic 농도에 비례 → moderate 차단

**Stage 1 M2 + Stage 3 T6 통합**: Eq.17-11의 $F_{inhibited}/F_{normal}$ 항이 *gut + hepatic 분리*되면 더 정확한 prediction.

#### F. Lopinavir/Ritonavir Combination Product (Table 17-2, p.534)

**Beneficial DDI 사례**:
- Lopinavir alone: F 낮고 CL 빠름 → 8h 간격 dosing 필요
- + Ritonavir (CYP3A4 strong MBI): lopinavir CL ↓, F ↑
- 결과: lopinavir 12h 간격 dosing + lower daily dose
- *낮은 daily dose · 적은 frequency · 낮은 IIV*

**Stage 3 T4-EXT mechanism**: ritonavir = CYP3A4 mechanism-based inhibitor (Table 17-5 strong). 본 카드 mechanism으로 lopinavir AUC ratio 정량 prediction 가능.

#### G. Penicillin–Probenecid (CONTEXT, p.555)

**Mechanism**: Probenecid가 anionic transport (renal secretion) competitive inhibit → penicillin CL_R 감소. Probenecid 본인은 lipophilic + reabsorbed → 낮은 CL → 안정 농도.

**임상 적용**: Penicillin + probenecid 조합으로 *낮은 dose · 더 긴 효과* 달성. 1950s 이후 standard.

#### H. 다른 Multifaceted 사례 (CONTEXT, 1줄씩)

- **Imipenem–Cilastatin (Fig.17-12)**: cilastatin이 renal dehydropeptidase inhibit → imipenem urinary recovery 24% → 80%
- **Lidocaine–Propranolol**: propranolol이 cardiac output 감소 → hepatic blood flow 감소 → lidocaine (high extraction) hepatic CL 감소 (hemodynamic mechanism)
- **Salicylic acid renal CL**: urine pH 변화 (acetazolamide, NH4Cl)에 sensitive — pH 의존 reabsorption
- **Loperamide–Quinidine** / **Ketoconazole–Ritonavir**: CNS PgP inhibition → CSF/brain 노출 증가 (희귀하지만 documented)
- **Glucagon–lidocaine**: glucagon이 hepatic blood flow 증가 → lidocaine CL 증가

#### I. Stage 3 통합 — 임상 진단 sequence

다중 mechanism 의심 시:
1. Total CL 측정 (alone vs DDI)
2. Renal CL (CL_R) 분리 측정
3. F 측정 — IV vs oral 비교 시 mechanism 분리
4. Vd 측정 — tissue uptake transporter 영향 평가
5. Plasma binding 직접 측정 — displacement 분리
6. Active metabolite 측정 — drug-metabolite mechanism 평가
7. Time course — single-dose vs steady-state 비교

각 변화를 *분리해서 측정* 후 mechanism 합산 → Eq.17-11 / Eq.17-13 / Eq.17-15 framework 각각 적용.

#### J. NONMEM (multifaceted DDI integrative model)

```
$PK
; --- victim drug pharmacokinetics ---
F_GUT  = THETA(1) * (1 - INH_GUT)        ; gut bioavailability
F_HEP  = THETA(2) * (1 - INH_HEP)        ; hepatic bioavailability
F      = F_GUT * F_HEP                    ; total F

; --- mechanisms separated ---
INH_GUT  = (CU_INHIBITOR_GUT/KI_GUT) / (1 + CU_INHIBITOR_GUT/KI_GUT)
INH_HEP  = (CU_INHIBITOR_HEP/KI_HEP) / (1 + CU_INHIBITOR_HEP/KI_HEP)
INDUCT   = 1 + ALPHA_IND * CU_INHIBITOR_HEP    ; chronic
TRANSPORT_INH = (CU_INHIB/KI_TRANSPORT) / (1 + CU_INHIB/KI_TRANSPORT)

CL_HEP   = CL_BASE * (FM*(1-INH_HEP) + (1-FM)) * INDUCT
CL_REN   = CL_R_BASE * (1 - TRANSPORT_INH)
CL       = CL_HEP + CL_REN
V        = V_BASE * (1 - TRANSPORT_INH * KP_FACTOR)  ; uptake transporter
```

**핵심**: 각 mechanism을 *분리된 covariate*로 modeling. 합쳐서 modeling하면 mechanism 식별 불가.

#### K. Zettelkasten Atom

```yaml
---
aliases: [Multifaceted DDI, Transporter-mediated DDI, Atorvastatin rifampin, Digoxin quinidine, Fluconazole midazolam, OATP1B1 inhibition, Route effect DDI]
tags: [pharmacometrics/ddi, transporters, oatp, pgp, multi-mechanism, tozer]
up: "[[T6 경쟁적 억제 정량]]"
related: ["[[T1 Saturable renal transport]]", "[[T2 First-pass]]", "[[T3 TMDD]]", "[[T4-EXT MBI]]", "[[T8 Induction]]"]
source: "Tozer 5e, Ch.17, pp.553–566; Fig.17-10/11/19; Table 17-2/17-7/17-8"
---

Multifaceted DDI: 같은 약물 쌍에 복수 mechanism 동시. Digoxin-Quinidine (Table 17-8): PgP renal+biliary inhibition + tissue uptake transporter inhibition → CL 50%↓, Vd 50%↓, F 13%↑. Atorvastatin-Rifampin IV acute (Fig.17-19): OATP1B1 inhibition → AUC 7×, Cmax 10×, t½ 8→3h, Vd 17×↓ (rate-limiting step shift metabolism→uptake). Multiple-dose rifampin 만성 = induction dominant 反대 효과. Rosuvastatin-Cyclosporine (Fig.17-11): OATP1B1 → 11× Cmax. Diltiazem-Lovastatin (Table 17-7): oral 3.57× vs IV 1.27× (gut wall inhibition). Fluconazole-Midazolam (Fig.17-10): F_G 0.57→0.88, F_H 0.42→0.72 (gut+hepatic 분리). Lopinavir/Ritonavir = beneficial MBI combination. 임상 진단: CL/F/Vd/CL_R 각각 분리 측정 후 mechanism 합산. NONMEM: 각 mechanism 분리 covariate.
```

---

### T10. Pharmacodynamic Interactions — Eq.17-21, Isobologram

<!-- ANCHOR -->
T5–T9가 모두 *PK DDI*였다면, T10은 *PD DDI* — 두 약물이 *같은 receptor target*에서 경쟁/협력. Stage 1 M8 (competitive PD), M9 (noncompetitive·enantiomer·multiple binding)의 통합 임상 적용. 본 카드는 단순히 PD 카테고리를 다루는 것이 아니라 *PK DDI와 PD DDI를 분리하는 진단 framework*를 제공.

<!-- MASTER LENS -->
> **[개념 Big Idea]**
>
> **왜 치명적**: 환자가 morphine + diphenhydramine 동시 복용 → 호흡 저하·과진정. 임상의가 "두 약물 모두 sedative이니까 시너지" 가정 → diphenhydramine dose 감량. 그러나 Eq.17-21 (두 full agonist 모델)에 따르면 *Emax 천장이 존재* → 두 약물이 같은 receptor 경쟁 시 dose 감량보다 *한 약물 중단*이 더 효과적. 또한 *Cu unchanged 확인* 없이 PD interaction 가정하면 PK DDI (e.g., diphenhydramine이 morphine glucuronidation inhibit) missed.
>
> **체화 직관**: PD vs PK DDI 진단 = *unbound C가 변하는가?* Cu 변화 = PK DDI; Cu unchanged + 효과 변화 = PD DDI. Tozer Ch.17 명시 (p.536): "Distinction between the two is made by relating response to the unbound plasma concentration of the pharmacologically active moiety." 이 단일 question이 임상 의사결정의 첫 분기점.
>
> **이 직관을 머릿속에 박고 아래를 읽어라**: 본 카드는 Stage 1 M8 (Eq 3:49 EC50 shift)·M9 (Eq 3:50 Emax shift, ketamine enantiomer)이 임상 isobologram framework로 외화. PD additivity vs synergy vs antagonism의 단일 graphical tool.

#### A. Two Full Agonists at Same Receptor — Eq.17-19 ~ 17-21

**Eq.17-19** (single agonist):
$$E = \frac{E_{max} \cdot C^\gamma}{C_{50}^\gamma + C^\gamma}$$

**Eq.17-20** (rearrangement):
$$\frac{E}{E_{max}} = \frac{C^\gamma / C_{50}^\gamma}{1 + C^\gamma / C_{50}^\gamma}$$

**Eq.17-21** (two full agonists, same target, $\gamma_A = \gamma_B$):
$$\frac{E}{E_{max}} = \frac{\dfrac{Cu_A^\gamma}{Cu_{50,A}^\gamma} + \dfrac{Cu_B^\gamma}{Cu_{50,B}^\gamma}}{1 + \dfrac{Cu_A^\gamma}{Cu_{50,A}^\gamma} + \dfrac{Cu_B^\gamma}{Cu_{50,B}^\gamma}}$$

**핵심 결론** (Fig.17-20):
- 두 full agonist 동시 → $E_{max}$ 천장 *초과 불가*
- 한 약물이 이미 80% Emax 도달 → 다른 약물 추가 한계 효과 미미
- 두 약물 모두 saturating 농도일 때 → 합쳐도 단일 농도와 동일 Emax

**임상 함의**: 같은 receptor 두 agonist 조합 시 *시너지 없음*. 한 약물 dose 증량과 동등한 효과만 얻음. 임상 적용: morphine + meperidine (둘 다 µ-opioid agonist) 조합 *비합리*.

#### B. Stage 1 M8 + M9 통합 — PK·PD mathematical equivalence

**핵심 통찰** (Stage 3 T6 카드 K절과 mirror):
- Stage 1 M8 (PD competitive antagonism): $EC_{50}^{app} = EC_{50} \cdot (1 + I/K_i)$
- Stage 3 T6 (PK competitive inhibition): $K_m^{app} = K_m \cdot (1 + Cu_I/K_I)$
- 동일 mathematical structure (단순 mass action competition)

**차이점**:
- PD: receptor binding equilibrium (수 sec~min)
- PK: enzyme binding equilibrium (수 min)
- 둘 다 같은 ODE structure로 modeling 가능

**Stage 1 M9 (noncompetitive)** — PD 분야의 *Eq.17-21 변형 케이스*:
- Noncompetitive: Emax 자체 감소 (allosteric)
- Eq.17-21은 *competitive (same site)*이지만 *cooperative not assumed*
- Enantiomer interaction (ketamine R/S, Eq 3:53): 같은 receptor에 다른 친화도 → R-isomer가 S-isomer를 competitively block

#### C. Isobologram (Fig.17-21) — 가산성·시너지·길항 진단

**Isobole**: 동일 response 만드는 두 약물 농도 조합의 곡선

**가산성 (additivity)**:
- 두 약물이 *서로 대체 가능* (potency 비율로 환산)
- Isobole = 직선
- $\dfrac{Cu_A}{Cu_{50,A}} + \dfrac{Cu_B}{Cu_{50,B}} = $ const

**시너지 (synergism)**:
- 실제 isobole이 직선 아래 (concave)
- 두 약물 조합이 *예상보다 적은 농도*로 동일 효과
- 예: midazolam + propofol (induction of anesthesia)

**길항 (antagonism)**:
- 실제 isobole이 직선 위 (convex)
- 두 약물 조합이 *예상보다 많은 농도* 필요
- 예: isoproterenol + propranolol (β-receptor)

**임상 함의**:
- 시너지는 *별개 mechanism*에서 자주 (e.g., thiazide diuretic + β-blocker 혈압 강하)
- 길항은 *같은 receptor 반대 효과* (agonist + antagonist)

#### D. Greco Universal Response Surface (Eq.17-22) — 정량 framework

**Loewe additivity 기반**:
$$1 = \frac{Drug_1}{IC_{50,1} \cdot \left(\dfrac{E}{E_{CON}-E}\right)^{1/m_1}} + \frac{Drug_2}{IC_{50,2} \cdot \left(\dfrac{E}{E_{CON}-E}\right)^{1/m_2}} + \frac{\alpha \cdot Drug_1 \cdot Drug_2}{IC_{50,1} \cdot IC_{50,2} \cdot \left(\dfrac{E}{E_{CON}-E}\right)^{(1/(2m_1)+1/(2m_2))}}$$

**파라미터 $\alpha$ (interaction term)**:
- $\alpha > 0$ (lower 95% CI > 0): **시너지** statistically significant
- $\alpha < 0$ (upper 95% CI < 0): **길항** statistically significant
- 95% CI overlap 0: **가산성** (additive)

**적용**: 항암제 (anticancer) 조합 — 초기 application. 항생제 (antimicrobial) 조합 — 후속 application.

#### E. PD DDI 임상 사례 (Tozer Ch.17)

**Avoidable PD DDI (Table 17-1)**:
- **Diphenhydramine ↔ Alcohol** (mutual sedation): 두 sedatives PD additive
- **Naloxone → Fentanyl** (analgesia 길항): naloxone이 µ-opioid receptor 경쟁 antagonist

**Beneficial PD combinations**:
- **Vitamin K → Warfarin (over-anticoagulation 교정)**: vitamin K가 clotting factor 합성 회복 — *PD antagonism intentional*
- **Naloxone → Opioid overdose 치료**: 의도적 antagonism

**시너지 PD 예**:
- **Midazolam + Propofol** (induction of anesthesia): 다른 receptor (GABA-A 다른 subunit)에서 시너지
- **Cyclosporine + Tacrolimus** (immunosuppression): 같은 calcineurin pathway, additive 또는 시너지

**길항 PD 예**:
- **Isoproterenol + Propranolol** (cardiostimulant): β-receptor 같은 site agonist + antagonist
- **Atropine + Pilocarpine** (muscarinic): 같은 receptor 반대 effect

#### F. PK vs PD DDI 임상 진단 알고리즘

**핵심 측정**: Unbound plasma concentration of pharmacologically active moiety.

**진단 sequence**:
1. Multiple dose 정상상태 도달 후 효과 변화 확인
2. 동일 시점 unbound C 측정
3. 분기:
   - **Cu 변화 + 효과 변화**: PK DDI (T6/T7/T8/T9 framework 적용)
   - **Cu unchanged + 효과 변화**: PD DDI (본 T10 framework 적용)
   - **Cu 변화 + 효과 unchanged**: PD compensation (드물지만 documented)
   - **Cu unchanged + 효과 unchanged**: 임상적으로 무의미한 측정 변동

#### G. Stage 1 M8/M9 + Stage 3 T10 통합 — Session 종결 framework

본 T10 카드가 Session 08의 *최종 통합 layer*:
- M8/M9 (Stage 1 mechanism)
- 임상 isobologram·Greco framework (Stage 3 적용)
- PK vs PD 진단 (전체 Session의 첫 분기점이 마지막에 다시 등장)

이 *circular structure*가 28-session protocol의 mastery 표시 — 첫 mechanism이 마지막 임상 framework로 *닫혀서 돌아옴*.

#### H. Endogenous compound competition (CONTEXT, p.568)

> "drugs are invariably competing with one or more endogenous compounds for a target"

대부분 약물이 endogenous ligand (acetylcholine, dopamine, glutamate 등)와 *target에서 경쟁*. 그러나 endogenous concentration *target site에서* 측정 어려움 → IIV의 일부.

#### I. Active metabolite as PD competitor (CONTEXT, p.568)

약물의 metabolite가 *같은 target에 agonist/antagonist* 경우 — Tozer Ch.18 (Metabolites and Drug Response)에서 자세히. 본 카드는 1줄 인지: morphine ↔ morphine-6-glucuronide (둘 다 µ-opioid agonist, M6G가 더 potent in some assays).

#### J. NONMEM (PD interaction with Eq.17-21)

```
$PRED
; --- PD interaction model (two competing agonists) ---
DRIVER_A = (CU_A / CU50_A)**GAMMA
DRIVER_B = (CU_B / CU50_B)**GAMMA
EFFECT   = EMAX * (DRIVER_A + DRIVER_B) / (1 + DRIVER_A + DRIVER_B)
```

#### K. Zettelkasten Atom

```yaml
---
aliases: [Eq.17-21, Isobologram, PD interaction, Pharmacodynamic DDI, Loewe additivity, Greco]
tags: [pharmacometrics/ddi, pharmacodynamics, receptor-competition, isobologram, tozer]
up: "[[M8 PD competitive antagonism]]"
related: ["[[M9 PD enantiomer noncompetitive]]", "[[T6 PK competitive inhibition]]", "[[Tozer Ch.18 Metabolites]]"]
source: "Tozer 5e, Ch.17, pp.566–569; Eq.17-19/20/21/22; Fig.17-20/17-21"
---

PD DDI: 두 full agonist 같은 receptor 경쟁 (Eq.17-21) → Emax 천장 초과 불가 (Fig.17-20). Stage 1 M8 PD = Stage 3 T6 PK competitive와 mathematical structure 동일 (mass action competition). Isobologram (Fig.17-21): 직선=가산성, 아래=시너지 (midazolam+propofol), 위=길항 (isoproterenol+propranolol). Greco Eq.17-22 universal response surface: α 부호로 통계적 시너지/길항 분류. PK vs PD 진단 알고리즘: Cu 변화 = PK DDI; Cu unchanged + 효과 변화 = PD DDI (Tozer p.536). Session 08 circular closure — 첫 mechanism이 마지막 임상 framework로 돌아옴.
```

---


## §5. Confusion Pair Dissection (3-Stage 통합)

본 §5는 9개 혼동쌍으로 구성. CP1–CP4는 Stage 1 정본; CP5–CP6는 Stage 2 추가; CP7–CP9는 Stage 3 신규. **Critical Blow는 CP8 (Inhibition vs Induction)** — Stage 3 Apex 혼동쌍.

---

<!-- CONFUSION -->
### CP1. Capacity-limited (M2) vs Flow-limited (M7) — Stage 1 정본 요약

| 비교 차원 | A. Capacity-limited | B. Flow-limited |
|---|---|---|
| **표면적 유사성** | 둘 다 nonlinear PK; dose↑ 시 CL 변화 | |
| **수식/코드 형태** | $Cl = V_m/(K_m + C)$ — Vm/Km 한계 | $Cl = Q_H \cdot E_H$ — Q_H 한계 |
| **생리학적 지시체** | 효소·운반체 capacity (intrinsic) | 장기 혈류 |
| **dose↑ 효과** | C↑ 따라 CL↓ (saturation) | E_H 변화 따라 CL 변화, but CL 자체 dose 무관 |
| **Stage 2 임상 prototype** | Phenytoin, alcohol, ascorbic acid | Lidocaine, propranolol |
| **⚡ 기억 고리** | "Capacity = *공장이 병목* (효소 수 한계). Flow = *고속도로가 병목* (혈류 한계). Phenytoin은 공장 작아서 dose 늘리면 줄을 서서 못 빠짐. Lidocaine은 고속도로 좁아서 dose 무관하게 빠지는 속도 일정." | |

---

<!-- CONFUSION -->
### CP2. PK22 Autoinduction (M4) vs Multiple-dose accumulation — Stage 1 정본 요약

| 비교 차원 | A. PK22 Autoinduction | B. Multiple-dose accumulation |
|---|---|---|
| **표면적 유사성** | 둘 다 multiple dose에서 single-dose와 다른 PK | |
| **Mechanism** | 효소 turnover ODE 변화 ($R_{in}$↑ feedback) | Linear superposition |
| **t½ 변화** | 시간에 따라 *감소* (CL↑) | 시간 무관 |
| **Css/Single dose 비** | Css가 *예상보다 낮음* (CL↑) | $1/(1-e^{-k\tau})$ 정확 prediction |
| **NONMEM 진단** | enzyme compartment ODE 필수 | ADVAN 표준 |
| **⚡ 기억 고리** | "Autoinduction은 *약이 자기 자신의 무덤을 판다*. 첫 dose = 무덤 시작, 매일 dose = 무덤 깊어짐, multiple dose t½ = 무덤이 다 파인 후. Linear accumulation은 *같은 무덤에 비가 차오를 뿐*, 무덤 자체는 안 변함." | |

---

<!-- CONFUSION -->
### CP3. Open system (M5) vs Closed system (in vitro) — Stage 1 정본 요약

| 비교 차원 | A. Open (in vivo) | B. Closed (in vitro) |
|---|---|---|
| **표면적 유사성** | 둘 다 단백 결합·fu 측정 | |
| **System | Continuous input/output (homeostatic) | Fixed total amount |
| **Cu 결정 인자** | $Cu = K^0/CL_u$ — *dosing rate*만 | $Cu \cdot fu = C_{total}$ — *fu* 변화 |
| **단백 변화 효과** | Cu 무변화 (CL_int 무관) | Cu 변화 (단백 변화 직접 반영) |
| **임상 함의** | Dose 조정 사유 아님 | "Displacement = 위험" 가설의 출처 |
| **⚡ 기억 고리** | "Closed = *주머니 속 물*: 실 풀려 (단백 분해) 더 많이 떠돌아. Open = *수도꼭지에서 흐르는 강*: 자갈 (단백) 깔아도 강물 양 무관. In vitro 실험은 주머니 속, in vivo는 강." | |

---

<!-- CONFUSION -->
### CP4. M8 PD competitive (Eq 3:49) vs M9 PD noncompetitive (Eq 3:50) — Stage 1 정본 요약

| 비교 차원 | A. Competitive (M8) | B. Noncompetitive (M9) |
|---|---|---|
| **수식** | $EC_{50}^{app} = EC_{50}(1 + I/K_i)$ | $E_{max}^{app} = E_{max}/(1 + I/K_i)$ |
| **영향** | EC50 이동 (potency↓) | Emax 감소 (efficacy↓) |
| **Inhibitor 농도↑ 시 회복** | dose↑로 회복 가능 | dose 무관, 회복 불가 |
| **수용체 위치** | 같은 active site | 다른 allosteric site |
| **⚡ 기억 고리** | "Competitive = *문 앞 줄서기*. 줄 더 많아도 강한 사람 (dose↑) 들어감. Noncompetitive = *문 자체를 부수기*. dose 아무리 높여도 부서진 문 통과 불가." | |

---

<!-- CONFUSION -->
### CP5. T4 MBI vs M8/T6 Competitive Inhibition — Stage 2 추가 (Stage 2 Critical Blow)

본 쌍은 임상 DDI에서 가장 자주 혼동되는 두 mechanism. Stage 3 Ch.17의 Eq.17-9 (competitive) vs Eq.17-13/14 (MBI) 정량 prediction 분기의 mechanism 기반.

| 비교 차원 | A. Competitive inhibition | B. MBI (Mechanism-based) |
|---|---|---|
| **표면적 유사성** | 둘 다 효소 활성 감소 → CL↓ → AUC↑. Inhibitor 추가 후 substrate AUC 증가 패턴 동일하게 보임. | |
| **수식/코드 형태** | $K_m^{app} = K_m(1 + I/K_I)$, *효소 양 불변* | $E^{ss}$ 자체 감소 (Stage 1 M3 turnover ODE에 분해 항 추가) |
| **생리학적/구조적 지시체** | Reversible 결합 — active site competition. *분 단위 평형* | Inactivation substrate. *효소 t½ 단위 dynamics* |
| **시간 의존성** | Inhibitor C에 *즉시* 반응. Onset/offset = inhibitor PK | Onset/offset = *enzyme t½* (3–5d). Inhibitor 단기 노출도 long-term effect |
| **Single vs Multiple dose** | Single dose에 일관된 inhibition | Single vs day 7 *질적으로 다른* 패턴 (clarithromycin Fig.16-26) |
| **임상 결과** | Cimetidine-phenytoin: K_m' 4→6, Css 50%↑. Inhibitor 중단 즉시 회복 | Clarithromycin-saquinavir: QT 연장. 중단 후 3–7d 회복 |
| **수식 지표** | $Cu_I/K_I$만 | $k_{inact} \cdot Cu_I / (K_I \cdot k_E)$ — *modifier 추가* |
| **⚡ 기억 고리** | "Competitive는 *enzyme 한 자리에서 두 ligand가 의자 뺏기*. MBI는 *enzyme 자체를 자살하게 만드는 substrate*. 의자가 차 있으면 다음 손님은 기다리지만 (reversible, 의자 다시 비워짐), 의자가 부서지면 새 의자 만들 때까지 손님 못 받는다 (suicide, enzyme 합성 기다림)." | |

---

<!-- CONFUSION -->
### CP6. M5 Open system (일반 단백) vs T3 TMDD — Stage 2 추가

| 비교 차원 | A. M5 Open system protein binding | B. T3 TMDD |
|---|---|---|
| **표면적 유사성** | 둘 다 단백·수용체 saturable binding. fu·Kd·Bmax 동일 파라미터. 동일 mass action 도출. | |
| **수식 형태** | $C_u = K^0/CL_u$ (open system) | $V_d, CL$이 dose에 따라 *변동* |
| **결합 단백 capacity** | 매우 큼 (Albumin 600 µM, AAG 15 µM) | 매우 작음 (target receptor nM) |
| **결합 affinity** | 중간 ($K_d$ µM) | 매우 높음 (mAb $K_d$ pM–nM) |
| **임상 dose에서 농도/Kd** | 일반적으로 ≪ albumin Kd | 일반적으로 ≈ Kd (saturation 영역) |
| **임상 dose 조정** | 단백 변화는 사유 *아님* (Stage 1 M5) | Dose 자체가 PK 결정 (PK·PD 분리 불가) |
| **Vd 변화** | 농도 무관 | 농도 의존 (Bosentan 0.67→0.16 L/kg) |
| **⚡ 기억 고리** | "Open system = *수도꼭지에서 흐르는 강* — 자갈 (단백) 깔아도 흐르는 사람 수 무관. TMDD는 *그 자갈 자체가 사람을 끌어당기는 magnetic pebble* — 자갈에 매달린 사람 비율이 dose에 따라 변하고, 자갈에 매달린 사람이 *제거되는 통로*이기도. 일반 단백은 storage, target은 *함정*." | |

---

<!-- CONFUSION -->
### CP7. T5 Displacement-only vs T6 Inhibition — Stage 3 추가

본 쌍은 1967년 historical 가설 (warfarin–phenylbutazone "displacement") vs 실제 mechanism (inhibition + displacement)의 임상 진단 framework. 임상의가 Total C와 Unbound C를 분리 측정하지 못하면 두 mechanism 구별 불가.

| 비교 차원 | A. Displacement-only (T5) | B. Inhibition (T6) |
|---|---|---|
| **표면적 유사성** | 둘 다 victim drug Total C 변화. 단백 결합 약물에서 동시 발생 가능. | |
| **Mechanism** | 결합 단백 site 경쟁 (M5 mass action) | 효소 active site 경쟁 (M2 capacity) |
| **수식** | $f_u \uparrow$, $CL_{int}$ 무변화 | $CL_{int}$ ↓, $f_u$ 무변화 |
| **Total C 변화** | ↓ (CL = fu·CLint, fu↑로 CL↑) | ↑ (CL↓로 직접) |
| **Unbound C 변화 (sustained)** | **무변화** ($Cu = K^0/CL_u$) | **↑** ($Cu \uparrow$ as $CL_{int} \downarrow$) |
| **임상 효과 변화** | 무 (Cu unchanged) | 유 (Cu↑ 비례) |
| **임상 prototype** | Phenytoin–Valproate (Fig.17-3) | Theophylline–Enoxacin (Fig.17-6) |
| **Mixed case** | Warfarin–Phenylbutazone (Fig.17-18): displacement *AND* inhibition | |
| **진단 단일 question** | Unbound C가 sustained 변화하는가? No = displacement only / Yes = inhibition | |
| **임상 dose 조정** | 불필요 (Cu unchanged) | 필요 (Cu↑) |
| **⚡ 기억 고리** | "Displacement = *주차장에서 자리 뺏기*. 자리 (단백 site) 적어졌지만 *차의 도로 진입 (효소 처리)*은 정상 → 도로 위 차 (Cu) 무변화. Inhibition = *도로 자체 차단*. 자리는 그대로지만 차가 도로에 못 들어가 → 도로 위 차 (Cu) 줄어드는 것이 아니라 *건물 안 차 (drug in body) 누적* → Cu 증가." | |

---

<!-- CONFUSION -->
### CP8. T6 Inhibition vs T8 Induction — **Stage 3 Critical Blow**

본 쌍은 Stage 3 가장 중요한 혼동쌍 — *시상수와 방향성 모두 반전*. NDA reviewer가 inhibitor와 inducer를 혼동하면 임상 환자 dose 조정이 *완전히 반대 방향*으로 잘못됨.

| 비교 차원 | A. Inhibition (T6/T4-EXT) | B. Induction (T8) |
|---|---|---|
| **표면적 유사성** | 둘 다 enzyme activity 변화 → CL 변화 → AUC 변화. 같은 약물 (e.g., rifampin)이 둘 다 가능. | |
| **Mechanism (Stage 1 M3 ODE 변형)** | 효소 *분해 가속* (MBI) 또는 *active site 점유* (reversible) | 효소 *합성 가속* ($R_{in}$↑) |
| **CL 변화 방향** | **↓** | **↑** |
| **AUC 변화 방향** | **↑** | **↓** |
| **t½ 변화** | **↑** (CL↓) | **↓** (CL↑) |
| **시간 차원 dominant** | Reversible: inhibitor PK<br>MBI: enzyme t½ (~3d) | Inducer t½ 또는 enzyme t½ (느린 쪽) |
| **임상 prototype** | Erythromycin → Sildenafil (Table 17-1) | Rifampin → Warfarin (Table 17-1) |
| **Withdrawal recovery** | Reversible: 즉시<br>MBI: 2주 (CYP3A4) | Inducer t½에 따라 (phenobarbital 4d → 3–4주) |
| **임상 dose 조정 방향** | **감량** (toxicity 위험) | **증량** (효과 부족 위험) |
| **약물 동일 중복 사례** | Rifampin은 OATP1B1 *inhibitor* (acute) + CYP3A *inducer* (chronic) — Atorvastatin–Rifampin (Fig.17-19) |
| **NDA labeling 함의** | Section 12.3 "expected AUC ratio increase" + dose 감량 권고 | Section 12.3 "expected AUC ratio decrease" + dose 증량 또는 alternative |
| **⚡ 기억 고리 (Critical Blow)** | "Inhibition = *공장 노동자 묶기* (reversible) 또는 *공장 노동자 죽이기* (MBI). 어느 쪽이든 즉시 또는 장기 효과. Induction = *공장 노동자 새로 고용*. 노동자 (enzyme) 늘어 처리량 증가. Critical Blow: rifampin은 *고용 + 묶기 동시* — IV acute에서는 OATP1B1 묶기, multiple dose에서는 CYP3A4 신규 고용. *dose 조정 방향이 정반대*이므로 *시점·route 별로 separate prediction 필수*. NDA에서 두 mechanism 동시 다루지 못하면 deficiency letter." | |
| **임상 치명적 결과** | dose 그대로 유지 → toxicity (warfarin bleeding, statin myopathy) | dose 그대로 유지 → 치료 실패 (oral contraceptive + rifampin 임신, anticoagulation 부족) |

---

<!-- CONFUSION -->
### CP9. T6 Single Inhibitor vs T7 PM × Inhibitor — Stage 3 추가

본 쌍은 약물유전체 phenotype에 따라 같은 inhibitor가 *전혀 다른 정량 영향*을 미치는 mechanism. 임상의가 phenotype 무시하고 균일 dose 조정 시 PM 환자에서 *order of magnitude* 위험.

| 비교 차원 | A. EM + Inhibitor (T6) | B. PM + Inhibitor (T7) |
|---|---|---|
| **표면적 유사성** | 둘 다 substrate AUC↑. 같은 inhibitor 작동. | |
| **수식** | Eq.17-11: $1/[fm/(1+Cu_I/K_I) + (1-fm)]$ | Eq.17-18: $1/(1 - fm_{POLY} - fm_{NP})$ |
| **분모 구조** | $fm/(1+Cu_I/K_I) + (1-fm)$ — inhibitor strength dependent | $(1 - fm_{POLY} - fm_{NP})$ — inhibitor strength independent (full inhibition 가정) |
| **AUC ratio 상한** | $1/(1-fm)$ — inhibitor strength→∞ 시 점근 | $1/(1-fm_{POLY}-fm_{NP})$ — *fm 두 경로 합* |
| **중요 변수** | $Cu_I/K_I$ (inhibitor strength) | $fm_{POLY}$ (polymorphic 비율) |
| **임상 prototype** | Theophylline–Enoxacin (fm=0.67, max 3×) | Omeprazole–Clarithromycin in PM (fm_POLY=0.92, **33×**) |
| **약물유전체 testing 필요성** | 일반적으로 불필요 | **필수** (CYP2D6/2C19 genotyping) |
| **임상 dose 조정** | 25–50% 감량 | 종종 contraindication |
| **⚡ 기억 고리** | "EM + inhibitor = *대로(polymorphic) 막힌 우회로 (nonpolymorphic) 살아 있음* — 우회 가능, dilute 효과. PM + inhibitor = *대로 이미 결손 + 우회로마저 막힘* — *최후의 잔길 (CL_O)만 남아* AUC 폭발. fm_POLY가 클수록 잔길이 작아져 발산." | |

---

## §7. Self-Test: Active Recall Module (3-Stage 통합 — Q1–Q20)

**구성**: 회상 40% (8 questions) / 적용 60% (12 questions). Stage 1 (Q1–Q10) + Stage 2 (Q11–Q15) + Stage 3 (Q16–Q20). Q20 = **Boss Dilemma 최종형** (NDA DDI label strategy, Socratic Dilemma).

---

<!-- SELF-TEST -->
### Stage 1 — Q1–Q10 (Gabrielsson mechanism canonical) — 정본 요약

*정본은 별도 Stage 1 산출물 참조. 본 통합본은 SR 태그와 핵심 키워드만 표시.*

- **Q1 [회상, ★★]**: M2 MM 수식 도출 — $V_m, K_m, Cl(C)$
- **Q2 [회상, ★]**: M3 turnover ODE — $dE/dt = R_{in} - k_{out}E$
- **Q3 [적용, ★★]**: PK17 데이터 (Gabrielsson) — linear vs MM 모델 판별
- **Q4 [적용, ★]**: PK18 ethanol (Gabrielsson) — Vmax/Km 초기 추정 절차
- **Q5 [적용, ★★]**: PK22 autoinduction (Gabrielsson) — kout/E0 의 임상 의미
- **Q6 [회상, ○]**: M5 open system 결론 — Cu = K⁰/CLu
- **Q7 [적용, ★]**: Drug-metabolite flip-flop 진단
- **Q8 [회상, ○]**: M8 Eq 3:49 EC50 shift formula
- **Q9 [적용, ★]**: M9 ketamine enantiomer interaction (Eq 3:53)
- **Q10 [Boss Dilemma, ★★]**: Capacity vs flow-limited 약물의 hepatic disease 환자 dose 조정 trade-off

---

<!-- SELF-TEST -->
### Stage 2 — Q11–Q15 (Tozer Ch.16 임상 정량) — Stage 2 산출물에서 통합

*Stage 2 산출물 그대로 통합. 본 위치에 있는 그대로 유지.*

#### Q11 [적용, ★★]
한 phenytoin 환자가 300 mg/day에서 안정적 Css = 8 mg/L. 환자가 질문: "내가 앞으로 10년 동안 phenytoin 복용해야 하는데, 일일 dose를 50 mg 증량하면 Css가 어떻게 되나요?" 가정: $K_m' = 4$ mg/L, 환자 본인의 $V_m$을 위 데이터에서 산출.

> **정답**:
> Eq.16-7로부터 $V_m$ 추정: $C_{ss} = K_m' R_0/(V_m - R_0)$ → $8 = 4 \cdot 300/(V_m - 300)$ → $V_m = 450$ mg/day.
>
> 새 dose 350 mg/day: $C_{ss}^{new} = 4 \cdot 350/(450 - 350) = $ **14 mg/L**.
>
> 50 mg (17%) 증량 → 농도 8→14 mg/L (75% 증가). Vm=450의 78% 영역에 있어 분모 (Vm−R₀)가 작아 변화에 민감.
>
> **t₉₀ 도달**: Eq.16-10 (V=50 L 가정): $t_{90} = 4 \cdot 50 \cdot (2.303 \cdot 450 - 0.9 \cdot 350)/(100)^2$ ≈ **14일**.
>
> **임상 권고**: 증량 후 *2–3주* trough 추적, 18 mg/L 초과 시 즉각 감량. "한 번에 농도 안정 안 됨; 14 mg/L 안정까지 약 2주."
>
> **다음 깊이 질문**: 만약 5년간 hepatic cirrhosis 진행해 V_m 450→350 mg/day가 된다면 같은 350 mg dose에서 어떤 일이?

#### Q12 [적용, ★★]
Dicloxacillin (T1)을 신부전 환자에게 처방. 정상 환자 1g IV 후 CLR=104 mL/min. 신부전 환자 GFR=30 mL/min (정상 25%). 동일 AUC를 위한 dose 조정 추론. Saturable secretion mechanism 고려.

> **정답**:
> Dicloxacillin은 secretion 우세 (CLR≫fu·GFR=4.8 in 정상). 신부전:
> - GFR↓ → fu·GFR ≈ 1.2 mL/min (작은 감소)
> - Secretion mechanism도 신부전에서 일반적으로 감소
>
> 단순 GFR 비례 dose 감량 (25%)은 saturable secretion 약물에서 부족. 신부전 환자 dose 그대로 유지 시 plasma C↑ → secretion saturable에 의해 CLR 추가 감소 → AUC 비선형으로 더 증가.
>
> **권고**: (1) Dose 감량 (정상 dose의 25% 시작), (2) 측정된 신환 plasma C로 individual CLR 산출, (3) Cmax·trough 모두 측정. 단지 GFR 비례 dose 감량은 1차 추정.
>
> **다음 깊이 질문**: 같은 신부전 환자에서 ascorbic acid (saturable reabsorption) 권고는 dicloxacillin과 *반대* 방향?

#### Q13 [적용, ★]
Trandolapril (Fig.16-19)을 임상에서 단일 dose만 측정한 PK study가 *biexponential decline*을 발견. 분석가가 "이 약은 2-compartment 분포 kinetics"라 결론. 동의?

> **정답**:
> **결론**: 동의 *불가*. 단일 dose data만으로는 *concentration-dependent protein binding* (TMDD)와 *2-compartment 분포 kinetics*가 mathematically *동일 형태*. 두 mechanism은 *근본적으로 다른* 임상 함의.
>
> **추가 진단 절차**:
> 1. Multiple dose PK: accumulation ratio가 long t½ 예측보다 *작다면* (1.49 actual) → TMDD 의심
> 2. 여러 dose의 dose-normalized profile 중첩: 2-compartment는 dose-비례 superposition; TMDD는 dose에 따라 곡선 모양 변화
> 3. Plasma protein binding 직접 측정: fu가 농도에 따라 변화면 TMDD
> 4. Mass balance·organ uptake: 2-compartment는 peripheral compartment 축적; TMDD는 target 축적
>
> **임상 차이**: 2-compartment는 dose escalation 시 PK 비례; TMDD는 long t½ 효과가 *감소*; AUC vs dose 비선형.
>
> **다음 깊이 질문**: 어떤 추가 *single dose* 실험이 두 mechanism을 구별 가능?

#### Q14 [회상, ★]
M3-EXT carbamazepine autoinduction에서 turnover time ~5일이 임상 dose titration 권고에 어떤 *정량적* 함의?

> **정답**:
> **Plateau 도달**: 4–5 × turnover time = **20–25일** (carbamazepine).
>
> PK22 (Stage 1 M4): turnover t½ = 30h → plateau 4–5 × 30h = **5–6일**.
>
> **차이**: 효소 종류·induction 강도 차이. Carbamazepine (CYP3A4 dominant) — 시스템 전체 *느린 dynamics*.
>
> **임상 권고 분기**:
> - 단일 dose t½ (12h)으로 7일이면 정상상태 추정 → *완전히 잘못*
> - Carbamazepine 매 trough 측정: 1주 이상; *3주 전 dose 조정 후* 첫 의미 trough
>
> **임상 사고 패턴**: "*약물 t½이 아닌 효소 t½이 master clock*."
>
> **다음 깊이 질문**: Stage 3에서 carbamazepine이 *다른 약물* 효소를 induction (cf carbamazepine-warfarin)할 때 자기 turnover와 동일한 induction time course 예상?

#### Q15 [Boss Dilemma — Socratic Dilemma extension, ★★]

**시나리오 (Stage 1 Q10의 임상 적용 확장)**:
신약 후보 X NDA 책임자. X는 Phase 3 통과·NDA 직전. PK 특성:
- Single dose IV: linear (Vmax/Km 잘 정의 안 됨; 농도 항상 Km 미만)
- Single dose oral: F=15%
- Multiple dose oral (Phase 2/3): dose 5× → AUC 8× → *비선형*
- Plasma t½: single 4h, day 14 multiple 18h

NDA reviewer에게 어떤 비선형 mechanism 제안?

**Option A — Saturable first-pass (T2)**
**Option B — MBI autoinhibition (T4)**
**Option C — TMDD (T3)**
**Option D — 위 3가지 동시**

> **정답 (수석 NDA 전략의 Trade-off 논리)**:
>
> **결정**: **Option D (mechanism 다중성 인지) + 우선순위 진단 study 추가**. NDA timeline 압박에도 *지금* 추가 study 안 하면 *post-marketing*에서 black box warning.
>
> **Option별 deficiency**:
> 1. A 단독: "single IV linear, multiple t½ 4→18h — first-pass만으로는 multiple t½ 증가 불가" → Deficiency Letter
> 2. B 단독: "MBI라면 dose-비례 AUC 어떻게 설명? Saturable first-pass 없으면 oral 비례 5→8 anomaly 미설명"
> 3. C 단독: "TMDD라면 IV에서도 비선형 expected"
> 4. D + study: 가장 방어 가능. (a) IV-oral microdose (F dose 의존), (b) Day 14 probe substrate (midazolam) → MBI 진단, (c) Target binding kinetics → TMDD
>
> **NDA timeline**: 6–12개월 추가 mechanistic study vs deficiency letter 18–24개월 지연. 사전 study가 더 빠름.
>
> **수석 모델러 통찰**: Mechanism 진단 → robust label. "mechanism이 명확하면 dose가 안전". Stage 3 Ch.17 정량 DDI prediction이 본 사례에 직접 적용.
>
> **다음 깊이 질문**: 위 mechanism 식별 후, FDA가 요구하는 *Drug Interaction Studies* (Stage 3 T6 Eq.17-11 기반) 우선순위는?

---

<!-- SELF-TEST -->
### Stage 3 — Q16–Q20 (Tozer Ch.17 DDI 정량 framework) — 신규

#### Q16 [회상, ★★]
Eq.17-11 (FDA DDI Guidance 핵심식)을 기억으로 재현하라. 다음 변수들의 의미를 명시:
- AUC ratio
- $f_m$
- $Cu_I/K_I$
- $F_{inhibited}/F_{normal}$

> **정답**:
> $$\frac{AUC_{\text{inhibited}}}{AUC_{\text{normal}}} = \frac{F_{\text{inhibited}}}{F_{\text{normal}}} \cdot \frac{1}{\dfrac{f_m}{1 + Cu_I/K_I} + (1 - f_m)}$$
>
> **변수 의미**:
> - **AUC ratio**: Inhibitor 동반 시 substrate AUC가 정상 대비 몇 배인지. FDA DDI Guidance에서 ≥5× = "strong inhibitor", 2–5× = moderate, 1.25–2× = weak.
> - **$f_m$**: 정상 상태에서 inhibited pathway가 substrate 총 clearance에서 차지하는 분율. fm→1일 때 inhibition 효과 dramatic; fm<0.5에서 영향 marginal.
> - **$Cu_I/K_I$**: 임상 시 unbound inhibitor concentration 대비 inhibition constant 비. *In vitro* $K_I$가 작아도 임상 $Cu_I$가 작으면 비율 작음 → in vivo inhibition 약함.
> - **$F_{inhibited}/F_{normal}$**: Inhibitor가 *gut wall first-pass*에 영향 시 1보다 큼 (oral DDI > IV DDI 원인).
>
> **MBI 변형 (Eq.17-14)**: $Cu_I/K_I$가 $k_{inact} \cdot Cu_I / (K_I \cdot k_E)$로 치환 — $k_{inact}/k_E$가 *modifier*.
>
> **다음 깊이 질문**: $Cu_I$를 in vivo 직접 측정 어렵다. 어떤 surrogate를 NDA submission에서 사용?

#### Q17 [적용, ★★]
Theophylline–Enoxacin DDI (Fig.17-6) 데이터: 정상 t½=8.8h, enoxacin 동반 t½=22h. Theophylline은 demethylation·ring oxidation·renal excretion 등 multiple pathways. Enoxacin이 모든 CYP pathway full inhibit한다고 가정 시 fm을 추정하라. Eq.17-10 사용.

> **정답**:
> Eq.17-5: $t_{1/2,inh} / t_{1/2,normal} = CL_{normal} / CL_{inh}$ → $22/8.8 = 2.5$ → $CL_{inh} / CL_{normal} = 0.4$.
>
> Eq.17-10: $0.4 = fm/(1+Cu_I/K_I) + (1-fm)$.
>
> Full inhibition 가정 ($Cu_I/K_I \to \infty$, 분수 항 → 0):
> $$0.4 = 0 + (1 - fm)$$
> $$\boxed{fm = 0.6}$$
>
> Tozer p.549에서 ~0.67로 명시되며, 본 계산이 일치 (CL ratio 측정 정확도 차이).
>
> **임상 함의**:
> - Theophylline 60% CYP-mediated → strong CYP1A2 inhibitor (e.g., fluvoxamine) 동반 시 dose 감량 필수
> - 40%는 다른 경로 (renal·다른 CYP) — 이 부분은 inhibitor 무관 보존
> - Enoxacin은 Table 17-5에서 moderate (CYP1A2) — 본 fm 추정으로 임상 dose 조정 정량화 가능
>
> **다음 깊이 질문**: 만약 동일 환자에 ciprofloxacin (또 다른 CYP1A2 inhibitor) 추가 동반 시 cumulative inhibition 효과는 Eq.17-10로 어떻게 modeling?

#### Q18 [적용, ★★]
환자 A: CYP2C19 EM phenotype, omeprazole 20 mg/day 안정. CYP2C19 fm = 0.85 (omeprazole). Clarithromycin 500 mg q12h 추가. Clarithromycin은 CYP3A4 strong MBI (Eq.17-14 modifier ≈ 11). Omeprazole에서 CYP3A4 fraction (nonpolymorphic) fm_NP = 0.10. EM에서 omeprazole AUC ratio 예측. PM phenotype 환자에서는?

> **정답**:
> **EM에서 (Eq.17-14, MBI form 적용)**:
> - CYP3A4 inhibition (modifier=11) 적용
> - $CL_{inh}/CL_{normal} = fm_{NP}/(1+11) + (1-fm_{NP}) = 0.10/12 + 0.90 = 0.908$
> - AUC ratio = $1/0.908 \approx$ **1.10** (10% 증가, 임상 의의 미미)
>
> **PM에서 (Eq.17-18 적용)**:
> - $fm_{POLY}$ = 0.85, $fm_{NP}$ = 0.10
> - Maximum exposure ratio = $1/(1 - 0.85 - 0.10) = 1/0.05 =$ **20×**
>
> **임상 함의**:
> - EM 환자: clarithromycin 동반 무시할 만한 영향 (CYP3A4가 omeprazole에서 minor pathway)
> - PM 환자: 20× exposure → *dramatic toxicity 위험* → clarithromycin 동반 시 omeprazole 중단 또는 H2 blocker로 전환
>
> **Fig.17-15 검증**: omeprazole-clarithromycin observed max ratio = ~33 (실제 fm_POLY ≈ 0.92로 계산하면 더 높음)
>
> **임상 의사결정**: PM phenotype에서 같은 약물 조합이 *order of magnitude* 다른 위험. CPIC guideline의 mechanism 기반.
>
> **다음 깊이 질문**: 본 환자가 한국인 (CYP2C19 PM 빈도 ~15%, 백인 ~3%)이라면 NDA labeling에서 어떤 추가 권고?

#### Q19 [적용, ★]
Atorvastatin–Rifampin (Fig.17-19) 데이터: single oral atorvastatin + IV rifampin 단일 dose. AUC 7×↑, t½ 8h→3h, Vd/F 17×↓. 분석가 결론 "rifampin이 CYP3A4 inhibit". 동의? Mechanism 진단.

> **정답**:
> **결론**: 동의 *불가*. Rifampin은 잘 알려진 CYP3A4 *inducer*. *In vitro* CYP3A4 inhibition은 임상 농도보다 훨씬 높은 농도에서만 발생.
>
> **실제 mechanism (Tozer p.566)**: **OATP1B1 inhibition** (hepatic uptake transporter).
>
> **추론 절차**:
> 1. CYP3A4 inhibition 가정 시 AUC↑ 예상하지만 t½↑도 예상 → 그러나 실제 t½ *감소*
> 2. AUC↑ + t½↓ + Vd↓ 동시 = *Vd 감소가 dominant*. CL/V 비율에서 V 감소가 CL 감소보다 큼
> 3. Vd 감소 mechanism: hepatic uptake 차단 → atorvastatin이 liver 진입 못 함 → tissue distribution 감소
> 4. CL 감소 mechanism: hepatic 진입 차단 → rate-limiting step이 metabolism→uptake로 이동
> 5. 따라서 OATP1B1 (atorvastatin hepatic uptake transporter) inhibition이 rifampin acute mechanism
>
> **Multiple-dose 만성 rifampin과 paradox**: 만성 rifampin은 CYP3A4 induction dominant → atorvastatin AUC *감소*. *시간/route별 mechanism 분기*.
>
> **NDA 함의**: Rifampin 단일·만성·IV·oral 각각 *질적으로 다른 DDI mechanism*. Section 12.3에서 4 시나리오 separate prediction 필요.
>
> **다음 깊이 질문**: Rosuvastatin–Cyclosporine (Fig.17-11)도 OATP1B1 inhibition. 두 사례 (atorvastatin vs rosuvastatin) 임상 함의 차이?

#### Q20 [Boss Dilemma — Socratic Dilemma 최종형, ★★] **NDA DDI Label Strategy**

**시나리오**: 당신은 신약 Y의 NDA 책임자. Y의 PK·DDI 데이터:

**Y 본인 PK**:
- Oral F = 30% (gut wall + hepatic first-pass)
- 주 metabolic pathway: CYP3A4 (fm_3A = 0.85), minor: CYP2D6 (fm_2D6 = 0.10)
- $V_d$ = 80 L (large), $f_u$ = 0.05 (highly bound)
- $t_{1/2}$ = 12 hr

**Phase 1 DDI substudies**:
1. **Y + Itraconazole** (CYP3A4 strong reversible inhibitor): AUC ratio = 6.2× (oral)
2. **Y + Clarithromycin** (CYP3A4 strong MBI): AUC ratio = 5.5× (oral)
3. **Y + Rifampin chronic** (CYP3A4 strong inducer): AUC ratio = 0.15× (oral, 85% 감소)
4. **Y + Quinidine** (CYP2D6 strong inhibitor): AUC ratio = 1.15× (임상 의의 미미)
5. **Y + Diltiazem oral** (CYP3A4 moderate MBI): AUC ratio = 3.1× (oral); IV diltiazem: 1.4×

**Genotype data**: Y target population에서 CYP3A4 functional polymorphism 보고 없음 (CYP2D6 PM ~10%).

**규제 환경**: FDA가 NDA 검토 시 다음 4개 핵심 분류 요구 — (a) Strong inhibitor 동반 권고, (b) Moderate inhibitor 권고, (c) Inducer 권고, (d) Polymorphism 권고.

**Boss Dilemma 질문**:
NDA Section 12.3 Drug Interactions에서 *어떤 dose 조정 권고를* 어떤 mechanism 근거로 제시하겠는가? 다음 4개 옵션의 trade-off를 평가하라:

**Option A — 가장 엄격한 보수적 권고**:
"Y는 CYP3A4 inhibitor 동반 contraindicated, inducer 동반 contraindicated."
- 장점: 안전성 maximally 보장, deficiency letter 위험 적음
- 단점: 임상 사용 범위 *심각하게 제한*; 시장성 손실; 환자 alternative 부족

**Option B — Inhibitor strength 별 stratified 권고**:
"Strong inhibitor: dose 75% 감량 또는 alternative; Moderate: 50% 감량; Weak: dose 그대로 monitoring."
- 장점: 정량 framework; 임상 적용 가능
- 단점: MBI vs reversible 구별 누락 → MBI inhibitor 철수 후 회복 시점 권고 부족

**Option C — Mechanism 기반 detailed 권고**:
"Strong reversible (e.g., itraconazole): dose 75% 감량; Strong MBI (e.g., clarithromycin): dose 75% 감량 + 2주 wash-out; Inducer: dose 적정 또는 alternative; Route effect (oral vs IV): oral inhibitor 동반 시 추가 25% 감량."
- 장점: Mechanism precision; Stage 3 T4-EXT/T6/T8/T9 framework 직접 외화
- 단점: Label complexity 증가; 임상의 implementation difficulty

**Option D — Bayesian dose individualization**:
"각 환자별 inhibitor 농도 + Y target concentration 측정 + Bayesian forecasting algorithm으로 dose 개별화. PopPK model 동봉."
- 장점: Maximally precise; 환자별 최적
- 단점: Implementation 인프라 필요; FDA가 standard label 형식 요구

**당신의 NDA 권고와 trade-off 논리를 작성하라.**

> **정답 (수석 NDA 전략의 통합 Trade-off 논리)**:
>
> **결정**: **Option C 기본 + Option B simple summary table + Option D supplementary**.
>
> **이유 분석**:
>
> **(1) Mechanism 정확성이 후속 확장의 기반**:
> - 단순 inhibitor strength stratification (Option B)은 MBI vs reversible 구별 누락 → 임상에서 *MBI inhibitor 철수 후 2주 wash-out* 미반영 → toxicity 사례
> - Mechanism 기반 (Option C)은 본 Stage 3 framework (T4-EXT, T6, T7, T8, T9)의 직접 외화. 학술적으로 defensible
>
> **(2) Label complexity는 두 layer로 해결**:
> - Section 12.3 main: Option C detailed mechanism
> - Table for clinicians (Option B simple): Strong/Moderate/Weak inhibitor stratification (Table 17-5/17-6 형식)
> - 둘 다 제공 → 임상의가 simple table 사용, depth 필요 시 mechanism section
>
> **(3) Polymorphism 권고**:
> - CYP2D6 PM ~10%, fm_2D6 = 0.10: Eq.17-18 max ratio = $1/(1-0.10-0.85) = 1/0.05 = 20×$ — *PM에서 CYP3A4 strong inhibitor 동반 시 20× exposure*
> - 이 시나리오를 Option C에 명시: "Patients with CYP2D6 poor metabolizer phenotype + concurrent strong CYP3A4 inhibitor: contraindicated unless TDM available"
>
> **(4) Route effect 권고**:
> - Diltiazem oral 3.1× vs IV 1.4× (Stage 3 T9, Table 17-7 mechanism)
> - 임상 의사결정: Y는 oral인 경우가 많으므로 oral inhibitor 동반 시 *추가 dose 감량*
>
> **(5) Bayesian individualization (Option D)**:
> - FDA standard label 형식 외 → main label에는 부적합
> - 그러나 NDA submission supplementary로 PopPK model + simulation 동봉 → reviewer가 mechanism understanding 평가
> - Post-marketing TDM service 권고 (Y가 narrow therapeutic index인 경우)
>
> **NDA Section 12.3 권고 sequence (final draft)**:
>
> 1. **Strong reversible CYP3A4 inhibitors (itraconazole, ketoconazole, ritonavir, telithromycin)**: Dose **75% 감량** (예: 정상 100 mg/day → 25 mg/day). Inhibitor 중단 후 즉시 정상 dose 복귀 가능.
>
> 2. **Strong MBI CYP3A4 inhibitors (clarithromycin, ritonavir)**: Dose **75% 감량**. Inhibitor 중단 후 **2주 동안** 감량 dose 유지 (CYP3A4 enzyme recovery time, Eq.17-13/14 mechanism). 그 이후 정상 dose 복귀.
>
> 3. **Moderate CYP3A4 inhibitors (diltiazem, erythromycin, fluconazole, verapamil)**:
>    - Oral co-administration: dose **50% 감량**
>    - IV co-administration: dose **25% 감량** (route effect, Stage 3 T9 mechanism)
>
> 4. **Strong CYP3A4 inducers (rifampin, carbamazepine, phenobarbital, St. John's wort)**:
>    - Dose **2× 증량 시도** OR alternative
>    - Inducer 시작 후 **3–4주** 후 plateau 도달까지 *점진적 증량* (Eq.17-15 framework, phenobarbital-dicumarol Fig.17-17 mechanism)
>    - Inducer 중단 후 **3–4주 동안 점진적 dose 감량** (역방향 동일 시상수)
>
> 5. **CYP2D6 poor metabolizer phenotype + concurrent strong CYP3A4 inhibitor**:
>    - **Contraindicated** unless therapeutic drug monitoring (TDM) available (Eq.17-18 max ratio = 20×)
>    - 한국·아시아 인구 PM 빈도 ~15% — 추가 주의
>
> 6. **PD interactions (Stage 3 T10 framework)**:
>    - 동일 receptor agonist 동반: Emax 천장 효과; 추가 효과 미미; combination 비합리
>    - 동일 receptor antagonist 동반: 효과 무 → alternative
>
> **Supplementary (Section 12.3 외)**:
> - PopPK model 동봉 (Bayesian forecasting compatible)
> - Post-marketing surveillance plan: TDM-supported dose adjustment in high-risk subgroups
>
> **Trade-off 요약**:
> - 상기 detailed 권고는 *학술적 defensibility + 임상 implementability* 균형
> - Single mechanism framework 대신 multi-mechanism integrated → reviewer가 "scientific rigor" 평가
> - Label complexity는 simple summary table 동봉으로 보완
> - Bayesian individualization은 main label 외 supplementary로 → flexibility 보유
>
> **Stage 3 통합 통찰 (수석 모델러)**:
> - Stage 1 mechanism canonical (M1–M9) → Stage 2 임상 정량 (M-EXT + T1–T4) → Stage 3 DDI framework (T4-EXT + T5–T10) → NDA labeling
> - 각 stage가 *전 단계 mechanism의 외화*. NDA section 12.3 권고는 *수식의 임상 언어 번역*.
> - Reviewer가 mechanism precision 평가 시 Eq.17-11/17-13/17-14/17-15/17-18 *모두 인용 가능한* draft가 strong NDA.
> - 본 Boss Dilemma의 답이 Session 08의 mastery 표시.
>
> **다음 깊이 질문 (Session 09 forward)**:
> Y의 active metabolite도 CYP3A4-cleared이고 활성. Active metabolite의 DDI는 본 Y framework에 어떻게 통합? (Tozer Ch.18 *Metabolites and Drug Response* — Session 09 영역)

---

## §8. Meta-Frame & Big Picture (3-Stage 통합)

<!-- RECAP -->

### A. Positioning — Session 08의 28-session 아키텍처 위치

**선행 (Session 01–07)** — 본 Session이 *전제로 사용하는 mechanism*:
- Session 01–04: Linear PK foundation (Vd, CL, t½, AUC, compartment models)
- Session 05–06: NONMEM 코딩 conventions (ADVAN1–13, $DES, $PK)
- Session 07: ODE-based modeling (parent-metabolite, parallel absorption)

**현재 (Session 08)** — 본 통합본의 3-stage 구조:
- **Stage 1 (Gabrielsson)**: 비선형 PK *분류 체계* + DDI PD mechanism
- **Stage 2 (Tozer Ch.16)**: 임상 정량 anchor + 추가 mechanism (T1–T4)
- **Stage 3 (Tozer Ch.17)**: DDI 정량 prediction framework + 규제 언어

**바로 다음 (Session 09–10)**:
- Session 09: **Tozer Ch.18 Metabolites and Drug Response** — active metabolite의 PK·PD interaction (본 T6 carryover)
- Session 10: Pharmacogenetics integration — CPIC guidelines을 본 T7 (Eq.17-18) framework로 외화

**고급 module로의 출구 (Session 11+)**:
- PopPK with nonlinear IIV/RUV (NONMEM mixture model)
- PBPK whole-body model (장기별 mechanism 통합)
- TMDD full quasi-equilibrium (단백 의약품 PK, 본 T3 확장)
- FDA DDI Guidance 직접 적용 (본 T6/T7/T8 directly applicable)
- IND/NDA Section 12.3 작성 실습 (Q20 Boss Dilemma 직접 응용)

### B. Dependencies — Session 08을 대충 넘겼을 때의 실패 모드

**실패 모드 1**: 비선형 PK 약물에 선형 모델 적용
- Phenytoin TDM에서 Vmax/Km 추정 실패 → Css predict 못 함
- 환자 dose 조정 시 비대칭 toxicity (M2-EXT 67% dose↑ → 9× Css)

**실패 모드 2**: Time-dependent kinetics를 IIV 변동성으로 오해
- Carbamazepine multiple-dose data를 single-dose ETA(VC)로 fit
- η-shrinkage 큼 → 진단 missed → 효소 turnover mechanism 안 보임

**실패 모드 3**: NDA 시 single dose IV linear만 보고 multifaceted DDI missed
- Phase 3 이후 reviewer "multiple mechanism 식별 안 됨" → Deficiency Letter
- Q15 Boss Dilemma 시나리오의 임상 발현

**실패 모드 4 (Stage 2 추가)**: Phenytoin TDM에서 환자 albumin 정상이고 total C 8 mg/L → dose 안정 추정 → 5%/yr enzyme decline의 hepatic disease 진행 missed
- M2-EXT의 Vm-R₀ 분모 발산을 모르면 매년 같은 dose가 점점 위험
- 매 1년 ALT·albumin·trough 동시 추적 + Vm 재산출 권고

**실패 모드 5 (Stage 2 추가)**: Bosentan/mAb를 일반 단백 결합 약물처럼 modeling (M5 open system 결론 적용)
- Dose escalation 시 V_d 변화를 IIV로 보고 ω²만 키워 fit
- 실제 mechanism = dose-dependent V_d (T3 TMDD)
- ETA shrinkage 큼 → 진단 missed

**실패 모드 6 (Stage 3 추가) — Inhibitor vs Inducer 혼동 (CP8 Critical Blow)**
- Rifampin acute IV (OATP1B1 inhibitor) vs chronic oral (CYP3A4 inducer) 구별 실패
- 같은 약물에 두 mechanism이 다른 시간/route에서 dominant
- 임상에서 dose 조정이 *반대 방향*으로 잘못됨 → toxicity 또는 치료 실패

**실패 모드 7 (Stage 3 추가) — Phenotype 무시 inhibitor 처방**:
- CYP2C19 PM 환자 omeprazole에 clarithromycin 추가 → Eq.17-18 max ratio = 20–33×
- 표준 dose 조정 권고만 따라서 dose 50% 감량 → 여전히 10× exposure → toxicity
- CPIC guideline 준수 → genotype-guided dose adjustment

**실패 모드 8 (Stage 3 추가) — Multifaceted DDI 단일 mechanism framework 적용**:
- Atorvastatin–rifampin acute IV에 CYP3A4 inhibition framework 적용 → AUC ratio 1.5× prediction
- 실제 OATP1B1 inhibition mechanism이 dominant → AUC 7×
- NDA에서 transporter pathway 누락 → reviewer deficiency

**실패 모드 9 (Stage 3 추가) — PD vs PK DDI 진단 실패**:
- Cu unchanged + 효과 변화 시 PD DDI인데 PK mechanism 가정
- Diphenhydramine + alcohol mutual sedation을 metabolic interaction으로 잘못 modeling
- 실제 mechanism (CNS receptor convergent) missed → 임상 dose 조정 무효

### C. Professional Moat — Session 08 통합 외화

**Stage 1 Moat (Gabrielsson mechanism canonical)**:
1. NONMEM을 실행하고 GOF 플롯을 생성하는 주니어 모델러와, 2구획 모델을 데이터에 적합시키는 AI가 이미 존재한다. 그러나 Vmax/Km 식을 보고 *왜 이 형태인지* — substrate가 enzyme active site와 reversible binding을 하며 mass action equilibrium을 따르기 때문 — 를 *수학적·생리학적 mechanism level*로 통합 설명할 수 있는 연구자는 둘 다 복제 못 한다.
2. PK22 autoinduction의 turnover ODE를 보고 *carbamazepine·rifampin·atorvastatin acute*을 *동일 mechanism의 다른 표현*으로 즉시 mapping할 수 있는 직관.
3. M5 open vs closed system 결론을 *임상 단백 결합 약물 dose 조정*에 *직접 적용*할 수 있는 능력.
4. M8/M9 PD interaction이 PK domain의 M2/T6와 *동일 mathematical structure*임을 인지하는 통합 시각.

**Stage 2 Moat (임상 패턴 인식)**:
1. Phenytoin 환자의 dose 67% 증량이 9배 농도를 만드는 mechanism을 분모 (Vm−R₀)의 발산으로 *30초 안에* explanation. 환자에게 도식 (Fig.16-9의 점근선)으로 clinical safety education.
2. Multiple dose oral t½이 single dose IV t½과 다른 약물에서 즉시 MBI suspect. Probe substrate study 권고. AI/ML 모델은 데이터 mining만 하고 mechanism inference 못 함.
3. Bosentan, monoclonal antibody의 dose-dependent V_d를 TMDD 시그너처로 인식. PopPK 모델에 dose covariate on V_d를 *mechanism 기반*으로 부여 (단순 statistical fit 아님).
4. 신부전 환자에서 dicloxacillin (saturable secretion) vs ascorbic acid (saturable reabsorption) dose 조정의 *opposite direction*을 mechanism으로 derive. GFR 비례 dose adjustment의 *과소·과대 위험*을 약물별로 설명.
5. Salicylic acid 같은 "opposing nonlinearities" 약물에서 total CL 일정해 보이는 것을 saturable binding (fu↑) + saturable metabolism (CLu↓)의 fortuitous 상쇄로 인식. Unbound 농도가 dosing rate에 *비대칭* 증가하는 것을 따로 측정 권고.
6. NDA reviewer 관점에서 multiple nonlinear mechanism이 동시 작동하는 약물의 *진단 우선순위*를 IV-oral cross-over → probe substrate → target occupancy 순으로 design (Q15 Boss Dilemma 결론).

**Stage 3 Moat (DDI 정량 framework 외화 — 본 통합본의 정점)**:
1. **Eq.17-11 (FDA DDI Guidance 핵심식)을 메모리로 즉시 재현하고**, 임의 약물 쌍에 fm·Cu_I/K_I·F 변화를 substitute하여 AUC ratio prediction 30초 내 산출. 이는 *NDA Section 12.3 작성·FDA reviewer 응답 직접 capability*.
2. **Reversible vs MBI inhibitor 구별의 mathematical signature** ($Cu_I/K_I$ vs $k_{inact} \cdot Cu_I / (K_I \cdot k_E)$)를 mechanism으로 설명하고, clarithromycin 11× CL 감소가 단순 reversible 가정 1.025×의 *280× 증폭*임을 즉시 해석.
3. **Phenotype × Inhibitor 위험 정량화**: CYP2D6 PM 환자에 strong inhibitor 동반 시 Eq.17-18을 즉시 적용하여 max exposure ratio 산출. 한국인 PM 빈도까지 고려한 ethnicity-adjusted dose recommendation.
4. **Inhibition vs Induction 시상수 분리 진단** (CP8 Critical Blow): Same drug (rifampin)의 acute vs chronic, IV vs oral mechanism 분기를 즉시 인지. NDA section 12.3에서 *4 시나리오 separate prediction* 작성.
5. **Multifaceted DDI 분리 진단 능력**: Total CL/F/Vd/CL_R 변화에서 각 mechanism (CYP/transporter/displacement/binding)의 partial contribution 분리 추론. Atorvastatin–rifampin에서 OATP1B1 mechanism을 30초 내 진단.
6. **PD vs PK DDI 진단의 단일 question** ("Cu가 sustained 변화하는가?")으로 임상 DDI를 즉시 분류. Stage 1 M5 open system 결론을 임상 의사결정에 직결.
7. **NDA Boss Dilemma (Q20) 응답 capability**: Mechanism precision (Stage 3 T4-EXT/T6/T7/T8/T9) + Implementability (simple table) + Bayesian supplementary (PopPK model)의 *3-layer label* draft. 단순 dose adjustment table 수준의 NDA submission과의 *category 차이*.

**핵심 통합 통찰 (Session 08 종결)**:

> **수석 모델러는 mechanism 분류 → 임상 정량 → 규제 언어를 *단일 thread*로 연결한다.**
>
> Stage 1의 mass action equation이 Stage 2의 phenytoin 9× Css를 거쳐 Stage 3의 FDA DDI Guidance Eq.17-11로 *수학적으로 동일한 식*이며, 이 동등성을 인지하는 능력이 NDA reviewer level의 mastery 표시이다. 본 Session 08의 모든 카드는 이 단일 thread의 다른 표현이다.
>
> *"Mechanism이 정확하면 dose가 안전하다"* — 본 명제가 28-session protocol에서 본 Session이 차지하는 위치이다.

---

## ✦ STEP 1 완료 — 3-Stage 확장통합 최종

다음이 준비되었습니다:

- **§1 세션 헤더 & 로드맵 (3-Stage 통합)**
  - 3-Stage 통합 Big Idea 단일 문장
  - Stage별 source 파일 + 페이지 명시
  - 3-Stage 통합 지식 그래프 (Stage 1 → 2 → 3 dependency 도식)

- **§2 개념 해부 카드 (총 21개)**
  - **Stage 1**: M1–M9 (구조 anchor 요약, 정본은 별도 산출물)
  - **Stage 2**: M2-EXT, M3-EXT, M5-EXT, T1, T2, T3, T4 (7 카드)
  - **Stage 3**: T4-EXT, T5, T6, T7, T8, T9, T10 (7 카드)
  - **Apex Concepts**: M2 (Stage 1), T4 (Stage 2), **T6** (Stage 3 = 통합 Apex)
  - 모든 카드에 Master's Lens Big Idea + Cross-references + NONMEM + Zettelkasten Atom

- **§5 혼동 쌍 해부 (총 9개)**
  - Stage 1: CP1–CP4 (구조 요약)
  - Stage 2: CP5–CP6 (Stage 2 Critical Blow = CP5)
  - Stage 3: CP7–CP9 (**Stage 3 Critical Blow = CP8 Inhibition vs Induction**)
  - 모든 혼동쌍에 구조적 기억 고리 (Stage 3 Critical Blow는 NDA labeling 함의 명시)

- **§7 자기 테스트 (총 20 questions)**
  - Stage 1: Q1–Q10 (구조 요약)
  - Stage 2: Q11–Q15 (정본 통합)
  - Stage 3: Q16–Q20 (신규 — Eq.17-11 회상, theophylline-enoxacin fm 추정, PM × inhibition 정량, atorvastatin-rifampin mechanism, **Q20 NDA DDI Label Boss Dilemma 최종형**)

- **§8 메타프레임 & 빅 픽처 (3-Stage 통합)**
  - Positioning: Session 08의 28-session 위치
  - Dependencies: 9개 실패 모드 (Stage 1: 3, Stage 2: 3, Stage 3: 3)
  - **Professional Moat — 3-Stage 통합 외화 (총 17개 capability item)**

### 감지된 소스 유형 통합

- **혼합 multi-source**:
  - Vol I 데이터 이론 (Gabrielsson 5e) — mechanism canonical
  - Vol I 임상 (Rowland & Tozer 5e Ch.16) — 임상 정량 anchor
  - Vol I 임상 + 규제 (Rowland & Tozer 5e Ch.17) — DDI prediction framework

### Data Anchoring 소스 (verbatim 정량 anchor)

**Stage 1 (Gabrielsson)**:
- PK17: linear vs MM 모델 판별, WRSS/AIC 비교 (Table 17.1)
- PK18: ethanol Vmax≈10g/hr, Km≈100mg/L, 2구획 MM 모델 (Eq 18:1–18:13, Table 18.1)
- PK22: autoinduction $a=0.041$, $k_{out}=0.023$ h⁻¹, kout/E0 (Table 22.2)

**Stage 2 (Tozer Ch.16)**:
- Phenytoin: Vm≈500 mg/day, Km≈0.4 mg/L (fu=0.1, Km'=4); 67% dose↑→9× Css
- Alcohol: Vm≈10 g/hr, Km≈100 mg/L, Vd≈42 L/70 kg
- Ascorbic acid: 75 mg/day → 9 mg/L vs 10,000 mg/day → 19 mg/L
- Nicardipine F: 19→22→28→36% (10–40 mg q8h)
- Dicloxacillin: 1g CLR=104, 2g CLR=63 mL/min; fu=0.04
- Bosentan Vss: 10 mg→0.67, 750 mg→0.16 L/kg
- Trandolaprilat: accumulation ratio 1.49; fu 0.05→0.20
- Carbamazepine autoinduction: turnover ~5 days
- Clarithromycin MBI: kinact=0.07/min, kE≈0.23/day

**Stage 3 (Tozer Ch.17)**:
- Theophylline–Enoxacin: t½ 8.8→22h; Css 4→9 mg/L; CL_inh/CL_normal=0.44; fm=0.67
- Desipramine–Quinidine: fm(CYP2D6)=0.75; CL 4×↓
- Desipramine–Fluoxetine (Table 17-11): AUC 284→2110 µg·hr/L; t½ 16.1→63.8h; CL/F 289→27.1 L/hr
- Phenytoin–Valproate (Fig.17-3): N=25/11/9 patients; total↓ unbound unchanged
- Warfarin–Phenylbutazone (Fig.17-18): fu=0.005; CL=0.1 L/hr; phenobarbital plateau 100 mg/L
- Digoxin–Quinidine (Table 17-8): CL 140→72 mL/min; CL_R 101→51; Vd 500→240 L; F 0.75→0.85
- Rosuvastatin–Cyclosporine (Fig.17-11): Cmax 11×, AUC 7×
- Clarithromycin MBI 정량: kinact/kE=438; Cu_I/K_I=0.025 → 11× CL감소 (vs reversible 1.025×)
- Diltiazem–Lovastatin (Table 17-7): AUC ratio 1.27 IV vs 3.57 oral
- Fluconazole–Midazolam (Fig.17-10): oral 5.6×, IV 2×; F 24→63%; F_H 0.42→0.72; F_G 0.57→0.88
- Atorvastatin–Rifampin (Fig.17-19): Cmax 10×, AUC 7×; t½ 8→3h; CL/F 9× 감소
- Phenobarbital–Dicumarol (Fig.17-17): 3–4 weeks plateau; phenobarbital t½=4d
- Omeprazole–Clarithromycin (Fig.17-15): max ratio ~33 (PM phenotype); fm_POLY≈0.92

### 핵심 Cross-references (3-Stage 정합성 표시)

- M2 → M2-EXT → T6 (capacity-limited mechanism의 임상·DDI 외화)
- M3 → M3-EXT → T4 → T4-EXT → T8 (turnover ODE의 4가지 분기 — Apex 학습 path)
- M5 → M5-EXT → T3 → T5 (단백 결합의 mechanism → prototype → TMDD → DDI 진단)
- M8/M9 → T6 → T10 (PD/PK 경쟁의 mathematical equivalence 통합)
- T1 → T9 (renal transport mechanism의 multifaceted 임상 발현)
- T2 → T9 (first-pass mechanism의 route effect DDI 발현)

### 통합 Apex Concept (Session 08 종결 통찰)

**Mass action competition이 PK 효소 (M2/T6) · PD 수용체 (M8/T10) · 단백 결합 (M5/T3/T5) · 운반체 (T1/T9) 모든 도메인에서 동일 mathematical form ($1 + I/K_I$ in denominator)으로 표면화**한다. 본 통합 통찰이 Session 08 mastery의 단일 표시이며, NDA reviewer level의 mechanism precision의 출처이다.

---

*Step 1 Draft v0 — Session 08 — 3-Stage Final Integrated*
*Source: Gabrielsson 5e (Stage 1) + Rowland & Tozer 5e Ch.16 (Stage 2) + Ch.17 (Stage 3)*
*PIPET Lab · Pharmacometrics PhD Program*
*Master's Lens v2.0 + 3-Stage 확장통합 (Mechanism canonical → 임상 정량 → DDI 정량 framework → 규제 언어)*
*워크플로우 v3.3.2 Phase 1 산출물 — Phase 2 (Source Fidelity Audit) 입력 ready*

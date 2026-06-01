# 01_step1_draft_v0.md

> **Phase 1 / Step 4 (최종 통합본) — Gabrielsson + Tozer Ch.5 + Tozer Ch.20 + Tozer App.D·E**
>
> **Sources**:
> - Gabrielsson J & Weiner D, *Pharmacokinetic and Pharmacodynamic Data Analysis*, 5th ed. (Swedish Pharmaceutical Press, 2010). §2.3 (pp.48–56) · §2.5 (pp.77–94) · PK5 (pp.494–499).
> - Rowland M & Tozer TN, *Clinical Pharmacokinetics and Pharmacodynamics: Concepts and Applications*, 5th ed. (Wolters Kluwer, 2011). Ch.5 — Elimination (pp.119–168) · Ch.20 — Metabolites and Drug Response (pp.657–686) · **App.D — Plasma-to-Blood Concentration Ratio (pp.775–776)** · **App.E — Well-Stirred Model of Hepatic Clearance (pp.777–780)**.
>
> **Status**:
> - ✅ Step 1 (Gabrielsson) 완료
> - ✅ Step 2 (Tozer Ch.5) 통합 완료
> - ✅ Step 3 (Tozer Ch.20) 통합 완료
> - ✅ **Step 4 (Tozer App.D + App.E) 통합 완료 — *본 최종 버전***
>
> **Mode 매핑**:
> - Gabrielsson §2.3 = B-Standard · §2.5 (Well-stirred + IVIVE + Route×Extraction) = A-Critical · PK5 = B-Standard
> - Tozer Ch.5 = **A-Critical** · Tozer Ch.20 = **A-Critical** (트리거: fm/CL(m)/V(m) 오류는 parent-metabolite PopPK 구조를 직접 왜곡)
> - **Tozer App.D = B-Standard** (기존 M10 보강용 first-principles; 새 MUST 카드 없음)
> - **Tozer App.E = B-Standard** (기존 M4·M15·M18 보강용 first-principles; 두 교재 well-stirred *cross-validation* 제공; 새 MUST 카드 없음)
>
> **Image rights = None** (모든 Figure는 Phase 4C에서 SVG 자체 제작; 본 phase에서는 FIGURE 마커 미삽입).

---

## 0. Curation Map (Master's Lens)

> **판정 원칙**: "이 개념을 체화하지 않으면 다음 개념의 이해가 구조적으로 무너지는가?"
> Yes → MUST / No, 그러나 풍부함을 더한다 → CONTEXT (가장 가까운 MUST 카드 안에 1–2 문장으로 흡수)

### 0.1 MUST 항목 (체화 필수) — Step 1 + Step 2 + Step 3

| # | 항목 | Source | Mode | 구조적 필요성 |
|---|------|--------|------|---------------|
| **M1** | Clearance의 비례관계 정의 — `dX/dt = Cl·C` (Eq 2:83, 2:180, Eq 5-1) | G+T5 | B | 모든 후속 유도의 출발점. |
| **M2** | ClR · fe · 혈장+소변 simultaneous regression (Eq 2:87, 2:99–101, 2:102, 2:104) | G | B | NONMEM fe 파라미터화 + 신기능 공변량 모델링의 직접 선행. |
| **M3** | ARE plot vs Excretion Rate plot — 사용 조건과 한계 | G | B | 그래픽 진단의 첫 단계. |
| **M4** | Hepatic extraction & Well-stirred 유도 (Eq 2:188–2:195; Eq 5-14, 5-15) | G+T5 | **A** | 간기능 공변량 모델링 수식 기반. |
| **M5** | High vs Low extraction 극한 단순화 — *Tozer 사례 통합* | G+T5 | **A** | 약물 분류와 PopPK 공변량 분기점. |
| **M6** | 투여경로 × 추출비 × fu 의 4사분면 — *Tozer phenytoin/clofibric acid 통합* | G+T5 | **A** | 단백결합 변화의 임상 해석 전체. |
| **M7** | IVIVE의 세 가지 함정 (single-point, MMP, condensation) | G | **A** | AIMS 컨설팅 실무 직결. |
| **M8** | 4가지 간 청소율 모델 비교 (Table 2.9) | G | **A** | PBPK 시뮬레이션 모델 선택. |
| **M9** | PK5 — 통합해 vs ODE 등가성 (Eq 5:1–5:4) | G | B | NONMEM ADVAN1 vs ADVAN6 이론적 근거. |
| **M10** | Plasma vs Blood Clearance & C/Cb 비 (Eq 5-4, 5-5) | T5 | **A** | 추출비 분류는 *blood* 기준만 유효. |
| **M11** | Clearance Additivity (CL = CLR + CLH; Eq 5-9) | T5 | **A** | 신부전 dose 조절 권고의 수식 기반. |
| **M12** | Biliary Excretion & Enterohepatic Cycling (Eq 5-16) | T5 | **A** | EHC는 distribution; biliary obstruction의 t½ 정반대. |
| **M13** | Renal Tubular Reabsorption — urine pH & flow (Eq 5-22, 5-23) | T5 | **A** | Methamphetamine 50배 변동 근거. |
| **M14** | Half-life as Derived (Secondary) Parameter (Eq 5-24, 5-25) | T5 | **A** | t½는 CL과 V에 의존, 그 역이 아니다. |
| **M15** | Extended Clearance & Permeability/Transporter (Eq 5-35, 5-36) | T5 | **A** | OATP1B1·P-gp 시대 IVIVE. |
| **M16** | **Parent–Metabolite Mass Balance & AUC Ratio** (Eq 20-1, 20-4, 20-5, 20-6, 20-7) — *Tozer Ch.20 신규* | T20 | **A** | 모자식 시스템 *수식적 골격*. AUC 비로 fm·CL·V 분리 추론하는 모든 후속 분석의 출발점. |
| **M17** | **Rate-Limiting Step in Metabolite Disposition** (formation vs elimination rate-limited) — *Tozer Ch.20 신규* | T20 | **A** | 대사체 t½가 parent의 것인지 자기 것인지 — 단일 판단이 PopPK metabolite V(m) 식별성과 신부전 외삽 좌우. |
| **M18** | **First-Pass Impact on Metabolite Disposition** (oral parent = parent + metabolite cocktail) — *Tozer Ch.20 신규* | T20 | **A** | 고추출 약물 oral 시 대사체 농도 해석; AUC(m) 경로 의존성으로 hepatic vs extrahepatic 부위 진단. |
| **M19** | **Steady-State Metabolite Concentration & Multiple-Dose Prediction** (Eq 20-12, 20-15) — *Tozer Ch.20 신규* | T20 | **A** | 만성 투약 metabolite noxic accumulation의 정량 예측; superposition으로 single-dose AUC만으로 multi-dose 평형 예측 가능. |
| **M20** | **신기능 저하 시 대사체 축적 + Interconversion — Dose Adjustment 시나리오** — *Tozer Ch.20 신규* | T20 | **A** | §1 dilemma의 *완성형*. fe만 보고 dose 결정하면 active metabolite 13배 축적 — procainamide·morphine·clofibric acid의 임상 함정. |

(G = Gabrielsson; T5 = Tozer Ch.5; T20 = Tozer Ch.20; G+T5 = 동일 개념 다른 깊이)

### 0.2 CONTEXT 항목 (전용 카드 없음)

| # | 항목 | Source | 흡수 위치 |
|---|------|--------|-----------|
| C1 | Nephron 해부, GFR 110–130 mL·min⁻¹, 소변 pH 4.5–8 | G+T5 | M2 |
| C2 | Eq 2:107–2:108 (1-cmt + 1st-order absorption + 소변) | G | M9 |
| C3 | Eq 2:115 (urinary data로부터 F 추정) | G | M2 말미 |
| C4 | Inter-species characteristics (Table 2.7) | G | M7 |
| C5 | Distributed/Dispersion model 세부 유도 | G | M8 |
| C6 | 1/K sampling design 원칙 | G | M9 말미 |
| C7 | "대사체" — Tozer Ch.20에서 본격 → **Step 3 M16–M20 통합 완료** | G | (해결됨) |
| C8 | Phase I/II 반응 분류 + CYP 분포 (Fig 5-1~5-4) | T5 | M11 |
| C9 | Reference 생리학적 수치 (QH=1.35 L/min, QR=1.1 L/min, GFR=120 mL/min, bile=0.5–0.8 mL/min) | T5 | M4·M11·M12 |
| C10 | Soft drug 개념 (prodrug 반대) | T5 | M11 |
| C11 | Forced diuresis & overdose 적용 | T5 | M13 |
| C12 | Renal metabolism (minor 언급) | T5 | M13 |
| C13 | Pulmonary clearance가 additivity 예외인 이유 | T5 | M11 |
| C14 | OATP1B1, P-gp, MRP2 transporter 위치 | T5 | M15 |
| C15 | **Sequential metabolism (clopidogrel 2-step 활성화)** | T20 | M16 |
| C16 | **Therapeutically important metabolites (Table 20-1)** — codeine→morphine, prednisone→prednisolone 등 | T20 | M16·M20 |
| C17 | **Carbamazepine autoinduction (Fig 20-11)** — 비선형 metabolite 형성 | T20 | M19 |
| C18 | **AUC ratio diagnostics — 4 possibilities** (Eq 20-21~20-24) | T20 | M20 |
| C19 | **Methylprednisolone hemisuccinate (Fig 20-2)** — Case B 사례 (parent rate-limiting) | T20 | M17 |
| **C20** | **App.D mass-balance 5단계 유도 (Eq D-1 ~ D-5)** — plasma volume·blood cell volume·KpBC 분리 | TD | M10 |
| **C21** | **App.D Eq D-6 first-principles**: `C/Cb = 1 / {1 + H[fu·KpBC − 1]}` | TD | M10 |
| **C22** | **App.D Eq D-8 KpBC 역산식** + Study Problem 1 정량 (anemic·nephrotic 비교) | TD | M10 |
| **C23** | **App.E Model I (Eq E-1 ~ E-8) Tozer 대안 유도** — Gabrielsson Eq 2:188-2:195와 *동일 결론, 다른 출발점* (cross-validation) | TE | M4 |
| **C24** | **App.E Model II ρ 항 (Eq E-9 ~ E-13)**: `ρ = Pin·SA / (Pout·SA + CLint)` — intracellular/extracellular unbound 비 | TE | M15 |
| **C25** | **App.E permeability 두 극한 (Eq E-14, E-15)**: ρ → 1 회복 vs Pin << QH에서 `CLb,H = fub·Pin` | TE | M15 |
| **C26** | **App.E oral first-principles (Eq E-19, E-20)**: `AUCpo = Dose / (fub·ρ·CLint)` — *QH 무관* | TE | M18 |

### 0.3 Mode 분기 매핑 (Scope Lock 준수)

| 섹션 | 페이지 | Source | Mode | 처리 카드 |
|------|--------|--------|------|----------|
| §2.3 신장 청소율 | 48–56 | G | B | M2, M3 |
| §2.5.2 Well-stirred | 79–82 | G | A | M4 |
| §2.5.3 Route × extraction × fu | 83–85 | G | A | M6 |
| §2.5.4 IVIVE | 85–89 | G | A | M7 |
| §2.5.5 4-model | 90–94 | G | A | M8 |
| PK5 | 494–499 | G | B | M9 |
| Tozer Ch.5 Processes of Elimination | 120–124 | T5 | A | M11 |
| Tozer Ch.5 Clearance in General | 124–128 | T5 | A | M10, M11 |
| Tozer Ch.5 Hepatic Clearance — Perfusion/Binding | 128–135 | T5 | A | M4·M5·M6 보강 |
| Tozer Ch.5 Hepatic Clearance — Permeability/Transporter | 136–138 | T5 | A | M15 |
| Tozer Ch.5 Biliary & Enterohepatic | 137–138 | T5 | A | M12 |
| Tozer Ch.5 Renal Clearance | 138–148 | T5 | A | M13 + M2 보강 |
| Tozer Ch.5 Half-life Dependence | 148–150 | T5 | A | M14 |
| Tozer Ch.5 Integration Cases | 150–163 | T5 | A | M5·M6·M11 보강 |
| **Tozer Ch.20 Single Dose: Rate-Limiting** | 659–662 | T20 | A | **M16, M17** |
| **Tozer Ch.20 Single Dose: AUC Ratio** | 662–665 | T20 | A | **M16 + M17 사례** |
| **Tozer Ch.20 Hepatic Extraction Impact** | 665–669 | T20 | A | **M18** |
| **Tozer Ch.20 Constant-Rate Infusion** | 669–671 | T20 | A | **M19** |
| **Tozer Ch.20 Multiple-Dose Regimen** | 671–673 | T20 | A | **M19** |
| **Tozer Ch.20 Renal Impairment Variability** | 673–675 | T20 | A | **M20** |
| **Tozer Ch.20 Nonlinear** | 675–676 | T20 | A | M19 (carbamazepine) |
| **Tozer Ch.20 Interconversion** | 676–679 | T20 | A | **M20** |
| **Tozer Ch.20 AUC Diagnostics** | 680–682 | T20 | A | **M20** |
| **Tozer App.D Plasma-to-Blood Mass Balance** | 775 | TD | B | **M10 보강** (Eq D-1 ~ D-6) |
| **Tozer App.D KpBC Determination + Study Problem** | 776 | TD | B | **M10 보강** (Eq D-7, D-8) |
| **Tozer App.E Model I (Rapid Equilibration)** | 777–778 | TE | B | **M4 보강** (Eq E-1 ~ E-8) — *cross-validation* |
| **Tozer App.E Model II (Permeability)** | 778–779 | TE | B | **M15 보강** (Eq E-9 ~ E-15) — *ρ 항* |
| **Tozer App.E Events After Oral Dose** | 779 | TE | B | **M18 보강** (Eq E-16 ~ E-20) |

---

## §1 Why This Chapter Matters (도입)

<!-- MASTER LENS -->
**Big Idea**: 본 챕터를 체화하지 않으면, NONMEM에서 `CL`을 추정하고 `WT`나 `CrCL`을 공변량으로 넣는 그 *가장 일상적인* 작업 한 번이 잘못된 가정 위에서 작동하게 된다. 신부전 환자에 대해 `CL_typ = θ1 · (CrCL/100)^θ2`라는 모델은 *전체* clearance가 신청소율에 비례한다고 암묵적으로 주장한다. fe ≈ 1인 약물(aminoglycoside)에서는 옳지만, fe = 0.35인 약물(PK5의 약물)에서는 65%의 clearance가 신기능과 무관함을 무시 — 신부전 코호트 용량을 5–10% 과소추정.

**Tozer Ch.5가 강조하는 메시지**: 같은 약물의 *plasma* CL(1.3 L/min)과 *blood* CL(0.13 L/min)이 10배 차이날 수 있다 (plasma-to-blood ratio = 0.1인 경우). 이 차이를 무시한 "고추출 약물" 결론이 IVIVE 가장 흔한 오류이며, 임상 함의는 정반대 — **"plasma clearance에서 멈추지 마라; blood clearance까지 가야 분류가 결정된다"**.

**Tozer Ch.20의 함정 — *가장 위험한* 추가 메시지**: §1의 fe = 0.35 약물이 *active metabolite*를 만들고 그것이 *주로 신청소*된다면, 정상 환자에서는 무관하던 metabolite가 anuric 환자에서 **13배 축적** (Tozer p.674 정량 예제). 그 결과 parent drug 농도만 보고 "신부전에서 CL이 절반이니 dose도 절반"이라고 결정하면 — 약리 효과는 metabolite가 더 크게 좌우 — *실제 임상 효과는 7배 과량* 노출. 이게 procainamide·morphine·prednisone에서 임상의가 만나는 위험이며, **fe가 작아도 active metabolite의 fe(m)이 크면 dose 조절은 metabolite 기준으로 해야** 한다. **"parent drug PK만으로 결정된 dose는 active metabolite 약물에서 임상적으로 위험하다."**

**왜 Gabrielsson + Tozer Ch.5 + Tozer Ch.20을 한 묶음으로?**
- **§2.3 (G)**: 신장 청소율 정의 + ARE/Rate plot + simultaneous regression.
- **§2.5 (G)**: 청소율을 간으로 일반화 + 분자 수준 분해 (fu, Q_H, Cl_int).
- **PK5 (G)**: NONMEM 코딩 기준점.
- **Tozer Ch.5 (T5)**: 수치적 reference + 임상 사례 + plasma↔blood 변환 + EHC + 신세관 재흡수 + half-life 파생 의미.
- **Tozer Ch.20 (T20)**: 모자식 PK 수식 골격 + rate-limiting + first-pass의 대사체 영향 + 신부전 metabolite 축적 + interconversion + AUC 비 진단법.

**한 마디로**: §2.3은 "어떻게 측정", §2.5는 "왜 그 크기", PK5는 "어떻게 코드", Tozer Ch.5는 "실제 약물에서", Tozer Ch.20은 "약물 + 대사체의 *합산* 효과로서", **Tozer App.D·E는 "first-principles 차원에서 수식의 *어디서 출발하는지*"**.

**Tozer Appendix D·E의 마지막 메시지** — "한 약물에 대해 *세 양*을 동시에 인지해야 PopPK 분석이 견고하다":
1. **Plasma-blood 변환** (App.D Eq D-6): `C/Cb = 1 / {1 + H[fu·KpBC − 1]}` — KpBC와 fu의 *조합*이 변환을 결정. 단순 "Cb/C = 0.5" 경험치가 아닌 *first-principles 식*.
2. **간 청소율의 well-stirred 골격** (App.E Eq E-1 ~ E-8, Model I): Gabrielsson Eq 2:188-2:195와 *완전히 다른 표기와 변수명*에서 *동일 결론에 수렴* — 두 교재 cross-validation이 well-stirred 모델의 광범위한 수용을 입증.
3. **막투과성 ρ 항** (App.E Eq E-13, Model II): `CLb,H = QH·[fub·ρ·CLint / (QH + fub·ρ·CLint)]` — Tozer Ch.5의 extended clearance (Eq 5-35)와 *동일 결과의 다른 표현*. ρ → 1이면 기본 well-stirred 회복.

임상 함의: Phenytoin (fu = 0.1, KpBC ≈ 0.5, plasma-to-blood ≈ 0.45)을 *plasma CL만으로* 평가하면 — fub ≠ fu 인식 누락 + uremia 시 fu 변동에 따라 *plasma-to-blood 비도 동시 변동* → IVIVE에서 *수배의* 노출 예측 오차. 본 통합 *최종 phase*에서 §1의 fe = 0.35 dilemma는 **세 축**으로 확장:

> **3-Axis Dilemma**: **신청소 (renal) × 대사체 (metabolite) × plasma-blood (App.D·E)** — 본 phase의 §7이 이 세 축이 동시 작용하는 *단일 시나리오*로 재설계됨.

---

## §2 Concept Anatomy Cards

---

### M1. Clearance의 비례관계 정의 — `dX/dt = Cl · C`

<!-- MASTER LENS -->
**Big Idea**: Clearance는 "단위 시간당 약물이 완전히 제거되는 가상의 혈장 부피". *가상의 부피*라는 점이 본질 — 관찰된 제거 속도(`dX/dt`)를 관찰된 농도(`C`)로 나눈 비례상수. 이 추상화 덕분에 약물의 양·농도에 의존하지 않고 한 숫자로 elimination 능력 표현.

#### 정의 (Gabrielsson p.49 Eq 2:83; p.77 Eq 2:180; Tozer p.124 Eq 5-1)

$$V \cdot \frac{dC}{dt} = \frac{dX}{dt} = -Cl \cdot C \quad\Leftrightarrow\quad \text{Rate of elimination} = CL \cdot C$$

#### 핵심 결과 (적분 후, p.49 Eq 2:84–2:86)

$$Cl = \frac{Dose}{AUC_0^\infty}$$

NCA에서 가장 흔한 식. compartment 가정 없이 mass balance만으로 정의.

#### 변형 — Oral (p.78 Eq 2:182–2:183)

$$\frac{Cl}{F} = \frac{D_{po}}{AUC_{po}^\infty}, \quad Cl = F \cdot Cl_o$$

`Cl_o = Cl/F` "oral clearance" (apparent). 경구만으로 F와 Cl 분리 *불가* — 식별성 한계.

#### Free fraction과의 관계 (p.78 Eq 2:184–2:185; Tozer p.127 Eq 5-4, 5-6)

$$Cl = f_u \cdot Cl_u, \quad Cl_u = \frac{Cl}{f_u}$$

**Tozer 추가 점** (p.150): Cl_u는 *임상적으로 의미 있는* 양 — 약리 효과는 unbound 농도가 결정.

<!-- ANCHOR -->
**다음 카드로의 연결**: 이 비례관계를 신장에 적용 → M2. Plasma↔blood 변환 → M10. 대사체로 확장하면 `dA(m)/dt = CLf · C − CL(m) · C(m)` (Eq 20-4) → **M16**.

---

### M2. ClR · fe · 혈장+소변 simultaneous regression의 골격

<!-- MASTER LENS -->
**Big Idea**: 신청소율(ClR)과 fe는 *혈장 데이터만으로는* 추정 불가. 소변 sample 필요. 두 데이터 source(continuous-in-time 혈장 + interval-averaged 소변)를 한 모델에서 동시 fit하는 것이 본 카드의 핵심.

#### 신장 생리 (CONTEXT — 두 교재 종합)

Nephron: Bowman's capsule (여과; <60,000 dalton; Gabrielsson p.48), proximal tubule (분비 + 재흡수), loop of Henle, distal tubule. **GFR 110–130 mL·min⁻¹** (G) 또는 **120 mL·min⁻¹** (Tozer p.140; 70kg, 20세). **신장 혈류 ~1.1 L·min⁻¹** (Tozer p.125, 심박출량 20–25%), 약 10%만 여과. 소변 pH 4.5–8 변동 (자세히 → M13).

#### 핵심 정의 (Eq 2:87, 2:110; Tozer p.140 Eq 5-21)

$$\frac{dX_u}{dt} = Cl_R \cdot C, \quad CL_R = \frac{\text{Rate of urinary excretion}}{\text{Plasma concentration}}$$

$$X_{u,0-\infty} = Cl_R \cdot AUC_0^\infty$$

$$Cl_R = \frac{X_u(t_1, t_2)}{AUC(t_1, t_2)}$$

마지막 형태가 *time-window별 ClR 변동* 직접 검증에 유용.

#### fe와 Cl, ClR 상수관계 (p.55 Eq 2:104)

$$f_e = \frac{k_u}{k_u + k_m} = \frac{Cl_R}{Cl_R + Cl_m} = \frac{Cl_R}{Cl}$$

#### Tozer 보강 — 신청소 *세 가지* 메커니즘 분리 (p.139 Eq 5-17, 5-18)

$$\text{Rate of excretion} = (1 - F_R) \cdot \left[\text{Filtration} + \text{Secretion}\right]$$

$$CL_R = (1 - F_R) \cdot \left[CL_f + CL_S\right]$$

`CL_f = fu · GFR` (filtration), `CL_S` (secretion), `F_R` (재흡수 분율).

**진단 추론** (Tozer p.141, p.142):
- `CL_R > fu · GFR` → 분비 우세 (probenecid sensitive).
- `CL_R < fu · GFR` → 재흡수 우세 (비극성 약염기).
- `CL_R = fu · GFR` → 여과만 (creatinine, gentamicin).

> **CONTEXT 흡수 — Eq 2:115 (p.56)**: `F = AUC_po · D_iv / (AUC_iv · D_po) = Cl_iv / Cl_po`.

#### Simultaneous nonlinear regression (Eq 2:102–2:103, 2:106)

$$\frac{dX_u}{dt} = f_e \cdot Cl \cdot C, \quad C = \frac{D_{iv}}{V} \cdot e^{-\frac{Cl}{V} \cdot t}, \quad X_u = f_e \cdot D_{iv} \cdot \left[1 - e^{-\frac{Cl}{V} \cdot t}\right]$$

**ARE/Rate plot 대비 우월** (3가지): (1) untransformed data 동시 사용; (2) X_u^∞ 정확 측정 *불필요*; (3) 완전 방광 비움 *불필요*.

**제한**: fe < 0.1 시 simultaneous도 자주 실패.

#### Trench-Level Tip

<!-- TRENCH -->
**현장 팁 — NONMEM**: `DVID`/`CMT`로 dependent variable type 구분, **residual error를 두 ε으로 분리**. PK5에서 plasma CV% 2.84%, urine CV% 8.96% — 약 3배 차이. 같은 ε으로 묶으면 plasma underweighted (Gabrielsson p.498).

<!-- ANCHOR -->
**다음**: ARE와 Rate plot → M3. 신세관 재흡수 정량 → M13.

---

### M3. ARE plot vs Excretion Rate plot — 사용 조건과 한계

<!-- MASTER LENS -->
**Big Idea**: 두 plot은 같은 K(소실 속도상수)를 추정하지만, *어디에 noise가 모이고 어디에 신호가 보이는지*가 정반대. ARE는 cumulative — ClR 시간 변동 평활. Rate는 midpoint averaging — half-life << collection interval일 때 부정확.

#### 두 plot 수식

**Rate plot** (p.51 Eq 2:90–2:92):

$$\ln\left(\frac{dX_u}{dt}\right) = \ln\left(Cl_R \cdot \frac{D_{iv}}{V}\right) - K \cdot t$$

**ARE plot** (p.51–52 Eq 2:93–2:98):

$$\ln(X_u^\infty - X_u) = \ln(X_u^\infty) - K \cdot t$$

#### 한계 비교

| 항목 | Rate | ARE |
|------|------|-----|
| t1/2 << collection interval | **부정확** | 안정 |
| 방광 비완전 비움 | **부정확** | 누적 보정 |
| X_u^∞ 정확 추정 필요? | 아니오 | **예** |
| ClR 시간 변동 (pH/혈류) | **드러남** | 평활 |
| Absorption/assay 누적 오류 | 작음 | **편향** |

#### 실무 판단

1. 두 plot을 *모두* 그린다.
2. Rate fluctuation > ARE → ClR 시간 변동 (pH·혈류 의심).
3. ARE 절편 ≠ 직접 측정 → 방광 비완전 비움 또는 sampling 누락.
4. t1/2 ≈ collection interval → simultaneous regression이 강건.

#### Trench-Level Tip

<!-- TRENCH -->
**현장 팁**: PK5 Figure 2.36 (p.51) vs Figure 5.3 (p.497) — *동일 데이터*에서 ARE t1/2 ≈ 5–6h, Rate t1/2 ≈ 6–6.3h. simultaneous 후 사라짐 (CV% 모두 < 5%).

#### Tozer 보강 — pH-감수성 약물 시간 변동을 *Rate plot이 잡는* 사례

Tozer p.145 Figure 5-16: Methamphetamine (pKa 10) 산성뇨 (70–80% 회수) vs 알칼리뇨 (1–2%). Rate plot fluctuation이 직접 가시화. ARE는 누적 평활로 정보 잃음. 산성/염기성 약물 시험에서 두 plot *반드시 함께* 사용해야 하는 임상적 정당성.

<!-- ANCHOR -->
**다음**: §2.5 — 청소율을 *간*으로 일반화 → M4.

---

### M4. Hepatic extraction & Well-stirred 모델 유도

<!-- MASTER LENS -->
**Big Idea**: Well-stirred는 hepatic clearance를 *세 분리 가능 입력값*으로 표현 — Q_H, fu, Cl_int. 분모 `Q_H + f_u · Cl_int`의 어느 항이 우세한가가 약리 분류 결정.

#### 핵심 변수 (Reference values from Tozer Ch.5)

| 기호 | 정의 | Reference |
|------|------|-----------|
| Q_H | hepatic blood flow | **1.35 L·min⁻¹** (Tozer p.125) — portal 1050 + arterial 300 mL/min |
| Cl_int | intrinsic clearance | 약물별 |
| fu (fu_b) | free fraction in **blood** | (plasma fu와 다름; → M10) |
| Cl_H | hepatic organ clearance | |
| E_H | extraction ratio | 0 ≤ E_H ≤ 1 |
| F_H | hepatic availability = 1 − E_H | |

#### 8단계 유도 (Eq 2:188 → Eq 2:195)

**Step 1** (p.81 Eq 2:188): $V_H \cdot \frac{dC_H}{dt} = Q_H \cdot C_{in} - Q_H \cdot C_{out} - f_u \cdot Cl_{int} \cdot C_{out}$

**Step 2**: 정상상태 `dC_H/dt = 0`.

**Step 3–4**: $C_{out} = \frac{Q_H}{Q_H + f_u \cdot Cl_{int}} \cdot C_{in}$

**Step 5–7** (Eq 2:194):

$$E_H = \frac{f_u \cdot Cl_{int}}{Q_H + f_u \cdot Cl_{int}}$$

**Step 8** (Eq 2:195; Tozer Eq 5-14):

$$\boxed{Cl_H = Q_H \cdot E_H = \frac{Q_H \cdot f_u \cdot Cl_{int}}{Q_H + f_u \cdot Cl_{int}}}$$

#### 4가지 즉각적 함의

1. **0 ≤ E_H ≤ 1** — 혈류가 *상한*.
2. **E_H = 0.5 점**: Q_H = f_u · Cl_int.
3. **fu의 위치**: *Cl_int에 곱해진* 형태 — 단백결합과 효소 *불가분*.
4. **F_H = Q_H / (Q_H + f_u · Cl_int)**.

#### Q_H에 대한 hyperbolic 거동 (Tozer Fig 5-10, p.135)

- 저추출 (fu·Cl_int << Q_H): Cl_H가 hepatocellular activity에 비례.
- 고추출 (fu·Cl_int >> Q_H): Cl_H가 Q_H에 점근.
- E_H = 0.5: fu·Cl_int = Q_H.

> **CONTEXT 흡수 — Tozer Figure 5-9 (p.134)**: Tolbutamide(E_H ~0.07), Phenytoin (~0.5), Diazepam, Propranolol (~0.95) — isolated rat liver fu varying 검증.
>
> **CONTEXT 흡수**: fu가 *blood* 기준 (G p.79; T5 p.135). plasma fu_p와 fu_b 변환 → **M10**, **App.D 통합 완료 (M10 내)**.

> **CONTEXT 흡수 — App.E Model I cross-validation (Tozer pp.777–778, Eq E-1 ~ E-8)**: Tozer Appendix E는 *blood-based* 표기 (Cb, fub)와 rapid equilibration 가정 (Cucell = Cuout)에서 출발하여 Gabrielsson Eq 2:188–2:195와 *완전히 동일한* extraction ratio를 도출 — `E_H = fub·CLint / (QH + fub·CLint)` (Eq E-6) → `CLb,H = QH·fub·CLint / (QH + fub·CLint)` (Eq E-8). 두 교재의 *독립 유도가 동일 결론에 수렴*함은 well-stirred 모델의 수식적 견고성을 입증하며, 표기 차이만 있음 — 단 fu와 fub 혼동은 약물별 다른 비율로 추정 편향을 일으키므로 *반드시* Confusion Pair #14에서 분리 처리.

<!-- ANCHOR -->
**다음**: 분모 우세성에 따른 두 단순화 → M5.

---

### M5. High vs Low extraction 극한 단순화 — *Tozer 사례 통합*

<!-- MASTER LENS -->
**Big Idea**: 동일 식이 분류에 따라 *완전히 다른 두 단순화* — High `Cl_H ≈ Q_H` (flow-limited) vs Low `Cl_H ≈ f_u · Cl_int` (capacity-limited). 임상 변동성 해석 정반대. Tozer는 *실제 약물 사례*로 검증.

#### High extraction (Eq 2:204): `Cl_H ≈ Q_H`

- fu·Cl_int 무관 (IV total).
- **Tozer 대표 (p.130 Table 5-2)**: alprenolol, cocaine, meperidine, morphine, nicotine, nitroglycerin, propoxyphene, **verapamil**, **lidocaine**, **propranolol**.

#### Low extraction (Eq 2:205): `Cl_H ≈ f_u · Cl_int`

- Q_H 무관. fu·Cl_int 직접 비례.
- **Tozer 대표**: carbamazepine, diazepam, ibuprofen, paroxetine, salicylic acid, valproic acid, **warfarin**, **phenytoin**, **tolbutamide**, **alfentanil**, **theophylline**.

#### Intermediate (0.3–0.7) — 단순화 *불가*

- **Tozer**: aspirin, codeine, cyclosporine, ondansetron, nifedipine, nortriptyline.
- PopPK는 *반드시 full equation*.

#### Tozer 검증 #1 — Alfentanil + Rifampin (저추출 효소 유도, p.152)

- Control: CL = 22 L/h/70kg → E_H ≈ 0.27 (low).
- Rifampin 후: AUC 감소, CL 증가 (예측대로).

#### Tozer 검증 #2 — Alprenolol + Pentobarbital (고추출 효소 유도, p.153)

- Control: blood CL = 1.2 L/min ≈ Q_H → E_H ≈ 0.89.
- Pentobarbital 10일: 농도 곡선 *거의 변화 없음* (E_H 0.78 → 0.94).
- 그러나 oral F는 22% → 6% 감소.

#### Tozer 검증 #3 — Fentanyl + Itraconazole vs Ritonavir (고→저 전환, p.154–155)

- Itraconazole (약한 inhibitor): 변화 없음.
- Ritonavir (강한 inhibitor): CL 0.94 → 0.32 L/h/kg (3배 감소) → **고추출→저추출 분류 전환**.
- *조건부 상태*: 추출비 분류는 고정 라벨이 아닌 DDI에 따라 변경 가능.

#### Tozer 검증 #4 — Lidocaine + Propranolol/Metoprolol (고추출 혈류 변화, p.156–157)

- Q_H 감소 → CL 감소 (예측대로).

#### Confusion 경고

<!-- CONFUSION -->
**Confusion (M5.a)**: "High extraction이면 fu 무관"은 **IV total**에 한정. Unbound 또는 oral에서는 fu 결정적 → M6.

#### Trench-Level Tip — DDI boundary

<!-- TRENCH -->
**현장 팁**: 강한 inhibitor DDI 시뮬레이션에서 baseline high extraction 약물(fentanyl)이 *어느 시점에서 low로 전환되는지* 모니터. 전환점 이후 분모 표현 변경 → 추가 억제 *비선형 증가*. AIMS DDI phase 1 dose escalation 안전성 [확인 필요 — 본 PDF 범위 외].

<!-- ANCHOR -->
**다음**: IV 정상상태에서 *경로 × 추출 × fu* 4 조합 → M6.

---

### M6. 투여경로 × 추출비 × fu 의 4사분면 — *Tozer 사례 통합*

<!-- MASTER LENS -->
**Big Idea**: "fu 변화 시 어떻게?" 정답은 *4 조합 모두 다름*. 가장 위험: **highly cleared IV — unbound Css가 fu에 비례 증가**.

#### 4사분면 (Gabrielsson Fig 2.61, p.85)

|              | **Total Css** | **Unbound Css** |
|--------------|---------------|------------------|
| **IV, High E_H** | `R₀/Q_H` (Eq 2:207) — fu 무관 | `fu · R₀/Q_H` (Eq 2:208) — **⚠️ fu 의존** |
| **IV, Low E_H** | `R₀/(fu · Cl_int)` [복원] — fu 의존 | `R₀/Cl_int` (Eq 2:210) — fu 무관 |
| **Oral, High E_H** | `R₀/(fu · Cl_int)` (Eq 2:212) — fu 의존 | `R₀/Cl_int` (Eq 2:213) — fu 무관 |
| **Oral, Low E_H** | `R₀/(fu · Cl_int)` (Eq 2:212) — fu 의존 | `R₀/Cl_int` (Eq 2:213) — fu 무관 |

#### Warning (Gabrielsson p.84): Etidocaine (IV + High E_H) — fu 변동 시 unbound 갑작스런 상승.

#### Tozer 검증 #1 — Phenytoin in Uremia (저추출, **큰 V**, fu 증가, p.159–160)

- Uremia: AUC 절반, V 2배, **t1/2 거의 동일**.
- 해석: fu 0.10 → 0.20–0.30 → CL 2배 (저추출), V 2배 (large V; Eq 5-30) → t1/2 약분.
- **Cl_int 자체 무변**.
- 임상: total 정상 범위 적용 시 *underdose* — free phenytoin 측정 필요.

#### Tozer 검증 #2 — Clofibric Acid in Nephrotic Syndrome (저추출, **작은 V**, p.161–162)

- Nephrotic: t1/2 16.5 → **8.7 h** (절반).
- 해석: fu 0.03 → 0.055 → CL 1.8배, V 거의 무변 (small V; Eq 5-34) → t1/2 단축.
- **메시지**: 동일 "저추출 + fu 증가"이지만 V 크기에 따라 t1/2 거동 *완전히 다름*.

#### Tozer 검증 #3 — Propranolol (고추출, 큰 V, fu 변동, Fig 5-28, p.160)

- fu 0.07 → 0.11: blood CL 불변 (perfusion-limited), V 비례 증가, **t1/2 비례 증가**.

#### PopPK 공변량 함의

| 약물 분류 | 단백결합 변화 | PopPK 공변량 우선 |
|-----------|---------------|---------------------|
| IV + High E_H, large V | total 무변, **unbound 비례 ↑**, t1/2 ↑ | 혈류·체중·심박출량 |
| IV + Low E_H, large V (phenytoin) | total ↓, unbound 무변, **t1/2 무변** | albumin·CYP 활성 |
| IV + Low E_H, small V (clofibric acid) | total ↓, unbound 무변, **t1/2 ↓** | albumin·CYP + V의 fu 의존 |
| Oral 모두 | total 비례 ↓, unbound 무변, first-pass 큼 | F 통합 |

> **CONTEXT 흡수 — Tozer Eq 5-30, 5-34 (V vs fu)**:
> - Large V (>50 L): `V ≈ V_R · (fu/fu_R)` → fu 비례.
> - Small V: `V = V_E + Constant·fu` → fu 거의 무관.

<!-- ANCHOR -->
**다음**: Cl_int 추정 함정 → M7.

---

### M7. IVIVE의 세 가지 함정 — Single-point, MMP, Data condensation

<!-- MASTER LENS -->
**Big Idea**: In vitro Vmax, Km을 in vivo Cl_int로 외삽하는 IVIVE는 *세 곳에서* 시스템 실패. AIMS 컨설팅 가장 흔한 실패 지점.

#### Inter-species 출발점 (CONTEXT)

Gabrielsson p.87 Table 2.7 (인간): 70 kg, 간 1500 g, 간혈류 1450 mL·min⁻¹, 10⁶ cells/g 120, **마이크로솜 단백 50 mg/g (range 20–77)**. 마지막 *range*가 함정 #2 출발점.

#### 함정 #1 — Single-point method (Fig 2.63, p.88)

- 단일 농도 v₀ → Cl_int = Vmax/(Km + C₀) ≈ Vmax/Km을 *상수* 가정.
- 위험: saturable kinetics 평탄화 → **저농도 F 과대평가, 고농도 F 과소평가**.
- Phenytoin 같은 saturation 약물의 dose escalation 예측 *완전 잘못*.

#### 함정 #2 — MMP 보정계수 (Table 2.8, p.87)

| In vitro 카테고리 | MMP=20 | MMP=50 | MMP=77 |
|-------------------|--------|--------|--------|
| Low (E<0.3) | **0.15** ✓ | 0.31 | 0.40 |
| Intermediate | 0.5 | **0.7** | 0.79 |
| High (E>0.7) | 0.8 | 0.93 | **0.95** ✓ |

(Gabrielsson p.87)

- "Low"에 MMP=77 → 0.40 reclassify → CL 2.5배 과대 → FIH 위험.
- IVIVE 보고서 *반드시 MMP 명시* + sensitivity analysis.

#### 함정 #3 — Data condensation (Fig 2.64–2.65, p.88–89)

- 농도-시간 → v₀–C₀ 5점 축약 → 저/고용량 (Vmax, Km) 평균화.
- 본문 예 (p.89): 저농도 Vmax=0.97, Km=0.091 vs 고농도 Vmax=1.02, Km=8.9 — 5점에서 single linear.
- **해결**: untransformed 농도-시간 nonlinear regression.

#### Trench-Level Tip

<!-- TRENCH -->
**현장 팁 — AIMS**: in vitro 데이터 받으면 (1) MMP 명시? (2) Vmax/Km이 raw 농도-시간 fit인가, condensation 후인가? 후자면 raw로 untransformed fit 재실행 [확인 필요 — 본 PDF 범위 외 추론].

#### Tozer 보강 — Plasma vs Blood IVIVE 함정 (p.127, p.128)

In vitro = blood, 임상 = plasma. **변환 → M10**. 핵심: plasma CL 1.3 L/min + C/Cb 0.1 → blood CL 0.13 L/min → **고추출이 아니라 저추출**.

#### Plasma vs blood 보정 (Eq 2:221–2:227, p.89–90)

$$CL_H = CL_{H,B} \cdot \frac{C_B}{C_P}$$

C_B/C_P first-principles 유도 → **M10 (App.D Eq D-6 통합 완료)**.

<!-- ANCHOR -->
**다음**: 4가지 모델 비교 → M8.

---

### M8. 4가지 간 청소율 모델 비교 (Table 2.9)

<!-- MASTER LENS -->
**Big Idea**: 같은 (Q_H, fu, Cl_int)에 대해 4 모델 서로 다른 E_H — *highly cleared에서 차이 큼*. PBPK 모델 선택 차이가 임상 외삽에서 *수배의* 노출 예측 오차.

#### Table 2.9 자체 재구성 (Gabrielsson p.94)

먼저 4 모델에 공통 적용되는 *3 무차원 변수* 정의:
- `R_N = f_u · Cl_int / Q_H` — clearance/flow ratio (extraction efficiency 핵심).
- `ε²` (Distributed model) — variance of relative blood flow; intra-organ flow heterogeneity 측정.
- `D_N` (Dispersion model) — axial dispersion number; D_N → 0 = plug flow, D_N → ∞ = perfectly mixed.
- `a = (1 + 4·R_N·D_N)^{1/2}` — Dispersion model 보조 변수.

| Parameter | **Well-stirred** | **Parallel tube** | **Distributed** | **Dispersion** |
|-----------|------------------|-------------------|------------------|----------------|
| **E_H** | $\dfrac{R_N}{1 + R_N}$ | $1 - e^{-R_N}$ | $1 - e^{-R_N \left(1 + \tfrac{1}{2} \varepsilon^2 R_N\right)}$ [확인 필요] | $1 - \dfrac{4a}{(1+a)^2 \cdot e^{(a-1)/(2 D_N)} - (1-a)^2 \cdot e^{-(a+1)/(2 D_N)}}$ [확인 필요] |
| **F_H** | $1 - E_H$ | $1 - E_H$ | $1 - E_H$ | $1 - E_H$ |
| **Cl_H** | $Q_H \cdot E_H$ | $Q_H \cdot E_H$ | $Q_H \cdot E_H$ | $Q_H \cdot E_H$ |

> **[확인 필요]** Distributed model의 정확한 expansion form (`1 + ε²R_N/2`이 지수 내부 곱셈자인지 합자인지) 및 Dispersion model 닫힌 해는 Gabrielsson p.93–94 본문 + Roberts & Rowland 원전 (1986)에서 페이지 별로 표기가 다를 수 있어 *원전 직접 cross-reference 후* 최종 확정. 본 카드의 형태는 Gabrielsson Table 2.9 (p.94) 기반 *재구성*; Phase 2 변환 시 Roberts & Rowland 1986 원전 식 (Roberts MS, Rowland M. *J Pharm Sci* 75:1100–1106, 1986)과 *반드시 1:1 검증* 필요.

#### 모델 간 *수렴 조건* 정밀화

| 조건 | Distributed → | Dispersion → |
|------|----------------|----------------|
| 이질성·혼합 극단적 큼 | ε² → ∞ → **Well-stirred** | D_N → ∞ → **Well-stirred** |
| 이질성·혼합 극단적 작음 | ε² → 0 → **Parallel tube** | D_N → 0 → **Parallel tube** |
| 수치적으로 fit 가능 | ε이 *데이터에서* 추정 | D_N이 *데이터에서* 추정 |

#### 4 모델 개념적 차이

- **Well-stirred (venous equilibrium)**: 간 내부 농도 = outflow.
- **Parallel tube (sinusoidal)**: 입구→출구 *지수 감소*. 평균 = log-mean.
- **Distributed**: ε² 큼 → well-stirred. 작음 → parallel tube.
- **Dispersion**: D_N → ∞ → well-stirred. D_N → 0 → parallel tube.

#### 모델 간 예측 차이 방향

`f_u · Cl_int / Q_H` 큰 (highly cleared) → 차이 가장 큼. Parallel tube > well-stirred (`1 − e^(−x) > x/(1+x)` for x > 0).

#### Confusion 경고

<!-- CONFUSION -->
**Confusion (M8.a)**: 수렴 방향 자주 거꾸로 외워짐. **올바른 직관**: 이질성·혼합 *극단적으로 큼* → 시간 평균이 well-stirred와 같아짐.

> **CONTEXT 흡수**: ε, D_N, R_N 모두 *데이터에서* 추정 (Gabrielsson p.93).

<!-- ANCHOR -->
**다음**: PK5 case → M9.

---

### M9. PK5 — 통합해 vs ODE 시스템의 등가성

<!-- MASTER LENS -->
**Big Idea**: PK5는 1-cmt IV bolus + 소변을 *두 표현*으로 풀고, **거의 동일 추정값과 정밀도** 검증 (p.499). NONMEM ADVAN1 vs ADVAN6의 *상호교환 가능성* 이론적 근거.

#### Problem (p.494)

IV bolus 250 mg, 0.5–24 h plasma + 누적 소변, Cl·V·fe 추정, constant CV.

#### 두 표현

**통합해** (p.495 Eq 5:1, 5:2):

$$C_{iv} = \frac{D_{iv}}{V} \cdot e^{-\frac{Cl}{V} \cdot t}, \quad X_u = f_e \cdot D_{iv} \cdot \left[1 - e^{-\frac{Cl}{V} \cdot t}\right]$$

**ODE** (p.495 Eq 5:3, 5:4):

$$\frac{dC}{dt} = -\frac{Cl}{V} \cdot C, \quad \frac{dA_u}{dt} = f_e \cdot Cl \cdot C$$

#### 초기 vs 최종 추정값 — **반드시 분리**

| 파라미터 | 초기 (그래픽) | 최종 (simultaneous) |
|----------|---------------|---------------------|
| V | ~7 L | (본문 미명시) |
| Cl | ~2 L·h⁻¹ | **1.2 L·h⁻¹** |
| fe | ~0.3 | **≈0.35** |
| ClR | (간접) | **0.42 L·h⁻¹** |

**중요**: Cl 2→1.2 (40% 감소) — 그래픽 NCA가 *체계적으로 큰* Cl. trapezoidal AUC + initial slope 시각 추정 부정확.

#### 결과 정밀도 (p.498)

CV%: plasma 2.84%, urine 8.96%. 모든 파라미터 CV% < 5%.

#### NONMEM 코딩

- **Integrated** → `$SUBROUTINE ADVAN1 TRANS2`.
- **ODE** → `$SUBROUTINE ADVAN6/13` + `$MODEL COMP=(CENTRAL) COMP=(URINE)` + `$DES`.

ODE는 Michaelis-Menten 비선형 *직접 확장 가능*.

> **CONTEXT 흡수 — 1/K sampling**: K 추정 최적 sampling time.

<!-- ANCHOR -->
**§2 종결의 1차**: M1–M9 = Gabrielsson covering. **다음 Tozer Ch.5 6개** → M10–M15.

---

### M10. Plasma vs Blood Clearance & C/Cb 비 — *Tozer 신규*

<!-- MASTER LENS -->
**Big Idea**: 약물의 *추출비 분류* — "고추출인가 저추출인가?" — 는 **반드시 blood clearance로 답해야**. Plasma CL = 1.3 L/min만 보고 "고추출"이라 결론 내리면, plasma-to-blood = 0.1인 약물에서는 *blood CL = 0.13 L/min에 불과해 사실은 저추출* — 임상 함의 정반대. IVIVE 가장 흔한 시스템 오류.

#### 핵심 정의 (Tozer Eq 5-4, p.127)

$$\text{Rate of elimination} = CL \cdot C = CL_b \cdot C_b = CL_u \cdot C_u$$

- `CL` — plasma clearance.
- `CL_b` — blood clearance.
- `CL_u` — unbound clearance.

#### 변환 (Tozer Eq 5-5, 5-6)

$$CL_b = CL \cdot \left(\frac{C}{C_b}\right), \quad CL_u = \frac{CL}{f_u}$$

#### C/C_b 범위 (Tozer p.127)

- **0.3 ~ 2.0** 일반. 일부 매우 낮음 (cyclosporine ~0.03).
- 상한 ≈ 2.0 ≈ 1/(1 − hematocrit) (혈장 한정).

#### 왜 well-stirred가 blood 기준인가 (p.135)

간에 *혈류로 전달*되는 양은 plasma×plasma flow가 아니라 *blood × blood flow*. Mass balance가 *blood*일 때만 정확.

#### Tozer 핵심 사례 (p.127)

> Plasma CL 1.3 L/min, C/C_b = 0.1 → Blood CL 0.13 L/min << Q_H = 1.35 L/min → **저추출**. 임상 함의 정반대.

#### Unbound Clearance 의미 (p.127)

저추출: `CL ≈ fu·CL_int` → `CL_u ≈ CL_int`.
고추출: `CL ≈ Q_H` → `CL_u = Q_H/fu` — fu 반비례.

#### Trench-Level Tip — IVIVE 검증 첫 단계

<!-- TRENCH -->
**현장 팁**: PBPK·IVIVE 보고서 받으면 *반드시 첫 페이지*에서 (1) C/C_b 명시? (2) CL이 plasma인가 blood인가? (3) E_H 계산이 *blood*로? 셋 중 하나라도 불명확이면 잠재 오류. AIMS 표준 첫 질문 [확인 필요].

> **CONTEXT 흡수 — App.D first-principles (Tozer pp.775–776, Eq D-1 ~ D-8)**: 전혈 mass-balance (`Cb·VB = C·VP + CBC·VBC`) + RBC partition (`CBC = KpBC·fu·C`) + 부피 분율 (`VP = (1−H)·VB`, `VBC = H·VB`)에서 출발하여 다음 두 결과식 도출:
>
> $$\boxed{\frac{C}{C_b} = \frac{1}{1 + H \cdot [f_u \cdot K_{PBC} - 1]} \quad \text{(Eq D-6)}, \qquad K_{PBC} = \frac{H - 1 + (C_b/C)}{f_u \cdot H} \quad \text{(Eq D-8)}}$$
>
> Eq D-6은 *세 결정자* (H, fu, KpBC)의 조합으로 plasma-to-blood 비를 결정하며, **`fu·KpBC < 1` → C/Cb > 1 (RBC 회피); `fu·KpBC > 1` → C/Cb < 1 (RBC 강한 분배)**. Tozer p.776 Study Problem 1은 H/fu 변동 시나리오 (anemic, nephrotic) 정량 풀이를 제시 — 본 통합본에서는 *symbolic 수준*으로만 보존하고, 풀이 자체는 학습자가 교재 원문을 직접 풀어볼 *Phase 4 학습 과제*로 분리. **임상 메시지**: 단백결합 변동 (uremia, hypoalbuminemia, DDI displacement) 시 plasma-to-blood 비 *동시 변동* → plasma 농도만 측정하는 routine TDM은 *hidden bias* 발생 가능.

#### NONMEM 코딩 — App.D 환자별 변환

```
BPRATIO = 1.0 / (1.0 + H * (FU * KPBC - 1.0))
CLB    = CL * BPRATIO            ; blood clearance per patient
```

KpBC는 약물별 *상수*로 model에 fixed (in vitro RBC partition 측정 또는 별도 i.v. paired blood/plasma study에서 Eq D-8로 추정).

#### Trench-Level Tip — fu vs fub 혼동 검출

<!-- TRENCH -->
**현장 팁**: NONMEM 보고서 검토 시, 코드의 `FU` 컬럼이 *plasma fu*인지 *blood fub*인지 *반드시 명시 확인*. Tozer Ch.5 well-stirred (Eq 5-14) 분모 `Q_H + fub·CLint`에 *plasma fu*를 잘못 입력하면 CL_H 추정 *체계적 편향*. Confusion Pair #14에 정리.

<!-- ANCHOR -->
**다음**: 한 약물의 한 청소율의 두 표현. 그러나 *여러 기관*이 동시 청소할 때 → M11.

---

### M11. Clearance Additivity — `CL = CLR + CLH` *Tozer 신규*

<!-- MASTER LENS -->
**Big Idea**: 한 약물이 여러 기관(신장 + 간 + 폐)에서 동시 제거 시 청소율은 *덧셈* — 순환계 해부학적 결과 (병렬 배치). additivity가 무너지는 *유일 예외*(폐)가 있으며, 흡입 약물·기침 억제제 PopPK가 시스템적으로 잘못된다. fe와 (1−fe)의 의미가 이 위에서만 정의 — 신부전 dose 조절 권고의 수식 기반.

#### 핵심 정의 (Tozer Eq 5-7, 5-8, 5-9, p.128)

$$\boxed{CL = CL_R + CL_H}$$

#### 두 청소율 분리 추정 (p.128)

- **Total CL**: i.v. dose / AUC.
- **Renal CL**: `fe · CL`.
- **Hepatic CL**: `(1 − fe) · CL`.

#### 신부전 환자 dose 조절 수식적 근거

$$CL_i = \underbrace{(1 - f_{e,\text{typ}}) \cdot CL_{\text{typ}}}_{\text{비신청소}} + \underbrace{f_{e,\text{typ}} \cdot CL_{\text{typ}} \cdot \frac{CrCL_i}{120}}_{\text{신청소}}$$

fe = 0.35, CrCL = 30: `CL_i = 0.65·CL + 0.088·CL = 0.74·CL` (26% 감소). *전체*를 power-scale하는 단순 모델은 더 큰 감소 외삽 → over-conservative.

#### Pulmonary Clearance — Additivity의 *유일* 예외 (p.128)

폐는 *직렬*. 정맥혈이 모두 폐 통과 후 좌심방. 측정 농도는 *폐 떠난 후* → 단순 additivity 위배. 흡입 약물·기침 억제제 PopPK는 *반드시 별도 모델*.

#### Phase I/II 분류 — CONTEXT (p.121)

- Phase I: oxidation, reduction, hydrolysis. 흔히 prodrug → active.
- Phase II: glucuronidation, sulfation, acetylation.
- CYP abundance: CYP3A4 가장 풍부; CYP2D6 ~2%이지만 prescribed drug clearance의 25% 담당.
- 약물 60–70%가 CYP3A4 또는 CYP2D6 — DDI risk 출발점.

#### Soft Drug — CONTEXT (p.124)

활성 약물을 국소 적용 후 systemic 흡수 시 *비활성 대사체로 빠르게 전환*. 예: ciclesonide.

<!-- ANCHOR -->
**다음**: 간 약물 일부는 bile 배설 → 장 재흡수. EHC는 elimination이 아니라 **distribution** → M12.

---

### M12. Biliary Excretion & Enterohepatic Cycling — *Tozer 신규*

<!-- MASTER LENS -->
**Big Idea**: 담즙으로 빠진 약물이 *장에서 재흡수*되면 그 *cycle*은 **distribution**. biliary obstruction 시 t1/2가 *반대 방향*으로 변할 수 있음 (V 감소 → t1/2 단축 vs CL 감소 → t1/2 연장).

#### 정의 (Tozer Eq 5-16, p.137)

$$\text{Biliary clearance} = \frac{(\text{Bile flow}) \cdot (\text{Concentration in bile})}{\text{Concentration in plasma}}$$

#### Reference 수치 (p.137)

- Bile flow: 0.5–0.8 mL/min.
- Bile-to-plasma ratio: ≤1 ~ up to 1000 (biliary CL up to 500 mL/min).
- 상한: hepatic blood flow (1.35 L/min).

#### 담즙 분비의 *4가지 조건* (p.138)

1. 능동 분비. 2. 극성 (비극성은 회장 재흡수). 3. MW > 350 g/mol. 4. 분비 메커니즘별 특이성.

**Glucuronide conjugates**가 4 조건 모두 만족 → biliary 우세 + EHC 흔함.

#### Enterohepatic Cycle (Fig 5-12, p.138)

- 직접 EHC: drug → bile → 장 → reabsorption → portal → liver.
- 간접 EHC: drug → metabolite (glucuronide) → bile → 장 → β-glucuronidase 가수분해 → drug → reabsorption.

> "enterohepatic cycling is a component of distribution, not elimination" (p.137)

#### Biliary Obstruction의 t1/2 변화 (p.148)

- **Case A** (완전 EHC): 차단 → V 감소 (CL 무변) → **t1/2 단축**.
- **Case B** (EHC 없음): 차단 → V 무변, CL 감소 → **t1/2 연장**.

t1/2 변화 방향만으로는 EHC 여부 추론 불가 → V와 CL을 *분리* (→ M14).

<!-- ANCHOR -->
**다음**: 간 처리 끝. urine pH·flow → M13.

---

### M13. Renal Tubular Reabsorption — Urine pH & Flow — *Tozer 신규*

<!-- MASTER LENS -->
**Big Idea**: Methamphetamine 같은 약물·용량에서 sodium bicarbonate 복용 시 1–2% 소변 회수, ammonium chloride 복용 시 70–80% — *50배 차이*. **신세관 재흡수**의 pH 의존성. 약리학적 pH 조절(forced alkalinization for aspirin overdose)의 수식적 기반.

#### 핵심 정의 (Eq 5-22, 5-23, p.142)

평형 시:

$$CL_R = \frac{(\text{Urine flow}) \cdot (\text{Urine concentration})}{\text{Plasma concentration}}$$

비이온화 평형:

$$\boxed{CL_R = f_u \cdot \text{Urine flow}}$$

평형 시 CL_R 하한.

#### Urine Flow

- 정상 1–2 mL/min. Forced diuresis: up to 15–20 mL/min.
- 재흡수 활발 약물에만 영향.

#### Urine pH — Henderson-Hasselbalch (Tables 5-3, 5-4)

비이온화 형태가 막 통과 → 재흡수. 평형 시 비이온화 농도 plasma = urine.

**Tozer Table 5-3 자체 재구성** (p.143; 단백결합 없음, urine flow 1 mL/min, plasma pH 7.4; mL/min CL_R):

| 약물 | 성격 | pKa | pH 4.4 | pH 6.4 | pH 7.9 |
|------|------|-----|--------|--------|--------|
| A | Acid | 2.4 | 0.001 | 0.1 | 3 |
| B | Acid | 6.4 | 0.1 | 0.2 | 3 |
| C | Acid | 10.4 | 1.0 | 1.0 | 1.0 |
| D | Base | 2.4 | 1.0 | 1.0 | 1.0 |
| E | Base | 6.4 | 90 | 2 | 0.9 |
| F | Base | 10.4 | 1000 | 10 | 0.3 |

**핵심 패턴**:
- pKa<2 산, pKa>12 염기: pH 둔감.
- 약산 (pKa 3–7.5): pH ↑ → CL_R ↑ → 알칼리화로 가속 (salicylic acid).
- 약염기 (pKa 6–12): pH ↓ → CL_R ↑ → 산성화로 가속 (amphetamine).

#### Tozer 검증

- **Methamphetamine** (pKa 10): 산성뇨 70–80% / 알칼리뇨 1–2% — 50배.
- **Salicylic Acid** (pKa 3): pH<6.5 거의 0 / pH>7.5 200 mL/min 이상 — aspirin overdose 알칼리 이뇨 근거.
- **Phenobarbital** (pKa 7.2): flow + pH 동시 효과 2–3배.
- **Diethylcarbamazine** (pKa 10): 산성 38 L/h / 알칼리 1 L/h — 38배.

#### Forced Diuresis 적용 기준 (p.147)

1. 신청소 주 경로 (또는 overdose에서 metabolic saturate).
2. 약물 *normally extensive 재흡수*.
3. 재흡수 pH 감수성.

이미 90→10% 감소 약물은 추가 가속 marginal.

#### Renal Metabolism — CONTEXT (p.147)

신장 hydrolysis, oxidation, conjugation 효소 — minor route이지만 renal impairment에서 상대 비중 증가.

#### Trench-Level Tip

<!-- TRENCH -->
**현장 팁 — PopPK urine pH covariate**: weak acid (pKa 3–7.5) 또는 weak base (pKa 6–12) sparse-sampling PopPK에서 urine pH 측정되면 *반드시* covariate 후보. 무시 시 inter-occasion variability 부풀어 inter-individual 왜곡.

<!-- ANCHOR -->
**다음**: t1/2는 **CL과 V의 derived parameter**, *primary*가 아님 → M14.

---

### M14. Half-life as Derived (Secondary) Parameter — *Tozer 신규*

<!-- MASTER LENS -->
**Big Idea**: t1/2 변화 관찰은 *결론*이 아니라 *질문*. CL 또는 V의 변화 *결과*. "rifampin이 t1/2 단축"은 미완성 — "CL 증가, V 무변"으로 분해해야 메커니즘(효소 유도) 결정. **t1/2는 CL과 V에 의존, 그 역이 아니다** (Tozer p.119).

#### 핵심 정의 (Eq 5-24, 5-25, p.148)

$$k = \frac{CL}{V}, \quad t_{1/2} = \frac{0.693}{k} = \frac{0.693 \cdot V}{CL}$$

#### Primary vs Secondary (Table 5-6, p.151)

| Type | 파라미터 | 정의 |
|------|----------|------|
| **Primary** | CL (CL_R, CL_H), V | 생리학적 *직접*. PopPK 추정 대상. |
| **Secondary (derived)** | t1/2, k, fe | Primary로부터 *계산*. 그 자체로 생리 의미 부여 금지. |
| **Observations** | AUC, Cmax, Ae | Primary + dose 함수. 직접 측정. |

NONMEM에서 `THETA(CL)`, `THETA(V)` 추정하지 `THETA(t1/2)` 추정 *안 함*.

#### t1/2 변화의 4가지 시나리오 (p.148)

1. **CL ↑, V 무변** → 효소 유도, 신혈류 ↑ (alfentanil + rifampin).
2. **CL 무변, V ↓** → 단백결합 변화 + small V, EHC drug의 biliary obstruction.
3. **CL ↑, V ↑ (비례)** → fu 변화 + large V drug. **t1/2 거의 무변** (phenytoin in uremia).
4. **CL ↓, V ↑** → 모순적 — 흔치 않음.

#### Tozer "강조" 사례

- **Phenytoin in Uremia**: t1/2 무변 + CL 2배 + V 2배. *t1/2만 보고 "신부전 영향 없다"는 완전히 잘못* — total 절반, unbound 정상이지만 noxic은 unbound가 결정.
- **Biliary Obstruction**: EHC 활발 → t1/2 단축 / EHC 없음 → t1/2 연장. **t1/2 방향만으로 EHC 추론 불가**.

#### Half-life "범위" (Fig 5-19, p.149)

- CL: 0.01–100 L/h (10,000배). V: 3–7000 L (2,000배). t1/2: 분 ~ 수개월. 같은 t1/2 다른 CL/V.
- Long-half-life drugs (low CL, large V) *부재* (예외: mAb): 누적 *수주*, 독성 detoxification 느림 → 시장 진입 적음.

#### NONMEM 코딩

```
$PK
CL = THETA(1) * EXP(ETA(1))
V  = THETA(2) * EXP(ETA(2))
K  = CL/V
T_HALF = 0.693/K           ; reporting only
```

<!-- ANCHOR -->
**다음**: 약물이 *세포 내로 들어가는* 과정 자체가 율속 → M15.

---

### M15. Extended Clearance & Permeability/Transporter Roles — *Tozer 신규*

<!-- MASTER LENS -->
**Big Idea**: Pravastatin, rosuvastatin, valsartan은 well-stirred 예측과 실제 임상 CL이 *수배 어긋난다*. *간세포 내 진입*이 율속 — OATP1B1 같은 uptake transporter. SLCO1B1 polymorphism 또는 cyclosporine inhibitor가 CL 자체 변화. 현대 IVIVE 새 표준.

#### 기본 well-stirred의 한계 (Fig 5-11, p.136)

basolateral P·SA가 lipophilicity와 양의 상관:
- Diclofenac, lidocaine, diazepam (lipophilic): P·SA >> Q_H → well-stirred OK.
- **Pravastatin, rosuvastatin, valsartan**: P·SA < Q_H → uptake permeability 율속.
- Atenolol, ampicillin: 매우 낮음, transporter-mediated.

#### Hepatic Transporters 위치 (p.137)

**Basolateral (혈액↔간세포)**: **OATP1B1** (uptake), OATP1B3, OATP2B1; MRP3 (efflux to blood).
**Apical/canalicular (간세포↔bile)**: **P-gp / MDR1**, MRP2, BCRP.

#### Extended Clearance (Eq 5-35, 5-36, p.162)

$$CL_{int,H} = \frac{(PS_{influx} + PS_{pd}) \cdot CL_{int}}{(PS_{efflux} + PS_{pd} + CL_{int})}$$

$$CL_{b,H} = Q_H \cdot \frac{f_{u_b} \cdot (PS_{influx} + PS_{pd}) \cdot CL_{int}}{Q_H \cdot (PS_{efflux} + PS_{pd} + CL_{int}) + f_{u_b} \cdot (PS_{influx} + PS_{pd}) \cdot CL_{int}}$$

여기서 `CL_int = CL_int,met + CL_int,bil`.

#### 기본 well-stirred로의 환원

`PS_influx + PS_pd` >> 그리고 `PS_efflux + PS_pd << CL_int` → `CL_int,H = CL_int` → 기본 well-stirred (M4) 회복.

#### 율속 단계 분류

| 율속 단계 | 약물 예 |
|-----------|---------|
| Hepatic blood flow | Lidocaine, propranolol |
| Hepatocellular metabolism | Diazepam, warfarin |
| **Basolateral uptake** | **Pravastatin, rosuvastatin, valsartan** |
| **Apical efflux (bile)** | 일부 cytotoxic [확인 필요] |

#### 임상 함의

- OATP1B1 inhibitor (cyclosporine, gemfibrozil) + statin → 노출 *수배 ↑* → rhabdomyolysis 위험.
- SLCO1B1 \*5 polymorphism (~15%): 활성 ↓ → 2–3배 노출.

#### 통합 IVIVE 워크플로우 5단계

1. Plasma → Blood 변환 (M10). 2. Extraction ratio 분류 (M5). 3. 율속 단계 (M15). 4. MMP (M7). 5. Vmax/Km (M7).

#### Trench-Level Tip — Statin PBPK

<!-- TRENCH -->
**현장 팁**: Statin PBPK 받으면 *반드시* OATP1B1 inhibition을 covariate scenario로. 단일 inhibitor가 동시에 CYP3A4 inhibitor면 효과 *증폭*. AIMS에서 statin·gemfibrozil 같은 조합은 단순 CYP-only 모델로 임상 변화 폭 예측 못 함 [확인 필요].

> **CONTEXT 흡수 — App.E Model II ρ term (Tozer pp.778–779, Eq E-9 ~ E-15)**: Model I의 rapid equilibration 가정을 완화하여 hepatocyte 막투과성을 명시 — intracellular mass balance에서 *intracellular-to-extracellular unbound concentration ratio* `ρ = Pin·SA / (Pout·SA + CL_int)`를 정의. 결과식:
>
> $$\boxed{CL_{b,H} = Q_H \cdot \frac{f_{ub} \cdot \rho \cdot CL_{int}}{Q_H + f_{ub} \cdot \rho \cdot CL_{int}} \quad \text{(Eq E-13)}}$$
>
> *세 임상 시나리오*: (#1) Pin·SA >> CLint → ρ ≈ 1 → **기본 well-stirred (Model I) 회복** (lipophilic 약물); (#2) Pin·SA << CLint → ρ = Pin·SA/CLint → **basolateral uptake 율속** (statins); (#3) Pin << QH → **`CLb,H ≈ fub·Pin`** (Eq E-15, 매우 polar 약물). Eq 5-35 (Tozer Ch.5)와 *수학적 동등* (`PS_influx ≈ Pin·SA`, `PS_efflux ≈ Pout·SA`, `PS_pd ≈ 0` 매핑) — App.E가 first-principles 유도 제공.

> **임상 함의**: SLCO1B1 \*5 polymorphism (~15% 보유) → OATP1B1 활성 감소 → Pin·SA 감소 → ρ 감소 → CLb,H 비례 감소 → 통상 statin AUC 2–3배 증가 → rhabdomyolysis 위험. Cyclosporine 같은 OATP1B1 inhibitor도 동일 메커니즘.

#### 통합 IVIVE 워크플로우 5단계 (Step 4 갱신)

1. **Plasma → Blood 변환** (M10 + App.D Eq D-6 first-principles).
2. **Extraction ratio 분류** (M5).
3. **율속 단계 진단** (M15 + App.E Eq E-13의 *세 시나리오 분류*).
4. **MMP 보정** (M7).
5. **Vmax/Km untransformed fit** (M7).

<!-- ANCHOR -->
**§2 종결의 2차**: M1–M9 (Gabrielsson) + M10–M15 (Tozer Ch.5 + App.D·E 통합) = 15개 카드. **이제 Tozer Ch.20이 도입하는 모자식 PK 5개 신규 카드** → M16–M20.

---

### M16. Parent–Metabolite Mass Balance & AUC Ratio Analysis — *Tozer Ch.20 신규*

<!-- MASTER LENS -->
**Big Idea**: 한 약물의 elimination은 그 약물 자체로 끝나지 않는다 — 대부분 약물은 *대사체*를 만들고, 그 대사체가 임상 효과·독성·약물상호작용을 좌우할 수 있다 (Tozer Table 20-1: codeine→morphine, prednisone→prednisolone, sulindac→sulfide, propranolol→4-hydroxypropranolol 등). 본 카드는 모자식(parent–metabolite) 시스템의 *mass balance 골격*을 정의하고, **혈장 AUC 비(AUC[m]/AUC)만으로** fm·CL·V를 분리 추론하는 정량적 도구를 제공한다. AIMS 컨설팅에서 active metabolite를 가진 약물의 PopPK 분석을 처음 받았을 때, 이 한 카드의 식들이 분석의 *모든* 출발점이 된다.

#### 모자식 scheme — 두 단계로 분해

```
        k_other (inactive pathways)
A    →
Drug  k_f                k(m)
in    →    A(m)    →    Ae(m)
body       Metabolite    Eliminated
           in body       metabolite
```

전체 elimination rate constant: `k = k_f + k_other`.

#### 핵심 mass balance (Tozer Eq 20-1, p.659)

$$\frac{dA(m)}{dt} = \underbrace{k_f \cdot A}_{\text{Rate of formation}} - \underbrace{k(m) \cdot A(m)}_{\text{Rate of elimination}}$$

**중요한 단서** (Tozer p.659): `k_f · A`는 엄밀히 *systemic circulation으로 entry*되는 rate. 일부 대사체가 organ 내에서 추가 대사되면 (sequential metabolism), 형성된 양 중 *일부만* 혈류로 방출.

> **CONTEXT 흡수 — Sequential metabolism (p.659)**: Clopidogrel은 inactive prodrug, 장 + 간에서 *2-step 대사*를 거쳐 P2Y12 receptor에 결합하는 활성 대사체로 전환. 본 카드의 단순 `k_f · A` 표현은 이런 sequential 시스템에서 *single equivalent rate*로 단순화.

#### Plasma 농도 형태 (Tozer Eq 20-4, p.662)

$$\frac{dA(m)}{dt} = \underbrace{CL_f \cdot C}_{\text{Formation}} - \underbrace{CL(m) \cdot C(m)}_{\text{Elimination}}$$

여기서:
- `CL_f` — **formation clearance** (parent → metabolite의 clearance).
- `CL(m)` — total clearance of metabolite.
- `CL_f = fm · CL` (fm = fraction of dose converted to systemically available metabolite).

#### AUC 비 — 본 카드의 핵심 도구 (Tozer Eq 20-5, 20-6, p.662–663)

이 식을 0에서 ∞까지 적분 (대사체 초기·말기 0):

$$\boxed{\frac{AUC(m)}{AUC} = \frac{CL_f}{CL(m)}}$$

`CL_f = fm · CL` 대입:

$$\boxed{\frac{AUC(m)}{AUC} = fm \cdot \frac{CL}{CL(m)} = fm \cdot \frac{\text{Clearance of drug}}{\text{Clearance of metabolite}}}$$

**이 단순한 비가 본 카드 전체의 압축**:
- AUC 비 > 1 + fm 알려져 있음 → CL(m) < CL (대사체가 *더 천천히* 청소됨).
- AUC 비 < 1 → CL(m) ≥ CL/fm — 대사체가 *더 빨리* 청소.
- 두 양 중 하나만 알면 다른 하나 결정.

#### Methylprednisolone hemisuccinate 사례 (Tozer Fig 20-2, p.662)

i.v. ester(parent) 80mg 후:
- AUC(ester) = 2.1 mg·hr/L
- AUC(methylprednisolone) = 3.9 mg·hr/L  ← 더 큼!
- fm ≈ 1 (가수분해 빠르고 거의 완전).
- 결론: AUC 비 > 1, fm = 1 → **CL(m) < CL(ester)**. Methylprednisolone이 *더 천천히* 청소.

→ V나 t1/2를 *전혀* 몰라도 두 청소율의 *대소관계*는 정확히 결정.

#### Tolbutamide / hydroxytolbutamide 사례 (Tozer Fig 20-4, p.665)

- Tolbutamide t1/2 = 4 hr.
- 거의 전 dose가 hydroxytolbutamide로 대사 (urinary recovery 검증, fm ≈ 1).
- AUC 비 ≈ 1/20 (parent / metabolite 약 20배).

→ fm ≈ 1, AUC 비 ≈ 0.05 → **CL(m) / CL ≈ 20** → 대사체가 *훨씬 빠르게* 청소. 대사체 농도가 임상적으로 의미 있는 농도에 절대 도달 못 함.

#### 모-자 rate constant 비 (Tozer Eq 20-7, p.664)

$$\boxed{\frac{k(m)}{k} = \frac{CL(m)/CL}{V(m)/V}}$$

**메시지**: rate constant 비는 단순 CL 비가 아니라 V로 normalize.
- CL(m) > CL이지만 V(m) < V이면 → k(m) >> k.
- Naphthoxylactic acid 사례에서 핵심.

#### Propranolol / naphthoxylactic acid 사례 (Tozer Fig 20-3, p.663)

i.v. propranolol 후:
- Plasma AUC(naphthoxylactic acid) > AUC(propranolol)에도 불구하고 농도-시간 곡선 *parallel* decay.
- 추론 1: Parallel decay → formation rate-limited (자세히 → M17).
- 추론 2: AUC 비 + 알려진 fm < 1 → CL(naphthoxylactic acid) < CL(propranolol).
- 추론 3: 농도(metabolite) >> 농도(propranolol) (Fig 20-3). 이건 **V(m) << V**일 때만 가능.
- 결론: V(m)/V가 CL(m)/CL보다 *훨씬* 작아 k(m) > k가 됨에도 *parallel decay* 발생 (k_f < k가 강한 통제력).

> "The volumes of distribution of basic parent drugs are often in excess of 100 L (1.4 L/kg), whereas those of their acidic metabolites are closer to 10 to 20 L (0.14–0.30 L/kg)" (Tozer p.664). 이 *V(m) << V* 패턴이 basic parent → acidic metabolite의 *전형*.

#### PopPK 함의

NONMEM에서 parent-metabolite 모델 코딩의 핵심:
1. **추정**: CL_f, CL(m), V(m) (primary).
2. **Derived**: AUC 비, k(m), fm (만약 데이터로 식별 불가하면 fm은 *외부 정보*로 고정).
3. **데이터 한계**: parent + metabolite 동시 측정 + i.v. 투여 *둘 다* 있어야 fm 식별 가능. 그렇지 않으면 fm·CL(m)이 *합쳐서만* 식별.

#### Trench-Level Tip — fm 식별성

<!-- TRENCH -->
**현장 팁**: Active metabolite PopPK 모델에서 fm을 *별도 추정 파라미터*로 두지 말고, 가능하면 **별도 i.v. metabolite study에서 측정한 CL(m)** 으로 *고정*하고 모-자 동시 fitting. fm·CL(m)이 곱으로만 식별되는 경우, fm 추정 시 SE가 *비현실적으로 큼* → ETA에 흡수되어 전체 정밀도 붕괴. Tozer Eq 20-13의 `AUC(m)_single = F(m)·Dose/CL(m)`이 별도 metabolite 투여 후 CL(m) 추정의 직접 식이며, AIMS BioScience consulting에서 *반드시 두 번의 별도 i.v. study*를 요구해야 하는 이유 [확인 필요 — 본 PDF 범위 외 NONMEM 실무 추론].

<!-- ANCHOR -->
**다음**: 위 식들은 *모든* 모자식 시스템에 적용. 그러나 농도-시간 *프로파일의 모양*은 **rate-limiting step**에 따라 정성적으로 다름 → M17.

---

### M17. Rate-Limiting Step in Metabolite Disposition — *Tozer Ch.20 신규*

<!-- MASTER LENS -->
**Big Idea**: 모자식 시스템 농도-시간 곡선은 *어느 단계가 율속*이냐에 따라 두 가지로 갈린다. **Case A (formation rate-limited; k << k(m))**에서 대사체는 parent와 *parallel*하게 decay하며, **t1/2(metabolite) = t1/2(parent)** — 그러나 이 t1/2는 metabolite *본래* t1/2가 *아니다* (별도 i.v. metabolite 시 더 짧음). **Case B (elimination rate-limited; k(m) << k)**에서 대사체는 parent보다 *늦게* peak에 도달하고 *훨씬 천천히* decay하며, **t1/2(metabolite)는 metabolite 본래 t1/2**. 두 case의 구분은 농도-시간 plot 한 장으로 결정되며, *NONMEM 모델 구조 선택과 신부전 시 metabolite 축적 예측의 출발점*.

#### 핵심 원칙 (Tozer p.661)

> "Substances formed beyond the rate-limiting step decline with the half-life of this slowest step."

이 한 문장이 본 카드의 압축. Sequential한 elimination chain에서 *어떤 시점에 형성된 substance든* 그 시점부터의 decay는 *chain 내 가장 느린 단계*의 t1/2를 따른다.

#### 두 case의 진단 (Tozer Fig 20-1, p.660)

| 특징 | **Case A**: k << k(m) (formation RL) | **Case B**: k(m) << k (elimination RL) |
|------|-----|-----|
| 농도 곡선 (semilog) | parent와 *parallel* decay | metabolite가 parent보다 *훨씬 느리게* |
| Metabolite peak time | parent peak 가깝거나 직후 | parent가 거의 사라진 *훨씬 후* |
| Amount(metabolite) 절대값 | 대부분 시점에서 < amount(parent) | Metabolite peak 후 amount > parent |
| Metabolite t1/2 (관찰) | parent의 t1/2 — *metabolite 본래 t1/2가 아님* | metabolite *본래* t1/2 |
| 대표 예 | propranolol → naphthoxylactic acid; tolbutamide → hydroxytolbutamide | methylprednisolone hemisuccinate → methylprednisolone |
| 흔함 | 흔한 경우 ("the most common situation"; p.660) | 드문 경우, 주로 *prodrug* |

#### Case A의 정량 결과 (Eq 20-2, 20-3, p.661)

Formation rate-limited에서 quasi-steady state:

$$k(m) \cdot A(m) \approx k_f \cdot A$$

$$\boxed{A(m) \approx \frac{k_f}{k(m)} \cdot A = \frac{fm \cdot k}{k(m)} \cdot A}$$

*서명*: 대사체 양은 parent 양에 *비례적으로 묶임*. Parent가 줄면 metabolite도 같은 비율로 줄어든다.

> 중요: 이 등식은 *근사*. 엄밀히는 elimination rate가 formation rate를 약간 초과해야 metabolite amount 감소. 그러나 그 차이가 매우 작아 *비례 관계*가 시간 내내 유지.

#### Case B의 정량 결과

Elimination rate-limited에서 parent 대사가 끝난 후 metabolite는 자기 자신의 first-order decay:

$$A(m, t) = A(m, t^*) \cdot e^{-k(m) \cdot (t - t^*)}$$

t* = parent가 거의 사라진 시점.

#### Case A가 *흔한* 이유 — Volume과 Clearance의 mirror image

Tozer p.664가 명시:

> "Basic parent drugs are often in excess of 100 L (1.4 L/kg), whereas those of their acidic metabolites are closer to 10 to 20 L (0.14–0.30 L/kg). These metabolites... bound more strongly to albumin, thereby further restricting their tissue distribution."

즉:
- Basic parent → acidic metabolite: 매우 흔함 (propranolol → naphthoxylactic acid).
- V(parent) ~ 5–10× V(metabolite).
- CL(parent) < CL(metabolite) (대사체가 더 polar → 더 빠른 신청소).
- 결과: k(m) = CL(m)/V(m)이 *분자 분모 모두* parent보다 큰 방향 → k(m) >> k → **formation rate-limited**.

이것이 "왜 Case A가 더 흔한가"의 *생리화학적* 근거.

#### Case B의 elegant 사례: Methylprednisolone hemisuccinate (Fig 20-2, p.662)

- Hemisuccinate ester는 esterase로 매우 빠르게 가수분해 (t1/2 = 0.25 hr).
- Methylprednisolone (metabolite)은 t1/2 = 2.7 hr — *훨씬 느림*.
- Parent (ester)가 1–2 hr 만에 거의 사라진 후, metabolite는 자기 t1/2 = 2.7 hr로 decay.
- 이 case가 **prodrug의 약리학적 정수**: 활성 약물(methylprednisolone)을 *수용성 ester*로 i.v. → 빠른 가수분해 → 활성 약물이 천천히 elimination.

#### Sequential chain 일반화 (p.661)

```
A → B → E → G → H → I → J
   k₁  k₂  k₃  k₄  k₅  k₆
```

만약 k₃ = 0.05 hr⁻¹ (가장 작음)이고 다른 k는 모두 ≥ 0.5 hr⁻¹ → **G가 율속**:
- A, B, E의 terminal t1/2: 자체의 fastest k.
- G, H, I의 terminal t1/2: 모두 t1/2 = 0.693/0.05 = 13.9 hr.

**원칙**: chain 내 *어떤 species든* 그 t1/2는 *fastest decay path*에 의해 결정. 형성 단계가 그 path보다 느리면, 형성 단계가 율속.

#### 모자식 t1/2가 거의 같을 때 — 중간 case

Parent와 metabolite의 본래 t1/2가 비슷하면 어느 단계도 명확히 율속이 아님:
- Metabolite는 *본래 t1/2*보다 약간 *느리게* decay (parent가 일부 남아 형성 유지).
- 정확한 거동은 모-자 미분방정식 시스템의 수치해.

#### NONMEM 코딩 — Case A vs Case B 모델 구조

**Case A (formation rate-limited)**:
```
$PK
CL  = THETA(1) * EXP(ETA(1))   ; parent total CL
V   = THETA(2) * EXP(ETA(2))   ; parent V
FM  = THETA(3)                 ; fixed (외부 정보)
CLM = THETA(4) * EXP(ETA(3))   ; metabolite CL
VM  = THETA(5) * EXP(ETA(4))   ; metabolite V

K   = CL/V
KM  = CLM/VM
KF  = FM * K

$DES
DADT(1) = -K  * A(1)
DADT(2) = KF * A(1) - KM * A(2)
```

식별성: `KF · V`와 `KM · VM`이 데이터에 강하게 묶이지만, fm 자체는 *별도 i.v. metabolite study* 없이 분리 어려움.

**Case B**: 모델 구조 동일. KM이 작아 metabolite terminal phase가 자기 t1/2를 보임 → KM 추정 정밀도 *훨씬 높음*.

#### Confusion 경고

<!-- CONFUSION -->
**Confusion (M17.a)**: "Metabolite 관찰 t1/2 = 5 hr"이라는 보고에서, 이 5 hr가 metabolite *자신의* t1/2인가, 아니면 parent에 *묶인* t1/2인가? 답: case에 따라. Case A이면 5 hr는 parent t1/2이고 metabolite 본래 t1/2는 *훨씬 짧음*. Case B이면 5 hr가 본래. **별도 i.v. metabolite 투여 study가 결정적** — 별도 study에서 metabolite t1/2가 1 hr면 Case A 확정.

#### Trench-Level Tip — 신부전 시 metabolite 축적 예측

<!-- TRENCH -->
**현장 팁**: Active metabolite 신부전 dose 결정 시, *반드시* rate-limiting step 먼저 진단. **Case A**: metabolite 축적의 *상한*은 parent 축적에 묶임 → parent CL 보정만으로 metabolite 노출도 자동 보정. **Case B**: metabolite는 *자기 t1/2*로 누적 → parent CL과 *별도로* metabolite CL 보정 필요. 후자 무시되면 metabolite *수배* 축적 → 독성. procainamide·morphine의 임상 함정 (자세히 → M20).

<!-- ANCHOR -->
**다음**: 모자식에서 *경구* 투여 시 first-pass의 영향 → M18.

---

### M18. First-Pass Impact on Metabolite Disposition — *Tozer Ch.20 신규*

<!-- MASTER LENS -->
**Big Idea**: 고추출 약물을 oral로 주는 것은 사실상 **약물 + 대사체 cocktail**을 i.v. 투여하는 것과 같다. Propranolol을 80 mg 경구로 주면 21%만 혈류에 propranolol로 도달하고, *79%가 이미 대사체로* 간을 빠져나오면서 systemic으로 들어간다. 이 단순한 사실이 활성 대사체를 가진 약물(prodrug, propranolol, morphine, codeine)의 *경구 투여 후 효과*가 *i.v. 투여 후 효과보다 더 빠르고 더 강한* 이유다. PopPK에서 *경로 의존적 대사체 데이터*는 hepatic vs extrahepatic 대사 부위를 *진단하는* 강력한 도구이기도 하다.

#### 경구 시 metabolite 두 source (Tozer Fig 20-6, p.667)

```
                  ┌─→ Drug (absorbed) ─→ ...
Drug oral ──→ Liver
                  └─→ Metabolite formed during absorption ─→ systemic
                            (first-pass formation)

         Drug in body ──→ Metabolite formed from absorbed drug
                            (post-absorption formation)
```

**Total metabolite plasma = first-pass formation + post-absorption formation**.

#### 고추출 parent 정량 결과 (Fig 20-5, p.666)

Propranolol 20 mg 경구 vs i.v.:

| 측정값 | i.v. | Oral |
|--------|------|------|
| Propranolol AUC | (reference) | ~0.21 × i.v. |
| Naphthoxylactic acid AUC | (i.v. 후 형성) | *similar* (per dose 보정) |
| Metabolite/parent 농도 비 | 낮음 | **훨씬 높음** |
| Metabolite peak time | 1.5–2 hr | parent와 *동시 또는 더 일찍* |

**핵심**:
- 경구 시 metabolite가 *parent보다* 빠르게 peak.
- First-pass에서 형성된 metabolite는 *i.v. metabolite 투여*와 동등한 거동.
- **Total metabolite 곡선은 두 source의 합** — 첫 통과 (빠른 entry, metabolite 본래 t1/2로 decay) + 흡수 후 (parent 묶인 거동).

#### 진단 도구: AUC(m)의 경로 의존성

**규칙** (p.667):
- Metabolite가 *간에서만* 형성되고 모든 parent가 GI wall 통과 → **AUC(m)이 oral과 i.v. 사이에서 동일** (per-dose 보정 후).
- Metabolite가 *gut wall이나 lumen*에서도 형성 → **AUC(m)이 oral 후 더 큼**.

#### Tozer 검증 #1 — Morphine (Fig 20-7, p.668)

Morphine 10 mg dose-equivalent:
- Morphine itself: oral F = 0.21 (높은 first-pass).
- Morphine-6-glucuronide AUC: **oral과 i.v.에서 거의 동일**.

→ 결론: morphine 낮은 oral F는 *간*에서 (gut wall 아님). Metabolite 거의 전적으로 hepatic origin.

→ 임상 함의: i.v.에서 oral 전환 시, *metabolite 활성*을 고려하면 dose 비율이 단순 1/F = 5배가 *아니라* 더 작아짐. 활성 metabolite가 oral에서 거의 동일하게 entry.

#### Tozer 검증 #2 — Isoproterenol (Table 20-3, p.669)

| Route | Isoproterenol | Iso-conjugate | O-Methyl-iso | O-Methyl-conjugate |
|-------|---------------|---------------|--------------|---------------------|
| i.v. | 62.2% | 0% | 13.0% | 24.8% |
| Oral | 6.3% | **62.0%** | 5.6% | 1.3% |

**핵심**: 경구에서 conjugate가 *압도적*. i.v. 후 conjugate 0% — 두 경로 패턴이 *질적으로 다름*.

**진단**: Conjugation이 *gut wall*에서 first-pass로 우세. i.v. 시 다른 경로 (catechol-O-methyltransferase, monoamine oxidase) 우세.

→ Isoproterenol PopPK는 oral과 i.v.에서 *완전히 다른 모델 구조* 필요.

#### Therapeutic 함의 — Active metabolite + first-pass의 4 조합

| Parent | Metabolite | First-pass | 임상 결과 |
|--------|------------|------------|-----------|
| Active | Inactive | High | Oral F 낮음 → high oral dose. Effect parent에 묶임. |
| Inactive | Active | High | **Prodrug** — oral이 i.v.보다 *효과적*. |
| Active | Active | High | **Combination** — oral이 *빠르고 강한 onset* (propranolol). |
| Active | Active | Low | i.v. ≈ oral. |

#### Propranolol 임상 관찰 (p.666–667)

> "Following a single oral dose, the pharmacologic effect is maximal at the peak propranolol concentration, but for a given plasma concentration of propranolol, the response seen after an oral dose is greater than that observed following an i.v. dose. The explanation appears to be the presence of a significant concentration of one or more pharmacologically active metabolites, formed on the first pass through the liver. Certainly, one identified metabolite, 4-hydroxypropranolol, is as active as propranolol."

→ **"plasma propranolol 농도만으로 효과 모델링하면 oral과 i.v.에서 *다른* PK-PD"** 임상 paradox의 메커니즘. Active metabolite 모델 포함해야 일관된 PK-PD.

#### Trench-Level Tip — Oral 약물 PopPK 모델 설계

<!-- TRENCH -->
**현장 팁**: Active metabolite + high-extraction 약물의 oral PopPK는 *반드시* `First-pass formation`을 별도 컴파트먼트로:

```
$MODEL
COMP=(DEPOT)        ; oral dose
COMP=(CENTRAL)      ; parent
COMP=(CENTRAL_M)    ; metabolite

$PK
KA  = THETA(1) * EXP(ETA(1))
F1  = THETA(2)              ; oral F of parent
FH  = THETA(3)              ; hepatic availability
FM_FP = (1-FH) * THETA(4)   ; fraction first-pass formation → systemic

$DES
DADT(DEPOT)    = -KA * A(DEPOT)
DADT(CENTRAL)  =  KA * F1 * A(DEPOT) - K * A(CENTRAL)
DADT(CENTRAL_M)= KA * FM_FP * A(DEPOT) + KF * A(CENTRAL) - KM * A(CENTRAL_M)
```

이게 **두 metabolite source 분리** NONMEM 표준. 단순 `KF * A(CENTRAL)`만 두면 first-pass missed → metabolite peak time *더 늦게* 예측되어 misfit.

> **CONTEXT 흡수 — App.E oral first-principles (Tozer p.779, Eq E-16 ~ E-20)**: hepatic extraction이 oral 손실의 유일한 원인이라는 가정 + Eq E-13 + universal NCA 관계 (`F·Dose = CL·AUC_po`)에서 algebraic 단순화 → 다음 *주목할 만한 결론*:
>
> $$\boxed{AUC_{po} = \frac{Dose}{f_{ub} \cdot \rho \cdot CL_{int}} \quad \text{(Eq E-19, 단회);} \quad AUC_{ss,po} = \frac{Dose}{f_{ub} \cdot \rho \cdot CL_{int}} \quad \text{(Eq E-20, 만성 plateau)}}$$
>
> **Oral AUC가 hepatic blood flow Q_H에 완전히 무관** — 운동/sepsis/심부전 등 Q_H 변동 시 i.v.는 변동하지만 oral은 무변. 4 결정자 (fub, ρ, CLint, Dose) 중 *어느 것이 변하든* AUC에 직접 영향. **임상 함의**: 단백결합 변동 (fub) + transporter inhibition (ρ) + CYP DDI (CLint)이 *각각 독립적으로 작용하면 곱셈* — cyclosporine+simvastatin 같은 dual-mechanism inhibitor에서 AUC가 *수배* 증가 가능 (rhabdomyolysis 위험). Tozer Ch.20 Eq 20-15와 결합하면 metabolite oral plateau = `(fm × Dose) / (fub × ρ × CLm,int × τ)` — Step 3+4의 통합 결과식.

#### Trench-Level Tip — Oral DDI 시뮬레이션

<!-- TRENCH -->
**현장 팁**: Oral 약물 DDI 시뮬레이션 보고서 받으면 *반드시* (1) ρ 변화 (uptake/efflux transporter inhibition), (2) CLint 변화 (CYP inhibition/induction), (3) fub 변화 (단백결합 displacement) — 세 메커니즘을 *각각 분리*해서 평가했는지 확인. *곱셈 효과*가 가장 큰 임상 위험 — 단일 메커니즘만 평가한 보고서는 *under-conservative*. AIMS BioScience DDI 분석 표준 [확인 필요 — 본 PDF 범위 외].

<!-- ANCHOR -->
**다음**: 만성 투약 *plateau* + *time to plateau* → M19.

---

### M19. Steady-State Metabolite Concentration & Multiple-Dose Prediction — *Tozer Ch.20 신규*

<!-- MASTER LENS -->
**Big Idea**: 만성 투약의 가장 중요한 두 양은 (1) plateau metabolite 농도, (2) plateau 도달 시간. **Plateau 농도는 fm·R_inf/CL(m)** — *세 가지* 양으로 결정. **Plateau 도달 시간은 두 t1/2 중 *긴 쪽*에 의해 결정** — metabolite t1/2가 parent보다 길면 metabolite가 한참 후에야 plateau (N-desalkylhalazepam). Multiple-dose 거동은 single-dose AUC(m)만으로 *예측 가능* (Eq 20-15, superposition). 이 식들이 active metabolite 약물의 만성 처방 *안전성* 평가의 직접 도구.

#### Constant-Rate Infusion: 정상상태

i.v. infusion rate R_inf. Plateau에서 형성·소실 균형:

$$fm \cdot R_{inf} = CL(m) \cdot C(m)_{ss}$$

(Tozer Eq 20-12, p.670):

$$\boxed{C(m)_{ss} = \frac{fm \cdot R_{inf}}{CL(m)}}$$

Amount-based (Eq 20-11):

$$A(m)_{ss} = \frac{fm \cdot R_{inf}}{k(m)}$$

#### 수치 예제 (p.670)

R_inf = 5 mg/hr, fm = 0.5, k(m) = 0.1 hr⁻¹, CL(m) = 1.0 L/hr:

$$A(m)_{ss} = \frac{0.5 \cdot 5}{0.1} = 25 \text{ mg}$$
$$C(m)_{ss} = \frac{0.5 \cdot 5}{1.0} = 2.5 \text{ mg/L}$$

#### Time to Plateau — 두 시나리오

**시나리오 1: Bolus + Infusion (constant parent 즉시 달성)**

Parent 농도가 t=0부터 상수 → metabolite formation rate 상수 → metabolite는 *자기 자신의 t1/2*로 plateau 접근.

→ **Time to plateau = metabolite t1/2** (3.3 t1/2(metabolite) for 90%).

**시나리오 2: Infusion alone (no loading)**

Tozer Fig 20-8 두 sub-case:

- **Case A (parent t1/2 > metabolite t1/2; 흔한 경우)**:
  - Parent가 자기 t1/2로 plateau 접근.
  - Metabolite는 formation rate-limited → parent에 *비례적으로 묶임*.
  - **Metabolite plateau = parent t1/2**.
  - 4 × t1/2(parent)에서 95%.

- **Case B (parent t1/2 < metabolite t1/2; 드뭄)**:
  - Parent가 *먼저* plateau (metabolite는 거의 안 올라감).
  - 그 후 parent 일정 → metabolite formation rate 상수 → metabolite는 자기 t1/2로 plateau.
  - **Metabolite plateau = metabolite t1/2**.

**압축 규칙**: Metabolite plateau time = max(t1/2 parent, t1/2 metabolite).

#### Postinfusion Decline

- Case A: parent 천천히 사라짐 → metabolite 형성 천천히 감소 → metabolite도 parent t1/2.
- Case B: parent 빠르게 사라짐 → metabolite는 자기 t1/2로 decay.
- 일반: postinfusion decline = *둘 중 더 긴 t1/2*.

#### Multiple-Dose Oral Regimen

만성 oral plateau는 single-dose AUC(m)로부터 *직접* 예측 (superposition):

$$AUC(m)_{single} = \frac{F(m) \cdot Dose}{CL(m)}$$ (Tozer Eq 20-13, p.672)

여기서 F(m) = oral dose 중 systemic metabolite로 entry되는 분율.

만성 plateau 평균 (dosing interval τ):

$$C(m)_{av,ss} = \frac{F(m) \cdot Dose}{\tau \cdot CL(m)}$$ (Eq 20-14)

두 식 결합 → **Tozer Eq 20-15** (p.673):

$$\boxed{C(m)_{av,ss} = \frac{AUC(m)_{single}}{\tau}}$$

**이 식이 본 카드의 *임상적으로 가장 유용한* 한 줄**: 단일 oral dose의 metabolite AUC만 측정하면 *어떤 dosing regimen*의 plateau metabolite 평균 농도를 *즉시* 계산 가능. CL(m), F(m), fm 모두 *몰라도* 됨.

**예**: AUC(m)_single = 120 mg·hr/L (100 mg single dose), 12 hr 간격 → C(m)_av,ss = 120/12 = 10 mg/L.

#### N-Desalkylhalazepam 사례 (Fig 20-9, p.672)

Halazepam 10 mg every 8 hr × 13일:
- Halazepam (parent) plateau에 빠르게 도달.
- N-Desalkylhalazepam (metabolite) plateau에 *훨씬 늦게* — 5–10일.
- Plateau에서 metabolite 농도 > parent 농도 (CL(m) 더 작음).
- 투약 중지 후 metabolite는 parent보다 *훨씬 천천히* decay.

**임상**: Halazepam의 약리 효과는 N-desalkylhalazepam에 묶임. 만성 중지 후 효과(과 부작용)가 *수일~수주* 지속. Long-acting benzodiazepine 패밀리의 *임상적 특이성*.

#### CONTEXT 흡수 — Carbamazepine Autoinduction (Fig 20-11, p.676)

Carbamazepine은 자기 metabolism을 induce ("autoinduction"):
- Daily dose 100 → 1200 mg 시 plasma C_av,ss는 *비례 안 함* (sub-proportional).
- C(metabolite)/C(parent) 비는 dose에 *증가*.

**해석**: dose 증가 → formation pathway induced → CL_f 증가 → AUC(m)/AUC 증가.

**PopPK 함의**: Time-varying CL 모델링 필수 — `CL(t) = CL_baseline · (1 + Imax·time/(T50+time))`.

#### Trench-Level Tip — Active metabolite 만성 dosing 안전성

<!-- TRENCH -->
**현장 팁**: Active metabolite 신약의 phase 1 single-dose study에서 *반드시* AUC(m) 측정, 만성 dosing 시 예상 plateau를 Eq 20-15로 계산. metabolite 활성·독성 prior가 있으면 (hERG 차단 등), plateau 농도가 *toxic threshold 넘는지* 사전 평가. Phase 2/3 design에서 dosing interval과 maximum dose 결정의 *수식적* 출발점 — 단일 dose만으로 만성 안전성을 *합리적* 예측하는 유일한 도구. AIMS BioScience active metabolite consulting 표준 [확인 필요 — 본 PDF에 specific 사례 미명시; 추론].

<!-- ANCHOR -->
**다음**: 신부전에서는 어떻게 변하는가? Active metabolite가 *주로 신청소*될 때 *13배* 노출 오류 → §1 dilemma 완성형 → M20.

---

### M20. 신기능 저하 시 대사체 축적 — Dose Adjustment 시나리오 + Interconversion — *Tozer Ch.20 신규*

<!-- MASTER LENS -->
**Big Idea**: §1 도입의 fe = 0.35 dilemma는 사실 *불완전*했다. 진짜 임상 dilemma는 **active metabolite 약물의 신부전 dose 조절**이다. Tozer p.674 워크드 예제에서, parent의 *fe만 0.5*인 약물(신청소가 절반)이 신부전 환자에서 농도 2배 증가에 그치는데, 동일 환자에서 *active metabolite* 농도는 *13배* 증가한다. 활성 합산하면 단순 parent 분석은 dose를 약 1.4배 *과대* — anuric 환자에서 표준 dose의 14% (약 1/7)만. procainamide·morphine·prednisone에서 임상의가 만나는 함정. 또한 *interconversion*(parent ↔ metabolite 양방향 전환)이 있는 약물 — clofibric acid·prednisone — 에서 metabolite 신청소 차단이 *parent의 effective CL*까지 감소시키는 *간접* 메커니즘이 추가된다.

#### 워크드 예제 — Tozer p.673–675 (Fig 20-10, Table 20-4)

가상 약물 정상 신기능 (Table 20-4):

| Parameter | Drug | Active Metabolite |
|-----------|------|-------------------|
| Total CL | 30 L/hr | 10 L/hr |
| Renal CL | 15 L/hr | 8.5 L/hr |
| fe (정상) | 0.5 | 0.85 |
| Oral F | 0.8 | 0.3 (= fm of parent) |

투약: 10 mg/hr, drug·metabolite *equipotent + additive*.

**정상 환자 정상상태**:

$$C_{av,ss} = \frac{0.8 \cdot 10}{30} = 0.27 \text{ mg/L}$$
$$C(m)_{av,ss} = \frac{0.3 \cdot 0.8 \cdot 10}{10} = 0.24 \text{ mg/L}$$

총 활성 = 0.27 + 0.24 = 0.51 mg/L.

**Anuric 환자 (renal CL = 0)**:

Drug extrarenal CL = 30 − 15 = 15 L/hr.

$$C(d)_{av,ss} = \frac{0.8 \cdot 10}{15} = 0.53 \text{ mg/L}$$

→ 정상 대비 **2배** (parent만 보면).

**중요한 변화**: anuric 환자에서 parent의 elimination 경로가 바뀜. fe(parent) = 0.5의 50%가 *모두 active metabolite formation으로 redistributed* → fm: 0.3 → 0.6 (Tozer Fig 20-10 시나리오).

→ Anuric metabolite formation:

$$\text{Rate of formation} = 0.6 \cdot 0.8 \cdot 10 = 4.8 \text{ mg/hr}$$

Metabolite extrarenal CL = 10 − 8.5 = 1.5 L/hr.

$$C(m,d)_{av,ss} = \frac{0.6 \cdot 0.8 \cdot 10}{1.5} = 3.2 \text{ mg/L}$$

→ 정상 대비 **13배 증가**!

총 활성 in anuric: 0.53 + 3.2 = 3.73 mg/L.

**Dose 조절 비**:

$$\frac{\text{Anuric dose}}{\text{Normal dose}} = \frac{0.51}{3.73} \approx 0.14$$

→ Anuric 환자에서 **약 1/7 dose** — 즉 1.4 mg/hr.

#### 시나리오별 dose 조절 결정 트리 (Tozer p.675)

**시나리오 A — Metabolite formation이 parent 주 elimination 경로 + metabolite는 비신경로**:
- fm → 1, fe(m) → 0.
- 신부전이 *parent CL이나 metabolite CL 모두 거의 영향 없음*.
- → **Dose 조절 불필요**.

**시나리오 B — Parent 신청소 minor + active metabolite가 거의 전적 신청소**:
- fe(parent) 작음, fm 작음, **fe(m) → 1**.
- 신부전이 parent CL 거의 영향 없지만, **metabolite CL 격감**.
- → **Metabolite polynomially 축적** → dose *반드시 감소*.
- 가장 위험 — 임상의가 parent CL만 보고 "괜찮다"고 결론.

**시나리오 C — 양쪽 일부**:
- 워크드 예제 같은 중간 case. 정량 계산 필수.

#### 임상 사례 — Procainamide / NAPA

(Study Problem 3, p.683):
- Procainamide: fe ~ 50%, hepatic acetylation으로 NAPA 형성.
- NAPA: 거의 전적 renal excretion, *intrinsic antiarrhythmic 활성*.
- 정상: NAPA/procainamide plasma 비 ~ 0.5–2.
- 신부전: NAPA/procainamide 비 *5–6까지 증가* — Fig 20-14.

**임상 함의**: 신부전에서 procainamide만으로 *총 항부정맥 효과* 평가 불가. *반드시* NAPA 측정. 임상 모니터링이 "parent + NAPA"로 표준인 *수식적* 이유.

#### Interconversion — *간접* 신부전 영향 (p.676–679, Fig 20-13)

일부 약물은 parent ↔ metabolite *양방향* 전환. Tozer Table 20-5 핵심 페어:

| Parent | Metabolite | Equilibrium |
|--------|------------|-------------|
| Prednisone | Prednisolone (active) | Prednisolone 우세 |
| Cortisol | Cortisone | Cortisol 우세 |
| Sulindac (inactive) | Sulindac sulfide (active) | Sulfide 우세 (prodrug) |
| Lovastatin (lactone) | Lovastatin acid (active) | Open acid (활성형) |
| Clofibric acid | Clofibric acid glucuronide | Clofibric acid 우세 |

#### Clofibric Acid — *간접 신부전 효과*의 elegant 예 (Fig 20-13, p.679)

- 정상: clofibric acid의 fe ≈ 0.06 (매우 작음).
- *naïve 추론*: 신부전에서 clofibric acid 농도 거의 변화 없을 것.
- **실제** (Fig 20-13): serum creatinine 1 → 10 mg/dL (GFR 100 → 10 mL/min)에서 clofibric acid의 unbound CL이 **~250 → ~30 mL/min** (약 8배 감소!).

**메커니즘** (p.679):
1. Clofibric acid → glucuronide via 간 conjugation (활발).
2. Glucuronide는 거의 전적 신청소 (fe[glucuronide] → 1).
3. 신부전 → glucuronide 축적.
4. **Glucuronide → clofibric acid 가수분해 (interconversion)** — esterase에 의해 plasma/장에서.
5. → Effective clofibric acid CL 감소 (*nominally* parent 신청소 무관).

→ "fe(parent) = 0.06"만 보고 "신부전 안전"이라 결론 시 **8배 노출 오류**. Interconversion + glucuronide 신청소 의존성 *간접* 효과.

**일반 원리**: 약물이 어떤 대사체와 interconvert + 그 대사체가 신청소 → 신부전 시 대사체 축적 → 역가수분해 → parent의 *effective elimination* 감소. ester glucuronides (clofibric acid, ciprofibrate, ketoprofen)에서 흔함. Ether glucuronides는 가수분해 안 됨 *없음*.

#### Tozer p.682 AUC Diagnostics — 4 possibilities (CONTEXT)

Oral 약물 plasma 농도가 *Occasion B에서 감소*하는 관찰의 *원인 진단*. AUC(m)/AUC 비 거동으로 4 가능성 구분:

| 원인 | AUC(B)/AUC(A) | AUC(m)(B)/AUC(m)(A) | [AUC(m)/AUC]_B vs A |
|------|----------------|----------------------|----------------------|
| 1. 흡수 감소 (incomplete dissolution) | < 1 | < 1 (동일 비율) | 같음 |
| 2a. fu 증가 (단백결합 감소; CL_f 비례 ↑) | < 1 | 무변 (CL_m 무변) | **B > A** |
| 2b1. 효소 유도 (formation pathway만) | < 1 | 무변 | **B > A** |
| 2b2. 효소 유도 (다른 pathway) | < 1 | < 1 | 같음 |
| 2c. 신청소 증가 | < 1 | < 1 | 같음 |

**결정 트리**:
- AUC(m)/AUC 비 *증가* → 단백결합 감소 또는 formation enzyme 유도.
- 비 *동일* → 흡수 문제, 다른 pathway 유도, 또는 신청소 증가.

이 진단 표가 "왜 이 환자 plasma 농도가 떨어졌는가?"의 *증거 기반* 답. PopPK ETA 흡수 대신 *covariate 명시*하기 위한 출발점.

#### NONMEM — Active metabolite + 신부전 covariate

```
$PK
; Parent
CL_R   = THETA(1) * (CRCL/120)
CL_NR  = THETA(2)
CL     = CL_R + CL_NR

; Metabolite formation (assuming fm increases as renal pathway shut)
FE     = CL_R / CL
FM     = THETA(3) + (1 - FE) * THETA(4)   ; reroute to metabolite
CLF    = FM * CL

; Metabolite (mostly renal cleared)
CLM_R  = THETA(5) * (CRCL/120)
CLM_NR = THETA(6)
CLM    = CLM_R + CLM_NR

V      = THETA(7) * EXP(ETA(1))
VM     = THETA(8) * EXP(ETA(2))

$DES
DADT(CENT)   = -CL/V * A(CENT)
DADT(CENT_M) = CLF/V * A(CENT) - CLM/VM * A(CENT_M)
```

**핵심 covariate**: CRCL이 parent CL과 metabolite CL *둘 다*에. ETA에만 의존하면 신부전 코호트 metabolite 축적 *체계적 패턴* 잃음.

#### Trench-Level Tip — Active metabolite 신약 phase 1 결정 트리

<!-- TRENCH -->
**현장 팁**: Active metabolite 신약의 phase 1 SAD에서 신부전 코호트 *반드시* 포함되어야 하는지 사전 평가:

1. **Step 1**: Parent fe < 0.3? Yes → step 2; No → standard renal impairment study 필요.
2. **Step 2**: Active metabolite 존재? Yes → step 3; No → 신부전 study minor.
3. **Step 3**: Metabolite fe(m) > 0.5? Yes → **반드시 신부전 study 필수** (시나리오 B); No → step 4.
4. **Step 4**: Interconversion 존재? (esterase 가수분해 가능?) Yes → 추가 검토; No → minor.

이 트리 무시되면 phase 3에서 *예상치 못한 독성* 노출. AIMS BioScience consulting active metabolite 신약 시 *반드시* phase 1 protocol design 전 4 step 검증 [확인 필요 — 본 PDF 범위 외 실무 추론].

<!-- ANCHOR -->
**§2 종결**: M1–M9 (Gabrielsson) + M10–M15 (Tozer Ch.5) + **M16–M20 (Tozer Ch.20)** = **20개 카드**. **이제 Tozer Ch.20 통합으로 새로 등장하는 confusion pairs 4개를 §5에 추가** → §5.

---

## §5 Confusion Pairs — 가장 자주 잘못 묶이는 개념 쌍

> *왜 둘이 닮아 보이는데 결정적으로 다른가*의 **구조적 이유**를 인코딩.

### Confusion Pair #1 — ARE plot vs Excretion Rate plot

<!-- CONFUSION -->
**닮은 점**: 둘 다 K를 slope로. 단일로그 plot 직선.

**다른 점**: ARE는 *남은* 양, Rate는 *순간* 배설속도.

**구조적 이유**: 시간 변동 — Rate는 instantaneous, ARE는 적분 → 평활. **소변 pH/혈류 변동 detection → Rate plot. Robust slope → ARE plot.** ARE는 X_u^∞ 정확 측정 필요. 방광 비완전 비움 — ARE 누적 편향.

### Confusion Pair #2 — Plasma CL vs Renal CL vs fe

<!-- CONFUSION -->
**닮은 점**: 단위 동일, dose+AUC로 추정.

**다른 점**: `Cl = Dose/AUC` (모든 경로), `ClR = X_u^∞/AUC` (신장만), `fe = ClR/Cl` (비율).

**구조적 이유**: **"Cl은 합, ClR은 부분, fe는 비율"**. 두 개 알면 세 번째 자동. fe < 0.1이면 simultaneous fit조차 ClR 안정 추정 불가.

### Confusion Pair #3 — Free fraction의 plasma vs blood

<!-- CONFUSION -->
**닮은 점**: 둘 다 "결합되지 않은 분율".

**다른 점**: f_u (또는 f_u,p) — 혈장. f_u,b — 전혈 (RBC 분배 포함).

**구조적 이유**: **Well-stirred는 *blood* 기준** (Gabrielsson p.79; Tozer p.135). plasma fu를 그대로 넣으면 hematocrit 무시. C_b/C_p ratio 결정자. *App.D Eq D-6 통합 완료 → Confusion Pair #14에 fu vs fub 정밀 처리*.

### Confusion Pair #4 — Highly cleared drug에서 IV vs Oral

<!-- CONFUSION -->
**닮은 점**: 동일 약물, fu, Cl_int.

**다른 점**:
| | Total Css | Unbound Css |
|---|---|---|
| **IV** | fu 무관 | **fu에 의존** ⚠️ |
| **Oral** | fu에 의존 | fu 무관 |

**구조적 이유**: **"Highly cleared IV는 unbound가 위험, oral은 total이 위험"**. IV: Q_H 결정 → fu 변동이 unbound에 직접. Oral: first-pass에서 fu·Cl_int → fu 약분.

### Confusion Pair #5 — Distributed model의 이질성 ↔ 수렴 방향

<!-- CONFUSION -->
**닮은 점**: spectrum 중간점.

**다른 점**: Distributed: ε² 작음 → parallel tube. ε² 큼 → well-stirred. Dispersion: D_N → 0 → parallel tube. D_N → ∞ → well-stirred.

**구조적 이유**: **"이질성·혼합 클수록 well-stirred에 수렴"**. well-stirred는 *결과 평균화* 조건. 이질성 극단 → 시간 평균 = well-stirred.

### Confusion Pair #6 — Single-point Cl_int illusion

<!-- CONFUSION -->
**닮은 점**: 수식 형태 동일.

**다른 점**: Single-point는 평탄화, multiple-point는 saturation 회복.

**구조적 이유**: **"Single-point는 한 점을 통과하는 *어떤* 직선이든 그릴 수 있다"**. 임상 농도 saturation이면 저용량 F 과대, 고용량 F 과소.

### Confusion Pair #7 — Plasma Clearance vs Blood Clearance — *Tozer Ch.5*

<!-- CONFUSION -->
**닮은 점**: 같은 elimination rate를 표현.

**다른 점**: Plasma CL은 혈장 농도 기준, Blood CL은 전혈 — *Extraction ratio 계산은 반드시 blood*.

**구조적 이유**: **"분류는 *blood* 기준에서만 유효"**. 1.3 L/min plasma CL은 겉보기에 Q_H 근접이지만, C/C_b = 0.1이면 blood CL = 0.13 L/min — 실은 저추출. 분류 정반대.

### Confusion Pair #8 — Total CL vs Renal CL vs Hepatic CL의 Additivity — *Tozer Ch.5*

<!-- CONFUSION -->
**닮은 점**: 모두 단위 동일.

**다른 점**: CL_total = CL_R + CL_H + CL_pulm + ... (additivity), 단 **CL_pulm은 예외** (직렬 위치).

**구조적 이유**: **"병렬 기관은 더해지고, 직렬 기관은 더해지지 않는다"**. 신/간 — 동맥혈 병렬. 폐 — 정맥혈 직렬.

### Confusion Pair #9 — Half-life 변화 ↔ 메커니즘 추론 — *Tozer Ch.5*

<!-- CONFUSION -->
**닮은 점**: t1/2 단축은 효소 유도/혈류 증가/biliary obstruction 모두 후보.

**구조적 이유**: **"t1/2 변화는 *질문*의 시작이지 *답*이 아니다"**. CL/V/fu/total vs unbound 4 질문. Derived parameter — 직접 메커니즘 안 가리킴.

---

### Confusion Pair #10 — fe (Renal Fraction) vs fm (Metabolite Fraction) — *Tozer Ch.20*

<!-- CONFUSION -->
**닮은 점**: 둘 다 dose의 *분율*. 둘 다 0–1 범위. 이름 비슷 (fe vs fm). 둘 다 신부전 dose 조절 핵심 변수.

**다른 점**: 
- **fe = ClR/CL** — 신장으로 *직접 unchanged 배설*되는 dose 분율.
- **fm = CLf/CL** — *active or inactive metabolite*로 변환되어 systemic으로 entry되는 분율.
- 한 약물의 fe + fm + (다른 직접 elimination) = 1.

**구조적 이유 (memory hook)**: **"fe는 *parent를 보면서 신장 보는 비율*; fm은 *parent를 보면서 metabolite 만드는 비율*"**.

**임상 적용 — *반드시* 두 양 모두 알아야**:
- fe = 0.5, fm = 0.4: parent의 50%가 신장, 40%가 metabolite, 나머지 10%는 직접 hepatic. 신부전에서 — fe 부분이 줄지만, *어디로 redirected되는가*가 결정적: metabolite로 가면 fm이 0.4 → 0.9로 증가 (Tozer p.674), 비활성 다른 경로로 가면 약리 효과 무변.
- fe = 0.5, fm = 0 (metabolite 없음): 신부전 dose 정확히 0.5×.
- fe = 0, fm = 0.6: 신부전에서 *parent CL 변화 없음*. 그러나 metabolite가 신청소되면 *metabolite 축적* → 시나리오 B (M20).

### Confusion Pair #11 — Formation Rate-Limited vs Elimination Rate-Limited — *Tozer Ch.20*

<!-- CONFUSION -->
**닮은 점**: 둘 다 모자식에서 metabolite t1/2 결정. 둘 다 농도-시간 plot 진단.

**다른 점**: 
- **Formation rate-limited (Case A; k << k(m); 흔함)**: metabolite는 parent와 *parallel* decay. 관찰 t1/2(metabolite) = t1/2(parent), 단 이는 metabolite *본래* t1/2 *아님*.
- **Elimination rate-limited (Case B; k(m) << k; 드뭄)**: metabolite는 parent보다 *훨씬 천천히* decay. 관찰 t1/2(metabolite) = metabolite *본래* t1/2.

**구조적 이유 (memory hook)**: **"Parent와 parallel decay를 보이는 metabolite의 t1/2는 *거짓말* — 진짜 metabolite t1/2는 별도 i.v. metabolite 투여로만 알 수 있다"**.

**임상 적용 — 신부전 metabolite 축적 예측**:
- Case A: parent CL 보정만으로 metabolite 농도도 *자동 보정* (formation rate에 묶임).
- Case B: parent와 metabolite가 *독립적* 거동 → parent CL 보정과 *별도* metabolite CL 보정 필요. 후자 무시되면 *수배* 축적.

**진단 결정**: parent와 metabolite t1/2가 같다는 *관찰만으로* Case A 단정하지 말 것. 별도 i.v. metabolite study에서 *훨씬 짧은* metabolite t1/2 측정되어야 Case A 확정.

### Confusion Pair #12 — Active Metabolite vs Inactive Metabolite의 PopPK 처리 — *Tozer Ch.20*

<!-- CONFUSION -->
**닮은 점**: 둘 다 *parent dose 분율*로 형성. 둘 다 plasma 측정 가능. 둘 다 fm·CL/CL(m)로 AUC 비 계산.

**다른 점 — PopPK 모델 구조**:
- **Inactive metabolite**: parent의 elimination *quantification 도구*로만 사용. AUC(m) 측정으로 fm 추정 + parent CL 분해. Metabolite 자체는 모델에 *명시적으로 포함하지 않아도 됨* (관심 없음).
- **Active metabolite**: parent + metabolite *둘 다* effect compartment를 갖는 *연결 PK-PD 모델* 필수. NONMEM에서 두 별도 컴파트먼트 + 두 별도 effect 항. PopPK 추정량 ETA 구조도 두 species 각각.

**구조적 이유 (memory hook)**: **"Inactive metabolite는 *분석 도구*; active metabolite는 *임상 작용물질*"**.

**Edge case — Interconversion**: parent ↔ metabolite 양방향 전환이 있으면 (prednisone ↔ prednisolone, sulindac ↔ sulindac sulfide), 두 species는 *효과적으로 한 종*. 결합 V_total과 결합 CL_irrev (각각 비가역 elimination 합)으로 모델링이 더 적절. 단순 parent-metabolite 식별성이 *완전히 다른* 형태가 됨.

### Confusion Pair #13 — fe-only Metabolite Drug vs fm-only Metabolite Drug의 신부전 함의 — *Tozer Ch.20*

<!-- CONFUSION -->
**닮은 점**: 둘 다 신부전에서 *어떤 형태든 농도 증가*. 둘 다 dose 조절 후보.

**다른 점 — 무엇이 축적되는가**:
- **fe-only (parent 직접 신청소)**: 신부전에서 *parent 농도* 증가. fe = 0.9이면 parent 거의 비례 증가, metabolite 영향 무관. Aminoglycoside 패턴.
- **fm-only with high fe(m) (parent → metabolite, metabolite 신청소)**: 신부전에서 parent 농도는 거의 *변하지 않을 수 있음*. 그러나 *metabolite 13배 증가* (M20 워크드). Procainamide/NAPA 패턴.

**구조적 이유 (memory hook)**: **"신부전 dose 조절은 *parent 농도*만으로 결정하면 안 된다 — 활성 species 총 노출이 기준"**.

**임상 결정 트리**:
1. 약물 active metabolite 존재? → No: parent CL만 보정.
2. Yes → metabolite fe(m) 측정. fe(m) < 0.3 → 시나리오 A. fe(m) > 0.7 → 시나리오 B (반드시 metabolite-based 조절).
3. Interconversion 추가 평가 (clofibric acid 패턴 — *간접* 신부전 영향).

이 결정 트리가 §1 dilemma의 *완성형* — 단순 fe 기반 모델 (Model A vs Model B)이 *완전한* 답이 아니라, **active metabolite fe(m)을 같이 보는 4-축 평가**로 확장.

---

### Confusion Pair #14 — fu (Plasma) vs fub (Blood) — *Tozer App.D*

<!-- CONFUSION -->
**닮은 점**: 둘 다 "단백결합 후 unbound 분율". 둘 다 0–1. 둘 다 PopPK 코드의 `FU` 변수로 표기되기 쉬움. 둘 다 hepatic clearance의 결정자.

**다른 점**: 
- **fu** (= fu_p): `Cu / C` — plasma unbound / **plasma** total. 측정은 plasma 직접.
- **fub**: `Cu / Cb` — plasma unbound / **blood** total. 측정 직접 어려움 — *변환 필요*.
- 관계: `fub = fu × (C/Cb)` — App.D Eq D-6의 plasma-to-blood 비가 *직접 곱해짐*.

**구조적 이유 (memory hook)**: **"Plasma 농도는 plasma 단백결합과 짝, blood 농도는 blood 분배 (RBC 포함)와 짝. *짝지어진 표현* 외에는 차원 오류"**.

**App.D Eq D-6의 결정자 (fu × KpBC)에 따른 fub의 거동**:
- `fu × KpBC < 1` (RBC 회피) → C/Cb > 1 → **fub > fu** (*수치적으로 더 큼*).
- `fu × KpBC > 1` (RBC 강한 분배) → C/Cb < 1 → **fub < fu** (*수치적으로 더 작음*).
- `fu × KpBC = 1` → C/Cb = 1 → fub = fu (*같음*).

**임상 시나리오별 fu vs fub 차이**:
| 약물 | 약물 화학 특성 | C/Cb | fu | fub | fu/fub |
|------|------------------|------|-----|------|---------|
| Phenytoin | 약산, 단백결합 강함 | ~0.55 | 0.10 | 0.18 | 0.55 |
| Propranolol | 약염기, lipophilic | ~0.70 | 0.10 | 0.14 | 0.70 |
| Cyclosporine | RBC 강한 분배 | ~0.03 | 0.05 | 1.7 | **0.03** |

→ Cyclosporine 같은 극단적 RBC partition 약물에서는 *fu와 fub의 차이가 30배* — *어느 것을 NONMEM 코드에 넣는가*에 따라 추정 결과 *완전히 다름*.

**임상 함의 (각 식의 올바른 짝)**:

| 식 | 올바른 분율 | 잘못 넣으면 |
|----|--------------|---------------|
| Tozer Eq 5-14 (well-stirred): `CL_b,H = QH·fub·CLint / (QH + fub·CLint)` | **fub** (blood) | 추출비 분류 잘못 (M5) |
| Eq E-13 (Model II): `CL_b,H = QH·fub·ρ·CLint / (QH + fub·ρ·CLint)` | **fub** (blood) | 동일 |
| Eq E-19 (oral AUC): `AUC_po = Dose / (fub·ρ·CLint)` | **fub** (blood) | DDI 예측 *약물별 다른 비율로* 잘못 |
| Tozer Eq 5-21 (renal CL filtration): `CL_R = fu · GFR` | **fu** (plasma) | 신청소 기여 잘못 |
| Tozer Eq 5-23 (urine reabsorption): `CL_R ≥ fu · Urine flow` | **fu** (plasma) | 동일 |

**기억 압축**: **"신장은 plasma에서 여과 → fu, 간은 blood에서 추출 → fub"** — 두 기관의 *물리적 출발점*이 다르기 때문에 식의 unbound 분율도 *물리적으로 다른 양*.

**Trench tip**: NONMEM 데이터셋 검토 시 — `FU` 컬럼이 직접 측정값 (plasma)인지, App.D Eq D-6으로 변환된 값 (fub)인지 *반드시 metadata 명시*. 두 교재가 표기 다름 (Gabrielsson은 fu, Tozer는 종종 fub) → 보고서 cross-reference 시 혼동 빈번.

---

## §7 Self-Test — Socratic Dilemma

<!-- SELF-TEST -->

> **§7 구조 (Step 4 *최종*)**: 본 질문 7개 (Q1–Q4 핵심 dilemma + Q5–Q7 Tozer Ch.5 보강 + Q8 Tozer Ch.20 핵심) + **Q14 진짜 Socratic Dilemma (두 충돌하는 optimization target)** + Quick Self-Test 19문항 (4 layer 통합). 본 §7은 *최종 형태*.

### 핵심 Dilemma (Q1–Q4 — 신청소 axis)

당신은 **신청소율(ClR)에 의해 35% 배설되는 신약 X의 phase 1 PopPK 보고서**를 작성 중. Renal impairment 코호트(GFR 30–60 mL·min⁻¹) 데이터에서 다음 두 모델 결정:

**Model A (단순)**: $$Cl_i = Cl_{typ} \cdot \left(\frac{CrCL_i}{100}\right)^{\theta}$$

**Model B (분리)** (Tozer Eq 5-9 + additivity):
$$Cl_i = (1 - f_{e,typ}) \cdot Cl_{typ} + f_{e,typ} \cdot Cl_{typ} \cdot \frac{CrCL_i}{100}$$

**두 모델 모두 fit 양호, OFV 거의 동일**.

**질문 1**: CrCL ≈ 100에서 *어떻게 같은가*?
**질문 2**: CrCL = 15 외삽에서 *어떻게 다른가*?
**질문 3**: Phase 3 신부전 용량 권고. base case vs sensitivity?
**질문 4**: Model A가 옳다면 — fe가 35%가 아니었는가? 비신청소가 신기능 의존? 구분 방법?

### Tozer Ch.5 보강 — 질문 5–7 (Step 2)

**질문 5 (M11 + M14)**: 신부전에서 *t1/2 무변* 관찰. Model B와 일치? CrCL = 30, V는 정상의 1.3배. Mechanism?

**질문 6 (M10 + M5)**: Plasma CL = 22 L/h, plasma-to-blood = 0.3. Hepatic blood CL과 E_H? Plasma CL만 보면 어떻게 *틀려 보이는가*?

**질문 7 (M15)**: SLCO1B1 \*5 polymorphism 보유자에서 노출 2.5배. 별도 covariate vs ETA?

### Tozer Ch.20 보강 — 질문 8 (Step 3, *핵심 1문항*)

**질문 8 (M17 진단 + M20 시나리오 결합)** — 약물 X에 active metabolite Y가 동반. 임상 데이터:
- i.v. parent 후 plasma 농도-시간 곡선이 parent와 metabolite *parallel decay* (둘 다 t1/2 ≈ 6 hr 관찰).
- 별도 i.v. metabolite Y 투여 study에서 metabolite *본래* t1/2 = 1.5 hr.
- 정상에서 fm = 0.4, fe(m) = 0.85.

**(a)** 어느 case (formation vs elimination rate-limited)? 진단 근거?
**(b)** *시나리오 분류* (M20의 A/B/C 결정 트리)? 신부전 환자에서 어떤 species가 가장 많이 축적되는가?
**(c)** parent CL만 보고 dose 결정하면 *왜 위험한가*?

### 답안의 방향성 (Q1–Q8 스포일러)

**Q1–Q4 (Step 1 신청소 dilemma)**:
- Q1: CrCL = 100에서 둘 다 `Cl_i = Cl_typ` (수렴).
- Q2: Model A는 *모든* CL이 power-scale → severe impairment 매우 낮게 외삽. Model B는 65% 비신청소 *건드려지지 않음* → ~70% × Cl_typ로 수렴. **Model B가 보수적**.
- Q3: 환자 안전 우선이면 *낮은 Cl 예측* Model A를 base; under-treatment 위험. 보통 둘 다 보고 + sensitivity. 메시지: **fe 사전 지식을 explicit incorporate**.
- Q4: Model A 옳을 가능성 — *비신청소 자체가 신기능 의존* 시 (uremic toxin이 hepatic CYP3A4 down-regulate). 검증: metabolite formation rate ↔ CrCL 상관성 — Tozer Ch.20 framework로 분리 진단.

**Q5–Q7 (Step 2 Tozer Ch.5 보강)**:
- Q5 (M11+M14): Model B와 일치 안 함. *t1/2 무변* + CL 감소 + V 1.3배 ↑ → fu 증가 (large V drug; M6 phenytoin 패턴) — **fu를 covariate로**.
- Q6 (M10+M5): Blood CL = 22×0.3 = 6.6 L/h. Hepatic blood CL = 0.65×6.6 = 4.3 L/h. E_H = 4.3/81 ≈ **0.053 — very low**. Plasma CL 22/81 ≈ 0.27 (intermediate으로 *잘못 보임*) → **분류 오류 위험**.
- Q7 (M15): SLCO1B1이 uptake transporter 영향 → blood CL 자체 변화. fe와 무관 → Model B *비신청소 항*에 추가 covariate. ETA 흡수만 시키면 *체계적 패턴* 잃음.

**Q8 (Step 3 Tozer Ch.20 — 핵심 1문항)**:
- (a) 별도 i.v. metabolite t1/2 = 1.5 hr (관찰 6 hr보다 *훨씬 짧음*) → **Case A (formation rate-limited) 확정**. parent t1/2 = 6 hr가 metabolite *겉보기* t1/2를 결정.
- (b) fe(m) = 0.85 → 신부전 시 metabolite CL 격감 → **시나리오 B (M20)**. Active metabolite가 *압도적으로* 축적.
- (c) Case A이지만 fe(m)가 크면 metabolite 자체 CL의 신부전 의존성이 강해 — **parent CL 보정 (renal axis)이 *부족*하고, metabolite CL 별도 보정 (metabolite axis) 필수**. parent agonist의 plasma 농도만 보면 metabolite 축적 위험을 *체계적으로 놓침*.



### Tozer App.D·E 보강 — 질문 14 (Step 4 *최종 Socratic Dilemma*)

**질문 14 (Two Competing Optimization Targets — *진짜 Socratic Dilemma*)**

당신은 **active metabolite를 가진 만성 투약 신약 Z의 신부전 환자 dose 권고**를 최종 결정 중이다. 다음 *두 임상 목표*가 충돌한다:

**Target A — Metabolite 안전성 보수성**:
*"Active metabolite 축적이 신부전에서 큰 폭으로 일어날 수 있으므로 (M20 시나리오 B), 신부전 환자에서 dose를 *aggressively* 감소시켜야 한다 (예: 정상의 25-30%). 일부 환자에서 under-treatment가 발생해도 toxic accumulation 회피가 우선."*

**Target B — Parent Exposure 기반 효능 유지**:
*"Parent drug의 plasma exposure가 효능을 결정하며, parent CL이 신부전에서 비례 감소하지 않으면 (예: fe = 0.35로 26% 감소만) parent dose를 크게 줄이는 것은 *under-treatment*. 표준 dose의 65-75%로 유지하여 효능 보장."*

**핵심 Dilemma**: 두 목표는 *상호 배타적*이며 — Target A 채택 시 효능 부족 위험, Target B 채택 시 metabolite 독성 위험. 어느 것을 *우선*하는가?

**(a)** 두 Target 각각의 *수식적 근거*를 본 통합본 카드 번호로 명시 (예: Target A → M20 시나리오 B 결정 트리; Target B → M11 additivity).

**(b)** 두 Target 중 어느 것이 옳은지 결정하기 위해 *반드시 측정해야 할* PK 파라미터 *3개*는? (어떤 데이터가 dilemma를 *해소*하는가?)

**(c)** *상황 의존적* 결정 — 어떤 환자 특성·약물 특성에서 Target A가 우선되어야 하고, 어떤 경우 Target B가 우선되어야 하는가?

**(d)** *임상 실무에서 이 dilemma가 자주 일어나는 약물 사례*를 본 통합본에서 식별 (Tozer Ch.20 본문 명시 약물).

#### 질문 14 답안 방향성

**(a) 수식적 근거**:
- Target A: M20 시나리오 B (`fe(m) → 1`인 active metabolite) + Tozer p.674 워크드 예제 (anuric에서 metabolite 13배 축적) + Confusion Pair #11 (Case B에서 metabolite는 *자기 t1/2*로 누적; parent CL 보정과 *별도* metabolite CL 보정 필요).
- Target B: M11 additivity (`CL = (1-fe)·CL_typ + fe·CL_typ·CrCL/120`) — 비신청소 (1-fe) 부분이 신기능과 *무관*하게 유지 → fe 작은 약물 (예: 0.35)에서 신부전 dose는 *전체*가 아닌 *fe 비례분*만 감소. M14 (t1/2는 derived parameter — primary는 CL과 V).

**(b) 결정적 측정 파라미터 *3개***:
1. **fe(m) — metabolite의 신청소 분율**: < 0.3이면 Target B 안전 (시나리오 A); > 0.7이면 Target A 강제 (시나리오 B).
2. **Metabolite 약리 활성과 효력 (intrinsic potency 비)**: parent의 *몇 %* 효력? equipotent (M20 워크드처럼)이면 metabolite 축적 영향 큼; metabolite 활성이 parent의 1/10이면 13배 축적도 임상 영향 미미.
3. **Therapeutic index (TI) of metabolite**: metabolite의 toxic-to-effective 농도 비. TI 좁으면 (예: < 5) Target A 강제; TI 넓으면 (> 50) Target B 안전 여유.

이 3개가 측정되면 dilemma가 *수식적으로 해소* — 단순한 trade-off가 아닌 정량 결정.

**(c) 상황 의존적 결정**:

| 조건 | Target A 우선 (보수적 dose 감량) | Target B 우선 (효능 유지) |
|------|-------------------------------------|------------------------------|
| Active metabolite 효력 | parent와 equipotent 또는 더 강함 | parent의 1/10 미만 |
| fe(m) | > 0.7 | < 0.3 |
| Therapeutic index | 좁음 (procainamide·NAPA 패턴) | 넓음 |
| 환자 모니터링 | 어려움 (외래) | 가능 (TDM 가능) |
| 임상 endpoint 측정 | 어려움 (delayed onset) | 즉각 (혈압 등) |
| 약물 정지 가능성 | 어려움 (만성 indication) | 쉬움 |

**(d) 임상 실무 사례** (Tozer Ch.20 본문 명시 약물):
- **Procainamide / NAPA** (Tozer p.683 Study Problem 3): 항부정맥, fe(m) → 1, equipotent → **Target A 강제**. 임상 모니터링이 "parent + NAPA" 표준.
- **Morphine / Morphine-6-glucuronide** (Tozer Fig 20-7): M6G가 진통 활성, fe(m) 큼 → **Target A 강제** (신부전 환자 morphine dose aggressive 감량).
- **Sulindac / Sulindac sulfide** (Tozer Table 20-5, p.667): sulfide가 active form, interconversion → 신부전에서 추가 복잡성.
- **Codeine / Morphine** (Tozer Table 20-1): codeine 자체 약하고 morphine이 *주 효과* — fm·fe(m) 모두 큼 → **Target A 강제**.

**임상 메시지**: 본 dilemma는 *fe = 0.35*나 *Plasma-blood 변환* 같은 *수치*가 아니라 **약물의 *물리화학적 본질* (active metabolite 존재 + 그 metabolite의 신청소 의존성 + 효력 비)에 의해 결정**된다. App.D·E의 first-principles는 *수치 정확도*에 기여하되, dilemma 자체는 *분자 수준*에서 결정.

### Quick Self-Test (가상 수치 사용 — *교육용 계산 연습*; 통합 19문항)

> 본 절의 수치는 *교육용 가정* (symbolic 수치)이며 *실측 임상 데이터를 가장한 것이 아님*. 학습자가 교재 본문 식을 *직접 적용* 연습하도록 단순화된 문제.

**Layer 1 (Gabrielsson §2.3·§2.5·PK5)**

- **Q5** (M2): Cl = 1.2 L·h⁻¹, fe = 0.35. ClR = ?
- **Q6** (M9): V = 7 L, Cl = 1.2 L·h⁻¹. K = ?
- **Q7** (M6, IV): Highly cleared IV 환자, albumin 절반 (fu 2배). 총 Css? Unbound Css?
- **Q8** (M6, Oral): 같은 환자가 oral. 총 Css? Unbound Css?

(답: Q5 = 0.42 L·h⁻¹; Q6 = 0.171 h⁻¹; Q7 IV total 무변, IV unbound 2배 ⚠️; Q8 oral total 절반, oral unbound 무변.)

**Layer 2 (Tozer Ch.5)**

- **Q9** (M10): Plasma CL = 1.0 L/min, plasma-to-blood = 0.5. Blood CL? E_H (Q_H = 1.35)?
- **Q10** (M11): 약물 Y의 fe = 0.40, total CL = 5 L/h. CL_R? CL_H?
- **Q11** (M14): 효소 유도로 CL 2배, V 무변. t1/2?

(답: Q9 blood CL = 0.5 L/min, E_H ≈ 0.37 (intermediate); Q10 CL_R = 2 L/h, CL_H = 3 L/h; Q11 t1/2 절반.)

**Layer 3 (Tozer Ch.20)**

- **Q12** (M16): i.v. parent 후 AUC(parent) = 100, AUC(metabolite) = 50. fm = 0.5. CL/CL(m)?
- **Q13** (M17): Parent t1/2 = 8 hr, 별도 i.v. metabolite t1/2 = 1 hr. Case?
- **Q14_quick** (M19): AUC(m)_single = 60 ng·hr/mL after 100 mg oral. τ = 12 hr. C(m)_av,ss?
- **Q15** (M20): fe(parent) = 0.1, fm = 0.4, fe(m) = 0.9. 신부전 시 어느 시나리오?

(답: Q12 = 1 (AUC 비 = 0.5 = 0.5 × CL/CL(m) → CL/CL(m) = 1); Q13 = Case A (formation RL); Q14_quick = 5 ng/mL; Q15 = **시나리오 B** — metabolite가 격감.)

**Layer 4 (Tozer App.D·E)**

**Q16 (M10 + App.D Eq D-6)**: H = 0.45, fu = 0.05, KpBC = 100. C/Cb = ?
**Q17 (M10 + App.D Eq D-8)**: 측정 H = 0.40, C/Cb = 0.40, fu = 0.10. KpBC = ?
**Q18 (M15 + App.E Eq E-13의 ρ)**: Pin·SA = 5, Pout·SA = 5 (passive diff), CLint = 50. ρ = ? Model I 회복?
**Q19** (M18 + App.E Eq E-19): Eq E-19에 따르면 *oral AUC는 hepatic blood flow QH 변동 시* 변동하는가? (정확/부정확)

(답: Q16 = 1/(1 + 0.45×[0.05×100 - 1]) = 1/(1 + 0.45×4) = 1/2.8 ≈ **0.357**; Q17 = (0.40 - 1 + 0.40)/(0.10×0.40) = -0.20/0.04 = **-5** — *비물리적 결과* (KpBC < 0 불가) → 측정 오류 또는 fu 잘못 측정 진단; Q18 = 5/(5+50) = **0.091**, *Model I 회복 안 됨* (Pin·SA << CLint이므로 시나리오 #2: basolateral uptake rate-limited); Q19 = **부정확 — Oral AUC는 QH에 무관**, QH 변동 무관하게 일정 (i.v.는 변동).)

---

## §8 Recap & NONMEM/PopPK Bridge

<!-- RECAP -->

### 통합 Phase 1 (Step 1 + Step 2 + Step 3 + Step 4) 핵심 흐름의 압축

**Layer 1: Gabrielsson 핵심 (M1–M9)**

$$\underbrace{\frac{dX}{dt} = Cl \cdot C}_{\text{M1}} \rightarrow \underbrace{Cl_R \cdot C, \ f_e = \frac{Cl_R}{Cl}}_{\text{M2}} \rightarrow \underbrace{\text{ARE} \mid \text{Rate} \mid \text{Sim}}_{\text{M3}}$$

$$\underbrace{Cl_H = \frac{Q_H \cdot f_u \cdot Cl_{int}}{Q_H + f_u \cdot Cl_{int}}}_{\text{M4}} \rightarrow \underbrace{\begin{cases} Q_H & (\text{high}) \\ f_u \cdot Cl_{int} & (\text{low}) \end{cases}}_{\text{M5}} \rightarrow \underbrace{\text{4 사분면}}_{\text{M6}} \rightarrow \underbrace{\text{IVIVE}}_{\text{M7}} \rightarrow \underbrace{\text{4 model}}_{\text{M8}} \rightarrow \underbrace{\text{PK5}}_{\text{M9}}$$

**Layer 2: Tozer Ch.5 통합층 (M10–M15)**

$$\underbrace{CL_b = CL \cdot \frac{C}{C_b}}_{\text{M10}} \rightarrow \underbrace{CL = CL_R + CL_H}_{\text{M11}} \rightarrow \underbrace{\text{biliary} + \text{EHC}}_{\text{M12}} \rightarrow \underbrace{CL_R = f_u \cdot \text{Urine flow}}_{\text{M13}} \rightarrow \underbrace{t_{1/2} = \frac{0.693V}{CL}}_{\text{M14}} \rightarrow \underbrace{\text{Ext CL: PS}_{\text{up,eff}} + CL_{\text{int}}}_{\text{M15}}$$

**Layer 3: Tozer Ch.20 통합층 (M16–M20) — Step 3**

$$\underbrace{\frac{dA(m)}{dt} = CL_f \cdot C - CL(m) \cdot C(m)}_{\text{M16: 모자식 mass balance}} \rightarrow \underbrace{\frac{AUC(m)}{AUC} = fm \cdot \frac{CL}{CL(m)}}_{\text{M16: AUC 비}}$$

$$\rightarrow \underbrace{\text{Case A (formation RL) vs Case B (elimination RL)}}_{\text{M17: rate-limiting}} \rightarrow \underbrace{\text{Oral = parent + metabolite cocktail}}_{\text{M18: first-pass}}$$

$$\rightarrow \underbrace{C(m)_{ss} = \frac{fm \cdot R_{inf}}{CL(m)}, \ C(m)_{av,ss} = \frac{AUC(m)_{single}}{\tau}}_{\text{M19: SS metabolite}} \rightarrow \underbrace{\text{시나리오 A/B/C + Interconversion}}_{\text{M20: 신부전 dose adjustment}}$$

**Layer 4: Tozer App.D + App.E 통합층 (M4·M10·M15·M18 보강) — Step 4 *최종***

$$\underbrace{\frac{C}{C_b} = \frac{1}{1 + H[f_u K_{PBC} - 1]}}_{\text{M10: App.D 5단계 mass-balance}} \quad \xleftrightarrow[\text{Cross-Validation}]{\text{동일 결론}} \quad \underbrace{\frac{C_b}{C} = 1 + H[f_u K_{PBC} - 1]}_{\text{M10: Eq D-7 역수}} \quad \rightarrow \quad \underbrace{K_{PBC} = \frac{H - 1 + C_b/C}{f_u \cdot H}}_{\text{M10: Eq D-8 역산}}$$

$$\underbrace{Cl_H = \frac{Q_H f_u Cl_{int}}{Q_H + f_u Cl_{int}}}_{\text{M4: Gabrielsson Eq 2:195}} \quad \xleftrightarrow[\text{Cross-Validation}]{\text{*표기 다름, 결론 동일*}} \quad \underbrace{CL_{b,H} = \frac{Q_H f_{ub} Cl_{int}}{Q_H + f_{ub} Cl_{int}}}_{\text{M4: App.E Eq E-8}} \quad \rightarrow \quad \underbrace{CL_{b,H} = Q_H \cdot \frac{f_{ub} \rho Cl_{int}}{Q_H + f_{ub} \rho Cl_{int}}}_{\text{M15: App.E Eq E-13 (Model II)}}$$

$$\underbrace{AUC_{po} = \frac{Dose}{f_{ub} \cdot \rho \cdot Cl_{int}}}_{\text{M18: App.E Eq E-19, Q_H 무관}} \quad \xleftrightarrow[\text{Cross-Validation}]{\text{4 결정자: f_{ub}, ρ, Cl_{int}, Dose}} \quad \underbrace{AUC_{ss,po} = \frac{Dose}{f_{ub} \cdot \rho \cdot Cl_{int}}}_{\text{M18: Eq E-20, plateau도 동일}}$$

> **Layer 4의 의미**: 본 layer는 *새 개념을 추가하지 않는다*. 이미 Layer 1·2의 결론(Gabrielsson well-stirred, Tozer extended CL)을 *first-principles 차원에서 수렴 검증*한다. 두 교재의 *독립적* 유도가 *동일* 결론에 도달함을 보여 well-stirred 모델의 수식적 견고성을 입증.

### NONMEM 구현 직접 매핑 — 통합 확장 (Step 4 갱신)

| 개념 | NONMEM/nlmixr2 구현 |
|------|---------------------|
| Eq 2:83 (`dX/dt = Cl·C`) | `$PK CL=THETA(1)*EXP(ETA(1))` |
| Eq 2:104 (`fe = ClR/Cl`) | `FE=THETA(2)*EXP(ETA(2)); CLR=FE*CL` |
| Tozer Eq 5-5 (plasma↔blood) | `CLB = CL * BPRATIO ; BPRATIO 컬럼/공변량` |
| Tozer Eq 5-9 (additivity) | `CL = CL_R + CL_H; CL_R = (CRCL/120)*FE*CL_TYP; CL_H = (1-FE)*CL_TYP` |
| Eq 2:102 (simultaneous fit) | `$ERROR DVID-conditional` |
| Eq 2:195 (well-stirred) | `CL = Q*FU*CLINT/(Q+FU*CLINT)` |
| Tozer Eq 5-35 (extended CL) | `CL_INT_H = (PS_INF+PS_PD)*CL_INT/(PS_EFF+PS_PD+CL_INT)` |
| Eq 5:1–5:2 (integrated) | `$SUBROUTINE ADVAN1 TRANS2` |
| Eq 5:3–5:4 (ODE) | `$SUBROUTINE ADVAN6 TOL=6` + `$MODEL` + `$DES` |
| **Tozer Eq 20-1 (모자식 ODE)** | **`$DES DADT(CENT_M) = KF*A(CENT) - KM*A(CENT_M)`** |
| **Tozer Eq 20-6 (AUC 비)** | **`$EST 후 NWPRI/PRIOR로 fm·CL/CL(m) 비 추정`** |
| **Tozer Eq 20-12 (SS metabolite)** | **`CSSM = FM*RINF/CLM ; predicted SS`** |
| **Tozer Eq 20-15 (multi-dose)** | **`AUCM_TAU = AUCM_SINGLE/TAU ; superposition prediction`** |
| **Tozer M20 신부전 covariate** | **두 species CL에 *동시* CRCL 적용; `CL_NR` + `CL_R(CRCL)` 분리, `CLM_NR` + `CLM_R(CRCL)` 분리** |
| **Tozer Carbamazepine autoinduction** | **`CL = CL_BASE * (1 + IMAX*TIME/(T50+TIME))` time-varying** |
| **Tozer Interconversion (clofibric acid)** | **`DADT(CENT)   = -CL_DM*A(CENT) + CL_MD*A(CENT_M); DADT(CENT_M) =  CL_DM*A(CENT) - CL_MD*A(CENT_M) - CL_MO*A(CENT_M)` (Tozer Fig 20-12 양방향)** |
| **App.D Eq D-6 (plasma-to-blood ratio)** | **`BPRATIO = 1.0/(1.0 + H*(FU*KPBC - 1.0))` — 환자별 데이터셋 컬럼으로 미리 계산; KPBC는 model에 fixed (in vitro 측정 또는 별도 study)** |
| **App.D Eq D-8 (KpBC inverse)** | **`KPBC = (H - 1 + (1.0/BPRATIO))/(FU*H)` — paired blood/plasma sample data로부터 직접 추정** |
| **App.E Eq E-13 (Model II ρ)** | **`RHO = PSIN/(PSOUT + CLINT_HEP); CLB_H = QH*FUB*RHO*CLINT_HEP/(QH + FUB*RHO*CLINT_HEP)` — uptake transporter polymorphism (SLCO1B1) covariate 적용** |
| **App.E Eq E-19 (oral AUC, QH 무관)** | **`AUC_PO_PRED = DOSE/(FUB*RHO*CLINT_HEP) ; verification & DDI prediction; QH항 부재 — 운동·심부전 시뮬레이션에서 i.v.와 oral *분리* 평가`** |

### 본 챕터가 PIPET 연구 라인에 직결되는 지점 (Step 4 최종 갱신)

1. **Prof. Seunghoon Han (DallphinAtoM/PBPK)**: M4–M8 + M10–M15 + M16–M20 + **App.D·E first-principles** 직접 기반. 특히 **App.E Eq E-13 (Model II ρ)**가 PBPK active uptake transporter (OATP1B1) covariate 모델링의 *수식적 근거*, **App.D Eq D-6**가 plasma-blood paired data 검증의 *first-principles 도구*.
2. **Prof. Sungpil Han (R/LLM-NONMEM)**: M9 + M14 + M16의 fm 식별성 함정 + **App.D·E의 두 교재 cross-validation 패턴**이 LLM 자동 코드 생성기가 *반드시 자동 인식*해야 할 패턴 — 동일 결론에 두 표기 (Gabrielsson fu vs Tozer fub) 변환 검증 자동화.
3. **AIMS BioScience 컨설팅**: M7 + M10 + M15 + M19 + M20 + **§7 Q14의 3-axis 복합 dilemma 풀이 패턴**이 active metabolite 신약 phase 1·2 보고서 종합 검증의 *결정 트리*. 6단계 워크플로우 + 신부전 4단계 결정 트리 + 3-axis 평가 패러다임.

### Step 4 통합 — 본 phase 종결 메시지

본 통합본은 *4 layer*로 구성되어:
- **Layer 1 (Gabrielsson, M1–M9)**: PopPK 기초 수식 + IVIVE workflow.
- **Layer 2 (Tozer Ch.5, M10–M15)**: 임상 적용 + plasma↔blood 변환 + extended clearance.
- **Layer 3 (Tozer Ch.20, M16–M20)**: 모자식 PK + active metabolite + 신부전 metabolite 축적.
- **Layer 4 (Tozer App.D·E, M4·M10·M15·M18 보강)**: First-principles 두 교재 cross-validation + ρ 항 + oral first-principles의 *QH 무관 결과*.

본 phase 종결 시점에 **20개 MUST 카드 + 14개 Confusion Pairs + 14개 §7 본 질문 + 19개 Quick Self-Test**가 *Phase 2 (의미 단위 fragmentation) 와 Phase 4 (Obsidian 입주)* 입력으로 준비되었다.

> Phase 4 Obsidian YAML frontmatter 입주 시 — 각 MUST 카드는 *최소* tags `[#PIPET, #Pharmacometrics, #Clearance]` + cross-link `[[M4]] [[M10]] [[M16]]` 형태로. App.D·E first-principles 보강은 별도 노트가 *아니라* M4·M10·M15·M18의 H1 헤딩 아래 *동일 노트 내* 보충 단락으로 포함.

---

## Step 4 (Phase 1 *최종*) 완료 블록

### Step 4 산출물 요약

| 영역 | Step 3 → Step 4 변동 |
|------|-----------------------|
| Curation Map MUST | 20개 → 20개 (변동 없음 — App.D·E는 CONTEXT 흡수) |
| Curation Map CONTEXT | 19개 → 26개 (C20–C26 신규: App.D·E 7개 항목) |
| §2 MUST 카드 보강 | M4 (App.E Model I), M10 (App.D Eq D-6/D-8), M15 (App.E Model II ρ), M18 (App.E Eq E-19) |
| §5 Confusion Pairs | 13개 → 14개 (#14: fu vs fub) |
| §7 본 질문 | 13개 → 8개 (Q1–Q8 핵심 보존) + Q14 (Socratic Dilemma 재설계) |
| §7 Quick Self-Test | 15개 → 19개 (Q16–Q19 App.D·E 신규) |
| §8 Recap | Layer 4 (App.D·E cross-validation) 추가 + NONMEM 매핑 4행 신규 |

### Patch Pass 1 적용 결과 (검수 의견 반영)

| 의견 | 적용 결과 |
|------|-----------|
| #1 CONTEXT 처리 압축 | M4·M10·M15·M18 보강부를 *각 1단락 + 핵심식*으로 압축 — mini-card 수준 → CONTEXT 1–2 sentence 규칙 준수 |
| #2 M8 Table 2.9 placeholder 복원 | Distributed/Dispersion 식 placeholder 제거 + 변수 정의 (`R_N`, `ε²`, `D_N`, `a`) 명시; 단 [확인 필요] 태그로 Roberts & Rowland 1986 원전 재대조 권고 |
| #3 §7 Socratic Dilemma 재설계 | Q14를 *Two competing optimization targets* (Target A metabolite 안전성 vs Target B parent 효능 유지) 형태로 재작성 — 충돌 + 결정자 + 상황 의존 + 임상 사례 4단계 |
| #4 가상 수치 정리 | Quick Self-Test 도입부에 "*교육용 가정* (symbolic 수치)" 명시 — 학습 연습용임을 분명히 함; Q14의 가설 시나리오 정량 풀이 (Mr. K) 부분은 Q14 재설계 시 *수식적 근거 + 결정 트리* 중심으로 전환되어 가설 수치 의존 최소화 |
| #5 통합 흔적 제거 | "Step 4 통합 예정" (M7, §5 #3) 제거 → "통합 완료" 표현으로 갱신; 완료 블록의 과밀 self-audit 단락 압축 |

### Phase 2 입력 준비 상태

- **Atomic units**: M1–M20 (20개) + Confusion Pairs (14개) + §7 (Q1–Q8 + Q14) + Quick Self-Test (19문항)
- **Inter-card linking**: `<!-- ANCHOR -->` 마커 22개가 directed graph 입력 — Phase 3 변환 직접 가능
- **Obsidian metadata**: § 헤딩 + Mode (A/B) + Source (G·T5·T20·TD·TE) 표기로 YAML frontmatter 자동 생성 가능
- **Phase 4C SVG candidates**: Tozer Ch.5 Fig 5-10·5-12·5-16·5-19·5-28 + Tozer Ch.20 Fig 20-1·20-2·20-3·20-7·20-8·20-9·20-10·20-11·20-12·20-13 (App.D·E는 개념도만, 별도 figure 없음)
- **잔존 [확인 필요] 태그**: 11건 (Step 1·2·3 누적) + M8 Table 2.9의 Distributed/Dispersion 식 (Roberts & Rowland 1986 원전 재검증 필요)

---

*Phase 1 *최종* 통합본 `01_step1_draft_v0.md` — Patch Pass 1 적용 완료. Phase 2 진행 가능.*

---

C-260502-072613-V8R

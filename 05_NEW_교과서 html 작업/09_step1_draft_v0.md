각하의 Phase 1 실행을 시작합니다. PDF 두 권(Gabrielsson §2.6 + PK26 + PK27 / Rowland & Tozer Ch.21)을 통합 분석하여 Step 1 Draft v0를 생성합니다.

---

# CURATION MAP

본 세션의 학습 목표는 표면적으로 "TMDD 모델링"이지만, 거장의 시각에서 보면 **(a) Turnover라는 단일 수학적 골격이 호르몬·단백질·항체·임상 PD를 통일하는 방식과 (b) 그 골격 위에 표적 결합이 얹혔을 때 PK 곡선이 4-페이즈로 분기하는 메커니즘을 동시에 체화**하는 것이다. 따라서 Curation은 후속 학습(mAb PopPK, FcRn 조작, NDA 비선형성 보고)이 의존하는 구조적 spine만 MUST로 추출한다.

## MUST (5개 — 체화 필수)

| # | 개념 | 후속 의존성 검증 |
|---|---|---|
| **M1** | **Turnover Paradigm (`kin`/`kout`)** | 이것 없이는 TMDD의 target compartment(`R`)도, FcRn 회수도, mAb 수렴 실패 진단도 해석 불가. |
| **M2** | **Protein/Antibody Distinctive PK** (Vd 제한·림프관 흡수·MW-기반 GFR·FcRn salvage) | 항체 비선형성을 "병태생리학적으로" 설명하지 못하면 임상 시나리오·규제 보고가 무너진다. |
| **M3** | **TMDD 4-Phase 농도-시간 프로파일 (A→B→C→D)** | 곡선 형태를 페이즈로 읽지 못하면 모델 선택(Full vs MM)이 데이터-기반이 아닌 임의 선택이 된다. |
| **M4** | **Full TMDD Model (8-parameter ODE system)** ⚡ **Apex Concept** | mAb의 비선형 PK·target occupancy·complex sink을 통합 표현하는 mechanistic 골격. PD와 PK가 한 수식으로 묶이는 지점. |
| **M5** | **Michaelis-Menten Approximation의 유효 경계** | "MM이 데이터에 맞아 보인다"의 함정을 인식하지 못하면 저농도 외삽에서 NDA Deficiency Letter. |

## CONTEXT (Card 본문에 1–2문장으로 흡수)

- **§2.6.1의 욕조 비유** (10 L bucket / 1 L·min⁻¹ tap → t_t = 10 min) → M1 카드의 직관 보조  
- **§2.6.3 IgX (sc 40 µg·kg⁻¹) / IgG·IgM·IgA·IgD·IgE turnover Table 2.11** → M1 카드의 임상 앵커  
- **§2.6.4 Estradiol (15 postmenopausal women, kin 19 µg·24h⁻¹, Cl 1.6 L·min⁻¹)** → M1 카드의 "endogenous" 응용  
- **§2.6.5 Comparison of Models Table 2.13** → M1의 통합 시각  
- **§2.6.6 Body Temperature / §2.6.7 Feedback** → M1 카드의 "PD 확장" 한 문장 (Apex 아님 — Scope Lock 지침)  
- **R&T Ch.21 Tables 21-1, 21-3, 21-12 (mAb 분류·치료 용도)** → M2 카드의 임상 컨텍스트  
- **Glomerular sieving coefficients Table 21-9 / Capillary permeability Fig.21-14** → M2 카드의 ADME 메커니즘  
- **FcγR-mediated clearance** → M2 카드 안에 짧게 (FcRn과 구분 목적)  
- **Immunogenicity Fig.21-19** → M2 카드 마지막 한 문장  
- **PK26 Efalizumab (5 i.v. doses, reduced 2-cmt + parallel linear/MM, Vt=0.061, Vmax=0.039, Km=0.161)** → M5 카드의 "MM이 통하는 케이스" 앵커  
- **Renal disease anakinra Fig.21-18, Table 21-16** → §6 시나리오로 이연 (Step 2)

---

<!-- MASTER LENS -->

# §1 Session Header & Roadmap

**Source**: [혼합]  
- Gabrielsson & Weiner 5e, Ch.2 §2.6 Turnover (pp.94–111) + Case Study PK26 (pp.599–601) + Case Study PK27 (pp.602–610)  
- Rowland & Tozer 5e, Ch.21 Protein Drugs (pp.687–730)

**Mode**: A-Critical | **Image rights**: None (P-type pointer만 §3 단계에서 허용)

## Big Idea (한 문장)

> **"항체의 비선형 PK는 약물의 성질이 아니라 표적의 수학(`kin`/`kout`/`kon`/`koff`/`ke(RL)`)이며, 이 수학을 5개 mechanistic 파라미터로 분해하지 못하고 2개 phenomenological 상수(`Vmax`/`Km`)로 압축하는 순간 저농도 외삽에서 100배 규모의 체계적 바이어스가 발생한다."**

## 개념 항법도

```
M1. Turnover Paradigm (kin/kout)
       │
       ├─ M2. Protein/Antibody PK 특수성
       │      (림프관·GFR cutoff·FcRn)
       │      └─ Apex 진입 전 "왜 항체는 다른가" 답변
       │
       └─ M3. TMDD 4-Phase 곡선 (A·B·C·D)
              └─ M4. Full TMDD Model ⚡ Apex
                     │  (8-parameter 완전 모델)
                     └─ M5. MM 근사 ↔ 유효 경계
                            (90–95% occupancy / Kd / biomarker potency)
```

## 지식 그래프 위치

- **선행 필수**: 1구획·2구획 선형 PK / Michaelis-Menten 효소론(Vmax·Km) / ODE 기본 / NONMEM `$DES` 구조 (Session II-04에서 다룬 General ADVAN/`$DES`가 본 세션 §6에서 직접 활용됨)
- **본 세션이 열어주는 후속 영역**:  
  (i) mAb PopPK 모델링 (sparse sampling + IIV on R0/Vmax)  
  (ii) FcRn 조작을 통한 반감기 연장 (next-gen biologic engineering)  
  (iii) QSP·PBPK에서 target compartment를 organ-specific으로 분해  
  (iv) NDA/IND PopPK 섹션 작성 시 비선형 클리어런스의 규제 언어  
  (v) Indirect Response PD 모델 (kin-stimulation/inhibition은 §2.6.6의 8-OH-DPAT body temperature 모델에서 직접 차용)

---

# §2 Concept Anatomy Cards

---

## ▌ Card M1 — Turnover Paradigm (`kin`/`kout`)

<!-- MASTER LENS -->

### [개념 Big Idea: 거장의 시각]

**왜 치명적으로 중요한가**: 항체의 21일 반감기를 보고 "약물이 안 빠진다"고 해석하면 틀린다. IgG 풀의 정상상태(≈10 g·L⁻¹)는 합성과 분해의 동적 평형이며, mAb는 이 평형 위에 얹힌 외부 입력일 뿐이다. 이 시각 없이 항체 PD/PK 보고서를 작성하면 reviewer가 "왜 baseline subtraction이 적절한가?"를 묻는 순간(Fig.2.77의 4가지 baseline 시나리오) 논리 전체가 무너진다.

**체화해야 할 단 하나의 직관**: `kin`은 **수도꼭지의 수압(mass·time⁻¹, 절대 속도)**, `kout`은 **욕조 마개 구멍의 크기(time⁻¹, 분율)**. 수도꼭지를 2배로 열면 정상상태 수위만 2배가 되고 도달 시간(`Tss`)은 변하지 않는다. 마개를 2배로 열면 수위는 절반이 되면서 **동시에** 도달 시간도 빨라진다. 이 비대칭성(Fig.2.70)이 turnover의 모든 임상 응용을 지배한다.

**이 직관을 머릿속에 박고 아래를 읽어라**: 모든 endogenous compound(IgG·estradiol·hyaluronan·cortisol·body temperature)는 `dA/dt = kin − kout·A`라는 동일한 골격으로 기술되며, TMDD의 `target` compartment(`R`)도 정확히 이 형태를 따른다. mAb가 표적과 결합하면 본질적으로 "외부 약물이 endogenous turnover에 inhibition으로 개입"한 것이다.

---

### A. Formal Definition

**Turnover system**은 zero-order 합성 `kin`과 first-order 분해 `kout·A`가 평형을 이루어 baseline `A0`를 유지하는 동적 시스템이다. 기본 ODE는

$$\frac{dA}{dt} = k_{in} - k_{out}\cdot A \quad \text{(Eq.2:237)}$$

정상상태(`dA/dt = 0`)에서 다음 5개 관계가 모두 성립한다:

| 관계식 | 의미 | Eq. |
|---|---|---|
| $k_{in} = k_{out}\cdot A_0$ | input = output 평형 | 2:239 |
| $k_{out} = k_{in}/A_0$ | fractional rate는 비율로 정의 | 2:240 |
| $A_0 = k_{in}/k_{out}$ | baseline은 두 율의 비 | 2:241 |
| $t_t = 1/k_{out} = A_0/k_{in}$ | turnover time = MRT | 2:242 |
| $t_{1/2} = \ln(2)/k_{out} = \ln(2)\cdot t_t$ | 반감기와 turnover time의 정확한 관계 | 2:244 |

> **단위**: `kin` [mass·time⁻¹] / `kout` [time⁻¹] / `A0` [mass] / `t_t` [time]. 이 단위 관계를 잠시라도 놓치면 `kin`을 `kout`처럼 쓰는 dimensional error가 NONMEM `$THETA` 초기값에서 발생한다.

---

### B. Derivation / Code Structure

#### B-1. Bucket Analogy (§2.6.1, p.96)

부피 10 L 욕조, 수도꼭지 1 L·min⁻¹ 입력 → `tt = 10 min`. 사람 몸의 물 42 L, 일일 입력 2.5 L → 물의 turnover time ≈ 17일. 이 "욕조 시간"이 항체의 21일 반감기와 동일한 수학적 구조를 갖는다는 점이 §2.6의 통일 메시지다.

#### B-2. PK 파라미터와의 연결 (§2.6.1 Eq.2:243)

$$t_t = \bar{t} = \frac{1}{k_{out}} = \frac{A_0}{k_{in}} = \frac{C_0\cdot V_{ss}}{C_0\cdot Cl} = \frac{V_{ss}}{Cl} = MRT$$

이 식의 핵심은 **turnover time = MRT**라는 것 — 즉, endogenous compound의 정상상태 풀 안에 머무는 평균 시간이 곧 PK의 MRT다. 이것이 단일 화합물 PK와 endogenous turnover를 같은 framework로 묶는 다리다. `[출처: Gabrielsson 5e, Ch.2, p.96]`

#### B-3. 임상 데이터 앵커 — IgX Subcutaneous (§2.6.3, Fig.2.74)

- **실험**: Growth hormone-like IgX, sc 40 µg·kg⁻¹, healthy volunteer 1명
- **Predose baseline**: 32 µg·L⁻¹
- **추정 결과**:  
  - `Cl/F` = 0.03 L·h⁻¹·kg⁻¹  
  - `V/F` = 0.10 L·kg⁻¹  
  - `kin` = 0.78 µg·h⁻¹·kg⁻¹  
  - `t_t` = 2.7 h, `MIT` = 1.8 h  
  - `t1/2` = 2.5 h → `kout` = 0.27 h⁻¹ (시간당 27% turnover)  
  - Pool size = `kin`/`kout` = 2.3 µg·kg⁻¹

> **거장의 메모**: sc dose만으로는 `Cl`과 `kin`을 구별할 수 없다 — 둘 다 `Cbaseline = kin/Cl` 안에서 ratio로만 식별된다. iv dose가 추가되어야 turnover time `t_t`와 mean input time `MIT`가 분리된다. 이 "추정 가능성(identifiability)" 논리가 §6의 NONMEM 데이터셋 설계에서 직접 재등장한다.

#### B-4. 다섯 면역글로불린 비교 (Table 2.11, p.102)

| Ig | MW (kDa) | Serum (mg·mL⁻¹) | t_{1/2} (days) | Turnover (mg·kg⁻¹·day⁻¹) | Fractional catabolic (% pool·day⁻¹) |
|---|---|---|---|---|---|
| IgA | 160(400) | 1.5–26 | 5.8 | 24 | 25 |
| IgD | 175 | 0.02–0.04 | 2.8 | 0.4 | 37 |
| IgE | 190 | 0.0003 | 2.5 | 0.016 | 89 |
| IgG | 150 | 9.5–12.5 | **23** | 33 | **6.7** |
| IgM | 950(1150) | 0.7–1.7 | 5.1 | 6.7 | 18 |

> **체화 포인트**: IgG의 `t1/2 = 23일 / fractional rate 6.7%·day⁻¹`은 다른 Ig 대비 4–10배 길다. 이 차이의 메커니즘이 **FcRn salvage** (Card M2)이며, 이것이 mAb를 약물로 만든 단일 가장 중요한 생물학적 사실이다.

---

### C. Structural Necessity

왜 ODE는 `kin − kout·A` 형태인가? 두 가지 수학적 필연 때문이다.

1. **Mass conservation**: 모든 분자는 만들어지거나 분해될 수밖에 없으며, 외부 입력이 없는 한 두 항(생산·소실)으로만 농도 변화가 발생한다. 단일 구획 가정 하에 이는 ODE의 일차 형태로 unique하다.
2. **First-order kinetics의 필연성**: Mass-action principle에 따르면 분해는 분자 농도에 비례한다 (`-kout·A`). 만약 효소가 saturate된다면 Michaelis-Menten으로 확장되지만, 그 경우에도 저농도 한계에서는 first-order로 reduce된다 (Card M5의 핵심). 영차 분해는 저장소가 무한할 때만 발생하며, endogenous compound에서는 거의 항상 first-order가 지배적이다.

영차 합성(`+kin`)의 필연성은 **합성이 농도와 무관하게 외부 cue(유전자 발현·호르몬 자극)에 의해 결정**되기 때문이다. 만약 합성이 자기 농도 양성 피드백을 가지면 박테리아 성장의 `+k_growth·A` 형태가 되며 (Eq.2:260), 이는 turnover가 아닌 polynomial expansion이다.

---

### D. Assumptions & Boundary Conditions

| 가정 | 위반 시 발생하는 일 |
|---|---|
| **Stationarity (parameter time-invariance)** | Diurnal variation(Fig.2.77 upper right), feedback rebound(lower left), Zeitgeber-driven(lower right)에서 baseline subtraction이 잘못된 결과를 준다. body temperature(§2.6.6) 모델은 정확히 이 위반의 예시 — 단일 turnover로 시작했다가 Peletier model의 oscillator 쌍으로 확장된다. |
| **Linear elimination** | Hyaluronan(Case Study PK32) 같은 saturable elimination을 갖는 endogenous compound에서는 `kout`이 농도 의존적이 된다. |
| **Single compartment** | r-hSOD nephrectomized rat (§2.6.2 Fig.2.72)처럼 central에 신장이 포함된 경우 central elimination 가정이 깨지며 `Vss`가 잘못 추정된다. |
| **No feedback** | IgG의 자기 농도 의존적 t_{1/2} 단축 (R&T Ch.2 Fig.2.84) — FcRn 보호 시스템이 30 mg·mL⁻¹에서 saturate되어 nonlinear feedback이 생긴다. |

---

### E. Limitations

기본 turnover model이 처리하지 못하는 영역과 다음 단계 복잡성:

1. **Saturable processes** → Michaelis-Menten turnover (hyaluronan PK32)
2. **Negative feedback / tolerance** → moderator compartment 추가 (§2.6.7 Ackerman hormone-glucose model, Eq.2:261–2:263)
3. **External Zeitgeber** → coupled oscillator (Peletier model Eq.2:256, body temperature §2.6.6)
4. **Target binding** → **TMDD** (Card M4) — 본 세션의 핵심 확장

---

### F. Five Cognitive Layers

| Layer | Vol I — 이론 (Gabrielsson + R&T) |
|---|---|
| **L1 형식적 수학** | `dA/dt = kin − kout·A` / 정상상태 5관계식 (Eq.2:239–2:244) |
| **L2 기하학적 직관** | Fig.2.70 좌우 대조: `kin` 변화 = 수직 평행이동(시간축 불변) / `kout` 변화 = 수직+수평 동시 변화 |
| **L3 구조적 동일성** | 화학 반응 평형(law of mass action), RC 회로의 capacitor charge/discharge, 인구 동학(생산·사망), 회계학(현금 유입·유출) — 모두 `dA/dt = source − sink·A` |
| **L4 생리학적 의미** | `kin` ↔ 합성 효소·분비 세포·외부 input rate / `kout` ↔ proteolytic enzymes·신장 GFR·FcRn 미보호 분획 |
| **L5 실무 투영** | NONMEM `$DES`: `DADT(2) = KIN − KOUT·A(2)` / TDM에서 endogenous baseline 제외 알고리즘 / NDA의 PD endpoint baseline 정의 |

---

### G. Zettelkasten Atom

```yaml
---
aliases: [Turnover Model, kin/kout 패러다임, Indirect Response Skeleton]
tags: [pharmacometrics/turnover, pkpd/indirect-response, modeling/foundational]
up: "[[PK/PD Mastery — Vol I — Session 09]]"
related: ["[[TMDD Full Model]]", "[[Indirect Response PD]]", "[[FcRn Salvage]]", "[[Estradiol Postmenopausal Turnover]]"]
source: "Gabrielsson & Weiner 5e, Ch.2 §2.6, pp.94–105"
---

# Turnover Paradigm

모든 endogenous compound의 농도는 `dA/dt = kin − kout·A`라는 단일 ODE로 기술되며, 정상상태 baseline은 `A0 = kin/kout`이다.
`kin`은 절대 input rate(mass·time⁻¹), `kout`은 fractional turnover rate(time⁻¹)이며, `kin` 변화는 정상상태 수위만 바꾸고 `kout` 변화는 수위와 도달 시간(`Tss = ln2/kout`)을 동시에 바꾼다.
이 framework는 IgG turnover, body temperature circadian rhythm, 그리고 TMDD의 target compartment까지 통일한다. 항체 PK의 비선형성은 약물 자체의 성질이 아니라 이 turnover 위에 표적 결합이 얹힌 결과다.
```

<!-- ANCHOR -->  
M1의 turnover 골격을 손에 잡았으니, 이제 항체가 왜 이 골격에서 특수한 위치를 점하는지 — 즉 림프관 흡수·MW-기반 신장 cutoff·FcRn salvage라는 세 가지 "병태생리학적 차별점"을 봐야 한다. 이 세 메커니즘이 M3·M4의 4-페이즈 곡선과 8-파라미터 모델을 가능하게 만든다.

<!-- RECAP -->  
**M1 정리**: Turnover = source(`kin`, 영차) − sink(`kout·A`, 일차). 정상상태 5관계식이 endogenous PK 전체를 통합. `kin` 변화와 `kout` 변화의 비대칭(Fig.2.70)이 임상 해석의 핵심.

---

## ▌ Card M2 — Protein/Antibody의 Distinctive PK

<!-- MASTER LENS -->

### [개념 Big Idea: 거장의 시각]

**왜 치명적으로 중요한가**: 항체 후보 물질을 small molecule처럼 oral·linear PK 가정으로 Phase 1 설계하면 두 가지 실패가 동시에 발생한다 — (i) sc 흡수에 며칠이 걸려 t_max가 5–8일에 형성되는데 첫 sampling을 24시간에만 두면 흡수 단계 전체를 놓친다; (ii) 22일 반감기를 가진 물질을 4주 single-dose 연구로 종결하면 terminal phase의 비선형성이 보이지 않는다 (Fig.21-7 Efalizumab의 0.1–10 mg·kg⁻¹ 곡선이 정확히 이 함정의 시각화).

**체화해야 할 단 하나의 직관**: 항체의 PK는 **세 가지 병태생리학적 게이트**의 조합으로 결정된다 — (1) **림프관 게이트** (sc 투여 후 MW > 16 kDa는 혈관 capillary 대신 림프계로 흡수, t_peak 5–8일), (2) **신장 게이트** (MW > ~30 kDa는 GFR로 거의 못 나감), (3) **FcRn 게이트** (IgG는 endothelial cell에 endocytosis된 후 산성 endosome에서 FcRn에 결합·재순환하여 분해를 회피, t_{1/2} 21일). 이 세 게이트를 통과하지 못한 분획만이 "약리학적으로 의미 있는" 약물이다.

**이 직관을 머릿속에 박고 아래를 읽어라**: TMDD의 비선형성은 이 세 게이트 위에 추가된 "네 번째 게이트(target binding)"이며, 그 새로운 게이트만이 농도 의존적이다. Card M3·M4의 모든 수식이 이 위계를 따른다.

---

### A. Formal Definition

**Therapeutic protein**의 PK는 small molecule과 다음 4가지 측면에서 본질적으로 다르다:

1. **분포 부피 제한**: `Vss ≈ 0.04–0.23 L·kg⁻¹` (혈장 ↔ ECF 사이) (Table 21-6) — small molecule처럼 세포내 분포가 일어나지 않는다.
2. **MW-의존적 신장 처리**: 신장 sieving coefficient가 ~5 kDa에서 0.89 → ~69 kDa에서 0.001로 급감 (Table 21-9, Fig.21-3).
3. **림프관 매개 흡수**: sc/im 투여 후 MW > 16 kDa는 림프관 우세 (Fig.21-16, Supersaxo data).
4. **단백질분해 (Proteolysis) 우세**: CYP 대사가 아니라 ubiquitous proteolytic enzymes (endothelial cells 1000+ m² 표면) 또는 receptor-mediated endocytosis (LDLR, mannose receptor, asialoglycoprotein receptor — Table 21-10).

IgG class 항체에 대해서는 추가로:

5. **FcRn salvage**: 산성 endosome (pH ~6)에서 FcRn 결합 → 재순환 → 분해 회피 → t_{1/2} ≈ 21일 (Fig.21-5).

---

### B. Derivation / Code Structure

#### B-1. Glomerular Sieving 데이터 (Table 21-9, p.704)

| Protein | MW (g·mol⁻¹) | Sieving coef. |
|---|---|---|
| Insulin | 6,000 | 0.89 |
| PTH (bovine) | 9,000 | 0.69 |
| Lysozyme | 14,600 | 0.75 |
| Myoglobin | 16,900 | 0.75 |
| Growth hormone | 22,000 | 0.65 |
| Superoxide dismutase | 32,000 | 0.33 |
| HRP (cationic) | 40,000 | 0.34 |
| HRP (neutral) | 40,000 | 0.06 |
| HRP (anionic) | 40,000 | **0.007** |
| Bence-Jones (λ-L) | 44,000 | 0.085 |
| Albumin | 69,000 | 0.001 |

> **체화 포인트**: 같은 40 kDa에서 cationic vs anionic이 **48배** 차이. 항체(IgG ~150 kDa, anionic at physiological pH)는 신장 게이트가 사실상 닫혀 있다 → 분해는 다른 경로(endothelial proteolysis + FcRn-회피분획) 의존. `[출처: R&T 5e, Ch.21, p.704]`

#### B-2. Lymphatic Recovery (Fig.21-16, sheep popliteal lymph)

| Compound | MW (Da) | Lymph recovery (% of dose) |
|---|---|---|
| FUdR | 246 | <5 |
| Inulin | 5,200 | 21 |
| Cytochrome c | 12,300 | 38 |
| Interferon-α-2a | 19,000 | 60 |

선형 회귀: lymph recovery ≈ 3.2% per kDa. **mAb (~150 kDa) 추정 lymph recovery > 80%**.

#### B-3. mAb sc Bioavailability (Table 21-15)

| Antibody | F | t_peak (days) | t_{1/2} (days) |
|---|---|---|---|
| Adalimumab | 0.64 | 5.5 | 30 |
| Bevacizumab (iv only) | — | — | 20 |
| Efalizumab | 0.50 | — | 17 |
| Omalizumab | 0.62 | 7.5 | 26 |
| Trastuzumab | — (iv) | — | 8.3 |

> sc bioavailability가 0.5–0.8에 머무는 이유: 림프관 transit 중 부분적 단백질분해 (presystemic loss). first-pass equivalent of lymphatic system. `[출처: R&T 5e, Ch.21, p.722–723]`

#### B-4. FcRn Salvage 메커니즘 (Fig.21-5)

```
  Plasma (pH 7.4)
       │ IgG가 endothelial cell에 endocytosis
       ▼
  Endosome (pH 6.0) — FcRn이 IgG에 강하게 결합
       │ FcRn-IgG 복합체는 vesicle로 분리
       ▼
  Recycling endosome → 세포 표면 (pH 7.4)
       │ FcRn-IgG 결합 풀림 (FcRn은 산성에서만 친화적)
       ▼
  Plasma 재진입 (salvage 완료)
   
   ※ FcRn에 결합 못한 IgG → lysosome → 분해
```

이 pH-의존적 salvage가 IgG의 21일 반감기를 만든다. mAb 엔지니어링에서 FcRn 친화도를 높이면 t_{1/2}를 30–40일로 연장 가능 (next-gen biologics).

#### B-5. Antibody 4-parameter 2-comp 모델의 한계 (§2.6.2, p.99)

cynomolgus monkey 항체 데이터 (5 i.v. infusions, 0.77–771 µmol·kg⁻¹, Fig.2.71):
- `CL` = 6 mL·h⁻¹·kg⁻¹
- `Vss` = 4 L·kg⁻¹

> **Gabrielsson의 경고 (p.99)**: "When the rate constant for redistribution k21 is much less than the rate constant of irreversible antibody elimination in the peripheral compartment k20, Vss will be incorrectly estimated."  
> 즉 항체가 organ tissue throughout the body에서 분해된다는 것을 알면서도 central elimination만 가정하면, Eq.2:145의 `Vss` 공식이 false answer를 준다. **항체의 distribution volume이 4 L·kg⁻¹인 것은 진짜 분포가 아니라 모델 misspecification일 가능성이 있다.**

---

### C. Structural Necessity

왜 단백질의 신장 처리가 sieving + proximal tubular metabolism인가? 두 단계 분리가 필연인 이유:

1. **Glomerular barrier는 size-selective + charge-selective filter**: pore size + glycocalyx 음전하가 동시에 작용 → albumin (anionic, 69 kDa)이 거의 안 새는 이유.
2. **Proximal tubule는 amino acid recovery system**: 작은 단백질(insulin, PTH)이 filter되면 brush border peptidase로 분해 + transporter로 재흡수 → urine에 거의 안 나타남 → 따라서 단백질의 "renal excretion"은 거의 모두 **renal handling/processing** (분해)이다.

이 분리가 무너지면 (예: tubular damage), filtered protein이 그대로 urine으로 — 이것이 임상적으로 **proteinuria**의 한 메커니즘이다.

---

### D. Assumptions & Boundary Conditions

- **FcRn 미포화 가정**: 치료 농도에서는 일반적으로 미포화이지만, 매우 고농도 IVIG 치료(>30 mg·mL⁻¹)에서는 포화 → IgG의 t_{1/2}가 23일 → 11일로 단축 (R&T Ch.2 Fig.2.84). 이것이 IgG에서 보이는 inherent feedback의 한 예.
- **Lymphatic transit time-invariance**: 운동·마사지·체온 변화가 림프 흐름을 변화시켜 sc 흡수율을 ±50% 변동시킬 수 있음. IgX의 sc dose-PK는 운동 환자에서 다르게 나타날 수 있다.
- **No pre-existing antidrug antibodies (ADA)**: ADA가 형성되면 immune complex 형성 → phagocytosis 증가 → mAb clearance 증가 (또는 드물게 감소). 첫 dose와 5–10번째 dose의 PK가 달라지는 이유.

---

### E. Limitations

- 이 framework는 **TMDD를 명시적으로 포함하지 않는다** — 표적 binding이 PK에 의미 있게 영향을 주는 순간 Card M4의 8-파라미터 모델이 필요하다.
- FcγR-mediated clearance (Table 21-11) — opsonized phagocytosis — 는 정량 모델링이 어렵다 (수많은 cell type, 농도 의존성 불명확). 일반적으로 lumped first-order로 처리.
- Methotrexate와 dopamine agonist가 FcγR expression을 28–44% 변경시키지만 (R&T p.706), 이 약물 상호작용은 임상적으로 거의 평가되지 않음.

---

### F. Five Cognitive Layers

| Layer | 내용 |
|---|---|
| **L1 형식적 수학** | sieving coefficient(`SC = Cfilt/Cunbound`) / 림프 lump-sum 흡수율 |
| **L2 기하학적 직관** | 신장 게이트의 sigmoid drop-off (5–60 kDa) / 림프 흡수율의 quasi-linear 증가 (Fig.21-16) |
| **L3 구조적 동일성** | 분자체 cromatography(size-exclusion)와 동형 / FcRn salvage = pH-gated transporter recycling |
| **L4 생리학적 의미** | 림프관 = "느린 우회로", FcRn = "분자 주차장 재발행 시스템" |
| **L5 실무 투영** | mAb sc dosing interval 설계 (2–4주) / FcRn-engineered mAb 용량 50% 절감 / 신부전 환자에서 mAb dose 미조정 (작은 단백질은 조정 필요) |

---

### G. Zettelkasten Atom

```yaml
---
aliases: [Antibody PK, Protein Drug Distinctive PK, FcRn Salvage]
tags: [pharmacometrics/biologics, mAb/PK, ADME/proteins]
up: "[[PK/PD Mastery — Vol I — Session 09]]"
related: ["[[Turnover Paradigm]]", "[[TMDD Full Model]]", "[[Glomerular Filtration]]", "[[Lymphatic Transport]]"]
source: "Rowland & Tozer 5e, Ch.21, pp.687–730 + Gabrielsson 5e §2.6.2"
---

# Protein/Antibody Distinctive PK

단백질 약물의 PK는 small molecule과 4가지 게이트에서 다르다: (i) Vss 0.04–0.23 L·kg⁻¹ (혈장–ECF 제한), (ii) MW > 30 kDa GFR 차단, (iii) sc 투여 시 림프관 우세 흡수 (t_peak 5–8일), (iv) IgG-class는 FcRn salvage로 t_{1/2} 21일.
mAb의 21일 반감기는 약물의 metabolic stability가 아니라 endothelial cell의 endocytosis-recycling cycle에서 산성 endosome FcRn 결합으로 분해를 회피한 결과다.
이 4 게이트를 이해하지 못하고 항체 후보의 임상 dosing을 small molecule처럼 설계하면 sampling design부터 무너진다.
```

<!-- ANCHOR -->  
M2의 4 게이트를 손에 잡았으니, 이제 mAb가 표적과 결합하는 순간 — 즉 다섯 번째 게이트 (target binding)가 추가되는 순간 — PK 곡선이 어떻게 4-페이즈로 분기하는지 봐야 한다. 이 페이즈 구조를 모르고 8-파라미터 ODE를 쓰면 코드는 돌아가지만 해석은 망상이다.

<!-- RECAP -->  
**M2 정리**: 항체 PK는 4 게이트의 합성물 — (i) Vss 제한, (ii) MW-기반 신장 cutoff, (iii) 림프관 sc 흡수, (iv) FcRn salvage. 이 위에 표적 결합이 5번째 게이트로 추가된 것이 TMDD.

---

## ▌ Card M3 — TMDD 4-Phase 농도-시간 프로파일

<!-- MASTER LENS -->

### [개념 Big Idea: 거장의 시각]

**왜 치명적으로 중요한가**: PK27 Fig.27.1의 4개 dose 곡선(1.5/5/15/45 mg·kg⁻¹)을 보면 **저용량 곡선이 고용량 곡선보다 빨리 떨어지는 것처럼 보이는 역설**이 발생한다. 이를 "데이터 노이즈"로 해석하고 단순 2-구획 모델을 fit하면 NDA 심사관이 즉시 잡아낸다. 이 현상은 **저용량에서 표적이 미포화 → target-mediated 경로가 활성 → clearance가 더 빠른** 것이다. 이 페이즈 구조를 한 눈에 읽지 못하면 모델 선택의 근거 자체가 없어진다.

**체화해야 할 단 하나의 직관**: TMDD 곡선은 **농도 사다리**다. 위에서 아래로 4개의 페이즈가 차례로 활성화/비활성화된다 — (A) 초기 2차 결합(L+R→RL이 매우 빠름), (B) 표적 포화 후 비특이 1차 소실만 작동(겉보기 linear), (C) 표적이 부분 포화 풀리며 mixed-order, (D) 최종 저농도에서 koff·ke(RL)이 지배. 같은 약물이 농도에 따라 4가지 다른 PK를 보여준다.

**이 직관을 머릿속에 박고 아래를 읽어라**: 4 페이즈 = 4개 ODE의 dominant term이 차례로 바뀌는 것. Fig.27.7의 4개 ODE 가 페이즈마다 다른 이유다. 이 위계를 알면 8-파라미터 모델(Card M4)의 식별가능성도 자동으로 따라온다.

---

### A. Formal Definition

**TMDD characteristic profile**은 ligand `L`의 농도 vs 시간 plot을 semi-log로 그렸을 때 나타나는 4개의 구별 가능한 페이즈로 정의된다 (PK27 Fig.27.7, R&T Fig.21-9):

| Phase | 농도 영역 | Dominant ODE term | 의미 |
|---|---|---|---|
| **A** | `L >> R₀` (초기) | $\frac{dL}{dt} \approx -k_{on}\cdot L\cdot R$ | 2차 결합이 매우 빠름. 짧은 dip. 저용량에서 더 두드러짐. |
| **B** | `L >> Km`, target saturated | $\frac{dL}{dt} \approx -\frac{Cl_{(L)}}{V_c}\cdot L$ | 비특이 1차 소실만 작동. 외관상 선형 PK. |
| **C** | `L ~ Km`, target 부분 포화 | $\frac{dL}{dt} \approx -\frac{Cl_{(L)}}{V_c}\cdot L - k_{int}\cdot \frac{L}{L + K_d}$ | Mixed-order. **곡선의 가속 구간**. |
| **D** | `L << Kd` (terminal) | $\frac{dL}{dt} \approx -k_{e(RL)}\cdot L$ | koff와 ke(RL)이 지배. terminal slope가 가파름. |

`[출처: Gabrielsson 5e, Ch.PK27, p.610]`

---

### B. Derivation / Code Structure

#### B-1. PK27 데이터셋의 페이즈 라벨링 (Fig.27.1, p.603)

4개 i.v. dose: 1.5, 5, 15, 45 mg·kg⁻¹. monoclonal antibody.

- **45 mg·kg⁻¹ 곡선**: A는 거의 안 보임(L >> R₀로 즉시 saturate). B 페이즈가 길게 우세 → 단순 1-구획처럼 보임. C가 늦게 나타나 D로 빠짐.
- **1.5 mg·kg⁻¹ 곡선**: A 페이즈가 명확히 보이는 짧은 초기 drop. B는 짧음. C·D가 dominant → 곡선이 빠르게 떨어짐.
- **R₀ = 12 mg·L⁻¹** (수평 dashed line). 모든 곡선이 결국 이 line 근처에서 굽어진다.
- **Km = (koff + ke(RL))/kon ≈ 0.03** (Fig.27.5의 horizontal dashed line). 매우 낮은 Km — high-affinity binding.
- **Kd = koff/kon ≈ 0.01** (Km보다 낮음, 차이는 ke(RL) 때문).

#### B-2. 페이즈별 ODE의 reduce (Fig.27.7)

원본 Eq.27:1의 풀어 쓴 형태:
$$V_c\cdot \frac{dL}{dt} = Input_L - Cl_L\cdot L - Cl_d\cdot(L - L_t) - k_{on}\cdot L\cdot R + k_{off}\cdot RL$$

Phase A에서 $k_{on}\cdot L\cdot R$ term이 dominant (R이 아직 미고갈, L 매우 높음):
$$\frac{dL}{dt} \approx -k_{on}\cdot L\cdot R$$

Phase B에서 R이 거의 모두 RL로 묶임 → free R ≈ 0 → on-binding term ≈ 0 → 1차 소실만:
$$\frac{dL}{dt} \approx -\frac{Cl_L}{V_c}\cdot L$$

Phase C에서 RL이 다시 분해되며 R이 부분 회복 → quasi-equilibrium 가정으로 MM-like:
$$\frac{dL}{dt} \approx -\frac{Cl_L}{V_c}\cdot L - k_{in}\cdot \frac{L}{L + K_d}$$

Phase D에서 L이 매우 낮아 RL formation 미미, 기존 RL의 분해 속도가 dominant:
$$\frac{dL}{dt} \approx -k_{e(RL)}\cdot L$$

> **거장의 메모**: 페이즈마다 dominant term이 바뀌므로 **어느 한 페이즈만 sampling해서는 모델 식별 불가**. PK27 데이터가 0–600시간을 커버한 이유 (4개 페이즈를 모두 잡기 위해). `[출처: Gabrielsson 5e, Ch.PK27, p.610]`

#### B-3. Total Clearance vs Concentration (Fig.27.3 right)

총 클리어런스 `Cl(L) + TMDD`를 농도에 대해 plot하면:

```
  Cl_total
    │
    │── plateau1 (저농도, Cl + R-mediated, 양 트랙 모두 1차)
    │       \
    │        \  decreasing region (target 점점 saturate)
    │         \
    │          \___________ plateau2 (고농도, Cl만 작동)
    │  
    └─── 농도(log) ──→
   "Effective concentration range"가 두 plateau 사이의 transition zone
```

- 양 끝 plateau는 **둘 다 linear PK**이지만 메커니즘이 다르다 (이것이 §5 Confusion Pair 4의 핵심).
- 양 plateau의 차이 = R-mediated clearance contribution = `Vmax/Km` ratio of MM 근사.

---

### C. Structural Necessity

왜 4 페이즈인가? 3도 5도 아닌가?

**수학적 필연**: 시스템에 3개의 시간상수가 있다 — (i) `1/(kon·R₀)` (binding time), (ii) `1/Cl·V_c⁻¹` (non-specific elimination time), (iii) `1/ke(RL)` (complex internalization time). 이 3개 timescale의 분리도(separation)가 4개 구분 가능한 dynamics를 만든다 — 빠른 binding + 느린 non-specific elim + 느린 complex internalization + transition zone = 4 phase.

만약 binding이 매우 느리면 (low affinity, high Kd) → A 페이즈가 사라지고 단순 2-구획처럼 보임. 만약 ke(RL)이 매우 빠르면 → D 페이즈가 단축. 실제 PK27의 monoclonal antibody는 이 3 timescale이 모두 명확히 분리되어 있어 4 페이즈가 textbook example로 나타난다.

---

### D. Assumptions & Boundary Conditions

- **Soluble target only**: PK27/R&T Fig.21-9는 soluble target 가정. **Membrane-bound target은 internalization rate가 다르고 turnover dynamics가 다름** → Fig.27.7의 페이즈 구조가 변형됨.
- **Single target site**: 다중 표적 (예: bispecific antibody)에서는 페이즈 수가 늘어남.
- **Linear target turnover**: `kin = kout·R₀`가 시간 불변 가정. 염증·암 진행 시 target 합성률 변화 → 페이즈 dynamics 변형.

---

### E. Limitations

- 페이즈 식별을 위한 sampling 부담: 0~500시간을 dense하게 샘플 — Phase 1에서는 가능하지만 Phase 3 sparse sampling에서는 거의 불가. 따라서 mAb PopPK는 페이즈 식별보다 prior-informed Bayesian estimation에 의존.
- Phase A의 짧은 시간 스케일 (수 분~수 시간) 때문에 임상 sampling으로 잡기 어려움 → kon 추정의 어려움 (PK27 dataset I에서 kon CV% 17%, dataset III에서 1%로 개선되는 이유).

---

### F. Five Cognitive Layers

| Layer | 내용 |
|---|---|
| **L1 형식적 수학** | 4개 페이즈 ODE reduce form / 시간상수 분리 조건 |
| **L2 기하학적 직관** | semi-log plot에서 4개 다른 slope가 차례로 나타남 / 저용량 곡선이 고용량보다 빨리 내려가는 "역설" |
| **L3 구조적 동일성** | 화학 공정의 multi-stage reactor (각 stage의 rate-limiting step) / 다단계 cascade의 timescale separation |
| **L4 생리학적 의미** | A=initial overshoot, B=mAb이 평형 안정화, C=therapeutic window, D=tail (드물게 측정) |
| **L5 실무 투영** | sampling design: dense at 0–24h (A), 1–7day (B-C), 7–60day (C-D) / dose escalation 해석 |

---

### G. Zettelkasten Atom

```yaml
---
aliases: [TMDD 4-Phase Profile, Mager-Jusko Phases A-D]
tags: [pharmacometrics/tmdd, mAb/nonlinear-PK, modeling/phase-analysis]
up: "[[PK/PD Mastery — Vol I — Session 09]]"
related: ["[[TMDD Full Model]]", "[[MM Approximation Boundary]]", "[[Quasi-Equilibrium Approximation]]"]
source: "Gabrielsson 5e PK27 Fig.27.7 (p.610) + R&T Fig.21-9 (p.712)"
---

# TMDD 4-Phase Profile

TMDD ligand의 농도-시간 곡선은 4개 페이즈를 보인다: (A) 초기 2차 결합 dip, (B) target saturated 1차 선형, (C) mixed-order transition, (D) koff/ke(RL) terminal.
페이즈 식별은 비선형성 모델 선택의 근거이며, 양쪽 끝(A와 D 부근)이 모두 "linear PK"로 보이지만 메커니즘이 다르다.
4개 페이즈를 sampling으로 cover하지 못하면 8-파라미터 식별이 불가능 — PK27이 0–600h을 dense하게 샘플한 이유.
```

<!-- ANCHOR -->  
4 페이즈가 농도에 따라 차례로 활성/비활성화되는 구조를 손에 잡았으니, 이제 이 4 페이즈를 모두 한 번에 generate하는 8-파라미터 ODE 시스템 — Mager-Jusko Full TMDD Model — 의 해부로 진입할 수 있다. 이것이 본 세션의 ⚡ Apex Concept이다.

<!-- RECAP -->  
**M3 정리**: TMDD 곡선의 4 페이즈(A·B·C·D)는 3개 timescale 분리에서 자연발생. 양 끝의 linear PK는 같은 모양이지만 메커니즘이 정반대(병렬 vs 잔존). 페이즈 식별이 모델 선택의 근거.

---

## ▌ Card M4 — Full TMDD Model (8-parameter ODE system) ⚡ **Apex Concept**

<!-- MASTER LENS -->

### [⚡ Apex Concept] [개념 Big Idea: 거장의 시각]

**왜 치명적으로 중요한가**: 본 세션의 모든 다른 개념이 결국 이 한 모델로 수렴한다. mAb 후보의 FIH 용량 예측, Phase 1 sampling design, Phase 3 PopPK report, NDA의 비선형 클리어런스 섹션, 그리고 모든 PD biomarker integration이 이 8-파라미터 framework 위에서 작동한다. 이 모델을 mechanistic level에서 내면화하지 못하면, mAb 모델러는 vendor 소프트웨어의 default를 돌리는 기능공이 될 뿐 — bispecific의 confounded TMDD나 ADC의 payload release dynamics 같은 next-generation 문제 앞에서 작동을 멈춘다.

**체화해야 할 단 하나의 직관**: Full TMDD = **(M1의 turnover skeleton) ⊗ (M2의 항체 PK 4-게이트) ⊗ (M3의 4 페이즈 dynamics)**. 즉 `target` compartment(R)는 자기 turnover(kin/kout)를 유지하면서, `ligand` compartment(L)와 second-order 결합을 통해 `complex`(RL)을 형성하고, 이 RL이 ke(RL)로 사라지는 — **세 개의 ODE가 서로를 통해 비선형성을 만드는 작은 dynamical system**이다. 어느 한 ODE도 다른 두 개와 분리될 수 없다.

**이 직관을 머릿속에 박고 아래를 읽어라**: 8개 파라미터(`Cl, Vc, Cld, Vt, kon, koff, ke(RL), R₀, kout`)를 메모리하지 말고, 각 파라미터가 4-페이즈 중 어느 페이즈를 지배하는가를 외워라. 그 매핑(F. Cognitive Layers)이 식별 가능성·디버깅·임상 해석의 모든 열쇠다.

---

### A. Formal Definition

**Full TMDD Model** (Mager & Jusko 2001)은 다음 4개 ODE로 정의되는 mechanistic 시스템이다:

$$\frac{dC_L}{dt} = \frac{1}{V_c}\left[Input_L - Cl_L\cdot C_L - Cl_d\cdot(C_L - C_t) - k_{on}\cdot C_L\cdot R + k_{off}\cdot C_{RL}\right] \quad \text{(27:1, 1)}$$

$$\frac{dC_t}{dt} = \frac{1}{V_t}\left[Cl_d\cdot C_L - Cl_d\cdot C_t\right] \quad \text{(27:1, 2)}$$

$$\frac{dR}{dt} = k_{in} - k_{out}\cdot R - k_{on}\cdot C_L\cdot R + k_{off}\cdot C_{RL} \quad \text{(27:2)}$$

$$\frac{dC_{RL}}{dt} = k_{on}\cdot C_L\cdot R - k_{off}\cdot C_{RL} - k_{e(RL)}\cdot C_{RL} \quad \text{(27:3)}$$

with **초기조건**: $C_L(0) = Dose/V_c$, $C_t(0) = 0$, $R(0) = R_0 = k_{in}/k_{out}$, $C_{RL}(0) = 0$.

with **유도 정의**:  
$$K_d = \frac{k_{off}}{k_{on}}, \quad K_m = \frac{k_{off} + k_{e(RL)}}{k_{on}}$$

`[출처: Gabrielsson 5e PK27, pp.606–607 + Mager & Jusko 2001 / R&T Eq.21-1~21-6, p.711]`

---

### B. Derivation / Code Structure

#### B-1. 각 ODE의 mass balance 해부

- **Eq.27:1 (ligand central)**: 입력 `Input_L` + 비특이 청소 `-Cl_L·C_L` + 분포 `±Cl_d·(C_L−C_t)` + binding loss `−kon·C_L·R` + complex 분해 회귀 `+koff·C_RL`. 즉 ligand는 (i) 비특이 분해, (ii) tissue 분포, (iii) target 결합으로 사라지지만, complex 분해 시 일부 회귀.
- **Eq.27:1 (ligand tissue)**: 단순 2-구획 distribution. target과 complex는 central에만 존재 (가정).
- **Eq.27:2 (target turnover + binding)**: `kin − kout·R` 부분이 정확히 Card M1의 turnover skeleton. 추가로 binding loss `−kon·C_L·R` + complex 분해 회귀 `+koff·C_RL`.
- **Eq.27:3 (complex dynamics)**: formation `+kon·C_L·R` − dissociation `−koff·C_RL` − internalization sink `−ke(RL)·C_RL`.

> **체화 포인트**: `kin·C_L·R` term이 두 ODE에 똑같은 부호로 나타난다 (loss in L, loss in R, gain in RL). 이것이 mass conservation의 명시적 enforcement. 코드에서 부호 한 곳을 잘못 쓰면 mass가 spontaneously 생성/소멸 — 즉시 NONMEM `MINIMIZATION FAILED`.

#### B-2. PK27 데이터로 본 식별 가능성 위계 (Table 27.2, p.609)

| Parameter | Dataset I (L only) CV% | Dataset II (L+R) CV% | Dataset III (L+R+RL) CV% |
|---|---|---|---|
| `Cl` | 1 | 1 | 1 |
| `kon` | **17** | 2 | 1 |
| `koff` | **27** | **13** | 3 |
| `Vt` | 2 | 2 | 1 |
| `Cld` | 4 | 3 | 3 |
| `kout` | 6 | 2 | 2 |
| `R₀` | 4 | 1 | 1 |
| `ke(RL)` | **27** | **23** | 2 |

> **거장의 메모**: ligand만으로는 `kon`, `koff`, `ke(RL)`이 부정확. target까지 추가해도 `koff`, `ke(RL)`은 여전히 부정확. **complex 데이터까지 있어야 모든 8 파라미터가 1–3% precision에 도달**한다. 이것이 Phase 1 mAb 연구에서 free target과 complex assay 개발에 막대한 자원이 투입되는 이유. `[출처: Gabrielsson 5e PK27 Table 27.2, p.609]`

#### B-3. NONMEM `$DES` 구조 (B-Standard 모델러용)

```
$MODEL
  COMP=(LIGCEN)   ; A(1) = ligand central
  COMP=(LIGTIS)   ; A(2) = ligand tissue
  COMP=(TARGET)   ; A(3) = target R
  COMP=(COMPLEX)  ; A(4) = ligand-target complex RL

$PK
  CL  = THETA(1) * EXP(ETA(1))
  V1  = THETA(2)                    ; fixed at 0.05 L/kg per PK27
  Q   = THETA(3) * EXP(ETA(2))
  V2  = THETA(4) * EXP(ETA(3))
  KON = THETA(5) * EXP(ETA(4))
  KOFF= THETA(6) * EXP(ETA(5))
  KER = THETA(7) * EXP(ETA(6))      ; ke(RL)
  R0  = THETA(8) * EXP(ETA(7))
  KOUT= THETA(9) * EXP(ETA(8))
  KIN = R0 * KOUT                   ; derived, not estimated
  
  A_0(3) = R0 * V1                  ; target initial = R0
  ; A_0(1)=A_0(2)=A_0(4)=0 by default

$DES
  CL_CONC = A(1)/V1
  CT_CONC = A(2)/V2
  R_CONC  = A(3)/V1                 ; target shares Vc
  RL_CONC = A(4)/V1                 ; complex shares Vc
  
  BIND   = KON  * CL_CONC * R_CONC * V1
  UNBIND = KOFF * A(4)
  
  DADT(1) = -CL*CL_CONC - Q*(CL_CONC-CT_CONC) - BIND + UNBIND
  DADT(2) =  Q*(CL_CONC-CT_CONC)
  DADT(3) =  KIN*V1 - KOUT*A(3) - BIND + UNBIND
  DADT(4) =  BIND - UNBIND - KER*A(4)

$ERROR
  IPRED_L = A(1)/V1
  Y = IPRED_L * (1 + EPS(1))        ; constant relative error per PK27
```

> **거장의 메모**: `BIND` term을 `KON*CL_CONC*R_CONC*V1`로 쓰는 이유 — `kon`은 (concentration·time)⁻¹ 단위이므로 amount/time을 얻으려면 V1 곱셈 필요. 단위 실수가 가장 흔한 NONMEM `$DES` 버그. `[출처: Gabrielsson 5e PK27 + 표준 NONMEM ADVAN13 패턴]`

#### B-4. 임상 데이터 앵커 — Efalizumab (PK26, Fig.21-7 R&T)

PK26은 의도적으로 Full TMDD 대신 **reduced 2-cmt parallel linear+MM**를 fit (target/complex 데이터 없음으로 인한 식별 불가):

| Parameter | Estimate | CV% |
|---|---|---|
| `Vt` | 0.061 L·kg⁻¹ | 13 |
| `Vmax` | 0.039 mg·h⁻¹·kg⁻¹ | 12 |
| `Km` | **0.161** mg·L⁻¹ | **44** |
| `Cl_d` | 0.031 L·h⁻¹·kg⁻¹ | 23 |
| `Cl_L` | 0.007 L·h⁻¹·kg⁻¹ | 10 |

> **PK26의 자백**: "A full TMDD model failed to fit data with resulting good parameter precision **as expected due to the lack of target and complex data**" (p.601). 즉 Efalizumab 임상 dataset이 target/complex assay를 갖추지 못해 식별 불가능했음을 명시. **Km의 CV% 44%는 이 모델의 한계의 직접적 증거** — Card M5의 Validity Boundary로 직접 이어진다. `[출처: Gabrielsson 5e PK26, p.601]`

---

### C. Structural Necessity

왜 8개 파라미터가 모두 필요한가? 어느 하나를 빼면 무엇이 무너지는가?

| 파라미터 제거 | 무너지는 페이즈/현상 |
|---|---|
| `Cl_L` 제거 | 고농도 plateau (Phase B) 사라짐 → Cl_total이 농도와 함께 0으로 → 비현실적 |
| `Vc` 고정 안함 | Phase A의 dilution volume 식별 불가 → kon 추정 흔들림 (PK27이 V_c=0.05 L·kg⁻¹로 fix한 이유) |
| `kon` 제거 | binding 자체 불가 → TMDD 시스템 붕괴 |
| `koff` 제거 | RL이 영구 trap → Phase D의 koff-driven slope 사라짐 |
| `ke(RL)` 제거 | RL이 sink가 없음 → 정상상태 R 추정 불가 |
| `R₀` 제거 | target baseline 무너짐 → kin/kout ratio 추정 불가 |
| `kout` 제거 | target turnover 정지 → mAb 농도 변화에 따른 R 회복 dynamics 없음 |

각 파라미터는 **구별되는 데이터 영역에서 정보를 제공**하므로 — 충분한 dataset richness 하에서는 — 제거할 수 없다. PK27 dataset III에서 모든 8개가 1–3% precision에 도달하는 것이 이 식별 가능성의 경험적 증명.

---

### C-2. Plausible Fallacy (그럴싸한 오류) — ⚡ Apex 전용

**오류**: "MM 근사가 ligand 데이터에 잘 맞고 GOF plot이 깨끗하면, Full TMDD 대신 MM을 NDA에 제출해도 안전하다."

**나비효과의 메커니즘**:

PK27 Fig.27.6에서 MM 모델을 ligand 데이터에 fit하면 — 4개 dose 중 상위 3개에는 잘 맞아 보이지만 — **최저 용량 곡선에서 systematic deviation**이 발생한다. MM은 4 페이즈 중 (B)+(C) 영역만 잡고, (A) 초기 2차 결합과 (D) terminal koff/ke(RL) 페이즈를 못 잡기 때문이다. 이로 인해 추정된 `Km = 3.7 mg·L⁻¹` vs **true Km = 0.03 mg·L⁻¹** — **123배 over-prediction**.

이 123배 바이어스는 다음과 같이 임상에 전파된다:

1. **저농도 외삽**: 정상상태 trough 농도 예측에서 MM은 R-mediated clearance를 과소평가 → trough를 과대평가 → "dosing interval 늘려도 안전" 잘못된 결론.
2. **FIH dose 예측**: MABEL (minimum anticipated biological effect level) 계산에서 target occupancy를 잘못 계산 → first-in-human dose가 실제 receptor saturation 한참 위로 설정 → tornado-shaped CRS 위험.
3. **Pediatric extrapolation**: 어린이의 R₀가 성인과 다른데 MM은 R₀ 자체를 estimate하지 않으므로 outside-of-range 외삽 시 PD 예측 완전 실패.

**GOF Diagnostic Signature** (이름 부여): **"Phantom Linearity"** — 저용량 dose group의 conditional weighted residuals (CWRES)가 dose-stratified plot에서 아래쪽으로 systematic bias (항상 음수). 표준 OFV·VPC plot에서는 잡히지 않으며 **dose-by-time stratified residual plot**에서만 보임. 모든 mAb PopPK reviewer는 이 시그니처를 본능적으로 찾는다.

`[출처: Gabrielsson 5e PK27 Fig.27.6 + Peletier & Gabrielsson 2012]`

---

### D. Assumptions & Boundary Conditions

| 가정 | 위반 시 |
|---|---|
| **Soluble target only** | Membrane target에서는 internalization이 cell-specific → ke(RL) heterogeneous. PK27의 single ke(RL) 가정 깨짐. |
| **R₀ at single SS baseline** | 질병 진행 (예: 종양 성장)에서 R₀ 시간 변화 → 비정상상태 baseline. |
| **No pre-existing autoantibody** | ADA 형성 시 immune complex가 추가 sink → 모델에 반영하려면 9th compartment 필요. |
| **Vc, Vt time-invariant** | edema·acute kidney injury에서 Vc shift → 추정값 bias. |
| **Single binding site** | bispecific antibody에서는 두 R, 두 RL → 16 ODE. |

---

### E. Limitations

- **식별 가능성**: target/complex 데이터 없으면 8 파라미터 fit 실패 (PK26이 Reduced 모델 사용한 이유).
- **임상 환경**: target/complex assay가 없는 약물(대다수)에는 적용 불가 → quasi-steady-state (QSS) 또는 quasi-equilibrium (QE) 근사 사용. R&T p.712: "QE approximation is adequate when internalization rate is much smaller than dissociation rate."
- **계산 비용**: 8 파라미터 + 4 ODE → NONMEM FOCEI estimation 시간이 시간 단위로 늘어남. ADVAN13 (general non-linear) 사용 필수.
- **다중 mAb 동시 모델링** (combination therapy): non-additive binding interactions → 모델 복잡도 폭발.

---

### F. Five Cognitive Layers

| Layer | 내용 |
|---|---|
| **L1 형식적 수학** | 4 ODE + 8 파라미터 + 2 유도식 (Kd, Km) / mass conservation 부호 검증 |
| **L2 기하학적 직관** | 4 페이즈가 시간상수 분리에서 자연발생 / R₀ horizontal line이 Phase B asymptote |
| **L3 구조적 동일성** | Lotka-Volterra predator-prey (R = prey, L = predator, RL = consumed prey) / Receptor-ligand-internalization with biased agonism |
| **L4 생리학적 의미** | kon = molecular collision rate (target accessibility), koff = thermodynamic dissociation, ke(RL) = endosomal trafficking rate |
| **L5 실무 투영** | NONMEM `$DES` 16-line 구조 / Phase 1 dataset richness 요구사항 / NDA 비선형 클리어런스 narrative 작성 / FcRn-engineered mAb의 Cl_L 절감 효과 모델링 |

---

### G. Zettelkasten Atom

```yaml
---
aliases: [Mager-Jusko TMDD, Full 8-Parameter TMDD, PK27 Model]
tags: [pharmacometrics/tmdd, mAb/pkpd-mechanistic, modeling/apex-concept]
up: "[[PK/PD Mastery — Vol I — Session 09]]"
related: ["[[Turnover Paradigm]]", "[[Antibody Distinctive PK]]", "[[TMDD 4-Phase]]", "[[MM Approximation Boundary]]", "[[QE/QSS Approximations]]"]
source: "Mager & Jusko J Pharmacokin Pharmacodyn 2001;28:507–532 / Gabrielsson 5e PK27 / R&T 5e Ch.21 Eq.21-1~21-6"
---

# Full TMDD Model

mAb의 비선형 PK를 mechanistic level에서 표현하는 8-파라미터 4-ODE 시스템: ligand 2-구획(Cl_L, V_c, Cl_d, V_t) + target turnover(R_0, k_out) + binding(k_on, k_off) + complex sink(k_e(RL)).
세 ODE(L, R, RL)가 비선형 결합으로 연결되어 4 페이즈를 동시 generate.
ligand만의 데이터로는 8 파라미터 식별 불가능 — target과 complex 데이터까지 있어야 1–3% precision 도달 (PK27 Table 27.2).
MM 근사로 대체 시 Km이 100배 이상 over-predict될 수 있음 (PK27 Fig.27.6: 0.03 → 3.7).
```

<!-- ANCHOR -->  
이 8-파라미터 framework를 손에 잡았으니, 마지막 Card M5에서는 — 임상 현실에서 target/complex assay가 없을 때 — 어떤 조건에서 MM 근사가 정당화되며 어떤 조건에서 NDA Deficiency로 이어지는지의 정량적 경계를 봐야 한다. 이것이 모든 mAb 모델러가 매일 마주치는 결정의 본질.

<!-- RECAP -->  
**M4 정리**: Full TMDD = 4 ODE(L, L_t, R, RL) + 8 파라미터(Cl_L, V_c, Cl_d, V_t, k_on, k_off, k_e(RL), R_0, k_out). target+complex 데이터 필수. ⚡ Apex Concept. Plausible Fallacy = "MM이 잘 맞으니 안전하다" (Phantom Linearity GOF signature로만 잡힘).

---

## ▌ Card M5 — Michaelis-Menten 근사의 유효 경계

<!-- MASTER LENS -->

### [개념 Big Idea: 거장의 시각]

**왜 치명적으로 중요한가**: 임상 현실에서 90% 이상의 mAb 후보 약물은 target/complex assay가 없거나 cost·sample volume 제약으로 측정 불가하다. 따라서 PopPK 모델러는 거의 항상 reduced 모델을 선택해야 하며, 이때 "MM 근사가 언제 통하고 언제 통하지 않는가"의 정량적 경계를 모르면 맹목적으로 default를 돌리는 것이 된다. PK26 (Efalizumab)이 이 경계를 통과한 사례 vs PK27 (synthetic dataset)이 통과 못한 사례 — 둘의 차이가 임상 모델러의 직업적 가치 그 자체.

**체화해야 할 단 하나의 직관**: MM은 **(Phase B + Phase C) 만 잡는 2-파라미터 cartoon**이다. **Phase A (초기 2차 결합)와 Phase D (terminal koff/ke(RL))를 무시한다.** 따라서 MM 근사가 정당화되는 조건은 정확히 두 가지 — (i) **target occupancy ≥ 90–95%** (Phase B가 거의 모든 시간을 차지 → A·D 무시 가능) 또는 (ii) **C >> R₀** (Phase B가 dominant). 이 둘 중 하나가 성립하지 않으면 MM 사용은 "근사"가 아니라 "구조적 misspecification"이다.

**이 직관을 머릿속에 박고 아래를 읽어라**: PK27의 텍스트는 이 경계를 정확히 한 문장으로 명시한다 — *"If greater than, say 90-95% occupancy is needed, the model can be simplified to a linear first-order disposition model. If the target occupancy is less than Kd (koff/kon) or less than some biomarker potency, then the Michaelis-Menten approximation may not suffice."* (PK27 p.609). 이 경계가 모든 mAb 모델 선택의 헌법.

---

### A. Formal Definition

**Reduced 2-compartment with parallel linear + MM clearance**:

$$\frac{dC_L}{dt} = \frac{1}{V_c}\left[Input_L - Cl_L\cdot C_L - Cl_d\cdot(C_L - C_t) - Cl_{MM}\cdot C_L\right] \quad \text{(Eq.27:4)}$$

with

$$Cl_{MM} = \frac{V_{max}}{K_m + C_L} \quad \text{(Eq.27:5)}$$

이 모델은 Full TMDD의 5개 mechanistic 파라미터 (`R₀, k_on, k_off, k_out, k_e(RL)`)를 2개 phenomenological 파라미터 (`Vmax, Km`)로 압축한다.

---

### B. Derivation / Code Structure

#### B-1. Quasi-Steady-State (QSS) reduction (R&T p.712)

QSS 가정 하에서 `dC_RL/dt ≈ 0`:
$$k_{on}\cdot C_L\cdot R = (k_{off} + k_{e(RL)})\cdot C_{RL}$$

표적 보존(`R + RL = R_tot`) 가정 + steady-state 추가 시:
$$Cl_{MM} = \frac{R_{tot}\cdot k_{e(RL)}}{K_m + C_L}, \quad K_m = \frac{k_{off} + k_{e(RL)}}{k_{on}}$$

따라서 `Vmax = R_tot · k_e(RL)`로 mechanistic하게 해석 가능 — 단, `R_tot`과 `k_e(RL)`을 분리할 수는 없다.

#### B-2. PK27의 정량적 경계 검증 (Fig.27.6, p.609)

| Parameter | True (Full TMDD) | MM 추정 | Bias |
|---|---|---|---|
| `Km` | 0.03 mg·L⁻¹ | **3.7** mg·L⁻¹ | **123× over** |
| `Vmax/Km` (initial slope) | (mechanistic) | (phenomenological) | 차이는 페이즈 의존 |

> **거장의 메모**: 123배 over-prediction은 무슨 의미인가? `Km`은 청소율이 절반 saturate되는 농도. 진짜 `Km = 0.03`이면 `C ≥ 0.3 mg·L⁻¹`에서 saturate되지만, MM 추정 `Km = 3.7`이면 `C ≥ 37 mg·L⁻¹`이 되어야 saturate된다고 예측. **저용량 군 (1.5 mg·kg⁻¹ → 초기 30 mg·L⁻¹)은 MM 모델 입장에서 "아직 saturate 안됨"이지만 실제로는 이미 충분히 saturate 상태.** 이 misclassification이 곡선 형태의 systematic deviation을 만든다. `[출처: Gabrielsson 5e PK27, p.609]`

#### B-3. 두 가지 명시적 경계 조건 (PK27 p.609 직접 인용)

> "If greater than, say **90-95% occupancy** is needed, the model can be simplified to a linear first-order disposition model."  
> "If the **target occupancy is less than Kd (koff/kon)** or less than some biomarker potency, then the Michaelis-Menten approximation **may not suffice**."

**조건 1 (90–95% 점유율 보장)**: 모든 임상 농도 시간 구간에서 `C_L ≥ 9–19 × Kd`. 이 경우 R은 거의 항상 saturate되어 — TMDD가 사실상 1차 비특이 청소만 남는 것처럼 보임. 이때는 단순 linear 1차 모델조차 충분 (MM도 필요 없음).

**조건 2 (점유율이 Kd 또는 biomarker potency 이하)**: MM 근사 부적합. Full TMDD 또는 QSS 사용 필수.

#### B-4. Efalizumab (PK26) 사례 — MM이 정당화된 케이스

- 5개 dose (0.1 ~ 10 mg·kg⁻¹) 중 가장 낮은 0.1 mg·kg⁻¹ (Vc 0.05 L·kg⁻¹ 가정 시 C₀ ≈ 2 mg·L⁻¹)이 추정 `Km = 0.161` 보다 약 12배 높음 → 임상 dose range 전반에서 saturated 영역.
- **결과**: MM 근사로 `Cl_L = 0.007 / Vmax = 0.039 / Km = 0.161` 추정, GOF 양호. 다만 `Km`의 CV%는 44%로 가장 부정확 — **이는 어떤 데이터로도 Km이 well-identified 되지 않음을 의미** (Phase C가 충분히 sample되지 않음).

> **체화 포인트**: PK26은 MM이 통하는 사례의 textbook example이지만, **Km의 CV% 44%는 빨간 깃발**이다. 만약 임상 환경에서 0.05 mg·kg⁻¹ 이하의 매우 낮은 dose가 추가되었다면 MM은 무너졌을 것이다. 즉 PK26은 "운 좋게" 통한 사례이며, low-dose extension에 대한 재평가 의무가 있다.

---

### C. Structural Necessity

왜 MM은 정확히 Phase A와 Phase D를 놓치는가?

- **Phase A (초기 2차 결합)**: `dL/dt = -kon·L·R`. MM은 `R`을 명시적으로 모델하지 않으므로, 이 페이즈의 빠른 dip을 reproduce할 수 없다. MM은 항상 t=0에서 단순 dilution 후 1차 감소로 시작.
- **Phase D (terminal koff·ke(RL))**: 진짜 곡선은 `dL/dt = -ke(RL)·L`로 가파른 slope. MM은 `Cl_L·C_L` (저농도에서 ClMM이 0으로 수렴)만 남아 — 더 완만한 slope. 이로 인해 terminal AUC를 과대평가.

**구조적 핵심**: MM은 `R₀`라는 "stock"을 모델하지 않으므로, target depletion → recovery dynamics 자체를 잡을 수 없다. 따라서 다회 dosing 후 second dose 응답이 first dose와 다른 현상 (target re-saturation 시간) 같은 임상적으로 결정적인 dynamics를 놓친다.

---

### D. Assumptions & Boundary Conditions

- **Single saturable elimination pathway**: 만약 두 개 이상의 target (e.g., bispecific) 이 동시에 작동하면 MM은 single Vmax로 lump → 더 큰 misspecification.
- **Time-invariant Vmax/Km**: target up-regulation (autoimmune flare) 또는 down-regulation (immunosuppression progression)에서 Vmax 시간 변화 → 추정값 bias.
- **No target turnover modeled**: kin/kout이 없으므로 RL의 endogenous target depletion 회복 시간을 모름. 다회 dosing에서 cumulative target loss가 발생해도 MM은 평형 유지로 가정.

---

### E. Limitations

- **저용량 외삽 불가**: NDA submission에서 핵심 — 임상 dose range 위(toxicity 평가)와 아래(MABEL/sensitive subpopulation) 모두에서 MM 외삽은 reviewer가 의심한다.
- **Pediatric extrapolation 위험**: 어린이의 R₀가 다르면 MM의 phenomenological `Km`은 mechanistic 의미를 잃음.
- **Combination therapy 평가 불가**: 두 mAb이 같은 target에 경쟁하면 MM은 단순 Vmax 합산 — 실제로는 binding kinetics 경쟁이 발생.

---

### F. Five Cognitive Layers

| Layer | 내용 |
|---|---|
| **L1 형식적 수학** | Eq.27:4–27:5 / QSS reduction 도출 / Vmax = R_tot · k_e(RL) mechanistic 해석 |
| **L2 기하학적 직관** | MM 곡선은 Phase B–C만 fit / Phase A·D에서 systematic deviation |
| **L3 구조적 동일성** | 효소 반응 MM kinetics와 동형 (E + S → ES → E + P, 여기서 S=ligand, E=target, P=internalized) |
| **L4 생리학적 의미** | Vmax = max receptor turnover rate, Km = effective binding constant inflated by ke(RL) |
| **L5 실무 투영** | mAb PopPK 기본 default — 단, 외삽 영역 검증 필수 / NDA narrative에 "MM approximation valid range" 명시 의무 / Phase 1 sampling이 Phase A·D 커버 못하면 MM choice 자체가 정당화 부족 |

---

### G. Zettelkasten Atom

```yaml
---
aliases: [MM Approximation TMDD, Reduced 2-Compartment TMDD, Parallel Linear+MM]
tags: [pharmacometrics/tmdd, mAb/reduced-model, modeling/approximation-boundary]
up: "[[PK/PD Mastery — Vol I — Session 09]]"
related: ["[[Full TMDD Model]]", "[[QSS Approximation]]", "[[Quasi-Equilibrium]]", "[[NDA Nonlinear Clearance Narrative]]"]
source: "Gabrielsson 5e PK27 Eq.27:4-27:5 (p.607) + R&T 5e p.712"
---

# MM Approximation Validity Boundary

Reduced TMDD 모델 = 2-compartment + parallel linear (Cl_L) + MM (Vmax, Km) clearance.
Full TMDD의 5개 mechanistic 파라미터(R_0, k_on, k_off, k_out, k_e(RL))를 2개로 압축.
유효 조건: (i) target occupancy ≥ 90-95% throughout dose range OR (ii) C >> R_0.
부적합 조건: target occupancy < K_d (k_off/k_on) OR < biomarker potency.
PK27에서 MM이 진짜 K_m=0.03을 3.7로 추정 (123× over) — Phase A와 Phase D를 놓침.
PK26 Efalizumab은 MM 정당화 사례지만 K_m의 CV% 44%는 식별 부족 신호.
NDA 외삽 시 MM 유효 영역을 narrative로 명시 필수.
```

<!-- ANCHOR -->  
이상으로 5개 MUST 카드를 모두 마쳤다. M1(turnover skeleton) → M2(항체 PK 4-게이트) → M3(4-페이즈 곡선) → M4(Full TMDD ⚡ Apex) → M5(MM 유효 경계). 다음 §5에서는 이 카드들이 만들어내는 4개의 가장 위험한 혼동쌍을 해부한다 — 그 중 하나는 NDA Deficiency Letter로 직결된다.

<!-- RECAP -->  
**M5 정리**: MM은 2-파라미터 phenomenological 압축. 유효 조건 = 90–95% occupancy or C >> R_0. 부적합 조건 = occupancy < K_d. 외삽 영역에서 항상 검증.

---

# §5 Confusion Pair Dissection

<!-- CONFUSION -->

## ▌ Pair 1 — Turnover Rate (`R_in`/`k_in`) vs Fractional Turnover Rate (`k_out`)

| 비교 차원 | `k_in` (Turnover Rate) | `k_out` (Fractional Turnover Rate) |
|---|---|---|
| **표면적 유사성** | 둘 다 "rate constant"라는 말이 붙고, 둘 다 turnover system을 정의하며, 둘 다 Eq.2:241에서 비율을 이룸. NONMEM 코드에서 변수명 `KIN`·`KOUT`이 항상 같이 등장. | |
| **수식/코드 형태** | `dA/dt = +k_in − ...`, 단위 [mass·time⁻¹], 절대 input rate | `dA/dt = ... − k_out·A`, 단위 [time⁻¹], fractional rate |
| **생리학적/구조적 지시체** | 합성 효소 활성, 분비 세포 수, 외부 입력 (infusion, sc dose) | proteolytic enzyme activity, GFR, FcRn-회피 분획, target-mediated clearance contribution |
| **변화 방향** (Fig.2.70) | 2배 증가 시 정상상태 `A_0`만 2배 ↑, 도달 시간(`Tss`) **불변** | 2배 증가 시 정상상태 `A_0` 절반 ↓ **and** 도달 시간 **절반 ↓** (둘 다 변함) |
| **임상/모델링 결과** | `k_in` 잘못 해석 → infusion rate 조정으로 정상상태 빨리 도달 가능하다고 오해 → 임상 시간표 misjudgment | `k_out` 잘못 해석 → enzyme inhibitor 효과로 trough만 변한다고 오해, 실제로는 t_{1/2}와 dosing interval 모두 재계산 필요 |
| **⚡ 기억 고리** | **`k_in`은 수도꼭지의 수압 (절대 부피·시간⁻¹). `k_out`은 욕조 마개 구멍의 크기 (분율·시간⁻¹). 수도꼭지를 더 열면 욕조가 더 깊게 차지만 채우는 시간은 같다 — 분율이 안 변했으니까. 마개를 더 열면 깊이도 시간도 동시에 변한다 — 분율이 변했으므로. 이 비대칭성은 Fig.2.70의 좌우 그래프가 다른 모양인 수학적 이유다.** | |

`[출처: Gabrielsson 5e §2.6.1 Fig.2.70, pp.96–97]`

---

<!-- CONFUSION -->

## ▌ Pair 2 — Full TMDD Model vs Michaelis-Menten Approximation ⚡ **CRITICAL BLOW**

| 비교 차원 | Full TMDD (8-parameter) | MM Approximation (2-parameter) |
|---|---|---|
| **표면적 유사성** | 둘 다 mAb의 비선형 PK를 다루고, 둘 다 ligand 데이터에 fit 가능하며, 고용량 영역에서는 거의 같은 곡선을 만듦. GOF plot이 깨끗할 때 시각적으로 구별 어려움. | |
| **수식/코드 형태** | $V_c\frac{dL}{dt} = ... -k_{on}LR + k_{off}RL$ + 3 추가 ODE (Eq.27:1-27:3) | $V_c\frac{dL}{dt} = ... -\frac{V_{max}\cdot L}{K_m + L}$ (Eq.27:4-27:5) |
| **생리학적/구조적 지시체** | `R_0`, `k_on`, `k_off`, `k_out`, `k_e(RL)` 각각이 분자 물리·세포생물 실체에 매핑 | `Vmax`, `Km`은 mechanistic 의미가 lump됨. `Vmax = R_tot · k_e(RL)`로 분리 불가능. |
| **변화 방향** | target up-regulation → R_0 증가 → 비선형 영역 확장 (정성·정량 추적 가능) | target up-regulation → Vmax 어떻게 변할지 불분명, Km 변화 추정 불가 |
| **임상/모델링 결과** | Phase 1 dataset이 4 페이즈 모두 cover하지 않으면 식별 실패 (PK26이 fit 시도했다가 포기) | dataset richness 적으면 사용 가능. 단, 외삽 영역 (저용량·pediatric·long-term trough)에서 systematic bias. |
| **⚡ 기억 고리** | **Full TMDD = 5거울 천체망원경 (R_0, k_on, k_off, k_out, k_e(RL)). MM = 2거울 망원경 (Vmax, Km). 두 망원경 모두 별(임상 농도)은 보이지만, 받침대(target turnover)와 수신기(complex internalization)는 5거울만 본다. NDA 심사관이 받침대 광학 수치를 묻는데 "MM으로 충분합니다"라고 답하면 — 그 즉시 Deficiency Letter. PK27 Fig.27.6의 K_m 0.03 vs 3.7 = 123배 — 망원경 수치가 두 자릿수 다른 것은 노이즈가 아니라 구조적 misspecification.** | |
| 🔴 **치명적 타격** | **MM 근사를 Phase 1/2에서 채택하고, Phase 3 sparse sampling에서 평균 농도가 Km의 30% 미만으로 내려가는 trough population (예: long-interval dosing 또는 weight-based dose에서 hyper-clearance phenotype)을 외삽한 후 NDA 제출 시 — FDA Clinical Pharmacology reviewer가 dose-stratified residual plot을 요청하면 "Phantom Linearity" GOF signature가 즉시 노출된다. Deficiency Letter는 다음 형태로 도착: "The applicant's choice of Michaelis-Menten approximation is not justified for the dose range and target occupancy levels in the proposed dosing regimen. Provide either (i) a target-mediated drug disposition model with sensitivity analyses or (ii) clinical pharmacology evidence that target occupancy exceeds 90% throughout the dosing interval in the population of interest." 이 deficiency 응답에는 6–18개월의 modeling 추가 작업이 소요되며, NDA approval timeline이 직접 지연된다.** | |

`[출처: Gabrielsson 5e PK27 pp.602–610 + R&T 5e p.711–712]`

---

<!-- CONFUSION -->

## ▌ Pair 3 — `K_d` (Dissociation Constant) vs `K_m` (Michaelis-Menten Constant) in TMDD

| 비교 차원 | `K_d = k_off/k_on` | `K_m = (k_off + k_e(RL))/k_on` |
|---|---|---|
| **표면적 유사성** | 둘 다 nM 수준의 affinity 단위, 둘 다 PK27 Fig.27.5의 두 horizontal dashed line으로 표시되며, 둘 다 binding strength를 묘사하는 듯 보임. 차이가 항상 두 자릿수 미만이라 시각적으로 가까움. | |
| **수식/코드 형태** | $K_d = k_{off}/k_{on}$ — 두 binding rate의 ratio | $K_m = (k_{off} + k_{e(RL)})/k_{on}$ — koff에 internalization sink가 추가됨 |
| **생리학적/구조적 지시체** | 화학자의 thermodynamic equilibrium constant — pure binding affinity | 효소학자의 kinetic constant — binding + 결합 후 운명 (internalization) 모두 반영 |
| **변화 방향** | FcRn engineering (binding affinity 증가) → k_on ↑ → K_d ↓. Internalization 영향 없음. | 같은 engineering이라도 ke(RL) 변화 없으면 K_m도 K_d 따라 ↓. 그러나 ADC payload conjugation으로 ke(RL) ↑ → K_m도 ↑ (K_d 변화 없이) |
| **임상/모델링 결과** | K_d로 receptor occupancy 계산 시: `occupancy = C/(C + K_d)` — 순수 결합 평형 가정. | K_m으로 동일 계산 시: 실제 K_m > K_d이므로 occupancy 과소평가. **0.03 vs 0.01 = 3배 — 약물의 occupancy를 33% 낮게 보고할 위험.** |
| **⚡ 기억 고리** | **K_d는 thermodynamics (정적), K_m은 kinetics (동적). 차이는 `k_e(RL)` 하나 — "결합 후 출구". K_d는 binding affinity만 측정 (BLI/SPR로 측정 가능), K_m은 cellular machinery까지 포함 (cell-based assay 또는 PK27 같은 in vivo PK fitting으로만 추출). `k_e(RL) → 0`이면 두 상수 일치 — 즉 internalization이 매우 느린 soluble target의 경우 K_d ≈ K_m. 막결합 receptor의 internalization이 빠르면 K_m >> K_d로 갈라짐. PK27의 0.01 vs 0.03 차이는 정확히 ke(RL)/kon = 0.02의 contribution.** | |

`[출처: Gabrielsson 5e PK27 Fig.27.1, p.603 + Eq.27:5–27:6]`

---

<!-- CONFUSION -->

## ▌ Pair 4 — Linear PK at Low Concentration vs Linear PK at High Concentration in TMDD

| 비교 차원 | Linear PK at very low C (Phase D 이후) | Linear PK at very high C (Phase B) |
|---|---|---|
| **표면적 유사성** | 둘 다 semi-log plot에서 일직선 (1차 동역학), 둘 다 PK27 Fig.27.3의 위·아래 양 끝에 "Linear PK" 라벨, 둘 다 단순 1-구획 모델로 fit 가능. 학습 초기 혼동 1순위. | |
| **수식/코드 형태** | `dL/dt ≈ -(Cl_L/V_c)·L − (R_0·k_e(RL))·L` (양 트랙 평행 1차) | `dL/dt ≈ -(Cl_L/V_c)·L` (단일 1차) |
| **생리학적/구조적 지시체** | **Parallel routes**: 비특이 청소(`Cl_L`) + R-mediated 청소(R 모두 free, R-binding 1차로 작동) 모두 active. R이 saturate되지 않은 상태. | **Single route**: 비특이 청소만 작동. R이 모두 RL로 묶여 free R ≈ 0. R-mediated route가 정지. |
| **변화 방향** | Cl_total = Cl_L + R_0·k_e(RL) — 두 항 합 (Fig.27.3 right plateau 1, 더 높음) | Cl_total = Cl_L — 한 항만 (Fig.27.3 right plateau 2, 더 낮음) |
| **임상/모델링 결과** | 저용량 phase 1 cohort에서 관찰. **이 영역의 1차 slope에서 `R_0·k_e(RL) = Vmax`를 추정 가능 (단, 이 영역에 도달할 만큼 sampling이 충분한 경우만)**. 저용량 cohort 누락 시 Vmax 추정 자체가 불가. | 고용량 cohort에서 관찰. 이 영역에서만 fit해도 비특이 청소만 추정 가능 — 비선형성을 놓침. **고용량만 보고 "linear PK입니다"라고 보고하면 saturation 메커니즘 자체를 인지하지 못함.** |
| **⚡ 기억 고리** | **양 끝 다 "linear"라는 단어가 붙지만, 한쪽은 두 갈래 평행 고속도로(Cl_L 차선 + R 차선 동시 운행), 다른 쪽은 한 갈래 단일 고속도로(Cl_L 차선만 살아있고 R 차선은 정체로 ke(RL) bottleneck에 갇힘). Fig.27.3 right의 Cl_total vs C plot에서 양 끝 plateau의 높이 차이가 정확히 R-mediated 기여분(Vmax/Km in MM, R_0·k_e(RL) in mechanistic). 이 차이를 "linear vs linear"로 보면 정보 손실 — 차이를 "병렬 vs 잔존"으로 봐야 임상에서 dose escalation의 의미를 읽는다.** | |

`[출처: Gabrielsson 5e PK27 Fig.27.3, p.604 + Fig.27.7, p.610]`

---

# §7 Self-Test: Active Recall Module

<!-- SELF-TEST -->

## Q1 (★★, 회상)

**질문**: Eq.2:237의 turnover ODE `dA/dt = k_in − k_out·A`에서, `k_in`을 2배로 증가시킨 후 새로운 정상상태에 도달하는 시간(`T_ss`)이 변하지 않는 이유를 1차 동역학적으로 설명하라. 또한 `k_out`을 2배로 변경했을 때 `T_ss`와 정상상태 `A_0`가 어떻게 변하는지 정량적으로 답하라.

<details>
<summary>정답 공개</summary>

새로운 정상상태 도달 시간은 시스템의 시간 상수에 의해 결정되며, 1차 동역학 시스템에서 이 시간 상수는 `1/k_out`이다 (`T_ss ≈ 4–5 × 1/k_out`). `k_in`은 시스템의 forcing function일 뿐 시간 상수에 영향을 주지 않으므로, `k_in` 변경 시 새로운 `A_0 = k_in/k_out`만 바뀌고 `T_ss`는 불변. 반면 `k_out`을 2배로 늘리면: (i) 새로운 `A_0 = k_in/(2·k_out) = A_0/2` (정상상태 절반으로 감소), (ii) 새로운 `T_ss ≈ 4/(2·k_out) = T_ss/2` (도달 시간도 절반). 이것이 Fig.2.70의 좌우 비대칭의 정확한 수학적 근거.

**다음 깊이 질문**: 이 비대칭성을 임상에 적용하면 — albumin 합성률 30% 감소 환자(간경변)와 albumin 분해 효소 30% 항진 환자(catabolic state)를 같은 hypoalbuminemia로 보지만, infusion 기반 supplementation의 효과 시간표가 두 환자에서 어떻게 다를까?
</details>

---

## Q2 (★★, 회상)

**질문**: Full TMDD model의 4개 ODE를 모두 적고, 각 ODE에서 `k_on·C_L·R` term이 어떻게 (어떤 부호로) 등장하는지 표로 정리하라. 이 부호 일관성이 무엇을 보장하는가?

<details>
<summary>정답 공개</summary>

| ODE | `k_on·C_L·R` term 부호 |
|---|---|
| `dC_L/dt` | **−** (ligand가 binding으로 사라짐) |
| `dC_t/dt` | (없음 — tissue compartment는 binding과 무관) |
| `dR/dt` | **−** (target이 binding으로 사라짐) |
| `dC_RL/dt` | **+** (complex가 binding으로 생성됨) |

부호 일관성 규칙: ligand 1 mole + target 1 mole → complex 1 mole (1:1 stoichiometry). 따라서 ligand에서 1 mole 사라지면 target에서도 1 mole 사라지고 complex로 1 mole 나타남. 이 부호 패턴이 **mass conservation**을 enforce하며, 코드에서 한 곳의 부호를 잘못 쓰면 mass가 spontaneously 생성/소멸 → NONMEM `MINIMIZATION FAILED` 또는 비물리적 농도 발생 (negative R 등).

**다음 깊이 질문**: 만약 receptor가 dimerizing target (2 ligand per receptor) 이면 이 부호 패턴이 어떻게 수정되는가? bispecific antibody는?
</details>

---

## Q3 (★, 회상)

**질문**: PK27 Table 27.2에서 dataset I (ligand only) → dataset III (ligand+target+complex)로 가면서 `k_off`의 CV%가 27% → 13% → 3%로 개선된다. 이 개선의 mechanistic 이유를 한 문장으로 답하고, **이 데이터 의존성이 임상 mAb 프로그램의 assay 개발 우선순위에 주는 implication**을 한 문장으로 더하라.

<details>
<summary>정답 공개</summary>

`k_off`는 `RL`이 `L`과 `R`로 분해되는 속도이므로 `RL` 농도-시간 곡선에서만 직접 정보를 얻을 수 있으며, ligand나 target만 측정해서는 dissociation dynamics가 다른 source(diffusion, target turnover)와 confound된다 — complex assay가 추가되어야 `k_off`가 isolated.

임상 implication: mAb 후보의 Phase 1 protocol에서 free target 및 ligand-target complex assay 개발은 ligand assay와 동일한 우선순위로 다뤄져야 한다. Complex assay 부재는 모든 mechanistic 파라미터의 위계적 식별 실패를 강제하며 (PK26 Efalizumab 사례), 결국 reduced 모델 사용을 강요받게 되는데, 이는 외삽 영역에서의 NDA reviewer 질의에 대비할 수 없게 만든다.

**다음 깊이 질문**: complex assay가 비용·sample volume 제약으로 일부 cohort에서만 가능하다면, optimal experimental design (e.g., D-optimality, Fisher information)으로 어떤 dose·시간점에 complex 측정을 할당해야 가장 큰 식별 가능성 이득을 얻는가?
</details>

---

## Q4 (★★, 적용)

**질문**: 당신은 새로운 mAb 후보 약물(soluble cytokine 표적, R₀ 추정 0.5 nM, K_d 0.05 nM, k_e(RL) 추정 0.001 min⁻¹)의 Phase 1 PK 결과를 분석하고 있다. 0.1 mg·kg⁻¹ dose에서 t=1h trough 농도가 5 nM, t=72h trough 농도가 0.5 nM로 측정되었다. 이 데이터에 대해 **MM 근사를 사용해도 정당화되는가?** PK27 p.609의 두 정량적 경계 조건을 직접 적용하여 답하라.

<details>
<summary>정답 공개</summary>

PK27 두 경계 조건:  
(i) target occupancy ≥ 90–95%: `occupancy = C/(C+K_d)`. t=1h: 5/(5+0.05) = 99% ✓ ; t=72h: 0.5/(0.5+0.05) = 91% ✓ (두 시점 모두 통과).  
(ii) target occupancy < K_d (0.05 nM)인 영역이 있는가: 측정된 가장 낮은 농도 0.5 nM이 K_d의 10배 — 이 데이터 범위 안에서는 occupancy < K_d 영역 없음 ✓.

**결론**: 측정된 데이터 범위 내에서 MM 근사는 **잠정적으로 정당화**됨. 그러나 두 가지 caveat:  
(a) t=72h 이후 trough가 더 낮아지면 (예: dosing interval 연장) 이 정당화는 깨질 수 있음.  
(b) Phase 1 cohort 외 — 어린이, 신부전 환자, weight-based dose에서 hyper-clearance phenotype — 에서는 R_0가 다를 수 있어 외삽 부적절.

**임상 결정**: 현 데이터로 MM 사용 가능, 단 NDA narrative에 "MM approximation valid range: C_L ≥ 0.5 nM, equivalent to ≥10·K_d"를 명시하고, sub-population (특히 long dosing interval)에서 sensitivity analysis로 Full TMDD와 비교해야 함.

**다음 깊이 질문**: 만약 t=72h trough가 0.05 nM (K_d와 같음)으로 측정되었다면 결론이 어떻게 바뀌는가? 이 시점에서 occupancy는 50%이며 정확히 PK27 경계 조건 (ii)의 violation 임계점.
</details>

---

## Q5 (★★, 적용)

**질문**: PK26의 `K_m` 추정값 0.161 mg·L⁻¹의 CV%가 44%이다. 이 정밀도 부족이 의미하는 것은 무엇이며, 왜 다른 파라미터(`Cl_L` 10%, `Vmax` 12%)는 잘 식별되었는데 `K_m`만 부정확한가? Fig.27.3의 4-페이즈 구조를 사용하여 답하라.

<details>
<summary>정답 공개</summary>

`K_m`은 4-페이즈 구조에서 Phase C (mixed-order transition)의 곡률을 결정하는 파라미터다. Phase B (high C, target saturated, MM에서 ClMM ≈ Vmax/C → Vmax 정보)와 Phase D 부근 (low C, 만약 잘 sampled되면)에서 추출 가능하지만, **Phase C 자체는 좁은 농도/시간 영역**이며 PK26의 5개 dose가 충분히 dense하지 않다면 이 transition zone이 sparse하게 sampled됨.

`Cl_L`은 가장 낮은 dose (0.1 mg·kg⁻¹)의 terminal phase에서 추정 가능 (TMDD 트랙이 거의 saturate되기 어렵지만 어느 정도 정상 1차 회귀로 수렴) — 따라서 잘 식별.  
`Vmax`는 high-dose Phase B에서 ClMM의 lower asymptote (Cl_L 외 추가 청소)로 잘 추정.  
`K_m`은 **Phase B와 Phase D 사이의 transition curvature**가 dense하게 sampled 되어야만 식별 가능 — PK26 데이터가 이 영역에서 sparse하기 때문에 CV% 44%.

**임상 implication**: PK26의 결과를 NDA에 인용할 때 `K_m`에 대한 sensitivity analysis가 필수이며, 외삽 시 `K_m`의 95% CI를 propagate해야 한다. 만약 어떤 용량에서 농도가 K_m의 lower CI 한계 (예: K_m = 0.05) 부근에 있다면 비선형 영역에 들어가는 것으로 봐야 한다.

**다음 깊이 질문**: 이런 식별 실패를 미리 진단할 수 있는 design tool은? (답: Fisher information matrix 기반 D-optimal design, 또는 prospective sensitivity analysis using simulated likelihood profile).
</details>

---

## Q6 (★, 적용)

**질문**: 한 동료가 새로운 항체의 cynomolgus monkey 데이터를 보여주며 "전형적인 2-구획 PK이고 CL=6 mL·h⁻¹·kg⁻¹, Vss=4 L·kg⁻¹입니다"라고 보고했다. Gabrielsson §2.6.2 (p.99)의 경고를 적용하여, 이 보고에서 의심해야 할 점을 한 가지 지적하라.

<details>
<summary>정답 공개</summary>

Vss = 4 L·kg⁻¹는 항체로서 매우 큰 분포 부피이며 (Table 21-6에서 대부분의 mAb가 0.04–0.1 L·kg⁻¹ 범위), 이는 항체가 plasma+ECF에 거의 제한된다는 일반 원칙과 모순된다. Gabrielsson §2.6.2 p.99의 경고: "When the rate constant for redistribution k_21 is much less than the rate constant of irreversible antibody elimination in the peripheral compartment k_20, V_ss will be incorrectly estimated [by the standard mammillary 4-parameter model]". 즉 항체가 tissue throughout the body에서 분해되는 것이 알려져 있는데, central elimination만 가정하는 표준 모델로 fit하면 V_ss가 인위적으로 부풀려진다. **이 보고서의 V_ss = 4 L·kg⁻¹는 진짜 분포 부피가 아니라 모델 misspecification의 가능성이 높다** — 추가 tissue distribution 데이터 (e.g., radiolabeled mAb biodistribution) 없이는 받아들일 수 없다.

**다음 깊이 질문**: tissue catabolism이 dominant하다면 어떤 모델 구조가 적절한가? (답: peripheral compartment에서 elimination, 또는 PBPK with organ-specific catabolic rates).
</details>

---

## Q7 (★, 적용)

**질문**: PK27 Fig.27.7의 Phase A에서 `dL/dt ≈ -k_on·L·R`이다. 이 페이즈 동안 ligand의 농도-시간 그래프 모양을 정성적으로 묘사하라. 또한 1.5 mg·kg⁻¹ dose에서 이 페이즈가 더 두드러지게 보이는 (Fig.27.1 right inset의 dashed circle) 이유를 설명하라.

<details>
<summary>정답 공개</summary>

Phase A는 second-order kinetics이므로 농도가 매우 빠르게 떨어지지만 **순수 1차가 아닌 더 가파른 초기 dip** 후 slope이 점차 완화되는 형태. 곡선 모양은 logistic function의 거울상 비슷 — t=0 근처에서 매우 가파르게 감소하다가 R이 고갈되면서 Phase B로 부드럽게 전이.

1.5 mg·kg⁻¹ dose에서 더 두드러진 이유: 초기 농도 C₀ = 1500/(0.05 L·kg⁻¹·1000) ≈ 30 mg·L⁻¹로, R₀ = 12 mg·L⁻¹와 같은 자릿수. 따라서 R이 빠르게 saturate되지 않고 binding이 여러 시간 동안 의미 있게 진행 — Phase A의 dip이 시간적으로 길어짐 (관측 가능). 반면 45 mg·kg⁻¹ dose에서 C₀ ≈ 900 mg·L⁻¹ >> R₀ = 12 → R이 거의 즉시 saturate되어 Phase A가 시간적으로 너무 짧아 관측 불가, Phase B로 직접 보임.

**다음 깊이 질문**: Phase A를 임상 sampling으로 잡으려면 t=0–24h 동안 어떤 sampling density가 필요한가? sparse PopPK study에서 이를 어떻게 보강할 수 있는가?
</details>

---

## Q8 (★★, 적용 — 복합)

**질문**: M3·M4·M5를 통합하라. 한 mAb 후보가 다음 데이터를 보인다:  
- Phase 1: 5개 dose (0.01, 0.1, 1, 10, 100 mg/kg) ascending IV bolus  
- 0.01 mg/kg cohort에서 t_{1/2} = 2일, 0.1 mg/kg cohort에서 t_{1/2} = 5일, 100 mg/kg cohort에서 t_{1/2} = 21일  
- target/complex assay 없음  

이 데이터를 보고 **(a) TMDD 존재 여부, (b) Full TMDD vs MM 모델 선택, (c) 만약 MM 사용한다면 외삽 영역의 신뢰성을 어떻게 보고할지** 답하라.

<details>
<summary>정답 공개</summary>

**(a) TMDD 존재**: 명확한 증거. dose-dependent t_{1/2}는 비선형 PK의 hallmark이며, 저용량에서 짧고 고용량에서 긴 패턴은 정확히 TMDD 시그니처 (저용량에서 R-mediated 청소 우세 → 빨리 사라짐, 고용량에서 R 포화 → 비특이 청소만 → 21일 IgG-typical t_{1/2}). t_{1/2}의 10배 변동은 단순 covariate effect로 설명 불가.

**(b) 모델 선택**: target/complex assay 부재로 Full TMDD는 식별 불가 (PK26과 동일 상황). 따라서 Reduced 2-cmt + parallel linear+MM 사용 강제. 단, **R_0와 mechanistic 파라미터는 추정 불가**임을 protocol에 명시하고, in vitro binding studies (SPR/BLI for K_d), tissue imaging (radiolabeled biodistribution for R_0 surrogate)를 보완 evidence로 사용.

**(c) 외삽 영역 신뢰성 보고**:  
- 임상 dose range 내 (`C_L`이 추정 K_m보다 10배 이상 높은 영역)에서만 1차 결론 도출.  
- 외삽 범위 (lower trough, pediatric, hepatic/renal impairment subpopulation)에서는 반드시 sensitivity analysis: K_m을 ±50%, ±90% 변동시켜 PD endpoint 변동 확인.  
- NDA narrative에 명시: "The MM approximation is empirically supported within the studied dose range. Extrapolation to dose intervals or patient subpopulations resulting in trough concentrations below [K_m × 5] should be evaluated through targeted clinical studies or mechanistic TMDD modeling supported by additional target/complex measurements."

**다음 깊이 질문**: 0.001 mg/kg microdose study가 가능하다면 어떤 정보를 추가로 제공하며, 이것이 모델 선택에 어떻게 영향을 주는가?
</details>

---

## Q9 (★, 회상)

**질문**: IgG의 t_{1/2}가 23일로 다른 면역글로불린 (IgA 5.8일, IgM 5.1일, IgE 2.5일)보다 4–10배 긴 메커니즘을 한 단어로 답하고, 이 메커니즘이 mAb 약물 엔지니어링에 어떻게 활용되는지 한 문장으로 답하라.

<details>
<summary>정답 공개</summary>

**메커니즘**: FcRn salvage (Brambell receptor pH-dependent recycling).

**엔지니어링 활용**: mAb의 Fc 영역에 point mutation을 도입하여 FcRn 친화도를 정상 IgG 대비 2–10배 증가시키면 endothelial endosome에서 더 많은 분획이 분해를 회피·재순환하여 t_{1/2}를 21일 → 30–40일로 연장 가능 (next-generation biologics, 예: 변이된 IgG-Fc를 가진 차세대 mAb).

**다음 깊이 질문**: FcRn 친화도를 무한정 늘리면 무엇이 한계가 되는가? (답: target tissue penetration 감소 — recycling이 너무 강하면 capillary endothelium에서 빠져나오지 못함).
</details>

---

## Q10 (★★, **보스 딜레마 — Socratic Dilemma**)

**질문 (final question)**:

당신은 신약개발 회사 PopPK 그룹 리드이다. 10억 달러 규모의 Phase 3 mAb 프로그램이 NDA 제출 6개월 전이다. 임상 데이터셋은 ligand 농도만 갖고 있고 (target/complex assay는 Phase 1에서 부분적으로만 측정됨), 현재까지 PopPK 모델은 reduced 2-compartment + parallel linear + MM (PK26 패턴)으로 fit되어 있으며 GOF는 깨끗하다.

당신은 두 가지 선택지에 직면한다:

**선택 A — "MM 모델 그대로 NDA 제출"**: 표준 reviewer 검토를 거치되, 외삽 영역(pediatric extension, weight-based dosing의 underweight subpopulation, long dosing interval option)에서 Phantom Linearity GOF signature가 잡힐 위험이 있다. Deficiency Letter 가능성 30%, 그 경우 6–18개월 지연 + 추가 modeling 비용 200만 달러. 발견되지 않으면 on-time approval.

**선택 B — "Full TMDD model 추가 개발 후 sensitivity analysis로 둘 다 제출"**: Phase 1의 부분 target/complex 데이터를 활용해 informative prior (e.g., R_0와 K_d는 prior, 나머지는 estimate)로 partial Full TMDD fit. 이로 인해 NDA 제출이 4개월 지연됨 (확정 비용). 그러나 reviewer가 외삽 영역 질의 시 즉시 응답 가능, deficiency 위험 < 5%.

**어느 선택지를 택할 것인가? 그 결정을 어떻게 규제 문서에서 방어할 것인가?**

<details>
<summary>정답 공개 — 거장의 Trade-off 논리</summary>

이 문제에 단순한 정답은 없다. 그러나 수석 모델러의 결정 framework는 다음과 같다:

**선택 B를 택한다 — 단, 한 가지 단서 하에서**:

수석 모델러의 reasoning chain은 다음과 같이 진행된다:

1. **위험 가중 기댓값**: 선택 A의 기대 비용 = (30% × $200M ROI loss + $2M modeling cost + 12개월 지연 효과) ≈ $60M+ 위험. 선택 B의 비용 = 4개월 지연 (확정) ≈ $X (회사에 따라 다르지만 일반적으로 $20–40M). **선택 B가 절대 비용 측면에서 더 작다.**

2. **장기 평판 효과**: NDA Deficiency Letter는 회사의 향후 mAb 프로그램에서 reviewer scrutiny를 영구적으로 높인다. 한 번 "이 회사는 비선형성을 cut corner한다"는 평가가 reviewer pool에 형성되면, 다음 5–10개의 mAb 제출 모두 더 엄격한 검토를 받게 됨. 이 평판 효과의 NPV는 수억 달러 단위.

3. **결정의 규제 문서 방어**: 선택 B를 택한 narrative — *"In recognition of the limitations of the Michaelis-Menten approximation for extrapolation beyond the studied dose-concentration range (Peletier & Gabrielsson 2012; Gabrielsson 5e PK27), we developed a partial TMDD model utilizing informative priors derived from in vitro binding studies (K_d) and Phase 1 target measurements (R_0). Sensitivity analyses comparing the Full TMDD and reduced MM models demonstrate that key extrapolation predictions [pediatric subpopulation, long-interval dosing, weight-based dosing in lower-percentile patients] remain robust within ±15% across both modeling frameworks. The reduced MM model is retained as the primary analysis given its computational efficiency for routine population dosing simulations, with the Full TMDD model serving as the mechanistic verification."*  
   이 narrative는 (i) 두 모델 모두 사용했음을 명시, (ii) 한쪽의 한계를 학술 문헌으로 인정, (iii) 외삽 영역에서 두 모델의 일치를 정량적으로 보장 — reviewer가 추가 질의할 여지를 사전 차단.

4. **단서**: 만약 임상 데이터가 정말로 high-occupancy regime (모든 trough > 10·K_d)에 머물러 있고, pediatric/extension은 별도 study로 나중에 다룰 계획이라면, 선택 A도 정당화 가능. 그 경우 NDA narrative에 "MM approximation valid within the dose range studied; sub-populations and dose modifications outside this range will be evaluated in dedicated post-approval studies"를 명시하고 reviewer pre-meeting에서 사전 alignment 추구.

**핵심 통찰**: 이 결정은 "어느 모델이 더 정확한가"가 아니라 "**규제 환경에서 어떤 결정의 방어 가능성이 더 높은가**"의 문제다. 모델러는 데이터의 정확성뿐 아니라 **결정의 외부 검토 가능성** (audit trail, 외삽의 명시적 한계, reviewer가 anticipated questions에 대한 사전 답변)을 함께 설계해야 한다.

이것이 NONMEM을 돌릴 줄 아는 주니어 모델러와 — 규제 위험·장기 평판·자원 할당을 동시 최적화하는 — 수석 모델러의 차이다.

</details>

---

# §8 Meta-Frame & Big Picture

## A. Positioning (28-session 아키텍처 내 위치)

### 본 세션이 전제하는 선행 지식 (이미 체화 완료)

- **1구획·2구획 선형 PK** (Cl, Vd, t_{1/2}, MRT) — Card M2의 항체 PK 4 게이트가 이 위에 얹힘
- **Michaelis-Menten 효소론** (Vmax, Km, saturation kinetics) — Card M5의 MM 근사는 효소론의 PK 응용
- **ODE 기본 + Runge-Kutta 적분** — Card M4의 4-ODE 시스템 수치해
- **General ADVAN/`$DES` 구조** (Session II-04) — Card M4의 NONMEM 구현
- **Turnover paradigm 친숙성** (이전 단편적 노출) — Card M1에서 정식화

### 바로 다음에 오는 세션 (immediate next)

- **Indirect Response PD models** (Sharma & Jusko, Dayneka et al) — Card M1의 turnover skeleton이 PD response variable로 직접 확장됨. body temperature §2.6.6의 8-OH-DPAT 모델이 정확히 이 다리.
- **Quasi-steady-state TMDD approximations** (Gibiansky et al) — Card M5의 MM 근사를 mathematically rigorous하게 일반화

### 이 기반에 결정적으로 의존하는 고급 도메인

- **mAb PopPK 모델링**: Card M3·M4가 PopPK 모델 구조의 직접적 토대. IIV on R_0, k_e(RL) 등이 inter-patient variability의 mechanistic 해석.
- **PBPK for biologics**: Card M2의 림프관·FcRn 메커니즘이 organ-specific compartment design의 출발점.
- **QSP (Quantitative Systems Pharmacology)**: Card M4의 Full TMDD가 receptor occupancy → downstream signaling cascade로 확장되어 전체 immune response 모델 또는 종양 성장 모델과 결합.
- **Bispecific antibody / ADC 모델링**: 단일 target TMDD (Card M4)가 multi-target 또는 payload-conjugate variant로 확장.
- **FcRn engineering 시뮬레이션**: Card M2의 FcRn salvage가 t_{1/2} 연장 전략의 정량 framework.

## B. Dependencies — 이 섹션을 대충 넘겼을 때 발생하는 구체적 실패 모드

**실패 1: PopPK 모델 선택 시 MM을 default로 채택하고 외삽 영역 검증 누락**
- 메커니즘: Card M5의 정량적 경계 조건(90–95% occupancy / C >> R_0 / occupancy < K_d)을 내면화하지 못하면, MM을 모든 mAb의 default로 적용하게 됨. 임상 dose range 내에서는 GOF가 깨끗해 문제가 보이지 않음.
- 임상 trace: NDA 제출 → reviewer가 pediatric/elderly subpopulation 외삽 요청 → "Phantom Linearity" GOF signature 노출 → Deficiency Letter → 6–18개월 지연 + 추가 modeling 자원 200만 달러 손실.

**실패 2: TMDD 4-페이즈 구조를 인식하지 못하고 dose-dependent t_{1/2}를 "이상한 데이터"로 처리**
- 메커니즘: Card M3의 4-페이즈 구조를 모르면 저용량 cohort에서 t_{1/2}가 짧고 고용량 cohort에서 길게 보이는 현상을 noise·assay artifact로 오해. 이를 outlier removal로 처리하거나 dose-stratified separate fit으로 회피.
- 임상 trace: TMDD 시그니처 자체를 인지하지 못함 → Phase 2 dose selection이 잘못된 모델 (dose-independent linear PK)에 기반 → Phase 3에서 trough concentrations이 예측보다 훨씬 낮은 sub-population 발견 → efficacy underperformance → trial failure 또는 dose redesign 필요.

**실패 3: Full TMDD model을 ligand-only 데이터로 fit 시도하여 식별 실패 발생, 원인을 찾지 못해 무작위 fixing**
- 메커니즘: PK27 Table 27.2의 식별 위계 (ligand → +target → +complex로 CV% 감소)를 모르면, Full TMDD가 ligand-only에서 fit 안 되는 이유를 algorithmic 문제로 오해 → `k_off`, `k_e(RL)`을 무작위 값으로 fix하거나 `$OMEGA`를 강제 0으로 설정 → 결과 파라미터 추정값이 mechanistic 의미 잃음.
- 임상 trace: 보고서에 "TMDD model successfully fit"이라고 기재되었으나 사실상 부분적으로 fixed parameter set의 manual tuning. 외부 검토(internal QA, 외부 컨설턴트, FDA reviewer) 시 즉시 발견 → 회사 내부 평판 손상 + project re-do.

## C. Professional Moat — 본 세션의 직접 답변

> NONMEM에서 reduced 2-compartment + MM 모델을 fit하고 GOF plot을 생성할 수 있는 주니어 모델러는 이미 자동화 가능한 경쟁자이며, AI는 표준 mAb dataset에서 이 fit을 수 분 만에 produces한다. 본 세션의 8-파라미터 Full TMDD 시스템 (Card M4)과 그 유효 경계 (Card M5)를 — mechanistic level에서, 4-페이즈 구조 (Card M3)에 매핑된 채로 — 진정으로 내면화한 모델러는 그 둘 중 어느 것도 복제할 수 없는 무엇을 갖고 있는가?

**구조적 필연성 수준의 답**: 본 세션을 체화한 모델러는 다음 4가지를 동시에 수행할 수 있다. AI도 주니어도 이 동시성을 갖지 못한다.

**(1) 모델 선택의 mechanistic 정당화 — narrative 작성 능력**:  
"왜 MM을 선택했는가?"에 대해 — Phase 1 데이터 농도 분포의 95% 분위수가 추정 K_m의 10배 이상에 머무르며, K_d의 mechanistic floor (in vitro SPR로 측정한 0.5 nM)가 임상 trough보다 100배 낮음을 sensitivity analysis로 verify 가능. 이를 NDA의 Clinical Pharmacology Section 5.3.2에 6단락으로 작성. 이것은 mechanistic 이해 없이 textbook formula 암기로는 작성 불가능.

**(2) Phase 1 sampling design의 식별 가능성 의식 설계**:  
신규 mAb 후보의 FIH 프로토콜에서 — target과 complex assay 비용이 sample당 $X로 제약될 때 — D-optimal design 원칙을 활용하여 어떤 시간점에 어떤 measurement를 할당할지 결정. PK27 Table 27.2의 식별 위계를 prior로 활용하여, 단순한 dense sampling이 아닌 구조적 정보 기반 sampling 계획. 이것이 protocol 비용을 절반 이하로 줄이면서도 8 파라미터 식별 가능성을 보장.

**(3) GOF plot을 시각으로만 보는 게 아니라 4 페이즈 진단으로 읽는 능력**:  
표준 GOF (DV vs PRED, CWRES vs IPRED) 외에 **dose-stratified residual plot**과 **time-stratified residual plot**을 자동으로 추가 검토. "Phantom Linearity" 시그니처 (Card M4 C-2)를 시각적 패턴으로 즉시 인식. 이것은 AI가 표준 GOF 검토 알고리즘에서 못 잡는 미묘한 미스피케이션이며, 인간 모델러의 patterned domain expertise.

**(4) 비선형 PK 보고서를 "linearity가 깨지는 이유"의 mechanistic narrative로 작성**:  
"비선형 PK가 관찰됨"이라는 phenomenological 기술이 아니라, "TMDD에 의한 비선형성으로, 임상 dose range의 lower bound에서 target occupancy가 95% 미만으로 떨어지면서 R-mediated clearance contribution이 active해지는 것이 그 메커니즘"이라는 **mechanistic 진단**을 작성. 이 진단 능력은 — 같은 데이터를 두 모델러가 보아도 — 한쪽은 "데이터 fit이 잘 됨"이라고 보고하고 다른 쪽은 "외삽 신뢰성의 정량적 한계"를 보고하게 만드는 결정적 차이.

이 4가지 능력의 조합은 — 그것이 정확히 본 세션 5개 카드의 통합 — 자동화 불가능한 직업적 가치이며, mAb era에 PK 모델러가 사라지지 않는 이유다.

---

✦ STEP 1 완료.

다음이 준비되었습니다:
  • §1 세션 헤더 & 로드맵 (Big Idea 1문장 + 개념 항법도 + 28-세션 그래프 위치)
  • §2 개념 해부 카드 (5개 MUST 카드: M1 Turnover Paradigm / M2 Antibody Distinctive PK / M3 TMDD 4-Phase Profile / M4 Full TMDD Model / M5 MM Approximation Boundary, **Apex: M4 Full TMDD Model**)
  • §5 혼동 쌍 해부 (4개 쌍: kin/kout / Full vs MM / Kd vs Km / Low-C Linear vs High-C Linear, **Critical Blow 적용: Full TMDD vs MM Approximation**)
  • §7 자기 테스트 (10개 질문 — 회상 4 / 적용 5 / 보스 딜레마 1, **보스 딜레마: NDA 6개월 전 모델 선택 트레이드오프**)
  • §8 메타프레임 & 빅 픽처 (Positioning + 3가지 실패 모드 + Professional Moat 4-능력 분석)
  • 감지된 소스 유형: 혼합 — Vol I (Gabrielsson §2.6 + PK26 + PK27 = 수식·데이터 / R&T Ch.21 = 임상·생리)
  • Data Anchoring 소스: PK26 Efalizumab 5 i.v. doses(0.1–10 mg·kg⁻¹), PK27 monoclonal antibody 4 doses(1.5/5/15/45 mg·kg⁻¹) + 8-parameter ODE system, Gabrielsson Table 2.11 5 immunoglobulins(IgG t_{1/2}=23일), R&T Table 21-15 mAb sc bioavailability(Adalimumab F=0.64), R&T Fig.21-5 FcRn salvage mechanism

CONTEXT 흡수: §2.6.1 욕조 비유, §2.6.3 IgX sc, §2.6.4 estradiol postmenopausal, §2.6.5 Comparison Table 2.13, §2.6.6 body temperature, §2.6.7 feedback, R&T Tables 21-1/21-3/21-9/21-12, R&T Fig.21-3 sieving by charge, R&T Fig.21-19 immunogenicity — 모두 해당 카드 본문에 1–2문장 또는 표로 압축 흡수.

마커 검증: <!-- MASTER LENS --> ×6 (§1+5 카드), <!-- ANCHOR --> ×5, <!-- CONFUSION --> ×4, <!-- SELF-TEST --> ×1, <!-- RECAP --> ×5. FIGURE 마커 0개 (Phase 4C 이연 — 지침 준수).

"계속"을 입력하면 Step 2 HTML 컴파일러가 실행됩니다.
Step 2는 위 내용 전체(§1·§2·§5·§7·§8) +
§3(구조적 동형성 지도: TMDD ↔ predator-prey ↔ Lotka-Volterra ↔ enzyme kinetics ↔ pH-buffered protonation) +
§4(인터랙티브 시뮬레이터: 8-parameter Full TMDD vs MM 비교 + Assumption Collapse 토글) +
§6(실용 시나리오 & 진단 병리: NDA narrative 작성 + Phantom Linearity GOF detection)를
단일 완성 HTML 파일(V5.1 Apex Edition + 4 graph bug fixes)로 통합합니다.

---

C-260502-064832-K7M

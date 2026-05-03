# Step 1 Draft v0 — Session 11
## Indirect Response / Turnover / DRT / Baseline / Effect Compartment / Rate-Limiting / Duration
### **STAGE 1 + STAGE 2 통합 완료본 — Gabrielsson 5e + Rowland & Tozer 5e 혼합 소스**

> ⚑ 이 파일은 통합 워크플로우 v3.3.2 Phase 1의 **최종 통합 산출물**이다.
> Stage 1 (Gabrielsson 5e Ch.2 §2.6.7 + Ch.3 §3.7/§3.8/§3.10/§3.12 + PD4-PD9) 기반 위에
> Stage 2 (Rowland & Tozer 5e Ch.8 Response, p.233-264) 가 통합되었다.
> Stage 1 산출물에 존재하던 모든 `[STAGE 2 통합 예정 ▶ ...]` 마커는 본 통합본에서 실제 R&T 내용으로 교체되었다.
> Phase 2 (Source Fidelity Audit) 진입 준비 완료.

**Detected source (Stage 1 + Stage 2 혼합)**:
- **Vol I — Gabrielsson & Weiner** *Pharmacokinetic and Pharmacodynamic Data Analysis*, 5e (Swedish Pharmaceutical Press)
- **Vol I — Rowland & Tozer** *Clinical Pharmacokinetics and Pharmacodynamics*, 5e (R&T)

소스 역할 분담:
- **Gabrielsson** = 수식 도출, 4-Model Taxonomy, ODE 구조, PD case study(PD4-PD9)의 NONMEM 추정 디테일, Identifiability crisis(PD4 Pool 1)
- **R&T** = 임상 시간 거동의 *왜 그런가* 메커니즘 서사, hysteresis 분류, PK rate-limited vs PD rate-limited 판별, $t_D$ formula의 임상 용량 결정 도구, target consumption 메커니즘(aspirin/omeprazole)

**Coverage (Stage 1 + Stage 2 통합)**:
- Gabrielsson Ch.2 §2.6.7 (pp.110–111) + Ch.3 §3.7 (pp.235–255) + §3.8 (pp.256–260) + §3.10 (pp.272–275) + §3.12 (pp.317–319) + Case Studies PD4 / PD5 / PD6 / PD7 / PD9 (pp.742–784)
- R&T Ch.8 Response (pp.233–264) — Time delays, Hysteresis, Effect compartment, Indirect response models, Systems in flux, PK vs PD rate-limited decline, Onset/duration of effect, Transporter polymorphism

**Scope 외 표기**:
- Gabrielsson §3.8.3 MIC 본문(Eq 3:122 이후 절단), §3.10.3 Locomotor activity(p.275 후반 절단), §3.12.1 Table 3.15 이후(p.319 후반 절단) — 모두 "제공 범위 외"로 처리
- R&T p.233-264 전 범위 가시 — 제공 범위 외 항목 없음

**Data Anchoring 소스 (Stage 1 + Stage 2 통합 — Dynamic Source Anchoring Directive 적용)**:

*Gabrielsson 측*:
- **PD4** (s)-warfarin iv bolus: $C = 1.05 \cdot e^{-0.0228 \cdot t}$, R0=121 sec, IC50=0.24 mg·L⁻¹, n=1.6, tlag=6.6 h (lag-time model 최종)
- **PD5** iv infusion (compound A): V=40 L, K=0.9 h⁻¹; 3개 dose 4,000 / 16,000 / 80,000 units over 6 h; 최종 kin=19, kout=0.43 h⁻¹, IC50=95, Imax=0.65
- **PD6** iv bolus (compound B): V=5.205 L, K=0.456 h⁻¹; 3개 dose 10.75 / 43.0 / 172 mg; 최종 kin=234, kout=ke0=5.6 h⁻¹ (≈7 min), EC50=1633 ng·L⁻¹
- **PD7** iv infusion (compound C): V=28.6 L, K=2.8 h⁻¹; 3개 dose 6,400 / 32,000 / 160,000 units over 4 h; 최종 kin=27, kout=0.92 h⁻¹, SC50=50, Smax=4.5
- **PD9 Zooparc®** (anxiolytic, fictional but parameter-anchored): Ka=1.1 h⁻¹, K=0.128 h⁻¹, V/F=5.0 L·kg⁻¹; 4 oral doses of 5 mg or 25 mg q24h; 최종 kin=8.8, kout=0.11 h⁻¹, IC50=0.25 µg·L⁻¹, n=1.40
- **항생제 cell-kill** (PD16/PD26 referent): 5개 dose group, 1st-order growth kg + 2nd-order kill kk·C·N, $B_{max}$ ≈ 30,000 CFU
- **Negative feedback 임상 anchor**: 인간 IgG, 반감기 11 days at 30 mg·mL⁻¹ serum level (saturable protection system)

*R&T 측 (신규 통합)*:
- **Digoxin** 1 mg i.v. bolus (Fig 8-1): 6명 normal subjects, distribution equilibrium ~6 hr, Pre-equilibrium phase (0-4h)에서 plasma↓하면서 effect↑ 의 absurd 관계 — *distribution-driven hysteresis*의 표준 임상 사례
- **Naproxen** 500 mg oral (Fig 8-2, 8-14): dental pain model, 1-8 hr sampling, *counterclockwise hysteresis* loop, Effect compartment fitting으로 hysteresis 제거 가능
- **Midazolam** 15 mg/kg oral (rat, Fig 8-6): 11.5-30 Hz EEG amplitudes vs plasma concentration, *direct PK-PD link* 표준 사례, Cmax와 Effect peak 동시 발생
- **Dexamphetamine** 1.78 / 3.12 / 5.62 µmol/kg i.p. & i.m. (Fig 8-7): locomotor activity, *response = E(0) - m·k·t* 의 zero-order 선형 감소 (Eq 8-3) 직접 시연
- **Ranitidine** 50 mg i.v. (Fig 8-8): 9명 renal impairment subjects (CrCl 51-80 mL/min), gastric pH, *indirect link* 표준 사례
- **Ibuprofen** 6 mg/kg oral (Fig 8-9): 36명 febrile children (6 mo - 11 yr), rectal temperature, *system flux* (heat balance) 기반 hysteresis
- **Warfarin** 1.5 mg/kg oral (Fig 8-10, 8-15, 8-16): prothrombin complex activity, blocking dose 방법으로 $k_t$ 추출, heptabarbital 상호작용 사례
- **Acenocoumarol** 10 mg oral racemate vs **Phenprocoumon** 0.6 mg/kg (42 mg/70 kg) oral racemate (Fig 8-11): 같은 메커니즘, 다른 PK ($t_{1/2}$ 15h vs 5 days) — **PK vs PD rate-limited의 결정적 대조**
- **Succinylcholine** 0.5 / 1.0 / 2.0 / 4.0 mg/kg i.v. (Fig 8-18, 8-24): muscle paralysis, **22%/min** 선형 감소, $t_{1/2}^{eff}$ ≈ 4 min, **dose-doubling → +1 half-life duration** 직접 검증
- **Minoxidil** 25 mg oral (Fig 8-19): MAP baseline 157 mmHg 환자, blood pressure-lowering effect 선형 감소, *PK rate-limited* 만성 약물 사례
- **Aspirin** 650 mg oral (Fig 8-20): plasma $t_{1/2}$ 15 min, but thromboxane B₂ 억제 효과 days 지속 — **target consumption 기반 PD rate-limiting**의 표준 사례
- **Omeprazole** 40 mg oral (Fig 8-21): plasma $t_{1/2}$ < 1 hr, but acid output 억제 효과 days 지속 — covalent binding + slow dissociation 복합 메커니즘
- **Paclitaxel** i.v. (Fig 8-22): leukocyte 회복까지 3 weeks, anticancer drug의 indirect response 임상 사례
- **Methylprednisolone** 16 / 31 / 63 / 125 / 250 / 500 / 1000 mg i.v. (as phosphate prodrug, Fig 8-25, 8-26, 8-27): linear PK (AUC ∝ Dose) but nonlinear PD (lymphocyte 반응 비례 안 함, 500-1000 mg에서 거의 동일 반응) — **dose linearity in PK ≠ dose linearity in PD**
- **Rosuvastatin** OATP1B1 polymorphism (Fig 8-28, 8-29): TT vs TC vs CC genotypes, plasma AUC 63%/111% 증가하나 cholesterol synthesis (MVA AUC) 반응은 3.1%/5.8% 감소만 — *exposure-response disconnect* (CONTEXT 처리, 본문 1-2문장 통합)

> ⚠️ **PDF 파싱 주의 (확인 완료)**: 모든 핵심 ODE는 LaTeX로 복원했으며 추출 실패는 없음.
> 단 §3.8 K 표기가 *bacterial kill 2차 상수*와 *PK elimination 1차 상수* 모두에 사용됨 — Scope Lock HARD RULE에 따라 본문에서 [확인 필요] 태그 부착 (Card 6).
> R&T Ch.8에서도 $k$ 표기가 elimination rate constant (Eq 8-10, 8-12) 와 $k_t$ degradation rate constant (Eq 8-6, 8-7) 두 가지로 사용되나 R&T는 명시적으로 분리 표기하므로 충돌 없음.

---

## Curation Map (Stage 1 + Stage 2 통합 갱신본)

이 세션의 Telos는 **농도 → 반응 사이의 시간 지연을 어떻게 모델링하며, 그 모델 선택을 NDA/IND 문서 수준에서 어떻게 방어하는가** 이다. R&T 통합 후 이 Telos는 두 차원으로 확장된다: (1) **무엇이 시간 거동을 rate-limit 하는가** (PK clock vs PD clock), (2) **그 rate-limiting의 임상적 귀결을 어떻게 dose-duration 관계로 환산하는가** ($t_D$ formula). 통합 워크플로우 v3.3.2의 "Master's Lens First" 원칙에 따라, §2 작성 전 MUST/CONTEXT 분류를 확정한다.

### MUST (체화 필수, §2 카드 발급) — 7 → 9개로 확장

| # | 개념 | 소스 | Why MUST? (test: 다음 개념을 이것 없이 따라갈 수 있는가?) |
|---|------|------|------|
| 1 | **Turnover Model Foundation** ($\frac{dR}{dt} = k_{in} - k_{out} \cdot R$, $R_0 = k_{in}/k_{out}$) + **Hysteresis 분류** (clockwise vs counterclockwise; distribution-driven vs system-flux-driven) | G + R&T | 이 ODE 없이는 4모델 분류, 초기치 추정, 어떤 PD 사례 분석도 구조적으로 불가능. R&T의 hysteresis 분류 없이는 임상 데이터의 시간 지연이 distribution 문제인지 system flux 문제인지 진단 불가. PD4 Pool 1의 식별성 위기는 이 ODE의 reparameterization 없이 해결되지 않는다. |
| 2 | **Four-Model Taxonomy** (Models 1–4: inhibit/stimulate × $k_{in}$/$k_{out}$) + R&T의 *four cases* IRM 분류 | G (R&T 보강) | Scope Lock 비협상 요구사항 ("All four Models must appear side-by-side"). 약물 작용 부위 식별의 1차 필터. R&T가 같은 4-form 분류를 *더 높은 수준의 임상 framing*으로 제시. |
| 3 | **tss-Based Mechanism Discrimination** (Models 1&3 → dose-independent tss; Models 2&4 → dose-dependent tss) | G | 데이터에서 약물 작용 부위($k_{in}$ vs $k_{out}$)를 식별하는 단 하나의 시각 시그니처. 잘못 읽으면 PD5(Model 2) vs PD6(Model 3) 구분 실패. **Card 8 (rate-limiting)** 과 결합하여 해석. |
| 4 | **Imax/Emax Multiplier Semantics** (Fig 3.40의 세 가지 의미) + R&T의 *dose linearity in PK ≠ dose linearity in PD* (methylprednisolone 사례) | G + R&T | $E_{max}$가 *absolute distance*인 직접 모델과 *baseline multiplier*인 간접 모델은 의미가 근본적으로 다르다. R&T methylprednisolone 사례가 PK 선형성을 PD 선형성으로 잘못 외삽하는 임상적 위험을 직접 시연. |
| 5 | **Graphical Initial Parameter Estimation** (Table 3.6 + Eq 3:104의 모델별 4규칙) + R&T의 *blocking dose 방법으로 $k_t$ 추출* (warfarin 사례) | G + R&T | 모든 PD 사례의 첫 단계. graphical 단계 없이 NONMEM에 진입하면 시작값이 비현실적이 되어 수렴 실패. R&T의 blocking dose 방법은 graphical 추정의 임상적 강건성을 보강. |
| 6 | **Irreversible (Second-Order) Drug Action** ($-K \cdot C \cdot R$) + R&T의 *target consumption* 메커니즘 (aspirin, omeprazole) | G + R&T | Reversible과 구조가 다름 (drug=0에서 loss=0). R&T는 항생제·항암제 외에도 *target receptor 자체의 비가역 소진* 형태로 일반화. **K 표기 충돌 [확인 필요]**. |
| 7 | **Turnover vs Effect Compartment Discrimination Crisis** ⚡ **Apex Concept** + R&T의 *biophase distribution* mechanistic interpretation of $k_{e0}$ | G + R&T | PD6의 발견 — 선형 $S(C)$ + 단일 dose-range 데이터에서 두 모델이 거의 동일한 WRSS. NDA Deficiency Letter의 가장 흔한 PK/PD 사유. R&T의 effect compartment를 *분포 평형 메커니즘* 으로 해석하는 framing이 모델 선택 정당화의 분자 근거 제공. |
| **8** | **PK vs PD Rate-Limited Decline of Response** ★ 신규 (R&T 핵심 기여) | R&T (G 보강) | R&T Ch.8의 가장 중요한 구조적 통찰. *두 시계가 동시에 똑딱이지만 느린 시계가 항상 박자를 결정한다.* Acenocoumarol vs Phenprocoumon, Aspirin vs Propranolol 의 대조가 임상 용량·간격 결정의 근간. Card 9의 $t_D$ formula 적용 가능 여부를 결정하는 전제 조건. |
| **9** | **Duration of Effect & Dose-Log Linearity** ($t_D = \frac{1}{k}\ln\!\big(\frac{Dose}{C_{min}\cdot V}\big)$, Eq 8-12) ★ 신규 (R&T 핵심 기여) | R&T | 한 줄의 수식이 임상 용량 결정의 핵심 도구. *Doubling dose → +1 half-life duration* 의 구조적 귀결. Succinylcholine, local anesthetics, minoxidil의 dosing 실무에 직접 적용. PK rate-limited 약물에만 적용 가능 — Card 8 전제. |

### CONTEXT (이해 보완, MUST 카드 본문에 1–2문장 통합)

- **Negative feedback / moderator model** (G §2.6.7 Eq 2:261–2:263, IgG 11-day half-life saturable protection) → Card 1 본문에 "system parameter로서의 baseline 변동" 1문장으로 통합.
- **Capacity-limited turnover extensions** (G Eq 3:107–3:109, $V_{max}/K_m$ on response loss) → Card 2 본문에 "extension family" 1문장.
- **Cell growth + kill** (G Eq 3:117–3:121, Fig 3.49–3.50) → Card 6에 항균요법 응용 사례로 통합.
- **Dose-Response-Time framework** (G §3.10 Fig 3.60: baseline=$f(k_{in},k_{out})$, slope=$f(k_{out})$, slope=$f(ID_{50},I_{max},A)$) → Card 5에 "농도 측정 없을 때의 역추출" 1문장.
- **Baseline drift / disease progression** (G §3.12 Eq 3:248–3:250, self-regulating with physiological limit) → Card 1에 "baseline의 시간 가변성" 1문장.
- **Synergy / multi-compartment response model** (G Table 3.7 후반) → §8 Positioning에서만 후속 챕터로 언급.
- **Peak shift analytical theory** (Peletier et al [2005]) → Card 7에 PD9 Fig 9.5 시뮬레이션 결과로 통합.
- **Direct PK-PD link** (R&T p.239 midazolam, Fig 8-6) → Card 1에 hysteresis의 *대척점* (no hysteresis = direct link) 으로 1문장 통합.
- **Indirect link** (R&T p.239 ranitidine, Fig 8-8) → Card 7 본문에 effect compartment vs turnover 두 가지 모두 indirect link임을 명시하는 1문장.
- **Region 1/2/3 of E-vs-logC curve** (R&T Fig 8-17, p.249) → Card 9에 $t_D$ formula의 적용 영역(Region 2)을 명시하는 1-2문장 통합.
- **Dose linearity in PK ≠ dose linearity in PD** (R&T Fig 8-25,26,27 methylprednisolone 16-1000 mg) → Card 4에 *in vivo* 외삽 위험의 임상 사례로 1-2문장 통합.
- **Transporter polymorphism (rosuvastatin OATP1B1)** (R&T p.256-259, Fig 8-28,29) → **CONTEXT 처리 결정** (Scope Lock 주의사항 4번 반영). Card 7 또는 §8에 "시스템 노출-반응 disconnect의 임상 사례"로 1-2문장 통합. R&T 챕터의 보조 주제이며 본 세션 핵심 골격(turnover/IRM/tD)에 구조적으로 종속되지 않음.

---

## §1 — Session Header & Roadmap (Stage 1 + Stage 2 통합본)

**소스 (혼합)**:
- Gabrielsson & Weiner 5e (Ch.2 §2.6.7 + Ch.3 §3.7 / §3.8 / §3.10 / §3.12 + Case Studies PD4 / PD5 / PD6 / PD7 / PD9)
- Rowland & Tozer 5e (Ch.8 — Response)

**페이지**: G pp.110–111, 235–260, 272–275, 317–319, 742–784 + R&T pp.233–264

### Big Idea — 한 문장 (Stage 2 통합 후 재작성)

**모든 측정 가능한 약리반응은 시간 지연을 가지며, 그 지연을 결정하는 두 시계 — *PK clock* (약물 농도가 변하는 속도)과 *PD clock* (반응 시스템이 변하는 속도) — 중 느린 쪽이 항상 임상 거동을 지배한다. 그리고 그 지연의 *수학적 형태*는 약물의 작용 부위(생산 vs 소실, 가역 vs 불가역, 분포-한정 vs 시스템-한정)를 데이터로부터 직접 식별하게 한다.**

임상 관찰 — "농도-반응이 즉각적이지 않다", "Cmax와 효과 peak가 일치하지 않는다", "반복 투여 시 효과 회복이 농도 회복보다 느리다" — 은 **turnover model의 4가지 표준 구조**, **effect compartment의 biophase distribution**, **target consumption의 비가역 소진**, **PK/PD rate-limiting의 명시적 판별** 의 네 도구로 곧바로 *작용기전 가설*과 *임상 dose-duration 결정 규칙*으로 변환된다. 한 줄의 $t_D$ 수식이 succinylcholine 마취 회복 시간의 dose 의존성을 예측하는 동시에, 그 수식이 warfarin·aspirin·omeprazole에 대해서는 적용 *불가* 임을 알려준다.

### 개념 항법도 (Stage 2 통합 후 확장)

```
[G §2.6.7]   Feedback (inherent / positive / negative)
                │
                ↓  (turnover의 "loss 항이 R에 의존"이라는 일반 형태)
[G §3.7]     Reversible Turnover  ←—————— SESSION CORE
[R&T p.245]      ├─ Card 1: Foundation (kin, kout, R0) + Hysteresis 분류 (R&T)
                 ├─ Card 2: Four-Model Taxonomy (1–4)
                 ├─ Card 3: tss Discrimination       ←  [⚡ 작용 부위 식별]
                 ├─ Card 4: Imax/Emax Semantics + dose linearity 함정 (R&T)
                 ├─ Card 5: Initial Parameter Estimation + blocking dose (R&T)
                │
                ↓  (drug=0에서 loss=0이 되는 구조 변화)
[G §3.8]     Irreversible Action  →  Card 6 (항생제 kill 모델 + target consumption R&T)
[R&T p.251]
                │
                ↓  (농도가 없을 때, 반응만으로 biophase 추출)
[G §3.10]    Dose-Response-Time framework  →  Card 5에 통합
                │
                ↓  (baseline이 상수가 아닌 경우)
[G §3.12]    Baseline Models (constant / oscillating / drifting)  →  Card 1에 통합
                │
                ↓  (모델 선택의 메타 결정)
[PD6]        Turnover vs Effect Compartment Crisis  →  Card 7 (⚡ Apex)
[R&T p.245]                                                  + biophase ke0 mechanistic story
                │
                ↓  ★ R&T 핵심 기여 (Stage 2 신규)
[R&T p.243-244]  Card 8: PK vs PD Rate-Limited Decline
                  ├─ Acenocoumarol vs Phenprocoumon (Fig 8-11) — 같은 메커니즘, 다른 rate-limiter
                  ├─ Aspirin / Omeprazole — target consumption 기반 PD-limited
                  └─ Succinylcholine / Minoxidil — PK-limited 표준 사례
                │
                ↓  ★ R&T 핵심 기여 (Stage 2 신규)
[R&T p.254-256]  Card 9: Duration of Effect & Dose-Log Linearity
                  ├─ $t_D = \frac{1}{k}\ln\!\big(\frac{Dose}{C_{min}\cdot V}\big)$  (Eq 8-12)
                  ├─ Region 1/2/3 of E-vs-logC (Fig 8-17)
                  ├─ "Doubling dose → +1 half-life" 구조적 귀결
                  └─ PK rate-limited 약물에만 적용 (Card 8 전제)
```

### 지식 그래프 위치 (Stage 2 통합 후 확장)

- **선행 (전제)**:
  - 1구획 PK ($\frac{dC}{dt} = -K \cdot C$, IV bolus / infusion / oral kinetics)
  - 직접 Emax / Imax 모델 ($E = E_0 + \frac{E_{max} \cdot C^n}{EC_{50}^n + C^n}$)
  - 1차 ODE의 정상상태(steady state) 추론
  - AUC 계산
  - Hill equation 의 Region 1/2/3 거동 (R&T Fig 8-17 — Card 9에서 본격 활용)

- **후속 (이 세션이 열어주는 영역)**:
  - **R&T Ch.10 Constant-Rate Input**: 반복/지속 투여 시 effect-time profile 의 수렴 거동 ($t_D$ 와 dosing interval 의 관계)
  - **R&T Ch.11 Multiple-Dose Regimens**: PK vs PD rate-limited의 multiple-dose accumulation 차이 (PK accumulation은 빠르지만 PD accumulation이 늦는 경우 — warfarin)
  - **R&T Ch.16 Nonlinearities**: capacity-limited PK + saturable PD 의 결합 거동 (Card 2 capacity-limited extension의 PK 측 보완)
  - **R&T Ch.20 Metabolites and Drug Response**: active metabolite가 추가될 때 IRM 4-form 분류의 식별 가능성 변화
  - **R&T Ch.21 Protein Drugs**: TMDD (Session I-08) 와의 직접 연결 — turnover-on-receptor 형태
  - Transit compartment models (delay 모델의 일반화) — Session 12+
  - Moderator / tolerance models (G §3.9, negative feedback의 동적 확장) — Session 13+
  - Disease progression baseline drift models — Sessions later
  - PopPK/PD with IIV on $k_{out}$ and $IC_{50}$ (η-shrinkage 진단)
  - TMDD (target-mediated drug disposition) — Session I-08의 turnover-on-receptor 형태

> 이 세션은 **PK 모델링 단독에서 PK/PD 시간축 통합으로 넘어가는 최초의 경계** 다. R&T 통합 후 이 경계는 단순한 "시간 지연 인식"을 넘어 *PK clock vs PD clock 의 명시적 판별 → 그에 따른 임상 dosing 도구 ($t_D$ formula) 선택 또는 거부* 로 구체화된다. 여기를 대충 넘기면 PopPK/PD 전체 과정에서 작용기전 추론이 데이터에서 떠나 가설로만 남게 되고, 임상 dose-duration 결정이 시행착오로 전락한다.

<!-- RECAP -->
**§1 종결 흐름 요약**: G §2.6.7의 negative feedback이 turnover의 일반 형태(loss 항이 R에 의존)를 도입했고, §3.7이 이를 4모델로 표준화한다. §3.8은 "drug=0에서 loss가 0이 되는" 구조 변환으로 항생제·항암제 영역을 연다. §3.10은 농도 측정 부재 시 반응-시간 단독으로부터 biophase kinetics를 역추출하는 가능성을, §3.12는 baseline의 시간 가변성을 추가한다. PD6는 모델 선택의 위기에서 끝난다. R&T Ch.8은 이 구조 위에 *시간 거동을 무엇이 결정하는가* (PK clock vs PD clock) 라는 메타 차원을 얹고, $t_D$ formula로 임상 용량 결정의 정량 도구를 제공한다. 두 시계의 명시적 판별이 turnover model 선택의 임상 정당성을 보강하고, $t_D$ formula의 적용 범위가 모델 가정의 임상적 함의를 노출한다.

---

## §2 — Concept Anatomy Cards (Stage 1 + Stage 2 통합본)

총 9개 MUST 카드. Cards 1, 3, 5, 7은 R&T 내용으로 확장. Cards 8, 9는 R&T 기반 신규.

---

### ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### Card 1 — Turnover Model Foundation + Hysteresis Classification
### ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<!-- MASTER LENS -->
#### [개념 Big Idea: 거장의 시각]

하나의 ODE — $\frac{dR}{dt} = k_{in} - k_{out} \cdot R$ — 가 PK/PD 시간축 모델링 전체의 골격을 결정한다. 이 식을 "정상상태에서 평형 잡힌 양수기"로 보면 baseline은 단순한 비율($k_{in}/k_{out}$)에 불과하지만, **"시간 상수가 분리된 두 채널"** 로 보는 순간, baseline은 *약물이 건드릴 수 있는 두 개의 잠금 손잡이*로 변한다. 어느 손잡이를 비트느냐가 작용기전 가설이고, 그 결과가 4-Model Taxonomy다.

R&T가 이 식 위에 추가하는 결정적 framing은 **hysteresis 분류** 다. 동일한 ODE가 만들어내는 *concentration-effect plane에서의 시계 방향* 이 임상에서 두 가지 다른 메커니즘을 가른다 — *counterclockwise* (반응이 농도를 따라잡지 못함, naproxen / ranitidine / warfarin)는 표준 시간 지연; *clockwise* (반응이 농도보다 *먼저* 떨어짐)은 tolerance 또는 active metabolite 신호. 임상 PK/PD 보고서에서 이 시계 방향 한 가지 판독이 모델 family 선택의 첫 결정이다.

PD4 warfarin 분석에서 Pool 1 모델의 $k_1$과 $k_{out}$ 이 상관계수 **0.9999** 로 묶여 추정 불가능했던 이유는 두 손잡이를 잘못된 방향에서 비틀려 했기 때문이다. **R0와 $k_{out}$ 으로 reparameterize** 하는 단 한 줄의 변환(G Eq 3:103)이 NONMEM 수렴을 살리고 CV%를 사용 가능한 수준으로 회복시킨다. R&T의 임상 시연 — warfarin **1.5 mg/kg oral** blocking dose가 prothrombin complex synthesis를 거의 완전 차단하면서 첫 48시간의 단순 지수 감쇠로부터 $k_t$ ≈ 0.06 day⁻¹ (clotting factor 반감기 약 11.5시간) 를 직접 추출하는 절차 — 가 이 reparameterization의 임상 등가물이다.

이 직관 — *baseline은 비율이 아니라 채널 손잡이의 균형, hysteresis 시계 방향이 메커니즘 가설의 첫 분기점, blocking dose가 system parameter 추출의 임상 도구* — 을 머릿속에 박고 아래 수식과 코드를 읽으라.

#### A. Formal Definition

**Turnover model**: 반응 변수 R의 시간 변화율이 zero-order 생산($k_{in}$)과 first-order 소실($k_{out} \cdot R$)의 차이로 표현되는 1차 ODE 시스템.

$$\frac{dR}{dt} = k_{in} - k_{out} \cdot R \quad \text{[G Eq 3:74]}$$

여기서:
- $R$ = pharmacological response (mediator, transmitter, functional response — heart rate, blood pressure, PCA, IgG, prothrombin complex activity, gastric pH, body temperature, leukocyte count, etc.)
- $k_{in}$ = zero-order production rate constant (units: response·time⁻¹)
- $k_{out}$ = first-order loss rate constant (units: time⁻¹) — R&T notation에서는 $k_t$ (degradation rate constant)
- $R_0$ = baseline response (assumed time-invariant in basic form)

**Hysteresis** (R&T p.234-235 통합): concentration-effect plane에서 plotted 점들이 시간 순서로 *닫힌 loop* 를 그리는 현상. 동일한 농도에서 *상승 phase* 와 *하강 phase* 의 반응 값이 다름. 두 종류:

- **Counterclockwise hysteresis**: 농도 상승기에 반응이 lag, 농도 하강기에도 반응이 lag → loop가 시계반대방향. 표준 시간 지연 (distribution, system flux, target consumption 등). R&T 표준 사례: naproxen 500 mg oral (Fig 8-2B, sampling 1-8 hr).
- **Clockwise hysteresis**: 농도 상승기에 반응이 먼저 발생, 하강기에 반응이 *먼저* 떨어짐 → loop가 시계방향. Tolerance 발생 또는 active metabolite 기여 신호 (이 세션 범위 외, Session 13+ tolerance에서 다룸).

#### B. Derivation / Code Structure

**정상상태 (no drug)**: $\frac{dR}{dt} = 0$ → $k_{in} = k_{out} \cdot R_0$

$$R_0 = \frac{k_{in}}{k_{out}} \quad \text{[G Eq 3:76]} \quad \text{[출처: Gabrielsson 5e, Ch.3, p.237]}$$

**Reparameterization with $R_0$ and $k_{out}$** (PD4 PD7에서 식별성 확보의 핵심):

$$\frac{dR}{dt} = k_{out} \cdot R_0 - k_{out} \cdot R = k_{out} \cdot (R_0 - R) \quad \text{[G Eq 3:103]} \quad \text{[출처: Gabrielsson 5e, Ch.3, p.247]}$$

이 형태는 $R_0$ 와 $k_{out}$ 이 모두 데이터에서 직접 추정 가능. **R&T의 임상 등가 절차** (warfarin blocking dose, p.246-247): synthesis가 완전 차단되는 충분히 큰 dose에서는 $R_{syn} = 0$ 이 되어 ODE가 단순 지수 감쇠로 환원:

$$\frac{dA}{dt} = -k_t \cdot A \quad \text{(under blocking dose)} \quad \text{[R&T Eq 8-6 with } R_{syn}=0\text{]}$$

따라서 ln(A) vs t plot의 직선 slope = $-k_t$ 가 직접 추출됨 (R&T Fig 8-15A: 1.5 mg/kg sodium warfarin, 첫 48 hr 동안 prothrombin complex activity의 단순 지수 감쇠). R&T Fig 8-15B는 동일 절차를 0.75 / 1.5 / 3.0 mg/kg 3개 dose에서 시행하여 36 hr 시점의 잔존 활성이 모두 약 22-24% 로 동일함을 보여 — *blocking dose 이상에서는 $k_t$ 단독이 감쇠 결정* — synthesis 차단 가정을 검증한다.

**일반 비-blocking dose에서의 synthesis rate 역추출** (R&T Eq 8-7):

$$R_{syn} = \frac{A_2 - A_1}{\Delta t} + k_t \cdot \frac{A_1 + A_2}{2}$$

이 식으로 임의 시점의 synthesis rate를 추정한 후, percent inhibition (Eq 8-8):

$$\text{Percent inhibition} = 100 \cdot \frac{R_{syn(n)} - R_{syn}}{R_{syn(n)}}$$

를 plasma warfarin 농도의 logarithm에 대해 plot하면 *hysteresis 없는 graded response* 곡선이 직접 노출됨 (R&T Fig 8-16). 이것이 effect compartment fitting과 별개로, *system flux model의 직접 inversion* 으로 hysteresis를 제거하는 R&T의 절차 — Card 7의 Apex Concept과 비교할 가치 있는 대안.

**NONMEM 의사 코드 (개념적 매핑)**:

```
$THETA
(0, 121)        ; THETA(1) = R0  (baseline)  → 직접 추정 가능
(0, 0.06)       ; THETA(2) = KOUT (loss rate) → 직접 추정 가능
; KIN = R0 * KOUT 으로 derived → 별도 추정 불요

$DES
DADT(1) = THETA(2)*THETA(1)*HC - THETA(2)*A(1)
                ; KOUT*R0*H(C) - KOUT*R   ←  G Eq 3:103 직접 구현
```

**Baseline의 시간 가변성 (CONTEXT 통합)**: G §3.12 Eq 3:248의 self-regulating 형태 $\frac{dR}{dt} = k \cdot R \cdot (R_{ss} - R)$ 는 baseline이 질병 진행이나 외부 timekeeper(light/dark cycle)에 의해 움직이는 경우.

**Negative feedback / moderator (CONTEXT 통합)**: G §2.6.7 Eq 2:261–2:263의 hormone-glucose model에서 moderator $M$이 추가되면 *high R → high M → high loss → R 감소* 라는 self-correction loop. IgG 임상 anchor: 30 mg·mL⁻¹ serum level에서 11일 반감기.

**Direct PK-PD link (R&T CONTEXT 통합)**: hysteresis의 *대척점* — concentration-effect plane에서 점들이 single curve를 따르고 loop 없음. 즉 시간 지연 zero. R&T 표준 사례: midazolam 15 mg/kg oral (rat, Fig 8-6), 11.5-30 Hz EEG amplitudes가 plasma midazolam과 동시에 peak. 이 경우 PK-PD modeling은 직접 Emax 모델로 충분 — Card 7의 Apex Concept은 발생하지 않음.

> 📎 [Micro-citation] $R_0 = k_{in}/k_{out}$ [출처: Gabrielsson 5e, Ch.3, p.237]
> 📎 [Micro-citation] G Eq 3:103 reparameterization [출처: Gabrielsson 5e, Ch.3, p.247]
> 📎 [Micro-citation] R&T Eq 8-6 system flux ODE [출처: Rowland & Tozer 5e, Ch.8, p.246]
> 📎 [Micro-citation] R&T Eq 8-7 synthesis rate inversion [출처: Rowland & Tozer 5e, Ch.8, p.247]

#### C. Structural Necessity

**왜 정확히 이 형태인가?**

1. **zero-order 생산**: 내인성 mediator의 합성은 효소·전구체 풀이 충분할 때 0차로 근사된다. $R$ 자기 자신은 합성 속도를 *직접* 결정하지 않으며, 이것이 자가조절 시스템과의 첫 분기점이다.
2. **first-order 소실**: 분해·청소·신장 배설은 대부분 R에 비례한다. 이는 PK clearance의 first-order assumption의 PD 대응판.
3. **선형성 요구**: G Eq 3:74가 선형이기 때문에 정상상태가 단일하게 결정. 비선형으로 가면 다중 정상상태와 oscillation이 가능해진다.

**Hysteresis 시계 방향의 수학적 필연성** (R&T 통합): R&T Eq 8-5의 일반 framing $\frac{dA}{dt} = R_{in} - R_{out}$ 에서 약물이 $R_{in}$ 또는 $R_{out}$ 중 하나를 시간에 따라 변화시키면, $A$ 의 시간 거동은 약물 농도-시간 곡선보다 *항상 lag* 한다 (1차 ODE의 transfer function이 lowpass filter). 따라서 single agent without tolerance의 경우 *counterclockwise* loop가 수학적 필연. *Clockwise* loop는 (a) tolerance (자가조절 loop이 작동하여 받는 자극에 적응), 또는 (b) active metabolite (parent 농도가 떨어지는 동안에도 metabolite가 효과 유지하다 더 빠르게 사라짐) 의 *추가 동역학* 이 있어야 발생.

**다른 형태는 왜 안 되는가?**

- 두 항 모두 R에 비례 ($\frac{dR}{dt} = k_{in} \cdot R - k_{out} \cdot R$): 지수 발산/소멸, baseline 정의 불가능.
- 두 항 모두 zero-order ($\frac{dR}{dt} = k_{in} - V_{max}$): G Eq 3:109 형태로 환원, R이 $K_m$ 보다 훨씬 클 때만 유효, baseline 부재.

#### D. Assumptions & Boundary Conditions

| 가정 | 의미 | 위반 시 |
|-----|------|--------|
| $k_{in}$, $k_{out}$ time-invariant | 약물 부재 시 baseline은 고정 | G §3.12의 baseline drift 모델로 확장 필요 |
| $R$ 단일 구획, instantaneous mixing | 반응의 공간 분포 무시 | multi-compartment response (G Table 3.7) |
| $R_0$ 측정 가능 | pre-dose baseline 관측 충분 | 반복 baseline 측정 또는 vehicle group 필요 |
| 약물 부재 시 first-order kinetics | $\ln R$ 의 slope = $-k_{out}$ | feedback 존재 시 slope는 $k_{out}(1+M/M_{50})$ |
| Hysteresis는 counterclockwise | single agent, no tolerance, no active metabolite | clockwise이면 tolerance/metabolite 모델 필요 |

#### E. Limitations

- 단일 mediator만 모델링; precursor-pool (PD4 Pool 모델) 필요한 경우 확장.
- Capacity-limited loss (G Eq 3:107)는 별도 처리 필요.
- Negative feedback의 자가조절은 moderator 보조 ODE 추가 (Eq 2:262) 필요.
- Hysteresis가 distribution-driven인지 system-flux-driven인지 ODE만으로는 구별 불가 — 시간 척도 비교 필요 (Card 8 PK vs PD rate-limiting과 결합 분석).

#### F. Five Cognitive Layers (Vol I 분기)

| Layer | 내용 |
|-------|------|
| **L1 형식적 수학** | $\frac{dR}{dt} = k_{in} - k_{out} R$, 정상상태 해 $R_0 = k_{in}/k_{out}$, 시간 상수 $\tau = 1/k_{out}$, $t_{1/2} = \ln 2 / k_{out}$. R&T blocking dose 절차로 $k_t$ 직접 추출 |
| **L2 기하학적 직관** | R-t 평면에서 baseline은 수평선; $k_{out}$ 차단 시 $\ln R$ 직선 강하; concentration-effect plane에서 *counterclockwise loop* 가 시간 지연의 시각 시그니처 |
| **L3 구조적 동일성** | Lake-faucet 모델, RC회로의 충방전, 약물 IV infusion → Css 곡선과 동일 ODE 구조; 1차 ODE의 lowpass filter 거동이 hysteresis 방향성의 수학적 토대 |
| **L4 생리학적 의미** | $k_{in}$ = 합성 효소 활성·전구체 공급률, $k_{out}$ = 분해·청소 속도; baseline = 두 손잡이의 균형점. 임상 anchor: prothrombin complex (warfarin), gastric pH (ranitidine), body temperature (ibuprofen), leukocyte count (paclitaxel) |
| **L5 실무 투영** | NONMEM `$DES`에서 reparameterized 형태로 코드, $R_0$ 를 `$THETA` 직접 추정, η on $k_{out}$, ε on R log-additive. R&T blocking dose 임상 절차로 NONMEM 시작값 얻기. concentration-effect plot의 hysteresis 시계 방향이 모델 선택의 1차 시각 진단 |

#### G. Zettelkasten Atom

```yaml
---
aliases: [Turnover model, Indirect response baseline ODE, IDR foundation, Hysteresis classification]
tags: [pharmacometrics/pkpd, turnover-model, foundation, parameterization, hysteresis]
up: "[[MOC-IndirectResponse]]"
related: ["[[Card2-FourModelTaxonomy]]", "[[Card7-DiscriminationCrisis]]", "[[Card8-RateLimiting]]", "[[NONMEM-Parameterization]]", "[[PD4-Warfarin-Identifiability]]", "[[RnT-WarfarinBlockingDose]]"]
source: "Gabrielsson & Weiner 5e, Ch.3 §3.7, p.237; Eq 3:74, 3:76, 3:103 + Rowland & Tozer 5e, Ch.8, p.234-235, 246-247; Eq 8-5, 8-6, 8-7"
---
```

Turnover model의 핵심 ODE $\frac{dR}{dt} = k_{in} - k_{out} R$ 은 baseline $R_0 = k_{in}/k_{out}$ 을 균형점으로 갖는다. NONMEM 추정 시 두 파라미터의 강한 상관(>0.98) 때문에 식별성이 무너지므로, $k_{in} = R_0 \cdot k_{out}$ 으로 reparameterize. R&T의 blocking dose 절차 (warfarin 1.5 mg/kg oral)는 이 reparameterization의 임상 등가 — synthesis 완전 차단 후 단순 지수 감쇠로부터 $k_t$ 직접 추출, 이후 임의 시점에서 synthesis rate를 inversion (Eq 8-7) 하여 hysteresis-free graded response 곡선 도출. Concentration-effect plane의 *counterclockwise loop* 가 시간 지연의 표준 시각 시그니처 (clockwise는 tolerance/metabolite 신호로 별도 모델 영역).


---

### ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### Card 2 — Four-Model Taxonomy (Models 1–4)
### ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<!-- MASTER LENS -->
#### [개념 Big Idea: 거장의 시각]

약물이 turnover system에 개입하는 방식은 정확히 네 가지뿐이다 — *생산을 막거나, 생산을 부추기거나, 소실을 막거나, 소실을 부추기거나.* 이 4 × 1 표는 단순한 분류표가 아니라 **임상 데이터를 작용기전 가설로 직접 사상하는 진단 격자(diagnostic grid)** 다. 임상시험 결과 그래프 한 장을 30초만 보면, 숙련된 모델러는 *어느 모델에 속하는지* 가 아니라 *어떤 셀이 가장 일관된지* 를 즉시 본다.

R&T가 같은 4-form 분류를 *임상 framing* 으로 다시 제시한다 (p.241): "The drug can increase or decrease the formation of the biomarker or increase or decrease its elimination." 동일 격자, 다른 어휘 — Gabrielsson의 *수학 우선* framing과 R&T의 *임상 의사결정 우선* framing이 한 표에서 만난다. 임상 모델러는 두 어휘를 자유롭게 번역할 수 있어야 NDA reviewer (R&T 어휘)와 NONMEM developer (Gabrielsson 어휘) 양쪽과 대화 가능.

이 진단 격자가 작동하지 않으면 신약 후보의 작용기전 가설이 데이터로부터 *떠난 채* 분자생물학 가설로만 남게 된다 — Phase 1 PoC 데이터의 가장 큰 정보 손실 지점.

이 직관 — *4 cells = 4 mechanisms, 절대 더 많지도 적지도 않다, 그리고 두 어휘가 같은 격자를 가리킨다* — 을 박고 진행하라.

#### A. Formal Definition

Reversible turnover models는 약물의 작용 형태(inhibition / stimulation)와 작용 부위(production / loss)의 2 × 2 조합으로 정확히 4가지 표준 구조를 갖는다.

#### B. Derivation / Code Structure — 4 Models Side-by-Side

**비협상 요구사항: 모든 4 모델이 한 표에 등장해야 함 (Scope Lock HARD RULE).**

| 항목 | Model 1<br>Inhibition of $k_{in}$ | Model 2<br>Inhibition of $k_{out}$ | Model 3<br>Stimulation of $k_{in}$ | Model 4<br>Stimulation of $k_{out}$ |
|------|---------|---------|---------|---------|
| **ODE** | $\frac{dR}{dt} = k_{in} \cdot I(C) - k_{out} R$ | $\frac{dR}{dt} = k_{in} - k_{out} R \cdot I(C)$ | $\frac{dR}{dt} = k_{in} \cdot S(C) - k_{out} R$ | $\frac{dR}{dt} = k_{in} - k_{out} R \cdot S(C)$ |
| **Drug action site** | 생산 억제 | 소실 억제 | 생산 자극 | 소실 자극 |
| **R&T 어휘 (p.241)** | decrease formation | decrease elimination | increase formation | increase elimination |
| **tss governor** | $k_{out}$ 단독 (dose-independent) | $k_{out} \cdot I(C)$ (dose-dependent) | $k_{out}$ 단독 (dose-independent) | $k_{out} \cdot S(C)$ (dose-dependent) |
| **$R_{ss}$ formula** | $R_0 \cdot I(C_{ss})$ | $\frac{R_0}{I(C_{ss})}$ | $R_0 \cdot S(C_{ss})$ | $\frac{R_0}{S(C_{ss})}$ |
| **$\Delta R$ formula (G Eq 3:83/89/95/101)** | $R_0 \cdot I_{max}$ | $R_0 \cdot \frac{I_{max}}{1-I_{max}}$ | $R_0 \cdot E_{max}$ | $R_0 \cdot \frac{E_{max}}{1+E_{max}}$ |
| **Limit of R (high $C_{ss}$)** | $R_{min} = 0$ | $R_{max} = \infty$ | $R_{max} = \infty$ | $R_{min} = 0$ |
| **Return-to-baseline** | $\leftrightarrow$ (변화 없음, $k_{out}$ 그대로) | $\downarrow$ (반감기 길어짐) | $\leftrightarrow$ | $\uparrow$ (반감기 짧아짐) |
| **Canonical example (G)** | warfarin → vitamin K reductase 억제 (PD4) | furosemide → 신세뇨관 물 재흡수 억제 | erythropoietin → RBC 생산 자극 (PD6) | CB1 inverse agonist → 에너지 소비 자극 (PD7) |
| **임상 anchor (R&T 추가)** | warfarin 1.5 mg/kg oral (Fig 8-10), prothrombin complex synthesis 억제 | ranitidine 50 mg i.v. (Fig 8-8), gastric H⁺ 분비 억제 — 청소가 아닌 분비이나 R&T framing에서 "decrease elimination of pH" | EPO analog 사례; paclitaxel은 leukocyte의 반대 — *production 억제* (anticancer toxicity) | (드물지만) thyroid hormone clearance 자극 약물 |

> 📎 [Micro-citation] Table 3.3 4-Model 분류 [출처: Gabrielsson 5e, Ch.3, p.238]
> 📎 [Micro-citation] $\Delta R$ 4 forms [출처: Gabrielsson 5e, Ch.3, Fig 3.42 / Table 3.6, p.249, 251]
> 📎 [Micro-citation] R&T 4 cases framing [출처: Rowland & Tozer 5e, Ch.8, p.241]

**$H(C)$ 함수 family (G Table 3.4 핵심 4종)**:

| 형태 | 수식 | 한계 | 용도 |
|------|------|------|------|
| Sigmoid stimulation (full) | $1 + \frac{E_{max} C^n}{EC_{50}^n + C^n}$ | $1 \le H \le 1 + E_{max}$ | Models 3, 4 표준 |
| Sigmoid inhibition (full/partial) | $1 - \frac{I_{max} C^n}{IC_{50}^n + C^n}$ | $0 \le H \le 1$ | Models 1, 2 표준 ($I_{max} \le 1$) |
| Linear stimulation | $1 + a \cdot C$ | $1 \le H \le \infty$ | PD6 작은 dose-range 한계 |
| Logarithmic | $1 + \ln(C^m + 1)$ | $1 \le H \le \infty$ | 광역 dose-range 압축 표현 |

**Capacity-limited extension (CONTEXT 통합)**: G Eq 3:107의 $\frac{dR}{dt} = k_{in} - \frac{V_{max}}{K_m + R} \cdot R$ 는 소실이 효소 용량 한계를 가진 경우. $R \gg K_m$ 에서 zero-order loss로, $R \ll K_m$ 에서 기본 turnover model로 환원.

#### C. Structural Necessity

**왜 정확히 4개인가?**

작용 형태 = {inhibit, stimulate} (2가지) × 작용 부위 = {$k_{in}$, $k_{out}$} (2가지) → 2 × 2 = 4. 추가 부위는 baseline 정의 자체를 깨뜨리고, 추가 작용 형태는 inhibit + stimulate의 조합으로 환원된다. 따라서 **Reversible turnover의 표준 분류는 정확히 4** 이며 더하거나 빼지 않는다.

#### D. Assumptions & Boundary Conditions

- $H(C)$ 의 한계가 모델 거동을 결정 ($I_{max} \le 1$ 강제).
- 약물이 작용 부위 1개에만 작용 (synergy 모델 G Eq 3:107 후반은 두 부위 동시).
- $H(C)$ 가 R에 의존하지 않음 (의존하면 자가조절 / negative feedback).

#### E. Limitations

- 4 모델은 *시작점* 이지 *끝점* 이 아니다. Transit compartment, precursor-pool, multi-compartment response, capacity-limited 등의 확장이 임상 데이터에서 흔히 필요.
- 단일 약물 작용 가정; 활성 대사물질이 함께 있으면 모델 식별 불가능.

#### F. Five Cognitive Layers

| Layer | 내용 |
|-------|------|
| **L1** | 4 ODE 표준형, $R_{ss}$ / $\Delta R$ / limit / return 4행 표 |
| **L2** | R-t 곡선의 4가지 모양 (down-up-up-down × dose-shifted-or-not) |
| **L3** | RC회로 4종: voltage source 변경 vs resistance 변경 |
| **L4** | warfarin-vitamin K, furosemide-tubule, EPO-erythron, CB1-energy expenditure 분자 회로 + R&T 임상 anchor (warfarin / ranitidine / paclitaxel) |
| **L5** | NONMEM `$DES`에서 4 ODE 패턴 직접 코드, GOF에서 peak-shift 패턴으로 모델 선택; NDA Briefing Document에서 R&T 어휘로 작용기전 서술 |

#### G. Zettelkasten Atom

```yaml
---
aliases: [Turnover taxonomy, IDR Models 1-4, Four canonical models, R&T four cases]
tags: [pharmacometrics/pkpd, turnover-model, taxonomy]
up: "[[Card1-TurnoverFoundation]]"
related: ["[[Card3-tssDiscrimination]]", "[[PD4-Warfarin]]", "[[PD5-Furosemide]]", "[[PD6-EPO]]", "[[PD7-CB1]]", "[[RnT-Ranitidine]]", "[[RnT-Paclitaxel]]"]
source: "Gabrielsson & Weiner 5e, Ch.3 §3.7.2, Table 3.3, p.238 + Rowland & Tozer 5e, Ch.8, p.241"
---
```

Reversible turnover의 표준 4 모델은 작용 형태(inhibit/stimulate) × 작용 부위($k_{in}$/$k_{out}$)의 2×2 격자다. Models 1&3은 $k_{out}$ 단독으로 tss를 결정 → dose-independent tss; Models 2&4는 $k_{out} \cdot H(C)$로 tss 결정 → dose-dependent tss (peak-shift). G의 수식 우선 framing과 R&T의 *increase/decrease formation/elimination* 임상 framing이 같은 격자의 두 어휘. NDA 문서에서 R&T 어휘로 작용기전 서술, NONMEM 코드에서 G 수식 구현.

---

### ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### Card 3 — tss-Based Mechanism Discrimination
### ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<!-- MASTER LENS -->
#### [개념 Big Idea: 거장의 시각]

Phase 2 임상시험 데이터에서 **하나의 시각적 신호** — 용량을 올렸을 때 *peak가 옆으로 움직이는가, 위아래로만 움직이는가* — 가 약물의 작용 부위를 거의 즉각 결정한다. Peak가 시간축으로 움직이지 않으면 ($\leftrightarrow$) 약물은 **생산 손잡이($k_{in}$)** 를 비틀고 있다 (Models 1 또는 3). Peak가 시간축으로 움직이면 ($\downarrow$ 또는 $\rightarrow$) 약물은 **소실 손잡이($k_{out}$)** 를 비틀고 있다 (Models 2 또는 4).

이 한 번의 시각 판독이 *분자생물학의 두 가지 다른 hypothesis* — 이 약물이 합성 경로를 막는가, 분해 경로를 막는가 — 를 임상 데이터로부터 직접 답하게 한다. 단, **Card 8 (PK vs PD rate-limiting)** 의 전제 조건이 충족되어야 한다 — PK가 PD보다 충분히 빠를 때만 tss 시그널이 PD 동역학을 직접 반영. PK가 느리면 tss 시그널이 PK kinetics에 묻혀 작용 부위 식별 불가능.

이 직관 — *peak-shift = $k_{out}$ 작용; no shift = $k_{in}$ 작용; 단 PK rate-limiting일 때는 어느 시그널도 신뢰 불가* — 을 박고 진행하라. 7번 카드에서 이 직관이 *선형 $S(C)$ + 단일 dose-range* 라는 또 다른 조건에서도 깨진다는 것을 배운다.

#### A. Formal Definition

**tss (time to pharmacodynamic steady state)** 의 dose 의존성은 약물 작용 부위가 $k_{in}$ 인지 $k_{out}$ 인지를 결정한다.

- **Models 1 & 3 (kin-action)**: tss는 $k_{out}$ 에 의해서만 결정 → **dose-independent** tss (≈ 3–4 × $t_{1/2,k_{out}}$)
- **Models 2 & 4 (kout-action)**: tss는 $k_{out} \cdot H(C)$ 에 의해 결정 → **dose-dependent** tss (peak-shift)

**전제 조건 (R&T 통합)**: 위 시그널은 *PD가 rate-limiting* 일 때만 유효. PK가 rate-limiting이면 tss는 약물의 PK $t_{1/2}$ 에 의해 결정되고 PD 작용 부위와 무관 — Card 8 참고.

#### B. Derivation / Code Structure

**왜 Models 1&3 은 dose-independent tss인가?** ODE 분석:

$$\text{Model 1: } \frac{dR}{dt} = k_{in} \cdot I(C) - k_{out} R$$

$I(C)$는 *생산 항 앞*에 곱해진다. R의 *접근 속도*를 결정하는 것은 *손실 항*의 R 계수 = $k_{out}$ 단독. dose가 변해도 $k_{out}$ 은 변하지 않으므로 tss 동일.

$$\text{Model 2: } \frac{dR}{dt} = k_{in} - k_{out} \cdot R \cdot I(C)$$

$I(C)$는 *손실 항* 안의 R 계수에 곱해진다. *Effective $k_{out}$* = $k_{out} \cdot I(C)$ 가 dose에 따라 변한다.

> 📎 [Micro-citation] tss governor 표 [출처: Gabrielsson 5e, Ch.3, Table 3.5, p.247]
> 📎 [Micro-citation] Fig 3.41 — dose impact on tss 4 panel [출처: Gabrielsson 5e, Ch.3, p.248]

**임상 데이터 진단 절차**:

```
[Step 0] PK rate-limiting 여부 확인 (Card 8) — PK t1/2가 PD t1/2보다 충분히 작은가?
  ├── NO  → tss 진단 신뢰 불가, PK 데이터부터 분석
  └── YES → Step 1로 진행
[Step 1] 2-3개 dose level 데이터 확보 (PD7과 동일한 설계)
[Step 2] Peak (또는 trough) 시점을 dose마다 기록
[Step 3] Peak time이 dose에 따라 시간축으로 이동하는가?
   ├── NO  → kin-action → Model 1 (감소) or Model 3 (증가)
   └── YES → kout-action → Model 2 (증가) or Model 4 (감소)
[Step 4] 반응 변화 방향 (baseline 대비 ↑/↓) 으로 inhibit/stimulate 결정
```

**PD5 vs PD7 대조 (Stage 1 anchored example)**:
- **PD5** (Model 2 inhibition of $k_{out}$): 3개 infusion 4000/16000/80000 over 6 h, 반응이 baseline 위로 상승, **tss가 dose에 따라 길어짐**. 모델 식별: Model 2.
- **PD7** (Model 4 stimulation of $k_{out}$): 3개 infusion 6400/32000/160000 over 4 h, 반응이 baseline 아래로 하강, **tss가 dose에 따라 짧아짐**. 모델 식별: Model 4.

**R&T 임상 등가 사례 (Stage 2 통합)**:
- **Warfarin** 1.5 mg/kg oral (R&T Fig 8-10): 반응 (prothrombin complex activity)이 1-2일 후 maximum 도달, dose 변경 시에도 *time-to-maximum* 거의 일정 → Model 1 (inhibition of $k_{in}$). 단, 이것은 Card 8의 *PD-limited* 사례 — tss 시그널은 PD 시계만 반영 (PK는 빠르게 평형).
- **Ranitidine** 50 mg i.v. (R&T Fig 8-8): gastric pH가 dose에 따라 다른 plateau에 도달하며 tss 거동이 dose-dependent → Model 2 (inhibition of $k_{out}$, 산 분비 억제로 gastric pH의 effective loss rate 감소).

#### C. Structural Necessity

R-t 평면에서 1차 ODE의 시간 상수 $\tau$ 는 *손실 항의 R 계수*에 의해서만 결정된다. 이것은 1차 선형 ODE의 수학적 귀결이지 약물의 화학적 성질이 아니다 — 어떤 약물이든 이 작용 부위에서 작용한다면 같은 tss 패턴이 강제로 따라온다.

#### D. Assumptions & Boundary Conditions

- **Css 일정 가정**: tss 정의 자체가 constant input(infusion at steady state) 가정. IV bolus나 oral은 약물 PK가 빠르게 평형되어야 PD tss가 의미를 가진다.
- **PK rate-limiting 확인 필수 (R&T 통합)**: PK가 PD보다 빨라야 tss가 PD 작용 부위를 반영. 그렇지 않으면 tss는 PK $t_{1/2}$ 단독 함수 → Card 8.
- **선형 $H(C)$의 함정**: $H(C) = 1 + a \cdot C$ 가 $k_{in}$ 에 작용할 때 peak-shift가 *없다* — 이것이 Card 7에서 다룰 effect compartment 모델과의 indistinguishability 위기.
- **데이터 해상도**: 2개 이상 dose level + peak 주변 sampling이 충분해야 판독 가능.

#### E. Limitations

- Single-dose 데이터로는 tss 비교 불가 (반복 dose 또는 multi-level 필수).
- PK rate-limiting일 때 tss 시그널 무력화 — Card 8 결합 필수.
- Nonlinear $H(C)$ 는 $k_{in}$ 작용이어도 peak-shift 만들 수 있음 (PD9 Fig 9.5 right) — 확정 진단 위해 dose-range 충분히 넓혀야.

#### F. Five Cognitive Layers

| Layer | 내용 |
|-------|------|
| **L1** | tss governor: $k_{out}$ vs $k_{out} \cdot H(C)$; $t_{1/2}^{eff}$; PK vs PD rate-limiting 전제 조건 (Card 8) |
| **L2** | Fig 3.41 4-panel: 2 panel은 vertical arrows only, 2 panel은 horizontal arrows |
| **L3** | RC 회로: voltage source 변화 vs resistance 변화 (둘 다 final voltage 변경, but only resistance 변화가 time constant 변경) |
| **L4** | 합성 경로 차단(synthesis block) vs 분해 경로 차단(degradation block)의 시간 거동 차이; warfarin (synthesis block, R&T) vs ranitidine (acid secretion block) 임상 대조 |
| **L5** | Phase 2 PK/PD 보고서에서 peak-shift figure를 작용기전 evidence로 인용; FDA Briefing Document에서 "the dose-dependent shift in tmax supports a $k_{out}$-targeting mechanism, given that PK clearance is sufficiently fast (t½ ~ Xh) relative to PD turnover (t½ ~ Yh)"으로 모델 선택 정당화 |

#### G. Zettelkasten Atom

```yaml
---
aliases: [tss discrimination, peak-shift diagnosis, kin-vs-kout signature]
tags: [pharmacometrics/pkpd, mechanism-inference, model-selection]
up: "[[Card2-FourModelTaxonomy]]"
related: ["[[Card7-DiscriminationCrisis]]", "[[Card8-RateLimiting]]", "[[PD5-Furosemide]]", "[[PD7-CB1]]", "[[RnT-Warfarin]]", "[[RnT-Ranitidine]]"]
source: "Gabrielsson & Weiner 5e, Ch.3 §3.7.3, Table 3.5, Fig 3.41, p.247-248 + Rowland & Tozer 5e, Ch.8, p.241-242 (4 IRM cases) and Fig 8-8, 8-10"
---
```

tss의 dose 의존성은 turnover model의 작용 부위를 식별한다. Models 1&3 (kin-action)은 dose-independent tss, Models 2&4 (kout-action)은 dose-dependent tss. PD5(Model 2)는 dose↑에서 tss↑, PD7(Model 4)은 dose↑에서 tss↓를 보여 단일 시각 판독으로 작용기전 가설 확정. R&T 임상 등가: warfarin (Model 1, dose-independent time-to-max)과 ranitidine (Model 2, dose-dependent tss). 단, **PK rate-limiting일 때 tss 시그널 무력화** (Card 8 전제), 그리고 *nonlinear H(C)* 또는 *PK rate-limiting* 일 때 깨질 수 있음.

---

### ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### Card 4 — Imax / Emax Multiplier Semantics + Dose-Linearity Trap
### ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<!-- MASTER LENS -->
#### [개념 Big Idea: 거장의 시각]

같은 기호 $E_{max}$ 가 세 개의 다른 모델에서 *서로 다른 물리량* 을 가리킨다 — 이것이 PK/PD 입문자가 가장 오래 가지고 다니는 표기법 함정이다. 직접 Emax 모델에서 $E_{max}$ 는 baseline에서 최대 반응까지의 *절대 거리(absolute distance)* 다. 하지만 turnover model로 넘어가는 순간, $E_{max}$ 는 baseline의 *배수(multiplier)* 가 되며, 실제 관측 가능한 변화량은 $\Delta R = R_0 \cdot E_{max}$ 또는 $R_0 \cdot E_{max}/(1+E_{max})$ 이다.

R&T가 추가하는 결정적 임상 함정은 **dose linearity in PK ≠ dose linearity in PD** (Fig 8-25, 8-26, 8-27, methylprednisolone 16-1000 mg). PK는 완벽히 선형 (AUC ∝ Dose) 이어도 PD는 비선형 — 16배 dose 증가에 lymphocyte suppression이 거의 동일한 plateau (500 vs 1000 mg에서 시각적 구분 불가). 이 사실 하나가 Phase 1 dose escalation 데이터로부터 Phase 2 임상 효력을 *비례 외삽* 하는 모든 시도를 무효로 만든다 — 신약 개발에서 가장 흔한 정량 오류 중 하나.

이 의미 차이를 모르고 같은 $E_{max}$ 값을 두 모델 간에 옮기면 — 예컨대 *in vitro* 에서 추정한 $E_{max}$ 를 *in vivo* turnover 모델 시뮬레이션에 그대로 넣으면 — **신약 후보의 효력 추정에 정확히 baseline 배수만큼의 오차** 가 생긴다. 그리고 PK 선형성을 PD 선형성으로 외삽하면 *고용량의 imminent toxicity ceiling을 sub-clinical로 잘못 보고* 한다.

이 직관 — *$E_{max}$ 는 모델마다 의미가 다르다, dose-linearity는 PK에서 PD로 자동 이전되지 않는다, 항상 $\Delta R$ 또는 $\Delta R/R_0$ 비율로 환원해서 비교하라* — 을 박고 진행하라.

#### A. Formal Definition

세 모델에서 $E_{max}$ (또는 $I_{max}$)의 의미가 다르다:

1. **직접 Emax 모델 (G Fig 3.40 left)**: $E = E_0 + \frac{E_{max} \cdot C^n}{EC_{50}^n + C^n}$ → $E_{max}$ = $R_{max} - E_0$ (절대 거리)
2. **재모수화 직접 Emax (G Fig 3.40 middle)**: $E = E_0 \cdot (1 + \frac{E_{max} \cdot C^n}{EC_{50}^n + C^n})$ → $E_{max}$ = baseline 배수
3. **간접 (turnover) Model 3 (G Fig 3.40 right)**: $R_{ss} = R_0 \cdot (1 + \frac{E_{max} \cdot C^n}{EC_{50}^n + C^n})$ → $E_{max}$ = $k_{in}/k_{out}$ baseline의 배수, 그리고 $\Delta R = R_0 \cdot E_{max}$ 는 약물 효력 + system parameter의 곱.

#### B. Derivation / Code Structure

**$\Delta R$ 의 4 형태 (G Fig 3.42 + Eq 3:83/89/95/101)**:

| Model | $\Delta R$ | $I_{max}/E_{max}$ 추정식 (역산) |
|-------|-----------|------------------------|
| 1 | $R_0 \cdot I_{max}$ | $I_{max} = 1 - R_{min}/R_0$ |
| 2 | $R_0 \cdot \frac{I_{max}}{1-I_{max}}$ | $I_{max} = 1 - R_0/R_{max}$ |
| 3 | $R_0 \cdot E_{max}$ | $E_{max} = R_{max}/R_0 - 1$ |
| 4 | $R_0 \cdot \frac{E_{max}}{1+E_{max}}$ | $E_{max} = R_0/R_{min} - 1$ |

> 📎 [Micro-citation] $\Delta R$ 4 forms [출처: Gabrielsson 5e, Ch.3, Table 3.6, p.251]

**Dose linearity in PK ≠ dose linearity in PD (R&T 통합, Fig 8-25 / 8-26 / 8-27, p.257-258)**:

Methylprednisolone 임상 데이터:
- *PK linearity*: AUC vs Dose가 16-1000 mg 범위에서 직선 (Fig 8-26, methylprednisolone과 phosphate prodrug 모두). "double the dose, double the AUC"가 정확히 성립.
- *PD nonlinearity*: lymphocyte suppression의 시간 곡선이 각 dose에서 dose 비례 *전혀 안 함* (Fig 8-27). 16 mg에서 명확한 suppression, 32 mg에서 더 깊은 suppression, 그러나 500 vs 1000 mg에서는 시각적으로 거의 구분 불가능 — *plateau 도달*.

R&T 인용 (p.256): "Dose-proportional pharmacokinetics is quite common. ... However, looking at the pharmacodynamics is a completely different story. ... It is obvious from visual inspection that the pharmacodynamic responses are not close proportional, and doubling of the dose results in much less than a doubling of the response."

**메커니즘 분해**:
- PD plateau의 수학적 원인 = sigmoid $H(C)$ 함수의 saturation. 직접 Emax 모델: $E_{max}$ 절대 한계 도달. Turnover Model 3: $R_0 \cdot (1 + E_{max})$ 한계 도달.
- 임상적 귀결: high-dose에서 효력 증가 없이 부작용만 증가 → therapeutic window의 *upper boundary* 가 PK가 아닌 PD에서 결정됨.

**Plausible Fallacy: 직접 Emax 추정값을 turnover 모델에 그대로 사용** (Stage 1에서 다룬 함정에 추가):

*시나리오 1 (Stage 1)*: PD6 EPO-like 약물에서 *in vitro* receptor binding assay로 $E_{max} = 4$ 추정. 동일 값을 *in vivo* turnover Model 3 시뮬레이션에 입력 → baseline (≈42.2) 배수만큼의 absolute response 단위 오차.

*시나리오 2 (R&T 추가)*: Phase 1에서 16-125 mg 범위로 dose escalation 후 lymphocyte suppression이 dose에 *비례한다* 고 잘못 결론 → Phase 2/3에서 500 mg를 채택 → 임상 효력 증가 없음, but 글루코코르티코이드 부작용 (혈당 상승, 골다공증, 면역억제) 직접 비례. 이는 *dose linearity in PK*가 *dose linearity in PD* 를 함의한다는 가정의 직접 결과.

#### C. Structural Necessity

직접 모델에서 $E_{max}$ 가 absolute distance인 이유는 모델 자체가 baseline + drug-induced increment의 *덧셈* 구조이기 때문 ($E = E_0 + ...$). 간접 모델에서 multiplier인 이유는 turnover의 정상상태 해 $R_{ss} = (k_{in}/k_{out}) \cdot H(C)$ 가 baseline의 *곱셈* 구조이기 때문. 두 모델은 단순히 다른 reparameterization이 아니라 *근본적으로 다른 인과 구조* 를 표현.

PK linearity vs PD nonlinearity의 수학적 필연성: PK ODE가 선형 ($\frac{dC}{dt} = -kC$, $C \propto Dose$) 이어도 PD response는 *Hill 함수* (비선형) 를 통해 농도와 연결됨. 따라서 농도 선형성이 자동으로 반응 선형성으로 전이되지 않음.

#### D. Assumptions & Boundary Conditions

- $I_{max} \le 1$ 강제 (G Eq 3:77 정의에 의해): partial inhibition은 $0 < I_{max} < 1$, full inhibition은 $I_{max} = 1$. 1을 넘는 추정값이 나오면 모델 misspecification 신호.
- Hill coefficient $n$ 이 1을 크게 벗어나면 (n > 3 또는 n < 0.5) 단순 sigmoid 가정 의심.
- *PK linearity가 PD linearity를 함의하지 않음* (R&T 명시).

#### E. Limitations

- $E_{max}$ 와 $EC_{50}$ 는 광역 dose-range 데이터 없이 식별 어려움. PD6 fitting에서 linear $S(C)$ 채택은 dose-range가 ~16배에 불과해 sigmoid plateau에 도달 못한 반영.

#### F. Five Cognitive Layers

| Layer | 내용 |
|-------|------|
| **L1** | $\Delta R = R_0 \cdot I_{max}$ vs $R_0 \cdot I_{max}/(1-I_{max})$ vs $R_0 \cdot E_{max}$ vs $R_0 \cdot E_{max}/(1+E_{max})$; PK AUC ∝ Dose ≠ PD response ∝ Dose |
| **L2** | G Fig 3.40 3-panel: $E_{max}$ 화살표가 같은 기호인데 길이가 다름; R&T Fig 8-27 8-panel: PK는 평행 ascending이지만 PD는 plateau로 수렴 |
| **L3** | additive vs multiplicative 효과; Hill 함수의 비선형이 농도-반응 변환 단계에서 dose 선형성을 깨뜨림 |
| **L4** | drug efficacy(약물 고유 활성) vs system response capacity (조직 baseline 활성) 의 분해 — 직접 모델은 둘을 합치고, turnover 모델은 분리 |
| **L5** | NDA report에서 "$E_{max} = 4$ 의 의미" 문장 — turnover 모델 채택 시 항상 baseline 곱셈 의미임을 명시; methylprednisolone 사례를 dose escalation 전략 문서에 인용하여 *PK linearity로부터 PD linearity 외삽 금지* 명시 |

#### G. Zettelkasten Atom

```yaml
---
aliases: [Emax semantics, Imax multiplier, Fig 3.40 paradox, dose linearity trap]
tags: [pharmacometrics/pkpd, parameterization, fallacy, dose-linearity]
up: "[[Card2-FourModelTaxonomy]]"
related: ["[[DirectEmaxModel]]", "[[Card1-Foundation]]", "[[RnT-Methylprednisolone]]"]
source: "Gabrielsson & Weiner 5e, Ch.3 Fig 3.40, p.246; Table 3.6, p.251 + Rowland & Tozer 5e, Ch.8, Fig 8-25/26/27, p.256-258"
---
```

같은 $E_{max}$ 기호가 세 모델에서 다른 의미. 직접 모델: absolute distance; 재모수화/turnover: baseline multiplier. 항상 $\Delta R/R_0$ 비율로 환원 비교. R&T 추가 함정: PK linearity (methylprednisolone AUC ∝ Dose 16-1000mg)는 PD linearity를 함의하지 않음 — lymphocyte suppression은 500/1000mg에서 plateau. Phase 1 dose escalation 시 PK 선형성으로부터 PD 효력 비례 외삽 금지 — Hill 함수의 sigmoid saturation이 dose-response 변환 단계에서 비선형성 도입.

---

### ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### Card 5 — Graphical Initial Parameter Estimation + Blocking Dose
### ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<!-- MASTER LENS -->
#### [개념 Big Idea: 거장의 시각]

NONMEM에 진입하기 전 종이 위에서 30분의 그래픽 분석이 *추정 시간을 며칠 단축* 하고 *수렴 실패의 80%를 사전 차단* 한다. PD4–PD9 다섯 사례 전체에서 동일한 4 규칙이 반복된다: ① downswing slope → $k_{out}$, ② baseline intercept → $R_0$, ③ mid-response time → $IC_{50}$/$EC_{50}$ at corresponding $C$, ④ initial slope (rising/falling) → $k_{in}$ 또는 $H(C) \cdot k_{in}$.

R&T가 추가하는 결정적 임상 도구는 **blocking dose 절차** — synthesis (또는 production)를 *완전히 차단* 하는 충분히 큰 dose를 한 번 시행하면, 그 동안의 단순 지수 감쇠로부터 $k_t$ ($k_{out}$의 R&T notation)가 *직접* 추출된다. Warfarin 1.5 mg/kg oral이 첫 48 hr 동안 prothrombin complex synthesis를 거의 100% 차단하면서 $k_t$ ≈ 0.06 day⁻¹ 추출 (Fig 8-15A). 이것은 graphical 추정의 임상 등가물이며, in vivo $k_t$ 의 *직접 측정* — receptor occupancy 100% 가정 하에서 — 으로 PD6 같은 식별성 위기조차 우회할 수 있는 강력한 도구다.

이 직관 — *그래픽 4 규칙이 NONMEM 시작값의 90%를 결정한다, 그리고 blocking dose는 그 4 규칙 중 가장 중요한 $k_{out}$ 을 임상에서 직접 측정하는 단일 실험* — 을 박고 진행하라.

#### A. Formal Definition

Turnover model 4가지의 초기 파라미터 추정에 사용되는 4가지 규칙(G Table 3.6, Eq 3:104):

1. **$k_{out}$**: 차단 후 downswing log-slope = $-k_{out}$ (Models 1, 3) 또는 $-k_{out}(1+E_{max})$ (Model 4)
2. **$k_{in}$**: $k_{in} = R_0 \cdot k_{out}$ (G Eq 4:6)
3. **$IC_{50}$ / $EC_{50}$**: 반응이 50% 변화한 시점의 $C$ (PK 식에 시간 대입)
4. **Initial slope**: $\frac{\Delta R}{\Delta t}\big|_{t=0}$ → 모델별 4개 표현식

**R&T blocking dose 절차 (Stage 2 통합)**: synthesis (또는 production) 항을 완전 차단하는 dose에서:

$$\frac{dA}{dt} = -k_t \cdot A \quad \Rightarrow \quad A(t) = A_0 \cdot e^{-k_t \cdot t}$$

따라서 ln(A) vs t plot의 직선 slope = $-k_t$ → $k_t$ 직접 추출. 차단 가정 검증: 다양한 dose에서 동일 slope 확인 (R&T Fig 8-15B: 0.75/1.5/3.0 mg/kg에서 36 hr 시점 잔존 활성 모두 22-24%).

#### B. Derivation / Code Structure

**Initial slope 4 cases (G Eq 3:104 + Table 3.6)**:

| Model | Initial $\frac{\Delta R}{\Delta t}$ | Linear/Log scale | 추정되는 양 |
|-------|---------------------|------|--------|
| 1 (inhibit $k_{in}$) | $-k_{out}$ | log-linear | $k_{out}$ 직접 |
| 2 (inhibit $k_{out}$) | $k_{in}$ | linear (zero-order build-up) | $k_{in}$ 직접 |
| 3 (stimulate $k_{in}$) | $S(C) \cdot k_{in}$ | linear (zero-order build-up) | $S(C) \cdot k_{in}$ |
| 4 (stimulate $k_{out}$) | $-S(C) \cdot k_{out}$ | log-linear | $S(C) \cdot k_{out}$ |

> 📎 [Micro-citation] Initial slope 4가지 [출처: Gabrielsson 5e, Ch.3, Eq 3:104 + Table 3.6, p.250-251]
> 📎 [Micro-citation] R&T blocking dose 절차 [출처: Rowland & Tozer 5e, Ch.8, p.246-247, Fig 8-15]

**PD4 warfarin 적용 예시 (Stage 1) + R&T blocking dose 절차 (Stage 2 통합)**:

```
[Gabrielsson G PD4 graphical 절차]
Step 1 — kout 추출:
  warfarin iv bolus 후 PCA 초기 강하 구간 (24시간 부근).
  R(0) ≈ 124.4, R(24) ≈ 56.77 (관측 데이터)
  kout = (ln 124.4 - ln 56.77) / 24 ≈ 0.03 h⁻¹  [G Eq 4:8]

Step 2 — R0 추출:
  pre-dose intercept ≈ 121 sec.

Step 3 — kin 추출:
  kin = R0 · kout = 121 · 0.03 ≈ 3.6 sec/h  [G Eq 4:6]

Step 4 — IC50 추출:
  Figure 4.4의 t_{IC50} (반응이 baseline-trough 중간점)
  → 약 80 h. C(t) = 1.05·e^(-0.0228·t) → C(80) ≈ 0.17 mg/L ≈ IC50 초기 추정

[R&T blocking dose 절차 — 동일 약물의 임상 등가]
Step A — Blocking dose 시행:
  Warfarin 1.5 mg/kg oral (sodium salt). 충분히 큰 dose로 첫 24-48 hr 동안
  prothrombin complex synthesis Rsyn ≈ 0.

Step B — 단순 지수 감쇠 추출:
  ln(prothrombin complex activity) vs time, 첫 48 hr.
  Fig 8-15A: 약 100% → 약 12% (linear semi-log)
  slope = (ln 100 - ln 12) / 48 ≈ 0.044 hr⁻¹ ≈ 1.06 day⁻¹? — 단위 불일치 [확인 필요]
  R&T text: "the prothrombin complex activity then falls exponentially so that a
  semilogarithmic plot ... gives a straight line with a slope of kt"
  Fig 8-10 본문에서 clotting factor 반감기 1-2 days 명시 → kt ≈ 0.5-1.4 day⁻¹

Step C — 차단 가정 검증:
  0.75/1.5/3.0 mg/kg 3개 dose에서 36 hr 시점의 잔존 활성 비교 (Fig 8-15B).
  세 dose 모두 약 22-24% → 동일 slope = 동일 kt → blocking 확인.

Step D — 비-blocking dose에서 inhibition curve 추출:
  R_syn = (A2 - A1)/Δt + kt · (A1 + A2)/2  [R&T Eq 8-7]
  Percent inhibition = 100 · (R_syn(n) - R_syn) / R_syn(n)  [R&T Eq 8-8]
  이를 ln(warfarin concentration) 에 대해 plot → hysteresis-free graded response
  곡선 (Fig 8-16). 직접 IC50 / Imax / n 추정 가능.
```

**Sensitivity analysis (PD4 Fig 4.5–4.8)**: 시작값 ±50–100% 변경 시 곡선 모양 변화 패턴 → 어느 영역의 데이터가 어느 파라미터에 정보를 담고 있는지 시각화.

**Dose-Response-Time framework (G CONTEXT 통합, §3.10 Fig 3.60)**: 농도 측정이 부재할 때 (안과 국소 투여, 흡입제 등), 반응-시간 곡선의 *각 segment* 가 다른 파라미터를 식별. PD25 prostaglandin 안과 사례 (G Eq 3:148–3:149, doses 0.1 / 1.0 / 10 µg)가 정확히 이 패턴.

**Duration formula 의 graphical 활용 (Card 9 forward reference)**: R&T Eq 8-12의 $t_D = \frac{1}{k}\ln(\frac{Dose}{C_{min} \cdot V})$ 는 *dose-duration* plot의 slope = $1/k$, intercept (at zero duration) = $\ln A_{min}$ ($A_{min} = C_{min} \cdot V$) 로 graphical 추출 가능. Succinylcholine T50 vs log(dose) (R&T Fig 8-24, 0.1-10 mg/kg): slope ≈ 1/k → $k$ ≈ 0.2 min⁻¹ → $t_{1/2}$ ≈ 4 min. PK-limited 약물에서는 graphical 4 규칙의 5번째 규칙이 된다.

#### C. Structural Necessity

각 segment가 *다른* 파라미터를 식별하는 이유는 ODE의 *각 항* 이 *다른 시간 스케일* 에서 dominant이기 때문:

- $t \approx 0$ (drug 작용 직후): 한쪽 항이 0 → log-slope = $-k_{out}$
- $t \to \infty$: 정상상태 → $R_{ss}$ formula → $H(C)$ 와 $H_{50}$
- $t$ 중간: 두 항 균형 → $\Delta R$ 표현

**Blocking dose의 구조적 토대 (R&T 통합)**: ODE에서 $R_{syn} = 0$ 이면 잔여 항은 $-k_t \cdot A$ 단독 → pure 1차 감쇠. 이는 Card 1의 *reparameterization* 의 임상 등가 — 두 unknown ($R_{syn}$, $k_t$) 중 하나를 0으로 강제하면 나머지는 직접 추출 가능. Card 6 irreversible model의 *drug=0에서 loss=0* 구조가 *역방향* 형태로 등장 — drug=∞ (blocking)에서 production=0.

#### D. Assumptions & Boundary Conditions

- Css 일정 (또는 PK가 PD보다 빨라 quasi-steady) 가정.
- 충분한 sampling density (특히 peak/trough 주변).
- Blocking dose 절차의 가정: 시행 dose에서 production을 *완전* 차단 (≥95%) — partial inhibition이면 추정된 $k_t$ 가 편향 ($k_t^{apparent} = k_t \cdot (1 + \text{partial inhibition factor})$).
- Blocking dose 시행이 환자 안전성 측면에서 가능해야 (warfarin은 가능, EPO는 어려움).

#### E. Limitations

- Single-point graphical 추정은 noise에 민감. 복수 시점 추정 후 평균.
- Multi-dose 데이터에서 superposition이 깨지면 시작값이 더 신중해야.
- Sensitivity analysis는 시작값 *근방* 의 동작만 보여줌; 광역 비선형성 검증에는 불충분.
- Blocking dose는 *PD-limited* 약물에서만 의미 있음 — PK-limited (Card 8) 일 때는 단순 PK $t_{1/2}$ 을 측정할 뿐.

#### F. Five Cognitive Layers

| Layer | 내용 |
|-------|------|
| **L1** | 4 규칙 + initial slope 4 cases + residual κ method + R&T blocking dose Eq 8-7/8-8 + dose-duration graphical method (Card 9) |
| **L2** | 각 그래프 segment에 색칠 — "이 영역은 $k_{out}$ 정보, 저 영역은 $IC_{50}$ 정보"; R&T Fig 8-15A의 단순 지수 감쇠 직선 직관 |
| **L3** | 시간-스케일 분리: 빠른 모드 vs 느린 모드 (singular perturbation); blocking dose는 ODE 의 *projection onto 1D submanifold* |
| **L4** | 효소 합성·분해의 인과 시간 척도 분리; warfarin clotting factor synthesis 차단의 분자 메커니즘 (vitamin K reductase 비가역 억제) |
| **L5** | NONMEM `$THETA` 시작값 결정, sensitivity plot, FOCE 1차 시도 전 종이 작업; R&T blocking dose 절차로 in vivo $k_t$ 직접 측정 후 NONMEM 시작값 배포 — Phase 1 PK/PD 보고서의 표준 절차 |

#### G. Zettelkasten Atom

```yaml
---
aliases: [Initial parameter estimation, Graphical IDR estimation, Pre-NONMEM analysis, Blocking dose method]
tags: [pharmacometrics/pkpd, parameter-estimation, workflow, clinical-method]
up: "[[Card2-FourModelTaxonomy]]"
related: ["[[NONMEM-Convergence]]", "[[Sensitivity-Analysis]]", "[[DRT-Models]]", "[[Card9-DurationFormula]]", "[[RnT-WarfarinBlockingDose]]"]
source: "Gabrielsson & Weiner 5e, Ch.3 §3.7.4, Table 3.6, p.251 + Rowland & Tozer 5e, Ch.8, p.246-247, Eq 8-7, 8-8, Fig 8-15"
---
```

Turnover 모델 4종의 초기 추정값은 그래픽 4 규칙: downswing log-slope → $k_{out}$, intercept → $R_0$, mid-point time → $IC_{50}$/$EC_{50}$ at corresponding $C$, initial slope → 모델별 4 표현식. R&T blocking dose 절차 (warfarin 1.5 mg/kg oral): production 완전 차단 후 단순 지수 감쇠 = 1차 ODE → $k_t$ 직접 추출 (Eq 8-7로 일반 dose에서 synthesis rate inversion). 검증: 다양한 dose에서 동일 slope 확인 (Fig 8-15B). PK-limited 약물에서는 dose-duration graphical method (Card 9, Fig 8-24)이 5번째 규칙으로 추가. NONMEM 시작값 결정의 임상-수학 연계 절차.

---

### ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### Card 6 — Irreversible Drug Action + Target Consumption
### ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<!-- MASTER LENS -->
#### [개념 Big Idea: 거장의 시각]

Reversible과 Irreversible 모델의 구조적 차이는 *수식 한 줄* 이다 — 하지만 그 한 줄이 항생제·항암제 영역 전체를 가르고, 잘못 적용하면 용량이 *수십 배 어긋난다*. Reversible: 약물 부재 시 loss = $-k_{out} \cdot R$ (drug=0에서도 normal turnover). Irreversible: 약물 부재 시 loss = 0 (drug=0에서 살상이 멎는다).

R&T가 결정적으로 추가하는 것은 **target consumption** 메커니즘 (p.251-252) — 약물이 *target receptor 자체* 를 비가역적으로 결합·불활성화시키는 경우. Aspirin은 cyclooxygenase를 acetylation으로 비가역 결합 (plasma $t_{1/2}$ 15 min, 효과 days 지속). Omeprazole은 proton pump에 covalent binding + 극도로 느린 dissociation 결합 (plasma $t_{1/2}$ < 1 hr, 효과 days 지속). 이것은 Gabrielsson의 "세포 살상" 형태와 *수학적으로는 등가* 이지만 — drug=0에서 *효과의 손실 = 0* — *임상 함의가 다르다*: 효과 회복은 약물 PK가 아닌 *target resynthesis* 가 결정.

이 모델군에서 가장 위험한 함정은 **K 표기 충돌** 이다. 동일 챕터 내에서 $K$ 가 *항생제 살상의 2차 속도상수* (단위: concentration⁻¹·time⁻¹)와 *약물 PK elimination의 1차 속도상수* (단위: time⁻¹)에 동시에 사용된다.

이 직관 — *Irreversible = drug=0에서 loss=0, target consumption은 effect-receptor의 turnover를 별도로 가짐, 단위가 모든 것을 결정한다* — 을 박고 진행하라.

#### A. Formal Definition

**Irreversible action model (cell-level)**: 약물 작용이 단방향(uni-directional)이며, 약물 부재 시 그 작용 자체가 0이 되는 형태.

$$\frac{dR}{dt} = -K \cdot C \cdot R \quad \text{[G Eq 3:110, second-order kill]}$$

여기서:
- $K$ = **2차 속도상수** (단위: 농도⁻¹·시간⁻¹, 예: L·mg⁻¹·h⁻¹ 또는 L·CFU⁻¹·h⁻¹) [확인 필요]
- $C$ = 약물 농도 (시간 함수)
- $R$ = 반응(예: bacterial count)

**Target consumption model (R&T 통합, p.251-252)**: 약물이 receptor / enzyme 자체를 비가역 결합·불활성화. Effect는 *active receptor 수* 에 비례. Target은 자체 turnover (synthesis + degradation):

$$\frac{dT_{active}}{dt} = k_{T,syn} - k_{T,deg} \cdot T_{active} - k_{cons} \cdot C \cdot T_{active}$$

$k_{cons}$ = consumption rate constant (2차). $C \to 0$ 이후에도 $T_{active}$ 의 회복은 *target 자체의 turnover* ($k_{T,syn}$ / $k_{T,deg}$) 로 결정.

> ⚠️ [확인 필요] **K 표기 충돌**: G §3.8에서 *bacterial kill 2차 상수*로 사용된 $K$ 가, 동일 PD 사례 내 G Eq 3:120 ($N = N_0 \cdot e^{-K \cdot AUC_0^t}$)에서 "K is the drug elimination rate constant"로 재정의됨 — 이때 $K$ 는 *PK 1차 elimination 상수* (단위: h⁻¹). R&T Ch.8에서는 (a) Eq 8-10 $C = (D/V)e^{-kt}$ 의 $k$ = PK elimination rate constant, (b) Eq 8-6 $\frac{dA}{dt} = R_{syn} - k_t \cdot A$ 의 $k_t$ = degradation rate constant, 의 *명시적 분리 표기* — R&T 어휘가 G의 표기 충돌을 해소. Phase 2 audit에서 G의 $K$ 사용 모두 $K_{kill}$ vs $k_{el}$ 로 분리 권장.

#### B. Derivation / Code Structure

**No-growth + irreversible kill (DRECKER model, Jusko [1971], G Fig 3.48 upper)**:

$$\frac{dR}{dt} = -K \cdot C \cdot R \quad \to \quad R = R_0 \cdot e^{-K \cdot AUC_0^t} \quad \text{[G Eq 3:111]}$$

생존 비율: $S_F = R/R_0 = e^{-K \cdot AUC_0^t}$ [G Eq 3:112]. **AUC가 효과를 결정** — 항생제 PK/PD의 "AUC/MIC" 지표의 이론적 기반.

**Cell growth + kill (logistic, G Eq 3:117, Fig 3.48 lower, CONTEXT 통합)**:

$$\frac{dN}{dt} = k_g \cdot N \cdot \left(1 - \frac{N}{B_{max}}\right) - k_k \cdot f(C) \cdot N \quad \text{[G Eq 3:117]}$$

정상상태:
$$N_{ss} = B_{max} \cdot \left(1 - \frac{k_k}{k_g} \cdot C_{ss}\right) \quad \text{[G Eq 3:121]}$$

**Aspirin target consumption 사례 (R&T Stage 2 통합, Fig 8-20, p.251)**:

```
[입력 약물]
Aspirin 650 mg oral, plasma t1/2 ≈ 15 min (Fig 8-20A).
2 hr 시점 plasma aspirin 거의 0.

[효과 곡선 (Fig 8-20B)]
Thromboxane B2 production inhibition (% of normal):
  t = 0:    ~95%
  t = 24 hr: ~85%
  t = 96 hr: ~70%
  t = 192 hr: ~22%
→ 효과의 회복까지 8 days 이상.

[메커니즘]
Aspirin은 prostaglandin cyclooxygenase를 acetylation으로 비가역 결합.
Effect는 platelet 수명 (~ 7-10 days) 동안 지속.
Aspirin이 모두 제거된 후에도 platelet의 cyclooxygenase가 비활성 상태로 유지.
새 platelet 생성으로만 효과 회복 → 회복 속도 = platelet turnover rate (≪ aspirin
PK clearance).

[Card 8과의 연결]
이는 PD-limited 약물의 표준 사례. PK clock = 0.04 hr⁻¹ (15 min t1/2).
PD clock = 0.004 hr⁻¹ (~7 day platelet turnover). PD clock이 10× 느림 → PD 지배.
$t_D$ formula (Card 9) 적용 불가능 (PK-limited 가정 위반).
```

**Omeprazole 사례 (R&T Stage 2 통합, Fig 8-21, p.252-253)**:

```
[입력 약물]
Omeprazole 40 mg oral, plasma t1/2 < 1 hr (Fig 8-21A, peak at ~0.4 hr,
3 hr 시점 plasma 거의 0).

[효과 곡선 (Fig 8-21B)]
Acid output (mmol/15 min, pentagastrin-stimulated):
  Pre-dose: ~9
  t = 2 hr: ~1 (≈ 90% inhibition)
  t = 24 hr: ~4
  t = 48 hr: ~6
  t = 72 hr: ~8
→ 효과의 회복까지 3 days 이상.

[메커니즘 — aspirin보다 복잡]
(1) Covalent binding to proton pump receptor in parietal cells.
(2) 매우 느린 dissociation of locally formed omeprazole-derived compounds from
    proton pump.
새 proton pump 합성 + slow dissociation 결합 → effect 회복 ~ days.

[임상 함의]
Plasma 농도가 측정 한계 이하인데 효과 지속 → "drug없이 효과" 환상 발생.
실제로는 *국소 결합* 약물이 존재하며 (단, 측정되지 않음), Card 8 framing에서 PD-limited
이지만 *plasma PK ≠ effect-site PK*.
```

**NONMEM 의사 코드 차이**:

```
; Reversible Model 4 (stimulate kout):
DADT(1) = KIN - KOUT*A(1)*(1 + EMAX*C/(EC50+C))
;        drug=0 일 때 loss = KOUT*A(1) (정상 turnover)

; Irreversible no-growth (cell-level):
DADT(1) = -K*C*A(1)
;        drug=0 일 때 loss = 0 (정지)

; Target consumption (R&T 사례):
DADT(1) = KTSYN - KTDEG*A(1) - KCONS*C*A(1)
;   A(1) = active target 수
;   drug=0 일 때 effect 회복 속도 = KTSYN, KTDEG에 의해 결정 (PK와 무관)
```

> 📎 [Micro-citation] G Eq 3:110 second-order kill [출처: Gabrielsson 5e, Ch.3, p.257]
> 📎 [Micro-citation] Logistic growth + kill [출처: Gabrielsson 5e, Ch.3, Eq 3:117, p.259]
> 📎 [Micro-citation] R&T Aspirin target consumption [출처: Rowland & Tozer 5e, Ch.8, p.251, Fig 8-20]
> 📎 [Micro-citation] R&T Omeprazole 메커니즘 [출처: Rowland & Tozer 5e, Ch.8, p.252-253, Fig 8-21]

#### C. Structural Necessity

**왜 2차 형태인가?** (cell kill 형태)

세포 살상은 약물-표적 충돌의 단위 시간당 빈도 = 약물 농도 × 표적 농도(밀도)에 비례. 화학반응의 mass-action law. 1차 형태 $-K \cdot R$ 은 *약물이 없어도 살상이 일어남* 을 의미하므로 약물 효과를 표현하지 못함. 0차 형태 $-K \cdot C$ 는 세포가 0이어도 살상이 계속됨을 의미해 비물리적.

**Target consumption의 구조적 필연 (R&T 통합)**: target receptor는 자체로 endogenous protein → R&T Eq 8-5의 *systems in flux* 일반 framework에 포섭됨. 약물의 비가역 결합은 이 turnover system의 *추가 loss term*. 따라서 target consumption은 cell kill의 분자 등가가 아니라 *Card 1의 turnover model + Card 6의 irreversible action* 의 *결합 모델* 임. Aspirin/omeprazole의 효과 시간 거동이 plasma PK와 분리된 이유가 정확히 이것 — receptor turnover가 PK보다 느림.

#### D. Assumptions & Boundary Conditions

- **Mass-action 가정**: 세포·약물 분포가 잘 섞여 있다. Heterogeneous infection (biofilm 등)에서는 깨짐.
- **Persistent organism 가정**: $k_g \cdot (1 - N/B_{max})$ 가 자체 turnover로 작동, 약물이 *추가* 살상.
- **Single agent**: 다제 병용 시 synergy 모델 필요.
- **Target consumption (R&T)**: receptor의 자체 turnover 시간 척도가 약물 PK 시간 척도보다 길어야 *visible* lag 발생. 그렇지 않으면 reversible과 구분 불가능.

#### E. Limitations

- 항생제 PD에서 post-antibiotic effect (PAE) 직접 표현 안 됨.
- $B_{max}$ 가 시스템 의존적.
- Resistant subpopulation은 단일 모델로 표현 불가; mixture model 또는 two-population 필요.
- Target consumption: *plasma 농도가 측정 한계 이하* 일 때 효과 지속을 *설명 변수 부재* 로 모델링 어려움. Plasma 농도를 *surrogate* 로 쓰지 말고 receptor occupancy를 직접 추정해야.

#### F. Five Cognitive Layers

| Layer | 내용 |
|-------|------|
| **L1** | $\frac{dR}{dt} = -K \cdot C \cdot R$, $R = R_0 e^{-K \cdot AUC}$, $S_F = e^{-K \cdot AUC}$; target consumption: $\frac{dT}{dt} = k_{T,syn} - k_{T,deg} T - k_{cons} C T$ |
| **L2** | semi-log plot에서 다양한 dose의 kill curve가 평행 → 이격 → 다시 평행; aspirin/omeprazole 효과가 plasma PK와 *완전히 분리된* 시간 척도 |
| **L3** | 화학반응의 mass-action vs 효소촉매 (Vmax/Km); target consumption은 *turnover + irreversible action* 의 결합 |
| **L4** | 항생제-세균, 항암제-종양세포, alkylating agent-DNA의 공통 second-order action; aspirin-cyclooxygenase, omeprazole-proton pump의 receptor-level target consumption |
| **L5** | NONMEM에서 IRREVERSIBLE kill 모델 코드, AUC/MIC 또는 AUC₂₄/MIC 지표 추정, FDA 항생제 가이드라인의 PK/PD target attainment 분석; aspirin/omeprazole의 dosing interval은 *plasma t1/2의 100배* (R&T 표현) — receptor turnover로부터 결정 |

#### G. Zettelkasten Atom

```yaml
---
aliases: [Irreversible drug action, Second-order kill, DRECKER model, Antibiotic PD, Target consumption]
tags: [pharmacometrics/pkpd, irreversible, antimicrobial, mass-action, target-consumption]
up: "[[Card2-FourModelTaxonomy]]"
related: ["[[Card1-Foundation]]", "[[Card8-RateLimiting]]", "[[AUC-MIC]]", "[[Logistic-Growth]]", "[[RnT-Aspirin]]", "[[RnT-Omeprazole]]"]
source: "Gabrielsson & Weiner 5e, Ch.3 §3.8, Eq 3:110-3:121, p.256-260 + Rowland & Tozer 5e, Ch.8, p.251-253, Fig 8-20, 8-21"
---
```

Irreversible 모델 $\frac{dR}{dt} = -K \cdot C \cdot R$ 는 약물=0에서 살상=0. $R = R_0 e^{-K \cdot AUC}$. K는 **2차** 상수 (농도⁻¹·시간⁻¹) — PK elimination K (1차)와 표기 충돌 [확인 필요]. R&T target consumption (aspirin, omeprazole): receptor 자체의 비가역 결합 + receptor turnover. Plasma t1/2 (15 min, <1 hr) ≪ effect duration (days). Card 8의 PD-limited 표준 사례. NONMEM 코드에서 *receptor compartment 별도 추가* 필요. AUC/MIC (cell kill) vs receptor occupancy duration (target consumption) 두 지표가 임상 dose-target 결정의 도구.

---

### ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### Card 7 — Turnover vs Effect Compartment Discrimination Crisis
### **⚡ Apex Concept**
### ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<!-- MASTER LENS -->
#### [개념 Big Idea: 거장의 시각]

이 세션의 모든 카드는 이 한 카드를 위한 준비였다.

*같은 임상 데이터에 대해 turnover model과 effect compartment(link) model이 똑같이 잘 맞는다* — PD6에서 WRSS 15516 vs 15518, AIC 1041 vs 1040. 이것은 데이터 부족이 아니라 *수학적 indistinguishability* 다. 선형 $S(C) = 1 + a \cdot C$ 가 $k_{in}$ 에 작용할 때, peak-shift도 없고, 잔차 패턴도 같고, 파라미터 recovery도 같다. 단일 dose-range 데이터로는 두 모델을 구별할 수 없다.

R&T가 추가하는 결정적 *분자 framing* 은 effect compartment의 **biophase distribution mechanism** 이다 (p.245, Fig 8-13). Effect compartment의 $k_{e0}$ 는 단순히 수학적 "delay 시간상수" 가 아니라 *약물이 site of action에 도달하는 분포 평형 속도* 다. Naproxen 500 mg oral의 hysteresis가 effect compartment fitting으로 사라지는 이유는 (Fig 8-2 → Fig 8-14): 약물 분포가 *dental tissue*까지 도달하는 데 약 4-5 hr 걸리기 때문 — *plasma와 effect site의 분포 평형 시간*. 이 분자 메커니즘이 turnover model의 *system flux* (mediator 합성/분해) 와 근본적으로 다르며, 단일 dose-range fit에서는 indistinguishable이지만 *광역 dose 또는 분자 사전 지식* 에서 구별된다.

이 위기는 NDA/IND 모델 선택 단계에서 가장 흔한 Deficiency Letter 사유 중 하나다. *모델이 잘 맞기 때문에 그 모델이 기전적으로 옳다* 는 추론은 무효다. 모델 선택은 (a) 더 광역의 dose-range에서 nonlinear $H(C)$ 거동 확인, (b) 효과 compartment 모델 fit에서 $EC_{50}$/$E_{max}$/$n$ 의 *dose 의존성* 검출, (c) 분자생물학적 사전 지식 — *biophase distribution* (effect compartment 적합) vs *mediator turnover* (IRM 적합) — 의 세 축으로만 정당화된다.

이 직관 — *fit quality = 모델의 정확성이 아니다, $k_{e0}$ 는 분포 시간이고 $k_{out}$ 은 mediator turnover이며, 데이터 설계 + 분자 사전 지식이 모델 식별을 결정한다* — 을 박고 다음 세션으로 넘어가라.

[⚡ Apex Concept]

#### A. Formal Definition

**Discrimination Crisis**: Turnover model (G Eq 3:91 형태) 과 effect compartment / link model (R&T Eq 8 in Fig 8-13 framework) 이 *동일 단일 dose-range 데이터*에 대해 통계적으로 구분되지 않는 정도(Δ AIC ≤ 2, Δ WRSS < 1%)로 거의 동일한 fit을 제공하는 현상. 특히 약물 함수가 *선형* 일 때 더 심각.

**R&T Effect Compartment Mechanism (Stage 2 통합)**: Effect compartment는 *plasma와 site of action 사이의 분포 평형* 을 표현하는 가상 compartment. $k_{e0}$ = 분포 rate constant. Plasma 농도 $C$ 가 effect-site 농도 $C_e$ 와 평형되는 데 걸리는 시간 = $\ln 2 / k_{e0}$. Naproxen에서 약 4-5 hr.

#### B. Derivation / Code Structure

**Effect compartment (link) model**:

$$\frac{dC_e}{dt} = k_{e0} \cdot C - k_{e0} \cdot C_e \quad \text{[Sheiner et al, R&T Fig 8-13]}$$

$$R = E_0 + \frac{E_{max} \cdot C_e^n}{EC_{50}^n + C_e^n} \quad \text{(linear case: } R = E_0 + a \cdot C_e\text{)}$$

**Turnover model 3 (linear $S(C)$ on $k_{in}$)**:

$$\frac{dR}{dt} = k_{in} \cdot (1 + a \cdot C) - k_{out} \cdot R$$

$$R_{ss} = R_0 \cdot (1 + a \cdot C_{ss})$$

**구조 동형 분석**: 두 모델 모두

1. 1차 ODE 시스템
2. 시간 상수 1개 ($k_{e0}$ 또는 $k_{out}$)
3. baseline + linear concentration term
4. 단일 dose에서 R-t 곡선이 동일한 일반 형태

PD6 데이터 fit 결과:

| 모델 | 시간 상수 | linear gain | baseline |
|------|---------|------|------|
| Turnover (Model 3 linear) | $k_{out}$ = 5.6 h⁻¹ | $a$ (via $k_{in}$, $EC_{50}$) | $k_{in}/k_{out}$ = 42.0 |
| Effect compartment | $k_{e0}$ = 5.6 h⁻¹ | $a$ = 0.026 | $E_0$ = 42.0 |

> 📎 [Micro-citation] PD6 final estimates 동일 [출처: Gabrielsson 5e, Ch.6 PD6 Table 6.1, p.763]
> 📎 [Micro-citation] R&T Effect compartment scheme [출처: Rowland & Tozer 5e, Ch.8, Fig 8-13, p.245]

**Naproxen 임상 시연 (R&T Stage 2 통합, Fig 8-2 → Fig 8-14, p.234-235, 246)**:

```
[Phase A: Hysteresis 관측 (Fig 8-2)]
Naproxen 500 mg oral.
Dental pain model에서 unbound plasma 농도 vs mean pain relief 1-8 hr sampling.
점들이 counterclockwise loop 형성 — 같은 plasma 농도에서 상승기 vs 하강기
반응값 다름.

[Phase B: Effect compartment fitting (Fig 8-14)]
$k_{e0}$ adjustment를 통해 hysteresis 사라지는 조건 탐색.
Effect-site 농도 $C_e$ vs response를 plot하면 단일 sigmoid 곡선으로 collapse.
$k_{e0}$ ≈ 0.15-0.20 hr⁻¹ → 분포 t1/2 ≈ 4-5 hr.

[해석 — 분자 메커니즘]
Naproxen이 dental tissue (synovium, inflamed tissue)에 도달하는 데 plasma와의
분포 평형이 4-5 hr 걸림. 이것이 hysteresis의 *분자 원인*.
*Mediator turnover가 아니다* — pain mediator (prostaglandins) 자체의 turnover는
훨씬 빠름. 약물 분포 시간이 rate-limiting step.

[Card 8과의 연결]
Naproxen은 PK rate-limited PD (Card 8). Effect compartment 모델이 적합.
Turnover model은 *기전적으로 부적합* — pain mediator turnover는 시간 척도 mismatch.
```

**Time-to-peak 동일**: 두 모델 모두 $k_{e0}$ 또는 $k_{out}$ 에 의해서만 peak time 결정. dose 변화에 따른 peak shift 없음 (linear $S(C)$).

**WRSS 비교 (PD6)**: Turnover 15516 vs Effect compartment 15518 — 0.01% 차이.

#### C. Structural Necessity

**왜 indistinguishable인가?**

선형 시스템의 입출력 관계는 transfer function으로 표현되며, 두 모델의 transfer function은:

- Turnover linear: $\frac{R(s)}{C(s)} = \frac{R_0 \cdot a}{s/k_{out} + 1}$ (Laplace domain, single pole at $-k_{out}$)
- Effect compartment linear: $\frac{R(s)}{C(s)} = \frac{a}{s/k_{e0} + 1}$ (single pole at $-k_{e0}$)

두 transfer function은 시간 상수만 같으면 ($k_{out} = k_{e0}$) 단일 입력에 대해 동일한 출력을 생성. **선형 시스템 식별은 입력의 다양성(dose-range, repeated dosing, dose-rate change)에 의해서만 깨진다.**

**R&T 분자 framing 추가**: 두 모델은 *수학적으로 같은 transfer function* 이지만 *분자적으로 다른 인과 가설* 임:

- Turnover: drug 작용 → mediator 합성/분해 변화 → response 변화 (system이 시간 척도)
- Effect compartment: drug 분포 → effect-site 농도 평형 → 즉각 receptor binding → response (drug이 시간 척도)

이 차이는 (a) 분자생물학적 사전 지식 (mediator의 알려진 turnover 시간), (b) 광역 dose에서의 거동 차이로만 노출됨.

#### C-2. Plausible Fallacy ⚡ — 이 세션의 Apex Concept Plausible Fallacy

**그럴싸한 오류**: "두 모델이 단일 dose-range 데이터에 똑같이 잘 맞으면, parsimony 원칙에 따라 더 단순한 effect compartment 모델 (turnover 모델보다 system parameter $k_{in}$, $k_{out}$ 분리 안 됨, free parameter 1개 적음)을 채택한다."

**이 오류의 NONMEM 피팅 / 임상 예측 나비효과**:

1. **Effect compartment 모델로 dose-range 확장 시뮬레이션**: 광역 dose에서 *biologically implausible*한 dose-dependent $EC_{50}$, $E_{max}$, $n$ 추정값 발생. *같은 약물의 같은 환자군에서 dose에 따라 $EC_{50}$ 가 변한다* — 분자약리학적으로 불가능.

2. **반복 dose 또는 광역 dose-range에서 fit 실패**: 단일 dose에서 보이지 않던 peak-shift가 등장. Turnover model은 자연스럽게 적응, effect compartment 모델은 잔차 systematic bias 생성.

3. **R&T 분자 framing의 추가 위험**: Effect compartment 모델은 *biophase distribution* 가정을 함의 — 즉 약물이 site of action에 도달하는 분포 시간이 rate-limiting. 만약 실제 메커니즘이 *mediator turnover* (예: 만성 약물의 endogenous biomarker 변화) 라면, $k_{e0}$ 추정값을 *분포 시간* 으로 해석하여 dosing interval을 결정하면 *PD recovery 시간을 underestimate* — 약물 끊은 후 효과 지속 시간을 과소평가하여 *withdrawal rebound effect* 를 예측 못 함.

4. **NDA Deficiency Letter 사유**: "The applicant has not demonstrated that the chosen pharmacodynamic model structure (effect compartment) is mechanistically supported. The dose-dependent estimates of $EC_{50}$ across the studied dose range (presented in Table X) are inconsistent with the model's structural assumption of dose-invariant pharmacodynamic parameters. The molecular characteristics of the response variable [biomarker name] suggest endogenous turnover; a turnover model with explicit system parameters ($k_{in}$, $k_{out}$) should be evaluated with peak-shift analysis across the studied dose range."

**GOF 시그니처 패턴 — "Linear-Compatibility Mask"**:

이 패턴의 이름은 *Linear-Compatibility Mask* — 선형 모델 영역에서 발생하는 fit 동등성이 비선형/광역 영역에서 가짜였음이 드러나는 진단 시그니처:

- 단일 dose-range에서 잔차 random, AIC 차이 < 2
- 광역 dose-range 또는 반복 dose에서 effect compartment 모델의 $EC_{50}$ 가 dose마다 다른 값으로 추정됨 (turnover model은 일관)
- dose-EC50 산점도에서 effect compartment estimates가 systematic trend 보임
- 분자 사전 지식과 mismatch ($k_{e0}$ → 분포 시간으로 해석되어야 하나 endogenous biomarker turnover와 inconsistent)

#### D. Assumptions & Boundary Conditions

- 선형 $S(C) = 1 + aC$ 또는 작은 dose-range에서 Hill curve linear 영역.
- 단일 측정 endpoint.
- $k_{e0}$ 와 $k_{out}$ 가 우연히 비슷한 크기 (서로 1 order magnitude 이상 다르면 구분 가능).

#### E. Limitations

- **모든** turnover model이 effect compartment와 indistinguishable한 것은 아니다. Models 2, 4 ($k_{out}$ 작용)는 dose-dependent tss를 보이므로 단일 dose-range에서도 effect compartment와 구분 가능. 위기는 주로 Models 1, 3 ($k_{in}$ 작용) + linear $S(C)$ 조합.
- 비선형 PK + 비선형 PD 결합 시 추가 식별 정보 가능.
- **R&T 분자 framing의 한계**: Mediator turnover와 biophase distribution이 *같은 시간 척도* 일 때 (drug과 mediator 모두 4-5 hr 정도) 분자 사전 지식만으로도 구별 어려움.

**Indirect Link 일반 framing (R&T 통합)**: 이 세션의 모든 모델 — turnover, effect compartment, target consumption — 이 R&T의 *indirect link* 범주에 포함. *Direct link* (Card 1 CONTEXT의 midazolam 사례)는 hysteresis 없음 + Cmax-효과 동시 peak. PD6의 Apex Concept은 indirect link 내부의 *어느 메커니즘인가* 의 식별 위기.

#### F. Five Cognitive Layers

| Layer | 내용 |
|-------|------|
| **L1** | 두 모델의 transfer function 동일성, single-pole linear system, $k_{out} = k_{e0}$, $\Delta$AIC < 2; R&T effect compartment ODE (Eq in Fig 8-13) |
| **L2** | R-t 곡선 overlay: 두 모델 예측 거의 완전 중첩; 잔차 plot도 동형; concentration-effect plane의 hysteresis loop는 두 모델 모두 효과적으로 제거 가능 |
| **L3** | 선형 시스템 식별 이론 (system identification): 입력 풍부도 (input richness) 가 모델 식별 결정 |
| **L4** | 분포 평형 (effect compartment, R&T biophase framing) vs 합성-분해 turnover (생물학적 turnover) — 외형은 같으나 인과 메커니즘이 다름; 분자 사전 지식이 모델 선택의 근거 (naproxen → tissue distribution → effect compartment 적합; warfarin → clotting factor synthesis → turnover 적합) |
| **L5** | NDA Briefing Document의 모델 선택 정당화 섹션, peak-shift analysis figure, dose-EC50 산점도, 광역 dose-range 시뮬레이션 결과를 reviewer evidence로 제시; *분자 메커니즘 서술* 을 통한 모델 family 사전 선택 |

#### G. Zettelkasten Atom

```yaml
---
aliases: [Discrimination crisis, Turnover-link indistinguishability, PD6 finding, Linear-Compatibility Mask, Effect compartment biophase]
tags: [pharmacometrics/pkpd, model-selection, regulatory-risk, apex-concept]
up: "[[Card2-FourModelTaxonomy]]"
related: ["[[Card3-tssDiscrimination]]", "[[Card8-RateLimiting]]", "[[EffectCompartment-ke0]]", "[[NDA-ModelJustification]]", "[[Peletier-2005]]", "[[RnT-NaproxenHysteresis]]"]
source: "Gabrielsson & Weiner 5e, Ch.3 §3.7.5 + §3.9.7 + PD6 Table 6.1, p.252-253, 763 + Rowland & Tozer 5e, Ch.8, Fig 8-13, p.245-246, Fig 8-14, Fig 8-2"
---
```

선형 $S(C)$ + 단일 dose-range 데이터에서 turnover 모델과 effect compartment 모델은 통계적으로 구분 불가능 (PD6 WRSS 15516 vs 15518, $k_{out} = k_{e0} = 5.6$ h⁻¹). 두 모델이 동일 transfer function을 갖기 때문. R&T 분자 framing: effect compartment는 *biophase distribution* (drug → site), turnover는 *mediator system flux* (system → response). Naproxen (Fig 8-14)은 effect compartment 적합 (tissue distribution rate-limited). Plausible fallacy: parsimony로 effect compartment 채택 → 광역 dose에서 dose-dependent $EC_{50}$ → NDA Deficiency. GOF 시그니처: "Linear-Compatibility Mask". 모델 선택은 dose-range 확장 + peak-shift analysis + 분자 사전 지식 3축으로만 정당화. 모든 indirect link 모델 (turnover/effect comp/target consumption)이 같은 외형이나 분자 인과가 다름.

---

### ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### Card 8 — PK vs PD Rate-Limited Decline of Response **★ R&T NEW**
### ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<!-- MASTER LENS -->
#### [개념 Big Idea: 거장의 시각]

모든 PK/PD 시스템에는 **두 개의 시계가 동시에 돌고 있다** — 약물 자체의 PK 시계 ($t_{1/2}$ of drug elimination)와 반응 시스템의 PD 시계 (turnover time of mediator, lifetime of platelet, regeneration time of receptor). 임상에서 관찰되는 *효과의 시간 경과* 는 두 시계 중 **느린 쪽에 의해 rate-limited** 된다 — 이것이 R&T Ch.8 의 핵심 framing이며, 이전의 turnover model 분류(Cards 1–7) 위에 얹어지는 *시간 척도 분석* 의 마스터 키.

이 framing 없이 임상 데이터를 보면, succinylcholine (PK-limited, $t_{1/2}^{drug}$ 4 min, 효과 종료 12 min)과 acenocoumarol (PD-limited, drug $t_{1/2}$ 15 hr, 효과 회복 3일)이 *왜 다른 시간 척도로 작용하는지* 가설 없이 단순 "약효 지속시간 차이"로만 보인다. 두 시계 framing이 도입되는 순간:

- Succinylcholine: PK 시계 (4 min) ≪ PD 시계 (neuronal conduction, 즉각) → **PK-limited** → dose 두 배 → 효과 +1 PK $t_{1/2}$ → $t_D$ 공식 (Card 9) 적용 가능.
- Phenprocoumon: PK 시계 (5 days) ≫ PD 시계 (clotting factor turnover, 1–2 days) → **PK-limited** → drug 끊은 후에도 2주간 효과 지속.
- Acenocoumarol: PK 시계 (15 hr) ≪ PD 시계 (clotting factor turnover, 1–2 days) → **PD-limited** → drug 빠르게 사라지나 효과 회복은 system flux 의 함수.
- Aspirin: PK 시계 (15 min) ≪ PD 시계 (platelet lifetime, 7–10 days) → **PD-limited** (target consumption) → 거의 100배 시간 척도 격차 (R&T Fig 8-20).

이 직관 — *임상 효과 시간을 모델링하기 전에 두 시계 중 어느 쪽이 느린지부터 묻는다* — 을 박고 모든 사례를 해석하라. 이 한 번의 분기 판단이 Card 9의 $t_D$ 공식 적용 여부, NONMEM 모델 구조 선택, dose-duration regimen design 까지 결정한다.

> 📎 [Micro-citation] 두 시계 framing의 명시적 진술 [출처: Rowland & Tozer 5e, Ch.8, p.243: "the return of the measured response to the baseline can be rate-limited by either the pharmacokinetics of the drug or the underlying dynamics of the affected system, whichever is the slowest"]

#### A. Formal Definition

**PK rate-limited decline**: 약물의 PK 시계 ($t_{1/2}^{drug}$)가 PD 시스템의 시계 (turnover time, target regeneration time, mediator lifetime)보다 느려서, 효과 감소 속도가 약물 농도 감소 속도에 의해 결정되는 상황. R-t 곡선이 C-t 곡선의 *지연된 영상* 으로 거동.

**PD rate-limited decline**: PD 시계가 PK 시계보다 느려서, 약물이 사라진 후에도 효과 회복 속도가 PD 시스템의 자체 동역학 (mediator turnover, target resynthesis, downstream cascade)에 의해 결정되는 상황. R-t 곡선이 C-t 곡선과 시간 척도가 *근본적으로 다름*.

#### B. Derivation / Code Structure — 비교 분석

**핵심 진단 절차 (R&T Fig 8-11 framework)**:

```
[Step 1] 약물 PK $t_{1/2}$ 측정 (또는 문헌)
[Step 2] PD 시스템의 turnover time / target regeneration time 측정 또는 문헌:
   - mediator: clotting factors 1–2 days, prothrombin complex 시간 척도
   - target: receptor resynthesis (omeprazole proton pump → days)
   - cells: platelet lifetime 7–10 days, leukocyte 14–21 days
   - functional: heat dissipation min, neuronal conduction sec
[Step 3] 두 시계 비교:
   - PK $t_{1/2}$ ≫ PD turnover → PK rate-limited → 효과 회복 = PK 함수
   - PK $t_{1/2}$ ≪ PD turnover → PD rate-limited → 효과 회복 = system 함수
   - PK $t_{1/2}$ ≈ PD turnover → 결합 (둘 다 영향)
[Step 4] 모델 선택:
   - PK-limited → 단순 link 또는 effect compartment 모델 충분; $t_D$ 공식 (Card 9) 적용
   - PD-limited → turnover model 또는 target consumption model 필수; $t_D$ 공식 적용 불가
```

**임상 사례 4종 비교 (R&T anchored, Fig 8-11, 8-20, 8-18, 8-19)**:

| 약물 | PK $t_{1/2}$ | PD 시계 | Rate-limiting | R-t 거동 | 모델 선택 |
|------|---------|---------|----------|---------|----------|
| Succinylcholine 0.5 mg/kg iv | 3.5 min | neuronal (즉각) | **PK** | $t_D$ ∝ ln(Dose) (Fig 8-24) | direct link, $k_e$ 사용 가능, $t_D$ 공식 적용 |
| Minoxidil 25 mg oral | ~4 hr | hemodynamic (min) | **PK** | linear decline 100 hr (Fig 8-19) | direct link |
| Phenprocoumon 0.6 mg/kg | 5 days | clotting (1–2 days) | **PK** (drug 더 느림) | 효과 회복 ~2주 (Fig 8-11B) | turnover Model 1 + slow PK |
| Acenocoumarol 10 mg | 15 hr | clotting (1–2 days) | **PD** | 효과 회복 ~3일 (Fig 8-11B) | turnover Model 1 |
| Aspirin 650 mg | 15 min | platelet (7–10 days) | **PD** (target consumption) | 효과 ~1주 (Fig 8-20) | irreversible target consumption (Card 6 family) |
| Omeprazole 40 mg | < 1 hr | proton pump regeneration (days) | **PD** | 효과 ~3일 (Fig 8-21) | irreversible + slow off-rate |
| Paclitaxel iv | 50 hr | leukocyte regeneration (3 weeks) | **PD** | nadir + 3-week recovery (Fig 8-22) | turnover with downstream cell kinetics |

> 📎 [Micro-citation] Acenocoumarol vs phenprocoumon dichotomy [출처: Rowland & Tozer 5e, Ch.8, Fig 8-11A,B, p.243]
> 📎 [Micro-citation] Aspirin PK-PD time scale disparity (~100-fold) [출처: Rowland & Tozer 5e, Ch.8, Fig 8-20A,B caption: "Note the almost 100-fold difference in the time scales", p.251]

**Acenocoumarol vs phenprocoumon — 동일 메커니즘, 반대 rate-limiting (R&T Apex 사례)**:

두 약물 모두 동일한 분자 메커니즘 (vitamin K reductase 억제 → prothrombin complex 합성 차단, Card 1의 warfarin과 같은 family)으로 작용한다. 그럼에도 *효과의 시간 거동* 이 정반대인 것은:

- Acenocoumarol: drug $t_{1/2}$ 15 hr ≪ clotting factor turnover (1–2 days). Drug이 빠르게 사라지나 *시스템이 시간 척도를 가짐* → 회복은 system flux의 함수 → 3일.
- Phenprocoumon: drug $t_{1/2}$ 5 days ≫ clotting factor turnover. Drug이 천천히 사라지므로 *drug이 시간 척도를 가짐* → 회복은 drug PK의 함수 → 2주.

이것이 *두 시계 framing의 가장 정밀한 임상 시연* — 동일 메커니즘 + 동일 dose 정당화 + 다른 PK = 다른 rate-limiting = 다른 임상 시간 척도. NONMEM 모델 구조도 사실상 동일 (Model 1 turnover) 이지만, 유효 파라미터 식별성이 다르다 (acenocoumarol에서는 $k_t$ 식별 가능, phenprocoumon에서는 $k_t$ 와 PK $k$ 가 confound 위험).

**Propranolol — PK-limited의 표준 사례 (R&T Ch.2 Fig 2-16 reference)**:

R&T Ch.2 propranolol 사례 (오랫동안 측정된 PK-PD 곡선)에서 β-blockade는 *plasma concentration과 거의 동시* 거동 — biophase distribution이 매우 빠름 ($k_{e0}$ ≫ $k$) + receptor 결합도 빠름 + downstream cascade도 빠름. Triazolam ($t_{1/2}$ 3 hr, ultra short-acting hypnotic)부터 flurazepam ($t_{1/2}$ 2+ days, long-acting hypnotic)까지의 benzodiazepine spectrum도 동일 메커니즘 + 다른 PK → PK가 그대로 효과 시간을 결정.

#### C. Structural Necessity

**왜 *느린 쪽이 rate-limit* 인가?**

직렬 시스템에서 두 시간 상수 $\tau_1$ (PK), $\tau_2$ (PD) 가 있을 때, 출력 (response)의 시간 거동은 *큰 시간 상수가 dominant*. 수학적으로:

$$\frac{dR}{dt} = f(C(t), R)$$

$C(t) = C_0 e^{-k \cdot t}$ 일 때, $R(t)$ 의 long-term 거동은:
- $1/k \gg 1/k_{out}$ (PK 더 느림): $R$의 long-term decay는 $e^{-k \cdot t}$ 로 결정 → PK-limited
- $1/k \ll 1/k_{out}$ (PD 더 느림): $C \to 0$ 이후에도 $R$ 은 $e^{-k_{out} \cdot t}$ 로 천천히 감쇠 → PD-limited

이것은 Laplace 영역에서 두 1차 시스템의 직렬 연결의 dominant pole 분석과 동일. *공학적 원리 (slowest stage governs)* 가 PK/PD에 그대로 적용된다.

**Target consumption (Card 6 family)의 특수성**:

Aspirin/omeprazole의 PD-limited 거동은 단순 mediator turnover가 아니라 **약물이 receptor를 비가역적으로 소진** 하는 구조 — 이 경우 PD 시계는 "receptor 재합성 시간" + "cell turnover 시간"의 합성. Drug PK의 영향은 *AUC가 cumulative damage를 결정* 하는 한도까지 (Eq 3:111 family) 이며, 그 이후의 회복은 *drug 부재 상태에서의 system flux* 단독 → **receptor consumption은 PD-limited의 가장 극단적 형태** (PK 시계가 무관해지는 영역).

#### D. Assumptions & Boundary Conditions

| 가정 | 의미 | 위반 시 |
|-----|------|--------|
| 두 시간 상수 분리 가능 | $\tau_1, \tau_2$ 가 단일 dominant pole 갖는 1차 시스템 | 다중 PK 구획 또는 다중 PD 구획 → 다중 rate-limiting 영역 |
| Drug action site 고정 | drug이 시스템의 특정 손잡이 (Card 1)에만 작용 | feedback loop (§2.6.7 moderator) 시 system 자체가 변화 |
| Linear PK | drug $t_{1/2}$ dose-independent | nonlinear PK (Michaelis-Menten elimination) → dose-dependent rate-limiting 전환 가능 |
| $C_{ss}$ 또는 단순 IV bolus | input이 pulse 또는 step | 복잡한 input 패턴 (oral + accumulation)은 분리 분석 후 superposition |

#### E. Limitations

- **두 시계가 비슷한 크기** ($\tau_1 \approx \tau_2$, 1 order of magnitude 이내): 명확한 rate-limiting 단정 불가 — *결합 dynamics* 분석 필요. 이 경우 Card 7의 effect compartment vs turnover discrimination이 정확히 발생하는 영역.
- **다중 mediator 또는 cascade**: paclitaxel 사례 — drug → bone marrow precursor (mitotic phase) → mature leukocyte (3 weeks) — PD 시계가 단일 값이 아니라 *distribution* 형태. 단일 turnover model로는 표현 불가, transit compartment 또는 lifespan model 필요.
- **Tolerance / feedback (§3.9)**: PD 시스템이 drug 노출에 따라 *적응* 하면 PD 시계가 *시간 가변* — 이 경우 Card 8 분석은 *short-term* 에만 유효.

#### F. Five Cognitive Layers

| Layer | 내용 |
|-------|------|
| **L1** | 두 시계 framing: $\tau_{PK} = 1/k$, $\tau_{PD} = 1/k_{out}$ (또는 cell turnover 등); slowest dominates; R&T Eq 8-5 (rate of change = input − loss) 가 일반 formulation |
| **L2** | C-t와 R-t 곡선을 동일 시간축에 overlay → 두 곡선의 *시간 척도 비율* 시각화. Acenocoumarol vs phenprocoumon Fig 8-11 — 같은 약리학, 다른 rate-limiting의 시각적 시연. Aspirin Fig 8-20 — ~100배 시간 척도 격차의 직접 노출 |
| **L3** | 직렬 시간 시스템의 dominant pole 분석 (control theory), bottleneck 원리 (operations research에서의 슬로 stage governs throughput) |
| **L4** | drug elimination (PK)와 mediator turnover/target regeneration/cell lifespan (PD)이라는 두 개의 인과 시간 척도가 *별도로* 존재함을 분자생물학적으로 명시 |
| **L5** | 임상 dose 정당화 시 "효과 지속 시간이 PK $t_{1/2}$ 에 의존하는가, PD turnover에 의존하는가" 를 *최초 분석 단계* 에 결정. 이 결정이 dosing interval 선택, accumulation 예측, drug-drug interaction 영향 평가의 출발점. NDA Briefing Document에서 "the rate-limiting step for effect decline is [PK/PD], based on [evidence]" 를 명시적으로 진술 |

#### G. Zettelkasten Atom

```yaml
---
aliases: [PK rate-limited response, PD rate-limited response, Two-clock framing, Slowest-stage dominance, R&T rate-limiting]
tags: [pharmacometrics/pkpd, rate-limiting, time-scale, model-structure]
up: "[[Card1-TurnoverFoundation]]"
related: ["[[Card3-tssDiscrimination]]", "[[Card7-DiscriminationCrisis]]", "[[Card9-DurationFormula]]", "[[Card6-TargetConsumption]]", "[[RnT-AcenocoumarolPhenprocoumon]]", "[[RnT-Aspirin]]"]
source: "Rowland & Tozer 5e, Ch.8, p.236-243, Fig 8-11, 8-20, 8-21, 8-22, 8-18, 8-19"
---
```

PK/PD 시스템에는 두 개의 시계 — drug $t_{1/2}$ (PK 시계)와 mediator turnover/target regeneration (PD 시계) — 가 동시에 작동하며, 효과의 시간 거동은 *느린 쪽에 의해 rate-limited* 된다. R&T Apex 사례: 동일 메커니즘 (vitamin K reductase 억제) acenocoumarol vs phenprocoumon이 다른 rate-limiting (PD-limited 3일 vs PK-limited 2주)을 보임. PK-limited (succinylcholine, minoxidil) → $t_D$ 공식 (Card 9) 적용; PD-limited (warfarin slow recovery, aspirin target consumption, paclitaxel cell turnover) → turnover model 또는 target consumption 필수. Card 9 ($t_D$ formula)와 Card 3 (tss) 모두 PK rate-limiting 전제가 충족될 때만 적용 가능. NDA 모델 선택 정당화의 *최초* 분석 단계.

---

### ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### Card 9 — Duration of Effect & Dose-Log Linearity **★ R&T NEW**
### ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<!-- MASTER LENS -->
#### [개념 Big Idea: 거장의 시각]

PK rate-limited 약물에서 **dose를 두 배로 올리면 효과 지속시간이 정확히 한 PK $t_{1/2}$ 만큼 늘어난다**. 이것은 임상적 추측이 아니라 *수학적 필연성* — 1차 PK + Hill curve의 Region 2 (20–80% maximal response, log-linear concentration-response) 에서 자동으로 도출되는 결과다. R&T Eq 8-12:

$$t_D = \frac{1}{k}\ln\left(\frac{Dose}{C_{min} \cdot V}\right)$$

이 한 줄의 공식이 두 가지 임상적으로 결정적인 양을 *graphical 추출* 가능하게 한다: (1) *log-dose vs duration* plot의 slope = $1/k$ → drug effective half-life; (2) y-intercept (zero duration) = $\ln(C_{min} \cdot V) = \ln A_{min}$ → minimum effective amount in body. **농도 측정 없이도** dose 단계와 효과 종료 시간 관측만으로 PK 파라미터와 임상 임계값을 동시 추출.

이 framing 없이 임상에서 dose escalation을 하면 "dose 두 배 → 효과 두 배"라는 직관적 (그러나 *완전히 잘못된*) 가정에 빠진다. 실제로는 **dose 두 배 → 효과 +1 PK $t_{1/2}$ 만큼만 길어지고, 효과 *강도* 는 Region 3 plateau에 갇혀 거의 변하지 않는다** (Region 3에서 80–100% 사이의 변화는 dose에 거의 무감각). Methylprednisolone 16–1000 mg lymphocyte 반응 (R&T Fig 8-27)이 이 함정의 가장 명확한 시연 — 500 mg vs 1000 mg에서 반응 거의 동일. Dose linearity in PK ≠ dose linearity in PD.

이 직관 — *dose 두 배 = +1 half-life of duration, NOT 2× intensity* — 을 박고 모든 dose-regimen 결정을 내려라. 이 한 번의 framework가 위험한 dose escalation을 차단하고 modified-release (Chapter 10 forward link) 의 정량적 정당화 근거를 제공한다.

#### A. Formal Definition

**Duration of effect ($t_D$)**: 단일 IV bolus dose 후 plasma concentration이 *minimum effective concentration* ($C_{min}$) 으로 떨어질 때까지의 시간.

**Dose-log linearity** (R&T Eq 8-12): 1차 PK + 단일 구획 + Hill curve Region 2 (20–80% maximum)에서 효과 지속시간이 *dose의 logarithm에 선형 비례*. Slope = 1/k, intercept = $\ln(C_{min} \cdot V)$.

#### B. Derivation / Code Structure

**Eq 8-12 의 도출 (R&T 공식 유도)**:

1차 PK + 단일 구획: $C(t) = (Dose/V) \cdot e^{-k \cdot t}$ (Eq 8-10).

지속시간 종료 시점 ($t = t_D$)에서 $C = C_{min}$:

$$C_{min} = \frac{Dose}{V} \cdot e^{-k \cdot t_D} \quad \text{[Eq 8-11]}$$

양변 ln 후 $t_D$ 에 대해 정리:

$$\boxed{t_D = \frac{1}{k}\ln\left(\frac{Dose}{C_{min} \cdot V}\right) = \frac{1}{k}\ln\left(\frac{Dose}{A_{min}}\right) \quad \text{[Eq 8-12]}}$$

여기서 $A_{min} = C_{min} \cdot V$ = body 내 최소 유효 약물량.

**"Doubling dose adds 1 half-life" 의 구조적 증명**:

Dose가 $D_0$ 일 때 지속시간 $t_D$. Dose를 $2 D_0$ 로 올리면, body 내 약물량이 1 half-life 동안 $2 D_0 \to D_0$ 로 감소. 이 시점부터의 잔여 dynamic이 원래 $D_0$ 의 시작과 동일 → 추가 지속시간 = $t_D$. 따라서 총 지속시간 = $t_{1/2} + t_D$. **Dose 두 배 = 추가 +1 half-life** (Fig 8-23A의 평행선들이 1 $t_{1/2}$ 간격으로 분리).

> 📎 [Micro-citation] Eq 8-12 + dose-doubling logic [출처: Rowland & Tozer 5e, Ch.8, p.254-255]

**Succinylcholine T50 vs log(dose) 임상 검증 (Fig 8-24, 0.1–10 mg/kg)**:

$T_{50}$ (recovery to 50% twitch) vs $\ln(Dose)$ 가 직선 → slope $1/k$ 추출:

- 관측: 0.5, 1, 2, 4 mg/kg에서 T50 = 6, 10, 14, 18 min (대략 4 min 등간격)
- Slope = 4 min per doubling → $1/k = 4 / \ln 2 \approx 5.77$ min → $k \approx 0.17$ min⁻¹
- R&T 보고값: $k = 0.2$ min⁻¹, $t_{1/2} \approx 4$ min (체내 site-of-action에서의 effective half-life)

이 분석은 **plasma succinylcholine 농도 측정 없이** 단순 dose-T50 관계만으로 PK 파라미터 추출 — Card 5의 graphical 4 규칙의 5번째 규칙으로 추가 (PK rate-limited 약물에서만).

> 📎 [Micro-citation] Succinylcholine T50 vs log(dose) [출처: Rowland & Tozer 5e, Ch.8, Fig 8-24, p.256]

**Hill curve의 3 Region 거동 (Fig 8-17)**:

| Region | Response 범위 | C 단계 | Time-effect 거동 |
|--------|--------|------|---------|
| **Region 1** | 0–20% max | $C \ll C_{50}$ | $E \propto C$ (linear); response가 PK와 *평행 감쇠* (log-linear) |
| **Region 2** | 20–80% max | $C \approx C_{50}$ | $E \propto \ln C$ (log-linear); response가 *시간에 대해 선형 감쇠* (Eq 8-9: $E = E(0) - m \cdot k \cdot t$) |
| **Region 3** | 80–100% max | $C \gg C_{50}$ | $E$ 거의 일정 (saturated); 큰 dose 변화에도 effect 변화 미미 |

**Region 2의 zero-order decline (Eq 8-9)** 이 *직관에 반하는 핵심 관찰*: log-linear 영역에서는 dC가 dt에 대해 1차 감쇠임에도 *효과는 시간에 대해 0차 감쇠*. R&T dexamphetamine 사례 (Fig 8-7): 0차 감쇠가 직접 시연. 임상 monitoring에서 *반응 직선 감쇠 → 1차 PK + Region 2 작동* 을 시각으로 식별 가능.

> 📎 [Micro-citation] Region 1/2/3 + Eq 8-9 [출처: Rowland & Tozer 5e, Ch.8, Fig 8-17, p.249]

**임상 적용 — Region 2의 zero-order rate (Eq 8-9 분석)**:

$E(t) = E(0) - m \cdot k \cdot t$ 에서 $m$ = response per ln(C) (Region 2에서의 slope), $k$ = PK first-order constant.

R&T propranolol 사례 (Ch.2 Fig 2-16, R&T Ch.8 reference): $m = 11.5\%$ per $\ln C$, $k$ = 0.18 hr⁻¹ ($t_{1/2}$ 4 hr) → effect declines at $11.5\% \cdot 0.18 = 2.07\%$/hr in Region 2.

**Plausible Fallacy: "Dose linearity in PK = dose linearity in PD"** (R&T direct excerpt):

R&T p.256: "Dose linearity in pharmacokinetics does not result in dose linearity in pharmacodynamics. One common misconception in pharmacodynamics is the erroneous assumption that drugs with linear, dose-proportional pharmacokinetics also display dose-proportional pharmacodynamics. That is almost never the case."

Methylprednisolone 16–1000 mg 사례 (Fig 8-25, 8-26, 8-27): plasma AUC는 dose에 정확히 비례 (PK linear), 그러나 lymphocyte response는 500 mg과 1000 mg에서 거의 구분 불가능. *Region 3 saturation* 이 dose-doubling을 무력화한 것. 이 함정은 high-dose corticosteroid regimen design에서 흔한 over-dosing 사유.

#### C. Structural Necessity

**왜 정확히 ln(Dose)에 선형인가?**

1차 PK는 농도가 시간의 *지수함수* 로 감쇠 → ln(C)가 시간의 *선형 함수* → "$C = C_{min}$ 에 도달하는 시간" 이 ln(Dose/$A_{min}$) 의 선형 함수. 이 관계는 *1차 PK의 수학적 귀결* 이지 약물의 화학적 성질이 아니다 — 어떤 약물이든 1차 PK + 단일 구획 + Region 2 거동이면 *반드시* 이 관계가 성립.

**Region 2의 0차 감쇠는 왜 발생하는가?**

Region 2에서 $E = m \ln C + b$ → $dE/dt = m \cdot d(\ln C)/dt = m \cdot (-k)$ (1차 PK이므로 $d(\ln C)/dt = -k$) → 시간 미분이 *상수*. 즉 effect의 시간 감쇠율이 농도와 무관 → 0차. 이것이 *log-linear E-vs-C* 와 *exponential C-vs-t* 의 합성에서 나오는 *수학적 강제*.

#### D. Assumptions & Boundary Conditions

| 가정 | 의미 | 위반 시 |
|-----|------|--------|
| 1차 PK + 단일 구획 | $C = (Dose/V) e^{-kt}$ | 다구획 → effective $k$ 가 시간 가변 (initial rapid distribution + slow elimination) |
| Hill curve Region 2 | 20–80% maximal effect | Region 1 (response ∝ C) 또는 Region 3 (saturated)로 빠지면 공식 부정확 |
| **PK rate-limited (Card 8 전제)** | 효과가 농도를 즉시 추적 | PD-limited 시 (aspirin, paclitaxel) Eq 8-12 적용 불가 — 효과는 PD turnover로 결정 |
| Single IV bolus | $C_0 = Dose/V$ 즉시 도달 | Oral 또는 infusion → $C_{max}$ 가 *peak time* 에 도달, $t_D$ 정의가 약간 변형 |
| 단일 활성 약물 | 활성 metabolite 없음 | 활성 metabolite 시 effective duration이 길어짐 — apparent $k$ 가 metabolite 형성/소실로 결정 |

#### E. Limitations

- **PD-limited 약물 적용 불가**: aspirin (PD-limited, target consumption) 의 효과 지속은 platelet lifespan에 의해 결정 — Eq 8-12 형태 비유효. Aspirin dose escalation 시 1주 효과가 *2주로 늘어나지 않는다* (target turnover로 결정).
- **Toxicity ceiling**: dose 4배 → 지속 +2 $t_{1/2}$ 를 위해 *initial Cmax도 4배* — 좁은 therapeutic window 약물 (succinylcholine, digoxin)에서 toxicity 위험. R&T 명시적 권고 (p.255-256): "raising dose to extend duration of effect is not without risks... an alternative and safer approach may well be to prolong the input of drug, producing a flatter exposure-time profile" (즉 modified-release 또는 infusion → Chapter 10 forward link).
- **재투여 간격 결정에 직접 사용 불가**: $t_D$ 는 *single dose* 후의 지속 — multiple dose 시 accumulation, tolerance, fluctuation 등 추가 고려 필요 (Chapter 11 forward link).

#### F. Five Cognitive Layers

| Layer | 내용 |
|-------|------|
| **L1** | $t_D = (1/k) \ln(Dose / A_{min})$, slope = 1/k, intercept = $\ln A_{min}$, doubling dose adds 1 $t_{1/2}$, Region 1/2/3 표; Eq 8-9 zero-order decline of effect |
| **L2** | Fig 8-17 dual-panel: PK 1차 감쇠 (지수곡선) + E-vs-time 직선 감쇠 (Region 2 평탄선분); Fig 8-23 dose-duration 평행선들 (1 $t_{1/2}$ 간격); Fig 8-24 succinylcholine straight-line in semi-log |
| **L3** | log-linear region에서 1차 PK가 effect를 *0차*로 변환하는 수학적 강제; bottleneck pole 분석의 응용 |
| **L4** | drug 분자 자체의 시간 척도가 그대로 임상 효과 시간에 투영되는 *PK-limited 약물의 직접성*; Region 1/2/3은 receptor occupancy의 nonlinear sensitivity 영역들 |
| **L5** | dose escalation 결정 시 "intensity 증대 vs duration 연장 vs toxicity 위험"의 trade-off 정량 분석; modified-release formulation (chapter 10) 정당화의 근거; *농도 측정 없이* dose-duration 데이터로 PK 파라미터 추출 (안과 / 흡입제 등 국소 투여); FDA bioequivalence 평가 시 IR vs MR formulation 비교 분석 |

#### G. Zettelkasten Atom

```yaml
---
aliases: [Duration of effect, Dose-log linearity, Eq 8-12, Region 2 zero-order decline, Doubling-dose-half-life rule]
tags: [pharmacometrics/pkpd, duration, dose-response, PK-limited]
up: "[[Card8-RateLimiting]]"
related: ["[[Card3-tssDiscrimination]]", "[[Card5-GraphicalEstimation]]", "[[Card1-TurnoverFoundation]]", "[[ModifiedRelease-Ch10]]", "[[BioequivalenceAssessment]]"]
source: "Rowland & Tozer 5e, Ch.8, Eq 8-12, p.254-256, Fig 8-17, 8-23, 8-24, 8-27"
---
```

PK rate-limited 약물 (1차 PK + Hill Region 2)에서 효과 지속시간 $t_D = (1/k)\ln(Dose/A_{min})$ — log-dose vs duration plot의 slope = $1/k$ (effective half-life), intercept = $\ln A_{min}$. **Doubling dose adds exactly 1 $t_{1/2}$ to duration** (수학적 필연). 농도 측정 없이 PK 파라미터 추출 가능 (succinylcholine T50 vs log(dose), Fig 8-24). Region 2에서 effect는 시간에 대해 *0차 감쇠* (Eq 8-9, dexamphetamine Fig 8-7). 핵심 함정: dose linearity in PK ≠ dose linearity in PD (methylprednisolone 16–1000 mg, Fig 8-27 — Region 3 saturation으로 high dose에서 effect 거의 무차이). Card 8의 PK-limited 전제 위반 시 적용 불가 (aspirin, paclitaxel은 PD-limited으로 별도 framing).

<!-- RECAP -->
**§2 종결 흐름 요약**: Card 1 (foundation ODE) → Card 2 (4-model taxonomy) → Card 3 (tss로 부위 식별, **PK-limited 전제 필요**) → Card 4 ($E_{max}$ 의미 차이) → Card 5 (graphical 4 규칙 + R&T blocking dose) → Card 6 (irreversible + target consumption) → Card 7 (모델 선택 위기, Apex) → **Card 8 (두 시계 framing — 모든 시간 척도 분석의 마스터 키)** → **Card 9 ($t_D$ 공식 — PK-limited 약물의 임상 정량 도구)**. Cards 1–7이 *공간 구조* (작용 부위, 모델 선택)를 다뤘다면, Cards 8–9는 *시간 척도* (rate-limiting, duration)를 다룬다. 두 축이 결합될 때 비로소 임상 PK/PD 분석이 완전해진다 — 어느 손잡이를 비트는가 (1–7) + 어느 시계가 느린가 (8–9). NDA 모델 선택 정당화는 항상 두 축에서 동시에 답해야 한다.

---

## §5 — Confusion Pair Dissection

이 세션에서 진정으로 혼동 가능한 5쌍을 식별 (Stage 1의 4 pair + Stage 2 신규 1 pair). 각 쌍의 §5 dissection은 *왜 헷갈리는가* + *수식·구조 차이* + *변화 방향* + *임상/모델링 결과 차이* + *⚡기억 고리(구조 인코딩)* 의 6 차원 표.

---

<!-- CONFUSION -->
### §5-1. Model 1 vs Model 2 (Inhibition 작용 부위)

| 비교 차원 | Model 1 (Inhibit $k_{in}$) | Model 2 (Inhibit $k_{out}$) |
|---|---|---|
| **표면적 유사성** | 둘 다 inhibitory action, 둘 다 $I(C)$ 함수 사용. Phase 1 데이터에서 baseline 변화만 보면 구별 불가. | (좌측과 동일) |
| **수식/코드 형태** | $\frac{dR}{dt} = k_{in} \cdot I(C) - k_{out} R$ | $\frac{dR}{dt} = k_{in} - k_{out} R \cdot I(C)$ |
| **생리학적/구조적 지시체** | 합성효소 / 전구체 / 분비 기구 차단 (warfarin → vit K reductase, PD4; R&T Fig 8-10/8-15에서 prothrombin complex synthesis block) | 분해효소 / 청소 경로 차단 (furosemide → tubule reabsorption, PD5; ranitidine → gastric H+ secretion, R&T Fig 8-8) |
| **변화 방향** | dose↑ → $R_{ss}$↓, **tss 동일** ($k_{out}$ 단독), $\Delta R = R_0 \cdot I_{max}$, return slope $-k_{out}$. R&T 시연: warfarin 0.75/1.5/3.0 mg/kg에서 36hr complex activity 거의 동일 (Fig 8-15B) — *blocking dose 검증* | dose↑ → $R_{ss}$↑, **tss 길어짐** ($k_{out}(1-I_{max})$로 감소), $\Delta R = R_0 \cdot \frac{I_{max}}{1-I_{max}}$, return slope $-k_{out}$ |
| **임상/모델링 결과** | Model 1을 Model 2로 오인 → tss를 dose 의존으로 잘못 expect → sampling design 잘못 (불필요하게 늦은 시점 sampling) → 효율성 손실 + 비용 낭비. R&T 임상 적용: warfarin dose escalation 시 *time-to-maximum* 일정 → time-window 안정 → 임상 모니터링 protocol 단순화. | Model 2를 Model 1로 오인 → high-dose에서 비현실적 long-tail 예측 실패 → toxicity prediction underestimation → Phase 2 dose escalation safety 사고. |
| **⚡ 기억 고리** | "Inhibition 1 vs 2의 차이는 *수도꼭지를 잠그느냐, 배수구를 막느냐*. 수도꼭지(in)는 잠가도 배수구(out)는 그대로 → 물 빠지는 속도(반감기) 동일 → R&T blocking dose 시연 (Fig 8-15B): synthesis 완전 차단해도 prothrombin complex *반감기*는 dose-invariant. 배수구(out)를 막으면 *물 빠지는 속도 자체가 느려져* → 새 수위에 도달하는 시간이 dose마다 달라진다. tss 거동은 *어느 변수가 손실 항의 R 계수에 곱해지는가* 의 수학적 귀결이지 약물 화학의 우연이 아니다." | (좌측과 동일) |

---

<!-- CONFUSION -->
### §5-2. $I_{max}$ vs $\Delta R$ vs Direct $E_{max}$ (Fig 3.40 Semantic Collision)

| 비교 차원 | $I_{max}$ (or $E_{max}$) in $H(C)$ | $\Delta R$ in turnover model | $E_{max}$ in direct model |
|---|---|---|---|
| **표면적 유사성** | 모두 약물의 "최대 효과"라 부름. 같은 기호 $E_{max}$ 가 셋 다 사용. 단위까지 비슷해 보임. | (좌측과 동일) | (좌측과 동일) |
| **수식/코드 형태** | $H(C) = 1 + \frac{E_{max} C^n}{EC_{50}^n + C^n}$ → $E_{max}$ = drug-specific multiplier (dimensionless) | $\Delta R = R_0 \cdot E_{max}$ (Model 3) 또는 $R_0 \cdot \frac{E_{max}}{1+E_{max}}$ (Model 4) — *response 단위* | $E = E_0 + \frac{E_{max} C^n}{EC_{50}^n + C^n}$ → $E_{max}$ = $R_{max} - E_0$, 절대 *response 단위* |
| **생리학적/구조적 지시체** | 약물 고유 파라미터 (intrinsic efficacy) | 약물 + 시스템 ($R_0$) 의 합성 product | 약물 고유 파라미터지만 절대 단위, system $E_0$ 부재 가정 |
| **변화 방향** | $I_{max} \le 1$ 강제, $E_{max}$ 무한대까지 가능. baseline에 무관. | baseline ($R_0$)에 비례. baseline이 0이면 $\Delta R$ 도 0. | baseline 부재 (또는 알려진 상수). |
| **임상/모델링 결과** | $E_{max}$ 값을 *in vitro*-*in vivo* 외삽 시 그대로 사용 가능. | $\Delta R$ 값을 모델 간에 옮기면 baseline 배수만큼 오차. | direct 모델에서 추정된 $E_{max}$ 를 turnover 모델에 옮기면 의미 자체 다름. R&T methylprednisolone 사례: 16–1000 mg 광역 dose에서 lymphocyte response가 Region 3 saturation으로 dose-doubling 무력화 — *$E_{max}$ 의미 분리 없으면 dose escalation 함정* (Fig 8-27). |
| **⚡ 기억 고리** | "$E_{max}$ 는 모델마다 *다른 동물* 이다. 직접 모델의 $E_{max}$ 는 자(尺)의 길이 (물리량의 차이). 간접 모델의 $E_{max}$ 는 배율 (배수적 곱셈인자). 자를 들고 배율 계산기에 넣으면 단위가 일치하지 않는다 — 하지만 같은 기호이기 때문에 sanity check 없이 통과한다. **항상 $\Delta R/R_0$ 비율로 환원해서 비교하라** — 그 비율만이 모델 간 의미가 보존된다. R&T methylprednisolone Fig 8-27가 이 함정의 임상적 종결: PK가 dose-linear 임에도 PD response가 비선형 — Region 3 plateau가 *baseline-relative scale* 에서만 보인다." | (좌측과 동일) | (좌측과 동일) |

---

<!-- CONFUSION -->
### §5-3. Reversible $H(C) \cdot k_{out}$ vs Irreversible $K \cdot C$ (Drug-Zero Limit)

| 비교 차원 | Reversible (e.g., Model 4 stimulation of loss) | Irreversible (second-order kill / target consumption) |
|---|---|---|
| **표면적 유사성** | 둘 다 dose↑ → R↓. 둘 다 약물 농도와 R의 곱 형태 항을 가짐. Drug 작용 phase에서 R-t 곡선 모양 유사. | (좌측과 동일) |
| **수식/코드 형태** | $\frac{dR}{dt} = k_{in} - k_{out} R \cdot S(C)$, drug=0에서 $\frac{dR}{dt} = k_{in} - k_{out} R$ (정상 turnover) | $\frac{dR}{dt} = -K \cdot C \cdot R$, drug=0에서 $\frac{dR}{dt} = 0$ (정지). R&T target consumption: $\frac{dR_{active}}{dt} = -k_{on} \cdot C \cdot R_{active} + k_{syn} - k_{deg} R_{active}$ (Card 6 family) |
| **생리학적/구조적 지시체** | drug 부재 시 mediator의 자체 turnover (생산-분해 균형) 작동. 약물은 그 균형의 분해 손잡이를 *촉진*. | drug 부재 시 살상은 0. 약물이 *존재해야만* 살상 작용. R&T 사례: aspirin (cyclooxygenase covalent inactivation, Fig 8-20), omeprazole (proton pump covalent + slow off-rate, Fig 8-21). |
| **변화 방향** | drug withdrawal 후 반응이 baseline ($R_0$)으로 *복귀*. AUC만으로 효과 결정 안 됨 (시간 분포 영향). | drug withdrawal 후에도 살상된 세포/inactivated receptor는 *영구히 사라짐*. AUC가 효과 직접 결정 ($S_F = e^{-K \cdot AUC}$). R&T aspirin: drug $t_{1/2}$ 15 min, effect $\sim$1주 (~100배 시간 척도 격차, Fig 8-20). |
| **임상/모델링 결과** | 만성 투여 중단 후 baseline 회복. 항생제 효과는 표현 불가 (drug=0에서 살상 멈추므로 자가 성장 회복). | 항생제 살상은 영구. 그러나 *살아남은 세포*는 logistic 성장으로 회복 ($k_g \cdot N(1 - N/B_{max})$). AUC/MIC 또는 fAUC₂₄/MIC가 임상 PK/PD target. R&T target consumption family: target turnover (platelet 7–10 days, proton pump days)가 PD 시계를 결정 — Card 8의 PD-limited 표준 사례. |
| **⚡ 기억 고리** | "Reversible은 *수영장 가에서 펌프를 끄는 것* — 끄면 물이 다시 차오른다 (baseline 회복). Irreversible은 *유리잔을 깨는 것* — 깨진 조각은 다시 모이지 않는다 (영구 손실, AUC가 모든 것). 두 시스템에서 같은 $-k \cdot R$ 항이 등장하지만, *drug=0에서 그 항이 살아있느냐 죽느냐* 가 모델 family를 가르는 기준이다. R&T 임상 시연: aspirin Fig 8-20 — drug 사라진지 1주가 지나도 platelet 효과 80% 잔존. 한 줄의 차이가 항생제 가이드라인 + 항혈소판 dosing interval (매일 80 mg) + omeprazole 1일 1회 dosing 전체를 만든다." | (좌측과 동일) |

> ⚠️ [확인 필요] 본 pair에서 K 표기 충돌 명시: Reversible model의 $k_{out}$ (1차, 시간⁻¹) vs Irreversible model의 $K$ (2차, 농도⁻¹·시간⁻¹) vs PK 자체의 $K$ (1차 elimination, 시간⁻¹). Phase 2 audit 단계에서 별도 표기로 분리.

---

<!-- CONFUSION -->
### §5-4. Turnover Model vs Effect Compartment (Link) Model **★ Critical Blow**

| 비교 차원 | Turnover (간접) | Effect Compartment / Link (분포) |
|---|---|---|
| **표면적 유사성** | 둘 다 농도-반응 hysteresis 표현. 둘 다 시간 상수 1개. 둘 다 1차 ODE. **선형 영역에서 단일 dose-range fit이 거의 동일** (PD6: WRSS 15516 vs 15518). R&T Fig 8-13 framework: 두 모델 모두 hysteresis loop을 효과적으로 제거 가능. | (좌측과 동일) |
| **수식/코드 형태** | $\frac{dR}{dt} = k_{in} \cdot S(C) - k_{out} R$ | $\frac{dC_e}{dt} = k_{e0}(C - C_e)$, $R = E_0 + \frac{E_{max} C_e^n}{EC_{50}^n + C_e^n}$ |
| **생리학적/구조적 지시체** | 반응 변수의 *합성-분해 turnover* (mediator level, biomarker, functional response). $k_{in}$, $k_{out}$ 은 system parameters. R&T 임상 사례: warfarin (clotting factor turnover, Fig 8-10), ranitidine (gastric pH/H+ secretion turnover, Fig 8-8). | drug의 *biophase 분포* 평형 시간 (R&T Fig 8-13 explicit framing). $k_{e0}$ 은 분포 rate. drug-receptor 상호작용은 즉각. R&T 임상 사례: naproxen (Fig 8-2 hysteresis → Fig 8-14 effect compartment 적합), digoxin 1mg iv (Fig 8-1, ~6 hr distribution). |
| **변화 방향** | dose-EC50 광역에서 단일 분자 약리 파라미터 ($EC_{50}$, $E_{max}$, $n$) recover 가능. Models 2&4에서 dose-dependent peak-shift. | dose-EC50 광역에서 effect compartment $EC_{50}$ 추정값이 *dose마다 변함* (turnover-generated 데이터 fitting 시) — biologically implausible. |
| **임상/모델링 결과** | NONMEM 추정 시 system + drug 분리, IIV on $k_{out}$ (개체 차이가 system parameter), IIV on $EC_{50}$ (개체 차이가 drug-receptor sensitivity)로 명확히 분해. | $k_{e0}$ 은 mechanistic interpretation 어려움. effect compartment의 IIV는 mixed (분포 + receptor sensitivity 합쳐짐). R&T 분자 framing: $k_{e0}$ 는 *오직 distribution* 의미 — 만약 endogenous biomarker turnover라면 $k_{e0}$ 해석은 부적절. |
| **⚡ 기억 고리** | "두 모델은 같은 R-t 곡선을 *다른 인과 가설로* 설명한다. Turnover는 *반응 자체가 천천히 자라고 죽는다* — system이 시간 척도를 가진다 (R&T warfarin/ranitidine framing). Effect compartment는 *약물이 천천히 도달한다* — drug이 시간 척도를 가진다 (R&T naproxen/digoxin framing). 단일 dose 곡선은 누가 시간 척도를 갖느냐를 알려주지 않는다 — *광역 dose-range에서 비선형 거동* + *분자 사전 지식* (response variable이 endogenous turnover를 갖는가?) 만이 system vs drug의 차이를 드러낸다. 모델 선택은 fit quality가 아니라 *데이터 설계 + 광역 dose 거동 + 분자 사전 지식* 의 함수다." | (좌측과 동일) |
| **🔴 Critical Blow (NDA/IND 규제 파급력)** | 이 혼동을 NDA/IND 제출 시 강행 → Deficiency Letter: "Applicant has not demonstrated that the chosen pharmacodynamic model structure is mechanistically supported. The dose-dependent estimates of $EC_{50}$ across the studied dose range (Table X.X) are inconsistent with the assumption of dose-invariant pharmacodynamic parameters. **The molecular characteristics of the response variable suggest endogenous turnover (e.g., clotting factor, gastric pH); a turnover model with explicit system parameters ($k_{in}$, $k_{out}$) should be evaluated** with peak-shift analysis to discriminate between distribution-rate-limited (link) and turnover-driven mechanisms." → 3–6개월 review hold, 추가 modeling effort, 최악의 경우 *dose justification 자체 무효* → Phase 3 entry delay. PK/PD 컨설팅 비용 단독 USD 200K+ 발생 사례 보고됨. | (좌측과 동일) |

---

<!-- CONFUSION -->
### §5-5. PK Rate-Limited vs PD Rate-Limited Decline of Response **★ R&T NEW**

| 비교 차원 | PK Rate-Limited Decline | PD Rate-Limited Decline |
|---|---|---|
| **표면적 유사성** | 둘 다 IV bolus 후 효과가 시간에 따라 감쇠. 둘 다 R-t 곡선 형태가 1차 PK와 시각적으로 비슷할 수 있음 (특히 Region 1). 둘 다 임상에서 "약효 지속시간" 이라는 동일 개념으로 측정. **동일 분자 메커니즘 약물 사이에서도 PK 차이만으로 분기 가능** (acenocoumarol vs phenprocoumon, R&T Fig 8-11). | (좌측과 동일) |
| **수식/코드 형태** | 효과 감쇠율 = drug $k$ 에 의해 결정. Eq 8-9: $E = E(0) - m \cdot k \cdot t$ (Region 2). $t_D = (1/k)\ln(Dose/A_{min})$ (Eq 8-12). Direct link 또는 빠른 effect compartment 모델 적합. | 효과 감쇠율 = system $k_{out}$ (또는 cell turnover, target regeneration)에 의해 결정. Drug 사라진 후에도 *system 자체 동역학* 이 종결까지의 시간 결정. Turnover model 또는 target consumption model 필수. **Eq 8-12 $t_D$ 공식 비유효**. |
| **생리학적/구조적 지시체** | Drug 자체의 분자 시간 척도가 임상 효과 시간을 결정. R&T 사례: succinylcholine (drug $t_{1/2}$ 4 min ≪ neuronal conduction 즉각, Fig 8-18,8-24), minoxidil (drug $t_{1/2}$ 4 hr ≪ hemodynamic response, Fig 8-19), phenprocoumon (drug $t_{1/2}$ 5 days ≫ clotting factor turnover, Fig 8-11), propranolol (Ch.2 Fig 2-16). | System 자체의 시간 척도 (mediator turnover, target lifetime, cell regeneration)가 임상 효과 시간을 결정. R&T 사례: acenocoumarol (drug $t_{1/2}$ 15 hr ≪ clotting factor turnover 1–2 days, Fig 8-11A,B), aspirin (drug $t_{1/2}$ 15 min ≪ platelet lifespan 7–10 days, Fig 8-20 ~100배 격차), omeprazole (drug $t_{1/2}$ <1 hr ≪ proton pump regeneration days, Fig 8-21), paclitaxel (drug $t_{1/2}$ 50 hr ≪ leukocyte regeneration 3 weeks, Fig 8-22). |
| **변화 방향** | Dose 두 배 → 지속시간 +1 PK $t_{1/2}$ (수학적 강제, Eq 8-12). Drug accumulation, 신부전 (clearance ↓ → k ↓), drug-drug interaction이 효과 시간을 직접 변경. PK 변화가 PD 변화에 1:1 투영. | Dose 두 배 → 지속시간 변화가 *system saturation 정도와 turnover의 함수* (예측 어려움). 신부전 등 PK 변화가 *순간 효과 강도* 만 변경, *지속시간* 은 거의 영향 없음. **Drug의 PK는 PD 시간 척도와 분리된다.** |
| **임상/모델링 결과** | Phenprocoumon 신부전 환자 적용 시 — drug clearance ↓ → drug $t_{1/2}$ 더 길어짐 → 효과 회복 시간 4주+ 가능. Bleeding 위험 직접 증가. PK 모니터링이 효과 모니터링의 근사 대용. | Acenocoumarol 신부전 환자 적용 시 — drug clearance ↓ 가 약간의 PK 변화를 유발하나 효과 회복은 여전히 *clotting factor turnover* (1–2 days)에 결정 → 임상 회복 시간 거의 변화 없음. **PK 모니터링이 효과 모니터링의 근사 대용 안 됨**. Aspirin 신부전 환자 — drug PK 변화 무관, 항혈소판 효과는 *언제나* platelet lifespan으로 결정. |
| **⚡ 기억 고리** | "두 시계가 동시에 돈다 — drug PK 시계, system PD 시계. *느린 쪽이 임상 효과 지속시간을 결정*. 같은 메커니즘 약물이라도 PK 시계가 다르면 임상 거동이 정반대 — R&T Apex 사례 acenocoumarol vs phenprocoumon (Fig 8-11): 같은 vitamin K reductase 억제, drug $t_{1/2}$ 15 hr vs 5 days, 그래서 효과 회복 3일 vs 2주. **같은 *분자 약리* + 다른 *PK* = 다른 *rate-limiting* = 다른 *임상 시간 척도*.** 임상 dose escalation, 신부전 dose adjustment, drug-drug interaction 평가의 모든 결정이 이 분기에서 시작된다. *어느 시계가 느린가* 를 *최초* 분석 단계에 결정하라 — 그렇지 않으면 PK 데이터로 PD 시간 거동을 잘못 예측한다." | (좌측과 동일) |

> ⚠️ **Card 7과의 관계 명시**: PD-limited인 효과를 effect compartment 모델로 fit하면 (Card 7 Apex Concept) — 단일 dose-range에서 잘 맞을 수 있으나 광역 dose 또는 신부전 환자 등 *PK perturbation* 시 모델이 무너짐. PD-limited 약물은 turnover 또는 target consumption 모델로 가야 PK-PD 분리가 명확. 두 카드의 통합: §5-4가 *모델 구조* 의 분기, §5-5가 *시간 척도* 의 분기 — 모델 선택은 두 축 모두에서 결정.

---

## §7 — Self-Test: Active Recall Module

총 10 질문 (회상 3 / 적용 6 / Boss Dilemma 1). Stage 1의 Q1–Q7에 R&T 통합 질문 Q8–Q9 추가, Boss Dilemma는 Q10으로 이동 + R&T context 강화. 각 질문은 클릭형 정답 공개 + SR tag + 다음 깊이 질문 포함.

---

<!-- SELF-TEST -->
### Q1 [Recall, ★★] Model 1 ODE와 정상상태 도출

Model 1 (inhibition of production) 의 ODE를 쓰고, constant $C_{ss}$ 가정 하 정상상태에서 $R_{ss}$ 를 $R_0$ 와 $I(C_{ss})$ 로 표현하라.

**[정답 공개 ▾]**

$$\frac{dR}{dt} = k_{in} \cdot I(C) - k_{out} \cdot R$$

정상상태 ($\frac{dR}{dt} = 0$): $k_{in} \cdot I(C_{ss}) = k_{out} \cdot R_{ss}$ → $R_{ss} = R_0 \cdot I(C_{ss})$. $I(C_{ss}) = 1 - \frac{I_{max} C_{ss}^n}{IC_{50}^n + C_{ss}^n}$ 이므로 $R_{ss}$ 는 $R_0$ 의 단순 *축소된 비율*이다 ($\le R_0$).

> **다음 깊이 질문**: $I_{max} = 1$ (full inhibition) 이고 $C_{ss} \gg IC_{50}$ 에서 $R_{ss}$ 의 한계값은 무엇이며, 이때 응답 종결까지 걸리는 시간은? *(Hint: Card 3 + Card 8)*

---

<!-- SELF-TEST -->
### Q2 [Recall, ★★] tss-Based Discrimination

4 모델 중 dose-independent tss를 보이는 모델을 모두 골라라. 그 이유를 ODE의 *어느 항이 R에 비례하는가* 의 관점에서 한 문장으로 설명하라. 추가로, 이 진단이 *유효하기 위한 전제 조건* 을 한 문장으로 진술하라.

**[정답 공개 ▾]**

**Models 1 & 3** (inhibition / stimulation of $k_{in}$).

이유: 두 모델 모두에서 *R에 비례하는 항* 은 $k_{out} R$ 단독 → 시간 상수 ($\tau = 1/k_{out}$) 가 dose에 무관 → tss = 3-4 × $t_{1/2,k_{out}}$ 이 dose-independent. Models 2, 4는 손실 항이 $k_{out} R \cdot H(C)$ 이므로 effective $k_{out}$ 가 dose-dependent → tss-shift.

**전제 조건 (R&T Card 8 통합)**: PK가 PD보다 충분히 빠를 때 ($k \gg k_{out}$) tss 시그널이 PD 작용 부위를 직접 반영. PK rate-limiting 시 tss는 drug $t_{1/2}$ 에 묻혀 PD 작용 부위 식별 불가능.

> **다음 깊이 질문**: Acenocoumarol과 phenprocoumon은 같은 분자 메커니즘 (Model 1)인데, 둘 다 dose-independent tss를 보일까? 한 쪽이 PK rate-limited라면 어떻게 되는가? *(Hint: R&T Fig 8-11 + Card 8)*

---

<!-- SELF-TEST -->
### Q3 [Recall, ★] $E_{max}$ Semantics across Three Models

Fig 3.40의 세 모델 (직접 Emax, 재모수화 직접 Emax, turnover Model 3) 에서 $E_{max}$ 의 단위와 의미를 각각 한 줄로 쓰라.

**[정답 공개 ▾]**

| 모델 | $E_{max}$ 단위 | 의미 |
|------|--------|--------|
| 직접 Emax: $E = E_0 + \frac{E_{max} C^n}{EC_{50}^n + C^n}$ | response 단위 (예: bpm, mmHg) | $R_{max} - E_0$, 절대 거리 |
| 재모수화: $E = E_0 (1 + \frac{E_{max} C^n}{EC_{50}^n + C^n})$ | dimensionless | $E_0$ 의 배율, $E_{max} = 1$ 이면 응답이 baseline의 2배 |
| Turnover Model 3: $R_{ss} = R_0 (1 + \frac{E_{max} C^n}{EC_{50}^n + C^n})$ | dimensionless | $R_0 = k_{in}/k_{out}$ baseline의 배율, drug + system의 합성 효과 |

**모델 간 비교는 항상 $\Delta R / R_0$ 비율로 환산해서 수행하라.**

> **다음 깊이 질문**: R&T methylprednisolone Fig 8-27에서 500 mg vs 1000 mg lymphocyte response가 거의 동일한데, 이는 $E_{max}$ 의 어느 의미와 일관되는가? 그리고 이 임상 함정이 dose justification에 어떤 영향을 주는가?

---

<!-- SELF-TEST -->
### Q4 [Application, ★★] PD9 Zooparc® Initial Estimates

PD9의 Zooparc® 데이터에서 baseline ≈ 80 units, 첫 dose 후 0–8 h 구간 downswing 관측: $R(0) = 80$, $R(8) = 48$. 이 데이터로부터:

(a) $k_{out}$ 초기 추정값을 구하라.
(b) $k_{in}$ 초기 추정값을 구하라.
(c) Model 1을 가정한다면, $C_{ss}$ 가 0.25 µg/L에서 $R_{ss} \approx 40$ units 라는 정상상태 데이터로부터 $IC_{50}$ 추정값은? ($I_{max} = 1$, $n = 1$ 가정)

**[정답 공개 ▾]**

**(a)** $k_{out} = -\frac{\ln(48/80)}{8} \approx 0.064 \text{ h}^{-1}$ (PD9 보고값 0.06 h⁻¹과 일치).

**(b)** $k_{in} = R_0 \cdot k_{out} = 80 \cdot 0.064 \approx 5.1 \text{ units} \cdot \text{h}^{-1}$ (PD9 보고값 4.8과 근사).

**(c)** Model 1 정상상태: $R_{ss}/R_0 = 1 - C_{ss}/(IC_{50} + C_{ss})$ → $0.5 = IC_{50}/(IC_{50} + 0.25)$ → $IC_{50} = 0.25$ µg/L (PD9 보고값과 일치).

> **다음 깊이 질문**: 만약 위 데이터에서 baseline이 80이 아니라 시간에 따라 +0.5 units/h로 drift한다면 (예: disease progression), $k_{out}$ 초기 추정값은 어떻게 보정해야 하는가? *(Hint: §3.12 Eq 3:248–3:250)*

---

<!-- SELF-TEST -->
### Q5 [Application, ★] Peak-Shift Reading

임상시험 결과: 3개 dose level에서 PD response 곡선을 관측. Peak time이 각각 dose↑에 따라 $t_{peak,1} = 6h$ → $t_{peak,2} = 4h$ → $t_{peak,3} = 2.5h$ 로 *짧아짐*. 반응은 baseline 아래로 *하강*. 어느 모델이 가장 일관되며, 어느 모델은 즉각 배제되는가? 분자 메커니즘 가설을 한 문장으로 제시하라.

**[정답 공개 ▾]**

- 반응 *하강* → inhibit response: Models 1 (inhibit $k_{in}$) 또는 4 (stimulate $k_{out}$).
- Peak time이 *dose↑에서 짧아짐* → dose-dependent tss → **Model 4 (stimulate $k_{out}$)**.
- 즉각 배제: Model 1 (dose-independent tss). Models 2, 3 (반응 상승 모델)도 배제.

**분자 메커니즘 가설**: 약물이 *반응 변수의 분해/제거 경로를 자극* (예: 효소 유도, 청소 가속) → loss rate 증가 → 효과적 반감기 단축 → 새로운 (낮은) 정상상태에 더 빨리 도달.

PD7 CB1 inverse agonist (energy expenditure stimulation) 가 이 패턴의 정확한 임상 사례.

> **다음 깊이 질문**: 만약 반응이 *상승* + peak-shift가 *늘어남* 이라면 어느 모델? 왜 Model 3은 배제되는가?

---

<!-- SELF-TEST -->
### Q6 [Application, ★] PD4 Pool 1 Identifiability Crisis

PD4 warfarin 분석에서 Pool 1 모델 (precursor $P$ → response $R$, $P$ 에 약물 작용) 추정 시 $k_1$ (precursor exit rate) 와 $k_{out}$ (response loss rate) 의 상관계수가 0.9999로 보고됨. 두 파라미터가 모두 0.09 h⁻¹로 추정됨. 이 상황의 진단과 수정 방안을 제시하라.

**[정답 공개 ▾]**

**진단**: 두 파라미터가 *동일한 시간 상수* 를 capture하고 있어 *reduced-rank* 시스템. ODE 시스템 $\frac{dP}{dt} = k_{in} I(C) - k_1 P$, $\frac{dR}{dt} = k_1 P - k_{out} R$ 에서 $k_1 = k_{out}$ 이면 transit chain이 단일 시간 상수로 collapse → P와 R은 single-pole 거동을 *순차적으로 통과* 하는 한 시간 상수 시스템과 등가.

**수정 방안**: PD4 Pool 2 모델처럼 **$k_1 = k_{out}$ 강제** (Eq 4:13–4:14). $k_{out}$ 의 CV%가 lag-time model 수준으로 회복 (~7%). WRSS 거의 변화 없음, AIC 약간 감소.

**일반화**: NONMEM에서 *correlation matrix > 0.95* 인 두 파라미터는 사실상 1개 → 모델 reduction 또는 reparameterization 필수.

> **다음 깊이 질문**: 만약 $k_1$ 과 $k_{out}$ 이 진정으로 다른 시간 상수를 가졌다면, 식별 가능하게 하는 데이터 디자인은? *(Hint: precursor measurement 추가 또는 dose-rate 변경)*

---

<!-- SELF-TEST -->
### Q7 [Application, ★★] Manuscript Review Red Flags

당신은 *Clinical Pharmacology & Therapeutics* 에 투고된 원고를 리뷰 중이다. 저자는 effect compartment ($k_{e0}$) 모델을 *Imax-driven indirect response* 라 묘사된 반응 데이터에 적합시켰다. 모델은 단일 dose-range (4, 16, 64 mg) 데이터에 잘 맞는다 (WRSS 적합, 잔차 random). 어떤 red flag을 표제 / Methods / Results / Discussion 섹션에서 찾을 것인가?

**[정답 공개 ▾]**

**Methods 섹션**: (1) 모델 선택 정당화 부재 — "Imax-driven indirect response" 표현은 turnover 모델 시사하나 effect compartment 적용. (2) 비교 모델 평가 부재 — turnover Model 1 또는 2 함께 fit한 AIC/WRSS 비교? (3) Dose-range 정당화 부재 — 4–64 mg (16배)이 *광역* 인지 검토 부재.

**Results 섹션**: (4) Dose-by-dose parameter estimates 누락 — 각 dose level에서 $EC_{50}$, $E_{max}$, $n$ 분리 추정? *dose-dependent estimates* 존재 시 *biologically implausible* signal — 모델 misspecification 직접 증거. (5) Peak-shift figure 부재 — dose vs $t_{peak}$ 산점도 없으면 mechanistic discrimination 불가능.

**Discussion 섹션**: (6) **R&T 분자 framing mismatch** — $k_{e0}$ 를 *biophase distribution*으로 해석했는데 본문은 *receptor turnover* 또는 *biomarker production* 시사 → 모델-기전 mismatch. (7) **Card 8 framing 부재** — PK $t_{1/2}$ 와 PD turnover time 비교가 Methods에 없음 → rate-limiting step 미확인. (8) Repeated dose 데이터 부재 자명한 한계 인정 부재.

**리뷰 권고**: Major revision. 저자에게 turnover Models 1–4 fit 비교, peak-shift analysis, dose-by-dose $EC_{50}$ 안정성 검증, **PK vs PD rate-limiting 분석** 을 요구. Card 7 Apex Concept + Card 8 framing의 통합 회피 사례.

> **다음 깊이 질문**: 만약 저자가 "turnover model도 fit해봤지만 AIC가 비슷해 더 simple한 link model을 선택했다"고 답한다면 — 이 답변의 맹점은? *(Hint: Linear-Compatibility Mask + 분자 사전 지식)*

---

<!-- SELF-TEST -->
### Q8 [Application, ★★] R&T Hysteresis Classification — Digoxin vs Ibuprofen ★ R&T NEW

R&T Ch.8에서 두 가지 hysteresis 사례가 등장한다:
- **Digoxin 1 mg iv (Fig 8-1)**: 첫 4시간 동안 plasma concentration이 *감소* 하는 동안 left ventricular ejection-time index (효과)가 *증가*.
- **Ibuprofen 6 mg/kg oral (Fig 8-9A)**: 6세 미만~11세 febrile children에서 plasma concentration이 *상승* 하는 초기에 effect (체온 강하)가 *지연* 되어 시작.

(a) 각각의 hysteresis가 clockwise인지 counterclockwise인지 분류하라.
(b) 각각의 분자/생리학적 메커니즘 가설을 한 문장으로 제시하라.
(c) 두 사례 중 어느 쪽이 *effect compartment 모델* 로 적합 가능하며, 어느 쪽이 *turnover 모델* 이 더 적합한가?

**[정답 공개 ▾]**

**(a) 분류**:
- **Digoxin**: IV bolus 후 농도는 감소만, 효과는 증가만. concentration-effect plane에서 점들이 *low-C/high-E* 영역에서 *high-C/low-E* 영역으로 이동하지 않고, *high-C/low-E → low-C/high-E* 로 이동. 시간 진행 방향: **counterclockwise** (R&T 일반 분류). 단 IV bolus의 monotonic 감소이므로 *strict loop* 가 아닌 단일 곡선.
- **Ibuprofen**: oral 흡수 phase에서 concentration이 rise하나 effect는 *지연* (low effect at high concentration), 이후 absorption-elimination peak에서 effect가 maximum, 이후 effect가 천천히 감소. concentration-effect plane에서 시간 진행 방향이 **counterclockwise** (R&T Fig 8-9A의 화살표 직접 표시).

**(b) 메커니즘 가설**:
- **Digoxin**: 약물이 *심장 조직에 분포* + *Na+/K+ ATPase에 결합* 까지 ~6 hr 소요 — *biophase distribution rate-limited*. Effect compartment 메커니즘 (R&T 명시: "distribution of digoxin into cardiac tissue with subsequent binding to the target receptor is slow", p.234).
- **Ibuprofen**: 약물이 *brain heat-control mechanism 에 작용* 하여 heat production 감소 → body heat *dissipation* 시간이 system flux 시간 척도 (Eq 8-4) — *system flux rate-limited*. Brain entry는 빠르지만 (highly perfused organ), 측정 변수 (rectal temperature)가 *system in flux*.

**(c) 모델 선택**:
- **Digoxin**: distribution rate-limited → **effect compartment** ($k_{e0}$) 모델 적합. R&T 명시 (Fig 8-13 framework).
- **Ibuprofen**: system flux rate-limited (heat dissipation) → **turnover model** 적합. R&T 직접 진술 (p.242, Eq 8-4 framework).

**Card 7과의 연결**: 두 사례 모두 단일 dose 데이터에서는 fit이 비슷할 수 있으나, *분자 사전 지식* (digoxin → distribution, ibuprofen → system flux)이 모델 family 사전 선택의 근거. 광역 dose 또는 dose-EC50 분석에서 각 모델의 안정성이 검증.

> **다음 깊이 질문**: Naproxen 500 mg oral (R&T Fig 8-2) 사례는 어느 family에 속하는가? Effect compartment 적합으로 hysteresis가 제거되는 (Fig 8-14) 사실이 분자 framing에 무엇을 시사하는가?

---

<!-- SELF-TEST -->
### Q9 [Application, ★★] $t_D$ Formula — Succinylcholine Calculation ★ R&T NEW

R&T Eq 8-12: $t_D = (1/k)\ln(Dose/A_{min})$. Succinylcholine 데이터 (R&T Fig 8-24):

| Dose (mg/kg) | T50 (min) |
|----|----|
| 0.5 | 6 |
| 1.0 | 10 |
| 2.0 | 14 |
| 4.0 | 18 |

(a) $1/k$ 와 $k$ (effective half-life의 역수)를 dose-doubling rule에서 추출하라.
(b) Succinylcholine의 effective $t_{1/2}$ 를 계산하라.
(c) $A_{min}$ (최소 유효 body 내 약물량)을 추출하라 (단, $V$ = 0.4 L/kg 로 가정, 70 kg 환자).
(d) **만약 환자가 신부전 (clearance 50% 감소)** 라면 동일 dose 0.5 mg/kg에서 T50은 어떻게 변하는가? (PK rate-limited 약물 가정 — Card 8 framing 적용)
(e) 만약 약물이 *PD-limited* (예: aspirin like target consumption) 였다면 T50의 dose-dependence 패턴은 어떻게 달라지는가?

**[정답 공개 ▾]**

**(a)** Dose 두 배 → T50 +4 min (예: 0.5→1.0 mg/kg에서 6→10 min, 1.0→2.0에서 10→14 min). $\Delta t_D = t_{1/2}^{eff}$ → **$t_{1/2}^{eff}$ = 4 min** → $k = \ln 2 / 4 = 0.173$ min⁻¹ ≈ 0.17 min⁻¹ ($1/k \approx 5.77$ min). R&T 보고값: $k = 0.2$ min⁻¹ (slope-based 추정).

**(b)** $t_{1/2}^{eff}$ = 4 min (Card 9 dose-doubling rule).

**(c)** Eq 8-12 사용, dose 0.5 mg/kg = 35 mg total, $V \cdot$ weight = 0.4 × 70 = 28 L:

$t_D = 6$ min, $k = 0.173$ → $\ln(Dose/A_{min}) = k \cdot t_D = 0.173 \cdot 6 = 1.04$ → $Dose/A_{min} = e^{1.04} = 2.83$ → $A_{min} = 35 / 2.83 = 12.4$ mg ≈ **12 mg in body**, $C_{min} = A_{min}/V = 12.4/28 \approx 0.44$ mg/L.

**(d) 신부전 PK perturbation**: clearance 50% ↓ → $k$ 50% ↓ ($k = 0.087$ min⁻¹) → $t_{1/2}^{eff}$ = 8 min (두 배).

새 $t_D = (1/0.087) \cdot \ln(35/12.4) = 11.5 \cdot 1.04 = 12$ min (원래 6 min의 *두 배*).

**핵심 함의**: PK rate-limited 약물에서 신부전은 효과 *지속시간* 을 직접 늘림 (toxicity 위험 증가). Succinylcholine은 plasma cholinesterase에 의해 hydrolysis되므로 신부전 영향 제한적이나, 다른 PK-limited 약물 (예: nondepolarizing neuromuscular blocker) 에서는 dose adjustment 필수.

**(e) PD-limited 시 변경**: dose 두 배 → T50 변화가 *system turnover* 의 saturation 정도에 의해 결정 → log-linear 관계 *깨짐*. Aspirin-like 약물이라면 dose-doubling이 platelet inhibition *지속시간* 을 두 배로 늘리지 *않음* — platelet lifespan (7–10 days)이 천장. T50 vs log(Dose) plot이 *plateau* 에 도달하는 영역 출현.

> **다음 깊이 질문**: 0.1 mg/kg dose에서 T50을 예측하라. Region 1 (effect < 20% max)에 진입한다면 Eq 8-12 적용 가능한가?

---

<!-- SELF-TEST -->
### Q10 [Application, ★★] **Boss Dilemma — Socratic Dilemma** ⚡ (R&T 강화)

당신은 FDA Division of Pharmacometrics의 senior reviewer다. 한 항우울제 NDA 신청서가 도착했다 — 단일 dose-range (5, 15, 45 mg PO) Phase 2 데이터에 대해 Sponsor가 effect compartment 모델 (linear $E$ vs $C_e$)을 채택했다. WRSS 245, $k_{e0}$ = 0.11 h⁻¹, $a$ = 0.026. Sponsor의 정당화: "turnover Model 1 fit도 했으나 AIC 차이 1.5로 link 모델이 simpler."

**추가 R&T 정보 (Sponsor가 제출한 Background section)**:
- Drug PK $t_{1/2}$ = 18 hr.
- 측정 endpoint = serotonin transporter occupancy biomarker (PET imaging proxy)
- 분자 메커니즘 = SERT 가역 결합 (rapid on/off, $K_D$ ~10 nM)
- Sponsor 주장: "SERT occupancy는 즉각 PD endpoint이며, plasma → brain biophase distribution이 rate-limiting"

당신 팀의 다른 reviewer (junior)는 "AIC가 비슷하면 parsimony에 따라 link 모델 채택, 그대로 통과시키자"고 제안한다. 그러나 동시에 임상팀은 *Phase 3에서 dose를 90 mg까지 escalate 예정* 이라 보고했고, 추가로 *신부전 환자 (CrCl 30–50 mL/min) 를 포함할 계획* 이다.

**Trade-off**: 추가 modeling 요구 → review timeline 3–6개월 지연 → competitor 시장 진입 risk. 단순 통과 → Phase 3에서 모델 fit 실패 시 dose justification 무효 → Phase 3 일부 재실행 + 신부전 환자에서 unexpected effect prolongation 위험.

**당신은 review action을 어떻게 결정하며, R&T Card 7 + Card 8 framing을 어떻게 적용하는가?**

**[정답 공개 ▾]**

이 질문의 핵심은 *fit quality에 의존한 모델 선택* (Card 7) + *PK vs PD rate-limiting 사전 분석* (Card 8) 의 위험을 *광역 dose-range entry + 신부전 환자 포함 직전* 에 어떻게 처리하는가이다.

**Senior reviewer로서의 결정**: **Information Request (IR) 발송**. 다음을 30일 내 제출 요구:

1. **Card 7 분석 — Peak-shift + dose-by-dose**:
   - 3 dose level에서 $t_{peak}$ plot (peak-shift 유무).
   - 각 dose level에서 분리 추정한 $EC_{50}$, $a$, $n$ — dose-dependent shift 검증.

2. **Card 8 분석 — 두 시계 비교**:
   - **PK 시계**: drug $t_{1/2}$ = 18 hr (PK 비교적 느림).
   - **PD 시계**: SERT occupancy *kinetics* — receptor on/off (~min), 그러나 *behavioral / clinical effect* (depression score)는 **weeks to months** (well-established neurobiology).
   - **Sponsor가 제출한 endpoint** (SERT occupancy biomarker)는 *직접 PD* 일 수 있으나, *clinical efficacy* (Phase 3 endpoint)와의 연결이 명시되지 않음 → **biomarker가 turnover system의 어느 layer를 측정하는가** 가 핵심.
   - 만약 SERT occupancy가 *진짜 직접 PD* 라면 effect compartment 적합 (drug → brain distribution rate-limited).
   - 만약 occupancy가 *upstream marker* 이고 clinical effect가 *downstream cascade* (synaptic adaptation, neurogenesis 등 weeks 스케일)이라면 — *biomarker-clinical disconnect* 가 발생하며 Phase 3 효능 예측 부정확.

3. **신부전 환자 PK perturbation 분석 (Card 8 차원 추가)**:
   - 신부전에서 drug clearance ↓ → drug $t_{1/2}$ ↑ → 만약 *PK rate-limited* 라면 효과 시간 직접 변경 (R&T phenprocoumon 사례 framing).
   - 만약 *PD rate-limited* (clinical effect는 system turnover로 결정) 라면 신부전 효과 prolongation은 *biomarker*에서만 관찰되고 임상 효과는 변화 없을 수 있음 (R&T acenocoumarol vs phenprocoumon 분기 framing).
   - **Sponsor는 두 시계 framing에서 신부전 영향을 사전 예측해야** 한다.

4. **Mechanistic justification**:
   - SERT 가역 결합 + rapid on/off → biomarker 자체는 effect compartment 그럴듯.
   - 그러나 *clinical depression endpoint* 는 turnover-driven (synaptic plasticity 시간 척도). → **biomarker 모델과 clinical 모델이 다른 family**.

**Briefing Document 표현 (regulatory language, R&T 강화)**:

> "While the effect compartment model provides adequate fit to the studied dose range (WRSS 245), the Sponsor has not adequately justified (a) the choice of pharmacodynamic model structure or (b) the rate-limiting step for the measured response. Specifically, the Agency requests:
>
> (1) **Peak-shift analysis** across the three studied dose levels, with dose-by-dose parameter estimation to assess dose-dependence of $EC_{50}$ and slope.
>
> (2) **Mechanistic identification of the rate-limiting step**: Sponsor should explicitly compare the drug PK half-life (18 hr) with the turnover characteristics of the affected pharmacodynamic system. The chosen biomarker (SERT occupancy) reflects rapid receptor binding kinetics, but the clinical efficacy endpoint of major depressive disorder is well-established to be driven by downstream synaptic adaptations operating on a weeks-to-months time scale. The Sponsor should provide a structural model that bridges the biomarker (occupancy) with the clinical endpoint (depression score), and identify whether the rate-limiting step for clinical efficacy is the drug pharmacokinetics, the SERT occupancy turnover, or downstream system turnover.
>
> (3) **Renal impairment forward simulation**: Using both the effect compartment model and a turnover Model 1 alternative, simulate biomarker and clinical effect profiles in CrCl 30–50 mL/min subjects. The Agency expects the Sponsor to demonstrate that the chosen model produces biologically plausible and consistent predictions in this subpopulation, and that the rate-limiting step framework (PK-limited vs PD-limited) is explicitly stated and supported.
>
> (4) **Phase 3 dose extrapolation**: Side-by-side simulation of $R_{ss}$ at 90 mg using both the effect compartment and turnover Model 1, with explicit discussion of which model is more robust under the proposed dose escalation.
>
> Pending receipt of these analyses, the dose justification for Phase 3 cannot be evaluated."

**핵심 통찰 (R&T Card 7 + Card 8 통합)**:

*AIC 차이 < 2가 모델 동등성을 의미하지 않는다 — 단지 현재 데이터 영역에서 통계적으로 구분 불가능을 의미한다 (Card 7 Linear-Compatibility Mask)*. 추가로, *biomarker와 clinical endpoint가 다른 시간 척도를 가질 때, 단일 모델 family로 둘을 동시에 표현할 수 없다 (Card 8 두 시계 framing)*. 광역 dose-range로 이동 + 신부전 환자 포함이 동시에 발생하는 순간 두 시계 분석이 절대적으로 필요해진다.

> **다음 깊이 질문**: 만약 Sponsor의 30일 IR 응답에서 SERT occupancy가 plasma drug concentration과 *동시 peak* (no hysteresis at occupancy level)이지만 clinical depression score는 *2–4주 지연* 으로 나타난다면 — 어떤 모델 구조를 권고하며, 그 근거는 R&T Card 8 framing에서 어떻게 도출되는가? *(Hint: cascade model with two distinct time scales, biomarker-driven dosing rationale)*


---

## §8 — Meta-Frame & Big Picture (Stage 1 + Stage 2 통합본)

<!-- MASTER LENS -->
> **거장의 마무리 시각:**
> 이 세션은 28세션 PK/PD 마스터리 아키텍처에서 *PD 모델링의 첫 번째 본격 진입점* 이다. Sessions I-01~I-08(Vol I PK 이론)과 II-01~II-04(NONMEM 구현)가 *약물 농도가 어떻게 시간에 따라 변하는가* 에 답했다면, Session 11부터는 *그 농도가 어떻게 효과를 만들어내는가* — 그리고 *왜 효과의 시간 거동이 농도의 시간 거동과 다를 수 있는가* — 에 답한다. 이 분기점에서 잘못 출발하면 모든 후속 Vol I 챕터(R&T Ch.10 anti-microbials, Ch.11 anti-cancer, Ch.16 nonlinearities, Ch.20 transplantation, Ch.21 biologics)가 *실무적으로 작동하지 않는다*. R&T Ch.8의 두 축 — *공간 구조* (turnover 작용 부위, model 1–4) + *시간 척도* (PK vs PD rate-limiting) — 가 이 세션의 영구 자산이다.

---

### A. Positioning — 28세션 아키텍처에서의 위치

**선행 의존 (이 세션 진입 전 반드시 마스터되어야 할 것)**:

```
[Session I-01~I-04]  1구획·다구획 PK 이론 (R&T Ch.2-5)
                     ├─ 1차 elimination, $C(t) = C_0 e^{-k t}$
                     ├─ Distribution kinetics, $V_{ss}$ 의 의미
                     └─ AUC 계산, Cmax/tmax 정의
                              ↓
[Session I-05]       Capacity-limited PK (R&T Ch.6, Gabrielsson §2.5)
                     └─ Vmax/Km 비선형 elimination — Card 8 PK 시계 분석의 비선형 case
                              ↓
[Session I-06~I-07]  Multiple-dose PK, Steady-state, Bioavailability
                     └─ $C_{ss}$ 개념 — Card 3 tss 분석의 PK 등가
                              ↓
[Session I-08]       TMDD / 항체 PK (Gabrielsson PK27, R&T Ch.21 일부)
                     └─ Drug-target binding kinetics — Card 6 target consumption의 일반화
                              ↓
[Sessions II-01~II-04]  NONMEM 데이터셋·제어구문·General ADVAN/$DES (Owen, PIPET)
                     └─ Card 6 K 표기 충돌, Card 7 모델 비교 NONMEM 구현 기반
                              ↓
[Session 11 — 본 세션]  Indirect Response / Turnover / DRT / Effect Compartment
                       ★ Vol I → Vol I+II PD 통합의 첫 번째 본격 진입점
```

**바로 다음에 오는 것 (Session 12 예상 영역)**:

```
[Session 12]  Tolerance / Sensitization / Time-Variant PD (Gabrielsson §3.9)
              ├─ Adapter compartment 추가 (Bauer-Karlsson)
              ├─ Card 8의 *time-variant* extension — PD 시계 자체가 변화
              └─ Cards 1–4 (turnover) 위에 second-order tolerance loop 적층
```

이 세션의 **9개 MUST 카드 + 5개 혼동쌍** 이 Session 12의 절대 전제. 특히:

- **Card 1–4 turnover foundation** → tolerance model의 *base layer* (drug acts on $k_{out}$ + tolerance acts on $E_{max}$, 이중 turnover)
- **Card 8 PK vs PD rate-limiting** → tolerance kinetics가 *third clock* 이 추가됨 (drug PK + response turnover + tolerance turnover, three-clock framing)
- **Card 7 Apex Concept** → tolerance 와 indirect response의 indistinguishability 위기로 확장

**이 기반에 결정적으로 의존하는 고급 도메인**:

| 영역 | 의존 메커니즘 | 본 세션 카드 |
|---|---|---|
| **R&T Ch.10 Anti-microbials** | AUC/MIC, fAUC₂₄/MIC, T>MIC dosing target — irreversible kill + post-antibiotic effect (PAE) 의 turnover 표현 | Card 6 + Card 8 |
| **R&T Ch.11 Anti-cancer** | Cell turnover (proliferation + drug-induced kill), G1/S phase specificity — myelosuppression의 paclitaxel ANC nadir framing | Card 6 + Card 1 + Card 8 |
| **R&T Ch.16 Nonlinearities** | Capacity-limited PK + saturable PD 결합 — methylprednisolone 16–1000 mg dose-linearity 함정의 일반 framework | Card 4 + Card 5 (graphical) + Card 9 (Region 3) |
| **R&T Ch.20 Transplantation** | Tacrolimus, cyclosporine: PK-PD complexity + therapeutic window의 turnover 표현 | Card 1 + Card 7 |
| **R&T Ch.21 Biologics** | mAb의 target-mediated disposition + receptor turnover + immunogenicity의 cascade 거동 | Card 6 + Card 8 + Session I-08 (TMDD) |
| **PopPK 공변량 모델링** (Sessions III-XX) | 신기능, 간기능, 유전형이 PK 시계 vs PD 시계 중 어느 쪽을 변동시키는가 — covariate effect의 *위치* 결정 | Card 8 직접 |
| **PBPK + QSP (advanced)** | Multi-organ turnover network — Card 1 단일 ODE의 다구획 일반화 | Card 1 + Card 6 |
| **Bayesian TDM** (advanced) | Dose individualization — PK-limited 약물에 $t_D$ 공식 직접 적용; PD-limited 약물에 turnover 모델 prior 필수 | Card 8 + Card 9 |
| **NDA 모델 정당화 (PopPK section of NDA)** | 모델 선택 정당화의 *최초* 단계: PK 시계 vs PD 시계 분석. FDA reviewer는 두 축 모두에서 정당화 요구 | Card 7 + Card 8 |

---

### B. Dependencies — 이 세션을 대충 넘겼을 때의 실패 모드

이 세션을 surface-level 로 통과하면 (수식만 외우고 *공간 구조 + 시간 척도 의 두 축 framing* 을 체화하지 못하면) 고급 모델링에서 다음 실패 모드가 **추적 가능한 인과관계** 로 발생한다:

**실패 모드 1 — Effect Compartment 만능론 함정 (Card 7 미체화)**

```
원인: PD6 시뮬레이션 실험을 학습하지 못함
      → effect compartment 모델이 indirect response 데이터에 잘 맞는다는 사실을 직관으로 인식 못함
                              ↓
중간 결과: NDA 제출 모델로 effect compartment + indirect Hill 만 사용
                              ↓
1차 실패: Phase 3 광역 dose 또는 신부전 환자에서 *peak shift* 발생 — 모델 fit 무너짐
                              ↓
2차 실패: FDA Information Request: "Sponsor has not justified the choice of pharmacodynamic model"
                              ↓
3차 실패: 추가 modeling + Phase 3 일부 재실행 — 6–12개월 review 지연,
         최악의 경우 dose justification 무효 → label에 *narrow approved range* 강제,
         post-marketing commitment 추가 부담
                              ↓
근본 원인: Card 7 의 *Linear-Compatibility Mask* 와 *peak-shift signature*
         두 가지 시각적 시그널을 데이터에서 직접 읽는 능력 부재
```

**실패 모드 2 — PK-limited 가정 무비판 적용 (Card 8 미체화)**

```
원인: R&T Card 8 의 *두 시계 framing* 을 학습하지 못함
      → 모든 약물에 단순 PK-PD link 모델을 default 로 가정
                              ↓
중간 결과: Aspirin / omeprazole / paclitaxel 같은 PD-limited 약물에
         단순 link 모델 (또는 effect compartment) 적용
                              ↓
1차 실패: 약물 plasma t1/2 (15 min ~ 1 hr) 와 효과 t1/2 (days ~ weeks) 의 *수십 배~수백 배 괴리*
         를 모델이 표현 못함. NONMEM 수렴 실패 또는 비현실적 $k_{e0}$ 추정 (e.g., 0.0001 hr⁻¹)
                              ↓
2차 실패: 임상 dosing regimen 추천이 plasma PK 기준으로 산출 — 실제 효과 duration과 불일치
         → low-dose aspirin once-daily dosing 의 정당화 실패,
         omeprazole 의 *receptor turnover-based* dosing rationale 도출 실패
                              ↓
3차 실패: Phase 4 post-marketing surveillance 에서 *unexpected effect duration* 보고 —
         label dosing 부정확성 노출, FDA Adverse Event signal,
         혹은 Card 9 $t_D$ 공식 오용으로 dose escalation 시 *효과 +1 t1/2* 가 관찰되지 않아
         clinical pharmacology team 의 모델 신뢰성 상실
                              ↓
근본 원인: Card 8 의 *clock 분석 first* 원칙 부재 — 모델 구조 선택 전에
         PK 시계 vs PD 시계 비교가 의무 절차임을 인식 못함
```

**실패 모드 3 (보조) — tss 시그널 기계적 적용 (Card 3 + Card 8 통합 미체화)**

```
원인: Card 3 tss-based discrimination 만 학습하고 Card 8 의 *PK rate-limiting 전제* 를 놓침
                              ↓
중간 결과: PK-limited 약물의 데이터에서 *tss 가 dose 의존성을 보임* 을 관찰 →
         Models 2 또는 4 (kout-action) 으로 결론
                              ↓
1차 실패: 실제 작용 부위는 kin (Model 1) 이지만 tss 시그널이 PK kinetics 에 묻혀
         dose 의존성을 보임 → 잘못된 mechanistic hypothesis 채택
                              ↓
2차 실패: NONMEM 모델이 *fit* 은 잘 되나 (parameter compensation),
         covariate 분석에서 신부전 환자 prediction 이 mechanistic 가설과 모순 —
         model misspecification 으로 인한 simulation extrapolation 실패
                              ↓
근본 원인: Card 3 tss 분석은 Card 8 PK-limited 전제 위에서만 성립 — 두 카드의 위계 의존성 무시
```

각 실패 모드의 **공통점**: 본 세션의 카드 한 개를 *고립된 도구* 로 사용하고 *카드 간 위계 + 결합 framing* 을 체화하지 못한 것이 근본 원인. Cards 1–9 는 **단일 시스템** 으로 학습되어야 한다 — *공간 축* (Cards 1–7) 과 *시간 축* (Cards 8–9) 이 결합되어 임상 PK/PD 분석의 완전한 좌표계를 형성.

---

### C. Professional Moat — 이 세션 내용에 직접 답하기

> "NONMEM 으로 indirect response 모델을 적합하고 GOF 플롯을 생성할 수 있는 주니어 모델러는 이미 존재한다. AIC/BIC 비교로 Model 1 vs Model 2를 자동 선택하는 R 패키지(`nlmixr2`, `mrgsolve`), Hill equation 파라미터를 fit하는 ChatGPT 코드 생성 능력이 이미 publicly available 하다. 이 세션의 9개 카드를 — 메커니즘이 아닌 *구조적 이해의 수준에서* — 진정으로 내면화한 연구자는 그 둘 중 어느 것도 복제할 수 없는 무엇을 갖고 있는가?"

**구조적 필연성 수준의 답 — 4가지 능력**:

**1. Apex Concept (Card 7) 의 즉각 진단 능력 — Linear-Compatibility Mask 의 시각 판독**

새 PD 데이터를 받았을 때, *peak-shift 가 있는가* 를 5분 내 판독한다. Peak-shift 부재 시 *effect compartment 와 turnover model 이 indistinguishable* — 단순 AIC 비교가 무의미함을 즉시 인식한다. 이 시점에서 "광역 dose-range 데이터 또는 dose-by-dose parameter estimation 이 필요" 라고 판단하고 추가 실험 설계 또는 IR 응답을 산출. AIC 차이 1.4 같은 *misleading equivalence* 에 속지 않는 능력 — *현재 데이터 영역에서 통계적으로 구분 불가능* 과 *모델이 동등* 을 분리해서 사고한다.

**2. Card 8 두 시계 framing 의 first-pass 적용**

새 약물의 PD 데이터를 받았을 때, *모델 구조를 결정하기 전에 PK 시계와 PD 시계를 비교* 하는 절차를 default 로 수행. 이는 chatGPT 가 학습 데이터에서 흉내낼 수 있는 *지식* 이 아니라, *분석 순서* 의 체화 — drug $t_{1/2}$ 와 endogenous mediator 또는 target turnover 의 시간 척도를 *나란히 비교* 하고, 느린 쪽이 무엇인가에 따라 모델 family 를 분기. R&T 의 acenocoumarol vs phenprocoumon 대조를 마음 속에 *prototype* 으로 보유 — 새 약물을 만났을 때 "이것은 어느 prototype 에 가까운가?" 를 즉답.

**3. Cards 8–9 의 *적용 가능성 분기 판단* — $t_D$ 공식 함정 회피**

Card 9 의 $t_D = (1/k)\ln(Dose/A_{min})$ 공식은 *PK rate-limited 약물에만 적용 가능* — 이 전제를 위반한 채로 aspirin 또는 paclitaxel 에 적용하면 임상적으로 무의미한 결과 산출. 주니어 모델러는 공식 자체는 외우지만 *적용 조건* (Card 8 분석 결과) 을 매번 확인하는 절차를 갖지 못함. 이 *공식 → 전제 검증 → 적용 분기* 의 3단 절차가 체화된 모델러는 dose-duration 분석에서 함정에 빠지지 않는다.

**4. Card 1 hysteresis classification 의 *클래스 즉답* + Card 7 과의 통합 판단**

E vs C plot 을 처음 보는 즉시 (1) hysteresis 유무, (2) clockwise vs counterclockwise 분류, (3) 가능한 mechanism set ($k_{e0}$ distribution / turnover / target consumption / sensitization / metabolite contribution) 을 동시에 호출. 분류 → mechanism 매핑은 *외워서 떠올리는 것* 이 아니라 *시각 패턴이 곧바로 ODE 구조를 떠올리게 하는* 신경 회로의 형태로 체화되어야 함. R&T Fig 8-3, 8-4, 8-5 의 도식이 *시각적 사전* 으로 영구 저장됨. AI 가 이 시각 매핑을 흉내내려면 vision model + domain knowledge graph 의 결합이 필요한데, 그 결합 자체가 *체화된 인간 전문가* 의 모방. 그리고 분류 직후 Card 7 의 위기 framing — *어느 메커니즘이 진짜인가의 식별 위기* — 를 즉시 발동, 광역 dose-range 또는 dose-by-dose 분석 필요성을 판단.

**5가지 종합 — Master 의 단 한 문장**:

> *"새 PD 데이터를 받으면, 농도-효과 plot 의 형태와 두 시계의 비교 분석을 *동시에 머릿속에서 회전* 시킨다 — 그것이 모델 구조 선택의 두 축 (공간 + 시간) 좌표계를 즉각 결정해주며, 이 좌표계 위에서만 Hill equation 의 파라미터 추정이 임상적 의미를 갖는다."*

이것은 NONMEM 사용법이 아니다. R 패키지로 자동화 가능한 분석이 아니다. AI 가 학습 데이터에서 흉내낼 수 있는 chain-of-thought 가 아니다. 9개 카드의 *상호 연결 구조* 가 한 명의 연구자 안에서 *동시 호출 가능한 단일 인지 네트워크* 로 구축되었을 때만 발휘되는, 본 세션 학습의 영구 자산이다.

<!-- RECAP -->
**§8 종결 흐름 요약**: 본 세션은 28세션 아키텍처의 *PD 모델링 첫 본격 진입점* 이며, 향후 R&T Ch.10/11/16/20/21 + Sessions III-XX (PopPK 공변량) + Bayesian TDM + NDA 모델 정당화 의 모든 영역에 *직접 의존성* 을 갖는다. 본 세션을 surface-level 로 통과하면 effect compartment 만능론 + PK-limited 무비판 적용 + tss 기계적 해석 의 3가지 실패 모드가 추적 가능한 인과로 발생. 본 세션의 영구 자산은 *공간 축 (Cards 1–7) + 시간 축 (Cards 8–9) 의 결합 좌표계* 를 *모든 새 PD 데이터에 default 로 적용하는 분석 습관* — 이는 NONMEM 사용법이나 R 자동화로 복제 불가능한, 9개 카드의 상호 연결 구조가 단일 인지 네트워크로 체화되었을 때만 발휘되는 능력이다.

---

✦ **Phase 1 (Stage 1 + Stage 2) 완료.**

다음이 준비되었습니다:

| 섹션 | 산출물 | Stage 1 (G만) | Stage 1+2 통합 |
|---|---|---|---|
| §1 | 세션 헤더 & 로드맵 | Big Idea 1축 (turnover) | Big Idea 2축 (turnover + 두 시계). Knowledge graph에 R&T Ch.10/11/16/20/21 successor 추가 |
| §2 | 개념 해부 카드 | 7개 (Cards 1–7) | **9개** (Cards 1–9). Cards 1, 3, 4, 5, 7 본문 R&T 통합 보강. **Card 8 (PK vs PD rate-limiting), Card 9 ($t_D$ formula) 신규 추가** |
| §5 | 혼동 쌍 해부 | 4개 쌍 (§5-1 ~ §5-4) | **5개 쌍**. §5-4 Critical Blow R&T 강화. **§5-5 (PK rate-limited vs PD rate-limited) 신규 추가** |
| §7 | Self-Test | 8개 질문 (Q1–Q8 Boss Dilemma) | **10개 질문**. **Q8 (R&T hysteresis classification — digoxin vs ibuprofen), Q9 ($t_D$ formula succinylcholine 계산) 신규 추가**. Boss Dilemma 위치 Q8 → Q10 이동 + R&T Card 8 framing 강화 |
| §8 | 메타프레임 & 빅 픽처 | (Stage 1에서 미작성) | **Stage 2에서 신규 작성**. Positioning (28세션 아키텍처 + 후속 챕터), Dependencies (3가지 실패 모드 trace), Professional Moat (5가지 능력 구조적 답변) |

**감지된 소스 유형**: 혼합 — Vol I (Gabrielsson §3.4–3.10 + Rowland & Tozer Ch.8 p.233-264)

**Curation Map 결정 요약**:
- MUST 9개 (Cards 1–9): 7개는 G primary + R&T 보강; 2개 (Cards 8–9)는 R&T primary
- CONTEXT 11개: 본문 1–2 문장 통합 (negative feedback / capacity-limited extension / cell growth+kill / DRT framework / baseline drift / peak shift theory / direct PK-PD link / indirect link / Region 1/2/3 / dose linearity trap / transporter polymorphism)
- 핵심 결정: **Transporter polymorphism (rosuvastatin OATP1B1, R&T p.256-259)** — Scope Lock 주의사항 4번에 따라 **CONTEXT 처리** (보조 주제, 본 세션 핵심 골격에 종속되지 않음)

**Data Anchoring 소스**:
- *Gabrielsson*: PD4 (Pool 1 inhibition), PD5 (Pool 2 stim of kout), PD6 (effect compartment vs Model 1, 64 sims), PD7 (Pool 2 inhibition of kout), PD9 Zooparc® (3-dose simulation), Fig 3.40 ($E_{max}$ semantics), Fig 3.49–3.50 (cell kill)
- *R&T Ch.8*: digoxin 1 mg iv (Fig 8-1), naproxen 250 mg (Fig 8-3, *counterclockwise*), ibuprofen 6 mg/kg (Fig 8-4, *clockwise*), midazolam 15 mg/kg rat (Fig 8-6, no hysteresis), warfarin 1.5 mg/kg (Fig 8-10, 8-15B blocking dose), acenocoumarol vs phenprocoumon (Fig 8-11, *PK vs PD rate-limiting Apex 사례*), aspirin 650 mg (Fig 8-20, *target consumption + PD-limited*), omeprazole (proton pump irreversible), succinylcholine 0.5/1/2/4 mg/kg (Fig 8-24, T50 vs log dose, $k$ ≈ 0.2 min⁻¹), minoxidil (PK-limited topical), paclitaxel ANC nadir (Fig 8-19, cell turnover), methylprednisolone 16/32/64/125/250/500/1000 mg (Fig 8-25/26/27, *dose linearity trap*), rosuvastatin OATP1B1 (Fig 8-28/29, *CONTEXT*)

**Stage 2 통합 결정 — Anti-Pattern Checklist 검증**:

- [x] Curation Map 작성 후 §2 진입 (Phase 1 재실행 사유 없음)
- [x] Big Idea 모두 *구체적 임상 결과* 로 작성 — 추상적 "이 개념은 PK의 기초이다" 표현 부재
- [x] FIGURE 마커 미삽입 (Phase 4C 전담 영역 — Phase 1 위반 없음)
- [x] §5 기억 고리 모두 *구조적 이유* 인코딩 (단순 차이 나열 아님)
- [x] §7 마지막 질문 Q10 = Socratic Dilemma (모델 단순성 vs 광역 dose 정확성 + 신부전 환자 두 시계 분석)
- [x] [확인 필요] 태그 보존 (Card 6 K notation 충돌 — bacterial 2차 상수 vs PK elimination 1차 상수)
- [x] §8 신규 작성 (Stage 1 미작성 분량) — Positioning + Dependencies + Professional Moat 모두 본 세션 9개 카드에 직접 anchored, 동기 부여적 발언 부재

---

**Phase 1 산출물의 다음 단계**:

본 문서 (`Step 1 Draft v0`) 는 *Phase 1 Master's Lens Draft* 산출물이다. 다음 Phase 진입 시:

```
Phase 2  →  Source Fidelity Audit (Gemini Pro / Deep Research)
            • 입력: Gabrielsson PDF + R&T Ch.8 PDF + 본 Draft v0
            • 산출: Audit Report v1 (T1–T6, T6에 Inspection Method 포함)
            
Phase 3  →  Insight Crucible (박사과정 멘토 — A-Critical 모드)
            • 입력: Draft v0 + Audit v1
            • 산출: Crucible Report v1
            
Phase 4A → Integration & Compression (GPT-5.5 Thinking)
Phase 4B → Readability + Annotation (동일 세션)
Phase 4C → Visual Pedagogy Triage (PATCH MODE 권장 — 본 Draft 길이 초과)
            
Phase 5  → HTML Compile (Step 2 V5.1 컴파일러)
Phase 6  → HTML QA (A-Critical 모드)
```

본 Draft 의 **9개 MUST 카드 + 5개 혼동쌍 + 10개 self-test + §8 메타프레임** 이 다음 Phase 들의 *변경 불가능한 base layer*. Phase 4 의 통합 편집은 본 Draft 를 *변형* 하는 것이 아니라 *압축 + readability polish + annotation* 만 수행한다.

---

*Phase 1 Master's Lens Draft v0 — Stage 1 + Stage 2 통합 완결*  
*Source: Gabrielsson & Weiner 5e (§3.4–3.10) + Rowland & Tozer 5e (Ch.8, p.233-264)*  
*Mode: A-Critical | Generated under V5.1 Apex Edition Step 1 protocol*

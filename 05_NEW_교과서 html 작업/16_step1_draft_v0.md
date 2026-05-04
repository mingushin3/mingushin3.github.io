# Session 016 — 임상 통합 캡스톤 (패턴 인식 · TDM · 질환 · 치료 의사결정)
## Step 1 Master's Lens Draft v0 (Stage 3 of 3 — FINAL Cumulative Integration)

> **Stage Integration Map (3단계 누적 확장 완료)**
>
> 이 세션은 단일 챕터가 아니라 **네 권의 교과서 챕터를 임상 의사결정 흐름으로 통합**하는 캡스톤이다. 본 v0은 Stage 1·2·3까지 모두 통합된 최종 단일 산출물이다:
>
> | Stage | 소스 | 추가된 §2 카드 | 추가된 §5 혼동쌍 | 통합 골격에서의 역할 |
> |---|---|---|---|---|
> | Stage 1 ✅ | Gabrielsson Ch.6 + PK15 + PK35 | §2.1–§2.6 | §5.1–§5.3 | **모델 구조 선택 + 개인 파라미터 추정 + 노출 보고** |
> | Stage 2 ✅ | R&T Ch.15 (Disease) | §2.7 Rd Framework, §2.8 Cockcroft-Gault, §2.9 투석 보충 용량 | §5.4 hepatic high-E vs 신배설 약물 | **개인이 모집단에서 벗어나는 이유** |
> | **Stage 3 ✅ (FINAL)** | R&T Ch.18 (Initiating and Managing Therapy) | **§2.10 TCS 적용 조건, §2.11 Loading Dose 결정 원칙, §2.12 Missed/Erratic Dosing** | **§5.5 Maintenance vs Loading dose** | **임상 의사결정 — 처방·관리** |
>
> 최종 통합 내러티브:
>
> ```
> [Ch.6 Pattern Recognition] → 어떤 PD 모델을 쓸 것인가
>           ↓
> [Ch.15 Disease]            → 환자가 모집단에서 얼마나 벗어났는가
>           ↓
> [PK35 Bayesian]            → 그 환자의 개인 파라미터를 어떻게 추정할 것인가
>           ↓
> [Ch.18 Initiating Therapy] → 그 추정으로 어떤 용량을 처방할 것인가  ← Stage 3
>           ↓
> [PK15 Toxicokinetics]      → 그 노출을 규제·임상에 어떻게 보고할 것인가
> ```

---

## ━━ Curation Map (Stage 1 + Stage 2 + Stage 3 최종 누적) ━━

### MUST tier — 체화 필수 (§2 전용 카드)

| # | 개념 | 이유 |
|---|---|---|
| **2.1** | **패턴 인식 결정 알고리즘** (4축) | PD 모델 선택의 진입점. 이것 없이 NONMEM 코딩 불가. |
| **2.2** | **Peak-shift Directionality** [⚡ Apex #1] | 좌/우 방향이 곧 모델 클래스. 방향 오판 → NDA Exposure-Response wrong mechanism. |
| **2.3** | **Effect Compartment (Link Model)** | "Time-delay 있음 + Peak-shift 없음" 표준 답. |
| **2.4** | **Turnover Model** | PD 작업말 70%. kin·I(C), kin-kout·R·S(C) 두 작용점 구분 핵심. |
| **2.5** | **Receptor On/Off** | 좌향 peak-shift 분기에서 turnover 외 유일 대안. 2차 결합 동역학. |
| **2.6** | **Bayesian Objective Function** [⚡ Apex #2] | 모든 TDM 소프트웨어의 추정 엔진. 세 극단 케이스 인식. Stage 2/3 확장. |
| **2.7** | **Rd Framework** [⚡ Apex #3] | $R_d = RF \cdot f_e + 1-f_e$. fe(약물)·RF(환자) 분리. Stage 3에서 LD 분기 추가. |
| **2.8** | **Cockcroft-Gault** | Rd 입력 단계. 비만/근감소 함정. |
| **2.9** | **Hemodialysis 보충 용량** | $V_u<120$L AND $CL_u<CL_{uD}$ 두 조건. half-life 단축 ≠ 임상적 제거. |
| **2.10** | **TCS 적용 조건** [⚡ Apex #4 — Stage 3] | 5 criteria. Warfarin 부적용 vs Phenytoin 적용 분기. |
| **2.11** | **Loading Dose 결정 원칙** | $D_L = V \cdot C_{target}/F$. V 의존 — CL보다 well-defined. |
| **2.12** | **Missed/Erratic Dosing 수식 framework** | Eq. 18-1 ~ 18-4. Superposition 원리. 임상 TDM 80% 처리. |

### CONTEXT tier — 1–2문장으로만 §2 본문 편입

| 항목 | 편입 위치 | 처리 |
|---|---|---|
| Case A~I 개별 방정식 | §2.4·§2.5 본문 | 패턴 분류 인스턴스 1–2문장. |
| Hill·Gompertz·Linear concentration-response | §2.4 본문 | "Drug mechanism function 변형" 1문장. |
| Hysteresis (CCW vs CW) | §2.3 본문 | Effect compartment 진단 시그니처 1문장. |
| Tolerance / Down-regulation (Case I) | §2.4 본문 | "시간 의존 EC50(t)" 1문장. |
| **PK15 NCA + 안전역** (10–320 µmol·day⁻¹·kg⁻¹, Cmax ~50 µM, 치료 0.05–0.1 µM, >100배) | §1 + Step 2 §6 예약 | §2 카드 없음. §7·§8 인용. |
| Adaptation / Rebound (Eq. 6:35) | §2.4 본문 | Bi-phasic decline 신호 1문장. |
| **Hepatic disease** (Child-Pugh, Cefetamet/Meptazinol/Verapamil 비교) | §2.7 본문 + §5.4 | 신질환과의 대조. |
| **Cardiovascular disease** (CHF, Sheiner digoxin Table 15-7) | §2.6 B-3 | Conditional prior 인스턴스. |
| **CAPD** | §2.9 본문 | Hemodialysis 대조 1문장. |
| **Disease-on-PD** (WHIG, biomarker type 0–6) | §8 Moat | "확장 가능한 시야" 1문장. |
| **Sources of variability** (Fig. 18-2/18-5/18-6) | §2.10 본문 | TCS 적용 조건의 정량 근거. |
| **Pharmacogenomic variability** (CYP2D6 trimipramine, HLA-B*5701, TPMT) | §2.10 본문 | Genotype 기반 prior selection 인스턴스. |
| **Adherence patterns** (Table 18-4) | §2.12 본문 | Forgiving/unforgiving drug 개념. |
| **Doubling-up doses** (Fig. 18-10) | §2.12 본문 | Eq. 18-4 erratic framework specific case. |
| **Discontinuing therapy / tapering** (β-blocker, corticosteroid) | §8 본문 | 의사결정 비대칭성 인지 1문장. |
| **Confidence in estimates** (Fig. 18-13) | §2.6 B-4 + §2.12 본문 | 초기 sample → V; 후기 → CL. |
| **Dose strengths** (warfarin 1·2·2.5·5·7.5·10 mg) | §2.11 본문 | LD theoretical → actual product mapping 1문장. |
| **Tolerance to PD** (nitroglycerin patch, terazosin) | §8 본문 | 만성 dosing PD 변동 1문장. |
| **Changes in therapy** (drug interaction) | §8 + §2.10 본문 | TCS 재적용 trigger 1문장. |

### 의도적 제외

- §6.4·§6.5·§6.6·§6.9의 2차 미분 패턴, fu vs C 관계 (Eq. 6:111) — 별도 세션
- MDRD GFR (Table 15-4) — Cockcroft-Gault 표준 유지
- 단백질 약물 신장 대사 (imipenem) — Ch.21 Protein Drugs
- Ch.15 Study Problems pp.483–489 — §7 디자인 참고
- **Ch.18 Study Problems pp.606–610** — §7 디자인 참고
- **Adherence 사회·심리 측면** — PK/PD framework 외
- **Variability 섹션 Fig. 18-2/18-5/18-6 quantitative analysis** — §2.10 입력 정보

---

# §1 — Session Header & Roadmap

**Session ID**: 016 — 임상 통합 캡스톤 (패턴 인식 · TDM · 질환 · 치료 의사결정)

**Sources**:
- **Stage 1**: Gabrielsson & Weiner 5e — Ch.6 (pp.423–466), PK15 (pp.546–548), PK35 (pp.641–643)
- **Stage 2**: Rowland & Tozer 5e — Ch.15 Disease (pp.443–489)
- **Stage 3**: Rowland & Tozer 5e — Ch.18 Initiating and Managing Therapy (pp.577–610)
  - 핵심 추출: TCS criteria (pp.594–606), Loading Dose 결정 (pp.584–586), Missed/9-13-17-21/Erratic 수식 (pp.600–606), Confidence in Estimates Fig. 18-13
  - CONTEXT: Variability (Fig. 18-2/18-5), Adherence (Table 18-4), Discontinuing therapy, Tolerance, Dose strengths

<!-- MASTER LENS -->

**Big Idea (단 한 문장)**:
> 데이터의 *형태*는 그 데이터를 만든 *기계*의 흔적이고, 환자의 *질환*은 그 기계의 파라미터를 모집단에서 끌어내며, *Bayesian 추정*은 그 변동을 정량화하고, *임상 의사결정*은 그 정량을 처방으로 전환한다 — 이 사슬의 한 고리라도 끊기면 그 환자에게 도달하는 약물의 양은 그 환자에게 필요한 양과 *체계적으로* 어긋난다.

**개념 항법도 (Stage 1·2·3 누적 — 완성)**:

```
              [거시: 패턴 인식 결정 알고리즘 §2.1]
                          │
        ┌─────────────────┴─────────────────┐
        │                                   │
  Time-delay 없음                     Time-delay 있음
        │                ┌──────────────────┴──────────────────┐
   E = E0 ± a·C       Peak-shift 없음                  Peak-shift 있음
                   [§2.3 Effect Compartment]                   │
                                                ┌──────────────┴──────────────┐
                                          Leftward (←)                 Rightward (→)
                                          │                                   │
                                  kout 자극 (turnover)              kin 억제 (turnover)
                                  OR Receptor on/off                          │
                                  [§2.4 §2.5 §2.2 Apex]              [§2.4 §2.2 Apex]
                                                  │
                                    [§2.6 개인 파라미터 추정 — Bayesian]
                                                  │
                              ▼ (Stage 2) ▼
                   [§2.7 Rd Framework] ← [§2.8 Cockcroft-Gault]
                              │
                ┌─────────────┴─────────────┐
        Rd = RF·fe(t) + 1−fe(t)         투석 환자
        (외래/입원 dose 조정)            [§2.9 hemodialysis 보충 용량]
                              │
                  ▼ (Stage 3) ▼
        [§2.10 TCS 적용 조건] ← 5 criteria 평가
                  │
        ┌─────────┴─────────┐
   Initial dose 결정           Maintenance dose 조정
   [§2.11 Loading Dose]        [§2.6·§2.7·§2.9의 출력 적용]
        │                              │
        └────────┬─────────────────────┘
                 │
        [§2.12 Missed/Erratic Dosing]  ← 비정형 임상 시나리오 정량 평가
                 │
        [§6 노출 보고 — PK15 안전역 (Step 2 deferred)]
```

**지식 그래프 위치**:

- **선행 필수**: 1구획 IV/oral PK, Emax/Hill, Turnover 기초, Effect Compartment, kon/koff, 정규분포 likelihood, Renal anatomy, Body composition vs age/weight, $f_e$ 정의, **Multiple-Dose accumulation 원리** (Ch.11 R&T) — Stage 3 §2.11·§2.12 직접 입력, **Therapeutic window** (Ch.9 R&T) — Stage 3 TCS 입력.

- **이 세션이 열어주는 후속 영역**:
  - PopPK PD 통합 모델 NONMEM 구현 ($PK + $PD + $DES)
  - Bayesian TDM 소프트웨어 운용 (BestDose, ID-ODS, Pmetrics)
  - NDA/IND PK/PD 섹션 규제 언어
  - 신부전 환자 dose 조정 임상 운용 — Rd 계산
  - 투석 약사 보충 용량 산정 — Eq. 15-34
  - Conditional prior TDM — Sheiner 형 covariate prior
  - **임상 약사 처방 권고 작성** — Loading/Maintenance/Missed dose 의무기록 기재 (Ch.18 직접)
  - **Phase 4 RMP** — TCS 약물 post-marketing concentration data 분석
  - **Pharmacogenomic-guided dosing** — CYP2D6·HLA·TPMT 기반 prior 조건화

**학습 목표 (Stage 1·2·3 통합)**:
1. 4축 패턴 인식으로 60초 내 모델 클래스 좁히기.
2. Peak-shift 좌/우 → ODE 작용점 매핑 + 기계론적 설명.
3. Bayesian 두 합 항의 분산비로 개인성 반영도 평가.
4. PK15 ">100배 안전역" NDA 규제 언어 작성.
5. Cockcroft-Gault → RF → Rd 산출.
6. 30% 규칙으로 신부전 조정 대상 약물 분류.
7. Hemodialysis 보충 용량 Eq. 15-34 적용.
8. Sheiner 1977 conditional prior로 PK35 추정 검증.
9. 간경변 vs 신부전의 PK 변동 *방향성* 매트릭스 운영.
10. **TCS 5 criteria로 임의 약물의 적용 가능성 신속 평가** (warfarin 부적용 vs phenytoin 적용).
11. **$D_L = V \cdot C_{target}/F$ 계산 + available dose strengths 매핑**.
12. **Missed/9-13-17-21/Erratic 수식 적용 → 비정형 dosing 환자 농도 예측·해석**.
13. **TCS 적용 *전*과 *후*의 Bayesian 정확도 차이** + 한 점 vs 다 점, flat vs conditional prior 평가 — Stage 1·2·3 통합 정점.

<!-- RECAP -->
**§1 흐름 요약**: "어떤 모델을 쓸 것인가(Ch.6) → 그 환자가 모집단에서 얼마나 벗어났는가(Ch.15) → 그 환자의 파라미터를 어떻게 추정할 것인가(PK35) → **그 추정으로 어떤 용량을 처방·관리할 것인가(Ch.18)** → 그 결과를 어떻게 보고할 것인가(PK15)" — 5단계 의사결정 사슬이 단일 환자 visit에서 운영되는 단일 흐름으로 완성.

---

# §2 — Concept Anatomy Cards

## §2.1 — 패턴 인식 결정 알고리즘

> ### ━━ 거장의 시각 ━━
> <!-- MASTER LENS -->
>
> **왜 치명적으로 중요한가**: 이 4축 알고리즘 없이 PD 모델을 선택하면, NONMEM이 수렴하더라도 그 추정값은 *데이터를 만든 생물학과 무관한 숫자*가 된다 — 즉, 모든 후속 dose-extrapolation, FIH 용량 결정, 라벨링이 오류 위에 쌓인다.
>
> **체화해야 할 단 하나의 직관**: PD 데이터의 *형태*는 ODE의 *어느 항이 약물에 의해 조작되었는가*에 대한 직접적 흔적이다 — Peak-shift는 시간 척도의 변화이며, 시간 척도는 rate constant이며, rate constant는 ODE의 항에 박혀 있다.
>
> **이 직관을 머릿속에 박고 아래를 읽어라**: 가브리엘슨이 9개 케이스를 늘어놓은 이유는 9개 답을 외우라는 게 아니라, **4축의 조합으로 모든 답이 도출된다**는 것을 보여주기 위함이다.

### A. Formal Definition

응답-시간 곡선 $R(t)$의 시각적 특징을 4개 진단 축으로 분해하여 ODE 구조의 후보 집합을 좁히는 절차. 가브리엘슨 5e Ch.6 §6.1 Figure 6.1·§6.9 Figure 6.12.

4축:
1. **Baseline 축**: $R(t=0) = E_0 \neq 0$ vs $= 0$
2. **Time-delay 축**: $t_{\max}^{C}$와 $t_{\max}^{R}$ 시간차
3. **Peak-shift 축**: 용량↑ 시 $t_{\text{extreme}}$ 좌(←)·우(→)·불변
4. **Saturation 축**: dose-normalized AUCE plot 수평선 이탈 여부

### B. Derivation / 결정 트리

```
[Step 1] Baseline 있음? ── 없음 → E = E0 ± a·C [Case 6.6-A]
                       └─ 있음 → [Step 2]
[Step 2] Time-delay? ── 없음 → E = E0 ± Hill function
                     └─ 있음 → [Step 3]
[Step 3] Peak-shift? ── 없음 → Effect compartment [§2.3]
                     └─ 있음 → [Step 4]
[Step 4] 방향?       ── ← Leftward → kout 자극 OR Receptor on/off
                     └─ → Rightward → kin 억제 [§2.4]
[Step 5] Saturation 검증 (dose-normalized AUCE)
```

**Micro-citation**: `[출처: Gabrielsson 5e, Ch.6, p.423, p.466, Fig.6.1·6.12]`

### C. Structural Necessity

4축이 정확한 이유: **PD 모델 자유도가 정확히 4개 정성적 의사결정으로 환원**.
- Baseline → $E_0$ 또는 $k_{in}/k_{out}$ 항 필요 여부 (생리적 항상성 존재)
- Time-delay → kinetic separation 필요 ($k_{e0}$ or turnover)
- Peak-shift → 약물 작용점 비선형성 강제
- Saturation → drug action 함수 형태 (Hill vs linear)

5축은 redundant, 3축은 model class 분리 불가.

### D. Assumptions & Boundary Conditions

1. **Plasma kinetics 선형** (가브리엘슨 §6.1) — TMDD/saturable elimination 시 false PD peak-shift.
2. **충분한 dose range + sampling 밀도** — 최소 3 dose levels, nadir/peak dense sampling.
3. **단일 작용점** — kin/kout 동시 작용 시 부분 상쇄로 false no-shift.

### E. Limitations

- 후보 좁힘만 — 단일 모델 결정에는 dose-normalized AUCE 검증 필수.
- Secondary peaks (tolerance), bi-phasic decline, Case 6.4-B 같은 dual-action은 추가 진단 필요.
- Sparse data 시 peak-shift 방향 통계적 모호 (§7 Boss Dilemma 대상).

### F. Five Cognitive Layers

| L | 내용 |
|---|---|
| **L1** | 4축 = ODE 자유도 1:1 대응. 9 생리적 분기. |
| **L2** | Peak-shift = 시간축 위상 이동. Dose-dependence가 spectral signature. |
| **L3** | First-order kinetics, RC time constant, logistic growth — turnover 동형. |
| **L4** | kin (zero-order 합성) vs kout (first-order 분해) — 다른 메커니즘. |
| **L5** | NONMEM `DADT(1) = KIN*(1-IMAX*C/(IC50+C)) - KOUT*A(1)` vs `DADT(1) = KIN - KOUT*A(1)*(1+SMAX*C/(SC50+C))` — 한 줄 차이, 의미 정반대. |

### G. Zettelkasten Atom

```yaml
---
aliases: [패턴 인식 알고리즘, Pattern Recognition Decision Tree]
tags: [pharmacometrics/pd, model-selection, gabrielsson/ch6]
up: "[[PD 모델링 MOC]]"
related: ["[[Peak-shift Directionality]]", "[[Effect Compartment]]",
          "[[Turnover Model]]", "[[Receptor On-Off Model]]"]
source: "Gabrielsson & Weiner 5e, Ch.6, pp.423–466"
---
```

PD 데이터 모델 클래스는 4 시각 축(baseline·time-delay·peak-shift·saturation) 조합으로 좁혀진다. ODE 구조 자유도와 1:1 대응. 알고리즘은 *후보로 좁힐 뿐* — 단일 모델은 dose-normalized AUCE 검증. 가정: linear plasma kinetics + 단일 작용점 + 3+ doses.

<!-- ANCHOR -->
4축 중 가장 진단력 높은 단 하나가 **Peak-shift Directionality** — §2.2가 별도 Apex Concept인 이유.

---

## §2.2 — Peak-shift Directionality [⚡ Apex Concept]

> ### ━━ 거장의 시각 ━━
> <!-- MASTER LENS -->
>
> **왜 치명적으로 중요한가**: 30년 차 모델러가 Phase 1 dose-finding 데이터를 받아 가장 먼저 보는 것이 peak-shift의 좌우 방향 — 이 한 가지가 IC50 vs SC50, kin vs kout 작용을 가르며, 방향 거꾸로 읽으면 NDA Exposure-Response 전체가 wrong drug mechanism 위에 써져 Deficiency Letter 직결.
>
> **체화해야 할 단 하나의 직관**: Peak/nadir이 *왼쪽으로* 이동 = 약물이 *반응 소실 가속* 또는 *수용체 풀 빨리 고갈* (out 또는 binding 측). 오른쪽 = 약물이 *반응 생성 차단* (in 측). **방향은 약물이 손댄 쪽을 그대로 가리킨다.**
>
> **이 직관을 머릿속에 박고 아래를 읽어라**: 가브리엘슨이 Case B(좌향), C(좌향, on/off), G(우향)를 분리한 이유가 이 단일 진단의 임팩트 강조.

### A. Formal Definition

용량↑ 시 $t_{\text{extreme}}$ 이동 방향 $\partial t_{\text{extreme}} / \partial \text{Dose}$의 부호.

| 방향 | 모델 클래스 | ODE | 약물 함수 위치 |
|---|---|---|---|
| **No shift** | Effect compartment | $dC_e/dt = k_{e0}(C_p - C_e)$ | 별도 구획 + 선형 PK |
| **← Leftward (a)** | Turnover, kout 자극 | $dR/dt = k_{in} - k_{out} \cdot R \cdot S(C)$ | $k_{out}$ 항에 $S(C)$ |
| **← Leftward (b)** | Receptor on/off | $d[RC]/dt = k_{on} \cdot C \cdot [R] - k_{off} \cdot [RC]$ | $[R_T] - [RC]$ 풀 빨리 고갈 |
| **→ Rightward** | Turnover, kin 억제 | $dR/dt = k_{in} \cdot I(C) - k_{out} \cdot R$ | $k_{in}$ 항에 $I(C)$ |

**Micro-citation**: Case B/C/E/F/G/H `[출처: Gabrielsson 5e, Ch.6, pp.430–435, Eq. 6:10–6:12, 6:18, 6:32–6:33]`

### B. Derivation — 좌/우 분기의 기계론

**Rightward — kin 억제**: $I(C) = 1 - I_{\max}C^n/(IC_{50}^n + C^n)$. 용량↑ → $I(C) \to 1 - I_{\max}$ 지속. R은 자연 분해 ($k_{out}$만)되어 *천천히* 깊은 nadir 도달 → 우측 이동.

**Leftward — kout 자극**: $S(C) = 1 + S_{\max}C^n/(SC_{50}^n + C^n)$. 용량↑ → 분해 가속 → 빠른 새 정상상태 $R_{ss} = k_{in}/[k_{out} \cdot S(C)]$ 도달 → 좌측 이동.

**Leftward — Receptor on/off**: $C$가 *2차 항*에서 곱해짐. 용량↑ → $k_{on} \cdot C \cdot [R]$ 가속 → free receptor 풀 빨리 소진 → max binding 시간 단축.

### C. Structural Necessity

수학적 비대칭성:
- **kin (zero-order, 농도 무관)** 억제 → 시상수 *길어짐* → 우향
- **kout · R (first-order, R 비례)** 자극 → 시상수 *짧아짐* → 좌향
- **2차 binding (C 직접 곱)** → dose↑이 binding rate↑로 직결 → 좌향

요약: **시상수가 빨라지는 방향이 좌향, 시상수가 약물 농도와 비선형 결합하는 항이 약물 작용점**.

### C-2. Plausible Fallacy

> #### ⚠ 가장 자주 저지르는 직관적 오류
>
> **오류**: "용량 ↑ → 약효 강화 → nadir 깊어짐 → 따라서 더 *늦게* 도달" 추론 → 모든 leftward 데이터를 rightward로 잘못 읽음.
>
> **나비효과**:
> 1. Leftward 데이터 → kin 억제 모델 채택 → IC50 추정.
> 2. 실제는 SC50인데 IC50 라벨로 NDA 제출.
> 3. Dose extrapolation 3–10배 편향 (특히 고용량).
> 4. FDA Deficiency: "Mechanistic inconsistency".
>
> **GOF 시그니처 — "고용량 후기 잔차 부채꼴 패턴"**: CWRES vs time에서 고용량군 nadir 이후 잔차 한쪽 부채꼴, 저용량군 정상.
> **대응**: kin 억제·kout 자극 모두 fit + simultaneous multi-dose 검증.

### D-E. Assumptions & Limitations

가정: drug mechanism function이 saturable + linear plasma kinetics + ≥5배 dose ratio.
한계: sparse sampling 시 통계적 분리 불가, mixed mechanism 시 false no-shift, tolerance (Case I) 시 EC50(t) 추가 진단.

### F. Five Cognitive Layers

| L | 내용 |
|---|---|
| **L1** | $\partial t_{\text{extreme}} / \partial \text{Dose}$ 부호 = ODE 작용점. |
| **L2** | 곡선의 시간축 *위상 이동*, dose-dependence = response-surface 곡률. |
| **L3** | Enzyme-substrate (out 자극) vs feedback inhibition (in 억제) 동형. |
| **L4** | kin 억제 = "수도꼭지 잠금", kout 자극 = "배수구 확대" — 시간 척도 정반대. |
| **L5** | IPRED-DV 잔차 시계열 부채꼴 → 메커니즘 의심 → simultaneous multi-dose fit 검증. |

### G. Zettelkasten Atom

```yaml
---
aliases: [Peak-shift, 피크 시프트, 시간-응답 위상 이동]
tags: [pharmacometrics/pd, apex-concept, gabrielsson/ch6]
up: "[[패턴 인식 결정 알고리즘]]"
related: ["[[Turnover Model]]", "[[Receptor On-Off Model]]",
          "[[High-dose late-time fan-shaped residual]]"]
source: "Gabrielsson & Weiner 5e, Ch.6, Cases B/C/E/F/G/H, pp.430–436"
---
```

용량↑ 시 $t_{\text{extreme}}$ 이동 방향이 ODE 작용점을 가리킨다. 좌향 = kout 자극 또는 receptor on/off. 우향 = kin 억제. No shift = effect compartment. 방향 오판 시 IC50/SC50 라벨 반대 → NDA wrong mechanism. 진단: 고용량 후기 부채꼴 잔차.

<!-- ANCHOR -->
"no peak-shift" → §2.3 Effect Compartment, "leftward 또는 rightward" → §2.4 Turnover 또는 §2.5 Receptor On/Off.

---

## §2.3 — Effect Compartment (Link Model)

> ### ━━ 거장의 시각 ━━
> <!-- MASTER LENS -->
>
> **왜 치명적으로 중요한가**: 마취제(propofol, fentanyl), 항부정맥제(verapamil) — 임상 hysteresis 데이터의 90%가 effect compartment로 충분. Turnover로 강제하면 over-fitting으로 simulation 왜곡.
>
> **체화해야 할 단 하나의 직관**: Effect compartment = *물리적 분포 지연*만. 어떤 *생리적 항상성*도 가정 안 함. Turnover는 그 위에 항상성 더한 것.
>
> **이 직관을 머릿속에 박고 아래를 읽어라**: $k_{e0}$는 분포 rate이지 turnover rate가 아니다 — 같은 시간 차원 *다른 물리량*.

### A-B. Definition & Derivation

핵심 ODE (Eq. 6:5, 6:14, 6:19):
$$\frac{dC_e}{dt} = k_{e0}(C_p - C_e)$$

응답 함수 변형:
- 선형 + baseline: $E = E_0 + a \cdot C_e$ (Case 6.4-D, Eq. 6:20) `[출처: Gabrielsson 5e, Ch.6, Eq. 6:20]`
- Hill + baseline: $E = E_0 + E_{\max} C_e^n / (EC_{50}^n + C_e^n)$ (Eq. 6:15)
- Inhibitory Hill: $E = E_0 - I_{\max} C_e / (IC_{50} + C_e)$ (Eq. 6:54)

### C. Structural Necessity

Fick 분포 평형의 직접 결과: 두 구획 농도차 비례 mass transfer. $k_{e0}$ = 분포 시상수. 강제 가정: (1) 작용 부위 약물 외 동역학 없음, (2) plasma↔effect 선형 분포.

### D-E. Assumptions & Limitations

- **No baseline turnover** — 호르몬 회로(코르티솔)에 부적합.
- **No peak-shift** — 발생 시 turnover 전환.
- **Counter-clockwise hysteresis** 시그니처 (Case 6.6-C 동맥혈 solid line) — *동맥혈*이 effect *선행*이면 진짜 분포 지연, 정맥혈이 *후행*이면 metabolite/sampling artifact.
- 한계: saturable response (Hill로 dose-dependent peak-shift 불가), active metabolite 시 $C_e$가 metabolite 시간 코스를 빨아들여 메커니즘 가려짐.

### F-G. Cognitive Layers & Atom

| L | 내용 |
|---|---|
| **L1** | $dC_e/dt = k_{e0}(C_p - C_e)$ — 단일 first-order ODE. |
| **L2** | $C_e(t)$ = $C_p(t)$의 exponentially smoothed version. |
| **L3** | RC low-pass filter, exponential moving average — first-order delay 동형. |
| **L4** | 약물의 혈관→시냅스 후막 *물리적 이동*. BBB·tissue 침투. |
| **L5** | NONMEM `DADT(2) = KE0*(C - A(2))` 한 줄 + `EFFECT = A(2)`. |

```yaml
---
aliases: [Effect Compartment, Link Model, Biophase, ke0 model]
tags: [pharmacometrics/pd, model/link]
related: ["[[Peak-shift Directionality]]", "[[Hysteresis loop]]"]
source: "Gabrielsson & Weiner 5e, Ch.6, Eq. 6:5, 6:14, 6:19"
---
```

물리적 분포 지연만. $dC_e/dt = k_{e0}(C_p - C_e)$. Time-delay + no peak-shift 표준 답. CCW hysteresis 시그니처. 항상성 가정 없음.

<!-- ANCHOR -->
Effect compartment가 *물리적 지연*만이라면, §2.4 Turnover는 *생리적 항상성*과 *in/out 작용*을 더해 peak-shift도 만드는 더 일반적 framework.

---

## §2.4 — Turnover Model

> ### ━━ 거장의 시각 ━━
> <!-- MASTER LENS -->
>
> **왜 치명적으로 중요한가**: Ch.6 9개 케이스 중 6개(A/B/D/E/F/G/H)가 turnover 변형 — 임상 PD 모델링 작업말 70%. 어느 항에 약물 함수가 곱해지는가 = 약물 작용 메커니즘. 잘못 코딩 시 simultaneous multi-dose fit이 *수렴은 하지만* 메커니즘은 거꾸로.
>
> **체화해야 할 단 하나의 직관**: Turnover = *욕조 모델*. 수도꼭지(kin, 0차) + 배수구(kout·R, 1차). 약물은 둘 중 *하나*에만 손댄다.
>
> **이 직관을 머릿속에 박고 아래를 읽어라**: 두 작용점은 *대칭이 아니다* — in은 zero-order, out은 first-order. 이 비대칭이 좌/우 peak-shift 근원.

### A-B. Definition & 4 작용 모드

기본: $dR/dt = k_{in} - k_{out} \cdot R$. $R_0 = k_{in}/k_{out}$.

| 모드 | ODE | Peak-shift | 케이스 |
|---|---|---|---|
| **kin 억제** | $dR/dt = k_{in} I(C) - k_{out} R$ | 우향 → | Case G (Eq. 6:32) |
| **kout 자극** | $dR/dt = k_{in} - k_{out} R \cdot S(C)$ | 좌향 ← | Case B (Eq. 6:10, 6:17) |
| **kin 자극** | $dR/dt = k_{in} S(C) - k_{out} R$ | 우향 → | Case E (Eq. 6:23–24) |
| **kout 억제** | $dR/dt = k_{in} - k_{out} R \cdot I(C)$ | 좌향 ← (tsunami) | Case H (Eq. 6:34) |

`[출처: Gabrielsson 5e, Ch.6]`

### C. Structural Necessity

**4 모드 = 2 작용점 × 2 작용 방향**. 추가 변형:
- **Case I (Adaptation)**: 두 번째 inactive 구획 $R_i$ 추가, bi-phasic decline (Eq. 6:35).
- **Case 6.6-H**: $R_{low}$ 생리적 floor.

### D-E. Assumptions & Limitations

가정: baseline 시간 불변, 단일 작용점, linear plasma PK, 응답 1:1 transduction.
한계: bi-phasic decline은 두-구획 변형, 두 작용 동시 시 식별성 문제, Hill 채택은 saturation 검증 필수.

### F-G. Cognitive Layers & Atom

| L | 내용 |
|---|---|
| **L1** | 4 모드. 약물 함수가 곱해진 항이 작용점. |
| **L2** | $R(t)$는 *moving target*. 시상수 $1/k_{out}$ (kin 작용) vs $1/[k_{out}S(C)]$ (kout 자극) — 후자는 dose 의존. |
| **L3** | CSTR (chemical engineering), mortality/birth rate (population dynamics) 동형. |
| **L4** | kin = 호르몬 합성, 효소 발현, 적혈구 생성. kout = 분해, 제거, 사멸. |
| **L5** | NONMEM 한 줄 코드 차이. baseline IC: $R(t=0) = k_{in}/k_{out}$. |

```yaml
---
aliases: [Turnover Model, Indirect Response Model, IDR, Jusko model]
tags: [pharmacometrics/pd, model/turnover]
related: ["[[Peak-shift Directionality]]", "[[kin inhibition]]", "[[kout stimulation]]"]
source: "Gabrielsson & Weiner 5e, Ch.6, Cases A/B/D/E/F/G/H"
---
```

생리적 항상성 + 약물이 in/out 한 곳 작용. 4 모드 × peak-shift 방향 1:1. NONMEM 한 줄 차이 = 메커니즘 전체.

<!-- TRENCH -->
**Trench-Tip — 두 모드 분리 안 될 때**: dose ratio < 5배 또는 sparse nadir sampling 시 동일 OFV 수렴. **detection**: post-fit으로 peak-shift 방향 *예측*해 nadir dose-trend와 비교. 부호 불일치 = 잘못된 모드. **insertion**: 보고서 "두 모드 동등 적합, 추가 데이터 필요"로 안전 기술.

<!-- ANCHOR -->
좌향 분기에서 *다른 후보*는 receptor on/off (§2.5) — 형태 비슷하나 메커니즘·코드 다름 (§5.2 Critical Blow).

---

## §2.5 — Receptor On/Off Model

> ### ━━ 거장의 시각 ━━
> <!-- MASTER LENS -->
>
> **왜 치명적으로 중요한가**: GPCR 길항제, 항원-항체, 효소 저해제 — 고정 receptor 풀 점유 메커니즘. Turnover로 강제하면 *in vivo binding kinetics 정보 영구 소실*.
>
> **체화해야 할 단 하나의 직관**: 2차 결합 동역학 — $k_{on} \cdot C \cdot [R]$에서 농도와 free receptor 풀이 *직접 곱해짐*. 이 곱셈이 leftward peak-shift 근원.

### A-B. Definition & Derivation

핵심 ODE (Eq. 6:7, 6:11, 6:18, 6:27, 6:49):
$$\frac{d[RC]}{dt} = k_{on} \cdot C \cdot ([R_T] - [RC]) - k_{off} \cdot [RC]$$

응답: $E = E_0 - [RC]$ (antagonist) 또는 $E_0 + a \cdot [RC]$ (agonist).

정상상태: $[RC]_{ss} = R_T \cdot C / (C + K_D)$, $K_D = k_{off}/k_{on}$.

`[출처: Gabrielsson 5e, Ch.6, Eq. 6:11, 6:18, p.427, p.431]`

### C. Structural Necessity

**Leftward 이유**: 용량↑ → C↑ → first 항 $k_{on} \cdot C \cdot [R]$ 가속 → free receptor 풀 빨리 소진 → max binding 시간 단축.

vs Turnover kout 자극: peak-shift는 *시상수 dose 의존성*이지만, on/off는 *유한 풀 dose 의존 고갈 시간*에서 옴 — 데이터 유사하나 수학 다름.

### D-E. Assumptions & Limitations

가정 (가브리엘슨 p.431): (1) on/off가 distribution보다 느림, (2) receptor가 PK 영향 없음 (TMDD 아님), (3) 고정 $R_T$.
한계: multi-state binding, downregulation (long-term), TMDD overlap (high-affinity).

### F-G. Cognitive Layers & Atom

| L | 내용 |
|---|---|
| **L1** | 2차 결합 + 1차 해리. $K_D = k_{off}/k_{on}$. |
| **L2** | Phase plane에서 [RC] vs C dose-dependent 곡선, $R_T$ 직선 빠르게 접근. |
| **L3** | $A + B \rightleftharpoons AB$, Michaelis-Menten enzyme-substrate, Hill-Langmuir adsorption — 모두 동형. |
| **L4** | 시냅스 후막 receptor, 효소 활성 부위, 항체 결합 — 풀이 유한. |
| **L5** | NONMEM `DADT(2) = KON*C*(RT - A(2)) - KOFF*A(2)`. RT는 fix 또는 baseline에서 계산. |

```yaml
---
aliases: [Receptor On/Off, Occupancy Model, kon-koff Model]
tags: [pharmacometrics/pd, model/binding]
related: ["[[Turnover Model]]", "[[Peak-shift Directionality]]", "[[TMDD]]"]
source: "Gabrielsson & Weiner 5e, Ch.6, Cases A/B/C/F"
---
```

고정 receptor 풀 + 2차 결합 + 1차 해리. $E = E_0 \pm [RC]$. Leftward는 dose↑로 $R_T$ 풀 빨리 고갈. $K_D = k_{off}/k_{on}$. 가정: binding < distribution speed + receptor가 PK 영향 없음.

<!-- ANCHOR -->
§2.1–§2.5는 *어떤 모델 구조*. §2.6은 그 구조를 *특정 환자 데이터에 적합* — Bayesian. Stage 1의 두 번째 정상이며, Stage 2·3 결합 지점.

---

## §2.6 — Bayesian Objective Function (PK35)

> ### ━━ 거장의 시각 ━━
> <!-- MASTER LENS -->
>
> **왜 치명적으로 중요한가**: 모든 임상 TDM 소프트웨어가 출력하는 개인 파라미터 추정값은 *이 단일 식의 최소화 결과*. 식의 두 합 항이 어떻게 균형 잡는지 모르면, 소프트웨어 출력의 Cl이 모집단에 *고집스럽게 머무는지* 데이터에 *과민 반응*하는지 해석 불가 → 잘못 해석한 출력으로 환자 처방.
>
> **체화해야 할 단 하나의 직관**: Bayesian LS = *두 사람의 합의*. 모집단 prior는 "평균에 가까울 것"이라 주장, 데이터 likelihood는 "이 환자는 다르다"라 주장. 합의 결과 = *각자 자신감(분산 역수) 가중 평균*.
>
> **이 직관을 머릿속에 박고 아래를 읽어라**: PK35의 Cl 추정값 5.7 L·h⁻¹가 모집단 1.8의 *3배*가 된 이유는, 두 농도 데이터가 모집단보다 더 많은 "확실성"을 제공해서다.

### A. Formal Definition

환자 PK 파라미터 $\hat{P}$ 추정 시, 모집단 prior $P_{pop}$와 관측 농도 $C_{obs}$를 분산 가중 결합한 손실 함수. 최소화 = MAP estimate.

### B. 핵심 식 + 세 극단 케이스

(Eq. 35:1, 35:5):
$$\text{Bayes}(LS) = \sum \frac{(P_{pop} - \hat{P})^2}{\text{var}(\hat{P})} + \sum \frac{(C_{obs} - \hat{C})^2}{\text{var}(\hat{C})}$$

PK35 명시 (Eq. 35:5):
$$\text{Bayes}(LS) = \sum \frac{(Cl_{pop} - \hat{Cl})^2}{\text{var}(\hat{Cl})} + \sum \frac{(V_{pop} - \hat{V})^2}{\text{var}(\hat{V})} + \sum \frac{(C_{obs} - \hat{C})^2}{\text{var}(\hat{C})}$$

`[출처: Gabrielsson 5e, Ch.35, Eq. 35:1, 35:5, p.641, p.643]`

예측 모델 (Eq. 35:2): $\hat{C}(t) = (D/V) e^{-(Cl/V) t}$.

| 케이스 | 조건 | 결과 |
|---|---|---|
| **(1) 농도 없음** | $\hat{C}$ 항 평가 불가 → 둘째 합 제거 | $\hat{P} \to P_{pop}$ |
| **(2) 사전 없음** | $\text{var}(\hat{P}) \to \infty$ → 첫째 합 0 | $\hat{P} \to$ MLE |
| **(3) 둘 다** | 두 합 유한 | Full Bayesian |

### B-2. PK35 임상 사례 수치

55세, 60kg 남성, CHF, Lanoxicap 0.2 mg/일 정상상태:
- $C_1 = 2.5$ µg·L⁻¹ at $t = 458$ h, $C_2 = 0.9$ µg·L⁻¹ at $t = 479$ h
- $Cl_{pop} = 1.8$ L·h⁻¹, var $\propto 3.24$
- $V_{pop} = 500$ L, var $\propto 250{,}000$
- 초기: $V = 350$ L, $Cl = 2$ L·h⁻¹

**최적화 결과**:
- $\hat{Cl} = 5.7$ L·h⁻¹ (모집단 ~3.2배)
- $\hat{V} = 119.6$ L (모집단 ~24%)
- $t_{1/2} = 0.693 \cdot 119.6 / 5.7 = 14.5$ h

**가브리엘슨 p.643 해석**: V 모집단 일탈 이유 = 환자 낮은 체중 (60 kg) — digoxin V는 체중 강한 상관. 모집단 평균 자체가 *biased*였고, 두 농도가 그 bias 교정.

### B-3. Conditional Prior — Stage 2 확장 (Sheiner Digoxin)

<!-- ANCHOR -->

PK35의 $Cl_{pop} = 1.8$, $V_{pop} = 500$은 **flat prior**. R&T Ch.15 Table 15-7 Sheiner 공식은 **conditional prior** — $CL_{cr}$·CHF severity로 조건화.

| CHF | $CL$ (L·h⁻¹·kg⁻¹) | $V$ (L·kg⁻¹) |
|---|---|---|
| Mild | $CL_{cr} + 0.048$ | $3.8 + 52 \cdot CL_{cr}$ |
| Severe | $0.9 \cdot CL_{cr} + 0.02$ | $3.8 + 52 \cdot CL_{cr}$ |

`[출처: R&T 5e, Ch.15, Table 15-7; orig. Sheiner LB et al. *J Pharmacokinet Biopharm* 1977;5:445–479]`

**PK35 환자에 적용한 역계산** (60 kg, mild CHF):
- $\hat{Cl} = 5.7$ → 0.095 L·h⁻¹·kg⁻¹ → $CL_{cr} \approx 0.047$ L·h⁻¹·kg⁻¹ ≈ 47 mL·min⁻¹ (≈40 mL/min for 60kg)
- $\hat{V} = 119.6$ → 1.99 L·kg⁻¹ → $CL_{cr} \approx -0.035$ (음수, **불가능**)

**진단**: PK35의 ($\hat{Cl}$, $\hat{V}$) 쌍이 Sheiner mild CHF 공식과 *내부 불일치*. V가 Sheiner 예측 최저값($CL_{cr}=0$일 때 228 L)보다도 작음.

**두 해석**:
1. PK35 flat prior가 *과도하게 헐거워* (var(V) ∝ 250,000) likelihood가 prior 무시하고 *물리적 부적절 V로 수렴*. → conditional prior 사용 시 V가 그 하한에 anchored되어 합리적 추정.
2. Severe CHF 또는 *uremia 동반 신부전*. R&T p.464: "Digoxin distributes much less extensively to tissues in uremia, resulting in a smaller volume of distribution and a shorter half-life than that predicted from loss of renal function." → Sheiner 1977 자체가 부적합, 더 최신 covariate model 필요.

<!-- TRENCH -->
**임상 함의**: 모집단에서 멀리 떨어진 추정값일 때 — (a) 환자 진실 특이성 vs (b) prior 헐거워 데이터에 끌려간 결과 — *conditional prior 평가* 없으면 구별 불가. **TDM 소프트웨어 구축자 관점**: Sheiner 1977은 NONMEM 직접 조상 — 첫 covariate 모집단 PK. 현대 TDM은 모두 conditional prior 보유. *prior 정당성 평가 능력*이 §2.6 핵심 확장.

### B-4. TCS 적용 *전*과 *후*의 Bayesian 정확도 — Stage 3 확장

<!-- ANCHOR -->

PK35는 *2개 농도 데이터* 기반. 임상 현실에서 TCS 적용 *전*(첫 dose)과 *후*(농도 측정 후) 추정 정확도가 *질적으로 다르다*. R&T Ch.18 Fig. 18-13의 confidence-in-estimates가 정량화.

**TCS 적용 *전* (initial dose)**:
- 농도 없음 → §5.3 Case 1: $\hat{P} \to P_{pop}$
- Flat prior + 평균 환자 → 비교적 정확
- Flat prior + 특수군 (신부전, CHF, 노인) → **체계적 bias** (PK35 V 과대추정 위험)
- Conditional prior + 정확 covariate → 가장 정확
- **결정**: 가능한 covariate 최대 활용 conditional prior로 시작.

**TCS 적용 *후* (1–2점 농도 측정 후)**:
- §5.3 Case 3: full Bayesian
- 정확도는 *데이터 점 수*와 *측정 timing*에 의존:

R&T Fig. 18-13 confidence pattern:

| Sample timing (환자 t1/2) | 정보 우선 | 임상 함의 |
|---|---|---|
| < 1 t1/2 | $V$ (peak/distribution) | Loading dose 검증. CL 거의 추정 불가. |
| 2–3 t1/2 | 모호 (V·CL 모두 영향) | 권장 회피. |
| 4+ t1/2 (steady state) | $CL$ (최대 정확도) | Maintenance 결정. |

**4+ t1/2 sampling이 CL 최적인 이유**: $\bar{C}_{ss} = F \cdot \text{Dose}/(CL \cdot \tau)$는 *V 무관*. Bayesian 합 항에서 $\bar{C}_{ss}$ 데이터가 *직접 CL 제한*.

**Stage 1·2·3 통합 기준점**: TCS 적용 후 conditional prior + 정상상태 농도 결합 시 — Sheiner 같은 covariate model이 *상한·하한*, 농도 데이터가 *그 범위 내 환자별 최적값* → flat prior 단독 또는 데이터 단독 대비 *비대칭적* 정확도 향상.

<!-- TRENCH -->
**Phase 4 RMP**: TCS 약물(digoxin·vancomycin·cyclosporine) post-marketing concentration data 수집 시, 각 농도 점의 *t1/2 ratio* 함께 기록 → Fig. 18-13 confidence weights 적용 → 부정확 timing 데이터 가중치 감소.

### C. Structural Necessity

식이 정확히 이 형태인 이유: 정규분포 사후분포 negative log:
$$\log p(P|D) \propto \log p(P) + \log p(D|P)$$
정규분포 가정 하 $-\log p(P|D) \propto \frac{(P_{pop} - P)^2}{2 \text{var}(P)} + \frac{(C_{obs} - \hat{C}(P))^2}{2 \text{var}(C)}$ — 정확히 Eq. 35:1.

### C-2. 자주 발생하는 misuse

"농도 1점이면 Bayesian 의미 있다" — 실제 **1점 + 2모수 = underdetermined**. var($\hat{Cl}$)가 매우 작지 않으면 추정값이 모집단 머묾. PK35가 *2점*을 사용한 이유: Cl·V 동시 식별. 한 점은 $Cl/V$만 알려주고, 두 점이 있어야 분리.

### D-E. Assumptions & Limitations

가정: 모집단 정규분포 (실제 log-normal 흔함), 측정 오차 정규분포, var calibration 신뢰성, steady state.
한계: sparse data + tight prior → 사전이 데이터 덮음 (가장 흔한 함정), 모집단 prior의 wrong patient (특수군), identifiability (모수 ≤ 데이터 점).

### F-G. Cognitive Layers & Atom

| L | 내용 |
|---|---|
| **L1** | 정규분포 사후분포 negative log. 두 합 항 분산 가중. |
| **L2** | 파라미터 공간 두 등고선 교점 = MAP. var 비율 = 등고선 크기. |
| **L3** | 가중 평균 $\hat{P} = w_{pop} P_{pop} + w_{data} P_{MLE}$. Kalman filter, ridge regression 동형. |
| **L4** | 모집단 일반 지식 + 환자 측정 = 신뢰도 가중 합의. 임상의 직관 + 검사 결합 동형. |
| **L5** | NONMEM `$ESTIMATION METHOD=POSTHOC` 또는 ETA 추정 = Bayesian MAP. 모든 임상 TDM 엔진. |

```yaml
---
aliases: [Bayesian Least Squares, MAP, Maximum A Posteriori]
tags: [pharmacometrics/estimation, bayesian, gabrielsson/pk35, tdm]
up: "[[개인 파라미터 추정 MOC]]"
related: ["[[Population PK]]", "[[MLE]]", "[[NONMEM POSTHOC]]",
          "[[TDM Software]]", "[[Conditional Prior]]", "[[TCS]]"]
source: "Gabrielsson & Weiner 5e, PK35, Eq. 35:1, 35:5"
---
```

정규분포 사후 negative log. 두 합: prior + likelihood, 분산 역수 가중. 세 극단: 농도 없음 → 모집단; 사전 없음 → MLE; 둘 다 → full Bayes. PK35 사례: Cl 5.7 vs 모집단 1.8. NONMEM POSTHOC = MAP. **Stage 3**: TCS 적용 *전*(prior만)과 *후*(data 결합) 정확도 비대칭 — Fig. 18-13으로 timing 가중.

<!-- TRENCH -->
**Trench-Tip — 분산 calibration 검증**: 출력 추정값이 모집단에 *너무 가까운* 경우 var($\hat{P}$) 과소; *너무 튀는* 경우 var($\hat{C}$) 과소. **detection**: var($\hat{P}$) ±50% sensitivity. **insertion**: 보고서 "var ±50%에 추정값 ±X% 변화" 명시.

<!-- ANCHOR -->
PK15는 별도 카드 없이 §1·§7·§8에서 *적용 사례*로 인용. NCA·안전역은 Step 2 §6.


---

## §2.7 — Rd Framework: 신질환 PK 변동의 정량 분해 [⚡ Apex Concept #3]

<!-- MASTER LENS -->

**한 줄 요약**: 신부전 환자 unbound clearance = $RF \cdot f_e + (1-f_e)$ — 두 독립 인자(약물 fe·환자 RF) 곱셈+덧셈. 이 분해 없이는 신부전 dose 조정이 *왜 어떤 약물에 필요하고 어떤 약물에 불필요한지* 설명 불가.

### A. Formal Definition

**Eq. 15-7 (full)**:
$$R_d = \frac{CL_u(d)}{CL_u(t)} = RF \cdot f_e(t) + [1 - f_e(t)] \cdot \frac{(140 - \text{Age}) \cdot \text{Wt}(d)^{0.75}}{1936}$$

**Eq. 15-8 (simplified, 60세·70 kg)**:
$$R_d = RF \cdot f_e(t) + 1 - f_e(t)$$

- $RF = CL_{cr}(d) / CL_{cr}(t)$ (Eq. 15-13)
- $f_e(t) = CL_{uR}(t) / CL_u(t)$ (Eq. 15-9)
- 표준: 60세, 70 kg, $CL_{cr}(t) \approx 70$ mL·min⁻¹

**Maintenance dose (Eq. 15-17)**: $(D_M/\tau)_d = R_d \cdot (D_M/\tau)_t$

**Half-life ratio (Eq. 15-10/11)**: $t_{1/2}(d)/t_{1/2}(t) = [V_u(d)/V_u(t)] \cdot (1/R_d)$

### B. Derivation — 왜 *덧셈*인가

총 unbound CL = 신·비신 합:
- $CL_{uR}(d) = RF \cdot f_e(t) \cdot CL_u(t)$ (Eq. 15-3, 가정 1: 신청소율 RF 비례)
- $CL_{uNR}(d) = [1 - f_e(t)] \cdot CL_u(t)$ (Eq. 15-4, 가정 2: 비신 CL 신질환 무관)

두 항 더하고 $CL_u(t)$로 나누면 Eq. 15-8.

**Fig. 15-8 직관**: $R_d$ vs $RF$ 직선. 기울기 = $f_e(t)$, y절편 = $1 - f_e(t)$.

### B-2. Stage 3 추가 — Loading Dose에 RF 적용 vs 미적용

<!-- ANCHOR -->

**핵심 분기**: *Maintenance는 RF 비례 조정, Loading은 대부분 RF 무관*.

- **Maintenance 목표**: $\bar{C}_{ss} = F \cdot \text{Dose}/(CL_u \cdot \tau)$ 유지. $CL_u$ 가 $R_d$ 비율 감소 → dose 같은 비율 감소.
- **Loading 목표**: 즉시 target 도달. $D_L = V \cdot C_{target}/F$ — *V만* 등장.

**V는 RF에 영향받는가?** R&T Ch.15 일반 (p.464): "Volume of distribution is generally not greatly affected by renal function impairment." → LD 일반적으로 RF 보정 *불필요*.

**예외 — Digoxin uremia (R&T p.464)**: "Digoxin distributes much less extensively to tissues in uremia, resulting in a smaller volume of distribution and a shorter half-life than that predicted from loss of renal function." Uremia에서 V 60–80% 수준 → LD도 같은 비율 감소. **§5.5 핵심 함정**: 이것이 maintenance·loading 모두 RF로 조정하는 *유일 예외*.

| 약물 유형 | Maintenance | Loading dose |
|---|---|---|
| 일반 신배설 ($f_e > 0.30$) | $\times R_d$ | 조정 불필요 |
| 일반 간대사 ($f_e < 0.30$) | 조정 불필요 (30% 규칙) | 조정 불필요 |
| **Digoxin uremia** | $\times R_d$ | **V 감소 비율 (~0.6–0.8×)** |

### C. Structural Necessity — fe·RF 분리의 가치

**fe (약물 속성 — NCA에서 결정, 라벨 명시) vs RF (환자 속성 — 매 결정 시 Cockcroft-Gault)**.

이 분리 덕에 임상 약사는 *어떤 환자에 대해서도* 라벨 fe + 곱셈 한 번으로 dose 조정. 분리되지 않은 결합 형태였다면 매 약물·매 환자 별도 임상시험 필요.

**Fig. 15-9A heat map**: $f_e \to 1$ + $RF \to 0$일 때 $R_d$ 최소 → *최대 dose 감소 영역*. 두 조건 중 하나만 충족하면 영향 약화.

### C-2. The 30% Rule (R&T p.462)

> "Except for drugs with very low therapeutic indices, a reduction of less than 30% in the dosing rate, based on a change in renal function alone, is probably unwarranted... as long as $f_e(t) \le 0.30$ and the metabolites are inactive, no change in a regimen is called for, based on renal function, regardless of the function. Similarly, if renal function is 0.70 or more of the typical value, no change is needed."

- $f_e(t) \le 0.30$ → 조정 불필요
- $RF \ge 0.70$ → 조정 불필요
- 두 조건 모두 위배 시에만 조정 검토.

### D-E. Assumptions & Limitations

| 가정 | 위배 시 |
|---|---|
| $CL_{uNR}$ 신질환 무관 | Imipenem (신장 brush-border 대사, Fig. 15-15), 단백질 약물 |
| 신청소율 $CL_{cr}$ 비례 (unit nephron) | Michaelis-Menten 신배설, 활성 분비-재흡수 비대칭 |
| 활성 대사체 없음 | Morphine→M6G — 대사체 신배설 별도 평가 (R&T Ch.20) |
| F 신질환 무관 | 드물게 위배 (R&T p.463) |
| 단백 결합이 CL 비율에 영향 없음 | unbound 식이라 영향 없음, 단 total 해석 시 주의 (Phenytoin $f_u$ 0.1→0.25) |
| **V 신질환 무관** (Stage 3) | **Digoxin uremia 예외** (R&T p.464) |

한계: 간질환(Child-Pugh 비단일 framework, Fig. 15-3 효소 차등 영향), CHF (Sheiner conditional 공식 외 보편 framework 없음), concurrent disease (PK35의 신부전+CHF).

### F-G. Cognitive Layers & Atom

| L | 내용 |
|---|---|
| **L1** | $R_d$ = fe·RF 곱셈+덧셈 분해. |
| **L2** | fe(약물)·RF(환자) 출처 분리. |
| **L3** | 30% 규칙 — 조정 대상 약물 분류. |
| **L4** | $CL_{uNR}$ 가정 위배 (imipenem, 단백질 약물). |
| **L5** | NONMEM `$PK CL = THETA(1) * (RF**THETA(2)) * ...` covariate model. |

```yaml
---
aliases: [Rd Framework, renal disease unbound clearance ratio, unit nephron hypothesis]
tags: [pharmacometrics/disease, renal, dose-adjustment, rowland-tozer/ch15]
up: "[[신질환 dose 조정 MOC]]"
related: ["[[Cockcroft-Gault]]", "[[fraction excreted unchanged]]",
          "[[30% Rule]]", "[[Sheiner Digoxin]]", "[[Loading Dose]]",
          "[[Digoxin Uremia Exception]]"]
source: "Rowland & Tozer 5e, Ch.15, Eq. 15-7/15-8/15-13/15-17"
---
```

$R_d = RF \cdot f_e + 1 - f_e$. fe(약물)·RF(환자) 분리. 30% 규칙. 위배: imipenem, M6G. **Stage 3**: LD 무보정 일반 원칙, digoxin uremia 유일 예외.

---

## §2.8 — Cockcroft-Gault & RF 정량화

<!-- MASTER LENS -->

**한 줄 요약**: 환자 4개 수치(나이·체중·성별·SCr)로 $CL_{cr}$ 계산 → RF 변환. Rd framework 입력 단계.

### A. Formal Definition

**Cockcroft-Gault (R&T Table 15-5, mg/dL SCr)**:
- 남: $CL_{cr}$ (mL/min) = $(140 - \text{Age}) \cdot \text{Wt} / (72 \cdot \text{SCr})$
- 여: × 0.85

**Schwartz (children)**: $CL_{cr}$ (mL/min/1.73 m²) = Factor·Height/SCr
- 미숙아~1세: 0.33; 만삭~1세: 0.43; 소아·청소년 여: 0.55; 청소년 남: 0.70

**RF**: $CL_{cr}(d) / CL_{cr}(t)$, $CL_{cr}(t) \approx 70$ mL/min (남 ~74, 여 ~66, 평균 70).

### B. Derivation — SCr만으로 충분 이유

정상 정상상태: 크레아티닌 *생성률 = 청소율* → $\text{SCr} = \text{Production rate}/CL_{cr}$ (Eq. 15-12). 생성률 = 근육량 비례 → 나이·체중·성별로 1차 근사. SCr 단독은 근육량 정보 누락 → Cockcroft-Gault가 보정.

### C. Structural Necessity

이상적: 24h 소변 수집 직접 측정. 임상 현실: 부정확 빈발 (R&T p.456 "incomplete urine collection... underestimate"). SCr 단독 측정은 무료에 가깝고 즉시 가용 → *덜 정확하지만 가용한* 추정이 표준.

### C-2. Plausible Fallacy — 비만·근감소·노년·AKI

R&T Table 15-5 footnote: "Poor estimates are obtained for patients who are obese or emaciated."

| 환자 유형 | C-G 예상 | 실제 |
|---|---|---|
| **비만** (체중↑, 근육량↑) | $CL_{cr}$ 과대 | 지방조직 비생산 → 진짜 $CL_{cr}$ 낮음 |
| **근감소** (와상, 심한 신부전) | SCr 정상 같아 과대 | 생성률↓ → SCr 낮은 채로 → 신기능↓ 미반영 (R&T p.460: "1–2 mg/dL/day rise instead of 3 mg/dL/day") |
| **노인 (>80세)** | 표준 적용 | reliable, frailty/sarcopenia 시 과대 |
| **임신부** | 표준 부적용 | GFR 변화 큼, 별도 보정 |
| **AKI (Fig. 15-11)** | 정상상태 가정 위배 | SCr 선형 상승, 현재 $CL_{cr}$ 미반영 (R&T Eq. 15-14, turnover ~8.8 h) |

**탐지**: BMI, frailty score, lean body mass. 의심 시 24h $CL_{cr}$ 또는 cystatin C.

### D-E. Assumptions & Limitations

가정: 정상상태, 표준 근육량, $CL_{cr} \ne$ GFR (~15–20% 더 큼, R&T p.455).
한계: MDRD/CKD-EPI는 ml/min/1.73m² (체중 보정 별도), cystatin C 표준화 진행 중.

### F-G. Cognitive Layers & Atom

| L | 내용 |
|---|---|
| **L1** | 4 수치로 $CL_{cr}$. |
| **L2** | $CL_{cr}(t) = 70$ mL/min 정규화. |
| **L3** | 비만/근감소/AKI 정확도 급락 — 항상 의심. |
| **L4** | MDRD 단위 변환, 단백 결합 변화 unbound 청소율 해석. |
| **L5** | NONMEM 시간 의존 covariate $CL_{cr}(t)$, 또는 SCr·Age·Wt ETA·THETA 분리. |

```yaml
---
aliases: [Cockcroft-Gault, RF, renal function ratio]
tags: [pharmacometrics/disease, renal, covariate]
related: ["[[Rd Framework]]", "[[Schwartz formula]]", "[[MDRD]]", "[[AKI]]"]
source: "Rowland & Tozer 5e, Ch.15, Table 15-5; Cockcroft & Gault 1976"
---
```

남: $CL_{cr} = (140-\text{Age}) \cdot \text{Wt}/(72 \cdot \text{SCr})$, 여: ×0.85. 비만·근감소·AKI 부정확. AKI 시 SCr 선형 상승.

---

## §2.9 — Hemodialysis 보충 용량

<!-- MASTER LENS -->

**한 줄 요약**: Dialysis가 *임상적으로 의미 있는지* + *보충 용량 얼마* — 세 정량 기준. "투석되는가"가 아니라 "투석으로 *몸의 의미 있는 분율이 제거되는가*".

### A. Formal Definitions

**Dialysis blood clearance (Eq. 15-18)**:
$$CL_{bD} = (Q_{b,in} C_{b,in} - Q_{b,out} C_{b,out}) / C_{b,in}$$

또는 dialysate 회수 (Eq. 15-21, 가장 정확):
$$CL_{bD} = V_D \cdot C_D / AUC_{b,in}(0-\tau)$$

**Fraction via dialysis (Eq. 15-29)**: $f_D = CL_{uD}/(CL_u + CL_{uD})$

**Fraction lost during τ (Eq. 15-28)**: $1 - e^{-k_D \tau}$, $k_D = (CL_u + CL_{uD})/V_u$

**Body amount removed (Eq. 15-30)**: $\boxed{f_D \cdot (1 - e^{-k_D \tau})}$

**Supplemental dose (Eq. 15-34)**:
$$D_{\text{supp}} = V \cdot C(0) \cdot (e^{-k \tau} - e^{-k_D \tau})$$

### B. Derivation — 두 인자 곱

투석 τ 동안 제거 분율 = 두 분리 사건 곱:
1. 그 시간 동안 어떤 분율이 나가는가 — $1 - e^{-k_D \tau}$
2. 나간 양 중 dialysate에 포함되는가 — $f_D$

두 조건 *모두* 성립해야 임상적 제거. **Half-life 단축만으로 불충분** (R&T p.472, phenobarbital: half-life 137h → 5.7h, 24× 단축, 그러나 3h 투석 29%만 제거).

### C. Structural Necessity — Fig. 15-18 두 차원

| 조건 | 의미 |
|---|---|
| $V_u < \sim 120$ L | 분포 작아 plasma compartment에 가까움 — dialyzer 도달 가능 |
| $CL_u < CL_{uD}$ | 자체 CL 낮아 dialyzer가 의미 있는 비중 |

둘 중 하나 위배 → 4h 투석 < 20% 제거.

### C-2. Hemodialysis vs CAPD

- **Hemodialysis**: dialysate 연속 갱신 → sink 유지. $CL_{uD}$ 일정. 일반 dialyzer creatinine 청소율 80–200 mL/min, drug $CL_{uD}$ 그 이하. High-flux 더 큼.
- **CAPD**: dialysate 복강 고임 (dwell 4–6h). 농도 평형 → 효과 감소. $CL_{uD}$ 2–7 mL/min. *임상 약물 제거 미미*. 하지만 dialysate에 약물 첨가 i.p. 투여 (gentamicin 2 mg/L → 144 L · 2 mg/L = 288 mg, R&T p.474).

### D-E. Assumptions & Limitations

가정: $V_u, CL_u, CL_{uD}$ 시간 무관, 1구획, $C_{b,in}$ 정확, hematocrit 변화 무시 (~3 L 손실).
위배: 단백 결합 변화·rebound (vancomycin 다구획), high-efficiency dialyzer 측정 변동성.
확장: high-flux (vancomycin MW 1448 제거 가능, R&T p.488 Bohler 1992), hemoperfusion (활성탄), CAPD i.p. (dwell time bioavailability, Fig. 15-22).

### F-G. Cognitive Layers & Atom

| L | 내용 |
|---|---|
| **L1** | $f_D$ × $(1-e^{-k_D\tau})$ = 진짜 제거 분율. |
| **L2** | half-life 단축 ≠ 임상적 제거. 두 조건 평가. |
| **L3** | Eq. 15-34로 보충 용량 계산. |
| **L4** | High-flux/hemoperfusion/CAPD, post-dialysis rebound. |
| **L5** | NONMEM time-varying CL: `IF(DIAL.EQ.1) CL = CL + CLD`. |

```yaml
---
aliases: [hemodialysis dosing, dialysis clearance, supplemental dose]
tags: [pharmacometrics/disease, dialysis, hemodialysis]
related: ["[[Rd Framework]]", "[[CAPD]]", "[[High-flux Membrane]]"]
source: "Rowland & Tozer 5e, Ch.15, Eq. 15-29/15-30/15-34"
---
```

$f_D = CL_{uD}/(CL_u + CL_{uD})$. 제거 = $f_D \cdot (1-e^{-k_D\tau})$. 보충 = $V \cdot C(0) (e^{-k\tau} - e^{-k_D\tau})$. 두 조건: $V_u<120$L AND $CL_u<CL_{uD}$. Half-life 단축 ≠ 임상 제거.


---

## §2.10 — Target Concentration Strategy (TCS) 적용 조건 [⚡ Apex Concept #4 — Stage 3]

> ### ━━ 거장의 시각 ━━
> <!-- MASTER LENS -->
>
> **왜 치명적으로 중요한가**: TCS는 *모든 저치료지수 약물에 자동 적용되는 도구가 아니다* — 5개 criteria 모두 충족되는 약물에서만 임상적 가치가 있다. Warfarin 같이 PD 변동성이 우세한 약물에 TCS를 적용하면 plasma concentration 측정 비용·시간이 *임상 의사결정에 기여 없이* 소비된다. 반대로 5개 criteria 모두 충족하는 약물(digoxin, vancomycin, cyclosporine, phenytoin)에 TCS를 *적용하지 않으면* 환자 개인성을 반영하지 못한 처방으로 독성 또는 효능 부전.
>
> **체화해야 할 단 하나의 직관**: TCS는 *PK 변동성이 PD 변동성보다 크고 측정 가능할 때*만 의미 있다. 두 조건 중 하나라도 깨지면 TCS는 임상적 무가치하거나 오해 부른다. R&T Table 18-2가 이 trade-off의 핵심.
>
> **이 직관을 머릿속에 박고 아래를 읽어라**: 5개 criteria는 무관한 체크리스트가 아니라 *한 가지 핵심 질문* — "농도를 측정하면 처방이 달라지는가?" — 의 단계별 분해.

### A. Formal Definition

환자 개인 plasma drug concentration을 정기·체계 측정하여, 측정값을 *prior 모집단 PK 정보*와 결합해 individual PK 파라미터 추정 → *target concentration window* 도달·유지하는 dose 조정 framework. R&T Ch.18 pp. 594–606.

**5 적용 Criteria (R&T Ch.18)**:
1. **Good Concentration-Response Relationship** — 농도가 효과 강도/확률과 정량 상관.
2. **High Probability of Therapeutic Failure** — 좁은 치료역 + PK 변동성 + 유전 + 동반 질환 + drug interaction (R&T Ch.13/15/17 통합).
3. **When a Problem Arises** — 정상 dose에서 효능 부족/독성 시 — 비순응·생체이용률·빠른 elimination·PD resistance 구별 도구.
4. **Population Pharmacokinetic Information Available** — prior 분포 알려져 있어야 Bayesian 가능.
5. **Reliable Assay** — 민감·정확·specific + *next clinical decision 전 turn-around* (보통 t1/2 정도).

### B. Derivation — 5 Criteria의 *논리 사슬*

```
[1] 농도가 효과를 예측하는가? ── NO → TCS 무가치 (warfarin: PD 변동성 우세)
                           └ YES → ↓
[2] 치료 실패 가능성 *충분히* 높아 모니터링 비용 정당화? ── NO → 일반 처방
                           └ YES → ↓
[3] 임상 문제 발생 또는 위험 큼? ── Reactive: "Problem 시만"
                                └ Prophylactic: 정기 측정
[4] Prior 분포 알려져 있는가? ── NO → 측정값 단독 해석 (제한적)
                            └ YES → MAP estimation (§2.6)
[5] Assay turn-around 가능? ── NO → TCS 운영 불가 (정보 outdated)
                            └ YES → TCS 적용
```

5 모두 충족: digoxin, vancomycin, cyclosporine, phenytoin, theophylline (R&T Table 18-5).

### B-2. PK vs PD 변동성 분류 (R&T Table 18-2)

| PK | PD | TCS 가치 | 사례 |
|---|---|---|---|
| 높음 | 높음 | 전면 모니터링 — biomarker 없으면 약물 비유용 | 드뭄 |
| 낮음 | 낮음 | 모니터링 불필요 — 표준 dose | 표준 항생제 |
| 낮음 | 높음 | **PD 모니터링** 필수, plasma 무가치 | **Warfarin (INR)** |
| **높음** | **낮음** | **TCS 매우 유용** | **Phenytoin, Digoxin, Vancomycin** |

R&T Fig. 12-4: warfarin은 unbound S-warfarin 농도 같아도 INR 환자별 차이 → PD 우세.
R&T Fig. 18-8: phenytoin은 within-patient PK 안정 + between-patient PK 변동성 큼 + PD 변동성 작음 → TCS 정확히 그 사분면.

### C. Structural Necessity — 왜 5개

5 criteria = §2.6 Bayesian 식 입력 4개 + 임상 운영 1개:
- C1 (concentration-response) = $\hat{C}$ 약리학적 의미 (likelihood)
- C2 (high failure prob) = TCS 비용-편익 정당화 (variance 가치)
- C3 (when problem) = TCS 작동 모드 (proactive vs reactive)
- C4 (population PK info) = $P_{pop}$, var($\hat{P}$) 가용성 (prior 항)
- C5 (reliable assay) = $C_{obs}$, var($\hat{C}$) 가용성 (likelihood 항) + 시의성

5 criteria = §2.6 식의 *임상 가용성*으로 번역.

### C-2. Plausible Fallacy — TCS 항상 적용

> **Misuse**: "저치료지수 → TCS 적용해야".
>
> **반례 — Warfarin**: 좁은 치료역, fatal — 그러나 plasma concentration 측정은 임상 결정 거의 안 바꿈. PD 변동성(VKORC1·CYP2C9, vitamin K, 동반 질환) 압도적. INR target window가 *concentration이 아니라 INR 자체로* 정의됨.
>
> **나비효과**:
> 1. Warfarin plasma concentration 측정 비용 지속.
> 2. 측정 vs INR 불일치 → 임상 혼란.
> 3. concentration 따라 dose 조정 → INR target 벗어남 → 부작용.
> 4. Post-marketing 규제 부담 증가.
>
> **GOF 시그니처 — "Concentration vs Endpoint disconnect"**: 동일 환자 농도 ±30% vs INR ±100% 변동 → TCS *signal noise보다 작음*.

### D-E. Assumptions & Limitations

- **Linear PK in target range** — phenytoin nonlinear은 *추가 모니터링 사유*.
- **Stable PD over time** — tolerance/sensitization 시 같은 농도 다른 효과 (nitroglycerin).
- **Single active species** — 활성 metabolite 시 모물질만 측정 underestimate (nortriptyline → 10-OH).
- **Adherence 가정** — 비순응 시 측정값 history 불일치 → §2.12 framework 검증.

한계:
- Pharmacogenomic variability (CYP2D6, HLA, TPMT) — 그룹별 conditional prior 권장.
- Drug interactions (phenytoin + valproic acid) — prior 재선정.
- Active metabolite (cyclosporine).
- Free vs total concentration (uremia·surgery·displacing drug).

### F-G. Cognitive Layers & Atom

| L | 내용 |
|---|---|
| **L1** | 5 criteria → §2.6 Bayesian 입력 가용성. |
| **L2** | PK·PD 변동성 4사분면 (Table 18-2). |
| **L3** | Warfarin (PD 우세 무가치) vs Phenytoin (PK 우세 + nonlinear 필수) 패턴 인식. |
| **L4** | 활성 metabolite (nortriptyline 10-OH), 단백 결합 변화 (uremia phenytoin) 보정. |
| **L5** | TDM 소프트웨어 운영 — prior 선정, var calibration, output sensitivity. |

```yaml
---
aliases: [TCS, Target Concentration Strategy, TDM, plasma concentration monitoring]
tags: [pharmacometrics/clinical, tdm, dose-individualization, rowland-tozer/ch18]
up: "[[임상 의사결정 MOC]]"
related: ["[[Bayesian Objective Function]]", "[[Conditional Prior]]",
          "[[Therapeutic Window]]", "[[PK vs PD Variability]]",
          "[[Pharmacogenomics]]", "[[Loading Dose]]"]
source: "Rowland & Tozer 5e, Ch.18, pp.594–606, Tables 18-2/18-5/18-6"
---
```

5 criteria: ① concentration-response, ② high failure prob, ③ when problem, ④ population PK info, ⑤ reliable assay. PK 변동성 우세 + PD 낮음 = TCS 최적. Warfarin = PD 우세 INR로 충분. Phenytoin·digoxin·vancomycin·cyclosporine·theophylline·nortriptyline = TCS 필수. §2.6 Bayesian 입력 *임상 가용성*.

<!-- TRENCH -->
**Trench-Tip — TCS 1분 분류**: ① therapeutic window 알려져 있나? (Y=1점) ② PD biomarker 측정 가능 + PK보다 신뢰? (N=1점, Y면 PD 우선) ③ CL inter-patient CV% > 30%? (Y=1점). 3점=강력 추천, 2점=case-by-case, ≤1점=비효율.

<!-- ANCHOR -->
§2.10이 *적용 조건*이라면, §2.11은 *처음 처방하는 dose* — Loading dose. R&T Ch.18에서 가장 임상적인 한 쌍.

---

## §2.11 — Loading Dose 결정 원칙

<!-- MASTER LENS -->

**왜 치명적으로 중요한가**: 응급 약물(esmolol, lidocaine), 고지속성 약물(amiodarone, digoxin)에서 LD 부족 시 *target까지 4–5 t1/2 소요* → 환자가 효과 없는 시기 거치고, 과량 시 즉시 독성. 이 결정은 *입원 첫 6시간 안*이며, TCS *전*에 결정 → 농도 데이터 없이 *prior에만 의존*.

**체화해야 할 단 하나의 직관**: Maintenance = *시간당 들어가는 양 = 시간당 청소되는 양* (CL 의존). Loading = *분포 부피를 단번에 채워 target 달성* (V 의존). **두 결정의 변수가 다르다 — CL은 환자별 크게 변동, V는 비교적 well-defined.** 따라서 LD 추정 confidence가 maintenance보다 *항상 높다*.

**이 직관을 머릿속에 박고 아래를 읽어라**: LD 결정 3축 = *urgency*, *half-life*, *PD time course*.

### A. Formal Definition

정상상태 dosing 시작 전, target 농도 즉시 달성 위해 maintenance보다 큰 양을 단일·분할 투여하는 dose. R&T Ch.18 pp. 584–586.

핵심 식:
$$D_L = \frac{V \cdot C_{target}}{F}$$

또는 plateau 누적 amount 기준:
$$D_L = \frac{F \cdot \text{Dose}_{maint}}{1 - e^{-k\tau}}$$

(single-dose plateau accumulation factor 적용)

### B. Derivation — 왜 V 의존

**Maintenance**: $\bar{C}_{ss} = F \cdot \text{Dose}/(CL \cdot \tau) \to \text{Dose} = \bar{C}_{ss} \cdot CL \cdot \tau / F$ — **CL 의존**.

**Loading (IV bolus 모델)**: $C(0) = D_L \cdot F / V$. Target 달성: $C_{target} = D_L \cdot F / V \to D_L = V \cdot C_{target} / F$ — **V 의존**.

**왜 CL이 LD에 없나?** Loading 목표는 *순간 도달*. 그 순간 CL 작용 시간 = 0 → CL 무관. 시간 흐르며 CL 작용 → 농도 감소 → maintenance가 *손실 대체*.

### B-2. Confidence in V vs CL (R&T Fig. 18-5)

R&T Fig. 18-5의 pie chart:
- **F**: 95% well-defined (oral bioavailability)
- **V**: 55% body weight + 25% age + 10% renal function + 10% other = covariate로 *대부분 설명*
- **Hepatic clearance**: 60% **unexplained** + 20% body weight + 15% age + 5% renal — *unidentified factors* 60% 가장 큼

**임상 함의**:
- LD 추정: **V에 weight·age·SCr 적용 → 5–10% 정확도** 가능
- Maintenance 추정: **CL에 동일 covariate → 30–40% 정확도**

따라서 *prior 단독*으로 처방 결정 시 LD가 maintenance보다 *항상* 더 신뢰성 높음.

### C. Structural Necessity — 3축 결정 트리

```
[Axis 1] Urgency 있나?
  ├ YES (esmolol VT, lidocaine arrhythmia) → LD 필수, IV bolus
  │   esmolol t1/2 = 9 min, 30 min 기다리면 VT 지속
  │
  └ NO  → ↓
[Axis 2] Half-life ≥ 24h (편의 dosing interval) 인가?
  ├ YES (amiodarone t1/2 50–60일, digoxin 36h)
  │   → LD 권장 — 4–5 t1/2 = days–weeks 소요
  │   예: mefloquine 1250 mg 단일 LD = 전체 치료 (t1/2 3주, no maintenance)
  │   예: chloroquine 2500 mg 분할 LD (1000 → 500/6-8h → 500×2일)
  │       — 단일 2500 mg 시 부작용 (headache, drowsiness, cardiovascular collapse)
  │
  └ NO (t1/2 < 12h, τ = 8–12h)
   → 자연 누적 4–5 t1/2 = 1일 → LD 불필요
            
[Axis 3] PD response가 PK보다 *느린가*?
  ├ YES → LD 무의미 (alendronate Fig. 18-7 — bone density 6–12 months, bisphosphonates 더 길어)
  │       항우울제, statin, antihyperlipidemic — therapeutic response weeks–months
  │
  └ NO  → LD 효과 즉시 발현 → 의미 있음
```

### C-2. Available Dose Strengths 제약

이론 LD를 *상용 product strengths*에 mapping. 예: warfarin 1·2·2.5·5·7.5·10 mg, simvastatin 5·10·20·40·80 mg, digoxin 0.125·0.25·0.5 mg. 보통 strengths 차이 *2배*. Half-tablet (scored)도 제한. 임상 처방 = *이론 LD 가장 가까운 단위로 round*.

### D-E. Assumptions & Limitations

가정: linear PK in target range, V 추정 정확 (covariate 충실 적용), 환자 *분포 평형 도달 시간*이 LD timing보다 빠름 (IV 즉시), bioavailability F 가정 정확.
한계:
- **Distribution kinetics** — 다구획 모델에서 LD 후 초기 피크가 V_central 기준이 아닌 V_total에 도달하기 전 *과도한 농도* 발생 (R&T Ch.19, digoxin 후 초기 피크 6h, R&T Ch.18 Table 18-7 Fig 18-12 참고).
- **Dose-limited adverse events** — 단일 큰 LD 시 즉각 부작용 (chloroquine 분할 이유).
- **Bioavailability 변동** — oral LD는 F 변동 시 target 미도달 (digoxin tablets vs capsules vs elixir, Table 18-7).

### F-G. Cognitive Layers & Atom

| L | 내용 |
|---|---|
| **L1** | $D_L = V \cdot C_{target}/F$. V 의존. |
| **L2** | V는 covariate(weight·age·RF)로 5–10% 정확도, CL은 30–40%. |
| **L3** | 3 축 (urgency · half-life · PD time course). |
| **L4** | Distribution kinetics, dose-limited AE, oral F 변동 보정. |
| **L5** | 임상 처방: 이론 LD → available strengths round. |

```yaml
---
aliases: [Loading Dose, LD, Priming Dose]
tags: [pharmacometrics/clinical, dosing, rowland-tozer/ch18]
up: "[[임상 의사결정 MOC]]"
related: ["[[TCS]]", "[[Maintenance Dose]]", "[[Multiple-Dose Regimens]]",
          "[[Distribution Kinetics]]", "[[Digoxin Uremia Exception]]"]
source: "Rowland & Tozer 5e, Ch.18, pp.584–586"
---
```

$D_L = V \cdot C_{target}/F$. V 의존 — covariate로 well-defined. 3 축: urgency·half-life·PD time course. Available strengths round. R&T Fig. 18-5: V 90% 설명, CL 40%. Distribution kinetics·dose-limited AE 주의.

<!-- TRENCH -->
**Trench-Tip — IV bolus 후 distribution peak 회피**: 다구획 분포 약물(digoxin)은 LD IV 후 6h 이내 *V_central 기준 초기 피크*가 V_total 기준 target보다 높음. 임상 운영: digoxin LD 분할 (각 ~0.25 mg q6h × 3 = total 0.75 mg) 또는 IV 천천히 5–10 min infusion. R&T Table 18-7 elderly 1–1.5 mg in divided doses 권장.

<!-- ANCHOR -->
§2.10·§2.11이 *initial dose 처방*을 다룬다면, §2.12는 *그 이후* — missed dose, erratic dosing, 비정형 임상 시나리오를 정량 평가하는 framework.

---

## §2.12 — Missed Dose · 9-13-17-21 · Erratic Dosing 수식 framework

<!-- MASTER LENS -->

**왜 치명적으로 중요한가**: TDM 환자의 80%가 *완벽한 정상상태 fixed-interval regimen이 아니다* — missed dose, "9-13-17-21" 병원 schedule, erratic 간격. 이 framework 없이는 측정 농도값과 *정상상태 prediction의 disconnect*를 해석할 수 없으며, 비순응을 "환자 PK가 다르다"로 잘못 진단하여 dose adjustment 오류.

**체화해야 할 단 하나의 직관**: Multiple-dose 농도의 어느 시점이든 *과거 모든 dose의 superposition*이다. 각 dose가 IV bolus 모델로 단독 기여한 농도를 *그 시점까지 시간*으로 decay시켜 합산. *Missed dose는 0 mg dose*로 합산에서 빠짐. *Erratic dose는 각각 다른 양·시간*으로 동일한 합산.

**이 직관을 머릿속에 박고 아래를 읽어라**: 4개 식(Eq. 18-1 ~ 18-4)은 모두 같은 superposition을 *임상 시나리오별 형태*로 풀어쓴 것.

### A. Formal Definitions — 4 식

(R&T Ch.18 pp. 600–606, IV bolus + 1구획 가정)

**Eq. 18-1 — 한 dose missed**:
$$C_{ss}(t) = \frac{F \cdot \text{Dose}}{V} \cdot \left[\frac{e^{-kt}}{1 - e^{-k\tau}} - e^{-kt}\right]$$

(첫 항: missed 안 했을 때 정상상태 농도. 둘째 항: missed dose가 단독 기여했을 농도 *제거*.)

**Eq. 18-2 — 두 consecutive doses missed** (둘째가 $t_2$ 전):
$$C_{ss}(t_2) = \frac{F \cdot \text{Dose}}{V} \cdot \left[\frac{e^{-kt_2}}{1 - e^{-k\tau}} - e^{-kt_1} - e^{-kt_2}\right]$$

**Eq. 18-3 — 9-13-17-21 (4 daily doses, unequal intervals)**:
$$C_{ss}(t_{\text{eval}}) = \frac{F \cdot \text{Dose}}{V} \cdot \frac{e^{-kt_1} + e^{-kt_2} + e^{-kt_3} + e^{-kt_4}}{1 - e^{-k\tau}}$$

($\tau = 24$ hr 일일 cycle, $t_i$ = 각 dose 후 sampling 시점까지 시간)

**Eq. 18-4 — Erratic dosing**:
$$C(t) = \frac{F}{V} \cdot \sum_i \text{Dose}_i \cdot e^{-k t_i}$$

(각 dose 별 dose·기간 다름. 4 doses 이상은 *4 t1/2 이전 dose 무시* 가능 — 잔류 < 6%.)

### B. Derivation — Superposition 원리

핵심: **선형 PK에서 multiple dose 농도는 single-dose 농도들의 합**.

각 dose를 IV bolus로 단독 가정하면:
- Dose_i가 단독 시 t시점 농도: $(F \cdot \text{Dose}_i / V) e^{-k(t-t_i^{\text{dose}})}$
- 여러 dose 합산: $C(t) = \sum_i (F \cdot \text{Dose}_i / V) e^{-k(t-t_i^{\text{dose}})}$

정상상태 fixed-interval은 무한 등비급수 합 → $1/(1-e^{-k\tau})$ 인자.

Missed dose = 합산에서 그 한 항만 제거. Erratic = 각 항이 *다른 dose·다른 시간*.

### B-2. Worked Examples (R&T Ch.18 직접 인용)

**Digoxin 두 missed dose (R&T p.602)**:
- 60세, 70 kg 남성, $CL_{cr} = 75$ mL/min, daily 0.25 mg tablet
- $F = 0.8$, $V = 226 + 298 \cdot 75/(29+75) = 441$ L
- $CL$ (CHF present, R&T Table 18-7 footnote c) = $1.3 \cdot 75 + 20 = 117.5$ mL/min ≈ 7.05 L/hr
  *(또는 footnote d: $0.33 \cdot 70 + 0.9 \cdot 75 = 91$ mL/min ≈ 5.46 L/hr)*
- $k$ = $5.46/441$ = 0.0123 hr⁻¹ ≈ 0.3 day⁻¹
- 마지막 missed dose 24h 후 sampling, 두 consecutive missed:
$$C(t_2) = 0.8 \cdot \frac{250}{441} \cdot \left[\frac{e^{-0.0123 \cdot 48}}{1 - e^{-0.0123 \cdot 24}} - e^{-0.0123 \cdot 24} - e^{-0.0123 \cdot 48}\right] = 0.39 \text{ µg/L}$$
- 결과: **0.39 µg/L** — 치료 범위(0.8–2.0 µg/L) *아래* → 임상적 부족.

**Vancomycin 9-13-17-21 (R&T p.603)**:
- 5세, 20 kg, $CL_{cr} = 55$ mL/min
- $F = 1.0$, $V = 0.7 \cdot 20 = 14$ L
- $CL = 8.45 \cdot (20/70)^{0.75} = 3.3$ L/hr (또는 $CL_{cr} = 55$ mL/min = 3.3 L/hr)
- $k = 3.3/14 = 0.24$ hr⁻¹
- 250 mg q9-13-17-21, sampling 8:00 (다음날, 9:00 dose 1h 전):
- 9-15-21-3 q6h: $C(8:00) = 1.0 \cdot (250/14) \cdot e^{-0.24 \cdot 5}/(1 - e^{-0.24 \cdot 6}) = 7.1$ mg/L (정상범위)
- 9-13-17-21: $C(8:00) = 1.0 \cdot (250/14) \cdot (e^{-0.24 \cdot 23} + e^{-0.24 \cdot 19} + e^{-0.24 \cdot 15} + e^{-0.24 \cdot 11})/(1 - e^{-0.24 \cdot 24}) = 2.03$ mg/L
- 결과: **2.03 mg/L** — 치료 범위(5–15 mg/L) *아래* → 9-13-17-21이 trough에서 ineffective.

**Vancomycin Erratic (R&T p.604)**:
- 68 kg, 60세 남성, atrial fib, SCr 2.2 mg/dL
- $CL_{cr} = (140-60) \cdot 68 / (72 \cdot 2.2) = 34$ mL/min = 2.06 L/hr
- $V = 0.62 \cdot 68 = 42.2$ L, $k = 2.06/42.2 = 0.049$ hr⁻¹
- Dose history: Feb 22 9:00 (500 mg), 17:00 (1000 mg), 24:00 (1000 mg), Feb 23 8:00 (500 mg). Sample 13:00 → 34 mg/L.
- Predict: $C = (1.0/42.2) \cdot (500 \cdot e^{-0.049 \cdot 28} + 1000 \cdot e^{-0.049 \cdot 20} + 1000 \cdot e^{-0.049 \cdot 13} + 500 \cdot e^{-0.049 \cdot 5}) = 33.7$ mg/L
- 결과: **34 (관측) vs 33.7 (예측)** — 일치 → 환자 PK 표준 모집단 합치, dose 감량 필요.

### C. Structural Necessity — Confidence in Estimates (Fig. 18-13)

R&T Fig. 18-13: infusion 시작 시점부터 plateau까지의 농도가 *언제 sampling하는가*에 따라 V vs CL 구별 능력이 다름:
- **< 1 t1/2**: 대부분 V만 영향. CL 변동 차이 거의 없음 → V 추정에 좋음.
- **2 t1/2**: 모호 — 동일 농도를 *V 증가* 또는 *CL 감소*로 양쪽 설명 가능.
- **4+ t1/2 (plateau)**: $C_{ss}$만 보면 *CL만* 결정 (V 무관) → CL 추정에 가장 좋음.

**임상 함의**:
- Missed/Erratic 데이터 해석 시 *각 농도가 마지막 dose로부터 몇 t1/2*인지 확인 → 정보 추출 가능 파라미터 제한.
- 1 t1/2 이내 농도 → V 검증 (LD 적절성).
- 4+ t1/2 → CL 추정 (maintenance 적절성).
- 2 t1/2 부근 → 추가 정보 부족, sampling 권장 회피.

### C-2. Forgiving vs Unforgiving Drugs

R&T p.591 + Table 18-4:

| Forgiving | Unforgiving |
|---|---|
| t1/2 ≫ τ (amiodarone 50–60일, phenobarbital 4일) | t1/2 ≪ τ (esmolol 9 min — 지속 infusion) |
| Response가 long-lived (statin, bisphosphonate) | Antimicrobial/antiviral (resistance emergence) |
| Missed dose 영향 미미 | Missed dose → therapeutic failure |

**Doubling-up (Fig. 18-10)**: dose 빈도 작을수록 (once-daily) doubling 위험 큼. 8h regimen에서 doubling은 peak ~2배 (안전 mostly), once-daily에서 doubling은 peak 2배 → 부작용 위험 ↑.

### D-E. Assumptions & Limitations

가정: linear PK (1구획 + IV bolus 근사), F 일정, 모든 dose history 정확 기록, 환자 비순응이 시뮬레이션 외 다른 형태 아님.
한계:
- **Multi-compartment distribution** — IV bolus 가정 부정확 (digoxin distribution peak 6h, R&T Ch.19).
- **Non-linear PK** — phenytoin 같은 경우 superposition 위배.
- **Dose history 부정확 기록** — 환자 자가 보고 부정확.
- **Active metabolite contribution** — 모물질 농도만으로 부족.
- **Time-varying parameters** — 신기능 급격 변화, drug interaction 추가/제거 시 superposition 부정확.

### F-G. Cognitive Layers & Atom

| L | 내용 |
|---|---|
| **L1** | Eq. 18-1~18-4 = superposition 다른 형태. |
| **L2** | 각 dose의 IV bolus 단독 농도 합. Missed = 그 항 제거. |
| **L3** | Sample timing이 V vs CL 정보 결정 (Fig. 18-13). |
| **L4** | Forgiving (long t1/2, persistent response) vs Unforgiving (short t1/2, antimicrobial). |
| **L5** | TDM 보고서 — 관측 vs 예측 비교, ±20% 이내면 환자 PK 표준; 이외면 PK 변동 또는 비순응 의심. |

```yaml
---
aliases: [Missed Dose, Erratic Dosing, 9-13-17-21 Regimen, Superposition]
tags: [pharmacometrics/clinical, tdm, dosing, rowland-tozer/ch18]
up: "[[임상 의사결정 MOC]]"
related: ["[[Multiple-Dose Regimens]]", "[[Adherence]]", "[[TCS]]",
          "[[Confidence in Estimates]]", "[[Forgiving Drugs]]"]
source: "Rowland & Tozer 5e, Ch.18, Eq. 18-1/18-2/18-3/18-4, pp.600–606"
---
```

선형 PK + 1구획 IV bolus의 superposition. 4 식 = 시나리오별 형태. Worked: digoxin 2 missed → 0.39 µg/L (sub-therapeutic), vancomycin 9-13-17-21 → 2.03 mg/L (sub), erratic → 34 vs 33.7 (일치). Sample timing이 V·CL 정보 결정 (Fig. 18-13). Forgiving vs unforgiving. 한계: multi-compartment, non-linear, time-varying.

<!-- TRENCH -->
**Trench-Tip — 관측 vs 예측 disconnect 진단**: 측정값이 예측보다 50% 낮으면 — (a) 비순응 (1+ 누락) (b) 빠른 elimination (PK 변동) (c) 흡수 저하 (oral bioavailability 변동). 의무기록·약물 dispensing record 확인이 비순응 식별 유일 방법. *Sample timing*이 4 t1/2 plateau 시 CL 변동 의심, < 1 t1/2 시 LD/V 변동 의심. 50% 높으면 — (a) makeup dose, (b) drug interaction (CL 감소), (c) PK 변동.


---

# §5 — Confusion Pair Dissection

## §5.1 — Effect Compartment vs Turnover (Time-delay + No Peak-shift 분기)

<!-- CONFUSION -->

| 비교 차원 | Effect Compartment | Turnover |
|---|---|---|
| **표면적 유사성** | 둘 다 plasma peak 후 effect peak 늦음. 단일 dose 거의 구별 불가. | |
| **수식 형태** | $dC_e/dt = k_{e0}(C_p - C_e)$, $E = f(C_e)$ | $dR/dt = k_{in}(\cdot I) - k_{out} R(\cdot S)$ |
| **물리적 지시체** | 약물 *분포 지연* (혈관→tissue) | 응답 *합성/분해 항상성*에 약물 끼어듦 |
| **Baseline 처리** | $E_0$ 외부 add (fitted constant, 의미 없음) | $R_0 = k_{in}/k_{out}$ 시스템 도출 (생리적 항상성) |
| **용량↑ 시** | 같은 $t_{\max}^E$, 단순 *높아짐* | *위상 이동* (peak-shift) |
| **임상 결과** | Turnover 데이터를 EC로 fit → peak-shift signal 잔차 갇힘 → over-prediction | EC 데이터를 turnover로 fit → kin·kout 의미 없음, simulation 왜곡 |
| **⚡ 기억 고리** | **EC = *물리학*(Fick 분포), Turnover = *생리학*(항상성). 회복 단계 baseline 회귀 = turnover. plasma decay 추종 = EC.** | |

**진단 규칙**: 다용량 데이터에서 peak-shift 없으면 EC 우선. 분명하면 Turnover/Receptor on/off. Saturation 검증은 Hill 함수 채택, 모델 클래스 영향 없음.

---

## §5.2 — kout Stimulation vs kin Inhibition (Peak-shift 방향) ← **🔥 Critical Blow**

<!-- CONFUSION -->

| 비교 차원 | kout Stimulation (좌향 ←) | kin Inhibition (우향 →) |
|---|---|---|
| **표면적 유사성** | 둘 다 baseline → nadir → 회복 V자. **저용량 거의 동일**. | |
| **수식** | $dR/dt = k_{in} - k_{out} R \cdot S(C)$, $S(C) = 1 + S_{\max}C^n/(SC_{50}^n+C^n)$ | $dR/dt = k_{in} I(C) - k_{out} R$, $I(C) = 1 - I_{\max}C^n/(IC_{50}^n+C^n)$ |
| **생리적 지시체** | 분해 효소 *활성화* → 응답 *빨리 사라짐* | 합성 효소 (COX, HMG-CoA) 또는 분비 *차단* → 공급 끊김 |
| **Peak-shift** | 시상수 $1/[k_{out}S(C)]$ 단축 → **좌향** | $I(C)\to 1-I_{\max}$ 지속, R은 자연 분해만 → **우향** |
| **회복 형태** | Wash-out 후 정상 $1/k_{out}$ 복귀 — *대칭 V자* | 시상수 항상 $1/k_{out}$ — *비대칭 J자* (좌측 길고 우측 정상) |
| **임상 결과** | kin 억제로 잘못 fit → SC50을 IC50로 → in vivo target *분해 효소 inhibitor* 헛수고 | kout 자극으로 잘못 fit → IC50을 SC50로 → *합성 효소 activator* 헛수고 |
| **⚡ 기억 고리** | **시상수 약물 농도와 *결합* 시 좌향 (out 측 곱). 시상수 *고정* 시 우향 (in 측은 자연 분해 좌우). "약물이 시간 척도 빠르게 만들면 곡선 왼쪽으로 끌려간다"** | |

| **🔥 치명적 타격** | 이 혼동을 NDA 제출하면, FDA Clinical Pharmacology 심사관은 (1) 제안 메커니즘 in vitro와 in vivo population PK/PD 모델 *서로 다른 작용점 가리킴* 발견 → (2) **"Mechanistic inconsistency between in vitro pharmacology and population PK/PD model"** Deficiency Letter. 추가 in vivo dose-escalation 데이터 요구 → 라벨링 confidence interval 넓어짐 → 첫 출시 dose recommendation *과도하게 보수적* → 약효 underestimation으로 commercial impact. Phase 3 종료 후 발견 시 NDA 재제출 ~6–12개월 지연. |

**Trench 검증**: 두 모델 *모두* simultaneous multi-dose data fit + OFV·visual GOF·peak-shift 방향 예측치 3중 비교. ΔOFV < 3.84 (df=1, p=0.05) 시 분리 불가 — 추가 데이터 요구 보고서 명시.

---

## §5.3 — Bayesian "농도 없음" vs "사전정보 없음" 극단 (TDM 출력 해석)

<!-- CONFUSION -->

| 비교 차원 | Case 1: 농도 없음 | Case 2: 사전 없음 (var($\hat{P}$) → ∞) |
|---|---|---|
| **표면적 유사성** | 둘 다 Bayes(LS) 한 합 항 *사라지는* 극단. TDM 소프트웨어가 명시 구별 안 함. | |
| **수식** | $\text{Bayes}(LS) = \sum (P_{pop}-\hat{P})^2/\text{var}(\hat{P})$ — 첫째만 | $\text{Bayes}(LS) \approx \sum (C_{obs}-\hat{C})^2/\text{var}(\hat{C})$ — 둘째만 |
| **추정값** | $\hat{P} = P_{pop}$ (모집단 그대로) | $\hat{P} = \hat{P}_{MLE}$ (데이터만) |
| **임상 상황** | 치료 *시작 전* 초기 용량 (혈중 농도 측정 전) | 모집단 prior가 *그 환자에게 부적합* (특수군: 신부전, 간경변, CHF) |
| **신뢰도** | 모집단 평균이 *그 환자에 적용 가능한가*에 의존. 평균 환자 OK, 특수군 위험. | *충분한 데이터 점*에 의존. 1점 underdetermined, 2점부터 Cl·V 분리 (PK35). |
| **임상 결과** | Case 1을 Case 3로 오인 → "환자 개인성 반영" 잘못 보고 → 실제 모집단 그대로 | Case 2를 Case 3로 오인 → "사전이 보호" 잘못 보고 → 실제 noise 과민 |
| **⚡ 기억 고리** | **Case 1 = *지도만 있고 GPS 없음*. Case 2 = *GPS만 있고 지도 없음*. Case 3 (full Bayes) = 둘 다. Case 1을 Case 3로 부르는 것 = "현재 위치를 도시 평균으로 보고", Case 2를 Case 3로 부르는 것 = "GPS noise만 의지".** | |

**TDM 소프트웨어 체크리스트**:
1. 입력 prior var가 *그 환자 그룹에 calibrated*?
2. 농도 점 수가 모수 수의 *최소 동일* 또는 이상?
3. 출력이 prior 평균과 거의 같으면 → Case 1 가까움 → 개인성 미반영 의심.
4. 출력 신뢰구간 매우 넓으면 → Case 2 가까움 → 데이터 부족.

→ Stage 3 (R&T Ch.18)에서 이 체크리스트가 *TCS 적용 조건*과 직접 결합 (§2.10).

---

## §5.4 — Hepatic High-E (Verapamil) vs Renal-Excreted (Cefetamet)

<!-- CONFUSION -->

**왜 함정인가**: "환자에 질환 → 약물 노출 증가"라는 *느슨한 직관*은 옳을 때도 있고 *정반대로 틀릴 때*도 있다. 정확한 진술은 **질환 종류 × 약물 청소 경로**의 매트릭스로 기술.

**구체 데이터 (R&T Table 15-1, p.446)**:

| 약물 | $f_e$ | 청소 경로 | 간경변 시 변화 |
|---|---|---|---|
| **Cefetamet** | 0.85 | 신배설 | F: 0.45→0.50, CL: 7.7→7.5, $f_u$: 0.82→0.85, $t_{1/2}$: 2.4→2.4 — **변화 없음** |
| **Meptazinol** | < 0.05 | 간대사 (high-E) | F: 0.07→0.28 (**4배**), CL: 83→72, $t_{1/2}$: 2.7→4.2 |
| **Verapamil** | < 0.05 | 간대사 (high-E) | F: 0.22→0.52 (**2.4배**), CL: 76→37 (**½**), $f_u$: 0.10→0.16, $t_{1/2}$: 3.7→14.2 (**4배**) |

**같은 환자(간경변)·다른 약물 → 정반대**:
- Cefetamet 무영향 — 신배설 + 단백 결합 약함 + 신질환 동반 없음.
- Verapamil 모든 파라미터 변화 — high-E 간대사 + 알부민 결합 → 간경변 hepatocellular activity↓ + portacaval shunt → F 급증, CL 급감.

**같은 약물(verapamil)·다른 질환**:
- 간경변: F↑, CL↓, $t_{1/2}$↑↑↑
- 신부전: 거의 무영향 ($f_e < 0.05$, 30% 규칙 충족)

**Verapamil vs Cefetamet 매트릭스**:

| 변동 *원인* | Verapamil 간경변 | Cefetamet 신부전 |
|---|---|---|
| F 증가 | 1차 통과↓ + portacaval shunt | (해당 없음) |
| CL 감소 | hepatic enzyme/perfusion ↓ | unit nephron (filter+secrete+reabsorb 동시↓) |
| 정량 framework | Child-Pugh (불완전) | $R_d = RF \cdot f_e + 1-f_e$ 정량 정확 |
| 30% 규칙 적용 | ✗ (Child-Pugh 단일 임계값 부재) | ✓ ($f_e \le 0.30$ → 조정 불필요) |

<!-- TRENCH -->
**Trench-Tip**: 의사가 "신부전 환자에 verapamil 감량 필요?"라 물으면, $f_e < 0.05$ 근거 "30% 규칙으로 조정 불필요" 답이 카리브레이션. 그러나 같은 환자가 cefetamet 받으면 "조정 필요" — *환자 같아도 약물에 따라 답 갈림*.

→ Stage 3 (Ch.18)에서 이 매트릭스가 *TCS 적용 조건* + *initial dose 선정* 결정에 직접 들어감 (예: vancomycin 신부전 환자 LD 조정 vs maintenance 조정 분리).

---

## §5.5 — Maintenance Dose 조정 vs Loading Dose 조정 (Stage 3 NEW)

<!-- CONFUSION -->

**왜 함정인가**: 신부전 환자에 dose 조정할 때 — *maintenance와 loading을 같은 비율로 조정하는가, 아니면 다르게 조정하는가?* 임상 약사가 가장 자주 마주치는 분기점이며, 잘못 조정하면 정상상태 도달 시간이 *몇 배 늘어나거나* 즉각 독성.

| 비교 차원 | Maintenance Dose 조정 | Loading Dose 조정 |
|---|---|---|
| **목표 metric** | 정상상태 평균 농도 $\bar{C}_{ss}$ 유지 | 즉시 target 농도 도달 |
| **계산 변수** | $\bar{C}_{ss} = F \cdot \text{Dose}/(CL \cdot \tau) \to \text{Dose} \propto CL$ — **CL 의존** | $D_L = V \cdot C_{target}/F$ — **V 의존** |
| **신부전 보정 (Rd framework)** | $\times R_d = RF \cdot f_e + 1-f_e$ (CL 감소 비율) | **일반적으로 무보정** — V는 RF에 거의 무관 |
| **간경변 보정 (high-E)** | $\times CL_{lc}/CL_t$ — Child-Pugh 가이드 | F 증가 시 LD *오히려 감소* (oral 투여) |
| **추정 confidence (R&T Fig. 18-5)** | CL은 covariate로 30–40% 설명 — **추정 confidence 낮음** | V는 covariate로 90% 설명 — **추정 confidence 높음** |
| **임상 결과** | Maintenance 잘못 조정 → 정상상태 농도 ±50% 편차 → 만성 효과 부전 또는 독성 | LD 잘못 조정 → *첫 6시간 내* 즉각 독성 또는 효과 미발현 |
| **⚡ 기억 고리** | **Maintenance는 *수도꼭지 흐름량* (시간 단위로 들어가는 양 = 나가는 양). Loading은 *욕조 부피 채우기* (단번에 V 채워 target 도달). 수도꼭지는 *환자별 변동 큼* (CL 30–40% confidence), 욕조 부피는 *비교적 정해짐* (V 90% confidence). 따라서 LD prior 추정이 maintenance보다 *항상* 정확.** | |

| **유일 예외 — Digoxin Uremia (R&T p.464)** | "Digoxin distributes much less extensively to tissues in uremia, resulting in a smaller volume of distribution and a shorter half-life than that predicted from loss of renal function." Uremia 환자 V 60–80% 수준 → **LD도 V 감소 비율로 보정 필수**. 이것이 maintenance·loading *둘 다* RF로 조정해야 하는 *유일* 케이스. 이 예외를 모르고 "LD는 V 의존이니 RF 무관"으로만 처방하면 **첫 6시간 digoxin 독성 (시야장애·부정맥)**. |

**임상 운영 분기**:

```
환자 신부전 (RF = 0.4) + Vancomycin 처방
  │
  ├ Maintenance: typical 1g q12h × R_d = 1g × 0.41 ≈ 410 mg q12h
  │   (R_d = 0.4 · 0.95 + 0.05 = 0.41)
  │
  └ Loading: 25 mg/kg × 70 kg = 1750 mg (or 15-25 mg/kg) — RF *무보정*
      → V (70kg) ≈ 0.62 · 70 = 43 L 변화 없음
      → target 25–30 mg/L 즉시 도달

대조: 환자 신부전 (RF = 0.4) + Digoxin (uremia 동반!) 처방
  │
  ├ Maintenance: typical 0.25 mg/일 × R_d = 0.25 × 0.72 ≈ 0.125 mg/일
  │   (R_d = 0.4 · 0.7 + 0.3 = 0.58 ~ 0.72 — Sheiner 공식 적용 시)
  │
  └ Loading: typical 1 mg × 0.7 (uremia V 감소) ≈ 0.7 mg in divided
      → uremia V ~ 60–80% 표준 → LD도 동등 비율 감소
      → 단순 RF 보정만으로 부족 — *uremia 특이 V 감소* 추가 보정
```

**Stage 1·2 carry-forward**: §7 Q11에서 PK35 환자(CHF + 추정 신부전 동반)의 $\hat{V} = 119.6$ L가 Sheiner mild CHF 공식 예측 V 하한(228 L)보다도 작다는 분석 → 이 환자는 **uremia 동반 가능성** → *이 §5.5 매트릭스의 right column 적용 대상*. Q13에서 이 가능성을 *Loading dose 결정으로 carry-forward*.

<!-- RECAP -->
**§5 흐름 요약 (Stage 1·2·3 누적)**: 5 혼동쌍은 의사결정 사슬의 5 지점에 위치 — (5.1) 모델 클래스 함정, (5.2) 메커니즘 방향 함정 [Critical Blow], (5.3) 추정 단계 사전·데이터 균형, (5.4) 질환·약물 PK 변동 *방향성* 매트릭스, **(5.5) 임상 의사결정 단계 — Maintenance vs Loading 조정 분기 + Digoxin uremia 유일 예외**. 이 다섯 함정을 *동시에* 운영하는 능력이 임상 약리학자의 핵심 카리브레이션.


---

# §7 — Self-Test: Active Recall Module

<!-- SELF-TEST -->

### Q1 [회상, ★★]
Turnover model 4 작용 모드(kin↑·kin↓·kout↑·kout↓) 각각 (a) ODE 한 줄, (b) peak-shift 방향 30초 안에 재현.

> **정답**:
> - kin 억제: $dR/dt = k_{in} I(C) - k_{out} R$ — **우향 →**
> - kin 자극: $dR/dt = k_{in} S(C) - k_{out} R$ — **우향 →**
> - kout 자극: $dR/dt = k_{in} - k_{out} R \cdot S(C)$ — **좌향 ←**
> - kout 억제: $dR/dt = k_{in} - k_{out} R \cdot I(C)$ — **좌향 ← (tsunami)**
>
> 패턴: **약물 함수 곱해진 항이 in측이면 우향, out측이면 좌향**.
>
> 다음 깊이: kin·kout 모두 작용 시 식별성 문제 어떻게 발생?

### Q2 [회상, ★★]
PK35 Bayesian objective function 전체식 + 세 합 항이 페널티화하는 것 한 줄씩.

> **정답**:
> $$\text{Bayes}(LS) = \sum \frac{(Cl_{pop}-\hat{Cl})^2}{\text{var}(\hat{Cl})} + \sum \frac{(V_{pop}-\hat{V})^2}{\text{var}(\hat{V})} + \sum \frac{(C_{obs}-\hat{C})^2}{\text{var}(\hat{C})}$$
>
> - 첫째: Cl 모집단 일탈 페널티 (분산 역수 가중)
> - 둘째: V 모집단 일탈 페널티
> - 셋째: 예측 농도 vs 관측 농도 페널티
>
> 다음 깊이: 모집단 prior가 wrong patient group이면 첫·둘째 항이 옳은 추정을 *방해*하는 메커니즘?

### Q3 [회상, ★]
Effect compartment ODE + 응답 함수 두 줄. Peak-shift 방향?

> **정답**:
> $$\frac{dC_e}{dt} = k_{e0}(C_p - C_e), \quad E = E_0 + \frac{E_{\max}C_e^n}{EC_{50}^n + C_e^n}$$
> Peak-shift: **없음** (linear PK 가정 하). Dose-dependent peak-shift 데이터에 부적합.
>
> 다음 깊이: Hill $n$ 매우 클 때 EC가 약한 peak-shift 모방?

### Q4 [회상, ○]
Receptor on/off ODE + $K_D$를 $k_{on}$·$k_{off}$로 표현. Leftward 이유 한 줄.

> **정답**:
> $$\frac{d[RC]}{dt} = k_{on} C ([R_T] - [RC]) - k_{off} [RC], \quad K_D = k_{off}/k_{on}$$
> Leftward: 용량↑ → $k_{on} C [R]$ 가속 → free receptor 풀 빨리 고갈 → max binding 시간 단축.
>
> 다음 깊이: $R_T$ 절대값 추정 가능? 아니면 fix?

### Q5 [적용, ★★]
신약 X Phase 1 데이터: (a) baseline ≠ 0, (b) plasma peak 후 1.5h nadir, (c) 1·5·25 mg에서 nadir 시간 1.8·1.5·1.0h *왼쪽 이동*, (d) 25 mg에서 nadir 깊이 plateau.
**(i) 모델 후보? (ii) NONMEM `$DES`? (iii) 추가 검증?**

> **정답**:
> (i) **Turnover with kout stimulation (Hill)** 또는 **Receptor on/off** — leftward + saturation.
>
> (ii) Turnover kout 자극:
> ```
> $DES
>   DADT(1) = KIN - KOUT*A(1)*(1 + SMAX*CP**HILL/(SC50**HILL + CP**HILL))
> ```
> Receptor on/off:
> ```
> $DES
>   DADT(1) = KON*CP*(RT - A(1)) - KOFF*A(1)
> ```
>
> (iii) 두 모델 simultaneous fit + OFV. Dose-normalized AUCE plot Hill 정당화. simultaneous multi-dose 식별성. 회복기 시상수 — Turnover면 $1/k_{out}$ 일정, Receptor on/off면 dose 미묘 변화.
>
> 다음 깊이: ΔOFV < 3.84 시 어느 모델 NDA 제출?

### Q6 [적용, ★★]
TDM 시나리오: 70세 여, 45 kg, eGFR 30 mL/min, digoxin 0.125 mg/일 정상상태. 농도 1점 (24h trough) 1.2 ng/mL. 소프트웨어 prior는 정상 신기능. **출력 Cl 추정값이 모집단 95%로 거의 동일. 해석 + 다음 단계?**

> **정답**:
> §5.3 **Case 1 가까운 상황**:
> - 1점은 Cl·V 동시 식별 부족 (underdetermined)
> - Prior가 *이 환자에 부적합* (정상 신기능 prior, 환자 신부전)
> - 결과 추정값 모집단 머묾 — *false confidence*
>
> 다음 단계:
> 1. **Prior 재선정** — 신부전 conditional prior (Stage 2 적용)
> 2. **추가 농도** — 최소 1점 더 (peak/trough pair), dose interval 중간점
> 3. **출력 신뢰구간 점검** — prior 폭과 비슷하면 정보 추가 거의 없음 직접 증거
>
> 다음 깊이: 신부전 conditional prior 시 var($\hat{Cl}$) 어떻게 조정해야 *돕는지* *덮는지* 구별? (→ Stage 2·3 통합)

### Q7 [적용, ○]
PK15 안전역 보고: 신약 X 12개월 dog, oral 10·56·320 µmol·day⁻¹·kg⁻¹, Cmax·AUC dose 선형, 320군 Cmax ~50 µM, 독성 무관찰. 임상 치료 농도 0.05–0.1 µM. NDA Toxicology Summary 한 단락 작성.

> **정답**:
> > "12-month repeated-dose safety study in dogs (oral doses 10, 56, and 320 µmol·day⁻¹·kg⁻¹) demonstrated dose-linear pharmacokinetics for both Cmax and AUC across the entire dose range, with no observed gender-dependent or capacity-dependent kinetic differences. The highest tested dose (320 µmol·day⁻¹·kg⁻¹) achieved Cmax of approximately 50 µM without any toxicologically significant findings. Anticipated therapeutic plasma concentrations of 0.05–0.1 µM in humans correspond to **a safety margin exceeding 100-fold** based on Cmax exposure. This supports the proposed Phase 1 first-in-human dose with adequate safety headroom."
>
> 핵심: 10·56·320 + Linear PK + 50 µM + 0.05–0.1 µM + **>100배** (가브리엘슨 p.547 표현).
>
> 다음 깊이: Capacity-limited 신호 발견 시 보고 문구 변경?

### Q8 [적용, ★★]
NDA 검토 코멘트: *"The proposed turnover model with kin inhibition predicts a rightward peak-shift, but Figure 5.3 shows the response nadir occurring earlier with increasing dose, not later. Please clarify."* 응답 전략?

> **정답**:
> §5.2 Critical Blow 현실 발생:
>
> 1. **즉시 인정**: 검토 관찰 정확, 모델 클래스가 데이터 peak-shift 방향과 *부정합* 인정.
> 2. **재분석 약속**: kout stimulation 재적합 + simultaneous multi-dose.
> 3. **방어 가능 케이스**: ΔOFV 작고 in vitro evidence가 kin inhibition 강력 지지 시 "two competing mechanisms" 보고, NDA 라벨링은 *덜 mechanistic*한 통계 모델 한정.
> 4. **Stage 1 §2.4 Trench-Tip**: 추가 dose escalation 또는 mechanistic biomarker로 분리.
>
> 절대 금지: 이전 모델 방어 위해 데이터 cherry-pick 또는 covariate 인위 추가.
>
> 다음 깊이: in vitro·in vivo 일관 kin inhibition인데 임상만 좌향 시 — 어떤 *third mechanism*? (TMDD, autoinduction, 활성 metabolite)

### Q10 [적용 — Stage 2, ★★]
**상황**: 65세 여, 60kg, SCr 2.0 mg/dL. Vancomycin (MW 1448, $f_e = 0.95$, V 0.7 L/kg, $t_{1/2}$ 6h, 단백 결합 ~50%). 일반 1g IV q12h.

**(1) Cockcroft-Gault → $CL_{cr}$. (2) Eq. 15-8로 $R_d$ → maintenance ratio. (3) 30% 규칙 + 권장 dose.**

> **정답**:
> **(1)**: $CL_{cr} = 0.85 \cdot (140-65) \cdot 60 / (72 \cdot 2.0) = 26.6$ mL/min
>
> **(2)**: $RF = 26.6/70 = 0.38$. $R_d = 0.38 \cdot 0.95 + 0.05 = 0.41$.
>
> **(3)**: $f_e = 0.95 > 0.30$ ✓, $RF = 0.38 < 0.70$ ✓ — 두 조건 위배 → **조정 필요**.
> 권장: 1g × 0.41 ≈ **410 mg q12h** 또는 1g q30h. 임상에서는 vancomycin TDM 표준 → trough 10–20 mg/L 목표 후속.
>
> Carry-through: dialysis 환자 아님 → §2.9 미적용. Dialysis 진행 시 vancomycin은 high-flux 제거 가능 (Bohler 1992) → 보충 용량 검토.

### Q11 [적용 — Stage 2, ★★]
**상황** (PK35 carry-through): PK35 55세, 60kg 남성 CHF에서 $\hat{Cl} = 5.7$ L/h, $\hat{V} = 119.6$ L. R&T Table 15-7 mild CHF 공식으로 implicit $CL_{cr}$ 역계산. 임상적 합리?

> **정답**:
> Sheiner mild CHF: $CL = (CL_{cr} + 0.048) \cdot \text{Wt}$ (kg, $CL_{cr}$ L·h⁻¹·kg⁻¹).
>
> $\hat{Cl}/\text{Wt} = 5.7/60 = 0.095$ L·h⁻¹·kg⁻¹
> $0.095 = CL_{cr} + 0.048 \to CL_{cr} = 0.047$ L·h⁻¹·kg⁻¹ ≈ 47 mL·min⁻¹·70kg → 60kg 환자 ~40 mL/min.
>
> **임상 합리**: 55세 CHF에서 $CL_{cr} \approx 40$ mL/min은 *moderate impairment* — Cockcroft-Gault 표준 70 대비 RF ≈ 0.57. CHF prerenal azotemia 흔함 → 합리.
>
> **그러나 V 역계산 모순**: $V/\text{Wt} = 3.8 + 52 \cdot CL_{cr}$ → $CL_{cr} = 0.047$일 때 $V = 6.24$ L/kg = 374 L. 추정 $\hat{V} = 119.6$ L는 그 *1/3*. **Sheiner 예측 하한($CL_{cr}=0$일 때 228 L)보다도 작다**. 두 가능성:
> ① Flat prior 헐거워 V가 *물리적 하한 아래*로 끌려감.
> ② 환자 *uremia 동반* (R&T p.464: digoxin V는 uremia에서 *예측보다 더 작아짐*).
>
> **본 사례 의미**: PK35 평면 prior + 단지 두 점 농도가 *의학적 plausible 범위 밖* V 추정 가능. **Conditional prior(Sheiner 1977) 사용했다면** 첫째 합 항이 *생리적 V 범위*를 enforce했을 것 → §2.6 B-3.

### Q12 [적용 — Stage 2, ★]
**상황**: Phenobarbital ($V$ 38L, $CL$ 0.4 L/h, $t_{1/2}$ 137h, $f_u$ 0.5, MW 232). 매일 dose + 주 3회 hemodialysis (3h, high-flux dialyzer creatinine CL 150 mL/min). 임상적 의미?

> **정답**:
> **Step 1 — 두 조건 (§2.9 C)**:
> - $V_u = V/f_u = 38/0.5 = 76$ L < 120 L ✓
> - $CL_u = CL/f_u = 0.8$ L/h
> - $CL_{uD} \approx 9$ L/hr (high-flux 전형)
> - $CL_u = 0.8 < CL_{uD} = 9$ ✓
>
> 두 조건 충족 — qualitatively 의미 있음.
>
> **Step 2 — 정량 (Eq. 15-29, 15-30)**:
> - $f_D = 9/(0.8+9) = 0.92$
> - $k_D = 9.8/76 = 0.129$ h⁻¹ → during-dialysis $t_{1/2} = 5.4$h
> - 3h 동안 몸 분율: $0.92 \cdot (1 - e^{-0.129 \cdot 3}) = 0.92 \cdot 0.32 = 0.29$
>
> **Step 3 — 해석**:
> Half-life 137h → 5.4h **24× 단축** (인상적). 그러나 3h 세션 ~29%만 제거. 이유: during-dialysis half-life > 세션 시간 ($t_{1/2,during}$ 5.4h > τ 3h).
>
> **Trap**: half-life 단축만으로 "효과적 dialysis" 결론 — *세션 시간 vs during-dialysis half-life* 비교 빠뜨림.
>
> **임상 결정**: 정상상태 농도 유지 위해 일일 dose *2배* (R&T p.474). Eq. 15-34 보충 용량 추가 검토.

### Q13 [적용 — Stage 3, ★★] ← **carry-forward 정점, Q11 → Q13 사슬**
**상황 (Q11 carry-forward)**: Q11에서 PK35 환자의 $\hat{V} = 119.6$ L가 Sheiner 예측 V 하한(228 L)보다 작아 *uremia 동반 가능성* 추정. 이제 같은 환자에 *다음 dose 결정*을 해야 한다 — 의사가 digoxin therapy를 "더 빠른 효과" 위해 *Loading dose* 추가 처방을 고려 중. TCS 데이터 (두 농도)가 있으나 prior는 평면. **(1) §2.10 5 criteria로 TCS 적용 평가. (2) Loading dose 결정 — V를 Sheiner conditional prior 기반? 추정 $\hat{V}$? RF 보정? Uremia 보정? (3) Stage 1·2·3 통합 권고를 NDA briefing 언어로 작성.**

> **정답** (Stage 1·2·3 통합 정점):
>
> **(1) TCS 5 criteria 평가**:
> | C | Digoxin 적용 | 평가 |
> |---|---|---|
> | C1 concentration-response | ✓ | trough 0.8–2 µg/L well-defined |
> | C2 high failure prob | ✓ | 좁은 치료역, 좁은 PD 변동 + 높은 PK 변동 (Table 18-1) |
> | C3 when problem | ✓ | 환자 농도 데이터 이미 있음, *uremia 의심* 발생 |
> | C4 population PK info | ✓ | Sheiner 1977 conditional prior 가용, R&T Table 18-7 |
> | C5 reliable assay | ✓ | 표준 immunoassay, turn-around ~hours |
>
> 5 criteria 모두 충족 — **TCS 적용 강력 권장**. 단, *어떤 prior*를 쓰는가가 핵심 분기.
>
> **(2) Loading dose 결정 — 4 시나리오 비교**:
>
> | 시나리오 | LD 계산 | 비판 |
> |---|---|---|
> | (a) Flat prior $V_{pop} = 500$ L | $D_L = 500 \cdot 1.5 / 1 = 750$ µg | 환자 V 추정 무시 → 즉각 독성 위험 |
> | (b) Bayesian $\hat{V} = 119.6$ L | $D_L = 119.6 \cdot 1.5 = 179$ µg | $\hat{V}$가 *물리 하한 이하* 가능성 — flat prior 결과의 artifact |
> | (c) Sheiner mild CHF, no uremia: $V = 3.8 + 52 \cdot 0.047 = 6.24$ L/kg → 374 L | $D_L = 374 \cdot 1.5 = 561$ µg | uremia 미반영 |
> | (d) **Sheiner + uremia 70% 보정 (R&T p.464)**: $V \approx 374 \cdot 0.7 = 262$ L | $D_L \approx 262 \cdot 1.5 = 393$ µg ≈ **0.4 mg** divided | **§5.5 매트릭스의 right column 적용 — 유일 예외 케이스** |
>
> **임상 결정**: (d) 권장. 단일 LD 0.4 mg을 0.2 mg q4h × 2 분할 (R&T digoxin LD 표준 분할 권고 — distribution kinetics rebound 회피).
>
> Maintenance: 별도 — Q11 추정 $\hat{Cl} = 5.7$ L/h가 Sheiner mild CHF + $CL_{cr}$ 0.047 L·h⁻¹·kg⁻¹ 합치 → R&T Table 18-7 footnote 적용 시 (0.25 mg/일) × 0.4–0.5 = **0.1–0.125 mg/일** (CHF 신부전 동반 환자 표준).
>
> **(3) NDA Briefing Document 언어**:
>
> > "For this patient (55-year-old, 60 kg male, CHF with concomitant suspected uremia based on Bayesian-derived V deviation from Sheiner mild-CHF predictions), the recommended dosing regimen is: Loading dose 0.4 mg in divided doses (0.2 mg q4h × 2), Maintenance 0.125 mg daily.
> >
> > The rationale integrates three independent lines of evidence: (a) Cockcroft-Gault-equivalent CL_cr of approximately 40 mL/min derived from Sheiner 1977 conditional prior reverse-calculation on observed $\hat{Cl}$ = 5.7 L/h; (b) reduced volume of distribution attributable to uremia-associated tissue redistribution as documented in Rowland & Tozer 5th edition page 464; (c) Bayesian individual estimate $\hat{V}$ = 119.6 L from two steady-state concentrations (2.5 µg/L at t = 458 h, 0.9 µg/L at t = 479 h, PK35 case study).
> >
> > Sensitivity analysis demonstrates that flat-prior-based loading dose recommendations (750 µg) carry an acute toxicity risk in the first six hours due to over-estimation of distribution volume, while Bayesian-individual-only recommendations (179 µg) under-estimate due to physiologically implausible volume estimates likely arising from prior misspecification. The selected loading dose of 393 µg balances these two failure modes by anchoring volume estimation in disease-conditional prior with explicit uremia correction.
> >
> > Therapeutic drug monitoring is recommended at 24 h post-loading and at 7 days steady-state to refine maintenance dosing per the Bayesian-conditional framework. Monitoring frequency should be increased upon any change in concomitant medications or renal function status."
>
> **이 답이 보여주는 통합 능력**:
> - Stage 1: §2.6 Bayesian 추정의 한계 + Case 1·3 인식 (flat prior + 2점 → physically implausible V)
> - Stage 2: §2.7 Rd framework + §5.4 conditional prior (Sheiner 1977) 평가
> - Stage 3: §2.10 TCS 5 criteria + §2.11 LD 결정 ($V \cdot C_{target}$) + §5.5 Maintenance vs Loading 분기 + Digoxin uremia 유일 예외
> - 규제 carry-through: sensitivity analysis로 *복수 가능성* bound 명시 — Boss Dilemma Q9의 "carry through and bound" 원칙 적용

### Q9 [Boss Dilemma — Socratic, ★★, 최종 질문]

**상황**: 신약 Y Phase 2 dose-finding 데이터. 명확한 baseline + time-delay + saturation, 단 **peak-shift 방향 통계적 모호** — 95% CI 좌향·우향 모두 포함. 추가 데이터 6개월 + 추가 코호트 비용 부담.

당신은 두 선택 사이:

**선택 A (보수적, "model agnostic")**: Effect compartment + Hill로 fit. peak-shift 무시. NONMEM 수렴 양호, GOF 양호. 단, dose extrapolation에서 *고용량 안전성 마진*이 실제 turnover일 경우 부정확. NDA "empirical PD model"로 기술.

**선택 B (mechanism 추구, "biology-driven")**: kin inhibition·kout stimulation *모두* fit, ΔOFV < 3.84로 분리 불가 명시. 두 모델 dose extrapolation *모두* 보여주고 conservative bound로 임상 권고. 보고서 길이 30% 증가, 검토자 confusion 위험.

**Phase 3 출시 결정 회의에서 어느 쪽? FDA Briefing Document에서 어떻게 방어?**

**[Stage 3 추가 — 환자군이 신부전·CHF 동반이라면 (Stage 2·3 통합 차원)?]**

> **정답 — 수석 모델러 Trade-off 논리**:
>
> **답은 단일 정답 없음 — 약물 *위험-이익 프로파일*과 *환자군*에 따라**:
>
> | 약물·환자 특성 | 권장 | 방어 논리 |
> |---|---|---|
> | 좁은 치료역 + 신부전·CHF 환자군 다수 (항암제, 항부정맥제) | **선택 B + Stage 2 통합** | "Mechanistic uncertainty is explicitly carried through to dose recommendation. Conservative bound from two competing models combined with disease-conditional prior covariates ensures no patient subgroup experiences exposures derived from wrong mechanism in vulnerable population." 라벨링의 *defendable* 기반. |
> | 넓은 치료역, 효능 차이 작음 (일반 항생제, 항고혈압제) | **선택 A + Phase 4 commitment** | "Empirical model adequately captures dose-response. Mechanistic refinement deferred to Phase 4 with biomarker." 효율 중심. Phase 4 commitment가 *방어 핵심*. |
> | High-stakes 메커니즘 주장 (novel target, breakthrough) | **선택 B + 추가 데이터** | "We will not finalize labeling without resolving mechanism. Additional dose-escalation cohort planned." 6개월 출시 지연 감수. |
>
> **수석 모델러가 *절대 하지 않는 것***: 선택 A 택하고 mechanism 불확실성 *언급 안 함*. 후일 mechanism 발견 시 dose extrapolation 틀린 쪽이면 — post-marketing safety signal → *대형 라벨 변경* 또는 *withdrawal*.
>
> **규제 문서 핵심 표현**: "The model selection process explicitly considered both turnover model variants and the effect compartment alternative. **Furthermore, sensitivity analyses extended to disease-conditional prior covariates (renal impairment, congestive heart failure) per Rowland & Tozer 5th edition Chapter 15 framework**, ensuring that mechanistic uncertainty does not compound with disease-induced PK variability in the recommended dose range. Sensitivity analyses demonstrating the impact of model uncertainty on dose recommendation are provided in Appendix [X]."
>
> 즉 **선택 자체가 아니라 그 선택을 *명시 carry*하고 sensitivity로 *bound*하고 *Stage 2·3의 환자군 변동까지 sensitivity 차원에 추가*하는 것**이 진짜 답.
>
> **Stage 1·2·3 통합 답**: peak-shift 모호성 + PK 변동성 (질환) + 처방 의사결정 (LD vs maintenance, §5.5)이 *2D sensitivity matrix*로 확장 — 행: model class (A vs B), 열: 환자 covariate (정상·신부전·CHF·dialysis). 16 cell의 dose recommendation이 NDA Appendix에 explicit. 검토자 confusion 위험 vs 방어 가능성 trade-off가 임상 약리학자의 *전문가적 무게중심*을 결정.

<!-- RECAP -->
**§7 흐름 요약 (Stage 1·2·3 누적)**: 13 질문 = Stage 1 9개(회상 4 + 적용 4 + Boss Dilemma 1) + Stage 2 3개(Q10·Q11·Q12) + **Stage 3 통합 1개(Q13)**. ★★ 7문항(Q1·Q2·Q5·Q6·Q10·Q11·Q13·Q9) 다음 세션 SR-flagged. **Q11 → Q13 carry-forward 사슬**이 Stage 1·2·3 전체를 *단일 환자 한 결정*으로 수렴 — Sheiner conditional prior로 PK35 추정 검증 (Stage 2) → uremia 동반 가능성 추정 → §5.5 Maintenance vs Loading 매트릭스의 right column 적용 → Loading dose 0.4 mg divided + Maintenance 0.125 mg/일 (Stage 3) → NDA briefing 언어. 이 사슬을 머릿속에서 5분 안에 운영하는 능력이 임상 약리학자의 카리브레이션.


---

# §8 — Meta-Frame & Big Picture (Stage 1·2·3 통합 — FINAL)

## A. 이 세션이 28-Session 프로그램에서 차지한 위치

본 Session 016은 PK/PD Mastery 프로그램의 **첫 번째 임상 통합 캡스톤** — Sessions 001–015에서 다진 이론적 도구들(NCA, 1·2 구획 PK, ADVAN, Turnover, TMDD, Bayesian, 신질환·간질환·CHF·dialysis, TCS·Loading dose·Missed/Erratic dosing)을 *단일 환자의 단일 visit*에 동시 적용하는 통합 운영 능력의 첫 검증.

```
[Sessions 001–008] 기초 PK 도구상자
[Sessions 009–015] PD 모델·population PK·질환 covariate
[Session 016 (현재) ← Stage 1·2·3 통합 캡스톤]  ★ 이 자리
        │
        ├─ 모델 구조 + 개인 추정 + 질환 + 임상 처방을 단일 결정 사슬로 운영
        │
[Sessions 017–020] PopPK NONMEM 구현 (CWRES, GOF, η-shrinkage, OFV χ²)
[Sessions 021–023] Pediatric, Pregnancy, Geriatric covariate
[Sessions 024–026] PBPK·QSP·MIDD framework
[Sessions 027–028] NDA·IND·Phase 4 RMP 규제 통합 캡스톤 (최종)
```

Session 016 이후 모든 후속 세션은 *이 통합 사슬의 한 노드를 깊이 파는* 형태 — 예: Sessions 017–020은 §2.1–§2.6의 *NONMEM 구현 디테일*, Sessions 021–023은 §2.7·§5.4·§5.5 *covariate 확장*, Sessions 027–028은 Q9·Q13의 *규제 언어와 의사결정 비대칭 명시*.

**현재 누적 도달**: 임상 약리학자가 단일 환자에 대해 (모델 → 추정 → 질환 → 처방) 4단계 의사결정을 5분 안에 운영하고, 그 결정의 sensitivity를 *2D matrix(model × covariate × dose)*로 NDA Appendix에 explicit하게 carry-through하는 능력.

## B. 핵심 Failure Modes — 임상 처방으로 환자에게 도달하는 8가지 silent error

다음은 *각각이 발견 시 라벨 변경, 환자 안전성 재평가, 또는 NDA 재제출로 이어지는* 종류의 오류:

1. **Peak-shift 방향 거꾸로 읽기** (§2.2, §5.2 Critical Blow) — kin/kout 라벨 반대 → "wrong drug mechanism in clinical pharmacology section" Deficiency Letter.

2. **Bayesian 출력의 "false individualization"** (§2.6 Case 1, §5.3) — TDM 소프트웨어 출력이 모집단 그대로인데 "환자 개인성 반영" 보고 → 농도 측정 비용이 임상 결정에 *기여 없이* 소비.

3. **Bayesian 출력의 "data-driven deception"** (§2.6 Case 2, §5.3) — wrong patient group prior에 sparse data만으로 estimation → 추정값이 *물리적 부적절 범위*로 끌려감 (PK35 V = 119.6 L 사례).

4. **30% 규칙 무시 over-engineering** (§2.7) — $f_e = 0.05$ 약물에 신부전 dose 조정 권고 → 임상의 confusion + 약사 시간 낭비, 동시에 *진짜 조정 필요한 fe = 0.95 약물*에 대한 신호 약화.

5. **Conditional prior 부적용** (§2.6 B-3, Stage 2) — 신부전·CHF·노인 환자에 평면 모집단 prior 적용 → estimation 결과가 *그 환자군*의 진실에서 체계적으로 어긋남.

6. **TCS 부적용 약물에 TCS 적용** (§2.10, Stage 3) — Warfarin 같은 PD 우세 약물에 plasma concentration 측정 비용 → INR target 와 plasma 농도 *불일치* 시 임상 혼란, 부작용 위험. 또는 그 반대로 *TCS 필수 약물에 TCS 미적용* (phenytoin nonlinear PK).

7. **Loading dose에 RF 보정 + Digoxin uremia 예외 미인지** (§2.11, §5.5, Stage 3) — 신부전 환자 vancomycin·aminoglycoside LD 무용 보정 (지연된 target 도달) 또는, 더 위험하게 — *digoxin uremia 환자에 LD 무보정* (첫 6시간 즉각 독성). §5.5 매트릭스의 right column 적용을 *놓치는* 단일 패턴이 가장 임상적 위험.

8. **Missed/Erratic dosing 데이터를 PK 변동으로 오진단** (§2.12, Stage 3) — 환자 비순응을 "환자 PK가 모집단과 다르다"로 잘못 해석 → dose adjustment 진행 → *실제로는 dose history 기록 부정확*. R&T Eq. 18-1~18-4 superposition 평가로 distinguishing — 측정값이 *기록된 dose history* 와 ±20% 이내면 PK 표준, 이외면 비순응 또는 PK 변동 의심.

이 8가지 모두 *조용히 발생 + 측정 시 늦음 + 발견 시 큰 비용*. Step 2 HTML이 이 8가지에 대한 패턴 검출 visualization 제공 (Stage 3 Phase 4C에서 결정).

## C. Professional Moat — 6 차원 동시 운영의 차별성

같은 데이터셋을 받았을 때 30년 차 임상 약리학자가 *5분 안*에 운영하는 6 차원이 *동시에 합의*에 도달하는 능력 = 모집단 PK 모델러와 임상 약사를 동시에 능가하는 "임상 통합 능력".

| 차원 | 운영 내용 | Session 016에서의 카드 |
|---|---|---|
| **1. 모델 구조** | 4축 패턴 인식 + peak-shift 방향 → PD 모델 클래스 후보 좁힘 | §2.1, §2.2, §2.3, §2.4, §2.5 |
| **2. 개인 추정** | Bayesian 두 합 항 분산 균형 → MAP estimate; flat vs conditional prior 선택 | §2.6 (B-3, B-4 포함) |
| **3. 질환 covariate** | $R_d$ 분해 + Cockcroft-Gault + 30% 규칙 + Sheiner conditional prior + dialysis 두 조건 | §2.7, §2.8, §2.9 |
| **4. TCS 적용성** | 5 criteria + PK·PD 변동성 4사분면 + Table 18-2 분류 | §2.10 |
| **5. Loading dose** | $V \cdot C_{target}/F$ + 3 축 결정 트리 (urgency·half-life·PD time course) + V well-defined property + Digoxin uremia 예외 | §2.11, §5.5 |
| **6. Missed/Erratic 정량** | Eq. 18-1~18-4 superposition + sample timing의 Fig. 18-13 confidence + forgiving vs unforgiving 분류 | §2.12 |

**5분 운영 시나리오 — Q13의 추상화**:

```
[0:00] 환자 chart open → 60kg, CHF, $\hat{V}=119.6$ L 추정 발견
[0:30] 차원 2: Sheiner mild CHF 공식 역계산 → V 하한도 안 맞음 → 의심
[1:00] 차원 3: 신부전 동반 + uremia 가능성 추정 (Stage 2)
[1:30] 차원 4: Digoxin TCS 적용 ✓ — 5 criteria 충족
[2:30] 차원 5: LD 결정 — §5.5 right column (uremia 예외) → V × 0.7 보정
[3:30] 차원 1·6: 다른 farm의 농도 데이터 superposition 검증, peak-shift 무관 (PK only)
[4:30] NDA briefing 언어 작성 (Q13 (3))
[5:00] 처방: LD 0.4 mg divided, Maintenance 0.125 mg/일, follow-up TDM 24h·7d
```

이 시나리오에서 6 차원 중 *1개라도* 빠지면 결정이 부분적이고 *체계적으로 편향*. 이 6 차원 동시 운영이 — 단일 환자 단일 visit에서 — Session 016 통합 캡스톤이 검증하는 핵심 역량.

**확장 가능한 시야 (CONTEXT tier 후속 흡수 대상)**:
- **Disease-on-PD** (R&T Ch.15 후반 WHIG): 본 세션은 *PK*에 초점. 후속에서 PD biomarker 분류(type 0–6, R&T) + 질환 효과 모델 통합.
- **Pharmacogenomic-conditional prior** (CYP2D6 trimipramine, HLA-B*5701, TPMT): genotype을 conditional prior로 흡수.
- **Phase 4 RMP TCS 약물 데이터**: post-marketing concentration data를 Fig. 18-13 sample timing weight + adherence pattern 분류로 reanalyze.

## D. Master's Lens 메타지침 — Stage 1·2·3 검증 결과

Session 016의 핵심 메타 학습:

1. **결정 사슬은 "조립 가능"한 모듈이 아니라 "동시에 합의되어야 하는" 6 차원** — 한 차원에서 결론 → 다른 차원으로 carry → 다음 차원 검증 → 모순 시 *역방향* carry-back. Q11→Q13 사슬이 이 carry-forward·carry-back 운영의 prototype.

2. **"30% 규칙·5 criteria·두 조건"의 공통 구조** — 각 framework이 *조정·적용·계산 *불필요한* boundary를 명시*. 이 boundary 없으면 모든 환자에 모든 조정 → over-engineering으로 진짜 신호 매몰.

3. **Conditional prior > Flat prior > 데이터 단독** — Stage 1 PK35는 *flat prior 한계*를 보여주는 사례, Stage 2 Sheiner 1977은 그 한계의 *해결책*, Stage 3 TCS post-measurement는 그 해결책의 *실시간 적용 framework*.

4. **"Sensitivity carry-through to dose recommendation"** — 모델 불확실성·prior 불확실성·환자 covariate 불확실성을 *모두 명시 bound로 전달*하는 것이 임상 약리학자의 규제·임상·과학 동시 만족 카리브레이션. Q9 Boss Dilemma의 2D matrix 운영이 이 원칙의 직접 적용.

5. **§5.5 매트릭스의 "유일 예외" — Digoxin uremia** — Framework은 *대부분*의 케이스에 일관되게 적용되어야 하지만, *예외*가 framework의 *경계*를 정의. 이 예외를 *같은 정확도로* 인지하고 적용하는 능력이 framework의 *limit*을 운영하는 능력 — 즉, framework 안에서 모든 답이 나오지 않을 때 *어디서 깨지는지*를 인지하고 *대체 framework을 호출*하는 능력.

이 5가지 메타지침이 본 세션의 *carry-forward*. Session 017 (PopPK NONMEM 구현)에서 이 5 메타지침을 코드 수준에서 implementation할 때 첫 검증.

<!-- RECAP -->
**§8 Big Picture 요약**: Session 016이 28-session 프로그램에서 *첫 임상 통합 캡스톤*으로서 Sessions 001–015의 도구를 단일 환자 결정에 *6 차원 동시 운영*하는 능력을 검증. 8 silent failure mode 모두 발견 시 라벨/Phase 4/NDA 재제출 비용. 6 차원 동시 5분 운영이 *모집단 PK 모델러와 임상 약사를 동시에 능가*하는 임상 약리학자의 차별성. 5 메타지침(carry-forward, framework boundary, conditional prior, sensitivity carry-through, framework limit)이 후속 Sessions 017–028의 backbone.

---

# ✦ Stage 1·2·3 누적 완료 (FINAL)

## 산출물 검증 체크리스트

**섹션 완성도**:
- §1 Session Header & Roadmap ✓ (Stage 1·2·3 통합 학습 목표 13개)
- §2 Concept Anatomy Cards: §2.1–§2.12 (12 MUST cards) ✓
  - 4 Apex Concepts: §2.2 Peak-shift Directionality, §2.6 Bayesian, §2.7 Rd Framework, §2.10 TCS Criteria
  - Stage 3 NEW: §2.10, §2.11, §2.12 (전부 R&T Ch.18 직접 추출)
- §5 Confusion Pair Dissection: §5.1–§5.5 (5 pairs) ✓
  - Stage 3 NEW: §5.5 Maintenance vs Loading dose + Digoxin uremia 유일 예외
- §7 Self-Test: Q1–Q13 + Q9 Boss Dilemma ✓
  - Stage 3 NEW: Q13 (Q11 → Q13 carry-forward, NDA briefing 언어)
- §8 Meta-Frame & Big Picture ✓ (8 failure modes, 6 dimension Moat, 5 meta-principles)

**소스 커버리지**:
| 소스 | 페이지 | 적용 §·Q |
|---|---|---|
| Gabrielsson Ch.6 | pp.423–466 | §2.1–§2.5, §5.1, §5.2, Q1–Q5, Q8 |
| Gabrielsson PK15 | pp.546–548 | §1, §7 Q7, §8 |
| Gabrielsson PK35 | pp.641–643 | §2.6 (B, B-2, B-3, B-4), §5.3, Q2, Q11, Q13 |
| R&T Ch.15 (Disease) | pp.443–489 | §2.7, §2.8, §2.9, §5.4, Q10–Q12 |
| R&T Ch.18 (Initiating Therapy) | pp.577–610 | §2.10, §2.11, §2.12, §5.5, Q13, §8 (failure modes 6–8) |

**Data Anchoring 검증** (모든 수치는 출처 페이지 명시):
- PK15: 10/56/320 µmol·day⁻¹·kg⁻¹ doses, Cmax ~50 µM, 치료 0.05–0.1 µM, **>100배 안전역**
- PK35: $\hat{Cl}$ = 5.7 L/h, $\hat{V}$ = 119.6 L, $t_{1/2}$ = 14.5 h, 2개 농도 (2.5 µg/L at 458h, 0.9 µg/L at 479h)
- R&T Ch.15: Eq. 15-7 (full), 15-8 (simplified), 15-13 (RF), 15-17 (maintenance), 15-29/30 (dialysis fraction), 15-34 (보충 용량)
- R&T Ch.18: Eq. 18-1 (1 missed), 18-2 (2 missed), 18-3 (9-13-17-21), 18-4 (erratic), Table 18-2 (PK·PD 변동성), Table 18-5 (TCS 약물), Table 18-7 (digoxin dosing), Fig. 18-5 (V vs CL covariate explanation), Fig. 18-13 (confidence in estimates)
- Worked examples (R&T): digoxin 2 missed → **0.39 µg/L** (sub-therapeutic), vancomycin 9-13-17-21 → **2.03 mg/L** (sub-therapeutic), vancomycin erratic → **34 mg/L 관측 vs 33.7 mg/L 예측** (일치)
- 유일 예외 (R&T p.464 직접 인용): "Digoxin distributes much less extensively to tissues in uremia, resulting in a smaller volume of distribution and a shorter half-life than that predicted from loss of renal function."

**Phase 4C Figure 결정 후보** (Step 2 HTML 학습문서로 이월):
- **Mermaid**: §2.1 4축 결정 트리, §2.10 TCS 5 criteria 결정 사슬, §2.11 Loading dose 3 축 결정 트리, §5.5 Maintenance vs Loading 분기 + Digoxin uremia 예외 강조
- **CSS heat map**: §2.7 $R_d$ vs $f_e$ × $RF$ 2D heatmap (Fig. 15-9A 재현), §2.10 PK·PD 변동성 4사분면 + warfarin·phenytoin pin
- **Chart.js interactive simulator**:
  1. Peak-shift directionality simulator (kin·kout × stim·inhib 4 모드, slider로 dose 변경, peak-shift 방향 자동 판정)
  2. Bayesian objective function landscape — flat vs conditional prior, var($\hat{P}$) ±50% sensitivity, MAP point 이동
  3. Cockcroft-Gault → $R_d$ → maintenance dose calculator (실시간)
  4. Hemodialysis 두 조건 visualization ($V_u$, $CL_u/CL_{uD}$ 평면)
  5. **Confidence-in-Estimates Fig. 18-13 reproduction** — sample timing slider × V·CL info 분리 시각화
  6. **Missed-dose superposition simulator** — dose history 자유 입력, 각 dose IV bolus 단독 농도 + 합산 농도 동시 표시, "관측 vs 예측" disconnect 진단
- **Q13 dose-decision pathway visualization**: 4 시나리오 (flat / Bayesian individual / Sheiner no-uremia / Sheiner+uremia) 각각의 LD·maintenance 비교

**NO Stage 4 slot — 본 v0이 최종 통합 산출물**.

---

**다음 단계 (Phase 진행)**:

```
✓ Phase 0  (scope lock)        — 완료
✓ Phase 1  (Master's Lens v0)  — 본 산출물 (FINAL)
→ Phase 2  (knowledge integration / Step 1 외부 검증)
→ Phase 3  (refinement / 누락 항목 보완)
→ Phase 4A (재미·매력 강화 / Big Idea 한 문장 카리브레이션)
→ Phase 4B (deep audit / Apex Concept 4개 분리 검증)
→ Phase 4C (figure 결정 / Mermaid·CSS·Chart.js 후보 ↑ 평가)
→ Step 2   (HTML 학습문서 / V5.1 protocol 4 bug fix 적용)
→ Step 3   (학습 효율성 검증 / 8 failure mode 자가진단)
```

**최종 메시지** (Stage 1·2·3 통합 산출물 마무리):

> 데이터의 *형태*는 그 데이터를 만든 *기계*의 흔적이고,
> 환자의 *질환*은 그 기계의 파라미터를 모집단에서 끌어내며,
> *Bayesian 추정*은 그 변동을 정량화하고,
> *임상 의사결정*은 그 정량을 처방으로 전환한다 —
> 이 사슬의 *한 고리라도 끊기면* 그 환자에게 도달하는 약물의 양은
> 그 환자에게 필요한 양과 *체계적으로* 어긋난다.
>
> Session 016이 검증하는 카리브레이션:
> *6 차원을 5분 안에 동시 운영하고, 그 결정의 sensitivity를 NDA Appendix에 explicit하게 carry-through하며, framework이 깨지는 boundary (Digoxin uremia 같은 유일 예외)를 같은 정확도로 운영하는* 임상 약리학자의 능력.

---


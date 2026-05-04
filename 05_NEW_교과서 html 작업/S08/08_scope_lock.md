=== SCOPE LOCK ===

Source      : Gabrielsson J & Weiner D. Pharmacokinetic and
              Pharmacodynamic Data Analysis: Concepts and Applications,
              5th ed. Swedish Pharmaceutical Press.
              [파일 A] 08_G_비선형_PK_MM_DDI_기전.pdf  ← 개념 본문
              [파일 B] 08_T_비선형_PK_MM_DDI_기전.pdf  ← Case Study 실습

Chapter     : Ch. 2.7  Nonlinear Systems – Capacity, Time, Flow and
                        Binding                        (pp. 112–141)
              Ch. 3.5.7 Multiple Binding Site Model    (p. 224, 하단)
              Ch. 3.6.1–3.6.4  Interaction Models      (pp. 224–227)
              ※ §3.6.5–3.6.6 (pp. 228–229)는 본 Scope 외
              Case Studies PK17 / PK18 / PK22          (pp. 553–585)

Chapter role: 비선형 PK의 4대 원인(Capacity·Time·Flow·Binding)을
              수식-도식-사례 삼각 구조로 확립; MM 소거 파라미터
              (Vmax, Km)의 추정 원리와 Cl·t½의 농도의존성을 체득;
              효소 유도(auto/heteroinduction) 반전율 모델 및
              DDI 상호작용 PD 모델(경쟁적·비경쟁적·일반 경험·
              enantiomer)까지 연결하는 비선형 시스템 통합 레이어.

Learner     : PhD pharmacometrics 과정 (2026년 3월 입학);
              임상약사 경력 ~10년; PopPK 입문-중급 전환 단계;
              NONMEM·nlmixr2 기초 병행 학습 중.

Final output: 단일 자기완결형 HTML (Step 2 산출물)

Mode        : A-Critical
              — 수식 유도 과정·파라미터 물리적 의미·PK17/18/22
                케이스 수치 검증 포함; 임상 판단 함의까지 명시

Image rights: None
              — 교재 Figure(2.85–2.112, 3.23–3.27, 17.1, 18.1–18.4,
                22.1–22.3) 재현 금지;
                동등 개념은 SVG/HTML 자체 제작 다이어그램으로 대체

=== CONTENT BOUNDARY (엄격 적용) ===

IN SCOPE (이 범위만 다룬다)
  ① 비선형성 진단법
       · dose-normalized AUC vs Dose 탐색 그래프 해석
         (Fig 2.85–2.86 원리; 직접 재현 불가)
       · 중첩 원리(superposition) 위반 판별 기준

  ② Capacity-limited kinetics (§2.7.2, PK17, PK18)
       · MM 수식 계열: Eq 2:264–2:274, 2:309
       · Cl = Vmax/(Km+C) 의 두 극한 (zero-order ↔ first-order)
       · AUC 및 농도의존 t½ (Eq 2:271–2:272)
       · 볼루스·지속주입·1차 흡수 입력별 dC/dt (Eq 2:270–2:274)
       · PK17: linear vs MM 모델 판별, WRSS/AIC 비교 (Table 17.1)
       · PK18: 에탄올 2구획 MM 모델, Vmax·Km 초기 추정 절차
                (Eq 18:1–18:13, Table 18.1)

  ③ Time-dependent kinetics (§2.7.3, PK22)
       · 효소 turnover 모델: dE/dt = Rin − kout·E (Eq 2:275–2:278)
       · Cl(t) 시간 함수 (Eq 2:282–2:287)
       · Heteroinduction 예시: pentobarbital → nortriptyline
         (kout t½ ≈ 158 h, pre/peri/post-induction MRT)
       · Autoinduction feedback 모델 (Eq 2:289–2:293, PK22)
         — 파라미터: Vc, Vt, a, k12, k21, kout, E0
                     (Table 2.17, 22.2)

  ④ Flow-dependent kinetics (§2.7.4)
       · 개념 참조만 (상세는 §2.4 — scope 외)

  ⑤ Nonlinear binding (§2.7.5)
       · fu 비선형성: Eq 2:294–2:303
       · 개방(in vivo) vs 폐쇄(in vitro) 계 오해 교정
       · warfarin–phenylbutazone: 결합 변위 vs CYP2C9 억제 구별

  ⑥ Nonlinear drug–metabolite model (§2.7.6)
       · 2구획 drug + 1구획 metabolite + MM 소거
         (Eq 2:304–2:308)
       · flip-flop 해석, full vs reduced model 비교
         (Table 2.18–2.20)

  ⑦ 에탄올: 통합 사례 (§2.7.7)
       · Capacity + Time(CYP2E1 유도) + Flow 3중 의존성
       · 생체이용률 농도의존성 (Eq 18:13)

  ⑧ DDI Interaction PD Models (§3.6.1–3.6.4, pp. 224–227)
       · 경쟁적 길항: Eq 3:49, EC50 이동 원리
       · 비경쟁적 길항: Eq 3:50, Emax 감소 원리
       · 일반 경험 모델 (Eq 3:51, Table 3.2)
       · Enantiomer interaction model (Eq 3:52–3:53, ketamine)
       · 다중 결합 부위 모델 (Eq 3:48, p. 224)

OUT OF SCOPE (언급하지 않는다)
  · §2.1–2.6 선형 PK 개념 (별도 선행 강의)
  · §2.8 NCA (별도 강의)
  · §3.1–3.5.6 단일 약물 PD 모델 기초
  · §3.6.5 추가 S자형 함수 (Gompertz·Weibull 등, pp. 228–229)
  · §3.6.6 반응 kinetics (non-steady state dynamics, p. 229)
  · PK19–PK21·PK23–PK24 Case Studies (파일 내 페이지 부재)
  · PopPK IIV/RUV 구조 (별도 강의)

=== HARD RULES ===

* 작업 범위: pp.112–141 / pp.224–227 / pp.553–585.
  이 범위를 벗어난 내용은 확장하지 않는다.
* 수치(파라미터 추정값, 단위, 농도)는 원문 PDF에 명시된 것만
  인용한다; 부재 시 [확인 필요] 플래그 후 보류.
* 교재 Figure 재현 금지(Image rights = None);
  동등 개념은 SVG·HTML 자체 제작 다이어그램으로 대체.
* 임상 결론(예: 용량 조정 불필요 원칙, bupivacaine 예외)은
  원문 근거 문장과 함께 제시.
* 교재에 없는 약물명·임상 수치를 예시로 삽입하지 않는다.
=================
=== SCOPE LOCK ===

Source       : Rowland & Tozer, Clinical Pharmacokinetics and
               Pharmacodynamics, 5th ed. (R&T 5e)
Chapter      : Ch.16 — Nonlinearities
Pages        : p.491 – p.529
Chapter role : 비선형 PK의 개념 토대 — 용량의존·시간의존 동태를
               발생시키는 포화 기전(Michaelis-Menten 대사, 포화
               수송, 포화 단백결합, TMDD) 전체를 체계화한다.
               Ch.17 Drug Interactions의 경쟁적 억제(Km 변화)·
               기전기반 억제(Vm 변화) 정량 예측의 직접 선행 지식.
               PopPK 맥락에서는 비선형 혼합효과 모델 구조 선택,
               포화 소실 경로의 fm 추정, 개인내 변동성 해석의
               수학적 기반.
Learner      : PhD pharmacometrics student; clinical pharmacist
               background; PopPK entry–intermediate
Final output : Single self-contained HTML (Step 2)
Mode         : A-Critical

Image rights : None
               # 교과서 원그림(Fig.16-1 ~ 16-30) 직접 임베드 불가.
               # 구조 이해에 필수적 figure는 Figure Pointer(P) 또는
               # 구조 재현 Schematic(R/N)으로 처리.

HARD RULES (apply to all phases):
- Do not expand beyond p.491–p.529.
- Do not fabricate values, experimental conditions, or page citations
  absent from the source PDF.
- Key anchoring data present in source — use verbatim:
    · Phenytoin: Vm ≈ 500 mg/day, Km ≈ 0.4 mg/L (fu=0.1 → Km'=4 mg/L)
    · Alcohol: Vm ≈ 10 g/hr, Km ≈ 100 mg/L, Vd ≈ 42 L/70 kg
    · Nicardipine saturable first-pass: F = 19→36% across 10–40 mg q8h
    · Ascorbic acid: plateau 9 mg/L @ 75 mg/day vs 19 mg/L @ 10,000 mg/day
    · Naproxen AUC nonlinearity: dose range 0–4 g oral
    · Disopyramide: nonlinear binding to α₁-acid glycoprotein
    · Cefonicid: saturable albumin binding, 30 mg/kg i.v.
    · Trandolaprilat: nonlinear ACE binding, Fu 0.05→0.20
    · Bosentan: saturable tissue (endothelin receptor) binding
    · Dicloxacillin: CLR dose-dependent (1 g → 2 g), fu = 0.04
    · Carbamazepine autoinduction: turnover time ~5 days
    · Clarithromycin autoinhibition: AUC/t½ disproportionate increase
      250 mg→500 mg, single→day 7
- [확인 필요] = flag and retain; never delete unverifiable content.
- Do not reproduce or embed copyrighted textbook figures unless
  Image rights = User-supplied OR Open-license source with attribution.
=================
=== SCOPE LOCK ===

Source       : Rowland & Tozer, Clinical Pharmacokinetics and
               Pharmacodynamics, 5th ed. (R&T 5e)
Chapter      : Ch.17 — Drug Interactions
Pages        : p.531 – p.576
Chapter role : 약동학적 약물상호작용의 정량 예측 프레임워크 —
               흡수 변화(bioavailability), 분포 변화(displacement),
               청소율 변화(경쟁적 억제·기전기반 억제·유도)를
               추출비(extraction ratio) 원리와 연결하여 임상·규제
               판단의 언어로 번환한다.
               Ch.16 Nonlinearities(Michaelis-Menten/fm 개념)를
               전제로 하며, NDA/IND Drug Interaction 섹션 및
               FDA DDI Guidance의 AUC ratio 예측(Eq.17-11)이
               이 챕터에서 직접 도출된다.
               PopPK 맥락에서는 inhibition/induction에 의한
               개체내 CL 변화 모델링, fm 추정, 상호작용 PK/PD
               분리(unbound C-R curve)의 직접 기반.
Learner      : PhD pharmacometrics student; clinical pharmacist
               background; PopPK entry–intermediate
Final output : Single self-contained HTML (Step 2)
Mode         : A-Critical

Image rights : None
               # 교과서 원그림(Fig.17-1 ~ 17-22) 직접 임베드 불가.
               # Figure Pointer(P) 또는 Schematic(R/N)으로 처리.

HARD RULES (apply to all phases):
- Do not expand beyond p.531–p.576.
- Do not fabricate values, experimental conditions, or page citations
  absent from the source PDF.
- Key anchoring data present in source — use verbatim:
    · Theophylline–Enoxacin: t½ 8.8 hr → 22 hr; Css 4→9 mg/L;
      CLinhib/CLnormal = 0.44; fm = 0.67
      Enoxacin 400 mg q12h × 4 days (Rogge et al. 1989)
    · Desipramine–Quinidine: fm(CYP2D6) ≈ 0.75; CLred 4-fold
    · Desipramine–Fluoxetine (Table 17-11): AUC 284→2110 µg·hr/L;
      t½ 16.1→63.8 hr; CL/F 289→27.1 L/hr (Bergstrom 1992)
    · Phenytoin–Valproic acid (Fig.17-3): N=25/11/9 patients;
      total C↓, unbound C unchanged — displacement only
    · Warfarin–Phenylbutazone (Fig.17-18): fu=0.005; CL=0.1 L/hr;
      10 mg/day warfarin; phenylbutazone 100 mg t.i.d. days 13–22
    · Digoxin–Quinidine (Table 17-8): CL 140→72 mL/min;
      CLR 101→51 mL/min; Vd 500→240 L; F 0.75→0.85
    · Rosuvastatin–Cyclosporine (Fig.17-11): Cmax ↑11-fold;
      AUC ↑7-fold; heart transplant recipients
    · Clarithromycin MBI: kinact = 0.07 min⁻¹; kE ≈ 0.23 day⁻¹
      (t½(enzyme) ≈ 3 days); kinact/kE = 438; CuI/KI = 0.025
      → 11-fold CL reduction vs 1.025-fold for reversible
    · Diltiazem–Lovastatin (Table 17-7): AUC ratio 1.27(i.v.) vs
      3.57(oral) — route-of-administration effect
    · Fluconazole–Midazolam (Fig.17-10): 400 mg fluconazole;
      oral AUC ↑5.6-fold, i.v. AUC ↑2-fold; F 24%→63%;
      FH 0.42→0.72, FG 0.57→0.88
    · Atorvastatin–Rifampin (Fig.17-19): Cmax ↑10-fold, AUC ↑7-fold;
      t½ 8→3 hr; CL/F reduced 9-fold; OAT1B1 inhibition
    · Lopinavir/Ritonavir combination product (Table 17-2)
    · Inhibitor classification (Table 17-5): Strong/Moderate/Weak
      by AUC fold-increase; mechanism-based inhibitors marked (b)
    · CYP substrate list (Table 17-6): ≥4-fold AUC increase
      with strong inhibitor
    · Poor vs. extensive metabolizer max exposure ratio (Eq.17-18):
      1/(1−fmPOLY−fmNP); Fig.17-15 clinical validation
    · Phenobarbital–Dicumarol (Fig.17-17): 3–4 weeks to new
      plateau; controlled by phenobarbital t½ = 4 days
    · Pharmacodynamic interactions: isobologram concept (Fig.17-21);
      two full agonists — Emax ceiling (Eq.17-21)
- [확인 필요] = flag and retain; never delete unverifiable content.
- Do not reproduce or embed copyrighted textbook figures unless
  Image rights = User-supplied OR Open-license source with attribution.
=================
작성 근거 메모
항목선택 이유Mode A-CriticalMM 소거·유도 모델은 수식 오독 시 NONMEM 코드에서 직접 오류로 이어짐; 파라미터 물리적 의미와 임상 함의 엄밀 확인 필수파일 A(G) / 파일 B(T) 병기개념과 Case Study가 분리 파일이므로, Step 2에서 cross-reference 시 페이지 혼선 방지DDI PD section 포함파일명에 "DDI 기전" 명시; §3.6 경쟁/비경쟁 모델이 실제 DDI 연구설계·규제 제출의 PD 파트 기초이므로 scope에 편입Image rights = None교재 저작권 보호; 핵심 그림(Fig 2.87–2.88 Cl-C 관계, Fig 2.92 유도 time course 등)은 HTML 단계에서 SVG 자작 대체
운영 제언: 두 챕터가 강하게 연결되어 있어(Ch.16의 Cu,ss=KmR0/(Vm−R0)C_{u,ss} = K_m R_0/(V_m - R_0)
Cu,ss​=Km​R0​/(Vm​−R0​) → Ch.17의 CLinhibitedCL_{inhibited}
CLinhibited​ 도출) Ch.16을 먼저 세션으로 처리한 뒤 Ch.17을 진행하는 순서를 권장합니다. 또는 두 챕터를 단일 세션으로 통합 처리할 경우 Ch.16의 Michaelis-Menten 파라미터 체계를 §2 첫 카드로 배치하는 구조가 최적입니다.
Phase 1 진행 시 주의사항
1. p.224 이중 귀속 처리 — §3.5.7 (Multiple binding site model)과 §3.6.1 (Competitive antagonism)이 동일 페이지(p.224)에 혼재합니다. Phase 1 추출 시 섹션 헤더 기준으로 구분하되, p.224 전체를 두 섹션에 걸쳐 이중 처리하지 않도록 주의하세요.
2. PK21 내용 경계 — §2.7.3.3 본문(pp.123–125)에 nortriptyline 사례가 서술되어 있고, 이는 IN SCOPE입니다. 그러나 Case Study PK21 자체는 파일에 없으므로 본문 서술 범위 내에서만 수치를 인용하고, PK21 원문을 별도 참조하지 않습니다.
3. 에탄올 §2.7.7 ↔ PK18 교차 참조 — 개념(§2.7.7, pp.139–141)과 케이스(PK18, pp.556–562)가 동일 현상을 다른 깊이로 다룹니다. Phase 1에서 양쪽 수치(Vmax, Km, 생체이용률 곡선)를 분리 추출한 뒤 Step 2에서 통합 설명 구조를 잡으세요.
4. 주의 1 — 수식 복원 우선순위 (Ch.16·17 공통)
PDF 텍스트 추출 시 수식이 깨질 가능성이 높습니다. 특히 Ch.17의 Eq.17-9~17-14 (경쟁적 억제/MBI 정량화 수식)와 Ch.16의 Eq.16-7~16-10 (phenytoin 정상상태·plateau 도달시간)은 [복원] 태그를 적극 활용하되 맥락 기반 LaTeX 복원을 우선하세요. 생략은 금지입니다.
5. 주의 2 — Curation Map 작성 순서 강제 (A-Critical 필수)
두 챕터 모두 MUST/CONTEXT 분류 없이 §2 카드 작성을 시작하면 안 됩니다. Ch.16에서는 Michaelis-Menten 정상상태 수식(Cuss = Km·R₀/(Vm−R₀))과 포화 대사의 임상 결과가 MUST 최상위입니다. Ch.17에서는 CLinhib/CLnormal 예측 수식과 extraction ratio 조건 분기가 MUST 최상위이며, displacement 단독 상호작용은 CONTEXT 처리가 적절합니다.
6. 주의 3 — 챕터 간 의존성 처리 방향
Ch.17 Phase 1 실행 시, Ch.16의 fm, Km, Vm 개념을 이미 알고 있다는 전제로 §2를 작성하세요 (중복 도출 금지). 단, §1 지식 그래프 위치에 "Ch.16 Nonlinearities 선행 필요"를 명시적으로 표기해야 합니다.

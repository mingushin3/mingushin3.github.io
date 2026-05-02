=== SCOPE LOCK ===

Source       : [Primary] Gabrielsson & Weiner 5e (G&W)
                 Ch.3 §3.9 Effect Compartment (Link) Models — pp.261–272
                 Ch.3 §3.11 Tolerance and Rebound Models — pp.284–302
                 Ch.3 §3.13 Transduction Models — pp.323–325
                 Case Studies PD13, PD20, PD21, PD35 — pp.805–809, 836–848, 910–914
               [Secondary] Rowland & Tozer 5e (R&T)
                 Ch.8 Response — pp.233–264

Chapter      : Ch.3 §3.9 / §3.11 / §3.13 — Effect Compartment · Tolerance & Rebound · Transduction Models

Pages        : G&W pp.261–272, 284–302, 323–325, 805–809, 836–848, 910–914
               R&T pp.233–264

Chapter role : PK/PD 시간 지연(hysteresis) 현상의 세 가지 기계론적 해법을
               완성하는 핵심 축:
               (1) 분포 지연 → Effect Compartment / ke0 모델로 해소
               (2) 체계 반응의 지연·적응 → Tolerance/Rebound/Feedback 모델로 포착
               (3) 수용체–관찰 반응 사이 연쇄 → Transduction(Transit) 모델로 구현.
               이 세 축을 이해하지 못하면 간접반응 모델(Indirect Response)과
               PopPK/PD 통합 모델링의 모델 선택 논리가 붕괴된다.
               선행 지식: Emax/Hill 방정식(§2), Indirect Response 4모델(§3.7),
               1·2구획 PK 수식.
               후속 지식: TMDD, PKPD 시뮬레이션, 규제 제출용 임상-PD 모델.

Learner      : PhD pharmacometrics student; clinical pharmacist background;
               PopPK entry–intermediate; NONMEM 실습 단계 진입 전.

Final output : Single self-contained HTML (Step 2 — V5.1 Apex Edition)

Mode         : A-Critical
               근거: 수식·ODE·규제 파급력·케이스스터디 실제 데이터가
               모두 포함된 핵심 축 세션. 모델 선택 오류 시 NDA/IND
               Deficiency Letter 위험 직결.

Image rights : None
               (모든 Figure는 Pointer 방식으로 처리 — 원문 교과서 직접 열람 지시)

Dynamic Source Anchoring — 필수 실제 수치 목록:
  [G&W] PD20: analgesic iv bolus D=45 µg/kg, V=1 L/kg, K=0.50 h⁻¹,
               initial estimates Emax≈3–5, EC50≈1.5 µg/L, ke0≈0.1 h⁻¹
  [G&W] PD21: rabbit, oral 1 & 2 µmol/kg antagonist X;
               ke0=0.025 min⁻¹, kout=0.031 min⁻¹, koff=0.018 min⁻¹;
               IC50≈40–42 nM; t½ke0=28 min, t½kout=22 min, t½koff=39 min
  [G&W] PD13: two consecutive iv infusions; Model II (negative feedback)
               best fit: kin=30, kout=2.9, ktol=4.2, EC50=350, n=7.4;
               AIC=−97.5, WRSS=0.083
  [G&W] PD35: human male volunteer, 3 doses; C0=1.05, 4×1.05, 16×1.05 nmol/L;
               K=0.0228 h⁻¹ (t½≈30 h); 3 transit compartments optimal
               (WRSS=642 vs 789 for 2, 1319 for 1); τ≈9.8 h per compartment
  [G&W] Table 3.9: t½ke0 real compounds — terbutaline FEV-1 7.5 min,
               theophylline FEV-1 11 min, d-tubocurarine 4 min,
               fentanyl spectral edge 6.4 min, QT-quinidine 8 min
  [R&T] digoxin: cardiac effect peaks while plasma falls 0–4 h post iv bolus
  [R&T] naproxen: 500 mg oral, counterclockwise hysteresis, peak 3–4 h;
               effect compartment removes hysteresis (Fig 8-14)
  [R&T] warfarin: 1.5 mg/kg oral; prothrombin complex nadir ~48 h;
               t½ complex ≈1–2 days
  [R&T] aspirin 650 mg: t½ 15 min; antiplatelet effect persists days
  [R&T] succinylcholine 0.5 mg/kg iv: T50 ≈6 min, k≈0.2 min⁻¹;
               response declines linearly 80→20% at 22%/min

핵심 개념 골격 (Curation Map — 사전 판단):
  MUST:
    1. Effect Compartment 모델 구조 및 ke0 도출
    2. Hysteresis 방향(시계/반시계) 판별 및 기계론적 원인 분류
    3. Tolerance/Rebound: 음성 피드백(Moderator M) 모델 ODE 쌍
    4. Transduction 모델(Transit 구획 연쇄) ODE 체계
  CONTEXT:
    - Pool/Precursor 모델 (MUST 3의 대안 구조로 1–2문장)
    - 시간-의존 파라미터 약화(Colburn–Eldon) 접근법 (한계 언급 수준)
    - Antagonistic metabolite 모델 (경험적 한계 1문장)
    - tmax 불변 원칙 (link model vs. turnover 구분 도구로 언급)

HARD RULES:
  - 이 page range를 벗어나지 않는다.
  - 수치·실험조건·페이지 인용을 소스 없이 지어내지 않는다.
  - [확인 필요] = 표시 유지; 삭제 금지.
  - Image rights = None → 교과서 원그림 임베드 금지;
    Figure Pointer(📖 callout) 방식으로만 처리.
=================
Phase 1 진행 시 주의사항
① §3.10 의도적 제외 확인 필수
Scope Lock의 page range는 §3.9(pp.261–272) → §3.11(pp.284–302)로 §3.10 Dose-Response-Time Models(pp.272–284)를 명시적으로 건너뛴다. PDF에는 해당 내용이 존재한다. Phase 1 초안 작성 전, §3.10 제외가 커리큘럼 의도(세션 분리 또는 범위 축소)인지 확인하고 Curation Map에 CONTEXT 처리 여부를 결정할 것. 의도적 제외가 맞다면 현행 유지.
② G&W + R&T 역할 분담 명확 적용
두 소스가 동시에 투입된다. Phase 1 작성 중 G&W = 수식 도출·실험 데이터 앵커링, R&T = 임상·생리학적 해석·hysteresis 진단 논리로 역할을 분리하여 혼용하지 않을 것. 특히 hysteresis 방향 판별(시계/반시계) 설명은 R&T Ch.8 논리를 우선 적용한다.
③ PD13 데이터 해석 경계 준수
Case Study PD13의 Model I·II·III 파라미터 비교표(Table 13.1)는 §3.11 Tolerance 개념의 핵심 앵커이나, §3.9 Effect Compartment 카드에서 오용될 위험이 있다. "Link 모델을 Turnover 데이터에 잘못 적용했을 때의 결과"로만 §3.9 C-2 Plausible Fallacy에 인용하고, PD13 수치 자체는 §3.11 카드에 귀속시킬 것.

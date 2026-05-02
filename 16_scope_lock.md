=== SCOPE LOCK ===

Source       : Gabrielsson & Weiner 5e (Pharmacokinetic and Pharmacodynamic
               Data Analysis)
               — Part A: Chapter 6 (Theory section)
               — Part B: PK15, PK35 (Pharmacokinetic Applications section)

Chapter      : Ch.6 — Pattern Recognition (§6.1, §6.3–§6.6, §6.9)
               PK15 — Toxicokinetics (NCA, 노출 지표, 안전역)
               PK35 — Bayesian Model (Digoxin TDM, 개인 파라미터 추정)

Pages        : p.423–466 (Ch.6) | p.546–548 (PK15) | p.641–643 (PK35)
               ※ 총 비연속 ~49 페이지. 단일 세션 처리 상한에 해당.
               Step 2 토큰 절단 위험 인지 하에 진행.
               절단 발생 시 Ch.6 → PK35 → PK15 우선순위로 완성.

Chapter role : 캡스톤 통합 세션 — 세 파트는 아래 단방향 인과 흐름으로 연결됨:
               [Ch.6 패턴 인식] → PD 모델 구조 선택 능력 확보
                 ↓ (올바른 모델이 있어야 파라미터 추정이 의미를 가짐)
               [PK35 Bayesian TDM] → 개인 PK 파라미터의 사후 추정 원리
                 ↓ (파라미터를 추정했으면 노출을 규제 언어로 보고해야 함)
               [PK15 Toxicokinetics] → NCA 기반 노출 지표 및 안전역 소통
               
               PK15는 Ch.6/PK35의 심화 개념 없이도 독립 이해 가능한
               보완 파트이며, Ch.6·PK35가 선행 필수.

               선행 필수 지식: 1구획 IV/oral PK, Emax/Hill 함수,
               Turnover 모델 기초 (dR/dt = kin – kout·R),
               Effect Compartment (ke0), Receptor On/Off (kon/koff)
               후속 열리는 영역: PopPK PD 통합 모델링(NONMEM $DES),
               Bayesian TDM 소프트웨어 운용,
               NDA/IND PK/PD 섹션 작성

Learner      : PhD pharmacometrics student; clinical pharmacist background;
               PopPK entry–intermediate. 기초 PK 구획 모델과 Emax는 체화됨.
               Turnover 모델 수식은 이론적으로 노출됐으나 "어느 상황에
               어느 모델을" 데이터 형태에서 즉독하는 Expert Pattern Matching
               능력이 미형성 상태.

Final output : Single self-contained HTML (Step 2)

Mode         : A-Critical (Ch.6 + PK35) / B-Standard 가중(PK15)
               — Ch.6: 모델 선택 오류 → NDA Deficiency Letter 직결.
                 Peak-shift 방향 오판 → EC50 수배 편향. A-Critical.
               — PK35: Bayesian 목적함수 이해 없이 TDM 소프트웨어
                 출력 맹신 → 고위험 임상 판단. A-Critical.
               — PK15: NCA 비구획 분석 + 안전역 소통.
                 구현·워크플로우 중심. B-Standard 가중 처리.
                 (§2 카드 깊이를 Ch.6·PK35보다 1단계 낮게 설정)

Image rights : None
               (교과서 원본 Figure는 Pointer 타입으로만 안내. 임베드 금지.)

HARD RULES (apply to all phases):
- Do not expand beyond the specified page ranges.
- Do not fabricate values, experimental conditions, or page citations
  absent from the source PDF.
- PK15 실험 데이터(개, 경구, 10/56/320 µmol·day⁻¹·kg⁻¹,
  Cmax/AUC 선형성, 안전역 >100배, 치료 농도 0.05–0.1 µM,
  Cmax ~50 µM)는 책 수치 그대로 인용. 가상 수치 대체 금지.
- PK35 임상 데이터(55세 남성, CHF, Digoxin 0.2 mg, Lanoxicap,
  C₁=2.5 µg·L⁻¹ at 458 h, C₂=0.9 µg·L⁻¹ at 479 h,
  Cl_pop=1.8 L·h⁻¹, V_pop=500 L,
  추정값: Cl=5.7 L·h⁻¹, V=119.6 L, t½=14.5 h)는
  책 수치 그대로 인용.
- Ch.6 케이스(A~I)별 모델 수식(Eq. 6:1–6:111)은 LaTeX 복원 필수.
  PDF 파싱 오류 수식은 맥락 복원 후 [복원] 표기.
- Peak-shift 방향성(좌·우)과 Saturation 유무의 진단 인과는
  원문 논리 보존.
- [확인 필요] = flag and retain; never delete unverifiable content.
- Do not reproduce or embed copyrighted textbook figures.
=================
=== SCOPE LOCK ===

Source       : Rowland & Tozer, Clinical Pharmacokinetics and Pharmacodynamics, 5th ed.
Chapter      : Ch. 15 — Disease
Pages        : p. 443 – p. 489
Chapter role : "질환에 의한 PK 변동의 정량적 예측 프레임워크;
               신기능 저하 환자에서 투여 용량 조정 계산의 유일한
               정량적 기반. Ch. 14 (Age, Weight, Gender)의 직접 후속이며,
               Ch. 18 (TDM)의 필수 선행 개념. 이 챕터 없이는
               digoxin·vancomycin TDM 계산 불가."

Learner      : PhD pharmacometrics student; clinical pharmacist background;
               PopPK entry–intermediate

Final output : Single self-contained HTML (Step 2)
Mode         : A-Critical

Image rights : None

HARD RULES (apply to all phases):
- Do not expand beyond this page range.
- Do not fabricate values, experimental conditions, or page citations
  absent from the source PDF.
- [확인 필요] = flag and retain; never delete unverifiable content.
- Do not reproduce or embed copyrighted textbook figures unless
  Image rights = User-supplied OR Open-license source with attribution.

=================

[거장의 시각 — 챕터 위치 해석]

이 챕터는 "병이 있는 사람에게 약을 얼마나 줘야 하는가"라는
임상 질문에 수식으로 답하는 방법론의 핵심이다.
핵심 개념 계층은 다음과 같다:

① 간질환 → F↑ + CL↓의 이중 효과 → 구체적 예시:
   verapamil (고추출비: F 0.22→0.52, CL 76→37 L/hr),
   cefetamet (신배설 주도: 변화 없음), meptazinol (고추출비 bioavailability 400%↑)
   Child-Pugh Classification (Table 15-2) 활용

② 심혈관질환 → hepatic blood flow↓ → high-E drug CL↓
   lidocaine ↔ indocyanine green clearance 상관 (Fig. 15-4)

③ 신질환 — 이 챕터의 核心:
   Rd = CLu(d)/CLu(t) = RF·fe(t) + [1−fe(t)]·[(140−Age)·Wt^0.75 / 1936]
   Cockcroft-Gault 공식 (Table 15-5)
   Amikacin 3가지 조정 전략 (dosing interval↑ vs. dose↓ vs. 혼합)
   Gentamicin/Phenobarbital 혈액투석 보충 용량 계산 (Eq. 15-34)
   CAPD clearance 원리 (VPC/T ≈ 6.7 mL/min의 저효율)

④ 질환의 PD 영향:
   disease progression model: dS/dt = kin − kout·S
   symptomatic vs. disease-modifying treatment effect 구분
   WHIG model (Fig. 15-25)

실무 파급력:
- fe(t) ≥ 0.3이면서 RF < 0.7인 환자 → 무조건 용량 조정 검토
- Rd 계산은 NDA 신장애 집단 PK 분석의 이론적 근거
- Supplemental dose = V·C(0)·(e^{−k·τ} − e^{−kD·τ}) 공식은
  투석환자 항생제 TDM의 직접 계산 도구

=================
=== SCOPE LOCK ===

Source       : Rowland & Tozer, Clinical Pharmacokinetics and
               Pharmacodynamics, 5th ed.
Chapter      : Ch. 18 — Initiating and Managing Therapy
Pages        : p. 577 – p. 610
               ※ Study Problems (pp. 606–610)는 §7 Self-Test
               문항 설계 참고에만 사용. MUST 카드 범위 불포함.

Chapter role : "Section 4 (Individualization)의 종합 통합 챕터.
               Ch. 15 (Disease)에서 학습한 Rd 공식·CLcr 추정·
               투석 보충용량 계산을 직접 임상 의사결정으로
               전환하는 방법론 전체를 다룬다 (Ch. 15가 직접
               선행 개념이며, Digoxin PK 파라미터 공식은
               Ch. 15 Table 15-7에서 그대로 연결됨).
               Target Concentration Strategy (TCS)의 작동 조건
               정의, Digoxin·Vancomycin TDM 정량 시나리오
               (missed dose, 9-13-17-21 regimen, erratic dosing)
               계산의 완결판.
               이 챕터를 체화하지 않으면 PopPK 보고서에서
               '임상적 의미' 섹션을 쓸 수 없다."

Learner      : PhD pharmacometrics student; clinical pharmacist
               background; PopPK entry–intermediate

Final output : Single self-contained HTML (Step 2)
Mode         : A-Critical

Image rights : None

HARD RULES (apply to all phases):
- Do not expand beyond this page range.
- Do not fabricate values, experimental conditions, or page
  citations absent from the source PDF.
- [확인 필요] = flag and retain; never delete unverifiable content.
- Do not reproduce or embed copyrighted textbook figures unless
  Image rights = User-supplied OR Open-license source with
  attribution.
- Study Problems는 §7 Self-Test 설계 참고용으로만 사용하며,
  MUST 개념 카드 내용으로 확장하지 않는다.

=================

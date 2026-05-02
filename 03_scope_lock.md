=== SCOPE LOCK ===

Source A (G)  : Gabrielsson & Weiner, Pharmacokinetic and
                Pharmacodynamic Data Analysis, 5th ed.
Chapter       : Ch. 2 — Pharmacokinetic Concept
                §2.2.4  Extravascular administration
                §2.2.5  Estimation of absorption parameters (1st-order input)
                §2.2.6  Estimation of absorption parameters (zero-order input)
                §2.2.7  What lies behind the apparent Ka?
                §2.2.8  Estimation of bioavailability
                §2.2.9  How does input to plasma compartment vary?
                §2.2.10 Multiple dosing
                §2.2.11 Absorption from multiple sites
                §2.2.12 Conclusions for extravascular dosing
                Case Study PK2 — One-compartment oral dosing
                Case Study PK3 — One-compartment 1st- and 0-order input
Pages         : p. 28 – p. 47 ; p. 476 – p. 486

Source B (T)  : Rowland & Tozer, Clinical Pharmacokinetics and
                Pharmacodynamics, 5th ed.
Chapter       : Ch. 6 — Kinetics Following an Extravascular Dose
                Ch. 7 — Absorption
                Appendix F — Absorption Kinetics (Method of Residuals)
Pages         : p. 169 – p. 195 ; p. 197 – p. 220 ; p. 781 – p. 784

Chapter role  : 경구(및 경혈관외) 투여 후 PK의 수학적·개념적 토대.
                IV bolus 이후 첫 번째 임상 현실 — 흡수 단계가 존재하는
                계(system)에서 F·Ka·Tmax·AUC가 어떻게 결정되는가를
                확립한다.
                PopPK 흡수 서브모델(1st-order, transit compartment,
                Weibull, zero-order) 구축의 필수 선행 지식이며,
                NONMEM ADVAN2/ADVAN4·ODE 코딩 및
                flip-flop 오동정(misidentification) 회피의 직접 근거다.

Learner       : PhD pharmacometrics 1학기; 임상약사 10년 경력;
                IV bolus PK (CL, V, t½) 개념 완성;
                PopPK 개론 진입 단계 — 흡수 파라미터 추정 및
                모델 식별가능성(identifiability) 이슈 첫 노출

Final output  : Single self-contained HTML (Step 2)

Mode          : B-Standard
                # 근거: Ka·F·Tmax 공식 유도(A급 수준)와
                # flip-flop·Ka,app vs Ka,true 개념(임상 해석 직결)은
                # 심화 처리 필요. 단, PK2·PK3 Case Study 수치 재현
                # (검증용 계산 포함) 및 Rowland §7 흡수 생리학은
                # B-Standard 내 "중점" 절로 처리한다.

Image rights  : None
                # 두 교재 모두 유료 저작권 도서.
                # 교재 Figure(2.15–2.32, 6-1~6-15, F-1 등)는
                # 재현 금지; 대신 동등한 의미의 원본 SVG/ASCII
                # 다이어그램으로 대체 생성할 것.

=================

CONCEPTUAL SPINE (이 Scope Lock의 핵심 학습 경로)

① 흡수의 물리적 의미
   IV 직접 → 혈장 | Extravascular: 흡수 속도(Ka) × 생체이용률(F) 가 
   함께 작용. C(t) = (Ka·F·Dose / V·(Ka−K)) · [e^{−K·t} − e^{−Ka·t}]
   [Eq. 2:35 / G pp.30; Eq. F-1 / T p.782]

② 파라미터 삼위일체
   - F  : 전신 순환 도달 분율 — AUC_po/AUC_iv × D_iv/D_po
   - Ka : 장관 소실 겉보기 1차 속도상수 (Ka,app = Ka,true + Kd)
   - Tmax = ln(Ka/K)/(Ka−K)  [lag-time 없을 때; Eq. 2:52 / G p.35]
   → Cmax, AUC, Tmax 삼자는 상호 종속 — 하나만 바뀌어도 나머지 변동

③ Flip-flop 동정
   Ka < K 일 때: terminal slope → Ka (not K)
   IV 데이터 없이 경구만 있으면 식별 불가
   [§2.2.4 / G p.29; Ch.6 Case C / T p.175]

④ 잔차법(Method of Residuals)
   terminal slope → K, back-extrapolation → A₀·e^{−K·t},
   residual = extrapolated − observed → slope = −Ka
   lag-time = 두 직선 교점 [§2.2.5 / G p.32; Appendix F / T p.781]

⑤ V/F 식별불가능성(identifiability ceiling)
   경구 단독 시: V와 F를 분리 추정 불가 → V/F만 추정 가능
   IV 병용 시만 F·V 독립 추정 가능 [§2.2.4 / G p.32]

⑥ Ka,app vs Ka,true
   Ka,app = Ka,true + Kd  (Kd: 장내 분해·분변 소실 속도상수)
   F = Ka,true / (Ka,true + Kd)   [Eq. 2:70 / G p.41]

⑦ Zero-order vs First-order 판별
   PK3: 1차 모델 CV% 3400% → 비구분; 0차 모델 CV% 5~14%
   AIC 차이(76.2 vs 85.2) + residual randomness → 0차 선택
   [G pp.483–486]

⑧ 생체이용률 추정 방법 이중성
   NCA: F = AUC_po/AUC_iv · D_iv/D_po  (CL 일정 가정)
   Compartmental: Ctotal = Civ + Cpo 동시 피팅 [§2.2.8 / G p.42]

⑨ 누적 입력 다양성 (T Ch.6 + G §2.2.9)
   Bolus / Zero-order / First-order / Multiple Zero / Multiple First /
   Exponential+Zero 조합 → 각 입력 함수에 따른 C(t) 패턴

⑩ Bioequivalence 판단 기준
   90% CI of AUC·Cmax ratio: 0.80–1.25 내 → BE 선언
   tmax는 BE 기준 지표지만 CI 기반 판정 아님 [T Ch.6 pp.182–183]

=================

HARD RULES (apply to all phases):
- Do not expand beyond the page ranges above (G pp.28–47, 476–486;
  T pp.169–195, 197–220, 781–784).
- Do not fabricate numerical values, experimental subjects,
  or parameter estimates absent from the source PDFs.
- [확인 필요] = flag and retain; never silently delete.
- Do not reproduce or embed copyrighted textbook figures.
  All visuals must be original SVG or ASCII constructed to
  express equivalent conceptual content.
- Ka,app / Ka,true 구분 및 flip-flop 주의 경고는
  모든 Ka 언급 맥락에서 반드시 병기할 것.
=================

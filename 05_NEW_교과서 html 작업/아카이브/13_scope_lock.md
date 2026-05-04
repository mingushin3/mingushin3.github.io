=== SCOPE LOCK ===

Source       : Rowland & Tozer 5e (R&T) + Gabrielsson & Weiner 5e (G&W) — 혼합 소스
               ※ R&T: Vol I 임상 이론 (개체 간 변이의 생리학적·통계적 프레임)
               ※ G&W: Vol I 데이터 이론 (다중 피험자 분석, 공변량 모델링 실험 데이터)

Chapter      :
  [R&T] Ch.12 — Variability
  [R&T] Ch.13 — Genetics (CYP 다형성·약력학적 변이, Ch.12 연장)
  [G&W] Ch.4  — Modeling Strategies (EDA, 파라미터 식별성, 다중 피험자 풀링)
  [G&W] PK50  — Analysis of Multiple Subjects Concentration- and Response-Time Profiles

Pages        :
  R&T  p.361–410  (Ch.12 p.361–392 + Ch.13 p.393–410)
  G&W  p.333–352  (Ch.4 전반부: EDA, 식별성, 추정능력)
  G&W  p.704–710  (PK50: CpD 항부정맥제, 12명, 2구획, 혈장단백결합 공변량)

Chapter role : "개체 간 변이(IIV/BSV)와 공변량의 개념적 기초 —
               NONMEM 혼합효과모델에서 θ·ω²·η·ε·σ²의 생물학적·통계적 의미를
               내면화하지 못하면, $OMEGA 해석·GOF 잔차 진단·공변량 모델 구축·
               용량 개별화 설계가 모두 구조적으로 붕괴된다.
               이 세션은 PopPK 커리큘럼 전체의 분산 파라미터 축을 정초한다."

Learner      : PhD pharmacometrics student (2026년 3월 입학, 가톨릭대);
               임상약사 배경; PopPK 입문-중급; NONMEM 기초 경험 있음

Final output : Single self-contained HTML (Step 2, V5.1 Apex Edition)

Mode         : A-Critical
               근거: IIV·IOV·RUV의 오차 모델 구조 (가산/비례/지수형),
               공변량 모델링 (fu를 PK 파라미터 공변량으로 사용하는 PK50 실험),
               최대우도법·OFV·LRT, 유전적 다형성(CYP2D6/2C9/2C19·VKORC1)이
               규제 제출 파급력을 가짐 → 전체 Phase 실행 필수

Image rights : None
               # 교과서 원그림 임베드 금지; Figure Pointer(P) 또는 신규 도식(N)만 허용

HARD RULES (apply to all phases):
- Do not expand beyond this page range.
- Do not fabricate values, experimental conditions, or page citations
  absent from the source PDFs.
- [확인 필요] = flag and retain; never delete unverifiable content.
- G&W PK50 실제 수치 반드시 앵커링:
    CpD 566 µg / 5h IV infusion / 12명 antiarrhythmic patients
    Cl = 11.4 L·h⁻¹ (CV 28%), Cld = 4.35 L·h⁻¹ (CV 39%)
    Vc = 19.9 L (CV 29%), Vt = 30.9 L (CV 35%)
    fu 평균 0.016 ± 0.0049; EC₅₀(total) = 1.8 µg·L⁻¹, Emax = 2.1, n = 2.1
    반응 8배 IIV (0.5–4.0 response units) — 혈장단백결합으로 일부만 설명됨
- R&T 실제 임상 수치 반드시 앵커링:
    nortriptyline 25mg tid / 263명 (Fig. 12-2), log-normal 분포
    warfarin 일일 용량 범위 (Fig. 12-1), theophylline 350mg 5명 (Fig. 12-21)
    CpD 데이터(PK50)와 연결해 unbound vs total 변이 대비 논의
- Do not reproduce or embed copyrighted textbook figures unless
  Image rights = User-supplied OR Open-license source with attribution.
=================
거장의 시각 — 이 Scope Lock을 쓴 이유:
두 소스는 역할이 엄격하게 분리됩니다. R&T는 "왜 사람마다 다른가"의 임상·생리학적 언어를, G&W PK50은 "그 변이를 데이터에서 어떻게 꺼내는가"의 실험적 증거를 담당합니다. 이 두 축이 합쳐질 때 비로소 학습자는 OMEGA 행렬의 숫자 하나가 "간부전 환자에서 $C_l
이 왜 달라지는가"라는 생물학적 현실을 코딩한 것임을 직관으로 읽게 됩니다. Scope Lock의 페이지 범위와 실제 수치 앵커링은 그 직관이 추상에 머물지 않도록 못박는 장치입니다.
Phase 1 진행 시 주의사항
① Ch.13 MUST/CONTEXT 분리 선제 선언 필수
Ch.13은 18페이지에 걸쳐 CYP2D6·2C9·2C19·TPMT·NAT2·UGT·약력학적 다형성을 모두 망라합니다. Phase 1 Curation Map에서 MUST: "유전적 다형성이 IIV의 불연속적 구조를 만드는 메커니즘" 하나로 수렴시키고, 개별 isoform 세부 사항(아세틸화·가수분해·hydrolysis 각론)은 CONTEXT 1–2문장 처리를 선언한 뒤 §2 작성을 시작해야 합니다. 그러지 않으면 §2 카드가 약리유전학 강의록이 됩니다.
② G&W Ch.4 EDA 내용의 역할 명확화
Ch.4의 spaghetti plot(4.2.2)·NAD/NPD(4.2.2)는 IIV 시각화와 population approach 도입 근거로 MUST 처리 가능합니다. 그러나 Lineweaver-Burke·Scatchard plot 선형화(4.2.4)·Euler 수치적분(4.6–4.7) 등은 이 세션의 핵심 축과 거리가 있으므로 CONTEXT 또는 생략이 적절합니다. Phase 1 Curation Map에서 이 경계를 명시적으로 그어야 합니다.
③ 두 소스의 역할 충돌 지점 사전 설정
R&T Ch.12는 ω²·σ²를 개념적으로 설명하고, G&W PK50은 동일 개념을 12명 실험 데이터로 앵커링합니다. 혼합 소스 처리 규칙대로 R&T = 임상·생리학적 의미 담당, G&W = 수치 앵커링·데이터 도출 담당으로 역할을 처음부터 분리해 §2 카드별 인용 출처가 뒤섞이지 않도록 해야 합니다.

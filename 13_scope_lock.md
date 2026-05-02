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

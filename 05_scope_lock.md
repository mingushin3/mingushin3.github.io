=== SCOPE LOCK ===

Source       : Gabrielsson & Weiner 5e (G&W) + Rowland & Tozer 5e (R&T)
               혼합 소스 운영 규칙:
                 G&W → 수식 도출·실험 데이터·재파라미터화 5종·수치 앵커링 담당
                 R&T → 임상 해석·분포 속도론 결과·PD 연결·용량 설계 담당

Chapter      : [G&W]  Ch.2 §2.4.1–2.4.6 (Multi-Compartment Models,
                       Reparameterization) + Case Studies PK7, PK8
               [R&T]  Ch.19 — Distribution Kinetics

Pages        : [G&W]  이론 p.57–77 / 케이스 p.505–517
               [R&T]  p.613–656

Chapter role : 2구획 모델의 구조적 골격을 완성하는 세션.
               ① 이중지수 방정식 → 매크로상수(A, α, B, β) 도출 및
                  잔차법(method of residuals)을 통한 곡선 분리
               ② 미시상수(k₁₀, k₁₂, k₂₁, Vc) ↔ 생리적 파라미터
                  (Cl, Cld, Vc, Vt) 상호 변환 공식 체계
               ③ 재파라미터화 5종(매크로·미시·생리적·Takada·Colburn)의
                  수치적·조건수적 비교 — NONMEM 파라미터 선택의 직접 근거
               ④ V₁ / Vss / Vβ 개념 구분 및 임상 상황별 적용 기준
               ⑤ 분포 속도론이 Css 도달 시간·다회 투여 축적·
                  TDM·PD 해석에 미치는 임상적 파급력

               선행 개념: 1구획 모델, CL = Dose/AUC, Vd = CL/k, MRT
               후속 개념: NONMEM ADVAN3/11 파라미터 선택 근거,
                          Population PK 공변량 모델링에서 Vss vs. Vβ 선택,
                          η-shrinkage 해석

Learner      : PhD pharmacometrics student; clinical pharmacist background;
               PopPK entry–intermediate

Final output : Single self-contained HTML (Step 2)

Mode         : A-Critical
               근거: 수식·NONMEM 구현 선택·규제 파급력·임상 용량 결정
               4개 축이 교차. 재파라미터화 선택 오류 → $COV step 조건수
               폭등 → NDA Deficiency Letter 사유로 직결.

Image rights : None
               (교과서 원그림 임베드 불가; P/N 유형만 허용)

KEY DATA ANCHORS (Dynamic Source Anchoring — Phase 1 수식 복원 기준):
  [G&W Fig.2.43]  A ≈ 70 mg·L⁻¹, B = 28 mg·L⁻¹
                   α = ln(70/10)/130 min⁻¹, β = ln(28/10)/450 min⁻¹
  [G&W PK7]       Div = 100 µg; AUC = 250 µg·min/L; CL = 0.4 L·min⁻¹
                   MRT = 280 min; Vss = 110 L
  [G&W PK8]       Compound X, Div = 100 µg IV bolus (Colburn 1983)
                   5종 모델 WRSS 비교 (Table 8.1)
  [R&T Aspirin]   650 mg IV bolus
                   C = 67e⁻⁰·²³ᵗ + 33e⁻⁰·⁰⁵ᵗ mg/L
                   CL = 683 mL/min; V₁ = 6.5 L; V = 13.7 L; Vss = 10.4 L
  [R&T Nicardipine] t½(β) ≈ 12 hr; 50% Css 도달 ≈ 1 hr (Fig.19-10)
  [R&T Gentamicin]  terminal t½ = 87 hr (환자 개인값)
                    first phase t½ ≈ 4 hr; f₂ ≈ 0
                    accumulation index (terminal term) = 16

HARD RULES:
- Do not expand beyond the page ranges above.
- Do not fabricate values, experimental conditions, or page citations
  absent from the source PDFs.
- [확인 필요] = flag and retain; never delete unverifiable content.
- Do not reproduce or embed copyrighted textbook figures.
=================

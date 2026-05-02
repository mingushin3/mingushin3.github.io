=== SCOPE LOCK ===

Source       : [혼합] Gabrielsson & Weiner 5e (G) + Rowland & Tozer 5e (R&T)

Chapter      :
  [G] Ch.2 §2.6 Turnover (§2.6.1–§2.6.7) +
      Case Study PK26 (Efalizumab — 항체 PK 모델링) +
      Case Study PK27 (Target Mediated Drug Disposition)
  [R&T] Ch.21 Protein Drugs

Pages        :
  [G]   §2.6:    p.94  – p.111
        PK26:    p.599 – p.601
        PK27:    p.602 – p.610
  [R&T] Ch.21:   p.687 – p.730

Chapter role :
  항체/단백질 의약품의 비선형 PK를 지배하는 두 가지 핵심 원리 —
  (1) Turnover: 내인성 물질 항상성의 수학적 골격 (kin/kout 패러다임);
  (2) TMDD: 표적 매개 배치의 기계론적 완전 모델 vs. Michaelis-Menten 근사 —
  을 통합적으로 체화하는 세션.
  선행 필수: 1구획 선형 PK, Michaelis-Menten 효소론.
  후행 개방: mAb PopPK 모델링, QSP/PBPK, 규제 제출용 PK/PD 섹션 작성,
             FcRn 조작을 통한 반감기 연장 전략 (next-gen biologic engineering).
  이 세션 없이 mAb 임상 개발 PopPK 보고서를 작성하면 TMDD 비선형성을
  단순 MM으로 처리하고 저농도 외삽에서 체계적 바이어스를 보고하는 상황이 발생한다.

Learner      : PhD pharmacometrics student; clinical pharmacist background;
               PopPK entry–intermediate; NONMEM 실습 경험 보유

Final output : Single self-contained HTML (Step 2, V5.1 Apex Edition)

Mode         : A-Critical
  근거: TMDD 수식 구조(8-파라미터 완전 모델), MM 근사 타당성 경계,
        FcRn/Fcγ 기전, 비선형성과 PD의 공통 메커니즘,
        규제(NDA/IND) PopPK 섹션 파급력이 모두 최고 수준.

Image rights : None
  → I-type figure 비활성. 교과서 원그림(Fig.27.2, Fig.27.3, Fig.21-8, Fig.21-9)은
    FIGURE_POINTER(P-type)로만 안내.

Role split (혼합 소스 처리 규칙):
  [G]  §2.6 + PK26/PK27 = 수식 도출·데이터 앵커링·ODE 구조 담당
         실제 실험 데이터 100% 인용 필수 (Efalizumab 5용량 i.v.,
         단클론 항체 1.5/5/15/45 mg·kg⁻¹, IgX sc 40 µg·kg⁻¹,
         r-hSOD 정상/신절제 랫트, 에스트라다이올 폐경 후 여성 15명)
  [R&T] Ch.21 = 생리학적 기전·임상 해석·ADME 병태생리학 담당
         실제 임상 수치 인용 필수 (Table 21-6 Vd, Table 21-14 F,
         Table 21-15 mAb 반감기, Fig.21-7 Efalizumab PK,
         Table 27.2 파라미터 정밀도 비교)

HARD RULES (apply to all phases):
- Do not expand beyond stated page ranges.
- Do not fabricate values, experimental conditions, or page citations.
- [확인 필요] = flag and retain; never delete unverifiable content.
- Do not reproduce or embed copyrighted textbook figures
  (Image rights = None → placeholder + FIGURE_POINTER only).
- Michaelis-Menten 근사 유효 범위(C ≫ R₀ 또는 target occupancy ≥ 90–95%) 외
  적용 시 "고위험 근사 오류"로 명시.
- TMDD 파라미터 표기는 PK27/R&T Ch.21의 통일 표기(kon, koff, kin, kout,
  ke(RL), R₀, Km, Kd)를 엄격히 준수; 문헌별 혼용 표기 충돌 시 [복원] 처리.
=================

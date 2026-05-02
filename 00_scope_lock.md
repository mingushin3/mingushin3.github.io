=== SCOPE LOCK ===

Source       : Gabrielsson & Weiner 5e (G) + Rowland & Tozer 5e (T) — 혼합 소스
               G: Chapter 1 — General Principles
               T: Chapter 1 — Therapeutic Relevance
                  Chapter 2 — Fundamental Concepts and Terminology

Pages        : G: p.1 – p.7
               T: p.3 – p.49

Chapter role : "Pre-Sprint 철학·용어 기반 세션 —
               모든 후속 PopPK 세션의 인식론적 토대를 구축한다.
               이 세션 없이는 모델 선택의 근거, 파라미터 해석의 방향,
               GOF 판단의 언어 자체가 흔들린다.

               G Ch.1은 모델링의 존재론적 정당성과 방법론적 규율을
               확립한다 — '왜 모델링하는가', '어떤 순서로 사고하는가'
               (Modeling Carousel), '수식 노예화·소프트웨어 맹신'이라는
               5대 dysfunction 방어법.

               T Ch.1–2는 PK/PD를 임상 의사결정의 언어로 번역한다 —
               용량 설계의 합리적 근거(Therapeutic Window), PK↔PD
               두 국면의 비분리성, Emax/C50/Hill 방정식이라는 농도-반응
               정량화의 핵심 수식 체계, 그리고 turnover 개념이라는
               지연 반응 이해의 열쇠.

               선행 지식: 없음 (진입점 세션)
               후속 개방: 1구획·다구획 모델, 청소율·분포용적 체계,
               비선형 PK(Michaelis-Menten), TDM 임상 적용,
               PopPK IIV/RUV 모델 선택 논리 전체."

Learner      : PhD pharmacometrics student; clinical pharmacist background;
               PopPK entry–intermediate

Final output : Single self-contained HTML (Step 2)

Mode         : B-Standard
               # 근거: 수식 도출보다 개념 정착이 목적인 세션이나,
               # Emax/Hill 방정식(규제 PD 모델의 핵심)·Turnover
               # 개념(간접 반응 모델 선행 개념)·모델링 Carousel
               # (NONMEM 워크플로 철학의 원형)은 PhD 수준 체화가
               # 요구되어 C-Fast-Safe 아님.
               # GOF 판단·파라미터 초기추정치 오류(Local minimum)
               # 등 실무 파급력도 있어 Phase 2 감사 생략 부적절.

Image rights : None
               # G Fig.1.1(Modeling Carousel), G Fig.1.2(Parameter space /
               # Local minimum), T Fig.1-2(PK→PD rational approach),
               # T Fig.1-3(PK/PD linked), T Fig.1-4(Therapeutic Window),
               # T Fig.1-5(Accumulation regimens), T Fig.2-1(Cmax/tmax),
               # T Fig.2-4(ADME physiologic diagram), T Fig.2-5(Compartments),
               # T Fig.2-7(Model types), T Fig.2-11(Ketamine Emax),
               # T Fig.2-16(Hill steepness), T Fig.2-18(Quantal alfentanil)
               # 모두 저작권 보호 도서 — Image rights = None.
               # Phase 4C에서 FIGURE_POINTER(P) 모드만 허용.
               # G Fig.1.2(Local minimum OFV landscape)는 ESSENTIAL 후보:
               # 파라미터 공간 기하학 직관에 대체 불가.
               # T Fig.1-3, T Fig.2-11은 ESSENTIAL 후보:
               # PK↔PD 통합 구조, Hill 곡선 형태 없이 텍스트만으로
               # 전달 불충분.

HARD RULES (apply to all phases):
- G Ch.1과 T Ch.1–2의 페이지 범위를 벗어난 내용 확장 금지.
- Modeling Carousel 6단계, Emax/C50/Hill γ 수치,
  warfarin 실험 데이터(Nagashima et al. 1969), alfentanil C50 수치
  (breast 0.27, lower abdomen 0.31, upper abdomen 0.42 mg/L),
  propranolol γ≈1·C50=5.3 μg/L, total body water turnover 수치
  (2.5 L/day, 0.06 day⁻¹, 17 days) — 모두 출처 기반 인용 필수.
  가상 수치로 대체 금지.
- [확인 필요] = flag and retain; never delete unverifiable content.
- 두 소스의 역할 분담 엄수:
  G → 모델링 철학·방법론적 규율 담당
  T → 임상 기전·PK/PD 언어·정량적 수식 체계 담당
- 저작권 도서 figure 직접 임베드 금지 (Image rights = None).
=================

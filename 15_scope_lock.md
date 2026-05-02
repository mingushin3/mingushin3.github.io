=== SCOPE LOCK ===

Source       : Gabrielsson & Weiner 5e
               (Pharmacokinetic and Pharmacodynamic Data Analysis:
               Concepts and Applications)

Chapter      : Ch. 4 §4.4, §4.7–4.10 + Ch. 5 §5.2.3–5.2.4, §5.3.3
               — 모델링 전략: 초기값 추정 · GOF 진단 · 경쟁 모델 판별 ·
                 실험 설계 (편미분 · 민감도 분석 · 독성동태 설계)

               ⚠ 누락 구간 명시:
               §4.5(Minimization)·§4.6(Weighting), pp.365–367은
               업로드 PDF에 포함되지 않음. Phase 1은 해당 구간을
               임의 보완하지 않는다. 언급이 필요한 경우 [확인 필요]로
               플래그 처리 후 유지.

Pages        : p.352–364 (§4.4)
               p.368–392 (§4.7–4.10)  ← pp.365–367 업로드 부재
               p.399–414 (§5.2.3–5.2.4, §5.3.3)

Chapter role : "모델링 캐러셀(modeling carousel)의 실행 척추 —
               탐색적 데이터 분석(EDA)에서 초기값 획득(§4.4),
               잔차 기반 GOF 판독(§4.7), 경쟁 모델 선택(§4.8),
               이상치 처리(§4.9), 편미분 기반 최적 샘플링 시점 도출(§5.2.3),
               민감도 분석으로 실험 재설계(§5.2.4)까지 이어지는
               PK/PD 모델러의 핵심 실전 기술 사이클.
               §4.4에서 배운 초기값이 왜 중요한지는 §4.7의 수렴 이론,
               §4.8의 F 검정 적용 조건, §5.2.3의 최적 설계점이
               모두 전제로 한다. 이 섹션 없이는 규제 제출용
               모델 선택 근거를 논리적으로 방어할 수 없다.
               §5.3.3(독성동태 설계)은 CONTEXT 처리 — MUST 카드
               신설 금지."

Learner      : 박사과정 계량약리학 학생 (임상약사 배경;
               PopPK 입문~중급 수준); 기본 비선형 회귀 개념 보유,
               NONMEM 실행 경험 있음, GOF 플롯 해석 및
               모델 비교 기준 체계화 필요 단계

Final output : 단일 self-contained HTML (Step 2)

Mode         : A-Critical
               근거: (1) 수식·통계 도구(WRSS, F*, AIC, SC, 편미분)가
               규제 제출(NDA/IND)에서 모델 선택 근거로 직접 인용됨.
               (2) F 검정의 nested/non-nested 적용 조건 혼동은
               Deficiency Letter 사유. (3) 초기값 품질이 수렴 실패의
               직접 원인이며, 이는 모든 후속 모델링 신뢰성을 결정.
               (4) 편미분 기반 샘플링 설계를 이해하지 못하면
               최적 설계 시험을 기획할 수 없음.

Image rights : None
               (교과서 원도 재현 불가; §3 SVG 다이어그램 및
               §4 인터랙티브 시뮬레이터로 학습 목적 구현)

HARD RULES (apply to all phases):
- Do not expand beyond this page range.
- pp.365–367 누락 구간: 임의 보완 금지. 언급 필요 시 [확인 필요] 처리.
- 모든 실험 수치(동물종, 화합물명, 투여 경로, 실제 파라미터 수치,
  Table 4.3·4.4·4.5·4.6·4.7 데이터)는 소스 PDF 직접 인용 필수.
  가상 수치 생성 절대 금지.
- [확인 필요] = flag and retain; never delete unverifiable content.
- Do not reproduce or embed copyrighted textbook figures.
  (Figure 4.17–4.59, Figure 5.4–5.10 등 원도 임베드 금지)

---

[거장의 부가 지침 — Step 1 실행 전 반드시 숙지]

이 섹션의 핵심 함정 3가지:

① 초기값 실패 함정
   - "소프트웨어가 초기값을 자동 추정해주므로 괜찮다"는 착각이
     nonlinear 모델에서 local minimum 수렴을 유발한다.
   - p.352–353에서 Gabrielsson이 Hill equation의 실제 경험을
     구체적으로 서술 — 이 서술을 100% 인용할 것.

② F 검정 적용 조건 혼동 (규제 파급력 최대)
   - Michaelis-Menten 소실 vs 1차 소실 비교에 F 검정 적용 시도
     (unnested + 다른 weighting → 이중 위반, Table 4.8에 명시).
   - 이 혼동은 Deficiency Letter 실제 사유 — Critical Blow 행 지정.

③ 상관계수(r) 오용 함정
   - r = 0.96(OLS)이 r = 0.94(IRLS)보다 "더 좋은 모델"이라는
     오판 — p.382 Figure 4.53 실제 데이터로 해부할 것.

Dynamic Source Anchoring 필수 대상 수치:
- Fig 4.17: 두 피험자 IV bolus 10 mg
  K = 0.01 min⁻¹, t½ ≈ 65 min, AUC = 100,000 µg·L⁻¹·min,
  Cl = 0.1 L·min⁻¹, V = 10 L
- Fig 4.18: A=1, B=0.8 µg·L⁻¹, α=0.05, β=0.003 min⁻¹
- warfarin-PCA (§4.4.1.3, Eq. 4:22):
  kout = 0.03 h⁻¹ (slope = ln(124)−ln(56.77) / (0−24))
- Table 4.3: 간접반응모델 최종 파라미터 추정값 전체 수치
- Table 4.4: A=100, α=0.01, B=1, b=0.05 (이중지수 경계값)
- Table 4.5–4.7: in vitro 순수오차 분석 전체 수치
  (FLOF = 15.35, Fcrit = 2.76)
- §5.2.3: α=0.69 h⁻¹, β=0.069 h⁻¹ → 최적 샘플링 1.4 h, 14 h
- §5.2.4: Case Study PK18·PD4 민감도 분석 파라미터 수치

=================

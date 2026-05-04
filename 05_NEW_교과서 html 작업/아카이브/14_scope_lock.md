=== SCOPE LOCK ===

Source       : Gabrielsson & Weiner 5e (Vol I — Data & Theory)
                 + Rowland & Tozer 5e (Vol I — Clinical Theory)
Chapter      : G&W: §2.10 Inter-Species Scaling + Case Study PK28 (Elementary Dedrick)
                     + Case Study PK29 (Complex Dedrick) [pp. 170–191, 611–620]
               R&T: Ch.14 Age, Weight, and Gender [pp. 411–441]
                     + Ch.22 Allometry & Disposition Kinetics [pp. 731–743]
Pages        : G&W p. 170–191 (§2.10) / p. 611–620 (PK28–29)
               R&T p. 411–441 (Ch.14) / p. 731–743 (Ch.22 allometry 섹션)
Chapter role : "종간 외삽(allometric scaling)의 이론·수식·실험 데이터 앵커 챕터.
                Phase I FIH 용량 선택, 소아 용량 설계, PBPK 모델의 시스템 파라미터
                스케일링 전 과정의 수학적 기반. 이 개념 없이는 PK28/29 코드 해석,
                소아 PopPK 공변량 모델(BSA·WT 지수 선택), 규제 제출용 FIH 용량
                정당화 섹션 작성이 모두 불가능하다."
Learner      : PhD pharmacometrics student; clinical pharmacist background;
               PopPK entry–intermediate level
Final output : Single self-contained HTML (Step 2)
Mode         : A-Critical

Image rights : None
               # 교과서 Figure 삽입 불가.
               # Figure 2.143, 2.145, 2.148, 2.150, 2.156, 2.158 (G&W)
               #   및 Fig. 14-7, 14-20, 22-1, 22-4, 22-6 (R&T)는
               #   Pointer(P) callout으로 처리하고 직접 임베드하지 않는다.

DUAL-SOURCE INTEGRATION RULES:
  - G&W = 수식 도출 · 실험 데이터 앵커링 (methadone, compound X 실측치) 전담
  - R&T = 임상 해석 · 연령/체중/성별 보정 · 규제 언어 전담
  - 두 소스 수식이 충돌할 경우 G&W 수치 우선, R&T 임상 프레임으로 해석
  - 가상 수치(X약물, Y환자) 절대 금지 — 책에 등장하는 실제 화합물만

HARD RULES (apply to all phases):
  - Do not expand beyond the specified page ranges.
  - Do not fabricate values, experimental conditions, or page citations
    absent from the source PDFs.
  - [확인 필요] = flag and retain; never delete unverifiable content.
  - Do not reproduce or embed copyrighted textbook figures.
    (Image rights = None → all figures as Pointer callout only)
=================
거장의 시각에서 본 이 세션의 핵심 판단:
이 챕터가 A-Critical인 이유는 세 가지입니다. 첫째, Y=a⋅BWbY = a \cdot BW^b
Y=a⋅BWb라는 단순해 보이는 수식이 실제로는 FIH 초기 용량 선택의 법적 근거가 되는 수식이라는 점. 둘째, 지수 bb
b의 선택 오류(0.75 vs 1.0 혼동)가 마우스-인간 간 3,000배 체중 차이에서 7.7배 오차로 증폭된다는 점. 셋째, G&W의 메타돈(PK28: mouse/rat/man, IV bolus 25/500/100,000 µg)과 compound X(PK29: 5종, 3,500배 체중 범위)라는 구체적 실험 데이터가 있어 수식이 실제 어떻게 작동하는지를 수치로 검증할 수 있다는 점입니다.
Phase 1 진행 시 주의사항
① Curation Map 우선 결정 필수 — R&T Ch.14 압축 전략
R&T Ch.14는 30페이지이지만 allometric scaling의 MUST 항목은 실질적으로 세 곳입니다: BSA 산출식(Eq.14-1, 14-2), 소아 유지용량 공식(Eq.14-5, 14-6), 그리고 Fig. 14-7(크레아티닌 청소율-연령 곡선). 흡수 변화·성별 차이·Study Problems는 전부 CONTEXT 1–2문장 처리 선언을 Curation Map에 명시해두어야 §2 카드 과부하를 막을 수 있습니다.
② 두 소스의 지수 표기 충돌 사전 인지
G&W는 clearance 지수를 bb
b, volume 지수를 dd
d로 구분합니다. R&T Ch.22는 같은 지수를 bb
b로 통일 표기하며 문맥으로 구분합니다. §2 카드 작성 시 두 표기법을 명시적으로 정렬하지 않으면 §5 혼동쌍이 자동 생성되는 오류가 발생합니다. Phase 1 §2-B(Derivation) 작성 시 "G&W 표기 기준, R&T 대응 표기 병기" 형식을 고정하십시오.
③ Data Anchoring 소스 2개 분리 명시 필수
G&W PK28(메타돈: mouse 23g/rat 250g/man 70kg, a=0.319a=0.319
a=0.319, t1/2t_{1/2}
t1/2​: 1.5/3.9/35h)과 PK29(compound X: 5종, a=0.021,b=0.74,c=0.076,d=1.18a=0.021, b=0.74, c=0.076, d=1.18
a=0.021,b=0.74,c=0.076,d=1.18)는 §4 시뮬레이터 기본값과 §6 시나리오 수치의 유일한 합법 출처입니다. R&T 수치(digoxin Vd, 크레아티닌 청소율 등)는 G&W 수치와 맥락 없이 혼용하지 말고 소스 출처를 각 수치 옆에 태그로 구분하십시오.

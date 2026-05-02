=== SCOPE LOCK ===

Source       : Gabrielsson & Weiner 5e
               "Pharmacokinetic and Pharmacodynamic Data Analysis"
Chapter      : Chapter 3 — Pharmacodynamic Concepts
               + Case Study PD3 — Inhibitory Imax Model
Pages        : p.199–p.224 (§3.1–§3.6.1) +
               p.229–p.234 (§3.6.6–§3.6.7: 반응 동력학, AUEC) +
               p.732–p.741 (PD3 케이스 스터디)
               ※ pp.225–228(§3.6.2–§3.6.5, 경쟁길항 이후 상호작용
                 모델 연속)은 첨부 PDF에 없음 — 해당 범위 내용은
                 추정하거나 보완하지 않고 [확인 필요]로 표시할 것.
Chapter role : PD 모델링의 실험 데이터 기반 개념 기초.
               수용체 결합 이론(질량작용법칙, §3.3) →
               농도-반응 모델 계보(선형 → Emax → Sigmoid Emax →
               Composite Emax, §3.5) → 비평형 동력학 개요(§3.6.6) →
               AUEC 도출(§3.6.7) 의 구조적 흐름을 확립함.
               이 챕터에서 확립한 Emax/EC₅₀/Hill-n 파라미터 개념이
               간접반응 모델(kin/kout) 및 Effect Compartment 세션의
               직접 선행 요건이 됨. (해당 개념 자체는 R&T Ch.8에서 전개)
Learner      : PhD pharmacometrics student; clinical pharmacist background;
               PopPK entry–intermediate
Final output : Single self-contained HTML (Step 2)
Mode         : A-Critical
               (수식 도출 + 실험 데이터 앵커링 + 규제 파급력 모두 존재)

Image rights : None
               # 교과서 원그림 임베드 불가. Pointer(P) 또는 Redraw(R) 방식 사용.

HARD RULES (apply to all phases):
- Do not expand beyond this page range.
- pp.225–228은 첨부 파일에 부재. 해당 구간 내용은 절대 추정·보완
  하지 말 것. 언급이 필요한 경우 [확인 필요 — 첨부 PDF 미포함 구간]
  으로 플래그 처리.
- Do not fabricate values, experimental conditions, or page citations
  absent from the source PDF.
- Dynamic Source Anchoring 필수:
    PD3 실험 데이터(혈압, steady-state):
      E₀ = 175 mmHg (그래픽 추정) / 확정: E₀ = 171
      Imax ≈ 35 mmHg (그래픽 추정) / 확정: Imax = 34.7
      IC₅₀ ≈ 120 µg·L⁻¹ (그래픽 추정) / 확정: IC₅₀ = 140
      n ≈ 2 (그래픽 추정) / 확정: n = 2.03
      (0–800 µg·L⁻¹ 범위, Sigmoid Imax 모델)
    Lundström et al. [1992] 복합 Imax 데이터:
      IC₅₀₁ = 1.8, IC₅₀₂ = 23 µg·L⁻¹;
      Imax,1 = 4, Imax,2 = 3.2; n₁ = 1.4, n₂ = 3.7
    Remoxipride: 600 mg/day, t½(반응) = 1–2주 vs. t½(혈장) = 5–10 h
    위 수치를 §4 시뮬레이터 기본값 및 §6 시나리오에 직접 사용할 것.
- [확인 필요] = flag and retain; never delete unverifiable content.
- Do not reproduce or embed copyrighted textbook figures.

=================
=== SCOPE LOCK ===

Source       : Rowland & Tozer 5e
               "Clinical Pharmacokinetics and Pharmacodynamics"
Chapter      : Chapter 8 — Response
Pages        : p.233–p.264
Chapter role : PK/PD 통합 임상 개념의 핵심 관문.
               농도-반응 관계의 시간적 맥락(시간 지연, 히스테리시스,
               직접/간접 링크, 간접반응 모델)을 생리학적 메커니즘으로 설명.
               효과 지속 시간의 로그-용량 비례성 및 효과 구획 개념 확립.
               이후 다구획 모델, 간접반응 모델(kin/kout),
               만성 투여 반응 세션의 직접 전제 개념군.
Learner      : PhD pharmacometrics student; clinical pharmacist background;
               PopPK entry–intermediate
Final output : Single self-contained HTML (Step 2)
Mode         : A-Critical
               (임상 메커니즘 + 생리학적 시스템 + 규제 PK/PD 파급력)

Image rights : None
               # 교과서 원그림 임베드 불가. Pointer(P) 또는 Redraw(R) 방식 사용.

HARD RULES (apply to all phases):
- Do not expand beyond this page range.
- Do not fabricate values, experimental conditions, or page citations
  absent from the source PDF.
- Dynamic Source Anchoring 필수:
    Digoxin: 1 mg i.v. bolus, 6명 정상 피험자 (Shapiro et al. 1970),
             4시간 이내 혈중농도 하강 + 좌심실 박출 시간 지수 상승
    Naproxen: 500 mg 경구, 치과 통증 모델, 비결합 농도 vs. 통증 완화
              반시계 방향 히스테리시스 (Syntex USA Inc., 1994)
    Warfarin: 1.5 mg/kg 경구 (sodium salt), 5명 남성 피험자 (Nagashima 1969)
              프로트롬빈 복합체 반감기 1–2일, 반응 최대 1–2일 후
    Succinylcholine: 0.5 mg/kg i.v. bolus, 근마비 80%→20% 선형 소실
                     k = 0.2 min⁻¹, t½ ≈ 4 min (Walts & Dillon 1967)
    Methylprednisolone phosphate: 16–1000 mg, 6명 피험자, 선형 PK
                                   비선형 림프구 감소 반응 (Derendorf 1991)
    — 이 수치를 §4 시뮬레이터 기본값 및 §6 시나리오에 직접 사용할 것.
- [확인 필요] = flag and retain; never delete unverifiable content.
- Do not reproduce or embed copyrighted textbook figures.

=================
Phase 1 진행 시 공통 주의사항

Vol I 소스 분기 적용: 두 소스 모두 Vol I(이론) 분류이므로 §2-B는 "NONMEM 코드 블록" 대신 "단계별 수식 도출 + 생리학적 항 주석"으로 전개. $DES 코드 구조 작성 절대 금지.
Scope Lock A 전용: §3.6.2–§3.6.5 구간은 Phase 1에서 언급하지 않거나 [확인 필요] 처리. Curation Map 작성 시 해당 구간의 개념(예: 비경쟁적 길항)을 MUST 항목으로 설정하지 말 것.
두 Scope Lock 동시 처리 시: Gabrielsson은 수식 도출·실험 데이터 앵커링 담당, R&T는 임상·시간적 해석 담당으로 역할 분리 후 통합. 혼합 소스 처리 규칙에 따라 Big Idea 블록부터 출처를 명확히 구분.

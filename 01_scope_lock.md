=== SCOPE LOCK ===

Source       : Gabrielsson & Weiner 5e (Vol I — 데이터 이론) +
               Rowland & Tozer 5e (Vol I — 임상 이론) [혼합 소스]

Chapter      : [G] Ch.2 §2.2.1–2.2.3 — One-Compartment Models
                   (IV Bolus, Constant Rate Infusion, CL/V Integration)
               [G] §2.2.4–2.2.5 — Extravascular Administration
                   [CONTEXT 처리 우선; Ka·F는 MUST 승격 금지]
               [G] Case Study PK1 — One-compartment IV bolus dosing
                   [적용·계산 실습 앵커; 이론 확장 금지]
               [R&T] Ch.3 — Kinetics Following an Intravenous Bolus Dose

Pages        : [G]  본문: p.14–32  ← 비연속
                    응용: p.469–475 (Case Study PK1)
               [R&T] p.53–76
               ※ 비연속 범위 주의: G 본문부와 응용부 사이(p.33–468)는
                 본 세션 범위 밖. 확장 금지.
               ※ 총 합산 ~57페이지 (G: 26+7 / R&T: 24) — A-Critical 단일
                 세션 상한에 근접. Phase 1 작성자는 §2 카드 수를 CL·V·t½·K
                 핵심 4개 + MRT 1개 이내로 제한할 것.

Chapter role : 계량약리학 전체 체계의 출발점.
               【핵심 목적】 CL·V·t½·K 4파라미터의 정의·도출·
               상호의존 관계("t½은 CL과 V의 함수이지 역이 아님")를 확립.
               이후 다구획 모델, 비선형 PK, 간/신 청소율,
               PopPK 공변량 모델링의 선행 필수 지식.
               【부수 목적 — CONTEXT 수준】 흡수 파라미터(Ka·F·t_lag)는
               이 챕터에 등장하나 별도 세션(흡수 모델 세션) 주제이므로
               본 세션에서 CONTEXT 1–2문장 이상 확장 금지.

               혼합 소스 역할 분담:
               · Gabrielsson → 수식 도출·단계별 계산·실제 실험 데이터
                 (Compound A, 4명 지원자, 10 mg IV bolus, Table 1.1/1.2/1.3)
               · R&T → 생리학적 기전 해석·추출비 모델·
                 midazolam/creatinine/inulin 임상 예시·
                 MRT 개념·신장 청소율·분포와 소실의 경쟁 관계

Learner      : PhD pharmacometrics student; clinical pharmacist background;
               PopPK entry–intermediate

Final output : Single self-contained HTML (Step 2)

Mode         : A-Critical
               (CL·V·t½는 모든 PopPK 모델링의 추정 파라미터이자
                NDA/IND PopPK 보고서 핵심 기술 항목 —
                수식·표·규제 파급력 모두 최고 등급)

Image rights : None
               (교과서 원본 그림 임베드 불가;
                Fig.2.2/2.3/2.4/2.6/2.7/2.12/3-1/3-2/3-3/3-4/3-6은
                Pointer 처리 또는 신규 SVG로 재도식화)

HARD RULES (apply to all phases):
- Do not expand beyond this page range.
- Do not fabricate values, experimental conditions, or page citations
  absent from the source PDFs.
- Gabrielsson Table 1.1/1.2/1.3의 실제 수치(K, Cl, V, AUC, t½, MRT)를
  §2 도출 예시 및 §4 시뮬레이터 기본값으로 반드시 사용. 가상 수치 금지.
- R&T midazolam 실측값(Dose=7.5 mg base, AUC=287 µg·hr/L,
  CL=26 L/hr, t½=3.8 hr, V=142 L)을 §6 임상 시나리오에 반드시 인용.
- §2.2.4–2.2.5 (Ka·F) 내용은 CONTEXT 1–2문장 처리; 전용 카드 생성 금지.
- [확인 필요] = flag and retain; never delete unverifiable content.
- Do not reproduce or embed copyrighted textbook figures.
=================

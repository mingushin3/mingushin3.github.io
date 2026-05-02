=== SCOPE LOCK ===

Source       : Gabrielsson & Weiner 5e (Primary — 수식 도출·데이터 앵커링)
               + Rowland & Tozer 5e (Secondary — 임상 기전·치료역 해석)
               [혼합 소스: G = 수식·데이터 담당 / R&T = 임상·생리학적 의미 담당]

Chapter      : G:  Ch.2 §2.2.2  Constant rate infusion
                       §2.2.9  How does input to the plasma compartment vary?
                       §2.2.10 Multiple dosing
                       §2.2.11 Absorption from multiple sites
                   Case Study PK11 (Two-compartment repeated oral dosing)
                   Case Study PK13 (Bolus plus constant rate infusion)
               R&T: 치료역(Therapeutic Window), 항정상태(Steady State),
                    다중투여(Multiple Dosing), 축적(Accumulation) 대응 섹션

Pages        : G:  p.22–46 (§2.2.2–2.2.11)
                   p.528–531 (PK11)
                   p.537–539 (PK13)
               R&T: [확인 필요 — 07_T PDF 실제 페이지 확인 후 교체]
               # ⚠ R&T 페이지 미확정 상태.
               # Phase 2 T5 Coverage Audit 실행 전 반드시 실제 범위로 교체할 것.
               # 확정 전까지 Phase 1은 G 소스만을 주 텍스트로 처리하고,
               # R&T는 임상 해석 보완 소스로 참조에 한정한다.

Chapter role : "항정상태 농도를 결정하는 두 지배자(t½ → 도달 시간 / Cl → 농도 수준)의
               분리를 수식으로 체화하는 섹션.
               이 분리를 내면화하지 못하면 ①다중투여 NONMEM 데이터셋 구성(ADDL/II/SS),
               ②TDM 기반 용량 조정, ③항정상태까지의 농도 궤적 예측,
               ④flip-flop 동태 인식이 구조적으로 성립하지 않는다.
               PopPK 공변량 모델링의 Css 목표 설정 및
               Phase 1 다중투여 설계 근거 수식의 직접적 전제 지식."

Learner      : PhD pharmacometrics student; clinical pharmacist background;
               PopPK entry–intermediate

Final output : Single self-contained HTML (Step 2)

Mode         : A-Critical
               [근거: ①Css = Rin/Cl 및 R = 1/(1−e^(−kτ))은 TDM·NDA 용량 결정 핵심 수식;
               ②항정상태 가정 위반은 NONMEM SS=1/SS=2 코딩 오류로 직결;
               ③flip-flop 미인식은 Ka 방향 오류를 유발;
               ④다중투여 설계 근거 수식으로 규제 제출에 직접 사용됨]

Image rights : None
               [교과서 원그림 임베드 불가 — Figure Pointer(P) 모드만 운영]

HARD RULES (apply to all phases):
- Do not expand beyond this page range.
- Do not fabricate values, experimental conditions, or page citations
  absent from the source PDFs.
- [확인 필요] = flag and retain; never delete unverifiable content.
- Do not reproduce or embed copyrighted textbook figures unless
  Image rights = User-supplied OR Open-license source with attribution.
- G 소스: PK11·PK13의 실제 실험 수치를 §4 시뮬레이터 기본값 및
  §6 시나리오에 반드시 인용할 것.
  (PK11: 400 mg oral, tid Day5–9;
         A=70 mg/L, B=1 mg/L, Ka=0.7 h⁻¹, α=0.6 h⁻¹, β=0.07 h⁻¹;
         Emax=97%, EC50=0.8 mg/L
   PK13: bolus 400 µg/kg + infusion 800 µg/kg over 26 min;
         therapeutic window 50–300 µg/L;
         Vc=2.0 L/kg, Cl=1.0 L/min/kg, Cld=1.0 L/min/kg, Vt=5.0 L/kg)
- R&T 소스: 치료역 임상 수치 및 항정상태 판단 기준을 §2 임상 해석에 보완 인용.
  페이지 미확정 구간은 [확인 필요]로 플래그하고 삭제하지 말 것.

핵심 개념 사전 식별 (Curation Map 초안):
  MUST:
    M1. 정속 주입과 Css — Css = Rin/Cl; 도달 시간은 t½만이 결정 (G p.22–25)
    M2. 다중투여 축적인자 R — R = 1/(1−e^(−kτ)); τ/t½ 비율 의존 (G p.44–45)
    M3. 항정상태(Steady State) 정의 — 연속 주입 SS vs. 다중투여 SS의 개념 구분
    M4. Flip-flop 동태 — Ka > K 조건; terminal slope 오인 위험 (G p.45)
  CONTEXT:
    C1. 다중부위 흡수(§2.2.11) — 이중 피크, Frct 파라미터 (G p.46)
    C2. 주입–볼루스 동등성 변환 (Eq.2:31) — 다구획 일반화
    C3. Vss 추정 — 항정상태 낙하곡선 AUC법 (PK13 Eq.13:4)
=================
=== SCOPE LOCK ===

Source       : Rowland & Tozer, Clinical Pharmacokinetics and
               Pharmacodynamics, 5th Edition (R&T 5e)
Chapter      : Ch.9 — Therapeutic Window /
               Ch.10 — Constant-Rate Input /
               Ch.11 — Multiple-Dose Regimens /
               Appendix I — Amount of Drug in Body on
               Accumulation to Plateau
Pages        : p.267–358 + p.795–797 (Appendix I)
               ※ 총 약 93쪽. Phase 1 토큰 초과 시 Ch.11(p.319–358)
                 우선 완성 → "계속" 입력으로 Ch.9·10 처리.
                 Ch.11이 MUST-tier 핵심 세션이며, Ch.9·10은
                 그 선행 이론 맥락으로 위치함.
Chapter role : 용량요법 설계의 완전한 이론적 삼각형.
               Ch.9 = 치료 창의 benefit/risk 가중 도출 논리 —
               "왜 혈중농도를 표적으로 삼는가"의 철학적 기반.
               Ch.10 = 정속 주입 정상상태(Css = Rinf/CL) —
               고원 도달 시간이 half-life 단독으로 결정됨을
               수학적으로 확립.
               Ch.11 = 반복 투여 시 축적·평탄역·부하/유지용량
               수학 구조(Eq.11-1 ~ 11-25) — NDA/IND PopPK
               보고서에 직접 인용되는 규제 언어.
               선행 지식: CL·Vd·t½·F (Ch.3–7).
               후속 지식: 개체 변이(Ch.12), TDM(Ch.18),
               비선형 PK(Ch.16), 약물상호작용(Ch.17).
Learner      : PhD pharmacometrics student (1학기);
               clinical pharmacist background;
               PopPK entry–intermediate.
Final output : Single self-contained HTML (Step 2)
Mode         : A-Critical
               근거: 수식(Eq.11-3~11-22)·임상 수치 테이블
               (Table 11-1~11-7, Table 9-1)·규제 파급력
               전부 내포. Ch.11 핵심 수식군은 후속
               PopPK 워크플로우 전체의 구조적 전제.
Image rights : None
               모든 Figure는 P-type Pointer로만 처리.
               원그림 임베드·재현 절대 금지.

HARD RULES (apply to all phases):
- Do not expand beyond this page range.
- Do not fabricate values, experimental conditions, or
  page citations absent from the source PDF.
- [확인 필요] = flag and retain; never delete unverifiable
  content.
- Do not reproduce or embed copyrighted textbook figures
  unless Image rights = User-supplied OR Open-license
  source with attribution.
=================
Phase 1 진행 시 주의사항
1.  R&T [확인 필요] 플래그 처리
Phase 1 실행 시 R&T 소스 인용이 필요한 모든 지점에 [확인 필요 — R&T 페이지 미확정] 플래그를 인라인으로 달아 출력할 것. Phase 2 감사 전 삭제 금지.
2. G 소스 3개 범위의 통합 순서
§2.2.2(정속 주입) → §2.2.10(다중투여·축적) → §2.2.11(다부위 흡수) → PK11 → PK13 순서로 개념을 전개할 것. Case Study는 MUST 개념의 적용 사례로 배치하되 독립 카드로 분리하지 않아도 됨.
3. Css 결정 인자 분리 — 핵심 교육 목표
"도달 시간 = t½ 결정 / 도달 농도 = Cl 결정"이라는 두 지배자의 분리가 §2 Big Idea 블록에서 명시적으로 선언되어야 함. 이것이 이 세션의 Professional Moat 핵심이므로 §8C에서도 동일 구조로 수렴할 것.
Phase 1 진행 시 주의사항
4. 토큰 관리: 93쪽 A-Critical은 단일 Phase 1 실행 한계에 근접합니다. step2_V5.1 프로토콜의 토큰 절단 방지 지침(<!-- ✂ 여기까지 생성 완료 -->)이 발동될 가능성이 높으므로, "계속" 입력 준비를 미리 해두세요.
5. 큐레이션 지침 이동: 수정 전 Scope Lock의 "거장 보충 메모(MUST-tier 목록, 실제 수치 앵커링 목록)"는 Scope Lock에서 제거되었습니다. 이 내용은 Prompt 1의 CURATION DIRECTIVE 섹션 또는 별도 메모로 Phase 1 실행 시 함께 첨부하세요.
6. 챕터 우선순위 고정: Ch.11이 MUST-tier 핵심입니다. Phase 1이 중간에 절단되더라도 Ch.11 §2 카드(Rac, Cav,ss, 부하/유지용량)가 먼저 완성되어야 Step 2 HTML의 §4 시뮬레이터가 올바른 기본값을 가질 수 있습니다.

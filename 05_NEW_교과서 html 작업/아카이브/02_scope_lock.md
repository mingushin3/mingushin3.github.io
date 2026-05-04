=== SCOPE LOCK ===

Source       : 혼합 소스
               [Vol I-A] Rowland & Tozer 5e (R&T)
                 Ch.4 "Membranes and Distribution" p.77–118
                 Appendix B "Ionization and the pH Partition Hypothesis" p.763–765
                   ← 선수 지식 확인용 참조만. MUST 카드 생성 금지.
                 Appendix C "Distribution of Drugs Extensively Bound to Plasma
                   Proteins" p.767–773
                   ← 소용적 Vd MUST 카드 내 수식 도출 보조 소스.
                 Appendix D "Plasma-to-Blood Concentration Ratio" p.775–776
                   ← 혈장-혈액 농도비 MUST 카드 내 수식 도출 보조 소스.
               [Vol I-B] Gabrielsson & Weiner 5e (G&W)
                 Ch.2 §2.9.3–§2.9.5 p.163–169
                 PK47 "Plasma protein binding modeling" p.690–693

Chapter      : 분포의 생물학 — 막투과·분포용적·단백결합
               (Membranes, Volume of Distribution, and Plasma Protein Binding)

Pages        : R&T p.77–118, p.763–765(참조), p.767–773(보조), p.775–776(보조)
               G&W p.163–169, p.690–693

Chapter role : 이 섹션은 "왜 약물이 혈장 밖으로 나가는가, 얼마나 나가는가, 그리고
               무엇이 그 양을 결정하는가"에 대한 생물학적·수학적 토대를 확립한다.
               구체적으로: (1) 막투과의 물리화학적 결정인자(분자 크기·지질친화도·
               이온화도·수송체), (2) 분포 속도의 율속 단계(관류 제한 vs. 투과성 제한),
               (3) Vd의 수학적 구조와 생리학적 의미
               ($V = V_P + \sum V_{Ti} \cdot K_{pi}$),
               (4) 혈장단백결합($f_u$)과 조직결합($f_{uT}$)이 Vd를 지배하는 메커니즘,
               (5) 총 농도 대 비결합 농도($C$ vs. $C_u$)의 임상·규제적 선택 논리.
               이 개념 없이는 간 추출비 모델(Ch.5), covariate 모델링(albumin→Vd),
               PBPK 구획 설계, TDM 용량 조정이 구조적으로 불가능하다.

Learner      : PhD pharmacometrics student; 임상약사 배경; PopPK 입문-중급

Final output : Single self-contained HTML (Step 2)

Mode         : A-Critical
               근거: 핵심 수식(분포반감기, Vd-fu 관계, 소용적 모델)·
               임상 데이터(propranolol·warfarin·cephalosporin 실제 수치)·
               규제 언어(IND에서 $C_u$ 측정 권고, NDA에서 결합/비결합 동시 측정)·
               고파급력 혼동쌍($C$ vs. $C_u$, 관류제한 vs. 투과성제한, $V$ vs. $V_u$)
               네 가지 A-Critical 기준을 모두 충족.

Image rights : None
               (교과서 원도 재현 불가; §3 SVG 및 §4 시뮬레이터는 신규 생성으로 대체)

HARD RULES (apply to all phases):
- Do not expand beyond the page ranges above.
- Do not fabricate numerical values, experimental conditions, or page citations
  absent from the source PDFs.
  실제 데이터 앵커 (소스 기반 기준값):
    R&T: ibuprofen fu = 0.005 (albumin 43→28 g/L 시 fu' = 0.0077, 54% 증가)
         propranolol Vd–fu 선형관계 (6 controls + 15 hepatic disease patients,
         40 mg IV bolus, Eq.4-25)
         cephalosporins V–fu 선형 (fu→0 시 V intercept ≈ 7 L ≈ albumin Vd)
         warfarin 신증후군: V 9.4→13.7 L, CL 0.20→0.58 L/hr, t½ 36→18 hr,
         albumin 43→12.5 g/L (Table 4-12)
         thiopental 25 mg/kg IV bolus to dog (liver/muscle/fat 분포, Fig.4-13)
         indinavir 800 mg q8h HIV 성인 8명, CSF vs. plasma unbound (Fig.4-10)
    G&W: Compound 1 (PT = 0.3 and 50, n=2 sites) / Compound 2 (PT = 0.1 and 10,
         n=4 sites); Ka ≈ 6 concentration units (Eq.47:4)
         Table 47.1 전체 데이터 (Cu, fu, PT 실험값)
- [확인 필요] = flag and retain; never delete unverifiable content.
- Do not reproduce or embed copyrighted textbook figures (Image rights = None).

CURATION CONSTRAINTS (Phase 1 Curation Map 강제 조건):
- MUST-tier 개념 상한: 최대 6개.
  초과 시 가장 낮은 downstream 파급력 항목부터 CONTEXT로 강등.
- Appendix B (ionization/Henderson-Hasselbalch): CONTEXT-tier 고정.
  임상약사 PhD 선수지식. 별도 MUST 카드 생성 절대 금지.
  관련 내용은 "막투과 결정인자" MUST 카드 내 1–2문장 CONTEXT 처리.
- Appendix C·D: 독립 MUST 카드 금지.
  각각 소용적 Vd MUST 카드, 혈장-혈액 농도비 MUST 카드의
  B항(Derivation) 내 수식 보조 소스로만 활용.
=================
거장의 시각 코멘트 — 왜 이 조합인가:
두 소스는 같은 주제를 상보적 렌즈로 조명합니다. R&T는 *"분포가 왜 이 구조인가"* — 생리학·임상 기전 중심으로 막투과부터 Vd까지 체계적으로 전개합니다. G&W는 *"실제 결합 데이터를 어떻게 모델링하는가"* — PK47의 실험 수치(PT, Ka, n)와 비선형 fuf_u
fu​-CuC_u
Cu​ 관계를 정량적으로 다룹니다. 두 소스를 동시에 처리해야 **수식의 생물학적 의미(R&T)**와 **데이터에서 파라미터를 추출하는 실무(G&W)**가 동시에 체화됩니다.
Phase 1 진행 시 주의사항
①  Curation Map을 반드시 먼저 출력하고 MUST 6개 상한 준수
Ch.4의 소주제(막구조→수송체→관류/투과 제한→Vd→단백결합→조직결합→소용적 모델)가 모두 MUST로 올라올 경우 Step 1이 붕괴합니다. 관류 제한·투과성 제한은 하나의 카드로 통합하고, 소용적 모델(App.C)은 Vd 카드 B항 내 처리를 권장합니다.
② G&W PK47 데이터는 §2 B항 수치 앵커로만 사용
PK47은 독립 개념이 아니라 단백결합 MUST 카드의 Dynamic Source Anchoring 소스입니다. 별도 카드로 분리하면 세션이 비대화됩니다.
③ CC
C vs. CuC_u
Cu​ 혼동쌍은 §5 Critical Blow 지정 예약
G&W §2.9.3–§2.9.5 + Benet & Hoener [2003] 456개 약물 결론은 이 혼동쌍의 실무 파급력이 가장 크며, NDA/IND 규제 맥락과 직결됩니다. Phase 1 시작 전 이 쌍을 Critical Blow 후보로 미리 지정해두면 Curation Map 작성이 수월합니다.

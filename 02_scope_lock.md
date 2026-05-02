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

=== SCOPE LOCK ===
Source       : Gabrielsson J & Weiner D, "Pharmacokinetic and
               Pharmacodynamic Data Analysis: Concepts and Applications"
               5th ed. (Swedish Pharmaceutical Press, 2010)
               File IDs: 04_G (교재 발췌) / 04_T (강의 발췌)

Chapter      : Ch.2 §2.3 Plasma and Urine Data
                         §2.5 Clearance Concepts
               Ch.5  Case Study PK5 — One-Compartment IV Plasma/Urine I

Pages        : §2.3  pp. 48–56
               §2.5  pp. 77–94
               PK5   pp. 494–499

Chapter role : [Tier-1 Conceptual Foundation]
               본 범위는 약동학의 핵심 파라미터인 청소율(Cl)의
               생리학적·수학적 기반을 확립하는 챕터다.
               학습 위계상 세 개의 레이어로 구성된다.

               Layer A — 신장 청소율 (§2.3, pp.48–56)
                 · 신장 생리(GFR, 능동분비, 재흡수) → ClR 수식 유도
                 · ARE plot / Excretion Rate plot의 도시 원리 및 한계
                 · 혈장+소변 동시 비선형 회귀 (누적 소변배설량 모델)
                 → NONMEM 실무에서 fe 파라미터화 및 신기능 공변량
                   모델링의 직접 선행 지식

               Layer B — 청소율 개념 확장 (§2.5, pp.77–94)
                 · Well-stirred / Parallel tube / Distributed /
                   Dispersion 4개 간 청소율 모델의 수식 체계 비교
                 · 고추출 vs. 저추출 약물의 투여경로별
                   Css 및 unbound Css 의존성 (Table 2.9)
                 · In vitro–in vivo extrapolation (IVIVE):
                   Vmax, Km → Clint → ClH 스케일링의 함정
                   (single-point 법, MMP 보정계수 오류)
                 → PBPK/IVIVE 모델링 및 간기능 공변량 처리의
                   필수 선행 개념; Prof. Seunghoon Han 연구라인
                   (DallphinAtoM/PBPK) 과 직결

               Layer C — 실전 적용 (PK5, pp.494–499)
                 · IV bolus 250 mg 투여 후 혈장+소변 동시 피팅
                 · 통합해(analytic) vs. 미분방정식 모델 비교
                 · CV 가중법, 파라미터 정밀도 해석
                 → NONMEM $SUBROUTINE ADVAN1/TRANS2 +
                   소변 compartment ODE 코딩 실습의 직접 기반

Learner      : Ph.D. pharmacometrics student (PIPET Lab, entry–
               intermediate level); 임상약사 10년 배경 보유.
               수식 직관은 강하나 NONMEM 구현 경험은 아직 제한적.
               PopPK 논문 분석 시스템(PIPET-Vault v4.0) 병행 구축 중.

Final output : Single self-contained HTML (Step 2)

Mode         : §2.3 → B-Standard
                 (ARE/Rate plot: 임상약사 배경으로 직관 가능;
                  수식 유도 중심의 체계적 정리로 충분)
               §2.5 Well-stirred 모델 → A-Critical
                 (4가지 간 청소율 모델 수식 비교, IVIVE 함정,
                  고/저추출 약물의 투여경로 의존성:
                  PopPK 공변량 모델 선택에 직결; 오개념 발생 빈도 高)
               §2.5 in vitro/in vivo → A-Critical
                 (single-point 법의 오류, MMP 보정계수 영향:
                  AIMS BioScience 컨설팅 실무와 직결)
               PK5 → B-Standard
                 (수치 예제 + NONMEM 코딩 연결 포인트 명시)

Image rights : None
               # I-type figure 비활성화
               # 교재 원본 Figure 2.33–2.68, Figure 5.1–5.3은
               #   저작권 보호 대상; HTML 출력에 재현 금지.
               # 대신 개념도는 SVG/CSS로 자체 제작하여 대체할 것.

HARD RULES:
- §2.3, §2.5, PK5 범위 외로 확장 금지.
- 교재 수식 번호(2:83–2:236, 5:1–5:5) 인용 시
  반드시 해당 수식이 실제 페이지에 존재함을 확인 후 기재.
- [확인 필요] 플래그: 교재에 명시되지 않은 수치·조건·인용
  삽입 금지; 불확실한 내용은 플래그 후 유지.
- Table 2.9 (4개 모델 파라미터 비교)는 핵심 참조 테이블로
  HTML 내 자체 재구성 가능 (수치는 교재와 동일하게 유지).
- MMP 보정계수 Table 2.8 수치 재현 시 출처 명기 필수.
=================

=== SCOPE LOCK ===
Source      : Rowland M, Tozer TN. Clinical Pharmacokinetics and
              Pharmacodynamics: Concepts and Applications, 5th ed.
              Wolters Kluwer; 2011.
Chapter     : Ch.5 — Elimination
Pages       : p.119 – p.168
Chapter role: Clearance의 생리학적 의미(추출비·고유청소율·혈류),
              간·신 경로별 소실 메커니즘(여과·분비·재흡수),
              혈장단백결합·혈류·세포활성 변화가 CL/t½에 미치는
              영향을 정량적으로 제시하는 독립 챕터.
              [이 Scope Lock은 p.119–168 범위만 처리하며,
               타 챕터·부록으로의 확장 참조는 금지]
Learner     : PhD pharmacometrics student; 임상약사 10년 경력;
              PopPK 입문-중급; NONMEM/nlmixr2 학습 중
Final output: Single self-contained HTML (Step 2)
Mode        : A-Critical
              트리거 조건:
              (a) 추출비·고유청소율 수치가 잘못되면 PopPK
                  CL 파라미터 해석 전체가 왜곡됨
              (b) 간·신 소실 메커니즘 오류는 용량 조절 판단에
                  직결되므로 오류 허용 임계값 = 0
Image rights: None
              교재 Fig. 5-1 ~ 5-29는 저작권 보호 대상; 재현 금지.
              개념 다이어그램은 독자 제작 SVG로만 대체할 것.

HARD RULES:
* p.119–168 범위를 벗어나는 확장 금지
* 수치(QH=1.35 L/min, GFR=120 mL/min 등) 출처 없이
  변경·생략 불가
* [확인 필요] 태그 사용 후 보존; 삭제 금지
* 교재 Figure를 HTML에 임베드하지 말 것
* 타 챕터(Ch.20, App.D·E) 내용 인용 시 → [확인 필요] 태그 부착
=================

=== SCOPE LOCK ===
Source      : Rowland M, Tozer TN. Clinical Pharmacokinetics and
              Pharmacodynamics: Concepts and Applications, 5th ed.
              Wolters Kluwer; 2011.
Chapter     : Ch.20 — Metabolites and Drug Response
Pages       : p.657 – p.686
Chapter role: 대사체 PK의 종합 응용 챕터.
              속도제한단계(형성 vs. 소실 rate-limiting),
              AUC(m)/AUC 비율을 통한 청소율 비교,
              간 추출 및 first-pass 효과가 대사체 농도에 미치는
              영향, 정상상태·다중투여·신기능 저하 시 대사체 용량
              조절 시나리오, 상호전환(interconversion) 및 비선형성
              을 포괄하는 독립 챕터.
              [이 Scope Lock은 p.657–686 범위만 처리하며,
               타 챕터·부록으로의 확장 참조는 금지]
Learner     : PhD pharmacometrics student; 임상약사 10년 경력;
              PopPK 입문-중급; NONMEM/nlmixr2 학습 중
Final output: Single self-contained HTML (Step 2)
Mode        : A-Critical
              트리거 조건:
              (a) fm, CL(m), V(m) 오류는 parent-metabolite
                  연결 PopPK 구조를 직접 왜곡함
              (b) 신기능 저하 용량 조절 시나리오는 임상 안전성에
                  직결; 오류 허용 임계값 = 0
Image rights: None
              교재 Fig. 20-1 ~ 20-15는 저작권 보호 대상; 재현 금지.
              AUC 비율·rate-limiting 개념도는 독자 제작 SVG로만
              대체할 것.

KEY EQUATIONS TO PRESERVE EXACTLY:
  Eq.20-1  : dA(m)/dt = kf·A − k(m)·A(m)
  Eq.20-5  : AUC(m)/AUC = CLf / CL(m)
  Eq.20-6  : AUC(m)/AUC = fm · CL / CL(m)
  Eq.20-7  : k(m)/k = [CL(m)/CL] / [V(m)/V]       ← 추가
  Eq.20-12 : C(m)ss = fm·Rinf / CL(m)
  Eq.20-15 : C(m)av,ss = AUC(m)single / τ

HARD RULES:
* p.657–686 범위를 벗어나는 확장 금지
* Table 20-1 ~ 20-7의 약물명·수치 임의 수정 불가
* [확인 필요] 태그 사용 후 보존; 삭제 금지
* 교재 Figure를 HTML에 임베드하지 말 것
* 타 챕터(Ch.5, App.D·E) 내용 인용 시 → [확인 필요] 태그 부착
=================

=== SCOPE LOCK ===
Source      : Rowland M, Tozer TN. Clinical Pharmacokinetics and
              Pharmacodynamics: Concepts and Applications, 5th ed.
              Wolters Kluwer; 2011.
Chapter     : Appendix D — Plasma-to-Blood Concentration Ratio
              Appendix E — Well-Stirred Model of Hepatic Clearance
Pages       : p.775 – p.780
Chapter role: 수학적 유도 부록 쌍.
              Appendix D: 헤마토크릿·단백결합·혈구친화도(KpBC)를
              통한 C/Cb 도출 — Ch.5 추출비 계산의 정량적 근거.
              Appendix E: Well-stirred model의 정상상태 mass-balance
              유도 (Model I: 기본식, Model II: 막투과성 추가);
              경구투여 후 생체이용률과 AUCpo 관계식까지 확장.
              두 부록 모두 Ch.5·Ch.20의 공식들에 대한
              first-principles 증명으로 기능.
Learner     : PhD pharmacometrics student; 임상약사 10년 경력;
              PopPK 입문-중급; NONMEM/nlmixr2 학습 중
Final output: Single self-contained HTML (Step 2)
Mode        : B-Standard
              (유도 과정이 주 목적; 개념 오류보다 수식 전개
               순서 파악이 우선)
Image rights: None
              (삽화 없는 수식 중심 부록; SVG 불필요)

KEY EQUATIONS TO PRESERVE EXACTLY:
  Eq.D-6  : C/Cb = 1 / {1 + H[fu·KpBC − 1]}
  Eq.D-8  : KpBC = (H − 1 + Cb/C) / (fu·H)
  Eq.E-6  : EH = fu_b·CLint / (QH + fu_b·CLint)
  Eq.E-8  : CLb,H = QH·[fu_b·CLint / (QH + fu_b·CLint)]
  Eq.E-13 : CLb,H = QH·[fu_b·ρ·CLint / (QH + fu_b·ρ·CLint)]
  Eq.E-19 : AUCpo = Dose / (fu_b·ρ·CLint)

HARD RULES:
* p.775–780 범위를 벗어나는 확장 금지
* 유도 단계(Eq.D-1→D-6, Eq.E-1→E-8) 생략 시 [확인 필요] 태그 부착
* 수식 변수 정의(VB, VBC, H, KpBC, ρ, fub 등) 반드시 명시
* [확인 필요] 태그 사용 후 보존; 삭제 금지
=================
Phase 1 진행 시 주의사항
1. 파일명의 "대사체(代謝體)" 처리
파일명 04_G_청소율_간_신장_대사체에 "대사체"가 포함되어 있으나, 업로드된 PDF 범위 내에서 대사체 전용 섹션은 존재하지 않습니다. 해당 개념은 §2.3의 fm/km 파라미터와 §2.5의 Clm 항목으로 분산 수록되어 있습니다. Phase 1에서 별도 대사체 PK 섹션을 신설하거나 page range를 임의 확장하지 마세요. 현재 범위 내 fm/km 언급으로 충분합니다.
2. Table 2.9 수식 재현 시 검증 필수
4개 간 청소율 모델(Well-stirred / Parallel tube / Distributed / Dispersion)의 EH, FH, ClH 수식을 HTML로 재구성할 때, 교재 원본 Table 2.9의 수식과 1:1 대조 후 기재하세요. Distributed/Dispersion 모델의 지수 표현식은 오타 발생 가능성이 높습니다.
3. PK5 수치 인용 범위
PK5(pp.494–499)에서 최종 추정값(Cl = 1.2 L·h⁻¹, fe ≈ 35%, ClR = 0.42 L·h⁻¹)은 PDF에 명시된 값이므로 직접 인용 가능합니다. 단, "초기 추정값"(V ≈ 7 L, Cl ≈ 2 L·h⁻¹)과 "최종 추정값"을 혼용하지 않도록 Phase 1 메모에 명시적으로 구분해 두세요.
4. 타 챕터 참조 차단: 각 Scope Lock에 "타 챕터 인용 시 [확인 필요] 태그"를 명시했으나, Phase 1 실행 중 Ch.5 ↔ Ch.20 개념이 자연스럽게 교차될 수 있음. 참조가 발생하면 내용 보강이 아닌 태그 부착으로만 처리할 것.
5. Eq.20-7 재확인: 수정 Scope Lock에 추가한 k(m)/k = [CL(m)/CL] / [V(m)/V]는 p.664 원문 기반이나, Phase 1에서 HTML 렌더링 시 분수 표기 형식이 Eq.20-5·6과 일관되게 처리되는지 확인 필요.
6. SVG 대체 범위 명확화: Image rights = None이므로 모든 Figure는 SVG 독자 제작이 원칙. 단, "개념을 보여주는 간략 다이어그램"과 "교재 Figure의 재현"의 경계가 모호해질 수 있으므로, Phase 1 산출물 검토 시 SVG가 교재 Figure를 1:1 모방하는지 별도 확인할 것.

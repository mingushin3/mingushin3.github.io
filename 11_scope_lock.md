=== SCOPE LOCK ===

Source       : Gabrielsson & Weiner, Pharmacokinetic and Pharmacodynamic
               Data Analysis, 5th ed. (Swedish Pharmaceutical Press)

Chapter      : Ch. 2 §2.6.7 (Feedback) +
               Ch. 3 §3.7 (Turnover Models – Reversible) +
               Ch. 3 §3.8 (Turnover Models – Irreversible) +
               Ch. 3 §3.10 (Dose-Response-Time Models) +
               Ch. 3 §3.12 (Baseline Models) +
               PD4 / PD5 / PD6 / PD7 / PD9 Case Studies

Pages        : pp. 110–111 · 235–260 · 272–275 · 317–319 · 742–784

Chapter role : ① Conceptual spine of PK/PD delay modeling:
                  establishes why indirect (turnover-driven) models
                  outperform effect-compartment (link) models when
                  the response variable has its own biological turnover.
               ② Provides the four canonical model structures
                  (Models 1–4: inhibit/stimulate × kin/kout) that
                  underpin the majority of published PopPK/PD papers
                  in immunology, hematology, endocrinology, and
                  anti-infective pharmacology.
               ③ Bridges conceptual math (ODEs, limiting solutions,
                  Rss, ΔR, initial-slope rules) to full worked case
                  studies (warfarin-PCA, furosemide, EPO-analog,
                  CB1 agonist, Zooparc®) with graphical parameter
                  estimation — the exact workflow used in NONMEM /
                  nlmixr2 model development.
               ④ Prerequisites satisfied before this chunk:
                  one-compartment PK, Emax/Imax direct-effect models,
                  first-order ODE steady-state reasoning.
               ⑤ Unlocks after this chunk:
                  transit-compartment models, moderator/tolerance
                  models (§3.9), PopPK/PD with IIV on kout & IC50,
                  disease-progression baseline drift modeling.

Learner      : PhD pharmacometrics student (entry–intermediate);
               licensed clinical pharmacist background (~10 yr);
               primary tools: NONMEM, nlmixr2, mrgsolve;
               vault: Obsidian PIPET-Vault (iCloud-synced);
               learning mode: JIT, deep mechanistic understanding
               preferred over encyclopedic coverage.

Final output : Single self-contained HTML (Step 2 flashcard/
               reference page); Obsidian-compatible YAML
               frontmatter block also required.

Mode         : A-Critical
               Rationale: This is the single most tested conceptual
               domain in PopPK/PD manuscripts and FDA reviewer
               questions. Every equation, limiting value, and
               steady-state relationship must be verified precisely.
               Graphical parameter estimation rules (slope → kout,
               intercept → R0, peak-shift → mechanism discrimination)
               are high-yield for both NONMEM coding and manuscript
               critical review.

Image rights : None
               All figures (3.33–3.50, 4.1–4.8, 5.1–5.3, 6.1,
               7.1–7.3, 9.1–9.5) are copyrighted textbook material.
               Reproduce only as original schematic redraws or
               equation-driven mrgsolve/R simulations; never embed
               or screenshot source figures directly.

===============================================
HARD RULES (apply to all phases):

* Do not expand beyond the page ranges listed above.
* Do not fabricate parameter values, experimental conditions,
  drug names, or equation numbers absent from the source PDF.
* [확인 필요] = flag and retain; never silently delete
  unverifiable content.
* Do not reproduce copyrighted figures (Image rights = None).
  Permitted alternatives: (a) pure equation blocks,
  (b) original ASCII/SVG schematics, (c) mrgsolve R code
  that regenerates the conceptual curve shape.
* Model equations must be typeset in LaTeX MathJax syntax
  inside the HTML output; never use plain-text approximations
  for differential equations.
* All four Models (1–4) must appear side-by-side in a
  comparison table with: ODE form · drug action site ·
  tss governor · Rss formula · ΔR formula · limit of R ·
  return-to-baseline behavior · canonical clinical example.
* PD case study parameter tables (Tables 4.1, 5.1, 6.1, 7.1,
  9.1) may be reproduced as data tables (not figures);
  cite page number in caption.
* Irreversible models (§3.8): clearly distinguish second-order
  kill constant K from first-order kout; flag confusion risk
  with [확인 필요] if notation is ambiguous in context.
* §3.10 및 §3.12는 제공 PDF 내 가시 범위(p.272–275, 317–319)에 한정하여
  서술하고, 절단된 소절(3.10.3, §3.12 후반)은 "제공 범위 외"로 명시한다.
=== END SCOPE LOCK ===

=== SCOPE LOCK ===

Source       : Rowland & Tozer, Clinical Pharmacokinetics and
               Pharmacodynamics, 5th ed. (R&T 5e)
Chapter      : Ch. 8 — Response
Pages        : p. 233 – p. 264
Chapter role : PK/PD 통합의 시간축 입문 챕터.
               "농도가 반응을 즉시 반영하지 않는다"는 현상을
               수식·임상 사례·모델 구조로 체계화한다.
               Effect compartment, Indirect Response Model(IRM),
               효과 지속시간 수식($t_D$), 용량-지속시간 로그 선형성의
               개념적 기반을 제공하며, 이후 Ch.10(Constant-Rate Input),
               Ch.11(Multiple-Dose Regimens), Ch.16(Nonlinearities),
               Ch.20(Metabolites and Drug Response),
               Ch.21(Protein Drugs)의 PK/PD 연결 고리를 이해하기 위한
               필수 선행 챕터.
               PopPK 모델링에서 effect compartment($k_{e0}$) 또는
               Turnover 모델(IRM Type I–IV) 선택의 판단 기준을
               여기서 습득한다.

Learner      : PhD pharmacometrics student; clinical pharmacist
               background; PopPK entry–intermediate
Final output : Single self-contained HTML (Step 2)
Mode         : A-Critical
               — Effect compartment 선택 오류·IRM 기전 혼동은
                 NDA 제출용 PK/PD 보고서의 모델 선택 근거를
                 무효화시킨다. 수식·임상 수치·규제 파급력 모두
                 A-Critical 기준 충족.

Image rights : None
               — 교과서 원그림(Fig. 8-1 ~ 8-33) 저작권 보호 대상.
                 HTML 내 임베드 금지.
                 원그림 참조 위치는 FIGURE_POINTER 처리.

HARD RULES (apply to all phases):
- Do not expand beyond p. 233–264.
- Do not fabricate values, experimental conditions, or page citations
  absent from the source PDF.
- [확인 필요] = flag and retain; never delete unverifiable content.
- Do not reproduce or embed copyrighted textbook figures.
  Image rights = None → 모든 figure는 FIGURE_POINTER 처리.

=================
Phase 1 진행 시 주의사항
1. Model 1 vs. Model 3 tss 동일성 — 둘 다 kout 단독 지배 → dose-independent tss. 이것이 Model 2/4와의 최우선 감별 기준이므로, 표 작성 시 해당 셀 오기재 zero-tolerance로 검토할 것.
2. PD6 warfarin 숫자 — Table 4.1의 kout 값이 모델별로 0.03 / 0.06 / 0.09 h⁻¹로 3단계 변화함. HARD RULE상 fabrication 금지이므로, 모델 번호와 수치를 PDF p.751 원본과 1:1 대조 후 기재할 것.
3. §3.8 이중 K 표기 충돌 — bacterial kill 모델의 K(second-order, L·CFU⁻¹·h⁻¹) vs. PK elimination의 K(first-order, h⁻¹)가 같은 표기를 공유함. Phase 1 콘텐츠 정리 시 반드시 [확인 필요] 태그 부착 후 Phase 2에서 구분 표기 처리할 것.
4. **Curation Map 선행 필수** — 이 챕터는 개념이 많고(hysteresis → effect compartment → IRM → tD​ → rate-limiting step) 구조적 연결이 복잡합니다. MUST / CONTEXT 분류를 Curation Map에서 먼저 확정한 뒤 §2 카드 작성을 시작해야 합니다. 특히 *Transporter Polymorphism* 절(p.256–259)은 CONTEXT 처리 여부를 Curation Map에서 명시적으로 판단해야 합니다.
5. 임상 수치 앵커링 대상 확인 — R&T 5e는 구체적 임상 데이터를 다수 포함합니다(digoxin 1 mg i.v., naproxen 500 mg oral, warfarin 1.5 mg/kg oral, succinylcholine 0.5 mg/kg i.v. 등). Dynamic Source Anchoring Directive에 따라 이 수치들이 §2 도출부와 §6 시나리오에 일관되게 반영되어야 합니다. 가상 수치 보완 시 출처 표기 필수.
6. Figure Pointer 밀도 관리 — Fig. 8-1부터 Fig. 8-33까지 33개 그림이 존재합니다. Phase 1에서는 figure marker를 삽입하지 않고(Phase 4C 전담), 본문에서 그림을 참조할 때 "Fig. 8-X 참조" 정도의 텍스트 언급만 유지하면 됩니다. Phase 1 산출물에 FIGURE 마커가 등장하면 Anti-pattern으로 제거 대상입니다.

거장 시각에서의 편집 메모 (사용 전 확인 권장):
이 Scope Lock에서 특히 주의해야 할 세 가지 고밀도 구간이 있습니다.
첫째, Model 1 vs. Model 3의 tss 거동 동일성입니다. 둘 다 kout에 의해서만 tss가 결정되므로 dose-independent tss를 보입니다. 이것이 Model 2/4(kout 작용)와의 핵심 감별점이며, PD5 vs. PD6 비교에서 실제로 드러납니다.
둘째, PD6의 핵심 통찰입니다. 선형 S(C) 하에서는 turnover model과 effect compartment model이 동일한 WRSS를 낼 수 있어 단일 dose-range 데이터로는 두 모델을 감별할 수 없습니다. 이 한계를 명시적으로 가르치는 것이 이 챕터의 가장 중요한 실용적 교훈입니다.
셋째, §3.8의 K 표기 충돌 위험입니다. 세균 kill 모델에서 K는 second-order rate constant(단위: L·CFU⁻¹·h⁻¹)이지만, 같은 장에서 K가 elimination rate constant로도 쓰입니다. 학습 노트에 [확인 필요] 태그로 명시해두는 것을 권장합니다.

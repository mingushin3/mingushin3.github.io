# Audit Report v1
## Session 02 — 분포의 생물학: 막투과·분포용적·단백결합

**업무 형태:** 파일 분석 / PDF 대조 감사 / 웹 검색 OFF  
**입력:** 02_T PDF, 02_G PDF, Step 1 Draft v0, Phase 1 Patch Memo, Source Fidelity Auditor prompt  
**감사 범위:** Rowland & Tozer Ch.4 + Appendix B/C/D, Gabrielsson & Weiner §2.9.3–2.9.5 + PK47, Step 1 Draft v0 전체  
**감사 모드:** Source Fidelity Audit. 문장 개선·재작성·교육적 보강은 수행하지 않고, 원문 대응성·오류·누락·그림/표 학습가치만 판정함.

---

## 0. Executive Verdict

### 최종 판정

**조건부 Go.**  
Step 1 Draft v0는 세션의 핵심 구조를 잘 잡았고, 6개 MUST 카드 선정도 원문 범위와 대체로 정합적이다. 그러나 A-Critical 세션 기준으로는 다음 이유 때문에 **바로 Step 2 HTML 컴파일로 넘기면 안 된다.**

1. **수식 오류/불일치 1건이 명확함:** Curation Map의 PK47 `fu` 식은 원문 Eq.47:1과 다르다.
2. **원문에 없는 실무·규제·개발 표현이 다수 섞임:** “FDA reviewer deficiency letter”, “매년 수십 건 phase 1 폐기”, “Rodgers–Rowland 80% variance”, “Vd 한 자릿수 정확도 예측” 등은 첨부 PDF 범위에서 확인되지 않는다.
3. **원문 수치의 과잉 정밀화/시각 추정값이 일부 있음:** Fig.2.141의 total potency fold, Fig.4-13의 fat equilibrium 3.5 h, Fig.4-10의 CSF/plasma 1/10 등은 원문 취지를 반영하지만 author-stated value가 아니다.
4. **일부 source attribution이 부정확함:** `fub > 1`은 G&W p.168에서 명시되며, Draft의 “R&T p.106 명시”는 부정확하다.

### 권장 진행

**원본 v0 보존 → Audit Report v1 첨부 → Phase 2 Source Fidelity Patch → Phase 4A에서 공식 패치 → 그 다음 HTML.**

---

## T1: Equation / Numerical Audit

| Item | Draft v0 Expression | PDF Source | Classification | Correction |
|---|---|---|---|---|
| M1 Eq.4-1 | `Net rate = P·SA·(Cu1-Cu2)` | R&T Ch.4 p.80 Eq.4-1 | MATCH | 없음 |
| M1 driving force | bound form은 막을 통과하지 못하므로 driving force는 `Cu` | R&T p.80 protein binding paragraph | MATCH | 없음 |
| M1 molecular size | MW 400→800 g/mol에서 permeability 약 300-fold 감소 | R&T p.82 / Fig.4-3 | MATCH | 없음 |
| M1 atenolol | atenolol 246 g/mol, oral bioavailability 50% | R&T p.81 | MATCH | 없음 |
| M1 oxytocin | oxytocin 1007 g/mol, GI absorption 거의 없음 | R&T p.81 | MATCH | 없음 |
| M1 calcitonin-salmon | 3432 g/mol, nasal spray 3% absorbed | R&T p.81 | MISSING in Draft main card, present only if not cited | Not mandatory, but useful if size example needs full triad |
| M1 caffeine logP | Big Idea: “같은 logP 2.0의 caffeine” | R&T Fig.4-4: caffeine은 logP ≈ 0 부근, lomustine이 ≈2 | ERROR | caffeine을 logP 2.0 예시로 쓰면 안 됨. `caffeine(logP≈0)`로 정정 필요 |
| M1 vinblastine/vincristine | logP 1.7–1.8인데 permeability 낮음, P-gp substrate | R&T Fig.4-4 / p.82 | MATCH | 없음 |
| M1 “100배 낮음” | vinblastine/vincristine permeability 100배 낮음 | R&T Fig.4-4 visual estimate; text says lower than expected | RESTORED [확인 필요] | author-stated value가 아니므로 “markedly lower” 또는 “visual estimate” 표시 권장 |
| M1 pH partition | un-ionized form만 membrane 통과, pH별 total concentration 차이 | R&T Ch.4 p.83 + App.B p.763–765 | MATCH | 없음 |
| M1 pKa thresholds | weak acids pKa >7.5 essentially un-ionized; pKa 3.0–7.5 pH-sensitive | R&T App.B p.763 | MATCH | 없음 |
| M1 Eq.4-26 | `CuT/Cu = Puptake/Pefflux` | R&T p.110 Eq.4-26 | MATCH | 없음 |
| M1 Caco-2/PAMPA | `P`는 보통 Caco-2 또는 PAMPA surrogate | Not in attached PDFs | NOT_IN_SOURCE | 외부 실무 확장으로 태그하거나 삭제 |
| M1 Lipinski rule of 5 | `Lipinski's rule of 5 + P-gp screen` | Not in attached PDFs | NOT_IN_SOURCE | 외부 확장으로 태그하거나 삭제 |
| M1 phase 1 screening claim | “phase 1 진입 전 소실” | Not in attached PDFs | NOT_IN_SOURCE | 삭제 또는 `[실무 추론]` 태그 필요 |
| M1 “임상 1상 폐기 수십 건/년” | CNS 후보가 BBB 미통과로 매년 수십 건 폐기 | Not in attached PDFs | NOT_IN_SOURCE | 반드시 삭제 또는 외부 근거 별도 요구 |
| M2 Eq.4-7 | `CT(t)=Kpb·CA·(1-e^-kTt)` | R&T p.97 Eq.4-7 | MATCH | 없음 |
| M2 Eq.4-6 | `t1/2,distribution = 0.693·Kpb/(Q/VT)` | R&T p.97 Eq.4-6 | MATCH | 없음 |
| M2 `kT` | `kT=(Q/VT)/Kpb` | R&T p.97 Eq.4-5 | MATCH | 없음 |
| M2 perfusion rates | Lung 10.0, kidney 4.0, brain 0.5, adipose 0.025, inactive muscle 0.025 | R&T Table 4-4 p.96 | MATCH | 없음 |
| M2 adipose/fat equilibrium | “thiopental fat 평형 약 3.5 h” | R&T Fig.4-13 says after 3 h much drug remains in fat; no 3.5 h author value | RESTORED [확인 필요] | author-stated value가 아니므로 “several hours” 또는 “Fig.4-13 visual estimate”로 낮춤 |
| M2 lymph flow | lymphatic drainage “약 1 mL/min” | R&T Fig.4-14 caption: 1–10 mL/min per 70 kg | ERROR | `1–10 mL/min per 70 kg`로 정정 |
| M2 MW >5000 | molecules >5000 g/mol mostly lymph-mediated/slow distribution | R&T Table 4-1 + Fig.4-14 | MATCH | 없음 |
| M2 ribitol | ribitol MW 152, mixed/permeability example | R&T Fig.4-17 p.99 | MATCH | 없음 |
| M2 penicillin G | large polar compound, CNS permeability limitation | R&T p.100 / Fig.4-18 | MATCH | 없음 |
| M3 Eq.4-8 | `V = Amount in body / C = A/C` | R&T p.102 Eq.4-8 | MATCH | 없음 |
| M3 V not physical volume | V may greatly exceed physical body volume | R&T Fig.4-19 + p.103–111 | MATCH | 없음 |
| M3 quinacrine/chloroquine | quinacrine ~50,000 L, chloroquine ~13,000 L | R&T Fig.4-19 visual axis; exact values not tabulated | RESTORED [확인 필요] | “order-of-magnitude”로 표현하거나 exact value 제거 |
| M3 `A = Vp·C + VT·Kp·C` | Eq.4-11 | R&T p.103 Eq.4-11 | MATCH | 없음 |
| M3 `V = Vp + VT·Kp` | Eq.4-12 derived from Eq.4-11 | R&T p.103 Eq.4-12 | MATCH | 없음 |
| M3 `V = Vp + ΣVT,i·Kp,i` | Eq.4-13 | R&T p.104 Eq.4-13 | MATCH | 없음 |
| M3 `Vu = Amount/Cu` | Eq.4-14 | R&T p.104 Eq.4-14 | MATCH | 없음 |
| M3 `Vb = Amount/Cb` | Eq.4-15 | R&T p.104 Eq.4-15 | MATCH | 없음 |
| M3 Eq.4-25 | `V = Vp + VTW·fu/fuT` | R&T p.109 Eq.4-25 | MATCH | 없음 |
| M3 VTW | `VTW ≈ 39 L` | R&T p.109: aqueous volume outside plasma, consistent with 42 L total body water minus plasma | RESTORED | acceptable simplification |
| M3 brain 2% | brain contributes little to whole-body V, about 2% body weight | R&T p.109 | MATCH | 없음 |
| M3 Eq.4-29 | `V = Vp + VTW·(fu/fuT)·(Puptake/Pefflux)` | R&T p.111 Eq.4-29 | MATCH | 없음 |
| M3 physiologic spaces | plasma 3 L, extracellular water 16 L, total body water 42 L | R&T p.111 | MATCH | 없음 |
| M3 albumin floor | albumin apparent volume about 7.5 L | R&T p.111 + p.112 Eq.4-30 | MATCH | 없음 |
| M3 MW threshold | high MW >70,000 g/mol, extravascular distribution slow/nonexistent | R&T p.111 | MATCH | 없음 |
| M3 adalimumab | MW 142,000 g/mol, V about 5–6 L | R&T p.111 | MATCH | 없음 |
| M3 caffeine/alcohol | small freely membrane-crossing, V about 40 L | R&T p.111 | MATCH | 없음 |
| M3 small-Vd model | `V = 7.5 + (7.5 + VR/fuR)·fu` | R&T p.112 Eq.4-30; App.C Eq.C-13 equivalent after parameter substitution | MATCH | 없음 |
| M3 `V < 15 L` | small-volume drugs model applicable | R&T p.112 + Table 4-8 | MATCH | 없음 |
| M3 cephalosporin intercept | Fig.4-25 intercept ≈7 L, albumin volume | R&T p.112–113 Fig.4-25 | MATCH | 없음 |
| M3 cephalosporin fu→1 V | extrapolation to fu=1 gives V≈20 L; >16 L and <42 L | R&T p.113 | MATCH, but underused | Consider adding if Phase 4A needs richer data anchor |
| M3 cephalosporin Vu | Fig.4-26 Vu decreases as fu increases | R&T p.113 Fig.4-26 | MATCH if mentioned; otherwise MISSING_EXAMPLE | Strongly useful in M3/M6 bridge |
| M3 warfarin Table 4-12 | V 9.4→13.7 L; CL 0.20→0.58 L/hr; t1/2 36→18 hr; albumin 43→12.5 g/L | R&T Table 4-12 p.118 | MATCH | 없음 |
| M3/Q8 warfarin fu estimate | `fu'=(43/12.5)·0.005≈0.0172` | R&T study problem gives inputs, not answer | RESTORED | 계산 자체는 correct; “worked answer”가 아니라 “derived from study problem”로 표시 |
| M4 Curation Map PK47 formula | `fu = 1/[1 + 1/(Cu/n[PT]) + 1/(Ka·n·[PT])]` | G&W p.691 Eq.47:1 | ERROR | `fu = 1 - 1/(1 + Cu/(n[PT]) + 1/(Ka·n[PT]))`로 정정 또는 Curation Map에서 식 삭제 |
| M4 Eq.4-17 | `fu = Cu/C` | R&T p.105 Eq.4-17 | MATCH | 없음 |
| M4 Eq.4-18 | `Ka = Cb,t/(Cu·P)` | R&T p.105 Eq.4-18 | MATCH | 없음 |
| M4 Eq.4-19 | `fu = 1/(1 + Ka·fup·Pt)` | R&T p.105 Eq.4-19 | MATCH | 없음 |
| M4 Eq.47:1 | `fu = 1 - 1/(1 + Cu/(n[PT]) + 1/(Ka·n[PT]))` | G&W p.691 Eq.47:1 | MATCH in M4 body | 없음 |
| M4 Eq.47:2 | `C = Cu/fu = Dose rate/Clu / [1 - ...]` | G&W p.691 Eq.47:2 | MATCH | 없음 |
| M4 Eq.47:3 | `fu ≈ 1/(1 + Ka·n[PT])` | G&W p.692 Eq.47:3 | MATCH | 없음 |
| M4 Eq.47:4 | Draft: `0.0015 = 1/(1+2·Ka·50)` → Ka≈6 | G&W p.693 Eq.47:4: `0.15 = 100/(1+2·Ka·50)` | MATCH | Equivalent percent vs fraction form |
| M4 n range | n commonly varies between 1 and 4 | G&W p.693 | MATCH | 없음 |
| M4 Compound protein concentrations | Compound 1: 50/0.3; Compound 2: 10/0.1 | G&W Table 47.1 + p.693 | MATCH | 없음 |
| M4 simultaneous fit | low + high protein concentration reduces n–Ka correlation and improves precision | G&W p.693 | MATCH | 없음 |
| M4 `fub > 1` attribution | Draft says R&T p.106 | G&W p.168 explicitly states fub can exceed unity; R&T source not confirmed in given page | ERROR | Source attribution을 G&W p.168로 수정 |
| M4 albumin site I/II | albumin site I/II examples | Not in attached PDFs | NOT_IN_SOURCE | 외부 생화학 확장으로 태그하거나 삭제 |
| M5 Kp definition | tissue-to-plasma/blood equilibrium distribution ratio | R&T Eq.4-4, Fig.4-20, p.97/p.104 | MATCH | 없음 |
| M5 acidic phospholipid | metoprolol Kp varies with acidic phospholipid content | R&T Fig.4-24 p.110 | MATCH | 없음 |
| M5 r > 0.85 | strong positive correlation r >0.85 | R&T Fig.4-24 visual correlation; exact r not stated in caption/text | RESTORED [확인 필요] | exact r 삭제 또는 “strong positive relationship”로 낮춤 |
| M5 propranolol | V varies with fu in 6 controls + 15 chronic hepatic disease patients after 40-mg bolus | R&T Fig.4-23 p.110 | MATCH | 없음 |
| M5 propranolol V 200–700 L | visual range from Fig.4-23 | RESTORED [확인 필요] | “visual range” 또는 approximate 표시 |
| M5 Indinavir | 800 mg q8h, 8 HIV adults, CSF unbound lower/later/reduced fluctuation | R&T Fig.4-10 p.91 | MATCH in general | `1/10`은 approximate visual estimate로 표시 필요 |
| M5 brain body weight | brain ≈2% body weight; local transporter effects may not change whole-body V much | R&T p.109/p.111 | MATCH | 없음 |
| M5 Rodgers–Rowland method | “PBPK Rodgers–Rowland method” | Not in attached PDFs | NOT_IN_SOURCE | 후속 PBPK 연결로만 남기거나 삭제 |
| M5 acidic phospholipid explains 80% variance | Not in attached PDFs | NOT_IN_SOURCE | 반드시 삭제 또는 외부 근거 필요 |
| M5 one-digit Vd prediction | “Vd를 한 자릿수 단위 정확도로 예측” | Not in attached PDFs | NOT_IN_SOURCE | 반드시 삭제 또는 외부 근거 필요 |
| M6 Eq.2:373 | `C = Cu/fu`, `AUCu=AUC×fu` under constant fu | G&W p.167 Eq.2:373 and text | MATCH | 없음 |
| M6 Fig.2.134 | total concentration-response confounded; unbound reverses potency order | G&W p.163 Fig.2.134/text | MATCH | 없음 |
| M6 Compound A/B exact values | A F>95%, B F<5%, fu values, 90 times | G&W Fig.2.134 visual/text; exact values embedded in figure | MATCH/RESTORED | Keep as figure-based; no external issue |
| M6 Fig.2.136 | Equal AUCs can have different concentration ranges/durations | G&W p.164 Fig.2.136/text | MATCH but underemphasized | Should retain as author key warning |
| M6 extent vs duration | distinguish extent (Cmax/AUC) vs duration (td/treatment period) | G&W p.167 | MATCH | 없음 |
| M6 Fig.2.140 | fu vs Cu clearer than fu vs total C; total confounded by fu variability | G&W p.167 Fig.2.140 | MATCH | 없음 |
| M6 Fig.2.141 | Dog/rat/mouse total curves differ, unbound ECu50 ≈2 nM | G&W p.168 Fig.2.141 | MATCH | Total potency fold is visual/inferred; mark approximate |
| M6 Benet & Hoener | 456 drugs; PPB changes PK parameters but usually not clinical outcome; rare IV high-extraction narrow TW exception | G&W p.168 | MATCH | 없음 |
| M6 IND/NDA | IND: ex vivo PPB at several concentrations/species including man; NDA: limited clinical studies with unbound+total; routine good-to-have discouraged | G&W p.169 | MATCH | 없음 |
| M6 FDA reviewer deficiency letter | FDA reviewer deficiency letter / PopPK reviewer wording | Not in attached PDFs | NOT_IN_SOURCE | `[실무 추론]` 태그 또는 삭제 |
| M6 FDA Guidance on PopPK Analyses | cited in “방어 언어” | Not in attached PDFs | NOT_IN_SOURCE | 외부 근거 없으면 삭제 |
| §7 Boss Dilemma lidocaine analog | IV lidocaine analog, EH≈0.7, α1-AGP 2-fold etc. | Not in attached PDFs as case; only principle supported by Benet & Hoener | NOT_IN_SOURCE | educational hypothetical로 명확히 표시 필요 |

---

## T2: Examples & Data Audit

| Item | Draft v0 Status | PDF Location | Classification | Importance | Action |
|---|---|---|---|---|---|
| Functional membranes / skin thickness | Rejected | R&T Fig.4-1 p.79 | OMITTED_JUSTIFIABLE | LOW | 별도 카드 불필요 |
| Transcellular/paracellular/facilitated routes | Included in M1 | R&T Fig.4-2 p.80 | INCLUDED_CORRECT | HIGH | 유지 |
| Atenolol / oxytocin / calcitonin size triad | Partly included | R&T p.81 | INCLUDED_CORRECT but incomplete | MEDIUM | calcitonin 3432 g/mol, 3% nasal absorption은 optional enrichment |
| BBB lipophilicity examples | Included | R&T Fig.4-4 p.82 | INCLUDED_ERROR for caffeine logP in Big Idea; otherwise correct | HIGH | caffeine logP correction mandatory |
| pH partition / ion trapping | Included as context | R&T Fig.4-5 p.83, App.B | INCLUDED_CORRECT | HIGH | 유지 |
| Membrane properties table | Briefly context in M2 | R&T Table 4-1 p.84 | INCLUDED_AS_CONTEXT | MEDIUM | sufficient |
| Carrier-mediated transport saturation | Included | R&T Fig.4-6 p.84 | INCLUDED_CORRECT | MEDIUM | 유지 |
| Transporter distribution table | Mostly omitted | R&T Fig.4-8/Table4-2 p.86–89 | OMITTED_JUSTIFIABLE | LOW-MEDIUM | 본 세션에서는 list overload 방지 가능 |
| Indinavir CSF/plasma | Included | R&T Fig.4-10 p.91 | INCLUDED_CORRECT with approximate value caveat | MEDIUM | `1/10`은 approximate 표시 |
| Fexofenadine + grapefruit juice | Omitted | R&T Fig.4-11 p.91 | OMITTED_JUSTIFIABLE | LOW | transporter DDI session으로 이월 가능 |
| SGLT2 inhibitor | Rejected | R&T Fig.4-12 p.92 | OMITTED_JUSTIFIABLE | LOW | 유지 |
| Activated charcoal reversible transport | Rejected | R&T Table 4-3 p.93 | OMITTED_JUSTIFIABLE | LOW-MEDIUM | Vd/fu 세션에서는 생략 가능 |
| Thiopental dog tissue distribution | Included | R&T Fig.4-13 p.94 | INCLUDED_CORRECT except 3.5 h estimate | HIGH | exact 시간값 낮춤 |
| Lymph/macromolecule distribution | Included as context | R&T Fig.4-14 p.95 | INCLUDED_ERROR for lymph flow | HIGH for biologics context | `1–10 mL/min per 70 kg` 정정 |
| Organ perfusion table | Included | R&T Table 4-4 p.96 | INCLUDED_CORRECT | HIGH | 유지 |
| Kidney/brain/fat distribution simulation | Included | R&T Fig.4-16 p.98 | INCLUDED_CORRECT | HIGH | View instruction recommended |
| Ribitol distribution | Included as limitation | R&T Fig.4-17 p.99 | INCLUDED_CORRECT | MEDIUM | 유지 |
| Penicillin G CNS distribution | Included/brief | R&T Fig.4-18 p.100 | INCLUDED_CORRECT | HIGH | M2 bridge로 유지 |
| Albumin distribution | Included as floor | R&T Table 4-5 p.101 | INCLUDED_CORRECT | HIGH | 유지 |
| Apparent V range | Included | R&T Fig.4-19 p.103 | INCLUDED_CORRECT with exact-value caveat | HIGH | exact 50,000 L 낮춤 |
| Two-compartment V schematic | Included via equations | R&T Fig.4-20 p.104 | INCLUDED_CORRECT | HIGH | 유지 |
| Fraction unbound drug examples | Partly included | R&T Fig.4-21 p.107 | OMITTED_JUSTIFIABLE | MEDIUM | optional |
| fu and protein concentration | Included | R&T Fig.4-22 p.108 | INCLUDED_CORRECT | HIGH | 유지 |
| Propranolol V vs fu | Included | R&T Fig.4-23 p.110 | INCLUDED_CORRECT with visual range caveat | HIGH | 유지 |
| Metoprolol acidic phospholipid Kp | Included | R&T Fig.4-24 p.110 | INCLUDED_CORRECT except exact r | HIGH | exact r 제거 |
| Small-Vd drug list | Included conceptually | R&T Table4-8 p.112 | INCLUDED_AS_CONTEXT | MEDIUM | sufficient |
| Cephalosporin V vs fu | Included | R&T Fig.4-25 p.113 | INCLUDED_CORRECT | HIGH | 유지 |
| Cephalosporin Vu vs fu | Underused | R&T Fig.4-26 p.113 | MISSING_EXAMPLE | MEDIUM-HIGH | M3/M6 bridge에 1문장 반영 권장 |
| Conditions altering albumin/α1-AGP | Included | R&T Table4-9 p.114 | INCLUDED_CORRECT | HIGH | 유지 |
| Fractions in body formulas | Mostly omitted | R&T Table4-10 p.115 | OMITTED_JUSTIFIABLE | MEDIUM | formula overload 방지 가능 |
| Study problem Table4-11 | Omitted | R&T Table4-11 p.117 | OMITTED_JUSTIFIABLE | LOW-MEDIUM | 필요 시 self-test로만 활용 |
| Warfarin nephrotic syndrome | Included | R&T Table4-12 p.118 | INCLUDED_CORRECT | HIGH | 유지 |
| Appendix B pKa figures | Included as context | R&T Fig.B-1/B-2 p.764–765 | INCLUDED_CORRECT | MEDIUM | 유지 |
| Appendix C model | Included in M3 | R&T App.C p.767–773 | INCLUDED_CORRECT | HIGH | 유지 |
| Appendix D plasma-to-blood | Included as context | R&T App.D p.775–776 | INCLUDED_CORRECT | MEDIUM | 유지 |
| G&W Fig.2.134 A/B | Included | G&W p.163 | INCLUDED_CORRECT | HIGH | 유지 |
| G&W Fig.2.135 exposure metrics | Included | G&W p.163 | INCLUDED_CORRECT | HIGH | 유지 |
| G&W Fig.2.136 equal AUC warning | Underemphasized | G&W p.164 | MISSING_AUTHOR_MSG partial | HIGH | M6에 1문장 이상 명확히 유지 |
| G&W Fig.2.137 nonlinear rat kinetics | Omitted | G&W p.165 | OMITTED_JUSTIFIABLE | LOW-MEDIUM | toxicokinetic-specific; optional |
| G&W Fig.2.138 minipump/drug holidays | Omitted | G&W p.165–166 | OMITTED_JUSTIFIABLE | LOW | 본 세션 scope 밖 |
| G&W Fig.2.139 dose/time-dependent kinetics | Omitted | G&W p.166 | OMITTED_JUSTIFIABLE | LOW | toxicokinetic-specific |
| G&W Fig.2.140 | Included | G&W p.167 | INCLUDED_CORRECT | HIGH | 유지 |
| G&W Fig.2.141 dog/rat/mouse | Included | G&W p.168 | INCLUDED_CORRECT with approximate fold caveat | HIGH | 유지 |
| G&W Table2.21 metrics | Included | G&W p.169 | INCLUDED_CORRECT | HIGH | 유지 |
| G&W PK47 Figure47.1/Table47.1 | Included | G&W p.690–693 | INCLUDED_CORRECT | HIGH | 유지 |

---

## T3: Author Key Messages

| Message | PDF Location | In Draft v0? | Status |
|---|---|---|---|
| Membrane transport principles apply to distribution, elimination, and absorption; drugs often must pass membranes to reach action site. | R&T opening p.78 | Yes | INCLUDED |
| Drug distribution chapter proceeds from kinetic considerations to equilibrium concepts and reversible transfer. | R&T opening p.78 | Yes, concept map | INCLUDED |
| Only unbound drug diffuses across most cell membranes; unbound concentration is the driving force. | R&T p.80 | Yes | INCLUDED |
| Size, lipophilicity, and charge are the three major drug properties determining permeability; membrane properties also matter. | R&T p.81–84 | Yes | INCLUDED |
| pH partition is useful but often inaccurate alone; transporter/paracellular mechanisms can violate simple pH predictions. | R&T p.83 + App.B | Partly | SHOULD_FIX: limitation should remain visible, not only context |
| Distribution rate is governed by perfusion, membrane permeability, and tissue affinity; high Kp can slow equilibrium despite high extent. | R&T p.94–100 | Yes | INCLUDED |
| V is an apparent volume, not necessarily a physiologic volume; binding in plasma/tissues makes physical interpretation unsafe. | R&T p.103–111 | Yes | INCLUDED |
| When V is large, changes in plasma protein binding often do not change unbound concentration for a given amount because V changes proportionally. | R&T p.114–115 | Yes | INCLUDED |
| Small-Vd albumin-bound drugs require the albumin distribution model; albumin volume creates a floor near 7.5 L. | R&T p.111–113/App.C | Yes | INCLUDED |
| PPB changes may alter PK parameters but usually not clinical outcome; rare exception: IV high-extraction narrow therapeutic window. | G&W p.168 | Yes | INCLUDED |
| Routine AUC comparison across species is dangerous because same AUC can mean different concentration ranges and durations. | G&W p.164 | Partial | SHOULD_FIX: author warning should be more explicit |
| Distinguish extent of exposure (Cmax, AUC) from duration of exposure (td/treatment period). | G&W p.167 | Yes | INCLUDED |
| AUCu/Cu can be more appropriate than total AUC/C for species extrapolation and safety margins when PPB differs. | G&W p.167–168 | Yes | INCLUDED |
| Do not always measure unbound; measure whenever possible. IND: ex vivo PPB across species/concentrations; NDA: limited clinical studies; routine “good to have” discouraged. | G&W p.169 | Yes | INCLUDED |
| PK47: free fraction is a nonlinear proportionality constant/variable between total and unbound concentration; simultaneous fitting across protein concentrations improves precision. | G&W p.690–693 | Yes | INCLUDED |

---

## T4: Priority Summary

| # | Item | Priority | Rationale |
|---|---|---|---|
| 1 | Curation Map M4 PK47 formula is wrong | MUST_FIX | Eq.47:1 mismatch; A-Critical 수식 오류 |
| 2 | Big Idea caffeine logP 2.0 claim | MUST_FIX | Fig.4-4와 직접 충돌 |
| 3 | “임상 1상 폐기 수십 건/년” claim | MUST_FIX | 첨부 PDF 근거 없음, 숫자성 주장 |
| 4 | `fub > 1` source attribution to R&T p.106 | MUST_FIX | 첨부 PDF 명시 근거는 G&W p.168 |
| 5 | lymph flow 약 1 mL/min | MUST_FIX | 원문은 1–10 mL/min per 70 kg |
| 6 | FDA reviewer deficiency letter / FDA Guidance wording | MUST_FIX | 첨부 PDF 범위 밖 규제 표현 |
| 7 | Rodgers–Rowland 80% variance / one-digit Vd prediction | MUST_FIX | 첨부 PDF 범위 밖, 강한 정량 주장 |
| 8 | M5 r>0.85 exact correlation | SHOULD_FIX | Fig.4-24 시각상 강한 상관이나 exact r 미제시 |
| 9 | Fig.4-13 fat equilibrium 3.5 h | SHOULD_FIX | author-stated value 아님 |
| 10 | Fig.2.141 total potency “90-fold” | SHOULD_FIX | figure-based visual inference; exact author value 아님 |
| 11 | Fig.4-10 CSF/plasma 1/10 | SHOULD_FIX | figure-based approximate; 원문은 “much lower” |
| 12 | G&W Fig.2.136 equal-AUC warning underemphasized | SHOULD_FIX | author key message; M6에 명시 필요 |
| 13 | Cephalosporin unbound Vd Fig.4-26 underused | SHOULD_FIX | Fig.4-25와 paired message; active form concentration 해석에 유용 |
| 14 | Caco-2/PAMPA/Lipinski | OPTIONAL | 실무 확장이지만 원문 밖; 태그하면 유지 가능 |
| 15 | calcitonin full size example | OPTIONAL | M1 size intuition enrichment |
| 16 | Fexofenadine/GFJ, SGLT2, charcoal | REJECT for Step 1 main flow | Scope creep 가능; 다른 세션/부록 처리 적합 |
| 17 | Toxicokinetics definition | REJECT for Step 1 main flow | G&W p.169 이후이지만 본 세션 범위 외 |

---

## T5: Coverage Audit

| PDF Element | Type | PDF Location | Step 1 Status | Omission Verdict | Required Action |
|---|---|---|---|---|---|
| Chapter objectives: membrane/distribution terms | Heading/objectives | R&T p.77–78 | INCLUDED_AS_MUST | None | 유지 |
| MEMBRANES | H2 | R&T p.78 | INCLUDED_AS_MUST | None | 유지 |
| TRANSPORT PROCESSES | H2 | R&T p.79 | INCLUDED_AS_MUST | None | 유지 |
| Protein Binding before diffusion | H3/paragraph | R&T p.80 | INCLUDED_AS_MUST | None | 유지 |
| Diffusion | H3 | R&T p.80 | INCLUDED_AS_MUST | None | 유지 |
| Drug Properties Determining Permeability | H3 | R&T p.81 | INCLUDED_AS_MUST | None | caffeine 오류 수정 |
| Membrane Characteristics | H3 | R&T p.83–84 | INCLUDED_AS_CONTEXT | None | 유지 |
| Carrier-Mediated Transport | H3 | R&T p.85–89 | INCLUDED_AS_MUST | None | 세부 transporter list는 생략 가능 |
| Membrane Resistance and Drug Movement | H3 | R&T p.90–92 | INCLUDED_AS_CONTEXT | None | indinavir 정도만 유지 |
| Movement of Highly Polar Drugs | H3 | R&T p.92–93 | OMITTED_JUSTIFIABLE | Low relevance | 없음 |
| Reversible Nature of Transport | H2 | R&T p.93 | OMITTED_JUSTIFIABLE | Scope edge | charcoal는 부록/다음 세션 가능 |
| Rate of Distribution to Tissues | H2 | R&T p.94 | INCLUDED_AS_MUST | None | 유지 |
| Perfusion Rate Limitations | H3 | R&T p.94–98 | INCLUDED_AS_MUST | None | 유지 |
| Permeability Rate Limitations | H3 | R&T p.98–100 | INCLUDED_AS_MUST | None | 유지 |
| Lymphatic discussion | H3/context | R&T p.95 | INCLUDED_AS_CONTEXT | MISSING_BRIDGE if flow wrong | lymph flow 정정 |
| Extent of Distribution | H2 | R&T p.102 | INCLUDED_AS_MUST | None | 유지 |
| Binding within Blood | H3 | R&T p.104–105 | INCLUDED_AS_MUST | None | 유지 |
| Plasma Protein Binding | H3 | R&T p.105–108 | INCLUDED_AS_MUST | None | 유지 |
| Tissue Distribution/Tissue Binding | H3 | R&T p.108–110 | INCLUDED_AS_MUST | None | 유지 |
| Transporters in tissue distribution | H3 | R&T p.110–111 | INCLUDED_AS_MUST | None | 유지 |
| Small Volume of Distribution / Model | H2/H3 | R&T p.111–113 | INCLUDED_AS_MUST | None | 유지 |
| Location in Body | H3 | R&T p.114–115 | INCLUDED_AS_CONTEXT | None | Table4-10는 생략 가능 |
| Altered Binding and Loading Dose | H3 | R&T p.114–116 | INCLUDED_AS_MUST | None | 유지 |
| Key Relationships | Summary | R&T p.115–116 | INCLUDED_AS_MUST | None | 유지 |
| Study Problems | Study problems | R&T p.116–118 | INCLUDED_AS_CONTEXT | Table4-12 only | Warfarin 유지 |
| Appendix B Ionization | Appendix | R&T p.763–765 | INCLUDED_AS_CONTEXT | None | 유지 |
| Appendix C Distribution of Drugs Extensively Bound to Plasma Proteins | Appendix | R&T p.767–773 | INCLUDED_AS_MUST for C-13; otherwise context | None | 유지 |
| Appendix D Plasma-to-Blood Concentration Ratio | Appendix | R&T p.775–776 | INCLUDED_AS_CONTEXT | None | 유지 |
| G&W §2.9.3 Exposure based on total concentrations | H2 | G&W p.163–167 | INCLUDED_AS_MUST | Equal-AUC warning partial | Fig.2.136 warning 강화 |
| G&W §2.9.4 Exposure based on unbound concentrations | H2 | G&W p.167–168 | INCLUDED_AS_MUST | None | 유지 |
| G&W §2.9.5 Conclusions about exposure | H2 | G&W p.169 | INCLUDED_AS_MUST | None | 유지 |
| G&W PK47 Objectives/Problem/Initial estimates/Interpretation | Exercise sections | G&W p.690–693 | INCLUDED_AS_MUST | None | Curation formula 수정 |
| Repeated author message: unbound concentration, not total concentration, is driving/active comparator | Repeated message | R&T p.80; G&W p.167–168; PK47 p.693 | INCLUDED_AS_MUST | None | 유지 |
| Repeated author message: V/AUC single scalar cannot replace distribution/exposure shape | Repeated message | R&T V section; G&W Fig.2.136 | INCLUDED_AS_CONTEXT | MISSING_AUTHOR_MSG partial | M6에서 명시 |

---

## T6: Figure Inventory & Learning Value Audit

Inspection note: rendered page images were generated and visual review was performed from page contact sheets plus focused inspection of source-critical pages. `VISUAL_INSPECTED` means the rendered page/figure was visible in the inspection set.

| Figure/Table | Page | Teaches | Value | View Instruction? | Redraw/New Schematic? | Inspection Method | Rationale |
|---|---:|---|---|---|---|---|---|
| R&T Fig.4-1 | 79 | Functional membranes vary in thickness/structure | USEFUL | NO | NO | VISUAL_INSPECTED | concept intro; not central to Vd/fu |
| R&T Fig.4-2 | 80 | paracellular, passive transcellular, facilitated transcellular paths | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M1 route taxonomy의 핵심 |
| R&T Fig.4-3 | 81 | molecular size and lipophilicity jointly determine permeability | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M1 수치 직관의 핵심 |
| R&T Fig.4-4 | 82 | BBB permeability vs logP, exceptions by size/efflux | ESSENTIAL | YES | YES | VISUAL_INSPECTED | caffeine/logP 오류 수정에 핵심 |
| R&T Fig.4-5 | 83 | pH partition and ion trapping direction | USEFUL | YES | YES | VISUAL_INSPECTED | CONTEXT지만 learner confusion 방지 |
| R&T Table4-1 | 84 | different membrane properties | USEFUL | NO | NO | VISUAL_INSPECTED | context로 충분 |
| R&T Fig.4-6 | 84 | carrier-mediated transport saturability | USEFUL | YES | YES | VISUAL_INSPECTED | M4/transport saturation bridge |
| R&T Fig.4-7 | 85 | passive vs facilitated absorption profiles | USEFUL | NO | NO | VISUAL_INSPECTED | M1 보조 |
| R&T Fig.4-8 | 86 | transporter locations in eliminating organs | USEFUL | NO | YES | VISUAL_INSPECTED | 복잡해 Step 1 main에는 부적합 |
| R&T Table4-2 | 87–89 | transporter substrates/inhibitors/locations | SKIPPABLE | NO | NO | VISUAL_INSPECTED | detail list overload |
| R&T Fig.4-9 | 90 | passive diffusion/efflux balance in BBB | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Eq.4-26 intuition에 중요 |
| R&T Fig.4-10 | 91 | indinavir plasma vs CSF unbound concentration | USEFUL | YES | YES | VISUAL_INSPECTED | transporter/BBB clinical anchor |
| R&T Fig.4-11 | 91 | grapefruit juice reduces fexofenadine exposure | SKIPPABLE | NO | NO | VISUAL_INSPECTED | transporter DDI 세션으로 이월 |
| R&T Fig.4-12 | 92 | SGLT2 inhibition and glucose/HbA1c | SKIPPABLE | NO | NO | VISUAL_INSPECTED | drug target topic, current scope 밖 |
| R&T Table4-3 | 93 | activated charcoal and reversible transport | USEFUL | NO | NO | VISUAL_INSPECTED | reversible transport illustration, but main flow 아님 |
| R&T Fig.4-13 | 94 | thiopental tissue distribution by perfusion and affinity | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M2 anchor; redraw helpful |
| R&T Fig.4-14 | 95 | perfusion vs permeability limitation and lymph flow | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M2/macromolecule bridge 핵심 |
| R&T Table4-4 | 96 | organ perfusion rates and sizes | ESSENTIAL | YES | NO | VISUAL_INSPECTED | M2 수치 anchor |
| R&T Fig.4-15 | 96 | perfusion-limited tissue model | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Eq.4-2–4-7 structural basis |
| R&T Fig.4-16 | 98 | approach to tissue equilibrium under different Q/Kp | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M2 핵심 학습 그림 |
| R&T Fig.4-17 | 99 | ribitol mixed/permeability limitation in muscle/liver | USEFUL | YES | YES | VISUAL_INSPECTED | limitation/fallacy 방지 |
| R&T Fig.4-18 | 100 | penicillin G distribution into muscle vs brain | USEFUL | YES | YES | VISUAL_INSPECTED | permeability limitation clinical anchor |
| R&T Table4-5 | 101 | albumin distribution amount/concentration | ESSENTIAL | YES | NO | VISUAL_INSPECTED | 7.5 L floor 근거 |
| R&T Table4-6 | 102 | representative V values by drugs | USEFUL | NO | NO | VISUAL_INSPECTED | Fig.4-19가 더 직관적 |
| R&T Fig.4-19 | 103 | apparent V varies widely across drugs | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M3 Big Idea 핵심 |
| R&T Fig.4-20 | 104 | plasma+tissue mass balance for V | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Eq.4-11/12 intuition |
| R&T Table4-7 | 106 | V, Vb, Vu examples across drugs | USEFUL | YES | NO | VISUAL_INSPECTED | binding within blood 보조 |
| R&T Fig.4-21 | 107 | fraction unbound values for representative drugs | USEFUL | NO | NO | VISUAL_INSPECTED | optional reference |
| R&T Fig.4-22 | 108 | fu variation with protein concentration | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M4 mass-action bridge |
| R&T Fig.4-23 | 110 | propranolol V varies with fu | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M3/M5 source anchor |
| R&T Fig.4-24 | 110 | metoprolol Kp vs acidic phospholipid | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M5 핵심 anchor |
| R&T Table4-8 | 112 | representative small-V drugs | USEFUL | NO | NO | VISUAL_INSPECTED | example list; not central |
| R&T Fig.4-25 | 113 | cephalosporin V increases with fu; intercept ≈ albumin volume | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Apex M3 핵심 그림 |
| R&T Fig.4-26 | 113 | cephalosporin unbound V decreases with fu | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Fig.4-25와 paired concept |
| R&T Table4-9 | 114 | conditions altering albumin and α1-AGP | ESSENTIAL | YES | NO | VISUAL_INSPECTED | clinical translation 핵심 |
| R&T Table4-10 | 115 | fraction of drug in body formulas | USEFUL | NO | NO | VISUAL_INSPECTED | Formula-heavy; context로 충분 |
| R&T Table4-11 | 117 | equilibrium ratio and perfusion rates for study problem | USEFUL | NO | NO | VISUAL_INSPECTED | self-test material |
| R&T Table4-12 | 118 | warfarin nephrotic syndrome PK parameters | ESSENTIAL | YES | NO | VISUAL_INSPECTED | small-Vd clinical anchor |
| R&T Fig.B-1 | 764 | drug pKa range examples | USEFUL | NO | NO | VISUAL_INSPECTED | context figure |
| R&T Fig.B-2 | 765 | percent ionized vs pH for acids/bases | USEFUL | YES | YES | VISUAL_INSPECTED | pH partition context에 유용 |
| R&T Table C-1 | 768 | symbols/definitions for Appendix C | USEFUL | NO | NO | VISUAL_INSPECTED | derivation support |
| R&T Fig.C-1 | 767 | albumin distribution model compartments | ESSENTIAL | YES | YES | VISUAL_INSPECTED | small-Vd model 이해에 핵심 |
| R&T Fig.C-2 | 770 | V vs fu behavior by VR/fuR | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Eq.C-13 geometry |
| R&T Table C-2 | 771 | relationships for drug fractions | USEFUL | NO | NO | VISUAL_INSPECTED | advanced formula table |
| R&T Table C-3 | 773 | distribution parameters of selected drugs | USEFUL | NO | NO | VISUAL_INSPECTED | study problem support |
| R&T Table C-4 | 773 | analysis of distribution data | USEFUL | NO | NO | VISUAL_INSPECTED | optional |
| R&T Table C-5 | 773 | effect of albumin changes on distribution | ESSENTIAL | YES | NO | VISUAL_INSPECTED | warfarin/small-Vd concept reinforce |
| G&W Fig.2.134 | 163 | dose vs total vs unbound concentration-response can reverse potency | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M6 Critical Blow 핵심 |
| G&W Fig.2.135 | 163 | Cavg/Css, Cmax, AUC, AUC above threshold/td | ESSENTIAL | YES | YES | VISUAL_INSPECTED | exposure metrics map |
| G&W Fig.2.136 | 164 | equal AUC can have different peak/duration/toxicity implications | ESSENTIAL | YES | YES | VISUAL_INSPECTED | author warning 핵심 |
| G&W Fig.2.137 | 165 | nonlinear kinetics in rats with dose-normalized curves | USEFUL | NO | NO | VISUAL_INSPECTED | toxicokinetics-specific |
| G&W Fig.2.138 | 166 | once-daily dosing vs controlled input/drug holidays | USEFUL | NO | YES | VISUAL_INSPECTED | exposure duration concept 보조 |
| G&W Fig.2.139 | 166 | capacity- and time-dependent clearance can offset | USEFUL | NO | YES | VISUAL_INSPECTED | toxicokinetic nuance |
| G&W Fig.2.140 | 167 | fu vs Cu cleaner than fu vs total C | ESSENTIAL | YES | YES | VISUAL_INSPECTED | M6/M4 bridge 핵심 |
| G&W Fig.2.141 | 168 | species total curves differ; unbound ECu50 ≈2 nM aligns | ESSENTIAL | YES | YES | VISUAL_INSPECTED | species extrapolation 핵심 |
| G&W Table2.21 | 169 | exposure metrics and applicability | ESSENTIAL | YES | NO | VISUAL_INSPECTED | M6 table backbone |
| G&W Fig.47.1 | 691 | free fraction vs Cu at two protein concentrations for two compounds | ESSENTIAL | YES | YES | VISUAL_INSPECTED | PK47 핵심 데이터 그림 |
| G&W Table47.1 | 692 | PK47 raw binding data for compounds 1/2 | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Eq.47 fitting source data |

---

## Patch Memo Independent Classification

| Patch Memo Claim | Independent Classification | Rationale |
|---|---|---|
| M4 수식 표기 불안정/오류 | ERROR confirmed | Curation Map formula differs from Eq.47:1 |
| PK47이 독립 개념처럼 보일 위험 | OPTIONAL/SHOULD_FIX | 구조상 M4 안에 들어가 있으나 title/curation에서 PK47이 전면화됨 |
| M1 Big Idea “매년 수십 건” 과함 | NOT_IN_SOURCE confirmed | 첨부 PDF 근거 없음 |
| Regulatory 표현 과함 | NOT_IN_SOURCE confirmed for deficiency letter/FDA guidance | IND/NDA general recommendation은 source 있음; deficiency letter는 없음 |
| Rodgers–Rowland/PBPK 확장 과함 | NOT_IN_SOURCE confirmed | 첨부 PDF 밖 |
| CONTEXT 항목 길어질 위험 | OPTIONAL | 실제 v0에서는 일부 context가 적정, 일부는 확장됨 |
| Self-test/보스 딜레마는 source 밖 가정 포함 | NOT_IN_SOURCE but pedagogically permissible if tagged | hypothetical marker 필요 |

---

## Final Action List for Phase 2 / Phase 4A

1. **Curation Map M4 식 즉시 수정 또는 삭제.**  
2. **M1 Big Idea caffeine/logP 오류 수정.**  
3. **모든 source 밖 실무·규제 claim에 `[실무 추론]` 또는 `[외부 문헌 필요]` 태그 부여.** 특히 FDA reviewer, deficiency letter, Rodgers–Rowland, 80% variance, one-digit Vd prediction.  
4. **숫자형 시각 추정값은 author-stated value와 분리.** 3.5 h, 1/10, 90-fold, r>0.85, V 50,000 L 등.  
5. **G&W Fig.2.136 equal-AUC warning을 M6에 명확히 보존.**  
6. **Fig.4-26 unbound Vd 감소 메시지를 M3/M6 bridge에 1문장 반영 권장.**  
7. **source attribution 정정:** `fub > 1`은 G&W p.168로.  
8. **lymph flow 정정:** `1–10 mL/min per 70 kg`.  
9. **HTML 전 단계에서 Phase 4C Figure Instruction을 반영:** ESSENTIAL로 표시된 그림은 “view instruction” 후보로 넘김.

---

## Bottom Line

Step 1 Draft v0는 **구조적으로는 합격**이다. 다만 현재 상태는 “원문 기반 핵심 설명 + 고급 실무 추론 + 외부 문헌성 표현”이 한 층위에 섞여 있다. A-Critical 세션에서는 이 혼합이 가장 위험하다. 위 MUST_FIX 항목을 먼저 패치하면 Step 2 HTML 컴파일로 진행 가능하다.

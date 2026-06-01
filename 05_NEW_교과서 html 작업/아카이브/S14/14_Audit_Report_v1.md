# 14_Audit Report v1
## Session 14 · Allometric Scaling: Inter-Species Extrapolation, Body Weight, and Age

**업무 형태:** 파일 분석 / Source Fidelity Audit  
**웹 검색:** OFF  
**입력:** 014_G PDF + 014_T PDF + `14_step1_draft_v0.md` + `S14_phase1_patch memo.md`  
**감사 역할:** Source Fidelity Auditor — rewrite 금지, source 대조만 수행  
**판정:** **Phase 1 재실행 불필요 / Phase 2 감사 통과 전 HTML 직행 금지**

---

## 0. Executive Verdict

이번 Draft v0는 **알로메트리의 핵심 spine** — `Y = a·BW^b`, clearance exponent, volume exponent, Dedrick plot, equal unbound AUC 기반 dose translation — 을 전반적으로 잘 잡고 있습니다. 특히 G&W §2.10과 PK28/PK29의 데이터 anchor는 Step 1 초안으로 충분히 유효합니다.

다만 최종 Content Lock으로 보기에는 다음 오류·과잉 확장이 남아 있습니다.

| 영역 | 판정 | 요약 |
|---|---:|---|
| MUST 카드 구성 | PASS | C1–C5 구조는 적절합니다. |
| G&W §2.10 수식 반영 | PASS with caveat | 핵심 수식은 대부분 맞습니다. |
| PK28/PK29 수치 anchor | CAUTION | PK28 t1/2와 PK29 parameter set에 source 내부 불일치가 있어 version tagging 필요. |
| R&T Ch.14 age/renal maturation 메시지 | UNDERWEIGHT | C5 context에 들어갔지만 저반영입니다. |
| FIH dose translation 방향성 | MUST_FIX | `b=1` 오류의 dose/AUC 방향 설명이 불안정합니다. |
| 4.1배/7.4배/7.7배 fold 계산 | MUST_FIX | species pair가 섞였습니다. |
| FDA/ICH/NDA/MABEL/NONMEM 표현 | MUST_FIX | PDF 직접 근거가 아니므로 라벨링 또는 삭제 필요. |
| HTML 직행 가능성 | NO | Phase 4A patch 전 HTML compile 금지. |

---

# T1: Equation/Numerical Audit

| Item | Draft v0 Expression | PDF Source | Classification | Correction |
|---|---|---|---|---|
| Master allometric equation | `Y = a·BW^b` | G&W Eq.2:374; R&T Eq.22-2 | MATCH | 유지. |
| Log transformation | `ln(Y)=ln(a)+b·ln(BW)` | G&W Eq.2:379; R&T Eq.22-1는 `log Y = log a + b log W` | MATCH | 유지. |
| `a`와 `b` 해석 | `a`는 drug-dependent, `b`는 variable type-dependent | G&W p.177: `a` drug dependent, `b` depends on kinetic/physiological variable | MATCH with caveat | `b`가 완전 drug-independent처럼 보이지 않게 “대체로 변수 유형에 의존하나 실제 CL exponent는 자료 품질·비선형성·binding 등에 따라 변동” 문구 필요. |
| Metabolic rate | `Metabolic rate = a·BW^0.75` | G&W Eq.2:375 | MATCH | 유지. |
| Turnover time | `Energy content/metabolic rate = a3·BW^0.25` | G&W Eq.2:376–2:377 | MATCH | 유지. |
| Surface/volume relation | `surface ∝ length²`, `volume ∝ length³`, `surface ∝ volume^(2/3)` | G&W p.173–174; R&T p.733–734 | MATCH | 유지. |
| Brody exponent range | `b = 0.5–0.8` | G&W p.174: Brody exponent `0.5–0.8` | MATCH | 유지. |
| Clearance allometric model | `CL_i = a·BW_i^b` | G&W Eq.2:380; PK28 Eq.28:1 | MATCH | 유지. |
| Clearance exponent | `b ≈ 0.75`; range `0.5–1.0` | G&W Table 2.22: CL/metabolic rate exponent 0.75; Fig.2.159: majority 0.5–1.0; R&T Fig.22-1/22-4 | MATCH with caveat | G&W p.178는 실제 CL exponent가 `0.2 to >1`까지 갈 수 있다고도 명시. Boundary condition에 반영 필요. |
| R&T mouse-human 7.7-fold example | Draft uses `7.7배` with mouse-human logic | R&T p.733: 20-g mouse → 70-kg human, `3500` vs `455`, 7.7-fold | MATCH only if 20 g mouse 기준 | Draft가 “23 g mouse”와 섞으면 ERROR. `20 g R&T example = 7.7`; `23 g G&W methadone = 7.42`로 분리. |
| Big Idea `4.1배` | “마우스 23 g→인간 70 kg, 3,000배 BW에서 4.1배 오류” | 계산상 rat 250 g→human 70 kg에서 `(280)^0.25≈4.09`; mouse 23 g→human 70 kg에서 `(3043)^0.25≈7.43` | ERROR | `4.1배`는 rat-human 기준으로만 사용. mouse-human 기준은 약 7.4배. |
| `b=1` 사용 시 human CL | “인간 청소율 4.1배 과대평가 → subtherapeutic 시작” | Source는 b=0.75 vs 1의 parameter projection 차이를 설명하나 subtherapeutic 방향은 직접 제시하지 않음 | ERROR | 일반 target AUC dose 계산에서는 CL 과대평가가 dose 과대 산출로 이어질 수 있음. `dose/AUC 계산 방향을 명시`해야 함. |
| Volume allometric model | `V_i = c·BW_i^d` | G&W Eq.2:382; PK28 Eq.28:2 | MATCH | 유지. |
| Volume exponent | `d≈1.0`; blood volume 0.99, skeletal mass 1.09, Vd 1.0 | G&W Table 2.22 | MATCH | 유지. |
| Half-life scaling | `t1/2 ∝ BW^(d-b) ≈ BW^0.25` | G&W Eq.2:391–2:392; Table 2.22 | MATCH | 유지. |
| Breath/heartbeat time | `BW^0.28`, ratio ≈4 | G&W Eq.2:388–2:390 and p.182 | MATCH | 유지. |
| MLP formula | `MLP = 10.839·W^0.636·BW^-0.225` | G&W Eq.2:396; Table 2.23 | MATCH | 유지. |
| MLP values | human 93.4 y; dog 19.7 y; rat 4.7 y; mouse 2.7 y | G&W Table 2.23 | MATCH | 유지. |
| Elementary Dedrick plot | `C/(Dose/BW)` vs `t/BW^(1-b)` | G&W §2.10.6; PK28 Fig.28.2 | MATCH | 유지. |
| Complex Dedrick plot | `C/(Dose/BW^d)` or `C·BW^d/Dose` vs `t/BW^(d-b)` | G&W §2.10.7; Fig.2.158; PK29 Fig.29.3 | MATCH | 유지. |
| Kallynochron definition | clears same volume of plasma per kg BW | G&W §2.10.4 and §2.10.6 | MATCH | 유지. |
| Apolysichron definition | clears same volume of plasma per `BW^d` and eliminates same fraction | G&W §2.10.4 and §2.10.7 | MATCH | 유지. |
| PK28 body weights/doses | mouse 23 g, rat 250 g, man 70 kg; IV bolus 25, 500, 100,000 µg | G&W §2.10.6; PK28 | MATCH | 유지. |
| PK28 t1/2 | Draft uses 1.5/3.9/35 h in final summary; elsewhere may imply 1.5/2.9/35 h | G&W §2.10.6 p.186 says 1.5/2.9/35 h; PK28 p.613 says 1.5/3.9/35 h | RESTORED / SOURCE_DISCREPANCY | `[source discrepancy] §2.10.6=2.9 h, PK28=3.9 h`로 표시. 하나를 선택할 경우 Case Study PK28 기준인지 본문 기준인지 명시. |
| PK28 `a=0.319`, `AUC=3.13`, `3.04` check | Draft uses `AUC=1/a=3.13`; intercept/slope gives 3.04 | G&W p.186; PK28 p.613 | MATCH | 유지. |
| PK28 hepatic extraction | `<10%` | G&W p.186; PK28 p.613 | MATCH | 유지. |
| PK28 model misspecification caution | “unless ≥2 dose levels, multiple dose/steady-state, model misspecification ruled out” | G&W p.186 and PK28 p.614 | MATCH but underused | Keep as explicit warning near C4, not only limitations. |
| PK29 body weights | 20 g, 250 g, 3.5 kg, 14 kg, 70 kg | G&W §2.10.7; PK29 p.616 | MATCH | 유지. |
| PK29 doses | 10, 125, 200, 6000, 12000 µg | G&W §2.10.7; PK29 p.615–616 | MATCH | 유지. |
| PK29 weight range | Draft says `3500-fold`; final summary says `3500배` | G&W §2.10.7 says 3500-fold; PK29 text says 3000-fold, although 70/0.02=3500 | RESTORED / SOURCE_DISCREPANCY | `about 3000–3500-fold` or `70/0.02=3500; Case text says 3000-fold`로 표시. |
| PK29 parameter set | Draft: `a=0.021, b=0.74, c=0.076, d=1.18, e=0.56, g=0.075` | G&W §2.10.7 p.189 exactly this; PK29 p.619 gives `0.021, 0.75, 0.10, 1.21, 0.54, 0.071` | RESTORED / SOURCE_DISCREPANCY | Draft가 “PK29 p.619”까지 같이 cite하면 불일치. `§2.10.7 set`과 `PK29 case set`을 분리 표시해야 함. |
| PK29 Vss values and phases | Mouse/rat mono; monkey/dog/man bi; Table 29.1 values | G&W PK29 Table 29.1 | MATCH if used | 본문에 유지 가능. |
| Equal unbound AUC | `AUCu,rat = AUCu,man = Dose/CLu` | G&W Eq.2:417 | MATCH | 유지. |
| Dose translation formula | `Dose_man = Dose_rat·(BW_man/BW_rat)^b` | G&W Eq.2:420 | MATCH for equal unbound AUC total dose scaling | C5 제목/본문에서 “FIH starting dose 직접 결정식”으로 쓰면 ERROR. |
| Ratio of mg/kg dose | `(Dose_man/BW_man)/(Dose_rat/BW_rat)=(BW_man/BW_rat)^(b-1)` | Algebra from Eq.2:420 | MATCH | 유지. |
| `CLu = CL/fu` correction | Draft cites unbound clearance and species binding | G&W Eq.2:421; R&T Table 22-1 | MATCH | 유지. |
| Cefazolin fu example | rat 0.07, dog 0.7 | R&T Fig.22-9 text; Table 22-1 has multiple compounds | MATCH | 유지. |
| Ceftizoxime/fluconazole examples | ceftizoxime t1/2 allometry; fluconazole renal CL exponent 0.67 | R&T Fig.22-7/22-8 | MATCH if mentioned | Good context but not central. |
| Epoetin-β exponent | `b=0.775` | R&T Fig.22-5 | MATCH | If used for mAb generalization, label carefully: Epoetin-β is therapeutic protein, not mAb. |
| “mAb generally b≈0.85” | Draft Q6 scenario says mAb 일반적으로 ~0.85 | Not in attached source range | NOT_IN_SOURCE | 삭제하거나 `[교과서 외 일반 지식]`로 표시. |
| Pediatric BSA formula | `BSA=1.73·(Weight/70)^0.75` | R&T Key Relationships p.436 | MATCH | 유지. |
| Pediatric maintenance dose | `Child dose = 1.5·(Weight/70)^0.75·adult dose` when typical patient 60 y | R&T Key Relationships p.436; Fig.14-20 context | MATCH | 유지 가능. |
| Tobramycin child example | 15 kg child: daily dose 66 mg, 4.4 mg/kg | R&T p.433 | MATCH if included | Draft does not centralize; optional. |
| CYP3A elderly decline | Draft: `60세 이상 1%/yr`, `80세≈60세의 80%` | R&T Fig.14-13: elderly 65–75 has 60–70% of young adult; “1% per year” rule is discussed by analogy to creatinine clearance | RESTORED with caveat | `1%/yr` should be phrased as approximate heuristic, not exact CYP3A4 linear formula from 60 onward. |
| Chronologic vs functional age | Draft underuses | R&T Ch.14 opening and elderly section | MISSING / SHOULD_FIX | Add to C5/§8: BW scaling is starting point, not age/maturation/renal function complete model. |
| NONMEM `$PK` example | `TVCL = THETA(1)*(WT/70)^0.75` | Not in attached textbook source | NOT_IN_SOURCE | Keep only as `[교과서 외 구현 번역]`. |
| PBPK/QSP implementation | PBPK is in R&T Ch22; QSP not central in attached source | PARTIAL / NOT_IN_SOURCE | PBPK may remain as R&T context; QSP should be `[교과서 외 확장]`. |
| ICH/FDA standard, MABEL, Deficiency Letter | Multiple statements in Draft | Not in attached PDFs | NOT_IN_SOURCE | Remove or label `[교과서 외 규제/실무 해석]`; do not present as PDF-supported. |
| “NDA Deficiency Letter direct reason” | Curation Map and Critical Blow | Not in PDFs | NOT_IN_SOURCE | MUST_FIX. |

---

# T2: Examples & Data Audit

| Item | Draft v0 Status | PDF Location | Classification | Importance | Action |
|---|---|---|---|---:|---|
| G&W Fig.2.142 clearance × potency × dose | mostly absent | G&W p.170 | MISSING | MEDIUM | C1/C5 intro에 “scaled CL × potency가 early decision metric”로 1문장 보강 가능. |
| G&W Fig.2.143 in vitro/in vivo reductionistic vs in vivo/in vivo integrative | partially implied | G&W p.171 | MISSING | MEDIUM | C5 또는 §8에 scaling data source 구분으로 1문장. |
| G&W Fig.2.144 oxygen consumption vs BW | included conceptually | G&W p.172 | INCLUDED_CORRECT | HIGH | 유지. |
| G&W Fig.2.145 scalable vs less scalable compound | underrepresented | G&W p.174 | MISSING | HIGH | Allometry failure signature의 핵심 visual anchor로 C2 limitation에 추가 권장. |
| G&W Fig.2.146 Vss examples | absent | G&W p.175 | MISSING | LOW | C3 enrichment only. |
| G&W Fig.2.148 log-log CL vs BW | included | G&W p.176 | INCLUDED_CORRECT | HIGH | 유지. |
| G&W Fig.2.149 exponent 1 vs 0.75 | included conceptually | G&W p.177 | INCLUDED_CORRECT | HIGH | 유지. |
| G&W Fig.2.150 prediction interval caution | partly included | G&W p.177 | INCLUDED_CORRECT | MEDIUM | “correlation ≠ precise prediction” 메시지 명시 권장. |
| G&W Fig.2.151 sources of human CL variability | included | G&W p.178 | INCLUDED_CORRECT | HIGH | 유지. |
| G&W Fig.2.152 within vs between species exponent | weak | G&W p.178 | MISSING | MEDIUM | 0.67 vs 0.75 논의에서 useful. |
| G&W Table 2.22 exponent/doubling table | included | G&W p.180 | INCLUDED_CORRECT | HIGH | 유지. |
| G&W Fig.2.153 clinical dose variability | included | G&W p.180 | INCLUDED_CORRECT | HIGH | 유지. |
| G&W Fig.2.154 first dose difficulty / 500–3000 mg tablet example | partly included | G&W p.181 | INCLUDED_CORRECT | MEDIUM | “reasonable first dose uncertainty” 근거로 C5에 짧게 반영. |
| G&W Table 2.23 MLP | included | G&W p.183 | INCLUDED_CORRECT | MEDIUM | 유지. |
| G&W Fig.2.155 leverage of species | included | G&W p.184 | INCLUDED_CORRECT | HIGH | 유지. |
| G&W Fig.2.156 methadone elementary Dedrick | included | G&W p.184 | INCLUDED_CORRECT | HIGH | 유지. |
| G&W Table 2.24 PK28 summary | included partly | G&W p.186 | INCLUDED_CORRECT with source discrepancy | HIGH | t1/2 2.9/3.9 discrepancy tag. |
| G&W Fig.2.157 Compound X raw curves | included | G&W p.187 | INCLUDED_CORRECT | HIGH | 유지. |
| G&W Fig.2.158 complex Dedrick | included | G&W p.189 | INCLUDED_CORRECT | HIGH | 유지. |
| G&W Fig.2.159 b distribution 91 compounds | included | G&W p.191 | INCLUDED_CORRECT | HIGH | 유지. |
| PK28 Methadone case | included | G&W PK28 p.611–614 | INCLUDED_CORRECT with source discrepancy | HIGH | t1/2 value label. |
| PK29 Compound X case | included | G&W PK29 p.615–620 | INCLUDED_CORRECT with parameter-set discrepancy | HIGH | §2.10.7 set vs PK29 set 분리. |
| R&T Ch14 typical patient/usual regimen | weak | R&T p.412–415 | MISSING | MEDIUM | C5/§8에 보강. |
| R&T Table 14-1 digoxin young healthy vs CHF inpatient | absent | R&T p.415 | MISSING | HIGH | “age+disease confounding; healthy adult data limited” 메시지에 적합. |
| R&T Fig.14-7 renal-excretion age curve | weak | R&T p.419 | MISSING | HIGH | 소아·고령 dose scaling의 핵심. C5에 반영. |
| R&T Fig.14-8/14-9 neonatal renal maturation | weak | R&T p.420–421 | MISSING | MEDIUM | Neonate caution에 1문장. |
| R&T Fig.14-13 CYP3A elderly decline | included | R&T p.424 | INCLUDED_CORRECT with caveat | MEDIUM | 1%/yr는 heuristic으로 낮출 것. |
| R&T p.435–436 mg/kg/BSA warning and key relationships | partly included | R&T p.435–436 | INCLUDED_CORRECT but underweighted | HIGH | “broader use of mg/kg/BSA rules is suspect”를 C5에 추가. |
| R&T Fig.22-1 physiological allometry | included conceptually | R&T p.732 | INCLUDED_CORRECT | HIGH | 유지. |
| R&T Fig.22-2 0.75 vs 1: 7.7-fold | included but species-pair mixed | R&T p.733 | INCLUDED_ERROR | HIGH | 20 g mouse 기준으로 분리. |
| R&T Fig.22-3 BSA 0.67 | included | R&T p.734 | INCLUDED_CORRECT with caveat | MEDIUM | Ch14 BSA 0.75 formula와 구분. |
| R&T Fig.22-4 cyclophosphamide V/CL exponents | included in summary/context | R&T p.734 | INCLUDED_CORRECT | MEDIUM | 유지. |
| R&T Fig.22-5 epoetin-β b=0.775 | included in self-test | R&T p.735 | INCLUDED_CORRECT but overgeneralized | MEDIUM | mAb 일반화 금지. |
| R&T Fig.22-6 methotrexate Dedrick | mostly absent | R&T p.736 | MISSING | LOW | G&W PK28이 이미 Dedrick anchor이므로 omission justified/optional. |
| R&T Fig.22-7/22-8 ceftizoxime/fluconazole | mentioned in summary | R&T p.737–738 | INCLUDED_CORRECT | LOW | Context only. |
| R&T Fig.22-9 and Table 22-1 protein binding | included | R&T p.739–740 | INCLUDED_CORRECT | HIGH | 유지. |
| R&T Fig.22-10 microdosing | absent | R&T p.741 | OMITTED_JUSTIFIABLE | LOW | 본 세션 핵심 밖. |
| R&T Fig.22-11/22-12 prediction of clearance/distribution | PBPK/in vitro context weak | R&T p.742–743 | MISSING | MEDIUM | “allometry alone vs in vitro/PBPK integration” 메시지로 1문장 가능. |

---

# T3: Author Key Messages

| Message | PDF Location | In Draft v0? | Status |
|---|---|---:|---|
| Scaling is useful for predicting exposure/PK in man, but some compounds are poorly predicted; key question is why failures occur. | G&W §2.10.1 p.170–172 | PARTIAL | SHOULD_FIX: failure criteria를 C2 limitations에 더 명시. |
| Earlier extrapolations carry more risk; later extrapolations are more predictive/confirmative. | G&W p.170–171 | NO | OPTIONAL: drug development stage context로 1문장. |
| Ultimate goal is not only PK but response-time prediction; PD turnover parameters may matter. | G&W p.171 | PARTIAL | SHOULD_FIX: §8에 PD scaling/turnover bridge로 보강. |
| Energy consumption and BW-dependent metabolic rate explain interspecies PK variation. | G&W p.172–173 | YES | PASS. |
| Allometry is especially useful when elimination is physical transport or disposition independent of protein binding; may fail with qualitative metabolic/excretion differences. | G&W p.173 | YES | PASS, but plasma protein binding caveat should be emphasized. |
| A good correlation does not necessarily imply good prediction. | G&W p.177 | PARTIAL | SHOULD_FIX: C2 caution 문장으로 추가. |
| Predicted clinical dose variability depends on effective concentration, animal clearance, and exponent b. | G&W Fig.2.153 p.180 | YES | PASS. |
| First dose prediction from allometric data can have a large range and may not design tolerability study adequately. | G&W p.180–181 | PARTIAL | SHOULD_FIX in C5: equation is backbone, not direct FIH dose. |
| PK28 interpretation requires caution unless multiple dose levels, steady-state/multiple-dose data, and model misspecification are ruled out. | G&W p.186 / PK28 p.614 | PARTIAL | SHOULD_FIX: warning should be elevated near PK28 anchor. |
| Equal unbound AUC equation assumes equal unbound areas; shapes may differ substantially. | G&W p.190 | PARTIAL | MUST_FIX: C5 should state formula assumptions. |
| Allometric scaling works for many compounds if data are well-behaved and precise, but fails for binding, metabolism, polymorphism, enterohepatic, nonlinear, route differences, etc. | G&W p.191 | YES | PASS. |
| Chronologic age does not necessarily define functional age; chapter statements apply to average persons, not individuals. | R&T Ch14 p.411–412 | WEAK | SHOULD_FIX. |
| Flat dosing regimens that fail to account for age are unlikely to meet individual elderly needs. | R&T p.412 | WEAK | SHOULD_FIX. |
| The typical patient depends on drug and indication; in chapter, typical patient often considered 60 y and 70 kg. | R&T p.414 | NO/WEAK | OPTIONAL/SHOULD depending on C5 age framing. |
| Age/disease confounding matters; young healthy estimates may have limited application to patients, as with digoxin. | R&T Table 14-1 and text p.415 | NO | SHOULD_FIX. |
| Absorption rate may change with age, but extent generally assumed unchanged in subsequent dosage calculations. | R&T p.416–417 | NO | OMITTED_JUSTIFIABLE. |
| Weight adjustment generally considered when weight differs by >30% from typical patient. | R&T p.417 | NO | OPTIONAL. |
| Children and elderly dosing require renal maturation/senescence and BSA/renal function; BW alone is insufficient. | R&T p.419–436 | PARTIAL | SHOULD_FIX. |
| Broader use of mg/kg or mg/1.73m² rules is suspect unless limits are specified. | R&T p.435 | WEAK | SHOULD_FIX/MUST_FIX because it counterbalances C5 overclaim. |
| Allometry and disposition kinetics: V scales ~1, clearance/functional measures ~0.75. | R&T Ch22 p.732–735 | YES | PASS. |
| 0.75 vs 1 exponent difference becomes large across mouse-human body weight. | R&T Fig.22-2 p.733 | YES but mixed | MUST_FIX species-pair split. |
| Species differences in protein binding can be large and affect prediction. | R&T Fig.22-9/Table 22-1 | YES | PASS. |
| Allometry has been most successful for V; clearance prediction may need in vitro/in vivo models. | R&T p.741–743 | PARTIAL | SHOULD_FIX if PBPK/in vitro context retained. |

---

# T4: Priority Summary

| # | Item | Priority | Rationale |
|---:|---|---|---|
| 1 | Big Idea의 `4.1배`와 mouse 23 g/3,000배 체중 차이 혼용 | MUST_FIX | 계산 기준 species pair가 틀렸습니다. Rat-human은 4.1, mouse-human은 7.4–7.7입니다. |
| 2 | `b=1` 오류 → `subtherapeutic` 시작이라는 방향성 | MUST_FIX | Target AUC 기반 dose 계산에서는 CL 과대예측이 dose 과대 산출로 이어질 수 있습니다. |
| 3 | C5 FIH dose equation을 직접 starting dose 결정식처럼 제시 | MUST_FIX | G&W Eq.2:420은 equal unbound AUC 기반 total dose scaling입니다. FIH starting dose는 safety factor/MABEL/NOAEL 등과 결합되어야 합니다. |
| 4 | NDA Deficiency Letter/FDA reviewer phrase/ICH-FDA standard/MABEL | MUST_FIX | Attached PDFs에 직접 근거 없음. 삭제 또는 `[교과서 외 규제 해석]` 태그 필요. |
| 5 | NONMEM `$PK`, PBPK/QSP 구현 문장 | MUST_FIX | NONMEM/QSP는 PDF 직접 내용 아님. `[교과서 외 구현 번역]` 태그 필요. PBPK는 R&T Ch22 근거가 있으나 세부 구현은 별도. |
| 6 | PK29 parameter set source discrepancy | MUST_FIX | §2.10.7 p.189 set과 PK29 p.619 set이 다릅니다. 둘 중 하나를 명시하거나 discrepancy note 필요. |
| 7 | PK28 rat t1/2 2.9 vs 3.9 h discrepancy | SHOULD_FIX | Source 내부 불일치. Case Study 기준/본문 기준을 분리해야 합니다. |
| 8 | R&T Ch14 age/maturation/renal function 메시지 저반영 | SHOULD_FIX | “BW allometry alone is insufficient”라는 안전장치가 C5의 과감함을 보정해야 합니다. |
| 9 | G&W Fig.2.145 scalable vs less scalable compound 미반영 | SHOULD_FIX | Allometry failure를 시각적으로 가르치는 핵심 figure입니다. |
| 10 | R&T mg/kg/BSA broad rule caution 미반영 | SHOULD_FIX | C5의 FIH/dose translation overclaim을 낮추는 핵심 author message. |
| 11 | CYP3A4 1%/yr 문구 | SHOULD_FIX | R&T는 elderly 60–70% of young adult와 1%/yr heuristic을 제시합니다. 60→80세 exact formula로 쓰면 부정확합니다. |
| 12 | Table 2.27 sources of variability 언급 | SHOULD_FIX | Attached G&W page range에서는 table content 자체가 노출되지 않습니다. “mentioned by source but table not included in excerpt”로 처리. |
| 13 | Epoetin-β b=0.775를 mAb 일반론으로 확장 | SHOULD_FIX | Epoetin-β는 therapeutic protein example; mAb 일반 지수로 source-supported 아님. |
| 14 | Digoxin Table 14-1 누락 | OPTIONAL/SHOULD_FIX | Age+disease confounding 교육 효과가 큽니다. |
| 15 | Microdosing Fig.22-10 누락 | REJECT | 본 세션 core가 아님. Ch22 범위에 있어도 Step 1 MUST로 끌어올리면 scope creep. |
| 16 | PBPK figures 22-13 onward | REJECT for Step 1 core | Draft source는 Ch22 p.731–743 중심. 744 onward PBPK는 후속 세션/Context로 충분. |

---

# T5: Coverage Audit

| PDF Element | Type | PDF Location | Step 1 Status | Omission Verdict | Required Action |
|---|---|---|---|---|---|
| 2.10 Inter-Species Scaling | Section | G&W p.170–191 | INCLUDED_AS_MUST | — | 유지. |
| 2.10.1 When and why extrapolate? | Section | G&W p.170–172 | INCLUDED_AS_CONTEXT | MISSING_AUTHOR_MSG partial | Scaling failure question and response-time goal 보강. |
| 2.10.2 What is allometry? | Section | G&W p.172–173 | INCLUDED_AS_MUST | — | 유지. |
| 2.10.3 Allometric equations | Section | G&W p.173–180 | INCLUDED_AS_MUST | — | 유지. |
| 2.10.4 Time scales differ between species | Section | G&W p.181–183 | INCLUDED_AS_CONTEXT | — | 유지. |
| 2.10.5 Estimation of parameters | Section | G&W p.183–184 | INCLUDED_AS_CONTEXT | MISSING_BRIDGE partial | Leverage/parameter precision as context. |
| 2.10.6 Elementary Dedrick plot | Section | G&W p.184–186 | INCLUDED_AS_MUST | — | 유지. |
| 2.10.7 Complex Dedrick plot | Section | G&W p.186–189 | INCLUDED_AS_MUST | — | 유지. |
| 2.10.8 Integration of concepts | Section | G&W p.189–190 | INCLUDED_AS_MUST | — | C5 assumptions 강화. |
| 2.10.9 Physiological variables/failure conditions | Section | G&W p.191 | INCLUDED_AS_CONTEXT | — | 유지. |
| Eq.2:374–2:421 | Formulas | G&W p.173–190 | INCLUDED_AS_MUST | — | T1 corrections only. |
| Fig.2.142–2.159 | Figures | G&W p.170–191 | PARTIAL | MISSING_EXAMPLE for 2.145 | T6 참조. |
| Table 2.22 | Table | G&W p.180 | INCLUDED_AS_MUST | — | 유지. |
| Table 2.23 | Table | G&W p.183 | INCLUDED_AS_CONTEXT | — | 유지. |
| Table 2.24 | Table | G&W p.186 | INCLUDED_AS_CONTEXT | SOURCE_DISCREPANCY | t1/2 label. |
| PK28 Methadone | Case Study | G&W p.611–614 | INCLUDED_AS_MUST | SOURCE_DISCREPANCY | t1/2 2.9/3.9 source tag. |
| PK29 Compound X | Case Study | G&W p.615–620 | INCLUDED_AS_MUST | SOURCE_DISCREPANCY | parameter set tag. |
| Ch14 Objectives | Chapter opening | R&T p.411 | INCLUDED_AS_CONTEXT weak | MISSING_AUTHOR_MSG | Age/weight/gender scope summary. |
| Typical patient/usual dosage regimen | Section | R&T p.412–415 | OMITTED_PROBLEMATIC | MISSING_BRIDGE | C5/§8에 typical patient concept 보강. |
| Pharmacodynamics | Section | R&T p.415–416 | OMITTED_JUSTIFIABLE | — | 본 세션 core 아님. |
| Pharmacokinetics—Absorption | Section | R&T p.416–417 | OMITTED_JUSTIFIABLE | — | 본 세션 core 아님. |
| Disposition—Body Weight and Composition | Section | R&T p.417–419 | INCLUDED_AS_CONTEXT | — | 유지. |
| Change in Physiologic Functions and Drug Disposition with Age | Section | R&T p.419–428 | INCLUDED_AS_CONTEXT weak | MISSING_BRIDGE | Renal maturation/elderly decline 보강. |
| Gender Differences | Section | R&T p.427–429 | OMITTED_JUSTIFIABLE | — | 본 세션 core에서 제외 가능. |
| Adjustment of Dosage for Age | Section | R&T p.429–435 | INCLUDED_AS_CONTEXT weak | MISSING_BRIDGE | C5에 핵심 공식과 제한 강화. |
| Dosages per kg or per 1.73 m² | Section | R&T p.435–436 | INCLUDED_AS_CONTEXT | MISSING_AUTHOR_MSG | Broad use suspect 경고 추가. |
| Key Relationships | Box | R&T p.436 | INCLUDED_AS_CONTEXT | — | 유지. |
| Study problems | Problems | R&T p.436–441 | OMITTED_JUSTIFIABLE | — | Step 1 본문에는 불필요. |
| Ch22 Objectives and synthetic prediction framing | Chapter opening | R&T p.731 | INCLUDED_AS_CONTEXT weak | MISSING_AUTHOR_MSG | Allometry limitations/in vitro integration을 보강. |
| Allometry and Disposition Kinetics—Origin/Application | Section | R&T p.732–741 | INCLUDED_AS_MUST | — | 유지. |
| Microdosing | Section | R&T p.739–741 | OMITTED_JUSTIFIABLE | — | 본 세션 core 아님. |
| Prediction of Clearance | Section | R&T p.741–743 | INCLUDED_AS_CONTEXT weak | MISSING_BRIDGE | “clearance prediction may need in vitro hepatic model” 1문장. |
| Prediction of Distribution | Section | R&T p.743 | INCLUDED_AS_CONTEXT weak | — | 유지 가능. |

---

# T6: Figure Inventory & Learning Value Audit

**Inspection note:** PDF page renders and extracted captions/context were used. Rows marked `VISUAL_INSPECTED` were assessed from rendered page content available in the parsed PDF/page images; rows marked `CAPTION_AND_CONTEXT` are conservatively rated and should not be treated as visually essential unless later Phase 4C explicitly redraws them.

## T6-A. Gabrielsson & Weiner §2.10 + PK28/PK29

| Figure/Table | Page | Teaches | Value | View Instruction? | Redraw/New Schematic? | Inspection Method | Rationale |
|---|---:|---|---|---|---|---|---|
| Fig.2.142 | 170 | Human dose as function of scaled clearance and potency | USEFUL | NO | YES | CAPTION_AND_CONTEXT | Early decision context, but not core math. |
| Fig.2.143 | 171 | Reductionistic in vitro/in vivo vs integrative in vivo/in vivo prediction | USEFUL | NO | YES | VISUAL_INSPECTED | Helps distinguish data sources for scaling. |
| Fig.2.144 | 172 | Oxygen consumption per mass and absolute oxygen consumption across BW | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Physiological reason for 0.75 exponent. |
| Fig.2.145 | 174 | Scalable vs less scalable clearance examples; prediction interval difference | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Best figure for “allometry can fail” message; Draft underuses it. |
| Fig.2.146 | 175 | Vss scaling for two compounds | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Supports volume exponent discussion. |
| Fig.2.147 | 175 | Physiological variables vs BW | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Reinforces exponent types. |
| Fig.2.148 | 176 | Log-log CL vs BW and intercept/slope | ESSENTIAL | YES | NO | CAPTION_AND_CONTEXT | Direct visual for `a` and `b`. |
| Fig.2.149 | 177 | Linear scale and log-log comparison for b=1 vs b=0.75 | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Central plausible fallacy figure. |
| Fig.2.150 | 177 | Prediction interval around allometric regression | USEFUL | YES | NO | CAPTION_AND_CONTEXT | Caution: correlation not exact prediction. |
| Fig.2.151 | 178 | Variability sources: animal CL, BW ratio, exponent b | ESSENTIAL | YES | YES | CAPTION_AND_CONTEXT | Supports C5 uncertainty and leverage. |
| Fig.2.152 | 178 | Within- vs between-species exponent differences | USEFUL | NO | YES | CAPTION_AND_CONTEXT | Helps 0.67 vs 0.75 nuance. |
| Table 2.22 | 180 | Doubling BW factors for exponents and examples | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Core reference for b/d distinction. |
| Fig.2.153 | 180 | Sources of predicted clinical dose variability | ESSENTIAL | YES | YES | CAPTION_AND_CONTEXT | Strong reason not to overstate FIH formula. |
| Fig.2.154 | 181 | Difficulty predicting first dose; large dose range | USEFUL | YES | NO | CAPTION_AND_CONTEXT | Useful C5 caution. |
| Table 2.23 | 183 | MLP by species | USEFUL | NO | NO | VISUAL_INSPECTED | Context for physiological time. |
| Fig.2.155 | 184 | Leverage of species in CL regression | USEFUL | YES | NO | CAPTION_AND_CONTEXT | Supports species selection discussion. |
| Fig.2.156 | 184 | Methadone raw and elementary Dedrick normalized curves | ESSENTIAL | YES | YES | CAPTION_AND_CONTEXT | Primary elementary Dedrick anchor. |
| Table 2.24 | 186 | Methadone CL, V, AUC, t1/2 for mouse/rat/man | ESSENTIAL | YES | NO | CAPTION_AND_CONTEXT | Numerical anchor but OCR/table extraction incomplete. |
| Fig.2.157 | 187 | Compound X raw multi-species curves | ESSENTIAL | YES | NO | CAPTION_AND_CONTEXT | Shows need for complex Dedrick. |
| Fig.2.158 | 189 | Complex Dedrick superposition | ESSENTIAL | YES | YES | CAPTION_AND_CONTEXT | Central C4 visual. |
| Fig.2.159 | 191 | Distribution of clearance exponent b for 91 compounds | ESSENTIAL | YES | NO | CAPTION_AND_CONTEXT | Supports realistic exponent variability. |
| Fig.28.1 | 612 | Methadone observed/predicted curves | USEFUL | YES | NO | CAPTION_AND_CONTEXT | Case-specific validation. |
| Table 28.1 | 612 | Methadone CL/V/AUC/t1/2 by species | ESSENTIAL | YES | NO | CAPTION_AND_CONTEXT | Needs manual verification due source discrepancy. |
| Fig.28.2 | 613 | Elementary Dedrick plot for methadone | ESSENTIAL | YES | YES | CAPTION_AND_CONTEXT | Best learner view for kallynochron. |
| Fig.29.1 | 616 | Compound X IV bolus data in five species | ESSENTIAL | YES | NO | CAPTION_AND_CONTEXT | Shows raw interspecies differences. |
| Table 29.1 | 616 | Compound X Clin vivo/in vitro, Vss, half-life, BW, phases | ESSENTIAL | YES | NO | CAPTION_AND_CONTEXT | Main data table for PK29. |
| Fig.29.2 | 617 | Log-log CL and Vss allometry for Compound X | ESSENTIAL | YES | NO | CAPTION_AND_CONTEXT | Direct source for initial a,b,c,d. |
| Fig.29.3 | 619 | Raw fit and complex Dedrick superposition | ESSENTIAL | YES | YES | CAPTION_AND_CONTEXT | Best final visual for complex Dedrick. |

## T6-B. Rowland & Tozer Ch.14

| Figure/Table | Page | Teaches | Value | View Instruction? | Redraw/New Schematic? | Inspection Method | Rationale |
|---|---:|---|---|---|---|---|---|
| Fig.14-1 | 412 | Elderly-skewed disease incidence | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Context for typical patient only. |
| Fig.14-2 | 413 | Diseases distributed across lifespan; migraine sex difference | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Context. |
| Fig.14-3 | 413 | Hay fever more common in youth | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Context. |
| Fig.14-4 | 414 | Prescription drug use increases with age/polypharmacy | USEFUL | NO | NO | VISUAL_INSPECTED | Supports elderly dosing relevance. |
| Table 14-1 | 415 | Digoxin PK in young healthy vs CHF inpatients | USEFUL | YES | NO | VISUAL_INSPECTED | Good warning: healthy adult ≠ patient. |
| Fig.14-5 | 416 | Desflurane MAC decreases with age | USEFUL | NO | NO | VISUAL_INSPECTED | PD age sensitivity; not core. |
| Fig.14-6 | 417 | Average weight over lifespan | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Background for dose equations. |
| Table 14-2 | 418 | Neonate/adult plasma binding and Vd | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Supports age distribution differences. |
| Fig.14-7 | 419 | Half-life, clearance, maintenance dose across age for renal drug | ESSENTIAL | YES | YES | CAPTION_AND_CONTEXT | Most important R&T Ch14 figure for this session. |
| Fig.14-8 | 420 | Neonatal creatinine clearance day 1 vs day 6 | USEFUL | YES | NO | VISUAL_INSPECTED | Maturation warning. |
| Fig.14-9 | 421 | Creatinine clearance vs conceptional age | USEFUL | YES | NO | CAPTION_AND_CONTEXT | Prematurity/renal maturation. |
| Fig.14-10 | 422 | Physiologic functions decline ~1%/yr in adulthood | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Supports elderly decline heuristic. |
| Fig.14-11 | 423 | Renal/hepatic functional decline context | USEFUL | NO | NO | CAPTION_AND_CONTEXT | OCR caption incomplete; manual review optional. |
| Fig.14-12 | 424 | Pediatric duodenal CYP3A4 activity vs age | USEFUL | NO | NO | VISUAL_INSPECTED | Maturation context. |
| Fig.14-13 | 424 | CYP3A clearance in elderly ~60% of young adults | USEFUL | YES | NO | VISUAL_INSPECTED | Draft uses this; view recommended. |
| Fig.14-14 | 425 | Diazepam half-life across lifespan | USEFUL | NO | NO | VISUAL_INSPECTED | Age metabolism context. |
| Fig.14-15 | 425 | Neonatal CYP2C19 development | USEFUL | NO | NO | VISUAL_INSPECTED | Maturation context. |
| Fig.14-16 | 426 | Diazepam half-life increases with adult age | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Elderly metabolism context. |
| Fig.14-17 | 427 | Diazepam unbound clearance reduced in elderly | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Clearance vs half-life context. |
| Fig.14-18 | 428 | Warfarin dose decreases with age and sex/genotype | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Practical individualized dosing example. |
| Fig.14-19 | 428 | Gender effect on CYP3A metabolism | SKIPPABLE | NO | NO | CAPTION_AND_CONTEXT | Gender outside current core. |
| Table 14-3 | 429 | Median weights by age/sex | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Supports age/weight equations. |
| Fig.14-20 | 430 | Maintenance dose fraction across age | ESSENTIAL | YES | YES | CAPTION_AND_CONTEXT | Direct dose-adjustment visual. |
| Fig.14-21 | 431 | Bupropion milk/plasma | SKIPPABLE | NO | NO | CAPTION_AND_CONTEXT | Lactation outside core. |
| Fig.14-22 | 432 | AED concentration/dose ratio in children | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Pediatric clearance per kg example. |
| Table 14-4 | 433 | Expected CrCL by age/sex | USEFUL | YES | NO | VISUAL_INSPECTED | Supports age/gender renal adjustment. |
| Table 14-5 | 437 | Diphenhydramine PK in children/young/elderly | OPTIONAL | NO | NO | CAPTION_AND_CONTEXT | Study problem data. |
| Fig.14-23 | 438 | Ceftriaxone clearance age^0.25 | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Age scaling example. |
| Table 14-6 | 439 | Felodipine age PK data | OPTIONAL | NO | NO | CAPTION_AND_CONTEXT | Study problem data. |
| Table 14-7 | 439 | Vd in obese vs control for three drugs | USEFUL | NO | NO | CAPTION_AND_CONTEXT | C3 obesity limitation support. |
| Table 14-8 | 440 | Montelukast pediatric doses | OPTIONAL | NO | NO | CAPTION_AND_CONTEXT | Dose example; not core. |
| Fig.14-24 | 441 | Inhaled anesthetic MAC decreases with age | OPTIONAL | NO | NO | CAPTION_AND_CONTEXT | PD sensitivity; outside core. |

## T6-C. Rowland & Tozer Ch.22 p.731–743

| Figure/Table | Page | Teaches | Value | View Instruction? | Redraw/New Schematic? | Inspection Method | Rationale |
|---|---:|---|---|---|---|---|---|
| Fig.22-1 | 732 | Heart weight ~1, GFR/cardiac output/heat ~0.75 across mammals | ESSENTIAL | YES | YES | VISUAL_INSPECTED | R&T’s core allometry visual. |
| Fig.22-2 | 733 | 0.75 vs 1 exponents create 7.7-fold mouse-human difference | ESSENTIAL | YES | YES | CAPTION_AND_CONTEXT | Directly audits Draft fold error. |
| Fig.22-3 | 734 | BSA exponent close to 0.67 | USEFUL | YES | NO | CAPTION_AND_CONTEXT | Needed to nuance BSA vs 0.75. |
| Fig.22-4 | 734 | Cyclophosphamide V exponent 0.985, CL exponent 0.754 | ESSENTIAL | YES | NO | CAPTION_AND_CONTEXT | Strong CL/V asymmetry example. |
| Fig.22-5 | 735 | Epoetin-β clearance exponent 0.775 | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Protein example; not mAb general rule. |
| Fig.22-6 | 736 | Methotrexate Dedrick plot | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Additional Dedrick example; G&W already covers. |
| Fig.22-7 | 737 | Ceftizoxime t1/2 prediction from animal allometry | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Half-life prediction example. |
| Fig.22-8 | 738 | Fluconazole renal clearance exponent 0.67 | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Renal CL/BSA relation. |
| Fig.22-9 | 739 | fu variability across species, cefazolin 0.07 vs 0.7 | ESSENTIAL | YES | YES | CAPTION_AND_CONTEXT | Key boundary condition. |
| Table 22-1 | 740 | Human vs animal protein binding differences | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Supports unbound clearance correction. |
| Fig.22-10 | 741 | Midazolam microdose predicts therapeutic dose PK | SKIPPABLE | NO | NO | CAPTION_AND_CONTEXT | Out of core. |
| Fig.22-11 | 742 | In vitro metabolic data → hepatic clearance → total clearance | USEFUL | NO | YES | VISUAL_INSPECTED | Useful if Draft keeps PBPK/in vitro context. |
| Fig.22-12 | 743 | Predicted vs observed CYP clearance | USEFUL | NO | NO | CAPTION_AND_CONTEXT | Clearance prediction limits/integration. |

---

# Patch Memo Independent Verification

| Patch Memo Item | Audit Classification | Source-based Decision |
|---|---|---|
| 4.1배와 3,000배 체중 차이 혼용 | ERROR confirmed | Must fix. Rat-human 4.1; mouse-human 7.4–7.7. |
| `CL 과대평가 → subtherapeutic` 방향성 | ERROR/logic confirmed | Must fix. Dose/AUC direction needs explicit framework. |
| C5 FIH formula over-direct | ERROR confirmed | Eq.2:420 is allometric backbone/equal AUCu scaling, not standalone FIH dose decision. |
| NDA/FDA Deficiency Letter 문구 unsupported | NOT_IN_SOURCE confirmed | Remove or label as textbook-external scenario. |
| “ICH/FDA standard b=0.75” unsupported | NOT_IN_SOURCE confirmed for attached PDFs | Lower to physiological allometric rationale; regulatory statement needs external source, but web OFF. |
| R&T Ch14 age/maturation message weak | MATCH confirmed | Should fix. |
| NONMEM/PBPK/QSP implementation label | PARTIAL confirmed | NONMEM/QSP not source; PBPK is source only at concept level. |
| PK28/PK29 exact numbers audit | PATCH MEMO incomplete | Additional finding: PK28 and PK29 have source-internal numerical discrepancies. |

---

# Minimal Phase 4A Patch List

1. **Big Idea 수정**  
   - `mouse 23 g→human 70 kg`이면 fold는 약 `7.4`.  
   - `rat 250 g→human 70 kg`이면 fold는 약 `4.1`.  
   - `R&T Fig.22-2 20 g mouse→70 kg human`이면 fold는 `7.7`.

2. **Dose direction 수정**  
   - `b=1` 단순 mg/kg scaling은 큰 동물/인간에서 unit body weight clearance 감소를 무시하여 human mg/kg dose를 과대 산출할 수 있음.  
   - Target AUC 기반에서는 CL 과대예측 → dose 과대 산출 가능.  
   - `subtherapeutic` 단정 삭제.

3. **C5 제목 조정**  
   - `FIH Dose Translation` → `FIH Dose Translation의 allometric backbone`.  
   - Eq.2:420은 equal AUCu 기반 총량 scaling이며, 실제 starting dose는 safety factor, NOAEL/HED, exposure margin, pharmacologic activity/MABEL 등과 결합된다고 분리.

4. **Regulatory/implementation 태그**  
   - `NDA Deficiency Letter`, `FDA reviewer`, `ICH/FDA standard`, `MABEL`, `NONMEM control stream`, `QSP`는 `[교과서 외 실무/구현 해석]`으로 표시하거나 삭제.

5. **PK28 source discrepancy note**  
   - `t1/2 mouse/rat/man`: G&W §2.10.6 = `1.5/2.9/35 h`; PK28 = `1.5/3.9/35 h`.  
   - 최종본에서는 하나를 선택하지 말고 discrepancy note 삽입.

6. **PK29 parameter set note**  
   - G&W §2.10.7 set: `a=0.021, b=0.74, c=0.076, d=1.18, e=0.56, g=0.075`.  
   - PK29 case set: `a=0.021, b=0.75, c=0.10, d=1.21, e=0.54, g=0.071`.  
   - Draft의 citation scope와 수치를 일치시킬 것.

7. **R&T Ch14 보강 문장**  
   - “BW allometry is the starting point, not the complete dose equation for children or elderly patients; maturation, renal function, biological age, disease state, and body composition may dominate.”

8. **G&W Fig.2.145 보강**  
   - Scalable vs less scalable example을 C2 Limitations 또는 §5 diagnostic signature에 반영.

---

# Final Audit Judgment

**Step 1 Draft v0는 구조적으로 좋은 초안입니다.**  
그러나 현재 상태로는 **FIH dose translation과 규제 문구가 source보다 앞서 나가며**, `4.1/7.4/7.7` fold 계산과 PK28/PK29 source-internal discrepancy를 정리하지 않으면 HTML 컴파일 후 학습자에게 잘못된 확신을 줄 수 있습니다.

**Recommended route:**

```text
원본 v0 보존
→ 이 Audit Report v1 첨부
→ Phase 4A 공식 패치
→ Phase 4C figure/view instruction 반영
→ HTML Compile
```

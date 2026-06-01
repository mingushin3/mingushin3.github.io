# 11_Audit Report v1 — Source Fidelity Audit

**업무 형태**: 파일 분석 / 웹 검색 OFF / PDF 대조 감사  
**입력**: `011_G_Indirect Response Turnover·DRT·Baseline(1).pdf` + `011_T_Indirect Response Turnover·DRT·Baseline(1).pdf` + `11_step1_draft_v0(1).md` + `S11_phase1_patch memo.md`  
**산출**: `11_Audit Report v1`  
**감사 역할**: Source Fidelity Auditor — 문장 개선·비유 추가·교육적 재작성 금지, 원문 근거 대조만 수행  

## Executive Audit Verdict

**판정: CONDITIONAL GO to Phase 3/4A after MUST_FIX patch. HTML 직행은 금지.**

Draft v0는 Gabrielsson의 turnover/indirect response 수식축과 Rowland & Tozer의 time-delay/rate-limiting/duration 임상축을 대체로 잘 통합했다. 핵심 골격인 `turnover foundation`, `4-model taxonomy`, `tss/peak-shift discrimination`, `effect compartment vs turnover`, `PK vs PD rate-limiting`, `duration-log dose relationship`은 원문 근거가 충분하다.

다만 다음 항목은 반드시 수정해야 한다.

1. **Naproxen 오류**: Draft 말미 요약의 `naproxen 250 mg (Fig 8-3)`은 원문과 불일치. 원문은 **single oral 500-mg dose, Fig 8-2, dental pain, 1–8 h sampling, counterclockwise hysteresis**.
2. **Figure number 오류**: `ibuprofen Fig 8-4`, `paclitaxel Fig 8-19` 표기는 오류. Ibuprofen은 **Fig 8-9**, paclitaxel은 **Fig 8-22**. Fig 8-19는 minoxidil.
3. **Minoxidil framing 오류**: `minoxidil (PK-limited topical)`은 부정확. 원문 Fig 8-19는 **single oral 25-mg dose**, baseline MAP 157 mmHg 환자에서 MAP lowering effect를 보인 사례. Topical use는 배경 설명일 뿐 해당 figure의 dosing context가 아니다.
4. **Zooparc® dose 오류**: Draft 상단 `4 oral doses of 5 mg or 25 mg q24h`는 원문 데이터와 불일치. Figure 9.1/9.2의 관측 용량은 **2.5 mg 및 5 mg 반복 투여**이고, `25 mg per day`는 Table 9.1 이후 larger study에 대한 추정/전망이다.
5. **Regulatory overclaim**: `NDA/IND`, `NDA Deficiency Letter`, `FDA Division reviewer`, `Information Request`, `review timeline 3–6개월` 등은 첨부 교과서의 직접 근거가 아니다. 유지하려면 `[교과서 외 실무 해석]` 또는 `[교육용 가상 시나리오]`로 분리해야 한다.
6. **Direct response와 충돌 가능한 과장**: “모든 측정 가능한 약리반응은 시간 지연을 가진다”는 Gabrielsson의 delayed-nature 관점을 반영하지만, R&T Ch.8의 **direct PK-PD link / rapidly equilibrating response** 사례와 함께 제시되어야 한다.
7. **tss/peak-shift 결정 규칙 과잉**: 원문은 tss/peak shift를 강력한 진단 신호로 쓰되, data resolution, dose range, PK-rate limitation, mechanistic prior를 함께 고려하라고 한다. Draft 일부는 deterministic rule처럼 읽힐 수 있다.

---

## T1: Equation/Numerical Audit

| Item | Draft v0 Expression | PDF Source | Classification | Correction |
|---|---|---|---|---|
| Turnover foundation | `dR/dt = kin - kout·R`; `R0 = kin/kout` | G p.237, Eq 3:74–3:76 | MATCH | 수정 불필요. |
| `kin`, `kout` unit semantics | `kin`: response·time⁻¹; `kout`: time⁻¹ | G p.237 | MATCH | 수정 불필요. |
| Hysteresis definition | 동일 농도에서 rising/falling phase response가 다름 | T p.234–235, Fig 8-2 | MATCH | 수정 불필요. |
| Direct response caveat | Draft Big Idea: “모든 측정 가능한 약리반응은 시간 지연” | G p.236의 “all responses delayed in nature” 취지 + T p.239 direct link | RESTORED [확인 필요] | R&T direct link와 충돌하지 않도록 “지연이 무시 가능하면 direct response처럼 다룬다”는 caveat 필요. |
| Negative feedback equations | Eq 2:261–2:263, moderator M, `kout`, `M50`; IgG half-life 11 days at 30 mg·mL⁻¹ | G p.110–111, Fig 2.83–2.84 | MATCH | 수정 불필요. |
| Four-model taxonomy | Models 1–4: inhibit/stimulate × production/loss | G p.237–238, Table 3.3; T p.241 four cases | MATCH | 수정 불필요. |
| Inhibition function | `I(C)` with `0 ≤ Imax ≤ 1`, `IC50` | G p.237, Eq 3:77 | MATCH | 수정 불필요. |
| Stimulation function | `S(C)`, `Emax`, `EC50` | G p.237, Eq 3:78 | MATCH | 수정 불필요. |
| Model 1 equation | `dR/dt = kin·I(C) - kout·R` | G p.238–239, Eq 3:79 | MATCH | 수정 불필요. |
| Model 2 equation | `dR/dt = kin - kout·R·I(C)` | G p.240–241, Eq 3:85 | MATCH | 수정 불필요. |
| Model 3 equation | `dR/dt = kin·S(C) - kout·R` | G p.242–243, Eq 3:90 | MATCH | 수정 불필요. |
| Model 4 equation | `dR/dt = kin - kout·R·S(C)` | G p.244–245, Eq 3:96 | MATCH | 수정 불필요. |
| tss discrimination | Models 1&3 dose-independent tss; Models 2&4 dose-dependent tss | G p.247–251, Table 3.5–3.6, Fig 3.41–3.43 | MATCH with caveat | Deterministic rule처럼 표현된 문장에는 data resolution / PK-rate limitation caveat 필요. |
| `Imax/Emax` semantics | Direct Emax vs turnover multiplier distinction; Fig 3.40 | G p.246, Fig 3.40 | MATCH | 수정 불필요. |
| Initial parameter estimate table | Table 3.6 expressions for Models 1–4 | G p.251, Table 3.6 | MATCH | 수정 불필요. |
| Manual initial estimate recommendation | “invest time in manual derivation”; 2–3 dose levels recommended | G p.251 | MATCH | 수정 불필요. |
| Blocking dose equation | `dA/dt = -kt·A` under blocked synthesis; `Rsyn` estimation | T p.244–245, Fig 8-15, Eq 8-6–8-7 | MATCH | 수정 불필요. |
| DRT framework | baseline, slope, ID50/Imax/A 추출 | G p.272–275, Fig 3.60–3.63 | MATCH | 수정 불필요. |
| Irreversible kill | `dR/dt = -K·C·R`, `SF = exp(-K·AUC)` | G p.257, Eq 3:110–3:112 | MATCH | 수정 불필요. |
| Cell growth/kill | logistic growth + second-order kill; `Bmax ≈ 30,000 CFU` | G p.258–260, Fig 3.49–3.50, Eq 3:117–3:121 | MATCH | 수정 불필요. |
| K notation conflict | G §3.8에서 bacterial kill `K/kk`와 PK elimination `K`가 혼재 | G p.257–260, Eq 3:110–3:120 | MATCH | Phase 4에서는 `Kkill/kk` vs `Kelim`로 교육용 표기 분리 권장. |
| Effect compartment ODE | `dCe/dt = ke0·C - ke0·Ce` | G PD6 p.759–763; T p.244–246, Fig 8-13–8-14 | MATCH | 수정 불필요. |
| PD6 model equivalence | `kout = ke0 = 5.6 h⁻¹`, ~7 min; turnover vs effect compartment similar WRSS/AIC | G PD6 p.763, Table 6.1 | MATCH | 수정 불필요. |
| `tD` formula | `tD = (1/k) ln(Dose/(Cmin·V)) = (1/k) ln(Dose/Amin)` | T p.254–255, Eq 8-12, Fig 8-23 | MATCH | 수정 불필요. |
| Dose doubling rule | dose doubling → duration +1 half-life | T p.255, Fig 8-23–8-24 | MATCH | 수정 불필요. |
| Succinylcholine doses | 0.5/1/2/4 mg·kg⁻¹ i.v.; `k ≈ 0.2 min⁻¹`; half-life about 4 min | T p.255–256, Fig 8-24 | MATCH | 수정 불필요. |
| Succinylcholine linear decline | response declines essentially linearly between 80% and 20%; ~22%/min example | T p.249–250, Fig 8-18 | MATCH | 수정 불필요. |
| Naproxen main data anchor | 500 mg oral, dental pain, 1–8 h sampling, counterclockwise hysteresis | T p.234–235, Fig 8-2 | MATCH where stated | Draft 상단 data anchor는 맞음. |
| Naproxen late summary | `naproxen 250 mg (Fig 8-3)` | T p.234–235, Fig 8-2 | ERROR | `naproxen 500 mg oral (Fig 8-2)`로 수정. Fig 8-3은 downstream pharmacodynamic events schematic. |
| Ibuprofen late summary | `ibuprofen 6 mg/kg (Fig 8-4, clockwise)` | T p.241–242, Fig 8-9 | ERROR | `ibuprofen 6 mg/kg oral (Fig 8-9)`로 수정. Fig 8-4는 tight binding/persistent effect schematic. |
| Minoxidil | 25 mg oral; MAP baseline 157 mmHg | T p.250, Fig 8-19 | MATCH where stated | “topical” framing은 해당 figure context가 아니므로 별도 correction 필요. |
| Minoxidil late summary | `minoxidil (PK-limited topical)` | T p.250, Fig 8-19 | ERROR | `single oral 25-mg dose of minoxidil; MAP-lowering effect`로 수정. |
| Aspirin | 650 mg oral; plasma half-life ~15 min; thromboxane B2 inhibition persists for days | T p.251, Fig 8-20 | MATCH | 수정 불필요. |
| Omeprazole | 40 mg oral; plasma t½ < 1 h; acid output inhibition persists days | T p.252, Fig 8-21 | MATCH | 수정 불필요. |
| Paclitaxel | i.v.; plasma eliminated within ~2 days; leukocytes return to baseline in ~3 weeks | T p.253–254, Fig 8-22 | MATCH where stated | “ANC nadir Fig 8-19” 표기는 correction 필요. |
| Paclitaxel late summary | `paclitaxel ANC nadir (Fig 8-19)` | T p.253–254, Fig 8-22 | ERROR | `paclitaxel leukocyte fraction/leukopenia, Fig 8-22`로 수정. |
| Methylprednisolone doses | 16/31/63/125/250/500/1000 mg i.v. as phosphate prodrug | T p.257–258, Fig 8-25–8-27 | MATCH where exact | Draft 일부 late summary의 `16/32/64/...`는 source exact values가 아니므로 correction 필요. |
| Methylprednisolone rounded summary | `16/32/64/125/250/500/1000 mg` | T p.257, Fig 8-25 | ERROR | `16/31/63/125/250/500/1000 mg`로 수정. |
| Rosuvastatin OATP1B1 | AUC +63%/+111%; MVA AUC response reduction 3.1%/5.8% | T p.258–259, Fig 8-28–8-29 | MATCH | CONTEXT 처리 유지. |
| Ranitidine | 50 mg i.v.; nine renal impairment subjects; CrCl 51–80 mL/min; gastric pH | T p.240, Fig 8-8 | MATCH | 수정 불필요. |
| Ibuprofen | 36 febrile children, 6 months–11 years, 6-mg/kg oral dose | T p.241–242, Fig 8-9 | MATCH | 수정 불필요. |
| Acenocoumarol vs phenprocoumon | 10 mg acenocoumarol; 0.6 mg/kg phenprocoumon [42 mg/70 kg]; half-lives 15 h vs ~5 days | T p.243, Fig 8-11 | MATCH | 수정 불필요. |
| Midazolam | 15 mg/kg orally in rat; EEG 11.5–30 Hz; direct link | T p.239, Fig 8-6 | MATCH | 수정 불필요. |
| PD4 warfarin | `(s)-warfarin` concentration model and lag-time final values; IC50=0.24 mg·L⁻¹, n=1.6, tlag=6.6 h | G PD4 p.742–751, Table 4.1 | MATCH | 수정 불필요. |
| PD5 compound A | V=40 L; K=0.9 h⁻¹; doses 4000/16000/80000 units over 6 h; final kin=19, kout=0.43 h⁻¹, IC50=95, Imax=0.65 | G PD5 p.753–757, Table 5.1 | MATCH | 수정 불필요. |
| PD6 compound B | V=5.205 L; K=0.456 h⁻¹; 10.75/43.0/172 mg; final kin=234, kout=5.6 h⁻¹, EC50=1633 ng·L⁻¹ | G PD6 p.758–763, Table 6.1 | MATCH | 수정 불필요. |
| PD7 compound C | V=28.6 L; K=2.8 h⁻¹; 6400/32000/160000 units; final kin=27, kout=0.92 h⁻¹, SC50=50, Smax=4.5 | G PD7 p.764–769, Table 7.1 | MATCH | 수정 불필요. |
| PD9 Zooparc® parameter values | Ka=1.1 h⁻¹, K=0.128 h⁻¹, V/F=5.0 L·kg⁻¹; final kin=8.8, kout=0.11 h⁻¹, IC50=0.25 µg·L⁻¹, n=1.40 | G PD9 p.778–783, Table 9.1 | MATCH | 수정 불필요. |
| PD9 observed doses | Draft: `4 oral doses of 5 mg or 25 mg q24h` | G PD9 p.778–779, Fig 9.1–9.2; p.782 Table 9.1 discussion | ERROR | 관측 figure dose는 `2.5 mg` and `5 mg` repeated dosing. `25 mg/day`는 larger study에서 충분할 것이라는 전망. |
| Regulatory reviewer scenario | FDA/NDA/IR/3–6개월 delay 등 | 첨부 G/T PDF에는 직접 근거 없음 | NOT_IN_SOURCE | `[교육용 가상 시나리오]` 또는 `[교과서 외 실무 해석]`로 라벨링. Source Fidelity 본문 claim으로 잠그면 안 됨. |

---

## T2: Examples & Data Audit

| Item | Draft v0 Status | PDF Location | Classification | Importance | Action |
|---|---|---|---|---|---|
| Digoxin delay | Included: 1 mg i.v. bolus, 6 normal subjects, distribution equilibrium ~6 h | T Fig 8-1, p.234 | INCLUDED_CORRECT | HIGH | 유지. |
| Naproxen hysteresis | Included correctly in main data anchor as 500 mg oral; incorrectly later as 250 mg/Fig 8-3 | T Fig 8-2, p.234–235 | INCLUDED_ERROR | HIGH | 모든 표기를 `500 mg oral, Fig 8-2, 1–8 h`로 통일. |
| Tissue distribution explanation | Included as hysteresis cause | T p.235–236 | INCLUDED_CORRECT | MEDIUM | 유지. |
| Downstream pharmacodynamic events | Partly included | T Fig 8-3, p.236 | INCLUDED_AS_CONTEXT | MEDIUM | Figure number confusion 방지. Fig 8-3은 naproxen이 아니라 A/B/C compartment schematic. |
| Direct link midazolam | Included | T Fig 8-6, p.239 | INCLUDED_CORRECT | MEDIUM | 유지. |
| Dexamphetamine zero-order decline | Included | T Fig 8-7, p.239–240; Eq 8-1–8-3 | INCLUDED_CORRECT | MEDIUM | 유지. |
| Ranitidine indirect link | Included | T Fig 8-8, p.240 | INCLUDED_CORRECT | MEDIUM | CONTEXT 유지. |
| Ibuprofen system flux | Included but late figure number wrong | T Fig 8-9, p.241–242 | INCLUDED_ERROR | HIGH | `Fig 8-9`로 수정. |
| Warfarin sluggish response/blocking | Included | T Fig 8-10, 8-15, 8-16; G PD4 | INCLUDED_CORRECT | HIGH | 유지. |
| Acenocoumarol vs phenprocoumon | Included | T Fig 8-11, p.243 | INCLUDED_CORRECT | HIGH | 유지. |
| Input-output turnover schematic | Partly included | T Fig 8-12, p.244 | INCLUDED_AS_CONTEXT | MEDIUM | Core ODE와 연결 유지. |
| Effect compartment | Included | T Fig 8-13–8-14, p.244–246; G PD6 | INCLUDED_CORRECT | HIGH | 유지. |
| Region 1/2/3 E-logC | Included | T Fig 8-17, p.248 | INCLUDED_CORRECT | HIGH | `tD` applicability caveat와 연결. |
| Succinylcholine | Included | T Fig 8-18, 8-24, p.249–256 | INCLUDED_CORRECT | HIGH | 유지. |
| Minoxidil | Included main data anchor correctly; late summary wrongly says topical | T Fig 8-19, p.250 | INCLUDED_ERROR | MEDIUM | `oral 25 mg` context로 고정. |
| Aspirin target consumption | Included | T Fig 8-20, p.251 | INCLUDED_CORRECT | HIGH | 유지. |
| Omeprazole target consumption | Included | T Fig 8-21, p.252 | INCLUDED_CORRECT | HIGH | 유지. |
| Paclitaxel leukopenia | Included main data anchor correctly; late summary figure wrong | T Fig 8-22, p.253–254 | INCLUDED_ERROR | MEDIUM | `Fig 8-22`, leukocyte fraction/leukopenia로 수정. |
| Methylprednisolone dose-linearity trap | Included; exact doses correct in main anchor, rounded in late summary | T Fig 8-25–8-27, p.257–258 | INCLUDED_ERROR | MEDIUM | 31/63 mg exact values 유지. |
| Rosuvastatin OATP1B1 | Included as context | T Fig 8-28–8-29, p.258–259 | INCLUDED_CORRECT | LOW–MEDIUM | CONTEXT 1–2문장 유지. |
| Propranolol study problem | Included in self-test context | T Table 8-1, Fig 8-32, p.262–263 | INCLUDED_CORRECT | LOW | Optional. |
| Endogenous substance study problem | Not central | T Table 8-2, Fig 8-33, p.263–264 | MISSING but justifiable | LOW | 본문 카드에는 생략 가능; self-test 확장에는 optional. |
| G negative feedback / IgG | Included as context | G Fig 2.83–2.84, p.110–111 | INCLUDED_CORRECT | MEDIUM | 유지. |
| G turnover taxonomy | Included as core | G Table 3.3, Fig 3.35–3.39 | INCLUDED_CORRECT | HIGH | 유지. |
| G model characteristics / H(C) forms | Included | G Table 3.4–3.5, Fig 3.40–3.43 | INCLUDED_CORRECT | HIGH | 유지. |
| G initial parameter estimates | Included | G Table 3.6, p.251 | INCLUDED_CORRECT | HIGH | 유지. |
| G model behavior / effect compartment issue | Included, Apex | G Fig 3.44–3.46; PD6 Table 6.1 | INCLUDED_CORRECT | HIGH | 유지하되 regulatory overclaim 분리. |
| G irreversible cell kill | Included | G Fig 3.47–3.50, p.256–260 | INCLUDED_CORRECT | MEDIUM | K notation 분리 권장. |
| G DRT miotic data | Included as context | G Fig 3.60–3.63, p.272–275 | INCLUDED_CORRECT | MEDIUM | 유지. |
| G baseline models | Included as context | G Fig 3.92–3.94, Table 3.15, p.317–319 | INCLUDED_CORRECT | MEDIUM | 1–2문장 context 유지. |
| PD4 warfarin case | Included | G PD4 p.742–752 | INCLUDED_CORRECT | HIGH | 유지. |
| PD5 compound A | Included | G PD5 p.753–757 | INCLUDED_CORRECT | HIGH | 유지. |
| PD6 compound B | Included | G PD6 p.758–763 | INCLUDED_CORRECT | HIGH | 유지. |
| PD7 compound C | Included | G PD7 p.764–769 | INCLUDED_CORRECT | HIGH | 유지. |
| PD9 Zooparc® | Included with dose error | G PD9 p.778–783 | INCLUDED_ERROR | HIGH | 관측 dose를 2.5/5 mg로 수정; 25 mg/day는 전망으로 분리. |

---

## T3: Author Key Messages

| Message | PDF Location | In Draft v0? | Status |
|---|---|---|---|
| Time must always be considered when integrating exposure and response after a single dose. | T Ch.8 opening, p.233 | Yes | INCLUDED_CORRECT |
| Response often lags behind plasma concentration; hysteresis helps detect temporal features of drug response. | T p.234–235 | Yes | INCLUDED_CORRECT |
| Direct PK-PD link exists when exposure and response are parallel without appreciable delay. | T p.239, Fig 8-6 | Partly | SHOULD_FIX: Big Idea의 “모든 반응 지연” 표현과 함께 caveat 필요. |
| Time delay may be caused by tissue distribution, downstream pharmacodynamics, system flux, or target binding/turnover. | T p.235–253 | Yes | INCLUDED_CORRECT |
| A measured response can be rate-limited by PK or by PD; the slower process controls the decline. | T p.243 | Yes | INCLUDED_CORRECT |
| In Region 2 of an E-logC relationship, response declines linearly with time after a single dose. | T p.247–249, Fig 8-17 | Yes | INCLUDED_CORRECT |
| Duration of effect is often proportional to log dose; dose doubling increases duration by one half-life. | T p.254–256, Eq 8-12, Fig 8-23–8-24 | Yes | INCLUDED_CORRECT |
| Linear/dose-proportional PK almost never implies dose-proportional PD. | T p.256–258, Fig 8-25–8-27 | Yes | INCLUDED_CORRECT |
| Exposure-response can disconnect when systemic plasma exposure does not reflect site-of-action exposure, e.g., OATP1B1/rosuvastatin. | T p.258–259, Fig 8-28–8-29 | Yes as CONTEXT | INCLUDED_CORRECT |
| Turnover models are biologically/mechanistically motivated and may help explain intra-/interindividual variability. | G p.235 | Yes | INCLUDED_CORRECT |
| G states responses are delayed in nature, with classification depending on time frame and data resolution. | G p.236 | Yes | INCLUDED_BUT_NEEDS_CAVEAT with T direct-link examples. |
| Four basic turnover models are inhibition/stimulation of production/loss. | G p.237–245, Table 3.3 | Yes | INCLUDED_CORRECT |
| Initial parameter estimates should be manually derived; 2–3 dose levels and good resolution help mechanism discrimination. | G p.251 | Yes | INCLUDED_CORRECT |
| Lack of peak shift with increasing doses does not necessarily imply an effect compartment/link model. | G PD9 p.782–783 | Yes | INCLUDED_CORRECT; ensure deterministic tss rule is softened. |
| Turnover vs effect-compartment models can fit similarly under limited designs; additional dose range/repeated dosing/mechanistic information may be needed. | G PD6 p.763; PD9 p.782–783 | Yes | INCLUDED_CORRECT but regulatory claim requires label. |
| Baseline may be constant, time-varying, exposure-varying, or physiologically limited. | G p.317–319, Fig 3.92–3.94, Table 3.15 | Yes as CONTEXT | INCLUDED_CORRECT |

---

## Patch Memo Cross-check

| Memo Item | Audit Classification | Rationale | Priority |
|---|---|---|---|
| Naproxen 용량 표기 흔들림 | MATCH | Draft late summary에 `naproxen 250 mg (Fig 8-3)` 존재. 원문은 500 mg, Fig 8-2. | MUST_FIX |
| NDA/IND/Deficiency Letter 표현은 출처 기반 아님 | MATCH | G/T PDF는 model discrimination과 dose-duration logic을 다루지만 NDA/IR/deficiency terminology를 직접 제공하지 않음. | MUST_FIX |
| MUST 9개는 과밀 | OPTIONAL / SHOULD_FIX | Source fidelity 오류는 아니나 HTML/Content Lock 관점에서 압축 필요. | SHOULD_FIX |
| “모든 측정 가능한 약리반응은 지연” 낮추기 | MATCH | G 취지는 있으나 T direct link와 함께 caveat 필요. | MUST_FIX |
| tss/peak-shift deterministic rule 과잉 | MATCH | 원문은 data resolution과 model limitation caveat를 둔다. | MUST_FIX |
| Card 6 K 표기 충돌 확인 | MATCH | G §3.8에서 kill constant와 PK elimination constant가 모두 `K`로 등장. | SHOULD_FIX |
| R&T 사례 과다로 핵심 흐름 약화 | OPTIONAL / SHOULD_FIX | Source 오류는 아니나 CONTEXT 압축 필요. | SHOULD_FIX |
| Phase 1 재실행 불필요 / Phase 2 필수 / HTML 직행 금지 | MATCH | 현 상태는 source-backed core + fixable errors. | MUST_FIX before HTML |

---

## T4: Priority Summary (sorted: MUST_FIX → SHOULD_FIX → OPTIONAL → REJECT)

| # | Item | Priority | Rationale |
|---:|---|---|---|
| 1 | Naproxen `250 mg / Fig 8-3` | MUST_FIX | 원문과 직접 불일치. `500 mg oral / Fig 8-2`가 정답. |
| 2 | Ibuprofen `Fig 8-4` | MUST_FIX | 원문 figure는 Fig 8-9. Fig 8-4는 tight binding schematic. |
| 3 | Paclitaxel `Fig 8-19 / ANC nadir` | MUST_FIX | 원문 figure는 Fig 8-22, leukocyte fraction/leukopenia. Fig 8-19는 minoxidil. |
| 4 | Minoxidil `topical` framing | MUST_FIX | 해당 원문 사례는 single oral 25-mg dose의 MAP lowering effect. |
| 5 | PD9 Zooparc® observed dose | MUST_FIX | 원문 관측 dose는 2.5/5 mg 반복. 25 mg/day는 future study projection. |
| 6 | Regulatory/NDA/IND/Deficiency/FDA reviewer claims | MUST_FIX | 첨부 PDF 직접 근거 없음. 유지 시 `[교과서 외 실무 해석]` 또는 `[교육용 가상 시나리오]` 라벨 필요. |
| 7 | “모든 측정 가능한 약리반응은 시간 지연” | MUST_FIX | R&T direct link 사례와 함께 caveat가 필요. |
| 8 | tss/peak-shift as deterministic rule | MUST_FIX | 원문은 data resolution, PK-rate limitation, dose range caveat를 둔다. |
| 9 | Methylprednisolone rounded doses 32/64 mg | SHOULD_FIX | 원문 exact dose는 31/63 mg. 정확한 data anchor 유지 필요. |
| 10 | K notation conflict | SHOULD_FIX | Source는 맞지만 학습자 혼란 방지를 위해 `Kkill/kk` vs `Kelim` 분리 필요. |
| 11 | R&T 사례의 MUST/CONTEXT 분리 | SHOULD_FIX | Source 오류는 아니지만 본문 과밀 위험. rosuvastatin/ranitidine/propranolol/study problems는 CONTEXT/optional 권장. |
| 12 | Card 8–9 separation | SHOULD_FIX | Source fidelity 오류는 아니나 rate-limiting + duration formula는 하나의 판단 흐름으로 압축 가능. |
| 13 | Figure pointer/view instruction | SHOULD_FIX | Fig 8-2, 8-11, 8-17, 8-23/24, G Fig 3.40/3.41/3.43/Table 3.6/PD6 Table 6.1은 학습자에게 명시적으로 보라고 해야 함. |
| 14 | Propranolol study problem expansion | OPTIONAL | 원문 근거 있으나 session core는 아님. |
| 15 | Endogenous substance Study Problem 2 | OPTIONAL | T p.263–264 자료이지만 core card에는 생략 가능. |
| 16 | Direct reproduction of textbook figures | REJECT | Image rights = None; Phase 4C에서 독자적 schematic만 허용. |

---

## T5: Coverage Audit

| PDF Element | Type | PDF Location | Step 1 Status | Omission Verdict | Required Action |
|---|---|---|---|---|---|
| G §2.6.7 Feedback | Heading | G p.110–111 | INCLUDED_AS_CONTEXT | OK | Negative feedback/IgG 1–2문장 유지. |
| G inherent / positive / negative feedback equations | Equations 2:259–2:263 | G p.110–111 | INCLUDED_AS_CONTEXT | OK | Moderator model은 context 유지. |
| G Fig 2.83–2.84 | Figures | G p.110–111 | INCLUDED_AS_CONTEXT | OK | T6에서 useful. |
| G §3.7 Turnover Models – Reversible Drug Effects | Heading | G p.235–255 | INCLUDED_AS_MUST | OK | 유지. |
| G §3.7.1 Background | Heading | G p.235–236 | INCLUDED_AS_MUST | OK | Direct vs delayed/hysteresis framing 유지. |
| G Fig 3.33–3.34 | Figures | G p.235–236 | INCLUDED_AS_MUST | OK | Fig 3.33 view instruction 권장. |
| G §3.7.2 Turnover model taxonomy | Heading | G p.236–245 | INCLUDED_AS_MUST | OK | 유지. |
| G Eq 3:74–3:78 | Named equations | G p.237 | INCLUDED_AS_MUST | OK | 유지. |
| G Table 3.3; Fig 3.35–3.39 | Table/Figures | G p.238–245 | INCLUDED_AS_MUST | OK | 4-model side-by-side 유지. |
| G §3.7.3 Model characteristics | Heading | G p.245–247 | INCLUDED_AS_MUST | OK | Emax semantics 유지. |
| G Table 3.4–3.5; Fig 3.40 | Table/Figure | G p.245–247 | INCLUDED_AS_MUST | OK | Fig 3.40 view instruction 권장. |
| G §3.7.4 Initial parameter estimates | Heading | G p.247–251 | INCLUDED_AS_MUST | OK | 유지. |
| G Fig 3.41–3.43; Table 3.6 | Figures/Table | G p.248–251 | INCLUDED_AS_MUST | OK | Table 3.6 essential. |
| G §3.7.5 Model behavior | Heading | G p.252–254 | INCLUDED_AS_MUST | OK | Effect compartment crisis와 연결. |
| G Fig 3.44–3.46 | Figures | G p.252–254 | INCLUDED_AS_MUST | OK | Apex Figure set. |
| G §3.7.6 Model extensions | Heading | G p.255 | INCLUDED_AS_CONTEXT | OK | Table 3.7 context 유지. |
| G §3.8 Irreversible Drug Action | Heading | G p.256–260 | INCLUDED_AS_MUST | OK | 유지. |
| G §3.8.1 Simple irreversible action — Cell killing | Heading | G p.257 | INCLUDED_AS_MUST | OK | K notation 분리. |
| G §3.8.2 Cell growth coupled with cell killing | Heading | G p.258–260 | INCLUDED_AS_CONTEXT | OK | 항균요법 응용 context 유지. |
| G §3.8.3 MIC | Heading | G p.260 onward | OMITTED_JUSTIFIABLE | Out of provided/draft scope | 제공 범위 절단으로 생략 가능. |
| G Fig 3.47–3.50 | Figures | G p.256–260 | INCLUDED_AS_MUST/CONTEXT | OK | Fig 3.47 view recommended. |
| G Eq 3:110–3:122 | Equations | G p.257–260 | INCLUDED_AS_MUST/CONTEXT | OK | Eq 3:122 이후는 절단 범위 주의. |
| G §3.10 Dose-Response-Time Models | Heading | G p.272–275 | INCLUDED_AS_CONTEXT | OK | Card 5/9 context 유지. |
| G §3.10.1 Background | Heading | G p.272 | INCLUDED_AS_CONTEXT | OK | 유지. |
| G §3.10.2 Miotic data | Heading | G p.273–274 | INCLUDED_AS_CONTEXT | OK | Optional detail. |
| G §3.10.3 Locomotor activity | Heading | G p.275 onward | INCLUDED_AS_CONTEXT | OK | 제공 범위 후반 절단 표시 유지. |
| G Fig 3.60–3.63 | Figures | G p.272–275 | INCLUDED_AS_CONTEXT | OK | useful. |
| G §3.12 Baseline models | Heading | G p.317–319 | INCLUDED_AS_CONTEXT | OK | baseline drift context 유지. |
| G Fig 3.92–3.94; Table 3.15 | Figures/Table | G p.317–319 | INCLUDED_AS_CONTEXT | OK | 1–2문장 context 유지. |
| G Case Study PD4 | Case study | G p.742–752 | INCLUDED_AS_MUST | OK | 유지. |
| G PD4 Fig 4.1–4.8; Table 4.1 | Figures/Table | G p.742–752 | INCLUDED_AS_MUST/CONTEXT | OK | Table 4.1 values 유지. |
| G Case Study PD5 | Case study | G p.753–757 | INCLUDED_AS_MUST | OK | 유지. |
| G PD5 Fig 5.1–5.3; Table 5.1 | Figures/Table | G p.753–757 | INCLUDED_AS_MUST | OK | 유지. |
| G Case Study PD6 | Case study | G p.758–763 | INCLUDED_AS_MUST | OK | Apex 유지. |
| G PD6 Fig 6.1; Table 6.1 | Figure/Table | G p.759–763 | INCLUDED_AS_MUST | OK | Table 6.1 essential. |
| G Case Study PD7 | Case study | G p.764–769 | INCLUDED_AS_MUST | OK | 유지. |
| G PD7 Fig 7.1–7.3; Table 7.1 | Figures/Table | G p.764–769 | INCLUDED_AS_MUST | OK | 유지. |
| G Case Study PD9 | Case study | G p.778–783 | INCLUDED_AS_MUST | INCLUDED_ERROR | MISSING_EXAMPLE if dose not corrected | 관측 dose 2.5/5 mg로 수정. |
| G PD9 Fig 9.1–9.5; Table 9.1 | Figures/Table | G p.778–783 | INCLUDED_AS_MUST | OK with correction | Fig 9.5 caveat 유지. |
| T Ch.8 Objectives/opening | Chapter opening | T p.233 | INCLUDED_AS_MUST | OK | time must be considered 메시지 유지. |
| T Time Delays Between Concentration and Response | Heading | T p.234 | INCLUDED_AS_MUST | OK | 유지. |
| T Detecting Time Delays | Heading | T p.234–235 | INCLUDED_AS_MUST | OK with correction | Naproxen correction. |
| T Causes of Time Delay / Tissue Distribution | Heading | T p.235–236 | INCLUDED_AS_MUST/CONTEXT | OK | 유지. |
| T Pharmacodynamics | Heading | T p.236–238 | INCLUDED_AS_CONTEXT | OK | downstream compartment schematic 유지. |
| T Direct and Indirect Link | Heading | T p.239–240 | INCLUDED_AS_MUST/CONTEXT | OK | Direct-link caveat 필요. |
| T Indirect Response Models | Heading | T p.240–245 | INCLUDED_AS_MUST | OK | four cases와 blocking dose 유지. |
| T Systems in Flux | Heading | T p.241–243 | INCLUDED_AS_MUST | OK | Ibuprofen/warfarin 유지. |
| T Revealing the Concentration-Response Relationship | Heading | T p.244 | INCLUDED_AS_MUST | OK | 유지. |
| T Effect Compartment | Heading | T p.244–246 | INCLUDED_AS_MUST | OK | 유지. |
| T Decline of Response with Time | Heading | T p.247–253 | INCLUDED_AS_MUST | OK | 유지. |
| T When Pharmacokinetics Rate-Limits Decline | Heading | T p.247–250 | INCLUDED_AS_MUST | OK | 유지. |
| T When Pharmacodynamics Rate-Limits Decline | Heading | T p.251–253 | INCLUDED_AS_MUST | OK | aspirin/omeprazole/paclitaxel 유지. |
| T Onset and Duration of Response | Heading | T p.254–256 | INCLUDED_AS_MUST | OK | Card 9 유지/압축. |
| T Onset of Effect | Heading | T p.254 | INCLUDED_AS_CONTEXT | OK | brief context. |
| T Duration of Effect | Heading | T p.254–256 | INCLUDED_AS_MUST | OK | Eq 8-12 유지. |
| T Impact of Transporter Polymorphism | Heading | T p.256–259 | INCLUDED_AS_CONTEXT | OK | Rosuvastatin context 유지. |
| T Key Relationships | Summary | T p.260 | OMITTED_PROBLEMATIC | MISSING_AUTHOR_MSG | Key relationship list는 §8 또는 recap에 반영 권장. |
| T Study Problems | Exercises | T p.260–264 | PARTLY_INCLUDED | OK | Core에는 optional; propranolol self-test 포함. |
| T Table 8-2/Fig 8-33 endogenous substance problem | Worked exercise | T p.263–264 | OMITTED_JUSTIFIABLE | Low-critical exercise | 본문 생략 가능. |
| Repeated author message: direct link vs delayed response distinction | Repeated concept | G p.235–236; T p.239 | PARTLY_INCLUDED | MISSING_BRIDGE | Big Idea에 direct-link caveat 필요. |
| Repeated author message: slower of PK/PD clocks controls response decline | Repeated concept | T p.243, p.247–253; G turnover model behavior | INCLUDED_AS_MUST | OK | 유지. |
| Repeated author message: dose/proportional PK does not imply dose/proportional PD | Repeated concept | T p.256–258 | INCLUDED_AS_CONTEXT/MUST | OK | 유지. |

---

## T6: Figure Inventory & Learning Value Audit

**Inspection basis**: PDF rendered page/contact-sheet visual inspection + text/caption cross-check. Direct figure reproduction/design was not performed.

| Figure/Table | Page | Teaches | Value | View Instruction? | Redraw/New Schematic? | Inspection Method | Rationale |
|---|---:|---|---|---|---|---|---|
| G Fig 2.83 | G p.110 | Negative feedback model with response R and moderator M. | USEFUL | NO | YES | VISUAL_INSPECTED | Text alone conveys equations, schematic helps system intuition. |
| G Fig 2.84 | G p.111 | Negative feedback shortens half-life as concentration/moderator increases. | USEFUL | YES | YES | VISUAL_INSPECTED | Useful for feedback-dependent t½ concept. |
| G Fig 3.33 | G p.235 | Direct response vs delayed hysteretic response. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Structural distinction fails without seeing time and C-R panels. |
| G Fig 3.34 | G p.236 | Direct vs indirect response site of drug action. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Core turnover concept schematic. |
| G Table 3.3 | G p.238 | Four basic turnover models and drug action examples. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Side-by-side taxonomy is central. |
| G Fig 3.35 | G p.239 | Model 1 inhibition of production response profile. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Shows dose changes level, not tss. |
| G Fig 3.36 | G p.240 | Warfarin Model 1 semi-log slope for `kout`. | USEFUL | YES | YES | VISUAL_INSPECTED | Reinforces blocking/downslope logic. |
| G Fig 3.37 | G p.241 | Model 2 inhibition of loss response profile. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Needed for dose-dependent tss contrast. |
| G Fig 3.38 | G p.243 | Model 3 stimulation of production response profile. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Needed for production-side stimulation. |
| G Fig 3.39 | G p.244 | Model 4 stimulation of loss response profile. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Needed for loss-side stimulation and tss shortening. |
| G Table 3.4 | G p.245 | Alternative functional forms for H(C). | USEFUL | NO | NO | VISUAL_INSPECTED | Useful but text/table sufficient. |
| G Fig 3.40 | G p.246 | Emax semantic difference across direct and turnover models. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Prevents parameter meaning error. |
| G Table 3.5 | G p.247 | Impact of I(C)/S(C) on tss and R. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Mechanism discrimination core. |
| G Fig 3.41 | G p.248 | Dose impact on the four turnover models. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Visual peak/tss mechanism discriminator. |
| G Fig 3.42 | G p.249 | Response-time curves under model variants. | USEFUL | NO | YES | VISUAL_INSPECTED | Enriches but not structurally mandatory if Fig 3.41/3.43 shown. |
| G Fig 3.43 | G p.250 | Initial slope determinants for Models 1–4. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Directly supports initial-estimate rules. |
| G Table 3.6 | G p.251 | Expressions for initial parameter estimates. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Must be checked for implementation. |
| G Fig 3.44 | G p.252 | Theoretical combination of effect compartment and turnover. | USEFUL | YES | YES | VISUAL_INSPECTED | Key bridge for discrimination crisis. |
| G Fig 3.45 | G p.253 | Link/effect-compartment model fitting turnover-generated data. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Shows misleading link model fit. |
| G Fig 3.46 | G p.254 | Simulations showing dose dependency/peak shift. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Central to effect-compartment vs turnover limitation. |
| G Table 3.7 | G p.255 | Extensions of turnover models. | USEFUL | NO | NO | VISUAL_INSPECTED | Context family only. |
| G Fig 3.47 | G p.256 | Reversible vs irreversible drug action. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Needed to distinguish drug-zero limit. |
| G Fig 3.48 | G p.257 | No-growth vs growth cell kill schematic. | USEFUL | NO | YES | VISUAL_INSPECTED | Helps but equations can carry core. |
| G Fig 3.49 | G p.258 | Bacterial count vs time for five doses including vehicle. | USEFUL | YES | YES | VISUAL_INSPECTED | Empirical anchor for cell growth/kill. |
| G Fig 3.50 | G p.260 | Initial parameter estimation for growth/kill model. | USEFUL | NO | YES | VISUAL_INSPECTED | Useful for Phase 4 schematic. |
| G Fig 3.60 | G p.272 | Dose-response-time model decomposition. | USEFUL | YES | YES | VISUAL_INSPECTED | Supports DRT context. |
| G Fig 3.61 | G p.273 | Prostaglandin/miotic data context. | USEFUL | NO | YES | VISUAL_INSPECTED | Example-specific. |
| G Fig 3.62 | G p.274 | Observed/predicted miotic response vs time. | USEFUL | NO | YES | VISUAL_INSPECTED | Example-specific. |
| G Fig 3.63 | G p.275 | Response vs biophase amount. | USEFUL | NO | YES | VISUAL_INSPECTED | Useful for DRT. |
| G Fig 3.92 | G p.317 | Time/exposure/baseline model patterns. | USEFUL | NO | YES | VISUAL_INSPECTED | Context for baseline models. |
| G Fig 3.93 | G p.318 | Schematic data patterns from baseline/turnover changes. | USEFUL | NO | YES | VISUAL_INSPECTED | Context. |
| G Fig 3.94 | G p.318 | Physiological limit/self-regulation response. | USEFUL | NO | YES | VISUAL_INSPECTED | Context. |
| G Table 3.15 | G p.319 | Examples of baseline models and turnover rates. | USEFUL | NO | NO | VISUAL_INSPECTED | Context table. |
| G Fig 4.1 | G p.742 | Warfarin/vitamin K cycle. | USEFUL | YES | YES | VISUAL_INSPECTED | Mechanistic anchor for PD4. |
| G Fig 4.2 | G p.743 | Observed warfarin concentration and PCA response. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Case data anchor. |
| G Fig 4.3 | G p.743 | Candidate turnover models for warfarin. | USEFUL | YES | YES | VISUAL_INSPECTED | Supports model selection. |
| G Fig 4.4 | G p.746 | Semi-log response slope for `kout`. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Initial estimate anchor. |
| G Fig 4.5 | G p.747 | Sensitivity analysis. | USEFUL | NO | NO | VISUAL_INSPECTED | Diagnostic enrichment. |
| G Fig 4.6 | G p.747 | Sensitivity analysis. | USEFUL | NO | NO | VISUAL_INSPECTED | Diagnostic enrichment. |
| G Fig 4.7 | G p.748 | Sensitivity analysis. | USEFUL | NO | NO | VISUAL_INSPECTED | Diagnostic enrichment. |
| G Fig 4.8 | G p.750 | Warfarin response vs concentration. | USEFUL | YES | YES | VISUAL_INSPECTED | IC50/lag context. |
| G Table 4.1 | G p.751 | Final parameter estimates and model comparison. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Required for PD4 numeric audit. |
| G Fig 5.1 | G p.754 | Compound A observed response at three infusions. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | PD5 data anchor. |
| G Fig 5.2 | G p.755 | Semi-log estimate for PD5. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Initial estimate anchor. |
| G Fig 5.3 | G p.756 | Model 2 schematic for inhibition of loss. | USEFUL | NO | YES | VISUAL_INSPECTED | Reinforces taxonomy. |
| G Table 5.1 | G p.757 | PD5 final parameter estimates. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Required numeric anchor. |
| G Fig 6.1 | G p.759 | PD6 observed response and model fit. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Apex discrimination case. |
| G Table 6.1 | G p.763 | Turnover vs effect compartment estimates. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Core evidence for equal `kout/ke0`. |
| G Fig 7.1 | G p.764 | PD7 response data after infusion. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | PD7 data anchor. |
| G Fig 7.2 | G p.765 | Semi-log / model schematic for PD7. | USEFUL | YES | YES | VISUAL_INSPECTED | Supports estimates. |
| G Fig 7.3 | G p.766 | Response vs concentration for PD7. | USEFUL | NO | YES | VISUAL_INSPECTED | Enrichment. |
| G Table 7.1 | G p.769 | PD7 final parameter estimates. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Required numeric anchor. |
| G Fig 9.1 | G p.778 | Zooparc® repeated-dose response. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Dose correction depends on this. |
| G Fig 9.2 | G p.779 | Zooparc® concentration-response hysteresis at 2.5/5 mg. | USEFUL | YES | YES | VISUAL_INSPECTED | Supports dose correction. |
| G Fig 9.3 | G p.780 | Observed response/concentration relation. | USEFUL | NO | YES | VISUAL_INSPECTED | Context. |
| G Fig 9.4 | G p.781 | Response-time/diagnostic plot. | USEFUL | NO | YES | VISUAL_INSPECTED | Context. |
| G Table 9.1 | G p.782 | PD9 parameter estimates. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Required numeric anchor. |
| G Fig 9.5 | G p.783 | Peak-shift simulations for loss vs production action. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Key caveat: no peak shift ≠ effect compartment. |
| T Fig 8-1 | T p.234 | Digoxin delayed cardiac effect despite falling plasma concentration. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Core time-delay clinical anchor. |
| T Fig 8-2 | T p.235 | Naproxen counterclockwise hysteresis after 500 mg oral dose. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Corrects Draft error. |
| T Fig 8-3 | T p.236 | Downstream pharmacodynamic event compartments A/B/C. | USEFUL | YES | YES | VISUAL_INSPECTED | Not naproxen; figure-number correction needed. |
| T Fig 8-4 | T p.238 | Tight binding causing persistent effect after plasma decline. | USEFUL | NO | YES | VISUAL_INSPECTED | Not ibuprofen; figure-number correction needed. |
| T Fig 8-5 | T p.238 | More downstream measurement gives more delayed response. | USEFUL | NO | YES | VISUAL_INSPECTED | Context. |
| T Fig 8-6 | T p.239 | Midazolam direct PK-PD link in rat EEG. | USEFUL | YES | YES | VISUAL_INSPECTED | Needed to balance “all delayed” message. |
| T Fig 8-7 | T p.240 | Dexamphetamine zero-order linear response decline. | USEFUL | YES | YES | VISUAL_INSPECTED | Supports Eq 8-3. |
| T Fig 8-8 | T p.240 | Ranitidine indirect link in renal impairment. | USEFUL | NO | YES | VISUAL_INSPECTED | Context example. |
| T Fig 8-9 | T p.242 | Ibuprofen system-flux hysteresis in febrile children. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Corrects Draft figure-number error. |
| T Fig 8-10 | T p.243 | Warfarin concentration-response sluggishness. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Core indirect response example. |
| T Fig 8-11 | T p.243 | Acenocoumarol vs phenprocoumon PK vs PD rate-limiting. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Card 8 central figure. |
| T Fig 8-12 | T p.244 | Input-output turnover schematic. | USEFUL | NO | YES | VISUAL_INSPECTED | Supports Eq 8-5. |
| T Fig 8-13 | T p.245 | Effect compartment schematic. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Card 7 essential. |
| T Fig 8-14 | T p.246 | Naproxen effect compartment fitting removes hysteresis. | USEFUL | YES | YES | VISUAL_INSPECTED | Supports link model explanation. |
| T Fig 8-15 | T p.246 | Warfarin blocking dose and prothrombin complex synthesis. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Blocking method core. |
| T Fig 8-16 | T p.247 | Warfarin inhibition vs concentration. | USEFUL | NO | YES | VISUAL_INSPECTED | Supports IC relationship. |
| T Fig 8-17 | T p.248 | E-logC regions 1/2/3 and zero-order decline. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | `tD` applicability depends on this. |
| T Fig 8-18 | T p.250 | Succinylcholine linear decline between 80% and 20%. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Duration mechanics anchor. |
| T Fig 8-19 | T p.250 | Minoxidil MAP lowering after 25 mg oral dose. | USEFUL | YES | YES | VISUAL_INSPECTED | Corrects paclitaxel/minoxidil confusion. |
| T Fig 8-20 | T p.251 | Aspirin short plasma exposure vs days-long thromboxane B2 inhibition. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Target consumption core. |
| T Fig 8-21 | T p.252 | Omeprazole plasma decline vs days-long acid inhibition. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Target consumption/tight binding core. |
| T Fig 8-22 | T p.253–254 | Paclitaxel plasma decline vs delayed leukocyte recovery. | USEFUL | YES | YES | VISUAL_INSPECTED | Corrects Draft figure-number error. |
| T Fig 8-23 | T p.255 | Duration increases by one half-life per dose doubling; log-dose linearity. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Card 9 core. |
| T Fig 8-24 | T p.256 | Succinylcholine T50 vs log dose. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Direct clinical validation of Eq 8-12. |
| T Fig 8-25 | T p.257 | Methylprednisolone/prodrug plasma levels across doses. | USEFUL | NO | NO | VISUAL_INSPECTED | PK evidence part. |
| T Fig 8-26 | T p.257 | AUC proportional to methylprednisolone dose. | USEFUL | YES | NO | VISUAL_INSPECTED | Dose-linear PK anchor. |
| T Fig 8-27 | T p.258 | Lymphocyte response not dose-proportional at high doses. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Dose-linearity trap core. |
| T Fig 8-28 | T p.258–259 | Rosuvastatin plasma PK by OATP1B1 genotype. | USEFUL | NO | NO | VISUAL_INSPECTED | Context. |
| T Fig 8-29 | T p.259 | Rosuvastatin cholesterol synthesis response disconnect. | USEFUL | NO | NO | VISUAL_INSPECTED | Context. |
| T Fig 8-30 | T p.261 | Study problem concentration-response curve. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Exercise-only. |
| T Fig 8-31 | T p.261 | Study problem time profiles. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Exercise-only. |
| T Table 8-1 | T p.262 | Propranolol exercise tachycardia data. | USEFUL | NO | NO | VISUAL_INSPECTED | Optional self-test. |
| T Fig 8-32 | T p.262 | Propranolol response-time plot. | USEFUL | NO | NO | VISUAL_INSPECTED | Optional self-test. |
| T Table 8-2 | T p.263 | Drug/endogenous substance data for study problem. | USEFUL | NO | NO | VISUAL_INSPECTED | Optional. |
| T Fig 8-33 | T p.263–264 | Endogenous substance response-time plot. | USEFUL | NO | NO | VISUAL_INSPECTED | Optional. |

---

## Final Lock Recommendation

**Phase 1 재실행은 불필요**하다. Draft v0의 core curation은 충분히 우수하다. 그러나 다음 패치 전에는 HTML compile로 넘어가면 안 된다.

**Minimum patch set before Content Lock**:

1. Naproxen / ibuprofen / paclitaxel / minoxidil figure-number and dose/context corrections.
2. PD9 Zooparc® dose correction: observed 2.5/5 mg; 25 mg/day는 projection으로 분리.
3. Regulatory/NDA/FDA/IR 문장 source-tier labeling.
4. Direct-link caveat 추가: direct response를 부정하지 않도록 표현 수위 조정.
5. tss/peak-shift discrimination caveat 추가.
6. Methylprednisolone rounded dose correction: 31/63 mg.
7. K notation disambiguation: `Kkill/kk` vs `Kelim`.
8. T Key Relationships summary를 §8 recap 또는 self-test에 짧게 반영.

**Post-patch status expected**: GO to Phase 3 Insight Crucible and Phase 4A Content Lock.

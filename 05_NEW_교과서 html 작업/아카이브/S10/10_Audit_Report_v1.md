# 10_Audit Report v1 — Source Fidelity Audit

**업무 형태:** 파일 분석 / PDF 대조 감사 / 웹 검색 OFF  
**대상 세션:** Session 10 — PD 모델 기초: Emax · Hill · AUEC  
**입력:** `010_G_PD 모델 기초 Emax·Hill·AUEC(1).pdf` + `010_T_PD 모델 기초 Emax·Hill·AUEC(1).pdf` + `10_step1_draft_v0.md` + `S10_phase1_patch memo.md`  
**산출:** Source Fidelity Audit Report v1  
**감사 역할:** Verification only. 문장 개선/교육 강화/재작성은 수행하지 않고, Draft v0의 사실·수식·수치·예시가 PDF source에 대응되는지 판정함.

---

## Executive Verdict

**최종 판정: Conditional Go — Phase 4A 패치 필수 / HTML 직행 금지 / Phase 1 재작성 불필요**

Draft v0의 큰 구조, 즉 **C1 Law of Mass Action → C2 Sigmoid Emax/Hill → C3 Hysteresis → C4 Effect Compartment/Indirect Response → C5 AUEC/Duration** 5-card 구성은 source scope와 대체로 잘 맞는다. 특히 G&W는 receptor occupancy, Emax, sigmoid Emax, composite/multiple-site model, non-steady-state response, AUEC, PD3 model discrimination을 제공하고, R&T는 time delay, hysteresis, effect compartment, systems-in-flux, duration of effect, PK/PD rate-limiting examples를 제공한다.

그러나 Draft v0에는 **source-supported 교과서 사실**과 **실무적·규제적 확장 해석**이 섞여 있다. 특히 다음 항목은 mandatory correction이다.

1. **“5–100배 오차 / FIH 용량 과추정 / NDA 권장 용량”**: PDF 직접 근거 없음 → `NOT_IN_SOURCE`.
2. **Hill `n`의 메커니즘 단정**: G&W는 `n`을 flexibility/sigmoidicity parameter로 설명하며, 큰 `n`이 cooperativity/transduction/receptor-effector heterogeneity를 *indicate/may indicate* 할 수 있다고 말할 뿐, 단독 증명으로 보지 않는다 → 과잉 해석.
3. **Aspirin 75 mg, 7–10일, 수술 전 7일 중단, perioperative bleeding**: R&T 범위는 aspirin 650 mg, plasma half-life 15 min, antiplatelet effect several days 수준 → clinical guideline 확장은 PDF 밖.
4. **Naproxen `ke0 ≈ 0.5–1 hr⁻¹`**: R&T 원문은 effect compartment로 hysteresis가 제거되고 distribution half-life가 minutes to hours라고 설명하지만, 해당 수치 범위는 확인되지 않음.
5. **NONMEM `$DES`, grid search, IIV on EC50/Emax/n, FDA Deficiency Letter/Clinical Hold**: source가 아니라 구현/규제 해석 → `[실무 구현 번역]` 또는 삭제 필요.
6. **G&W §3.6.2–§3.6.5 부재 구간**: Draft가 `[확인 필요 — 첨부 PDF 미포함 구간]`으로 표시한 것은 적절. 단, 해당 구간 내용을 추정해 보완하면 안 됨.

---

## T1: Equation/Numerical Audit

| Item | Draft v0 Expression | PDF Source | Classification | Correction |
|---|---|---|---|---|
| Scope range | G&W §3.1–3.6.1 + §3.6.6–3.6.7 + PD3; R&T Ch.8 | 첨부 PDF: G&W p.199–224, p.229–234, p.732–741; R&T p.233–264 | MATCH | 유지. 단 G&W p.225–228은 실제로 첨부 범위 밖으로 처리해야 함. |
| PD definition | PD = time course of biological effects, exposure-effect relationship, mechanisms | G&W p.199 §3.1 | MATCH | 유지. |
| Ideal PD measure | sensitive, gradual, meaningful, objective, reproducible | G&W p.200 | MATCH | Draft에서 상대적으로 약함. T3/T5에서 SHOULD_FIX. |
| Dose levels | control + response at 2–4 dose levels; one reaches max response | G&W p.200 | MATCH/OMITTED_CONTEXT | Draft에서 명시 약함. C2/PD3 experimental design 맥락에 1문장 보강 권장. |
| Two response classes | graded/continuous vs quantal/dichotomous | G&W p.200–201 | MATCH_AS_CONTEXT | Draft의 주제가 continuous PD이므로 짧은 context로 충분. |
| EC50 definition | agonist concentration producing 50% of maximal possible effect | G&W p.201 | MATCH | 유지. |
| IC50 definition | antagonist concentration reducing specified response to 50% of former value | G&W p.201 | MATCH | 유지. |
| `Emax = α[R_T]` | 모든 receptor occupied 시 maximal response | G&W p.203 Eq.3:6–3:7 | MATCH | 유지. |
| Law of mass action association/dissociation | `d[RC]/dt = k1[R][C] - k-1[RC]`; equilibrium zero | G&W p.202–203 Eq.3:1–3:3 | MATCH | Draft의 `V_c·d[RC]/dt`는 source 식에 volume term이 명시되지 않으므로 simplification/implementation insertion. 삭제 또는 footnote 필요. |
| `K_d = k_-1/k_1` | equilibrium dissociation constant | G&W p.203 Eq.3:3 | MATCH | 유지. |
| Smaller Kd = higher affinity | smaller Kd pushes equilibrium to right | G&W p.203 | MATCH | 유지. |
| `RC/R_T = C/(C+K_d)` | receptor occupancy | G&W p.203 Eq.3:5 | MATCH | 유지. |
| `E/Emax = C/(C+K_d)` / `E = Emax·C/(C+Kd)` | occupancy-to-response model | G&W p.203–204 Eq.3:8–3:10 | MATCH | 유지. |
| `EC50 is much less than Kd` | signal amplification; response curve left of occupancy curve | G&W p.204 Fig.3.4 | MATCH with caveat | 원문은 “often/also exceptions” 맥락. Draft의 “일반적으로 훨씬 작다”는 유지 가능하나 예외 문구 필요. |
| Cascade example 10% occupancy → 90% response | Fig.3.5 caption | G&W p.205 Fig.3.5 | MATCH | 유지. |
| Spare receptor 40% vs 85% occupancy | Fig.3.6 text | G&W p.206 | MATCH | 유지. |
| Cheng-Prusoff | `IC50 = Ki(1 + [L]/Kd)`, `Ki = IC50/(1+[L]/Kd)` | G&W p.208 Eq.3:15–3:16 | MATCH | CONTEXT 처리 적절. |
| Linear effect model | `E = E0 + S·C`; valid in linear range | G&W p.211 Eq.3:22–3:23 | MATCH_AS_CONTEXT | Draft가 Emax의 local approximation으로 둔 것 적절. |
| Log-linear effect model | effect vs log concentration linear often 20–80% max range | G&W p.211–212 Eq.3:24–3:26 | MATCH_AS_CONTEXT | R&T Eq.8-3와 연결 가능. |
| Ordinary Emax model | `E = E0 + Emax·C/(EC50+C)` | G&W p.213 Eq.3:27 | MATCH | 유지. |
| Ordinary Imax model | inhibitory counterpart | G&W p.214 Eq.3:29–3:30 | MATCH | 유지. |
| Sigmoid Emax model | `E = Emax·C^n/(EC50^n+C^n)` | G&W p.216 Eq.3:32 | MATCH | 유지. |
| Hill `n` meaning | Draft: “not merely fitting; therapeutic window gatekeeper; n>1 direct mechanistic signal” | G&W p.216: exponent n does not have direct biological interpretation; extension/flexibility; large n may indicate binding cooperativity/transduction adjustments/receptor-effector heterogeneity | ERROR / OVERINTERPRETATION | 반드시 낮출 것: `n`은 curve steepness/sigmoidicity/flexibility parameter이며, mechanism hypothesis를 제시할 수 있으나 단독 증거는 아님. |
| n range | `n generally varies between 1 and 10` | G&W p.220 | MATCH | 유지 가능. |
| `n<1` interpretation | active metabolites or multiple receptor sites | G&W p.216 | MATCH | 유지. 단 “흔적” 수준으로 표현. |
| Unbound concentration transformation | `ECu50 = EC50·fu` style cancellation; n preserved | G&W p.216–217 Eq.3:33 | MATCH | 유지. |
| Sigmoid Imax with baseline | `E = E0 - Imax·C^n/(IC50^n+C^n)` | G&W p.218 Eq.3:34–3:35 | MATCH | 유지. |
| Graphical slope | `m = n·Emax/4`; `n = 4m/Emax` | G&W p.219 Eq.3:38–3:40 | MATCH | 유지. |
| `C0 = EC50·e^{-2/n}` | intercept recovery | G&W p.219 Eq.3:42 | MATCH | 유지. |
| Target concentration model | Draft Q4 formula for sigmoid Imax baseline | G&W p.221 Table 3.1 | MATCH with sign caveat | Draft의 부호 처리 설명은 혼동 가능. Table 3.1에 맞춰 target response를 baseline-relative 또는 absolute response로 명확히 해야 함. |
| Composite Emax parameters | `IC50,1=1.8`, `IC50,2=23 µg/L`; `Imax,1=4`, `Imax,2=3.2`; `n1=1.4`, `n2=3.7` | G&W p.221–222 Eq.3:43, Fig.3.20 | MATCH | 유지. |
| Multiple binding site model | Eq.3:48; caffeine brain concentration example | G&W p.224 | MATCH_AS_CONTEXT | 유지. |
| Competitive antagonism only start | §3.6.1 included; §3.6.2–3.6.5 absent | G&W p.224 only; p.225–228 absent | MATCH | Draft의 `[확인 필요]` 처리 유지. |
| Non-steady-state response | `dR/dt = k_in - k_out·R`; response kinetics framework | G&W p.229–230 Eq.3:56 onwards | RESTORED / PARTIAL | Draft가 C4/C5에 흡수했으나 세부식은 적게 반영. 핵심만 유지 가능. |
| AUEC definition | `AUC_E = ∫ E dt` | G&W p.233 §3.6.7 | MATCH | 유지. |
| AUEC closed form | `AUC_E = Emax/K · ln(1 + D/(EC50·V))` | G&W p.233 Eq.3:73 | MATCH | 유지. |
| Sigmoid Emax AUEC no closed form | Draft: numerical integration needed | G&W Eq.3:73 only ordinary Emax derivation; sigmoid not given | RESTORED / INFERENCE | 합리적 수학 추론이지만 source 직접문장은 아님. `[수학적 추론]` 태그 권장. |
| R&T time must be considered | “In practice, time always needs to be considered” | R&T p.233 | MATCH | Draft C3–C5 방향과 부합. |
| Digoxin | 1 mg IV; plasma falls while left ventricular ejection-time index rises for first 4 h; wait ~6 h for distribution equilibrium | R&T p.234 Fig.8-1 | MATCH | 유지. |
| Naproxen | 500 mg oral; dental pain; counterclockwise hysteresis | R&T p.234–235 Fig.8-2 | MATCH | 유지. |
| Naproxen `ke0 ≈ 0.5–1 hr⁻¹` | Draft self-test | R&T p.245 Fig.8-13/8-14: effect compartment; distribution half-life minutes to hours | NOT_IN_SOURCE | 삭제 또는 `[확인 필요]`. 원문 수치로 쓰면 안 됨. |
| Hysteresis definition | different path when concentration rises vs falls | R&T p.234–235 | MATCH | 유지. |
| Effect compartment concept | hypothetical compartment linking plasma concentration with response; removes hysteresis in naproxen | R&T p.245–246 Fig.8-13–8-14 | MATCH | 유지. |
| Effect compartment ODE / NONMEM code | Draft `$DES`, `ke0` implementation/grid search | R&T conceptual figure; no NONMEM/grid-search content | NOT_IN_SOURCE | `[실무 구현 번역]`로 분리 또는 삭제. |
| Systems in flux | drug can modulate formation/loss of endogenous substance | R&T p.241–244, p.246–248 | MATCH | 유지. |
| Warfarin | 1.5 mg/kg oral sodium warfarin; prothrombin complex turnover; half-life 1–2 days | R&T p.242, p.247 | MATCH | 유지. |
| Warfarin Eq.8-7 | synthesis rate from A1/A2/Δt + kt·average | R&T p.247 | MATCH | Draft Q6 계산은 source-consistent. |
| Acenocoumarol/phenprocoumon | acenocoumarol t1/2 15 h, return baseline ~3 days; phenprocoumon t1/2 6 days, return ~2 weeks | R&T p.243–244 Fig.8-11 | MATCH | Draft “5d” for phenprocoumon appears inconsistent if present; use 6 days. |
| Succinylcholine | 0.5 mg/kg bolus; elimination t1/2 4 min; `k≈0.2 min^-1`; dose doubling increases duration by 1 half-life | R&T p.249, p.255–256 Fig.8-18/8-24 | MATCH | 유지. |
| Aspirin source anchor | 650 mg oral; t1/2 15 min; antiplatelet activity several days | R&T p.251 Fig.8-20 | MATCH | 유지. |
| Aspirin 75 mg / 7–10 days / surgery 7 days / bleeding | Draft C5 and critical blow | Not in provided R&T/G&W pages | NOT_IN_SOURCE | 삭제 또는 `[교과서 외 임상 확장]`. Source-fidelity 본문에서는 쓰지 말 것. |
| Omeprazole | 40 mg oral; plasma concentration low by ~3 h; t1/2 just less than 1 h; acid inhibition persists days, measured day 1–3 | R&T p.252 Fig.8-21 | MATCH with correction | Draft “2시간 PK → 3일 효과”는 원문보다 거칠다. `t1/2 <1 h; little remains by 3 h; acid suppression returns over days`로 수정. |
| Paclitaxel | plasma little remains after 2 days; leukocyte fraction changes sluggishly over weeks | R&T p.253 Fig.8-22 | MATCH | 유지. |
| Duration formula | `t_D = (1/K) ln(D/A_min)` / log-dose relation | R&T p.254–255 Eq.8-11–8-12, Fig.8-23 | MATCH | 유지. |
| Methylprednisolone | 16–1000 mg; PK AUC dose proportional; lymphocyte response saturates from ~250–1000 mg | R&T p.257–258 Fig.8-25–8-27 | MATCH | 유지. |
| Rosuvastatin OATP1B1 | transporter polymorphism affects plasma exposure but lipid response variability smaller/different | R&T p.258–259 Fig.8-28–8-29 | MATCH | 유지. |
| PD3 parameters | `Imax=34.7`, `IC50=140`, `n=2.03`, `E0=171`; AIC 45.6; ordinary `Imax=49.8`, `IC50=175`, `E0=177`, AIC 50.8 | G&W PD3 p.735 Table 3.2 | MATCH | 유지. |
| PD3 baseline graphical | baseline ~175, Imax ~35, IC50 ~120, n~2 | G&W PD3 p.733–734 | MATCH | 유지. |
| PD3 F-test | 0–500: F*=3.5255 < 5.9874; 0–800: F*=6.4664 > 5.5914 | G&W p.734–735 | MATCH | 유지. |
| PD3 concentration design | need 800 µg/L sample to discriminate; VIF inflated without 800 | G&W p.740–741 | MATCH | 유지. |
| `noise >5% → n precision >50%` | Draft trench tip | G&W Table 3.3: 5% error row has n estimate/precision reported around `1.8 ± 50%`; text says n differs markedly | MATCH with caution | “폭발”은 과장. `5% error에서 n CV 약 50% 및 accuracy 저하`로 낮출 것. |
| “NDA 권장 용량/Deficiency Letter/Clinical Hold” | Draft multiple places | Not in textbook PDFs | NOT_IN_SOURCE | 삭제 또는 `[규제 실무 가상 시나리오]`. |
| “FIH 5–100배” | Draft multiple places | Not in textbook PDFs | NOT_IN_SOURCE | MUST_FIX. |

---

## T2: Examples & Data Audit

| Item | Draft v0 Status | PDF Location | Classification | Importance | Action |
|---|---|---|---|---|
| Full/partial agonist, antagonist, inverse agonist | Context only | G&W p.201 Fig.3.2 | INCLUDED_CORRECT | MEDIUM | 유지. Definitions anchor로 충분. |
| Law of mass action receptor binding | C1 MUST | G&W p.202–204 Eq.3:1–3:10, Fig.3.3–3.4 | INCLUDED_CORRECT | HIGH | 유지. |
| Cascade effect | C1 context/limitation | G&W p.205 Fig.3.5 | INCLUDED_CORRECT | HIGH | 유지. 단 `EC50<Kd` 예외 문구 필요. |
| Spare receptors | C1 context/limitation | G&W p.206 Fig.3.6 | INCLUDED_CORRECT | HIGH | 유지. |
| Saturation binding/NSB | Context | G&W p.206–207 Fig.3.7, Eq.3:13 | INCLUDED_CORRECT | MEDIUM | C1에 1문장 유지. |
| Displacement/Cheng-Prusoff | Context | G&W p.208 Fig.3.8, Eq.3:14–3:16 | INCLUDED_CORRECT | MEDIUM | 유지. |
| Linear/log-linear effect examples | Context | G&W p.210–212 Fig.3.10–3.11 | INCLUDED_CORRECT | MEDIUM | C2 도입부 또는 C5 duration 연결에 충분. |
| Ordinary Emax/Imax examples | C1/C2 bridge | G&W p.213–215 Fig.3.12–3.14 | INCLUDED_CORRECT | HIGH | 유지. |
| Sigmoid Emax model | C2 MUST | G&W p.216–220 Fig.3.15–3.19 | INCLUDED_CORRECT | HIGH | 유지. `n` 해석 패치 필요. |
| Composite Emax Lundström data | C2 limitation/context | G&W p.221–223 Fig.3.20–3.22 | INCLUDED_CORRECT | MEDIUM | 유지. 단 상세는 과도하면 context로 압축. |
| Multiple binding site/caffeine example | C2 limitation/context | G&W p.224 Fig.3.23 | INCLUDED_CORRECT | MEDIUM | 유지. |
| Competitive antagonism §3.6.1 | Context/check-needed | G&W p.224 | INCLUDED_CORRECT | LOW | Scope warning 유지. |
| G&W §3.6.2–3.6.5 | Draft says absent | PDF not attached | INCLUDED_CORRECT | HIGH | 추정 금지. `[첨부 PDF 미포함]` 유지. |
| Kinetics of pharmacological responses | C5 bridge | G&W p.229–232 Fig.3.27–3.31 | INCLUDED_PARTIAL | HIGH | C5에서 AUEC만 강하고 kinetic response equations는 약함. 핵심문장 보강 권장. |
| AUEC | C5 MUST | G&W p.233–234 Fig.3.32, Eq.3:72–3:73 | INCLUDED_CORRECT | HIGH | 유지. |
| PD3 inhibitory Imax model | C2 MUST anchor | G&W p.732–741 | INCLUDED_CORRECT | HIGH | 유지. |
| PD3 Table 3.2 | C2 Plausible Fallacy | G&W p.735 Table 3.2 | INCLUDED_CORRECT | HIGH | 유지. |
| PD3 residuals/F-test/AIC | C2 | G&W p.734–736 Fig.3.3, Eq.3:3 | INCLUDED_CORRECT | HIGH | 유지. |
| PD3 delta function | C2 | G&W p.736–737 Fig.3.4 | INCLUDED_CORRECT | MEDIUM | 유지 가능. |
| PD3 partial derivatives | C2 | G&W p.737 Fig.3.5 | INCLUDED_CORRECT | MEDIUM | 유지 가능. |
| PD3 simulation error | C2 trench tip | G&W p.738–739 Table 3.3, Fig.3.6–3.7 | INCLUDED_CORRECT_WITH_TONE_RISK | HIGH | `폭발` 등 표현 완화. |
| PD3 VIF | C2 | G&W p.740–741 Table 3.4–3.5 | INCLUDED_CORRECT | HIGH | 유지. |
| R&T objectives | Mostly implicit | R&T p.233 | MISSING | MEDIUM | T3/T5에서 key message로 보강. |
| Digoxin | C3 | R&T p.234 Fig.8-1 | INCLUDED_CORRECT | HIGH | 유지. |
| Naproxen hysteresis | C3 | R&T p.234–235 Fig.8-2 | INCLUDED_CORRECT | HIGH | 유지. |
| Propranolol direct link | C3/C5 context | R&T p.235–237, p.240 Fig.8-6 | INCLUDED_CORRECT | MEDIUM | 유지. |
| Locomotor CNS response | Mostly omitted | R&T p.240 Fig.8-7 | OMITTED_JUSTIFIABLE | LOW | 세션 핵심 아님. |
| Ranitidine/gastric pH | Mostly omitted | R&T p.240 Fig.8-8 | OMITTED_JUSTIFIABLE | LOW | C4/C5에서 omeprazole이 더 좋은 anchor. |
| Ibuprofen fever | C4 | R&T p.241 Fig.8-9 | INCLUDED_CORRECT | MEDIUM | 유지. |
| Warfarin/prothrombin | C4 | R&T p.242, p.247 Fig.8-10, 8-15, 8-16 | INCLUDED_CORRECT | HIGH | 유지. |
| Acenocoumarol/phenprocoumon | C5 | R&T p.243–244 Fig.8-11 | INCLUDED_CORRECT_WITH_CORRECTION | HIGH | phenprocoumon half-life source는 6 days. Draft에 5d 있으면 수정. |
| Aspirin | C5 | R&T p.251 Fig.8-20 | INCLUDED_ERROR_PARTIAL | HIGH | 650 mg, t1/2 15 min, several days effect만 source-supported. 75 mg/7–10 days/surgery 7 days는 제거. |
| Omeprazole | C5 | R&T p.252 Fig.8-21 | INCLUDED_CORRECT_WITH_CORRECTION | HIGH | t1/2 just <1 h; little plasma after 3 h; effect returns over days. “2h PK”는 수정. |
| Paclitaxel | C5 | R&T p.253 Fig.8-22 | INCLUDED_CORRECT | MEDIUM | 유지. |
| Duration formula/succinylcholine | C5 | R&T p.254–256 Fig.8-23–8-24 | INCLUDED_CORRECT | HIGH | 유지. |
| Methylprednisolone | C5 context | R&T p.257–258 Fig.8-25–8-27 | INCLUDED_CORRECT | MEDIUM | 유지. |
| Rosuvastatin OATP1B1 | C4/C5 context | R&T p.258–259 Fig.8-28–8-29 | INCLUDED_CORRECT | MEDIUM | 유지. |
| R&T study problems | Mostly omitted | R&T p.260–264 Fig.8-30–8-33, Tables 8-1–8-2 | OMITTED_JUSTIFIABLE | LOW | self-test가 이미 별도 존재하므로 필수 아님. |

---

## T3: Author Key Messages

| Message | PDF Location | In Draft v0? | Status |
|---|---|---|---|
| PD is time course of biological effects, exposure-effect relationships, and mechanisms. | G&W p.199 | Present | MATCH |
| Models of concentration-response provide baseline/maximal effect, sensitivity, and temporal information. | G&W p.199 Fig.3.1 | Present but diffuse | SHOULD_FIX: Figure 3.1 message를 §1에서 더 명확히 표시 권장. |
| Kinetic-dynamic PK/PD modeling aims to identify key in vivo properties to predict magnitude and time course under physiological/pathological conditions. | G&W p.200 | Partly present | SHOULD_FIX: `dose-response only is insufficient` 메시지와 함께 보강. |
| In vitro potency/efficacy or in vivo dose alone is insufficient; exposure over time in relevant compartments is crucial. | G&W p.200 | Present conceptually | MATCH |
| Ideal PD measure should be sensitive, gradual, meaningful, objective, reproducible. | G&W p.200 | Mostly absent | SHOULD_FIX |
| Response should include control and 2–4 dose levels, one reaching maximum response. | G&W p.200 | Mostly absent | SHOULD_FIX, especially C2 experimental design. |
| Occupancy is often not directly related to response; signal amplification may shift response curve left of occupancy curve. | G&W p.204–205 | Present | MATCH with caveat: avoid overclaim. |
| Hill exponent `n` does not have direct biological interpretation; it gives flexibility/steepness and may indicate cooperativity/transduction/heterogeneity. | G&W p.216, p.220 | Partly contradicted | MUST_FIX |
| Concentration drives effect in Emax/Hill; target effect can be inverted to target concentration. | G&W p.220–221 | Present | MATCH |
| No absolute criteria for model selection; residual scatter and WRSS reduction relative to extra parameters matter. | G&W p.741 PD3 conclusion | Present via F-test/AIC | MATCH |
| In practice, time always needs to be considered when integrating PK with response. | R&T p.233 | Present | MATCH |
| Response often lags behind plasma concentration; hysteresis is diagnostic of temporal features. | R&T p.234–235 | Present | MATCH |
| Time delay can be kinetic (distribution to site) or dynamic (affected system turnover). | R&T p.235–244 | Present | MATCH |
| Response may be PK-rate-limited or PD-rate-limited; the slower process governs decline/duration. | R&T p.243–253 | Present | MATCH |
| Duration of effect is often proportional to log dose; doubling dose may increase duration by one half-life under assumptions. | R&T p.254–256 | Present | MATCH |
| PK linearity does not guarantee PD linearity. | R&T methylprednisolone p.257–258 | Present | MATCH |

---

## T4: Priority Summary

| # | Item | Priority | Rationale |
|---|---|---|---|
| 1 | “5–100배 오차”, “FIH 용량 과추정”, “Phase 1 용량 예측에서 5–100배” | MUST_FIX | PDF 직접 근거 없음. G&W supports Kd/EC50 divergence, cascade/spare receptor, not quantitative FIH error. |
| 2 | Hill `n`을 direct mechanism/gatekeeper로 단정 | MUST_FIX | G&W p.216 explicitly says n has no direct biological interpretation. |
| 3 | Aspirin 75 mg, 7–10일, 수술 전 7일 중단, perioperative bleeding | MUST_FIX | R&T source anchor is 650 mg, t1/2 15 min, effect several days; guideline scenario is external. |
| 4 | Naproxen `ke0 ≈ 0.5–1 hr^-1` | MUST_FIX | R&T says distribution half-life minutes to hours; no ke0 numeric range found in provided PDF. |
| 5 | NONMEM `$DES`, grid search, IIV, FDA Deficiency Letter/Clinical Hold | MUST_FIX | Useful implementation/regulatory inference but not textbook source. Must be tagged or removed. |
| 6 | G&W §3.6.2–§3.6.5 treatment | MUST_FIX | Missing PDF pages must remain `[확인 필요 — 첨부 PDF 미포함]`; no reconstruction. |
| 7 | Phenprocoumon half-life if written as 5 days | MUST_FIX | R&T text states phenprocoumon half-life is 6 days in the compared example. |
| 8 | Omeprazole timing wording | SHOULD_FIX | Source: t1/2 just <1 h; little remains after 3 h; acid secretion restoration over days, measurements day 1–3. Draft “2h PK→3d effect” is simplified. |
| 9 | Ideal PD measure and 2–4 dose levels message | SHOULD_FIX | G&W p.200 author key design message underrepresented. |
| 10 | C4 overload | SHOULD_FIX | Conceptually valid but combines effect compartment, indirect response, NONMEM implementation. Better as two internal subblocks. |
| 11 | PD3 residual pattern exact sign ranges | SHOULD_FIX | Source supports larger amplitude/deviating trend; exact sign-by-concentration ranges should be verified visually or softened. |
| 12 | `n` CV/precision “폭발” wording | SHOULD_FIX | Source supports ~50% CV at 5% error and accuracy problems; tone should be neutral. |
| 13 | Composite Emax details | OPTIONAL | Correct but could be context-only to avoid scope creep. |
| 14 | Rosuvastatin OATP1B1 | OPTIONAL | Correct but peripheral; keep as one-line clinical bridge. |
| 15 | Study problems/Tables 8-1–8-2 | OPTIONAL | Useful for exercises but not necessary in Step 1 concept cards. |
| 16 | Adding new external guideline details | REJECT | Would worsen source fidelity unless separately marked as external. |

---

## T5: Coverage Audit

### T5-A. G&W Structural Elements

| PDF Element | Type | PDF Location | Step 1 Status | Omission Verdict | Required Action |
|---|---|---|---|---|
| 3.1 Background | Heading/key message | p.199–200 | INCLUDED_AS_MUST/CONTEXT | — | Keep; add ideal PD measure sentence. |
| Figure 3.1 PK drives PD; exposure, efficacy/potency, onset/intensity/duration | Figure | p.199 | INCLUDED_AS_CONTEXT | MISSING_AUTHOR_MSG minor | Add explicit view/reference in roadmap. |
| 3.2 Definitions | Heading | p.200–202 | INCLUDED_AS_CONTEXT | — | Sufficient. |
| Fig.3.2 full/partial agonist, antagonist, inverse agonist | Figure | p.201 | INCLUDED_AS_CONTEXT | — | Sufficient. |
| 3.3 Law of Mass Action | Heading | p.202–206 | INCLUDED_AS_MUST | — | Keep. |
| Eq.3:1–3:10 receptor binding to Emax | Equations | p.202–204 | INCLUDED_AS_MUST | — | Keep; remove non-source volume term unless tagged. |
| Eq.3:11–3:12 transduction/cascade | Equations | p.204–205 | INCLUDED_AS_CONTEXT | — | Keep, avoid overclaim. |
| Fig.3.3 drug-receptor equilibrium | Figure | p.202 | INCLUDED_AS_MUST | — | Useful view. |
| Fig.3.4 Kd vs EC50 stimulus-response | Figure | p.204 | INCLUDED_AS_MUST | — | Essential view. |
| Fig.3.5 cascade effect | Figure | p.205 | INCLUDED_AS_CONTEXT | — | Essential view. |
| Fig.3.6 spare receptors | Figure | p.206 | INCLUDED_AS_CONTEXT | — | Useful view. |
| 3.4 Receptor Binding Models | Heading | p.206–210 | INCLUDED_AS_CONTEXT | — | Sufficient. |
| 3.4.1 Saturation studies; Eq.3:13; Fig.3.7 | Heading/equation/figure | p.206–207 | INCLUDED_AS_CONTEXT | — | Sufficient. |
| 3.4.2 Displacement studies; Eq.3:14–3:17; Fig.3.8 | Heading/equations/figure | p.208–210 | INCLUDED_AS_CONTEXT | — | Sufficient. |
| Fig.3.9 one- vs two-site displacement | Figure | p.209 | OMITTED_JUSTIFIABLE | — | Not needed for core. |
| 3.5 Pharmacodynamic Models | Heading | p.210 | INCLUDED_AS_MUST | — | Keep. |
| 3.5.1 Background | Heading | p.210 | INCLUDED_AS_CONTEXT | — | Sufficient. |
| 3.5.2 Linear model Eq.3:22–3:23 Fig.3.10 | Heading/equation/figure | p.210–211 | INCLUDED_AS_CONTEXT | — | Sufficient. |
| 3.5.3 Log-linear model Eq.3:24–3:26 Fig.3.11 | Heading/equation/figure | p.211–212 | INCLUDED_AS_CONTEXT | — | Link to R&T Region 2 optional. |
| 3.5.4 Ordinary Emax Eq.3:27–3:31 Fig.3.12–3.14 | Heading/equations/figures | p.213–215 | INCLUDED_AS_MUST | — | Keep. |
| 3.5.5 Sigmoid Emax Eq.3:32–3:42 Fig.3.15–3.19 | Heading/equations/figures | p.216–220 | INCLUDED_AS_MUST | — | Keep; MUST_FIX n interpretation. |
| Table 3.1 target effect/concentration models | Table | p.221 | INCLUDED_AS_MUST | — | Keep; verify target concentration formula signs. |
| 3.5.6 Composite Emax Eq.3:43–3:47 Fig.3.20–3.22 | Heading/equations/figures | p.221–223 | INCLUDED_AS_CONTEXT | — | Sufficient. |
| 3.5.7 Multiple binding site Eq.3:48 Fig.3.23 | Heading/equation/figure | p.224 | INCLUDED_AS_CONTEXT | — | Sufficient. |
| 3.6 Interaction Models / 3.6.1 Competitive antagonism | Heading | p.224 | INCLUDED_AS_CONTEXT | — | Keep as boundary. |
| §3.6.2–§3.6.5 | Missing source pages | p.225–228 absent | OMITTED_JUSTIFIABLE | — | Do not infer. |
| 3.6.6 Kinetics of pharmacological responses Eq.3:56–3:71 Fig.3.27–3.31 | Heading/equations/figures | p.229–232 | INCLUDED_AS_CONTEXT/MUST | MISSING_BRIDGE minor | C5 should explicitly bridge non-steady-state response to AUEC. |
| 3.6.7 Area under response-time curve Eq.3:72–3:73 Fig.3.32 | Heading/equations/figure | p.233–234 | INCLUDED_AS_MUST | — | Keep. |
| Case Study PD3 objectives/rationale | Case study | p.732–733 | INCLUDED_AS_MUST | — | Keep. |
| PD3 Fig.3.1–3.2 graphical data/initial estimates | Figures | p.733–734 | INCLUDED_AS_MUST | — | Keep. |
| PD3 Table 3.1 F table | Table | p.734 | INCLUDED_AS_MUST | — | Keep only necessary F values. |
| PD3 Table 3.2 parameter estimates | Table | p.735 | INCLUDED_AS_MUST | — | Keep. |
| PD3 Fig.3.3 residuals | Figure | p.736 | INCLUDED_AS_MUST | — | Keep, soften exact sign pattern unless visually verified. |
| PD3 delta function Fig.3.4 | Equation/figure | p.736–737 | INCLUDED_AS_CONTEXT | — | Keep optional. |
| PD3 partial derivatives Fig.3.5 | Figure | p.737 | INCLUDED_AS_CONTEXT | — | Keep optional. |
| PD3 simulation error Fig.3.6–3.7 Table 3.3 | Figures/table | p.738–739 | INCLUDED_AS_MUST/CONTEXT | — | Keep with neutral language. |
| PD3 VIF Tables 3.4–3.5 | Tables | p.740–741 | INCLUDED_AS_MUST | — | Keep. |
| PD3 overall conclusions | Concluding message | p.741 | INCLUDED_AS_CONTEXT | — | Add to T3 wording if needed. |

### T5-B. R&T Structural Elements

| PDF Element | Type | PDF Location | Step 1 Status | Omission Verdict | Required Action |
|---|---|---|---|---|
| Chapter 8 Objectives | Objectives | p.233 | INCLUDED_AS_CONTEXT | MISSING_AUTHOR_MSG minor | Add 1–2 objectives in roadmap. |
| Opening: time always considered; reversible drugs, inactive metabolites assumption | Author message | p.233 | INCLUDED_AS_MUST | — | Keep. |
| Time delays between concentration and response | Heading | p.234 | INCLUDED_AS_MUST | — | Keep. |
| Detecting Time Delays | Heading | p.234–235 | INCLUDED_AS_MUST | — | Keep. |
| Fig.8-1 digoxin 1 mg IV | Figure | p.234 | INCLUDED_AS_MUST | — | Keep. |
| Fig.8-2 naproxen 500 mg oral hysteresis | Figure | p.235 | INCLUDED_AS_MUST | — | Keep. |
| Causes of Time Delay — Tissue Distribution | Heading | p.235–236 | INCLUDED_AS_MUST | — | Keep. |
| Causes — Pharmacodynamics | Heading | p.236–244 | INCLUDED_AS_MUST | — | Keep. |
| Fig.8-3 downstream compartments | Figure | p.236 | INCLUDED_AS_MUST | — | Keep. |
| Fig.8-4 tight binding/slow dissociation | Figure | p.238 | INCLUDED_AS_CONTEXT | — | Keep. |
| Fig.8-5 downstream peak delay | Figure | p.238 | INCLUDED_AS_CONTEXT | — | Useful but not essential. |
| Fig.8-6 propranolol direct link | Figure | p.239–240 | INCLUDED_AS_CONTEXT | — | Sufficient. |
| Fig.8-7 locomotor activity CNS response | Figure | p.240 | OMITTED_JUSTIFIABLE | — | Low priority. |
| Fig.8-8 ranitidine gastric pH | Figure | p.240 | OMITTED_JUSTIFIABLE | — | Low priority. |
| Systems in Flux | Heading | p.241 | INCLUDED_AS_MUST | — | Keep. |
| Fig.8-9 ibuprofen temperature | Figure | p.241 | INCLUDED_AS_MUST | — | Keep. |
| Fig.8-10 warfarin prothrombin complex | Figure | p.242 | INCLUDED_AS_MUST | — | Keep. |
| Fig.8-11 acenocoumarol/phenprocoumon PK vs PD rate-limiting | Figure | p.243 | INCLUDED_AS_MUST | — | Keep; correct phenprocoumon t1/2. |
| Fig.8-12 endogenous rhythms | Figure | p.244 | OMITTED_JUSTIFIABLE | — | Optional. |
| Effect Compartment heading | Heading | p.245 | INCLUDED_AS_MUST | — | Keep. |
| Fig.8-13 effect compartment concept | Figure | p.245 | INCLUDED_AS_MUST | — | Keep. |
| Fig.8-14 naproxen effect compartment | Figure | p.246 | INCLUDED_AS_MUST | — | Keep, no unsupported ke0. |
| Systems in Flux second heading | Heading | p.246 | INCLUDED_AS_MUST | — | Keep. |
| Fig.8-15 blocking warfarin dose | Figure | p.247 | INCLUDED_AS_MUST | — | Keep. |
| Fig.8-16 heptabarbital-warfarin | Figure | p.248 | INCLUDED_AS_CONTEXT | — | Useful optional. |
| Decline in intensity of effect Eq.8-3 | Concept/equation | p.249 | INCLUDED_AS_MUST | — | Keep. |
| Fig.8-17 effect decline regions | Figure | p.249 | INCLUDED_AS_MUST | — | Keep. |
| Fig.8-18 succinylcholine effect | Figure | p.250 | INCLUDED_AS_MUST | — | Keep. |
| Fig.8-19 minoxidil | Figure | p.250 | INCLUDED_AS_CONTEXT | — | Optional. |
| Fig.8-20 aspirin | Figure | p.251 | INCLUDED_AS_MUST | — | Keep source facts only. |
| Fig.8-21 omeprazole | Figure | p.252 | INCLUDED_AS_MUST | — | Keep source facts only. |
| Fig.8-22 paclitaxel | Figure | p.253 | INCLUDED_AS_CONTEXT | — | Keep optional. |
| Onset of Effect | Heading | p.254 | INCLUDED_AS_CONTEXT | — | Sufficient. |
| Duration of Effect Eq.8-11–8-12 | Heading/equations | p.254–255 | INCLUDED_AS_MUST | — | Keep. |
| Fig.8-23 duration vs dose | Figure | p.255 | INCLUDED_AS_MUST | — | Keep. |
| Fig.8-24 succinylcholine dose-duration | Figure | p.256 | INCLUDED_AS_MUST | — | Keep. |
| Methylprednisolone Fig.8-25–8-27 | Figures | p.257–258 | INCLUDED_AS_CONTEXT | — | Keep optional. |
| Rosuvastatin Fig.8-28–8-29 | Figures | p.258–259 | INCLUDED_AS_CONTEXT | — | Keep optional. |
| Key Relationships | Summary | p.260 | INCLUDED_AS_CONTEXT | — | Add minimal if missing. |
| Study Problems + Fig.8-30–8-33 + Tables 8-1–8-2 | Exercises | p.260–264 | OMITTED_JUSTIFIABLE | — | Not required in Step 1. |

---

## T6: Figure Inventory & Learning Value Audit

**Inspection note:** PDF pages were rendered to PNG and reviewed as contact sheets. Captions and surrounding text were cross-checked with extracted text. For all rows below, inspection method is marked `VISUAL_INSPECTED` unless otherwise specified.

### T6-A. G&W Figures and Tables

| Figure/Table | Page | Teaches | Value | View Instruction? | Redraw/New Schematic? | Inspection Method | Rationale |
|---|---:|---|---|---|---|---|---|
| Fig.3.1 | 199 | PK exposure drives PD, separating efficacy/potency and temporal response. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Chapter roadmap figure; redraw could clarify dual-axis PK/PD structure. |
| Fig.3.2 | 201 | Full/partial agonist, antagonist, inverse agonist action profiles. | USEFUL | YES | NO | VISUAL_INSPECTED | Helpful for definitions; not central to Emax/Hill derivation. |
| Fig.3.3 | 202 | Reversible drug-receptor equilibrium and transduction step. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Required for C1 law-of-mass-action derivation. |
| Fig.3.4 | 204 | Kd vs EC50 and left-shifted response due to transduction. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Core to Kd/EC50 confusion; redraw may make occupancy vs response clearer. |
| Fig.3.5 | 205 | Cascade amplification: small occupancy can generate large response. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Key support for EC50<Kd and signal amplification. |
| Fig.3.6 | 206 | Spare receptor concept with different occupancy requirements. | USEFUL | YES | YES | VISUAL_INSPECTED | Valuable but text can carry concept; redraw would be clearer. |
| Fig.3.7 | 207 | Total, specific, and non-specific binding. | USEFUL | NO | NO | VISUAL_INSPECTED | Binding context only. |
| Fig.3.8 | 208 | Displacement binding and IC50 in semi-log scale. | USEFUL | NO | NO | VISUAL_INSPECTED | Supports Cheng-Prusoff context. |
| Fig.3.9 | 209 | Single- vs two-site binding/displacement behavior. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Outside core session. |
| Fig.3.10 | 211 | Linear effect-concentration model and baseline/slope. | USEFUL | NO | NO | VISUAL_INSPECTED | Introductory approximation. |
| Fig.3.11 | 212 | Log-linear effect model and 20–80% linearity. | USEFUL | YES | NO | VISUAL_INSPECTED | Connects to R&T linear decline of graded response. |
| Fig.3.12 | 213 | Ordinary agonistic Emax model, EC50, Emax, baseline. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Core Emax visual. |
| Fig.3.13 | 214 | Antagonistic/inhibitory Emax model. | USEFUL | YES | NO | VISUAL_INSPECTED | Useful counterpart to agonist model. |
| Fig.3.14 | 215 | Comparison of Emax response with and without baseline. | USEFUL | NO | NO | VISUAL_INSPECTED | Clarifies E0/Rmax distinction. |
| Fig.3.15 | 216 | Sigmoid Emax curves for different n on linear/log scales. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Central Hill visual; redraw should annotate `n` as phenomenologic. |
| Fig.3.16 | 217 | Total vs unbound concentration response across species/fu. | USEFUL | YES | YES | VISUAL_INSPECTED | Good for unbound potency; could be simplified. |
| Fig.3.17 | 218 | Inhibitory sigmoid Imax with different n. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Directly supports PD3 Imax modeling. |
| Fig.3.18 | 218–219 | Graphical estimation of EC50, m, n from log concentration-response. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Important for initial estimates; redraw could improve readability. |
| Fig.3.19 | 220 | Ordinary vs sigmoid Imax fit to PD3-like data. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Key for model discrimination. |
| Table 3.1 | 221 | Target effect and target concentration model formulas. | USEFUL | YES | NO | VISUAL_INSPECTED | Useful for self-test/target concentration. |
| Fig.3.20 | 222 | Composite Emax simulated mixture dynamics. | USEFUL | NO | NO | VISUAL_INSPECTED | Context/limitation. |
| Fig.3.21 | 222 | Observed/model-predicted composite relationship. | USEFUL | NO | NO | VISUAL_INSPECTED | Context/limitation. |
| Fig.3.22 | 223 | U-shaped/bell-shaped composite model mechanisms. | USEFUL | NO | YES | VISUAL_INSPECTED | Useful as warning; redraw could simplify. |
| Fig.3.23 | 224 | Multiple binding site model with peak then decline. | USEFUL | NO | NO | VISUAL_INSPECTED | Context/limitation. |
| Fig.3.27 | 229 | Non-steady-state response and model components. | USEFUL | YES | YES | VISUAL_INSPECTED | Bridges to response kinetics; not fully used in Draft. |
| Fig.3.28 | 230 | Bolus vs infusion response-time patterns. | USEFUL | YES | YES | VISUAL_INSPECTED | Good bridge to dynamic response. |
| Fig.3.29 | 231 | Concentration and effect time course under Hill function. | USEFUL | YES | NO | VISUAL_INSPECTED | Supports C5. |
| Fig.3.30 | 232 | Semi-log response-time curves; decline behavior. | USEFUL | YES | NO | VISUAL_INSPECTED | Connects to effect duration/decline. |
| Fig.3.31 | 232 | Acute antipsychotic effect response-time modeling. | USEFUL | NO | NO | VISUAL_INSPECTED | Example; not core. |
| Fig.3.32 | 234 | AUEC and elimination rate constant relation. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Core AUEC concept; redraw recommended. |
| PD3 Fig.3.1 | 733 | Observed/model-predicted fall in blood pressure for 0–500 and 0–800 designs. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Direct model discrimination evidence. |
| PD3 Fig.3.2 | 734 | Graphical initial estimates for E0, Imax, IC50. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Supports numerical anchor. |
| PD3 Table 3.1 | 734 | F table values for model comparison. | USEFUL | NO | NO | VISUAL_INSPECTED | Needed only for audit of F-test. |
| PD3 Table 3.2 | 735 | Parameter estimates and CV% for ordinary vs sigmoid models/designs. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Main numerical anchor. |
| PD3 Fig.3.3 | 736 | Absolute residuals vs concentration for ordinary/sigmoid models. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Supports residual diagnosis. |
| PD3 Fig.3.4 | 737 | Delta function for optimal discrimination points. | USEFUL | NO | NO | VISUAL_INSPECTED | Useful for design insight. |
| PD3 Fig.3.5 | 737 | Predicted response and partial derivatives. | USEFUL | NO | NO | VISUAL_INSPECTED | Useful but advanced. |
| PD3 Fig.3.6 | 738 | Simulated data at different error levels. | USEFUL | NO | NO | VISUAL_INSPECTED | Supports error/precision message. |
| PD3 Table 3.3 | 738 | Parameter estimates/precision at error levels. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Supports `n` precision claim. |
| PD3 Fig.3.7 | 739 | Parameter precision vs simulated error. | USEFUL | YES | NO | VISUAL_INSPECTED | Good visual summary. |
| PD3 Table 3.4 | 741 | VIF comparison 0–500 vs 0–800 designs. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Supports design value of 800 µg/L. |
| PD3 Table 3.5 | 741 | VIF for predicted response at target concentrations. | USEFUL | NO | NO | VISUAL_INSPECTED | Supports final design conclusion. |

### T6-B. R&T Figures and Tables

| Figure/Table | Page | Teaches | Value | View Instruction? | Redraw/New Schematic? | Inspection Method | Rationale |
|---|---:|---|---|---|---|---|---|
| Fig.8-1 | 234 | Digoxin plasma concentration declines while cardiac effect rises initially. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Core time-delay example. |
| Fig.8-2 | 235 | Naproxen unbound concentration and pain relief form counterclockwise hysteresis. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Core hysteresis diagnostic. |
| Fig.8-3 | 236 | Site of action and downstream compartments create PD delays. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Core conceptual model; redraw would simplify. |
| Fig.8-4 | 238 | Tight binding/slow dissociation can make response decline slower than concentration. | USEFUL | YES | NO | VISUAL_INSPECTED | Supports PD-rate-limited concept. |
| Fig.8-5 | 238 | Downstream measurement sites peak later than upstream sites. | USEFUL | YES | YES | VISUAL_INSPECTED | Good for location/dynamics distinction. |
| Fig.8-6 | 239 | Direct link PK-PD model example with propranolol. | USEFUL | NO | NO | VISUAL_INSPECTED | Context for direct response. |
| Fig.8-7 | 240 | Locomotor activity as a delayed CNS response example. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Peripheral. |
| Fig.8-8 | 240 | Ranitidine concentration and gastric pH response. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Peripheral. |
| Fig.8-9 | 241 | Ibuprofen fever response with indirect dynamics. | USEFUL | YES | NO | VISUAL_INSPECTED | Helpful systems-in-flux example. |
| Fig.8-10 | 242 | Warfarin plasma concentration vs prothrombin complex activity. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Core indirect response example. |
| Fig.8-11 | 243 | Acenocoumarol vs phenprocoumon: PK vs PD rate-limited decline. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Central to C5 rate-limiting distinction. |
| Fig.8-12 | 244 | Endogenous rhythms/variability in systems. | USEFUL | NO | NO | VISUAL_INSPECTED | Optional context. |
| Fig.8-13 | 245 | Effect compartment concept. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Core C4 concept; redraw recommended. |
| Fig.8-14 | 246 | Naproxen effect compartment removes hysteresis. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Direct evidence for effect-site delay. |
| Fig.8-15 | 247 | Warfarin blocking dose estimates prothrombin turnover. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Supports indirect response calculations. |
| Fig.8-16 | 248 | Heptabarbital-warfarin interaction affects response without changing concentration-inhibition relation. | USEFUL | NO | NO | VISUAL_INSPECTED | Advanced example. |
| Fig.8-17 | 249 | Three response decline regions and quasi-linear decline between 80–20%. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Supports duration/decline logic. |
| Fig.8-18 | 250 | Succinylcholine effect after bolus and steep decline. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Important duration/rate-limited anchor. |
| Fig.8-19 | 250 | Minoxidil response example. | USEFUL | NO | NO | VISUAL_INSPECTED | Optional. |
| Fig.8-20 | 251 | Aspirin short plasma half-life but prolonged antiplatelet effect. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Core PD-rate-limited example. |
| Fig.8-21 | 252 | Omeprazole plasma profile vs prolonged gastric acid inhibition. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Core irreversible/receptor-resynthesis example. |
| Fig.8-22 | 253 | Paclitaxel plasma vs leukocyte time course. | USEFUL | YES | NO | VISUAL_INSPECTED | Strong PD-system example. |
| Fig.8-23 | 255 | Duration increases one half-life per dose doubling; log-dose linearity. | ESSENTIAL | YES | YES | VISUAL_INSPECTED | Core duration formula visual. |
| Fig.8-24 | 256 | Succinylcholine dose-duration data. | ESSENTIAL | YES | NO | VISUAL_INSPECTED | Verifies dose doubling rule. |
| Fig.8-25 | 257 | Methylprednisolone and prodrug plasma levels across doses. | USEFUL | NO | NO | VISUAL_INSPECTED | Supports PK linearity context. |
| Fig.8-26 | 257 | AUC linear with methylprednisolone dose. | USEFUL | YES | NO | VISUAL_INSPECTED | Supports “PK linearity”. |
| Fig.8-27 | 258 | Lymphocyte count response saturates across higher doses. | USEFUL | YES | NO | VISUAL_INSPECTED | Supports “PK linearity ≠ PD linearity”. |
| Fig.8-28 | 259 | Rosuvastatin concentration profiles by OATP1B1 genotype. | USEFUL | NO | NO | VISUAL_INSPECTED | Optional translational example. |
| Fig.8-29 | 259 | Rosuvastatin AUC vs cholesterol synthesis variability. | USEFUL | NO | NO | VISUAL_INSPECTED | Optional translational example. |
| Fig.8-30 | 261 | Study problem: plasma drug concentration-time profile. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Exercise only. |
| Fig.8-31 | 261 | Study problem: response-time profile. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Exercise only. |
| Table 8-1 | 262 | Study problem: percent reduction in exercise tachycardia with time after propranolol. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Exercise only. |
| Fig.8-32 | 262 | Study problem plot related to propranolol response. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Exercise only. |
| Table 8-2 | 263 | Study problem: plasma concentrations of drug/endogenous substance after bolus dose. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Exercise only. |
| Fig.8-33 | 263 | Study problem plot for endogenous substance. | SKIPPABLE | NO | NO | VISUAL_INSPECTED | Exercise only. |

---

## Patch Memo Independent Classification

| Patch memo item | Classification | Audit decision |
|---|---|---|
| Phase 1 is good but not final; Phase 2 required | MATCH | Adopt. |
| 5–100배/FIH not source-based | MATCH | Adopt as MUST_FIX. |
| Hill `n` overinterpreted | MATCH | Adopt as MUST_FIX. |
| C4 overloaded and contains implementation translation | MATCH | Adopt as SHOULD_FIX/MUST_TAG. |
| Naproxen `ke0≈0.5–1 hr^-1` needs confirmation | MATCH | Adopt as MUST_FIX/NOT_IN_SOURCE. |
| Aspirin 75 mg/7–10 days/surgery 7 days is external | MATCH | Adopt as MUST_FIX. |
| “계속 → HTML” workflow conflict | MATCH | Adopt; final guidance should be Phase 2/Phase 4A, not HTML direct. |
| PD3 numerical anchors generally strong | MATCH | Keep but correct tone/interpretation. |

---

## Final Action List for Phase 4A Patch

1. Replace all `5–100배`, `FIH`, `NDA 권장 용량`, `FDA Deficiency Letter`, `Clinical Hold` claims with `[실무 추론]` or delete.
2. Rewrite Hill `n` interpretation: **phenomenologic steepness/flexibility parameter; possible mechanism clue, not proof**.
3. Correct aspirin paragraph to **650 mg oral, plasma t1/2 15 min, antiplatelet activity several days** only; remove 75 mg/7–10 days/surgery 7 days unless explicitly marked external.
4. Correct omeprazole paragraph to **40 mg oral, t1/2 just <1 h, little plasma after 3 h, acid secretion returns over days/day 1–3**.
5. Remove or tag naproxen `ke0≈0.5–1 hr^-1` as `[확인 필요]`.
6. Split or internally label C4 as:
   - C4a Effect Compartment: distribution delay / hysteresis absorber.
   - C4b Systems-in-flux / Indirect Response: turnover-controlled response.
7. Add a short G&W p.200 design message: ideal PD measure + control + 2–4 dose levels with one reaching maximum.
8. Retain PD3 numerical anchor, but avoid implying that `n` proves mechanism.
9. Keep G&W §3.6.2–§3.6.5 as missing-source boundary. Do not reconstruct.
10. Before HTML compile, run a Phase 4C visual pedagogy pass using the ESSENTIAL figures listed in T6.

---

## Final Verdict

```text
GO        : Source Fidelity Audit completed; Draft v0 can proceed to patch/content lock.
NO-GO     : Direct HTML compile without Phase 4A source-fidelity patch.
REDO      : Full Phase 1 regeneration not required.
MUST_FIX  : Yes — unsupported quantitative/regulatory claims and Hill-n interpretation.
CONFIDENCE: High for major findings; moderate for fine-grained equation glyphs due PDF text extraction artifacts, mitigated by rendered page inspection.
```

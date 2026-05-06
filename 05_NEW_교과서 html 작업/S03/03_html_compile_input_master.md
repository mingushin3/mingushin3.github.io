# 03_HTML Compile Input Master

**Target output filename:** `03_html_compile_input_master.md`  
**Session:** 03 — 경구(혈관외) PK: F · ka · tmax · 흡수  
**Assembly phase:** Phase 4D — Learner-Complete + Mastery-Enriched + HTML-Ready Master Assembler  
**Assembly mode:** PATCH MODE  
**HTML status:** Ready for Phase 5 input; no HTML generated in this file.

## Phase 4D Certification

| Certificate | Status | Basis |
|---|---|---|
| Learner-Standalone Certificate | PASS | PART A is independently readable and contains no compiler/audit/process text. |
| Zero-Omission Certificate | PASS | High-impact Scope/Audit/Crucible/PDF-required items are present, repaired in Content Lock v2, or justifiably omitted. |
| Mastery-Uplift Certificate | PASS | PART A contains five bounded, source-labeled augmentation notes without broad rewrite. |
| Source-Boundary Certificate | PASS | All augmentations are labeled by source status and introduce no new page tags, unsupported numbers, or new named examples. |
| HTML-Readiness Certificate | PASS | PART B contains Phase 5 rendering instructions, marker mapping, page-tag rules, guardrails, and splice verification. |


## Assembly Mode

**PATCH MODE.** `03_Content Lock v2.1.md` is a figure marker patch / insertion map rather than a full marked body. The learner-facing scientific body was therefore constructed from the Content Lock v2 scientific body, with approved Figure Strategy markers spliced at exact verified anchors. Process logs, adjudication tables, and compiler instructions are kept out of PART A and placed in PART B.

## Input Manifest

| File | Role | Authority level | Used for | Notes |
|---|---|---|---|---|
| `03_scope_lock(4).md` | scope boundary | A0 | source range, learner, mode, image rights, chapter role | Controls allowed scope. |
| `03_G_경구 PK F·Ka·Tmax·흡수(5).pdf` | PDF verification source | A1 | G pp.28–47, PK2 pp.476–482, PK3 pp.483–486 | Used for high-impact page/figure/equation verification only. |
| `03_T_경구 PK F·Ka·Tmax·흡수(5).pdf` | PDF verification source | A1 | T Ch.6, Ch.7 context, Appendix F | Used for Eq.6-3, F/urine, BE, Appendix F verification. |
| `03_Audit_Report_v1(4).md` | audit guardrail | A2 | MUST_FIX/SHOULD_FIX corrections, forbidden regressions | Not used as learner prose source. |
| `03_Content Lock v2(4).md` | canonical body | A3 | learner scientific body | Process/adjudication tables are moved to PART B or excluded from PART A. |
| `03_Content Lock v2.1.md` | figure insertion source | A4 | PATCH MODE marker blocks and insertion map | Four KEEP markers were spliced. |
| `03_crucible_report_v1(2).md` | crucible guardrail | A5 | bounded mastery insights | Used only through labeled augmentation gate. |
| `03_step1_draft_v0(3).md` | deprecated source | A6 | regression check only | Not copied as raw learner text. |
| `S03_phase1_patch memo(3).md` | locked reference | A6 | workflow sanity check and regression awareness | Confirms Phase 1 was not HTML-ready. |
| `붙여넣은 마크다운(2)(52).md` | compiler instruction | A7 | Phase 5 rendering contract | Included/summarized in PART B. |
| `붙여넣은 텍스트 (1)(78).txt` | Phase 4D assembler instruction | process instruction | output structure and gates | Adapted to filename `03_html_compile_input_master.md`. |


## PART A — Learner-Facing Complete Handout

## Learner Navigation Aid

**How to use this handout:** Read §1 once for the spine, then study §2 Card 1–5 in order. Use §5 to eliminate common confusions, §7 for active recall, and §8 to reconnect the chapter to later PopPK absorption modeling.

**Learning route:** `C(t) Master Equation → tmax/Cmax → F → V/F + flip-flop → ka,app vs ka,true → confusion pairs → self-test → meta-frame`.

**Before you start:** You should already be comfortable with IV bolus 1-compartment PK, CL, V, half-life, exponential decay, and AUC.

**After you finish:** You should be able to state what oral-only data can identify (`V/F`, `CL/F`, apparent `ka`, terminal slope ambiguity) and what it cannot identify without extra evidence.

**Figure-rights note:** Textbook figures are not reproduced. `FIGURE_POINTER` blocks tell the HTML compiler to create text-only textbook reference callouts; `FIGURE_SCHEMATIC` is a redraw brief, not copyrighted image reproduction.

---


# 03_Content Lock v2 — 경구(혈관외) PK: F · ka · tmax · 흡수

**Source A (G):** Gabrielsson & Weiner 5e, Ch.2 §§2.2.4–2.2.12 (pp.28–47), PK2 (pp.476–482), PK3 (pp.483–486)  
**Source B (T):** Rowland & Tozer 5e, Ch.6 (pp.169–195), Ch.7 (pp.197–220; context only), Appendix F (pp.781–784)  
**Mode:** B-Standard  
**Symbol convention:** **ka** = absorption rate constant, **kel** = elimination rate constant, **V/F** = apparent volume after oral/extravascular data, **CL/F** = apparent oral clearance.

---

## 0. Updated Curation Map

### MUST — 최종 체화 카드 5개

| # | Concept | 핵심 수식 / 출처 | 최종 판정 |
|---|---|---|---|
| 1 | **C(t) Master Equation** | G Eq.2:32–2:35 [G p.30]; T mass-balance Eq.6-3 [T p.172] + integrated solution Eq.F-1 [T p.782] | MUST. 모든 tmax, Cmax, AUC, lag-time, flip-flop 논의의 출발점. |
| 2 | **tmax / Cmax** | G Eq.2:49–2:55 [G pp.34–35]; T tmax Eq.F-6 [T p.783] | MUST. “흡수속도 = 소실속도”의 평형 조건. |
| 3 | **Bioavailability F** | G Eq.2:71–2:74 [G pp.41–42]; T Eq.6-9–6-17 [T pp.183–186]; urine data Eq.6-18–6-21 [T pp.187–188] | MUST. rate(ka)와 extent(F)를 분리하는 핵심 축. |
| 4 | **APEX: V/F 식별불가능성 + Flip-flop** | V/F [G p.32; T p.185]; flip-flop [G Fig.2.17, p.30; T Case C, pp.175–176] | MUST. 경구 단독 데이터 해석의 구조적 한계. |
| 5 | **ka,app vs ka,true** | apparent GI loss [G pp.40–41]; F = ka,true/(ka,true+kd), Eq.2:70 [G p.41] | MUST. 적합된 ka가 “흡수”가 아니라 “장관 소실”일 수 있음을 고정. |

### CONTEXT — 본문 안에 압축 흡수

| 항목 | 위치 | 처리 |
|---|---|---|
| Lag time | Card 1, Card 2 | Eq.2:39–2:42 [G pp.32–33]를 1차 흡수식의 시간 이동으로 처리. |
| Method of Residuals | Card 2 | 초기 추정 알고리즘으로 압축; Appendix F [T pp.781–783]와 연결. |
| Zero-order input | Card 1, §5 | Eq.2:66–2:67 [G p.38], Fig.6-2 [T p.171], PK3 [G pp.483–486]로 “대체 입력 함수” 수준 유지. |
| Multiple dosing / accumulation | §8 | R = 1/(1−e^(−kel·τ)), Eq.2:78 [G p.45]는 다음 세션 dependency로만 배치. |
| Multiple absorption sites | Card 5, §8 | Eq.2:80–2:82 [G pp.46–47]를 다중 peak / site heterogeneity의 경고로 1문장 처리. |
| Ch.7 absorption physiology / BCS | §8 | BCS·gastric emptying·first-pass는 흡수 변동성의 생리학적 배경으로만 압축 [T pp.197–220]. |
| Pidgeon-Pitlick / Vaughan | 제외 | B-Standard 10분 handout 기준에서는 과도한 수식 깊이. |
| Local topical BE / microdialysis | 제외 | 본 세션의 F·ka·tmax core에서 벗어남. |

---

## §1. SESSION HEADER & ROADMAP

**Title:** 경구 및 혈관외 투여의 PK — F · ka · tmax 그리고 흡수 단계가 만드는 모든 것

<!-- MASTER LENS -->
### Big Idea

<!-- ANNOTATION -->
IV bolus는 투여 직후 전신 순환에 약물이 들어와 **초기 농도 C0**를 만든다. 반면 경구/혈관외 투여는 **초기 농도 0에서 흡수와 소실이 경쟁하며 만들어지는 차이지수 곡선(← 두 지수함수의 차이로 생긴 곡선)**이다. 따라서 이 곡선에서는 F와 V가 `V/F`로 묶이고, ka와 kel은 terminal slope 해석에서 서로 뒤바뀔 수 있다. 이 때문에 경구 단독 데이터는 “잘 맞는 모델”과 “진짜 생리학”을 자동으로 구분해주지 않는다.

### 이 세션의 한 줄 항법도

```
C(t) Master Equation
  → tmax/Cmax: 흡수속도 = 소실속도
  → F: 흡수의 extent는 AUC로 본다
  → V/F + flip-flop: 경구 단독 데이터의 식별 한계
  → ka,app vs ka,true: 적합된 ka가 실제 흡수인가, 장관 소실인가
```

### 선행·후속 위치

**선행:** IV bolus 1구획 PK(CL, V, t1/2, AUC), 1차 ODE, 자연로그/지수함수, AUC 사다리꼴법.  
**직후:** multiple dosing, accumulation factor, two-compartment oral model, transit/Erlang/Weibull input, modified-release 및 BE 평가.  
**실무 연결:** NONMEM ADVAN2/ADVAN4, oral PopPK parameter reporting, food effect, formulation effect, flip-flop 검증.

<!-- RECAP -->
**§1 Recap:** 이 세션의 목표는 식을 외우는 것이 아니라, oral curve에서 “무엇이 실제로 식별되는가”를 자동으로 의심하는 눈을 만드는 것이다.

---

## §2. CONCEPT ANATOMY CARDS

---

### Card 1. C(t) Master Equation — 경구 PK의 모든 것이 시작되는 한 줄

<!-- MASTER LENS -->
**거장의 시각:** 경구 1구획 모델의 핵심은 농도 곡선을 “두 지수 함수의 차이”로 보는 것이다. 상승부는 흡수 과정이 아직 남아 있다는 신호이고, 하강부는 반드시 소실만의 신호가 아니다.

**체화 직관:** `ka − kel`은 단순한 분모가 아니라 두 지수 과정이 시간축에서 얼마나 분리되어 보이는지를 결정한다. `ka ≈ kel`이면 두 과정은 그래프상 거의 분리되지 않아 한계식으로 수렴하고, `ka < kel`이면 혈장에 들어온 약물은 빠르게 제거되지만 관찰 terminal decline은 남아 있는 흡수 과정에 의해 느리게 보일 수 있다.

**A. Formal Definition**

<!-- ANNOTATION -->
1구획 모델, 1차 흡수, 1차 소실, linear PK(← dose 비례성이 유지되는 PK)를 가정한 extravascular concentration-time equation이다. 흡수 부위의 약물은 시간에 따라 1차로 줄어들고, 그중 F fraction이 전신 순환에 도달한다 [G p.30; T pp.171–172].

**B. Model structure**

흡수 부위:

$$
\frac{dA_g}{dt} = -k_a A_g
$$

혈장/central compartment:

$$
\frac{dC}{dt} = \frac{k_a F D_{po} e^{-k_a t}}{V} - k_{el} C
$$

`[Source: G Eq.2:32–2:34, p.30; T Eq.6-2–6-3, pp.171–172]`

적분 해:

$$
\boxed{C(t)=\frac{k_a F D_{po}}{V(k_a-k_{el})}\left(e^{-k_{el}t}-e^{-k_a t}\right)}
$$

`[Source: G Eq.2:35, p.30; T Appendix F Eq.F-1, p.782]`

<!-- ANNOTATION -->
**C. Lag-time(← 흡수 시작 전 지연시간) extension**

Lag-time이 있으면 투여 시각이 아니라 실제 흡수 시작 시점 이후의 시간만 식에 들어간다.

$$
C(t)=0 \quad (t<t_{lag})
$$

$$
C(t)=\frac{k_a F D_{po}}{V(k_a-k_{el})}\left(e^{-k_{el}(t-t_{lag})}-e^{-k_a(t-t_{lag})}\right) \quad (t\ge t_{lag})
$$

`[Source: G Eq.2:39–2:42, pp.32–33]`

**D. Zero-order input as a different input function**

0차 흡수는 central elimination 구조는 그대로 두고 input function만 바꾼 경우다. Absorption이 지속되는 동안에는 input이 거의 일정하고, 입력이 끝난 뒤에는 washout만 남는다 [G Eq.2:66–2:67, p.38; T Fig.6-2, p.171]. PK3에서 zero-order model의 AIC가 first-order보다 좋았지만, 교재는 이것이 물리적으로 “진짜 zero-order absorption”을 증명하는 것은 아니라고 경고한다. 여러 dose, 반복투여, IV 비교가 있어야 mechanism 해석이 가능하다 [G pp.483–486].

<!-- TRENCH -->
**Trench tip [교과서 외 해석]:** NONMEM ADVAN2 oral model의 KA initial은 큰 값과 작은 값을 모두 시도한다. 서로 다른 initial이 서로 다른 해 또는 비슷한 OFV로 수렴하면 flip-flop 또는 practical identifiability 문제를 의심한다.

<!-- ANCHOR -->
*차이지수 곡선이 만들어졌다면, 다음 질문은 그 곡선이 언제 가장 높아지는가다.*

<!-- RECAP -->
**Card 1 Recap:** Oral C(t)는 “흡수 지수 − 소실 지수”이며, F와 V는 진폭을, ka와 kel은 모양과 terminal slope 해석을 지배한다.

---

> **Mastery Note — [CRUCIBLE_DERIVED]**  
> `ka−kel`을 분모로만 보지 말고, 두 1차 과정이 관찰 곡선에서 얼마나 분리되어 보이는지를 나타내는 신호로 읽어라. `ka≈kel`이면 공식 계산보다 먼저 parameter separation 자체가 약해졌는지 점검해야 한다.

<!-- FIGURE_SCHEMATIC -->
Title: 1차 extravascular input의 compartment topology
Mode: R
Visual objective: 5초 안에 Dpo → gut compartment → F-scaled input → central compartment → elimination 흐름을 보게 한다.
Core message: Master Equation은 두 지수의 차이로 보이지만, 그 뿌리는 gut loss와 central elimination이 직렬로 연결된 1차 ODE 구조다.
Elements to include: Oral dose Dpo; gut/absorption site Ag; first-order gut loss arrow labeled ka·Ag; systemic input branch labeled F·ka·Ag; optional non-systemic loss branch labeled (1−F) or gut loss/degradation; central compartment C or A/V; elimination arrow labeled kel·C or CL·C; output label C(t) = difference of exponentials.
Elements to exclude: textbook bucket/reservoir drawing style; empirical concentration-time curves; zero-order input; multiple absorption sites; transit compartments; numerical values.
Suggested rendering: Mermaid
Caption: 1차 흡수 oral model은 gut에서 사라지는 과정과 central compartment에서 제거되는 과정이 직렬로 결합된 구조다.
Alt text: Oral dose가 gut compartment를 거쳐 F-scaled input으로 central compartment에 들어가고, central compartment에서 elimination되는 흐름도.
Source relation: Redrawn from textbook concept
<!-- /FIGURE_SCHEMATIC -->

### Card 2. tmax / Cmax — 흡수속도와 소실속도가 같아지는 순간

<!-- MASTER LENS -->
**거장의 시각:** tmax는 “가장 많이 흡수된 시간”이 아니라, **순유입이 0이 되는 시간**이다. 즉 rate of absorption과 rate of elimination이 같아지는 순간이다 [T p.173; G pp.34–35].

**A. Derivation**

Master equation을 미분하고 `dC/dt = 0`으로 두면:

$$
\frac{dC}{dt}=\frac{k_a F D_{po}}{V(k_a-k_{el})}\left(-k_{el}e^{-k_{el}t}+k_a e^{-k_a t}\right)=0
$$

따라서:

$$
\boxed{t_{max}=\frac{\ln(k_a/k_{el})}{k_a-k_{el}}}
$$

`[Source: G Eq.2:49–2:52, pp.34–35; T Eq.F-6, p.783]`

`ka >> kel`이면 다음 근사가 가능하다.

$$
C_{max}\approx \frac{F D_{po}}{V}e^{-k_{el}t_{max}}
$$

`[Source: G Eq.2:53, p.35]`

Lag-time이 있으면 관찰 tmax는 `tlag`만큼 뒤로 이동한다 [G Eq.2:54–2:55, p.35].

**B. 왜 F와 V가 tmax 식에서 사라지는가**

F, dose, V는 linear system에서 곡선의 높이를 위아래로 scale한다. 그러나 `dC/dt = 0`은 “높이”가 아니라 “기울기가 0이 되는 시간 위치”를 찾는 조건이다. 따라서 곡선 전체가 위아래로 커지거나 작아져도 tmax의 시간 위치는 바뀌지 않는다. 그래서 linear 1구획 oral PK에서는 dose나 F가 바뀌면 Cmax와 AUC는 바뀌지만 tmax는 바뀌지 않는다 [T Fig.6-5, p.174].

**C. Method of Residuals**

Terminal straight line에서 `kel`을 먼저 추정한다. 그 다음 back-extrapolated line에서 관찰 농도를 빼 residual line을 만들면, 이 residual slope가 `−ka`가 된다. 두 직선의 교점은 lag-time 추정에 사용될 수 있다 [G pp.31–33; T Appendix F pp.781–783]. 단, 이 방법은 terminal slope가 정말 elimination을 반영한다는 전제를 둔다. 따라서 flip-flop 상황에서는 위험하다.

<!-- TRENCH -->
**Trench tip [교과서 외 해석]:** 수기 residual method에서 terminal point 선택은 “눈대중”이 아니라 최소 3개 이상의 terminal points, 충분한 log-linear fit, Cmax 이후 충분히 늦은 시점이라는 기준으로 고정해야 한다. 기준을 만족하지 않으면 ka와 kel 초기값이 서로 오염된다.

**D. Limiting case: ka = kel**

`ka`와 `kel`이 거의 같으면 두 지수 함수는 분리되지 않고 다음 한계식으로 수렴한다.

$$
C(t)=\frac{k' F D_{po}}{V}t e^{-k't}
$$

`[Source: G Eq.2:58, p.37]`

<!-- ANCHOR -->
*tmax와 Cmax는 rate의 문제지만, 전체 노출량 AUC는 extent의 문제다. 이 지점에서 F가 등장한다.*

<!-- RECAP -->
**Card 2 Recap:** tmax는 rate balance의 시점이며, linear 조건에서는 F·dose·V가 아니라 ka와 kel의 상대적 크기로 정해진다.

---

> **Mastery Note — [CRUCIBLE_DERIVED]**  
> linear 1구획 oral PK에서 tmax가 F·dose·V에 의존하지 않는 이유는 곡선을 위아래로 늘려도 기울기 0의 위치는 움직이지 않기 때문이다. 따라서 관찰 tmax가 dose나 조건에 따라 체계적으로 움직이면, 단순 scale 변화가 아니라 rate process나 비선형성 가능성을 먼저 의심한다.

### Card 3. Bioavailability F — 흡수의 정도(extent)를 AUC로 읽는다

<!-- MASTER LENS -->
**거장의 시각:** ka는 “얼마나 빨리 들어오는가”를, F는 “얼마나 많이 전신 순환에 도달했는가”를 묻는 값이다. 두 개념을 섞으면 food effect, BE, formulation effect 해석이 모두 흐려진다.

**A. Absolute bioavailability**

<!-- ANNOTATION -->
동일 약물의 IV reference가 있을 때, plasma AUC 기반 bioavailability F(← 전신 순환 도달 분율)는 다음과 같이 계산한다.

$$
\boxed{F=\frac{AUC_{po}}{AUC_{iv}}\cdot\frac{D_{iv}}{D_{po}}}
$$

`[Source: G Eq.2:74, p.42; T Eq.6-11, p.183]`

이 식의 전제는 clearance가 두 투여 사이에서 동일하다는 것이다 [T p.183]. R&T의 parameter-estimation 예시는 i.m. dose의 F를 97%, oral solution의 F를 46%로 계산하여 route별 extent 차이를 보여준다 [T Table 6-1 / Fig.6-14, pp.183–184].

**B. Relative bioavailability**

두 extravascular formulation A/B를 비교할 때:

$$
\boxed{F_{rel}=\frac{AUC_B}{AUC_A}\cdot\frac{D_A}{D_B}}
$$

`[Source: T Eq.6-15, p.185]`

Relative F는 IV reference 없이도 두 제품의 systemic delivery 차이를 비교할 수 있다 [T pp.183–185].

**C. Urine data caveat**

Plasma AUC만이 유일한 경로는 아니다. R&T는 urinary excretion data로도 bioavailability, relative bioavailability, renal clearance를 추정할 수 있음을 제시한다. 단, 이 해석은 fraction excreted unchanged와 renal handling이 비교 조건에서 일정하다는 전제를 요구한다 [T Eq.6-18–6-21, pp.187–188].

**D. Mechanistic F**

<!-- ANNOTATION -->
생리학적으로 F는 gut lumen에서의 fraction absorbed, intestinal first-pass(← 장 통과 중 대사/손실), hepatic first-pass(← 간 통과 중 대사/손실)가 곱해진 결과로 이해할 수 있다.

$$
F \approx F_F \cdot F_G \cdot F_H
$$

`[Source: T Ch.7 context, pp.197–220]`

이 식은 본 세션에서 full physiology로 확장하지 않고, F가 단순 “용해되어 들어온 양”이 아니라 장관·장벽·간을 통과한 결과임을 상기시키는 용도로만 사용한다.

**E. BE context**

R&T는 bioequivalence에서 test/reference ratio의 90% CI와 0.80–1.25 기준을 설명한다 [T Fig.6-13, p.183]. 본 세션에서는 “Frel만 같아도 충분한가?”가 핵심 질문이다. Frel이 같아 AUC가 유사해도 ka가 달라 Cmax와 tmax가 달라질 수 있으므로, extent와 rate는 함께 읽어야 한다.

<!-- ANCHOR -->
<!-- ANNOTATION -->
*F는 AUC로 읽을 수 있지만, 경구 단독에서는 F와 V가 분리되지 않는다. 즉 AUC가 달라졌을 때 그 원인이 F 변화인지 CL 변화인지, 또는 농도 진폭이 V 때문인지 F 때문인지 단독 자료만으로는 나눌 수 없다. 이것이 Apex 카드의 출발점이다.*

<!-- RECAP -->
**Card 3 Recap:** F는 흡수의 extent이고, ka는 rate다. AUC는 F·Dose/CL을 읽지만, 경구 단독에서는 CL이 아니라 CL/F가 추정된다.

---

> **Practice Lens — [AUDIT_DERIVED]**  
> F와 ka를 분리해서 보고하면 food/formulation effect 문장이 안전해진다. AUC 변화는 extent 또는 clearance/F 문제를, Cmax·tmax 변화는 rate와 input function 문제를 우선 제기하지만, 경구 단독 자료만으로 원인을 확정하지 않는다.

### Card 4. APEX — V/F 식별불가능성 + Flip-flop 동정

<!-- MASTER LENS -->
<!-- ANNOTATION -->
**거장의 시각:** 경구 단독 모델에서 좋은 OFV와 작은 RSE는 “모델이 데이터를 잘 설명한다”는 뜻이지, V와 F가 원리적으로 분리되었다는 뜻이 아니다. Numerical identifiability와 structural identifiability(← 원리적으로 분리 추정 가능한지)는 다르다.

**A. V/F structural identifiability**

Master equation에서 F와 V는 항상 `F/V` 형태로 함께 나타난다.

$$
C(t)=\frac{k_a F D_{po}}{V(k_a-k_{el})}\left(e^{-k_{el}t}-e^{-k_a t}\right)
$$

따라서 경구 단독 데이터는 `V`와 `F`를 분리하지 못하고 `V/F`만 추정한다. 마찬가지로 clearance는 `CL/F`로 보고해야 한다 [G p.32; T p.185].

정확한 AUC 관계는 다음이다.

$$
\boxed{AUC=\frac{F\cdot Dose}{CL}=\frac{Dose}{CL/F}}
$$

`Dose/(CL/F)`는 대수적으로 `F·Dose/CL`과 같다. 그러나 AUC만 보고서는 변화의 원인이 F인지 CL인지 분리할 수 없다.

**B. Flip-flop practical identifiability**

일반적으로 `ka > kel`이면 oral terminal slope는 elimination을 반영한다. 그러나 `ka < kel`이면 남아 있는 absorption process가 더 느린 과정이 되므로, 관찰 terminal slope는 absorption을 반영할 수 있다. 이때 terminal half-life를 elimination half-life로 읽으면 소실을 잘못 해석하게 된다 [G Fig.2.17, p.30; T Case C, pp.175–176].

**핵심 경고:** “rising limb = absorption phase, declining limb = elimination phase”라는 말은 flip-flop에서는 틀릴 수 있다 [G pp.29–30; T pp.173–176].

**C. Case anchors**

- **Fluticasone propionate:** median tmax는 90 min이고 Cmax는 30–90 min에 나타나지만, absorption half-life는 3.8–4 h로 해석된다. early tmax가 빠른 absorption을 증명하지 않는다 [T Fig.6-7, p.177].
- **Theophylline:** food/water는 absorption kinetics를 바꾸지만 terminal half-life는 약 6.3 h로 유지되어 absorption 변화와 disposition 변화를 구분하는 예시가 된다 [T Fig.6-8, p.178].
- **Penicillin G:** sparingly soluble i.m. formulation은 absorption이 rate-limiting이 될 수 있음을 보여준다 [T Fig.6-9, p.178].
- **PK2:** lag-time model은 `Ka = 0.043 min⁻¹`, `K = 0.0088 min⁻¹`, `V/F = 32 L`, `tlag = 16 min`을 제시한다 [G p.480]. 같은 case에서 `F = 82%`와 `true V = 20 L` 문구는 `32×0.82≈26 L`과 산술상 충돌하므로, 본 handout에서는 “원문 수치 충돌 [확인 필요]”로 유지하고 계산값을 source-confirmed value로 확정하지 않는다 [G p.480].
- **PK2 Solution III:** reversed initial estimate는 다른 `ka/kel/V/F` 해로 수렴할 수 있음을 보여준다. 단, OCR/unit 표기에는 `[확인 필요]` 플래그를 유지한다 [G pp.481–482].
- **PK3:** first-order model은 `Ka≈Ke`와 큰 CV/RSE 문제를 보이고, zero-order model은 AIC가 낮다(85.2 vs 76.2). 그러나 better fit은 true zero-order absorption의 증명이 아니다 [G Table 3.1, p.486].

**D. NONMEM reporting implication**

경구 단독 PopPK에서는 F를 1로 fix하고 `V/F`, `CL/F`로 보고하는 것이 구조적으로 정직하다. `F1`을 estimate하거나 임의 값으로 fix한 뒤 V와 CL을 absolute value처럼 보고하면, prior assumption이 estimated parameter처럼 보일 위험이 있다. `[교과서 외 해석 — NONMEM reporting practice]`

<!-- TRENCH -->
**Trench signatures [교과서 외 해석]:**  
1. **Twin Suppression Pattern:** ka와 kel의 두 해가 모두 plausible하여 ETA(KA)와 ETA(KEL)가 강하게 보상되는 패턴.  
2. **V/F Drift:** 같은 covariate가 `V/F`와 `CL/F`에 비례적으로 나타나면 F-driven 변화 가능성을 의심한다.  
3. **Phantom Volume Drift:** `V/F` 변화를 V 변화로 보고하는 오류. 핵심 식은 `AUC = F·Dose/CL = Dose/(CL/F)`이다.

<!-- ANCHOR -->
*V/F 문제는 “얼마나 들어왔는가”와 “어디에 분포했는가”의 분리 문제다. 다음 카드는 ka 자체도 겉보기 값일 수 있음을 보여준다.*

<!-- RECAP -->
**Card 4 Recap:** 경구 단독 데이터는 V와 F를 분리하지 못하고, flip-flop에서는 terminal slope도 kel로 확정하지 못한다. 좋은 fit은 진짜 parameter의 증거가 아니다.

---

> **Practice Lens — [CRUCIBLE_DERIVED]**  
> 작은 RSE와 좋은 적합도는 주어진 model parameterization 안에서의 정밀도일 수 있다. 경구 단독 모델에서는 “정밀하게 추정된 V/F”와 “원리적으로 분리된 V”를 구분해 보고해야 한다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.30, Fig.2.17
Why this matters: IV와 PO terminal slope가 parallel이면 oral terminal phase를 elimination으로 해석할 수 있지만, non-parallel이면 absorption-limited terminal decline이 될 수 있다. 이 figure는 terminal slope label이 kel에서 ka로 바뀌는 지점을 직접 보여준다.
When to look: Card 4를 읽은 직후.
Learner instruction: 왼쪽 panel에서는 IV와 PO terminal slope가 어떻게 같은 방향으로 떨어지는지 확인하라. 오른쪽 panel에서는 PO terminal slope가 IV slope와 달라질 때, terminal slope label이 kel에서 ka로 바뀔 수 있음을 확인하라.
<!-- /FIGURE_POINTER -->

### Card 5. ka,app vs ka,true — ka가 측정하는 것은 무엇인가

<!-- MASTER LENS -->
<!-- ANNOTATION -->
**거장의 시각:** 모델 output의 ka를 “흡수속도상수”라고 부르더라도, 그 값은 apparent(← 모델에서 보이는 겉보기) parameter일 수 있다. 즉 실제 plasma appearance만이 아니라 gut compartment에서 사라지는 모든 경로를 반영할 수 있다.

**A. Apparent GI loss**

장관에서 약물이 사라지는 경로가 실제 흡수(`ka,true`)와 장내 분해/손실(`kd`)로 나뉘면, 관찰되는 apparent first-order loss는 다음과 같다.

$$
\boxed{k_{a,app}=k_{a,true}+k_d}
$$

`[Source: G Fig.2.24 and text, pp.40–41]`

전신 순환 도달 fraction은 다음과 같이 표현된다.

$$
\boxed{F=\frac{k_{a,true}}{k_{a,true}+k_d}}
$$

`[Source: G Eq.2:70, p.41]`

**B. Interpretation**

적합된 `ka`가 커졌다는 것은 곧바로 “흡수가 빨라졌다”를 뜻하지 않는다. “gut compartment에서 더 빨리 사라졌다”는 뜻일 수도 있다. AUC가 같이 변하지 않으면 onset/rate 변화일 가능성이 크고, AUC도 변하면 extent 변화가 동반된 것이다 [G pp.40–41].

**C. Multiple absorption sites**

흡수 부위가 여러 개이면 concentration-time curve는 다중 peak 또는 비정형 상승부를 보일 수 있다. G는 buccal + GI 같은 multiple absorption site 구조를 Eq.2:80–2:82로 제시한다 [G pp.46–47]. 이 경우 단일 ka는 여러 input process를 하나로 눌러 담은 summary parameter로 읽어야 한다.

<!-- TRENCH -->
**Trench tip [교과서 외 해석]:** food effect 보고서에서 “ka 감소 = 흡수 저하”라고 쓰지 않는다. `Frel(AUC ratio)`을 함께 보고하여, AUC 변화 없이 ka만 바뀌면 onset/rate 변화, AUC도 바뀌면 extent 변화로 분리한다.

<!-- RECAP -->
**Card 5 Recap:** ka는 항상 “진짜 흡수속도”가 아니다. 적합된 ka의 생리학적 의미는 모델 구조와 외부 evidence가 결정한다.

---

> **Failure Mode — [TEXTBOOK_DERIVED]**  
> fitted ka를 true absorption으로 단정하면 장관 분해·fecal loss·site heterogeneity를 모두 흡수속도 변화로 오해한다. 이 카드는 ka를 생리학적 label이 아니라 model-visible disappearance signal로 읽게 만드는 안전장치다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.40, Fig.2.24
Why this matters: ka,app는 true absorption만이 아니라 gut degradation/loss를 포함할 수 있다. 이 figure는 fitted ka를 생리학적 true absorption으로 바로 읽으면 안 되는 이유를 compartment 구조로 분리한다.
When to look: Card 5를 읽은 직후.
Learner instruction: gut compartment에서 사라지는 흐름과 systemic circulation에 실제로 들어가는 흐름을 분리해서 보라. fitted ka가 왜 곧바로 ka,true가 아닌지 확인하라.
<!-- /FIGURE_POINTER -->

## §5. CONFUSION PAIR DISSECTION

<!-- CONFUSION -->
### 혼동쌍 1. ka vs kel under flip-flop — Critical Blow

| 질문 | 올바른 판단 |
|---|---|
| Terminal slope는 항상 kel인가? | 아니다. `ka < kel`이면 terminal slope는 absorption을 반영할 수 있다 [G p.30; T pp.175–176]. |
| Oral curve만 보고 kel을 확정할 수 있는가? | 일반적으로 어렵다. IV 또는 route/formulation comparison이 필요하다. |
| Early tmax는 빠른 absorption의 증거인가? | 아니다. Fluticasone은 early tmax에도 absorption half-life가 길 수 있음을 보여준다 [T p.177]. |

**Critical Blow:** terminal half-life를 elimination half-life로 착각하면 dosing interval, accumulation, washout 판단이 모두 흔들린다.

<!-- CONFUSION -->
### 혼동쌍 2. F vs ka — extent와 rate

| 혼동 | 정리 |
|---|---|
| F가 증가하면 tmax도 빨라진다? | linear 조건에서는 F는 높이를 scale하지만 tmax는 ka와 kel의 상대값으로 결정된다 [G p.35; T p.174]. |
| ka가 증가하면 AUC도 증가한다? | F와 CL이 일정하면 ka 변화는 shape/tmax/Cmax를 바꾸지만 total AUC는 바꾸지 않는다 [T p.176]. |
| AUC가 같으면 제형 차이가 없다? | AUC가 같아도 Cmax/tmax가 다를 수 있으므로 rate 차이는 남는다 [T pp.181–183]. |

<!-- CONFUSION -->
### 혼동쌍 3. V/F vs V — Critical Blow

| 잘못된 보고 | 올바른 보고 |
|---|---|
| “경구 모델에서 V가 50 L로 추정되었다.” | “경구 단독 모델에서 V/F가 50 L로 추정되었다.” |
| “covariate가 V를 증가시켰다.” | “covariate가 V/F를 변화시켰다. 원인이 V인지 F인지는 본 자료만으로 분리 불가.” |
| “RSE가 낮으니 V가 식별되었다.” | “given model에서 V/F가 정밀하게 추정되었을 뿐, structural identifiability가 해결된 것은 아니다.” |

**Critical Blow:** V/F를 V로 바꾸어 쓰는 순간, 흡수율 변화가 분포용적 변화처럼 보이는 phantom interpretation이 생긴다.

<!-- CONFUSION -->
### 혼동쌍 4. First-order ka vs Zero-order input

| 항목 | First-order input | Zero-order input |
|---|---|---|
| 입력률 | 남은 양에 비례 | 일정 시간 동안 거의 일정 |
| semilog residual | 1차 과정이면 직선성 기대 | 일정 입력 종료 전후로 다른 패턴 |
| 실무 의미 | immediate-release solution/tablet의 단순 근사 | controlled-release/osmotic pump의 근사; 진짜 zero-order absorption은 드묾 [G p.486] |
| PK3 교훈 | first-order model은 ka·kel 비분해와 RSE 문제 | zero-order model이 AIC상 우월했지만 메커니즘 증명은 아님 [G pp.483–486] |

<!-- RECAP -->
**§5 Recap:** 경구 PK에서 가장 위험한 혼동은 slope label, apparent parameter, rate/extent를 서로 바꿔 부르는 것이다. 이름표가 바뀌면 같은 숫자도 다른 임상 결론을 만든다.

---

## §7. SELF-TEST: ACTIVE RECALL MODULE

<!-- SELF-TEST -->
### Q1. Master equation을 쓰고 각 항의 의미를 설명하라.

**Answer:**

$$
C(t)=\frac{k_a F D_{po}}{V(k_a-k_{el})}\left(e^{-k_{el}t}-e^{-k_a t}\right)
$$

`ka`는 absorption-site loss rate, `F`는 systemic fraction, `Dpo`는 dose, `V`는 volume, `kel`은 elimination rate, bracket은 elimination exponential과 absorption exponential의 차이다 [G p.30; T p.782].

<!-- SELF-TEST -->
### Q2. 왜 tmax 식에는 F, V, dose가 들어가지 않는가?

**Answer:** tmax는 `dC/dt = 0`이 되는 시간이다. Linear system에서는 F, V, dose가 곡선의 높이를 scale할 뿐 기울기 0의 시간 위치는 바꾸지 않는다. 따라서 `tmax = ln(ka/kel)/(ka−kel)`이다 [G p.35].

<!-- SELF-TEST -->
### Q3. Frel = 1.0인 두 oral formulation이 임상적으로 완전히 같다고 말할 수 있는가?

**Answer:** 아니다. Frel = 1.0은 AUC 기반 extent가 같다는 뜻이다. ka가 다르면 Cmax와 tmax가 달라질 수 있고, onset이나 peak-related safety가 중요한 약물에서는 임상적 차이가 남을 수 있다 [T pp.181–183].

<!-- SELF-TEST -->
### Q4. PK2에서 V/F = 32 L, F = 0.82가 제시되었다. 진짜 V는 몇 L인가?

**Answer:** 산술적으로는 `V = (V/F)×F = 32×0.82≈26 L`이다. 그러나 원문은 `true V = 20 L`이라고 서술하여 산술값과 충돌한다. 따라서 최종 handout에서는 26 L를 확정 source value로 쓰지 않고, “원문 수치 충돌 [확인 필요]”로 표시한다 [G p.480].

<!-- SELF-TEST -->
### Q5. Oral-only ADVAN2 fit에서 ka = 0.05 hr⁻¹, kel = 0.5 hr⁻¹가 나왔다. 관찰 terminal half-life를 `ln2/0.5 = 1.4 h`라고 써도 되는가?

**Answer:** 안 된다. `ka < kel`이면 oral curve의 관찰 terminal slope는 더 작은 rate constant인 `ka = 0.05 hr⁻¹`를 따를 수 있으므로 terminal half-life는 약 `ln2/0.05 = 13.9 h`로 보인다. `kel = 0.5 hr⁻¹`는 혈장에 들어온 뒤의 true elimination일 수 있지만, oral-only terminal slope만으로 확정할 수 없다.

<!-- SELF-TEST -->
### Q6. PK3에서 zero-order model의 AIC가 first-order보다 낮았다. “흡수가 진짜 0차”라고 결론 내릴 수 있는가?

**Answer:** 아니다. PK3는 zero-order input model이 해당 dataset을 더 잘 설명한다는 것을 보여준다. 그러나 true mechanism을 확정하려면 dose range, repeated dosing, IV data 등 추가 evidence가 필요하다 [G pp.483–486].

<!-- SELF-TEST -->
### Q7. ka,app = 1.0 hr⁻¹이고 kd = 0.4 hr⁻¹라면 ka,true와 F는?

**Answer:** `ka,true = ka,app − kd = 0.6 hr⁻¹`.  

$$
F=\frac{k_{a,true}}{k_{a,true}+k_d}=\frac{0.6}{1.0}=0.6
$$

이 계산은 G Eq.2:70의 구조를 이용한 해석이며, 실제 데이터에서는 kd를 별도 evidence 없이 분리하기 어렵다 [G p.41].

<!-- SELF-TEST -->
### Q8. Boss dilemma: oral-only data에서 terminal slope가 0.18 hr⁻¹로 보이고, alternative model은 kel = 0.69 hr⁻¹도 가능하다고 한다. 무엇을 보고해야 하는가?

**Answer:** `0.18 hr⁻¹`가 관찰 terminal slope라면 관찰 terminal half-life는 `ln2/0.18≈3.85 h`다. 그러나 flip-flop 가능성이 있으면 이 0.18이 kel인지 ka인지 확정할 수 없다. 보고 문장은 다음처럼 써야 한다. “oral-only data에서 terminal slope는 0.18 hr⁻¹로 관찰되었으나, IV 또는 route/formulation comparison 없이는 이것을 elimination rate로 확정할 수 없다. Dose recommendation은 두 해에 대한 sensitivity analysis로 방어해야 한다.” `[교과서 외 해석 포함]`

<!-- RECAP -->
**§7 Recap:** 계산보다 중요한 것은 label이다. 같은 숫자라도 ka인지 kel인지, V인지 V/F인지 잘못 붙이면 임상 결론이 달라진다.

---

## §8. META-FRAME & BIG PICTURE

### A. Positioning

본 세션은 IV bolus 이후 첫 번째 임상 현실, 즉 **흡수 단계가 있는 계**를 다룬다. 이후 multiple dosing, modified-release, food effect, BE, PopPK absorption model을 만나도 판단 기준은 다시 네 가지 질문으로 돌아온다.

1. 입력 함수는 1차인가, 지연/0차/다중 site인가?  
2. F는 일정한가, 제형·식사·first-pass에 의해 달라지는가?  
3. terminal slope는 kel인가, ka인가?  
4. 보고된 V와 CL은 absolute인가, apparent(V/F, CL/F)인가?

### B. Dependencies — 본 세션을 놓치면 생기는 실패 모드

| 실패 모드 | 실제 결과 |
|---|---|
| V/F를 V로 보고 | covariate effect를 분포 변화로 오해. |
| CL/F를 CL로 보고 | F 변화가 clearance 변화처럼 보임. |
| terminal slope를 무조건 kel로 해석 | flip-flop에서 half-life와 accumulation 판단 오류. |
| ka 변화를 absorption extent 변화로 단정 | food/formulation effect 메시지 오류. |
| tmax dose-dependence를 무시 | saturable absorption, first-pass saturation, nonlinear elimination 신호를 놓침. |
| zero-order better fit을 mechanism proof로 단정 | controlled-release/solubility/dissolution 근사를 생리학적 확정으로 과장. |

### C. Professional Moat

30년 차 pharmacometrics 연구자는 경구 모델 결과를 볼 때 먼저 “모델이 맞았는가?”가 아니라 “무엇이 식별되었는가?”를 묻는다. Phase 1 SAD 회의에서 senior가 던지는 실무 질문은 단순하다: **“FIH 단계에서 IV arm 또는 absolute F 확인 가능성을 평가했는가?”** 이 질문 하나가 F, V/F, CL/F, flip-flop, ka,app의 모든 위험을 앞으로 끌어낸다. `[교과서 외 해석]`

### D. Ch.7 context in one sentence

ka와 F의 변동성은 BCS, gastric emptying, dissolution, transporter, intestinal/hepatic first-pass 같은 생리·물리화학적 요인에서 오며, 본 세션의 수식은 그 복잡성을 1차 input과 F라는 두 개의 apparent 축으로 압축해 읽는 첫 단계다 [T pp.197–220].

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.47, Fig.2.32
Why this matters: oral concentration-time curve를 결정하는 요인은 Content Lock의 여러 카드에 분산되어 있다. 이 figure는 그 요인들을 chapter conclusion 수준에서 다시 하나의 구조로 묶어준다.
When to look: §8 Meta-frame을 읽은 뒤, Final Recap 직전.
Learner instruction: figure의 각 determinant를 Content Lock의 5개 MUST card에 다시 매핑하라. 특히 F, input rate, elimination/distribution, apparent parameter가 서로 다른 질문에 답한다는 점을 확인하라.
<!-- /FIGURE_POINTER -->

### E. Final lock sentence

<!-- RECAP -->
**Final Recap:** 경구 PK의 핵심은 C(t)를 맞추는 데서 끝나지 않는다. 더 중요한 일은 C(t)에서 실제로 분리 가능한 것과 분리 불가능한 것을 구분하는 것이다. 경구 단독 데이터는 `V/F`, `CL/F`, apparent ka, 그리고 terminal slope ambiguity를 남긴다. 이 네 가지를 명시하면 handout은 안전하고, 생략하면 모델은 그럴듯하지만 위험해진다.

---

## PART B — Compiler-Only Appendix

This appendix is not learner-facing. It exists only to protect Phase 5 rendering fidelity and prevent regression.

### B1. Compilation Contract

- PART A is the only learner-facing body.
- Phase 5 must render PART A without altering content.
- PART B is instruction/guardrail only.
- Do not restore deprecated material.
- Do not add new scientific content.
- Do not render PART B as learner content unless explicitly requested.
- Do not generate new Mermaid/SVG during Phase 4D; Phase 5 may render only the approved `FIGURE_SCHEMATIC` brief.

### B2. Figure Rendering Instructions

- Approved KEEP figure markers: #1 `FIGURE_SCHEMATIC`, #4 `FIGURE_POINTER`, #6 `FIGURE_POINTER`, #7 `FIGURE_POINTER`.
- Rejected figure candidates #2, #3, and #5 must not be restored.
- Image rights = None: do not embed copyrighted textbook images.
- Render `FIGURE_POINTER` as text-only callout.
- Render `FIGURE_SCHEMATIC` as a structurally distinct redraw from the brief; do not reproduce textbook layout, color palette, or image.
- Preserve all Source fields in figure markers.

#### Approved Figure Strategy and Insertion Map

```markdown
# 03_Content Lock v2.1 — Figure Marker Patch

## 1. Output Mode Declaration

**PATCH MODE**

- 적용 근거: Content Lock v2는 약 5,166 words로 6,000 words 이하이나, 최종 KEEP marker 수가 4개로 `marker count ≤4` 조건에 해당한다.
- 목적: Content Lock v2 본문을 재출력하지 않고, Phase 5에서 원문 v2에 marker만 splice하여 v2.1을 생성한다.
- Image rights: Scope Lock상 `Image rights = None`이므로 textbook figure 원본 삽입은 금지한다. Mode I는 사용하지 않는다. Copyrighted textbook figures는 pointer 또는 구조적으로 구분되는 redraw brief로만 처리한다.

---

## 2. Figure Strategy Table — View (A) Reading-order Figure Plan

| # | Reading order | Location (§ + concept card) | Mode | Source figure (if any) | Trigger | Why text alone is insufficient | Expected learning gain | Decision |
|---|---|---|---|---|---|---|---|---|
| 1 | §2 → Card 1 | Card 1. C(t) Master Equation | R | Textbook basis: G Fig.2.15; T Fig.6-4 | G1, G2 | ODE와 적분식만으로는 `gut loss`, `systemic input`, `central elimination`, `observed C(t)`가 같은 시스템의 다른 층위라는 점이 한눈에 보이지 않는다. | learner가 Master Equation을 단순 공식이 아니라 compartment topology에서 나온 결과로 읽게 된다. | KEEP |
| 2 | §2 → Card 2 | Card 2. tmax / Cmax, Method of Residuals | P | G Fig.2.18–2.19 | G1, G5 | residual method와 lag-time 교점은 시각화가 있으면 이해가 빠르지만, v2에서는 context-level 처리이고 B-Standard figure budget에서 Apex보다 우선순위가 낮다. | residual method의 보조 이해. | REJECT — budget triage; residual method는 Card 2 본문과 equation anchor로 충분히 방어 가능. |
| 3 | §2 → Card 3 | Card 3. Bioavailability F | P | T Fig.6-5; T Fig.6-13; T Table 6-1 | G2, G5 | F, Frel, BE, urine-data estimation은 여러 figure/table로 흩어져 있어 하나를 고르면 오히려 범위가 확장된다. | rate vs extent 보조 이해. | REJECT — Card 3은 equation과 caveat 중심이며, visual ROI가 Card 4/5보다 낮다. |
| 4 | §2 → Card 4 | Card 4. APEX — V/F 식별불가능성 + Flip-flop | P | G Fig.2.17 | G2, G5 | parallel/non-parallel IV/PO terminal slope는 텍스트만으로는 slope label 전환이 잘못 매핑되기 쉽다. | learner가 terminal slope를 자동으로 kel로 읽는 습관을 중단한다. | KEEP |
| 5 | §5 | Confusion Pair 4. First-order ka vs Zero-order input | P | T Fig.6-2; G PK3 Fig.3.1 / Table 3.1 | G2, G5 | first-order vs zero-order는 유용한 비교지만 v2의 core risk는 apparent parameter와 flip-flop이다. | input-function 비교 보조 이해. | REJECT — §5 본문 표와 PK3 설명으로 충분하며, B-Standard budget 초과. |
| 6 | §2 → Card 5 | Card 5. ka,app vs ka,true | P | G Fig.2.24 | G2, G5 | `ka,app = ka,true + kd`는 식으로는 간단하지만, gut compartment에서 disappearance와 systemic appearance가 분리된다는 구조는 시각화 없이는 쉽게 놓친다. | learner가 fitted ka를 곧바로 true absorption으로 부르지 않게 된다. | KEEP |
| 7 | §8 | Meta-frame & Big Picture | P | G Fig.2.32 | G3, G5 | 전체 oral concentration-time curve determinants는 본문 여러 카드에 분산되어 있어, 마지막에 source summary를 보지 않으면 chapter-level 구조가 흩어진 채 끝난다. | learner가 F·ka·V/F·CL/F·input-function을 하나의 oral curve determinant map으로 재결합한다. | KEEP |

---

## 3. Figure Strategy Table — View (B) Type-sorted Summary

**Pointers (P):** #4, #6, #7 → 3 / 3 allowed for B-Standard  
**Schematics (R/N):** #1 → 1 / 1 allowed for B-Standard  
**Images (I):** none → 0; Image rights = None  
**Rejected due to budget or lower ROI:** #2, #3, #5

Budget decision: **PASS** — B-Standard strict budget satisfied.

---

## 4. Figure Briefs — KEEP Items Only

### Figure #1 — R schematic brief

- **Title:** 1차 extravascular input의 compartment topology
- **Visual objective:** learner가 5초 안에 `Dpo → gut compartment → F-scaled input → central compartment → elimination` 흐름을 본다.
- **Core message:** Master Equation은 두 지수의 차이로 보이지만, 그 뿌리는 gut loss와 central elimination이 직렬로 연결된 1차 ODE 구조다.
- **Elements to include:**
  - Oral dose `Dpo`
  - Gut/absorption site `Ag`
  - first-order gut loss arrow labeled `ka·Ag`
  - systemic input branch labeled `F·ka·Ag`
  - optional non-systemic loss branch labeled `(1−F)` or `gut loss / degradation`
  - central compartment `C` or `A/V`
  - elimination arrow labeled `kel·C` or `CL·C`
  - output label: `C(t) = difference of exponentials`
- **Elements to exclude:**
  - textbook bucket/reservoir drawing style
  - empirical concentration-time curves
  - zero-order, multiple absorption sites, transit compartments
  - numerical values
- **Suggested rendering:** Mermaid flowchart
- **Caption:** 1차 흡수 oral model은 gut에서 사라지는 과정과 central compartment에서 제거되는 과정이 직렬로 결합된 구조다.
- **Alt text:** Oral dose가 gut compartment를 거쳐 F-scaled input으로 central compartment에 들어가고, central compartment에서 elimination되는 흐름도.
- **Source relation:** Redrawn from textbook concept (no exact reproduction)

### Figure #4 — P pointer brief

- **Source:** Gabrielsson & Weiner 5e, p.30, Fig.2.17
- **Why this figure matters:** 이 figure는 IV와 PO terminal slope가 parallel이면 oral terminal phase를 elimination으로 볼 수 있지만, non-parallel이면 absorption-limited terminal decline이 될 수 있음을 직접 보여준다.
- **When to look:** Card 4를 읽은 직후.
- **Learner instruction:** 왼쪽 panel에서는 IV와 PO terminal slope가 어떻게 같은 방향으로 떨어지는지 확인하라. 오른쪽 panel에서는 PO terminal slope가 IV slope와 달라질 때, terminal slope label이 kel에서 ka로 바뀔 수 있음을 확인하라.

### Figure #6 — P pointer brief

- **Source:** Gabrielsson & Weiner 5e, p.40, Fig.2.24
- **Why this figure matters:** 이 figure는 `ka,app`가 true absorption만이 아니라 gut degradation/loss를 포함할 수 있음을 compartment 구조로 분리한다.
- **When to look:** Card 5를 읽은 직후.
- **Learner instruction:** gut compartment에서 사라지는 흐름과 systemic circulation에 실제로 들어가는 흐름을 분리해서 보라. fitted ka가 왜 곧바로 `ka,true`가 아닌지 확인하라.

### Figure #7 — P pointer brief

- **Source:** Gabrielsson & Weiner 5e, p.47, Fig.2.32
- **Why this figure matters:** 이 figure는 oral concentration-time curve를 결정하는 요인을 chapter conclusion 수준에서 압축한다.
- **When to look:** §8 Meta-frame을 읽은 뒤, Final Recap 직전.
- **Learner instruction:** figure의 각 determinant를 Content Lock의 5개 MUST card에 다시 매핑하라. 특히 F, input rate, elimination/distribution, apparent parameter가 서로 다른 질문에 답한다는 점을 확인하라.

---

## 5. Insertion Map (PATCH MODE)

| # | Reading order | Anchor (exact heading or unique text from Content Lock v2) | Insert position | Marker block |
|---|---|---|---|---|
| 1 | §2 → Card 1 | `### Card 1. C(t) Master Equation — 경구 PK의 모든 것이 시작되는 한 줄` | after this anchor card; immediately before `### Card 2. tmax / Cmax — 흡수속도와 소실속도가 같아지는 순간` | See Marker Block #1 below |
| 4 | §2 → Card 4 | `### Card 4. APEX — V/F 식별불가능성 + Flip-flop 동정` | after this anchor card; immediately before `### Card 5. ka,app vs ka,true — ka가 측정하는 것은 무엇인가` | See Marker Block #4 below |
| 6 | §2 → Card 5 | `### Card 5. ka,app vs ka,true — ka가 측정하는 것은 무엇인가` | after this anchor card; immediately before `## §5. CONFUSION PAIR DISSECTION` | See Marker Block #6 below |
| 7 | §8 | `### D. Ch.7 context in one sentence` | after this subsection; immediately before `### E. Final lock sentence` | See Marker Block #7 below |

### Marker Block #1

```text
<!-- FIGURE_SCHEMATIC -->
Title: 1차 extravascular input의 compartment topology
Mode: R
Visual objective: 5초 안에 Dpo → gut compartment → F-scaled input → central compartment → elimination 흐름을 보게 한다.
Core message: Master Equation은 두 지수의 차이로 보이지만, 그 뿌리는 gut loss와 central elimination이 직렬로 연결된 1차 ODE 구조다.
Elements to include: Oral dose Dpo; gut/absorption site Ag; first-order gut loss arrow labeled ka·Ag; systemic input branch labeled F·ka·Ag; optional non-systemic loss branch labeled (1−F) or gut loss/degradation; central compartment C or A/V; elimination arrow labeled kel·C or CL·C; output label C(t) = difference of exponentials.
Elements to exclude: textbook bucket/reservoir drawing style; empirical concentration-time curves; zero-order input; multiple absorption sites; transit compartments; numerical values.
Suggested rendering: Mermaid
Caption: 1차 흡수 oral model은 gut에서 사라지는 과정과 central compartment에서 제거되는 과정이 직렬로 결합된 구조다.
Alt text: Oral dose가 gut compartment를 거쳐 F-scaled input으로 central compartment에 들어가고, central compartment에서 elimination되는 흐름도.
Source relation: Redrawn from textbook concept
<!-- /FIGURE_SCHEMATIC -->
```

### Marker Block #4

```text
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.30, Fig.2.17
Why this matters: IV와 PO terminal slope가 parallel이면 oral terminal phase를 elimination으로 해석할 수 있지만, non-parallel이면 absorption-limited terminal decline이 될 수 있다. 이 figure는 terminal slope label이 kel에서 ka로 바뀌는 지점을 직접 보여준다.
When to look: Card 4를 읽은 직후.
Learner instruction: 왼쪽 panel에서는 IV와 PO terminal slope가 어떻게 같은 방향으로 떨어지는지 확인하라. 오른쪽 panel에서는 PO terminal slope가 IV slope와 달라질 때, terminal slope label이 kel에서 ka로 바뀔 수 있음을 확인하라.
<!-- /FIGURE_POINTER -->
```

### Marker Block #6

```text
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.40, Fig.2.24
Why this matters: ka,app는 true absorption만이 아니라 gut degradation/loss를 포함할 수 있다. 이 figure는 fitted ka를 생리학적 true absorption으로 바로 읽으면 안 되는 이유를 compartment 구조로 분리한다.
When to look: Card 5를 읽은 직후.
Learner instruction: gut compartment에서 사라지는 흐름과 systemic circulation에 실제로 들어가는 흐름을 분리해서 보라. fitted ka가 왜 곧바로 ka,true가 아닌지 확인하라.
<!-- /FIGURE_POINTER -->
```

### Marker Block #7

```text
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.47, Fig.2.32
Why this matters: oral concentration-time curve를 결정하는 요인은 Content Lock의 여러 카드에 분산되어 있다. 이 figure는 그 요인들을 chapter conclusion 수준에서 다시 하나의 구조로 묶어준다.
When to look: §8 Meta-frame을 읽은 뒤, Final Recap 직전.
Learner instruction: figure의 각 determinant를 Content Lock의 5개 MUST card에 다시 매핑하라. 특히 F, input rate, elimination/distribution, apparent parameter가 서로 다른 질문에 답한다는 점을 확인하라.
<!-- /FIGURE_POINTER -->
```
```

### B3. Page Tag Rendering Rules

- Preserve all `[p.XX]`, `[pp.XX–YY]`, `[pp.XX, YY]`, and `[p.확인 필요]` tags from PART A.
- Render page tags visibly in HTML.
- Do not fabricate, delete, renumber, or relocate page tags.
- `[p.확인 필요]` remains visible unless resolved by a later verified PDF/Audit pass.
- Do not apply page-tag wrapping inside code blocks or inside `FIGURE_*` marker blocks.
- Source page tags must remain visible in print output.

### B4. HTML Compiler Requirements

The following compiler instruction is preserved as the Phase 5 rendering contract.

```text
ROLE: Education UX Engineer.
Function: transform Content Lock v2.1 into a production-quality HTML file.
You render content. You do not alter it.

If inputs include a PATCH MODE Insertion Map (instead of a fully-marked v2.1):
  Step 1 (mandatory): Splice each marker block into Content Lock v2 at the specified
                      anchor location, producing a working v2.1 in memory.
                      Do not modify any other text.
  Step 2 (mandatory): Output a Splice Verification Table BEFORE rendering HTML.
                      If any anchor cannot be matched exactly, STOP and report.
  Step 3:             Render HTML as below.

INPUT: Content Lock v2.1 (or Content Lock v2 + Insertion Map)
DESIGN REFERENCE: [attach reference HTML — T.E.A. Loop Playbook or equivalent]

=== PATCH MODE SPLICE VERIFICATION ===

When rendering from PATCH MODE inputs, output the following table BEFORE the HTML:

## Splice Verification Table (PATCH MODE only)

| Marker # | Anchor text (truncated to 60 chars) | Anchor found? | Match count | Inserted? | Final location (§ + card) |
|----------|-------------------------------------|---------------|-------------|-----------|---------------------------|

Rules:
- Anchor found?  : YES if exact substring match found in Content Lock v2; NO otherwise.
- Match count    : number of times the anchor appears (must be exactly 1 — see below).
- Inserted?      : YES only if Anchor found = YES AND Match count = 1.
- Final location : the § and concept card immediately preceding the inserted marker.

HALT CONDITIONS (do NOT proceed to HTML rendering if any apply):
  H1. Any "Anchor found?" = NO.
  H2. Any "Match count" ≠ 1 (zero matches OR multiple matches → ambiguous).
  H3. Any "Inserted?" = NO.

If a HALT condition triggers:
  Stop rendering. Output:
    "PATCH MODE SPLICE FAILED — N markers could not be inserted unambiguously.
     Return to Phase 4C and request anchor revision (verbatim, unique, ≥40 chars,
     extend to ≥60 chars if collision)."
  Do NOT guess insertion location.
  Do NOT proceed to HTML output.

If all markers pass: continue to HTML rendering and include the Splice Verification Table
as a comment block at the top of the HTML file (inside <!-- ... --> for traceability).

=== MARKER → COMPONENT MAPPING (mandatory) ===

| Marker / Pattern                  | HTML Component              | Style specification                                              |
|-----------------------------------|-----------------------------|------------------------------------------------------------------|
| <!-- MASTER LENS -->              | Callout box                 | border-left:4px solid #c9a84c; background:rgba(201,168,76,0.08)  |
| <!-- ANNOTATION -->               | Inline abbr / tooltip       | font-size:0.85em; color:var(--muted); font-style:italic          |
| <!-- ANCHOR -->                   | Bridge sentence             | font-style:italic; color:var(--muted)                            |
| <!-- TRENCH -->                   | Practical tip box           | border-left:4px solid var(--rose); background:rose-tint          |
| <!-- CONFUSION -->                | Side-by-side comparison     | .box.amber class                                                 |
| <!-- SELF-TEST -->                | Click-to-reveal accordion   | Question visible; answer hidden until click                      |
| <!-- RECAP -->                    | Section summary box         | border-left:4px solid var(--blue); background:blue-tint          |
| [확인 필요]                        | Highlighted flag            | <mark> tag                                                       |
| [p.XX] / [pp.XX–YY] / [pp.XX, YY] | Inline source page tag      | <span class="source-page">[p.XX]</span> — see CSS below          |
| [p.확인 필요]                      | Source page uncertainty tag | <span class="source-page source-uncertain">[p.확인 필요]</span>  |
| <!-- FIGURE_POINTER -->           | Textbook reference callout  | border-left:4px solid var(--purple); 📖 icon                     |
| <!-- FIGURE_SCHEMATIC -->         | Inline schematic <figure>   | Render via Mermaid (default) or inline SVG; <figcaption> below   |
| <!-- FIGURE_IMAGE_SLOT -->        | Image figure or placeholder | <figure> with <img> if file provided; styled placeholder if not  |

=== SOURCE PAGE TAG RENDERING RULES (v3.3.3 신설) ===

Source page tags are NOT HTML comment markers — they appear as plain text in
Content Lock v2.1 (e.g., "Concept Anatomy: Hepatic Clearance [p.123]").
The HTML compiler must detect them via pattern matching and wrap them in <span> elements.

Pattern detection (regex-equivalent, applied to body text only):
  - \[p\.(\d+)\]                 → standard single-page tag
  - \[pp\.(\d+)[–-](\d+)\]       → range tag (en-dash or hyphen)
  - \[pp\.(\d+(?:,\s*\d+)+)\]    → multi-page non-contiguous tag
  - \[p\.확인 필요\]              → uncertainty tag

Rendering:
  Standard tags  → <span class="source-page">[p.XX]</span>
  Uncertain tags → <span class="source-page source-uncertain">[p.확인 필요]</span>

Detection scope:
  - APPLY pattern detection to body text inside §2 cards, equation captions, and example headings.
  - DO NOT apply pattern detection inside <pre><code> blocks (preserve verbatim in code).
  - DO NOT apply pattern detection inside <!-- FIGURE_* --> marker blocks (those have their own
    internal "Source:" fields and are not body content tags).

Fabrication prohibition:
  - DO NOT add page tags that are not present in Content Lock v2.1.
  - DO NOT silently remove page tags during rendering.
  - DO NOT alter page numbers (e.g., normalizing en-dash to em-dash is permitted; changing
    page numbers is forbidden).

=== RENDERING REQUIREMENTS ===

Math      : MathJax CDN — inline \(...\), display \[...\]
Code      : <pre><code> dark background, language class attribute
Navigation: sticky left sidebar, anchor jump per § section
Accordion : Self-Test answers hidden by default; revealed on user click
Checklist : sessionStorage state persistence across page reload
Controls  : code block copy button, print/PDF button (window.print())
Responsive: ≤768px single-column + collapsed nav; ≥1024px two-column
Dark/Light: prefers-color-scheme auto-switch
Print     : remove backgrounds, hide navigation, optimize page-break-inside
            Source page tags MUST remain visible in print mode (do not hide via @media print).

=== NAVIGATION ANCHOR INTEGRITY RULES ===

The HTML must include a sticky left sidebar table of contents.

For every sidebar link:
- Use <a href="#..."> links only.
- Every href target must have a matching id in the body.
- Every major section heading (§1, §2, §3...) must receive a stable id.
- Every concept card inside §2 must also receive a stable id when possible.
- The href value and body id must match exactly, including spelling and hyphens.
- Do not create TOC links whose target id does not exist.
- Do not create duplicate ids.
- Enable smooth scrolling with:

html { scroll-behavior: smooth; }

Before finalizing, self-check:
1. Count all sidebar href="#id" values.
2. Confirm each id exists exactly once in the document.
3. Confirm no duplicate id exists in the body.
4. If any mismatch exists, fix before output.

Required implementation:
- The sidebar must be placed on the left side on desktop.
- The sidebar must remain visible while scrolling unless the viewport is mobile-sized.
- Each major section must be reachable by clicking the sidebar entry.
- Each §2 concept card should be reachable by clicking its sidebar sub-entry when concept-card headings are present.
- The active section may be highlighted using IntersectionObserver or equivalent JavaScript.
- On mobile viewports, the sidebar may collapse, but anchor navigation must still work.

=== FIGURE RENDERING RULES ===

GENERAL:
- Every figure marker becomes a proper <figure> block (or pointer callout) with caption and alt text.
- Figures must not interrupt reading flow — place at end of the concept card they belong to.
- Visual style consistent with the design system. No decorative imagery.
- Do not generate or embed figures not present in Content Lock v2.1.

FIGURE_POINTER:
- Render as a compact callout box with class .figure-pointer:
    border-left: 4px solid var(--purple);
    background: rgba(155, 89, 182, 0.06);
    icon: 📖
- Display: Source / Why this matters / When to look / Learner instruction.
- Do NOT generate or embed an image — pointer is text-only.

FIGURE_SCHEMATIC (Mode R or N):
- Default rendering: Mermaid via CDN (https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js).
  Use <div class="mermaid">...</div> inside <figure>.
- Use inline SVG only when the schematic requires curve plotting, precise spatial layout,
  or shapes Mermaid cannot express (e.g., concentration-time curves, radar plots).
- For comparison-style figures (Confusion-pair), CSS side-by-side cards (no SVG) are acceptable
  if the brief's "Suggested rendering" specifies CSS-card.
- Implement the brief faithfully: include only listed elements; exclude listed exclusions.
- Do not reproduce the textbook figure's exact layout, color palette, or label placement
  even when "Redrawn from textbook concept" — visual distinctness is mandatory.
- Caption: render as <figcaption>.
- Alt text: render as alt attribute on SVG container or aria-label on <figure>.
- Mermaid initialization in inline JS:
    mermaid.initialize({ startOnLoad: true, theme: 'neutral',
                         themeVariables: { fontFamily: 'var(--font)' } });

MERMAID SELF-CHECK (생성 직후 self-validate):
After generating each Mermaid block, verify all of the following BEFORE finalizing:
  M1. Block opens with a valid directive: flowchart TD | flowchart LR |
      graph TD | graph LR | sequenceDiagram | classDiagram | stateDiagram-v2 | erDiagram.
  M2. Node IDs contain ONLY [A-Za-z0-9_]. No parentheses, slashes, dots, hyphens,
      Korean characters, spaces, or quotes inside IDs.
  M3. Any label containing parentheses, special characters, or non-ASCII characters
      is wrapped in double quotes:  A["Clearance (CL)"]
  M4. Edge labels with special chars use the |"label"| form:  A -->|"Q × E"| B
  M5. Subgraph titles, when used, are quoted:  subgraph "Hepatic"
  M6. No trailing semicolons inside node definitions.
  M7. If any of M1–M6 cannot be satisfied OR Mermaid expressiveness is insufficient,
      FALLBACK to one of:
        - inline SVG (for spatial/curve figures)
        - CSS side-by-side cards (for comparison figures)
      Do not emit a Mermaid block that is likely to fail rendering.

FIGURE_IMAGE_SLOT:
- If Rights = User-supplied AND image file exists in working directory:
    <figure><img src="..." alt="..." /><figcaption>...</figcaption></figure>
- If Rights = Open-license AND license/attribution provided in marker:
    <figure>
      <img src="..." alt="..." />
      <figcaption>
        [Caption text]
        <span class="figure-attribution">
          Source: [Attribution]. License: [License type].
          [<a href="[Source URL]">link</a>]
        </span>
      </figcaption>
    </figure>
- If Rights = placeholder OR file unavailable:
    Render styled placeholder box with class .figure-placeholder:
    [📖 교과서 원그림 삽입 위치 — Source: Book, p.XX, Fig.Y]
    Do not generate an approximation of the textbook figure.

CAPTION & ALT TEXT (all schematic/image figures):
- Caption mandatory. Alt text mandatory. Both from the brief.

=== CSS DESIGN SYSTEM (inherit from reference) ===

Variables: --bg, --surface, --surface-2, --ink, --muted, --faint,
           --line, --line-strong, --blue, --green, --purple, --amber, --rose,
           --radius, --radius-sm, --shadow, --font, --mono

Add for navigation:
  html {
    scroll-behavior: smooth;
  }
  .sidebar {
    position: sticky;
    top: 0;
    align-self: start;
    height: 100vh;
    overflow-y: auto;
  }
  .sidebar a {
    display: block;
    text-decoration: none;
  }
  .sidebar a.active {
    font-weight: 700;
    border-left: 3px solid var(--purple);
  }
  @media (max-width: 768px) {
    .sidebar {
      position: static;
      height: auto;
      max-height: none;
    }
  }

Add for v3.3 figure components:
  .figure-pointer { border-left: 4px solid var(--purple); ... }
  figure { margin: 1.5em 0; }
  figcaption { color: var(--muted); font-size: 0.9em; margin-top: 0.5em; }
  .figure-attribution { display: block; font-size: 0.8em; margin-top: 0.3em;
                        color: var(--faint); }
  .figure-placeholder { border: 2px dashed var(--line-strong); padding: 2em;
                         text-align: center; color: var(--muted); }

Add for v3.3.3 source page tag components:
  .source-page {
    font-size: 0.78em;
    color: var(--purple);
    background: rgba(155, 89, 182, 0.10);
    padding: 2px 6px;
    border-radius: 6px;
    vertical-align: super;
    white-space: nowrap;
    margin-left: 0.25em;
    font-weight: 500;
    letter-spacing: 0.01em;
  }
  .source-page.source-uncertain {
    color: var(--amber);
    background: rgba(245, 158, 11, 0.12);
    border: 1px dashed var(--amber);
  }
  /* Print: keep tags visible for offline traceability */
  @media print {
    .source-page {
      background: transparent;
      color: #000;
      border: 1px solid #888;
    }
  }
  /* Hover: subtle elevation to confirm interactivity (if linked to PDF in future) */
  .source-page:hover {
    background: rgba(155, 89, 182, 0.18);
  }

=== OUTPUT SPECIFICATION ===

Single HTML file with all custom CSS and custom JS inline.
External runtime dependencies are allowed ONLY for:
  - MathJax CDN
  - Mermaid CDN
  - cdnjs.cloudflare.com library list (e.g., highlight.js for code coloring)
No external local .css / .js / font / image files unless explicitly supplied by the user.
File header comment block: document title | chapter | generation date.
PATCH MODE only: include Splice Verification Table as a comment block in the HTML header.

=== PROHIBITED ===

- <iframe>, <embed>, external .js files (other than permitted CDNs), external local .css
  files, external font files (other than permitted CDNs).
- Any modification to Content Lock v2.1 text content (including page tag text).
- Self-Test answer text visible without user interaction.
- Markers rendered as plain text (every marker must become its mapped component).
- Source page tags rendered as plain bracketed text without <span> wrapping.
- Reproducing copyrighted textbook figures exactly when rendering R/N schematics.
- Embedding textbook images without User-supplied or Open-license rights with attribution.
- Emitting Mermaid blocks that fail M1–M6 self-check.
- Proceeding to HTML rendering when any PATCH MODE Splice Verification HALT condition
  (H1–H3) is triggered.
- Guessing insertion location for unmatched anchors.
- Adding new source page tags or altering existing ones during HTML compilation.
- Hiding source page tags via @media print or display:none under any condition.
- Creating sidebar TOC links whose target ids do not exist.
- Creating duplicate body ids.
- Creating body ids that are not stable or that change across repeated generations for the same heading text.

Output (PATCH MODE):
  1. Splice Verification Table
  2. (only if all markers pass) Complete HTML from <!DOCTYPE html> to </html>

Output (FULL MODE):
  Complete HTML from <!DOCTYPE html> to </html>.
```

### B5. Audit Guardrails

- Keep Rowland & Tozer Ch.7 only as context, not as a broad physiology chapter.
- Never label T Eq.6-3 as the integrated oral concentration solution; it is the mass-balance ODE. Integrated first-order absorption solution is Appendix F Eq.F-1.
- Do not restore the erroneous flip-flop intuition that slow absorption should cause a fast terminal decline; when `ka < kel`, observed terminal decline may be absorption-limited.
- Do not state that every oral parameter is simply “not true.” The locked distinction is: `V/F` and `CL/F` are apparent; terminal slope label may be ambiguous under flip-flop; fitted `ka` may be apparent GI disappearance.
- Do not state plasma AUC-based absolute F is available without an IV/reference clearance basis. Preserve the urine-data caveat from T Ch.6.
- Do not treat PK2 `32×0.82≈26 L` as a confirmed source value; retain the source inconsistency flag because the textbook text also states `true V = 20 L`.
- Do not move PK3 CV/RSE problems into PK2.
- Preserve corrected self-test logic for Q5 and Q8: observed terminal half-life follows the smaller apparent terminal rate under flip-flop ambiguity.
- Do not restore unsupported NDA deficiency-letter, ICH/FDA guidance, or external reviewer claims as textbook-derived content.
- Do not restore rejected items: Vaughan/Pidgeon-Pitlick full derivations, local topical BE/microdialysis, broad BCS expansion, broad Bayesian/shrinkage diagnostics, or unapproved code blocks.


#### Locked Adjudication Reference from Content Lock v2

```markdown
## 0.1 Adjudication Table Summary

**원칙:** Audit MUST_FIX는 기본 채택. Crucible Grade A는 PDF spine에 연결되거나 [교과서 외 해석]으로 명시 가능한 경우만 채택. Grade C와 unsupported regulatory phrasing은 삭제.

| Source | Item | Verdict | Rationale |
|---|---|---|---|
| Audit T4 #1 | Source B에 Ch.7 누락 | ADOPT | 본문이 BCS·gastric emptying·F product를 쓰므로 `Ch.7 context only`로 header에 추가. |
| Audit T4 #2 | T Eq.6-3를 Master Equation으로 오표기 | ADOPT | T Eq.6-3은 mass-balance ODE이고, integrated solution은 Appendix F Eq.F-1. |
| Audit T4 #3 | flip-flop 직관 문장 오류 | ADOPT | `ka < kel`이면 관찰 terminal slope가 residual absorption을 따라 느리게 보일 수 있도록 수정. |
| Audit T4 #4 | “V·F·ka·kel 모두 진짜 아님” 과강함 | ADOPT | V/F 분리 불가와 terminal slope label 불확정을 분리해 표현. |
| Audit T4 #5 | urine-data caveat 누락 | ADOPT | T Ch.6이 plasma와 urine 기반 F/Frel/CLr 추정을 모두 다루므로 Card 3에 1문장 삽입. |
| Audit T4 #6 | PK2 V=26 L vs 원문 V=20 L 충돌 | ADOPT | 계산값을 정답화하지 않고 “source inconsistency / arithmetic check”로 플래그 유지. |
| Audit T4 #7 | PK2에 CV% 3400% 잘못 연결 | ADOPT | 3400%는 PK3 Table 3.1에만 연결하고 PK2는 high SE/correlation로 수정. |
| Audit T4 #8 | V/F 32→6.54를 6배로 표현 | ADOPT | 산술상 약 5배로 수정하거나 수치 비교만 유지. |
| Audit T4 #9 | Self-test Q5 half-life logic | ADOPT | `ka < kel` oral-only에서 관찰 terminal slope는 작은 rate constant를 따라야 함. |
| Audit T4 #10 | Self-test Q8 half-life / flip-flop logic | ADOPT | `ln2/0.18≈3.85 h`, `ln2/0.69≈1.0 h`를 구분해 재작성. |
| Audit T4 #11 | ICH/FDA/deficiency letter unsupported | ADOPT | 외부 guidance 단언은 삭제; NONMEM 실무 tip은 [교과서 외 해석]으로 분리. |
| Audit T4 #12 | Phantom Volume Drift AUC algebra | ADOPT | `AUC = F·Dose/CL = Dose/(CL/F)`로 정정. |
| Audit T4 #13 | T Table 6-1 parameter-estimation example | PARTIAL_ADOPT | Card 3에 i.m. 97%, oral 46% 예시를 1문장 anchor로 삽입. |
| Audit T4 #14 | T Fig.6-5 dose proportionality message | ADOPT | Linear system에서 dose/F 변화는 Cmax·AUC를 scale하고 tmax는 바꾸지 않는다고 Card 2/3에 반영. |
| Audit T4 #15 | Theophylline / Penicillin G examples | PARTIAL_ADOPT | Card 4에 route/formulation discrimination 예시로 1문장씩만 삽입. |
| Audit T4 #16 | G Fig.2.32 view instruction | REJECT_FOR_4A | Figure inventory는 Phase 4C로 이관; 4A 본문에는 figure marker를 넣지 않음. |
| Audit T4 #17 | Vaughan / Pidgeon-Pitlick omitted | ADOPT | B-Standard에서 제외 유지. |
| Audit T4 #18 | Local BE/topical microdialysis omitted | ADOPT | 본 세션 core 밖이라 제외 유지. |
| Audit T4 #19 | Ch.7 BCS는 1–2문장 context only | ADOPT | §8에 1문장으로 압축. |
| Audit T1/T2 MATCH rows | Source-backed equations/examples | ADOPT | Eq.2:35, Eq.2:52, Eq.2:74, Eq.2:70, PK2/PK3 핵심 anchor는 페이지 태그와 함께 유지. |
| Audit T1/T2 ERROR/NOT_IN_SOURCE rows | unsupported or internally inconsistent claims | ADOPT_AS_CORRECTION | 오류 수식·half-life·external regulatory wording은 수정 또는 삭제. |
| Audit T6 | Figure inventory | CARRY_FORWARD | 명시 지침에 따라 4A adjudication 대상에서 제외하고 Phase 4C로 이관. |
| Crucible T4-1 | CSTR/RC/화학공학 비유 과다 | PARTIAL_ADOPT | CSTR 등 부정확한 동형성은 삭제하고 “1차 ODE 직렬 시스템” 1문장으로 압축. |
| Crucible T4-2 | predator-prey turning point 비유 | REJECT | 비선형 predator-prey는 본 모델과 구조가 달라 삭제. |
| Crucible T4-3 | §5 PK3 시그니처 행 과다 | ADOPT | PK3는 “first-order RSE 폭발 vs zero-order AIC 우위” 1문장으로 압축. |
| Crucible T4-4 | zero-order physiological mapping 과장 | ADOPT | controlled-release/osmotic pump의 근사로 제한하고 진짜 zero-order는 드물다고 수정. |
| Crucible T4-5 | Q3 자기참조 후속 질문 | ADOPT | tmax 90% CI 문장 삭제, Frel=1.0이지만 tmax가 다른 상황으로 변경. |
| Crucible T4-6 | §8 Professional Moat 중복 마무리 | ADOPT | 중복 결론 삭제 후 RECAP에 통합. |
| Crucible T4-7 | BCS 맥락 과다 문장 | ADOPT | §8에서 literal 1문장으로 압축. |
| Crucible Grade A | Cognitive Wall #1/#2/#4 | PARTIAL_ADOPT | PDF spine에 직접 연결되는 범위에서 Card 1/2/5에 1–2문장만 삽입. |
| Crucible Grade A | Expert Intuition patterns 1/2/4 | PARTIAL_ADOPT | Pattern 1/2는 [교과서 외 해석] Trench로 유지; Pattern 4는 깊이 통합하지 않음. |
| Crucible Grade A | Risk #1 F1 estimate/fix | PARTIAL_ADOPT | PDF 직접 source가 아니므로 [교과서 외 해석]으로 Card 4에 삽입. |
| Crucible Grade A | Twin Suppression / V/F Drift signatures | PARTIAL_ADOPT | [교과서 외 해석]로 명명만 유지; 수치 cutoff는 확정 단언하지 않음. |
| Crucible Grade A | Confusion Pair 3 Critical Blow | ADOPT | V/F vs V 혼동도 핵심 위험이므로 §5에 Critical Blow 추가. |
| Crucible Grade A | Tip 1 KA initial trap | PARTIAL_ADOPT | [교과서 외 해석] 실무 tip으로 Card 1에 압축 삽입. |
| Crucible Grade A | Tip 3 F1 fix/reporting | PARTIAL_ADOPT | [교과서 외 해석]으로 Card 4에 삽입. |
| Crucible Grade B | numerical vs structural identifiability | ADOPT | Apex 카드의 핵심 학습 가치가 높아 Card 4에 명시. |
| Crucible Grade B | SAD 회의 senior 질문 | PARTIAL_ADOPT | §8 Professional Moat에 1문장으로 압축. |
| Crucible Grade B | Residual method 자동화 기준 | PARTIAL_ADOPT | [교과서 외 해석]으로 Card 2에 1문장 삽입. |
| Crucible Grade B | food effect ka,app reporting | PARTIAL_ADOPT | [교과서 외 해석]으로 Card 5에 삽입. |
| Crucible Grade B | Phantom Volume Drift algebra correction | ADOPT | Audit #12와 함께 Card 4/§5에 반영. |
| Crucible Grade B | dose-dependent tmax signal | ADOPT | Linear 조건의 반례로 §8 failure mode에 반영. |
| Crucible Grade C | ICH/FDA guidance expansion | REJECT | PDF source 밖이고 이번 작업은 web OFF/PDF 대조 기반. |
| Crucible Grade C | BCS Class III/IV 상세 | REJECT | Ch.7은 context only. |
| Crucible Grade C | TMDD with oral input deep dive | REJECT | 다음 고급 세션 dependency로만 유지. |
| Crucible Grade C | Bayesian identifiability analysis | REJECT | B-Standard handout 범위 초과. |
| Crucible Grade C | RSE too-small pattern full integration | REJECT | ETA/shrinkage 고급 세션 영역; 1줄 경고도 본문 길이상 제외. |

---
```

### B6. Crucible Guardrails

- Crucible Report v1 is not a raw content source at this stage.
- Preserve only already-adopted or explicitly allowed Grade A/B logic.
- Do not reintroduce omitted or rejected Crucible items.
- Do not convert speculative insight into textbook-derived fact.
- Any expert inference must remain visibly labeled and must not add unsupported numerical values, new named examples, new equations, or new page tags.

### B7. Deprecated and Forbidden Restorations

- Step 1 Draft v0 is deprecated.
- Do not restore rejected overclaims, unsupported numbers, unsupported regulatory claims, source-unsupported examples, unapproved code, or unapproved figures.
- Do not use Step 1 Draft v0 as learner-body source except through the Micro-Patch Gate.
- Do not restore the old source header omitting T Ch.7.
- Do not restore the old `T Eq.6-3 = Master Equation` mapping.
- Do not restore broad external guidance language unless a later workflow explicitly allows web/external-source verification.

### B8. PATCH MODE Splice Verification Table

| Marker # | Anchor text (truncated to 60 chars) | Anchor found? | Match count | Inserted? | Final location (§ + card) |
|---|---|---|---:|---|---|
| 1 | `### Card 1. C(t) Master Equation — 경구 PK의 모든 것이 시작되는 한 줄` | YES | 1 | YES | §2 / Card 1 |
| 4 | `### Card 4. APEX — V/F 식별불가능성 + Flip-flop 동정` | YES | 1 | YES | §2 / Card 4 |
| 6 | `### Card 5. ka,app vs ka,true — ka가 측정하는 것은 무엇인가` | YES | 1 | YES | §2 / Card 5 |
| 7 | `### D. Ch.7 context in one sentence` | YES | 1 | YES | §8 / D. Ch.7 context |


### B9. Zero-Omission Coverage Matrix

| Domain | Required item | Evidence in PART A | Status | Action |
|---|---|---|---|---|
| C1 Scope concepts | C(t), tmax/Cmax, F, V/F+flip-flop, ka,app vs ka,true | §0 MUST map + §2 Cards 1–5 | PRESENT | None |
| C1 Chapter role | Oral/extravascular absorption as first clinical reality after IV bolus; PopPK/NONMEM dependency | §1 roadmap + §8 Positioning/Dependencies | PRESENT | None |
| C2 Data anchors | PK2 lag-time model: Ka, K, V/F, tlag; PK2 source inconsistency; PK3 AIC/CV/RSE issue | Card 4 Case anchors + Self-test Q4/Q6 | PRESENT | None |
| C2 R&T examples | i.m. 97%, oral 46%; fluticasone, theophylline, penicillin G context | Card 3 and Card 4 Case anchors | PRESENT_COMPRESSED | Kept within B-Standard scope |
| C3 Audit MUST_FIX | Ch.7 source, Eq.6-3 vs Eq.F-1, flip-flop, V/F wording, F urine caveat, PK2 V conflict, self-test logic, unsupported regulatory phrasing | §0 source lines, Cards 1–4, Self-test Q4/Q5/Q8, §8 | PRESENT | No micro-patch needed |
| C4 Audit T5 findings | Omitted/problematic items and missing author messages | Content Lock v2 adjudicated; learner body preserves adopted corrections; rejections in B5 | PRESENT_COMPRESSED | No restoration of rejected items |
| C5 Figure coverage | KEEP markers #1, #4, #6, #7; rejected #2, #3, #5 not restored | Spliced marker blocks in §2 and §8; B2 strategy table | PRESENT | PATCH MODE splice PASS |
| C6 Page-tag integrity | Preserve existing page tags and [p.확인 필요] flags; no fabricated tags | PART A retains original Content Lock tags; augmentations add none | PRESENT | HTML compiler must wrap tags only |
| C7 Crucible Grade A | cognitive walls, identifiability, KA initial/reporting cautions, confusion pairs | Cards 1–5, §5, §8 plus 5 labeled augmentation notes | PRESENT_COMPRESSED | Augmentations are bounded |
| C8 Deprecated draft regression | Step 1 errors not restored: Eq.6-3 mislabel, over-strong true-parameter claim, unsupported ICH/FDA/NDA claims | B5/B7 guardrails; PART A wording follows Content Lock v2 | PRESENT | Step 1 not used as raw source |
| C9 Canonical integrity | Scientific learner body equals Content Lock v2 scientific body + approved 4C markers + labeled mastery notes | PART A construction | PRESENT | No broad rewrite; no micro-patches |


### B10. Micro-Patch Log

No micro-patches needed. PART A equals the learner-facing scientific portion of Content Lock v2 with approved 4C markers spliced at verified anchors, except for the bounded Mastery Augmentation Layer.

| Patch # | Location | Source trigger | Inserted text | PDF/Audit basis | Why allowed | Page tag handling |
|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — |

### B11. Mastery Augmentation Log

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
|---:|---|---|---|---|---|---|
| 1 | §2 Card 1 | M/K | YES | CRUCIBLE_DERIVED | Converts `ka−kel` from algebraic denominator into parameter-separation intuition. | Low |
| 2 | §2 Card 2 | M/J | YES | CRUCIBLE_DERIVED | Explains tmax scale-invariance and when dose/condition dependence becomes a warning sign. | Low |
| 3 | §2 Card 3 | W/J | YES | AUDIT_DERIVED | Keeps F/ka/AUC/Cmax/tmax reporting language separated. | Low |
| 4 | §2 Card 4 | J/R | YES | CRUCIBLE_DERIVED | Separates numerical precision from structural identifiability. | Low |
| 5 | §2 Card 5 | F/K | YES | TEXTBOOK_DERIVED | Prevents fitted ka from being over-labeled as true absorption. | Low |


#### Rejected or deferred augmentation candidates

| Rejected candidate | Reason for rejection |
|---|---|
| Full external regulatory guidance expansion | Requires web/external sources and was rejected by Audit/Content Lock for this PDF-only workflow. |
| Detailed BCS Class III/IV physiology expansion | Ch.7 is context-only under Scope Lock; broad physiology would reopen scope. |
| Bayesian/shrinkage identifiability diagnostics | Useful but beyond B-Standard learner handout and not directly PDF-grounded. |
| New named clinical examples | Disallowed unless already present in PDF/Audit/Crucible; no additional examples added. |


### B12. Final Phase 5 Safety Checklist

- PART A alone is learner-facing and complete.
- PART A contains no audit/process/compiler text.
- PART A includes the scientific learner body plus approved spliced markers.
- All approved figure markers are present exactly once.
- No unapproved figure markers were added.
- All source page tags are preserved exactly unless a later verified correction is made.
- No page tags were fabricated.
- Audit and Crucible were not used as raw prose sources.
- Step 1 Draft v0 was not used as a content source except through the Micro-Patch Gate.
- Rejected material was not restored.
- Mastery augmentations are visibly labeled and adjacent to the relevant concept.
- No augmentation introduces unsupported numerical values, new named drug/example, new equation, or new page tag.
- PART B contains all Phase 5 rendering requirements.
- No HTML was generated in Phase 4D.
- No Mermaid/SVG code was generated in Phase 4D.


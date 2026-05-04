# 03_Content Lock v2 — Editorial Process Log

## PASS 1 — Edit Log

| Location (§ + card) | Edit type | Before (excerpt) | After (excerpt) |
|---|---|---|---|
| §1 Big Idea | R1/R2 | “IV bolus는... 만들지만, 경구/혈관외 투여는...” | IV와 경구/혈관외 투여를 두 문장으로 분리하고, “따라서/이 때문에”로 causal chain을 명시. |
| Card 1 Formal Definition | R4 | “linear PK를 가정한 extravascular concentration-time equation” | `linear PK`의 의미를 first-use gloss로 보완하고 sentence load를 낮춤. |
| Card 1 Lag-time | R2/R5 | “실제 흡수 시작 시점 이후의 시간만 식에 들어간다” | 투여 시각과 흡수 시작 시각의 차이를 명시. |
| Card 1 Zero-order input | R1/R2 | “같은 central elimination에 다른 input function을 붙인 경우” | central elimination 유지 + input function 변경으로 구조를 분리. |
| Card 2 tmax scaling | R1/R5 | “곡선의 높이를 수직으로 scale한다” | 높이 변화와 기울기 0의 시간 위치를 분리해 설명. |
| Card 2 Residual method | R1 | 한 문장 안에 terminal line, residual line, flip-flop caveat 포함 | terminal line → residual line → caveat 순서로 분할. |
| Card 3 F/ka distinction | R1/R3 | “ka는..., F는...” | 각 파라미터가 묻는 질문을 명시. |
| Card 3 Urine caveat | R2 | “단, fraction...” | urinary method의 전제를 별도 문장으로 고정. |
| Card 4 AUC relation | R1/R2 | “Dose/(CL/F)는...” | algebraic equivalence와 interpretation limit를 분리. |
| Card 4 Flip-flop | R1/R2 | “관찰 terminal slope는 absorption process를 반영할 수 있다” | absorption이 느린 과정이 되는 이유를 명시. |
| Card 5 ka interpretation | R1/R3 | “ka가 커졌다는 것은...” | “흡수 빨라짐” 단정 금지를 먼저 제시. |
| §8 Final Recap | R1/R3 | “핵심은 C(t)를 맞추는 것이 아니라...” | model fit 이후의 identifiability 판단을 더 가까이 배치. |

## PASS 2 — Annotation Candidate Table

| Type | Location (§ + card) | Current text (excerpt) | Proposed annotation | Risk |
|---|---|---|---|---|
| A | §1 Big Idea | 차이지수 곡선 | 차이지수 곡선(← 두 지수함수의 차이로 생긴 곡선) | Low |
| A | Card 1 Formal Definition | linear PK | linear PK(← dose 비례성이 유지되는 PK) | Low |
| A | Card 1 Lag-time | Lag-time extension | Lag-time(← 흡수 시작 전 지연시간) | Low |
| A | Card 3 Absolute F | bioavailability F | bioavailability F(← 전신 순환 도달 분율) | Low |
| A | Card 3 Mechanistic F | intestinal/hepatic first-pass | first-pass glosses for intestinal/hepatic loss | Low |
| B | Card 3 → Card 4 Anchor | F와 V가 분리되지 않는다 | AUC 변화 원인과 concentration amplitude 원인을 나눌 수 없다는 bridge | Low |
| A | Card 4 Master Lens | structural identifiability | structural identifiability(← 원리적으로 분리 추정 가능한지) | Low |
| A | Card 5 Master Lens | apparent parameter | apparent(← 모델에서 보이는 겉보기) parameter | Low |
| C | Card 4 V/F | V/F as shadow analogy | 구조적 식별불가능성을 비유로 설명 | Medium/High |

## PASS 2 — Final Recommendation

**Must annotate (Low risk):** 차이지수 곡선, linear PK, Lag-time, bioavailability F, first-pass, structural identifiability, apparent parameter, Card 3→4 bridge.

**Optional (Medium risk, high learning value):** V/F structural analogy. 최종본에서는 흐름 방해와 과잉 설명 위험 때문에 제외.

**Do not annotate:** 이미 명확한 tmax derivation, self-test 계산 문항, case anchor 수치. 추가 설명은 길이를 늘리고 기술 정밀도를 희석할 가능성이 높음.

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

### E. Final lock sentence

<!-- RECAP -->
**Final Recap:** 경구 PK의 핵심은 C(t)를 맞추는 데서 끝나지 않는다. 더 중요한 일은 C(t)에서 실제로 분리 가능한 것과 분리 불가능한 것을 구분하는 것이다. 경구 단독 데이터는 `V/F`, `CL/F`, apparent ka, 그리고 terminal slope ambiguity를 남긴다. 이 네 가지를 명시하면 handout은 안전하고, 생략하면 모델은 그럴듯하지만 위험해진다.

---

## Content Lock v2 Length Check

- Content Lock v1 final body: 24,806 Unicode chars / 34,970 bytes.
- Content Lock v2 final body: 25,509 chars (2.8% vs v1; within +8% limit).
- Pass 1 readability edits were limited to cognitively dense or causally implicit sentences.
- Pass 2 annotations were restricted to low-risk glosses and one high-value bridge.
- `[확인 필요]` items and source page tags were preserved unchanged.
- Figure inventory intentionally remains excluded and is carried forward to Phase 4C.


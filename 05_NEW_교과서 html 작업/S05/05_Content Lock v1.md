# 05_Content Lock v1
## 2구획 모델 — 이중지수 분해 / α·β 재파라미터화 / V₁·Vss·Vβ 체계

> **Source:** Gabrielsson & Weiner 5e Ch.2 §2.4.1–2.4.6 + Case Studies PK7/PK8 [G&W pp.57–77, 505–517] + Rowland & Tozer 5e Ch.19 [R&T pp.613–656]  
> **Mode:** A-Critical  
> **Status:** Phase 4A Content Lock v1 — Source Fidelity Audit v1 + Insight Crucible v1 adjudicated and compressed  
> **Scope note:** Audit T6 Figure Inventory is not adjudicated in this file and is carried forward unchanged to Phase 4C.

---

## Updated Curation Map

### MUST — §2 정식 카드 5개

| # | Concept | Content Lock 판정 |
|---|---|---|
| **M1** | **이중지수 방정식 + 잔차법(Method of Residuals)** | 유지. 2구획의 출발점은 semilog 곡선을 두 지수항으로 분리하는 것이다. 잔차법은 교육적 curve-stripping 및 initial estimate 감각을 위한 도구로 제한한다. [G&W pp.59–63; R&T pp.615–623] |
| **M2** | **Macro ↔ Micro ↔ Physiological 3중 좌표계 변환** | 유지하되, 4 자유도 표현을 source parameter set으로 수정한다: macro $(A,\alpha,B,\beta)$, micro $(V_c,k_{10},k_{12},k_{21})$, physiological $(V_c,CL,Cld,V_t)$. [G&W pp.60–71; R&T pp.618–619] |
| **M3** | **V₁ / Vss / Vβ 3중 분포용적 체계** | Apex로 유지. 잘못된 ellipsis 식은 삭제하고 source-supported 식만 남긴다. $V_1 \le V_{ss} \le V_\beta$는 표준 central-elimination 2구획 가정에서만 사용한다. [G&W pp.63–65; R&T pp.617, 628–630] |
| **M4** | **재파라미터화 5종 + condition number** | 유지하되 PK8 condition number 범위를 **29.69–3,186**으로 수정한다. 3,186/29.69 ≈ 107배이므로 “200배”를 삭제한다. [G&W pp.513–517] |
| **M5** | **분포속도론의 임상 파급 + terminal half-life의 함정** | 유지하되 “항상 빗나간다”를 삭제한다. terminal half-life는 많은 약물에서 유용하지만, $f_2$, 투여 방식, plateau 시점, tissue accumulation을 확인하지 않으면 단순 적용이 깨진다. [R&T pp.631–641] |

### CONTEXT — 인접 MUST 카드 안에서 1–2문장 처리

- **Catenary vs mammillary**: mammillary가 mainstream; catenary=enterohepatic recirculation 예시는 source 밖이므로 삭제. [G&W p.58]
- **AUMC/MRT/effective half-life**: M1/M3/M5에서 필요한 식만 보존. [G&W pp.63–64; R&T pp.629–630]
- **Takada/Colburn time-dependent volume models**: M4의 5종 비교표에만 둔다. [G&W pp.66–67, 513–517]
- **Infusion/extravascular/urine data**: route/input extension으로만 언급. [G&W pp.72–77; R&T pp.624–639]
- **PK7 model discrimination**: F-test/AIC/precision/residual/simplest adequate model rule을 M4 한계와 §8에 압축 통합. [G&W pp.505–512]
- **PD response sections**: 현재 세션에서는 제외. Ch.19 후반부는 PD/effect 세션으로 넘긴다. [R&T pp.643–656]

### 제외 / 후속 세션

- Albumin binding, $f_u/f_{u,T}$, membrane partitioning 상세: distribution determinants 세션으로 이동.
- Hemodialysis rebound / lithium redistribution: clinical redistribution 세션으로 이동.
- Full NONMEM debugging tree, PBPK/QSP, TMDD: 후속 실무 세션으로 이동.
- FDA guidance 직접 인용: 본 PDF source 밖이므로 여기서는 `[외부 근거 필요]`로만 남긴다.

---

## 4A-1. Adjudication Table Summary

### Verdict count

| Source | ADOPT | PARTIAL_ADOPT | REJECT | Carry-forward |
|---|---:|---:|---:|---:|
| Audit v1 T1–T5 + Patch Memo | 68 | 23 | 6 | — |
| Audit v1 T6 Figure Inventory | — | — | — | 전체 Phase 4C로 이관 |
| Crucible v1 | 12 | 12 | 4 | — |

### Audit v1 — T1 Equation/Numerical Audit

| Source | Item | Verdict | Rationale |
|---|---|---|---|
| Audit T1 | Bi-exponential IV bolus 식 | ADOPT | G&W Eq.2:117 및 R&T Eq.19-2와 일치하므로 핵심식으로 유지. |
| Audit T1 | Half-life 식 | ADOPT | G&W Eq.2:118–2:119와 일치. |
| Audit T1 | Residual method | ADOPT | G&W Fig.2.43 및 R&T aspirin residual procedure와 일치. |
| Audit T1 | G&W Fig.2.43 수치 | PARTIAL_ADOPT | 수치는 유지하되 source 단위 혼재 가능성을 `[단위 확인 필요]`로 표시. |
| Audit T1 | $C_0=A+B$ | ADOPT | zero-time intercept validation으로 유지. |
| Audit T1 | $AUC=A/\alpha+B/\beta$ | ADOPT | G&W/R&T 모두 support. |
| Audit T1 | $AUMC=A/\alpha^2+B/\beta^2$ | ADOPT | G&W/R&T 모두 support. |
| Audit T1 | Fractional areas $f_1,f_2$ | ADOPT | elimination phase 판단의 핵심으로 유지. |
| Audit T1 | “fractional area determines elimination phase” | ADOPT | Fig.2.45/Table 2.4 및 R&T pp.622–623 메시지와 일치. |
| Audit T1 | 2-compartment ODE amount equations | ADOPT | R&T Eq.19-4–19-5 및 G&W ODE formulation과 일치. |
| Audit T1 | Eigenvalue explanation | PARTIAL_ADOPT | source explicit는 아니므로 `[수학적 해석]` tag로 유지. |
| Audit T1 | $\alpha+\beta$, $\alpha\beta$ 관계 | ADOPT | G&W Eq.2:124–2:125 및 R&T Table 19-1과 일치. |
| Audit T1 | Macro→Micro formulas | ADOPT | G&W Eq.2:121–2:129와 일치. |
| Audit T1 | $Cld=k_{12}V_c=k_{21}V_t$ | PARTIAL_ADOPT | 유지하되 R&T equation number claim은 제거. |
| Audit T1 | $CL=k_{10}V_c$ | ADOPT | R&T p.618/Table 19-1 및 G&W physiological model과 일치. |
| Audit T1 | NONMEM ADVAN3/TRANS4 code | PARTIAL_ADOPT | PDF source가 아니므로 `[실무 확장: NONMEM implementation]`로 격리. |
| Audit T1 | TRANS3 vs TRANS4 covariance claim | PARTIAL_ADOPT | 상세 fallback은 삭제하고 source 외 실무 노트 1문장만 유지. |
| Audit T1 | 2-compartment 4 DOF 혼합표현 | ADOPT | 오류이므로 source parameter sets로 수정. |
| Audit T1 | plasma data alone structural non-identifiability | ADOPT | G&W Fig.2.46/R&T pp.618–619와 일치. |
| Audit T1 | $V_1=Dose/(A+B)$ | ADOPT | R&T Eq.19-3 및 G&W Eq.2:129와 일치. |
| Audit T1 | $V_\beta=CL/\beta=Dose/(AUC\cdot\beta)$ | ADOPT | R&T Eq.19-11 및 G&W Vz discussion과 일치. |
| Audit T1 | $V_{ss}=MRT\cdot CL=Dose\cdot AUMC/AUC^2$ | ADOPT | G&W/R&T와 일치. |
| Audit T1 | $V_{ss}=V_1(1+k_{12}/k_{21})$ | PARTIAL_ADOPT | central elimination only/standard 2-comp assumption 명시. |
| Audit T1 | malformed $V_{ss}$ ellipsis formula | ADOPT | 삭제하고 source-supported 식만 남김. |
| Audit T1 | $V_1\le V_{ss}\le V_\beta$ | PARTIAL_ADOPT | 표준 source assumption 아래에서만 사용. |
| Audit T1 | Aspirin biexponential | ADOPT | R&T p.616 source와 일치. |
| Audit T1 | Aspirin one-compartment values | PARTIAL_ADOPT | $CL=0.98$ L/min 또는 980 mL/min으로 표기 정리. |
| Audit T1 | Aspirin two-compartment CL | ADOPT | $CL=683$ mL/min 유지. |
| Audit T1 | Aspirin “clearance 30% off” | PARTIAL_ADOPT | 방향을 명확화: terminal-only one-compartment CL은 true CL보다 약 44% overestimate. |
| Audit T1 | Aspirin “dose calculations underestimated” | ADOPT | 오류이므로 “maintenance dose 과대평가/고정용량 exposure underprediction”으로 수정. |
| Audit T1 | Aspirin $V_1/V_{ss}/V_\beta$ 및 $f_1/f_2$ | ADOPT | R&T source와 일치. |
| Audit T1 | Salicylic acid V values | ADOPT | R&T p.629–630과 일치. |
| Audit T1 | Gentamicin V values/half-lives/$f_2$ | ADOPT | R&T pp.630, 632, 635–636과 일치. |
| Audit T1 | Gentamicin accumulation index 16 | ADOPT | Fig.19-14 narrative와 일치. |
| Audit T1 | Gentamicin Vβ-based toxicity/inefficacy causal claim | PARTIAL_ADOPT | 교과서 직접 claim이 아니므로 `[실무 추론]`으로 낮춤. |
| Audit T1 | slowly equilibrating tissue amount 식 | ADOPT | R&T Eq.19-30과 일치. |
| Audit T1 | Nicardipine plateau values | ADOPT | R&T Fig.19-10/p.631과 일치. |
| Audit T1 | Eq.19-26 plateau equation | ADOPT | R&T Eq.19-26/19-27과 일치. |
| Audit T1 | “5 half-lives to plateau” generic claim | PARTIAL_ADOPT | source-aligned 50%/90% 표현으로 수정. |
| Audit T1 | “항상 빗나간다” | ADOPT | 과장 표현 삭제 및 $f_2$/context dependent로 완화. |
| Audit T1 | Effective half-life $\ln2\cdot MRT$ | ADOPT | G&W Eq.2:139와 일치. |
| Audit T1 | effective half-life as “true elimination-oriented” | PARTIAL_ADOPT | `[해석]` tag를 붙여 과잉 source claim 방지. |
| Audit T1 | PK8 condition number table values | ADOPT | Table 8.1 값 유지. |
| Audit T1 | PK8 range 29.69–4,104 | ADOPT | 오류이므로 29.69–3,186으로 수정. |
| Audit T1 | “200배 진폭” | ADOPT | 오류이므로 약 107배/약 100배 이상으로 수정. |
| Audit T1 | condition number >1000 threshold | PARTIAL_ADOPT | PDF source 밖이므로 `[실무 기준]`으로만 유지. |
| Audit T1 | NDA Deficiency Letter direct trigger | PARTIAL_ADOPT | source 밖이므로 `[실무 추론] regulatory review risk`로 낮춤. |
| Audit T1 | FDA guidance recommends physiological parameterization | REJECT | supplied PDF source 밖이고 본 세션 핵심에 필수 아님. |
| Audit T1 | Takada equation | ADOPT | G&W Eq.2:150–2:151/PK8와 일치. |
| Audit T1 | Colburn equation | ADOPT | G&W Eq.2:152–2:153/PK8와 일치. |
| Audit T1 | CL reparameterized model | ADOPT | G&W Eq.2:148–2:149/PK8와 일치. |
| Audit T1 | PK7 condition values | PARTIAL_ADOPT | 4,104는 PK7 tri-exponential 맥락으로만 표기. |
| Audit T1 | PK8 NCA fallback | ADOPT | M4 limitation에 추가. |

### Audit v1 — T2 Examples & Data Audit

| Source | Item | Verdict | Rationale |
|---|---|---|---|
| Audit T2 | G&W Fig.2.39 | ADOPT | mono/bi/multi-exponential decline의 도입 개념으로 1문장 유지. |
| Audit T2 | Catenary vs mammillary | PARTIAL_ADOPT | 구분은 유지, source 밖 analogy는 삭제. |
| Audit T2 | Fig.2.42 central/peripheral/urine profiles | ADOPT | tissue별 time course 차이를 M1에 압축 반영. |
| Audit T2 | Fig.2.43 residual method | ADOPT | M1의 핵심 anchor. |
| Audit T2 | Fig.2.45/Table 2.4 fractional AUC | ADOPT | M1/M5의 핵심 anchor. |
| Audit T2 | Fig.2.46 non-identifiability | ADOPT | M2 assumption/risk에 반영. |
| Audit T2 | SHAM Table 2.5 | REJECT | NCA reference로는 유용하나 10분 handout의 핵심이 아님. |
| Audit T2 | §2.4.3 reparameterization | ADOPT | M4 핵심. |
| Audit T2 | Fig.2.47 time-dependent volume | ADOPT | M3/M4 직관으로 1문장 유지. |
| Audit T2 | Fig.2.48/2.49 physiological ODE | ADOPT | M2/M4 핵심. |
| Audit T2 | Fig.2.50 partition/SS equality caveat | ADOPT | M2/M3 가정에 1문장 추가. |
| Audit T2 | Constant-rate infusion | PARTIAL_ADOPT | detailed derivation은 제외, M5 route extension으로만 유지. |
| Audit T2 | Extravascular administration | PARTIAL_ADOPT | 상세식 제외, context 한 줄만 유지. |
| Audit T2 | Plasma + urine data | PARTIAL_ADOPT | 상세식 제외, route/data extension으로만 유지. |
| Audit T2 | PK7 Part I | ADOPT | model discrimination warning으로 M4/§8에 추가. |
| Audit T2 | PK7 AIC/F-test | ADOPT | simplest adequate model rule로 반영. |
| Audit T2 | PK8 Compound X | ADOPT | M4의 quantitative anchor. |
| Audit T2 | PK8 NCA fallback | ADOPT | M4 limitation에 추가. |
| Audit T2 | Thiopental dog example | ADOPT | distribution kinetics direct evidence로 유지. |
| Audit T2 | Thiopental numeric details | PARTIAL_ADOPT | partition/fat/Vd 직관만 1문장 추가. |
| Audit T2 | Zoledronic acid/azithromycin | REJECT | 흥미롭지만 현재 10분 handout 범위 초과. |
| Audit T2 | Aspirin example | ADOPT | 오류 방향 수정 후 M1/M3/§7 유지. |
| Audit T2 | Aspirin V comparison | ADOPT | M3 핵심. |
| Audit T2 | Digoxin oral nose | PARTIAL_ADOPT | input/absorption bridge로만 유지. |
| Audit T2 | Midazolam-like short infusion | PARTIAL_ADOPT | “midazolam-like kinetics”로 정확히 완화. |
| Audit T2 | Long-term infusion stop/propofol-like schematic | REJECT | 세부 infusion topic으로 scope 밖. |
| Audit T2 | Fig.19-9 V1/V/Vss | ADOPT | M3 핵심. |
| Audit T2 | Endogenous tracer example | REJECT | 현재 handout 핵심 아님. |
| Audit T2 | Nicardipine example | ADOPT | M5 핵심. |
| Audit T2 | Fig.19-11 f2 spectrum | ADOPT | M5 핵심. |
| Audit T2 | Fig.19-12 tissue plateau | ADOPT | M5 limitation에 유지. |
| Audit T2 | Eptifibatide bolus+infusion | PARTIAL_ADOPT | practical context 1문장으로 유지. |
| Audit T2 | Gentamicin 8-hourly IM | ADOPT | M5 핵심. |
| Audit T2 | Oral regimen when effect wears off | PARTIAL_ADOPT | PD/oral regimen detailed discussion은 제외, context 한 줄. |
| Audit T2 | Fig.19-16 volume-term utility | ADOPT | Vss/Vβ 적용 조건으로 M5에 추가. |
| Audit T2 | Tobramycin renal impairment | ADOPT | altered clearance context로 유지. |
| Audit T2 | Renal simulation threshold | PARTIAL_ADOPT | renal impairment 강조 시에만 1문장; 숫자 남발 금지. |
| Audit T2 | Lithium/hemodialysis redistribution | REJECT | 별도 clinical redistribution 세션. |
| Audit T2 | PD response sections | REJECT | source range에는 있으나 현재 scope 밖. |

### Audit v1 — T3 Author Key Messages

| Source | Item | Verdict | Rationale |
|---|---|---|---|
| Audit T3 | One-compartment useful but inaccurate when distribution takes time | ADOPT | §1 Big Idea와 M1에 반영. |
| Audit T3 | Ignoring distribution kinetics can cause misinterpretation/dosage discrepancy | ADOPT | M1 aspirin 방향 수정 후 반영. |
| Audit T3 | Early rapid decline/effect changes as distribution evidence | ADOPT | M1/M5에 반영. |
| Audit T3 | Perfusion/permeability/partitioning determine distribution time | PARTIAL_ADOPT | M1/M3에 1문장 반영. |
| Audit T3 | Exponential terms define number of pools | ADOPT | M1 structural necessity에 반영. |
| Audit T3 | Compartment model not unique | ADOPT | M2 assumption/risk에 반영. |
| Audit T3 | Rate constants rarely directly physiologic | ADOPT | M2 warning에 반영. |
| Audit T3 | Elimination occurs at all times; CL=Dose/AUC | ADOPT | M1/M2에 반영. |
| Audit T3 | Terminal phase not always elimination phase | ADOPT | M1/M5/§5에 반영. |
| Audit T3 | V1, V/Vβ, Vss distinct | ADOPT | M3 핵심. |
| Audit T3 | Vss between V1 and V/Vβ | PARTIAL_ADOPT | standard assumptions 명시. |
| Audit T3 | Many drugs have f2>0.8 | ADOPT | “항상” 표현을 완화하는 데 사용. |
| Audit T3 | Plasma and tissue plateau can differ | ADOPT | M5에 반영. |
| Audit T3 | Vss/Vβ applicability during multiple dosing | ADOPT | M5에 Fig.19-16 rule 추가. |
| Audit T3 | Renal impairment affects first phase in aminoglycosides | ADOPT | Gentamicin/tobramycin context 유지. |
| Audit T3 | Terminal half-life loses simple application | ADOPT | M5 핵심. |
| Audit T3 | Clearance preferred over micro-constant elimination | PARTIAL_ADOPT | G&W source로만 설명, regulatory/NONMEM overclaim은 분리. |
| Audit T3 | PK7 model choice logic | ADOPT | M4/§8에 반영. |
| Audit T3 | PK8 WRSS vs condition number | ADOPT | M4 핵심. |
| Audit T3 | PK8 NCA fallback | ADOPT | M4 limitation. |

### Audit v1 — T4 Priority + Patch Memo

| Source | Item | Verdict | Rationale |
|---|---|---|---|
| Audit T4 #1 | PK8 range 29.69–4,104 | ADOPT | 29.69–3,186으로 수정. |
| Audit T4 #2 | 200배 진폭 | ADOPT | 약 107배로 수정. |
| Audit T4 #3 | Aspirin dose-risk direction | ADOPT | one-compartment CL overestimate 방향으로 수정. |
| Audit T4 #4 | malformed Vss formula | ADOPT | 삭제 및 source 식만 사용. |
| Audit T4 #5 | “항상 빗나간다” | ADOPT | source-consistent wording으로 완화. |
| Audit T4 #6 | NDA Deficiency Letter 직접 사유 | PARTIAL_ADOPT | `[실무 추론] review risk`로 낮춤. |
| Audit T4 #7 | NONMEM/FDA/PIPET source-like claims | PARTIAL_ADOPT | source 밖 주장은 삭제 또는 명시 tag 부착. |
| Audit T4 #8 | 4 DOF 오류 | ADOPT | source parameter set으로 수정. |
| Audit T4 #9 | PK8 NCA fallback | ADOPT | M4 limitation 반영. |
| Audit T4 #10 | Fig.19-16 volume applicability | ADOPT | M5에 반영. |
| Audit T4 #11 | PK7 model discrimination | ADOPT | M4/§8에 반영. |
| Audit T4 #12 | Eigenvalue explanation | PARTIAL_ADOPT | `[수학적 해석]` tag. |
| Audit T4 #13 | catenary=EHC analogy | REJECT | supplied source 밖이고 핵심 아님. |
| Audit T4 #14 | Thiopental numeric details | PARTIAL_ADOPT | Vd 예측 직관에 필요한 수치만 1문장. |
| Audit T4 #15 | PD response sections | REJECT | current session scope 밖. |
| Patch Memo | Condition number max 3,186 | ADOPT | Audit confirmed. |
| Patch Memo | Aspirin direction | ADOPT | Audit confirmed. |
| Patch Memo | NDA wording | PARTIAL_ADOPT | 실무 추론으로 downgrade. |
| Patch Memo | Eigenvalue tag | PARTIAL_ADOPT | 삭제 없이 tag 분리. |
| Patch Memo | NONMEM implementation link | PARTIAL_ADOPT | future/implementation note로만 유지. |
| Patch Memo | “항상” softening | ADOPT | Audit confirmed. |

### Audit v1 — T5 Coverage Audit

| Source | Item | Verdict | Rationale |
|---|---|---|---|
| Audit T5-A | G&W §2.4–2.4.3 | ADOPT | 2구획 본체와 reparameterization core. |
| Audit T5-A | G&W §2.4.4–2.4.6 | PARTIAL_ADOPT | route/input/data extensions로 압축. |
| Audit T5-A | G&W §2.5 edge | REJECT | CL 개념은 이미 충분하며 scope edge. |
| Audit T5-A | PK7 | ADOPT | model discrimination bridge로 반영. |
| Audit T5-A | PK8 | ADOPT | M4 core. |
| Audit T5-A | R&T distribution evidence/bolus/compartment/parameters | ADOPT | M1–M3 core. |
| Audit T5-A | R&T infusion/multiple dosing/altered clearance | PARTIAL_ADOPT | M5 임상 파급만 유지. |
| Audit T5-A | R&T redistribution/PD sections | REJECT | separate clinical redistribution/PD session. |
| Audit T5-B | G&W Eq.2:117–2:145 | ADOPT | M1–M3 core. |
| Audit T5-B | G&W Eq.2:146–2:165 | PARTIAL_ADOPT | reparameterization과 partition caveat만 유지. |
| Audit T5-B | G&W Eq.2:166–2:180 | PARTIAL_ADOPT | route/input extension으로만 유지. |
| Audit T5-B | G&W PK7 Eq.7 | PARTIAL_ADOPT | model discrimination principle만 유지. |
| Audit T5-B | G&W PK8 Eq.8 | ADOPT | M4 core. |
| Audit T5-B | R&T Eq.19-1–19-30 | PARTIAL_ADOPT | 2구획, V terms, plateau, tissue accumulation core만 유지. |
| Audit T5-B | R&T later PD equations | REJECT | out of scope. |
| Audit T5-C | G&W figures/tables core | PARTIAL_ADOPT | content anchor만 보존; Phase 4C에서 시각화 처리. |
| Audit T5-C | R&T figures/tables core | PARTIAL_ADOPT | 내용 반영하되 Figure markers는 삽입하지 않음. |

### Crucible v1 — P1/P3/Tips/Compression/Priority Matrix

| Source | Item | Verdict | Rationale |
|---|---|---|---|
| Crucible T1-a1 | Eigenvalue 제약식 운영 의미 | PARTIAL_ADOPT | `[수학적 해석]`으로 1문장만 추가. |
| Crucible T1-a2 | Fractional area를 그래프에서 즉시 읽는 훈련 | ADOPT | M1/M5에 knee/area/terminal-straightness checklist 추가. |
| Crucible T1-a3 | V1/Vss/Vβ 사전 예측 직관 | PARTIAL_ADOPT | thiopental 수치 기반 1문장으로 M3에 반영. |
| Crucible T1-b | Covariate model building에서 5개 카드 동시 활성화 | ADOPT | §1 항법도 직후에 추가. |
| Crucible T1-c1 | OFV/RSE signal | PARTIAL_ADOPT | §8 Professional moat에 source 밖 실무 신호로 1문장. |
| Crucible T1-c2 | CWRES vs TIME slope signal | PARTIAL_ADOPT | §8에 1문장. |
| Crucible T1-c3 | η-shrinkage >30% | PARTIAL_ADOPT | external practice로만 표시. |
| Crucible T1-c4 | WRSS + condition number simultaneous read | ADOPT | M4에 반영; >1000 threshold는 `[실무 기준]`. |
| Crucible T2-a risk1 | central elimination assumption reporting | ADOPT | M2 assumptions에 explicit reporting caveat. |
| Crucible T2-a risk2 | Vss reporting convention/FDA guidance | REJECT | PDF source 밖이며 직접 인용 불가. |
| Crucible T2-a risk3 | PK7 model discrimination as practical risk | ADOPT | M4/§8 반영. |
| Crucible T2-b1 | Phantom V2 | ADOPT | §8 failure mode에 압축 통합. |
| Crucible T2-b2 | Macro Drift | PARTIAL_ADOPT | §8 failure mode 1문장. |
| Crucible T2-b3 | Initial Estimate Trap | ADOPT | M4 limitation/§8에 반영. |
| Crucible T2-c | Effective vs terminal half-life critical blow | ADOPT | §5 혼동쌍 #4에 Critical Blow 행 추가. |
| Crucible T3 tip1 | Residual method not production NONMEM algorithm | ADOPT | M1 trench tip으로 반영. |
| Crucible T3 tip2 | Debugging order: initial values before reparameterization | ADOPT | M4 trench tip으로 반영. |
| Crucible T3 tip3 | “terminal? effective?” lab rule | ADOPT | §5 #4 기억 고리에 반영. |
| Crucible T3 tip4 | RSE before condition number | PARTIAL_ADOPT | M4 limitation에 source 외 실무 note로 반영. |
| Crucible T3 tip5 | Sparse design Phantom V2 | ADOPT | §8 failure mode에 반영. |
| Crucible T4 delete | M1 §F L1 duplicate | ADOPT | 삭제. |
| Crucible T4 compress | M2 §C 4 DOF duplicate | ADOPT | 1문장으로 압축. |
| Crucible T4 compress | M2 NONMEM TRANS3/TRANS4 detail | ADOPT | 2문장 이하로 축소. |
| Crucible T4 compress | M3 five layers | ADOPT | 삭제/압축. |
| Crucible T4 delete | M4 F L1/L3 | ADOPT | 삭제. |
| Crucible T4 delete | M5 F L1/L3 | ADOPT | 삭제. |
| Crucible T4 compress | §5 Macro vs Micro | ADOPT | 1 row로 압축. |
| Crucible T4 compress | §5 effective vs terminal | ADOPT | Critical Blow만 남기고 압축. |
| Crucible T4 replace | §7 Q3 | ADOPT | 적용 질문으로 대체. |
| Crucible T4 compress | §8 duplicate ADVAN/COV | ADOPT | 압축. |
| Crucible Grade C | 추가 NONMEM debugging tree | REJECT | separate session. |
| Crucible Grade C | PBPK/QSP expansion | REJECT | scope creep. |
| Crucible Grade C | FDA guidance direct citation | REJECT | source 밖. |
| Crucible Grade C | TMDD Apex expansion | REJECT | 후속 세션. |

---

## §1 — Session Header & Roadmap

**Session 05 · 2구획 모델: 이중지수 분해와 α·β 재파라미터화**

<!-- MASTER LENS -->
**Big Idea:** 2구획 모델은 “곡선이 두 번 꺾인다”는 관찰을 $A,\alpha,B,\beta$라는 macro-constant로 분해한 뒤, 이를 $CL,Q,V_1,V_2$ 또는 $V_c,CL,Cld,V_t$처럼 해석 가능한 좌표계로 다시 옮기는 기술이다. 이 좌표계 선택은 단순 notation 문제가 아니라, clearance 추정, volume 해석, covariance stability, multiple-dosing simulation을 동시에 바꾼다. [G&W pp.59–71; R&T pp.615–641]

**개념 항법도:**

```text
M1. 이중지수 + 잔차법
       ↓  두 지수항의 slope/intercept는 무엇을 뜻하는가?
M2. Macro ↔ Micro ↔ Physiological 좌표계
       ↓  어느 좌표계의 V를 임상·모델에 쓸 것인가?
M3. V₁ / Vss / Vβ
       ↓  용적 혼동이 loading dose, amount in body, tissue accumulation을 어떻게 왜곡하는가?
M4. 재파라미터화 5종 + condition number
       ↓  같은 curve라도 왜 어떤 parameterization은 안정하고 어떤 것은 불안정한가?
M5. 분포속도론의 임상 파급
       ↓  terminal half-life가 언제 유용하고 언제 위험한가?
```

<!-- ANCHOR -->
**Workflow anchor:** PopPK covariate model building의 forward inclusion 단계에서는 다섯 카드가 동시에 켜진다. $f_2$는 신기능 변화가 어느 phase를 바꿀지 예측하고(M1/M5), 좌표계는 covariate를 $CL$에 붙일지 $\beta$에 붙일지 결정하며(M2), $V_{ss}$와 $V_\beta$ 구분은 체중·tissue amount 해석을 좌우하고(M3), condition number/RSE는 covariate model을 deployable하게 유지할지 판단한다(M4). [실무 통합]

**선행 지식:** 1구획 IV bolus, $AUC=Dose/CL$, $V_d=CL/k$, MRT/AUMC, linear ODE.

**후속 지식:** NONMEM ADVAN3/4/11/12 선택, sparse sampling design, $\eta$-shrinkage 해석, 3구획 모델, tissue/target-site PK, clinical multiple-dosing simulation.

<!-- RECAP -->
**이 세션의 한 줄 회수:** 2구획 모델의 본질은 “두 지수항을 외우는 것”이 아니라, **곡선 분해 → 좌표계 변환 → volume 선택 → dosing 해석**을 한 번에 연결하는 것이다.

---

## §2 — Concept Anatomy Cards

### Card M1 — 이중지수 방정식과 잔차법(Method of Residuals)

<!-- MASTER LENS -->
**개념 Big Idea:** IV bolus 뒤 plasma curve가 semilog plot에서 하나의 직선이 아니라 두 직선의 합으로 보이면, early phase는 주로 distribution + 일부 elimination, terminal phase는 느린 return/distribution process와 elimination의 합성 결과로 해석해야 한다. 2구획 분석은 이 curve를 “두 phase의 합”으로 분해하는 데서 시작한다. [G&W pp.59–60; R&T pp.615–616]

**Formal definition:**

$$C(t)=A\cdot e^{-\alpha t}+B\cdot e^{-\beta t},\qquad \alpha>\beta>0$$

$A,B$는 zero-time intercept, $\alpha,\beta$는 phase slope의 절댓값이다. Semilog plot에서 기울기는 각각 $-\alpha$, $-\beta$이고, $C_0=A+B$다. [G&W pp.59–60; R&T pp.615–617]

**잔차법의 핵심 절차:** terminal $\beta$-phase를 먼저 log-linear regression으로 외삽하여 $B e^{-\beta t}$를 얻고, 초기 관측치에서 이를 빼서 residual curve $C_{resid}(t)=C_{obs}(t)-B e^{-\beta t}$를 만든다. 이 residual이 semilog에서 직선이면 그 기울기가 $-\alpha$, 절편이 $A$다. [G&W p.60; R&T p.616]

**G&W Fig.2.43 anchor:** $A\approx70$, $B=28$, $\alpha=\ln(70/10)/130=0.0150\ \text{min}^{-1}$, $\beta=\ln(28/10)/450=0.00229\ \text{min}^{-1}$로 제시된다. Source figure/caption의 단위 표기가 혼재되어 보이므로 최종 시각화 단계에서는 `[단위 확인 필요]`를 유지한다. [G&W p.60]

**Secondary parameters:**

$$AUC_0^\infty=\frac{A}{\alpha}+\frac{B}{\beta},\qquad
AUMC_0^\infty=\frac{A}{\alpha^2}+\frac{B}{\beta^2}$$

$$t_{1/2,\alpha}=\frac{\ln2}{\alpha},\qquad t_{1/2,\beta}=\frac{\ln2}{\beta}$$

$$f_1=\frac{A/\alpha}{AUC},\qquad f_2=\frac{B/\beta}{AUC},\qquad f_1+f_2=1$$

$f_2$가 크면 terminal phase가 elimination interpretation에 가까워지고, $f_2$가 작으면 terminal slope는 elimination보다 redistribution을 더 반영할 수 있다. [G&W p.63; R&T pp.622–623]

<!-- TRENCH -->
**Trench tip:** 잔차법은 production NONMEM 알고리즘이 아니다. 종이에서 curve-stripping을 손으로 하는 이유는 simultaneous nonlinear regression에 넣을 initial estimate 감각을 얻기 위해서다. [실무 확장]

**Structural necessity:** 2구획 central/peripheral amount ODE는 다음과 같다.

$$\frac{dA_1}{dt}=-(k_{12}+k_{10})A_1+k_{21}A_2$$

$$\frac{dA_2}{dt}=k_{12}A_1-k_{21}A_2$$

[수학적 해석] 선형 상수계수 2×2 ODE의 해가 두 지수항의 합으로 나타나기 때문에, $\alpha$와 $\beta$는 이 system matrix에서 유래한다. 따라서 $\alpha+\beta=k_{12}+k_{21}+k_{10}$, $\alpha\beta=k_{21}k_{10}$ 관계가 생기며, macro 4개는 임의로 움직이는 4개 숫자가 아니라 micro-parameter space의 제약을 반영한다. [G&W pp.61–62; R&T pp.618–619]

**그래프를 볼 때 3초 checklist:** knee가 어디 있는가($\alpha/\beta$), 두 phase의 면적 비율이 어느 쪽으로 기우는가($f_1/f_2$), terminal line이 정말 직선인가(3구획 가능성). [G&W p.63; R&T p.632]

**Aspirin warning:** R&T의 aspirin 650 mg IV bolus 예시는 early sampling을 놓치면 terminal-only one-compartment 해석으로 $CL=0.98$ L/min을 얻게 되지만, biexponential 해석에서는 $CL=683$ mL/min이다. 즉 terminal-only one-compartment 해석은 CL을 약 44% overestimate하고, 이로부터 maintenance dose를 계산하면 과대평가 위험이 있다. [R&T pp.615–620]

**Boundary conditions:** linear kinetics, central에서의 빠른 mixing, distribution phase sampling, mammillary structure, central elimination assumption이 필요하다. 이 조건이 깨지면 bi-exponential fit은 가능해도 physiological interpretation은 흔들린다. [G&W pp.57–65; R&T pp.617–619]

<!-- RECAP -->
**Recap:** M1에서 기억할 것은 “$A,\alpha,B,\beta$를 구하라”가 아니라, **곡선을 phase별로 분해한 뒤 각 phase가 AUC와 elimination interpretation에 얼마나 기여하는지 읽는 것**이다.

---

### Card M2 — Macro ↔ Micro ↔ Physiological 3중 좌표계 변환

<!-- MASTER LENS -->
**개념 Big Idea:** 같은 2구획 curve는 세 좌표계로 표현된다. Macro는 curve description, micro는 ODE transition, physiological은 clearance/volume language다. 모델러가 실무에서 쓰는 것은 대개 physiological 좌표계지만, 그 정당성은 macro/micro 변환을 이해할 때 생긴다. [G&W pp.60–71; R&T pp.618–619]

| 좌표계 | Parameter set | 역할 |
|---|---|---|
| Macro | $A,\alpha,B,\beta$ | 관측 plasma curve의 두 지수항 표현 |
| Micro | $V_c,k_{10},k_{12},k_{21}$ | compartment ODE의 fractional rate constants |
| Physiological | $V_c,CL,Cld,V_t$ | clearance, distribution clearance, central/peripheral volume로 해석 |

**Core conversions:**

$$CL=k_{10}V_c$$

$$Cld=k_{12}V_c=k_{21}V_t$$

$$V_c=\frac{D_{iv}}{A+B}$$

$$k_{21}=\frac{A\beta+B\alpha}{A+B}$$

$$k_{10}=\frac{\alpha\beta}{k_{21}}$$

$$k_{12}=\alpha+\beta-k_{21}-k_{10}$$

[G&W pp.60–62, 68–71; R&T pp.618–619]

<!-- ANCHOR -->
**왜 4개인가:** M1에서 본 두 지수항은 curve를 설명하는 4개 자유도다. source-supported 4-parameter sets는 micro $(V_c,k_{10},k_{12},k_{21})$ 또는 physiological $(V_c,CL,Cld,V_t)$이며, 혼합표현 $(V_c,V_t,k_{10},k_{12})$를 독립 자유도처럼 쓰면 안 된다. [G&W pp.60–62, 71]

**비식별성의 핵심:** plasma biexponential curve만으로는 central elimination only, peripheral elimination only, both-compartment elimination을 구별할 수 없다. 통상 central elimination only model을 쓰는 이유는 생리적으로 그럴듯하기 때문이지, plasma data가 그것을 증명했기 때문이 아니다. [G&W p.65; R&T pp.618–619]

**Reporting caveat:** 보고서에서는 “elimination from central compartment only” 및 “peripheral compartment lumping” 가정을 명시해야 한다. tissue PK, large protein drugs, target-mediated elimination이 의심되는 경우에는 이 가정의 mechanistic justification이 필요하다. [R&T p.618–619; 실무 추론]

**NONMEM bridge:** `[실무 확장]` ADVAN3/TRANS4의 표준 표현은 $CL,V_1,Q,V_2$이며, $K=CL/V_1$, $K_{12}=Q/V_1$, $K_{21}=Q/V_2$로 ODE transition을 만든다. 이 코드는 supplied PDFs의 직접 내용이 아니므로 implementation note로만 둔다.

**Partition caveat:** physiological ODE에서 central/peripheral concentration이 steady state에서 같아진다는 표현은 partitioning이 없다는 가정 위에 있다. 실제 tissue concentration이 plasma와 다르면 서로 다른 distribution clearance 또는 partition coefficient가 필요하지만, 두 compartment 모두의 data 없이는 식별이 어렵다. [G&W p.70]

<!-- RECAP -->
**Recap:** M2의 실무 의미는 “macro를 micro로 바꾸는 공식 암기”가 아니라, **plasma curve만으로 식별되는 것과 가정으로 보충하는 것을 분리하는 능력**이다.

---

### Card M3 — V₁ / Vss / Vβ 3중 분포용적 체계

<!-- MASTER LENS -->
**개념 Big Idea:** 2구획에서 “volume of distribution”은 하나가 아니다. $V_1$은 bolus 직후 central dilution, $V_{ss}$는 distribution equilibrium에서 amount/C, $V_\beta$는 terminal slope와 CL로 계산되는 apparent terminal volume이다. 이 셋을 섞으면 amount in body, loading dose, tissue accumulation 해석이 흔들린다. [R&T pp.617, 628–630; G&W pp.63–65]

| Volume | Source-supported formula | 의미 | 주의 |
|---|---|---|---|
| $V_1$ | $V_1=Dose/(A+B)$ | initial dilution/central volume | bolus 직후 central + very rapidly equilibrating tissues |
| $V_{ss}$ | $V_{ss}=MRT\cdot CL=Dose\cdot AUMC/AUC^2$ | steady-state amount-to-plasma ratio | 표준 2구획 central elimination에서는 $V_{ss}=V_1(1+k_{12}/k_{21})$ |
| $V_\beta$ or $V$ | $V_\beta=CL/\beta=Dose/(AUC\cdot\beta)$ | terminal slope 기반 apparent volume | terminal slope가 distribution return에 지배되면 크게 부풀 수 있음 |

[G&W pp.63–65; R&T pp.617, 621–630]

**Ordering:** 표준 central-elimination 2구획 가정에서 $V_1\le V_{ss}\le V_\beta$로 생각할 수 있다. 하지만 이 부등식은 universal law가 아니라 source model assumption 안에서의 working rule이다. [R&T pp.629–630]

**Aspirin anchor:** aspirin은 $V_1=6.5$ L, $V_{ss}=10.4$ L, $V_\beta=13.7$ L로 차이는 있지만 치명적으로 벌어지지는 않는다. [R&T pp.617, 629–630]

**Gentamicin anchor:** gentamicin에서는 $V_1=14$ L, $V_{ss}=56$ L, $V_\beta=345$ L로 $V_\beta$가 $V_{ss}$보다 약 6배 크다. terminal half-life 87 hr는 plasma elimination half-life처럼 행동하지 않으며, 초기 phase half-life 약 4 hr가 therapeutic plasma concentration 조절에 더 중요해진다. [R&T pp.630, 635–641]

**Thiopental intuition:** R&T thiopental dog example에서 fat partitioning이 크고 adipose tissue가 total apparent Vd의 큰 몫을 차지하므로, lipophilicity·perfusion·partitioning 정보는 새 약물의 $V_{ss}/V_1$과 $V_\beta$ 부풀림을 사전에 의심하게 해주는 단서다. [R&T pp.614–615]

<!-- CONFUSION -->
**Plausible Fallacy:** “terminal slope가 가장 늦은 phase이므로 $V_\beta$가 가장 진짜 volume이다.”  
**Correction:** $V_\beta$는 terminal slope로 계산된 apparent volume이다. slowly equilibrating tissue에서 plasma로 돌아오는 속도가 terminal slope를 지배하면, $V_\beta$는 body amount를 직접 나타내는 volume이 아니라 terminal curve geometry의 산물이 된다. [R&T pp.628–630]

**Clinical use rule:** loading dose나 amount-at-steady-state 사고에는 $V_{ss}$가 더 적절하고, terminal phase extrapolation에는 $V_\beta$가 쓰인다. 다회투여 interval 내에서는 fluctuation이 작고 true steady state에 가까울 때 $V_{ss}$가 쓸 만하며, interval 말기 distribution equilibrium에 가까워진 뒤에는 $V_\beta$가 approximate amount estimate에 쓰일 수 있다. gentamicin-like case처럼 interval 내 distribution disequilibrium이 크면 둘 다 단순 적용하기 어렵다. [R&T pp.638–639]

<!-- RECAP -->
**Recap:** 2구획에서 volume을 묻는 질문에는 먼저 “어느 volume?”이라고 답해야 한다. $V_1$, $V_{ss}$, $V_\beta$는 서로 다른 질문에 대한 답이다.

---

### Card M4 — 재파라미터화 5종과 condition number

<!-- MASTER LENS -->
**개념 Big Idea:** 같은 biexponential data를 5개 parameterization으로 fit하면 WRSS는 비슷해도 parameter precision과 condition number는 크게 달라진다. 즉 model form이 같아도 좌표계가 estimation geometry를 바꾼다. [G&W pp.513–517]

**PK8 anchor:** Compound X 100 µg IV bolus data에서 G&W는 5가지 parameterization을 비교한다. Table 8.1의 condition number는 ODE model 29.69, Macro model 125.2, Colburn 2243, Reparameterized model 2306, Takada 3186이다. 따라서 PK8의 범위는 **29.69–3,186**이고, 최대/최소 비율은 약 **107배**다. [G&W pp.513–517]

| Model family | 핵심 parameterization | Content Lock 판단 |
|---|---|---|
| Macro | $A,\alpha,B,\beta$ | curve description에는 직관적이나 intercept/slope correlation 가능성 큼 |
| Takada | time-dependent $V(t)$ | WRSS가 낮아도 condition number가 큼 |
| Colburn | exponential approach of $V(t)$ | time-dependent volume intuition 제공 |
| Reparameterized CL model | $D_{iv},CL$ 포함 | clearance language로 bridge |
| ODE physiological | $CL,V_c,Cld,V_t$ | PK8에서 lowest condition number |

**Core lesson:** 가장 낮은 WRSS가 production model의 충분조건은 아니다. Takada model은 WRSS가 낮아도 condition number가 높고, ODE model은 condition number가 가장 낮다. [G&W p.516]

<!-- TRENCH -->
**Trench tip:** condition number가 폭증하면 좌표계부터 바꾸기 전에 THETA 초기치를 먼저 확인한다. 초기치가 자릿수부터 틀리면 좌표계와 무관하게 information matrix가 나빠질 수 있다. 디버깅 순서: initial estimate → log-domain parameterization → reparameterization. [실무 디버깅 순서]

**RSE caveat:** condition number는 parameter 간 정보 직교성을, RSE는 각 parameter 자체의 추정 신뢰성을 본다. PK8 Table 8.1에는 RSE가 없으므로 그 표만으로 production 결정을 끝내지 않는다. [실무 확장]

**PK7 model discrimination bridge:** G&W PK7은 mono/bi/tri-exponential discrimination에서 AIC/F-test, precision, correlations, residuals, simplest adequate model rule을 함께 보게 한다. 특히 weighting scheme이 다른 model을 단순 F-test로 비교하면 안 된다. [G&W pp.505–512]

**NCA fallback:** G&W PK8은 initial phase가 거의 보이지 않지만 배제할 수 없을 때 NCA가 제안될 수 있음을 언급한다. 이것은 “2구획 fit을 무조건 강행”하라는 세션이 아니라, data가 phase를 식별할 때만 parametric 2구획 해석을 신뢰하라는 경고다. [G&W p.517]

<!-- RECAP -->
**Recap:** M4에서 기억할 숫자는 “29.69–3,186” 자체보다, **fit이 비슷해 보여도 좌표계가 covariance geometry를 100배 이상 바꿀 수 있다**는 사실이다.

---

### Card M5 — 분포속도론의 임상 파급과 terminal half-life의 함정

<!-- MASTER LENS -->
**개념 Big Idea:** terminal half-life는 자주 유용하지만, distribution kinetics가 강할 때는 “약물이 사라지는 속도”가 아니라 “slow tissue에서 plasma로 돌아오는 속도”를 더 많이 반영할 수 있다. plateau 도달, tissue accumulation, renal impairment dosing은 $f_1/f_2$와 투여 방식까지 함께 봐야 한다. [R&T pp.631–641]

**Plateau equation:**

$$\frac{C(t)}{C_{ss}}=f_1(1-e^{-\alpha t})+f_2(1-e^{-\beta t})$$

$f_2$가 크면 terminal half-life가 plateau 도달을 대체로 설명한다. 반대로 $f_2$가 작으면 terminal half-life가 길어도 plasma plateau는 훨씬 빨리 접근할 수 있다. [R&T pp.631–633]

**Nicardipine anchor:** terminal half-life가 약 12 hr로 길지만, plasma concentration은 1 hr 안에 약 50% Css에 도달하고 약 15 hr에 90% Css에 도달한다. terminal half-life만 보고 loading dose 필요성을 판단하면 초기 과량 투여 위험이 생길 수 있다. [R&T p.631]

**Gentamicin anchor:** terminal half-life가 87 hr이어도 plasma therapeutic behavior는 약 4 hr 초기 phase에 의해 좌우된다. terminal term 기반 accumulation index는 16배가 될 수 있지만, 이것은 plasma peak/trough accumulation과 동일하지 않고 slowly equilibrating tissue accumulation을 말한다. [R&T pp.635–641]

**Tissue vs plasma plateau:** plasma가 plateau에 빨리 접근해도 slowly equilibrating tissue는 훨씬 늦게 접근할 수 있다. 따라서 response site가 peripheral/tissue 쪽이면 plasma half-life만으로 onset/duration을 해석하면 안 된다. [R&T pp.633–634]

**Multiple dosing volume rule:** fluctuation이 작고 true steady state에 가까울 때는 $V_{ss}$가 amount estimate에 유용하다. interval 말기 distribution equilibrium에 가까우면 terminal volume $V$도 approximation으로 쓰일 수 있다. 그러나 gentamicin-like 경우처럼 interval 전체가 distribution disequilibrium이면 어느 volume도 단순 amount calculator가 되지 않는다. [R&T pp.638–639]

**Softened warning:** “terminal half-life는 항상 틀린다”가 아니다. R&T는 많은 약물에서 $f_2>0.8$이면 terminal phase가 plateau/time-course를 잘 설명한다고 말한다. 핵심은 “terminal인지 effective인지, plasma인지 tissue인지, $f_2$가 얼마인지”를 확인하는 것이다. [R&T pp.631–641]

<!-- TRENCH -->
**Lab rule:** 누군가 “이 약물의 half-life는 X시간”이라고 말하면 바로 묻는다: “terminal? effective? plasma? tissue?” 둘이 다르면 multiple-dosing simulation이 달라진다. [실무 확장]

<!-- RECAP -->
**Recap:** M5의 실전 규칙은 **half-life 하나로 dosing을 말하지 말고, $f_1/f_2$, volume term, input pattern, sampling time을 같이 본다**는 것이다.

---

## §5 — Confusion Pairs & Critical Blow

### Pair 1 — Bi-exponential curve vs “two elimination processes”

<!-- CONFUSION -->
| Trap | Correction | Critical cue |
|---|---|---|
| 두 지수항을 두 개의 independent elimination pathway로 해석한다. | 두 지수항은 linear ODE system의 eigen-components다. elimination은 central clearance로 계속 일어나지만, observed phase는 distribution과 elimination의 합성 결과다. | $f_2$가 작으면 terminal phase를 elimination phase라 부르면 위험하다. [G&W p.63; R&T pp.622–623] |

### Pair 2 — $V_{ss}$ vs $V_\beta$ [Critical Blow]

<!-- CONFUSION -->
| Trap | Correction | Critical Blow |
|---|---|---|
| terminal slope로 계산한 $V_\beta$를 body amount/loading dose용 volume으로 쓴다. | steady-state amount 또는 loading dose 사고에는 $V_{ss}$가 더 가까운 volume이다. $V_\beta$는 terminal slope geometry의 산물이다. | Gentamicin: $V_\beta=345$ L, $V_{ss}=56$ L, $V_1=14$ L. $V_\beta$를 “진짜 body volume”처럼 쓰면 tissue redistribution과 plasma dosing을 혼동한다. [R&T pp.630, 635–641] |

### Pair 3 — Macro vs Micro vs Physiological parameterization

<!-- CONFUSION -->
| Trap | Correction |
|---|---|
| $A,\alpha,B,\beta$를 “모델 파라미터”로만 외우고 $CL,Q,V_1,V_2$와 별개로 생각한다. | Macro는 curve description, micro는 ODE transition, physiological은 interpretation/reporting 좌표계다. 같은 model이라도 좌표계가 condition number와 interpretability를 바꾼다. [G&W pp.60–71; R&T pp.618–619] |

### Pair 4 — Terminal half-life vs Effective/clinical half-life [Critical Blow]

<!-- CONFUSION -->
| Trap | Correction | Critical Blow |
|---|---|---|
| 논문에 half-life가 12 hr라고 적혀 있으면 plateau 도달에도 12 hr 단위를 그대로 적용한다. | terminal half-life인지, effective half-life인지, plasma/tissue 중 어디의 half-life인지 확인한다. | Nicardipine-style case: terminal $t_{1/2}\approx12$ hr이지만 50% Css는 약 1 hr. terminal half-life만 보고 loading dose를 권하면 초기 과량 투여 판단이 나올 수 있다. [R&T p.631] |

### Pair 5 — Better WRSS vs better model

<!-- CONFUSION -->
| Trap | Correction |
|---|---|
| WRSS가 가장 낮은 parameterization을 무조건 채택한다. | WRSS, residual pattern, precision/RSE, condition number, correlation, biological plausibility를 함께 본다. G&W PK8에서 ODE model은 lowest condition number이고, Takada는 낮은 WRSS에도 high condition number다. [G&W pp.513–517] |

<!-- RECAP -->
**Confusion recap:** 이 세션의 치명적 혼동은 모두 “curve geometry를 physiological truth로 바로 읽는 것”에서 생긴다. curve는 evidence이고, interpretation은 assumption과 좌표계를 통해 얻어진다.

---

## §7 — Self-Test Blocks

### Q1. Residual method reconstruction

<!-- SELF-TEST -->
G&W Fig.2.43에서 terminal phase를 외삽하여 $B=28$, $\beta=\ln(28/10)/450$를 얻었다. 초기 관측치에서 무엇을 빼야 $\alpha$ phase를 얻는가?

**Answer key:** 각 초기 관측치 $C_{obs}(t_i)$에서 $B e^{-\beta t_i}$를 뺀다. residual을 semilog plot에 다시 놓고 slope/intercept를 구하면 $\alpha$와 $A$가 나온다. [G&W p.60]

### Q2. Aspirin CL direction

<!-- SELF-TEST -->
Aspirin 650 mg IV bolus에서 terminal-only one-compartment 해석은 $CL=0.98$ L/min, biexponential 해석은 $CL=683$ mL/min이다. terminal-only 해석은 true CL을 과소평가하는가, 과대평가하는가?

**Answer key:** 과대평가한다. $0.98$ L/min은 683 mL/min보다 약 44% 높다. 따라서 maintenance dose 계산은 과대평가 위험이 있다. [R&T pp.615–620]

### Q3. Volume ratio application

<!-- SELF-TEST -->
Aspirin과 gentamicin 중 $V_\beta/V_{ss}$ 비율이 더 큰 약물은 무엇이며, 왜 중요한가?

**Answer key:** Gentamicin이다. Aspirin은 $13.7/10.4\approx1.3$이지만 gentamicin은 $345/56\approx6.2$다. 큰 비율은 terminal slope-derived volume을 steady-state amount volume처럼 쓰면 안 된다는 경고다. [R&T pp.629–641]

### Q4. Structural non-identifiability

<!-- SELF-TEST -->
동일한 biexponential plasma curve를 central elimination only, peripheral elimination only, both elimination model이 모두 설명할 수 있다. plasma data만으로 무엇을 결론낼 수 없나?

**Answer key:** elimination site를 식별할 수 없다. central elimination only는 보통 physiologic plausibility 때문에 선택되는 working assumption이며, tissue data나 mechanistic justification 없이 plasma curve만으로 증명된 것이 아니다. [G&W p.65; R&T pp.618–619]

### Q5. Terminal half-life trap

<!-- SELF-TEST -->
Nicardipine처럼 terminal half-life가 12 hr인데 1 hr에 50% Css에 도달하는 case에서 terminal half-life만으로 loading dose를 권하면 왜 위험한가?

**Answer key:** plateau approach가 terminal term만으로 결정되지 않고 $f_1/f_2$ 가중합으로 결정되기 때문이다. plasma는 이미 빠르게 올라가는데 terminal half-life만 보면 “너무 늦게 도달한다”고 오판하여 과도한 loading을 권할 수 있다. [R&T pp.631–633]

### Q6. PK8 model selection

<!-- SELF-TEST -->
PK8에서 Takada model은 WRSS가 낮고 ODE model은 condition number가 낮다. 어느 하나만 보고 결정하면 안 되는 이유는?

**Answer key:** WRSS는 fit residual 크기, condition number는 parameter estimation geometry를 본다. 둘 중 하나만 좋다고 deployable model은 아니다. PK8의 핵심은 “동일 데이터/비슷한 fit에서도 좌표계가 condition number를 크게 바꾼다”는 것이다. [G&W pp.513–517]

### Q7. Sparse design diagnosis

<!-- SELF-TEST -->
첫 sample이 distribution phase 이후에만 존재하는 sparse design에서 ADVAN3 TRANS4 fit 후 $V_2$ RSE >100%, ETA(V2) shrinkage >80%, early CWRES positive trend가 보인다. 가장 먼저 의심할 것은?

**Answer key:** “약물의 $V_2$가 진짜 작다”가 아니라 distribution phase가 data에 없어 $V_2$가 식별되지 않는 Phantom V2 상황을 의심한다. [실무 확장]

### Q8. Half-life lab rule

<!-- SELF-TEST -->
회의에서 누군가 “half-life가 87 hr이므로 8시간 간격 투여하면 plasma가 16배 축적된다”고 말한다. 무엇을 되물어야 하는가?

**Answer key:** terminal half-life인지 effective/plasma half-life인지, $f_2$가 얼마인지, 축적이 plasma인지 slowly equilibrating tissue인지 물어야 한다. Gentamicin-like case에서는 terminal term accumulation과 plasma therapeutic fluctuation을 구분해야 한다. [R&T pp.635–641]

<!-- RECAP -->
**Self-test recap:** 8개 질문을 모두 통과하면, 2구획 모델을 “공식”이 아니라 “모델 선택·volume 해석·dosing simulation의 사고 도구”로 사용할 준비가 된 것이다.

---

## §8 — Knowledge Graph, Failure Modes, and Professional Moat

### A. 이번 세션 직후 연결되는 지식

| Next node | 이 세션에서 가져가는 것 |
|---|---|
| NONMEM ADVAN3/4/11/12 | $CL,V_1,Q,V_2$ 좌표계가 macro/micro와 어떻게 연결되는지 이해 |
| Sparse sampling design | distribution phase sample 없이는 $V_2$, $Q$, $\alpha$ 식별이 약해짐 |
| Covariate model building | covariate는 보통 slope/half-life가 아니라 $CL,V,Q$ 같은 physiological parameter에 붙인다 |
| Multiple-dosing simulation | terminal half-life 하나가 아니라 $f_1/f_2$, input duration, $V_{ss}/V_\beta$를 같이 본다 |
| 3구획 model | biexponential이 residual에서 다시 휘면 tri-exponential 또는 deeper tissue compartment 의심 |

### B. Failure modes

| Failure mode | Signature | Preventive rule |
|---|---|---|
| **Terminal-only CL error** | early sampling 누락, 1-compartment CL overestimate | distribution phase sampling을 확보하고 biexponential 가능성 확인 |
| **Vβ-as-Vss error** | $V_\beta/V_{ss}$가 큰데 loading/amount 계산에 $V_\beta$ 사용 | amount/steady-state에는 $V_{ss}$ 우선, terminal extrapolation에는 $V_\beta$ |
| **Phantom V2** | sparse design, $V_2$ RSE >100%, ETA(V2) shrinkage >80% | “작은 $V_2$” 결론 전 distribution-phase identifiability 확인 |
| **Macro Drift** | $A/B$ high correlation, covariance instability | production에는 physiological parameterization 우선 고려 |
| **Initial Estimate Trap** | condition number 폭증, 초기치 변경만으로 결과 급변 | initial estimate → log-domain → reparameterization 순서로 디버깅 |
| **WRSS-only selection** | lowest WRSS model이 high condition number | residual, precision, condition number, biological plausibility를 함께 판단 |
| **F-test misuse** | weighting scheme 다른 model을 단순 F-test 비교 | PK7 rule: residual/precision/correlation/simplest adequate model을 함께 사용 |

### C. Professional moat — 30년차 모델러가 1분 안에 보는 것

1. Semilog curve의 knee와 terminal straightness를 보고 2구획/3구획 가능성을 가른다.  
2. $f_2$를 보고 terminal half-life가 clinical time scale을 대표할지 판단한다.  
3. $V_\beta/V_{ss}$ 비율로 terminal volume 오용 위험을 본다.  
4. WRSS가 낮아도 condition number/RSE/correlation이 나쁘면 production model로 보류한다.  
5. CWRES vs TIME이 early positive 또는 S-shaped pattern이면 structural misspecification 또는 missing distribution phase를 의심한다.  
6. $\eta$-shrinkage가 높으면 covariate effect의 해석 가능성을 낮게 본다. [실무 기준]

### D. Minimal practical algorithm

```text
1. Plot semilog C-time curve.
2. Early sampling이 distribution phase를 포착했는지 확인.
3. Bi-exponential 가능성이 있으면 A, α, B, β를 rough estimate.
4. AUC, f1, f2, V1, Vss, Vβ를 계산.
5. Vβ/Vss와 f2를 보고 terminal half-life 해석 가능성을 평가.
6. Physiological parameterization으로 CL, Q/Cld, V1, V2를 설정.
7. Fit 후 residual, RSE, correlation, condition number를 함께 확인.
8. Sparse design 또는 high shrinkage이면 V2/Q/covariate 해석을 보류.
9. Multiple dosing은 terminal half-life 하나가 아니라 f1/f2-weighted plateau equation으로 점검.
```

### E. Scope carry-forward to Phase 4C

- 원그림 임베드는 금지한다.
- Figure inventory는 Audit T6에서 이미 분리되었으므로 여기서는 marker를 삽입하지 않는다.
- Phase 4C에서는 Fig.2.43 residual method, Fig.2.46 non-identifiability, Table 8.1 condition number, R&T Fig.19-9/10/14/16의 pedagogical replacement schematic을 우선 검토한다.

<!-- RECAP -->
**Final recap:** 2구획 모델의 mastery는 $C=Ae^{-\alpha t}+Be^{-\beta t}$를 외우는 것이 아니다. 좋은 모델러는 그 식을 보고 곧바로 **sampling adequacy, CL bias direction, volume choice, condition number risk, half-life misuse**를 함께 읽는다.

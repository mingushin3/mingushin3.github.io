# 02_Content Lock v1 — 분포의 생물학: 막투과·분포용적·단백결합

> **Phase**: 4A Content Lock v1  
> **Source scope**: Rowland & Tozer 5e Ch.4 p.77–118 + Appendix B p.763–765 + Appendix C p.767–773 + Appendix D p.775–776 / Gabrielsson & Weiner 5e Ch.2 §2.9.3–2.9.5 p.163–169 + PK47 p.690–693  
> **Output rule**: Markdown text only. Figure inventory is not adjudicated here and flows to Phase 4C unchanged.  
> **Compression check**: Content Lock v1 is shorter than Step 1 Draft v0. Generic analogies, repeated warnings, unsupported regulatory phrasing, and source-outside numerical claims were deleted or tagged.

---

## Updated Curation Map

본 세션의 중심 질문은 하나다. **약물은 혈장 밖으로 얼마나 나가며, 그 양은 무엇이 결정하는가?** 답은 막투과 속도(M1), 분포 율속(M2), apparent volume의 수학 구조(M3), plasma binding(M4), tissue binding/Kp(M5), total vs unbound exposure 선택(M6)이 한 시스템으로 연결될 때만 보인다.

### MUST

| # | 개념 | Content Lock verdict |
|---|---|---|
| M1 | 막투과의 결정인자: size, lipophilicity, charge, transporters | **MUST 유지.** caffeine logP 오류와 “임상 1상 폐기 수십 건” claim 삭제. |
| M2 | 분포의 율속 단계: perfusion- vs permeability-rate limitation | **MUST 유지.** lymph flow는 `1–10 mL/min per 70 kg`로 정정. thiopental fat 평형 시간은 “several hours / after 3 h much remains” 수준으로 낮춤. |
| M3 | 분포용적의 수학 구조 **[Apex]** | **MUST 유지·강화.** Eq.4-8, 4-11~4-16, 4-25, 4-29, Eq.4-30/App.C를 연결하고 Fig.4-26의 Vu 감소 메시지를 추가. |
| M4 | 혈장단백결합과 fu의 농도의존성 | **MUST 유지·정정.** Curation Map의 잘못된 PK47 식 삭제. Eq.47:1~47:4는 본문 source-anchored data에서만 사용. |
| M5 | 조직결합과 Kp의 결정인자 | **MUST 유지·압축.** acidic phospholipid와 Kp의 관계는 유지하되 `r>0.85`, Rodgers-Rowland depth, 80% variance, one-digit Vd prediction 삭제. |
| M6 | 노출 지표 선택: total vs unbound | **MUST 유지·강화.** G&W equal-AUC warning, Fig.2.140, Fig.2.141, IND/NDA recommendation을 보존. 가상 FDA guidance/deficiency-letter wording 삭제. |

### CONTEXT

| 항목 | 처리 |
|---|---|
| Ionization & pH partition | M1에서 1문장 원칙 + pKa 범위만 유지. [R&T p.83, App.B pp.763–765] |
| Lymphatic/macromolecule distribution | M2의 permeability-limited 극단으로 1문장 유지. [R&T pp.95, 100–101] |
| Plasma-to-blood concentration ratio | M5에서 App.D 핵심식만 유지. [R&T pp.775–776] |
| Vd range | M3에서 “apparent V는 생리 부피를 초과할 수 있다”는 메시지로 유지하되 quinacrine/chloroquine exact value는 order-of-magnitude로 낮춤. [R&T p.103] |
| Exposure metrics table | M6에서 Cmax/AUC/td/treatment period 선택 논리로 유지. [G&W p.169] |

### REJECT / DELETE

- `Caco-2/PAMPA`, `Lipinski rule of 5`, `phase 1 진입 전 소실`, `매년 수십 건`, `FDA Guidance on PopPK Analyses`, `deficiency letter`, `Rodgers–Rowland 80% variance`, `one-digit Vd prediction`, `M5 r>0.85` exact correlation.
- T6 Figure Inventory는 본 문서에서 재판정하지 않음.
- SGLT2 inhibitor, activated charcoal, fexofenadine-grapefruit juice, toxicokinetics definition은 main flow에서 제외.

---

## Adjudication Table Summary

| Source | Item | Verdict | Rationale |
|---|---|---|---|
| Audit T1 | Eq.4-1, driving force, Eq.4-5~4-7, Eq.4-8, Eq.4-11~4-16, Eq.4-25, Eq.4-29, Eq.4-30/App.C, Eq.4-17~4-19, Eq.2:373 | ADOPT | PDF와 일치하며 본 세션의 수학 골격이므로 page tag와 함께 유지. |
| Audit T1 | M1 caffeine logP 2.0 claim | ADOPT | R&T Fig.4-4와 충돌하므로 caffeine은 logP≈0, lomustine은 logP≈2 부근으로 정정. |
| Audit T1 | vinblastine/vincristine “100배 낮음” | PARTIAL_ADOPT | P-gp substrate로 expected보다 낮다는 원문 메시지는 유지하되 정확한 배수는 “markedly lower / 시각 추정 [확인 필요]”로 낮춤. |
| Audit T1 | calcitonin-salmon size example | PARTIAL_ADOPT | full triad가 교육적으로 유용하므로 M1에 1문장만 추가. |
| Audit T1 | Caco-2/PAMPA, Lipinski, phase 1 screening claim | REJECT | 첨부 PDF 밖 실무 확장이며 10분 handout에는 불필요. |
| Audit T1 | “임상 1상 폐기 수십 건/년” | REJECT | 숫자성 claim이나 첨부 PDF 근거 없음. |
| Audit T1 | thiopental fat equilibrium 3.5 h | PARTIAL_ADOPT | Fig.4-13은 after 3 h에도 fat에 많이 남는다는 메시지이므로 exact 3.5 h 삭제. |
| Audit T1 | lymph flow 약 1 mL/min | ADOPT | 원문 caption의 `1–10 mL/min per 70 kg`로 정정. |
| Audit T1 | quinacrine/chloroquine exact V values | PARTIAL_ADOPT | Fig.4-19 visual scale 기반이므로 “생리 부피를 크게 초과하는 order-of-magnitude”로 압축. |
| Audit T1 | cephalosporin V vs fu, Vu vs fu | ADOPT | Fig.4-25와 Fig.4-26은 M3/M6 bridge의 핵심이므로 paired message로 반영. |
| Audit T1 | warfarin nephrotic syndrome | ADOPT | V, CL, t1/2, albumin 수치가 원문 table anchor이므로 유지. |
| Audit T1 | M4 Curation Map PK47 formula error | ADOPT | Curation Map에서는 식을 삭제하고 본문에서 Eq.47:1로 정정. |
| Audit T1 | `fub > 1` attribution | ADOPT | R&T p.106 attribution 삭제, G&W p.168로 source attribution 정정. |
| Audit T1 | albumin site I/II | REJECT | 첨부 PDF 밖 생화학 확장. |
| Audit T1 | M5 acidic phospholipid relationship | ADOPT | R&T Fig.4-24의 핵심 메시지로 유지. |
| Audit T1 | M5 `r>0.85`, propranolol visual range | PARTIAL_ADOPT | exact value는 삭제하고 “strong relationship / visual range”로 낮춤. |
| Audit T1 | Rodgers-Rowland, 80% variance, one-digit Vd prediction | REJECT | 첨부 PDF 밖 강한 PBPK claim. |
| Audit T1 | G&W Fig.2.134, Fig.2.140, Fig.2.141 | ADOPT | total vs unbound exposure의 핵심 근거. Fig.2.141 total potency fold는 approximate로만 처리. |
| Audit T1 | G&W Fig.2.136 equal-AUC warning | ADOPT | Draft에서 약했으므로 M6에 명시적으로 보강. |
| Audit T1 | Benet & Hoener 456 drugs, IND/NDA recommendation | ADOPT | G&W p.168–169의 author conclusion이므로 유지. |
| Audit T1 | FDA reviewer deficiency letter / FDA Guidance wording | REJECT | 첨부 PDF 범위 밖. “검토에서 active species 근거를 요구받을 수 있음”도 본문에는 넣지 않음. |
| Audit T1 | §7 Boss Dilemma lidocaine analog | PARTIAL_ADOPT | 교육용 가상 사례로만 남기고 실제 source-derived case처럼 표현하지 않음. |
| Audit T2 | INCLUDED_CORRECT examples | ADOPT | M1~M6에 page tag와 함께 보존하되 중복 설명은 압축. |
| Audit T2 | OMITTED_JUSTIFIABLE / LOW examples | REJECT | main flow를 흐리는 scope creep는 유지하지 않음. |
| Audit T3 | pH partition limitation | ADOPT | transporter/paracellular violation을 M1 limitation에 1문장 반영. |
| Audit T3 | equal-AUC warning underemphasized | ADOPT | M6 Big Idea와 §5 Critical Blow에 반영. |
| Audit T3 | unbound concentration as active comparator | ADOPT | M1 driving force, M4 fu, M6 AUCu를 관통하는 master lens로 유지. |
| Audit T4 | MUST_FIX #1–7 | ADOPT | 수식 오류, source attribution, external regulatory/PBPK claims는 모두 본문에서 수정·삭제. |
| Audit T4 | SHOULD_FIX #8–13 | ADOPT | exact visual estimates를 낮추고 Fig.2.136/Fig.4-26 메시지 보강. |
| Audit T4 | OPTIONAL #14–15 | PARTIAL_ADOPT | Caco-2/PAMPA/Lipinski는 삭제, calcitonin triad는 1문장만 채택. |
| Audit T4 | REJECT #16–17 | REJECT | SGLT2, charcoal, toxicokinetics는 current main flow 밖. |
| Audit T5 | Coverage elements included as MUST/CONTEXT | ADOPT | R&T/G&W 핵심 coverage 유지. |
| Audit Patch | Patch memo claims | ADOPT | M4 formula/title, M1 Big Idea, regulatory overreach, Rodgers-Rowland overreach 모두 패치. |
| Crucible T1 | Eq.C-13 “albumin ferry” intuition | ADOPT | M3 Big Idea에 1문장 비유로 통합. |
| Crucible T1 | Kp가 클수록 평형이 늦다는 직관 | ADOPT | M2에서 “채울 양이 커지고 공급은 제한된다”로 보강. |
| Crucible T1 | fuT vs active transporter boundary | ADOPT | M5 limitation에 통합. |
| Crucible T1 | NDA Module 2.7.2 / ICU phenytoin integration points | PARTIAL_ADOPT | source 밖 submission template은 배제하고 §8에서 “실무 연결”로 짧게만 처리. |
| Crucible T1 | 베테랑 즉각 직관 6개 | PARTIAL_ADOPT | 핵심 4개는 §8에 통합, allometric 일반론은 삭제. |
| Crucible T2 | Deficiency-letter scenarios | PARTIAL_ADOPT | 가상 FDA wording은 삭제하고, “source 밖 방어 언어 금지” 원칙만 §7 주석으로 반영. |
| Crucible T2 | NONMEM error signatures 3개 | PARTIAL_ADOPT | Albumin covariate and PK47 misfit는 [교과서 외 실무 해석]으로 압축, Vss vs Vβ는 1문장만. |
| Crucible T2 | fu constant vs Cu-dependent downstream pair | ADOPT | §5 Critical Blow에 포함. |
| Crucible T3 #1 | Albumin Covariate Asymmetry | ADOPT | M3 Trench tip으로 반영하되 교과서 외 실무 해석 표시. |
| Crucible T3 #2 | acidic/basic drug protein covariate choice | ADOPT | M4/M5 bridge에 짧게 반영하되 pKa heuristic은 [교과서 외 실무 해석]로 표시. |
| Crucible T3 #3 | saturable PPB vs saturable CL differential dx | PARTIAL_ADOPT | §7 self-test로 통합하여 본문 길이 증가 최소화. |
| Crucible T3 #4 | PPB method bias | PARTIAL_ADOPT | M4 limitation 1문장으로 유지하되 source 밖 실무 경고 표시. |
| Crucible T3 #5 | Vss vs Vβ confusion | PARTIAL_ADOPT | M3 limitation 1문장으로 유지하되 source 밖 실무 경고 표시. |
| Crucible T4 | D1–D11 deletion candidates | ADOPT | 자명한 analogy와 중복 sections 삭제·압축. |
| Crucible Grade C | Rodgers-Rowland depth, TMDD specifics, FDA/EMA guideline numbers, allometry card | REJECT | scope creep 또는 외부 문헌 영역. |

---

## §1 — Session Header & Roadmap

### Big Idea

<!-- MASTER LENS -->
분포용적은 실제 부피가 아니라 **amount in body를 concentration으로 나누기 위해 도입한 apparent proportionality constant**이다. 이 상수는 대체로 `plasma binding(fu)`가 약물을 혈장 쪽에 붙잡는 힘과 `tissue binding(fuT/Kp)`이 조직 쪽으로 끌어당기는 힘의 균형으로 결정된다. [R&T pp.102–111]

### Concept Navigation

```text
M1 막투과 결정인자
  → M2 분포 율속: perfusion-limited인가 permeability-limited인가?
  → M3 Vd의 수학 구조 [Apex]
  → M4 plasma binding과 fu 농도의존성
  → M5 tissue binding, Kp, transporter
  → M6 total vs unbound exposure 선택
  → §5 Critical Blow: C vs Cu
```

### Knowledge Graph Position

- 이전 세션의 `C(t) = (Dose/V)·e^{-kt}`에서 $V$가 무엇인지 해부하는 장이다.
- 다음 elimination 세션에서는 $f_u$가 well-stirred hepatic clearance 식의 분자로 들어간다.
- PopPK에서는 albumin, α1-AGP, renal/liver disease covariate가 `V`, `CL`, 또는 `fu`에 어떤 방향으로 연결되는지 판단하는 기반이 된다.

---

## §2 — Concept Anatomy Cards

---

### M1 · 막투과의 결정인자

<!-- MASTER LENS -->
**핵심 직관**: 막투과는 “lipophilic이면 통과한다”가 아니라 **size × lipophilicity × charge × transporter**의 곱이다. Eq.4-1의 $P$는 이 네 축과 막 구조가 합쳐진 macroscale permeability이다. [R&T pp.80–84, 85–90]

#### A. Formal Definition

막 양쪽 수성구획의 unbound 농도가 $Cu_1$, $Cu_2$일 때 net transport rate는 다음과 같다.

$$	ext{Net rate of transport}=P\cdot SA\cdot(Cu_1-Cu_2)$$

[출처: R&T Eq.4-1, p.80]

Bound drug은 일반적으로 막을 통과하지 못하므로 driving force는 total concentration $C$가 아니라 unbound concentration $Cu$이다. [R&T p.80]

#### B. Source-Anchored Details

- **Size**: 같은 lipophilicity에서 MW 400 → 800 g/mol로 증가하면 skin permeability는 약 300-fold 낮아진다. [R&T Fig.4-3, p.81–82] Atenolol 246 g/mol은 GI absorption이 가능하지만, oxytocin 1007 g/mol은 GI membrane을 거의 통과하지 못하고, calcitonin-salmon 3432 g/mol은 nasal absorption도 약 3% 수준이다. [R&T p.81]
- **Lipophilicity**: BBB permeability는 대체로 n-octanol/water partition coefficient가 증가할수록 증가한다. 단, vinblastine·vincristine은 lipophilicity만으로 기대되는 값보다 낮은 permeability를 보이는데, 원문은 P-glycoprotein efflux substrate임을 주요 이유로 든다. [R&T Fig.4-4, p.82] “100배” 같은 배수는 시각 추정 [확인 필요]로만 취급한다.
- **Charge / pH partition**: 약산·약염기에서는 un-ionized form이 lipoidal membrane을 주로 통과한다. 평형에서 un-ionized 농도는 같아질 수 있지만, pH와 pKa에 따라 total concentration은 달라진다. [R&T p.83; App.B pp.763–765]
- **Transporter**: passive facilitated transporter는 equilibrium 도달 속도를 바꾸고, active transporter는 steady-state unbound ratio 자체를 바꿀 수 있다. Active transport가 있을 때:

$$\frac{Cu_T}{Cu}=\frac{P_{uptake}}{P_{efflux}}$$

[출처: R&T Eq.4-26, p.110]

<!-- TRENCH -->
**Trench-Level Tip**: logP와 MW가 좋아도 P-gp/BCRP efflux substrate이면 BBB 또는 gut wall에서 effective permeability가 크게 낮아질 수 있다. 단, Caco-2/PAMPA, Lipinski rule은 이 source 범위 밖이므로 본 handout에서는 삭제한다.

<!-- ANCHOR -->
막을 통과하는 성질이 정해지면, 다음 질문은 “조직으로 가는 속도가 blood flow에 의해 제한되는가, membrane 자체에 의해 제한되는가?”이다.

---

### M2 · 분포의 율속 단계

<!-- MASTER LENS -->
**핵심 직관**: 조직 분포는 “얼마나 많이 가는가”와 “얼마나 빨리 가는가”를 분리해야 한다. Tissue affinity가 커질수록 equilibrium extent는 커지지만, 채워야 할 양이 커지므로 equilibrium time은 길어질 수 있다. [R&T pp.94–100]

#### A. Formal Definition

Perfusion-rate limited distribution에서는 membrane crossing이 충분히 빠르고, 조직으로 들어가는 공급 속도는 blood flow가 결정한다. Tissue concentration의 접근은 mono-exponential 형태를 따른다.

$$k_T=\frac{Q/V_T}{K_{pb}}$$

$$t_{1/2,distribution}=\frac{0.693\cdot K_{pb}}{Q/V_T}$$

$$C_T(t)=K_{pb}\cdot C_A\cdot(1-e^{-k_Tt})$$

[출처: R&T Eq.4-5~4-7, p.97]

#### B. Source-Anchored Details

| Tissue | Perfusion rate, mL/min/g | 해석 |
|---|---:|---|
| Lung | 10.0 | 매우 빠른 equilibrium 가능 |
| Kidney | 4.0 | flow-rich organ |
| Brain | 0.5 | flow는 높지만 BBB permeability가 별도 제한 가능 |
| Adipose | 0.025 | 매우 낮은 flow → high Kp 약물에서 늦은 equilibration |
| Inactive muscle | 0.025 | 큰 tissue mass + 낮은 perfusion |

[출처: R&T Table4-4, p.96]

- **Thiopental dog 25 mg/kg IV bolus**: brain은 빠르게 오르고 빠르게 빠지는 반면, fat은 low perfusion/high affinity 때문에 after 3 h에도 상당량이 남는다. exact “3.5 h equilibrium”은 author-stated value가 아니므로 삭제한다. [R&T Fig.4-13, p.94]
- **Macromolecule/lymphatic extreme**: large molecule은 혈관 벽 passage가 제한되며 lymphatic drainage가 중요한데, 원문 caption은 lymph flow를 `1–10 mL/min per 70 kg`로 제시한다. [R&T Fig.4-14, p.95] MW >5000 g/mol에서는 permeability limitation과 lymphatic return이 분포 속도를 크게 늦출 수 있다. [R&T Table4-1, p.84; Fig.4-14, p.95]
- **Ribitol and penicillin G**: small polar compound도 조직별 permeability에 따라 mixed limitation을 보이고, penicillin G는 muscle과 달리 brain/CSF에서 permeability limitation이 두드러진다. [R&T Fig.4-17 p.99; Fig.4-18 p.100]

#### C. Boundary Conditions

- Eq.4-5~4-7은 **perfusion-rate limited** 가정에서만 안전하다.
- permeability-rate limited tissue에서는 $Q$를 올려도 distribution rate가 비례해서 증가하지 않는다.
- High $K_{pb}$는 “많이 간다”와 동시에 “평형 도달이 늦다”를 의미할 수 있다.

<!-- RECAP -->
**M2 recap**: distribution half-life는 blood flow, tissue size, tissue affinity의 함수이다. 큰 $K_{pb}$와 낮은 $Q/V_T$가 만나면 distribution은 느려진다.

---

### M3 · 분포용적의 수학 구조 **[Apex Concept]**

<!-- MASTER LENS -->
**핵심 직관**: $V$는 약물이 차지한 실제 부피가 아니라 `Amount/C`이다. 작은 Vd의 albumin-bound 산성 약물에서는 albumin이 ferry처럼 약물을 plasma와 extravascular albumin space로 운반한다. $f_u\to0$이면 약물은 그 ferry에서 거의 내리지 않으므로, 약물의 apparent V는 albumin distribution volume인 약 7.5 L 근처에서 floor를 갖는다. [R&T pp.111–113; App.C pp.767–773]

#### A. Formal Definition

$$V=\frac{\text{Amount in body}}{C}=\frac{A}{C}$$

[출처: R&T Eq.4-8, p.102]

Tissue/plasma equilibrium ratio $K_p$를 쓰면:

$$A=V_p\cdot C+V_T\cdot K_p\cdot C$$

$$V=V_p+V_T\cdot K_p$$

$$V=V_p+\sum_i V_{T,i}\cdot K_{p,i}$$

[출처: R&T Eq.4-11~4-13, pp.103–104]

측정 matrix가 바뀌면 apparent volume도 달라진다.

$$V_u=\frac{A}{C_u},\qquad V_b=\frac{A}{C_b}$$

[출처: R&T Eq.4-14~4-15, p.104]

#### B. Binding-Based Structure

Plasma/tissue unbound fraction으로 쓰면:

$$V=V_p+V_{TW}\cdot\frac{f_u}{f_{uT}}$$

[출처: R&T Eq.4-25, p.109]

Transporter가 tissue distribution을 지배하면:

$$V=V_p+V_{TW}\cdot\frac{f_u}{f_{uT}}\cdot\frac{P_{uptake}}{P_{efflux}}$$

[출처: R&T Eq.4-29, p.111]

Small-Vd albumin-bound drug model에서는:

$$V=7.5+\left(7.5+\frac{V_R}{f_{uR}}\right)\cdot f_u$$

[출처: R&T Eq.4-30, p.112; App.C Eq.C-13, pp.767–773]

#### C. Source-Anchored Data Anchors

- Plasma 3 L, extracellular water 16 L, total body water 42 L는 V 해석의 physiologic anchor다. [R&T p.111]
- Albumin apparent distribution volume은 약 7.5 L이며, cephalosporin Fig.4-25에서 $f_u\to0$ extrapolation intercept가 약 7 L로 보인다. [R&T Table4-5 p.101; Fig.4-25 pp.112–113]
- 같은 cephalosporin series에서 $V$는 $f_u$와 함께 증가하지만, $V_u$는 $f_u$가 증가할수록 감소한다. 이 paired message가 “total concentration 기준 V”와 “unbound concentration 기준 V”가 같은 생리적 의미가 아님을 보여준다. [R&T Fig.4-25~4-26, p.113]
- Warfarin nephrotic syndrome 예시: albumin 43→12.5 g/L, V 9.4→13.7 L, CL 0.20→0.58 L/hr, t1/2 36→18 hr. [R&T Table4-12, p.118]
- Adalimumab 같은 high MW antibody는 V가 약 5–6 L로 작고, caffeine/alcohol처럼 small freely permeating molecule은 V가 total body water에 접근한다. [R&T p.111]

#### D. Apex Fallacy

“$f_u$가 증가하면 unbound concentration이 증가하므로 loading dose를 올려야 한다”는 직관은 small-Vd albumin-bound drug에서 틀릴 수 있다. 같은 amount에서 $f_u$가 증가하면 total $C$는 낮아지고 $V$는 증가하지만, $C_u$는 반드시 같은 방향으로 증가하지 않는다. R&T의 cephalosporin/warfarin 논리는 이 함정을 정면으로 다룬다. [R&T pp.112–118]

<!-- TRENCH -->
**[교과서 외 실무 해석] Albumin covariate asymmetry**: large-Vd drug에서 albumin을 `V` covariate로만 넣고 `CL` 쪽을 보지 않으면 total concentration 기준 CL 변화가 누락될 수 있다. ETA-CL vs albumin 관계가 ETA-V vs albumin보다 강하면 CL covariate도 검토한다.

**[교과서 외 실무 경고] Vss vs Vβ**: multi-compartment model에서 loading dose는 Vss 기반, terminal half-life 해석은 Vβ 기반이라는 구분을 유지한다.

<!-- RECAP -->
**M3 recap**: $V$는 `Vp + tissue term`이며, tissue term은 $K_p$ 또는 $f_u/f_{uT}$로 읽을 수 있다. Small-Vd albumin-bound drug에서는 albumin distribution volume이 floor를 만든다.

---

### M4 · 혈장단백결합과 fu의 농도의존성

<!-- MASTER LENS -->
**핵심 직관**: $f_u$는 고정 상수가 아니라 protein concentration, binding affinity, binding site 수, unbound concentration의 함수다. 따라서 “total concentration ↔ unbound concentration” 변환은 $f_u$가 일정하다는 검증 위에서만 안전하다. [R&T pp.105–108; G&W pp.690–693]

#### A. Formal Definition

$$f_u=\frac{C_u}{C}$$

[출처: R&T Eq.4-17, p.105]

Single binding site에서 association constant는:

$$K_a=\frac{C_{b,t}}{C_u\cdot P}$$

[출처: R&T Eq.4-18, p.105]

R&T의 mass-law relationship은 protein concentration과 binding site occupancy가 $f_u$를 바꾼다는 점을 보여준다.

$$f_u=\frac{1}{1+K_a\cdot f_{up}\cdot P_t}$$

[출처: R&T Eq.4-19, p.105]

#### B. PK47 Source-Anchored Data

G&W PK47은 $f_u$를 $C_u$, total protein concentration $[P_T]$, site number $n$, affinity $K_a$의 함수로 모델링한다.

$$f_u=1-\frac{1}{1+\frac{C_u}{n[P_T]}+\frac{1}{K_a\cdot n[P_T]}}$$

[출처: G&W Eq.47:1, p.691]

Low-$C_u$ approximation:

$$f_u\approx\frac{1}{1+K_a\cdot n[P_T]}$$

[출처: G&W Eq.47:3, p.692]

G&W는 Compound 1에서 $[P_T]=50$과 0.3, Compound 2에서 $[P_T]=10$과 0.1 조건을 사용하고, $n$은 대략 1–4 범위, $K_a$는 Eq.47:4 초기 추정으로 약 6 concentration units 수준을 제시한다. [G&W Table47.1 p.692; Eq.47:4 p.693]

#### C. Boundary Conditions

- Eq.47:1은 single binding-site class 모델이다. multiple site class가 있으면 residual pattern이 systematic하게 남을 수 있다.
- $AUCu=AUC\times f_u$는 $f_u$가 시간·농도에 대해 충분히 일정할 때만 안전하다. [G&W p.167]
- G&W는 `fub > 1`이 가능하다고 명시한다; 이는 bound/free ratio이므로 fraction bound와 혼동하면 안 된다. [G&W p.168]

<!-- TRENCH -->
**[교과서 외 실무 해석] Protein covariate choice**: acidic drug는 albumin, basic drug는 α1-AGP 변화에 먼저 주목한다. R&T Table4-9는 albumin과 α1-AGP가 disease state에 따라 달라질 수 있음을 보여준다. [R&T Table4-9, p.114]

**[교과서 외 실무 경고] PPB method bias**: equilibrium dialysis와 ultrafiltration은 method bias가 다를 수 있다. 이 문장은 PDF 원문이 아니라 실험 데이터 수령 단계의 실무 주의로만 사용한다.

<!-- RECAP -->
**M4 recap**: $f_u$는 protein concentration과 binding site saturation에 따라 변할 수 있다. total-to-unbound conversion은 $f_u$ constant assumption이 무너지면 함께 무너진다.

---

### M5 · 조직결합과 Kp의 결정인자

<!-- MASTER LENS -->
**핵심 직관**: 큰 Vd는 “plasma에서 많이 풀려 있다”가 아니라 “tissue에서 더 강하게 붙잡힌다”는 신호인 경우가 많다. Basic drug의 큰 Vd는 plasma binding보다 tissue binding, 특히 acidic phospholipid affinity로 설명되는 경우가 많다. [R&T pp.108–111]

#### A. Formal Definition

Tissue-to-plasma equilibrium distribution ratio $K_p$는 tissue concentration과 plasma concentration의 평형 비율이며, R&T는 Eq.4-25와 Eq.4-12를 비교해 $K_p\sim f_u/f_{uT}$로 해석할 수 있음을 설명한다. [R&T pp.104, 109–110]

#### B. Source-Anchored Details

- Furosemide와 amiodarone은 plasma $f_u$가 비슷한 범위일 수 있으나 V는 크게 다르다. 차이는 basic drug의 높은 tissue binding, 즉 낮은 $f_{uT}$에서 온다. [R&T p.110]
- Propranolol은 6 controls + 15 chronic hepatic disease patients에서 40 mg IV bolus 후 $V$와 $f_u$의 관계가 제시된다. 이는 plasma binding 변화가 $V$ 변동을 설명할 수 있음을 보여준다. [R&T Fig.4-23, p.110]
- Metoprolol tissue $K_p$는 tissue acidic phospholipid concentration과 강한 positive relationship을 보인다. Exact `r>0.85`는 원문에 없으므로 삭제한다. [R&T Fig.4-24, p.110]
- Indinavir 800 mg q8h HIV adults 8명에서 CSF unbound concentration은 plasma unbound보다 낮고 지연되며 fluctuation이 작다. Exact “1/10”은 approximate visual estimate로만 취급한다. [R&T Fig.4-10, p.91]
- Brain은 whole-body mass의 약 2%이므로 local transporter effect가 whole-body V를 크게 바꾸지 않을 수 있다. [R&T pp.109, 111]

#### C. Plasma-to-Blood Context

Appendix D의 핵심은 blood/plasma concentration ratio가 hematocrit, plasma fu, red cell binding에 의해 달라진다는 점이다.

$$\frac{C_b}{C}=1+H\left(f_u\cdot K_{PBC}-1\right)$$

[출처: R&T App.D, pp.775–776]

#### D. Boundary Condition

Transporter가 지배적이면 tissue unbound concentration과 plasma unbound concentration이 자유롭게 평형을 이룬다는 단순 $f_{uT}$ 해석이 깨질 수 있다. BBB의 efflux transporter가 대표적인 예다. [R&T pp.90–91, 110–111]

<!-- RECAP -->
**M5 recap**: $K_p$는 tissue affinity의 숫자 표현이고, $f_{uT}$는 tissue binding의 inverse signal이다. Transporter가 있으면 $K_p$는 binding뿐 아니라 uptake/efflux imbalance까지 반영한다.

---

### M6 · 노출 지표 선택: total vs unbound

<!-- MASTER LENS -->
**핵심 직관**: exposure metric은 “하나의 AUC 숫자”가 아니라, 어떤 concentration species가 어떤 시간 패턴으로 pharmacology를 만든다는 주장이다. Total concentration이 protein binding 차이에 confounded되면 unbound concentration이 active comparator가 된다. [G&W pp.163–169]

#### A. Formal Definition

Total and unbound concentration 관계:

$$C=\frac{C_u}{f_u}$$

$f_u$가 일정하면:

$$AUC_u=AUC\times f_u$$

[출처: G&W Eq.2:373, p.167]

#### B. Source-Anchored Details

- G&W Fig.2.134는 dose-response, total concentration-response, unbound concentration-response가 서로 다른 결론을 낼 수 있음을 보여준다. Total concentration 관계는 plasma protein binding 차이에 confounded되고, unbound concentration 기준에서는 potency order가 뒤집힌다. [G&W p.163]
- G&W Fig.2.136은 같은 AUC라도 peak, duration above threshold, toxicity implication이 다를 수 있음을 경고한다. “equal AUC = equal effect”는 process shape을 잃는 단일 scalar shortcut이다. [G&W p.164]
- G&W Fig.2.140은 $f_u$를 total concentration보다 $C_u$에 대해 그릴 때 더 명확한 관계를 보일 수 있음을 제시한다. [G&W p.167]
- G&W Fig.2.141은 dog/rat/mouse total concentration-response curve는 다르게 보이나 unbound ECu50가 약 2 nM 부근으로 정렬될 수 있음을 보여준다. Total potency fold는 visual/inferred estimate로만 다룬다. [G&W p.168]
- G&W Table2.21은 exposure metric을 `Cmax`, `AUC`, `td`, treatment period 등으로 나누고, 각 metric의 적용 상황을 구분한다. [G&W p.169]
- G&W는 456 drugs 검토를 인용하며 protein binding change가 PK parameters에는 영향을 줄 수 있으나 clinical outcome에는 대개 큰 영향을 주지 않고, 예외는 IV high-extraction drug with narrow therapeutic window라고 정리한다. [G&W p.168]
- G&W 결론: IND 단계에서는 여러 concentration과 species(including human)에서 ex vivo plasma protein binding을 측정하고, NDA 단계에서는 selected clinical studies에서 unbound와 total concentration을 함께 얻는 것이 권장된다. Routine “good to have” 측정은 지양한다. [G&W p.169]

#### C. Boundary Conditions

- $f_u$가 dose-, time-, concentration-dependent이면 $AUC_u=AUC\times f_u$ shortcut은 무효가 될 수 있다.
- Total AUC가 같아도 peak-driven toxicity 또는 duration-above-threshold effect는 다를 수 있다. [G&W Fig.2.136, p.164]
- “unbound를 항상 측정하라”가 아니라 “의사결정이 unbound species에 민감한 상황에서 측정하라”가 G&W의 결론이다. [G&W p.169]

<!-- RECAP -->
**M6 recap**: total concentration은 assay-friendly metric이고, unbound concentration은 active species에 가까운 metric이다. 어느 쪽을 쓸지는 binding 차이, species extrapolation, exposure shape, decision risk가 결정한다.

---

## §5 — Confusion Pair Dissection

### Confusion Pair 1 — C vs Cu **[Critical Blow]**

<!-- CONFUSION -->
| 구분 | C, total concentration | Cu, unbound concentration |
|---|---|---|
| 정의 | bound + unbound | unbound only |
| 막투과 driving force | 부적합 | 적합 [R&T p.80] |
| Exposure-response | PPB 차이에 confounded 가능 | active species 비교에 유리 [G&W pp.163, 167–168] |
| Shortcut | assay가 쉬움 | fu 측정 또는 모델 필요 |
| 실패 모드 | species/compound potency order가 왜곡됨 | fu가 time-dependent이면 계산 오류 가능 |

<!-- MASTER LENS -->
Critical Blow는 “C와 Cu 중 무엇이 참인가?”가 아니라, **지금 의사결정의 causal species가 무엇인가?**이다. 막투과, receptor interaction, species extrapolation이 문제이면 $Cu$가 더 직접적이다. 하지만 $f_u$가 안정적이고 decision이 total assay 기반으로 검증되어 있다면 $C$도 유용하다.

### Confusion Pair 2 — Perfusion-rate vs Permeability-rate limitation

<!-- CONFUSION -->
Perfusion-rate limitation에서는 blood flow가 속도를 정하고 Eq.4-5~4-7이 안전하다. Permeability-rate limitation에서는 membrane passage가 bottleneck이며, brain penicillin G나 macromolecule lymphatic distribution처럼 blood flow만으로 설명되지 않는다. [R&T pp.94–100]

### Confusion Pair 3 — fu vs fuT

<!-- CONFUSION -->
$f_u$는 plasma에서 unbound fraction이고, $f_{uT}$는 tissue에서 unbound fraction이다. $V=V_p+V_{TW}(f_u/f_{uT})$이므로 $f_u$가 커지면 V는 커질 수 있고, $f_{uT}$가 작아지면 V는 크게 커진다. [R&T Eq.4-25, p.109]

### Confusion Pair 4 — Small Vd vs Large Vd response to protein binding

<!-- CONFUSION -->
Small-Vd albumin-bound drugs에서는 albumin distribution model과 7.5 L floor가 필요하다. Large-Vd basic drugs에서는 tissue binding이 지배적이므로 plasma protein binding 변화만으로 V와 Cu를 해석하면 위험하다. [R&T pp.111–118]

---

## §7 — Self-Test: Active Recall Module

### Q1
<!-- SELF-TEST -->
Eq.4-1에서 concentration difference가 $C_1-C_2$가 아니라 $Cu_1-Cu_2$인 이유는?

**Answer**: bound drug은 일반적으로 막을 통과하지 못하고, unbound drug만 diffusion driving force가 되기 때문이다. [R&T p.80]

### Q2
<!-- SELF-TEST -->
MW 400→800 g/mol 증가와 logP 증가가 permeability에 미치는 방향을 각각 말하라.

**Answer**: MW 증가는 permeability를 크게 낮추고, logP 증가는 대체로 permeability를 높인다. 단 transporter substrate이면 logP 예측이 깨질 수 있다. [R&T Fig.4-3~4-4, pp.81–82]

### Q3
<!-- SELF-TEST -->
Perfusion-rate limited tissue에서 $K_{pb}$가 커지면 distribution half-life는 어떻게 변하는가?

**Answer**: $t_{1/2,distribution}=0.693K_{pb}/(Q/V_T)$이므로 커진다. 친화도가 크면 채워야 할 tissue amount가 많아져 equilibrium 도달이 늦어진다. [R&T p.97]

### Q4
<!-- SELF-TEST -->
Small-Vd albumin-bound drug에서 $f_u\to0$일 때 V가 0 L이 아니라 약 7.5 L 근처 floor를 갖는 이유는?

**Answer**: 약물이 albumin에 붙어 plasma와 extravascular albumin space에 분포하기 때문이다. Albumin distribution volume이 약 7.5 L floor를 만든다. [R&T p.111–113; App.C pp.767–773]

### Q5
<!-- SELF-TEST -->
Warfarin nephrotic syndrome에서 albumin 감소가 V, CL, t1/2에 어떤 방향 변화를 보였는가?

**Answer**: albumin 43→12.5 g/L에서 V 9.4→13.7 L, CL 0.20→0.58 L/hr, t1/2 36→18 hr로 변했다. [R&T Table4-12, p.118]

### Q6
<!-- SELF-TEST -->
G&W Eq.2:373의 $AUC_u=AUC\times f_u$를 쓰기 위한 핵심 조건은?

**Answer**: $f_u$가 시간·농도·dose에 대해 충분히 일정해야 한다. 그렇지 않으면 total AUC에 하나의 fu를 곱하는 shortcut이 깨진다. [G&W p.167]

### Q7
<!-- SELF-TEST -->
Equal AUC인데 toxicity가 다를 수 있는 이유는?

**Answer**: 같은 area라도 peak concentration, threshold 초과 시간($t_d$), concentration-time shape이 다를 수 있기 때문이다. [G&W Fig.2.136, p.164]

### Q8
<!-- SELF-TEST -->
PK47에서 low/high protein concentration을 동시에 fit하는 이유는?

**Answer**: $n$과 $K_a$의 correlation을 줄이고 precision을 높이기 위해서다. [G&W p.693]

### Q9 — Boss Dilemma
<!-- SELF-TEST -->
신약 후보에서 total AUC는 종간 차이가 큰데 unbound ECu50는 종간 정렬된다. 어느 exposure metric을 safety margin 논의의 중심에 놓을 것인가?

**Answer**: unbound exposure를 중심 metric으로 두되, total exposure와 $f_u$ 측정 방법을 함께 제시한다. G&W는 total concentration-response가 PPB 차이에 confounded될 수 있고, unbound concentration이 species extrapolation에서 더 적절할 수 있음을 보여준다. [G&W pp.163, 167–169]

### Q10 — [교육용 가상 사례]
<!-- SELF-TEST -->
Phase 1 SAD에서 dose-normalized AUC가 dose 증가와 함께 감소한다. Saturable clearance와 saturable PPB를 어떻게 구분할 것인가?

**Answer**: dose별 ex vivo $f_u$를 확인한다. $f_u$가 dose/Cu에 따라 증가하면 saturable PPB가 원인일 수 있고, $f_u$가 일정하면 clearance nonlinearity를 우선 의심한다. 이 문항은 교과서 수식의 실무 적용이며, 특정 PDF case는 아니다.

---

## §8 — Meta-Frame & Big Picture

### A. Positioning

<!-- MASTER LENS -->
이 세션은 **distribution을 physiology로 읽는 법**을 세운다. 이후 clearance, multiple dosing, TDM, PBPK, PopPK covariate modeling은 모두 여기서 정의된 $Cu$, $f_u$, $f_{uT}$, $K_p$, $V$ 위에 쌓인다.

### B. Dependencies

이 섹션을 약하게 이해하면 다음 오류가 발생한다.

1. **Loading dose 오류**: $V$가 apparent proportionality constant임을 잊고 physiologic volume처럼 해석한다.
2. **Covariate 오류**: albumin 변화가 total CL, total V, unbound exposure에 미치는 방향을 구분하지 못한다.
3. **Exposure metric 오류**: equal AUC를 equal effect로 가정하고 peak/duration 정보를 잃는다.
4. **Species extrapolation 오류**: total concentration-response의 potency order를 active unbound species의 potency order로 착각한다.
5. **Protein binding 오류**: $f_u$를 상수로 가정하고 saturable binding 또는 protein concentration change를 놓친다.

### C. Professional Moat

박사과정생이 이 세션에서 가져가야 할 한 문장은 다음이다.

<!-- RECAP -->
**분포는 “약물이 어디에 있는가”가 아니라, plasma와 tissue 사이의 binding·permeability·flow가 만든 equilibrium and time-course problem이다.** Total concentration은 관찰값이고, unbound concentration은 많은 경우 causal species에 더 가깝다. $V$는 그 둘을 amount와 연결하는 apparent constant이다.

### D. System Integration Points

- **Clinical pharmacology summary**: dose-exposure linearity를 쓸 때 absorption/permeability(M1), V/dose dependence(M3), saturable PPB(M4), exposure metric(M6)이 한 문단 안에서 연결된다.
- **TDM**: hypoalbuminemia, renal failure, α1-AGP change가 동시 발생하면 total concentration만으로는 active exposure를 놓칠 수 있다.
- **NONMEM**: albumin/α1-AGP covariate는 `V`에만 기계적으로 붙이는 것이 아니라, total vs unbound scale과 CL 해석까지 함께 결정해야 한다.

---

## Content Lock Notes

- Audit MUST_FIX는 모두 반영했다.
- Audit T6 Figure Inventory는 본 문서에서 재판정하지 않았고 Phase 4C로 넘긴다.
- `[확인 필요]` 성격의 visual estimate는 exact value로 쓰지 않고 “visual/approximate” 또는 qualitative wording으로 낮췄다.
- 첨부 PDF 밖 실무 확장은 삭제하거나 `[교과서 외 실무 해석]`으로 표시했다.

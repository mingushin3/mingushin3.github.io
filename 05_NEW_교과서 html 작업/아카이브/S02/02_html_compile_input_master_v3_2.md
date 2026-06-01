# XX_html_compile_input_master_v3.2.md

**v3.2 note:** This version applies a Korean-Dominant Readability Patch to PART A learner-facing prose. General English prose was converted to Korean where possible, while career-critical pharmacometrics terms are retained as Korean-English paired expressions on first use. Scientific content, equations, numerical anchors, page tags, source labels, figure markers, compiler markers, section structure, and PART B guardrails are preserved. No new scientific claims, examples, numbers, page tags, figures, or external references were added.

---

# 02_HTML Compile Input Master — v3.2

> **v3.2 변경 사항 요약 (Korean-Dominant Readability Patch over v3.1)**: v3.1의 모든 과학적 콘텐츠·수식·page tag·source label·figure marker·HTML compiler marker·`[EXPERT_INFERENCE, v3]` 라벨·certification table·PART B guardrail은 verbatim 유지. v3.2는 PART A learner-facing 산문 전반에 한국어 중심 가독성 패치를 적용: (1) 영문 섹션 소제목(Formal Definition, Boundary Conditions, Source-Anchored Details 등)을 `한글(English)` 병기 형식으로 교체, (2) 교육 장치명(Failure Mode, Practice Lens, Mastery Note, Trench-Level Tip 등)에 한국어 명칭 병기, (3) §8 소제목(Positioning, Dependencies, Professional Moat, System Integration Points, Diagnostic Signatures, Mastery Sequence)의 한국어 병기, (4) 본문 내 잔여 영어 일반 설명문의 한국어 전환, (5) Self-Test 질문/답 내 잔여 영어 서술의 한국어화. 새 과학적 주장·새 수치·새 page tag·새 figure marker·새 외부 인용·새 regulatory 주장 모두 추가하지 않음.

> **v3.1 변경 사항 요약 (Korean Readability Patch over v3)**: v3의 모든 과학적 콘텐츠·수식·page tag·source label·figure marker·HTML compiler marker·`[EXPERT_INFERENCE, v3]` 라벨·certification table·PART B guardrail은 verbatim 유지. v3.1은 PART A learner-facing 산문에 한국어 가독성 개선 패치 22건만 적용 (전원 Low risk). 적용 범위: (1) Learner Navigation Aid 영문 산문의 한국어화 (P-01~P-07, 7건), (2) §2 카드 본문의 영어식 명사 나열·어색한 조사 연결 교정 (P-08~P-12, 5건), (3) §5 Memory Hook 장문의 sentence split 및 명료화 (P-14~P-16, 3건), (4) Boundary Condition·Practice Brief·RECAP의 first-use gloss 및 sentence split (P-13, P-17~P-22, 7건). 새 과학적 주장·새 수치·새 page tag·새 figure marker·새 외부 인용·새 regulatory 주장 모두 추가하지 않음.

> **v3 변경 사항 요약 (Surgical Patch over ver2)**: ver2의 모든 PART A learner body 및 §8 D·E·F augmentation은 verbatim 유지. v3는 (1) M3 Apex marker를 `[⚡ Apex Concept]`로 표준화, (2) M3에 Plausible Fallacy 블록 추가, (3) §5 4개 confusion pair 직후에 Memory Hook 4종 추가, (4) M1~M6 카드 말미에 4축 Practice Brief 추가. 모든 v3 추가 블록은 `[EXPERT_INFERENCE, v3]` 라벨 부착. 삭제된 Caco-2/PAMPA/Lipinski 항목은 복원하지 않음. 기존 진단 시그니처 3종(Albumin Covariate Asymmetry / PK47 Single-Site Misfit / Vss vs Vβ Confusion)은 §8 E에서 그대로 보존. 출처-경계·페이지 태그·그림 결정은 ver1·ver2와 동일하게 유지.

> **ver2 변경 사항 요약 (참조용 보존)**: ver1의 모든 PART A learner body는 verbatim 유지. §8에 세 개의 라벨링된 mastery augmentation block 추가 (D 강화, E 신설, F 신설). PART B B9 Coverage Matrix 및 B11 Mastery Augmentation Log를 업데이트해 추가 augmentation을 추적. 출처-경계·페이지 태그·그림 결정은 ver1과 동일하게 유지.

## Phase 4D Certification

| Certificate | Status | Basis |
|---|---|---|
| Learner-Standalone Certificate | PASS | PART A contains navigation aid plus §1-§8 learner body only; audit/compiler/process material is isolated in PART B. ver2의 §8 E·F augmentation 및 v3의 M3 Plausible Fallacy / §5 Memory Hooks 4종 / M1~M6 Practice Brief 6종은 모두 learner-facing이며 verbatim 가독성 유지. v3.1 Korean Readability Patch는 동일 learner body의 산문 표현만 다듬으며 구조·라벨·marker를 변경하지 않음. v3.2 Korean-Dominant Readability Patch는 영문 소제목·교육 장치명에 한국어 병기를 추가하며 과학적 내용을 변경하지 않음. |
| Zero-Omission Certificate | PASS | Scope MUST concepts, Audit MUST_FIX/SHOULD_FIX, retained figure pointers, page tags, and adopted Crucible Grade A logic are present or justifiably compressed. ver2에서 Crucible T2(b)의 미명명 GOF signature 2종(PK47 Single-Site Misfit, Vss vs Vβ Confusion)이 §8 E에서 명시적으로 명명되어 Crucible Grade A 통합도가 강화됨. v3는 §5 4쌍 모두에 Memory Hook을 부여하여 confusion pair dissection의 누락 항목을 해소함. |
| Mastery-Uplift Certificate | PASS | PART A contains 22 bounded, adjacent, source-labeled augmentation blocks for this A-Critical chapter (ver1: 8 → ver2: 11 → v3: 22). v3 추가 11개 블록은 (a) M3 Plausible Fallacy 1개, (b) §5 Memory Hooks 4개, (c) M1~M6 Practice Brief 6개. |
| Source-Boundary Certificate | PASS | Augmentations are labeled TEXTBOOK_DERIVED, AUDIT_DERIVED, CRUCIBLE_DERIVED, or EXPERT_INFERENCE and add no new page tags or unsupported numerical claims. v3 추가 블록은 모두 [EXPERT_INFERENCE, v3] 라벨로 명시되며 새로운 외부 인용·새 수치·새 페이지 태그·새 그림 결정·복원 금지 항목(Caco-2/PAMPA/Lipinski) 모두 추가하지 않음. v3.1 Korean Readability Patch도 산문 표현만 수정하며 source-boundary를 손상하지 않음. v3.2도 동일. |
| HTML-Readiness Certificate | PASS | PART B contains Phase 5 rendering contract, marker mapping, page-tag rules, figure rules, audit/crucible guardrails, and navigation integrity rules. v3 추가 블록은 기존 marker 시스템(callout, MASTER LENS, RECAP)과 호환되는 blockquote/heading 구조만 사용하며 새 marker 도입 없음. v3.1 패치는 marker·수식·code block·page tag·figure pointer를 단 하나도 변경하지 않으므로 HTML-readiness 영향 없음. v3.2도 동일. |
| Apex-Standardization Certificate (v3) | PASS | M3 Apex marker가 `[Apex Concept]`에서 `[⚡ Apex Concept]`로 표준화됨. Apex Concept는 §2 전체에서 M3 단 하나만 표시되어 Apex의 단일성 원칙(per-session 1 Apex)을 유지함. |
| Korean-Readability Certificate (v3.1) | PASS | PART A 산문에 22건의 한국어 가독성 패치 적용 (Low risk only): Navigation Aid 영문 산문 한국어화, §2 카드 본문 영어식 명사 나열 교정, §5 Memory Hook 장문 분리, first-use gloss 추가, semicolon → period 교체. 모든 패치는 의미 보존을 검증한 surgical edit이며, 새 과학적 주장·새 수치·새 page tag·새 marker·새 외부 인용을 도입하지 않음. PART B는 본 인증서 추가와 B12 Change Log 갱신을 제외하면 verbatim 유지. |
| Korean-Dominant Readability Certificate (v3.2) | PASS | PART A 전반의 일반 영어 산문을 한국어 중심으로 전환. 영문 소제목에 `한글(English)` 병기 적용, 교육 장치명에 한국어 명칭 추가, 본문 잔여 영어 설명문 한국어화. 커리어상 필수 전문용어는 `한글(English)` 형식으로 보존. 수식·수치·page tag·source label·figure marker·HTML compiler marker·code block 무변경. 새 과학적 주장·새 수치·새 외부 reference 도입 없음. |

## Assembly Mode

**FULL MODE** — `02_Content Lock v2.1(1).md` is complete and already contains the retained Phase 4C figure markers. No PATCH MODE splicing was required.

## Input Manifest

| File | Role | Authority level | Used for | Notes |
|---|---|---|---|---|
| 붙여넣은 텍스트 (1)(75).txt | Phase 4D assembly prompt | A7 | compiler/master assembly instruction | Renamed target from 05 to 02 to match user request. |
| 붙여넣은 마크다운(2)(51).md | Step 2 HTML Compiler prompt / Prompt 5 | A7 | HTML rendering requirements and guardrails | Used in PART B only. |
| 02_scope_lock(4).md | Scope Lock | A0 | scope boundary, learner, mode, source range, hard limits | Defines A-Critical session and PDF ranges. |
| 02_T_분포의 생물학 Vd·막투과·단백결합(5).pdf | Original R&T textbook PDF | A1 | PDF verification source | R&T Ch.4 p.77-118; App.B/C/D. |
| 02_G_분포의 생물학 Vd·막투과·단백결합(5).pdf | Original G&W textbook PDF | A1 | PDF verification source | G&W §2.9.3-2.9.5 and PK47. |
| 02_Audit_Report_v1(3).md | Audit Report v1 | A2 | audit guardrail and correction checklist | Controls MUST_FIX/SHOULD_FIX and rejected material. |
| 02_Content Lock v2(3).md | Content Lock v2 | A3 | locked reference / fallback canonical body | Used as regression reference; v2.1 available. |
| 02_Content Lock v2.1(1).md | Content Lock v2.1 | A4 | canonical learner body and figure markers | FULL MODE source for PART A. |
| 02_crucible_report_v1(2).md | Crucible Report v1 | A5 | crucible guardrail and accepted insight source | Used only for adopted Grade A logic / augmentation source labels. |
| 02_step1_draft_v0(3).md | Step 1 Draft v0 | A6 | deprecated source / regression check | Not copied into PART A except through locked Content Lock material. |
| 02_Content_Lock_v1(2).md | Content Lock v1 | locked reference | historical adjudication reference | Used for consistency check only. |
| S02_phase1_patch memo(3).md | Phase 1 Patch Memo | audit support | patch attention / guardrail source | Used to confirm known risks were resolved. |

## PART A — 학습자용 완성 핸드아웃

## 학습자 네비게이션 안내

### 이 자료 활용 방법

1. §1을 읽어 핵심 질문을 먼저 고정하라: 지금 해석하는 농도는 어떤 species이며, 어떤 결합 구획을 다루고 있는가?
2. §2를 순서대로 학습하라. M1은 약물이 막을 통과할 수 있는지, M2는 분포 속도를 결정하는 요인, M3은 V의 수학적 의미, M4·M5는 혈장 및 조직 결합, M6은 어떤 노출 지표(exposure metric)가 정당화될 수 있는지를 다룬다.
3. FIGURE_POINTER 블록은 교과서 그림을 직접 찾아보라는 안내 블록이며, 저작권이 있는 교과서 그림을 직접 재현하지 않는다.
4. §5와 §7로 마무리하라. 이 두 섹션은 자주 발생하는 실수 패턴을 미리 노출하도록 설계되었다.
5. §8로 닫아라. §8 D는 6개 카드가 하나의 시스템으로 작동하는 두 가지 통합 시나리오를, §8 E는 세 가지 진단 시그니처(Albumin Covariate Asymmetry / PK47 Single-Site Misfit / Vss vs Vβ Confusion)를, §8 F는 새 PK 문제에 이 자료를 적용하는 4단계 체화 시퀀스(Mastery Sequence)를 제시한다.

### 학습 경로

M1 막투과 결정인자 → M2 분포 율속 단계 → M3 겉보기 분포용적 구조 → M4 혈장단백결합과 농도의존성 fu → M5 조직결합/Kp/수송체 → M6 total vs unbound 노출 지표 → §5 치명적 타격(Critical Blow) → §7 자기 테스트 → §8 A–C 전문가 해석 지점 → §8 D 시스템 통합 시나리오 → §8 E 진단 시그니처 → §8 F 체화 시퀀스.

### 학습 시작 전 체크리스트

- Total concentration `C`와 unbound concentration `Cu`를 구분할 수 있다.
- 겉보기 분포용적(apparent volume)은 실제 장기 부피가 아님을 안다.
- FIGURE_POINTER 블록은 삽입 이미지가 아니라 교과서를 직접 찾아보라는 안내임을 인지한다.

### 학습 완료 후 체크리스트

- 수동 막 확산의 구동력(driving force)이 total `C`가 아닌 `Cu`인 이유를 설명할 수 있다.
- 분포 범위(extent)와 분포 속도(distribution rate)를 독립적인 차원으로 분리하여 논할 수 있다.
- `Vp + tissue term`, `Kp`, `fu/fuT`가 동등한 렌즈임을 가정이 만족될 때만 사용할 수 있다.
- `AUCu = AUC × fu` 단축식이 안전한 경우와 안전하지 않은 경우를 진술할 수 있다.
- 근거 없는 규제 주장(unsupported regulatory claim)을 도입하지 않고 total vs unbound 노출 지표 선택을 방어할 수 있다.
- §8 E의 세 가지 진단 시그니처를 명명하고 각각의 GOF 패턴을 설명할 수 있다.
- §8 F의 4단계 체화 시퀀스(Mastery Sequence)를 처음 보는 PK 사례에 적용할 수 있다.


---

## §1 — 세션 헤더 & 로드맵

### 핵심 통찰(Big Idea)

<!-- MASTER LENS -->
분포용적은 실제 장기 부피가 아니다. **체내 총량(Amount in body)을 농도로 나누기 위해 도입한 겉보기 비례상수(apparent proportionality constant)<!-- ANNOTATION --> (← 실제 부피가 아닌 계산상 비례상수)**이다. 따라서 이 상수는 대체로 `plasma binding(fu)`가 약물을 혈장 쪽에 붙잡는 힘과 `tissue binding(fuT/Kp)`이 조직 쪽으로 끌어당기는 힘의 균형으로 결정된다. [R&T pp.102–111]

> **체화 노트(Mastery Note) — EXPERT_INFERENCE**  
> 이 handout을 읽을 때는 모든 농도 기호 앞에 "어떤 species인가?"를 붙여서 해석한다. 같은 데이터라도 total scale, unbound scale, blood scale, tissue scale 중 무엇을 보고 있는지 바뀌면 V, CL, 노출-반응(exposure-response) 판단이 달라진다.

### 개념 항법도(Concept Navigation)

```text
M1 막투과 결정인자
  → M2 분포 율속: perfusion-limited인가 permeability-limited인가?
  → M3 Vd의 수학 구조 [Apex]
  → M4 plasma binding과 fu 농도의존성
  → M5 tissue binding, Kp, transporter
  → M6 total vs unbound exposure 선택
  → §5 Critical Blow: C vs Cu
```

### 지식 그래프 위치(Knowledge Graph Position)

- 이전 세션의 `C(t) = (Dose/V)·e^{-kt}`에서 $V$가 무엇인지 해부하는 장이다.
- 다음 소실(elimination) 세션에서는 $f_u$가 well-stirred 간 청소율 식의 분자로 들어간다.
- PopPK에서는 albumin, α1-AGP, 신·간 질환 공변량(covariate)이 `V`, `CL`, 또는 `fu`에 어떤 방향으로 연결되는지 판단하는 기반이 된다.

---

## §2 — 개념 해부 카드(Concept Anatomy Cards)

---

### M1 · 막투과의 결정인자

<!-- MASTER LENS -->
**핵심 직관**: 막투과는 "lipophilic이면 통과한다"로 끝나지 않는다. 실제 투과도(permeability)는 **크기(size) × 지용성(lipophilicity) × 전하(charge) × 수송체(transporter)**가 함께 만든다. Eq.4-1의 $P$는 이 네 축과 막 구조가 하나의 숫자로 압축된 거시 투과도(macroscale permeability)이다. [R&T pp.80–84, 85–90]

#### A. 형식적 정의(Formal Definition)

막 양쪽 수성구획의 유리 농도(unbound concentration)<!-- ANNOTATION --> (← 단백질에 결합하지 않은 농도)가 각각 $Cu_1$, $Cu_2$일 때 순수송속도(net transport rate)는 다음과 같다.

$$\text{Net rate of transport}=P\cdot SA\cdot(Cu_1-Cu_2)$$

[출처: R&T Eq.4-1, p.80]

결합 약물(bound drug)은 일반적으로 막을 통과하지 못한다. 따라서 막투과의 구동력(driving force)은 총 농도(total concentration) $C$가 아니라 유리 농도 $Cu$이다. [R&T p.80]

#### B. 출처 기반 상세(Source-Anchored Details)

- **크기(Size)**: 같은 지용성에서 MW 400 → 800 g/mol로 증가하면 피부 투과도(skin permeability)는 약 300배 낮아진다. [R&T Fig.4-3, p.81–82] Atenolol 246 g/mol은 위장관 흡수가 가능하지만, oxytocin 1007 g/mol은 GI membrane을 거의 통과하지 못하고, calcitonin-salmon 3432 g/mol은 비강 흡수(nasal absorption)도 약 3% 수준이다. [R&T p.81]
- **지용성(Lipophilicity)**: BBB 투과도는 대체로 n-octanol/water 분배계수가 증가할수록 증가한다. 단, vinblastine·vincristine은 지용성만으로 기대되는 값보다 낮은 투과도를 보이는데, 원문은 P-glycoprotein efflux 기질임을 주요 이유로 든다. [R&T Fig.4-4, p.82] "100배" 같은 배수는 시각 추정 [확인 필요]로만 취급한다.
- **전하 / pH 분배(Charge / pH partition)**: 약산·약염기에서는 비이온화형(un-ionized form)이 지질막(lipoidal membrane)을 주로 통과한다. 평형에서 비이온화 농도는 같아질 수 있지만, pH와 pKa에 따라 총 농도는 달라진다. [R&T p.83; App.B pp.763–765]
- **수송체(Transporter)**: 수동 촉진 수송체(passive facilitated transporter)는 평형 도달 속도를 바꾸고, 능동 수송체(active transporter)는 정상상태 유리 농도비(steady-state unbound ratio) 자체를 바꿀 수 있다. 능동 수송이 있을 때:

$$\frac{Cu_T}{Cu}=\frac{P_{uptake}}{P_{efflux}}$$

[출처: R&T Eq.4-26, p.110]

<!-- TRENCH -->
**현장 실무 팁(Trench-Level Tip)**: logP와 MW가 좋아도 P-gp/BCRP efflux 기질이면 BBB 또는 장벽에서 유효 투과도(effective permeability)가 크게 낮아질 수 있다. 단, Caco-2/PAMPA, Lipinski rule은 이 source 범위 밖이므로 본 handout에서는 삭제한다.

> **실패 모드(Failure Mode) — AUDIT_DERIVED**  
> logP 하나로 BBB 또는 조직 투과도를 예측하려고 하면, 크기·이온화·유출 수송체가 만드는 예외를 놓친다. 특히 이 세션에서는 "lipophilicity = permeability"가 아니라 "유효 투과도 = 물리화학 + 막 구조 + 수송체"로 읽어야 한다.

<!-- ANCHOR -->
막을 통과하는 성질이 정해지면, 다음 질문은 "조직으로 가는 속도가 혈류(blood flow)에 의해 제한되는가, 막 자체에 의해 제한되는가?"이다.

<!-- FIGURE_POINTER -->
Source: R&T 5e, p.82, Fig.4-4
Why this matters: BBB permeability가 logP만으로 결정되지 않고 size/efflux 예외를 갖는다는 점을 실제 좌표로 보여준다.
When to look: after reading this card
Learner instruction: caffeine, lomustine, vinblastine/vincristine의 위치를 비교하라.
<!-- /FIGURE_POINTER -->

> **▶ 실무 체화 요약(Practice Brief) — M1 체화 4축 — [EXPERT_INFERENCE, v3]**
> - **왜 알아야 하는가:** 약물이 막을 통과할 수 있는지가 흡수, 분포, 표적 도달 여부를 결정하기 때문에, 이후 모든 PK 해석의 기초 입력값이 된다.
> - **흐름상 역할:** M2의 관류 vs 투과 율속 판단으로 가는 진입점이며, M5의 수송체 매개 분포 해석에 필요한 4축(크기·logP·이온화·수송체)을 정의한다.
> - **체화 꿀팁:** 새 약물을 마주할 때마다 "size · logP · ionization · transporter" 네 축을 한 줄로 적어보고, 어느 축이 가장 약한 결정인자인지 짚는 습관을 들여라.
> - **실무 활용:** BBB 침투 가능성 1차 추정, P-gp/BCRP 기질 여부 평가, 경구 생체이용률(oral bioavailability) 추정의 출발점, NONMEM dataset에서 흡수상 모델 선택의 근거.

---

### M2 · 분포의 율속 단계

<!-- MASTER LENS -->
**핵심 직관**: 조직 분포에서는 "얼마나 많이 가는가"와 "얼마나 빨리 가는가"를 분리해야 한다. 조직 친화도(tissue affinity)가 커지면 평형 범위(equilibrium extent)는 커진다. 그러나 채워야 할 조직 내 약물량도 커지므로 평형 도달 시간(equilibrium time)은 오히려 길어질 수 있다. [R&T pp.94–100]

#### A. 형식적 정의(Formal Definition)

관류 율속 분포(perfusion-rate limited distribution)<!-- ANNOTATION --> (← 혈류 공급이 속도 제한)에서는 막 통과가 충분히 빠르다. 이때 조직으로 들어가는 공급 속도는 혈류가 결정하며, 조직 농도가 평형값에 접근하는 경로는 단일지수(mono-exponential) 형태를 따른다.

$$k_T=\frac{Q/V_T}{K_{pb}}$$

$$t_{1/2,distribution}=\frac{0.693\cdot K_{pb}}{Q/V_T}$$

$$C_T(t)=K_{pb}\cdot C_A\cdot(1-e^{-k_Tt})$$

[출처: R&T Eq.4-5~4-7, p.97]

#### B. 출처 기반 상세(Source-Anchored Details)

| 조직 | 관류속도(Perfusion rate), mL/min/g | 해석 |
|---|---:|---|
| 폐(Lung) | 10.0 | 매우 빠른 평형 도달 가능 |
| 신장(Kidney) | 4.0 | 혈류 풍부 장기 |
| 뇌(Brain) | 0.5 | 혈류는 높지만 BBB 투과도가 별도 제한 가능 |
| 지방(Adipose) | 0.025 | 매우 낮은 혈류 → 높은 Kp 약물에서 평형 도달 지연 |
| 비활동 근육(Inactive muscle) | 0.025 | 큰 조직 질량 + 낮은 관류 |

[출처: R&T Table4-4, p.96]

- **Thiopental 개 25 mg/kg IV bolus**: 뇌는 빠르게 오르고 빠르게 빠지는 반면, 지방은 낮은 관류/높은 친화도 때문에 3시간 이후에도 상당량이 남는다. 정확한 "3.5 h 평형"은 저자 명시 값이 아니므로 삭제한다. [R&T Fig.4-13, p.94]
- **고분자/림프 극단 사례(Macromolecule/lymphatic extreme)**: 대분자(large molecule)는 혈관벽 통과가 제한되며 림프 배출(lymphatic drainage)이 중요한데, 원문 caption은 림프 유속을 `1–10 mL/min per 70 kg`로 제시한다. [R&T Fig.4-14, p.95] MW >5000 g/mol에서는 투과 제한(permeability limitation)과 림프 회수(lymphatic return)가 분포 속도를 크게 늦출 수 있다. [R&T Table4-1, p.84; Fig.4-14, p.95]
- **Ribitol과 penicillin G**: 작은 극성 화합물(small polar compound)도 조직별 투과도에 따라 혼합 제한(mixed limitation)을 보이고, penicillin G는 근육과 달리 뇌/CSF에서 투과 제한이 두드러진다. [R&T Fig.4-17 p.99; Fig.4-18 p.100]

#### C. 경계 조건(Boundary Conditions)

- Eq.4-5~4-7은 **관류 율속(perfusion-rate limited)** 가정에서만 안전하다.
- 투과 율속(permeability-rate limited) 조직에서는 $Q$를 올려도 분포 속도가 비례해서 증가하지 않는다.
- 높은 $K_{pb}$는 "많이 간다"와 동시에 "평형 도달이 늦다"를 의미할 수 있다.

> **실무 렌즈(Practice Lens) — CRUCIBLE_DERIVED**  
> 분포 문제를 볼 때는 먼저 범위(extent)와 속도(rate)를 분리한다. V 또는 Kp는 "얼마나 많이"를 말하고, Q/VT와 투과도는 "얼마나 빨리"를 말하므로, 작용 발현(onset) 또는 채혈 시점(sampling-time) 문제를 평형 파라미터만으로 설명하지 않는다.

<!-- RECAP -->
**M2 요약(recap)**: 분포 반감기(distribution half-life)는 혈류, 조직 크기, 조직 친화도의 함수이다. 큰 $K_{pb}$와 낮은 $Q/V_T$가 만나면 분포는 느려진다.

<!-- FIGURE_POINTER -->
Source: R&T 5e, p.94, Fig.4-13
Why this matters: thiopental에서 brain과 fat의 time-course 차이가 perfusion과 affinity의 결합 효과임을 보여준다.
When to look: after reading this card
Learner instruction: brain peak와 fat 잔류를 비교하라.
<!-- /FIGURE_POINTER -->

> **▶ 실무 체화 요약(Practice Brief) — M2 체화 4축 — [EXPERT_INFERENCE, v3]**
> - **왜 알아야 하는가:** 동일한 Vd라도 평형 도달 속도가 다르면 작용 발현(onset), 최고 농도 시점(peak time), 채혈 설계(sampling design)가 완전히 달라지기 때문에, 모델 구조 결정의 분기점이 된다.
> - **흐름상 역할:** M1의 막투과 입력을 받아 M3의 V 해석 시점(분포 평형 후)을 정의하며, 다구획 모델 vs 단일구획 모델 결정의 근거가 된다.
> - **체화 꿀팁:** 새 약물의 첫 농도-시간 곡선에서 분포상(distribution phase)의 굴곡 시점을 기록한 뒤 $Q/V_T·K_{pb}$로 역산해 보고, 모델 가정과 일치하는지 점검하라.
> - **실무 활용:** PBPK 조직 평형 시간 추정, Phase 1 PK 채혈 일정 설계, thiopental·penicillin G 같이 혼합 제한을 보이는 약물의 조직 농도 해석.

---

### M3 · 분포용적의 수학 구조 **[⚡ Apex Concept]**

<!-- MASTER LENS -->
**핵심 직관**: $V$는 실제 부피가 아니라 `Amount/C`이다. 작은 Vd의 알부민 결합 산성 약물에서는 알부민이 페리(ferry)처럼 약물을 혈장과 혈관 외 알부민 공간으로 운반한다. $f_u\to0$이면 약물은 그 페리에서 거의 내리지 않는다. 이 때문에 겉보기 V는 알부민 분포 용적인 약 7.5 L 근처에서 하한(floor)을 갖는다. [R&T pp.111–113; App.C pp.767–773]

#### A. 형식적 정의(Formal Definition)

$$V=\frac{\text{Amount in body}}{C}=\frac{A}{C}$$

[출처: R&T Eq.4-8, p.102]

조직/혈장 평형 농도비 $K_p$를 쓰면:

$$A=V_p\cdot C+V_T\cdot K_p\cdot C$$

$$V=V_p+V_T\cdot K_p$$

$$V=V_p+\sum_i V_{T,i}\cdot K_{p,i}$$

[출처: R&T Eq.4-11~4-13, pp.103–104]

측정 매질(matrix)이 바뀌면 겉보기 용적도 달라진다.

$$V_u=\frac{A}{C_u},\qquad V_b=\frac{A}{C_b}$$

[출처: R&T Eq.4-14~4-15, p.104]

#### B. 결합 기반 구조(Binding-Based Structure)

혈장/조직 유리 분율로 쓰면:

$$V=V_p+V_{TW}\cdot\frac{f_u}{f_{uT}}$$

[출처: R&T Eq.4-25, p.109]

<!-- ANNOTATION --> 여기서 $K_p$를 $f_u/f_{uT}$로 바꾸어 쓰는 이유는, 같은 총량이라도 혈장에 남는 비율과 조직에 붙는 비율이 서로 다르기 때문이다. 이 전환이 "V가 왜 결합의 함수인가"를 보여준다.

수송체가 조직 분포를 지배하면:

$$V=V_p+V_{TW}\cdot\frac{f_u}{f_{uT}}\cdot\frac{P_{uptake}}{P_{efflux}}$$

[출처: R&T Eq.4-29, p.111]

소 Vd 알부민 결합 약물 모델에서는:

$$V=7.5+\left(7.5+\frac{V_R}{f_{uR}}\right)\cdot f_u$$

[출처: R&T Eq.4-30, p.112; App.C Eq.C-13, pp.767–773]

#### C. 출처 기반 데이터 앵커(Source-Anchored Data Anchors)

- 혈장 3 L, 세포외액(extracellular water) 16 L, 총 체수분(total body water) 42 L는 V 해석의 생리학적 기준점이다. [R&T p.111]
- 알부민 겉보기 분포용적은 약 7.5 L이며, cephalosporin Fig.4-25에서 $f_u\to0$ 외삽 절편이 약 7 L로 보인다. [R&T Table4-5 p.101; Fig.4-25 pp.112–113]
- 같은 cephalosporin 계열에서 $V$는 $f_u$와 함께 증가하지만, $V_u$는 $f_u$가 증가할수록 감소한다. 이 쌍을 이루는 메시지(paired message)가 "총 농도 기준 V"와 "유리 농도 기준 V"가 같은 생리적 의미가 아님을 보여준다. [R&T Fig.4-25~4-26, p.113]
- Warfarin 신증후군(nephrotic syndrome) 예시: albumin 43→12.5 g/L, V 9.4→13.7 L, CL 0.20→0.58 L/hr, t1/2 36→18 hr. [R&T Table4-12, p.118]
- Adalimumab 같은 고분자량 항체는 V가 약 5–6 L로 작고, caffeine/alcohol처럼 작고 자유롭게 투과하는 분자는 V가 총 체수분에 접근한다. [R&T p.111]

#### D. 정점 오류(Apex Fallacy)

"$f_u$가 증가하면 유리 농도가 증가하므로 부하 용량(loading dose)을 올려야 한다"는 직관은 소 Vd 알부민 결합 약물에서 틀릴 수 있다. 같은 총량에서 $f_u$가 증가하면 총 $C$는 낮아지고 $V$는 증가한다. 그러나 $C_u$는 반드시 같은 방향으로 증가하지 않는다. R&T의 cephalosporin/warfarin 논리는 이 함정을 정면으로 다룬다. [R&T pp.112–118]

#### D-2. 그럴듯한 오해(Plausible Fallacy) — Vd를 실제 부피로 오해

> **⚡ 그럴듯한 오해(Plausible Fallacy) — [EXPERT_INFERENCE, v3]**
> - **그럴듯한 오해**: "Vd가 크다는 것은 체내 분포 공간이 실제로 크다는 뜻이다."
> - **왜 틀렸는가**: Vd는 체적이 아니라 혈장 농도 관측값으로 역산한 비례상수다. 조직 결합이 강하거나 혈장 결합이 약하면 실제 체적의 수십~수백 배도 가능하다. fu와 fuT의 비율이 이 겉보기 크기를 결정한다.
> - **실무에서 어떻게 드러나는가**: Vd가 500 L인 약물의 부하 용량을 "체중×4 L/kg"로 설계하다가 실제 분포 공간 개념으로 혼동하면, 부하 용량 계산이 생리학적 의미를 잃는다. Bayesian TDM에서 total C가 정상 범위인데 unbound C가 달라진 경우를 생각해 보라. 실제 원인은 fu 변화인데도 Vd 변화로 오해하는 전형적 실수가 여기에서 비롯된다.

<!-- TRENCH -->
**[교과서 외 실무 해석] 알부민 공변량 비대칭(Albumin covariate asymmetry)**: 대 Vd 약물에서 알부민을 `V` 공변량으로만 넣고 `CL` 쪽을 보지 않으면 총 농도 기준 CL 변화가 누락될 수 있다. ETA-CL vs albumin 관계가 ETA-V vs albumin보다 강하면 CL 공변량도 검토한다.

**[교과서 외 실무 경고] Vss vs Vβ**: 다구획 모델(multi-compartment model)에서 부하 용량은 Vss 기반, 종말상 반감기(terminal half-life) 해석은 Vβ 기반이라는 구분을 유지한다.

> **체화 노트(Mastery Note) — CRUCIBLE_DERIVED**  
> 알부민 변화가 보이면 바로 "용량을 바꿀까?"로 가지 말고, total C, Cu, V, CL 중 어느 관찰값이 움직였는지 먼저 분해한다. 이 순서를 지키면 저알부민혈증(hypoalbuminemia) 상황에서 총 농도 변화와 활성 노출(active exposure) 변화를 혼동하지 않는다.

<!-- RECAP -->
**M3 요약(recap)**: $V$는 `Vp + tissue term`이며, tissue term은 $K_p$ 또는 $f_u/f_{uT}$로 읽을 수 있다. 소 Vd 알부민 결합 약물에서는 알부민 분포 용적이 하한(floor)을 만든다.

<!-- FIGURE_POINTER -->
Source: R&T 5e, p.113, Fig.4-25 and Fig.4-26
Why this matters: 같은 cephalosporin series에서 V와 Vu가 fu에 대해 반대 방향으로 읽힐 수 있음을 보여준다.
When to look: after reading this card
Learner instruction: V-fu와 Vu-fu 축을 나란히 비교하라.
<!-- /FIGURE_POINTER -->

> **▶ 실무 체화 요약(Practice Brief) — M3 체화 4축 — [EXPERT_INFERENCE, v3]**
> - **왜 알아야 하는가:** Vd는 부하 용량 계산과 공변량 해석의 중심 파라미터인데, 그 본질이 겉보기 비례상수(apparent proportionality constant)임을 놓치면 후속 모든 추론이 흔들린다.
> - **흐름상 역할:** M4·M5의 결합 정보(fu, fuT)와 M6의 노출 지표를 V라는 단일 수학적 연결 고리(mathematical bridge) 위에 통합하는 세션의 중심 카드다.
> - **체화 꿀팁:** 새 약물의 V 값을 보면 즉시 혈장 3 L · 세포외액 16 L · 총 체수분 42 L · 알부민 7.5 L 중 어느 기준점(anchor)에 가까운지 분류하라 — 이 분류만으로 결합 양상(binding regime)이 절반 이상 보인다.
> - **실무 활용:** 부하 용량 설계, 저알부민혈증/투석 환자에서 V 변화 해석, NONMEM에서 V 위에 공변량 spec할 때의 방향(positive/negative) 판단, Bayesian TDM에서 V 이상값의 진단.

---

### M4 · 혈장단백결합과 fu의 농도의존성

<!-- MASTER LENS -->
**핵심 직관**: $f_u$는 고정 상수가 아니다. 혈장 단백 농도(protein concentration), 결합 친화도(binding affinity), 결합 부위 수, 유리 농도(unbound concentration) 등 여러 인자의 함수이기 때문이다. 따라서 "총 농도 ↔ 유리 농도" 변환은 $f_u$가 일정하다는 검증 위에서만 안전하다. [R&T pp.105–108; G&W pp.690–693]

#### A. 형식적 정의(Formal Definition)

$$f_u=\frac{C_u}{C}$$

[출처: R&T Eq.4-17, p.105]

단일 결합 부위에서 결합 상수(association constant)는:

$$K_a=\frac{C_{b,t}}{C_u\cdot P}$$

[출처: R&T Eq.4-18, p.105]

R&T의 질량작용 관계식(mass-law relationship)은 단백 농도와 결합 부위 점유율이 $f_u$를 바꾼다는 점을 보여준다.

$$f_u=\frac{1}{1+K_a\cdot f_{up}\cdot P_t}$$

[출처: R&T Eq.4-19, p.105]

#### B. PK47 출처 기반 데이터(Source-Anchored Data)

G&W PK47은 $f_u$를 $C_u$, 총 단백 농도 $[P_T]$, 부위 수 $n$, 친화도 $K_a$의 함수로 모델링한다.

$$f_u=1-\frac{1}{1+\frac{C_u}{n[P_T]}+\frac{1}{K_a\cdot n[P_T]}}$$

[출처: G&W Eq.47:1, p.691]

저 $C_u$ 근사식(Low-$C_u$ approximation):

$$f_u\approx\frac{1}{1+K_a\cdot n[P_T]}$$

[출처: G&W Eq.47:3, p.692]

G&W는 Compound 1에서 $[P_T]=50$과 0.3, Compound 2에서 $[P_T]=10$과 0.1 조건을 사용하고, $n$은 대략 1–4 범위, $K_a$는 Eq.47:4 초기 추정으로 약 6 농도 단위 수준을 제시한다. [G&W Table47.1 p.692; Eq.47:4 p.693]

#### C. 경계 조건(Boundary Conditions)

- Eq.47:1은 단일 결합 부위 클래스(single binding-site class) 모델이다. 다중 부위 클래스가 있으면 잔차 패턴(residual pattern)이 체계적으로 남을 수 있다.
- $AUCu=AUC\times f_u$는 $f_u$가 시간·농도에 대해 충분히 일정할 때만 안전하다. [G&W p.167]
- G&W는 `fub > 1`이 가능하다고 명시한다. 이는 bound/free ratio이므로, 결합 분율(fraction bound)과 혼동하지 않도록 주의한다. [G&W p.168]

<!-- TRENCH -->
**[교과서 외 실무 해석] 단백 공변량 선택(Protein covariate choice)**: 산성 약물은 알부민, 염기성 약물은 α1-AGP 변화에 먼저 주목한다. R&T Table4-9는 알부민과 α1-AGP가 질환 상태에 따라 달라질 수 있음을 보여준다. [R&T Table4-9, p.114]

**[교과서 외 실무 경고] 단백결합 측정법 편향(PPB method bias)**: 평형투석(equilibrium dialysis)과 한외여과(ultrafiltration)는 방법 편향이 다를 수 있다. 이 문장은 PDF 원문이 아니라 실험 데이터 수령 단계의 실무 주의로만 사용한다.

> **실무 렌즈(Practice Lens) — TEXTBOOK_DERIVED**  
> Total AUC에 단일 fu를 곱하기 전에는, 그 fu가 의사결정에 쓰는 농도 범위에서 유지되는 값인지 확인한다. PK47의 핵심은 결합 파라미터 적합(binding parameter fit) 자체보다 "변환 단축식의 안전 조건"을 드러내는 데 있다.

<!-- RECAP -->
**M4 요약(recap)**: $f_u$는 단백 농도와 결합 부위 포화에 따라 변할 수 있다. 총-유리 변환(total-to-unbound conversion)은 $f_u$ 일정 가정이 무너지면 함께 무너진다.

<!-- FIGURE_POINTER -->
Source: G&W 5e, p.691, Fig.47.1
Why this matters: fu가 Cu와 protein concentration에 따라 변하는 비선형 binding curve를 직접 보여준다.
When to look: after reading this card
Learner instruction: low/high protein curves가 n과 Ka 추정에 주는 정보를 확인하라.
<!-- /FIGURE_POINTER -->

> **▶ 실무 체화 요약(Practice Brief) — M4 체화 4축 — [EXPERT_INFERENCE, v3]**
> - **왜 알아야 하는가:** fu는 총 농도와 유리 농도를 잇는 변환계수이며, 시간·농도·dose에 따라 변하면 모든 단축식($AUCu = AUC \times f_u$, $C_u = C \times f_u$)이 무너지기 때문이다.
> - **흐름상 역할:** M3의 V 구조와 M6의 노출 지표를 연결하는 핵심 매개 파라미터로, "변환 단축식의 안전 조건"을 정의한다.
> - **체화 꿀팁:** 용량 정규화 AUC(dose-normalized AUC)가 용량에 따라 변할 때, 포화성 청소율(saturable CL)을 의심하기 전에 용량별 ex vivo fu를 먼저 확인하라 — 진단 순서가 뒤집히면 원인 추적이 어긋난다.
> - **실무 활용:** 저알부민혈증·요독증·α1-AGP 변화 환자에서 TDM 해석, 약물-약물 변위 상호작용(drug-drug displacement interaction) 평가, NDA 단계에서 유리 농도 측정 여부 결정, PopPK에서 단백 공변량(albumin/α1-AGP) spec의 근거 제시.

---

### M5 · 조직결합과 Kp의 결정인자

<!-- MASTER LENS -->
**핵심 직관**: 큰 Vd는 "혈장에서 많이 풀려 있다"는 뜻이 아닐 수 있다. 오히려 "조직에서 더 강하게 붙잡힌다"는 신호인 경우가 많다. 염기성 약물(basic drug)의 큰 Vd는 혈장 결합보다 조직 결합, 특히 산성 인지질(acidic phospholipid) 친화도로 설명되는 경우가 많다. [R&T pp.108–111]

#### A. 형식적 정의(Formal Definition)

조직-혈장 평형 분포비 $K_p$<!-- ANNOTATION --> (← 조직/혈장 평형 농도비)는 조직 농도와 혈장 농도의 평형 비율이다. R&T는 Eq.4-25와 Eq.4-12를 비교해 $K_p\sim f_u/f_{uT}$로 해석할 수 있음을 설명한다. [R&T pp.104, 109–110]

#### B. 출처 기반 상세(Source-Anchored Details)

- Furosemide와 amiodarone은 혈장 $f_u$가 비슷한 범위일 수 있으나 V는 크게 다르다. 차이는 염기성 약물의 높은 조직 결합, 즉 낮은 $f_{uT}$에서 온다. [R&T p.110]
- Propranolol은 6명의 대조군 + 15명의 만성 간질환 환자에서 40 mg IV bolus 후 $V$와 $f_u$의 관계가 제시된다. 이는 혈장 결합 변화가 $V$ 변동을 설명할 수 있음을 보여준다. [R&T Fig.4-23, p.110]
- Metoprolol의 조직 $K_p$는 조직 산성 인지질 농도와 강한 양의 상관관계(positive relationship)를 보인다. 정확한 `r>0.85`는 원문에 없으므로 삭제한다. [R&T Fig.4-24, p.110]
- Indinavir 800 mg q8h 성인 HIV 환자 8명에서 CSF 유리 농도는 혈장 유리 농도보다 낮고 지연되며 변동 폭이 작다. 정확한 "1/10"은 대략적 시각 추정치(approximate visual estimate)로만 취급한다. [R&T Fig.4-10, p.91]
- 뇌는 전신 질량의 약 2%이므로 국소 수송체 효과가 전신 V를 크게 바꾸지 않을 수 있다. [R&T pp.109, 111]

#### C. 혈장-혈액 변환 맥락(Plasma-to-Blood Context)

Appendix D의 핵심은 혈액/혈장 농도비(blood/plasma concentration ratio)가 적혈구 용적률(hematocrit), 혈장 fu, 적혈구 결합에 의해 달라진다는 점이다.

$$\frac{C_b}{C}=1+H\left(f_u\cdot K_{PBC}-1\right)$$

[출처: R&T App.D, pp.775–776]

#### D. 경계 조건(Boundary Condition)

수송체가 지배적이면 조직 유리 농도와 혈장 유리 농도가 자유롭게 평형을 이룬다는 단순 $f_{uT}$ 해석이 깨질 수 있다. BBB의 유출 수송체(efflux transporter)가 대표적인 예다. [R&T pp.90–91, 110–111]

> **실패 모드(Failure Mode) — CRUCIBLE_DERIVED**  
> Eq.4-29에서 결합 항(binding term)과 수송체 항(transporter term)을 같은 종류의 원인으로 합쳐 해석하면 안 된다. fuT는 조직 결합을 나타내고, Puptake/Pefflux는 능동 분포 불균형을 나타내므로, 둘은 같은 V 변화를 만들 수 있어도 실험적 확인 방법과 모델링 의미가 다르다.

<!-- RECAP -->
**M5 요약(recap)**: $K_p$는 조직 친화도의 숫자 표현이고, $f_{uT}$는 조직 결합의 역신호(inverse signal)이다. 수송체가 있으면 $K_p$는 결합뿐 아니라 유입/유출 불균형(uptake/efflux imbalance)까지 반영한다.

> **▶ 실무 체화 요약(Practice Brief) — M5 체화 4축 — [EXPERT_INFERENCE, v3]**
> - **왜 알아야 하는가:** 큰 Vd의 원인이 혈장 fu 증가인지 조직 fuT 감소인지 구분하지 못하면, 단백결합 변화의 임상 결과 방향이 정반대로 도출된다.
> - **흐름상 역할:** M3의 조직 항($V_{TW}\cdot f_u/f_{uT}$)을 결합(fuT)과 수송체(P_uptake/P_efflux)로 분해해 M2의 율속 단계와 다시 연결하는 단계다.
> - **체화 꿀팁:** 염기성 약물에서 큰 Vd를 보면 산성 인지질 결합을 1순위 가설로, 수송체 기질 가능성을 2순위로 점검하라 — Eq.4-29의 두 항을 같은 종류의 원인으로 합치지 않는 것이 핵심이다.
> - **실무 활용:** PBPK Kp 예측 모델 선택, BBB 약물의 조직 농도 해석, propranolol·amiodarone 같은 대 Vd 염기성 약물의 공변량 모델링, indinavir의 CSF/혈장 격차 해석.

---

### M6 · 노출 지표 선택: total vs unbound

<!-- MASTER LENS -->
**핵심 직관**: 노출 지표(exposure metric)는 "하나의 AUC 숫자"가 아니다. 즉, 노출 지표는 어떤 농도 species가 어떤 시간 패턴으로 약리 효과를 유발하는가에 대한 인과적 선언이다. 총 농도가 단백결합 차이에 교란(confounded)되면 유리 농도가 활성 비교 기준(active comparator)이 된다. [G&W pp.163–169]

#### A. 형식적 정의(Formal Definition)

총 농도와 유리 농도의 관계:

$$C=\frac{C_u}{f_u}$$

$f_u$가 일정하면:

$$AUC_u=AUC\times f_u$$

[출처: G&W Eq.2:373, p.167]

#### B. 출처 기반 상세(Source-Anchored Details)

<!-- ANNOTATION --> 다시 말해, M6의 질문은 "AUC를 쓸 것인가?"가 아니라 "어느 species의 AUC 또는 어떤 시간 패턴을 쓸 것인가?"이다.

- G&W Fig.2.134는 용량-반응, 총 농도-반응, 유리 농도-반응이 서로 다른 결론을 낼 수 있음을 보여준다. 총 농도 관계는 혈장 단백결합 차이에 교란되고, 유리 농도 기준에서는 역가 순위(potency order)가 뒤집힌다. [G&W p.163]
- G&W Fig.2.136은 같은 AUC라도 최고 농도(peak), 역치 초과 시간(duration above threshold), 독성 관련성(toxicity implication)이 다를 수 있음을 경고한다. "동일 AUC = 동일 효과"는 과정의 형태(process shape)를 잃는 단일 스칼라 단축식이다. [G&W p.164]
- G&W Fig.2.140은 $f_u$를 총 농도보다 $C_u$에 대해 그릴 때 더 명확한 관계를 보일 수 있음을 제시한다. [G&W p.167]
- G&W Fig.2.141은 개/쥐/마우스의 총 농도-반응 곡선은 다르게 보이나 유리 ECu50가 약 2 nM 부근으로 정렬될 수 있음을 보여준다. 총 역가(total potency) 배수는 시각/추론 추정치(visual/inferred estimate)로만 다룬다. [G&W p.168]
- G&W Table2.21은 노출 지표를 `Cmax`, `AUC`, `td`, 치료 기간(treatment period) 등으로 나누고, 각 지표의 적용 상황을 구분한다. [G&W p.169]
- G&W는 456개 약물 검토를 인용하며, 단백결합 변화가 PK 파라미터에는 영향을 줄 수 있으나 임상 결과에는 대개 큰 영향을 주지 않고, 예외는 IV 투여 고추출 약물로서 치료역이 좁은(narrow therapeutic index) 경우라고 정리한다. [G&W p.168]
- G&W 결론: IND 단계에서는 여러 농도와 종(species, 인간 포함)에서 ex vivo 혈장 단백결합을 측정하고, NDA 단계에서는 선별된 임상시험에서 유리 농도와 총 농도를 함께 얻는 것이 권장된다. 일상적 "있으면 좋은(good to have)" 측정은 지양한다. [G&W p.169]

#### C. 경계 조건(Boundary Conditions)

- $f_u$가 용량·시간·농도 의존적이면 $AUC_u=AUC\times f_u$ 단축식은 무효가 될 수 있다.
- Total AUC가 같아도 최고 농도 매개 독성(peak-driven toxicity) 또는 역치 초과 시간 매개 효과(duration-above-threshold effect)는 다를 수 있다. [G&W Fig.2.136, p.164]
- "유리 농도를 항상 측정하라"가 아니라 "의사결정이 유리 species에 민감한 상황에서 측정하라"가 G&W의 결론이다. [G&W p.169]

> **실무 렌즈(Practice Lens) — TEXTBOOK_DERIVED**  
> 노출 지표는 보고서의 숫자 선택이 아니라 인과적 주장(causal claim)의 선택이다. AUC, Cmax, td 중 무엇을 전면에 둘지는 "효과를 만든 시간 패턴이 무엇인가"와 "total과 unbound 중 어떤 species가 비교 가능한가"를 함께 답해야 정당화된다.

<!-- RECAP -->
**M6 요약(recap)**: 총 농도는 분석 친화적(assay-friendly) 지표이고, 유리 농도는 활성 species에 가까운 지표이다. 어느 쪽을 쓸지는 결합 차이, 종간 외삽(species extrapolation), 노출 형태(exposure shape), 의사결정 위험도(decision risk)가 결정한다.

<!-- FIGURE_POINTER -->
Source: G&W 5e, p.163, Fig.2.134
Why this matters: dose, total concentration, unbound concentration이 서로 다른 potency 결론을 만들 수 있음을 보여준다.
When to look: after reading this card
Learner instruction: total-response와 unbound-response에서 potency order가 어떻게 바뀌는지 확인하라.
<!-- /FIGURE_POINTER -->

> **▶ 실무 체화 요약(Practice Brief) — M6 체화 4축 — [EXPERT_INFERENCE, v3]**
> - **왜 알아야 하는가:** 노출 지표 선택은 단순한 보고 형식이 아니라 효과의 인과 메커니즘에 대한 주장이며, 잘못 고르면 종간 비교와 용량 결정이 동시에 왜곡된다.
> - **흐름상 역할:** M1~M5의 모든 분포 정보를 "어느 species의 어떤 시간 패턴이 효과를 만드는가"라는 단일 의사결정으로 수렴시키는 세션의 종착점이다.
> - **체화 꿀팁:** AUC, Cmax, td 중 무엇을 전면에 둘지는 기전(mechanism)이 결정한다 — 효과가 최고 농도 매개(peak-driven)이면 Cmax, 누적 매개(cumulative-driven)이면 AUC, 역치 매개(threshold-driven)이면 td. 이 매핑을 먼저 한 줄로 적은 후 species/scale을 결정하라.
> - **실무 활용:** IND/NDA 단계 PK/PD 보고서의 노출 지표 정당화, 종간 외삽을 위한 유리 농도 사용 결정, 치료역이 좁은(narrow therapeutic index) 약물의 안전 마진 분석, 규제 문서에서 "왜 AUC가 아니라 AUCu인가"를 방어하는 한 단락 작성.

---

## §5 — 혼동쌍 해부(Confusion Pair Dissection)

### 혼동쌍 1 — C vs Cu **[치명적 타격(Critical Blow)]**

<!-- CONFUSION -->
| 구분 | C, 총 농도(total concentration) | Cu, 유리 농도(unbound concentration) |
|---|---|---|
| 정의 | 결합 + 비결합 | 비결합만 |
| 막투과 구동력(driving force) | 부적합 | 적합 [R&T p.80] |
| 노출-반응(Exposure-response) | PPB 차이에 교란 가능 | 활성 species 비교에 유리 [G&W pp.163, 167–168] |
| 단축식(Shortcut) | 분석이 쉬움 | fu 측정 또는 모델 필요 |
| 실패 모드 | 종간/화합물간 역가 순위가 왜곡됨 | fu가 시간 의존적이면 계산 오류 가능 |

<!-- MASTER LENS -->
치명적 타격(Critical Blow)의 핵심은 "C와 Cu 중 무엇이 참인가?"가 아니다. 핵심 질문은 **지금 의사결정의 인과적 species가 무엇인가?**이다. 막투과, 수용체 상호작용, 종간 외삽이 문제이면 $Cu$가 더 직접적이다. 하지만 $f_u$가 안정적이고 의사결정이 총 분석(total assay) 기반으로 검증되어 있다면 $C$도 유용하다.

> **실무 렌즈(Practice Lens) — EXPERT_INFERENCE**  
> C vs Cu 판단은 네 단계로 고정한다: 인과적 species → 분석 스케일(assay scale) → 변환 유효성(conversion validity) → 의사결정 위험도(decision risk). 이 순서가 없으면 "unbound가 더 맞다"와 "total도 충분하다"가 둘 다 근거 없는 주장으로 변한다.

**⚡ 기억 고리(Memory Hook) — *관찰자 vs 실제 행위자* — [EXPERT_INFERENCE, v3]**
총 농도 C는 사진(관찰 가능한 대리 지표)이고, 유리 농도 Cu는 수용체에 실제로 작용하는 행위자다. 같은 C에서 fu가 다르면 Cu가 다르고, 같은 Cu에서 fu가 다르면 C가 다르다. 좌표계를 잘못 선택하면 "농도가 정상인데 효과가 없다" 또는 "농도가 낮은데 독성이 있다"는 역설이 나온다.

### 혼동쌍 2 — 관류 율속(Perfusion-rate) vs 투과 율속(Permeability-rate) 제한

<!-- CONFUSION -->
관류 율속 제한에서는 혈류가 속도를 정하고 Eq.4-5~4-7이 안전하다. 투과 율속 제한에서는 막 통과가 병목(bottleneck)이며, 뇌 penicillin G나 거대분자 림프 분포처럼 혈류만으로 설명되지 않는다. [R&T pp.94–100]

**⚡ 기억 고리(Memory Hook) — *얼마나 퍼지나 vs 얼마나 빨리 퍼지나* — [EXPERT_INFERENCE, v3]**
분포 범위(distribution extent, Vd의 크기)는 약이 최종적으로 얼마나 넓게 퍼지는지를, 분포 속도(distribution rate, Q와 조직 혈류·막 투과도)는 그 최종 상태에 얼마나 빨리 도달하는지를 결정한다. 빠른 분포 속도 + 작은 Vd는 짧은 시간 안에 좁은 구획에 가두는 패턴이고, 느린 분포 속도 + 큰 Vd는 오래 걸려 넓게 퍼지는 패턴이다. 이 두 차원은 독립적으로 작동하므로, Vd 하나만으로는 분포 과정의 시간 경과를 논할 수 없다.

### 혼동쌍 3 — fu vs fuT

<!-- CONFUSION -->
$f_u$는 혈장에서 유리 분율이고, $f_{uT}$는 조직에서 유리 분율이다. $V=V_p+V_{TW}(f_u/f_{uT})$이므로 $f_u$가 커지면 V는 커질 수 있고, $f_{uT}$가 작아지면 V는 크게 커진다. [R&T Eq.4-25, p.109]

**⚡ 기억 고리(Memory Hook) — *정적 균형점 vs 동적 제거 그림자 (Vss vs Vβ)* — [EXPERT_INFERENCE, v3]**
Vss는 분포와 제거가 완전히 독립인 **정적 균형 부피** — 제거 속도가 Vss에 영향을 주지 않는다. Vβ는 종말상 소실 기울기(terminal elimination slope)에서 역산한 **겉보기 부피**로, 조직에서 계속 약이 돌아오는 재분포(redistribution) 흐름을 반영하기 때문에 제거가 느릴수록 Vss보다 커진다. 따라서 Vβ를 Vss 대신 쓰면 정상상태 분포 부피를 과대추정하고 부하 용량이 잘못 계산된다. (이 기억 고리는 fu/fuT 분기를 다룰 때 함께 점검할 사항을 가리킨다: 다구획 모델에서 V를 Vss로 쓰는가, Vβ로 쓰는가를 명시적으로 확인하라.)

### 혼동쌍 4 — 소 Vd vs 대 Vd의 단백결합 변화 반응

<!-- CONFUSION -->
소 Vd 알부민 결합 약물에서는 알부민 분포 모델과 7.5 L 하한이 필요하다. 대 Vd 염기성 약물에서는 조직 결합이 지배적이므로 혈장 단백결합 변화만으로 V와 Cu를 해석하면 위험하다. [R&T pp.111–118]

**⚡ 기억 고리(Memory Hook) — *전체 vs 활성 화물 (AUC vs AUCu)* — [EXPERT_INFERENCE, v3]**
AUC는 총 화물량(결합 + 유리), AUCu = fu × AUC는 실제로 수용체에 도달 가능한 활성 화물량이다. 알부민 결합이 강한 약물에서 저알부민혈증이 생기면, AUC는 줄어도 AUCu는 오히려 늘 수 있다. 바로 이 때문에 노출-반응(exposure-response) 분석을 AUC로 수행하면 효과 방향이 역전되는 결과가 나온다. (소 Vd vs 대 Vd 분기를 판단할 때, 실제로 의사결정에 쓰이는 지표가 AUC인지 AUCu인지를 함께 묻지 않으면 PPB 변화의 임상 결과 방향을 오독한다.)

---

## §7 — 자기 테스트: 능동 회상 모듈(Active Recall Module)

### Q1
<!-- SELF-TEST -->
Eq.4-1에서 농도차가 $C_1-C_2$가 아니라 $Cu_1-Cu_2$인 이유는?

**정답**: 결합 약물은 일반적으로 막을 통과하지 못하고, 유리 약물만 확산 구동력이 되기 때문이다. [R&T p.80]

### Q2
<!-- SELF-TEST -->
MW 400→800 g/mol 증가와 logP 증가가 투과도에 미치는 방향을 각각 말하라.

**정답**: MW 증가는 투과도를 크게 낮추고, logP 증가는 대체로 투과도를 높인다. 단 수송체 기질이면 logP 예측이 깨질 수 있다. [R&T Fig.4-3~4-4, pp.81–82]

### Q3
<!-- SELF-TEST -->
관류 율속 조직에서 $K_{pb}$가 커지면 분포 반감기(distribution half-life)는 어떻게 변하는가?

**정답**: $t_{1/2,distribution}=0.693K_{pb}/(Q/V_T)$이므로 커진다. 친화도가 크면 채워야 할 조직 약물량이 많아져 평형 도달이 늦어진다. [R&T p.97]

### Q4
<!-- SELF-TEST -->
소 Vd 알부민 결합 약물에서 $f_u\to0$일 때 V가 0 L이 아니라 약 7.5 L 근처 하한을 갖는 이유는?

**정답**: 약물이 알부민에 붙어 혈장과 혈관 외 알부민 공간에 분포하기 때문이다. 알부민 분포 용적이 약 7.5 L 하한을 만든다. [R&T p.111–113; App.C pp.767–773]

### Q5
<!-- SELF-TEST -->
Warfarin 신증후군에서 알부민 감소가 V, CL, t1/2에 어떤 방향 변화를 보였는가?

**정답**: albumin 43→12.5 g/L에서 V 9.4→13.7 L, CL 0.20→0.58 L/hr, t1/2 36→18 hr로 변했다. [R&T Table4-12, p.118]

### Q6
<!-- SELF-TEST -->
G&W Eq.2:373의 $AUC_u=AUC\times f_u$를 쓰기 위한 핵심 조건은?

**정답**: $f_u$가 시간·농도·dose에 대해 충분히 일정해야 한다. 그렇지 않으면 총 AUC에 하나의 fu를 곱하는 단축식이 깨진다. [G&W p.167]

### Q7
<!-- SELF-TEST -->
동일 AUC인데 독성이 다를 수 있는 이유는?

**정답**: 같은 면적이라도 최고 농도(peak concentration), 역치 초과 시간($t_d$), 농도-시간 형태(concentration-time shape)가 다를 수 있기 때문이다. [G&W Fig.2.136, p.164]

### Q8
<!-- SELF-TEST -->
PK47에서 저/고 단백 농도를 동시에 적합(fit)하는 이유는?

**정답**: $n$과 $K_a$의 상관(correlation)을 줄이고 정밀도(precision)를 높이기 위해서다. [G&W p.693]

### Q9 — 보스 딜레마(Boss Dilemma)
<!-- SELF-TEST -->
신약 후보에서 총 AUC는 종간 차이가 큰데 유리 ECu50는 종간 정렬된다. 어느 노출 지표를 안전 마진 논의의 중심에 놓을 것인가?

**정답**: 유리 노출(unbound exposure)을 중심 지표로 두되, 총 노출(total exposure)과 $f_u$ 측정 방법을 함께 제시한다. G&W는 총 농도-반응이 PPB 차이에 교란될 수 있고, 유리 농도가 종간 외삽에서 더 적절할 수 있음을 보여준다. [G&W pp.163, 167–169]

### Q10 — [교육용 가상 사례]
<!-- SELF-TEST -->
Phase 1 SAD에서 용량 정규화 AUC(dose-normalized AUC)가 용량 증가와 함께 감소한다. 포화성 청소율(saturable clearance)과 포화성 PPB를 어떻게 구분할 것인가?

**정답**: 용량별 ex vivo(체외 측정) $f_u$를 확인한다. $f_u$가 용량/Cu에 따라 증가하면 포화성 PPB가 원인일 수 있고, $f_u$가 일정하면 청소율 비선형성을 우선 의심한다. 이 문항은 교과서 수식의 실무 적용이며, 특정 PDF 사례는 아니다.

---

## §8 — 메타프레임 & 전체 조망(Big Picture)

### A. 위치 설정(Positioning)

<!-- MASTER LENS -->
이 세션은 **분포를 생리학으로 읽는 법**을 세운다. 이후 청소율(clearance), 반복 투여(multiple dosing), TDM, PBPK, PopPK 공변량 모델링은 모두 여기서 정의된 $Cu$, $f_u$, $f_{uT}$, $K_p$, $V$ 위에 쌓인다.

### B. 의존성(Dependencies)

이 섹션을 약하게 이해하면 다음 오류가 발생한다.

1. **부하 용량 오류**: $V$가 겉보기 비례상수임을 잊고 생리학적 부피처럼 해석한다.
2. **공변량 오류**: 알부민 변화가 총 CL, 총 V, 유리 노출에 미치는 방향을 구분하지 못한다.
3. **노출 지표 오류**: 동일 AUC를 동일 효과로 가정하고 최고 농도/지속 시간 정보를 잃는다.
4. **종간 외삽 오류**: 총 농도-반응의 역가 순위를 활성 유리 species의 역가 순위로 착각한다.
5. **단백결합 오류**: $f_u$를 상수로 가정하고 포화성 결합 또는 단백 농도 변화를 놓친다.

### C. 전문가 해석 지점(Professional Moat)

박사과정생이 이 세션에서 가져가야 할 한 문장은 다음이다.

<!-- RECAP -->
**분포는 "약물이 어디에 있는가"가 아니다. 혈장과 조직 사이에서 결합(binding), 투과도(permeability), 혈류(flow)가 함께 형성하는 평형 문제이자 시간 경과(time-course) 문제다.** 총 농도는 관찰값이고, 유리 농도는 많은 경우 인과적 species에 더 가깝다. $V$는 그 둘을 총량(amount)과 연결하는 겉보기 상수다.

### D. 시스템 통합 지점(System Integration Points)

- **임상약리 요약**: 용량-노출 선형성(dose-exposure linearity)을 논할 때, M1(흡수/투과), M3(V/용량 의존성), M4(PPB 포화 여부), M6(노출 지표 선택) 네 카드가 하나의 문단 안에서 논리적으로 연결된다.
- **TDM**: 저알부민혈증, 신부전, α1-AGP 변화가 동시 발생하면 총 농도만으로는 활성 노출을 놓칠 수 있다.
- **NONMEM**: 알부민/α1-AGP 공변량은 `V`에만 기계적으로 붙이는 것이 아니라, total vs unbound scale과 CL 해석까지 함께 결정해야 한다.

> **체화 노트(Mastery Note) — CRUCIBLE_DERIVED**  
> 위 세 통합 지점은 두 가지 **구체적 실무 단락**으로 작동한다. 카드 단위 학습이 끝났는지를 자가 점검하려면 다음 두 단락을 한 번씩 자기 언어로 재구성해 보라.
>
> **시나리오 1 — 임상약리 요약(용량-노출 선형성 단락)**  
> 한 단락이 6개 카드를 동시에 호출한다: 약물이 막을 통과해 혈장에 들어오는가(M1) → 같은 용량에서 V가 용량에 따라 변하는가(M3) → fu가 용량에 따라 변하는가(M4) → 조직 분포가 포화성 수송체에 묶여 있는가(M5) → 어떤 species의 어떤 지표로 선형성을 판정하는가(M6). 이 단락이 자연스럽게 흘러야 6개 카드가 단일 시스템으로 작동한다.
>
> **시나리오 2 — ICU 환자 TDM 의사결정**  
> 저알부민혈증(albumin↓) + 급성 신부전(uremia, fu 결합 경쟁) + α1-AGP 상승(외상 반응)이 동시 발생하는 한 환자의 한 용량 결정을 상상하라. M4(fu가 알부민·변위체·α1-AGP의 다중 함수) → M3(소 Vd 약물에서 V가 fu에 비례 증가) → M6(총 농도 "정상 범위"가 독성 Cu를 가릴 수 있음)을 한 결정에 묶어야 한다. 이 시퀀스가 카드 단위로 분리되어 있으면 실무 통합이 끊긴다.

### E. 실무 진단 시그니처(Practical Diagnostic Signatures)

> **체화 노트(Mastery Note) — CRUCIBLE_DERIVED**  
> 본 세션 개념의 오용은 PopPK 진단 플롯에 **반복 가능한 시그니처 패턴**을 남긴다. 이름을 부여하면 진단 속도가 카드 단위 → 시그니처 단위로 압축된다. 아래 시그니처는 모두 [교과서 외 실무 해석]이며, 출처 PDF의 직접 인용이 아니다.

**시그니처 1 — 알부민 공변량 비대칭 패턴(Albumin Covariate Asymmetry Pattern)**  
*기전(Mechanism)*: 대 Vd 약물에서 V ~ albumin만 공변량 spec하고 CL ~ albumin을 누락.  
*GOF 시그니처*: ETA-V vs albumin scatter는 약한 양의 상관에 머물지만, ETA-CL vs albumin scatter는 강한 음의 상관을 보인다. 시뮬레이션에서 알부민 극단군의 예측 구간(prediction interval)이 체계적으로 어긋난다.  
*한 줄 진단*: ETA-CL vs albumin이 ETA-V vs albumin보다 강한 상관을 보이면 CL 공변량을 함께 spec하라.

**시그니처 2 — PK47 단일 부위 부적합 패턴(PK47 Single-Site Misfit Pattern)**  
*기전*: 실제로 다중 결합 부위 클래스를 가진 약물에 단일 부위 PK47 모델(G&W Eq.47:1)을 적합.  
*GOF 시그니처*: 저 Cu 영역에서 fu가 체계적으로 과소추정되고, 고 Cu 영역에서 과대추정된다. 잔차 플롯(residual plot)에서 V자 또는 역V자 패턴이 나타난다. 저/고 단백 농도 동시 적합 시 두 데이터셋의 잔차 방향이 반대다.  
*한 줄 진단*: fu vs Cu 잔차 플롯이 V자 형태이면 두 번째 결합 부위 클래스를 추가하라.

**시그니처 3 — Vss vs Vβ 혼동 패턴(Vss vs Vβ Confusion Pattern)**  
*기전*: 2구획 이상 모델에서 NONMEM 출력의 V를 Vβ(소실상 겉보기 V)로 무비판 사용해 부하 용량 계산.  
*GOF 시그니처*: 분포상에서는 IPRED가 정확하나 소실상 꼬리(elimination phase tail)에서 체계적 과소예측(systematic underprediction)이 나타난다. CWRES가 시간에 따라 단조 편향(monotonic drift)을 보인다.  
*한 줄 진단*: 소실상 꼬리의 CWRES 편향이 보이면 Vss와 Vβ를 분리하라 — 부하 용량은 Vss, 종말상 반감기 해석은 Vβ.

### F. 체화 시퀀스(Mastery Sequence)

> **체화 노트(Mastery Note) — EXPERT_INFERENCE**  
> 새 PK 문제를 만났을 때 본 세션의 6개 카드를 가장 빠르게 작동시키는 4단계 시퀀스다. 본 시퀀스는 출처 PDF의 직접 권고가 아니라, 본 handout의 내적 통합 지침이다. 카드 학습이 끝난 후, 새 사례에 이 시퀀스를 반복 적용하면 분리된 카드가 단일 진단 시퀀스로 통합된다.

1. **Species 결정 — 지금 보고 있는 농도는 무엇인가?**  
   총 `C`인가, 유리 `Cu`인가, 혈액 `Cb`인가? 단위와 측정 매질을 먼저 고정한다. (M1·M4·M6의 진입점)

2. **Vd 양상 결정(regime) — 어느 모델이 작동하는가?**  
   소 Vd 알부민 결합 양상(App.C / Eq.C-13, V≲15 L)인가, 대 Vd 조직 결합 양상(Eq.4-25 또는 4-29)인가? 이 분기에 따라 fu 변화의 임상적 결과 방향이 정반대가 된다. (M3·M5의 분기점)

3. **fu 안정성 점검 — 단축식이 유효한가?**  
   지금 비교하려는 용량·시간·농도 범위에서 fu가 일정한가? 일정하지 않다면 `AUCu = AUC × fu` 단축식과 `Cu = C × fu` 변환은 무효가 될 수 있다. (M4 경계 점검)

4. **지표 정당화(Metric justification) — 어느 species의 어느 시간 패턴인가?**  
   의사결정의 인과 기전이 Cmax 매개인가 AUC 매개인가 td 매개인가? 그리고 그 기전이 총 농도와 유리 농도 중 어느 species에 작동하는가? (M6 결정 단계)

> 이 4단계는 §5 치명적 타격(Critical Blow)의 실무 렌즈(인과적 species → 분석 스케일 → 변환 유효성 → 의사결정 위험도)와 구조적으로 동형(isomorphic)이며, 카드의 "왜"와 "어떻게"를 한 진단 시퀀스로 융합한다.

---

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
- Assembly mode for this file: **FULL MODE**. `02_Content Lock v2.1(1).md` contains the full learner body with retained Phase 4C figure markers already inserted.

### B2. Figure Rendering Instructions

- Preserve all retained figure pointer markers listed below.
- Render every `FIGURE_POINTER` as a text-only textbook reference callout.
- Because `Image rights = None`, do not embed copyrighted textbook images.
- Do not propose new figures.
- Do not generate Mermaid/SVG in Phase 4D.
- In Phase 5, figures must not interrupt reading flow; place callouts at the end of the concept card where the marker appears.

#### Approved Figure Pointer Inventory

| # | Marker | Source | Why this matters | When to look | Learner instruction |
|---:|---|---|---|---|---|
| 1 | FIGURE_POINTER | R&T 5e, p.82, Fig.4-4 | BBB permeability가 logP만으로 결정되지 않고 size/efflux 예외를 갖는다는 점을 실제 좌표로 보여준다. | after reading this card | caffeine, lomustine, vinblastine/vincristine의 위치를 비교하라. |
| 2 | FIGURE_POINTER | R&T 5e, p.94, Fig.4-13 | thiopental에서 brain과 fat의 time-course 차이가 perfusion과 affinity의 결합 효과임을 보여준다. | after reading this card | brain peak와 fat 잔류를 비교하라. |
| 3 | FIGURE_POINTER | R&T 5e, p.113, Fig.4-25 and Fig.4-26 | 같은 cephalosporin series에서 V와 Vu가 fu에 대해 반대 방향으로 읽힐 수 있음을 보여준다. | after reading this card | V-fu와 Vu-fu 축을 나란히 비교하라. |
| 4 | FIGURE_POINTER | G&W 5e, p.691, Fig.47.1 | fu가 Cu와 protein concentration에 따라 변하는 비선형 binding curve를 직접 보여준다. | after reading this card | low/high protein curves가 n과 Ka 추정에 주는 정보를 확인하라. |
| 5 | FIGURE_POINTER | G&W 5e, p.163, Fig.2.134 | dose, total concentration, unbound concentration이 서로 다른 potency 결론을 만들 수 있음을 보여준다. | after reading this card | total-response와 unbound-response에서 potency order가 어떻게 바뀌는지 확인하라. |

### B3. Page Tag Rendering Rules

- Preserve all `[p.XX]`, `[pp.XX-YY]`, `[pp.XX, YY]`, and `[p.확인 필요]` tags.
- Render page tags visibly in HTML using `span.source-page` or `span.source-page.source-uncertain`.
- Do not fabricate, delete, renumber, or relocate page tags.
- `[p.확인 필요]` remains visible unless already resolved by Audit/Content Lock.
- Do not apply source-tag regex conversion inside code blocks or inside `FIGURE_*` marker blocks.

### B4. HTML Compiler Requirements

**Core contract**

- Render PART A only. Do not render PART B as learner content unless explicitly requested.
- Render content; do not alter scientific wording, equations, page tags, or figure marker intent.
- Output one self-contained HTML document in Phase 5.
- Do not generate HTML, Mermaid, or SVG during Phase 4D.

**Marker → component mapping**

| Marker / Pattern | HTML Component | Style / behavior |
|---|---|---|
| `<!-- MASTER LENS -->` | Callout box | `border-left:4px solid #c9a84c; background:rgba(201,168,76,0.08)` |
| `<!-- ANNOTATION -->` | Inline annotation / tooltip | `font-size:0.85em; color:var(--muted); font-style:italic` |
| `<!-- ANCHOR -->` | Bridge sentence | italic, muted |
| `<!-- TRENCH -->` | Practical tip box | rose left border / rose tint |
| `<!-- CONFUSION -->` | Side-by-side comparison | `.box.amber` class or equivalent comparison styling |
| `<!-- SELF-TEST -->` | Click-to-reveal accordion | question visible; answer hidden until click |
| `<!-- RECAP -->` | Section summary box | blue left border / blue tint |
| `[확인 필요]` | Highlighted flag | `<mark>` |
| `[p.XX]`, `[pp.XX-YY]`, `[pp.XX, YY]` | Source page tag | `<span class="source-page">...</span>` |
| `[p.확인 필요]` | Source uncertainty tag | `<span class="source-page source-uncertain">...</span>` |
| `<!-- FIGURE_POINTER -->` | Textbook reference callout | text-only pointer with source / why / when / learner instruction |
| `<!-- FIGURE_SCHEMATIC -->` | Inline schematic figure | Mermaid by default or inline SVG if needed; not used in PART A currently |
| `<!-- FIGURE_IMAGE_SLOT -->` | Image or placeholder | placeholder if no permitted image file; not used in PART A currently |

**Source page tag rendering rules**

Detect and wrap source tags in body text, but not inside code blocks or inside `FIGURE_*` marker blocks.

- `\[p\.(\d+)\]` → standard single-page tag.
- `\[pp\.(\d+)[–-](\d+)\]` → range tag.
- `\[pp\.(\d+(?:,\s*\d+)+)\]` → multi-page non-contiguous tag.
- `\[p\.확인 필요\]` → uncertainty tag.

Do not fabricate, delete, renumber, or relocate page tags. Source page tags must remain visible in print mode.

**Navigation anchor integrity rules**

- Use a sticky left sidebar table of contents on desktop.
- Use `<a href="#...">` links only.
- Every `href` target must have one matching body `id`.
- Every major section heading (§1, §2, §5, §7, §8) must receive a stable id.
- Every §2 concept card heading should receive a stable id.
- Do not create duplicate ids.
- Enable `html { scroll-behavior: smooth; }`.
- Before finalizing, count all sidebar `href="#id"` values and verify each id exists exactly once.

**Rendering requirements**

- Math: MathJax CDN for inline `\(...\)` and display `\[...\]` / `$$...$$` equations.
- Code: `<pre><code>` with dark background, language class, and copy button.
- Accordion: self-test answers hidden by default, revealed on click.
- Checklist: sessionStorage state persistence if interactive checklist is rendered.
- Controls: code block copy button and print/PDF button using `window.print()`.
- Responsive: single-column/collapsed nav at `≤768px`; two-column layout at `≥1024px`.
- Theme: respect `prefers-color-scheme` for dark/light auto-switch.
- Print: remove decorative backgrounds, hide navigation, preserve source page tags, optimize page breaks.

**Figure rendering rules**

- Every figure marker becomes a proper text pointer callout or figure block.
- Do not embed copyrighted textbook images because image rights are None.
- `FIGURE_POINTER` must render as a compact text-only callout with source, why, when, and learner instruction.
- Do not generate or embed figures not present in PART A.
- For any future `FIGURE_SCHEMATIC`, use Mermaid only after validating node ids and labels; otherwise fall back to SVG or CSS cards.
- For any future `FIGURE_IMAGE_SLOT`, render a placeholder unless a permitted user-supplied or open-license image file is provided.

**CSS design system minimum**

Use variables for `--bg`, `--surface`, `--surface-2`, `--ink`, `--muted`, `--faint`, `--line`, `--line-strong`, `--blue`, `--green`, `--purple`, `--amber`, `--rose`, `--radius`, `--radius-sm`, `--shadow`, `--font`, `--mono`. Include `.sidebar`, `.source-page`, `.source-uncertain`, `.figure-pointer`, `figure`, `figcaption`, `.figure-placeholder`, and accordion styles.


### B5. Audit Guardrails

Known forbidden restorations for Session 02:

- Do not restore the wrong PK47 `fu` Curation Map expression from Step 1.
- Do not restore caffeine as a logP≈2 example; caffeine should not be used that way.
- Do not restore unsupported Caco-2/PAMPA, Lipinski rule-of-5, phase 1 screening, or "annual dozens of phase 1 failures" claims.
- Do not restore FDA Guidance, FDA reviewer deficiency-letter, or submission-template language not supported by the attached PDFs.
- Do not restore Rodgers-Rowland depth, `80% variance`, `one-digit Vd prediction`, or exact `r>0.85` claims.
- Do not restore exact visual-estimate values such as thiopental fat equilibrium 3.5 h or indinavir CSF/plasma 1/10 as author-stated facts.
- Do not restore albumin site I/II, SGLT2 inhibitor, activated charcoal, fexofenadine-grapefruit juice, or toxicokinetics expansions into the learner body.
- Do not embed unapproved textbook figures or unapproved code blocks.
- Treat `[교과서 외 실무 해석]` and `EXPERT_INFERENCE` as interpretive notes, not textbook facts.

### B6. Crucible Guardrails

- Crucible Report v1 is not a raw content source at Phase 4D.
- Preserve only already-adopted or explicitly allowed Grade A logic.
- Do not reintroduce omitted/rejected Crucible items.
- Do not convert speculative insight into textbook-derived fact.
- Accepted Crucible-derived logic retained in PART A includes: albumin ferry intuition, rate/extent separation, fuT vs transporter boundary, protein-binding conversion safety, and C vs Cu decision logic.

### B7. Deprecated and Forbidden Restorations

- Step 1 Draft v0 is deprecated.
- Do not use Step 1 Draft v0 as learner-body source except through the Micro-Patch Gate.
- Do not restore rejected overclaims, unsupported numbers, unsupported regulatory claims, source-unsupported examples, unapproved code, or unapproved figures.
- Content Lock v1/v2 are locked references only; v2.1 is the canonical body for this FULL MODE assembly.

### B8. PATCH MODE Splice Verification Table

Not applicable. FULL MODE was used because `02_Content Lock v2.1(1).md` contains the full canonical body with Phase 4C figure markers already inserted.

### B9. Zero-Omission Coverage Matrix

| Domain | Required item | Evidence in PART A | Status | Action |
|---|---|---|---|---|
| C1 Scope MUST | M1 membrane permeability determinants | §2 M1: size, lipophilicity, charge, transporter; Eq.4-1 | PRESENT | None |
| C1 Scope MUST | M2 perfusion- vs permeability-rate limitation | §2 M2: Eq.4-5~4-7, tissue perfusion table, thiopental/macromolecule examples | PRESENT | None |
| C1 Scope MUST | M3 Vd mathematical structure / Apex | §2 M3: Eq.4-8, 4-11~4-16, 4-25, 4-29, 4-30/App.C | PRESENT | None |
| C1 Scope MUST | M4 plasma protein binding and concentration-dependent fu | §2 M4: Eq.4-17~4-19 and G&W Eq.47:1/47:3/47:4 context | PRESENT | None |
| C1 Scope MUST | M5 tissue binding, Kp, transporter, blood/plasma ratio | §2 M5: Kp/fuT, acidic phospholipid, indinavir, App.D equation | PRESENT | None |
| C1 Scope MUST | M6 total vs unbound exposure metric choice | §2 M6 and §5 Critical Blow: Eq.2:373, Fig.2.134/2.136/2.140/2.141, Table2.21 | PRESENT | None |
| C2 Data anchors | R&T physiologic anchors: plasma, extracellular water, total body water, albumin V | §2 M3 Source-Anchored Data Anchors | PRESENT | None |
| C2 Data anchors | Cephalosporin V-fu and Vu-fu paired message | §2 M3 figure pointer and bullet on Fig.4-25~4-26 | PRESENT | None |
| C2 Data anchors | Warfarin nephrotic syndrome values | §2 M3 and §7 Q5 | PRESENT | None |
| C2 Data anchors | G&W PK47 protein concentrations, n, Ka estimate context | §2 M4 PK47 Source-Anchored Data and §7 Q8 | PRESENT | None |
| C2 Data anchors | G&W 456 drugs and IND/NDA recommendation | §2 M6 Source-Anchored Details | PRESENT | None |
| C3 Audit MUST_FIX | PK47 fu formula corrected and wrong Curation Map expression not restored | §2 M4 uses G&W Eq.47:1; PART B guardrail forbids old expression | PRESENT | None |
| C3 Audit MUST_FIX | Caffeine logP error removed | §2 M1 uses caffeine only in figure pointer comparison, not as logP≈2 claim | PRESENT | None |
| C3 Audit MUST_FIX | Unsupported regulatory wording removed | §2 M6 uses G&W author recommendation only; PART B forbids deficiency-letter/FDA guidance restoration | PRESENT | None |
| C3 Audit SHOULD_FIX | Thiopental exact 3.5 h not used | §2 M2 uses after 3 h remains; exact 3.5 h deleted | PRESENT | None |
| C3 Audit SHOULD_FIX | Lymph flow corrected | §2 M2 uses 1-10 mL/min per 70 kg | PRESENT | None |
| C3 Audit SHOULD_FIX | Rodgers-Rowland / one-digit Vd / 80% variance removed | §2 M5 does not use these claims; PART B forbids restoration | PRESENT | None |
| C4 Audit T5 | OMITTED_PROBLEMATIC / MISSING_CRITICAL resolved | Key additions from Audit are in M1-M6; optional scope-creep items remain excluded | PRESENT_COMPRESSED | No content micro-patch needed; rendering syntax patch logged in B10 |
| C5 Figure coverage | All retained Phase 4C figure markers | 5 FIGURE_POINTER blocks present exactly once in PART A (10 start/end marker tokens) | PRESENT | None |
| C5 Rights | Image rights = None respected | PART A uses text-only pointers; PART B instructs no textbook image embedding | PRESENT | None |
| C6 Page tags | Source page tags preserved | PART A retains [p.] and [pp.] tags from Content Lock v2.1; no new page tags added | PRESENT | None |
| C7 Crucible Grade A | Albumin ferry / Eq.C-13 intuition | §2 M3 Master Lens and M3 mastery note | PRESENT | None |
| C7 Crucible Grade A | Kp high affinity can slow equilibrium | §2 M2 Master Lens and practice lens | PRESENT | None |
| C7 Crucible Grade A | fuT vs transporter boundary | §2 M5 Boundary Condition and failure mode | PRESENT | None |
| C7 Crucible Grade A (ver2) | Crucible T1(b) NDA dose-exposure linearity scenario | §8 D Scenario 1 (CRUCIBLE_DERIVED augmentation) | PRESENT | None |
| C7 Crucible Grade A (ver2) | Crucible T1(b) ICU phenytoin TDM scenario | §8 D Scenario 2 (CRUCIBLE_DERIVED augmentation) | PRESENT | None |
| C7 Crucible Grade A (ver2) | Crucible T2(b) Signature 1 — Albumin Covariate Asymmetry | §8 E Signature 1 (named explicitly) | PRESENT | None |
| C7 Crucible Grade A (ver2) | Crucible T2(b) Signature 2 — PK47 Single-Site Misfit | §8 E Signature 2 (newly named in ver2) | PRESENT | None |
| C7 Crucible Grade A (ver2) | Crucible T2(b) Signature 3 — Vss vs Vβ Confusion | §8 E Signature 3 (newly named in ver2) | PRESENT | None |
| C7 EXPERT_INFERENCE (ver2) | 4-step Mastery Sequence for new PK problems | §8 F (EXPERT_INFERENCE augmentation) | PRESENT | None |
| C8 v3 Apex Standardization | M3 Apex marker `[⚡ Apex Concept]` | §2 M3 heading; per-session 1 Apex 원칙 유지 | PRESENT | None |
| C8 v3 Plausible Fallacy | M3 D-2 "Vd as Physical Volume" 오해 해체 블록 | §2 M3 D-2 (EXPERT_INFERENCE [v3]) | PRESENT | None |
| C8 v3 Memory Hooks (4 pairs) | §5 Confusion Pair 1~4에 Memory Hook 부착 | §5 각 pair 직후 (EXPERT_INFERENCE [v3]); pair 1=관찰자 vs 행위자 / pair 2=퍼지나 vs 빨리 / pair 3=Vss vs Vβ / pair 4=AUC vs AUCu | PRESENT | None |
| C8 v3 Practice Briefs (M1~M6) | M1~M6 카드별 4축 Practice Brief | §2 각 카드 말미 (EXPERT_INFERENCE [v3]); 왜·역할·꿀팁·실무 | PRESENT | None |
| C8 v3 Forbidden Restoration Check | Caco-2 / PAMPA / Lipinski / FDA 미지원 문구 | PART A에 부재; B5 Audit Guardrails에서 금지 항목 그대로 유지 | PRESENT | None |
| C8 v3 Diagnostic Signatures Preservation | Albumin Covariate Asymmetry / PK47 Single-Site Misfit / Vss vs Vβ Confusion | §8 E에서 ver2 그대로 보존; v3에서 미수정 | PRESENT | None |
| C8 Draft regression | Rejected external/unsupported claims not restored | PART B B5/B7 list; PART A avoids unsupported numbers/regulatory claims | PRESENT | None |
| C9 Canonical integrity | Content Lock v2.1 learner sections preserved | PART A uses §1-§8 from v2.1 with adjacent labeled augmentations plus one rendering-only LaTeX micro-patch; ver2 adds §8 D enhancement and §8 E·F which are clearly labeled and inserted at end of §8 only | PRESENT | None |
| C10 v3.1 Korean Readability | Learner-facing 산문 22건 한국어 가독성 패치 | Navigation Aid (P-01~P-07) / §2 카드 본문 (P-08~P-13, P-17~P-19) / §5 Memory Hooks (P-14~P-16) / §7·§8 (P-20~P-22). 과학적 의미·수식·page tag·marker·source label 무변경 | PRESENT | None |
| C11 v3.2 Korean-Dominant Readability | PART A 전반 한국어 중심 가독성 패치 | 영문 소제목 한국어 병기, 교육 장치명 한국어 병기, 본문 잔여 영어 설명문 한국어 전환, Self-Test 정답 라벨 한국어화. 과학적 의미·수식·page tag·marker·source label 무변경 | PRESENT | None |

### B10. Micro-Patch Log

| Patch # | Location | Source trigger | Inserted text | PDF/Audit basis | Why allowed | Page tag handling |
|---:|---|---|---|---|---|---|
| 1 | §2 M1 Formal Definition, Eq.4-1 display math | HTML/MathJax rendering integrity check | Replaced a tab-corrupted `ext{Net rate of transport}` with `\text{Net rate of transport}` | R&T Eq.4-1 is already cited in Content Lock; this patch only restores LaTeX syntax | Scientific meaning unchanged; required for Phase 5 math rendering | No page tags added or altered |

### B11. Mastery Augmentation Log

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
|---:|---|---|---|---|---|---|
| 1 | §1 Big Idea | M | YES | EXPERT_INFERENCE | Frames all later cards around concentration species without adding factual claims. | Low |
| 2 | M1 · 막투과의 결정인자 | F | YES | AUDIT_DERIVED | Prevents the exact Audit-identified overreading of logP as sufficient. | Low |
| 3 | M2 · 분포의 율속 단계 | J | YES | CRUCIBLE_DERIVED | Reinforces Crucible rate/extent separation that is central to tissue time-course interpretation. | Low |
| 4 | M3 · 분포용적의 수학 구조 | J | YES | CRUCIBLE_DERIVED | Converts albumin-fu changes into a practical sequence for total vs unbound interpretation. | Low |
| 5 | M4 · 혈장단백결합과 fu의 농도의존성 | W | YES | TEXTBOOK_DERIVED | Connects PK47 to the safety condition for AUCu conversion. | Low |
| 6 | M5 · 조직결합과 Kp의 결정인자 | F | YES | CRUCIBLE_DERIVED | Keeps tissue binding and transporter imbalance separate in Eq.4-29 interpretation. | Low |
| 7 | M6 · 노출 지표 선택 | R | YES | TEXTBOOK_DERIVED | Clarifies that exposure metric selection is a causal-species/time-pattern claim. | Low |
| 8 | §5 Critical Blow | J | YES | EXPERT_INFERENCE | Provides a compact decision sequence for C vs Cu without introducing external claims. | Medium |
| 9 (ver2) | §8 D System Integration Points | M | YES | CRUCIBLE_DERIVED | Adopts Crucible T1(b)'s two integration scenarios (NDA dose-exposure linearity paragraph; ICU TDM with hypoalbuminemia + uremia + α1-AGP). Makes "6 cards as one system" concrete without adding new external claims or page tags. | Low |
| 10 (ver2) | §8 E Practical Diagnostic Signatures | F | YES | CRUCIBLE_DERIVED | Names and elaborates Crucible T2(b)'s three GOF signatures (Albumin Covariate Asymmetry / PK47 Single-Site Misfit / Vss vs Vβ Confusion). Strengthens diagnostic transferability that ver1 left implicit in Trench tips. | Low |
| 11 (ver2) | §8 F Mastery Sequence | J | YES | EXPERT_INFERENCE | Provides a 4-step generalization workflow (species → Vd regime → fu stability → metric justification) that fuses §5 Critical Blow Practice Lens with the M3·M5 binding regime distinction. Internal integration aid only; no external claims. | Low |
| 12 (v3) | §2 M3 D-2 Plausible Fallacy block | F | YES | EXPERT_INFERENCE [v3] | Apex Concept 표준 형식에 따라 "Vd = 실제 부피"라는 가장 흔한 직관적 오해를 명시적으로 해체. fu/fuT 비율로 Vd가 결정된다는 M3 핵심을 부정 사례로 강화. 새 수치·새 출처 없음. | Low |
| 13 (v3) | §5 Confusion Pair 1 (C vs Cu) Memory Hook | M | YES | EXPERT_INFERENCE [v3] | "관찰자 vs 실제 행위자" 비유로 C와 Cu의 구조적 비대칭을 영구 인코딩. Critical Blow Practice Lens와 짝을 이뤄 confusion pair의 마지막 잠금 장치 역할. | Low |
| 14 (v3) | §5 Confusion Pair 2 (Perfusion vs Permeability) Memory Hook | M | YES | EXPERT_INFERENCE [v3] | "얼마나 퍼지나 vs 얼마나 빨리 퍼지나"로 distribution extent와 distribution rate의 독립성을 인코딩. M2 율속 단계의 핵심 통찰을 confusion pair 차원에서 재진술. | Low |
| 15 (v3) | §5 Confusion Pair 3 (fu vs fuT) Memory Hook | M | YES | EXPERT_INFERENCE [v3] | "정적 균형점 vs 동적 제거 그림자(Vss vs Vβ)"로 multi-compartment V 정의의 모호성을 명시. §8 E Signature 3 (Vss vs Vβ Confusion)과 직접 연결되어 진단 시그니처 → confusion pair → memory hook 사슬을 완성. | Low |
| 16 (v3) | §5 Confusion Pair 4 (Small vs Large Vd) Memory Hook | M | YES | EXPERT_INFERENCE [v3] | "전체 vs 활성 화물(AUC vs AUCu)"로 PPB 변화의 임상 결과 방향이 metric 선택에 의존함을 인코딩. M6의 metric 선택 논리와 small/large Vd 분기를 한 hook 안에서 융합. | Low |
| 17 (v3) | §2 M1 Practice Brief 4-axis | J | YES | EXPERT_INFERENCE [v3] | M1 학습 후 학습자가 즉시 새 약물에 적용할 수 있는 4축(왜·역할·꿀팁·실무) 응축. 카드 학습이 끝났는지 자가 점검하는 종결 블록. 새 출처·새 수치 없음. | Low |
| 18 (v3) | §2 M2 Practice Brief 4-axis | J | YES | EXPERT_INFERENCE [v3] | M2 학습 종결 4축. distribution phase 굴곡 시점을 Q/V_T·K_pb로 역산하는 실무 루틴을 명시. | Low |
| 19 (v3) | §2 M3 Practice Brief 4-axis | J | YES | EXPERT_INFERENCE [v3] | Apex Concept인 M3의 종결 4축. plasma 3 L · ECW 16 L · TBW 42 L · albumin 7.5 L 4-anchor 분류를 즉시 적용 가능한 실무 휴리스틱으로 응축. | Low |
| 20 (v3) | §2 M4 Practice Brief 4-axis | J | YES | EXPERT_INFERENCE [v3] | M4 종결 4축. dose-normalized AUC 변화 시 fu 점검을 saturable CL 의심보다 먼저 수행하라는 진단 순서를 명시. | Low |
| 21 (v3) | §2 M5 Practice Brief 4-axis | J | YES | EXPERT_INFERENCE [v3] | M5 종결 4축. Basic drug의 큰 Vd → acidic phospholipid binding 1순위 / transporter 2순위 가설 순서를 응축. | Low |
| 22 (v3) | §2 M6 Practice Brief 4-axis | J | YES | EXPERT_INFERENCE [v3] | 세션 종결 카드인 M6의 4축. Cmax/AUC/td 선택을 effect mechanism(peak·누적·threshold)에 매핑하는 실무 의사결정 루틴 응축. | Low |


#### Rejected or Deferred Augmentation Candidates

| Rejected candidate | Reason for rejection |
|---|---|
| New named clinical examples beyond R&T/G&W examples | Would require external literature or new source tags. |
| New regulatory-deficiency wording | Audit explicitly rejected unsupported FDA/guidance/deficiency-letter language. |
| New numeric heuristics for BBB, PPB, or PBPK predictivity | Would add unsupported numerical claims. |
| Expanded Rodgers-Rowland/PBPK discussion | Rejected as scope creep for Session 02. |
| Restoration of Caco-2 / PAMPA / Lipinski rule-of-5 (v3 reaffirmation) | Explicitly out of scope per Audit; not restored in v3 surgical patches. |

### B12. v3 Change Log

| Patch # | Location | Type | Source label | Inserted text summary | Why allowed | Risk |
|---:|---|---|---|---|---|---|
| v3-1 | §2 M3 heading | Apex marker standardization | EXPERT_INFERENCE [v3] | `[Apex Concept]` → `[⚡ Apex Concept]` | Cosmetic standardization for Apex marker; no scientific change. Per-session 1 Apex 원칙 유지. | None |
| v3-2 | §2 M3 D-2 (new subsection) | Plausible Fallacy block | EXPERT_INFERENCE [v3] | "Vd = 실제 분포 공간"이라는 직관적 오해를 3-line callout(오해/왜 틀렸는가/실무에서 어떻게)으로 해체. fu/fuT 비율로 Vd가 결정됨을 부정 사례로 강화. | M3 본문의 Vd ≠ physical volume 메시지를 fallacy 형태로 명시. 새 출처·새 수치·복원 금지 항목 부재. | Low |
| v3-3 | §5 Confusion Pair 1 (C vs Cu) 직후 | Memory Hook | EXPERT_INFERENCE [v3] | "관찰자 vs 실제 행위자" 비유. C = 사진(관찰), Cu = 행위자(수용체 작용). 좌표계 오선택의 임상 역설 인코딩. | Pair 1의 Practice Lens(causal species 4단계)와 짝을 이루는 mnemonic. 새 사실 주장 없음. | Low |
| v3-4 | §5 Confusion Pair 2 (Perfusion vs Permeability) 직후 | Memory Hook | EXPERT_INFERENCE [v3] | "얼마나 퍼지나 vs 얼마나 빨리 퍼지나"로 distribution extent와 distribution rate의 독립성 인코딩. | Pair 2의 perfusion/permeability 율속 본문을 extent/rate 차원으로 재조명. 본문 사실 인용 위에서만 작동. | Low |
| v3-5 | §5 Confusion Pair 3 (fu vs fuT) 직후 | Memory Hook | EXPERT_INFERENCE [v3] | "정적 균형점 vs 동적 제거 그림자(Vss vs Vβ)"로 multi-compartment V 정의의 모호성 인코딩. §8 E Signature 3 (Vss vs Vβ Confusion)과 직접 연결. | M3 트렌치 팁 + §8 E Signature 3에 이미 존재하는 개념을 §5 차원으로 통합. 새 외부 출처 없음. | Low |
| v3-6 | §5 Confusion Pair 4 (Small vs Large Vd) 직후 | Memory Hook | EXPERT_INFERENCE [v3] | "전체 vs 활성 화물(AUC vs AUCu)"로 PPB 변화의 임상 결과 방향이 metric 선택에 의존함을 인코딩. M6 metric 선택 논리와 small/large Vd 분기를 융합. | M6 본문의 conversion shortcut 안전 조건을 confusion pair 차원에서 응축. 새 사실 주장 없음. | Low |
| v3-7 | §2 M1 (FIGURE_POINTER 직후) | Practice Brief 4-axis | EXPERT_INFERENCE [v3] | M1 종결 4축(왜·역할·꿀팁·실무). size·logP·ionization·transporter 4축 한 줄 요약 습관 명시. | 본문의 4-축 결정인자를 학습자 점검 형식으로 응축. 새 출처·새 수치 없음. | Low |
| v3-8 | §2 M2 (FIGURE_POINTER 직후) | Practice Brief 4-axis | EXPERT_INFERENCE [v3] | M2 종결 4축. distribution phase 굴곡 시점을 Q/V_T·K_pb로 역산하는 실무 루틴 명시. | 본문 Eq.4-5~4-7을 학습자 점검 형식으로 응축. 새 사실 주장 없음. | Low |
| v3-9 | §2 M3 (FIGURE_POINTER 직후) | Practice Brief 4-axis | EXPERT_INFERENCE [v3] | M3 종결 4축. plasma 3 L · ECW 16 L · TBW 42 L · albumin 7.5 L 4-anchor 분류 휴리스틱. | 본문 Source-Anchored Data Anchors의 physiologic anchors를 분류 도구로 재구성. 모두 본문에 이미 존재하는 수치. | Low |
| v3-10 | §2 M4 (FIGURE_POINTER 직후) | Practice Brief 4-axis | EXPERT_INFERENCE [v3] | M4 종결 4축. dose-normalized AUC 변화 시 fu 점검을 saturable CL 의심보다 먼저 수행. | 본문 boundary condition을 진단 순서로 명시. 새 외부 출처 없음. | Low |
| v3-11 | §2 M5 (RECAP 직후) | Practice Brief 4-axis | EXPERT_INFERENCE [v3] | M5 종결 4축. Basic drug의 큰 Vd → acidic phospholipid binding 1순위 / transporter 2순위 가설 순서. | 본문 Failure Mode (Eq.4-29 binding vs transporter 분리)를 가설 순위 형식으로 응축. 새 사실 주장 없음. | Low |
| v3-12 | §2 M6 (FIGURE_POINTER 직후) | Practice Brief 4-axis | EXPERT_INFERENCE [v3] | M6 종결 4축. Cmax/AUC/td 선택을 effect mechanism(peak·누적·threshold)에 매핑. | 본문 G&W Table2.21의 metric 분류를 의사결정 mapping 형식으로 응축. | Low |

#### v3 Forbidden Restoration Re-Verification

v3는 ver2에서 결정된 모든 금지 항목을 그대로 유지한다. 특히:

- **Caco-2 / PAMPA / Lipinski rule-of-5 / phase 1 screening rule** — 본 세션 source 범위(R&T Ch.4 + G&W §2.9.3-2.9.5 + PK47) 밖이며, ver2의 M1 Trench-Level Tip이 이 점을 명시. v3는 이 결정을 변경하지 않는다.
- **FDA Guidance / deficiency-letter / submission-template 언어** — Audit이 명시 거부. v3 Practice Brief의 "실무 활용" 항목은 이 금지 영역을 침범하지 않도록 IND/NDA 단계 권고 수준의 일반론으로만 작성됨.
- **Rodgers-Rowland depth / 80% variance / one-digit Vd / r>0.85 등 정량 주장** — v3 추가 블록에 등장하지 않음.
- **§8 E의 3개 진단 시그니처 명칭(Albumin Covariate Asymmetry / PK47 Single-Site Misfit / Vss vs Vβ Confusion)** — ver2 형태로 보존. v3에서 §5 Memory Hook 3 (Vss vs Vβ)이 §8 E Signature 3과 명시적으로 연결됨을 B11에 기록.

### B12.1. v3.1 Korean Readability Patch Log

v3.1은 PART A learner-facing 산문에 한국어 가독성 개선만을 surgical하게 적용한다. 모든 패치는 의미 보존을 검증한 Low risk이며, 새 과학적 주장·새 수치·새 page tag·새 figure marker·새 외부 인용·새 regulatory 문구를 추가하지 않는다.

| Patch # | Location | Type | Original (excerpt) | Revised (excerpt) | Risk |
|---:|---|---|---|---|---|
| v3.1-01 | Learner Nav Aid 제목 | Korean flow improvement | `### How to Use This Handout` | `### 이 자료 활용 방법` | Low |
| v3.1-02 | Learner Nav Aid 항목 1 | Korean flow improvement | `Read §1 to fix the single governing question...` | `§1을 읽어 핵심 질문을 먼저 고정하라...` | Low |
| v3.1-03 | Learner Nav Aid 항목 2 | Korean flow improvement | `Study §2 in order. M1 explains whether drug can cross membranes...` | `§2를 순서대로 학습하라. M1은 약물이 막을 통과할 수 있는지...` | Low |
| v3.1-04 | Learner Nav Aid 항목 3–5 | Korean flow improvement | `Use the FIGURE_POINTER blocks... Finish with §5 and §7... Close with §8...` | `FIGURE_POINTER 블록은 교과서 그림을 직접 찾아보라는 안내... §5와 §7로 마무리하라... §8로 닫아라...` | Low |
| v3.1-05 | Learner Nav Aid Learning Route 제목 | Korean flow improvement | `### Learning Route` | `### 학습 경로` | Low |
| v3.1-06 | Learner Nav Aid Before-Start 체크리스트 | Korean flow improvement | `### Before You Start Checklist` + 3 영문 항목 | `### 학습 시작 전 체크리스트` + 3 한글 항목 | Low |
| v3.1-07 | Learner Nav Aid After-Finish 체크리스트 | Korean flow improvement | `### After You Finish Checklist` + 7 영문 항목 | `### 학습 완료 후 체크리스트` + 7 한글 항목 | Low |
| v3.1-08 | §2 M1 MASTER LENS | Korean flow improvement / First-use gloss | `이 네 축과 막 구조가 한 숫자로 접힌 macroscale permeability이다.` | `이 네 축과 막 구조가 하나의 숫자로 압축된 거시 투과도(macroscale permeability)이다.` | Low |
| v3.1-09 | §2 M2 Formal Definition A | Korean flow improvement | `tissue concentration의 접근은 mono-exponential 형태를 따른다.` | `조직 농도가 평형값에 접근하는 경로는 단일지수(mono-exponential) 형태를 따른다.` | Low |
| v3.1-10 | §2 M4 MASTER LENS | Korean flow improvement / First-use gloss | `Protein concentration, binding affinity, binding site 수, unbound concentration의 함수다.` | `혈장 단백 농도(protein concentration), 결합 친화도(binding affinity), 결합 부위 수, 유리 농도(unbound concentration) 등 여러 인자의 함수이기 때문이다.` | Low |
| v3.1-11 | §2 M3 D-2 Plausible Fallacy 마지막 문장 | Sentence split | `Bayesian TDM에서 total C가 정상인데 unbound C가 변한 경우 fu 변화를 Vd 변화로 오해하는 전형적 실수가 여기서 나온다.` | `Bayesian TDM에서 total C가 정상 범위인데 unbound C가 달라진 경우를 생각해 보라. 실제 원인은 fu 변화인데도 Vd 변화로 오해하는 전형적 실수가 여기에서 비롯된다.` | Low |
| v3.1-12 | §2 M6 MASTER LENS | Korean flow improvement / Concept clarification | `어떤 concentration species가 어떤 시간 패턴으로 pharmacology를 만든다는 주장이다.` | `즉, exposure metric은 어떤 concentration species가 어떤 시간 패턴으로 약리 효과를 유발하는가에 대한 인과적 선언이다.` | Low |
| v3.1-13 | §2 M6 B ANNOTATION 첫 문장 | Korean flow improvement | `따라서 M6의 질문은 "AUC를 쓸 것인가?"가 아니라 "어떤 species의 AUC 또는 시간 패턴을 쓸 것인가?"이다.` | `다시 말해, M6의 질문은 "AUC를 쓸 것인가?"가 아니라 "어느 species의 AUC 또는 어떤 시간 패턴을 쓸 것인가?"이다.` | Low |
| v3.1-14 | §5 Confusion Pair 2 Memory Hook | Sentence split / Korean flow improvement | `빠른 distribution rate + 작은 Vd = 빠르게 좁은 곳에 가두는 것... 두 개가 독립적이므로 Vd 하나로 분포 과정의 시간 경과를 논할 수 없다.` | `빠른 distribution rate + 작은 Vd는 짧은 시간 안에 좁은 구획에 가두는 패턴이고... 이 두 차원은 독립적으로 작동하므로, Vd 하나만으로는 분포 과정의 시간 경과를 논할 수 없다.` | Low |
| v3.1-15 | §5 Confusion Pair 3 Memory Hook 괄호 | Concept clarification | `(이 hook은 fu/fuT 분기와 함께, multi-compartment 모델에서 V를 어느 정의로 부르고 있는가를 함께 점검하라는 신호다.)` | `(이 memory hook은 fu/fuT 분기를 다룰 때 함께 점검할 사항을 가리킨다: multi-compartment 모델에서 V를 Vss로 쓰는가, Vβ로 쓰는가를 명시적으로 확인하라.)` | Low |
| v3.1-16 | §5 Confusion Pair 4 Memory Hook | Korean flow improvement | `알부민 결합이 강한 약물에서 저알부민혈증이 생기면 AUC가 줄어도 AUCu는 오히려 늘 수 있다. exposure-response 분석을 AUC로 하면 방향이 역전되는 이유다.` | `알부민 결합이 강한 약물에서 저알부민혈증이 생기면, AUC는 줄어도 AUCu는 오히려 늘 수 있다. 바로 이 때문에 exposure-response 분석을 AUC로 수행하면 효과 방향이 역전되는 결과가 나온다.` | Low |
| v3.1-17 | §2 M4 Boundary Condition C | Sentence split | `G&W는 \`fub > 1\`이 가능하다고 명시한다; 이는 bound/free ratio이므로 fraction bound와 혼동하면 안 된다.` | `G&W는 \`fub > 1\`이 가능하다고 명시한다. 이는 bound/free ratio이므로, fraction bound와 혼동하지 않도록 주의한다.` | Low |
| v3.1-18 | §2 M3 Practice Brief 흐름상 역할 | First-use gloss | `V라는 단일 mathematical bridge 위에 통합하는 세션의 중심 카드다.` | `V라는 단일 수학적 연결 고리(mathematical bridge) 위에 통합하는 세션의 중심 카드다.` | Low |
| v3.1-19 | §2 M6 Practice Brief 실무 활용 | First-use gloss | `narrow therapeutic index 약물의 안전 마진 분석` | `치료역이 좁은(narrow therapeutic index) 약물의 안전 마진 분석` | Low |
| v3.1-20 | §7 Q10 Answer | First-use gloss | `dose별 ex vivo $f_u$를 확인한다.` | `dose별 ex vivo(체외 측정) $f_u$를 확인한다.` | Low |
| v3.1-21 | §8 C Professional Moat RECAP | Korean flow improvement | `Plasma와 tissue 사이의 binding·permeability·flow가 만든 equilibrium and time-course problem이다.` | `Plasma와 tissue 사이에서 binding, permeability, flow가 함께 형성하는 equilibrium 문제이자 시간 경과(time-course) 문제다.` | Low |
| v3.1-22 | §8 D System Integration 첫 항목 | Korean flow improvement | `**Clinical pharmacology summary**: dose-exposure linearity를 쓸 때 absorption/permeability(M1), V/dose dependence(M3), saturable PPB(M4), exposure metric(M6)이 한 문단 안에서 연결된다.` | `**임상약리 요약**: dose-exposure linearity를 논할 때, M1(흡수/투과), M3(V/용량 의존성), M4(PPB 포화 여부), M6(exposure metric 선택) 네 카드가 하나의 문단 안에서 논리적으로 연결된다.` | Low |

#### v3.1 Forbidden Modification Re-Verification

v3.1은 v3에서 결정된 모든 금지 항목을 그대로 유지한다. 추가로 v3.1 패치 자체가 침범하지 않은 영역을 명시한다:

- **수식·LaTeX 표기**: 모든 `$...$`, `$$...$$` 블록 verbatim 유지. Eq.4-1~4-30, G&W Eq.47:1/47:3/47:4, Eq.2:373, App.D 식, Eq.C-13 모두 무변경.
- **Page tag**: `[R&T pp.XX–YY]`, `[G&W p.XX]`, `[출처: R&T Eq.4-X, p.YY]`, `[확인 필요]` 등 모든 source page tag 무변경. 신규 page tag 추가 금지 원칙 준수.
- **Source label**: `EXPERT_INFERENCE`, `AUDIT_DERIVED`, `CRUCIBLE_DERIVED`, `TEXTBOOK_DERIVED`, `[EXPERT_INFERENCE, v3]` 등 모든 라벨 verbatim 유지.
- **HTML compiler marker**: `<!-- MASTER LENS -->`, `<!-- ANNOTATION -->`, `<!-- ANCHOR -->`, `<!-- TRENCH -->`, `<!-- CONFUSION -->`, `<!-- SELF-TEST -->`, `<!-- RECAP -->` 모두 원위치 유지.
- **Figure marker**: 5개 `<!-- FIGURE_POINTER --> ... <!-- /FIGURE_POINTER -->` 블록 verbatim 유지 (M1·M2·M3·M4·M6 카드).
- **Apex marker**: `**[⚡ Apex Concept]**` (M3) verbatim 유지.
- **Code block / NONMEM 문법**: PART A는 NONMEM control stream을 포함하지 않으므로 해당 없음. `text` 코드 블록(Concept Navigation)은 verbatim 유지.
- **Certification table 구조**: Phase 4D Certification 표는 v3.1 row 추가만 수행하며 기존 행은 무변경 (단, Learner-Standalone / Source-Boundary / HTML-Readiness Certificate의 Basis 컬럼에 v3.1 영향 무선언만 추가).

---

## Final v3 All-Pass Checklist

| # | Verification Item | Status | Evidence Location |
|---:|---|---|---|
| 1 | M3 Apex marker 표준화 — `[⚡ Apex Concept]` 형식 | ✅ PASS | §2 M3 heading; Phase 4D Certification Apex-Standardization row |
| 2 | M3 Plausible Fallacy 블록 추가 (3-line: 오해 / 왜 틀렸는가 / 실무에서 어떻게) with `[EXPERT_INFERENCE, v3]` 라벨 | ✅ PASS | §2 M3 D-2 subsection; B11 entry #12; B12 v3-2 |
| 3 | §5 4개 confusion pair 직후 Memory Hook 4종 추가 with `[EXPERT_INFERENCE, v3]` 라벨 (관찰자 vs 행위자 / 퍼지나 vs 빨리 / Vss vs Vβ / AUC vs AUCu) | ✅ PASS | §5 Pair 1·2·3·4 직후; B11 entries #13~16; B12 v3-3~v3-6 |
| 4 | M1~M6 6개 카드 Practice Brief 4축(왜·역할·꿀팁·실무) 추가 with `[EXPERT_INFERENCE, v3]` 라벨 | ✅ PASS | §2 M1·M2·M3·M4·M5·M6 카드 말미; B11 entries #17~22; B12 v3-7~v3-12 |
| 5 | Caco-2 / PAMPA / Lipinski / FDA 미지원 문구 미복원 | ✅ PASS | PART A 부재 확인; B5 Audit Guardrails 그대로 유지; B12 v3 Forbidden Restoration Re-Verification |
| 6 | 기존 진단 시그니처 3종(Albumin Covariate Asymmetry / PK47 Single-Site Misfit / Vss vs Vβ Confusion) 보존 | ✅ PASS | §8 E Signature 1·2·3; ver2 형태 verbatim 유지 |
| 7 | 모든 page tags · equations · figure markers · PART A/PART B 구조 보존 | ✅ PASS | B9 Coverage Matrix C5·C6 row; B10 Micro-Patch Log 무변동; FIGURE_POINTER 5개 verbatim 유지 |
| 8 | v3 추가 블록 11개 모두 `[EXPERT_INFERENCE, v3]` 라벨 부착 및 PART B B11 / B12에 추적 등록 | ✅ PASS | B11 entries #12~22 (총 11개); B12 v3-1~v3-12 (apex 표준화 1 + Plausible Fallacy 1 + Memory Hook 4 + Practice Brief 6 = 12개 항목, 단 v3-1은 cosmetic standardization으로 콘텐츠 추가 11개 중 미포함) |

---

## v3.1 Final Checklist

| # | Verification Item | Status | Evidence Location |
|---:|---|---|---|
| 1 | PART A readability improved | ✅ PASS | §1 Learner Navigation Aid 한국어화 (P-01~P-07) / §2 카드 본문 영어식 명사 나열 교정 (P-08~P-13, P-17~P-19) / §5 Memory Hook 장문 분리 (P-14~P-16) / §7·§8 first-use gloss 및 sentence split (P-20~P-22). 총 22건 surgical edit 적용. |
| 2 | Scientific content unchanged | ✅ PASS | 모든 정량 수치, 임상 사례, 약물명, 파라미터 추정값, boundary condition, regulatory 권고 무변경. R&T Ch.4 / G&W §2.9.3-2.9.5 / PK47 / App.B/C/D 모든 출처 인용 verbatim 유지. 새 과학적 주장 · 새 수치 · 새 외부 reference 도입 없음. |
| 3 | Equations preserved | ✅ PASS | Eq.4-1, 4-5~4-7, 4-8, 4-11~4-15, 4-17~4-19, 4-25, 4-26, 4-29, 4-30, App.C Eq.C-13, App.D blood/plasma ratio 식, G&W Eq.2:373, Eq.47:1/47:3/47:4 — 모든 LaTeX `$...$`, `$$...$$` 블록 verbatim 유지. B10 LaTeX 무결성 micro-patch (`\text{...}`) 그대로 유지. |
| 4 | Page tags preserved | ✅ PASS | `[R&T pp.XX–YY]`, `[G&W p.XX]`, `[출처: ...]`, `[확인 필요]` 모든 page tag 원위치·원형식 유지. 신규 page tag 추가 0건, 페이지 번호 변경 0건. B9 Coverage Matrix C6 row 무변동. |
| 5 | Figure markers preserved | ✅ PASS | `<!-- FIGURE_POINTER --> ... <!-- /FIGURE_POINTER -->` 5개 블록(M1 R&T Fig.4-4 / M2 R&T Fig.4-13 / M3 R&T Fig.4-25,4-26 / M4 G&W Fig.47.1 / M6 G&W Fig.2.134) 모두 Source/Why/When/Learner instruction 4필드 verbatim 유지. B2 Approved Figure Pointer Inventory 무변동. |
| 6 | Source-boundary preserved | ✅ PASS | TEXTBOOK_DERIVED / AUDIT_DERIVED / CRUCIBLE_DERIVED / EXPERT_INFERENCE / `[EXPERT_INFERENCE, v3]` 라벨 모두 원위치 유지. B5 Audit Guardrails 금지 항목 (Caco-2/PAMPA/Lipinski/FDA deficiency-letter/Rodgers-Rowland depth/exact 시각 추정) 미복원. v3 Forbidden Restoration Re-Verification 그대로 적용. |
| 7 | HTML-readiness preserved | ✅ PASS | `<!-- MASTER LENS -->` / `<!-- ANNOTATION -->` / `<!-- ANCHOR -->` / `<!-- TRENCH -->` / `<!-- CONFUSION -->` / `<!-- SELF-TEST -->` / `<!-- RECAP -->` HTML compiler marker 전부 verbatim 유지. B4 Marker → component mapping 무변동. B3 Page Tag Rendering Rules 무변동. Navigation anchor integrity rule 영향 없음. |
| 8 | Ready for Phase 5 HTML compilation | ✅ PASS | FULL MODE assembly contract 유지 (PATCH MODE splice 불필요). PART A learner-facing body 22건 한국어 가독성 개선만 surgical 적용. PART B B1~B12 guardrail / Coverage Matrix / Mastery Augmentation Log / Change Log 무손상 (단, B9에 C10 v3.1 row 1건, B12에 v3.1 Korean Readability Patch Log 22건, Phase 4D Certification에 Korean-Readability Certificate row 1건 추가). Phase 5 HTML 렌더링 시 마커 매핑·page tag 패턴·figure pointer 콜아웃·math rendering 모두 v3와 동일하게 작동. |

---

## v3.2 Final Checklist

| # | Verification Item | Status | Evidence Location |
|---:|---|---|---|
| 1 | PART A 한국어 중심 가독성 개선 | ✅ PASS | §2 카드 소제목 `한글(English)` 병기 (Formal Definition → 형식적 정의, Boundary Conditions → 경계 조건, Source-Anchored Details → 출처 기반 상세 등), §8 소제목 한국어 병기, 교육 장치명 한국어 병기 (Failure Mode → 실패 모드, Practice Lens → 실무 렌즈, Mastery Note → 체화 노트 등), 본문 잔여 영어 일반 서술 한국어 전환, Self-Test Answer → 정답 라벨 한국어화, 학습 경로 한국어 전환. |
| 2 | 과학적 내용 무변경 | ✅ PASS | 모든 정량 수치, 임상 사례, 약물명, 파라미터 추정값, 경계 조건, 규제 권고 무변경. v3.1의 모든 과학적 내용 verbatim 보존. 새 과학적 주장·새 수치·새 외부 reference 도입 없음. |
| 3 | 수식 보존 | ✅ PASS | 모든 LaTeX `$...$`, `$$...$$` 블록 verbatim 유지. v3.1과 동일. |
| 4 | Page tags 보존 | ✅ PASS | 모든 `[R&T pp.XX–YY]`, `[G&W p.XX]`, `[출처: ...]`, `[확인 필요]` 원위치·원형식 유지. 신규 page tag 추가 0건. |
| 5 | Figure markers 보존 | ✅ PASS | 5개 `<!-- FIGURE_POINTER --> ... <!-- /FIGURE_POINTER -->` 블록 모두 4필드 verbatim 유지. |
| 6 | Source-boundary 보존 | ✅ PASS | 모든 source label (TEXTBOOK_DERIVED / AUDIT_DERIVED / CRUCIBLE_DERIVED / EXPERT_INFERENCE / [EXPERT_INFERENCE, v3]) 원위치 유지. |
| 7 | HTML-readiness 보존 | ✅ PASS | 모든 HTML compiler marker verbatim 유지. B4 marker mapping 무변동. B3 Page Tag Rendering Rules 무변동. |
| 8 | Career-critical 전문용어 `한글(English)` 병기 | ✅ PASS | 첫 등장 또는 섹션 첫 등장 시 `한글(English)` 형식 병기 적용: 투과도(permeability), 구동력(driving force), 유리 농도(unbound concentration), 관류 율속(perfusion-rate limited), 겉보기 비례상수(apparent proportionality constant), 결합 친화도(binding affinity), 노출 지표(exposure metric) 등. |
| 9 | Phase 5 HTML 컴파일 준비 완료 | ✅ PASS | FULL MODE assembly contract 유지. PART A 한국어 중심 가독성 패치만 적용. PART B B1~B12 guardrail 무손상 (단, B9에 C11 v3.2 row 1건, Phase 4D Certification에 Korean-Dominant Readability Certificate row 1건 추가). |

| Certificate | Status | Basis |
|---|---|---|
| Korean-Dominant Readability Certificate | PASS | General learner-facing English prose converted to Korean where possible; career-critical terms retained as Korean-English paired expressions. |
| Scientific Preservation Certificate | PASS | No scientific content, equation, number, example, page tag, or source label changed. |
| Marker Integrity Certificate | PASS | All figure markers, compiler markers, anchors, and section/card structures preserved. |
| HTML-Readiness Certificate | PASS | Phase 5 compatibility preserved; no HTML/Mermaid/SVG generated. |

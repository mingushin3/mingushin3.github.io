# 14_HTML Compile Input Master

## Phase 4D Certification

| Certificate | Status | Basis |
|---|---|---|
| Learner-Standalone Certificate | PASS | PART A starts with a learner navigation aid and contains §1, §2, §5, §7, and §8 as a complete study handout without audit/process tables. |
| Zero-Omission Certificate | PASS | Scope Lock, Audit MUST/SHOULD fixes, Content Lock v2, v2.1 insertion map, Crucible Grade A logic, and PDF figure/page anchors were cross-checked; no high-impact unresolved omission remains. |
| Mastery-Uplift Certificate | PASS | Eight bounded, adjacent, source-labeled mastery augmentations were inserted without broad rewrite. |
| Source-Boundary Certificate | PASS | Each augmentation is labeled TEXTBOOK_DERIVED, AUDIT_DERIVED, CRUCIBLE_DERIVED, or EXPERT_INFERENCE; no new page tags, unsupported numerical anchors, or new named examples were added. |
| HTML-Readiness Certificate | PASS | PART B contains the Phase 5 compilation contract, figure rules, page-tag rules, marker mapping, navigation integrity rules, audit/crucible guardrails, and PATCH MODE splice verification. |

## Assembly Mode

PATCH MODE — `14_Content_Lock_v2.1(1).md` is a Figure Marker Patch / Insertion Map, not a full re-emitted learner body. PART A was constructed from learner-facing `14_Content_Lock_v2(2).md` §1–§8, with the seven approved Phase 4C markers spliced at exact unique anchors.

## Input Manifest

| File | Role | Authority level | Used for | Notes |
|---|---|---:|---|---|
| `14_scope_lock(3).md` | scope boundary | A0 | source range, learner, mode, image-right boundary, hard rules | Image rights = None; textbook figures must be pointers only. |
| `014_G_알로메트릭 스케일링 종간 외삽·체중·연령(4).pdf` | PDF verification source | A1 | G&W §2.10, PK28, PK29 formulas, data anchors, figure identities | Used only for verification/high-impact grounding. |
| `014_T_알로메트릭 스케일링 종간 외삽·체중·연령(4).pdf` | PDF verification source | A1 | R&T Ch.14/Ch.22 age-weight and allometry anchors | Used only for verification/high-impact grounding. |
| `14_Audit_Report_v1(3).md` | audit guardrail | A2 | MUST_FIX/SHOULD_FIX correction and regression prevention | Controls fold correction, FIH directionality, unsupported claims. |
| `14_Content_Lock_v2(2).md` | canonical body | A3 | base learner body | §1–§8 used; process/adjudication §0 excluded from learner-facing PART A. |
| `14_Content_Lock_v2.1(1).md` | figure insertion source | A4 | PATCH MODE figure strategy and exact insertion anchors | Seven approved markers; two schematics, five pointers. |
| `14_crucible_report_v1(1).md` | crucible guardrail | A5 | preserved Grade A logic and mastery augmentation basis | Used only as controlled insight source, not raw prose source. |
| `S14_phase1_patch memo(2).md` | locked reference / deprecated source check | A6 | regression check against Phase 1 known weaknesses | Not copied into PART A. |
| `14_step1_draft_v0(2).md` | deprecated source | A6 | regression check only | Not used as learner-body source. |
| `붙여넣은 마크다운(2)(63).md` | compiler instruction | A7 | Phase 5 HTML rendering requirements | Navigation anchor integrity, marker mapping, page tag rendering, Mermaid checks. |
| `붙여넣은 텍스트 (1)(88).txt` | Phase 4D assembler instruction | workflow instruction | current assembly protocol | Renamed target from 05 to user-requested 14. |

## PART A — Learner-Facing Complete Handout

## Learner Navigation Aid

**How to use this handout:** Read §1 once for the spine, study §2 C1–C5 in order, then use §5 to prevent the three common confusions before attempting §7. Figure pointers do not reproduce textbook images; when a pointer appears, consult the named textbook figure in the source PDF/book.

**Learning route:**

1. C1: understand why `Y=a·BW^b` is a scale law, not just a regression line.
2. C2: lock the CL exponent and the `b=1` fallacy.
3. C3: separate flow (`b`) from extent (`d`) and derive time/rate consequences.
4. C4: use Dedrick plots as diagnostics for exponent structure.
5. C5: treat allometric dose translation as an equal-AUCu backbone, not a final clinical dose rule.
6. §5–§7: test whether you can block source discrepancies, unsupported regulatory language, and exponent-swapping errors.

**Before you start:** Confirm you can define CL, V, AUC, half-life, unbound fraction, and first-order elimination.  
**After you finish:** You should be able to explain why `0.75` and `1.0` are not interchangeable, why time scales as `d-b`, and why pediatric/elderly dosing needs functional-age and organ-function layers beyond body weight.


## §1 — Session Header & Roadmap

**Source:** Gabrielsson & Weiner 5e §2.10 (p.170–191), Case Study PK28 (p.611–614), Case Study PK29 (p.615–620); Rowland & Tozer 5e Ch.14 (p.411–441), Ch.22 allometry section (p.731–743).

### Big Idea

<!-- MASTER LENS -->
$Y=a\cdot BW^b$는 단순 회귀식이 아니다. 종간 체중 차이를 **parameter scale**로 번역하는 거듭제곱 언어다.
<!-- ANNOTATION -->
여기서 parameter scale(← 체중 차이를 파라미터 단위로 옮기는 척도)은 “kg 차이”를 CL, V, dose 같은 PK 파라미터의 차이로 바꾸는 읽기 방식이다. 핵심 오류는 `b=0.75`와 `b=1.0`의 차이를 작게 보는 것이다. R&T의 20-g mouse→70-kg human 예시에서는 같은 값 1이 `b=1`이면 3500, `b=0.75`이면 455가 되어 7.7배 차이가 난다 [R&T p.733]. G&W PK28의 23-g mouse→70-kg human에서는 약 7.4배, rat 250-g→human 70-kg에서는 약 4.1배 차이다. 이 차이는 “용량을 낮게 시작한다/높게 시작한다”의 단순 구호가 아니라, **target AUC 기반에서는 CL 과대예측이 dose 과대 산출로 이어질 수 있다**는 dose/AUC 방향성 문제다.

### 개념 항법도

```text
[C1] Master Equation: Y = a·BW^b
        │
        ├──▶ [C2] CL exponent b≈0.75 ─────────────┐
        │                                           ├──▶ [C5] Equal-AUCu dose backbone
        └──▶ [C3] V exponent d≈1.0 ────────────────┘
                  │
                  ├──▶ t1/2 ∝ BW^(d-b)≈BW^0.25
                  ├──▶ kel ∝ BW^(b-d)≈BW^-0.25
                  └──▶ [C4] Dedrick Superposition
```

### 지식 그래프 위치

**선행 전제:** CL, V, AUC, half-life의 정의; one-compartment exponential decay; plasma protein binding(← 단백 결합으로 자유 약물 농도가 달라지는 현상)과 unbound clearance 개념.  
<!-- ANNOTATION -->
**직접 후속:** pediatric/elderly dose adjustment, PopPK weight covariate choice, PBPK organ blood flow/volume scaling, FIH exposure translation table.  
**주의:** NONMEM control stream, ICH/FDA/MABEL language, QSP implementation은 본 PDF가 직접 다루는 내용이 아니므로 본문에서는 `[교과서 외 구현/실무 해석]`으로만 다룬다.

<!-- RECAP -->
**§1 요약:** 이 세션의 spine은 `Y=a·BW^b → CL b≈0.75 → V d≈1 → time d-b≈0.25 → Dedrick → equal-AUCu dose backbone`이다. 반드시 고정해야 할 교정 지점은 `4.1/7.4/7.7` fold 기준을 분리하고, FIH dose formula를 standalone starting-dose rule이 아닌 allometric exposure backbone으로 낮추는 것이다.

---


<!-- FIGURE_SCHEMATIC --><br>Title: Allometric spine: variable type → exponent → time/dose consequence<br>Mode: N<br>Visual objective: 5초 안에 C1–C5가 하나의 workflow라는 점을 보이게 한다.<br>Core message: Y=a·BW^b는 독립 수식이 아니라 CL, V, time, Dedrick, equal-AUCu dose translation을 연결하는 spine이다.<br>Elements to include: Start node Y=a·BW^b; CL / flow / b≈0.75; V / extent / d≈1; t1/2 ∝ BW^(d-b); kel ∝ BW^(b-d); Dedrick superposition; Equal-AUCu dose backbone; caveat gates fu, metabolism route, nonlinear PK, functional age.<br>Elements to exclude: regulatory agency logos, unsupported ICH/FDA claims, detailed PBPK/QSP submodels, animal cartoons.<br>Suggested rendering: Mermaid<br>Caption: Allometric scaling should be read as a connected decision spine, not as five isolated formulas.<br>Alt text: A flowchart begins with Y=a·BW^b, branches to CL and V exponents, then connects to half-life, rate constant, Dedrick plots, and dose translation caveats.<br>Source relation: Newly designed<br><!-- /FIGURE_SCHEMATIC -->

## §2 — Concept Anatomy Cards

---

### ━━ C1. Master Allometric Equation: $Y=a\cdot BW^b$ ━━

<!-- MASTER LENS -->
**개념 Big Idea:** 알로메트리(← 크기와 생리 변수의 거듭제곱 관계)는 “큰 동물은 단순히 작은 동물의 확대판인가?”라는 질문에 대한 정량적 답이다.
<!-- ANNOTATION --> `a`는 화합물·변수의 절편, `b`는 체중이 바뀔 때 해당 변수의 변화율을 결정하는 지수다.

#### A. Formal Definition

$$Y=a\cdot BW^b \quad [G\&W\ Eq.2:374,\ p.173;\ R\&T\ Eq.22\text{-}2,\ p.732]$$

양변 로그 변환:

$$\ln(Y)=\ln(a)+b\cdot\ln(BW) \quad [G\&W\ Eq.2:379,\ p.176;\ R\&T\ Eq.22\text{-}1,\ p.732]$$

- **$a$:** drug-dependent 또는 compound-dependent intercept. 단위는 $b$에 의존한다.
- **$b$:** 대체로 variable type-dependent exponent. 다만 실제 CL exponent는 자료 품질, 종 수, 비선형성, 종간 protein binding 차이 등에 따라 변동할 수 있다 [G&W p.177–178].

#### B. Derivation — 왜 거듭제곱 함수인가

G&W는 대사율이 $BW^{0.75}$로 스케일링하고, energy content가 대략 $BW^1$에 비례하므로 turnover time이 $BW^{0.25}$로 나온다고 제시한다 [G&W Eq.2:375–377, p.173]. 즉 알로메트리는 “체중이 커질수록 절대 처리량은 증가하지만, 단위 체중당 처리 효율은 감소한다”는 생리학적 압축이다.

표면적-부피 직관도 같은 방향을 준다. 기하학적으로 surface는 length², volume은 length³이므로 surface는 volume^(2/3)에 비례한다. 그러나 실제 생리학 변수는 단순 외부 표면적보다 더 복잡해, Brody의 경험적 지수는 0.5–0.8 범위로 나타난다 [G&W p.173–174].

#### C. Structural Meaning

<!-- ANCHOR -->
Log-log 직선은 단순히 “회귀가 잘 맞는다”는 뜻이 아니다. `[교과서 외 수학적 해석]`으로 말하면, 이는 체중 배율이 달라져도 같은 지수 법칙이 유지되는 scale-invariant 구조를 가정한다. 이 가정이 깨지는 순간이 allometry failure의 시작이다.

#### D. Boundary Conditions

G&W는 allometry가 physical transport processes, disposition이 plasma protein binding에 크게 좌우되지 않는 물질에서 특히 유용하다고 설명한다. 반대로 종간 metabolism/excretion의 질적 차이, CYP450 isozyme makeup 차이, plasma protein binding 차이가 크면 실패할 수 있다 [G&W p.173].

#### E. Zettelkasten Atom

```yaml
aliases: [allometric law, allometric power function, Y=a·BW^b]
tags: [pharmacometrics/allometry, scaling/inter-species]
source: "G&W §2.10.3 p.173–176; R&T Ch.22 p.731–733"
```

<!-- RECAP -->
**C1 핵심:** Allometry는 `a`와 `b`로 종간 차이를 압축한다. 하지만 `b`는 “항상 고정된 자연상수”가 아니라, 변수 유형과 데이터 품질, binding, 비선형성, 종간 mechanism 차이에 영향을 받는 생리학적 prior다.

> **Mastery Note — [CRUCIBLE_DERIVED]**  
> Log-log 직선은 “그럴듯한 그림”이 아니라 scale-invariance claim이다. 따라서 C1을 적용할 때는 먼저 이 약물의 clearance 또는 volume에 종 고유의 characteristic mechanism이 들어오는지를 묻는다.

---

### ━━ C2. [Apex] Clearance Exponent $b\approx0.75$ ━━

<!-- MASTER LENS -->
**개념 Big Idea:** Clearance는 “공간의 크기”가 아니라 **단위 시간당 처리 흐름**이다. 그래서 V처럼 BW¹로 증가하지 않고, 대사율·혈류·GFR과 같은 functional variable처럼 대략 $BW^{0.75}$로 증가한다 [G&W Table 2.22, p.180; R&T Fig.22-1, p.732].

#### A. Formal Definition

$$CL_i=a\cdot BW_i^b \quad [G\&W\ Eq.2:380,\ p.176;\ PK28\ Eq.28:1,\ p.611]$$

G&W는 CL/metabolic rate의 대표 exponent를 0.75로 제시하지만, 실제 CL exponent는 약 0.2에서 >1까지 변할 수 있다고 경고한다 [G&W p.178]. Fig.2.159는 91개 화합물의 CL exponent 분포가 주로 0.5–1.0 범위에 놓임을 보여준다 [G&W p.191].

#### B. Plausible Fallacy — `b=1` linear per-kg scaling

**오류:** “mg/kg 처방에 익숙하니 clearance도 kg에 선형 비례한다.” 이것이 linear per-kg scaling(← kg당 값이 일정하다는 가정) 오류다.  
<!-- ANNOTATION -->
**교정:** CL은 rate/flow variable이므로 `b≈0.75`가 physiological prior다.

- **R&T 20-g mouse→70-kg human:** `b=1`이면 3500, `b=0.75`이면 455 → 7.7배 차이 [R&T p.733].
- **G&W PK28 23-g mouse→70-kg human:** $(70/0.023)^{0.25}\approx7.4$배 차이.
- **Rat 250-g→70-kg human:** $(70/0.25)^{0.25}\approx4.1$배 차이.

Target AUC dose 계산에서는 CL 과대예측이 목표 AUC를 맞추기 위한 dose 과대 산출로 이어질 수 있다. 따라서 “CL 과대평가 → subtherapeutic 시작”이라는 단정은 사용하지 않는다.

#### C. Failure Conditions

Allometry failure는 random error가 아니라 mechanism signal일 수 있다. G&W Fig.2.145는 scalable compound에서는 70-kg human CL prediction interval이 약 10-fold 범위이지만, less scalable compound에서는 약 1000-fold 범위까지 넓어질 수 있음을 보여준다 [G&W p.174].

주요 failure trigger:

1. species-dependent plasma protein binding;
2. different metabolic routes or CYP isozyme composition;
3. nonlinear Michaelis-Menten behavior;
4. enterohepatic recirculation;
5. route/formulation differences;
6. variable central/peripheral volume ratio [G&W p.191].

> <!-- TRENCH -->
> **[TRENCH — unbound clearance scaling]** 종간 fu 차이가 크면 total CL이 아니라 $CL_u=CL/f_u$를 스케일링한다. G&W Eq.2:421은 $CL_{u,man}=CL_{u,rat}\cdot(BW_{man}/BW_{rat})^b$ 형태로 제시되며 [G&W p.190], R&T Table 22-1은 cefazolin 등에서 human-animal plasma protein binding 차이가 크게 나타날 수 있음을 보여준다 [R&T p.740]. `[교과서 외 실무 해석]` fu 비교는 가능하면 동일 농도, buffer, 온도, assay method에서 측정된 값끼리 해야 한다.

#### D. Expert Diagnostic Trigger

`[교과서 외 실무 해석]` PopPK 또는 종간 회귀에서 estimated $b>1$이 나오면 “추정값을 그대로 믿을 것인가?”가 아니라 “종간 binding, transporter, saturation, data quality 중 무엇이 slope를 밀어 올렸는가?”를 먼저 묻는다. 반대로 두 종만으로 얻은 $b<0.5$는 생리학적 신호보다 statistical leverage failure일 가능성이 크다.

#### E. Zettelkasten Atom

```yaml
aliases: [clearance allometric exponent, b_CL, Brody-Kleiber clearance scaling]
tags: [pharmacometrics/allometry, clearance, FIH/exposure-translation]
source: "G&W §2.10.3 p.176–180; G&W Fig.2.159 p.191; R&T Ch.22 p.732–735"
```

<!-- ANCHOR -->
CL의 $b\approx0.75$는 시간당 처리량의 지수다. 그럼 V는 왜 $d\approx1$인가? 답은 V가 “흐름”이 아니라 “공간”이기 때문이다.

<!-- FIGURE_POINTER --><br>Source: Rowland & Tozer 5e, Ch.22, p.733, Fig.22-2<br>Why this matters: This is the cleanest source-side visual for the b=1 versus b=0.75 error. It makes the 7.7-fold mouse-human gap visible rather than merely calculable.<br>When to look: After reading C2 Plausible Fallacy and before moving to C2 Failure Conditions.<br>Learner instruction: Compare the b=1 and b=0.75 projections at the human body-weight end. Then restate in one sentence why mg/kg linear scaling overestimates human CL/dose in target-AUC logic.<br><!-- /FIGURE_POINTER -->

<!-- FIGURE_POINTER --><br>Source: Gabrielsson & Weiner 5e, §2.10.3, p.174, Fig.2.145<br>Why this matters: The figure separates compounds where allometry gives a useful prediction from compounds where prediction intervals become dangerously wide. This directly supports the C2 message that failure is often a mechanism/data-quality signal, not just noise.<br>When to look: After reading C2 Failure Conditions.<br>Learner instruction: Identify which panel represents a scalable compound and which represents a less scalable compound. Then map the broad prediction interval back to at least two C2 failure triggers.<br><!-- /FIGURE_POINTER -->

> **Practice Lens — [AUDIT_DERIVED]**  
> `b=1` 오류를 검토할 때는 “용량이 낮아진다/높아진다”라는 구호보다 계산 논리를 먼저 고정한다. Target AUC 기반에서는 CL 과대예측이 dose 과대 산출로 이어질 수 있으므로, 방향성 문장은 항상 exposure target과 함께 써야 한다.

---

### ━━ C3. Volume Exponent $d\approx1.0$ ━━

<!-- MASTER LENS -->
**개념 Big Idea:** V는 flow가 아니라 extent다. 체액, 혈액량, 조직 부피가 대체로 체중에 비례하므로 분포용적은 대략 BW¹로 증가한다. 이 $d\approx1$과 CL의 $b\approx0.75$의 차이 0.25가 종간 시간 척도를 만든다.

#### A. Formal Definition

$$V_i=c\cdot BW_i^d \quad [G\&W\ Eq.2:382,\ p.179;\ PK28\ Eq.28:2,\ p.611]$$

G&W Table 2.22는 blood volume exponent 0.99, skeletal mass 1.09, Vd 약 1.0을 제시한다 [G&W p.180].

#### B. Consequence — half-life and rate constant

$$t_{1/2}=\ln2\cdot\frac{V}{CL}=\ln2\cdot\frac{c\cdot BW^d}{a\cdot BW^b}\propto BW^{d-b}$$

$d\approx1$, $b\approx0.75$이면:

$$t_{1/2}\propto BW^{0.25},\qquad k_{el}=\frac{CL}{V}\propto BW^{b-d}\approx BW^{-0.25}$$

<!-- ANCHOR -->
학생은 “half-life는 BW^0.25”를 외우지만, 더 중요한 것은 **모든 first-order rate constant가 큰 동물에서 더 작아진다**는 사실이다. 같은 분수 $V/CL$을 시간으로 읽으면 half-life이고, 뒤집어 $CL/V$로 읽으면 rate constant다. 즉 큰 동물은 절대 CL은 크지만, 단위 시간당 제거되는 fraction은 작다.
<!-- ANNOTATION -->

#### C. Data Anchor — Methadone PK28

G&W PK28 methadone anchor:

| Species | BW | Dose | Note |
|---|---:|---:|---|
| Mouse | 23 g | 25 µg IV bolus | elementary Dedrick anchor |
| Rat | 250 g | 500 µg IV bolus | source-internal t½ discrepancy 있음 |
| Man | 70 kg | 100,000 µg IV bolus | human anchor |

- $a=0.319$, $AUC=1/a=3.13$ [G&W §2.10.6 p.186; PK28 p.613].
- Hepatic extraction <10% [G&W p.186; PK28 p.613].
- **t½ discrepancy:** G&W §2.10.6 본문은 1.5/2.9/35 h, PK28 case는 1.5/3.9/35 h로 rat 값이 다르다. 본문 인용 시 `[§2.10.6 set]` 또는 `[PK28 case set]`을 명시한다.

#### D. Limitations

V exponent는 대체로 1에 가깝지만, $V_{ss}$는 tissue affinity, fat distribution, transporter, protein binding에 따라 0.8–1.2 범위로 흔들릴 수 있다. R&T Ch.14의 obesity examples도 “body weight가 항상 biologically relevant volume은 아니다”라는 경고로 읽어야 한다 [R&T p.439].

<!-- RECAP -->
**C3 핵심:** $d\approx1$은 분포 공간이 체중에 비례한다는 뜻이고, $b<d$는 큰 동물에서 제거 fraction이 느려진다는 뜻이다. $d-b$와 $b-d$를 동시에 볼 수 있어야 half-life와 rate constant를 같은 구조로 이해한다.

<!-- FIGURE_SCHEMATIC --><br>Title: Flow vs extent split: why b and d cannot be swapped<br>Mode: N<br>Visual objective: 5초 안에 CL, V, half-life, and kel의 방향성을 분리한다.<br>Core message: CL은 flow라서 b≈0.75, V는 extent라서 d≈1이며, 두 지수의 차이가 time과 rate constant를 반대 방향으로 만든다.<br>Elements to include: Two-column layout CL = a·BW^b vs V = c·BW^d; labels flow/rate vs space/extent; arrows V/CL → t1/2 ∝ BW^(d-b); CL/V → kel ∝ BW^(b-d); warning strip Do not use d=1 for CL scaling and Do not use b=0.75 for V scaling without evidence.<br>Elements to exclude: new animal examples, extra species-specific numbers, study-problem calculations.<br>Suggested rendering: CSS-card<br>Caption: The clinical error is not forgetting 0.75; it is swapping a flow exponent and a volume exponent.<br>Alt text: A two-column diagram contrasts clearance as flow with exponent 0.75 and volume as extent with exponent 1, then shows half-life and elimination rate constant as opposite ratios.<br>Source relation: Newly designed<br><!-- /FIGURE_SCHEMATIC -->

> **Failure Mode — [CRUCIBLE_DERIVED]**  
> $t_{1/2}$만 외우면 $k_{el}$의 부호를 놓친다. 큰 동물에서 rate constant가 작아지는 구조를 보지 못하면 CL과 V의 exponent를 서로 바꾸는 오류가 반복된다.

---

### ━━ C4. Dedrick Superposition: Elementary + Complex ━━

<!-- MASTER LENS -->
**개념 Big Idea:** Dedrick plot(← 종별 PK 곡선을 같은 척도에 겹치는 변환)은 종간 PK curve를 “같은 과정의 다른 시간 척도”로 접어 넣는 변환이다.
<!-- ANNOTATION --> 시간축만 조정하는 것이 아니라, dose-normalized concentration 축도 BW exponent에 맞게 조정한다.

#### A. Formal Definitions

**Elementary Dedrick plot** (`d=1` 가정):

$$y=\frac{C}{Dose/BW},\qquad x=\frac{t}{BW^{1-b}}$$

**Complex Dedrick plot** (`d\neq1` 일반형):

$$y=\frac{C}{Dose/BW^d}=\frac{C\cdot BW^d}{Dose},\qquad x=\frac{t}{BW^{d-b}}$$

Kallynochron은 $d=1$ 가정의 per-kg time scale이고, Apolysichron은 $d$를 명시적으로 반영한 generalized physiological time scale이다 [G&W §2.10.6–2.10.7, p.184–189].

#### B. Derivation

Mono-exponential model:

$$C=\frac{D_{iv}}{V}\cdot e^{-(CL/V)t}$$

Allometric substitution:

$$C=\frac{D_{iv}}{c\cdot BW^d}\cdot e^{-(a/c)\cdot BW^{b-d}\cdot t} \quad [G\&W\ Eq.2:384,\ p.179]$$

따라서 concentration은 $Dose/BW^d$로, time은 $BW^{d-b}$로 정규화되어야 한다. `[교과서 외 수학적 해석]`으로 말하면 이는 Buckingham π theorem류의 dimensional analysis와 같은 직관이다. 변수들이 가진 mass/time/volume 차원을 제거하면 독립적인 무차원 그룹이 남고, Dedrick 변환은 그 그룹의 PK 버전이다.

#### C. AUC relation

Elementary Dedrick context에서 G&W는 AUC가 $1/a$로 정리됨을 보인다 [G&W Eq.2:386, p.179]. 이것은 C5의 “equal unbound AUC”와 분리된 사실이 아니라 같은 논리의 수학적 전단계다.

#### D. Data Anchor — PK28 and PK29

**PK28 Methadone**: mouse/rat/man IV bolus 자료를 elementary Dedrick plot으로 중첩한다 [G&W p.184–186; PK28 p.611–614]. 단, case는 단일 dose level이며 G&W도 ≥2 dose levels, multiple dosing/steady state, model misspecification 배제가 필요하다고 경고한다 [PK28 p.614].

**PK29 Compound X**: mouse 20 g, rat 250 g, monkey 3.5 kg, dog 14 kg, man 70 kg의 5종 자료를 사용한다 [G&W p.186–189; PK29 p.615–620].

- G&W §2.10.7 parameter set: $a=0.021$, $b=0.74$, $c=0.076$, $d=1.18$, $e=0.56$, $g=0.075$ [G&W p.189].
- PK29 case set: $a=0.021$, $b=0.75$, $c=0.10$, $d=1.21$, $e=0.54$, $g=0.071$ [PK29 p.619].
- Weight range: arithmetic 70/0.020 = 3500-fold; PK29 case text may state about 3000-fold. 본문에서는 `about 3000–3500-fold`로 표기한다.

> <!-- TRENCH -->
> **[TRENCH — Elementary vs Complex Dedrick switch]** log-log $V$ vs $BW$ slope가 0.9–1.1 밖이면 Elementary Dedrick($d=1$ 가정)을 고집하지 않는다. PK29처럼 $d\approx1.18$이면 $C/(Dose/BW^d)$와 $t/BW^{d-b}$를 쓰는 Complex Dedrick으로 전환한다.

<!-- RECAP -->
**C4 핵심:** Dedrick superposition은 curve-fitting 장식이 아니라 CL exponent와 V exponent를 동시에 검증하는 diagnostic이다. Elementary가 실패하면 “plot이 안 예쁜 것”이 아니라 “d=1 가정이 깨졌을 가능성”을 먼저 본다.

<!-- FIGURE_POINTER --><br>Source: Gabrielsson & Weiner 5e, Case Study PK28, p.613, Fig.28.2<br>Why this matters: It is the best learner-facing view of elementary Dedrick superposition for methadone. The learner sees that normalization is meant to collapse mouse, rat, and human concentration-time curves onto a shared physiological time scale.<br>When to look: After reading C4 Data Anchor — PK28 and before reading C4 limitations.<br>Learner instruction: Focus on the axis transformations, not only the curve shapes. Ask what assumption about d is required for this elementary version to work.<br><!-- /FIGURE_POINTER -->

<!-- FIGURE_POINTER --><br>Source: Gabrielsson & Weiner 5e, Case Study PK29, p.619, Fig.29.3<br>Why this matters: This is the final visual proof of why Complex Dedrick is needed when d≠1 and multicompartment scaling enters. It connects the allometric parameter set to curve superposition.<br>When to look: After F5 and after reading C4 Complex Dedrick / PK29 material.<br>Learner instruction: Compare this figure mentally against the elementary Dedrick logic. Identify where the BW^d normalization changes the concentration axis and why that matters for compound X.<br><!-- /FIGURE_POINTER -->

> **Practice Lens — [CRUCIBLE_DERIVED]**  
> Dedrick plot은 예쁜 overlay를 만드는 도구가 아니라 exponent pair를 검증하는 진단 도구다. Curve fan-out이 보이면 먼저 $d=1$ 가정, compartment 비율, binding 또는 mechanism mismatch를 의심한다.

---

### ━━ C5. FIH Dose Translation의 Allometric Backbone ━━

<!-- MASTER LENS -->
**개념 Big Idea:** C5는 FIH starting dose 전체를 결정하는 단독 공식이 아니다. G&W Eq.2:417–421은 **equal unbound AUC(← 자유 약물 AUC를 같게 맞추는 기준)를 유지하기 위한 total dose scaling backbone**이다.
<!-- ANNOTATION --> 실제 FIH starting dose는 이 backbone에 safety margin, toxicology, pharmacology, exposure-response, route, formulation, PD metric을 더해 결정한다.

#### A. Equal-unbound-AUC backbone

$$AUC_{u,rat}=AUC_{u,man}=\frac{Dose_{rat}}{CL_{u,rat}}=\frac{Dose_{man}}{CL_{u,man}} \quad [G\&W\ Eq.2:417,\ p.190]$$

$$Dose_{man}=Dose_{rat}\cdot\left(\frac{BW_{man}}{BW_{rat}}\right)^b \quad [G\&W\ Eq.2:420,\ p.190]$$

$$CL_{u,man}=CL_{u,rat}\cdot\left(\frac{BW_{man}}{BW_{rat}}\right)^b \quad [G\&W\ Eq.2:421,\ p.190]$$

mg/kg dose ratio로 쓰면:

$$\frac{Dose_{man}/BW_{man}}{Dose_{rat}/BW_{rat}}=\left(\frac{BW_{man}}{BW_{rat}}\right)^{b-1}$$

$b<1$이면 큰 동물의 mg/kg dose는 작은 동물보다 낮아진다.

#### B. Assumptions

1. unbound AUC가 pharmacologic effect와 연결된다;
2. target affinity와 relevant pharmacology가 종간 크게 다르지 않다;
3. PK가 linear range에 있다;
4. fu 차이가 있으면 $CL_u$로 보정한다;
5. AUC가 적절한 exposure metric이다. Cmax-driven toxicity 또는 time-above-threshold metric이면 별도 판단이 필요하다.

G&W는 equal AUC라도 concentration-time curve의 shape는 상당히 다를 수 있음을 명시한다 [G&W p.190]. 따라서 C5는 AUC backbone이지 full curve equivalence 보장이 아니다.

#### C. Pediatric and elderly context from R&T

R&T Ch.14는 age, weight, gender가 drug response variability의 중요한 원천이며, chronologic age가 functional age를 정의하지 않는다고 경고한다 [R&T p.411–412]. 또한 age를 고려하지 않는 flat dosing은 개별 elderly patient의 필요를 충족하지 못할 수 있다고 설명한다 [R&T p.412].

R&T Key Relationships는 BSA를 다음처럼 체중 기반으로 근사한다:

$$BSA=1.73\cdot\left(\frac{Weight}{70}\right)^{0.75} \quad [R\&T\ p.436]$$

그리고 typical 60-year-old adult 대비 child maintenance dose를 다음처럼 제시한다:

$$Child\ maintenance\ dose=1.5\cdot\left(\frac{Weight_{child}}{70}\right)^{0.75}\cdot Typical\ adult\ maintenance\ dose \quad [R\&T\ Eq.14\text{-}6,\ p.432;\ Key\ Relationships,\ p.436]$$

다만 R&T는 mg/kg 또는 mg/1.73 m² 규칙의 broader use는 적용 한계(age, body composition, renal function)를 명시하지 않으면 의심스럽다고 경고한다 [R&T p.435]. 즉 **BW allometry는 시작점이지, pediatric/elderly dose equation 전체가 아니다.**

#### D. Elderly metabolism statement correction

“CYP3A4 metabolism이 60세 이상 매년 1% 감소”라는 문장은 과단정이다. R&T는 creatinine clearance가 adulthood에서 대략 1%/yr 감소한다는 rule of thumb을 제시하고 [R&T p.422], CYP3A substrates에서는 elderly group이 young adult보다 낮은 clearance를 보이며 그 연령 차이를 해석할 때 1%/yr creatinine clearance heuristic이 관련된다고 설명한다 [R&T p.424]. 따라서 최종 문장은 다음처럼 제한한다: **노인에서는 renal/hepatic function과 biological age를 별도로 보아야 하며, CYP3A clearance도 young adult 대비 감소할 수 있지만 단순 선형 시간 함수로 쓰지 않는다.**

<!-- RECAP -->
**C5 핵심:** C5의 수식은 equal unbound AUC를 맞추는 allometric backbone이다. FIH dose justification이나 pediatric/elderly dosing에서는 이 backbone 위에 functional age, renal/hepatic function, body composition, binding, PD metric, safety margin을 얹어야 한다.

<!-- FIGURE_POINTER --><br>Source: Rowland & Tozer 5e, Ch.14, p.430, Fig.14-20<br>Why this matters: It visually prevents the common mistake that BW^0.75 alone solves pediatric/elderly dosing. It shows maintenance-dose fraction varying across age, which is exactly the C5 caveat.<br>When to look: After reading C5 Pediatric and elderly context and before the C5 recap.<br>Learner instruction: Track how dose fraction changes from infancy through old age. Then state why functional age and renal/hepatic function must sit on top of BW allometry.<br><!-- /FIGURE_POINTER -->

> **Mastery Note — [TEXTBOOK_DERIVED]**  
> Equal-AUCu dose backbone은 “최종 FIH dose”가 아니라 exposure translation의 중심축이다. R&T의 age/weight 논리는 이 축 위에 functional age와 organ function을 더해야 개인 환자 용량이 된다는 점을 보강한다.

---

## §5 — Confusion Pair Dissection

---

<!-- CONFUSION -->
### Pair 1. Clearance exponent $b$ vs Volume exponent $d$

| 비교 차원 | $b$ — CL exponent | $d$ — V exponent |
|---|---|---|
| 변수 성격 | flow/rate, 단위 시간당 처리량 | space/extent, 분포 공간 |
| 전형값 | $b\approx0.75$ | $d\approx1.0$ |
| 생리학적 근거 | metabolic rate, organ blood flow, GFR | body water, blood volume, tissue volume |
| 체중 2배 시 | CL 약 $2^{0.75}=1.68$배 | V 약 $2^1=2$배 |
| 시간 결과 | $t_{1/2}\propto BW^{d-b}$ | $k_{el}\propto BW^{b-d}$ |
| 가장 위험한 오류 | dose/CL scaling에 $d=1$을 넣어 linear per-kg처럼 외삽 | V scaling에 $b=0.75$를 넣어 volume을 과소/과대예측 |

**Critical Blow:** rat 250 g→human 70 kg에서 $b=0.75$ 대신 $d=1$처럼 선형 scaling하면 차이는 $(70/0.25)^{0.25}\approx4.1$배다. mouse 23 g→human에서는 약 7.4배, R&T 20-g mouse 예시는 7.7배다. 이 오류는 “소수점 차이”가 아니라 첫 human exposure estimate의 order를 바꾼다.

---

<!-- CONFUSION -->
### Pair 2. Kallynochron vs Apolysichron

| 비교 차원 | Kallynochron | Apolysichron |
|---|---|---|
| 사용 맥락 | Elementary Dedrick | Complex Dedrick |
| 전제 | $d=1$ | $d$를 추정/반영 |
| 시간축 | $t/BW^{1-b}$ | $t/BW^{d-b}$ |
| 해석 | per-kg clearance time | per-$BW^d$ fractional elimination time |
| 실패 신호 | $d\neq1$이면 curve fan-out | $d\neq1$에서 curve collapse 가능 |

**기억 고리:** Kallynochron은 “kg당 청소”의 시간이고, Apolysichron은 “$BW^d$당 청소”의 시간이다. $d=1$이면 둘은 같아 보이지만, PK29 compound X처럼 $d>1$이면 차이가 드러난다.

---

<!-- CONFUSION -->
### Pair 3. Body Weight Allometric Scaling vs Body Surface Area Scaling

| 비교 차원 | $BW^b$ allometry | BSA scaling |
|---|---|---|
| 수식 | $Y=a\cdot BW^b$ | $BSA\approx1.73(Weight/70)^{0.75}$ |
| 지수 | 변수/자료에 따라 추정 또는 prior | 임상적으로 체중 0.75승 근사 |
| 장점 | 화합물·변수 특이성 반영 | 처방/소아 용량에 친숙 |
| 위험 | 종 수 부족 시 slope 불안정 | 적용 한계 없이 광범위 사용 시 부정확 |
| R&T 메시지 | — | mg/kg 또는 mg/1.73 m² rule은 age, body composition, renal function 한계를 명시해야 함 [R&T p.435] |

**정리:** BSA는 allometry의 적이 아니라 임상적으로 굳어진 $BW^{0.75}$ 근사다. 그러나 BSA라는 이름이 붙었다고 renal maturation, obesity, functional age 문제가 사라지는 것은 아니다.

<!-- RECAP -->
**§5 요약:** `b`와 `d`의 혼동은 dose와 half-life를 동시에 망가뜨린다. Kallynochron/Apolysichron 혼동은 Dedrick plot 해석을 망가뜨린다. BSA와 BW allometry 혼동은 pediatric/elderly dosing을 과도하게 단순화한다.

> **Failure Mode — [CRUCIBLE_DERIVED]**  
> 혼동쌍은 암기 문제가 아니라 보고서 검토 checklist다. `b/d`, Kallynochron/Apolysichron, BSA/BW allometry 중 하나라도 섞이면 table, figure, dose narrative가 동시에 흔들린다.

---

## §7 — Self-Test: Active Recall Module

---

<!-- SELF-TEST -->
### Q1. Recall — `a`와 `b`의 의미

**질문:** $Y=a\cdot BW^b$에서 $a$와 $b$를 각각 한 문장으로 설명하고, CL과 V의 전형적 exponent를 답하시오.

**정답:**

- $a$: compound-dependent intercept; $BW=1$에서의 기준값이며 단위는 $b$에 의존한다.
- $b$: 체중 변화에 대한 scaling exponent; 대체로 변수 유형에 의존하지만 자료 품질과 mechanism에 따라 변한다.
- CL: $b\approx0.75$; metabolic rate/functional flow variable.
- V: $d\approx1.0$; volume/extent variable.
- 따라서 $t_{1/2}\propto BW^{d-b}\approx BW^{0.25}$, $k_{el}\propto BW^{b-d}\approx BW^{-0.25}$.


---

<!-- SELF-TEST -->
### Q2. Recall — 왜 `b=1`이 위험한가

**질문:** 23-g mouse에서 70-kg human으로 CL을 외삽할 때 `b=1`과 `b=0.75`의 차이는 몇 배인가? rat 250 g→human에서는 몇 배인가?

**정답:**

- Mouse 23 g→human 70 kg: $(70/0.023)^{1-0.75}\approx7.4$배.
- Rat 250 g→human 70 kg: $(70/0.25)^{0.25}\approx4.1$배.
- R&T의 20-g mouse 예시는 3500 vs 455로 7.7배 차이를 제시한다 [R&T p.733].
- Target AUC 기반 dose 계산에서는 CL 과대예측이 dose 과대 산출로 이어질 수 있다.


---

<!-- SELF-TEST -->
### Q3. Derivation — $t_{1/2}$와 $k_{el}$의 종간 지수

**질문:** $CL=aBW^b$, $V=cBW^d$일 때 $t_{1/2}$와 $k_{el}$의 BW exponent를 도출하시오.

**정답:**

$$t_{1/2}=\ln2\cdot V/CL=\ln2\cdot(c/a)BW^{d-b}$$

$$k_{el}=CL/V=(a/c)BW^{b-d}$$

$d=1$, $b=0.75$이면 $t_{1/2}\propto BW^{0.25}$이고 $k_{el}\propto BW^{-0.25}$이다. 큰 동물은 절대 CL이 크지만, 단위 시간당 제거 fraction은 작다.


---

<!-- SELF-TEST -->
### Q4. Dedrick — Elementary vs Complex

**질문:** Elementary Dedrick과 Complex Dedrick의 y축/x축 변환을 쓰고, 언제 Complex가 필요한지 답하시오.

**정답:**

- Elementary: $C/(Dose/BW)$ vs $t/BW^{1-b}$; $d=1$ 가정.
- Complex: $C/(Dose/BW^d)$ 또는 $C\cdot BW^d/Dose$ vs $t/BW^{d-b}$.
- log-log $V$ vs $BW$ slope가 1에서 벗어나면, 예를 들어 PK29 compound X처럼 $d\approx1.18$이면 Complex Dedrick이 필요하다.


---

<!-- SELF-TEST -->
### Q5. Source discrepancy handling — PK28/PK29

**질문:** PK28 methadone과 PK29 compound X의 source-internal numerical discrepancy를 어떻게 인용해야 하는가?

**정답:**

- PK28 methadone rat $t_{1/2}$: G&W §2.10.6 본문은 2.9 h, PK28 case는 3.9 h로 다르다. 하나를 고르지 말고 `[§2.10.6 set]` 또는 `[PK28 case set]`을 명시한다.
- PK29 parameter set: G&W §2.10.7은 $a=0.021,b=0.74,c=0.076,d=1.18,e=0.56,g=0.075$; PK29 case는 $a=0.021,b=0.75,c=0.10,d=1.21,e=0.54,g=0.071$이다. citation scope와 수치를 일치시킨다.


---

<!-- SELF-TEST -->
### Q6. Application — human CL 예측

**시나리오:** Mouse BW=25 g, observed CL=0.012 L/hr. 70-kg human CL을 (a) $b=0.75$, (b) $b=1.0$으로 계산하고 차이를 해석하시오.

**정답:**

(a) $CL_{human}=0.012\cdot(70/0.025)^{0.75}\approx4.6$ L/hr.  
(b) $CL_{human}=0.012\cdot(70/0.025)^1\approx33.6$ L/hr.  
차이는 약 7.3배다. $b=1$은 linear per-kg fallacy이며, target AUC 기반에서는 dose도 과대 산출할 수 있다.


---

<!-- SELF-TEST -->
### Q7. Application — child/elderly dose context

**질문:** 왜 소아 또는 노인 용량에서 $BW^{0.75}$만으로 충분하지 않은가?

**정답:**

R&T Ch.14는 chronologic age가 functional age를 정의하지 않는다고 설명한다 [R&T p.411–412]. 소아에서는 renal/hepatic maturation, 체수·binding 변화가 중요하고, 노인에서는 renal function, hepatic metabolism, disease state, body composition이 중요하다. 따라서 $BW^{0.75}$는 시작점일 뿐이며, renal/hepatic function과 biological age 보정이 필요하다.


---

<!-- SELF-TEST -->
### Q8. Boss Dilemma — two-species regression vs physiological prior

**시나리오:** Rat와 dog 두 종만으로 log-log CL 회귀를 했더니 $b=0.62$가 나왔다. 문헌적 physiological prior $b=0.75$와 충돌한다. FIH exposure translation table에는 무엇을 primary로 두겠는가?

**정답:**

두 종 회귀의 점추정값은 leverage가 약하고 confidence interval이 넓을 가능성이 크다. 따라서 primary는 physiological prior $b=0.75$로 두고, $b=0.5,0.62,0.75,1.0$ sensitivity analysis를 함께 제시한다. 단, `b=0.75`를 특정 ICH/FDA 조항이 직접 명시한다고 쓰지 않는다. 본 PDF 범위에서 방어 가능한 표현은 “mammalian metabolic rate와 functional flow variable의 allometric rationale에 근거한 prior”이다. `[확인 필요]` 규제 문구는 원문 가이드라인 확인 전 사용하지 않는다.


<!-- RECAP -->
**§7 요약:** self-test의 목표는 수치 암기가 아니라 세 가지 방어 능력이다. (1) `b`와 `d`를 구별한다. (2) `b=1` 오류가 dose/AUC에 주는 방향을 설명한다. (3) source discrepancy와 NOT_IN_SOURCE 규제 표현을 스스로 차단한다.

> **Practice Lens — [EXPERT_INFERENCE]**  
> Self-test 답안을 실제 보고서 문장으로 바꿀 때는 “무엇을 primary assumption으로 두고, 무엇을 sensitivity로 보였는가”를 반드시 적는다. 이렇게 쓰면 수식 지식이 모델 선택의 방어 논리로 전환된다.

---

## §8 — Meta-Frame & Big Picture

### A. Positioning — 이 세션이 시스템으로 작동하는 세 순간

1. **Animal-to-human exposure translation table:** C1이 table equation, C2가 CL column, C3가 V/time column, C4가 curve-superposition check, C5가 equal-AUCu dose backbone이다.
2. **PopPK weight covariate decision:** `[교과서 외 구현 해석]` WT exponent를 fix할지 estimate할지 결정할 때 C2의 physiological prior와 C3의 V exponent가 동시에 필요하다.
3. **PBPK parameter scaling:** R&T Ch.22는 allometry를 human kinetics prediction의 한 축으로 다룬다. Organ blood flow는 rate-like, organ volume은 extent-like로 구분해 scale해야 한다 [R&T p.731–743].

### B. Failure Modes if this section is weak

**Failure Mode 1 — Allometric Slope Drift.**  
`[교과서 외 구현 해석]` 성인 60–90 kg처럼 WT range가 좁은 데이터에서 CL exponent를 자유 추정하면 SE가 커지고 점추정값이 흔들린다. 이 경우에는 $b=0.75$ fixed model을 primary로 두고, sensitivity analysis로 추정값의 영향을 따로 보여주는 편이 더 방어 가능하다.

**Failure Mode 2 — Volume Exponent Lock-in Bias.**  
$V$ exponent를 항상 1로 고정하면 PK29 compound X처럼 $d>1$인 약물에서 Dedrick superposition이 실패한다. 큰 체중에서 ηV trend가 남으면 d를 estimate하거나 Complex Dedrick 구조를 검토한다.

**Failure Mode 3 — Functional age omission.**  
소아·노인에서 BW scaling만 쓰면 maturation, renal function, body composition, disease state가 누락된다. R&T의 핵심 메시지는 “typical patient”와 “individual patient”가 다르다는 것이다 [R&T p.412–415].

### C. Professional Moat — diagnostic, not motivational

1. **$b$의 이탈을 신호와 잡음으로 구별한다.** $b>1$ 또는 $b<0.5$가 나오면 먼저 종 수, leverage, binding, nonlinearity, metabolism route 차이를 확인한다.
2. **FIH/exposure translation에서 수식과 언어를 분리한다.** G&W Eq.2:420은 equal-AUCu dose backbone이지 standalone starting-dose rule이 아니다.
3. **Dedrick plot을 diagnostic으로 읽는다.** Elementary plot fan-out은 “그림 실패”가 아니라 $d\neq1$, multicompartment 비율 차이, 또는 model misspecification의 신호다.
4. **Source discrepancy를 숨기지 않는다.** PK28 t½와 PK29 parameter set 불일치는 citation 규약으로 드러내고, 임의로 하나를 정답처럼 고정하지 않는다.

### D. Final One-Page Mental Model

```text
1. 변수의 종류를 먼저 묻는다.
   - flow/rate?  → CL, GFR, blood flow → b≈0.75
   - space/extent? → V, blood volume, tissue mass → d≈1
   - time? → V/CL → d-b≈0.25
   - rate constant? → CL/V → b-d≈-0.25

2. 종간 dose/exposure translation은 total dose가 아니라 unbound exposure 관점에서 읽는다.
   - AUCu equality → Dose ∝ BW^b
   - mg/kg ratio → BW^(b-1)

3. 예외를 먼저 찾는다.
   - fu 차이, CYP isoform 차이, nonlinear PK, transporter, enterohepatic recirculation, route/formulation 차이

4. source language를 지킨다.
   - PDF-supported: G&W/R&T 수식, PK28/PK29 anchor, R&T age/renal/BSA caution
   - not directly supported: ICH/FDA/MABEL/NONMEM/QSP claims → 삭제 또는 [교과서 외 해석]
```

<!-- RECAP -->
**§8 최종 요약:** Session 14의 핵심은 `0.75를 외우는 것`이 아니다. `어떤 변수가 왜 0.75이고, 어떤 변수는 왜 1이며, 그 차이가 시간과 dose를 어떻게 바꾸는지`를 보는 것이다. 이 학습본은 allometric spine을 유지하되, fold 오류, FIH overclaim, source-internal discrepancy, unsupported regulatory language를 제거한 형태로 읽어야 한다.

> **Mastery Note — [EXPERT_INFERENCE]**  
> 이 세션의 최종 문장은 “0.75가 맞다”가 아니라 “0.75는 flow 변수의 생리학적 prior이고, 자료와 mechanism이 그 prior를 언제 밀어내는지 판단한다”이다. 이 관점이 allometry를 공식 암기에서 모델링 판단으로 바꾼다.

---

## PART B — Compiler-Only Appendix

This appendix is not learner-facing. It exists only to protect Phase 5 rendering fidelity.

### B1. Compilation Contract

- PART A is the only learner-facing body.
- Phase 5 must render PART A without altering content.
- PART B is instruction/guardrail only.
- Do not restore deprecated material.
- Do not add new scientific content.
- Do not render PART B as learner content unless explicitly requested.

### B2. Figure Rendering Instructions

- Preserve the approved F1–F7 figure plan below.
- Preserve P/N decisions and source fields in PART A figure markers.
- Image rights = None: do not embed copyrighted textbook images. Render `FIGURE_POINTER` as text-only callout.
- Do not propose new figures.
- Do not generate Mermaid/SVG in Phase 4D; Phase 5 may render only approved schematics.

| # | Mode | Location | Source / relation | Rendering decision |
|---:|---|---|---|---|
| F1 | N schematic | §1 후, §2 진입 전 | Newly designed | Render as non-textbook allometric spine schematic; no copyrighted image. |
| F2 | P pointer | C2 말미 | R&T Ch.22 p.733 Fig.22-2 | Text-only pointer; no embedded figure. |
| F3 | P pointer | C2 말미 | G&W §2.10.3 p.174 Fig.2.145 | Text-only pointer; no embedded figure. |
| F4 | N schematic | C3 말미 | Newly designed | Render as CSS-card or Mermaid schematic; no new examples. |
| F5 | P pointer | C4 말미 | G&W PK28 p.613 Fig.28.2 | Text-only pointer; no embedded figure. |
| F6 | P pointer | C4 말미 | G&W PK29 p.619 Fig.29.3 | Text-only pointer; no embedded figure. |
| F7 | P pointer | C5 말미 | R&T Ch.14 p.430 Fig.14-20 | Text-only pointer; no embedded figure. |

### B3. Page Tag Rendering Rules

- Preserve all `[p.XX]`, `[pp.XX–YY]`, `[pp.XX, YY]`, and `[p.확인 필요]` tags exactly as present in PART A.
- Render page tags visibly in HTML.
- Do not fabricate, delete, renumber, or relocate page tags.
- `[p.확인 필요]` remains visible unless already resolved by Audit/Content Lock.

### B4. HTML Compiler Requirements

- Render PART A only; do not alter, summarize, reorder, or expand scientific content.
- Generate one self-contained HTML file with inline custom CSS and JS.
- External runtime dependencies are allowed only for MathJax CDN, Mermaid CDN, and approved CDN libraries such as highlight.js.
- MathJax: support inline `\(...\)` and display `\[...\]` as well as existing dollar-style equations after safe conversion if needed.
- Code blocks: render as `<pre><code>` with copy buttons.
- Self-test markers: render as click-to-reveal accordions; answers must be hidden by default.
- Controls: include print/PDF button using `window.print()` and copy controls for code blocks.
- Responsive layout: desktop left sticky sidebar; mobile single-column/collapsed navigation.
- Dark/light: respect `prefers-color-scheme`.
- Print: hide navigation/backgrounds but keep source-page tags visible.

#### Marker-to-component mapping

| Marker / Pattern | HTML component | Required style/behavior |
|---|---|---|
| `&lt;!-- MASTER LENS --&gt;` | callout box | gold border-left, soft background |
| `&lt;!-- ANNOTATION --&gt;` | inline note/tooltip style | muted italic small text |
| `&lt;!-- ANCHOR --&gt;` | bridge sentence | muted italic bridge |
| `&lt;!-- TRENCH --&gt;` | practical tip box | rose border-left/background |
| `&lt;!-- CONFUSION --&gt;` | side-by-side comparison / amber box | preserve tables |
| `&lt;!-- SELF-TEST --&gt;` | accordion | question visible; answer hidden until click |
| `&lt;!-- RECAP --&gt;` | summary box | blue border-left/background |
| `[확인 필요]` | highlighted flag | `<mark>` |
| `[p.XX]`, `[pp.XX–YY]`, `[pp.XX, YY]` | source page span | `.source-page` |
| `[p.확인 필요]` | uncertainty source span | `.source-page.source-uncertain` |
| `&lt;!-- FIGURE_POINTER --&gt;` | textbook reference callout | text-only; purple border-left; no image |
| `&lt;!-- FIGURE_SCHEMATIC --&gt;` | inline schematic `<figure>` | Mermaid or CSS-card as specified; caption and alt text required |
| `&lt;!-- FIGURE_IMAGE_SLOT --&gt;` | image/placeholder | not used in this file unless explicitly supplied with rights |

#### Source page tag rendering

- Detect tags by regex-equivalent patterns: `\[p\.(\d+)\]`, `\[pp\.(\d+)[–-](\d+)\]`, `\[pp\.(\d+(?:,\s*\d+)+)\]`, `\[p\.확인 필요\]`.
- Apply detection to body text, cards, equation captions, and example headings.
- Do not apply detection inside code blocks or inside `FIGURE_*` marker blocks.
- Do not add, delete, renumber, or relocate source page tags.
- Keep source-page tags visible in print.

#### Navigation anchor integrity rules

- Include a sticky left sidebar table of contents.
- Use `<a href="#...">` links only.
- Every sidebar target must have exactly one matching body `id`.
- Every major section heading (§1, §2, §5, §7, §8) must receive a stable id.
- Every §2 concept card should receive a stable id when possible.
- Do not create duplicate ids or TOC links whose targets do not exist.
- Enable `html { scroll-behavior: smooth; }`.
- Before finalizing: count sidebar hrefs, confirm each target exists once, confirm no duplicate ids, and fix any mismatch.

#### Figure rendering constraints

- Every figure marker must become either a pointer callout or a proper `<figure>` block.
- `FIGURE_POINTER`: render Source / Why this matters / When to look / Learner instruction; do not generate or embed an image.
- `FIGURE_SCHEMATIC`: render only the listed elements and explicitly exclude listed exclusions; do not reproduce textbook layout, labels, or artwork.
- Mermaid self-check: valid directive, safe ASCII node IDs, quoted labels for special characters/non-ASCII, no trailing semicolons, and fallback to CSS-card/SVG if Mermaid is likely to fail.
- Do not add figures not present in PART A.

#### Prohibited in Phase 5

- Do not render PART B as learner content.
- Do not modify PART A text, page tags, equations, source language, or markers.
- Do not expose self-test answers by default.
- Do not leave markers as plain text.
- Do not embed textbook images without explicit rights.
- Do not output Mermaid that fails self-check.
- Do not create sidebar links with missing or duplicated ids.


### B5. Audit Guardrails

Do not restore or introduce:

- `4.1배` as mouse-human; it is rat 250 g→human 70 kg only.
- `7.4배` and `7.7배` without species/source distinction.
- The deleted claim “CL overprediction necessarily causes subtherapeutic starting dose.”
- Unsupported FDA/EMA/ICH/NDA/MABEL reviewer claims as textbook fact.
- Unsupported NONMEM/QSP implementation claims as textbook-derived content.
- Unsupported numerical values or examples absent from PDF/Audit/Content Lock.
- Embedded textbook figures despite Image rights = None.
- New figure ideas or unapproved code blocks.
- Total-CL scaling where unbound clearance is required by binding context.
- Silent correction of PK28 t½ or PK29 parameter-set discrepancies without source-scope labeling.


### B6. Crucible Guardrails

- Crucible Report v1 is not a raw content source for Phase 5.
- Preserve only logic already present in PART A or explicitly logged in the Mastery Augmentation Layer.
- Do not turn `EXPERT_INFERENCE` notes into textbook-derived statements.
- Do not reintroduce rejected or lower-priority Crucible items.
- Do not add new named drugs, new regulatory claims, new numerical thresholds, or new page tags from Crucible ideas.


### B7. Deprecated and Forbidden Restorations

- Step 1 Draft v0 is deprecated and must not be used as learner-body source.
- Do not restore rejected overclaims, unsupported numbers, unsupported regulatory claims, source-unsupported examples, unapproved code, or unapproved figures.
- Do not use Step 1 material except through a formally logged micro-patch gate.
- No such micro-patch was required for this assembly.


### B8. PATCH MODE Splice Verification Table

| Marker # | Anchor text (truncated to 60 chars) | Anchor found? | Match count | Inserted? | Final location (§ + card) |
|---|---|---|---:|---|---|
| F1 | `## §1 — Session Header & Roadmap` | YES | 1 | YES | §1 Session Header & Roadmap |
| F2 | `CL의 $b\approx0.75$는 시간당 처리량의 지수다. 그럼 V는 왜 $d\approx1$인가? 답은 ` | YES | 1 | YES | §2 C2 Clearance Exponent — b=1 fallacy |
| F3 | `CL의 $b\approx0.75$는 시간당 처리량의 지수다. 그럼 V는 왜 $d\approx1$인가? 답은 ` | YES | 1 | YES | §2 C2 Failure Conditions |
| F4 | `**C3 핵심:** $d\approx1$은 분포 공간이 체중에 비례한다는 뜻이고, $b<d$는 큰 동물에서 ` | YES | 1 | YES | §2 C3 Volume Exponent / §5 Pair 1 연결 |
| F5 | `**C4 핵심:** Dedrick superposition은 curve-fitting 장식이 아니라 CL e` | YES | 1 | YES | §2 C4 Elementary Dedrick / PK28 |
| F6 | `**C4 핵심:** Dedrick superposition은 curve-fitting 장식이 아니라 CL e` | YES | 1 | YES | §2 C4 Complex Dedrick / PK29 |
| F7 | `**C5 핵심:** C5의 수식은 equal unbound AUC를 맞추는 allometric backbon` | YES | 1 | YES | §2 C5 Pediatric/elderly context |


### B9. Zero-Omission Coverage Matrix

| Domain | Required item | Evidence in PART A | Status | Action |
|---|---|---|---|---|
| C1 Scope concepts | Master equation, CL exponent, V exponent, Dedrick, equal-AUCu dose backbone | §2 C1–C5 | PRESENT | None |
| C1 Scope chapter role | Theory/data-anchor chapter for FIH, pediatric dose, PBPK scaling, PK28/PK29 interpretation | §1 roadmap, §8 positioning | PRESENT | None |
| C2 Data anchors | G&W PK28 methadone mouse/rat/man BW/dose, AUC=1/a, hepatic extraction, t½ discrepancy | C3 Data Anchor; Q5 | PRESENT | None |
| C2 Data anchors | G&W PK29 compound X parameter-set discrepancy and complex Dedrick need | C4 Data Anchor; Q4/Q5 | PRESENT | None |
| C2 Data anchors | R&T 20-g mouse to 70-kg human 3500 vs 455, 7.7-fold | §1 Big Idea, C2, Q2 | PRESENT | None |
| C3 Audit MUST_FIX | 4.1/7.4/7.7 fold species pairs separated | §1 Big Idea; C2; §5 Pair 1; Q2 | PRESENT | None |
| C3 Audit MUST_FIX | `b=1` directionality corrected: target-AUC CL overprediction may cause dose overprediction | §1 Big Idea; C2; Q2; Practice Lens | PRESENT | None |
| C3 Audit MUST_FIX | Unsupported FDA/ICH/NDA/MABEL/NONMEM claims removed or downgraded | §1 caution; §7 Q8; §8 text labels `[교과서 외 구현 해석]` | PRESENT | None |
| C3 Audit SHOULD_FIX | `b` not treated as fixed natural constant; varies with data/mechanism | C1, C2, §8 | PRESENT | None |
| C4 Audit T5 | R&T Ch.14 age/renal/functional-age message preserved | C5, Q7, §8 Failure Mode 3 | PRESENT | None |
| C4 Audit T5 | Protein-binding/unbound clearance boundary retained | C1 Boundary, C2 TRENCH, C5 assumptions | PRESENT | None |
| C5 Figure coverage | F1–F7 approved figure markers present exactly once each; image rights respected | PART A figure markers; B8 verification | PRESENT | None |
| C5 Rejected figures | Rejected/deferred textbook figures not restored as embedded images | PART A has no `FIGURE_IMAGE_SLOT` and no image paths | PRESENT | None |
| C6 Page tags | Existing source page tags preserved; no new page tags fabricated by augmentation | PART A page tags inherited from Content Lock v2 and marker sources | PRESENT | None |
| C7 Crucible Grade A | Scale-invariance, k_el directionality, Dedrick diagnostic, source-boundary logic preserved | C1/C3/C4 notes; §7/§8 | PRESENT_COMPRESSED | None |
| C8 Deprecated Draft regression | Wrong FIH wording, unsupported regulatory overclaim, Step 1 figure/code overreach blocked | PART A and B5/B7 guardrails | PRESENT | None |
| C9 Canonical integrity | Scientific body equals §1–§8 of Content Lock v2 plus exact approved figure markers, labeled augmentation, and non-scientific process-label neutralization | PART A | PRESENT | None |

### B10. Micro-Patch Log

No scientific micro-patches were needed. PART A equals exact-spliced learner-facing Content Lock v2.1 except approved Mastery Augmentation Layer, learner navigation wrapper, and four non-scientific process-label neutralizations that remove `Draft v0`/`Content Lock` wording from learner-facing sentences without changing scientific meaning.

### B11. Mastery Augmentation Log

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
|---:|---|---|---|---|---|---|
| 1 | C1 end | M | YES | CRUCIBLE_DERIVED | Clarifies scale-invariance claim without adding new formula or page tag. | Low |
| 2 | C2 end | J/R | YES | AUDIT_DERIVED | Reinforces corrected AUC/dose directionality from Audit. | Low |
| 3 | C3 end | F | YES | CRUCIBLE_DERIVED | Prevents half-life/rate-constant sign confusion. | Low |
| 4 | C4 end | J | YES | CRUCIBLE_DERIVED | Frames Dedrick as diagnostic rather than decorative overlay. | Low |
| 5 | C5 end | R | YES | TEXTBOOK_DERIVED | Keeps equal-AUCu backbone distinct from final dose selection. | Low |
| 6 | §5 end | F | YES | CRUCIBLE_DERIVED | Turns confusion pairs into review checklist. | Low |
| 7 | §7 end | J | YES | EXPERT_INFERENCE | Converts self-test outputs into model-selection narrative. | Medium |
| 8 | §8 end | M | YES | EXPERT_INFERENCE | Locks allometry as prior-plus-override judgment. | Medium |


#### Rejected augmentation candidates

| Rejected candidate | Reason for rejection |
|---|---|
| Additional named clinical examples beyond methadone/compound X/cefazolin and source-listed context | Would introduce new named examples not required by Scope/Audit/Content Lock. |
| New regulatory agency-specific language for FIH justification | PDF does not directly support specific external regulatory wording; would violate source-boundary rule. |
| Additional numerical thresholds for acceptable b/d estimates | Would add unsupported numerical claims beyond the source/Audit/Content Lock set. |
| New figure ideas beyond F1–F7 | Would exceed Phase 4C approved figure plan and risk Phase 5 drift. |

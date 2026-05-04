# 14_Content Lock v1
## Session 14 · Allometric Scaling: Inter-Species Extrapolation, Body Weight, and Age

**Source set:** Gabrielsson & Weiner 5e §2.10, PK28, PK29 + Rowland & Tozer 5e Ch.14, Ch.22.  
**적용 입력:** Step 1 Draft v0 + Source Fidelity Audit Report v1 + Insight Crucible Report v1 + Original PDFs.  
**출력 상태:** Content Lock v1 — Phase 4C figure triage 전 텍스트 확정본.  
**표기 규약:** G&W 기준으로 clearance exponent는 **b**, volume exponent는 **d**로 쓴다. R&T Ch.22는 문맥상 두 지수를 모두 b로 표기하므로, 필요 시 **b_CL**, **b_V**로 병기한다.  
**외부 해석 규칙:** 원 PDF에 직접 근거가 없는 실무·규제·NONMEM 문장은 삭제하거나 `[교과서 외 실무/구현 해석]`으로 낮춘다. `[확인 필요]`는 삭제하지 않고 보류 항목에 남긴다.

---

## 0. Adjudication Table Summary

### 0.1 판정 집계

| 입력원 | ADOPT | PARTIAL_ADOPT | REJECT | 보류/Phase 4C 이월 | 핵심 조치 |
|---|---:|---:|---:|---:|---|
| Audit Report v1 | 31 | 14 | 7 | T6 figure inventory 전체 | MUST_FIX 전부 반영, NOT_IN_SOURCE 문장 삭제/라벨링 |
| Crucible Report v1 | 9 | 8 | 6 | 없음 | Grade A 전부 반영, Grade B는 길이 증가 없는 범위에서 압축 반영, Grade C 거부 |
| Draft v0 원문 | — | — | — | — | §1→§2→§5→§7→§8 구조 유지, 중복·과장·외부 규제문 제거 |

### 0.2 Audit v1 상세 판정

| Source | Item (brief description) | Verdict | Rationale |
|---|---|---|---|
| Audit T1 | Master allometric equation `Y = a·BW^b` | ADOPT | G&W Eq.2:374와 R&T Eq.22-2에 부합하므로 C1 핵심 수식으로 유지. |
| Audit T1 | Log transformation `ln(Y)=ln(a)+b·ln(BW)` | ADOPT | G&W Eq.2:379 및 R&T Eq.22-1와 일치하므로 C1에 유지. |
| Audit T1 | `a` drug-dependent, `b` variable type-dependent | PARTIAL_ADOPT | `b`를 완전 drug-independent로 단정하지 않고 “대체로 변수 유형에 의존하나 자료·binding·비선형성에 따라 변동”으로 수정. |
| Audit T1 | Metabolic rate `BW^0.75`와 turnover time `BW^0.25` | ADOPT | G&W Eq.2:375–377의 spine이므로 C1/C3/C4에 유지. |
| Audit T1 | Surface-volume relation and Brody exponent range | ADOPT | 표면적-부피 직관과 Brody 0.5–0.8 범위는 C1/C2 context로 유지하되 과장 없이 압축. |
| Audit T1 | Clearance model `CL_i=a·BW_i^b` | ADOPT | G&W Eq.2:380 및 PK28 Eq.28:1과 일치. |
| Audit T1 | Clearance exponent `b≈0.75`, 실측 범위 | PARTIAL_ADOPT | 기본 prior는 0.75로 유지하되 G&W p.178의 `0.2 to >1` 변동 가능성을 boundary condition에 삽입. |
| Audit T1 | R&T 20-g mouse → 70-kg human 7.7-fold | ADOPT | R&T p.733의 3500 vs 455 예시로 C2의 fold anchor를 수정. |
| Audit T1 | Draft Big Idea의 mouse-human `4.1배` 오류 | ADOPT | `4.1배`는 rat 250 g→human 70 kg에만 적용, mouse 23 g→human 70 kg은 약 7.4배로 교정. |
| Audit T1 | `b=1` 사용 시 “subtherapeutic 시작” 방향성 오류 | ADOPT | target AUC 기반에서는 CL 과대예측이 dose 과대 산출로 이어질 수 있으므로 “subtherapeutic” 단정 삭제. |
| Audit T1 | Volume model `V_i=c·BW_i^d` | ADOPT | G&W Eq.2:382 및 PK28 Eq.28:2와 일치. |
| Audit T1 | Volume exponent `d≈1.0` | ADOPT | G&W Table 2.22의 blood volume, skeletal mass, Vd 지수와 일치. |
| Audit T1 | Half-life scaling `t1/2 ∝ BW^(d-b)` | ADOPT | G&W Eq.2:391–392와 일치하며 C3/C4의 causal bridge로 유지. |
| Audit T1 | Breath/heartbeat time, MLP formula and values | PARTIAL_ADOPT | 핵심 spine은 아니므로 C4 context 1문장으로 압축. |
| Audit T1 | Elementary and Complex Dedrick plot formulas | ADOPT | G&W §2.10.6–2.10.7 및 PK28/PK29의 핵심이므로 C4에 유지. |
| Audit T1 | Kallynochron and Apolysichron definitions | ADOPT | C4와 §5 Pair 2의 핵심 구분으로 유지. |
| Audit T1 | PK28 body weights/doses | ADOPT | mouse 23 g, rat 250 g, man 70 kg; IV bolus 25/500/100,000 µg를 source tag와 함께 유지. |
| Audit T1 | PK28 t1/2 source discrepancy | ADOPT | G&W §2.10.6 = 1.5/2.9/35 h, PK28 case = 1.5/3.9/35 h로 병기. |
| Audit T1 | PK28 `a=0.319`, `AUC=1/a=3.13`, hepatic extraction <10% | ADOPT | PK28 data anchor로 유지. |
| Audit T1 | PK28 model misspecification caution | ADOPT | 단일 dose·단순 모델 제한을 C4 limitation에 명시. |
| Audit T1 | PK29 body weights, doses, weight range | ADOPT | 5종 body weight/dose anchor는 유지하되 `about 3000–3500-fold`로 discrepancy 처리. |
| Audit T1 | PK29 parameter set discrepancy | ADOPT | G&W §2.10.7 set과 PK29 case set을 분리 병기. |
| Audit T1 | Equal unbound AUC and dose translation Eq.2:417–420 | ADOPT | C5의 allometric backbone으로 유지. |
| Audit T1 | C5를 standalone FIH starting dose 식처럼 제시 | ADOPT | C5 제목을 “FIH Dose Translation의 allometric backbone”으로 격하. |
| Audit T1 | `CLu=CL/fu` and species binding correction | ADOPT | C2/C5 boundary condition으로 유지. |
| Audit T1 | Cefazolin fu example | ADOPT | R&T Table 22-1/주변 텍스트의 종간 protein binding boundary 예시로 유지. |
| Audit T1 | Ceftizoxime/fluconazole examples | PARTIAL_ADOPT | central spine이 아니므로 C2/C4 context로만 압축. |
| Audit T1 | Epoetin-β `b=0.775` | PARTIAL_ADOPT | therapeutic protein 예시로만 언급 가능; mAb 일반론으로 확장하지 않음. |
| Audit T1 | “mAb generally b≈0.85” | REJECT | 첨부 PDF 범위에서 직접 근거가 없으므로 main self-test에서 삭제. |
| Audit T1 | Pediatric BSA formula and maintenance dose | ADOPT | R&T Ch.14 Key Relationships 근거로 C5 age/pediatric context에 유지. |
| Audit T1 | Tobramycin child example | REJECT | 본 세션 spine 대비 주변 예시이며 길이 증가를 유발하므로 제외. |
| Audit T1 | CYP3A elderly decline `1%/yr` 단정 | PARTIAL_ADOPT | creatinine clearance heuristic와 CYP3A elderly 60–70% 수준 메시지를 분리해 수정. |
| Audit T1 | Chronologic vs functional age | ADOPT | R&T Ch.14의 핵심 안전장치로 C5/§8에 추가. |
| Audit T1 | NONMEM `$PK` example | PARTIAL_ADOPT | PDF 직접 근거가 아니므로 `[교과서 외 구현 해석]` 라벨을 붙인 §8 실무 번역으로만 유지. |
| Audit T1 | PBPK/QSP implementation | PARTIAL_ADOPT | PBPK는 R&T Ch.22의 context로 high-level 유지, QSP 상세는 후속 의존으로만 유지. |
| Audit T1 | FDA/ICH/NDA/MABEL/Deficiency Letter 표현 | REJECT | 첨부 PDF 직접 근거가 없으므로 본문에서 삭제하고 보류 표에 `[확인 필요]`로만 남김. |
| Audit T2/T5 | G&W Fig.2.145 scalable vs less scalable underused | ADOPT | Figure marker는 넣지 않고 C2 limitation에 “10-fold vs 1000-fold prediction interval” 메시지만 반영. |
| Audit T2/T5 | G&W Fig.2.142/2.143 early decision/data source context | PARTIAL_ADOPT | C1/C5에 1문장 context로 압축. |
| Audit T2/T5 | R&T Ch.14 age/renal maturation underweighted | ADOPT | C5와 §8에 “BW allometry alone is insufficient” 문장 추가. |
| Audit T2/T5 | R&T broad mg/kg or mg/1.73 m² caution | ADOPT | §5 Pair 3와 C5 limitation에 반영. |
| Audit T4 | Microdosing Fig.22-10 | REJECT | 본 세션 core가 아니며 Audit도 reject. |
| Audit T4 | PBPK figures 22-13 onward | REJECT | Scope Lock 범위 밖 또는 후속 세션 범위. |
| Audit T6 | Figure inventory items | 보류/Phase 4C | 사용자 지시상 T6 figure inventory는 4A adjudication 대상이 아니므로 변경 없이 Phase 4C로 이월. |

### 0.3 Crucible v1 상세 판정

| Source | Item (brief description) | Verdict | Rationale |
|---|---|---|---|
| Crucible A1 | `k_el=CL/V`, rate constant scales as `BW^-0.25` | ADOPT | C3와 §5 Pair 1에 causal bridge로 삽입하면 학습 밀도가 올라가며 PDF 수식과 논리적으로 일치. |
| Crucible A2 | Estimated `b>1` as mechanism-first diagnostic | PARTIAL_ADOPT | PDF-supported failure mechanisms과 연결하되 transporter/TMDD는 `[교과서 외 실무 해석]`으로 라벨링. |
| Crucible A3 | ICH M3/FDA standard phrase deletion | ADOPT | Audit NOT_IN_SOURCE와 정합. |
| Crucible A4 | “Allometric Slope Drift” signature | PARTIAL_ADOPT | NONMEM 직접 근거가 아니므로 §8에 `[교과서 외 구현 해석]`으로 축소 삽입. |
| Crucible A5 | Two-point regression insufficiency | ADOPT | G&W p.178의 species number/data quality caution과 정합하여 Q8에 반영. |
| Crucible A6 | Elementary vs Complex Dedrick diagnostic using V slope | ADOPT | PK29의 d>1 사례와 직접 연결되므로 C4 boundary에 삽입. |
| Crucible A7 | Delete over-stretched analogies | ADOPT | 도시 인프라, Big-O 비유 삭제. |
| Crucible A8 | Correct 1%/yr and ICH phrases | ADOPT | Audit와 동일한 MUST_FIX. |
| Crucible B1 | Dedrick = Buckingham Pi | PARTIAL_ADOPT | PDF에는 직접 나오지 않으므로 `[교과서 외 수학적 해석]`으로 1문장 삽입. |
| Crucible B2 | 5 cards as one system | ADOPT | §8 positioning을 단순 목록에서 통합 workflow로 압축 전환. |
| Crucible B3 | TMDD/transporter substrate caution | PARTIAL_ADOPT | PDF failure logic과 부합하나 TMDD 상세는 외부 해석으로 라벨링. |
| Crucible B4 | fu measurement condition matching | PARTIAL_ADOPT | PDF 직접 문장은 아니므로 C2 trench에 `[교과서 외 실무 해석]`으로 유지. |
| Crucible B5 | PK28 source discrepancy citation rule | ADOPT | Audit source discrepancy와 정합. |
| Crucible B6 | Compress body water enumeration | ADOPT | C3에서 1문장으로 압축. |
| Crucible B7 | Compress Professional Moat | ADOPT | §8 C를 motivational tone에서 diagnostic tone으로 축소. |
| Crucible C1 | PBPK build flowchart | REJECT | Session 16 범위. |
| Crucible C2 | Additional ICH section numbers | REJECT | source fabrication 위험. |
| Crucible C3 | QSP target turnover detailed derivation | REJECT | 본 세션 scope 밖. |
| Crucible C4 | Microdosing approach | REJECT | Audit OMITTED_JUSTIFIABLE과 정합. |
| Crucible C5 | Tip #5 in §2 C2 | REJECT | Tip #1과 중복; §8 B에만 짧게 반영. |
| Crucible C6 | Detailed pediatric ontogeny curves | REJECT | Session 15 scope; C5에 안전장치만 유지. |
| Crucible D1 | Delete “도시 인프라 스케일링” analogy | ADOPT | cognitive bridge 약함. |
| Crucible D2 | Delete “Allen’s Big-O” analogy | ADOPT | pharmacometrics reader에게 효용 낮음. |
| Crucible D3 | Compress TBW/neonate enumeration | ADOPT | C3에서 `체수·근육량·혈액량` 1문장으로 압축. |
| Crucible D4 | Compress Q5 arithmetic | ADOPT | §7 계산 과정은 핵심 논리 중심으로 단축. |
| Crucible D5 | Compress §8 Professional Moat | ADOPT | 진단 능력 중심으로 재작성. |
| Crucible D6 | Modify CYP3A 1%/yr statement | ADOPT | creatinine clearance heuristic와 CYP3A elderly observation 분리. |
| Crucible D7 | Modify FDA/EMA/ICH phrase | ADOPT | 조항 번호 없는 physiological rationale + sensitivity language로 수정. |

### 0.4 `[확인 필요]`/NOT_IN_SOURCE 보류 항목

| 항목 | 처리 |
|---|---|
| “ICH M3(R2) 또는 ICH S6가 b=0.75를 명시 권장한다” | 본문에서 삭제. 규제 문서 원문 검증 전까지 `[확인 필요]`. |
| “FDA Clinical Pharmacology reviewer Deficiency Letter” 문구 | 본문에서 삭제. 교육용 가상 시나리오로도 쓰지 않음. |
| “MABEL이 이 PDF 범위에서 직접 설명된다” | 본문에서 삭제. 후속 FIH/MABEL 세션으로 이월. |
| “mAb 일반 b≈0.85” | 본문에서 삭제. PDF 내 epoetin-β는 therapeutic protein 예시일 뿐 mAb 일반론 근거 아님. |
| NONMEM `$PK` 구현 예시 | `[교과서 외 구현 해석]`으로만 §8에 제한 유지. |

---

## ⚑ Updated Curation Map

### MUST 항목 (§2 Concept Anatomy Card 5개)

| # | 개념 | 분류 사유 |
|---|---|---|
| **C1** | Master Allometric Equation: $Y = a \cdot BW^b$ | 종간 외삽의 공통 수학 골격. log-log 직선화, `a`/`b` 해석, scale dependence를 연결한다. |
| **C2** | **[Apex] Clearance Exponent $b \approx 0.75$** | human CL과 dose translation의 가장 큰 leverage. `b=1` linear per-kg 오류가 mouse-human에서 약 7.4–7.7배, rat-human에서 약 4.1배 차이로 증폭된다. |
| **C3** | Volume Exponent $d \approx 1.0$ | V는 공간(extent), CL은 흐름(rate)이라는 비대칭을 만든다. $d-b$가 반감기와 rate constant의 종간 시간 지수다. |
| **C4** | Dedrick Superposition: Elementary + Complex | $C/(Dose/BW^d)$ 및 $t/BW^{d-b}$ 변환으로 종간 곡선을 하나의 생리학적 시간축에 중첩한다. PK28/PK29의 실측 anchor가 있다. |
| **C5** | Equal-unbound-AUC Dose Translation의 allometric backbone | G&W Eq.2:417–421의 allometric dose backbone. 실제 FIH starting dose 전체가 아니라 exposure translation의 수학적 구성요소다. |

### CONTEXT 항목 (1–2문장 처리)

| 항목 | 배치 | 처리 원칙 |
|---|---|---|
| Half-life scales as $BW^{d-b}\approx BW^{0.25}$ | C3/C4 | 핵심 causal bridge로 유지. |
| $k_{el}=CL/V \propto BW^{b-d}\approx BW^{-0.25}$ | C3/§5 | Crucible Grade A로 추가. |
| Brody exponent 0.5–0.8; real CL exponent 0.2 to >1 | C2 | boundary condition으로 유지. |
| MLP, breath time, heartbeat time | C4 | physiological time context 1문장. |
| BSA scaling | C5/§5 Pair 3 | R&T Eq.14-2와 broad-use caution을 함께 제시. |
| Protein binding, metabolism, polymorphism, enterohepatic, nonlinear PK | C2/C5 | allometry failure triggers로 유지. |
| Pediatric/elderly age adjustment | C5/§8 | BW scaling alone insufficient 메시지로 제한. |
| NONMEM/PopPK implementation | §8 | `[교과서 외 구현 해석]`으로만 유지. |
| ICH/FDA/MABEL/NDA phrasing | 보류 표 | 본문에서 삭제. |

---

## §1 — Session Header & Roadmap

**Source:** Gabrielsson & Weiner 5e §2.10 (p.170–191), Case Study PK28 (p.611–614), Case Study PK29 (p.615–620); Rowland & Tozer 5e Ch.14 (p.411–441), Ch.22 allometry section (p.731–743).

### Big Idea

<!-- MASTER LENS -->
$Y=a\cdot BW^b$는 단순 회귀식이 아니라, 종간 체중 차이를 **parameter scale**로 번역하는 거듭제곱 언어다. 핵심 오류는 `b=0.75`와 `b=1.0`의 차이를 작게 보는 것이다. R&T의 20-g mouse→70-kg human 예시에서는 같은 값 1이 `b=1`이면 3500, `b=0.75`이면 455가 되어 7.7배 차이가 난다 [R&T p.733]. G&W PK28의 23-g mouse→70-kg human에서는 약 7.4배, rat 250-g→human 70-kg에서는 약 4.1배 차이다. 이 차이는 “용량을 낮게 시작한다/높게 시작한다”의 단순 구호가 아니라, **target AUC 기반에서는 CL 과대예측이 dose 과대 산출로 이어질 수 있다**는 dose/AUC 방향성 문제다.

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

**선행 전제:** CL, V, AUC, half-life의 정의; one-compartment exponential decay; plasma protein binding과 unbound clearance 개념.  
**직접 후속:** pediatric/elderly dose adjustment, PopPK weight covariate choice, PBPK organ blood flow/volume scaling, FIH exposure translation table.  
**주의:** NONMEM control stream, ICH/FDA/MABEL language, QSP implementation은 본 PDF가 직접 다루는 내용이 아니므로 본문에서는 `[교과서 외 구현/실무 해석]`으로만 다룬다.

<!-- RECAP -->
**§1 요약:** 이 세션의 spine은 `Y=a·BW^b → CL b≈0.75 → V d≈1 → time d-b≈0.25 → Dedrick → equal-AUCu dose backbone`이다. Draft v0의 가장 큰 교정은 `4.1/7.4/7.7` fold 기준을 분리하고, FIH dose formula를 standalone starting-dose rule이 아닌 allometric exposure backbone으로 낮추는 것이다.

---

## §2 — Concept Anatomy Cards

---

### ━━ C1. Master Allometric Equation: $Y=a\cdot BW^b$ ━━

<!-- MASTER LENS -->
**개념 Big Idea:** 알로메트리는 “큰 동물은 단순히 작은 동물의 확대판인가?”라는 질문에 대한 정량적 답이다. `a`는 화합물·변수의 절편, `b`는 체중이 바뀔 때 해당 변수의 변화율을 결정하는 지수다.

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

---

### ━━ C2. [Apex] Clearance Exponent $b\approx0.75$ ━━

<!-- MASTER LENS -->
**개념 Big Idea:** Clearance는 “공간의 크기”가 아니라 **단위 시간당 처리 흐름**이다. 그래서 V처럼 BW¹로 증가하지 않고, 대사율·혈류·GFR과 같은 functional variable처럼 대략 $BW^{0.75}$로 증가한다 [G&W Table 2.22, p.180; R&T Fig.22-1, p.732].

#### A. Formal Definition

$$CL_i=a\cdot BW_i^b \quad [G\&W\ Eq.2:380,\ p.176;\ PK28\ Eq.28:1,\ p.611]$$

G&W는 CL/metabolic rate의 대표 exponent를 0.75로 제시하지만, 실제 CL exponent는 약 0.2에서 >1까지 변할 수 있다고 경고한다 [G&W p.178]. Fig.2.159는 91개 화합물의 CL exponent 분포가 주로 0.5–1.0 범위에 놓임을 보여준다 [G&W p.191].

#### B. Plausible Fallacy — `b=1` linear per-kg scaling

**오류:** “mg/kg 처방에 익숙하니 clearance도 kg에 선형 비례한다.”  
**교정:** CL은 rate/flow variable이므로 `b≈0.75`가 physiological prior다.

- **R&T 20-g mouse→70-kg human:** `b=1`이면 3500, `b=0.75`이면 455 → 7.7배 차이 [R&T p.733].
- **G&W PK28 23-g mouse→70-kg human:** $(70/0.023)^{0.25}\approx7.4$배 차이.
- **Rat 250-g→70-kg human:** $(70/0.25)^{0.25}\approx4.1$배 차이.

Target AUC dose 계산에서는 CL 과대예측이 목표 AUC를 맞추기 위한 dose 과대 산출로 이어질 수 있다. 따라서 Draft v0의 “CL 과대평가 → subtherapeutic 시작” 단정은 삭제한다.

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
학생은 “half-life는 BW^0.25”를 외우지만, 더 중요한 것은 **모든 first-order rate constant가 큰 동물에서 더 작아진다**는 사실이다. 즉 큰 동물은 절대 CL은 크지만, 단위 시간당 제거되는 fraction은 작다.

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

---

### ━━ C4. Dedrick Superposition: Elementary + Complex ━━

<!-- MASTER LENS -->
**개념 Big Idea:** Dedrick plot은 종간 PK curve를 “같은 과정의 다른 시간 척도”로 접어 넣는 변환이다. 시간축만 조정하는 것이 아니라, dose-normalized concentration 축도 BW exponent에 맞게 조정한다.

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

---

### ━━ C5. FIH Dose Translation의 Allometric Backbone ━━

<!-- MASTER LENS -->
**개념 Big Idea:** C5는 FIH starting dose 전체를 결정하는 단독 공식이 아니다. G&W Eq.2:417–421은 **equal unbound AUC를 유지하기 위한 total dose scaling backbone**이다. 실제 FIH starting dose는 이 backbone에 safety margin, toxicology, pharmacology, exposure-response, route, formulation, PD metric을 더해 결정한다.

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

Draft v0의 “CYP3A4 metabolism이 60세 이상 매년 1% 감소”는 과단정이다. R&T는 creatinine clearance가 adulthood에서 대략 1%/yr 감소한다는 rule of thumb을 제시하고 [R&T p.422], CYP3A substrates에서는 elderly group이 young adult보다 낮은 clearance를 보이며 그 연령 차이를 해석할 때 1%/yr creatinine clearance heuristic이 관련된다고 설명한다 [R&T p.424]. 따라서 최종 문장은 다음처럼 제한한다: **노인에서는 renal/hepatic function과 biological age를 별도로 보아야 하며, CYP3A clearance도 young adult 대비 감소할 수 있지만 단순 선형 시간 함수로 쓰지 않는다.**

<!-- RECAP -->
**C5 핵심:** C5의 수식은 equal unbound AUC를 맞추는 allometric backbone이다. FIH dose justification이나 pediatric/elderly dosing에서는 이 backbone 위에 functional age, renal/hepatic function, body composition, binding, PD metric, safety margin을 얹어야 한다.

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

---

## §8 — Meta-Frame & Big Picture

### A. Positioning — 이 세션이 시스템으로 작동하는 세 순간

1. **Animal-to-human exposure translation table:** C1이 table equation, C2가 CL column, C3가 V/time column, C4가 curve-superposition check, C5가 equal-AUCu dose backbone이다.
2. **PopPK weight covariate decision:** `[교과서 외 구현 해석]` WT exponent를 fix할지 estimate할지 결정할 때 C2의 physiological prior와 C3의 V exponent가 동시에 필요하다.
3. **PBPK parameter scaling:** R&T Ch.22는 allometry를 human kinetics prediction의 한 축으로 다룬다. Organ blood flow는 rate-like, organ volume은 extent-like로 구분해 scale해야 한다 [R&T p.731–743].

### B. Failure Modes if this section is weak

**Failure Mode 1 — Allometric Slope Drift.**  
`[교과서 외 구현 해석]` 성인 60–90 kg처럼 WT range가 좁은 데이터에서 CL exponent를 자유 추정하면 SE가 커지고 점추정값이 흔들린다. 이 경우 $b=0.75$ fixed model과 sensitivity analysis가 더 방어 가능하다.

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
**§8 최종 요약:** Session 14의 핵심은 `0.75를 외우는 것`이 아니다. `어떤 변수가 왜 0.75이고, 어떤 변수는 왜 1이며, 그 차이가 시간과 dose를 어떻게 바꾸는지`를 보는 것이다. Content Lock v1은 Draft v0의 강한 spine을 유지하되, fold 오류, FIH overclaim, source-internal discrepancy, unsupported regulatory language를 제거했다.

---

## End of Content Lock v1

**Phase 4C 이월:** Audit T6 Figure Inventory는 본 문서에서 adjudication하지 않았으며, 사용자 지시에 따라 figure/pointer/redraw 판단으로 그대로 이월한다.  
**Length control:** Draft v0의 주요 구조를 유지하되 §2 over-explanation, §7 산수 과정, §8 motivational prose, unsupported regulatory language를 압축·삭제했다.

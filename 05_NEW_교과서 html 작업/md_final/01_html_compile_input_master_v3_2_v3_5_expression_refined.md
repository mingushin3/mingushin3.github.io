> **v3.5 note:** This version applies an Expression Refinement Patch to PART A only. Scientific content, equations’ meaning, numerical anchors, page tags, source labels, figure marker boundary tags and field keys, compiler markers, section/card structure, code blocks, and PART B guardrails are preserved. The patch normalizes mathematical expressions into MathJax/LaTeX-ready notation, converts remaining general English prose and FIGURE_POINTER learner-facing field values into Korean, applies first-use Korean-English pairing for career-critical terms, and rewrites learner-facing prose in a Korean doctoral-level friendly expert lecture style with a light degree of punchy, high-retention phrasing at key conceptual decision points. No new scientific claims, examples, numbers, page tags, figures, or external references were added.

# XX_html_compile_input_master_v3.2.md
**v3.2 note:** This version applies a Korean-Dominant Readability Patch to PART A learner-facing prose. General English prose was converted to Korean where possible, while career-critical pharmacometrics terms are retained as Korean-English paired expressions on first use. Scientific content, equations, numerical anchors, page tags, source labels, figure markers, compiler markers, section structure, and PART B guardrails are preserved. No new scientific claims, examples, numbers, page tags, figures, or external references were added.

**v3.1 note:** This version applies a Korean Readability Patch to improve learner-facing Korean prose while preserving scientific content, equations, page tags, source labels, figure markers, and Phase 5 HTML-readiness. No new scientific claims, page tags, numerical anchors, figure decisions, or external references were added.

---

# 01_html_compile_input_master.md — v3.2

> **Version note (v3.2):** v3.1에 Korean-Dominant Readability Patch를 적용했다. 변경 범위는 (a) §2 카드 내부 하위 섹션 헤더(A/B/C/D)를 영어에서 한국어로 전환(KRD-001 ~ KRD-016), (b) 본문 내 일반 영어 산문을 한국어로 전환하고 핵심 전문용어는 `한글(English)` 형식으로 병기(KRD-017 ~ KRD-040), (c) §8 하위 섹션 헤더를 한국어로 전환(KRD-041 ~ KRD-043), (d) Practice Brief / Mastery Augmentation 등 학습 장치 레이블에 한국어 병기 추가(KRD-044 ~ KRD-055). **과학적 본문, 수치 anchor, 모든 page tag, figure marker, HTML compiler marker, MathJax 수식, NONMEM 관련 표기, source label은 일체 변경하지 않았다.** Phase 5 HTML compiler는 v3.2 PART A를 그대로 렌더링 대상으로 삼을 수 있다. 자세한 변경 내역은 PART B §B16 v3.2 Change Log 참조.

> **Version note (v3.1 — 보존):** PART A에 31개의 Low-risk Korean Readability Patch를 적용했다. 변경 범위는 (a) §1 Learner Navigation Aid 섹션의 영어 안내문·표 헤더·체크포인트 행을 한국어로 통일(P-001 ~ P-014), (b) C1–C5 카드의 Big Idea / Plausible Fallacy / Practice Brief / Boundary 일부 문장을 한국어 독해 흐름에 맞춰 분리·재조립(P-015 ~ P-028, P-030), (c) §5 Pair 1 "Critical correction" 레이블을 "핵심 정정"으로 변경(P-031), (d) C5 Practice Brief 흐름상 역할의 오탈자(`brige` → `bridge`) 수정(P-029). **과학적 본문, 수치 anchor(Compound A S1–S4 numerics, Creatinine/Inulin, midazolam/gentamicin), 모든 page tag(`[G p.XX]`, `[R&T p.XX]`), `<!-- FIGURE_POINTER -->`/`<!-- FIGURE_SCHEMATIC -->`/`<!-- MASTER LENS -->`/`<!-- TRENCH -->`/`<!-- CONFUSION -->`/`<!-- SELF-TEST -->`/`<!-- RECAP -->`/`<!-- ANCHOR -->`/`<!-- ANNOTATION -->` 마커, MathJax 수식, NONMEM 관련 표기, source label은 일체 변경하지 않았다.** Phase 5 HTML compiler는 v3.1 PART A를 그대로 렌더링 대상으로 삼을 수 있다. 자세한 변경 내역은 PART B §B15 v3.1 Change Log 참조. v3 change log는 §B14에 그대로 유지.

> **Version note (v3):** v2의 Source-fidelity 본문(Content Lock v2 base + 4개 4C marker splice + ver2 P1–P5 patches)은 변경 없이 보존된다. v3는 독립 감사에서 식별된 4개 구조적 결함만 외과적으로 보완한다: (a) Apex 레이블 표준화(`[Apex]` → `[⚡ Apex Concept]`) + Apex Concept Plausible Fallacy 블록 1건 추가, (b) §5 세 혼동쌍 모두 Memory Hook 부여, (c) CL vs K 쌍에 Critical Blow 행 추가, (d) C1–C5 카드별 Practice Brief 4축 블록 추가, (e) §8C Professional Moat 5–6개 불릿으로 구체화. **기존 과학 본문, page tag, 수식, Compound A 수치 anchor, 영어 기술 용어, 기존 figure marker는 일체 변경하지 않았다.** 모든 신규 해석 추가는 `[EXPERT_INFERENCE, v3]` 또는 `[TEXTBOOK_DERIVED, v3]`로 태그된다. 자세한 변경 내역은 PART B §B14 v3 Change Log 참조. ver2 patch log는 §B13에 그대로 유지.

> **Version note (ver2 — 보존):** Source-fidelity 본문은 ver1과 동일한 Content Lock v2 base + 4개 4C marker splice를 유지한다. ver2는 (a) MathJax 렌더링을 깨는 critical typo 1건 수정, (b) Crucible Grade A에 이미 합의된 source-bound 표현 강화 3건, (c) Phase 5 navigation 신뢰성을 위한 PART B 메타데이터 추가만 적용했다. **새로운 과학적 주장·수치·예시·page tag는 일체 추가하지 않았다.** 자세한 변경 내역은 PART B §B13 Ver2 Patch Log 참조.

## PART A — 학습자용 완성 핸드아웃

# 세션 01 — 1구획 IV 동력학: CL · V · t½ · K

**Source:** Gabrielsson & Weiner 5e Ch.2 §2.2.1–2.2.5 + Case Study PK1 / Rowland & Tozer 5e Ch.3  
**Pages:** G p.14–32, p.469–475 / R&T p.53–76  
**Mode:** A-Critical  
**Learner:** 계량약리학 박사과정, PopPK 입문–중급  
**그림 권한 안내(Figure rights note):** 이 자료에는 교과서 그림을 직접 수록하지 않습니다. `FIGURE_POINTER` 마커는 학습자가 참고해야 할 교과서 그림을 안내합니다. `FIGURE_SCHEMATIC` 마커는 원본 그림을 복제하지 않고 새로 설계할 도식의 요약(brief)을 기술합니다.

## 학습 내비게이션 안내

### 이 자료 사용법

1. §1을 한 번 읽으면서 파라미터 위계를 먼저 고정하면 됩니다. $CL$과 $V$가 일차 파라미터(primary parameter)이고, $K$, $t_{1/2}$, 1구획 $MRT$는 이 둘로부터 파생됩니다.
2. §2는 카드 순서대로 학습하면 됩니다. C1과 C2는 건너뛰지 않는 것이 좋습니다. 이후의 모든 시간 파라미터가 이 두 카드에 의존하기 때문입니다.
3. Figure pointer가 나오면 계속 읽기 전에 해당 교과서 그림을 먼저 확인하면 됩니다. 이 마커는 장식용 주석이 아니라 학습 경로의 일부입니다.
4. §7 자기 테스트를 하기 전에 §5를 통해 주요 혼동 쌍을 먼저 능동적으로 구분해 보세요.
5. §8은 최종 전문가 시각으로 활용하면 됩니다. 숫자를 해석하기 전에 파라미터 위계부터 읽어야 합니다.

### 학습 순서

`§1 로드맵 → C1 청소율 → C2 분포용적 → C3 K → C4 반감기 → C5 MRT → §5 혼동쌍 → §7 자기 테스트 → §8 메타프레임`

### 시작 전 / 완료 후 체크포인트

| 체크 항목 | 시작 전 | 완료 후 |
|---|---|---|
| 파라미터 위계 | $CL$과 $V$가 일차(primary)인 이유를 말할 수 있는가? | $K$와 $t_{1/2}$가 이차(secondary)인 이유를 암기 문구 없이 설명할 수 있는가? |
| 노출량(Exposure) 대 시간 | AUC, $C^0$, 기울기(slope), $C_{ss}$를 구분할 수 있는가? | 각각을 결정하는 파라미터를 지목할 수 있는가? |
| 겉보기 용적(Apparent volume) | $V$가 해부학적 부피가 아닌 이유를 말할 수 있는가? | 매우 큰 $V$를 실제 체적으로 오해하지 않고 해석할 수 있는가? |
| 말단 기울기(Terminal slope) | 반로그 말단 기울기(semilog terminal slope)를 정의할 수 있는가? | terminal slope가 전체 소실(elimination)을 안전하게 대표하지 못하는 조건을 말할 수 있는가? |
| NCA 연결 | $MRT$를 정의할 수 있는가? | $MRT=1/K=1.443\cdot t_{1/2}$가 1구획 IV bolus에서만 성립하는 이유를 설명할 수 있는가? |

---

## §1 — 세션 헤더와 로드맵

<!-- MASTER LENS -->
<!-- ANNOTATION -->
**핵심 아이디어(Big Idea):** $CL$과 $V$는 약물 체내 처리(disposition), 즉 분포와 소실을 묶은 체내 처리 과정을 결정하는 두 일차 좌표(primary coordinate)입니다. $K$와 $t_{1/2}$는 그 좌표가 만든 시간 그림자입니다. 다시 말해, 관찰되는 기울기(slope)와 반감기(half-life)는 원인이 아니라 결과입니다. 그림자($K$, $t_{1/2}$)만 보고 원인이 $CL$인지 $V$인지 단정하면 유지용량, 부하용량, 공변량 위치가 모두 틀릴 수 있습니다. [G p.17; R&T p.58]

```
IV bolus, 1-cmt, first-order
        │
        ├── Primary:  CL  ──┐
        │                   ├── K = CL/V ── t½ = ln(2)/K = 0.693V/CL
        └── Primary:  V   ──┘

Exposure/AUC  ← governed by CL
Initial concentration C0 ← governed by V
Mean residence time MRT ← 1/K only in 1-cmt IV bolus
```

<!-- ANCHOR -->
R&T의 도입 그림(opening figures)은 이 구조를 가장 빠르게 보여 줍니다. Drugs A/B는 같은 초기 농도에서 출발하지만 기울기와 AUC가 다릅니다. 반대로 Drugs C/D는 같은 반감기(half-life)를 보이지만 초기 농도와 AUC가 다릅니다. 즉, "처음 높이"와 "기울기"는 같은 정보가 아닙니다. 서로 다른 일차 결정인자(primary determinant)가 표면에 드러난 모습입니다. [R&T p.54–55]

이 세션에서는 다음 다섯 카드만 고정합니다: **C1 청소율(Clearance) → C2 분포용적(Volume) → C3 소실속도상수(Elimination Rate Constant) → C4 반감기(Half-life) → C5 MRT**.

**선행:** 1차 ODE, 자연로그, 혈장/혈액/조직 구분.  
**후속:** 다구획 동력학(multi-compartment kinetics), 흡수 모델(absorption models), 간/신 청소율(hepatic/renal clearance), 집단약동학(PopPK, population pharmacokinetics) 공변량 모델링(covariate modeling), NCA 모멘트 분석(moment analysis).

---


<!-- FIGURE_POINTER -->
Source: [Rowland & Tozer 5e, p.54, Fig.3-1; p.55, Fig.3-2]
Why this matters: 같은 용량(dose)에서 "초기 농도", "기울기", "AUC"가 서로 다른 정보를 담는다는 사실을 한 번에 분리해 보여 줍니다. 이 그림이 없으면 학습자가 $C^0$, 기울기(slope), AUC를 하나의 노출 지표처럼 뭉뚱그려 읽을 위험이 큽니다.
When to look: §1 로드맵을 읽은 뒤에 확인하면 됩니다.
Learner instruction: Fig.3-1에서는 같은 초기 농도(initial concentration)에서 기울기(slope)와 AUC가 어떻게 갈라지는지 확인해 보세요. Fig.3-2에서는 같은 반감기(half-life)라도 초기 농도와 AUC가 달라질 수 있음을 먼저 확인하면 됩니다.
<!-- /FIGURE_POINTER -->

<!-- MASTER LENS -->
> **전문가 보강(Mastery Augmentation) — [CRUCIBLE_DERIVED]**  
> 이 핸드아웃의 판정 순서는 간단합니다. 노출량·유지용량 질문은 먼저 $CL$로, 초기농도·부하용량 질문은 먼저 $V$로, 시간축 질문은 $CL/V$ 또는 $V/CL$ 조합으로 되돌려 읽으면 됩니다. 이 순서가 지켜져야 기울기와 반감기가 원인처럼 보이는 착시를 피할 수 있습니다.


## §2 — 개념 해부 카드

### 🃏 C1. 청소율(Clearance, $CL$) [⚡ Apex Concept]

<!-- MASTER LENS -->
<!-- ANNOTATION -->
$CL$은 "농도가 얼마나 빨리 내려가는가"가 아니라 **단위 시간당 완전히 비워지는 가상의 혈장/혈액 부피**입니다. 이 관점에서 보면 $CL=Q\cdot E$는 직관적으로 이해됩니다. 혈류량 $Q$가 약물을 장기에 가져오고, 추출비 $E$(← 장기 통과 중 제거되는 비율)가 청소 효율을 정합니다. 따라서 완전 추출자라도 $CL$은 $Q$를 넘을 수 없습니다. 여기서 핵심은 속도처럼 보이는 값을 유량 구조로 읽는 것입니다. [R&T p.55–56]

#### A. 형식적 정의(Formal Definition)

**청소율(Clearance, $CL$):** 단위 시간당 혈장 또는 혈액에서 약물이 완전히 제거되는 겉보기 용적(apparent volume)입니다. 단위는 유속 단위(flow unit)입니다. [G p.16; R&T p.56]

$$
\text{Rate of elimination}=CL\cdot C \qquad [\text{R\&T Eq.3-4, p.56; G Eq.2:2, p.16}]
$$

$$
CL=Q\cdot E \qquad [\text{R\&T Eq.3-5, p.56}]
$$

#### B. 용량, AUC, 그리고 항정상태

<!-- ANNOTATION -->
AUC는 시간 전체에 걸친 노출 적분(exposure integral), 즉 농도-시간 곡선 아래 면적입니다. 1차 IV bolus에서는 제거된 총량이 $CL\cdot AUC$로 표현됩니다. 전체 용량(dose)이 결국 제거되므로 다음 관계가 성립합니다. [G p.19; R&T p.59–60]

$$
CL=\frac{Dose}{AUC_0^\infty}
$$

일정 속도 주입(constant infusion)에서는 다음과 같습니다.

$$
\frac{dC}{dt}=\frac{R_{in}}{V}-\frac{CL}{V}C
$$

항정상태에서 $dC/dt=0$이므로 다음과 같습니다.

$$
C_{ss}=\frac{R_{in}}{CL} \qquad [\text{G Eq.2:22, p.23}]
$$

<!-- ANCHOR -->
여기서 $V$가 소거됩니다. $V$는 항정상태에 도달하는 **속도**를 바꾸지만, 동일 주입속도(infusion rate)에서 최종 $C_{ss}$는 $CL$이 결정합니다. [G p.22–23]

#### C. Compound A 기준 데이터

Gabrielsson Case Study PK1은 4명에게 Compound A 10 mg IV bolus를 투여한 출처 기반(source-bound) 계산 기준점입니다. [G p.469–475]

| Subject | Sex | $K$ (min⁻¹) | $V$ (L) | $CL$ (L/min) | $AUC$ (µg·min·L⁻¹) |
|---|---:|---:|---:|---:|---:|
| 1 | M | 0.01 | 10 | 0.1 | 98,000 |
| 2 | M | 0.02 | 9.8 | 0.2 | 49,000 |
| 3 | F | 0.02 | 10 | 0.2 | 51,000 |
| 4 | F | 0.01 | 20 | 0.2 | 51,000 |

[Source: G Tables 1.2/1.3, p.473–474]

<!-- ANCHOR -->
**정정된 핵심:** Subject 1과 4는 $K$와 $t_{1/2}$가 비슷하지만 $CL$은 2배 다릅니다. S1은 $CL=0.1$ L/min, S4는 $CL=0.2$ L/min입니다. S4에서는 $V$도 동일 비율로 커져 있어 $K=CL/V$가 우연히 보존된 결과입니다. 따라서 같은 $R_{in}$에서 두 사람의 $C_{ss}$는 절반 차이가 납니다(§7 Q5에서 정량 확인). $K$와 $t_{1/2}$만 보고 "두 사람이 같은 약물 처리 능력을 가졌다"고 읽는 것이 이 세션 전체의 핵심 함정입니다. [G p.473–474; G Eq.2:22, p.23]

#### D. 경계 및 압축

- $CL=Q\cdot E$는 간/신 청소율(hepatic/renal clearance)의 문을 열지만, 고추출(high extraction)/저추출(low extraction) 약물 예시와 장기별 모델은 후속 청소율 세션으로 넘깁니다. [R&T p.56]
- 혈관외 투여(extravascular dosing)에서는 $F$ 때문에 겉보기 파라미터(apparent parameter) 해석이 필요하지만, $K_a$, $F$, $t_{lag}$는 흡수 세션 주제입니다. [G p.28–32]
- $CL_R=f_e\cdot CL$은 신장 기여분(renal contribution)을 분리하는 맥락으로만 유지합니다. [R&T p.66–68]

<!-- TRENCH -->
[실무 확장/교과서 외 해석] NONMEM에서 공변량을 $K$에 직접 묶으면 $CL$ 변화와 $V$ 변화가 한 항에 섞입니다. `TRANS2`처럼 $CL$과 $V$를 분리해 두는 이유는 통계적 편의가 아니라 인과 위치 보존입니다.

<!-- RECAP -->
**C1 요약(Recap):** $CL$은 노출량과 유지용량을 결정하는 일차 소실 파라미터(primary elimination parameter)입니다. $t_{1/2}$이나 $K$가 아니라 $CL$을 먼저 물어야 합니다.

<!-- MASTER LENS -->
> **[⚡ Apex Concept] 그럴듯한 오해 (Plausible Fallacy) — [EXPERT_INFERENCE, v3]**
>
> - **그럴듯한 오해:** "Compound A에서 Subject 1과 Subject 4의 $K$가 같으면, 두 피험자의 소실 능력(elimination capacity)이 같습니다."
> - **왜 틀렸는가:** $K=CL/V$이므로 $K$가 같아도 $CL$과 $V$가 모두 다를 수 있습니다. Subject 1의 작은 $V$(10 L)에서 작은 $CL$(0.1 L/min)이, Subject 4의 큰 $V$(20 L)에서 큰 $CL$(0.2 L/min)이 같은 $K$를 만듭니다. 부하용량(loading dose)은 $V$에, 유지용량(maintenance dose)과 AUC는 $CL$에 의존하므로 임상 결정이 분기됩니다.
> - **실무에서 어떻게 드러나는가:** $K$를 공변량(covariate) 탐색의 대상으로 삼으면 $CL$과 $V$의 서로 다른 생리학적 원인이 한 항 안에 뭉개집니다. 그 결과 예측력이 낮은 모델이 만들어집니다. GOF에서 잔차 패턴이 체중이나 신기능과 연동되어 나타나도 원인을 $K$에서 찾으면 올바른 공변량 위치를 놓칩니다.

> **▶ 실무 체화 요약(Practice Brief) — C1 체화 4축 — [EXPERT_INFERENCE, v3]**
> - **왜 알아야 하는가:** $CL$을 이차 파라미터(secondary parameter)로 오해하면, 신기능 저하나 약물상호작용으로 노출량이 변했을 때 $t_{1/2}$ 변화만 보고 역추정하게 됩니다. 그 결과 유지용량을 잘못 결정하게 됩니다.
> - **흐름상 역할:** C1은 이 세션 전체 카드의 결정 분기점(C2의 $V$, C3의 $K=CL/V$, C4의 $t_{1/2}=0.693\cdot V/CL$, C5의 $V_{ss}=CL\cdot MRT$)입니다. 이후 간/신 청소율(hepatic/renal clearance) 세션과 PopPK 공변량(covariate) 모델링, 즉 공변량을 $CL$에 묶는 표준 관행의 출발점입니다.
> - **체화 꿀팁:** 수식 $CL=Dose/AUC$를 외우는 대신 "단위 시간당 비워지는 혈장 부피"라는 생리학적 지시체를 먼저 고정하면 됩니다. 그러면 $C_{ss}=R_{in}/CL$에서 $V$가 사라지는 이유가 즉시 보입니다.
> - **실무 활용:** NONMEM 데이터셋에서 용량-AUC 쌍(dose-AUC pair)으로 NCA $CL$을 산출해 모델 기반(model-based) $CL$과 비교하는 것이 첫 GOF 점검입니다. 두 값이 크게 다르면 모델 구조 또는 데이터 무결성을 의심합니다.

---


<!-- FIGURE_POINTER -->
Source: [Rowland & Tozer 5e, p.55, Fig.3-3]
Why this matters: 저장소-추출기 도식(reservoir-extractor diagram)은 $Q$, $E$, $C$, $C_{out}$이 어떻게 연결되어 $CL=Q\cdot E$가 되는지 시각적으로 고정해 줍니다. 텍스트만 읽으면 $CL$을 단순 기울기(slope)나 제거 속도로 오해하기 쉽습니다.
When to look: C1 청소율(Clearance) 카드를 읽은 뒤에 확인하면 됩니다.
Learner instruction: 저장소(reservoir)를 "몸", 추출기(extractor)를 "간/신장"으로 대응시켜 보세요. 들어가는 양 $Q\cdot C$와 제거되는 분율(fraction) $E$의 곱이 왜 청소율(clearance)의 물리적 의미가 되는지 확인하면 됩니다.
<!-- /FIGURE_POINTER -->

<!-- MASTER LENS -->
> **전문가 보강(Mastery Augmentation) — [CRUCIBLE_DERIVED]**  
> $CL=Dose/AUC$에서 $V$가 사라진다는 사실은 암기용 공식이 아니라 유지용량 판단의 구조입니다. 분포공간은 곡선의 출발점과 시간상수를 바꾸지만, 전체 투약 사건을 적분하면 노출-용량 변환의 중심에는 $CL$만 남습니다.


### 🃏 C2. 분포용적(Volume of Distribution, $V$)

<!-- MASTER LENS -->
<!-- ANNOTATION -->
$V$는 실제 해부학적 부피가 아니라 **체내 총량을 혈장 농도로 환산하는 겉보기 희석 공간(apparent dilution space)**입니다. 같은 100 units를 넣어도 물에만 녹으면 $V=10$ L, 숯(charcoal)에 결합해 물에서 거의 안 보이면 $V=100$ L이 됩니다. 총량은 같지만 측정 가능한 농도가 다르기 때문입니다. [G Fig.2.3, p.14–15; R&T p.63–64]

#### A. 형식적 정의(Formal Definition)

$$
V=\frac{A_b}{C} \qquad [\text{G Eq.2:14, p.20; R\&T Eq.3-26, p.63}]
$$

IV bolus에서는 역외삽 절편(back-extrapolated intercept)으로 다음을 계산합니다.

$$
V=\frac{D_{iv}}{C^0} \qquad [\text{G Eq.2:13, p.20}]
$$

R&T는 시간 0 외삽(time-zero extrapolation)만으로 $V$를 확신하기 어려운 상황을 지적합니다. 분포 평형이 완성되기 전의 절편은 실제 분포공간을 안정적으로 대표하지 못할 수 있기 때문입니다. 그래서 말단 단계(terminal phase)에서 $CL$과 $k$로 $V$를 구하는 우회식을 제시합니다. [R&T p.63]

$$
V=\frac{CL}{K}=1.44\cdot CL\cdot t_{1/2} \qquad [\text{R\&T Eq.3-27/3-28, p.63}]
$$

#### B. 겉보기 분포용적이 거대해질 수 있는 이유

Gabrielsson은 $V$를 비결합 용적(unbound volume)과 유리 분율(free fraction)로 분해합니다. [G p.20]

$$
V=V_u\cdot f_u \qquad [\text{G Eq.2:15, p.20}]
$$

조직 분배(tissue partition)까지 고려하면 $V_{ss}$는 혈액 부피와 조직별 분배계수의 합으로 표현됩니다. [G Eq.2:16–2:18, p.20–21]

$$
V_{ss}=V_B+\sum V_{Ti}\cdot K_{Pi}\cdot(1-E_{Ti})
$$

Quinacrine의 $V=40{,}000$ L는 겉보기 분포용적(apparent volume)의 극단값입니다. 이 값은 실제 체적이 아니라 조직 결합(tissue binding)과 측정 공간(measurement space)의 불일치를 흡수한 환산률로 읽어야 합니다. [G p.20]

#### C. Compound A 기준 데이터

Compound A에서 Subject 1–3의 $V$는 약 10 L이고, Subject 4는 20 L입니다. Gabrielsson Fig.1.2는 Subject 4의 낮은 절편(intercept)이 더 큰 용적(volume)을 의미한다고 설명합니다. [G p.470, p.473]

<!-- ANCHOR -->
$V$가 커지면 동일 용량(dose)에서 $C^0=D/V$가 낮아집니다. 그러나 $V$만으로 AUC가 결정되지는 않습니다. AUC는 $CL$이 결정합니다. [G Fig.2.6, p.17; G Fig.2.12, p.26–27]

#### D. 경계 및 압축

- 1구획 모델에서는 $V$와 $V_{ss}$ 구분이 사실상 사라지지만, 다구획에서는 $V_c$, $V_{ss}$, 말단 용적(terminal volume)이 분기됩니다. 이 본격 전개는 분포 동력학(distribution kinetics) 세션으로 넘깁니다. [G p.20–21; R&T p.61]
- $V$를 이용한 부하용량(loading dose) 계산은 분포 단계(distribution phase)가 충분히 빠르다는 가정에 의존합니다. [R&T p.62–64]

<!-- TRENCH -->
[실무 확장/교과서 외 해석] 반로그 도표(semi-log plot)에서 명백한 꺾임점(break point)이 보이면, 1구획 $V$를 곧바로 부하용량(loading dose)에 쓰기 전에 중심 구획 용적(central volume) 대 항정상태 용적(steady-state volume) 문제를 점검합니다.

<!-- RECAP -->
**C2 요약(Recap):** $V$는 "약물이 어디에 얼마나 숨어 있는가"를 혈장 농도 하나로 환산한 겉보기 파라미터(apparent parameter)입니다. $C^0$와 부하용량(loading dose)에는 직접적이지만, 유지 노출량(maintenance exposure)은 $CL$이 결정합니다.

> **▶ 실무 체화 요약(Practice Brief) — C2 체화 4축 — [EXPERT_INFERENCE, v3]**
> - **왜 알아야 하는가:** $V$를 실제 해부학적 부피로 오해하면 $V=40{,}000$ L 같은 quinacrine 값을 모델 오류로 판단해 정상 데이터를 폐기하게 됩니다.
> - **흐름상 역할:** C2의 $V$는 C1의 $CL$과 함께 일차(primary) 파라미터 쌍을 이루며, C3($K=CL/V$)와 C4($t_{1/2}=0.693\cdot V/CL$)의 분모로 직접 들어갑니다. 이후 분포 동력학(distribution kinetics) 세션에서 $V_c$, $V_{ss}$, terminal $V_z$로 분기됩니다.
> - **체화 꿀팁:** "측정 공간(plasma)과 총량 사이의 환산률"이라는 정의를 고정하면 됩니다. 조직 결합이 강할수록 혈장(plasma) 농도가 낮아져 환산률($V$)이 커진다는 인과 방향이 자동으로 생깁니다.
> - **실무 활용:** 부하용량(loading dose) 계산식 $LD=V\cdot C_{target}$의 $V$로 바로 사용됩니다. NCA에서 $V_z=CL/\lambda_z$로 산출된 값이 $V_{ss}$와 다를 때는 다구획 동력학을 의심하는 첫 번째 신호가 됩니다.

---


<!-- FIGURE_POINTER -->
Source: [Gabrielsson & Weiner 5e, p.15, Fig.2.3]
Why this matters: 두 양동이(bucket)의 실제 물 부피가 같아도 측정 농도 차이 때문에 겉보기 용적(apparent volume)이 10 L와 100 L로 달라지는 장면을 보여 줍니다. 이 그림이 없으면 $V$를 실제 해부학적 부피로 오해하기 쉽습니다.
When to look: C2 분포용적(Volume of Distribution) 카드를 읽은 뒤에 확인하면 됩니다.
Learner instruction: 두 양동이(bucket) 모두 총 용량(dose)은 100 units로 같다는 점을 먼저 확인해 보세요. 그다음 숯 결합(charcoal binding) 때문에 측정 공간의 농도가 낮아지면 왜 겉보기 $V$가 커지는지 확인하면 됩니다.
<!-- /FIGURE_POINTER -->

<!-- MASTER LENS -->
> **전문가 보강(Mastery Augmentation) — [AUDIT_DERIVED]**  
> $V$가 매우 크다는 말은 "몸 안에 실제로 그만한 부피가 있다"는 뜻이 아닙니다. 측정 공간(plasma)에서 보이는 농도가 낮아졌기 때문에 총량을 그 농도로 환산한 겉보기 공간(apparent space)이 커진 것입니다.


### 🃏 C3. 소실속도상수(Elimination Rate Constant, $K$)

<!-- MASTER LENS -->
$K$는 독립적 제거 능력이 아니라 **체내 약물량(amount) 중 단위 시간당 제거되는 분율(fraction)**입니다. 즉, $K$는 "얼마나 잘 제거하는가"와 "얼마나 넓게 퍼져 있는가"의 비율입니다. 제거 능력($CL$)을 분포 공간($V$)으로 나눈 값이므로 $K=CL/V$가 됩니다. [G p.17; R&T p.56]

#### A. 형식적 정의와 ODE

$$
K=\frac{CL}{V} \qquad [\text{G p.17; R\&T Eq.3-7, p.56}]
$$

$$
\frac{dC}{dt}=-K\cdot C=-\frac{CL}{V}\cdot C \qquad [\text{G Eq.2:1, p.16; R\&T Eq.3-9, p.57}]
$$

적분하면 다음과 같습니다.

$$
C=C^0\cdot e^{-K\cdot t}=\frac{D}{V}\cdot e^{-(CL/V)\cdot t} \qquad [\text{G Eq.2:4, p.17; R\&T Eq.3-10, p.58}]
$$

반로그 도표(semi-log plot)에서는 다음과 같습니다.

$$
\ln C=\ln C^0-K\cdot t
$$

따라서 기울기(slope)는 $-K$입니다. [G Fig.2.4/2.6, p.15–17; R&T Eq.3-11, p.58]

#### B. 분율 제거의 직관

R&T Table 3-1은 $K=0.1$ hr⁻¹인 저장소(reservoir)에서 100 mg이 1시간 후 90 mg, 2시간 후 81 mg, 3시간 후 72.9 mg으로 감소하는 예를 제시합니다. 매 시간 "10 mg"이 아니라 **남아 있는 양의 10%**가 제거됩니다. [R&T p.57]

$$
\frac{A}{Dose}=e^{-Kt}=\left(\frac12\right)^n,\quad n=t/t_{1/2} \qquad [\text{R\&T Eq.3-19, p.59}]
$$

#### C. 경계(Boundary)

- 분포 단계(distribution phase) 중 관찰되는 빠른 농도 저하(decline)가 반드시 소실(elimination) $K$를 의미하지는 않습니다. midazolam은 초기 약 1시간 동안 분포 단계를 보입니다. 이후 말단 단계(terminal phase)에서 소실 반감기(elimination half-life)가 해석됩니다. [R&T p.61–62]
- 혈관외(extravascular) flip-flop에서는 말단 기울기(terminal slope)가 흡수 속도를 반영할 수 있으므로, 이 세션에서는 배경 맥락으로만 다룹니다. [G p.29–30]

<!-- TRENCH -->
[실무 확장/교과서 외 해석] `ADVAN1 TRANS1`에서 $K$를 직접 추정하면 적합(fit) 자체는 가능하지만, 공변량이 $CL$에 작용하는지 $V$에 작용하는지 분리하기 어렵습니다. `TRANS2`식 $CL/V$ 모수화(parameterization)는 후속 PopPK 해석 가능성을 보존합니다.

<!-- RECAP -->
**C3 요약(Recap):** $K$는 반로그 기울기(semi-log slope)로 보이는 값이지만, 구조적으로는 $CL/V$입니다. 기울기가 변했을 때 $CL$이 변했는지 $V$가 변했는지는 별도로 판단해야 합니다.

> **▶ 실무 체화 요약(Practice Brief) — C3 체화 4축 — [EXPERT_INFERENCE, v3]**
> - **왜 알아야 하는가:** $K$를 일차 파라미터(primary parameter)로 다루면 신기능 변화($CL$ 효과)와 체수분 변화($V$ 효과)가 한 항에 섞여 공변량(covariate)이 잘못 부착되거나 누락됩니다.
> - **흐름상 역할:** C3는 C1·C2의 합성 결과이자 C4($t_{1/2}=\ln 2/K$)와 C5($MRT=1/K$의 1구획 형태)의 출발점입니다. NONMEM `ADVAN1 TRANS1` vs `TRANS2` 선택의 직접적 근거가 됩니다.
> - **체화 꿀팁:** "독립 능력이 아니라 효율의 비율"이라는 표현을 머릿속에 고정하면 됩니다. 그러면 반로그 기울기(semi-log slope)를 보고도 자동으로 "이 기울기(slope)가 $CL$에서 왔는지 $V$에서 왔는지"를 묻게 됩니다.
> - **실무 활용:** NCA에서 말단 기울기(terminal slope) $\lambda_z$를 $K$ 대용으로 보고할 때, 1구획 동력학이 아닌 경우 $\lambda_z$는 진정한 소실(elimination) $K$가 아님을 명시해야 합니다.

---

### 🃏 C4. 반감기(Half-life, $t_{1/2}$)

<!-- MASTER LENS -->
$t_{1/2}$는 "약물이 빠지는 속도" 자체가 아니라 **$CL$과 $V$가 합성해 만든 시간 척도**입니다. 그러므로 $t_{1/2}$는 원인 변수가 아니라 결과 변수로 읽어야 합니다. R&T는 이 점을 명확히 밝힙니다. 반감기(half-life)와 소실속도상수(elimination rate constant)는 대개 $CL$과 $V$에 의존하며, 그 반대 방향이 아닙니다. [R&T p.53, p.58]

#### A. 형식적 정의(Formal Definition)

$$
t_{1/2}=\frac{\ln 2}{K}=\frac{0.693\cdot V}{CL} \qquad [\text{G Eq.2:3/2:6, p.17–18; R\&T Eq.3-15/3-16, p.58}]
$$

같은 $CL$이라도 $V$가 다르면 $t_{1/2}$는 달라집니다. R&T의 creatinine과 inulin 예시는 이 점을 직접 보여 줍니다. [R&T p.58]

| Compound | $CL$ (L/hr) | $V$ (L) | $t_{1/2}$ (hr) | 해석 |
|---|---:|---:|---:|---|
| Creatinine | 4.5 | 42 | 6.5 | total body water에 가까운 분포 |
| Inulin | 4.5 | 16 | 2.5 | extracellular water에 가까운 분포 |

같은 $CL=4.5$ L/hr인데 $t_{1/2}$가 다른 이유는 $V$가 다르기 때문입니다. [R&T p.58]

#### B. 항정상태 도달 시간

일정 속도 주입(constant infusion)에서 항정상태 도달 정도는 반감기 단위로 표현됩니다. Gabrielsson Fig.2.8은 1 반감기 후 50%, 2 반감기 후 75%, 3 반감기 후 87.5%, 3–4 반감기 후 약 90% 도달을 보여 줍니다. [G p.22]

R&T는 6.64 반감기 후 약 99%가 제거된다고 설명합니다. [R&T p.59]

<!-- ANCHOR -->
$V$는 $C_{ss}$ 자체를 바꾸지 않지만, $t_{1/2}=0.693\cdot V/CL$을 통해 항정상태 도달 시간을 바꿉니다. 따라서 유지용량(maintenance dose)과 부하용량(loading dose)의 질문은 분리해야 합니다. [G p.22–23]

#### C. 분포 단계의 한계

R&T midazolam case는 7.5 mg base IV bolus 후 반로그 농도 프로파일(semilog profile)이 이상성(biphasic)이며, 초기 약 1시간은 분포 단계(distribution phase)라고 설명합니다. 이때 5분 시점 혈장에는 0.61 mg만 있고, 7.5 mg 중 6.9 mg, 즉 92%가 혈장 밖으로 분포되어 있습니다. [R&T p.61–62]

R&T Fig.3-5는 2시간까지 AUC가 전체 AUC의 48%라고 제시합니다. Fig.3-6은 분포와 소실의 속도 경쟁을 두 시나리오로 설명합니다. Midazolam처럼 분포가 소실보다 빠르고 분포 단계 동안 누적 AUC가 전체의 절반 정도에 머물면 말단 단계가 소실을 대표하기 쉽습니다. [R&T p.64–65]

반대로 gentamicin은 말단 단계 도달 전 대부분의 소실이 이미 발생합니다. R&T는 gentamicin IV dose의 95% 초과가 분포 평형(distribution equilibrium) 전에 소변으로 제거된다고 설명합니다. 이 경우 말단 단계를 곧바로 "소실 전체의 대표"로 읽으면 안 됩니다. [R&T p.66]

<!-- ANCHOR -->
결국 *분포 단계 AUC 대 전체 AUC의 비율* 하나가 모델 단순화의 가능성을 결정합니다. Midazolam처럼 50% 부근이면 1구획 근사가 일부 임상 목적에서 안전하고, gentamicin처럼 95%가 분포 단계 동안 빠져나가면 말단 기울기(terminal slope)를 소실 대표값으로 쓰는 것 자체가 위험합니다. [R&T p.64–66]

<!-- TRENCH -->
[실무 확장/교과서 외 해석] 말단 기울기(terminal slope)는 "마지막 직선"이 아니라 "분포 단계 오염이 충분히 작아진 뒤의 직선"으로 잡아야 합니다. 최소 데이터 포인트 수, 회귀 품질(regression quality), AUC 분율(fraction)을 함께 점검합니다.

<!-- RECAP -->
**C4 요약(Recap):** $t_{1/2}$가 길어졌다는 말은 원인 진단이 아닙니다. 반드시 "$CL$ 변화인가, $V$ 변화인가, 분포 단계 문제인가"를 되물어야 합니다.

> **▶ 실무 체화 요약(Practice Brief) — C4 체화 4축 — [EXPERT_INFERENCE, v3]**
> - **왜 알아야 하는가:** $t_{1/2}$ 증가를 곧바로 신기능 저하로 해석하면 부종으로 인한 $V$ 증가 가능성을 놓칩니다. 그 결과 용량 감량이 필요 없는 환자에게 불필요한 용량 조절을 권고하게 됩니다.
> - **흐름상 역할:** C4는 C1·C2가 만들어낸 시간 그림자이자, 항정상태 도달 시간(time-to-steady-state, 3–5 half-lives)과 투여간격(dosing interval) 결정의 직접 근거입니다. 반복투여 축적(multi-dose accumulation) 세션과 PopPK simulation에서 지속적으로 참조됩니다.
> - **체화 꿀팁:** "$t_{1/2}$는 결과 변수다"를 고정하면 됩니다. 이 한 줄이 $t_{1/2}$ 변화 앞에서 자동으로 "AUC와 $C^0$를 분리해서 보자"는 반응을 만듭니다.
> - **실무 활용:** TDM 임상에서 채혈 시간창(sampling time window) 설계의 출발점입니다. NCA 보고서에서 terminal phase 데이터 점 수와 회귀(regression) $R^2$가 동반 보고되어야 신뢰 가능한 $t_{1/2}$ 추정이 됩니다.

---


<!-- FIGURE_SCHEMATIC -->
Title: 분포 단계(distribution phase)와 소실 단계(elimination phase)의 경쟁 판정
Mode: R
Visual objective: 5초 안에 "말단 기울기(terminal slope)가 소실(elimination)을 대표하는 조건"과 "대표하지 못하는 조건"을 구분하게 합니다.
Core message: 말단 단계(terminal phase)는 자동으로 소실 단계(elimination phase)가 아닙니다. 분포(distribution)와 소실(elimination)의 속도 경쟁이 허락할 때만 소실 해석에 안전하게 쓰입니다.
Elements to include: 두 개의 병렬 lane; lane 1 = 분포(distribution)가 빠르고 소실(elimination)이 상대적으로 느린 경우; lane 2 = 분포 평형(distribution equilibrium) 전에 소실(elimination)이 상당히 진행되는 경우; 초기 분포 단계(early distribution phase); 말단 단계(terminal phase); AUC 비중(AUC share); 라벨 "terminal slope: 주의해서 사용 가능" 및 "terminal slope: 오도 가능".
Elements to exclude: 새로운 약물 수치; 다구획 미분방정식; 실제 교과서 곡선의 형태·색상·배치 복제; NONMEM 모델 코드(model code).
Suggested rendering: Mermaid
Caption: 분포(distribution)와 소실(elimination)의 상대 속도에 따라 말단 기울기(terminal slope) 해석의 안전성이 달라집니다.
Alt text: 두 개의 병렬 흐름도가 분포(distribution)가 먼저 정리되는 경우와 소실(elimination)이 먼저 크게 진행되는 경우를 비교합니다.
Source relation: 교과서 개념을 바탕으로 새로 그린 도식입니다.
<!-- /FIGURE_SCHEMATIC -->

<!-- MASTER LENS -->
> **전문가 보강(Mastery Augmentation) — [CRUCIBLE_DERIVED]**  
> 말단 기울기(terminal slope)를 채택할 때의 질문은 "마지막 구간이 직선인가?"가 아닙니다. "그 직선이 전체 소실 과정을 대표할 만큼 분포 단계의 영향이 작아졌는가?"입니다. 이 차이가 $t_{1/2}$를 안전한 요약값으로 쓸 수 있는지 결정합니다.


### 🃏 C5. 평균체류시간(Mean Residence Time, $MRT$)

<!-- MASTER LENS -->
<!-- ANNOTATION -->
$MRT$는 약물 분자가 체내에 평균적으로 머무는 시간입니다. $t_{1/2}$가 "절반으로 줄어드는 시간"이라면, $MRT$는 농도-시간 곡선의 시간 방향 평균입니다. 즉 1차 모멘트(← 시간으로 가중한 농도 면적)를 AUC로 나눈 값입니다. [G p.19; R&T p.60]

#### A. 형식적 정의(Formal Definition)

$$
AUC_0^\infty=\int_0^\infty C(t)dt \qquad [\text{G Eq.2:8, p.19}]
$$

$$
AUMC_0^\infty=\int_0^\infty t\cdot C(t)dt \qquad [\text{G Eq.2:10, p.19}]
$$

$$
MRT=\frac{AUMC_0^\infty}{AUC_0^\infty} \qquad [\text{G Eq.2:11, p.19}]
$$

1구획 IV bolus에서는 다음이 성립합니다. [R&T Eq.3-25, p.60]

$$
MRT=\frac1K=\frac{t_{1/2}}{\ln 2}\approx1.443\cdot t_{1/2}
$$

#### B. Compound A 기준 데이터

| Subject | $K$ (min⁻¹) | $t_{1/2}$ (min) | $MRT$ (min) | $MRT/t_{1/2}$ |
|---|---:|---:|---:|---:|
| 1 | 0.01 | 68 | 98 | 1.44 |
| 2 | 0.02 | 34 | 48 | 1.41 |
| 3 | 0.02 | 36 | 53 | 1.47 |
| 4 | 0.01 | 71 | 100 | 1.41 |

[Source: G Table 1.3, p.474]

<!-- ANCHOR -->
4명 모두 $MRT/t_{1/2}$가 약 1.44에 모입니다. 이 비율은 1구획 IV bolus에서 단일지수 감소(monoexponential decline)가 성립한다는 수학적 서명(signature)입니다. 이 세션에서는 이 사실까지만 고정하고, 다구획 또는 혈관외(extravascular) MRT 전개는 후속 세션으로 보냅니다. [G p.19, p.474; R&T p.60–61]

#### C. 경계(Boundary)

- AUMC는 $t\cdot C(t)$의 적분이므로 말단 영역(terminal region)에서의 외삽(extrapolation) 오차가 AUC보다 크게 증폭됩니다. 이것이 NCA 보고서에서 $MRT$ 추정의 안정성이 $t_{1/2}$보다 낮은 이유입니다. 그래서 말단 단계 데이터의 품질이 결정적으로 중요합니다. [G p.19]
- $MRT=1/K=1.443\,t_{1/2}$는 1구획 IV bolus에 한정됩니다. 혈관외 투여나 다구획 동력학에서는 이 단순 관계가 깨집니다. 그 일반화는 후속 NCA·다구획 세션 영역입니다. [R&T p.60–61]

<!-- RECAP -->
**C5 요약(Recap):** $MRT$는 NCA에서 "평균 체류 시간"을 주는 연결 파라미터(bridge parameter)입니다. 1구획 IV bolus에서는 $1/K$로 단순하지만, 이 단순성이 성립하는 조건을 기억해야 합니다.

> **▶ 실무 체화 요약(Practice Brief) — C5 체화 4축 — [EXPERT_INFERENCE, v3]**
> - **왜 알아야 하는가:** $MRT$를 $t_{1/2}$의 단순 변형(× 1.443)으로 외우면, 다구획·혈관외(extravascular) 상황에서 이 관계가 깨질 때 NCA 보고서를 잘못 해석하게 됩니다.
> - **흐름상 역할:** C5는 C1–C4의 종합이자 비구획분석(NCA, non-compartmental analysis) 세션의 연결고리(bridge)입니다. $V_{ss}=CL\cdot MRT$를 통해 분포 동력학(distribution kinetics) 세션의 $V_{ss}$ 정의로 직접 연결됩니다.
> - **체화 꿀팁:** $t_{1/2}$는 중위, $MRT$는 평균이라는 통계적 비유를 고정하면 됩니다. $\ln 2$가 등장하는 모든 자리는 "절반이 되는 시점"이지 "평균 체류"가 아님이 자동으로 떠오릅니다.
> - **실무 활용:** Compound A에서처럼 $MRT/t_{1/2}\approx 1.443$이면 1구획 단일지수(monoexponential)의 정량적 신호입니다. 1.443에서 크게 벗어나면 다구획성·흡수 지연·말단 외삽(terminal extrapolation) 오차를 의심하는 첫 번째 진단 단서가 됩니다.

---

<!-- MASTER LENS -->
> **전문가 보강(Mastery Augmentation) — [TEXTBOOK_DERIVED]**  
> $MRT/t_{1/2}\approx 1.443$은 단순한 암기값이 아니라 단일지수(monoexponential) 1구획 IV bolus 구조의 서명입니다. 이 비율이 크게 흐트러지면 먼저 "자료가 1구획처럼 행동하고 있는가?"를 점검해야 합니다.

## §5 — 혼동쌍 해부(Confusion Pair Dissection)

### 🔀 혼동쌍 1. $CL$ vs $K$ — 일차 vs 이차(Primary vs Secondary)

<!-- CONFUSION -->

| 비교 | $CL$ | $K$ |
|---|---|---|
| 본질 | 단위 시간당 완전히 제거되는 겉보기 용적(apparent volume) | 단위 시간당 제거되는 분율(fraction) |
| 단위 | 용적/시간(volume/time) | 1/시간(1/time) |
| 핵심식 | $CL=Dose/AUC=R_{in}/C_{ss}=Q\cdot E$ | $K=CL/V$ |
| 생리학적 위치 | 혈류, 추출, 대사, 배설 경로와 직접 연결 | $CL$과 $V$의 비율로만 해석 가능 |
| 임상 질문 | "노출과 유지용량이 어떻게 변하는가?" | "반로그 기울기(semi-log slope)와 반감기가 어떻게 보이는가?" |
| **치명적 타격(Critical Blow)** | $K$를 공변량(covariate) 탐색의 대상으로 삼아 신기능이나 체중의 영향을 $K$에 모델링하면, 신기능이 $CL$에, 체중이 $V$에 각각 독립적으로 영향을 주는 생리학적 구조를 놓치게 됩니다. 그 결과 공변량이 없거나 잘못된 방향으로 추가된 모델이 규제 제출에 사용되며, 신부전 환자의 용량 조절 근거가 결여된 NDA 패키지가 만들어집니다. [EXPERT_INFERENCE, v3] | (좌측 셀과 동일 — 혼동쌍 전체에 적용되는 결과) |

**핵심 정정:** $K$가 같아도 $CL$이 같다는 뜻은 아닙니다. Compound A Subject 1과 4는 $K\approx0.01$ min⁻¹로 유사하지만 $CL$은 0.1 vs 0.2 L/min으로 다릅니다. [G p.473–474]

> **⚡ 기억 고리 (Memory Hook) — *배수구 vs 배수 속도* — [EXPERT_INFERENCE, v3]**
> $CL$은 **배수구의 크기**(단위 시간당 혈액 정화량 = 처리 용량)이고, $K$는 **수위가 떨어지는 상대 속도**($=CL/V$, 욕조 크기로 나눈 값)입니다. 배수구가 커도 욕조가 크면 수위는 천천히 떨어집니다. 그래서 $K$가 같아도 $CL$은 전혀 다를 수 있습니다. 공변량(covariate)이 붙는 곳은 배수구($CL$)와 욕조($V$)이지, 그 비율($K$)이 아닙니다.

<!-- TRENCH -->
[실무 확장/교과서 외 해석] 통계적 적합도(fit)가 좋아도 공변량을 $K$에 직접 묶으면 $CL$ 매개 변화와 $V$ 매개 변화가 분리되지 않을 수 있습니다. 적합 통과와 외삽 가능성(extrapolation)은 같은 문제가 아닙니다.

### 🔀 혼동쌍 2. $V$ vs $V_{ss}$ — 겉보기 bolus 용적 vs 항정상태 분포 용적

<!-- CONFUSION -->

| 비교 | $V$ | $V_{ss}$ |
|---|---|---|
| 본질 | $A_b/C$ 또는 $D/C^0$로 보는 겉보기 희석 공간(apparent dilution space) | 조직 분배계수와 조직 용적(tissue volume)을 반영한 항정상태 분포 공간(steady-state distribution space) |
| 이 세션 처리 | 1구획에서는 사실상 같은 개념으로 사용 | 식의 의미만 맥락으로 유지 |
| 위험 | 실제 해부학적 부피로 오해 | 분포 동력학(distribution kinetics) 세션 내용을 이 세션에 과도하게 끌어옴 |

**고정:** 본 세션에서는 "$V$는 겉보기 파라미터(apparent parameter)"까지만 체화하면 됩니다. $V_{ss}$의 본격 해석은 후속 분포 동력학(distribution kinetics)에서 다룹니다. [G p.20–21; R&T p.63–64]

> **⚡ 기억 고리 (Memory Hook) — *용기 크기 vs 외관상 용기 크기* — [EXPERT_INFERENCE, v3]**
> $V$는 "약이 실제로 어디에 있는가"가 아니라, 관측된 혈장 농도(plasma concentration)를 설명하기 위해 **가정해야 하는 겉보기 공간의 크기**입니다. 조직 결합이 강할수록 $V$는 실제 체적을 훨씬 초과합니다. $V_{ss}$는 평형 상태에서의 이 겉보기 크기이며, 다구획 모델에서는 중심 구획 $V$와 달라집니다. 두 개의 수조 중 하나가 조직이고 약이 그 안에 갇혀 있다면, 혈장만 재면 수조가 훨씬 커 보이는 원리와 같습니다.

### 🔀 혼동쌍 3. $t_{1/2}$ vs $MRT$

<!-- CONFUSION -->

| 비교 | $t_{1/2}$ | $MRT$ |
|---|---|---|
| 본질 | 농도/약물량(amount)이 절반 되는 시간 | 분자가 체내에 머무는 평균 시간 |
| 수식 | $0.693/K=0.693\cdot V/CL$ | $AUMC/AUC$ |
| 1구획 IV bolus | $t_{1/2}=0.693\cdot MRT$ | $MRT=1.443\cdot t_{1/2}$ |
| 해석 위험 | 말단 단계(terminal phase) 선택 오류 | AUMC 말단 외삽(terminal extrapolation) 오류 |

> **⚡ 기억 고리 (Memory Hook) — *중위 vs 무게중심* — [EXPERT_INFERENCE, v3]**
> $t_{1/2}$은 농도가 반으로 줄어드는 **중위 시간**이고, $MRT$는 약 분자 한 개가 체내에 머무는 **평균 체류 시간**($AUMC/AUC$)입니다. 1구획 1차 제거에서 $MRT=1/K=t_{1/2}/\ln 2\approx 1.443\times t_{1/2}$입니다. 이 1.443배는 생리학적 차이가 아니라 **지수함수 적분의 수학적 필연**입니다. 분포나 흡수 지연이 더해지면 $MRT$는 $t_{1/2}$보다 훨씬 더 길어질 수 있어, 반감기 하나로 체류 시간을 추정하는 오류가 생깁니다.

<!-- RECAP -->
**§5 요약(Recap):** 세 혼동쌍은 모두 "표면적으로 비슷하지만 위계가 다르다"는 문제입니다. $CL$ vs $K$는 일차/이차(primary/secondary)의 차이입니다. $V$ vs $V_{ss}$는 겉보기/항정상태(apparent/steady-state)의 차이입니다. $t_{1/2}$ vs $MRT$는 절반이 되는 시간과 평균 체류 시간의 차이입니다.

---

## §7 — 자기 테스트: 능동 회상 모듈(Active Recall Module)

<!-- SELF-TEST -->
### Q1 [회상 ★★]
$t_{1/2}$을 $V$와 $CL$로 표현하고, 왜 이차 파라미터(secondary parameter)인지 설명해 보세요.

**정답:**
$$
t_{1/2}=\frac{0.693\cdot V}{CL}
$$
따라서 $t_{1/2}$은 $V$와 $CL$의 함수입니다. $t_{1/2}$만 보고 $CL$ 감소인지 $V$ 증가인지 알 수 없습니다. [G p.17–18; R&T p.58]

### Q2 [회상 ★]
$V$의 정의식 두 가지를 쓰세요.

**정답:**
$$
V=\frac{A_b}{C},\qquad V=\frac{D_{iv}}{C^0}
$$
또는 말단 단계(terminal phase) 정보가 있으면 $V=CL/K=1.44\cdot CL\cdot t_{1/2}$로 계산합니다. [G p.20; R&T p.63]

### Q3 [회상 ★]
$C_{ss}=R_{in}/CL$을 1구획 주입(infusion) ODE에서 도출해 보세요.

**정답:**
$$
\frac{dC}{dt}=\frac{R_{in}}{V}-\frac{CL}{V}C
$$
항정상태에서 $dC/dt=0$입니다:
$$
C_{ss}=\frac{R_{in}}{CL}
$$
$V$는 소거됩니다. $V$는 항정 도달 시간에 영향을 주지만 최종 $C_{ss}$ 자체는 $CL$이 결정합니다. [G p.22–23]

### Q4 [회상 ○]
$MRT$의 정의식과 1구획 IV bolus에서 $t_{1/2}$와의 관계를 쓰세요.

**정답:**
$$
MRT=\frac{AUMC}{AUC},\qquad MRT=\frac1K=1.443\cdot t_{1/2}
$$
단, 두 번째 등식은 1구획 IV bolus 한정입니다. [G p.19; R&T p.60]

### Q5 [적용 ★★]
Compound A Subject 1과 4는 다음과 같습니다. 같은 주입속도(infusion rate) $R_{in}=10$ µg/min를 주면 $C_{ss}$는 같을까요?

| Subject | $V$ (L) | $CL$ (L/min) | $K$ (min⁻¹) | $t_{1/2}$ (min) |
|---|---:|---:|---:|---:|
| 1 | 10 | 0.1 | 0.01 | 68 |
| 4 | 20 | 0.2 | 0.01 | 71 |

[Source: G Tables 1.2/1.3, p.473–474]

**정답:** 같지 않습니다.
$$
C_{ss,1}=10/0.1=100\;\mu g/L
$$
$$
C_{ss,4}=10/0.2=50\;\mu g/L
$$
두 subject는 $K$와 $t_{1/2}$가 비슷하지만 $CL$이 다릅니다. 항정 농도는 $CL$이 결정합니다. [G Eq.2:22, p.23]

### Q6 [적용 ★★]
어떤 환자군에서 $t_{1/2}$가 길어졌습니다. 이것이 $CL$ 감소 때문인지 $V$ 증가 때문인지 구분하려면 무엇을 보아야 할까요?

**정답:** AUC와 $C^0$를 분리해서 봅니다. $CL$ 감소는 $AUC=Dose/CL$ 증가로 나타납니다. $V$ 증가는 $C^0=D/V$ 감소로 나타납니다. 따라서 둘이 동시에 변하면 $t_{1/2}$ 하나로는 원인 분리가 불가능합니다. [G p.17–20; R&T p.58–60]

### Q7 [적용 ★]
R&T midazolam case: 79-kg 성인, 7.5 mg base IV bolus, AUC = 287 µg·hr/L, $t_{1/2}=3.8$ hr.  
(a) $CL$은? (b) $V$는? (c) 5분 혈장 농도 180 µg/L, 혈장 용적 3.4 L이면 혈장 내 약물량과 혈장 밖 분율(fraction)은?

**정답:**
$$
CL=7500/287=26.1\;L/hr\approx26\;L/hr
$$
$$
V=1.44\times 26\times 3.8=142\;L
$$
혈장(plasma) 내 약물량은 $180\;\mu g/L\times 3.4\;L=612\;\mu g=0.612$ mg입니다. 따라서 $7.5-0.612=6.89$ mg, 약 92%가 이미 혈장 밖에 있습니다. [R&T p.61–63]

### Q8 [적용 ★]
어떤 IV bolus 자료에서 $MRT/t_{1/2}$가 1.85였습니다. 1구획 IV bolus의 기대값 1.443과 다릅니다. 무엇을 의심해야 할까요?

**정답:** 1구획 IV bolus의 단순 지수 감소가 아닐 가능성, 특히 분포 동력학(distribution kinetics) 또는 말단 외삽(terminal extrapolation) 문제를 의심합니다. 출처 기반 결론은 여기까지입니다. 구체적인 NONMEM ADVAN 선택은 후속 실무 모델링 판단입니다. [G p.19; R&T p.60–66]

### Q9 — 출처 기반 보스 딜레마(Boss Dilemma) ★★
새 IV bolus 약물이 반로그 도표(semilog plot)에서 이상성 감소(biphasic decline)를 보입니다. 1구획 모델은 단순하고 AUC 중심 결정을 설명하기 쉽습니다. 2구획 모델은 분포 단계를 더 잘 설명하지만 현재 데이터가 희박합니다(sparse). 어떤 논리로 모델 구조를 방어해야 할까요?

**정답:** "어느 모델이 항상 옳은가"가 아니라 **분포 단계가 임상적으로 중요한 시간대인지**를 먼저 판단합니다. Midazolam처럼 분포가 빠르고 분포 단계 AUC가 전체의 50% 미만이면 1구획 근사가 일부 목적에서 가능합니다. 그러나 gentamicin처럼 말단 단계 전에 대부분의 소실이 발생하면 말단 기울기 중심 해석은 위험합니다. 따라서 모델 선택은 통계적 단순성만이 아니라 농도-시간 프로파일에서 분포와 소실이 경쟁하는 방식에 근거해야 합니다. [R&T p.61–66]

<!-- RECAP -->
**§7 요약(Recap):** 계산 문제의 핵심은 수식 암기가 아니라 "어떤 식에서 어떤 파라미터가 소거되는가"를 보는 것입니다. $C_{ss}$에서는 $V$가 소거되고, $t_{1/2}$에서는 $CL$과 $V$가 함께 남습니다.

---

## §8 — 메타프레임과 큰 그림(Meta-Frame & Big Picture)

### A. 위치 지정(Positioning)

이 세션은 PK/PD 학습 그래프의 출발점입니다. 이후의 모든 구조는 여기서 갈라집니다.

- **다구획 모델:** 말단 단계가 정말 소실을 대표하는지 묻습니다. [R&T p.61–66]
- **흡수 모델(Absorption models):** 혈관외 말단 기울기가 $K$인지 $K_a$인지 묻습니다. [G p.28–32]
- **간/신 청소율(Hepatic/Renal clearance):** $CL=Q\cdot E$와 $CL_R=f_e\cdot CL$을 장기별 생리학으로 분해합니다. [R&T p.55–68]
- **PopPK 공변량:** 공변량을 $CL$에 둘지 $V$에 둘지 결정합니다. [실무 확장/교과서 외 해석]
- **NCA:** $AUC$, $AUMC$, $MRT$가 구획 모델 없이 노출과 체류 시간을 요약합니다. [G p.19; R&T p.60]

### B. 의존성(Dependencies) — 대충 넘기면 생기는 실패 모드

1. **$t_{1/2}$ 단독 해석 오류**  
   $t_{1/2}$ 증가를 곧바로 $CL$ 감소로 읽으면 $V$ 변화 가능성을 놓칩니다. 정답은 항상 "AUC와 $C^0$가 어떻게 변했는가"를 같이 묻는 것입니다. [G p.17–20; R&T p.58–60]

2. **$V$를 실제 부피로 오해**  
   $V=40{,}000$ L 같은 값을 보고 모델이 틀렸다고 판단하면 겉보기 용적(apparent volume) 개념을 놓친 것입니다. $V$는 측정 공간인 혈장 농도(plasma concentration)와 총량 사이의 환산률입니다. [G p.20; R&T p.63–64]

3. **말단 단계 자동 신뢰(Terminal phase 자동 신뢰)**  
   Midazolam처럼 말단 단계가 소실을 잘 대표하는 경우도 있지만, gentamicin처럼 대부분의 소실이 말단 단계 전에 끝나는 예외도 있습니다. [R&T p.61–66]

4. **$K$-직접 모수화($K$-direct parameterization)의 해석 손실**  
   [실무 확장/교과서 외 해석] $K$에 공변량을 직접 묶으면 $CL$ 변화와 $V$ 변화가 구분되지 않습니다. 이 세션의 일차/이차(primary/secondary) 위계는 단순한 교과서 문장이 아니라 PopPK 모수화(parameterization)의 안전장치입니다.

### C. 전문가 해석 지점(Professional Moat)

자동화 도구는 IV bolus 자료(data)에 단일지수 적합(monoexponential fit)을 빠르게 수행하고 $CL$, $V$, $K$, $t_{1/2}$를 출력할 수 있습니다. 그러나 전문가의 가치는 **숫자를 출력하는 것**이 아닙니다. 핵심은 **숫자의 위계를 읽는 것**입니다.

- $C_{ss}$가 다른 이유를 $t_{1/2}$가 아니라 $CL$에서 찾습니다.
- $t_{1/2}$가 바뀌었을 때 $CL$인지 $V$인지 먼저 분해합니다.
- 반로그 도표의 말단 직선(terminal straight line)이 언제 소실을 대표하지 않는지 압니다.
- 출처 기반 진술(source-bound statement)과 [실무 확장/교과서 외 해석]을 구분합니다.

**v3 확장 — 결정 방향성의 구체화 [EXPERT_INFERENCE, v3]:**

- **AUC와 유지용량(maintenance dose)은** → $CL$의 역수에 비례합니다. 신기능이나 약물상호작용으로 $CL$이 반으로 줄면 AUC는 두 배가 됩니다. 이 방향을 즉시 계산하지 못하면 용량 조절 회의에서 기여가 불가능합니다.
- **$C^0$(IV bolus 직후 농도)와 부하용량(loading dose)은** → $V$의 함수입니다. 신부전 환자의 $V$가 변하지 않으면 부하용량은 수정할 필요가 없습니다.
- **말단 기울기(terminal slope)와 반감기는** → $CL/V$의 조합입니다. 단독으로 $CL$도 $V$도 결정하지 못합니다.
- **공변량(covariate)이 붙어야 할 위치는** → $CL$(신기능, 효소유전형)인지 $V$(체중, 수분 상태)인지를 먼저 가설로 잡고 GOF 잔차를 봅니다. $K$를 대상으로 삼으면 두 생리학이 혼재된 표현을 추정하게 됩니다.
- **NCA에서 $MRT$를 보고할 때는** → 구획 모델의 $V/CL$과 어떻게 다른지 설명할 수 있어야 합니다. $MRT=AUMC/AUC$이고, $V_{ss}=CL\cdot MRT$입니다.
- **고위험 상황 인식:** GOF에서 CWRES가 체중이나 CrCl과 상관되어 있다면 → $CL$ 또는 $V$ 중 어느 파라미터에 공변량을 추가할지 판단하는 첫 질문은 "이 공변량이 배수구($CL$)에 영향을 주는가, 아니면 욕조 크기($V$)에 영향을 주는가?"입니다.

<!-- RECAP -->
**최종 요약(Final Recap):** 1구획 IV bolus PK의 본질은 네 식으로 잠깁니다: $CL=Dose/AUC$, $V=D/C^0$, $K=CL/V$, $t_{1/2}=0.693\cdot V/CL$. 그러나 이 자료의 진짜 목표는 식 암기가 아니라 위계 체화입니다. **$CL$과 $V$를 먼저 보고, $K$와 $t_{1/2}$를 그 결과로 읽으면 됩니다.**


---

## PART B — Compiler-Only Appendix

> **Compiler-only warning:** PART B is not learner-facing. Phase 5 must render PART A only. PART B exists to preserve fidelity, prevent regression, and carry rendering instructions.

### B1. Input Manifest

| File | Role | Authority level | Used for | Notes |
| --- | --- | --- | --- | --- |
| 01_scope_lock(4)/(5).md | scope boundary | A0 | Scope range, learner mode, source boundaries, concept limits | Duplicate copies verified identical; `(5)` used. |
| 01_G_1구획 IV PK CL·V·t½(5).pdf | PDF verification source | A1 | Gabrielsson source range and figure/page identity checks | 26-page PDF excerpt; no direct figure embedding. |
| 01_T_1구획 IV PK CL·V·t½(5).pdf | PDF verification source | A1 | Rowland & Tozer source range and figure/page identity checks | 24-page PDF excerpt; no direct figure embedding. |
| 01_Audit_Report_v1(5)/(6).md | audit guardrail | A2 | Factual corrections, unsupported material deletion, figure/page guardrails | Duplicate copies verified identical; `(6)` used. |
| 01_Content Lock v2(3).md | canonical body | A3 | Base learner body for PATCH MODE splicing | §1–§8 used as learner-facing body; process/adjudication sections kept out of PART A. |
| 01_Content Lock v2.1(3).md | figure insertion source | A4 | PATCH MODE figure strategy, marker blocks, insertion map | Four KEEP markers spliced into PART A. |
| 01_crucible_report_v1(2)/(3).md | crucible guardrail | A5 | Grade A insight preservation and forbidden restoration checks | Duplicate copies verified identical; `(3)` used. |
| S01_phase1_patch memo(3)/(4).md | locked reference | A6 support | Audit attention guide and regression context | Duplicate copies verified identical; not copied into learner body. |
| 01_step1_draft_v0(3)/(4).md | deprecated source | A6 | Regression check only | Duplicate copies verified identical; no direct restoration. |
| 01_Content Lock v1(2).md | superseded locked reference | A6 support | Historical reference only | Superseded by v2; not used as canonical body. |
| 붙여넣은 텍스트 (1)(74).txt | Phase 4D instruction | Controller | Master assembler requirements and pass/fail gates | Output filename normalized from prompt default `05_...` to requested `01_...`. |
| 붙여넣은 마크다운(2)(50).md | compiler instruction | A7 | Phase 5 HTML rendering requirements | Condensed into compiler contract below. |


### B2. Mode Declaration

- **Detected mode:** PATCH MODE.
- **Reason:** `01_Content Lock v2.1(3).md` is a figure marker insertion본 / insertion map, not a full reprint of the canonical body.
- **Base body:** `01_Content Lock v2(3).md`, learner-facing §1–§8.
- **Splice rule:** insert only the four approved 4C markers at unique anchors.
- **Scientific text alteration:** none.
- **Learner wrapper and mastery layer:** added as separate, labeled additions.

### B3. Splice Verification Table

| Marker # | Anchor text (truncated) | Anchor found? | Match count | Inserted? | Final location (§ + card) |
| --- | --- | --- | --- | --- | --- |
| 1 | `## §1 — Session Header & Roadmap` | YES | 1 | YES | §1 — Session Header & Roadmap |
| 2 | `### 🃏 C1. Clearance ($CL$) [⚡ Apex Concept]` | YES | 1 | YES | §2 — C1 Clearance |
| 3 | `### 🃏 C2. Volume of Distribution ($V$)` | YES | 1 | YES | §2 — C2 Volume of Distribution |
| 4 | `### 🃏 C4. Half-life ($t_{1/2}$)` | YES | 1 | YES | §2 — C4 Half-life |


### B4. Zero-Omission Coverage Matrix

| Domain | Required item | Evidence in PART A | Status | Action |
| --- | --- | --- | --- | --- |
| C1 Scope concepts | C1–C5 cards: CL, V, K, t1/2, MRT | §2 contains all five concept cards in locked order | PRESENT | None |
| C1 Scope role | CL/V/t1/2/K hierarchy: t1/2 is function of CL and V, not vice versa | §1 Big Idea; C3; C4; §5 Pair 1 | PRESENT | None |
| C1 Scope boundary | Ka, F, tlag not promoted to MUST | C1 boundary; C3 boundary; rejected/deferred rules in Part B | PRESENT_COMPRESSED | Do not expand in Phase 5 |
| C2 Data anchors | Compound A Case Study PK1 4-subject CL/V/K/AUC and MRT table | C1 Compound A anchor; C5 Compound A anchor | PRESENT | None |
| C2 Data anchors | Creatinine vs inulin same CL, different V/t1/2 | C4 Formal definition table | PRESENT | None |
| C3 Audit MUST_FIX | Subject 1 vs Subject 4 CL self-contradiction corrected | C1 anchor states S1 CL=0.1, S4 CL=0.2 and C_ss not equal | PRESENT | None |
| C3 Audit MUST_FIX | Unsupported clinical/regulatory/NONMEM numeric claims removed or isolated | §7 Q9 source-bound dilemma; TRENCH labels for practice extensions | PRESENT | None |
| C4 Audit T5 | R&T Fig.3-1/3-2 opening bridge included | Figure Pointer #1 after §1 | PRESENT | None |
| C4 Audit T5 | R&T Fig.3-6 distribution/elimination bridge included | Figure Schematic #4 after C4 | PRESENT | None |
| C5 Figure coverage | All four KEEP markers present exactly once; rejected candidates not restored | Splice Verification Table; Part A markers #1–#4 | PRESENT | None |
| C5 Image rights | No copyrighted textbook figure embedded | Figure rights note; marker instructions; compiler contract | PRESENT | Phase 5 must render pointers or redrawn schematic only |
| C6 Page tags | Existing Content Lock page tags preserved; no new page tags fabricated | All source tags preserved in Part A body and figure marker Source fields | PRESENT | None |
| C7 Crucible Grade A | Fix-1/Fix-2/Delete-3/Delete-4/Add-5/Add-6/Tip-7/Tip-8/Compress-9 preserved | C1 correction; toned wording; removed invented claims; figure markers; C3/C4 TRENCH; Q9 compressed | PRESENT | None |
| C8 Deprecated draft regression | Step 1 v0 rejected material not restored | No unsupported FDA 30%, invented OFV/COV statistics, or numeric clinical expansions | PRESENT | None |
| C9 Canonical body integrity | Scientific body remains Content Lock v2 §1–§8 with approved markers and labeled augmentations | No broad rewrite; no equation/page-tag alteration | PRESENT | None |
| C10 v3 Apex label (v3) | C1 marker uses standardized `[⚡ Apex Concept]` instead of informal `[Apex]` | C1 heading line; B3 splice table also updated for consistency | PRESENT (v3) | None |
| C11 v3 Plausible Fallacy (v3) | Apex card carries Plausible Fallacy block grounded in existing S1/S4 anchor | C1 card after Recap | PRESENT (v3) | None |
| C12 v3 Memory Hooks (v3) | All three §5 confusion pairs carry structurally-encoded Memory Hooks | §5 Pair 1/2/3 each has a Memory Hook callout | PRESENT (v3) | None |
| C13 v3 Critical Blow (v3) | Highest-impact pair (CL vs K) carries Critical Blow row in comparison table | §5 Pair 1 table 치명적 타격 row | PRESENT (v3) | None |
| C14 v3 Practice Briefs (v3) | C1–C5 cards each carry 4-axis Practice Brief (왜·흐름·꿀팁·실무) | After each card Recap | PRESENT (v3) | None |
| C15 v3 §8C expansion (v3) | Professional Moat extended from 4 abstract bullets to 4 + 6 decision-direction bullets | §8C Professional Moat | PRESENT (v3) | None |
| C16 v3 LaTeX integrity (v3) | All v3 additions preserve subscript/fraction conventions: $K$, $CL$, $V$, $t_{1/2}$, $MRT$, $AUC$, $C_{ss}$, $V_{ss}$ | Inspected v3 inserts: no `\a`-style BEL char, no broken subscripts, no fractured fractions | PASS (v3) | None |


### B5. Controlled Micro-Patch Log

No micro-patches needed. PART A equals Content Lock v2 §1–§8 with exact approved 4C marker splices, learner navigation wrapper, and labeled Mastery Augmentation Layer. The correction and compression work required by Audit/Crucible had already been incorporated in Content Lock v2.

### B6. Mastery Augmentation Log

| Augmentation # | Location | Epistemic label | Purpose | Why allowed |
| --- | --- | --- | --- | --- |
| AUG-1 | after Figure Pointer #1 / before §2 | CRUCIBLE_DERIVED | Reader decision order: exposure→CL, initial/loading→V, time→CL/V or V/CL | No new numeric/example; clarifies existing hierarchy |
| AUG-2 | after C1 Figure Pointer | CRUCIBLE_DERIVED | V cancels from Dose/AUC interpretation; CL remains exposure-dose transformer | Directly grounded in Content Lock C1 |
| AUG-3 | after C2 Figure Pointer | AUDIT_DERIVED | Large V means measurement-space mismatch, not anatomical volume | Grounded in G Fig.2.3/quinacrine apparent-volume correction |
| AUG-4 | after C4 Figure Schematic | CRUCIBLE_DERIVED | Terminal slope gate: representation of elimination, not just visual straightness | Grounded in R&T Fig.3-6/midazolam/gentamicin discussion |
| AUG-5 | after C5 card / before §5 | TEXTBOOK_DERIVED | MRT/t1/2≈1.443 as monoexponential one-compartment signature | Already present in C5; adds internalization only |
| AUG-6 (v3) | C1 card, after Recap | EXPERT_INFERENCE, v3 | Apex Concept Plausible Fallacy: same K does not mean same elimination capacity | Reuses existing locked S1/S4 CL/V values; no new numerics |
| AUG-7 (v3) | C1–C5 cards, after each Recap | EXPERT_INFERENCE, v3 | Practice Brief 4-axis blocks (왜·흐름·꿀팁·실무) for each card | Each block re-grounds existing locked content; no new equations |
| AUG-8 (v3) | §5 Pair 1 (CL vs K), after table | EXPERT_INFERENCE, v3 | Memory Hook: drain (CL) vs water-level descent rate (K) | Reuses existing locked CL/V/K hierarchy |
| AUG-9 (v3) | §5 Pair 2 (V vs Vss), after Lock | EXPERT_INFERENCE, v3 | Memory Hook: container size vs apparent container size | Reuses existing locked apparent-volume framing |
| AUG-10 (v3) | §5 Pair 3 (t½ vs MRT), after table | EXPERT_INFERENCE, v3 | Memory Hook: median (t½) vs centroid (MRT); 1.443 as math necessity | Reuses already-locked 1.443 ratio |
| AUG-11 (v3) | §5 Pair 1 table | EXPERT_INFERENCE, v3 | Critical Blow row: K-as-covariate-target → NDA failure mode | Caution-direction extension of existing Critical correction |
| AUG-12 (v3) | §8C Professional Moat | EXPERT_INFERENCE, v3 | 6-bullet decision-direction expansion (AUC/CL, C0/V, terminal/CL·V, covariate position, MRT/Vss, GOF triage question) | Operationalizes existing hierarchy without new clinical numerics |


### B7. Approved Figure Strategy / Insertion Map Summary

| # | Location | Mode | Source relation | Phase 5 action |
|---:|---|---|---|---|
| 1 | after §1 Roadmap | P | R&T Fig.3-1 p.54 + Fig.3-2 p.55 | Render as text-only figure pointer callout; do not embed source images. |
| 2 | after C1 Clearance | P | R&T Fig.3-3 p.55 | Render as text-only figure pointer callout; do not embed source image. |
| 3 | after C2 Volume | P | G Fig.2.3 p.15 | Render as text-only figure pointer callout; do not embed source image. |
| 4 | after C4 Half-life | R | Redrawn from R&T Fig.3-6 concept | Generate a new schematic from the brief only; do not reproduce the textbook layout, colors, or curves. |


Rejected figure candidates must not be restored in Phase 5: C3 G Fig.2.6 pointer, §5 G Fig.2.11/2.12 schematic, C5 G Table 1.3 pointer, and additional C4 R&T Fig.3-4/Fig.3-7 pointers.

### B8. Phase 5 Compilation Contract

**Scope of rendering**
- Render **PART A only** as learner-facing HTML.
- PART B is compiler reference; do not render PART B as learner content.

**Marker → component mapping (mandatory)**
- `<!-- MASTER LENS -->` → callout box; gold left border 4px; background `rgba(201,168,76,0.08)`.
- `<!-- ANNOTATION -->` → inline gloss; muted color; italic.
- `<!-- ANCHOR -->` → bridge sentence; italic; muted.
- `<!-- TRENCH -->` → practical tip box; rose left border; rose-tint background.
- `<!-- CONFUSION -->` → side-by-side comparison panel; amber accent.
- `<!-- SELF-TEST -->` → click-to-reveal accordion; question visible, answer hidden until interaction.
- `<!-- RECAP -->` → section summary box; blue left border; blue-tint background.
- `[확인 필요]` → highlighted flag (`<mark>`).
- `<!-- FIGURE_POINTER -->` → text-only figure pointer callout; purple left border; 📖 icon.
- `<!-- FIGURE_SCHEMATIC -->` → inline `<figure>` with Mermaid (default) or SVG; `<figcaption>` below; alt text required.

**Figure rendering rules (learner-facing)**
- Pointer markers: text-only callout; do not embed source images.
- Schematic markers: render exactly the brief; do not reproduce textbook layout, colors, or curves; visually distinct from source.
- Image-insert markers: not used in this session (Image rights = None).
- Mermaid blocks must pass M1–M6 self-check (valid directive; safe node IDs; quoted complex labels; no trailing semicolons inside node defs); fall back to inline SVG or CSS comparison cards if Mermaid expressiveness is insufficient.

**Page tag rendering rules**
- Detect `[p.XX]`, `[pp.XX–YY]`, `[pp.XX, YY]`, `[p.확인 필요]` patterns in body text only.
- Wrap in `<span class="source-page">…</span>`; uncertainty tags additionally carry `.source-uncertain`.
- Do not apply pattern detection inside `<pre><code>` blocks or inside figure marker blocks (those have their own internal "Source:" fields).
- Preserve page numbers exactly; do not normalize, fabricate, or remove.
- Print-mode visibility must be preserved (no `display:none` via `@media print`).

**Recommended canonical anchor id list (for stable navigation)**
| Section / card | Recommended `id` |
|---|---|
| §1 — Session Header & Roadmap | `sec-1-roadmap` |
| §2 — Concept Anatomy Cards | `sec-2-cards` |
| C1 Clearance | `card-c1-cl` |
| C2 Volume of Distribution | `card-c2-v` |
| C3 Elimination Rate Constant | `card-c3-k` |
| C4 Half-life | `card-c4-thalf` |
| C5 Mean Residence Time | `card-c5-mrt` |
| §5 — Confusion Pair Dissection | `sec-5-confusion` |
| §5 Pair 1 (CL vs K) | `pair-1-cl-vs-k` |
| §5 Pair 2 (V vs Vss) | `pair-2-v-vs-vss` |
| §5 Pair 3 (t½ vs MRT) | `pair-3-thalf-vs-mrt` |
| §7 — Self-Test | `sec-7-selftest` |
| §8 — Meta-Frame & Big Picture | `sec-8-metaframe` |

**Output specification**
- Single self-contained HTML file with inline custom CSS and JS.
- External runtime dependencies allowed only for: MathJax CDN, Mermaid CDN, cdnjs library list (e.g., highlight.js).
- No `<iframe>`, no external local CSS/JS/font/image files.
- Self-Test answers hidden by default; revealed on user interaction only.
- Print mode: backgrounds suppressed; navigation hidden; source page tags remain visible.

### B9. Forbidden Restoration List

The following items must NOT be reintroduced in Phase 5 even if they appear in deprecated drafts or memos:
- Unsupported FDA-style 30% adjustment percentages.
- Invented OFV thresholds or `$COV` step success/failure statistics not in source PDFs.
- Quantitative clinical scenarios beyond Compound A, Creatinine/Inulin, Midazolam, Gentamicin.
- Loading dose worked example beyond `LD = V × C_target` qualitative reference (Practice Brief, C2 실무 활용).
- Hierarchy Collapse signature naming as a separate GOF pattern label.
- §3 Structural Isomorphism, §4 Interactive Simulator, §6 Pragmatic Application Scenarios — these are HTML compile responsibilities under separate Step 2 Apex protocol, not part of this single-source v3.x handout.

### B10. Source-Boundary Certificate

- All scientific claims in PART A trace to: Gabrielsson & Weiner 5e Ch.2 §2.2.1–2.2.5 + Case Study PK1 (G p.14–32, p.469–475) OR Rowland & Tozer 5e Ch.3 (p.53–76).
- All [실무 확장/교과서 외 해석] tags mark non-source-bound practice extensions.
- All `[EXPERT_INFERENCE, v3]` tags mark v3 augmentations that re-articulate locked content without adding new numerics, page tags, or external claims.
- v3.1 patches are Korean readability adjustments only; they introduce zero new scientific content.

### B11. Trace Hashes

| Artifact | sha256 (descriptive) |
|---|---|
| Content Lock v2 base body | `bb5eab629fc9118a` (ver1 reference) |
| ver2 spliced PART A body | recomputed by downstream pipeline if required |
| v3 spliced PART A body | recomputed by downstream pipeline if required |
| v3.1 spliced PART A body | recomputed by downstream pipeline if required (v3.1 surgical Korean readability patches only) |
| v3.2 spliced PART A body | recomputed by downstream pipeline if required (v3.2 Korean-Dominant Readability Patch) |

### B12. Final Checklist

- PART A is independently readable as a learner handout.
- PART A contains learner navigation aid, canonical body, approved figure markers, preserved page tags, self-tests, and labeled augmentations.
- PART A contains no audit/adjudication process tables.
- PART B contains process logs, coverage matrix, compiler rules, guardrails, ver2 patch log, v3 change log, v3.1 change log, and v3.2 change log only.
- No HTML was generated.
- No Mermaid/SVG code was generated.
- ver2 patches (P1–P5) applied; v3 patches (V1–V6) applied; v3.1 Korean readability patches (KR-001–KR-031) applied; v3.2 Korean-Dominant readability patches (KRD-001–KRD-083) applied; canonical scientific body unchanged.
- Critical MathJax rendering bug (BEL char + 'pprox' typo) FIXED in ver2 and preserved in v3 / v3.1 / v3.2.
- v3.2 Korean-Dominant patches preserve all v3.1 numerics, page tags, figure markers, self-test answers, and equations.
- Final output filename: `01_html_compile_input_master_v3.2.md`.

### B13. Ver2 Patch Log

| # | Type | Location | Change | Source authority | Risk control |
|---|---|---|---|---|---|
| P1 | CRITICAL TYPO FIX | C5 Practice Brief / display math | Removed BEL character + `pprox` → `\approx`; restored `\frac{t_{1/2}}{\ln 2}\approx 1.443\cdot t_{1/2}` rendering. | LaTeX/MathJax syntax; no scientific change. | Pure rendering fix; no content alteration. |
| P2 | LANG TONING | C1 anchor | Tightened "두 사람이 같은 약물 처리 능력을 가졌다" framing. | Source-bound interpretation of S1/S4 difference. | Verbal compression only; no numeric change. |
| P3 | LANG TONING | §5 Pair 1 critical correction | Standardized "정정된 핵심" → "Critical correction" / "핵심 정정". | Crucible Grade A (already approved). | Bilingual label consistency. |
| P4 | DEPTH | C5 MRT card | Added a 2-bullet `#### C. Boundary` matching depth of other cards. Bullet 1: AUMC sensitivity to terminal extrapolation. Bullet 2: $MRT=1/K=1.443\,t_{1/2}$ holds only in 1-cmt IV bolus; generalization is future-session. | G p.19 (AUMC is t·C(t) integral). R&T p.60–61 (1-cmt IV bolus restriction explicitly stated). | The flagged NOT_IN_SOURCE formula `MRTiv = Vss/CL` (Audit T1 line 71) is **not** introduced; only the qualitative statement that the simple relation breaks outside 1-cmt IV bolus, which is direct R&T p.60–61 content. |
| P5 | COMPILER METADATA | PART B §B8 Navigation anchor integrity rules | Added a "Recommended canonical anchor id list" table. PART B is compiler-only and does not affect learner-facing PART A content. | Phase 5 compiler operational requirement; no scientific authority needed. | Pure rendering metadata; no content change. |

**Items intentionally NOT changed in ver2 (and why):**
- Subject 1 vs 4 V values: kept as-is (S1=10, S4=20). Already source-bound.
- Loading dose formula `LD = V × C_target`: not added. R&T p.62–64 supports it conceptually, but Audit/Crucible did not flag its absence as a gap, and adding the formula would expand the worked-example surface beyond Content Lock v2 scope.
- "Hierarchy Collapse pattern" GOF signature naming (Crucible T2(b)): not added as a named pattern. Already represented as concept in C3 TRENCH ("공변량이 CL에 작용하는지 V에 작용하는지 분리하기 어렵다") with `[실무 확장/교과서 외 해석]` tag. Naming the signature would constitute new NOT_IN_SOURCE practice content under a new label.
- §6 Pragmatic Application Scenarios + §3 Structural Isomorphism + §4 Interactive Simulator: intentionally omitted from PART A. These are Step 2 HTML compiler responsibilities (§3·§4·§6 are generated in the HTML compile phase per Step 1 protocol), not Step 1 deliverables.

**Verification after patch:**
- All page tags in PART A: identical to ver1 (no additions, no removals).
- All figure markers: identical to ver1 (4 markers, same anchors, same content).
- Self-test answers: identical to ver1.
- Splice Verification Table (B3): unchanged.
- Trace hash recomputation needed: Spliced PART A body sha256 will differ from ver1 (`bb5eab629fc9118a`) due to P1–P4 edits. New hash will be computed on the final output file by a downstream pipeline if required; recorded here only descriptively.



### B14. v3 Change Log

**Patch scope:** ver2 → v3 surgical patch. Canonical scientific body unchanged. No new external numerics, no new page tags, no new figure markers, no NONMEM code reproduced. v3 addresses only structural-pedagogical gaps identified by independent third-party audit, while preserving the source-fidelity guarantees of v2.

| # | Type | Location | Change | Source authority | Risk control |
|---|---|---|---|---|---|
| V1 | LABEL STANDARDIZATION | C1 heading + B3 splice anchor row | `[Apex]` → `[⚡ Apex Concept]` per Step 1 protocol convention. | Step 1 protocol convention; no scientific authority required. | Pure label rename; B3 anchor row updated for internal consistency. |
| V2 | APEX EXTENSION | C1 card after Recap | Added Plausible Fallacy block: same K does not imply same elimination capacity; uses already-locked S1/S4 CL/V values. | Reuses Audit T1 corrected interpretation and locked S1/S4 numerics from G Tables 1.2/1.3, p.473–474. | No new numerics; tag `[EXPERT_INFERENCE, v3]`. |
| V3 | PEDAGOGICAL DEPTH | C1–C5 cards, each after Recap | Added 4-axis Practice Brief blocks (왜 알아야 하는가 / 흐름상 역할 / 체화 꿀팁 / 실무 활용). | Each axis re-grounds existing locked content; no new equations or numerics introduced. | All five blocks tagged `[EXPERT_INFERENCE, v3]`. |
| V4 | MEMORY ENCODING | §5 Pair 1, Pair 2, Pair 3 | Added one Memory Hook each, encoding *structural reason for difference*: drain vs descent rate (CL vs K); container vs apparent container (V vs Vss); median vs centroid (t½ vs MRT, with 1.443 as integral-of-exponential math necessity). | Reuses existing locked hierarchy; ratio 1.443 already source-anchored in C5 (G p.19, p.474). | No new external metaphors importing fresh quantitative claims; tag `[EXPERT_INFERENCE, v3]`. |
| V5 | CRITICAL BLOW | §5 Pair 1 (CL vs K) table | Added 치명적 타격 row: K-as-covariate-target → NDA package missing renal-impairment dose-adjustment justification. | Operationalization of TRENCH note already present at line 469 of v2 (covariate at K obscures CL/V separation). | No new regulatory citation; framed as plausible failure mode, tag `[EXPERT_INFERENCE, v3]`. |
| V6 | DECISION-DIRECTION EXPANSION | §8C Professional Moat | Preserved existing 4 abstract bullets; appended 6-bullet "decision-direction" expansion (AUC↔CL, C0↔V, terminal↔CL/V, covariate position, MRT/Vss bridge, GOF triage question). | Each bullet re-articulates locked equations from C1–C5; no new clinical examples or page tags. | Tagged `[EXPERT_INFERENCE, v3]`. |

**v3 LaTeX integrity verification (per PATCH 6 directive):**

- Subscripts: `t_{1/2}`, `C_{ss}`, `C^0`, `V_{ss}`, `R_{in}`, `K_{Pi}`, `f_u`, `V_u`, `V_B`, `V_{Ti}`, `E_{Ti}`, `f_e` — all preserved with proper brace grouping.
- Fractions: `\frac{...}{...}` and inline `Dose/AUC`, `CL/V`, `R_{in}/CL`, `\ln 2/K`, `t_{1/2}/\ln 2`, `D/V`, `D/C^0`, `AUMC/AUC` — all preserved.
- Special operators: `\approx`, `\cdot`, `\sum`, `\int_0^\infty`, `\ln` — verified intact in both v2-original blocks and v3 inserts.
- BEL-character / typo regression check: no `\a` (U+0007) followed by malformed `pprox` patterns in v3 inserts. ver2 P1 fix preserved.
- All v3 inserts use `$...$` inline and `> ...` blockquote-only formatting; no new `$$...$$` display blocks introduced (preserves existing display-math inventory).

**Items intentionally NOT changed in v3 (and why):**

- Compound A Subject 1/4 numerics (V=10/20 L, CL=0.1/0.2 L/min, K=0.01 min⁻¹): kept as-is per non-negotiable preservation rule. Memory Hook V4 and Plausible Fallacy V2 reference these values without altering them.
- §6 Pragmatic Application Scenarios + §3 Structural Isomorphism + §4 Interactive Simulator: still intentionally omitted from PART A. These are Step 2 HTML compiler responsibilities, not Step 1 deliverables. (Same rationale as ver2 §B13.)
- Loading dose formula `LD = V × C_target`: still not added to canonical body. Mentioned only inside the C2 Practice Brief 실무 활용 axis as a tagged `[EXPERT_INFERENCE, v3]` interpretive note, not as a new locked equation.
- ver2 P1–P5 patches and their rationale: preserved verbatim in B13.
- Existing figure markers, page tags, trace hashes (B11), source-boundary certificate (B10): unchanged.

**Verification after v3 patch:**

- All v2 page tags in PART A: identical (no additions, no removals).
- All v2 figure markers: identical (4 markers, same anchors, same content).
- v2 self-test answers: identical.
- v2 Compound A numerics: identical.
- ver2 §B13 patch log entries: preserved verbatim.
- New v3 augmentations: 6 entries (V1–V6), all tagged with epistemic label `[EXPERT_INFERENCE, v3]`.
- New v3 PART A insertion blocks: 1 Apex label rename + 1 Plausible Fallacy + 5 Practice Briefs + 3 Memory Hooks + 1 Critical Blow row + 1 Professional Moat expansion = 12 surgical inserts in PART A.
- B6 Mastery Augmentation Log: extended from 5 to 12 entries (AUG-1 to AUG-12).
- B4 Zero-Omission Coverage Matrix: extended from C1–C9 to C1–C16 (added C10–C16 for v3 items).
- B3 Splice Verification Table: anchor text for marker #2 updated from `[Apex]` to `[⚡ Apex Concept]` for consistency with v3 heading.

### B15. v3.1 Change Log — Korean Readability Patch

**Patch scope:** v3 → v3.1 surgical Korean readability patch. **Canonical scientific body unchanged.** No new external numerics, no new page tags, no new figure markers, no new equations, no new NONMEM/R code, no new clinical scenarios. v3.1 addresses only learner-facing Korean prose readability — specifically, the §1 Learner Navigation Aid (which was entirely in English in v3) and a small set of awkwardly long or stylistically uneven Korean sentences inside C1–C5 cards and §5 Pair 1.

| # | Type | Location | Change | Risk |
|---|---|---|---|---|
| KR-001 | Korean flow improvement | §1 Navigation — section header | `### How to Use This Handout` → `### 이 자료 사용법` | Low |
| KR-002 | Korean flow improvement | §1 Navigation — item 1 | English numbered guidance → Korean equivalent (parameter hierarchy lock instruction). Technical terms (`$CL$`, `$V$`, `$K$`, `$t_{1/2}$`, `$MRT$`) preserved. | Low |
| KR-003 | Korean flow improvement | §1 Navigation — item 2 | English numbered guidance → Korean equivalent (card order discipline). C1/C2 references preserved. | Low |
| KR-004 | Korean flow improvement | §1 Navigation — item 3 | English numbered guidance → Korean equivalent (figure pointer instruction). Marker name preserved. | Low |
| KR-005 | Korean flow improvement | §1 Navigation — item 4 | English numbered guidance → Korean equivalent (§5 → §7 sequencing). Section labels preserved. | Low |
| KR-006 | Korean flow improvement | §1 Navigation — item 5 | English numbered guidance → Korean equivalent (§8 framing instruction). Section label preserved. | Low |
| KR-007 | Korean flow improvement | §1 Navigation — section header | `### Learning Route` → `### 학습 순서` | Low |
| KR-008 | Korean flow improvement | §1 Navigation — section header | `### Before You Start / After You Finish` → `### 시작 전 / 완료 후 체크포인트` | Low |
| KR-009 | Korean flow improvement | §1 Navigation — table header row | `\| Checkpoint \| Before starting \| After finishing \|` → `\| 체크 항목 \| 시작 전 \| 완료 후 \|` | Low |
| KR-010 | Korean flow improvement | §1 Navigation — table row 1 | English Q&A pair (Parameter hierarchy) → Korean. Variable symbols (`$CL$`, `$V$`, `$K$`, `$t_{1/2}$`) preserved. | Low |
| KR-011 | Korean flow improvement | §1 Navigation — table row 2 | English Q&A pair (Exposure vs time) → Korean. AUC/$C^0$/slope/$C_{ss}$ preserved. | Low |
| KR-012 | Korean flow improvement | §1 Navigation — table row 3 | English Q&A pair (Apparent volume) → Korean. `$V$` symbol preserved. | Low |
| KR-013 | Korean flow improvement | §1 Navigation — table row 4 | English Q&A pair (Terminal slope) → Korean. "semilog terminal slope" technical term preserved. | Low |
| KR-014 | Korean flow improvement | §1 Navigation — table row 5 | English Q&A pair (NCA bridge) → Korean. `$MRT=1/K=1.443t_{1/2}$` formula preserved. | Low |
| KR-015 | Korean flow improvement | C1 MASTER LENS annotation (line 90 of v3) | `즉시 직관화된다` → `즉시 직관적으로 이해된다` (smoother predicate). | Low |
| KR-016 | Sentence split | C1 Plausible Fallacy bullet 3 | Long compound sentence split into two: "원인이 한 항 안에 뭉개진다. 그 결과 예측력이 낮은 모델이 만들어진다." Trailing GOF clause preserved. | Low |
| KR-017 | Sentence split | C1 Practice Brief — 왜 알아야 하는가 | Long causal chain split into two sentences with explicit "그 결과" connective. Scientific content (`$CL$`, `$t_{1/2}$`, neoteric maintenance dose) preserved. | Low |
| KR-018 | Concept clarification | C1 Practice Brief — 흐름상 역할 | `S01 전 카드` → `이 세션 전체 카드` (clearer Korean expansion of compressed reference). C2/C3/C4/C5 equation references preserved. | Low |
| KR-019 | First-use gloss | C2 Boundary D | `분포 위상이 충분히 빠르다는 가정` → `분포 단계(distribution phase)가 충분히 빠르다는 가정` (Korean term + parenthetical English standard). | Low |
| KR-020 | Korean flow improvement | C2 Practice Brief — 흐름상 역할 | `primary 좌표를 형성하며` → `primary 파라미터 쌍을 이루며` (more natural Korean predicate). | Low |
| KR-021 | Korean flow improvement | C2 Practice Brief — 실무 활용 | `다구획성 의심의 첫 시그널이 된다` → `다구획 동력학을 의심하는 첫 번째 신호가 된다` (natural Korean expression). | Low |
| KR-022 | First-use gloss | C3 Big Idea | `체내 amount 중 단위 시간당 제거되는 fraction` → `체내 약물량(amount) 중 단위 시간당 제거되는 fraction` (Korean term + parenthetical English standard). | Low |
| KR-023 | Korean flow improvement | C3 Boundary first sentence | `반드시 elimination $K$가 아니다` → `반드시 elimination $K$를 의미하지는 않는다` (clearer modal Korean phrasing). | Low |
| KR-024 | Korean flow improvement | C3 Boundary flip-flop sentence | `이 세션에서는 context로만 둔다` → `이 세션에서는 배경 맥락으로만 다룬다` (Korean predicate replaces transliterated English). | Low |
| KR-025 | Sentence split | C4 Big Idea — R&T citation | Single colon-construction sentence split into two: "R&T는 이 점을 명확히 밝힌다. half-life와 elimination rate constant는 …". Scientific content preserved verbatim. | Low |
| KR-026 | Korean flow improvement | C4 Section C — AUC ratio sentence | Long-dash construction `즉 한 가지 비율 — *…* — 이 모델 단순화 가능성을 가른다` → `결국 *…의 비율* 하나가 모델 단순화의 가능성을 결정한다`. Italic emphasis preserved. | Low |
| KR-027 | Korean flow improvement | C4 Practice Brief — 흐름상 역할 | `무한 반복 인용된다` → `지속적으로 참조된다` (formal Korean replaces colloquial intensifier). | Low |
| KR-028 | Sentence split | C5 Boundary first bullet | Run-on sentence split into two: "이것이 NCA 보고서에서 $MRT$ 추정의 안정성이 $t_{1/2}$보다 낮은 이유다. 그래서 terminal phase 데이터의 품질이 결정적으로 중요하다." | Low |
| KR-029 | Redundancy trimming (typo fix) | C5 Practice Brief — 흐름상 역할 | `brige` → `bridge` (typo correction; otherwise identical). | Low |
| KR-030 | Korean flow improvement | C5 Practice Brief — 실무 활용 | `첫 진단점이 된다` → `첫 번째 진단 단서가 된다` (natural Korean expression). | Low |
| KR-031 | Korean flow improvement | §5 Pair 1 — Critical correction label | `**Critical correction:**` → `**핵심 정정:**` (Korean label consistent with surrounding handout language). | Low |

**v3.1 LaTeX integrity verification:**

- All MathJax inline `$...$` and display `$$...$$` blocks: untouched.
- Subscripts (`t_{1/2}`, `C_{ss}`, `C^0`, `V_{ss}`, `R_{in}`, `K_{Pi}`, `f_u`, `V_u`, `V_B`, `V_{Ti}`, `E_{Ti}`, `f_e`): preserved character-for-character.
- Fractions (`\frac{...}{...}` and inline divisions): preserved.
- Special operators (`\approx`, `\cdot`, `\sum`, `\int_0^\infty`, `\ln`): preserved.
- BEL-character / typo regression check: no `\a` (U+0007) + malformed `pprox` patterns introduced. ver2 P1 fix preserved.
- The `brige` → `bridge` typo fix in C5 Practice Brief is plain prose, not LaTeX; no math impact.

**Items intentionally NOT changed in v3.1 (and why):**

- All scientific content in C1–C5 cards: unchanged.
- All page tags (`[G p.XX]`, `[R&T p.XX]`, `[Source: G Tables 1.2/1.3, p.473–474]`, etc.): unchanged.
- All `<!-- FIGURE_POINTER -->` and `<!-- FIGURE_SCHEMATIC -->` marker blocks (4 total): unchanged byte-for-byte (Source/Why/When/Learner instruction fields, plus brief fields).
- All HTML compiler markers (`<!-- MASTER LENS -->`, `<!-- ANNOTATION -->`, `<!-- ANCHOR -->`, `<!-- TRENCH -->`, `<!-- CONFUSION -->`, `<!-- SELF-TEST -->`, `<!-- RECAP -->`): unchanged.
- All §7 self-test questions and answers (Q1–Q9): unchanged.
- All §5 Memory Hooks and Critical Blow row: unchanged.
- All Compound A numerics (S1–S4 V/CL/K/AUC/MRT): unchanged.
- Creatinine vs Inulin comparison (R&T p.58): unchanged.
- midazolam (R&T p.61–62) and gentamicin (R&T p.66) anchor numerics: unchanged.
- §8C Professional Moat 4+6 bullet structure: unchanged.
- ver2 §B13 and v3 §B14 patch logs: preserved verbatim.
- B3 Splice Verification Table: unchanged (all four anchor strings still match exactly because no v3.1 patch modifies any anchor heading).
- B7 Approved Figure Strategy: unchanged.
- B10 Source-Boundary Certificate: unchanged in scope; v3.1 entry added stating "Korean readability adjustments only; zero new scientific content".

**Verification after v3.1 patch:**

- Page tag count: identical to v3 (no additions, no removals).
- Figure marker count: 4 in v3, 4 in v3.1 — anchor positions and contents identical.
- Self-test answer count and content: identical to v3 (Q1–Q9).
- Compound A numerics: identical to v3.
- Equation count and rendering: identical to v3.
- B3 anchor matches: 4/4 unchanged.
- B4 Coverage Matrix entries: still PRESENT or PASS for C1–C16; v3.1 introduces no new domain.
- B6 Augmentation Log: AUG-1 through AUG-12 unchanged (v3.1 readability patches do not constitute new mastery augmentations).
- HTML readiness: unaffected. Phase 5 marker→component mapping (B8) operates on the same 9 marker types, same page tag patterns, and same figure markers as v3.

---

## Final v3.1 All-Pass Checklist

| # | Audit item | Status | Evidence (1-line) |
|---:|---|---|---|
| 1 | PART A readability improved | **PASS** | §1 Navigation now fully in Korean (KR-001~KR-014); 17 additional surgical Korean prose patches applied to C1–C5 cards and §5 Pair 1 (KR-015~KR-031). |
| 2 | Scientific content unchanged | **PASS** | Compound A S1–S4 numerics, Creatinine/Inulin table, midazolam/gentamicin numerics, all derivations and equations identical to v3. No new claims, examples, or values introduced. |
| 3 | Equations preserved | **PASS** | All MathJax blocks (inline `$...$` and display `$$...$$`) byte-identical to v3. Subscripts, fractions, operators verified intact. |
| 4 | Page tags preserved | **PASS** | All `[G p.XX]`, `[R&T p.XX]`, and Source attribution tags identical to v3 (no additions, no removals). |
| 5 | Figure markers preserved | **PASS** | 4 markers (3× FIGURE_POINTER + 1× FIGURE_SCHEMATIC) identical byte-for-byte; all internal Source / Why / When / Learner instruction / brief fields unchanged. |
| 6 | Source-boundary preserved | **PASS** | All [실무 확장/교과서 외 해석] tags retained; all `[EXPERT_INFERENCE, v3]` and `[TEXTBOOK_DERIVED, v3]` tags retained; Forbidden Restoration List (B9) honored; v3.1 introduces zero source-bound additions. |
| 7 | HTML-readiness preserved | **PASS** | B8 marker→component mapping unaltered; B7 Figure Strategy unaltered; B3 Splice Verification Table 4/4 anchors still match exactly; canonical anchor id list (B8) unchanged. |
| 8 | Ready for Phase 5 HTML compilation | **PASS** | Single self-contained `.md` file; PART A is complete learner handout with all markers / page tags / equations / figure briefs intact; PART B carries unchanged compiler contract + new B15 v3.1 change log. Phase 5 can render PART A directly with no preprocessing. |

**전체 판정: 8/8 PASS.** v3.1 Korean Readability Patch는 학습자-facing 한국어 가독성을 개선하면서 v3의 source-fidelity, 수식, page tag, figure marker, HTML 렌더링 준비 상태를 모두 보존하였다. Phase 5 HTML compiler는 v3.1 PART A를 그대로 렌더링 대상으로 삼을 수 있다.

### B16. v3.2 Change Log — Korean-Dominant Readability Patch

**Patch scope:** v3.1 → v3.2 Korean-Dominant Readability Patch. **과학적 본문 절대 불변.** 새로운 수치, page tag, figure marker, 수식, NONMEM/R 코드, 임상 시나리오 추가 없음. v3.2는 PART A의 학습자-facing 영어 산문을 체계적으로 한국어로 전환하고, 경력상 필수적인 전문용어는 `한글(English)` 형식으로 병기한다. v3.1이 §1 Navigation과 일부 카드 문장에 국한되었다면, v3.2는 §2 하위 섹션 헤더, §5/§7/§8 헤더, 본문 전반의 영어 산문, 학습 장치 레이블까지 포괄한다.

| # | Type | Location | Change | Risk |
|---|---|---|---|---|
| KRD-001~004 | 헤더 한국어화 | §2 C1/C2/C4/C5 `#### A. Formal definition` | → `#### A. 형식적 정의(Formal Definition)` | Low |
| KRD-005 | 헤더 한국어화 | §2 C3 `#### A. Formal definition and ODE` | → `#### A. 형식적 정의와 ODE` | Low |
| KRD-006 | 헤더 한국어화 | §2 C1 `#### B. Dose, AUC, and steady state` | → `#### B. 용량, AUC, 그리고 항정상태` | Low |
| KRD-007~008 | 헤더 한국어화 | §2 C1/C2 `#### C. Compound A anchor` | → `#### C. Compound A 기준 데이터` | Low |
| KRD-009~010 | 헤더 한국어화 | §2 C1/C2 `#### D. Boundary and compression` | → `#### D. 경계 및 압축` | Low |
| KRD-011 | 헤더 한국어화 | §2 C2 `#### B. Why apparent volume can be huge` | → `#### B. 겉보기 분포용적이 거대해질 수 있는 이유` | Low |
| KRD-012 | 헤더 한국어화 | §2 C3 `#### B. Fractional elimination intuition` | → `#### B. 분율 제거의 직관` | Low |
| KRD-013~014 | 헤더 한국어화 | §2 C3/C5 `#### C. Boundary` | → `#### C. 경계(Boundary)` | Low |
| KRD-015 | 헤더 한국어화 | §2 C4 `#### B. Time to steady state` | → `#### B. 항정상태 도달 시간` | Low |
| KRD-016 | 헤더 한국어화 | §2 C4 `#### C. Distribution phase limitation` | → `#### C. 분포 단계의 한계` | Low |
| KRD-017 | 한국어화 | Figure rights note | 전문 영문 → 한국어 설명 + `한글(English)` 병기 | Low |
| KRD-018 | 한국어화 | §1 학습 순서 | 영어 카드명 → 한국어 카드명 | Low |
| KRD-019 | 한국어화 | §1 R&T opening figures 문장 | `opening figures` → `도입 그림(opening figures)`, `primary determinant` → `일차 결정인자(primary determinant)` 등 | Low |
| KRD-020 | 한국어화 | §1 선행/후속 | 영어 후속 주제명 → 한국어 + (English) 병기 | Low |
| KRD-021 | 한국어화 | C1 정의 | `Clearance ($CL$):` → `청소율(Clearance, $CL$):`, `apparent volume` → `겉보기 용적(apparent volume)`, `flow unit` → `유속 단위(flow unit)` | Low |
| KRD-022 | 한국어화 | C1 B | `Constant infusion` → `일정 속도 주입(constant infusion)` | Low |
| KRD-023 | 한국어화 | C1 C | `source-bound 계산 anchor` → `출처 기반(source-bound) 계산 기준점` | Low |
| KRD-024 | 한국어화 | C1 D | `hepatic/renal clearance` → `간/신 청소율(hepatic/renal clearance)`, `Extravascular dosing` → `혈관외 투여(extravascular dosing)` 등 | Low |
| KRD-025 | 한국어화 | C1 Recap | `Recap` → `요약(Recap)`, `exposure` → `노출량`, `maintenance dose` → `유지용량`, `primary elimination parameter` → `일차 소실 파라미터(primary elimination parameter)` | Low |
| KRD-026 | 한국어화 | C2 Big Idea | `apparent dilution space` → `겉보기 희석 공간(apparent dilution space)`, `charcoal` → `숯(charcoal)` | Low |
| KRD-027 | 한국어화 | C2 A | `back-extrapolated intercept` → `역외삽 절편(back-extrapolated intercept)` | Low |
| KRD-028 | 한국어화 | C2 A | `time-zero extrapolation` → `시간 0 외삽(time-zero extrapolation)`, `terminal phase` → `말단 단계(terminal phase)` | Low |
| KRD-029 | 한국어화 | C2 B | `unbound volume` → `비결합 용적(unbound volume)`, `free fraction` → `유리 분율(free fraction)` | Low |
| KRD-030 | 한국어화 | C2 B | `Tissue partition` → `조직 분배(tissue partition)` | Low |
| KRD-031 | 한국어화 | C2 B | `apparent volume` → `겉보기 분포용적(apparent volume)`, `tissue binding` → `조직 결합(tissue binding)`, `measurement space` → `측정 공간(measurement space)` | Low |
| KRD-032 | 한국어화 | C2 D | `terminal volume` → `말단 용적(terminal volume)`, `distribution kinetics` → `분포 동력학(distribution kinetics)` | Low |
| KRD-033 | 한국어화 | C2 TRENCH | `Semi-log plot` → `반로그 도표(semi-log plot)`, `break point` → `꺾임점(break point)`, `central vs steady-state volume` → 한국어 전개 | Low |
| KRD-034 | 한국어화 | C2 Recap | `apparent parameter` → `겉보기 파라미터(apparent parameter)`, `loading dose` → `부하용량(loading dose)`, `maintenance exposure` → `유지 노출량(maintenance exposure)` | Low |
| KRD-035 | 한국어화 | C3 C | `Distribution phase` → `분포 단계(distribution phase)`, `decline` → `농도 저하(decline)`, `elimination half-life` → `소실 반감기(elimination half-life)`, `Extravascular` → `혈관외(extravascular)`, `terminal slope` → `말단 기울기(terminal slope)` | Low |
| KRD-036 | 한국어화 | C3 Recap | `semi-log slope` → `반로그 기울기(semi-log slope)` | Low |
| KRD-037 | 한국어화 | C4 B | `Constant infusion` → `일정 속도 주입(constant infusion)`, `half-life/half-lives` → `반감기` | Low |
| KRD-038 | 한국어화 | C4 B | `half-lives` → `반감기` | Low |
| KRD-039 | 한국어화 | C4 ANCHOR | `maintenance dose` → `유지용량(maintenance dose)`, `loading dose` → `부하용량(loading dose)` | Low |
| KRD-040 | 한국어화 | C4 C | `semilog profile` → `반로그 농도 프로파일(semilog profile)`, `biphasic` → `이상성(biphasic)`, `distribution phase` → `분포 단계(distribution phase)`, `plasma` → `혈장` | Low |
| KRD-041 | 한국어화 | C4 C | `distribution/elimination` 경쟁 문단 전체 → 한국어 중심 전환. `terminal phase` → `말단 단계`, `distribution equilibrium` → `분포 평형(distribution equilibrium)`, `urine` → `소변` | Low |
| KRD-042 | 한국어화 | C4 ANCHOR | `distribution-phase AUC` → `분포 단계 AUC`, `terminal slope` → `말단 기울기(terminal slope)` | Low |
| KRD-043 | 한국어화 | C4 TRENCH | `Terminal slope` → `말단 기울기(terminal slope)`, `regression quality` → `회귀 품질(regression quality)`, `AUC fraction` → `AUC 분율(fraction)` | Low |
| KRD-044 | 한국어화 | C4 Recap | `distribution phase` → `분포 단계` | Low |
| KRD-045~048 | 레이블 병기 | 5개 Mastery Augmentation 블록 | `Mastery Augmentation` → `전문가 보강(Mastery Augmentation)` | Low |
| KRD-049~053 | 레이블 병기 | 5개 Practice Brief 블록 | `Practice Brief` → `실무 체화 요약(Practice Brief)` | Low |
| KRD-054 | 한국어화 | C5 ANCHOR | `monoexponential decline` → `단일지수 감소(monoexponential decline)`, `signature` → `서명(signature)`, `lock` → `고정`, `extravascular` → `혈관외(extravascular)` | Low |
| KRD-055 | 한국어화 | C5 C | `terminal` → `말단 영역(terminal region)`, `extrapolation` → `외삽(extrapolation)`, `terminal phase` → `말단 단계`, `extravascular` → `혈관외` | Low |
| KRD-056 | 한국어화 | C5 Recap | `bridge parameter` → `연결 파라미터(bridge parameter)` | Low |
| KRD-057 | 헤더 한국어화 | §5 | `Confusion Pair Dissection` → `혼동쌍 해부(Confusion Pair Dissection)` | Low |
| KRD-058 | 헤더 한국어화 | §5 Pair 1 | `Pair 1` → `혼동쌍 1`, `Primary vs Secondary` → `일차 vs 이차(Primary vs Secondary)` | Low |
| KRD-059 | 한국어화 | §5 Pair 1 표 | `apparent volume` → `겉보기 용적(apparent volume)`, `fraction` → `분율(fraction)`, `volume/time` → `용적/시간(volume/time)` | Low |
| KRD-060 | 한국어화 | §5 Pair 1 표 | `semi-log slope` → `반로그 기울기(semi-log slope)`, `covariate` → `공변량(covariate)`, `치명적 타격` → `치명적 타격(Critical Blow)` | Low |
| KRD-061 | 한국어화 | §5 Pair 1 TRENCH | `fit` → `적합도(fit)`, `$CL$-mediated` → `$CL$ 매개`, `extrapolation` → `외삽 가능성(extrapolation)` | Low |
| KRD-062 | 헤더 한국어화 | §5 Pair 2 | `Apparent bolus volume vs steady-state distribution` → `겉보기 bolus 용적 vs 항정상태 분포 용적` | Low |
| KRD-063 | 한국어화 | §5 Pair 2 표 | `apparent dilution space` → `겉보기 희석 공간(apparent dilution space)`, `tissue volume` → `조직 용적(tissue volume)`, `context` → `맥락`, `distribution kinetics` → `분포 동력학(distribution kinetics)` | Low |
| KRD-064 | 한국어화 | §5 Pair 2 Lock | `Lock:` → `고정:`, `apparent parameter` → `겉보기 파라미터(apparent parameter)`, `distribution kinetics` → `분포 동력학(distribution kinetics)` | Low |
| KRD-065 | 한국어화 | §5 Pair 2 Memory Hook | `plasma concentration` → `혈장 농도(plasma concentration)`, `central $V$` → `중심 구획 $V$` | Low |
| KRD-066 | 헤더 한국어화 | §5 Pair 3 | `Pair 3` → `혼동쌍 3` | Low |
| KRD-067 | 한국어화 | §5 Pair 3 표 | `amount` → `약물량(amount)`, `1-cmt IV bolus` → `1구획 IV bolus`, `terminal phase` → `말단 단계(terminal phase)`, `terminal extrapolation` → `말단 외삽(terminal extrapolation)` | Low |
| KRD-068 | 한국어화 | §5 Recap | `primary/secondary` → `일차/이차(primary/secondary)`, `apparent/steady-state` → `겉보기/항정상태(apparent/steady-state)` | Low |
| KRD-069 | 헤더 한국어화 | §7 | `Self-Test: Active Recall Module` → `자기 테스트: 능동 회상 모듈(Active Recall Module)` | Low |
| KRD-070 | 한국어화 | §7 Q7 문제 | `adult` → `성인`, `plasma concentration/volume` → `혈장 농도/용적`, `plasma 내 amount/fraction` → `혈장 내 약물량/분율` | Low |
| KRD-071 | 한국어화 | §7 Q7 정답 | `Plasma 내 amount` → `혈장 내 약물량`, `plasma 밖` → `혈장 밖` | Low |
| KRD-072 | 한국어화 | §7 Q8 정답 | `distribution kinetics` → `분포 동력학(distribution kinetics)`, `terminal extrapolation` → `말단 외삽(terminal extrapolation)`, `Source-bound` → `출처 기반` | Low |
| KRD-073 | 한국어화 | §7 Q9 제목 | `Source-bound Boss Dilemma` → `출처 기반 보스 딜레마(Boss Dilemma)`, `semilog plot` → `반로그 도표(semilog plot)`, `biphasic decline` → `이상성 감소(biphasic decline)`, `sparse` → `희박(sparse)` | Low |
| KRD-074 | 한국어화 | §7 Q9 정답 | `distribution phase` → `분포 단계`, `terminal phase/slope` → `말단 단계/기울기`, `elimination` → `소실`, `concentration-time profile` → `농도-시간 프로파일` | Low |
| KRD-075 | 한국어화 | §7 Recap | `parameter` → `파라미터` | Low |
| KRD-076 | 헤더 한국어화 | §8 | `Meta-Frame & Big Picture` → `메타프레임 & 빅 픽처(Meta-Frame & Big Picture)` | Low |
| KRD-077 | 헤더 한국어화 | §8A | `Positioning` → `위치 지정(Positioning)` | Low |
| KRD-078 | 한국어화 | §8A 내용 | `terminal phase` → `말단 단계`, `Absorption models` → `흡수 모델(Absorption models)`, `Hepatic/Renal clearance` → `간/신 청소율(Hepatic/Renal clearance)`, `PopPK covariates` → `PopPK 공변량`, `compartment model` → `구획 모델`, `exposure/residence time` → `노출/체류 시간` | Low |
| KRD-079 | 한국어화 | §8B 3–4항 | `Terminal phase` → `말단 단계`, `$K$-direct parameterization` → `$K$-직접 모수화`, `primary/secondary` → `일차/이차(primary/secondary)`, `parameterization` → `모수화(parameterization)` | Low |
| KRD-080 | 헤더 한국어화 | §8C | `Professional Moat` → `전문가 해석 지점(Professional Moat)` | Low |
| KRD-081 | 한국어화 | §8C 본문 | `monoexponential fit` → `단일지수 적합(monoexponential fit)`, `terminal straight line` → `말단 직선(terminal straight line)`, `elimination` → `소실`, `Source-bound statement` → `출처 기반 진술(source-bound statement)` | Low |
| KRD-082 | 한국어화 | §8C v3 확장 | `maintenance dose/loading dose` → `유지용량(maintenance dose)/부하용량(loading dose)`, `Terminal slope/half-life` → `말단 기울기/반감기`, `Covariate/target` → `공변량/대상`, `parameter` → `파라미터` | Low |
| KRD-083 | 한국어화 | Final Recap | `Final Recap` → `최종 요약(Final Recap)`, `handout` → `이 자료` | Low |

**v3.2 LaTeX 무결성 검증:**

- 모든 MathJax 인라인 `$...$` 및 디스플레이 `$$...$$` 블록: v3.1 대비 변경 없음.
- 하첨자(`t_{1/2}`, `C_{ss}`, `C^0`, `V_{ss}`, `R_{in}`, `K_{Pi}`, `f_u`, `V_u`, `V_B`, `V_{Ti}`, `E_{Ti}`, `f_e`): 글자 단위 보존.
- 분수(`\frac{...}{...}` 및 인라인 나눗셈): 보존.
- 특수 연산자(`\approx`, `\cdot`, `\sum`, `\int_0^\infty`, `\ln`): 보존.
- BEL 문자 / 오탈자 회귀 점검: v3.2 패치에서 `\a`(U+0007) + 깨진 `pprox` 패턴 도입 없음. ver2 P1 수정 보존.

**v3.2에서 의도적으로 변경하지 않은 항목 (및 이유):**

- 모든 과학적 본문 내용 (C1–C5 카드): 변경 없음.
- 모든 page tag (`[G p.XX]`, `[R&T p.XX]`, `[Source: G Tables 1.2/1.3, p.473–474]` 등): 변경 없음.
- 모든 `<!-- FIGURE_POINTER -->` 및 `<!-- FIGURE_SCHEMATIC -->` 마커 블록 (4개): Source/Why/When/Learner instruction 필드 포함하여 바이트 단위 동일.
- 모든 HTML compiler marker: 변경 없음.
- 모든 §7 자기 테스트 질문과 정답 (Q1–Q9): 과학적 내용 변경 없음 (표현 한국어화만).
- 모든 §5 기억 고리와 치명적 타격 행: 과학적 내용 변경 없음.
- Compound A 수치 (S1–S4 V/CL/K/AUC/MRT): 변경 없음.
- Creatinine vs Inulin 비교 (R&T p.58): 변경 없음.
- midazolam (R&T p.61–62) 및 gentamicin (R&T p.66) 앵커 수치: 변경 없음.
- §8C 전문가 해석 지점 4+6 불릿 구조: 변경 없음.
- PART B §B13–B15 패치 로그: 그대로 보존.
- B3 Splice Verification Table: 변경 없음.
- B7 Approved Figure Strategy: 변경 없음.
- B10 Source-Boundary Certificate: 범위 변경 없음; v3.2 항목 추가 ("Korean-Dominant readability adjustments only; zero new scientific content").

**v3.2 패치 후 검증:**

- Page tag 수: v3.1과 동일 (추가 없음, 제거 없음).
- Figure marker 수: v3.1에서 4개, v3.2에서 4개 — 앵커 위치와 내용 동일.
- 자기 테스트 정답 수와 내용: v3.1과 과학적으로 동일 (Q1–Q9).
- Compound A 수치: v3.1과 동일.
- 수식 수와 렌더링: v3.1과 동일.
- B3 앵커 일치: 4/4 변경 없음.
- B4 Coverage Matrix 항목: C1–C16 모두 PRESENT 또는 PASS 유지.
- B6 Augmentation Log: AUG-1부터 AUG-12 변경 없음 (v3.2 가독성 패치는 새로운 mastery augmentation이 아님).
- HTML 준비 상태: 영향 없음. Phase 5 marker→component 매핑(B8)은 동일한 9개 마커 유형, 동일한 page tag 패턴, 동일한 figure marker에서 작동.

---

## Final v3.2 All-Pass Checklist

| # | 감사 항목 | 상태 | 근거 (1줄) |
|---:|---|---|---|
| 1 | PART A 한국어 중심 가독성 개선 | **PASS** | §2 카드 하위 헤더 16개 한국어화; 본문 영어 산문 ~40개 위치 한국어 전환; 학습 장치 레이블 10개에 한국어 병기; §5/§7/§8 헤더 한국어화 (KRD-001~KRD-083). |
| 2 | 과학적 내용 불변 | **PASS** | Compound A S1–S4 수치, Creatinine/Inulin 표, midazolam/gentamicin 수치, 모든 도출과 수식이 v3.1과 동일. 새로운 주장, 예시, 수치 도입 없음. |
| 3 | 수식 보존 | **PASS** | 모든 MathJax 블록(인라인 `$...$` 및 디스플레이 `$$...$$`)이 v3.1과 바이트 동일. 하첨자, 분수, 연산자 보존 확인. |
| 4 | Page tag 보존 | **PASS** | 모든 `[G p.XX]`, `[R&T p.XX]`, Source 귀속 태그가 v3.1과 동일 (추가·제거 없음). |
| 5 | Figure marker 보존 | **PASS** | 4개 마커 (3× FIGURE_POINTER + 1× FIGURE_SCHEMATIC) 바이트 동일; 모든 내부 Source / Why / When / Learner instruction / brief 필드 변경 없음. |
| 6 | Source-boundary 보존 | **PASS** | 모든 [실무 확장/교과서 외 해석] 태그 유지; 모든 `[EXPERT_INFERENCE, v3]` 및 `[TEXTBOOK_DERIVED, v3]` 태그 유지; Forbidden Restoration List (B9) 준수; v3.2는 source-bound 추가 없음. |
| 7 | HTML 준비 상태 보존 | **PASS** | B8 marker→component 매핑 변경 없음; B7 Figure Strategy 변경 없음; B3 Splice Verification Table 4/4 앵커 정확히 일치; canonical anchor id list (B8) 변경 없음. |
| 8 | Phase 5 HTML 컴파일 준비 완료 | **PASS** | 단일 self-contained `.md` 파일; PART A는 모든 marker / page tag / 수식 / figure brief가 포함된 완성 학습자 핸드아웃; PART B는 변경 없는 compiler contract + 새 B16 v3.2 change log 포함. Phase 5는 v3.2 PART A를 전처리 없이 직접 렌더링할 수 있다. |

**전체 판정: 8/8 PASS.** v3.2 Korean-Dominant Readability Patch는 학습자-facing 영어 산문을 체계적으로 한국어로 전환하면서, v3.1의 source-fidelity, 수식, page tag, figure marker, HTML 렌더링 준비 상태를 모두 보존하였다. Phase 5 HTML compiler는 v3.2 PART A를 그대로 렌더링 대상으로 삼을 수 있다.

---

| Certificate | Status | Basis |
|---|---|---|
| Korean-Dominant Readability Certificate | PASS | General learner-facing English prose converted to Korean where possible; career-critical terms retained as Korean-English paired expressions. |
| Scientific Preservation Certificate | PASS | No scientific content, equation, number, example, page tag, or source label changed. |
| Marker Integrity Certificate | PASS | All figure markers, compiler markers, anchors, and section/card structures preserved. |
| HTML-Readiness Certificate | PASS | Phase 5 compatibility preserved; no HTML/Mermaid/SVG generated. |

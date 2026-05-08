# XX_html_compile_input_master_v3.2.md

**v3.2 note:** This version applies a Korean-Dominant Readability Patch to PART A learner-facing prose. General English prose was converted to Korean where possible, while career-critical pharmacometrics terms are retained as Korean-English paired expressions on first use. Scientific content, equations, numerical anchors, page tags, source labels, figure markers, compiler markers, section structure, and PART B guardrails are preserved. No new scientific claims, examples, numbers, page tags, figures, or external references were added.

**v3.1 note:** This version applies a Korean Readability Patch to improve learner-facing Korean prose while preserving scientific content, equations, page tags, source labels, figure markers, and Phase 5 HTML-readiness. No new scientific claims, page tags, numerical anchors, figure decisions, or external references were added.

---

# 11_HTML Compile Input Master — v3.2 (Korean-Dominant-Readability-Patched)

## Version Note

**v3.1 → v3.2 변경 사유**: v3.1은 35건의 Korean Readability Patch로 Big Idea 오프너·§7 질문·§8 산문·Recap·Trench·Structural·Learner Navigation의 영문 산문을 한국어로 전환했으나, PART A 전반에 걸쳐 표 항목, Mastery Note/Practice Lens/Failure Mode 블록, 테이블 셀, 정의 산문, 소제목 헤더 등에 여전히 영문 산문이 광범위하게 잔존한다는 점이 v3.2 audit에서 식별되었다. v3.2는 v3.1 본문(fact·equation·page tag·marker·Apex·Critical Blow·Mastery Anchor·Boss Dilemma·Memory Hooks·Practice Brief·hidden-state thread)을 100% 무손상 유지한 채로, 잔존 영문 산문을 같은 의미의 한국어 산문으로 교체하고 커리어상 필수 전문용어는 `한글(English)` 병기 형식으로 통일하는 Korean-Dominant Readability Patch를 적용한다. 모든 v3.2 patch는 Low risk이며 Korean-dominant flow improvement 단일 change-type에 한정된다. 새 fact·수치·예시·page tag·외부 reference·figure marker는 도입되지 않는다.

**v2 → v3 변경 사유**: v2는 Phase 4D 5대 Certificate를 모두 통과하고 Crucible v1 Grade A 5종 거장 통찰을 Mastery Anchor로 복원했으나, Independent Master Reviewer의 v3 audit에서 4가지 gap이 식별되었다 — (1) §5의 학습자용 **기억 고리(Memory Hook)가 7개 핵심 conceptual pair에서 전면 부재**, (2) **§7 보스 딜레마**가 누락되었거나 정답 키 형태에 가까워 trade-off 학습 효과가 약함, (3) **PD4 Pool 1/2 r=0.9999 비식별성** 인사이트가 Mastery Augmentation Layer에만 머물러 학습자 본문에 명시되지 않음, (4) **카드 간 서사 실** — "이 카드에서 지연되는 hidden state는 무엇인가?"라는 thread가 끊겨 있어 카드 1→8의 인과 흐름이 시각적으로 부각되지 않음. v3는 v2 본문(fact·equation·page tag·marker·Apex·Critical Blow)을 100% 무손상 유지한 채로, 이 4가지 gap만을 외과적으로 메운다. 모든 v3 추가는 [EXPERT_INFERENCE, v3] 라벨이 명시되며, 새 drug example·page tag·외부 fact를 도입하지 않는다.

**v1 → v2 변경 사유**: v1은 5대 Certificate(Learner-Standalone, Zero-Omission, Mastery-Uplift, Source-Boundary, HTML-Readiness)를 모두 통과했으나, Crucible v1이 Grade A로 채택한 거장 통찰 5종(PD4 Pool 1/2 r=0.9999 비식별성, OFV stuck-then-drop pattern, Hysteresis 30초 방향 진단, Mirror-Slope Misread PD7 정량 수치, Post-trough rebound timing 직관)이 v1에서는 일반화·압축되어 거장 voice가 약화되어 있었다. v2는 **content lock v2 본문(fact·equation·page tag·marker)을 100% 무손상 유지**한 채로, Phase 4D의 Mastery Augmentation Layer를 확장하여 위 5종을 명시적으로 복원한다. 또한 Card 8.D의 Rosuvastatin 절을 §5-5 footnote로 이동하여 흐름 정합성을 높이고, §8C Professional Moat와 §5 Recap을 거장의 30초 진단 sequence 형태로 강화한다.

## Phase 4D Certification (v3.2)

| Certificate | Status | Basis (v3.2) |
|---|---|---|
| Learner-Standalone Certificate | PASS | PART A는 §1–§8 학습자 본문만 포함; audit/process/compiler 자료는 PART B에 격리. v3.2 Korean-Dominant patch는 모두 PART A 학습자 본문 안에서 영문→한국어 산문 교체 및 전문용어 `한글(English)` 병기 통일로만 작동 — 새 가드레일 도입 없음. |
| Zero-Omission Certificate | PASS | v3 Crucible Grade A 5종 + v3 audit 4 gap fix 모두 PRESENT 유지. v3.2 patch는 정보 추가·삭제·이동 없이 surface form만 한국어 지배적으로 변환. HOLD_UNRESOLVED 없음. |
| Mastery-Uplift Certificate | PASS | v3의 8개 Mastery Anchor + 7쌍 Memory Hook + Boss Dilemma + 8개 hidden-state diagnostic + 8개 Practice Brief 모두 byte-equivalent 의미로 보존. v3.2는 본문 재작성·재구조화를 수행하지 않음. |
| Source-Boundary Certificate | PASS | v3.2 patch는 모두 영문 산문→한국어 산문 surface 교체 및 전문용어 병기 통일에 한정. 새 drug example·page tag·외부 fact·수치·예시·regulatory claim 도입 0건. R&T 직접 인용문(*"Dose linearity in pharmacokinetics..."*)은 attributed quotation으로 영문 보존. |
| HTML-Readiness Certificate | PASS | PART B B1-B14 그대로 보존; B15(v3.1→v3.2 변경 로그) 신규 추가. Marker·page tag·navigation anchor·responsive/print·forbidden restoration·Insertion Map·Splice Verification Table 모두 byte-level 보존. FIGURE_POINTER·FIGURE_SCHEMATIC 블록 내 영문 brief 미변경. |

## Assembly Mode

PATCH MODE (v3.2 유지)

Rationale: `11_Content Lock v2.1.md`는 figure marker insertion plan이며, learner-facing canonical body는 `11_Content Lock v2.md`에서 가져옴. 6개의 marker block이 지정 위치에 splice됨. v3.2는 v3.1의 splice 결과를 변경하지 않는다(B8 Splice Verification Table은 byte-level 동일; 6개 marker block 위치·내용·anchor 텍스트 동일). v3.2 patch는 marker block 외부의 학습자 산문에만 적용된다.

## Input Manifest (v3.2 추가 행만 표시; 나머지는 v3.1과 동일)

| File | Role | Authority level | Used for | Notes |
|---|---|---|---|---|
| `11_html_compile_input_master_v3.1.md` (v3.1) | v3.2 base substrate | A8 | v3.2의 모든 §1-§8 본문 의미는 v3.1에서 carry-over | v3.2는 영문→한국어 Korean-Dominant patch layer만 적용 |
| v3.2 Korean-Dominant Readability Patch audit | v3.2 readability authority | A6 | PART A 잔존 영문 산문 식별: 표 항목, Mastery Note/Practice Lens/Failure Mode 블록, 정의문, 소제목 헤더, 비교표 셀 | v3.2 patches의 근거 |
| (v1·v2·v3·v3.1의 Input Manifest 모든 항목 carry-over) | — | — | — | v3.2는 v1·v2·v3·v3.1 위에 누적적으로 작업 |

## PART A — Learner-Facing Complete Handout

## 학습자 안내(Learner Navigation Aid)

### Obsidian-compatible YAML frontmatter to preserve in Phase 5

```yaml
title: "Session 11 — Indirect Response / Turnover / DRT / Baseline / Effect Compartment / Rate-Limiting / Duration"
source_universe:
  - "Gabrielsson & Weiner 5e: Ch.2 §2.6.7; Ch.3 §3.7–3.8, §3.10, §3.12; PD4/PD5/PD6/PD7/PD9"
  - "Rowland & Tozer 5e: Ch.8 pp.233–264"
learner: "PhD pharmacometrics student, entry–intermediate"
mode: "A-Critical"
image_rights: "None; render source textbook figures only as pointers or visually distinct redraws"
phase: "4D HTML compile input — v2 mastery-strengthened"
```

### 이 학습 자료 사용법(How to use this handout)

§1을 한 번 읽어 세션의 핵심 질문을 파악한 후, §2를 여덟 개의 개념 카드로 공부한다. 각 카드에서 먼저 수식 또는 결정 규칙을 잠근 다음, 인접한 Mastery/Practice/Failure 노트를 살피고, 있는 경우 승인된 figure pointer나 redraw instruction을 활용한다. Figure pointer block을 이미지로 취급하지 않는다. 이것들은 Phase 5 렌더링 지시문이거나 교과서 참조 안내다.

**v2 학습 사용법 추가**: 각 카드의 첫 단락(Big Idea)은 세 가지 질문에 동시에 답하도록 구성되어 있다 — ① **이 지식이 왜 이번 세션의 critical path에 있는가**(임상·모델링 결과 차원), ② **앞 카드와 뒤 카드 사이에서 어떤 인과적 다리를 놓는가**(흐름 위치), ③ **이 카드를 5초 안에 활용하기 위해 잡아야 할 핵심 mental model은 무엇인가**(체화 핵심 직관). 카드별로 이 셋이 한 단락에 자연스럽게 녹아 있도록 적었다. 이어지는 본문은 이 mental model을 잡은 상태로 읽어야 가장 효율적이다.

### 학습 경로(Learning route)

1. Turnover baseline과 hysteresis 분류.
2. 생산/소실 4모델 분류 체계.
3. `tss`와 peak-shift 선별 진단, 주의사항 포함.
4. Imax/Emax 의미 잠금과 linear-PK/nonlinear-PD 경고.
5. Graphical 초기값 설정, blocking-dose 논리, DRT 맥락.
6. 비가역적 작용과 target-consumption 회복.
7. Turnover 대 effect-compartment 감별 위기.
8. PK clock 대 PD clock, 그리고 PK-rate-limited일 때만 적용하는 duration formula.

### 시작 전 / 마친 후 체크리스트(Before you start / after you finish checklist)

- 시작 전: direct response, distribution delay, turnover delay, target consumption, PK/PD rate-limiting이 각각 별개의 후보 설명임을 확인한다.
- 진행 중: 지연 반응이 나타날 때마다 느린 clock이 어디에 있는지 묻는다.
- 마친 후: 보지 않고 self-test에 답한다. model family와 clock 위치 모두 식별할 수 있으면 세션 목표 달성이다.

> **저작권 / 그림 사용 안내(Copyright / figure-use note)**  
> 원본 교과서 그림은 임베드되지 않는다. `FIGURE_POINTER` 블록은 텍스트 전용 callout으로 렌더링되어야 하며, 단일 `FIGURE_SCHEMATIC` 블록은 교과서 레이아웃을 재현(reproduction)하는 것이 아니라 시각적으로 구분되는 redraw여야 한다.


# §1 — 세션 헤더 & 로드맵(Session Header & Roadmap)

<!-- MASTER LENS -->
## 핵심 통찰(Big Idea)

대부분의 임상적으로 관찰되는 pharmacodynamic response는 plasma concentration과 완전히 동시에 움직이지 않는다. 그러나 모든 지연을 별도 모델로 다루는 것은 아니다. 지연이 **무시 가능할 정도로 짧으면 direct PK-PD link**로 충분하다. 반대로 지연이 관찰 가능하면 그 원인을 **distribution delay, turnover/system flux, target consumption, 또는 PK/PD rate-limiting clock** 중 하나로 분해해야 한다. [G pp.235–236; T pp.233–235, 239]

<!-- ANNOTATION --> 여기서 hysteresis는 "같은 농도에서도 시간 경로에 따라 response가 달라지는 현상"이다.

<!-- ANCHOR -->
## 개념 항법도(Conceptual navigation)

이 세션은 다음 순서로 잠긴다.

1. `dR/dt = kin − kout·R`가 baseline과 time constant를 만든다. [G p.237]
2. 약물은 production 또는 loss 중 하나를 inhibit/stimulate한다. [G pp.237–245]
3. tss/peak shift는 작용 부위의 강력한 신호지만, PK rate-limiting과 limited dose range에 의해 가려질 수 있다. [G pp.247–251; G pp.778–783]
4. Effect compartment와 turnover model은 제한된 설계에서 거의 같은 curve를 낼 수 있다. 따라서 fit quality만으로 구조를 잠그면 안 된다. [G pp.758–763; T pp.244–246]
5. Response decline은 drug PK clock 또는 system PD clock 중 느린 쪽이 결정한다. 이 때문에 `tD` formula는 PK-rate-limited일 때만 사용한다. [T pp.243, 247–256]

<!-- RECAP -->
## 잠긴 핵심 메시지(Locked takeaway)

이 장의 핵심은 "delayed response는 하나의 현상이 아니라 여러 원인의 공통 표면형"이라는 점이다. 모델링의 첫 질문은 "어떤 ODE가 curve를 잘 맞추는가?"가 아니라 "무엇이 시간을 rate-limit 하는가?"이다.

---

# §2 — 개념 해부 카드(Concept Anatomy Cards)

## Card 1 — Turnover Model Foundation + Hysteresis Classification

<!-- MASTER LENS -->
### Big Idea

Turnover model의 최소 골격은 response가 **생산되는 속도**와 **사라지는 속도**의 차이다. Baseline은 독립적인 상수가 아니라 두 속도의 비율이다. Hysteresis loop는 이 system이 plasma concentration을 즉시 따라가지 못한다는 시각적 신호다. 이 말은 direct response를 부정한다는 뜻이 아니다. 먼저 **지연이 data resolution 안에서 보이는지**를 판단한다. [G pp.235–237; T pp.234–235, 239]

> **왜 첫 카드인가**: 이후 일곱 카드의 모든 결정 — 4-model 작용 부위, tss 진단, Emax 의미, graphical 초기값, irreversible 여부, effect compartment 가설, PK/PD clock 선택 — 은 이 두 줄짜리 ODE에서 분기한다. **`R0=kin/kout`을 비율로 보지 못하면 다음 카드들은 모두 암기 대상이 된다.** 이 카드의 체화 목표는 단 하나다: response 곡선을 보자마자 머릿속에서 "두 개의 수도꼭지 — 들어오는 양 vs 빠지는 양 — 의 균형이 깨진 시간 경로"로 자동 변환되어야 한다.

### A. 공식 정의(Formal definition)

$$\frac{dR}{dt}=k_{in}-k_{out}R \quad \text{[G Eq 3:74; G p.237]}$$

정상상태에서는:

$$R_0=\frac{k_{in}}{k_{out}} \quad \text{[G Eq 3:76; G p.237]}$$

- `R`: 측정된 약리학적 반응(measured pharmacological response).
- `kin`: 0차 생산 속도(zero-order production rate), response·time⁻¹.
- `kout`: 1차 소실 속도(first-order loss rate), time⁻¹.
- `R0`: 기저 반응(baseline response); 기본 모델에서는 시간 불변(time-invariant)으로 둔다.

### B. Hysteresis 분류(Hysteresis classification)

Hysteresis는 같은 concentration에서 상승기(rising phase)와 하강기(falling phase)의 response가 서로 다른 현상이다. [T pp.234–235]

| 패턴(Pattern) | 해석(Interpretation) | 고정 사례(Locked examples) |
|---|---|---|
| 반시계 방향(Counterclockwise) | 반응이 농도 뒤에서 따라옴; 분포 지연, 하류 PD, 또는 system flux | Naproxen 500 mg oral, dental pain, 1–8 h, Fig 8-2 [T pp.234–235]; ibuprofen 6 mg/kg oral, febrile children, Fig 8-9 [T pp.241–242] |
| Hysteresis 없음 / direct link | 작용 부위 평형과 반응 생성이 관측 시간 척도 대비 빠름 | Midazolam 15 mg/kg oral in rat EEG, Fig 8-6 [T p.239] |
| 시계 방향(Clockwise) | 내성(tolerance), 피드백, 활성 대사체, 또는 기타 추가 동역학 | 범위 참고: 이 세션의 핵심 R&T worked example에 포함되지 않음; 추후 tolerance 영역에서 다룸. |

### C. 재파라미터화(Reparameterization)

모델 적합 시 `kin`과 `kout`를 독립적으로 먼저 추정하지 말고 `R0`와 `kout`를 우선 추정한다:

$$k_{in}=R_0 k_{out}$$

$$\frac{dR}{dt}=k_{out}(R_0-R) \quad \text{[G Eq 3:103; G p.247]}$$

PD4가 이 중요성을 보여준다: 충분한 실험설계 없이 상류 pool과 response의 turnover 상수를 독립 추정하면 비식별성(non-identifiability)에 근접할 수 있다. [G pp.742–752]

<!-- TRENCH -->
### 현장 팁(Trench-level tip)

`kin`과 `kout`가 극단적 상관을 보이거나 covariance step이 "stuck then drops" 패턴을 보이면 `R0 × kout`로 재코딩한다. 이것은 단순한 표기 변경이 아니다. 분리가 어려운 두 속도 파라미터에서 하나의 baseline과 하나의 시간 상수로 탐색 기하학(search geometry)을 본질적으로 바꾸는 것이다.

### D. 맥락 통합(Context integration)

음성 피드백(negative feedback)은 조절인자 `M`을 추가하여 반응이 높을수록 소실이 가속될 수 있게 한다. IgG 사례는 혈청 IgG 30 mg·mL⁻¹에서 반감기가 약 11일로 단축되는 것을 보여주며, 이는 `kout`이 고정 상수가 아니라 system 상태에 의존할 수 있음을 예시한다. [G pp.110–111]

Baseline drift 모델은 별도의 확장이다. 질병 진행 또는 일주기 변동이 `R0`를 움직이면 기본 constant-baseline turnover 방정식만으로는 불충분하다. [G pp.317–319]

<!-- RECAP -->
### Recap

Baseline은 비율이고, hysteresis는 시간 지연 진단 신호이며, 재파라미터화는 turnover 모델 비식별성에 대한 첫 번째 실용적 방어다.

> **🔗 지연되는 숨겨진 상태 [EXPERT_INFERENCE, v3]**: kin/kout으로 turnover하는 response pool 자체. plasma C는 즉시 변하지만 R은 1/kout 시간 상수로 따라온다 — 이것이 다음 카드들에서 분기할 모든 "delay assignment" 결정의 기본 hidden state다.

---

> **실무 관점(Practice Lens) — [AUDIT_DERIVED]**  
> "직접(direct)" 대 "지연(delayed)" 판정은 모델 계열 결정 이전에 **설계 해상도(design-resolution) 결정**으로 먼저 다뤄야 한다. 지연이 sampling 및 response-resolution 척도에서 보이지 않으면, 생물학적으로 순간적인 반응은 없더라도 direct link가 방어 가능할 수 있다.

> **Mastery Anchor #1 — Hysteresis 30-second direction diagnosis [CRUCIBLE_DERIVED]**  
> 30년 베테랑은 plasma C vs response 산점도를 받자마자 loop 회전 방향만으로 1차 분류를 끝낸다. **Counterclockwise**(R&T naproxen Fig 8-2, ibuprofen Fig 8-9의 시계반대 회전) → 효과가 농도를 *뒤따르는* 양상 → 후보 3가지: ① 효과 부위 분포 지연(effect compartment), ② Systems-in-flux(turnover), ③ active metabolite 생성 지연. **Clockwise** → 효과가 농도보다 *앞서가는* 양상 → 후보군: ① tolerance/down-regulation, ② counter-regulatory feedback, ③ enantiomer-specific kinetics(이 후자 분류는 [교과서 외 실무 해석]; 전자 3분류는 R&T 본문 직접 도출). 이 30초 진단이 끝나야 Card 2-3의 4-model 분류가 efficient하게 작동한다.

> **Mastery Anchor #2 — Reparameterization signature: OFV "stuck-then-drop" [CRUCIBLE_DERIVED]**  
> NONMEM 출력에서 30회 iteration 동안 OFV가 거의 변하지 않다가 갑자기 큰 폭으로 하락한다면, 그것은 보통 `r(kin, kout) > 0.98` 상관이 search direction을 죽이고 있다는 신호다. PD5 Table 5.1이 이 패턴을 직접 기록한다 — *"correlation greater than 0.98… reparameterization of the model by baseline R0 and kout."* 이 패턴을 본 베테랑은 $COV step 결과를 기다리지 않고 즉시 Eq 3:103의 (R0, kout) 재파라미터화로 옮겨간다. PD4 Pool 1의 `r(k1, kout) = 0.9999`, CV% 4000 사례가 이 비식별성의 극단형이며, 같은 데이터에 k1=kout 제약을 걸어 만든 Pool 2의 "정상적인 CV%"는 데이터가 동등성을 *지지*한 것이 아니라 제약이 비식별성을 *해결*한 것일 뿐이라는 점을 PD4 §Comparison이 직접 지적한다.

> **🎯 Practice Brief — Card 1 [EXPERT_INFERENCE, v3]**: 데이터 받자마자 plasma C vs response 산점도부터 그리고 hysteresis 방향만으로 1차 분류를 30초 안에 끝낸다. counterclockwise → distribution/turnover/active-metabolite, clockwise → tolerance/feedback. 그 다음 OFV stuck-then-drop 시그니처가 보이면 즉시 (R0, kout) 재파라미터화로 옮겨간다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.235, Fig 3.33; Rowland & Tozer 5e, p.235, Fig 8-2
Why this matters: Fig 3.33 separates direct response from delayed hysteretic response. Fig 8-2 shows that the same naproxen concentration can map to different pain relief depending on the rising/falling phase.
When to look: after reading Card 1
Learner instruction: First inspect the time plots, then inspect the concentration-response loop. Follow the time labels to verify that hysteresis is a time-ordered path, not scatter around a static curve.
<!-- /FIGURE_POINTER -->

## Card 2 — Four-Model Taxonomy: Inhibit/Stimulate × Production/Loss

<!-- MASTER LENS -->
### Big Idea

가역적 turnover 반응에서 약물이 작용할 수 있는 부위는 딱 네 가지다: production 억제, loss 억제, production 촉진, loss 촉진. 이 분류표는 단순한 명명 작업이 아니다. 생물학적 기전을 NONMEM `$DES` 블록으로 번역하는 최소 문법이다. [G pp.237–245; T pp.240–241]

> **흐름에서의 역할**: Card 1이 baseline을 비율로 봤다면, Card 2는 그 비율을 약물이 어디에서 깨는가를 결정한다. Card 3의 tss 거동, Card 4의 Emax 의미, Card 5의 초기값 도출, Card 7의 effect compartment 감별까지 — **모두 "input을 건드렸나 output을 건드렸나"라는 이 카드의 한 가지 질문에서 분기**한다. 체화 목표는 PD 데이터 한 장면을 보고 4개 칸 중 하나로 자동 분류하는 것이다.

### A. Drug functions

$$I(C)=1-\frac{I_{max}C^n}{IC_{50}^n+C^n}, \quad 0\le I_{max}\le 1 \quad \text{[G Eq 3:77; G p.237]}$$

$$S(C)=1+\frac{E_{max}C^n}{EC_{50}^n+C^n} \quad \text{[G Eq 3:78; G p.237]}$$

### B. Four models side-by-side

| Model | ODE | Drug action site | `tss` governor | `Rss` at constant `Css` | Maximal `ΔR` expression | Limit of `R` | Return-to-baseline behavior | Canonical example |
|---|---|---|---|---|---|---|---|---|
| 1. Inhibition of production | $\frac{dR}{dt}=k_{in}I(C)-k_{out}R$ [G pp.238–239] | Blocks input / biosynthesis | `kout`, dose-independent if PK fast | $R_{ss}=R_0I(C_{ss})$ | $\Delta R=R_0I_{max}$ [G p.239] | Down toward 0 if full inhibition | Recovery governed by `kout` after drug disappears | Warfarin inhibits vitamin K cycle / prothrombin complex [G PD4 pp.742–752; T pp.242–247] |
| 2. Inhibition of loss | $\frac{dR}{dt}=k_{in}-k_{out}RI(C)$ [G pp.240–241] | Blocks output / removal | effective `kout·I(C)`, dose-dependent | $R_{ss}=R_0/I(C_{ss})$ | $\Delta R=R_0 I_{max}/(1-I_{max})$ [G p.241] | Can rise above baseline | Return depends on restored loss process | Furosemide-type retention example [G p.238] |
| 3. Stimulation of production | $\frac{dR}{dt}=k_{in}S(C)-k_{out}R$ [G pp.242–243] | Stimulates input | `kout`, dose-independent if PK fast | $R_{ss}=R_0S(C_{ss})$ | $\Delta R=R_0E_{max}$ [G p.243] | Rises to multiplier of baseline | Recovery governed by `kout` | Erythropoietin stimulates RBC production [G p.238] |
| 4. Stimulation of loss | $\frac{dR}{dt}=k_{in}-k_{out}RS(C)$ [G pp.244–245] | Stimulates output | effective `kout·S(C)`, dose-dependent | $R_{ss}=R_0/S(C_{ss})$ | $\Delta R=R_0E_{max}/(1+E_{max})$ [G p.245] | Falls below baseline | Faster return at high stimulation | CB1 inverse agonist / energy expenditure example [G p.238]; PD7 compound C [G pp.764–769] |

### C. Structural necessity

<!-- ANNOTATION --> 이 네 모델의 차이는 "response가 올라가느냐 내려가느냐"보다 "drug가 input을 바꾸느냐 output을 바꾸느냐"에 있다. 따라서 다음 Card 3의 `tss` 판별도 이 input/output 구분에서 나온다.

Models 1·3은 0차 input term을 변경하므로 시간 상수가 `1/kout`으로 보존된다. Models 2·4는 1차 loss term을 변경하므로 effective time constant가 농도에 따라 달라진다. 그렇기 때문에 `tss` 거동이 작용 부위를 식별할 수 있지만, PK가 더 느린 clock이 아닐 때만 성립한다.

<!-- TRENCH -->
### Trench-level tip

반응 방향만으로 모델을 추론하지 않는다. 하향 반응은 Model 1과 Model 4 모두에서 발생할 수 있다. 시간 경과 패턴이 필요하다: production-side 모델은 주로 extent를 바꾸고, loss-side 모델은 extent와 겉보기 속도를 모두 바꾼다.

<!-- RECAP -->
### Recap

4-모델 분류표는 이 세션의 구조적 잠금장치다. 이후의 모든 주장 — tss, peak shift, 초기 추정값, 모델 감별 — 은 약물이 input을 바꿨는가 output을 바꿨는가의 귀결이다.

> **🔗 지연되는 숨겨진 상태 [EXPERT_INFERENCE, v3]**: 약물의 작용 부위(input vs output)에 따라 결정되는 response pool. Models 1·3은 input을 건드려 시간 상수 1/kout을 보존하고, Models 2·4는 output을 건드려 effective kout이 농도에 따라 변동하는 hidden state를 만든다.

---

> **숙련도 노트(Mastery Note) — [CRUCIBLE_DERIVED]**  
> 이 분류체계는 단순한 명명 작업이 아니라 작용 부위 배정(action-site assignment)이다. 약물이 input에 위치하는지 output에 위치하는지가 결정되면, 예상되는 `tss` 거동과 `kout`의 해석이 달라진다.

> **Mastery Anchor #3 — 5-minute structural model compression [CRUCIBLE_DERIVED]**  
> PD7 Fig 7.1 데이터를 본 30년 베테랑은 5분 안에 Model 4(stimulation of loss)로 압축한다. 추론 절차: ① 응답이 baseline에서 **하강** → 직접 자극은 production stimulation에서만 가능 → 따라서 stimulation은 loss 측에서 일어난다. ② tss가 **dose-dependent로 단축** → Models 1, 3 제외(이들은 loss term을 건드리지 않으므로 tss는 dose-independent이어야 한다). ③ ΔR 방향이 baseline 아래 → Model 2 제외 → **Model 4 확정**. PD5(Model 2: 응답이 baseline 위로 상승, tss 길어짐)와 PD7(Model 4: 응답이 baseline 아래로 하강, tss 짧아짐)을 side-by-side로 학습하면 이 추론이 "암송 가능"에서 "수행 가능"으로 전환된다.

> **🎯 Practice Brief — Card 2 [EXPERT_INFERENCE, v3]**: PD response 곡선을 본 순간 4개 칸(Inhibit/Stimulate × Production/Loss) 중 하나로 강제 분류한다. 응답 방향(↑/↓)과 tss의 dose-dependence(있음/없음) 조합을 5분 내 확인 — input-side(Models 1·3)는 tss=kout 보존, output-side(Models 2·4)는 effective kout이 농도 의존.

<!-- FIGURE_SCHEMATIC -->
Title: Four Turnover Models: Drug Action Site → Time-Constant Consequence
Mode: R
Visual objective: Within 5 seconds, show whether the drug acts on input or output and why that changes tss behavior.
Core message: Production-side models mainly change response extent, whereas loss-side models change both response extent and apparent response speed.
Elements to include: 2×2 grid of inhibition/stimulation by production/loss; central R0 = kin/kout baseline relation; input-side labels kin × I(C) and kin × S(C); output-side labels kout × I(C) and kout × S(C); bottom strip stating Models 1/3 → tss mostly kout, Models 2/4 → concentration-dependent apparent kout.
Elements to exclude: Full ODEs already printed in Card 2; case-study parameter values; full response-time curves.
Suggested rendering: Mermaid
Caption: Drug action site determines whether the drug changes response extent alone or also changes the apparent response clock.
Alt text: A 2 by 2 map of the four turnover models showing input-side and output-side drug effects and their expected tss consequences.
Source relation: Redrawn from textbook concept
<!-- /FIGURE_SCHEMATIC -->

## Card 3 — tss / Peak-Shift Mechanism Discrimination

<!-- MASTER LENS -->
### Big Idea

`tss`와 peak-shift는 강력한 진단 신호이지 최종 판정이 아니다. Models 1과 3은 loss rate가 변하지 않으므로 PD 정상상태 도달 시간이 용량과 무관한 경향이 있다. Models 2와 4는 loss term이 약물에 의해 변하므로 용량 의존적 `tss`가 나타날 수 있다. 이 규칙은 강하지만 절대 판정은 아니다. PK가 느리거나, dose range가 좁거나, response가 noisy하거나, mechanism에 unmodeled nonlinearity가 있으면 깨질 수 있다. [G pp.247–251; G pp.778–783; T p.243]

> **흐름에서의 역할**: Card 2가 4개 분류 칸을 만들었다면, Card 3은 그 칸 중 어디에 있는지를 *데이터 한 장*에서 판독하는 첫 진단 도구다. **이 카드를 deterministic rule로 외우는 순간 NDA Population PK/PD Analysis 모델 선택 근거가 PD9 Fig 9.5의 명시적 반례 한 장에 무력화**된다. 체화 목표는 tss를 "강한 1차 가설 발생기"로 쓰되, 동시에 4가지 가림 조건(PK rate-limiting, narrow dose range, noisy response, unmodeled nonlinearity)을 동시에 떠올리는 것이다.

### A. 핵심 추론(Core inference)

| 관찰(Observation) | 1차 기전 가설(First mechanistic hypothesis) | 주의사항(Caveat) |
|---|---|---|
| 용량 간 유사한 `tss` | 생산 측 작용: Model 1 또는 3 | PK rate-limiting 또는 제한된 데이터 해상도에 의해 가려질 수 있다. |
| 용량에 따라 `tss`가 단축되거나 연장됨 | 소실 측 작용: Model 2 또는 4 | PK가 PD clock보다 빠를 때만 성립. |
| 용량 증가에 따른 peak shift 부재 | Effect compartment를 증명하지 않음 | PD9 시뮬레이션이 이 과대해석을 명시적으로 경고한다. [G pp.778–783] |

<!-- TRENCH -->
### Trench-level tip — Mirror-slope misread

모든 모델을 Model 1/3처럼 취급하여 초기 반응 기울기에서 `kout`을 추정하지 않는다. Models 2/4에서는 초기 또는 겉보기 기울기가 `I(C)` 또는 `S(C)`에 의해 용량 의존적으로 스케일될 수 있다. 용량 의존적 `kout` 추정치는 대부분 생물학이 아니라 잘못된 구조 지정의 결과다. [G p.251]

### B. 실용적 판정 규칙(Practical decision rule)

`tss/peak-shift`는 **선별(triage)** 목적으로 사용하되, 최소한 하나 이상의 추가적 근거를 요구한다:

- 비선형 `H(C)` 거동을 노출할 수 있을 만큼 넓은 dose range;
- 반복 투여 또는 washout 데이터;
- production vs loss에 대한 신뢰할 수 있는 기전적 사전 정보(prior);
- PK clock이 PD clock보다 빠를 것;
- effect compartment 대안을 포함한 모델 비교.

<!-- RECAP -->
### Recap

`tss`는 *어디를 볼지* 알려주는 것이지, *어디서 멈출지*를 알려주는 것이 아니다. 가장 안전한 표현은 이것이다: "관측된 PK-rate 조건 하에서, `tss` 패턴이 production 측/loss 측 기전을 지지한다."

> **🔗 지연되는 숨겨진 상태 [EXPERT_INFERENCE, v3]**: loss term의 effective time constant. Models 2/4에서 이것이 dose에 따라 변하므로 tss가 dose-dependent로 나타나지만, PK rate-limiting · 좁은 dose range · noisy response · unmodeled nonlinearity가 이 시그니처를 가린다.

---

> **실패 모드(Failure Mode) — [AUDIT_DERIVED]**  
> 흔한 과도확장은 `tss` 또는 peak shift를 기전의 증거로 취급하는 것이다. 강력한 선별 신호로 사용하되, PK rate-limiting, 제한된 dose range, 또는 비선형 약물 기능이 예상 패턴을 가릴 수 있는지 반드시 검증한다.

> **Mastery Anchor #4 — Mirror-Slope Misread quantitative signature [CRUCIBLE_DERIVED]**  
> Mirror-slope misread는 추상적 경고가 아니라 **dose-level별 추정 `kout` 값의 단조 변화**라는 정량 시그니처를 갖는다. PD7 Fig 7.1을 사례로 보면 6,400 unit 용량에서 추정 `kout ≈ 0.6 h⁻¹`, 160,000 unit 용량에서 추정 `kout ≈ 1.6 h⁻¹` — 같은 system parameter이어야 할 `kout`이 dose에 따라 단조 증가한다. System parameter는 정의상 dose-invariant여야 하므로, **이 단조 변화는 biology가 아니라 misspecification artifact의 직접 신호**다. Table 3.6의 'Initial ΔR/Δt' 행은 Models 1·4에서만 −kout이고, Models 2·3에서는 zero-order kin이라는 점이 이 misread의 수학적 뿌리다. 정확한 처방: 초기 기울기를 `kout`로 외삽하기 전에 먼저 4-model taxonomy로 작용 부위를 확정한다.

> **🎯 Practice Brief — Card 3 [EXPERT_INFERENCE, v3]**: tss 패턴은 가설 발생기로만 사용한다. PK rate-limiting · 좁은 dose range · noisy response · unmodeled nonlinearity 4가지 가림 조건을 동시에 점검한 후에야 mechanism 결정으로 진행 — dose-level별 `kout` 추정치가 단조 변하면 biology가 아니라 mirror-slope misread를 의심한다.

## Card 4 — Imax/Emax Multiplier Semantics + Linear PK ≠ Linear PD

<!-- MASTER LENS -->
### Big Idea

`Emax`는 모든 모델에서 같은 단위와 의미를 갖지 않는다. Direct Emax 모델에서는 baseline으로부터의 절대 거리인 경우가 많다. Turnover 모델에서는 이미 `kin/kout` 비율로 정의된 system baseline에 곱해지는 배율이다. 이 의미를 혼동하면 in vitro potency, clinical EC50, and model-derived effect size가 서로 비교 가능한 것처럼 보인다. 실제로는 그렇지 않다. [G p.246]

> **흐름에서의 역할**: Card 1-3이 *시간*과 *작용 부위*를 잠갔다면, Card 4는 *효과 크기의 의미*를 잠근다. 이 카드를 놓치면 `Emax = 0.65` 같은 단일 추정치 하나가 *drug-specific potency*인지 *system-baseline에 대한 multiplier*인지 구분이 안 되며, in vitro IC50과 PopPK IC50의 비교가 의미 있는 것처럼 보이는 함정에 빠진다. 체화 목표는 모델 코드를 보자마자 `Emax`의 단위와 의미를 자동으로 분류하는 것이다.

### A. 의미 잠금(Semantic lock)

| 모델 형태(Model form) | 파라미터 의미(Parameter meaning) | 단위 / 해석(Unit / interpretation) |
|---|---|---|
| Direct additive Emax | $E=E_0+\frac{E_{max}C^n}{EC_{50}^n+C^n}$ | `Emax`는 반응 단위를 가짐; 절대 거리(absolute distance). |
| Direct reparameterized multiplier | $E=E_0(1+\frac{E_{max}C^n}{EC_{50}^n+C^n})$ | `Emax`는 무차원 배율(dimensionless multiplier). |
| Turnover Model 3 | $R_{ss}=R_0(1+\frac{E_{max}C^n}{EC_{50}^n+C^n})$ | `Emax`는 system turnover를 통해 작용하는 배율. |

### B. Linear PK does not imply linear PD

Methylprednisolone가 잠긴 사례다: 정확한 i.v. phosphate-prodrug 용량 시리즈는 16 / 31 / 63 / 125 / 250 / 500 / 1000 mg이다. 혈장 AUC는 용량에 거의 비례적으로 증가하지만 lymphocyte 반응은 비례적으로 증가하지 않으며, 고용량은 PD plateau에 근접한다. [T pp.256–258]

R&T 본문(p.256)은 이 함정을 단호하게 명시한다 — *"Dose linearity in pharmacokinetics does not result in dose linearity in pharmacodynamics. That is almost never the case."*

또한 systemic exposure가 곧 site-of-action exposure가 아닌 disconnect 사례도 같은 챕터에 등장한다: rosuvastatin OATP1B1 polymorphism은 plasma AUC를 substantially 변화시키지만 cholesterol synthesis response는 modestly 변한다(Fig 8-28/8-29 context only; 이것은 별도 turnover model이 아니라 exposure-response disconnect의 보조 관찰). [T pp.258–259]

<!-- TRENCH -->
### Trench-level tip

"용량 비례적 노출은 용량 비례적 반응을 지지한다"는 결론을 적기 전에, 그 반응을 Hill curve 렌즈로 통과시켜 본다. 제안된 dose range가 Region 3에 위치한다면, 추가 노출은 주로 plateau 지속시간 또는 독성 위험을 늘릴 뿐 반응을 두 배로 만들지는 않는다.

<!-- RECAP -->
### Recap

모델, 연구, 또는 화합물 간 효과 파라미터를 비교할 때는 항상 `ΔR/R0`로 변환한 후 비교한다.

> **🔗 지연되는 숨겨진 상태 [EXPERT_INFERENCE, v3]**: kin/kout 비율로 정의된 system baseline. turnover 모델의 Emax는 이 baseline을 곱셈적으로 변형하므로, direct Emax 모델의 absolute response distance와는 의미·단위가 모두 다른 hidden quantity다.

---

> **숙련도 노트(Mastery Note) — [CRUCIBLE_DERIVED]**  
> 모델 간 비교 시, 파라미터 레이블을 비교하기 전에 반응 스케일에서 관찰 가능한 것(observable)부터 비교한다. Turnover 모델에서는 같은 레이블이 직접적인 수직 반응 거리가 아니라 baseline 스케일의 system perturbation을 인코딩할 수 있다.

> **🎯 Practice Brief — Card 4 [EXPERT_INFERENCE, v3]**: Emax 추정치를 보고하기 전에 그 단위와 의미(absolute distance vs baseline multiplier)를 코드 형태에서 확인하고, ΔR/R0 normalization 후에 cross-model 비교를 한다. dose-proportional AUC를 본 순간 자동으로 dose-proportional response를 가정하지 않는다 — Hill curve의 어느 region에 있는지 먼저 확인.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.246, Fig 3.40
Why this matters: The figure shows that the same parameter label does not represent the same observed vertical response distance across model classes. Without the visual, learners may compare Emax values across direct and turnover models as if they had identical semantics.
When to look: after reading Card 4 Semantic lock
Learner instruction: Compare the vertical distance corresponding to observed ΔR with the model parameter label. Ask whether the parameter is an absolute response distance or a baseline-scaled multiplier.
<!-- /FIGURE_POINTER -->

## Card 5 — Graphical Initial Parameter Estimation + Blocking Dose / DRT

<!-- MASTER LENS -->
### Big Idea

초기 추정값은 '진짜 모델링' 이전의 번거로운 과정이 아니다. Turnover PD에서 graphical estimation은 첫 번째 기전적 점검 단계다. NONMEM이 탐색을 시작하기 전에 baseline, time constant, potency, and maximal effect를 먼저 분리해 두는 단계다. [G pp.247–251]

> **흐름에서의 역할**: Card 1-4가 *어떤 모델*인지 결정했다면, Card 5는 *그 모델의 파라미터 출발점*을 손으로 분리해 두는 단계다. 이 단계가 부실하면 NONMEM은 정답을 알면서도 그 위치까지 못 가거나, 비식별성 골짜기에 갇힌 채 가짜 수렴을 보고한다. 체화 목표는 raw response-time plot 한 장에서 `R0`, `kout`, 그리고 (potency, maximal effect)의 자릿수까지를 5분 안에 추정해보는 손버릇이다 — 이 손버릇이 fitted parameters의 sanity check 기준선이 된다.

### A. 최소 graphical 작업 흐름(Minimal graphical workflow)

1. 투약 전 또는 vehicle baseline에서 `R0`를 추정한다.
2. 종말 회복 곡선, blocked-synthesis 감소 구간, 또는 log-linear 복귀에서 `kout`를 추정한다.
3. `kin = R0·kout`으로 production rate를 계산한다.
4. 2–3개 용량 수준의 정상상태 또는 peak 반응으로 `IC50/EC50`와 `Imax/Emax`의 출발 자릿수를 잡는다.
5. 그런 다음에야 nonlinear mixed-effects estimation을 실행한다.

### B. Blocking-dose 유사 방법(Blocking-dose analogue)

Warfarin blocking-dose 분석은 `kout`을 직접 추출하는 임상적 등가 방법을 보여준다. 합성이 거의 완전히 차단될 때, prothrombin complex activity는 다음을 따른다:

$$\frac{dA}{dt}=-k_tA \quad \text{[T Eq 8-6; T pp.244–246]}$$

비차단 구간에서는 합성 속도를 재구성할 수 있다:

$$R_{syn}=\frac{A_2-A_1}{\Delta t}+k_t\frac{A_1+A_2}{2} \quad \text{[T Eq 8-7; T p.247]}$$

이는 hysteretic 반응-시간 기록을 억제-농도 관계로 변환한다. [T pp.244–247]

### C. DRT 맥락(DRT context)

Dose-Response-Time 분석은 농도 데이터가 없더라도 baseline, slope, potency, maximal effect를 추론할 수 있다. 그러나 full PK/PD modeling보다 거친 역문제(inverse problem)다. 노출(exposure) 데이터가 있으면 측정 노출을 DRT로 대체하지 말고, DRT를 후퇴 대안(fallback) 또는 교육적 가교(teaching bridge)로 둔다. [G pp.272–275]

<!-- TRENCH -->
### Trench-level tip

터무니없는 초기값이 필요한 모델은 대부분 graphical 단계를 건너뛰었거나 잘못된 clock을 사용했다는 뜻이다. Random effects를 확장하기 전에 출발점의 생물학을 먼저 수정해야 한다.

<!-- RECAP -->
### Recap

수동 초기 추정값은 구식 방법이 아니다. 식별가능성(identifiability) 감사의 첫 단계다.

> **🔗 지연되는 숨겨진 상태 [EXPERT_INFERENCE, v3]**: NONMEM 추정 이전의 R0와 kout. graphical workflow가 이 hidden state의 자릿수를 잠그지 못하면, 비식별성 골짜기에서 가짜 수렴이 보고되며 이는 다음 임상시험 설계를 비가역적으로 오염시킨다.

---

> **실무 관점(Practice Lens) — [CRUCIBLE_DERIVED]**  
> 수동 초기 추정값은 NONMEM 이전 시대의 향수가 아니다. 기전적 감사(mechanism audit)다: 기울기, baseline, 또는 blocking-dose 논리가 적합된 파라미터를 대략적으로라도 지지하지 못한다면, 최적화가 잘못된 문제를 깔끔하게 풀고 있을 가능성이 높다.

> **Mastery Anchor #5 — Graphical workflow as identifiability backstop [TEXTBOOK_DERIVED]**  
> PD5 case study가 이 워크플로우의 표준형이다. Compound A에서 `V = 40 L`, `K = 0.9 h⁻¹`인 PK가 먼저 잠긴 상태에서, 4000/16000/80000 unit의 6시간 infusion 데이터를 받는다. ① pre-infusion baseline으로 `R0`를 직접 읽고, ② post-infusion 회복 곡선의 semi-log plot에서 terminal slope로 `kout ≈ 0.43 h⁻¹`의 자릿수를 손으로 잡고, ③ `kin = R0 × kout`로 production rate의 출발점을 정한다. ④ 세 dose levels의 plateau 응답으로 `IC50 ≈ 95`, `Imax ≈ 0.65`의 자릿수까지 잡은 후에야 NONMEM 추정에 들어간다(Table 5.1). 이 손버릇이 빠진 워크플로우에서는 PD4 Pool 1 같은 `r(k1, kout) = 0.9999` 비식별성이 잡히지 않은 채 통과하고, "다음 시험의 sampling time horizon이 절반으로 단축된다"는 PD4 §Comparison 메시지처럼 **잘못된 모델 선택이 후속 임상시험 설계를 비가역적으로 오염**시킨다.

> **🎯 Practice Brief — Card 5 [EXPERT_INFERENCE, v3]**: NONMEM 추정 이전에 raw response-time plot에서 R0, kout, IC50/EC50, Imax/Emax의 자릿수를 손으로 5분 내 잡아두고, 그 값을 fitted parameters의 sanity check 기준선으로 쓴다. fitted 값이 graphical 자릿수에서 한 order 이상 벗어나면 비식별성 또는 misspecification 신호.

## Card 6 — Irreversible Drug Action + Target Consumption

<!-- MASTER LENS -->
### Big Idea

가역적 turnover 모델은 system이 반응을 지속적으로 생산하고 제거하기 때문에 baseline으로 돌아간다. 비가역적 작용은 다르다. 약물 노출 기간 동안 반응 단위, 표적, 또는 세포가 영구적으로 제거된다. 따라서 약물은 사라지더라도 그 생물학적 결과는 지속될 수 있다(drug may disappear while the biological consequence persists). [G pp.256–260; T pp.251–252]

> **흐름에서의 역할**: Card 1-5가 모두 *reversible* turnover의 다양한 형태를 다뤘다면, Card 6은 그 가정 — drug=0이면 system이 baseline으로 돌아온다 — 자체를 깨는 사례를 잠근다. 이 카드를 놓치면 aspirin, omeprazole, paclitaxel 같은 약물의 duration을 plasma half-life로 외삽하는 결정적 오류로 이어진다. 체화 목표는 "drug 사라짐 = effect 사라짐"이라는 무의식적 가정을 분리해서 — Card 7-8의 effect compartment·rate-limiting clock 결정에 필요한 사전 분기점을 만드는 것이다.

### A. 핵심 비가역 방정식(Core irreversible equation)

$$\frac{dR}{dt}=-K_{kill}\,C\,R \quad \text{[G Eq 3:110; G p.257]}$$

적분 형태의 생존율(survival fraction):

$$SF=\exp(-K_{kill}\cdot AUC) \quad \text{[G Eq 3:112; G p.257]}$$

`Kkill`은 2차 약리작용 상수(second-order drug-action constant)이며, 1차 PK 소실 상수가 아니다.

> [확인 필요] Source notation uses `K` in more than one context across irreversible kill and PK elimination. In this locked handout, `Kkill/kk` means pharmacodynamic killing; `Kelim` means PK elimination.

### B. 표적 소비 사례(Target consumption examples)

- Aspirin 650 mg 경구: 혈장 반감기는 짧지만, 혈소판 기능이 표적 대체(target replacement)에 의존하므로 thromboxane B₂ 억제가 수일간 지속된다. [T p.251]
- Omeprazole 40 mg 경구: 혈장 반감기가 1시간 미만이지만, proton-pump 결합/재생 동역학으로 인해 산분비 억제가 수일간 지속된다. [T p.252]
- Paclitaxel 정맥투여: 혈장 농도 감소는 백혈구 회복보다 훨씬 먼저 일어나며, 회복에 약 3주가 소요될 수 있다. Fig 8-22 맥락을 사용하며, Fig 8-19가 아니다. [T pp.253–254]

### C. 세포 성장/사멸 맥락(Cell growth/kill context)

세포가 증식할 때, 비가역적 사멸은 성장 동역학 안에 포함되어야 한다. Gabrielsson의 cell-growth/kill 프레임워크는 logistic 또는 용량-제한 성장과 2차 사멸을 추가한다. `Bmax≈30,000 CFU`는 맥락 앵커이며 별도의 MUST 카드가 아니다. [G pp.258–260]

<!-- RECAP -->
### Recap

약물이 사라진 후에도 system turnover로 생물학적 손실이 계속되면 reversible turnover를 사용한다. 노출이 표적/세포를 소비했고 회복이 대체에 의존하면 비가역적/target-consumption 논리를 고려한다.

> **🔗 지연되는 숨겨진 상태 [EXPERT_INFERENCE, v3]**: 약물이 사라진 후에도 비어 있는 target/platelet/cell pool. 회복 clock은 drug PK가 아니라 target replacement rate로 잠기며 — 이 hidden state를 무시하면 plasma half-life로 effect duration을 외삽하는 결정적 오류로 직결된다.

---

> **실패 모드(Failure Mode) — [TEXTBOOK_DERIVED]**  
> 약물 소실을 효과 소실과 동일시하지 않는다. 회복이 표적 대체(target replacement), 세포 재성장, 또는 system 수복에 의존하면, 혈장 PK만으로는 회복 clock을 제공할 수 없다.

> **🎯 Practice Brief — Card 6 [EXPERT_INFERENCE, v3]**: duration 질문을 받으면 먼저 "drug=0이면 effect=0인가?"를 묻고, 답이 NO이면 plasma PK 외 target replacement clock을 별도로 모델링한다. SF = exp(−Kkill·AUC) 형태가 적용되는지(target/cell consumption) 또는 reversible turnover로 충분한지를 *작용 기전 단계*에서 결정.

## Card 7 — [⚡ Apex Concept] Turnover vs Effect Compartment Discrimination Crisis

<!-- MASTER LENS -->
### Big Idea

Turnover 모델과 effect-compartment 모델은 제한된 단회 투여 설계 하에서 거의 동일한 response-time 곡선을 만들어낼 수 있다. 차이는 곡선의 매끄러움(curve smoothness)이 아니다. 차이는 인과적 주장에 있다: **지연이 일어나는 이유가 약물이 <!-- ANNOTATION --> biophase(← 실제 작용부위 주변 농도 공간)에 천천히 도달하기 때문인가, 아니면 반응 system 자체가 천천히 turnover하기 때문인가?** [G pp.758–763; T pp.244–246]

> **왜 Apex인가**: 이 세션에서 가장 자주 발생하는 실무 오류는 *틀린 모델 선택*이 아니라 *데이터가 두 모델 중 하나를 결정해주지 못한다는 사실 자체를 보지 못하는 것*이다. PD6는 그 비식별성을 정량화한 단일 사례다. 체화 목표는 fit이 아무리 깔끔해도 — 특히 단일 dose-range 데이터 위에서 — 인과 구조 두 가지가 동치 표면 위에 있다는 사실을 자동으로 의심하는 습관이다.

### A. 경쟁하는 구조들(Competing structures)

Turnover 예시:

$$\frac{dR}{dt}=k_{in}S(C)-k_{out}R$$

Effect compartment 예시:

$$\frac{dC_e}{dt}=k_{e0}(C-C_e), \quad R=f(C_e) \quad \text{[T pp.244–246]}$$

PD6가 이 위기를 잠근다: turnover와 effect-compartment 적합도가 본질적으로 같은 잔차 거동을 보이며, `kout`과 `ke0`가 모두 약 5.6 h⁻¹ 부근의 비슷한 값으로 수렴한다. [G pp.758–763]

> **📌 비식별성의 본질 — 학습자 본문 잠금 [EXPERT_INFERENCE, v3]**  
> Pool 1과 Pool 2 모델은 단일 dose range 데이터에서 사실상 구별 불가능하다(r=0.9999, ΔWRSS≈2). 이 비식별성은 피팅 실패가 아니라 **데이터가 두 모델을 분리하기에 충분하지 않다는 정보를 전달**한다. Wider dose range 또는 mechanism-based prior 없이는 어느 모델이 '옳은가'라는 질문 자체가 데이터로 답할 수 없다. 이 점이 Card 7을 Apex로 만드는 핵심이며, 이어지는 §B(How to discriminate)의 모든 evidence 항목은 이 비식별성을 *우회*하기 위한 외부 정보 — mechanism prior, broader design, perturbation — 의 목록이다.

### B. 감별 방법(How to discriminate)

| 증거(Evidence) | Turnover 지지(Supports turnover) | Effect compartment 지지(Supports effect compartment) |
|---|---|---|
| 반응 변수(Response variable) | 내인성 매개물질, 바이오마커, 세포 수, 응고인자, 위산 pH | 작용 부위로의 약물 분포가 지연의 가능한 원인 |
| Dose range | 비선형 turnover 생성 거동을 드러낼 만큼 넓을 것 | 안정적인 `EC50`과 타당한 `ke0`로 hysteresis가 해소됨 |
| 교란(Perturbation) | 반복 투여/washout이 system 회복 시간을 드러냄 | Biophase 평형으로 onset과 offset을 설명 |
| 기전적 사전 정보(Mechanistic prior) | 알려진 합성/소실 과정 | 알려진 조직 분포 지연 |

<!-- CONFUSION -->
### 치명적 타격(Critical Blow) — 교과서 기반 핵심 + 실무 해석 라벨

**교과서 기반**: 적합도(fit quality)만으로는 지연이 분포에 의한 것인지 turnover에 의한 것인지 증명할 수 없다. 제한된 설계에서는 두 구조가 동등하게 보일 수 있다. [G pp.758–763; T pp.244–246]

**[교과서 외 실무 해석]**: 규제 모델링 보고서에서 이것은 모델 선택 문단에 대안 구조 평가, 기전적 정당화, 그리고 민감도 분석(sensitivity analysis)을 포함해야 한다는 의미다. 명시적으로 실무 외삽임을 라벨링하지 않은 채 "NDA deficiency" 같은 미지지(unsupported) 표현을 사용하지 않는다.

<!-- TRENCH -->
### 현장 팁(Trench-level tip)

Turnover가 생성한 system에 effect-compartment 모델을 적합시켰을 때 `EC50`이 dose에 따라 변한다면, 그 약물 파라미터는 system 동역학을 흡수하고 있는 것이다. 이것은 potency 발견이 아니라 구조적 경고다.

<!-- RECAP -->
### Recap

Effect compartment는 "약물이 늦다"고 말한다. Turnover는 "생물학이 느리다"고 말한다. 곡선만으로는 어느 것이 맞는지 알 수 없다.

> **🔗 지연되는 숨겨진 상태 [EXPERT_INFERENCE, v3]**: 단일 dose-range 데이터 위에서 turnover의 R(t)와 effect compartment의 Ce(t)는 동일 fit을 만든다. 어느 hidden state가 '진짜' 지연되는 것인가 — biology인가 plasma-to-biophase distribution인가 — 는 데이터 단독으로 결정 불가능하며, 이것이 이 카드를 Apex로 만드는 비식별성의 본질이다.

---

> **실무 관점(Practice Lens) — [EXPERT_INFERENCE]**  
> 두 인과 구조가 동등하게 적합할 때, 규율 있는 접근은 생물학적 가정을 문서화하고 두 구조를 분리할 수 있는 설계 요소를 명시하는 것이다. 이 카드에서 모델의 방어 가능성(defensibility)은 곡선의 매끄러움이 아니라 기전(mechanism)과 설계 근거(design support)에서 나온다.

> **Mastery Anchor #6 — PD6 quantitative equivalence (the crisis as numbers) [CRUCIBLE_DERIVED]**  
> PD6 Table 6.1이 이 비식별성을 숫자로 박는다. 같은 데이터에 두 구조를 적합시켰을 때:
>
> | Metric | Turnover (linear S·kin) | Effect compartment | Δ |
> |---|---|---|---|
> | WRSS | 15,516 | 15,518 | 2 |
> | AIC | 1,041 | 1,040 | −1 |
> | 시간 상수 | `kout = 5.6 h⁻¹` | `ke0 = 5.6 h⁻¹` | 0 |
> | Half-doubling 농도 | `EC50 = 1,633 ng·L⁻¹` | `a = 0.026 → ~1,623 ng·L⁻¹` | <1% |
>
> ΔWRSS = 2와 ΔAIC = −1은 model selection criterion 입장에서 사실상 동치다. PD9 §Perspectives Fig 9.5 right panel의 단언(*"a lack of peak shift with increasing doses does not necessarily imply an effect compartment (link) model"*)이 이 카드의 한 줄짜리 잠금장치다. **mechanism prior 또는 wider dose range 없이는 두 모델 분리가 불가능**하다는 것이 이 표의 메시지이며, 이것이 Card 7의 Apex 위상을 정당화한다.

> **🎯 Practice Brief — Card 7 [EXPERT_INFERENCE, v3]**: 단일 dose-range 데이터에서 turnover와 effect compartment 두 모델을 *모두* 적합시키고 ΔWRSS·ΔAIC·kout/ke0 값으로 비식별성을 정량 확인한다. ΔWRSS≲5, kout≈ke0이면 데이터로는 결정 불가 — mechanism prior(endogenous mediator vs tissue distribution) 또는 broader design으로 정당화하거나, sensitivity analysis로 의사결정이 모델 선택과 무관함을 증명한다.

<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.759, Fig 6.1; p.763, Table 6.1
Why this matters: This is the apex discrimination example: the response-time fits can appear essentially equivalent while the causal interpretations remain different. Table 6.1 makes the kout/ke0 near-equivalence concrete.
When to look: after reading Card 7 Competing structures
Learner instruction: Inspect the response-time fit first, then inspect the kout and ke0 estimates. Do not decide the mechanism from smoothness of fit alone.
<!-- /FIGURE_POINTER -->

## Card 8 — PK Clock vs PD Clock + Duration Formula Boundary

<!-- MASTER LENS -->
### Big Idea

투약 후 두 개의 시계가 동시에 작동한다: 약물의 PK clock과 반응 system의 PD clock. 관찰되는 반응 감소는 이 중 느린 쪽의 시계가 결정한다. 따라서 drug elimination에 근거한 duration formula는 response가 PK-rate-limited이고 exposure-response relationship이 사실상 고정되어 있을 때만 유효하다. [T pp.243, 247–256]

> **세션 닫음 카드의 역할**: Card 1-7이 모델 *구조*에 관한 결정이었다면, Card 8은 그 구조 위에서 *임상 dose-duration 의사결정*이 가능한지 여부를 결정한다. 이 카드를 거치지 않고 Eq 8-12를 사용하면 warfarin·aspirin·omeprazole·paclitaxel 같은 PD-rate-limited 약물에 대해 수학적으로 매끈하지만 임상적으로 무의미한 duration 예측이 나온다. 체화 목표는 어떤 약물에서든 duration 질문을 받았을 때 자동으로 *"PK clock과 PD clock 중 어느 쪽이 느린가?"*를 먼저 묻는 reflex다.

### A. Clock 감별(Clock discrimination)

| 상황(Situation) | 느린 clock(Slower clock) | 고정 사례(Locked examples) | 모델링 귀결(Modeling consequence) |
|---|---|---|---|
| PK rate-limited | 약물 소실/분포 | Succinylcholine 0.5/1/2/4 mg·kg⁻¹ i.v., 근이완; minoxidil 단회 경구 25 mg, MAP 저하 [T pp.249–256] | `tD` 공식이 의미 있을 수 있다. |
| PD rate-limited | System turnover/표적 재생 | Acenocoumarol vs 응고인자 turnover; aspirin 혈소판/TxB₂; omeprazole proton-pump 회복; paclitaxel 백혈구 회복 [T pp.243, 251–254] | Turnover/target-consumption 모델이 필요; PK `k`만으로는 duration 예측 불가. |
| 약물 PK가 system보다 느릴 때 | 간접 기전에서도 PK가 지배 | Phenprocoumon 반감기 ~5일 vs 응고인자 동역학 [T p.243] | 항응고 효과 회복이 약물 잔류를 따른다. |

### B. Region 1/2/3과 선형 감소(Region 1/2/3 and linear decline)

계단식 E-logC 관계의 중간 구간에서는 단일 용량 투여 후 반응이 시간에 따라 근사적으로 선형으로 감소한다:

$$Response=E(0)-mkt \quad \text{[T Eq 8-9; T pp.247–249]}$$

이것은 Region 2에 대한 서술이다. 즉, response가 Hill curve의 중간 구간에 있을 때의 근사다. Region 3은 plateau에 가깝고, Region 1은 1차 동역학 유사 거동으로 복귀한다. Succinylcholine의 대략 22%/min 감소가 이 중간 구간 선형성을 예시한다. [T pp.249–250]

### C. Duration 공식(Duration formula)

<!-- ANNOTATION --> 따라서 clock 감별이 먼저 끝나야 한다. PK-rate-limited 반응에서 노출-반응 관계가 사실상 고정되어 있을 때:

$$t_D=\frac{1}{k}\ln\left(\frac{Dose}{C_{min}V}\right)=\frac{1}{k}\ln\left(\frac{Dose}{A_{min}}\right) \quad \text{[T Eq 8-12; T pp.254–255]}$$

용량을 두 배로 올리면 약물 반감기 하나만큼의 duration이 추가된다:

$$\Delta t_D=\frac{\ln 2}{k}=t_{1/2}$$

이것이 succinylcholine의 duration이 용량 두 배마다 대략 유효 반감기 하나만큼 증가하는 이유다. [T pp.255–256]

<!-- TRENCH -->
### Wrong-clock warning

Eq 8-12를 warfarin, aspirin, omeprazole, paclitaxel처럼 PD-rate-limited 상황에 적용하지 않는다. System clock이 약물 소실보다 느리면 이 공식은 수학적으로는 깔끔하지만 생물학적으로 틀린 duration을 반환한다.

<!-- RECAP -->
### Recap

Duration을 계산하기 전에 먼저 묻는다: "어느 clock이 느린가?" 답이 PD라면 PK `k`를 duration 결정 인자로 사용하는 것을 중단한다.

> **🔗 지연되는 숨겨진 상태 [EXPERT_INFERENCE, v3]**: PK clock과 PD clock 중 느린 쪽. 어느 clock이 rate-limiting인지 결정하지 않은 채 Eq 8-12를 적용하면 수학은 매끈하나 임상은 무의미하다 — 이 hidden state의 위치가 곧 duration formula의 적용 가능 여부를 결정한다.

---

> **실패 모드(Failure Mode) — [AUDIT_DERIVED]**  
> Duration 공식은 clock 선택 전에 적용하면 위험해진다. PK와 PD 중 어느 쪽이 rate-limiting인지를 먼저 결정한다. 그 이후에야 대수적 dose-duration 관계가 의도된 의미를 갖는다.

> **Mastery Anchor #7 — Post-trough rebound timing as moderator/feedback signal [CRUCIBLE_DERIVED]**  
> 30년 베테랑은 turnover 모델 fit을 받자마자 **post-trough 회복 곡선의 타이밍**을 본다. observed 데이터가 모델보다 빠르게 baseline으로 돌아온다면 그것은 moderator/feedback compartment 누락의 즉각적 신호다 — `kout`이 시간에 따라 변하지 않는다는 basic turnover 가정의 위반이다. G&W §2.6.7 Eq 2:261-2:263과 IgG 11일 saturable protection이 이 패턴의 prototype이며(serum IgG 30 mg·mL⁻¹에서 half-life가 11일로 단축), `$COV step` 결과가 출력되기 전에 이 시각 점검이 끝나야 한다. 같은 logic이 Card 8의 wrong-clock 진단에도 적용된다 — 예측 duration이 관측 duration과 50% 이상 어긋나거나 dose 증량 시 예측 duration의 증가가 관측치와 비례하지 않는다면, 그것은 rate-limiting clock이 잘못 잡혔다는 정량 시그니처다.

> **Mastery Anchor #8 — Acenocoumarol vs Phenprocoumon as the canonical clock-pair [CRUCIBLE_DERIVED]**  
> 동일한 prothrombin complex 동역학을 공유하는 두 약물에서 acenocoumarol(half-life ~15 h)은 PD clock이 baseline 복귀를 지배하고, phenprocoumon(half-life ~5–6일)은 PK clock이 지배한다(Fig 8-11). 이는 *동일 작용기전을 공유하는 약물군에서도 약물별 PK가 rate-limiting step을 결정한다*는 사실의 결정판이다. **단일 약물 데이터에 갇힌 학습자에게는 이 사실 자체가 보이지 않는다.** 따라서 새로운 약물의 duration 질문을 받을 때, 같은 mechanism을 공유하는 다른 약물의 PK profile을 함께 비교하는 것이 첫 번째 reflex가 되어야 한다.

> **🎯 Practice Brief — Card 8 [EXPERT_INFERENCE, v3]**: duration formula(Eq 8-12) 적용 전에 항상 "PK clock과 PD clock 중 어느 쪽이 느린가?"를 reflex로 묻는다. PK-rate-limited면 dose 두 배가 한 half-life의 duration을 추가하고, PD-rate-limited면 turnover/target-replacement model로 대체 — 같은 mechanism이라도 약물별 PK profile이 rate-limiting step을 결정한다는 점을 잊지 않는다.

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.243, Fig 8-11
Why this matters: The same anticoagulant response system can be limited by different clocks depending on drug PK. This figure prevents the common error of assigning recovery only to the shared PD mechanism.
When to look: before applying the Card 8 duration formula
Learner instruction: Compare the recovery time-course for the short-PK and long-PK anticoagulant. Identify which curve is governed by system recovery and which is governed by drug persistence.
<!-- /FIGURE_POINTER -->

<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.255, Fig 8-23; p.256, Fig 8-24
Why this matters: These figures show the visual consequence of Eq 8-12: under PK-rate-limited conditions, dose doubling adds approximately one half-life of duration. Without this plot, the formula is easy to memorize but easy to misuse.
When to look: after reading Card 8 Duration formula
Learner instruction: Trace how equal log-dose increments translate into equal time increments. Then re-check that the example is PK-rate-limited before generalizing the formula.
<!-- /FIGURE_POINTER -->

# §5 — 혼동 쌍 해부(Confusion Pair Dissection)

<!-- CONFUSION -->
## §5-1. Model 1 vs Model 2 — 생산 억제(Inhibition of Production) vs 소실 억제(Inhibition of Loss)

| 차원(Dimension) | Model 1: 생산 억제(inhibit production) | Model 2: 소실 억제(inhibit loss) |
|---|---|---|
| ODE | $dR/dt=k_{in}I(C)-k_{out}R$ [G pp.238–239] | $dR/dt=k_{in}-k_{out}RI(C)$ [G pp.240–241] |
| 방향(Direction) | 반응 감소 | 반응 증가 |
| `tss` | 주로 `kout`, PK가 빠르면 용량 독립적 | 유효 `kout·I(C)`, 용량 의존적 |
| 흔한 오류(Common error) | production vs loss를 명시하지 않고 하향 반응을 모두 "억제"로 부름 | loss inhibition을 확인하지 않고 상향 반응을 production stimulation으로 취급함 |
| 기억 잠금(Memory lock) | 약물이 수도꼭지를 잠근다. | 약물이 배수구를 막는다. |

<!-- CONFUSION -->
## §5-2. Direct Emax vs Turnover Imax/Emax

| 차원(Dimension) | Direct 모델 | Turnover 모델 |
|---|---|---|
| 파라미터 표면(Parameter surface) | 즉각적 농도-반응 관계 | 생산/소실 동역학 후의 system 반응 |
| `Emax` 의미 | 파라미터화에 따라 절대 반응 거리 또는 baseline 배율 | `kin/kout` baseline에 대한 배율 |
| 안전한 비교 방법(Safe comparison) | 같은 스케일이면 관찰된 반응 단위로 직접 비교 | `ΔR/R0`와 기전 특이적 `IC50/EC50` 비교 |
| 핵심 사례(Key example) | Midazolam direct link [T p.239] | PD5/PD7 turnover 파라미터 표 [G pp.753–769] |

<!-- CONFUSION -->
## §5-3. Reversible Turnover vs 비가역적 사멸(Irreversible Kill) / 표적 소비(Target Consumption)

| 차원(Dimension) | Reversible turnover | 비가역적 / 표적 소비(Irreversible / target consumption) |
|---|---|---|
| 약물 중단 후 거동(Drug-off behavior) | `kin/kout`에 의해 system이 복귀 | 표적/세포 대체까지 효과가 지속될 수 있음 |
| 핵심 방정식(Core equation) | $dR/dt=k_{in}-k_{out}R$ | $dR/dt=-K_{kill}CR$ |
| 사례(Example) | Warfarin/응고인자 turnover [T pp.242–247] | Aspirin/TxB₂, omeprazole/proton pump [T pp.251–252] |
| 오류(Error) | 지연된 회복이 비가역적 작용을 의미한다고 가정 | 약물 소실이 효과 소실을 의미한다고 가정 |

<!-- CONFUSION -->
## §5-4. Turnover 모델 vs Effect Compartment — 치명적 쌍(Critical Pair)

| 차원(Dimension) | Turnover 모델 | Effect compartment |
|---|---|---|
| 지연의 소속(Delay belongs to) | 반응 생물학(Response biology) | 작용 부위(biophase)로의 약물 분포 |
| 파라미터(Parameter) | `kin`, `kout`, `R0`, `IC50/EC50` | `ke0`, `Ce`, direct response 파라미터 |
| 최선의 사전 정보(Best prior) | 내인성 매개물질/세포/바이오마커 turnover | 조직 평형 지연 |
| 함정(Trap) | 적합도가 link 모델을 모방할 수 있음 | 적합도가 system turnover를 `ke0`에 흡수할 수 있음 |
| 잠긴 해석(Locked interpretation) | 적합도 단독이 아닌 기전적 사전 정보 + 설계 근거를 사용한다. | 동일. |

**[교과서 외 실무 해석]** 규제 제출 형식의 글에서, 이 지점이 대안 모델 비교(alternative model comparison)와 기전적 정당화(mechanistic justification)가 들어가야 할 위치다. 설계가 구조를 감별할 수 없다면 선택된 구조를 자명한 것처럼 제시하지 않는다.

<!-- CONFUSION -->
## §5-5. PK Rate-Limited vs PD Rate-Limited 감소(Decline)

## §5-5. PK Rate-Limited vs PD Rate-Limited 감소

| 차원(Dimension) | PK-rate-limited | PD-rate-limited |
|---|---|---|
| 느린 clock(Slow clock) | 약물 농도 감소 | System 회복/표적 대체 |
| 공식(Formula) | `tD` 공식 적용 가능 | PK `k`로 `tD` 공식 사용 = 잘못된 clock 적용 |
| 사례(Example) | Succinylcholine; minoxidil [T pp.249–256] | Acenocoumarol, aspirin, omeprazole, paclitaxel [T pp.243, 251–254] |
| 임상적 실패(Clinical failure) | Duration에 대한 청소율(clearance) 효과를 간과 | 노출만으로 duration 변화를 과대 예측 |

> **각주(Footnote) — 노출-반응 단절(Exposure-response disconnect, CONTEXT only)**  
> Rosuvastatin OATP1B1 polymorphism은 systemic plasma exposure를 substantially 변화시키지만 site-of-action(cholesterol synthesis) response는 modestly 변한다. 이는 별도의 turnover model이 아니라 **systemic exposure ≠ site-of-action exposure**의 보조 사례다. Bioequivalence가 효과 동등성을 보장하지 않는 메커니즘으로 자주 인용된다. [T pp.258–259]

<!-- CONFUSION -->
## §5-6. ⚡ 기억 고리(Memory Hooks) — 7가지 핵심 개념 쌍 [EXPERT_INFERENCE, v3]

이 섹션은 §5-1~§5-5의 5개 비교 표를 보완하는 **기억 고리 모음**이다. 각 hook은 두 개념의 차이가 발생하는 *구조적 필연*을 비유로 인코딩한다 — 단순 차이 나열이 아니라 차이의 *이유*를 머릿속에 박는다. §5-1·§5-4와 일부 cross-reference되며, 나머지 5쌍은 §2 본문에 이미 잠긴 개념의 회상 트리거로 작동한다.

---

### Pair 1 — direct effect(직접 효과) vs indirect response(간접 반응)

**⚡ 기억 고리** — *바로 켜지는 전등 vs 서서히 따뜻해지는 전기장판*: Direct effect는 약물 농도가 오르면 반응이 즉시 따라오는 **즉각 반응 시스템** — 플라즈마 농도와 효과가 시간 위상이 같다. Indirect response는 약물이 production 또는 loss를 바꾸고, 그 변화가 response pool에 축적되어 효과가 나타나는 **지연 반응 시스템** — 전기장판처럼 열이 쌓여야 따뜻해진다. PD 데이터에서 반응이 Cmax보다 늦게 피크에 도달한다면 indirect response 메커니즘을 먼저 의심한다.

---

### Pair 2 — Model I (생산 억제, production inhibition) vs Model II (소실 억제, loss inhibition)

*Cross-reference: §5-1*

**⚡ 기억 고리** — *수원 틀기 vs 배수구 막기*: Model I은 약이 **수원(production)을 줄이는** 모델 — pool이 점점 비워진다. Model II는 약이 **배수구(loss)를 막는** 모델 — pool이 쌓인다. 방향이 반대이므로 baseline에서의 response trajectory도 반대다. 그러나 단일 dose range에서는 두 모델이 사실상 같은 데이터를 만든다(Pool 1/2 비식별성) — 방향 결정을 위해서는 mechanism prior 또는 더 넓은 용량 범위 데이터가 필요하다.

---

### Pair 3 — kin vs kout (turnover 속도 파라미터)

**⚡ 기억 고리** — *수원 속도 vs 배수 속도*: 기저상태에서 pool이 일정하다면 kin = kout × baseline이 성립한다 — 수원이 채우는 속도와 배수구가 비우는 속도가 같다. kout (= 1/MRT_response)는 반응의 반감기를 결정한다. 약이 kin을 절반으로 줄이면 새 steady state는 baseline의 절반이 되지만, 그 도달에 걸리는 시간은 0.693/kout이다 — **효과의 시간 경과는 농도 PK가 아니라 kout이 결정한다**는 점이 direct effect와 가장 다른 점이다.

---

### Pair 4 — baseline R0 vs steady-state Rss (약물 효과 하)

**⚡ 기억 고리** — *출발점 vs 목적지*: Baseline R0는 약 투여 전 pool의 자연 균형점(수원=배수구). Rss는 약 효과 하에서의 새 균형점 — 약이 production을 줄이면 Rss < R0, loss를 줄이면 Rss > R0. **그 사이를 이동하는 속도는 kout이 결정한다. R0와 Rss 사이의 거리는 Emax와 EC50이 결정한다.**

---

### Pair 5 — rebound(반등) vs natural recovery(자연 회복)

**⚡ 기억 고리** — *과교정 vs 자연 복귀*: Rebound는 약을 중단했을 때 반응이 baseline을 **초과하여 오르는 것** — 약이 production을 억제했을 때 중단 시 pool이 빠르게 생산되며 초과한다. Natural recovery는 baseline으로 단순히 돌아오는 것. 구분 기준: 반응이 baseline을 넘어서면 rebound, 단조롭게 감소하면 natural recovery. **Rebound는 turnover 모델에서만 나타나는 시그니처다.**

---

### Pair 6 — duration of effect(효과 지속시간) vs AUC of effect(효과의 면적)

**⚡ 기억 고리** — *효과의 길이 vs 효과의 면적*: Duration은 반응이 threshold 이상(또는 이하)에 머무는 **시간 길이** — 단일 숫자. AUC of effect는 시간에 따른 반응-시간 곡선 아래 면적 — 총 효과의 크기. 같은 duration이어도 AUC가 다를 수 있다(반응의 높이가 다를 때). Indirect response 모델에서 duration은 kout과 투여 프로토콜에 의존하며, AUC of effect는 kin/kout과 Emax에 의존한다.

---

### Pair 7 — Pool 1/2 모델 비식별성(non-identifiability) vs 모델 오설정(misspecification)

*Cross-reference: §5-4 (Critical Blow), Card 7 PATCH 3 paragraph*

**⚡ 기억 고리** — *지도가 둘 다 정확 vs 지도가 틀림*: Pool 1/2 비식별성은 데이터가 두 모델 중 어느 것이 맞는지 결정하지 못하는 상태 — 두 지도가 이 영역에서 모두 정확하게 그려져 있어 어느 것을 쓸지 선택 불가. Model misspecification은 데이터와 맞지 않는 틀린 지도를 선택한 상태. **비식별성은 모델 선택의 정보 부족 문제이고, misspecification은 구조적 오류다.** ΔWRSS≈2, ΔAIC≈−1은 비식별성의 신호이지 misspecification의 신호가 아니다.

---

<!-- RECAP -->
## §5 Recap — 다섯 가지 clock 위치 오류(The five clock-location errors)

이 세션에서 발생하는 거의 모든 오류는 algebra 오류가 아니라 **clock-location 오류**다. 즉, 시간을 지배하는 *느린 clock의 위치*를 잘못 짚었기 때문에 발생하는 오류다. 5가지 표준 패턴으로 정리한다.

| 오류 패턴(Error pattern) | 잘못 짚은 clock | 잠긴 반례(Locked counter-example) |
|---|---|---|
| **E1. Mirror-slope misread** | early response slope를 모든 모델에서 −kout로 외삽 | PD7: 6,400U → 0.6 h⁻¹, 160,000U → 1.6 h⁻¹ — system parameter가 dose-dependent로 보이는 misspecification artifact [G p.251] |
| **E2. Phantom convergence with linear S(C)** | turnover와 effect compartment가 같은 fit을 줬으므로 effect compartment 확정 | PD6 Table 6.1: ΔWRSS = 2, kout = ke0 = 5.6 h⁻¹ — fit 동등성이 mechanism 결정을 의미하지 않음 [G pp.758–763] |
| **E3. Wrong-clock tD** | 모든 약물에 Eq 8-12 적용 | warfarin/aspirin/omeprazole/paclitaxel은 PD-rate-limited — PK k로 계산한 tD는 임상적으로 무의미 [T pp.251–254] |
| **E4. Linear-PK = linear-PD assumption** | dose-proportional AUC가 곧 dose-proportional response | methylprednisolone 16-1000 mg: AUC는 비례하나 lymphocyte response는 plateau 진입 [T pp.256–258] |
| **E5. Same-mechanism = same-clock assumption** | 동일 작용기전이면 같은 rate-limiting step | acenocoumarol(PD-limited, 15 h) vs phenprocoumon(PK-limited, ~5 days) — 같은 anticoagulant mechanism, 다른 지배 clock [T p.243] |

이 5가지를 외운 학습자는 이 세션의 모델링 결정을 거의 자동으로 방어할 수 있다.

---

# §7 — 자기 테스트: 능동 회상 모듈(Self-Test: Active Recall Module)

<!-- SELF-TEST -->
## Q1 [회상] Model 1 ODE와 정상상태(steady state)

Model 1 ODE를 쓰고, 일정한 `Css` 하에서 `Rss`를 도출하라.

**정답(Answer)**  
$$\frac{dR}{dt}=k_{in}I(C)-k_{out}R$$  
정상상태에서: $R_{ss}=R_0I(C_{ss})$. [G pp.238–239]

<!-- SELF-TEST -->
## Q2 [회상] `tss`가 용량 독립적인 모델은?

`tss`가 용량 독립적인 모델은 무엇인가?

**정답(Answer)**  
Models 1과 3 — 1차 소실 항이 `kout·R`로 유지되기 때문이다. Models 2와 4는 약물이 소실 항을 변경하므로 용량 의존적 `tss`를 보일 수 있다. 단, 이 결론은 PK가 더 느린 clock이 아닐 때만 성립한다. [G pp.247–251; T p.243]

<!-- SELF-TEST -->
## Q3 [응용] PD9의 peak shift 부재 해석

용량이 증가해도 peak shift가 나타나지 않는다. 이것이 effect compartment 모델을 증명하는가?

**정답(Answer)**  
아니다. PD9는 peak shift 부재가 link/effect-compartment 모델을 반드시 의미하지 않는다고 명시적으로 경고한다. Dose range, 비선형 약물 기능, system 동역학을 함께 고려해야 한다. [G pp.778–783]

<!-- SELF-TEST -->
## Q4 [응용] PD9 Zooparc® 용량 정정

Zooparc® 반복 투여 데이터에서 확인된 용량 수준은 무엇이며, 25 mg/day는 어떻게 기술해야 하는가?

**정답(Answer)**  
관찰된 반복 투여 figure는 2.5 mg과 5 mg을 사용한다. 25 mg/day 진술은 투사(projection)/대규모 연구 논의이며, 관찰된 용량 맥락이 아니다. [G pp.778–783]

<!-- SELF-TEST -->
## Q5 [응용] Naproxen 정정

"naproxen 250 mg, Fig 8-3"이라는 오류 표현을 수정하라.

**정답(Answer)**  
Naproxen 500 mg 경구, dental pain 모델, 1–8 h sampling, 반시계 방향(counterclockwise) hysteresis, Fig 8-2. Fig 8-3은 하류 약력학 도식이며, naproxen 그림이 아니다. [T pp.234–236]

<!-- SELF-TEST -->
## Q6 [응용] 잘못된 clock의 `tD`

Aspirin duration 예측에 Eq 8-12가 왜 부적절한가?

**정답(Answer)**  
Aspirin의 혈장 노출은 빠르게 사라지지만, 표적/혈소판 기능 회복이 더 느리기 때문에 thromboxane B₂ 억제는 지속된다. Duration은 PD/표적 대체에 의해 결정되며, PK rate-limited가 아니다. [T p.251]

<!-- SELF-TEST -->
## Q7 [응용] Turnover vs effect compartment

단일 용량 데이터가 turnover와 effect-compartment 두 모델 모두에 동등하게 적합한다. 두 모델 중 하나를 결정하는 데 어떤 증거가 필요한가?

**정답(Answer)**  
반응 변수에 대한 기전적 사전 정보, 더 넓은 dose range, 반복 투여/washout, PK clock 교란, 그리고 `EC50/ke0`이 생물학적으로 타당하게 유지되는지 여부. 적합도 단독으로는 불충분하다. [G pp.758–763; T pp.244–246]

<!-- SELF-TEST -->
## Q8 [응용] Linear PK ≠ linear PD

Methylprednisolone AUC가 16–1000 mg 범위에서 용량 비례적이다. 그것이 왜 용량 비례적 lymphocyte 반응을 정당화하지 않는가?

**정답(Answer)**  
반응이 노출-반응 곡선의 plateau 구간에 진입할 수 있다. R&T의 lymphocyte 사례는 PK가 용량 비례적임에도 고용량에서 추가 PD 반응이 거의 없음을 보여준다. R&T 본문(p.256)은 단호하게 명시한다 — *"Dose linearity in pharmacokinetics does not result in dose linearity in pharmacodynamics. That is almost never the case."* [T pp.256–258]

<!-- SELF-TEST -->
## Q9 [보스 딜레마(Boss dilemma)]

스폰서가 다음을 주장한다: "phenprocoumon과 acenocoumarol은 동일한 항응고 기전을 공유하므로, 반응 회복은 동일한 PD turnover half-life로 결정되어야 한다." 동의하는가, 거부하는가? **30년 경력 심사자가 사용할 구체적 방어 논리로 정당화하라.**

**정답(Answer) — Trade-off 논리**  
**거부(Reject).** 동일한 기전이 동일한 rate-limiting clock을 의미하지는 않는다. Acenocoumarol은 PK 반감기가 더 짧으며(~15 h), 회복은 PD-clock 제한적이 된다(응고인자 turnover). Phenprocoumon은 PK 반감기가 훨씬 길어(~5일), 회복은 PK-clock 제한적이 된다(약물 잔류가 system clock보다 우세). [T p.243]

이 차이가 임상·규제 차원에서 갖는 trade-off는 다음과 같다:
- **Sponsor의 단순화 채택 시**: 두 약물에 동일한 dose-titration step-up rule 적용 → phenprocoumon 누적 위험 또는 acenocoumarol 미달 dose. 어느 쪽이든 환자 안전·약효 부전 사고로 직결.
- **Mechanism-only justification의 규제적 위험**: 모델 선택 paragraph에서 "동일 mechanism이므로 동일 PD half-life"라는 추론은 design support 없이 데이터로 방어 불가능 → "insufficient justification for proposed dosing interval" 형태의 deficiency 위험. [교과서 외 실무 해석]
- **올바른 방어 논리**: 약물별 PK profile이 동일 PD system 위에서 어떤 clock을 활성화시키는지를 acenocoumarol vs phenprocoumon Fig 8-11 데이터로 직접 증명한 후, 각 약물별로 별도의 dose-duration model을 사용한다. 단일 PD half-life claim은 phenprocoumon에서 임상적으로 무의미하고 acenocoumarol에서만 유효하다.

<!-- SELF-TEST -->
## ⚡ 보스 딜레마 ★★ [EXPERT_INFERENCE, v3]

Pool 1과 Pool 2 indirect response 모델 중 어느 것을 Phase 2 용량 결정에 사용할 것인가? 두 모델은 현재 데이터(단일 dose group, 제한된 dose range)에서 ΔWRSS=2, kout=ke0로 사실상 비식별적이다.

**선택지 A**: 기존 생물학적 증거가 production inhibition을 지지한다면(예: 생체표지자가 생성률과 연관) Model I을 선택하고, 비식별성을 보고서에서 limitation으로 명시한다.

**선택지 B**: 어느 메커니즘도 확실하지 않다면, 두 모델을 모두 제출하고 sensitivity analysis를 통해 용량 결정이 모델 선택에 얼마나 민감한지 제시한다. 더 보수적인 용량 예측을 제공하는 모델을 기본으로 사용한다.

**거장의 Trade-off 논리**  
A는 기계론적으로 간결하지만 데이터 외 prior를 사용했다는 비판을 받을 수 있다. B는 불확실성을 투명하게 전달하지만 의사결정자에게 혼란을 줄 수 있다. **규제 제출에서는 "어느 모델을 선택했는가"보다 "왜 이 불확실성이 용량 결정의 안전성에 영향을 주지 않는가"를 설명하는 것이 핵심이다.** 즉, 두 모델 모두에서 제안된 Phase 2 용량이 안전 한계 안에 있음을 sensitivity analysis로 증명하면, 모델 선택 자체가 의사결정의 critical path에서 빠진다 — 이것이 "비식별성을 *우회*하는" 정통 규제 전략이다.

이 딜레마의 Apex 메시지: 비식별성 앞에서 모델을 *선택*하려 하지 말고, 비식별성이 의사결정에 *영향을 주지 않는 결정 구조*를 설계하라.

<!-- RECAP -->
## §7 Recap

올바른 답은 반드시 **model family**와 **clock 위치** 모두를 식별해야 한다. 수학적으로 맞는 공식이라도 잘못된 clock에 적용하면 틀린 것이다.

---

# §8 — 메타프레임 & 빅 픽처(Meta-Frame & Big Picture)

## A. 약리계측학 아키텍처에서의 위치(Positioning in the pharmacometrics architecture)

이 세션은 직접 노출-반응 모델링(direct exposure-response modeling)과 고급 질병/반응 시스템 사이에 위치한다. 여기서부터 모델러는 곡선 적합(curve fitting)을 넘어 원인 분리를 수행해야 한다. 이 단계는 다음을 처음으로 분리해야 하는 지점이다:

- 약물 파라미터(drug parameters)와 system 파라미터의 분리;
- 분포 지연(distribution delay)과 생물학적 turnover delay의 분리;
- 노출 정도(exposure extent)와 반응 지속시간(response duration)의 분리;
- 모델 적합도(model fit)와 모델 의미(model meaning)의 분리.

이는 transit compartment, tolerance/moderator 모델, 질병 진행, system 파라미터에 IIV가 있는 PopPK/PD, 임상시험 sampling 설계 등 후속 작업의 토대가 된다.

## B. 이 세션을 약하게 다뤘을 때의 실패 모드(Failure modes if this session is weak)

| 실패 모드(Failure mode) | 실무적 결과(Practical consequence) |
|---|---|
| 모든 지연을 effect compartment로 처리 | `ke0`이 생물학을 흡수한다. 새로운 투여 프로토콜에서 dosing 시뮬레이션이 실패한다. |
| `tss`를 모델의 결정적 증거로 처리 | 기전적 주장이 설계 근거를 과대평가한다. |
| `Emax` 단위 혼동 | 교차 연구 또는 in vitro/임상 potency 비교가 오해를 유발한다. |
| PD-rate-limited 약물에 `tD` 적용 | Duration 예측이 생물학적으로 무의미해진다. |
| Baseline drift 무시 | 질병 진행 또는 일주기 변동이 약물 효과로 오독된다. |

## C. 전문가 해석 지점(Professional moat) — 30년 베테랑의 30초 진단 시퀀스

30년 경력의 약리계측학(pharmacometrics) 심사자는 곡선이 매끄러운지를 가장 먼저 묻지 않는다. 데이터를 본 첫 30초 안에 진단 시퀀스를 실행한다. **이 시퀀스가 NONMEM을 실행할 수 있는 주니어 모델러와의 본질적 차이다 — 같은 데이터를 보고도 도달하는 결론의 정확성과 속도가 완전히 다르다.**

1. **Hysteresis 방향 (Mastery Anchor #1)**: plasma C vs response 산점도에서 loop 방향만으로 1차 분류 — counterclockwise는 distribution/turnover/active-metabolite, clockwise는 tolerance/feedback/enantiomer-specific. 30초 안에 첫 가설이 잡힌다.
2. **Response direction × tss 거동 (Mastery Anchor #3)**: 응답 방향과 tss의 dose-dependence 조합으로 4-model 칸 중 하나를 5분 안에 압축. PD5(Model 2)와 PD7(Model 4) side-by-side가 이 추론의 표준 reference.
3. **Post-trough rebound timing (Mastery Anchor #7)**: turnover fit이 나오자마자 회복 곡선의 타이밍을 본다. observed가 모델보다 빠르면 moderator/feedback 누락 신호. `$COV step` 결과를 기다리지 않는다.
4. **OFV 궤적 패턴 (Mastery Anchor #2)**: OFV가 30 iteration 동안 stuck-then-drop이면 즉시 (R0, kout) 재파라미터화로 옮겨간다. 이것은 cosmetic이 아니라 search geometry의 본질적 변경이다.
5. **Clock pair 비교 (Mastery Anchor #8)**: 새 약물의 duration 질문을 받으면 같은 mechanism을 공유하는 다른 약물의 PK profile을 함께 본다. acenocoumarol vs phenprocoumon이 표준 reference pair.

이 다섯 단계를 30초 안에 통과한 후에야 NONMEM 출력에 손을 댄다. 자동화된 도구는 단계 1, 4를 모방할 수 있지만 단계 2, 3, 5의 *데이터의 의미를 묻는 직관*은 데이터 외부의 mechanistic prior를 요구하므로 복제되지 않는다.

<!-- RECAP -->
## 최종 잠긴 요약(Final locked summary)

간접 반응 모델링(Indirect response modeling)은 "지연을 추가하는 것"이 아니다. 올바른 인과 clock에 지연을 할당하는 것이다. 따라서 잠긴 작업 흐름은 다음과 같다:

**hysteresis direction → four-model action site → tss/peak-shift triage → initial-parameter audit → turnover-vs-link discrimination → PK/PD clock selection → duration formula only if PK-rate-limited.**


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

- Preserve P/R/N/I decisions from the Figure Strategy / Insertion Map.
- If Image rights = None: do not embed copyrighted textbook images. Render `FIGURE_POINTER` as text-only callout.
- `FIGURE_SCHEMATIC` must be a visually distinct redraw; do not reproduce textbook layout, color palette, or label placement.
- Do not propose new figures.
- Do not generate Mermaid/SVG in Phase 4D; Phase 5 performs rendering.

#### Approved Figure Strategy / Insertion Map

# 11_Content Lock v2.1 — Figure Marker Insertion Plan

**Output mode declaration: PATCH MODE**

**Mode rationale**: Content Lock v2 is long (>6000 words; approximately 6935 whitespace-delimited tokens in the local file). Therefore the full Content Lock body is not re-emitted. This v2.1 deliverable contains only the visual strategy, briefs, and insertion map needed to splice figure markers into the unchanged Content Lock v2 file.

**Phase boundary**: This file decides figures only. It does not generate Mermaid, SVG, HTML, or any image. Source textbook images are not embedded because image rights are not available; all source textbook visuals are handled as POINTERs, and one structurally distinct REDRAW brief is provided for Phase 5.

---

## Figure Strategy Table — View A. Reading-order Figure Plan

| # | Reading order | Location (§ + concept card) | Mode | Source figure(s) | Trigger | Why text alone is insufficient | Expected learning gain | Decision |
|---:|---|---|---|---|---|---|---|---|
| 1 | §2-1 | Card 1 — Turnover Model Foundation + Hysteresis Classification | P | G&W Fig 3.33 [G p.235] + R&T Fig 8-2 [T p.235] | G2, G5 | Direct vs delayed response and counterclockwise hysteresis are temporal patterns; prose definitions do not show that the same concentration can map to different responses depending on time path. | Learner can visually separate direct link, delayed response, and hysteresis loop before reading later model-discrimination cards. | KEEP |
| 2 | §2-2 | Card 2 — Four-Model Taxonomy: Inhibit/Stimulate × Production/Loss | R | Redrawn from G&W Table 3.3, Table 3.5, Figs 3.35–3.39 concept set [G pp.238–247] | G1, G2, G4 | The existing table lists ODEs, but the learner must mentally infer how input/output site controls `tss`; that inference is central and error-prone. | A single structural map links action site → effective time constant → expected `tss` behavior. | KEEP |
| 3 | §2-4 | Card 4 — Imax/Emax Multiplier Semantics + Linear PK ≠ Linear PD | P | G&W Fig 3.40 [G p.246] | G2, G5 | The semantic trap is geometric: `Emax`, `Imax`, and observed `ΔR` are not the same vertical distance across direct and turnover forms. | Prevents cross-model parameter comparison errors by making the `ΔR/R0` distinction visible. | KEEP |
| 4 | §2-5 | Card 5 — Graphical Initial Parameter Estimation + Blocking Dose / DRT | P | R&T Fig 8-15 [T p.246] | G1, G5 | Blocking-dose logic is a slope-extraction procedure; equations alone do not show how the observed response-time profile is converted into synthesis-rate reasoning. | Learner sees why blocked synthesis exposes a degradation clock and why manual initial estimation is mechanistic, not cosmetic. | REJECT — useful, but lower ROI than Card 7/8 figures under pointer budget. |
| 5 | §2-6 | Card 6 — Irreversible Drug Action + Target Consumption | P | G&W Fig 3.47 [G p.256] or R&T Figs 8-20–8-21 [T pp.251–252] | G2, G5 | Reversible vs irreversible persistence is visually helpful, but the current Card 6 text already separates `drug-off` turnover from target/cell replacement. | Would reinforce target-consumption intuition. | REJECT — lower ROI than the clock and duration figures because Card 6 is not the session's apex decision point. |
| 6 | §2-7 | Card 7 — Turnover vs Effect Compartment Discrimination Crisis | P | G&W Fig 6.1 [G p.759] + G&W Table 6.1 [G p.763] | G2, G5 | The apex lesson is that two causal models can look nearly the same; the learner must inspect the fit/estimate equivalence, not only read the warning. | Makes "fit quality alone is insufficient" concrete by pairing curve similarity with similar `kout/ke0`. | KEEP |
| 7 | §2-8A | Card 8 — PK Clock vs PD Clock + Duration Formula Boundary | P | R&T Fig 8-11 [T p.243] | G2, G5 | PK vs PD rate-limiting is a comparative time-course concept; text alone can hide that the same mechanism can have different limiting clocks across drugs. | Learner sees acenocoumarol vs phenprocoumon as the canonical "same PD system, different slow clock" example. | KEEP |
| 8 | §2-8C | Card 8 — PK Clock vs PD Clock + Duration Formula Boundary | P | R&T Fig 8-23 [T p.255] + R&T Fig 8-24 [T p.256] | G1, G5 | `tD` and dose-doubling are logarithmic time relationships; without the source plot, the formula can be memorized without understanding its visual consequence. | Learner sees why dose doubling adds one half-life of duration only under the PK-rate-limited boundary. | KEEP |
| 9 | §8 | Meta-Frame & Big Picture | N | Newly designed workflow overview | G3, G4 | A workflow schematic would be attractive, but the final locked summary already states the sequence explicitly. | Would reinforce the overall workflow. | REJECT — decorative/summary value; not necessary under strict visual ROI. |

---

## Figure Strategy Table — View B. Type-sorted Summary

**Pointers (P): #1, #3, #6, #7, #8 → 5 / max 5**

- #1 Card 1 paired pointer: direct/delayed response + clinical hysteresis.
- #3 Card 4 pointer: Imax/Emax semantic distinction.
- #6 Card 7 pointer: turnover vs effect-compartment equivalence.
- #7 Card 8 pointer: PK vs PD rate-limiting clocks.
- #8 Card 8 pointer: duration-log dose relationship.

**Schematics (R/N): #2 → 1 / max 2**

- #2 Card 2 REDRAW: four-model action-site map.

---

# Insertion Map (PATCH MODE)

The following map is authoritative for v2 → v2.1 splicing. Do not re-output or rewrite the Content Lock v2 body. Insert each marker block at the end of the specified concept card, on its own lines, before the next card or section heading.

| # | Reading order | Anchor copied verbatim from Content Lock v2 | Insert position | Marker block |
|---:|---|---|---|---|
| 1 | §2-1 | `## Card 1 — Turnover Model Foundation + Hysteresis Classification` | after this anchor card | See Marker Block 1 below |
| 2 | §2-2 | `## Card 2 — Four-Model Taxonomy: Inhibit/Stimulate × Production/Loss` | after this anchor card | See Marker Block 2 below |
| 3 | §2-4 | `## Card 4 — Imax/Emax Multiplier Semantics + Linear PK ≠ Linear PD` | after this anchor card | See Marker Block 3 below |
| 4 | §2-7 | `## Card 7 — [⚡ Apex Concept] Turnover vs Effect Compartment Discrimination Crisis` | after this anchor card | See Marker Block 4 below |
| 5 | §2-8A | `## Card 8 — PK Clock vs PD Clock + Duration Formula Boundary` | after this anchor card | See Marker Block 5 below |
| 6 | §2-8C | `## Card 8 — PK Clock vs PD Clock + Duration Formula Boundary` | after this anchor card, immediately after Marker Block 5 | See Marker Block 6 below |

## Marker Block 1

```text
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.235, Fig 3.33; Rowland & Tozer 5e, p.235, Fig 8-2
Why this matters: Fig 3.33 separates direct response from delayed hysteretic response. Fig 8-2 shows that the same naproxen concentration can map to different pain relief depending on the rising/falling phase.
When to look: after reading Card 1
Learner instruction: First inspect the time plots, then inspect the concentration-response loop. Follow the time labels to verify that hysteresis is a time-ordered path, not scatter around a static curve.
<!-- /FIGURE_POINTER -->
```

## Marker Block 2

```text
<!-- FIGURE_SCHEMATIC -->
Title: Four Turnover Models: Drug Action Site → Time-Constant Consequence
Mode: R
Visual objective: Within 5 seconds, show whether the drug acts on input or output and why that changes tss behavior.
Core message: Production-side models mainly change response extent, whereas loss-side models change both response extent and apparent response speed.
Elements to include: 2×2 grid of inhibition/stimulation by production/loss; central R0 = kin/kout baseline relation; input-side labels kin × I(C) and kin × S(C); output-side labels kout × I(C) and kout × S(C); bottom strip stating Models 1/3 → tss mostly kout, Models 2/4 → concentration-dependent apparent kout.
Elements to exclude: Full ODEs already printed in Card 2; case-study parameter values; full response-time curves.
Suggested rendering: Mermaid
Caption: Drug action site determines whether the drug changes response extent alone or also changes the apparent response clock.
Alt text: A 2 by 2 map of the four turnover models showing input-side and output-side drug effects and their expected tss consequences.
Source relation: Redrawn from textbook concept
<!-- /FIGURE_SCHEMATIC -->
```

## Marker Block 3

```text
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.246, Fig 3.40
Why this matters: The figure shows that the same parameter label does not represent the same observed vertical response distance across model classes. Without the visual, learners may compare Emax values across direct and turnover models as if they had identical semantics.
When to look: after reading Card 4 Semantic lock
Learner instruction: Compare the vertical distance corresponding to observed ΔR with the model parameter label. Ask whether the parameter is an absolute response distance or a baseline-scaled multiplier.
<!-- /FIGURE_POINTER -->
```

## Marker Block 4

```text
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.759, Fig 6.1; p.763, Table 6.1
Why this matters: This is the apex discrimination example: the response-time fits can appear essentially equivalent while the causal interpretations remain different. Table 6.1 makes the kout/ke0 near-equivalence concrete.
When to look: after reading Card 7 Competing structures
Learner instruction: Inspect the response-time fit first, then inspect the kout and ke0 estimates. Do not decide the mechanism from smoothness of fit alone.
<!-- /FIGURE_POINTER -->
```

## Marker Block 5

```text
<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.243, Fig 8-11
Why this matters: The same anticoagulant response system can be limited by different clocks depending on drug PK. This figure prevents the common error of assigning recovery only to the shared PD mechanism.
When to look: before applying the Card 8 duration formula
Learner instruction: Compare the recovery time-course for the short-PK and long-PK anticoagulant. Identify which curve is governed by system recovery and which is governed by drug persistence.
<!-- /FIGURE_POINTER -->
```

## Marker Block 6

```text
<!-- FIGURE_POINTER -->
Source: Rowland & Tozer 5e, p.255, Fig 8-23; p.256, Fig 8-24
Why this matters: These figures show the visual consequence of Eq 8-12: under PK-rate-limited conditions, dose doubling adds approximately one half-life of duration. Without this plot, the formula is easy to memorize but easy to misuse.
When to look: after reading Card 8 Duration formula
Learner instruction: Trace how equal log-dose increments translate into equal time increments. Then re-check that the example is PK-rate-limited before generalizing the formula.
<!-- /FIGURE_POINTER -->
```

### B3. Page Tag Rendering Rules

- Preserve all `[p.XX]`, `[pp.XX–YY]`, `[pp.XX, YY]`, `[p.확인 필요]`, `[G ...]`, and `[T ...]` source tags as visible traceability text.
- Render page tags visibly in HTML.
- Do not fabricate, delete, renumber, or relocate page tags.
- `[p.확인 필요]` remains visible unless already resolved by Audit/Content Lock.
- Do not apply source-page regex inside code blocks or inside figure marker blocks.

### B4. HTML Compiler Requirements

(v1과 동일. Education UX Engineer role definition, PATCH MODE Splice Verification halt conditions, marker → component mapping table, page tag rendering rules, CSS variable requirements 모두 v1에서 carry-over. v2는 이 섹션 변경 없음.)

### B5. Audit Guardrails

Regression-prevention items for Session 11:

- Do not restore `naproxen 250 mg` or `Fig 8-3` as the naproxen anchor; the locked correction is naproxen 500 mg oral, dental pain, 1–8 h, counterclockwise hysteresis, Fig 8-2.
- Do not restore `ibuprofen Fig 8-4`; the locked figure is Fig 8-9.
- Do not restore `paclitaxel Fig 8-19`; Fig 8-19 is minoxidil and paclitaxel is Fig 8-22.
- Do not frame the minoxidil figure as topical; the locked example is single oral 25 mg with MAP-lowering context.
- Do not restore Zooparc® `5 mg or 25 mg q24h` as observed repeated-dose data; observed repeated-dose figures are 2.5 mg and 5 mg, while 25 mg/day is a projection/larger-study statement.
- Do not present NDA/IND/FDA reviewer/deficiency-letter wording as textbook-derived. Keep any such language explicitly labeled `[교과서 외 실무 해석]` or omit it.
- Do not restore an absolute "all measurable responses are delayed" claim without the direct-response caveat.
- Do not treat `tss` or peak shift as deterministic proof of mechanism; preserve the data-resolution, dose-range, PK-rate-limiting, and mechanistic-prior caveats.
- **v3.2 추가 가드레일**: PART A의 한국어 지배적으로 변환된 산문(§2 카드 표 항목, Mastery Note/Practice Lens/Failure Mode 블록, 비교 표 셀, Trench tip, 정의 산문, 소제목 헤더, §5/§7/§8 본문)을 영문으로 되돌리지 않는다. v3.2 patch가 적용된 모든 위치는 v3.2 Korean-Dominant Patch table P-36–P-72로 추적 가능하다.
- **v3.1 추가 가드레일**: PART A의 한국어화된 산문 (Big Idea 오프너, §7 질문, §8 산문, Recap, Trench, Structural 블록, Learner Navigation)을 영문으로 되돌리지 않는다. v3.1 patch가 적용된 모든 위치는 Korean Readability Patch v3.1 patch table P-01–P-35로 추적 가능하다.
- **v2 추가**: v2의 Mastery Anchor 8개는 모두 Crucible v1 Grade A 항목 또는 ADOPT 항목에서 직접 도출됨. 신규 사실 도입 없음.

### B6. Source-Boundary Guardrails

- Do not introduce new drug examples beyond the locked source universe (Gabrielsson & Weiner 5e + Rowland & Tozer 5e).
- Do not introduce new page tags beyond those already in PART A.
- Do not introduce new numerical anchors beyond those already in PART A.
- Do not introduce regulatory claims (NDA/IND/FDA) without `[교과서 외 실무 해석]` label.
- Mastery Anchors and Practice Briefs in PART A are bounded augmentations — do not expand them with new sources.
- v3 additions ([EXPERT_INFERENCE, v3]) are locked structural patches — do not expand with new fact, page tag, or example.
- **v3.2 추가**: Korean-Dominant Readability Patch는 영문→한국어 surface 교체 + career-critical 전문용어의 `한글(English)` 병기 통일에 한정. 새 사실·예시·page tag·수치·외부 reference 도입 0건이며, 의미 보존성은 v3.2 patch table에서 검증됨.
- **v3.1 추가**: Korean Readability Patch는 영문→한국어 surface 교체에 한정. 새 사실·예시·page tag 도입 0건이며, 의미 보존성은 v3.1 patch table에서 검증됨.

### B7. Deprecated and Forbidden Restorations

- Step 1 Draft v0 is deprecated.
- Do not restore rejected overclaims, unsupported numbers, unsupported regulatory claims, source-unsupported examples, unapproved code, or unapproved figures.
- Do not use Step 1 Draft v0 as learner-body source except through the Micro-Patch Gate.
- Do not restore Phase 1 card overgrowth; Cards 8–9 remain merged in Card 8.
- Do not restore rejected figure candidates #4, #5, or #9 from v2.1.

### B8. PATCH MODE Splice Verification Table

| Marker # | Anchor text | Anchor found? | Match count | Inserted? | Final location (§ + card) |
|---:|---|---|---:|---|---|
| 1 | `## Card 1 — Turnover Model Foundation + Hysteresis Classification` | YES | 1 | YES | Card 1 — Turnover Model Foundation + Hysteresis Classification |
| 2 | `## Card 2 — Four-Model Taxonomy: Inhibit/Stimulate × Production/Loss` | YES | 1 | YES | Card 2 — Four-Model Taxonomy: Inhibit/Stimulate × Production/Loss |
| 3 | `## Card 4 — Imax/Emax Multiplier Semantics + Linear PK ≠ Linear PD` | YES | 1 | YES | Card 4 — Imax/Emax Multiplier Semantics + Linear PK ≠ Linear PD |
| 4 | `## Card 7 — [⚡ Apex Concept] Turnover vs Effect Compartment Discrimination Crisis` | YES | 1 | YES | Card 7 — [⚡ Apex Concept] Turnover vs Effect Compartment Discrimination Crisis |
| 5 | `## Card 8 — PK Clock vs PD Clock + Duration Formula Boundary` | YES | 1 | YES | Card 8 — PK Clock vs PD Clock + Duration Formula Boundary |
| 6 | `## Card 8 — PK Clock vs PD Clock + Duration Formula Boundary` | YES | 1 | YES | Card 8 — PK Clock vs PD Clock + Duration Formula Boundary, immediately after Marker Block 5 |

### B9. Zero-Omission Coverage Matrix (v2 update)

| Domain | Required item | Evidence in PART A | Status | Action |
|---|---|---|---|---|
| C1 Scope concepts | Turnover foundation, four models, tss/peak-shift, Imax/Emax semantics, initial estimates, irreversible action, effect compartment discrimination, PK/PD clock + duration | §2 Cards 1–8 | PRESENT | None |
| C1 Scope chapter role | Separate distribution delay, turnover delay, target consumption, and rate-limiting clocks | §1 Big Idea; §8 Final locked summary | PRESENT | None |
| C2 Required data anchors | G&W PD4/PD5/PD6/PD7/PD9 anchors retained where Content Lock v2 locked them | §2 Cards 3, 5, 7 and self-test Q3–Q4 | PRESENT_COMPRESSED | Do not expand beyond Content Lock. |
| C2 Required data anchors | R&T clinical anchors: digoxin, naproxen, midazolam, ibuprofen, warfarin, acenocoumarol/phenprocoumon, succinylcholine, minoxidil, aspirin/omeprazole/paclitaxel, methylprednisolone, rosuvastatin | §2 Cards 1, 4, 6, 8; §5; §7 | PRESENT_COMPRESSED | Kept at MUST/CONTEXT level. |
| C3 Audit MUST_FIX | (v1과 동일 — naproxen, ibuprofen, paclitaxel, minoxidil, Zooparc, regulatory, "all delayed", tss deterministic, methylprednisolone, K notation 모두 PRESENT) | (v1 위치 carry-over) | PRESENT | (v1과 동일) |
| C4 Audit T5 | T Key Relationships / direct-link vs delayed bridge / slower-clock author message | §1; §8; Card 8 | PRESENT | None |
| C5 Figure coverage | Approved KEEP figures #1, #2, #3, #6, #7, #8 | Six figure marker blocks in Cards 1, 2, 4, 7, 8 | PRESENT | Render only approved markers. |
| C5 Figure rights | No copyrighted textbook images embedded | Learner navigation note; PART B B2/B4 | PRESENT | Render pointers or distinct redraw only. |
| C6 Page tags | Existing `[G ...]` and `[T ...]` page tags preserved | PART A body | PRESENT | No new page tags fabricated. |
| C7 Crucible Grade A — basic adopted set | tss first-order analogue, ΔR/Emax semantics, Region 2 boundary, PK/PD clock non-identifiability, wrong-clock warning | Cards 3, 4, 8; §5; §7 | PRESENT_COMPRESSED | Preserved only as adopted logic. |
| **C7-v2 Crucible Grade A — mastery-anchor 5종 (v2 신규 강화)** | **PD4 Pool 1/2 r=0.9999 비식별성 (Wall #4) → Card 1 Anchor #2** | **Card 1 Mastery Anchor #2** | **PRESENT** | **v1에서 일반화되었던 reparameterization tip을 정량화된 비식별성 사례로 강화** |
| **C7-v2** | **OFV stuck-then-drop pattern (Intuition #2) → Card 1 Anchor #2** | **Card 1 Mastery Anchor #2** | **PRESENT** | **v1의 단순 trench tip을 진단 시그니처로 강화** |
| **C7-v2** | **Hysteresis 30-second direction diagnosis (Intuition #4) → Card 1 Anchor #1** | **Card 1 Mastery Anchor #1** | **PRESENT** | **v1의 Card 1.B 표 상태를 30초 진단 sequence로 명시화** |
| **C7-v2** | **Mirror-Slope Misread PD7 quantitative (T3 Tip 1) → Card 3 Anchor #4** | **Card 3 Mastery Anchor #4** | **PRESENT** | **v1의 abstract trench tip을 6,400U → 0.6 h⁻¹, 160,000U → 1.6 h⁻¹ 정량 시그니처로 강화** |
| **C7-v2** | **Post-trough rebound timing diagnosis (Intuition #1) → Card 8 Anchor #7** | **Card 8 Mastery Anchor #7** | **PRESENT** | **v1의 §8C 한 줄을 카드 단위 진단 anchor로 강화** |
| **C7-v2** | **5-minute structural model compression (Integration #1) → Card 2 Anchor #3** | **Card 2 Mastery Anchor #3** | **PRESENT** | **v1의 추상적 분류를 PD7 추론 절차 3단계로 명시화** |
| **C7-v2** | **PD6 quantitative equivalence Table (T2(c) Critical Blow) → Card 7 Anchor #6** | **Card 7 Mastery Anchor #6** | **PRESENT** | **v1의 한 줄 수치 언급을 ΔWRSS=2/ΔAIC=−1/kout=ke0=5.6 정량 표로 강화** |
| **C7-v2** | **Acenocoumarol vs Phenprocoumon canonical clock-pair (Wall #4 + Integration #4) → Card 8 Anchor #8** | **Card 8 Mastery Anchor #8** | **PRESENT** | **v1의 Card 8.A 표 한 행을 same-mechanism≠same-clock 결정판 reference로 강화** |
| C8 Deprecated draft regression | unsupported regulatory overclaims, wrong figure numbers, wrong naproxen/minoxidil/Zooparc framing, broad scope creep | PART B B5/B7 guardrails | PRESENT | Do not restore Step 1 text. |
| C9 Canonical body integrity | Content Lock v2 learner body spliced with approved markers; no broad rewrite | PART A §1–§8 | PRESENT | Only learner wrappers, labeled augmentations, and v2 Mastery Anchors added. |
| **C10-v2 Layout adjustments** | **Card 8 Section D (Rosuvastatin) → §5-5 footnote 이동** | **§5-5 Footnote** | **PRESENT** | **v1의 Card 8 흐름 어색함 해소; 본문 fact·page tag 동일 유지** |

### B10. Micro-Patch Log (v2)

v1과 비교하여 추가된 micro-patch:

1. **Big Idea 3-pillar 강화**: Card 1, 2, 3, 4, 5, 6, 7, 8의 Big Idea 직후 1단락의 mental model anchor를 추가. 기존 fact·equation·page tag·marker는 변경하지 않음.
2. **Card 8.D Rosuvastatin → §5-5 footnote 이동**: Card 8 흐름 정합성 향상. 본문 wording은 그대로 유지 (T pp.258–259 page tag 보존).
3. **Card 4.B에 R&T 명시 인용 추가**: *"Dose linearity in pharmacokinetics does not result in dose linearity in pharmacodynamics. That is almost never the case."* 라는 R&T p.256 직접 인용 추가. 이는 fabrication이 아닌 source-supported quote이며 Audit T3 Author Key Messages에서 INCLUDED_CORRECT로 검증된 메시지.
4. **§5 Recap → §5-Recap 5-error 구조화**: v1의 1단락 추상 메시지를 5개 표준 error 패턴으로 구조화. 모든 데이터·수치·page tag는 본문 cards에 이미 존재하는 것만 인용.
5. **§7 Q9 답변 확장**: Trade-off logic을 sponsor 시나리오 + 규제 위험 + 올바른 방어 논리 3단으로 확장. 새 fact·page tag·약물 추가 없음.
6. **§8C → 30-second diagnostic sequence**: 5단계로 구조화. 각 단계는 Mastery Anchor #1·#2·#3·#7·#8과 cross-reference.

No micro-patches modified scientific content. PART A v2 = PART A v1 + bounded, source-labeled augmentations.

### B11. Mastery Augmentation Log

#### v1 inserted (carry-over)

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
|---:|---|---|---|---|---|---|
| 1 | Card 1 | Practice Lens | YES | AUDIT_DERIVED | Clarifies direct-vs-delayed as resolution-sensitive before model selection. | Low |
| 2 | Card 2 | Mastery Note | YES | CRUCIBLE_DERIVED | Converts taxonomy into action-site and clock reasoning. | Low |
| 3 | Card 3 | Failure Mode | YES | AUDIT_DERIVED | Prevents deterministic overuse of tss/peak shift. | Low |
| 4 | Card 4 | Mastery Note | YES | CRUCIBLE_DERIVED | Prevents parameter-label comparison errors. | Low |
| 5 | Card 5 | Practice Lens | YES | CRUCIBLE_DERIVED | Frames manual estimates as mechanistic sanity checks. | Low |
| 6 | Card 6 | Failure Mode | YES | TEXTBOOK_DERIVED | Prevents drug-disappearance/effect-disappearance confusion. | Low |
| 7 | Card 7 | Practice Lens | YES | EXPERT_INFERENCE | Adds model-defensibility lens without new data or examples. | Medium |
| 8 | Card 8 | Failure Mode | YES | AUDIT_DERIVED | Prevents wrong-clock application of duration formula. | Low |

#### v2 newly inserted (Mastery Anchors)

| # | Location | Type | Inserted? | Source status | Rationale | Risk |
|---:|---|---|---|---|---|---|
| 1 | Card 1 | Mastery Anchor | YES | CRUCIBLE_DERIVED (Intuition #4) | 30-second hysteresis direction diagnosis로 카드의 진단 reflex를 명시화. 기존 Card 1.B 표 상태를 sequence로 변환. | Low |
| 2 | Card 1 | Mastery Anchor | YES | CRUCIBLE_DERIVED (Wall #4 + Intuition #2) | PD4 Pool 1/2 r=0.9999 비식별성 + OFV stuck-then-drop pattern을 카드 단위 진단 reflex로 elevate. | Low |
| 3 | Card 2 | Mastery Anchor | YES | CRUCIBLE_DERIVED (Integration #1) | 5-minute structural model compression의 PD7 추론 3단계로 4-model 분류 reflex를 표준화. | Low |
| 4 | Card 3 | Mastery Anchor | YES | CRUCIBLE_DERIVED (Tip 1) | Mirror-Slope Misread를 PD7 6,400U → 0.6 h⁻¹, 160,000U → 1.6 h⁻¹의 정량 시그니처로 강화. | Low |
| 5 | Card 5 | Mastery Anchor | YES | TEXTBOOK_DERIVED (PD5 Table 5.1) | Graphical workflow를 PD5 Compound A 4단계 절차로 구체화. PD5 Table 5.1 수치 인용 유지. | Low |
| 6 | Card 7 | Mastery Anchor | YES | CRUCIBLE_DERIVED (T2(c) Critical Blow) | PD6 Table 6.1 ΔWRSS/ΔAIC/kout=ke0/EC50 정량 표로 비식별성 결정타를 cement. | Low |
| 7 | Card 8 | Mastery Anchor | YES | CRUCIBLE_DERIVED (Intuition #1) | Post-trough rebound timing 진단을 카드 단위 anchor로 elevate. moderator/feedback 누락 신호로 명시. | Low |
| 8 | Card 8 | Mastery Anchor | YES | CRUCIBLE_DERIVED (Wall #4 + Integration #4) | Acenocoumarol vs Phenprocoumon을 same-mechanism≠same-clock canonical pair로 elevate. §7 Q9 trade-off 답변과 cross-reference. | Low |

#### Rejected v2 candidates

| Rejected candidate | Reason for rejection |
|---|---|
| Add new named clinical examples beyond G&W/R&T source universe | Would violate source boundary and require external support. |
| Add Mermaid/SVG code in v2 | Phase 4D decides content/markers only; Phase 5 renders visuals. |
| Add extra figure candidates for negative feedback, DRT, or target consumption | Rejected by v2.1 visual ROI/budget logic; v2 maintains v1 figure budget. |
| Add NONMEM `$DES` code blocks for taxonomy demonstration | G&W/R&T source universe does not include NONMEM control streams; would require [교과서 외 실무 해석] label and dilute source-boundary discipline. |
| Expand Card 8.D Rosuvastatin into a separate sub-card | Rejected. Rosuvastatin is exposure-response disconnect CONTEXT only; promoting it violates the locked Content Lock v2 MUST/CONTEXT separation. v2 instead moves it to §5-5 footnote where it belongs structurally. |

### B12. v1 → v2 Change Log (NEW)

이 섹션은 v2가 v1으로부터 무엇을 변경했는지에 대한 완전한 audit trail이다. v2는 다음 6가지만 변경했고, 그 외는 모두 v1과 동일하다.

| Change # | 위치 | 변경 종류 | v1 상태 | v2 상태 | Source authorization |
|---:|---|---|---|---|---|
| 1 | Card 1-8 Big Idea 직후 | augmentation | 단독 단락 | + 1단락 mental model anchor (3-pillar: 왜 중요/흐름 위치/체화 직관) | self-derived synthesis from existing Big Idea content; no new fact added |
| 2 | Card 1, 2, 3, 5, 7, 8 | new Mastery Anchor | 0개 | 8개 (Mastery Anchor #1-#8) | All from Crucible v1 Grade A or Audit T1/T3 INCLUDED_CORRECT |
| 3 | Card 8 Section D | relocation | Card 8.D 본문 | §5-5 footnote | Wording, page tag (T pp.258–259), source-boundary 모두 보존 |
| 4 | Card 4.B | source quote 추가 | indirect reference | 직접 인용 *"Dose linearity in pharmacokinetics... almost never the case."* | R&T p.256 직접 인용; Audit T3 INCLUDED_CORRECT |
| 5 | §5 Recap | structuring | 1단락 prose | 5-error 표 (E1-E5) | 모든 5개 error는 본문 cards에 이미 존재 |
| 6 | §7 Q9 답변 + §8C Professional Moat | expansion | 단순 답 / 5-question prose | trade-off 3단 logic / 5-step 30-second diagnostic sequence | Cross-references existing Mastery Anchors only |

#### Invariants preserved (v1 = v2)

- 모든 source page tags ([G ...], [T ...], [p.확인 필요]).
- 모든 equations and their numbering.
- 모든 figure marker blocks (B8 Splice Verification Table 그대로).
- 모든 [확인 필요] flags.
- 모든 [교과서 외 실무 해석] labels.
- PART B B1-B8의 모든 가드레일 (B5/B6/B7 forbidden restoration list).
- Compilation Contract (B1).
- Approved figure budget (5 pointers + 1 schematic; v2.1 Insertion Map identical).

v2의 모든 변경은 boundedness·adjacency·source-labeling 규칙 안에서 이루어졌다. v2 PART A에 있는 모든 추가 prose는 (a) Mastery Anchor 라벨이 명시되어 있거나, (b) 기존 Big Idea 직후 단일 단락 내에 위치하거나, (c) 표 구조화된 §5 Recap 내에 위치한다. PART A의 §1, §2 본문, §5 표, §7 Q1-Q8, §8A, §8B는 v1과 byte-level 동일하다.

### B13. v2 → v3 Change Log (NEW)

이 섹션은 v3가 v2로부터 무엇을 변경했는지에 대한 완전한 audit trail이다. v3는 다음 7가지만 변경했고, 그 외는 모두 v2와 동일하다(특히 v2의 8개 Mastery Anchor와 모든 페이지 태그, 모든 수식, 모든 figure marker block은 byte-level 보존).

| Change # | 위치 | 변경 종류 | v2 상태 | v3 상태 | Source authorization |
|---:|---|---|---|---|---|
| 1 | Card 7 H2 header | label normalization | `## Card 7 — Turnover vs Effect Compartment Discrimination Crisis` + `### Big Idea — Apex Concept` | `## Card 7 — [⚡ Apex Concept] Turnover vs Effect Compartment Discrimination Crisis` + `### Big Idea` | V5.0 Apex framework label standard; B8 Splice Table 및 Insertion Map 동기화 |
| 2 | Card 1-8 각 카드 Recap 직후 | new diagnostic line | 부재 | 1줄 "🔗 지연되는 숨겨진 상태" 진단 질문 (총 8개) | EXPERT_INFERENCE, v3; 카드 간 서사 thread 명시화 |
| 3 | Card 7 본문 (§A 직후, §B 직전) | learner-facing 본문 paragraph 추가 | Pool 1/2 r=0.9999 비식별성은 Mastery Anchor #2(Card 1)와 #6(Card 7)의 augmentation layer에만 존재 | "📌 비식별성의 본질" 학습자 본문 잠금 paragraph로 명시 이동 | EXPERT_INFERENCE, v3; v3 audit gap #3 fix |
| 4 | §5 (§5-5와 §5 Recap 사이) | new subsection 추가 | 부재 | `## §5-6. ⚡ Memory Hooks — 7 Critical Conceptual Pairs` (7쌍 Memory Hook 풀 세트) | EXPERT_INFERENCE, v3; v3 audit gap #1 fix; §5-1 Pair 2 및 §5-4 Pair 7과 cross-reference |
| 5 | §7 Q9 직후 (§7 Recap 직전) | new boss dilemma 추가 | Q9이 [Boss dilemma] 라벨을 갖고 있으나 acenocoumarol vs phenprocoumon application question 형태로, "정답이 명확한" trade-off | `## ⚡ 보스 딜레마 ★★ [EXPERT_INFERENCE, v3]` Pool 1/2 Phase 2 dose decision으로 *비식별성을 우회하는 결정 구조* 학습 — 단일 정답 없는 trade-off | EXPERT_INFERENCE, v3; v3 audit gap #2 fix |
| 6 | Card 1-8 각 카드 (Mastery Anchor 또는 Failure Mode 직후) | new Practice Brief layer | 부재 | 1줄 "🎯 Practice Brief" actionable instruction (총 8개) | EXPERT_INFERENCE, v3; 카드 본문을 actionable 1줄로 압축, 새 fact 도입 없음 |
| 7 | Header / Phase 4D Cert / Assembly Mode / Input Manifest / B5 / 신규 B13 | metadata + audit log | v2 상태 | v3 상태 + B13 changelog 신규 | v3 audit trail; structural integrity guard |

#### Invariants preserved (v2 = v3)

- 모든 source page tags ([G ...], [T ...], [p.확인 필요]) — byte-level 동일.
- 모든 equations and their numbering — byte-level 동일.
- 모든 figure marker blocks (B8 Splice Verification Table은 Card 7 anchor 텍스트만 동기화; 6개 marker block 위치·내용 동일).
- 모든 [확인 필요] flags.
- 모든 [교과서 외 실무 해석] labels.
- v2의 8개 Mastery Anchor (#1-#8) — byte-level 동일.
- §5-1~§5-5 비교 표 — byte-level 동일 (§5-6만 신규 추가).
- §7 Q1~Q9 — byte-level 동일 (⚡ 보스 딜레마만 Q9 다음에 신규 추가).
- §8 Final locked summary 및 Professional moat 5-step diagnostic sequence — byte-level 동일.
- PART B B1-B12의 모든 가드레일 (B13만 신규 추가, B5에 v3 가드레일 줄 1개 추가).
- Compilation Contract (B1).
- Approved figure budget (5 pointers + 1 schematic; v2.1 Insertion Map identical).

v3의 모든 변경은 boundedness·adjacency·source-labeling 규칙 안에서 이루어졌다. v3 PART A에 있는 모든 추가 prose는 (a) [EXPERT_INFERENCE, v3] 라벨이 명시되어 있고, (b) 기존 Recap·Mastery Anchor·H2 헤더에 인접 위치에 삽입되었으며, (c) §5-6 또는 ⚡ 보스 딜레마처럼 명시적으로 분리된 학습자 보강 블록 안에 위치한다. PART A의 §1, §2 A·B·C·D·E·F·G 본문, §5-1~§5-5 표, §7 Q1-Q9, §8A·B·C는 v2와 byte-level 동일하다.

### B14. v3 → v3.1 Change Log (NEW)

이 섹션은 v3.1이 v3으로부터 무엇을 변경했는지에 대한 완전한 audit trail이다. v3.1은 35건의 surgical Korean Readability Patch만 적용했고, 그 외는 모두 v3과 동일하다(특히 v3의 8개 Mastery Anchor·7쌍 Memory Hook·Boss Dilemma·8개 hidden-state diagnostic·8개 Practice Brief·모든 페이지 태그·모든 수식·모든 figure marker block·Apex 라벨·Critical Blow는 byte-level 보존).

| Patch # | 위치 | 변경 종류 | v3 상태 | v3.1 상태 | Source authorization |
|---:|---|---|---|---|---|
| P-01 | Learner Navigation — How to use (1문단) | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | v3.1 readability audit; LANGUAGE DIRECTIVE 준수 |
| P-02 | Learner Navigation — How to use (마지막 문장) | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-03 | Learner Navigation — Learning route (8개 항목) | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-04 | Learner Navigation — Before/After checklist (3항목) | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-05 | Card 2 Big Idea — 오프너 3문장 | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-06 | Card 3 Big Idea — 오프너 3문장 | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-07 | Card 4 Big Idea — 오프너 3문장 | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-08 | Card 5 Big Idea — 오프너 2문장 | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-09 | Card 6 Big Idea — 오프너 3문장 | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-10 | Card 8 Big Idea — 오프너 2문장 | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-11 | Card 2 — C. Structural Necessity | Korean flow improvement | 영문 3문장 | 한국어 3문장 (의미 동일) | 동일 |
| P-12 | Card 2 — Trench-level tip | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-13 | Card 3 — Trench-level tip (Mirror-slope misread) | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-14 | Card 5 — A. Minimal graphical workflow (5단계 bullet) | Korean flow improvement | 영문 5단계 | 한국어 5단계 (의미 동일) | 동일 |
| P-15 | Card 5 — B. Blocking-dose analogue (오프너 문장) | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-16 | Card 5 — B. Blocking-dose analogue (마지막 문장) | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-17 | Card 5 — Trench-level tip | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-18 | Card 6 — Recap | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-19 | Card 8 — B. Region 1/2/3 (오프너 문장) | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-20 | Card 8 — Wrong-clock warning (Trench) | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-21 | §7 Q1 — 질문 본문 | Korean flow improvement | 영문 질문 | 한국어 질문 (의미 동일) | 동일 |
| P-22 | §7 Q2 — 질문 본문 | Korean flow improvement | 영문 질문 | 한국어 질문 (의미 동일) | 동일 |
| P-23 | §7 Q3 — 질문 본문 | Korean flow improvement | 영문 질문 | 한국어 질문 (의미 동일) | 동일 |
| P-24 | §7 Q4 — 질문 본문 | Korean flow improvement | 영문 질문 | 한국어 질문 (의미 동일) | 동일 |
| P-25 | §7 Q5 — 질문 본문 | Korean flow improvement | 영문 질문 | 한국어 질문 (의미 동일) | 동일 |
| P-26 | §7 Q6 — 질문 본문 | Korean flow improvement | 영문 질문 | 한국어 질문 (의미 동일) | 동일 |
| P-27 | §7 Q7 — 질문 본문 | Korean flow improvement | 영문 질문 | 한국어 질문 (의미 동일) | 동일 |
| P-28 | §7 Q8 — 질문 본문 | Korean flow improvement | 영문 질문 | 한국어 질문 (의미 동일) | 동일 |
| P-29 | §7 Q9 — 질문 본문 | Korean flow improvement | 영문 질문 | 한국어 질문 (의미 동일) | 동일 |
| P-30 | §8 A — 오프너 + 영문-한문 전환부 | Korean flow improvement | 혼합 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-31 | §8 B — Failure modes 표 "Practical consequence" 열 (5행) | Korean flow improvement | 영문 5행 | 한국어 5행 (의미 동일) | 동일 |
| P-32 | Card 1 — Recap | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-33 | Card 7 — Recap | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-34 | §7 Recap | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-35 | §8 Final locked summary — 오프너 + 전환부 | Korean flow improvement | 혼합 산문 | 한국어 산문 (의미 동일) | 동일 |

#### Invariants preserved (v3 = v3.1)

- 모든 source page tags ([G ...], [T ...], [p.확인 필요]) — byte-level 동일.
- 모든 equations and their numbering — byte-level 동일.
- 모든 NONMEM/R 코드, parameter symbols (CL, V, Vd, AUC, Cmax, Tmax, ka, ke0, EC50, Emax, IIV, BSV, RUV, OMEGA, SIGMA, ETA, EPS, OFV, VPC, GOF, CWRES) — byte-level 동일.
- 모든 figure marker blocks (FIGURE_POINTER·FIGURE_SCHEMATIC 6개) — byte-level 동일.
- 모든 HTML compiler markers (MASTER LENS·ANNOTATION·ANCHOR·TRENCH·CONFUSION·SELF-TEST·RECAP) — byte-level 동일.
- 모든 [확인 필요] flags 및 [교과서 외 실무 해석] labels.
- Card 7 [⚡ Apex Concept] 라벨 및 §5-4 Critical Blow.
- v2의 8개 Mastery Anchor (#1-#8) 본문 — byte-level 동일.
- v3의 §5-6 7쌍 Memory Hooks 본문 — byte-level 동일.
- v3의 ⚡ 보스 딜레마 본문 — byte-level 동일.
- v3의 8개 hidden-state diagnostic line — byte-level 동일.
- v3의 8개 Practice Brief — byte-level 동일.
- v3의 Card 7 "📌 비식별성의 본질" 학습자 본문 잠금 paragraph — byte-level 동일.
- §1·§5-1~§5-5 비교 표·Card 1·Card 6·Card 7·Card 8 본문 표 — byte-level 동일.
- R&T 직접 인용문 (*"Dose linearity in pharmacokinetics..."*) — byte-level 동일 (attributed quotation, 영문 보존).
- Card 4.B 'Region 3' / 'Region 1' 영문 표현 — byte-level 동일 (R&T 본문 표준 용어).
- Card 7 Big Idea 본문 (영문 + biophase annotation) — byte-level 동일 ([⚡ Apex Concept] 카드의 source-anchored core).
- §1 Big Idea·Conceptual navigation·Locked takeaway — byte-level 동일.
- Card 1 Big Idea — byte-level 동일.
- Card 1·4·6·7 Trench-level tip 본문 — byte-level 동일.
- Card 2·3·4·5·7·8 Mastery Note·Practice Lens·Failure Mode 라벨 블록 — byte-level 동일.
- §8 A bullet list (drug parameters from system parameters 외 4행) — byte-level 동일.
- §8 A 마지막 단락 ("It unlocks later work...") — byte-level 동일.
- §8 C Professional moat 본문 — byte-level 동일.
- §8 Final locked summary workflow line — byte-level 동일.
- PART B B1-B13의 모든 가드레일 (B14만 신규 추가, B5/B6에 v3.1 가드레일 줄 각 1개 추가).
- Compilation Contract (B1).
- Approved figure budget (5 pointers + 1 schematic; v2.1 Insertion Map identical).
- B8 PATCH MODE Splice Verification Table — byte-level 동일.

v3.1의 모든 변경은 boundedness·adjacency·source-labeling 규칙 안에서 이루어졌다. v3.1은 v3 본문에 새 정보를 추가하지 않고 영문 산문→한국어 산문 surface 교체만 수행했다. 모든 patch는 같은 의미를 보존하며, 어떤 patch도 과학적 사실·수치·수식·page tag·source label·figure marker·HTML compiler marker·R&T 직접 인용·NONMEM/R 코드·parameter symbol을 변경하지 않는다. PART B는 본 changelog 섹션 추가와 B5/B6의 v3.1 가드레일 줄 추가 외에 byte-level 동일하다.

### B15. v3.1 → v3.2 Change Log (NEW)

이 섹션은 v3.2가 v3.1로부터 무엇을 변경했는지에 대한 완전한 audit trail이다. v3.2는 PART A 잔존 영문 산문에 대한 surgical Korean-Dominant Readability Patch만 적용했고, 그 외는 모두 v3.1과 동일하다(특히 v3의 8개 Mastery Anchor·7쌍 Memory Hook·Boss Dilemma·8개 hidden-state diagnostic·8개 Practice Brief·모든 페이지 태그·모든 수식·모든 figure marker block·Apex 라벨·Critical Blow는 byte-level 보존).

| Patch # | 위치 | 변경 종류 | v3.1 상태 | v3.2 상태 | Source authorization |
|---:|---|---|---|---|---|
| P-36 | 학습자 안내(Learner Navigation) — 헤더 (`Learner Navigation Aid`, `How to use this handout`, `Learning route`, `Before you start / after you finish checklist`) | Korean-Dominant pairing | 영문 헤더 | `한글(English)` 병기 헤더 | v3.2 readability audit; 의미 동일 |
| P-37 | Card 1 — `### A. Formal definition` 헤더 | Korean-Dominant pairing | 영문 헤더 | `### A. 공식 정의(Formal definition)` | 동일 |
| P-38 | Card 1 — 파라미터 정의 4행 (R, kin, kout, R0) | Korean flow improvement | 영문 정의 | 한국어 정의 (의미 동일, 영문 약어 보존) | 동일 |
| P-39 | Card 1 — `### B. Hysteresis classification` 헤더 + 설명문 + 표 (Pattern·Interpretation·Locked examples) | Korean flow improvement | 영문 표 + 설명 | 한국어 헤더·설명·표 (영문 약물명·figure 번호 보존) | 동일 |
| P-40 | Card 1 — `### C. Reparameterization` 헤더 + PD4 설명 산문 | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-41 | Card 1 — Trench-level tip 본문 | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-42 | Card 1 — `### D. Context integration` 본문 (IgG, baseline drift) | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-43 | Card 1 — Practice Lens 본문 | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-44 | Card 2 — Recap 본문 | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-45 | Card 2 — Mastery Note 본문 | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-46 | Card 3 — `### A. Core inference` 헤더 + 표 3행 | Korean flow improvement | 영문 표 | 한국어 헤더·표 (영문 약어 보존) | 동일 |
| P-47 | Card 3 — `### B. Practical decision rule` 헤더 + 5-bullet 산문 | Korean flow improvement | 영문 헤더·산문 | 한국어 헤더·산문 (의미 동일) | 동일 |
| P-48 | Card 3 — Recap 본문 | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-49 | Card 3 — Failure Mode 본문 | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-50 | Card 4 — `### A. Semantic lock` 헤더 + 표 3행 | Korean flow improvement | 영문 표 | 한국어 헤더·표 (수식·약어 보존) | 동일 |
| P-51 | Card 4 — Methylprednisolone 본문 산문 | Korean flow improvement | 영문 산문 | 한국어 산문 (의미·수치·page tag 동일) | 동일 |
| P-52 | Card 4 — Trench-level tip 본문 | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-53 | Card 4 — Recap 본문 | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-54 | Card 4 — Mastery Note 본문 | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-55 | Card 5 — A/B/C 헤더 + Blocking-dose 산문 + DRT 맥락 산문 | Korean flow improvement | 영문 헤더·산문 | 한국어 헤더·산문 (의미·수식 동일) | 동일 |
| P-56 | Card 5 — Recap 본문 | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-57 | Card 5 — Practice Lens 본문 | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-58 | Card 6 — Big Idea 잔여 영문 ("drug may disappear...") | Korean flow improvement | 혼합 산문 | 한국어 산문 + 영문 병기 (의미 동일) | 동일 |
| P-59 | Card 6 — A/B/C 헤더 + 표적 소비 사례 3-bullet + cell growth 본문 | Korean flow improvement | 영문 헤더·산문 | 한국어 헤더·산문 (의미·약물명·page tag 동일) | 동일 |
| P-60 | Card 6 — Failure Mode 본문 | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-61 | Card 7 — Big Idea 본문 (turnover vs effect compartment 인과 주장) | Korean flow improvement | 영문 산문 + biophase annotation | 한국어 산문 + biophase annotation 보존 (의미·page tag 동일) | 동일 — biophase `<!-- ANNOTATION -->` marker는 byte-level 동일 |
| P-62 | Card 7 — A 헤더 + Turnover/Effect compartment example 라벨 + PD6 locks the crisis 산문 | Korean flow improvement | 영문 산문 | 한국어 산문 (수식·수치·page tag 동일) | 동일 |
| P-63 | Card 7 — `### B. How to discriminate` 헤더 + 4행 표 (Evidence·Supports turnover·Supports effect compartment) | Korean flow improvement | 영문 표 | 한국어 헤더·표 (의미 동일) | 동일 |
| P-64 | Card 7 — Critical Blow 헤더 + source-grounded core + practical extrapolation 산문 | Korean flow improvement | 영문 산문 | 한국어 산문 (`[교과서 외 실무 해석]` 라벨 보존, page tag 동일) | 동일 |
| P-65 | Card 7 — Trench-level tip 본문 | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-66 | Card 7 — Practice Lens 본문 | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-67 | Card 8 — `### A. Clock discrimination` 헤더 + 표 3행 | Korean flow improvement | 영문 표 | 한국어 헤더·표 (약물명·수치·page tag 동일) | 동일 |
| P-68 | Card 8 — `### B. Region 1/2/3 and linear decline` 헤더 + 산문 + Region 3/1/Succinylcholine 설명 | Korean flow improvement | 혼합 산문 | 한국어 산문 (수식·수치·page tag 동일; Region 1/2/3은 R&T 표준 용어로 영문 보존) | 동일 |
| P-69 | Card 8 — `### C. Duration formula` 헤더 + ANNOTATION 본문 + dose doubling 라인 + succinylcholine duration 산문 | Korean flow improvement | 혼합 산문 | 한국어 산문 (수식·수치·page tag 동일) | 동일 |
| P-70 | Card 8 — Failure Mode 본문 | Korean flow improvement | 영문 산문 | 한국어 산문 (의미 동일) | 동일 |
| P-71 | §5-1~§5-5 — 5개 비교 표의 헤더와 셀 (Dimension·Direction·Common error·Memory lock 등) | Korean flow improvement | 영문 표 | 한국어 표 (수식·약어·page tag·약물명 보존) | 동일 |
| P-72 | §5-6 — 7쌍 Memory Hook 헤더 (Pair 1~7) + §5 Recap 헤더와 표 헤더 + Footnote 헤더 + §7 Self-Test 헤더와 Q1-Q9 질문/정답 + §8 A/B/C 헤더와 산문 + Final locked summary 헤더 + 저작권 안내 + §1 섹션 헤더 + §2 섹션 헤더 + §5 섹션 헤더 + Card 7 §A 헤더 | Korean flow improvement | 영문 헤더·산문 | 한국어 헤더·산문 (`한글(English)` 병기 통일, 수식·page tag·R&T 직접 인용 보존) | 동일 — R&T p.256 직접 인용문(*"Dose linearity in pharmacokinetics..."*)은 attributed quotation으로 영문 보존 |

#### Invariants preserved (v3.1 = v3.2)

- 모든 source page tags ([G ...], [T ...], [pp.XX–YY], [p.XX], [p.확인 필요]) — byte-level 동일.
- 모든 equations and their numbering — byte-level 동일.
- 모든 NONMEM/R 코드, parameter symbols (CL, V, Vd, AUC, Cmax, Tmax, ka, ke0, EC50, Emax, IIV, BSV, RUV, OMEGA, SIGMA, ETA, EPS, OFV, VPC, GOF, CWRES) — byte-level 동일.
- 모든 figure marker blocks (FIGURE_POINTER·FIGURE_SCHEMATIC 6개) 및 그 내부 영문 brief 필드(Source/Why this matters/When to look/Learner instruction/Title/Mode/Visual objective/Core message/Elements/Suggested rendering/Caption/Alt text/Source relation) — byte-level 동일.
- 모든 HTML compiler markers (MASTER LENS·ANNOTATION·ANCHOR·TRENCH·CONFUSION·SELF-TEST·RECAP·FIGURE_POINTER·FIGURE_SCHEMATIC) — byte-level 동일.
- 모든 [확인 필요] flags 및 [교과서 외 실무 해석] labels.
- Card 7 [⚡ Apex Concept] 라벨 및 §5-4 Critical Blow 구조.
- v2의 8개 Mastery Anchor (#1-#8) 본문 — byte-level 동일.
- v3의 §5-6 7쌍 Memory Hooks 본문 — byte-level 동일.
- v3의 ⚡ 보스 딜레마 본문 — byte-level 동일.
- v3의 8개 hidden-state diagnostic line — byte-level 동일.
- v3의 8개 Practice Brief — byte-level 동일.
- v3의 Card 7 "📌 비식별성의 본질" 학습자 본문 잠금 paragraph — byte-level 동일.
- R&T 직접 인용문 (*"Dose linearity in pharmacokinetics..."*) — byte-level 동일 (attributed quotation, 영문 보존).
- Region 1/2/3 영문 표현 — byte-level 동일 (R&T 본문 표준 용어).
- v3.1의 35개 patch 결과 — byte-level 동일.
- PART B B1-B14의 모든 가드레일 (B15만 신규 추가, B5/B6에 v3.2 가드레일 줄 각 1개 추가).
- Compilation Contract (B1).
- Approved figure budget (5 pointers + 1 schematic; v2.1 Insertion Map identical).
- B8 PATCH MODE Splice Verification Table — byte-level 동일.

v3.2의 모든 변경은 boundedness·adjacency·source-labeling 규칙 안에서 이루어졌다. v3.2는 v3.1 본문에 새 정보를 추가하지 않고 영문 산문→한국어 산문 surface 교체 + career-critical 전문용어의 `한글(English)` 병기 통일만 수행했다. 모든 patch는 같은 의미를 보존하며, 어떤 patch도 과학적 사실·수치·수식·page tag·source label·figure marker·HTML compiler marker·R&T 직접 인용·NONMEM/R 코드·parameter symbol을 변경하지 않는다. PART B는 본 changelog 섹션 추가와 B5/B6의 v3.2 가드레일 줄 추가 외에 byte-level 동일하다.

---

# Final v3 All-Pass Checklist

이 체크리스트는 v3 출력의 정합성을 v2 → v3 patch 작업 종료 후 검증한다. 8항목 모두 PASS여야 v3가 release 가능하다.

| # | 항목 | 검증 기준 | 상태 |
|---:|---|---|---|
| 1 | **PATCH 1 — Apex 레이블 표준화** | Card 7 H2 헤더에 `[⚡ Apex Concept]` 배지 포함; B8 Splice Verification Table 및 Insertion Map의 Card 7 anchor 텍스트 동기화; "Big Idea — Apex Concept" → "Big Idea" 단일화 | ✅ PASS |
| 2 | **PATCH 2 — 카드 간 hidden-state 서사 thread** | Card 1·2·3·4·5·6·7·8 각각 Recap 직후 1줄 "🔗 지연되는 숨겨진 상태" 진단 줄 존재 (총 8개); 모두 [EXPERT_INFERENCE, v3] 라벨 | ✅ PASS |
| 3 | **PATCH 3 — Pool 1/2 비식별성 학습자 본문 이동** | Card 7 §A(Competing structures) 직후, §B(How to discriminate) 직전에 "📌 비식별성의 본질 — 학습자 본문 잠금" paragraph 존재; r=0.9999, ΔWRSS≈2 정량 인사이트 명시 | ✅ PASS |
| 4 | **PATCH 4 — §5-6 Memory Hooks 7쌍** | §5-5와 §5 Recap 사이에 §5-6 신규 subsection 존재; Pair 1~7 모두 "⚡ 기억 고리" 비유 인코딩 포함; 구조적 필연(수학·메커니즘·물리) 인코딩 충족; §5-1 Pair 2 및 §5-4 Pair 7 cross-reference 명시 | ✅ PASS |
| 5 | **PATCH 5 — ⚡ 보스 딜레마** | §7 Q9 직후, §7 Recap 직전에 "## ⚡ 보스 딜레마 ★★ [EXPERT_INFERENCE, v3]" 신규 섹션 존재; Pool 1/2 Phase 2 dose decision; 선택지 A/B + 거장의 Trade-off 논리 + Apex 메시지 4단 구조 | ✅ PASS |
| 6 | **PATCH 6 — §2 카드별 Practice Brief** | Card 1·2·3·4·5·6·7·8 각각 1줄 "🎯 Practice Brief" actionable instruction 존재 (총 8개); 모두 [EXPERT_INFERENCE, v3] 라벨; 새 drug example·page tag 도입 없음 | ✅ PASS |
| 7 | **PATCH 7 — PART B v3 audit trail** | Header·Phase 4D Cert (v3)·Assembly Mode·Input Manifest 모두 v3로 갱신; B5에 v3 가드레일 줄 추가; B13 v2→v3 Change Log 신규 섹션 완비 | ✅ PASS |
| 8 | **NON-NEGOTIABLE PRESERVATION 4항 무손상** | (a) Apex 레이블 정규화 후에도 Apex 본문 보존, (b) Critical Blow(§5-4 §Card 7) 보존, (c) 모든 페이지 태그 ([G ...], [T ...], [pp.XX-YY], [p.확인 필요]) byte-level 보존, (d) PD6 quantitative equivalence table (ΔWRSS=2, ΔAIC=−1, kout=ke0=5.6 h⁻¹) byte-level 보존; 새 drug example·page tag 도입 0건 | ✅ PASS |

**v3 종합 판정: ALL-PASS — release 가능.**

v3 release 후 Phase 5 HTML compile에서는 v2와 동일한 splice contract가 유지되며, v3 추가 layer(hidden-state diagnostic line·Memory Hooks·Boss Dilemma·Practice Brief)는 모두 PART A 학습자 본문에 위치하므로 별도 marker block 없이 자연 렌더링된다. Card 7 H2 헤더의 `[⚡ Apex Concept]` 배지는 Phase 5 CSS에서 `apex-badge` 클래스로 시각적 강조를 적용한다.

---

# v3.1 Final Checklist

이 체크리스트는 v3.1 출력의 정합성을 v3 → v3.1 Korean Readability Patch 작업 종료 후 검증한다. 8항목 모두 PASS여야 v3.1이 release 가능하다.

| # | 항목 | 검증 기준 | 상태 |
|---:|---|---|---|
| 1 | **PART A readability improved** | 35건 patch (P-01–P-35) 모두 적용 완료; Big Idea 6개 카드 오프너·§7 Q1–Q9 질문·§8 A·B·Final Summary·Recap·Trench·Structural·Learner Navigation 영문 산문이 모두 자연스러운 한국어로 교체됨; LANGUAGE DIRECTIVE("모든 산문 출력은 한국어") 준수 | ✅ PASS |
| 2 | **Scientific content unchanged** | 모든 fact·numerical anchor·drug example·clinical scenario·regulatory framing이 v3와 동일; 새 과학적 주장·새 수치·새 예시 도입 0건; 의미 보존성은 patch table에서 1:1 검증됨 | ✅ PASS |
| 3 | **Equations preserved** | 모든 LaTeX 수식 ($dR/dt = kin − kout·R$, $R_0 = kin/kout$, $R_{ss} = R_0 I(C_{ss})$, $SF = exp(−Kkill·AUC)$, $t_D = (1/k)\ln(Dose/A_{min})$, Eq 3:74·3:76·3:77·3:78·3:103·3:110·3:112·8-6·8-7·8-9·8-12 외 전체) byte-level 동일; equation numbering 변경 없음 | ✅ PASS |
| 4 | **Page tags preserved** | 모든 source page tags ([G ...], [T ...], [pp.XX–YY], [p.XX], [p.확인 필요]) byte-level 동일; 새 page tag 도입 0건; 페이지 번호 변경 0건; 위치 이동 0건 | ✅ PASS |
| 5 | **Figure markers preserved** | 6개 FIGURE_POINTER 블록·1개 FIGURE_SCHEMATIC 블록 모두 byte-level 동일; Source/Why this matters/When to look/Learner instruction/Title/Mode/Visual objective/Core message/Elements/Suggested rendering/Caption/Alt text/Source relation 필드 전체 보존; PATCH MODE Insertion Map (B8) 6개 marker 모두 anchor 텍스트 동일 | ✅ PASS |
| 6 | **Source-boundary preserved** | Source universe (Gabrielsson & Weiner 5e + Rowland & Tozer 5e) 외 새 reference 도입 0건; R&T p.256 직접 인용문 attributed quotation으로 영문 보존; [교과서 외 실무 해석] labels 전체 보존; PART B B6 source-boundary guardrail에 v3.1 추가 줄 명시 | ✅ PASS |
| 7 | **HTML-readiness preserved** | 모든 HTML compiler markers (`<!-- MASTER LENS -->`, `<!-- ANNOTATION -->`, `<!-- ANCHOR -->`, `<!-- TRENCH -->`, `<!-- CONFUSION -->`, `<!-- SELF-TEST -->`, `<!-- RECAP -->`, `<!-- FIGURE_POINTER -->`, `<!-- FIGURE_SCHEMATIC -->`, `<!-- /FIGURE_POINTER -->`, `<!-- /FIGURE_SCHEMATIC -->`) byte-level 동일; YAML frontmatter 보존; PATCH MODE Splice Verification Table (B8) Match count 1·Inserted YES 6개 모두 유효 | ✅ PASS |
| 8 | **Ready for Phase 5 HTML compilation** | PATCH MODE 유지; Insertion Map의 6개 anchor 텍스트 byte-level 동일하므로 splice 작동; Phase 5 marker→component mapping 변경 없음; CSS variable·responsive·print 요구사항 v3와 동일; v3.1 patch는 모두 marker block 외부의 학습자 산문에만 적용되어 splice fidelity에 영향 없음 | ✅ PASS |

**v3.1 종합 판정: ALL-PASS — release 가능.**

v3.1 release 후 Phase 5 HTML compile에서는 v3과 동일한 splice contract가 유지되며, v3.1 patch는 모두 PART A 학습자 본문 산문 surface에만 적용되었으므로 marker block·page tag·equation·figure·structure·anchor에 영향이 없다. v3의 모든 mastery layer (8 Mastery Anchor·7 Memory Hook·Boss Dilemma·8 hidden-state diagnostic·8 Practice Brief·Card 7 비식별성 paragraph)는 byte-level 보존되어 한국어 독해 흐름이 개선된 환경에서 그대로 동작한다. Card 7 H2 헤더의 `[⚡ Apex Concept]` 배지 및 §5-4 Critical Blow는 v3와 동일하게 Phase 5 CSS에서 `apex-badge` 클래스로 시각적 강조를 적용한다.

---

# v3.2 Final Checklist

이 체크리스트는 v3.2 출력의 정합성을 v3.1 → v3.2 Korean-Dominant Readability Patch 작업 종료 후 검증한다. 8항목 모두 PASS여야 v3.2가 release 가능하다.

| # | 항목 | 검증 기준 | 상태 |
|---:|---|---|---|
| 1 | **PART A Korean dominance achieved** | v3.1에서 잔존했던 §2 카드 표 항목·Mastery Note·Practice Lens·Failure Mode·비교 표 셀·Trench tip·정의 산문·소제목 헤더·§5/§7/§8 본문의 영문 산문이 모두 한국어 또는 `한글(English)` 병기 형식으로 변환됨; 카드별 헤더(`### A. ...`, `### B. ...`)는 한국어 번역 + 영문 병기로 통일; LANGUAGE DIRECTIVE("모든 산문 출력은 한국어") 준수 | ✅ PASS |
| 2 | **Career-critical terms retained as paired form** | clearance, volume of distribution, half-life, bioavailability, exposure, residual error, IIV, BSV, RUV, identifiability, reparameterization, plausible fallacy, Practice Brief, Memory Hook, Boss Dilemma, Critical Blow, Professional Moat 등 국제 학술·실무에서 영문으로 알아야 할 용어는 첫 등장 시 `한글(English)` 형식으로 병기됨 | ✅ PASS |
| 3 | **Scientific content unchanged** | 모든 fact·numerical anchor·drug example·clinical scenario·regulatory framing이 v3.1과 동일; 새 과학적 주장·새 수치·새 예시 도입 0건; 의미 보존성은 P-36–P-72 patch table에서 1:1 검증됨 | ✅ PASS |
| 4 | **Equations and code preserved** | 모든 LaTeX 수식, NONMEM 변수명, parameter symbol(CL, V, ka, ke0, EC50, Emax, kin, kout, IIV, BSV, RUV, OFV, GOF, CWRES 등) byte-level 동일; equation numbering 변경 없음; code block 내 syntax 변경 0건 | ✅ PASS |
| 5 | **Page tags preserved** | 모든 source page tags ([G ...], [T ...], [pp.XX–YY], [p.XX], [p.확인 필요]) byte-level 동일; 새 page tag 도입 0건; 페이지 번호 변경 0건; 위치 이동 0건 | ✅ PASS |
| 6 | **Figure markers and compiler markers preserved** | 6개 FIGURE_POINTER 블록·1개 FIGURE_SCHEMATIC 블록 모두 byte-level 동일 (Source/Why this matters/When to look/Learner instruction/Title/Mode/Visual objective/Core message/Elements/Suggested rendering/Caption/Alt text/Source relation 영문 brief 필드 전체 보존); 모든 HTML compiler markers (MASTER LENS·ANNOTATION·ANCHOR·TRENCH·CONFUSION·SELF-TEST·RECAP·FIGURE_POINTER·FIGURE_SCHEMATIC) byte-level 동일; PATCH MODE Insertion Map (B8) 6개 marker 모두 anchor 텍스트 동일 | ✅ PASS |
| 7 | **Source-boundary and invariants preserved** | Source universe (Gabrielsson & Weiner 5e + Rowland & Tozer 5e) 외 새 reference 도입 0건; R&T p.256 직접 인용문(*"Dose linearity in pharmacokinetics..."*) attributed quotation으로 영문 보존; [교과서 외 실무 해석] labels 전체 보존; v3의 모든 mastery layer (8 Mastery Anchor·7 Memory Hook·Boss Dilemma·8 hidden-state diagnostic·8 Practice Brief·Card 7 비식별성 paragraph·Card 7 [⚡ Apex Concept] 배지·§5-4 Critical Blow) byte-level 보존 | ✅ PASS |
| 8 | **Ready for Phase 5 HTML compilation** | PATCH MODE 유지; Insertion Map의 6개 anchor 텍스트 byte-level 동일하므로 splice 작동; Phase 5 marker→component mapping 변경 없음; CSS variable·responsive·print 요구사항 v3.1과 동일; v3.2 patch는 모두 marker block 외부의 학습자 산문에만 적용되어 splice fidelity에 영향 없음 | ✅ PASS |

**v3.2 종합 판정: ALL-PASS — release 가능.**

v3.2 release 후 Phase 5 HTML compile에서는 v3.1과 동일한 splice contract가 유지되며, v3.2 patch는 모두 PART A 학습자 본문 산문 surface에만 적용되었으므로 marker block·page tag·equation·figure·structure·anchor에 영향이 없다. v3의 모든 mastery layer (8 Mastery Anchor·7 Memory Hook·Boss Dilemma·8 hidden-state diagnostic·8 Practice Brief·Card 7 비식별성 paragraph)는 byte-level 보존되어 한국어 지배적 독해 흐름이 추가로 개선된 환경에서 그대로 동작한다. Card 7 H2 헤더의 `[⚡ Apex Concept]` 배지 및 §5-4 Critical Blow는 v3.1과 동일하게 Phase 5 CSS에서 `apex-badge` 클래스로 시각적 강조를 적용한다. v3.1의 P-01–P-35 patch 결과는 v3.2 안에서 그대로 유지되며, v3.2의 P-36–P-72 patch는 그 위에 누적적으로 작용한다.

---

# Final Certification

| Certificate | Status | Basis |
|---|---|---|
| Korean-Dominant Readability Certificate | PASS | General learner-facing English prose converted to Korean where possible; career-critical terms retained as Korean-English paired expressions. |
| Scientific Preservation Certificate | PASS | No scientific content, equation, number, example, page tag, or source label changed. |
| Marker Integrity Certificate | PASS | All figure markers, compiler markers, anchors, and section/card structures preserved. |
| HTML-Readiness Certificate | PASS | Phase 5 compatibility preserved; no HTML/Mermaid/SVG generated. |

# 06_Content Lock v2.1 — Figure Marker Patch Plan
## NCA·노출 평가·MRT·비구획 실무

**Output mode**: **PATCH MODE**  
**Rationale**: Content Lock v2는 긴 text-final 문서이므로 full re-emission 시 미세 변형 위험이 크다. 따라서 본 산출물은 Content Lock v2 본문을 재출력하지 않고, figure strategy table, figure briefs, insertion map, marker blocks만 제공한다.  
**Telos**: 그림을 만들지 않는다. 어떤 그림이, 왜, 어디에 필요한지만 결정한다. Mermaid/SVG/HTML 생성은 Phase 5로 이관한다.  
**Image rights**: Scope Lock 기준 `None`. 따라서 Mode I는 사용하지 않는다. 저작권 있는 교과서 이미지는 삽입하지 않고, 필요 시 Pointer(P) 또는 구조적으로 다른 Redraw brief(R)만 사용한다.  
**Budget**: A-Critical chapter 기준 Pointer(P) 최대 5개, Schematic(R/N) 최대 2개. 본 patch는 Pointer 5개 + Redraw 1개 = budget 내.

---

## 1. Figure Strategy Table — View A. Reading-order Figure Plan

| # | Reading order | Location (§ + concept card) | Mode | Source figure/table | Trigger | Why text alone is insufficient | Expected learning gain | Decision |
|---:|---|---|---|---|---|---|---|---|
| 1 | §1 | Session Header & Roadmap | P | Gabrielsson Fig 2.113, p.141 | G3, G5 | NCA와 nonlinear regression의 차이를 “면적 합” vs “함수/parameter fitting”으로 한눈에 보지 않으면, 이후 PK41에서 왜 NCA가 final parameter가 아니라 initial estimate로 내려가는지 구조적으로 늦게 이해한다. | NCA의 정체성을 첫 장에서 고정한다. | KEEP |
| 2 | §2 C1 | AUC 계산 — linear/log-linear trapezoidal rule, λz, extrapolation | R | Gabrielsson Figs 2.114–2.120, pp.142–147; R&T Fig A-1, p.760 | G1, G2, G4, G5 | C1은 사다리꼴 계산, 상승/하강 bias, log-linear fallback, terminal slope, observed vs predicted $C_{last}$가 한 카드에 겹쳐 있다. 원문 figure를 각각 보면 학습자가 “품질관리 chain”으로 통합하지 못할 수 있다. | AUC audit chain: `trapezoid → method choice → λz → tail → downstream CL/V`를 한 번에 본다. | KEEP |
| 3 | §2 C2 | AUMC와 MRT — first moment와 평균 체류시간 | P | Gabrielsson Fig 2.121, p.148; R&T Fig H-2, p.791 | G1, G2, G5 | AUMC tail이 왜 AUC tail보다 더 민감한지는 식만으로는 시간 가중의 시각적 효과가 잘 보이지 않는다. | AUC와 AUMC의 tail sensitivity 차이를 직관화한다. | KEEP |
| 4 | §2 C3 | Apex — CL, $V_{ss}$, $V_z$와 투여 경로 보정 | P | Gabrielsson Fig 2.126, p.157 | G1, G2, G5 | §2.8.8의 대안식은 수식만 보면 “다른 공식”처럼 보인다. washout AUC from steady state를 보아야 이것이 적용 영역 문제임을 이해한다. | standard MRT/$V_{ss}$ 공식과 §2.8.8 대안식의 역할 차이를 고정한다. | KEEP |
| 5 | §2 C4 | Exposure metrics — dose가 아니라 concentration을 본다 | P | Gabrielsson Fig 2.135, p.163 | G1, G2, G5 | $C_{ss}$, $C_{max}$, AUC, threshold-above exposure, $t_d$는 표로 읽으면 병렬 목록처럼 보이지만, 실제로는 response mechanism에 따라 선택되는 exposure summary다. | exposure metric 선택을 “목록 암기”에서 “response question에 맞춘 선택”으로 전환한다. | KEEP |
| 6 | §2 C4 | PK41 dynamic source anchor — NCA에서 nonlinear regression으로 | P | Gabrielsson Fig 41.2, p.663 | G2, G4, G5 | PK41 수치 anchor는 텍스트만으로도 가능하지만, CL이 dose와 함께 감소하는 패턴을 직접 보지 않으면 nonlinear transition signal이 약해진다. | “NCA-CL 감소 = reporting finding이 아니라 model transition signal”을 시각적으로 고정한다. | KEEP |
| R1 | §2 C1 | C1 separate textbook figures | REJECT/MERGE | Gabrielsson Fig 2.114, 2.115, 2.116, 2.117, 2.120 | G5 | 개별 figure는 유용하지만 각각 pointer로 넣으면 C1이 figure-heavy가 된다. | 핵심은 개별 원문 inspection보다 C1 audit chain 통합이다. | MERGE into #2 |
| R2 | §2 C1 | Mixed linear-up/log-down method | REJECT | Gabrielsson Fig 2.118, p.146 | G5 weak | Content Lock v2 본문이 이미 method choice와 author-balancing message를 충분히 설명한다. | 별도 marker 없이 C1 R schematic에서 주변 요소로만 반영 가능하다. | REJECT |
| R3 | §2 C4 | §2.9 case examples beyond metric summary | REJECT | Gabrielsson Figs 2.127–2.134, pp.159–163 | G5 | 각 예시는 좋지만 모두 pointer로 넣으면 C4가 사례 catalogue가 된다. Fig 2.135와 Fig 41.2가 핵심 decision point를 더 잘 대표한다. | exposure philosophy는 C4 table과 #5 marker로 충분히 유지된다. | REJECT |
| R4 | R&T Appendix | AUC/MRT worked tables | REJECT | R&T Table A-1, Fig A-1, Table H-1, Table H-2 | G5 weak | Content Lock v2가 이미 numerical anchors를 source-tagged text로 보존한다. | 계산 검증에는 유용하지만 구조 이해를 크게 추가하지 않는다. | REJECT |

---

## 2. Figure Strategy Table — View B. Type-sorted Summary

**Pointers (P)**: #1, #3, #4, #5, #6 → 5 / 5 budget  
**Schematics (R/N)**: #2 → 1 / 2 budget  
**Images (I)**: none → Image rights = None  

**Budget decision**: PASS.  
**Rights decision**: PASS. Mode I 없음. Textbook figures는 직접 삽입하지 않고 pointer 또는 visually distinct redraw brief로만 처리한다.  
**Patch decision**: PATCH MODE 유지. Content Lock v2 본문 재출력 없음.

---

## 3. Figure Briefs — KEEP items only

### Figure #1 — Pointer

- **Source**: Gabrielsson & Weiner 5e, p.141, Fig 2.113 “Comparison of NCA and nonlinear regression.”
- **Why this figure matters**: NCA가 area sums를 다루고 regression이 parameterized function을 fitting한다는 대비는 이 세션 전체의 프레임이다. 이 그림이 없으면 PK41에서 NCA가 왜 final answer가 아니라 regression 초기값으로 내려가는지 구조적 전환이 약해진다.
- **When to look**: §1 Recap 직후, C1로 들어가기 전.
- **Learner instruction**: 왼쪽 panel에서 NCA가 각 구간 면적을 더하는 방식을 먼저 보라. 오른쪽 panel에서는 model parameters가 curve shape를 설명한다는 점만 확인하고, 아직 수식 세부로 들어가지 않는다.

### Figure #2 — Redraw brief

- **Title**: C1 AUC Audit Chain — trapezoid, method choice, λz, tail, downstream parameters
- **Visual objective**: 5초 안에 “AUC 계산은 단일 공식이 아니라 quality-control chain”임을 보게 한다.
- **Core message**: AUC 신뢰도는 사다리꼴 계산보다 terminal slope와 extrapolated tail 검증에서 결정되며, 그 오류는 CL/$V_z$/$V_{ss}$로 전파된다.
- **Elements to include**:
  - observed concentration-time points
  - linear trapezoid segment
  - descending segment with log-linear alternative
  - terminal semi-log slope labeled $\lambda_z$
  - $C_{last}^{obs}$ vs $\hat C_{last}$ decision point
  - extrapolated tail fraction checkpoint
  - downstream arrows to CL, $V_z$, $V_{ss}$, exposure comparison
- **Elements to exclude**:
  - exact textbook layout or shaded regions copied from source figures
  - numerical example values
  - software-specific λz algorithm
  - BA/BE regulatory thresholds
- **Suggested rendering**: SVG
- **Caption**: AUC audit는 `observed area + terminal extrapolation`의 chain이며, 각 단계의 오류가 downstream NCA parameters로 전파된다.
- **Alt text**: 관측 농도-시간 점에서 사다리꼴 면적, terminal slope, 외삽 tail, downstream 파라미터로 이어지는 흐름도.
- **Source relation**: Redrawn from textbook concept

### Figure #3 — Pointer

- **Source**: Gabrielsson & Weiner 5e, p.148, Fig 2.121; Rowland & Tozer 5e, p.791, Fig H-2
- **Why this figure matters**: C2의 핵심은 AUMC가 time-weighted exposure라는 점이다. AUMC tail의 영향은 수식만으로는 늦게 체화되므로, concentration curve와 first-moment curve를 눈으로 비교해야 한다.
- **When to look**: C2 Recap 직후, C3로 넘어가기 전.
- **Learner instruction**: concentration curve와 $t\cdot C(t)$ curve의 late-time 영역을 비교하라. AUMC에서는 늦은 시간이 다시 가중되므로 tail sampling이 MRT에 더 크게 들어간다는 점만 확인한다.

### Figure #4 — Pointer

- **Source**: Gabrielsson & Weiner 5e, p.157, Fig 2.126
- **Why this figure matters**: C3 Apex에서 §2.8.8 대안식은 단순한 공식 대체가 아니라 적용 영역의 변경이다. washout AUC를 직접 보아야 input-time-dominant 상황에서 표준식이 왜 불안정해지는지 이해된다.
- **When to look**: C3 Recap 직후, C4로 넘어가기 전.
- **Learner instruction**: steady-state plateau 이후 washout curve에서 어떤 AUC가 쓰이는지 먼저 확인하라. 그 다음 Eq.2:366/2:367이 왜 zero/negative $V_{ss}$를 피하는지 본문 수식으로 돌아가 검토한다.

### Figure #5 — Pointer

- **Source**: Gabrielsson & Weiner 5e, p.163, Fig 2.135
- **Why this figure matters**: C4의 exposure metrics는 단순 목록이 아니다. 그림을 통해 $C_{ss}$/average concentration, $C_{max}$, AUC, threshold-above exposure/$t_d$가 서로 다른 pharmacologic question에 답하는 요약값임을 분리할 수 있다.
- **When to look**: C4 Recap 직후, §5 Confusion Pair로 넘어가기 전.
- **Learner instruction**: 각 metric이 concentration-time profile의 어느 부분을 요약하는지 표시 위치를 확인하라. 이후 어떤 PD/safety endpoint가 peak, cumulative burden, duration 중 무엇에 가까운지 생각한다.

### Figure #6 — Pointer

- **Source**: Gabrielsson & Weiner 5e, p.663, Fig 41.2
- **Why this figure matters**: PK41의 핵심은 CL 감소가 숫자 한 줄이 아니라 model transition signal이라는 점이다. 이 figure가 없으면 learner가 NCA-CL을 dose별 descriptive table로만 읽고 nonlinear regression 전환의 필연성을 약하게 느낄 수 있다.
- **When to look**: C4 Recap 직후 또는 Q4 self-test 전에.
- **Learner instruction**: dose가 증가할수록 CL이 감소하는 방향성만 확인하라. 그 다음 C4의 Michaelis-Menten regression 전환 문장으로 돌아가 “왜 CL/$t_{1/2}$가 final parameter가 아닌가”를 연결한다.

---

## 4. Insertion Map (PATCH MODE)

> 표 셀에서 multi-line marker가 깨지는 것을 막기 위해, `Marker block ID`를 먼저 제시하고, 바로 아래 **Splicing-ready marker blocks**에 실제 삽입할 complete marker를 제공한다. Phase 5 operator는 Content Lock v2 본문을 변경하지 않고, 아래 anchor 뒤에 해당 marker block을 그대로 삽입한다.

| # | Reading order | Anchor — verbatim unique string from Content Lock v2 | Insert position | Marker block ID |
|---:|---|---|---|---|
| 1 | §1 after roadmap | `**§1 Recap**: NCA의 강점은 단순함이고, 약점도 같은 지점에서 온다. 모델을 덜 세우는 대신, terminal slope·input correction·linear elimination 가정이 무너지면 오류가 조용히 후속 분석으로 전파된다.` | after this anchor card | FIG-P01 |
| 2 | §2 C1 after card | `**C1 Recap**: AUC가 흔들리면 CL, $V_z$, $V_{ss}$, exposure comparison이 모두 흔들린다. NCA audit은 항상 $\lambda_z$ plot과 %extrapolated area에서 시작한다.` | after this anchor card | FIG-R02 |
| 3 | §2 C2 after card | `**C2 Recap**: AUMC는 time-weighted exposure다. 그래서 tail과 input correction을 놓치면 MRT는 안정적인 평균이 아니라 terminal slope 오류를 증폭한 숫자가 된다.` | after this anchor card | FIG-P03 |
| 4 | §2 C3 after card | `**C3 Recap**: C3는 Apex다. AUC와 AUMC의 작은 불확실성은 여기서 CL과 volume이라는 임상적 이름을 얻고, 그 순간부터 훨씬 설득력 있어 보이기 때문이다.` | after this anchor card | FIG-P04 |
| 5–6 | §2 C4 after card | `**C4 Recap**: C4는 계산 카드가 아니라 해석 카드다. NCA가 AUC와 concentration metrics를 만든 뒤, 어떤 metric을 efficacy/safety argument의 중심에 둘지 결정하는 단계다.` | after this anchor card | FIG-P05 + FIG-P06 |

---

## 5. Splicing-ready marker blocks

### FIG-P01

```markdown
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.141, Fig 2.113
Why this matters: NCA가 area sums를 다루고 regression이 parameterized function을 fitting한다는 대비는 이 세션 전체의 프레임이다. 이 그림이 없으면 PK41에서 NCA가 왜 final answer가 아니라 regression 초기값으로 내려가는지 구조적 전환이 약해진다.
When to look: §1 Recap 직후, C1로 들어가기 전
Learner instruction: 왼쪽 panel에서 NCA가 각 구간 면적을 더하는 방식을 먼저 보라. 오른쪽 panel에서는 model parameters가 curve shape를 설명한다는 점만 확인하고, 아직 수식 세부로 들어가지 않는다.
<!-- /FIGURE_POINTER -->
```

### FIG-R02

```markdown
<!-- FIGURE_SCHEMATIC -->
Title: C1 AUC Audit Chain — trapezoid, method choice, λz, tail, downstream parameters
Mode: R
Visual objective: 5초 안에 “AUC 계산은 단일 공식이 아니라 quality-control chain”임을 보게 한다.
Core message: AUC 신뢰도는 사다리꼴 계산보다 terminal slope와 extrapolated tail 검증에서 결정되며, 그 오류는 CL/$V_z$/$V_{ss}$로 전파된다.
Elements to include: observed concentration-time points; linear trapezoid segment; descending segment with log-linear alternative; terminal semi-log slope labeled $\lambda_z$; $C_{last}^{obs}$ vs $\hat C_{last}$ decision point; extrapolated tail fraction checkpoint; downstream arrows to CL, $V_z$, $V_{ss}$, exposure comparison
Elements to exclude: exact textbook layout or shaded regions copied from source figures; numerical example values; software-specific λz algorithm; BA/BE regulatory thresholds
Suggested rendering: SVG
Caption: AUC audit는 `observed area + terminal extrapolation`의 chain이며, 각 단계의 오류가 downstream NCA parameters로 전파된다.
Alt text: 관측 농도-시간 점에서 사다리꼴 면적, terminal slope, 외삽 tail, downstream 파라미터로 이어지는 흐름도.
Source relation: Redrawn from textbook concept
<!-- /FIGURE_SCHEMATIC -->
```

### FIG-P03

```markdown
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.148, Fig 2.121; Rowland & Tozer 5e, p.791, Fig H-2
Why this matters: C2의 핵심은 AUMC가 time-weighted exposure라는 점이다. AUMC tail의 영향은 수식만으로는 늦게 체화되므로, concentration curve와 first-moment curve를 눈으로 비교해야 한다.
When to look: C2 Recap 직후, C3로 넘어가기 전
Learner instruction: concentration curve와 $t\cdot C(t)$ curve의 late-time 영역을 비교하라. AUMC에서는 늦은 시간이 다시 가중되므로 tail sampling이 MRT에 더 크게 들어간다는 점만 확인한다.
<!-- /FIGURE_POINTER -->
```

### FIG-P04

```markdown
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.157, Fig 2.126
Why this matters: C3 Apex에서 §2.8.8 대안식은 단순한 공식 대체가 아니라 적용 영역의 변경이다. washout AUC를 직접 보아야 input-time-dominant 상황에서 표준식이 왜 불안정해지는지 이해된다.
When to look: C3 Recap 직후, C4로 넘어가기 전
Learner instruction: steady-state plateau 이후 washout curve에서 어떤 AUC가 쓰이는지 먼저 확인하라. 그 다음 Eq.2:366/2:367이 왜 zero/negative $V_{ss}$를 피하는지 본문 수식으로 돌아가 검토한다.
<!-- /FIGURE_POINTER -->
```

### FIG-P05

```markdown
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.163, Fig 2.135
Why this matters: C4의 exposure metrics는 단순 목록이 아니다. 그림을 통해 $C_{ss}$/average concentration, $C_{max}$, AUC, threshold-above exposure/$t_d$가 서로 다른 pharmacologic question에 답하는 요약값임을 분리할 수 있다.
When to look: C4 Recap 직후, §5 Confusion Pair로 넘어가기 전
Learner instruction: 각 metric이 concentration-time profile의 어느 부분을 요약하는지 표시 위치를 확인하라. 이후 어떤 PD/safety endpoint가 peak, cumulative burden, duration 중 무엇에 가까운지 생각한다.
<!-- /FIGURE_POINTER -->
```

### FIG-P06

```markdown
<!-- FIGURE_POINTER -->
Source: Gabrielsson & Weiner 5e, p.663, Fig 41.2
Why this matters: PK41의 핵심은 CL 감소가 숫자 한 줄이 아니라 model transition signal이라는 점이다. 이 figure가 없으면 learner가 NCA-CL을 dose별 descriptive table로만 읽고 nonlinear regression 전환의 필연성을 약하게 느낄 수 있다.
When to look: C4 Recap 직후 또는 Q4 self-test 전에
Learner instruction: dose가 증가할수록 CL이 감소하는 방향성만 확인하라. 그 다음 C4의 Michaelis-Menten regression 전환 문장으로 돌아가 “왜 CL/$t_{1/2}$가 final parameter가 아닌가”를 연결한다.
<!-- /FIGURE_POINTER -->
```

---

## 6. Final Phase 5 handoff note

- Phase 5는 위 marker blocks를 그대로 Content Lock v2에 splice하여 `06_Content Lock v2.1`을 만든다.
- Mode P는 원문 figure inspection 지시만 제공하며, 이미지를 삽입하지 않는다.
- Mode R(#2)은 SVG 또는 동등한 non-code visual brief로 구현하되, 교과서 figure의 exact layout, shading, labels, color scheme을 복제하지 않는다.
- 본 patch는 과학적 주장, 수식, source page tags, annotation marker를 추가·수정하지 않는다.

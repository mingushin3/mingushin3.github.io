# 05_Content Lock v2 — Pass Trace

## PASS 1 — Edit log table

| Location (§ + card) | Edit type (R1–R5) | Before (excerpt) | After (excerpt) |
|---|---|---|---|
| §1 Big Idea | R1, R4 | “macro-constant로 분해한 뒤, 이를 ... 다시 옮기는 기술” | “macro-constant로 분해한다. 그다음 이를 ... 다시 옮긴다.” |
| §1 Workflow anchor | R1, R2 | “$f_2$는 ... 예측하고, 좌표계는 ... 결정하며...” | forward inclusion에서 M1/M5 → M2 → M3 → M4 순으로 문장 분리 |
| §1 후속 지식 | R1 | “$\eta$-shrinkage 해석” | 첫 사용 지점에 짧은 gloss 추가 |
| §2 M1 Big Idea | R1, R5 | “semilog plot에서 하나의 직선이 아니라 두 직선의 합으로 보이면...” | semilog plot gloss 추가 및 “단순한 시각적 꺾임이 아니다”로 의미 명시 |
| §2 M1 Formal definition | R1 | “zero-time intercept” | 첫 사용 지점에 짧은 gloss 추가 |
| §2 M1 잔차법 | R1, R2 | terminal 외삽과 residual 계산이 한 문장에 압축 | 외삽 → subtraction → residual regression 순서로 문장 분리 |
| §2 M1 fractional area | R2 | “$f_2$가 크면..., $f_2$가 작으면...” | 두 조건을 별도 문장으로 분리하여 반대 방향을 명확화 |
| §2 M2 Big Idea | R2 | “그 정당성은 macro/micro 변환을 이해할 때 생긴다” | 같은 curve를 설명한다는 논리를 명시 |
| §2 M3 Big Idea | R1 | $V_1$, $V_{ss}$, $V_\beta$ 정의가 한 문장에 압축 | 세 volume 정의를 두 문장으로 분리 |
| §2 M4 Core lesson | R2 | “Takada model은..., ODE model은...” | WRSS와 condition number의 판단 축을 문장 분리 |
| §2 M5 Big Idea | R2, R3 | terminal half-life 유용성과 함정이 한 문장에 병렬 | “자주 유용하다. 그러나...” 구조로 완화 및 인과 명시 |
| §5 Confusion recap | R1 | “curve는 evidence이고, interpretation은...” | “curve는 evidence다.”로 분리 |
| §8 Final recap | R3 | “그 식을 보고 곧바로...” | “그 식을 보는 순간...”으로 실무적 중요성 전면화 |

## PASS 2 — Annotation candidate table

| Type | Location (§ + card) | Current text (excerpt) | Proposed annotation | Risk |
|---|---|---|---|---|
| A | §1 Big Idea | macro-constant | “곡선의 절편·기울기 상수” | Low |
| A | §1 후속 지식 | $\eta$-shrinkage | “ETA 정보 부족 지표” | Low |
| A | §2 M1 Big Idea | semilog plot | “농도축만 로그인 그래프” | Low |
| A | §2 M1 Formal definition | zero-time intercept | “t=0 외삽 절편” | Low |
| B | §2 M2 좌표계 table 직후 | 좌표계 3종 table | 같은 curve를 서로 다른 질문에 맞춰 다시 쓰는 방식이라는 bridge | Low |
| B | §2 M3 volume table 직후 | $V_1/V_{ss}/V_\beta$ table | “volume이 얼마인가?”는 불완전한 질문이라는 bridge | Low |
| A | §2 M4 Big Idea | condition number | “추정 불안정성의 수치 지표” | Low |
| B | §2 M5 plateau equation 직후 | plateau equation | 두 phase의 $C_{ss}$ 접근을 $f_1/f_2$로 가중합한다는 bridge | Low |
| C | §2 M2 | 좌표계 개념 | 지도/좌표 비유 | Medium — 독해 흐름 중단 가능 |
| C | §2 M3 | volume 3종 | 세 카메라 렌즈 비유 | High — apparent volume 오해 가능 |
| B | §8 Failure modes | Phantom V2 | sparse design의 정보 부족 bridge | Medium — 이미 충분히 명확 |

## PASS 2 — Final recommendation list

### Must annotate (Low risk)
- §1 Big Idea: macro-constant first-use gloss
- §1 후속 지식: $\eta$-shrinkage first-use gloss
- §2 M1: semilog plot, zero-time intercept first-use glosses
- §2 M2: 좌표계 bridge sentence
- §2 M3: “which volume?” bridge sentence
- §2 M4: condition number first-use gloss
- §2 M5: plateau equation bridge sentence

### Optional (Medium risk, high learning value)
- §8 Phantom V2 bridge: 제외. 이미 Failure mode table과 Q7에서 충분히 설명됨.
- §2 M2 좌표계 analogy: 제외. PhD reader에게 과도한 비유로 보일 수 있음.

### Do not annotate
- $AUC$, $AUMC$, $MRT$, $CL$, $V_1/V_{ss}/V_\beta$ 자체: 본 세션 전제 수준 또는 이미 본문에서 충분히 정의됨.
- PK7/PK8 수치와 R&T 사례: 새 annotation 없이 source tag 보존이 더 중요함.
- NONMEM implementation note: supplied PDF 밖 실무 확장이므로 추가 설명을 붙이지 않음.

## Constraint check

- Content Lock v1 length: 40,640 characters
- Content Lock v2 length: 41,230 characters
- Increase: 1.45%
- Limit: ≤8%
- Result: PASS

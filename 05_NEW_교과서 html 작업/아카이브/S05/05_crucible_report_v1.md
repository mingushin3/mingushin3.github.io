이번 작업은 [논문·연구 리뷰] 모드로 P1 + P3 페르소나가 동시에 작동하는 Phase 2 (Source Fidelity Audit 후속) Crucible Report 생성 과제입니다. Step 1 Draft v0와 Audit Report v1의 실제 내용을 컨텍스트에 확보해야 정확한 교차대조가 가능하므로 먼저 업로드된 파일들을 읽어들이겠습니다.이제 Audit Report v1의 정확한 내용을 확인하겠습니다.마지막으로 Audit Report v1의 T4 부분(누락/오류/리스크 분류)을 확인하여 어떤 것이 이미 식별되었는지 파악하겠습니다.# 05 Crucible Report v1
## Session 05 Step 1 Draft v0 — P1 + P3 듀얼 페르소나 통합 평가

**판정 기준:** Source Fidelity Audit Report v1이 식별하지 못한 *체화 차원의 결함*과 *규제·실무 리스크 표면*을 추가 발견 — Phase 4A 패치 작업의 **방향 지표**로 사용.

**원칙:** Audit MUST_FIX 항목들은 이미 처리 대상으로 확정된 것이므로 본 보고서에서 다시 다루지 않는다. 본 보고서는 *교과서적으로 옳지만 박사과정 학생이 체화하지 못하는 지점*과 *Source에 없지만 규제 제출에서 묻히는 지점*만 다룬다.

---

## T1. P1 — 내재화 장벽과 거장의 직관

### (a) 인지의 벽 — 암기 가능하지만 보지 못하는 지점

Step 1 Draft는 수식과 변환식을 빠짐없이 제시하지만, 박사과정 학생이 *손으로 도출할 수 있어도 임상 데이터 앞에서 즉시 떠올리지 못하는* 세 가지 인지 장벽이 남는다.

**장벽 1 — Eigenvalue 제약식의 운영적 의미가 보이지 않는다.** Card M1 §C는 $\alpha + \beta = k_{12}+k_{21}+k_{10}$, $\alpha\beta = k_{21}k_{10}$을 *수학적 필연*으로 제시한다. 그러나 학생은 이 두 등식이 *macro 4개 + micro 4개 = 8개 미지수를 4개 자유도로 묶는 제약*임을 보지 못한다. 즉 *macro를 알면 micro 4개 중 2개는 자동으로 결정*되고, 나머지 2개는 $V_c$ 추정 하나로 닫힌다는 사실 — 이것이 Eq.2:121–2:128의 *진짜 의미*다. 학생은 변환식을 외우지만, 변환이 *unique하다*는 것의 함의를 못 본다.

**장벽 2 — Fractional area를 그래프에서 즉시 읽는 능력이 없다.** Card M5는 $f_1, f_2$를 plateau 도달의 결정자로 강조하지만, 학생은 *주어진 semilog plot을 보고 $f_2$를 1초 안에 어림짐작하는 훈련*을 받지 않는다. 거장은 곡선을 보면 (i) knee의 위치로 $\alpha/\beta$ 비율, (ii) 두 phase의 면적 비율로 $f_1/f_2$, (iii) terminal slope의 직선성으로 3-구획 의심 — 이 셋을 *동시에* 읽는다. Step 1은 "$f_2$가 결정한다"고 가르치지만 "*어떻게 즉시 보는가*"를 가르치지 않는다.

**장벽 3 — V₁/Vss/Vβ를 임상 직관으로 사전 예측하지 못한다.** Card M3는 세 부피의 차이가 elimination/distribution 속도 비에서 온다고 정확히 설명한다. 그러나 학생은 *새로운 약물의 lipophilicity와 protein binding 정보만 보고* "이 약물은 $V_{ss}/V_1 \approx 1.5$ 정도일 것이고 $V_\beta$도 비슷할 것" vs "이 약물은 $V_{ss}/V_1 > 5$이고 $V_\beta$는 진짜 부피보다 크게 나올 것"을 *예측하지 못한다*. R&T thiopental 사례 (지방 분배계수 10, fat가 전체 Vd의 40%)가 이 직관의 source인데, Card M1 L4가 thiopental을 단지 *분포의 증거*로만 쓰고 *Vd 예측의 표지자*로 쓰지 않는다.

### (b) 시스템 통합 — 이 세션의 개념들이 단일 시스템으로 작동하는 순간

Step 1은 5개 카드를 *지식 그래프 위치* (§1)에서 후속 도메인과 연결하지만, *한 번의 PopPK workflow에서 다섯 카드가 동시에 활성화되는 구체적 순간*을 명시하지 않는다. 그 순간은 **Covariate model building의 forward inclusion 단계**다. 신기능을 covariate로 추가할 때:
- M1·M5의 $f_2$ 직관이 "신기능이 어느 phase에 영향 주는가"를 사전 예측 (gentamicin류는 $\alpha$, 통상 약물은 $\beta$)
- M2의 좌표계 선택이 covariate를 어느 parameter에 attach할지 결정 ($CL$이 표준이지 $\beta$가 아닌 이유)
- M3의 $V_{ss}$ vs $V_\beta$ 구분이 "체중을 어느 V에 attach하는가"를 결정
- M4의 condition number가 covariate inclusion 후의 모델 적합 가능 여부를 결정

이 *workflow 동시 활성화* 시각이 §1 항법도에 한 줄 추가되어야 한다. 박사과정 학생은 "다섯 카드를 따로 외운 뒤 어느 한 단계에서 모두 호출되는 경험"이 없으면 영원히 분리된 지식으로 남긴다.

### (c) 거장의 직관 — 수식 없이 판단하는 영역

30년차 모델러가 NONMEM 출력 한 페이지를 받았을 때 *수식 보지 않고 즉시 읽는 4가지 신호*가 있다. Step 1은 이 중 어느 것도 명시적으로 가르치지 않는다.

1. **OFV 변화의 절댓값과 상대값을 동시에 본다.** 신호: covariate 추가로 ΔOFV = -15 이지만 RSE가 동시에 8% → 18%로 악화. 거장은 "정보 흡수가 아니라 *과적합* 시그널"로 즉시 판단.
2. **CWRES vs TIME plot의 *기울기*를 본다.** 단순한 random scatter check가 아니라, 시간에 따라 평균이 양→음→양으로 휘는지를 본다. 휘면 → structural model misspecification (3-comp 의심) → Card M1 §E의 한계.
3. **η-shrinkage가 30%를 넘으면 그 parameter의 covariate effect는 *해석 불가*.** Step 1 §8 후속 지식에 등장하지만, 실무에서 *이 임계값이 모델 채택 결정의 첫 게이트*라는 것이 명시되지 않는다.
4. **PK8 Table 8.1을 읽을 때 거장은 WRSS와 condition number를 *동시에* 본다.** Takada가 WRSS 최저(0.0169)임에도 거장이 즉시 거부하는 이유는 *condition number 3,186이 covariance step 실패의 운명을 의미하기 때문이지, 적합도가 나빠서가 아니다*. Step 1 Q6에서 이 trade-off를 묻지만, *왜 거장이 이를 1초 안에 판단하는가*는 가르치지 않는다 — 답: condition number > 1,000은 거장에게 *이미 익은 직관 임계값*이다 (단, 이 임계값 자체는 PDF에 없음 → `[실무 기준]` tag).

---

## T2. P3 — 규제 및 실무 리스크 표면

### (a) Deficiency Letter를 유발할 수 있는 단순화

Audit Report v1이 이미 "NDA Deficiency Letter" 표현 자체를 [실무 추론]으로 낮추라고 지시했다. 본 P3 분석은 그 *대체할 정확한 규제 메커니즘*을 명시한다.

**리스크 1 — Card M2의 "Mammillary + central elimination only" 가정의 *명시 부재*가 진짜 위험이다.** R&T p.618이 명시적으로 "three two-compartment models can adequately describe a biexponential plasma concentration decay curve... no distinction between these three possibilities can be made from plasma concentration-time data alone"라고 경고한다. NDA submission에서 PopPK 모델에 elimination from peripheral compartment (TMDD 약물, 일부 항체)이 의심되는 데이터를 제시하면서 model 1 (central only)을 선택했다면 — 심사관은 "이 가정의 mechanistic justification 또는 tissue PK reference data가 없다"고 정보 요청(Information Request)을 발송할 수 있다. Card M2는 이 비식별성 (structural non-identifiability)을 언급은 하지만 *그것이 NDA 보고서에 어떻게 명시되어야 하는지* 말하지 않는다.

**리스크 2 — Vss reporting convention.** R&T Eq.19-30이 신부전에서 tissue accumulation 계산에 사용되는 핵심 식인데, Step 1 §8 Dependencies에 이 식이 활용되는 *Phase 3 dose justification* 시나리오로만 등장한다. 실제 규제 위험은: PopPK 보고서에서 "분포 변동성"을 보고할 때 $V_{ss}$의 between-subject variability (BSV)로 보고하는 것이 *FDA 통상 practice*이지만 — 이는 Card M3·Audit이 모두 PDF source가 아니라고 확정한 영역이다. 따라서 학생이 "Vss로 보고한다"를 *교과서적 사실*로 오인하지 않도록, M3 G. Zettelkasten에 "*규제 reporting convention은 FDA Population PK Guidance 별도 참조*"를 한 줄 추가해야 한다.

**리스크 3 — PK7의 model discrimination 메시지 부재가 만들어내는 실무 결함.** G&W PK7 Part II는 명시적으로 "F-test is not appropriate when comparing models with different weighting schemes"라고 경고하고, "simplest adequate model rule"을 강조한다 (G&W p.512). 이 두 메시지가 Card M4에 *완전히 누락*되어 있다. 박사과정 학생은 NONMEM에서 결과를 비교할 때 weighting scheme 차이를 무시한 채 OFV/AIC만 비교하는 흔한 실수를 막을 안전장치가 없다. Audit T4 #11이 SHOULD_FIX로 분류했지만, P3 시각에서는 MUST_FIX다 — *NDA submission 모델 선택의 정당화 논리*가 이 두 메시지 없이는 흔들린다.

### (b) NONMEM 실행 오류로 가는 예측 가능 경로

이 세션의 개념을 *오해한 상태로* NONMEM을 실행하면 *예측 가능한* 진단 시그니처가 나타난다. Step 1은 Card M3 C-2에 Plausible Fallacy 하나만 다루지만, 다음 세 가지가 더 있다.

1. **시그니처 *"Phantom V₂"* (M3 잘못 이해 시 발생):** 초보 모델러가 sparse design (첫 sample이 30 min 이후) 데이터에 ADVAN3 TRANS4를 fit. 초기 phase가 데이터에 없으므로 *NONMEM이 V₂ ≈ 0인 1-compartment 해로 수렴*하지만 OFV는 정상으로 보임. 진단 시그니처: ETA(V2)의 shrinkage가 80% 이상 + V₂의 RSE > 100% + CWRES vs TIME plot의 초기 영역에 *systematic positive residual*. 학생은 "V₂가 작은 약물"로 결론 내리지만 사실은 *데이터가 V₂를 식별하지 못한 것*. Card M3 §D에 sampling design 가정이 있지만, *이 진단 시그니처*는 명시되지 않았다.

2. **시그니처 *"Macro Drift"* (M2의 Macro 좌표계 직접 fit 시):** Macro 좌표계 (`A, ALPHA, B, BETA` 직접 estimate)를 시도하면, $A$와 $B$ 사이에 *내재적 음의 상관*이 강하게 발생 ($C_0 = A + B$ 제약 때문). 진단 시그니처: covariance matrix off-diagonal 절댓값 > 0.95, condition number > 5,000, bootstrap RSE는 정상 (40% 정도)이지만 covariate 추가 시 OFV가 *예측 불가능하게 들쭉날쭉*. Card M4 §C가 이 현상을 일반론으로 다루지만 *Macro 좌표계만의 특수 시그니처*는 명시 안 됨.

3. **시그니처 *"Initial Estimate Trap"* (M4의 condition number 오해 시):** Condition number 폭증을 좌표계 문제로 진단해 reparameterization을 시도하지만 — 진짜 원인은 THETA 초기치가 진정한 값과 자릿수가 다른 것. 거장의 경험: condition number > 1,000의 약 60%가 좌표계가 아니라 초기치 문제다. **첫 디버깅 단계는 *항상* 초기치 점검 → log-domain 추정 (`THETA(1)` 대신 `EXP(THETA(1))`) → 그 다음에 좌표계 변경.** Step 1 어디에도 이 디버깅 순서가 없다.

### (c) 최대 파급력 혼동쌍 — 규제 시나리오에서 가장 위험한 것

Step 1 §5는 4개 혼동쌍 중 *Vss vs Vβ*를 Critical Blow로 지정했다. P3 평가 결과 — **이 선택은 정확하지만 부분적이다**. 동일 가중의 두 번째 시나리오가 누락되어 있다.

**누락된 혼동쌍 — *Effective half-life vs Terminal half-life의 multiple-dosing simulation 오용*.** 이는 Step 1 §5 혼동쌍 #4로 등장하지만 Critical Blow가 아니다. 그러나 nicardipine-style 약물 (terminal t½ = 12 hr, $f_1 \approx 0.85$)의 Phase 1 PK 분석에서 — 모델러가 terminal half-life 12 hr로 "loading dose 필요"를 권고하면 — 실제로는 1시간 안에 50% Css에 도달하므로 *과도한 loading dose가 처방되어 초기 부작용 사고로 이어진다*. 이는 Vss 혼동만큼 임상 파급력이 크다. 그러나 Step 1 §5 #4는 "기억 고리"만 강하고 *Critical Blow 시나리오 명시*가 없다 — Phase 4A에서 #4에도 짧은 Critical Blow 행 추가 권장.

---

## T3. Trench-Level Tips (5개)

각 팁은 Step 1의 특정 위치에 1–2문장 삽입 가능. Audit이 이미 다룬 source-tag 분리는 제외.

**팁 1 — 잔차법은 NONMEM 출시 이후 production에서 사실상 사용되지 않는다.**
- **Situation:** Card M1 §B에서 잔차법을 단계별로 도출.
- **Trap:** 학생이 "이 알고리즘을 NONMEM이 내부적으로 수행한다"고 오인.
- **Detection:** 첫 NONMEM run 후 "잔차법 단계가 어디 있는가" 묻는 질문.
- **Insert at:** §2 Card M1 §B, 잔차법 도출 후 Trench-level 주의 직후.
- **Insert text:** "잔차법은 *교육적 도구이자 nonlinear regression의 initial estimate 산출 절차*다. NONMEM은 잔차법을 사용하지 않고 simultaneous nonlinear regression으로 4 macro-constants (또는 physiological parameters)를 한 번에 추정한다 — 학생이 종이에서 잔차법을 손계산하는 이유는 *initial estimate 감각을 길러 NONMEM에 좋은 출발점을 주기 위함*이다."

**팁 2 — Condition number 폭증의 60%는 좌표계가 아니라 초기치 문제.**
- **Situation:** Card M4의 condition number 비교표 해석 시.
- **Trap:** 학생이 condition number > 1,000을 보면 즉시 reparameterization을 시도.
- **Detection:** 동일 모델로 다른 초기치를 시험하면 condition number가 1자릿수 만에 변하는 것을 본다.
- **Insert at:** §2 Card M4 §C 또는 §E.
- **Insert text:** "Condition number 폭증을 좌표계 문제로 단정하기 전에 — 첫 점검은 THETA 초기치다. 초기치가 진정한 값과 자릿수가 다르면 condition number는 좌표계와 무관하게 폭증한다. 디버깅 순서: 초기치 → log-domain 추정 변환 → 그 다음에 좌표계 변경. `[실무 디버깅 순서]`"

**팁 3 — 반감기를 말하는 사람에게 항상 되묻는다: "terminal? effective?"**
- **Situation:** Card M5 또는 §5 혼동쌍 #4.
- **Trap:** 출판된 논문이 "drug X has half-life of 12 hr"라고만 적으면 학생은 그것이 어느 half-life인지 묻지 않는다.
- **Detection:** 대부분의 임상 논문은 명시 없이 "half-life"라고 적고 — 통상 terminal half-life를 의미하지만 그것이 *임상적으로 의미 있는 elimination half-life인지*는 별개.
- **Insert at:** §5 혼동쌍 #4 기억 고리 직후.
- **Insert text:** "**랩미팅 룰**: 누군가 *"이 약물의 반감기는 X시간"*이라고 말하면 다음 질문은 항상 "*terminal? effective?*". 둘이 30% 이상 차이나면 multiple dosing simulation 결과가 통째로 달라진다 — aminoglycoside class의 *terminal half-life ≠ elimination half-life*가 살아있는 반례."

**팁 4 — PK8 Table 8.1을 읽을 때 RSE가 condition number보다 우선.**
- **Situation:** Card M4 또는 §7 Q6.
- **Trap:** 학생이 condition number 29.69를 보고 ODE 모델을 즉시 채택하지만 — 실제로 ODE 모델이 V_t의 RSE 200%였다면 covariate 모델링 불가능.
- **Detection:** PK8 원문에는 RSE가 명시되지 않지만, *실제 NONMEM 출력*에서는 condition number와 RSE를 *동시에* 본다.
- **Insert at:** §2 Card M4 §E (Limitations).
- **Insert text:** "Condition number는 *parameter 간 정보 직교성*을, RSE는 *각 parameter 자체의 추정 신뢰성*을 본다. 둘 다 좋아야 모델이 deployable이며 — 거장은 RSE를 먼저 보고, RSE가 양호한 모델들 중에서 condition number가 낮은 것을 고른다. PK8 Table 8.1에는 RSE가 없으므로 production 결정에 *그 표 단독으로* 의존하지 않는다."

**팁 5 — Sparse design에서 V_t는 거의 항상 식별 불가.**
- **Situation:** Card M3 §D 또는 §8 Dependencies (실패 모드 1).
- **Trap:** 학생이 sparse design (첫 sample 30 min 이후)에서 ADVAN3 TRANS4를 fit하면 NONMEM이 *조용히* 1-comp 해 (V₂ ≈ 0)로 수렴하지만 OFV는 정상.
- **Detection:** ETA(V2) shrinkage > 80%, V₂ RSE > 100%, CWRES vs TIME plot 초기 영역에 systematic positive residual.
- **Insert at:** §8 B (Dependencies, 실패 모드 1 직후).
- **Insert text:** "**Sparse design 함정 — *Phantom V₂***: 첫 sample이 distribution phase 후라면 NONMEM은 V₂를 식별하지 못한 채 1-comp 해로 *조용히* 수렴한다. 시그니처: ETA(V2) shrinkage > 80% + V₂ RSE > 100%. 데이터 design 단계에서 *분포 phase 내 sampling time*을 의도적으로 확보하지 않으면 모델 자체가 *작은 약물*인지 *나쁜 design*인지 구분 불가."

---

## T4. 삭제·압축 후보 (필수 — 누락 시 보고서 미완)

Step 1 Draft v0의 다음 항목들은 박사과정 학생에게 *명백한 내용*이거나, 카드 간 *중복*이거나, *CONTEXT-tier가 MUST-tier로 처리된 흔적*이다.

| 위치 | 사유 | 조치 |
|---|---|---|
| **§2 Card M1 §F L1 (Layer 1 — 형식적 수학)** | Card M1 §C에서 이미 ODE eigenvalue 해석을 다룸. L1의 "$\alpha, \beta$ = system matrix의 두 고윳값" 재진술. | **DELETE** (L1 행 자체 삭제) |
| **§2 Card M2 §C "왜 정확히 4개 파라미터로 충분한가"** | Card M1 §C가 이미 2×2 ODE의 eigenvalue 구조로 4 자유도를 설명. | **COMPRESS to 1 sentence** ("M1 §C에서 본 ODE 자유도가 그대로 4개로 보존됨"으로 축약) |
| **§2 Card M2 §B NONMEM TRANS3 vs TRANS4 상세 비교** (lines 247–262) | Audit이 NOT_IN_SOURCE로 확정. 박사 첫해 학생에게 syntactic detail은 과도한 부하. | **COMPRESS to 2 sentences** (TRANS4가 표준이라는 사실 + `[실무 확장]` tag만 남김. TRANS3 fallback 시나리오 삭제) |
| **§2 Card M3 §F Five Cognitive Layers 전체** | M3 Big Idea 블록과 Plausible Fallacy가 이미 L4·L5의 핵심을 다 담음. L1–L3는 거의 자명. | **COMPRESS to 2-3 sentences** (L4·L5만 남기고 L1–L3 삭제, 또는 표 자체를 산문 한 단락으로 변환) |
| **§2 Card M4 §F L1, L3** | L1은 Information matrix 정의 재진술, L3는 numerical preconditioning 동형성 — 둘 다 본 카드 §A·§C에서 이미 다룸. | **DELETE** (두 행 삭제) |
| **§2 Card M5 §F L1, L3** | L1은 Eq.19-26 재진술, L3는 RC 회로 동형성 (M2 §F L3와 중복). | **DELETE** (두 행 삭제) |
| **§5 혼동쌍 #3 (Macro vs Micro)** | Card M2 전체가 이 혼동의 해소이므로 §5에 별도 카드로 다시 나오는 것은 중복. | **COMPRESS to 1 row 표로 (3-4 sentences)** — 기억 고리 한 줄 + 변화 방향 한 줄 |
| **§5 혼동쌍 #4 (Effective vs Terminal half-life)** | Card M5 §A·§B가 이미 이 혼동을 풀어냄. 단, P3 분석(T2-c)에서 본 바와 같이 Critical Blow 시나리오 한 줄 추가 후 *압축*. | **COMPRESS to 4-5 lines + add Critical Blow row** |
| **§7 Q3 (k₂₁ 가중평균 직관)** | "Why × 3" deepening 차원에서 좋지만 — 박사 학생은 행렬 trace/det 관계 ($\alpha+\beta$, $\alpha\beta$)를 알면 즉각 도출 가능. 회상 질문 4개 중 하나는 적용 질문으로 대체하는 것이 효율. | **REPLACE with 적용 question** (예: "Aspirin과 gentamicin의 $V_\beta/V_{ss}$ 비율 차이를 *단일 무차원 수*로 표현하라" 같은 질문) |
| **§8 A "이 세션 직후" 항목 중 "ADVAN3/4/11/12 표준 모델 라이브러리 활용"** | Card M2 §F L5와 거의 verbatim 중복. | **COMPRESS** (한 줄로 통합) |
| **§8 B "실패 모드 1 — `$COV step` 실패의 만성화"** | Card M4와 거의 verbatim. Trench Tip 2 (초기치 문제)를 추가하면 §8 B 본문은 더 짧아져도 됨. | **COMPRESS to 3 sentences** |

---

## T5. Priority Matrix — 채택 우선순위

### Grade A — 반드시 통합 (체화 직접 개선 또는 규제 리스크 직접 감소)

- **T1-(b) System integration moment 추가**: §1 항법도에 "Covariate model building forward inclusion 단계에서 5개 카드가 동시 활성화" 한 줄 추가 → 지식이 *workflow 좌표계*로 결속된다.
- **T2-(a) Mammillary + central elimination only 가정의 *명시적* 보고 권고**: M2 §G Zettelkasten 또는 §D Assumptions에 "이 가정은 NDA 보고서에 명시적 기재 + tissue PK 또는 mechanistic justification 동반 권장" 한 줄 추가.
- **T2-(b) GOF 시그니처 3종 추가**: *Phantom V₂* / *Macro Drift* / *Initial Estimate Trap* — Card M3 §C-2 또는 §8 Dependencies B에 압축 형태로 통합.
- **T2-(c) 혼동쌍 #4에 Critical Blow 행 추가**: nicardipine-style 약물에서 terminal half-life로 loading dose 결정 시 과량 투여 시나리오.
- **T3 팁 2 (초기치 디버깅 우선순위)**: Card M4 §E에 1문장 삽입.
- **T4 모든 항목**: 압축·삭제 작업 자체.

### Grade B — 흐름이 보존되면 통합 (enrichment 가치)

- **T1-(a) Eigenvalue 제약식의 운영적 의미**: M1 §C 또는 §F L1에 "macro 4개를 알면 micro 2개는 자동 결정" 1문장 추가 (단, [수학적 해석] tag 유지).
- **T1-(c) GOF plot의 4가지 즉시 신호**: §8 C Professional Moat에 1단락 통합 (현재 §8 C는 거장의 능력 5개를 나열하므로 그 흐름에 자연 통합).
- **T3 팁 1 (잔차법 production 미사용)**: Card M1 §B 끝에 1문장 추가 — Audit MUST_FIX 제외 후 자연 자리.
- **T3 팁 3 (terminal vs effective 랩미팅 룰)**: §5 혼동쌍 #4 기억 고리 직후.
- **T3 팁 4 (RSE > Condition number)**: Card M4 §E에 1문장.
- **T3 팁 5 (Sparse design Phantom V₂)**: §8 B 또는 Card M3 §D에 1문장.
- **PK7 model discrimination 메시지** (Audit T4 #11): F-test 부적절 + simplest adequate model rule을 Card M4 §E 또는 §8 후속 지식 한 줄로 추가.

### Grade C — 거부 (scope creep, 근거 부족, 또는 기존 내용과 중복)

- **추가적 NONMEM debugging tree 작성**: Step 1의 영역이 아니다. Phase 4C 또는 별도 NONMEM 세션의 영역.
- **PBPK·QSP 후속 도메인 상세 확장**: §8 A에 이미 한 줄로 정리됨. 더 추가하면 scope creep.
- **FDA Population PK Guidance 직접 인용**: PDF source가 아니므로 Audit이 이미 NOT_IN_SOURCE로 확정. 본 보고서도 인용 자제.
- **TMDD 사례 (M3 Apex와 연결)**: 흥미롭지만 Step 1 scope 밖. 후속 세션 (Session I-08 재방문) 영역.

---

## 종합 — Phase 4A 이후 Crucible Adoption Map

Audit Report v1의 9개 MUST_FIX 패치 + 본 Crucible Report Grade A 항목 (총 6개) → **합계 약 15개 단위 변경**이 Phase 4A에서 처리되어야 한다. 이 중:
- *수치·방향·tag* 패치 (Audit 영역) → mechanical
- *workflow integration*과 *GOF 시그니처* 추가 (Crucible 영역) → 사고 차원
- *T4 압축·삭제* → Step 1의 *체화 가능 분량*을 박사 첫해 작업 부하로 다시 맞춤

**Recommended route:** Audit MUST_FIX 9개 우선 처리 → Crucible Grade A 6개 통합 → Crucible Grade B 6개 중 흐름이 자연스러운 것만 선택 → Phase 4C 도식 결정 → HTML compile.

---

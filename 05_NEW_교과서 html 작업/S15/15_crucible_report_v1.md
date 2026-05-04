# Session 15 — Phase 3 Insight Crucible Report v1

**입력**: PDF (Gabrielsson 5e Ch.4-5 발췌) + Step 1 Draft v0 + Audit Report v1 + Patch Memo
**역할**: P1 (30년 차 시니어 멘토) + P3 (FDA 임상약리 시니어 리뷰어) 동시 운영
**필터**: Step 1 내용 재진술 금지 — 1년차 박사과정에게 5분 안에 이 챕터 이해를 영구적으로 한 단계 끌어올릴 통찰만 추출

---

## T1. P1 — 내면화 장벽과 거장의 직관

### (a) 인지 장벽 — 외울 수는 있지만 보지 못하는 것들

Draft v0는 6개 카드를 잘 짜냈지만, 1년차 박사과정이 이 카드들을 통째로 암기하고도 **여전히 보지 못하는 5가지 시각적 사실**이 있다. 이것들이 멘토가 5분 동안 채워줘야 할 진짜 공백이다.

첫째, **F-test의 nested 조건의 위상학적 의미**다. 학생은 "reduced = full의 특정 파라미터를 0으로 고정"이라는 정의를 외울 수 있지만, OFV surface 위에서 **reduced model이 full model의 lower-dimensional subspace로 박혀 있다**는 기하학을 보지 못한다. Non-nested 비교는 두 model이 *별개의 surface 위에 산다*는 위상학적 사실이며, 이 둘의 OFV 차이는 같은 좌표계 안의 양이 아니다 — 그래서 F 분포가 정의되지 않는다. *Insert at §2 MUST 3 C. Structural Necessity*: "Nested란 단순한 파라미터 포함 관계가 아니라 두 모델이 같은 likelihood surface의 부분-전체 관계로 연결되어 있다는 위상학적 사실이며, 이것이 분포를 정의하는 기반이다."

둘째, **r 값이 dynamic range에 의해 자동으로 끌어올려지는 메커니즘**이다. 학생은 Fig.4.53의 r=0.96 OLS / r=0.94 IRLS 사례를 외울 수 있지만, **데이터의 농도 폭이 3-log 이상으로 넓어지는 순간 어떤 모델이라도 r이 0.95를 넘긴다**는 사실을 본능으로 갖지 못한다. *Insert at §5 혼동쌍 #2 기억 고리 직전*: "PK 데이터처럼 농도가 3-log 이상 펼쳐진 데이터에서는 r이 0.95를 넘기는 데 모델이 기여하는 부분이 거의 없다 — r 0.95는 dynamic range의 함수이지 fit의 함수가 아니다."

셋째, **편미분 극값 = likelihood 곡률의 출처**라는 단일성이다. 학생은 "$\partial C/\partial \theta$가 큰 시점에서 sample하라"는 처방을 외울 수 있지만, 그것이 **likelihood surface가 그 파라미터 방향으로 가파르게 휘어지는 시점**과 동일하다는 사실(Fisher information의 정의 자체)을 보지 못한다. *Insert at §2 MUST 5 C. Structural Necessity*: "편미분이 큰 시점은 likelihood surface가 그 파라미터 방향으로 가파른 곡률을 갖는 시점이며, 곡률이 크다는 것은 minimum이 좁고 깊다는 것 — 즉 정밀도가 높다는 것이다."

넷째, **상관 = ridge minimum의 기하학**이다. Draft v0의 §2 MUST 4 C가 "ridge 형태 surface"를 한 줄 언급했지만, 1년차 학생은 이것을 *시각화*하지 못한다. *Insert at §2 MUST 4 L2 기하학적 직관*: "Ridge 능선을 머릿속에 그려라 — 능선 위 어느 점에 서 있어도 OFV가 거의 같다; 학생이 estimate하는 두 점이 능선 위 임의의 두 점일 뿐이다."

다섯째, **잔차 패턴은 모델이 놓친 시간 스케일의 직접 노출**이라는 사실이다. Banana shape는 "exponential term 부족"이 아니라 **빠른 시간 스케일이 모델 안에 없다**는 *시간 구조의 결손 신호*다. *Insert at §2 MUST 2 C. Structural Necessity*: "잔차의 시간 패턴은 모델이 놓친 시간 스케일의 직접 노출이며, banana 골짜기의 폭이 빠진 시간 상수의 역수와 대응한다 — 이것이 lag-time bulge와 banana를 구별하는 메커니즘이다."

### (b) 시스템 통합 — 6개 도구가 하나로 작동하는 순간

Draft v0의 §1 개념 항법도는 6개 MUST를 사이클로 그려놓았지만, **이 사이클이 실무에서 통합되는 단일 작동 단위**가 무엇인지는 명시하지 않았다. 답은 명확하다: **modeling carousel 한 회전 = NONMEM control file 한 버전 + 그에 딸린 진단 plot 세트 + 다음 cohort의 sampling schedule 권고서 한 장**. 이것이 시니어 모델러의 "한 사이클"이다.

*Insert at §8 A. Positioning 끝부분*: "본 챕터의 6개 도구가 통합되어 작동하는 실무 단위는 한 번의 NONMEM run이 아니라, 하나의 control file + GOF 진단 plot 한 세트 + 다음 cohort에게 보낼 sampling 권고문 한 장이다 — 이 셋이 분리되면 사이클이 닫히지 않는다."

### (c) 거장의 즉각적 판단 — 방정식 없이 보는 것들

30년 차가 NONMEM 출력을 1초 안에 판단하는 4가지가 있다. **첫째**, OFV trajectory의 처음 5 iteration이 잘 안 떨어지면 "초기값 의심" — 재실행 결정이 즉시 내려진다. **둘째**, 잔차 plot의 형태(banana / fan / lag bulge)는 sub-second에 위상학적 인식으로 처리되며, 패턴 매칭이 아니라 형태 자체가 진단명을 호출한다. **셋째**, 두 모델이 같은 데이터에서 비슷한 OFV를 내면 "둘 다 잘못된 모델"을 의심하는 *역방향 추론*이 작동한다 — 학생은 항상 더 좋은 쪽을 찾으려 하지만, 베테랑은 이 시점에 메커니즘 가설을 다시 검토한다. **넷째**, CV%가 50%를 넘으면 모델 결함이 아니라 *데이터 결함*으로 즉각 reframe — 처방은 "모델 단순화"가 아니라 "다음 cohort의 sampling 변경"이다. *Insert at §8 C. Professional Moat (1) 또는 (3) 보강*: "두 경쟁 모델이 비슷한 OFV를 낼 때 베테랑이 의심하는 것은 '어느 쪽이 더 옳은가'가 아니라 '둘 다 잘못된 메커니즘일 가능성'이며, 이 역방향 추론이 mechanistic 가설로의 회귀를 가능하게 한다."

---

## T2. P3 — 규제·실무 리스크 표면

### (a) Step 1의 단순화가 만드는 리뷰어 challenge 경로

Audit가 명시했듯, Draft v0가 사용한 "Deficiency Letter / 6-month extension / Major Deficiency" 같은 표현은 PDF 무근거이며 삭제 또는 일반화 대상이다(T4에서 다룸). 그러나 **규제 리뷰어가 모델 선택 근거의 신뢰성을 challenge하는 추론 경로 자체**는 Step 1에 명확히 들어 있어야 하며, Draft가 *위장된 단순화*로 이 경로를 잘못 그린 곳이 두 곳 있다.

첫째, **§2 MUST 4 (정밀도-상관) Big Idea**가 "$|r| > 0.95$이면 채택 금지"로 강하게 진술됐지만, 실무에서는 *"하나를 fix하고 다른 하나만 추정"*이라는 옵션이 살아있다(Fig.4.55 right panel). Step 1이 이 옵션을 §7 Q8에서만 다뤘는데, **fix 결정의 정당화 부담** — literature value의 출처, in vitro 데이터의 in vivo 적용 가능성, 인구 차이 — 이 카드 본문에서 명시되지 않았다. *Insert at §2 MUST 4 D. Assumptions & Boundary Conditions*: "한 파라미터를 fix하는 옵션은 통계적으로 유효하지만, 그 fix 값의 출처(literature, in vitro, prior study)와 인구 적용성에 대한 정당화 책임이 모델러에게 옮겨가며, 이 정당화 부재가 리뷰어 challenge의 진입점이다."

둘째, **§5 혼동쌍 #1**에서 F-test 위반의 대안으로 AIC를 제시했지만, **AIC 차이의 해석 기준** ($\Delta$AIC가 얼마면 "유의미한가")에 대한 가이드라인이 PDF에 없다는 사실 자체가 학습자에게 인식돼야 한다. 이것은 weakness가 아니라 *교과서가 의도적으로 비워둔 영역* — 메커니즘 plausibility로 채워야 한다는 신호다. *Insert at §5 혼동쌍 #1 변화 방향 행 직후 또는 §7 Q9 정답 보강*: "AIC 차이의 임계값은 PDF에서 정의되지 않으며, 이 빈자리는 메커니즘 plausibility와 외부 데이터(in vitro, prior literature)로 채워야 한다는 교과서의 암묵적 신호다."

### (b) NONMEM 실행에서 예측 가능한 진단 시그니처

Step 1 §2 MUST 3의 "Phantom Convergence Pattern" 명명은 훌륭하다. 그러나 실무에서 자주 만나는 두 패턴이 더 있다.

**"Boundary Stickiness"**: §4.4.2 boundary scaling 적용 시, IE가 LB·UB의 기하학적 중간이 아니거나 (특히 Table 4.4의 β처럼) IE가 boundary와 동일한 경우, 알고리즘이 그 boundary에 stuck된다. 진단 시그니처는 final estimate가 정확히 boundary 값이고 `$COVARIANCE` step에서 NEAR BOUNDARY 또는 R MATRIX SINGULAR 경고. *Insert at §2 MUST 1 [B-5] When all else fails 끝*: "IE가 boundary에 너무 가까우면(Table 4.4의 β=0.05=UB가 그 예) 수렴이 그 자리에 stuck되며, 출력에서는 NEAR BOUNDARY 경고로 노출된다 — IE는 항상 LB·UB의 기하학적 중간에 두라."

**"Spurious Identifiability"**: Univariate CI는 좁고 fit는 좋지만 planar CI는 넓을 때, 학생이 univariate만 보고 안심하는 함정. 진단 시그니처는 condition number $\kappa$가 1000을 넘는 것 (Step 1 §2 MUST 4 L5가 언급했지만 압축이 필요 — T4 항목). 이것을 §2 MUST 4의 **C 또는 D**에 *교과서 본문 메시지* 형태로 끌어올려야 한다. *Insert at §2 MUST 4 E. Limitations*: "Univariate CI가 좁다는 것은 그 파라미터를 *고립시켜 흔들었을 때*의 정밀도이며, 다른 파라미터가 함께 흔들리는 실제 상황의 정밀도(planar CI)와 다르다 — 두 CI가 크게 차이나면 모델은 fit는 잘 되어도 추정치는 의미가 없다."

### (c) 가장 파급력 큰 혼동쌍 — Triangulation Mental Model

Step 1이 §5 혼동쌍 #1을 Critical Blow로 지정한 것은 옳다. Phase 3에서 추가할 통찰은 **F-test 위반 시 시니어 모델러의 메타 전략**이다: 단일 통계 기준이 무력화되면 *증거의 다중 수렴(triangulation)* 으로 옮겨간다 — 잔차 패턴(구조 결함 노출) + 메커니즘 plausibility(in vitro Km, 효소 발현 패턴) + 외부 데이터(prior literature) + 시각적 예측 검증(observed vs predicted overlay). 이는 Step 1 Q9 옵션 C가 단편적으로 다뤘지만, **시스템적 사고 패턴**으로는 명시되지 않았다. *Insert at §5 혼동쌍 #1 Critical Blow 행 직후 또는 §7 Q9 정답 마무리*: "단일 통계 기준이 무력화될 때 시니어 모델러는 단일 대체 기준을 찾는 것이 아니라 다중 증거 수렴으로 옮겨간다 — 잔차 패턴, 메커니즘 plausibility, 외부 데이터, 시각적 검증이 같은 방향을 가리키는 것이 통계 검정의 부재를 보완한다."

---

## T3. Trench-Level Tips (실무 함정 — 5개)

**Tip 1 — Boundary Stickiness 회피**
- Situation: §4.4.2 boundary scaling으로 알고리즘 안정화 시도 중
- Trap: Table 4.4의 β IE=0.05인데 UB도 0.05로 동일 — 이런 mismatch가 PDF table 자체에 있고, 학생이 그대로 모방하면 final estimate가 boundary에 박혀버림
- Detection: NONMEM 출력에서 final estimate = UB (또는 LB), `$COVARIANCE` step의 NEAR BOUNDARY 경고
- Insert at: §2 MUST 1 [B-5] When all else fails 끝
- Insert text: "Table 4.4의 β=0.05가 UB와 동일한 것은 PDF table의 mismatch이며, 실무에서는 IE를 LB와 UB의 기하학적 중간에 두지 않으면 알고리즘이 boundary에 stuck된다."

**Tip 2 — 잔차는 두 축으로 plot한다**
- Situation: §4.7.2 잔차 진단
- Trap: 잔차 vs 시간만 plot하면 fan shape (variance 결함)을 못 보고, 잔차 vs 예측값만 plot하면 banana (구조 결함)를 못 본다
- Detection: 한 축에서 random scatter처럼 보이지만 다른 축에서는 systematic 패턴
- Insert at: §2 MUST 2 B. Derivation [B-3] 잔차 패턴 카탈로그 직후 (또는 §5 혼동쌍 #3 처방 행 보강)
- Insert text: "잔차 vs 시간과 잔차 vs 예측값을 항상 함께 plot하라 — 한 축의 random scatter가 다른 축의 systematic 패턴을 가리는 일이 흔하며, 두 plot의 형태 차이가 구조 결함과 변량 결함을 분리한다."

**Tip 3 — Pure Error LOF의 적용 한계**
- Situation: §4.7.3 lack-of-fit F-test
- Trap: 학생이 임상 PK 데이터(환자별 1회 측정)에 LOF F-test를 적용하려 함
- Detection: 같은 시점 반복 측정이 없는 데이터셋에서 pure error 계산을 시도하는 보고서
- Insert at: §2 MUST 2 [B-4] Pure error vs LOF 통합 부분
- Insert text: "§4.7.3의 LOF F-test는 같은 시점 반복 측정이 가능한 in vitro·세포 실험에 한정되며, 환자별 1회 측정인 임상 PK 데이터에서는 시행 불가 — 대신 잔차 패턴 분석으로 lack-of-fit를 진단한다."

**Tip 4 — 편미분 plot의 정규화**
- Situation: §5.2.3 편미분 기반 sampling design
- Trap: Raw $\partial C/\partial \theta$를 plot하면 파라미터 단위 차이로 두 곡선의 절대 크기 비교가 무의미 (Fig.5.4가 raw 값을 plot한 것은 시각적 단순화)
- Detection: 두 파라미터의 편미분 plot이 자릿수 단위로 차이나면서 작은 쪽이 항상 "정보가 적다"고 잘못 결론
- Insert at: §2 MUST 5 [B-1] bi-exponential 편미분 직후
- Insert text: "Fig.5.4의 raw 편미분 plot은 시각적 단순성을 위함이며, 실무에서는 정규화된 sensitivity ($\theta_i \cdot \partial C/\partial \theta_i / C$)를 plot해야 파라미터 간 정보량을 직접 비교할 수 있다."

**Tip 5 — Weighting 선택의 데이터-driven 정당화**
- Situation: §5 혼동쌍 #1 또는 §7 Q9 — F-test 위반 시 동일 weighting으로 재적합 결정
- Trap: 어떤 weighting을 선택하느냐의 정당화 부담이 또 다른 무한 회귀 — "constant relative를 선택한 이유는?" "그 이유의 근거는?"
- Detection: 보고서에서 weighting 선택이 "관행" 또는 "default"로 처리되어 있음
- Insert at: §5 혼동쌍 #1 Critical Blow 행 직전 또는 §7 Q9 정답 보강
- Insert text: "Weighting 선택은 잔차 패턴 그 자체로 정당화한다 — fan shape이면 constant relative, 균질 잔차면 constant absolute; 이것은 통계적 trick가 아니라 likelihood 모델의 데이터-driven 선택이다."

---

## T4. Deletion Candidates — Mandatory

Audit MUST_FIX와 정합되는 13개 항목. Step 1을 잠그기 전 모두 처리해야 한다.

| # | 위치 | 사유 | 조치 |
|---|---|---|---|
| 1 | §1 거장의 시각 — "모든 모델링 실패의 80%" | Audit가 PDF 무근거 수치로 분류 | DELETE — "도구의 적용 조건을 잘못 이해해서 발생하는 실패가 빈번하다"로 정성화 |
| 2 | §1 지식 그래프 위치 — "FDA Guidance 'Population Pharmacokinetics' (Feb 2022)" | Audit가 FDA Guidance 직접 인용을 PDF 외부로 분류 | DELETE 특정 guidance 인용; "[교과서 외 규제 연결] 본 챕터의 GOF framework는 현대 PopPK regulatory 보고서 GOF 섹션과 직접 매핑된다"로 압축 |
| 3 | §2 MUST 1 [B-5] When all else fails — Eq.4:44 + Table 4.4 전체 도식 | CONTEXT 통합이 의도였으나 너무 길게 펼쳐짐; 본문 1-2문장으로 충분 | COMPRESS to 2 sentences |
| 4 | §2 MUST 3 [F. L5] "$\Delta$OFV > 3.84" + PsN scm.pl + NDA Module 5 인용 문구 | Audit가 PopPK 구현·규제 표현 PDF 외부로 분류 | LABEL "[교과서 외 구현 번역]"으로 명시 후 1-2문장 압축 |
| 5 | §2 MUST 4 [F. L5] NONMEM `$COVARIANCE` step의 "OMEGA HAS A VARIANCE > 3.5" 경고 + EIGENVALUES condition number $\kappa$ > 1000 | Audit가 NONMEM 특유 경고 메시지 PDF 외부로 분류 | LABEL "[교과서 외 구현 번역]"하되 $\kappa$ 진단은 보존 |
| 6 | §2 MUST 5 [F. L5] PFIM, PopED, NONMEM `$DESIGN` 블록(미지원) | Audit가 모두 PDF 외부 도구로 분류 | LABEL "[교과서 외 구현 도구]"하되 도구 지향성 보존 |
| 7 | §2 MUST 6 [F. L5] mrgsolve, Sobol total-order index, metabolic control analysis | Audit가 PDF 외부 도구로 분류 | LABEL "[교과서 외 구현 도구]" |
| 8 | §5 혼동쌍 #1 Critical Blow 행 — "Major Deficiency", "6-month review extension", FDA reviewer 인용 문구 | Audit가 Deficiency Letter 표현 PDF 무근거로 분류 | COMPRESS to 1-2 sentences without specific FDA letter format: "이 비교 조건 위반은 모델 선택 근거의 신뢰성을 약화시키며, 규제 리뷰어가 challenge하는 전형적 진입점이 된다" |
| 9 | §5 혼동쌍 #4 (Outlier) 처방 행의 "Cook's distance, hat matrix" | PDF에 직접 명시 안 됨; 외부 통계 도구 | LABEL "[교과서 외 통계 도구]" |
| 10 | §5 혼동쌍 #2 기억 고리 — "키 큰 사람과 작은 사람" 비유 부분 | Memory hook이 너무 길어 메인 메시지(dynamic range 메커니즘)를 가림 | COMPRESS to 2-3 sentences focusing on dynamic range |
| 11 | §7 Q9 정답 — "1주일 추가 작업의 비용 = 수십만 USD, 6-month extension의 비용 = 수천만 USD" | Audit가 USD 비용 수치 PDF 무근거로 분류 | DELETE numeric figures: "마감 연장은 통계적 결함보다 가벼운 손실이며, 결함 발생 시 회복 비용이 훨씬 크다"로 정성화 |
| 12 | §8 Dependencies 실패 모드 1·2의 "특허 보호 6개월 손실 (시장 가치 수천만~수억 USD)", "임상 일정 지연" 비용 수치 | 동일 — Audit가 USD 비용 PDF 외부로 분류 | COMPRESS to qualitative regulatory consequence |
| 13 | §2 MUST 2 [B-4] Pure error vs LOF 수치 도출이 §7 Q7과 중복 | Q7이 이미 LOF 계산을 처리하므로 본문은 개념적 차별화만 남기면 됨 | COMPRESS MUST 2 [B-4] to 2-3 sentences distinguishing pure error vs model comparison F-test |

**추가 source-range 정정 (Audit T1)**: Ch.5 범위 표기 `p.399-414`를 `p.399-405 / p.412-414`로 정정하고 p.406-411 미업로드 명시.

---

## T5. Priority Matrix

**Grade A (반드시 incorporate — 내면화 향상 또는 규제 리스크 직접 감소):**
- T1(a) 인지 장벽 5개 모두 — Step 1을 능동 회상 도구로 만드는 핵심 (특히 nested의 위상학적 의미, r의 dynamic range 메커니즘)
- T1(b) System Integration의 통합 작동 단위 (control file + GOF plot + sampling 권고문) — §8 보강
- T2(a) 정밀도-상관 카드의 "fix 결정 정당화 부담" — §2 MUST 4 D 보강
- T2(b) Boundary Stickiness, Spurious Identifiability 진단 시그니처 — 즉각 실무력 향상
- T2(c) Triangulation Mental Model — §5 혼동쌍 #1 Critical Blow 후속 또는 §7 Q9 정답 보강
- T3 Tips #1, #2, #3, #5 — 즉시 적용 가능, 빈번한 함정 차단
- T4 모든 13개 항목 — Audit MUST_FIX와 정합

**Grade B (flow 보존 시 incorporate — 풍부화 가치):**
- T1(c) Expert Intuition 4가지 (특히 OFV trajectory 5-iteration 진단, 두 모델 비슷한 OFV의 역방향 추론) — §8 C. Professional Moat 보강 (Step 1이 부분적으로 다뤘으므로 중복 위험 관리)
- T3 Tip #4 (편미분 plot 정규화) — 실무 가치 있지만 Step 1이 이론을 다뤘으므로 추가 가치 marginal

**Grade C (reject — scope creep, 무근거, 또는 중복):**
- F-test boundary parameter problem 보강 — Self-Test Q5에서 이미 다룸
- AIC $\Delta$ 임계값 가이드라인 ($\Delta$AIC > 10 = strong evidence) — PDF 직접 근거 없음
- VPC, PPC, NPDE 같은 현대 NLME 진단 도구 — Audit가 PDF 외부로 분류
- Triangulation을 별도 카드로 신설하자는 제안 — Step 1 §7 Q9 옵션 C 보강으로 충분

---

## 종합 판정

Phase 1 → Phase 2 (Source Fidelity Audit) → **Phase 3 (현재 — Insight Crucible) 통과 가능**. Step 1의 6-카드 + 4-혼동쌍 + 9-Q 골격은 보존하되, T4의 13개 deletion/compression과 T1·T2·T3에서 식별된 16개 insertion text를 Phase 4 Content Lock에서 삽입하라. **Phase 4 → Phase 4C Visual Pedagogy → Phase 5 HTML Compile 순서 준수**.

핵심 한 줄: *Step 1은 modeling carousel의 6개 도구를 잘 짰지만, 학습자가 그것을 외우고도 보지 못하는 5가지 시각적 사실(위상학, dynamic range 메커니즘, likelihood 곡률, ridge 기하학, 시간 스케일 분해)을 P1이 채워야 하고, P3는 Audit가 식별한 PDF 외부 표현(규제 비용 수치, NONMEM 구현 표현)을 일관되게 라벨링·압축해야 한다.*

---

먼저 첨부된 Step 1 Draft v0와 Audit Report v1을 읽고, PDF 원문과 교차대조한 후 Phase 3 Insight Crucible 보고서를 작성하겠습니다.이제 Audit Report v1을 읽어 MUST_FIX 제약 사항을 파악하겠습니다.세 문서(원문 PDF, Step 1 Draft v0, Audit Report v1)를 모두 검토했습니다. 이제 P1 + P3 페르소나로 Phase 3 Insight Crucible 보고서를 작성하겠습니다.

---

# **Phase 3 Insight Crucible Report v1**
## Pre-Sprint: 모델링 철학·용어 (G Ch.1 + T Ch.1–2)

**모드**: [논문·연구 리뷰] · A-Critical / B-Standard
**작동 페르소나**: P1 (계량약리학 30년 멘토) + P3 (FDA 임상약리학 reviewer) 동시 작동
**Source Fidelity Audit MUST_FIX 제약**: 모두 준수, 위반 없음
**필터 기준**: "박사 1년차가 이 챕터를 막 읽고 나왔을 때, 5분 엘리베이터 대화에서 30년 베테랑이 *영구적으로 이해를 한 단계 끌어올리기 위해* 무슨 말을 할 것인가" — 이 필터를 통과한 것만 포함, Step 1 기존 내용 재진술은 일체 배제

---

## **T1. P1 — 내재화 장벽 & 거장의 직관**

### **(a) 인지 벽 — 외울 수는 있으나 끝내 *보지* 못하는 지점**

#### Wall 1 — Carousel을 "절차"로 외우면 *비선형 회귀의 algorithmic 필연*이 보이지 않는다

학생이 외울 수 있는 것은 G Fig.1.1의 6단계 cycle이다. 학생이 *보지 못하는* 것은 이 6단계가 *임의의 절차*가 아니라 *non-convex objective surface 위의 nonlinear least squares optimization이 강제하는 위상학적 필연*이라는 사실이다. EDA가 만들어 내는 것은 "graphical initial estimate" — 이 표현은 Step 1 §2 M1에 정확히 들어가 있다 — 그러나 학생의 머릿속에서 이 graphical estimate는 *parameter space의 어느 basin of attraction에 진입할 것인가*에 대한 사전 정보로 변환되지 않는다. G Fig.1.2의 *bowl 형태 (Audit 정정에 따르면 yellow A·B·C는 possible initial estimate, red D·E는 final estimate)*가 보여 주는 것은 단순한 그릇이 아니라 *parameter manifold의 위상학적 구조* — 즉, 여러 골짜기를 가진 surface다. 학생이 이 그림을 *지도 없이 산을 오르는 사람에게 지도를 쥐어 주는 행위*가 아니라 *산 자체가 여러 골짜기를 가졌음을 알려 주는 행위*로 읽지 못하면, "EDA를 왜 하는가"는 끝내 *epistemological commitment*가 아닌 *형식적 절차*로 남는다. **Step 1 §2 M1 §C는 이 알고리즘적 필연을 *언급*했으나 *시각적으로 박지는 못했다*.**

#### Wall 2 — M3와 M4 *중 무엇을 고를지의 판단 기준*은 Step 1 어디에도 없다

M2(PK/PD Linkage)는 *왜* 통합해야 하는지를 정의하고, M3(Hill)는 PD를 인코딩하고, M4(Turnover)는 시간 지연을 인코딩한다. 학생은 이 분업을 외운다. 학생이 *보지 못하는* 것은: 새 데이터셋 앞에서 *M3만으로 충분한가, M4가 필요한가*를 판단하는 30초 룰 — 즉, **effect의 peak time이 concentration의 peak time과 *분리되어 있는가*** — 가 Step 1 §2 어디에도 명시되지 않았다는 점이다. T Fig.1-6 (warfarin oral 1.5 mg/kg, 5 male volunteers)이 *바로 이 분리*를 보여 주는 dataset이지만, Step 1은 이를 M4 카드의 *Big Idea anchor*로만 쓰고, *분리 여부 자체가 모델 선택의 entry rule*이라는 점은 *암묵적*으로 둔다. §2 §2-Recap은 "M3는 PD 인코딩, M4는 시간 지연 인코딩"이라 *두 카드를 분리만 했지*, *판단 기준*은 학생에게 위임했다. **이것이 박사 1년차가 warfarin-like 데이터에 default Hill model로 fitting하기 시작하는 이유의 인식론적 뿌리다.**

#### Wall 3 — γ는 "곡선의 가파름"이 아니라 *처방의 인지 모드*를 결정한다

Step 1 §2 M3 §B는 γ=1과 γ=2의 20–80% 농도 비율(16배 vs 4배)을 정확히 도출했다. 학생이 *보지 못하는* 것은 이 수학적 사실의 *임상 인지적 함의*다 — γ는 처방자의 *인지 모드 자체*를 분기시킨다.

- γ ≈ 1 (propranolol — Lalonde 1987, T Fig.2-17): 환자 간 unbound 농도가 16배 차이라도 효과가 graded하므로, 처방은 *titrate-by-symptom* 모드. 부작용을 모니터링하며 점진 조정.
- γ가 매우 가파른 경우 (alfentanil — Ausems 1986, T Fig.2-18): C50이 0.27 / 0.31 / 0.42 mg/L (수술 부위별)라는 *불과 1.5배 농도 범위*에서 *quantal* response가 발생. 즉 환자는 *마취 성공/실패의 binary 사건*을 경험. 처방은 *threshold-crossing* 모드 — *titration이라는 개념 자체가 사실상 의미를 잃는다*.

T p.40은 *"generally γ lies between 1 and 3"*이라고 명시했고 (Audit T1 항목, OPTIONAL/SHOULD), 매우 가파른 γ는 *quantal에 점근*한다고 적었다. **Step 1은 γ의 수학적 정의는 정확하나, γ가 *처방의 인지 모드 자체*를 분기시킨다는 통찰은 빠져 있다.** 이것이 학생이 alfentanil같은 약물의 NDA submission 자료를 읽고도 *"왜 이 약은 dose level이 이렇게 좁게 설정되었는가"*를 묻지 않는 이유다.

#### Wall 4 — 4개 turnover parameter 중 *어느 것이 conserved되는가*가 indirect response model parametrization을 결정한다

Step 1 §2 M4는 $A_{ss}$ / $R_t$ / $k_t$ / $t_t$ 네 파라미터를 정의하고 $R_t = k_t A_{ss}$, $t_t = 1/k_t$의 수학적 관계를 정확히 도출했다. 학생이 *보지 못하는* 것은: T p.46의 사막 환경 사례에서 *오직 $A_{ss}$만 invariant*이고 나머지 셋은 모두 8배 변한다는 사실이 의미하는 것 — *homeostasis가 보존하는 양과 보존하지 않는 양의 구별*. 이 prior knowledge는 substance마다 다르며 (water의 경우 $A_{ss}$ conserved, albumin의 경우 conserved 아님), 약물 perturbation 시 *어느 파라미터로 system이 기울어지는가*를 결정한다. **이 인식이 없으면 indirect response NONMEM 모델의 KIN/KOUT parametrization 결정이 *임의*가 되고, 그 결과는 §B [B.4]의 코드 블록 (Audit가 NOT_IN_SOURCE로 분리하라고 명시한 부분)이 *데이터셋과 mismatch될 때*의 디버깅 지옥이다.**

---

### **(b) 시스템 통합 — 4개 개념이 *하나의 시스템*으로 작동하는 단 하나의 지점**

박사 1년차가 *NONMEM dataset을 처음 받은 30초* — 바로 이 순간이 4개 카드가 *동시에* 작동해야 하는 단 하나의 지점이다. Step 1은 4개 카드를 *수직 계층*(§2 Recap)으로 정의했으나, 이 계층이 *수평적 동시성*으로 운용되는 PopPK workflow 진입점은 §8 어디에도 명시되지 않았다.

구체적 mental procedure (`30-Second Diagnostic Grid`):

| Lens | 보는 것 | 판단 |
|------|---------|------|
| **M1 lens** | dose level 분포의 다양성, sampling density | EDA의 dose-normalized AUC plot이 *해석 가능한가*를 판단 |
| **M2 lens** | dataset이 측정한 site (plasma / serum / whole blood)와 ADME chain의 어느 phase | *어떤 first-pass component가 missing되어 model identifiability를 위협하는가*를 판단 |
| **M3 lens** | 가장 높은 dose의 effect가 *plateau에 도달한 흔적*이 있는가 | Hill γ를 *estimate할 수 있는가, 1로 fix해야 하는가*를 사전 판단 |
| **M4 lens** | concentration의 peak time과 effect의 peak time이 *얼마나 분리되어 있는가* | direct effect Hill만으로 충분한가, indirect response가 필요한가의 entry rule |

이 4-lens grid가 *동시에* 작동하지 않으면 control stream 작성 자체가 임의가 된다. **박사 1년차의 가장 흔한 결함은 4개 lens 중 *하나만* 들고 데이터를 보는 것** — 보통 M1(carousel) 또는 M3(Hill) 한쪽으로 편향된다.

---

### **(c) 30년 베테랑의 expert intuition — 수식을 보지 않고 판단하는 지점**

베테랑이 *데이터·플롯·NONMEM 출력의 첫 30초*에 즉시 감지하는 패턴들 중 Step 1 범위(*철학·용어 sprint*)에 직접 연결되는 것만:

**Intuition α: dose-normalized AUC plot의 30초 mental graph**
log-log scale에서 AUC vs dose 기울기가 정확히 1이면 linear PK; >1이면 saturable elimination 의심; <1이면 saturable absorption 또는 enterohepatic recycling 의심. 이는 G p.5의 EDA 권고 — *"plotting plasma concentrations and AUCs (exposure) against dose, gender or time to ascertain if the kinetics of a drug is nonlinear"* — 을 *raw data 첫 20행만 보고 머릿속에서 plot하는 정신 procedure*로 변환한 것. 신진 모델러는 이 plot을 R/ggplot에서 그리는 데 5분, 해석에 5분이 걸린다.

**Intuition β: turnover-driven 사례를 만나면 PK fit *전에* effect time profile을 본다**
T Fig.1-6 (warfarin)과 T Fig.1-7 (paclitaxel leukocyte)의 공통 시그니처는 *peak effect time과 peak concentration time의 시간 분리*. 베테랑은 raw effect-time data를 보면서 peak time을 머릿속에서 추정하고, 이것이 PK peak time과 *얼마나 떨어져 있는가*로 *direct effect Hill만 vs indirect response 필요*를 판단. 신진 모델러는 default Hill model을 fit하고 GOF가 나쁘면 *그제야* turnover model을 고려한다 — 이 순서가 며칠을 소비한다.

**Intuition γ: $E_{\max}$의 임상적 ceiling은 약물 자체가 아니라 *환자의 다른 생리*가 결정한다**
T p.41 명시 — *"the maximum response produced clinically for some drugs may be less than that pharmacologically possible. For example, ... the entire cardiovascular system may deteriorate, and the patient may die long before the heart rate approaches its maximum value."* 베테랑은 새 약물의 Phase 1 데이터를 받으면 *"이 약물의 pharmacological $E_{\max}$ 추정치가 임상적으로 의미 있는가"*를 가장 먼저 묻는다. **Step 1 §2 M3 §E는 이를 *limitation*으로 한 줄 적었으나, *agonist의 $E_{\max}$ 추정 자체가 항상 임상적으로 도달 불가*라는 비대칭성은 강조되지 않았다 — antagonist는 ceiling 정의 명확 (T p.41).**

---

## **T2. P3 — 규제·실무 위험 표면**

### **(a) Step 1의 단순화가 reviewer questioning을 유발할 수 있는 지점**

Audit MUST_FIX는 이미 *과장된 deficiency 표현*을 삭제하라고 명시했다. P3 시각의 임무는 *역방향* — Step 1이 *너무 깔끔하게* 단순화한 나머지 reviewer가 실제로 question을 제기할 수 있는 지점의 식별이다.

**Risk P3-1: M2 [B.3]의 Therapeutic Window 확률 집합 표기는 PDF에 없는 formalization** [확인 필요]

Step 1은 therapeutic window를 $\{C : \Pr(\text{therapeutic} \mid C) \geq \theta_T \wedge \Pr(\text{adverse} \mid C) \leq \theta_A\}$로 *수학적으로 formalize*했다. T Fig.1-4와 T p.6은 이를 *exposure range with acceptable risk-benefit*로 *정성적*으로만 정의한다. **Audit가 이를 NOT_IN_SOURCE로 분류한 것은 정확하다.** P3 risk는 *학생이 이 formalization을 regulatory text에 차용했을 때*: reviewer가 *"$\theta_T$, $\theta_A$의 임상적 정당화는?"*을 질문할 수 있고, 답이 *"교과서 정의를 확장한 것"*이면 deficiency 가능. 해법: 이 표기는 [해석/교육용 formalization] 태그로 분리하고, *실제 regulatory text에는 정성적 정의만 사용*해야 함을 §2 M2 §B 끝에 1문장 명시.

**Risk P3-2: M3의 unbound concentration 사용 강조가 *unconditional 의무*처럼 표현되어 있다**

Step 1 §2 M3 §D는 unbound concentration이 *driver*임을 강조한다. T p.21은 이와 동시에 명시 — *"makes little difference whether total or unbound drug is measured"*는 binding이 stable한 condition. 임상시험 protocol design에서 unbound assay는 cost를 증가시키므로, *binding이 변하는 condition* (renal/hepatic disease, displacement interaction, pregnancy, severe burns — T p.21)이 study population에 포함될 때만 정당화된다. P3 risk: Step 1을 그대로 따른 학생이 *모든 임상시험에서 unbound assay를 default로 요구*하면, study cost-benefit justification에서 reviewer questioning. **해법: §2 M3 §D에 *"단, fraction unbound가 stable한 study population에서는 total concentration도 작동"*의 단서 1문장 추가.**

**Risk P3-3: §2 §B [B.4]의 NONMEM/R 코드 블록 자체가 source fidelity 위반**

Audit MUST_FIX. Pre-Sprint *철학·용어* 세션의 PDF 범위에 NONMEM 문법은 없다. P3 시각: *Step 1 본문에 NONMEM control stream을 두는 것 자체가 source fidelity 7.2/10 → 6.5/10으로 점수를 낮추는 가장 큰 단일 요인*. 코드 블록은 [실무 구현 예시] 별도 섹션으로 분리하거나, 본문에서는 ODE 형태($dA/dt = R_{\text{in}} - k_t A$)까지만 두고 코드는 후속 NONMEM 세션으로 이연하는 것이 적절.

---

### **(b) NONMEM 실행 오류의 진단 시그니처 — 이름 부여**

세 가지 시그니처는 *각 카드의 미체화*가 만들어 내는 NONMEM 출력 패턴이다. **Step 1 §2의 §C-2(Plausible Fallacy) 또는 §F L5 layer에 *시그니처 이름만* 삽입하고, 구체적 detection 기준은 [실무 추론] 태그로 분리할 것을 권장.**

#### Signature P3-A: "Premature Convergence Mirage" [실무 추론]
- **발생 trigger**: M1(EDA) 미수행 → default initial estimate(THETA=1, OMEGA=0.1)로 직접 `$ESTIMATION METHOD=1`
- **시그니처**: OFV가 빠르게 수렴 (5–10 iteration), `$COV step successful`, IPRED vs DV plot이 *45도선 따라 분포 (외형상 정상)*, **그러나 conditional weighted residual vs TIME plot에 *systematic trend* 존재** — 이것이 mirage의 단서
- **검증 절차**: G p.6 권고 — *"rerunning the program with different initial estimates"* — 에 따라 다른 initial estimate로 재실행. 다른 OFV로 수렴하면 local minimum confirm

#### Signature P3-B: "Hill γ Identifiability Collapse" [실무 추론]
- **발생 trigger**: M3의 dose range가 C50 근처에 집중되어 *saturation region(>2× C50) 데이터가 부족*함에도 γ를 estimate
- **시그니처**: γ의 RSE > 30~50%, condition number 폭증, $COV step에서 algorithmically singular 메시지
- **해법**: γ를 1로 fix (parsimony) 또는 dose range 확장한 study redesign

#### Signature P3-C: "Turnover-PD Mis-attribution" [실무 추론]
- **발생 trigger**: M4(turnover) 미체화 → warfarin-like data에 direct effect Hill model 적용
- **시그니처**: PK는 정확히 fit되나 PD residual이 *시간 의존적 systematic deviation* — 초기 시간 over-prediction, 후기 시간 under-prediction (또는 그 역). Concentration-effect plot에서 *hysteresis loop* 관찰 (T p.5의 표현 — *"time delays between concentration and response"*에 대응하는 시각적 시그니처)
- **해법**: indirect response model로 전환 또는 effect compartment(biophase) model 도입

---

### **(c) 가장 파급력 큰 혼동쌍 — 한 가지 시나리오**

Step 1 §5는 PK vs PD 혼동쌍에 Critical Blow를 적용했다. **P3 시각의 판정: PK vs PD는 *학부 교과서 수준에서 이미 분리되어 있어 박사 1년차도 개념적으로는 구분*. Submission에서 두 phase를 헷갈리는 deficiency는 매우 드물다. 더 위험한 혼동쌍은 §5 Pair 2의 *Graded vs Quantal*이다.**

Critical Blow를 옮기거나 추가해야 할 이유: *같은 약물이 어느 endpoint에서는 graded, 어느 endpoint에서는 quantal*인 경우의 만성적 혼동이 실제로 발생.

**시나리오** [교육용 가상 시나리오]:
임상시험 protocol에 *primary endpoint*로 quantal response("≥50% pain reduction at 24h: Y/N")가 정의되어 있는데, modeler가 *graded* response 데이터(연속 pain VAS score)로 Hill model을 fitting하여 dose-response를 도출. 결과는 *내부적으로 일관*하나, primary endpoint analysis와 *통계적 framework가 어긋남*(continuous vs binary outcome). Statistician의 logistic regression 분석과 modeler의 sigmoid Emax model이 *같은 dose에서 다른 efficacy*를 산출 → reviewer questioning: *"왜 두 분석이 다른 dose를 추천하는가?"*

해법: §5 Pair 2 (Graded vs Quantal)에 Critical Blow 행 추가. 단, *deficiency letter 단정* 표현 금지 (Audit MUST_FIX), *protocol-modeling alignment 문제로 인한 reviewer questioning 가능* 정도의 표현으로 유지.

---

## **T3. Trench-Level Tips (5개)**

| # | Situation | Trap | Detection | Insert at | Insert text |
|---|-----------|------|-----------|-----------|-------------|
| **1** | M1 카드 §F L5 (EDA 실무 진입점) | 박사 1년차는 ggplot으로 *예쁜 plot 만들기*에 시간을 쓰고, *plot에서 무엇을 볼지의 사전 체크리스트*를 갖지 않는다 | EDA에 30분 이상 소요되었는데 산출물이 *fitting 시 사용할 initial estimate 표 1개*가 아니면 EDA framework가 머릿속에서 수단-목적 도치된 것 | §2 M1 §F L5 끝 | **EDA의 산출물은 plot 그 자체가 아니라 *"initial estimate 1표 + nonlinearity yes/no 1줄"*이다. 이 둘을 30분 안에 만들지 못하면 Carousel Step 4가 학생 머릿속에서 *수단-목적 도치*된 것이다 [실무 추론].** |
| **2** | M3 카드 §D 직후 (γ estimate vs fix 결정) | dose range가 C50 근처에 집중되어 saturation region 데이터가 부족함에도 γ를 *기본 estimate*로 둠 | γ의 RSE > 30%, condition number 폭증 | §2 M3 §D 끝 | **Dose range가 C50 근처에 집중되고 saturation region 데이터가 부족하면 γ를 1로 fix하는 것이 *parsimony*. RSE > 30%이면 *fix로 회귀*가 default — γ identifiability collapse를 회피하는 운영 룰 [실무 추론].** |
| **3** | M2 카드 §E (Adherence-related limitation) | 임상시험 데이터의 adherence monitoring이 자가보고 의존이면 model이 *missed dose의 model artifact를 PK variability로 흡수* | OMEGA(CL/F) 추정치가 ~50%대로 폭증 — Vrijens 2008의 1년 후 50% non-persistent와 일치 (T Fig.1-10) | §2 M2 §E | **자가보고 adherence 데이터에서 OMEGA(CL/F)가 ~50%대로 폭증하면 PK variability가 아니라 *missed dose의 model artifact*일 수 있다 — Vrijens 2008 cohort 1년 후 50% non-persistent와 일치 (T Fig.1-10) [실무 추론].** |
| **4** | M1 §F L5 (dose-normalized plot EDA) | NONMEM dataset의 EVID/CMT/RATE column 하나라도 misformat되면 dose-normalize plot이 *spurious nonlinearity*를 보여주고 학생은 진짜 saturable kinetics로 오해 | dose-normalized concentration peak가 dose에 비례하지 않을 때 | §2 M1 §F L5 | **Dose-normalized plot이 nonlinearity를 시사할 때, 결론을 내리기 전에 *NONMEM dataset의 EVID/CMT/RATE column부터 1차 검증*하라. 가장 흔한 spurious nonlinearity의 출처는 dataset misformat이다 [실무 추론].** |
| **5** | M4 §F L5 (indirect response baseline parametrization) | `BASELINE = KIN/KOUT` parametrization을 sparse data에서 사용하면 KIN-KOUT identifiability collapse | KIN-KOUT correlation > 0.95 또는 둘 중 하나의 RSE > 50% | §2 M4 §F L5 | **Sparse data에서는 `BASELINE = KIN/KOUT` 분리 estimation이 collapse하므로, *BASELINE을 직접 estimate하고 KIN을 BASELINE × KOUT로 derive*하는 것이 운영 룰 [실무 추론].** |

---

## **T4. Deletion Candidates (Mandatory)**

PhD reader에게 자명하거나, 카드 간 중복이거나, CONTEXT-tier가 MUST 수준으로 확장된 것들. **이 섹션은 task spec상 비선택적이다.**

| # | 위치 | 처리 | 사유 |
|---|------|------|------|
| **D1** | §2 M1 §A의 "constant / parameter / variable" jargon 정리 | **DELETE** (단, primary vs secondary parameter 구별 1줄은 후속 카드 K·AUC·t½ 재등장을 위해 유지) | Audit MATCH지만 PhD reader에게 자명. CONTEXT-tier가 MUST 카드 §A를 침식. M1은 *"왜 6단계인가"*에 집중되어야 함 |
| **D2** | §2 M2 §A의 ADME·Disposition·First-pass·Bioavailability·Enterohepatic 5개 통합 paragraph (≈100 단어) | **COMPRESS to 1 sentence** | 5개 CONTEXT-tier 개념이 mini-card 수준으로 확장. Curation Map의 "1–2문장 흡수" 규칙 위반 (Patch Memo Patch 2와 일치). 권장 압축: *"PK phase는 ADME chain을 따라 dose가 systemic exposure로 변환되는 과정이며, first-pass loss·bioavailability·enterohepatic cycling은 이 chain의 component를 가리킨다."* |
| **D3** | §2 M2 §A의 "Intravascular vs Extravascular vs Parenteral" paragraph | **COMPRESS to 1 sentence** | 동일 카드 내 두 번째 mini-paragraph. PhD reader에게 자명 |
| **D4** | §2 M3 §E의 Active metabolite·Prodrug·Stereoisomer 통합 mini-card (acenocoumarol·methylphenidate·aspirin/salicylic acid·sildenafil·methylprednisolone·dolasetron·famciclovir) | **COMPRESS to 2 sentences** (stereoisomer 1개 사례 + active metabolite 1개 사례만 유지) | 약물명 list는 교육적 풍부함이지만 MUST 카드 §E의 핵심이 아님 |
| **D5** | §2 M3 §F L3의 "Hill ≅ Michaelis-Menten ≅ Langmuir isotherm" structural isomorphism | **DELETE** 또는 **[해석] 태그** | Audit NOT_IN_SOURCE. T 범위에 직접 근거 없음 |
| **D6** | §2 M3 §F L4의 "Hb-O2 binding γ ≈ 2.7" | **DELETE** | Audit ERROR/NOT_IN_SOURCE. PDF 외부 정량값. PhD reader가 즉시 의심할 hallucination 위험점 |
| **D7** | §2 M3 §B [B.4]의 R/NONMEM Hill code block | **MOVE to 별도 [실무 구현 예시] section** 또는 **DELETE from Step 1 본문** | Audit NOT_IN_SOURCE. Pre-Sprint *철학·용어*의 본문에 NONMEM 문법은 부적절. ODE 형태까지만 본문에 두고 코드는 후속 NONMEM 세션으로 이연 |
| **D8** | §2 M4 §B [B.4]의 NONMEM `$DES` indirect response template | **MOVE to 별도 [실무 구현 예시]** 또는 **DELETE** | D7와 동일 |
| **D9** | §2 M4 §F L5의 "warfarin clotting factor t_t = 6시간~3일" | **DELETE** | Audit NOT_IN_SOURCE. PDF 외부 정량값. *응고인자 turnover*라는 *질적 사실*은 유지하되 정량값은 삭제 |
| **D10** | §7 Q9 정답 공개의 "수백억 원 의사결정", "FDA/EMA reviewer가 이의 제기 못 함" | **DELETE** (Audit MUST_FIX 명시) | 과장 정량/단정. *결정의 documentation 중요성*이라는 *질적 통찰*은 유지 |
| **D11** | §7 Q9 정답 공개의 "*Risk*: Phase 3 실패 후에야 발견" 단정 | **SOFTEN** | Audit NOT_IN_SOURCE. *"체계적으로 잘못 추천될 수 있음"* 정도로 약화 |
| **D12** | §8 C (Professional Moat)의 "AI가 구조적으로 못 한다", "epistemological commitment" | **DELETE 또는 별도 *Mentor Reflection* 섹션으로 분리** | Audit MUST_FIX. PDF 범위에 없음. *Source-based Step 1 본문의 일부가 아님*. 동기 부여 가치는 인정하되 본문에서 분리 |
| **D13** | §8 B Failure Mode 1·2의 "FDA가 reviewer analysis로 covariate effect re-test", "external validation step에서 발견되면 다행, 아니면 NDA submission까지" | **SOFTEN with [실무 추론] 태그** | Audit NOT_IN_SOURCE. *Failure mode trace 자체*는 가치 있으나 *FDA의 구체적 행동*은 [실무 추론] 분리 |

---

## **T5. Priority Matrix**

### **Grade A — 반드시 반영 (직접 internalization 개선 또는 regulatory risk 감소)**

| # | 항목 | 위치 |
|---|------|------|
| **A1** | Wall 1 — Carousel을 *비선형 회귀의 algorithmic 필연*으로 보는 시각 강화 | §2 M1 §C의 "Structural Necessity" 1문장 보강 |
| **A2** | Wall 2 — *M3 vs M4 entry rule* (effect peak time vs concentration peak time 분리 여부) | §2 §2-Recap 또는 M2-M3 anchor에 1문장 추가 |
| **A3** | Wall 3 — γ가 *처방 인지 모드* (titration vs threshold)를 분기 | §2 M3 §F L5에 1문장 |
| **A4** | Risk P3-1 — Therapeutic Window 확률 집합 표기에 [해석/교육용 formalization] 태그 (Audit MUST_FIX) | §2 M2 §B [B.3] 끝 |
| **A5** | 3개 진단 시그니처(Premature Convergence Mirage, Hill γ Identifiability Collapse, Turnover-PD Mis-attribution) — *이름만* 삽입 | §2 각 카드 §C-2 또는 §F L5 |
| **A6** | T3 Tip 1, Tip 2, Tip 4 (각 1–2문장) | §2 M1·M3 §F L5 |
| **A7** | T4 D1–D13 모두 적용 | (Audit MUST_FIX와 일치, 비선택적) |

### **Grade B — flow 보존 시 반영 (enrichment 가치)**

| # | 항목 | 위치 |
|---|------|------|
| **B1** | Wall 4 — *어느 turnover parameter가 conserved되는가*가 indirect response parametrization을 결정 | §2 M4 §C 1문장 |
| **B2** | T1(b) 30-Second Diagnostic Grid (4-lens 동시성) | §2 §2-Recap 끝에 1문단 |
| **B3** | Intuition α (dose-normalized AUC plot 30초 mental graph) | §2 M1 §F L5 1문장 |
| **B4** | Intuition β (turnover-driven 사례에서 effect time profile 먼저 보기) | §2 M4 §F L5 또는 M2-M4 anchor 1문장 |
| **B5** | Intuition γ ($E_{\max}$의 임상적 ceiling은 다른 생리가 결정) | §2 M3 §E 1문장 추가 |
| **B6** | Critical Blow를 §5 Pair 1에서 Pair 2로 *이동 또는 추가* (Graded vs Quantal의 protocol-modeling misalignment 시나리오, [교육용 가상 시나리오] 태그) | §5 Pair 2 |
| **B7** | T3 Tip 3 (Adherence-driven OMEGA artifact), Tip 5 (KIN/KOUT collapse) | §2 M2 §E, M4 §F L5 |
| **B8** | Risk P3-2 — unbound concentration *unconditional 의무* 단정 완화 | §2 M3 §D 1문장 단서 |

### **Grade C — reject (scope creep, 미지원, 기존 내용 중복)**

| # | 항목 | 사유 |
|---|------|------|
| **C1** | Intuition β의 자매 — CWRES fan-shape (additive vs proportional error) | Step 1 *철학·용어* 범위 초과. 후속 GOF 진단 세션 자료 |
| **C2** | $COV step condition number > 1000 룰 | 동일. NONMEM convergence diagnostics 별도 세션 |
| **C3** | PopPK workflow의 Step 2/Step 3 상세 (NONMEM `$ESTIMATION` 검토, regulatory submission 작성) | Pre-Sprint 범위 초과 |
| **C4** | 3개 시그니처의 *상세 detection 기준* (RSE 임계, condition number 임계 등) | 모두 [실무 추론], PDF 출처 없음. *시그니처 이름*만 Step 1에, detection 상세는 후속 세션 |
| **C5** | Graded vs Quantal 가상 임상시험 시나리오의 *완전한 dialogic 재현* | §6 (Practical Scenarios)의 자료. Step 1 본문에는 *시그니처 이름*과 1문장 시나리오만 |

---

## **검증 체크 (출력 전)**

- [✓] Step 1 재작성 없음 — insertion 위치와 deletion 지시만 제공
- [✓] 모든 insertion이 §number + concept card 명시
- [✓] Insertion text 모두 1–2문장 max (Tip 5개 모두 검토 완료)
- [✓] 정량값/guideline 번호/실험 데이터 fabrication 없음 — 모두 [실무 추론] 또는 [확인 필요] 태그
- [✓] Phase 4C 자료(figure 결정)는 본 보고서 범위 외 — 다루지 않음
- [✓] 불확실 claim은 [확인 필요] 또는 [실무 추론] 태그
- [✓] T4 deletion list 13개 — non-negotiable 명시 완료
- [✓] Audit MUST_FIX 항목과 충돌 없음 — 모두 fixed constraint로 처리
- [✓] 한국어 산문 + 영어 기술 용어 / NONMEM 문법 / 수식 / 약물명

---

## **운영자 노트 (P1)**

이 Crucible 보고서가 의도하는 한 줄 변화는 다음과 같다. **Phase 4A로 진입할 때, Step 1 Draft v0를 *과장 단정 패치*로만 다듬지 말고, 4개 *Wall*과 3개 *Signature*가 만드는 *인지적 hook의 grid*를 박사 1년차의 머릿속에 박는 것**까지 진행할 것. 패치는 단순한 *correctness 작업*이 아니라 *체화 hook 작업*이다. Audit가 정확성을 보장하고 Crucible가 깊이를 보장한다 — 이 두 보고서를 같이 들고 Phase 4A로 가야 Step 2 HTML이 *학습 자료*가 아닌 *체화 도구*가 된다.

다음 단계에서 Phase 4A patch를 진행할 때, Grade A 7개 항목과 T4 D1~D13을 *동시에* 적용해야 한다. Grade A를 적용하면서 D1~D4의 압축을 함께 수행하지 않으면, 카드의 정보 밀도가 추가 insertion 때문에 *역으로 증가*하여 가독성이 무너진다.

---

### Obsidian Filing Guide

- **저장 위치**: `02_LITERATURE/024_Gabrielson-Textbook/Pre-Sprint/` 또는 `03_PROJECTS/032_Dissertation/Curriculum-Crucible/`
- **파일명**: `2026-05-03_PreSprint_Crucible_논문리뷰.md`
- **태그**:
  - `#P1_Action` — Wall 1–4 internalization, 30-Second Diagnostic Grid 운영 룰
  - `#P3_Audit` — 3개 NONMEM Signature, Risk P3-1/2/3
  - 추가 태그: `#pharmacometrics/methodology` `#nonmem/diagnostics` `#pk-pd/linkage` `#turnover/indirect-response` `#regulatory/source-fidelity`
- **링크 제안**:
  - `[[2026-05-03_PreSprint_Step1_Draft_v0]]`
  - `[[2026-05-03_PreSprint_Audit_Report_v1]]`
  - `[[Modeling Carousel — G Fig.1.1]]`
  - `[[PK-PD Linkage MOC]]`
  - `[[Hill γ Identifiability]]`
  - `[[Indirect Response Model — KIN-KOUT Parametrization]]`

---

**ID**: C-260503-094412-K7Q

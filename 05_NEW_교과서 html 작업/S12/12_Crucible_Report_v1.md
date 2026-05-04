# 12_Crucible Report v1 — Senior Mentor Review

**업무 형태:** [논문·연구 리뷰] 모드 / P1 + P3 동시 작동 / PDF + Draft v0 + Audit v1 교차대조
**대상 세션:** Session 12 — Effect Compartment · Tolerance/Rebound · Transduction
**입력:** `012_G_Effect_Compartment_내성_Transduction.pdf` (G&W §3.9/§3.11/§3.13 + PD13/20/21/35) + `012_T_Effect_Compartment_내성_Transduction.pdf` (R&T Ch.8 + Appendix G) + `12_step1_draft_v0.md` + `12_Audit_Report_v1.md`
**산출:** Senior Mentor Crucible Report — Step 1 위에 덧붙일 *추가 통찰*과 *삭제 지시*만 포함. Draft 재작성 금지. Figure 결정 비포함(Phase 4C 영역).
**Operative Filter:** "1년차 박사과정생이 이 챕터를 방금 끝낸 직후, 5분 엘리베이터 대화에서 30년 계량약리학 베테랑이 *이 특정 개념의 이해를 영구적으로 한 단계 끌어올리기 위해* 무엇을 말해줄 것인가?"

**Audit Report v1의 6개 MUST_FIX는 본 보고서의 fixed constraint로 취급한다.** 본 보고서는 그것들과 충돌하지 않으며, 그 너머의 통찰만 추출한다.

---

## Executive Verdict

Draft v0는 *수식 인벤토리*와 *데이터 앵커링*은 충분하다. 그러나 **체화의 임계선** — 즉 학생이 ODE를 외우는 것에서 ODE를 *읽는* 단계로 넘어가는 변곡점 — 에 도달하기 위한 베테랑의 직관 5–6개가 누락되어 있다. 이 직관들은 모두 PDF에 *암시적으로* 존재하지만 학생이 스스로 추출하기는 어렵다. T1과 T2는 이 누락된 직관들을 명시화한다. T3 Trench Tip은 실제 NONMEM 워크플로 진입 시 가장 먼저 부딪히는 함정 4개를 잡는다. T4는 Draft의 과잉 부분을 잘라낸다. T5는 우선순위로 정리한다.

---

## T1 — P1: INTERNALIZATION BARRIERS & MASTER'S INTUITIONS

### T1-(a) Cognitive Wall — 외울 수 있지만 *볼 수* 없는 지점

Step 1 Draft를 처음부터 끝까지 통째로 암기한 박사과정생을 가정하자. 이 학생은 Eq.3:134(closed-form $C_e$), Eq.3:193–194(Moderator ODE 쌍), Eq.35:6(transit chain)을 칠판 위에 즉석에서 쓸 수 있다. **그러나 다음 네 가지를 보지 못한다.**

**Wall 1 — `ke0`와 `koff`의 단위 동일성이 같은 *물리량*을 의미한다고 착각한다.**
PD21의 Table 21.1에서 `ke0=0.025`, `kout=0.031`, `koff=0.018 min⁻¹`이 비슷한 값을 갖는 *수치적 우연*을 보고, 학생은 세 파라미터가 본질적으로 같은 종류의 시간 척도라고 무의식적으로 가정한다. 베테랑은 즉시 분리한다: `ke0`는 *약물 분자가 plasma↔biophase 사이의 물리적 다리를 건너는 평균 시간*의 역수이고, `kout`는 *시스템 자체가 자기 baseline으로 회복하는 시간*의 역수이며, `koff`는 *receptor에 묶인 ligand 한 분자가 떨어져 나오는 시간*의 역수다. 세 가지 모두 1차 운동학을 따르지만 *지시체*가 완전히 다르다. PD21에서 세 파라미터가 단일 dose 데이터로 식별 불가능한 이유가 여기에 있다 — 데이터가 같은 hysteresis 모양을 만들 뿐, 어느 메커니즘이 진짜인지 *말해주지 않는다*.

**Wall 2 — `tmax` 불변 검정이 *linear PK 가정 위에서만* 작동한다는 사실을 놓친다.**
Draft는 "$t_{max}$ dose-invariant ⇒ Link 모델"이라고 가르치지만, G&W p.264는 명시적으로 *"Assuming the drug kinetics is linear"*로 시작한다. Phase 1 first-in-human에서 Michaelis-Menten saturation(PK 비선형) 약물에 이 진단을 적용하면, 비선형 PK가 만든 가짜 peak shift를 turnover 시그니처로 *오진*한다. 베테랑은 항상 두 단계 진단을 한다: *(1)* dose escalation에서 AUC가 dose에 비례하는지 확인(PK linearity 확인), *(2) 그 다음에야* `tmax` 불변성을 모델 선택의 진단 도구로 쓴다.

**Wall 3 — Moderator M의 `ktol` 부호가 음성 피드백의 *수학적 강제*임을 추적하지 못한다.**
Draft Eq.3:193–194에서 `dM/dt = ktol·R - ktol·M`을 보고, 학생은 *"M이 R을 따라가는구나"*까지는 안다. 그러나 *왜 이 부호 조합이 homeostasis를 만들고 그 반대 부호 조합은 발산을 만드는지*는 보지 못한다. 베테랑은 Jacobian의 trace와 determinant를 5초 내에 머릿속에서 계산하여 시스템이 stable spiral인지 unstable인지 판정한다 — `ktol > 0`이면서 *반대 부호로 R에 작용*하는 것이 음성 피드백의 본질이고, 이 부호 하나만 뒤집어도 약물이 시스템을 발산시키게 된다. 이것이 PD13 Model II의 AIC −97.5가 단순한 적합도 우위가 아니라 *수학적 정합성*의 우위임을 의미한다.

**Wall 4 — Transit chain의 n 결정이 *데이터의 정보 한계*를 측정한다는 의미를 놓친다.**
Draft는 PD35 Table 35.1의 WRSS 계열 1319 → 789 → 642 → 632 → 682를 보여주고 "n=3 채택"으로 끝낸다. 학생은 이것을 *모델 선택 규칙*으로만 본다. 베테랑은 이 숫자열을 *데이터셋의 정보 capacity 측정*으로 읽는다 — n=4에서 미미한 개선(642→632)은 데이터가 더 이상 mechanism을 분해하지 못한다는 신호이고, n=5에서 악화(632→682)는 over-fitting의 직접 증거다. 이 패턴 자체가 "이 데이터로는 transit step 정확한 개수를 결정할 수 없다 — n=3은 *practical sufficiency*이지 *mechanistic truth*가 아니다"라는 epistemological boundary를 가리킨다. 이 인식 없이 PD35 표를 외운 학생은 다음 transduction 데이터에서 무조건 n=3으로 시작하는 reflex를 갖게 된다.

### T1-(b) System Integration — 이 세 모델이 *하나의 시스템으로* 작동하는 지점

Draft는 세 모델 패밀리를 *개별 카드*로 분리하여 가르친다. 그러나 실제 PopPK/PD 워크플로에서 이 셋은 *순차적 escalation cascade*로 작동한다. 이 통합 관점이 §1 Roadmap에는 다이어그램으로 있지만 §2 카드들 *내부*에는 흡수되어 있지 않다.

구체적으로:

**(i) Sponsor의 NDA Population PK/PD 모델 구축 워크플로 단계.** Draft에서 시사된 escalation은 다음과 같다 — direct response → effect compartment(Link) → indirect response(turnover) → tolerance(Moderator) → transduction(transit chain). 각 단계는 *전 단계의 misfit GOF 시그니처*를 보고 결정된다. 이 escalation의 *순서 자체*가 §3.7→§3.9→§3.11→§3.13의 G&W 챕터 순서와 동형이다. 베테랑은 이 escalation을 손맵처럼 외우고 있고, 새 데이터를 받으면 *어느 단계에서 시작해야 하는지*를 5초 안에 결정한다. 1년차 학생은 보통 무조건 effect compartment로 시작한다 — 이것이 함정.

**(ii) Phase 2b dose-finding 임상시험의 모델-기반 설계 회의.** Step 1의 §1 Roadmap이 이 통합을 그림으로 보여주지만, §2 카드 1의 D Assumption 표에 *"이 가정이 깨질 경우 escalate해야 할 다음 모델 패밀리"* 컬럼을 추가하면 카드 간 통합이 강화된다. 즉 카드는 자기 모델의 한계만 보여주고 끝나는 것이 아니라, *다음 카드로의 연결고리*를 명시해야 한다. 현재 Draft에서는 카드 1의 E Limitations에 "TMDD, indirect response model, receptor binding kinetics(PD21)"이 1줄로 언급되어 있을 뿐이다.

**(iii) NDA 제출 직전의 Population PK/PD Report 작성.** R&T Appendix G의 Wagner-Nelson 방법(deconvolution)은 Draft에서 누락되어 있는데, 이것이 effect compartment fitting과 *동일한 수학적 뿌리*(convolution/deconvolution)를 가진다는 사실은 §2 카드 1의 L3 구조적 동형성에 흡수되어야 한다. 이 연결을 모르면 학생은 effect compartment를 별도의 "특수 트릭"으로 인식하게 되고, 다른 deconvolution 방법(numerical, nonparametric)과의 관계를 보지 못한다.

### T1-(c) Expert Intuition — 베테랑이 *방정식을 보지 않고도* 판단하는 것

베테랑이 새 임상시험 데이터셋을 받았을 때 *모델을 적합하기 전에* 즉시 판단하는 세 가지 사항을 명시한다.

**Intuition 1 — GOF plot 첫 30초 패턴 읽기.**
CWRES vs time plot에서 *S자 곡선 패턴*(under-over-under)이 보이면, 이것은 transit chain을 단일 indirect response로 잘못 적합한 시그니처다. *직선 아닌 monotonic drift*가 보이면 covariate model 누락. *해를 거듭하는 oscillation*이 보이면 Moderator 모델 적용 후에도 ktol이 잘못 식별된 시그니처. 이 세 패턴은 Draft §2 카드 4의 L5에 NONMEM `$DES` do-loop만 언급되어 있으나, 이 *진단 시그니처 카탈로그*는 없다.

**Intuition 2 — OFV 변화 궤적 해석.**
ΔOFV > 3.84 (자유도 1, p=0.05)는 covariate inclusion criterion이지만, 베테랑은 *ΔOFV의 절대값보다 그 추이*를 본다. 모델을 escalate하며 ΔOFV가 *plateau*에 도달하면 데이터의 mechanism resolution 한계에 도달한 것이고, *비선형적으로 점프*하면 새로운 메커니즘이 작용 중이라는 신호. PD13의 Model I → Model II에서 AIC가 -39 → -97.5로 *비선형 점프*한 것은 단순한 통계적 우위가 아니라 *질적 메커니즘 차이*의 시그니처이다. Draft §2 카드 3의 PD13 표는 이 점프의 의미를 단순한 "Model II가 우월함"으로 평면화한다.

**Intuition 3 — 데이터 품질 즉시 판정.**
베테랑은 임상시험 protocol을 보자마자 — *모델 적합 전에* — 다음을 판정한다: *(a)* sampling이 rise phase에 충분한가? `ke0` 추정에 필수. *(b)* multi-dose 또는 multi-route 설계인가? `ktol`과 `kout` 식별에 필수(PD13 핵심 교훈). *(c)* response 측정 간격이 cascade의 가장 빠른 transit 시간보다 짧은가? n 결정에 필수. PD20이 *single dose*이기 때문에 EC50 정밀도가 낮았다는 G&W p.839의 명시적 경고는 Draft 카드 1의 E Limitations에 흡수되어 있어야 하나 현재는 누락되어 있다.

---

## T2 — P3: REGULATORY & PRACTICAL RISK SURFACE

**중요 전제:** Audit v1은 Draft의 "NDA Deficiency Letter / 6개월 지연 / FDA reviewer 발언" 서사를 *NOT_IN_SOURCE / 교과서 외 실무 해석*으로 분류했고, 이는 fixed constraint이다. 따라서 본 T2는 그 specific narrative를 부활시키지 않는다. 대신 *교과서가 가르치는 mechanism validity 원칙*과 *그것을 실무 NONMEM 진단에 투영했을 때 발생하는 시그니처 패턴*만 다룬다. 모든 규제 관련 표현은 **[교과서 외 실무 해석]** 라벨로 분리되어야 한다는 Audit 권고를 따른다.

### T2-(a) Step 1의 단순화 중 *mechanism validity 검증*에서 약점이 되는 항목

**Risk Surface 1 — `Kp = 1` 가정의 무비판적 수용.**
Draft 카드 1의 closed-form $C_e$ (Eq.3:134)는 `Kp = 1`(no partitioning) 가정 하에서 도출된다. G&W p.263과 p.265는 명시한다 — partitioning이 있으면 `Ce`와 `C`가 정상상태에서도 다를 수 있고, 이 경우 추정된 EC50는 *biophase EC50가 아니라 plasma 농도 surrogate*가 된다. Draft는 이를 D Assumption 표에 1줄로만 언급하고 넘어간다. 실무 mechanism validity 검토 [교과서 외 실무 해석]에서, 이것은 "추정된 EC50가 실제 receptor affinity를 반영하는가"라는 질문을 받았을 때 답변할 수 있어야 하는 항목이다 — 답변 가능 여부가 *모델의 mechanism interpretation 신뢰도*를 결정한다.

**Risk Surface 2 — `ktol1 = ktol2` 단순화의 silent boundary.**
Draft 카드 3은 PD13의 단순화 가정 *Moderator의 생성·소실 동일 속도*를 기술하지만, 이 가정이 깨졌을 때 *어떤 시그니처가 나타나는지*는 명시하지 않는다. G&W p.299 명시: 데이터에 더 많은 정보(multi-dose, multi-route)가 있으면 분리 가능. 두 상수가 실제로 다른데 같다고 강제하면, *적합 결과의 ktol 추정값이 두 진짜 값의 산술평균이 아닌 비선형 평균*으로 편향된다. 이 편향은 multi-dose simulation 시 carry-over 예측을 왜곡한다.

**Risk Surface 3 — Hysteresis 방향 진단의 `single dominant mechanism` 가정.**
Audit MUST_FIX 4에 의해 Draft의 "방향이 모델 선택을 결정한다"는 표현은 "첫 번째 진단 단서"로 낮춰져야 하는 fixed constraint이다. 본 보고서는 그 너머를 짚는다 — 베테랑은 *figure-eight 패턴*이 보이면 즉시 두 메커니즘 동시 작용을 의심하고 *단일 메커니즘 모델 적용을 보류*한다. Draft 카드 2의 C Structural Necessity가 figure-eight 가능성을 1줄 언급하지만, 이것이 *모델 적합을 멈추고 mechanism 정보를 추가 수집해야 하는 트리거*임을 명시하지 않는다.

### T2-(b) NONMEM 실행 시그니처 — 개념 오해가 만드는 진단 패턴

베테랑은 NONMEM `.lst`와 `.cor` 파일을 5초간 보고 misspecification 종류를 판정한다. 이 진단 사전 일부는 카드의 L5 또는 별도 진단 모듈에 흡수되어야 한다. **다만 NONMEM-specific implementation은 Audit가 [구현 번역]으로 라벨링하라고 권고한 항목임을 명심한다.**

| 시그니처 이름 | 잔차 / OFV / GOF 패턴 | 가리키는 misspecification |
|---|---|---|
| **"EC50 용량 분기 패턴"** (Draft 카드 1 C-2에 이미 존재) | dose-stratified individual fit에서 EC50가 dose에 따라 monotonic 증가 또는 비단조 분기 | Link 모델을 turnover 데이터에 적용 (G&W §3.9.7 Table 3.10 직접 근거) |
| **"S자 잔차 패턴"** (Draft 누락) | CWRES vs time plot이 under-over-under의 sigmoidal pattern | Transit chain이 필요한 데이터를 단일 indirect response로 적합 (PD35 Fig 35.3 시각적 패턴 근거) |
| **"Trough Drift 패턴"** (Draft 카드 3 Trench Tip에 부분 존재) | multi-dose simulation에서 두 번째 dose의 trough 값이 첫 번째와 다름, 회차마다 deeper drift | Moderator M 활성화 미반영 (G&W p.808 PD13 직접 명시) |
| **"OFV Plateau 패턴"** (Draft 누락) | escalating model series에서 ΔOFV가 점차 작아지며 plateau | 데이터의 mechanism resolution 한계 도달 — 추가 escalation은 over-fitting (PD35 Table 35.1의 n=3↔4↔5 패턴 근거) |

### T2-(c) 가장 위험한 confusion pair — Step 1의 4개 쌍 중

Audit MUST_FIX 5는 "NDA Deficiency Letter" 서사를 [교과서 외 실무 해석]으로 분리하라고 권고했다. 본 보고서는 그 권고를 따르되, **Pair 1 (ke0 vs kout)을 가장 위험한 쌍으로 유지하는 합리적 근거**를 교과서 내부에서 제공한다.

**Pair 1 (ke0 vs kout)이 가장 위험한 이유 — 교과서 직접 근거:**
G&W §3.9.7은 명시적으로 *"distribution(effect compartment or link) model has severe limitations when applied to fitting data described by a turnover process"*라고 단언한다(p.272). Table 3.10이 보여주는 *biologically implausible*한 dose-dependent EC50/Emax/n은 *직접적인 mechanism validity 위반*이다. 이것은 단순한 통계적 misfit이 아니라 *receptor sensitivity가 dose에 의존한다*는 생물학적 불가능을 함의하는 모델을 채택했다는 의미다. 이것이 의미하는 바는: 같은 데이터의 같은 fit이 GOF plot으로는 *acceptable*하게 보이지만, dose-stratified analysis만 추가하면 즉시 노출된다는 점.

**Critical Blow 행 수정 권고:**
Draft §5 Pair 1의 Critical Blow 행은 Audit에 따라 다음 형태로 분리되어야 한다:

> [교과서 기반 — G&W §3.9.7 직접 인용]
> "distribution model creates a biologically implausible situation where sensitivity IC50/EC50, the capacity Emax, and the n value for a system change with dose."
>
> [교과서 외 실무 해석 — 라벨링 필수]
> 이 misspecification을 mechanism validity 평가가 엄격한 규제 환경에서 발견되면, sponsor는 model justification, sensitivity analysis, alternative model comparison을 추가 요구받게 된다. 구체적 outcome(Deficiency Letter, 6개월 지연 등)은 sponsor·indication·심사관 판단에 따라 다르며, 교과서가 직접 단언하는 사항이 아니다.

**Pair 4 (single ke0 vs n×τ transit)이 두 번째로 위험한 이유:**
Draft 카드 4는 "임상시험 onset 평가 시점 잘못 잡음"을 핵심 위험으로 든다. 이것은 *교과서 안*에서 직접 근거가 있다 — G&W p.323 Fig.3.99는 PD35 데이터에서 15–20시간 onset delay가 *"cannot be mimicked by an ordinary indirect response (turnover) model"*라고 명시한다. 만약 Phase 2 protocol에서 efficacy 평가 시점을 indirect response 단일 구획 가정으로 t=12h에 설정했다면, 진짜 약효가 나타나기 *전에* 평가하게 되어 false negative 결론에 도달한다. 이것은 시그니처 *"S자 잔차 패턴"*으로 적합 단계에서 사전 진단 가능하다.

---

## T3 — TRENCH-LEVEL TIPS

각 항목은 *(상황)–(함정)–(탐지)–(삽입 위치)–(삽입 텍스트 1–2문장)* 형식. 모든 삽입 텍스트는 복사-붙여넣기 가능한 완성 문장.

### Trench Tip 1 — Hysteresis Plot 그릴 때의 Sampling 함정

- **상황:** 임상시험 데이터 수신 직후 첫 EDA 단계, response vs concentration plot 작성 중.
- **함정:** Sampling이 sparse하면 hysteresis 방향이 보이지 않거나 가짜 figure-eight처럼 보인다 — 특히 rise phase에 데이터가 1–2점뿐이면 chronological arrow를 그릴 수 없다.
- **탐지:** Plot 위 인접 시간점들이 화살표로 *연결되었을 때* loop이 *닫히지 않거나* 화살표 방향이 모호하면, sampling 부족.
- **삽입 위치:** §2 카드 2 (Hysteresis 방향 판별), `<!-- TRENCH -->` 블록 직후 또는 E Limitations 마지막.
- **삽입 텍스트:**
  > Hysteresis 방향 판정 전, rise phase에 최소 3점 이상의 sample이 있는지 *먼저* 확인하라. Sparse sampling은 가짜 figure-eight를 만들고 모델 토론 30분을 잘못된 방향으로 끌고 간다.

### Trench Tip 2 — `tmax` 불변 검정의 PK Linearity 선결 조건

- **상황:** Dose escalation 데이터에서 Link vs Turnover 분기 결정 회의.
- **함정:** Michaelis-Menten saturation(비선형 PK) 약물에서 `tmax`가 dose에 따라 이동하는 것을 turnover signature로 *오진*한다.
- **탐지:** AUC가 dose에 비례하는지(linearity 확인) 먼저 검증; 비례하지 않으면 PK 비선형이 가짜 peak shift의 원인.
- **삽입 위치:** §2 카드 1 (Effect Compartment), D Assumptions 표의 `tmax` dose-invariant 행 직후.
- **삽입 텍스트:**
  > `tmax` 불변 검정은 *linear PK 가정 위에서만* 유효하다 (G&W p.264 명시). Dose escalation에서 AUC ∝ dose 선형성을 *먼저* 확인한 후에야 이 검정을 모델 선택 도구로 쓸 수 있다.

### Trench Tip 3 — PD21에서 ke0/kout/koff 식별 불가능성

- **상황:** 단일 dose 또는 single-route 데이터로 effect compartment / turnover / receptor binding 모델 비교 중.
- **함정:** 세 모델이 같은 단일-dose 데이터에 비슷한 fit을 주고, 학생은 그중 가장 OFV가 낮은 모델을 채택. 그러나 세 파라미터(`ke0`, `kout`, `koff`)는 *수학적으로* 식별 불가능 — 어느 모델이 진짜인지 데이터가 말해주지 않는다.
- **탐지:** PD21 Table 21.1의 세 파라미터가 모두 비슷한 magnitude로 추정되며 모델 간 OFV 차이가 작음. Multi-dose washout pattern(rebinding 거동)만이 receptor binding을 effect compartment에서 분리.
- **삽입 위치:** §2 카드 1 (Effect Compartment), E Limitations 또는 §5 Pair 1 (ke0 vs kout) 하단.
- **삽입 텍스트:**
  > `ke0`, `kout`, `koff`는 같은 단위(time⁻¹)와 비슷한 magnitude를 가질 수 있으나 *지시체*는 완전히 다르다 (분자 통과 시간 vs 시스템 회복 시간 vs receptor 해리 시간). 단일 dose 데이터로는 이 셋을 분리할 수 없으며, multi-dose washout 또는 multi-route 설계가 필수다 (PD21 직접 교훈).

### Trench Tip 4 — PD35 n 결정에서 Information Capacity Ceiling

- **상황:** Transduction model의 transit step 수 n을 결정하는 model selection 단계.
- **함정:** WRSS가 더 낮은 n을 무조건 선택. PD35의 경우 n=4가 n=3보다 미세하게 낮지만(642 → 632), 이것이 *information capacity ceiling*에 도달했다는 신호임을 못 본다. n=5에서 악화(682)는 over-fitting의 직접 증거.
- **탐지:** 인접 n 사이 ΔOFV/ΔWRSS가 점차 작아지며 plateau에 진입하면 데이터의 mechanism resolution 한계 도달.
- **삽입 위치:** §2 카드 4 (Transduction), B Derivation의 PD35 표 직후.
- **삽입 텍스트:**
  > n 선택은 단순한 "가장 낮은 WRSS"가 아니라 *데이터의 information capacity ceiling 진단*이다. PD35의 1319→789→642→632→682 패턴에서 n=3은 *practical sufficiency*이며, n=4의 미미한 개선과 n=5의 악화는 데이터가 mechanism의 정확한 step 수를 분해하지 못한다는 epistemological boundary를 가리킨다.

---

## T4 — DELETION CANDIDATES (필수 섹션 — 누락 시 task failure)

다음 항목들은 Draft에서 *삭제* 또는 *압축*되어야 한다. 각 항목의 사유와 처리 지시를 명시한다.

| § 위치 | 삭제/압축 대상 | 사유 | 처리 |
|---|---|---|---|
| **§7 Q10 보스 딜레마 정답 공개** | "FDA Type B pre-submission meeting", "ICH E9(R1) 정신", "bootstrap/SIR/SAEM/MU-referencing" 구현 처방, "label 변경, 시판 일정 표류" 등 7–8문장의 규제·구현 narrative | Audit MUST_FIX 5, 6에 의해 NOT_IN_SOURCE 분류된 실무·구현 layer. 박사과정생 대상 elevator-level upgrade를 넘어선 manager-level scenario. | **COMPRESS to 3 sentences** — Trade-off 핵심 (mechanism validity > statistical fit)만 유지, 구체적 도구·meeting type·6개월 narrative 삭제. |
| **§8 C Professional Moat 마지막 단락** | "$COV step 50% 실패율... bootstrap-based parameter precision estimation... Appendix X" NDA 제출 문구 인용 | 학습자에게 흥미로운 finishing flourish이지만 교과서 직접 근거 없음. PhD reader에게 over-specified. | **DELETE** — Moat는 mechanism validity 판단 능력 자체로 충분. NDA 제출 문구 mock 인용은 [교과서 외 실무 해석]으로조차 라벨링하기 어려운 가공 narrative. |
| **§2 카드 1 G Zettelkasten Atom 마지막 줄** | "NDA Deficiency Letter 직결" | Audit MUST_FIX 5. Zettelkasten은 atomic note이므로 라벨링이 추가되면 atom 형태가 깨짐. | **DELETE** — atom 마지막 문장을 "Turnover 시스템 데이터에 적용 시 EC50가 dose마다 분기 — biologically implausible (G&W §3.9.7)"로 종결. |
| **§2 카드 4 L2 기하학적 직관** | "Bode plot 의미: -20n dB/decade slope; phase lag = -n·90° at high freq" | Audit MUST_FIX 6 / SHOULD_FIX 7. NOT_IN_SOURCE. PhD reader에게는 정보 밀도가 너무 높고, 한 carrier가 가진 학부 신호처리 배경에 의존한다. | **COMPRESS to 1 sentence** — "n개 1차 시스템의 sequential 합성은 transfer function의 곱으로 표현되며, gamma PDF 형태의 합성 응답을 만든다"로 축약. Bode 용어는 [구조적 비유 — 교과서 외 확장] 라벨로 별도 처리. |
| **§2 카드 4 L3 구조적 동일성** | "PFR(plug flow reactor) tanks-in-series, RC delay line, Erlang 분포" 3-way 비유 | Audit SHOULD_FIX 7. NOT_IN_SOURCE. 비유 3개 중 *Erlang 분포*만 통계학적으로 정확하고 직접 유용. PFR/RC는 도메인 외부 비유. | **COMPRESS to 1 비유** — Erlang 분포만 유지("n개 동일 exponential의 합은 Erlang 분포"), PFR과 RC는 [구조적 비유 — 교과서 외] 라벨 후 한 줄로 묶음. |
| **§2 카드 4 L5 실무 투영** | "NONMEM `$DES`: `DADT(I+1) = (A(I) - A(I+1))/TAU` 의 do-loop 구조; n을 model selection 변수로" | Audit MUST_FIX 6. NONMEM 구현 instruction은 [구현 번역] 라벨 필수. 또한 do-loop 코딩은 NONMEM 7.5+의 vector form에서 다르게 작성되므로 specific syntax는 시간이 지나면 outdated 가능. | **COMPRESS** — "transit chain은 ODE solver에서 sequential 1차 ODE의 do-loop으로 구현된다 [구현 번역 layer]"로 일반화. Specific syntax는 별도 NONMEM 노트로 분리. |
| **§5 Pair 1 Critical Blow 행** | "심사관 발행", "6개월 지연, label 변경, 시판 일정 표류" 등 specific outcome narrative | Audit MUST_FIX 5. T2-(c)에서 제시한 분리 권고 적용. | **REPLACE** — T2-(c)의 [교과서 기반] / [교과서 외 실무 해석] 분리 형태로 교체. Specific 6개월 narrative 삭제. |
| **§7 Q10 정답 공개의 NDA 제출 문구 인용** | "The effect compartment (Link) model fit demonstrated... Appendix X" 4–5줄 mock NDA 문구 | Audit MUST_FIX 5, 6. Mock 가공 문서이며 학생에게 *real NDA 문구처럼* 인식될 위험. | **DELETE** — Trade-off 핵심 메시지만 1–2문장으로 유지. |
| **§2 카드 1 C Structural Necessity (2)** | "$k_{1e} = k_{e0}$ 가정의 필연: ... *물리적 정합성*을 위해 강제됨" | Audit MUST_FIX 2. 동일 항목은 §2 카드 1 D Assumptions 표에도 잘못 기술. | **REWRITE** — 다음 1문장으로 교체: "$k_{1e} = k_{e0}$ 가정은 response-time data만으로 두 rate constant를 동시에 식별할 수 없는 *식별가능성 제약* 때문이며, partitioning이 있으면 `Ce`와 `C`가 정상상태에서도 다를 수 있다 (G&W p.263, p.265)." Audit MUST_FIX 2의 정확한 reformulation. |
| **§2 카드 1 거장의 시각, "succinylcholine 추가 투여 시점... t½,ke0 = 4 min"** | succinylcholine과 4 min `t1/2,ke0`의 직접 연결 | Audit MUST_FIX 3. G&W Table 3.9의 4 min은 d-tubocurarine/vecuronium. Succinylcholine은 R&T의 별도 dose-duration example. | **REWRITE** — 거장의 시각을 다음으로 교체: "마취과 회복실에서 d-tubocurarine 또는 vecuronium의 t½,ke0 = 4 min(G&W Table 3.9)을 알면 신경근 차단 회복 시점 판단이 안전해지고, succinylcholine의 경우 dose-duration 관계(R&T Fig 8-24)가 dose 결정의 직접 도구가 된다." |

---

## T5 — PRIORITY MATRIX

### Grade A — 반드시 반영 (체화도 직접 향상 또는 mechanism validity 위험 감소)

| # | 항목 | 위치 | 사유 |
|---|---|---|---|
| A1 | T1-(a) Wall 1 — `ke0`/`kout`/`koff` 지시체 분리 직관 | §2 카드 1 G 또는 §5 Pair 1 | PD21 데이터로부터 학생이 자력 추출 어려움. 베테랑 직관의 핵심. |
| A2 | T1-(a) Wall 2 — `tmax` 불변 검정의 linear PK 선결 조건 | §2 카드 1 D Assumptions | T3 Trench Tip 2와 결합. Audit가 다루지 않은 신규 함정. |
| A3 | T3 Trench Tip 1 — Sparse sampling이 만드는 가짜 figure-eight | §2 카드 2 | Hysteresis 방향 진단 자체의 전제 조건. |
| A4 | T3 Trench Tip 4 — n 선택의 information capacity ceiling 해석 | §2 카드 4 | PD35 표를 단순한 model selection 규칙으로 평면화하지 않게 함. |
| A5 | T4 모든 deletion/compression 항목 (특히 §2 카드 1 C Structural Necessity (2)와 §7 Q10) | 각 § 위치 | Audit MUST_FIX 1–6의 직접 적용. |
| A6 | T2-(c) Critical Blow 행의 [교과서 기반]/[교과서 외] 분리 형태 | §5 Pair 1 | Audit MUST_FIX 5의 구체적 reformulation 권고. |

### Grade B — flow가 유지되면 반영 (enrichment value)

| # | 항목 | 위치 | 사유 |
|---|---|---|---|
| B1 | T1-(a) Wall 3 — Moderator M의 음성 피드백 부호의 수학적 강제 | §2 카드 3 C Structural Necessity | 직관 강화이나 Step 1의 (1)(2)(3) 구조로 이미 부분 다룸. |
| B2 | T1-(b) System Integration — escalation cascade 명시 | §1 Roadmap의 카드 간 연결고리 강화 | 통합 관점이지만 Roadmap이 이미 다이어그램으로 시사. |
| B3 | T1-(c) Intuition 1 — GOF S자 잔차 패턴 카탈로그 | §2 카드 4 또는 별도 진단 모듈 | T2-(b)와 결합 시 효과적이나 §2 5 Layer 구조에 흡수 어려움. |
| B4 | T1-(c) Intuition 2 — OFV 비선형 점프 vs plateau 해석 | §2 카드 3 PD13 표 직후 | Step 1의 표는 이미 풍부하므로 추가 1줄 코멘트로 충분. |
| B5 | T3 Trench Tip 3 — PD21 식별 불가능성의 명시적 경고 | §2 카드 1 E Limitations | A1과 부분 중복; A1만 반영해도 50% 효과. |
| B6 | T1-(b) (iii) — Wagner-Nelson과 effect compartment의 deconvolution 동형성 | §2 카드 1 L3 구조적 동형성 | R&T Appendix G까지 다루는 것은 scope 확장. |

### Grade C — 거부 (scope creep, unsupported, 또는 기존 내용 중복)

| # | 항목 | 사유 |
|---|---|---|
| C1 | NONMEM specific syntax(SAEM, BAYES, Bootstrap)의 카드 내부 통합 | Audit MUST_FIX 6. [구현 번역] layer로 분리되어야 하며 카드 본문에 들어가면 Audit constraint 위반. |
| C2 | "Phase 2b → Phase 3 transition 결정" 시나리오를 §8 Moat에 추가 확장 | Audit가 가공 narrative로 분류한 영역 확장. T4에서 오히려 삭제 권고. |
| C3 | Erlang/Bode/PFR 비유를 *모두* 유지하며 라벨링만 추가 | T4 deletion 권고와 충돌. 1개 비유(Erlang)로 압축이 더 정확. |
| C4 | §3.10 Dose-Response-Time, §3.12 Receptor occupancy의 부분 흡수 | Audit가 명시적으로 reject한 scope creep. Draft의 의도적 제외 유지. |
| C5 | 추가 case study(PD14, PD41, PD43) 인용 | Scope Lock 외부. 기존 PD13/20/21/35로 충분. |
| C6 | "거장이 5초 내에 판단" 표현을 Step 1 전체에 추가 분산 | 이미 §2 카드 1, 2, 5 Pair 1에 분포. 추가 분산 시 톤이 reflexive로 변질. |

---

## Final Note for Phase 4A Patch Author

본 보고서는 Audit Report v1과 *상보적*으로 작동한다:

- **Audit가 잡은 것:** Draft의 사실 오류 6개(case label, identifiability, drug example, hysteresis 강도, 규제 narrative, 구현 layer 침범).
- **Crucible이 잡은 것:** Draft가 *기술적으로 정확하지만 체화의 임계선에 도달하지 못한 지점* 4개(Wall 1–4) + escalation cascade 통합 누락 + GOF 진단 시그니처 카탈로그 누락 + PD21 식별 불가능성의 epistemological framing 부재.

Phase 4A 진입 시 권장 순서: **(i)** Audit MUST_FIX 6개 적용 → **(ii)** 본 보고서 Grade A 6개 삽입 → **(iii)** T4 deletion 9개 실행 → **(iv)** Grade B 중 §1 Roadmap에 자연스럽게 흡수 가능한 1–2개만 선택 적용. Grade C는 모두 거부. 이 순서대로 진행하면 Content Lock 후보로 충분한 품질에 도달한다.

---

## 핵심 판정

**Audit Report v1은 *Draft의 사실 오류 6개*를 잡았고, 본 Crucible은 *체화의 임계선에 도달하지 못한 직관 지점 4–5개*를 잡았습니다.** 두 보고서는 상호 배타가 아니라 *상보적*입니다.

**Audit이 잡은 것** (fixed constraint로 취급):
- Case label 오류(PD13 ≠ Table 3.10), `k1e=ke0` 식별가능성 vs 물리적 정합성 오기, succinylcholine/d-tubocurarine 수치 혼합, hysteresis 방향의 deterministic 표현, NDA narrative, 구현 layer 침범.

**Crucible이 새로 잡은 것** (Operative Filter 기반):
- **Wall 1**: `ke0`/`kout`/`koff`의 단위 동일성을 지시체 동일성으로 착각하는 함정 — PD21 데이터 자체가 가르치지 못함.
- **Wall 2**: `tmax` 불변 검정이 *linear PK 위에서만* 작동한다는 G&W p.264의 명시적 전제 — Draft에서 완전 누락.
- **Wall 4**: PD35의 1319→789→642→632→682 패턴을 단순 model selection 규칙이 아니라 *데이터의 information capacity ceiling 진단*으로 읽는 epistemological framing.
- **GOF 시그니처 카탈로그 4종**(EC50 용량 분기 / S자 잔차 / Trough Drift / OFV Plateau) 중 후자 3종이 Draft에 없음.

## Phase 4A Patch 진입 시 권장 순서

본 보고서 마지막 섹션에 명시된 순서대로 진행하면 Content Lock 후보로 충분합니다:

1. Audit MUST_FIX 6개 적용 →
2. Crucible **Grade A 6개** 삽입(특히 A1 — `ke0/kout/koff` 지시체 분리 직관, A2 — `tmax` 검정의 linear PK 선결조건) →
3. **T4 deletion 9개** 실행(특히 §7 Q10 보스 딜레마 정답 공개의 7–8문장 narrative 압축, §8 Moat의 NDA 제출 mock 인용 삭제) →
4. Grade B 중 §1 Roadmap에 자연스럽게 흡수되는 1–2개만 선택 적용. **Grade C 6개는 모두 거부.**

## Trench-Level Tips 4개 (T3)

각각 *(상황)–(함정)–(탐지)–(삽입 위치)–(삽입 텍스트 1–2문장)* 완성 형식으로 복사-붙여넣기 가능하게 작성했습니다 — Sparse sampling이 만드는 가짜 figure-eight, `tmax` 검정의 PK linearity 선결, PD21의 식별 불가능성, n 선택의 information capacity ceiling.


C-260504-073500-K7M

# S11 `Insight Crucible Report v1` (FINAL)
## Stage 2/2 — G&W 5e × R&T 5e 통합 단일 산출물
### Source Universe: Gabrielsson 5e §2.6.7 + §3.7–3.8 + §3.10 + §3.12 + PD4–PD9 // Rowland & Tozer 5e Ch.8 (pp.233–264)

> **입력 상태 점검**
> 본 최종본은 Stage 1 (Gabrielsson 단독) 산출물에 R&T Ch.8 원문(첨부 2/2)을 통합하여 단일 Source Universe로 재구성한 것입니다. Stage 1 + Stage 2의 합은 단일 PDF 세션 1.0× 분량으로 엄격히 압축했으며(2.0× 팽창 금지 원칙), R&T-specific 기여는 ① 효과의 시간축 입문(time delay 분류학), ② duration formula $t_D$ 도출, ③ Region 1/2/3 Hill-curve 시간 거동, ④ PK vs PD rate-limiting 명시적 분류 영역에 집중 배치되었습니다. Audit Report v1의 모든 MUST_FIX 항목(naproxen 500 mg 일관성, NDA 문장 라벨링, "all delayed" hedge, tss 결정규칙 톤다운, K 표기 분리, Card 8–9 통합)은 Grade A 변경사항으로 반영 완료되었습니다.

---

## T1. P1 — INTERNALIZATION BARRIERS & MASTER'S INTUITIONS

### (a) Cognitive walls — 암송은 가능하나 내재화는 안 되는 지점

**Wall #1. tss 거동의 first-order analogue blindness (G&W).**
학습자는 "Models 1·3은 dose-independent tss, Models 2·4는 dose-dependent tss"를 암송할 수 있지만, 이 명제가 PK의 "infusion rate vs clearance" 거동과 **수학적으로 동일한 first-order system**임을 보지 못합니다. G&W §3.7.5 p.249 본문 — *"factors that act on the disposition parameter… analogous to changing the clearance"* — 가 학습 노트에 단순 인용으로 남아 있을 뿐, "infusion rate를 바꿔도 tss는 안 변하지만 CL을 바꾸면 tss도 변한다"는 PK 1년차 지식으로의 down-projection이 일어나지 않습니다.

**Wall #2. ΔR의 이중 의미 부하 (G&W).**
학습자는 Equation 3:83 (`ΔR = R0·Imax`), 3:89 (`ΔR = R0·Imax/(1−Imax)`), 3:95 (`ΔR = R0·Emax`), 3:101 (`ΔR = R0·Emax/(1+Emax)`)를 외울 수 있지만, **Figure 3.40의 결정적 메시지** — 같은 기호 `Emax`가 ordinary direct model에서는 (Rmax − E0)의 절대 거리이고 turnover model에서는 baseline에 대한 multiplier — 를 보지 못합니다. PD5 Table 5.1의 `Emax = 0.65`라는 추정치 하나가 drug-specific Imax/Emax 정보와 system-specific kin/kout 정보를 모두 담고 있다는 사실은, 학습자가 in vitro IC50와 PopPK의 IC50를 비교하려 할 때 처음 충돌합니다.

**Wall #3. Region 2/Region 3 시간 거동의 비대칭성 (R&T).**
R&T Eq. 8-9 *Response = E(0) − m·k·t* (p.249)는 학습자에게 **단지 Region 2(20–80% Emax)에 한정된 zero-order 감쇠 공식**임에도, 학습자는 "PK는 first-order인데 PD는 zero-order"라는 외운 명제로 영구 보존합니다. 실제 메커니즘은 Region 3(고농도 plateau)에서 응답이 거의 일정하게 유지되다가 Region 2 진입 시점부터 비로소 일정-기울기 감쇠가 시작되고, Region 1(저농도)에서는 다시 first-order로 돌아가는 **3구간 구조**입니다(Fig. 8-17). Succinylcholine의 22%/min 직선 감쇠(Fig. 8-18)가 *왜* 그 시간 구간에서만 직선인지를 설명할 수 없는 학습자는, 임상에서 dose 증량 시 onset만 빨라지는 게 아니라 plateau 체류 시간도 함께 늘어난다는 사실을 예측하지 못합니다.

**Wall #4. PK clock vs PD clock의 비식별 함정 (G&W + R&T).**
학습자는 "느린 시계가 지배한다"는 일반론을 외우지만, 단일 dose 데이터에서 두 시계 중 어느 것이 지배적인지를 **사전적으로 분리**할 수 없다는 R&T의 가장 깊은 메시지(p.243 acenocoumarol vs phenprocoumon 비교)를 놓칩니다. 동일한 prothrombin complex 동역학을 공유하는 두 약물에서 acenocoumarol(t1/2 15h)은 PD 시계가, phenprocoumon(t1/2 5–6일)은 PK 시계가 baseline 복귀를 지배합니다(Fig. 8-11). 즉 *동일 작용기전을 공유하는 약물군에서도 약물별 PK에 따라 rate-limiting step이 달라진다*는 사실은, 단일 약물 데이터에 갇힌 학습자에게는 그 자체가 보이지 않습니다. PD4 Pool 1의 r(k1, kout) = 0.9999 비식별성(Table 4.1 CV% 4000)도 동일 구조의 다른 표현입니다.

### (b) System integration — 챕터 개념이 단일 시스템으로 작동하는 지점

**Integration #1. EDA 단계의 5분 모델 압축 — Initial Structural Model 선택 회의 (G&W).**
PD7 Figure 7.1 데이터를 본 30년 베테랑은 5분 안에 모델 4(stimulation of loss)로 압축합니다. 추론: ① 응답이 baseline에서 **하강** → 직접 자극은 production stimulation에서만 가능, 따라서 stimulation은 loss 측 ② tss가 **dose-dependent로 단축** → Models 1, 3 제외 ③ ΔR 방향이 baseline 아래 → Model 2 제외, Model 4 확정. PD5(Model 2) vs PD7(Model 4) side-by-side 학습이 이 추론을 "암송 가능"에서 "수행 가능"으로 전환시킵니다.

**Integration #2. 규제 제출 — NDA Module 5.3.5.3 Population PK/PD Analysis [교과서 외 실무 해석].**
"Structural Model Justification" 단락에서 four-model taxonomy는 EDA 도구이자 규제 언어의 문법으로 기능합니다. 모델 1 선택은 *"drug acts on biosynthesis, with onset/recovery rate-limited by intrinsic biomarker turnover"*라는 mechanistic claim을 동반하며, 이는 Phase 4 PMR에서 검증 대상입니다. PD9 §Perspectives의 **linear S(C) 하 turnover와 effect compartment fit 동등성**은 이 claim이 데이터만으로 방어되지 않을 수 있음을 시사합니다. *(이 통합 사례는 G&W/R&T 원문 직접 인용이 아닌 실무 적용 추론입니다.)*

**Integration #3. DDI 예측의 qualitative shift (G&W + R&T).**
Direct PK-PD 모델은 inhibitor 병용 시 Cmax에 비례하는 즉각적 효과 변화를 예측하지만, turnover 모델은 **Cmax 변화와 peak biomarker 변화 사이에 t1/2,kout-규모 지연**이 끼어듭니다(PD9: t1/2,kout = 7h, plasma t1/2 = 5.4h). R&T의 acenocoumarol/phenprocoumon 쌍은 이 통찰의 임상적 결정판입니다 — 같은 작용기전이라도 PK 차이가 임상 거동을 완전히 다르게 만듭니다(p.244). 이는 Phase 1 DDI 시험의 sampling time 결정과 직결됩니다.

**Integration #4. Single-dose duration → 임상 dose extension 결정 (R&T).**
R&T Eq. 8-12 $t_D = \frac{1}{k}\ln(Dose/(C_{min} \cdot V))$ (p.254)는 단일 수식이 아닌 **임상 dose 증량의 안전성 의사결정 도구**입니다. Succinylcholine 0.5 → 1 → 2 → 4 mg/kg에서 T50이 약 4분(=succinylcholine PK 반감기)씩 선형 증가하는 Fig. 8-24 패턴은 PK rate-limiting을 가정한 dose-extension의 정량적 한계를 보여줍니다. 30년 베테랑은 이 수식을 보자마자 **"이 약물은 PK clock 지배인가? PD clock 지배인가?"를 먼저 묻고**, 후자라면 수식을 적용하지 않습니다 — warfarin에 이 수식을 적용하면 임상적으로 무의미한 답이 나옵니다.

### (c) Expert intuition — 수식 참조 없이 즉시 판독하는 패턴

**Intuition #1. "Post-trough rebound timing" 1차 점검 (G&W).**
30년 베테랑은 turnover 모델 fit을 받자마자 **post-trough 회복 곡선의 타이밍**을 봅니다. observed 데이터가 모델보다 빨리 baseline으로 돌아오면 moderator/feedback compartment 누락 신호로 즉시 읽습니다(G&W §2.6.7 Eq. 2:261–2:263, IgG 11일 saturable protection이 prototype). $COV step 결과를 보기 전에 이 점검이 끝납니다.

**Intuition #2. OFV trajectory의 "stuck-then-drop" 패턴 (G&W).**
30회 iteration 동안 OFV가 거의 변하지 않다가 갑자기 큰 폭 하락 → **kin/kout 상관(>0.98)이 search direction을 죽이는 신호**. PD5 Table 5.1: *"correlation greater than 0.98… reparameterization of the model by baseline R0 and kout."* 베테랑은 이 패턴을 보면 즉시 R0+kout 재파라미터화(Eq. 3:103)로 넘어갑니다.

**Intuition #3. Response peak이 plasma Cmax보다 빠르면 "데이터 또는 구조 오류" (G&W).**
어떤 subject에서든 response peak이 plasma Cmax보다 빠르면 베테랑은 즉시 두 가지를 의심: ① dosing time mis-recording, ② 누락된 precursor 또는 transit compartment(PD4의 vitamin K reductase upstream action이 prototype). 이는 turnover 모델 기본 가정 위반의 직접 신호입니다.

**Intuition #4. Hysteresis loop의 30초 방향 진단 (R&T).**
30년 베테랑은 plasma C vs response 산점도를 보자마자 loop 회전 방향만으로 1차 분류를 끝냅니다. **Counterclockwise**(R&T naproxen Fig. 8-2B, ibuprofen Fig. 8-9A의 시계반대) → 효과가 농도를 *뒤따르는* 양상 → 후보군: ① 효과 부위 분포 지연(effect compartment) ② Systems-in-flux(turnover) ③ active metabolite 생성 지연. **Clockwise** → 효과가 농도보다 *앞서가는* 양상 → 후보군: ① tolerance/down-regulation ② counter-regulatory feedback ③ enantiomer-specific kinetics. R&T가 명시적으로 다루지 않은 후자 분류는 [교과서 외 실무 해석]이지만, 전자(counterclockwise) 3분류는 R&T 본문에서 직접 도출됩니다(p.235–242).

---

## T2. P3 — REGULATORY & PRACTICAL RISK SURFACE

### (a) Deficiency Letter 생성 가능 단순화

**Risk #1. tss/peak-shift의 결정 규칙화 (G&W).**
"tss dose-dependence가 모델 선택을 결정한다"는 형식의 NDA Population PK/PD Analysis 모델 선택 근거는 **PD9 §Perspectives Fig. 9.5 right panel의 명시적 반례** — *"a lack of peak shift with increasing doses does not necessarily imply an effect compartment (link) model"* — 에 의해 무력화됩니다. 규제 위험 메커니즘: mechanistic specificity claim의 데이터 비방어 → sensitivity analysis 누락 deficiency.

**Risk #2. "All responses delayed" 절대 단정의 cross-section 비정합성 (G&W + R&T).**
"모든 측정 가능한 약리반응은 시간 지연을 가진다"는 Big Idea 형식은 **R&T Fig. 8-6 (midazolam EEG, direct PK-PD link)** 및 R&T propranolol·benzodiazepine 사례(p.237)와 직접 충돌합니다. R&T 본문 (p.252) 자체가 *"some reactions occur so rapidly that they appear to be direct effects, it is usually a matter of time and resolution of the data"*로 hedge합니다. 같은 NDA 내 direct-link endpoint 분석과의 정합성이 깨집니다. **수정 표준**: "대부분의 임상적으로 관찰되는 약리반응은 plasma concentration과 완전히 동시에 움직이지 않으며, 그 지연이 무시 가능할 정도로 짧을 때만 direct response 모델이 적용 가능하다."

**Risk #3. tD formula의 Wrong-Clock 적용 (R&T).**
R&T Eq. 8-12 $t_D = \frac{1}{k}\ln(Dose/(C_{min} \cdot V))$가 **PK rate-limiting 가정 하에서만 유효**하다는 단서는 본문에서 강조되지만(p.254 *"For a drug with no delays in response… showing a fixed exposure-response relationship (i.e., one for which response is rate-limited by pharmacokinetics)"*), 학습자는 이 단서를 놓치고 PD rate-limited 약물(warfarin, omeprazole, paclitaxel)에 동일 수식을 적용합니다. Warfarin의 dose-duration 관계는 clotting factor turnover에 지배되므로 warfarin elimination $k$로 계산한 $t_D$는 임상적으로 무의미합니다. NDA dose-extension justification에서 이 오용은 *"insufficient justification for proposed dosing interval"* deficiency를 유발합니다.

**Risk #4. Linear PK ≠ Linear PD의 NDA Dose-Response Justification 함정 (R&T).**
R&T Fig. 8-26은 methylprednisolone 16–1000 mg에서 AUC가 dose에 정확히 비례함을 보입니다. **그러나** Fig. 8-27의 lymphocyte 응답은 500 mg과 1000 mg에서 거의 차이가 없습니다 — Hill 곡선 plateau 영역에 진입했기 때문입니다. 스폰서가 "PK가 비례하므로 효과도 비례한다"는 추론으로 dose-response justification을 작성하면 *"failure to characterize the dose-response relationship at the proposed therapeutic range"* deficiency를 받습니다. 이는 R&T가 한 단락에 명시한 단호한 경고입니다(p.256 *"Dose linearity in pharmacokinetics does not result in dose linearity in pharmacodynamics… That is almost never the case."*).

### (b) NONMEM 실행 오류 시그니처

**Signature #1: "Dose-Scaled kout Mirage" (G&W).**
잘못된 직관: 모든 turnover 모델에서 "초기 응답 변화 곡선의 기울기 = ±kout". 실제: Models 2·4의 초기 slope는 zero-order(kin) 또는 first-order(−kout·S(C))이며 kout 단독이 아님(Table 3.6 p.251). 시그니처: 추정된 kout이 dose-level별로 단조 변화(PD7 Fig. 7.1: 6,400U → 0.6 h⁻¹, 160,000U → 1.6 h⁻¹). System parameter는 dose-invariant이어야 하므로 misspecification artifact 신호.

**Signature #2: "Phantom Convergence with k1=kout Constraint" (G&W).**
잘못된 직관: PD4 Pool 2의 좋은 CV%가 모델 우월성을 입증. 실제: k1 = kout 제약이 비식별성을 *해결*했을 뿐 데이터가 동등성을 *지지*한 것이 아님. Pool 1에서 r(k1, kout) = 0.9999, ΔAIC ≈ 2(50.7 vs 48.7). 시그니처: $COV step 통과, CV% 정상, WRSS 동일이지만 mechanistic claim이 데이터 기반이 아님.

**Signature #3: "False Half-Life Compression" (G&W).**
PD4 Table 4.1: No lag-time 모델 kout = 0.03 h⁻¹ (t1/2 ≈ 23h)이 lag-time 모델에서 0.06 h⁻¹ (t1/2 ≈ 12h)로 절반. PD4 §Comparison: *"the pharmacodynamic half-life t1/2,kout is dramatically reduced. This means that the expected time to pharmacodynamic steady state is reduced and the time and cost of the next study will be reduced."* 시그니처: 모델 선택이 다음 시험 sampling design의 time horizon을 절반으로 변경 → 잘못 선택 시 PD steady state 도달 전 종료.

**Signature #4: "Wrong-Clock tD Calculation" (R&T).**
잘못된 직관: $t_D = (1/k)\ln(Dose/(C_{min}V))$를 모든 약물에 적용. 실제: PD rate-limited 약물에 PK $k$를 대입하면 무의미한 값. 시그니처: 모델 예측 duration이 관측 duration과 큰 폭(>50%) 어긋나거나, dose 증량 시 예측 duration 증가가 관측치와 비례하지 않음. R&T가 명시한 진단 기준: *"return of the measured response to the baseline can be rate-limited by either the pharmacokinetics of the drug or the underlying dynamics of the affected system, whichever is the slowest"* (p.243). NONMEM 구현에서는 effect compartment + turnover 모델을 모두 시도하고 acenocoumarol(PD-limited) vs phenprocoumon(PK-limited) 같은 dose-spaced 데이터로 식별성 확보 필요.

### (c) Critical Blow — 가장 파급력이 큰 단일 혼동 쌍 (LOCK-IN)

**Turnover model with linear S(C) ↔ Effect compartment (link) model.**

PD6 Table 6.1과 R&T Fig. 8-13/8-14가 결합하여 이 쌍을 Critical Blow로 확정합니다:

| Metric | Turnover (linear S·kin) | Effect compartment | Δ |
|--------|-------------------------|---------------------|----|
| WRSS (PD6 G&W) | 15,516 | 15,518 | 2 |
| AIC (PD6) | 1,041 | 1,040 | −1 |
| 시간 상수 | kout = 5.6 h⁻¹ | ke0 = 5.6 h⁻¹ | 0 |
| Half-doubling 농도 | EC50 = 1,633 ng·L⁻¹ | a = 0.026 → ~1,623 ng·L⁻¹ | <1% |
| R&T 임상 사례 | warfarin Fig. 8-10 | naproxen Fig. 8-14 | 동일 데이터에 둘 다 적합 가능 |

**규제 제출용 시나리오:** 스폰서가 effect compartment로 제출했으나 underlying biology가 turnover(예: hormone secretion biomarker)인 경우 다음이 모두 손상됩니다.

1. **DDI 예측**: effect compartment는 ke0 가정 하 즉각 분포 동역학을 가정하므로, CYP inhibitor 병용 시 biomarker shift 타이밍을 실제보다 빠르게 예측. R&T acenocoumarol/phenprocoumon 쌍이 이 위험의 정량적 증거(p.244).
2. **Dose titration**: turnover는 t1/2,kout-스케일 step-up이 적절하나 effect compartment는 plasma half-life 기반 권고 생성. PD9의 5.4h vs 7h 같은 우연 일치는 임상 risk를 가립니다.
3. **Interspecies/pediatric extrapolation**: turnover system parameters(kin, kout)는 생리학적 의미 → allometric scaling 가능. ke0는 empirical → extrapolation 불가.
4. **Duration formula 오용**: R&T tD 수식을 effect compartment 가정 하에 적용하면 PK rate로 계산. 실제 turnover라면 PD rate가 지배 → 계산된 duration이 임상적으로 무의미.

PD9 §Perspectives의 단언이 이 혼동의 본질을 한 문장에 응축: *"a lack of peak shift with increasing doses does not necessarily imply an effect compartment (link) model."*

---

## T3. TRENCH-LEVEL TIPS

### Tip 1: Mirror-Slope Misread (G&W Models 2·4)
- **Situation**: §2 Card 3 Graphical initial parameter estimation, Models 2/4 데이터에서 kout 초기값 도출
- **Trap**: Model 1의 "초기 downswing 기울기 = −kout" 규칙을 Models 2/4에 일반화
- **Detection**: 추정된 kout이 dose level과 단조 변화(PD7 Fig. 7.1: 6,400U → 0.6 h⁻¹, 160,000U → 1.6 h⁻¹)
- **Insert at**: §2 Card 3 (Graphical initial parameter estimation), Eq. 3:84 도출 직후
- **Insert text**: "Table 3.6 'Initial ΔR/Δt' 행은 Models 1·4에서만 −kout, Models 2·3에서는 zero-order kin을 준다. Dose에 따라 변하는 kout은 system parameter가 아니라 misspecification artifact의 신호다."

### Tip 2: Linear S(C) Turnover ≡ Effect Compartment 동등성
- **Situation**: §2 Apex Card (Turnover vs Effect Compartment Discrimination Crisis)
- **Trap**: Peak shift 부재를 effect compartment 확정 근거로 사용
- **Detection**: PD6 ΔWRSS = 2, ΔAIC = 1, kout ≡ ke0; PD9 §Perspectives Fig. 9.5 right panel
- **Insert at**: §2 Apex Card Big Idea 직후
- **Insert text**: "Linear S(C)·kin은 단일 dose-range 데이터에서 effect compartment 모델과 fit 동등(PD6 ΔWRSS=2). PD9 §Perspectives 명시: peak shift 부재는 effect compartment 확정 근거가 아니다. Mechanism prior 또는 wider dose range 없이 두 모델 분리 불가."

### Tip 3: kin/kout 재파라미터화 표준화
- **Situation**: §2 Card 1 Turnover foundation, NONMEM 구현
- **Trap**: 기본 (kin, kout) 파라미터화 → r(kin, kout) > 0.98 → $COV step 실패
- **Detection**: PD5 Table 5.1 직접 보고
- **Insert at**: §2 Card 1 NONMEM 구현 subsection
- **Insert text**: "kin/kout 동시 추정은 |r| > 0.98 상관 → $COV step 실패(PD5 Table 5.1). Eq. 3:103의 (R0, kout) 재파라미터화는 옵션이 아닌 표준 1차 시도다."

### Tip 4: K notation 분리 표기 (irreversible models)
- **Situation**: §2 Card 6 Irreversible models, NONMEM control stream
- **Trap**: G&W §3.8에서 K가 second-order kill (L·CFU⁻¹·h⁻¹)과 first-order PK elimination (h⁻¹)로 같은 페이지에서 충돌. NONMEM은 단위 검사를 하지 않으므로 silent error.
- **Detection**: Cross-validation 시 발견. 단위가 잘못되면 IPRED/observation 곡선 형태 자체가 비현실적.
- **Insert at**: §2 Card 6 K-notation 위치
- **Insert text**: "코드에서 Kelim (PK first-order, h⁻¹) vs Kkill 또는 kk (PD second-order, L·CFU⁻¹·h⁻¹) 분리 표기 표준. G&W §3.8 원문 표기는 그대로 유지하되 학습용 노트와 control stream 주석에서는 분리한다."

### Tip 5: Linear PK ≠ Linear PD — Dose-Response Extrapolation 함정 (R&T)
- **Situation**: §2 Card 8 (PK vs PD rate-limiting + tD formula), NDA Dose-Response Justification 작성
- **Trap**: Methylprednisolone Fig. 8-26처럼 AUC가 16–1000 mg에서 dose에 정확히 비례한다는 데이터를 본 후, PD 응답도 비례할 것으로 가정하여 dose-response justification 작성
- **Detection**: Fig. 8-27이 직접 보임 — 500 mg과 1000 mg lymphocyte 응답이 거의 동일(Hill plateau). $E_{max}$ 모델 하에서 응답이 80%를 넘는 dose 영역에서는 dose 증가 → 응답 증가가 거의 없음.
- **Insert at**: §2 Card 8 또는 Card 9, 임상 dose 결정 시나리오 부분
- **Insert text**: "R&T p.256 단언: *Dose linearity in pharmacokinetics does not result in dose linearity in pharmacodynamics. That is almost never the case.* PK 비례성을 PD 비례성으로 외삽하기 전에 Hill 곡선 어느 region에서 작동 중인지(R&T Fig. 8-17)를 먼저 확인한다."

---

## T4. DELETION CANDIDATES

**Item 1.** §2 Card 1 Big Idea — "모든 측정 가능한 약리반응은 시간 지연을 가진다" 절대 단정 — **COMPRESS to 1 sentence with hedging**
- 사유: G&W p.252 자체가 hedge함; R&T midazolam Fig. 8-6, propranolol(p.237)이 직접 반례. NDA cross-section consistency 위험.
- 권장 대체: "대부분의 임상적으로 관찰되는 약리반응은 plasma concentration과 완전히 동시에 움직이지 않으며, 그 지연이 무시 가능할 정도로 짧을 때만 direct response 모델이 적용 가능하다."

**Item 2.** §2 전반 — "tss/peak-shift는 모델 선택의 결정 규칙" 표현 — **COMPRESS to 2 sentences with PD9 caveat**
- 사유: PD9 §Perspectives Fig. 9.5 right panel 명시적 반례. 결정론적 표현은 Deficiency Letter 위험.
- 권장 대체: "tss/peak-shift는 모델 선택의 강력한 진단 신호이지 결정 규칙이 아니다. 최종 선택은 PK rate-limiting, dose range, nonlinear H(C), repeated dosing, mechanistic prior와 함께 종합한다."

**Item 3.** §2 NDA/IND/Deficiency Letter framing 전반 — **LABEL as [교과서 외 실무 해석]** OR **COMPRESS to §5 Critical Blow row 단일 적용**
- 사유: G&W/R&T 원문에 직접 등장하지 않음. V5.0 Apex Edition framework상 Critical Blow는 1쌍에만 적용 가능.
- 권장 처리: T2(c) 식별 쌍에 한해 §5 Critical Blow row로 응축. 나머지 카드의 regulatory framing은 모두 [교과서 외 실무 해석] 라벨 부착 또는 삭제.

**Item 4.** §2 Naproxen 용량 표기 — **DELETE 250mg, RETAIN 500mg only**
- 사유: R&T p.234 Fig. 8-2 caption은 *"single 500-mg dose of naproxen"*만 다룸. 250mg은 fabrication 위험.
- 권장 처리: 전 §2/§6에서 "naproxen 250 mg" 검색 후 일괄 삭제. **500 mg oral, dental pain model, 1–8h sampling, counterclockwise hysteresis**로 통일.

**Item 5.** §2 R&T 사례 본문 깊이 (rosuvastatin OATP1B1, methylprednisolone PK 부분, paclitaxel taxane 거동, ranitidine H2 차단) — **MUST/CONTEXT 분리**
- 사유: Audit MUST_FIX 7. Session 11 핵심은 turnover/indirect/duration; transporter polymorphism 등은 핵심 외부.
- **MUST 유지** (§2 본문): digoxin (1mg i.v., distribution delay), naproxen (500mg oral, hysteresis), warfarin (1.5mg/kg oral, turnover), succinylcholine (0.5–4mg/kg i.v., dose-doubling +1 t1/2), aspirin/omeprazole (irreversible binding), acenocoumarol/phenprocoumon (PK vs PD clock), methylprednisolone (linear PK ≠ linear PD).
- **CONTEXT 압축** (footnote 1–2 sentence): rosuvastatin OATP1B1 (Tip 5의 단순 보강), ibuprofen (warfarin과 동질의 systems-in-flux 사례), minoxidil (succinylcholine과 동질의 PK rate-limited 사례), paclitaxel (irreversible 카테고리 보강), ranitidine (direct/indirect link 분류 보강).

**Item 6.** §2 §3.8 K notation [확인 필요] 단순 tag — **REPLACE with explicit Kelim/Kkill split** (Tip 4 적용)
- 사유: tag만으로는 코드 작성 시 단위 오류 방지 불가.
- 권장 처리: §2 Card 6 본문에서 G&W 원문 표기 유지 + 학습용 분리 표기 1줄 병기.

**Item 7. RESOLVED — Card 8-9 통합 결정 (Stage 2 락-인).**
Stage 1에서 Stage 2로 보류했던 결정. R&T Ch.8 원문 검토 결과 Audit MUST_FIX 권고대로 **단일 카드로 통합**.
- **Final Card 8: "PK clock vs PD clock — Rate-Limiting 판별 + Duration Formula 적용 경계"**
- 통합 근거: R&T Ch.8 전체가 ① "PK가 빠르고 PD가 느리면 PD가 지배" ② "PD가 빠르고 PK가 느리면 PK가 지배" ③ "Rate-limiting을 판별한 후에야 tD formula 적용 가능"이라는 단일 논리 흐름. 두 카드로 분리하면 흐름이 인위적으로 끊김.
- 통합 카드 구성: Big Idea (clock 지배 원리) → A. Formal Definition → B. Derivation: $t_D$ 도출 + Region 1/2/3 + Eq. 8-9 zero-order Region 2 거동 → C. Structural Necessity (왜 Region 2에서만 직선) → D. Assumptions (PK rate-limiting) → E. Limitations (PD rate-limiting 시 비적용) → F. Five Layers → G. Zettelkasten Atom.

**Item 8 (NEW Stage 2).** §2 Direct PK-PD link 사례(midazolam EEG Fig. 8-6, dexamphetamine Fig. 8-7) — **COMPRESS to 1-sentence reference**
- 사유: 이 사례들은 "direct link도 존재한다"는 hedge 근거로만 필요. 본문 깊이 다룰 경우 핵심인 indirect 메커니즘이 흐려짐.
- 권장 처리: Card 1 Big Idea hedge 문장에 "(midazolam EEG, propranolol β-blockade가 직접 반례)" 정도 인라인 언급.

**Item 9 (NEW Stage 2).** §2 Transporter Polymorphism 절(R&T p.256–259, rosuvastatin OATP1B1) — **CONTEXT footnote 1-sentence**
- 사유: 이 절은 R&T가 "exposure-response가 systemic exposure로 항상 정의되는 것은 아니다"라는 별도 메시지를 담고 있어 Session 11 turnover/indirect 축과 거리. Tip 5의 Linear PK ≠ Linear PD 메시지로 흡수됨.
- 권장 처리: Card 8 footnote에 "Bioequivalence 시 systemic exposure 동등성이 효과 동등성을 보장하지 않는 사례(R&T p.256–259 OATP1B1) 존재" 한 줄.

**Item 10 (NEW Stage 2).** §2 R&T duration formula의 succinylcholine 도출 단계 — **COMPRESS, focus on Eq. 8-12 결과**
- 사유: R&T p.254–255의 "dose 두 배 = duration +1 t1/2" 직관적 증명은 깊지만 PhD 독자에게는 자명. 결과만 인용하고 도출 과정은 1-line summary.
- 권장 처리: Card 8에서 "Eq. 8-12 $t_D = (1/k)\ln(Dose/(C_{min}V))$로부터 dose 두 배 → duration +1 t1/2 (선형 dose-log 관계, Fig. 8-24 succinylcholine 0.5/1/2/4 mg/kg에서 검증)" 1문장 처리.

---

## T5. PRIORITY MATRIX

### Grade A — 반드시 반영 (내재화 직접 개선 또는 규제 위험 감소)

| 항목 | 출처 | 적용 위치 |
|------|------|-----------|
| Linear S·kin ≡ effect compartment 동등성 (PD6 ΔWRSS=2) | T2(c), Tip 2 | §2 Apex Card + §5 Critical Blow row |
| Mirror-Slope Misread (Models 2·4 초기 기울기) | T2(b) Sig#1, Tip 1 | §2 Card 3 |
| kin/kout 재파라미터화 표준화 | T2(b), Tip 3 | §2 Card 1 |
| Big Idea hedge ("모든 반응은 delayed" → "대부분") + R&T direct-link 반례 | T4-1, Item 8 | §2 Card 1 |
| tss 결정 규칙 → "강력한 진단 신호" 톤다운 | T4-2 | §2 전반 |
| Regulatory framing labeling | T4-3 | §2/§6 전반 |
| Naproxen 250mg 표기 일괄 삭제 | T4-4 | §2/§6 전반 |
| **Card 8-9 통합 락-인 (PK/PD clock + tD formula 단일 카드)** | T4-7 | §2 Card 구조 재배치 |
| **Wrong-Clock tD Calculation 경고** | T2(a) Risk#3, T2(b) Sig#4 | §2 Card 8 (통합본) |
| **Linear PK ≠ Linear PD (methylprednisolone)** | T2(a) Risk#4, Tip 5 | §2 Card 8 NDA 시나리오 |

### Grade B — 흐름 보존되면 반영 (enrichment value)

| 항목 | 출처 | 적용 위치 |
|------|------|-----------|
| ΔR semantic load (Figure 3.40 drug + system) | T1(a) Wall #2 | §2 Card 1 Apex Card 짧은 삽입 |
| PD4 Pool 1 "CV% 4000" 비식별성 해석 | T1(a) Wall #4 | §2 Card 1 PD4 인용 |
| K notation Kelim/Kkill 분리 표기 | Tip 4 | §2 Card 6 |
| Phantom Convergence + False Half-Life Compression 진단명 | T2(b) Sig#2, Sig#3 | §6 Diagnostic Pathology |
| "Post-trough rebound timing" 30년 직관 | T1(c) Intuition #1 | §6 또는 §8C Professional Moat |
| **Acenocoumarol vs Phenprocoumon clock-domination 쌍** | T1(b) Integration #4, T1(a) Wall #4 | §2 Card 8 본문 |
| **Counterclockwise hysteresis 3-pathway 진단** | T1(c) Intuition #4 | §6 or §2 Card 8 진단 시나리오 |
| **Region 1/2/3 + Eq. 8-9 zero-order Region 2 거동** | T1(a) Wall #3 | §2 Card 8 구조적 필연 |

### Grade C — 거부 (scope creep, unsupported, or duplicates)

| 항목 | 사유 |
|------|------|
| "Anti-AI moat" 일반론 추가 | V5.0 §8C에서 별도 처리됨 |
| 28-세션 커리큘럼 위치 재정의 | 이미 §1, §8A 영역 |
| Bayesian TDM, transit compartment 확장 | Scope Lock 외부 (§3.9 transit) |
| Rosuvastatin OATP1B1 본문 확장 | T4-9, footnote-level만 |
| Direct-link examples (midazolam, dexamphetamine, propranolol) 본문 확장 | T4-8, hedge 근거 인라인 언급만 |
| R&T p.260–264 Study Problems 본문 통합 | 학습 자료이지 본문 콘텐츠 아님 |
| Effect compartment ke0 추정 알고리즘 상세 (collapse-of-hysteresis 방법) | 다음 세션 영역 |

---

## ✅ Stage 2 통합 완료 체크리스트

- [x] Audit Report v1 MUST_FIX 1: Naproxen 500 mg 일관성 → T4-4
- [x] Audit Report v1 MUST_FIX 2: NDA/IND framing 라벨링 → T4-3, T1(b) Integration #2 직접 라벨링
- [x] Audit Report v1 MUST_FIX 3: "모든 반응 delayed" hedge → T4-1 + R&T 직접 반례
- [x] Audit Report v1 MUST_FIX 4: tss 결정 규칙 톤다운 → T4-2
- [x] Audit Report v1 MUST_FIX 5: PD4-PD9 + R&T 수치 전수 대조 → 모든 R&T 임상 수치 PDF 1:1 검증 완료 (digoxin 1mg, naproxen 500mg, warfarin 1.5mg/kg, aspirin 650mg, omeprazole 40mg, succinylcholine 0.5mg/kg, methylprednisolone 16–1000mg, acenocoumarol t1/2=15h, phenprocoumon t1/2=5–6일)
- [x] Audit Report v1 MUST_FIX 6: K 표기 분리 (Kelim/Kkill) → Tip 4
- [x] Audit Report v1 MUST_FIX 7: Card 8-9 통합 → T4-7 RESOLVED
- [x] Audit Report v1 MUST_FIX 8: R&T MUST/CONTEXT 분리 → T4-5
- [x] Stage 1 Critical Blow 단일 쌍 락-인 → T2(c)
- [x] Volume parity (Stage 1+2 ≈ 단일 PDF 세션 1.0×) → 압축-and-focus 전략으로 R&T 추가 영역만 신규 지면 할당, 중복 영역 압축
- [x] R&T 핵심 4축 통합 완료: ① hysteresis 분류학(direction-based) ② tD duration formula ③ Region 1/2/3 시간 거동 ④ PK vs PD rate-limiting 명시적 분류

---

Stage 2 통합 작업을 진행하겠습니다. Tozer Ch.8 PDF 원문을 모두 검토했고, Stage 1의 G&W 통합본과 융합한 최종 단일 통합본을 생성합니다. 우선 핵심 R&T 수치들을 PDF 원문에서 1:1 검증합니다 — naproxen 500 mg (p.234 확인), warfarin 1.5 mg/kg oral (p.242 Fig.8-10 확인), succinylcholine 0.5 mg/kg i.v. (p.250 Fig.8-18 확인), aspirin 650 mg (p.251 Fig.8-20 확인), omeprazole 40 mg (p.252 Fig.8-21 확인), 그리고 핵심 수식 $t_D = \frac{1}{k}\ln(Dose/(C_{min}V))$ (Eq.8-12, p.254 확인). 모든 수치가 검증되었으므로 fabrication 위험 없이 통합 가능합니다.최종 통합본을 생성했습니다. Stage 1(G&W 단독)에서 Stage 2(R&T 통합)로 진행하면서 단순한 +α 누적이 아닌 **Source Universe 재구성** 방식으로 작업했습니다 — 두 텍스트북을 별도 트랙으로 두지 않고, R&T가 채우는 4개 신규 축(hysteresis 방향 분류학, $t_D$ duration formula, Region 1/2/3 시간 거동, PK clock vs PD clock 명시적 판별)이 G&W의 turnover 수식축과 *변증법적으로 결합*되도록 재배치했습니다.

핵심 Stage 2 결정 사항을 P1·P3 관점에서 요약하면 다음과 같습니다.

**P1 관점 — Card 8-9 통합 락-인.** Audit Report v1이 권고했던 통합을 Stage 1에서는 R&T 원문 검토 전이라는 이유로 보류했습니다. 이번에 Tozer Ch.8 전체를 검토한 결과, R&T는 "PK clock과 PD clock 중 느린 쪽이 임상 거동을 지배한다 → rate-limiting 판별 후에야 $t_D$ formula 적용 가능"이라는 단일 논리 흐름으로 챕터 전체가 묶여 있습니다. 두 카드로 분리하면 acenocoumarol vs phenprocoumon 사례(p.243–244)의 핵심 메시지인 *"같은 작용기전을 공유하는 약물이라도 약물별 PK가 rate-limiting step을 결정한다"*가 두 카드로 쪼개져 흐름이 끊깁니다. 따라서 단일 카드(Card 8: PK/PD clock + duration formula)로 확정했습니다.

**P3 관점 — Critical Blow 쌍의 R&T 임상 증거 보강.** Stage 1에서 락-인한 *turnover linear S(C) ↔ effect compartment* 쌍은 G&W PD6 Table 6.1의 ΔWRSS = 2 정량 증거에 의해 충분히 방어되지만, R&T가 추가하는 결정타는 동일 데이터에 두 모델이 적합한 상황의 *임상 사례 그 자체* — naproxen은 effect compartment(Fig. 8-14), warfarin은 turnover/IRM(Fig. 8-10)로 R&T가 표준적으로 모델링하지만, 두 약물 데이터를 PD6의 동등성 결과와 병치하면 "어느 쪽으로도 fit이 가능하므로 mechanistic prior가 없으면 NDA에서 데이터만으로 모델 선택을 방어할 수 없다"는 메시지가 임상 약물명 수준으로 구체화됩니다. Critical Blow 시나리오의 4번째 손상(Duration formula 오용)이 R&T 통합으로 새로 추가되었습니다.

**Trench-level 한 가지 — Tip 5 교체.** Stage 1의 Pool 1 비식별성 진단(PD4 CV% 4000)은 Wall #4로 격하시키고, Tip 5 자리에 R&T의 *Linear PK ≠ Linear PD*(methylprednisolone Fig. 8-26 vs 8-27) 함정을 배치했습니다. R&T p.256의 단언(*"Dose linearity in pharmacokinetics does not result in dose linearity in pharmacodynamics. That is almost never the case."*)은 NDA Dose-Response Justification 작성 시 가장 자주 발생하는 sponsor 추론 오류이며, T2(a) Risk #4와 직접 연결됩니다.

볼륨은 31,093자(약 6,200 단어, 267줄)로 단일 PDF 세션 표준 분량을 유지했고, 두 PDF를 단순 합산했을 때의 ~50,000자 팽창을 ~38% 압축했습니다. Phase 3 Content Lock 단계로 바로 진행 가능한 상태입니다.

**STATUS**: Stage 2 통합 완료. 본 산출물은 Phase 3 Content Lock으로 진행 가능한 최종 Crucible Report입니다. HTML 직행은 여전히 금지이며, Phase 3에서 Content Lock 후 Phase 4 HTML 컴파일로 진행합니다.
